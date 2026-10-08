<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { lerp, perspectiveWeight } from './convex-geometry.mjs'

// Phép phối cảnh P(z, t) = z/t với t > 0. Trục ngang là z, trục đứng là t.
// Ảnh của một điểm là giao của tia từ gốc qua điểm đó với đường t = 1.
const svg = ref(null)
const view = ref(makeView({ x0: -1.5, x1: 7.5, y0: -0.4, y1: 4.2, width: 440, height: 300 }))
const P = p => view.value.point(p)
const pts = ref({ u: [1, 1], v: [6, 3] })
const drag = createDragger(svg, view, (name, value) => {
  if (value[1] < 0.3) return // giữ trong miền t > 0, tránh quá sát trục
  pts.value = { ...pts.value, [name]: value }
}, { step: 0.1, snap: 0.1 })
const theta = ref(0.5)
const w = computed(() => lerp(pts.value.u, pts.value.v, theta.value))
const persp = p => p[0] / p[1]
const mu = computed(() => perspectiveWeight(theta.value, pts.value.u[1], pts.value.v[1]))
const imageOfPoint = computed(() => persp(w.value))
const sameTheta = computed(() => theta.value * persp(pts.value.u) + (1 - theta.value) * persp(pts.value.v))
const ray = p => { const s = 4.4 / p[1]; return [p[0] * s, 4.4] }
</script>

<template>
  <figure class="study-lab" aria-label="Phép phối cảnh như một máy ảnh lỗ kim">
    <p class="lab-title">Chia cho tọa độ cuối: đoạn thẳng vẫn là đoạn thẳng</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Hai điểm u, v trong nửa mặt phẳng t dương, các tia từ gốc và ảnh của chúng trên đường t bằng 1" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <rect x="0" y="0" :width="view.width" :height="view.sy(0)" class="lab-region-soft" style="opacity: 0.35" />
      <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
      <line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
      <line x1="0" :x2="view.width" :y1="view.sy(1)" :y2="view.sy(1)" class="lab-line" />
      <text :x="view.width - 52" :y="view.sy(1) - 6" class="lab-small">t = 1</text>
      <text :x="view.width - 16" :y="view.sy(0) + 16" class="lab-small">z</text><text :x="view.sx(0) + 6" y="14" class="lab-small">t</text>
      <line v-for="name in ['u', 'v']" :key="`ray${name}`" :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P(ray(pts[name]))[0]" :y2="P(ray(pts[name]))[1]" class="lab-guide" />
      <line :x1="P([0, 0])[0]" :y1="P([0, 0])[1]" :x2="P(ray(w))[0]" :y2="P(ray(w))[1]" class="lab-guide" />
      <line :x1="P(pts.u)[0]" :y1="P(pts.u)[1]" :x2="P(pts.v)[0]" :y2="P(pts.v)[1]" class="lab-accent" />
      <line :x1="P([persp(pts.u), 1])[0]" :y1="P([persp(pts.u), 1])[1]" :x2="P([persp(pts.v), 1])[0]" :y2="P([persp(pts.v), 1])[1]" class="lab-good" />
      <circle :cx="P(w)[0]" :cy="P(w)[1]" r="7" class="lab-dot-warn" />
      <circle :cx="P([imageOfPoint, 1])[0]" :cy="P([imageOfPoint, 1])[1]" r="7" class="lab-dot-warn" />
      <circle :cx="P([sameTheta, 1])[0]" :cy="P([sameTheta, 1])[1]" r="6" class="lab-dot-hollow" />
      <circle v-for="name in ['u', 'v']" :key="name" :cx="P(pts[name])[0]" :cy="P(pts[name])[1]" r="9" class="lab-handle" tabindex="0" role="slider" :aria-label="`Điểm ${name} = (z, t)`" @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, pts[name], $event)" />
      <text :x="P(pts.u)[0] + 10" :y="P(pts.u)[1] - 10">u</text><text :x="P(pts.v)[0] + 10" :y="P(pts.v)[1] - 10">v</text>
    </svg>
    <div class="lab-controls">
      <label>θ = {{ fmt(theta) }}<input v-model.number="theta" type="range" min="0" max="1" step="0.05" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>u = {{ fmtPoint(pts.u, 1) }} có ảnh P(u) = {{ fmt(persp(pts.u)) }}, còn v = {{ fmtPoint(pts.v, 1) }} có ảnh P(v) = {{ fmt(persp(pts.v)) }}. Đoạn xanh lá là ảnh của đoạn tím.</p>
      <p>Điểm vàng θu + (1 − θ)v có ảnh <span class="is-accent">{{ fmt(imageOfPoint, 3) }}</span>. Ảnh này bằng μP(u) + (1 − μ)P(v) với μ = θt_u/(θt_u + (1 − θ)t_v) = {{ fmt(mu, 3) }}, chứ không phải với chính θ (vòng tròn rỗng, ứng với {{ fmt(sameTheta, 3) }}).</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Đặt u và v cùng độ cao t. Khi đó μ và θ có bằng nhau không?</li>
        <li>Kéo v lên cao hơn nhiều so với u. Điểm ảnh của trung điểm (θ = 0.5) lệch về phía P(u) hay P(v)?</li>
        <li>Kéo u lại gần trục z (t nhỏ). Ảnh P(u) chạy đi đâu?</li>
      </ol>
    </details>
  </figure>
</template>
