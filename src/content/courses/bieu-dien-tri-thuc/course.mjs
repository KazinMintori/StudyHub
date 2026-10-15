import { lesson as lesson0 } from './lectures/01-gioi-thieu-tac-tu/lesson.mjs'
import { lesson as lesson1 } from './lectures/02-tim-kiem-mu/lesson.mjs'
import { lesson as lesson2 } from './lectures/03-tim-kiem-kinh-nghiem/lesson.mjs'
import { lesson as lesson3 } from './lectures/04-tim-kiem-doi-khang/lesson.mjs'
import { lesson as lesson4 } from './lectures/05-csp/lesson.mjs'
import { lesson as lesson5 } from './lectures/14-logic-bieu-dien-tri-thuc/lesson.mjs'
import { lesson as lesson6 } from './lectures/16-mang-bayes/lesson.mjs'
import { slides as slides0 } from './lectures/01-gioi-thieu-tac-tu/slides.mjs'
import { slides as slides1 } from './lectures/02-tim-kiem-mu/slides.mjs'
import { slides as slides2 } from './lectures/03-tim-kiem-kinh-nghiem/slides.mjs'
import { slides as slides3 } from './lectures/04-tim-kiem-doi-khang/slides.mjs'
import { slides as slides4 } from './lectures/05-csp/slides.mjs'
import { slides as slides5 } from './lectures/14-logic-bieu-dien-tri-thuc/slides.mjs'
import { slides as slides6 } from './lectures/16-mang-bayes/slides.mjs'

export const course = {
  "id": "bieu-dien-tri-thuc",
  "code": "01",
  "name": "Biểu diễn tri thức & Tìm kiếm",
  "short": "Tri thức & Tìm kiếm",
  "current": true,
  "description": "Mô hình hóa bài toán, chọn cách tìm kiếm và biểu diễn tri thức để suy luận.",
  "foundations": [
  "tap-hop",
  "menh-de",
  "luong-tu",
  "do-thi",
  "cay",
  "trang-thai",
  "hang-doi",
  "ngan-xep",
  "hang-doi-uu-tien",
  "do-phuc-tap",
  "heuristic",
  "xac-suat-co-dieu-kien",
  "doc-lap"
],
  "parts": [
  {
    "title": "Phần 1. Tổng quan và tác tử thông minh",
    "description": "Đặc tả tác tử, môi trường và cấu trúc giải quyết bài toán.",
    "lessons": [
      "01-gioi-thieu-tac-tu"
    ]
  },
  {
    "title": "Phần 2. Không gian trạng thái và thuật toán tìm kiếm",
    "description": "Chiến lược tìm kiếm mù và tìm kiếm kinh nghiệm Heuristic, A*.",
    "lessons": [
      "02-tim-kiem-mu",
      "03-tim-kiem-kinh-nghiem"
    ]
  },
  {
    "title": "Phần 3. Tìm kiếm đối kháng và bài toán ràng buộc",
    "description": "Thuật toán Minimax, cắt tỉa Alpha-Beta và bài toán thỏa mãn ràng buộc.",
    "lessons": [
      "04-tim-kiem-doi-khang",
      "05-csp"
    ]
  },
  {
    "title": "Phần 4. Biểu diễn tri thức và suy luận",
    "description": "Logic vị từ, luật suy diễn và mô hình mạng Bayes.",
    "lessons": [
      "14-logic-bieu-dien-tri-thuc",
      "16-mang-bayes"
    ]
  }
],
  "illustration": "search",
  lessons: [lesson0, lesson1, lesson2, lesson3, lesson4, lesson5, lesson6],
  slides: [...slides0, ...slides1, ...slides2, ...slides3, ...slides4, ...slides5, ...slides6]
}
