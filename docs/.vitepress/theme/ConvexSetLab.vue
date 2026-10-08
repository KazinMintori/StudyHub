<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { convexHull, insideConvexPolygon, insidePolygon, add, scale, sub, combination } from './convex-geometry.mjs'

// type="test": kéo hai điểm trong một hình để kiểm tra định nghĩa tập lồi.
// type="hull": bao lồi của một tập điểm và các tổ hợp lồi của chúng.
const props = defineProps({ type: { type: String, default: 'test' } })
const svg = ref(null)
const view = ref(makeView({ x0: -4, x1: 4, y0: -3, y1: 3, width: 440, height: 330 }))
const P = p => view.value.point(p)

const regular = (k, r, phase = 0) => Array.from({ length: k }, (_, i) => [r * Math.cos(phase + (2 * Math.PI * i) / k), r * Math.sin(phase + (2 * Math.PI * i) / k)])
const star = Array.from({ length: 10 }, (_, i) => { const rr = i % 2 ? 1.1 : 2.6, t = Math.PI / 2 + (i * Math.PI) / 5; return [rr * Math.cos(t), rr * Math.sin(t)] })
const shapes = {
  hexagon: { label: 'Lục giác đều (kể cả biên)', convex: true, inside: p => insideConvexPolygon(p, regular(6, 2.5, Math.PI / 6)), outline: [regular(6, 2.5, Math.PI / 6)], pair: [[-1.5, -0.8], [1.8, 1.0]] },
  ellipse: { label: 'Elip đặc', convex: true, inside: ([x, y]) => (x / 3.2) ** 2 + (y / 2.2) ** 2 <= 1 + 1e-9, outline: [Array.from({ length: 80 }, (_, i) => [3.2 * Math.cos((2 * Math.PI * i) / 80), 2.2 * Math.sin((2 * Math.PI * i) / 80)])], pair: [[-2, 1], [2, -1]] },
  crescent: { label: 'Hình trăng khuyết', convex: false, inside: ([x, y]) => x * x + y * y <= 6.25 && (x - 1.4) ** 2 + y * y > 3.24, outline: [Array.from({ length: 80 }, (_, i) => [2.5 * Math.cos((2 * Math.PI * i) / 80), 2.5 * Math.sin((2 * Math.PI * i) / 80)]), Array.from({ length: 80 }, (_, i) => [1.4 + 1.8 * Math.cos((2 * Math.PI * i) / 80), 1.8 * Math.sin((2 * Math.PI * i) / 80)])], pair: [[0.2, 2.2], [0.2, -2.2]] },
  star: { label: 'Ngôi sao năm cánh', convex: false, inside: p => insidePolygon(p, star), outline: [star], pair: [star[0], star[2]].map(p => scale(0.92, p)) },
  union: { label: 'Hợp của hai hình tròn rời nhau', convex: false, inside: ([x, y]) => (x + 2) ** 2 + y * y <= 1.69 || (x - 2) ** 2 + y * y <= 1.69, outline: [-2, 2].map(c => Array.from({ length: 60 }, (_, i) => [c + 1.3 * Math.cos((2 * Math.PI * i) / 60), 1.3 * Math.sin((2 * Math.PI * i) / 60)])), pair: [[-2, 0.3], [2, -0.3]] }
}
const shapeKey = ref('crescent')
const shape = computed(() => shapes[shapeKey.value])
const pts = ref({ a: [0.2, 2.2], b: [0.2, -2.2] })
function pickShape(key) { shapeKey.value = key; const [a, b] = shapes[key].pair; pts.value = { a: [...a], b: [...b] } }

const points = ref([[-2.6, -1.2], [-1.2, 1.9], [0.4, 0.3], [1.5, 2.1], [2.8, 0.2], [1.6, -1.8], [-0.6, -2.1], [0.9, -0.4]])
const drag = createDragger(svg, view, (name, value) => {
  if (name === 'a' || name === 'b') pts.value = { ...pts.value, [name]: value }
  else points.value = points.value.map((p, i) => (String(i) === name ? value : p))
}, { step: 0.1, snap: 0.05 })

// --- test ---
const samples = computed(() => {
  const { a, b } = pts.value, out = []
  for (let i = 0; i <= 120; i++) { const t = i / 120; const p = add(b, scale(t, sub(a, b))); out.push({ p, ok: shape.value.inside(p) }) }
  return out
})
const pieces = computed(() => {
  const list = []
  for (const s of samples.value) {
    if (!list.length || list.at(-1).ok !== s.ok) list.push({ ok: s.ok, from: s.p, to: s.p })
    else list.at(-1).to = s.p
  }
  return list
})
const endpointsInside = computed(() => shape.value.inside(pts.value.a) && shape.value.inside(pts.value.b))
const segmentOk = computed(() => samples.value.every(s => s.ok))
const outsideFraction = computed(() => samples.value.filter(s => !s.ok).length / samples.value.length)

// --- hull ---
const hull = computed(() => convexHull(points.value))
const isVertex = p => hull.value.some(q => q[0] === p[0] && q[1] === p[1])
const mixWeights = ref(null)
function randomMix() {
  const raw = points.value.map(() => Math.random() ** 2)
  const total = raw.reduce((s, w) => s + w, 0)
  mixWeights.value = raw.map(w => w / total)
}
const mixPoint = computed(() => (mixWeights.value ? combination(points.value, mixWeights.value) : null))
function addPoint() { points.value = [...points.value, [Math.round((Math.random() * 6 - 3) * 10) / 10, Math.round((Math.random() * 4.4 - 2.2) * 10) / 10]]; mixWeights.value = null }
function removePoint() { if (points.value.length > 3) points.value = points.value.slice(0, -1); mixWeights.value = null }
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'test' ? 'Kiểm tra định nghĩa tập lồi bằng hai điểm' : 'Bao lồi của một tập điểm'">
    <p class="lab-title">{{ type === 'test' ? 'Đoạn nối hai điểm có ở lại trong tập không?' : 'Bao lồi: sợi dây chun quanh các điểm' }}</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" :aria-label="type === 'test' ? `Hình ${shape.label} và đoạn nối hai điểm` : 'Các điểm, bao lồi tô màu và các đỉnh của bao lồi'" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <template v-if="type === 'test'">
        <template v-if="shapeKey === 'crescent'">
          <circle :cx="view.sx(0)" :cy="view.sy(0)" :r="2.5 * view.width / 8" class="lab-region" />
          <circle :cx="view.sx(1.4)" :cy="view.sy(0)" :r="1.8 * view.width / 8" class="lab-cutout" />
        </template>
        <polygon v-for="(poly, i) in (shapeKey === 'crescent' ? [] : shape.outline)" :key="i" :points="poly.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <line v-for="(piece, i) in pieces" :key="`p${i}`" :x1="P(piece.from)[0]" :y1="P(piece.from)[1]" :x2="P(piece.to)[0]" :y2="P(piece.to)[1]" :class="piece.ok ? 'lab-good' : 'lab-bad'" />
        <circle v-for="name in ['a', 'b']" :key="name" :cx="P(pts[name])[0]" :cy="P(pts[name])[1]" r="9" class="lab-handle" tabindex="0" role="slider" :aria-label="`Điểm ${name === 'a' ? 'x' : 'y'}`" @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, pts[name], $event)" />
        <text :x="P(pts.a)[0] + 12" :y="P(pts.a)[1] - 8">x</text><text :x="P(pts.b)[0] + 12" :y="P(pts.b)[1] - 8">y</text>
      </template>
      <template v-else>
        <polygon v-if="hull.length >= 3" :points="hull.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <circle v-if="mixPoint" :cx="P(mixPoint)[0]" :cy="P(mixPoint)[1]" r="7" class="lab-dot-warn" />
        <circle v-for="(p, i) in points" :key="i" :cx="P(p)[0]" :cy="P(p)[1]" :r="isVertex(p) ? 9 : 7" :class="isVertex(p) ? 'lab-handle' : 'lab-handle lab-handle-alt'" tabindex="0" role="slider" :aria-label="`Điểm thứ ${i + 1}`" @pointerdown="drag.start(String(i), $event)" @keydown="drag.key(String(i), p, $event)" />
      </template>
    </svg>
    <div v-if="type === 'test'" class="lab-buttons" role="group" aria-label="Chọn hình">
      <button v-for="(item, key) in shapes" :key="key" :aria-pressed="shapeKey === key" @click="pickShape(key)">{{ item.label }}</button>
    </div>
    <div v-else class="lab-buttons">
      <button @click="randomMix">Lấy một tổ hợp lồi ngẫu nhiên</button>
      <button @click="addPoint">Thêm một điểm</button>
      <button @click="removePoint">Bỏ điểm cuối</button>
    </div>
    <div class="lab-readout" role="status">
      <template v-if="type === 'test'">
        <p v-if="!endpointsInside" class="is-bad">Có ít nhất một đầu mút nằm ngoài tập. Định nghĩa chỉ xét các cặp điểm thuộc tập, nên hãy kéo cả hai điểm vào vùng tô.</p>
        <p v-else-if="segmentOk"><span class="is-good">Cả đoạn [x, y] nằm trong tập.</span> Một cặp điểm tốt chưa chứng minh được tập lồi, vì định nghĩa đòi điều này với mọi cặp điểm.</p>
        <p v-else><span class="is-bad">Khoảng {{ Math.round(outsideFraction * 100) }}% đoạn [x, y] nằm ngoài tập.</span> Chỉ một cặp điểm như vậy là đủ để kết luận tập không lồi.</p>
        <p>Hình đang chọn {{ shape.convex ? 'là tập lồi: bạn sẽ không tìm được cặp điểm nào làm đoạn nối đi ra ngoài.' : 'không lồi: hãy tìm thêm những cặp điểm khác làm đoạn nối đi ra ngoài.' }}</p>
      </template>
      <template v-else>
        <p>Bao lồi có {{ hull.length }} đỉnh trong tổng số {{ points.length }} điểm. Các điểm màu vàng nằm bên trong và không phải đỉnh.</p>
        <p v-if="mixPoint">Tổ hợp lồi vừa lấy cho điểm {{ fmtPoint(mixPoint) }} với các trọng số {{ mixWeights.map(w => fmt(w)).join(', ') }} (tổng bằng 1). Điểm này luôn rơi vào vùng tô.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol v-if="type === 'test'">
        <li>Với hình trăng khuyết, tìm một cặp điểm làm đoạn nối cắt qua phần bị khoét. Có cặp điểm nào mà đoạn nối vẫn nằm trong tập không?</li>
        <li>Với ngôi sao, đặt hai điểm ở đầu hai cánh kề nhau. Rồi đặt chúng ở đầu hai cánh đối nhau. Trường hợp nào đoạn nối đi ra ngoài?</li>
        <li>Với lục giác và elip, cố gắng làm đoạn nối đi ra ngoài. Vì sao bạn không làm được?</li>
      </ol>
      <ol v-else>
        <li>Kéo một điểm bên trong ra ngoài bao lồi. Bao lồi thay đổi thế nào, và điểm đó có trở thành đỉnh không?</li>
        <li>Bấm lấy tổ hợp lồi ngẫu nhiên nhiều lần. Điểm vàng có bao giờ ra ngoài vùng tô không?</li>
        <li>Kéo một đỉnh vào bên trong. Đỉnh đó còn ảnh hưởng tới hình dạng bao lồi không?</li>
      </ol>
    </details>
  </figure>
</template>
