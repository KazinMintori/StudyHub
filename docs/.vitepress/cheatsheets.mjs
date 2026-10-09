import { concepts } from './concepts.mjs'
import { lectureSlides, lectureConceptIds } from './lecture-model.mjs'
import { physicsMotionCheatsheet } from './physics-motion-course.mjs'

export const cheatsheets = { 'vat-ly-1/02-chuyen-dong-thang': physicsMotionCheatsheet }

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
