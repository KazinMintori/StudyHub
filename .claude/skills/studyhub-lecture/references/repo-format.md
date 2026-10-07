# Hợp đồng file của StudyHub

Đọc trước khi tạo hoặc sửa bất kỳ file nào của website. Mọi mục dưới đây được rút từ mã nguồn hiện tại của repo (`docs/.vitepress/*.mjs`, `scripts/sync-courses.mjs`, `scripts/verify-courses.mjs`). Nếu mã đổi, mã thắng tài liệu này; sửa lại tài liệu.

## 1. Một bài giảng = ba phần trên cùng một trang

Trang `/<môn>/bai-giang/<slug>.html` có ba tab, địa chỉ `#slides`, `#notes`, `#kien-thuc-can-co`:

| Tab | Dữ liệu lấy từ | Ai viết |
| --- | --- | --- |
| Slides | `course.slides` trong `docs/.vitepress/course-catalog.mjs`, lọc theo `note === slug` | Skill viết sau khi Notes đã khóa |
| Notes | `docs/<môn>/bai-giang/<slug>.md` | Phần chính của skill |
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

Trường slide là **chuỗi thuần**, không phải Markdown/LaTeX: công thức viết bằng Unicode đọc được (`P(A|B) = P(A∩B) / P(B), P(B)>0`, `x_{k+1} = x_k − η∇f(x_k)`). Giữ điều kiện ngay trong chuỗi công thức hoặc trong bullet cạnh nó. Dấu nháy đơn trong chuỗi JS phải được escape hoặc dùng nháy kép “ ”.

Tiêu chuẩn một slide catalog: tiêu đề là một kết luận hoặc câu hỏi có nội dung; 2–4 bullet, mỗi bullet là câu trọn nghĩa; `formula` khi bài có công thức trung tâm; `example` khi một con số cụ thể làm ý rõ hơn. Mỗi bài thường 3–6 slide, theo mạch của Notes. Slide là bản ôn nhanh của Notes, không chứa khẳng định mà Notes không có.

Chạy `node -e "import('./docs/.vitepress/course-catalog.mjs').then(m=>console.log(m.courseCatalog.length))"` sau khi sửa để bắt lỗi cú pháp.

## 5. Kiến thức nền và Wiki

Mỗi `id` trong `prerequisites` phải tồn tại ở **cả ba** chỗ, nếu không `verify-courses.mjs` fail hoặc `relatedConcepts()` ném lỗi:

1. `docs/.vitepress/concepts.mjs`: `'<id>': term('Tên', ['alias 1','alias 2'], 'định nghĩa', 'ví dụ', 'khi nào dùng', 'câu hỏi tự kiểm', 'đáp án')`. Tab Kiến thức nền in thẳng năm chuỗi này bằng `{{ }}` của Vue: **văn bản thuần, không Markdown, không `$…$`**. Viết ký hiệu bằng Unicode (∇f, x ∈ A, P(A|B)). Định nghĩa phải tự đứng được vì người học có thể chỉ đọc tab này.
2. `docs/.vitepress/wiki-content.mjs`: thêm `id` vào đúng một nhóm trong `wikiGroups`, và thêm `wikiDetails['<id>']` (đoạn “Giải thích kỹ thuật”, Markdown, có thể nhiều đoạn với `\n\n`). Có thể thêm `connections['<id>']` để chỉ định thuật ngữ liên quan; mọi id trong đó phải tồn tại.
3. `docs/wiki/<id>.md`: `npm run sync:courses` tự sinh từ hai file trên nếu chưa có; sau đó sửa trực tiếp file này (build không ghi đè). File phải chứa `## Giải thích kỹ thuật`.

`aliases` quyết định liên kết tự động: `term-links.mjs` nối **lần xuất hiện đầu tiên trong mỗi đoạn inline** của Notes/Wiki tới `/wiki/<id>.html`, bỏ qua tiêu đề, code, công thức và link có sẵn; so khớp không phân biệt hoa thường và theo ranh giới từ. Chọn alias đúng cách người Việt viết trong bài, kể cả biến thể (“véc-tơ”, “vector”). Tránh alias quá chung (“hàm”, “tập”) vì sẽ gắn link nhầm khắp nơi.

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
- Dùng LaTeX trong chuỗi slide → hiện nguyên ký tự `\frac`.
- Container quên `:::` đóng → nuốt phần còn lại của bài.
- Đặt hình ở chỗ khác `img/<lec>/` cạnh bài rồi viết đường dẫn tay → dễ gãy khi site chạy dưới `/StudyHub/`. Giữ quy ước đường dẫn tương đối như các bài hiện có và xem trang đã build.
- Viết `$…$` hoặc `**…**` trong `concepts.mjs` → tab Kiến thức nền hiện nguyên ký tự.
- Sửa `docs/wiki/<id>.md` nhưng không sửa `concepts.mjs` → định nghĩa trong tab Kiến thức nền (lấy từ concepts) và trang Wiki lệch nhau.


## Quy tắc giao diện Mực tím trên giấy vở

- Notes là tab mặc định; thứ tự Notes, Slides, Kiến thức nền. Địa chỉ cũ `#bai-tap` chuyển về Notes. Bài tập môn ở cuối Notes.
- Không chèn mục lục trong Markdown: VitePress có mục lục bên phải và trên điện thoại.
- Tiêu đề viết bằng chữ; không đặt công thức trong heading vì mục lục làm mất ký hiệu.
- Công thức trong Notes và Wiki dùng `$…$`; chữ tiếng Việt nằm ngoài công thức.
- Màu lấy từ `docs/.vitepress/theme/tokens.css`. SVG nội tuyến dùng biến token; SVG tĩnh dùng bảng màu sáng và đặt trên giấy trắng khi tối.
- Chữ SVG tối thiểu 14 đơn vị; chữ trong hình không dưới 12 đơn vị.
