<script setup>
import { computed } from 'vue'
import { feedbackConfig } from '../../../config/feedback.mjs'
import { useFeedback } from '../controllers/useFeedback.js'

const props = defineProps({
  pageTitle: { type: String, default: '' },
  courseName: { type: String, default: '' }
})
const { dialog, trigger, descriptionInput, category, description, contact, includePage, honeypot, context, error, status, copied, fallbackReason, issueUrl, show, close, onClose, submit, copyMessage, backToForm, writeAnother, onBackdropClick } = useFeedback(() => props)
const remaining = computed(() => feedbackConfig.maxDescriptionLength - description.value.length)
const placeholders = {
  content: 'Ví dụ: Ở mục 2, công thức thứ ba thiếu dấu trừ trước tích phân.',
  display: 'Ví dụ: Trên điện thoại, hình ở cuối bài bị tràn ra ngoài màn hình.',
  suggestion: 'Ví dụ: Mình muốn có thêm bài tập có lời giải cho phần này.'
}
</script>

<template>
  <button ref="trigger" type="button" class="feedback-trigger" aria-label="Góp ý hoặc báo lỗi" aria-haspopup="dialog" aria-controls="feedback-dialog" title="Góp ý hoặc báo lỗi" @click="show">
    <svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5H4l-2 2V11.5A8.5 8.5 0 0 1 10.5 3h2A8.5 8.5 0 0 1 21 11.5Z" /><path d="M7 9h9M7 13h6" /></svg>
  </button>
  <Teleport to="body">
    <dialog id="feedback-dialog" ref="dialog" class="feedback-dialog" aria-labelledby="feedback-title" @cancel.stop.prevent="close" @close="onClose" @click="onBackdropClick">
      <header class="feedback-header">
        <h2 id="feedback-title">{{ status === 'sent' ? 'Đã nhận góp ý' : 'Góp ý cho StudyHub' }}</h2>
        <button type="button" class="feedback-close" aria-label="Đóng cửa sổ góp ý" @click="close"><svg viewBox="0 0 24 24" width="20" height="20" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18" /></svg></button>
      </header>

      <section v-if="status === 'sent'" class="feedback-done" role="status">
        <svg class="feedback-done-icon" viewBox="0 0 48 48" width="48" height="48" aria-hidden="true"><circle cx="24" cy="24" r="20" /><path d="m15 24.5 6 6 12-13" /></svg>
        <p>Cảm ơn bạn. Góp ý đã được gửi tới nhóm biên soạn{{ contact ? ', và chúng mình sẽ liên hệ lại nếu cần thêm thông tin' : '' }}.</p>
        <div class="feedback-actions">
          <button type="button" class="feedback-secondary" @click="writeAnother">Gửi góp ý khác</button>
          <button type="button" class="feedback-submit" @click="close">Quay lại bài học</button>
        </div>
      </section>

      <section v-else-if="status === 'fallback'" class="feedback-fallback">
        <p class="feedback-warning" role="alert">{{ fallbackReason }} Nội dung bạn viết vẫn được giữ nguyên.</p>
        <p>Bạn có thể sao chép góp ý để gửi qua kênh liên lạc của lớp, hoặc thử gửi lại sau ít phút.</p>
        <div class="feedback-actions feedback-actions-stack">
          <button type="button" class="feedback-submit" @click="copyMessage">{{ copied ? 'Đã sao chép ✓' : 'Sao chép nội dung góp ý' }}</button>
          <button type="button" class="feedback-secondary" @click="backToForm">Sửa lại hoặc thử gửi lại</button>
        </div>
        <p v-if="issueUrl" class="feedback-note">Nếu có tài khoản GitHub, bạn cũng có thể <a :href="issueUrl" target="_blank" rel="noopener noreferrer">mở góp ý dưới dạng issue công khai</a>.</p>
      </section>

      <form v-else novalidate @submit.prevent="submit">
        <p class="feedback-intro">Thấy chỗ sai, chỗ khó hiểu hay có ý tưởng? Viết vài dòng, không cần đăng nhập.</p>
        <fieldset class="feedback-categories">
          <legend>Bạn muốn góp ý về</legend>
          <label v-for="item in feedbackConfig.categories" :key="item.id" class="feedback-chip" :title="item.label">
            <input v-model="category" type="radio" name="feedback-category" :value="item.id" :disabled="status === 'sending'" />
            <span>{{ item.short }}</span>
          </label>
        </fieldset>

        <label for="feedback-description" class="feedback-label">Nội dung</label>
        <textarea id="feedback-description" ref="descriptionInput" v-model="description" rows="4" :maxlength="feedbackConfig.maxDescriptionLength" :placeholder="placeholders[category]" :disabled="status === 'sending'" :aria-invalid="Boolean(error)" :aria-describedby="error ? 'feedback-error feedback-count' : 'feedback-count'" />
        <div class="feedback-meta">
          <p v-if="error" id="feedback-error" class="feedback-error" role="alert">{{ error }}</p>
          <span id="feedback-count" class="feedback-count" :class="{ low: remaining < 100 }">Còn {{ remaining }} ký tự</span>
        </div>

        <label for="feedback-contact" class="feedback-label">Email hoặc cách liên hệ <span class="feedback-optional">(không bắt buộc)</span></label>
        <input id="feedback-contact" v-model="contact" type="text" autocomplete="email" :maxlength="feedbackConfig.maxContactLength" placeholder="Để trống nếu bạn muốn ẩn danh" :disabled="status === 'sending'" />

        <label v-if="context" class="feedback-page">
          <input v-model="includePage" type="checkbox" :disabled="status === 'sending'" />
          <span>Đính kèm trang đang đọc<strong>{{ context.pageTitle }}</strong><small v-if="context.courseName">{{ context.courseName }}</small></span>
        </label>

        <!-- Hidden from people and assistive technology; filled only by spam bots. -->
        <input v-model="honeypot" class="feedback-trap" type="text" name="website" tabindex="-1" autocomplete="off" aria-hidden="true" />

        <button type="submit" class="feedback-submit" :disabled="status === 'sending'">
          <span v-if="status === 'sending'" class="feedback-spinner" aria-hidden="true" />
          {{ status === 'sending' ? 'Đang gửi…' : 'Gửi góp ý' }}
        </button>
        <p class="feedback-note">Góp ý chỉ được nhóm biên soạn đọc. Bạn đừng ghi mật khẩu hay thông tin riêng tư.</p>
      </form>
    </dialog>
  </Teleport>
</template>

<style scoped>
.feedback-trigger { position: fixed; right: max(var(--space-4), env(safe-area-inset-right)); bottom: max(var(--space-4), env(safe-area-inset-bottom)); z-index: 22; display: inline-flex; align-items: center; justify-content: center; box-sizing: border-box; width: 46px; height: 46px; padding: 0; border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper); color: var(--ink-2); cursor: pointer; transition: color var(--motion-fast), border-color var(--motion-fast); }
.feedback-trigger:hover { color: var(--tim); border-color: var(--tim); }
svg { fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
.feedback-dialog { position: fixed; inset: auto var(--space-4) var(--space-4) auto; box-sizing: border-box; width: min(420px, calc(100vw - 32px)); max-width: none; max-height: calc(100dvh - 32px); overflow-y: auto; margin: 0; padding: var(--space-5); border: 1px solid var(--rule); border-radius: var(--radius-xl); background: var(--paper); color: var(--ink); box-shadow: var(--shadow); font: var(--fs-small)/1.6 var(--font-ui); }
.feedback-dialog::backdrop { background: var(--scrim); opacity: .25; }
.feedback-header { display: flex; align-items: center; justify-content: space-between; gap: var(--space-2); margin-bottom: var(--space-2); }
.feedback-header h2 { margin: 0; font-size: 18px; font-weight: 700; }
.feedback-close { display: grid; place-items: center; flex-shrink: 0; width: 40px; height: 40px; margin-right: calc(var(--space-2) * -1); color: var(--ink-2); border-radius: var(--radius); cursor: pointer; }
.feedback-close:hover { background: var(--sunken); }
.feedback-dialog p { margin: 0 0 var(--space-3); color: var(--ink-2); }
.feedback-intro { margin-bottom: var(--space-3) !important; }
.feedback-categories { display: flex; flex-wrap: wrap; gap: var(--space-2); margin: 0 0 var(--space-3); padding: 0; border: 0; }
.feedback-categories legend { width: 100%; margin-bottom: var(--space-2); padding: 0; font-weight: 600; }
.feedback-chip { position: relative; display: inline-flex; cursor: pointer; }
.feedback-chip input { position: absolute; inset: 0; opacity: 0; margin: 0; cursor: pointer; }
.feedback-chip span { display: inline-flex; align-items: center; min-height: 36px; padding: 0 var(--space-3); border: 1px solid var(--control); border-radius: 999px; color: var(--ink-2); transition: all var(--motion-fast); }
.feedback-chip:hover span { border-color: var(--tim); color: var(--tim); }
.feedback-chip input:checked + span { border-color: var(--tim); background: var(--tim-soft); color: var(--tim); font-weight: 600; }
.feedback-chip input:focus-visible + span { outline: 2px solid var(--tim); outline-offset: 2px; }
.feedback-label { display: block; margin: 0 0 var(--space-2); font-weight: 600; }
.feedback-optional { font-weight: 400; color: var(--ink-3); }
.feedback-dialog :is(textarea, input[type="text"]) { display: block; box-sizing: border-box; width: 100%; min-height: 44px; padding: var(--space-2) var(--space-3); border: 1px solid var(--control); border-radius: var(--radius); background: var(--paper); color: var(--ink); font: 16px/1.6 var(--font-ui); }
.feedback-dialog :is(textarea, input[type="text"]):focus { border-color: var(--tim); outline: none; box-shadow: 0 0 0 3px var(--tim-soft); }
.feedback-dialog textarea { resize: vertical; min-height: 104px; max-height: 35dvh; }
.feedback-dialog :is(textarea, input)::placeholder { color: var(--ink-3); }
.feedback-meta { display: flex; justify-content: space-between; align-items: flex-start; gap: var(--space-3); min-height: 24px; margin: var(--space-1) 0 var(--space-3); }
.feedback-meta .feedback-error { margin: 0; color: var(--do); }
.feedback-count { margin-left: auto; font-size: 12px; color: var(--ink-3); white-space: nowrap; }
.feedback-count.low { color: var(--do); }
.feedback-page { display: flex; align-items: flex-start; gap: var(--space-2); margin: var(--space-3) 0; padding: var(--space-2) var(--space-3); border: 1px solid var(--rule); border-radius: var(--radius); background: var(--canvas); cursor: pointer; overflow-wrap: anywhere; }
.feedback-page input { width: 18px; height: 18px; margin: 2px 0 0; flex-shrink: 0; accent-color: var(--tim); }
.feedback-page span { display: grid; gap: 0; color: var(--ink-2); line-height: 1.5; }
.feedback-page strong { font-weight: 600; color: var(--ink); }
.feedback-page small { font-size: 12px; color: var(--ink-3); }
.feedback-trap { position: absolute !important; left: -9999px; width: 1px; height: 1px; opacity: 0; }
.feedback-submit, .feedback-secondary { display: flex; align-items: center; justify-content: center; gap: var(--space-2); width: 100%; min-height: 44px; padding: var(--space-2) var(--space-3); border-radius: var(--radius); font-weight: 600; cursor: pointer; }
.feedback-submit { border: 1px solid var(--tim); color: var(--paper); background: var(--tim); }
.feedback-submit:hover:not(:disabled) { background: var(--tim-hover); }
.feedback-submit:disabled { opacity: .7; cursor: progress; }
.feedback-secondary { border: 1px solid var(--control); color: var(--ink); background: var(--paper); }
.feedback-secondary:hover { border-color: var(--tim); color: var(--tim); }
.feedback-spinner { width: 14px; height: 14px; border: 2px solid currentColor; border-right-color: transparent; border-radius: 50%; animation: feedback-spin .8s linear infinite; }
@keyframes feedback-spin { to { transform: rotate(360deg); } }
.feedback-dialog .feedback-note { margin: var(--space-3) 0 0; font-size: 12px; line-height: 1.7; color: var(--ink-3); }
.feedback-note a { color: var(--tim); text-decoration: underline; text-underline-offset: 3px; }
.feedback-done { display: grid; justify-items: center; text-align: center; padding-top: var(--space-2); }
.feedback-done-icon { color: var(--tim); margin-bottom: var(--space-3); stroke-width: 2.4; }
.feedback-actions { display: grid; grid-template-columns: 1fr 1fr; gap: var(--space-2); width: 100%; }
.feedback-actions-stack { grid-template-columns: 1fr; }
.feedback-warning { padding: var(--space-3); border-left: 3px solid var(--do); border-radius: var(--radius-sm); background: var(--canvas); color: var(--ink) !important; }
.feedback-trigger:focus-visible, .feedback-dialog :is(button, a):focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
:global(html.study-zen-mode .feedback-trigger) { display: none; }
@media (max-width: 599px) {
  .feedback-trigger { right: max(var(--space-3), env(safe-area-inset-right)); bottom: max(var(--space-3), env(safe-area-inset-bottom)); }
  .feedback-dialog { inset: auto 0 0; width: 100%; max-height: calc(100dvh - 16px); border-radius: var(--radius-xl) var(--radius-xl) 0 0; padding: var(--space-4) max(var(--space-4), env(safe-area-inset-right)) max(var(--space-4), env(safe-area-inset-bottom)) max(var(--space-4), env(safe-area-inset-left)); }
  .feedback-actions { grid-template-columns: 1fr; }
}
@media (prefers-reduced-motion: reduce) { .feedback-trigger, .feedback-chip span { transition: none; } .feedback-spinner { animation-duration: 2.4s; } }
@media print { .feedback-trigger, .feedback-dialog { display: none !important; } }
</style>
