<script setup>
import {computed} from 'vue'
import {useChapterExercises} from '../controllers/useChapterExercises.js'
const props=defineProps({chapter:{type:Number,required:true}})
const {groups,selected,html,state,select,step,retry}=useChapterExercises(computed(()=>props.chapter))
const index=computed(()=>groups.value.findIndex(g=>g.id===selected.value))
</script>
<template>
 <section class="chapter-exercise-groups" aria-label="Bài tập cuối chương">
  <h2>Bài tập cuối chương</h2>
  <div v-if="groups.length" class="exercise-group-controls">
   <label for="exercise-group-select">Nhóm bài</label>
   <select id="exercise-group-select" :value="selected" @change="select($event.target.value)">
    <option v-for="group in groups" :key="group.id" :value="group.id">{{group.title}}</option>
   </select>
   <div class="exercise-group-steps">
    <button class="study-button" :disabled="index===0" @click="step(-1)">Nhóm trước</button>
    <span>{{index+1}} / {{groups.length}}</span>
    <button class="study-button" :disabled="index===groups.length-1" @click="step(1)">Nhóm sau</button>
   </div>
  </div>
  <p v-if="state==='loading'" role="status">Đang tải bài tập…</p>
  <div v-else-if="state==='error'" role="alert">
   <p>Chưa tải được nhóm bài tập. Hãy thử lại.</p>
   <button class="study-button" @click="retry">Thử lại</button>
  </div>
  <div v-else-if="state==='ready'" class="exercise-group-content" v-html="html"></div>
 </section>
</template>
<style scoped>
.exercise-group-controls{display:grid;gap:var(--space-3);margin:var(--space-4) 0}
label{font-weight:600}
select{width:100%;min-width:0;min-height:44px;padding:var(--space-2);border:1px solid var(--rule);border-radius:var(--radius);background:var(--paper);color:var(--ink);font:inherit}
.exercise-group-steps{display:flex;align-items:center;justify-content:space-between;gap:var(--space-2);flex-wrap:wrap}
.exercise-group-steps span{white-space:nowrap}
.exercise-group-content{min-width:0}
</style>
