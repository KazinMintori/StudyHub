import { lesson as lesson0 } from './lectures/01-hieu-the-gioi-bang-du-lieu/lesson.mjs'
import { lesson as lesson1 } from './lectures/02-phan-loai-du-lieu/lesson.mjs'
import { lesson as lesson2 } from './lectures/03-tom-tat-du-lieu-dinh-tinh/lesson.mjs'
import { lesson as lesson3 } from './lectures/04-tom-tat-du-lieu-dinh-luong/lesson.mjs'
import { lesson as lesson4 } from './lectures/05-ngu-phap-do-hoa/lesson.mjs'
import { lesson as lesson5 } from './lectures/06-phan-tich-co-dieu-kien/lesson.mjs'
import { lesson as lesson6 } from './lectures/07-tom-tat-lien-he-bien-so/lesson.mjs'
import { lesson as lesson7 } from './lectures/08-hoi-quy-tuyen-tinh-boi/lesson.mjs'
import { lesson as lesson8 } from './lectures/09-co-so-xac-suat/lesson.mjs'
import { lesson as lesson9 } from './lectures/10-tinh-toan-xac-suat/lesson.mjs'
import { lesson as lesson10 } from './lectures/11-phan-phoi-xac-suat/lesson.mjs'
import { lesson as lesson11 } from './lectures/12-bien-ngau-nhien/lesson.mjs'
import { lesson as lesson12 } from './lectures/13-ky-vong-va-sai-so-chuan/lesson.mjs'
import { lesson as lesson13 } from './lectures/14-phan-phoi-lien-tuc-va-xap-xi-chuan/lesson.mjs'
import { lesson as lesson14 } from './lectures/15-tu-mau-den-tong-the/lesson.mjs'
import { lesson as lesson15 } from './lectures/16-khoang-tin-cay/lesson.mjs'
import { lesson as lesson16 } from './lectures/17-phuong-phap-bootstrapping/lesson.mjs'
import { lesson as lesson17 } from './lectures/18-kiem-dinh-gia-thuyet-1/lesson.mjs'
import { lesson as lesson18 } from './lectures/19-kiem-dinh-gia-thuyet-2/lesson.mjs'
import { lesson as lesson19 } from './lectures/20-sai-lech-do-thiet-ke/lesson.mjs'
import { lesson as lesson20 } from './lectures/21-dinh-nghia-nhan-qua/lesson.mjs'
import { lesson as lesson21 } from './lectures/22-thi-nghiem-ngau-nhien/lesson.mjs'
import { lesson as lesson22 } from './lectures/23-tac-dong-nhan-qua-nghien-cuu-quan-sat/lesson.mjs'
import { lesson as lesson23 } from './lectures/24-phuong-phap-binh-phuong-be-nhat/lesson.mjs'
import { lesson as lesson24 } from './lectures/25-danh-gia-va-cai-thien-du-doan/lesson.mjs'
import { lesson as lesson25 } from './lectures/26-hien-tuong-qua-khop/lesson.mjs'
import { lesson as lesson26 } from './lectures/27-hoi-quy-logistic/lesson.mjs'
import { slides as slides0 } from './lectures/01-hieu-the-gioi-bang-du-lieu/slides.mjs'
import { slides as slides1 } from './lectures/02-phan-loai-du-lieu/slides.mjs'
import { slides as slides2 } from './lectures/03-tom-tat-du-lieu-dinh-tinh/slides.mjs'
import { slides as slides3 } from './lectures/04-tom-tat-du-lieu-dinh-luong/slides.mjs'
import { slides as slides4 } from './lectures/05-ngu-phap-do-hoa/slides.mjs'
import { slides as slides5 } from './lectures/06-phan-tich-co-dieu-kien/slides.mjs'
import { slides as slides6 } from './lectures/07-tom-tat-lien-he-bien-so/slides.mjs'
import { slides as slides7 } from './lectures/08-hoi-quy-tuyen-tinh-boi/slides.mjs'
import { slides as slides8 } from './lectures/09-co-so-xac-suat/slides.mjs'
import { slides as slides9 } from './lectures/10-tinh-toan-xac-suat/slides.mjs'
import { slides as slides10 } from './lectures/11-phan-phoi-xac-suat/slides.mjs'
import { slides as slides11 } from './lectures/12-bien-ngau-nhien/slides.mjs'
import { slides as slides12 } from './lectures/13-ky-vong-va-sai-so-chuan/slides.mjs'
import { slides as slides13 } from './lectures/14-phan-phoi-lien-tuc-va-xap-xi-chuan/slides.mjs'
import { slides as slides14 } from './lectures/15-tu-mau-den-tong-the/slides.mjs'
import { slides as slides15 } from './lectures/16-khoang-tin-cay/slides.mjs'
import { slides as slides16 } from './lectures/17-phuong-phap-bootstrapping/slides.mjs'
import { slides as slides17 } from './lectures/18-kiem-dinh-gia-thuyet-1/slides.mjs'
import { slides as slides18 } from './lectures/19-kiem-dinh-gia-thuyet-2/slides.mjs'
import { slides as slides19 } from './lectures/20-sai-lech-do-thiet-ke/slides.mjs'
import { slides as slides20 } from './lectures/21-dinh-nghia-nhan-qua/slides.mjs'
import { slides as slides21 } from './lectures/22-thi-nghiem-ngau-nhien/slides.mjs'
import { slides as slides22 } from './lectures/23-tac-dong-nhan-qua-nghien-cuu-quan-sat/slides.mjs'
import { slides as slides23 } from './lectures/24-phuong-phap-binh-phuong-be-nhat/slides.mjs'
import { slides as slides24 } from './lectures/25-danh-gia-va-cai-thien-du-doan/slides.mjs'
import { slides as slides25 } from './lectures/26-hien-tuong-qua-khop/slides.mjs'
import { slides as slides26 } from './lectures/27-hoi-quy-logistic/slides.mjs'

export const course = {
  "id": "xac-suat-thong-ke",
  "code": "03",
  "name": "Xác suất thống kê",
  "short": "Xác suất thống kê",
  "current": true,
  problemSets: [
    { slug: 'problem-set-01', title: 'Problem Set 01: Câu hỏi và dữ liệu' }
  ],
  "description": "Học theo UC Berkeley STAT 20: Từ câu hỏi nghiên cứu, dữ liệu quan sát, tóm tắt trực quan đến suy rộng thống kê, quan hệ nhân quả và mô hình dự đoán.",
  "foundations": [
  "thong-ke-mo-ta",
  "suy-rong-thong-ke",
  "mau-tong-the",
  "ket-luan-nhan-qua",
  "du-doan-thong-ke",
  "tap-hop",
  "khong-gian-mau",
  "to-hop",
  "xac-suat-co-dieu-kien",
  "doc-lap",
  "bien-ngau-nhien",
  "ky-vong",
  "phuong-sai",
  "tich-phan",
  "dataframe"
],
  "parts": [
  {
    "title": "Phần 1. Câu hỏi và dữ liệu",
    "description": "Phân loại các phát biểu thống kê, cấu trúc bảng dữ liệu và thu thập quan sát.",
    "lessons": [
      "01-hieu-the-gioi-bang-du-lieu",
      "02-phan-loai-du-lieu"
    ]
  },
  {
    "title": "Phần 2. Tóm tắt dữ liệu",
    "description": "Tóm tắt dữ liệu định tính, định lượng, ngữ pháp đồ họa và mô hình hồi quy.",
    "lessons": [
      "03-tom-tat-du-lieu-dinh-tinh",
      "04-tom-tat-du-lieu-dinh-luong",
      "05-ngu-phap-do-hoa",
      "06-phan-tich-co-dieu-kien",
      "07-tom-tat-lien-he-bien-so",
      "08-hoi-quy-tuyen-tinh-boi"
    ]
  },
  {
    "title": "Phần 3. Suy rộng thống kê",
    "description": "Cơ sở xác suất, biến ngẫu nhiên, phân phối mẫu, khoảng tin cậy và kiểm định giả thuyết.",
    "lessons": [
      "09-co-so-xac-suat",
      "10-tinh-toan-xac-suat",
      "11-phan-phoi-xac-suat",
      "12-bien-ngau-nhien",
      "13-ky-vong-va-sai-so-chuan",
      "14-phan-phoi-lien-tuc-va-xap-xi-chuan",
      "15-tu-mau-den-tong-the",
      "16-khoang-tin-cay",
      "17-phuong-phap-bootstrapping",
      "18-kiem-dinh-gia-thuyet-1",
      "19-kiem-dinh-gia-thuyet-2",
      "20-sai-lech-do-thiet-ke"
    ]
  },
  {
    "title": "Phần 4. Quan hệ nhân quả",
    "description": "Định nghĩa nhân quả, thí nghiệm ngẫu nhiên có đối chứng và suy luận trong nghiên cứu quan sát.",
    "lessons": [
      "21-dinh-nghia-nhan-qua",
      "22-thi-nghiem-ngau-nhien",
      "23-tac-dong-nhan-qua-nghien-cuu-quan-sat"
    ]
  },
  {
    "title": "Phần 5. Mô hình dự đoán",
    "description": "Phương pháp bình phương bé nhất, đánh giá sai số, hiện tượng quá khớp và hồi quy Logistic.",
    "lessons": [
      "24-phuong-phap-binh-phuong-be-nhat",
      "25-danh-gia-va-cai-thien-du-doan",
      "26-hien-tuong-qua-khop",
      "27-hoi-quy-logistic"
    ]
  }
],
  "illustration": "bayes",
  "contentPolicy": "full-source-translation",
  lessons: [lesson0, lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8, lesson9, lesson10, lesson11, lesson12, lesson13, lesson14, lesson15, lesson16, lesson17, lesson18, lesson19, lesson20, lesson21, lesson22, lesson23, lesson24, lesson25, lesson26],
  slides: [...slides0, ...slides1, ...slides2, ...slides3, ...slides4, ...slides5, ...slides6, ...slides7, ...slides8, ...slides9, ...slides10, ...slides11, ...slides12, ...slides13, ...slides14, ...slides15, ...slides16, ...slides17, ...slides18, ...slides19, ...slides20, ...slides21, ...slides22, ...slides23, ...slides24, ...slides25, ...slides26]
}
