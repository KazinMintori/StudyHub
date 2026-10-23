# Rà lý thuyết chương 6

Ngày cập nhật: 24/10/2026. Phạm vi nguồn: Trang in 171–190, trang PDF 191–210 của Young & Freedman, ấn bản 15.

## Kết quả và phạm vi

Lý thuyết gồm lời mở, bốn mục 6.1–6.4, mười ví dụ, bốn câu tự kiểm và tổng kết. Có 37 hình trích trực tiếp từ PDF, gồm hình mở đầu, Hình 6.1–6.28, ba hình ứng dụng và năm sơ đồ tổng kết. Hình 6.29 ở trang PDF 212 thuộc bài tập cầu nối, không thuộc phần lý thuyết này.

Chương vẫn giữ trạng thái `draft`. Bài tập cuối chương chưa hoàn chỉnh nên không được nghiệm thu chung với phần lý thuyết.

## Những lỗi đã sửa khi đối chiếu độc lập

- Hình mở đầu là người ném bóng chày, không phải cung thủ. Đã sửa chú thích, khôi phục câu hỏi về ba quả bóng và tính lại động năng tương ứng.
- Đã sửa khung cắt để giữ đầy đủ các bảng, đồ thị và nhãn. Các trường hợp đáng chú ý gồm Hình 6.3, 6.8, 6.10, 6.14, 6.16, 6.19, 6.20, 6.25, ảnh gân và sơ đồ tổng kết.
- Đã thay chú thích chỉ dựa trên suy đoán bằng 82 nhãn tiếng Anh thực sự xuất hiện trong ảnh. Chín ảnh không có chữ được để trống danh sách thuật ngữ, giữ chú thích tiếng Việt bên ngoài.
- Đã khôi phục đủ số hiệu công thức 6.1–6.19. Đã bổ sung điều kiện hệ quán tính, các trường hợp công bằng không, số liệu tiết diện sợi cơ, giới hạn mô hình lò xo và cách tính công suất leo cầu thang thứ hai.
- Đã phân biệt tổng công lên đầu búa với công của riêng đầu búa lên dầm trong Ví dụ 6.4. Đã sửa trình kiểm tra câu tự kiểm 6.4 để kiểm công suất lực cản của bốn động cơ, thay vì kiểm một câu hỏi khác.
- Cheatsheet gồm 28 dòng công thức, chỉ có định nghĩa, tính chất, công thức, đơn vị và điều kiện áp dụng. Dữ liệu được biên dịch thành SVG toán thực sự.

## Kiểm tra đã chạy

- `C:/Users/Ai/miniconda3/python.exe -I -X utf8 raw_materials/physics/verify_chapter06_remaining_theory.py`: Đạt. Bao gồm số liệu ban đầu của mười ví dụ, các câu tự kiểm, đổi đơn vị và tích phân độc lập cho ví dụ xích đu.
- `measure-physics-math.mjs`: 135 công thức hiển thị, 577 công thức nội dòng, không có lỗi chiều rộng hoặc cú pháp ở ngưỡng 28ex/27ex.
- So sánh điểm ảnh của 37 hình với đúng trang và hình chữ nhật PDF: Đạt. Đã xem trực quan cả ảnh ghép và trang nguồn, không chỉ dựa vào phép so sánh điểm ảnh.
- Kiểm tra trình duyệt 18 trường hợp cho bốn mục, trang chương và cheatsheet tại các chiều rộng 320, 375 và 1440 pixel: Đạt. Không có lỗi toán, ảnh hỏng, công thức tràn trang hoặc nhãn còn ký tự TeX chưa biên dịch.
- `check_lecture.mjs vat-ly-1/06-cong-dong-nang`: Một bài và bốn chủ đề, không có lỗi hoặc cảnh báo cấu trúc.
- Bộ kiểm tra bundle và bộ nạp cheatsheet: Tám kiểm tra đạt, bao gồm kiểm tra mọi công thức và chú giải biến của chương 6 đều có SVG toán.

Build và deploy toàn bộ chỉ thực hiện trên GitHub Actions. Báo cáo này không chứng nhận phần bài tập chưa hoàn chỉnh hoặc các chương khác.
