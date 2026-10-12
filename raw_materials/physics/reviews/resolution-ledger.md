# Kết quả xử lý lượt rà Luna

Phạm vi xuất bản của lượt này là ba chương 21–23 đã hoàn tất và bản thảo lý thuyết chương 24. Các chương còn lại chưa được chứng nhận đầy đủ. Báo cáo từng chương ghi phạm vi đối chiếu nguồn và giới hạn kiểm tra.

| Phát hiện | Xử lý |
| --- | --- |
| Cụm “cầu chì” ở đề 21.1 gây hiểu nhầm | Đổi thành “một quả cầu nhỏ bằng chì”. |
| Crop 21.9, 21.17, 21.20, 21.22, 21.30, P21.96 | Điều chỉnh khung lấy hình, giữ nhãn và bỏ chữ văn bản ngoài sơ đồ. Mở ảnh kiểm tra trực tiếp. |
| 21.91, 21.93, 21.97 thiếu bước đại số hoặc nguyên hàm | Thêm phép đổi biến, nguyên hàm, thế cận, chọn nghiệm và điều kiện. Python kiểm lại các bước tích phân và điểm quay đầu. |
| Q22.3 nêu cấu hình nguồn bất khả thi so với hình | Giải thích A,B,D nằm trong C, nên nguồn ngoài C ở ngoài cả bốn mặt và không đổi điện thông. |
| Crop 22.21, 22.25, 22.27, P22.56 | Bỏ chữ thừa, giữ nhãn đầy đủ và đơn vị hai trục đồ thị. Mở ảnh kiểm tra trực tiếp. |
| 22.24 thiếu chú giải các nhãn viết tay tiếng Anh | Thêm điện tích tổng, mặt Gauss, điện tích thành hốc và mặt ngoài. |
| Các đề dùng lại hình không đặt hình cạnh đề | Thêm hình vào 16 vị trí ngay sau đề, gồm 22.25 và 22.32. |
| 22.53, 22.54, 22.55 còn gọn ở bước nền | Thêm phép suy Gauss và khai triển phép trung bình các dữ liệu đã đổi biến. |
| Crop P23.65 cụt điện áp và Airflow | Mở rộng crop và xem lại đủ các nhãn. |
| 23.41(e) thiếu hướng trường ngoài | Ghi thành phần xuyên tâm có dấu, ba trường hợp q > Q, q < Q, q = Q. |
| Chú thích mới chỉ dịch thuật ngữ, bỏ câu chú giải trong ảnh | Ba Luna đọc ảnh và tạo bảng giải nghĩa đầy đủ theo chương. Bố trí danh sách Việt (English) dưới ảnh, không lặp cùng nhãn trên một ảnh. |
| Tab Slides có dữ liệu nhưng không hiển thị | Khôi phục thẻ ôn tập cho Vật lý 2, có nút và phím chuyển thẻ. Bộ kiểm tra duyệt từng thẻ. |
| Nhấn đậm dày ở các ý (a), (b) và lựa chọn | Bỏ nhấn đậm ở ký hiệu ý, giữ nhấn ở thuật ngữ và điều kiện quyết định. |

Hồ sơ Python bổ sung là `verify_reviewed_integral_steps.py`. Bộ kiểm tra ảnh, MathText, bố cục chuyển kích thước và browser được chạy riêng. Build thành công và kiểm tra tự động không thay thế các kết luận đối chiếu nguồn của reviewer.
