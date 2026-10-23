# Nghiệm thu định dạng chủ đề Tập lồi và bao lồi

Antigravity làm trong worktree riêng tại bản 56d09dab. Cầu nối kết thúc với lỗi `expected string or bytes-like object, got 'NoneType'`. Chỉ có hai tệp được giao thay đổi, HEAD không đổi và diff không có lỗi khoảng trắng. Đây không được ghi nhận là một lượt thực thi Antigravity thành công.

Parent đọc toàn bộ diff và hiệu chỉnh trước khi tích hợp:

- Khôi phục đầy đủ các phép tính từng tọa độ của phân phối xác suất, dùng phân số tương đương để vừa màn hình hẹp.
- Khai báo rõ ký hiệu chuẩn Euclid viết gọn, giữ bước xét từng tọa độ trong chứng minh với chuẩn một.
- Giữ khai triển trường hợp hai điểm, các hệ số trung gian của quy nạp, trọng số tam giác và các bước giải hệ xác suất.
- Sửa chỗ ngắt trước dấu bằng, bỏ cách bẻ tập hợp ở dấu phẩy, dịch các nhãn tiếng Anh trong công thức sang tiếng Việt.
- Tách điều kiện độc lập và đưa dấu phân cách công thức về dòng riêng. Không thu nhỏ, che hoặc tạo vùng cuộn cho công thức.

Kiểm tra bản cuối:

- Đo 39 công thức hiển thị và 371 công thức nội dòng: Không còn phát hiện vượt ngưỡng 28 ex và 27 ex tương ứng.
- Kiểm tra bài và 25 trang chủ đề: Không lỗi, không cảnh báo.
- Python tính lại các ví dụ số gốc và 100 phép thử đẳng thức bậc hai: Đạt.
- Trình duyệt ở 320, 375 và 1440 px, mở toàn bộ chứng minh, lời giải và khung tra cứu: Không công thức tràn và chiều rộng trang bằng chiều rộng màn hình.

Đây là nghiệm thu định dạng và các phép tính được nêu. Không suy rộng thành tuyên bố đã kiểm chứng mọi định lý hoặc mọi bài trong toàn website.
