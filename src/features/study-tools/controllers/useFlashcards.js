import { ref, computed, watch, onMounted } from 'vue'
import { readStored, writeStored } from '../../../core/storage/index.js'
import {
  filterCardsByCourse,
  countKnownCards,
  getCardByIndex,
  getNextCardIndex,
  recordCardReview,
  resetCardReviews
} from '../services/flashcardService.mjs'
import { cards as defaultCards } from '../data/flashcards.mjs'

export function useFlashcards(options = {}) {
  const allCards = options.cards || defaultCards
  const getCourses = () => options.courses || []

  const subject = ref('all')
  const index = ref(0)
  const revealed = ref(false)
  const remembered = ref({})

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

  function review(known) {
    if (!current.value) return
    remembered.value = recordCardReview(remembered.value, current.value, known)
    writeStored('studyhub_flashcards', remembered.value)
    index.value = getNextCardIndex(index.value, 1, deck.value.length)
    revealed.value = false
  }

  function next(direction) {
    index.value = getNextCardIndex(index.value, direction, deck.value.length)
    revealed.value = false
  }

  function resetReview() {
    remembered.value = resetCardReviews(remembered.value, deck.value)
    writeStored('studyhub_flashcards', remembered.value)
    index.value = 0
    revealed.value = false
  }

  onMounted(() => {
    remembered.value = readStored('studyhub_flashcards', {}) || {}
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
