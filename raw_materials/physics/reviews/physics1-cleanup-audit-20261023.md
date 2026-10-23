# Báo Cáo Rà Soát & Kiến Nghị Dọn Dẹp Tệp (Physics 1 Cleanup Audit)
**Ngày thực hiện**: 23/10/2026
**Phạm vi**: Đợt biên tập Vật lý đại cương 1 (Physics 1: Chương 09, 10, 11, 17, 18, 19, 20)
**Tệp sở hữu duy nhất**: `raw_materials/physics/reviews/physics1-cleanup-audit-20261023.md` (Toàn bộ các tệp khác là bất biến)
**Quy chế**: Báo cáo kiểm định chỉ đọc (Report-only), không xóa trực tiếp, tuân thủ nguyên tắc không xóa ảnh gốc, bài giảng hoàn chỉnh, bộ kiểm chứng số học (verifiers), kịch bản trích xuất ảnh tái lập và bằng chứng nghiệm thu.

---

## 1. Phương Pháp & Lệnh Kiểm Tra Thực Tế

Quá trình kiểm tra sử dụng các lệnh chuẩn theo quy định:
1. `git status --short`:
   - Kết quả: Working tree sạch, không có tệp thừa ngoài luồng.
2. `git ls-files <paths>`:
   - Xác minh sự tồn tại chính xác của 10 tệp được kiểm tra trong chỉ mục Git.
3. `bounded rg references`:
   - Tra cứu chéo các liên kết trực tiếp, tham chiếu gián tiếp qua `raw_materials/physics/translation-manifest.json`, catalog `docs/.vitepress/physics-courses.mjs`, và các kịch bản thực thi.
4. `git diff --check`:
   - Kết quả: Mã thoát `0`, không có khoảng trắng thừa hay lỗi cú pháp diff.

---

## 2. Bảng Tổng Hợp 10 Tệp Đã Kiểm Định

| STT | Đường Dẫn Chính Xác (Tracked Path) | Phân Loại | Bằng Chứng Tra Cứu (Reference Evidence) | Khuyến Nghị |
| :--- | :--- | :--- | :--- | :---: |
| 1 | `raw_materials/physics/reviews/physics1-thermal-parent-progress-20261022.md` | Báo cáo tiến độ tạm thời cũ | 0 tham chiếu trong `docs/`, `scripts/`, `raw_materials/`. Văn bản ghi rõ: *"This is a historical private progress record. Current status is recorded in physics1-priority-status-20261023.md."* | **RELOCATE** / **REMOVE** |
| 2 | `raw_materials/physics/chapter-02-task-list.md` | Danh sách tác vụ cục bộ đã xong | 0 tham chiếu trong toàn bộ mã nguồn. Là danh mục 10 dòng kiểm tra tác vụ hoàn tất của chương 2 để ở thư mục gốc `raw_materials/physics/`. | **RELOCATE** / **REMOVE** |
| 3 | `raw_materials/physics/reviews/physics1-priority-status-20261023.md` | Báo cáo trạng thái nghiệm thu hiện hành | Ghi nhận trạng thái hoàn tất chương 9, 18, tiến độ chương 19 và các chương còn lại của đợt Physics 1. Được tham chiếu bởi báo cáo trước làm nguồn chuẩn. | **KEEP** |
| 4 | `raw_materials/physics/chapter-09-review.json` | Hồ sơ kiểm chuẩn nội dung | Tham chiếu trực tiếp trong `raw_materials/physics/translation-manifest.json` tại mục `manifest.chapters[sourceChapter == 9].completionReview`. Không được coi là tệp mồ côi. | **KEEP** |
| 5 | `scripts/sync-physics1-priority.mjs` | Công cụ đồng bộ bài giảng & catalog | Công cụ sinh nội dung tái lập (reproducible generator), phân giải AST của `docs/.vitepress/physics-courses.mjs`, cập nhật Slides, Notes cho các chương 9, 10, 11, 17, 18, 19, 20. | **KEEP** |
| 6 | `scripts/sync-physics1-priority-wiki.mjs` | Công cụ đồng bộ kiến thức nền & Wiki | Công cụ sinh nội dung tái lập, đồng bộ khái niệm và liên kết từ `docs/.vitepress/physics1-priority-foundations.mjs` sang hệ thống Wiki. | **KEEP** |
| 7 | `scripts/prepare-physics1-09-theory-a-assets.py` | Kịch bản cắt ảnh PDF tái lập | Trích xuất và căn chỉnh pixel chuẩn RGB từ `young-freedman-15.pdf` sang `docs/vat-ly-1/bai-giang/img/young-09/`. Tham chiếu trong `raw_materials/physics/verify_chapter09_theory_a.py`. | **KEEP** |
| 8 | `raw_materials/physics/verify_chapter11_theory_a.py` | Bộ kiểm chứng số học & hình ảnh | Kiểm chứng độc lập các Ví dụ 11.1–11.4 và TYU 11.1–11.3. Có tham chiếu đường dẫn tuyệt đối máy trạm `C:/Users/Ai/.../measure-math.mjs` tại dòng 343 cần sửa thành đường dẫn tương đối. | **KEEP** *(cần sửa path)* |
| 9 | `raw_materials/physics/verify_chapter20_theory_b.py` | Bộ kiểm chứng số học & hình ảnh | Kiểm chứng độc lập các Ví dụ 20.5–20.8 và chu trình Carnot/entropy. Có tham chiếu đường dẫn tuyệt đối máy trạm `C:/Users/Ai/.../measure-math.mjs` tại dòng 37 cần sửa thành tương đối. | **KEEP** *(cần sửa path)* |
| 10 | `docs/agy-plans/2026-10-23-physics1-cleanup-audit.md` | Kế hoạch kiểm định dọn dẹp | Kế hoạch phân định ranh giới tác vụ hiện hành (`READY_FOR_AGY`), lưu trữ ràng buộc ủy quyền và hợp đồng đầu ra. | **KEEP** |

---

## 3. Phân Tích Chi Tiết Từng Tệp

### 3.1. `raw_materials/physics/reviews/physics1-thermal-parent-progress-20261022.md`
- **Thực trạng**: Đây là bản ghi chép tiến độ làm việc ngày 22/10/2026 giữa các tác vụ phân tán. Ngay phần đầu tệp nêu rõ tệp đã bị thay thế bởi `physics1-priority-status-20261023.md`.
- **Kết quả tra cứu**: Lệnh `rg "physics1-thermal-parent-progress-20261022" docs/ scripts/ raw_materials/` trả về mã thoát `1` (0 kết quả tham chiếu).
- **Khuyến nghị**: **RELOCATE** vào kho lưu trữ lịch sử (`raw_materials/physics/reviews/archive/`) hoặc **REMOVE** nếu parent agent xác nhận toàn bộ số liệu đối chiếu đã được tổng hợp đầy đủ vào `physics1-priority-status-20261023.md`.

### 3.2. `raw_materials/physics/chapter-02-task-list.md`
- **Thực trạng**: Tệp danh mục tác vụ 10 dòng của chương 2 (chương đã hoàn thành từ các đợt trước) nằm rời rạc tại thư mục gốc `raw_materials/physics/`.
- **Kết quả tra cứu**: Lệnh `rg "chapter-02-task-list" scripts/ docs/ raw_materials/` trả về mã thoát `1` (0 kết quả tham chiếu).
- **Khuyến nghị**: **RELOCATE** sang `raw_materials/physics/reviews/` để gom nhóm các tài liệu đánh giá, hoặc **REMOVE** nếu quy trình bàn giao chương 2 không còn yêu cầu giữ checklist tạm.

### 3.3. `raw_materials/physics/reviews/physics1-priority-status-20261023.md`
- **Thực trạng**: Hồ sơ tổng hợp kết quả nghiệm thu chính thức của toàn bộ đợt Physics 1 (chương 9, 18 hoàn tất; chương 19 đang rà soát; chương 10, 11, 17, 20 đang hoàn thiện).
- **Kết quả tra cứu**: Là bằng chứng nghiệm thu (audit evidence) cốt lõi của repo hiện tại.
- **Khuyến nghị**: **KEEP**. Tuyệt đối không xóa theo nguyên tắc bảo toàn bằng chứng đánh giá.

### 3.4. `raw_materials/physics/chapter-09-review.json`
- **Thực trạng**: Tệp cấu trúc JSON lưu trữ kết quả kiểm tra tính toàn vẹn ảnh nguồn, ledger số học của chương 9.
- **Kết quả tra cứu**: Được khai báo trực tiếp trong `raw_materials/physics/translation-manifest.json` (`"completionReview": "raw_materials/physics/chapter-09-review.json"`).
- **Khuyến nghị**: **KEEP**. Không được hiểu nhầm là tệp thừa khi không xuất hiện trong Markdown, vì tệp này nằm trong schema quản lý của manifest.

### 3.5. `scripts/sync-physics1-priority.mjs`
- **Thực trạng**: Kịch bản tự động đồng bộ hóa nội dung bản dịch sang cấu trúc VitePress (`docs/vat-ly-1/bai-giang/`), đồng thời chèn Metadata, liên kết Slides và Cheatsheet.
- **Kết quả tra cứu**: Được kiểm thử và sử dụng xuyên suốt trong commit `de02d44d`.
- **Khuyến nghị**: **KEEP**. Là kịch bản tái lập cần thiết phục vụ bảo trì và cập nhật các chương Physics 1.

### 3.6. `scripts/sync-physics1-priority-wiki.mjs`
- **Thực trạng**: Kịch bản nạp và đồng bộ thuật ngữ, định nghĩa, liên kết khái niệm cho môn Vật lý 1 từ `docs/.vitepress/physics1-priority-foundations.mjs`.
- **Kết quả tra cứu**: Cung cấp cơ sở dữ liệu tri thức Wiki phục vụ tooltip và navigation của Physics 1.
- **Khuyến nghị**: **KEEP**. Kịch bản sinh dữ liệu nền tảng bắt buộc phải giữ lại.

### 3.7. `scripts/prepare-physics1-09-theory-a-assets.py`
- **Thực trạng**: Kịch bản Python đọc tệp gốc PDF `young-freedman-15.pdf`, thực hiện phép crop toạ độ chính xác, nén ảnh PNG phục vụ bài giảng lý thuyết 9.1–9.3.
- **Kết quả tra cứu**: Được tham chiếu bởi bộ kiểm thử `raw_materials/physics/verify_chapter09_theory_a.py`.
- **Khuyến nghị**: **KEEP**. Thuộc diện kịch bản trích xuất ảnh tái lập được bảo vệ nghiêm ngặt.

### 3.8. `raw_materials/physics/verify_chapter11_theory_a.py`
- **Thực trạng**: Kịch bản kiểm chứng số học và ảnh cho chương 11 Lý thuyết A.
- **Phát hiện bất thường**: Tại dòng 343 có đoạn:
  `measure_script = Path("C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs")`
  Đường dẫn này trỏ tuyệt đối tới một worktree tạm thời từ ngày 22/10/2026 (`physics1-priority-20261022`). Khi worktree cũ bị xóa, bước kiểm tra `test_math_measure()` sẽ báo lỗi `AssertionError: measure-math.mjs missing`.
- **Khuyến nghị**: **KEEP**. Thuộc diện bộ kiểm chứng số học (verifiers) không được xóa. Kiến nghị parent agent sửa đường dẫn thành đường dẫn tương đối trong repo hoặc kiểm tra điều kiện tồn tại mềm.

### 3.9. `raw_materials/physics/verify_chapter20_theory_b.py`
- **Thực trạng**: Kịch bản kiểm chứng số học và ảnh cho chương 20 Lý thuyết B.
- **Phát hiện bất thường**: Tương tự như chương 11, tại dòng 37 chứa đường dẫn máy trạm:
  `script = "C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs"`
- **Khuyến nghị**: **KEEP**. Cần giữ lại để bảo toàn các phép tính Carnot và entropy, đồng thời chuyển đổi đường dẫn máy trạm sang đường dẫn nội bộ dự án.

### 3.10. `docs/agy-plans/2026-10-23-physics1-cleanup-audit.md`
- **Thực trạng**: Tài liệu phân công tác vụ và kế hoạch kiểm định độc lập của đợt dọn dẹp này.
- **Kết quả tra cứu**: Chứa hợp đồng phạm vi, danh mục cấm và tiêu chí nghiệm thu được tạo bởi người dùng/parent agent.
- **Khuyến nghị**: **KEEP**. Cần duy trì trong `docs/agy-plans/` để làm bằng chứng quản trị quy trình và kiểm soát thay đổi.

---

## 4. Những Điểm Còn Nghi Vấn & Điểm Nghẽn (Uncertainties & Blockers)

1. **Vấn đề thư mục tạm `qa/physics1-priority`**:
   - Thư mục `qa/` nằm trong `.gitignore` và không được track trên Git. Các kịch bản sinh đồ thị và verifier (như `verify_priority_ch19_theory.py`, `verify_priority_ch20_numbered.py`, `generate-physics1-18-lj-plot.py`) ghi tệp JSON/PNG đệm vào `qa/physics1-priority/`.
   - Một số verifier cũ (`verify_chapter11_theory_a.py`, `verify_chapter20_theory_b.py`) phụ thuộc vào công cụ phụ trợ `measure-math.mjs` nằm trong thư mục `qa/` của worktree cũ.
   - **Khuyến nghị**: Di dời công cụ `measure-math.mjs` vào thư mục kịch bản được track chính thức (ví dụ: `scripts/verification/measure-math.mjs`) thay vì để trong thư mục `qa/` bị gitignore.

2. **Quyền quyết định xóa hay di dời (Relocate vs Remove)**:
   - Hai tệp `physics1-thermal-parent-progress-20261022.md` và `chapter-02-task-list.md` không còn giá trị vận hành trực tiếp. Tuy nhiên, việc xóa vĩnh viễn hay chuyển vào thư mục lưu trữ (`archive/`) thuộc quyền quyết định của parent agent trong lượt dọn dẹp hoàn nguyên tiếp theo.

---

## 5. Trạng Thái Hoàn Tất

- **Báo cáo**: Đã lập đầy đủ và lưu tại `raw_materials/physics/reviews/physics1-cleanup-audit-20261023.md`.
- **Số lượng đường dẫn kiến nghị**: Đúng 10 tệp hiện hữu, có bằng chứng đối soát rõ ràng.
- **Tính bất biến**: Toàn bộ các tệp khác trong repository không bị chỉnh sửa, xóa bỏ hoặc tạo mới ngoài phạm vi.
- **Trạng thái**: **COMPLETED (Sẵn sàng cho parent agent phê duyệt)**.
