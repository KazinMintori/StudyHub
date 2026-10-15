> Rà soát của Codex: Cả hai lượt cầu nối trả lỗi expected string or bytes-like object, got NoneType sau khi có tệp đầu ra. Không coi trạng thái cầu nối là thành công. Đã giữ worktree và bản chụp, rà đủ năm đường dẫn, tái hiện ba lỗi HTML và kiểm tra bản sửa độc lập. Bản web trước thay đổi truyền khoảng1.26MB HTML gzip và21KB JavaScript lean, không phải24MB dữ liệu mạng mỗi lần mở trực tiếp. Bản HTML giải nén có2179 công thức và94 thẻ ảnh. Tối ưu ảnh/font không tự giải quyết toàn bộ DOM lớn. Kết quả số liệu nằm tại qa/physics/chapter38/public-loading-baseline.json. Build và kiểm tra font trên bản xuất cuối do GitHub Actions đảm nhiệm.

# Báo Cáo Rà Soát Tối Ưu Tải Trang Và Nạp Sớm Phông Chữ (Loading Performance Review)

- **Người thực hiện**: Antigravity (AGY Agent) — Đợt hiệu chỉnh CORRECTION 1.
- **Ngày hoàn thành**: 2026-10-15.
- **Phạm vi tác vụ**: Khắc phục triệt để 3 lỗi phân tích HTML trong `injectHtmlImgAttributes`, bảo toàn nạp ảnh gốc (native image loading) và nạp sớm phông chữ giới hạn chuẩn xác (bounded emitted-font preloads) theo kế hoạch `docs/agy-plans/2026-10-15-loading-performance.md`.
- **Môi trường**: Worktree cô lập `C:/Users/Ai/.codex/worktrees/studyhub-loading-agy/StudyHub` trên nhánh detached HEAD tại baseline `f87deef`.
- **Ủy quyền**: `dangerously_skip_permissions=true` được người dùng xác nhận và ghi nhận tường minh ngày 2026-10-15.

---

## 1. Danh Mục Tệp Thuộc Quyền Sở Hữu (Owned Files)

Đúng 5 đường dẫn theo phạm vi được giao, không chỉnh sửa bất kỳ tệp nào khác ngoài danh sách:
1. `scripts/build/markdown-presentation.mjs`: Phân tích HTML vững chắc cho ảnh, chú thích, script/style và tên thuộc tính chính xác; bổ sung theo dõi trạng thái `tagState` (`inScript`, `inStyle`) và ruler `study_image_loading`.
2. `docs/.vitepress/config.mjs`: Tích hợp hook `transformHead` gọi bộ nạp sớm phông chữ từ asset thực tế.
3. `scripts/build/font-preloads.mjs`: Module trích xuất và lọc các tệp phông chữ phát sinh thực tế phục vụ preload.
4. `scripts/tests/loading-performance.test.mjs`: Bộ kiểm thử tự động toàn diện cho nạp ảnh, phông chữ và 4 bài kiểm thử hồi quy hành vi tập trung (behavioral regressions).
5. `raw_materials/physics/reviews/loading-performance-agy-review.md`: Báo cáo đối chiếu và giải trình kỹ thuật này.

---

## 2. Các Lỗi Phân Tích HTML Đã Tái Hiện Và Biện Pháp Xử Lý (CORRECTION 1 Fixes)

Supervisor đã tái hiện 3 lỗi làm sai lệch HTML trong hàm `injectHtmlImgAttributes`:

### 2.1. Lỗi 1: Ký tự `>` trong thuộc tính có dấu ngoặc kép và nhầm lẫn `data-loading`
- **Hiện tượng**: Thẻ `<img src="sample.png" data-loading="custom" alt="x > y">` bị biến đổi thành `<img ... alt="x decoding="async" > y">`.
- **Nguyên nhân cốt lõi**:
  1. Biểu thức chính quy cũ sử dụng `[^>]*?` để quét thuộc tính, khiến biểu thức dừng ngay tại ký tự `>` bên trong chuỗi `alt="x > y"`, cắt đứt giá trị thuộc tính và chèn thuộc tính mới vào giữa chuỗi.
  2. Kiểm tra `\bloading\s*=` dùng ranh giới từ `\b`. Do dấu gạch nối `-` trong `data-loading` không phải ký tự từ (`\w`), ranh giới từ `\b` khớp ngay trước chữ `l`, nhận diện nhầm `data-loading` thành `loading`.
- **Giải pháp**:
  - Viết lại bộ quét thẻ ảnh hỗ trợ giá trị thuộc tính nằm trong dấu nháy kép `"[^"]*"`, nháy đơn `'[^']*'` hoặc không có nháy: `(<img\b)((?:[^>"']|"[^"]*"|'[^']*')*?)(\s*\/?>)`. Nhờ đó, ký tự `>` nằm trong dấu nháy được bảo toàn nguyên vẹn 100%.
  - Xây dựng hàm `hasExactAttribute(attrs, attrName)` phân tích chính xác tên thuộc tính theo chuẩn HTML5: Phải được phân tách bằng khoảng trắng và chỉ so khớp đúng tên thuộc tính độc lập (`loading` hoặc `decoding`), không nhận nhầm `data-loading`, `my-loading`, `loading-mode` hay từ `loading` nằm trong giá trị chuỗi.

### 2.2. Lỗi 2: Thẻ `<script>` chứa chuỗi ảnh bị đột biến và tiêu tốn lượt nạp eager
- **Hiện tượng**: `<script>const marker = '<img src="not-an-image.png">';</script>` bị can thiệp chèn thuộc tính nạp ảnh và làm mất trạng thái `loading="eager"` của ảnh nội dung thật phía sau.
- **Nguyên nhân cốt lõi**: Thẻ `<script>` chứa thẻ ảnh giả lập bị `injectHtmlImgAttributes` xử lý như ảnh thật. Đồng thời, trong ngữ cảnh inline của markdown-it, các thẻ HTML inline có thể bị tách thành các token riêng biệt.
- **Giải pháp**:
  - Nhận diện toàn khối `<script\b[\s\S]*?<\/script>` và `<style\b[\s\S]*?<\/style>` trong `HTML_TOKEN_RE`, giữ nguyên vẹn từng byte (byte-for-byte unchanged) và tuyệt đối không gọi `getLoadingAttrs()`.
  - Bổ sung cơ chế theo dõi trạng thái `tagState` (`inScript`, `inStyle`) trong ruler `study_image_loading` khi duyệt qua các token con inline, đảm bảo bất kỳ token HTML nào nằm trong cặp thẻ script/style chưa đóng đều được bỏ qua an toàn.

### 2.3. Lỗi 3: Chú thích HTML `<!-- <img src="comment.png"> -->` bị đột biến và đẩy ảnh thật thành lazy
- **Hiện tượng**: Ảnh nằm trong chú thích HTML `<!-- ... -->` bị xử lý và khiến ảnh nội dung thật tiếp theo nhận `loading="lazy"`.
- **Nguyên nhân cốt lõi**: Chú thích không được loại trừ trước khi quét thẻ ảnh, làm tăng chỉ số `contentImageIndex`.
- **Giải pháp**: Nhánh `<!--[\s\S]*?(?:-->|$)` trong `HTML_TOKEN_RE` nhận diện chú thích HTML và trả về nguyên trạng từng byte, không tiêu tốn lượt ảnh đầu tiên. Nhờ đó, ảnh nội dung thật đầu tiên luôn giữ vững trạng thái `loading="eager"`.

---

## 3. Nội Dung Kỹ Thuật Tổng Thể (System Architecture)

### 3.1. Nạp ảnh gốc và giải mã bất đồng bộ (Native Image Loading & Async Decoding)
- **Quy tắc thứ tự xuất hiện (Eager-first, Lazy-later)**:
  - Ảnh nội dung thật đầu tiên trên mỗi trang luôn nhận `loading="eager"` để trình duyệt tải ngay lập tức, tối ưu LCP.
  - Các ảnh nội dung tiếp theo nhận `loading="lazy"` để tiết kiệm băng thông và bộ nhớ.
  - Mọi ảnh nội dung đều nhận `decoding="async"` để giải mã ngoài luồng chính.
- **Bảo toàn thuộc tính tường minh**: Giữ nguyên 100% các giá trị `loading` hoặc `decoding` do tác giả chủ động khai báo trước đó.
- **Bảo toàn thành phần học thuật**: Toàn bộ chú thích `<figcaption>`, danh sách song ngữ đối chiếu từ `physicsImageLabels`, nhãn thuật ngữ `termLinks` và công thức toán MathJax đều nguyên vẹn.

### 3.2. Nạp sớm phông chữ giới hạn chuẩn xác (Bounded Emitted-Font Preloads)
- **Nhắm đúng asset phát sinh thực tế (Same emitted woff2 assets)**: Không tạo URL giả mạo, không đoán mã hash, không tạo bản sao thừa, không trỏ vào đường dẫn `/node_modules` và không sử dụng CDN bên ngoài.
- **Giới hạn nghiêm ngặt ở 4 tệp trọng số bình thường**:
  1. `Source Serif 4 Variable`: Tập ký tự Latin chuẩn (`source-serif-4-latin-standard-normal-*.woff2`).
  2. `Source Serif 4 Variable`: Tập ký tự Tiếng Việt chuẩn (`source-serif-4-vietnamese-standard-normal-*.woff2`).
  3. `Be Vietnam Pro`: Trọng số 400 tập Latin chuẩn (`be-vietnam-pro-latin-400-normal-*.woff2`).
  4. `Be Vietnam Pro`: Trọng số 400 tập Tiếng Việt chuẩn (`be-vietnam-pro-vietnamese-400-normal-*.woff2`).
- **Hỗ trợ đa môi trường base**: Đồng bộ với cả base production (`/StudyHub/`) lẫn base local/root (`/`).

---

## 4. Kết Quả Xác Minh (Verification Commands & Test Output)

Toàn bộ các lệnh kiểm thử và kiểm tra cú pháp bắt buộc đều vượt qua 100%:

```bash
# 1. Chạy bộ kiểm thử hiệu năng tải trang và bộ kiểm thử cache toán học
node --test scripts/tests/loading-performance.test.mjs scripts/tests/static-math-cache.test.mjs
```
**Kết quả thực tế (21/21 passed, 0 failed)**:
```text
✔ single standalone image becomes figure with eager loading and async decoding (10.05ms)
✔ multiple images: first is eager and later images are lazy by default (3.58ms)
✔ avoids eager-loading all figures: inline first image makes subsequent figure lazy (2.28ms)
✔ preserves explicit loading and decoding attributes on images (3.51ms)
✔ preserves captions, bilingual labels and math markup intact (34.63ms)
✔ resets image count per document render (2.43ms)
✔ regression (1): preserves > inside quoted attributes and recognizes data-loading is not loading attribute (2.03ms)
✔ regression (2): script and style blocks remain byte-for-byte unchanged and do not consume first-image status (2.38ms)
✔ regression (3): HTML comments remain byte-for-byte unchanged and do not make the real image lazy (3.22ms)
✔ regression (all 3 combined): mixed document with comments, scripts, custom attributes, and multiple images (2.13ms)
✔ bounds font preloads to primary normal-weight Latin and Vietnamese subsets (0.68ms)
✔ generateFontPreloads produces valid HeadConfig tuples with correct attributes (0.25ms)
✔ supports development base (/) and production base (/StudyHub/) (0.17ms)
✔ never manufactures font URLs when assets are empty or unavailable (0.59ms)
✔ deduplicates with existing head tags (0.17ms)
✔ identical expressions reuse rendering and keep the same binding (1.24ms)
✔ inline and display modes have separate cached results (0.20ms)
✔ numbered Physics equations share expressions and retain each tag (0.24ms)
✔ labelled expressions bypass the cache because references can change (0.15ms)
✔ render failure restores a numbered token and does not cache the error (0.26ms)
✔ real MathJax markup is preserved inside the escaped Vue binding (37.03ms)
ℹ tests 21
ℹ suites 0
ℹ pass 21
ℹ fail 0
ℹ cancelled 0
ℹ skipped 0
ℹ todo 0
ℹ duration_ms 419.75
```

```bash
# 2. Kiểm tra cú pháp tĩnh các module đã sửa đổi
node --check scripts/build/font-preloads.mjs
node --check scripts/build/markdown-presentation.mjs
node --check docs/.vitepress/config.mjs
```
**Kết quả thực tế**: Mã thoát 0, không có bất kỳ lỗi cú pháp nào.

```bash
# 3. Kiểm tra tính toàn vẹn git và không vi phạm quy chuẩn diff
git status --short
git diff --check
git diff --name-only
```
**Kết quả thực tế**: `git diff --check` sạch hoàn toàn, không có lỗi whitespace hay định dạng. Thay đổi chỉ nằm trong đúng các tệp được giao.

---

## 5. Giới Hạn Đo Đạc, Rào Cản Và Trạng Thái Hoàn Thành

- **Giới hạn đo đạc thực tế (Measurement Limits)**:
  - Báo cáo này tuyệt đối không đưa ra các tuyên bố chưa qua đo lường thực tế (như "tăng tốc tải trang X%" hay "loại bỏ hoàn toàn FOUT"). Hiệu quả thực tế của việc nạp phông chữ và nạp ảnh phụ thuộc vào điều kiện mạng, thiết bị người dùng và hành vi bộ đệm trình duyệt, cần được theo dõi qua các chỉ số RUM/Web Vitals sau khi deploy.
  - Trong môi trường dev (`vitepress dev`), Vite sử dụng cơ chế on-demand HMR nên `TransformContext.assets` chỉ sẵn sàng trong lượt xuất tĩnh tĩnh (build).
- **Tuân thủ quy định không build toàn cục cục bộ**: Hoàn toàn tuân thủ `AGENTS.md`, không tự ý chạy `npm run ci:build` trên máy cục bộ của người dùng để tránh nghẽn CPU và RAM. Khâu đóng gói tĩnh toàn cục được ủy thác tự động 100% cho GitHub Actions CI.
- **Rào cản và lỗi phân quyền (Blockers & Permissions)**: Không gặp bất kỳ lỗi phân quyền hay rào cản kỹ thuật nào trong suốt quá trình thực thi.
- **Trạng thái cuối cùng**: `COMPLETED_READY_FOR_CODEX_REVIEW`.
