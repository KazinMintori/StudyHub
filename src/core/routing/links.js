import { withBase } from 'vitepress'
import { pagePath } from './page-path.mjs'

// Match VitePress's default .html URLs so direct links also work on simple static servers.
export function studyLink(path) {
  return withBase(pagePath(path))
}
