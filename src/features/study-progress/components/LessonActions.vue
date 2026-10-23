<script setup>
import { useLessonActions } from '../controllers/useLessonActions.js'
import { lecturePath } from '../../lecture/services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'
const { course, nextLesson, part, readable, storageMessage } = useLessonActions()
</script>

<template>
  <section v-if="readable" v-show="part === 'notes'" class="lesson-actions">
    <nav v-if="nextLesson" aria-label="Sau bài học" class="next-lesson-nav">
      <a class="text-link next-lesson-link" :href="studyLink(lecturePath(course.id, nextLesson.slug))">
        Tiếp: {{ nextLesson.title }}
      </a>
    </nav>
    <p v-if="storageMessage" role="status" class="storage-notice">{{ storageMessage }}</p>
  </section>
</template>
