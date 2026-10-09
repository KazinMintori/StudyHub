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
- **Khai triển tường minh trước khi viết tắt**: Mọi công thức dùng ký hiệu dồn ($\sum, \prod, \dots$) phải được khai triển tường minh ít nhất một lần (ví dụ $\sum_{i=1}^k \theta_i = \theta_1 + \dots + \theta_k = 1$ với $\theta_i \ge 0$), nêu rõ miền chỉ số, trực giác bản chất và trường hợp cơ sở $k=2$.
- **Tách văn xuôi khỏi Math**: Không nhét văn xuôi nhận xét vào trong khối toán LaTeX bằng `\text{...}`.
- **Giới hạn inline**: Công thức nội dòng `$…$` tối đa 38ex. Quá dài phải chuyển sang khối `$$...$$` riêng.

### Chuẩn mực văn phong & Từ nối tiếng Việt:
- **Hạn chế dấu chấm phẩy (`;`)**: Trong lời giảng văn xuôi, hạn chế tối đa dấu `;`. Thay thế bằng các từ nối tiếng Việt chuẩn xác (*và, nhưng, tuy nhiên, trái lại, ngược lại, vì vậy, do đó, kéo theo, dẫn đến, suy ra, hệ quả là, đồng nghĩa với...*) hoặc tách thành các câu đơn rõ ràng. Tra cứu tại `references/tu-noi-va-dien-dat.md`.
- **Tránh dịch máy (`contract` -> "hợp đồng", lạm dụng "lớp")**: Dùng *quy chuẩn cấu trúc file*, *chuẩn giao tiếp dữ liệu (schema)* thay vì "hợp đồng file/dữ liệu"; dùng *ánh xạ co* (không dùng "ánh xạ hợp đồng"); linh hoạt dùng *họ bài toán*, *dạng bài toán*, *họ hàm*, *tầng mạng* thay vì lạm dụng từ "lớp".

### Lệnh kiểm thử tiêu chuẩn:
```sh
npm run ci:build
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
```

