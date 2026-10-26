import test from 'node:test'
import assert from 'node:assert/strict'
import { createDragger, makeView, svgPoint } from '../../src/features/labs/controllers/svg-drag.js'

function event(pointerId, extras = {}) {
  return { pointerId, button: 0, preventDefault() { this.prevented = true }, ...extras }
}

function surface() {
  const captured = new Set()
  return {
    setPointerCapture(id) { captured.add(id) },
    hasPointerCapture: id => captured.has(id),
    releasePointerCapture(id) { captured.delete(id) },
    getScreenCTM: () => ({ inverse: () => ({ scale: 2 }) }),
    createSVGPoint: () => ({ x: 0, y: 0, matrixTransform(matrix) { return { x: this.x * matrix.scale, y: this.y * matrix.scale } } })
  }
}

test('SVG coordinate conversion accounts for a canvas scaled down on mobile', () => {
  const svg = surface()
  assert.deepEqual(svgPoint(svg, { clientX: 25, clientY: 35 }), { x: 50, y: 70 })
  assert.equal(svgPoint({ ...svg, getScreenCTM: () => null }, {}), null)
  assert.equal(svgPoint({ ...svg, getScreenCTM: () => ({ inverse() { throw new Error('Detached SVG') } }) }, {}), null)
})

test('only the captured primary pointer moves a point and other fingers cannot end its drag', () => {
  const svg = surface(), moves = []
  const view = { value: makeView({ x0: 0, x1: 10, y0: 0, y1: 10, width: 200, height: 200 }) }
  const drag = createDragger({ value: svg }, view, (...args) => moves.push(args))
  drag.start('first', event(7, { currentTarget: svg }))
  drag.start('second', event(8, { currentTarget: svg, isPrimary: false }))
  drag.move(event(8, { clientX: 40, clientY: 20 }))
  drag.end(event(8))
  assert.equal(moves.length, 0)
  assert.equal(svg.hasPointerCapture(7), true)
  drag.move(event(7, { clientX: 40, clientY: 20 }))
  assert.deepEqual(moves, [['first', [4, 8]]])
  drag.end(event(7))
  assert.equal(svg.hasPointerCapture(7), false)
  drag.move(event(7, { clientX: 50, clientY: 20 }))
  assert.equal(moves.length, 1)
})

test('secondary buttons and non-primary touches do not start drags or prevent page gestures', () => {
  const svg = surface(), moves = []
  const drag = createDragger({ value: svg }, { value: makeView({ x0: 0, x1: 10, y0: 0, y1: 10 }) }, (...args) => moves.push(args))
  for (const rejected of [event(1, { button: 2, currentTarget: svg }), event(2, { isPrimary: false, currentTarget: svg })]) {
    drag.start('point', rejected)
    drag.move({ ...rejected, clientX: 20, clientY: 30 })
    assert.equal(rejected.prevented, undefined)
  }
  assert.deepEqual(moves, [])
})

test('keyboard and direction buttons share snapping, bounds and the model constraint callback', () => {
  let position = [1, 2]
  const view = { value: makeView({ x0: 0, x1: 3, y0: 0, y1: 3.98 }) }
  // A fitting point may change its y coordinate while its x coordinate stays fixed.
  const drag = createDragger({ value: null }, view, (_, next) => { position = [position[0], next[1]] }, { step: .1, snap: .1 })
  drag.key('data-point', position, event(undefined, { key: 'ArrowRight' }))
  assert.deepEqual(position, [1, 2])
  drag.key('data-point', position, event(undefined, { key: 'ArrowUp' }))
  assert.deepEqual(position, [1, 2.1])
  drag.key('data-point', position, event(undefined, { key: 'ArrowUp', shiftKey: true }))
  assert.deepEqual(position, [1, 2.6])
  position = [1, 3.96]
  drag.key('data-point', position, event(undefined, { key: 'ArrowUp' }))
  assert.deepEqual(position, [1, 3.98])
  const unrelated = event(undefined, { key: 'Tab' })
  drag.key('data-point', position, unrelated)
  assert.equal(unrelated.prevented, undefined)
})
