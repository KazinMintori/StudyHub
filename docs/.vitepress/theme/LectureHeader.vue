<script setup>
import { computed, ref, nextTick } from 'vue'
import { useRouter, useData, onContentUpdated } from 'vitepress'
import { useLecture, lectureParts, lecturePart } from './lecture-state'
import { lecturePath, readingMinutes } from '../lecture-model.mjs'
import { studyLink } from './links'
const { course, lesson, part } = useLecture(), router = useRouter(), { page } = useData()
const currentPart = computed(() => course.value?.parts?.find(p => p.lessons.includes(lesson.value?.slug)))
const updated = computed(() => page.value.lastUpdated ? new Date(page.value.lastUpdated).toLocaleDateString('vi-VN', { timeZone: 'Asia/Bangkok' }) : '')
const mobileOutline = ref(null)
const articleHeadings = ref([])
onContentUpdated(async () => {
  await nextTick()
  articleHeadings.value = [...document.querySelectorAll('.main > .vp-doc h2[id]')].map(heading => ({ slug: heading.id, title: heading.textContent.replace(/\u200b/g, '').trim() }))
})
function openSidebar() { document.querySelector('.VPLocalNav .menu')?.click() }
function closeOutline() { if (mobileOutline.value) mobileOutline.value.open = false }
function select(id) { lecturePart.value = id; router.go(studyLink(lecturePath(course.value.id, lesson.value.slug, id))) }
</script>
<template>
  <nav v-if="course && lesson" class="mobile-lecture-nav" aria-label="Điều hướng bài học"><button aria-label="Mở danh sách bài giảng" @click="openSidebar"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M3 5h14M3 10h14M3 15h14" fill="none" stroke="currentColor" stroke-width="1.5" /></svg></button><a :href="studyLink(`/${course.id}/`)">{{ course.short }}</a><details v-if="part === 'notes'" ref="mobileOutline"><summary>Mục lục</summary><nav aria-label="Mục lục bài viết"><a v-for="heading in articleHeadings" :key="heading.slug" :href="`#${heading.slug}`" @click="closeOutline">{{ heading.title }}</a></nav></details></nav>
  <header v-if="course && lesson" class="lecture-header book-header"><nav class="book-breadcrumbs" aria-label="Đường dẫn bài đọc"><a :href="studyLink(`/${course.id}/`)">{{ course.name }}</a><template v-if="currentPart"><span class="part-crumb">/</span><span class="part-crumb">{{ currentPart.title }}</span></template></nav><h1>{{ lesson.title }}</h1><div class="lecture-meta"><span>Bài {{ lesson.number ?? course.lessons.indexOf(lesson) + 1 }} · {{ readingMinutes(course.id, lesson.slug) }} phút đọc</span><span v-if="updated" class="updated-date">Cập nhật {{ updated }}</span><a :href="studyLink('/goc-hoc-tap#notes')">Ghi chú của bạn</a></div><p v-if="lesson.status !== 'ready'" class="draft-notice">Bài đang được soạn. Kiến thức nền đã đọc được.</p></header>
  <nav v-if="course && lesson" class="course-tabs lecture-tabs" aria-label="Các phần của bài giảng"><a v-for="item in lectureParts" :key="item.id" :href="studyLink(lecturePath(course.id, lesson.slug, item.id))" :aria-current="part === item.id ? 'page' : undefined" @click.prevent="select(item.id)">{{ item.name }}<span v-if="item.id === 'kien-thuc-can-co'" class="tab-count">{{ lesson.prerequisites.length }}</span></a></nav>
</template>
