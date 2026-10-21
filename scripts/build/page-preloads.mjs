// VitePress preloads every dynamic import of the app chunk on every page. The
// Mermaid renderer (~700 kB) is such an import, so pages without a diagram
// would download it for nothing. Keep the hint only where a diagram exists.
const MERMAID_PRELOAD = /\s*<link rel="modulepreload" href="[^"]*\/chunks\/mermaid-render\.[\w-]+\.js">/g

export function dropUnusedPreloads(html) {
  if (/class="mermaid"/.test(html)) return html
  return html.replace(MERMAID_PRELOAD, '')
}
