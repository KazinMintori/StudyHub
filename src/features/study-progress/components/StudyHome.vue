<script setup>
import { useStudyHome } from '../controllers/useStudyHome.js'
import { studyLink } from '../../../core/routing/links.js'
import CourseArt from '../../illustrations/components/CourseArt.vue'
import HeroArt from '../../illustrations/components/HeroArt.vue'
import SpotArt from '../../illustrations/components/SpotArt.vue'

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

const totalLessons = catalog.reduce((sum, course) => sum + course.lessons.length, 0)
const tools = [
  { name: 'wiki', tone: 'lam', title: 'Wiki thuật ngữ', text: 'Tra định nghĩa, ví dụ và câu hỏi ôn lại của từng khái niệm nền.', href: '/wiki/' },
  { name: 'tools', tone: 'hong', title: 'Góc học tập', text: 'Flashcard, sổ ghi chú và hẹn giờ tập trung trong một chỗ.', href: '/goc-hoc-tap' },
  { name: 'guide', tone: 'ngoc', title: 'Hướng dẫn học', text: 'Cách đọc một bài: Notes, Slides, Kiến thức nền và Bài tập.', href: '/guide/' }
]
</script>

<template>
  <main class="study-home">
    <section class="home-hero" aria-labelledby="home-title">
      <div class="home-hero-copy">
        <header class="home-intro">
          <p class="home-eyebrow">Không gian tự học cho sinh viên UET</p>
          <h1 id="home-title">Bài giảng ôn tập cho sinh viên UET</h1>
          <p class="home-lead">
            {{ catalog.length }} học phần, {{ totalLessons }} bài giảng có Notes, Slides, Kiến thức nền và bài tập có lời giải.
          </p>
        </header>

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
                <span>{{ resume ? 'Tiếp tục học' : 'Học bài đầu tiên' }}</span>
                <span class="cta-arrow" aria-hidden="true">→</span>
              </a>
            </div>
          </div>
        </section>
      </div>
      <div class="home-hero-art"><HeroArt /></div>
    </section>

    <section id="hoc-phan" aria-labelledby="course-heading">
      <div class="section-heading">
        <div>
          <h2 id="course-heading">Học phần</h2>
          <p class="section-subtitle">Chọn một môn để xem lộ trình bài giảng và phần ôn luyện.</p>
        </div>
        <label v-if="catalog.length >= 6" class="course-search">
          <span>Tìm học phần</span>
          <span class="course-search-field">
            <svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true"><circle cx="8.5" cy="8.5" r="5.5" fill="none" stroke="currentColor" stroke-width="1.8" /><path d="M13 13l4 4" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" /></svg>
            <input v-model="query" type="search" placeholder="Tìm theo tên môn hoặc chủ đề">
          </span>
        </label>
      </div>
      <div class="course-list">
        <a
          v-for="(course, index) in visibleCourses"
          :key="course.id"
          class="course-row"
          :style="{ '--card-index': index }"
          :href="studyLink(`/${course.id}/`)"
        >
          <div class="course-card-art"><CourseArt :course="course" /></div>
          <div class="course-copy">
            <h3>{{ course.name }}</h3>
            <p v-if="course.description" class="course-summary">{{ course.description }}</p>
          </div>
          <span class="course-end">
            <span>{{ course.lessons.length }} {{ course.presentation === 'philosophy' ? 'chương' : 'bài' }}</span>
            <span class="course-open" aria-hidden="true">→</span>
          </span>
        </a>
      </div>
      <div v-if="!visibleCourses.length" class="empty-state empty-state-art" role="status">
        <SpotArt name="empty" />
        <p>Không tìm thấy học phần. Thử tên môn hoặc chủ đề khác.</p>
      </div>
    </section>

    <section class="home-tools" aria-labelledby="tools-heading">
      <h2 id="tools-heading">Góc học tập</h2>
      <div class="home-tool-grid">
        <a v-for="tool in tools" :key="tool.name" class="home-tool" :href="studyLink(tool.href)">
          <SpotArt :name="tool.name" :tone="tool.tone" />
          <span class="home-tool-copy">
            <strong>{{ tool.title }}</strong>
            <span>{{ tool.text }}</span>
          </span>
        </a>
      </div>
    </section>
  </main>
</template>
