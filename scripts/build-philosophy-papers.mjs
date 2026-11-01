import { readFile, writeFile, mkdir } from 'node:fs/promises'
import { cleanQuestionFeedback } from '../src/features/philosophy/services/quiz-feedback.mjs'
const check = process.argv.includes('--check')
const root = 'src/content/courses/triet-hoc-mac-lenin/exam/papers'
const docs = 'docs/triet-hoc-mac-lenin/on-thi/de-thi'
const json = value => JSON.stringify(value, null, 2) + '\n'
async function output(file, content) {
  if (check) { if (await readFile(file, 'utf8') !== content) throw Error(`Outdated ${file}`) }
  else await writeFile(file, content)
}
// A fixed shuffle keeps individual papers stable across visits and publications.
function shuffle(input, seed) {
  const array = [...input]
  let state = seed
  for (let index = array.length - 1; index > 0; index--) {
    state = (Math.imul(state, 1664525) + 1013904223) >>> 0
    const other = state % (index + 1)
    ;[array[index], array[other]] = [array[other], array[index]]
  }
  return array
}
const chapters = await Promise.all([1, 2, 3].map(async number => {
  const bank = JSON.parse(await readFile(`src/content/courses/triet-hoc-mac-lenin/exam/chuong-${number}.json`, 'utf8'))
  return shuffle(bank.questions.map(question => ({ ...cleanQuestionFeedback(question), chapter: number })), 20261102 + number)
}))
const total = chapters.reduce((sum, chapter) => sum + chapter.length, 0)
const used = [0, 0, 0], ordered = []
for (let index = 0; index < total; index++) {
  const next = chapters.map((chapter, number) => ({ number, deficit: used[number] < chapter.length ? (index + 1) * chapter.length / total - used[number] : -Infinity }))
    .sort((a, b) => b.deficit - a.deficit || a.number - b.number)[0].number
  ordered.push(chapters[next][used[next]++])
}
if (!check) { await mkdir(root, { recursive: true }); await mkdir(docs, { recursive: true }) }
const count = Math.ceil(total / 60), base = Math.floor(total / count), remainder = total % count
const papers = []; let offset = 0
for (let index = 0; index < count; index++) {
  const number = index + 1, id = `tong-hop-${String(number).padStart(2, '0')}`, size = base + (index < remainder ? 1 : 0)
  const questions = ordered.slice(offset, offset + size).map(question => {
    const { sourceReference, knowledgeIds, level, questionType, ...student } = question
    return student
  })
  offset += size
  const spec = { id, title: `Đề luyện trắc nghiệm ${String(number).padStart(2, '0')}`, count: size,
    chapterCounts: [1, 2, 3].map(chapter => questions.filter(question => question.chapter === chapter).length),
    path: `/triet-hoc-mac-lenin/on-thi/de-thi/${id}` }
  papers.push(spec)
  await output(`${root}/${id}.json`, json({ version: 1, ...spec, kind: 'generated', questions }))
  await output(`${docs}/${id}.md`, `---
layout: page
title: "${spec.title}"
course: triet-hoc-mac-lenin
section: exam
outline: false
sidebar: false
---

<script setup>
import PhilosophyMockExam from '../../../../src/features/philosophy/components/PhilosophyMockExam.vue'
import bank from '../../../../src/content/courses/triet-hoc-mac-lenin/exam/papers/${id}.json'
</script>

<PhilosophyMockExam :bank="bank" />
`)
}
await output(`${root}/catalog.json`, json({ version: 1, totalQuestions: total, papers }))
console.log(`${check ? 'Validated' : 'Generated'} ${count} papers; ${total} unique questions, each used once.`)
