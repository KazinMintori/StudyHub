import { lesson as lesson28 } from './lectures/28-dem-va-xac-suat-co-dien/lesson.mjs'
import { lesson as lesson29 } from './lectures/29-phan-phoi-roi-rac-mo-rong/lesson.mjs'
import { lesson as lesson30 } from './lectures/30-phan-phoi-lien-tuc-mo-rong/lesson.mjs'
import { lesson as lesson31 } from './lectures/31-vector-ngau-nhien-va-phan-phoi-dong-thoi/lesson.mjs'
import { lesson as lesson32 } from './lectures/32-hiep-phuong-sai-va-ky-vong-co-dieu-kien/lesson.mjs'
import { lesson as lesson33 } from './lectures/33-bien-doi-va-thong-ke-thu-tu/lesson.mjs'
import { lesson as lesson34 } from './lectures/34-momen-ham-sinh-va-bat-dang-thuc/lesson.mjs'
import { lesson as lesson35 } from './lectures/35-luat-so-lon-va-dinh-ly-gioi-han/lesson.mjs'
import { lesson as lesson36 } from './lectures/36-phan-phoi-mau-chinh-xac/lesson.mjs'
import { lesson as lesson37 } from './lectures/37-uoc-luong-diem-momen-va-hop-ly-cuc-dai/lesson.mjs'
import { lesson as lesson38 } from './lectures/38-tinh-du-va-hieu-qua-uoc-luong/lesson.mjs'
import { lesson as lesson39 } from './lectures/39-khoang-tin-cay-tham-so/lesson.mjs'
import { lesson as lesson40 } from './lectures/40-kiem-dinh-tham-so-va-cong-suat/lesson.mjs'
import { lesson as lesson41 } from './lectures/41-kiem-dinh-khi-binh-phuong/lesson.mjs'
import { lesson as lesson42 } from './lectures/42-phan-tich-phuong-sai/lesson.mjs'
import { lesson as lesson43 } from './lectures/43-suy-luan-hoi-quy-tuyen-tinh/lesson.mjs'
import { lesson as lesson44 } from './lectures/44-phuong-phap-phi-tham-so/lesson.mjs'
import { lesson as lesson45 } from './lectures/45-suy-luan-bayes-va-du-doan/lesson.mjs'
import { slides as slides28 } from './lectures/28-dem-va-xac-suat-co-dien/slides.mjs'
import { slides as slides29 } from './lectures/29-phan-phoi-roi-rac-mo-rong/slides.mjs'
import { slides as slides30 } from './lectures/30-phan-phoi-lien-tuc-mo-rong/slides.mjs'
import { slides as slides31 } from './lectures/31-vector-ngau-nhien-va-phan-phoi-dong-thoi/slides.mjs'
import { slides as slides32 } from './lectures/32-hiep-phuong-sai-va-ky-vong-co-dieu-kien/slides.mjs'
import { slides as slides33 } from './lectures/33-bien-doi-va-thong-ke-thu-tu/slides.mjs'
import { slides as slides34 } from './lectures/34-momen-ham-sinh-va-bat-dang-thuc/slides.mjs'
import { slides as slides35 } from './lectures/35-luat-so-lon-va-dinh-ly-gioi-han/slides.mjs'
import { slides as slides36 } from './lectures/36-phan-phoi-mau-chinh-xac/slides.mjs'
import { slides as slides37 } from './lectures/37-uoc-luong-diem-momen-va-hop-ly-cuc-dai/slides.mjs'
import { slides as slides38 } from './lectures/38-tinh-du-va-hieu-qua-uoc-luong/slides.mjs'
import { slides as slides39 } from './lectures/39-khoang-tin-cay-tham-so/slides.mjs'
import { slides as slides40 } from './lectures/40-kiem-dinh-tham-so-va-cong-suat/slides.mjs'
import { slides as slides41 } from './lectures/41-kiem-dinh-khi-binh-phuong/slides.mjs'
import { slides as slides42 } from './lectures/42-phan-tich-phuong-sai/slides.mjs'
import { slides as slides43 } from './lectures/43-suy-luan-hoi-quy-tuyen-tinh/slides.mjs'
import { slides as slides44 } from './lectures/44-phuong-phap-phi-tham-so/slides.mjs'
import { slides as slides45 } from './lectures/45-suy-luan-bayes-va-du-doan/slides.mjs'

const support = {
  28: ['to-hop', 'khong-gian-mau'],
  29: ['bien-ngau-nhien', 'ky-vong', 'phuong-sai'],
  30: ['tich-phan', 'phan-phoi-gauss'],
  31: ['phan-phoi-dong-thoi', 'doc-lap'],
  32: ['hiep-phuong-sai', 'ky-vong-co-dieu-kien', 'ma-tran-hiep-phuong-sai'],
  33: ['phan-phoi-dong-thoi', 'tich-phan'],
  34: ['ham-sinh-momen', 'ky-vong'],
  35: ['luat-so-lon', 'dinh-ly-gioi-han-trung-tam'],
  36: ['phan-phoi-mau', 'uoc-luong-khong-chech'],
  37: ['uoc-luong-hop-ly-cuc-dai', 'likelihood', 'uoc-luong-khong-chech'],
  38: ['thong-ke-du', 'thong-tin-fisher'],
  39: ['khoang-tin-cay', 'phan-phoi-mau'],
  40: ['kiem-dinh-gia-thuyet', 'cong-suat-kiem-dinh'],
  41: ['kiem-dinh-gia-thuyet', 'doc-lap'],
  42: ['phan-tich-phuong-sai'],
  43: ['khoang-tin-cay', 'binh-phuong-toi-thieu'],
  44: ['kiem-dinh-gia-thuyet'],
  45: ['likelihood', 'phan-phoi-tien-nghiem', 'phan-phoi-hau-nghiem', 'ky-vong-co-dieu-kien'],
}

export const classicalLessons = [lesson28, lesson29, lesson30, lesson31, lesson32, lesson33, lesson34, lesson35, lesson36, lesson37, lesson38, lesson39, lesson40, lesson41, lesson42, lesson43, lesson44, lesson45].map((lesson, index) => ({
  ...lesson,
  supplementary: true,
  supplementNumber: index + 1,
  displayNumber: `BT${String(index + 1).padStart(2, '0')}`,
  supportingConcepts: [...new Set([...(lesson.supportingConcepts || []), ...(support[lesson.number] || [])])].filter(id => !lesson.prerequisites.includes(id)),
}))

export const classicalSlides = [...slides28, ...slides29, ...slides30, ...slides31, ...slides32, ...slides33, ...slides34, ...slides35, ...slides36, ...slides37, ...slides38, ...slides39, ...slides40, ...slides41, ...slides42, ...slides43, ...slides44, ...slides45]

export const classicalPart = {
  id: 'bo-tro-co-dien',
  title: 'Bổ trợ xác suất thống kê cổ điển',
  description: 'Xác suất giải tích và thống kê toán, với các chuyên đề riêng về phân phối, giới hạn, ước lượng, kiểm định và mô hình thống kê. Bấm tên mục để xem lộ trình học.',
  link: '/xac-suat-thong-ke/bo-tro-co-dien',
  collapsed: true,
  lessons: classicalLessons.map(lesson => lesson.slug),
}
