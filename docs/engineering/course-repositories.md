# Repo chính và các repo học phần

Repo `KazinMintori/StudyHub` quản lý giao diện Vue, bộ máy VitePress, công cụ kiểm tra và workflow xuất bản. Mỗi học phần có một repo riêng tư mang tên `StudyHub-course-<id>`. GitHub Actions ghép nguồn trước khi kiểm tra và build. Người đọc vẫn truy cập một website với các đường dẫn cũ.

## 1. Cách ghép nguồn

`config/course-repositories.json` ghi repo, mã commit đầy đủ và phạm vi đường dẫn của từng học phần. Mỗi lần xuất bản chỉ sử dụng các commit đã khóa. Thay đổi trên nhánh `main` của repo học phần chưa tự động trở thành nội dung đang phát hành.

Mỗi repo học phần giữ nguyên cây đường dẫn tương đối, gồm `docs/<id>/`, `src/content/courses/<id>/` và các tài nguyên liên quan. Tệp `studyhub-course.json` ghi SHA-256 của từng tệp. Các module Wiki và cấu hình dùng chung vẫn nằm ở repo chính. Một số dữ liệu Vật lý dùng chung tiếp tục đi qua module tương thích hiện có.

Ngày cập nhật của bài được giữ trong metadata nguồn. Việc chuyển repo không làm toàn bộ bài giảng mang cùng ngày cập nhật mới. Khi xuất nội dung đã sửa, công cụ chỉ cập nhật ngày của những tệp thay đổi.

```text
Repo chính công khai
  config/course-repositories.json
       │ Khóa commit của từng học phần
       ▼
Các repo học phần riêng tư
       │ GitHub Actions đọc bằng deploy key riêng
       ▼
Kiểm tra → Build trên GitHub → Một website GitHub Pages
```

Việc tách repo giảm dung lượng checkout và phạm vi thay đổi của từng học phần. Tốc độ trình duyệt còn phụ thuộc vào tải dữ liệu theo nhu cầu, điều hướng và chi phí dựng trang. Trình duyệt không tải tài liệu từ API của các repo riêng tư.

## 2. Khởi tạo máy biên soạn

Tài khoản Git trên máy cần quyền đọc các repo học phần. Công cụ dùng HTTPS và Git Credential Manager trên máy cá nhân. Không ghi token vào file cấu hình.

```bash
npm ci
npm run courses:sync
npm run dev
```

Nguồn được tải vào `.course-repositories/<id>/` và ghép vào các đường dẫn quen thuộc trong workspace. Thư mục cache cùng các bản nguồn đã ghép không được commit lại vào repo chính. Công cụ kiểm checksum và từ chối ghi đè tệp đã được sửa tại máy.

## 3. Sửa một học phần

Biên soạn và kiểm tra tại các đường dẫn `docs/`, `raw_materials/` và `src/content/courses/` như trước. Sau khi hoàn tất, xuất thay đổi vào checkout riêng của học phần.

```bash
npm run courses:export -- toan-cho-ai
git -C .course-repositories/toan-cho-ai diff
git -C .course-repositories/toan-cho-ai switch -c update-lesson
git -C .course-repositories/toan-cho-ai add .
git -C .course-repositories/toan-cho-ai commit -m "Cập nhật bài giảng"
git -C .course-repositories/toan-cho-ai push origin HEAD
```

Sau khi kiểm tra và hợp nhất ở repo học phần, lấy mã commit đầy đủ rồi cập nhật phiên bản ở repo chính.

```bash
npm run courses:pin -- toan-cho-ai <commit-40-ky-tu>
npm run courses:sync
npm run courses:check
```

Commit thay đổi `config/course-repositories.json` cùng các thay đổi giao diện hoặc cấu hình liên quan ở repo chính. Khi cần quay lại phiên bản trước, đổi pin về commit cũ rồi đồng bộ. Những chỉnh sửa chưa xuất phải được lưu trước khi đổi pin.

PDF và PPTX nguồn vốn bị Git bỏ qua tiếp tục được giữ tại máy. Công cụ không tự đưa giáo trình lớn vào repo học phần. Tài liệu lớn cần cơ chế lưu trữ riêng khi được bổ sung vào quy trình.

## 4. Quyền truy cập khi xuất bản

Secret `STUDYHUB_COURSE_DEPLOY_KEYS` ở repo chính chứa bảng khóa SSH theo ID học phần. Mỗi khóa chỉ có quyền đọc một repo học phần. Workflow chỉ truyền secret vào bước ghép nguồn. Khóa tạm được xóa khi bước này kết thúc, kể cả khi tải nguồn thất bại.

Script kiểm khóa máy chủ SSH của GitHub qua API HTTPS, tải đúng commit đã pin, kiểm checksum rồi mới cập nhật workspace. Repo thiếu quyền đọc hoặc nội dung không khớp sẽ làm bước kiểm tra thất bại. Hệ thống không âm thầm sử dụng bản nguồn cũ.

GitHub Pages Free xuất bản từ repo chính công khai. Các repo học phần có thể riêng tư vì chúng không tự chạy Pages. Nội dung đã xuất bản trên website vẫn công khai. Lịch sử từng được công khai ở repo chính không bị xóa bởi việc tách nguồn.

## 5. Thêm học phần

Tạo một repo riêng tư có module `src/content/courses/<id>/course.mjs`, các trang `docs/<id>/` và `studyhub-course.json`. Thêm mục tương ứng vào file khóa. Khai báo đường dẫn hẹp, tránh chồng lấn với học phần khác hoặc mã giao diện. Thêm khóa chỉ đọc của repo mới vào secret và cập nhật import của danh mục tại `src/content/catalog.mjs`.

Chạy đồng bộ cùng toàn bộ kiểm tra nguồn trước khi phát hành. Build toàn bộ vẫn chỉ chạy trên GitHub Actions. Không chạy `npm run ci:build` tại máy biên soạn.

## Tài liệu tham khảo

- [GitHub Pages và phạm vi gói Free](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages).
- [Deploy key và quyền chỉ đọc theo repo](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/managing-deploy-keys).
- [Khóa commit của repo phụ trong mô hình Git](https://git-scm.com/docs/gitsubmodules).
