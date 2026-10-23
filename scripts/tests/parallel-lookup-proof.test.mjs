import test from 'node:test'
import assert from 'node:assert/strict'
import { createMarkdownRenderer } from 'vitepress'
import config from '../../docs/.vitepress/config.mjs'
import { filterParallelCheatsheet } from '../../src/features/lecture/services/parallel-cheatsheet.mjs'
import { fileURLToPath } from 'node:url'

test('Proofs receive a dedicated class without marking ordinary solutions',async()=>{
 const md=await createMarkdownRenderer(fileURLToPath(new URL('../../docs/',import.meta.url)),config.markdown)
 const html=md.render('::: proof Tính duy nhất\n\nLập luận đầy đủ.\n\n:::\n\n::: solution\n\nLời giải.\n\n:::')
 assert.match(html,/<details class="[^"]*\bproof\b[^"]*"><summary>Chứng minh: Tính duy nhất<\/summary>/)
 assert.match(html,/<summary>Lời giải<\/summary>/)
 assert.equal((html.match(/\bproof\b/g)||[]).length,1)
 assert(!html.includes('Lập luận đầy đủ. Chứng minh'))
})
test('Parallel lookup matches Vietnamese accents and preserves complete source items',()=>{
 const formula={name:'Mômen động lượng',formulaRows:[{label:'Bảo toàn',formula:'L_i=L_f'}],description:'Không có mômen ngoại lực'}
 const table={headers:['Chất','Hệ số'],rows:[['Đồng','385'],['Thép','50']]}
 const data={sections:[{id:'rotation',title:'Vật rắn',items:[formula,{name:'Nhiệt lượng',formula:'Q=mcT'}]},{id:'materials',title:'Vật liệu',table}]}
 const result=filterParallelCheatsheet(data,'momen dong')
 assert.equal(result.length,1);assert.equal(result[0].items[0],formula);assert.equal(result[0].items.length,1)
 assert.equal(filterParallelCheatsheet(data,'bao toan')[0].items[0],formula)
 assert.deepEqual(filterParallelCheatsheet(data,'dong')[1].table.rows,[['Đồng','385']])
 assert.deepEqual(filterParallelCheatsheet(data,'không tồn tại'),[])
 assert.equal(data.sections[0].items.length,2)
})
