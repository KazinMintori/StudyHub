# Rà soát phần luyện tập và thảo luận Chương 5

Đã đối chiếu và tích hợp 41 đơn vị, gồm 12 bài hướng dẫn VP, 28 câu thảo luận và một bài cầu nối với đủ 10 câu hỏi định hướng. Chương 5 còn 118 bài đánh số cần được nghiệm thu. Trạng thái chương vẫn là bản nháp, chưa bật trang bài tập cuối chương.

Đã đọc các trang PDF 177–179 và kiểm tra những hình lý thuyết được bài tập dẫn lại. Chín ảnh giữ nguyên điểm ảnh khi đối chiếu với vùng tương ứng trong PDF. Hai sơ đồ lời giải riêng có ba giản đồ lực, dùng chữ cỡ 20 đơn vị. Các mũi tên được kiểm tra trực tiếp từ tọa độ trong SVG.

Phần tính toán có 626 kiểm tra độc lập. Trong đó có 28 trường hợp tối ưu tuyến tính để đối chứng miền ma sát của vật trong hình nón quay và 9 trường hợp tích phân phương trình chuyển động có lực cản bậc hai. Kiểm tra số học không thay thế việc đọc đề, giả thiết và lời giải.

Các sửa đổi có ý nghĩa gồm khôi phục đủ câu hỏi cầu nối, bỏ dữ kiện số tự thêm vào đề, sửa lựa chọn đồ thị của Q5.25 và Q5.26, thống nhất dấu của lực cản và bổ sung các trường hợp chu kỳ không có cận hữu hạn. Câu Q5.23 yêu cầu xét lực cản không khí, điều kiện này đã được giữ đúng sau khi kiểm tra trực tiếp câu tiếng Anh. Những khẳng định về ngưỡng chấn thương và hiệu ứng thủy động lực học không có căn cứ đã được bỏ.

Bản tích hợp đã qua 40 lượt kiểm tra trình bày tại các chiều rộng 320, 360, 375, 768 và 1440 px. Cả 41 lời giải đều đóng ban đầu. Không phát hiện lỗi hiển thị công thức, thanh cuộn, ảnh tải thất bại hoặc chữ SVG vượt khung và chồng nhau trong phạm vi đã kiểm tra. Đây là kiểm tra nội dung nhóm với bộ dựng Markdown và CSS của dự án, chưa phải xác nhận trang bài tập công khai.

Chương trình có thể chạy lại là `raw_materials/physics/verify_chapter5_partial_exercises.py`. Hai chương trình trong `scripts/` tái tạo ảnh từ PDF và sơ đồ lời giải. Dấu vân tay của Markdown và SVG dùng xuống dòng LF để kết quả nhất quán giữa Windows và GitHub. PNG và PDF vẫn được kiểm tra bằng byte gốc.

Việc còn lại gồm nghiệm thu toàn bộ 118 bài đánh số, kiểm tra nhóm bài của chương hoàn chỉnh, kiểm tra liên kết và giao diện thật, sau đó xác nhận bản triển khai GitHub. Báo cáo này không xác nhận toàn chương hay toàn học phần đã hoàn thành.
