import {ref,watch,onBeforeUnmount} from 'vue'
import {withBase} from 'vitepress'
import {useLecture} from '../../navigation/index.mjs'
import {exerciseAssetPath,resolveExerciseHtml} from '../services/chapter-exercises.mjs'
export function useChapterExercises(chapter) {
 const {part}=useLecture(),groups=ref([]),selected=ref(''),html=ref(''),state=ref('idle')
 let request,version=0,loadedChapter=null,loadedGroup=''
 async function load(){
  if(part.value!=='bai-tap'||import.meta.env.SSR)return
  if(loadedChapter!==chapter.value){groups.value=[];selected.value='';html.value='';loadedGroup='';loadedChapter=chapter.value}
  if(state.value==='ready'&&loadedGroup===selected.value&&html.value)return
  const current=++version
  request?.abort();request=new AbortController();state.value='loading';html.value=''
  try{
   if(!groups.value.length){
    const response=await fetch(withBase(exerciseAssetPath(chapter.value)),{signal:request.signal})
    if(!response.ok)throw Error('Cannot load exercise index')
    const data=await response.json()
    if(current!==version)return
    if(data.chapter!==chapter.value||!Array.isArray(data.groups)||!data.groups.length)throw Error('Invalid exercise index')
    groups.value=data.groups;selected.value=data.groups[0].id
   }
   const group=groups.value.find(g=>g.id===selected.value)
   if(!group)throw Error('Unknown exercise group')
   const response=await fetch(withBase(exerciseAssetPath(chapter.value,group.id+'.json')),{signal:request.signal})
   if(!response.ok)throw Error('Cannot load exercise group')
   const data=await response.json()
   if(current!==version)return
   if(data.id!==group.id||typeof data.html!=='string')throw Error('Invalid exercise group')
   html.value=resolveExerciseHtml(data.html,withBase('/'));loadedGroup=group.id;state.value='ready'
  }catch(error){if(current===version&&error.name!=='AbortError')state.value='error'}
 }
 function select(id){if(!groups.value.some(group=>group.id===id)||selected.value===id)return;selected.value=id;load()}
 function step(delta){const i=groups.value.findIndex(g=>g.id===selected.value),target=groups.value[i+delta];if(target)select(target.id)}
 watch([part,chapter],()=>{if(part.value==='bai-tap')load();else{version++;request?.abort()}},{immediate:true})
 onBeforeUnmount(()=>{version++;request?.abort()})
 return{groups,selected,html,state,select,step,retry:load}
}
