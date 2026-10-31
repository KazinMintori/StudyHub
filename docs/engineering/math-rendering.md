---
title: Quy chuẩn hiển thị công thức
description: Cách viết, kiểm tra và ngăn lỗi công thức trên toàn bộ StudyHub.
---

# Quy chuẩn hiển thị công thức

## Phạm vi

Quy chuẩn áp dụng cho Notes, Wiki, Slides, Cheatsheet, ghi chú nhanh, bài tập và mô phỏng. File được chèn bằng `@include` cũng là nội dung hiển thị, kể cả khi nằm trong `raw_materials/`.

## Delimiter và thụt lề

Công thức trong câu dùng một cặp `$`. Công thức riêng dòng dùng một cặp `$$`, mỗi delimiter nằm trên một dòng riêng. Không để khối toán rỗng, thiếu delimiter hoặc chứa tiêu đề, container hay đoạn văn.

Khi công thức nằm trong danh sách, delimiter mở, toàn bộ thân công thức và delimiter đóng phải có cùng mức thụt lề của nội dung mục đó. Với danh sách đánh số, tính cả độ rộng của số và dấu chấm. Ví dụ đúng:

```markdown
1. Xét trạng thái ban đầu:

   $$
   x = 0
   $$

   Đây là phần giải thích nằm ngoài công thức.
```

Không thụt lề riêng delimiter mở rồi đưa thân công thức và delimiter đóng về cột đầu. Markdown có thể hiểu chúng thuộc hai phạm vi khác nhau và nhận cả phần văn phía sau thành toán, dù số lượng dấu `$$` vẫn chẵn.

## Hiển thị trên điện thoại

- Công thức inline không vượt quá 38ex. Kiểm tra độ rộng thực tế trong danh sách, hộp gợi ý, lời giải và ghi chú nhanh.
- Đo theo lòng khung thực tế sau khi trừ padding, viền và thụt lề, không chỉ theo bề rộng màn hình. Công thức vừa trang vẫn có thể tràn khỏi blockquote hoặc hộp định nghĩa. Với biểu thức tập hợp dài, giữ công thức ngắn và giải thích miền, chỉ số, điều kiện ngay bên ngoài.
- Chuỗi biến đổi dài dùng `aligned`, ngắt tại dấu quan hệ và căn thẳng dấu quan hệ. Công thức ngắn giữ một dòng.
- Hệ phương trình có vế trái chênh lệch lớn căn từ đầu dòng để tránh thụt lề quá sâu.
- Viết đoạn giải thích ngoài TeX. Không đưa văn xuôi dài vào `\text{...}`.
- Không dùng cắt nội dung, thanh cuộn hoặc thu nhỏ chữ đến mức khó đọc để che lỗi công thức dài.
- MathML phụ trợ phải được ẩn khỏi bố cục thị giác. Công thức không tạo thanh cuộn hoặc mũi tên cuộn trên Windows và điện thoại.

## Bộ hiển thị và bước chặn lỗi

Ký tự tiếng Việt trong công thức phải có đủ nét chữ và kích thước chuẩn. Bộ SVG dùng chung bổ sung những ký tự còn thiếu trong font TeX, để dấu không bị tách và chữ không bị giãn sai. Notes, dữ liệu Slides/Cheatsheet và bài thi đều dùng cùng bộ ký tự này. Không sửa lỗi font bằng cách bỏ dấu tiếng Việt hoặc đổi kích thước công thức.

Notes được phân tích bằng cấu hình Markdown của VitePress. `staticMathPlugin` giữ SVG trong một binding HTML và từ chối công thức rỗng, công thức nuốt Markdown hoặc kết quả MathJax có lỗi. Kiểm tra này áp dụng cả đầu ra Vue và HTML bài tập.

Slides, Cheatsheet, ghi chú nhanh và lời giải trong bài thực hành dùng `mathTextPlugin` để biên dịch công thức từ module dữ liệu. Module riêng theo môn, kể cả module được tải khi mở Cheatsheet và module trong `docs/.vitepress/labs/`, phải được plugin nhận diện và đăng ký công thức đã biên dịch.

Kiểm tra phải mở toàn bộ include trước khi phân tích và giữ nguyên mọi ký tự TeX trong nguồn. Khi thay chuỗi trong JavaScript, dùng hàm trả về nội dung thay thế để các ký hiệu `$$` và `$&` không bị hiểu thành cú pháp thay chuỗi. Chỉ đọc file Notes chứa lệnh include sẽ bỏ sót nội dung người học thực sự nhận được. Không dùng riêng việc đếm delimiter hoặc kiểm tra lỗi JavaScript để kết luận công thức đúng.

## Kiểm tra trước khi push

Từ thư mục gốc:

```sh
npm run verify:math
node .agents/skills/studyhub-lecture/scripts/check_lecture.mjs --all
python -I .agents/skills/studyhub-lecture/scripts/tests/test_tools.py
```

`verify:math` phân tích toàn bộ Markdown công khai cùng các nguồn include, dựng công thức bằng MathJax và kiểm tra công thức trong dữ liệu Slides, Wiki, Cheatsheet. Bộ kiểm tra này cũng nằm trong `npm test` của GitHub Actions.

Để xem giao diện, chạy `npm run dev`, sau đó mở các trang đã sửa ở bề rộng 360px, 375px, 768px và màn hình máy tính. Mở cả lời giải đang gập và các tab liên quan. Xác nhận không lộ mã TeX, không có đoạn văn bị nhận thành toán, không có lỗi MathJax và không tràn ngang. Thử cuộn bằng cảm ứng theo cả hai chiều để kiểm tra thanh điều hướng.

Các kiểm tra trình duyệt có thể chạy khi máy chủ dev đã mở:

```sh
node scripts/verification/verify-math-mobile.mjs
node scripts/verification/verify-mobile-header.mjs
node scripts/verification/verify-mobile-lab-controls.mjs
```

Kết quả và ảnh lỗi được ghi trong `qa/`. Kiểm tra toán mở cả các lời giải đang gập và phân biệt công thức tràn trang với bảng có vùng cuộn riêng. Đây là các trường hợp hồi quy đại diện, không thay thế việc xem trang nội dung mới.

Build toàn bộ và deploy do GitHub Actions thực hiện sau khi push lên `main`. Không chạy `npm run ci:build`, `npm run build` hoặc `npm run docs:build` trên máy cục bộ.
