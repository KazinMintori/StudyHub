import { physics1Course, physics2Course } from './physics-courses.mjs'
import { dataProcessingCourse } from './data-processing-course.mjs'
import { mathAiCourse } from './math-ai-course.mjs'
import { xacSuatThongKeCourse } from './xac-suat-thong-ke-course.mjs'
const lesson = (slug, title, prerequisites, status = 'ready') => ({ slug, title, prerequisites, status })
const slide = (title, bullets, note, formula = '', example = '') => ({ title, bullets, note, formula, example })

export const courseCatalog = [
  {
    id: 'bieu-dien-tri-thuc', code: '01', name: 'Biểu diễn tri thức & Tìm kiếm', short: 'Tri thức & Tìm kiếm', current: true,
    description: 'Mô hình hóa bài toán, chọn cách tìm kiếm và biểu diễn tri thức để suy luận.',
    foundations: ['tap-hop', 'menh-de', 'luong-tu', 'do-thi', 'cay', 'trang-thai', 'hang-doi', 'ngan-xep', 'hang-doi-uu-tien', 'do-phuc-tap', 'heuristic', 'xac-suat-co-dieu-kien', 'doc-lap'],
    parts: [
      {
        title: 'Phần 1. Tổng quan và tác tử thông minh',
        description: 'Đặc tả tác tử, môi trường và cấu trúc giải quyết bài toán.',
        lessons: ['01-gioi-thieu-tac-tu']
      },
      {
        title: 'Phần 2. Không gian trạng thái và thuật toán tìm kiếm',
        description: 'Chiến lược tìm kiếm mù và tìm kiếm kinh nghiệm Heuristic, A*.',
        lessons: ['02-tim-kiem-mu', '03-tim-kiem-kinh-nghiem']
      },
      {
        title: 'Phần 3. Tìm kiếm đối kháng và bài toán ràng buộc',
        description: 'Thuật toán Minimax, cắt tỉa Alpha-Beta và bài toán thỏa mãn ràng buộc.',
        lessons: ['04-tim-kiem-doi-khang', '05-csp']
      },
      {
        title: 'Phần 4. Biểu diễn tri thức và suy luận',
        description: 'Logic vị từ, luật suy diễn và mô hình mạng Bayes.',
        lessons: ['14-logic-bieu-dien-tri-thuc', '16-mang-bayes']
      }
    ],
    lessons: [
      lesson('01-gioi-thieu-tac-tu', 'Giới thiệu & tác tử thông minh', ['trang-thai', 'menh-de'], 'draft'),
      lesson('02-tim-kiem-mu', 'Tìm kiếm mù: BFS, DFS, UCS & IDS', ['do-thi', 'trang-thai', 'hang-doi', 'ngan-xep', 'hang-doi-uu-tien', 'do-phuc-tap']),
      lesson('03-tim-kiem-kinh-nghiem', 'Tìm kiếm kinh nghiệm: Greedy & A*', ['do-thi', 'hang-doi-uu-tien', 'heuristic', 'do-phuc-tap']),
      lesson('04-tim-kiem-doi-khang', 'Tìm kiếm đối kháng: Minimax & Alpha–Beta', ['cay', 'ngan-xep', 'do-phuc-tap']),
      lesson('05-csp', 'Bài toán thỏa mãn ràng buộc', ['tap-hop', 'menh-de'], 'draft'),
      lesson('14-logic-bieu-dien-tri-thuc', 'Logic & biểu diễn tri thức', ['menh-de', 'luong-tu', 'tap-hop']),
      lesson('16-mang-bayes', 'Mạng Bayes & suy luận', ['xac-suat-co-dieu-kien', 'doc-lap', 'do-thi'], 'draft')
    ],
    slides: [], illustration: 'search'
  },
  mathAiCourse,
  xacSuatThongKeCourse,
  dataProcessingCourse,
  physics1Course,
  physics2Course,
  {
    id: 'giai-thuat-du-lieu', code: '06', name: 'Giải thuật nền tảng của Khoa học dữ liệu', short: 'Giải thuật dữ liệu', current: true,
    description: 'Đặc tả dữ liệu lớn, tính toán phân tán MapReduce, thuật toán PageRank và xử lý đồ thị quy mô lớn.',
    foundations: ['do-phuc-tap', 'ham-lap-trinh', 'dictionary', 'khoa-gia-tri', 'bam', 'phan-tan', 'ket-hop', 'vector', 'ma-tran', 'do-thi', 'xac-suat-co-dieu-kien'],
    parts: [
      {
        title: 'Phần 1. Nền tảng dữ liệu lớn và mô hình thuật toán',
        description: 'Đặc tả bài toán, độ đo khoảng cách, tiêu chuẩn đánh giá và nguyên lý Bonferroni.',
        lessons: ['bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan']
      },
      {
        title: 'Phần 2. Tính toán phân tán MapReduce',
        description: 'Mô hình lập trình Map/Shuffle/Reduce/Combine, nhân ma trận lớn và mô hình chi phí cụm máy.',
        lessons: ['bai-02-mapreduce-va-xu-ly-du-lieu-lon']
      },
      {
        title: 'Phần 3. Phân tích đồ thị và thuật toán PageRank',
        description: 'Mô hình Random Surfer, Power Iteration, xử lý Dead Ends, Spider Traps và Damping Factor.',
        lessons: ['bai-03-pagerank-mo-hinh-va-tinh-toan']
      }
    ],
    lessons: [
      lesson('bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan', 'Dữ liệu lớn & mô hình thuật toán', ['do-phuc-tap', 'phan-tan', 'bam']),
      lesson('bai-02-mapreduce-va-xu-ly-du-lieu-lon', 'MapReduce & xử lý dữ liệu lớn', ['khoa-gia-tri', 'phan-tan', 'ket-hop', 'ma-tran']),
      lesson('bai-03-pagerank-mo-hinh-va-tinh-toan', 'PageRank: Mô hình & tính toán', ['do-thi', 'ma-tran'])
    ],
    slides: [], illustration: 'mapreduce'
  },
  {
    id: 'dsa', code: '07', name: 'Cấu trúc dữ liệu & Giải thuật', short: 'CTDL & Giải thuật', current: true,
    description: 'Chọn cấu trúc lưu dữ liệu và đánh giá chi phí của từng cách xử lý.',
    foundations: ['mang', 'con-tro', 'de-quy', 'hang-doi', 'ngan-xep', 'cay', 'do-thi', 'do-phuc-tap', 'quy-nap'],
    parts: [
      {
        title: 'Phần 1. Độ phức tạp và đánh giá thuật toán',
        description: 'Đánh giá thời gian và không gian qua ký hiệu Big-O và phương pháp quy nạp.',
        lessons: ['complexity']
      },
      {
        title: 'Phần 2. Thuật toán sắp xếp và tìm kiếm',
        description: 'Các thuật toán sắp xếp kinh điển và tìm kiếm nhị phân trên dãy có thứ tự.',
        lessons: ['sorting', 'searching']
      },
      {
        title: 'Phần 3. Cấu trúc dữ liệu cây và đồ thị',
        description: 'Cây nhị phân, cây tìm kiếm, đồ thị và các thuật toán duyệt BFS, DFS.',
        lessons: ['trees', 'graphs']
      }
    ],
    lessons: [
      lesson('complexity', 'Phân tích độ phức tạp', ['do-phuc-tap', 'quy-nap']),
      lesson('sorting', 'Thuật toán sắp xếp', ['mang', 'de-quy', 'do-phuc-tap']),
      lesson('searching', 'Thuật toán tìm kiếm', ['mang', 'do-phuc-tap']),
      lesson('trees', 'Cây & cây nhị phân', ['cay', 'con-tro', 'de-quy']),
      lesson('graphs', 'Đồ thị & thuật toán duyệt', ['do-thi', 'hang-doi', 'ngan-xep'])
    ],
    slides: [], illustration: 'search'
  },
  {
    id: 'discrete-math', code: '08', name: 'Toán rời rạc', short: 'Toán rời rạc', current: true,
    description: 'Đọc logic, quan hệ và cấu trúc hữu hạn bằng các định nghĩa chính xác.',
    foundations: ['tap-hop', 'ham-so', 'menh-de', 'luong-tu', 'quy-nap', 'to-hop', 'quan-he', 'do-thi', 'cay'],
    parts: [
      {
        title: 'Phần 1. Logic mệnh đề và vị từ',
        description: 'Logic mệnh đề, bảng chân trị, logic vị từ và các lượng từ toán học.',
        lessons: ['logic']
      },
      {
        title: 'Phần 2. Tập hợp, quan hệ và ánh xạ',
        description: 'Định nghĩa tập hợp, tích Descartes, quan hệ tương đương, thứ tự và hàm số.',
        lessons: ['relations']
      },
      {
        title: 'Phần 3. Cơ sở lý thuyết đồ thị',
        description: 'Đỉnh, cạnh, đường đi, chu trình, đồ thị Euler, Hamilton và cây liên thông.',
        lessons: ['graph-theory']
      }
    ],
    lessons: [
      lesson('logic', 'Logic mệnh đề & vị từ', ['menh-de', 'luong-tu']),
      lesson('relations', 'Quan hệ & ánh xạ', ['tap-hop', 'quan-he', 'ham-so']),
      lesson('graph-theory', 'Lý thuyết đồ thị cơ bản', ['do-thi', 'cay'])
    ],
    slides: [], illustration: 'search'
  }
]

export const findCourse = id => courseCatalog.find(course => course.id === id)
