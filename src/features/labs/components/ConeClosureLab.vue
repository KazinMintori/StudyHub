<script setup>
import {computed,ref} from 'vue'
import LabPointControls from './LabPointControls.vue'
import {makeView,createDragger,fmtPoint} from '../controllers/svg-drag.js'
const svg=ref(null),mode=ref('original'),point=ref([1,0])
const view=ref(makeView({x0:-1.2,x1:2.5,y0:-1.2,y1:2.5,width:400,height:340,pad:30}))
const P=p=>view.value.point(p)
const belongs=computed(()=>mode.value==='original'?(point.value.every(v=>v>1e-9)||point.value.every(v=>Math.abs(v)<1e-9)):point.value.every(v=>v>=-1e-9))
const drag=createDragger(svg,view,(_,p)=>{point.value=p},{step:.1,snap:.05})
const names={original:'K: Thiếu hai tia biên',dual:'K*: Có cả biên',twice:'K**: Bao đóng của K'}
</script>
<template>
 <figure class="study-lab" aria-label="Nón không đóng và tác dụng của phép đối ngẫu hai lần">
  <figcaption class="lab-title">Phép đối ngẫu hai lần lấp lại biên còn thiếu</figcaption>
  <p class="lab-lead">K gồm gốc và các điểm có cả hai tọa độ dương. Chọn K, K* hoặc K**, rồi kéo điểm thử. Tia nét đứt là biên bị loại, trừ gốc vẫn thuộc K.</p>
  <div class="lab-buttons" role="group" aria-label="Nón và hai lần đối ngẫu"><button v-for="(name,value) in names" :key="value" type="button" :aria-pressed="mode===value" @click="mode=value">{{name}}</button></div>
  <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Góc phần tư dương, hai tia biên và điểm thử" @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
   <rect :x="P([0,0])[0]" y="30" :width="370-P([0,0])[0]" :height="P([0,0])[1]-30" class="shade"/>
   <line x1="30" x2="370" :y1="P([0,0])[1]" :y2="P([0,0])[1]" class="lab-axis"/><line :x1="P([0,0])[0]" :x2="P([0,0])[0]" y1="30" y2="310" class="lab-axis"/>
   <line :x1="P([0,0])[0]" x2="370" :y1="P([0,0])[1]" :y2="P([0,0])[1]" :class="mode==='original'?'open-edge':'closed-edge'"/><line :x1="P([0,0])[0]" :x2="P([0,0])[0]" y1="30" :y2="P([0,0])[1]" :class="mode==='original'?'open-edge':'closed-edge'"/>
   <circle :cx="P([0,0])[0]" :cy="P([0,0])[1]" r="5" class="lab-dot"/><text :x="P([0,0])[0]-15" :y="P([0,0])[1]+25">O</text><text x="360" :y="P([0,0])[1]+25">x₁</text><text :x="P([0,0])[0]-30" y="27">x₂</text>
   <circle :cx="P(point)[0]" :cy="P(point)[1]" r="8" :class="belongs?'lab-dot-accent':'lab-dot-bad'"/><circle :cx="P(point)[0]" :cy="P(point)[1]" r="30" class="lab-handle hit" tabindex="0" role="slider" aria-label="Điểm thử trong nón và bao đóng" :aria-valuetext="fmtPoint(point,3)" @pointerdown="drag.start('point',$event)" @keydown="drag.key('point',point,$event)"/>
  </svg>
  <details class="lab-tasks"><summary>Điều chỉnh bằng nút thay cho kéo</summary><LabPointControls :svg="svg"/></details>
  <div class="lab-buttons"><button type="button" @click="point=[1,0]">Điểm trên tia biên</button><button type="button" @click="point=[1,.2]">Điểm trong K</button><button type="button" @click="point=[0,0]">Gốc thuộc cả ba nón</button></div>
  <div class="lab-readout" role="status"><p>Điểm {{fmtPoint(point)}} {{belongs?'thuộc':'không thuộc'}} {{mode==='original'?'K':mode==='dual'?'K*':'K**'}}.</p><p>K* = R²₊ và K** = R²₊. Các phép thử tích vô hướng không âm không phân biệt được một tia biên với các điểm trong K tiến sát tia đó. Vì vậy K** chứa thêm hai tia biên mà K còn thiếu.</p><p>K vẫn lồi. Tính lồi yêu cầu các đoạn nối nằm trong tập, còn tính đóng yêu cầu giữ cả giới hạn của dãy điểm.</p></div>
 </figure>
</template>
<style scoped>
svg text{font-size:20px;pointer-events:none}.shade{fill:var(--tim-soft)}.open-edge{stroke:var(--tim);stroke-width:2;stroke-dasharray:6 5}.closed-edge{stroke:var(--tim);stroke-width:2.4}.hit{fill:transparent!important;stroke:transparent}.hit:focus-visible{stroke:var(--vang)}svg :is(line,rect,circle:not(.hit)){pointer-events:none}
</style>
