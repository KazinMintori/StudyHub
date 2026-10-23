# Rà soát chương 9 trong bản làm việc

Hồ sơ này dành cho biên tập, không được include vào bài giảng.

## Phạm vi nội dung

Đã đối chiếu các mục 9.1–9.6, lời mở đầu, tổng kết và phần cuối chương với PDF trang 292–321. Trang Notes giữ các ví dụ giảng dạy 9.1–9.11 và sáu câu tự kiểm ở vị trí tương ứng. Tab Bài tập có 12 bài luyện tập hướng dẫn, 22 câu thảo luận, 95 bài đánh số và một bài cầu nối.

Các bài cuối chương giữ đề trước khung lời giải gập. Trong lời giải có tóm tắt dữ kiện, hướng đi nêu lý do chọn tính chất hoặc công thức, các bước biến đổi và kết quả từng ý. Đoạn đọc về cá chình đi ngay trước các câu 9.92–9.95. Các bài yêu cầu dựng đồ thị có đồ thị trong khung lời giải.

## Những sai lệch đã sửa sau khi nhận bản nháp

- Ví dụ 9.7: Mã kiểm tra từng dùng đường kính 0,120 m làm bán kính. Dữ kiện thật cho bán kính 0,060 m, momen 0,090 kg m² và tốc độ góc 20 rad/s. Nội dung đúng được giữ và mã kiểm tra đã sửa.
- Hình 9.14: Bản cắt ban đầu trỏ nhầm vào ảnh kền kền. Đã trích đúng thiết bị hai quả nặng ở cuối trang PDF303. Ảnh kền kền được giữ riêng cùng ứng dụng so sánh với chim ruồi.
- Hình 9.2, 9.13 và hai hình của phần bài tập: Đã mở rộng vùng cắt để giữ đủ các phần hình hoặc nhãn.
- Các nhãn tiếng Anh do bản nháp tự suy diễn đã được bỏ. Chú thích chỉ dịch chữ thực sự có trong hình, mỗi nhãn một lần.
- Bài 9.91: Bước rãnh được đọc trực tiếp từ PDF là 1,55 micromét, không phải milimét.
- Bài cầu nối: Trường hợp trục nằm bất kỳ trong thanh dùng bán kính xa nhất là max(h,L−h). Dạng L−h được giữ cho cách chọn đầu thanh với h không vượt quá L/2.
- Ví dụ ước lượng cơ thể phân biệt bộ kích thước minh họa với số đo của người học. Tổng khối lượng trong mô hình Q9.22 đã được làm nhất quán.

## Kiểm tra

Số học được tính lại bằng Python, gồm bài có số liệu, phép khớp bình phương tối thiểu và các phép kiểm tra tích phân hoặc đồng nhất thức đối với bài ký hiệu. Ba đồ thị lời giải có script sinh lại.

Đã so sánh 56 ảnh trích với mảng RGB từ lần raster hóa PDF mới. Đã xem các bảng ảnh và các vùng nguồn cần sửa, sau đó kiểm tra lại mép hình. Pixel trùng khớp không được dùng thay cho việc xem hình.

Đã đo công thức trong 13 tệp nội dung, theo ngưỡng 25ex cho khối và 27ex cho nội dòng. Trang Notes, sáu chủ đề, Slides, Cheatsheet và toàn bộ 23 nhóm bài tập đã được kiểm tra ở 320, 360, 375 và 1440 px. Các lời giải được mở trong lượt kiểm tra bố cục. Khung lời giải được kiểm tra đóng khi vừa tải nhóm.

Phần Bài tập tải từng nhóm để không biên dịch hoặc tải đồng thời toàn bộ lời giải cùng trang Notes. Mỗi nhóm vẫn giữ nguyên từng đề và lời giải. Đã kiểm tra đủ 130 đề trên trình duyệt và không có yêu cầu tài nguyên lỗi.

Bộ 39 kiểm thử của skill và 139 kiểm thử của kho đã qua. Build toàn trang và deploy chưa chạy cho lượt thay đổi này. Chương được ghi nhận hoàn tất nội dung trong worktree riêng, không đồng nghĩa các chương ưu tiên còn lại đã hoàn tất.
