import { ref, computed, watch, nextTick, onMounted } from 'vue'
import MarkdownIt from 'markdown-it'
import { readStored, writeStored } from '../../../core/storage/index.js'
import {
  getNoteStorageKey,
  resolveInitialNote,
  getNoteDownloadFilename,
  createMarkdownOptions
} from '../services/notebookService.mjs'

export function useNotebook(options = {}) {
  const getCourses = () => options.courses || []

  const noteSubject = ref('general')
  const note = ref('')
  const loaded = ref(false)
  const saved = ref('')
  const mode = ref('edit')

  const markdown = new MarkdownIt(createMarkdownOptions())
  const renderedNote = computed(() => markdown.render(note.value))

  const currentKey = computed(() => getNoteStorageKey(noteSubject.value))

  async function loadNote() {
    loaded.value = false
    let text = readStored(currentKey.value, null)

    let legacyRawNotes = null
    if (text === null && noteSubject.value === 'general') {
      try {
        legacyRawNotes = localStorage.getItem('studyhub_notes')
      } catch {
        /* The download button remains available. */
      }
    }

    note.value = resolveInitialNote(text, legacyRawNotes, noteSubject.value)
    await nextTick()
    loaded.value = true
    saved.value = ''
  }

  function saveNote() {
    if (writeStored(currentKey.value, note.value)) {
      saved.value = 'Đã lưu trên trình duyệt'
    }
  }

  watch(note, () => {
    if (loaded.value) {
      saveNote()
    }
  })

  function downloadNote() {
    const filename = getNoteDownloadFilename(noteSubject.value)
    const url = URL.createObjectURL(new Blob([note.value], { type: 'text/markdown;charset=utf-8' }))
    const link = document.createElement('a')
    link.href = url
    link.download = filename
    link.click()
    setTimeout(() => URL.revokeObjectURL(url), 1000)
  }

  onMounted(() => {
    loadNote()
  })

  return {
    noteSubject,
    note,
    loaded,
    saved,
    mode,
    renderedNote,
    courses: getCourses,
    loadNote,
    saveNote,
    downloadNote
  }
}
