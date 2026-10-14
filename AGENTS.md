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
> - Khi soạn bài hoặc giải thích có chứa phép tính số học/toán học: **Bắt buộc chạy code Python tính lại**, không được đoán hoặc dựa vào trực giác.
> - **Tuyệt đối không để xuất hiện thanh cuộn (scrollbar) trên công thức toán**: Công thức hiển thị dài phải bẻ dòng bằng `\begin{aligned}` với `\\` và `&`; công thức inline không quá 38ex.

---

## 3. Các Lệnh Kiểm Thử & Xác Minh Bắt Buộc

Mọi AI khi thực hiện thay đổi nội dung hoặc mã nguồn phải chạy các lệnh kiểm tra sau từ thư mục gốc của repo:

```bash
# 1. Cài đặt dependency (nếu môi trường mới)
npm ci

# 2. Chạy máy chủ dev cục bộ (on-demand HMR nhẹ, dùng khi cần xem thử giao diện)
npm run dev

# 3. Kiểm tra bài giảng vừa sửa (chỉ mất ~0.5 giây, tốn rất ít RAM):
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs <môn>/<bài>
# Hoặc kiểm tra toàn diện cú pháp và liên kết:
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all

# 4. Chạy bộ bài kiểm thử tự động của skill
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
```

> [!NOTE]
> **Ủy thác build toàn cục cho GitHub Actions (Offload Full Build to GitHub Actions)**:
> - **Tuyệt đối không tự ý chạy `npm run ci:build` trên máy cục bộ của người dùng**, vì lệnh này phải nén bundle và xuất HTML tĩnh cho toàn bộ 779+ bài học, gây nghẽn CPU và ngốn 15+ GB RAM làm chậm máy người dùng.
> - Toàn bộ công việc build và deploy trang tĩnh đã được cấu hình tự động 100% trên hạ tầng máy chủ đám mây của GitHub qua GitHub Actions (`.github/workflows/deploy.yml`). Khi code được push lên `main`, GitHub sẽ tự khởi tạo runner để chạy `ci:build` và xuất bản lên GitHub Pages.
> - Trên máy cục bộ, AI chỉ chạy `check_lecture.mjs` và `test_tools.py` để xác minh tính đúng đắn trước khi commit và push.

---

## 4. Nguyên Tắc Sư Phạm Cốt Lõi ("Giảng Như Giáo Sư")

1. **Bắt đầu từ vấn đề thực tế**: Đi từ câu hỏi hoặc bài toán cụ thể mà khái niệm giải quyết, không bắt đầu bằng định nghĩa trơ trụi.
2. **Chính xác tuyệt đối**: Giữ đúng giả thiết, miền xác định, lượng từ, đơn vị đo lường và chiều suy luận.
3. **Mở bước khó**: Làm rõ những bước biến đổi mà người mới hay vấp ngã.
4. **Không bịa đặt**: Tuyệt đối không bịa trích dẫn, tác giả, số liệu thống kê hoặc năm tháng lịch sử.
5. **Tiếng Việt tự nhiên**: Hành văn sáng sủa, thuần Việt, tránh câu cú dịch máy thô cứng.
6. **Chủ quyền bài giảng (Chính danh, biến tri thức thành bài giảng độc lập)**: Bài giảng của StudyHub là giáo trình giảng dạy độc lập, hoàn chỉnh của chính người giảng viên. Tuyệt đối không để bài giảng mang tính chất sổ tay trích dẫn hay đối chiếu sách thụ động. Nghiêm cấm các câu và cụm từ: *“Nội dung lấy từ giáo trình…”*, *“Lấy từ slide của môn…”*, *“Bài tập lấy từ sách…”*, *“Ví dụ do người soạn thêm, không gán cho tác giả giáo trình…”*, *“Ảnh lấy từ sách”*, *“ảnh nguyên gốc sách”*, *“hình trong sách”*, *“dữ liệu này từ…”*, *“theo sách…”*, *“sách dùng…”*, *“nguyên tác…”*, *“bản dịch của…”*, *“tiến độ bản dịch…”*. Mọi tư liệu, hình ảnh, ví dụ, bài tập phải trở thành một phần tự nhiên của bài giảng (*“Hình 1.1: …”*, *“Xét bài toán thực tế sau:…”*, *“Quan sát đồ thị chuyển trạng thái…”*). Mọi bài giảng là một thực thể tri thức độc lập, hoàn chỉnh, tự chịu trách nhiệm về mặt học thuật và sư phạm. Mục cuối bài luôn đặt tên là `## Tài liệu tham khảo` theo chuẩn học thuật chuẩn mực, không phân bua “do người soạn bổ sung”.
7. **Văn phong giáo sư và nhà ngôn ngữ tiếng Việt đại tài**: Dùng từ ngữ tiếng Việt chuẩn xác, giàu tính sư phạm, uyên bác và dễ hiểu, không “giả trân”, không sáo rỗng kiểu AI. Các mẹo tư duy, trực giác thuật toán được lồng ghép tự nhiên (*“Một cách người người ta hay dùng trong thực tế để…”*, *“Để không bao giờ nhầm lẫn ở bước này…”* thay vì đóng khung máy móc *“Mẹo thú vị:”*). Luôn gắn kết lý thuyết trừu tượng với các ứng dụng thực tế sinh động trong đời sống và đặt câu hỏi đào sâu bản chất vấn đề.
8. **Chuẩn mực toán học & Chống tràn / Tuyệt đối không xuất hiện thanh cuộn (No Math Scrollbars)**:
   - Mọi công thức, phương trình, hàm số toán học hiển thị (`$$...$$`) và nội dòng (`$...$`) phải được format chính xác, thẩm mỹ, tuyệt đối không xuất hiện thanh cuộn ngang (scrollbar) trên bất kỳ kích cỡ màn hình nào (kể cả di động ~360px–375px hay trong các hộp `::: info`, `::: details`).
   - Với công thức hiển thị: Chủ động bẻ dòng bằng `\begin{aligned}...\end{aligned}`, ngắt dòng bằng `\\` tại dấu bằng, dấu bất đẳng thức ($=$, $\le$, $\ge$, $\approx$, $\implies$) hoặc phép toán ($+$, $-$) và căn lề bằng `&`. Không viết chuỗi đẳng thức trải dài trên một dòng đơn.
   - Tuyệt đối không nhét văn xuôi, câu nhận xét dài vào trong TeX bằng `\text{...}`. Văn xuôi phân tích phải viết ở đoạn văn bên ngoài khối toán.
   - Dấu mở `$$` và đóng `$$` phải luôn nằm trên một dòng riêng biệt, không dính liền với nội dung công thức hay đoạn văn xuôi.
   - Công thức inline (`$...$`): Không vượt quá 38ex; nếu dài hoặc phức tạp, bắt buộc tách thành khối `$$...$$` riêng.
9. **Khai triển tường minh trước khi viết tắt (Explicit Unpacking before Abbreviation)**:
   - Mọi công thức chứa ký hiệu viết tắt dồn ($\sum$, $\prod$, $\arg\min$, $\arg\max$, $\mathbb{E}[\cdot]$, tích Kronecker, ma trận khối...) **bắt buộc phải được khai triển tường minh ít nhất một lần khi giới thiệu**.
   - Tuyệt đối không viết $\sum_i \theta_i = 1$ lơ lửng, cộc lốc mà phải ghi rõ miền chỉ số và dạng khai triển: $\sum_{i=1}^k \theta_i = \theta_1 + \theta_2 + \dots + \theta_k = 1$ với $\theta_i \ge 0, \forall i = 1, \dots, k$.
   - Luôn giải thích bản chất bằng ngôn ngữ tự nhiên: Nêu rõ ý nghĩa vật lý/hình học (ví dụ: Các trọng số $\theta_i$ là tỷ lệ phần trăm phân bổ 100%, không có trọng số âm, phép bình quân gia quyền không làm biến dạng thang đo).
   - Xuất phát từ trường hợp nhỏ nhất ($k=2$: Đoạn thẳng $\theta_1 x_1 + (1 - \theta_1) x_2$ với $\theta_1 \in [0, 1]$) trước khi tổng quát hóa lên $k$ điểm hay $n$ chiều, giúp sinh viên nắm vững trực giác hình học trước khi dùng đại số trừu tượng.
   - Khuyến khích sử dụng công thức có chú thích (Annotated Math) bằng `\underbrace{...}_{...}` để chỉ rõ vai trò của từng cụm số hạng.
10. **Chuẩn mực văn phong tiếng Việt & Hạn chế dấu chấm phẩy (`;`)**:
   - Trong lời giảng văn xuôi, **hạn chế tối đa việc dùng dấu chấm phẩy (`;`)**. Dấu `;` thường khiến câu văn trở nên khô khan, rời rạc và mang nặng tính liệt kê máy móc.
   - Thay vào đó, hãy đọc kỹ quan hệ ngữ nghĩa giữa các vế để lựa chọn **từ nối tiếng Việt chuẩn xác** (*và, nhưng, tuy nhiên, trái lại, ngược lại, vì vậy, do đó, kéo theo, dẫn đến, suy ra, hệ quả là, đồng nghĩa với việc, trong khi, song song đó, cụ thể là, chẳng hạn...*) hoặc tách thành hai câu đơn độc lập với chủ ngữ rõ ràng.
   - Tra cứu chi tiết tại cẩm nang `references/tu-noi-va-dien-dat.md`.
11. **Thoát khỏi tư duy dịch máy (Calque & Translationese) — Tránh dùng từ máy móc kiểu "hợp đồng", lạm dụng "lớp"**:
   - **Không dịch bám từ `contract` thành "hợp đồng"** trong kỹ thuật và lập trình: Tránh dùng *"hợp đồng file"*, *"hợp đồng dữ liệu"*, *"hợp đồng nội dung"*. Hãy thay bằng các từ ngữ tiếng Việt tự nhiên và chuẩn mực: *Quy chuẩn cấu trúc file*, *chuẩn giao tiếp dữ liệu (schema)*, *yêu cầu nội dung*, *ràng buộc định dạng*. Tuyệt đối không dịch *contraction mapping* thành *"ánh xạ hợp đồng"* (bắt buộc dùng *ánh xạ co*).
   - **Tránh lạm dụng từ "lớp"**: Thay vì dịch máy móc mọi từ `class` hay `layer` thành "lớp", hãy sử dụng vốn từ tiếng Việt linh hoạt: Dùng *họ bài toán*, *dạng bài toán*, *nhóm bài toán* (thay vì lặp từ "lớp bài toán"); dùng *họ hàm* (thay vì "lớp hàm"); dùng *tầng kiến trúc*, *tầng mạng* (thay vì "lớp").
12. **Quy tắc viết hoa sau dấu hai chấm (`:`) (Capitalization After Colons)**:
   - Trong toàn bộ câu văn xuôi, tiêu đề, đề mục, danh sách liệt kê, chú thích hình ảnh/bảng biểu hoặc nhãn giải thích: **Cứ sau dấu hai chấm (`:`) thì từ tiếp theo bắt buộc phải bắt đầu bằng chữ cái viết hoa**.
   - Tuyệt đối không để chữ cái đầu tiên sau dấu `:` ở dạng chữ thường.
   - Các trường hợp chuẩn mực:
     - `Ví dụ: Xét mô hình tuyến tính sau...` (không viết `Ví dụ: xét mô hình...`)
     - `Lưu ý: Đây là bước chuyển trạng thái quan trọng...` (không viết `Lưu ý: đây là...`)
     - `- **Khái niệm**: Là ánh xạ từ tập nguồn sang tập đích...` (không viết `- **Khái niệm**: là ánh xạ...`)
     - `Hình 1.1: Đồ thị chuyển trạng thái của tác tử...` (không viết `Hình 1.1: đồ thị...`)
     - `Tập dữ liệu gồm ba cột: Cột ID, cột đặc trưng và cột nhãn mục tiêu.` (không viết `...ba cột: cột ID...`)
   - Quy tắc áp dụng cho toàn bộ dự án StudyHub (bài giảng, topic, wiki, catalog, cheatsheet, slides). Chỉ ngoại trừ các trường hợp cú pháp mã nguồn lập trình (`code`), đường dẫn URL, địa chỉ drive (`C:\`), hoặc công thức toán học TeX.
13. **Giao diện bài giảng tinh gọn & trực diện (Clean & Focused Lecture Presentation)**:
   - Danh sách bài giảng trong trang tổng quan môn học (`CourseOverview`) chỉ hiển thị duy nhất số thứ tự và tiêu đề bài giảng (`lesson.title`). Tuyệt đối không chèn các thông số phụ gây nhiễu thị giác như `X slide · Y mục hỗ trợ`.
   - Không hiển thị số lượng kiến thức nền ở thanh thông tin đầu môn học (`course-meta`), và không đặt các câu chú thích thừa thãi ở cuối trang môn học (như *"Trong Notes, bấm vào thuật ngữ có gạch chấm..."*). Giao diện phải sạch sẽ, tập trung tối đa vào nội dung học tập.
14. **Triệt tiêu hoàn toàn thanh cuộn & mũi tên scrollbar trên công thức toán (Zero Math Scrollbars & Spinner Arrows)**:
   - Mọi công thức toán học inline (`$...$`) và display (`$$...$$`) trên toàn bộ hệ thống (Notes, Wiki, Slides, Cheatsheets, Popovers, Labs) tuyệt đối không được xuất hiện thanh cuộn ngang/dọc hay các nút mũi tên cuộn của hệ điều hành (`▴▾`).
   - Công thức inline bắt buộc phải có `overflow: visible !important;` và ẩn triệt để thanh cuộn. Thẻ MathML phụ trợ (`mjx-assistive-mml`) phải luôn được ẩn hoàn toàn trên toàn cục dự án để không gây xung đột hiển thị nút mũi tên cuộn trên Windows/Chromium.
15. **Quy tắc hiển thị khái niệm Wiki liên ngành (Cross-Disciplinary Wiki Scope)**:
   - Môn học mặc định ưu tiên tìm kiếm và hiển thị định nghĩa khái niệm trong phạm vi chuyên môn của môn đó (ví dụ: Toán học trong môn *Cơ sở toán học cho AI*).
   - Tuy nhiên, đối với các khái niệm hoặc định luật thuần túy bắt nguồn từ lĩnh vực khoa học khác (ví dụ: *Định luật Snell* là quang học/vật lý xuất hiện trong bài toán tối ưu của Toán cho AI), cho phép liên kết và hiển thị định nghĩa từ lĩnh vực gốc tương ứng thông qua cơ chế fallback scope mở rộng trong `courseWikiScopes` (`docs/.vitepress/wiki-content.mjs`).
16. **Hạn chế dấu gạch ngang dài (em dash —) trong văn xuôi (Minimize Em Dashes)**:
   - Trong văn xuôi tiếng Việt, tuyệt đối hạn chế lạm dụng dấu gạch ngang dài (`—` hoặc `--`) để chêm xen vế phụ giải thích giữa câu. Đây là thói quen dịch máy bắt chước ngữ pháp tiếng Anh, làm gãy vụn câu văn và mất đi nhịp điệu tự nhiên của tiếng Việt.
   - Thay thế bằng các phương thức tiếng Việt chuẩn mực:
     - Dùng dấu phẩy (`,`) cho các vế phụ ngắn liền mạch.
     - Dùng dấu ngoặc đơn (`(...)`) cho chú thích bổ trợ, giải thích phụ hoặc thuật ngữ tương đương.
     - Dùng dấu hai chấm (`:`) khi chuẩn bị phát biểu định nghĩa, giải thích bản chất hoặc mở đầu liệt kê.
     - Dùng từ nối tiếng Việt tự nhiên (*tức là, cụ thể là, nghĩa là, vốn là, đồng nghĩa với việc...*).
     - Tách thành hai câu đơn độc lập khi vế giải thích đủ dài và có chủ ngữ riêng.
   - Các trường hợp hợp lệ duy nhất của dấu gạch ngang:
     - Dấu nối khoảng số, ngày tháng, thời gian (dùng en dash `–`: Ví dụ `tr. 12–15`, `1945–1975`).
     - Tên định lý, thuật toán liên danh hai hoặc nhiều tác giả (ví dụ: *Karush–Kuhn–Tucker*, *Cauchy–Schwarz*, *Gauss–Jordan*).
     - Dấu gạch đầu dòng danh sách liệt kê (`- ...`).
17. **Tính trực diện và đúng bản chất của ví dụ minh họa (Direct & Verified Exemplification)**:
   - Khi vừa phát biểu một khái niệm, định lý hoặc tính chất toán học, ví dụ đi kèm ngay sau đó bắt buộc phải chạm đúng vào bản chất kỹ thuật đặc thù của tính chất ấy.
   - Tuyệt đối không chọn ví dụ hời hợt, chung chung hoặc lấy đối tượng tầm thường làm lu mờ tính chất cần giảng dạy.
   - Mọi ví dụ đối chứng hoặc phản chứng phải được kiểm tra tính chất bằng code Python trước khi viết vào bài (chẳng hạn: Muốn minh họa hàm tựa lồi nhưng không lồi thì bắt buộc phải kiểm tra ma trận Hessian hoặc phép thử dây cung để chắc chắn hàm đó thực sự không lồi).
18. **Chuẩn hóa ký hiệu toán học trị tuyệt đối và chuẩn (Absolute Value & Norm Syntax)**:
   - Giá trị tuyệt đối hoặc khoảng cách: Dùng trực tiếp `|x - y|` hoặc `|c - b_i|`.
   - Chuẩn vector hoặc ma trận: Dùng `\|x\|` hoặc `\lVert x \rVert_2`.
   - Tuyệt đối không dùng `\vert{}` hay `\Vert{}` vì gây lỗi phân tích cú pháp, khoảng cách xấu và để lại cặp ngoặc nhọn `{}` rỗng trong MathJax / KaTeX của VitePress.
19. **Cấm lối viết "nghĩ thành tiếng" trong lời giải bài tập (No Thinking-Aloud in Solutions)**:
   - Lời giải bài tập phải là văn bản sư phạm mẫu mực, lập luận mạch lạc, chắc chắn và dứt khoát từ đầu đến cuối.
   - Nghiêm cấm đưa vào các câu nháp "nghĩ thành tiếng" kiểu tự độc thoại: *“Khoan đã, hãy xem lại…”*, *“À không, thay vào đó…”*, *“Ý tôi là…”*, *“Thử lại nào…”*, *“Nhầm rồi…”*. Mọi phép thử sai hay phân tích phản ví dụ phải được trình bày khách quan như một phần tự nhiên của bài giảng.
20. **Không bịa đặt tần suất lỗi sinh viên hoặc "bẫy thi cử" vô căn cứ (No Fabricated Error Frequency)**:
   - Tuyệt đối không đưa ra các khẳng định mang tính thống kê cảm tính về sai sót của người học nếu không có số liệu thực nghiệm: Nghiêm cấm các câu *“Sinh viên rất hay nhầm…”*, *“Lỗi phổ biến nhất của sinh viên là…”*, *“Đa số sinh viên đều mắc bẫy này…”*, *“Bẫy thi cử cực kỳ phổ biến…”*.
   - Cách diễn đạt chuẩn mực: Nêu trực diện hai cách hiểu đối lập hoặc chỉ rõ điểm mấu chốt dễ gây ngộ nhận (*“Một cách đọc dễ dẫn đến sai sót là... Trái lại, khi xét kỹ giả thiết...”*).
21. **Kiểm soát độ dài câu và mật độ in đậm (Sentence Length & Boldness Balance)**:
   - Tránh câu văn quá dài lê thê: Mỗi câu văn xuôi nên dưới 50–55 từ. Khi câu quá dài hoặc chứa nhiều ý, chủ động tách thành hai câu đơn độc lập với chủ ngữ rõ ràng để người học dễ tiếp thu và tránh hụt hơi.
   - Không lạm dụng in đậm (`**...**`): Chỉ in đậm tên thuật ngữ ở lần đầu tiên định nghĩa hoặc các điều kiện tiên quyết mang tính quyết định. Tuyệt đối không in đậm 4–5 cụm từ trong cùng một đoạn văn làm loãng điểm nhấn và tạo cảm giác tiếp thị, quảng cáo.



