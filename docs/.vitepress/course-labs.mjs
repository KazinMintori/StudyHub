// Module kết nối toàn bộ hệ thống bài tập và phòng Lab thực chiến của StudyHub
import { dataProcessingLabs } from './labs/data-processing-labs.mjs'
import { dsaLabs } from './labs/dsa-labs.mjs'
import { discreteMathLabs } from './labs/discrete-math-labs.mjs'
import { knowledgeLabs } from './labs/knowledge-labs.mjs'
import { probStatsLabs } from './labs/prob-stats-labs.mjs'

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
