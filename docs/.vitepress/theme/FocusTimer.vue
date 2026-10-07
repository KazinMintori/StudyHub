<script setup>
import { computed, ref, onMounted, onUnmounted } from 'vue'
import { readStored, writeStored } from './storage'

const minutes = ref(25), remaining = ref(1500), running = ref(false), sessions = ref(0), finished = ref(false)
let deadline = 0, interval
const display = computed(() => `${String(Math.floor(remaining.value / 60)).padStart(2, '0')}:${String(remaining.value % 60).padStart(2, '0')}`)
function save() { writeStored('studyhub_focus', { minutes: minutes.value, remaining: remaining.value, running: running.value, deadline, sessions: sessions.value }) }
function tick() {
  if (!running.value) return
  remaining.value = Math.max(0, Math.ceil((deadline - Date.now()) / 1000))
  if (!remaining.value) { running.value = false; sessions.value++; finished.value = true; save() }
}
function toggle() {
  if (running.value) { tick(); running.value = false }
  else { if (!remaining.value) remaining.value = minutes.value * 60; finished.value = false; deadline = Date.now() + remaining.value * 1000; running.value = true }
  save()
}
function reset() { running.value = false; remaining.value = minutes.value * 60; finished.value = false; save() }
onMounted(() => {
  const state = readStored('studyhub_focus', null)
  if (state && [5, 25, 50].includes(state.minutes) && Number.isFinite(state.remaining)) {
    minutes.value = state.minutes; remaining.value = Math.max(0, state.remaining); sessions.value = Number(state.sessions) || 0
    deadline = Number(state.deadline) || 0; running.value = !!state.running; tick()
  }
  interval = setInterval(tick, 250)
})
onUnmounted(() => { save(); clearInterval(interval) })
</script>

<template>
  <section class="focus-panel" aria-labelledby="focus-heading">
    <div class="panel-heading"><h2 id="focus-heading">Hẹn giờ tập trung</h2><span>Pomodoro</span></div>
    <p>25 phút học, 5 phút nghỉ.</p>
    <div class="timer-display" role="timer" :aria-label="`Còn ${display}`">{{ display }}</div>
    <div class="timer-modes" aria-label="Thời lượng phiên">
      <button v-for="m in [25, 50, 5]" :key="m" :aria-pressed="minutes === m" @click="minutes = m; reset()">{{ m === 5 ? 'Nghỉ 5 phút' : `${m} phút` }}</button>
    </div>
    <div class="button-row"><button class="study-button primary" @click="toggle">{{ running ? 'Tạm dừng' : remaining === 0 ? 'Phiên mới' : remaining < minutes * 60 ? 'Tiếp tục' : 'Bắt đầu' }}</button><button class="study-button" @click="reset">Đặt lại</button></div>
    <p class="small timer-status" role="status">{{ finished ? 'Đã xong phiên. Dành một chút thời gian nghỉ ngơi.' : `${sessions} phiên đã hoàn thành trên trình duyệt này` }}</p>
  </section>
</template>
