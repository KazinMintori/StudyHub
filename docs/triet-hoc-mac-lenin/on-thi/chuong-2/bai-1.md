---
title: "Bài kiểm tra 1"
course: triet-hoc-mac-lenin
section: exam
quiz: chuong-2
quizChapter: 2
quizTest: 1
outline: false
prev: false
next: false
---

<script setup>
import PhilosophyQuiz from '../../../../src/features/philosophy/components/PhilosophyQuiz.vue'
import PhilosophyPracticeLinks from '../../../../src/features/philosophy/components/PhilosophyPracticeLinks.vue'
import bank from '../../../../src/content/courses/triet-hoc-mac-lenin/exam/practice/chuong-2-bai-1.json'
</script>

<PhilosophyQuiz :bank="bank" />

<PhilosophyPracticeLinks chapter-id="chuong-2" :test-number="1" />
