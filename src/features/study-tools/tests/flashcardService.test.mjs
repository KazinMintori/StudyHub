import test from 'node:test'
import assert from 'node:assert/strict'
import {
  getCardKey,
  filterCardsByCourse,
  countKnownCards,
  getCardByIndex,
  getNextCardIndex,
  recordCardReview,
  resetCardReviews,
  getLessonLink
} from '../services/flashcardService.mjs'

test('flashcardService: getCardKey generates correct composite key', () => {
  const card = { course: 'toan-cho-ai', q: 'Tập lồi là gì?' }
  assert.equal(getCardKey(card), 'toan-cho-ai:Tập lồi là gì?')
  assert.equal(getCardKey(null), '')
})

test('flashcardService: filterCardsByCourse filters correctly', () => {
  const sampleCards = [
    { course: 'toan-cho-ai', q: 'Q1' },
    { course: 'vat-ly-2', q: 'Q2' },
    { course: 'toan-cho-ai', q: 'Q3' }
  ]

  assert.equal(filterCardsByCourse(sampleCards, 'all').length, 3)
  assert.equal(filterCardsByCourse(sampleCards, '').length, 3)
  assert.equal(filterCardsByCourse(sampleCards, 'toan-cho-ai').length, 2)
  assert.equal(filterCardsByCourse(sampleCards, 'vat-ly-2').length, 1)
  assert.equal(filterCardsByCourse(sampleCards, 'non-existent').length, 0)
  assert.deepEqual(filterCardsByCourse(null, 'all'), [])
})

test('flashcardService: countKnownCards counts only remembered cards in deck', () => {
  const sampleCards = [
    { course: 'c1', q: 'Q1' },
    { course: 'c1', q: 'Q2' },
    { course: 'c2', q: 'Q3' }
  ]
  const remembered = {
    'c1:Q1': true,
    'c1:Q2': false,
    'c2:Q3': true
  }

  assert.equal(countKnownCards(sampleCards, remembered), 2)
  assert.equal(countKnownCards(sampleCards.slice(0, 2), remembered), 1)
  assert.equal(countKnownCards(sampleCards, {}), 0)
  assert.equal(countKnownCards(null, remembered), 0)
})

test('flashcardService: getCardByIndex handles circular index wrapping', () => {
  const sampleCards = [
    { course: 'c1', q: 'Q0' },
    { course: 'c1', q: 'Q1' },
    { course: 'c1', q: 'Q2' }
  ]

  assert.equal(getCardByIndex(sampleCards, 0)?.q, 'Q0')
  assert.equal(getCardByIndex(sampleCards, 2)?.q, 'Q2')
  assert.equal(getCardByIndex(sampleCards, 3)?.q, 'Q0')
  assert.equal(getCardByIndex(sampleCards, 5)?.q, 'Q2')
  assert.equal(getCardByIndex(sampleCards, -1)?.q, 'Q2')
  assert.equal(getCardByIndex([], 0), null)
})

test('flashcardService: getNextCardIndex wraps transitions forward and backward', () => {
  const total = 5

  // Forward transition
  assert.equal(getNextCardIndex(0, 1, total), 1)
  assert.equal(getNextCardIndex(4, 1, total), 0) // wraps to start

  // Backward transition
  assert.equal(getNextCardIndex(1, -1, total), 0)
  assert.equal(getNextCardIndex(0, -1, total), 4) // wraps to end

  // Boundary checks
  assert.equal(getNextCardIndex(0, 1, 0), 0)
  assert.equal(getNextCardIndex(0, -1, -1), 0)
})

test('flashcardService: recordCardReview updates review state immutably', () => {
  const initial = { 'c1:old': true }
  const card = { course: 'c1', q: 'new' }

  const updatedKnown = recordCardReview(initial, card, true)
  assert.equal(updatedKnown['c1:new'], true)
  assert.equal(updatedKnown['c1:old'], true)
  assert.equal(initial['c1:new'], undefined) // immutable

  const updatedUnknown = recordCardReview(initial, card, false)
  assert.equal(updatedUnknown['c1:new'], false)
})

test('flashcardService: resetCardReviews clears only target deck cards and preserves others', () => {
  const initial = {
    'toan-cho-ai:Q1': true,
    'toan-cho-ai:Q2': true,
    'vat-ly-2:Q3': true
  }

  const toanDeck = [
    { course: 'toan-cho-ai', q: 'Q1' },
    { course: 'toan-cho-ai', q: 'Q2' }
  ]

  const result = resetCardReviews(initial, toanDeck)
  assert.equal(result['toan-cho-ai:Q1'], undefined)
  assert.equal(result['toan-cho-ai:Q2'], undefined)
  assert.equal(result['vat-ly-2:Q3'], true) // preserved other course progress!
  assert.equal(initial['toan-cho-ai:Q1'], true) // immutable
})

test('flashcardService: getLessonLink builds correct note anchor or overview url', () => {
  const withLesson = { course: 'toan-cho-ai', lesson: 'bai-01-nhap-mon' }
  const withoutLesson = { course: 'vat-ly-2', lesson: '' }

  assert.equal(getLessonLink(withLesson), '/toan-cho-ai/bai-giang/bai-01-nhap-mon#notes')
  assert.equal(getLessonLink(withoutLesson), '/vat-ly-2/')
  assert.equal(getLessonLink(null), '/')
})
