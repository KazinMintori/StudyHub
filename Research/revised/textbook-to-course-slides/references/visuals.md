# Thiết kế slide học: hình phải làm công việc trí tuệ

Đọc trước khi chọn hệ thẩm mỹ, bố cục, hình vẽ và dựng sản phẩm. Các kích thước là điểm khởi đầu cần kiểm tra trên bản render, không phải luật thay thế việc nhìn.

## 1. Khóa hướng thiết kế từ tham chiếu phù hợp

Ưu tiên mẫu người dùng, hình trong giáo trình, slide học tốt của cùng môn hoặc một tham chiếu học thuật phù hợp. Khi cần tìm thêm, chọn hình có nhiệm vụ giống bài đang dạy, thay vì mẫu quảng cáo đẹp nhưng khác chức năng.

Ghi ngắn: điều giữ từ tham chiếu, điều điều chỉnh, điều không phù hợp lớp học. Quan sát cách đặt nhãn, phân cấp, mật độ, quan hệ chữ–hình và độ chính xác; không chỉ lấy màu.

Nếu không có tham chiếu, dùng hệ mặc định bên dưới và kiểm tra bằng một cụm giảng khó. Không dừng công việc chỉ để tìm một phong cách riêng.

## 2. Xác định cấu trúc thông tin trước layout

Một slide cần một điểm bắt đầu, một đường đọc và một điều người học nhận ra sau khi đọc. Điểm nổi nhất có thể là hình, công thức, câu hỏi hoặc chứng cứ văn bản.

Chọn bố cục từ mối quan hệ:

| Nhiệm vụ | Cấu trúc thích hợp | Cần thấy rõ |
| --- | --- | --- |
| Định nghĩa | Phát biểu cùng một trường hợp cụ thể | Đối tượng, điều kiện và ví dụ |
| So sánh | Hai vùng đối chiếu trên cùng tiêu chí | Khác biệt có thể kiểm tra |
| Cơ chế | Các trạng thái có quan hệ nhân quả | Điều đổi, điều giữ và hướng biến đổi |
| Đọc đồ thị | Hình lớn và chú giải đặt gần phần cần đọc | Trục, đơn vị, quan sát chính |
| Chứng minh | Lập luận theo dòng, chú thích lý do | Tiền đề và bước quyết định |
| Ví dụ làm mẫu | Dữ kiện, các bước, kết quả và hình liên quan | Thao tác cùng lý do chọn |
| Văn bản | Trích đoạn đọc được và chú giải chính xác | Chi tiết làm chứng cứ cho cách đọc |
| Lịch sử | Dòng thời gian hoặc các nguồn đối chiếu | Thứ tự sự kiện và tình trạng nguồn |
| Kiểm tra hiểu | Câu hỏi và vật liệu đủ để trả lời | Nhiệm vụ cùng dữ kiện, chưa lộ đáp án |

Không biến bảng này thành bộ template đóng. Cùng một nhiệm vụ có thể cần các bố cục khác nhau theo hình nguồn và độ khó.

## 3. Hệ màu đa dạng nhưng có nghĩa

Chọn một nền chính, chữ, chữ phụ và các màu phân biệt đối tượng. Khóa các vai trò trong bài. Có thể đổi sắc độ theo chương khi không làm thay ý nghĩa của các đối tượng đã học.

Các bảng màu khởi đầu:

| Vai trò | Giấy sáng | Phân tích nền lạnh | Nền tối |
| --- | --- | --- | --- |
| Nền | #F7F5EF | #F3F6FB | #10232A |
| Chữ chính | #17212B | #14283D | #F2F5EF |
| Chữ phụ | #4C5966 | #4E6073 | #B9C9CC |
| Đối tượng A | #2458A6 | #215EAB | #98BEFF |
| Đối tượng B | #007C78 | #006D70 | #70D4CC |
| Đối tượng C | #7B3F86 | #733E89 | #D5B4EE |
| Trọng tâm / điều kiện | #9A4C11 | #925015 | #F0C66E |
| Lỗi / cảnh báo | #B13B35 | #A9393A | #F69A8C |

Các màu này dùng trên nền tương ứng; phải kiểm tra lại khi có lớp phủ, nền ảnh, fill hoặc opacity. Không dùng màu chữ trên nền cùng màu chỉ vì hợp bảng màu.

Mỗi màu cần vai trò cụ thể. Chẳng hạn P(A ∩ B) luôn đi cùng một màu và một nhãn trong cụm xác suất. Nếu dùng màu đỏ cho lỗi, tránh dùng đỏ tùy hứng cho một đối tượng đúng ngay trang sau.

Đa dạng có thể đến từ hình so sánh, các lớp trạng thái, bảng có phân cấp, nền chuyển đoạn và tỉ lệ chữ–hình. Không cần tăng số màu trên mỗi slide. Dùng nhiều màu khi hình có nhiều nhóm thật; giảm hoặc tách nhóm nếu không còn phân biệt được.

Chữ nội dung nên đạt tương phản 4,5:1, chữ lớn tối thiểu 3:1; đường và vùng đồ họa thiết yếu nên đạt 3:1 với nền kề. Đây là ngưỡng thiết kế tham khảo từ WCAG, không phải chứng nhận slide / PDF đã đáp ứng toàn bộ WCAG. Chiếu trong lớp có thể cần tương phản cao hơn.

Thêm nhãn, hình dạng, kiểu nét hoặc vị trí để không chỉ dựa vào màu. Xem bản thang xám cho các hình trọng tâm.

Nhãn gán một đại lượng hình học cho cạnh, khoảng, hướng hoặc miền phải chỉ đúng vào đại lượng đó. Với độ dài cạnh, đặt đường đo hoặc dấu ngoặc dọc theo cạnh hoặc song song với nó; cho đầu đường gióng chạm đúng hai đầu mút nếu chúng biểu diễn độ dài. Một mũi tên kết thúc ở giữa vùng tô không chỉ rõ cạnh của vùng. Trên hình đã render, lần theo đường gióng từ nhãn đến đối tượng và kiểm tra xem người học có thể gán nhầm cho cạnh khác hay không.

## 4. Chữ và bố cục

Với canvas khoảng 13,33 × 7,5 inch:

- Tiêu đề thường 30–38 pt; phần giới thiệu lớn có thể hơn.
- Chữ chính thường 22–28 pt; chữ 20 pt chỉ dùng khi vẫn đọc tốt trong điều kiện thực.
- Nhãn hình thường 16–20 pt. Nhãn mà người học cần đọc để làm bài phải đủ lớn như nội dung chính.
- Chú thích nguồn phụ có thể nhỏ hơn, nhưng không giấu giả thiết hoặc dữ kiện cần học trong chữ nhỏ.
- Giữ lề khoảng 0,5–0,7 inch và khoảng cách đủ để nhìn rõ nhóm.

Không thu nhỏ chữ vì một template cố định. Tách theo một bước giảng, mở rộng hình, hoặc chuyển chi tiết phù hợp sang tài liệu học.

Ưu tiên font có đủ dấu tiếng Việt, như IBM Plex Sans, Source Sans 3 hoặc Noto Sans; serif phù hợp cho đoạn văn, chuyển mục hoặc giọng học thuật. Toán dùng font và renderer toán. Kiểm tra font thực có trong môi trường, không chỉ khai báo tên.

Ngắt dòng theo đơn vị nghĩa. Tránh một từ cuối cô lập, dấu thanh bị cắt, công thức vỡ qua dòng hoặc chữ dính nhãn hình. Đừng in đậm toàn bộ đoạn; dùng weight để chỉ điều cần chú ý.

Khoảng trống được phép tạo tập trung, nhóm và nhịp nghỉ. Không có tỉ lệ lấp đầy bắt buộc. Nếu hình chính quá nhỏ hoặc các nhóm nằm rời rạc, sửa cân đối; nếu một công thức lớn đủ làm nhiệm vụ, không thêm chữ để “đỡ trống”.

## 5. Hình nào cần được vẽ?

Trước khi tạo một hình, ghi:

~~~text
Mục đích: người học cần nhận ra điều gì?
Đối tượng: những vật / biến / chứng cứ nào phải thấy?
Mã hóa: vị trí, độ dài, diện tích, màu hay kiểu nét mang nghĩa gì?
Điều giữ nguyên: dữ liệu, thang đo, tọa độ hoặc trạng thái nào?
Điều được biến đổi: phép biến đổi nào đang học?
Nguồn: hình gốc, dữ liệu thật, dữ liệu giả định hay sơ đồ bổ sung?
Kiểm tra: quan sát nào xác nhận hình nói đúng?
~~~

Đừng chỉ viết “một sơ đồ trực quan về chủ đề”. Nếu không thể nêu hình giúp hiểu điều gì, bỏ hoặc thiết kế lại.

Các phép thử:

- Nếu nói “cùng kích thước nhưng khác cấu trúc”, cho thấy hai đối tượng cùng kích thước.
- Nếu nói “mẫu số thay đổi”, cho thấy nhóm được xét trước và sau.
- Nếu nói “một bước làm sai kết quả”, đánh dấu đúng bước sai và hệ quả.
- Nếu nói “chi tiết này hỗ trợ một cách đọc”, đặt đúng đoạn văn và chỉ ra chi tiết ấy.

## 6. Hình nguồn và bản vẽ lại

Kiểm kê mọi hình / bảng có ý nghĩa trong phạm vi, cùng số trang PDF và số trang in nếu khác nhau. Ghi ID, mục đích, nơi dùng, cách trích và việc dịch nhãn.

Ưu tiên vector hoặc ảnh gốc; crop trang là phương án sau. DPI không tự bảo đảm đọc được: kiểm tra độ phân giải tại kích thước hiển thị cuối.

Giữ toàn bộ hình khi cần quan hệ giữa các phần. Khi phóng một bảng nhỏ, giữ vị trí của nó trong hình tổng thể và chỉ dẫn; không cắt trục hoặc legend để làm hình trông sạch.

Một bản vẽ lại có thể làm nhãn rõ hơn, dịch chữ hoặc tách trạng thái. Phải:

1. Liên kết tới hình nguồn và lưu bản gốc trong hồ sơ khi có thể.
2. Giữ dữ liệu, hình học và những phân biệt có ý nghĩa.
3. Kiểm tra đối chiếu, ghi thay đổi.
4. Ghi rõ khi chỉ là sơ đồ hóa, chẳng hạn “Sơ đồ, không theo tỉ lệ”.

Nếu cần hình gốc để hiểu tác giả hoặc chứng cứ, đưa nó vào tuyến chính. Nếu chỉ cần tra cứu, danh mục hình nguồn / phụ lục có thể phù hợp. Ghi lý do; đừng lược bỏ vì AI vẽ được một hình đẹp hơn.

## 7. Đồ thị và sơ đồ kỹ thuật

- Dữ liệu, hàm số và tọa độ phải xác định được, kể cả hình minh họa.
- Trục cần tên và đơn vị; nêu thang log, chuẩn hóa, cắt trục khi có.
- Dùng cùng thang và phạm vi cho so sánh nếu mục tiêu là so sánh trực tiếp. Nếu phải khác, nói rõ.
- Mũi tên nhân quả khác với mũi tên chỉ luồng xử lý; dùng nhãn hoặc quy ước rõ.
- Độ dày, diện tích, góc và kích thước không được vô tình tạo quan hệ định lượng sai.
- Giữ nhãn sát đối tượng; tránh yêu cầu mắt chạy qua lại giữa nhiều legend.
- Dùng công cụ vector, plot hoặc primitive native để kiểm soát hình; không giao hình có công thức / số liệu chính xác cho tạo ảnh tự do.

Với hình chồng lớp, kiểm tra occlusion và đường biên. Với hình 3D, kiểm tra phối cảnh không che quan hệ đang dạy. Không dùng 3D chỉ vì trông sinh động.

## 8. Công thức và ký hiệu

Chép từ nguồn và đối chiếu từng ký hiệu; kiểm tra riêng giả thiết, dấu âm, mũ, chỉ số, dấu chuyển vị, norm và bất đẳng thức.

Render bằng phương trình native, LaTeX hoặc MathML thành vector nếu phù hợp công cụ. Giữ nguồn biểu thức để sửa tiếp; không chỉ lưu bitmap cuối.

Cho thấy cấu trúc khi đó là phần cần hiểu: một vector với các phần tử, ma trận có hàng / cột, họ ràng buộc có miền chỉ số. Không bắt mọi ký hiệu đơn giản đều có một sơ đồ phân rã.

Màu, bracket hoặc đường dẫn có thể nối một số hạng với lời giải thích. Tránh dùng màu làm lẫn dấu toán. Một bước biến đổi cần lý do ở cạnh bước nếu người học chưa làm tự động.

## 9. Ảnh, minh họa và chuyển động

Dùng ảnh gốc khi chứng cứ vật lý, lịch sử, nghệ thuật hoặc quan sát là đối tượng học. Nêu nguồn và bối cảnh cần thiết.

Minh họa tạo sinh có thể hữu ích cho tình huống giả định hoặc vật thể khó hình dung. Kiểm tra lỗi giải phẫu, cấu trúc, chữ và bối cảnh. Không trình bày ảnh đó như quan sát thật.

Tạo chuyển động khi sự thay đổi theo thời gian là kiến thức đang học: quỹ đạo, vòng lặp, trạng thái hoặc phép biến đổi. Có điều khiển nhịp, điểm dừng và phương án giảm chuyển động khi định dạng hỗ trợ.

Trong PDF, dùng chuỗi khung chính có trạng thái đầu, bước quyết định và kết quả. Mỗi khung cần đọc được độc lập. Không hứa PDF có animation. Lưu asset đã chọn để tái sử dụng; bản render khóa không gọi lại bộ tạo ảnh.

## 10. Kiểm tra thẩm mỹ và khả năng đọc

Xem contact sheet để tìm nhịp lặp: nhiều trang cùng tỉ lệ, cùng ô, cùng vị trí nhấn dù nhiệm vụ học khác nhau. Chỉ sửa lặp vô ích; một hình nền ổn định trong chuỗi suy luận giúp người học theo bài.

Xem mọi trang ở kích thước trình chiếu. Phóng các công thức, bảng dày, hình nguồn và trang có chữ nhiều để kiểm tra chi tiết. Đọc trang như sinh viên: tiêu đề dẫn đến đâu, nhìn phần nào trước, nhãn nào ứng với đối tượng nào?

Kiểm tra thật trên output cuối: overflow, cắt glyph, đổi font, opacity, label collision, nguồn ảnh, đáp án bị lộ và thứ tự trang. Contact sheet một mình không đủ.

Sau sửa, render lại các trang bị ảnh hưởng và kiểm tra liên kết / thứ tự nếu có tách hoặc gộp. Không báo “đã QA” khi chỉ chạy một phép đo tự động.
