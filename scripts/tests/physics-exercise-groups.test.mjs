import test from 'node:test'
import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import {staticMathPlugin} from '../static-math-plugin.mjs'
import {splitPhysicsExercises} from '../content/physics-exercise-groups.mjs'
import {exerciseAssetPath,resolveExerciseHtml} from '../../src/features/lecture/services/chapter-exercises.mjs'
import {physicsExerciseFiles,validatePhysicsExerciseIds,publishedPhysicsExerciseChapters,physicsExerciseConfigs} from '../content/physics-exercise-config.mjs'
import {physics1Course} from '../../docs/.vitepress/physics-courses.mjs'
const problem=id=>'### '+id+'\n\nĐề bài đầy đủ.\n\n<details><summary>Xem lời giải chi tiết</summary>\n\nLời giải.\n\n</details>\n'
test('Grouping retains each prompt with its entire closed solution',()=>{
 const source='## Bài tập\n\n'+[1,2,3,4,5,6,7].map(n=>problem('9.'+n)).join('\n')
 const groups=splitPhysicsExercises(source,{chapter:9,kind:'numbered-a',size:3})
 assert.deepEqual(groups.map(g=>g.ids),[['9.1','9.2','9.3'],['9.4','9.5','9.6'],['9.7']])
 assert.equal(groups.flatMap(g=>g.markdown.match(/<\/details>/g)||[]).length,7)
 assert.throws(()=>splitPhysicsExercises(source.replace('</details>',''),{chapter:9,kind:'numbered-a'}),/closed solution/)
 assert.throws(()=>splitPhysicsExercises(problem('9.1')+problem('9.1'),{chapter:9,kind:'numbered-a'}),/Duplicate/)
})
test('Reading passage follows every group containing its questions',()=>{
 const source=problem('9.91')+'\n## Đọc hiểu khoa học: Đoạn đọc\n\nNội dung đoạn đọc.\n\n'+problem('9.92')+problem('9.93')
 const groups=splitPhysicsExercises(source,{chapter:9,kind:'numbered-b',size:1})
 assert.doesNotMatch(groups[0].markdown,/Nội dung đoạn đọc/)
 assert.match(groups[1].markdown,/Nội dung đoạn đọc/)
 assert.match(groups[2].markdown,/Nội dung đoạn đọc/)
 const combined=splitPhysicsExercises(source,{chapter:9,kind:'numbered-b',size:3})[0].markdown
 assert(combined.indexOf('### 9.91')<combined.indexOf('Nội dung đoạn đọc'))
 assert(combined.indexOf('Nội dung đoạn đọc')<combined.indexOf('### 9.92'))
})
test('Reading passages follow their actual question boundary in other chapters',()=>{
 const source=problem('18.83')+'\n## Đọc hiểu khoa học: Đoạn thứ nhất\n\nNội dung A.\n\n'
  +problem('18.84')+problem('18.85')+'\n## Đọc hiểu khoa học: Đoạn thứ hai\n\nNội dung B.\n\n'+problem('18.86')
 const groups=splitPhysicsExercises(source,{chapter:18,kind:'numbered-b',size:1})
 assert.doesNotMatch(groups[0].markdown,/Nội dung [AB]/)
 assert.match(groups[1].markdown,/Nội dung A/)
 assert.match(groups[2].markdown,/Nội dung A/)
 assert.match(groups[3].markdown,/Nội dung B/)
 assert.doesNotMatch(groups[3].markdown,/Nội dung A/)
 const prefix='## Đọc hiểu khoa học: Bối cảnh\n\nNội dung trước câu đầu.\n\n'+problem('18.86')+problem('18.87')
 const prefixGroups=splitPhysicsExercises(prefix,{chapter:18,kind:'numbered-b',size:1})
 for(const group of prefixGroups)assert.equal(group.markdown.match(/Nội dung trước câu đầu/g).length,1)
})
test('A bridge heading may have a descriptive title after its identifier',()=>{
 const source=problem('Bài tập cầu nối: Khí trên Europa')
 const groups=splitPhysicsExercises(source,{chapter:18,kind:'bridge'})
 assert.deepEqual(groups[0].ids,['Bài tập cầu nối'])
 assert.match(groups[0].markdown,/Khí trên Europa/)
})
test('Chapter18 grouping retains exactly its actual130 source prompts',()=>{
 assert.equal(physicsExerciseFiles(18)[2][1],'11-bai-tap-001-044.md')
 assert.equal(physicsExerciseFiles(18)[3][1],'12-bai-tap-045-087.md')
 const ids=[
  ...[4,7,8].flatMap(section=>[1,2,3,4].map(n=>'VP18.'+section+'.'+n)),
  ...Array.from({length:30},(_,i)=>'Q18.'+(i+1)),
  ...Array.from({length:87},(_,i)=>'18.'+(i+1)),
  'Bài tập cầu nối'
 ]
 assert.equal(validatePhysicsExerciseIds(18,[{ids}]),130)
 assert.throws(()=>validatePhysicsExerciseIds(18,[{ids:ids.filter(id=>id!=='18.87')}]),/numbered/)
 assert.throws(()=>validatePhysicsExerciseIds(18,[{ids:ids.filter(id=>id!=='Q18.30')}]),/discussion/)
 assert.throws(()=>validatePhysicsExerciseIds(18,[{ids:[...ids,'VP18.8.4']}]),/guided/)
 assert.throws(()=>physicsExerciseFiles(45),/Unconfigured/)
 for(const chapter of [9,10,11,17,18,19,20])assert(publishedPhysicsExerciseChapters.includes(chapter))
})
test('Exercise assets reject traversal and preserve the GitHub Pages base',()=>{
 assert.equal(exerciseAssetPath(9,'numbered-a-01.json'),'/physics-exercises/ch09/numbered-a-01.json')
 assert.throws(()=>exerciseAssetPath(9,'../../secret.json'))
 assert.throws(()=>exerciseAssetPath(NaN))
 const html='<img src="/vat-ly-1/x.png"><a href="/wiki/x.html">X</a><a href="https://example.com">Y</a>'
 assert.equal(resolveExerciseHtml(html,'/StudyHub/'),'<img src="/StudyHub/vat-ly-1/x.png"><a href="/StudyHub/wiki/x.html">X</a><a href="https://example.com">Y</a>')
})

test('Ready Physics1 chapters have their exercise data enabled for GitHub generation',()=>{
 for(const lesson of physics1Course.lessons){
  if(lesson.status==='ready'&&physicsExerciseConfigs[lesson.sourceChapter]){
   assert(publishedPhysicsExerciseChapters.includes(lesson.sourceChapter),'Missing generated exercises for '+lesson.slug)
  }
 }
 assert.equal(physicsExerciseFiles(4)[0][1],'parent-09-luyen-tap-huong-dan.md')
 const ids=[
  ...[1,4,5].flatMap(section=>[1,2,3,4].map(n=>'VP4.'+section+'.'+n)),
  ...Array.from({length:38},(_,i)=>'Q4.'+(i+1)),
  ...Array.from({length:60},(_,i)=>'4.'+(i+1)),
  'Bài tập cầu nối'
 ]
 assert.equal(validatePhysicsExerciseIds(4,[{ids}]),111)
 assert.throws(()=>validatePhysicsExerciseIds(4,[{ids:ids.filter(id=>id!=='4.60')}]),/numbered/)
})
test('Pre-rendered groups contain real SVG math; ordinary pages retain Vue bindings',()=>{
 const make=option=>{const md=new MarkdownIt().use(mathjax);md.use(staticMathPlugin,option);return md}
 assert.match(make().renderInline('$x^2$'),/v-html=/)
 const html=make({vueBinding:false}).renderInline('$x^2$')
 assert.match(html,/<svg/)
 assert.doesNotMatch(html,/v-html=/)
})
