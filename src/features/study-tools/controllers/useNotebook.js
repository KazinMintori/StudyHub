import { ref, computed, watch, nextTick, onMounted, toValue } from 'vue'
import MarkdownIt from 'markdown-it'
import { readStored, writeStored } from '../../../core/storage/index.js'
import {
  getNoteStorageKey,
  resolveInitialNote,
  getNoteDownloadFilename,
  createMarkdownOptions
} from '../services/notebookService.mjs'
import { normalizeWorkspaceCourse } from '../services/courseWorkspaceService.mjs'

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
  let loadVersion = 0
  const snapshots = new Map(), unsaved = new Map()

  async function loadNote() {
    const version = ++loadVersion
    loaded.value = false
    const key = currentKey.value
    let text = unsaved.has(key) ? unsaved.get(key) : readStored(key, snapshots.get(key) ?? null)

    let legacyRawNotes = null
    if (text === null && noteSubject.value === 'general') {
      try {
        legacyRawNotes = localStorage.getItem('studyhub_notes')
      } catch {
        /* The download button remains available. */
      }
    }

    note.value = resolveInitialNote(text, legacyRawNotes, noteSubject.value)
    snapshots.set(key, note.value)
    await nextTick()
    if (version !== loadVersion) return
    loaded.value = true
    saved.value = unsaved.has(key) ? 'Chưa lưu được. Bản nháp vẫn được giữ trong phiên này.' : ''
  }

  function saveNote() {
    if (!loaded.value) return
    const key = currentKey.value
    snapshots.set(key, note.value)
    if (writeStored(key, note.value)) {
      unsaved.delete(key)
      saved.value = 'Đã lưu trên trình duyệt'
    } else {
      unsaved.set(key, note.value)
      saved.value = 'Chưa lưu được. Bản nháp vẫn được giữ trong phiên này.'
    }
  }

  watch(note, () => {
    if (loaded.value) {
      saveNote()
    }
  }, { flush: 'sync' })

  watch(noteSubject, loadNote, { flush: 'sync' })
  watch(() => toValue(options.courseId), id => {
    if (!id) return
    const course = normalizeWorkspaceCourse(id, getCourses())
    noteSubject.value = course === 'all' ? 'general' : course
  }, { immediate: true, flush: 'sync' })

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
