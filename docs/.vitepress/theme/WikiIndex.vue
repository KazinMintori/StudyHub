<script setup>
import { computed, ref } from 'vue'
import { concepts } from '../concepts.mjs'
import { wikiGroups } from '../wiki-content.mjs'
import { studyLink } from './links'
const query=ref(''), selected=ref('all')
const normalize=text=>text.toLocaleLowerCase('vi').normalize('NFD').replace(/\p{M}/gu,'').replace(/đ/g,'d')
const entries=computed(()=>Object.entries(concepts).filter(([id,term])=>(selected.value==='all'||wikiGroups.find(g=>g.name===selected.value).ids.includes(id))&&normalize(`${term.name} ${term.aliases.join(' ')} ${term.definition}`).includes(normalize(query.value))).map(([id,term])=>({id,...term})))
</script>
<template><main class="wiki-index course-shell"><p class="eyebrow">KHO THUẬT NGỮ LIÊN KẾT</p><h1>Wiki học tập</h1><p>Mỗi khái niệm là một bài viết riêng. Bắt đầu từ thuật ngữ đang gặp, theo các liên kết để hiểu những nền tảng liên quan.</p><div class="wiki-filters"><label>Tìm thuật ngữ<input v-model="query" type="search" placeholder="Tên, ký hiệu hoặc từ khóa…"></label><label>Nhóm kiến thức<select v-model="selected"><option value="all">Tất cả</option><option v-for="g in wikiGroups" :key="g.name">{{ g.name }}</option></select></label></div><p class="small" role="status">{{ entries.length }} thuật ngữ</p><div class="wiki-entry-list"><a v-for="term in entries" :key="term.id" :href="studyLink(`/wiki/${term.id}`)"><h2>{{ term.name }}</h2><p>{{ term.definition }}</p><span>Đọc giải thích →</span></a></div><p v-if="!entries.length" class="empty-state">Chưa tìm thấy thuật ngữ. Thử tên khác hoặc bỏ bộ lọc.</p></main></template>
