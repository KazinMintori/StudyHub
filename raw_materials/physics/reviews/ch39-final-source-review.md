# Rà nội dung và trình bày chương 39

Phạm vi: Trang in 1279–1320 (PDF 1299–1340), sáu mục lý thuyết, mười ví dụ, sáu câu tự kiểm và 30 công thức đánh số. Có 91 bài đánh số, 22 câu thảo luận, 12 bài hướng dẫn và một bài cầu nối. Mỗi đề đứng trước hộp lời giải gập với Tóm tắt đề bài, Hướng đi có lý do chọn công thức, rồi các bước giải.

## Các sửa đổi sau khi đối chiếu

- Khôi phục proton ở bài 39.1 và ba loại hạt có cùng bước sóng 0,20 nm ở bài 39.2. Bản nháp trước đã đổi đề.
- Khôi phục các tiểu câu bị mất trong nhóm 39.20–39.45, gồm ion hóa và bán kính tương đối của ion beri, tốc độ quỹ đạo, mọi chuyển mức của Searsium, công thoát, khối lượng rút gọn và các ứng dụng laser.
- Giữ đầy đủ các hình E39.25, E39.27, P39.84, hình cầu nối 39.36, bảng sao và sáu cặp số liệu nhiễu xạ. Các bảng được đổi chiều hoặc tách thành các bảng hẹp, giữ nguyên mọi giá trị.
- Đổi đúng thời gian sống bài 39.76 thành 2,0 micro giây. Giữ đúng giả thiết ước lượng px ≈ h của bài 39.78 và 39.79, không thay h bằng hbar.
- Giữ khối lượng 1,32 × 10⁻²⁵ kg được cho trong bài 39.85. Phân biệt tốc độ alpha lớn hơn c do ngoại suy cổ điển với khả năng hạt nhân giật lùi ở 0,10c trong mô hình tương đối tính.
- Phân biệt khoảng độ rộng, độ lệch chuẩn, thang lan rộng và vận tốc thực. Bài 39.86 nêu rõ mô hình cộng độ rộng, mô hình Gaussian có hiệp phương sai ban đầu bằng không, cùng số hạng hiệp phương sai của trường hợp tổng quát.
- Không dùng độ rộng một cực đại riêng lẻ làm độ lệch chuẩn toàn bộ phân bố động lượng. Câu thảo luận về cách tử nhiều khe xét cả các bậc và bao ngoài.
- Phân biệt năng lượng toàn phần của hạt tự do với năng lượng liên kết nguyên tử. Nêu miền phi tương đối tính, gần đúng hạt nhân cố định, độ suy biến và giới hạn của suy luận nhiệt độ từ quang phổ.
- Bổ sung hai ý về laser bị thiếu trong bản nháp: Sự hấp thụ lấn át khi chiếu sáng trực tiếp hệ hai trạng thái, và việc đảo lộn giữa hai mức laser không đòi hỏi mức siêu bền đông hơn mức cơ bản.

## Ảnh và chú thích

Có 52 PNG trích từ các vùng PDF, tất cả khớp từng pixel với phép render cùng vùng và độ phóng đại. Không vẽ lại, ghép hoặc sửa nội dung ảnh. Hình 39.26 được mở rộng vùng trích để giữ đủ đường quỹ đạo. Hai vùng (a–c) và (d) của hình 39.29 được trình bày riêng, giữ nguyên bố trí bên trong từng vùng.

Có một SVG lời giải tái lập cho phép hồi quy bài 39.82. Mỗi ảnh có chú thích tiếng Việt. Các nhãn tiếng Anh thực có trên ảnh được giải nghĩa qua danh mục chú thích tập trung, mỗi nhãn một lần trong ảnh tương ứng.

## Các kiểm tra đã thực hiện

- Mọi bài định lượng có phép tính Python. Có các kiểm tra độc lập về bảo toàn, miền số lượng tử, giới hạn tương đối tính, phép đổi biến phổ với Jacobian, hồi quy và hiệp phương sai.
- Có 163 lượt trình duyệt cho lý thuyết và tài liệu hỗ trợ, thêm 19 lượt cho toàn bộ bài tập và Cheatsheet. Các lượt này dùng phông thật tại 320, 360, 375 và 1440 px, kèm thay đổi bề rộng trực tiếp.
- Đã mở các hộp lời giải để kiểm tra công thức. Đã kiểm đủ 126 đề và 126 hộp lời giải, mặc định đóng, các chú thích ảnh và nhãn song ngữ. Không phát hiện tràn công thức, mã TeX chưa render, MathML phụ trợ hiện ra hoặc lỗi JavaScript trong phạm vi kiểm tra.
- Lượt kiểm tra phông dự phòng ban đầu không được dùng làm chứng nhận cuối. Môi trường HMR riêng được sửa quyền đọc thư mục phông rồi kiểm lại. Không chạy build toàn cục tại máy người dùng.
- Kiểm cấu trúc bài, kiểm thử skill và bộ kiểm thử kho mã được thực hiện riêng. Bản ghi JSON đi kèm lưu số đếm công thức và phạm vi.

## Giới hạn và công việc tiếp theo

Các chương 40–44 chưa hoàn tất. Chưa chứng nhận toàn bộ bài của cả hai môn đáp ứng mọi quy tắc mới. Những công thức cũ và hiệu năng DOM của các trang bài tập lớn vẫn cần lượt rà riêng. Build và triển khai toàn bộ chỉ chạy trên GitHub Actions sau khi push.

Các tác vụ Antigravity được giới hạn phạm vi tệp và số lượt. Những báo cáo tự nhận hoàn tất nhưng không khớp đề thật đã bị loại. Tác vụ lỗi không được coi là thành công. Các worktree được giữ lại, còn bản tích hợp được sửa và kiểm bởi tác vụ chính.
