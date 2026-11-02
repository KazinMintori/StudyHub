import { readdir, readFile, mkdir, writeFile } from 'node:fs/promises'
import { join, relative } from 'node:path'
import { course } from '../../src/content/courses/toan-cho-ai/course.mjs'

const root = 'docs/toan-cho-ai/bai-giang'
async function walk(dir) {
  const entries = await readdir(dir, { withFileTypes: true })
  const groups = await Promise.all(entries.map(e => e.isDirectory() ? walk(join(dir, e.name)) : e.name.endsWith('.md') ? [join(dir, e.name)] : []))
  return groups.flat()
}
const files = await walk(root)
const pages = await Promise.all(files.map(async path => {
  const source = await readFile(path, 'utf8'), lines = source.split('\n')
  return { path: path.replaceAll('\\', '/'), lecture: source.match(/^lecture:\s*(.+)$/m)?.[1]?.trim(),
    sections: lines.flatMap((line, i) => /^#{2,3} /.test(line) ? [{ line: i + 1, title: line.replace(/^#+ /, '').trim() }] : []),
    labs: [...source.matchAll(/<([A-Z]\w*Lab)\b([^>]*)/g)].map(m => ({ component: m[1], props: m[2].trim() })),
    images: [...source.matchAll(/!\[([^\]]*)\]\(([^)]+)\)/g)].map(m => ({ alt: m[1], path: m[2] })) }
}))
const report = { note: 'Inventory only. A component count is not evidence of pedagogical or visual review.',
  lectures: course.lessons.map(l => ({ slug: l.slug, title: l.title, pages: pages.filter(p => p.lecture === l.slug) })),
  review: pages.filter(p => !course.lessons.some(l => l.slug === p.lecture)) }
const dir = 'raw_materials/toan-cho-ai/visual-review'
await mkdir(dir, { recursive: true })
await writeFile(join(dir, 'inventory.json'), JSON.stringify(report, null, 2) + '\n')
console.log(JSON.stringify({ lectures: report.lectures.length, pages: pages.length, sections: pages.reduce((n, p) => n + p.sections.length, 0), output: relative('.', join(dir, 'inventory.json')) }))
