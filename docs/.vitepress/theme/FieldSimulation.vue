<script setup>
import { computed, ref } from 'vue'
const charges = ref([{ x: 230, y: 180, q: 1 }, { x: 510, y: 180, q: -1 }]), selected = ref(1), message = ref('')
const arrows = computed(() => {
  const result = []
  for (let y = 24; y < 360; y += 24) for (let x = 24; x < 740; x += 24) {
    if (charges.value.some(c => Math.hypot(x - c.x, y - c.y) < 28)) continue
    let ex = 0, ey = 0
    for (const c of charges.value) { const dx = x - c.x, dy = y - c.y, r = Math.max(12, Math.hypot(dx, dy)); ex += c.q * dx / r ** 3; ey += c.q * dy / r ** 3 }
    const magnitude = Math.hypot(ex, ey)
    if (magnitude < 1e-8) continue
    const size = 8 + Math.min(8, magnitude * 10000), nx = ex / magnitude, ny = ey / magnitude
    result.push({ x, y, x2: x + nx * size, y2: y + ny * size, head: `${x + nx * size - nx * 4 - ny * 3},${y + ny * size - ny * 4 + nx * 3} ${x + nx * size},${y + ny * size} ${x + nx * size - nx * 4 + ny * 3},${y + ny * size - ny * 4 - nx * 3}` })
  }
  return result
})
function add(x = 370, y = 180) {
  if (charges.value.length >= 8) { message.value = 'Tối đa 8 điện tích. Xóa một điện tích để thêm.'; return }
  if (charges.value.some(c => Math.hypot(c.x - x, c.y - y) < 24)) { message.value = 'Chọn vị trí cách điện tích hiện tại ít nhất 24 đơn vị.'; return }
  charges.value.push({ x, y, q: selected.value }); message.value = `Đã thêm điện tích ${selected.value > 0 ? 'dương' : 'âm'}.`
}
function place(event) {
  const svg = event.currentTarget, point = svg.createSVGPoint(); point.x = event.clientX; point.y = event.clientY
  const mapped = point.matrixTransform(svg.getScreenCTM().inverse())
  add(Math.max(20, Math.min(720, mapped.x)), Math.max(20, Math.min(340, mapped.y)))
}
function clear() { charges.value = []; message.value = 'Đã xóa toàn bộ điện tích.' }
</script>

<template>
  <div class="field-simulation">
    <p>Chọn dấu điện tích rồi nhấn vào vùng mô phỏng. Các mũi tên cho biết hướng điện trường tổng hợp.</p>
    <div class="simulation-toolbar"><div class="button-row"><button class="study-button" :aria-pressed="selected === 1" @click="selected = 1">Điện tích dương (+)</button><button class="study-button" :aria-pressed="selected === -1" @click="selected = -1">Điện tích âm (−)</button></div><div class="button-row"><button class="study-button" @click="add()">Thêm ở giữa</button><button class="study-button" @click="clear">Xóa tất cả</button></div></div>
    <svg class="field-canvas" viewBox="0 0 740 360" role="img" aria-labelledby="field-title field-description" @click="place"><title id="field-title">Mô phỏng điện trường của các điện tích điểm</title><desc id="field-description">Mũi tên hướng ra khỏi điện tích dương và hướng vào điện tích âm. Dùng các nút bên trên và bên dưới để điều khiển bằng bàn phím.</desc><g class="field-arrows" v-for="(a, i) in arrows" :key="i"><line :x1="a.x" :y1="a.y" :x2="a.x2" :y2="a.y2"/><polyline :points="a.head"/></g><g v-for="(c, i) in charges" :key="`charge-${i}`"><circle :cx="c.x" :cy="c.y" r="16" :fill="c.q > 0 ? '#244bd6' : '#a83d30'"/><text :x="c.x" :y="c.y + 6" text-anchor="middle" fill="white" font-size="22">{{ c.q > 0 ? '+' : '−' }}</text></g></svg>
    <p class="small" role="status">{{ message || `${charges.length} điện tích · Tối đa 8 điện tích` }}</p>
    <div v-if="charges.length" class="charge-list"><span class="small">Điện tích hiện tại</span><button v-for="(c, i) in charges" :key="i" class="study-button" @click="charges.splice(i, 1); message = 'Đã xóa điện tích.'">Xóa {{ c.q > 0 ? '+' : '−' }}q #{{ i + 1 }}</button></div>
    <div class="simulation-caption"><div><h3>E = −∇V</h3><p>Điện trường chỉ theo chiều điện thế giảm nhanh nhất. Điện tích thử dương chịu lực cùng chiều điện trường.</p></div><p class="small">Mô hình minh họa các điện tích có cùng độ lớn trong không gian 2D. Mũi tên được chuẩn hóa để dễ đọc, không biểu diễn độ lớn tuyệt đối.</p></div>
  </div>
</template>
