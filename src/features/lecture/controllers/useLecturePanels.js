import { foundationGroupsFor, panelHasContent } from '../services/panel-rules.mjs'
import { computed, ref, watch, onMounted, onUnmounted } from 'vue'
import { useLecture } from '../../navigation/index.mjs'
import { lectureSlides, lectureCheatsheet } from '../services/lecture-model.mjs'
import { getCourseLab } from '../../labs/services/course-labs.mjs'
import { concepts } from '../../../../docs/.vitepress/concepts.mjs'
import { studyLink } from '../../../core/routing/links.js'

export function useLecturePanels() {
  const { course, lesson, part } = useLecture()
  const cheatsheet = computed(() => lectureCheatsheet(course.value, lesson.value))
  const lab = computed(() => getCourseLab(course.value, lesson.value))
  const index = ref(0)
  const slides = computed(() => lectureSlides(course.value, lesson.value))
  const current = computed(() => slides.value[index.value])
  const foundationGroups = computed(() => foundationGroupsFor(lesson.value, concepts))
  const allFoundations = computed(() => foundationGroups.value.flatMap(group => group.ids))
  const hasPanelContent = computed(() => panelHasContent(course.value, lesson.value, part.value))
  function load() {
    index.value = 0
  }
  function next(direction) {
    index.value = Math.max(0, Math.min(slides.value.length - 1, index.value + direction))
  }
  function keyboard(event) {
    if (part.value !== 'slides' || /INPUT|TEXTAREA|SELECT/.test(event.target.tagName)) return
    if (event.key === 'ArrowRight') { event.preventDefault(); next(1) }
    if (event.key === 'ArrowLeft') { event.preventDefault(); next(-1) }
  }

  function printCheatsheet() {
    if (typeof window !== 'undefined') window.print()
  }

  function scrollToExercise(event) {
    if (event) event.preventDefault()
    const el = document.getElementById('bai-tap') || document.querySelector('.main > .vp-doc h2:last-of-type')
    if (el) el.scrollIntoView({ behavior: 'smooth' })
  }

  function selectNotes(event) {
    if (event) event.preventDefault()
    part.value = 'notes'
    if (typeof window !== 'undefined') {
      window.location.hash = '#notes'
    }
  }

  onMounted(() => { load(); window.addEventListener('keydown', keyboard) })
  onUnmounted(() => { window.removeEventListener('keydown', keyboard) })
  watch(() => lesson.value?.slug, load)

  return { course, lesson, part, cheatsheet, lab, index, slides, current, foundationGroups, allFoundations, hasPanelContent, load, next, keyboard, printCheatsheet, scrollToExercise, selectNotes, concepts, studyLink }
}
