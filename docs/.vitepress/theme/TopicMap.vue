<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { findLecture, lessonTopics, topicPath, topicMinutes } from '../lecture-model.mjs'
import { studyLink } from './links'

// Bản đồ chủ đề đặt trong Notes của trang chương. Dữ liệu lấy từ topicGroups trong catalog.
const props = defineProps({ group: { type: Number, default: -1 } })
const { frontmatter } = useData()
const lesson = computed(() => findLecture(frontmatter.value.course, frontmatter.value.lecture))
const numbered = computed(() => lessonTopics(lesson.value))
const groups = computed(() => (lesson.value?.topicGroups || [])
  .map((group, g) => ({ ...group, g, items: numbered.value.filter(topic => topic.groupIndex === g).map(topic => ({ ...topic, number: numbered.value.indexOf(topic) + 1 })) }))
  .filter(group => props.group < 0 || group.g === props.group))
const total = computed(() => groups.value.reduce((sum, group) => sum + group.items.reduce((s, topic) => s + topicMinutes(frontmatter.value.course, frontmatter.value.lecture, topic.slug), 0), 0))
</script>

<template>
  <div v-if="lesson && groups.length" class="topic-map">
    <p v-if="group < 0" class="topic-map-meta">{{ numbered.length }} chủ đề · tổng cộng khoảng {{ total }} phút đọc</p>
    <section v-for="item in groups" :key="item.title" class="topic-map-group">
      <h3 class="topic-map-group-title">{{ item.title }}</h3>
      <p v-if="item.description" class="topic-map-group-description">{{ item.description }}</p>
      <ol>
        <li v-for="topic in item.items" :key="topic.slug">
          <a :href="studyLink(topicPath(frontmatter.course, frontmatter.lecture, topic.slug))">
            <span class="topic-map-number">{{ topic.number }}</span>
            <span class="topic-map-copy">
              <span class="topic-map-title">{{ topic.title }}</span>
              <span class="topic-map-question">{{ topic.question }}</span>
              <span class="topic-map-source">Khoảng {{ topicMinutes(frontmatter.course, frontmatter.lecture, topic.slug) }} phút<template v-if="topic.source"> · Convex Optimization {{ topic.source }}</template></span>
            </span>
          </a>
        </li>
      </ol>
    </section>
  </div>
</template>
