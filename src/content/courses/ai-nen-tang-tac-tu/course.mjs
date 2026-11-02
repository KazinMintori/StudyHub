import { lessons as lessonsA, slides as slidesA } from './parts/part-a.mjs'
import { lessons as lessonsC, slides as slidesC } from './parts/part-c.mjs'

export const id = 'ai-nen-tang-tac-tu'
export const name = 'Trí tuệ nhân tạo: Nền tảng của tác tử tính toán'
export const description = 'Giáo trình trí tuệ nhân tạo tiếp cận theo hướng tác tử tính toán, bao gồm biểu diễn tri thức, lập luận logic, lập kế hoạch và học máy.'
export const collection = 'extended'

export const source = {
  title: 'Artificial Intelligence: Foundations of Computational Agents',
  authors: ['David L. Poole', 'Alan K. Mackworth'],
  edition: 3,
  year: 2023,
  publisher: 'Cambridge University Press',
  url: 'https://artint.info/3e/html/ArtInt3e.html',
  kind: 'book',
  permission: 'user-confirmed'
}

export const parts = [
  {
    title: 'Phần I: Tác tử trong thế giới thực',
    lessons: [
      '01-tri-tue-nhan-tao-va-tac-tu'
    ]
  },
  {
    title: 'Phần II: Suy luận và lập kế hoạch trong điều kiện chắc chắn',
    lessons: [
      '05-menh-de-va-suy-dien'
    ]
  },
  {
    title: 'Phần V: Biểu diễn cá thể và quan hệ',
    lessons: [
      '15-ca-the-va-quan-he'
    ]
  }
]

export const lessons = [
  ...(lessonsA || []),
  ...(lessonsC || [])
]

export const slides = [
  ...(slidesA || []),
  ...(slidesC || [])
]

export const course = {
  id,
  code: 'ARTINT3E',
  name,
  short: 'Nền tảng tác tử AI',
  illustration: 'search',
  description,
  collection,
  source,
  parts,
  lessons,
  slides
}

export default course
