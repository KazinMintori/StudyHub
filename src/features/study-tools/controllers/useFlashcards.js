import { ref, computed, watch, onMounted, onUnmounted, toValue } from 'vue'
import { getStorage, writeStored } from '../../../core/storage/index.js'
import {
  filterCardsByCourse,
  getCardKey,
  countKnownCards,
  getCardByIndex,
  getNextCardIndex,
  recordCardReview,
  resetCardReviews
} from '../services/flashcardService.mjs'
import { cards as defaultCards } from '../data/flashcards.mjs'
import { normalizeWorkspaceCourse } from '../services/courseWorkspaceService.mjs'

export function useFlashcards(options = {}) {
  const allCards = options.cards || defaultCards
  const getCourses = () => options.courses || []

  const subject = ref('all')
  const index = ref(0)
  const revealed = ref(false)
  const remembered = ref({})
  let pendingReviews = {}

  const deck = computed(() => filterCardsByCourse(allCards, subject.value))
  const current = computed(() => getCardByIndex(deck.value, index.value))
  const knownCount = computed(() => countKnownCards(deck.value, remembered.value))

  const courseName = id => {
    const courses = getCourses()
    return courses.find(c => c.id === id)?.name || id
  }

  watch(subject, () => {
    index.value = 0
    revealed.value = false
  })

  watch(() => toValue(options.courseId), id => {
    if (id) subject.value = normalizeWorkspaceCourse(id, getCourses())
  }, { immediate: true, flush: 'sync' })

  function review(known) {
    if (!current.value) return
    // Read before modifying too: A storage event from another tab can still be
    // queued when the learner reviews a card or resets a course.
    remembered.value = recordCardReview(readReviews(), current.value, known)
    pendingReviews[getCardKey(current.value)] = Boolean(known)
    saveReviews()
    index.value = getNextCardIndex(index.value, 1, deck.value.length)
    revealed.value = false
  }

  function next(direction) {
    index.value = getNextCardIndex(index.value, direction, deck.value.length)
    revealed.value = false
  }

  function resetReview() {
    remembered.value = resetCardReviews(readReviews(), deck.value)
    for (const card of deck.value) pendingReviews[getCardKey(card)] = null
    saveReviews()
    index.value = 0
    revealed.value = false
  }

  function readReviews() {
    const storage = getStorage()
    if (!storage) return remembered.value
    try {
      const raw = storage.getItem('studyhub_flashcards')
      const reviews = raw === null ? {} : JSON.parse(raw) || {}
      // A quota error can leave older data readable. Keep only the unsaved
      // local changes on top so independent reviews from other tabs survive.
      for (const [key, value] of Object.entries(pendingReviews)) {
        if (value === null) delete reviews[key]
        else reviews[key] = value
      }
      return reviews
    } catch {
      return remembered.value
    }
  }

  function saveReviews() {
    if (writeStored('studyhub_flashcards', remembered.value)) pendingReviews = {}
  }

  function handleStorage(event) {
    if (event.storageArea && event.storageArea !== getStorage()) return
    if (event.key === 'studyhub_flashcards' || event.key === null) {
      if (event.newValue === null) pendingReviews = {}
      remembered.value = readReviews()
    }
  }

  onMounted(() => {
    remembered.value = readReviews()
    window.addEventListener('storage', handleStorage)
  })

  onUnmounted(() => {
    window.removeEventListener('storage', handleStorage)
  })

  return {
    subject,
    index,
    revealed,
    remembered,
    deck,
    current,
    knownCount,
    courseName,
    review,
    next,
    resetReview
  }
}
