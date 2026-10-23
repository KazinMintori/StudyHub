// Keep an initial heading link aligned while hydration, fonts and images change
// the article's height. User input always ends this short-lived correction.
export function stabilizeInitialHeading({
  browser = window,
  document = browser.document,
  getOffset,
  durationMs = 10000
}) {
  const initialUrl = browser.location.href
  let id
  try { id = decodeURIComponent(browser.location.hash.slice(1)) } catch { id = '' }
  if (!id) return { refresh() {}, stop() {} }

  let stopped = false
  let frame = 0
  let timeout
  const observer = new browser.ResizeObserver(schedule)
  const intentEvents = ['wheel', 'touchstart', 'pointerdown', 'keydown']

  function stop() {
    if (stopped) return
    stopped = true
    observer.disconnect()
    browser.cancelAnimationFrame(frame)
    browser.clearTimeout(timeout)
    for (const event of intentEvents) browser.removeEventListener(event, stop, true)
    browser.removeEventListener('hashchange', stop)
    browser.removeEventListener('resize', schedule)
    browser.removeEventListener('load', refresh)
    document.fonts?.removeEventListener('loadingdone', refresh)
  }

  function align() {
    if (stopped) return
    if (browser.location.href !== initialUrl) { stop(); return }
    const target = document.getElementById(id)
    if (!target?.matches('h2, h3, h4')) return
    const bounds = target.getBoundingClientRect()
    if (!bounds.width || !bounds.height) return
    const offset = getOffset()
    if (Math.abs(bounds.top - offset) > 1) {
      browser.scrollTo({ top: Math.max(0, browser.scrollY + bounds.top - offset), behavior: 'instant' })
    }
  }

  function schedule() {
    if (stopped || frame) return
    // Let Vue's DOM update and the resulting browser layout finish first.
    frame = browser.requestAnimationFrame(() => {
      frame = browser.requestAnimationFrame(() => { frame = 0; align() })
    })
  }

  function refresh() {
    if (stopped) return
    if (browser.location.href !== initialUrl) { stop(); return }
    observer.disconnect()
    const regions = new Set(document.querySelectorAll('.VPContent, .VPDoc, .main, .vp-doc'))
    const target = document.getElementById(id)
    if (target) regions.add(target)
    for (const element of regions) observer.observe(element)
    schedule()
  }

  for (const event of intentEvents) browser.addEventListener(event, stop, { capture: true, passive: true })
  browser.addEventListener('hashchange', stop)
  browser.addEventListener('resize', schedule)
  browser.addEventListener('load', refresh)
  document.fonts?.addEventListener('loadingdone', refresh)
  document.fonts?.ready.then(refresh)
  timeout = browser.setTimeout(stop, durationMs)
  refresh()
  return { refresh, stop }
}
