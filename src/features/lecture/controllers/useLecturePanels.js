import { panelHasContent } from '../services/panel-rules.mjs'
import { computed, ref, shallowRef, watch } from 'vue'
import { useLecture } from '../../navigation/index.mjs'
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
  const cheatsheet = computed(() => payload.value?.cheatsheet ?? null)
  const lab = computed(() => payload.value?.lab ?? null)
  const concepts = computed(() => payload.value?.concepts ?? {})
  const foundationGroups = computed(() => payload.value?.foundationGroups ?? [])
  const allFoundations = computed(() => foundationGroups.value.flatMap(group => group.ids))
  const hasPanelContent = computed(() => panelHasContent(course.value, lesson.value, part.value))
  const panelReady = computed(() => payloadState.value === 'ready')
  watch([hasPanelContent, () => lesson.value?.slug], ([visible]) => { if (visible && !import.meta.env.SSR) ensurePayload() }, { immediate: true })
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


  return { course, lesson, part, payloadState, panelReady, retryPayload: ensurePayload, cheatsheet, lab, foundationGroups, allFoundations, hasPanelContent, printCheatsheet, scrollToExercise, selectNotes, concepts, studyLink }
}
