import test from 'node:test'
import assert from 'node:assert/strict'
import { findLecture, findTopic } from './lecture-model.mjs'
import { findCourse } from '../../../content/catalog.mjs'

test('Lecture lookup tolerates missing frontmatter while a page is loading', () => {
  assert.equal(findLecture(undefined, undefined), undefined)
  assert.equal(findLecture('unknown-course', undefined), undefined)
  assert.equal(findLecture('vat-ly-2', undefined), undefined)
  assert.equal(findLecture(undefined, '01-dien-truong-coulomb'), undefined)
  assert.equal(findTopic(undefined, undefined, undefined), null)
})

test('Lecture lookup retains real lecture and course-review routes', () => {
  const physics = findCourse('vat-ly-2')
  assert.equal(findLecture(physics.id, physics.lessons[0].slug), physics.lessons[0])
  const math = findCourse('toan-cho-ai')
  assert.equal(findLecture(math.id, math.review.slug), math.review)
  assert.equal(findLecture(physics.id, 'unknown-lecture'), undefined)
})
