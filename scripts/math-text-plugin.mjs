import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import { parseAst } from 'rollup/parseAst'
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
      const courseContent = /[/\\]src[/\\]content[/\\]courses[/\\].*\.mjs$/.test(file)
      const cheatsheetService = /[/\\]src[/\\]features[/\\]lecture[/\\]services[/\\]cheatsheet-service\.mjs$/.test(file)
      if (!courseContent && !cheatsheetService && !/[/\\](?:concepts|course-catalog|math-labels|cheatsheets|[\w-]+-(?:course|courses|foundations))\.mjs$/.test(file)) return
      const expressions = new Set()
      // Read string values from syntax, including raw templates and the small
      // pure string helpers used to wrap display formulas. Never execute a module.
      const ast = parseAst(source), helpers = new Map()
      function visit(node, action, parent) {
        if (!node || typeof node !== 'object') return
        if (node.type) action(node, parent)
        for (const value of Object.values(node)) {
          if (Array.isArray(value)) value.forEach(child => visit(child, action, node))
          else if (value && typeof value === 'object') visit(value, action, node)
        }
      }
      function stringValue(node, bindings = {}, rawTemplate = false) {
        if (!node) return undefined
        if (node.type === 'Literal' && typeof node.value === 'string') return node.value
        if (node.type === 'Identifier') return bindings[node.name]
        if (node.type === 'BinaryExpression' && node.operator === '+') {
          const left = stringValue(node.left, bindings), right = stringValue(node.right, bindings)
          return left === undefined || right === undefined ? undefined : left + right
        }
        if (node.type === 'TaggedTemplateExpression' && node.tag.type === 'MemberExpression'
            && node.tag.object.name === 'String' && node.tag.property.name === 'raw') {
          return stringValue(node.quasi, bindings, true)
        }
        if (node.type === 'TemplateLiteral') {
          let value = ''
          for (let i = 0; i < node.quasis.length; i++) {
            value += rawTemplate ? node.quasis[i].value.raw.replace(/\r\n?/g, '\n') : node.quasis[i].value.cooked
            if (i < node.expressions.length) {
              const part = stringValue(node.expressions[i], bindings)
              if (part === undefined) return undefined
              value += part
            }
          }
          return value
        }
        if (node.type === 'CallExpression' && node.callee.type === 'Identifier') {
          const helper = helpers.get(node.callee.name), argument = stringValue(node.arguments[0], bindings)
          if (helper && argument !== undefined) return stringValue(helper.body, {[helper.params[0].name]: argument})
        }
        return undefined
      }
      visit(ast, node => {
        if (node.type === 'VariableDeclarator' && node.id.type === 'Identifier'
            && node.init?.type === 'ArrowFunctionExpression' && node.init.params.length === 1
            && node.init.params[0].type === 'Identifier') helpers.set(node.id.name, node.init)
      })
      visit(ast, (node, parent) => {
        if (node.type === 'TemplateLiteral' && parent?.type === 'TaggedTemplateExpression') return
        const value = stringValue(node)
        if (value === undefined) return
        for (const segment of mathSegments(value)) if (segment.startsWith('$')) expressions.add(segment)
      })
      const rendered = Object.fromEntries([...expressions].map(expression => {
        let html = cache.get(expression)
        if (html === undefined) {
          try { html = expression.startsWith('$$') ? md.render(expression) : md.renderInline(expression) }
          catch (error) { throw new Error(`Cannot render math in ${file}: ${JSON.stringify(expression)}`, {cause:error}) }
        }
        if (/data-mjx-error|<merror/.test(html)) throw new Error(`Invalid math in ${file}: ${expression}`)
        cache.set(expression, html)
        return [expression, html]
      }))
      return { code: `import { renderedMath as studyRenderedMath } from 'virtual:study-math-renderer';\n${source}\nObject.assign(studyRenderedMath, ${JSON.stringify(rendered)});`, map: null }
    }
  }
}
