// Inspect parser tokens, not pairs of dollar signs: List indentation can change
// the scope of a display formula even when the source has balanced delimiters.
export function* mathTokens(tokens) {
  for (const token of tokens) {
    if (token.type === 'math_block' || token.type === 'math_inline') yield token
    if (token.children) yield* mathTokens(token.children)
  }
}

export function swallowedMarkdown(token) {
  const content = token.content
  return (token.type === 'math_block' && !content.trim())
    || /(?:^|\n)\s*#{1,6}\s+\S/.test(content)
    || /(?:^|\n)\s*:::(?:\s|$)/.test(content)
    || /(?:^|\n)\s*\$\$\s*(?:\n|$)/.test(content)
    || content.split('\n').some(line => {
      const text = line.trim()
      return /^\p{L}[\p{L}\t ,.!?():;\-]{18,}$/u.test(text)
        && /\p{Ll}/u.test(text)
        && /(?:\p{L}{2,}[ \t]+){2,}\p{L}{2,}/u.test(text)
    })
}

export const mathRenderError = /data-mjx-error|data-mml-node\s*=\s*(?:&quot;|["'])merror|<merror\b/

export function physicsEquationTag(content, relativePath = '') {
  return /^vat-ly-[12]\//.test(relativePath.replaceAll('\\', '/'))
    ? content.match(/\\tag\{(\d+(?:\.\d+)*[a-zA-Z]?)\}/) : null
}

export function assertMathIntegrity(token, html, env = {}) {
  if (!swallowedMarkdown(token) && !mathRenderError.test(html)) return
  const file = env.relativePath || env.path || 'Markdown'
  const line = token.map ? `:${token.map[0] + 1}` : ''
  const reason = swallowedMarkdown(token) ? 'Empty formula or Markdown inside math' : 'MathJax rendering error'
  throw new Error(`${file}${line}: ${reason}. Check delimiters and list indentation.\n${token.content.slice(0, 240)}`)
}
