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

/** A pinned note uses the reading gutter only when the whole card fits there. */
export function pinnedPreviewPosition({ viewportWidth, viewportHeight, readingRect }) {
  if (viewportWidth < 640) return {
    modal: true,
    position: { left: '12px', right: '12px', bottom: 'calc(12px + env(safe-area-inset-bottom, 0px))', maxHeight: 'min(440px, 70dvh)' }
  }
  const top = Math.min(80, Math.max(16, viewportHeight - 240))
  const available = readingRect ? viewportWidth - readingRect.right - 32 : 0
  if (viewportWidth >= 1280 && readingRect?.width > 0 && available >= 260) return {
    modal: false,
    position: { left: `${readingRect.right + 16}px`, top: `${top}px`, width: `${Math.min(296, available)}px`, maxHeight: `calc(100dvh - ${top + 16}px)` }
  }
  const width = Math.min(360, viewportWidth - 32)
  return {
    modal: true,
    position: { left: `${(viewportWidth - width) / 2}px`, top: `${top}px`, width: `${width}px`, maxHeight: `calc(100dvh - ${top + 16}px)` }
  }
}
