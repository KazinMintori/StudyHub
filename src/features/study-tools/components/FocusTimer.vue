<script setup>
import { ref, watch } from 'vue'
import { useFocusTimer } from '../controllers/useFocusTimer.js'

const {
  minutes,
  remaining,
  running,
  sessions,
  finished,
  display,
  toggle,
  reset,
  selectMinutes
} = useFocusTimer()
const customMinutes = ref('25'), durationError = ref('')
watch(minutes, value => { customMinutes.value = String(value); durationError.value = '' }, { immediate: true })
function chooseDuration(value) {
  if (!selectMinutes(value)) { durationError.value = 'Nhập số phút nguyên từ 1 đến 240.'; return }
  customMinutes.value = String(minutes.value); durationError.value = ''
}
</script>

<template>
  <section class="focus-panel" aria-labelledby="focus-heading">
    <div class="panel-heading"><h2 id="focus-heading">Hẹn giờ tập trung</h2><span>Pomodoro</span></div>
    <p>25 phút học, 5 phút nghỉ.</p>
    <div class="timer-display" role="timer" :aria-label="`Còn ${display}`">{{ display }}</div>
    <div class="timer-modes" aria-label="Thời lượng phiên">
      <button v-for="m in [25, 50, 5]" :key="m" :aria-pressed="minutes === m" :disabled="running" @click="chooseDuration(m)">{{ m === 5 ? 'Nghỉ 5 phút' : `${m} phút` }}</button>
    </div>
    <form class="workspace-duration-form" novalidate @submit.prevent="chooseDuration(customMinutes)"><label for="workspace-focus-minutes">Thời lượng tùy chọn (phút)</label><div><input id="workspace-focus-minutes" v-model="customMinutes" type="text" inputmode="numeric" maxlength="3" :disabled="running" :aria-invalid="Boolean(durationError)" aria-describedby="workspace-duration-help"><button type="submit" class="study-button" :disabled="running">Áp dụng</button></div><p id="workspace-duration-help" :class="{ 'study-plan-error': durationError }" :role="durationError ? 'alert' : undefined">{{ durationError || (running ? 'Tạm dừng để đổi thời lượng.' : 'Chọn từ 1 đến 240 phút cho phiên học.') }}</p></form>
    <div class="button-row"><button class="study-button primary" @click="toggle">{{ running ? 'Tạm dừng' : remaining === 0 ? 'Phiên mới' : remaining < minutes * 60 ? 'Tiếp tục' : 'Bắt đầu' }}</button><button class="study-button" @click="reset">Đặt lại</button></div>
    <p class="small timer-status" role="status">{{ finished ? 'Đã xong phiên. Dành một chút thời gian nghỉ ngơi.' : `${sessions} phiên đã hoàn thành trên trình duyệt này` }}</p>
  </section>
</template>
