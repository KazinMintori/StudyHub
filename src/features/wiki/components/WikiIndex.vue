<script setup>
import { computed, ref, watch, nextTick } from 'vue'
import { concepts } from '../../../../docs/.vitepress/concepts.mjs'
import { wikiGroups } from '../../../../docs/.vitepress/wiki-content.mjs'
import { courseCatalog } from '../../../content/catalog.mjs'
import { wikiJourneys, wikiPeople } from '../data/atlas.mjs'
import { matchesWikiQuery, conceptSummary, conceptUsageIndex } from '../services/wiki-discovery.mjs'
import { studyLink } from '../../../core/routing/links.js'
import MathText from '../../../core/math/components/MathText.vue'
import SpotArt from '../../illustrations/components/SpotArt.vue'
import WikiTimeline from './WikiTimeline.vue'
const query = ref(''), selected = ref('all'), view = ref('concepts'), page = ref(1), resultHeading = ref(null)
const pageSize = 30, usage = conceptUsageIndex(courseCatalog)
const entries = computed(() => wikiGroups.filter(g => selected.value === 'all' || g.id === selected.value)
  .flatMap(g => g.ids.filter(id => concepts[id]).map(id => ({ id, ...concepts[id], group: g.name })))
  .filter(term => matchesWikiQuery(term, query.value)))
const people = computed(() => wikiPeople.filter(person => matchesWikiQuery(person, query.value)))
const count = computed(() => view.value === 'people' ? people.value.length : entries.value.length)
const pageCount = computed(() => Math.max(1, Math.ceil(count.value / pageSize)))
const visible = computed(() => entries.value.slice((page.value - 1) * pageSize, page.value * pageSize))
watch([query, selected, view], () => { page.value = 1 })
async function turn(direction) { page.value = Math.max(1, Math.min(pageCount.value, page.value + direction)); await nextTick(); resultHeading.value?.focus({ preventScroll: true }); resultHeading.value?.scrollIntoView({ block: 'start', behavior: 'instant' }) }
</script>
<template>
  <main class="wiki-index course-shell">
    <header class="page-hero wiki-hero"><div><p class="wiki-eyebrow">BẢN ĐỒ TRI THỨC</p><h1>Wiki học tập</h1><p>Từ một câu hỏi đến khái niệm, hình minh họa và những người mở ra cách nghĩ mới.</p><div class="wiki-stats"><span>{{ Object.keys(concepts).length }} khái niệm</span><span>{{ wikiPeople.length }} nhân vật</span><span>{{ wikiJourneys.length }} lộ trình đọc</span></div></div><SpotArt name="wiki" tone="lam" /></header>
    <section class="wiki-discovery" aria-labelledby="wiki-results-title">
      <nav class="wiki-view-switch" aria-label="Loại bài Wiki"><button type="button" :aria-pressed="view === 'concepts'" @click="view = 'concepts'">Khái niệm</button><button type="button" :aria-pressed="view === 'people'" @click="view = 'people'">Con người & ý tưởng</button></nav>
      <div class="wiki-filters"><label>Tìm trong Wiki<input v-model="query" type="search" placeholder="Tên hoặc từ khóa, không cần gõ dấu…" aria-controls="wiki-results"></label><label v-if="view === 'concepts'">Nhóm kiến thức<select v-model="selected"><option value="all">Tất cả lĩnh vực</option><option v-for="g in wikiGroups" :key="g.id" :value="g.id">{{ g.name }}</option></select></label></div>
    <section v-if="!query && selected === 'all' && view === 'concepts'" class="wiki-journeys" aria-labelledby="wiki-journey-heading">
      <div class="section-heading"><div><h2 id="wiki-journey-heading">Bắt đầu từ một câu hỏi</h2><p class="section-subtitle">Mỗi lộ trình nối những ý tưởng cần nhau.</p></div></div>
      <div class="wiki-journey-grid"><article v-for="(journey, index) in wikiJourneys" :key="journey.id" class="wiki-journey" :class="`tone-${journey.tone}`"><span class="wiki-journey-number">{{ String(index + 1).padStart(2, '0') }}</span><h3><a :href="studyLink(`/wiki/${journey.ids[0]}`)">{{ journey.title }}</a></h3><p>{{ journey.description }}</p><ol><li v-for="id in journey.ids" :key="id"><a :href="studyLink(`/wiki/${id}`)">{{ concepts[id].name }}</a></li></ol></article></div>
    </section>
      <h2 id="wiki-results-title" ref="resultHeading" tabindex="-1">{{ view === 'people' ? 'Con người & ý tưởng' : 'Tra cứu khái niệm' }}</h2><p class="wiki-result-count" role="status">{{ count }} {{ view === 'people' ? 'nhân vật' : 'khái niệm' }}<template v-if="count > pageSize"> · Trang {{ page }} / {{ pageCount }}</template></p>
      <div id="wiki-results">
        <WikiTimeline v-if="view === 'people' && !query" />
        <div v-if="view === 'concepts'" class="wiki-entry-grid"><a v-for="term in visible" :key="term.id" class="wiki-entry-card" :href="studyLink(`/wiki/${term.id}`)"><span class="wiki-entry-field">{{ term.group }}</span><h3>{{ term.name }}</h3><MathText as="p" :text="conceptSummary(term.definition)" /><span class="wiki-entry-footer">{{ usage.get(term.id) ? `Gặp trong ${usage.get(term.id)} bài` : 'Khái niệm bổ trợ' }} <span aria-hidden="true">↗</span></span></a></div>
        <div v-else class="wiki-people-grid"><a v-for="person in people" :key="person.id" class="wiki-person-card" :href="studyLink(`/wiki/nhan-vat/${person.id}`)"><span class="wiki-person-monogram" aria-hidden="true">{{ person.initials }}</span><div><span class="wiki-entry-field">{{ person.field }}</span><h3>{{ person.name }}</h3><p>{{ person.idea }}</p><span class="wiki-person-milestone">Dấu mốc {{ person.year }} <span aria-hidden="true">↗</span></span></div></a></div>
      </div>
      <nav v-if="view === 'concepts' && pageCount > 1" class="wiki-pagination" aria-label="Phân trang Wiki"><button class="study-button" :disabled="page === 1" @click="turn(-1)">← Trang trước</button><span>{{ page }} / {{ pageCount }}</span><button class="study-button" :disabled="page === pageCount" @click="turn(1)">Trang sau →</button></nav>
      <div v-if="!count" class="empty-state empty-state-art" role="status"><SpotArt name="empty" tone="lam" /><div><p>Chưa tìm thấy kết quả. Thử từ khóa ngắn hơn hoặc bỏ bộ lọc.</p><button class="text-link" @click="query = ''; selected = 'all'">Xóa bộ lọc</button></div></div>
    </section>
  </main>
</template>
