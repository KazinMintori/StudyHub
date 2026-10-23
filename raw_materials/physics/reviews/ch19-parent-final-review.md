# Rà soát chương 19

Phạm vi: Lời mở, tám mục 19.1–19.8, bảy ví dụ, câu tự kiểm tại từng mục, tổng kết, 12 bài luyện tập hướng dẫn, 24 câu thảo luận, 66 bài đánh số và một bài cầu nối. Nguồn đối chiếu tại PDF 633–661.

## Những điểm đã sửa

Đã phục hồi dữ kiện của các ví dụ 19.2, 19.3 và 19.6, phân biệt cách dùng nhiệt dung đã làm tròn trong 19.7. Bảng 19.1 được đối chiếu lại chín hàng. Quan hệ đoạn nhiệt có điều kiện mô hình khí lý tưởng, nhiệt dung không đổi và quá trình gần cân bằng. Giãn nở tự do không được đánh đồng với nén hoặc giãn đoạn nhiệt thuận nghịch.

Phần bài tập giữ đủ câu hỏi và lựa chọn của đoạn đọc 19.63–19.66. Đã sửa áp suất tuyệt đối trong 19.66, đọc đồ thị 19.4, 19.38 và 19.44, đồng thời tính lại các kết quả phụ thuộc. Q19.24 được sửa dấu tổng công và nhiệt vì vòng I lớn hơn vòng II. Diện tích hai vòng được kiểm tra độc lập từ đường Bézier của PDF, bên cạnh việc đọc chiều mũi tên.

Đã bổ sung tám giản đồ lời giải cho các bài yêu cầu vẽ hoặc hồi quy. Giản đồ 19.19 chỉ thể hiện loại quá trình do bộ dữ kiện ban đầu không mô tả cùng một trạng thái khí lý tưởng. Các dữ kiện không bị sửa âm thầm. Bài 19.36 nêu rõ những lựa chọn ước lượng khi tính sự nâng nắp nồi.

## Bố cục và ngôn ngữ

103 đề được chia thành 19 nhóm, mỗi đề có lời giải đóng khi tải. Đề, hình và các ý hỏi hiện trước lời giải. Lời giải có Tóm tắt đề bài, Hướng đi giải thích cách chọn định luật và các bước giải. Đoạn đọc được giữ cùng những câu hỏi tương ứng khi đổi nhóm.

Đã sửa ký tự xuống dòng bị in thành văn bản, các chuỗi quan hệ quá dài và những chỗ xuống dòng tách vế trái khỏi dấu bằng. Các phép thế số lặp lại chỉ được rút gọn sau khi tính lại bằng Python. Giữ phương trình vật lý, dữ kiện tóm tắt, các bước suy luận và kết quả. Công thức nội dòng được chuyển ra ngoài khi quá dài. Dấu chấm phẩy và lời văn cường điệu được biên tập lại.

47 ảnh PNG được so lại từng byte RGB với vùng cắt PDF. Chú thích tiếng Việt dưới ảnh và phần dịch nhãn được giữ một lần, không dịch ký hiệu toán thành nhãn tiếng Anh giả. Các hình đồ thị nguồn được giữ nguyên, các giản đồ lời giải bổ sung có chương trình tạo riêng. Ảnh 19.12 giữ đầy đủ đồ thị và nhãn, kèm một phần rất nhỏ ký tự tiếp nối ngoài hình ở góc ảnh. Đây là hạn chế mép cắt, không phải phần đồ thị bị thiếu.

## Kiểm tra

- Cấu trúc bài và tám trang chủ đề không báo lỗi.
- Đo công thức ở 15 tệp thô, với ngưỡng sàng lọc 28ex cho khối và 27ex cho nội dòng. Kết quả hiển thị thực tế được kiểm tra riêng, không suy từ ngưỡng sàng lọc.
- Chạy các bộ tính của bảy ví dụ, 12 bài luyện tập, 66 bài đánh số và bài cầu nối. Bổ sung kiểm tra tích phân áp suất van der Waals, các tỷ số nén nguyên của 19.61 và hình học thực của Q19.24.
- Kiểm tra trình duyệt ở 320, 360, 375 và 1440 px: Notes và tám chủ đề, toàn bộ 19 nhóm bài tập, Slides và Cheatsheet.

Hồ sơ nghiệm thu máy nằm trong `chapter-19-review.json`. Nội dung chỉ được ghi nhận hoàn tất trong worktree riêng. Chưa coi build hoặc triển khai GitHub đã thành công. Các chương ưu tiên còn lại vẫn được rà riêng.
