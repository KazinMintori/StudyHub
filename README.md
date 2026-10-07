# UET Study Hub

Website: [kazinmintori.github.io/StudyHub](https://kazinmintori.github.io/StudyHub/).

Repository: [KazinMintori/StudyHub](https://github.com/KazinMintori/StudyHub). Mỗi lần push vào `main`, GitHub Actions sẽ build và cập nhật website trên GitHub Pages.

Website bài giảng và ôn tập dùng [quancn12/Study_UET](https://github.com/quancn12/Study_UET) làm nền tảng VitePress. Giữ lại các học phần, bài giảng Markdown, tìm kiếm, công thức MathJax và sơ đồ Mermaid của source gốc.

Trang chủ được thiết kế lại theo hướng tối giản, bỏ emoji trang trí. Tích hợp các chức năng từ `index.html` cũ: Pomodoro, flashcard, ghi chú Markdown và mô phỏng điện trường. Bản gốc nằm ở `backups/index-original.html`.

## Chạy dự án

```sh
npm ci
npm run dev
```

Mở `http://localhost:5173`. Sửa nội dung trong `docs/`; các component giao diện nằm trong `docs/.vitepress/theme/`.

```sh
npm run build
npm run preview
```

Build tạo website tĩnh trong `dist/`, đồng thời xuất `index.html`, các trang và assets ra thư mục gốc để tương thích với cách phục vụ web cũ. `index.html` là file sinh tự động; chỉnh trang chủ tại `docs/index.md` và `StudyHome.vue`.

Để chạy bản tĩnh bằng một server đơn giản:

```sh
python -m http.server 8080 --directory dist
```

GitHub Actions sử dụng Node.js 22, chạy `npm run ci:build` và xuất bản thư mục `docs/.vitepress/dist`. `BASE_PATH` được đặt theo tên repository để hỗ trợ đường dẫn con `/StudyHub/`. `npm run build` vẫn tạo bản preview tĩnh cục bộ như trước.

## Công cụ học

- Pomodoro 25/50 phút, nghỉ 5 phút; giữ thời gian qua chuyển trang và tải lại.
- 15 flashcard thuộc 5 học phần, đáp án và tiến độ đã nhớ.
- Sổ Markdown riêng từng học phần, tự lưu, xem trước an toàn và xuất `.md`. Ghi chú cũ cùng origin được giữ lại trong sổ chung.
- Mô phỏng điện trường: thêm điện tích bằng chuột/chạm hoặc nút, xóa từng điện tích, xem trường tổng hợp.
- Đánh dấu bài đã học và tiếp tục bài gần nhất từ trang chủ.

Dữ liệu cá nhân được lưu cục bộ bằng localStorage; chưa đồng bộ giữa thiết bị. Các bài đang biên soạn được ghi rõ, và Slides chỉ tóm tắt Notes đã có nội dung.

## Cấu trúc môn học

Mỗi môn liệt kê các bài giảng. Mỗi bài có **Slides / Notes / Kiến thức cần có** trên cùng một trang, với các địa chỉ `#slides`, `#notes`, `#kien-thuc-can-co`. Nội dung chi tiết nằm trong `docs/<môn>/bai-giang/<bài>.md`. `docs/.vitepress/course-catalog.mjs` quản lý môn, bài học, danh sách nền tảng của từng bài và Slides có thuộc tính `note` chỉ bài tương ứng.

Các đường dẫn Notes cũ chuyển tiếp tới bài giảng; tiến độ cũ được giữ lại. Snapshot trước lần tổ chức theo bài nằm ở `backups/before-lecture-wiki/`. Phần ghi chú cá nhân trong Góc học tập vẫn là một công cụ riêng, khác Notes bài giảng.

Wiki nằm trong `docs/wiki/`, mỗi thuật ngữ là một file Markdown độc lập có giải thích kỹ thuật, ví dụ, câu hỏi tự kiểm tra và liên kết tới bài khác. Plugin `term-links.mjs` liên kết thuật ngữ trong Notes và Wiki, tránh tự liên kết bài Wiki với chính nó hoặc chèn vào code, công thức, tiêu đề và link sẵn có. Xem trước hỗ trợ chuột và bàn phím. Wiki có liên kết ngược và danh sách bài giảng dùng khái niệm đó. `wiki-content.mjs` cung cấp nội dung khởi tạo và quan hệ giữa khái niệm; các bài Wiki đã có không bị ghi đè khi build.

Nhúng minh họa trong Markdown bằng `<CodeIllustration type="search" />`. Các loại: `search`, `gradient`, `bayes`, `broadcast`, `mapreduce`, `field`. Mô hình tính toán nằm trong `theme/illustrations.js` và được kiểm tra bằng test. Component được đăng ký toàn cục nên bài học không cần tự import.

`npm run sync:courses` đồng bộ danh sách môn và đường dẫn chuyển tiếp; không ghi đè bài giảng hoặc Wiki đã có. Build tự chạy bước này. Khi thêm bài, tạo file trong `bai-giang/`, khai báo `course`, `lecture`, `section: lecture`, `lessonStatus`, rồi thêm tên bài, nền tảng cần có và Slides vào catalog.

`node scripts/verify-courses.mjs` kiểm tra cả 8 môn, ba phần theo từng bài, Wiki, liên kết qua lại, tiến độ, đường dẫn cũ, minh họa và bố cục. Dùng `QA_URL` để chọn server cần kiểm tra; mặc định là `http://127.0.0.1:8080`.

## Kiểm tra giao diện

`scripts/verify-ui.mjs` kiểm tra chức năng và bố cục tại 375, 768, 1024, 1440 px, tạo ảnh kiểm tra trong `qa/`. Chạy server trước, rồi:

```sh
node scripts/verify-ui.mjs
```

Có thể đặt `QA_URL` để kiểm tra bản preview và `PUPPETEER_EXECUTABLE_PATH` để dùng Chrome đã cài. Nếu chưa có Chrome cho Puppeteer, chạy `npx puppeteer browsers install chrome`.
