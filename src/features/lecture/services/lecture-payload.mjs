import { loadConceptData } from '../../wiki/services/concept-loader.mjs'
import { buildLectureCheatsheet } from './cheatsheet-builder.mjs'
import { cheatsheetLoaders } from './cheatsheet-loaders.mjs'
import { lectureSlides } from './lecture-model.mjs'
import { foundationGroupsFor } from './panel-rules.mjs'

// Slides, cheatsheets, labs and concept notes are only shown after a reader
// opens a lecture tab, and none of them is part of the server-rendered page.
// Each course module becomes its own chunk, so a lecture downloads only its
// course data instead of every subject's slides on every page.
const courseModules = import.meta.glob('../../../content/courses/*/course.mjs')
const cache = new Map()

async function loadFullCourse(courseId) {
  const load = courseModules[`../../../content/courses/${courseId}/course.mjs`]
  return load ? (await load()).course : null
}

async function loadPayload(course, lesson) {
  const key = `${course.id}/${lesson.slug}`
  const [fullCourse, conceptData, labs, explicit] = await Promise.all([
    loadFullCourse(course.id),
    loadConceptData(),
    import('../../labs/services/course-labs.mjs'),
    cheatsheetLoaders[key]?.() ?? null
  ])
  const sourceCourse = fullCourse || course
  const { concepts } = conceptData
  return {
    concepts,
    slides: lectureSlides(sourceCourse, lesson),
    cheatsheet: buildLectureCheatsheet(sourceCourse, lesson, { explicit, concepts }),
    foundationGroups: foundationGroupsFor(lesson, concepts),
    lab: labs.getCourseLab(course, lesson)
  }
}

/** Resolve everything the lecture panels render for one lesson (cached). */
export function loadLecturePayload(course, lesson) {
  if (!course || !lesson) return Promise.resolve(null)
  const key = `${course.id}/${lesson.slug}`
  if (!cache.has(key)) {
    cache.set(key, loadPayload(course, lesson).catch(error => {
      cache.delete(key)
      throw error
    }))
  }
  return cache.get(key)
}
