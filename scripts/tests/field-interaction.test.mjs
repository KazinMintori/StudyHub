import test from 'node:test'
import assert from 'node:assert/strict'
import { resolveChargePosition, chargeHitRadius } from '../../src/features/labs/services/field-interaction.mjs'

test('charge controls clamp to the plane and keep the same separation rule as dragging', () => {
  const charges = [{ x: 230, y: 180, q: 1 }, { x: 510, y: 180, q: -1 }]
  assert.deepEqual(resolveChargePosition(charges, 0, -100, 500), { x: 20, y: 340 })
  assert.deepEqual(resolveChargePosition(charges, 1, 900, -5), { x: 720, y: 20 })
  assert.equal(resolveChargePosition(charges, 0, 475, 180), null)
  assert.deepEqual(resolveChargePosition(charges, 0, 474, 180), { x: 474, y: 180 })
  assert.equal(resolveChargePosition(charges, 3, 200, 200), null)
  assert.equal(resolveChargePosition(charges, 0, NaN, 200), null)
  assert.deepEqual(charges[0], { x: 230, y: 180, q: 1 })
})

test('charge hit area remains at least 44 CSS pixels on small canvases', () => {
  for (const width of [280, 320, 335, 400, 740, 1000]) {
    assert(chargeHitRadius(width) * 2 * width / 740 >= 44 - 1e-9)
  }
  assert.equal(chargeHitRadius(0), 24)
})
