import {matterWavesCheatsheet} from '../../../../docs/.vitepress/physics-matter-waves-course.mjs'
import {photonCheatsheet} from '../../../../docs/.vitepress/physics-photon-course.mjs'
import {relativityCheatsheet} from '../../../../docs/.vitepress/physics-relativity-course.mjs'
import {diffractionCheatsheet} from '../../../../docs/.vitepress/physics-diffraction-course.mjs'
import {interferenceCheatsheet} from '../../../../docs/.vitepress/physics-interference-course.mjs'
import {geometricOpticsCheatsheet} from '../../../../docs/.vitepress/physics-geometric-optics-course.mjs'
import {opticsCheatsheet} from '../../../../docs/.vitepress/physics-optics-course.mjs'
import {emWaveCheatsheet} from '../../../../docs/.vitepress/physics-emwave-course.mjs'
import {acCheatsheet} from '../../../../docs/.vitepress/physics-ac-course.mjs'
import {inductanceCheatsheet} from '../../../../docs/.vitepress/physics-inductance-course.mjs'
import {inductionCheatsheet} from '../../../../docs/.vitepress/physics-induction-course.mjs'
import { sourcesCheatsheet } from '../../../../docs/.vitepress/physics-sources-course.mjs'
import { magneticCheatsheet } from '../../../../docs/.vitepress/physics-magnetic-course.mjs'
import { dcCheatsheet } from '../../../../docs/.vitepress/physics-dc-course.mjs'
import { currentCheatsheet } from '../../../../docs/.vitepress/physics-current-course.mjs'
import { concepts } from '../../../../docs/.vitepress/concepts.mjs'
import { lectureSlides, lectureConceptIds } from './lecture-model.mjs'
import { physicsMotionCheatsheet } from '../../../../docs/.vitepress/physics-motion-course.mjs'
import { electrostaticsCheatsheet } from '../../../../docs/.vitepress/physics-electrostatics-course.mjs'
import { gaussCheatsheet } from '../../../../docs/.vitepress/physics-gauss-course.mjs'
import { potentialCheatsheet } from '../../../../docs/.vitepress/physics-potential-course.mjs'
import { capacitanceCheatsheet } from '../../../../docs/.vitepress/physics-capacitance-course.mjs'
import { mathAiReviewCheatsheet } from '../../../content/courses/toan-cho-ai/lectures/on-luyen/review-course.mjs'

export const cheatsheets = { 'vat-ly-2/18-photon': photonCheatsheet, 'vat-ly-2/17-thuyet-tuong-doi': relativityCheatsheet, 'vat-ly-2/16-nhieu-xa': diffractionCheatsheet, 'vat-ly-2/15-giao-thoa': interferenceCheatsheet, 'vat-ly-2/14-quang-hinh-hoc': geometricOpticsCheatsheet, 'vat-ly-2/13-truyen-anh-sang': opticsCheatsheet, 'vat-ly-2/12-song-dien-tu': emWaveCheatsheet, 'vat-ly-2/11-dong-dien-xoay-chieu': acCheatsheet, 'vat-ly-2/10-tu-cam': inductanceCheatsheet, 'vat-ly-2/09-cam-ung-dien-tu': inductionCheatsheet, 'vat-ly-2/08-nguon-tu-truong': sourcesCheatsheet, 'vat-ly-2/07-tu-truong-luc-tu': magneticCheatsheet, 'vat-ly-2/06-mach-dien-mot-chieu': dcCheatsheet, 'vat-ly-2/05-dong-dien-dien-tro': currentCheatsheet, 'vat-ly-2/04-tu-dien-dien-moi': capacitanceCheatsheet, 'vat-ly-1/02-chuyen-dong-thang': physicsMotionCheatsheet, 'vat-ly-2/01-dien-truong-coulomb': electrostaticsCheatsheet, 'vat-ly-2/03-dinh-luat-gauss': gaussCheatsheet, 'vat-ly-2/02-dien-the': potentialCheatsheet, 'toan-cho-ai/on-luyen': mathAiReviewCheatsheet,
  'vat-ly-2/19-song-vat-chat': matterWavesCheatsheet,
}

export function getLectureCheatsheet(course, lesson) {
  if (!course || !lesson) return null
  if (['vat-ly-1', 'vat-ly-2'].includes(course.id) && lesson.status !== 'ready') return null
  const key = `${course.id}/${lesson.slug}`
  if (cheatsheets[key]) {
    return cheatsheets[key]
  }

  // Synthesize a structured cheatsheet dynamically
  const slides = lectureSlides(course, lesson)
  const conceptIds = lectureConceptIds(lesson)
  const formulaSlides = slides.filter(s => Boolean(s.formula))
  const sections = []

  // 1. Core formulas from slides
  if (formulaSlides.length > 0) {
    sections.push({
      id: 'formulas',
      title: 'Công thức & Khẳng định cốt lõi',
      badge: 'Công thức',
      items: formulaSlides.map(s => ({
        name: s.title,
        formula: s.formula,
        bullets: s.bullets,
        example: s.example
      }))
    })
  }

  // 2. Key takeaways & rules from slides without formulas
  const otherSlides = slides.filter(s => !s.formula)
  if (otherSlides.length > 0) {
    sections.push({
      id: 'rules',
      title: 'Quy tắc & Điểm chốt bài giảng',
      badge: 'Quy tắc',
      items: otherSlides.map(s => ({
        name: s.title,
        bullets: s.bullets,
        example: s.example
      }))
    })
  }

  // 3. Prerequisite definitions & quick lookup symbols
  const validConcepts = conceptIds.filter(id => concepts[id])
  if (validConcepts.length > 0) {
    sections.push({
      id: 'concepts-ref',
      title: 'Ký hiệu & Thuật ngữ then chốt',
      badge: 'Tra cứu nhanh',
      items: validConcepts.map(id => {
        const item = concepts[id]
        return {
          name: item.name,
          formula: item.notation || '',
          description: item.definition,
          example: item.example ? `Ví dụ: ${item.example}` : ''
        }
      })
    })
  }

  return {
    summary: `Bảng tổng hợp nhanh các công thức, quy tắc cốt lõi và thuật ngữ trọng tâm của bài giảng ${lesson.title}.`,
    sections
  }
}
