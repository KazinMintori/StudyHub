import { lesson as lesson0 } from './lectures/bai-01-tong-quan-cong-cu-chinh-sach-ai/lesson.mjs'
import { slides as slides0 } from './lectures/bai-01-tong-quan-cong-cu-chinh-sach-ai/slides.mjs'
import { lesson as lesson1 } from './lectures/bai-02-python-co-ban/lesson.mjs'
import { slides as slides1 } from './lectures/bai-02-python-co-ban/slides.mjs'
import { lesson as lesson2 } from './lectures/bai-03-cau-truc-du-lieu-ham-tep/lesson.mjs'
import { slides as slides2 } from './lectures/bai-03-cau-truc-du-lieu-ham-tep/slides.mjs'
import { lesson as lesson3 } from './lectures/bai-03-numpy/lesson.mjs'
import { slides as slides3 } from './lectures/bai-03-numpy/slides.mjs'
import { lesson as lesson4 } from './lectures/bai-04-lam-quen-pandas/lesson.mjs'
import { slides as slides4 } from './lectures/bai-04-lam-quen-pandas/slides.mjs'
import { lesson as lesson5 } from './lectures/bai-06-ket-noi-truy-xuat-du-lieu/lesson.mjs'
import { slides as slides5 } from './lectures/bai-06-ket-noi-truy-xuat-du-lieu/slides.mjs'
import { lesson as lesson6 } from './lectures/bai-10-lam-sach-du-lieu/lesson.mjs'
import { slides as slides6 } from './lectures/bai-10-lam-sach-du-lieu/slides.mjs'
import { lesson as lesson7 } from './lectures/bai-08-ghep-bang-chuyen-dang/lesson.mjs'
import { slides as slides7 } from './lectures/bai-08-ghep-bang-chuyen-dang/slides.mjs'
import { lesson as lesson8 } from './lectures/bai-12-truc-quan-hoa-co-ban/lesson.mjs'
import { slides as slides8 } from './lectures/bai-12-truc-quan-hoa-co-ban/slides.mjs'
import { lesson as lesson9 } from './lectures/bai-10-tong-hop-theo-nhom/lesson.mjs'
import { slides as slides9 } from './lectures/bai-10-tong-hop-theo-nhom/slides.mjs'
import { lesson as lesson10 } from './lectures/bai-08-du-lieu-thoi-gian/lesson.mjs'
import { slides as slides10 } from './lectures/bai-08-du-lieu-thoi-gian/slides.mjs'
import { lesson as lesson11 } from './lectures/bai-12-mo-hinh-hoa/lesson.mjs'
import { slides as slides11 } from './lectures/bai-12-mo-hinh-hoa/slides.mjs'
import { lesson as lesson12 } from './lectures/bai-14-ke-chuyen-bang-du-lieu/lesson.mjs'
import { slides as slides12 } from './lectures/bai-14-ke-chuyen-bang-du-lieu/slides.mjs'
import { lesson as lesson13 } from './lectures/phu-luc-a-numpy-nang-cao/lesson.mjs'
import { slides as slides13 } from './lectures/phu-luc-a-numpy-nang-cao/slides.mjs'
import { lesson as lesson14 } from './lectures/phu-luc-b-ipython/lesson.mjs'
import { slides as slides14 } from './lectures/phu-luc-b-ipython/slides.mjs'

export const course = {
  id: "xu-ly-du-lieu",
  code: "04",
  name: "Lập trình xử lý dữ liệu",
  short: "Xử lý dữ liệu",
  current: true,
  description: "Mười ba chương và hai phụ lục: Python, NumPy, pandas, dữ liệu, biểu đồ, mô hình và kiểm tra kết luận.",
  foundations: [
  "bien-kieu",
  "list",
  "dictionary",
  "ham-lap-trinh",
  "vong-lap",
  "mang",
  "chi-muc",
  "vector-hoa",
  "broadcasting",
  "gia-tri-thieu",
  "dataframe",
  "groupby",
  "thong-ke-mo-ta"
],
  parts: [
  {
    "title": "Phần 1. Công cụ và ngôn ngữ Python",
    "description": "Từ môi trường làm việc đến cấu trúc dữ liệu, hàm và tệp.",
    "lessons": [
      "bai-01-tong-quan-cong-cu-chinh-sach-ai",
      "bai-02-python-co-ban",
      "bai-03-cau-truc-du-lieu-ham-tep"
    ]
  },
  {
    "title": "Phần 2. Mảng và bảng dữ liệu",
    "description": "Tính toán bằng NumPy và làm việc với nhãn trong pandas.",
    "lessons": [
      "bai-03-numpy",
      "bai-04-lam-quen-pandas"
    ]
  },
  {
    "title": "Phần 3. Nạp, làm sạch và tổ chức dữ liệu",
    "description": "Đọc đúng dữ liệu, kiểm tra chất lượng, ghép bảng và chuyển dạng.",
    "lessons": [
      "bai-06-ket-noi-truy-xuat-du-lieu",
      "bai-10-lam-sach-du-lieu",
      "bai-08-ghep-bang-chuyen-dang"
    ]
  },
  {
    "title": "Phần 4. Biểu đồ, nhóm và thời gian",
    "description": "Quan sát phân phối, tổng hợp đúng đơn vị và phân tích theo lịch.",
    "lessons": [
      "bai-12-truc-quan-hoa-co-ban",
      "bai-10-tong-hop-theo-nhom",
      "bai-08-du-lieu-thoi-gian"
    ]
  },
  {
    "title": "Phần 5. Mô hình và các bài toán phân tích",
    "description": "Đưa dữ liệu vào mô hình và kiểm tra kết luận qua nhiều dạng bài toán.",
    "lessons": [
      "bai-12-mo-hinh-hoa",
      "bai-14-ke-chuyen-bang-du-lieu"
    ]
  },
  {
    "title": "Phụ lục",
    "description": "Tra cứu NumPy nâng cao và các công cụ của IPython.",
    "lessons": [
      "phu-luc-a-numpy-nang-cao",
      "phu-luc-b-ipython"
    ]
  }
],
  illustration: "broadcast",
  lessons: [{ ...lesson0, number: "1" }, { ...lesson1, number: "2" }, { ...lesson2, number: "3" }, { ...lesson3, number: "4" }, { ...lesson4, number: "5" }, { ...lesson5, number: "6" }, { ...lesson6, number: "7" }, { ...lesson7, number: "8" }, { ...lesson8, number: "9" }, { ...lesson9, number: "10" }, { ...lesson10, number: "11" }, { ...lesson11, number: "12" }, { ...lesson12, number: "13" }, { ...lesson13, number: "A" }, { ...lesson14, number: "B" }],
  slides: [...slides0, ...slides1, ...slides2, ...slides3, ...slides4, ...slides5, ...slides6, ...slides7, ...slides8, ...slides9, ...slides10, ...slides11, ...slides12, ...slides13, ...slides14]
}
