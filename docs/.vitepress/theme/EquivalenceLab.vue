<script setup>
import { computed, ref } from 'vue'
import { makeView, fmt } from './svg-drag'

// Đổi biến σ = e^s trong âm log-likelihood Gauss (ví dụ tự đặt của chủ đề 1, Lecture 02):
// f(σ) = n log σ + S/(2σ²) không lồi khi σ > √(3S/n), còn g(s) = f(e^s) = ns + (S/2)e^{−2s} lồi.
// Hai đồ thị dùng chung trục tung vì f(e^s) = g(s) tại mọi điểm.
const n = 5
const S = ref(20)
const s = ref(0.3)
const showChord = ref(true)
const f = (sig) => n * Math.log(sig) + S.value / (2 * sig * sig)
const fpp = (sig) => -n / sig ** 2 + 3 * S.value / sig ** 4
const g = (u) => n * u + (S.value / 2) * Math.exp(-2 * u)
const gpp = (u) => 2 * S.value * Math.exp(-2 * u)
const SIG = [0.3, 8], U = [Math.log(0.3), Math.log(8)]

const sigStar = computed(() => Math.sqrt(S.value / n))
const bend = computed(() => Math.sqrt(3 * S.value / n))
const fStar = computed(() => f(sigStar.value))
const yr = computed(() => [fStar.value - 0.8, fStar.value + 6.5])
const left = computed(() => makeView({ x0: SIG[0], x1: SIG[1], y0: yr.value[0], y1: yr.value[1], width: 230, height: 230 }))
const right = computed(() => makeView({ x0: U[0], x1: U[1], y0: yr.value[0], y1: yr.value[1], width: 230, height: 230 }))
const clampY = (y) => Math.min(yr.value[1] + 1, Math.max(yr.value[0] - 1, y))
const curve = (v, fn, a, b) => Array.from({ length: 241 }, (_, i) => a + (i / 240) * (b - a)).map(t => `${v.sx(t)},${v.sy(clampY(fn(t)))}`).join(' ')
const leftCurve = computed(() => curve(left.value, f, SIG[0], SIG[1]))
const rightCurve = computed(() => curve(right.value, g, U[0], U[1]))
const sig = computed(() => Math.exp(s.value))
const value = computed(() => g(s.value))
// Dây cung giữa σ₁ = 1.9σ* và σ₂ = 2.8σ* (f lõm khi σ > √3·σ*): nằm dưới đồ thị f (f lõm ở đó), còn ảnh của nó theo s nằm trên đồ thị g.
const chord = computed(() => {
  const a = 1.9 * sigStar.value, b = 2.8 * sigStar.value
  if (b > SIG[1]) return null
  const mid = (a + b) / 2, chordMid = (f(a) + f(b)) / 2
  return { a, b, mid, below: chordMid < f(mid), ua: Math.log(a), ub: Math.log(b) }
})
</script>

<template>
  <figure class="study-lab" aria-label="Đổi biến sigma bằng e mũ s trong âm log-likelihood Gauss">
    <p class="lab-title">Cùng một hàm, hai cách đo trục hoành</p>
    <p class="lab-lead">Bên trái là âm log-likelihood theo độ lệch chuẩn σ, bên phải là cùng hàm đó theo s = log σ. Hai đồ thị cho cùng giá trị tại các điểm tương ứng, nhưng chỉ một đồ thị là hàm lồi.</p>
    <div class="lab-pair">
      <svg :viewBox="`0 0 ${left.width} ${left.height}`" role="img" aria-label="Đồ thị f theo sigma, vùng f lõm được tô">
        <rect v-if="bend < SIG[1]" :x="left.sx(bend)" y="0" :width="left.width - left.sx(bend)" :height="left.height" class="lab-bad-fill" style="opacity: 0.35; stroke: none" />
        <line v-for="t in [1, 2, 4, 6, 8]" :key="`a${t}`" :x1="left.sx(t)" :x2="left.sx(t)" y1="0" :y2="left.height" class="lab-grid" />
        <text v-for="t in [1, 2, 4, 6]" :key="`b${t}`" :x="left.sx(t) + 3" :y="left.height - 6" class="lab-small">{{ t }}</text>
        <text x="8" y="18" class="lab-small">theo σ</text>
        <polyline :points="leftCurve" class="lab-line" />
        <template v-if="showChord && chord">
          <line :x1="left.sx(chord.a)" :y1="left.sy(f(chord.a))" :x2="left.sx(chord.b)" :y2="left.sy(f(chord.b))" class="lab-warn" />
          <circle :cx="left.sx(chord.a)" :cy="left.sy(f(chord.a))" r="4" class="lab-dot-warn" /><circle :cx="left.sx(chord.b)" :cy="left.sy(f(chord.b))" r="4" class="lab-dot-warn" />
        </template>
        <circle :cx="left.sx(sigStar)" :cy="left.sy(fStar)" r="5" class="lab-dot-hollow" />
        <circle v-if="sig <= SIG[1] && sig >= SIG[0]" :cx="left.sx(sig)" :cy="left.sy(clampY(value))" r="7" class="lab-dot-accent" />
      </svg>
      <svg :viewBox="`0 0 ${right.width} ${right.height}`" role="img" aria-label="Đồ thị g theo s bằng log sigma, là một hàm lồi">
        <line v-for="t in [-1, 0, 1, 2]" :key="`c${t}`" :x1="right.sx(t)" :x2="right.sx(t)" y1="0" :y2="right.height" class="lab-grid" />
        <text v-for="t in [-1, 0, 1, 2]" :key="`d${t}`" :x="right.sx(t) + 3" :y="right.height - 6" class="lab-small">{{ t }}</text>
        <text x="8" y="18" class="lab-small">theo s = log σ</text>
        <polyline :points="rightCurve" class="lab-line" />
        <template v-if="showChord && chord">
          <line :x1="right.sx(chord.ua)" :y1="right.sy(g(chord.ua))" :x2="right.sx(chord.ub)" :y2="right.sy(g(chord.ub))" class="lab-warn" />
          <circle :cx="right.sx(chord.ua)" :cy="right.sy(g(chord.ua))" r="4" class="lab-dot-warn" /><circle :cx="right.sx(chord.ub)" :cy="right.sy(g(chord.ub))" r="4" class="lab-dot-warn" />
        </template>
        <circle :cx="right.sx(Math.log(sigStar))" :cy="right.sy(fStar)" r="5" class="lab-dot-hollow" />
        <circle :cx="right.sx(s)" :cy="right.sy(clampY(value))" r="7" class="lab-dot-accent" />
      </svg>
    </div>
    <p class="lab-legend"><span class="legend-accent">điểm đang chọn, σ = e^s</span><span class="legend-warn">dây cung giữa σ = 1.9σ* và σ = 2.8σ*</span><span class="legend-bad">vùng f lõm</span></p>
    <div class="lab-controls">
      <label>s = log σ = {{ fmt(s, 2) }}<input v-model.number="s" type="range" :min="U[0]" :max="U[1]" step="0.01" /></label>
      <label>Tổng bình phương độ lệch S = {{ S }}<input v-model.number="S" type="range" min="5" max="40" step="1" /></label>
      <label class="lab-check"><input v-model="showChord" type="checkbox" /> Vẽ dây cung</label>
    </div>
    <div class="lab-readout" role="status">
      <p>n = {{ n }}, σ = e^s = {{ fmt(sig, 3) }}. Giá trị hai bên bằng nhau: f(σ) = g(s) = <span class="is-accent">{{ fmt(value, 3) }}</span>.</p>
      <p>f″(σ) = {{ fmt(fpp(sig), 3) }}<template v-if="fpp(sig) < 0">, âm: tại đây f cong xuống</template>, còn g″(s) = {{ fmt(gpp(s), 3) }} &gt; 0.</p>
      <p>Hai nghiệm tương ứng nhau: σ* = √(S/n) = {{ fmt(sigStar, 3) }} và s* = log σ* = {{ fmt(Math.log(sigStar), 3) }}, cùng giá trị tối ưu {{ fmt(fStar, 3) }}. Hàm f lõm khi σ &gt; √(3S/n) ≈ {{ fmt(bend, 2) }}.</p>
      <p v-if="showChord && chord" :class="chord.below ? 'is-bad' : ''">Ở bên trái, trung điểm dây cung thấp hơn đồ thị, nên f không lồi. Cùng hai điểm ấy, dây cung bên phải nằm trên đồ thị g.</p>
    </div>
    <details class="lab-tasks">
      <summary>Gợi ý thao tác</summary>
      <ol>
        <li>Kéo s qua lại. Vì sao chấm tím ở hai bên luôn có cùng độ cao?</li>
        <li>Đặt σ vào vùng tô đỏ. Dấu của f″ cho biết gì, và g″ tại điểm tương ứng thì sao?</li>
        <li>Tăng S. Nghiệm σ* và ranh giới của vùng lõm dịch chuyển thế nào, và tỉ số giữa chúng có đổi không?</li>
        <li>Bật dây cung. Hai đầu dây cung bên phải là ảnh của hai đầu dây cung bên trái. Phép đổi biến đã làm gì với độ cong?</li>
      </ol>
    </details>
  </figure>
</template>
