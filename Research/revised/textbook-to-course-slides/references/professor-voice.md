# Lời giảng, chữ trên slide và note tự học

Đọc trước khi soạn tiếng Việt. Đây là hướng dẫn biên tập theo ngữ cảnh lớp học, không phải bộ phát hiện tác giả AI. Các ví dụ là do người soạn tạo, không phải trích dẫn giáo trình.

## Chọn giọng theo người đọc

| Đầu ra | Cách viết | Điều phải tránh |
| --- | --- | --- |
| Lời giảng / giải thích trong chat | Nói với người đang học; dẫn bằng câu hỏi thật, giải thích tại đúng chỗ họ có thể vướng | Giọng đọc bài báo; giả vờ có kinh nghiệm cá nhân hoặc đã quan sát lớp học |
| Chữ trên slide | Tiêu đề có nội dung, phát biểu chính xác, ký hiệu và nhãn rõ; đủ điều kiện ngay cạnh kết luận | Chép toàn bộ lời nói lên màn hình; rút lời giải thành chuỗi danh từ |
| Note tự học | Văn xuôi đọc độc lập, phát biểu hình thức rồi giải thích; đủ các bước quyết định, ví dụ và liên kết | Dùng “ở đây”, “hình bên này”, “như vừa nói” khi không có địa chỉ cụ thể |
| Ghi chú giảng viên | Lời có thể nói, chỗ chỉ lên hình/bảng, khoảng dừng và phản hồi cho đáp án dự kiến | Chỉ ghi “giải thích trực giác”; giấu lý do thiết yếu trong note riêng |

Không chuyển mọi định nghĩa thành khẩu ngữ. Phát biểu toán học có thể rất gọn và hình thức. Câu theo sau nó mới có nhiệm vụ đưa người học vào lập luận. Giọng “giáo sư” ở đây là hành vi giải thích có trách nhiệm, không phải nhân vật giả có học hàm, tiểu sử hoặc quyền uy.

## Một câu mang một bước chính

Đặt động từ và đối tượng trước các nhãn trừu tượng. Một câu có thể chứa điều kiện và hệ quả, nhưng khi đổi nhiệm vụ tư duy thì nên tách. Đừng ghép lập mô hình, tìm hướng cập nhật và quy ước dấu trong một câu.

| Câu cần sửa trong lời giảng | Cách nói thường hợp hơn | Nghĩa phải kiểm tra |
| --- | --- | --- |
| “gradient tại điểm hiện hành” | “gradient tại \(x_k\)”, “gradient ở bước hiện tại” | \(x_k\) đã được giới thiệu chưa? |
| “chứng minh và vị trí dùng giả thiết” | “Giả thiết này được dùng ở bước nào?” | Bài phải chỉ ra đúng bước, không chỉ đổi nhãn |
| “tiến hành áp dụng định lý” | “áp dụng định lý” | Đã đủ giả thiết của định lý chưa? |
| “thực hiện việc biến đổi biểu thức” | “biến đổi biểu thức” | Phép biến đổi có bảo toàn tương đương không? |
| “tạo bước đi” | “chọn hướng cập nhật” hoặc “tính bước cập nhật” | Hướng, độ dài bước và độ dời là ba đối tượng khác nhau |
| “\(\nu\) tự do dấu” | “\(\nu\) không bị giới hạn dấu” | Chỉ nói trong quy ước ràng buộc đang dùng |
| “điều này đóng vai trò then chốt” | Nêu tác dụng cụ thể: “Bước này giúp ta so sánh với mọi \(y\).” | Có thật là so với mọi điểm trong miền không? |

Các cụm trên là dấu hiệu cần xem lại khi AI tự viết lời giảng. Giữ nguyên nếu đang trích nguồn để phân tích, hoặc nếu môn học có thuật ngữ đã thống nhất. Không thay thuật ngữ đúng bằng từ dễ nghe nhưng sai nghĩa.

Với nguồn EN, đọc [translation-vi.md](translation-vi.md) để phân biệt sai nghĩa thuật ngữ với câu chỉ gượng. “Điểm khả thi” có thể giữ và giải thích; contraction mapping dùng “ánh xạ co” theo ngữ cảnh. Khi diễn giải “không bị giới hạn dấu”, nói “âm, bằng 0 hoặc dương” nếu đang mô tả đầy đủ miền dấu. Không dùng nhãn nội bộ gượng như “hợp đồng nội dung” trong lời dạy.

## Phải giữ câu hỏi mà người học cần được trả lời

Bản yếu: “Gradient bằng 0, kết hợp với tính lồi, đảm bảo tối ưu toàn cục.”

Lời giảng tốt hơn cho bài toán không ràng buộc trên \(\mathbb R^n\), với \(f\) khả vi và lồi:

> Gradient bằng 0 thì đã đủ chưa? Với một hàm bất kỳ, chưa đủ. Ta cần tính lồi ở bước sau: với mọi \(y\),
> \[
> f(y)\ge f(x^\star)+\nabla f(x^\star)^T(y-x^\star).
> \]
> Vì \(\nabla f(x^\star)=0\), vế phải còn \(f(x^\star)\). Vậy không có điểm \(y\) nào cho giá trị nhỏ hơn. Chính bất đẳng thức này là chỗ ta dùng tính lồi.

Note tự học cho cùng ý:

> Giả sử \(f:\mathbb R^n\to\mathbb R\) khả vi và lồi. Bất đẳng thức bậc nhất của hàm lồi cho \(f(y)\ge f(x^\star)+\nabla f(x^\star)^T(y-x^\star)\) với mọi \(y\). Nếu \(\nabla f(x^\star)=0\), ta được \(f(y)\ge f(x^\star)\). Vì vậy \(x^\star\) là điểm cực tiểu toàn cục. Tính lồi được dùng để có bất đẳng thức bậc nhất; điều kiện điểm dừng được dùng để triệt tiêu số hạng tuyến tính.

Chữ trên slide có thể giữ giả thiết, bất đẳng thức và hai chú giải tại đúng số hạng. Phần hỏi–đáp có thể nằm trong lời giảng. Note vẫn phải chứa lập luận đầy đủ nếu sinh viên học độc lập.

Nếu bỏ tính lồi, \(f(x)=-x^2\) có \(f'(0)=0\) nhưng \(0\) là cực đại. Phản ví dụ chỉ cho thấy điều kiện điểm dừng chưa đủ; nó không nói rằng mọi điểm dừng của hàm không lồi đều là cực đại.

## Câu ngắn chỉ có ích khi nó làm việc

“Chỗ này dễ nhầm”, “Tại sao lại thế?”, “Đến bước này mới cần tính lồi” được phép khi ngay sau đó có chỗ nhầm, câu trả lời hoặc bước cụ thể. Không rải “khoan”, “hãy tưởng tượng”, “các bạn thấy không” vào mọi đoạn để diễn giọng người. Không ghi ngộ nhận là phổ biến nếu chưa có dữ liệu; có thể nói “Một cách suy ra dễ nhầm là…”.

Đổi nhịp theo chức năng: một câu ngắn nêu vướng mắc, vài câu giải thích, một công thức khi cần, rồi trở lại ý nghĩa. Không bắt mỗi đoạn có câu hỏi tu từ và câu tổng kết tròn trịa.

## Lượt sửa riêng cho ngôn ngữ

Trước khi sửa, ghi những phần phải giữ: điều kiện, miền, phủ định, lượng từ, kết luận, ký hiệu và nguồn. Sau đó:

1. Chỉ ra câu đang khó học vì thiếu đối tượng, quan hệ, bước nối hay sai giọng.
2. Khôi phục bước thiếu; dùng động từ hoặc ký hiệu đã biết để gọi đúng đối tượng.
3. Tách câu khi nó đổi việc: từ chứng minh sang chọn bước, từ tính toán sang quy ước.
4. Xóa cầu nối có thể dán vào bất kỳ bài nào. Cầu nối thật phải nhắc việc vừa biết và câu hỏi sắp giải quyết.
5. Đọc liền mạch trong đúng giọng đã chọn; đối chiếu lại các phần phải giữ.

Với một cụm bài, kiểm tra mật độ khuôn như “ta có thể thấy rằng”, “điều quan trọng ở đây”, “trực giác đằng sau”, “một cách tự nhiên”. Sửa khi chúng lặp hoặc che lý do, không thay chúng bằng một bộ từ đồng nghĩa khác. Không đặt điểm phần trăm “giống giáo sư”.
