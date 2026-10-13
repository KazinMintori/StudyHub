# Chốt rà soát chương 29

## Phạm vi nội dung

Đã biên soạn lời mở, tám mục lý thuyết, tổng kết và toàn bộ phần cuối chương, từ trang in 953 đến 987. Giữ 24 phương trình đánh số, 11 ví dụ, các câu tự kiểm trong mạch lý thuyết, 74 bài đánh số, 21 câu thảo luận, 12 bài biến thể và một bài cầu nối. Có 108 khung lời giải chi tiết cùng bảng tra cứu 37 bài lẻ.

Ba lượt rà độc lập được lưu trong các báo cáo basic-cross, advanced-cross và theory-figure-audit. Các phát hiện đã được xử lý như sau:

- Bài 29.58 có cả thành phần y và z của từ trường âm. Đã sửa đề, tích có hướng, dấu hiệu điện thế, đầu b cao thế hơn, sơ đồ SVG và verifier Python.
- Câu dẫn MCAT giữ bối cảnh hạn chế của kích thích trực tiếp trước phương pháp TMS, thay cho câu diễn đạt ngược ý nguồn trong bản nháp.
- Mục 29.5 nêu rõ thành phần tiếp tuyến được xác định bởi Faraday. Nếu dùng Gauss để loại phần xuyên tâm đối xứng, phải dùng một mặt trụ kín và các điều kiện không có điện tích, không có kỳ dị trên trục.
- Mục 29.7 bổ sung điều kiện tĩnh điện, từ tĩnh và điều kiện biên khi liên hệ Maxwell với Coulomb, Biot–Savart.
- Thuật ngữ máy phát điện xoay chiều và điện kế đã được Việt hóa. Các nhãn tiếng Anh trong hình được giải nghĩa đúng một lần dưới ảnh.
- Hình 29.17 đã bỏ riêng mảnh chữ của chú thích phía trên, giữ nguyên nhãn trục y. Hình E29.18 nới mép trên để giữ trọn nhãn dòng điện. Các crop khác đã rà trục, mũi tên và đơn vị.
- Đáp số 29.41 tuân phân số 1/6 trong đề, cho 0,958 s. Bài 29.45 cho 1,35 mA theo dữ kiện in. Bài 29.67 cho 4,71 mA, khác đơn vị sai trong đáp số phụ lục. Những khác biệt này được ghi riêng trong hồ sơ nội bộ.

## Cấu trúc và hiển thị

Notes giữ ví dụ và tự kiểm tại phần giảng liên quan. Phần cuối chương nằm trong tab Bài tập. Từng lời giải có Tóm tắt đề bài, Hướng đi theo gạch đầu dòng và bước giải chi tiết, mặc định gập. Cheatsheet đứng sau Bài tập và chỉ có định nghĩa, tính chất, công thức, điều kiện cùng ý nghĩa đại lượng và đơn vị. Có 12 Slides, 15 Wiki mới và một mục cảm ứng điện từ được mở rộng.

Bộ tài sản có 79 ảnh PNG từ nguồn và sáu sơ đồ hoặc đồ thị lời giải. Năm hình được sinh lại bằng script, đồ thị dữ liệu dùng đủ các điểm đo. Bảy bộ Python và kiểm kê cấu trúc 108 lời giải đã qua. Kết quả build, trình duyệt, Wiki và đổi kích thước cuối cùng được ghi trong `chapter-29-review.json` sau khi hoàn tất kiểm tra.

Lượt kiểm tra toàn bộ chín chương cũng phát hiện các lỗi định dạng còn sót từ đợt sửa công thức trước. Đã khôi phục đạo hàm năng lượng quay ở chương 21, tách các phương trình có hai số hiệu trong cùng khối ở chương 22 và 25, sửa căn hàng của slide dụng cụ đo ở chương 26. Tích phân điện thông ở chương 22 và hai chuỗi tính toán ở chương 28 được bẻ dòng. Phép cộng trường rời rạc, định luật Kirchhoff, công thức RC và công của lực từ cũng được sửa để đọc được ở 320 px. Nội dung, giả thiết, số hiệu và các bước suy luận được giữ đầy đủ.

## Giới hạn xác nhận

Phạm vi đã hoàn thiện là chương 29 cùng các chương Vật lý 2 đã khép nội dung trước đó. Chương 30 trở đi và phần còn lại của Vật lý 1 vẫn được ghi là chưa hoàn tất. Kết quả build không được dùng để chứng nhận các chương còn thiếu.
