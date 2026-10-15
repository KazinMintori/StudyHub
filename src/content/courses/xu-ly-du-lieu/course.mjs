import { lesson as lesson0 } from './lectures/bai-01-tong-quan-cong-cu-chinh-sach-ai/lesson.mjs'
import { lesson as lesson1 } from './lectures/bai-02-python-co-ban/lesson.mjs'
import { lesson as lesson2 } from './lectures/bai-03-numpy/lesson.mjs'
import { lesson as lesson3 } from './lectures/bai-04-lam-quen-pandas/lesson.mjs'
import { lesson as lesson4 } from './lectures/bai-05-series-dataframe-chuyen-sau/lesson.mjs'
import { lesson as lesson5 } from './lectures/bai-06-ket-noi-truy-xuat-du-lieu/lesson.mjs'
import { lesson as lesson6 } from './lectures/bai-07-xu-ly-chuoi/lesson.mjs'
import { lesson as lesson7 } from './lectures/bai-08-du-lieu-thoi-gian/lesson.mjs'
import { lesson as lesson8 } from './lectures/bai-10-lam-sach-du-lieu/lesson.mjs'
import { lesson as lesson9 } from './lectures/bai-11-llm-du-lieu-phi-cau-truc/lesson.mjs'
import { lesson as lesson10 } from './lectures/bai-12-truc-quan-hoa-co-ban/lesson.mjs'
import { lesson as lesson11 } from './lectures/bai-13-truc-quan-hoa-nang-cao/lesson.mjs'
import { lesson as lesson12 } from './lectures/bai-14-ke-chuyen-bang-du-lieu/lesson.mjs'
import { slides as slides0 } from './lectures/bai-01-tong-quan-cong-cu-chinh-sach-ai/slides.mjs'
import { slides as slides1 } from './lectures/bai-02-python-co-ban/slides.mjs'
import { slides as slides2 } from './lectures/bai-03-numpy/slides.mjs'
import { slides as slides3 } from './lectures/bai-04-lam-quen-pandas/slides.mjs'
import { slides as slides4 } from './lectures/bai-05-series-dataframe-chuyen-sau/slides.mjs'
import { slides as slides5 } from './lectures/bai-06-ket-noi-truy-xuat-du-lieu/slides.mjs'
import { slides as slides6 } from './lectures/bai-07-xu-ly-chuoi/slides.mjs'
import { slides as slides7 } from './lectures/bai-08-du-lieu-thoi-gian/slides.mjs'
import { slides as slides8 } from './lectures/bai-10-lam-sach-du-lieu/slides.mjs'
import { slides as slides9 } from './lectures/bai-11-llm-du-lieu-phi-cau-truc/slides.mjs'
import { slides as slides10 } from './lectures/bai-12-truc-quan-hoa-co-ban/slides.mjs'
import { slides as slides11 } from './lectures/bai-13-truc-quan-hoa-nang-cao/slides.mjs'
import { slides as slides12 } from './lectures/bai-14-ke-chuyen-bang-du-lieu/slides.mjs'

export const course = {
  "id": "xu-ly-du-lieu",
  "code": "04",
  "name": "Lập trình xử lý dữ liệu",
  "short": "Xử lý dữ liệu",
  "current": true,
  "description": "Học theo Python for Data Analysis: Từ Python, NumPy và pandas đến làm sạch, trực quan hóa và kiểm tra kết luận.",
  "foundations": [
  "bien-kieu",
  "list",
  "dictionary",
  "ham-lap-trinh",
  "vong-lap",
  "mang",
  "chi-muc",
  "con-tro",
  "vector-hoa",
  "broadcasting",
  "gia-tri-thieu",
  "dataframe",
  "groupby",
  "thong-ke-mo-ta"
],
  "parts": [
  {
    "title": "Phần 1. Công cụ và Python",
    "description": "Đặt câu hỏi, dựng môi trường và viết các bước xử lý bằng Python.",
    "lessons": [
      "bai-01-tong-quan-cong-cu-chinh-sach-ai",
      "bai-02-python-co-ban"
    ]
  },
  {
    "title": "Phần 2. NumPy và pandas",
    "description": "Tính trên mảng, chọn dữ liệu bảng, tổng hợp nhóm, nối và chuyển dạng.",
    "lessons": [
      "bai-03-numpy",
      "bai-04-lam-quen-pandas",
      "bai-05-series-dataframe-chuyen-sau"
    ]
  },
  {
    "title": "Phần 3. Nạp, chuẩn hóa và làm sạch dữ liệu",
    "description": "Đọc tệp và SQL, xử lý chuỗi, thời gian, giá trị thiếu và dữ liệu không hợp lệ.",
    "lessons": [
      "bai-06-ket-noi-truy-xuat-du-lieu",
      "bai-07-xu-ly-chuoi",
      "bai-08-du-lieu-thoi-gian",
      "bai-10-lam-sach-du-lieu"
    ]
  },
  {
    "title": "Phần 4. Trích xuất văn bản bằng LLM",
    "description": "Phần bổ sung: Schema, kiểm tra phản hồi và đánh giá trên mẫu đã gán nhãn.",
    "lessons": [
      "bai-11-llm-du-lieu-phi-cau-truc"
    ]
  },
  {
    "title": "Phần 5. Biểu đồ và kết luận",
    "description": "Chọn biểu đồ, đọc thang đo và kiểm tra mẫu số, cơ cấu nhóm và phạm vi kết luận.",
    "lessons": [
      "bai-12-truc-quan-hoa-co-ban",
      "bai-13-truc-quan-hoa-nang-cao",
      "bai-14-ke-chuyen-bang-du-lieu"
    ]
  }
],
  "illustration": "broadcast",
  lessons: [lesson0, lesson1, lesson2, lesson3, lesson4, lesson5, lesson6, lesson7, lesson8, lesson9, lesson10, lesson11, lesson12],
  slides: [...slides0, ...slides1, ...slides2, ...slides3, ...slides4, ...slides5, ...slides6, ...slides7, ...slides8, ...slides9, ...slides10, ...slides11, ...slides12]
}
