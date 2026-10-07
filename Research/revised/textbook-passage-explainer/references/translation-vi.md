# Diễn đạt kiến thức tiếng Anh bằng tiếng Việt chuyên ngành

Đọc khi nguồn có thuật ngữ tiếng Anh hoặc đang sửa bản dịch. Mục tiêu là diễn đạt cùng ý trong ngôn ngữ một giảng viên của môn dùng, giữ nghĩa toán/khoa học; không bảo toàn thứ tự từ tiếng Anh.

## Ba việc khác nhau

1. Hiểu phát biểu: đối tượng, quan hệ, điều kiện, miền, lượng từ, dấu, đơn vị và mức chắc chắn.
2. Chọn thuật ngữ theo khái niệm và môn học. Một từ có thể có nhiều nghĩa; tra cả cụm và định nghĩa thay vì lấy nghĩa phổ biến nhất của từng từ.
3. Viết câu đúng giọng đầu ra theo [professor-voice.md](professor-voice.md), rồi so nghĩa lại với nguồn.

“Khả thi” là thuật ngữ có thể giữ trong tối ưu. Không loại nó chỉ vì nghe hành chính trong đời thường. “Hợp đồng” có thể đúng trong ngữ cảnh thỏa thuận, nhưng không thay cho contraction mapping trong giải tích. Nhãn nội bộ của công cụ cũng phải rõ: dùng “kế hoạch giảng” hoặc “yêu cầu cho phần nội dung”; không đưa nhãn `teaching_contract` của bản cũ vào lời giảng.

## Chọn thuật ngữ có căn cứ

Ưu tiên yêu cầu của người dùng và glossary của khóa học, rồi cách gọi trong giáo trình tiếng Việt cùng môn. Nếu hai giáo trình dùng hai tên, giữ tên đã thống nhất và giải thích biến thể ở lần đầu khi cần. Không gọi một cách dịch là chuẩn duy nhất từ một kết quả tìm kiếm.

[terminology-memory.json](terminology-memory.json) chứa khái niệm, lĩnh vực, cách gọi được chọn, biến thể, lời giảng mẫu, nghĩa phải giữ và nguồn. `evidence.vi_usage` phân biệt cách gọi đã thấy trong nguồn tiếng Việt với lựa chọn biên tập của dự án. Nguồn giải thích khái niệm bằng tiếng Anh không chứng minh cách gọi tiếng Việt đã phổ biến.

Chỉ lấy các mục phù hợp đoạn đang giảng. `scripts/retrieve_terminology.py` tìm cụm theo lĩnh vực và lấy ví dụ cùng loại; đây là tra cứu văn bản cục bộ, không phải hệ tìm kiếm ngữ nghĩa hay model hiểu sách. Không có lĩnh vực và một từ có nhiều nghĩa thì script trả các nghĩa với trạng thái cần xác định, không tự chọn. Không có Python thì đọc mục liên quan trong JSON. Không tìm thấy mục không có nghĩa thuật ngữ đã được kiểm chứng.

Nếu chưa có tên Việt chắc chắn, dùng tên gốc kèm diễn giải rõ, hoặc hỏi đúng ngữ cảnh bị thiếu khi nó quyết định kết quả. Với từ “contraction” đứng riêng, phân biệt ánh xạ co trong lý thuyết điểm bất động với phép co tensor. Không mở một bản tra thuật ngữ không liên quan để lấp khoảng trống.

## Những nghĩa dễ mất khi sửa cho tự nhiên

| Cụm | Cách viết trong lớp | Điều phải giữ |
| --- | --- | --- |
| `contraction mapping` | “ánh xạ co”, hoặc “ánh xạ co chặt” theo giáo trình | Có cùng một hệ số q < 1 cho mọi cặp điểm; trong định nghĩa dùng 0 ≤ q < 1. “Khoảng cách nhỏ hơn” đơn thuần chưa thay được bất đẳng thức này. |
| `tensor contraction` | “phép co tensor” | Phép cộng theo cặp chỉ số phù hợp, không phải tính chất co khoảng cách. Trong ký hiệu tensor hình học, ghép một chỉ số trên với một chỉ số dưới; nếu ghép cùng loại, cần metric/cấu trúc đã cho. |
| `current iterate` | “điểm x_k”, “điểm lặp hiện tại” | x_k là điểm/giá trị, k là chỉ số bước. Không gọi k là điểm. |
| `feasible point` | “điểm khả thi”; “x thỏa mọi ràng buộc” để giải thích | Thỏa mọi ràng buộc trong miền; khả thi chưa có nghĩa tối ưu. |
| `stationarity condition` | “điều kiện dừng” | Điều kiện phụ thuộc bài toán: có thể là ∇f = 0 hay gradient của L; không tự coi đủ tối ưu. |
| `descent direction` | “hướng giảm” và giải thích tại điểm đang xét | Với f khả vi, ∇f(x)^T d < 0 cho giảm khi bước dương đủ nhỏ; không bảo đảm mọi bước dương đều giảm. |
| `free in sign` | “không bị giới hạn dấu”; “có thể âm, bằng 0 hoặc dương” | Bao gồm 0. Không chuyển thành “phải khác 0” hoặc “âm hay dương” như mô tả miền đầy đủ. |
| `active constraint` | “ràng buộc chặt tại x” hoặc tên đã chọn trong môn | Với g_i(x) ≤ 0, chặt tại x nghĩa là g_i(x) = 0. Không có nghĩa mọi ràng buộc đều chặt hay nhân tử luôn khác 0. |
| `free variable` | “biến tự do”, giải thích theo bài | Không đồng nhất miền không giới hạn dấu với biến tự do trong mọi môn; không dịch free thành miễn phí. |

Các bản dịch thường gặp được chọn cho gói này, không phải blacklist toàn tiếng Việt. Với active constraint, cách gọi phụ thuộc giáo trình; nếu gặp “ràng buộc tích cực”, kiểm tra định nghĩa và nguồn trước khi sửa. Không biến một sở thích về giọng thành khẳng định cả cộng đồng không dùng từ đó.

## Soạn rồi kiểm tra theo hai lượt

Lượt ngôn ngữ chỉ sửa câu gượng, danh từ hóa, đối tượng không rõ và khuôn lặp. Giữ riêng danh sách nghĩa phải bảo vệ; không thêm định lý, thuật toán hoặc điều kiện mới để câu nghe xuôi.

Lượt kiểm tra nghĩa so từng phát biểu nguồn với bản Việt: có mất phủ định, “mọi”, “tồn tại”, “có thể”, “nếu”, chiều suy ra, dấu, miền hay đối tượng không? Kiểm tra ví dụ số và công thức độc lập khi cần. Nếu câu cần chia, giữ quan hệ giữa các câu. Tính dừng của bài toán con không tự tạo hướng cập nhật của bài toán chính; thiếu ngữ cảnh thì nói rõ thiếu.

Không dùng dịch ngược như bằng chứng duy nhất: hai model có thể lặp cùng lỗi. Giữ một ghi nhận ngắn ở nơi có rủi ro, chẳng hạn “free in sign gồm 0; active là đẳng thức tại điểm đang xét”. Không công bố toàn bộ suy nghĩ nội bộ.

Kiểm tra cả giả định của ví dụ mới. Với phép co tensor, đừng lấy tổng A_ii của một tensor hai chỉ số dưới bất kỳ rồi gọi đó là phép co độc lập cơ sở. Một ví dụ trace gọn có thể dùng tensor A^i_j biểu diễn ánh xạ tuyến tính, co thành tổng A^i_i. Phân biệt tensor hình học với mảng số trong thư viện; nói rõ quy ước đang dùng mà không giảng thêm cả chương. Xem nguồn khái niệm ở [terminology-research.md](terminology-research.md).

## Ví dụ cùng nghĩa, khác giọng

Nguồn tự viết: “A point x is feasible if it satisfies all constraints.”

- Câu kỹ thuật: “Ta gọi x là điểm khả thi nếu x thỏa mọi ràng buộc.”
- Lời giảng: “Trước hết kiểm tra x có thỏa mọi ràng buộc không. Nếu thỏa, x là một điểm khả thi. Việc đó chưa cho biết x có tối ưu hay không.”

Nguồn tự viết: “The multiplier of an equality constraint is free in sign.”

- Câu kỹ thuật: “Nhân tử của ràng buộc đẳng thức không bị giới hạn dấu.”
- Lời giảng: “Với ràng buộc đẳng thức, ν có thể âm, bằng 0 hoặc dương. Ta không đặt điều kiện ν ≥ 0 chỉ vì ν là một nhân tử.”

Phần giải thích thêm phải được nhận diện đúng. Không gán câu “chưa tối ưu” hoặc ví dụ bổ sung cho tác giả nếu họ không viết. Chọn vài ví dụ gần loại nhiệm vụ, không chép toàn bộ kho vào prompt.

Ví dụ và dữ liệu để nghiên cứu huấn luyện: đọc [training-and-evaluation.md](training-and-evaluation.md) khi cần mở rộng dữ liệu hoặc đánh giá phiên bản; không cần huấn luyện model để dùng bước tra cứu và kiểm tra này.
