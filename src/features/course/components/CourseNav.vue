<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../../../content/catalog.mjs'
import { studyLink } from '../../../core/routing/links.js'
const {frontmatter}=useData(), course=computed(()=>findCourse(frontmatter.value.course))
</script>
<template><div v-if="course" class="course-navigation"><a class="course-parent" :href="studyLink(`/${course.id}/`)">← Bài giảng · {{ course.name }}</a></div></template>
