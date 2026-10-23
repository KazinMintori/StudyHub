import { ref, nextTick, onUnmounted } from 'vue'
import { captureFeedbackContext, buildFeedbackIssueUrl } from '../services/feedback.mjs'

export function useFeedback(getPageContext) {
  const dialog = ref(null)
  const trigger = ref(null)
  const descriptionInput = ref(null)
  const category = ref('content')
  const description = ref('')
  const context = ref(null)
  const error = ref('')
  let previousOverflow

  async function show() {
    if (!dialog.value || dialog.value.open) return
    context.value = captureFeedbackContext({ ...getPageContext(), href: window.location.href })
    error.value = ''
    previousOverflow = document.documentElement.style.overflow
    dialog.value.showModal()
    document.documentElement.style.overflow = 'hidden'
    await nextTick()
    descriptionInput.value?.focus({ preventScroll: true })
  }

  function close() { dialog.value?.close() }

  function restoreScroll() {
    if (previousOverflow === undefined) return
    document.documentElement.style.overflow = previousOverflow
    previousOverflow = undefined
  }

  function onClose() {
    restoreScroll()
    trigger.value?.focus({ preventScroll: true })
  }

  function submit() {
    error.value = ''
    try {
      const url = buildFeedbackIssueUrl({ category: category.value, description: description.value, context: context.value })
      // A native anchor avoids popup blockers and leaves the lesson and draft intact.
      const link = document.createElement('a')
      link.href = url
      link.target = '_blank'
      link.rel = 'noopener noreferrer'
      document.body.append(link)
      link.click()
      link.remove()
    } catch (cause) {
      error.value = cause.message
      nextTick(() => descriptionInput.value?.focus())
    }
  }

  function onBackdropClick(event) {
    if (event.target !== dialog.value) return
    const rect = dialog.value.getBoundingClientRect()
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) close()
  }

  onUnmounted(() => {
    dialog.value?.close()
    restoreScroll()
  })

  return { dialog, trigger, descriptionInput, category, description, context, error, show, close, onClose, submit, onBackdropClick }
}
