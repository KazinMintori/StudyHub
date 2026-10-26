import { ref, onMounted, onUnmounted } from 'vue'
import {
  DEFAULT_WORKSPACE_TABS,
  isValidTab,
  parseTabFromHash,
  formatTabHash
} from '../services/workspaceService.mjs'

export function useWorkspaceTabs(initialTabs = DEFAULT_WORKSPACE_TABS) {
  const tabs = initialTabs
  const active = ref(tabs[0]?.id || 'flashcards')

  function changeTab(id) {
    if (!isValidTab(id, tabs)) return
    active.value = id
    if (typeof window !== 'undefined' && window.history?.replaceState) {
      window.history.replaceState(window.history.state, '', formatTabHash(id))
    }
  }

  function syncHash() {
    if (typeof window === 'undefined') return
    const id = parseTabFromHash(window.location.hash, tabs, active.value)
    active.value = id
  }

  onMounted(() => {
    syncHash()
    if (typeof window !== 'undefined') {
      window.addEventListener('hashchange', syncHash)
      window.addEventListener('popstate', syncHash)
    }
  })

  onUnmounted(() => {
    if (typeof window !== 'undefined') {
      window.removeEventListener('hashchange', syncHash)
      window.removeEventListener('popstate', syncHash)
    }
  })

  return {
    tabs,
    active,
    changeTab,
    syncHash
  }
}
