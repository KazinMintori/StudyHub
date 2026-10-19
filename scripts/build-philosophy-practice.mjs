import { readFile, writeFile, mkdir } from 'node:fs/promises'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import { chapterPracticeTests, createPracticeBank } from '../src/features/philosophy/services/practice-tests.mjs'
import { cleanQuestionFeedback } from '../src/features/philosophy/services/quiz-feedback.mjs'

const root = fileURLToPath(new URL('../', import.meta.url))
const course = 'triet-hoc-mac-lenin'
const check = process.argv.includes('--check')
const json = value => JSON.stringify(value, null, 2) + '\n'
const catalog = JSON.parse(await readFile(path.join(root, `src/content/courses/${course}/exam/catalog.json`), 'utf8'))
const tests = []
async function output(relative, value) {
  const file = path.join(root, relative)
  if (check) {
    if (await readFile(file, 'utf8') !== value) throw new Error(`Outdated practice output: ${relative}`)
  } else {
    await mkdir(path.dirname(file), { recursive:true })
    await writeFile(file, value)
  }
}
for (const chapter of catalog.banks) {
  const bank = JSON.parse(await readFile(path.join(root, `src/content/courses/${course}/exam/${chapter.file}`), 'utf8'))
  for (const test of chapterPracticeTests(chapter)) {
    const practice = createPracticeBank(bank, test.testNumber, cleanQuestionFeedback)
    tests.push(test)
    await output(`src/content/courses/${course}/exam/practice/${test.id}.json`, json(practice))
    await output(`docs/${course}/on-thi/${chapter.id}/bai-${test.testNumber}.md`, `---
title: ${JSON.stringify(test.title)}
course: ${course}
section: exam
quiz: ${chapter.id}
quizChapter: ${chapter.chapter}
quizTest: ${test.testNumber}
outline: false
prev: false
next: false
---

<script setup>
import PhilosophyQuiz from '../../../../src/features/philosophy/components/PhilosophyQuiz.vue'
import PhilosophyPracticeLinks from '../../../../src/features/philosophy/components/PhilosophyPracticeLinks.vue'
import bank from '../../../../src/content/courses/${course}/exam/practice/${test.id}.json'
</script>

<PhilosophyQuiz :bank="bank" />

<PhilosophyPracticeLinks chapter-id="${chapter.id}" :test-number="${test.testNumber}" />
`)
  }
}
await output(`src/content/courses/${course}/exam/practice/catalog.json`, json({ schemaVersion:1, tests }))
console.log(`${check ? 'Validated' : 'Generated'} ${tests.length} practice tests with ${tests.reduce((sum,test)=>sum+test.count,0)} questions.`)
