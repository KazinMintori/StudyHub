<script setup>
import { computed, ref, watch, onMounted, onUnmounted, nextTick } from 'vue'
import { studyLink as withBase } from './links'
import MarkdownIt from 'markdown-it'
import FocusTimer from './FocusTimer.vue'
import FieldSimulation from './FieldSimulation.vue'
import { courses, cards } from './data'
import { readStored, writeStored, storageMessage } from './storage'

const tabs = [{ id: 'flashcards', name: 'Flashcard' }, { id: 'notes', name: 'Ghi chú' }, { id: 'focus', name: 'Hẹn giờ' }, { id: 'simulation', name: 'Mô phỏng' }]
const active = ref('flashcards'), subject = ref('all'), index = ref(0), revealed = ref(false), remembered = ref({})
const deck = computed(() => cards.filter(c => subject.value === 'all' || c.course === subject.value))
const current = computed(() => deck.value[index.value % deck.value.length])
const cardKey = c => `${c.course}:${c.q}`
const knownCount = computed(() => deck.value.filter(c => remembered.value[cardKey(c)]).length)
const courseName = id => courses.find(c => c.id === id)?.name
watch(subject, () => { index.value = 0; revealed.value = false })
function changeTab(id) { active.value = id; window.history.replaceState(null, '', `#${id}`) }
function syncHash() { const id = window.location.hash.slice(1); if (tabs.some(t => t.id === id)) active.value = id }
function review(known) {
  remembered.value[cardKey(current.value)] = known
  writeStored('studyhub_flashcards', remembered.value)
  index.value = (index.value + 1) % deck.value.length; revealed.value = false
}
function next(direction) { index.value = (index.value + direction + deck.value.length) % deck.value.length; revealed.value = false }
function resetReview() { for (const c of deck.value) delete remembered.value[cardKey(c)]; writeStored('studyhub_flashcards', remembered.value); index.value = 0; revealed.value = false }

const noteSubject = ref('general'), note = ref(''), loaded = ref(false), saved = ref(''), mode = ref('edit')
const markdown = new MarkdownIt({ html: false, linkify: true, breaks: true })
const renderedNote = computed(() => markdown.render(note.value))
const noteKey = () => `studyhub_note_${noteSubject.value}`
async function loadNote() {
  loaded.value = false
  let text = readStored(noteKey(), null)
  if (text === null && noteSubject.value === 'general') {
    try { text = localStorage.getItem('studyhub_notes') } catch { /* The download button remains available. */ }
  }
  note.value = typeof text === 'string' ? text : '# Ghi chú học tập\n\n## Điều mình đã hiểu\n\n- \n\n## Câu hỏi cần làm rõ\n\n- \n'
  await nextTick(); loaded.value = true; saved.value = ''
}
watch(note, () => { if (loaded.value) saveNote() })
function saveNote() { if (writeStored(noteKey(), note.value)) saved.value = 'Đã lưu trên trình duyệt' }
function downloadNote() {
  const url = URL.createObjectURL(new Blob([note.value], { type: 'text/markdown;charset=utf-8' }))
  const link = document.createElement('a'); link.href = url; link.download = `StudyHub-${noteSubject.value}.md`; link.click()
  setTimeout(() => URL.revokeObjectURL(url), 1000)
}
onMounted(() => { syncHash(); window.addEventListener('hashchange', syncHash); remembered.value = readStored('studyhub_flashcards', {}) || {}; loadNote() })
onUnmounted(() => window.removeEventListener('hashchange', syncHash))
</script>

<template>
  <main class="study-workspace">
    <header class="workspace-heading"><a class="small text-link" :href="withBase('/')">← Trang chủ</a><h1>Góc học tập</h1><p>Flashcard, ghi chú, hẹn giờ và mô phỏng để ôn bài.</p></header>
    <nav class="workspace-tabs" aria-label="Công cụ học tập"><a v-for="tab in tabs" :key="tab.id" :href="`#${tab.id}`" :aria-current="active === tab.id ? 'page' : undefined" @click.prevent="changeTab(tab.id)">{{ tab.name }}</a></nav>
    <p v-if="storageMessage" class="storage-message" role="status">{{ storageMessage }}</p>

    <section v-show="active === 'flashcards'" id="flashcards" class="workspace-section" aria-labelledby="flash-heading">
      <div class="section-heading"><div><h2 id="flash-heading">Nhớ trước khi xem đáp án</h2></div><label class="select-label">Học phần<select v-model="subject"><option value="all">Tất cả học phần</option><option v-for="c in courses" :key="c.id" :value="c.id">{{ c.name }}</option></select></label></div>
      <div class="flashcard-progress"><span>{{ knownCount }} / {{ deck.length }} thẻ đã nhớ</span><progress :value="knownCount" :max="deck.length" :aria-label="`${knownCount} trên ${deck.length} thẻ đã nhớ`"></progress><button class="text-link" @click="resetReview">Ôn lại từ đầu</button></div>
      <article class="flashcard">
        <div class="flashcard-top"><span>{{ courseName(current.course) }}</span><span>{{ index + 1 }} / {{ deck.length }}</span></div>
        <p class="flashcard-question">{{ current.q }}</p>
        <div v-if="revealed" class="flashcard-answer" aria-live="polite"><p>{{ current.a }}</p><a class="text-link" :href="withBase(current.lesson ? `/${current.course}/bai-giang/${current.lesson}#notes` : `/${current.course}/`)">Xem lại {{ current.lesson ? 'bài giảng' : 'lộ trình môn học' }}</a></div>
        <button v-else class="study-button primary" @click="revealed = true">Xem đáp án</button>
      </article>
      <div class="flashcard-actions"><button class="study-button" @click="next(-1)">← Thẻ trước</button><div v-if="revealed" class="button-row"><button class="study-button" @click="review(false)">Chưa nhớ</button><button class="study-button success" @click="review(true)">Đã nhớ</button></div><button class="study-button" @click="next(1)">Thẻ tiếp →</button></div>
      <p class="small tool-explanation">Thử trả lời bằng lời của mình trước khi mở đáp án. Tiến độ được lưu riêng cho từng thẻ trên trình duyệt này.</p>
    </section>

    <section v-show="active === 'notes'" id="notes" class="workspace-section" aria-labelledby="notes-heading">
      <div class="section-heading"><div><h2 id="notes-heading">Ghi lại bằng lời của bạn</h2></div><label class="select-label">Sổ ghi chú<select v-model="noteSubject" @change="loadNote"><option value="general">Ghi chú chung</option><option v-for="c in courses" :key="c.id" :value="c.id">{{ c.name }}</option></select></label></div>
      <div class="notes-toolbar"><div class="button-row"><button class="study-button" :aria-pressed="mode === 'edit'" @click="mode = 'edit'">Soạn thảo</button><button class="study-button" :aria-pressed="mode === 'preview'" @click="mode = 'preview'">Xem trước</button></div><div class="button-row"><button class="study-button" @click="saveNote">Lưu ghi chú</button><button class="study-button primary" @click="downloadNote">Tải .md</button></div></div>
      <label v-show="mode === 'edit'" class="notes-editor"><span class="small">Markdown · # tiêu đề · **in đậm** · - danh sách</span><textarea v-model="note" :disabled="!loaded" spellcheck="false" aria-label="Nội dung ghi chú Markdown"></textarea></label>
      <div v-if="mode === 'preview'" class="note-preview vp-doc" v-html="renderedNote"></div>
      <div class="notes-status"><span role="status">{{ saved || 'Tự lưu khi bạn viết' }}</span><span>{{ note.length.toLocaleString('vi-VN') }} ký tự</span></div>
      <p class="small tool-explanation">Ghi chú nằm trên trình duyệt này. Tải file .md để sao lưu hoặc mở trên thiết bị khác.</p>
    </section>

    <section v-show="active === 'simulation'" id="simulation" class="workspace-section" aria-labelledby="simulation-heading"><h2 id="simulation-heading">Nhìn thấy hướng của điện trường</h2><FieldSimulation /></section>
    <section v-show="active === 'focus'" id="focus" class="workspace-section workspace-focus"><FocusTimer /><div><h2>Hẹn giờ tập trung</h2><ol class="focus-guide"><li>Chọn một bài hoặc một câu hỏi cụ thể.</li><li>Bắt đầu phiên 25 hoặc 50 phút.</li><li>Ghi lại điều chưa hiểu để xử lý sau.</li><li>Dành 5 phút nghỉ trước phiên tiếp theo.</li></ol><a class="text-link" :href="withBase('/guide/')">Đọc thêm về phương pháp học</a></div></section>
  </main>
</template>
