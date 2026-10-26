import { computed, onMounted, onUnmounted, ref, watch } from 'vue'
import { getStorage, writeStored } from '../../../core/storage/index.js'
import { studyPlanKey, normalizeStudyTasks } from '../services/courseWorkspaceService.mjs'

export function useStudyPlan(courseId) {
  const tasks = ref([]), draft = ref(''), error = ref('')
  const key = computed(() => studyPlanKey(courseId.value))
  const completed = computed(() => tasks.value.filter(task => task.done).length)
  const pending = new Map()
  const snapshots = new Map()
  let loaded = false
  function load() {
    tasks.value = latest()
    draft.value = ''; error.value = ''; loaded = true
  }
  function latest() {
    let saved = snapshots.get(key.value) || []
    const store = getStorage()
    if (store) {
      try {
        const raw = store.getItem(key.value)
        try { saved = normalizeStudyTasks(raw === null ? [] : JSON.parse(raw)) } catch { saved = [] }
        snapshots.set(key.value, saved)
      } catch {
        // A blocked read must not erase tasks already loaded in this session.
      }
    }
    const current = new Map(saved.map(task => [task.id, task]))
    for (const [id, task] of pending.get(key.value) || []) {
      if (task === null) current.delete(id)
      else current.set(id, task)
    }
    return [...current.values()]
  }
  function save(id, task) {
    if (!pending.has(key.value)) pending.set(key.value, new Map())
    pending.get(key.value).set(id, task)
    tasks.value = normalizeStudyTasks(latest())
    if (writeStored(key.value, tasks.value)) {
      pending.delete(key.value)
      snapshots.set(key.value, tasks.value)
    }
  }
  function add() {
    const text = draft.value.trim()
    if (!text) { error.value = 'Nhập một việc cụ thể bạn muốn hoàn thành.'; return }
    const current = latest()
    if (current.length >= 100) { error.value = 'Danh sách đã có 100 việc. Xóa bớt việc đã xong để thêm việc mới.'; return }
    const id = globalThis.crypto?.randomUUID?.() || `${Date.now()}-${Math.random().toString(36).slice(2)}`
    save(id, { id, text: text.slice(0, 300), done: false })
    draft.value = ''; error.value = ''
  }
  function toggle(id) { const task = latest().find(task => task.id === id); if (task) save(id, { ...task, done: !task.done }) }
  function remove(id) { save(id, null) }
  function storage(event) {
    if (event.storageArea && event.storageArea !== getStorage()) return
    if (event.key === null) {
      pending.clear(); snapshots.clear(); tasks.value = []
      return
    }
    if (typeof event.key !== 'string' || !event.key.startsWith('studyhub_plan_')) return
    if (event.newValue === null) {
      // A deletion also applies to an unsaved overlay in an inactive course.
      pending.delete(event.key); snapshots.delete(event.key)
      if (event.key === key.value) tasks.value = []
      return
    }
    if (event.key === key.value) tasks.value = latest()
  }
  watch(key, () => { if (loaded) load() }, { flush: 'sync' })
  onMounted(() => { load(); window.addEventListener('storage', storage) })
  onUnmounted(() => window.removeEventListener('storage', storage))
  return { tasks, draft, error, completed, add, toggle, remove }
}
