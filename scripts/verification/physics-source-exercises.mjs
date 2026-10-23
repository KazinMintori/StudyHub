// PDF extraction can turn “+ (0.150 m)” into “10.150 m”. Only accept
// numbered prompt headings, never an arbitrary chapter-like decimal in prose.
export function numberedExerciseIds(source, chapter) {
  if (!Number.isInteger(chapter) || chapter < 1) throw new TypeError('Invalid chapter')
  const pattern = new RegExp(`^[\\t \\u00a0\\u2000-\\u200a]*${chapter}\\.(\\d{1,3})[\\t \\u00a0\\u2000-\\u200a]+(?=[•●]|[A-Z(])`, 'gm')
  return [...new Set([...source.matchAll(pattern)].map(m => Number(m[1])))].sort((a, b) => a - b)
}
