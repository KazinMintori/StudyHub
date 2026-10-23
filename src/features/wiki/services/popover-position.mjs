export function popoverPosition({ viewportWidth, viewportHeight, anchor, height = 280 }) {
  const gutter = viewportWidth < 640 ? 12 : 16
  const width = Math.min(360, viewportWidth - gutter * 2)
  if (viewportWidth < 640) return {
    left: `${gutter}px`, right: `${gutter}px`,
    bottom: `calc(${gutter}px + env(safe-area-inset-bottom, 0px))`
  }
  const availableHeight = Math.max(0, viewportHeight - gutter * 2)
  const previewHeight = Math.min(height, 420, viewportHeight * .72, availableHeight)
  const clampTop = (top, previewHeight) => Math.max(gutter, Math.min(top, viewportHeight - previewHeight - gutter))
  const sizeForHeight = availableHeight => ({ width: `${width}px`, maxHeight: `min(420px, 72dvh, ${availableHeight}px)` })
  const size = sizeForHeight(availableHeight)
  const top = clampTop(anchor.top, previewHeight)
  if (viewportWidth - anchor.right >= width + gutter * 2) return { ...size, left: `${anchor.right + gutter}px`, top: `${top}px` }
  if (anchor.left >= width + gutter * 2) return { ...size, left: `${anchor.left - width - gutter}px`, top: `${top}px` }
  const left = Math.max(gutter, Math.min(anchor.left, viewportWidth - width - gutter))
  const below = Math.max(0, viewportHeight - anchor.bottom - gutter * 2)
  const above = Math.max(0, anchor.top - gutter * 2)
  const placeBelow = previewHeight <= below || (previewHeight > above && below >= above)
  // Keep the anchor clickable when the preview needs to scroll on a short screen.
  const placementHeight = Math.min(availableHeight, placeBelow ? below : above)
  const visibleHeight = Math.min(previewHeight, placementHeight)
  const preferredTop = placeBelow ? anchor.bottom + gutter : anchor.top - visibleHeight - gutter
  return { ...sizeForHeight(placementHeight), left: `${left}px`, top: `${clampTop(preferredTop, visibleHeight)}px` }
}
