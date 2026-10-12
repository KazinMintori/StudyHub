const topic = (slug, title, question) => ({ slug, title, question, source: 'Tài liệu ôn tập' })
export const mathAiReviewLesson = {
  number: 8, slug: 'bai-08-tai-lieu-on-tap', title: 'Ôn luyện: Từ nền tảng đến thuật toán', kind: 'review',
  prerequisites: ['ham-so', 'dao-ham', 'tap-hop'],
  supportingConcepts: ['vector', 'ma-tran', 'chuan', 'gradient', 'hessian', 'ma-tran-psd', 'binh-phuong-toi-thieu', 'tap-loi', 'ham-loi', 'lagrangian', 'kkt', 'ham-doi-ngau', 'dieu-kien-slater', 'quy-tac-chuoi', 'tim-kiem-duong'],
  status: 'ready',
  description: 'Mô hình tối ưu, hồi quy, KKT, đối ngẫu, tính lồi, Taylor và thuật toán gradient qua toàn bộ nội dung bốn buổi ôn tập.',
  topicGroups: [
    { title: 'Ôn luyện 1', description: 'Vector, chuẩn, ma trận, dạng toàn phương và đạo hàm trước khi dùng các điều kiện tối ưu.', topics: [
      topic('khong-gian-va-ma-tran', 'Không gian Euclid, chuẩn và ma trận đối xứng', 'Chuẩn, hình cầu và trị riêng giúp mô tả bài toán tối ưu ra sao?'),
      topic('dao-ham-va-cuc-tri', 'Đạo hàm, gradient, Hessian và cực trị', 'Điều kiện nào chỉ tạo ứng viên và điều kiện nào chứng nhận cực tiểu?')
    ] },
    { title: 'Ôn luyện 2', description: 'Tính lồi và chứng nhận toàn cục, sau đó áp dụng vào hồi quy, LP và bài toán có cos.', topics: [
      topic('tinh-loi-va-toi-uu', 'Tập lồi, hàm lồi và nghiệm tối ưu', 'Vì sao một cực tiểu địa phương của bài toán lồi là toàn cục?'),
      topic('mo-hinh-va-hoi-quy', 'Mô hình tối ưu và hồi quy tuyến tính', 'Huấn luyện mô hình trở thành bài toán tối ưu như thế nào?'),
      topic('quy-hoach-tuyen-tinh', 'Quy hoạch tuyến tính và phân loại bài toán', 'Dùng đường mức và các đỉnh để giải hai bài toán tuyến tính ra sao?'),
      topic('bai-tap-cos', 'Giải bài toán ba biến có hàm cos', 'Chứng minh tính lồi và tìm nghiệm duy nhất bằng hai cách nào?')
    ] },
    { title: 'Ôn luyện 3', description: 'Dùng tính lồi đã học để hiểu KKT, giải theo tham số và chứng nhận bằng đối ngẫu.', topics: [
      topic('dieu-kien-kkt', 'Lagrangian và điều kiện KKT', 'Vì sao gradient mục tiêu phải cân bằng với gradient ràng buộc?'),
      topic('kkt-co-tham-so', 'Giải KKT theo tham số và tập ràng buộc chặt', 'Nghiệm thay đổi thế nào khi tổng nguồn lực đi qua ngưỡng?'),
      topic('doi-ngau-lagrange', 'Đối ngẫu Lagrange và điều kiện Slater', 'Một cận dưới có thể chứng minh nghiệm đã tối ưu bằng cách nào?'),
      topic('bai-tap-rang-buoc', 'Bài tập ràng buộc lồi và phi lồi', 'KKT đủ đến đâu khi hàm mục tiêu là đa thức bậc ba?')
    ] },
    { title: 'Ôn luyện 4', description: 'Đạo hàm dọc đường, hướng giảm, độ dài bước và hai vòng backtracking đầy đủ.', topics: [
      topic('quy-tac-chuoi-va-taylor', 'Quy tắc chuỗi và Taylor nhiều biến', 'Chuyển một hàm nhiều biến về một hàm trên đường thẳng để tính đạo hàm thế nào?'),
      topic('gradient-backtracking-newton', 'Gradient, backtracking và hướng Newton', 'Chọn hướng và bước đi để giảm hàm mục tiêu như thế nào?')
    ] }
  ]
}
const dependencies = {
  'khong-gian-va-ma-tran': [],
  'dao-ham-va-cuc-tri': ['khong-gian-va-ma-tran'],
  'tinh-loi-va-toi-uu': ['dao-ham-va-cuc-tri'],
  'mo-hinh-va-hoi-quy': ['khong-gian-va-ma-tran', 'tinh-loi-va-toi-uu'],
  'quy-hoach-tuyen-tinh': ['mo-hinh-va-hoi-quy', 'tinh-loi-va-toi-uu'],
  'bai-tap-cos': ['dao-ham-va-cuc-tri', 'tinh-loi-va-toi-uu'],
  'dieu-kien-kkt': ['tinh-loi-va-toi-uu', 'dao-ham-va-cuc-tri'],
  'kkt-co-tham-so': ['dieu-kien-kkt'],
  'doi-ngau-lagrange': ['dieu-kien-kkt', 'tinh-loi-va-toi-uu'],
  'bai-tap-rang-buoc': ['doi-ngau-lagrange', 'kkt-co-tham-so'],
  'quy-tac-chuoi-va-taylor': ['dao-ham-va-cuc-tri'],
  'gradient-backtracking-newton': ['quy-tac-chuoi-va-taylor', 'tinh-loi-va-toi-uu']
}
for (const group of mathAiReviewLesson.topicGroups) {
  for (const topic of group.topics) topic.requires = dependencies[topic.slug]
}
export const mathAiReviewSlides = []
export const mathAiReviewCheatsheet = {
  summary: 'Công thức và điều kiện áp dụng của bốn buổi ôn tập.',
  sections: [
    { id: 'foundations', title: 'Nền tảng và đạo hàm', badge: 'Ôn luyện 1', items: [
      { name: 'Hessian và trị riêng', bullets: ['Với ma trận đối xứng, PSD tương đương mọi trị riêng không âm.', 'Gradient bằng 0 ở biên không phải điều kiện cần của bài có ràng buộc.'] },
      { name: 'Cực tiểu không ràng buộc', formula: '$$\\nabla f(x)=0$$', bullets: ['Điều kiện cần tại điểm trong nếu f khả vi.', 'Với f thuộc C², Hessian PD tại điểm dừng đủ cho cực tiểu nghiêm địa phương.'] }
    ] },
    { id: 'convexity', title: 'Tính lồi và mô hình', badge: 'Ôn luyện 2', items: [
      { name: 'Sai số bình phương trung bình', formula: '$$L(a)=\\frac1N\\|Xa-y\\|_2^2$$', bullets: ['X có N hàng và d+1 cột nếu có hệ số chặn.', 'Phương trình chuẩn là $X^TXa=X^Ty$.'] },
      { name: 'Tính lồi của hàm trơn', bullets: ['Tính lồi cần Hessian PSD trên toàn miền mở lồi.', 'Gradient bằng 0 đủ cho tối ưu toàn cục của hàm lồi khả vi không ràng buộc.'] },
      { name: 'Bài toán có cos', formula: '$$x^\\star=(0,0,0),\\quad f^\\star=1$$', bullets: ['Đạo hàm bậc hai của cos là −cos.'] }
    ] },
    { id: 'kkt', title: 'KKT và đối ngẫu', badge: 'Ôn luyện 3', items: [
      { name: 'Quy ước dấu', bullets: ['Viết $f_i\\le0$ và $\\mu_i\\ge0$.', 'Nhân tử của đẳng thức được lấy dấu tùy ý.', 'KKT cần dưới LICQ và đủ cho bài toán lồi khả vi.'] },
      { name: 'Khoảng cách đối ngẫu', formula: '$$\\begin{aligned}0&\\le f(x)-p^\\star\\\\&\\le f(x)-g(\\mu,\\lambda)\\end{aligned}$$', bullets: ['x phải khả thi gốc và μ phải không âm.', 'Slater yêu cầu một điểm thỏa nghiêm các bất đẳng thức và thỏa các đẳng thức affine trong miền chung.'] },
      { name: 'Nhánh tham số lớn hơn 2', formula: '$$\\lambda=-\\frac{r+1}{3}$$', bullets: ['Cả ba tọa độ nghiệm đều dương khi r>2.'] }
    ] },
    { id: 'algorithms', title: 'Hướng và độ dài bước', badge: 'Ôn luyện 4', items: [
      { name: 'Hướng gradient', formula: '$$d=-\\nabla f(x)$$', bullets: ['Nếu gradient khác 0 thì tích gradient và hướng âm.', 'Chuẩn gradient nhỏ đo tính dừng, không tự đo khoảng cách đến nghiệm.'] },
      { name: 'Backtracking Armijo', formula: '$$\\begin{aligned}f(x+td)&\\le f(x)\\\\&\\quad+\\alpha t\\nabla f(x)^Td\\end{aligned}$$', bullets: ['Dùng $0<\\alpha<1/2$ và $0<\\beta<1$.', 'Nếu chưa đạt, thay t bởi beta nhân t và thử lại.', 'Wolfe còn cần điều kiện độ cong.'] },
      { name: 'Hướng Newton', formula: '$$\\nabla^2f(x)d=-\\nabla f(x)$$', bullets: ['Hessian PD bảo đảm hướng giảm khi gradient khác 0.', 'Giải hệ tuyến tính thay vì lập nghịch đảo.'] }
    ] }
  ]
}
