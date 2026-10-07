<script setup>
import { computed, ref, onMounted } from 'vue'
import { studyLink as withBase } from './links'
import FocusTimer from './FocusTimer.vue'
import { courses } from './data'
import { readStored } from './storage'
import { migrateProgress } from './progress-migration'

const query = ref(''), last = ref(null), completed = ref({})
const normalize = text => text.toLocaleLowerCase('vi').normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g, 'd')
const visibleCourses = computed(() => courses.filter(c => normalize(`${c.name} ${c.tags}`).includes(normalize(query.value))))
const doneCount = computed(() => Object.values(completed.value).filter(Boolean).length)
onMounted(() => { migrateProgress(); last.value = readStored('studyhub_last_lesson', null); completed.value = readStored('studyhub_completed', {}) || {} })
</script>

<template>
  <main class="study-home">
    <section class="home-intro">
      <div class="intro-copy">
        <div class="hero-brand">
          <img class="hero-logo light-only" :src="withBase('/logo.png')" alt="UET Polytechnic Logo" />
          <img class="hero-logo dark-only" :src="withBase('/logo-dark.png')" alt="UET Polytechnic Logo" />
        </div>
        <p class="eyebrow">UETỆ <span>/</span> KHÔNG GIAN TỰ HỌC</p>
        <h1>Học hiểu bản chất.<br><span>Ôn tập có hệ thống.</span></h1>
        <p class="intro-description">Bài giảng, công thức và ví dụ được sắp xếp theo từng học phần. Bắt đầu từ điều chưa hiểu, học từng chút một.</p>
        <div class="button-row"><a class="study-button primary" href="#hoc-phan">Chọn học phần <span aria-hidden="true">→</span></a><a class="text-link" :href="withBase('/guide/')">Cách học với UETệ <span aria-hidden="true">↗</span></a></div>
        <div class="intro-meta"><span>{{ courses.length.toString().padStart(2, '0') }} học phần</span><span>Tìm kiếm toàn bộ bài giảng</span><span>Sáng & tối</span></div>
      </div>
      <aside class="start-panel">
        <div class="start-panel-top"><span>{{ last ? 'TIẾP TỤC HỌC' : 'GỢI Ý BẮT ĐẦU' }}</span><img class="start-panel-logo" :src="withBase('/favicon.png')" alt="UET" /></div>
        <p class="small">{{ last ? 'Bài học gần nhất của bạn' : 'Biểu diễn tri thức & Tìm kiếm' }}</p>
        <h2>{{ last?.title || 'Tìm kiếm mù: BFS, DFS, UCS & IDS' }}</h2>
        <p>Đọc lý thuyết, theo dõi ví dụ từng bước, rồi tự kiểm tra lại kiến thức.</p>
        <a :href="withBase(last?.path || '/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu')">{{ last ? 'Tiếp tục bài học' : 'Mở bài học' }} <span aria-hidden="true">→</span></a>
        <div class="start-panel-footer">{{ doneCount ? `${doneCount} bài đã đánh dấu hoàn thành` : 'Tiến độ học được lưu trên trình duyệt của bạn' }}</div>
      </aside>
    </section>

    <div class="home-body">
      <section id="hoc-phan" class="course-section" aria-labelledby="course-heading">
        <div class="section-heading"><div><p class="eyebrow">THƯ VIỆN BÀI GIẢNG</p><h2 id="course-heading">Học phần</h2></div><span class="small">Tất cả môn học</span></div>
        <label class="course-search"><span>Lọc học phần</span><input v-model="query" type="search" placeholder="Tên môn hoặc chủ đề…"></label>
        <div class="course-list">
          <a v-for="course in visibleCourses" :key="course.id" class="course-row" :href="withBase(`/${course.id}/`)">
            <span class="course-number">{{ course.code }}</span>
            <div class="course-copy"><h3>{{ course.name }}</h3><p>{{ course.description }}</p><span class="course-tags">{{ course.tags }}</span></div>
            <div class="course-end"><span>{{ course.count ? `${course.count} bài giảng` : 'Lộ trình học' }}</span><span class="course-arrow" aria-hidden="true">↗</span></div>
          </a>
          <p v-if="!visibleCourses.length" class="empty-state">Không tìm thấy học phần. Thử tên môn hoặc chủ đề khác.</p>
        </div>
      </section>
      <aside class="study-side">
        <FocusTimer />
        <section class="tool-panel"><p class="eyebrow">HỌC CHỦ ĐỘNG</p><h2>Đọc. Nhớ. Tự giải thích.</h2><p>Biến bài giảng thành kiến thức của bạn với các công cụ nhỏ, dùng ngay trên web.</p><a :href="withBase('/goc-hoc-tap#flashcards')"><span>Flashcard ôn tập</span><span aria-hidden="true">→</span></a><a :href="withBase('/goc-hoc-tap#notes')"><span>Sổ ghi chú Markdown</span><span aria-hidden="true">→</span></a><a :href="withBase('/goc-hoc-tap#simulation')"><span>Mô phỏng điện trường</span><span aria-hidden="true">→</span></a></section>
      </aside>
    </div>
    <section class="home-footnote"><span class="eyebrow">MỘT CÁCH HỌC RÕ RÀNG HƠN</span><p>Hiểu bằng lời của mình. Kiểm tra bằng bài tập. Ghi lại điều còn vướng.</p><a :href="withBase('/guide/')">Xem hướng dẫn học <span aria-hidden="true">→</span></a></section>
  </main>
</template>
