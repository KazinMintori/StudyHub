<script setup>
import { studyLink as withBase } from '../../../core/routing/links.js'
import FieldSimulation from '../../labs/components/FieldSimulation.vue'
import { courses as defaultCourses } from '../data/course-options.mjs'
import { storageMessage } from '../../../core/storage/index.js'
import { useWorkspaceTabs } from '../controllers/useWorkspaceTabs.js'
import FlashcardDeck from './FlashcardDeck.vue'
import StudyNotebook from './StudyNotebook.vue'
import FocusTimer from './FocusTimer.vue'

const props = defineProps({
  courses: {
    type: Array,
    default: () => defaultCourses
  }
})

const {
  tabs,
  active,
  changeTab
} = useWorkspaceTabs()
</script>

<template>
  <main class="study-workspace">
    <header class="workspace-heading">
      <a class="small text-link" :href="withBase('/')">← Trang chủ</a>
      <h1>Góc học tập</h1>
      <p>Flashcard, ghi chú, hẹn giờ và mô phỏng để ôn bài.</p>
    </header>
    <nav class="workspace-tabs" aria-label="Công cụ học tập">
      <a
        v-for="tab in tabs"
        :key="tab.id"
        :href="`#${tab.id}`"
        :aria-current="active === tab.id ? 'page' : undefined"
        @click.prevent="changeTab(tab.id)"
      >{{ tab.name }}</a>
    </nav>
    <p v-if="storageMessage" class="storage-message" role="status">{{ storageMessage }}</p>

    <FlashcardDeck v-show="active === 'flashcards'" :courses="courses" />

    <StudyNotebook v-show="active === 'notes'" :courses="courses" />

    <section v-show="active === 'simulation'" id="simulation" class="workspace-section" aria-labelledby="simulation-heading">
      <h2 id="simulation-heading">Nhìn thấy hướng của điện trường</h2>
      <FieldSimulation />
    </section>

    <section v-show="active === 'focus'" id="focus" class="workspace-section workspace-focus">
      <FocusTimer />
      <div>
        <h2>Hẹn giờ tập trung</h2>
        <ol class="focus-guide">
          <li>Chọn một bài hoặc một câu hỏi cụ thể.</li>
          <li>Bắt đầu phiên 25 hoặc 50 phút.</li>
          <li>Ghi lại điều chưa hiểu để xử lý sau.</li>
          <li>Dành 5 phút nghỉ trước phiên tiếp theo.</li>
        </ol>
        <a class="text-link" :href="withBase('/guide/')">Đọc thêm về phương pháp học</a>
      </div>
    </section>
  </main>
</template>
