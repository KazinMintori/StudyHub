<script setup>
import { computed, ref, useId } from 'vue'
import { makeView, fmt } from './svg-drag'

// Hàm lồi bằng supremum của các hàm affine nằm dưới nó. Lấy k tiếp tuyến tại k điểm cách đều,
// max của chúng là một hàm tuyến tính từng khúc, lồi, nằm dưới f và tiến tới f khi k tăng.
const catalog = {
  sq: { label: 'x²', f: x => x * x, df: x => 2 * x, y: [-1, 6] },
  exp: { label: 'eˣ', f: x => Math.exp(x), df: x => Math.exp(x), y: [-1, 8] },
  abs: { label: '|x| + 0.3x²', f: x => Math.abs(x) + 0.3 * x * x, df: x => Math.sign(x) + 0.6 * x, y: [-1, 5] },
  lse: { label: 'log(1 + eˣ)', f: x => Math.log1p(Math.exp(x)), df: x => 1 / (1 + Math.exp(-x)), y: [-0.5, 3] }
}
const choice = ref('sq')
const k = ref(3)
const fn = computed(() => catalog[choice.value])
const clip = `${useId()}-env-clip`
const view = computed(() => makeView({ x0: -2.5, x1: 2.5, y0: fn.value.y[0], y1: fn.value.y[1], width: 440, height: 280 }))
const P = (x, y) => [view.value.sx(x), view.value.sy(y)]
const points = computed(() => (k.value === 1 ? [0] : Array.from({ length: k.value }, (_, i) => -2 + (4 * i) / (k.value - 1))))
const lines = computed(() => points.value.map(p => ({ p, a: fn.value.df(p), b: fn.value.f(p) - fn.value.df(p) * p })))
const env = x => Math.max(...lines.value.map(l => l.a * x + l.b))
const xs = Array.from({ length: 401 }, (_, i) => -2.5 + (5 * i) / 400)
const curve = computed(() => xs.map(x => P(x, fn.value.f(x)).join(',')).join(' '))
const envelope = computed(() => xs.map(x => P(x, env(x)).join(',')).join(' '))
const maxGap = computed(() => Math.max(...xs.filter(x => x >= -2 && x <= 2).map(x => fn.value.f(x) - env(x))))
</script>

<template>
  <figure class="study-lab" aria-label="Hàm lồi như supremum của các tiếp tuyến">
    <p class="lab-title">Hàm lồi là bao trên của các tiếp tuyến</p>
    <svg :viewBox="`0 0 ${view.width} ${view.height}`" role="img" :aria-label="`Đồ thị ${fn.label} và max của ${k} tiếp tuyến`">
      <defs><clipPath :id="clip"><rect x="0" y="0" :width="view.width" :height="view.height" /></clipPath></defs>
      <g :clip-path="`url(#${clip})`">
        <line x1="0" :x2="view.width" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" /><line :x1="view.sx(0)" :x2="view.sx(0)" y1="0" :y2="view.height" class="lab-axis" />
        <line v-for="(l, i) in lines" :key="`l${i}`" :x1="P(-2.5, l.a * -2.5 + l.b)[0]" :y1="P(-2.5, l.a * -2.5 + l.b)[1]" :x2="P(2.5, l.a * 2.5 + l.b)[0]" :y2="P(2.5, l.a * 2.5 + l.b)[1]" class="lab-guide" />
        <polyline :points="curve" class="lab-line" style="stroke-width: 2.5" />
        <polyline :points="envelope" class="lab-accent" style="stroke-width: 3" />
        <circle v-for="(l, i) in lines" :key="`p${i}`" :cx="P(l.p, l.b + l.a * l.p)[0]" :cy="P(l.p, l.b + l.a * l.p)[1]" r="4.5" class="lab-dot-warn" />
      </g>
    </svg>
    <p class="lab-legend"><span>đồ thị của f</span><span class="legend-guide">các tiếp tuyến</span><span class="legend-accent">max của các tiếp tuyến</span></p>
    <div class="lab-controls">
      <label>Hàm f(x) = <select v-model="choice"><option v-for="(item, key) in catalog" :key="key" :value="key">{{ item.label }}</option></select></label>
      <label>Số tiếp tuyến k = {{ k }}<input v-model.number="k" type="range" min="1" max="12" step="1" /></label>
    </div>
    <div class="lab-readout" role="status">
      <p>Max của {{ k }} tiếp tuyến là một hàm tuyến tính từng khúc, lồi, và nằm dưới f. Trên đoạn [−2, 2], f vượt nó nhiều nhất {{ fmt(maxGap, 3) }}.</p>
      <p>Mỗi tiếp tuyến là một cận dưới toàn cục của f, nên max của chúng cũng vậy. Khi dùng mọi tiếp tuyến, max của chúng trùng với f.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Với x², tăng k từ 2 lên 12. Sai số lớn nhất giảm theo quy luật nào khi k tăng gấp đôi?</li>
        <li>Với |x| + 0.3x², tiếp tuyến tại 0 lấy độ dốc nào? Vì sao điểm gãy không cản trở cách xây dựng này?</li>
        <li>Đây cũng là cách một số thuật toán xây mô hình xấp xỉ cho hàm lồi: mỗi lần tính gradient lại thêm một tiếp tuyến. Mô hình đó lệch về phía nào so với f?</li>
      </ol>
    </details>
  </figure>
</template>
