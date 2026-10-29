export function cleanHeadingTitle(text) {
  if (typeof text !== 'string') return ''
  return text.replace(/\u200b/g, '').trim()
}

export function findActiveHeading(headings = [], maxTop = 160) {
  if (!Array.isArray(headings) || !headings.length) return null
  const visible = headings.filter(h => {
    if (!h) return false
    if (typeof h.getBoundingClientRect === 'function') {
      const bounds = h.getBoundingClientRect()
      // Hidden exercise panels and collapsed solutions have zero-height
      // headings at top=0; they are not the reader's current position.
      return bounds.top <= maxTop && (bounds.height == null || bounds.height > 0)
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
