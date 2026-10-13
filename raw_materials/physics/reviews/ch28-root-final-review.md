# Chốt đối chiếu và hiển thị chương 28

Các báo cáo theo phạm vi được giữ như hồ sơ của từng lượt đọc. Bản tích hợp cuối đã xử lý thêm những điểm sau:

- Bài 28.13 dùng khoảng cách từ mỗi đoạn dòng đến điểm P bằng $3/\sqrt2$ cm. Hai trường cùng hướng vào mặt hình, tổng bằng $17{,}6\,\mu\mathrm T$. Đã sửa cả lời giải và phép tính Python, dùng tọa độ và tích có hướng thay cho đọc khoảng cách theo trực giác.
- Bài 28.47(b) có sơ đồ vòng dây, lõi sắt và ba đại lượng cùng trục. Bộ hình lời giải cuối gồm bốn SVG, thay cho ba SVG ở thời điểm các báo cáo hình ban đầu được viết.
- Bảng đáp số 28.59 đã sửa hướng tại Q thành hướng lên, cùng kết quả của lời giải vector. Đáp án phụ lục không được dùng để thay đổi hình học của đề.
- Giữ đủ 32 công thức đánh số và 12 ví dụ. Công thức 28.9 được nhắc lại trong một đoạn suy diễn nên số lần xuất hiện nhãn không bằng số công thức duy nhất.
- Các bảng tóm tắt nhiều cột, bảng độ cảm từ và lời giải bài 28.38 được chuyển thành các nhóm ngắn. Nội dung, dữ liệu và ảnh bảng được giữ đầy đủ. Các công thức dài được ngắt tại dấu quan hệ hoặc phép toán.

Chín bộ tính toán chạy qua. Kiểm tra toàn site trên bản xuất bản có 110 bài và 99 chủ đề, không có lỗi hoặc cảnh báo cấu trúc. Có 39 kiểm thử skill đạt. `npm run ci:build` kết thúc với exit 0, bản cuối tại `qa/physics/release28-checked`, thời gian build 171,34 s.

Kiểm tra trình duyệt toàn bộ tám chương Vật lý 2 đã hoàn thiện có 624 lượt ở 320, 360, 375 và 1440 px. Chương 28 chiếm 96 lượt. Có 243 lượt kiểm tra Wiki và 67 lượt đổi kích thước trực tiếp. Không ghi nhận tràn công thức, ảnh hỏng hoặc lỗi JavaScript. Ảnh chụp màn hình Cheatsheet và Bài tập trên điện thoại đã được xem lại.

Kết quả này áp dụng cho bản chương 28 và tám chương Vật lý 2 đã khép nội dung. Các chương 29–44 cùng phần còn lại của Vật lý 1 vẫn được ghi là chưa hoàn tất trong sổ rà 44 bài. Không lấy kết quả build để chứng nhận những chương chưa biên soạn.
