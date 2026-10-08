<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { concepts } from '../concepts.mjs'
import { conceptField } from '../wiki-content.mjs'
import { courseCatalog } from '../course-catalog.mjs'
import { lecturePath } from '../lecture-model.mjs'
import { studyLink } from './links'

const { frontmatter } = useData()
const id = computed(() => frontmatter.value.wikiTerm)
const field = computed(() => conceptField(id.value))
const lessonTerms = lesson => new Set([...(lesson.prerequisites || []), ...(lesson.supportingConcepts || [])])
const lectures = computed(() => courseCatalog.flatMap(course => course.lessons
  .filter(lesson => lessonTerms(lesson).has(id.value))
  .map(lesson => ({ course, lesson }))))
const alternatives = computed(() => {
  const current = concepts[id.value]
  if (!current) return []
  const aliases = new Set(current.aliases.map(alias => alias.toLocaleLowerCase('vi')))
  return Object.entries(concepts)
    .filter(([other, term]) => other !== id.value && term.aliases.some(alias => aliases.has(alias.toLocaleLowerCase('vi'))))
    .map(([other, term]) => ({ id: other, term, field: conceptField(other) }))
})
</script>

<template>
  <aside class="wiki-context-card" aria-label="Phạm vi của thuật ngữ">
    <p><strong>Lĩnh vực:</strong> {{ field.name }}</p>
    <p>Định nghĩa trên trang này được dùng trong lĩnh vực vừa nêu. Một từ giống nhau ở môn khác có thể mang nghĩa khác.</p>
    <div v-if="alternatives.length" class="wiki-other-senses">
      <strong>Nghĩa ở lĩnh vực khác</strong>
      <a v-for="item in alternatives" :key="item.id" :href="studyLink(`/wiki/${item.id}`)">{{ item.term.name }} <span>· {{ item.field.name }}</span></a>
    </div>
  </aside>
  <aside v-if="lectures.length" class="wiki-backlinks wiki-usage-top" aria-label="Bài giảng dùng khái niệm này"><h2>Bài giảng dùng khái niệm này</h2><ul><li v-for="{ course, lesson } in lectures" :key="`${course.id}/${lesson.slug}`"><a :href="studyLink(lecturePath(course.id, lesson.slug))">{{ lesson.title }}</a><span>{{ course.short }}</span></li></ul></aside>
</template>
