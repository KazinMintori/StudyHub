<script setup>
import { computed } from 'vue'
import { useCourseOverview } from '../controllers/useCourseOverview.js'
import PhilosophyCourse from '../../philosophy/components/PhilosophyCourse.vue'
import CourseArt from '../../illustrations/components/CourseArt.vue'
import { isExtendedCourse, getCourseSource, resolveCollectionBreadcrumbs } from '../../../content/collections.mjs'

const {
  frontmatter,
  course,
  review,
  view,
  lessons,
  primaryLessonCount,
  supplementCount,
  groups,
  syncView,
  studyLink,
  lecturePath,
  topicPath,
} = useCourseOverview()

const isExtended = computed(() => isExtendedCourse(course.value))
const source = computed(() => getCourseSource(course.value))
const breadcrumbs = computed(() => resolveCollectionBreadcrumbs(course.value))
const sourceHostname = computed(() => {
  const url = source.value?.url
  if (!url) return ''
  try {
    return new URL(url).hostname.replace(/^www\./, '')
  } catch {
    return String(url)
  }
})
</script>

<template>
  <PhilosophyCourse v-if="course?.presentation === 'philosophy'" />
  <main v-else-if="course" class="course-overview course-shell">
    <nav class="book-breadcrumbs" aria-label="Đường dẫn">
      <template v-for="crumb in breadcrumbs" :key="crumb.link">
        <a :href="studyLink(crumb.link)">{{ crumb.label }}</a>
        <span aria-hidden="true">/</span>
      </template>
      <span>{{ course.name }}</span>
    </nav>

    <header class="course-hero">
      <div class="course-hero-copy">
        <div v-if="isExtended" class="course-collection-pill">Học liệu mở rộng</div>
        <h1>{{ course.name }}</h1>
        <p class="course-description">{{ course.description }}</p>
      </div>
      <div class="course-hero-art"><CourseArt :course="course" /></div>
    </header>

    <section v-if="source" class="course-source-card" aria-labelledby="source-card-heading">
      <div class="source-card-badge">Tài liệu gốc</div>
      <div class="source-card-content">
        <div class="source-card-main">
          <h2 id="source-card-heading" class="source-card-title">{{ source.title }}</h2>
          <p class="source-card-authors">
            <strong>Tác giả:</strong> {{ Array.isArray(source.authors) ? source.authors.join(', ') : source.authors }}
            <template v-if="source.edition"> · Ấn bản {{ source.edition }}</template>
            <template v-if="source.year"> ({{ source.year }})</template>
            <template v-if="source.publisher"> · {{ source.publisher }}</template>
          </p>
        </div>
        <div class="source-card-link-wrap">
          <a v-if="source.url" :href="source.url" target="_blank" rel="noopener noreferrer" class="source-external-link">
            <span>{{ sourceHostname }}</span>
            <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" />
              <polyline points="15 3 21 3 21 9" />
              <line x1="10" y1="14" x2="21" y2="3" />
            </svg>
          </a>
        </div>
      </div>
    </section>

    <div class="course-meta">
      <span>{{ primaryLessonCount }} {{ isExtended ? 'chương' : 'bài giảng' }}</span>
      <span v-if="supplementCount">{{ supplementCount }} chuyên đề bổ trợ</span>
      <a :href="studyLink(`/goc-hoc-tap?mon=${course.id}`)">Góc học tập của môn</a>
      <a :href="studyLink(`/${course.id}/bai-tap`)">{{ course.problemSets ? 'Problem Set' : 'Bài tập ôn luyện' }}</a>
      <a v-if="course.id === 'xu-ly-du-lieu'" :href="studyLink(`/${course.id}/on-thi/`)">Ôn thi</a>
      <a v-if="course.id === 'xu-ly-du-lieu'" :href="studyLink(`/${course.id}/de-thi/`)">Đề thi</a>
      <a :href="studyLink(`/${course.id}/notes/lo-trinh`)">Lộ trình và tài liệu</a>
    </div>

    <nav v-if="review" class="workspace-tabs course-overview-tabs" aria-label="Nội dung môn học">
      <a :href="studyLink(`/${course.id}/`)" :aria-current="view === 'bai-giang' ? 'page' : undefined">Bài giảng</a>
      <a :href="studyLink(`/${course.id}/on-luyen`)" :aria-current="view === 'on-luyen' ? 'page' : undefined">Ôn luyện</a>
    </nav>

    <div v-if="view === 'bai-giang'" id="bai-giang">
      <section v-for="group in groups" :id="group.id" :key="group.title" class="course-part-section">
        <header class="part-banner">
          <h2>
            <a v-if="group.link" :href="studyLink(group.link)">{{ group.title }}</a>
            <template v-else>{{ group.title }}</template>
          </h2>
          <p v-if="group.description" class="part-description">{{ group.description }}</p>
        </header>
        <div class="lecture-list">
          <article v-for="lesson in group.entries" :key="lesson.slug">
            <a class="lecture-row" :href="studyLink(lecturePath(course.id, lesson.slug))">
              <span class="lesson-number">{{ lesson.displayNumber ?? lesson.number ?? (course?.lessons ? course.lessons.indexOf(lesson) + 1 : '') }}</span>
              <div class="lecture-list-copy">
                <h3>{{ lesson.title }}</h3>
              </div>
              <span v-if="lesson.status !== 'ready'" class="lesson-status">Bản nháp</span>
            </a>
          </article>
        </div>
      </section>
    </div>

    <div v-else-if="review" id="on-luyen">
      <section v-for="group in review.topicGroups" :key="group.title" class="course-part-section">
        <header class="part-banner">
          <h2>{{ group.title }}</h2>
          <p class="part-description">{{ group.description }}</p>
        </header>
        <div class="lecture-list">
          <article v-for="(topic, index) in group.topics" :key="topic.slug">
            <a class="lecture-row" :href="studyLink(topicPath(course.id, review.slug, topic.slug))">
              <span class="lesson-number">{{ index + 1 }}</span>
              <div class="lecture-list-copy">
                <h3>{{ topic.title }}</h3>
              </div>
            </a>
          </article>
        </div>
      </section>
      <div class="course-meta"><a :href="studyLink(lecturePath(course.id, review.slug))">Tổng hợp ôn luyện</a></div>
    </div>
  </main>
</template>
