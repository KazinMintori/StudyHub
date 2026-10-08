<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { withBase } from 'vitepress'

const dialog = ref(null)
const startButton = ref(null)
const storageKey = 'studyhub_welcome_seen'
let previousFocus
let previousOverflow

function show() {
  if (!dialog.value || dialog.value.open) return
  previousFocus = document.activeElement
  previousOverflow = document.documentElement.style.overflow
  dialog.value.showModal()
  document.documentElement.style.overflow = 'hidden'
}

function dismiss() {
  dialog.value?.close()
}

function restoreScroll() {
  if (previousOverflow === undefined) return
  document.documentElement.style.overflow = previousOverflow
  previousOverflow = undefined
}

function onClose() {
  restoreScroll()
  // Storage may be unavailable in private browsing; the screen still closes.
  try { sessionStorage.setItem(storageKey, '1') } catch {}
  if (previousFocus?.isConnected && previousFocus !== document.body) {
    previousFocus.focus({ preventScroll: true })
  } else {
    const heading = document.querySelector('main h1, .VPContent h1')
    if (heading) {
      heading.setAttribute('tabindex', '-1')
      heading.focus({ preventScroll: true })
    }
  }
}

onMounted(() => {
  let seen = false
  try { seen = sessionStorage.getItem(storageKey) === '1' } catch {}
  if (!seen) show()
})

onUnmounted(() => {
  dialog.value?.close()
  restoreScroll()
})

defineExpose({ show })
</script>

<template>
  <Teleport to="body">
    <dialog ref="dialog" class="welcome-screen" aria-labelledby="welcome-title" aria-describedby="welcome-description" @cancel.prevent="dismiss" @close="onClose" @keydown.tab.prevent="startButton?.focus()">
      <div class="welcome-content">
        <img :src="withBase('/uet-polytechnic.png')" alt="UET Education — UET Polytechnic" class="welcome-logo" width="2109" height="746" fetchpriority="high" />
        <p class="welcome-eyebrow">Không gian tự học dành cho sinh viên UET</p>
        <h2 id="welcome-title">Chào mừng đến với UETệ</h2>
        <p id="welcome-description" class="welcome-description">Tìm bài giảng theo học phần, hiểu lại những kiến thức nền và ôn tập theo nhịp học của bạn.</p>
        <dl class="welcome-features">
          <div><dt>Bài giảng</dt><dd>Đọc Notes, ôn nhanh với Slides và luyện tập qua các bài có lời giải.</dd></div>
          <div><dt>Wiki kiến thức</dt><dd>Tra cứu thuật ngữ và bổ sung kiến thức nền ngay khi cần.</dd></div>
          <div><dt>Góc học tập</dt><dd>Ôn bằng flashcard, lưu ghi chú và hẹn giờ tập trung.</dd></div>
        </dl>
        <button ref="startButton" class="study-button primary welcome-start" autofocus @click="dismiss">Bắt đầu học <span aria-hidden="true">→</span></button>
        <p class="welcome-hint">Bạn có thể xem lại phần giới thiệu ở cuối trang.</p>
      </div>
    </dialog>
  </Teleport>
</template>

<style scoped>
.welcome-screen {
  position: fixed;
  inset: 0;
  width: 100%;
  max-width: none;
  height: 100%;
  height: 100dvh;
  max-height: none;
  margin: 0;
  padding: var(--space-6);
  border: 0;
  background: var(--paper);
  color: var(--ink);
  overflow-y: auto;
  overscroll-behavior: contain;
}
.welcome-screen[open] { display: flex; }
.welcome-screen::backdrop { background: var(--paper); }
.welcome-content { width: min(880px, 100%); margin: auto; padding: var(--space-5) 0; text-align: center; }
.welcome-logo { display: block; width: min(440px, 100%); height: auto; margin: 0 auto var(--space-6); }
.welcome-eyebrow { font-size: var(--fs-small); color: var(--tim); margin-bottom: var(--space-3); }
.welcome-content h2 { font-size: var(--fs-display); font-weight: 700; line-height: 1.2; margin: 0; }
.welcome-description { max-width: 580px; margin: var(--space-4) auto 0; font-size: var(--fs-lead); color: var(--ink-2); }
.welcome-features { display: grid; grid-template-columns: repeat(3, 1fr); gap: var(--space-6); margin: var(--space-6) 0; padding: var(--space-5) 0; border-top: 1px solid var(--rule); border-bottom: 1px solid var(--rule); text-align: left; }
.welcome-features dt { font-weight: 600; font-size: var(--fs-lead); margin-bottom: var(--space-2); }
.welcome-features dd { margin: 0; color: var(--ink-2); font-size: var(--fs-ui); }
.welcome-start { min-width: 180px; gap: var(--space-4); }
.welcome-hint { font-size: var(--fs-small); color: var(--ink-3); margin-top: var(--space-4); }
@media (max-width: 767px) {
  .welcome-screen { padding: var(--space-5) 20px; }
  .welcome-content { padding: var(--space-3) 0; }
  .welcome-logo { width: min(340px, 100%); margin-bottom: var(--space-5); }
  .welcome-features { grid-template-columns: 1fr; gap: var(--space-4); padding: var(--space-4) 0; margin: var(--space-5) 0; }
  .welcome-start { width: 100%; }
}
@media print { .welcome-screen[open] { display: none; } }
</style>
