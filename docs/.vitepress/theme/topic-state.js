import { computed } from 'vue'
import { useData } from 'vitepress'
import { findCourse } from '../course-catalog.mjs'
import { findTopic } from '../lecture-model.mjs'

// Trạng thái của một trang chủ đề: chương chứa nó, vị trí trong chương và hai chủ đề kề.
export function useTopic() {
  const { frontmatter } = useData()
  const course = computed(() => findCourse(frontmatter.value.course))
  const found = computed(() => findTopic(frontmatter.value.course, frontmatter.value.lecture, frontmatter.value.topic))
  const lesson = computed(() => found.value?.lesson)
  const topics = computed(() => found.value?.topics || [])
  const index = computed(() => found.value?.index ?? -1)
  const topic = computed(() => found.value?.topic)
  const previous = computed(() => index.value > 0 ? topics.value[index.value - 1] : null)
  const next = computed(() => index.value >= 0 && index.value < topics.value.length - 1 ? topics.value[index.value + 1] : null)
  const nextLesson = computed(() => {
    const lessons = course.value?.lessons || []
    const at = lessons.indexOf(lesson.value)
    return at >= 0 ? lessons[at + 1] : null
  })
  return { frontmatter, course, lesson, topics, index, topic, previous, next, nextLesson }
}
