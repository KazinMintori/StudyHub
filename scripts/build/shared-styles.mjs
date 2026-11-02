import postcss from 'postcss'

// VitePress disables CSS splitting, so each independent build contains only
// the styles of its own pages. SPA navigation never loads another app.css.
// Publish their union on every page, keeping common rules only once and
// retaining scoped selectors, media queries, keyframes and relative URLs.
export function mergeStylesheets(sources) {
  const result = postcss.root()
  const seen = new Set()
  for (const source of sources) {
    const sheet = postcss.parse(source)
    const keys = []
    for (const node of [...sheet.nodes]) {
      const key = node.toString()
      keys.push(key)
      if (seen.has(key)) continue
      result.append(node)
    }
    // Only deduplicate between batches. Repeated declarations within one
    // stylesheet may intentionally restore an earlier cascade value.
    for (const key of keys) seen.add(key)
  }
  return result.toString()
}

const stylesheetLinks = /<link\b(?=[^>]*\brel="[^"]*\bstylesheet\b[^"]*")[^>]*\bhref="([^"]+)"[^>]*>/g

export function linkedStylesheets(html, files) {
  return [...html.matchAll(stylesheetLinks)].flatMap(([, href]) =>
    files.filter(file => href.endsWith('/' + file))
  )
}

export function replaceStylesheetLinks(html, files, shared) {
  return html.replace(stylesheetLinks, (link, href) => {
    const file = files.find(file => href.endsWith('/' + file))
    return file ? link.replace(href, href.slice(0, -file.length) + shared) : link
  })
}
