import { mkdir, readFile, writeFile } from 'node:fs/promises'
const check = process.argv.includes('--check')
for (const chapter of [1, 2, 3]) {
  const directory = `docs/triet-hoc-mac-lenin/on-thi/chuong-${chapter}`
  const file = `${directory}/dien-tu.md`
  const source = `---
layout: page
title: "Điền từ · Chương ${['I','II','III'][chapter - 1]}"
course: triet-hoc-mac-lenin
section: exam
outline: false
sidebar: false
---

<script setup>
import PhilosophyFillPractice from '../../../../src/features/philosophy/components/PhilosophyFillPractice.vue'
import bank from '../../../../src/content/courses/triet-hoc-mac-lenin/exam/fill/chuong-${chapter}.json'
</script>

<PhilosophyFillPractice :bank="bank" />
`
  if (check) { if (await readFile(file,'utf8') !== source) throw Error(`Outdated ${file}`) }
  else { await mkdir(directory,{recursive:true}); await writeFile(file,source) }
}
console.log(`${check ? 'Validated' : 'Generated'} three chapter fill-in routes.`)
