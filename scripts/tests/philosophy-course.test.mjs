import test from 'node:test'
import assert from 'node:assert/strict'
import { readFile, access } from 'node:fs/promises'
import { course } from '../../src/content/courses/triet-hoc-mac-lenin/course.mjs'
import { buildThemeConfig } from '../../src/features/course/services/build-navigation.mjs'
import { chapterPracticeTests } from '../../src/features/philosophy/services/practice-tests.mjs'

test('Philosophy has three source chapters without prerequisite or slide material', () => {
  assert.equal(course.lessons.length, 3)
  assert.deepEqual(course.foundations, [])
  assert.deepEqual(course.slides, [])
  assert.equal(course.lessons.flatMap(chapter => chapter.topics).length, 19)
  for (const chapter of course.lessons) assert.deepEqual(chapter.prerequisites, [])
})

test('Each topic is a complete independent page with Notes and isolated exercises', async () => {
  let total = 0
  for (const chapter of course.lessons) {
    const hub = await readFile(`docs/${course.id}/bai-giang/${chapter.slug}.md`, 'utf8')
    assert(hub.includes('<TopicMap :show-reading-time="false" />'))
    assert(!hub.includes('<PhilosophyTopic '), 'Chapter pages must not contain the topic lessons')
    assert.deepEqual(chapter.topicGroups.flatMap(group=>group.topics), chapter.topics)
    for (const topic of chapter.topics) {
      const section = await readFile(`docs/${course.id}/bai-giang/${chapter.slug}/${topic.slug}.md`, 'utf8')
      assert(section.includes(`topic: "${topic.slug}"`))
      assert(section.includes('section: "topic"'))
      assert(section.includes(`<PhilosophyTopic topic-id="${topic.id}">`))
      const notes = section.match(/<template #notes>([\s\S]*?)<\/template>/)?.[1]
      const exercises = section.match(/<template #exercises>([\s\S]*?)<\/template>/)?.[1]
      assert(notes?.trim())
      assert(exercises?.trim())
      assert(!/::: (exercise|solution)\b/.test(notes))
      assert(!notes.includes('Đáp án:'))
      assert(!/phút đọc|phút học|thời gian đọc/i.test(notes), 'Do not display reading estimates')
      const containers = [...exercises.matchAll(/^::: (exercise|solution)\b/gm)].map(match => match[1])
      assert(containers.length >= 2)
      assert.equal(containers.length % 2, 0)
      containers.forEach((kind, i) => assert.equal(kind, i % 2 ? 'solution' : 'exercise'))
      assert.equal((exercises.match(/<!-- workbook: /g) || []).length, containers.length / 2)
      assert(notes.includes('<figure class="philosophy-figure">'), 'Each topic needs a relevant, captioned illustration')
      assert(!/Câu hỏi đáng suy ngẫm|Liên hệ thực tiễn\s*:/i.test(notes), 'Reflection belongs in the argument, without announcing an editorial purpose')
      for (const solution of exercises.matchAll(/^::: solution[^\n]*\n([\s\S]*?)^:::/gm)) {
        assert(solution[1].trim().length > 40, 'Every question needs an explanatory answer')
      }
      total += containers.length / 2
    }
    const manifest = JSON.parse(await readFile(`src/content/courses/${course.id}/lectures/${chapter.slug}/content.json`, 'utf8'))
    assert.equal(manifest.cheatsheet, null)
    assert.equal(manifest.slides, null)
    assert.equal(manifest.topics.length,chapter.topics.length)
  }
  assert.equal(total, 253)
})

test('Every workbook exercise appears once in its matching topic with its complete prompt and options', async () => {
  const expected = [
    { multipleChoice: 35, trueFalse: 5, essay: 3 },
    { multipleChoice: 80, trueFalse: 20, essay: 5 },
    { multipleChoice: 80, trueFalse: 20, essay: 5 },
  ]
  const identifiers = new Set()
  for (const [index, chapter] of course.lessons.entries()) {
    const workbook = JSON.parse(await readFile(`raw_materials/${course.id}/workbook/chapter-${index + 1}.json`, 'utf8'))
    assert.deepEqual(workbook.expected, expected[index])
    const pages = new Map(await Promise.all(chapter.topics.map(async topic => [topic.slug, await readFile(`docs/${course.id}/bai-giang/${chapter.slug}/${topic.slug}.md`, 'utf8')])))
    for (const [kind, count] of Object.entries(expected[index])) {
      const entries = workbook.exercises.filter(item => item.kind === kind)
      assert.equal(entries.length, count)
      assert.deepEqual(entries.map(item => item.number).sort((a,b)=>a-b), Array.from({length:count},(_,i)=>i+1))
    }
    for (const exercise of workbook.exercises) {
      assert(!identifiers.has(exercise.id), exercise.id)
      identifiers.add(exercise.id)
      assert(pages.has(exercise.topic), exercise.topic)
      const page = pages.get(exercise.topic)
      assert.equal([...pages.values()].filter(text => text.includes(`workbook: ${exercise.id};`)).length, 1, exercise.id)
      assert(page.includes(exercise.prompt), `Complete question ${exercise.id}`)
      if (exercise.kind === 'multipleChoice') {
        assert.deepEqual(exercise.options.map(option=>option.key), ['A','B','C','D'])
        for (const option of exercise.options) assert(page.includes(option.text), `Option ${exercise.id}-${option.key}`)
      }
      assert(exercise.explanation?.trim().length > 40)
      if (exercise.answer === null && exercise.kind !== 'essay') assert(exercise.note?.trim(), `Ambiguous question ${exercise.id} needs an explicit note`)
      assert.deepEqual(exercise.pdfPages, exercise.printedPages.map(number=>number+1))
    }
  }
  assert.equal(identifiers.size, 253)
})

test('Illustrations have local assets, recorded authorship and a reuse license', async () => {
  const sources = JSON.parse(await readFile(`raw_materials/${course.id}/image-sources.json`, 'utf8'))
  assert.equal(sources.length, 19)
  assert.equal(new Set(sources.map(image=>image.topic)).size, 19)
  for (const image of sources) {
    await access(image.file)
    assert(image.width > 200 && image.height > 100)
    assert(image.page.startsWith('https://commons.wikimedia.org/wiki/File:'))
    assert(image.license && image.sha256)
  }
})

test('Exam is independent and the sidebar routes to individual topic pages', async () => {
  const config = buildThemeConfig({ courseCatalog: [course], wikiGroups: [], concepts: {} })
  const sidebar = config.sidebar[`/${course.id}/`]
  assert.deepEqual(sidebar[0].items.map(item => item.text), ['Học tập', 'Ôn thi'])
  assert.equal(sidebar.length, 4)
  assert.equal(sidebar.slice(1).flatMap(chapter => chapter.items).length, 19)
  for (const chapter of sidebar.slice(1)) for (const topic of chapter.items) {
    assert(!topic.link.includes('#'))
    await access(`docs${topic.link}.md`)
  }
})

test('Exam chapters lead to separate balanced practice tests', async () => {
  const source = await readFile(`docs/${course.id}/on-thi/index.md`, 'utf8')
  assert(source.includes('<PhilosophyExamOverview />'))
  const catalog=JSON.parse(await readFile(`src/content/courses/${course.id}/exam/catalog.json`,'utf8'))
  assert.equal(catalog.banks.length,2)
  assert.deepEqual(catalog.banks.map(bank=>bank.count),[360,440])
  for(const bank of catalog.banks) {
    const page=await readFile(`docs/${course.id}/on-thi/${bank.id}.md`,'utf8')
    assert(page.includes(`<PhilosophyPracticeChapter chapter-id="${bank.id}" />`))
    assert(!page.includes('<PhilosophyQuiz'))
    for(const practice of chapterPracticeTests(bank)) {
      const detail=await readFile(`docs${practice.path}.md`,'utf8')
      assert(detail.includes(`exam/practice/${practice.id}.json`))
      assert(detail.includes('<PhilosophyQuiz :bank="bank" />'))
    }
  }
})
