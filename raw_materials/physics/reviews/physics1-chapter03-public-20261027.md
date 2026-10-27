# Kiểm tra chương 3 trên website đã xuất bản

Chương 3 đã được xác nhận trên website sau lượt GitHub Actions [40375605657](https://github.com/KazinMintori/StudyHub/actions/runs/40375605657), commit `68ee041995d05688f602f644a262e625f7d3e60e`. Cả công việc build và triển khai đều thành công.

Tab Bài tập chứa đủ 115 mục trong 22 nhóm, gồm 13 bài luyện tập hướng dẫn, 16 câu thảo luận, 85 bài đánh số và bài cầu nối. Mỗi mục có một khung lời giải đóng khi tải. Đã đối chiếu dấu vân tay nguồn và 45 ảnh bài tập với dữ liệu Git của bản xuất bản. Mọi ảnh kiểm tra đều trùng khớp từng byte.

Trang chương và năm trang lý thuyết chứa đủ 47 khung hình đã duyệt. Đường dẫn ảnh có mã băm được lấy trực tiếp từ HTML xuất bản, sau đó tải và so sánh với tệp Git tương ứng. Không suy ra ảnh có mặt chỉ từ một danh sách tên dự kiến.

Kiểm tra trực tiếp trong trình duyệt gồm 110 trường hợp bài tập và 35 trường hợp lý thuyết hoặc cheatsheet. Năm chiều rộng là 320, 360, 375, 768 và 1440 px. Tất cả đạt, không ghi nhận ảnh thiếu, lỗi công thức, tràn trang hoặc thanh cuộn trên công thức trong phạm vi đã kiểm tra. Các công thức bài tập đều phải nhìn thấy được sau khi mở lời giải. Ảnh trong trang lý thuyết được yêu cầu tải trước khi đo bố cục.

Mười hai tệp nội dung đã được duyệt vẫn giữ nguyên dấu vân tay. Lượt kiểm tra này xác nhận bản xuất bản của chương 3. Nó không thay thế việc hoàn thiện chương 5, chương 8, rà toàn bộ hai học phần, viết báo cáo tổng kết hoặc dọn dẹp dự án.

Chi tiết số lượng, phạm vi và dấu vân tay báo cáo được lưu trong tệp JSON cùng tên.
