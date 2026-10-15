export function cleanHeadingTitle(text) {
  if (typeof text !== 'string') return ''
  return text.replace(/\u200b/g, '').trim()
}

export function findActiveHeading(headings = [], maxTop = 160) {
  if (!Array.isArray(headings) || !headings.length) return null
  const visible = headings.filter(h => {
    if (!h) return false
    if (typeof h.getBoundingClientRect === 'function') {
      return h.getBoundingClientRect().top <= maxTop
    }
    if (typeof h.top === 'number') {
      return h.top <= maxTop
    }
    return false
  })
  return visible.length ? visible[visible.length - 1] : null
}

export function buildLastLessonPayload({
  previous = {},
  trackedPath = '',
  trackedTitle = '',
  headingId = '',
  headingTitle = ''
} = {}) {
  return {
    ...previous,
    path: trackedPath,
    title: trackedTitle,
    heading: headingId || '',
    headingTitle: headingTitle || ''
  }
}
