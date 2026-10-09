# Hợp đồng file của StudyHub

Đọc trước khi tạo hoặc sửa bất kỳ file nào của website. Mọi mục dưới đây được rút từ mã nguồn hiện tại của repo (`docs/.vitepress/*.mjs`, `scripts/sync-courses.mjs`, `scripts/verify-courses.mjs`). Nếu mã đổi, mã thắng tài liệu này; sửa lại tài liệu.

## 1. Một bài giảng = bốn phần trên cùng một trang

Trang `/<môn>/bai-giang/<slug>.html` có bốn tab, địa chỉ `#notes`, `#slides`, `#cheatsheet`, `#kien-thuc-can-co`:

| Tab | Dữ liệu lấy từ | Ai viết |
| --- | --- | --- |
| Notes | `docs/<môn>/bai-giang/<slug>.md` | Phần chính của skill |
| Slides | `course.slides` trong `docs/.vitepress/course-catalog.mjs`, lọc theo `note === slug` | Skill viết sau khi Notes đã khóa |
| Cheatsheet | `cheatsheets` trong `docs/.vitepress/cheatsheets.mjs` hoặc sinh từ slide/công thức cốt lõi | Tờ tra cứu nhanh công thức, quy tắc, cú pháp và bẫy thi |
| Kiến thức nền | `lesson.prerequisites` trong catalog → các mục trong `concepts.mjs` → trang `docs/wiki/<id>.md` | Skill chọn và bổ sung khi thiếu |

Tiêu đề H1 của trang do `LectureHeader.vue` dựng từ `lesson.title` trong catalog. **Không viết thêm `# Tiêu đề` trong file Notes**; nó tạo hai H1. Bắt đầu nội dung bằng đoạn mở đầu hoặc `## 1. …`.

## 2. File Notes

Đường dẫn: `docs/<course-id>/bai-giang/<slug>.md`. Slug kebab-case không dấu, giữ quy ước của môn: `bai-01-…` (toan-cho-ai, xu-ly-du-lieu, giai-thuat-du-lieu) hoặc `01-…` (bieu-dien-tri-thuc, vat-ly-2, xac-suat-thong-ke). Xem slug đã có trong catalog trước khi đặt.

Frontmatter bắt buộc:

```yaml
---
course: toan-cho-ai
lecture: bai-03-ham-loi
section: lecture
title: "Hàm lồi & điều kiện tối ưu"
prerequisites: ["gradient", "to-hop-loi"]
lessonStatus: ready
description: "Một câu nêu phạm vi bài, dùng cho tìm kiếm."
---
```

- `lecture` phải trùng slug và tên file; `title` trùng `lesson.title` trong catalog; `prerequisites` trùng `lesson.prerequisites` (cùng thứ tự). `verify-courses.mjs` kiểm `lecture:` và `section: lecture`.
- `lessonStatus`: `ready` hoặc `draft`. Bài `draft` hiện thông báo “đang biên soạn” và không cho đánh dấu đã học. Chỉ đặt `ready` khi Notes đầy đủ **và** catalog có ít nhất một slide `note: '<slug>'` (verify sẽ fail nếu thiếu).
- `scripts/sync-courses.mjs` chỉ tạo frontmatter khi file chưa tồn tại; nó **không** đồng bộ lại khi catalog đổi. Sửa hai nơi cùng lúc.

Markdown được hỗ trợ (VitePress + cấu hình trong `config.mjs`):

| Cú pháp | Dùng khi | Hiển thị |
| --- | --- | --- |
| `$…$`, `$$…$$` | Mọi công thức (MathJax 3). Không dùng ảnh chụp công thức | Toán vector |
| ```` ```mermaid ```` | Sơ đồ quan hệ, luồng, cây nhỏ | Sơ đồ Mermaid |
| `::: example Tiêu đề` | Ví dụ có lời giải | Hộp “Ví dụ: …” |
| `::: proof Tiêu đề` | Chứng minh đầy đủ, có thể gập | Hộp gập “Chứng minh” |
| `::: derivation Tiêu đề` | Khai triển dài, đọc thêm | Hộp gập “Khai triển chi tiết” |
| `::: exercise Tiêu đề` | Đề bài để người học tự làm | Hộp “Bài tập” |
| `::: hint` | Gợi ý tăng dần | Hộp “Gợi ý” |
| `::: solution` | Lời giải — **luôn gập**, đặt ngay sau exercise/hint | Hộp gập “Lời giải” |
| `::: tip`, `::: info`, `::: warning`, `::: danger`, `::: details` | Hộp VitePress gốc; dùng có chủ đích (xem lecture-blueprint.md) | |
| `<details><summary>…</summary>…</details>` | Đáp án câu tự kiểm ngắn | Gập |
| `(dùng mục lục của VitePress)` | Mục lục trong bài dài | |
| `<CodeIllustration type="…" />` | Minh họa chạy được: `search`, `gradient`, `bayes`, `broadcast`, `mapreduce`, `field` | Component toàn cục, không cần import |

Mỗi container mở bằng `::: tên` phải đóng bằng `:::` trên dòng riêng. Không lồng container cùng loại. Không đặt đáp án trong cùng hộp với đề.

### Bài nhiều lớp

Một bài có thể có thêm các trang chủ đề `docs/<môn>/bai-giang/<slug>/<topic>.md` (frontmatter `section: topic`, `topic: <slug-chủ-đề>`), khai báo trong `topicGroups` của bài trong catalog. Trang Notes của bài khi đó là bản đồ chương có `<TopicMap />`. Cấu trúc, mô phỏng và kiểm tra: [topic-layers.md](topic-layers.md).

## 3. Hình và tài nguyên

- Hình riêng của bài: `docs/<môn>/bai-giang/img/<lec-xx>/<ten-hinh>.svg`, chèn bằng đường dẫn tương đối `![mô tả đầy đủ](img/lec-xx/ten-hinh.svg)`. Mô tả alt phải nói hình thể hiện điều gì, không chỉ “hình minh họa”.
- Ưu tiên SVG viết tay hoặc sinh bằng script tái lập được: `scripts/generate-<lec>-svgs.mjs` (xem `generate-lec03-svgs.mjs`). Dùng `font-family` có dấu tiếng Việt; không nhúng font ngoài.
- Mã thực hành dài: `materials/<lec-xx>/code/…`, liên kết bằng `/materials/...`. Code ngắn để minh họa nằm trong code fence của Notes.
- Không chép ảnh/trang sách có bản quyền vào `docs/`; vẽ lại có ghi nguồn (“Vẽ lại theo Hình 5.1, MMDS”) hoặc dẫn link.

## 4. Catalog: `docs/.vitepress/course-catalog.mjs`

```js
const lesson = (slug, title, prerequisites, status = 'ready') => ({ slug, title, prerequisites, status })
const slide = (title, bullets, note, formula = '', example = '') => ({ title, bullets, note, formula, example })
```

Thêm bài mới vào **ba** chỗ của đúng môn:

1. `lessons: [ … lesson('<slug>', '<Tên bài>', ['id-1','id-2']) ]` — thứ tự theo thứ tự học.
2. `parts[k].lessons: [ … '<slug>' ]` — sidebar dựng từ `parts`; thiếu ở đây thì bài không hiện trong mục lục.
3. `slides: [ … slide('<Tiêu đề>', ['ý 1','ý 2','ý 3'], '<slug>', '<công thức>', '<ví dụ>') ]`.

Trường slide là chuỗi văn bản có công thức TeX tường minh: `$…$` cho công thức trong câu, `$$…$$` cho công thức riêng dòng. `MathText.vue` hiển thị SVG và MathML hỗ trợ đọc màn hình, được biên dịch trước bằng cùng MathJax với Notes. Không dùng Markdown/HTML trong chuỗi slide. Trong chuỗi JavaScript phải viết hai dấu gạch chéo ngược cho mỗi lệnh TeX, ví dụ `"$\\frac{a}{b}$"`. Giữ giả thiết ngay trong công thức hoặc bullet cạnh nó; tiêu đề viết bằng chữ.

Tiêu chuẩn một slide catalog: tiêu đề là một kết luận hoặc câu hỏi có nội dung; 2–4 bullet, mỗi bullet là câu trọn nghĩa; `formula` khi bài có công thức trung tâm; `example` khi một con số cụ thể làm ý rõ hơn. Mỗi bài thường 3–6 slide, theo mạch của Notes. Slide là bản ôn nhanh của Notes, không chứa khẳng định mà Notes không có.

Chạy `node -e "import('./docs/.vitepress/course-catalog.mjs').then(m=>console.log(m.courseCatalog.length))"` sau khi sửa để bắt lỗi cú pháp.

## 5. Kiến thức nền và Wiki

Mỗi `id` trong `prerequisites` phải tồn tại ở **cả ba** chỗ, nếu không `verify-courses.mjs` fail hoặc `relatedConcepts()` ném lỗi:

1. `docs/.vitepress/concepts.mjs`: `'<id>': term('Tên', ['alias 1','alias 2'], 'định nghĩa', 'ví dụ', 'khi nào dùng', 'câu hỏi tự kiểm', 'đáp án')`. Tab Kiến thức nền, danh mục Wiki và ghi chú nhanh dùng `MathText`: văn bản có `$…$` và `$$…$$`, không dùng Markdown/HTML. Viết công thức bằng TeX, escape dấu gạch chéo ngược trong chuỗi JavaScript. Định nghĩa phải tự đứng được vì người học có thể chỉ đọc tab này.
2. `docs/.vitepress/wiki-content.mjs`: thêm `id` vào đúng một nhóm trong `wikiGroups`, và thêm `wikiDetails['<id>']` (đoạn “Giải thích kỹ thuật”, Markdown, có thể nhiều đoạn với `\n\n`). Có thể thêm `connections['<id>']` để chỉ định thuật ngữ liên quan; mọi id trong đó phải tồn tại.
3. `docs/wiki/<id>.md`: `npm run sync:courses` tự sinh từ hai file trên nếu chưa có; sau đó sửa trực tiếp file này (build không ghi đè). File phải chứa `## Giải thích kỹ thuật`.

`aliases` quyết định liên kết tự động: `term-links.mjs` nối **lần xuất hiện đầu tiên trong mỗi đoạn inline** của Notes/Wiki tới `/wiki/<id>.html`, bỏ qua tiêu đề, code, công thức và link có sẵn; so khớp không phân biệt hoa thường và theo ranh giới từ. Chọn alias đúng cách người Việt viết trong bài, kể cả biến thể (“véc-tơ”, “vector”). Tránh alias quá chung (“hàm”, “tập”) vì sẽ gắn link nhầm khắp nơi.

Liên kết thuật ngữ dùng hai tầng: bấm vào từ có gạch chấm để mở **ghi chú nhanh** ngay cạnh văn bản, rồi bấm nút trong thẻ để sang bài Wiki. Ghi chú nhanh lấy `name`, `definition` và `example` trong `concepts.mjs`; vì vậy ba trường này phải ngắn, tự đứng được; công thức dùng TeX có dấu phân cách, không dùng Markdown/HTML. Tên và aliases vẫn là văn bản thuần để tìm kiếm và liên kết thuật ngữ. `wikiDetails` và `docs/wiki/<id>.md` mới là nơi khai triển ký hiệu, điều kiện, ngộ nhận và liên hệ. Không nhồi toàn bộ bài Wiki vào ghi chú nhanh.

Một khái niệm khó được dạy ngay trong Notes vẫn có thể có mục Wiki để người học tra nhanh và đào sâu. Việc có mục Wiki **không tự biến nó thành prerequisite**: chỉ thêm vào `lesson.prerequisites` khi bài sử dụng khái niệm mà không dạy lại.

Mỗi khái niệm phải thuộc một lĩnh vực trong `wikiGroups`. Khi hai lĩnh vực dùng cùng một từ, tạo hai ID riêng và cho phép alias trùng; `term-links.mjs` phải chọn theo phạm vi của học phần. Ví dụ `tham-so-toan-hoc` và `tham-so-lap-trinh` cùng có alias “tham số”, nhưng Notes Toán không được liên kết tới trang lập trình. Nếu không đủ ngữ cảnh để phân giải, bỏ liên kết tự động thay vì chọn bừa.

Mỗi lesson có thể có `supportingConcepts` bên cạnh `prerequisites`. `prerequisites` là phần người học cần biết trước và phải khớp frontmatter. `supportingConcepts` là thuật ngữ xuất hiện trong Notes/Slides mà người học có thể tra trong khi đọc; không đưa chúng vào frontmatter. Tab Kiến thức nền hiển thị hai nhóm riêng và không được gọi toàn bộ danh sách hỗ trợ là tiên quyết.

Ghi chú nhanh có thể dùng trường `notation` với `$$…$$`, `bmatrix` hoặc `cases` để trình bày ma trận, vector hoặc hệ phương trình. Không ghép ma trận bằng ký tự ngoặc Unicode hay đặt công thức trong `pre`. Không đưa cú pháp list/mảng của ngôn ngữ lập trình như `[[1,2],[0,3]]` vào ví dụ đại số tuyến tính. Ghi chú ghim trên màn hình nhỏ phải có nền che (scrim) và lối đóng rõ; trên màn hình rộng phải nằm ngoài cột bài đọc, không che công thức hay đoạn đang đọc.

Ký pháp và cách gọi phải theo học phần. Trong NumPy, `shape=(3, 2)` là kích thước hai trục, `ndim=2` là số trục; `shape=(2,)` vẫn có `ndim=1`, dù chứa hai phần tử. Trong đại số tuyến tính, viết ma trận $3\times2$ hoặc $A\in\mathbb R^{3\times2}$; vector hai thành phần thuộc $\mathbb R^2$, không gọi theo tuple `shape`. Khi minh họa broadcasting, phần lập trình dùng mảng/code và ghi rõ `shape`, `ndim`; phần toán phải giải thích phép lặp hàng và cộng hai ma trận cùng kích thước. Nhãn, kích thước và công thức có khoảng cách riêng; không ghép nhãn sát ngoặc ma trận.

Chọn `prerequisites` là các khái niệm **bài này dùng mà không dạy lại**, xếp theo thứ tự nên đọc; không gắn toàn bộ `foundations` của môn. Khái niệm mới mà bài dạy thì nằm trong Notes, không phải ở Kiến thức nền.

## 6. Lệnh kiểm tra

```sh
npm ci                                   # lần đầu
node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs <course-id>/<slug>   # tích hợp một bài
node .claude/skills/studyhub-lecture/scripts/check_lecture.mjs --all                 # cả site
python3 .claude/skills/studyhub-lecture/scripts/review_teaching_text.py docs/<môn>/bai-giang/<slug>.md
npm run ci:build                         # sync + build VitePress; phải exit 0
npm run build && npx vitepress preview docs --port 8080   # rồi trong terminal khác:
QA_URL=http://127.0.0.1:8080 node scripts/verify-courses.mjs   # cần Chrome cho Puppeteer
```

`npm run build` còn xuất file tĩnh ra thư mục gốc (đã gitignore). Khi chỉ kiểm tra, dùng `npm run ci:build`. Đọc kết quả, đừng chỉ đọc exit code: warning của check_lecture và review là việc cần xem.

## 7. Chỗ hay hỏng

- Thêm bài vào `lessons` nhưng quên `parts` → bài không có trong sidebar.
- Đặt `ready` mà chưa có slide → verify fail.
- Thêm id vào `prerequisites` nhưng thiếu `wikiGroups`/`wikiDetails` → verify fail, có thể làm `relatedConcepts` ném lỗi khi build.
- Viết H1 trong Notes → hai tiêu đề.
- Lệnh TeX trong chuỗi slide thiếu `$…$` hoặc `$$…$$` → hiện nguyên ký tự `\frac`; `check_lecture.mjs` phát hiện lỗi này.
- Container quên `:::` đóng → nuốt phần còn lại của bài.
- Đặt hình ở chỗ khác `img/<lec>/` cạnh bài rồi viết đường dẫn tay → dễ gãy khi site chạy dưới `/StudyHub/`. Giữ quy ước đường dẫn tương đối như các bài hiện có và xem trang đã build.
- Viết `**…**` hoặc HTML trong `concepts.mjs` → hiện nguyên ký tự. Chỉ văn bản và TeX có dấu phân cách được hỗ trợ.
- Sửa `docs/wiki/<id>.md` nhưng không sửa `concepts.mjs` → định nghĩa trong tab Kiến thức nền (lấy từ concepts) và trang Wiki lệch nhau.


## Quy tắc giao diện Mực tím trên giấy vở

- Notes là tab mặc định; thứ tự Notes, Slides, Kiến thức nền. Địa chỉ cũ `#bai-tap` chuyển về Notes. Bài tập môn ở cuối Notes.
- Không chèn mục lục trong Markdown: VitePress có mục lục bên phải và trên điện thoại.
- Tiêu đề viết bằng chữ; không đặt công thức trong heading vì mục lục làm mất ký hiệu.
- Công thức trong Notes và Wiki dùng `$…$`; chữ tiếng Việt nằm ngoài công thức.
- Ký hiệu rút gọn được mở ít nhất một lần khi giới thiệu: tổng viết rõ các số hạng, tích viết rõ các thừa số, phép nhân ma trận viết rõ một hàng. Nêu miền chạy của chỉ số, ý nghĩa số hạng và một ví dụ nhỏ; chỉ dùng `\sum_i` sau khi phạm vi đã rõ. Dùng cả chỉ số dưới và cận trên khi giới thiệu tổng hữu hạn.
- Dấu cộng, trừ, nhân, chia và bằng thuộc cùng một biểu thức toán với các toán hạng để bộ hiển thị căn theo trục toán và đặt khoảng cách. Không ghép ma trận MathML với dấu phép toán bằng font văn bản; dùng một `mrow` chung. Trong code giữ `+`, `-`, `*`, `/`, `=` theo ngôn ngữ lập trình; trong toán dùng `\cdot`, `\times` hoặc phân số khi phù hợp, không thay mọi dấu bằng một quy tắc chung.
- Màu lấy từ `docs/.vitepress/theme/tokens.css`. SVG nội tuyến dùng biến token; SVG tĩnh dùng bảng màu sáng và đặt trên giấy trắng khi tối.
- Chữ SVG tối thiểu 14 đơn vị; chữ trong hình không dưới 12 đơn vị.
- **Chuẩn mực toán học & Chống tràn (No Scrollbars)**:
  - Tuyệt đối không để phát sinh thanh cuộn ngang (scrollbar) trên bất kỳ công thức nào, ở mọi kích thước màn hình và trong mọi khung hộp (`::: info`, `::: details`).
  - Mọi công thức hiển thị (`$$...$$`) dài hoặc nhiều bước biến đổi phải chủ động bẻ dòng bằng môi trường `\begin{aligned}...\end{aligned}`. Ngắt dòng bằng `\\` tại các dấu quan hệ ($=$, $\le$, $\ge$, $\approx$, $\implies$) hoặc phép toán ($+$, $-$) và căn lề bằng `&`. Không viết chuỗi đẳng thức trải dài trên một dòng đơn.
  - Tách hoàn toàn văn xuôi, nhận xét ra ngoài khối TeX. Không nhét văn xuôi dài vào `\text{...}` bên trong công thức.
  - Cặp dấu `$$` mở và đóng phải luôn nằm trên một dòng riêng biệt, không dính liền với nội dung công thức hay đoạn văn xuôi.
  - Công thức inline (`$...$`): Giới hạn chiều rộng không vượt quá 38ex; nếu dài hoặc phức tạp, bắt buộc tách thành khối `$$...$$` riêng.

