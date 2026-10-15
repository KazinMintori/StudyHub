// Module kết nối toàn bộ hệ thống bài tập và phòng Lab thực chiến của StudyHub
import { dataProcessingLabs } from '../../../content/courses/xu-ly-du-lieu/labs.mjs'
import { dsaLabs } from '../../../content/courses/dsa/labs.mjs'
import { discreteMathLabs } from '../../../content/courses/discrete-math/labs.mjs'
import { knowledgeLabs } from '../../../content/courses/bieu-dien-tri-thuc/labs.mjs'
import { probStatsLabs } from '../../../content/courses/xac-suat-thong-ke/labs.mjs'

export const courseLabs = {
  ...dataProcessingLabs,
  ...dsaLabs,
  ...discreteMathLabs,
  ...knowledgeLabs,
  ...probStatsLabs
}

export function getCourseLab(courseOrId, lessonOrSlug) {
  if (!courseOrId || !lessonOrSlug) return null
  const courseId = typeof courseOrId === 'string' ? courseOrId : courseOrId?.id
  const lessonSlug = typeof lessonOrSlug === 'string' ? lessonOrSlug : (lessonOrSlug?.slug || lessonOrSlug?.note)
  if (!courseId || !lessonSlug) return null
  const key = `${courseId}/${lessonSlug}`
  return courseLabs[key] || null
}
