---
layout: page
title: "Ôn thi bài 3"
course: xu-ly-du-lieu
section: exam
outline: false
sidebar: false
---

<script setup>
import ExamPractice from '../../../src/features/exam/components/ExamPractice.vue'
import bank from '../../../src/content/courses/xu-ly-du-lieu/exam/bai-03.json'
</script>

<ExamPractice :bank="bank" />
