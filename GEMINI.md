<!-- Tương thích với Google Antigravity & Gemini CLI -->
<!-- Xem tài liệu đầy đủ tại AGENTS.md -->

# StudyHub Guidelines (Gemini & Antigravity)

Vui lòng tuân theo hướng dẫn chi tiết tại [AGENTS.md](./AGENTS.md).

### Các Skill chính có thể kích hoạt:
- `.agents/skills/studyhub-lecture`: Soạn, chỉnh sửa, rà soát bài giảng, catalog, wiki, xuất slide deck.
- `.agents/skills/textbook-passage-explainer`: Giảng giải chi tiết đoạn giáo trình, công thức, kèm học trong chat.
- `.agents/skills/web-design-reviewer`: Kiểm tra và sửa lỗi giao diện, responsive, layout.

### Quy tắc định dạng toán học & Chống thanh cuộn (No Math Scrollbars):
- **Không scrollbar**: Tuyệt đối không để công thức xuất hiện thanh cuộn ngang trên cả desktop và mobile.
- **Bẻ dòng công thức dài**: Mọi biểu thức hoặc chuỗi biến đổi dài phải bẻ dòng bằng `\begin{aligned}...\end{aligned}`, ngắt tại dấu bằng ($=$), bất đẳng thức ($\le, \ge, \approx, \implies$) hoặc toán tử ($+, -$) bằng `\\` và căn lề bằng `&`.
- **Tách văn xuôi khỏi Math**: Không nhét văn xuôi nhận xét vào trong khối toán LaTeX bằng `\text{...}`.
- **Giới hạn inline**: Công thức nội dòng `$…$` tối đa 38ex. Quá dài phải chuyển sang khối `$$...$$` riêng.

### Lệnh kiểm thử tiêu chuẩn:
```sh
npm run ci:build
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
```

