import { readFile, stat } from 'node:fs/promises'
import path from 'node:path'

// Count transcluded text too: a small chapter wrapper can contain hundreds of
// exercises. Each child process exits before the next batch starts.
export async function expandedMarkdownBytes(file, stack = new Set()) {
  const absolute = path.resolve(file)
  if (stack.has(absolute)) throw new Error(`Recursive Markdown include: ${absolute}`)
  const source = await readFile(absolute, 'utf8')
  const next = new Set(stack).add(absolute)
  let bytes = Buffer.byteLength(source)
  for (const match of source.matchAll(/<!--\s*@include:\s*(.*?)\s*-->/g)) {
    const include = match[1].replace(/\{[^{}]*\}$/, '').trim()
    bytes += await expandedMarkdownBytes(path.resolve(path.dirname(absolute), include), next)
  }
  return bytes
}

export function partitionPages(entries, { maxBytes = 768 * 1024, maxPages = 100 } = {}) {
  if (!(maxBytes > 0) || !Number.isInteger(maxPages) || maxPages < 1) throw new Error('Invalid batch limits')
  const batches = []
  let current = { pages: [], bytes: 0 }
  const seen = new Set()
  for (const { page, bytes } of entries) {
    if (seen.has(page) || !Number.isFinite(bytes) || bytes < 0) throw new Error(`Invalid or duplicate page: ${page}`)
    seen.add(page)
    if (current.pages.length && (current.bytes + bytes > maxBytes || current.pages.length >= maxPages)) {
      batches.push(current)
      current = { pages: [], bytes: 0 }
    }
    current.pages.push(page)
    current.bytes += bytes
  }
  if (current.pages.length) batches.push(current)
  return batches
}

export async function planBuild(siteConfig, options) {
  if (siteConfig.mpa || siteConfig.metaChunk || siteConfig.sitemap || siteConfig.site.themeConfig?.search?.provider === 'local') {
    throw new Error('Batched build needs an explicit integration for MPA, metaChunk, sitemap or local search')
  }
  const entries = []
  for (const page of [...siteConfig.pages].sort()) {
    // VitePress discovers real source pages; do not include its implicit 404.
    await stat(path.resolve(siteConfig.srcDir, page))
    entries.push({ page, bytes: await expandedMarkdownBytes(path.resolve(siteConfig.srcDir, page)) })
  }
  if (!entries.length) throw new Error('No source pages found')
  return {
    pages: entries.map(entry => entry.page),
    batches: partitionPages(entries, options),
    assetsDir: siteConfig.assetsDir,
    rewrites: siteConfig.rewrites.map
  }
}
