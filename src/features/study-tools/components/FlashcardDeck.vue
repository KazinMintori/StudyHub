<script setup>
import { studyLink as withBase } from '../../../core/routing/links.js'
import { useFlashcards } from '../controllers/useFlashcards.js'

const props = defineProps({
  courseId: { type: String, default: '' },
  courses: {
    type: Array,
    default: () => []
  }
})

const {
  subject,
  index,
  revealed,
  deck,
  current,
  knownCount,
  courseName,
  review,
  next,
  resetReview
} = useFlashcards({ courses: props.courses, courseId: () => props.courseId })
</script>

<template>
  <section id="flashcards" class="workspace-section" aria-labelledby="flash-heading">
    <div class="section-heading">
      <div>
        <h2 id="flash-heading">Nhớ trước khi xem đáp án</h2>
      </div>
      <label v-if="!courseId" class="select-label">
        Học phần
        <select v-model="subject">
          <option value="all">Tất cả học phần</option>
          <option v-for="c in courses" :key="c.id" :value="c.id">{{ c.name }}</option>
        </select>
      </label>
    </div>
    <div v-if="deck.length" class="flashcard-progress">
      <span>{{ knownCount }} / {{ deck.length }} thẻ đã nhớ</span>
      <progress :value="knownCount" :max="deck.length" :aria-label="`${knownCount} trên ${deck.length} thẻ đã nhớ`"></progress>
      <button class="text-link" @click="resetReview">Ôn lại từ đầu</button>
    </div>
    <article v-if="current" class="flashcard">
      <div class="flashcard-top">
        <span>{{ courseName(current.course) }}</span>
        <span>{{ index + 1 }} / {{ deck.length }}</span>
      </div>
      <p class="flashcard-question">{{ current.q }}</p>
      <div v-if="revealed" class="flashcard-answer" aria-live="polite">
        <p>{{ current.a }}</p>
        <a class="text-link" :href="withBase(current.lesson ? `/${current.course}/bai-giang/${current.lesson}#notes` : `/${current.course}/`)">Xem lại {{ current.lesson ? 'bài giảng' : 'lộ trình môn học' }}</a>
      </div>
      <button v-else class="study-button primary" @click="revealed = true">Xem đáp án</button>
    </article>
    <div v-else class="empty-state" role="status">Học phần này chưa có flashcard. Bạn có thể dùng ghi chú và danh sách việc học để tự ôn tập.</div>
    <div v-if="deck.length" class="flashcard-actions">
      <button class="study-button" @click="next(-1)">← Thẻ trước</button>
      <div v-if="revealed" class="button-row">
        <button class="study-button" @click="review(false)">Chưa nhớ</button>
        <button class="study-button success" @click="review(true)">Đã nhớ</button>
      </div>
      <button class="study-button" @click="next(1)">Thẻ tiếp →</button>
    </div>
    <p class="small tool-explanation">Thử trả lời bằng lời của mình trước khi mở đáp án. Tiến độ được lưu riêng cho từng thẻ trên trình duyệt này.</p>
  </section>
</template>
