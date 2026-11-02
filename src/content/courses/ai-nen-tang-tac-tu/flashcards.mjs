const course = 'ai-nen-tang-tac-tu'
const intro = '01-tri-tue-nhan-tao-va-tac-tu'
const arch = '02-kien-truc-tac-tu-va-dieu-khien-phan-cap'
const search = '03-tim-kiem-loi-giai'
const logic = '05-menh-de-va-suy-dien'
const relations = '15-ca-the-va-quan-he'

export const flashcards = [
  {
    "id": "ai-nen-tang-tac-tu-ch04-fc01",
    "front": "Bài toán thỏa mãn ràng buộc (CSP) được cấu thành bởi những thành phần nào?",
    "back": "Gồm bộ ba: Tập hợp các biến đại số (V), miền giá trị của từng biến (dom), và tập các ràng buộc cứng/mềm (C). Nghiệm là một phép gán toàn phần thỏa mãn toàn bộ ràng buộc.",
    "category": "ai-nen-tang-tac-tu"
  },
  {
    "id": "ai-nen-tang-tac-tu-ch04-fc02",
    "front": "Khi nào một cung <X, c> trong mạng ràng buộc được gọi là nhất quán cung (Arc Consistent)?",
    "back": "Khi với mọi giá trị x trong dom[X], luôn tìm được ít nhất một bộ giá trị tương thích của các biến lân cận trong phạm vi của c sao cho ràng buộc c được thỏa mãn.",
    "category": "ai-nen-tang-tac-tu"
  },
  {
    "id": "ai-nen-tang-tac-tu-ch04-fc03",
    "front": "Độ phức tạp tính toán của thuật toán Khử biến (Variable Elimination) phụ thuộc vào yếu tố nào?",
    "back": "Tỷ lệ tuyến tính với số lượng biến n, nhưng tăng theo hàm mũ theo độ rộng cây (treewidth) của đồ thị ràng buộc ứng với thứ tự khử biến được chọn.",
    "category": "ai-nen-tang-tac-tu"
  },
  {
    "id": "ai-nen-tang-tac-tu-ch04-fc04",
    "front": "Cơ chế nào giúp Luyện kim mô phỏng (Simulated Annealing) thoát khỏi cực tiểu cục bộ?",
    "back": "Xác suất chấp nhận bước đi làm xấu đi P = exp(-delta_h / T). Ở nhiệt độ T cao, thuật toán tự do nhảy qua rào cản thế năng; khi T giảm dần, thuật toán hội tụ tham lam về cực tiểu.",
    "category": "ai-nen-tang-tac-tu"
  },
  { course, lesson: intro, q: 'Tác tử tính toán được định nghĩa thế nào và đánh giá ra sao?', a: 'Tác tử tính toán là tác tử mà các quyết định hành động có thể phân rã thành các phép toán nguyên thủy hiện thực hóa trên thiết bị vật lý. Tác tử được đánh giá duy nhất dựa trên cách thức nó hành động trong môi trường.' },
  { course, lesson: intro, q: 'Năm luồng đầu vào quyết định hành động của tác tử trong mô hình hộp đen gồm những gì?', a: 'Tri thức tiên nghiệm, kích thích từ môi trường, lịch sử kinh nghiệm quá khứ, mục tiêu hoặc sở thích, và năng lực hành động nguyên thủy.' },
  { course, lesson: intro, q: 'Mười chiều kích phức tạp trong không gian thiết kế tác tử có ý nghĩa gì?', a: 'Định hình cấu trúc và năng lực tác tử gồm: Tính mô đun, tầm nhìn lập kế hoạch, phương thức biểu diễn, giới hạn tính toán, khả năng học tập, tính bất định, cấu trúc sở thích, số lượng tác tử, tính tương tác và sự tương tác giữa các chiều.' },
  { course, lesson: intro, q: 'Bốn lớp giải pháp thường gặp trong AI khác nhau thế nào?', a: 'Nghiệm tối ưu (tốt nhất theo hàm mục tiêu), nghiệm thỏa mãn (đủ tốt theo tiêu chuẩn), nghiệm xấp xỉ tối ưu (nằm trong dung sai bảo đảm so với tối ưu), và nghiệm có xác suất đúng cao (lý thuyết PAC).' },
  { course, lesson: arch, q: 'Thân thể và bộ điều khiển tác tử tương tác với nhau qua những thành phần nào?', a: 'Thân thể gồm cảm biến chuyển đổi kích thích môi trường thành nhận thức gửi lên bộ điều khiển, và cơ cấu chấp hành nhận lệnh từ bộ điều khiển để chuyển thành hành động vật lý tác động lên môi trường.' },
  { course, lesson: arch, q: 'Vì sao tác tử cần trạng thái niềm tin thay vì lưu trữ toàn bộ lịch sử?', a: 'Vì dòng lịch sử tương tác kéo dài vô hạn trong khi dung lượng bộ nhớ tác tử là hữu hạn. Trạng thái niềm tin cô đọng toàn bộ thông tin quá khứ cần thiết phục vụ cho các quyết định hành động ở hiện tại và tương lai.' },
  { course, lesson: arch, q: 'Hai hàm tác tử hình thức remember và command có vai trò gì?', a: 'Hàm remember: S x P -> S cập nhật trạng thái niềm tin khi có nhận thức mới; hàm command: S x P -> C xác định lệnh điều khiển dựa trên trạng thái niềm tin hiện tại và nhận thức tức thời.' },
  { course, lesson: arch, q: 'Lợi ích cốt lõi của kiến trúc điều khiển phân cấp là gì?', a: 'Tách biệt các tầng theo tầm nhìn thời gian và mức độ trừu tượng. Tầng thấp phản xạ nhanh chóng với biến cố tức thời, che giấu chi tiết phần cứng để tầng cao tập trung hoạch định chiến lược dài hạn.' },
  { course, lesson: search, q: 'Không gian trạng thái hoàn chỉnh gồm những thành phần nào và đường đi nghiệm được xác định ra sao?', a: 'Gồm tập trạng thái, trạng thái xuất phát, tập các hành động hợp lệ sinh trạng thái láng giềng, vị từ kiểm tra trạng thái mục tiêu và hàm chi phí cung. Nghiệm là một chuỗi hành động dẫn từ trạng thái xuất phát đến trạng thái mục tiêu.' },
  { course, lesson: search, q: 'Vì sao tìm kiếm sâu dần (IDS) kết hợp được ưu điểm của cả BFS và DFS?', a: 'IDS lặp lại DFS với ngưỡng độ sâu tăng dần. Nó bảo đảm tính hoàn chỉnh và tìm ra nghiệm tối ưu (ít cung nhất) như BFS, nhưng chỉ tiêu thụ bộ nhớ tuyến tính O(bm) như DFS.' },
  { course, lesson: search, q: 'Hàm heuristic chấp nhận được và hàm heuristic đơn điệu khác nhau thế nào trong thuật toán A*?', a: 'Heuristic chấp nhận được không bao giờ ước tính vượt quá chi phí thực tế (h(n) <= cost*(n)), bảo đảm tính tối ưu của A*. Heuristic đơn điệu thỏa mãn bất đẳng thức tam giác (h(n) <= cost(n, n\') + h(n\')), bảo đảm giá trị f tăng đơn điệu và cho phép cắt tỉa đa đường đi an toàn tuyệt đối.' },
  { course, lesson: search, q: 'Cắt tỉa chu trình và cắt tỉa đa đường đi khác nhau thế nào về bộ nhớ và phạm vi bảo vệ?', a: 'Cắt tỉa chu trình kiểm tra nút lặp trên chính đường đi hiện tại (tốn 0 bộ nhớ phụ, không chống được trùng trạng thái giữa các nhánh). Cắt tỉa đa đường đi lưu tập explored toàn cục để loại bỏ mọi đường đi tới sau (tốn bộ nhớ cấp số nhân, triệt tiêu bùng nổ tổ hợp trên đồ thị dày).' },
  { course, lesson: logic, q: 'Hệ quả logic và một thủ tục suy diễn khác nhau thế nào?', a: 'Hệ quả logic là quan hệ ngữ nghĩa: Kết luận đúng trong mọi mô hình của cơ sở tri thức. Thủ tục suy diễn là cách thao tác trên biểu thức để tìm chứng minh. Tính đúng đắn bảo đảm kết luận tìm được là hệ quả logic; tính đầy đủ bảo đảm tìm được mọi hệ quả trong phạm vi đã nêu.' },
  { course, lesson: logic, q: 'Một mệnh đề xác định gồm những thành phần nào?', a: 'Gồm một nguyên tử ở đầu và một hội các nguyên tử ở thân, đọc là đầu đúng nếu mọi nguyên tử trong thân đúng. Thân rỗng tạo thành một sự kiện. Mệnh đề tương đương một tuyển chứa đúng một literal dương.' },
  { course, lesson: logic, q: 'Không chứng minh được một nguyên tử có đồng nghĩa với chứng minh phủ định của nó không?', a: 'Không. Trong ngữ nghĩa thông thường, một nguyên tử có thể đúng ở mô hình này và sai ở mô hình khác. Muốn dùng sự thất bại của chứng minh để kết luận phủ định, phải nêu rõ giả định tri thức đầy đủ và các điều kiện của thủ tục tìm kiếm.' },
  { course, lesson: logic, q: 'Suy luận chẩn đoán bằng giả thuyết cần thỏa điều kiện nào?', a: 'Các giả thuyết cùng với tri thức nền phải giải thích được quan sát và không dẫn đến mâu thuẫn. Tính tối thiểu thường được xét theo quan hệ bao hàm tập hợp, không tự động có nghĩa là ít giả thuyết nhất.' },
  { course, lesson: relations, q: 'Hằng ký hiệu và cá thể mà nó biểu thị có phải cùng một đối tượng không?', a: 'Không. Hằng là một ký hiệu của ngôn ngữ. Phép diễn giải ánh xạ hằng đó tới một cá thể trong miền. Hai hằng khác nhau vẫn có thể biểu thị cùng một cá thể nếu không giả định tên duy nhất.' },
  { course, lesson: relations, q: 'Một biểu thức không biến (ground) có đặc điểm gì?', a: 'Biểu thức không chứa biến logic. Một thể hiện không biến thu được bằng cách thay nhất quán mọi biến trong biểu thức bằng các hạng không biến.' },
  { course, lesson: relations, q: 'Phép thế tác động thế nào khi một biến xuất hiện nhiều lần?', a: 'Mọi lần xuất hiện của biến đó đều được thay bằng cùng một hạng. Phép áp dụng là đồng thời, không tự động áp dụng lại phép thế bên trong hạng vừa thay vào.' },
  { course, lesson: relations, q: 'Một phép hợp nhất tổng quát nhất bảo đảm điều gì?', a: 'Nó làm hai biểu thức trở nên giống hệt nhau và giữ lại mức tổng quát lớn nhất. Mọi phép hợp nhất khác đều có thể thu được bằng cách áp dụng thêm một phép thế vào kết quả tổng quát nhất, trong phạm vi các biến đang xét.' },
  {
    "id": "fc-artint-ch6-01",
    "front": "Giả thiết STRIPS (STRIPS Assumption) phát biểu điều gì?",
    "back": "Mọi đặc trưng nguyên thủy không xuất hiện trong danh sách hiệu ứng (effects) của một hành động thì mặc định giữ nguyên vẹn giá trị như ở trạng thái ngay trước đó.",
    "category": "Lập kế hoạch tiền định",
    "lecture": "06-lap-ke-hoach-tien-dinh"
  },
  {
    "id": "fc-artint-ch6-02",
    "front": "Công thức tính tiền điều kiện yếu nhất (weakest precondition) wp(g, act) trong STRIPS là gì?",
    "back": "wp(g, act) = Precondition(act) ∪ (g \\ Effects(act)), với điều kiện act là hữu ích và không chứa hiệu ứng làm sai lệch bất kỳ mệnh đề nào của g.",
    "category": "Lập kế hoạch tiền định",
    "lecture": "06-lap-ke-hoach-tien-dinh"
  },
  {
    "id": "fc-artint-ch6-03",
    "front": "Trong lập kế hoạch thứ tự từng phần (POP), khi một liên kết nhân quả <act_0, P, act_1> bị đe dọa bởi hành động A, có hai phương án bảo vệ nào?",
    "back": "Giáng cấp (Demotion): Ép buộc A < act_0; hoặc Thúc đẩy (Promotion): Ép buộc act_1 < A.",
    "category": "Lập kế hoạch tiền định",
    "lecture": "06-lap-ke-hoach-tien-dinh"
  },
  {
    "id": "fc-artint-ch6-04",
    "front": "Vì sao tìm kiếm lùi trong không gian trạng thái thuần túy lại bất khả thi đối với các bài toán thực tế?",
    "back": "Vì mục tiêu chỉ là phép gán từng phần cho một số đặc trưng, số lượng trạng thái thỏa mãn mục tiêu rất lớn (hàng triệu trạng thái), khiến tập biên ban đầu bùng nổ ngay lập tức.",
    "category": "Lập kế hoạch tiền định",
    "lecture": "06-lap-ke-hoach-tien-dinh"
  },
  {
    "id": "fc-artint-ch6-05",
    "front": "Heuristic danh sách xóa rỗng (Empty-Delete-List Heuristic) được tính toán như thế nào?",
    "back": "Nới lỏng bài toán bằng cách loại bỏ toàn bộ danh sách xóa trong STRIPS (các sự kiện đã đạt được không bao giờ bị mất), từ đó tìm kế hoạch tối ưu cho bài toán nới lỏng trong thời gian đa thức.",
    "category": "Lập kế hoạch tiền định",
    "lecture": "06-lap-ke-hoach-tien-dinh"
  },
  {
    "id": "fc-artint-ch7-01",
    "front": "Mục tiêu tối thượng của học máy trong kiến trúc tác tử tính toán là gì?",
    "back": "Mục tiêu không phải là ghi nhớ dữ liệu huấn luyện, mà là xây dựng mô hình về cơ chế sinh dữ liệu của thế giới để cải thiện hành vi và ra quyết định tối ưu trong tương lai.",
    "category": "Học máy có giám sát",
    "lecture": "07-hoc-may-co-giam-sat"
  },
  {
    "id": "fc-artint-ch7-02",
    "front": "Điểm dự đoán tối ưu trên tập dữ liệu tương ứng với các hàm mất mát L0, L1 và L2 là gì?",
    "back": "Dưới mất mát L0 (0-1), điểm dự đoán tối ưu là Yếu vị (Mode); dưới mất mát L1 (sai số tuyệt đối), tối ưu là Trung vị (Median); dưới mất mát L2 (bình phương), tối ưu là Kỳ vọng (Mean).",
    "category": "Học máy có giám sát",
    "lecture": "07-hoc-may-co-giam-sat"
  },
  {
    "id": "fc-artint-ch7-03",
    "front": "Độ lợi thông tin (Information Gain) trong cây quyết định được tính như thế nào?",
    "back": "Gain(E, c) bằng Entropy của tập mẫu trước phân tách trừ đi tổng Entropy có trọng số của các nhánh con sau khi kiểm tra điều kiện Boolean c.",
    "category": "Học máy có giám sát",
    "lecture": "07-hoc-may-co-giam-sat"
  },
  {
    "id": "fc-artint-ch7-04",
    "front": "Sự khác biệt bản chất giữa điều chuẩn L1 (Lasso) và điều chuẩn L2 (Ridge) là gì?",
    "back": "L2 thu hẹp độ lớn trọng số về gần 0 nhưng không triệt tiêu; L1 nhờ vào hình học đa diện góc nhọn có thể triệt tiêu hoàn toàn nhiều trọng số về đúng 0, tạo tính thưa và tự động chọn đặc trưng.",
    "category": "Học máy có giám sát",
    "lecture": "07-hoc-may-co-giam-sat"
  },
  {
    "id": "fc-artint-ch7-05",
    "front": "Cơ chế hoạt động cốt lõi của Cây tăng cường Gradient (GBDT) là gì?",
    "back": "GBDT huấn luyện chuỗi cây quyết định tuần tự, trong đó mỗi cây mới học cách khớp trực tiếp với vector gradient âm (phần dư) của hàm mất mát từ các cây trước đó.",
    "category": "Học máy có giám sát",
    "lecture": "07-hoc-may-co-giam-sat"
  },
  {
    "id": "fc-artint-ch8-01",
    "front": "Định lý xấp xỉ phổ quát (Universal Approximation Theorem) khẳng định điều gì về mạng nơ-ron truyền thẳng?",
    "back": "Một mạng nơ-ron chỉ với một tầng ẩn phi tuyến duy nhất chứa đủ số lượng nơ-ron có thể xấp xỉ bất kỳ hàm liên tục nào trên một tập compact trong R^d với độ chính xác tùy ý.",
    "category": "Mạng nơ-ron và học sâu",
    "lecture": "08-mang-no-ron-va-hoc-sau"
  },
  {
    "id": "fc-artint-ch8-02",
    "front": "Cơ chế hoạt động cốt lõi của thuật toán Adam (Adaptive Moment Estimation) là gì?",
    "back": "Adam kết hợp động lượng bậc một (Momentum) để duy trì hướng đi theo quán tính và động lượng bậc hai (RMS-Prop) để tự động điều chỉnh tốc độ học riêng biệt cho từng tham số theo bình phương gradient lịch sử.",
    "category": "Mạng nơ-ron và học sâu",
    "lecture": "08-mang-no-ron-va-hoc-sau"
  },
  {
    "id": "fc-artint-ch8-03",
    "front": "Hai đặc tính then chốt giúp mạng nơ-ron tích chập (CNN) xử lý hình ảnh vượt trội hơn mạng truyền thẳng (FNN) là gì?",
    "back": "Trường tiếp nhận cục bộ (Local Receptive Fields) giúp nắm bắt tương quan không gian gần, và chia sẻ trọng số (Weight Sharing) giúp tạo tính bất biến tịnh tiến đồng thời giảm đột biến số lượng tham số.",
    "category": "Mạng nơ-ron và học sâu",
    "lecture": "08-mang-no-ron-va-hoc-sau"
  },
  {
    "id": "fc-artint-ch8-04",
    "front": "Khối tàn dư (Residual Block) trong kiến trúc ResNet giải quyết vấn đề suy thoái mạng sâu như thế nào?",
    "back": "Thông qua đường tắt đồng nhất H(x) = F(x) + x, gradient có thể chảy trực tiếp ngược về các tầng nông mà không bị triệt tiêu, giúp mạng chỉ cần học phần biến đổi vi sai F(x) thay vì toàn bộ hàm ánh xạ.",
    "category": "Mạng nơ-ron và học sâu",
    "lecture": "08-mang-no-ron-va-hoc-sau"
  },
  {
    "id": "fc-artint-ch8-05",
    "front": "Cơ chế Tự chú ý (Self-Attention) trong Transformer khắc phục nhược điểm cốt lõi nào của RNN/LSTM?",
    "back": "Cho phép mọi cặp từ vựng trong chuỗi tương tác trực tiếp với độ dài đường dẫn O(1) bất kể khoảng cách, đồng thời xử lý song song toàn bộ ngữ cảnh mà không bị nghẽn cổ chai tuần tự.",
    "category": "Mạng nơ-ron và học sâu",
    "lecture": "08-mang-no-ron-va-hoc-sau"
  }
]
