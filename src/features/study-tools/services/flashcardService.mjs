/**
 * Pure domain service for flashcard operations.
 */

export function getCardKey(card) {
  if (!card) return ''
  return `${card.course}:${card.q}`
}

export function filterCardsByCourse(cards = [], courseId = 'all') {
  if (!Array.isArray(cards)) return []
  if (!courseId || courseId === 'all') return cards
  return cards.filter(card => card.course === courseId)
}

export function countKnownCards(cards = [], remembered = {}) {
  if (!Array.isArray(cards) || !remembered) return 0
  return cards.filter(card => Boolean(remembered[getCardKey(card)])).length
}

export function getCardByIndex(cards = [], index = 0) {
  if (!Array.isArray(cards) || cards.length === 0) return null
  const safeIndex = (((index % cards.length) + cards.length) % cards.length)
  return cards[safeIndex] || null
}

export function getNextCardIndex(currentIndex, direction, totalCount) {
  if (!Number.isFinite(totalCount) || totalCount <= 0) return 0
  const step = Number(direction) || 0
  const current = Number(currentIndex) || 0
  return (((current + step) % totalCount) + totalCount) % totalCount
}

export function recordCardReview(remembered = {}, card, isKnown) {
  if (!card) return { ...remembered }
  const key = getCardKey(card)
  return {
    ...remembered,
    [key]: Boolean(isKnown)
  }
}

export function resetCardReviews(remembered = {}, cards = []) {
  if (!remembered || typeof remembered !== 'object') return {}
  if (!Array.isArray(cards) || cards.length === 0) return { ...remembered }

  const keysToRemove = new Set(cards.map(getCardKey))
  const updated = {}
  for (const [key, value] of Object.entries(remembered)) {
    if (!keysToRemove.has(key)) {
      updated[key] = value
    }
  }
  return updated
}

export function getLessonLink(card) {
  if (!card) return '/'
  return card.lesson
    ? `/${card.course}/bai-giang/${card.lesson}#notes`
    : `/${card.course}/`
}
