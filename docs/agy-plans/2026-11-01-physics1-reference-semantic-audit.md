# Kiểm chứng nội dung tra cứu Vật lý 1

Status: READY_FOR_AGY

Hai tác vụ mới kiểm chứng nghĩa của công thức và kiến thức nền. Chúng khác hai tác vụ nối bằng chứng trước đó, có handle bị mất. Không khởi động lại hoặc giả định đã nhận kết quả của các handle cũ.

## Phạm vi và quyền

Người dùng đã yêu cầu dùng Antigravity làm song song và cho phép tự cấp quyền cho các tác vụ trong dự án. Hai tác vụ này chỉ được ghi bằng chứng trong thư mục QA riêng. Không được sửa nội dung giảng dạy.

- Tác vụ A: Chương 1, 3, 4. Worktree C:/Users/Ai/.codex/worktrees/physics1-remaining-ch01-theory-20261023/StudyHub. Chỉ sở hữu các tệp trong qa/reference-semantic-A-20261101/.
- Tác vụ B: Chương 6, 7, 9, 10, 11, 17. Worktree C:/Users/Ai/.codex/worktrees/physics1-ch17-theory-review-20261023/StudyHub. Chỉ sở hữu các tệp trong qa/reference-semantic-B-20261101/.

Giữ nguyên toàn bộ sửa đổi và tệp chưa theo dõi đang có tại hai worktree. Mọi đường dẫn khác đều chỉ đọc, kể cả cache dùng chung và kho nội dung riêng.

## Nguồn có thẩm quyền

- PDF: C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/raw_materials/physics/source/young-freedman-15.pdf.
- Bản ghim Vật lý 1: ec53e79d1e8b4b2a9720aaf0cc9bb6c1edc4d1e3, manifest tại C:/Users/Ai/.codex/worktrees/physics1-private-fixes-20261031/studyhub-course.json.
- Có thể đọc byte tại C:/Users/Ai/Documents/StudyHub/.course-repositories/vat-ly-1, nhưng phải đối chiếu SHA256 với manifest, cho phép khác đúng CRLF/LF. Không lấy HEAD cache thay bản ghim.
- Nguồn Wiki đang dùng tại C:/Users/Ai/.codex/worktrees/physics-final-acceptance-20261031/StudyHub/docs/wiki/ và các module foundations công khai tương ứng.
- Cheatsheet chung: docs/.vitepress/physics1-cheatsheets.mjs thuộc bản riêng Vật lý 1. Đọc đúng export của từng chương và đúng cấu hình course hiện tại, không suy từ tên hoặc bản cũ trong worktree.

## Tiêu chí nghiệm thu

Đối chiếu tất cả các dòng của cheatsheet trong phạm vi với các mục tương ứng của PDF. Kiểm tra dấu, miền áp dụng, biến, đơn vị, giả thiết và việc chỉ chứa định nghĩa, tính chất, công thức. Đọc danh sách prerequisites thực sự của từng chương và kiểm chứng nghĩa của các mục Wiki liên quan. Không yêu cầu thêm Wiki không liên quan hoặc tự đặt điều kiện tiên quyết chỉ vì danh sách trống.

Mỗi nhận định phải chỉ tới tệp, trường hoặc dòng cụ thể và trang PDF. Phân biệt lỗi vật lý, thiếu điều kiện, thiếu nội dung cần thiết và khuyến nghị tùy chọn. Không thêm ràng buộc nghiệm thu ngoài yêu cầu người dùng. Chỉ đề xuất bản sửa có bằng chứng, không tự sửa nguồn. Chạy Python tính lại hoặc kiểm tra thứ nguyên/giới hạn cho các biểu thức được kiểm chứng. Không chỉ tìm chuỗi hoặc đếm số công thức rồi kết luận đúng.

Tệp kết quả gồm review.json và verify.py cùng kết quả chạy trong thư mục QA riêng. JSON phải có từng chương, dòng công thức đã đọc, nguồn PDF, phạm vi Wiki, hash nguồn, phát hiện cụ thể, đề xuất sửa, kiểm tra Python và giới hạn của kết luận. Không kết luận nghiệm thu ảnh, bài tập, giao diện, triển khai hoặc toàn dự án.

## Lệnh và điều cấm

Đọc AGENTS và skill studyhub-lecture. Chạy git status --short, git rev-parse HEAD, git worktree list trước và sau. Dùng C:/Users/Ai/miniconda3/python.exe -I -X utf8 và thư viện PDF đã có. Không cài phụ thuộc, không tải trình duyệt, không build, không bật dev server, không commit, push, deploy, fetch, thao tác tài khoản, đọc bí mật hoặc xóa tệp. Không thay tài khoản Antigravity.

Permission mode: dangerously_skip_permissions=true, trong đúng phạm vi được người dùng ủy quyền. Quyền công cụ không mở rộng danh sách tệp được sửa.

Tối đa một lượt đầu và hai lượt sửa có bằng chứng cho mỗi tác vụ. Dừng và ghi rõ blocker nếu không đọc được nguồn hoặc không thể chứng minh nhận định. Codex sẽ kiểm tra độc lập trước khi nhận kết quả.
