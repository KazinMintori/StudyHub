<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, fmt } from './svg-drag'

// Phương pháp chia đôi cho bài toán tựa lồi (ví dụ tự đặt của chủ đề 3, Lecture 02):
// đặt bộ phát x trong vùng X = [−1, 1.5] × [1, 3] để cực tiểu f(x) = ‖x − a‖/‖x − b‖, a = (0, 0), b = (4, 0).
// Trên nửa mặt phẳng x₁ ≤ 2, f tựa lồi và f(x) ≤ t ⇔ ‖x − a‖² − t²‖x − b‖² ≤ 0, một hình tròn Apollonius
// tâm (a − t²b)/(1 − t²), bán kính t‖a − b‖/(1 − t²). Bài toán khả thi "hình tròn chạm X" đúng khi và chỉ khi
// t ≥ p* = √5 − 2 (tính bằng Python), đạt tại x* = (2 − √5, 1).
const A = [0, 0], B = [4, 0]
const PSTAR = Math.sqrt(5) - 2, XSTAR = [2 - Math.sqrt(5), 1], EPS = 0.01
const X = [[-1, 1], [1.5, 1], [1.5, 3], [-1, 3]]
const l = ref(0), u = ref(1), history = ref([])
const manual = ref(false), tManual = ref(0.4)
const clip = `${useId()}-bis-clip`
const done = computed(() => u.value - l.value <= EPS)
const tNext = computed(() => (l.value + u.value) / 2)
const tShow = computed(() => (manual.value ? tManual.value : tNext.value))
const feasible = (t) => t >= PSTAR
const disc = (t) => {
  const k = 1 - t * t
  return { c: [(A[0] - t * t * B[0]) / k, (A[1] - t * t * B[1]) / k], r: (t * Math.hypot(B[0] - A[0], B[1] - A[1])) / k }
}
function step() {
  if (done.value) return
  const t = tNext.value, ok = feasible(t)
  history.value = [...history.value, { k: history.value.length + 1, t, ok }]
  if (ok) u.value = t
  else l.value = t
}
function runAll() { manual.value = false; while (!done.value) step() }
function reset() { l.value = 0; u.value = 1; history.value = []; manual.value = false }

const view = makeView({ x0: -3.5, x1: 4.5, y0: -2.5, y1: 3.5, width: 460, height: 345 })
const P = (p) => [view.sx(p[0]), view.sy(p[1])]
const poly = X.map(p => P(p).join(',')).join(' ')
const unit = view.sx(1) - view.sx(0)
const shown = computed(() => disc(tShow.value))
const lastRows = computed(() => history.value.slice(-4))
</script>

<template>
  <figure class="study-lab" aria-label="Phương pháp chia đôi cho bài toán tựa lồi về tỉ số khoảng cách">
    <p class="lab-title">Chia đôi khoảng chứa giá trị tối ưu</p>
    <p class="lab-lead">Cần đặt một bộ phát trong vùng tô tím X sao cho tỉ số giữa khoảng cách tới người dùng A và khoảng cách tới nguồn nhiễu B nhỏ nhất. Các điểm có tỉ số không quá t lấp đầy một hình tròn, và câu hỏi "hình tròn có chạm X không" là một bài toán khả thi lồi.</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" aria-label="Vùng X, hai điểm A và B, hình tròn Apollonius của tập mức dưới tại mức t và phần giao với X">
      <defs><clipPath :id="clip"><polygon :points="poly" /></clipPath></defs>
      <line v-for="t in [-3, -2, -1, 0, 1, 2, 3, 4]" :key="`gx${t}`" :x1="view.sx(t)" :x2="view.sx(t)" y1="0" :y2="view.height" class="lab-grid" />
      <line v-for="t in [-2, -1, 0, 1, 2, 3]" :key="`gy${t}`" x1="0" :x2="view.width" :y1="view.sy(t)" :y2="view.sy(t)" class="lab-grid" />
      <line :x1="view.sx(2)" :x2="view.sx(2)" y1="0" :y2="view.height" class="lab-guide" />
      <text :x="view.sx(2) + 4" y="16" class="lab-small">x₁ = 2</text>
      <polygon :points="poly" class="lab-region" />
      <circle :cx="P(shown.c)[0]" :cy="P(shown.c)[1]" :r="shown.r * unit" :class="feasible(tShow) ? 'lab-good-fill' : 'lab-bad-fill'" style="opacity: 0.35" />
      <circle :cx="P(shown.c)[0]" :cy="P(shown.c)[1]" :r="shown.r * unit" :clip-path="`url(#${clip})`" class="lab-good-fill" style="opacity: 0.9" />
      <circle :cx="P(A)[0]" :cy="P(A)[1]" r="6" class="lab-dot" />
      <text :x="P(A)[0] - 20" :y="P(A)[1] + 20">A</text>
      <circle :cx="P(B)[0]" :cy="P(B)[1]" r="6" class="lab-dot-bad" />
      <text :x="P(B)[0] + 10" :y="P(B)[1] + 20">B</text>
      <circle v-if="done && !manual" :cx="P(XSTAR)[0]" :cy="P(XSTAR)[1]" r="6" class="lab-dot-warn" />
      <text x="10" :y="view.height - 10" class="lab-small">t = {{ fmt(tShow, 4) }}</text>
    </svg>
    <p class="lab-legend"><span class="legend-accent">vùng được phép X</span><span class="legend-good">phần của X có tỉ số ≤ t</span><span class="legend-bad">hình tròn không chạm X</span><span class="legend-guide">ranh giới x₁ = 2</span></p>
    <div class="lab-buttons">
      <button type="button" :disabled="done" @click="manual = false; step()">Kiểm tra t = (l + u)/2</button>
      <button type="button" :disabled="done" @click="runAll">Chạy đến khi u − l ≤ 0.01</button>
      <button type="button" @click="reset">Làm lại</button>
    </div>
    <div class="lab-controls">
      <label class="lab-check"><input v-model="manual" type="checkbox" /> Tự chọn mức t để xem tập mức dưới</label>
      <label v-if="manual">t = {{ fmt(tManual, 3) }}<input v-model.number="tManual" type="range" min="0.02" max="0.9" step="0.002" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>Khoảng hiện tại [l, u] = [{{ fmt(l, 4) }}, {{ fmt(u, 4) }}], độ dài {{ fmt(u - l, 4) }}, sau {{ history.length }} lần kiểm tra.</p>
      <p>Hình tròn ở mức t = {{ fmt(tShow, 4) }} có tâm ({{ fmt(shown.c[0], 3) }}, 0) và bán kính {{ fmt(shown.r, 3) }}.</p>
      <p v-if="feasible(tShow)" class="is-good">Hình tròn chạm X: có vị trí khả thi với tỉ số không quá t, nên p* ≤ t.</p>
      <p v-else class="is-bad">Hình tròn không chạm X: mọi vị trí khả thi có tỉ số lớn hơn t, nên p* ≥ t.</p>
      <p v-for="r in lastRows" :key="r.k">Lần {{ r.k }}: t = {{ fmt(r.t, 4) }}, {{ r.ok ? 'khả thi, đặt u = t' : 'không khả thi, đặt l = t' }}.</p>
      <p v-if="done" class="is-accent">Dừng sau {{ history.length }} lần, đúng bằng ⌈log₂(1/0.01)⌉ = 7. Giá trị tối ưu p* = √5 − 2 ≈ 0.2361 nằm trong [{{ fmt(l, 4) }}, {{ fmt(u, 4) }}], đạt tại x* = (2 − √5, 1).</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Bấm kiểm tra từng lần. Mỗi lần, khoảng [l, u] mất một nửa. Hai lần đầu, t = 0.5 rồi t = 0.25, cho kết luận gì?</li>
        <li>Bật chế độ tự chọn t và kéo từ nhỏ đến lớn. Hình tròn lớn dần và dịch sang trái thế nào, và nó chạm X đầu tiên ở đâu?</li>
        <li>Ở mức vừa đủ để chạm, hình tròn tiếp xúc với cạnh dưới của X. Tâm và bán kính của nó khi đó là bao nhiêu?</li>
        <li>Kéo t gần 1. Vì sao hình tròn phình ra rất nhanh, và điều đó nói gì về hình dạng của hàm f ở xa A và B?</li>
      </ol>
    </details>
  </figure>
</template>
