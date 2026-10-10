<script setup>
import { computed, ref } from 'vue'
import { courseCatalog } from '../course-catalog.mjs'
import { studyLink } from './links'
import { progressKey, useStudyProgress } from './progress'
import { canonicalLesson } from './progress-migration'

const query = ref('')
const { lastLesson } = useStudyProgress()
const normalize = text => text.toLocaleLowerCase('vi').normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g, 'd')
const visibleCourses = computed(() => courseCatalog.filter(c => normalize(`${c.name} ${c.description}`).includes(normalize(query.value))))
const starters = courseCatalog.flatMap(course => {
  const lesson = course.lessons.find(l => l.status === 'ready')
  return lesson ? [{ course, lesson }] : []
}).slice(0, 2)
const resume = computed(() => {
  const saved = lastLesson.value
  const path = canonicalLesson(saved?.path)
  const course = courseCatalog.find(c => c.lessons.some(l => l.status === 'ready' && progressKey(c, l) === path))
  if (!course) return null
  const lesson = course.lessons.find(l => progressKey(course, l) === path)
  return { course, lesson, path, heading: typeof saved.heading === 'string' ? saved.heading : '', headingTitle: typeof saved.headingTitle === 'string' ? saved.headingTitle : '' }
})
const resumeLink = computed(() => resume.value ? `${resume.value.path}#${resume.value.heading || 'notes'}` : '')
</script>
<template>
  <main class="study-home">
    <header class="home-intro"><h1>Bài giảng ôn tập cho sinh viên UET</h1></header>
    <section class="resume-panel" :class="{ 'has-resume': resume }" aria-labelledby="resume-heading">
      <template v-if="resume">
        <div class="resume-copy"><h2 id="resume-heading">Tiếp tục bài giảng</h2><p class="small">{{ resume.course.name }}</p><h3>{{ resume.lesson.title }}</h3><p v-if="resume.heading && resume.headingTitle">Đọc tới: {{ resume.headingTitle }}</p><p class="small">Lần đọc gần nhất được lưu trên trình duyệt này.</p></div>
        <a class="study-button primary" :href="studyLink(resumeLink)">Tiếp tục đọc</a>
      </template>
      <div v-else><h2 id="resume-heading">Bắt đầu từ đâu?</h2><div class="starter-list"><a v-for="{ course, lesson } in starters" :key="course.id" :href="studyLink(`/${course.id}/bai-giang/${lesson.slug}`)"><span>{{ course.name }}</span>{{ lesson.title }}</a></div></div>
    </section>
    <section id="hoc-phan" aria-labelledby="course-heading">
      <div class="section-heading">
        <h2 id="course-heading">Học phần</h2>
        <label v-if="courseCatalog.length >= 6" class="course-search">
          <span>Tìm học phần</span>
          <input v-model="query" type="search" placeholder="Tìm theo tên môn hoặc chủ đề">
        </label>
      </div>
      <div class="course-list">
        <a v-for="course in visibleCourses" :key="course.id" class="course-row" :href="studyLink(`/${course.id}/`)">
          <div class="course-copy">
            <h3>{{ course.name }}</h3>
          </div>
          <span class="course-end">{{ course.lessons.length }} bài</span>
        </a>
      </div>
      <p v-if="!visibleCourses.length" class="empty-state" role="status">Không tìm thấy học phần. Thử tên môn hoặc chủ đề khác.</p>
    </section>
  </main>
</template>
