/**
 * Font preload hint generator for StudyHub VitePress build.
 *
 * Inspects VitePress TransformContext.assets to discover actual emitted woff2
 * font files requested by CSS, bounded to above-the-fold normal-weight
 * Latin and Vietnamese subsets for Source Serif 4 and Be Vietnam Pro.
 */

export const PRELOAD_FONT_PATTERNS = [
  {
    name: 'source-serif-4-latin',
    regex: /source-serif-4-latin-standard-normal(?:\.[a-zA-Z0-9_-]+|-[a-zA-Z0-9_-]+)?\.woff2$/i
  },
  {
    name: 'source-serif-4-vietnamese',
    regex: /source-serif-4-vietnamese-standard-normal(?:\.[a-zA-Z0-9_-]+|-[a-zA-Z0-9_-]+)?\.woff2$/i
  },
  {
    name: 'be-vietnam-pro-latin-400',
    regex: /be-vietnam-pro-latin-400-normal(?:\.[a-zA-Z0-9_-]+|-[a-zA-Z0-9_-]+)?\.woff2$/i
  },
  {
    name: 'be-vietnam-pro-vietnamese-400',
    regex: /be-vietnam-pro-vietnamese-400-normal(?:\.[a-zA-Z0-9_-]+|-[a-zA-Z0-9_-]+)?\.woff2$/i
  }
]

/**
 * Filter and resolve emitted font asset paths matching the bounded preload set.
 *
 * @param {string[]} assets - List of emitted asset paths
 * @param {string} [base='/'] - Site base path
 * @returns {string[]} Matching asset paths
 */
export function resolveFontPreloadAssets(assets, base = '/') {
  if (!Array.isArray(assets) || assets.length === 0) {
    return []
  }

  const normalizedBase = base.endsWith('/') ? base : `${base}/`
  const selected = []
  const seenHrefs = new Set()

  for (const pattern of PRELOAD_FONT_PATTERNS) {
    const matched = assets.find(file => pattern.regex.test(file))
    if (!matched) continue

    let href = matched
    if (!href.startsWith('/') && !/^https?:\/\//i.test(href)) {
      href = `${normalizedBase}${href.replace(/^\.?\//, '')}`
    }

    if (!seenHrefs.has(href)) {
      seenHrefs.add(href)
      selected.push(href)
    }
  }

  return selected
}

/**
 * VitePress transformHead hook helper to inject bounded emitted-font preloads.
 *
 * @param {import('vitepress').TransformContext | string[]} context - VitePress transform context or asset list
 * @returns {import('vitepress').HeadConfig[]} Head tags for preloading
 */
export function generateFontPreloads(context) {
  const assets = Array.isArray(context) ? context : context?.assets
  if (!Array.isArray(assets) || assets.length === 0) {
    // In dev mode or when assets are not available, never manufacture fake URLs.
    return []
  }

  const base = context?.siteConfig?.site?.base || context?.siteData?.base || '/'
  const matchedHrefs = resolveFontPreloadAssets(assets, base)

  const existingPreloads = new Set(
    (context?.head || [])
      .filter(([tag, attrs]) => tag === 'link' && attrs?.rel === 'preload' && attrs?.as === 'font')
      .map(([_, attrs]) => attrs?.href)
  )

  const headConfigs = []
  for (const href of matchedHrefs) {
    if (existingPreloads.has(href)) continue

    headConfigs.push([
      'link',
      {
        rel: 'preload',
        href,
        as: 'font',
        type: 'font/woff2',
        crossorigin: ''
      }
    ])
  }

  return headConfigs
}
