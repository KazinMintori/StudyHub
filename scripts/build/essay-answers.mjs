import assert from 'node:assert/strict'
import {readFile} from 'node:fs/promises'
import {createHash} from 'node:crypto'
import path from 'node:path'

const hash=value=>createHash('sha256').update(value).digest('hex')
export async function loadEssayAnswers(root) {
  const base=path.join(root,'raw_materials/xu-ly-du-lieu/exam')
  const manifest=JSON.parse(await readFile(path.join(base,'essay-source-manifest.json'),'utf8'))
  assert.equal(manifest.files.length,8)
  const lessons=new Map(),questions=new Map()
  for(const source of manifest.files) {
    const bytes=await readFile(path.join(base,source.path))
    assert.equal(bytes.length,source.bytes,source.path)
    assert.equal(hash(bytes),source.sha256,source.path)
    const text=bytes.toString('utf8').replace(/^\uFEFF/,'').replace(/\r\n?/g,'\n')
    const headings=[...text.matchAll(/^###\s+(B\d+-(?:MR|R)?\d+)\s*$/gm)]
    const expected=headings.map((h,i)=>({id:h[1],markdown:text.slice(h.index+h[0].length,headings[i+1]?.index??text.length).trim()}))
    const authored=JSON.parse(await readFile(path.join(base,`essay-solutions/bai-${source.lesson}.json`),'utf8'))
    assert.equal(authored.sourceSha256,source.sha256)
    assert.deepEqual(authored.items.map(({id,markdown})=>({id,markdown})),expected,`${source.lesson}: complete current source answers`)
    lessons.set(source.lesson,{items:authored.items,inputSha256:hash(JSON.stringify(authored))})
    for(const item of authored.items) {
      assert(!questions.has(item.id),item.id)
      assert(!/Hướng dẫn chấm|Ý cần đạt|Điểm tối đa/i.test(item.markdown),`${item.id}: no grading guide`)
      questions.set(item.id,item)
    }
  }
  assert.equal(questions.size,184)
  return {lessons,questions}
}
export function renderEssayAnswer(entry,render) {
  assert(entry?.markdown.trim(),'Updated essay answer is required')
  // A supplement, when authored, follows the source answer without a generic label.
  return render(entry.markdown,true)+(entry.supplementMarkdown?render(entry.supplementMarkdown,true):'')
}
