import test from 'node:test'
import assert from 'node:assert/strict'
import {mathRelationLayoutIssues} from '../verification/math-relation-layout.mjs'
import {splitPhysicsExercises} from '../content/physics-exercise-groups.mjs'
const display=tex=>'$$\n'+tex+'\n$$'
test('Rejects dangling left sides after implications or independent equations',()=>{
 for(const connector of ['implies','iff','qquad','quad']){
  const bad=display(String.raw`\begin{aligned}
A &= B ${String.fromCharCode(92)+connector} C \\
&= D.
\end{aligned}`)
  assert.equal(mathRelationLayoutIssues(bad)[0]?.kind,'dangling-secondary-lhs')
  const source='### 9.1\n\nĐề bài.\n\n<details><summary>Xem lời giải</summary>\n\n'+bad+'\n\n</details>'
  assert.throws(()=>splitPhysicsExercises(source,{chapter:9,kind:'numbered-a'}),/Malformed math relation layout/)
 }
})
test('Keeps complete chains, independent equations and negative left sides',()=>{
 const good=display(String.raw`\begin{aligned}
A &= B \\
&= C, \\
-I_1 &= I_2-I_3.
\end{aligned}`)
 assert.deepEqual(mathRelationLayoutIssues(good),[])
 assert.deepEqual(mathRelationLayoutIssues(display(String.raw`A=B\implies C=D`)),[])
 assert.deepEqual(mathRelationLayoutIssues(display(String.raw`\begin{aligned}&A=B,\\&C=D.\end{aligned}`)),[])
})
test('Rejects empty right sides and ignores fenced code examples',()=>{
 const bad=display(String.raw`\begin{aligned}
A &= \\
B.
\end{aligned}`)
 assert.equal(mathRelationLayoutIssues(bad)[0]?.kind,'empty-right-side-before-break')
 assert.deepEqual(mathRelationLayoutIssues('```tex\n'+bad+'\n```'),[])
})
