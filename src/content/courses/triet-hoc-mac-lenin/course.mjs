import { lesson as chapter1 } from './lectures/chuong-1-triet-hoc-va-vai-tro/lesson.mjs'
import { lesson as chapter2 } from './lectures/chuong-2-chu-nghia-duy-vat-bien-chung/lesson.mjs'
import { lesson as chapter3 } from './lectures/chuong-3-chu-nghia-duy-vat-lich-su/lesson.mjs'

export const course = {
  "id": "triet-hoc-mac-lenin",
  "code": "10",
  "name": "Triết học Mác – Lênin",
  "short": "Triết học",
  "current": true,
  "description": "Ba chương tóm lược về triết học, chủ nghĩa duy vật biện chứng và chủ nghĩa duy vật lịch sử. Mỗi chủ đề đi liền với bài tập vận dụng.",
  "presentation": "philosophy",
  "foundations": [],
  "parts": [
    {
      "title": "Chương 1",
      "lessons": [
        "chuong-1-triet-hoc-va-vai-tro"
      ]
    },
    {
      "title": "Chương 2",
      "lessons": [
        "chuong-2-chu-nghia-duy-vat-bien-chung"
      ]
    },
    {
      "title": "Chương 3",
      "lessons": [
        "chuong-3-chu-nghia-duy-vat-lich-su"
      ]
    }
  ],
  lessons: [chapter1, chapter2, chapter3],
  slides: []
}
