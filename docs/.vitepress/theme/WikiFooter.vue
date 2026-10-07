<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { concepts } from '../concepts.mjs'
import { relatedConcepts } from '../wiki-content.mjs'
import { courseCatalog } from '../course-catalog.mjs'
import { lecturePath } from '../lecture-model.mjs'
import { studyLink } from './links'
const {frontmatter}=useData(), id=computed(()=>frontmatter.value.wikiTerm)
const incoming=computed(()=>Object.entries(concepts).filter(([other])=>other!==id.value&&relatedConcepts(other).includes(id.value)))
const lectures=computed(()=>courseCatalog.flatMap(course=>course.lessons.filter(lesson=>lesson.prerequisites.includes(id.value)).map(lesson=>({course,lesson}))))
</script>
<template><aside v-if="id" class="wiki-backlinks"><section><h2>Các thuật ngữ dẫn tới bài này</h2><div class="wiki-backlink-list"><a v-for="[other,term] in incoming" :key="other" class="study-term" :data-term="other" :href="studyLink(`/wiki/${other}`)">{{ term.name }}</a></div><p v-if="!incoming.length" class="small">Các bài Wiki khác có thể liên kết tới khái niệm này khi được bổ sung.</p></section><section><h2>Bài giảng cần khái niệm này</h2><ul><li v-for="{course,lesson} in lectures" :key="`${course.id}/${lesson.slug}`"><a :href="studyLink(lecturePath(course.id,lesson.slug,'kien-thuc-can-co'))">{{ lesson.title }}</a><span>{{ course.short }}</span></li></ul><p v-if="!lectures.length" class="small">Khái niệm bổ trợ cho việc đọc các thuật ngữ liên quan.</p></section><a class="text-link" :href="studyLink('/wiki/')">← Tất cả thuật ngữ</a></aside></template>
