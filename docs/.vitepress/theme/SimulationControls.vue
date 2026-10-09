<script setup>
import { computed, ref, watch } from 'vue'
import { useSimulationVisibility } from './simulation-visibility'

const props = defineProps({
  modelValue: { type: Number, required: true },
  max: { type: Number, required: true },
  resetKey: { default: null },
  label: { type: String, default: 'Bước' }
})
const emit = defineEmits(['update:modelValue'])
const root = ref(null), playing = ref(false), speed = ref(1)
let timer
function pause() { playing.value = false; clearTimeout(timer) }
const { visible, reducedMotion } = useSimulationVisibility(root, pause)
const atEnd = computed(() => props.modelValue >= props.max)
function seek(value) {
  pause()
  emit('update:modelValue', Math.max(0, Math.min(props.max, Number(value))))
}
function schedule() {
  clearTimeout(timer)
  if (!playing.value) return
  timer = setTimeout(() => {
    if (!visible.value || document.hidden || atEnd.value) { pause(); return }
    emit('update:modelValue', props.modelValue + 1)
  }, 1000 / speed.value)
}
function toggle() {
  if (playing.value) { pause(); return }
  if (atEnd.value) emit('update:modelValue', 0)
  playing.value = true
  schedule()
}
watch(() => props.modelValue, () => { if (atEnd.value) pause(); else schedule() })
watch(speed, schedule)
watch(() => props.resetKey, pause)
watch(() => props.max, pause)
</script>

<template>
  <div ref="root" class="simulation-controls" role="group" aria-label="Điều khiển mô phỏng">
    <div class="playback-buttons">
      <button type="button" class="play-toggle" :aria-pressed="playing" :disabled="max === 0" @click="toggle">
        <svg viewBox="0 0 20 20" aria-hidden="true"><path v-if="playing" d="M6 4v12M14 4v12" /><path v-else d="m6 3 10 7-10 7Z" /></svg>
        {{ playing ? 'Tạm dừng' : atEnd ? 'Phát lại' : 'Phát' }}
      </button>
      <button type="button" :disabled="modelValue === 0" aria-label="Lùi một bước" @click="seek(modelValue - 1)">← Lùi</button>
      <button type="button" :disabled="atEnd" aria-label="Tiến một bước" @click="seek(modelValue + 1)">Tiếp →</button>
      <button type="button" :disabled="modelValue === 0 && !playing" @click="seek(0)">Đặt lại</button>
    </div>
    <div class="playback-timeline">
      <label class="step-slider">{{ label }} {{ modelValue }} / {{ max }}
        <input type="range" min="0" :max="max" step="1" :value="modelValue" :disabled="max === 0" @input="seek($event.target.value)">
      </label>
      <label class="playback-speed">Tốc độ
        <select v-model.number="speed"><option :value=".5">0.5×</option><option :value="1">1×</option><option :value="2">2×</option></select>
      </label>
    </div>
    <p v-if="reducedMotion" class="motion-note">Đang giảm chuyển động theo cài đặt thiết bị. Bạn vẫn có thể xem từng bước hoặc nhấn Phát.</p>
  </div>
</template>

<style scoped>
.simulation-controls { margin: var(--space-4) 0; padding: var(--space-4); border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper); font: var(--fs-small)/1.5 var(--font-ui); }
.playback-buttons { display: flex; flex-wrap: wrap; gap: var(--space-2); }
.simulation-controls button, .simulation-controls select { min-height: 44px; border: 1px solid var(--control); border-radius: var(--radius); padding: var(--space-2) var(--space-3); background: var(--paper); color: var(--ink); font: inherit; cursor: pointer; }
.simulation-controls button:hover:not(:disabled) { border-color: var(--tim); background: var(--tim-soft); }
.simulation-controls .play-toggle { display: inline-flex; align-items: center; justify-content: center; gap: var(--space-2); min-width: 120px; background: var(--tim); border-color: var(--tim); color: var(--paper); }
.simulation-controls .play-toggle:hover:not(:disabled) { background: var(--tim-hover); color: var(--paper); }
.play-toggle svg { width: 18px; height: 18px; margin: 0; stroke: currentColor; stroke-width: 2; fill: none; }
.simulation-controls button:disabled { opacity: .5; cursor: default; }
.simulation-controls :is(button, select, input):focus-visible { outline: 3px solid var(--tim); outline-offset: 3px; }
.playback-timeline { display: flex; align-items: end; flex-wrap: wrap; gap: var(--space-4); margin-top: var(--space-3); }
.simulation-controls label { display: grid; gap: var(--space-1); margin: 0; font: inherit; font-variant-numeric: tabular-nums; }
.step-slider { flex: 1 1 160px; min-width: 0; }
.simulation-controls input { width: 100%; min-height: 44px; accent-color: var(--tim); cursor: pointer; }
.simulation-controls .motion-note { margin: var(--space-2) 0 0; font: inherit; color: var(--ink-2); }
@media (max-width: 480px) { .playback-buttons { display: grid; grid-template-columns: 1fr 1fr; } .simulation-controls { padding: var(--space-3); } }
</style>
