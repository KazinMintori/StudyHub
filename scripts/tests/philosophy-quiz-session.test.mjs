import test from 'node:test'
import assert from 'node:assert/strict'
import { readFileSync } from 'node:fs'
import { parse, compileScript, compileTemplate, compileStyle } from 'vue/compiler-sfc'
import {
  QUIZ_SESSION_VERSION, answerQuizQuestion, attemptQuestions, createQuizSession, filterQuizQuestions,
  historyStats, loadQuizSession, migrateParentQuizSession, nextUnansweredId, questionStatus, quizQuestions, quizResponse,
  quizStats, quizStorageKey, restartQuizSession, restoreQuizSession, saveQuizSession,
  setQuizQuestion,
} from '../../src/features/philosophy/services/quiz-session.mjs'

const question = (id, correctKey, group = 'A') => ({
  id, kind: 'quiz', prompt: `Nội dung của ${id}?`, group, groupTitle: group === 'A' ? 'Nội dung thứ nhất' : 'Nội dung thứ hai',
  options: ['A', 'B', 'C', 'D'].map(key => ({ key, text: `Phương án ${key}` })),
  correctKey, explanation: 'Giải thích đầy đủ.',
  distractors: ['A', 'B', 'C', 'D'].filter(key => key !== correctKey).map(key => ({ key, explanation: `Lý do ${key} sai.` })),
})
const bank = { schemaVersion: 1, id: 'chuong-1', chapter: 1, title: 'Chương I', questions: [question('CH001', 'B'), question('CH002', 'C'), question('CH003', 'A', 'B')] }
const complete = (session, id, key, source = bank) => answerQuizQuestion(source, session, id, key)
const memoryStorage = () => {
  const values = new Map()
  return { getItem: key => values.get(key) ?? null, setItem: (key, value) => values.set(key, value), values }
}

test('the first selection is immediately graded and locked, without mutating the previous session', () => {
  const empty = createQuizSession(bank)
  const selected = answerQuizQuestion(bank, empty, 'CH001', 'B')
  assert.equal(quizResponse(empty, 'CH001'), null, 'state helpers do not mutate the previous session')
  assert.deepEqual(quizResponse(selected, 'CH001'), { selectedKey: 'B', checked: true })
  assert.equal(questionStatus(bank.questions[0], selected), 'correct')
  assert.deepEqual(quizStats(bank, selected), { total: 3, answered: 1, correct: 1, wrong: 0, unanswered: 2 })
  assert.equal(answerQuizQuestion(bank, selected, 'CH001', 'A'), selected)
  assert.equal(answerQuizQuestion(bank, selected, 'CH001', 'B'), selected)
  assert.equal(answerQuizQuestion(bank, empty, 'CH001', 'Z'), empty)
  assert.equal(answerQuizQuestion(bank, empty, 'removed', 'A'), empty)
  const wrong = answerQuizQuestion(bank, empty, 'CH001', 'D')
  assert.equal(questionStatus(bank.questions[0], wrong), 'wrong')
  assert.equal(answerQuizQuestion(bank, wrong, 'CH001', 'B'), wrong)
})

test('correct, wrong and unanswered totals use checked answers and current answer keys', () => {
  let session = complete(createQuizSession(bank), 'CH001', 'B')
  session = complete(session, 'CH002', 'D')
  assert.deepEqual(quizStats(bank, session), { total: 3, answered: 2, correct: 1, wrong: 1, unanswered: 1 })
  const correctedBank = { ...bank, questions: [question('CH001', 'A'), question('CH002', 'D'), bank.questions[2]] }
  assert.deepEqual(quizStats(correctedBank, session), { total: 3, answered: 2, correct: 1, wrong: 1, unanswered: 1 })
  assert.equal(questionStatus(correctedBank.questions[0], session), 'wrong')
  assert.equal(questionStatus(correctedBank.questions[1], session), 'correct')
})

test('combined status, content and ID filters preserve source order', () => {
  let session = complete(createQuizSession(bank), 'CH001', 'A')
  session = complete(session, 'CH002', 'C')
  const ids = (...args) => filterQuizQuestions(bank, session, ...args).map(item => item.id)
  assert.deepEqual(ids('all'), ['CH001', 'CH002', 'CH003'])
  assert.deepEqual(ids('wrong'), ['CH001'])
  assert.deepEqual(ids('unanswered'), ['CH003'])
  assert.deepEqual(ids('all', ' ch00 ', 'A'), ['CH001', 'CH002'])
  assert.deepEqual(ids('all', '003', 'A'), [])
  assert.deepEqual(ids('unanswered', 'ch003', 'B'), ['CH003'])
})

test('navigation keeps choices and feedback and next-unanswered wraps without selecting the current question', () => {
  let session = createQuizSession(bank)
  assert.equal(nextUnansweredId(bank, session), 'CH002')
  session = complete(session, 'CH002', 'A')
  session = setQuizQuestion(bank, session, 'CH003')
  assert.equal(nextUnansweredId(bank, session), 'CH001')
  session = answerQuizQuestion(bank, session, 'CH001', 'B')
  session = setQuizQuestion(bank, session, 'CH002')
  assert.equal(quizResponse(session, 'CH002').checked, true)
  assert.equal(questionStatus(bank.questions[1], session), 'wrong')
  assert.equal(quizResponse(session, 'CH001').checked, true)
  assert.equal(setQuizQuestion(bank, session, 'unknown'), session)
  session = complete(session, 'CH001', 'B')
  session = setQuizQuestion(bank, session, 'CH003')
  assert.equal(nextUnansweredId(bank, session), null, 'only the currently open question remains')
  session = complete(session, 'CH003', 'A')
  assert.equal(nextUnansweredId(bank, session), null)
})

test('retry starts a new scope containing only checked wrong IDs and archives the previous round', () => {
  let session = complete(createQuizSession(bank), 'CH001', 'A')
  session = complete(session, 'CH002', 'C')
  const retry = restartQuizSession(bank, session, 'wrong')
  assert.deepEqual(retry.attempt.questionIds, ['CH001'])
  assert.deepEqual(retry.attempt.responses, {})
  assert.equal(retry.attempt.mode, 'wrong')
  assert.equal(retry.attempt.number, 2)
  assert.equal(retry.attempt.currentId, 'CH001')
  assert.equal(retry.history.length, 1)
  assert.deepEqual(retry.history[0], session.attempt)
  assert.equal(answerQuizQuestion(bank, retry, 'CH002', 'A'), retry, 'answers outside the retry scope are inaccessible')
  assert.deepEqual(historyStats(bank, retry), [{ number: 1, mode: 'all', total: 3, answered: 2, correct: 1, wrong: 1, unanswered: 1 }])
  const passedRetry = complete(retry, 'CH001', 'B')
  assert.equal(restartQuizSession(bank, passedRetry, 'wrong'), passedRetry, 'zero wrong answers never creates an empty round')
  const restarted = restartQuizSession(bank, passedRetry)
  assert.deepEqual(restarted.attempt.questionIds, ['CH001', 'CH002', 'CH003'])
  assert.equal(restarted.attempt.number, 3)
  assert.equal(restarted.history.length, 2)
  assert.deepEqual(quizResponse({ attempt: restarted.history[0] }, 'CH002'), { selectedKey: 'C', checked: true })
})

test('persistence resumes answers, retry scope and the current question', () => {
  const storage = memoryStorage()
  let session = complete(createQuizSession(bank), 'CH001', 'B')
  session = answerQuizQuestion(bank, session, 'CH002', 'D')
  session = setQuizQuestion(bank, session, 'CH002')
  assert.equal(saveQuizSession(bank, session, storage), true)
  assert.deepEqual(loadQuizSession(bank, storage), session)
  const retry = restartQuizSession(bank, complete(session, 'CH002', 'D'), 'wrong')
  const selectedRetry = answerQuizQuestion(bank, retry, 'CH002', 'C')
  saveQuizSession(bank, selectedRetry, storage)
  assert.deepEqual(loadQuizSession(bank, storage), selectedRetry)
})

test('chapter storage and resets remain isolated', () => {
  const otherBank = { ...bank, id: 'chuong-2', chapter: 2 }
  const storage = memoryStorage()
  const first = complete(createQuizSession(bank), 'CH001', 'A')
  const second = complete(createQuizSession(otherBank), 'CH003', 'A', otherBank)
  saveQuizSession(bank, first, storage)
  saveQuizSession(otherBank, second, storage)
  assert.notEqual(quizStorageKey(bank), quizStorageKey(otherBank))
  saveQuizSession(bank, restartQuizSession(bank, first), storage)
  assert.deepEqual(loadQuizSession(otherBank, storage), second)
  assert.equal(loadQuizSession(bank, storage).attempt.responses.CH001, undefined)
  assert.equal(loadQuizSession(bank, storage).history[0].responses.CH001.checked, true)
})

test('restore rejects corrupt envelopes and reconciles IDs, option keys and scoring against the current bank', () => {
  const fresh = createQuizSession(bank)
  for (const raw of [null, undefined, '', '{bad json', '[]', 3, true, { ...fresh, version: 99 }, { ...fresh, bankId: 'chuong-2' }, { ...fresh, bankSchemaVersion: 2 }]) {
    assert.deepEqual(restoreQuizSession(bank, raw), fresh)
  }
  const dirty = {
    ...fresh,
    attempt: {
      number: -2, mode: 'wrong', currentId: 'removed', questionIds: ['CH002', 'removed', 'CH001', 'CH002'],
      responses: {
        CH001: { selectedKey: 'B', checked: true, isCorrect: false, correctKey: 'A' },
        CH002: { selectedKey: 'Z', checked: true, isCorrect: true },
        CH003: { selectedKey: 'A', checked: true },
        removed: { selectedKey: 'D', checked: true },
      },
    },
    history: [null, [], 3, { mode: 'wrong', questionIds: ['removed'], responses: {} }],
  }
  const restored = restoreQuizSession(bank, JSON.stringify(dirty))
  assert.deepEqual(restored.attempt.questionIds, ['CH002', 'CH001'])
  assert.equal(restored.attempt.currentId, 'CH002')
  assert.deepEqual(restored.attempt.responses, { CH001: { selectedKey: 'B', checked: true } })
  assert.equal(quizStats(bank, restored).correct, 1)
  assert.deepEqual(restored.history, [])
  assert.equal(restored.attempt.number, 1)
})

test('new questions join a full-bank round and obsolete retry scopes recover to a usable full round', () => {
  const old = complete(createQuizSession(bank), 'CH001', 'B')
  const newBank = { ...bank, questions: [...bank.questions, question('CH004', 'D')] }
  assert.deepEqual(restoreQuizSession(newBank, old).attempt.questionIds, ['CH001', 'CH002', 'CH003', 'CH004'])
  const obsoleteRetry = { ...old, attempt: { ...old.attempt, mode: 'wrong', questionIds: ['removed'], currentId: 'removed' } }
  const restored = restoreQuizSession(bank, obsoleteRetry)
  assert.equal(restored.attempt.mode, 'all')
  assert.equal(restored.attempt.currentId, 'CH001')
  assert.deepEqual(restored.attempt.responses, {})
})

test('legacy selected drafts become answered while inherited answer properties are ignored', () => {
  const fresh = createQuizSession(bank)
  const responses = Object.create({ CH003: { selectedKey: 'A', checked: true } })
  responses.CH001 = { selectedKey: 'B', checked: false }
  const restored = restoreQuizSession(bank, { ...fresh, attempt: { ...fresh.attempt, responses } })
  assert.deepEqual(restored.attempt.responses, { CH001: { selectedKey: 'B', checked: true } })
  assert.equal(quizStats(bank, restored).answered, 1)
  assert.equal(answerQuizQuestion(bank, restored, 'CH001', 'A'), restored)
})

const batchBank = (number, questions) => ({ ...bank, id: `chuong-1-bai-${number}`, parentBankId: 'chuong-1', testNumber: number, totalTests: 2, questions })

test('legacy chapter responses migrate only into matching batches, grade drafts, and retain the parent record', () => {
  const storage = memoryStorage()
  const parent = createQuizSession(bank)
  parent.attempt.number = 2
  parent.attempt.currentId = 'CH002'
  parent.attempt.responses = {
    CH001: { selectedKey: 'B', checked: true, isCorrect: false },
    CH002: { selectedKey: 'D', checked: false },
    CH003: { selectedKey: 'A', checked: true },
    removed: { selectedKey: 'B', checked: true },
  }
  parent.history = [{ number: 1, mode: 'all', questionIds: bank.questions.map(item => item.id), currentId: 'CH003', responses: { CH001: { selectedKey: 'A', checked: true }, CH003: { selectedKey: 'A', checked: false } } }]
  const rawParent = JSON.stringify(parent)
  storage.setItem(quizStorageKey(bank), rawParent)
  const firstBank = batchBank(1, bank.questions.slice(0, 2))
  const secondBank = batchBank(2, bank.questions.slice(2))
  const first = loadQuizSession(firstBank, storage)
  const second = loadQuizSession(secondBank, storage)
  assert.equal(first.bankId, 'chuong-1-bai-1')
  assert.equal(first.attempt.mode, 'all')
  assert.deepEqual(first.attempt.questionIds, ['CH001', 'CH002'])
  assert.equal(first.attempt.currentId, 'CH002')
  assert.deepEqual(first.attempt.responses, { CH001: { selectedKey: 'B', checked: true }, CH002: { selectedKey: 'D', checked: true } })
  assert.deepEqual(quizStats(firstBank, first), { total: 2, answered: 2, correct: 1, wrong: 1, unanswered: 0 })
  assert.deepEqual(first.history[0].responses, { CH001: { selectedKey: 'A', checked: true } })
  assert.equal(second.attempt.currentId, 'CH003')
  assert.deepEqual(second.attempt.responses, { CH003: { selectedKey: 'A', checked: true } })
  assert.deepEqual(second.history[0].responses, { CH003: { selectedKey: 'A', checked: true } })
  assert.equal(storage.getItem(quizStorageKey(bank)), rawParent, 'migration never rewrites the original full chapter')
  assert.ok(storage.getItem(quizStorageKey(firstBank)), 'the migrated batch has an independent storage record')
  assert.ok(storage.getItem(quizStorageKey(secondBank)))
  assert.equal(answerQuizQuestion(firstBank, first, 'CH002', 'C'), first, 'migrated drafts are locked answers')
  const restarted = restartQuizSession(firstBank, first)
  saveQuizSession(firstBank, restarted, storage)
  assert.deepEqual(loadQuizSession(firstBank, storage), restarted, 'the blank restarted attempt is not replaced by old parent selections')
  assert.deepEqual(loadQuizSession(secondBank, storage), second, 'resetting one batch cannot change another batch')
  assert.equal(storage.getItem(quizStorageKey(bank)), rawParent)
})

test('parent migration opens the first unanswered batch question and always restores the full batch scope', () => {
  const parent = createQuizSession(bank)
  parent.attempt.mode = 'wrong'
  parent.attempt.questionIds = ['CH001', 'CH003']
  parent.attempt.currentId = 'CH003'
  parent.attempt.responses = { CH001: { selectedKey: 'B', checked: false }, CH003: { selectedKey: 'D', checked: true } }
  const firstBank = batchBank(1, bank.questions.slice(0, 2))
  const migrated = migrateParentQuizSession(firstBank, parent)
  assert.equal(migrated.attempt.mode, 'all')
  assert.deepEqual(migrated.attempt.questionIds, ['CH001', 'CH002'])
  assert.equal(migrated.attempt.currentId, 'CH002')
  assert.equal(quizResponse(migrated, 'CH003'), null)
  const preservedCurrent = migrateParentQuizSession(batchBank(2, bank.questions.slice(2)), parent)
  assert.equal(preservedCurrent.attempt.currentId, 'CH003')
  assert.equal(quizStats(batchBank(2, bank.questions.slice(2)), preservedCurrent).wrong, 1)
})

test('existing batch storage wins over parent state and corrupt parents cannot seed a new batch', () => {
  const storage = memoryStorage()
  const firstBank = batchBank(1, bank.questions.slice(0, 2))
  const parent = complete(createQuizSession(bank), 'CH001', 'A')
  saveQuizSession(bank, parent, storage)
  const freshBatch = createQuizSession(firstBank)
  saveQuizSession(firstBank, freshBatch, storage)
  assert.deepEqual(loadQuizSession(firstBank, storage), freshBatch)
  storage.setItem(quizStorageKey(firstBank), '{broken')
  assert.deepEqual(loadQuizSession(firstBank, storage), freshBatch, 'an existing corrupt batch must not resurrect old parent responses')
  for (const raw of ['{broken', null, '[]', { ...parent, version: 99 }, { ...parent, bankId: 'chuong-2' }, { ...parent, bankSchemaVersion: 5 }]) {
    assert.equal(migrateParentQuizSession(firstBank, raw), null)
  }
  assert.equal(migrateParentQuizSession(bank, parent), null)
  const quotaStorage = { getItem: key => key === quizStorageKey(bank) ? JSON.stringify(parent) : null, setItem() { throw new Error('quota') } }
  assert.equal(quizStats(firstBank, loadQuizSession(firstBank, quotaStorage)).answered, 1, 'an unavailable migration write must not hide recovered answers')
})

test('blocked or missing localStorage never prevents practice or SSR rendering', () => {
  const brokenStorage = { getItem() { throw new Error('blocked') }, setItem() { throw new Error('quota') } }
  assert.deepEqual(loadQuizSession(bank, brokenStorage), createQuizSession(bank))
  assert.equal(saveQuizSession(bank, createQuizSession(bank), brokenStorage), false)
  assert.deepEqual(loadQuizSession(bank), createQuizSession(bank))
  assert.equal(saveQuizSession(bank, createQuizSession(bank)), false)
})

test('empty and malformed question lists are handled without invalid navigation', () => {
  const malformed = { ...bank, questions: [null, question('CH001', 'B'), question('CH001', 'A'), { ...question('CH004', 'A'), options: [{ key: 'A' }] }, { ...question('CH005', 'Z') }, { ...question('CH006', 'B'), kind: 'essay' }] }
  assert.deepEqual(quizQuestions(malformed).map(item => item.id), ['CH001'])
  const emptyBank = { ...bank, questions: null }
  const empty = createQuizSession(emptyBank)
  assert.deepEqual(attemptQuestions(emptyBank, empty), [])
  assert.equal(empty.attempt.currentId, null)
  assert.equal(nextUnansweredId(emptyBank, empty), null)
  assert.deepEqual(quizStats(emptyBank, empty), { total: 0, answered: 0, correct: 0, wrong: 0, unanswered: 0 })
  assert.equal(restartQuizSession(emptyBank, empty), empty)
})

test('both published philosophy banks retain every question and remain independent', () => {
  for (const [id, count] of [['chuong-1', 360], ['chuong-2', 440]]) {
    const source = JSON.parse(readFileSync(`src/content/courses/triet-hoc-mac-lenin/exam/${id}.json`, 'utf8'))
    assert.equal(source.id, id)
    assert.equal(source.schemaVersion, QUIZ_SESSION_VERSION)
    assert.equal(quizQuestions(source).length, count)
    assert.equal(createQuizSession(source).attempt.questionIds.length, count)
  }
})

test('PhilosophyQuiz uses the shared exam interface and compiles for client and SSR', () => {
  const filename = 'src/features/philosophy/components/PhilosophyQuiz.vue'
  const source = readFileSync(filename, 'utf8')
  const { descriptor, errors } = parse(source, { filename })
  assert.deepEqual(errors, [])
  const script = compileScript(descriptor, { id: 'philosophy-quiz-test' })
  for (const ssr of [false, true]) {
    const template = compileTemplate({ id: 'philosophy-quiz-test', filename, source: descriptor.template.content, ssr, ssrCssVars: [], compilerOptions: { bindingMetadata: script.bindings } })
    assert.deepEqual(template.errors, [])
  }
  assert.equal(descriptor.styles.length, 0, 'No independent quiz layout or styling')
  assert.match(source, /import ExamPractice from/)
  assert.match(descriptor.template.content, /<ExamPractice/)
  assert.doesNotMatch(source, /v-html/)
  assert.doesNotMatch(descriptor.template.content, /kiểm tra|<form|type="submit"|sourceReference|sourceText|Ghi nhớ và đối chiếu/i)
})
