import { courseCatalog } from '../course-catalog.mjs'
export const courses = courseCatalog.filter(course => course.current).map(course => ({
  ...course,
  tags: 'Slides · Notes · Nền tảng theo từng bài',
  first: course.lessons.find(lesson => lesson.status === 'ready')?.slug || '',
  count: course.lessons.filter(lesson => lesson.status === 'ready').length
}))

export const cards = [
  { course: 'bieu-dien-tri-thuc', q: 'BFS và DFS khác nhau ở cấu trúc lưu các nút chờ thế nào?', a: 'BFS dùng hàng đợi FIFO, duyệt theo từng tầng. DFS dùng ngăn xếp LIFO hoặc đệ quy, đi sâu một nhánh trước.', lesson: '02-tim-kiem-mu' },
  { course: 'bieu-dien-tri-thuc', q: 'Hàm đánh giá của A* là gì?', a: 'f(n) = g(n) + h(n). g(n) là chi phí đã đi từ trạng thái đầu; h(n) ước lượng chi phí còn lại tới đích.', lesson: '03-tim-kiem-kinh-nghiem' },
  { course: 'bieu-dien-tri-thuc', q: 'Khi nào Alpha–Beta có thể cắt nhánh?', a: 'Khi α ≥ β. Nhánh đó không thể làm thay đổi lựa chọn của nút tổ tiên theo Minimax.', lesson: '04-tim-kiem-doi-khang' },
  { course: 'toan-cho-ai', q: 'Một tập được gọi là lồi khi nào?', a: 'Với mọi x, y trong tập và λ thuộc [0, 1], điểm λx + (1 − λ)y vẫn thuộc tập. Đoạn thẳng nối hai điểm bất kỳ nằm hoàn toàn trong tập.', lesson: 'bai-02-tap-loi' },
  { course: 'toan-cho-ai', q: 'Gradient Descent cập nhật tham số theo hướng nào?', a: 'Theo hướng ngược gradient: θ mới = θ cũ − η∇f(θ). η > 0 là tốc độ học; bước quá lớn có thể làm thuật toán không hội tụ.', lesson: 'bai-01-nhap-mon-toi-uu' },
  { course: 'toan-cho-ai', q: 'Cực tiểu địa phương của hàm lồi có tính chất gì?', a: 'Mọi cực tiểu địa phương của hàm lồi trên miền lồi đều là cực tiểu toàn cục.', lesson: 'bai-02-tap-loi' },
  { course: 'xac-suat-thong-ke', q: 'Công thức Bayes là gì?', a: 'P(A|B) = P(B|A)P(A) / P(B), với P(B) > 0. Nó cập nhật xác suất của A khi đã quan sát B.', lesson: '' },
  { course: 'xac-suat-thong-ke', q: 'Độc lập có nghĩa là hai biến cố loại trừ nhau không?', a: 'Không. Độc lập nghĩa là P(A∩B) = P(A)P(B). Loại trừ nhau nghĩa là A∩B rỗng; hai biến cố có xác suất dương và loại trừ nhau không độc lập.', lesson: '' },
  { course: 'xac-suat-thong-ke', q: 'Kỳ vọng và phương sai mô tả điều gì?', a: 'Kỳ vọng mô tả giá trị trung bình theo xác suất. Phương sai E[(X − E[X])²] mô tả độ phân tán quanh kỳ vọng.', lesson: '' },
  { course: 'xu-ly-du-lieu', q: 'Vector hóa trong NumPy có lợi ích gì?', a: 'Thao tác trên cả mảng bằng các phép toán được tối ưu, tránh nhiều vòng lặp Python. Ví dụ a * 2 nhân từng phần tử của mảng a với 2.', lesson: 'bai-03-numpy' },
  { course: 'xu-ly-du-lieu', q: 'Series và DataFrame khác nhau thế nào?', a: 'Series là cấu trúc một chiều có nhãn. DataFrame là bảng hai chiều, gồm các cột có thể có kiểu dữ liệu khác nhau.', lesson: 'bai-05-series-dataframe-chuyen-sau' },
  { course: 'xu-ly-du-lieu', q: 'loc và iloc chọn dữ liệu theo cách nào?', a: 'loc chọn theo nhãn, iloc chọn theo vị trí số nguyên. Với lát cắt, loc thường gồm cả nhãn cuối còn iloc loại trừ vị trí cuối.', lesson: 'bai-04-lam-quen-pandas' },
  { course: 'vat-ly-2', q: 'Dấu trừ trong E = −∇V mang ý nghĩa gì?', a: 'Điện trường hướng theo chiều điện thế giảm nhanh nhất. Gradient ∇V chỉ theo chiều điện thế tăng nhanh nhất.', lesson: '' },
  { course: 'vat-ly-2', q: 'V(x) = 2x² − 3x. Điện trường Ex tại x = 2 m là bao nhiêu?', a: 'Ex = −dV/dx = −(4x − 3). Tại x = 2 m, Ex = −5 V/m, hướng theo chiều âm của trục x.', lesson: '' },
  { course: 'vat-ly-2', q: 'Điện trường trong lòng vật dẫn ở trạng thái cân bằng tĩnh điện bằng bao nhiêu?', a: 'Bằng 0. Điện thế trong vật dẫn là hằng số và điện tích dư nằm trên bề mặt.', lesson: '' },
  { course: 'giai-thuat-du-lieu', q: 'Pha Shuffle trong mô hình MapReduce đảm nhận vai trò gì?', a: 'Gom nhóm tất cả các giá trị có cùng khóa từ các máy Worker Map và chuyển tới cùng một hàm Reduce xử lý.', lesson: 'bai-02-mapreduce-va-xu-ly-du-lieu-lon' },
  { course: 'giai-thuat-du-lieu', q: 'Hiện tượng Dead Ends trong thuật toán PageRank là gì và giải quyết thế nào?', a: 'Dead Ends là các trang không có liên kết ra ngoài, làm rò rỉ điểm PageRank về 0 trong quá trình lặp. Giải quyết bằng cách loại bỏ tạm thời hoặc phân phối lại xác suất nhảy ngẫu nhiên.', lesson: 'bai-03-pagerank-mo-hinh-va-tinh-toan' },
  { course: 'giai-thuat-du-lieu', q: 'Hệ số suy giảm (Damping Factor) beta trong PageRank giải quyết vấn đề gì?', a: 'Xử lý triệt để Spider Traps (bẫy nhện hút hết điểm) và Dead Ends bằng cách cho phép người lướt ngẫu nhiên dịch chuyển tức thời (teleport) với xác suất 1 - beta.', lesson: 'bai-03-pagerank-mo-hinh-va-tinh-toan' }
]
