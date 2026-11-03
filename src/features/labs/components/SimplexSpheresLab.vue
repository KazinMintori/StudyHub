<script setup>
import { computed, ref } from 'vue'
import { project3 } from '../services/foundation-geometry.mjs'

const tetra = ref(false)
const yaw = ref(30)
const triangle = Array.from({ length: 3 }, (_, i) => {
  const angle = -Math.PI/2 + i*2*Math.PI/3
  return [200+126*Math.cos(angle),158+126*Math.sin(angle)]
})
const vertices = [[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]]
const solid = computed(() => vertices.map(vertex => project3(vertex, {
  yaw: yaw.value, pitch: 22, scale: 126/Math.sqrt(3), origin: [200,158]
})))
const dots = computed(() => tetra.value ? solid.value : triangle)
const edges = computed(() => dots.value.flatMap((a,i) => dots.value.slice(i+1).map(b => [a,b])))
const inner = computed(() => tetra.value ? 42 : 63)
</script>

<template>
  <figure class="study-lab" aria-label="Đường tròn và mặt cầu cực trị của đơn hình đều">
    <figcaption class="lab-title">Từ tam giác đều sang tứ diện đều</figcaption>
    <p class="lab-lead">Đường tím là biên ngoài. Đường xanh là biên trong. Hai hình có chung tâm. Với tứ diện, hình tròn là hình chiếu trực giao của mặt cầu.</p>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="!tetra" @click="tetra=false">Tam giác đều R²</button>
      <button type="button" :aria-pressed="tetra" @click="tetra=true">Tứ diện đều R³</button>
      <button v-if="tetra" type="button" @click="yaw=(yaw+25)%360">Xoay tứ diện</button>
    </div>
    <svg viewBox="0 0 400 315" role="img" :aria-label="tetra ? 'Tứ diện đều và hình chiếu của hai mặt cầu' : 'Tam giác đều và hai đường tròn cực trị'">
      <circle cx="200" cy="158" r="126" class="outer-sphere" />
      <circle cx="200" cy="158" :r="inner" class="inner-sphere" />
      <line v-for="([a,b],i) in edges" :key="i" :x1="a[0]" :y1="a[1]" :x2="b[0]" :y2="b[1]" class="simplex-edge" />
      <circle v-for="([x,y],i) in dots" :key="'vertex'+i" :cx="x" :cy="y" r="4" class="lab-dot-accent" />
      <circle cx="200" cy="158" r="4" class="lab-dot-good" />
    </svg>
    <div class="lab-readout" role="status">
      <p v-if="tetra">Tứ diện đều trong ba chiều. Bán kính trong bằng một phần ba bán kính ngoài. Các điểm tiếp xúc là tâm của bốn mặt tam giác.</p>
      <p v-else>Tam giác đều trong hai chiều. Bán kính trong bằng một nửa bán kính ngoài. Đường tròn trong chạm trung điểm của ba cạnh.</p>
      <p>Tỉ số 1/n đạt dấu bằng trên đơn hình đều. Việc xoay hình chỉ thay góc quan sát.</p>
    </div>
  </figure>
</template>

<style scoped>
.outer-sphere { fill: none; stroke: var(--tim); stroke-width: 1.7; }
.inner-sphere { fill: var(--xanh-soft); stroke: var(--xanh); stroke-width: 1.7; }
.simplex-edge { stroke: var(--ink-2); stroke-width: 1.5; }
</style>
