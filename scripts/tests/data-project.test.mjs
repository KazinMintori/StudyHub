import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { buildThemeConfig } from '../../src/features/course/services/build-navigation.mjs'

test('Data project follows exam navigation with two distinct sections', () => {
  const theme=buildThemeConfig({courseCatalog:[{id:'xu-ly-du-lieu',name:'Dữ liệu',lessons:[]},{id:'other',name:'Khác',lessons:[]}],wikiGroups:[],concepts:{}})
  const items=theme.sidebar['/xu-ly-du-lieu/'][0].items
  assert.equal(items[items.findIndex(item=>item.text==='Ôn thi')+1].text,'Bài tập lớn')
  assert.deepEqual(items.at(-1).items.map(item=>item.text),['Đề bài tập lớn','Ví dụ thực hành'])
  assert(!theme.sidebar['/other/'][0].items.some(item=>item.text==='Bài tập lớn'))
})

test('City roster preserves every source city, exact path, four dates and monthly marker', async () => {
  const html=await readFile('raw_materials/xu-ly-du-lieu/bai-tap-lon/project-airbnb.html','utf8')
  const cities=JSON.parse(await readFile('src/content/courses/xu-ly-du-lieu/project/cities.json','utf8'))
  const decode=text=>text.replace(/&amp;/g,'&').replace(/&oacute;/g,'ó')
  const source=[...html.matchAll(/<article class="city">([\s\S]*?)<\/article>/g)].map(match=>{
    const body=match[1]
    return {name:decode(body.match(/<strong>(.*?)<\/strong>/)[1]),dataRoot:decode(body.match(/<code class="city-path">(.*?)<\/code>/)[1]),snapshots:[...body.matchAll(/<li>(\d{4}-\d{2}-\d{2})<\/li>/g)].map(m=>m[1]),monthly:body.includes('hàng tháng')}
  })
  assert.equal(cities.length,26)
  assert.deepEqual(cities.map(({name,dataRoot,snapshots,monthly})=>({name,dataRoot,snapshots,monthly})),source)
  assert.equal(new Set(cities.map(c=>c.dataRoot)).size,26)
  assert(cities.every(city=>city.snapshots.length===4))
})

test('Project brief includes required deliverables while worked example remains reserved', async () => {
  const brief=await readFile('docs/xu-ly-du-lieu/bai-tap-lon/index.md','utf8')
  const practice=await readFile('docs/xu-ly-du-lieu/bai-tap-lon/thuc-hanh.md','utf8')
  for(const token of ['20/09/2026','22/11/2026','5–8','100','10 trang','50 MB','AI_USAGE.md','requirements.txt','qa_report.csv','neighbourhood_cleansed','accuracy','F1','<ProjectCities />','5000000','3000','seed: 42'])assert(brief.includes(token),token)
  assert(practice.includes('sẽ được bổ sung'))
  assert(!practice.includes('```python'))
  assert(!/\|.*\|.*\|.*\|.*\|/.test(brief),'Keep tables narrow for mobile')
})
