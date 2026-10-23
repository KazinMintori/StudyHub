import test from 'node:test'
import assert from 'node:assert/strict'
import { popoverPosition } from './popover-position.mjs'

test('Mobile preview uses an inset bottom sheet rather than anchor coordinates', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 375, viewportHeight: 900, anchor: { top: 10, bottom: 20, left: 300, right: 350 } }), {
    left: '12px', right: '12px', bottom: 'calc(12px + env(safe-area-inset-bottom, 0px))'
  })
})
test('Desktop preview chooses the right side when enough space is available', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 1440, viewportHeight: 900, anchor: { top: 100, bottom: 125, left: 700, right: 800 } }), {
    width: '360px', maxHeight: 'min(420px, 72dvh, 868px)', left: '816px', top: '100px'
  })
})
test('Desktop preview switches to the left side near the right edge', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 1440, viewportHeight: 900, anchor: { top: 100, bottom: 125, left: 1000, right: 1200 } }), {
    width: '360px', maxHeight: 'min(420px, 72dvh, 868px)', left: '624px', top: '100px'
  })
})
test('A narrow desktop clamps horizontal position and places the preview above the anchor', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 640, viewportHeight: 600, anchor: { top: 350, bottom: 375, left: 280, right: 330 } }), {
    width: '360px', maxHeight: 'min(420px, 72dvh, 318px)', left: '264px', top: '54px'
  })
})

test('A tall tablet preview keeps its heading on screen when neither side has room', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 768, viewportHeight: 600, anchor: { top: 250, bottom: 275, left: 360, right: 410 }, height: 420 }), {
    width: '360px', maxHeight: 'min(420px, 72dvh, 293px)', left: '360px', top: '291px'
  })
})

test('A short viewport limits preview height while keeping a gutter at both edges', () => {
  assert.deepEqual(popoverPosition({ viewportWidth: 768, viewportHeight: 240, anchor: { top: 100, bottom: 125, left: 360, right: 410 }, height: 420 }), {
    width: '360px', maxHeight: 'min(420px, 72dvh, 83px)', left: '360px', top: '141px'
  })
})

test('Floating previews stay in the viewport at each placement branch and anchor edge', () => {
  for (const viewportWidth of [640, 768, 1440]) {
    for (const viewportHeight of [200, 600, 900]) {
      for (const height of [100, 280, 420, 1000]) {
        for (const top of [-10, 20, viewportHeight - 20]) {
          for (const left of [20, viewportWidth / 2, viewportWidth - 60]) {
            const anchor = { top, bottom: top + 20, left, right: left + 40 }
            const position = popoverPosition({ viewportWidth, viewportHeight, height, anchor })
            const maxHeight = Number(position.maxHeight.match(/, (\d+)px\)$/)[1])
            const previewHeight = Math.min(height, 420, viewportHeight * .72, maxHeight)
            assert.ok(parseFloat(position.top) >= 16)
            assert.ok(parseFloat(position.top) + previewHeight <= viewportHeight - 16)
            assert.ok(parseFloat(position.left) >= 16)
            assert.ok(parseFloat(position.left) + parseFloat(position.width) <= viewportWidth - 16)
            const overlapsAnchor = parseFloat(position.left) < anchor.right
              && parseFloat(position.left) + parseFloat(position.width) > anchor.left
              && parseFloat(position.top) < anchor.bottom
              && parseFloat(position.top) + previewHeight > anchor.top
            assert.equal(overlapsAnchor, false, 'A floating preview does not intercept clicks on its anchor')
          }
        }
      }
    }
  }
})
