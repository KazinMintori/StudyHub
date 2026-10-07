<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { courseCatalog } from '../course-catalog.mjs'
import { lecturePath } from '../lecture-model.mjs'
import { studyLink } from './links'
const { frontmatter } = useData()
const lectures = computed(() => courseCatalog.flatMap(course => course.lessons.filter(lesson => lesson.prerequisites.includes(frontmatter.value.wikiTerm)).map(lesson => ({ course, lesson }))))
</script>
<template><aside v-if="lectures.length" class="wiki-backlinks wiki-usage-top" aria-label="Bài giảng dùng khái niệm này"><h2>Bài giảng dùng khái niệm này</h2><ul><li v-for="{ course, lesson } in lectures" :key="`${course.id}/${lesson.slug}`"><a :href="studyLink(lecturePath(course.id, lesson.slug))">{{ lesson.title }}</a><span>{{ course.short }}</span></li></ul></aside></template>
