import test from 'node:test'
import assert from 'node:assert/strict'
import { lookupConcepts, lookupConnections, prioritizeLookupSections } from '../../src/features/lecture/services/lesson-lookup.mjs'

const concepts = {
  force: { name:'Lực', aliases:['force'], definition:'Tương tác giữa các vật' },
  friction: { name:'Ma sát nghỉ', aliases:['static friction'], definition:'Chống xu hướng trượt' },
  probability: { name:'Xác suất', definition:'Khả năng xảy ra biến cố' }
}

test('Handbook defaults to the lesson and never leaks unrelated Wiki entries', () => {
  assert.deepEqual(lookupConcepts(concepts,['force','force','missing']).map(term=>term.id),['force'])
  assert.deepEqual(lookupConcepts(concepts,['force'],'xác suất'),[])
  assert.deepEqual(lookupConcepts(concepts,['force'],'xac suat',{ global:true }).map(term=>term.id),['probability'])
  assert.deepEqual(lookupConcepts(concepts,['force'],'',{ global:true }),[])
})

test('Handbook searches aliases and Vietnamese without accents', () => {
  assert.equal(lookupConcepts(concepts,['friction'],'ma sat nghi')[0].id,'friction')
  assert.equal(lookupConcepts(concepts,['friction'],'static friction')[0].name,'Ma sát nghỉ')
})

test('An exact Wiki name ranks before incidental mentions in definitions', () => {
  const dictionary={ example:{ name:'Một ví dụ',definition:'Có sử dụng xác suất' },...concepts }
  assert.equal(lookupConcepts(dictionary,[],'xac suat',{global:true})[0].id,'probability')
})

test('Connections retain existing lesson sources, distinct targets and usable concepts', () => {
  const related=id=>id==='force'?['friction','friction','missing','force','probability']:[]
  const result=lookupConnections(concepts,['force','friction','missing'],related)
  assert.deepEqual(result,[{ id:'force',name:'Lực',targets:[{ id:'friction',name:'Ma sát nghỉ' }] }])
  assert.equal(lookupConnections(concepts,['force','friction'],related,'ma sat').length,1)
  assert.deepEqual(lookupConnections(concepts,['force'],related),[])
  assert.deepEqual(lookupConnections(concepts,['force'],()=>{ throw Error('Missing Wiki group') }),[])
})

test('Current section ranks first and section1.10 is distinct from section1.1', () => {
  const units={ id:'units',badge:'1.1–1.4' },products={ id:'products',badge:'1.10' },components={ id:'components',badge:'1.8–1.9' }
  const source=[units,components,products]
  assert.deepEqual(prioritizeLookupSections(source,'1.10'),[products,units,components])
  assert.deepEqual(prioritizeLookupSections(source,'1.8'),[components,units,products])
  assert.deepEqual(source,[units,components,products])
})
