import {readFile,writeFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import {composeLegacySupplement,canonicalPythonBlocks} from './build/essay-supplements.mjs'

const hash=value=>createHash('sha256').update(value).digest('hex')
const base='raw_materials/xu-ly-du-lieu/exam'
let count=0
for(let i=1;i<=8;i++){
  const n=String(i).padStart(2,'0'),file=`${base}/essay-solutions/bai-${n}.json`
  const authored=JSON.parse(await readFile(file,'utf8'))
  const bank=JSON.parse(await readFile(`${base}/banks/bai-${n}.json`,'utf8'))
  const reviews=JSON.parse(await readFile(`${base}/reviews/bai-${n}.json`,'utf8'))
  const codeKeys=canonicalPythonBlocks([...authored.items.map(x=>x.markdown),...bank.questions.filter(q=>q.kind==='essay').map(q=>q.answerMarkdown)])
  for(const item of authored.items){
    const previous=bank.questions.find(q=>q.id===item.id),review=reviews.items.find(q=>q.id===item.id)
    if(!previous||previous.kind!=='essay')throw Error(item.id)
    const explanation=composeLegacySupplement(item.markdown,previous.answerMarkdown,review?.explanationMarkdown||'',codeKeys)
    if(!explanation||/Hướng dẫn chấm|Ý cần đạt|Điểm tối đa|\*\*Chấm\s+\d/i.test(explanation))throw Error('Invalid supplement '+item.id)
    item.supplementMarkdown=explanation
    item.supplementSource={answerSha256:hash(previous.answerMarkdown),reviewSha256:hash(review?.explanationMarkdown||'')}
    count++
  }
  await writeFile(file,JSON.stringify(authored,null,2)+'\n')
}
if(count!==184)throw Error('Incomplete essay supplements')
console.log(`Prepared ${count} detailed explanations after the current primary answers.`)
