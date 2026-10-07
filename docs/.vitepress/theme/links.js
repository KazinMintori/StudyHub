import { withBase } from 'vitepress'

// Match VitePress's default .html URLs so direct links also work on simple static servers.
export function studyLink(path) {
  const [pathname, hash] = path.split('#')
  const target = pathname.endsWith('/') || pathname.endsWith('.html') ? pathname : `${pathname}.html`
  return withBase(target) + (hash ? `#${hash}` : '')
}
