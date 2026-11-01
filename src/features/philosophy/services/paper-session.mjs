const keys = ['A', 'B', 'C', 'D']
const questionsOf = bank => bank.questions || []
export const paperStorageKey = bank => `studyhub:philosophy:paper:v1:${bank.id}`
export function createPaperSession(bank) {
  return { version: 1, bankId: bank.id, index: 0, answers: {}, submitted: false }
}
export function restorePaperSession(bank, raw) {
  const fresh = createPaperSession(bank)
  try {
    const value = typeof raw === 'string' ? JSON.parse(raw) : raw
    if (value?.version !== 1 || value.bankId !== bank.id) return fresh
    fresh.index = Number.isInteger(value.index) ? Math.max(0, Math.min(value.index, questionsOf(bank).length - 1)) : 0
    fresh.submitted = value.submitted === true
    for (const question of questionsOf(bank)) {
      const key = Object.hasOwn(value.answers || {}, question.id) && value.answers[question.id]
      if (keys.includes(key)) fresh.answers[question.id] = key
    }
    return fresh
  } catch { return fresh }
}
export function answerPaper(bank, session, id, key) {
  if (session.submitted || !keys.includes(key) || !questionsOf(bank).some(question => question.id === id)) return session
  return { ...session, answers: { ...session.answers, [id]: key } }
}
export function paperResult(bank, session) {
  const questions = questionsOf(bank)
  const answered = questions.filter(question => keys.includes(session.answers[question.id])).length
  const correct = questions.filter(question => session.answers[question.id] === question.correctKey).length
  return { total: questions.length, answered, correct, wrong: answered - correct, unanswered: questions.length - answered,
    score: questions.length ? Number((correct * 10 / questions.length).toFixed(2)) : 0 }
}
export function loadPaperSession(bank, storage) {
  try { return restorePaperSession(bank, (storage ?? globalThis.localStorage)?.getItem(paperStorageKey(bank))) } catch { return createPaperSession(bank) }
}
export function savePaperSession(bank, session, storage) {
  try { (storage ?? globalThis.localStorage).setItem(paperStorageKey(bank), JSON.stringify(session)); return true } catch { return false }
}
