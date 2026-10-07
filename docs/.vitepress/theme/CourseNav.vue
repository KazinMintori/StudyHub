<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../course-catalog.mjs'
import { studyLink } from './links'
const {frontmatter}=useData(), course=computed(()=>findCourse(frontmatter.value.course))
</script>
<template><div v-if="course" class="course-navigation"><a class="course-parent" :href="studyLink(`/${course.id}/`)">← Bài giảng · {{ course.name }}</a></div></template>
