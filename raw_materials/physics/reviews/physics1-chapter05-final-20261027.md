# Hoàn thiện chương 5: Áp dụng các định luật Newton

Chương 5 đã đạt kiểm tra tại nguồn hiện tại và được đăng ký ở trạng thái sẵn sàng. Bản công khai đã vượt qua build, deploy và kiểm tra trang thực tế trên GitHub Pages. Đây chưa phải xác nhận hoàn tất toàn bộ Vật lý đại cương 1 hoặc đợt rà hai học phần.

Giữ đủ năm mục lý thuyết, 23 ví dụ có lời giải, bốn câu tự kiểm đặt trong mạch giảng và 16 công thức đánh số. Notes và năm trang chủ đề gồm đầy đủ 46 ảnh mở đầu, hình đánh số, ứng dụng và sơ đồ tổng kết đã đối chiếu. Có đủ nội dung lực cản, phép tích phân, chuyển động tròn không đều và bốn tương tác cơ bản.

Bài tập được tách riêng thành 159 mục, gồm 12 bài luyện tập hướng dẫn, 28 câu thảo luận, 118 bài đánh số và bài cầu nối có mười câu dẫn. Mỗi mục có một khung lời giải đóng, tóm tắt đề, hướng đi và lời giải chi tiết. Giữ toàn bộ các ý hỏi, đoạn đọc dùng chung, hình và dữ kiện. Có 53 ảnh trích cho phần bài tập và 26 SVG lời giải riêng. Mỗi lần hiển thị hình gốc chỉ có một phần chú thích tiếng Việt.

Cheatsheet có 36 dòng công thức và chỉ gồm định nghĩa, tính chất, công thức, điều kiện và đơn vị. Sáu kiến thức cần ôn trước và sáu khái niệm hỗ trợ có các trang Wiki truy cập được. Tab Cheatsheet đứng sau Bài tập. Giao diện không có tab Slides.

## Kết quả kiểm tra

- Trang học thực tế đạt 240 trường hợp ở 320, 360, 375, 768 và 1440 px. Trong đó có 140 trường hợp chuyển qua đủ 28 nhóm bài, 30 trường hợp Notes và năm chủ đề, 70 trường hợp Cheatsheet, kiến thức nền và 12 trang Wiki.
- Bản ghép nhóm được kiểm riêng trong 140 trường hợp bố cục và 26 trường hợp chữ SVG ở kích thước gốc. Không có công thức tràn, thanh cuộn toán, ảnh hỏng, chữ SVG bị cắt hoặc chồng lên nhau.
- Bộ kiểm tra cấu trúc 133 bài, 354 chủ đề không có lỗi hoặc cảnh báo. Bộ công cụ đạt 39 kiểm thử, nhóm kiểm tra bộ chia bài, dữ liệu nguồn và chế độ dev đạt 12 kiểm thử.
- Các mô hình vật lý và số liệu được kiểm chứng bằng bốn chương trình Python được lưu trong dự án. Mã băm nguồn và bằng chứng kiểm tra được ghi trong JSON đi kèm.

Lượt kiểm tra tuyến trang đầu tiên phát hiện thiếu khối hiển thị bài tập và khối phân tách Notes. Các khối này đã được bổ sung, sau đó kiểm tra lại đủ 159 mục thành công. Kết quả lỗi trước khi sửa được giữ trong bằng chứng nội bộ. Bộ đếm và tệp dữ liệu không đủ để xác nhận người học thực sự truy cập được nội dung.

Build và deploy toàn cục đã chạy thành công trên GitHub Actions. Không chạy build toàn cục trên máy người dùng. Chương 8, đợt rà toàn bộ hai môn, báo cáo kinh nghiệm cuối cùng và dọn dẹp vẫn đang tiếp tục.

## Xác minh bản công khai

Commit `efac57be50c76e7ed1f005a8ca9a15fab919d844` đã build và deploy thành công trong [GitHub Actions 40487728060](https://github.com/KazinMintori/StudyHub/actions/runs/40487728060). Trang công khai có đủ 159 mục, 28 nhóm, 79 ảnh bài tập và 46 ảnh lý thuyết khớp đúng byte với Git. Đã kiểm tra 240 trường hợp hiển thị thực tế, không có lỗi được ghi nhận.
