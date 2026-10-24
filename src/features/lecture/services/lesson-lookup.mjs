const normalize = value => String(value ?? '').normalize('NFD').replace(/\p{M}/gu, '').replace(/[đĐ]/g, 'd').toLowerCase()
const matches = (value, query) => normalize(query).trim().split(/\s+/).filter(Boolean).every(term => normalize(value).includes(term))

// An explicit id list keeps the initial results within the current lesson.
// Only the reader's Wiki action expands the search to the full dictionary.
export function lookupConcepts(concepts = {}, ids = [], query = '', { global = false } = {}) {
  if (global && !query.trim()) return []
  const keys = global ? Object.keys(concepts) : [...new Set(ids)]
  const result = keys.flatMap(id => {
    const term = concepts[id]
    return term && matches([term.name, ...(term.aliases || []), term.definition, term.use].join(' '), query)
      ? [{ id, ...term }] : []
  })
  if (!global) return result
  const needle = normalize(query).trim()
  const rank = term => {
    const names = [term.name, ...(term.aliases || [])].map(normalize)
    if (names.includes(needle)) return 0
    if (names.some(name => name.startsWith(needle))) return 1
    return matches(names.join(' '),query) ? 2 : 3
  }
  return result.sort((a,b) => rank(a)-rank(b))
}

export function lookupConnections(concepts = {}, ids = [], related = () => [], query = '') {
  const lessonIds = new Set(ids)
  return [...lessonIds].flatMap(id => {
    const term = concepts[id]
    if (!term) return []
    // relatedConcepts can fall back to a Wiki group, so ignore unknown ids.
    let links
    try { links = related(id) || [] } catch { links = [] }
    const targets = [...new Set(links)].filter(target => target !== id && lessonIds.has(target) && concepts[target])
    if (!targets.length || !matches([term.name, ...targets.map(target => concepts[target].name)].join(' '), query)) return []
    return [{ id, name: term.name, targets: targets.map(target => ({ id: target, name: concepts[target].name })) }]
  })
}

export function prioritizeLookupSections(sections = [], source = '') {
  const ordinal = label => {
    if (!/^\d+(?:\.\d+)?$/.test(label)) return null
    const [chapter, section = 0] = label.split('.').map(Number)
    return chapter * 1000 + section
  }
  const value = ordinal(source)
  if (value === null) return sections
  const relevant = section => {
    const bounds = String(section.badge ?? '').match(/\d+(?:\.\d+)?/g)?.map(ordinal) || []
    return bounds.length === 1 ? bounds[0] === value : bounds.length === 2 && value >= bounds[0] && value <= bounds[1]
  }
  return [...sections.filter(relevant), ...sections.filter(section => !relevant(section))]
}
