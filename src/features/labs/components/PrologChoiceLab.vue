<script setup>
import { computed, ref, watch } from 'vue'
import SimulationControls from './SimulationControls.vue'

const cut = ref(false)
const step = ref(0)
const courses = ['csc135', 'csc131']
const enrollments = [
  { student: 'arthur', course: 'csc135' },
  { student: 'charlie', course: 'csc135' },
  { student: 'olivia', course: 'csc135' },
  { student: 'jack', course: 'csc131' }
]
const eligible = ['charlie', 'olivia', 'jack']
const trace = computed(() => {
  const answers = []
  const frames = []
  const record = (goal, binding, event) => {
    frames.push({ goal, binding, event, answers: [...answers] })
  }
  record('student(X)', '—', 'Mở truy vấn')
  for (const course of courses) {
    record('teaches(kirke, C)', course, 'Chọn một giá trị cho C')
    if (cut.value) record('!', course, 'Bỏ các lựa chọn còn lại của teaches/2')
    for (const row of enrollments.filter(row => row.course === course)) {
      record(`studies(X, ${course})`, course, 'Thử sự thực phù hợp')
      record(`eligible(${row.student})`, course, `Thử với X = ${row.student}`)
      if (!eligible.includes(row.student)) {
        record(`studies(X, ${course})`, course, 'Mục tiêu thất bại. Gỡ ràng buộc X rồi thử sinh viên tiếp theo')
        continue
      }
      answers.push(row.student)
      record('□', course, `Trả lời X = ${row.student}`)
      record(`studies(X, ${course})`, course, 'Quay lui để tìm câu trả lời tiếp theo')
    }
    if (cut.value) break
    record('teaches(kirke, C)', '—', 'Hủy ràng buộc C và thử môn tiếp theo nếu còn')
  }
  record('—', '—', 'Đã duyệt hết các lựa chọn còn lại')
  return frames
})
const frame = computed(() => trace.value[Math.min(step.value, trace.value.length - 1)])
watch(cut, () => { step.value = 0 })
</script>

<template>
  <section class="math-lab" aria-label="Vết chạy quay lui trong Prolog">
    <label><input v-model="cut" type="checkbox"> Đặt dấu cắt sau teaches/2</label>
    <pre><code>student(X) :- teaches(kirke, C), {{ cut ? '!, ' : '' }}studies(X, C), eligible(X).</code></pre>
    <details>
      <summary>Sự thực và truy vấn</summary>
      <pre><code>{{ courses.map(course => 'teaches(kirke, ' + course + ').').join('\n') }}
{{ enrollments.map(row => 'studies(' + row.student + ', ' + row.course + ').').join('\n') }}
{{ eligible.map(student => 'eligible(' + student + ').').join('\n') }}

?- student(X).</code></pre>
    </details>
    <SimulationControls v-model="step" :max="trace.length - 1" :reset-key="cut" />
    <dl aria-live="polite">
      <dt>Mục tiêu đang xét</dt><dd><code>{{ frame.goal }}</code></dd>
      <dt>Ràng buộc của C</dt><dd><code>{{ frame.binding }}</code></dd>
      <dt>Thao tác</dt><dd>{{ frame.event }}</dd>
      <dt>Câu trả lời đã tìm</dt><dd>{{ frame.answers.join(', ') || 'Chưa có' }}</dd>
    </dl>
  </section>
</template>

<style scoped>
pre, code { white-space: pre-wrap; overflow-wrap: anywhere; }
</style>
