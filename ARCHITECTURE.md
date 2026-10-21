# Kiến trúc StudyHub

StudyHub dùng VitePress để xuất bản nội dung và Vue để cung cấp các chức năng học tập. Đường dẫn công khai của bài giảng vẫn nằm trong `docs/`. Mã giao diện, quy tắc xử lý và dữ liệu môn học được tổ chức riêng trong `src/`.

```text
src/
  app/                       # Ghép giao diện và stylesheet toàn trang
  config/                    # Ngưỡng responsive và cấu hình tương tác
  core/
    storage/                 # Đọc, ghi và phản hồi lỗi lưu trữ trình duyệt
    routing/                 # Đường dẫn có base path và đuôi .html
    math/                    # Hiển thị toán và nhận diện dấu phân cách TeX
    diagrams/                # Mermaid và hộp xem hình
    styles/                  # Font và quy tắc nền
  features/
    navigation/              # Sidebar, tab và đồng bộ hash
    study-progress/          # Học tiếp, vị trí đọc và chuyển đổi tiến độ cũ
    study-tools/             # Flashcard, ghi chú và hẹn giờ
    course/                  # Tổng quan học phần
    lecture/                 # Notes, slides, bài tập và kiến thức nền
    wiki/                    # Danh mục thuật ngữ và ghi chú nhanh
    labs/                    # Mô phỏng cùng thuật toán của từng mô hình
    illustrations/           # Minh họa bài học và sơ đồ dữ liệu
    site/                    # Giới thiệu website và đóng góp
    legacy/                  # Chuyển hướng tương thích với liên kết cũ
  content/
    catalog.mjs              # Ghép danh mục môn học
    courses/<course-id>/
      course.mjs             # Thông tin môn và thứ tự bài
      lectures/<lecture-slug>/
        lesson.mjs           # Tiêu đề, trạng thái, tiên quyết và nhóm chủ đề
        slides.mjs           # Slides thuộc riêng bài này
        content.json         # Chỉ mục nguồn Notes, ví dụ, bài tập và lời giải

config/                      # Cấu hình build và chính sách giữ sản phẩm sinh
scripts/content/             # Đồng bộ chỉ mục nội dung
scripts/maintenance/         # Đo dung lượng và dọn sản phẩm sinh có giới hạn
docs/<course-id>/bai-giang/   # Nguồn trang công khai, giữ nguyên URL
raw_materials/               # Nguồn biên soạn, có thể được Markdown include trực tiếp
```

## Ranh giới trách nhiệm

- `components/`: Dựng giao diện, nhận dữ liệu và chuyển sự kiện đến controller. Điều kiện hiển thị như `v-if` vẫn nằm ở đây.
- `controllers/`: Các composable điều phối trạng thái Vue, vòng đời, sự kiện và lời gọi service. Controller được phép kiểm tra điều kiện của sự kiện hoặc vòng đời.
- `services/`: Quy tắc chọn bài học tiếp, chuyển đổi dữ liệu, tính thời gian, phân loại tab và thuật toán mô phỏng. Quy tắc có thể kiểm thử độc lập được đặt ở đây.
- `core/`: Các khả năng dùng chung giữa nhiều chức năng. Core không phụ thuộc một feature cụ thể.
- `config/`: Giá trị cấu hình có tên rõ ràng. Không giấu trạng thái người dùng hoặc quy tắc nghiệp vụ trong cấu hình.
- `content/`: Dữ liệu học thuật và chỉ mục nguồn. Không phụ thuộc Vue, DOM hay controller.

Luồng thông thường là `Component → Controller → Service`. Controller sử dụng các khả năng dùng chung qua core. Service đọc dữ liệu nội dung khi cần, nhưng không gọi ngược component hoặc controller.

Không tạo thêm một tầng chỉ để đổi tên một hàm. Component trình bày đơn giản không bắt buộc có controller riêng. Thuật toán mô phỏng thuần tính toán nằm trong service, còn kéo thả và theo dõi vùng nhìn thuộc controller.

## Tìm đúng nơi cần sửa

| Công việc | Nơi bắt đầu |
| --- | --- |
| Đổi cách chọn bài học tiếp | `src/features/study-progress/services/` |
| Sửa việc ghi nhớ vị trí đọc | `src/features/study-progress/controllers/` |
| Sửa nút ba gạch và chuyển kích thước màn hình | `src/features/navigation/controllers/` |
| Sửa tab và địa chỉ có dấu `#` | `src/features/navigation/services/` |
| Sửa lưu ghi chú, flashcard hoặc Pomodoro | `src/features/study-tools/` |
| Sửa hộp Wiki che nội dung | `src/features/wiki/services/popover-position.mjs` |
| Sửa màu sáng và tối | `docs/.vitepress/theme/tokens.css` và các stylesheet trong `src/app/styles/` |
| Sửa nút đổi giao diện sáng và tối | VitePress DefaultTheme, cấu hình `appearance` trong `docs/.vitepress/config.mjs` |
| Thêm Lab hoặc sửa thuật toán của Lab | `src/features/labs/components/` và `services/` |
| Sửa thông tin, tiên quyết hoặc slides của một bài | `src/content/courses/<course-id>/lectures/<slug>/` |
| Sửa lời giảng hoặc bài tập đã xuất bản | Tệp `notes`, `topics`, `fragments`, `examples`, `exercises`, `solutions` được ghi trong `content.json` của bài |

## Nội dung và quyền sở hữu nguồn

Mỗi bài có một thư mục dữ liệu riêng. `content.json` ghi đường dẫn và dòng bắt đầu của từng ví dụ, bài tập, lời giải, cùng nguồn của hình ảnh được sử dụng. Chỉ mục được sinh bằng `npm run content:index` và tự cập nhật khi chạy đồng bộ hoặc build. Không sửa chỉ mục thay cho nguồn.

Lời giảng có thể nằm ngay trong Markdown công khai hoặc được include từ `raw_materials/`. Không sao chép đoạn văn sang nhiều nơi để tạo cảm giác phân tầng. Một đoạn có một nguồn chính, còn chỉ mục cho biết nơi sử dụng và vai trò của nó.

Hai môn Vật lý đang được biên soạn trong chat khác. Adapter `src/content/courses/vat-ly-*/course.mjs` tiếp tục đọc các module Vật lý hiện có trong `docs/.vitepress/`. Chỉ mục vẫn chia riêng từng bài. Không di chuyển các nguồn này khi phiên biên soạn còn hoạt động.

Một số module trong `docs/.vitepress/` là điểm truy cập tương thích cho script và công cụ biên soạn. Khi sửa dữ liệu bảy môn đã chuyển, sửa module trong `src/content/courses/`, tránh thay nội dung của tệp re-export bằng một bản dữ liệu thứ hai.

`ProbabilitySourceReader.vue` cũ không được import, đăng ký hay dùng trong trang công khai, nên đã loại bỏ cùng controller của nó. Bộ 59 tài liệu thống kê tĩnh và dữ liệu thư viện vẫn được giữ, cùng kiểm tra độ phủ và nguồn dẫn.

## Tải dữ liệu theo nhu cầu

Mỗi lần chuyển trang là một lần tải lại tài liệu (xem `src/app/theme.mjs`), nên chunk `theme` được tải ở mọi trang. Chunk này chỉ chứa mã giao diện và danh mục môn học rút gọn, khoảng 280 kB thay vì hơn 25 MB trước đây.

- `scripts/build/lite-catalog-plugin.mjs`: Trong bản build phía trình duyệt, `src/content/catalog.mjs` được thay bằng bản JSON giữ các trường điều hướng và bỏ `slides`. SSR, script Node và máy chủ dev vẫn dùng module gốc.
- `src/features/lecture/services/lecture-payload.mjs`: Slides, Cheatsheet, Lab và Kiến thức nền chỉ tải khi người đọc mở tab tương ứng. Mỗi môn là một chunk riêng. Tab bắt đầu tải khi con trỏ chạm vào thanh tab.
- `src/features/lecture/services/cheatsheet-loaders.mjs`: Bản lazy của bảng cheatsheet trong `cheatsheet-service.mjs`. Khi thêm cheatsheet mới, thêm vào cả hai nơi; `scripts/tests/bundle-splitting.test.mjs` kiểm tra hai bảng khớp nhau.
- `src/features/wiki/services/concept-loader.mjs`: Từ điển khái niệm tải khi người đọc rê chuột, chạm vào thuật ngữ, hoặc khi trình duyệt rảnh trên thiết bị có chuột. Component Wiki được đăng ký bất đồng bộ.
- `scripts/math-text-plugin.mjs`: Công thức dựng sẵn được gắn vào từng `export const`, nên export nào không được dùng sẽ bị loại cùng SVG của nó. Các export `*WikiDetails` chỉ dùng khi sinh trang Wiki, nên bản trình duyệt không mang SVG của chúng.
- `docs/.vitepress/config.mjs`: Tắt prefetch chunk JavaScript của VitePress (site không dùng chuyển trang SPA), thêm Speculation Rules để trình duyệt tải trước trang khi con trỏ dừng trên liên kết, và bỏ preload Mermaid ở trang không có sơ đồ.

Không import tĩnh `concepts.mjs`, `wiki-content.mjs`, `cheatsheet-service.mjs` hay module dữ liệu Vật lý từ layout, header hoặc controller dùng chung.

## Build và giữ QA

`npm run build`, `npm run docs:build` và GitHub Pages đều dùng một đầu ra là `docs/.vitepress/dist/`. `npm run export:static` chỉ dùng khi cần thêm bản `dist/` để chuyển giao. Không xuất HTML vào thư mục gốc repo.

`scripts/build/build-site.mjs` giữ khóa trong thời gian đồng bộ và build. Một checkout chỉ có một build chạy qua lệnh này tại một thời điểm, tránh hai phiên cùng ghi `.temp` hoặc `dist`. Khóa chỉ được tự dọn khi tiến trình sở hữu đã kết thúc hoặc build hiện tại hoàn tất.

Bản export có dấu nhận diện sản phẩm sinh. Lần export tiếp theo chỉ thay thế thư mục mang đúng dấu nhận diện, không cộng dồn các chunk cũ. Máy chủ dev bỏ qua thay đổi trong thư mục đầu ra để tránh tải lại giao diện khi một phiên khác build.

QA đang dùng cho Chương 30, `full-source`, báo cáo, script kiểm tra, snapshot chưa tích hợp và worktree của chat Vật lý được giữ. `release29-certified` là bản đối chiếu trước refactor. Không xem một tệp là thừa chỉ vì không xuất hiện trong menu.

Không giữ nhiều bản website giống nhau mang tên `final`, `checked`, `verified`, `publish`. Giữ báo cáo nhỏ kèm mã commit, một bản đối chiếu cần thiết và đầu ra đang kiểm tra. Xóa các bản website trung gian sau khi kiểm tra kết thúc.

```sh
npm run audit:storage
npm run clean:generated             # Chỉ liệt kê, chưa xóa
npm run clean:generated -- --apply  # Dừng build cục bộ trước khi dùng
```

Lệnh dọn có danh sách thư mục cố định, từ chối junction và không đụng vào QA Vật lý hay nguồn biên soạn. Nhật ký dọn lần đầu nằm trong `output/project-audit-2026-10-14/`.

## Quy tắc tương thích

Giữ nguyên URL, anchor, tên component dùng trong Markdown, class CSS và các khóa lưu trữ `studyhub_*`. Không xóa trang chuyển hướng chỉ vì trang đó không có trên menu. Không tạo bộ chuyển giao diện sáng tối riêng khi DefaultTheme đang quản lý chức năng ấy.

Khi chuyển component, cập nhật alias Mermaid, đăng ký Lab, script kiểm chứng và công cụ `check_lecture.mjs`. Kiểm tra cả trang đã build và luồng tương tác trên desktop, điện thoại.

GitHub Actions kiểm tra chỉ mục nội dung, chiều phụ thuộc, tên export, mô hình Wiki, các quy tắc chức năng và hiển thị toán trước khi build. Những lệnh kiểm giao diện cũ như `verify-ui`, `verify-redesign`, `verify-static`, `verify-courses` đi qua bộ kiểm tra hiện tại, không giữ các giả định của giao diện năm môn trước đây.
