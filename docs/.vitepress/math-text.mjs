// Shared delimiters for authored mathematical text; prose is always escaped.
export const mathSegments = source => String(source ?? '').split(/(\$\$[\s\S]*?\$\$|\$[^$\n]+\$)/g)
export const escapeText = source => String(source).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#39;')
export function renderMathText(source, expressions) {
  return mathSegments(source).map(segment => {
    if (!segment.startsWith('$')) return escapeText(segment)
    return expressions[segment] ?? escapeText(segment)
  }).join('')
}
