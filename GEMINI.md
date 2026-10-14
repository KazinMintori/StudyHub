<!-- Tương thích với Google Antigravity & Gemini CLI -->
<!-- Xem tài liệu đầy đủ tại AGENTS.md -->

# StudyHub Guidelines (Gemini & Antigravity)

Vui lòng tuân theo hướng dẫn chi tiết tại [AGENTS.md](./AGENTS.md).

### Các Skill chính có thể kích hoạt:
- `.agents/skills/studyhub-lecture`: Soạn, chỉnh sửa, rà soát bài giảng, catalog, wiki, xuất slide deck.
- `.agents/skills/textbook-passage-explainer`: Giảng giải chi tiết đoạn giáo trình, công thức, kèm học trong chat.
- `.agents/skills/web-design-reviewer`: Kiểm tra và sửa lỗi giao diện, responsive, layout.

### Nguyên tắc sư phạm cốt lõi & Chủ quyền bài giảng:
- **Chủ quyền bài giảng (Bài giảng độc lập, chính danh)**: Bài giảng của StudyHub là giáo trình giảng dạy độc lập, hoàn chỉnh của chính người giảng viên. Tuyệt đối không để bài giảng mang tính chất sổ tay trích dẫn hay đối chiếu sách thụ động. Nghiêm cấm các câu và cụm từ kiểu: *“Nội dung lấy từ giáo trình…”*, *“Lấy từ slide của môn…”*, *“Bài tập lấy từ sách…”*, *“Ví dụ do người soạn thêm, không gán cho tác giả giáo trình…”*, *“Ảnh lấy từ sách”*, *“ảnh nguyên gốc sách”*, *“hình trong sách”*, *“dữ liệu này từ…”*, *“theo sách…”*, *“sách dùng…”*, *“nguyên tác…”*, *“bản dịch của…”*, *“tiến độ bản dịch…”*. Mọi tư liệu, hình ảnh, ví dụ, bài tập phải trở thành một phần tự nhiên của bài giảng (*“Hình 1.1: …”*, *“Xét bài toán thực tế sau:…”*, *“Quan sát đồ thị chuyển trạng thái…”*). Mục cuối bài luôn đặt tên là `## Tài liệu tham khảo` theo đúng quy chuẩn học thuật chuẩn mực, không phân bua “do người soạn bổ sung”.
- **Bắt buộc chạy code Python kiểm tra số học**: Khi soạn bài hoặc giải thích có chứa phép tính số học, đại số ma trận, hoặc nghiệm bài toán: Bắt buộc chạy code Python tính lại, tuyệt đối không được đoán hoặc dựa vào trực giác.
- **Giảng như giáo sư**: Đi từ bài toán hoặc câu hỏi thực tế cụ thể, mở bước khó biến đổi, lồng ghép trực giác tự nhiên (*“Một cách người ta hay dùng trong thực tế để…”*, *“Để không bao giờ nhầm lẫn ở bước này…”*), loại bỏ triệt để các từ cảm tính AI (*“kỳ diệu”, “vô cùng”, “cực kỳ”, “mạnh mẽ”, “then chốt”* dùng vô căn cứ).
- **Tính trực diện và đúng bản chất của ví dụ minh họa**: Khi vừa phát biểu định nghĩa hoặc tính chất toán học, ví dụ đi kèm ngay sau đó bắt buộc phải chạm đúng vào bản chất kỹ thuật đặc thù của tính chất ấy. Không chọn ví dụ chung chung hay tầm thường; mọi ví dụ đối chứng/phản chứng phải được kiểm tra bằng code Python trước khi đưa vào bài.
- **Cấm lối viết "nghĩ thành tiếng" trong lời giải**: Lời giải bài tập phải là văn bản sư phạm mẫu mực, lập luận mạch lạc, chắc chắn và dứt khoát. Nghiêm cấm đưa vào các câu nháp tự độc thoại kiểu AI: *“Khoan đã, hãy xem lại…”*, *“À không, thay vào đó…”*, *“Ý tôi là…”*, *“Thử lại nào…”*, *“Nhầm rồi…”*.
- **Không bịa đặt tần suất lỗi sinh viên hoặc "bẫy thi cử"**: Tuyệt đối không đưa ra khẳng định cảm tính về sai sót của người học: Cấm các câu *“Sinh viên rất hay nhầm…”*, *“Lỗi phổ biến nhất là…”*, *“Đa số sinh viên đều mắc…”*, *“Bẫy thi cử cực kỳ phổ biến…”*. Hãy nêu trực diện hai cách hiểu đối lập hoặc trường hợp dễ sơ suất.

### Quy tắc định dạng toán học & Chống thanh cuộn (No Math Scrollbars):
- **Không scrollbar**: Tuyệt đối không để công thức xuất hiện thanh cuộn ngang trên cả desktop và mobile.
- **Bẻ dòng công thức dài**: Mọi biểu thức hoặc chuỗi biến đổi dài phải bẻ dòng bằng `\begin{aligned}...\end{aligned}`, ngắt tại dấu bằng ($=$), bất đẳng thức ($\le, \ge, \approx, \implies$) hoặc toán tử ($+, -$) bằng `\\` và căn lề bằng `&`.
- **Khai triển tường minh trước khi viết tắt**: Mọi công thức dùng ký hiệu dồn ($\sum, \prod, \dots$) phải được khai triển tường minh ít nhất một lần (ví dụ $\sum_{i=1}^k \theta_i = \theta_1 + \dots + \theta_k = 1$ với $\theta_i \ge 0$), nêu rõ miền chỉ số, trực giác bản chất và trường hợp cơ sở $k=2$.
- **Tách văn xuôi khỏi Math**: Không nhét văn xuôi nhận xét vào trong khối toán LaTeX bằng `\text{...}`.
- **Giới hạn inline**: Công thức nội dòng `$…$` tối đa 38ex. Quá dài phải chuyển sang khối `$$...$$` riêng.
- **Cú pháp trị tuyệt đối và chuẩn (Cấm `\vert{}`)**: Dùng trực tiếp `|x - y|` cho khoảng cách/trị tuyệt đối; dùng `\|x\|` hoặc `\lVert x \rVert_2` cho chuẩn vector. Tuyệt đối không dùng `\vert{}` hoặc `\Vert{}`.
- **Triệt tiêu hoàn toàn thanh cuộn & mũi tên scrollbar (Zero Math Scrollbars & Arrows)**: Tuyệt đối không để công thức hiển thị hoặc nội dòng xuất hiện thanh cuộn ngang/dọc hay các nút mũi tên cuộn Windows (`▴▾`) trên toàn hệ thống (Notes, Wiki, Slides, Cheatsheet, Popover). Ẩn hoàn toàn `mjx-assistive-mml`.
- **Giao diện bài giảng tinh gọn (Clean Lecture Presentation)**: Danh sách bài giảng trong `CourseOverview` chỉ hiển thị số thứ tự và tiêu đề bài giảng. Không để các thông số phụ như `X slide · Y mục hỗ trợ`, không hiển thị số lượng kiến thức nền ở header môn học, và không để dòng chú thích thừa ở chân trang môn học.

### Chuẩn mực văn phong & Dấu câu tiếng Việt:
- **Hạn chế dấu gạch ngang dài (em dash —) trong văn xuôi**: Tuyệt đối hạn chế lạm dụng dấu gạch ngang dài (`—` hoặc `--`) để chêm xen vế phụ giải thích giữa câu. Thay thế bằng các phương thức tiếng Việt chuẩn mực: Dùng dấu phẩy `,` cho vế phụ ngắn; dùng dấu ngoặc đơn `(...)` cho chú thích bổ trợ; dùng dấu hai chấm `:` khi giải thích bản chất; dùng từ nối thuần Việt (*tức là, cụ thể là, nghĩa là, đồng nghĩa với việc...*); hoặc tách câu độc lập. Chỉ dùng gạch ngang cho khoảng số/thời gian (`1945–1975`), tên định lý liên danh (*Cauchy–Schwarz*), hoặc gạch đầu dòng danh sách.
- **Hạn chế dấu chấm phẩy (`;`)**: Trong lời giảng văn xuôi, hạn chế tối đa dấu `;`. Thay thế bằng các từ nối tiếng Việt chuẩn xác (*và, nhưng, tuy nhiên, trái lại, ngược lại, vì vậy, do đó, kéo theo, dẫn đến, suy ra, hệ quả là, đồng nghĩa với...*) hoặc tách thành các câu đơn rõ ràng. Tra cứu tại `references/tu-noi-va-dien-dat.md`.
- **Kiểm soát độ dài câu & Mật độ in đậm**: Mỗi câu văn xuôi nên dưới 50–55 từ; câu quá dài phải tách thành câu đơn với chủ ngữ rõ ràng. Không in đậm 4–5 cụm trong một đoạn văn.
- **Tránh dịch máy (`contract` -> "hợp đồng", lạm dụng "lớp")**: Dùng *Quy chuẩn cấu trúc file*, *chuẩn giao tiếp dữ liệu (schema)* thay vì "hợp đồng file/dữ liệu"; dùng *ánh xạ co* (không dùng "ánh xạ hợp đồng"); linh hoạt dùng *họ bài toán*, *dạng bài toán*, *họ hàm*, *tầng mạng* thay vì lạm dụng từ "lớp".
- **Viết hoa sau dấu hai chấm (`:`)**: Cứ sau dấu `:` trong văn xuôi, tiêu đề, đề mục, danh sách hoặc chú thích hình ảnh/bảng biểu, từ tiếp theo bắt buộc phải viết hoa chữ cái đầu (ví dụ: `Ví dụ: Xét...`, `Lưu ý: Đây là...`, `- **Khái niệm**: Là...`, `Hình 1.1: Đồ thị...`). Tuyệt đối không để chữ cái đầu sau dấu `:` ở dạng chữ thường.
- **Khái niệm Wiki liên ngành (Cross-Disciplinary Wiki Scope)**: Môn học mặc định ưu tiên tìm kiếm và hiển thị định nghĩa khái niệm trong phạm vi chuyên môn của môn đó. Tuy nhiên, nếu một định luật/khái niệm thuần túy xuất phát từ lĩnh vực khoa học khác (ví dụ: *Định luật Snell* là quang học/vật lý xuất hiện trong bài toán tối ưu của Toán cho AI), cho phép liên kết và hiển thị định nghĩa từ lĩnh vực gốc tương ứng qua fallback scope trong `courseWikiScopes`.

### Lệnh kiểm thử tiêu chuẩn trên máy cục bộ (Local):
> [!NOTE]
> **Ủy thác build cho GitHub Actions**: Tuyệt đối không tự ý chạy `npm run ci:build` trên máy local của người dùng (tránh nghẽn CPU và ngốn 15+ GB RAM do render 779+ trang). Khâu build toàn cục do GitHub Actions tự động thực hiện trên đám mây khi push lên `main`.

```sh
# 1. Kiểm tra bài giảng vừa sửa (siêu tốc, tốn rất ít RAM):
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs <môn>/<bài>
# Hoặc kiểm tra toàn diện:
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all

# 2. Chạy bộ kiểm thử tự động của skill:
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
```
