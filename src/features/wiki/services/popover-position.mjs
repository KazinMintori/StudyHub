export function popoverPosition({ viewportWidth, viewportHeight, anchor, height = 280 }) {
  const gutter = viewportWidth < 640 ? 12 : 16
  const width = Math.min(360, viewportWidth - gutter * 2)
  if (viewportWidth < 640) return {
    left: `${gutter}px`, right: `${gutter}px`,
    bottom: `calc(${gutter}px + env(safe-area-inset-bottom, 0px))`
  }
  const top = Math.max(gutter, Math.min(anchor.top, viewportHeight - height - gutter))
  if (viewportWidth - anchor.right >= width + gutter * 2) return { width: `${width}px`, left: `${anchor.right + gutter}px`, top: `${top}px` }
  if (anchor.left >= width + gutter * 2) return { width: `${width}px`, left: `${anchor.left - width - gutter}px`, top: `${top}px` }
  const left = Math.max(gutter, Math.min(anchor.left, viewportWidth - width - gutter))
  return anchor.bottom + height + gutter <= viewportHeight
    ? { width: `${width}px`, left: `${left}px`, top: `${anchor.bottom + gutter}px` }
    : { width: `${width}px`, left: `${left}px`, bottom: `${viewportHeight - anchor.top + gutter}px` }
}
