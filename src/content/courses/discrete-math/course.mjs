import { lesson as lesson0 } from './lectures/logic/lesson.mjs'
import { lesson as lesson1 } from './lectures/relations/lesson.mjs'
import { lesson as lesson2 } from './lectures/graph-theory/lesson.mjs'
import { slides as slides0 } from './lectures/logic/slides.mjs'
import { slides as slides1 } from './lectures/relations/slides.mjs'
import { slides as slides2 } from './lectures/graph-theory/slides.mjs'

export const course = {
  "id": "discrete-math",
  "code": "08",
  "name": "Toán rời rạc",
  "short": "Toán rời rạc",
  "current": true,
  "description": "Đọc logic, quan hệ và cấu trúc hữu hạn bằng các định nghĩa chính xác.",
  "foundations": [
  "tap-hop",
  "ham-so",
  "menh-de",
  "luong-tu",
  "quy-nap",
  "to-hop",
  "quan-he",
  "do-thi",
  "cay"
],
  "parts": [
  {
    "title": "Phần 1. Logic mệnh đề và vị từ",
    "description": "Logic mệnh đề, bảng chân trị, logic vị từ và các lượng từ toán học.",
    "lessons": [
      "logic"
    ]
  },
  {
    "title": "Phần 2. Tập hợp, quan hệ và ánh xạ",
    "description": "Định nghĩa tập hợp, tích Descartes, quan hệ tương đương, thứ tự và hàm số.",
    "lessons": [
      "relations"
    ]
  },
  {
    "title": "Phần 3. Cơ sở lý thuyết đồ thị",
    "description": "Đỉnh, cạnh, đường đi, chu trình, đồ thị Euler, Hamilton và cây liên thông.",
    "lessons": [
      "graph-theory"
    ]
  }
],
  "illustration": "search",
  lessons: [lesson0, lesson1, lesson2],
  slides: [...slides0, ...slides1, ...slides2]
}
