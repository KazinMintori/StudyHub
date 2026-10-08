<script setup>
import { computed, ref } from 'vue'
import { courseCatalog } from '../course-catalog.mjs'
import { studyLink } from './links'

const query = ref('')
const normalize = text => text.toLocaleLowerCase('vi').normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g, 'd')
const visibleCourses = computed(() => courseCatalog.filter(c => normalize(`${c.name} ${c.description}`).includes(normalize(query.value))))
const starters = courseCatalog.flatMap(course => {
  const lesson = course.lessons.find(l => l.status === 'ready')
  return lesson ? [{ course, lesson }] : []
}).slice(0, 2)
</script>
<template>
  <main class="study-home">
    <header class="home-intro"><h1>Bài giảng ôn tập cho sinh viên UET</h1></header>
    <section class="resume-panel" aria-labelledby="starter-heading">
      <div><h2 id="starter-heading">Bắt đầu từ đâu?</h2><div class="starter-list"><a v-for="{ course, lesson } in starters" :key="course.id" :href="studyLink(`/${course.id}/bai-giang/${lesson.slug}`)"><span>{{ course.name }}</span>{{ lesson.title }}</a></div></div>
    </section>
    <section id="hoc-phan" aria-labelledby="course-heading"><div class="section-heading"><h2 id="course-heading">Học phần</h2><label v-if="courseCatalog.length >= 6" class="course-search"><span>Lọc học phần</span><input v-model="query" type="search" placeholder="Lọc theo tên môn hoặc chủ đề"></label></div><div class="course-list"><a v-for="course in visibleCourses" :key="course.id" class="course-row" :href="studyLink(`/${course.id}/`)"><div class="course-copy"><h3>{{ course.name }}</h3><p>{{ course.description }}</p></div><span class="course-end">{{ course.lessons.length }} bài</span></a></div><p v-if="!visibleCourses.length" class="empty-state" role="status">Không tìm thấy học phần. Thử tên môn hoặc chủ đề khác.</p></section>
    <nav class="home-tools" aria-label="Công cụ ôn tập"><h2>Công cụ ôn tập</h2><a :href="studyLink('/goc-hoc-tap#flashcards')">Flashcard</a><a :href="studyLink('/goc-hoc-tap#notes')">Sổ ghi chú</a><a :href="studyLink('/goc-hoc-tap#focus')">Hẹn giờ tập trung</a><a :href="studyLink('/goc-hoc-tap#simulation')">Mô phỏng điện trường</a></nav>
  </main>
</template>
