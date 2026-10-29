import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

let timestamps
export function applyCourseTimestamp(pageData) {
  if (pageData.frontmatter?.lastUpdated === false || pageData.frontmatter?.lastUpdated instanceof Date) return
  if (!timestamps) {
    try { timestamps = JSON.parse(readFileSync(fileURLToPath(new URL('../../.course-repositories/installed.json', import.meta.url)), 'utf8')).updatedAt || {} }
    catch { timestamps = {} }
  }
  const timestamp = timestamps[`docs/${pageData.relativePath}`]
  if (Number.isFinite(timestamp) && timestamp > 0) pageData.lastUpdated = timestamp
}
