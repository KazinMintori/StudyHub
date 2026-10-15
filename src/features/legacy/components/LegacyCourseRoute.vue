<script setup>
import { onMounted } from 'vue'
import { useData,useRouter } from 'vitepress'
import { findCourse } from '../../../content/catalog.mjs'
import { concepts } from '../../../../docs/.vitepress/concepts.mjs'
import { lecturePath } from '../../lecture/services/lecture-model.mjs'
import { studyLink } from '../../../core/routing/links.js'
const {frontmatter}=useData(), router=useRouter()
onMounted(()=>{
  if (frontmatter.value.legacyKind === 'slides') return
  const course=findCourse(frontmatter.value.course), hash=window.location.hash.slice(1)
  let target=`/${course.id}/`
  if(frontmatter.value.legacyKind==='foundations')target=concepts[hash]?`/wiki/${hash}`:'/wiki/'
  else if(/^slide-\d+$/.test(hash)){const slide=course.slides[Number(hash.slice(6))-1];if(slide)target=lecturePath(course.id,slide.note,'slides')}
  target=studyLink(target);window.history.replaceState({},'',target);router.go(target)
})
</script>
<template>
  <p v-if="frontmatter.legacyKind === 'slides'" class="course-shell empty-state">Bộ thẻ ôn tập đang được biên soạn.</p>
  <p v-else class="course-shell">Các phần đã được gom theo từng bài giảng. Đang mở địa chỉ mới…</p>
</template>
