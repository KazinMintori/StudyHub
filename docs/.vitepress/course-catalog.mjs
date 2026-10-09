import { physics1Course, physics2Course } from './physics-courses.mjs'
import { dataProcessingCourse } from './data-processing-course.mjs'
import { mathAiCourse } from './math-ai-course.mjs'
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
    slides: [
      slide('Từ bài toán đến không gian trạng thái', ['Xác định trạng thái đầu, hành động hợp lệ và điều kiện đích.', "Đồ thị mô tả quan hệ chuyển trạng thái, còn cây tìm kiếm mô tả các đường đã mở rộng.", 'Phân biệt số bước với tổng chi phí trước khi chọn thuật toán.'], '02-tim-kiem-mu', '', 'Một đường 3 cạnh có thể đắt hơn đường 4 cạnh nếu trọng số khác nhau.'),
      slide('BFS, DFS, UCS & IDS', ['BFS dùng hàng đợi FIFO, tìm đường ít cạnh nhất khi mọi bước có cùng chi phí.', "DFS dùng ngăn xếp nên tiết kiệm bộ nhớ theo chiều sâu, nhưng không bảo đảm tối ưu.", 'UCS ưu tiên chi phí đã đi g(n). Với chi phí bước có chặn dưới dương, nó đầy đủ và tối ưu.', 'IDS lặp DFS với giới hạn độ sâu tăng dần.'], '02-tim-kiem-mu'),
      slide('Greedy và A* nhìn về phía đích', ['Greedy chọn h(n) nhỏ nhất, có thể nhanh nhưng không bảo đảm lời giải tối ưu.', 'A* kết hợp chi phí đã đi với ước lượng còn lại.', "Heuristic admissible không ước lượng quá cao, còn tính consistent giúp xử lý đồ thị thuận lợi hơn."], '03-tim-kiem-kinh-nghiem', "A*: $f(n) = g(n) + h(n)$"),
      slide('Minimax & cắt tỉa Alpha–Beta', ['MAX chọn giá trị lớn nhất, MIN chọn giá trị nhỏ nhất ở tầng của mình.', "Ta truyền giá trị từ lá về gốc. Khi giới hạn độ sâu, kết quả còn phụ thuộc hàm đánh giá.", 'Alpha–Beta bỏ nhánh không thể thay đổi quyết định Minimax.'], '04-tim-kiem-doi-khang', "Cắt nhánh khi $\\alpha  \\ge  \\beta$"),
      slide('Biểu diễn tri thức bằng logic', ["Logic mệnh đề xét các phát biểu đúng hoặc sai, còn logic vị từ mô tả thêm đối tượng và quan hệ.", "Khi phân biệt lượng từ “mọi” với “tồn tại”, cần xác định rõ miền đang xét.", 'Suy luận cần luật hợp lệ, không chỉ dựa trên một vài ví dụ đúng.'], '14-logic-bieu-dien-tri-thuc', "$$\\neg \\forall x P(x) \\iff  \\exists x \\neg P(x)$$")
    ], illustration: 'search'
  },
  mathAiCourse,
  {
    id: 'xac-suat-thong-ke', code: '03', name: 'Xác suất thống kê', short: 'Xác suất thống kê', current: true,
    description: 'Phân biệt các phát biểu từ dữ liệu, rồi học xác suất có điều kiện, phân phối, kỳ vọng và biến thiên.',
    foundations: ['tap-hop', 'khong-gian-mau', 'to-hop', 'xac-suat-co-dieu-kien', 'doc-lap', 'bien-ngau-nhien', 'ky-vong', 'phuong-sai', 'tich-phan', 'mau-tong-the'],
    parts: [
      {
        title: 'Mở đầu. Câu hỏi và dữ liệu',
        description: 'Phân biệt mô tả dữ liệu, suy rộng thống kê, kết luận nhân quả và dự đoán.',
        lessons: ['00-hieu-the-gioi-bang-du-lieu']
      },
      {
        title: 'Phần 1. Cơ sở xác suất và định lý Bayes',
        description: 'Không gian mẫu, xác suất có điều kiện, tính độc lập và cập nhật niềm tin Bayes.',
        lessons: ['01-xac-suat-va-bayes']
      },
      {
        title: 'Phần 2. Biến ngẫu nhiên và quy luật phân phối',
        description: 'Biến ngẫu nhiên rời rạc, liên tục, hàm mật độ PDF và hàm phân phối tích lũy CDF.',
        lessons: ['02-bien-ngau-nhien']
      },
      {
        title: 'Phần 3. Các đặc trưng số và thống kê mẫu',
        description: 'Kỳ vọng, phương sai, hiệp phương sai và ước lượng tham số từ mẫu dữ liệu.',
        lessons: ['03-ky-vong-phuong-sai']
      }
    ],
    lessons: [
      { ...lesson('00-hieu-the-gioi-bang-du-lieu', 'Hiểu thế giới bằng dữ liệu', []), supportingConcepts: ['thong-ke-mo-ta', 'suy-rong-thong-ke', 'mau-tong-the', 'ket-luan-nhan-qua', 'du-doan-thong-ke'] },
      lesson('01-xac-suat-va-bayes', 'Xác suất có điều kiện & Bayes', ['tap-hop', 'khong-gian-mau', 'xac-suat-co-dieu-kien', 'doc-lap']),
      lesson('02-bien-ngau-nhien', 'Biến ngẫu nhiên & phân phối', ['bien-ngau-nhien', 'to-hop', 'tich-phan']),
      lesson('03-ky-vong-phuong-sai', 'Kỳ vọng, phương sai & mẫu dữ liệu', ['ky-vong', 'phuong-sai', 'mau-tong-the'])
    ],
    slides: [
      slide('Dữ liệu có thể hỗ trợ bốn loại phát biểu', ['Mô tả nói về dữ liệu đã có.', 'Suy rộng nói về một tập đối tượng lớn hơn tập đã quan sát.', 'Kết luận nhân quả nói về tác động khi thay đổi một biến.', 'Dự đoán nói về giá trị chưa biết dựa trên các biến đã biết.'], '00-hieu-the-gioi-bang-du-lieu'),
      slide('Mô tả giữ kết luận trong phạm vi quan sát', ['Bản mô tả có thể dùng con số, đồ thị hoặc lời văn.', 'Phải nêu rõ nhóm đối tượng mà dữ liệu mô tả.', 'Tỷ lệ tính từ nhóm trả lời khảo sát mô tả chính nhóm ấy.'], '00-hieu-the-gioi-bang-du-lieu', '', 'Dựa trên khảo sát một lớp học, 70% người trả lời cho biết chưa có kinh nghiệm viết mã máy tính.'),
      slide('Suy rộng cần căn cứ cho việc mở rộng phạm vi', ['Suy rộng dùng dữ liệu quan sát để phát biểu về một tập đối tượng lớn hơn.', 'Đổi “người trả lời khảo sát” thành “sinh viên toàn trường” làm thay đổi phạm vi kết luận.', 'Cần xem cách chọn mẫu và ai đã trả lời trước khi đánh giá kết luận.'], '00-hieu-the-gioi-bang-du-lieu', '', 'Dùng khảo sát một lớp học để phát biểu rằng 70% sinh viên toàn trường chưa có kinh nghiệm viết mã máy tính là suy rộng.'),
      slide('Kết luận nhân quả đặt câu hỏi về can thiệp', ['Một biến mô tả một đặc điểm có thể nhận các giá trị khác nhau.', 'Kết luận nhân quả khẳng định rằng thay đổi một biến ảnh hưởng đến biến khác.', 'Chỉ quan sát hai biến cùng thay đổi chưa đủ để kết luận nhân quả.'], '00-hieu-the-gioi-bang-du-lieu', '', '“Dữ liệu từ thí nghiệm ngẫu nhiên có đối chứng cho thấy dùng một loại kháng sinh mới loại bỏ hơn 99% các ca nhiễm khuẩn” là phát biểu nhân quả.'),
      slide('Dự đoán một giá trị chưa biết', ['Dự đoán dùng các biến đã biết để đoán giá trị của biến chưa biết.', 'Giá trị chưa biết có thể ở tương lai hoặc đã tồn tại nhưng chưa được quan sát.', 'Phân loại một phát biểu chưa chứng minh rằng dự đoán ấy chính xác.'], '00-hieu-the-gioi-bang-du-lieu', '', '“Dựa trên tin tức và giá cổ phiếu Uber hôm nay, tôi dự đoán giá ngày mai tăng 1,2%” là dự đoán.'),
      slide('Đối tượng và câu hỏi quyết định loại phát biểu', ['Xác định dữ liệu thực sự được ghi nhận trên những đối tượng nào.', 'So sánh tập đối tượng trong kết luận với tập đã quan sát.', 'Xác định phát biểu nói về tác động của can thiệp hay về một giá trị chưa biết.'], '00-hieu-the-gioi-bang-du-lieu', '', 'Trong một khảo sát, 7 trong 10 người trả lời chiếm 70%. Phạm vi kết luận quyết định đây là mô tả mẫu hay suy rộng về toàn trường.'),
      slide('Xác suất có điều kiện thay đổi miền xét', ['P(A|B) thu hẹp việc xét kết quả về biến cố B.', 'Hai biến cố độc lập không làm thay đổi xác suất của nhau.', 'Độc lập khác với loại trừ nhau.'], '01-xac-suat-va-bayes', "$$P(A\\mid B)=\\frac{P(A\\cap B)}{P(B)},\\qquad P(B)>0$$"),
      slide('Bayes cập nhật từ quan sát', ['Prior là xác suất trước quan sát.', 'Likelihood là mức phù hợp của quan sát khi giả thuyết đúng.', "Để tính posterior, tức xác suất sau quan sát, cần xét khả năng xuất hiện quan sát dưới các giả thuyết khác nhau."], '01-xac-suat-va-bayes', "$$P(A\\mid B)=\\frac{P(B\\mid A)P(A)}{P(B)}$$"),
      slide('Phân phối mô tả một biến ngẫu nhiên', ['PMF cho xác suất tại từng giá trị của biến rời rạc.', "PDF biểu diễn mật độ, còn xác suất trên một khoảng được tính bằng tích phân mật độ.", "$CDF F(x)=P(X\\le x)$ dùng được cho cả rời rạc và liên tục."], '02-bien-ngau-nhien'),
      slide('Trung tâm, độ phân tán và mẫu', ['Kỳ vọng là trung bình theo xác suất, có thể không là giá trị quan sát được.', "Phương sai đo mức phân tán bằng bình phương độ lệch, còn độ lệch chuẩn có cùng đơn vị với dữ liệu.", 'Thống kê mẫu ước lượng tham số tổng thể và phụ thuộc cách lấy mẫu.'], '03-ky-vong-phuong-sai', "$$\\operatorname{Var}(X) = \\mathbb E[X^{2}] - \\mathbb E[X]^{2}$$")
    ], illustration: 'bayes'
  },
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
      lesson('bai-03-pagerank-mo-hinh-va-tinh-toan', 'PageRank: mô hình & tính toán', ['do-thi', 'ma-tran'])
    ],
    slides: [
      slide('Dữ liệu lớn đổi nút thắt của thuật toán', ["Dữ liệu lớn hơn bộ nhớ RAM: tệp nhật ký $D > M$, không thể nạp trọn.", 'Dữ liệu phân tán trên nhiều máy: gom về một máy gây nghẽn mạng.', "Số cặp bùng nổ bậc hai: N tài liệu tạo $N(N-1)/2$ cặp cần so sánh."], 'bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan', "$$D>M,\\qquad\\binom N2=\\frac{N(N-1)}2$$", "$N = 10^{6}$ tài liệu tạo gần 500 tỷ cặp so sánh."),
      slide('Độ đo Jaccard và thuật toán xét mọi cặp', ['Biểu diễn tài liệu bằng tập hợp các đoạn ký tự (shingles).', "Jaccard đo tỷ lệ giao trên hợp: $J(S, T) = |S \\cap  T| / |S \\cup  T|$.", "Duyệt mọi cặp $1 \\le  i < j \\le  N$ bằng 2 con trỏ trong O(L), chi phí $O(N^{2}L)$."], 'bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan', "$$J(S,T)=\\frac{|S\\cap T|}{|S\\cup T|}\\in[0,1]$$", "Ví dụ MMDS 3.1: giao 3, hợp $8 \\to  J = \\frac{3}{8}$. Đạt ngưỡng khi $τ \\le  \\frac{3}{8}$."),
      slide('Đánh giá lời giải đa khía cạnh', ['Tính đúng: đáp ứng đặc tả trên mọi đầu vào hợp lệ, chứng minh bằng bất biến.', "Tài nguyên: đếm phép tính, bộ nhớ làm việc lớn nhất, $I/O$ đọc/ghi đĩa, dữ liệu mạng.", 'Vận hành: độ trễ truy vấn từng lượt, thông lượng QPS, chi phí xây dựng và cập nhật.'], 'bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan', "$$\\operatorname{recall}@k(q)=\\frac{|\\widehat N_k(q)\\cap N_k(q)|}{k}$$", "Ví dụ recall@5: chuẩn {a,b,c,d,e}, trả về {c,d,e,f,g} → recall = $\\frac{3}{5} = 60$%."),
      slide('Giảm ứng viên và nguy cơ bỏ sót', ["Tạo tập ứng viên A trước khi tính Jaccard chính xác: $\\widehat R=A\\cap R\\subseteq R$.", 'Hậu kiểm chỉ loại ứng viên sai (false positive), không cứu được cặp bị bỏ sót (false negative).', "Để giữ tính đúng $\\hat{R} = R$, bắt buộc bảo đảm R ⊆ A (không bỏ sót cặp đạt ngưỡng)."], 'bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan', "$\\widehat R=A\\cap R\\subseteq R$", 'LSH khuếch đại xác suất để chọn đúng cặp tương đồng cao vào tập ứng viên A.'),
      slide('Nguyên lý Bonferroni và giới hạn suy luận', ["Số phép thử bùng nổ tổ hợp: $C(P, 2) \\cdot  C(T, 2)$ biến cố cặp người–cặp ngày.", "Mô hình độc lập, ngẫu nhiên: xác suất 1 phép thử $p^{2} = 10^{-18}$.", "Kỳ vọng trùng ngẫu nhiên $\\mathbb E[X] \\approx  249.750$ biến cố: trùng ngẫu nhiên lấn át dấu hiệu thật."], 'bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan', "$$\\mathbb E[X] = C(P, 2) \\cdot  C(T, 2) \\cdot  p^{2}$$", "Trùng khách sạn chưa đủ chứng minh phối hợp. Jaccard cao chưa đủ chứng minh đạo văn."),
      slide('Map → nhóm theo khóa → Reduce', ['Map phát các cặp khóa–giá trị.', 'Shuffle đưa các giá trị cùng khóa tới cùng nhóm.', 'Reduce xử lý từng nhóm để thu kết quả cuối.'], 'bai-02-mapreduce-va-xu-ly-du-lieu-lon', '', 'Đếm từ: Map phát (từ,1), Reduce cộng các số 1 theo từ.'),
      slide('Combine cần đúng tính chất phép gom', ['Gom cục bộ giúp giảm truyền dữ liệu.', 'Phép gom cần giữ được thông tin cho kết quả cuối và đáp ứng tính chất cần thiết.', "Khi các nhóm có kích thước khác nhau, trung bình của các trung bình có thể sai, vì vậy cần truyền cặp (tổng, số lượng)."], 'bai-02-mapreduce-va-xu-ly-du-lieu-lon'),
      slide('Thời gian pha do máy chậm nhất quyết định', ['Một phân vùng quá lớn làm những máy còn lại chờ.', 'Thêm máy có thể tăng chi phí đồng bộ và truyền.', 'Kiểm tra cân bằng tải, lượng truyền và khả năng phục hồi khi máy lỗi.'], 'bai-02-mapreduce-va-xu-ly-du-lieu-lon'),
      slide('Từ đếm liên kết sang chia điểm đồng bộ', ['Đếm liên kết vào coi mọi liên kết ngang giá trị và không lan truyền tầm quan trọng.', 'Chia điểm: trang nguồn chia đều điểm cho các đích theo bậc ra d_j.', 'Cập nhật đồng bộ: dùng điểm cũ r^t tính cho mọi trang trong cùng một vòng.'], 'bai-03-pagerank-mo-hinh-va-tinh-toan', "$$r^{t+1} = M_0 r^t$$", "M_0 có cột là nguồn, hàng là đích. Tổng mỗi cột bằng 1."),
      slide('Nút cụt, bẫy liên kết và bước nhảy ngẫu nhiên', ['Nút cụt (dead end) làm rò rỉ điểm: tổng điểm giảm dần về 0.', 'Bẫy liên kết (spider trap) hút và dồn toàn bộ điểm về một nhóm trang.', "Random Surfer với xác suất $\\beta$ đi theo liên kết, $1-\\beta$ nhảy ngẫu nhiên. Bù đều điểm nút cụt $\\delta$."], 'bai-03-pagerank-mo-hinh-va-tinh-toan', "$$r^{t+1} = \\beta  M_0 r^t + [(1-\\beta ) + \\beta \\delta ^t] u$$", 'Hội tụ duy nhất theo định lý điểm bất động Banach trên chuẩn L1.'),
      slide('Biểu diễn thưa và chia khối ma trận', ["Web thực m ≪ $n^{2}$: ma trận đặc lãng phí $O(n^{2})$ bộ nhớ.", 'Biểu diễn theo nguồn: chỉ lưu mã nguồn, bậc ra toàn cục d_j và danh sách đích.', "Chia ma trận thành $k^{2}$ khối theo k dải nguồn và k dải đích để vừa bộ nhớ tác vụ."], 'bai-03-pagerank-mo-hinh-va-tinh-toan', "$$B_{\\mathrm{task}}\\approx\\frac{16n}{k}+B_{\\mathrm{buf}}$$", "$k^{2}$ là số tác vụ Map, không nhất thiết là số máy tính."),
      slide('Quy trình MapReduce và vai trò của Combine', ["Map nhận khối B_ab và dải r_b, phát $(i, r_b[j]/d_j)$ theo trang đích.", 'Combine gom tại chỗ các đóng góp vào cùng đích trong một tác vụ Map.', 'Reduce cộng dồn z_i và tính điểm đầy đủ kèm phần bù bước nhảy.'], 'bai-03-pagerank-mo-hinh-va-tinh-toan', "$$z_i=\\sum_{s=1}^{k_i}L_{is},\\qquad r_i^{t+1}=\\beta z_i+\\frac{(1-\\beta)+\\beta\\delta}{n}$$", "Combine giảm dữ liệu Shuffle H từ m bản ghi xuống số cặp (khối, đích) phân biệt. Với danh sách đóng góp $L_i=(L_{i1},\\ldots,L_{ik_i})$, tổng là $z_i=L_{i1}+\\cdots+L_{ik_i}$. $s$ chạy qua $k_i$ giá trị nhận tại trang $i$."),
      slide('Mô hình chi phí và nút thắt thời gian', ['Bộ nhớ mỗi tác vụ giảm khi tăng k nhưng tăng số lần đọc vector đầu vào.', 'Dữ liệu mạng Q phụ thuộc lượng bản ghi sau Combine truyền liên máy.', "Thời gian pha Map bị khống chế bởi tác vụ nặng nhất: $T_{\\mathrm{map}}\\ge\\max\\left(\\frac Wp,w_{\\max}\\right)$."], 'bai-03-pagerank-mo-hinh-va-tinh-toan', "$$T_{\\mathrm{map}}\\ge\\max\\left(\\frac Wp,w_{\\max}\\right)$$", 'Thêm máy không thể giảm thời gian vượt qua giới hạn của tác vụ nặng nhất.')
    ], illustration: 'mapreduce'
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
    slides: [
      slide('Đánh giá chi phí trước khi tối ưu code', ['Xác định kích thước đầu vào n.', 'Đếm thao tác chủ đạo và bộ nhớ phụ.', 'Nêu trường hợp đang xét và đừng coi Big-O là số giây thực tế.'], 'complexity'),
      slide('Sắp xếp: chọn theo bối cảnh', ['Insertion Sort phù hợp dữ liệu nhỏ hoặc gần có thứ tự.', 'Merge Sort có O(n log n) nhưng cần bộ nhớ phụ tùy cách cài đặt.', "Quick Sort trung bình nhanh. Lựa chọn pivot ảnh hưởng trường hợp xấu."], 'sorting'),
      slide('Tìm kiếm nhị phân cần thứ tự', ['Duy trì miền còn có thể chứa đáp án.', 'Mỗi bước bỏ khoảng một nửa miền tìm kiếm.', "Kiểm tra biên và điều kiện dừng. Dữ liệu chưa sắp xếp cần cách khác."], 'searching', 'Số bước: O(log n)'),
      slide('Cây nhị phân và quan hệ phân cấp', ['Cây có cấu trúc cha–con, không có chu trình trong mô hình đồ thị.', 'Cây tìm kiếm nhị phân duy trì thứ tự: cây con trái nhỏ hơn gốc, cây con phải lớn hơn gốc.', 'Duyệt tiền thứ tự, trung thứ tự và hậu thứ tự bằng đệ quy hoặc ngăn xếp.'], 'trees'),
      slide('Đồ thị và thuật toán duyệt', ['Phân biệt đồ thị có hướng với vô hướng.', 'BFS dùng hàng đợi tìm đường ít cạnh nhất, DFS dùng ngăn xếp.', 'Đánh dấu đỉnh đã thăm để tránh lặp vô hạn trên đồ thị.'], 'graphs')
    ], illustration: 'search'
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
    slides: [
      slide('Logic: kiểm tra giá trị đúng/sai', ['Dùng bảng chân trị để kiểm tra phát biểu.', 'Phép kéo theo chỉ sai khi tiền đề đúng, kết luận sai.', 'Phủ định lượng từ phải đổi “mọi” với “tồn tại”.'], 'logic'),
      slide('Quan hệ không nhất thiết là hàm', ['Quan hệ là tập các cặp có thứ tự.', 'Hàm yêu cầu mỗi đầu vào có đúng một đầu ra.', 'Kiểm tra phản xạ, đối xứng, bắc cầu khi xét quan hệ tương đương.'], 'relations'),
      slide('Đồ thị: bắt đầu từ đỉnh và cạnh', ['Phân biệt đồ thị có hướng với vô hướng.', "Đường đi nối tiếp các cạnh, còn chu trình quay về điểm đầu.", 'Cây liên thông không có chu trình trong mô hình vô hướng.'], 'graph-theory')
    ], illustration: 'search'
  }
]

export const findCourse = id => courseCatalog.find(course => course.id === id)
