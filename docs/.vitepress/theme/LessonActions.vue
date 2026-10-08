<script setup>
import { computed, onMounted, onBeforeUnmount, onUnmounted, watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'
import { useLecture } from './lecture-state'
import { lecturePath } from '../lecture-model.mjs'
import { studyLink } from './links'
import { readStored, writeStored, storageMessage } from './storage'
import { progressKey } from './progress'
const route = useRoute(), { course, lesson, part } = useLecture()
const readable = computed(() => lesson.value?.status === 'ready')
const nextLesson = computed(() => course.value?.lessons[course.value.lessons.indexOf(lesson.value) + 1])
let frame, trackedPath = '', trackedTitle = ''
async function load() {
  await nextTick()
  if (!readable.value) { trackedPath = ''; return }
  trackedPath = progressKey(course.value, lesson.value)
  trackedTitle = lesson.value.title
  const previous = readStored('studyhub_last_lesson', null)
  writeStored('studyhub_last_lesson', { ...(previous?.path === trackedPath ? previous : {}), path: trackedPath, title: lesson.value.title })
}
function recordHeading() {
  if (part.value !== 'notes' || !trackedPath) return
  // Navigation can reset scroll before this component finishes unmounting.
  if (window.location.pathname !== studyLink(trackedPath)) return
  const headings = [...document.querySelectorAll('.main > .vp-doc h2[id]')]
  if (!headings.length) return
  const heading = headings.filter(h => h.getBoundingClientRect().top <= 160).at(-1)
  const previous = readStored('studyhub_last_lesson', {})
  writeStored('studyhub_last_lesson', { ...previous, path: trackedPath, title: trackedTitle, heading: heading?.id || '', headingTitle: heading?.textContent.replace(/\u200b/g, '').trim() || '' })
}
function scroll() { if (frame) cancelAnimationFrame(frame); frame = requestAnimationFrame(recordHeading) }
onMounted(() => { load(); window.addEventListener('scroll', scroll, { passive: true }); window.addEventListener('pagehide', recordHeading) })
onBeforeUnmount(recordHeading)
onUnmounted(() => { cancelAnimationFrame(frame); window.removeEventListener('scroll', scroll); window.removeEventListener('pagehide', recordHeading) })
watch(() => route.path, load)
</script>
<template><section v-if="readable" v-show="part === 'notes'" class="lesson-actions"><nav aria-label="Sau bài học"><a v-if="nextLesson" class="text-link" :href="studyLink(lecturePath(course.id, nextLesson.slug))">Tiếp: {{ nextLesson.title }}</a><a class="text-link" :href="studyLink(`/${course.id}/bai-tap`)">Bài tập ôn luyện của môn</a></nav><p v-if="storageMessage" role="status">{{ storageMessage }}</p></section></template>
