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
  // VitePress removes frontmatter from included Markdown, but retains the
  // entry page's frontmatter for its own page-data parser.
  if (parents.length && path.extname(absolute) === '.md') {
    source = source.replace(/^\uFEFF?---\r?\n[\s\S]*?\r?\n(?:---|\.\.\.)(?:\r?\n|$)/, '')
  }
  for (const match of [...source.matchAll(/<!--\s*@include:\s*([^>]+?)\s*-->/g)]) {
    const target = path.resolve(path.dirname(absolute), match[1])
    const included = await readMarkdownIncludes(target, root, [...parents, absolute])
    // A replacement string interprets TeX's $$ and $& as substitutions.
    // Return the fragment from a callback so every character survives intact.
    source = source.replace(match[0], () => included)
  }
  return source
}
