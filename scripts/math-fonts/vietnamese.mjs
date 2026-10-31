import { TeXFont } from 'mathjax-full/js/output/svg/fonts/tex.js'
import glyphs from './source-serif-vietnamese.json' with { type: 'json' }

// MathJax's fallback measures unknown Unicode as generic browser text. That
// splits Vietnamese words and misplaces tone marks in server-rendered SVG.
// Supply paths and real advances only for missing glyphs, retaining TeX's
// existing symbols, accents, variants and layout metrics.
export function createVietnameseMathFont() {
  const font = new TeXFont()
  const additions = []
  for (const [variant, characters] of Object.entries(glyphs)) {
    const missing = {}
    for (const [code, metrics] of Object.entries(characters)) {
      const current = font.getChar(variant, Number(code))
      if (!current || current[3]?.unknown) {
        missing[code] = [...metrics.slice(0, 3), { ...metrics[3] }]
      }
    }
    additions.push([variant, missing])
  }
  for (const [variant, missing] of additions) font.defineChars(variant, missing)
  return font
}

export const vietnameseMathOptions = {
  svg: { font: createVietnameseMathFont() }
}
