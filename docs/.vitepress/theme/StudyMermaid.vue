<script setup>
import { ref, onMounted, onUnmounted, watch } from 'vue'
import { useData } from 'vitepress'
const props = defineProps({ graph: String, id: String, class: { type: String, default: 'mermaid' } })
const { isDark } = useData(), svg = ref(''), error = ref('')
let mounted = false, generation = 0
async function renderChart() {
  if (!mounted) return
  const version = ++generation
  const { renderStudyDiagram } = await import('./mermaid-render.js')
  try {
    const html = await renderStudyDiagram(decodeURIComponent(props.graph))
    if (mounted && version === generation) { svg.value = html; error.value = '' }
  } catch { if (mounted && version === generation) error.value = 'Không thể dựng sơ đồ. Tải lại trang để thử lại.' }
}
onMounted(() => { mounted = true; renderChart() })
onUnmounted(() => { mounted = false; generation++ })
watch([isDark, () => props.graph], renderChart)
</script>
<template><div :class="props.class"><p v-if="error" role="status">{{ error }}</p><div v-else v-html="svg"></div></div></template>
