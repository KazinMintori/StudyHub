<script setup>
import { onMounted, computed } from 'vue'
import { useData, useRouter } from 'vitepress'
import { studyLink } from './links'
const { frontmatter } = useData(), router = useRouter(), href = computed(() => studyLink(frontmatter.value.redirectTo))
onMounted(() => { const target = href.value + window.location.hash; window.history.replaceState({}, '', target); router.go(target) })
</script>
<template><div class="course-shell"><p>Bài học đã chuyển vào Notes.</p><a class="text-link" :href="href">Mở bài học trong Notes →</a></div></template>
