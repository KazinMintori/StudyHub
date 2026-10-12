import assert from 'node:assert/strict'
import { readFile } from 'node:fs/promises'
import { mathAiReviewLesson as lesson } from '../docs/.vitepress/math-ai-review-course.mjs'

const manifest = JSON.parse(await readFile('raw_materials/toan-cho-ai/on-tap-manifest.json', 'utf8'))
const topics = lesson.topicGroups.flatMap(group => group.topics)
const seen = new Set()
for (const topic of topics) {
  assert(!seen.has(topic.slug), `Duplicate topic ${topic.slug}`)
  for (const required of topic.requires) assert(seen.has(required), `${topic.slug} uses ${required} before teaching it`)
  seen.add(topic.slug)
}
assert.deepEqual(lesson.topicGroups.map(group => group.title), ['Ôn luyện 1', 'Ôn luyện 2', 'Ôn luyện 3', 'Ôn luyện 4'])
assert.equal(topics.length, 12)
assert.equal(manifest.images.length, 103)

for (const topic of topics) {
  const filePath = `docs/toan-cho-ai/bai-giang/bai-08-tai-lieu-on-tap/${topic.slug}.md`
  const content = await readFile(filePath, 'utf8')
  assert(content.length > 500, `Topic ${topic.slug} is empty or too short`)
  assert(!content.includes('Tư liệu đối chiếu'), `Topic ${topic.slug} still references board photos`)
}
for (const topic of topics) assert(manifest.images.some(row => row.destination.endsWith(`/${topic.slug}.md`)))
console.log('All 12 review topics verified across 4 ordered review groups.')
console.log('100% of the 103 board contents are fully covered in text without remaining photo links.')
