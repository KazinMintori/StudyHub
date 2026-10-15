<script setup>
import { useNotebook } from '../controllers/useNotebook.js'

const props = defineProps({
  courses: {
    type: Array,
    default: () => []
  }
})

const {
  noteSubject,
  note,
  loaded,
  saved,
  mode,
  renderedNote,
  loadNote,
  saveNote,
  downloadNote
} = useNotebook({ courses: props.courses })
</script>

<template>
  <section id="notes" class="workspace-section" aria-labelledby="notes-heading">
    <div class="section-heading">
      <div>
        <h2 id="notes-heading">Ghi lại bằng lời của bạn</h2>
      </div>
      <label class="select-label">
        Sổ ghi chú
        <select v-model="noteSubject" @change="loadNote">
          <option value="general">Ghi chú chung</option>
          <option v-for="c in courses" :key="c.id" :value="c.id">{{ c.name }}</option>
        </select>
      </label>
    </div>
    <div class="notes-toolbar">
      <div class="button-row">
        <button class="study-button" :aria-pressed="mode === 'edit'" @click="mode = 'edit'">Soạn thảo</button>
        <button class="study-button" :aria-pressed="mode === 'preview'" @click="mode = 'preview'">Xem trước</button>
      </div>
      <div class="button-row">
        <button class="study-button" @click="saveNote">Lưu ghi chú</button>
        <button class="study-button primary" @click="downloadNote">Tải .md</button>
      </div>
    </div>
    <label v-show="mode === 'edit'" class="notes-editor">
      <span class="small">Markdown · # tiêu đề · **in đậm** · - danh sách</span>
      <textarea v-model="note" :disabled="!loaded" spellcheck="false" aria-label="Nội dung ghi chú Markdown"></textarea>
    </label>
    <div v-if="mode === 'preview'" class="note-preview vp-doc" v-html="renderedNote"></div>
    <div class="notes-status">
      <span role="status">{{ saved || 'Tự lưu khi bạn viết' }}</span>
      <span>{{ note.length.toLocaleString('vi-VN') }} ký tự</span>
    </div>
    <p class="small tool-explanation">Ghi chú nằm trên trình duyệt này. Tải file .md để sao lưu hoặc mở trên thiết bị khác.</p>
  </section>
</template>
