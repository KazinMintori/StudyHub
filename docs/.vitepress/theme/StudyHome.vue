<script setup>
import { computed, ref } from 'vue'
import { courseCatalog } from '../course-catalog.mjs'
import { concepts } from '../concepts.mjs'
import { studyLink } from './links'
import { useStudyProgress } from './progress'
const query = ref('')
const { lastLesson: last } = useStudyProgress()
const normalize = text => text.toLocaleLowerCase('vi').normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g, 'd')
const visibleCourses = computed(() => courseCatalog.filter(c => normalize(`${c.name} ${c.description}`).includes(normalize(query.value))))
const totalLessons = courseCatalog.reduce((n, c) => n + c.lessons.length, 0)
const totalTerms = Object.keys(concepts).length
const starters = courseCatalog.flatMap(course => {
  const lesson = course.lessons.find(l => l.status === 'ready')
  return lesson ? [{ course, lesson }] : []
}).slice(0, 2)
const lastCourse = computed(() => courseCatalog.find(c => last.value?.path?.startsWith(`/${c.id}/`)))
const resume = computed(() => lastCourse.value?.lessons.some(l => last.value.path.includes(`/${l.slug}`)) ? last.value : null)
const resumeLink = computed(() => resume.value?.path + (resume.value?.heading ? `#${resume.value.heading}` : '#notes'))
</script>
<template>
  <main class="study-home">
    <header class="home-intro"><h1>Bài giảng ôn tập cho sinh viên UET</h1><p class="intro-description">{{ courseCatalog.length }} học phần, {{ totalLessons }} bài, {{ totalTerms }} thuật ngữ. Mỗi bài có Notes, Slides và Kiến thức nền.</p></header>
    <section class="resume-panel" aria-labelledby="resume-heading">
      <template v-if="resume"><div><h2 id="resume-heading">Tiếp tục đọc</h2><p class="small">{{ lastCourse.name }}</p><h3>{{ resume.title }}</h3><p v-if="resume.headingTitle">Đọc tới: {{ resume.headingTitle }}</p><p class="small">Lần đọc gần nhất được lưu trên trình duyệt này.</p></div><a class="study-button primary" :href="studyLink(resumeLink)">Đọc tiếp</a></template>
      <div v-else><h2 id="resume-heading">Bắt đầu từ đâu?</h2><div class="starter-list"><a v-for="{ course, lesson } in starters" :key="course.id" :href="studyLink(`/${course.id}/bai-giang/${lesson.slug}`)"><span>{{ course.name }}</span>{{ lesson.title }}</a></div></div>
    </section>
    <section id="hoc-phan" aria-labelledby="course-heading"><div class="section-heading"><h2 id="course-heading">Học phần</h2><label v-if="courseCatalog.length >= 6" class="course-search"><span>Lọc học phần</span><input v-model="query" type="search" placeholder="Lọc theo tên môn hoặc chủ đề"></label></div><div class="course-list"><a v-for="course in visibleCourses" :key="course.id" class="course-row" :href="studyLink(`/${course.id}/`)"><div class="course-copy"><h3>{{ course.name }}</h3><p>{{ course.description }}</p></div><span class="course-end">{{ course.lessons.length }} bài</span></a></div><p v-if="!visibleCourses.length" class="empty-state" role="status">Không tìm thấy học phần. Thử tên môn hoặc chủ đề khác.</p></section>
    <nav class="home-tools" aria-label="Công cụ ôn tập"><h2>Công cụ ôn tập</h2><a :href="studyLink('/goc-hoc-tap#flashcards')">Flashcard</a><a :href="studyLink('/goc-hoc-tap#notes')">Sổ ghi chú</a><a :href="studyLink('/goc-hoc-tap#focus')">Hẹn giờ tập trung</a><a :href="studyLink('/goc-hoc-tap#simulation')">Mô phỏng điện trường</a></nav>
  </main>
</template>
