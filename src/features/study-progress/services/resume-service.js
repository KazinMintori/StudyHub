import { canonicalLesson as defaultCanonicalLesson } from './progress-migration.js'
import { calculateProgressKey } from './progress-key.js'

export function resolveResumeLesson(savedLastLesson, catalog = [], options = {}) {
  if (!savedLastLesson || !savedLastLesson.path) return null
  const canonicalFn = options.canonicalLesson || defaultCanonicalLesson
  const keyFn = options.progressKey || calculateProgressKey

  const path = canonicalFn(savedLastLesson.path)
  const course = catalog.find(c =>
    c.lessons?.some(l => l.status === 'ready' && keyFn(c, l) === path)
  )
  if (!course) return null

  const lesson = course.lessons?.find(l => keyFn(course, l) === path)
  if (!lesson) return null

  return {
    course,
    lesson,
    path,
    heading: typeof savedLastLesson.heading === 'string' ? savedLastLesson.heading : '',
    headingTitle: typeof savedLastLesson.headingTitle === 'string' ? savedLastLesson.headingTitle : ''
  }
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
        path: `/${course.id}/bai-giang/${lesson.slug}`,
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
