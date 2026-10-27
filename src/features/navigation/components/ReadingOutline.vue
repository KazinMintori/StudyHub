<script setup>
import { inject, ref, watch } from 'vue'
import { readingOutlineKey } from '../controllers/use-reading-outline.mjs'
import { lecturePart } from '../controllers/use-lecture-navigation.mjs'

defineProps({ dropdown: Boolean })
const { headings, active, navigate } = inject(readingOutlineKey)
const disclosure = ref(null)
function close() { if (disclosure.value) disclosure.value.open = false }
function select(id) { close(); navigate(id) }
watch(lecturePart, close)
</script>

<template>
  <component :is="dropdown ? 'details' : 'div'" ref="disclosure" :class="['reading-outline', { 'reading-outline-dropdown': dropdown }]" @keydown.esc="close">
    <summary v-if="dropdown">Mục lục</summary>
    <p v-else class="reading-outline-title">Mục lục</p>
    <nav aria-label="Mục lục phần đang đọc">
      <a v-for="heading in headings" :key="heading.id" :href="`#${encodeURIComponent(heading.id)}`" :class="{ nested: heading.level === 3 }" :aria-current="active === heading.id ? 'location' : undefined" @click.prevent.stop="select(heading.id)">{{ heading.title }}</a>
      <p v-if="!headings.length" class="small">Phần này chưa có đề mục.</p>
    </nav>
  </component>
</template>

<style scoped>
.reading-outline { font: var(--fs-small)/1.5 var(--font-ui); }
.reading-outline-title { margin: 0 0 var(--space-3); color: var(--ink); font-weight: 600; }
nav { display: grid; gap: var(--space-1); }
nav a { display: block; padding: var(--space-2) 0; color: var(--ink-3); text-decoration: none; overflow-wrap: anywhere; }
nav a.nested { padding-left: var(--space-3); }
nav a:hover, nav a[aria-current] { color: var(--tim); }
nav a[aria-current] { font-weight: 600; }
.reading-outline-dropdown { display: none; position: relative; margin-left: auto; }
summary { display: flex; align-items: center; gap: var(--space-2); min-height: 44px; padding-inline: var(--space-2); color: var(--tim); cursor: pointer; list-style: none; }
summary::-webkit-details-marker { display: none; }
summary::after { content: '⌄'; }
.reading-outline-dropdown[open] summary::after { content: '⌃'; }
.reading-outline-dropdown nav { position: absolute; right: 0; top: 100%; z-index: 35; width: min(360px, calc(100vw - 40px)); max-height: 55dvh; overflow-y: auto; overscroll-behavior: contain; padding: var(--space-3) var(--space-4); border: 1px solid var(--rule); border-radius: var(--radius); background: var(--paper); box-shadow: var(--shadow); }
.reading-outline-dropdown nav a { min-height: 44px; }
@media (max-width: 1279px) { .reading-outline-dropdown { display: block; } }
@media print { .reading-outline { display: none; } }
</style>
