export function normalizeVietnamese(text) {
  if (typeof text !== 'string') return ''
  return text
    .toLocaleLowerCase('vi')
    .normalize('NFD')
    .replace(/\p{M}/gu, '')
    .replace(/đ/g, 'd')
}

export function filterCourses(catalog = [], query = '') {
  const q = normalizeVietnamese(query)
  if (!q) return catalog
  return catalog.filter(course => {
    const target = normalizeVietnamese(`${course?.name || ''} ${course?.description || ''}`)
    return target.includes(q)
  })
}
