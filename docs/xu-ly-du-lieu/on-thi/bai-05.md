---
layout: page
title: "Ôn thi bài 5"
course: xu-ly-du-lieu
section: exam
outline: false
sidebar: false
---

<script setup>
import ExamPractice from '../../../src/features/exam/components/ExamPractice.vue'
import bank from '../../../src/content/courses/xu-ly-du-lieu/exam/bai-05.json'
</script>

<ExamPractice :bank="bank" />
