<script setup>
import { computed } from 'vue'
import ExamPractice from '../../exam/components/ExamPractice.vue'
import { toExamBank } from '../services/exam-bank.mjs'
import {
  answerQuizQuestion, createQuizSession, loadQuizSession, saveQuizSession, setQuizQuestion,
} from '../services/quiz-session.mjs'

const props = defineProps({ bank: { type: Object, required: true } })
const examBank = computed(() => toExamBank(props.bank))
let session = null

function restore() {
  const previous = loadQuizSession(props.bank)
  // The shared renderer shows the complete test; preserve every existing selection.
  session = {
    ...previous,
    attempt: {
      ...createQuizSession(props.bank).attempt,
      responses: previous.attempt.responses,
      currentId: previous.attempt.currentId,
    },
  }
  return { answers: session.attempt.responses, currentQuestionId: session.attempt.currentId }
}

function record({ questionId, selectedKey }) {
  if (!session) restore()
  session = answerQuizQuestion(props.bank, session, questionId, selectedKey)
  saveQuizSession(props.bank, session)
}

function navigate(questionId) {
  if (!session) restore()
  session = setQuizQuestion(props.bank, session, questionId)
  saveQuizSession(props.bank, session)
}
</script>

<template>
  <ExamPractice :key="bank.id" :bank="examBank"
    :course-link="`/triet-hoc-mac-lenin/on-thi/${bank.parentBankId}.html`"
    :session-key="`studyhub_exam_session_triet-hoc-mac-lenin_${bank.id}`"
    :restore-state="restore" @answer="record" @navigate="navigate" />
</template>
