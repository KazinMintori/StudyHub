<script setup>
import { ref, nextTick } from 'vue'
import { onContentUpdated } from 'vitepress'
import { useTopic } from './topic-state'
import { lecturePath, topicPath } from '../lecture-model.mjs'
import { studyLink } from './links'

const { course, lesson, topics, index, topic } = useTopic()
const mobileOutline = ref(null)
const articleHeadings = ref([])
onContentUpdated(async () => {
  await nextTick()
  articleHeadings.value = [...document.querySelectorAll('.main > .vp-doc h2[id]')].map(heading => ({ slug: heading.id, title: heading.textContent.replace(/​/g, '').trim() }))
})
function openSidebar() { document.querySelector('.VPLocalNav .menu')?.click() }
function closeOutline() { if (mobileOutline.value) mobileOutline.value.open = false }
const lectureLabel = lesson => `Lecture ${String(lesson.number ?? 0).padStart(2, '0')}`
</script>

<template>
  <template v-if="course && lesson && topic">
    <nav class="mobile-lecture-nav" aria-label="Điều hướng chủ đề">
      <button aria-label="Mở danh sách bài giảng" @click="openSidebar"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M3 5h14M3 10h14M3 15h14" fill="none" stroke="currentColor" stroke-width="1.5" /></svg></button>
      <a :href="studyLink(lecturePath(course.id, lesson.slug))">{{ lectureLabel(lesson) }} · {{ index + 1 }}/{{ topics.length }}</a>
      <details ref="mobileOutline"><summary>Mục lục</summary><nav aria-label="Mục lục chủ đề"><a v-for="heading in articleHeadings" :key="heading.slug" :href="`#${heading.slug}`" @click="closeOutline">{{ heading.title }}</a></nav></details>
    </nav>
    <header class="lecture-header topic-header">
      <nav class="book-breadcrumbs" aria-label="Đường dẫn bài đọc">
        <a :href="studyLink(`/${course.id}/`)">{{ course.short || course.name }}</a>
        <span class="part-crumb">/</span>
        <a :href="studyLink(lecturePath(course.id, lesson.slug))">{{ lectureLabel(lesson) }}. {{ lesson.title }}</a>
        <span class="part-crumb">/</span>
        <span class="part-crumb">{{ topic.group }}</span>
      </nav>
      <h1>{{ topic.title }}</h1>
      <div class="lecture-meta">
        <span>Chủ đề {{ index + 1 }} / {{ topics.length }}</span>
      </div>
      <ol class="topic-progress" :aria-label="`Vị trí trong chương: chủ đề ${index + 1} trên ${topics.length}`">
        <li v-for="(item, i) in topics" :key="item.slug" :class="{ done: i < index, current: i === index }">
          <a :href="studyLink(topicPath(course.id, lesson.slug, item.slug))" :title="`${i + 1}. ${item.title}`" :aria-current="i === index ? 'page' : undefined"><span class="visually-hidden">{{ i + 1 }}. {{ item.title }}</span></a>
        </li>
      </ol>
    </header>
  </template>
</template>
