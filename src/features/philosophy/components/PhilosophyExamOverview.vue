<script setup>
import { studyLink } from '../../../core/routing/links.js'
import { course } from '../../../content/courses/triet-hoc-mac-lenin/course.mjs'
import catalog from '../../../content/courses/triet-hoc-mac-lenin/exam/catalog.json'
import { chapterPracticeTests } from '../services/practice-tests.mjs'
</script>

<template>
  <section class="philosophy-exam-overview" aria-label="Chọn chương ôn thi">
    <p class="exam-intro">Chọn chương và bài để luyện trắc nghiệm. Khi chọn phương án, bạn sẽ thấy ngay kết quả và giải thích. Tiến độ được lưu riêng từng bài để bạn tiếp tục hoặc luyện lại các câu sai.</p>
    <div class="exam-bank-list">
      <article v-for="bank in catalog.banks" :key="bank.id" class="exam-bank">
        <p class="exam-bank-label">Chương {{ bank.chapter === 1 ? 'I' : 'II' }} · {{ chapterPracticeTests(bank).length }} bài · {{ bank.count }} câu hỏi</p>
        <h2>{{ course.lessons[bank.chapter - 1].title }}</h2>
        <p>{{ bank.chapter === 1 ? 'Nguồn gốc và vấn đề cơ bản của triết học, biện chứng và siêu hình, sự hình thành học thuyết và vai trò của triết học.' : 'Vật chất và ý thức, các nguyên lý, phạm trù, quy luật, thực tiễn, nhận thức và chân lý.' }}</p>
        <a class="exam-start" :href="studyLink(`/triet-hoc-mac-lenin/on-thi/${bank.id}`)">Chọn bài <span aria-hidden="true">→</span></a>
      </article>
    </div>
  </section>
</template>

<style scoped>
.exam-intro { color: var(--ink-2); line-height: 1.85; margin-bottom: var(--space-6); }
.exam-bank-list { display: grid; gap: var(--space-5); }
.exam-bank { border: 1px solid var(--rule); border-radius: var(--radius-lg); padding: var(--space-5); }
.exam-bank-label { color: var(--tim); font: 600 var(--fs-small)/1.6 var(--font-ui); margin: 0; }
.exam-bank h2 { margin: var(--space-3) 0 !important; padding: 0 !important; border: 0 !important; font-size: var(--fs-h2); line-height: 1.45; }
.exam-bank > p:not(.exam-bank-label) { color: var(--ink-2); }
.exam-start { display: inline-flex; gap: var(--space-4); align-items: center; min-height: 48px; color: var(--tim); font: 600 var(--fs-ui)/1.6 var(--font-ui); }
.exam-start:hover { text-decoration: underline; text-underline-offset: 4px; }
.exam-start:focus-visible { outline: 2px solid var(--tim); outline-offset: 4px; }
</style>
