import { lesson as lesson0 } from './lectures/bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan/lesson.mjs'
import { lesson as lesson1 } from './lectures/bai-02-mapreduce-va-xu-ly-du-lieu-lon/lesson.mjs'
import { lesson as lesson2 } from './lectures/bai-03-pagerank-mo-hinh-va-tinh-toan/lesson.mjs'
import { slides as slides0 } from './lectures/bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan/slides.mjs'
import { slides as slides1 } from './lectures/bai-02-mapreduce-va-xu-ly-du-lieu-lon/slides.mjs'
import { slides as slides2 } from './lectures/bai-03-pagerank-mo-hinh-va-tinh-toan/slides.mjs'

export const course = {
  "id": "giai-thuat-du-lieu",
  "code": "06",
  "name": "Giải thuật nền tảng của Khoa học dữ liệu",
  "short": "Giải thuật dữ liệu",
  "current": true,
  "description": "Đặc tả dữ liệu lớn, tính toán phân tán MapReduce, thuật toán PageRank và xử lý đồ thị quy mô lớn.",
  "foundations": [
  "do-phuc-tap",
  "ham-lap-trinh",
  "dictionary",
  "khoa-gia-tri",
  "bam",
  "phan-tan",
  "ket-hop",
  "vector",
  "ma-tran",
  "do-thi",
  "xac-suat-co-dieu-kien"
],
  "parts": [
  {
    "title": "Phần 1. Nền tảng dữ liệu lớn và mô hình thuật toán",
    "description": "Đặc tả bài toán, độ đo khoảng cách, tiêu chuẩn đánh giá và nguyên lý Bonferroni.",
    "lessons": [
      "bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan"
    ]
  },
  {
    "title": "Phần 2. Tính toán phân tán MapReduce",
    "description": "Mô hình lập trình Map/Shuffle/Reduce/Combine, nhân ma trận lớn và mô hình chi phí cụm máy.",
    "lessons": [
      "bai-02-mapreduce-va-xu-ly-du-lieu-lon"
    ]
  },
  {
    "title": "Phần 3. Phân tích đồ thị và thuật toán PageRank",
    "description": "Mô hình Random Surfer, Power Iteration, xử lý Dead Ends, Spider Traps và Damping Factor.",
    "lessons": [
      "bai-03-pagerank-mo-hinh-va-tinh-toan"
    ]
  }
],
  "illustration": "mapreduce",
  lessons: [lesson0, lesson1, lesson2],
  slides: [...slides0, ...slides1, ...slides2]
}
