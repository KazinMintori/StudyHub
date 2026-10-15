<script setup>
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
</script>

<template>
  <section class="focus-panel" aria-labelledby="focus-heading">
    <div class="panel-heading"><h2 id="focus-heading">Hẹn giờ tập trung</h2><span>Pomodoro</span></div>
    <p>25 phút học, 5 phút nghỉ.</p>
    <div class="timer-display" role="timer" :aria-label="`Còn ${display}`">{{ display }}</div>
    <div class="timer-modes" aria-label="Thời lượng phiên">
      <button v-for="m in [25, 50, 5]" :key="m" :aria-pressed="minutes === m" @click="selectMinutes(m)">{{ m === 5 ? 'Nghỉ 5 phút' : `${m} phút` }}</button>
    </div>
    <div class="button-row"><button class="study-button primary" @click="toggle">{{ running ? 'Tạm dừng' : remaining === 0 ? 'Phiên mới' : remaining < minutes * 60 ? 'Tiếp tục' : 'Bắt đầu' }}</button><button class="study-button" @click="reset">Đặt lại</button></div>
    <p class="small timer-status" role="status">{{ finished ? 'Đã xong phiên. Dành một chút thời gian nghỉ ngơi.' : `${sessions} phiên đã hoàn thành trên trình duyệt này` }}</p>
  </section>
</template>
