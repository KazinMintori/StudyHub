import { panelHasContent } from '../services/panel-rules.mjs'
import { computed, ref, shallowRef, watch, onBeforeUnmount } from 'vue'
import { useLecture } from '../../navigation/index.mjs'
import { selectLecturePart } from '../../navigation/controllers/use-lecture-navigation.mjs'
import { loadLecturePayload } from '../services/lecture-payload.mjs'
import { studyLink } from '../../../core/routing/links.js'

export function useLecturePanels() {
  const { course, lesson, part } = useLecture()
  // Panel data is loaded on demand: the server-rendered page only shows Notes.
  const payload = shallowRef(null)
  const payloadState = ref('idle')
  let requestId = 0
  async function ensurePayload() {
    const currentCourse = course.value, currentLesson = lesson.value
    if (!currentCourse || !currentLesson) return
    const id = ++requestId
    if (payload.value?.key !== `${currentCourse.id}/${currentLesson.slug}`) payloadState.value = 'loading'
    try {
      const data = await loadLecturePayload(currentCourse, currentLesson)
      if (id !== requestId) return
      payload.value = { key: `${currentCourse.id}/${currentLesson.slug}`, ...data }
      payloadState.value = 'ready'
    } catch (error) {
      if (id !== requestId) return
      console.error('[StudyHub] Không tải được dữ liệu bài giảng', error)
      payloadState.value = 'error'
    }
  }
  const currentPayload = computed(() => payload.value?.key === `${course.value?.id}/${lesson.value?.slug}` ? payload.value : null)
  const cheatsheet = computed(() => currentPayload.value?.cheatsheet ?? null)
  const lab = computed(() => currentPayload.value?.lab ?? null)
  const concepts = computed(() => currentPayload.value?.concepts ?? {})
  const foundationGroups = computed(() => currentPayload.value?.foundationGroups ?? [])
  const allFoundations = computed(() => foundationGroups.value.flatMap(group => group.ids))
  const hasPanelContent = computed(() => panelHasContent(course.value, lesson.value, part.value))
  const panelReady = computed(() => Boolean(currentPayload.value) && payloadState.value === 'ready')
  watch([hasPanelContent, () => course.value?.id, () => lesson.value?.slug], ([visible]) => {
    requestId++
    if (visible && !import.meta.env.SSR) ensurePayload()
  }, { immediate: true })
  onBeforeUnmount(() => { requestId++ })
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
    return selectLecturePart('notes')
  }


  return { course, lesson, part, payloadState, panelReady, retryPayload: ensurePayload, cheatsheet, lab, foundationGroups, allFoundations, hasPanelContent, printCheatsheet, scrollToExercise, selectNotes, concepts, studyLink }
}
