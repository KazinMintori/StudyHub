<script setup>
import { computed, ref } from 'vue'
import LabPointControls from './LabPointControls.vue'
import { createDragger, fmt, fmtPoint, makeView } from '../controllers/svg-drag.js'

const svg=ref(null),theta=ref([1,0.5]),batch=ref(1),replacement=ref(true),cursor=ref(0),lastLoss=ref(null)
const sites=[[-1,0],[0,2],[2,1],[3,-1]],mean=[1,0.5]
const view=ref(makeView({x0:-2.3,x1:4.2,y0:-2.2,y1:3.2,width:400,height:340,pad:36}))
const gradientView=makeView({x0:-5.5,x1:5.5,y0:-5,y1:5,width:400,height:340,pad:36})
const distribution=computed(()=>{
  const samples=[]
  function enumerate(indices,start=0){
    if(indices.length===batch.value){
      samples.push([0,1].map(j=>indices.reduce((sum,i)=>sum+sites[i][j],0)/batch.value))
      return
    }
    for(let i=start;i<sites.length;i++)enumerate([...indices,i],replacement.value?0:i+1)
  }
  enumerate([])
  const groups=new Map()
  for(const point of samples){
    const key=point.join(',')
    const row=groups.get(key)||{point,count:0}
    row.count++;groups.set(key,row)
  }
  return {samples,points:[...groups.values()]}
})
const full=computed(()=>theta.value.map((x,i)=>x-mean[i]))
const selected=computed(()=>theta.value.map((x,i)=>x-distribution.value.samples[cursor.value%distribution.value.samples.length][i]))
const varianceFactor=computed(()=>replacement.value?1/batch.value:(4-batch.value)/(3*batch.value))
const totalVariance=computed(()=>3.75*varianceFactor.value)
const loss=p=>sites.reduce((sum,a)=>sum+((p[0]-a[0])**2+(p[1]-a[1])**2)/2,0)/sites.length
const drag=createDragger(svg,view,(_,point)=>{theta.value=[Math.max(-1.5,Math.min(3.5,point[0])),Math.max(-2,Math.min(2.5,point[1]))];lastLoss.value=null},{step:0.1})
function update(){lastLoss.value=loss(theta.value);theta.value=theta.value.map((x,i)=>x-0.1*selected.value[i])}
function chooseBatch(value){batch.value=value;cursor.value=0}
function chooseSampling(value){replacement.value=value;cursor.value=0}
const cross=(v,p)=>`M ${v.sx(p[0])-6} ${v.sy(p[1])} h 12 M ${v.sx(p[0])} ${v.sy(p[1])-6} v 12`
</script>

<template>
  <figure class="study-lab" aria-label="Phân phối gradient lô nhỏ trong không gian hai chiều">
    <figcaption class="lab-title">Ở nghiệm của toàn bộ dữ liệu, gradient từng lô vẫn có thể khác 0</figcaption>
    <p class="lab-lead">Bốn mẫu có mất mát bằng nửa bình phương khoảng cách tới bốn ô vuông. Kéo tham số θ màu vàng ở hình trái. Dấu cộng xanh là trung bình dữ liệu. Hình phải liệt kê mọi gradient lô nhỏ có thể có, chấm lớn hơn ứng với xác suất lớn hơn.</p>
    <div class="lab-pair">
      <svg ref="svg" viewBox="0 0 400 340" role="group" aria-label="Kéo vector tham số theta trong R2"
        @pointermove="drag.move" @pointerup="drag.end" @pointercancel="drag.end" @lostpointercapture="drag.end">
        <line x1="36" x2="364" :y1="view.sy(0)" :y2="view.sy(0)" class="lab-axis" />
        <line :x1="view.sx(0)" :x2="view.sx(0)" y1="36" y2="304" class="lab-axis" />
        <rect v-for="(p,i) in sites" :key="i" :x="view.sx(p[0])-5" :y="view.sy(p[1])-5" width="10" height="10" class="batch-site"><title>Mẫu {{i+1}} tại {{fmtPoint(p)}}</title></rect>
        <line :x1="view.sx(mean[0])" :y1="view.sy(mean[1])" :x2="view.sx(theta[0])" :y2="view.sy(theta[1])" class="batch-full-line" />
        <path :d="cross(view,mean)" class="batch-cross" />
        <circle :cx="view.sx(theta[0])" :cy="view.sy(theta[1])" r="7" class="lab-dot-warn" />
        <circle :cx="view.sx(theta[0])" :cy="view.sy(theta[1])" r="32" class="lab-handle batch-hit" tabindex="0" role="slider"
          aria-label="Vector tham số theta" :aria-valuetext="fmtPoint(theta)" @pointerdown="drag.start('theta',$event)" @keydown="drag.key('theta',theta,$event)" />
        <text x="9" y="25">θ₂</text><text x="365" y="328">θ₁</text>
      </svg>
      <svg viewBox="0 0 400 340" role="img" aria-label="Các gradient lô nhỏ và gradient toàn phần">
        <line x1="36" x2="364" :y1="gradientView.sy(0)" :y2="gradientView.sy(0)" class="lab-axis" />
        <line :x1="gradientView.sx(0)" :x2="gradientView.sx(0)" y1="36" y2="304" class="lab-axis" />
        <circle v-for="(row,i) in distribution.points" :key="i"
          :cx="gradientView.sx(theta[0]-row.point[0])" :cy="gradientView.sy(theta[1]-row.point[1])"
          :r="1+2.2*Math.sqrt(row.count/Math.max(...distribution.points.map(p=>p.count)))" class="batch-possible" />
        <circle :cx="gradientView.sx(selected[0])" :cy="gradientView.sy(selected[1])" r="6" class="batch-selected" />
        <path :d="cross(gradientView,full)" class="batch-cross" />
        <text x="9" y="25">g₂</text><text x="365" y="328">g₁</text>
      </svg>
    </div>
    <details class="lab-tasks"><summary>Điều chỉnh θ bằng nút</summary><LabPointControls :svg="svg" /></details>
    <div class="lab-buttons">
      <button type="button" :aria-pressed="replacement" @click="chooseSampling(true)">Có hoàn lại</button>
      <button type="button" :aria-pressed="!replacement" @click="chooseSampling(false)">Không hoàn lại</button>
      <button v-for="size in [1,2,4]" :key="size" type="button" :aria-pressed="batch===size" @click="chooseBatch(size)">B = {{size}}</button>
      <button type="button" @click="theta=[1,0.5]">Đưa θ về nghiệm</button>
      <button type="button" @click="theta=[0,0]">Đặt θ tại gốc</button>
      <button type="button" @click="cursor=(cursor+1)%distribution.samples.length">Lô tiếp theo trong danh sách</button>
      <button type="button" @click="update">Cập nhật theo lô đang chọn</button>
    </div>
    <div class="lab-readout" role="status">
      <p>θ = {{fmtPoint(theta)}}. Gradient toàn phần (dấu cộng xanh) = {{fmtPoint(full)}}. Gradient lô đang chọn (vòng vàng) = {{fmtPoint(selected)}}.</p>
      <p>B = {{batch}}, {{replacement?'lấy độc lập có hoàn lại':'chọn đều một tập con không hoàn lại'}}. Có {{distribution.samples.length}} kết quả lấy mẫu đồng xác suất, gồm {{distribution.points.length}} giá trị gradient khác nhau.</p>
      <p>Tổng phương sai hai tọa độ = {{fmt(totalVariance,4)}}. Sai số RMS của gradient = {{fmt(Math.sqrt(totalVariance),4)}}.</p>
      <p>Mất mát toàn phần = {{fmt(loss(theta),5)}}.<template v-if="lastLoss!==null"> Trước bước vừa dùng η = 0,1, mất mát là {{fmt(lastLoss,5)}}.</template></p>
      <p v-if="!replacement&&batch===4">Lô chứa toàn bộ dữ liệu nên nhiễu bằng 0.</p>
      <p v-else>Trung bình của toàn bộ phân phối bằng gradient toàn phần. Lô được duyệt theo danh sách để tái lập, không phải một phép rút ngẫu nhiên mới.</p>
    </div>
  </figure>
</template>

<style scoped>
.batch-site { fill: var(--paper); stroke: var(--ink-3); stroke-width: 1.5; }
.batch-full-line { stroke: var(--xanh); stroke-width: 1.5; }
.batch-cross { fill: none; stroke: var(--xanh); stroke-width: 2; }
.batch-possible { fill: var(--ink-3); }
.batch-selected { fill: none; stroke: var(--vang); stroke-width: 1.8; }
.batch-hit { fill: transparent !important; stroke: transparent; }
.batch-hit:focus-visible { stroke: var(--vang); }
svg text { font-size: 19px; pointer-events: none; }
</style>
