const lesson = (number, slug, title, prerequisites, supportingConcepts = []) => ({ number, slug, title, prerequisites, supportingConcepts, status: 'ready' })
const slide = (note, title, bullets, formula = '', example = '') => ({ note, title, bullets, formula, example })
// Một chương dài được chia thành các trang chủ đề, mỗi trang trả lời một câu hỏi.
// question: câu hỏi mà trang đó giải quyết, hiện trên bản đồ chương. source: mục tương ứng trong Convex Optimization.
const topic = (slug, title, question, source = '') => ({ slug, title, question, source })
const group = (title, description, topics) => ({ title, description, topics })
const topicGroups = {
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
    group('III. Hàm lồi', 'Nối hình học của tập lồi với giải tích: dây cung, tiếp tuyến, độ cong và các quy tắc lắp ghép hàm.', [
      topic('ham-loi', 'Hàm lồi và bất đẳng thức dây cung', 'Đồ thị nằm dưới mọi dây cung thì nói lên điều gì về một hàm số?', '§3.1.1–3.1.2'),
      topic('dieu-kien-bac-nhat', 'Điều kiện bậc nhất: tiếp tuyến nằm dưới đồ thị', 'Chỉ biết giá trị và đạo hàm tại một điểm, ta suy ra được gì về toàn bộ hàm?', '§3.1.3'),
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
  ['tham-so-toan-hoc','ham-so','tap-hop','to-hop-loi','tap-loi','ham-loi','chuan','ma-tran','he-phuong-trinh','mien-kha-thi','infimum','epigraph','binh-phuong-toi-thieu','likelihood'],
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
  description: 'Tám bài giảng đi từ kiến thức nền tới tối ưu lồi và huấn luyện mô hình, kèm phép tính mẫu, mô phỏng và bài tập có lời giải.',
  foundations: [...new Set([...prerequisites.flat(), ...supportingConcepts.flat()])],
  structureSource: 'https://courses.iaidev.com/math-4-AI/2627-1/',
  parts: [{ title: 'Bài giảng 00–07', lessons: slugs }],
  lessons: titles.map((title, i) => ({ ...lesson(i, slugs[i], title, prerequisites[i], supportingConcepts[i]), description: descriptions[i], topicGroups: topicGroups[slugs[i]] || [] })),
  slides: [
    slide(slugs[0], 'Ma trận biến nhiều dự đoán thành một phép nhân', ["Với A kích thước $m\\times n$ và w có n phần tử, Aw có m phần tử.", "Một hàng của A tương ứng một quan sát, còn một cột tương ứng một đặc trưng.", "Phần dư $r=Aw-b$ đo sai lệch của từng dự đoán."], "$$A\\in\\mathbb R^{m\\times n},\\qquad w\\in\\mathbb R^{n\\times1},\\qquad r\\in\\mathbb R^{m\\times1}$$", "Với các dữ liệu:\n\n$$A=\\begin{bmatrix}1\\\\2\\\\3\\end{bmatrix},\\qquad b=\\begin{bmatrix}1\\\\2\\\\2\\end{bmatrix}.$$\n\nNghiệm là $w=\\frac{11}{14}$, cho dự đoán:\n\n$$Aw=\\begin{bmatrix}\\frac{11}{14}\\\\\\frac{11}{7}\\\\\\frac{33}{14}\\end{bmatrix}.$$"),
    slide(slugs[0], 'Gradient mô tả bậc nhất, Hessian mô tả độ cong', ['Gradient của f là vector các đạo hàm riêng tại điểm khả vi.', 'Hessian của f là ma trận đạo hàm bậc hai.', "Ma trận đối xứng PSD thỏa $v^{T}Hv\\ge 0$ với mọi v. Dấu của từng phần tử không đủ để kết luận PSD."], "$$f(w)=\\frac12\\|Aw-b\\|_2^2,\\qquad \\nabla f(w)=A^T(Aw-b),\\qquad H=A^TA$$"),
    slide(slugs[0], 'Mô hình nhiễu Gauss cho tiêu chuẩn tổng bình phương phần dư', ["Giả sử các nhiễu độc lập và có cùng phương sai $\\sigma ^{2}>0$.", 'Lấy âm log biến tích các mật độ thành tổng bình phương phần dư cộng một hằng số.', "Khi $\\sigma ^{2}$ cố định, cực đại likelihood theo w tương đương cực tiểu tổng bình phương phần dư."], "$$-\\log p(b\\mid w)=\\text{hằng số}+\\frac{\\|Aw-b\\|_2^2}{2\\sigma^2}$$"),
    slide(slugs[1], 'Miền khả thi phải được xác định trước khi tìm nghiệm', ['Biến quyết định khác với dữ liệu cố định của bài toán.', 'Nghiệm phải khả thi và cho giá trị không lớn hơn mọi điểm khả thi khác.', 'Cận dưới hữu hạn không bảo đảm tồn tại một điểm đạt cận đó.'], "$$p^\\star=\\inf_{x\\in C}f(x)$$", "min x với $x>0$ có p*=0 nhưng không có nghiệm tối ưu."),
    slide(slugs[1], 'Tập lồi chứa đoạn nối, hàm lồi nằm dưới dây cung', ['Tập lồi phải chứa đoạn nối của mọi cặp điểm trong tập.', 'Hàm lồi cần có miền lồi và thỏa bất đẳng thức dây cung.', "Đồ thị của hàm lồi thường không phải tập lồi, trong khi epigraph của hàm lồi là tập lồi."], "$$f(\\theta x+(1-\\theta )y) \\le  \\theta f(x)+(1-\\theta )f(y)$$"),
    slide(slugs[1], 'Một mặt phẳng tiếp tuyến có thể chứng nhận nghiệm', ['Với f khả vi, lồi trên miền mở lồi, xấp xỉ bậc nhất là cận dưới toàn cục.', 'Không ràng buộc: gradient bằng 0 đủ để tối ưu.', 'Có ràng buộc: phải so hướng gradient với các điểm khả thi.'], "$$f(y) \\ge  f(x)+\\nabla f(x)^{T}(y-x)$$", "$\\min (x-2)^{2}$ với $x\\le 1$ đạt tại 1. Đạo hàm tại đó bằng −2."),
    slide(slugs[1], 'Tính lồi không tự tạo tính duy nhất', ['Tối ưu cục bộ của bài toán lồi là tối ưu toàn cục.', 'Lồi nghiêm trên miền khả thi lồi bảo đảm nhiều nhất một nghiệm.', 'Vẫn cần xét khả thi, bị chặn dưới và đạt nghiệm.']),
    slide(slugs[1], 'Mô hình điều khiển tuyến tính tạo mục tiêu toàn phương', ["Trạng thái hiện tại và đích là dữ liệu, còn hành động là biến cần chọn.", 'Bình phương sai lệch cộng điều chuẩn có Hessian PSD.', 'Giới hạn affine của hành động giữ miền khả thi lồi.'], "$$f(u)=\\frac12\\|Fs+Bu-r\\|_2^2+\\frac\\rho2\\|u\\|_2^2,\\qquad\\rho\\ge0$$"),
    slide(slugs[1], 'Hàm mất mát logistic lồi theo vector tham số', ["Điểm số $a^{T}w$ là hàm affine của tham số dù xác suất sigmoid là phi tuyến.", "Hessian của từng hàm mất mát là $p(1-p)aa^T$ và là ma trận PSD.", 'Với dữ liệu tách được, hàm mất mát có thể tiến tới cận nhưng không đạt tại một tham số hữu hạn.'], "$$\\ell(w)=\\log(1+\\exp(a^Tw))-b\\,a^Tw,\\qquad b\\in\\{0,1\\}$$"),
    slide(slugs[2], 'Dấu bất đẳng thức là một phần của chứng nhận tính lồi', ["Dạng chuẩn dùng $f_{i}(x)\\le 0$ với các fᵢ lồi.", 'Các đẳng thức phải affine.', 'Một biểu thức chưa đúng dạng chuẩn có thể có cải dạng tương đương lồi.'], "$$\\min_x f_0(x)\\quad\\text{với}\\quad f_i(x)\\le0,\\quad Ax=b$$"),
    slide(slugs[2], 'LP, QP và các nón là cách mô tả cấu trúc', ['LP dùng mục tiêu và ràng buộc affine.', 'QP dùng mục tiêu toàn phương PSD và ràng buộc affine.', "SOCP dùng chuẩn Euclid, còn SDP dùng bất đẳng thức ma trận PSD."], "$$\\min_x\\left(\\frac12x^TPx+q^Tx\\right),\\qquad P\\succeq0$$"),
    slide(slugs[2], 'Biến phụ có thể loại bỏ max và trị tuyệt đối', ["min maxᵢ fᵢ(x) tương đương min t với $f_{i}(x)\\le t$.", "Ràng buộc |$u|\\le t$ tương đương $u\\le t$ và −$u\\le t$.", 'Phải chỉ ra cách thu hồi x và giá trị tối ưu sau cải dạng.'], "$$\\min_x\\|Ax-b\\|_\\infty\\quad\\Longleftrightarrow\\quad\\min_{x,t}t\\quad\\text{với}\\quad-t\\mathbf1\\le Ax-b\\le t\\mathbf1$$"),
    slide(slugs[2], "Nới lỏng cho một cận, còn xấp xỉ thay bài toán bằng một mô hình gần đúng", ['Nới lỏng mở rộng miền khả thi và tạo cận dưới cho bài min.', 'Nghiệm nới lỏng có thể không khả thi cho bài gốc.', 'Xấp xỉ mục tiêu không tự cho cận nếu chưa chứng minh quan hệ giữa hai hàm.']),
    slide(slugs[3], 'Nhân tử không âm giữ Lagrangian ở dưới hàm mục tiêu', ["Tại điểm khả thi, $\\lambda _{i}f_{i}(x)\\le 0$ khi $\\lambda _{i}\\ge 0$.", 'Infimum của Lagrangian không lớn hơn giá trị tại điểm khả thi.', "Do đó $g(\\lambda ,\\nu )$ là một cận dưới ngay cả khi bài toán gốc không lồi."], "$$g(\\lambda,\\nu)=\\inf_x L(x,\\lambda,\\nu)\\le p^\\star$$"),
    slide(slugs[3], 'Hàm đối ngẫu được tính bằng cách tối ưu theo x trước', ['Giữ các nhân tử cố định, rồi lấy infimum theo x trong miền xác định.', 'Sau đó cực đại g theo các nhân tử khả thi.', 'Hàm g lõm vì là infimum của một họ hàm affine theo các nhân tử.'], "$$\\min_{x\\le1}(x-2)^2:\\quad g(\\lambda)=\\lambda-\\frac{\\lambda^2}{4},\\quad\\lambda\\ge0$$", "$\\lambda^\\star=2$, $x^\\star=1$; $g(2)=f(1)=1$."),
    slide(slugs[3], 'Slater đủ cho đối ngẫu mạnh trong bài toán lồi', ['Slater tìm một điểm thuộc nội tương đối của miền chung, thỏa đẳng thức và thỏa chặt các bất đẳng thức.', 'Đối ngẫu mạnh là d*=p*.', "KKT đủ trong bài toán lồi khả vi. Với Slater và nghiệm đạt, KKT cũng cần."]),
    slide(slugs[3], 'KKT và khoảng cách đối ngẫu chứng nhận nghiệm', ['Xác minh khả thi gốc, dấu của nhân tử, bù trừ và điều kiện dừng.', 'Một nhân tử bằng 0 không cho biết ràng buộc có chặt hay không.', "Nếu x và các nhân tử đều khả thi, $f(x)-g$ là cận trên cho độ thiếu tối ưu."], "$0 \\le  f(x)-p$* ≤ $f(x)-g(\\lambda ,\\nu )$"),
    slide(slugs[4], 'Hướng giảm và độ dài bước là hai quyết định', ["Hướng d giảm cục bộ khi $\\nabla f^{T}d<0$.", 'Backtracking thu nhỏ t cho đến khi ở trong miền và giảm đủ.', 'Hướng đúng vẫn có thể làm f tăng nếu chọn bước quá lớn.'], "f(x+td) ≤ $f(x)+\\alpha t\\nabla f^{T}d$, $0<\\alpha <\\frac12$, $0<\\beta <1$"),
    slide(slugs[4], 'Newton tối ưu mô hình toàn phương tại điểm hiện tại', ["Tính g và H rồi giải $Hd=-g$, thay vì lập H⁻¹.", 'H dương xác định bảo đảm hướng Newton là hướng giảm khi g khác 0.', 'Bài toàn phương dương xác định đến nghiệm sau một bước Newton đầy đủ.'], "$$g+Hd=0$$"),
    slide(slugs[4], 'Hệ Newton–KKT giữ ràng buộc đẳng thức', ["Nếu $Ax=b$, hướng phải thỏa $Ad=0$.", "Từ điểm chưa khả thi, vế phải khối dưới là $b-Ax$.", "Tìm bước từ hệ tuyến tính. Với khởi đầu chưa khả thi, tìm kiếm theo chuẩn phần dư KKT."], "$$\\begin{bmatrix}H&A^T\\\\A&0\\end{bmatrix}\\begin{bmatrix}d\\\\\\Delta\\nu\\end{bmatrix}=-\\begin{bmatrix}\\nabla f+A^T\\nu\\\\Ax-b\\end{bmatrix}$$"),
    slide(slugs[4], 'Self-concordance giới hạn mức thay đổi của độ cong', ["Trong một chiều: $|f'''|\\le2(f'')^{3/2}$ trên miền.", 'Trong nhiều chiều: xét cùng điều kiện trên mọi đường thẳng nằm trong miền.', "Đây là giả thiết dùng để phân tích Newton, nhưng không phải mọi hàm lồi đều thỏa điều kiện này."], "$$f(x)=-\\log x,\\quad x>0:\\quad |f'''(x)|=2[f''(x)]^{\\frac{3}{2}}=\\frac2{x^3}$$"),
    slide(slugs[5], 'Lô nhỏ cung cấp một ước lượng của gradient toàn bộ dữ liệu', ['Hàm mục tiêu huấn luyện là trung bình hàm mất mát trên tập huấn luyện.', 'Lấy mẫu đều cho gradient lô nhỏ không chệch khi tham số đang được giữ cố định.', "Một bước SGD có thể làm hàm mục tiêu trên toàn bộ dữ liệu tăng. Ngoài ra, việc giảm hàm mục tiêu trên tập huấn luyện không bảo đảm cải thiện trên tập xác thực."], "$$g^B=\\frac1{|B|}\\sum_{i\\in B}\\nabla\\ell_i(\\theta)$$", "Nếu lô $B=\\{2,5\\}$ thì $|B|=2$ và $g^B=\\frac{\\nabla\\ell_2(\\theta)+\\nabla\\ell_5(\\theta)}2$. Chỉ cộng gradient của các mẫu có chỉ số nằm trong $B$."),
    slide(slugs[5], 'Momentum giữ thông tin từ các bước trước', ['Vận tốc v tích lũy hướng cập nhật.', "Nesterov tính gradient tại điểm nhìn trước $\\theta +\\mu v$.", "Phải thống nhất quy ước dấu và khởi tạo $v=0$."], "$v^{+}=\\mu v-\\eta g$; $\\theta ^{+}=\\theta +v^{+}$"),
    slide(slugs[5], 'Khởi tạo cần phá đối xứng và duy trì thang phương sai', ['Các neuron cùng cấu trúc với trọng số giống nhau có thể nhận gradient giống nhau.', 'Glorot cân bằng thang truyền tín hiệu dưới giả định của mô hình tuyến tính hóa.', 'Fan-in và fan-out lần lượt đếm số đầu vào và đầu ra của tầng.'], "$$\\operatorname{Var}(W)=\\frac2{n_{\\mathrm{in}}+n_{\\mathrm{out}}}$$", "fan-in=4, fan-out=2: phân phối đều trên $[-1,1]$ có phương sai $\\frac{1}{3}$."),
    slide(slugs[6], 'AdaGrad và RMSProp thay thang cập nhật từng tọa độ', ['AdaGrad cộng dồn bình phương gradient từ đầu.', 'RMSProp dùng trung bình mũ để giảm ảnh hưởng các bước xa.', 'Các phép bình phương, căn và chia được thực hiện theo từng phần tử.'], "$$s^+=s+g^2,\\qquad\\theta^+=\\theta-\\frac{\\eta g}{\\sqrt{s^+}+\\varepsilon}$$"),
    slide(slugs[6], 'Adam dùng hai trạng thái và hiệu chỉnh khởi đầu', ['m theo dõi trung bình mũ của gradient.', 'v theo dõi trung bình mũ của bình phương gradient.', 'Chia cho 1−βᵗ để hiệu chỉnh trạng thái khởi tạo bằng 0.'], "$$\\theta^+=\\theta-\\frac{\\eta\\hat m}{\\sqrt{\\hat v}+\\varepsilon}$$", "$g_{1}=2$, $\\beta _{1}=0.9$, $\\beta _{2}=0.999$: $\\hat{m}_{1}=2$ và $\\hat{v}_{1}=4$."),
    slide(slugs[6], 'Độ cong còn có thể được dùng bằng hệ tuyến tính', ['Newton cần Hessian hoặc cách giải hệ tương ứng.', 'Gradient liên hợp giải hệ SPD bằng các hướng liên hợp.', "BFGS cập nhật xấp xỉ Hessian nghịch đảo, trong đó điều kiện $y^{T}s>0$ giúp giữ tính dương xác định."]),
    slide(slugs[6], 'So sánh thuật toán cần giữ nguyên điều kiện thử nghiệm', ['Giữ nguyên dữ liệu, điểm khởi tạo, ngân sách và hạt giống ngẫu nhiên khi đối chiếu.', 'Báo riêng hàm mất mát trên tập huấn luyện, trên tập xác thực và thời gian chạy.', "Mô phỏng toàn phương hai chiều chỉ minh họa phép cập nhật, vì vậy không thể dùng nó để xếp hạng các thuật toán cho mạng sâu."]),
    slide(slugs[7], 'LP đưa hàm tuyến tính lên đa diện', ["Dạng chuẩn là $\\min c^{T}x$ với $Ax=b$, $x\\ge 0$.", 'Nghiệm cơ sở lấy các cột độc lập rồi đặt biến còn lại bằng 0.', 'Có đỉnh và giá trị tối ưu hữu hạn thì có một đỉnh tối ưu.'], "$$x_B=A_B^{-1}b\\ge0$$", "$\\max 3x+2y$, $x+y\\le 4$, $x\\le 2$, x,$y\\ge 0$: tối ưu (2,2), giá trị 10."),
    slide(slugs[7], 'Bellman ghép chi phí hiện tại với phần còn lại', ['Trạng thái phải chứa thông tin đủ để xác định các lựa chọn về sau.', 'Với thời hạn hữu hạn tất định, tính từ trạng thái cuối rồi đi ngược.', 'Lưu cả giá trị tối ưu và hành động đạt giá trị đó.'], "$$V_t(s)=\\min_a\\{c_t(s,a)+V_{t+1}(T_t(s,a))\\}$$"),
    slide(slugs[7], 'LP và quy hoạch động có thể mô tả cùng một bài đường đi', ['DP dùng đệ quy theo cấu trúc thời gian hoặc DAG.', 'LP có thể dùng biến luồng hoặc các bất đẳng thức tiềm năng.', "Nếu có chu trình, cần cách xử lý khác vì đệ quy ngược trên DAG không áp dụng trực tiếp."], "$$V(T)=0,\\qquad V(S)=\\min_u\\{c(S,u)+V(u)\\}$$", "$S\\to A$:1, $S\\to B$:4, $A\\to T$:5, $A\\to B$:2, $B\\to T$:1: đường $S\\to A\\to B\\to T$ có chi phí 4.")
  ], illustration: 'gradient'
}
