<script setup>
import { computed, ref, watch, onMounted, onUnmounted } from 'vue'
import { useLecture } from './lecture-state'
import { lectureSlides, lectureCheatsheet, lectureLab } from '../lecture-model.mjs'
import { concepts } from '../concepts.mjs'
import { studyLink } from './links'
import MathText from './MathText.vue'

const { course, lesson, part } = useLecture()
const cheatsheet = computed(() => lectureCheatsheet(course.value, lesson.value))
const lab = computed(() => lectureLab(course.value, lesson.value))
const activeApproach = ref({})
function getApproach(taskId) { return activeApproach.value[taskId] || 'advanced' }
function setApproach(taskId, mode) { activeApproach.value = { ...activeApproach.value, [taskId]: mode } }
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

    <section v-else-if="part === 'bai-tap'" class="lecture-exercises" aria-label="Bài tập thực hành phòng Lab của bài giảng">
      <div v-if="lab" class="lab-container">
        <header class="lab-header">
          <div class="lab-title-group">
            <p class="eyebrow">PHÒNG LAB THỰC HÀNH · {{ (course.short || course.name).toUpperCase() }}</p>
            <h2>{{ lab.title }}</h2>
          </div>
        </header>

        <!-- Thẻ thông tin tập dữ liệu sử dụng -->
        <article v-if="lab.dataset" class="dataset-card">
          <div class="dataset-header">
            <div class="dataset-meta">
              <span class="dataset-badge">{{ lab.dataset.type }}</span>
              <h3 class="dataset-name">{{ lab.dataset.name }}</h3>
            </div>
            <div class="dataset-actions">
              <a :href="lab.dataset.url" target="_blank" rel="noopener noreferrer" class="study-button primary dataset-download-btn">
                <svg viewBox="0 0 20 20" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M10 3v10m0 0l-3.5-3.5M10 13l3.5-3.5M3 17h14"/></svg>
                <span>Tải / Xem Dữ liệu Gốc</span>
              </a>
              <a v-if="lab.dataset.secondary_url" :href="lab.dataset.secondary_url" target="_blank" rel="noopener noreferrer" class="study-button dataset-download-btn">
                <span>Nguồn Phụ ↗</span>
              </a>
            </div>
          </div>
          <p class="dataset-desc">{{ lab.dataset.description }}</p>
        </article>

        <!-- Danh sách các bài tập / tasks -->
        <div class="lab-tasks-list">
          <article v-for="(task, tIdx) in lab.tasks" :key="task.id" class="lab-task-card">
            <header class="task-card-header">
              <div class="task-badge">Task {{ tIdx + 1 }}</div>
              <h3>{{ task.title }}</h3>
            </header>

            <div class="task-prompt">
              <p><strong>Yêu cầu bài toán:</strong> {{ task.prompt }}</p>
            </div>

            <!-- Khối Phỏng đoán & Giả thuyết -->
            <div v-if="task.prediction" class="task-prediction">
              <div class="prediction-header">
                <svg viewBox="0 0 20 20" width="16" height="16" fill="currentColor" aria-hidden="true"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h1a1 1 0 100-2v-3a1 1 0 00-1-1H9z" clip-rule="evenodd"/></svg>
                <strong>Phỏng đoán & Giả thuyết bản chất:</strong>
              </div>
              <p>{{ task.prediction }}</p>
            </div>

            <!-- Bộ chuyển đổi 2 hướng tiếp cận -->
            <div class="task-solutions-wrapper">
              <div class="solution-tabs">
                <button
                  class="solution-tab-btn"
                  :class="{ active: getApproach(task.id) === 'basic' }"
                  @click="setApproach(task.id, 'basic')"
                >
                  Cách 1: Tiếp cận Cơ bản & Trực quan
                </button>
                <button
                  class="solution-tab-btn"
                  :class="{ active: getApproach(task.id) === 'advanced' }"
                  @click="setApproach(task.id, 'advanced')"
                >
                  Cách 2: Tiếp cận Nâng cao & Tối ưu
                </button>
              </div>

              <div class="solution-code-block">
                <pre v-if="getApproach(task.id) === 'basic'"><code>{{ task.solutionBasic }}</code></pre>
                <pre v-else><code>{{ task.solutionAdvanced }}</code></pre>
              </div>
            </div>

            <!-- Phân tích sư phạm & Lưu ý tránh bẫy -->
            <div v-if="task.explanation" class="task-explanation">
              <strong>Phân tích sư phạm & Lưu ý tránh bẫy:</strong>
              <p>{{ task.explanation }}</p>
            </div>

            <!-- Khối kiểm chứng Assertions -->
            <div v-if="task.verification" class="task-verification">
              <div class="verification-title">Kiểm chứng tính đúng đắn (Automated Assertions):</div>
              <pre><code>{{ task.verification }}</code></pre>
            </div>
          </article>
        </div>
      </div>

      <div v-else class="empty-lab-state">
        <div class="foundations-heading">
          <h2>Bài tập thực hành: {{ lesson.title }}</h2>
        </div>
        <p>Hệ thống bài tập thực hành chuyên sâu của bài học này đang được hoàn thiện. Bạn có thể xem các bài tập minh họa nằm xen kẽ ngay trong phần lý thuyết Notes, hoặc mở chuyên trang bài tập của toàn bộ môn học.</p>
        <div class="button-row" style="margin-top: 1rem;">
          <a class="study-button primary" :href="studyLink(`/${course.id}/bai-tap`)">Toàn bộ bài tập của môn học →</a>
        </div>
      </div>
    </section>
  </div>
</template>

<style scoped>
.lab-container {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
  color: var(--ink);
  font-family: var(--font-ui);
}
.lab-header {
  margin-bottom: var(--space-2);
}
.lab-title-group h2 {
  font-size: var(--fs-h2);
  font-weight: 700;
  margin: var(--space-1) 0 0;
  line-height: 1.3;
}
.dataset-card {
  background: var(--canvas);
  border: 1px solid var(--rule);
  border-left: 4px solid var(--tim);
  border-radius: var(--radius);
  padding: var(--space-4) var(--space-5);
  box-shadow: 0 1px 3px rgba(0,0,0,0.04);
}
.dataset-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: var(--space-4);
  flex-wrap: wrap;
  margin-bottom: var(--space-2);
}
.dataset-meta {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}
.dataset-badge {
  display: inline-block;
  align-self: flex-start;
  font-size: var(--fs-small);
  font-weight: 600;
  color: var(--tim);
  background: var(--tim-soft);
  padding: 2px 8px;
  border-radius: 4px;
}
.dataset-name {
  font-size: var(--fs-read);
  font-weight: 600;
  margin: 0;
}
.dataset-actions {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
}
.dataset-download-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-size: var(--fs-small);
  padding: 6px 12px;
  min-height: 36px;
  text-decoration: none;
}
.dataset-desc {
  font-size: var(--fs-ui);
  color: var(--ink-2);
  line-height: 1.6;
  margin: 0;
}
.lab-tasks-list {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}
.lab-task-card {
  background: var(--paper);
  border: 1px solid var(--rule);
  border-radius: var(--radius-lg);
  padding: var(--space-5);
  box-shadow: 0 2px 6px rgba(0,0,0,0.03);
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}
.task-card-header {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  border-bottom: 1px solid var(--rule);
  padding-bottom: var(--space-3);
}
.task-badge {
  font-size: var(--fs-small);
  font-weight: 700;
  color: #fff;
  background: var(--tim);
  padding: 2px 8px;
  border-radius: 4px;
  flex-shrink: 0;
}
.task-card-header h3 {
  font-size: var(--fs-read);
  font-weight: 600;
  margin: 0;
  line-height: 1.4;
}
.task-prompt p {
  font-size: var(--fs-ui);
  line-height: 1.65;
  margin: 0;
  color: var(--ink);
}
.task-prediction {
  background: var(--vang-soft);
  border-left: 3px solid var(--vang);
  padding: var(--space-3) var(--space-4);
  border-radius: 0 var(--radius) var(--radius) 0;
}
.prediction-header {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  color: #b45309;
  font-size: var(--fs-small);
  margin-bottom: var(--space-1);
}
.task-prediction p {
  font-size: var(--fs-ui);
  line-height: 1.6;
  color: var(--ink);
  margin: 0;
}
.task-solutions-wrapper {
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  overflow: hidden;
  background: var(--canvas);
}
.solution-tabs {
  display: flex;
  background: var(--paper);
  border-bottom: 1px solid var(--rule);
}
.solution-tab-btn {
  flex: 1;
  padding: var(--space-2) var(--space-4);
  font-size: var(--fs-small);
  font-weight: 600;
  color: var(--ink-3);
  background: transparent;
  border: none;
  border-bottom: 2px solid transparent;
  cursor: pointer;
  transition: all 0.15s ease;
  min-height: 40px;
}
.solution-tab-btn:hover {
  color: var(--tim);
}
.solution-tab-btn.active {
  color: var(--tim);
  border-bottom-color: var(--tim);
  background: var(--canvas);
}
.solution-code-block pre {
  margin: 0;
  padding: var(--space-4);
  background: #1e1e2e;
  color: #cdd6f4;
  overflow-x: auto;
  font-size: 13.5px;
  line-height: 1.6;
  font-family: var(--font-mono, monospace);
}
.task-explanation {
  background: var(--xanh-soft);
  border-left: 3px solid var(--xanh);
  padding: var(--space-3) var(--space-4);
  border-radius: 0 var(--radius) var(--radius) 0;
  font-size: var(--fs-ui);
  line-height: 1.6;
  color: var(--ink);
}
.task-explanation p {
  margin: var(--space-1) 0 0;
}
.task-verification {
  background: var(--canvas);
  border: 1px solid var(--rule);
  border-radius: var(--radius);
  padding: var(--space-3) var(--space-4);
}
.verification-title {
  font-size: var(--fs-small);
  font-weight: 600;
  color: var(--ink-2);
  margin-bottom: var(--space-2);
}
.task-verification pre {
  margin: 0;
  padding: var(--space-3);
  background: #24273a;
  color: #a6da95;
  border-radius: 4px;
  overflow-x: auto;
  font-size: 13px;
  line-height: 1.5;
  font-family: var(--font-mono, monospace);
}
@media (max-width: 767px) {
  .dataset-header {
    flex-direction: column;
    align-items: stretch;
  }
  .dataset-actions {
    flex-direction: column;
  }
  .solution-tabs {
    flex-direction: column;
  }
}
</style>
