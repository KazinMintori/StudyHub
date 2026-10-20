// Recover authored figures/lists accidentally rendered as indented HTML code.
import { readFile, writeFile } from 'node:fs/promises'
import path from 'node:path'
import { pathToFileURL } from 'node:url'
import MarkdownIt from 'markdown-it'

const md = new MarkdownIt({ html: true })
const htmlLine = /^[\t ]{4,}<\/?(?:img|div|ul|ol|li|p|strong|em|span|figure|figcaption|table|thead|tbody|tr|td|th|a)(?=[\s/>])/i
const accidentalBlocks = source => md.parse(source, {}).filter(token => token.type === 'code_block' && /^\s*<\/?(?:img|ul|ol|li|div|p)\b/i.test(token.content)).length

export function cleanLectureHtml(source) {
  const lines = source.split(/\r?\n/)
  let fence = null
  let changedLines = 0
  for (let i = 0; i < lines.length; i++) {
    const marker = lines[i].trimStart().slice(0, 3)
    const isFence = marker === String.fromCharCode(96).repeat(3) || marker === '~~~'
    if (isFence) { fence = fence ? null : marker; continue }
    if (fence) continue
    if (htmlLine.test(lines[i])) {
      lines[i] = lines[i].trimStart()
      changedLines++
    }
  }
  let normalized = lines.join('\n')
  // A single HTML paragraph is otherwise opaque to Markdown math rendering.
  // Fence contents are protected a second time before paragraph conversion.
  const ticks = String.fromCharCode(96).repeat(3)
  const fencePattern = new RegExp('(^[\\t ]*' + ticks + '[^\\n]*\\n[\\s\\S]*?^[\\t ]*' + ticks + '[^\\n]*$)', 'gm')
  let mathParagraphs = 0
  normalized = normalized.split(fencePattern).map((piece, index) => {
    if (index % 2) return piece
    return piece.replace(/<p\b[^>]*>([\s\S]*?)<\/p>/gi, (original, inner) => {
      if (!/\$[^$\n]+\$/.test(inner)) return original
      mathParagraphs++
      const plain = inner.replace(/<[^>]+>/g, '').trim()
      if (/^(?:Hình|Bảng)\s+\d/.test(plain)) {
        return '\n<div class="lecture-caption">\n\n' + inner.trim() + '\n\n</div>\n'
      }
      return '\n\n' + inner.trim() + '\n\n'
    })
  }).join('')
  return { source: normalized, changedLines, mathParagraphs, before: accidentalBlocks(source), after: accidentalBlocks(normalized) }
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  const write = process.argv.includes('--write')
  for (const file of process.argv.slice(2).filter(arg => arg !== '--write')) {
    if (!/\/xac-suat-thong-ke\/bai-giang\/\d{2}-[^/]+\.md$/.test(path.resolve(file).replaceAll('\\', '/'))) throw Error('Outside XSTK Notes: ' + file)
    const original = await readFile(file, 'utf8')
    const result = cleanLectureHtml(original)
    if (write && original !== result.source) await writeFile(file, result.source)
    if (result.changedLines || result.mathParagraphs) console.log(JSON.stringify({ file, changedLines: result.changedLines, mathParagraphs: result.mathParagraphs, accidentalBefore: result.before, accidentalAfter: result.after }))
  }
}
