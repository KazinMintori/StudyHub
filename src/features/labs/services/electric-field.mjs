// Relative Coulomb field on a plane through equal point charges; k|q| = 1.
export function electricField(charges, x, y) {
  let ex = 0, ey = 0
  for (const c of charges) {
    const dx = x - c.x, dy = y - c.y, r = Math.max(12, Math.hypot(dx, dy))
    ex += c.q * dx / r ** 3
    ey += c.q * dy / r ** 3
  }
  return { ex, ey, magnitude: Math.hypot(ex, ey) }
}

export function fieldLines(charges) {
  if (!charges.length) return []
  const positive = charges.filter(c => c.q > 0)
  const seeds = positive.flatMap(c => Array.from({ length: 16 }, (_, i) => {
    const angle = i * Math.PI / 8
    return [c.x + 20 * Math.cos(angle), c.y + 20 * Math.sin(angle)]
  }))
  // With only negative charges, field lines enter from the boundary.
  if (!positive.length) {
    for (let x = 20; x < 740; x += 40) seeds.push([x, 2], [x, 358])
    for (let y = 20; y < 360; y += 40) seeds.push([2, y], [738, y])
  }
  return seeds.flatMap(([x, y]) => {
    const points = [[x, y]]
    for (let i = 0; i < 380; i++) {
      if (x < 1 || x > 739 || y < 1 || y > 359 || charges.some(c => Math.hypot(x - c.x, y - c.y) < 16)) break
      const { ex, ey, magnitude } = electricField(charges, x, y)
      if (magnitude < 1e-9) break
      // Normalize for readable spacing; this is a field line, not particle dynamics.
      x += 4 * ex / magnitude
      y += 4 * ey / magnitude
      points.push([x, y])
    }
    return points.length > 2 ? [points.map(([px, py], i) => `${i ? 'L' : 'M'}${px.toFixed(2)},${py.toFixed(2)}`).join(' ')] : []
  })
}
