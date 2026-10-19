<script setup>
import { useStudyHome } from '../controllers/useStudyHome.js'
import { studyLink } from '../../../core/routing/links.js'

const {
  query,
  visibleCourses,
  catalog,
  resume,
  activeResume,
  activeResumeLink,
  getLessonChapter,
  getLessonDetailTitle
} = useStudyHome()
</script>

<template>
  <main class="study-home">
    <header class="home-intro"><h1>Bài giảng ôn tập cho sinh viên UET</h1></header>

    <section v-if="activeResume" class="resume-panel" aria-labelledby="resume-heading">
      <div class="resume-card-inner">
        <div class="resume-copy">
          <div class="resume-header-row">
            <span class="resume-kicker">
              <svg class="resume-kicker-icon" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
                <circle cx="12" cy="12" r="10" />
                <polyline points="12 6 12 12 16 14" />
              </svg>
              <span>{{ resume ? 'Tiếp tục bài giảng' : 'Bắt đầu học' }}</span>
            </span>
            <span class="resume-top-divider" aria-hidden="true">·</span>
            <span class="course-badge">{{ activeResume.course.name }}</span>
            <template v-if="getLessonChapter(activeResume.course, activeResume.lesson)">
              <span class="resume-path-sep" aria-hidden="true">/</span>
              <span class="resume-chapter-name">{{ getLessonChapter(activeResume.course, activeResume.lesson) }}</span>
            </template>
          </div>
          <h2 id="resume-heading" class="resume-title">
            {{ getLessonDetailTitle(activeResume.course, activeResume.lesson) }}
          </h2>
          <div v-if="activeResume.headingTitle" class="resume-bookmark">
            <svg class="resume-bookmark-icon" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z" />
            </svg>
            <span>Đang đọc: <strong>{{ activeResume.headingTitle }}</strong></span>
          </div>
        </div>

        <div class="resume-action">
          <a class="study-button primary resume-cta-btn" :href="studyLink(activeResumeLink)">
            <span>Tiếp tục học</span>
            <span class="cta-arrow" aria-hidden="true">→</span>
          </a>
        </div>
      </div>
    </section>
    <section id="hoc-phan" aria-labelledby="course-heading">
      <div class="section-heading">
        <h2 id="course-heading">Học phần</h2>
        <label v-if="catalog.length >= 6" class="course-search">
          <span>Tìm học phần</span>
          <input v-model="query" type="search" placeholder="Tìm theo tên môn hoặc chủ đề">
        </label>
      </div>
      <div class="course-list">
        <a v-for="course in visibleCourses" :key="course.id" class="course-row" :href="studyLink(`/${course.id}/`)">
          <div class="course-copy">
            <h3>{{ course.name }}</h3>
          </div>
          <span class="course-end">{{ course.lessons.length }} {{ course.presentation === 'philosophy' ? 'chương' : 'bài' }}</span>
        </a>
      </div>
      <p v-if="!visibleCourses.length" class="empty-state" role="status">Không tìm thấy học phần. Thử tên môn hoặc chủ đề khác.</p>
    </section>
  </main>
</template>
