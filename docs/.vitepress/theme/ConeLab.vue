<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { add, scale, dot, norm2, cross2 } from './convex-geometry.mjs'
const clipId = `${useId()}-clip`

// type="conic": nón sinh bởi hai hoặc ba vector, và tổ hợp nón θ₁v₁ + θ₂v₂.
// type="dual": nón K sinh bởi hai vector và nón đối ngẫu K*, cùng một vector thử y.
const props = defineProps({ type: { type: String, default: 'conic' } })
const svg = ref(null)
const view = ref(makeView({ x0: -4, x1: 4, y0: -3, y1: 3, width: 440, height: 330 }))
const P = p => view.value.point(p)
const vecs = ref({ v1: [2, 0.5], v2: [0.8, 2], v3: [-2, -1.5], y: [1.5, -1] })
const useThird = ref(false)
const t1 = ref(1), t2 = ref(0.5)
const drag = createDragger(svg, view, (name, value) => { vecs.value = { ...vecs.value, [name]: value } }, { step: 0.1, snap: 0.1 })

// Mô tả nón sinh bởi các vector trong R² bằng các khoảng góc. Trả về { kind, from, sweep }.
const TWO_PI = 2 * Math.PI
function planarCone(gens) {
  const vs = gens.filter(v => norm2(v) > 1e-9)
  if (!vs.length) return { kind: 'origin' }
  const angles = vs.map(v => (Math.atan2(v[1], v[0]) + TWO_PI) % TWO_PI).sort((a, b) => a - b)
  let maxGap = -1, at = 0
  for (let i = 0; i < angles.length; i++) {
    const next = i === angles.length - 1 ? angles[0] + TWO_PI : angles[i + 1]
    const gap = next - angles[i]
    if (gap > maxGap) { maxGap = gap; at = i }
  }
  if (angles.length === 1 || maxGap >= TWO_PI - 1e-9) return { kind: 'ray', from: angles[0], sweep: 0 }
  const from = angles[(at + 1) % angles.length], sweep = TWO_PI - maxGap
  if (Math.abs(maxGap - Math.PI) < 1e-6) return { kind: 'halfplane-or-line', from, sweep }
  if (maxGap < Math.PI) return { kind: 'plane', from: 0, sweep: TWO_PI }
  return { kind: 'wedge', from, sweep }
}
function wedgePolygon(cone, radius = 9) {
  if (cone.kind === 'origin') return []
  const steps = Math.max(2, Math.ceil(cone.sweep / 0.05))
  const arc = Array.from({ length: steps + 1 }, (_, i) => { const a = cone.from + (cone.sweep * i) / steps; return [radius * Math.cos(a), radius * Math.sin(a)] })
  return cone.kind === 'plane' ? arc : [[0, 0], ...arc]
}

// --- conic ---
const gens = computed(() => (useThird.value ? [vecs.value.v1, vecs.value.v2, vecs.value.v3] : [vecs.value.v1, vecs.value.v2]))
const cone = computed(() => planarCone(gens.value))
const isLine = computed(() => !useThird.value && Math.abs(cross2(vecs.value.v1, vecs.value.v2)) < 1e-9 && dot(vecs.value.v1, vecs.value.v2) < 0)
const combo = computed(() => add(scale(t1.value, vecs.value.v1), scale(t2.value, vecs.value.v2)))
const coneLabel = computed(() => {
  if (isLine.value) return 'Hai vector ngược hướng nhau: tổ hợp nón của chúng phủ cả một đường thẳng qua gốc, tức là một không gian con.'
  const k = cone.value.kind
  if (k === 'plane') return 'Ba vector này sinh ra toàn bộ mặt phẳng: mọi vector đều là một tổ hợp với hệ số không âm của chúng.'
  if (k === 'halfplane-or-line') return 'Các vector sinh ra một nửa mặt phẳng đóng có biên đi qua gốc.'
  if (k === 'ray') return 'Các vector cùng hướng: nón chỉ là một tia xuất phát từ gốc.'
  return `Nón là một hình quạt đỉnh tại gốc với góc mở ${fmt((cone.value.sweep * 180) / Math.PI, 0)}°.`
})

// --- dual ---
const dualGens = computed(() => {
  const [a, b] = [vecs.value.v1, vecs.value.v2]
  if (Math.abs(cross2(a, b)) < 1e-9) return null
  const turn = cross2(a, b) > 0 ? 1 : -1
  return turn > 0 ? [[-a[1], a[0]], [b[1], -b[0]]] : [[a[1], -a[0]], [-b[1], b[0]]]
})
const dualCone = computed(() => (dualGens.value ? planarCone(dualGens.value) : null))
const yIn = computed(() => dot(vecs.value.y, vecs.value.v1) >= -1e-9 && dot(vecs.value.y, vecs.value.v2) >= -1e-9)
const halfplaneOfY = computed(() => planarCone([[-vecs.value.y[1], vecs.value.y[0]], vecs.value.y, [vecs.value.y[1], -vecs.value.y[0]]]))
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'conic' ? 'Nón sinh bởi các vector' : 'Nón và nón đối ngẫu'">
    <p class="lab-title">{{ type === 'conic' ? 'Tổ hợp với hệ số không âm' : 'Nón K và nón đối ngẫu K*' }}</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" :aria-label="type === 'conic' ? 'Hình quạt sinh bởi các vector và một tổ hợp nón' : 'Nón K, nón đối ngẫu K và vector thử y'" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <defs><clipPath :id="clipId"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <line :x1="view.sx(-4)" :x2="view.sx(4)" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" :y1="view.sy(-3)" :y2="view.sy(3)" class="lab-axis" />
      <g :clip-path="`url(#${clipId})`">
        <template v-if="type === 'conic'">
          <line v-if="isLine" :x1="P(scale(-9, vecs.v1))[0]" :y1="P(scale(-9, vecs.v1))[1]" :x2="P(scale(9, vecs.v1))[0]" :y2="P(scale(9, vecs.v1))[1]" class="lab-accent" />
          <polygon v-else :points="wedgePolygon(cone).map(p => P(p).join(',')).join(' ')" class="lab-region" />
          <template v-if="!useThird">
            <line :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P(scale(t1, vecs.v1))[0]" :y2="P(scale(t1, vecs.v1))[1]" class="lab-guide" />
            <line :x1="P(scale(t1, vecs.v1))[0]" :y1="P(scale(t1, vecs.v1))[1]" :x2="P(combo)[0]" :y2="P(combo)[1]" class="lab-guide" />
            <circle :cx="P(combo)[0]" :cy="P(combo)[1]" r="7" class="lab-dot-warn" />
          </template>
        </template>
        <template v-else>
          <polygon v-if="halfplaneOfY" :points="wedgePolygon(halfplaneOfY).map(p => P(p).join(',')).join(' ')" class="lab-region-soft" />
          <polygon :points="wedgePolygon(planarCone([vecs.v1, vecs.v2])).map(p => P(p).join(',')).join(' ')" class="lab-region" />
          <polygon v-if="dualCone" :points="wedgePolygon(dualCone).map(p => P(p).join(',')).join(' ')" class="lab-good-fill" opacity="0.55" />
          <line :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P(vecs.y)[0]" :y2="P(vecs.y)[1]" :class="yIn ? 'lab-good' : 'lab-bad'" />
        </template>
      </g>
      <line v-for="name in (type === 'conic' && useThird ? ['v1', 'v2', 'v3'] : ['v1', 'v2'])" :key="`l${name}`" :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P(vecs[name])[0]" :y2="P(vecs[name])[1]" class="lab-line" />
      <circle v-for="name in (type === 'conic' && useThird ? ['v1', 'v2', 'v3'] : ['v1', 'v2'])" :key="name" :cx="P(vecs[name])[0]" :cy="P(vecs[name])[1]" r="9" class="lab-handle" tabindex="0" role="slider" :aria-label="`Vector ${name}`" @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, vecs[name], $event)" />
      <text v-for="name in (type === 'conic' && useThird ? ['v1', 'v2', 'v3'] : ['v1', 'v2'])" :key="`t${name}`" :x="P(vecs[name])[0] + 12" :y="P(vecs[name])[1] - 8">{{ name === 'v1' ? 'v₁' : name === 'v2' ? 'v₂' : 'v₃' }}</text>
      <template v-if="type === 'dual'">
        <circle :cx="P(vecs.y)[0]" :cy="P(vecs.y)[1]" r="9" class="lab-handle lab-handle-alt" tabindex="0" role="slider" aria-label="Vector thử y" @pointerdown="drag.start('y', $event)" @keydown="drag.key('y', vecs.y, $event)" />
        <text :x="P(vecs.y)[0] + 12" :y="P(vecs.y)[1] + 18">y</text>
      </template>
    </svg>
    <div v-if="type === 'conic'" class="lab-controls">
      <label>θ₁ = {{ fmt(t1) }}<input v-model.number="t1" type="range" min="0" max="2" step="0.05" :disabled="useThird" /></label>
      <label>θ₂ = {{ fmt(t2) }}<input v-model.number="t2" type="range" min="0" max="2" step="0.05" :disabled="useThird" /></label>
      <label class="lab-check"><input v-model="useThird" type="checkbox" /> Thêm vector thứ ba v₃</label>
    </div>
    <div class="lab-readout" role="status">
      <template v-if="type === 'conic'">
        <p v-if="!useThird">θ₁v₁ + θ₂v₂ = <span class="is-accent">{{ fmtPoint(combo) }}</span> với θ₁, θ₂ ≥ 0. Không có ràng buộc θ₁ + θ₂ = 1, nên điểm có thể chạy ra xa tùy ý.</p>
        <p>{{ coneLabel }}</p>
      </template>
      <template v-else>
        <p>yᵀv₁ = {{ fmt(dot(vecs.y, vecs.v1)) }} và yᵀv₂ = {{ fmt(dot(vecs.y, vecs.v2)) }}.</p>
        <p v-if="yIn"><span class="is-good">Cả hai tích vô hướng đều không âm, nên y thuộc K*.</span> Nửa mặt phẳng nhạt {x : yᵀx ≥ 0} chứa trọn nón K.</p>
        <p v-else><span class="is-bad">Có một tích vô hướng âm, nên y không thuộc K*.</span> Nửa mặt phẳng nhạt {x : yᵀx ≥ 0} không chứa trọn K.</p>
        <p v-if="!dualCone">Hai vector sinh thẳng hàng. Hãy kéo chúng ra để nón K có góc mở dương.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol v-if="type === 'conic'">
        <li>Giữ θ₂ = 0 và tăng θ₁. Điểm chạy theo tia nào?</li>
        <li>Kéo v₂ dần về phía ngược hướng với v₁. Góc mở của nón thay đổi thế nào ngay trước khi hai vector thẳng hàng?</li>
        <li>Bật v₃ và kéo nó sao cho ba vector "bao quanh" gốc. Lúc đó nón là gì?</li>
      </ol>
      <ol v-else>
        <li>Kéo y vòng quanh gốc. Vùng màu xanh, tức K*, gồm những hướng nào?</li>
        <li>Mở rộng góc của K. K* to ra hay nhỏ lại?</li>
        <li>Đặt v₁ = (1, 0) và v₂ = (0, 1). Khi đó K và K* có quan hệ gì?</li>
      </ol>
    </details>
  </figure>
</template>
