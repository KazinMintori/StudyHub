---
layout: page
title: "Đề thi"
course: xu-ly-du-lieu
section: exam
outline: false
---

<script setup>
import { withBase } from 'vitepress'
import catalog from '../../../src/content/courses/xu-ly-du-lieu/de-thi/catalog.json'
</script>

<main class="course-overview course-shell">
  <nav class="book-breadcrumbs" aria-label="Đường dẫn">
    <a :href="withBase('/xu-ly-du-lieu/')">Xử lý dữ liệu</a>
    <span>/</span><span>Đề thi</span>
  </nav>
  <header class="course-hero">
    <div class="course-hero-copy">
      <h1>Đề thi</h1>
      <p class="course-description">Bốn đề giữa kỳ chính thức và một đề luyện tập, có đầy đủ câu hỏi và lời giải. Làm trắc nghiệm để đối chiếu đáp án hoặc mở phần tự luận để xem từng bước giải.</p>
    </div>
  </header>
  <div class="course-meta">
    <span>5 đề · 130 câu</span>
    <a :href="withBase('/xu-ly-du-lieu/on-thi/')">Ngân hàng ôn thi</a>
    <a :href="withBase('/materials/xu-ly-du-lieu/de-thi/5-de-130-cau-loi-giai.pdf')" download>Tải PDF tổng hợp 5 đề</a>
  </div>
  <section class="course-part-section" aria-labelledby="exam-list-title">
    <header class="part-banner"><h2 id="exam-list-title">Danh sách đề</h2></header>
    <div class="lecture-list">
      <article v-for="exam in catalog" :key="exam.id">
        <a class="lecture-row" :href="withBase(`/xu-ly-du-lieu/de-thi/${exam.slug}.html`)">
          <span class="lesson-number">{{ exam.number }}</span>
          <div class="lecture-list-copy"><h3>{{ exam.title }}</h3><p>{{ exam.description }}</p></div>
        </a>
      </article>
    </div>
  </section>
</main>
