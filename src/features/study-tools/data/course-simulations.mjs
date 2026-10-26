// These destinations contain the named interactive component in their Notes.
// Keep the directory lightweight: Its modules do not import simulation code.
export const simulationCatalog = [
  { id: 'lifeguard', course: 'toan-cho-ai', title: 'Chọn lộ trình cứu hộ', description: 'Điều chỉnh điểm xuống nước và so sánh thời gian di chuyển.', path: '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/bai-toan-toi-uu.html', component: 'LifeguardLab' },
  { id: 'affine', course: 'toan-cho-ai', title: 'Đường thẳng và tổ hợp affine', description: 'Thay đổi các điểm và quan sát tổ hợp affine.', path: '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/duong-thang-va-tap-affine.html', component: 'AffineLab' },
  { id: 'convex-set', course: 'toan-cho-ai', title: 'Tập lồi và bao lồi', description: 'Kiểm tra đoạn nối hai điểm và dựng bao lồi.', path: '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/tap-loi-va-bao-loi.html', component: 'ConvexSetLab' },
  { id: 'gradient', course: 'toan-cho-ai', title: 'Gradient và đường mức', description: 'Di chuyển điểm xét để quan sát hướng gradient.', path: '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/dieu-kien-bac-nhat.html', component: 'GradientCutLab' },
  { id: 'linear-program', course: 'toan-cho-ai', title: 'Hướng tối ưu trong quy hoạch tuyến tính', description: 'So sánh đường mức và miền khả thi của bài toán.', path: '/toan-cho-ai/bai-giang/bai-02-tap-loi/quy-hoach-tuyen-tinh.html', component: 'LPDirectionLab' },
  { id: 'logistic', course: 'toan-cho-ai', title: 'Hồi quy logistic', description: 'Điều chỉnh tham số và theo dõi sự thay đổi của mô hình.', path: '/toan-cho-ai/bai-giang/bai-01-nhap-mon-toi-uu/tinh-loi-trong-mo-hinh-hoc-may.html', component: 'LogisticLab' },
  { id: 'blind-search', course: 'bieu-dien-tri-thuc', title: 'Duyệt đồ thị bằng BFS và DFS', description: 'Theo dõi thứ tự mở rộng các nút trong bài toán tìm kiếm.', path: '/bieu-dien-tri-thuc/bai-giang/02-tim-kiem-mu.html', component: 'CodeIllustration' },
  { id: 'mapreduce', course: 'giai-thuat-du-lieu', title: 'Luồng dữ liệu MapReduce', description: 'Theo dõi dữ liệu qua các bước Map, Shuffle và Reduce.', path: '/giai-thuat-du-lieu/bai-giang/bai-02-mapreduce-va-xu-ly-du-lieu-lon.html', component: 'CodeIllustration' },
  { id: 'dsa-search', course: 'dsa', title: 'Duyệt đồ thị', description: 'Quan sát hàng đợi, ngăn xếp và thứ tự duyệt.', path: '/dsa/bai-giang/graphs.html', component: 'CodeIllustration' },
  { id: 'discrete-search', course: 'discrete-math', title: 'Đồ thị và thứ tự duyệt', description: 'Liên hệ biểu diễn đồ thị với các bước tìm kiếm.', path: '/discrete-math/bai-giang/graph-theory.html', component: 'CodeIllustration' }
]

export function courseSimulations(courseId = 'all') {
  return simulationCatalog.filter(item => courseId === 'all' || item.course === courseId)
}
