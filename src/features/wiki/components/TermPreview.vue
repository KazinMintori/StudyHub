<script setup>
import MathText from '../../../core/math/components/MathText.vue'
import { useTermPreview } from '../controllers/useTermPreview.js'
const {
  route,
  term,
  wikiHref,
  position,
  popover,
  closeButton,
  pinned,
  field,
  anchor,
  timer,
  suppressFocus,
  clearAnchor,
  close,
  updatePosition,
  show,
  over,
  out,
  focusIn,
  focusOut,
  click,
  key,
  keepOpen,
  leavePopover,
  scroll,
} = useTermPreview()
</script>

<template>
  <Teleport to="body">
    <button v-if="term && pinned" type="button" class="term-preview-scrim" aria-label="Đóng ghi chú nhanh" @click="close({ restoreFocus: true })"></button>
    <aside
      v-if="term"
      id="study-term-preview"
      ref="popover"
      class="term-preview"
      :class="{ 'is-pinned': pinned }"
      :style="position"
      :role="pinned ? 'dialog' : 'tooltip'"
      :aria-labelledby="pinned ? 'study-term-preview-title' : undefined"
      @pointerenter="keepOpen"
      @pointerleave="leavePopover"
    >
      <div class="term-preview-heading">
        <div>
          <span class="term-preview-kicker">Ghi chú nhanh</span>
          <strong id="study-term-preview-title">{{ term.name }}</strong>
          <span v-if="field" class="term-preview-field">Lĩnh vực: {{ field.name }}</span>
        </div>
        <button
          v-if="pinned"
          ref="closeButton"
          type="button"
          class="term-preview-close"
          aria-label="Đóng ghi chú nhanh"
          @click="close({ restoreFocus: true })"
        >Đóng</button>
      </div>
      <MathText as="p" :text="term.definition" />
      <div class="term-preview-example">
        <span>Ví dụ:</span>
        <MathText as="p" :text="term.example" />
        <MathText v-if="term.notation" as="div" class="term-preview-notation" :text="term.notation" />
      </div>
      <a v-if="pinned" class="term-preview-wiki" :href="wikiHref">Đọc bài Wiki đầy đủ <span aria-hidden="true">→</span></a>
      <span v-else class="term-preview-hint">Nhấp để giữ ghi chú và mở đường dẫn tới Wiki.</span>
    </aside>
  </Teleport>
</template>
