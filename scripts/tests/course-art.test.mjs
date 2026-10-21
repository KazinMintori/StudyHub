import test from 'node:test'
import assert from 'node:assert/strict'
import { courseCatalog } from '../../src/content/catalog.mjs'
import { resolveCourseArt, bellBars, samplePath, arrowBetween, COURSE_MOTIFS } from '../../src/features/illustrations/services/course-art.mjs'

const MOTIFS = new Set(['tree', 'contour', 'bell', 'table-chart', 'pendulum', 'field', 'network', 'structures', 'venn', 'book-spiral', 'books'])
const TONES = new Set(['tim', 'lam', 'hong', 'ngoc', 'cam', 'vang', 'xanh', 'do'])

test('every course has a known illustration motif and tone', () => {
  for (const course of courseCatalog) {
    const art = resolveCourseArt(course)
    assert(MOTIFS.has(art.motif), `${course.id}: ${art.motif}`)
    assert(TONES.has(art.tone), `${course.id}: ${art.tone}`)
    assert(COURSE_MOTIFS[course.id], `${course.id} should have its own illustration`)
  }
  assert.deepEqual(resolveCourseArt({ id: 'mon-moi', illustration: 'gradient' }), { motif: 'contour', tone: 'tim' })
  assert.deepEqual(resolveCourseArt(null), { motif: 'books', tone: 'tim' })
})

test('illustration geometry stays inside the 160 × 120 view box', () => {
  const bars = bellBars()
  assert.equal(bars.length, 9)
  for (const bar of bars) {
    assert(bar.x >= 0 && bar.x + bar.width <= 160)
    assert(bar.y >= 0 && bar.y + bar.height <= 120.01)
  }
  assert.equal(bars[4].height, Math.max(...bars.map(bar => bar.height)))
  const path = samplePath(x => 60 + 10 * Math.sin(x), 10, 150, 20)
  for (const [, x, y] of path.matchAll(/(-?[\d.]+),(-?[\d.]+)/g)) {
    assert(+x >= 0 && +x <= 160 && +y >= 0 && +y <= 120)
  }
  const arrow = arrowBetween({ x: 0, y: 0, r: 5 }, { x: 100, y: 0, r: 10 })
  assert.match(arrow.line, /^M7,0 L82\.5,0$/)
  assert.match(arrow.head, /^M88,0 /)
})
