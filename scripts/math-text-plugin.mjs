import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import { mathSegments } from '../docs/.vitepress/math-text.mjs'

// Compile SVG and assistive MathML at build time, using the Notes renderer.
// Each data module carries only the expressions it uses.
export function mathTextPlugin() {
  const id = '\0study-math-renderer'
  const md = new MarkdownIt({ html: false }).use(mathjax)
  const cache = new Map()
  return {
    name: 'study-math-text',
    resolveId(source) { if (source === 'virtual:study-math-renderer') return id },
    load(source) { if (source === id) return 'export const renderedMath = {}' },
    transform(source, file) {
      // Course content can live in dedicated modules, including new subjects and cheatsheets.
      if (!/[/\\](?:concepts|course-catalog|math-labels|cheatsheets|[\w-]+-(?:course|courses|foundations))\.mjs$/.test(file)) return
      const expressions = new Set()
      for (const match of source.matchAll(/(['"])(?:\\.|(?!\1)[^\\])*?\1/g)) {
        const raw = match[0].slice(1, -1)
        const escapes = { '\\': '\\', n: '\n', r: '\r', t: '\t', "'": "'", '"': '"' }
        const value = raw.replace(/\\([\\nrt'"])/g, (_, character) => escapes[character])
        for (const segment of mathSegments(value)) if (segment.startsWith('$')) expressions.add(segment)
      }
      const rendered = Object.fromEntries([...expressions].map(expression => {
        const html = cache.get(expression) ?? (expression.startsWith('$$') ? md.render(expression) : md.renderInline(expression))
        if (/data-mjx-error|<merror/.test(html)) throw new Error(`Invalid math in ${file}: ${expression}`)
        cache.set(expression, html)
        return [expression, html]
      }))
      return { code: `import { renderedMath as studyRenderedMath } from 'virtual:study-math-renderer';\n${source}\nObject.assign(studyRenderedMath, ${JSON.stringify(rendered)});`, map: null }
    }
  }
}
