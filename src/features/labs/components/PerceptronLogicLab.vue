<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'
const gate = ref('AND')
const step = ref(0)
const points = [[0,0],[0,1],[1,0],[1,1]]
const trace = computed(() => {
  const frames = [{ weights: [0,0,0] }]
  let weights = [0,0,0]
  for (let epoch=1;epoch<=8;epoch++) {
    let errors=0
    for (const [x,y] of points) {
      const target=gate.value==='AND' ? x*y : Number(x!==y)
      const score=weights[0]+weights[1]*x+weights[2]*y
      const predicted=Number(score>=0)
      const error=target-predicted
      const next=weights.map((w,i)=>w+error*[1,x,y][i])
      frames.push({epoch,x,y,target,score,predicted,error,weights:next})
      weights=next
      if(error) errors++
    }
    if(!errors) break
  }
  return frames
})
const frame = computed(() => trace.value[Math.min(step.value, trace.value.length-1)])
const boundary = computed(() => {
  const [b,w1,w2] = frame.value.weights
  if (!w1 && !w2) return ''
  if (!w2) return 'M' + (45 - 220*b/w1) + ',10 V280'
  const y = x => 265 - 220*(-b-w1*x)/w2
  return 'M45,' + y(0) + ' L265,' + y(1)
})
watch(gate,()=>{step.value=0})
</script>

<template>
  <section class="math-lab" aria-label="Vết huấn luyện Perceptron">
    <label>Bảng chân trị <select v-model="gate"><option>AND</option><option>XOR</option></select></label>
    <p>Dự đoán 1 khi điểm lớn hơn hoặc bằng 0. Tốc độ học bằng 1.</p>
    <SimulationControls v-model="step" :max="trace.length-1" :reset-key="gate" />
    <svg viewBox="0 0 310 300" width="100%" role="img" aria-label="Bốn điểm dữ liệu và đường phân chia hiện tại">
      <defs><clipPath id="perceptron-plot"><rect x="10" y="10" width="280" height="280"/></clipPath></defs>
      <path d="M25 265H290M45 285V10" fill="none" stroke="currentColor" stroke-width="1"/>
      <g clip-path="url(#perceptron-plot)">
        <path v-if="boundary" :d="boundary" stroke="var(--vp-c-brand-1)" stroke-width="1.5"/>
      </g>
      <g v-for="([x,y],i) in points" :key="i">
        <circle :cx="45+220*x" :cy="265-220*y" r="13" fill="var(--vp-c-bg)" stroke="currentColor" stroke-width="1.4"/>
        <text :x="45+220*x" :y="270-220*y" text-anchor="middle" fill="currentColor" font-size="13">{{ gate==='AND'?x*y:Number(x!==y) }}</text>
      </g>
      <text x="286" y="282" fill="currentColor" font-size="13">x₁</text><text x="20" y="18" fill="currentColor" font-size="13">x₂</text>
    </svg>
    <div aria-live="polite">
      <template v-if="step">
        <p>Vòng {{ frame.epoch }} · Mẫu ({{ frame.x }}, {{ frame.y }})</p>
        <p>Điểm trước cập nhật {{ frame.score }} · Dự đoán {{ frame.predicted }} · Nhãn {{ frame.target }}</p>
        <p>Sai số {{ frame.error }}. Cộng sai số nhân với từng tọa độ của (1, {{ frame.x }}, {{ frame.y }}).</p>
      </template>
      <p>(b, w₁, w₂) = ({{ frame.weights.join(', ') }})</p>
    </div>
    <p>Vết chạy dừng sau một vòng không sai hoặc tối đa tám vòng.</p>
  </section>
</template>
