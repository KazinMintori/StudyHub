<script setup>
import { computed, ref } from 'vue'
import { makeView, createDragger, fmt, fmtPoint } from './svg-drag'
import { add, sub, scale, dot, norm2, convexHull, closestPolygons, polygonsIntersect, insideConvexPolygon } from './convex-geometry.mjs'

// type="sets": hai đa giác lồi kéo được, siêu phẳng trung trực của cặp điểm gần nhất.
// type="data": hai lớp điểm, bao lồi của mỗi lớp và đường tách có lề lớn nhất (§8.6.1 của sách).
// type="support": siêu phẳng tựa tại một điểm trên biên của một đa giác lồi.
const props = defineProps({ type: { type: String, default: 'sets' } })
const svg = ref(null)
const view = ref(makeView({ x0: -5, x1: 5, y0: -3.75, y1: 3.75, width: 440, height: 330 }))
const P = p => view.value.point(p)

function clipLine(p, d) {
  const v = view.value
  let t0 = -1e9, t1 = 1e9
  for (const [dv, lo, hi, pv] of [[d[0], v.x0, v.x1, p[0]], [d[1], v.y0, v.y1, p[1]]]) {
    if (Math.abs(dv) < 1e-12) { if (pv < lo || pv > hi) return null; continue }
    const s = (lo - pv) / dv, e = (hi - pv) / dv
    t0 = Math.max(t0, Math.min(s, e)); t1 = Math.min(t1, Math.max(s, e))
  }
  return t0 <= t1 ? [add(p, scale(t0, d)), add(p, scale(t1, d))] : null
}
const linePath = (p, d) => { const seg = clipLine(p, d); return seg ? { x1: P(seg[0])[0], y1: P(seg[0])[1], x2: P(seg[1])[0], y2: P(seg[1])[1] } : null }

// --- sets ---
const shapeA = [[-1, -0.9], [1.1, -0.4], [-0.2, 1.2]]
const shapeB = Array.from({ length: 5 }, (_, i) => [1.05 * Math.cos(Math.PI / 2 + (2 * Math.PI * i) / 5), 1.05 * Math.sin(Math.PI / 2 + (2 * Math.PI * i) / 5)])
const centers = ref({ A: [-2.4, -0.6], B: [2.2, 0.8] })
const polyA = computed(() => shapeA.map(p => add(p, centers.value.A)))
const polyB = computed(() => shapeB.map(p => add(p, centers.value.B)))
const setsIntersect = computed(() => polygonsIntersect(polyA.value, polyB.value))
const closest = computed(() => closestPolygons(polyA.value, polyB.value))

// --- data ---
const classX = ref([[-3, 1.5], [-2, 2.6], [-1.2, 1], [-2.6, -0.2]])
const classY = ref([[1.2, -1.4], [2.6, -0.4], [1.8, -2.6], [3.4, -2]])
const hullX = computed(() => convexHull(classX.value)), hullY = computed(() => convexHull(classY.value))
const dataIntersect = computed(() => polygonsIntersect(hullX.value, hullY.value) || classX.value.some(p => hullY.value.length >= 3 && insideConvexPolygon(p, hullY.value)) || classY.value.some(p => hullX.value.length >= 3 && insideConvexPolygon(p, hullX.value)))
const gap = computed(() => closestPolygons(hullX.value, hullY.value))

// --- support ---
const pentagon = [[-2.2, -1.6], [1.6, -2.1], [2.6, 0.4], [0.4, 2.4], [-2.4, 1.0]]
const perimeter = pentagon.map((p, i) => norm2(sub(pentagon[(i + 1) % pentagon.length], p)))
const total = perimeter.reduce((s, l) => s + l, 0)
const sParam = ref(0.12), fan = ref(0.5)
const outward = i => { const p = pentagon[i], q = pentagon[(i + 1) % pentagon.length], d = sub(q, p), n = [d[1], -d[0]]; return scale(1 / norm2(n), n) }
const boundary = computed(() => {
  let rest = sParam.value * total
  for (let i = 0; i < pentagon.length; i++) {
    if (rest <= perimeter[i] + 1e-12) {
      const t = rest / perimeter[i], p = add(pentagon[i], scale(t, sub(pentagon[(i + 1) % pentagon.length], pentagon[i])))
      if (t < 0.02) return { point: pentagon[i], vertex: i }
      if (t > 0.98) return { point: pentagon[(i + 1) % pentagon.length], vertex: (i + 1) % pentagon.length }
      return { point: p, edge: i }
    }
    rest -= perimeter[i]
  }
  return { point: pentagon[0], vertex: 0 }
})
const normal = computed(() => {
  const b = boundary.value
  if (b.edge !== undefined) return outward(b.edge)
  const n1 = outward((b.vertex + pentagon.length - 1) % pentagon.length), n2 = outward(b.vertex)
  const a1 = Math.atan2(n1[1], n1[0]); let a2 = Math.atan2(n2[1], n2[0])
  while (a2 < a1) a2 += 2 * Math.PI
  const a = a1 + fan.value * (a2 - a1)
  return [Math.cos(a), Math.sin(a)]
})
const supportOk = computed(() => pentagon.every(v => dot(normal.value, v) <= dot(normal.value, boundary.value.point) + 1e-9))
const centerHandle = name => name
const drag = createDragger(svg, view, (name, value) => {
  if (name === 'A' || name === 'B') centers.value = { ...centers.value, [name]: value }
  else if (name.startsWith('x')) classX.value = classX.value.map((p, i) => (`x${i}` === name ? value : p))
  else if (name.startsWith('y')) classY.value = classY.value.map((p, i) => (`y${i}` === name ? value : p))
}, { step: 0.1, snap: 0.05 })
</script>

<template>
  <figure class="study-lab" :aria-label="type === 'support' ? 'Siêu phẳng tựa của một đa giác lồi' : 'Siêu phẳng phân tách hai tập lồi'">
    <p class="lab-title">{{ type === 'sets' ? 'Một siêu phẳng giữa hai tập lồi rời nhau' : type === 'data' ? 'Tách hai lớp dữ liệu với lề lớn nhất' : 'Siêu phẳng tựa tại một điểm biên' }}</p>
    <svg ref="svg" :viewBox="`0 0 ${view.width} ${view.height}`" role="img" :aria-label="type === 'support' ? 'Ngũ giác lồi, một điểm trên biên và đường thẳng tựa tại điểm đó' : 'Hai tập, cặp điểm gần nhất và đường thẳng phân tách'" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end">
      <line :x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-grid" /><line :y1="0" :y2="view.height" :x1="view.sx(0)" :x2="view.sx(0)" class="lab-grid" />

      <template v-if="type === 'sets'">
        <polygon :points="polyA.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <polygon :points="polyB.map(p => P(p).join(',')).join(' ')" class="lab-good-fill" />
        <template v-if="!setsIntersect && closest.distance > 1e-6">
          <line v-if="linePath(scale(0.5, add(closest.p, closest.q)), [-(closest.q[1] - closest.p[1]), closest.q[0] - closest.p[0]])" v-bind="linePath(scale(0.5, add(closest.p, closest.q)), [-(closest.q[1] - closest.p[1]), closest.q[0] - closest.p[0]])" class="lab-accent" />
          <line :x1="P(closest.p)[0]" :y1="P(closest.p)[1]" :x2="P(closest.q)[0]" :y2="P(closest.q)[1]" class="lab-guide" />
          <circle :cx="P(closest.p)[0]" :cy="P(closest.p)[1]" r="5" class="lab-dot" /><circle :cx="P(closest.q)[0]" :cy="P(closest.q)[1]" r="5" class="lab-dot" />
          <text :x="P(closest.p)[0] - 14" :y="P(closest.p)[1] + 18">c</text><text :x="P(closest.q)[0] + 6" :y="P(closest.q)[1] + 18">d</text>
        </template>
        <circle v-for="name in ['A', 'B']" :key="name" :cx="P(centers[name])[0]" :cy="P(centers[name])[1]" r="9" class="lab-handle lab-handle-alt" tabindex="0" role="slider" :aria-label="`Tâm của tập ${name === 'A' ? 'C' : 'D'}, kéo để dời tập`" @pointerdown="drag.start(name, $event)" @keydown="drag.key(name, centers[name], $event)" />
        <text :x="P(centers.A)[0] - 6" :y="P(centers.A)[1] - 14">C</text><text :x="P(centers.B)[0] - 6" :y="P(centers.B)[1] - 14">D</text>
      </template>

      <template v-else-if="type === 'data'">
        <polygon v-if="hullX.length >= 2" :points="hullX.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <polygon v-if="hullY.length >= 2" :points="hullY.map(p => P(p).join(',')).join(' ')" class="lab-good-fill" />
        <template v-if="!dataIntersect && gap.distance > 1e-6">
          <template v-for="(base, i) in [gap.p, scale(0.5, add(gap.p, gap.q)), gap.q]" :key="i">
            <line v-if="linePath(base, [-(gap.q[1] - gap.p[1]), gap.q[0] - gap.p[0]])" v-bind="linePath(base, [-(gap.q[1] - gap.p[1]), gap.q[0] - gap.p[0]])" :class="i === 1 ? 'lab-accent' : 'lab-guide'" />
          </template>
          <line :x1="P(gap.p)[0]" :y1="P(gap.p)[1]" :x2="P(gap.q)[0]" :y2="P(gap.q)[1]" class="lab-warn" />
        </template>
        <circle v-for="(p, i) in classX" :key="`x${i}`" :cx="P(p)[0]" :cy="P(p)[1]" r="8" class="lab-handle" tabindex="0" role="slider" :aria-label="`Điểm lớp thứ nhất số ${i + 1}`" @pointerdown="drag.start(`x${i}`, $event)" @keydown="drag.key(`x${i}`, p, $event)" />
        <rect v-for="(p, i) in classY" :key="`y${i}`" :x="P(p)[0] - 8" :y="P(p)[1] - 8" width="16" height="16" class="lab-handle lab-handle-alt" tabindex="0" role="slider" :aria-label="`Điểm lớp thứ hai số ${i + 1}`" @pointerdown="drag.start(`y${i}`, $event)" @keydown="drag.key(`y${i}`, p, $event)" />
      </template>

      <template v-else>
        <polygon :points="pentagon.map(p => P(p).join(',')).join(' ')" class="lab-region" />
        <line v-if="linePath(boundary.point, [-normal[1], normal[0]])" v-bind="linePath(boundary.point, [-normal[1], normal[0]])" :class="supportOk ? 'lab-accent' : 'lab-bad'" />
        <line :x1="P(boundary.point)[0]" :y1="P(boundary.point)[1]" :x2="P(add(boundary.point, scale(1.2, normal)))[0]" :y2="P(add(boundary.point, scale(1.2, normal)))[1]" class="lab-warn" />
        <text :x="P(add(boundary.point, scale(1.35, normal)))[0]" :y="P(add(boundary.point, scale(1.35, normal)))[1]" class="lab-small">a</text>
        <circle :cx="P(boundary.point)[0]" :cy="P(boundary.point)[1]" r="7" class="lab-dot-warn" />
        <text :x="P(boundary.point)[0] + 8" :y="P(boundary.point)[1] + 18">x₀</text>
      </template>
    </svg>

    <div v-if="type === 'support'" class="lab-controls">
      <label>Vị trí x₀ trên biên: {{ fmt(sParam) }}<input v-model.number="sParam" type="range" min="0" max="0.999" step="0.004" /></label>
      <label v-if="boundary.vertex !== undefined">Chọn pháp tuyến trong chùm: {{ fmt(fan) }}<input v-model.number="fan" type="range" min="0" max="1" step="0.02" /></label>
    </div>
    <div class="lab-readout" role="status">
      <template v-if="type === 'sets'">
        <p v-if="setsIntersect" class="is-bad">Hai tập giao nhau. Không có siêu phẳng nào đặt chúng về hai phía nghiêm ngặt, và nếu phần trong của chúng chồng lên nhau thì không có siêu phẳng phân tách nào cả.</p>
        <template v-else>
          <p>Cặp điểm gần nhất là c = {{ fmtPoint(closest.p) }} và d = {{ fmtPoint(closest.q) }}, cách nhau {{ fmt(closest.distance) }}.</p>
          <p>Đường tím vuông góc với d − c và đi qua trung điểm của đoạn [c, d]. Hàm affine aᵀx − b với a = d − c âm trên C và dương trên D.</p>
        </template>
      </template>
      <template v-else-if="type === 'data'">
        <p v-if="dataIntersect" class="is-bad">Hai bao lồi giao nhau, nên không đường thẳng nào tách được hai lớp: có một điểm nằm trong bao lồi của cả hai lớp.</p>
        <template v-else>
          <p>Hai bao lồi cách nhau {{ fmt(gap.distance) }}. Đường tím là trung trực của đoạn nối hai điểm gần nhất, và dải giữa hai đường nét đứt có bề rộng bằng đúng khoảng cách đó.</p>
          <p>Theo §8.6.1 của sách, đây là đường tách có lề lớn nhất: lề (một nửa bề rộng dải) bằng {{ fmt(gap.distance / 2) }}.</p>
        </template>
      </template>
      <template v-else>
        <p>x₀ = {{ fmtPoint(boundary.point) }} {{ boundary.vertex !== undefined ? 'là một đỉnh. Tại đỉnh có cả một chùm siêu phẳng tựa: mọi pháp tuyến nằm giữa hai pháp tuyến của hai cạnh kề đều dùng được.' : 'nằm trên một cạnh. Ở đây chỉ có đúng một siêu phẳng tựa, chứa cả cạnh đó.' }}</p>
        <p>Pháp tuyến a = {{ fmtPoint(normal) }}. Mọi đỉnh của đa giác thỏa aᵀx ≤ aᵀx₀: <span :class="supportOk ? 'is-good' : 'is-bad'">{{ supportOk ? 'đúng' : 'sai' }}</span>.</p>
      </template>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol v-if="type === 'sets'">
        <li>Kéo hai tập lại gần nhau. Đường phân tách xoay và dịch thế nào?</li>
        <li>Cho hai tập chạm nhau tại đúng một điểm. Lúc đó còn đường phân tách không, và nó có tách nghiêm ngặt không?</li>
      </ol>
      <ol v-else-if="type === 'data'">
        <li>Kéo một điểm vuông vào bên trong bao lồi của lớp tròn. Điều gì xảy ra?</li>
        <li>Những điểm nào thật sự quyết định vị trí đường tách? Thử kéo một điểm nằm xa đường tách.</li>
      </ol>
      <ol v-else>
        <li>Đưa x₀ tới giữa một cạnh, rồi tới một đỉnh. Số siêu phẳng tựa thay đổi thế nào?</li>
        <li>Ở một đỉnh, kéo thanh chọn pháp tuyến tới hai đầu. Hai đường tựa giới hạn trùng với gì?</li>
      </ol>
    </details>
  </figure>
</template>
