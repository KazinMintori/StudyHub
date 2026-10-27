# Rà soát luyện tập hướng dẫn, thảo luận và bài cầu nối chương 8

Trạng thái: Đã hoàn thiện riêng 39 đơn vị gồm 12 bài luyện tập hướng dẫn, 26 câu thảo luận và một bài cầu nối. Chương chưa được xác nhận sẵn sàng xuất bản. Còn bước duyệt toàn bộ lý thuyết, kiến thức nền, Wiki, cheatsheet và các tab.

Đã đối chiếu trực tiếp các trang PDF 281–283 và đọc lại các ví dụ, hình được câu hỏi dẫn tới. Phát hiện bản nháp thảo luận cũ thay nhiều câu hỏi bằng câu khác. Đã khôi phục đúng nội dung các câu 7–11 và 15–19, gồm mọi phần hỏi và các lựa chọn. Mỗi đơn vị có một khung lời giải đóng với tóm tắt, hướng đi và lời giải.

Các kết quả cần giữ rõ điều kiện:

- VP8.6.4: Tỉ số tốc độ suy từ phương đứng cần góc lệch khác không. Góc bằng không không xác định tỉ số, còn góc vuông không phù hợp động lượng ngang ban đầu khác không.
- VP8.14.4: Không có ngoại lực chỉ suy ra vận tốc khối tâm không đổi. Đề chưa cho vận tốc khối tâm ban đầu. Lời giải trình bày nghiệm tổng quát và kết quả riêng khi tổng động lượng đầu bằng không. Hai mô hình Newton với lực tương tác từng đôi đã được tích phân độc lập để kiểm chứng sự không xác định duy nhất.
- Q8.11: Vận tốc tương đối trong cả ba ví dụ đàn hồi có cùng độ lớn trước và sau. Hai ví dụ một chiều đảo hướng, ví dụ hai chiều chỉ đổi hướng.
- Q8.17: Bảo toàn động lượng gần đúng trong lúc bóng chạm vợt cần kiểm tra xung lượng từ tay và trọng lực. Không áp dụng kết luận ấy cho toàn khoảng hai giây sau.
- Q8.20: Phụt khí thở có thể trao đổi động lượng. Chỉ đổi tư thế trong một hệ kín không làm khối tâm tự có động lượng ngang.
- Q8.22: Tỉ số động năng nghịch đảo khối lượng cần xét trong hệ khối tâm ban đầu, không phải mọi hệ quy chiếu.

Bài cầu nối giữ đủ sáu ý hỏi và 11 câu định hướng trước khung lời giải. Bên trong lời giải có 11 mục tương ứng và sơ đồ riêng biểu diễn ba trạng thái, chín trạng thái vật và bảy mũi tên vận tốc cùng tỉ lệ.

Bảy khung ảnh được giữ nguyên điểm ảnh gồm thanh tài nguyên đa phương tiện và sáu hình liên quan 8.3, 8.18, 8.23, 8.25, 8.26, 8.27. Mỗi lần hiển thị có một chú thích và một phần giải nghĩa nhãn. Thanh tài nguyên được lặp ở đầu mỗi nhóm luyện tập khi nhóm được xem độc lập, nên có tám lần hiện phần giải nghĩa trên toàn bộ tám nhóm.

Kết quả xác minh:

- 232 phép kiểm tra vật lý, hình học và cấu trúc có thể chạy lại bằng Python.
- 39 đơn vị và các phần trả lời được ràng buộc bằng mã băm.
- 7 ảnh tái tạo trùng điểm ảnh và mã băm, sơ đồ SVG tái tạo trùng mã băm.
- 83 công thức hiển thị và 395 công thức nội dòng qua kiểm tra độ rộng, không dùng ngoại lệ.
- 40 lượt xem trên các chiều rộng 320, 360, 375, 768 và 1440 px. Công thức hiện đủ, không tràn hoặc có thanh cuộn toán. Các khung lời giải ban đầu đóng và hình tải đủ.
- 1 lượt kiểm tra SVG ở hệ tọa độ gốc, không có chữ bị cắt hoặc chồng.

Đã giữ bản ghi của lỗi công cụ kiểm tra khi tên tệp SVG chỉ có trường publicFile. Công cụ đã được sửa để đọc trường này rồi chạy lại toàn bộ 40 lượt xem. Đây là lỗi của bộ kiểm tra riêng, không phải lỗi nội dung trang học.

Lệnh tái kiểm tra: Chạy Python với raw_materials/physics/verify_chapter8_guided_discussion.py. Hai tệp scripts/prepare-physics1-remaining-08-guided-discussion-assets.py và scripts/generate-physics1-remaining-08-bridge-solution.py tái tạo tài nguyên.

Báo cáo này chỉ xác nhận phạm vi 39 đơn vị. Các kiểm tra cấu trúc, số lượng và mã băm không thay thế việc đọc nội dung, không xác nhận hoàn tất toàn bộ hai học phần hoặc bản triển khai công khai.
