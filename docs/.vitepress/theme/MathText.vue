<script setup>
import { computed } from 'vue'
import { renderedMath } from 'virtual:study-math-renderer'
import { renderMathText } from '../math-text.mjs'
const props = defineProps({ text: { type: String, default: '' }, as: { type: String, default: 'span' } })
const html = computed(() => renderMathText(props.text, renderedMath))
</script>

<template><component :is="as" class="math-text" v-html="html" /></template>
