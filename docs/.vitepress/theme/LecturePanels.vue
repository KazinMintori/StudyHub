<script setup>
import { computed, ref, watch, onMounted, onUnmounted } from 'vue'
import { useLecture } from './lecture-state'
import { lectureSlides } from '../lecture-model.mjs'
import { concepts } from '../concepts.mjs'
import { studyLink } from './links'
import { readStored, writeStored, storageMessage } from './storage'
const { course, lesson, part } = useLecture(), index = ref(0), understood = ref({})
const slides = computed(() => lectureSlides(course.value, lesson.value)), current = computed(() => slides.value[index.value])
const required = computed(() => (lesson.value?.prerequisites || []).filter(id => concepts[id]))
const understoodCount = computed(() => required.value.filter(id => understood.value[id]).length)
function load() { index.value = 0; understood.value = readStored(`studyhub_foundations_${course.value?.id}`, {}) || {} }
function toggle(id) { const next = { ...understood.value, [id]: !understood.value[id] }; if (writeStored(`studyhub_foundations_${course.value.id}`, next)) understood.value = next }
function next(direction) { index.value = Math.max(0, Math.min(slides.value.length - 1, index.value + direction)) }
function keyboard(event) { if(part.value!=='slides'||/INPUT|TEXTAREA|SELECT/.test(event.target.tagName))return; if(event.key==='ArrowRight'){event.preventDefault();next(1)} if(event.key==='ArrowLeft'){event.preventDefault();next(-1)} }
onMounted(() => { load(); window.addEventListener('keydown', keyboard) })
onUnmounted(() => { window.removeEventListener('keydown', keyboard) })
watch(() => lesson.value?.slug, load)
</script>
<template><div v-if="course && lesson" class="lecture-panels">
  <section v-if="part==='slides'" class="lecture-slides" aria-label="Slides của bài giảng">
    <p class="eyebrow">Ý CHÍNH CỦA BÀI NÀY</p>
    <article v-if="current" class="course-slide" aria-live="polite"><p class="eyebrow">{{ index+1 }} / {{ slides.length }}</p><h2>{{ current.title }}</h2><ul><li v-for="bullet in current.bullets" :key="bullet">{{ bullet }}</li></ul><p v-if="current.formula" class="slide-formula">{{ current.formula }}</p><p v-if="current.example" class="slide-example"><strong>Ví dụ:</strong> {{ current.example }}</p></article>
    <p v-else class="empty-state">Slides của bài đang được biên soạn.</p>
    <div v-if="current" class="slide-controls"><button class="study-button" :disabled="index===0" @click="next(-1)">← Trước</button><span>{{ index+1 }} / {{ slides.length }} · Phím ← →</span><button class="study-button primary" :disabled="index===slides.length-1" @click="next(1)">Tiếp →</button></div>
  </section>
  <section v-else-if="part === 'kien-thuc-can-co'" class="lecture-foundations" aria-label="Kiến thức nền của bài giảng"><div class="foundations-heading"><h2>Kiến thức nền cho bài này</h2><span role="status">Đã hiểu {{ understoodCount }}/{{ required.length }}</span></div><p>Những khái niệm bài dùng mà không giảng lại.</p><article v-for="id in required" :id="`nen-tang-${id}`" :key="id" class="foundation-entry"><div class="foundation-entry-heading"><label class="foundation-check"><input type="checkbox" :checked="!!understood[id]" :aria-label="`Đã hiểu ${concepts[id].name}`" @change="toggle(id)"></label><details><summary><strong>{{ concepts[id].name }}</strong><span>{{ concepts[id].definition.split(/(?<=[.!?])\s/)[0] }}</span></summary><div class="foundation-content"><p>{{ concepts[id].definition }}</p><h4>Ví dụ</h4><p>{{ concepts[id].example }}</p><p><strong>Dùng để:</strong> {{ concepts[id].use }}</p><details><summary>Tự kiểm tra: {{ concepts[id].question }}</summary><p>{{ concepts[id].answer }}</p></details><a class="text-link" :href="studyLink(`/wiki/${id}`)">Đọc {{ concepts[id].name }} trong Wiki</a></div></details></div></article><p v-if="storageMessage" role="status" class="storage-message">{{ storageMessage }}</p></section>
</div></template>
