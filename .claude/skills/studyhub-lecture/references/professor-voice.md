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

Khi người học gặp nhiều thuật ngữ mới trong một đoạn, đừng kéo hết định nghĩa dài vào giữa lập luận và cũng đừng để từ lạ tự trôi qua. Giữ trong câu phần nghĩa cần cho bước hiện tại; thêm mục Wiki với định nghĩa ngắn và ví dụ để ghi chú nhanh mở được tại chỗ. Tránh câu meta chỉ có ích cho người soạn như “tuyến nội dung”, “theo yêu cầu của bạn”, “implementation này”; gọi thẳng phần học, nguồn hoặc phần cài đặt mà sinh viên đang đọc.

## Không viết bằng nhãn rút gọn

Một lỗi lặp lại của văn bản do AI soạn là bỏ bớt động từ, quan hệ và đối tượng, rồi ghép vài danh từ thành một nhãn có vẻ gọn: “Chọn gì, chấm gì, giới hạn đâu?”, “Từ dự đoán đến vector”, “Chuẩn dùng để chấm sai số”. Cách viết này buộc người mới tự khôi phục phần bị lược và tạo cảm giác như bản dịch tiêu đề quảng cáo.

- Tiêu đề mặc định gọi đúng nội dung: “Các thành phần của một bài toán tối ưu”, “Viết nhiều dự đoán bằng một phép nhân ma trận”.
- Chỉ dùng tiêu đề câu hỏi khi đó là câu hỏi người học thật sự cần trả lời và phần ngay sau trả lời nó. Không biến mọi mục thành câu hỏi.
- Không lặp cùng khuôn “Từ A đến B”, “Vì sao A?”, “A dùng để B” qua nhiều mục. Đọc riêng danh sách tiêu đề để phát hiện nhịp máy móc.
- Trong văn xuôi, giữ “vì”, “nếu”, “khi”, chủ thể và động từ. Một câu ngắn không được đánh đổi lấy quan hệ logic bị thiếu.

Đừng dùng “kiểm” như bản dịch mặc định của *check*. Chọn động từ theo hành động thật: “xác định kích thước”, “đối chiếu hai vế”, “xác minh điều kiện KKT”, “chứng minh tính lồi”, “thử một trường hợp”. “Kiểm tra” vẫn dùng được khi đúng nghĩa, nhưng “kiểm kích thước”, “kiểm dạng chuẩn” thường là câu cụt và không tự nhiên.

Đoạn hướng dẫn đọc bài phải là văn xuôi hoàn chỉnh. Tránh nhãn “Cách học:” theo sau bởi chuỗi mệnh lệnh rút gọn. Nói rõ phần nào là mạch chính, phần nào có thể để lại và lý do. Sau dấu hai chấm, viết hoa nếu phần sau là một câu độc lập; tốt hơn nữa, tách thành câu mới khi nhãn không cần thiết.

## Những khuôn đã thấy trong bài trên site

Rà riêng các khuôn sau khi biên tập Notes; chi tiết và cách sửa ở [lecture-blueprint.md](lecture-blueprint.md) mục 4:

- Đoạn trích mở đầu gán cho một nhà khoa học mà không có nguồn câu nói. Bịa trích dẫn là lỗi nội dung, không phải lỗi giọng.
- Nhãn hứa hẹn chiều sâu (“Bản chất”, “Tinh hoa”, “Trực giác then chốt”) đặt trước một câu khái quát. Thay bằng câu hỏi cụ thể và câu trả lời.
- Khẳng định tần suất không có dữ liệu (“bẫy cực kỳ phổ biến”, “sinh viên hay nhầm”). Dùng “một cách hiểu dễ nhầm là…” và cho ví dụ.
- Đánh giá thay giải thích (“cực kỳ hữu ích”, “đây chính là”, “vô cùng quan trọng”). Nói tác dụng cụ thể.
- In đậm dày đặc. In đậm tên khái niệm khi định nghĩa và điều kiện quyết định; phần còn lại để câu tự mang trọng tâm.

`scripts/review_teaching_text.py` chỉ ra vị trí các khuôn này để xem lại. Giữ nguyên khi đó là trích dẫn có nguồn hoặc khi từ được dùng đúng nghĩa chuyên môn (“bản chất” trong một luận đề triết học đang phân tích).

## Bốn dấu hiệu văn máy mà người học nhận ra

Người dùng của site đã chỉ ra bốn đặc điểm làm lời giảng đọc như văn máy. Mỗi dấu hiệu dưới đây kèm một ví dụ đã gặp khi soạn Lecture 01 của môn Cơ sở toán cho AI và cách sửa.

1. **Từ ngữ không ai dùng trong ngữ cảnh đó.** "Hãy cùng bước vào hành trình…", "một kỹ thuật kiểm tra rất mạnh", "đóng vai trò then chốt". Sửa bằng việc cụ thể mà khái niệm làm được: "kỹ thuật hạn chế lên một đường thẳng biến một câu hỏi nhiều chiều thành nhiều câu hỏi một chiều".
2. **Khuôn câu và khuôn câu hỏi lặp lại.** Mười bốn câu hỏi đào sâu trong một chương cùng mở bằng "Một bạn nói: … Bạn ấy đúng không?", trang nào cũng mở bằng "Trang này…", và "Đây chính là…" ở rất nhiều đoạn. Sửa theo nội dung của từng câu: "Khẳng định … nghe hợp lý. Hãy tìm một phản ví dụ.", "Để biết y có thuộc K* không, chỉ thử vài vector có đủ không?", "Điều gì xảy ra nếu bỏ giả thiết…?". Với "Đây chính là…", nói thẳng quan hệ: "Ta vừa tìm lại điều kiện nhân tử Lagrange, lần này chỉ bằng hình học."
3. **Rút ngắn thay vì giải thích.** "Tập lồi. Hàm lồi. Cực tiểu cục bộ. Toàn cục." là ghi chép của người đã hiểu. Người học cần câu có quan hệ: "Vì miền khả thi lồi và hàm mục tiêu lồi, mọi cực tiểu cục bộ đều là cực tiểu toàn cục." Mũi tên "→" trong lời giảng cũng là một dạng rút gọn như vậy.
4. **Dấu chấm phẩy thay cho từ nối.** "cho f = 1/4; phân phối thứ hai có…" sửa thành "cho f = 1/4, còn phân phối thứ hai có…". Tiếng Việt có rất nhiều từ nối (vì, nên, nhưng, còn, khi đó, chẳng hạn, ngược lại, nhờ đó). Một đoạn năm câu không có từ nối nào thường là danh sách khẳng định, chưa phải lời giải thích.

`review_teaching_text.py` đánh dấu các vị trí tương ứng bằng `AI_LEXICON`, `EVALUATIVE_PHRASE`, `QUESTION_TEMPLATE`, `REPEATED_OPENER`, `CHOPPY_RUN`, `ARROW_IN_PROSE`, `PROSE_SEMICOLON` và `LOW_CONNECTIVES`. Truyền cả chương một lượt, vì khuôn lặp giữa các trang không thấy được khi rà từng trang. Mục tiêu là lời giải thích tốt hơn, không phải né công cụ: đừng thay một khuôn bằng một khuôn mới, đừng đổi sang từ hiếm hay câu vụn để "giống người".
