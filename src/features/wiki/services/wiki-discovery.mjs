import { mathSegments } from '../../../core/math/services/math-text.mjs'
export const normalizeWikiQuery = value => String(value ?? '').toLocaleLowerCase('vi').normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g, 'd').trim()
export function conceptSummary(definition) {
  const prose = String(definition ?? '').split(/\$\$|\n\n/)[0]
  let result = ''
  for (const segment of mathSegments(prose)) {
    if (result.length + segment.length <= 220) result += segment
    else {
      if (!segment.startsWith('$')) result += segment.slice(0, Math.max(0, 217 - result.length)).replace(/\s+\S*$/, '')
      return result.trimEnd() + '…'
    }
  }
  return result
}
export function matchesWikiQuery(term, query) {
  const normalized = normalizeWikiQuery(query)
  if (!normalized) return true
  const searchable = normalizeWikiQuery([term.name, ...(term.aliases || []), term.definition || '', term.field || '', term.idea || ''].join(' '))
  return normalized.split(/\s+/).every(part => searchable.includes(part))
}
export function conceptUsageIndex(catalog) {
  const counts = new Map()
  for (const course of catalog) for (const lesson of course.lessons || []) {
    for (const id of new Set([...(lesson.prerequisites || []), ...(lesson.supportingConcepts || [])])) counts.set(id, (counts.get(id) || 0) + 1)
  }
  return counts
}
