<script setup>
import { computed, ref } from 'vue'
import { studyLink } from '../../../core/routing/links.js'
import catalog from '../../../content/courses/triet-hoc-mac-lenin/exam/papers/catalog.json'
import references from '../../../content/courses/triet-hoc-mac-lenin/exam/papers/references.json'
const institution = ref('')
const institutions = computed(() => [...new Set(references.items.map(item => item.institution))])
const filtered = computed(() => references.items.filter(item => !institution.value || item.institution === institution.value))
const kindLabels = { exam: 'Đề công bố', 'question-bank': 'Ngân hàng câu hỏi', 'review-guide': 'Hướng dẫn ôn tập', 'course-material': 'Học liệu' }
</script>

<template>
  <section class="philosophy-papers">
    <p class="papers-lead">Làm đề tổng hợp để tự đánh giá kiến thức cả ba chương, hoặc đọc các đề và tài liệu được công bố trên website trường.</p>
    <h2>Đề luyện trắc nghiệm</h2>
    <p>{{ catalog.papers.length }} đề tổng hợp, mỗi đề 59–60 câu. Chọn đáp án trong bài, nộp để xem điểm và lời giải. Các đề được biên soạn từ ngân hàng ôn tập của học phần.</p>
    <ol class="papers-grid"><li v-for="paper in catalog.papers" :key="paper.id"><a :href="studyLink(paper.path)"><strong>{{ paper.title }}</strong><span>{{ paper.count }} câu · Cả ba chương</span><span class="paper-start">Làm đề →</span></a></li></ol>
    <h2>Đề và tài liệu công bố</h2>
    <p>Các liên kết dưới đây dẫn tới tài liệu gốc. Mỗi mục ghi rõ loại tài liệu và đơn vị công bố để bạn tiện lựa chọn.</p>
    <label class="papers-filter">Trường hoặc đơn vị<select v-model="institution"><option value="">Tất cả đơn vị</option><option v-for="name in institutions" :key="name" :value="name">{{ name }}</option></select></label>
    <p class="papers-count" role="status">{{ filtered.length }} tài liệu</p>
    <div class="references-grid"><article v-for="item in filtered" :key="item.id" class="paper-reference"><p class="reference-label">{{ item.institution }}<span v-if="item.year"> · {{ item.year }}</span></p><h3><a :href="item.url" target="_blank" rel="noopener noreferrer">{{ item.title }}</a></h3><p class="reference-meta">{{ kindLabels[item.kind] }} · {{ item.format }}<span v-if="item.provenance === 'student-collection'"> · Bộ sưu tập sinh viên</span></p><p>{{ item.description }}</p><div class="reference-actions"><a :href="item.url" target="_blank" rel="noopener noreferrer">Mở trang tài liệu ↗</a><a v-if="item.fileUrl && item.fileUrl !== item.url" :href="item.fileUrl" target="_blank" rel="noopener noreferrer">Mở bản gốc ↗</a></div></article></div>
    <p v-if="!filtered.length">Chưa có tài liệu phù hợp với lựa chọn này.</p>
  </section>
</template>

<style scoped>
.philosophy-papers{font:var(--fs-ui)/1.85 var(--font-ui);min-width:0}.papers-lead{font-size:var(--fs-lead);color:var(--ink-2)}.philosophy-papers h2{margin-top:var(--space-7)}.papers-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:var(--space-4);list-style:none!important;padding:0!important;margin:var(--space-5) 0!important}.papers-grid li{margin:0;min-width:0}.papers-grid a{display:flex;flex-direction:column;gap:var(--space-2);min-height:140px;height:100%;padding:var(--space-4);border:1px solid var(--rule);border-radius:var(--radius-lg);text-decoration:none;box-sizing:border-box}.papers-grid strong{color:var(--ink);font-weight:600}.papers-grid span{font-size:var(--fs-small);color:var(--ink-2)}.papers-grid .paper-start{margin-top:auto;color:var(--tim)}.papers-grid a:hover{background:var(--canvas);border-color:var(--tim)}.philosophy-papers a:focus-visible,.papers-filter select:focus-visible{outline:2px solid var(--tim);outline-offset:3px}.papers-filter{display:flex;flex-direction:column;gap:var(--space-2);max-width:420px}.papers-filter select{min-height:44px;padding:var(--space-2) var(--space-3);border:1px solid var(--control);border-radius:var(--radius);background:var(--paper);color:var(--ink);font:inherit;max-width:100%}.papers-count,.reference-meta{font-size:var(--fs-small);color:var(--ink-3)}.references-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:var(--space-4)}.paper-reference{padding:var(--space-5);border:1px solid var(--rule);border-radius:var(--radius-lg);min-width:0;overflow-wrap:anywhere}.paper-reference h3{font:600 var(--fs-lead)/1.6 var(--font-ui);margin:var(--space-3) 0}.reference-label{color:var(--tim);font-size:var(--fs-small);margin:0}.reference-actions{display:flex;gap:var(--space-4);flex-wrap:wrap}.reference-actions a{display:inline-flex;min-height:44px;align-items:center}.paper-reference p{margin-block:var(--space-3)}
@media(max-width:800px){.papers-grid{grid-template-columns:repeat(2,minmax(0,1fr))}}@media(max-width:520px){.papers-grid,.references-grid{grid-template-columns:1fr}.papers-grid a{min-height:120px}.paper-reference{padding:var(--space-4)}}
</style>
