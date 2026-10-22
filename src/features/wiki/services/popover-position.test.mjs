import test from 'node:test'
import assert from 'node:assert/strict'
import { popoverPosition, pinnedPreviewPosition } from './popover-position.mjs'

test('Mobile preview uses an inset bottom sheet rather than anchor coordinates', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 375, viewportHeight: 900, anchor: { top: 10, bottom: 20, left: 300, right: 350 } }), {
    left: '12px', right: '12px', bottom: 'calc(12px + env(safe-area-inset-bottom, 0px))'
  })
})
test('Desktop preview chooses the right side when enough space is available', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 1440, viewportHeight: 900, anchor: { top: 100, bottom: 125, left: 700, right: 800 } }), {
    width: '360px', left: '816px', top: '100px'
  })
})
test('Desktop preview switches to the left side near the right edge', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 1440, viewportHeight: 900, anchor: { top: 100, bottom: 125, left: 1000, right: 1200 } }), {
    width: '360px', left: '624px', top: '100px'
  })
})
test('A narrow desktop clamps horizontal position and places the preview above the anchor', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 640, viewportHeight: 600, anchor: { top: 350, bottom: 375, left: 280, right: 330 } }), {
    width: '360px', left: '264px', bottom: '266px'
  })
})

test('A pinned card becomes modal when the reading column leaves too little space', () => {
  const result = pinnedPreviewPosition({ viewportWidth: 1280, viewportHeight: 800, readingRect: { right: 1004, width: 676 } })
  assert.equal(result.modal, true)
  assert.equal(result.position.width, '360px')
})

test('A pinned card fits entirely beyond the article rather than covering its last words', () => {
  const result = pinnedPreviewPosition({ viewportWidth: 1440, viewportHeight: 900, readingRect: { right: 1136, width: 780 } })
  assert.equal(result.modal, false)
  assert.equal(parseFloat(result.position.left), 1152)
  assert.equal(parseFloat(result.position.left) + parseFloat(result.position.width), 1424)
})

test('Mobile pinned notes retain the inset bottom sheet', () => {
  const result = pinnedPreviewPosition({ viewportWidth: 375, viewportHeight: 800 })
  assert.equal(result.modal, true)
  assert.equal(result.position.left, '12px')
  assert.equal(result.position.right, '12px')
  assert.match(result.position.bottom, /safe-area-inset-bottom/)
})
