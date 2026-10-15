import { mathAiReviewLesson } from './lectures/on-luyen/review-course.mjs'
import { lesson as lesson0 } from './lectures/bai-00-on-tap-nen-tang/lesson.mjs'
import { lesson as lesson1 } from './lectures/bai-01-nhap-mon-toi-uu/lesson.mjs'
import { lesson as lesson2 } from './lectures/bai-02-tap-loi/lesson.mjs'
import { lesson as lesson3 } from './lectures/bai-03-doi-ngau-lagrange/lesson.mjs'
import { lesson as lesson4 } from './lectures/bai-04-gradient-newton/lesson.mjs'
import { lesson as lesson5 } from './lectures/bai-05-toi-uu-huan-luyen/lesson.mjs'
import { lesson as lesson6 } from './lectures/bai-06-phuong-phap-thich-nghi/lesson.mjs'
import { lesson as lesson7 } from './lectures/bai-07-quy-hoach-tuyen-tinh-va-dong/lesson.mjs'
import { slides as slides0 } from './lectures/bai-00-on-tap-nen-tang/slides.mjs'
import { slides as slides1 } from './lectures/bai-01-nhap-mon-toi-uu/slides.mjs'
import { slides as slides2 } from './lectures/bai-02-tap-loi/slides.mjs'
import { slides as slides3 } from './lectures/bai-03-doi-ngau-lagrange/slides.mjs'
import { slides as slides4 } from './lectures/bai-04-gradient-newton/slides.mjs'
import { slides as slides5 } from './lectures/bai-05-toi-uu-huan-luyen/slides.mjs'
import { slides as slides6 } from './lectures/bai-06-phuong-phap-thich-nghi/slides.mjs'
import { slides as slides7 } from './lectures/bai-07-quy-hoach-tuyen-tinh-va-dong/slides.mjs'

export const course = {
  "id": "toan-cho-ai",
  "code": "02",
  "name": "Cơ sở toán cho AI",
  "short": "Toán cho AI",
  "current": true,
  "description": "Tám bài giảng từ kiến thức nền tới tối ưu lồi và huấn luyện mô hình, cùng tài liệu bốn buổi ôn tập có lời giải.",
  "foundations": [
  "ham-so",
  "dao-ham",
  "tap-hop",
  "vector",
  "tich-vo-huong",
  "gradient",
  "hessian",
  "ma-tran-psd",
  "tap-loi",
  "ham-loi",
  "chuan",
  "he-phuong-trinh",
  "kkt",
  "quy-tac-chuoi",
  "ky-vong",
  "phuong-sai",
  "ma-tran",
  "do-thi",
  "tham-so-toan-hoc",
  "dao-ham-rieng",
  "bien-ngau-nhien",
  "phan-phoi-gauss",
  "ma-tran-hiep-phuong-sai",
  "likelihood",
  "binh-phuong-toi-thieu",
  "to-hop-loi",
  "mien-kha-thi",
  "infimum",
  "epigraph",
  "dinh-luat-snell",
  "noi-long-toi-uu",
  "lagrangian",
  "ham-doi-ngau",
  "doi-ngau-manh",
  "dieu-kien-slater",
  "tim-kiem-duong",
  "tu-tuong-hop",
  "doc-lap",
  "gradient-ngau-nhien",
  "momentum-nesterov",
  "adagrad",
  "rmsprop",
  "adam",
  "gradient-lien-hop",
  "bfgs",
  "nghiem-co-so",
  "quy-hoach-dong",
  "trang-thai"
],
  "structureSource": "https://courses.iaidev.com/math-4-AI/2627-1/",
  "review": mathAiReviewLesson,
  "parts": [
  {
    "title": "Bài giảng",
    "lessons": [
      "bai-00-on-tap-nen-tang",
      "bai-01-nhap-mon-toi-uu",
      "bai-02-tap-loi",
      "bai-03-doi-ngau-lagrange",
      "bai-04-gradient-newton",
      "bai-05-toi-uu-huan-luyen",
      "bai-06-phuong-phap-thich-nghi",
      "bai-07-quy-hoach-tuyen-tinh-va-dong"
    ]
  }
],
  "illustration": "gradient",
  lessons: [lesson0, lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7],
  slides: [...slides0, ...slides1, ...slides2, ...slides3, ...slides4, ...slides5, ...slides6, ...slides7]
}
