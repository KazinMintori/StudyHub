import { canonicalLesson as defaultCanonicalLesson } from './progress-migration.js'
import { calculateProgressKey } from './progress-key.js'
import { lecturePath, lessonTopics, topicPath } from '../../lecture/services/lecture-model.mjs'

export function resolveResumeLesson(savedLastLesson, catalog = [], options = {}) {
  if (typeof savedLastLesson?.path !== 'string' || !savedLastLesson.path) return null
  const canonicalFn = options.canonicalLesson || defaultCanonicalLesson
  const keyFn = options.progressKey || calculateProgressKey

  const path = canonicalFn(savedLastLesson.path)
  if (typeof path !== 'string') return null
  const routePath = path.replace(/\/$/, '').replace(/\.html$/, '')

  for (const course of catalog) {
    const lessons = [...(course.lessons || []), ...(course.review ? [course.review] : [])]
    for (const lesson of lessons) {
      if (lesson.status !== 'ready') continue
      const topics = lessonTopics(lesson)
      const availableTopics = topics.length ? topics : (lesson.topics || [])
      const matchesLesson = lecturePath(course.id, lesson.slug) === routePath ||
        keyFn(course, lesson) === path
      const matchesTopic = availableTopics.some(topic => topicPath(course.id, lesson.slug, topic.slug) === routePath)
      if (!matchesLesson && !matchesTopic) continue

      return {
        course,
        lesson,
        path,
        heading: typeof savedLastLesson.heading === 'string' ? savedLastLesson.heading : '',
        headingTitle: typeof savedLastLesson.headingTitle === 'string' ? savedLastLesson.headingTitle : ''
      }
    }
  }
  return null
}

export function resolveResumeLink(resume) {
  if (!resume?.path) return ''
  return `${resume.path}#${resume.heading || 'notes'}`
}

export function resolveDefaultReadyLesson(catalog = []) {
  for (const course of catalog) {
    const lesson = course.lessons?.find(l => l.status === 'ready')
    if (lesson) {
      return {
        course,
        lesson,
        path: lecturePath(course.id, lesson.slug),
        heading: '',
        headingTitle: ''
      }
    }
  }
  return null
}

export function resolveActiveResume(savedLastLesson, catalog = [], options = {}) {
  const resume = resolveResumeLesson(savedLastLesson, catalog, options)
  const defaultStarter = resume ? null : resolveDefaultReadyLesson(catalog)
  const activeResume = resume || defaultStarter

  let activeResumeLink = ''
  if (resume) {
    activeResumeLink = resolveResumeLink(resume)
  } else if (defaultStarter) {
    activeResumeLink = defaultStarter.path
  }

  return {
    resume,
    resumeLink: resolveResumeLink(resume),
    defaultStarter,
    activeResume,
    activeResumeLink
  }
}
