# Khôi phục đầy đủ khung hình chương 25–26

Status: READY_FOR_AGY

Tác vụ G: Chỉ chuẩn bị và kiểm chứng ảnh ứng viên cho các lỗi khung đã được xem thực tế ở chương 25–26. Worktree riêng C:/Users/Ai/.codex/worktrees/physics1-10-theory-a-20261022/StudyHub, HEAD 638bd13613f82ddc24c055dc1fcdbaf0672fb42b, trạng thái nguồn sạch. Chỉ sở hữu qa/physics25-26-frame-candidates-G-20261101/**. Không sửa bất kỳ ảnh, Markdown, module, recipe, manifest hoặc Git nào.

Đọc biên bản đang có ở C:/Users/Ai/.codex/worktrees/physics-final-acceptance-20261031/StudyHub/qa/physics-final-20261101/p2-25-32-images-gpt/review.json. Chỉ lấy records.chapter thuộc 25,26 và frameVerdict bắt đầu confirmed. Đóng băng danh sách đầu vào trong QA trước khi làm vì tác giả khác tiếp tục rà các chương sau. Những nhận xét này là ứng viên cần kiểm lại, không phải mệnh lệnh bắt buộc mở rộng khung.

PDF gốc: C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/raw_materials/physics/source/young-freedman-15.pdf. Byte ảnh và recipe chỉ được dùng khi khớp manifest ở C:/Users/Ai/.codex/worktrees/physics2-private-fixes-20261029/studyhub-course.json, cho phép khác đúng LF/CRLF đối với văn bản. Bản mới 16ebff5918877b0f5f61f9c99faf6205cba3e4b0 chưa đổi chương 25–26. Tệp còn giữ ở cache dùng chung hoặc worktree cũ chỉ đọc.

Mỗi ảnh cần xem cạnh vùng PDF mở rộng, xác nhận nét in thật sự bị mất hoặc văn xuôi ngoài hình bị cắt dở. Khung mới phải giữ toàn bộ hình, nhãn, dấu, dây dẫn, đầu trục, mũi tên và tiểu hình. Không thêm khoảng trắng chỉ để đẹp, không dựa riêng vào bounding box phông hoặc việc khớp pixel. Nếu một hình sát văn xuôi, chọn vùng đủ nguyên vẹn và giải thích đánh đổi. Không tự xóa nội dung thuộc hình. Ảnh ứng viên chỉ là render PDF gốc ở đúng mức phóng của recipe, tuyệt đối không vẽ lại.

Ghi candidates.json: Mỗi key, SHA ảnh trước, recipe và trang PDF, tọa độ cũ/mới, mức phóng, hash ảnh ứng viên, lý do cụ thể, ảnh ngữ cảnh và bằng chứng đã thực sự xem sau render. Nếu không kiểm được trực quan, ghi chưa đạt thay vì gắn cờ đúng. Giữ mọi ứng viên và nguồn QA. Python kiểm lại hình ứng viên đúng pixel của vùng PDF. Parent xem, sửa nguồn và xuất bản riêng.

Không chạy build, dev, cài phụ thuộc, tải trình duyệt, network/fetch, đổi tài khoản, đọc bí mật, commit/push/deploy hoặc dọn tệp. Không dùng workflow research. Lưu git status, HEAD và worktree list trước/sau để bảo vệ trạng thái gốc. Người dùng đã yêu cầu dùng nhiều Antigravity và cho phép tự cấp quyền trong các tác vụ dự án giới hạn tin cậy, dangerously_skip_permissions=true. Tối đa một lượt đầu và hai lượt sửa có bằng chứng. Không báo hoàn tất toàn bộ môn học từ tác vụ này.
