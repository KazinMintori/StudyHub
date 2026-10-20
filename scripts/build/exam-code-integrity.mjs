import assert from 'node:assert/strict'
import MarkdownIt from 'markdown-it'

const markdown = new MarkdownIt()
const normalize = value => value.replace(/\r\n?/g, '\n').replace(/\n$/, '')
// Decode entities only: Markdown's full unescape would also modify regex backslashes.
export function htmlCodeText(value) {
  return value.replace(/<[^>]*>/g, '').replace(/&(?:#x[\da-f]+|#\d+|[a-z]+);/gi,
    entity => markdown.utils.unescapeAll(entity))
}
export function sourceCodeLiterals(text) {
  const inline = [], blocks = []
  function visit(tokens) {
    for (const token of tokens) {
      if (token.type === 'code_inline') inline.push(token.content)
      if (token.type === 'fence' || token.type === 'code_block') blocks.push(normalize(token.content))
      if (token.children) visit(token.children)
    }
  }
  visit(markdown.parse(text, {}))
  return { inline, blocks }
}
export function renderedCodeLiterals(html) {
  const blocks = [...html.matchAll(/<pre\b[^>]*>([\s\S]*?)<\/pre>/gi)].map(m => normalize(htmlCodeText(m[1])))
  const inline = [...html.replace(/<pre\b[^>]*>[\s\S]*?<\/pre>/gi, '').matchAll(/<code\b[^>]*>([\s\S]*?)<\/code>/gi)].map(m => htmlCodeText(m[1]))
  return { inline, blocks }
}
export function assertCodePreserved(source, rendered, label) {
  return assertCodeLiteralsPreserved(sourceCodeLiterals(source), rendered, label)
}
export function assertCodeLiteralsPreserved(expected, rendered, label) {
  const actual = renderedCodeLiterals(rendered)
  assert(!/&(?:quot|amp|lt|gt|apos|nbsp|#\d+|#x[\da-f]+),/i.test(rendered), `${label}: HTML entity terminator changed to comma`)
  assert(!/[<>]\s*,\s*=/.test(htmlCodeText(rendered)), `${label}: comma inserted into comparison operator`)
  assert.deepEqual(actual.blocks, expected.blocks, `${label}: exact fenced code and output`)
  for (const literal of expected.inline) {
    assert(actual.inline.includes(literal), `${label}: missing or altered inline code ${JSON.stringify(literal)}`)
  }
  return expected.inline.length + expected.blocks.length
}
