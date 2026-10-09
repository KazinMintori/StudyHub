import { readFile } from 'node:fs/promises'
import path from 'node:path'

// Count the text students actually receive, including source-linked translations.
export async function readMarkdownIncludes(file, root = process.cwd(), parents = []) {
  const absolute = path.resolve(file)
  const relative = path.relative(path.resolve(root), absolute)
  if (relative === '..' || relative.startsWith('..' + path.sep) || path.isAbsolute(relative)) {
    throw new Error(`Markdown include outside repository: ${absolute}`)
  }
  if (parents.includes(absolute)) throw new Error(`Cyclic Markdown include: ${absolute}`)
  let source = await readFile(absolute, 'utf8')
  for (const match of [...source.matchAll(/<!--@include:\s*([^>]+?)\s*-->/g)]) {
    const target = path.resolve(path.dirname(absolute), match[1])
    const included = await readMarkdownIncludes(target, root, [...parents, absolute])
    source = source.replace(match[0], included)
  }
  return source
}
