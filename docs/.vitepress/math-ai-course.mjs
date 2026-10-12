import { mathAiReviewLesson, mathAiReviewSlides } from './math-ai-review-course.mjs'

const lesson = (number, slug, title, prerequisites, supportingConcepts = []) => ({ number, slug, title, prerequisites, supportingConcepts, status: 'ready' })
const slide = (note, title, bullets, formula = '', example = '') => ({ note, title, bullets, formula, example })
// Một chương dài được chia thành các trang chủ đề, mỗi trang trả lời một câu hỏi.
// question: câu hỏi mà trang đó giải quyết, hiện trên bản đồ chương. source: mục tương ứng trong Convex Optimization.
const topic = (slug, title, question, source = '') => ({ slug, title, question, source })
const group = (title, description, topics) => ({ title, description, topics })
const topicGroups = {
  'bai-00-on-tap-nen-tang': [
    group('I. Hệ phương trình và giải tích ma trận', 'Giải hệ thiếu xác định, bổ đề Woodbury và vi phân hàm ma trận trong học máy.', [
      topic('he-thieu-xac-dinh-va-giai-tich-ma-tran', 'Hệ Tuyến Tính Thiếu Xác Định và Giải Tích Ma Trận', 'Trong vô số nghiệm của hệ thiếu xác định, nghiệm nào có chuẩn nhỏ nhất và tính thưa cao nhất?', '§C.5, §A.5')
    ])
  ],
  'bai-01-nhap-mon-toi-uu': [
    group('I. Bài toán tối ưu', 'Viết đúng một bài toán trước khi nghĩ tới chuyện giải nó.', [
      topic('bai-toan-toi-uu', 'Bài toán tối ưu và những gì cần viết ra', 'Muốn nói một phương án là tốt nhất, ta phải mô tả chính xác những đối tượng nào?', '§1.1, §4.1.1'),
      topic('hai-lop-bai-toan-kinh-dien', 'Bình phương tối thiểu và quy hoạch tuyến tính', 'Hai lớp bài toán quen thuộc này có điểm chung gì mà người ta giải được chúng một cách đáng tin cậy?', '§1.2–1.3')
    ]),
    group('II. Hình học của tập lồi', 'Các khối hình cơ bản, cách lắp ghép chúng và những định lý hình học dùng lại suốt môn học.', [
      topic('duong-thang-va-tap-affine', 'Đường thẳng, đoạn thẳng và tập affine', 'Điều kiện “các hệ số cộng lại bằng 1” mô tả loại hình học nào?', '§2.1.1–2.1.2'),
      topic('noi-tuong-doi', 'Chiều affine và nội tương đối', 'Một hình vuông nằm phẳng trong không gian ba chiều có “phần trong” hay không?', '§2.1.3'),
      topic('tap-loi-va-bao-loi', 'Tập lồi, tổ hợp lồi và bao lồi', 'Khi buộc mọi hệ số phải không âm, đường thẳng qua hai điểm còn lại phần nào?', '§2.1.4'),
      topic('non-loi', 'Nón và nón lồi', 'Bỏ điều kiện tổng bằng 1 nhưng vẫn giữ hệ số không âm thì ta thu được hình gì?', '§2.1.5'),
      topic('sieu-phang-va-nua-khong-gian', 'Siêu phẳng và nửa không gian', 'Một phương trình tuyến tính duy nhất chia không gian ra sao?', '§2.2.1'),
      topic('qua-cau-va-ellipsoid', 'Quả cầu và ellipsoid', 'Một ma trận đối xứng xác định dương vẽ ra hình gì trong không gian?', '§2.2.2'),
      topic('chuan-va-non-chuan', 'Quả cầu chuẩn và nón chuẩn', 'Vì sao quả cầu đơn vị của mọi chuẩn đều lồi, còn “quả cầu” của ‖x‖ với p = 1/2 thì không?', '§2.2.3'),
      topic('da-dien-va-don-hinh', 'Đa diện và đơn hình', 'Nên mô tả một đa giác bằng các cạnh hay bằng các đỉnh của nó?', '§2.2.4'),
      topic('non-psd', 'Nón các ma trận nửa xác định dương', 'Tập hợp các ma trận cũng có một hình dạng mà ta có thể hình dung được không?', '§2.2.5'),
      topic('phep-toan-giu-tinh-loi', 'Các phép toán giữ tính lồi của tập', 'Làm thế nào chứng minh một tập phức tạp là lồi mà không phải kiểm tra từng đoạn thẳng?', '§2.3.1–2.3.2'),
      topic('phoi-canh-va-phan-tuyen-tinh', 'Phép phối cảnh và hàm phân tuyến tính', 'Nhìn một vật lồi qua máy ảnh lỗ kim, ảnh thu được có còn lồi?', '§2.3.3'),
      topic('bat-dang-thuc-tong-quat', 'Nón chính quy và bất đẳng thức tổng quát', 'Khi so sánh hai vector, “nhỏ hơn” nên được hiểu theo nghĩa nào?', '§2.4'),
      topic('sieu-phang-phan-tach-va-tua', 'Siêu phẳng phân tách và siêu phẳng tựa', 'Hai tập lồi rời nhau có luôn ngăn được bằng một siêu phẳng không?', '§2.5'),
      topic('non-doi-ngau', 'Nón đối ngẫu và lựa chọn Pareto', 'Những hướng nào nhìn toàn bộ một nón từ cùng một phía, và điều đó giúp gì khi phải cân nhiều tiêu chí?', '§2.6')
    ]),
    group('III. Hàm lồi', 'Nối hình học của tập lồi với giải tích: Dây cung, tiếp tuyến, độ cong và các quy tắc lắp ghép hàm.', [
      topic('ham-loi', 'Hàm lồi và bất đẳng thức dây cung', 'Đồ thị nằm dưới mọi dây cung thì nói lên điều gì về một hàm số?', '§3.1.1–3.1.2'),
      topic('dieu-kien-bac-nhat', 'Điều kiện bậc nhất: Tiếp tuyến nằm dưới đồ thị', 'Chỉ biết giá trị và đạo hàm tại một điểm, ta suy ra được gì về toàn bộ hàm?', '§3.1.3'),
      topic('dieu-kien-bac-hai', 'Điều kiện bậc hai và độ cong', 'Hessian nửa xác định dương mang ý nghĩa hình học gì?', '§3.1.4'),
      topic('cac-ham-loi-quen-thuoc', 'Những hàm lồi thường gặp', 'Chuẩn, hàm max, log-sum-exp và log det lồi hay lõm, và ta chứng minh điều đó thế nào?', '§3.1.5'),
      topic('epigraph-tap-muc-duoi-jensen', 'Epigraph, tập mức dưới và bất đẳng thức Jensen', 'Nhìn một hàm lồi như một tập hợp thì ta được thêm những công cụ gì?', '§3.1.6–3.1.9'),
      topic('phep-toan-giu-tinh-loi-cua-ham', 'Các phép toán giữ tính lồi của hàm', 'Từ vài hàm lồi đã biết, ta lắp ghép được những hàm lồi mới nào và cần cẩn thận ở đâu?', '§3.2')
    ]),
    group('IV. Tính lồi trong bài toán tối ưu', 'Ghép miền lồi với hàm mục tiêu lồi để có những bảo đảm mà tối ưu tổng quát không có.', [
      topic('cuc-bo-va-toan-cuc', 'Cực tiểu cục bộ và cực tiểu toàn cục', 'Trong bài toán lồi, một điểm tốt nhất trong vùng lân cận có chắc là tốt nhất trên toàn miền?', '§4.2.1–4.2.2'),
      topic('dieu-kien-toi-uu', 'Điều kiện tối ưu bậc nhất trên miền lồi', 'Khi nghiệm nằm trên biên và gradient khác 0, ta kiểm chứng nó tối ưu bằng cách nào?', '§4.2.3'),
      topic('tinh-loi-trong-mo-hinh-hoc-may', 'Nhận diện tính lồi trong mô hình học máy', 'Hàm mất mát của hồi quy logistic là lồi, vậy còn mạng nơ-ron hai tầng thì sao?', '§4.4, §7.1')
    ])
  ],
  'bai-02-tap-loi': [
    group('I. Biến đổi bài toán', 'Viết lại một bài toán mà không làm sai lời giải, và nhận ra lúc tính lồi bị cách viết che khuất.', [
      topic('bai-toan-tuong-duong', 'Bài toán tương đương và các phép biến đổi cơ bản', 'Khi nào hai bài toán viết khác nhau lại cho cùng một lời giải, và phép biến đổi nào làm mất điều đó?', '§4.1.3, §4.2.1'),
      topic('khu-rang-buoc-va-toi-uu-tung-phan', 'Khử ràng buộc đẳng thức và tối ưu theo từng nhóm biến', 'Một ràng buộc đẳng thức tuyến tính có thể biến mất mà không mất thông tin nào không, và cái giá phải trả là gì?', '§4.1.3, §4.2.4'),
      topic('toi-uu-tua-loi', 'Hàm tựa lồi và phương pháp chia đôi', 'Nếu chỉ biết mọi tập mức dưới đều lồi, ta còn giải bài toán một cách đáng tin cậy được không?', '§3.4, §4.2.5')
    ]),
    group('II. Quy hoạch tuyến tính', 'Lớp bài toán đơn giản nhất nhưng mô tả được rất nhiều mô hình, từ hình học tới xác suất.', [
      topic('quy-hoach-tuyen-tinh', 'Quy hoạch tuyến tính: Các dạng viết và hình học của nghiệm', 'Vì sao mọi LP đều đưa được về cùng một dạng chuẩn, và nghiệm của nó nằm ở đâu trên đa diện?', '§4.3'),
      topic('mo-hinh-lp', 'Những bài toán trở thành LP', 'Tìm hình tròn lớn nhất nằm trong một đa giác nghe chẳng tuyến tính chút nào. Vì sao đó lại là một LP?', '§4.3.1'),
      topic('quy-hoach-phan-tuyen-tinh', 'Quy hoạch phân tuyến tính', 'Cực tiểu một tỉ số của hai hàm affine có khó hơn LP không?', '§4.3.2')
    ]),
    group('III. Quy hoạch toàn phương và nón bậc hai', 'Khi mục tiêu hay ràng buộc cong lên, nghiệm rời khỏi các đỉnh và chuẩn Euclid xuất hiện.', [
      topic('quy-hoach-toan-phuong', 'Quy hoạch toàn phương và QCQP', 'Khi mục tiêu cong như một cái bát, nghiệm còn nằm ở đỉnh của đa diện nữa không?', '§4.4–4.4.1'),
      topic('quy-hoach-non-bac-hai', 'Quy hoạch nón bậc hai và LP bền vững', 'Muốn một ràng buộc tuyến tính đúng với mọi tham số trong một vùng bất định, ta phải trả giá bằng hình dạng nào?', '§4.4.2')
    ]),
    group('IV. Quy hoạch hình học', 'Những bài toán không lồi trong biến gốc nhưng trở thành lồi sau khi chuyển sang thang logarit.', [
      topic('quy-hoach-hinh-hoc', 'Quy hoạch hình học', 'Một bài toán không lồi có thể trở thành lồi chỉ nhờ đổi sang thang logarit không?', '§4.5')
    ]),
    group('V. Bất đẳng thức suy rộng và SDP', 'Thay thứ tự từng thành phần bằng thứ tự của các ma trận nửa xác định dương.', [
      topic('bai-toan-dang-non-va-sdp', 'Bài toán dạng nón và quy hoạch nửa xác định', 'Thay "mọi thành phần không âm" bằng "ma trận nửa xác định dương", ta được lớp bài toán nào?', '§4.6.1–4.6.2'),
      topic('phan-bu-schur-va-bai-toan-tri-rieng', 'Phần bù Schur và các bài toán về trị riêng', 'Làm thế nào viết một ràng buộc phi tuyến như "chuẩn phổ không vượt quá t" thành một bất đẳng thức ma trận tuyến tính?', '§4.6.3, §A.5.5')
    ]),
    group('VI. Tối ưu vector', 'Khi phải cân nhiều mục tiêu cùng lúc, câu trả lời là cả một đường đánh đổi chứ không phải một điểm.', [
      topic('toi-uu-vector-va-danh-doi', 'Tối ưu vector, điểm Pareto và đường đánh đổi', 'Khi sai số nhỏ và tham số nhỏ là hai mục tiêu cùng lúc, thế nào là một lựa chọn tốt?', '§4.7, §6.3')
    ]),
    group('VII. Xấp xỉ, khớp hàm và ước lượng thống kê', 'Tìm hàm xấp xỉ tối ưu, thiết kế bộ phát hiện và chặn xác suất rủi ro bằng tối ưu lồi.', [
      topic('khop-ham-va-noi-suy', 'Khớp hàm, làm mượt spline và nội suy lồi', 'Làm thế nào tìm một hàm lồi khớp mượt mà với dữ liệu quan sát mà không làm mất tính lồi?', '§6.5'),
      topic('uoc-luong-phi-tham-so-va-kiem-dinh', 'Ước lượng phi tham số và thiết kế bộ phát hiện', 'Khi không biết dạng phân phối xác suất, làm sao thiết kế bộ phát hiện tối ưu qua LP?', '§7.2–7.3'),
      topic('can-chebyshev-va-chernoff', 'Cận xác suất Chebyshev, Chernoff và tối ưu hóa ma trận', 'Làm thế nào chặn trên xác suất đuôi và ngoại lai qua bài toán SDP và biến đổi Legendre?', '§7.4')
    ]),
    group('VIII. Quy hoạch mặt bằng', 'Bài toán bố trí không gian hình học và tối ưu hóa diện tích qua quy hoạch hình học.', [
      topic('quy-hoach-mat-bang', 'Quy hoạch mặt bằng và phân bổ không gian tối ưu', 'Làm thế nào tối ưu kích thước linh kiện và dây nối mà vẫn bảo toàn tỷ lệ khung hình?', '§8.8')
    ]),
    group('IX. Thiết kế thí nghiệm và Hình học cực trị', 'Thiết kế thí nghiệm tối ưu Fisher, ellipsoid thể tích cực trị Loewner–John và bài toán định vị mạng lưới.', [
      topic('thiet-ke-thi-nghiem-toi-uu', 'Thiết kế thí nghiệm tối ưu và Ma trận thông tin Fisher', 'Làm thế nào phân bổ ngân sách đo lường để ma trận thông tin Fisher đạt chất lượng cao nhất qua SDP?', '§7.5'),
      topic('ellipsoid-cuc-tri-va-tam-hinh-hoc', 'Ellipsoid thể tích cực trị và Các điểm tâm hình học', 'Làm sao tìm ellipsoid bao ngoài nhỏ nhất hoặc quả cầu nội tiếp lớn nhất của một đa diện qua LP và log-det?', '§8.4–8.5'),
      topic('bai-toan-dinh-vi-va-mang-luoi', 'Bài toán định vị, đặt vị trí và tối ưu hóa mạng lưới', 'Làm thế nào bố trí tọa độ các nút mạng để cực tiểu hóa tổng chi phí dây nối qua SOCP và giải hệ Laplacian?', '§8.7')
    ])
  ],
  'bai-04-gradient-newton': [
    group('I. Phương pháp điểm trong nâng cao', 'Khởi tạo khả thi qua Pha I, độ phức tạp trên nón chính quy và thuật toán Primal-Dual.', [
      topic('phuong-phap-pha-1-va-khoi-tao', 'Phương pháp Pha I và tìm điểm khả thi khởi đầu', 'Khi không có sẵn điểm xuất phát khả thi nghiêm ngặt, làm sao bắt đầu phương pháp điểm trong?', '§11.4'),
      topic('do-phuc-tap-va-bat-dang-thuc-tong-quat', 'Độ phức tạp và điểm trong trên nón chính quy', 'Phương pháp điểm trong cần chính xác bao nhiêu bước lặp Newton và mở rộng cho nón Lorentz/PSD thế nào?', '§11.5–11.6'),
      topic('phuong-phap-primal-dual', 'Phương pháp Điểm trong Primal-Dual', 'Vì sao cập nhật đồng thời biến nguyên thủy và đối ngẫu lại vượt trội hơn phương pháp hàm chắn truyền thống?', '§11.7–11.8')
    ])
  ]
}

const slugs = ['bai-00-on-tap-nen-tang', 'bai-01-nhap-mon-toi-uu', 'bai-02-tap-loi', 'bai-03-doi-ngau-lagrange', 'bai-04-gradient-newton', 'bai-05-toi-uu-huan-luyen', 'bai-06-phuong-phap-thich-nghi', 'bai-07-quy-hoach-tuyen-tinh-va-dong']
const titles = ['Ôn tập nền tảng toán học cho AI', 'Giới thiệu tối ưu, tập lồi và hàm lồi', 'Các bài toán tối ưu lồi', 'Đối ngẫu Lagrange', 'Tối ưu không ràng buộc và ràng buộc đẳng thức', 'Các phương pháp tối ưu trong huấn luyện mô hình học sâu', 'Các phương pháp tối ưu trong học sâu', 'Quy hoạch tuyến tính và quy hoạch động']
const prerequisites = [
  ['ham-so', 'dao-ham', 'tap-hop'],
  ['vector', 'tich-vo-huong', 'gradient', 'hessian', 'ma-tran-psd'],
  ['tap-loi', 'ham-loi', 'chuan', 'ma-tran-psd'],
  ['ham-loi', 'gradient', 'he-phuong-trinh'],
  ['gradient', 'hessian', 'ma-tran-psd', 'he-phuong-trinh', 'kkt'],
  ['gradient', 'quy-tac-chuoi', 'ky-vong', 'phuong-sai'],
  ['gradient', 'hessian', 'ky-vong', 'phuong-sai'],
  ['ma-tran', 'he-phuong-trinh', 'tap-loi', 'do-thi']
]
const supportingConcepts = [
  ['tham-so-toan-hoc','vector','ma-tran','tich-vo-huong','chuan','dao-ham-rieng','quy-tac-chuoi','hessian','ma-tran-psd','bien-ngau-nhien','ky-vong','phuong-sai','phan-phoi-gauss','ma-tran-hiep-phuong-sai','likelihood','binh-phuong-toi-thieu'],
  ['tham-so-toan-hoc','ham-so','tap-hop','to-hop-loi','tap-loi','ham-loi','chuan','ma-tran','he-phuong-trinh','mien-kha-thi','infimum','epigraph','binh-phuong-toi-thieu','likelihood','dinh-luat-snell'],
  ['tham-so-toan-hoc','mien-kha-thi','epigraph','he-phuong-trinh','ma-tran','noi-long-toi-uu','infimum','lagrangian'],
  ['tham-so-toan-hoc','mien-kha-thi','infimum','lagrangian','ham-doi-ngau','doi-ngau-manh','dieu-kien-slater','kkt','ma-tran'],
  ['tham-so-toan-hoc','chuan','dao-ham','tim-kiem-duong','tu-tuong-hop','mien-kha-thi'],
  ['tham-so-toan-hoc','bien-ngau-nhien','doc-lap','gradient-ngau-nhien','momentum-nesterov','phan-phoi-gauss','ma-tran-hiep-phuong-sai'],
  ['tham-so-toan-hoc','he-phuong-trinh','tim-kiem-duong','gradient-ngau-nhien','momentum-nesterov','adagrad','rmsprop','adam','gradient-lien-hop','bfgs'],
  ['tham-so-toan-hoc','tich-vo-huong','mien-kha-thi','infimum','lagrangian','nghiem-co-so','quy-hoach-dong','trang-thai']
]
const descriptions = [
  "Xác định kích thước ma trận, tính gradient và Hessian. Suy ra bình phương tối thiểu từ mô hình nhiễu Gauss.",
  "Lập bài toán, dùng đoạn thẳng để xét tập lồi và dây cung để xét hàm lồi. Giải thích điều kiện tối ưu toàn cục.",
  "Nhận diện LP, QP, SOCP, SDP và GP. Phân biệt cải dạng tương đương, xấp xỉ và nới lỏng.",
  'Dựng cận dưới từ Lagrangian, tính hàm đối ngẫu và dùng Slater, KKT để chứng nhận nghiệm.',
  "Theo dõi từng bước của phương pháp gradient, backtracking và Newton. Giải hệ Newton–KKT khi có ràng buộc đẳng thức.",
  'Từ gradient toàn bộ dữ liệu đến lô nhỏ, momentum, Nesterov và khởi tạo trọng số.',
  "Tính từng trạng thái AdaGrad, RMSProp và Adam. Đối chiếu với phương pháp dùng độ cong.",
  'Tìm nghiệm cơ sở của LP và tính Bellman ngược thời gian trên bài toán hữu hạn tất định.'
]
export const mathAiCourse = {
  id: 'toan-cho-ai', code: '02', name: 'Cơ sở toán cho AI', short: 'Toán cho AI', current: true,
  description: 'Tám bài giảng từ kiến thức nền tới tối ưu lồi và huấn luyện mô hình, cùng tài liệu bốn buổi ôn tập có lời giải.',
  foundations: [...new Set([...prerequisites.flat(), ...supportingConcepts.flat(), ...mathAiReviewLesson.prerequisites, ...mathAiReviewLesson.supportingConcepts])],
  structureSource: 'https://courses.iaidev.com/math-4-AI/2627-1/',
  reviewSlug: mathAiReviewLesson.slug,
  parts: [{ title: 'Bài giảng 00–07', lessons: slugs }, { title: 'Ôn luyện', lessons: [mathAiReviewLesson.slug] }],
  lessons: [...titles.map((title, i) => ({ ...lesson(i, slugs[i], title, prerequisites[i], supportingConcepts[i]), description: descriptions[i], topicGroups: topicGroups[slugs[i]] || [] })), mathAiReviewLesson],
  slides: [], illustration: 'gradient'
}
