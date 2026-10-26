import { isValidTab } from './workspaceService.mjs'

export function normalizeWorkspaceCourse(value, courses = []) {
  return typeof value === 'string' && courses.some(course => course.id === value) ? value : 'all'
}

export function parseWorkspaceCourse(search, courses = []) {
  if (typeof search !== 'string') return 'all'
  return normalizeWorkspaceCourse(new URLSearchParams(search).get('mon'), courses)
}

export function workspacePath(courseId = 'all', tab = 'flashcards', simulationId = '') {
  const specific = typeof courseId === 'string' && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(courseId) && !['all', 'general'].includes(courseId)
  const params = new URLSearchParams()
  if (specific) params.set('mon', courseId)
  if (typeof simulationId === 'string' && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(simulationId)) params.set('mo-phong', simulationId)
  const query = params.size ? `?${params}` : ''
  return `/goc-hoc-tap.html${query}#${isValidTab(tab) ? tab : 'flashcards'}`
}

export function studyPlanKey(courseId = 'all') {
  const safe = typeof courseId === 'string' && /^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(courseId) && courseId !== 'all' ? courseId : 'general'
  return `studyhub_plan_${safe}`
}

export function normalizeStudyTasks(raw) {
  if (!Array.isArray(raw)) return []
  const ids = new Set(), tasks = []
  for (const item of raw) {
    if (!item || typeof item !== 'object' || typeof item.id !== 'string' || typeof item.text !== 'string') continue
    const id = item.id.trim(), text = item.text.trim().slice(0, 300)
    if (!id || id.length > 80 || !text || ids.has(id)) continue
    ids.add(id)
    tasks.push({ id, text, done: item.done === true })
    if (tasks.length === 100) break
  }
  return tasks
}
