import { test, describe } from 'node:test'
import assert from 'node:assert/strict'
import {
  normalizeHash,
  isValidLecturePartId,
  classifyLectureHash,
  isSamePageLectureLink,
  shouldIgnoreNavigationClick
} from './tab-service.mjs'
import {
  DEFAULT_LECTURE_PART,
  EXERCISE_LECTURE_PART,
  LECTURE_PART_IDS
} from '../../../config/navigation.mjs'

describe('tab-service: normalizeHash', () => {
  test('returns empty string for null, undefined, or empty values', () => {
    assert.equal(normalizeHash(null), '')
    assert.equal(normalizeHash(undefined), '')
    assert.equal(normalizeHash(''), '')
    assert.equal(normalizeHash('   '), '')
    assert.equal(normalizeHash('#'), '')
  })

  test('strips leading hash', () => {
    assert.equal(normalizeHash('#slides'), 'slides')
    assert.equal(normalizeHash('#bai-tap'), 'bai-tap')
    assert.equal(normalizeHash('notes'), 'notes')
  })

  test('decodes URI encoded characters', () => {
    assert.equal(normalizeHash('#%C4%91%E1%BB%8Bnh-ngh%C4%A9a'), 'định-nghĩa')
    assert.equal(normalizeHash('%E2%9C%93'), '✓')
  })

  test('handles malformed URI sequences without throwing', () => {
    assert.equal(normalizeHash('#%E0%A4%A'), '%E0%A4%A')
  })
})

describe('tab-service: isValidLecturePartId', () => {
  test('validates string array and object array of allowed parts', () => {
    assert.equal(isValidLecturePartId('slides', LECTURE_PART_IDS), false)
    assert.equal(isValidLecturePartId('notes', LECTURE_PART_IDS), true)
    assert.equal(isValidLecturePartId('bai-tap', LECTURE_PART_IDS), true)
    assert.equal(isValidLecturePartId('kien-thuc-can-co', LECTURE_PART_IDS), true)
    assert.equal(isValidLecturePartId('cheatsheet', LECTURE_PART_IDS), true)

    const objectParts = [{ id: 'slides', name: 'Slides' }, { id: 'notes', name: 'Notes' }]
    assert.equal(isValidLecturePartId('slides', objectParts), true)
    assert.equal(isValidLecturePartId('unknown', objectParts), false)
  })

  test('rejects missing or non-matching IDs', () => {
    assert.equal(isValidLecturePartId(''), false)
    assert.equal(isValidLecturePartId('random-id'), false)
    assert.equal(isValidLecturePartId(null), false)
  })
})

describe('tab-service: classifyLectureHash', () => {
  test('classifies direct tab hashes correctly', () => {
    assert.equal(classifyLectureHash('#slides'), 'notes')
    assert.equal(classifyLectureHash('#notes'), 'notes')
    assert.equal(classifyLectureHash('#cheatsheet'), 'cheatsheet')
    assert.equal(classifyLectureHash('#kien-thuc-can-co'), 'kien-thuc-can-co')
    assert.equal(classifyLectureHash('#bai-tap'), 'bai-tap')
  })

  test('classifies hashes without leading hash prefix', () => {
    assert.equal(classifyLectureHash('slides'), 'notes')
    assert.equal(classifyLectureHash('cheatsheet'), 'cheatsheet')
  })

  test('falls back to default notes tab for empty or null hash', () => {
    assert.equal(classifyLectureHash(''), DEFAULT_LECTURE_PART)
    assert.equal(classifyLectureHash(null), DEFAULT_LECTURE_PART)
    assert.equal(classifyLectureHash(undefined), DEFAULT_LECTURE_PART)
    assert.equal(classifyLectureHash('#'), DEFAULT_LECTURE_PART)
  })

  test('classifies exercise anchors as bai-tap when anchor is in exercise content', () => {
    const isExerciseAnchor = (id) => id === 'bt-1' || id === 'bai-tap-2'
    assert.equal(classifyLectureHash('#bt-1', { isExerciseAnchor }), EXERCISE_LECTURE_PART)
    assert.equal(classifyLectureHash('#bai-tap-2', { isExerciseAnchor }), EXERCISE_LECTURE_PART)
  })

  test('classifies regular anchors as notes when not in exercise content', () => {
    const isExerciseAnchor = () => false
    assert.equal(classifyLectureHash('#dinh-nghia-1', { isExerciseAnchor }), DEFAULT_LECTURE_PART)
    assert.equal(classifyLectureHash('#muc-tieu', { isExerciseAnchor }), DEFAULT_LECTURE_PART)
  })

  test('handles malformed URI safely and falls back to default', () => {
    assert.equal(classifyLectureHash('#%E0%A4%A'), DEFAULT_LECTURE_PART)
  })

  test('respects custom allowedParts, defaultPart and exercisePart options', () => {
    const custom = classifyLectureHash('#custom-tab', {
      allowedParts: ['custom-tab', 'other'],
      defaultPart: 'fallback'
    })
    assert.equal(custom, 'custom-tab')

    const fallback = classifyLectureHash('#unknown', {
      defaultPart: 'custom-default'
    })
    assert.equal(fallback, 'custom-default')
  })
})

describe('tab-service: isSamePageLectureLink', () => {
  const currentHref = 'https://studyhub.uet.vnu.edu.vn/toan-ai/bai-giang/gioi-thieu'

  test('detects valid in-page lecture link clicks', () => {
    const result1 = isSamePageLectureLink(
      'https://studyhub.uet.vnu.edu.vn/toan-ai/bai-giang/gioi-thieu#slides',
      currentHref
    )
    assert.deepEqual(result1, { isMatch: false, part: null })

    const result2 = isSamePageLectureLink('#cheatsheet', currentHref)
    assert.deepEqual(result2, { isMatch: true, part: 'cheatsheet' })

    const result3 = isSamePageLectureLink('#bai-tap', currentHref)
    assert.deepEqual(result3, { isMatch: true, part: 'bai-tap' })
  })

  test('rejects links targeting different pathnames or origins', () => {
    const diffPath = isSamePageLectureLink(
      'https://studyhub.uet.vnu.edu.vn/toan-ai/bai-giang/khac#slides',
      currentHref
    )
    assert.deepEqual(diffPath, { isMatch: false, part: null })

    const diffOrigin = isSamePageLectureLink(
      'https://other-domain.edu.vn/toan-ai/bai-giang/gioi-thieu#slides',
      currentHref
    )
    assert.deepEqual(diffOrigin, { isMatch: false, part: null })
  })

  test('rejects links without matching lecture hash', () => {
    const nonLectureHash = isSamePageLectureLink(
      'https://studyhub.uet.vnu.edu.vn/toan-ai/bai-giang/gioi-thieu#random-heading',
      currentHref
    )
    assert.deepEqual(nonLectureHash, { isMatch: false, part: null })

    const noHash = isSamePageLectureLink(
      'https://studyhub.uet.vnu.edu.vn/toan-ai/bai-giang/gioi-thieu',
      currentHref
    )
    assert.deepEqual(noHash, { isMatch: false, part: null })
  })

  test('handles invalid or empty inputs safely', () => {
    assert.deepEqual(isSamePageLectureLink(null, currentHref), { isMatch: false, part: null })
    assert.deepEqual(isSamePageLectureLink('', currentHref), { isMatch: false, part: null })
    assert.deepEqual(isSamePageLectureLink('#slides', null), { isMatch: false, part: null })
  })
})

describe('tab-service: shouldIgnoreNavigationClick', () => {
  test('returns true when keyboard modifiers are pressed', () => {
    assert.equal(shouldIgnoreNavigationClick({ ctrlKey: true }), true)
    assert.equal(shouldIgnoreNavigationClick({ metaKey: true }), true)
    assert.equal(shouldIgnoreNavigationClick({ shiftKey: true }), true)
    assert.equal(shouldIgnoreNavigationClick({ altKey: true }), true)
  })

  test('returns true for non-primary mouse button clicks', () => {
    assert.equal(shouldIgnoreNavigationClick({ button: 1 }), true) // middle click
    assert.equal(shouldIgnoreNavigationClick({ button: 2 }), true) // right click
  })

  test('returns false for normal primary click without modifiers', () => {
    assert.equal(shouldIgnoreNavigationClick({ button: 0, ctrlKey: false, metaKey: false, shiftKey: false, altKey: false }), false)
    assert.equal(shouldIgnoreNavigationClick({}), false)
  })

  test('returns false for null/undefined event', () => {
    assert.equal(shouldIgnoreNavigationClick(null), false)
    assert.equal(shouldIgnoreNavigationClick(undefined), false)
  })
})
