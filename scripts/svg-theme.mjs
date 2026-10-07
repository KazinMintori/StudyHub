import { readFileSync } from 'node:fs'
const tokens = readFileSync(new URL('../docs/.vitepress/theme/tokens.css', import.meta.url), 'utf8').split('.dark')[0]
const value = name => tokens.match(new RegExp(`--${name}:\\s*([^;]+)`))[1].trim()
// External SVGs cannot inherit page custom properties. Export the light print palette.
export function themePrintedSvg(svg) {
  return svg.replace(/#[\da-f]{6}\b/gi, hex => {
    const [r,g,b] = [1,3,5].map(i => parseInt(hex.slice(i,i+2),16))
    const light = (r+g+b)/3, saturation = Math.max(r,g,b)-Math.min(r,g,b)
    if (light>250) return value('paper')
    if (light>220) return value(saturation>18 ? 'tim-soft' : 'canvas')
    if (light>180) return value(saturation>18 ? 'tim-soft' : 'rule')
    if (saturation>35) return value('tim')
    return value(light>85 ? 'ink-3' : light>45 ? 'ink-2' : 'ink')
  }).replace(/font-size="([\d.]+)"/g, (_, size) => `font-size="${Math.max(14, Number(size))}"`)
    .replace(/font-size:\s*([\d.]+)px/g, (_, size) => `font-size: ${Math.max(14,Number(size))}px`)
    .replace(/font-weight="(?:550|650)"/g, 'font-weight="600"')
    .replace(/fill="url\(#([^)]+)\)"/g, (_, id) => `fill="${value(id.startsWith('soft') ? 'tim-soft' : 'tim')}"`)
}
