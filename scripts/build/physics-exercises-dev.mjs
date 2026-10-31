import { readFile, stat } from 'node:fs/promises'
import { createHash } from 'node:crypto'
import { resolve } from 'node:path'
import { splitPhysicsExercises } from '../content/physics-exercise-groups.mjs'
import { physicsExerciseConfigs, physicsExerciseFiles, validatePhysicsExerciseIds } from '../content/physics-exercise-config.mjs'
import { vietnameseMathOptions } from '../math-fonts/vietnamese.mjs'

// Production publishes these JSON files during the cloud build. In development,
// render only the requested group, so a fresh checkout needs no full generation.
export function physicsExercisesDevPlugin({ base = '/', root = process.cwd() } = {}) {
  const chapters = new Map()
  let renderer
  async function chapterData(chapter) {
    const label = String(chapter).padStart(2, '0')
    const files = physicsExerciseFiles(chapter).map(([kind, file]) => ({
      kind, source: `raw_materials/physics/translations/chapter-${label}/${file}`
    }))
    const versions = await Promise.all(files.map(async file => {
      const info = await stat(resolve(root, file.source))
      return `${info.mtimeMs}:${info.size}`
    }))
    const version = versions.join('|')
    if (chapters.get(chapter)?.version === version) return chapters.get(chapter)
    const groups = [], sources = []
    for (const file of files) {
      const source = await readFile(resolve(root, file.source), 'utf8')
      sources.push({ file: file.source, sha256: createHash('sha256').update(source).digest('hex') })
      groups.push(...splitPhysicsExercises(source, { chapter, kind: file.kind, size: 6 }))
    }
    const total = validatePhysicsExerciseIds(chapter, groups)
    const data = { version, label, groups, sources, total, rendered: new Map() }
    chapters.set(chapter, data)
    return data
  }
  async function renderGroup(group, chapter) {
    if (!renderer) renderer = Promise.all([
      import('markdown-it'), import('markdown-it-mathjax3'), import('./markdown-presentation.mjs')
    ]).then(([{ default: MarkdownIt }, { default: mathjax }, { configureStudyMarkdown }]) => {
      const md = new MarkdownIt({ html: true }).use(mathjax, vietnameseMathOptions)
      configureStudyMarkdown(md, { base: '/', vueBinding: false })
      return md
    })
    const label = String(chapter).padStart(2, '0')
    const markdown = group.markdown.replace(new RegExp('(?:\\.\\./|\\./)img/young-' + label + '/', 'g'), `/vat-ly-1/bai-giang/img/young-${label}/`)
    const html = (await renderer).render(markdown, { relativePath: 'vat-ly-1/bai-giang/exercises.md' })
    if (/v-html=|data-mjx-error|<merror/.test(html)) throw new Error(`Invalid exercise math: ${group.id}`)
    return { id: group.id, title: group.title, ids: group.ids, html }
  }
  return {
    name: 'study-physics-exercises-dev', apply: 'serve',
    configureServer(server) {
      server.middlewares.use(async (request, response, next) => {
        let pathname
        try { pathname = new URL(request.url, 'http://localhost').pathname } catch { return next() }
        const prefix = base === '/' ? '' : base.replace(/\/$/, '')
        if (prefix && pathname.startsWith(prefix + '/')) pathname = pathname.slice(prefix.length)
        if (!pathname.startsWith('/physics-exercises/')) return next()
        const match = pathname.match(/^\/physics-exercises\/ch(\d{2})\/([a-zA-Z0-9_-]+)\.json$/)
        const chapter = Number(match?.[1])
        if (!match || !physicsExerciseConfigs[chapter]) {
          response.statusCode = 404
          return response.end('Exercise group not found')
        }
        try {
          const data = await chapterData(chapter), name = match[2]
          let payload
          if (name === 'index') payload = {
            chapter, sources: data.sources, total: data.total,
            groups: data.groups.map(({ markdown, ...group }) => group)
          }
          else {
            const group = data.groups.find(group => group.id === name)
            if (!group) { response.statusCode = 404; return response.end('Exercise group not found') }
            if (!data.rendered.has(name)) data.rendered.set(name, renderGroup(group, chapter))
            payload = await data.rendered.get(name)
          }
          response.setHeader('Content-Type', 'application/json; charset=utf-8')
          response.setHeader('Cache-Control', 'no-store')
          response.end(JSON.stringify(payload))
        } catch (error) {
          server.config?.logger?.error(error.message)
          response.statusCode = 500
          response.end('Cannot render exercise group')
        }
      })
    }
  }
}
