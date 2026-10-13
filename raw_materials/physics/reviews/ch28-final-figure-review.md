# Rà soát trực quan hình chương 28

Đã mở ở độ phân giải gốc toàn bộ 83 ảnh PNG trong `docs/vat-ly-2/bai-giang/img/young-28/` theo 14 ảnh lý thuyết A, 31 ảnh lý thuyết B và 38 ảnh cuối chương. Đối chiếu các trang nguồn 918–952 của PDF với các trang in render tương ứng, gồm các trang chứa hình tóm tắt và bài tập. Không tính ba sơ đồ SVG do root quản lý.

## Kết quả

- Phát hiện thêm một lỗi cắt ở mép phải của `hinh-p28-70.png`: Hai hàng dây dẫn chạm mép ảnh, trong khi bản gốc có khoảng trắng sau các ô cuối. Mở rộng crop phải từ 565 lên 580 điểm PDF trong `scripts/prepare-physics28-exercise-assets.py` và tạo lại PNG. Hình mới có đủ tám ô mỗi hàng và khoảng trắng hai bên.
- Kiểm tra riêng các hình P28.58, P28.61, P28.72, P28.76, P28.77, E28.28 và P28.66. Dữ liệu, mũi tên, trục và đầu dây còn nguyên. P28.66 kết thúc dây thẳng như bản PDF, phù hợp mô hình dây dài vô hạn.
- Kiểm tra nội dung tiếng Anh nằm trong hình: Ba module chú giải có 14, 31 và 38 khóa, khớp đủ ba nhóm ảnh. Nhãn tiếng Anh có nội dung được ghép với câu tiếng Việt; hình không có nhãn văn xuôi dùng mảng rỗng. Các biến, đơn vị và ký hiệu toán học được giữ nguyên.
- Không phát hiện lỗi cắt hoặc sai chiều vector khác trong lần xem toàn bộ ảnh ở độ phân giải gốc.

## Phạm vi đối chiếu PDF

Mỗi PNG trong nhóm được dựng từ PDF bằng các script crop đã lưu. Đã render và đối chiếu trang PDF ở kích thước lớn cho trang 28.1, các trang cuối chương có hình P28.58–P28.79, trang bảng tóm tắt và trang chứa crop được sửa. Contact sheet của 35 trang in 918–952 được xem để kiểm tra vị trí, ngữ cảnh và sự hiện diện của nguồn. Không chỉnh ba SVG hoặc module khóa học/Wiki.
