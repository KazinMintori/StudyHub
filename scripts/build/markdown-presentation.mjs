import { staticMathPlugin } from '../static-math-plugin.mjs'
import { termLinks } from '../../docs/.vitepress/term-links.mjs'
import { physicsImageLabels } from '../../docs/.vitepress/physics-image-labels.mjs'
import { responsiveTablesPlugin } from './responsive-tables.mjs'
import { setupProofRenderer } from './proof-containers.mjs'
import { normalizeExerciseContainers, setupExerciseRenderer } from './exercise-containers.mjs'

const HTML_TOKEN_RE = /<!--[\s\S]*?(?:-->|$)|<script\b(?:[^>"']|"[^"]*"|'[^']*')*(?:\/>|>[\s\S]*?(?:<\/script\s*>|$))|<style\b(?:[^>"']|"[^"]*"|'[^']*')*(?:\/>|>[\s\S]*?(?:<\/style\s*>|$))|(<img\b)((?:[^>"']|"[^"]*"|'[^']*')*?)(\s*\/?>)/gi

export function hasExactAttribute(attrs, attrName) {
  if (!attrs) return false
  const re = /(?:^|\s+)([^\s"'=<>`/]+)(?:\s*=\s*(?:"[^"]*"|'[^']*'|[^\s"'=<>`]+))?/g
  let match
  while ((match = re.exec(attrs)) !== null) {
    if (match[1].toLowerCase() === attrName.toLowerCase()) {
      return true
    }
  }
  return false
}

export function injectHtmlImgAttributes(html, getLoadingAttrs) {
  if (typeof html !== 'string' || !html.includes('<')) {
    return html
  }
  return html.replace(HTML_TOKEN_RE, (match, tagPrefix, attrs, closing) => {
    if (match.startsWith('<!--') || /^<script\b/i.test(match) || /^<style\b/i.test(match)) {
      return match
    }
    const hasLoading = hasExactAttribute(attrs, 'loading')
    const hasDecoding = hasExactAttribute(attrs, 'decoding')
    const { loading, decoding } = getLoadingAttrs()
    let additions = ''
    if (!hasLoading && loading) additions += ` loading="${loading}"`
    if (!hasDecoding && decoding) additions += ` decoding="${decoding}"`
    return `${tagPrefix}${attrs}${additions}${closing}`
  })
}

function updateTagState(content, tagState) {
  if (!content) return
  const stripped = content.replace(/<!--[\s\S]*?(?:-->|$)/g, '')
  if (tagState.inScript) {
    if (/<\/script\s*>/i.test(stripped)) {
      tagState.inScript = false
    }
    return
  }
  if (tagState.inStyle) {
    if (/<\/style\s*>/i.test(stripped)) {
      tagState.inStyle = false
    }
    return
  }
  const scriptMatches = [...stripped.matchAll(/<script\b[\s\S]*?(?:<\/script\s*>|$)/gi)]
  for (const m of scriptMatches) {
    if (!/<\/script\s*>|\/>/i.test(m[0])) {
      tagState.inScript = true
      break
    }
  }
  const styleMatches = [...stripped.matchAll(/<style\b[\s\S]*?(?:<\/style\s*>|$)/gi)]
  for (const m of styleMatches) {
    if (!/<\/style\s*>|\/>/i.test(m[0])) {
      tagState.inStyle = true
      break
    }
  }
}

function renderFigureCaption(md, image, env) {
  const children = image.children || []
  const literalTypes = new Set(['text', 'html_inline', 'softbreak'])
  // Image alt content is already tokenized. Render only its math tokens, while
  // keeping all other caption content literal and HTML-escaped.
  if (!children.some(child => child.type === 'math_inline')
    || children.some(child => child.type !== 'math_inline' && !literalTypes.has(child.type))) {
    return md.utils.escapeHtml(image.content)
  }
  return children.map(child => {
    if (child.type === 'math_inline') return md.renderer.renderInline([child], md.options, env)
    if (child.type === 'softbreak') return ' '
    return md.utils.escapeHtml(child.content)
  }).join('')
}

export function configureStudyMarkdown(md, { base, vueBinding = true }) {
      md.use(responsiveTablesPlugin)
      md.use(staticMathPlugin, { vueBinding })
      setupExerciseRenderer(md)
      setupProofRenderer(md)
      md.core.ruler.before('block', 'normalize_custom_containers', state => {
        state.src = normalizeExerciseContainers(state.src)
        state.src = state.src
          .replace(/^## Tự kiểm tra$/gm, '## Câu hỏi ôn lại')
          // A container title ends on the same line; never consume the next paragraph.
          .replace(/^[ \t]*::: example(?:[\t ]+(.*))?$/gm, (_, title) => {
            const label = title?.trim()
            const heading = !label ? 'Ví dụ'
              : /^Ví dụ(?:\s|:|$)/u.test(label) ? label
              : /^\d+(?:\.\d+)*(?::|\s|$)/u.test(label) ? `Ví dụ ${label}`
              : `Ví dụ: ${label}`
            return `::: info ${heading}`
          })
          .replace(/^[ \t]*::: proof(?:[\t ]+(.*))?$/gm, (_, title) => {
            const label = title?.trim()
            return '::: details ' + (label && /^Chứng minh\b/u.test(label) ? label : 'Chứng minh' + (label ? ': ' + label : ''))
          })
          .replace(/^[ \t]*::: solution(?:[\t ]+(.*))?$/gm, (_, title) => {
            const label = title?.trim()
            const heading = label && /^Lời giải\b/i.test(label)
              ? label
              : `Lời giải${label ? `: ${label}` : ''}`
            return `::: details ${heading}`
          })
          .replace(/^[ \t]*::: derivation(?:[\t ]+(.*))?$/gm, (_, title) => `::: details Khai triển chi tiết${title ? `: ${title}` : ''}`)
          .replace(/^[ \t]*::: hint(?:[\t ]+(.*))?$/gm, (_, title) => `::: tip Gợi ý${title ? `: ${title}` : ''}`)
          .replace(/^[ \t]*::: note(?:[\t ]+(.*))?$/gm, (_, title) => `::: info${title ? ` ${title}` : ''}`)
          .replace(/^[ \t]*:::[ \t]*$/gm, ':::');
      });
      md.use(termLinks,base)
      // Only standalone images become figures; captions allow math, with literal escaped prose.
      md.core.ruler.after('inline', 'study_image_captions', state => {
        for (let i = 1; i < state.tokens.length - 1; i++) {
          const token = state.tokens[i]
          if (token.type !== 'inline' || state.tokens[i-1].type !== 'paragraph_open') continue
          const children = token.children?.filter(child => child.type !== 'text' || child.content.trim()) || []
          if (children.length !== 1 || children[0].type !== 'image') continue
          const image = children[0]
          const caption = image.content
          state.tokens[i-1].tag = 'figure'
          state.tokens[i-1].attrSet('class', 'lecture-figure')
          state.tokens[i+1].tag = 'figure'
          if (caption) {
            const token = new state.Token('html_inline', '', 0)
            const key=image.attrGet('src')?.match(/(young-\d+\/[^/.]+)\.(?:png|svg)$/)?.[1]
            const pairs=physicsImageLabels[key]||[]
            const labels=pairs.map(([vi,en])=>`<li>${md.utils.escapeHtml(vi)} (${md.utils.escapeHtml(en)})</li>`).join('')
            token.content = `<figcaption>${renderFigureCaption(md, image, state.env)}${labels?`<div class="figure-labels"><span>Chú thích:</span><ul class="figure-label-list">${labels}</ul></div>`:''}</figcaption>`
            state.tokens[i].children.push(token)
          }
        }
      })
      // Native image loading and decoding hints:
      // - First content image gets loading="eager" (promptly loaded, not deferred)
      // - Subsequent content images get loading="lazy"
      // - Default to decoding="async"
      // - Explicit attributes (loading/decoding) on tokens or HTML tags are strictly preserved
      // - Avoid eager-loading all figures: only the first content image is eager
      md.core.ruler.after('study_image_captions', 'study_image_loading', state => {
        let contentImageIndex = 0
        const nextAttrs = () => {
          const isFirst = contentImageIndex === 0
          contentImageIndex++
          return { loading: isFirst ? 'eager' : 'lazy', decoding: 'async' }
        }

        const tagState = { inScript: false, inStyle: false }

        for (const token of state.tokens) {
          if (token.type === 'inline' && token.children) {
            for (const child of token.children) {
              if (child.type === 'html_inline') {
                if (tagState.inScript || tagState.inStyle) {
                  updateTagState(child.content, tagState)
                  continue
                }
                if (/<img\b/i.test(child.content)) {
                  child.content = injectHtmlImgAttributes(child.content, nextAttrs)
                }
                updateTagState(child.content, tagState)
              } else if (child.type === 'image') {
                if (!tagState.inScript && !tagState.inStyle) {
                  const { loading, decoding } = nextAttrs()
                  if (child.attrGet('loading') === null) {
                    child.attrSet('loading', loading)
                  }
                  if (child.attrGet('decoding') === null) {
                    child.attrSet('decoding', decoding)
                  }
                }
              }
            }
          } else if (token.type === 'html_block') {
            if (tagState.inScript || tagState.inStyle) {
              updateTagState(token.content, tagState)
              continue
            }
            if (/<img\b/i.test(token.content)) {
              token.content = injectHtmlImgAttributes(token.content, nextAttrs)
            }
            updateTagState(token.content, tagState)
          }
        }
      })
    }
