---
layout: page
title: "Đề 5"
course: xu-ly-du-lieu
section: exam
outline: false
sidebar: false
---

<script setup>
import ExamPractice from '../../../src/features/exam/components/ExamPractice.vue'
import bank from '../../../src/content/courses/xu-ly-du-lieu/de-thi/de-5.json'
</script>

<ExamPractice :bank="bank" course-link="/xu-ly-du-lieu/de-thi/" back-link-text="← Danh sách đề thi" session-key="studyhub_paper_de_5" />
