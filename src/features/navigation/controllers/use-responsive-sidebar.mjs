import { ref, onMounted, onUnmounted, nextTick } from 'vue'
import {
  NAVIGATION_BREAKPOINTS,
  NAVIGATION_SELECTORS
} from '../../../config/navigation.mjs'
import { evaluateResponsiveSidebar } from '../services/sidebar-service.mjs'

/**
 * Composable managing responsive sidebar desktop collapse preference,
 * matchMedia breakpoints, and mobile drawer focus restoration.
 */
export function useResponsiveSidebar() {
  const desktopSidebarCollapsed = ref(false)
  let sidebarBreakpoint
  let navigationBreakpoint

  function syncResponsiveNavigation() {
    if (typeof window === 'undefined' || typeof document === 'undefined') return

    const sidebarMatches = Boolean(sidebarBreakpoint?.matches)
    const navigationMatches = Boolean(navigationBreakpoint?.matches)
    const isSidebarOpen = Boolean(document.querySelector(NAVIGATION_SELECTORS.sidebarOpen))
    const isSidebarActiveElement = Boolean(
      document.querySelector(NAVIGATION_SELECTORS.sidebar)?.contains(document.activeElement)
    )

    const evaluation = evaluateResponsiveSidebar({
      sidebarMatches,
      navigationMatches,
      isSidebarOpen,
      desktopSidebarCollapsed: desktopSidebarCollapsed.value,
      isSidebarActiveElement
    })

    if (evaluation.shouldCloseDrawer) {
      // Close the actual DefaultTheme drawer so its modal state and scroll lock
      // are cleared. useSidebar() instances do not share their isOpen ref.
      document.querySelector(NAVIGATION_SELECTORS.backdrop)?.click()

      if (evaluation.shouldRestoreFocus) {
        nextTick(() => {
          document.querySelector(NAVIGATION_SELECTORS.sidebarToggle)?.focus({ preventScroll: true })
        })
      }
    }

    if (evaluation.shouldCloseNavHamburger) {
      document.querySelector(NAVIGATION_SELECTORS.navBarHamburgerExpanded)?.click()
    }
  }

  function toggleDesktopSidebar() {
    desktopSidebarCollapsed.value = !desktopSidebarCollapsed.value
  }

  onMounted(() => {
    if (typeof window === 'undefined') return
    sidebarBreakpoint = window.matchMedia(NAVIGATION_BREAKPOINTS.sidebar)
    navigationBreakpoint = window.matchMedia(NAVIGATION_BREAKPOINTS.navigation)
    sidebarBreakpoint.addEventListener('change', syncResponsiveNavigation)
    navigationBreakpoint.addEventListener('change', syncResponsiveNavigation)
  })

  onUnmounted(() => {
    sidebarBreakpoint?.removeEventListener('change', syncResponsiveNavigation)
    navigationBreakpoint?.removeEventListener('change', syncResponsiveNavigation)
  })

  return {
    desktopSidebarCollapsed,
    toggleDesktopSidebar,
    syncResponsiveNavigation
  }
}
