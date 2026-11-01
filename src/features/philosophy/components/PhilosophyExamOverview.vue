<script setup>
import { studyLink } from '../../../core/routing/links.js'
import { course } from '../../../content/courses/triet-hoc-mac-lenin/course.mjs'
import catalog from '../../../content/courses/triet-hoc-mac-lenin/exam/catalog.json'
import { chapterPracticeTests } from '../services/practice-tests.mjs'
const chapterLabels = ['I', 'II', 'III']
const descriptions = [
  'Nguồn gốc và vấn đề cơ bản của triết học, biện chứng và siêu hình, sự hình thành học thuyết và vai trò của triết học.',
  'Vật chất và ý thức, các nguyên lý, phạm trù, quy luật, thực tiễn, nhận thức và chân lý.',
  'Sản xuất vật chất, hình thái kinh tế – xã hội, giai cấp, dân tộc, nhà nước, ý thức xã hội và con người.',
]
</script>

<template>
  <section class="philosophy-exam-overview" aria-label="Chọn chương ôn thi">
    <p class="exam-intro">Ôn luyện từng chương bằng trắc nghiệm hoặc điền từ, rồi thử sức với đề tổng hợp. Tiến độ được lưu riêng từng bài để bạn tiếp tục phần đang làm.</p>
    <a class="exam-papers-link" :href="studyLink('/triet-hoc-mac-lenin/on-thi/de-thi/')"><span><strong>Đề thi trắc nghiệm</strong><span>Đề luyện tổng hợp và tài liệu công bố của các trường</span></span><span aria-hidden="true">→</span></a>
    <div class="exam-bank-list">
      <article v-for="bank in catalog.banks" :key="bank.id" class="exam-bank">
        <p class="exam-bank-label">Chương {{ chapterLabels[bank.chapter - 1] || bank.chapter }} · {{ chapterPracticeTests(bank).length }} bài · {{ bank.count }} câu hỏi</p>
        <h2>{{ course.lessons[bank.chapter - 1].title }}</h2>
        <p>{{ descriptions[bank.chapter - 1] }}</p>
        <div class="exam-bank-actions"><a class="exam-start" :href="studyLink(`/triet-hoc-mac-lenin/on-thi/${bank.id}`)">Trắc nghiệm <span aria-hidden="true">→</span></a><a class="exam-start" :href="studyLink(`/triet-hoc-mac-lenin/on-thi/${bank.id}/dien-tu`)">Điền từ <span aria-hidden="true">→</span></a></div>
      </article>
    </div>
  </section>
</template>

<style scoped>
.exam-intro { color: var(--ink-2); line-height: 1.85; margin-bottom: var(--space-6); }
.exam-papers-link { display:flex;align-items:center;justify-content:space-between;gap:var(--space-4);padding:var(--space-5);margin-bottom:var(--space-5);border:1px solid var(--tim);border-radius:var(--radius-lg);background:var(--tim-soft);text-decoration:none }
.exam-papers-link>span:first-child { display:grid;gap:var(--space-2) }.exam-papers-link strong{color:var(--ink);font:600 var(--fs-lead)/1.5 var(--font-ui)}.exam-papers-link span span{color:var(--ink-2);font-size:var(--fs-small)}.exam-bank-actions{display:flex;gap:var(--space-6);flex-wrap:wrap}
.exam-bank-list { display: grid; gap: var(--space-5); }
.exam-bank { border: 1px solid var(--rule); border-radius: var(--radius-lg); padding: var(--space-5); }
.exam-bank-label { color: var(--tim); font: 600 var(--fs-small)/1.6 var(--font-ui); margin: 0; }
.exam-bank h2 { margin: var(--space-3) 0 !important; padding: 0 !important; border: 0 !important; font-size: var(--fs-h2); line-height: 1.45; }
.exam-bank > p:not(.exam-bank-label) { color: var(--ink-2); }
.exam-start { display: inline-flex; gap: var(--space-4); align-items: center; min-height: 48px; color: var(--tim); font: 600 var(--fs-ui)/1.6 var(--font-ui); }
.exam-start:hover { text-decoration: underline; text-underline-offset: 4px; }
.exam-start:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; }
</style>
