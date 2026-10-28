import { ref, computed, nextTick, onUnmounted } from 'vue'
import { captureFeedbackContext, buildFeedbackIssueUrl, formatFeedbackText, hasFeedbackEndpoint, sendFeedback, validateFeedback } from '../services/feedback.mjs'

// status: 'idle' → 'sending' → 'sent', or 'fallback' when no direct channel works.
export function useFeedback(getPageContext) {
  const dialog = ref(null)
  const trigger = ref(null)
  const descriptionInput = ref(null)
  const category = ref('content')
  const description = ref('')
  const contact = ref('')
  const includePage = ref(true)
  const honeypot = ref('')
  const context = ref(null)
  const error = ref('')
  const status = ref('idle')
  const copied = ref(false)
  const fallbackReason = ref('')
  const canSendDirectly = hasFeedbackEndpoint()
  const issueUrl = computed(() => {
    try { return buildFeedbackIssueUrl(fields()) } catch { return '' }
  })
  let previousOverflow

  function fields() {
    return { category: category.value, description: description.value, contact: contact.value, context: context.value, includePage: includePage.value }
  }

  async function show() {
    if (!dialog.value || dialog.value.open) return
    context.value = captureFeedbackContext({ ...getPageContext(), href: window.location.href })
    error.value = ''
    if (status.value !== 'sending') status.value = 'idle'
    copied.value = false
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
    if (status.value === 'sent') reset()
    trigger.value?.focus({ preventScroll: true })
  }

  function reset() {
    description.value = ''
    contact.value = ''
    category.value = 'content'
    includePage.value = true
    status.value = 'idle'
    error.value = ''
    copied.value = false
  }

  async function writeAnother() {
    reset()
    await nextTick()
    descriptionInput.value?.focus()
  }

  async function submit() {
    error.value = ''
    copied.value = false
    try { validateFeedback(fields()) } catch (cause) {
      error.value = cause.message
      await nextTick()
      descriptionInput.value?.focus()
      return
    }
    // Bots fill every field; people never see this one.
    if (honeypot.value) { status.value = 'sent'; return }
    if (!canSendDirectly) {
      fallbackReason.value = 'Kênh gửi trực tiếp chưa sẵn sàng.'
      status.value = 'fallback'
      return
    }
    status.value = 'sending'
    try {
      await sendFeedback(fields())
      status.value = 'sent'
    } catch (cause) {
      fallbackReason.value = cause.message
      status.value = 'fallback'
    }
  }

  async function copyMessage() {
    const text = formatFeedbackText(fields())
    try {
      await navigator.clipboard.writeText(text)
    } catch {
      const area = document.createElement('textarea')
      area.value = text
      area.setAttribute('readonly', '')
      area.style.position = 'fixed'
      area.style.opacity = '0'
      dialog.value?.append(area)
      area.select()
      document.execCommand('copy')
      area.remove()
    }
    copied.value = true
  }

  function backToForm() {
    status.value = 'idle'
    nextTick(() => descriptionInput.value?.focus())
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

  return { dialog, trigger, descriptionInput, category, description, contact, includePage, honeypot, context, error, status, copied, fallbackReason, issueUrl, show, close, onClose, submit, copyMessage, backToForm, writeAnother, onBackdropClick }
}
