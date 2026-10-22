<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { concepts } from '../../../../docs/.vitepress/concepts.mjs'
import { conceptField } from '../../../../docs/.vitepress/wiki-content.mjs'
import { courseCatalog } from '../../../content/catalog.mjs'
import { lecturePath } from '../../lecture/services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'
import { peopleForConcept } from '../data/atlas.mjs'

const { frontmatter } = useData()
const id = computed(() => frontmatter.value.wikiTerm)
const field = computed(() => conceptField(id.value))
const people = computed(() => peopleForConcept(id.value))
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
    <div v-if="alternatives.length" class="wiki-other-senses">
      <strong>Nghĩa ở lĩnh vực khác</strong>
      <a v-for="item in alternatives" :key="item.id" :href="studyLink(`/wiki/${item.id}`)">{{ item.term.name }} <span>· {{ item.field.name }}</span></a>
    </div>
    <p v-if="people.length" class="wiki-person-links"><span>Con người & ý tưởng:</span><a v-for="person in people" :key="person.id" :href="studyLink(`/wiki/nhan-vat/${person.id}`)">{{ person.name }}</a></p>
    <details v-if="lectures.length"><summary>Gặp khái niệm này trong {{ lectures.length }} bài giảng</summary><ul><li v-for="{course, lesson} in lectures" :key="`${course.id}/${lesson.slug}`"><a :href="studyLink(lecturePath(course.id, lesson.slug))">{{ lesson.title }}</a> <span>· {{ course.short }}</span></li></ul></details>
  </aside>
</template>
