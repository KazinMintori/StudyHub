---
title: "Bài kiểm tra 5"
course: triet-hoc-mac-lenin
section: exam
quiz: chuong-1
quizChapter: 1
quizTest: 5
outline: false
prev: false
next: false
---

<script setup>
import PhilosophyQuiz from '../../../../src/features/philosophy/components/PhilosophyQuiz.vue'
import PhilosophyPracticeLinks from '../../../../src/features/philosophy/components/PhilosophyPracticeLinks.vue'
import bank from '../../../../src/content/courses/triet-hoc-mac-lenin/exam/practice/chuong-1-bai-5.json'
</script>

<PhilosophyQuiz :bank="bank" />

<PhilosophyPracticeLinks chapter-id="chuong-1" :test-number="5" />
