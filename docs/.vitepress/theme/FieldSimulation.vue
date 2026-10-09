<script setup>
import { computed, ref, useId, watch } from 'vue'
import { electricField, fieldLines } from './electric-field.mjs'
import { useSimulationVisibility } from './simulation-visibility'

const presets = {
  dipole: [{ x: 230, y: 180, q: 1 }, { x: 510, y: 180, q: -1 }],
  positive: [{ x: 370, y: 180, q: 1 }],
  pair: [{ x: 230, y: 180, q: 1 }, { x: 510, y: 180, q: 1 }]
}
const charges = ref(presets.dipole.map(c => ({ ...c }))), selected = ref(1), message = ref('')
const root = ref(null), playing = ref(false), speed = ref(1), showArrows = ref(true), showLines = ref(true), active = ref(0)
const { reducedMotion } = useSimulationVisibility(root, () => { playing.value = false })
const titleId = `field-title-${useId()}`, descriptionId = `${titleId}-description`
const activeCharge = computed(() => charges.value[active.value])
const lines = computed(() => fieldLines(charges.value))
watch(showLines, value => { if (!value) playing.value = false })
const arrows = computed(() => {
  const result = []
  for (let y = 24; y < 360; y += 24) for (let x = 24; x < 740; x += 24) {
    if (charges.value.some(c => Math.hypot(x - c.x, y - c.y) < 28)) continue
    const { ex, ey, magnitude } = electricField(charges.value, x, y)
    if (magnitude < 1e-8) continue
    const size = 8 + Math.min(8, magnitude * 10000), nx = ex / magnitude, ny = ey / magnitude
    result.push({ x, y, x2: x + nx * size, y2: y + ny * size, head: `${x + nx * size - nx * 4 - ny * 3},${y + ny * size - ny * 4 + nx * 3} ${x + nx * size},${y + ny * size} ${x + nx * size - nx * 4 + ny * 3},${y + ny * size - ny * 4 - nx * 3}` })
  }
  return result
})
function add(x = 370, y = 180) {
  x = Math.max(20, Math.min(720, x)); y = Math.max(20, Math.min(340, y))
  if (charges.value.length >= 8) { message.value = 'Tối đa 8 điện tích. Xóa một điện tích để thêm.'; return }
  if (charges.value.some(c => Math.hypot(c.x - x, c.y - y) < 36)) { message.value = 'Chọn vị trí cách điện tích hiện tại ít nhất 36 đơn vị.'; return }
  charges.value.push({ x, y, q: selected.value }); active.value = charges.value.length - 1
  message.value = `Đã thêm điện tích ${selected.value > 0 ? 'dương' : 'âm'}.`
}
function mappedPoint(event) {
  const svg = event.currentTarget, point = svg.createSVGPoint(); point.x = event.clientX; point.y = event.clientY
  return point.matrixTransform(svg.getScreenCTM().inverse())
}
let dragging = null, suppressClick = false
function beginDrag(event, index) {
  if (event.button !== 0 || dragging !== null) return
  active.value = index; dragging = event.pointerId; suppressClick = true
  event.currentTarget.ownerSVGElement.setPointerCapture(event.pointerId)
}
function moveCharge(x, y) {
  x = Math.max(20, Math.min(720, x)); y = Math.max(20, Math.min(340, y))
  if (charges.value.some((c, i) => i !== active.value && Math.hypot(c.x - x, c.y - y) < 36)) {
    message.value = 'Giữ các điện tích cách nhau ít nhất 36 đơn vị.'; return
  }
  Object.assign(activeCharge.value, { x, y }); message.value = ''
}
function drag(event) {
  if (dragging !== event.pointerId) return
  const point = mappedPoint(event); moveCharge(Math.round(point.x), Math.round(point.y))
}
function endDrag(event) {
  if (dragging !== event.pointerId) return
  dragging = null
  if (event.type === 'pointercancel') suppressClick = false
  if (event.currentTarget.hasPointerCapture(event.pointerId)) event.currentTarget.releasePointerCapture(event.pointerId)
}
function place(event) {
  if (suppressClick) { suppressClick = false; return }
  const point = mappedPoint(event); add(Math.round(point.x), Math.round(point.y))
}
function loadPreset(name) {
  playing.value = false; dragging = null; suppressClick = false
  charges.value = (presets[name] || []).map(c => ({ ...c })); active.value = 0
  message.value = name ? 'Đã nạp cấu hình mẫu.' : 'Đã xóa toàn bộ điện tích.'
}
function remove(index) {
  charges.value.splice(index, 1); active.value = Math.min(Math.max(0, active.value), charges.value.length - 1)
  if (!charges.value.length) playing.value = false
  message.value = 'Đã xóa điện tích.'
}
</script>

<template>
  <div ref="root" class="field-simulation">
    <p>Chọn dấu rồi nhấn vào vùng trống để thêm điện tích. Kéo điện tích để thay đổi vị trí, hoặc dùng các thanh chỉnh bên dưới.</p>
    <div class="simulation-toolbar">
      <div class="button-row"><button type="button" class="study-button" :aria-pressed="selected === 1" @click="selected = 1">Dương (+)</button><button type="button" class="study-button" :aria-pressed="selected === -1" @click="selected = -1">Âm (−)</button></div>
      <label class="field-preset">Cấu hình mẫu<select aria-label="Cấu hình điện tích" value="" @change="loadPreset($event.target.value); $event.target.value = ''"><option value="" disabled>Chọn cấu hình…</option><option value="dipole">Lưỡng cực (+, −)</option><option value="positive">Một điện tích dương</option><option value="pair">Hai điện tích dương</option></select></label>
    </div>
    <div class="field-display-options">
      <label><input v-model="showArrows" type="checkbox"> Mũi tên</label><label><input v-model="showLines" type="checkbox"> Đường sức</label>
      <button type="button" class="study-button" :aria-pressed="playing" :disabled="!charges.length || !showLines || reducedMotion" @click="playing = !playing">{{ playing ? 'Tạm dừng' : 'Chạy chỉ báo chiều' }}</button>
      <label>Tốc độ<select v-model.number="speed"><option :value=".5">0.5×</option><option :value="1">1×</option><option :value="2">2×</option></select></label>
    </div>
    <svg class="field-canvas" viewBox="0 0 740 360" role="img" :aria-labelledby="`${titleId} ${descriptionId}`" @click="place" @pointermove="drag" @pointerup="endDrag" @pointercancel="endDrag" @lostpointercapture="dragging = null">
      <title :id="titleId">Mô phỏng điện trường của các điện tích điểm</title><desc :id="descriptionId">Mũi tên và đường sức hướng ra khỏi điện tích dương, hướng vào điện tích âm. Dùng các thanh chỉnh vị trí và nút bên dưới để điều khiển bằng bàn phím.</desc>
      <g v-if="showArrows" class="field-arrows"><g v-for="(a, i) in arrows" :key="i"><line :x1="a.x" :y1="a.y" :x2="a.x2" :y2="a.y2"/><polyline :points="a.head"/></g></g>
      <g v-if="showLines" class="field-lines"><path v-for="(line,i) in lines" :key="`line-${i}`" :d="line"/><path v-for="(line,i) in lines" :key="`flow-${i}`" :d="line" class="field-flow" :style="{ animationPlayState: playing ? 'running' : 'paused', animationDuration: `${1.4/speed}s` }"/></g>
      <g v-for="(c, i) in charges" :key="`charge-${i}`" class="field-charge" @pointerdown.stop="beginDrag($event, i)" @click.stop="active = i; suppressClick = false">
        <circle :cx="c.x" :cy="c.y" r="23" class="charge-hit"/><circle v-if="active === i" :cx="c.x" :cy="c.y" r="21" class="charge-selection"/><circle :cx="c.x" :cy="c.y" r="16" :class="c.q > 0 ? 'charge-positive' : 'charge-negative'"/><text :x="c.x" :y="c.y + 6" text-anchor="middle" font-size="22">{{ c.q > 0 ? '+' : '−' }}</text>
      </g>
      <text v-if="!charges.length" x="370" y="180" text-anchor="middle" class="field-empty">Thêm điện tích để bắt đầu</text>
    </svg>
    <p v-if="reducedMotion" class="small">Đang giảm chuyển động theo cài đặt thiết bị; đường sức hiển thị tĩnh.</p>
    <p class="small" role="status">{{ message || `${charges.length} điện tích · Tối đa 8 điện tích` }}</p>
    <div class="button-row"><button type="button" class="study-button" :disabled="charges.length >= 8" @click="add()">Thêm ở giữa</button><button type="button" class="study-button" :disabled="!charges.length" @click="loadPreset('')">Xóa tất cả</button></div>
    <div v-if="charges.length" class="charge-editor">
      <label>Điện tích đang chỉnh<select v-model.number="active"><option v-for="(c,i) in charges" :key="i" :value="i">#{{ i+1 }} · {{ c.q > 0 ? '+q' : '−q' }}</option></select></label>
      <label>Vị trí ngang x = {{ activeCharge.x }}<input type="range" min="20" max="720" :value="activeCharge.x" @input="moveCharge(Number($event.target.value), activeCharge.y)"></label>
      <label>Vị trí dọc y = {{ activeCharge.y }}<input type="range" min="20" max="340" :value="activeCharge.y" @input="moveCharge(activeCharge.x, Number($event.target.value))"></label>
      <button type="button" class="study-button" @click="remove(active)">Xóa #{{ active+1 }}</button>
    </div>
    <div class="simulation-caption"><div><h3>E = −∇V</h3><p>Điện trường chỉ theo chiều điện thế giảm nhanh nhất. Điện tích thử dương chịu lực cùng chiều điện trường.</p></div><p class="small">Các điện tích điểm có cùng độ lớn, xét trên một mặt phẳng. Mũi tên được chuẩn hóa; các nét chuyển động chỉ chiều đường sức, không mô tả quỹ đạo hay vận tốc của hạt. Đường sức được vẽ gần đúng bằng các bước hữu hạn.</p></div>
  </div>
</template>
