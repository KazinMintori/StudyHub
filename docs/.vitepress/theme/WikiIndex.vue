<script setup>
import { computed, ref } from 'vue'
import { concepts } from '../concepts.mjs'
import { wikiGroups } from '../wiki-content.mjs'
import { courseCatalog } from '../course-catalog.mjs'
import { studyLink } from './links'
import MathText from './MathText.vue'
const query = ref(''), selected = ref('all')
const normalize = text => text.toLocaleLowerCase('vi').normalize('NFD').replace(/\p{M}/gu, '').replace(/đ/g, 'd')
const usage = id => courseCatalog.reduce((n, c) => n + c.lessons.filter(l => [...(l.prerequisites || []), ...(l.supportingConcepts || [])].includes(id)).length, 0)
const groups = computed(() => wikiGroups.filter(g => selected.value === 'all' || g.name === selected.value).map(g => ({ ...g, entries: g.ids.filter(id => normalize(`${concepts[id].name} ${concepts[id].aliases.join(' ')} ${concepts[id].definition}`).includes(normalize(query.value))).map(id => ({ id, ...concepts[id] })) })).filter(g => g.entries.length))
const count = computed(() => groups.value.reduce((n, g) => n + g.entries.length, 0))
</script>
<template><main class="wiki-index course-shell"><h1>Wiki thuật ngữ</h1><p>{{ Object.keys(concepts).length }} khái niệm nền dùng trong các bài giảng.</p><div class="wiki-filters"><label>Tìm thuật ngữ<input v-model="query" type="search" placeholder="Tìm thuật ngữ, không cần gõ dấu…"></label><label>Nhóm kiến thức<select v-model="selected"><option value="all">Tất cả</option><option v-for="g in wikiGroups" :key="g.name">{{ g.name }}</option></select></label></div><p class="small" role="status">{{ count }} thuật ngữ</p><section v-for="group in groups" :key="group.name" class="wiki-group"><h2>{{ group.name }}<span>{{ group.entries.length }}</span></h2><div class="wiki-entry-list"><a v-for="term in group.entries" :key="term.id" :href="studyLink(`/wiki/${term.id}`)"><h3>{{ term.name }}</h3><MathText as="p" :text="term.definition" /><span>{{ usage(term.id) ? `Dùng trong ${usage(term.id)} bài` : 'Khái niệm bổ trợ' }}</span></a></div></section><p v-if="!count" class="empty-state">Chưa tìm thấy thuật ngữ. Thử tên khác hoặc bỏ bộ lọc.</p></main></template>
