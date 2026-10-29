<script setup>
import { computed, defineAsyncComponent, h, nextTick, onMounted, onUnmounted, ref } from 'vue'
import { withBase } from 'vitepress'
import SpotArt from '../../illustrations/components/SpotArt.vue'
import { courses as defaultCourses } from '../data/course-options.mjs'
import { storageMessage } from '../../../core/storage/index.js'
import { useWorkspaceTabs } from '../controllers/useWorkspaceTabs.js'
import FlashcardDeck from './FlashcardDeck.vue'
import StudyNotebook from './StudyNotebook.vue'
import FocusTimer from './FocusTimer.vue'
import StudyPlan from './StudyPlan.vue'
import { parseWorkspaceCourse, normalizeWorkspaceCourse, workspacePath } from '../services/courseWorkspaceService.mjs'
import { courseSimulations } from '../data/course-simulations.mjs'
import { shouldIgnoreNavigationClick } from '../../navigation/services/tab-service.mjs'
import { stabilizeInitialHeading } from '../../navigation/services/initial-heading-stabilizer.mjs'

const FieldSimulation = defineAsyncComponent(() => import('../../labs/components/FieldSimulation.vue'))
const labLoaders = import.meta.glob('../../labs/components/*Lab.vue')
const componentCache = new Map()

const props = defineProps({
  courses: {
    type: Array,
    default: () => defaultCourses
  }
})

const {
  tabs,
  active,
  changeTab
} = useWorkspaceTabs()

const selectedCourse = ref(props.courses[0]?.id || 'all')
const resolveCourse = value => normalizeWorkspaceCourse(value, props.courses) === 'all' ? (props.courses[0]?.id || 'all') : value
const currentCourse = computed(() => props.courses.find(course => course.id === selectedCourse.value))
const simulations = computed(() => courseSimulations(selectedCourse.value))
const hasField = computed(() => selectedCourse.value === 'all' || selectedCourse.value === 'vat-ly-2')
const fieldOpened = ref(false)
const simulationId = ref('')
const simulationRunner = ref(null)
const simulationDirectory = ref(null)
let initialSimulation
function cancelInitialSimulation() { initialSimulation?.stop() }
function simulationReady() { initialSimulation?.refresh() }
const selectedSimulation = computed(() => simulations.value.find(item => item.id === simulationId.value))
const simulationComponent = computed(() => {
  const name = selectedSimulation.value?.component
  if (!name) return null
  if (!componentCache.has(name)) {
    const loader = name === 'CodeIllustration' ? () => import('../../illustrations/components/CodeIllustration.vue') : labLoaders[`../../labs/components/${name}.vue`]
    if (!loader) return null
    componentCache.set(name, defineAsyncComponent({
      loader, delay: 0,
      loadingComponent: { setup: () => () => h('p', { role: 'status' }, 'Đang tải mô phỏng…') },
      errorComponent: { setup: () => () => h('p', { role: 'alert' }, 'Chưa tải được mô phỏng. Kiểm tra kết nối rồi tải lại trang.') }
    }))
  }
  return componentCache.get(name)
})
const simulationProps = computed(() => selectedSimulation.value?.component === 'CodeIllustration'
  ? { type: selectedSimulation.value.id === 'mapreduce' ? 'mapreduce' : 'search' }
  : {})
function syncCourse() {
  selectedCourse.value = resolveCourse(parseWorkspaceCourse(window.location.search, props.courses))
  const requested = new URLSearchParams(window.location.search).get('mo-phong')
  simulationId.value = simulations.value.some(item => item.id === requested) ? requested : ''
}
function selectCourse(event) {
  cancelInitialSimulation()
  selectedCourse.value = resolveCourse(event.target.value)
  fieldOpened.value = false
  simulationId.value = ''
  const url = new URL(window.location.href)
  if (selectedCourse.value === 'all') url.searchParams.delete('mon')
  else url.searchParams.set('mon', selectedCourse.value)
  url.searchParams.delete('mo-phong')
  window.history.replaceState(window.history.state, '', url.pathname + url.search + url.hash)
}
async function openSimulation(item, event) {
  if (shouldIgnoreNavigationClick(event)) return
  event.preventDefault()
  cancelInitialSimulation()
  simulationId.value = item.id
  if (simulationDirectory.value) simulationDirectory.value.open = false
  const url = new URL(window.location.href)
  url.searchParams.set('mo-phong', item.id)
  window.history.replaceState(window.history.state, '', url.pathname + url.search + '#simulation')
  await nextTick()
  simulationRunner.value?.scrollIntoView({ block: 'start', behavior: 'instant' })
  simulationRunner.value?.querySelector('h3')?.focus({ preventScroll: true })
}
function selectTab(id, event) {
  if (shouldIgnoreNavigationClick(event)) return
  event.preventDefault()
  cancelInitialSimulation()
  changeTab(id)
}
onMounted(() => {
  syncCourse()
  if (selectedSimulation.value) {
    initialSimulation = stabilizeInitialHeading({ targetId: 'workspace-active-simulation', getOffset: () => (document.querySelector('.VPNav')?.getBoundingClientRect().bottom || 0) + 16 })
  }
  window.addEventListener('popstate', syncCourse)
})
onUnmounted(() => { cancelInitialSimulation(); window.removeEventListener('popstate', syncCourse) })
</script>

<template>
  <main class="study-workspace">
    <header class="workspace-heading page-hero">
      <div>
        <a class="small text-link" :href="withBase('/')">← Trang chủ</a>
        <h1>Góc học tập</h1>
        <p>Ghi chú, flashcard, kế hoạch và mô phỏng cho từng môn học.</p>
      </div>
      <SpotArt name="tools" tone="hong" />
    </header>
    <section class="workspace-course-context" aria-label="Học phần đang học">
      <label for="workspace-course">Chọn học phần<select id="workspace-course" :value="selectedCourse" @change="selectCourse"><option v-for="course in courses" :key="course.id" :value="course.id">{{ course.name }}</option></select></label>
      <div v-if="currentCourse" class="workspace-course-links"><a class="text-link" :href="withBase(`/${currentCourse.id}/`)">Bài giảng của môn</a><a class="text-link" :href="withBase(`/${currentCourse.id}/${currentCourse.presentation === 'philosophy' ? 'on-thi/' : 'bai-tap.html'}`)">{{ currentCourse.presentation === 'philosophy' ? 'Ôn thi' : 'Bài tập của môn' }}</a></div>
      <p v-else>Chọn một môn để mở đúng sổ ghi chú, bộ thẻ và danh sách việc học.</p>
    </section>
    <nav class="workspace-tabs vp-raw" aria-label="Công cụ học tập">
      <a
        v-for="tab in tabs"
        :key="tab.id"
        :href="withBase(workspacePath(selectedCourse, tab.id, simulationId))"
        :aria-current="active === tab.id ? 'page' : undefined"
        @click="selectTab(tab.id, $event)"
      >{{ tab.name }}</a>
    </nav>
    <p v-if="storageMessage" class="storage-message" role="status">{{ storageMessage }}</p>

    <FlashcardDeck v-show="active === 'flashcards'" :courses="courses" :course-id="selectedCourse" />

    <StudyNotebook v-show="active === 'notes'" :courses="courses" :course-id="selectedCourse" />

    <StudyPlan v-show="active === 'plan'" :course-id="selectedCourse" />

    <section v-show="active === 'simulation'" id="simulation" class="workspace-section" aria-labelledby="simulation-heading">
      <h2 id="simulation-heading">Mô phỏng và minh họa tương tác</h2>
      <p class="workspace-simulation-help">Trên điện thoại, chọn điểm rồi dùng các nút hướng hoặc thanh chỉnh. Bạn vẫn có thể vuốt phần nền để cuộn trang.</p>
      <section v-if="selectedSimulation && simulationComponent" ref="simulationRunner" class="workspace-lab-runner" :aria-label="selectedSimulation.title">
        <h3 id="workspace-active-simulation" tabindex="-1">{{ selectedSimulation.title }}</h3>
        <p class="small">Điều chỉnh trực tiếp bên dưới. Mô phỏng được mở riêng để bạn dễ thao tác trên điện thoại.</p>
        <component :is="simulationComponent" :key="selectedSimulation.id" v-bind="simulationProps" @vue:mounted="simulationReady" />
        <a class="text-link" :href="withBase(selectedSimulation.path)">Đọc bài giảng liên quan <span aria-hidden="true">→</span></a>
      </section>
      <details v-if="simulations.length" ref="simulationDirectory" class="workspace-simulation-directory" :open="!selectedSimulation">
        <summary>{{ selectedSimulation ? 'Đổi mô phỏng' : 'Chọn mô phỏng' }}<span>{{ simulations.length }} lựa chọn</span></summary>
          <div class="workspace-simulation-grid vp-raw">
          <a v-for="simulation in simulations" :key="simulation.id" :href="withBase(workspacePath(selectedCourse, 'simulation', simulation.id))" :aria-current="selectedSimulation?.id === simulation.id ? 'true' : undefined" @click="openSimulation(simulation, $event)"><strong>{{ simulation.title }}</strong><span>{{ simulation.description }}</span><span class="workspace-simulation-open">Mở mô phỏng <span aria-hidden="true">→</span></span></a>
        </div>
      </details>
      <section v-if="hasField" class="workspace-field-card" aria-labelledby="workspace-field-heading">
        <h3 id="workspace-field-heading">Điện trường và đường sức</h3><p>Thêm điện tích, chọn điện tích cần đổi và điều chỉnh vị trí bằng nút hướng hoặc thanh trượt.</p>
        <button v-if="!fieldOpened" class="study-button" type="button" @click="fieldOpened = true">Mở mô phỏng điện trường</button>
        <FieldSimulation v-if="fieldOpened" />
      </section>
      <p v-if="!simulations.length && !hasField" class="empty-state">Môn này chưa có mô phỏng riêng. Bạn có thể dùng bộ thẻ, ghi chú và danh sách việc học để ôn tập.</p>
    </section>

    <section v-show="active === 'focus'" id="focus" class="workspace-section workspace-focus">
      <FocusTimer />
      <div>
        <h2>Cách dùng phiên học</h2>
        <ol class="focus-guide">
          <li>Chọn một bài hoặc một câu hỏi cụ thể.</li>
          <li>Bắt đầu phiên 25 hoặc 50 phút.</li>
          <li>Ghi lại điều chưa hiểu để xử lý sau.</li>
          <li>Dành 5 phút nghỉ trước phiên tiếp theo.</li>
        </ol>
        <a class="text-link" :href="withBase('/guide/')">Đọc thêm về phương pháp học</a>
      </div>
    </section>
  </main>
</template>
