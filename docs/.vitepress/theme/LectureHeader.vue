<script setup>
import { computed } from 'vue'
import { useRouter } from 'vitepress'
import { useLecture, lectureParts, lecturePart } from './lecture-state'
import { lecturePath } from '../lecture-model.mjs'
import { studyLink } from './links'

const { course, lesson, part } = useLecture(), router = useRouter()

const currentPart = computed(() => {
  if (!course.value?.parts || !lesson.value) return null
  return course.value.parts.find(p => p.lessons.includes(lesson.value.slug))
})

function select(id) {
  lecturePart.value = id
  router.go(studyLink(lecturePath(course.value.id, lesson.value.slug, id)))
}
</script>

<template>
  <header v-if="course && lesson" class="lecture-header book-header">
    <nav class="book-breadcrumbs" aria-label="Đường dẫn bài đọc">
      <a :href="studyLink('/')">Trang chủ</a>
      <span class="sep">/</span>
      <a :href="studyLink(`/${course.id}/`)">{{ course.name }}</a>
      <template v-if="currentPart">
        <span class="sep">/</span>
        <span class="part-crumb">{{ currentPart.title }}</span>
      </template>
    </nav>

    <div class="lecture-header-meta">
      <span class="chapter-badge">BÀI {{ String(course.lessons.indexOf(lesson) + 1).padStart(2, '0') }}</span>
      <span v-if="currentPart" class="part-badge-small">🔖 {{ currentPart.title }}</span>
    </div>

    <h1>{{ lesson.title }}</h1>
    <p class="lecture-description">
      {{ lesson.status === 'ready'
        ? 'Tài liệu chuẩn mực theo phong cách sách giáo trình: Đọc lý thuyết, xem ví dụ thực tế và tra cứu công thức.'
        : 'Bài giảng đang được biên soạn. Bạn có thể tra cứu kiến thức nền tảng trước.' }}
    </p>

    <nav class="course-tabs lecture-tabs" aria-label="Ba phần của bài giảng">
      <a
        v-for="item in lectureParts"
        :key="item.id"
        :href="studyLink(lecturePath(course.id, lesson.slug, item.id))"
        :aria-current="part === item.id ? 'page' : undefined"
        @click.prevent="select(item.id)"
      >{{ item.name }}</a>
    </nav>
  </header>
</template>
