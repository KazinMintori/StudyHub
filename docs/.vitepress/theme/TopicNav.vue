<script setup>
import { computed, onMounted, watch } from 'vue'
import { useRoute } from 'vitepress'
import { useTopic } from './topic-state'
import { lecturePath, topicPath } from '../lecture-model.mjs'
import { studyLink } from './links'
import { readStored, writeStored } from './storage'

const route = useRoute()
const { course, lesson, topics, index, topic, previous, next, nextLesson } = useTopic()
const groups = computed(() => (lesson.value?.topicGroups || []).map(group => ({
  title: group.title,
  items: group.topics.map(item => ({ ...item, number: topics.value.findIndex(t => t.slug === item.slug) + 1 }))
})))

function remember() {
  if (!course.value || !lesson.value || !topic.value) return
  const path = `${topicPath(course.value.id, lesson.value.slug, topic.value.slug)}.html`
  const previousEntry = readStored('studyhub_last_lesson', null)
  writeStored('studyhub_last_lesson', { ...(previousEntry?.path === path ? previousEntry : {}), path, title: `${lesson.value.title}: ${topic.value.title}` })
}
onMounted(remember)
watch(() => route.path, remember)
</script>

<template>
  <section v-if="course && lesson && topic" class="topic-nav" aria-label="Chuyển giữa các chủ đề">
    <div class="topic-nav-cards">
      <a v-if="previous" class="topic-card previous" :href="studyLink(topicPath(course.id, lesson.slug, previous.slug))">
        <span class="topic-card-label">← Chủ đề trước · {{ index }}</span>
        <span class="topic-card-title">{{ previous.title }}</span>
      </a>
      <a v-else class="topic-card previous" :href="studyLink(lecturePath(course.id, lesson.slug))">
        <span class="topic-card-label">← Trang chương</span>
        <span class="topic-card-title">{{ lesson.title }}</span>
      </a>
      <a v-if="next" class="topic-card next" :href="studyLink(topicPath(course.id, lesson.slug, next.slug))">
        <span class="topic-card-label">Chủ đề tiếp theo · {{ index + 2 }} →</span>
        <span class="topic-card-title">{{ next.title }}</span>
        <span class="topic-card-question">{{ next.question }}</span>
      </a>
      <a v-else-if="nextLesson" class="topic-card next" :href="studyLink(lecturePath(course.id, nextLesson.slug))">
        <span class="topic-card-label">Hết chương · bài giảng tiếp theo →</span>
        <span class="topic-card-title">{{ nextLesson.title }}</span>
        <span class="topic-card-question">Trước khi sang bài mới, hãy quay lại trang chương để làm phần bài tập tổng hợp.</span>
      </a>
    </div>
    <details class="topic-outline">
      <summary>Toàn bộ chủ đề của {{ `Lecture ${String(lesson.number ?? 0).padStart(2, '0')}` }}</summary>
      <div v-for="group in groups" :key="group.title" class="topic-outline-group">
        <p>{{ group.title }}</p>
        <ol>
          <li v-for="item in group.items" :key="item.slug" :value="item.number">
            <a :href="studyLink(topicPath(course.id, lesson.slug, item.slug))" :aria-current="item.slug === topic.slug ? 'page' : undefined">{{ item.title }}</a>
          </li>
        </ol>
      </div>
      <a class="text-link" :href="studyLink(lecturePath(course.id, lesson.slug))">Về trang chương: bản đồ, Slides và Kiến thức nền</a>
    </details>
  </section>
</template>
