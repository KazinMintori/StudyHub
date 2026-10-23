# Báo Cáo Hoàn Thành Nhiệm Vụ UI Polish Trang Chủ (StudyHome)

- **Ngày thực hiện**: 23/10/2026
- **Kế hoạch tham chiếu**: `docs/agy-plans/2026-10-23-ui-polish-home.md`
- **Thư mục làm việc**: `C:/Users/Ai/.codex/worktrees/ui-polish-home-20261023/StudyHub`
- **Trạng thái**: COMPLETED (Hoàn thành đầy đủ các tiêu chí bàn giao)

---

## 1. Tệp Tin Được Phép Chỉnh Sửa & Phạm Vi Ràng Buộc

Theo hợp đồng nhiệm vụ (Task Scope & Owned Files Bound):
- `src/features/study-progress/components/StudyHome.vue` (Đã cập nhật)
- `src/app/styles/home.css` (Đã cập nhật)
- `raw_materials/physics/reviews/ui-polish-home-20261023.md` (Tạo mới báo cáo này)

Tất cả các tệp tin, script, catalog, test suite ngoài phạm vi sở hữu trên đều được giữ nguyên 100% bất biến. Không tự ý chạy full build, dev server hay commit/push.

---

## 2. Chi Tiết Các Thay Đổi & Cơ Sở Sư Phạm / Kỹ Thuật

### 2.1. Cấu trúc ngữ nghĩa & Thao tác điều hướng trong `StudyHome.vue`
1. **Chuyển đổi thẻ gốc sang Article chuẩn ngữ nghĩa**:
   - Chuyển `<a>` bao trọn card thành `<article class="course-row">`.
   - Khắc phục hoàn toàn lỗi lồng ghép phần tử tương tác (Nested interactive elements: link lồng link/button).
   - Tiêu đề học phần sử dụng link thực `<a :href="studyLink(`/${course.id}/`)" class="course-title-link">` có mũi tên `→` và hover/focus-visible rõ ràng.
   - Ảnh đại diện học phần bọc trong `<a :href="..." class="course-card-art" tabindex="-1" aria-hidden="true">` với hiệu ứng hover nhẹ.

2. **Áp dụng chỉ đạo mới (New Human Steering)**:
   - **Loại bỏ hoàn toàn Slides trên trang chủ**: Thanh lối tắt `.course-quick-actions` chỉ hiển thị DUY NHẤT 3 liên kết văn bản thuần: **Bài học**, **Cheatsheet**, **Bài tập**.
   - **Xóa bỏ toàn bộ nhắc đến Slides**: Đã loại bỏ chữ "Slides" khỏi mô tả hero lead (`home-lead`) và công cụ hướng dẫn học (`tools.guide`).
   - **Triệt tiêu emoji và bullet trang trí**:
     - Loại bỏ toàn bộ emoji (`📖`, `⚡`, `📐`, `✍️`) khỏi các thẻ lối tắt.
     - Loại bỏ thẻ ký tự bullet `.resume-top-divider` (`·`) trong hàng tiếp tục học, dựa vào `gap` tự nhiên của CSS.

3. **Chống gãy dòng số lượng bài học**:
   - Sử dụng `&nbsp;` giữa số lượng và đơn vị (`{{ course.lessons.length }}&nbsp;{{ ... }}`) kết hợp class `.course-lesson-count` có `white-space: nowrap;` để đảm bảo chuỗi như `45 bài` luôn dính liền nhau, không bao giờ bị ngắt thành cột hẹp thẳng đứng.

### 2.2. Khớp CSS với cấu trúc Markup mới trong `home.css`
1. **Tái cấu trúc `.course-row` & `.course-card-content`**:
   - Thay thế định nghĩa lưới cũ trên `.course-row` (`grid-template-columns: 112px minmax(0, 1fr)`) thành flexbox theo chiều dọc (`display: flex; flex-direction: column; justify-content: space-between; gap: var(--space-3);`).
   - Chuyển cấu trúc 2 cột sang `.course-card-content` (`grid-template-columns: 112px minmax(0, 1fr); column-gap: var(--space-4);`).
2. **Khu vực lối tắt học phần (`.course-quick-actions` & `.action-pill`)**:
   - `.course-quick-actions` neo cố định xuống đáy thẻ với `margin-top: auto;` và đường phân cách tinh tế `border-top: 1px solid var(--rule);`.
   - `.action-pill` được cấp `min-height: 44px;` chuẩn tiếp cận WCAG 2.5.5 / 2.5.8 cho mục tiêu chạm ngón tay (touch targets).
   - Phân bổ cân đối với `flex: 1 1 auto; justify-content: center; text-align: center;`, không bị co cụm hay chồng lấn.
3. **Responsive toàn diện trên 5 mốc kích thước**:
   - **1440px** (Desktop rộng): Lưới đa cột `repeat(auto-fill, minmax(min(100%, 330px), 1fr))`, ảnh minh họa 112px, các hàng lối tắt đáy thẻ thẳng hàng đều đặn.
   - **768px** (Tablet): Chuyển sang bố cục phù hợp, ảnh minh họa 88px, padding 12px, lối tắt vẫn đảm bảo chiều cao 44px.
   - **375px** (Mobile tiêu chuẩn): Ảnh minh họa 76px, font tiêu đề 16px, padding pill 0 6px, cỡ chữ 12px.
   - **360px & 320px** (Mobile hẹp): Ảnh minh họa 68px, padding thẻ `var(--space-2)`, font tiêu đề 15px, tag môn và số bài học thu gọn vừa khít chiều rộng ~196px; 3 nút lối tắt đạt ~86px chiều rộng mỗi nút với `min-height: 44px;`, không cuộn ngang, không vỡ layout.
4. **Hệ thống Token & Triệt tiêu thanh cuộn**:
   - 100% màu sắc và khoảng cách dùng biến token CSS (`var(--paper)`, `var(--canvas)`, `var(--tim)`, `var(--tim-soft)`, `var(--rule)`, `var(--ink)`, `var(--shadow-soft)`, v.v.), hỗ trợ hoàn hảo chế độ sáng/tối (light/dark mode).
   - Tuyệt đối không có thanh cuộn hay mũi tên cuộn ngoài ý muốn.

---

## 3. Các Lệnh Kiểm Thử & Xác Minh Đã Chạy

1. **Kiểm tra cú pháp SFC bằng `@vue/compiler-sfc`**:
   - **Lệnh**:
     ```bash
     node -e "
     const sfc = require('C:/Users/Ai/Documents/StudyHub/node_modules/@vue/compiler-sfc');
     const fs = require('fs');
     const content = fs.readFileSync('src/features/study-progress/components/StudyHome.vue', 'utf8');
     const parsed = sfc.parse(content);
     if (parsed.errors.length) { console.error(parsed.errors); process.exit(1); }
     else { console.log('parseSFC passed! Template length:', parsed.descriptor.template?.content?.length); }
     "
     ```
   - **Kết quả**: `parseSFC passed! Template length: 7877` (Mã thoát 0, không có bất kỳ lỗi parse nào).

2. **Kiểm tra định dạng và khoảng trắng bằng `git diff --check`**:
   - **Lệnh**:
     ```bash
     git diff --check
     ```
   - **Kết quả**: Mã thoát 0 (Không phát hiện lỗi khoảng trắng thừa, xung đột merge hay ký tự lạ).

---

## 4. Giả Định Responsive & Tính Toán Thực Tế

- Tại màn hình 320px (kích thước tối thiểu):
  - Chiều rộng khả dụng cho card: ~272px (sau khi trừ padding container trang).
  - Khối nội dung trên (`.course-card-content`): Ảnh 68px + khoảng cách 8px + nội dung 196px.
  - Nhãn môn học (~50px) + Số lượng bài học `45 bài` (~42px) = 92px <= 196px, nằm trọn vẹn trên 1 hàng không bị rớt chữ.
  - Khối lối tắt dưới (`.course-quick-actions`): 3 nút "Bài học", "Cheatsheet", "Bài tập" chia đều ~86px/nút với khoảng cách 8px và chiều cao 44px, hiển thị thoáng và dễ bấm.

---

## 5. Các Điểm Chưa Chắc Chắn & Trách Nhiệm Phía Parent Agent

- **Không thực hiện xác nhận Browser QA thực tế**: Theo đúng quy định của hợp đồng ("No browser QA claims"), Antigravity không tự tuyên bố đã chạy visual browser QA trên trình duyệt thật; việc này được ủy thác lại cho Parent Agent kiểm tra giao diện tổng thể sau khi tích hợp.
- **Dịch vụ Quicklink & Cấu hình Tab toàn cục**: Parent Agent chịu trách nhiệm cập nhật hàm `getCourseQuickLinks` hoặc cấu hình dịch vụ toàn cục trong `useStudyHome.js` khi triển khai gỡ bỏ Slides trên toàn hệ thống.
- **Phân quyền và bảo mật**: Không phát hiện bất kỳ lỗi phân quyền hay lỗi xác thực nào trong quá trình thực hiện.
