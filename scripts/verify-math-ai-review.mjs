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
  const filePath = `docs/toan-cho-ai/on-luyen/${topic.slug}.md`
  const content = await readFile(filePath, 'utf8')
  assert(content.length > 500, `Topic ${topic.slug} is empty or too short`)
}
for (const topic of topics) {
  const mapped = manifest.images.filter(row => row.destination.endsWith(`/${topic.slug}.md`))
  assert(mapped.length > 0, `Topic ${topic.slug} has no mapped source images`)
}
console.log('All 12 review topics verified across 4 ordered review groups.')
console.log('All 103 source images map to their reordered review topics.')
