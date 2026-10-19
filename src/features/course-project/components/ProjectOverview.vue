<script setup>
defineProps({ variant: { type: String, default: 'brief' } })
const facts = [
  ['4', 'Mốc dữ liệu', 'Đúng thành phố được giao'],
  ['5–8', 'Chỉ số KPI', 'Có khu vực, thời gian và LLM'],
  ['≥100', 'Nhãn tay', 'Đối chiếu cả LLM và baseline'],
  ['≤10', 'Trang báo cáo', 'Kèm mã nguồn chạy lại được']
]
const outputs = [
  ['01', 'Tải đúng dữ liệu', 'Script tải, ngày snapshot và danh sách mã.'],
  ['02', 'Giải thích cách làm sạch', 'Quy tắc QA, cờ lỗi và tác động trước/sau.'],
  ['03', 'Trả lời bằng chỉ số', 'KPI có công thức, đơn vị và mẫu số.'],
  ['04', 'Đo chất lượng LLM', 'Nhãn tay, baseline, accuracy/F1 và lỗi.'],
  ['05', 'Cho thấy kết quả', 'Hình về không gian, thời gian và review.'],
  ['06', 'Bàn giao để chạy lại', 'README, môi trường, một lệnh và tag final.']
]
const rubric = [
  ['Thu thập dữ liệu', 10, 'Đúng phạm vi, ngày chụp và nơi lưu.'],
  ['Làm sạch và chuẩn hóa', 20, 'Gắn cờ, xử lý có lý do và báo tác động.'],
  ['Bảng tổng hợp và KPI', 20, 'Công thức, đơn vị, snapshot và định dạng rõ.'],
  ['Trực quan hóa', 20, 'Ít nhất 5 hình, đủ nhãn và thông điệp.'],
  ['So sánh và diễn giải', 10, 'Có phát hiện, giới hạn và ảnh hưởng QA.'],
  ['Báo cáo và tái lập', 10, 'Tài liệu, seed, môi trường và chạy lại.'],
  ['Trình bày và vấn đáp', 10, 'Giải thích và bảo vệ lựa chọn kỹ thuật.']
]
</script>

<template>
  <div v-if="variant === 'brief'" class="project-overview">
    <dl class="project-facts">
      <div v-for="[value, label, note] in facts" :key="label">
        <dt>{{ label }}</dt><dd>{{ value }}</dd><p>{{ note }}</p>
      </div>
    </dl>
    <ol class="project-outputs" aria-label="Sáu phần sản phẩm cần có">
      <li v-for="[number, title, description] in outputs" :key="number">
        <span class="output-number" aria-hidden="true">{{ number }}</span>
        <div><strong>{{ title }}</strong><p>{{ description }}</p></div>
      </li>
    </ol>
  </div>
  <figure v-else class="project-rubric">
    <figcaption>Phân bố điểm trong bảng tiêu chí được cung cấp</figcaption>
    <ol>
      <li v-for="[name, points, description] in rubric" :key="name">
        <div class="rubric-label"><strong>{{ name }}</strong><span>{{ points }} điểm</span></div>
        <div class="rubric-track" aria-hidden="true"><span :style="{ width: `${points}%` }" /></div>
        <p>{{ description }}</p>
      </li>
    </ol>
    <p class="rubric-total">Tổng cơ bản 100 điểm. Phần nâng cao có thể được cộng tối đa 20 điểm theo bảng này.</p>
  </figure>
</template>

<style scoped>
.project-overview,.project-rubric { font-family: var(--font-ui); }
.project-facts { display: grid; grid-template-columns: repeat(4,minmax(0,1fr)); gap: var(--space-3); margin: var(--space-5) 0; }
.project-facts > div { display: flex; flex-direction: column; padding: var(--space-4); background: var(--tim-soft); border-radius: var(--radius-lg); min-width: 0; }
.project-facts dt { font-size: var(--fs-small); font-weight: 600; }
.project-facts dd { order: -1; margin: 0 0 var(--space-2); color: var(--tim); font-size: 30px; line-height: 1.2; font-weight: 700; }
.project-facts p { font-size: var(--fs-small); line-height: 1.6; margin: var(--space-2) 0 0; color: var(--ink-2); }
.project-outputs { display: grid; grid-template-columns: repeat(2,minmax(0,1fr)); gap: var(--space-3); padding: 0; list-style: none; }
.project-outputs li { display: flex; align-items: flex-start; gap: var(--space-3); padding: var(--space-4); margin: 0; border: 1px solid var(--rule); border-radius: var(--radius); }
.output-number { color: var(--tim); font-size: var(--fs-small); line-height: 1.8; }
.project-outputs strong { font-size: var(--fs-ui); }
.project-outputs p { font-size: var(--fs-small); line-height: 1.7; margin: var(--space-2) 0 0; color: var(--ink-2); }
.project-rubric { padding: var(--space-5); background: var(--canvas); border: 1px solid var(--rule); border-radius: var(--radius-lg); }
.project-rubric figcaption { font-size: var(--fs-lead); color: var(--ink); font-weight: 600; margin-bottom: var(--space-5); }
.project-rubric ol { display: grid; gap: var(--space-4); list-style: none; margin: 0; padding: 0; }
.project-rubric li { margin: 0; }
.rubric-label { display: flex; justify-content: space-between; gap: var(--space-3); font-size: var(--fs-ui); }
.rubric-label span { white-space: nowrap; color: var(--tim); }
.rubric-track { height: 5px; border-radius: var(--radius-sm); background: var(--rule); margin-top: var(--space-2); }
.rubric-track span { display: block; height: 100%; background: var(--tim); border-radius: inherit; }
.project-rubric li p { margin: var(--space-2) 0 0; color: var(--ink-2); font-size: var(--fs-small); line-height: 1.65; }
.rubric-total { font-size: var(--fs-small); line-height: 1.7; border-top: 1px solid var(--rule); padding-top: var(--space-4); margin-bottom: 0; }
@media(max-width:600px) { .project-facts { grid-template-columns: repeat(2,minmax(0,1fr)); }.project-outputs { grid-template-columns: 1fr; }.project-rubric { padding: var(--space-4); } }
</style>
