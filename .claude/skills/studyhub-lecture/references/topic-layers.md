# Bài nhiều lớp: trang chương và các trang chủ đề

Một chương dày (ví dụ chương 2–3 của *Convex Optimization*) không nên dồn vào một trang Notes dài: người học mới bị ngợp, mỗi khái niệm chỉ được vài đoạn, và không còn chỗ cho ví dụ, mô phỏng, câu hỏi đào sâu. StudyHub cho phép tách một bài thành **trang chương** (hub) và nhiều **trang chủ đề**, mỗi trang đi sâu vào một ý. Lecture 01 của môn Cơ sở toán cho AI là mẫu đầy đủ: 25 chủ đề trong bốn nhóm.

Dùng kiến trúc này khi người dùng yêu cầu "phân lớp", hoặc khi nguồn của một bài có nhiều khái niệm độc lập mà mỗi khái niệm cần ví dụ, hình và bài tập riêng. Với bài ngắn, một trang Notes vẫn tốt hơn.

## 1. Kiến trúc và đường dẫn

- Trang chương giữ nguyên: `docs/<course>/bai-giang/<lesson>.md`, `section: lecture`, ba tab Notes, Slides, Kiến thức nền, slug và tiến độ cũ. Notes của trang chương trở thành **bản đồ chương**: lời mở, `<TopicMap />`, lộ trình đọc, bức tranh chung (có thể kèm sơ đồ Mermaid), bài tập tổng hợp, tóm tắt, nguồn.
- Mỗi chủ đề: `docs/<course>/bai-giang/<lesson>/<topic-slug>.md`, URL `/<course>/bai-giang/<lesson>/<topic-slug>.html`.
- Catalog khai báo thứ tự đọc trong `topicGroups` của bài (với môn Toán cho AI: `docs/.vitepress/math-ai-course.mjs`):

```js
const topic = (slug, title, question, source = '') => ({ slug, title, question, source })
const group = (title, description, topics) => ({ title, description, topics })
topicGroups['bai-01-nhap-mon-toi-uu'] = [
  group('I. Bài toán tối ưu', 'Viết đúng một bài toán trước khi nghĩ tới chuyện giải nó.', [
    topic('bai-toan-toi-uu', 'Bài toán tối ưu và những gì cần viết ra', 'Một bài toán tối ưu gồm những phần nào…?', '§1.1, §4.1'),
  ]),
]
```

`question` là câu hỏi mà chủ đề trả lời, hiện trên bản đồ chủ đề và trên nút "chủ đề tiếp theo". `source` là mục sách, hiện ở đầu trang. `lecture-model.mjs` (`lessonTopics`, `topicPath`, `findTopic`) dựng thứ tự đọc; sidebar, thanh tiến độ, nút trước/sau và `TopicMap` đều đọc từ đây, nên **thêm chủ đề = thêm vào catalog + thêm file**, không sửa component.

## 2. Frontmatter và khung một trang chủ đề

```yaml
---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: ham-loi
section: topic
title: "Hàm lồi và bất đẳng thức dây cung"   # trùng catalog
description: "Một hai câu nói trang dạy gì, dùng cho tìm kiếm."
---
```

Không viết H1: `TopicHeader` đã in đường dẫn chương, tiêu đề, "Chủ đề k / N", thời gian đọc, mục sách và thanh tiến độ. Khung đã dùng tốt:

1. Hai ba đoạn mở đầu: câu hỏi có thật mà chủ đề trả lời, nối với chủ đề trước, rồi một câu nói phần dưới sẽ làm gì. Đổi cách nói câu cuối giữa các trang; đừng trang nào cũng "Trang này…".
2. Các mục đánh số `## 1.`, `## 2.`… Định nghĩa đặt trong `> **Định nghĩa.**`, định lý trong `> **Định lý.**`. Chứng minh, ví dụ, mẹo dùng `::: proof`, `::: example Tiêu đề`, `::: tip`.
3. Mô phỏng tương tác đặt ngay sau đoạn giới thiệu khái niệm, kèm một đoạn nói nên thử gì và quan sát gì (mục 4).
4. `## n. Những câu hỏi để đào sâu`: 3–4 câu `**Câu k.**`, mỗi câu một `<details><summary>Xem lời giải thích</summary>` có lập luận đầy đủ. Đa dạng cách đặt vấn đề (phản ví dụ cần tìm, dự đoán cần kiểm, "điều gì xảy ra nếu", tình huống học máy); không lặp khuôn "Một bạn nói…" ở nhiều trang.
5. `## n. Bài tập tự luyện`: `::: exercise` + `::: solution` (có thể `::: hint`). Dữ liệu tự đặt, không lấy dữ liệu bài tập về nhà của học phần.
6. `## Tóm tắt` hai đoạn và `## Nguồn và đọc thêm`: mục, trang, hình, ví dụ của sách; dòng cuối nói rõ phần nào người soạn bổ sung và "mọi con số đã được tính lại bằng chương trình".

Liên kết giữa các chủ đề dùng đường dẫn tương đối tới file `.md` (`[siêu phẳng tựa](./sieu-phang-phan-tach-va-tua.md)`). Từ trang chương: `./<lesson>/<topic>.md`.

## 3. Độ sâu mong đợi của một chủ đề

Một chủ đề không phải tóm tắt mục sách. Nó cần: ý nghĩa hình học của định nghĩa, ví dụ và phản ví dụ đã tính bằng code, cách nhìn khác của cùng một kết quả (chẳng hạn Hessian của log-sum-exp là một phương sai), liên hệ với các chủ đề khác và với học máy khi liên hệ đó đúng, và ranh giới của kết quả (bỏ giả thiết nào thì sai, phản ví dụ). Mỗi khẳng định ngoài sách phải kiểm được: tính lại, hoặc dẫn nguồn đã tra.

## 4. Mô phỏng tương tác (labs)

- File `docs/.vitepress/theme/<Ten>Lab.vue`. `theme/index.js` đăng ký mọi `*Lab.vue` theo tên file, nên chỉ cần tạo file rồi viết `<TenLab />` trong Markdown. `check_lecture.mjs` báo `LAB_MISSING` nếu gõ sai tên.
- Màu chỉ qua token và các lớp trong `theme/labs.css` (`lab-line`, `lab-accent`, `lab-good`, `lab-bad`, `lab-region`, `lab-bad-fill`, `lab-handle`, `lab-readout`, `lab-tasks`…). Không mã màu hex trong theme (script kiểm token sẽ chặn). SVG dùng `viewBox`, không đặt chiều rộng cứng.
- Mọi `id` trong SVG (clipPath, marker) sinh bằng `useId()`; hai lab cùng loại trên một trang không được trùng id.
- Điểm kéo được dùng `createDragger` của `theme/svg-drag.js` (chuột, chạm, phím mũi tên), có `role="slider"`, `aria-label`, `aria-valuetext`. Hình học dùng lại `theme/convex-geometry.mjs`, đường đồng mức dùng `theme/contour.mjs`; hàm thuần có test trong `scripts/tests/*.test.mjs`.
- Bảng kết quả (`lab-readout`, `role="status"`) nói bằng câu đầy đủ điều đang thấy và vì sao; con số trong đó phải khớp phép tính Python dùng cho bài. Kèm `<details class="lab-tasks">` 3–4 gợi ý thao tác có mục đích.
- Ngưỡng số học trong lab (sai số khi so sánh, bước của thanh trượt) phải được chọn sao cho người dùng chạm tới được trạng thái cần thấy; thêm nút "Đặt vào nghiệm" khi trạng thái đó khó kéo tới chính xác.

## 5. Kiểm tra trước khi bàn giao

```sh
node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs <course>/<lesson>      # chương + mọi chủ đề
python3 -I .claude/skills/studyhub-lecture/scripts/review_teaching_text.py --format text docs/<course>/bai-giang/<lesson>.md docs/<course>/bai-giang/<lesson>/*.md
npm run ci:build
```

`check_lecture.mjs` kiểm thêm cho lớp chủ đề: file có đủ theo catalog (`TOPIC_MISSING`), frontmatter khớp (`FRONTMATTER_TOPIC`, `TOPIC_TITLE_MISMATCH`), file thừa không có trong catalog (`TOPIC_ORPHAN`), trang chương thiếu `<TopicMap />`, link tương đối hỏng, slug chủ đề trùng, và **công thức inline rộng hơn 38ex** (`INLINE_MATH_WIDE`) vì công thức inline không xuống dòng và sẽ tràn ngang trên điện thoại. Chuyển những công thức đó thành `$$…$$` (có thể `aligned`) hoặc tách nhỏ. Hai dấu vết của TeX bị hỏng khi ghi bằng script cũng được bắt: ký tự điều khiển giữa dòng (`CONTROL_CHAR`, lỗi) và dòng có số dấu `$` lẻ (`INLINE_MATH_SPLIT`, cảnh báo).

Truyền **cả chương** cho `review_teaching_text.py` một lượt để thấy khuôn lặp giữa các trang (`QUESTION_TEMPLATE`, `REPEATED_OPENER`), ngoài các khuôn trong từng trang.

Cuối cùng mở trang ở bề rộng 375px và trên máy bàn: không cuộn ngang, mô phỏng kéo được, công thức hiển thị, sơ đồ Mermaid hiện.

## 6. Những lỗi đã gặp khi soạn Lecture 01 và 02

- Script Python viết qua heredoc của Git Bash trên Windows làm mất một nửa số dấu `\` trong TeX. Viết script bằng công cụ ghi file rồi chạy, không nhúng TeX vào heredoc.
- Ngay cả trong file script, chuỗi Python thường (không raw) vẫn đổi `\t`, `\n`, `\f`, `\v`, `\b`, `\a` thành ký tự điều khiển: `\tfrac` thành TAB + `frac`, `\ne` thành xuống dòng + `e`. Build vẫn chạy, MathJax vẫn vẽ, nhưng công thức sai ("400 ext m²", "20 e 0"), và lỗi này đã lên trang thật trước khi được phát hiện. Mọi chuỗi chứa TeX phải là raw string (`r"..."`), hoặc thay nội dung bằng công cụ sửa file. Sau mỗi lượt sửa bằng script, chạy `check_lecture.mjs` để bắt `CONTROL_CHAR` và `INLINE_MATH_SPLIT`.
- Ví dụ và bài tập vô tình dùng lại dữ liệu bài tập về nhà của học phần. Luôn đối chiếu với file bài tập trong `raw_materials` và đổi dữ liệu.
- Câu chuyện mở đầu (Dido), bài LP "phân bổ thời gian chạy hai tác vụ" và vài ví dụ nhỏ được lấy từ slide của học phần, kèm dòng ghi công. Ghi công không hợp thức hóa việc dùng một nguồn mà sổ nguồn của môn (`raw_materials/<môn>/authoring-map.md`) đã loại. Đọc mục "Ranh giới nguồn" của sổ trước khi chọn ví dụ xuyên suốt. Khi thay một ví dụ, tìm mọi chỗ nhắc lại nó (mục định nghĩa, câu hỏi, bài tập, tóm tắt, dòng nguồn) và tính lại mọi số liên quan.
- Lời giải "nghĩ thành tiếng" ("à không, thử lại…") làm người học rối. Lời giải chỉ trình bày lập luận đúng cuối cùng; phản ví dụ được kiểm bằng code trước. Ở Lecture 02 lỗi này vẫn lọt hai lần ("... thay vào đó, hãy", "... chính xác hơn"), một lần kèm kết luận sai về miền khả thi, nên `review_teaching_text.py` nay báo `THINKING_ALOUD`.
- Ví dụ minh họa phải thật sự có tính chất được nói tới. Ví dụ "chi phí trung bình" $(x_1^2 + 2x_2^2 + 1)/(x_1 + x_2)$ được chọn để minh họa hàm chỉ tựa lồi, nhưng kiểm Hessian cho thấy nó lồi (phối cảnh của bình phương chuẩn). Ví dụ được thay bằng tỉ số khoảng cách, và trường hợp cũ thành một câu hỏi đào sâu. Trước khi viết "không lồi", tính Hessian hoặc thử một dây cung bằng code.
- Thuật ngữ mới chỉ được dùng qua liên kết tự động không nằm trong `prerequisites` của bài nào, nên bản kiểm cũ bỏ qua chúng, và ký hiệu Unicode như ℓ₁, Bᵀ trong định nghĩa chỉ bị test của repo bắt lúc build. `check_lecture.mjs --all` nay kiểm mọi thuật ngữ.
- Từ đa nghĩa bị liên kết nhầm: "đồ thị" (của hàm số và lý thuyết đồ thị), "phép chiếu" (Euclid, tọa độ, phối cảnh), "đơn hình" (hình học và phương pháp đơn hình). Tạo ID riêng theo lĩnh vực hoặc dùng alias dài hơn; xem repo-format.md mục 5.
