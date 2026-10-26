/**
 * Exam session helper service for StudyHub exam practice feature.
 * Pure logic and state helpers for navigation, question filtering,
 * URL query synchronization, answer persistence, and statistical scoring.
 * Safe for both SSR and client execution.
 */

export const VALID_MODES = ['quiz', 'essay'];
export const DEFAULT_MODE = 'quiz';

/**
 * Normalizes question mode to 'quiz' or 'essay'.
 * @param {string|null|undefined} mode
 * @returns {'quiz'|'essay'}
 */
export function normalizeMode(mode) {
  if (typeof mode === 'string') {
    const trimmed = mode.trim().toLowerCase();
    if (trimmed === 'essay') return 'essay';
    if (trimmed === 'quiz') return 'quiz';
  }
  return DEFAULT_MODE;
}

/**
 * Filters a question array by mode.
 * @param {Array<object>} questions
 * @param {string} mode
 * @returns {Array<object>}
 */
export function filterQuestionsByMode(questions, mode) {
  if (!Array.isArray(questions)) return [];
  const targetMode = normalizeMode(mode);
  return questions.filter((q) => q && q.kind === targetMode);
}

/**
 * Finds index of a question by ID.
 * @param {Array<object>} questions
 * @param {string|null|undefined} id
 * @returns {number} 0-based index or -1 if not found
 */
export function findQuestionIndexById(questions, id) {
  if (!Array.isArray(questions) || !id) return -1;
  const targetId = String(id).trim();
  return questions.findIndex((q) => q && String(q.id).trim() === targetId);
}

/**
 * Resolves the active question index with safe fallback.
 * If id is missing, invalid, or out of range, safely falls back to 0 (or -1 if questions is empty).
 * @param {Array<object>} questions
 * @param {string|null|undefined} id
 * @returns {number}
 */
export function resolveActiveIndex(questions, id) {
  if (!Array.isArray(questions) || questions.length === 0) return -1;
  if (!id) return 0;
  const index = findQuestionIndexById(questions, id);
  return index >= 0 ? index : 0;
}

/**
 * Resolves the active question object with safe fallback.
 * @param {Array<object>} questions
 * @param {string|null|undefined} id
 * @returns {object|null}
 */
export function resolveActiveQuestion(questions, id) {
  const index = resolveActiveIndex(questions, id);
  if (index >= 0 && index < questions.length) {
    return questions[index];
  }
  return null;
}

/**
 * Computes previous and next question navigation metadata.
 * @param {Array<object>} questions
 * @param {number} currentIndex
 * @returns {{
 *   hasPrev: boolean,
 *   hasNext: boolean,
 *   prevId: string|null,
 *   nextId: string|null,
 *   prevIndex: number,
 *   nextIndex: number,
 *   currentIndex: number,
 *   total: number
 * }}
 */
export function getAdjacentNav(questions, currentIndex) {
  const list = Array.isArray(questions) ? questions : [];
  const total = list.length;
  const validIndex = currentIndex >= 0 && currentIndex < total ? currentIndex : -1;

  const hasPrev = validIndex > 0;
  const hasNext = validIndex >= 0 && validIndex < total - 1;

  return {
    hasPrev,
    hasNext,
    prevId: hasPrev ? list[validIndex - 1]?.id || null : null,
    nextId: hasNext ? list[validIndex + 1]?.id || null : null,
    prevIndex: hasPrev ? validIndex - 1 : -1,
    nextIndex: hasNext ? validIndex + 1 : -1,
    currentIndex: validIndex,
    total,
  };
}

/**
 * Safely parses search query string or URLSearchParams.
 * Supports format: ?mode=quiz|essay&cau=B3-001
 * Never throws in SSR / Node.
 * @param {string|URLSearchParams|null|undefined} queryInput
 * @returns {{ mode: 'quiz'|'essay', questionId: string|null }}
 */
export function parseExamQuery(queryInput) {
  if (!queryInput) {
    return { mode: DEFAULT_MODE, questionId: null };
  }

  let params;
  try {
    if (typeof queryInput === 'string') {
      const cleanString = queryInput.startsWith('?') ? queryInput.slice(1) : queryInput;
      params = new URLSearchParams(cleanString);
    } else if (queryInput instanceof URLSearchParams) {
      params = queryInput;
    } else {
      return { mode: DEFAULT_MODE, questionId: null };
    }
  } catch {
    return { mode: DEFAULT_MODE, questionId: null };
  }

  const rawMode = params.get('mode');
  const mode = normalizeMode(rawMode);

  const rawCau = params.get('cau');
  const questionId = rawCau && rawCau.trim().length > 0 ? rawCau.trim() : null;

  return { mode, questionId };
}

/**
 * Builds standard query string for exam practice URL.
 * e.g. ?mode=quiz&cau=B3-001
 * @param {{ mode?: string, questionId?: string|null }} options
 * @returns {string}
 */
export function buildExamQueryString({ mode, questionId } = {}) {
  const normMode = normalizeMode(mode);
  const params = new URLSearchParams();
  params.set('mode', normMode);
  if (questionId && String(questionId).trim().length > 0) {
    params.set('cau', String(questionId).trim());
  }
  return `?${params.toString()}`;
}

/**
 * Creates an empty or pre-populated exam session state object.
 * @param {object} initialAnswers
 * @returns {{ answers: Record<string, { selectedKey: string, isCorrect: boolean, correctKey: string|null, answeredAt: number }> }}
 */
export function createExamSessionState(initialAnswers = {}) {
  return {
    answers: initialAnswers && typeof initialAnswers === 'object' ? { ...initialAnswers } : {},
  };
}

// Imported papers may contain duplicate correct options or an invalid question.
// Keep those source options intact without inventing a single answer key.
export function acceptedQuizKeys(question) {
  if (question?.grading === 'manual') return [];
  const keys = Array.isArray(question?.correctKeys) && question.correctKeys.length
    ? question.correctKeys : [question?.correctKey];
  return [...new Set(keys.map(key => String(key || '').trim().toUpperCase())
    .filter(key => ['A', 'B', 'C', 'D'].includes(key)))];
}

export function recordQuizReview(sessionState, question) {
  if (!sessionState || !question?.id || question.grading !== 'manual') return null;
  if (!sessionState.answers) sessionState.answers = {};
  const record = { reviewed: true, selectedKey: null, correctKey: null, isCorrect: null, answeredAt: Date.now() };
  sessionState.answers[question.id] = record;
  return record;
}

// A reviewed key can change between publications. Restore selections, then
// derive correctness from the current bank instead of trusting an old score.
export function reconcileStoredAnswers(questions, stored = {}) {
  const answers = {};
  for (const question of filterQuestionsByMode(questions, 'quiz')) {
    const record = stored?.[question.id];
    if (question.grading === 'manual') {
      if (record?.reviewed) answers[question.id] = { ...record, selectedKey: null, correctKey: null, isCorrect: null };
      continue;
    }
    if (!record || !['A', 'B', 'C', 'D'].includes(record.selectedKey)) continue;
    answers[question.id] = {
      ...record,
      correctKey: question.correctKey,
      isCorrect: acceptedQuizKeys(question).includes(record.selectedKey),
    };
  }
  return answers;
}

/**
 * Records an answer for a quiz question.
 * @param {object} sessionState
 * @param {object} question
 * @param {string} selectedKey
 * @returns {{ selectedKey: string, isCorrect: boolean, correctKey: string|null, answeredAt: number }|null}
 */
export function recordQuizAnswer(sessionState, question, selectedKey) {
  if (!sessionState || !question || !question.id || !selectedKey) return null;
  if (question.grading === 'manual') return null;
  if (!sessionState.answers) {
    sessionState.answers = {};
  }

  const normKey = String(selectedKey).trim().toUpperCase();
  const correctKey = question.correctKey ? String(question.correctKey).trim().toUpperCase() : null;
  const isCorrect = acceptedQuizKeys(question).includes(normKey);

  const answerRecord = {
    selectedKey: normKey,
    isCorrect,
    correctKey,
    answeredAt: Date.now(),
  };

  sessionState.answers[question.id] = answerRecord;
  return answerRecord;
}

/**
 * Retrieves the recorded answer for a question.
 * @param {object} sessionState
 * @param {string} questionId
 * @returns {object|null}
 */
export function getAnswer(sessionState, questionId) {
  if (!sessionState || !sessionState.answers || !questionId) return null;
  return sessionState.answers[questionId] || null;
}

/**
 * Checks if a question has been answered in this session.
 * @param {object} sessionState
 * @param {string} questionId
 * @returns {boolean}
 */
export function isAnswered(sessionState, questionId) {
  return Boolean(getAnswer(sessionState, questionId));
}

/**
 * Calculates correct/wrong statistics for quiz questions.
 * @param {object} sessionState
 * @param {Array<object>} questions
 * @returns {{
 *   totalQuiz: number,
 *   answeredCount: number,
 *   correctCount: number,
 *   wrongCount: number,
 *   scorePercentage: number
 * }}
 */
export function calculateSessionStats(sessionState, questions) {
  const quizQuestions = filterQuestionsByMode(questions, 'quiz');
  const totalQuiz = quizQuestions.length;

  let correctCount = 0;
  let wrongCount = 0;
  let answeredCount = 0;

  for (const q of quizQuestions) {
    const ans = getAnswer(sessionState, q.id);
    if (ans) {
      answeredCount++;
      if (q.grading === 'manual') continue;
      if (ans.isCorrect) {
        correctCount++;
      } else {
        wrongCount++;
      }
    }
  }

  const gradableCount = quizQuestions.filter(q => q.grading !== 'manual').length;
  const scorePercentage = gradableCount > 0 ? Math.round((correctCount / gradableCount) * 100) : 0;

  return {
    totalQuiz,
    answeredCount,
    correctCount,
    wrongCount,
    scorePercentage,
  };
}

/**
 * Safely loads stored answers from sessionStorage if in browser environment.
 * @param {string} storageKey
 * @returns {Record<string, object>}
 */
export function loadStoredAnswers(storageKey) {
  if (typeof window === 'undefined' || !storageKey) return {};
  try {
    const raw = window.sessionStorage?.getItem(storageKey);
    if (!raw) return {};
    const parsed = JSON.parse(raw);
    return parsed && typeof parsed === 'object' ? parsed : {};
  } catch {
    return {};
  }
}

/**
 * Safely saves answers to sessionStorage if in browser environment.
 * @param {string} storageKey
 * @param {Record<string, object>} answers
 */
export function saveStoredAnswers(storageKey, answers) {
  if (typeof window === 'undefined' || !storageKey || !answers) return;
  try {
    window.sessionStorage?.setItem(storageKey, JSON.stringify(answers));
  } catch {
    // Ignore storage quota or disabled storage errors
  }
}
