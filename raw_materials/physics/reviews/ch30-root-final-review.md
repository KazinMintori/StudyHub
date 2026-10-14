# Rà soát chương 30 tại Codex

## Nguồn và nội dung

Đã đối chiếu chương 30 ở trang in 988–1017, cùng đáp số các bài lẻ ở A-18. Lời mở, sáu mục lý thuyết, tổng kết, 29 công thức đánh số và 10 ví dụ có nơi đến. Các câu tự kiểm được đặt tại phần giảng tương ứng, đề nhìn thấy và đáp án gập.

Phần cuối có 75 bài đánh số, 16 câu thảo luận, 12 bài biến thể và một bài cầu nối. Tất cả 104 lời giải dùng khung gập với Tóm tắt đề bài, Hướng đi theo gạch đầu dòng có lý do chọn công thức, và lập luận giải phía dưới. Bảng đáp số có đủ 38 bài lẻ, giữ các điều kiện và quy ước dấu của lời giải.

Các sai lệch dữ kiện, điều kiện đầu, số hiệu và đáp số được ghi trong ch30-root-source-clarifications.md. Hai điểm cần mô hình tường minh là xung bật trường ở 30.53 và dấu hỗ cảm ở 30.69. Các lời giải không lặp đáp số mâu thuẫn với mô hình vật lý.

## Đầu ra Antigravity

Người dùng đã cho phép chế độ bỏ qua hộp xác nhận quyền công cụ cho đúng hai worktree và tác vụ. Mỗi tác vụ có ba lần gọi, gồm lần đầu bị chặn quyền, lần chạy có đầu ra nhưng cầu nối báo lỗi NoneType, rồi một lượt sửa cuối. Lượt cuối A mất mã theo dõi sau khi cầu nối khởi động lại, còn B hết thời gian 1800 giây.

Không xem các trạng thái trên là thành công của tác vụ. Codex kiểm tra toàn bộ tệp tạo mới và không có sửa tệp tracked ngoài phạm vi. Các bản chụp ổn định được lưu ở QA. Sau đó Codex đối chiếu nguồn và sửa trực tiếp bản sao, trước khi tích hợp nội dung đã rà. Không chép các báo cáo AGY có mô tả bài tập bịa đặt vào hồ sơ đã nghiệm thu. Hai worktree gốc vẫn được giữ nguyên để truy hồi.

## Sửa chữa sau đọc đối chiếu

- Khôi phục bốn lựa chọn câu hỏi mở đầu và lựa chọn thứ năm của tự kiểm 30.1.
- Giữ đủ sáu mục tiêu, kiến thức cần ôn, các ứng dụng, nhận xét cuối ví dụ và quy trình phân tích mạch có cuộn cảm.
- Sửa ký hiệu Phi_B thiếu dấu gạch chéo, đặt nhãn 30.20 vào phương trình dao động điện tích và sửa phép chia ở Ví dụ 30.6.
- Khôi phục đề Ví dụ 30.7 hỏi phần năng lượng bị tiêu tán sau 2,3 hằng số thời gian.
- Sửa tiếp điểm nạp d, tiếp điểm phóng a trong mạch RLC và toàn bộ tiền tố micro của tự kiểm 30.6.
- Tính pha RLC theo cả điện tích và dòng đầu. Phân biệt hệ không dao động lặp lại với một nghiệm có thể đổi dấu một lần.
- Giữ bảng tương tự cơ–điện đầy đủ, đồng thời tách chuỗi công thức dài khỏi ô bảng.
- Bỏ chú thích nhãn tiếng Anh lặp lại trong Markdown, giữ duy nhất chú giải từ module dưới mỗi ảnh.
- Nới các crop bị cắt, gồm phần mạch của 30.13 và đoạn dây dưới hình tổng kết tự cảm.

## Các phần hỗ trợ và kiểm tra

Chương có 11 Slides, Cheatsheet sáu nhóm chỉ định nghĩa, tính chất, công thức và điều kiện, 11 Wiki mới cùng mục tự cảm được mở rộng. Có 44 ảnh PNG và sáu đồ thị SVG lời giải, trong đó các đồ thị dữ liệu dùng đủ điểm đo. Chú thích được viết bằng tiếng Việt và giải nghĩa mỗi nhãn tiếng Anh một lần trên mỗi hình.

Năm bộ Python, phép kiểm kê nội dung nguồn, đo độ rộng MathJax, kiểm tra công thức trên thẻ và kiểm tra chú thích ảnh đã chạy. Kết quả hiển thị cuối, build và kiểm thử được ghi trong chapter-30-review.json sau khi hoàn tất các bước. Kiểm tra cấu trúc và việc không có cảnh báo không thay thế đối chiếu ý nghĩa.

Phần đã khép nội dung trước đây là các chương 21–29. Chương 31–44 và phần còn lại của Vật lý 1 chưa được chứng nhận hoàn tất.
