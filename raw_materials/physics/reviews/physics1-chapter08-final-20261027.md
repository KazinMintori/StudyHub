# Hoàn thiện chương 8: Động lượng, xung lượng và va chạm

Chương 8 đã hoàn tất phần nội dung và kiểm tra trên trang học cục bộ. Bài giảng được chuyển sang trạng thái sẵn sàng. Build, deploy và xác minh bản công khai đang chờ thực hiện trên GitHub. Báo cáo này chưa xác nhận hoàn tất đợt rà toàn bộ hai học phần.

Giữ đủ sáu mục lý thuyết, 16 ví dụ có lời giải, sáu câu tự kiểm nằm trong mạch giảng và 40 phương trình đánh số. Đã đối chiếu lời dẫn, ứng dụng, giả thiết, các bước chứng minh và phần đánh giá kết quả với trang PDF 255–280. Phần giải thích phân biệt công với xung lượng, động lượng với động năng, vận tốc khối tâm không đổi với khối tâm đứng yên, vận tốc khí đối với tên lửa với vận tốc trong hệ quan sát.

Notes và các chủ đề có 44 ảnh mở đầu, hình đánh số, ảnh ứng dụng và sơ đồ tổng kết. Ví dụ 8.1 còn có Hình 6.14 được dẫn lại đầy đủ. Ảnh Atlas đã được mở rộng khung trích để khôi phục phần đầu bị cắt. Các điểm ảnh vốn được giữ lại không thay đổi. Chú thích tiếng Việt đi cùng hình và giải nghĩa các nhãn tiếng Anh xuất hiện.

Bài tập được tách thành 148 mục, gồm 12 bài luyện tập hướng dẫn, 26 câu thảo luận, 109 bài đánh số và một bài cầu nối có sáu phần, 11 câu dẫn. Mỗi mục có một khung lời giải đóng, tóm tắt đề, hướng đi nêu lý do chọn phương pháp và lời giải chi tiết. Giữ đoạn đọc và các lựa chọn của nhóm câu hỏi MCAT. Phần này có 29 ảnh trích và hai sơ đồ lời giải riêng.

Cheatsheet gồm 39 dòng công thức cùng các định nghĩa, tính chất, điều kiện và đơn vị. Các tổng hữu hạn được khai triển và chỉ số khối tâm được thống nhất với Notes. Năm kiến thức cần ôn trước và ba khái niệm hỗ trợ có tám trang Wiki truy cập được. Đã đồng bộ nội dung của bảy trang Wiki với dữ liệu dùng trong thẻ tra cứu. Giao diện không có tab Slides và tab Cheatsheet đứng sau Bài tập.

## Các điểm cần xử lý bằng lập luận

- Ví dụ 8.16 có thời điểm in là 75,6 s. Từ lưu lượng khối lượng và điều kiện vận tốc khí bằng không, phép tính cho 75,854467 s. Lời giải dùng 75,9 s khi làm tròn.
- Bài luyện tập VP8.14.4 chưa xác định vận tốc ban đầu của khối tâm. Lời giải nêu dạng tổng quát và ghi rõ điều kiện cần để dùng trường hợp khối tâm đứng yên.
- Bài 8.94 chưa đủ dữ kiện để suy ra duy nhất vị trí cuối sau khi cả hai người đã tiếp đất. Lời giải phân biệt kết quả có điều kiện với kết luận từ các dữ kiện được cho.
- Bài 8.100 cần đọc đúng các đoạn của đồ thị lực theo thời gian và tính cả khối lượng người lái. Bài 8.101 giữ đủ năm dòng dữ liệu và các kết quả tương ứng.
- Va chạm đàn hồi hai chiều bảo toàn độ lớn vận tốc tương đối. Không áp dụng phép đảo dấu của vận tốc tương đối một chiều cho mọi vector trong hai chiều.

## Kết quả kiểm tra

- Trang học thực tế đạt 220 trường hợp ở 320, 360, 375, 768 và 1440 px. Gồm 35 trường hợp Notes và sáu chủ đề, 135 trường hợp chuyển qua 27 nhóm bài, 50 trường hợp Cheatsheet, kiến thức nền và tám trang Wiki.
- Các khối lý thuyết và bài tập còn được kiểm riêng trong 40 và 135 trường hợp bố cục. Hai sơ đồ lời giải được kiểm biên chữ và chồng chữ ở kích thước gốc.
- Không phát hiện công thức tràn, thanh cuộn toán, MathML phụ trợ hiện ra, ảnh hỏng hoặc lỗi JavaScript trong các lượt kiểm trang đã nêu.
- Python kiểm 352 quan hệ, mô hình và đối chiếu điểm ảnh của lý thuyết. Các chương trình phần bài tập kiểm 270, 428 và 232 điều kiện. Có thêm 25 phép kiểm các ví dụ số và quan hệ vật lý trong Wiki.
- Kiểm tra cấu trúc 133 bài, 354 chủ đề không có lỗi hoặc cảnh báo. Bộ công cụ đạt 39 kiểm thử. Bộ kiểm tra chia nhóm bài, dữ liệu nguồn và chế độ dev đạt 12 kiểm thử.
- Chỉ mục chương 8 được sinh lại bằng chương trình hiện có với bộ lọc riêng. 137 chỉ mục còn lại giữ nguyên từng byte, bao gồm tệp chương 6 đã có thay đổi từ trước.

Mã băm nguồn, phạm vi từng bằng chứng và các quyết định rà soát được lưu trong JSON đi kèm. Các kết quả trên chứng minh phạm vi chương 8 đã kiểm, không thay thế việc duyệt toàn bộ Vật lý đại cương 1 và 2.
