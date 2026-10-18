Status: IMPLEMENTED_AND_INDEPENDENTLY_VERIFIED

# Sửa tiêu đề và viền bài tập

Người dùng yêu cầu gọi Antigravity sửa nhãn hiển thị thành
`Bài tập n: Đề bài`, không có dạng `Bài tập: Bài tập 1: ...`,
và bỏ đường viền vàng dọc phần bài tập.

Worktree tin cậy: `C:/Users/Ai/.codex/worktrees/data-course-20261018-b`.
Đã đồng bộ các file giao diện cần sửa từ main để giữ thay đổi mới nhất.

Antigravity sở hữu:
- `scripts/build/markdown-presentation.mjs`
- `src/app/styles/lecture.css`
- `scripts/verify-lecture-containers.mjs`
- `scripts/build/exercise-containers.mjs` nếu cần tách helper
- `scripts/tests/exercise-titles.test.mjs` nếu cần kiểm hồi quy
- `qa/data-exercise-ui/**`

File `scripts/build/responsive-tables.mjs` được chép làm phụ thuộc chỉ đọc.
Tất cả file khác và repo main chỉ được đọc. Không push, deploy, commit,
xóa dữ liệu, đọc thông tin bí mật hay build toàn site.

Đầu ra phải giữ nguyên đề, lời giải, anchor, bảng và code. Nhãn có sẵn
số bài phải giữ đúng số và tên đề. Tạo class ngữ nghĩa cho bài tập nếu cần
để bỏ riêng viền của bài tập, không xóa viền các cảnh báo khác.

Chạy kiểm container và kiểm nhãn không lặp. Codex sẽ xem diff, ghép thay
đổi và kiểm trực tiếp ở 360/1280 px trên dev server chính.

Quyền công cụ đầy đủ đã được người dùng cho phép trong đúng ba worktree
-a, -b, -c và phạm vi soạn/rà môn này, tiếp tục xác nhận khi yêu cầu sửa
nhãn/viền ngày 18/10/2026. `dangerously_skip_permissions=true`.

## Kiểm nhận

Antigravity viết helper, tích hợp renderer, CSS và kiểm hồi quy trong worktree
B. Lời gọi `d7706fcd054c4cf7b0603e87dac738c4` hết thời gian sau 1200 giây,
nhưng các file đã được tạo. Giữ worktree và phân loại lời gọi là timeout.
Codex tự đọc diff, bổ sung xử lý tiền tố lặp trong nguồn và bỏ qua code fence,
rồi chạy độc lập 50 ca container cùng bộ kiểm tiêu đề thực trên VitePress.

Đã xem trực tiếp trang NumPy ở 360 và 1280 px. Các nhãn không còn lặp,
viền bài tập bằng 0 px, viền cảnh báo thông thường vẫn là 3 px. Các ID bài,
đề, lời giải và nội dung code được giữ. Dependency của B dùng junction
node_modules tới main để kiểm tra, không cài thêm package.
