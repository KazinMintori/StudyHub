import { readFile, realpath, mkdir, copyFile } from 'node:fs/promises'
import path from 'node:path'
import { createHash } from 'node:crypto'

// Exercise HTML is fetched as JSON, so Vite cannot discover or rewrite its
// image references. Publish every referenced image explicitly before the index.
export async function publishPhysicsExerciseImages(html, { root = process.cwd() } = {}) {
  const directory = await realpath(root)
  const images = new Map()
  const pattern = /(<img\b[^>]*?\bsrc=)(["'])([^"']+)\2/gi
  for (const match of html.matchAll(pattern)) {
    const reference = match[3]
    if (images.has(reference)) continue
    if (!/^\/vat-ly-1\/bai-giang\/img\/young-\d{2}\/[a-zA-Z0-9_-]+\.(?:png|svg|webp|jpe?g)$/.test(reference)) {
      throw new Error('Unsupported exercise image path: ' + reference)
    }
    const source = await realpath(path.join(directory, 'docs', reference.slice(1)))
    const imageRoot = await realpath(path.join(directory, 'docs/vat-ly-1/bai-giang/img'))
    const relative = path.relative(imageRoot, source)
    if (relative.startsWith('..') || path.isAbsolute(relative)) throw new Error('Exercise image escapes its source directory')
    const bytes = await readFile(source)
    const sha256 = createHash('sha256').update(bytes).digest('hex')
    const publicPath = '/physics-exercises/assets/' + sha256.slice(0, 16) + '-' + path.basename(source)
    const destination = path.join(directory, 'docs/public', publicPath.slice(1))
    await mkdir(path.dirname(destination), { recursive: true })
    await copyFile(source, destination)
    images.set(reference, { source: path.relative(directory,source).replaceAll('\\','/'), publicPath, sha256 })
  }
  return {
    html: html.replace(pattern, (all, before, quote, reference) => before + quote + images.get(reference).publicPath + quote),
    images: [...images.values()]
  }
}
