# Đối chiếu bằng chứng hoàn tất Vật lý 2

Status: READY_FOR_AGY

Chỉ dịch và soát lỗi trong phạm vi đã giao. Không áp dụng workflow nghiên cứu, không tạo nghiên cứu mới hay mở thêm yêu cầu ngoài yêu cầu hiện có.

- Tác vụ D: Chương 21, 24–32. Worktree C:/Users/Ai/.codex/worktrees/physics1-remaining-ch01-theory-20261023/StudyHub. Chỉ ghi qa/physics2-evidence-D-20261101/**.
- Tác vụ E: Chương 33–44. Worktree C:/Users/Ai/.codex/worktrees/physics1-ch17-theory-review-20261023/StudyHub. Chỉ ghi qa/physics2-evidence-E-20261101/**.

Hai worktree cũ có nội dung chưa xuất bản. Toàn bộ tệp đang có phải giữ nguyên. Tệp ngoài thư mục QA riêng đều chỉ đọc. Không commit, fetch, push, deploy, build, chạy dev, cài phụ thuộc, tải trình duyệt, đổi tài khoản, đọc bí mật hoặc xóa tệp.

Bản ghim nội dung Vật lý 2: d805e1a00ba74fa210d5ab4802330481e497e99d. Manifest tại C:/Users/Ai/.codex/worktrees/physics2-private-fixes-20261029/studyhub-course.json. Tệp còn giữ tại C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub hoặc cache dùng chung chỉ được làm nguồn của bản ghim khi SHA256 khớp, cho phép khác CRLF/LF đối với văn bản. PDF nằm trong physics1-priority-20261022/StudyHub/raw_materials/physics/source/young-freedman-15.pdf.

Phạm vi chính là nối các lượt rà thực sự đã hoàn thành với bản đang dùng, không lặp công việc vì tên trạng thái trong bảng cũ. Đọc bảng qa/physics-final-20261031/remaining-acceptance-inventory/matrix.json trong worktree công khai physics-final-acceptance-20261031/StudyHub và các biên bản parent đã chỉ tới. Không nhận lời báo cáo của tác giả hoặc cờ true làm chứng nhận độc lập.

Với từng chương, đối chiếu nguồn lý thuyết, ví dụ/tự kiểm, hình gốc/chú thích, bài cuối chương và Cheatsheet/Wiki với đúng phạm vi biên bản. Giữ mọi nghiệm thu đã đạt, chỉ liệt kê delta hoặc phần thật sự thiếu bằng chứng. Đặc biệt không suy đủ khung hình từ việc ảnh khớp một vùng cắt PDF. Nếu biên bản parent thật sự đã xem đầy đủ khung, nối nguyên byte ảnh và ngữ cảnh chú thích/module nhãn. Nếu chưa có bằng chứng ấy, ghi rõ chưa đạt hoặc xem trực tiếp khung cạnh vùng PDF mở rộng trong đúng chương để đưa ra kết luận.

Mọi kết luận đã đạt cần tệp bằng chứng, commit đầy đủ thực sự tồn tại, hash đối chiếu và phạm vi. Không lấy commit xóa tệp để làm commit nghiệm thu. Không bịa hash hoặc đoán ID Wiki. Phải tìm đúng dữ liệu Cheatsheet đang được course dùng, không kiểm riêng bản cũ đã bị ghi đè.

Các chương 43–44 đã có đợt khôi phục và đọc nguồn độc lập ngày 31/10–1/11. Dùng báo cáo công khai hiện tại và kho QA đã nén trong bản ghim để giữ kết quả đó, không yêu cầu soạn lại. Ảnh chương 22–23 đã được sửa và kiểm web riêng nên nằm ngoài hai tác vụ này.

Ghi review.json gồm từng chương/tiêu chí, verdict có phạm vi, bằng chứng đã đọc, phép so hash đã chạy, delta và vấn đề nguồn xác nhận nếu có, giới hạn còn mở. Dùng Python đã có. Không cần chạy build hoặc kiểm web đã đạt nếu byte không đổi. Ghi git status, rev-parse HEAD và worktree list trước/sau, giữ dirty baseline. Permission dangerously_skip_permissions=true theo ủy quyền rõ ràng đã có của người dùng cho các tác vụ giới hạn tin cậy trong dự án. Mỗi tác vụ tối đa ba lượt, Codex rà kết quả trước khi nhận.
