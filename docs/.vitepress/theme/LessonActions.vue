<script setup>
import { ref, onMounted, watch, nextTick } from 'vue'
import { useRoute, useData } from 'vitepress'
import { studyLink as withBase } from './links'
import { readStored, writeStored, storageMessage } from './storage'
import { canonicalLesson, migrateProgress } from './progress-migration'
const route = useRoute(), { page, frontmatter } = useData()
const done = ref(false), readable = ref(false)
function lessonPath() { const base = import.meta.env.BASE_URL; return canonicalLesson('/' + route.path.slice(base.length).replace(/^\//, '')) }
async function load() {
  await nextTick()
  readable.value = frontmatter.value.section === 'lecture' && frontmatter.value.lessonStatus === 'ready'
  if (!readable.value) return
  migrateProgress()
  const path = lessonPath()
  done.value = !!(readStored('studyhub_completed', {}) || {})[path]
  writeStored('studyhub_last_lesson', { path, title: page.value.title })
}
function toggle() {
  const completed = readStored('studyhub_completed', {}) || {}
  completed[lessonPath()] = !done.value
  if (writeStored('studyhub_completed', completed)) done.value = completed[lessonPath()]
}
onMounted(load)
watch(() => route.path, load)
</script>
<template><div v-if="readable" class="lesson-actions"><button class="study-button" :aria-pressed="done" @click="toggle">{{ done ? 'Đã hoàn thành' : 'Đánh dấu đã học' }}</button><a :href="withBase('/goc-hoc-tap#notes')">Ghi chú bài học <span aria-hidden="true">↗</span></a><span v-if="storageMessage" role="status">{{ storageMessage }}</span></div></template>
