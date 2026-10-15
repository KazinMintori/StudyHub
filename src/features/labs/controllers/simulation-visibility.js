import { ref, watch, onMounted, onUnmounted } from 'vue'

// Observe the whole illustration, including simulations hidden by v-show tabs.
export function useSimulationVisibility(element, pause) {
  const visible = ref(false), reducedMotion = ref(false)
  let observer, media
  const motionChanged = () => { reducedMotion.value = media.matches; if (media.matches) pause() }
  const visibilityChanged = () => { if (document.hidden) pause() }
  onMounted(() => {
    media = window.matchMedia('(prefers-reduced-motion: reduce)')
    motionChanged()
    media.addEventListener('change', motionChanged)
    document.addEventListener('visibilitychange', visibilityChanged)
    observer = new IntersectionObserver(([entry]) => { visible.value = entry.isIntersecting })
    observer.observe(element.value.closest('figure, .field-simulation') || element.value)
  })
  watch(visible, value => { if (!value) pause() })
  onUnmounted(() => {
    pause()
    observer?.disconnect()
    media?.removeEventListener('change', motionChanged)
    document.removeEventListener('visibilitychange', visibilityChanged)
  })
  return { visible, reducedMotion }
}
