# StudyHub — Nền Tảng Bài Giảng & Ôn Tập UET

**StudyHub** là website tài liệu học tập, giáo trình chuyên sâu và bài giảng ôn tập chất lượng cao dành cho sinh viên trường Đại học Công nghệ (UET) - Đại học Quốc gia Hà Nội. Trang web được xây dựng nhằm mang đến trải nghiệm học tập tập trung, khoa học và trực quan trên nền tảng VitePress.

- **Website trực tuyến**: [kazinmintori.github.io/StudyHub](https://kazinmintori.github.io/StudyHub/)
- **Mã nguồn**: [KazinMintori/StudyHub](https://github.com/KazinMintori/StudyHub)

---

## 1. Điểm Nổi Bật

### Mô hình bài giảng 4-trong-1
Mỗi bài học trên StudyHub là một thực thể hoàn chỉnh, tích hợp 4 góc độ tiếp cận trên cùng một giao diện:
- **Notes (Giáo trình chi tiết)**: Lập luận chặt chẽ, mở các bước biến đổi toán học/thuật toán phức tạp, gắn liền bản chất lý thuyết với bài toán thực tiễn.
- **Slides (Thẻ ôn tập nhanh)**: Dàn ý chắt lọc, công thức trọng tâm và ví dụ then chốt, giúp sinh viên nắm bắt nhanh cấu trúc bài học và ôn tập trước kỳ thi.
- **Cheatsheet (Bảng tra cứu)**: Tổng hợp nhanh công thức cốt lõi, bảng tra cứu, quy tắc tính và các "bẫy thi" thường gặp.
- **Kiến thức nền & Wiki Thuật ngữ**: Liên kết đa chiều giữa bài giảng và hệ thống Bách khoa khái niệm (`docs/wiki/`). Tự động nhận diện thuật ngữ, cung cấp định nghĩa, trực giác, ví dụ và câu hỏi tự kiểm tra.

### Chuẩn mực hiển thị toán học & Đồ họa
- **Công thức TeX/KaTeX chuẩn mực**: Hiển thị sắc nét, tối ưu hóa giao diện chống tràn (tuyệt đối không xuất hiện thanh cuộn ngang) trên mọi kích thước màn hình, bao gồm cả thiết bị di động.
- **Sơ đồ Mermaid & Mô phỏng tương tác**: Trực quan hóa các khái niệm trừu tượng thông qua component `<CodeIllustration />` (Tìm kiếm không gian trạng thái, Gradient Descent, Định lý Bayes, Mô phỏng điện trường, MapReduce,...).

### Góc học tập cá nhân hóa
- **Đồng hồ Pomodoro**: Chế độ tập trung 25/50 phút, tự động duy trì thời gian khi chuyển trang hoặc tải lại.
- **Bộ Flashcards**: Hệ thống thẻ phản xạ kiến thức theo từng học phần, lưu trữ tiến độ ghi nhớ.
- **Sổ tay Markdown**: Ghi chú cá nhân riêng cho từng môn học, tự động lưu cục bộ (Local Storage), xem trước an toàn và hỗ trợ xuất file `.md`.
- **Theo dõi tiến độ**: Đánh dấu bài đã học, tự động ghi nhớ và gợi ý tiếp tục bài học gần nhất từ trang chủ.

---

## 2. Cấu Trúc Dự Án

```text
StudyHub/
├── docs/                      # Nội dung bài giảng và tài liệu VitePress
│   ├── .vitepress/            # Cấu hình VitePress, theme và dữ liệu catalog
│   │   ├── course-catalog.mjs # Quản lý danh mục môn học, bài giảng và Slides
│   │   ├── cheatsheets.mjs    # Dữ liệu bảng tra cứu và công thức Cheatsheet
│   │   ├── concepts.mjs       # Danh mục các khái niệm nền tảng
│   │   └── theme/             # Giao diện người dùng (Vue 3 components, CSS tokens)
│   ├── wiki/                  # Hệ thống bách khoa thuật ngữ độc lập
│   └── <môn-học>/             # Các môn học trong chương trình
│       └── bai-giang/         # Các bài giảng chi tiết dạng Markdown
├── scripts/                   # Bộ script kiểm tra, kiểm định chất lượng và đồng bộ
└── .agents/skills/            # Kỹ năng và công cụ hỗ trợ biên soạn bài giảng
```

---

## 3. Cài Đặt & Chạy Cục Bộ

### Yêu cầu môi trường
- **Node.js**: Phiên bản 20 hoặc 22 trở lên.
- **npm**: Đi kèm với Node.js.

### Khởi chạy môi trường phát triển

```sh
# 1. Cài đặt các gói phụ thuộc
npm ci

# 2. Khởi chạy máy chủ phát triển cục bộ
npm run dev
```

Sau khi chạy lệnh, truy cập `http://localhost:5173` trên trình duyệt. Khi chỉnh sửa nội dung trong `docs/`, trang web sẽ tự động cập nhật (Hot Module Replacement).

### Đóng gói & Xem trước bản tĩnh

```sh
# Đồng bộ dữ liệu môn học và đóng gói website tĩnh vào dist/
npm run build

# Xem trước bản đóng gói
npm run preview
```

Để chạy thử bản tĩnh bằng máy chủ HTTP đơn giản:

```sh
python -m http.server 8080 --directory dist
```

Mỗi khi có commit được đẩy lên nhánh `main`, quy trình GitHub Actions sẽ tự động kiểm tra, chạy `npm run ci:build` và xuất bản website lên GitHub Pages.

---

## 4. Kiểm Thử & Đảm Bảo Chất Lượng

Dự án áp dụng quy trình kiểm định nghiêm ngặt để đảm bảo chất lượng bài giảng và tính toàn vẹn của hệ thống:

```sh
# 1. Kiểm tra quá trình build VitePress
npm run ci:build

# 2. Kiểm tra liên kết catalog, Wiki, hình ảnh và cấu trúc bài giảng
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all

# 3. Chạy bộ bài kiểm thử tự động của skill biên soạn
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py

# 4. Kiểm tra toàn diện môn học, liên kết và mô phỏng
node scripts/verify-courses.mjs

# 5. Kiểm tra tính tương thích giao diện trên nhiều kích thước màn hình
node scripts/verify-ui.mjs
```

---

## 5. Tiêu Chuẩn Sư Phạm & Biên Soạn

Mọi bài giảng trên StudyHub tuân theo chuẩn mực:
- **Chủ quyền bài giảng**: Là tài liệu giảng dạy độc lập, hoàn chỉnh, dẫn dắt trực quan từ bản chất vấn đề đến mô hình toán học và thuật toán.
- **Chính xác tuyệt đối**: Giữ đúng giả thiết, miền xác định, các bước suy luận và số liệu tính toán.
- **Không thanh cuộn trên công thức**: Mọi công thức toán học dài đều được bẻ dòng bằng `\begin{aligned}` với `\\` và `&`, đảm bảo giao diện đọc thoáng đãng trên cả máy tính lẫn điện thoại di động.
