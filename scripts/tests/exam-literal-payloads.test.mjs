import test from 'node:test'
import assert from 'node:assert/strict'
import {createExamMarkdownRenderer} from '../build/exam-markdown.mjs'
import {htmlCodeText} from '../build/exam-code-integrity.mjs'

test('JSON, empty sets and named sets remain visible exam data',async()=>{
  const render=await createExamMarkdownRenderer(process.cwd(),{linkConcepts:false})
  const source='JSON cần xem.\n{"sentiment":"negative","aspects_negative":["noise"]}\n\n| ID | Gold |\n|---|---|\n| 1 | {host, noise} |\n| 2 | {} |'
  const html=render(source,true)
  assert(htmlCodeText(html).includes('{"sentiment":"negative","aspects_negative":["noise"]}'))
  assert(htmlCodeText(html).includes('{host, noise}'))
  assert(htmlCodeText(html).includes('{}'))
  assert(!/sentiment:negative=|<td host/.test(html))
})
