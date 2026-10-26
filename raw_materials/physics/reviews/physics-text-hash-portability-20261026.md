# Tính nhất quán dấu kiểm chứng trên Windows và GitHub

Khi chuẩn bị kiểm tra tài nguyên sau triển khai, đã phát hiện tám hình SVG lời giải chương 1 được ghi dấu SHA256 từ tệp Windows có xuống dòng CRLF. Git chuẩn hóa các tệp văn bản ấy sang LF. Hình vẽ và nội dung XML không đổi, nhưng dấu của bản làm việc không khớp dấu của Git blob.

Đã sửa chương trình sinh SVG để ghi rõ UTF-8 với LF. Danh mục tài nguyên được cập nhật theo dấu chuẩn này. Hai chương trình kiểm phần bài tập đã nghiệm thu chuẩn hóa riêng CRLF thành LF khi kiểm Markdown và SVG, nên dùng được trên cả bản sao Windows lẫn Linux. PNG và PDF vẫn được kiểm nguyên byte, không chuẩn hóa nội dung hoặc điểm ảnh.

Tám trường hợp hồi quy kiểm cả hai chương trình: LF và CRLF phải tương đương với văn bản, thay đổi dấu trong công thức vẫn phải bị phát hiện, còn mọi thay đổi byte trong PNG hoặc PDF vẫn phải làm dấu khác đi. Các chương trình kiểm lại 82 đơn vị chương 1 và 30 đơn vị chương 3 đều đạt sau sửa.

Một phép thử yêu cầu ảnh bằng đường dẫn nguồn trực tiếp đã được loại khỏi bằng chứng nghiệm thu triển khai. VitePress xử lý tài nguyên khi dựng trang, còn phần bài tập dùng ảnh được sao chép theo dấu nội dung. Các nhóm bài tập của chương 1 và 3 chưa được bật công khai, nên hiện chưa thể xác nhận việc tải ảnh của những nhóm ấy trên web. Khi chương được nghiệm thu trọn vẹn, phải kiểm chỉ mục, từng nhóm HTML và các URL ảnh thực tế được xuất bản.

Sửa chữa này chỉ liên quan đến dấu kiểm chứng và khả năng tái lập. Không thay đổi nội dung bài học, hình gốc hoặc trạng thái đang biên soạn của các chương còn thiếu.
