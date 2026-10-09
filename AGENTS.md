# StudyHub (UET) — Hướng Dẫn Chung Cho Mọi Trợ Lý AI (AI Agents)

Tài liệu này là quy ước tiêu chuẩn (Agent Instruction Standard) dành cho mọi hệ thống AI (Claude, Antigravity/Gemini, OpenAI Codex, Cursor, Windsurf, OpenCode, Cline, Roo Code, v.v.) khi làm việc trong kho lưu trữ StudyHub.

---

## 1. Giới Thiệu Dự Án

- **Bản chất**: Website tài liệu và bài giảng ôn tập dựa trên VitePress dành cho sinh viên trường Đại học Công nghệ (UET) - ĐHQGHN.
- **Ngôn ngữ**: Toàn bộ nội dung bài học bằng tiếng Việt chuẩn mực học thuật, tự nhiên, không khẩu hiệu.
- **Cấu trúc 1 bài giảng trên site** gồm 4 thành phần liên kết:
  1. **Notes**: Giáo trình chi tiết (`docs/<môn>/bai-giang/<slug>.md`).
  2. **Slides**: Bộ thẻ ôn tập nhanh trên web (`docs/.vitepress/course-catalog.mjs`).
  3. **Cheatsheet**: Tờ tra cứu nhanh công thức, quy tắc, cú pháp và bẫy thi (`docs/.vitepress/cheatsheets.mjs`).
  4. **Kiến thức nền (Prerequisites & Wiki)**: Liên kết khái niệm (`prerequisites` trong bài) → danh mục (`docs/.vitepress/concepts.mjs`) → trang Wiki chi tiết (`docs/wiki/<id>.md`).
- **Tài liệu nguồn gốc**: Lưu tại `raw_materials/<môn>/`.

---

## 2. Danh Mục Skills Tiêu Chuẩn Cho Mọi AI

Tất cả các kỹ năng (Skills) đã được chuẩn hóa theo định dạng **Agent Skills Standard** và đặt tại thư mục `.agents/skills/` (đồng thời liên kết với `.claude/skills/` để tương thích ngược 100% với Claude Code).

| Tên Skill | Vị Trí Lưu Trữ | Khi Nào Sử Dụng |
| :--- | :--- | :--- |
| **`studyhub-lecture`** | `.agents/skills/studyhub-lecture/` | Soạn bài mới, sửa/nâng cấp bài giảng, rà soát chất lượng (review), bổ sung thuật ngữ Wiki, hoặc xuất bộ slide trình chiếu PDF/PPTX. |
| **`textbook-passage-explainer`** | `.agents/skills/textbook-passage-explainer/` | Khi người dùng dán một đoạn giáo trình, công thức, slide hoặc bài tập vào chat và yêu cầu giảng giải, giải thích từng bước, hoặc kèm học/sửa bài làm. |
| **`web-design-reviewer`** | `.agents/skills/web-design-reviewer/` | Rà soát và sửa lỗi giao diện UI, responsive trên mobile, CSS, layout, tính khả dụng (a11y). |

> [!IMPORTANT]
> - Luôn đọc tài liệu `references/repo-format.md` bên trong `studyhub-lecture` trước khi chỉnh sửa bất kỳ tệp Markdown hay catalog nào của trang web.
> - Khi soạn bài hoặc giải thích có chứa phép tính số học/toán học: **bắt buộc chạy code Python tính lại**, không được đoán hoặc dựa vào trực giác.
> - **Tuyệt đối không để xuất hiện thanh cuộn (scrollbar) trên công thức toán**: Công thức hiển thị dài phải bẻ dòng bằng `\begin{aligned}` với `\\` và `&`; công thức inline không quá 38ex.

---

## 3. Các Lệnh Kiểm Thử & Xác Minh Bắt Buộc

Mọi AI khi thực hiện thay đổi nội dung hoặc mã nguồn phải chạy các lệnh kiểm tra sau từ thư mục gốc của repo:

```bash
# 1. Cài đặt dependency (nếu môi trường mới)
npm ci

# 2. Chạy máy chủ dev cục bộ
npm run dev

# 3. Đồng bộ & build VitePress (bắt buộc exit 0 trước khi hoàn tất)
npm run ci:build

# 4. Kiểm tra toàn diện liên kết catalog, Wiki, ảnh, cú pháp Markdown
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all

# 5. Chạy bộ 28 bài kiểm thử tự động của skill
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
```

---

## 4. Nguyên Tắc Sư Phạm Cốt Lõi ("Giảng Như Giáo Sư")

1. **Bắt đầu từ vấn đề thực tế**: Đi từ câu hỏi hoặc bài toán cụ thể mà khái niệm giải quyết, không bắt đầu bằng định nghĩa trơ trụi.
2. **Chính xác tuyệt đối**: Giữ đúng giả thiết, miền xác định, lượng từ, đơn vị đo lường và chiều suy luận.
3. **Mở bước khó**: Làm rõ những bước biến đổi mà người mới hay vấp ngã.
4. **Không bịa đặt**: Tuyệt đối không bịa trích dẫn, tác giả, số liệu thống kê hoặc năm tháng lịch sử.
5. **Tiếng Việt tự nhiên**: Hành văn sáng sủa, thuần Việt, tránh câu cú dịch máy thô cứng.
6. **Chủ quyền bài giảng (Chính danh, biến tri thức thành bài giảng độc lập)**: Bài giảng của StudyHub là giáo trình giảng dạy độc lập, hoàn chỉnh của chính người giảng viên. Tuyệt đối không để bài giảng mang tính chất sổ tay trích dẫn hay đối chiếu sách thụ động. Nghiêm cấm các cụm từ: *“Ảnh lấy từ sách”*, *“ảnh nguyên gốc sách”*, *“hình trong sách”*, *“dữ liệu này từ…”*, *“theo sách…”*, *“sách dùng…”*, *“nguyên tác…”*, *“bản dịch của…”*, *“tiến độ bản dịch…”*. Mọi tư liệu, hình ảnh, ví dụ, bài tập phải trở thành một phần tự nhiên của bài giảng (*“Hình 1.1: …”*, *“Xét bài toán thực tế sau:…”*, *“Quan sát đồ thị chuyển trạng thái…”*).
7. **Văn phong giáo sư và nhà ngôn ngữ tiếng Việt đại tài**: Dùng từ ngữ tiếng Việt chuẩn xác, giàu tính sư phạm, uyên bác và dễ hiểu, không “giả trân”, không sáo rỗng kiểu AI. Các mẹo tư duy, trực giác thuật toán được lồng ghép tự nhiên (*“Một cách người ta hay dùng trong thực tế để…”*, *“Để không bao giờ nhầm lẫn ở bước này…”* thay vì đóng khung máy móc *“Mẹo thú vị:”*). Luôn gắn kết lý thuyết trừu tượng với các ứng dụng thực tế sinh động trong đời sống và đặt câu hỏi đào sâu bản chất vấn đề.
8. **Chuẩn mực toán học & Chống tràn / Tuyệt đối không xuất hiện thanh cuộn (No Math Scrollbars)**:
   - Mọi công thức, phương trình, hàm số toán học hiển thị (`$$...$$`) và nội dòng (`$...$`) phải được format chính xác, thẩm mỹ, tuyệt đối không xuất hiện thanh cuộn ngang (scrollbar) trên bất kỳ kích cỡ màn hình nào (kể cả di động ~360px–375px hay trong các hộp `::: info`, `::: details`).
   - Với công thức hiển thị: Chủ động bẻ dòng bằng `\begin{aligned}...\end{aligned}`, ngắt dòng bằng `\\` tại dấu bằng, dấu bất đẳng thức ($=$, $\le$, $\ge$, $\approx$, $\implies$) hoặc phép toán ($+$, $-$) và căn lề bằng `&`. Không viết chuỗi đẳng thức trải dài trên một dòng đơn.
   - Tuyệt đối không nhét văn xuôi, câu nhận xét dài vào trong TeX bằng `\text{...}`. Văn xuôi phân tích phải viết ở đoạn văn bên ngoài khối toán.
   - Dấu mở `$$` và đóng `$$` phải luôn nằm trên một dòng riêng biệt, không dính liền với nội dung công thức hay đoạn văn xuôi.
   - Công thức inline (`$...$`): Không vượt quá 38ex; nếu dài hoặc phức tạp, bắt buộc tách thành khối `$$...$$` riêng.
