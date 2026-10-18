---
layout: page
title: "Ôn thi xử lý dữ liệu"
course: xu-ly-du-lieu
section: exam
outline: false
---

<script setup>
import { withBase } from 'vitepress'
import catalog from '../../../src/content/courses/xu-ly-du-lieu/exam/catalog.json'
</script>

<main class="course-overview course-shell exam-overview">
  <nav class="book-breadcrumbs" aria-label="Đường dẫn"><a :href="withBase('/xu-ly-du-lieu/')">Xử lý dữ liệu</a><span>/</span><span>Ôn thi</span></nav>
  <h1>Ôn thi</h1>
  <p>Luyện từng câu trắc nghiệm, đọc lý do đúng và sai của cả bốn lựa chọn, rồi tự trả lời các câu tự luận trước khi mở lời giải. Các bộ dưới đây giữ đủ câu trọng tâm, câu mở rộng và câu luyện regex trong tài liệu.</p>
  <section class="course-part-section">
    <header class="part-banner"><h2>Chọn bài học</h2></header>
    <div class="lecture-list">
      <article v-for="bank in catalog" :key="bank.lesson">
        <a class="lecture-row" :href="withBase(`/xu-ly-du-lieu/on-thi/bai-${bank.lesson}.html`)">
          <span class="lesson-number">{{ Number(bank.lesson) }}</span>
          <div class="lecture-list-copy"><h3>{{ bank.title }}</h3><p>{{ bank.quiz }} trắc nghiệm · {{ bank.essay }} tự luận</p></div>
        </a>
      </article>
    </div>
  </section>
  <p><a href="https://drive.google.com/drive/folders/1OXMdS5xJ57Shd4UrBnpuQz0sLjmyqrA8" target="_blank" rel="noopener">Tài liệu câu hỏi và đáp án</a></p>
</main>
