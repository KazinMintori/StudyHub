<script setup>
import { computed, ref, watch, onMounted, onUnmounted } from 'vue'
import { useLecture } from './lecture-state'
import { lectureSlides, lectureCheatsheet } from '../lecture-model.mjs'
import { concepts } from '../concepts.mjs'
import { studyLink } from './links'
import MathText from './MathText.vue'

const { course, lesson, part } = useLecture()
const cheatsheet = computed(() => lectureCheatsheet(course.value, lesson.value))
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
  </div>
</template>
