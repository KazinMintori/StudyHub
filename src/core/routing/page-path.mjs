// Resolve a static page URL before adding the deployment base.
export function pagePath(path) {
  const [location, hash] = path.split('#')
  const queryIndex = location.indexOf('?')
  const pathname = queryIndex < 0 ? location : location.slice(0, queryIndex)
  const query = queryIndex < 0 ? '' : location.slice(queryIndex)
  const isAsset = /\.(png|jpe?g|svg|webp|ico|gif|pdf)$/i.test(pathname)
  const target = pathname.endsWith('/') || pathname.endsWith('.html') || isAsset ? pathname : `${pathname}.html`
  return target + query + (hash ? `#${hash}` : '')
}
