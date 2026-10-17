Status: READY_FOR_AGY

# Biên soạn môn Lập trình xử lý dữ liệu

Ngày: 2026-10-18.

Người dùng đã cho phép Antigravity chạy công cụ không hỏi lại trong ba worktree dưới đây để biên soạn và kiểm tra môn học. Permission mode: `dangerously_skip_permissions=true`. Cấm push, deploy, truy cập thông tin bí mật, xóa dữ liệu và chạy build toàn site.

## Quy chuẩn chung

- Đọc `raw_materials/xu-ly-du-lieu/authoring-contract.json` và `source-inventory.json`.
- Biên soạn bài giảng tiếng Việt độc lập theo chủ đề chương 1–13 và phụ lục A, B của Wes. Không dịch hoặc diễn đạt lại sát toàn bộ sách, không sao chép hình hay lời văn được bảo hộ.
- IAI chỉ bổ sung kỹ thuật liên quan. Đưa đủ các bài tập minh thị vào chương phù hợp, giữ dữ kiện, viết lời giải rõ ràng và kiểm bằng Python. Phần chuyển thể IAI ghi công và giấy phép CC BY-NC-SA 4.0 trong Tài liệu tham khảo.
- Loại nội dung UET, vận hành học phần, bài tập lớn, chính sách AI đóng/mở. Không dùng notebook lecture-01. Bài 9 IAI không có trong lịch công khai.
- Dùng cấu trúc site hiện có. Giữ các slug cũ được phân công. Mục cuối là `## Tài liệu tham khảo`. Không H1 trong Notes. Frontmatter và lesson.mjs phải khớp.
- Soạn đầy đủ cơ chế, giả thiết, ví dụ, ranh giới, bài tập và lời giải gập. Không viết sổ mục lục tóm tắt thay bài giảng. Mỗi chủ đề kỹ thuật trong inventory phải có mục tương ứng hoặc lý do loại trong coverage JSON.
- Slides gồm 4–6 thẻ, cùng nội dung với Notes. Cheatsheet được site sinh từ slides. Prerequisites chỉ dùng ID trong hợp đồng.
- Đọc quy chuẩn trong `C:/Users/Ai/Documents/StudyHub/.agents/skills/studyhub-lecture/` gồm SKILL.md, references/repo-format.md, professor-voice.md, writing-vi.md, teaching-review.md. Các file này chỉ đọc.

## Quyền sở hữu

Mỗi agent chỉ được sửa Notes `docs/xu-ly-du-lieu/bai-giang/<slug>.md` và module `src/content/courses/xu-ly-du-lieu/lectures/<slug>/{lesson,slides}.mjs` có group tương ứng trong authoring-contract.json. Được tạo `scripts/verify-data-course-<group>.py` và `raw_materials/xu-ly-du-lieu/coverage-<group>.json`.

- A: `C:/Users/Ai/.codex/worktrees/data-course-20261018-a`. Chương 1–5 và phụ lục B.
- B: `C:/Users/Ai/.codex/worktrees/data-course-20261018-b`. Chương 6–10.
- C: `C:/Users/Ai/.codex/worktrees/data-course-20261018-c`. Chương 11–13 và phụ lục A.

Codex giữ quyền sửa course.mjs, các redirect cũ, source-map, authoring-map, bộ kiểm tổng thể và tích hợp. Cấm sửa file ngoài phạm vi, cấm sửa plan, cấm cài dependency, cấm sửa node_modules (có thể dùng dependency repo chính ở chế độ chỉ đọc). Cấm sửa worktree chính và worktree của agent khác.

## Nghiệm thu và kiểm tra

- Đọc đầy đủ nguồn được giao trong cache chỉ đọc `C:/Users/Ai/AppData/Local/Temp/studyhub-data-sources/`. Đọc nguồn IAI theo ánh xạ trong hợp đồng, không chỉ đọc tiêu đề.
- Chạy Python tính lại tất cả ví dụ và đáp án, ghi thành script có assertion thực chất.
- Kiểm module bằng Node. Codex chạy check_lecture sau khi tích hợp catalog.
- Chạy rà văn phong. Báo cụ thể sửa từ/câu nào, không tự cấp chứng nhận chung chung.
- Sau khi tích hợp, Antigravity sẽ được giao lượt kiểm render/LaTeX/font qua dev server, desktop và mobile. Không báo đã render nếu chưa xem bằng trình duyệt.
- Chạy `git diff --check`, `git diff --name-only`, `git status --short`. Không tự commit. Báo files, test output, trạng thái, blocker và lỗi quyền.

## Điểm dừng

Dừng khi đủ tiêu chí, gặp lỗi quyền/xác thực, timeout, hoặc cần thay phạm vi. Mỗi task tối đa một lần gọi đầu và hai lần sửa theo bằng chứng.
