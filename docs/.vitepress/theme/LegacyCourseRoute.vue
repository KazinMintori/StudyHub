<script setup>
import { onMounted } from 'vue'
import { useData,useRouter } from 'vitepress'
import { findCourse } from '../course-catalog.mjs'
import { concepts } from '../concepts.mjs'
import { lecturePath } from '../lecture-model.mjs'
import { studyLink } from './links'
const {frontmatter}=useData(), router=useRouter()
onMounted(()=>{
  const course=findCourse(frontmatter.value.course), hash=window.location.hash.slice(1)
  let target=`/${course.id}/`
  if(frontmatter.value.legacyKind==='foundations')target=concepts[hash]?`/wiki/${hash}`:'/wiki/'
  else if(/^slide-\d+$/.test(hash)){const slide=course.slides[Number(hash.slice(6))-1];if(slide)target=lecturePath(course.id,slide.note,'slides')}
  target=studyLink(target);window.history.replaceState({},'',target);router.go(target)
})
</script>
<template><p class="course-shell">Các phần đã được gom theo từng bài giảng. Đang mở địa chỉ mới…</p></template>
