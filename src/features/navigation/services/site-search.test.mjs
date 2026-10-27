import assert from 'node:assert/strict'
import { test } from 'node:test'
import { buildSearchEntries, searchEntries } from './site-search.mjs'

test('search finds Vietnamese course, topic and Wiki aliases without accents', () => {
  const entries = buildSearchEntries([{ id: 'toan', name: 'Toán học', lessons: [{ slug: 'toi-uu', title: 'Tối ưu', topicGroups: [{ topics: [{ slug: 'duong-thang', title: 'Đường thẳng' }] }] }] }], { gradient: { name: 'Gradient', aliases: ['Đạo hàm'] } })
  assert.equal(searchEntries(entries, 'toan hoc')[0].path, '/toan/')
  assert.equal(searchEntries(entries, 'duong thang')[0].path, '/toan/bai-giang/toi-uu/duong-thang')
  assert.equal(searchEntries(entries, 'dao ham')[0].path, '/wiki/gradient')
  assert.equal(searchEntries(entries, 'toi uu toan').length, 2)
  assert.deepEqual(searchEntries(entries, '   '), [])
  assert.deepEqual(searchEntries(entries, 'khong ton tai'), [])
})
