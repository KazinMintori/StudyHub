<script setup>
import { computed, onMounted, onBeforeUnmount, ref, shallowRef, useId, watch } from 'vue'

const props = defineProps({ svg: { type: Object, default: null }, axes: { type: String, default: 'xy' } })
const controlsId = `lab-point-${useId()}`
const handles = shallowRef([]), selected = ref(0), largeStep = ref(false)
const current = computed(() => handles.value[selected.value])
const label = element => element.getAttribute('aria-label')?.replace(/,\s*(?:kéo|dùng).*$/iu, '') || `Điểm ${handles.value.indexOf(element) + 1}`
const readout = computed(() => handles.value[selected.value]?.getAttribute('aria-valuetext') || '')
let observedSvg, observer, frame

function highlight() {
  for (const [index, element] of handles.value.entries()) element.classList.toggle('lab-handle-selected', selected.value === index)
}

function refresh() {
  const previous = current.value
  handles.value = [...(observedSvg?.querySelectorAll('.lab-handle') || [])]
  const retained = handles.value.indexOf(previous)
  selected.value = retained >= 0 ? retained : 0
  highlight()
}

function scheduleRefresh() {
  if (frame) return
  frame = requestAnimationFrame(() => { frame = null; refresh() })
}

function pick(event) {
  if (event.type === 'pointerdown' && event.isPrimary === false) return
  const handle = event.target.closest?.('.lab-handle')
  const index = handles.value.indexOf(handle)
  if (index >= 0) { selected.value = index; highlight() }
}

function disconnect() {
  observer?.disconnect()
  observedSvg?.removeEventListener('pointerdown', pick, true)
  observedSvg?.removeEventListener('focusin', pick, true)
  for (const handle of handles.value) handle.classList.remove('lab-handle-selected')
  if (frame) cancelAnimationFrame(frame)
  frame = null
}

function connect(svg) {
  disconnect()
  observedSvg = svg
  refresh()
  if (!svg) return
  svg.addEventListener('pointerdown', pick, true)
  svg.addEventListener('focusin', pick, true)
  observer = new MutationObserver(scheduleRefresh)
  observer.observe(svg, { childList: true, subtree: true, attributes: true, attributeFilter: ['aria-label', 'aria-valuetext'] })
}

function move(key) {
  if (!current.value?.isConnected) { refresh(); return }
  // Reuse each handle's existing keyboard route, including constraints such as
  // vertical-only fitting points and projection onto a feasible region.
  current.value.dispatchEvent(new KeyboardEvent('keydown', { key, shiftKey: largeStep.value, bubbles: true, cancelable: true }))
}

onMounted(() => connect(props.svg))
watch(() => props.svg, connect, { flush: 'post' })
watch(selected, highlight)
onBeforeUnmount(disconnect)
</script>

<template>
  <div v-if="handles.length" class="lab-point-controls" role="group" :aria-labelledby="`${controlsId}-title`">
    <p :id="`${controlsId}-title`" class="lab-point-heading">Di chuyển điểm không cần kéo</p>
    <div class="lab-point-options">
      <label :for="`${controlsId}-select`">Điểm cần điều chỉnh
        <select :id="`${controlsId}-select`" v-model.number="selected">
          <option v-for="(handle, index) in handles" :key="index" :value="index">{{ label(handle) }}</option>
        </select>
      </label>
      <label class="lab-point-step"><input v-model="largeStep" type="checkbox"> Di chuyển nhanh hơn</label>
    </div>
    <div class="lab-point-directions">
      <button type="button" aria-label="Dịch điểm sang trái" :disabled="!axes.includes('x')" @click="move('ArrowLeft')"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M16 10H4m5-5-5 5 5 5" /></svg><span>Trái</span></button>
      <button type="button" aria-label="Dịch điểm lên trên" :disabled="!axes.includes('y')" @click="move('ArrowUp')"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 16V4M5 9l5-5 5 5" /></svg><span>Lên</span></button>
      <button type="button" aria-label="Dịch điểm xuống dưới" :disabled="!axes.includes('y')" @click="move('ArrowDown')"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M10 4v12m-5-5 5 5 5-5" /></svg><span>Xuống</span></button>
      <button type="button" aria-label="Dịch điểm sang phải" :disabled="!axes.includes('x')" @click="move('ArrowRight')"><svg viewBox="0 0 20 20" aria-hidden="true"><path d="M4 10h12m-5-5 5 5-5 5" /></svg><span>Phải</span></button>
    </div>
    <p v-if="readout" class="lab-point-readout" role="status">{{ readout }}</p>
    <p v-if="axes === 'x'" class="lab-point-hint">Điểm này chỉ di chuyển sang trái hoặc sang phải.</p>
    <p v-else-if="axes === 'y'" class="lab-point-hint">Điểm này chỉ di chuyển lên hoặc xuống.</p>
    <p class="lab-point-hint">Chọn điểm rồi bấm nút hướng. Bạn vẫn có thể vuốt vùng trống để cuộn trang.</p>
  </div>
</template>
