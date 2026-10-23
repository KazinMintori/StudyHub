import { ref, computed, onMounted, onUnmounted } from 'vue'
import { getStorage, readStored, writeStored } from '../../../core/storage/index.js'
import {
  formatTimerDisplay,
  restoreTimerState,
  startTimer,
  resetTimer,
  tickTimer,
  isValidMinutes
} from '../services/focusTimerService.mjs'

export function useFocusTimer() {
  const minutes = ref(25)
  const remaining = ref(1500)
  const running = ref(false)
  const sessions = ref(0)
  const finished = ref(false)

  let deadline = 0
  let interval = null

  const display = computed(() => formatTimerDisplay(remaining.value))

  function save() {
    writeStored('studyhub_focus', {
      minutes: minutes.value,
      remaining: remaining.value,
      running: running.value,
      deadline,
      sessions: sessions.value
    })
  }

  function tick() {
    if (!running.value) return
    const result = tickTimer(deadline, sessions.value)
    remaining.value = result.remaining
    if (!result.running) {
      running.value = false
      sessions.value = result.sessions
      finished.value = true
      save()
    }
  }

  function toggle() {
    if (running.value) {
      // The deadline may have elapsed before the scheduled interval runs.
      tick()
      running.value = false
    } else {
      const started = startTimer(minutes.value, remaining.value)
      remaining.value = started.remaining
      deadline = started.deadline
      finished.value = started.finished
      running.value = true
    }
    save()
  }

  function reset() {
    const resetState = resetTimer(minutes.value)
    running.value = resetState.running
    remaining.value = resetState.remaining
    finished.value = resetState.finished
    deadline = resetState.deadline
    save()
  }

  function selectMinutes(m) {
    if (!isValidMinutes(m)) return false
    minutes.value = Number(m)
    reset()
    return true
  }

  function load() {
    const restored = restoreTimerState(readStored('studyhub_focus', null))
    minutes.value = restored.minutes
    remaining.value = restored.remaining
    sessions.value = restored.sessions
    deadline = restored.deadline
    running.value = restored.running
    finished.value = restored.finished
    if (restored.finished) {
      save()
    }
  }

  function handleStorage(event) {
    if (event.storageArea && event.storageArea !== getStorage()) return
    if (event.key === 'studyhub_focus' || event.key === null) load()
  }

  onMounted(() => {
    load()
    window.addEventListener('storage', handleStorage)
    interval = setInterval(tick, 250)
  })

  onUnmounted(() => {
    // Every state transition is already saved. Saving here could overwrite a
    // newer session from another tab before its storage event is delivered.
    window.removeEventListener('storage', handleStorage)
    if (interval) {
      clearInterval(interval)
    }
  })

  return {
    minutes,
    remaining,
    running,
    sessions,
    finished,
    display,
    toggle,
    reset,
    selectMinutes,
    save
  }
}
