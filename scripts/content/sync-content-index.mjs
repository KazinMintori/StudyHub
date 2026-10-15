import { readFile, writeFile, mkdir, access } from 'node:fs/promises'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { courseCatalog } from '../../src/content/catalog.mjs'

const root = fileURLToPath(new URL('../../', import.meta.url))
const relative = file => path.relative(root, file).replaceAll('\\', '/')
const exists = async file => { try { await access(file); return true } catch { return false } }

// Index canonical files and source spans rather than duplicate authored prose.
async function inspect(file, parents = [], publishedFile = file) {
  const absolute = path.resolve(file)
  const name = relative(absolute)
  if (name.startsWith('../') || path.isAbsolute(name)) throw new Error(`Content outside repository: ${name}`)
  if (parents.includes(absolute)) throw new Error(`Cyclic content include: ${name}`)
  const source = await readFile(absolute, 'utf8')
  const fragments = [], examples = [], exercises = [], solutions = [], assets = []
  const result = { fragments, examples, exercises, solutions, assets }
  const lines = source.split(/\r?\n/)
  let fence = false
  for (const [index, line] of lines.entries()) {
    if (/^\s*(```|~~~)/.test(line)) { fence = !fence; continue }
    if (fence) continue
    const container = line.match(/^\s*:::\s+(example|exercise|solution)\b(?:\s+(.*))?$/)
    if (container) {
      const type = { example: examples, exercise: exercises, solution: solutions }[container[1]]
      type.push({ source: name, line: index + 1, title: container[2] || '' })
    }
    const heading = line.match(/^#{2,6}\s+(Ví dụ|Bài tập|Lời giải)\b(.*)$/i)
    if (heading) {
      const type = /^Ví dụ/i.test(heading[1]) ? examples : /^Bài tập/i.test(heading[1]) ? exercises : solutions
      type.push({ source: name, line: index + 1, title: (heading[1] + heading[2]).trim() })
    }
    const references = [
      ...[...line.matchAll(/!\[[^\]]*\]\(<?([^\s)>]+)/g)].map(m => m[1]),
      ...[...line.matchAll(/<img\b[^>]*\bsrc=["']([^"']+)/g)].map(m => m[1])
    ]
    for (const reference of references) {
      const item = { reference, declaredIn: name, line: index + 1 }
      if (/^(https?:|data:|\/\/)/i.test(reference)) assets.push({ ...item, external: true })
      else {
        const url = decodeURIComponent(reference.split(/[?#]/)[0])
        const candidates = url.startsWith('/')
          ? [path.join(root, 'docs/public', url.slice(1)), path.join(root, 'docs', url.slice(1))]
          : [path.resolve(path.dirname(publishedFile), url)]
        let found = null
        for (const candidate of candidates) if (await exists(candidate)) { found = relative(candidate); break }
        assets.push({ ...item, source: found })
      }
    }
    const include = line.match(/<!--@include:\s*([^>]+?)\s*-->/)
    if (include) {
      const target = path.resolve(path.dirname(absolute), include[1])
      fragments.push(relative(target))
      const child = await inspect(target, [...parents, absolute], publishedFile)
      for (const key of Object.keys(result)) result[key].push(...child[key])
    }
  }
  return result
}

let count = 0
for (const course of courseCatalog) {
  for (const lesson of [...course.lessons, ...(course.review ? [course.review] : [])]) {
    const review = lesson.slug === course.review?.slug
    const notes = review
      ? `docs/${course.id}/on-luyen/tong-hop.md`
      : `docs/${course.id}/bai-giang/${lesson.slug}.md`
    const topics = (lesson.topicGroups || []).flatMap(group => group.topics).map(topic => ({
      slug: topic.slug,
      source: review ? `docs/${course.id}/on-luyen/${topic.slug}.md` : `docs/${course.id}/bai-giang/${lesson.slug}/${topic.slug}.md`
    }))
    const indexed = { fragments: [], examples: [], exercises: [], solutions: [], assets: [] }
    for (const source of [notes, ...topics.map(t => t.source)]) {
      if (!await exists(path.join(root, source))) throw new Error(`Missing lecture source: ${source}`)
      const item = await inspect(path.join(root, source))
      for (const key of Object.keys(indexed)) indexed[key].push(...item[key])
    }
    const manifest = {
      course: course.id, lecture: lesson.slug,
      route: review ? `/${course.id}/on-luyen/tong-hop` : `/${course.id}/bai-giang/${lesson.slug}`,
      notes, topics,
      slides: review ? 'docs/.vitepress/math-ai-review-course.mjs' : course.id.startsWith('vat-ly-') ? 'docs/.vitepress/physics-courses.mjs' : `src/content/courses/${course.id}/lectures/${lesson.slug}/slides.mjs`,
      cheatsheet: 'docs/.vitepress/cheatsheets.mjs',
      prerequisites: lesson.prerequisites || [],
      fragments: [...new Set(indexed.fragments)],
      examples: indexed.examples, exercises: indexed.exercises, solutions: indexed.solutions,
      assets: indexed.assets
    }
    const directory = path.join(root, 'src/content/courses', course.id, 'lectures', lesson.slug)
    await mkdir(directory, { recursive: true })
    await writeFile(path.join(directory, 'content.json'), JSON.stringify(manifest, null, 2) + '\n')
    count++
  }
}
console.log(`Indexed ${count} lecture/review bundles with canonical example, exercise and solution source spans.`)
