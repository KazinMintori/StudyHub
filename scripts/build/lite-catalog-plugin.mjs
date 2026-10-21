import path from 'node:path'
import { pathToFileURL, fileURLToPath } from 'node:url'
import { renderMathInStrings } from '../math-text-plugin.mjs'

// The course catalog is read by the layout on every page (sidebar state,
// headers, resume card). The real module also pulls every course module:
// slide decks and their pre-rendered MathJax SVG, about 5 MB of JavaScript.
// In the client build `src/content/catalog.mjs` becomes a JSON snapshot that
// keeps the navigation fields and drops the slide decks. Lecture panels load
// the full course module on demand (see lecture-payload.mjs).
//
// SSR, Node scripts and the dev server keep importing the real module.

const root = path.resolve(fileURLToPath(new URL('../../', import.meta.url)))
export const catalogFile = path.join(root, 'src/content/catalog.mjs')
// Course-level fields that only lecture panels read.
export const HEAVY_COURSE_FIELDS = ['slides']

export function liteCourse(course) {
  const copy = { ...course }
  for (const field of HEAVY_COURSE_FIELDS) delete copy[field]
  return copy
}

function collectStrings(value, into = []) {
  if (typeof value === 'string') into.push(value)
  else if (value && typeof value === 'object') for (const item of Object.values(value)) collectStrings(item, into)
  return into
}

export async function renderLiteCatalogModule() {
  // A fresh query string forces Node to re-evaluate the data after edits.
  const { courseCatalog } = await import(`${pathToFileURL(catalogFile).href}?lite=${Date.now()}`)
  const lite = courseCatalog.map(liteCourse)
  const math = renderMathInStrings(collectStrings(lite))
  return [
    Object.keys(math).length ? `import { renderedMath } from 'virtual:study-math-renderer'\nObject.assign(renderedMath, ${JSON.stringify(math)})` : '',
    `export const courseCatalog = JSON.parse(${JSON.stringify(JSON.stringify(lite))})`,
    'export const findCourse = id => courseCatalog.find(course => course.id === id)'
  ].join('\n')
}

export function liteCatalogPlugin() {
  let isBuild = false
  return {
    name: 'studyhub-lite-catalog',
    enforce: 'pre',
    configResolved(config) { isBuild = config.command === 'build' },
    load(id, options) {
      if (!isBuild || options?.ssr || id !== catalogFile) return null
      return renderLiteCatalogModule()
    }
  }
}
