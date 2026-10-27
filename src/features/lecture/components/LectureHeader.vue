<script setup>
import { computed, onMounted, onUnmounted } from 'vue'
import { useData } from 'vitepress'
import { useLecture, shouldIgnoreNavigationClick } from '../../navigation/index.mjs'
import { lecturePath, lectureParts } from '../services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'
import { loadLecturePayload } from '../services/lecture-payload.mjs'
import { workspacePath } from '../../study-tools/services/courseWorkspaceService.mjs'
import CourseArt from '../../illustrations/components/CourseArt.vue'
import ReadingOutline from '../../navigation/components/ReadingOutline.vue'
import { selectLecturePart } from '../../navigation/controllers/use-lecture-navigation.mjs'

const { course, lesson, part } = useLecture(), { page } = useData()
const currentPart = computed(() => course.value?.parts?.find(p => p.lessons.includes(lesson.value?.slug)))
const orderedParts = computed(() => course.value?.id === 'xac-suat-thong-ke'
  ? ['notes', 'kien-thuc-can-co', 'bai-tap', 'cheatsheet'].map(id => lectureParts.find(item => item.id === id))
  : lectureParts)
const updated = computed(() => page.value.lastUpdated ? new Date(page.value.lastUpdated).toLocaleDateString('vi-VN', { timeZone: 'Asia/Bangkok' }) : '')
function openSidebar() { document.querySelector('.VPLocalNav .menu')?.click() }
// Start downloading panel data as soon as the reader reaches for a tab.
function warmPanels() { loadLecturePayload(course.value, lesson.value).catch(() => {}) }
function select(id, event) {
  if (shouldIgnoreNavigationClick(event)) return
  if (event?.defaultPrevented) return
  event?.preventDefault()
  selectLecturePart(id)
}

function handleKeydown(e) {
  if (typeof window === 'undefined') return
  const target = e.target
  if (['INPUT', 'TEXTAREA', 'SELECT'].includes(target?.tagName) || target?.isContentEditable) return
  if (e.altKey && ['1', '2', '3', '4'].includes(e.key)) {
    const idx = parseInt(e.key, 10) - 1
    const targetPart = orderedParts.value[idx]
    if (targetPart && course.value && lesson.value) {
      e.preventDefault()
      select(targetPart.id)
    }
  }
}

onMounted(() => {
  if (typeof window !== 'undefined') {
    window.addEventListener('keydown', handleKeydown)
  }
})

onUnmounted(() => {
  if (typeof window !== 'undefined') {
    window.removeEventListener('keydown', handleKeydown)
  }
})
</script>

<template>
  <nav v-if="course && lesson" class="mobile-lecture-nav" aria-label="Điều hướng bài học">
    <button aria-label="Mở danh sách bài giảng" @click="openSidebar">
      <svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="M3 5h14M3 10h14M3 15h14" fill="none" stroke="currentColor" stroke-width="1.5" /></svg>
    </button>
    <a :href="studyLink(`/${course.id}/`)">{{ course.short }}</a>
    <ReadingOutline dropdown />
  </nav>

  <header v-if="course && lesson" class="lecture-header book-header">
    <div class="lecture-header-art"><CourseArt :course="course" /></div>
    <nav class="book-breadcrumbs" aria-label="Đường dẫn bài đọc">
      <a :href="studyLink(`/${course.id}/`)">{{ course.name }}</a>
      <template v-if="currentPart">
        <span class="part-crumb">/</span>
        <span class="part-crumb">{{ currentPart.title }}</span>
      </template>
    </nav>
    <h1>{{ lesson.title }}</h1>
    <div class="lecture-meta">
      <span v-if="lesson.supplementary">Chuyên đề bổ trợ {{ lesson.supplementNumber }}</span>
      <span v-else>Bài {{ lesson.number ?? course.lessons.indexOf(lesson) + 1 }}</span>
      <span v-if="updated" class="updated-date">Cập nhật {{ updated }}</span>
      <a :href="studyLink(workspacePath(course.id, 'notes'))">Ghi chú của bạn</a>
    </div>
    <p v-if="lesson.status !== 'ready'" class="draft-notice">Bài đang được soạn. Kiến thức nền đã đọc được.</p>
  </header>

  <div v-if="course && lesson" class="lecture-tabs-wrapper">
    <nav
      class="course-tabs lecture-tabs"
      aria-label="Các phần của bài giảng"
      @pointerenter.once="warmPanels"
      @focusin.once="warmPanels"
      @touchstart.once.passive="warmPanels"
    >
      <a
        v-for="(item, index) in orderedParts"
        :key="item.id"
        :href="studyLink(lecturePath(course.id, lesson.slug, item.id))"
        :aria-current="part === item.id ? 'page' : undefined"
        :title="`Phím tắt: Alt + ${index + 1}`"
        @click="select(item.id, $event)"
      >
        {{ item.name }}
      </a>
    </nav>
    <ReadingOutline dropdown class="tablet-reading-outline" />
  </div>
</template>
