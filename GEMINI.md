<!-- Tương thích với Google Antigravity & Gemini CLI -->
<!-- Xem tài liệu đầy đủ tại AGENTS.md -->

# StudyHub Guidelines (Gemini & Antigravity)

Vui lòng tuân theo hướng dẫn chi tiết tại [AGENTS.md](./AGENTS.md).

### Các Skill chính có thể kích hoạt:
- `.agents/skills/studyhub-lecture`: Soạn, chỉnh sửa, rà soát bài giảng, catalog, wiki, xuất slide deck.
- `.agents/skills/textbook-passage-explainer`: Giảng giải chi tiết đoạn giáo trình, công thức, kèm học trong chat.
- `.agents/skills/web-design-reviewer`: Kiểm tra và sửa lỗi giao diện, responsive, layout.

### Lệnh kiểm thử tiêu chuẩn:
```sh
npm run ci:build
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
```
