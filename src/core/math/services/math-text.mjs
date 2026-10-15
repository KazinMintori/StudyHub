// Preserve escaped currency signs while recognizing authored TeX delimiters.
export const mathSegments = source => String(source ?? '').split(/((?<!\\)\$\$[\s\S]*?(?<!\\)\$\$|(?<!\\)\$(?:\\[^\n]|[^$\\\n])*(?<!\\)\$)/g)
export const escapeText = source => String(source).replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;').replaceAll("'", '&#39;')
export function renderMathText(source, expressions) {
  return mathSegments(source).map(segment => {
    if (!segment.startsWith('$')) return escapeText(segment)
    return expressions[segment] ?? escapeText(segment)
  }).join('')
}
