<script setup>
import { feedbackConfig } from '../../../config/feedback.mjs'
import { useFeedback } from '../controllers/useFeedback.js'

const props = defineProps({
  pageTitle: { type: String, default: '' },
  courseName: { type: String, default: '' }
})
const { dialog, trigger, descriptionInput, category, description, context, error, show, close, onClose, submit, onBackdropClick } = useFeedback(() => props)
</script>

<template>
  <button ref="trigger" type="button" class="feedback-trigger" aria-label="Góp ý hoặc báo lỗi bài học" aria-haspopup="dialog" aria-controls="feedback-dialog" title="Góp ý hoặc báo lỗi bài học" @click="show">
    <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 11.5a8.5 8.5 0 0 1-8.5 8.5H4l-2 2V11.5A8.5 8.5 0 0 1 10.5 3h2A8.5 8.5 0 0 1 21 11.5Z" /><path d="M7 9h9M7 13h6" /></svg>
    <span>Góp ý</span>
  </button>
  <Teleport to="body">
    <dialog id="feedback-dialog" ref="dialog" class="feedback-dialog" aria-labelledby="feedback-title" aria-describedby="feedback-help" @cancel.stop.prevent="close" @close="onClose" @click="onBackdropClick">
      <header class="feedback-header">
        <h2 id="feedback-title">Góp ý cho StudyHub</h2>
        <button type="button" class="feedback-close" aria-label="Đóng cửa sổ góp ý" @click="close"><svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><path d="m6 6 12 12M18 6 6 18" /></svg></button>
      </header>
      <p id="feedback-help">Thấy chỗ cần sửa? Gửi vài dòng để bài học tốt hơn.</p>
      <div v-if="context" class="feedback-context">
        <span>Trang được đính kèm tự động</span>
        <strong>{{ context.pageTitle }}</strong>
        <span v-if="context.courseName">{{ context.courseName }}</span>
        <a :href="context.url" target="_blank" rel="noopener noreferrer">{{ context.url }}</a>
      </div>
      <form @submit.prevent="submit">
        <label for="feedback-category">Loại góp ý</label>
        <select id="feedback-category" v-model="category">
          <option v-for="item in feedbackConfig.categories" :key="item.id" :value="item.id">{{ item.label }}</option>
        </select>
        <label for="feedback-description">Mô tả lỗi hoặc góp ý</label>
        <textarea id="feedback-description" ref="descriptionInput" v-model="description" rows="4" :maxlength="feedbackConfig.maxDescriptionLength" required placeholder="Ví dụ: Công thức ở mục 2 thiếu dấu trừ…" :aria-invalid="Boolean(error)" :aria-describedby="error ? 'feedback-error feedback-privacy' : 'feedback-privacy'" />
        <p v-if="error" id="feedback-error" class="feedback-error" role="alert">{{ error }}</p>
        <p id="feedback-privacy" class="feedback-note">Cần đăng nhập GitHub. Góp ý sẽ công khai, bạn đừng ghi thông tin riêng tư. Tên bài và đường dẫn được điền sẵn.</p>
        <button type="submit" class="feedback-submit">Tiếp tục trên GitHub <span aria-hidden="true">↗</span></button>
        <p class="feedback-note feedback-confirmation">Ở tab mới, xác nhận tạo issue để gửi. Bạn có thể đính kèm ảnh tại đó.</p>
      </form>
    </dialog>
  </Teleport>
</template>

<style scoped>
.feedback-trigger { position: fixed; right: max(var(--space-4), env(safe-area-inset-right)); bottom: max(var(--space-4), env(safe-area-inset-bottom)); z-index: 22; display: inline-flex; align-items: center; justify-content: center; gap: var(--space-2); min-width: 44px; min-height: 44px; padding: 0 var(--space-3); border: 1px solid var(--rule); border-radius: var(--radius-lg); background: var(--paper); color: var(--ink-2); box-shadow: var(--shadow-soft); font: 500 var(--fs-meta)/1.4 var(--font-ui); cursor: pointer; transition: color var(--motion-fast), border-color var(--motion-fast); }
.feedback-trigger:hover { color: var(--tim); border-color: var(--tim); }
.feedback-dialog { position: fixed; inset: auto var(--space-4) var(--space-4) auto; box-sizing: border-box; width: min(400px, calc(100vw - 32px)); max-width: none; max-height: calc(100dvh - 32px); overflow-y: auto; margin: 0; padding: var(--space-5); border: 1px solid var(--rule); border-radius: var(--radius-xl); background: var(--paper); color: var(--ink); box-shadow: var(--shadow); font: var(--fs-small)/1.6 var(--font-ui); }
.feedback-dialog::backdrop { background: var(--scrim); opacity: .25; }
.feedback-header { display: flex; align-items: center; justify-content: space-between; gap: var(--space-2); }
.feedback-header h2 { margin: 0; font-size: 18px; font-weight: 700; }
.feedback-close { display: grid; place-items: center; flex-shrink: 0; width: 44px; height: 44px; color: var(--ink-2); border-radius: var(--radius); cursor: pointer; }
.feedback-close:hover { background: var(--sunken); }
.feedback-dialog p { margin: var(--space-2) 0 var(--space-4); color: var(--ink-2); }
.feedback-context { display: grid; gap: var(--space-1); padding: var(--space-3); margin-bottom: var(--space-4); border: 1px solid var(--rule); border-radius: var(--radius); background: var(--canvas); overflow-wrap: anywhere; }
.feedback-context span { font-size: var(--fs-meta); color: var(--ink-2); }
.feedback-context strong { font-weight: 600; }
.feedback-context a { color: var(--tim); text-decoration: underline; text-underline-offset: 3px; font-size: 12px; }
.feedback-dialog label { display: block; margin: var(--space-3) 0 var(--space-2); font-weight: 600; }
.feedback-dialog :is(select, textarea) { display: block; box-sizing: border-box; width: 100%; min-height: 44px; padding: var(--space-2) var(--space-3); border: 1px solid var(--control); border-radius: var(--radius); background: var(--paper); color: var(--ink); font: 16px/1.6 var(--font-ui); }
.feedback-dialog select { appearance: auto; }
.feedback-dialog textarea { resize: vertical; min-height: 112px; max-height: 35dvh; }
.feedback-dialog textarea::placeholder { color: var(--ink-3); }
.feedback-dialog .feedback-note { font-size: 12px; line-height: 1.7; }
.feedback-submit { display: flex; align-items: center; justify-content: center; gap: var(--space-2); width: 100%; min-height: 44px; padding: var(--space-2) var(--space-3); border: 1px solid var(--tim); border-radius: var(--radius); color: var(--paper); background: var(--tim); font-weight: 600; cursor: pointer; }
.feedback-submit:hover { background: var(--tim-hover); }
.feedback-dialog .feedback-confirmation { text-align: center; margin-bottom: 0; }
.feedback-dialog .feedback-error { color: var(--do); }
.feedback-trigger:focus-visible, .feedback-dialog :is(button, a, select, textarea):focus-visible { outline: 2px solid var(--tim); outline-offset: 3px; }
:global(html.study-zen-mode .feedback-trigger) { display: none; }
@media (max-width: 599px) {
  .feedback-trigger { right: max(var(--space-3), env(safe-area-inset-right)); bottom: max(var(--space-3), env(safe-area-inset-bottom)); padding: 0; }
  .feedback-trigger span { display: none; }
  .feedback-dialog { inset: auto 0 0; width: 100%; max-height: calc(100dvh - 16px); border-radius: var(--radius-xl) var(--radius-xl) 0 0; padding: var(--space-4) max(var(--space-4), env(safe-area-inset-right)) max(var(--space-4), env(safe-area-inset-bottom)) max(var(--space-4), env(safe-area-inset-left)); }
}
@media (prefers-reduced-motion: reduce) { .feedback-trigger { transition: none; } }
@media print { .feedback-trigger, .feedback-dialog { display: none !important; } }
</style>
