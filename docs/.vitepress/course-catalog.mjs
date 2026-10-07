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
      slide('Từ bài toán đến không gian trạng thái', ['Xác định trạng thái đầu, hành động hợp lệ và điều kiện đích.', 'Đồ thị mô tả quan hệ chuyển trạng thái; cây tìm kiếm mô tả các đường đã mở rộng.', 'Phân biệt số bước với tổng chi phí trước khi chọn thuật toán.'], '02-tim-kiem-mu', '', 'Một đường 3 cạnh có thể đắt hơn đường 4 cạnh nếu trọng số khác nhau.'),
      slide('BFS, DFS, UCS & IDS', ['BFS dùng hàng đợi FIFO, tìm đường ít cạnh nhất khi mọi bước có cùng chi phí.', 'DFS dùng ngăn xếp; tiết kiệm bộ nhớ theo chiều sâu nhưng không bảo đảm tối ưu.', 'UCS ưu tiên chi phí đã đi g(n). Với chi phí bước có chặn dưới dương, nó đầy đủ và tối ưu.', 'IDS lặp DFS với giới hạn độ sâu tăng dần.'], '02-tim-kiem-mu'),
      slide('Greedy và A* nhìn về phía đích', ['Greedy chọn h(n) nhỏ nhất, có thể nhanh nhưng không bảo đảm lời giải tối ưu.', 'A* kết hợp chi phí đã đi với ước lượng còn lại.', 'Heuristic admissible không ước lượng quá cao; consistent giúp xử lý đồ thị thuận lợi hơn.'], '03-tim-kiem-kinh-nghiem', 'A*: f(n) = g(n) + h(n)'),
      slide('Minimax & cắt tỉa Alpha–Beta', ['MAX chọn giá trị lớn nhất, MIN chọn giá trị nhỏ nhất ở tầng của mình.', 'Lan truyền giá trị từ lá về gốc; kết quả phụ thuộc hàm đánh giá khi giới hạn độ sâu.', 'Alpha–Beta bỏ nhánh không thể thay đổi quyết định Minimax.'], '04-tim-kiem-doi-khang', 'Cắt nhánh khi α ≥ β'),
      slide('Biểu diễn tri thức bằng logic', ['Mệnh đề diễn tả phát biểu đúng/sai; logic vị từ diễn tả đối tượng và quan hệ.', 'Phân biệt lượng từ “mọi” với “tồn tại”; luôn xác định miền xét.', 'Suy luận cần luật hợp lệ, không chỉ dựa trên một vài ví dụ đúng.'], '14-logic-bieu-dien-tri-thuc', '¬∀x P(x) ⇔ ∃x ¬P(x)')
    ], illustration: 'search'
  },
  {
    id: 'toan-cho-ai', code: '02', name: 'Cơ sở toán cho AI', short: 'Toán cho AI', current: true,
    description: 'Đọc tối ưu hóa từ hàm mục tiêu, đạo hàm đến hình học của tập lồi.',
    foundations: ['tap-hop', 'ham-so', 'vector', 'ma-tran', 'tich-vo-huong', 'chuan', 'gioi-han', 'dao-ham', 'dao-ham-rieng', 'gradient', 'quy-tac-chuoi', 'tri-rieng', 'to-hop-loi'],
    parts: [
      {
        title: 'Phần 1. Tối ưu hóa và Gradient Descent',
        description: 'Hàm mục tiêu, hướng giảm dốc và cập nhật tham số đạo hàm riêng.',
        lessons: ['bai-01-nhap-mon-toi-uu']
      },
      {
        title: 'Phần 2. Hình học tập lồi và phân tích nghiệm',
        description: 'Tập lồi, tổ hợp lồi, hàm lồi và tính chất cực tiểu toàn cục.',
        lessons: ['bai-02-tap-loi']
      }
    ],
    lessons: [
      lesson('bai-01-nhap-mon-toi-uu', 'Nhập môn tối ưu hóa', ['ham-so', 'vector', 'dao-ham', 'gradient', 'chuan']),
      lesson('bai-02-tap-loi', 'Tập lồi & hình học của nghiệm', ['tap-hop', 'vector', 'tich-vo-huong', 'to-hop-loi'])
    ],
    slides: [
      slide('Một bài toán tối ưu có ba thành phần', ['Biến quyết định biểu diễn điều có thể thay đổi.', 'Hàm mục tiêu đo điều muốn giảm hoặc tăng.', 'Ràng buộc xác định miền nghiệm khả thi; phải kiểm tra nghiệm có nằm trong miền đó không.'], 'bai-01-nhap-mon-toi-uu', 'min f(x), với x thuộc miền khả thi'),
      slide('Đọc gradient trước khi cập nhật', ['Gradient gom các đạo hàm riêng, chỉ hướng tăng nhanh nhất tại điểm khả vi.', 'Đi ngược gradient để tìm hướng giảm cục bộ.', 'Tốc độ học quyết định độ dài bước; bước quá lớn có thể làm mất hội tụ.'], 'bai-01-nhap-mon-toi-uu', 'x mới = x cũ − η∇f(x cũ)', 'f(x)=x²: x mới=(1−2η)x cũ; với 0<η<1, giá trị |x| giảm.'),
      slide('Tập lồi: đoạn thẳng vẫn ở trong tập', ['Lấy hai điểm bất kỳ trong tập và nối chúng bằng đoạn thẳng.', 'Nếu mọi điểm trên đoạn đều thuộc tập, đó là tập lồi.', 'Tổ hợp lồi dùng trọng số không âm, tổng trọng số bằng 1.'], 'bai-02-tap-loi', 'λx + (1−λ)y, 0 ≤ λ ≤ 1'),
      slide('Các phép xây dựng tập lồi', ['Giao của các tập lồi vẫn lồi.', 'Siêu phẳng và nửa không gian là các cấu trúc cơ bản.', 'Ảnh và ảnh ngược qua ánh xạ affine bảo toàn tính lồi; phép hợp nói chung không bảo toàn.'], 'bai-02-tap-loi')
    ], illustration: 'gradient'
  },
  {
    id: 'xac-suat-thong-ke', code: '03', name: 'Xác suất thống kê', short: 'Xác suất thống kê', current: true,
    description: 'Đi từ biến cố và xác suất có điều kiện đến phân phối, kỳ vọng và biến thiên.',
    foundations: ['tap-hop', 'khong-gian-mau', 'to-hop', 'xac-suat-co-dieu-kien', 'doc-lap', 'bien-ngau-nhien', 'ky-vong', 'phuong-sai', 'tich-phan', 'mau-tong-the'],
    parts: [
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
      lesson('01-xac-suat-va-bayes', 'Xác suất có điều kiện & Bayes', ['tap-hop', 'khong-gian-mau', 'xac-suat-co-dieu-kien', 'doc-lap']),
      lesson('02-bien-ngau-nhien', 'Biến ngẫu nhiên & phân phối', ['bien-ngau-nhien', 'to-hop', 'tich-phan']),
      lesson('03-ky-vong-phuong-sai', 'Kỳ vọng, phương sai & mẫu dữ liệu', ['ky-vong', 'phuong-sai', 'mau-tong-the'])
    ],
    slides: [
      slide('Xác suất có điều kiện thay đổi miền xét', ['P(A|B) thu hẹp việc xét kết quả về biến cố B.', 'Hai biến cố độc lập không làm thay đổi xác suất của nhau.', 'Độc lập khác với loại trừ nhau.'], '01-xac-suat-va-bayes', 'P(A|B) = P(A∩B) / P(B), P(B)>0'),
      slide('Bayes cập nhật từ quan sát', ['Prior là xác suất trước quan sát.', 'Likelihood là mức phù hợp của quan sát khi giả thuyết đúng.', 'Posterior là xác suất sau quan sát; cần tính cả khả năng quan sát từ các giả thuyết khác.'], '01-xac-suat-va-bayes', 'P(A|B) = P(B|A)P(A) / P(B)'),
      slide('Phân phối mô tả một biến ngẫu nhiên', ['PMF cho xác suất tại từng giá trị của biến rời rạc.', 'PDF là mật độ; xác suất liên tục được tính trên khoảng bằng tích phân.', 'CDF F(x)=P(X≤x) dùng được cho cả rời rạc và liên tục.'], '02-bien-ngau-nhien'),
      slide('Trung tâm, độ phân tán và mẫu', ['Kỳ vọng là trung bình theo xác suất, có thể không là giá trị quan sát được.', 'Phương sai đo bình phương độ lệch; độ lệch chuẩn quay về cùng đơn vị với dữ liệu.', 'Thống kê mẫu ước lượng tham số tổng thể và phụ thuộc cách lấy mẫu.'], '03-ky-vong-phuong-sai', 'Var(X) = E[X²] − E[X]²')
    ], illustration: 'bayes'
  },
  {
    id: 'xu-ly-du-lieu', code: '04', name: 'Lập trình xử lý dữ liệu', short: 'Xử lý dữ liệu', current: true,
    description: 'Đọc và biến đổi dữ liệu bằng Python, NumPy và pandas một cách có kiểm chứng.',
    foundations: ['bien-kieu', 'list', 'dictionary', 'ham-lap-trinh', 'vong-lap', 'mang', 'chi-muc', 'con-tro', 'vector-hoa', 'broadcasting', 'gia-tri-thieu', 'ky-vong', 'phuong-sai'],
    parts: [
      {
        title: 'Phần 1. Môi trường và ngôn ngữ Python',
        description: 'Thiết lập quy trình phân tích dữ liệu, kiểu dữ liệu cốt lõi, hàm và cấu trúc điều khiển.',
        lessons: ['bai-01-tong-quan-cong-cu-chinh-sach-ai', 'bai-02-python-co-ban']
      },
      {
        title: 'Phần 2. Tính toán vector với NumPy',
        description: 'Mảng nhiều chiều ndarray, bộ nhớ liên tục, ufunc và cơ chế broadcasting.',
        lessons: ['bai-03-numpy']
      },
      {
        title: 'Phần 3. Thao tác và phân tích dữ liệu với pandas',
        description: 'Cấu trúc Series, DataFrame, lọc theo nhãn/vị trí, xử lý giá trị thiếu và gom nhóm GroupBy.',
        lessons: ['bai-04-lam-quen-pandas', 'bai-05-series-dataframe-chuyen-sau']
      }
    ],
    lessons: [
      lesson('bai-01-tong-quan-cong-cu-chinh-sach-ai', 'Tổng quan, công cụ & quy trình học', ['bien-kieu', 'ham-lap-trinh']),
      lesson('bai-02-python-co-ban', 'Python cơ bản cho xử lý dữ liệu', ['bien-kieu', 'list', 'dictionary', 'vong-lap', 'ham-lap-trinh']),
      lesson('bai-03-numpy', 'NumPy & tư duy vector hóa', ['mang', 'chi-muc', 'con-tro', 'vector-hoa', 'broadcasting']),
      lesson('bai-04-lam-quen-pandas', 'Làm quen với pandas', ['chi-muc', 'dictionary', 'gia-tri-thieu']),
      lesson('bai-05-series-dataframe-chuyen-sau', 'Series & DataFrame chuyên sâu', ['chi-muc', 'gia-tri-thieu', 'ky-vong', 'phuong-sai'])
    ],
    slides: [
      slide('Một quy trình phân tích có thể kiểm tra', ['Xác định câu hỏi trước khi chọn công cụ.', 'Giữ nguồn dữ liệu, môi trường và các bước biến đổi để tái lập kết quả.', 'Đọc và kiểm tra code sinh ra; người dùng chịu trách nhiệm về kết luận.'], 'bai-01-tong-quan-cong-cu-chinh-sach-ai'),
      slide('Python: kiểu, dãy và hàm', ['Phân biệt số, chuỗi, Boolean và container.', 'Chỉ mục từ 0; lát cắt theo vị trí không lấy điểm stop.', 'return cho kết quả để dùng tiếp, khác với print.'], 'bai-02-python-co-ban'),
      slide('NumPy: đọc shape trước khi tính', ['dtype quy định kiểu lưu và độ chính xác; không bỏ qua nguy cơ tràn số.', 'Vector hóa thao tác trên mảng, tránh nhiều vòng lặp Python.', 'Broadcasting so trục từ cuối; view có thể dùng chung dữ liệu với mảng gốc.'], 'bai-03-numpy'),
      slide('pandas: nhãn khác vị trí', ['Series là một chiều có nhãn; DataFrame là bảng hai chiều.', 'loc theo nhãn, iloc theo vị trí số nguyên.', 'Đọc kiểu cột và giá trị thiếu trước khi lọc hoặc tổng hợp.'], 'bai-04-lam-quen-pandas'),
      slide('Đừng để phép tổng hợp che mất dữ liệu', ['groupby tách nhóm rồi áp dụng tổng hợp hoặc biến đổi.', 'Phân biệt số hàng, số giá trị không thiếu và số giá trị duy nhất.', 'Kiểm tra nhãn, kiểu và ý nghĩa của kết quả sau mỗi chuỗi biến đổi.'], 'bai-05-series-dataframe-chuyen-sau')
    ], illustration: 'broadcast'
  },
  {
    id: 'vat-ly-2', code: '05', name: 'Vật lý đại cương 2', short: 'Vật lý 2', current: true,
    description: 'Hiểu điện trường và điện thế từ lực, vector, đạo hàm và tích phân.',
    foundations: ['vector', 'tich-vo-huong', 'chuan', 'dao-ham', 'dao-ham-rieng', 'gradient', 'tich-phan', 'dien-tich', 'luc', 'cong-nang-luong', 'dien-the', 'thong-luong', 'don-vi', 'song'],
    parts: [
      {
        title: 'Phần 1. Tương tác tĩnh điện và điện trường',
        description: 'Định luật Coulomb, nguyên lý chồng chất và vector cường độ điện trường.',
        lessons: ['01-dien-truong-coulomb']
      },
      {
        title: 'Phần 2. Năng lượng tĩnh điện và điện thế',
        description: 'Công của lực điện trường, điện thế, mặt đẳng thế và gradient.',
        lessons: ['02-dien-the']
      },
      {
        title: 'Phần 3. Thông lượng và định luật Gauss',
        description: 'Thông lượng điện trường qua mặt kín và tính điện trường đối xứng.',
        lessons: ['03-dinh-luat-gauss']
      }
    ],
    lessons: [
      lesson('01-dien-truong-coulomb', 'Điện trường & định luật Coulomb', ['vector', 'chuan', 'dien-tich', 'luc', 'don-vi']),
      lesson('02-dien-the', 'Điện thế, công & gradient', ['cong-nang-luong', 'dien-the', 'dao-ham', 'gradient', 'tich-phan']),
      lesson('03-dinh-luat-gauss', 'Thông lượng & định luật Gauss', ['tich-vo-huong', 'thong-luong', 'tich-phan', 'dien-tich'])
    ],
    slides: [
      slide('Từ lực Coulomb tới điện trường', ['Điện tích cùng dấu đẩy nhau, trái dấu hút nhau.', 'Điện trường là lực trên một đơn vị điện tích thử dương.', 'Cộng vector các điện trường thành phần; không chỉ cộng độ lớn.'], '01-dien-truong-coulomb', 'E = F/q thử; |E điểm| = k|Q|/r²'),
      slide('Điện thế giúp tính công', ['Hiệu điện thế bằng độ thay đổi thế năng trên một đơn vị điện tích.', 'Điện trường hướng về phía điện thế giảm nhanh nhất.', 'Mặt đẳng thế vuông góc với điện trường ở nơi điện trường khác 0.'], '02-dien-the', 'E = −∇V; ΔU = qΔV'),
      slide('Gauss liên hệ điện tích với thông lượng', ['Tích phân trên mặt kín dùng pháp tuyến hướng ra ngoài.', 'Điện tích nằm bên trong mặt kín quyết định thông lượng tổng.', 'Muốn suy ra E đơn giản từ Gauss, cần đối xứng phù hợp.'], '03-dinh-luat-gauss', '∮ E·dA = Q bên trong / ε₀'),
      slide('Kiểm tra trước khi kết luận', ['Đổi mọi điện tích và khoảng cách về đơn vị thống nhất.', 'Nêu dấu, hướng và đơn vị của kết quả.', 'Phân biệt mô hình điện tích điểm với phân bố điện tích liên tục.'], '01-dien-truong-coulomb', 'N/C = V/m')
    ], illustration: 'field'
  },
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
      slide('Dữ liệu lớn đổi nút thắt của thuật toán', ['Không chỉ xét CPU: bộ nhớ, đọc/ghi và mạng đều có chi phí.', 'Chọn mô hình tính toán phù hợp với nơi dữ liệu nằm.', 'Đánh giá lượng dữ liệu truyền cùng tổng công việc.'], 'bai-01-bai-toan-du-lieu-lon-va-mo-hinh-thuat-toan'),
      slide('Map → nhóm theo khóa → Reduce', ['Map phát các cặp khóa–giá trị.', 'Shuffle đưa các giá trị cùng khóa tới cùng nhóm.', 'Reduce xử lý từng nhóm để thu kết quả cuối.'], 'bai-02-mapreduce-va-xu-ly-du-lieu-lon', '', 'Đếm từ: Map phát (từ,1), Reduce cộng các số 1 theo từ.'),
      slide('Combine cần đúng tính chất phép gom', ['Gom cục bộ giúp giảm truyền dữ liệu.', 'Phép gom cần giữ được thông tin cho kết quả cuối và đáp ứng tính chất cần thiết.', 'Trung bình của các trung bình không đúng nếu nhóm có kích thước khác nhau; truyền (tổng, số lượng).'], 'bai-02-mapreduce-va-xu-ly-du-lieu-lon'),
      slide('Thời gian pha do máy chậm nhất quyết định', ['Một phân vùng quá lớn làm những máy còn lại chờ.', 'Thêm máy có thể tăng chi phí đồng bộ và truyền.', 'Kiểm tra cân bằng tải, lượng truyền và khả năng phục hồi khi máy lỗi.'], 'bai-02-mapreduce-va-xu-ly-du-lieu-lon'),
      slide('PageRank: mô hình hóa sự quan trọng của trang', ['Một trang quan trọng nếu được trỏ bởi các trang quan trọng khác.', 'Random Surfer di chuyển ngẫu nhiên trên đồ thị liên kết Web.', 'Trạng thái dừng r = M*r chính là vector riêng ứng với trị riêng 1.'], 'bai-03-pagerank-mo-hinh-va-tinh-toan', 'r = β·M·r + (1−β)/N·1', 'β = 0.85 xử lý triệt để Spider Traps và Dead Ends.')
    ], illustration: 'mapreduce'
  },
  {
    id: 'dsa', code: '07', name: 'Cấu trúc dữ liệu & Giải thuật', short: 'CTDL & Giải thuật', current: false,
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
      slide('Sắp xếp: chọn theo bối cảnh', ['Insertion Sort phù hợp dữ liệu nhỏ hoặc gần có thứ tự.', 'Merge Sort có O(n log n) nhưng cần bộ nhớ phụ tùy cách cài đặt.', 'Quick Sort trung bình nhanh; lựa chọn pivot ảnh hưởng trường hợp xấu.'], 'sorting'),
      slide('Tìm kiếm nhị phân cần thứ tự', ['Duy trì miền còn có thể chứa đáp án.', 'Mỗi bước bỏ khoảng một nửa miền tìm kiếm.', 'Kiểm tra biên và điều kiện dừng; dữ liệu chưa sắp xếp cần cách khác.'], 'searching', 'Số bước: O(log n)'),
      slide('Cây và đồ thị lưu quan hệ', ['Cây có cấu trúc cha–con; đồ thị có thể có chu trình.', 'BFS dùng hàng đợi; DFS dùng ngăn xếp hoặc đệ quy.', 'Đánh dấu đã thăm để tránh lặp vô hạn trên đồ thị.'], 'graphs')
    ], illustration: 'search'
  },
  {
    id: 'discrete-math', code: '08', name: 'Toán rời rạc', short: 'Toán rời rạc', current: false,
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
      slide('Đồ thị: bắt đầu từ đỉnh và cạnh', ['Phân biệt đồ thị có hướng với vô hướng.', 'Đường đi liên tiếp các cạnh; chu trình quay về điểm đầu.', 'Cây liên thông không có chu trình trong mô hình vô hướng.'], 'graph-theory')
    ], illustration: 'search'
  }
]

export const findCourse = id => courseCatalog.find(course => course.id === id)
