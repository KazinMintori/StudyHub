<script setup>
import { useRouter } from 'vitepress'
import { useLecture, lectureParts, lecturePart } from './lecture-state'
import { lecturePath } from '../lecture-model.mjs'
import { studyLink } from './links'
const { course, lesson, part } = useLecture(), router = useRouter()
function select(id) {
  lecturePart.value = id
  router.go(studyLink(lecturePath(course.value.id, lesson.value.slug, id)))
}
</script>
<template>
  <header v-if="course && lesson" class="lecture-header">
    <a class="course-parent" :href="studyLink(`/${course.id}/`)">← {{ course.name }}</a>
    <p class="eyebrow">BÀI GIẢNG {{ String(course.lessons.indexOf(lesson)+1).padStart(2,'0') }}</p>
    <h1>{{ lesson.title }}</h1>
    <p class="lecture-description">{{ lesson.status === 'ready' ? 'Slides để nắm ý chính. Notes để học chi tiết. Kiến thức cần có để chuẩn bị nền tảng của bài này.' : 'Bài đang biên soạn. Bạn có thể đọc nền tảng cần chuẩn bị trước.' }}</p>
    <nav class="course-tabs lecture-tabs" aria-label="Ba phần của bài giảng"><a v-for="item in lectureParts" :key="item.id" :href="studyLink(lecturePath(course.id,lesson.slug,item.id))" :aria-current="part===item.id ? 'page' : undefined" @click.prevent="select(item.id)">{{ item.name }}</a></nav>
  </header>
</template>
