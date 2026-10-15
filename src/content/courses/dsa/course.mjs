import { lesson as lesson0 } from './lectures/complexity/lesson.mjs'
import { lesson as lesson1 } from './lectures/sorting/lesson.mjs'
import { lesson as lesson2 } from './lectures/searching/lesson.mjs'
import { lesson as lesson3 } from './lectures/trees/lesson.mjs'
import { lesson as lesson4 } from './lectures/graphs/lesson.mjs'
import { slides as slides0 } from './lectures/complexity/slides.mjs'
import { slides as slides1 } from './lectures/sorting/slides.mjs'
import { slides as slides2 } from './lectures/searching/slides.mjs'
import { slides as slides3 } from './lectures/trees/slides.mjs'
import { slides as slides4 } from './lectures/graphs/slides.mjs'

export const course = {
  "id": "dsa",
  "code": "07",
  "name": "Cấu trúc dữ liệu & Giải thuật",
  "short": "CTDL & Giải thuật",
  "current": true,
  "description": "Chọn cấu trúc lưu dữ liệu và đánh giá chi phí của từng cách xử lý.",
  "foundations": [
  "mang",
  "con-tro",
  "de-quy",
  "hang-doi",
  "ngan-xep",
  "cay",
  "do-thi",
  "do-phuc-tap",
  "quy-nap"
],
  "parts": [
  {
    "title": "Phần 1. Độ phức tạp và đánh giá thuật toán",
    "description": "Đánh giá thời gian và không gian qua ký hiệu Big-O và phương pháp quy nạp.",
    "lessons": [
      "complexity"
    ]
  },
  {
    "title": "Phần 2. Thuật toán sắp xếp và tìm kiếm",
    "description": "Các thuật toán sắp xếp kinh điển và tìm kiếm nhị phân trên dãy có thứ tự.",
    "lessons": [
      "sorting",
      "searching"
    ]
  },
  {
    "title": "Phần 3. Cấu trúc dữ liệu cây và đồ thị",
    "description": "Cây nhị phân, cây tìm kiếm, đồ thị và các thuật toán duyệt BFS, DFS.",
    "lessons": [
      "trees",
      "graphs"
    ]
  }
],
  "illustration": "search",
  lessons: [lesson0, lesson1, lesson2, lesson3, lesson4],
  slides: [...slides0, ...slides1, ...slides2, ...slides3, ...slides4]
}
