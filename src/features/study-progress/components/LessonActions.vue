<script setup>
import { useLessonActions } from '../controllers/useLessonActions.js'
import { lecturePath } from '../../lecture/services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'

const {
  course,
  nextLesson,
  part,
  readable,
  storageMessage
} = useLessonActions()
</script>

<template>
  <section v-if="readable && (nextLesson || storageMessage)" v-show="part === 'notes'" class="lesson-actions">
    <nav v-if="nextLesson" aria-label="Sau bài học">
      <a class="text-link" :href="studyLink(lecturePath(course.id, nextLesson.slug))">
        Tiếp: {{ nextLesson.title }}
      </a>
    </nav>
    <p v-if="storageMessage" role="status">{{ storageMessage }}</p>
  </section>
</template>
