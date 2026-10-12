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

const mathAiChapters = {
  'bai-00-on-tap-nen-tang': 'Phần 0. Nền tảng giải tích & ma trận',
  'bai-01-nhap-mon-toi-uu': 'Phần 1. Tối ưu lồi: Tập lồi, hàm lồi & bài toán tối ưu',
  'bai-02-tap-loi': 'Phần 2. Các lớp bài toán tối ưu lồi',
  'bai-03-doi-ngau-lagrange': 'Phần 3. Đối ngẫu Lagrange & điều kiện KKT',
  'bai-04-gradient-newton': 'Phần 4. Phương pháp Gradient, Newton & điểm trong',
  'bai-05-toi-uu-huan-luyen': 'Phần 5. Tối ưu trong huấn luyện mô hình sâu',
  'bai-06-phuong-phap-thich-nghi': 'Phần 6. Phương pháp thích nghi & mở rộng',
  'bai-07-quy-hoach-tuyen-tinh-va-dong': 'Phần 7. Quy hoạch tuyến tính & quy hoạch động'
}

function getLessonChapter(course, lesson) {
  if (!course || !lesson) return ''
  if (course.id === 'toan-cho-ai' && mathAiChapters[lesson.slug]) {
    return mathAiChapters[lesson.slug]
  }
  const part = course.parts?.find(p => p.lessons?.includes(lesson.slug))
  if (part && part.title && part.title !== 'Bài giảng') {
    return part.title
  }
  return part?.title || ''
}

function getLessonDetailTitle(course, lesson) {
  if (!course || !lesson) return ''
  const num = lesson.number ?? (course.lessons.indexOf(lesson) + 1)
  if (/^bài\s*\d+/i.test(lesson.title)) {
    return lesson.title
  }
  return `Bài ${num}: ${lesson.title}`
}

const resume = computed(() => {
  const saved = lastLesson.value
  const path = canonicalLesson(saved?.path)
  const course = courseCatalog.find(c => c.lessons.some(l => l.status === 'ready' && progressKey(c, l) === path))
  if (!course) return null
  const lesson = course.lessons.find(l => progressKey(course, l) === path)
  return { course, lesson, path, heading: typeof saved.heading === 'string' ? saved.heading : '' }
})
const resumeLink = computed(() => resume.value ? `${resume.value.path}#${resume.value.heading || 'notes'}` : '')

const defaultStarter = computed(() => {
  for (const course of courseCatalog) {
    const lesson = course.lessons.find(l => l.status === 'ready')
    if (lesson) {
      return {
        course,
        lesson,
        path: `/${course.id}/bai-giang/${lesson.slug}`
      }
    }
  }
  return null
})

const activeResume = computed(() => resume.value || defaultStarter.value)
const activeResumeLink = computed(() => {
  if (resume.value) return resumeLink.value
  if (defaultStarter.value) return defaultStarter.value.path
  return ''
})
</script>
<template>
  <main class="study-home">
    <header class="home-intro"><h1>Bài giảng ôn tập cho sinh viên UET</h1></header>
    
    <section v-if="activeResume" class="resume-panel" aria-labelledby="resume-heading">
      <div class="resume-card-inner">
        <div class="resume-copy">
          <div class="resume-header-row">
            <span class="course-badge">{{ activeResume.course.name }}</span>
            <span v-if="getLessonChapter(activeResume.course, activeResume.lesson)" class="resume-chapter-tag">
              {{ getLessonChapter(activeResume.course, activeResume.lesson) }}
            </span>
          </div>
          <h2 id="resume-heading" class="resume-title">
            {{ getLessonDetailTitle(activeResume.course, activeResume.lesson) }}
          </h2>
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
