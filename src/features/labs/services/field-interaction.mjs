export const FIELD_BOUNDS = Object.freeze({ minX: 20, maxX: 720, minY: 20, maxY: 340, separation: 36 })

// All input methods share the same bounds and charge separation rule.
export function resolveChargePosition(charges, index, x, y) {
  if (!charges[index] || !Number.isFinite(x) || !Number.isFinite(y)) return null
  const position = {
    x: Math.max(FIELD_BOUNDS.minX, Math.min(FIELD_BOUNDS.maxX, Math.round(x))),
    y: Math.max(FIELD_BOUNDS.minY, Math.min(FIELD_BOUNDS.maxY, Math.round(y)))
  }
  if (charges.some((charge, other) => other !== index && Math.hypot(charge.x - position.x, charge.y - position.y) < FIELD_BOUNDS.separation)) return null
  return position
}

export function chargeHitRadius(canvasWidth) {
  const width = Number.isFinite(canvasWidth) && canvasWidth > 0 ? canvasWidth : 740
  // Aim for 48px so the canvas border and pixel rounding retain a 44px target.
  return Math.max(23, 24 * 740 / width)
}
