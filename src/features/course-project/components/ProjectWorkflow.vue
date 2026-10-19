<script setup>
defineProps({ variant: { type: String, default: 'pipeline' } })
const quality = [
  { title: 'Dừng bước bị ảnh hưởng', tone: 'stop', cause: 'Thiếu cột khóa hoặc không đọc được tệp bắt buộc.', action: 'Báo đầu vào cần sửa. Không xuất KPI dựa trên dữ liệu hỏng.', evidence: 'Tên tệp, snapshot, cột thiếu và trạng thái bước.' },
  { title: 'Tiếp tục và ghi cảnh báo', tone: 'warn', cause: 'Một giá trị rất cao hoặc thay đổi ở cột tùy chọn.', action: 'Giữ dữ liệu, gắn cờ để xem xét. Chưa tự coi đó là lỗi.', evidence: 'Số hàng, điều kiện phát hiện và kết quả so sánh.' },
  { title: 'Giữ dòng, giới hạn cách dùng', tone: 'keep', cause: 'Listing thiếu giá nhưng có mã hợp lệ.', action: 'Giữ cho KPI đếm. Không đưa vào mẫu số của KPI giá.', evidence: 'Số listing có giá, thiếu giá và mẫu số từng chỉ số.' }
]
</script>

<template>
  <figure class="workflow" :class="{ 'workflow-quality': variant === 'quality' }">
    <template v-if="variant === 'pipeline'">
      <figcaption>Đầu vào, hai nhánh xử lý và sản phẩm cuối</figcaption>
      <div class="workflow-config">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16M8 3v6M16 9v6M10 15v6" /></svg>
        <div><strong>Cấu hình điều khiển toàn bộ lần chạy</strong><p>Thành phố · Snapshot · Mã listing/review · Quy tắc QA · Tham số LLM</p></div>
      </div>
      <ol class="workflow-main" aria-label="Luồng chính từ dữ liệu thô đến kết quả">
        <li class="stage bronze">
          <span class="stage-label">01 · Bronze</span>
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h9l5 5v13H5zM14 3v6h5M8 13h8M8 17h8" /></svg>
          <strong>Giữ dữ liệu gốc</strong>
          <p>CSV nén và GeoJSON đúng ngày, kèm nguồn và checksum.</p>
          <code>data/raw/</code>
          <span class="stage-next" aria-hidden="true">→</span>
        </li>
        <li class="stage silver">
          <span class="stage-label">02 · Silver</span>
          <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 4v16M15 4v16M3 15h18" /></svg>
          <strong>Chuẩn hóa và gắn cờ</strong>
          <p>Lọc đúng mã. Kiểm khóa, kiểu dữ liệu và điều kiện dùng dòng.</p>
          <code>data/processed/</code>
          <span class="stage-next" aria-hidden="true">→</span>
        </li>
        <li class="stage gold">
          <span class="stage-label">03 · Gold</span>
          <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 3v18h17M8 17v-5M13 17V8M18 17V5" /></svg>
          <strong>Tính chỉ số và sinh hình</strong>
          <p>KPI theo khu vực, thời gian và LLM. Xuất hình và báo cáo.</p>
          <code>kpi_*.csv · figures/</code>
        </li>
      </ol>
      <div class="workflow-branches">
        <div class="review-branch">
          <span class="branch-origin">Từ review đã chọn ở Silver</span>
          <div class="branch-steps"><strong>Nhãn tay<br/>Baseline + LLM</strong><span aria-hidden="true">→</span><strong>Đánh giá<br/>trên cùng mẫu</strong><span aria-hidden="true">→</span><strong>KPI và hình LLM<br/>đưa vào Gold</strong></div>
          <p>Nhãn người là dữ liệu tham chiếu. Dự đoán lỗi và phần chưa có kết quả vẫn phải được báo rõ.</p>
        </div>
        <div class="exception-branch"><span class="branch-origin">Từ cờ QA ở Silver</span><strong>Dòng cần xem lại</strong><p>Giữ nguyên giá trị và lý do. Chỉ giới hạn những phân tích chịu ảnh hưởng.</p><code>reports/qa_report.csv</code></div>
      </div>
    </template>
    <template v-else>
      <figcaption>Khi phát hiện vấn đề, chương trình làm gì?</figcaption>
      <div class="quality-actions">
        <article v-for="item in quality" :key="item.title" :class="item.tone">
          <strong>{{ item.title }}</strong>
          <dl><div><dt>Phát hiện</dt><dd>{{ item.cause }}</dd></div><div><dt>Quyết định</dt><dd>{{ item.action }}</dd></div><div><dt>Ghi bằng chứng</dt><dd>{{ item.evidence }}</dd></div></dl>
        </article>
      </div>
      <p class="workflow-rule">Mỗi quy tắc phải chỉ rõ khi phát hiện vấn đề thì làm gì.</p>
    </template>
  </figure>
</template>

<style scoped>
.workflow { margin: var(--space-5) 0; padding: var(--space-5); background: var(--canvas); border: 1px solid var(--rule); border-radius: var(--radius-lg); font-family: var(--font-ui); color: var(--ink); }
figcaption { color: var(--ink); font-size: var(--fs-lead); line-height: 1.6; font-weight: 600; margin-bottom: var(--space-5); }
.workflow-config { display: flex; gap: var(--space-3); padding: var(--space-4); border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper); }
svg { width: 28px; height: 28px; flex: 0 0 28px; fill: none; stroke: currentColor; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
.workflow-config svg { color: var(--tim); }
strong { display: block; font-size: 16px; line-height: 1.65; }
p { margin: var(--space-2) 0 0; font-size: var(--fs-small); line-height: 1.75; color: var(--ink-2); }
.workflow-main { padding: 0; margin: var(--space-5) 0; list-style: none; display: grid; grid-template-columns: repeat(3,minmax(0,1fr)); gap: var(--space-5); }
.stage { position: relative; display: flex; flex-direction: column; align-items: flex-start; padding: var(--space-4); border: 1px solid currentColor; border-radius: var(--radius); margin: 0; min-width: 0; }
.bronze { color: var(--vang); background: var(--vang-soft); }.silver { color: var(--tim); background: var(--tim-soft); }.gold { color: var(--xanh); background: var(--xanh-soft); }
.stage strong { color: var(--ink); margin-top: var(--space-3); }
.stage-label { font-size: var(--fs-small); font-weight: 600; margin-bottom: var(--space-4); }
.stage code { margin-top: auto; padding-top: var(--space-4); background: transparent; color: var(--ink-2); font-size: 14px; overflow-wrap: anywhere; white-space: normal; }
.stage-next { position: absolute; left: calc(100% + 4px); top: 50%; color: var(--ink-3); font-size: 20px; line-height: 1; }
.workflow-branches { display: grid; grid-template-columns: 2fr 1fr; gap: var(--space-4); }
.review-branch,.exception-branch { padding: var(--space-4); border: 1px dashed var(--control); border-radius: var(--radius); background: var(--paper); min-width: 0; }
.branch-origin { display: block; color: var(--tim); font-size: var(--fs-small); margin-bottom: var(--space-3); }
.branch-steps { display: flex; align-items: center; gap: var(--space-3); }.branch-steps strong { font-size: var(--fs-small); }.branch-steps > span { color: var(--ink-3); }
.exception-branch code { display: block; margin-top: var(--space-3); font-size: 14px; overflow-wrap: anywhere; white-space: normal; background: transparent; }
.quality-actions { display: grid; grid-template-columns: repeat(3,minmax(0,1fr)); gap: var(--space-4); }
.quality-actions article { padding: var(--space-4); background: var(--paper); border-top: 3px solid var(--control); border-radius: var(--radius); }
.quality-actions .stop { border-color: var(--do); }.quality-actions .warn { border-color: var(--vang); }.quality-actions .keep { border-color: var(--xanh); }
dl { font-size: var(--fs-small); line-height: 1.75; margin: var(--space-4) 0 0; }dl > div + div { margin-top: var(--space-4); }dt { color: var(--ink-3); }dd { margin: var(--space-1) 0 0; }
.workflow-rule { padding-top: var(--space-4); margin-top: var(--space-5); border-top: 1px solid var(--rule); }
@media(max-width:1100px) { .workflow-main { grid-template-columns: 1fr; gap: var(--space-5); }.stage-next { left: 50%; top: calc(100% + 3px); transform: rotate(90deg); }.workflow-branches,.quality-actions { grid-template-columns: 1fr; }.stage { display: grid; grid-template-columns: 32px minmax(0,1fr); gap: 0 var(--space-3); }.stage-label { grid-column: 1/-1; margin-bottom: var(--space-3); }.stage svg { grid-row: 2/4; }.stage strong { margin-top: 0; }.stage code { grid-column: 2; padding-top: var(--space-3); } }
@media(max-width:600px) { .workflow { padding: var(--space-4); }.branch-steps { flex-direction: column; align-items: flex-start; }.branch-steps > span { transform: rotate(90deg); margin-left: var(--space-3); } }
</style>
