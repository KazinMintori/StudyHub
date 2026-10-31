<script setup>
import { useLessonActions } from '../controllers/useLessonActions.js'
import { lecturePath } from '../../lecture/services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'
const { course, previousLesson, nextLesson, part, readable, storageMessage } = useLessonActions()
</script>

<template>
  <section v-if="readable" v-show="part === 'notes'" class="lesson-actions">
    <nav v-if="previousLesson || nextLesson" aria-label="Chuyển bài học" class="lesson-page-nav">
      <a v-if="previousLesson" class="lesson-page-link previous" rel="prev" :href="studyLink(lecturePath(course.id, previousLesson.slug))">
        <span class="lesson-page-label"><svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="m14 6-6 6 6 6M8 12h12" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" /></svg>Bài trước</span>
        <span class="lesson-page-title">{{ previousLesson.title }}</span>
      </a>
      <a v-if="nextLesson" class="lesson-page-link next" rel="next" :href="studyLink(lecturePath(course.id, nextLesson.slug))">
        <span class="lesson-page-label">Bài tiếp theo<svg viewBox="0 0 24 24" width="16" height="16" aria-hidden="true"><path d="m10 6 6 6-6 6M4 12h12" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" /></svg></span>
        <span class="lesson-page-title">{{ nextLesson.title }}</span>
      </a>
    </nav>
    <p v-if="storageMessage" role="status" class="storage-notice">{{ storageMessage }}</p>
  </section>
</template>
