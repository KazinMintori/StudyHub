# Thêm và cập nhật nội dung môn học

Mỗi môn có nhiều bài giảng; **mỗi bài** gồm Slides, Notes và Kiến thức nền. Ghi chú cá nhân trong Góc học tập là công cụ riêng của người học.

## Notes: nơi viết nội dung chi tiết

Tạo bài trong `docs/<môn>/bai-giang/<bài>.md`. Mỗi bài nên có mục tiêu học, giải thích, ví dụ, câu hỏi tự kiểm tra và nguồn tài liệu. Tiêu đề chung cùng ba phần được giao diện tạo từ catalog.

```yaml
---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
section: lecture
prerequisites: [vector, dao-ham, gradient]
lessonStatus: ready
---
```

Khai báo bài với cùng slug trong `course-catalog.mjs`. Danh sách `prerequisites` của bài trong catalog quyết định những khái niệm nào xuất hiện ở phần Kiến thức nền. Dùng ID từ `concepts.mjs`; tránh gắn toàn bộ nền tảng của môn cho mọi bài.

Các thuật ngữ đã khai báo được liên kết tự động trong phần văn bản của Notes. Code, công thức, tiêu đề và liên kết đã viết sẵn được giữ nguyên. Khi cần liên kết rõ ràng ở một vị trí khác, dùng Markdown:

```md
[Gradient](/wiki/gradient.md)
```

## Minh họa chạy bằng code

Nhúng component đã đăng ký trực tiếp trong Markdown:

```html
<CodeIllustration type="gradient" />
```

Các loại hiện có: `search` (BFS/DFS), `gradient`, `bayes`, `broadcast`, `mapreduce`, `field`. Mỗi loại cho phép thay đầu vào hoặc chạy từng bước. Giải thích giả định và giới hạn của mô hình ngay cạnh minh họa. Có thể tạo thêm component Vue cho nội dung mới rồi đăng ký trong theme.

## Slides: lấy trọng tâm từ Notes

Khai báo Slides trong `course-catalog.mjs`. Thuộc tính `note` là slug bài giảng sở hữu slide. Giao diện chỉ lấy những Slides của bài đang mở; mỗi slide có tiêu đề, vài ý chính và công thức nếu cần. Bài chưa soạn được ghi rõ trạng thái.

## Kiến thức nền: giúp người đọc tự bù nền

Mỗi khái niệm trong `concepts.mjs` gồm:

- Tên và cách gọi tương đương.
- Giải thích ký hiệu, định nghĩa và điều kiện áp dụng.
- Ví dụ đủ để kiểm tra cách hiểu.
- Lý do cần dùng trong môn.
- Câu hỏi tự kiểm tra cùng đáp án.

Sắp xếp `prerequisites` của bài theo thứ tự cần đọc. Với bài mới, rà lại những khái niệm chưa được giải thích trong Notes và đưa chúng vào nền tảng phù hợp.

## Wiki độc lập và liên kết thuật ngữ

Mỗi thuật ngữ có file Markdown riêng tại `docs/wiki/<id>.md`, khai báo `wikiTerm: <id>`. Viết giải thích kỹ thuật, điều kiện áp dụng, ví dụ và lỗi dễ nhầm. Liên kết sang thuật ngữ khác bằng Markdown hoặc dùng tên đã có trong `concepts.mjs` để tạo liên kết tự động. Không tự liên kết thuật ngữ của trang về chính trang đó.

Nội dung khởi tạo và quan hệ giữa thuật ngữ nằm ở `wiki-content.mjs`. Chỉnh bài Wiki trực tiếp sau khi tạo; build không ghi đè bài đã có. Danh sách “Bài giảng cần khái niệm này” lấy từ `prerequisites` trong catalog.

## Đồng bộ và kiểm tra

```sh
npm run sync:courses
npm run dev
npm run build
```

Danh sách bài giảng, Slides của từng bài và sidebar lấy cấu trúc từ catalog. Script đồng bộ không ghi đè bài giảng hoặc Wiki đã có. Kiểm tra đổi phần vẫn ở cùng bài, liên kết Wiki, bố cục điện thoại và kết quả minh họa trước khi xuất bản.

Tài liệu gốc có thể lưu trong `raw_materials/` cùng nguồn và thông tin học phần. Giữ đường dẫn cũ khi đổi vị trí bài để người học tiếp tục dùng liên kết đã lưu.
