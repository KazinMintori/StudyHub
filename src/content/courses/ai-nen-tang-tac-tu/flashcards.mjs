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
  },
  {
    "id": "fc-artint-ch9-01",
    "front": "Bản chất nhận thức luận của xác suất Bayes trong trí tuệ nhân tạo là gì?",
    "back": "Xác suất là thước đo mức độ thiếu tri thức của tác tử về thế giới, không phải đặc tính vật lý khách quan của vật thể. Định lý Bayes cập nhật niềm tin tiên nghiệm thành hậu nghiệm khi có bằng chứng mới.",
    "category": "Suy luận trong điều kiện bất định",
    "lecture": "09-suy-luan-trong-dieu-kien-bat-dinh"
  },
  {
    "id": "fc-artint-ch9-02",
    "front": "Tại sao tính độc lập có điều kiện lại có vai trò quyết định trong việc xây dựng mạng niềm tin?",
    "back": "Nó cho phép phân rã phân phối đồng thời khổng lồ 2^n - 1 tham số thành tích các phân phối có điều kiện cục bộ P(Xi | parents(Xi)), giúp biểu diễn và tính toán trong thời gian đa thức.",
    "category": "Suy luận trong điều kiện bất định",
    "lecture": "09-suy-luan-trong-dieu-kien-bat-dinh"
  },
  {
    "id": "fc-artint-ch9-03",
    "front": "Cơ chế hoạt động cốt lõi của giải thuật Khử biến (Variable Elimination) là gì?",
    "back": "Sử dụng tính chất phân phối để đẩy phép tính tổng cận biên vào sâu trong biểu thức tích, khử từng biến ẩn bằng cách nhân các nhân tử liên quan rồi cộng tổng, với độ phức tạp theo độ rộng cây.",
    "category": "Suy luận trong điều kiện bất định",
    "lecture": "09-suy-luan-trong-dieu-kien-bat-dinh"
  },
  {
    "id": "fc-artint-ch9-04",
    "front": "Hai giả thiết cơ bản tạo nên cấu trúc của Mô hình Markov ẩn (HMM) là gì?",
    "back": "Giả thiết Markov (trạng thái hiện tại chỉ phụ thuộc trạng thái ngay trước đó) và giả thiết cảm biến (quan sát hiện tại chỉ phụ thuộc trạng thái ẩn hiện tại và độc lập với lịch sử đo đạc).",
    "category": "Suy luận trong điều kiện bất định",
    "lecture": "09-suy-luan-trong-dieu-kien-bat-dinh"
  },
  {
    "id": "fc-artint-ch9-05",
    "front": "Ưu điểm cốt lõi của giải thuật Likelihood Weighting so với Rejection Sampling là gì?",
    "back": "Không bao giờ loại bỏ mẫu. Các biến bằng chứng được gán cứng theo giá trị quan sát và trọng số mẫu được tích lũy bằng tích xác suất các bằng chứng, tránh lãng phí khi bằng chứng hiếm gặp.",
    "category": "Suy luận trong điều kiện bất định",
    "lecture": "09-suy-luan-trong-dieu-kien-bat-dinh"
  },
  {
  "id": "fc-artint-ch10-01",
  "front": "Điểm khác biệt cốt lõi giữa Ước lượng hợp lý cực đại (MLE) và Ước lượng hậu nghiệm cực đại (MAP) là gì?",
  "back": "MLE chỉ tối đa hóa xác suất dữ liệu P(E | m) nên dễ bị quá khớp khi không gian mô hình phong phú. MAP tối đa hóa tích P(E | m)P(m), trong đó tiên nghiệm P(m) đóng vai trò là số hạng điều chuẩn tự nhiên theo nguyên lý Dao cạo Occam.",
  "category": "Học máy trong điều kiện bất định",
  "lecture": "10-hoc-may-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch10-02",
  "front": "Tại sao phân phối Beta và Dirichlet được gọi là phân phối tiên nghiệm liên hợp?",
  "back": "Vì khi kết hợp với hàm hợp lý nhị thức hoặc đa thức, phân phối hậu nghiệm thu được vẫn thuộc cùng một họ phân phối (Beta hoặc Dirichlet), và việc cập nhật niềm tin được thực hiện trực tiếp bằng phép cộng số đếm thực nghiệm vào số đếm giả.",
  "category": "Học máy trong điều kiện bất định",
  "lecture": "10-hoc-may-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch10-03",
  "front": "Tại sao bộ phân loại Naive Bayes bắt buộc phải sử dụng làm trơn Laplace?",
  "back": "Nếu một từ vựng chưa từng xuất hiện cùng một lớp trong tập huấn luyện, tần suất thực nghiệm bằng 0 sẽ triệt tiêu toàn bộ tích xác suất của văn bản về 0, dẫn tới lỗi chia cho 0 khi chuẩn hóa. Làm trơn Laplace gán một xác suất nhỏ đồng đều để giải thuật vận hành ổn định.",
  "category": "Học máy trong điều kiện bất định",
  "lecture": "10-hoc-may-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch10-04",
  "front": "Mối quan hệ toán học giữa Nguyên lý độ dài mô tả tối thiểu (MDL) và suy diễn Bayes là gì?",
  "back": "Nguyên lý MDL (tối thiểu hóa tổng độ dài thông điệp hai phần gồm mô tả mô hình và dữ liệu nén qua mô hình) hoàn toàn tương đương với ước lượng hậu nghiệm cực đại MAP trong thang logarit cơ số 2.",
  "category": "Học máy trong điều kiện bất định",
  "lecture": "10-hoc-may-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch10-05",
  "front": "Bản chất của hai bước lặp (E-step và M-step) trong giải thuật EM là gì?",
  "back": "Bước E sử dụng tham số hiện tại để suy luận phân phối xác suất hậu nghiệm (trách nhiệm mềm) của các biến tiềm ẩn. Bước M sử dụng các trách nhiệm mềm này như số đếm quan sát để cập nhật lại bộ tham số mới tối đa hóa log-hợp lý kỳ vọng.",
  "category": "Học máy trong điều kiện bất định",
  "lecture": "10-hoc-may-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch11-01",
  "front": "Sự khác biệt căn bản giữa xác suất quan sát P(Y | X) và xác suất can thiệp P(Y | do(X)) là gì?",
  "back": "P(Y | X) đo lường tương quan thụ động, cho phép suy luận cả xuôi dòng (nguyên nhân sang kết quả) lẫn ngược dòng (chẩn đoán). P(Y | do(X)) mô tả hành vi dùng ngoại lực ép X nhận giá trị cụ thể, cắt đứt các cơ chế tự nhiên trước đó và chỉ truyền thông tin nhân quả xuôi dòng.",
  "category": "Quan hệ nhân quả",
  "lecture": "11-quan-he-nhan-qua"
},
  {
  "id": "fc-artint-ch11-02",
  "front": "Hành vi can thiệp do(X=x) làm thay đổi cấu trúc đồ thị mạng nhân quả như thế nào?",
  "back": "Tạo ra đồ thị bị cắt cụt (mutilated graph) bằng cách xóa bỏ hoàn toàn tất cả các cung có hướng đi vào X từ các nút cha Parents(X), giải phóng X khỏi sự chi phối của các biến tiền nhân.",
  "category": "Quan hệ nhân quả",
  "lecture": "11-quan-he-nhan-qua"
},
  {
  "id": "fc-artint-ch11-03",
  "front": "Điểm va chạm (Collider: A -> B <- C) có tính chất gì đặc biệt trong tính phân tách d?",
  "back": "Khác với chuỗi liên hoàn và nhánh rẽ, điểm va chạm tự động bị chặn khi không quan sát B. Nhưng khi điều kiện hóa theo B (hoặc con cháu của B), đường đi lại bị mở thông, tạo ra tương quan phụ thuộc giả giữa hai nguyên nhân độc lập (hiệu ứng giải thích loại trừ).",
  "category": "Quan hệ nhân quả",
  "lecture": "11-quan-he-nhan-qua"
},
  {
  "id": "fc-artint-ch11-04",
  "front": "Hai điều kiện của Tiêu chuẩn Cửa sau (Backdoor Criterion) đối với cặp (X, Y) là gì?",
  "back": "(1) Tập biến Z không chứa bất kỳ con cháu nào của biến can thiệp X; (2) Tập biến Z chặn mọi đường đi cửa sau (đường đi bắt đầu bằng mũi tên đi vào X) nối giữa X và Y.",
  "category": "Quan hệ nhân quả",
  "lecture": "11-quan-he-nhan-qua"
},
  {
  "id": "fc-artint-ch11-05",
  "front": "Quy trình ba bước chuẩn mực để tính toán một mệnh đề phản thực tế là gì?",
  "back": "(1) Bắt cóc (Abduction): Cập nhật phân phối hậu nghiệm P(U | e) của các biến ngoại sinh theo bằng chứng thực tế; (2) Can thiệp (Action): Thay thế phương trình của X bằng X=x' tạo mô hình Mx'; (3) Dự đoán (Prediction): Dùng mô hình Mx' và P(U | e) tính phân phối kết quả Y.",
  "category": "Quan hệ nhân quả",
  "lecture": "11-quan-he-nhan-qua"
},
  {
  "id": "fc-artint-ch12-01",
  "front": "Định lý kỳ vọng hữu dụng của von Neumann – Morgenstern khẳng định điều gì?",
  "back": "Nếu sở thích của tác tử thỏa mãn 6 tiên đề duy lý (Đầy đủ, Bắc cầu, Đơn điệu, Phân rã, Liên tục, Thay thế), thì tồn tại hàm giá trị thực u sao cho mức ưa thích đối với mọi xổ số bằng đúng kỳ vọng toán học của hữu dụng.",
  "category": "Lập kế hoạch bất định",
  "lecture": "12-lap-ke-hoach-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch12-02",
  "front": "Thái độ né tránh rủi ro (Risk-averse) được thể hiện như thế nào qua hàm hữu dụng tiền tệ?",
  "back": "Hàm hữu dụng tiền tệ u(M) là hàm lõm (đạo hàm bậc hai âm). Khi đó mức tương đương chắc chắn nhỏ hơn kỳ vọng tiền tệ (CE < E[M]) và phần bù rủi ro dương (RP > 0).",
  "category": "Lập kế hoạch bất định",
  "lecture": "12-lap-ke-hoach-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch12-03",
  "front": "Ý nghĩa của một cung có hướng đi vào nút quyết định trong mạng quyết định là gì?",
  "back": "Là cung thông tin (information link): Chỉ định rằng giá trị của nút cha đó đã được tác tử quan sát và biết trước khi đưa ra quyết định tại nút hiện tại.",
  "category": "Lập kế hoạch bất định",
  "lecture": "12-lap-ke-hoach-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch12-04",
  "front": "Giá trị của thông tin hoàn hảo (VPI) có tính chất căn bản gì và tại sao?",
  "back": "VPI luôn không âm (VPI >= 0) vì trong trường hợp xấu nhất tác tử luôn có thể phớt lờ thông tin mới. VPI là chặn trên lý thuyết cho giá trị của mọi cảm biến có nhiễu.",
  "category": "Lập kế hoạch bất định",
  "lecture": "12-lap-ke-hoach-trong-dieu-kien-bat-dinh"
},
  {
  "id": "fc-artint-ch12-05",
  "front": "Sự khác biệt cốt lõi giữa thuật toán Lặp giá trị (Value Iteration) và Lặp chính sách (Policy Iteration) là gì?",
  "back": "Lặp giá trị cập nhật hàm V qua toán tử co Bellman cho đến khi hội tụ số học; Lặp chính sách luân phiên giữa Đánh giá chính sách (giải hệ phương trình tuyến tính) và Cải tiến chính sách (tham lam), luôn tìm ra chính sách tối ưu chính xác sau số bước hữu hạn.",
  "category": "Lập kế hoạch bất định",
  "lecture": "12-lap-ke-hoach-trong-dieu-kien-bat-dinh"
},
  {
    "id": "fc-artint-ch13-01",
    "front": "Điểm khác biệt cốt lõi giữa Học có giám sát (Supervised Learning) và Học tăng cường (Reinforcement Learning) là gì?",
    "back": "Học có giám sát nhận phản hồi chỉ dẫn (Instructive) từ nhãn đúng của giáo viên và dữ liệu tĩnh; Học tăng cường chỉ nhận phản hồi đánh giá (Evaluative) qua tín hiệu phần thưởng trễ hạn (Delayed Reward), và hành động của tác tử quyết định trực tiếp phân phối dữ liệu tương lai.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "13-hoc-tang-cuong",
    "tags": ["rl", "supervised-learning", "credit-assignment"]
  },
  {
    "id": "fc-artint-ch13-02",
    "front": "Phương trình cập nhật của Q-learning là gì và tại sao nó là một giải thuật Ngoài chính sách (Off-Policy)?",
    "back": "Q[s, a] <- Q[s, a] + alpha * (r + gamma * max_{a'} Q[s', a'] - Q[s, a]). Là Off-Policy vì mục tiêu sử dụng toán tử max_{a'} của chính sách tối ưu lý thuyết, hoàn toàn độc lập với chính sách hành vi thực tế (như epsilon-greedy) mà tác tử đang dùng để khám phá.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "13-hoc-tang-cuong",
    "tags": ["q-learning", "off-policy", "temporal-difference"]
  },
  {
    "id": "fc-artint-ch13-03",
    "front": "Tại sao trong bài toán Đi bộ bên bờ vực (Cliff Walking), SARSA lại đạt hiệu năng trực tuyến tốt hơn Q-learning khi có epsilon-greedy?",
    "back": "SARSA là On-Policy, cập nhật dựa trên hành động thực tế tiếp theo a', nên nó tính đến cả rủi ro rơi vực do các bước đi ngẫu nhiên epsilon và chọn đường vòng an toàn; Q-learning chọn đường men sát mép vực nên liên tục rơi vực trong quá trình học.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "13-hoc-tang-cuong",
    "tags": ["sarsa", "cliff-walking", "on-policy"]
  },
  {
    "id": "fc-artint-ch13-04",
    "front": "Kiến trúc Dyna-Q và thuật toán Quét ưu tiên (Prioritized Sweeping) giải quyết vấn đề gì trong học tăng cường?",
    "back": "Giải quyết sự lãng phí thời gian tính toán nhàn rỗi giữa các bước vật lý. Dyna-Q học mô hình thế giới P, R rồi chạy mô phỏng trong tâm trí; Prioritized Sweeping dùng hàng đợi ưu tiên theo sai số Bellman để lan truyền giá trị ngược nhanh chóng, tối đa hóa hiệu quả sử dụng mẫu (Sample Efficiency).",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "13-hoc-tang-cuong",
    "tags": ["dyna-q", "prioritized-sweeping", "model-based"]
  },
  {
    "id": "fc-artint-ch13-05",
    "front": "Hai giải pháp kiến trúc then chốt giúp Deep Q-Networks (DQN) ổn định quá trình huấn luyện mạng nơ-ron sâu là gì?",
    "back": "1. Bộ đệm tái hiện trải nghiệm (Experience Replay Buffer): Lấy mẫu ngẫu nhiên theo mini-batch để phá vỡ tương quan thời gian giữa các mẫu liên tiếp.\n2. Mạng mục tiêu độc lập (Target Network): Đóng băng trọng số w- để cố định mục tiêu TD, tránh hiện tượng mục tiêu dịch chuyển liên tục.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "13-hoc-tang-cuong",
    "tags": ["dqn", "experience-replay", "target-network", "deep-rl"]
  },
  {
    "id": "fc-artint-ch14-01",
    "front": "Sự khác biệt bản chất giữa Tự nhiên (Nature) và một Đối thủ chiến lược (Strategic Agent) trong thiết kế hệ thống AI là gì?",
    "back": "Tự nhiên là chủ thể vô tư lự, không có sở thích cá nhân, không có hàm độ thỏa dụng và hành động ngẫu nhiên theo quy luật vật lý (có thể mô hình hóa bằng MDP tĩnh). Đối thủ chiến lược sở hữu mục tiêu riêng, chủ động tối đa hóa lợi ích cá nhân, có khả năng dự đoán và thích nghi để khai thác điểm yếu của ta nếu ta coi họ là tĩnh.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "14-he-da-tac-tu",
    "tags": ["multiagent", "game-theory", "strategic-agent"]
  },
  {
    "id": "fc-artint-ch14-02",
    "front": "Ý nghĩa của hai tham số ngưỡng alpha và beta trong thuật toán Cắt tỉa Alpha-Beta là gì?",
    "back": "Alpha là giá trị tốt nhất (lớn nhất) mà người chơi MAX đã bảo đảm được dọc theo đường đi từ gốc; nhánh nút MIN nào trả về giá trị <= alpha sẽ bị cắt tỉa ngay (alpha-cutoff). Beta là giá trị tốt nhất (nhỏ nhất) mà người chơi MIN đã bảo đảm được; nhánh nút MAX nào trả về giá trị >= beta sẽ bị cắt tỉa ngay (beta-cutoff).",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "14-he-da-tac-tu",
    "tags": ["alpha-beta", "minimax", "game-tree"]
  },
  {
    "id": "fc-artint-ch14-03",
    "front": "Định nghĩa Cân bằng Nash (Nash Equilibrium) và phát biểu Định lý tồn tại của John Nash?",
    "back": "Cân bằng Nash là một hồ sơ chiến lược mà không có bất kỳ tác tử nào có động cơ đơn phương đi trệch khỏi chiến lược của mình (mỗi chiến lược là một phản ứng tốt nhất trước chiến lược của đối thủ). Định lý Nash (1950) chứng minh rằng mọi trò chơi hữu hạn luôn tồn tại ít nhất một Cân bằng Nash (trong không gian chiến lược thuần túy hoặc hỗn hợp).",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "14-he-da-tac-tu",
    "tags": ["nash-equilibrium", "game-theory", "best-response"]
  },
  {
    "id": "fc-artint-ch14-04",
    "front": "Khoản thuế Clarke trong Cơ chế VCG và nguyên lý Đấu giá giá thứ hai Vickrey vận hành như thế nào?",
    "back": "Thuế Clarke buộc mỗi tác tử phải trả khoản tiền bằng đúng mức thiệt hại ngoại tác mà sự tham gia của tác tử đó gây ra cho các thành viên còn lại trong xã hội, bảo đảm khai báo trung thực là chiến lược trội. Đấu giá Vickrey trao giải cho người trả giá cao nhất nhưng chỉ thu mức giá của người cao thứ hai, là trường hợp đặc biệt của VCG cho một món hàng.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "14-he-da-tac-tu",
    "tags": ["vcg", "mechanism-design", "vickrey-auction"]
  },
  {
    "id": "fc-artint-ch14-05",
    "front": "Định lý bất khả của Kenneth Arrow (1951) khẳng định điều gì về các cơ chế lựa chọn xã hội?",
    "back": "Với từ ba phương án trở lên, không tồn tại bất kỳ hàm lựa chọn xã hội nào thỏa mãn đồng thời cả 5 tiêu chí: 1. Đầy đủ và bắc cầu; 2. Miền xác định không hạn chế; 3. Hiệu quả Pareto; 4. Độc lập với các phương án không liên quan (IIA); và 5. Phi độc tài. Bất kỳ quy tắc bầu cử nào thỏa mãn 4 tiêu chí đầu đều là chế độ độc tài.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "14-he-da-tac-tu",
    "tags": ["arrow-theorem", "social-choice", "voting"]
  },
  {
    "id": "fc-artint-ch16-01",
    "front": "Mô hình biểu diễn bộ ba (Triples) trong đồ thị tri thức có cấu trúc và ưu điểm gì?",
    "back": "Mỗi sự kiện nguyên tử được biểu diễn bằng bộ ba <Chủ thể, Thuộc tính, Giá trị> (hay prop(Ind, Prop, Val)). Ưu điểm: Lược đồ mở không ràng buộc (schema-free), dễ dàng tích hợp các nguồn dữ liệu phân tán, có thể bổ sung thuộc tính mới mà không cần sửa bảng cấu trúc.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "16-do-thi-tri-thuc-va-ban-the-luan",
    "tags": [
      "knowledge-graph",
      "triples",
      "rdf"
    ]
  },
  {
    "id": "fc-artint-ch16-02",
    "front": "Kỹ thuật Hiện thực hóa quan hệ (Reification) giải quyết bài toán gì trong đồ thị tri thức?",
    "back": "Chuyển đổi một mối quan hệ n-ngôi, một sự kiện hoặc một phát biểu thành một cá thể độc lập trung gian. Kỹ thuật này cho phép gắn thêm các thuộc tính phụ (như thời gian, địa điểm, độ tin cậy, nguồn gốc) mà không làm bùng nổ số lượng vị từ trong cơ sở tri thức.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "16-do-thi-tri-thuc-va-ban-the-luan",
    "tags": [
      "reification",
      "knowledge-graph",
      "n-ary-relation"
    ]
  },
  {
    "id": "fc-artint-ch16-03",
    "front": "Sự khác biệt căn bản giữa TBox và ABox trong Logic Mô Tả (Description Logics) là gì?",
    "back": "TBox (Terminological Box) chứa các định nghĩa thuật ngữ, phân cấp lớp và tiên đề cấu trúc của bản thể luận (ổn định, thiết kế lúc đầu). ABox (Assertional Box) chứa các khẳng định dữ liệu thực tế về các cá thể cụ thể trong thế giới (biến động liên tục trong thời gian chạy).",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "16-do-thi-tri-thuc-va-ban-the-luan",
    "tags": [
      "description-logic",
      "tbox",
      "abox",
      "owl"
    ]
  },
  {
    "id": "fc-artint-ch16-04",
    "front": "Giả định thế giới mở (Open World Assumption - OWA) trong Semantic Web khác gì với CWA?",
    "back": "Dưới OWA, một sự kiện chưa được phát biểu thì được coi là chưa biết (unknown), không mặc định xem là sai. Điều này đối lập với CWA (Closed World Assumption) trong cơ sở dữ liệu quan hệ và Prolog vốn suy diễn cái gì không tìm thấy thì là sai.",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "16-do-thi-tri-thuc-va-ban-the-luan",
    "tags": [
      "open-world-assumption",
      "semantic-web",
      "owl"
    ]
  },
  {
    "id": "fc-artint-ch16-05",
    "front": "Bốn nguyên tắc của chuẩn dữ liệu khoa học FAIR bao gồm những gì?",
    "back": "1. Findable (Dễ tìm kiếm qua định danh bền vững PID/IRI); 2. Accessible (Dễ truy cập qua giao thức chuẩn mở); 3. Interoperable (Tương tác được qua bản thể luận hình thức); 4. Reusable (Tái sử dụng được với siêu dữ liệu xuất xứ và giấy phép mở).",
    "category": "ai-nen-tang-tac-tu",
    "lecture": "16-do-thi-tri-thuc-va-ban-the-luan",
    "tags": [
      "fair-data",
      "provenance",
      "social-impact"
    ]
  }
]
