import { staticMathPlugin } from '../static-math-plugin.mjs'
import { termLinks } from '../../docs/.vitepress/term-links.mjs'
import { physicsImageLabels } from '../../docs/.vitepress/physics-image-labels.mjs'

export function configureStudyMarkdown(md, { base }) {
      md.use(staticMathPlugin)
      md.core.ruler.before('block', 'normalize_custom_containers', state => {
        state.src = state.src
          .replace(/^## Tự kiểm tra$/gm, '## Câu hỏi ôn lại')
          // A container title ends on the same line; never consume the next paragraph.
          .replace(/^[ \t]*::: example(?:[\t ]+(.*))?$/gm, (_, title) => `::: info Ví dụ${title ? `: ${title}` : ''}`)
          .replace(/^[ \t]*::: proof(?:[\t ]+(.*))?$/gm, (_, title) => `::: details Chứng minh${title ? `: ${title}` : ''}`)
          .replace(/^[ \t]*::: exercise(?:[\t ]+(.*))?$/gm, (_, title) => `::: warning Bài tập${title ? `: ${title}` : ''}`)
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
      // Only standalone images become figures; escape alt text before inserting captions.
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
            token.content = `<figcaption>${md.utils.escapeHtml(caption)}${labels?`<div class="figure-labels"><span>Chú thích:</span><ul class="figure-label-list">${labels}</ul></div>`:''}</figcaption>`
            state.tokens[i].children.push(token)
          }
        }
      })
    }
