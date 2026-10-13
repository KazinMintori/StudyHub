<script setup>
import { computed, ref, onMounted, onUnmounted, watch } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../course-catalog.mjs'
import { lecturePath, topicPath } from '../lecture-model.mjs'
import { studyLink } from './links'
const { frontmatter } = useData()
const course = computed(() => findCourse(frontmatter.value.course))
const review = computed(() => course.value?.review)
const view = ref(frontmatter.value.reviewOverview ? 'on-luyen' : 'bai-giang')
const lessons = computed(() => course.value?.lessons || [])
const groups = computed(() => course.value.parts?.length ? course.value.parts.map(p => ({ ...p, entries: p.lessons.map(slug => lessons.value.find(l => l.slug === slug)).filter(Boolean) })).filter(group => group.entries.length) : [{ title: 'Bài giảng', entries: lessons.value }])
function syncView() { view.value = review.value && (frontmatter.value.reviewOverview || window.location.hash === '#on-luyen') ? 'on-luyen' : 'bai-giang' }
onMounted(() => {
  syncView()
  window.addEventListener('hashchange', syncView)
  window.addEventListener('popstate', syncView)
})
onUnmounted(() => {
  window.removeEventListener('hashchange', syncView)
  window.removeEventListener('popstate', syncView)
})
watch(() => frontmatter.value.course, () => { if (typeof window !== 'undefined') syncView() })
</script>
<template>
  <main v-if="course" class="course-overview course-shell">
    <nav class="book-breadcrumbs" aria-label="Đường dẫn"><a :href="studyLink('/')">Trang chủ</a><span>/</span><span>Học phần</span></nav>
    <h1>{{ course.name }}</h1>
    <p class="course-description">{{ course.description }}</p>
    <div class="course-meta">
      <span>{{ lessons.length }} bài giảng</span>
      <a :href="studyLink(`/${course.id}/bai-tap`)">Bài tập ôn luyện</a>
      <a :href="studyLink(`/${course.id}/notes/lo-trinh`)">Lộ trình và tài liệu</a>
    </div>
    <nav v-if="review" class="workspace-tabs course-overview-tabs" aria-label="Nội dung môn học">
      <a :href="studyLink(`/${course.id}/`)" :aria-current="view === 'bai-giang' ? 'page' : undefined">Bài giảng</a>
      <a :href="studyLink(`/${course.id}/on-luyen`)" :aria-current="view === 'on-luyen' ? 'page' : undefined">Ôn luyện</a>
    </nav>
    <div v-if="view === 'bai-giang'" id="bai-giang">
      <section v-for="group in groups" :key="group.title" class="course-part-section">
        <header class="part-banner"><h2>{{ group.title }}</h2><p v-if="group.description" class="part-description">{{ group.description }}</p></header>
        <div class="lecture-list"><article v-for="lesson in group.entries" :key="lesson.slug">
          <a class="lecture-row" :href="studyLink(lecturePath(course.id, lesson.slug))"><span class="lesson-number">{{ lesson.number ?? course.lessons.indexOf(lesson) + 1 }}</span><div class="lecture-list-copy"><h3>{{ lesson.title }}</h3></div><span v-if="lesson.status !== 'ready'" class="lesson-status">Bản nháp</span></a>
        </article></div>
      </section>
    </div>
    <div v-else-if="review" id="on-luyen">
      <section v-for="group in review.topicGroups" :key="group.title" class="course-part-section">
        <header class="part-banner"><h2>{{ group.title }}</h2><p class="part-description">{{ group.description }}</p></header>
        <div class="lecture-list"><article v-for="(topic, index) in group.topics" :key="topic.slug">
          <a class="lecture-row" :href="studyLink(topicPath(course.id, review.slug, topic.slug))"><span class="lesson-number">{{ index + 1 }}</span><div class="lecture-list-copy"><h3>{{ topic.title }}</h3></div></a>
        </article></div>
      </section>
      <div class="course-meta"><a :href="studyLink(lecturePath(course.id, review.slug))">Tổng hợp ôn luyện</a></div>
    </div>
  </main>
</template>
