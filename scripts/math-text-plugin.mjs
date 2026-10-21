import MarkdownIt from 'markdown-it'
import mathjax from 'markdown-it-mathjax3'
import { parseAst } from 'rollup/parseAst'
import { mathSegments } from '../docs/.vitepress/math-text.mjs'

// Exports that only build scripts and server rendering read.
export const CLIENT_UNUSED_EXPORT = /WikiDetails$/

let sharedRenderer
// Render every `$…$` / `$$…$$` segment found in the given strings with the
// same MathJax setup as the data-module transform. Used by build-time modules
// that synthesise data (for example the lightweight client catalog).
export function renderMathInStrings(values) {
  sharedRenderer ??= new MarkdownIt({ html: false }).use(mathjax)
  const rendered = {}
  for (const value of values) {
    for (const segment of mathSegments(value)) {
      if (!segment.startsWith('$') || segment in rendered) continue
      const html = segment.startsWith('$$') ? sharedRenderer.render(segment) : sharedRenderer.renderInline(segment)
      if (/data-mjx-error|<merror/.test(html)) throw new Error(`Invalid math: ${segment}`)
      rendered[segment] = html
    }
  }
  return rendered
}

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
    transform(source, file, options) {
      // Wiki article bodies are rendered into Markdown pages at build time; the
      // browser never reads them from data modules, so the client bundle skips
      // their pre-rendered SVG.
      const browser = !options?.ssr
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
      function collect(root, into) {
        visit(root, (node, parent) => {
          if (node.type === 'TemplateLiteral' && parent?.type === 'TaggedTemplateExpression') return
          const value = stringValue(node)
          if (value === undefined) return
          for (const segment of mathSegments(value)) if (segment.startsWith('$')) into.add(segment)
        })
      }
      // Attach each exported constant's formulas to that export, so bundles
      // drop the pre-rendered SVG of exports they never import (for example
      // Wiki article bodies in the client build). Everything else stays in an
      // unconditional registration, exactly as before.
      const scoped = []
      for (const statement of ast.body) {
        const declaration = statement.type === 'ExportNamedDeclaration' ? statement.declaration : null
        if (declaration?.type !== 'VariableDeclaration' || declaration.kind !== 'const') { collect(statement, expressions); continue }
        for (const declarator of declaration.declarations) {
          if (!declarator.init) continue
          if (/FunctionExpression$/.test(declarator.init.type)) { collect(declarator.init, expressions); continue }
          const own = new Set()
          collect(declarator.init, own)
          scoped.push({ init: declarator.init, own, name: declarator.id.name })
        }
      }
      const render = expression => {
        let html = cache.get(expression)
        if (html === undefined) {
          try { html = expression.startsWith('$$') ? md.render(expression) : md.renderInline(expression) }
          catch (error) { throw new Error(`Cannot render math in ${file}: ${JSON.stringify(expression)}`, {cause:error}) }
        }
        if (/data-mjx-error|<merror/.test(html)) throw new Error(`Invalid math in ${file}: ${expression}`)
        cache.set(expression, html)
        return [expression, html]
      }
      // An object with spreads (`{...a, ...b}`) counts as a possible getter
      // side effect, so it is rewritten to the equivalent Object.assign call
      // that bundlers can drop when the export is unused.
      const objectSource = init => {
        if (init.type !== 'ObjectExpression' || !init.properties.some(property => property.type === 'SpreadElement')) return source.slice(init.start, init.end)
        const parts = []
        let group = []
        const flush = () => { if (group.length) parts.push(`{${group.join(',')}}`); group = [] }
        for (const property of init.properties) {
          if (property.type === 'SpreadElement') { flush(); parts.push(source.slice(property.argument.start, property.argument.end)) }
          else group.push(source.slice(property.start, property.end))
        }
        flush()
        return `Object.assign({}, ${parts.join(', ')})`
      }
      const edits = []
      for (const { init, own, name } of scoped) {
        const serverOnly = browser && CLIENT_UNUSED_EXPORT.test(name || '')
        const list = serverOnly ? [] : [...own].filter(expression => !expressions.has(expression))
        const spreads = init.type === 'ObjectExpression' && init.properties.some(property => property.type === 'SpreadElement')
        if (!list.length && !spreads) continue
        const math = list.length ? JSON.stringify(Object.fromEntries(list.map(render))) : '{}'
        edits.push([init.start, init.end, `/*#__PURE__*/__studyWithMath(${objectSource(init)}, ${math})`])
      }
      let code = source
      for (const [start, end, text] of edits.sort((a, b) => b[0] - a[0])) code = code.slice(0, start) + text + code.slice(end)
      code = `import { renderedMath as studyRenderedMath } from 'virtual:study-math-renderer';\nconst __studyWithMath = (value, math) => (Object.assign(studyRenderedMath, math), value);\n${code}`
      if (expressions.size) code += `\nObject.assign(studyRenderedMath, ${JSON.stringify(Object.fromEntries([...expressions].map(render)))});`
      return { code, map: null }
    }
  }
}
