<script setup>
import { computed } from 'vue'
import { useStudyPlan } from '../controllers/useStudyPlan.js'
const props = defineProps({ courseId: { type: String, default: 'all' } })
const { tasks, draft, error, completed, add, toggle, remove } = useStudyPlan(computed(() => props.courseId))
</script>

<template>
  <section id="plan" class="workspace-section study-plan" aria-labelledby="plan-heading">
    <div class="section-heading"><div><h2 id="plan-heading">Việc cần học</h2><p>Chia buổi học thành những việc nhỏ có thể hoàn thành.</p></div><span class="small" role="status">{{ completed }} / {{ tasks.length }} việc đã xong</span></div>
    <form class="study-plan-form" @submit.prevent="add">
      <label for="study-plan-draft">Thêm việc học</label>
      <div><input id="study-plan-draft" v-model="draft" maxlength="300" placeholder="Ví dụ: Tự giải ba bài về đạo hàm" :aria-invalid="Boolean(error)" :aria-describedby="error ? 'study-plan-error' : undefined"><button type="submit" class="study-button primary">Thêm việc</button></div>
      <p v-if="error" id="study-plan-error" class="study-plan-error" role="alert">{{ error }}</p>
    </form>
    <ul v-if="tasks.length" class="study-plan-list" aria-label="Danh sách việc học">
      <li v-for="task in tasks" :key="task.id" :class="{ 'is-complete': task.done }">
        <label><input type="checkbox" :checked="task.done" @change="toggle(task.id)"><span>{{ task.text }}</span></label>
        <button type="button" class="study-plan-remove" :aria-label="`Xóa việc: ${task.text}`" @click="remove(task.id)"><svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><path d="m5 5 10 10M15 5 5 15" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" /></svg></button>
      </li>
    </ul>
    <p v-else class="empty-state">Chưa có việc học trong danh sách này. Thêm một mục tiêu nhỏ cho buổi học hôm nay.</p>
    <p class="small tool-explanation">Mỗi môn có danh sách riêng, được lưu trên trình duyệt này.</p>
  </section>
</template>
