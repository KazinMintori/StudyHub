import assert from 'node:assert/strict'
import {readFile,writeFile} from 'node:fs/promises'
import path from 'node:path'
import {fileURLToPath} from 'node:url'
import {createHash} from 'node:crypto'
import {createExamMarkdownRenderer} from './exam-markdown.mjs'
import {assertCodePreserved} from './exam-code-integrity.mjs'

const hash=value=>createHash('sha256').update(value).digest('hex')
export async function renderDataExamAdditions(root=fileURLToPath(new URL('../../',import.meta.url))) {
  const base=path.join(root,'raw_materials/xu-ly-du-lieu/exam')
  const manifestPath=path.join(base,'additions-20261106.json')
  let manifest
  try {manifest=JSON.parse(await readFile(manifestPath,'utf8'))}
  catch(error){if(error.code==='ENOENT')return;throw error}
  const render=await createExamMarkdownRenderer(root,{linkConcepts:false})
  const destination=path.join(root,'src/content/courses/xu-ly-du-lieu/exam')
  const catalog=JSON.parse(await readFile(path.join(destination,'catalog.json'),'utf8'))
  const audits=[]
  for(const source of manifest.lessons) {
    const bank=JSON.parse(await readFile(path.join(base,`banks/bai-${source.lesson}.json`),'utf8'))
    const review=JSON.parse(await readFile(path.join(base,`reviews/bai-${source.lesson}.json`),'utf8'))
    const feedback=new Map(review.items.map(item=>[item.id,item]))
    assert.equal(feedback.size,bank.questions.length)
    const questions=bank.questions.map(question=>{
      const item=feedback.get(question.id)
      assert(item && ['confirmed','corrected'].includes(item.verdict),`Unresolved ${question.id}`)
      const context=item.promptContextMarkdown||question.promptContextMarkdown
      const promptHtml=render((context?context+'\n\n':'')+question.promptMarkdown,true)
      assertCodePreserved(question.promptMarkdown,promptHtml,question.id)
      const correctKey=item.correctKey||question.correctKey
      const options=question.options.map(option=>{
        assert(item.optionExplanations[option.key]?.trim(),`${question.id}/${option.key}`)
        const html=render(option.markdown,true)
        assertCodePreserved(option.markdown,html,`${question.id}/${option.key}`)
        return {key:option.key,html,explanationHtml:render(item.optionExplanations[option.key],true)}
      })
      let solution
      if(question.kind==='quiz') {
        const primary=question.answerMarkdown.split(/^\*\*Vì sao các phương án|^- \*\*[A-D](?: sai)?[:.]/m)[0].trim()
        const answer=correctKey===question.correctKey?primary:`Đáp án đúng là **${correctKey}**. ${item.correctionReason}`
        solution=`${answer}\n\n${item.rationaleMarkdown}\n\n`+
          options.map(option=>`### Phương án ${option.key}\n\n${item.optionExplanations[option.key]}`).join('\n\n')
      } else {
        solution=question.answerMarkdown+(item.supplementMarkdown?.trim()?'\n\n'+item.supplementMarkdown:'')
      }
      assert(!/\*\*(?:Chấm|Kỹ năng|Nguồn|Mức dự kiến|Thời gian)/.test(solution),question.id)
      const answerHtml=render(solution)
      assertCodePreserved(solution,answerHtml,`${question.id}/answer`)
      return {id:question.id,kind:question.kind,group:question.group,promptHtml,options,
        correctKey:question.kind==='quiz'?correctKey:null,answerHtml}
    })
    const compiled={lesson:source.lesson,title:source.title,questions}
    await writeFile(path.join(destination,`bai-${source.lesson}.json`),JSON.stringify(compiled,null,2)+'\n')
    const record={lesson:source.lesson,title:source.title,total:questions.length,
      quiz:questions.filter(q=>q.kind==='quiz').length,essay:questions.filter(q=>q.kind==='essay').length}
    const index=catalog.findIndex(item=>item.lesson===source.lesson)
    if(index<0)catalog.push(record);else catalog[index]=record
    audits.push({lesson:source.lesson,sourceQuestionIds:source.sourceQuestionIds,
      renderedQuestionIds:questions.map(q=>q.id),inputSha256:hash(JSON.stringify({bank,review})),
      contentSha256:hash(JSON.stringify(compiled)),...record})
  }
  catalog.sort((a,b)=>Number(a.lesson)-Number(b.lesson))
  await writeFile(path.join(destination,'catalog.json'),JSON.stringify(catalog,null,2)+'\n')
  await writeFile(path.join(base,'additions-render-coverage.json'),JSON.stringify(audits,null,2)+'\n')
  console.log(`Rendered ${audits.reduce((sum,x)=>sum+x.total,0)} new questions with exact code and detailed feedback`)
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))await renderDataExamAdditions()
