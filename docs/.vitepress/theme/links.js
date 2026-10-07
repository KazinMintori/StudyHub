import { withBase } from 'vitepress'

// Match VitePress's default .html URLs so direct links also work on simple static servers.
export function studyLink(path) {
  const [pathname, hash] = path.split('#')
  const isAsset = /\.(png|jpe?g|svg|webp|ico|gif|pdf)$/i.test(pathname)
  const target = pathname.endsWith('/') || pathname.endsWith('.html') || isAsset ? pathname : `${pathname}.html`
  return withBase(target) + (hash ? `#${hash}` : '')
}
