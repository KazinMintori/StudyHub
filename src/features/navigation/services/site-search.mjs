const normalize = text => String(text || '').normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/gi, 'd').toLowerCase()

export function buildSearchEntries(courses, concepts = {}) {
  return [
    ...courses.flatMap(course => [
      { title: course.name, context: 'Học phần', path: `/${course.id}/` },
      ...course.lessons.flatMap(lesson => [
        { title: lesson.title, context: course.name, path: `/${course.id}/bai-giang/${lesson.slug}` },
        ...(lesson.topicGroups || []).flatMap(group => group.topics.map(topic => ({
          title: topic.title, context: `${course.short || course.name} · ${lesson.title}`,
          path: `/${course.id}/bai-giang/${lesson.slug}/${topic.slug}`
        })))
      ])
    ]),
    ...Object.entries(concepts).map(([id, concept]) => ({ title: concept.name, context: 'Wiki thuật ngữ', keywords: (concept.aliases || []).join(' '), path: `/wiki/${id}` }))
  ].map(entry => ({ ...entry, searchable: normalize(`${entry.title} ${entry.context} ${entry.keywords || ''}`), normalizedTitle: normalize(entry.title) }))
}

export function searchEntries(entries, query, limit = 30) {
  const term = normalize(query).trim()
  if (!term) return []
  const words = term.split(/\s+/)
  return entries.filter(entry => words.every(word => entry.searchable.includes(word)))
    .sort((a, b) => {
      const score = entry => entry.normalizedTitle === term ? 3 : entry.normalizedTitle.startsWith(term) ? 2 : entry.normalizedTitle.includes(term) ? 1 : 0
      return score(b) - score(a)
    })
    .slice(0, limit)
}
