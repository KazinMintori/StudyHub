/** Pure session logic for philosophy practice. No browser globals during SSR. */
export const QUIZ_SESSION_VERSION = 1
export const QUIZ_FILTERS = ['all', 'unanswered', 'wrong']
const COURSE_ID = 'triet-hoc-mac-lenin'
const KEYS = ['A', 'B', 'C', 'D']
const isRecord = value => Boolean(value && typeof value === 'object' && !Array.isArray(value))
const own = (object, key) => isRecord(object) && Object.hasOwn(object, key) ? object[key] : undefined
const bankVersion = bank => Number.isSafeInteger(bank?.schemaVersion) ? bank.schemaVersion : 1

export function quizQuestions(bank) {
  const seen = new Set()
  return (Array.isArray(bank?.questions) ? bank.questions : []).filter(question => {
    if (!question || question.kind !== 'quiz' || typeof question.id !== 'string' || !question.id.trim() || seen.has(question.id)) return false
    if (!Array.isArray(question.options) || question.options.length !== 4) return false
    const keys = question.options.map(option => option?.key)
    if (!KEYS.every(key => keys.includes(key)) || !KEYS.includes(question.correctKey)) return false
    seen.add(question.id)
    return true
  })
}

export function quizStorageKey(bank) {
  return `studyhub:${COURSE_ID}:quiz:v${QUIZ_SESSION_VERSION}:${encodeURIComponent(bank?.id || 'unknown')}:bank-v${bankVersion(bank)}`
}

function reconcileAttempt(questions, stored, fallbackNumber = 1) {
  const validIds = new Set(questions.map(question => question.id))
  const requested = stored?.mode === 'wrong' && Array.isArray(stored.questionIds) ? stored.questionIds : questions.map(question => question.id)
  const questionIds = [...new Set(requested.filter(id => typeof id === 'string' && validIds.has(id)))]
  const scope = new Set(questionIds)
  const responses = Object.fromEntries(questions.flatMap(question => {
    if (!scope.has(question.id)) return []
    const record = own(stored?.responses, question.id)
    if (!isRecord(record) || !question.options.some(option => option.key === record.selectedKey)) return []
    // Every valid selection is an answer now, including drafts from the former two-step UI.
    return [[question.id, { selectedKey: record.selectedKey, checked: true }]]
  }))
  return {
    number: Number.isSafeInteger(stored?.number) && stored.number > 0 ? stored.number : fallbackNumber,
    mode: stored?.mode === 'wrong' ? 'wrong' : 'all',
    questionIds,
    currentId: scope.has(stored?.currentId) ? stored.currentId : questionIds[0] || null,
    responses,
  }
}

export function createQuizSession(bank) {
  const questions = quizQuestions(bank)
  return {
    version: QUIZ_SESSION_VERSION,
    bankId: bank?.id || '',
    bankSchemaVersion: bankVersion(bank),
    attempt: reconcileAttempt(questions, null),
    history: [],
  }
}

/** Discard invalid selections, unknown IDs and cached scores. Current keys decide correctness. */
export function restoreQuizSession(bank, raw) {
  const fresh = createQuizSession(bank)
  let stored = raw
  try { if (typeof raw === 'string') stored = JSON.parse(raw) } catch { return fresh }
  if (!isRecord(stored) || stored.version !== QUIZ_SESSION_VERSION || stored.bankId !== fresh.bankId || stored.bankSchemaVersion !== fresh.bankSchemaVersion) return fresh
  const questions = quizQuestions(bank)
  const attempt = reconcileAttempt(questions, isRecord(stored.attempt) ? stored.attempt : null)
  // An obsolete retry scope cannot leave a nonempty bank stuck on an empty screen.
  if (!attempt.questionIds.length && questions.length) Object.assign(attempt, reconcileAttempt(questions, null, attempt.number))
  const history = (Array.isArray(stored.history) ? stored.history : [])
    .filter(isRecord)
    .map((record, index) => reconcileAttempt(questions, record, index + 1))
    .filter(record => record.questionIds.length && Object.keys(record.responses).length)
  return { ...fresh, attempt, history }
}

export function attemptQuestions(bank, session) {
  const byId = new Map(quizQuestions(bank).map(question => [question.id, question]))
  return (session?.attempt?.questionIds || []).flatMap(id => byId.has(id) ? [byId.get(id)] : [])
}

export function quizResponse(session, questionId) {
  return own(session?.attempt?.responses, questionId) || null
}

export function questionStatus(question, session) {
  const response = quizResponse(session, question?.id)
  if (!response?.checked) return 'unanswered'
  return response.selectedKey === question.correctKey ? 'correct' : 'wrong'
}

export function quizStats(bank, session) {
  const questions = attemptQuestions(bank, session)
  let correct = 0
  let wrong = 0
  for (const question of questions) {
    const status = questionStatus(question, session)
    if (status === 'correct') correct += 1
    if (status === 'wrong') wrong += 1
  }
  return { total: questions.length, answered: correct + wrong, correct, wrong, unanswered: questions.length - correct - wrong }
}

function scopedQuestion(bank, session, questionId) {
  if (!session?.attempt?.questionIds?.includes(questionId)) return null
  return quizQuestions(bank).find(question => question.id === questionId) || null
}

/** First selection is immediately graded and locked for this attempt. */
export function answerQuizQuestion(bank, session, questionId, selectedKey) {
  const question = scopedQuestion(bank, session, questionId)
  if (!question || quizResponse(session, questionId)?.checked || !question.options.some(option => option.key === selectedKey)) return session
  return {
    ...session,
    attempt: {
      ...session.attempt,
      responses: { ...session.attempt.responses, [questionId]: { selectedKey, checked: true } },
    },
  }
}

export function setQuizQuestion(bank, session, questionId) {
  if (!scopedQuestion(bank, session, questionId) || session.attempt.currentId === questionId) return session
  return { ...session, attempt: { ...session.attempt, currentId: questionId } }
}

/** Filters affect the jump list, so answering a question never removes its feedback. */
export function filterQuizQuestions(bank, session, filter = 'all', search = '', group = '') {
  const term = typeof search === 'string' ? search.trim().toLocaleLowerCase('vi') : ''
  return attemptQuestions(bank, session).filter(question => {
    if (term && !question.id.toLocaleLowerCase('vi').includes(term)) return false
    if (group && question.group !== group) return false
    const status = questionStatus(question, session)
    if (filter === 'unanswered') return status === 'unanswered'
    if (filter === 'wrong') return status === 'wrong'
    return true
  })
}

export function nextUnansweredId(bank, session) {
  const questions = attemptQuestions(bank, session)
  const index = questions.findIndex(question => question.id === session?.attempt?.currentId)
  for (let offset = 1; offset <= questions.length; offset += 1) {
    const question = questions[(Math.max(index, 0) + offset) % questions.length]
    if (question.id !== session?.attempt?.currentId && questionStatus(question, session) === 'unanswered') return question.id
  }
  return null
}

/** Starts a new round without touching another bank or discarding the previous round. */
export function restartQuizSession(bank, session, mode = 'all') {
  const questions = mode === 'wrong'
    ? attemptQuestions(bank, session).filter(question => questionStatus(question, session) === 'wrong')
    : quizQuestions(bank)
  if (!questions.length) return session
  const previous = session.attempt
  const history = Object.keys(previous.responses).length ? [...session.history, previous] : [...session.history]
  const number = Math.max(previous.number, ...history.map(attempt => attempt.number)) + 1
  return {
    ...session,
    attempt: { number, mode: mode === 'wrong' ? 'wrong' : 'all', questionIds: questions.map(question => question.id), currentId: questions[0].id, responses: {} },
    history,
  }
}

export function historyStats(bank, session) {
  return [...(session?.history || [])].reverse().map(attempt => ({
    number: attempt.number,
    mode: attempt.mode,
    ...quizStats(bank, { attempt }),
  }))
}

/** Split the legacy chapter attempt into an independent full-scope test attempt. */
export function migrateParentQuizSession(bank, raw) {
  if (typeof bank?.parentBankId !== 'string' || !bank.parentBankId || bank.parentBankId === bank.id) return null
  let stored = raw
  try { if (typeof raw === 'string') stored = JSON.parse(raw) } catch { return null }
  if (!isRecord(stored) || stored.version !== QUIZ_SESSION_VERSION || stored.bankId !== bank.parentBankId || stored.bankSchemaVersion !== bankVersion(bank)) return null
  const fresh = createQuizSession(bank)
  const questions = quizQuestions(bank)
  const attempt = reconcileAttempt(questions, { ...(isRecord(stored.attempt) ? stored.attempt : {}), mode: 'all' })
  const parentCurrent = stored.attempt?.currentId
  attempt.currentId = attempt.questionIds.includes(parentCurrent)
    ? parentCurrent
    : questions.find(question => !own(attempt.responses, question.id))?.id || attempt.questionIds[0] || null
  const history = (Array.isArray(stored.history) ? stored.history : [])
    .filter(isRecord)
    .map((record, index) => reconcileAttempt(questions, record, index + 1))
    .filter(record => record.questionIds.length && Object.keys(record.responses).length)
  return { ...fresh, attempt, history }
}

export function loadQuizSession(bank, storage) {
  try {
    const resolved = storage ?? (typeof window !== 'undefined' ? window.localStorage : null)
    const raw = resolved?.getItem(quizStorageKey(bank))
    // An existing test record always wins, including a deliberately restarted empty round.
    if (raw != null) return restoreQuizSession(bank, raw)
    if (bank?.parentBankId && bank.parentBankId !== bank.id) {
      const parentRaw = resolved?.getItem(quizStorageKey({ ...bank, id: bank.parentBankId }))
      const migrated = migrateParentQuizSession(bank, parentRaw)
      if (migrated) {
        saveQuizSession(bank, migrated, resolved)
        return migrated
      }
    }
    return createQuizSession(bank)
  } catch { return createQuizSession(bank) }
}

/** Returns false for blocked/quota storage so the UI can describe the practical limit. */
export function saveQuizSession(bank, session, storage) {
  try {
    const resolved = storage ?? (typeof window !== 'undefined' ? window.localStorage : null)
    if (!resolved) return false
    resolved.setItem(quizStorageKey(bank), JSON.stringify(session))
    return true
  } catch { return false }
}
