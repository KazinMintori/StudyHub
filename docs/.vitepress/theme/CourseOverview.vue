<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../course-catalog.mjs'
import { lecturePath, lectureSlides } from '../lecture-model.mjs'
import { studyLink } from './links'
const { frontmatter } = useData()
const course = computed(() => findCourse(frontmatter.value.course))

function getLesson(c, slug) {
  return c?.lessons?.find(l => l.slug === slug)
}

function getLessonIndex(c, slug) {
  const idx = c?.lessons?.findIndex(l => l.slug === slug)
  return idx >= 0 ? idx : 0
}
</script>

<template>
  <main v-if="course" class="course-overview course-shell">
    <a class="text-link small" :href="studyLink('/')">← Thư viện môn học</a>
    <p class="eyebrow">HỌC PHẦN {{ course.code }}</p>
    <h1>{{ course.name }}</h1>
    <p class="course-description">{{ course.description }}</p>

    <!-- Bookmark Parts Breakdown -->
    <template v-if="course.parts && course.parts.length">
      <div v-for="(part, pIdx) in course.parts" :key="part.title" class="course-part-section">
        <div class="part-banner">
          <div class="part-title-row">
            <span class="part-bookmark-icon" aria-hidden="true">🔖</span>
            <h2>{{ part.title }}</h2>
          </div>
          <p v-if="part.description" class="part-description">{{ part.description }}</p>
        </div>

        <div class="lecture-list">
          <article v-for="slug in part.lessons" :key="slug">
            <template v-if="getLesson(course, slug)">
              <span class="course-number">{{ String(getLessonIndex(course, slug) + 1).padStart(2, '0') }}</span>
              <div class="lecture-list-copy">
                <a class="lecture-title-link" :href="studyLink(lecturePath(course.id, slug))">
                  <h3>{{ getLesson(course, slug).title }}</h3>
                </a>
                <p>
                  {{ getLesson(course, slug).status === 'ready'
                    ? `${lectureSlides(course, getLesson(course, slug)).length} slide · Notes chi tiết · ${getLesson(course, slug).prerequisites.length} nền tảng cần có`
                    : 'Đang biên soạn · có nền tảng để chuẩn bị' }}
                </p>
                <nav aria-label="Chọn phần của bài giảng">
                  <a :href="studyLink(lecturePath(course.id, slug, 'slides'))">Slides</a>
                  <a :href="studyLink(lecturePath(course.id, slug, 'notes'))">Notes</a>
                  <a :href="studyLink(lecturePath(course.id, slug, 'kien-thuc-can-co'))">Kiến thức cần có</a>
                </nav>
              </div>
              <a class="lecture-open" :href="studyLink(lecturePath(course.id, slug))" :aria-label="`Mở ${getLesson(course, slug).title}`">→</a>
            </template>
          </article>
        </div>
      </div>
    </template>

    <!-- Fallback flat list -->
    <template v-else>
      <div class="lecture-list-heading">
        <h2>Bài giảng</h2>
        <p>Mỗi bài gồm Slides, Notes và Kiến thức cần có. Chọn bài trước, rồi học theo phần bạn cần.</p>
      </div>
      <div class="lecture-list">
        <article v-for="(lesson, i) in course.lessons" :key="lesson.slug">
          <span class="course-number">{{ String(i + 1).padStart(2, '0') }}</span>
          <div class="lecture-list-copy">
            <a class="lecture-title-link" :href="studyLink(lecturePath(course.id, lesson.slug))">
              <h3>{{ lesson.title }}</h3>
            </a>
            <p>
              {{ lesson.status === 'ready'
                ? `${lectureSlides(course, lesson).length} slide · Notes chi tiết · ${lesson.prerequisites.length} nền tảng cần có`
                : 'Đang biên soạn · có nền tảng để chuẩn bị' }}
            </p>
            <nav aria-label="Chọn phần của bài giảng">
              <a :href="studyLink(lecturePath(course.id, lesson.slug, 'slides'))">Slides</a>
              <a :href="studyLink(lecturePath(course.id, lesson.slug, 'notes'))">Notes</a>
              <a :href="studyLink(lecturePath(course.id, lesson.slug, 'kien-thuc-can-co'))">Kiến thức cần có</a>
            </nav>
          </div>
          <a class="lecture-open" :href="studyLink(lecturePath(course.id, lesson.slug))" :aria-label="`Mở ${lesson.title}`">→</a>
        </article>
      </div>
    </template>

    <div class="course-wiki-footnote">
      <div>
        <h2>Gặp thuật ngữ chưa quen?</h2>
        <p>Wiki giải thích từng khái niệm và kết nối những nền tảng liên quan. Bạn có thể mở Wiki từ thuật ngữ ngay trong bài.</p>
      </div>
      <a class="study-button" :href="studyLink('/wiki/')">Tra cứu Wiki →</a>
    </div>
    <a class="text-link" :href="studyLink(`/${course.id}/notes/lo-trinh`)">Lộ trình và tài liệu tham khảo của môn →</a>
  </main>
</template>
