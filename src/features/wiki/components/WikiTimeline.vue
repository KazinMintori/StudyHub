<script setup>
import { wikiPeople } from '../data/atlas.mjs'
import { studyLink } from '../../../core/routing/links.js'
const milestones = [...wikiPeople].sort((a, b) => Number(a.year) - Number(b.year))
</script>
<template>
  <section class="wiki-timeline" aria-labelledby="wiki-timeline-heading">
    <header><p class="wiki-eyebrow">LỊCH SỬ CỦA NHỮNG CÂU HỎI</p><h3 id="wiki-timeline-heading">Những ý tưởng đi qua thời gian.</h3><p>Mỗi mốc là một công trình. Mở một cái tên để đọc ý tưởng đằng sau.</p></header>
    <ol><li v-for="person in milestones" :key="person.id"><a :href="studyLink(`/wiki/nhan-vat/${person.id}`)"><span class="wiki-timeline-year">{{ person.year }}</span><span class="wiki-timeline-node" aria-hidden="true"></span><strong>{{ person.name }}</strong><span>{{ person.field }}</span><span class="wiki-timeline-arrow" aria-hidden="true">↗</span></a></li></ol>
  </section>
</template>
<style scoped>
.wiki-timeline { margin: var(--space-6) 0; padding: clamp(20px, 3vw, 32px); border: 1px solid var(--rule); border-radius: var(--radius-xl); background: linear-gradient(125deg, var(--tim-soft), var(--paper) 70%); font-family: var(--font-ui); }
header h3 { margin: 0 0 var(--space-2); font: 550 clamp(23px, 2.5vw, 30px)/1.3 var(--font-read); color: var(--ink); }header > p:last-child { margin: 0; color: var(--ink-2); font-size: var(--fs-small); line-height: 1.7; }
ol { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); padding: 0; list-style: none; margin: var(--space-6) 0 0; }li { min-width: 0; }a { position: relative; display: flex; flex-direction: column; align-items: flex-start; color: var(--ink); text-decoration: none; padding: 0 var(--space-4) var(--space-4) 0; min-height: 160px; }a::before { content: ''; position: absolute; left: 0; right: 0; top: 44px; height: 1px; background: var(--control); opacity: .5; }li:last-child a::before { right: 80%; }
.wiki-timeline-year { font: 500 26px/1 var(--font-read); color: var(--tim); margin-bottom: 14px; font-variant-numeric: tabular-nums; }.wiki-timeline-node { display: block; position: relative; width: 9px; height: 9px; border-radius: 50%; background: var(--tim); border: 2px solid var(--paper); outline: 1px solid var(--tim); margin: 0 0 18px 1px; transition: box-shadow 180ms; }strong { font: 600 var(--fs-small)/1.5 var(--font-ui); margin-bottom: 6px; }strong + span { font: var(--fs-meta)/1.65 var(--font-ui); color: var(--ink-3); }.wiki-timeline-arrow { color: var(--tim); margin-top: 10px; font-size: 21px; }a:hover strong { text-decoration: underline; text-underline-offset: 4px; }a:hover .wiki-timeline-node { box-shadow: 0 0 0 6px var(--tim-soft); }
@media (max-width: 1100px) { ol { grid-template-columns: repeat(3, minmax(0, 1fr)); row-gap: 24px; }li:nth-child(3n) a::before { right: 80%; } }
@media (max-width: 500px) { ol { grid-template-columns: minmax(0, 1fr); row-gap: 0; }a { min-height: 0; padding: 0 24px 24px 30px; }a::before, li:nth-child(3n) a::before { left: 4px; right: auto; top: 12px; width: 1px; height: 100%; }li:last-child a::before { height: 0; }.wiki-timeline-node { position: absolute; left: 0; top: 10px; }.wiki-timeline-year { font-size: 24px; margin-bottom: 8px; }.wiki-timeline-arrow { position: absolute; right: 0; top: 0; margin: 0; } }
@media (prefers-reduced-motion: reduce) { .wiki-timeline-node { transition: none; } }
</style>
