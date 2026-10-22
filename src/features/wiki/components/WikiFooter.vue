<script setup>
import { computed } from 'vue'
import { useData } from 'vitepress'
import { concepts } from '../../../../docs/.vitepress/concepts.mjs'
import { relatedConcepts } from '../../../../docs/.vitepress/wiki-content.mjs'
import { studyLink } from '../../../core/routing/links.js'
import { wikiJourneys } from '../data/atlas.mjs'
const {frontmatter}=useData(), id=computed(()=>frontmatter.value.wikiTerm)
const incoming=computed(()=>Object.entries(concepts).filter(([other])=>other!==id.value&&relatedConcepts(other).includes(id.value)))
const journey=computed(()=>wikiJourneys.find(item=>item.ids.includes(id.value)))
</script>
<template><aside v-if="id" class="wiki-backlinks"><nav v-if="journey" class="wiki-pathway" aria-label="Lộ trình đọc"><strong>{{ journey.title }}</strong><ol><li v-for="termId in journey.ids" :key="termId"><a :href="studyLink(`/wiki/${termId}`)" :aria-current="termId === id ? 'page' : undefined">{{ concepts[termId].name }}</a></li></ol></nav><section v-if="incoming.length"><h2>Các thuật ngữ dẫn tới bài này</h2><div class="wiki-backlink-list"><a v-for="[other,term] in incoming" :key="other" :href="studyLink(`/wiki/${other}`)">{{ term.name }}</a></div></section><a class="text-link" :href="studyLink('/wiki/')">← Khám phá Wiki</a></aside></template>
