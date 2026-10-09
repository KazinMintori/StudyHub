import { findCourse } from './course-catalog.mjs'
import { concepts } from './concepts.mjs'
import { resolveConceptForCourse } from './wiki-content.mjs'
import { lectureConceptIds, findLecture } from './lecture-model.mjs'

const escape = text => text.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
export function termLinks(md) {
  md.core.ruler.after('inline', 'study_term_links', state => {
    const path = (state.env.relativePath || '').replaceAll('\\', '/')
    const course = findCourse(path.split('/')[0])
    const wikiId = path.startsWith('wiki/') ? path.slice(5).replace(/\.md$/, '') : null
    if (!wikiId && (!course || (!path.includes('/notes/') && !path.includes('/bai-giang/')) || path.endsWith('/index.md'))) return

    let allowedConceptIds = null
    if (course) {
      const parts = path.split('/')
      let lesson = null
      if (parts.length >= 4) {
        lesson = findLecture(course.id, parts[2])
      } else if (parts.length === 3) {
        lesson = findLecture(course.id, parts[2].replace(/\.md$/, ''))
      }
      if (lesson) {
        allowedConceptIds = new Set(lectureConceptIds(lesson))
      } else {
        allowedConceptIds = new Set(course.foundations || [])
      }
    }

    const aliases = new Map()
    const blockedAliases = new Set((wikiId && concepts[wikiId]?.aliases || []).map(alias => alias.toLocaleLowerCase('vi')))
    for (const [id, term] of Object.entries(concepts)) {
      if (id === wikiId) continue
      if (allowedConceptIds && !allowedConceptIds.has(id)) continue
      for (const alias of term.aliases) {
        const key = alias.toLocaleLowerCase('vi')
        if (blockedAliases.has(key)) continue
        aliases.set(key, [...(aliases.get(key) || []), id])
      }
    }
    if (!aliases.size) return
    const names = [...aliases.keys()].sort((a, b) => b.length - a.length)
    if (!names.length) return
    const pattern = new RegExp(`(?<![\\p{L}\\p{N}_])(?:${names.map(escape).join('|')})(?![\\p{L}\\p{N}_])`, 'giu')
    for (let i = 0; i < state.tokens.length; i++) {
      const inline = state.tokens[i]
      if (inline.type !== 'inline' || !inline.children || state.tokens[i - 1]?.type === 'heading_open') continue
      const seen = new Set(), output = []
      let linkDepth = 0, htmlLink = false
      for (const token of inline.children) {
        if (token.type === 'link_open') linkDepth++
        if (token.type === 'html_inline' && /<a\b/i.test(token.content)) htmlLink = true
        if (token.type !== 'text' || linkDepth || htmlLink || /https?:\/\//.test(token.content)) output.push(token)
        else {
          let cursor = 0
          for (const match of token.content.matchAll(pattern)) {
            const id = resolveConceptForCourse(aliases.get(match[0].toLocaleLowerCase('vi')), course?.id)
            if (!id || seen.has(id)) continue
            if (match.index > cursor) { const text = new state.Token('text', '', 0); text.content = token.content.slice(cursor, match.index); output.push(text) }
            const open = new state.Token('html_inline', '', 0)
            open.content = `<button type="button" class="study-term" data-term="${id}" data-wiki="/wiki/${id}.html" aria-haspopup="dialog" aria-expanded="false" aria-controls="study-term-preview">`
            const text = new state.Token('text', '', 0); text.content = match[0]
            const close = new state.Token('html_inline', '', 0); close.content = '</button>'
            output.push(open, text, close)
            cursor = match.index + match[0].length; seen.add(id)
          }
          if (cursor < token.content.length) { const text = new state.Token('text', '', 0); text.content = token.content.slice(cursor); output.push(text) }
        }
        if (token.type === 'link_close') linkDepth--
        if (token.type === 'html_inline' && /<\/a\s*>/i.test(token.content)) htmlLink = false
      }
      inline.children = output
    }
  })
}
