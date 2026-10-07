<script setup>
import { ref, onMounted, onUnmounted, nextTick } from 'vue'
const dialog = ref(null), svg = ref(''), image = ref(''), scale = ref(1)
let observer, previousFocus
async function open(node) {
  previousFocus = document.activeElement
  svg.value = node.tagName.toLowerCase() === 'svg' ? node.outerHTML : ''
  image.value = svg.value ? '' : node.src
  scale.value = 1
  await nextTick(); dialog.value.showModal(); document.body.style.overflow = 'hidden'
}
function close() { dialog.value.close(); document.body.style.overflow = ''; previousFocus?.focus?.() }
function attach() {
  for (const container of document.querySelectorAll('.mermaid')) {
    if (container.querySelector('svg') && !container.querySelector('.mermaid-zoom-btn')) {
      const button = document.createElement('button'); button.className = 'mermaid-zoom-btn'; button.textContent = 'Phóng to'; button.type = 'button'
      button.onclick = event => { event.stopPropagation(); open(container.querySelector('svg')) }; container.appendChild(button)
      container.onclick = event => { if (!event.target.closest('a, button')) open(container.querySelector('svg')) }
    }
  }
  for (const img of document.querySelectorAll('.vp-doc img:not(.no-zoom)')) {
    if (img.dataset.zoomBound) continue
    img.dataset.zoomBound = 'true'; img.style.cursor = 'zoom-in'; img.tabIndex = 0; img.setAttribute('role', 'button'); img.setAttribute('aria-label', `Phóng to: ${img.alt || 'ảnh tài liệu'}`)
    img.onclick = () => open(img)
    img.onkeydown = event => { if (event.key === 'Enter' || event.key === ' ') { event.preventDefault(); open(img) } }
  }
}
onMounted(() => { attach(); observer = new MutationObserver(attach); observer.observe(document.querySelector('.VPContent') || document.body, { childList: true, subtree: true }) })
onUnmounted(() => { observer?.disconnect(); document.body.style.overflow = '' })
</script>

<template>
  <dialog ref="dialog" class="diagram-dialog" aria-label="Xem sơ đồ và ảnh tài liệu" @cancel.prevent="close" @click="event => { if (event.target === dialog) close() }">
    <div class="diagram-toolbar"><span>Ảnh & sơ đồ</span><div class="button-row"><button class="study-button" aria-label="Thu nhỏ" @click="scale = Math.max(.5, scale - .25)">−</button><span class="small">{{ Math.round(scale * 100) }}%</span><button class="study-button" aria-label="Phóng to" @click="scale = Math.min(4, scale + .25)">+</button><button class="study-button" @click="scale = 1">Đặt lại</button><button class="study-button primary" @click="close">Đóng</button></div></div>
    <div class="diagram-scroll"><div class="diagram-media" :style="{ width: `${scale * 100}%` }"><div v-if="svg" v-html="svg"></div><img v-else :src="image" alt="Ảnh tài liệu được phóng to"></div></div>
  </dialog>
</template>

<style>
.diagram-dialog { width: min(1100px, 94vw); max-width: 94vw; height: 88vh; max-height: 88vh; margin: auto; padding: 20px; border: 1px solid var(--vp-c-border); border-radius: 10px; background: var(--vp-c-bg); color: var(--vp-c-text-1); }
.diagram-dialog::backdrop { background: #121a24aa; }
.diagram-toolbar { display: flex; justify-content: space-between; align-items: center; gap: 15px; font-size: 14px; padding-bottom: 18px; border-bottom: 1px solid var(--vp-c-divider); }
.diagram-scroll { overflow: auto; height: calc(100% - 75px); padding-top: 25px; }
.diagram-media { margin: auto; }
.diagram-media svg { width: 100% !important; height: auto !important; max-width: none !important; }
.diagram-media img { width: 100%; height: auto; }
@media (max-width: 600px) { .diagram-toolbar > span { display: none; }.diagram-dialog { padding: 12px; }.diagram-toolbar .study-button { padding: 7px 10px; font-size: 11px; } }
</style>
