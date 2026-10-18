import test from 'node:test';
import assert from 'node:assert/strict';
import { readFileSync, readdirSync } from 'node:fs';
import { resolve } from 'node:path';
import { execFileSync } from 'node:child_process';
import { parse, compileScript, compileTemplate } from 'vue/compiler-sfc';

test('Reviewed feedback preserves question topics and signed indexing literals', () => {
  const loadReview = lesson => new Map(JSON.parse(readFileSync(resolve(`raw_materials/xu-ly-du-lieu/exam/reviews/bai-${lesson}.json`), 'utf8')).items.map(item => [item.id, item]));
  const first = loadReview('01');
  const third = loadReview('03');
  assert.match(first.get('B1-015').optionExplanations.D, /phụ thuộc/);
  assert.doesNotMatch(JSON.stringify(first.get('B1-015').optionExplanations), /Colab|VS Code/);
  assert.match(first.get('B1-024').optionExplanations.C, /khai báo/);
  assert.doesNotMatch(JSON.stringify(first.get('B1-024').optionExplanations), /cell|kernel|notebook/);
  assert.match(third.get('B3-003').optionExplanations.A, /`-1`/);
  assert.match(third.get('B3-MR09').optionExplanations.C, /`-1`/);
});

import {
  VALID_MODES,
  DEFAULT_MODE,
  normalizeMode,
  filterQuestionsByMode,
  findQuestionIndexById,
  resolveActiveIndex,
  resolveActiveQuestion,
  getAdjacentNav,
  parseExamQuery,
  buildExamQueryString,
  createExamSessionState,
  recordQuizAnswer,
  getAnswer,
  isAnswered,
  calculateSessionStats,
  loadStoredAnswers,
  saveStoredAnswers,
  reconcileStoredAnswers,
} from '../../src/features/exam/services/exam-session.mjs';

test('Published exam bank passes full source, review and detailed-solution audit', () => {
  const output = execFileSync(process.execPath, ['scripts/verify-data-exam.mjs'], { encoding: 'utf8' });
  assert.match(output, /PASS 548 questions/);
});

test('Restored selections are rescored against reviewed keys and ignore invalid records', () => {
  const questions = [{ id:'Q', kind:'quiz', correctKey:'C' }, {id:'R', kind:'quiz', correctKey:'B'}];
  const answers = reconcileStoredAnswers(questions, {
    Q:{ selectedKey:'C', correctKey:'A', isCorrect:false },
    R:{ selectedKey:'Z', isCorrect:true },
    removed:{ selectedKey:'A', isCorrect:true },
  });
  assert.deepEqual(Object.keys(answers), ['Q']);
  assert.equal(answers.Q.correctKey, 'C');
  assert.equal(answers.Q.isCorrect, true);
});

test('ExamPractice.vue SFC compiles cleanly with Vue compiler (client & SSR modes)', () => {
  const componentPath = resolve('src/features/exam/components/ExamPractice.vue');
  const source = readFileSync(componentPath, 'utf-8');

  // Parse SFC
  const sfc = parse(source, { filename: 'ExamPractice.vue' });
  assert.equal(sfc.errors.length, 0, `SFC parse errors: ${sfc.errors.map((e) => e.message).join(', ')}`);
  assert.ok(sfc.descriptor.template, 'ExamPractice.vue must have a <template> block');
  assert.ok(sfc.descriptor.scriptSetup, 'ExamPractice.vue must have a <script setup> block');
  assert.ok(sfc.descriptor.styles.length > 0, 'ExamPractice.vue must have a <style> block');
  assert.ok(sfc.descriptor.styles[0].scoped, 'ExamPractice.vue style block must be scoped');

  // Compile Script
  const scopeId = 'data-v-exampractice';
  const compiledScript = compileScript(sfc.descriptor, {
    id: scopeId,
  });
  assert.ok(compiledScript.content, 'Compiled script content must not be empty');

  // Compile Client Template with script bindings
  const compiledClientTemplate = compileTemplate({
    id: scopeId,
    source: sfc.descriptor.template.content,
    filename: 'ExamPractice.vue',
    scoped: true,
    compilerOptions: {
      bindingMetadata: compiledScript.bindings,
    },
  });
  assert.equal(
    compiledClientTemplate.errors.length,
    0,
    `Client template compile errors: ${compiledClientTemplate.errors.map((e) => (typeof e === 'string' ? e : e.message)).join(', ')}`
  );

  // Compile SSR Template with script bindings
  const compiledSsrTemplate = compileTemplate({
    id: scopeId,
    source: sfc.descriptor.template.content,
    filename: 'ExamPractice.vue',
    scoped: true,
    ssr: true,
    ssrCssVars: sfc.descriptor.cssVars,
    compilerOptions: {
      bindingMetadata: compiledScript.bindings,
    },
  });
  assert.equal(
    compiledSsrTemplate.errors.length,
    0,
    `SSR template compile errors: ${compiledSsrTemplate.errors.map((e) => (typeof e === 'string' ? e : e.message)).join(', ')}`
  );
});

test('normalizeMode: validates quiz and essay, falling back safely to quiz', () => {
  assert.equal(normalizeMode('quiz'), 'quiz');
  assert.equal(normalizeMode('essay'), 'essay');
  assert.equal(normalizeMode('QUIZ'), 'quiz');
  assert.equal(normalizeMode('Essay '), 'essay');
  assert.equal(normalizeMode('unknown'), DEFAULT_MODE);
  assert.equal(normalizeMode(''), DEFAULT_MODE);
  assert.equal(normalizeMode(null), DEFAULT_MODE);
  assert.equal(normalizeMode(undefined), DEFAULT_MODE);
  assert.deepEqual(VALID_MODES, ['quiz', 'essay']);
});

test('filterQuestionsByMode: filters questions correctly by quiz and essay', () => {
  const mockQuestions = [
    { id: 'Q1', kind: 'quiz' },
    { id: 'E1', kind: 'essay' },
    { id: 'Q2', kind: 'quiz' },
    { id: 'E2', kind: 'essay' },
  ];

  const quizOnly = filterQuestionsByMode(mockQuestions, 'quiz');
  assert.equal(quizOnly.length, 2);
  assert.deepEqual(quizOnly.map((q) => q.id), ['Q1', 'Q2']);

  const essayOnly = filterQuestionsByMode(mockQuestions, 'essay');
  assert.equal(essayOnly.length, 2);
  assert.deepEqual(essayOnly.map((q) => q.id), ['E1', 'E2']);

  assert.deepEqual(filterQuestionsByMode([], 'quiz'), []);
  assert.deepEqual(filterQuestionsByMode(null, 'quiz'), []);
});

test('resolveActiveIndex and resolveActiveQuestion: safe fallback for invalid IDs', () => {
  const mockQuestions = [
    { id: 'B1-001', kind: 'quiz' },
    { id: 'B1-002', kind: 'quiz' },
    { id: 'B1-003', kind: 'quiz' },
  ];

  // Exact matches
  assert.equal(findQuestionIndexById(mockQuestions, 'B1-002'), 1);
  assert.equal(resolveActiveIndex(mockQuestions, 'B1-002'), 1);
  assert.equal(resolveActiveQuestion(mockQuestions, 'B1-002')?.id, 'B1-002');

  // Missing or invalid ID safely falls back to index 0
  assert.equal(findQuestionIndexById(mockQuestions, 'INVALID-ID'), -1);
  assert.equal(resolveActiveIndex(mockQuestions, 'INVALID-ID'), 0);
  assert.equal(resolveActiveQuestion(mockQuestions, 'INVALID-ID')?.id, 'B1-001');

  assert.equal(resolveActiveIndex(mockQuestions, null), 0);
  assert.equal(resolveActiveIndex(mockQuestions, undefined), 0);
  assert.equal(resolveActiveIndex(mockQuestions, ''), 0);

  // Empty questions list safely returns -1 and null
  assert.equal(resolveActiveIndex([], 'B1-001'), -1);
  assert.equal(resolveActiveQuestion([], 'B1-001'), null);
});

test('getAdjacentNav: handles first, middle, last, and single-item question navigation', () => {
  const mockQuestions = [
    { id: 'Q1' },
    { id: 'Q2' },
    { id: 'Q3' },
  ];

  // First item
  const firstNav = getAdjacentNav(mockQuestions, 0);
  assert.equal(firstNav.hasPrev, false);
  assert.equal(firstNav.hasNext, true);
  assert.equal(firstNav.prevId, null);
  assert.equal(firstNav.nextId, 'Q2');
  assert.equal(firstNav.total, 3);

  // Middle item
  const midNav = getAdjacentNav(mockQuestions, 1);
  assert.equal(midNav.hasPrev, true);
  assert.equal(midNav.hasNext, true);
  assert.equal(midNav.prevId, 'Q1');
  assert.equal(midNav.nextId, 'Q3');

  // Last item
  const lastNav = getAdjacentNav(mockQuestions, 2);
  assert.equal(lastNav.hasPrev, true);
  assert.equal(lastNav.hasNext, false);
  assert.equal(lastNav.prevId, 'Q2');
  assert.equal(lastNav.nextId, null);

  // Single item
  const singleNav = getAdjacentNav([{ id: 'SOLO' }], 0);
  assert.equal(singleNav.hasPrev, false);
  assert.equal(singleNav.hasNext, false);
});

test('parseExamQuery: safely parses URL query strings without throwing', () => {
  assert.deepEqual(parseExamQuery('?mode=quiz&cau=B3-001'), {
    mode: 'quiz',
    questionId: 'B3-001',
  });

  assert.deepEqual(parseExamQuery('mode=essay&cau=B1-008'), {
    mode: 'essay',
    questionId: 'B1-008',
  });

  // Invalid mode falls back to quiz
  assert.deepEqual(parseExamQuery('?mode=invalid&cau=B1-005'), {
    mode: 'quiz',
    questionId: 'B1-005',
  });

  // Missing cau
  assert.deepEqual(parseExamQuery('?mode=essay'), {
    mode: 'essay',
    questionId: null,
  });

  // Null, undefined, empty string
  assert.deepEqual(parseExamQuery(''), { mode: 'quiz', questionId: null });
  assert.deepEqual(parseExamQuery(null), { mode: 'quiz', questionId: null });
  assert.deepEqual(parseExamQuery(undefined), { mode: 'quiz', questionId: null });
});

test('buildExamQueryString: builds URL search string correctly', () => {
  assert.equal(
    buildExamQueryString({ mode: 'quiz', questionId: 'B3-001' }),
    '?mode=quiz&cau=B3-001'
  );
  assert.equal(
    buildExamQueryString({ mode: 'essay', questionId: 'B1-008' }),
    '?mode=essay&cau=B1-008'
  );
  assert.equal(
    buildExamQueryString({ mode: 'quiz', questionId: null }),
    '?mode=quiz'
  );
  assert.equal(
    buildExamQueryString({ mode: 'invalid', questionId: 'Q1' }),
    '?mode=quiz&cau=Q1'
  );
});

test('recordQuizAnswer and calculateSessionStats: records choices and computes score statistics', () => {
  const session = createExamSessionState();
  const q1 = { id: 'Q1', kind: 'quiz', correctKey: 'B' };
  const q2 = { id: 'Q2', kind: 'quiz', correctKey: 'C' };
  const q3 = { id: 'Q3', kind: 'quiz', correctKey: 'A' };
  const e1 = { id: 'E1', kind: 'essay', correctKey: null };

  const allQuestions = [q1, q2, q3, e1];

  // Answer Q1 with 'B' (correct)
  const ans1 = recordQuizAnswer(session, q1, 'B');
  assert.ok(ans1);
  assert.equal(ans1.isCorrect, true);
  assert.equal(ans1.selectedKey, 'B');
  assert.equal(isAnswered(session, 'Q1'), true);
  assert.equal(getAnswer(session, 'Q1')?.isCorrect, true);

  // Answer Q2 with 'A' (wrong)
  const ans2 = recordQuizAnswer(session, q2, 'A');
  assert.ok(ans2);
  assert.equal(ans2.isCorrect, false);
  assert.equal(ans2.selectedKey, 'A');
  assert.equal(isAnswered(session, 'Q2'), true);

  // Check stats before Q3 is answered
  const stats1 = calculateSessionStats(session, allQuestions);
  assert.equal(stats1.totalQuiz, 3);
  assert.equal(stats1.answeredCount, 2);
  assert.equal(stats1.correctCount, 1);
  assert.equal(stats1.wrongCount, 1);
  assert.equal(stats1.scorePercentage, 33);

  // Answer Q3 with 'A' (correct)
  recordQuizAnswer(session, q3, 'A');
  const stats2 = calculateSessionStats(session, allQuestions);
  assert.equal(stats2.totalQuiz, 3);
  assert.equal(stats2.answeredCount, 3);
  assert.equal(stats2.correctCount, 2);
  assert.equal(stats2.wrongCount, 1);
  assert.equal(stats2.scorePercentage, 67);
});

test('loadStoredAnswers and saveStoredAnswers: safe in SSR and handles storage unavailability', () => {
  assert.deepEqual(loadStoredAnswers('test-key'), {});
  assert.doesNotThrow(() => saveStoredAnswers('test-key', { Q1: { selectedKey: 'A' } }));
});

test('Integration with all 8 real banks: verifies schema, 548 total questions, and kinds', () => {
  const banksDir = resolve('raw_materials/xu-ly-du-lieu/exam/banks');
  const files = readdirSync(banksDir).filter((f) => f.endsWith('.json')).sort();
  assert.equal(files.length, 8, 'Must have exactly 8 bank files (bai-01.json to bai-08.json)');

  let grandTotal = 0;
  let totalQuiz = 0;
  let totalEssay = 0;

  for (const file of files) {
    const raw = readFileSync(resolve(banksDir, file), 'utf-8');
    const bank = JSON.parse(raw);

    assert.ok(bank.lesson, `${file} missing lesson property`);
    assert.ok(bank.sourceTitle, `${file} missing sourceTitle property`);
    assert.ok(Array.isArray(bank.questions), `${file} questions must be an array`);

    const quizzes = filterQuestionsByMode(bank.questions, 'quiz');
    const essays = filterQuestionsByMode(bank.questions, 'essay');

    grandTotal += bank.questions.length;
    totalQuiz += quizzes.length;
    totalEssay += essays.length;

    // Verify individual question contract
    for (const q of bank.questions) {
      assert.ok(q.id, `Question in ${file} missing id`);
      assert.ok(['quiz', 'essay'].includes(q.kind), `Invalid kind in ${file}: ${q.kind}`);
      assert.ok(q.promptMarkdown, `Question ${q.id} in ${file} missing promptMarkdown`);

      if (q.kind === 'quiz') {
        assert.ok(Array.isArray(q.options), `Quiz ${q.id} in ${file} options must be array`);
        assert.equal(q.options.length, 4, `Quiz ${q.id} in ${file} must have 4 options A–D`);
        assert.ok(['A', 'B', 'C', 'D'].includes(q.correctKey), `Quiz ${q.id} has invalid correctKey: ${q.correctKey}`);
      } else {
        assert.equal(q.correctKey, null, `Essay ${q.id} in ${file} must have correctKey === null`);
      }
    }

    // Verify navigation on first and last question
    const firstNav = getAdjacentNav(quizzes, 0);
    assert.equal(firstNav.hasPrev, false);
    assert.equal(firstNav.hasNext, true);

    const lastNav = getAdjacentNav(quizzes, quizzes.length - 1);
    assert.equal(lastNav.hasPrev, true);
    assert.equal(lastNav.hasNext, false);
  }

  assert.equal(grandTotal, 548, 'Curriculum must contain exactly 548 questions across 8 lessons');
  assert.equal(totalQuiz, 364, 'Must have exactly 364 quiz questions');
  assert.equal(totalEssay, 184, 'Must have exactly 184 essay questions');
});
