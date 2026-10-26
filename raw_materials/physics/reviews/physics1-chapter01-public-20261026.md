# Xác nhận bản công khai Chương 1

GitHub Actions đã dựng và triển khai thành công commit `e1ca8af7cdecf721d258ae49ecb3a33a871e6241` trong lượt chạy 40316518324. Việc kiểm tra sau triển khai dùng các địa chỉ thật của website và đối chiếu nội dung với đúng commit này.

Trang bài tập cung cấp đủ 129 đơn vị trong 24 nhóm. Mọi nhóm giữ đủ mã bài, khung lời giải đóng ban đầu và công thức đã biên dịch. Ba mươi mốt ảnh có tên băm trên máy chủ khớp byte với tệp tương ứng trong Git. Các dấu vân tay nguồn trong chỉ mục bài tập cũng khớp commit.

Đã thao tác giao diện công khai để chọn từng nhóm và mở các lời giải, sau đó kiểm tra ở 320, 360, 375, 768 và 1440 px. Cả 120 trường hợp đều đạt, không ghi nhận lỗi JavaScript, yêu cầu ảnh thất bại, công thức tràn mép hoặc thanh cuộn của công thức trong phạm vi được kiểm tra.

Mười một trang lý thuyết, gồm trang chương và mười chủ đề, đều trả nội dung thành công. Bốn mươi hai ảnh lý thuyết được nhận diện từ các URL có tên băm mà VitePress thực sự xuất ra, tải lại và đối chiếu byte với Git. Không suy đường dẫn công khai trực tiếp từ tên tệp nguồn.

Lần thử đầu dùng nhầm tiền tố tên ảnh của chương khác nên bộ dò không nhận diện được ảnh. Đây là lỗi của bộ kiểm tra đường dẫn, không phải ảnh bị mất trên website. Sau khi lấy danh mục ảnh từ chương trình trích ảnh Chương 1 và đọc URL trong HTML thật, toàn bộ 42 ảnh đã được xác nhận.

Xác nhận này áp dụng cho Chương 1. Việc hoàn thiện và rà soát toàn bộ hai học phần, báo cáo tổng kết cùng dọn dẹp dự án vẫn thuộc các công việc tiếp theo.
