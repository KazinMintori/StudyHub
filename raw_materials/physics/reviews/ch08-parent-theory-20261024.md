# Rà lý thuyết chương 8

Phạm vi: Trang in 235–260, trang PDF 255–280 của Young & Freedman, ấn bản 15. Bao gồm lời mở, sáu mục 8.1–8.6 và tổng kết. Chương tiếp tục là `draft` do bài tập cuối chương chưa hoàn chỉnh.

## Nội dung đã đối chiếu và sửa

- Giữ đủ 16 ví dụ, sáu câu tự kiểm, câu hỏi mở đầu về mưa đá và ứng dụng bắt hai bóng có cùng động lượng. Đã đối chiếu dữ kiện với trang PDF, không suy ra tính đúng từ số lượng tiêu đề.
- Sửa ba phần trong trình tính vốn kiểm nhầm mô hình: Ví dụ 8.1 là hai thuyền trên băng, Ví dụ 8.3 có bóng bay ngang sang trái trước khi được đá lên góc 45°, Ví dụ 8.5 cho vận tốc cuối của B bằng 2,0 m/s và cần tìm A. Lời giải trên bài học đã được đối chiếu độc lập với dữ kiện gốc.
- Mở các bước đại số va chạm đàn hồi 8.21–8.25, phép thế trong Ví dụ 8.10 và phép bình phương hai phương trình thành phần trong Ví dụ 8.12. Giữ nhất quán đơn vị ở hai vế.
- Bổ sung bước đổi hệ quy chiếu khi mở rộng công thức vận tốc tương đối. Phân biệt việc đảo dấu trong một chiều với bảo toàn độ lớn vector vận tốc tương đối trong hai chiều.
- Khôi phục các điều kiện và đoạn đánh giá bị thiếu: Phân biệt động lượng với cơ năng, xung lượng với công, lực tức thời với nguyên lý tích phân, số ẩn trong va chạm hai chiều, ước tính lực ma sát so với lực va chạm và yêu cầu so sánh cả biến thiên động lượng lẫn vận tốc.
- Sửa câu gây hiểu nhầm hai robot phải có góc lệch bằng nhau. Điều kiện thực sự là hai thành phần động lượng theo phương vuông góc bằng nhau về độ lớn, ngược dấu.
- Khôi phục giả thiết lưu lượng khối lượng không đổi của Ví dụ 8.15. Bỏ diễn giải không có căn cứ về tên lửa nhiều tầng trong Ví dụ 8.16. Thời điểm khí phụt đứng yên trong hệ bệ phóng được tính lại là 75,9 s, có ghi chú đối chiếu riêng.
- Thêm lại ảnh và phần giảng ứng dụng chim gõ kiến, phát hiện ngoại hành tinh và mực chuyển động phản lực. Khôi phục đủ sáu sơ đồ tổng kết thay vì dùng ảnh chụp cả bảng tiếng Anh làm bài giảng.

## Ảnh và phần hỗ trợ

44 hình được trích đúng từ PDF, gồm 34 hình đánh số, ảnh mở đầu, ba ảnh ứng dụng và sáu sơ đồ tổng kết. Đã sửa các ảnh sai vị trí hoặc bị cắt mất nhãn, chẳng hạn Hình 8.2, 8.3, 8.5–8.8, 8.12–8.14 và 8.16. Chú thích chỉ dịch những nhãn tiếng Anh thực sự xuất hiện, mỗi nhãn một lần.

Kiến thức nền loại bỏ động lượng khỏi danh sách tiên quyết vì chính bài này dạy khái niệm ấy. Các liên kết mômen động lượng, tọa độ góc và vận tốc góc không liên quan đã được thay bằng động lượng, khối tâm và va chạm đàn hồi. Cheatsheet có 36 dòng công thức, chỉ chứa định nghĩa, tính chất, công thức và điều kiện áp dụng.

## Kiểm tra

- Python của người biên soạn kiểm tra lại dữ kiện gốc, số học, các phép đổi đơn vị, sáu câu tự kiểm và các hệ thức bổ sung bằng tính số hoặc kiểm phần dư.
- Một lượt tính độc lập khác đối chiếu 24 đơn vị gồm 16 ví dụ, sáu câu tự kiểm, câu hỏi mở đầu và ứng dụng bắt bóng. Kết quả số và giả thiết phù hợp dữ kiện gốc sau các sửa nêu trên.
- Đo công thức trong tám mảnh lý thuyết: 220 khối hiển thị và 726 công thức nội dòng, không có lỗi ở ngưỡng 28ex và 27ex. Kiểm tra quan hệ và cách ngắt dòng không phát hiện lỗi.
- Kiểm tra 24 trường hợp trình duyệt cho sáu mục, trang chương và cheatsheet ở 320, 375, 1440 pixel: Đạt. Không có công thức tràn mép, lỗi toán, ảnh hỏng hoặc ký tự TeX còn sót trong chú thích.
- `check_lecture.mjs vat-ly-1/08-dong-luong-va-cham`: Một bài và sáu chủ đề, không có lỗi hoặc cảnh báo cấu trúc.
- Kiểm tra bundle xác nhận mọi công thức và chú giải biến trong cheatsheet đều được biên dịch thành SVG toán.

Build và deploy toàn bộ chỉ thực hiện trên GitHub Actions. Báo cáo này không chứng nhận phần bài tập cuối chương chưa hoàn chỉnh.
