# Xác minh bản công khai của sáu chương đã sửa

Commit 5e360c54e86bcde5f6b76bb4cc41027e9e0c2a2f đã build và deploy thành công trong [GitHub Actions 40552984997](https://github.com/KazinMintori/StudyHub/actions/runs/40552984997). Không build toàn bộ trên máy người dùng.

Notes và toàn bộ trang lý thuyết của các chương 21, 23, 25, 35, 36 và 39 đạt 215 trường hợp hiển thị trên bản công khai. Tab Bài tập chương 21 đạt thêm năm trường hợp khi mở toàn bộ lời giải. Các độ rộng được kiểm là 320, 360, 375, 768 và 1440 px.

Trong phạm vi này không ghi nhận công thức tràn, thanh cuộn toán, MathML phụ trợ hiện ra hoặc ảnh hỏng. Các khung lời giải đóng khi mới mở trang và hai sơ đồ lời giải từng bị lặp chỉ xuất hiện một lần. Các mã băm nguồn sau lượt sửa cuối khớp commit được xuất bản. Tệp bài tập được chỉnh tiếp sau lượt sửa ảnh dùng mã băm mới trong báo cáo bài tập, với quan hệ thay thế được ghi rõ trong JSON.

Lượt kiểm đầu tiên giả định tên tệp ảnh công khai giống tên nguồn. Vite thêm mã băm vào tên tệp, nên phép đếm đó không tìm thấy ảnh dù ảnh vẫn hiển thị. Phép kiểm được sửa theo tên tệp thực tế, giữ bằng chứng lỗi cũ và chạy lại đủ năm cỡ màn hình thành công.

Kết quả này xác nhận bản công khai của các sửa đổi bố cục đã nêu. Các chương khác, việc duyệt đầy đủ nội dung nguồn, từng hình, bài tập, Cheatsheet, Wiki, báo cáo tổng kết và dọn dẹp vẫn tiếp tục.
