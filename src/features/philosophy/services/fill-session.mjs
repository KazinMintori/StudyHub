/** Pure grading and persistence helpers for chapter fill-in practice. */
export const FILL_SESSION_VERSION = 1
const isRecord = value => Boolean(value && typeof value === 'object' && !Array.isArray(value))
const version = bank => Number.isInteger(bank?.version) ? bank.version : 1
const own = (object, key) => isRecord(object) && Object.hasOwn(object, key) ? object[key] : undefined

/** Ignore accents and surface punctuation, but preserve all words, their order and digits. */
export function normalizeFillAnswer(value) {
  return String(value ?? '').normalize('NFD').replace(/\p{M}/gu, '')
    .replace(/[đĐ]/g, 'd').toLocaleLowerCase('vi')
    .replace(/[\p{P}\p{S}]/gu, ' ').replace(/\s+/gu, ' ').trim()
}

export function fillQuestions(bank) {
  const seen = new Set()
  return (Array.isArray(bank?.questions) ? bank.questions : []).filter(question => {
    if (!question || typeof question.id !== 'string' || !question.id.trim() || seen.has(question.id)) return false
    if (!Array.isArray(question.blanks) || !question.blanks.length || !Array.isArray(question.parts) || question.parts.length !== question.blanks.length + 1) return false
    if (!question.parts.every(part => typeof part === 'string') || !question.blanks.every(blank => typeof blank?.answer === 'string' && normalizeFillAnswer(blank.answer))) return false
    seen.add(question.id)
    return true
  })
}

export function gradeFillQuestion(question, values = []) {
  values = Array.isArray(values) ? values : []
  const results = (question?.blanks || []).map((blank, index) => {
    const value = normalizeFillAnswer(values[index])
    const accepted = [blank.answer, ...(Array.isArray(blank.alternatives) ? blank.alternatives : [])]
      .filter(answer => typeof answer === 'string' && normalizeFillAnswer(answer))
    return { empty: !value, correct: Boolean(value && accepted.some(answer => normalizeFillAnswer(answer) === value)), expected: blank.answer }
  })
  const complete = results.length > 0 && results.every(result => !result.empty)
  return { complete, correct: complete && results.every(result => result.correct), results }
}

export function fillStorageKey(bank) {
  return `studyhub:triet-hoc-mac-lenin:fill:v${FILL_SESSION_VERSION}:${encodeURIComponent(bank?.id || 'unknown')}:bank-v${version(bank)}`
}

export function createFillSession(bank) {
  return { version: FILL_SESSION_VERSION, bankId: bank?.id || '', bankVersion: version(bank), currentId: fillQuestions(bank)[0]?.id || null, responses: {} }
}

export function fillResponse(session, questionId) {
  return own(session?.responses, questionId) || null
}

export function restoreFillSession(bank, raw) {
  const fresh = createFillSession(bank)
  let stored = raw
  try { if (typeof raw === 'string') stored = JSON.parse(raw) } catch { return fresh }
  if (!isRecord(stored) || stored.version !== fresh.version || stored.bankVersion !== fresh.bankVersion || stored.bankId !== fresh.bankId) return fresh
  const questions = fillQuestions(bank)
  for (const question of questions) {
    const response = own(stored.responses, question.id)
    if (!isRecord(response) || !Array.isArray(response.values)) continue
    const values = question.blanks.map((_, index) => typeof response.values[index] === 'string' ? response.values[index].slice(0,160) : '')
    Object.defineProperty(fresh.responses,question.id, { enumerable:true, configurable:true, writable:true,
      value: { values, checked: response.checked === true && gradeFillQuestion(question, values).complete } })
  }
  if (questions.some(question => question.id === stored.currentId)) fresh.currentId = stored.currentId
  return fresh
}

export function setFillAnswer(bank, session, questionId, blankIndex, value) {
  const question = fillQuestions(bank).find(item => item.id === questionId)
  if (!question || !Number.isInteger(blankIndex) || blankIndex < 0 || blankIndex >= question.blanks.length || typeof value !== 'string' || fillResponse(session,questionId)?.checked) return session
  const values = question.blanks.map((_, index) => fillResponse(session, questionId)?.values[index] || '')
  values[blankIndex] = value.slice(0,160)
  return { ...session, responses: { ...session.responses, [questionId]: { values, checked: false } } }
}

export function submitFillQuestion(bank, session, questionId) {
  const question = fillQuestions(bank).find(item => item.id === questionId)
  const response = fillResponse(session, questionId)
  if (!question || response?.checked || !gradeFillQuestion(question, response?.values).complete) return session
  return { ...session, responses: { ...session.responses, [questionId]: { values: [...response.values], checked: true } } }
}

export function retryFillQuestion(bank, session, questionId) {
  const question = fillQuestions(bank).find(item => item.id === questionId)
  const response = fillResponse(session,questionId)
  if (!question || !response?.checked) return session
  const grade = gradeFillQuestion(question,response.values)
  const values = grade.correct ? question.blanks.map(()=>'') : response.values.map((value,index) => grade.results[index].correct ? value : '')
  return { ...session, responses: { ...session.responses, [questionId]: { values, checked: false } } }
}

export function setCurrentFillQuestion(bank, session, questionId) {
  return fillQuestions(bank).some(question=>question.id===questionId) && session.currentId!==questionId ? { ...session, currentId: questionId } : session
}

export function fillQuestionStatus(question, session) {
  const response = fillResponse(session,question?.id)
  return !response?.checked ? 'unanswered' : gradeFillQuestion(question,response.values).correct ? 'correct' : 'wrong'
}

export function fillStats(bank, session) {
  const questions = fillQuestions(bank)
  const correct = questions.filter(question=>fillQuestionStatus(question,session)==='correct').length
  const wrong = questions.filter(question=>fillQuestionStatus(question,session)==='wrong').length
  return { total: questions.length, correct, wrong, answered: correct + wrong, unanswered: questions.length - correct - wrong }
}

export function loadFillSession(bank, storage) {
  try { return restoreFillSession(bank,(storage ?? (typeof window !== 'undefined' ? window.localStorage : null))?.getItem(fillStorageKey(bank))) }
  catch { return createFillSession(bank) }
}

export function saveFillSession(bank, session, storage) {
  try {
    const target = storage ?? (typeof window !== 'undefined' ? window.localStorage : null)
    if (!target) return false
    target.setItem(fillStorageKey(bank),JSON.stringify(session))
    return true
  } catch { return false }
}
