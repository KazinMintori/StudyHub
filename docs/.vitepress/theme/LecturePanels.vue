<script setup>
import { computed, ref, watch, onMounted, onUnmounted } from 'vue'
import { useLecture } from './lecture-state'
import { lectureSlides, lectureCheatsheet } from '../lecture-model.mjs'
import { getCourseLab } from '../course-labs.mjs'
import { concepts } from '../concepts.mjs'
import { studyLink } from './links'
import MathText from './MathText.vue'

const { course, lesson, part } = useLecture()
const cheatsheet = computed(() => lectureCheatsheet(course.value, lesson.value))
const lab = computed(() => getCourseLab(course.value, lesson.value))
const index = ref(0)
const slides = computed(() => lectureSlides(course.value, lesson.value))
const current = computed(() => slides.value[index.value])
const required = computed(() => (lesson.value?.prerequisites || []).filter(id => concepts[id]))
const supporting = computed(() => (lesson.value?.supportingConcepts || []).filter(id => concepts[id] && !required.value.includes(id)))
const foundationGroups = computed(() => [
  {
    id: 'required',
    title: 'Cần ôn trước',
    description: 'Bài giảng dùng trực tiếp các khái niệm này mà không trình bày lại từ đầu.',
    ids: required.value
  },
  {
    id: 'supporting',
    title: 'Tra cứu trong khi đọc',
    description: 'Các thuật ngữ xuất hiện trong Notes hoặc Slides. Bạn không cần học thuộc trước; hãy mở mục tương ứng khi gặp chỗ chưa rõ.',
    ids: supporting.value
  }
].filter(group => group.ids.length))
const allFoundations = computed(() => foundationGroups.value.flatMap(group => group.ids))
function load() {
  index.value = 0
}
function next(direction) {
  index.value = Math.max(0, Math.min(slides.value.length - 1, index.value + direction))
}
function keyboard(event) {
  if (part.value !== 'slides' || /INPUT|TEXTAREA|SELECT/.test(event.target.tagName)) return
  if (event.key === 'ArrowRight') { event.preventDefault(); next(1) }
  if (event.key === 'ArrowLeft') { event.preventDefault(); next(-1) }
}

function printCheatsheet() {
  if (typeof window !== 'undefined') window.print()
}

function scrollToExercise(event) {
  if (event) event.preventDefault()
  const el = document.getElementById('bai-tap') || document.querySelector('.main > .vp-doc h2:last-of-type')
  if (el) el.scrollIntoView({ behavior: 'smooth' })
}

function selectNotes(event) {
  if (event) event.preventDefault()
  part.value = 'notes'
  if (typeof window !== 'undefined') {
    window.location.hash = '#notes'
  }
}

onMounted(() => { load(); window.addEventListener('keydown', keyboard) })
onUnmounted(() => { window.removeEventListener('keydown', keyboard) })
watch(() => lesson.value?.slug, load)
</script>

<template>
  <div v-if="course && lesson" class="lecture-panels">
    <section v-if="part === 'slides'" class="lecture-slides" aria-label="Slides của bài giảng">
      <p class="eyebrow">Ý CHÍNH CỦA BÀI NÀY</p>
      <article v-if="current" class="course-slide" aria-live="polite">
        <p class="eyebrow">{{ index + 1 }} / {{ slides.length }}</p>
        <h2>{{ current.title }}</h2>
        <ul><li v-for="bullet in current.bullets" :key="bullet"><MathText :text="bullet" /></li></ul>
        <MathText v-if="current.formula" as="div" class="slide-formula" :text="current.formula" />
        <div v-if="current.example" class="slide-example"><strong>Ví dụ:</strong> <MathText :text="current.example" /></div>
      </article>
      <p v-else class="empty-state">Slides của bài đang được biên soạn.</p>
      <div v-if="current" class="slide-controls"><button class="study-button" :disabled="index === 0" @click="next(-1)">← Trước</button><span>{{ index + 1 }} / {{ slides.length }} · Phím ← →</span><button class="study-button primary" :disabled="index === slides.length - 1" @click="next(1)">Tiếp →</button></div>
    </section>

    <section v-else-if="part === 'cheatsheet'" class="lecture-cheatsheet" aria-label="Cheatsheet tra cứu nhanh của bài giảng">
      <div class="cheatsheet-heading">
        <div class="cheatsheet-title-group">
          <p class="eyebrow">TỜ TRA CỨU NHANH · CẨM NANG ÔN TẬP</p>
          <h2>Cheatsheet: {{ lesson.title }}</h2>
        </div>
        <div class="cheatsheet-actions">
          <button class="study-button print-button" @click="printCheatsheet" title="In hoặc lưu PDF trang này">
            <svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M5 7V3h10v4M5 14H3a1 1 0 0 1-1-1V9a1 1 0 0 1 1-1h14a1 1 0 0 1 1 1v4a1 1 0 0 1-1 1h-2"/><rect x="5" y="11" width="10" height="6" rx="1"/></svg>
            <span>In / PDF</span>
          </button>
        </div>
      </div>
      <p v-if="cheatsheet && cheatsheet.summary" class="cheatsheet-summary"><MathText :text="cheatsheet.summary" /></p>

      <div v-if="cheatsheet && cheatsheet.sections && cheatsheet.sections.length" class="cheatsheet-grid">
        <article v-for="section in cheatsheet.sections" :key="section.id" :class="['cheatsheet-card', `card-${section.id}`]">
          <header class="card-header">
            <h3>{{ section.title }}</h3>
            <span v-if="section.badge" class="card-badge">{{ section.badge }}</span>
          </header>

          <div v-if="section.items && section.items.length" class="card-items">
            <div v-for="(item, idx) in section.items" :key="idx" class="cheatsheet-item">
              <h4 v-if="item.name" class="item-name">{{ item.name }}</h4>

              <div v-if="item.formula" class="item-formula">
                <MathText as="div" :text="item.formula" />
              </div>

              <pre v-if="item.code" class="item-code"><code>{{ item.code }}</code></pre>

              <MathText v-if="item.description" as="p" class="item-desc" :text="item.description" />

              <ul v-if="item.bullets && item.bullets.length" class="item-bullets">
                <li v-for="(bullet, bIdx) in item.bullets" :key="bIdx"><MathText :text="bullet" /></li>
              </ul>

              <div v-if="item.warning" class="item-pitfall">
                <div class="pitfall-warning"><strong>Bẫy thi:</strong> <MathText :text="item.warning" /></div>
                <div v-if="item.correct" class="pitfall-correct"><strong>Cách hiểu đúng:</strong> <MathText :text="item.correct" /></div>
              </div>

              <div v-if="item.example" class="item-example">
                <strong>Ví dụ:</strong> <MathText :text="item.example" />
              </div>
            </div>
          </div>

          <div v-if="section.table" class="card-table-wrapper">
            <table class="card-table">
              <thead>
                <tr>
                  <th v-for="h in section.table.headers" :key="h">{{ h }}</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(row, rIdx) in section.table.rows" :key="rIdx">
                  <td v-for="(cell, cIdx) in row" :key="cIdx"><MathText :text="cell" /></td>
                </tr>
              </tbody>
            </table>
          </div>
        </article>
      </div>
      <p v-else class="empty-state">Tờ tra cứu của bài đang được biên soạn.</p>

      <footer class="cheatsheet-footer">
        <p><em>Bấm <strong>In / PDF</strong> để in hoặc lưu bản tra cứu khi ôn tập.</em></p>
      </footer>
    </section>

    <section v-else-if="part === 'kien-thuc-can-co'" class="lecture-foundations" aria-label="Kiến thức nền của bài giảng">
      <div class="foundations-heading"><h2>Kiến thức hỗ trợ cho bài này</h2></div>
      <p>Hai nhóm dưới đây giúp bạn biết phần nào cần ôn trước và phần nào chỉ cần tra cứu khi đang đọc.</p>

      <section v-for="group in foundationGroups" :key="group.id" class="foundation-group" :aria-labelledby="`foundation-group-${group.id}`">
        <h3 :id="`foundation-group-${group.id}`">{{ group.title }}</h3>
        <p>{{ group.description }}</p>
        <article v-for="id in group.ids" :id="`nen-tang-${id}`" :key="id" class="foundation-entry">
          <div class="foundation-entry-heading">
            <details>
              <summary><strong>{{ concepts[id].name }}</strong><MathText :text="concepts[id].definition.split(/(?<=[.!?])\s/)[0]" /></summary>
              <div class="foundation-content">
                <MathText as="p" :text="concepts[id].definition" />
                <h4>Ví dụ</h4><MathText as="p" :text="concepts[id].example" />
                <MathText v-if="concepts[id].notation" as="div" class="foundation-notation" :text="concepts[id].notation" />
                <p><strong>Dùng khi:</strong> <MathText :text="concepts[id].use" /></p>
                <details><summary>Câu hỏi ôn lại: <MathText :text="concepts[id].question" /></summary><MathText as="p" :text="concepts[id].answer" /></details>
                <a class="text-link" :href="studyLink(`/wiki/${id}`)">Đọc bài Wiki về {{ concepts[id].name }}</a>
              </div>
            </details>
          </div>
        </article>
      </section>
    </section>

    <section v-else-if="part === 'bai-tap'" class="lecture-lab-panel" aria-label="Bài tập thực hành phòng Lab">
      <div class="lab-heading">
        <div class="lab-title-group">
          <p class="eyebrow">BÀI TẬP THỰC HÀNH & PHÒNG LAB THỰC CHIẾN</p>
          <h2>{{ lab?.title || ('Bài tập thực hành: ' + lesson.title) }}</h2>
        </div>
        <div class="lab-actions">
          <a class="study-button" :href="studyLink(`/${course.id}/bai-tap`)">Toàn bộ bài tập của môn học →</a>
        </div>
      </div>

      <!-- Khối thông tin bộ dữ liệu thực nghiệm -->
      <aside v-if="lab && lab.dataset" class="lab-dataset-card" aria-label="Bộ dữ liệu thực nghiệm">
        <div class="dataset-header">
          <span class="dataset-badge">BỘ DỮ LIỆU THỰC NGHIỆM</span>
          <span v-if="lab.dataset.type" class="dataset-type">{{ lab.dataset.type }}</span>
        </div>
        <h3 class="dataset-name">{{ lab.dataset.name }}</h3>
        <p v-if="lab.dataset.description" class="dataset-desc">{{ lab.dataset.description }}</p>
        <div v-if="lab.dataset.url" class="dataset-link-row">
          <a class="study-button primary" :href="lab.dataset.url" target="_blank" rel="noopener noreferrer">
            <svg viewBox="0 0 20 20" width="16" height="16" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.8">
              <path d="M4 16v1a2 2 0 002 2h8a2 2 0 002-2v-1M7 10l3 3m0 0l3-3m-3 3V3"/>
            </svg>
            <span>Tải / Xem dữ liệu gốc</span>
          </a>
          <span class="dataset-url-note">{{ lab.dataset.url }}</span>
        </div>
      </aside>

      <!-- Danh sách bài tập thực chiến -->
      <div v-if="lab && lab.tasks && lab.tasks.length" class="lab-tasks-list">
        <article v-for="(task, tIdx) in lab.tasks" :key="task.id || tIdx" class="lab-task-card">
          <header class="task-header">
            <span class="task-number">BÀI {{ tIdx + 1 }}</span>
            <h3 class="task-title">{{ task.title }}</h3>
          </header>

          <!-- Yêu cầu bài toán -->
          <div class="task-prompt">
            <MathText as="p" :text="task.prompt" />
          </div>

          <!-- Phỏng đoán & Trực giác trước khi chạy mã -->
          <div v-if="task.prediction" class="task-prediction">
            <div class="prediction-header">
              <span class="prediction-icon">💡</span>
              <strong>Phỏng đoán & Trực giác bản chất trước khi chạy mã:</strong>
            </div>
            <MathText as="p" :text="task.prediction" />
          </div>

          <!-- 2 Hướng giải bài tập -->
          <div class="task-solutions">
            <div v-if="task.solutionBasic" class="solution-block solution-basic">
              <div class="solution-header">
                <span class="solution-badge basic">Cách 1</span>
                <strong>Tiếp cận Căn bản & Trực quan</strong>
              </div>
              <pre class="item-code"><code>{{ task.solutionBasic }}</code></pre>
            </div>

            <div v-if="task.solutionAdvanced" class="solution-block solution-advanced">
              <div class="solution-header">
                <span class="solution-badge advanced">Cách 2</span>
                <strong>Tiếp cận Nâng cao & Tối ưu hóa</strong>
              </div>
              <pre class="item-code"><code>{{ task.solutionAdvanced }}</code></pre>
            </div>
          </div>

          <!-- Phân tích sư phạm & Lưu ý tránh bẫy -->
          <div v-if="task.explanation" class="task-explanation">
            <div class="explanation-header">
              <strong>📌 Phân tích bản chất & Điểm mấu chốt:</strong>
            </div>
            <MathText as="p" :text="task.explanation" />
          </div>

          <!-- Mã kiểm chứng tự động (Assert) -->
          <div v-if="task.verification" class="task-verification">
            <details>
              <summary><strong>Mã kiểm chứng tự động (Assertion check)</strong></summary>
              <pre class="item-code"><code>{{ task.verification }}</code></pre>
            </details>
          </div>
        </article>
      </div>

      <!-- Trạng thái bài tập chưa có lab riêng -->
      <div v-else class="lab-empty-state">
        <p class="empty-lead">Bài tập củng cố tri thức của bài học này đã được tích hợp xuyên suốt từng mục lý thuyết trong Notes.</p>
        <p>Để luyện tập thêm các bài toán thực chiến nâng cao và làm quen với bộ câu hỏi chuẩn bị cho kỳ thi, bạn có thể tham khảo chuyên trang Bài tập của môn học:</p>
        <div class="button-row" style="margin-top: 1.25rem;">
          <a class="study-button primary" :href="studyLink(`/${course.id}/bai-tap`)">Xem bài tập tổng hợp toàn môn →</a>
          <a class="study-button" href="#notes" @click="selectNotes">Quay lại đọc bài giảng Notes</a>
        </div>
      </div>
    </section>
  </div>
</template>
