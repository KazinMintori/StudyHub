# Rà soát hình bài tập chương 27

## Phạm vi và đối chiếu PDF

Đã đối chiếu các hình trong *University Physics with Modern Physics*, ấn bản 15, tại các trang in 908–917, tương ứng trang PDF 928–937 (chỉ số trang zero-based trong Python bằng số trang in cộng 19). Các trang 908–916 có 33 hình E/P/Q được dùng trong các bài tập chương 27. Trang 917 có hình không đánh số đi cùng đoạn MCAT về MRI. Tệp tạo ảnh đã xuất 34 crop duy nhất.

| Trang in | Hình nguồn | Tệp crop |
| --- | --- | --- |
| 908 | Q27.12 | `hinh-q27-12.png` |
| 909 | E27.13, E27.14 | `hinh-e27-13.png`, `hinh-e27-14.png` |
| 910 | E27.19, E27.22, E27.25, E27.29, E27.31 | `hinh-e27-19.png`, `hinh-e27-22.png`, `hinh-e27-25.png`, `hinh-e27-29.png`, `hinh-e27-31.png` |
| 911 | E27.33, E27.37–E27.41 | `hinh-e27-33.png`, `hinh-e27-37.png`, `hinh-e27-38.png`, `hinh-e27-39.png`, `hinh-e27-40.png`, `hinh-e27-41.png` |
| 912 | E27.43, E27.45 | `hinh-e27-43.png`, `hinh-e27-45.png` |
| 913 | P27.55, P27.56, P27.59, P27.63 | `hinh-p27-55.png`, `hinh-p27-56.png`, `hinh-p27-59.png`, `hinh-p27-63.png` |
| 914 | P27.64–P27.67, P27.69, P27.70 | `hinh-p27-64.png`, `hinh-p27-65.png`, `hinh-p27-66.png`, `hinh-p27-67.png`, `hinh-p27-69.png`, `hinh-p27-70.png` |
| 915 | P27.71–P27.73, P27.77 | `hinh-p27-71.png`, `hinh-p27-72.png`, `hinh-p27-73.png`, `hinh-p27-77.png` |
| 916 | P27.78, P27.81, P27.82 | `hinh-p27-78.png`, `hinh-p27-81.png`, `hinh-p27-82.png` |
| 917 | MRI proton-spin illustration | `mcat-spin.png` |

Các biến thể Guided Practice VP27.1.x, VP27.6.x và VP27.7.x dùng lại hình lý thuyết của chương, không tạo crop mới. Bài toán cầu nối về vòng dây không có hình riêng trên trang 908. Trong bản PDF không tìm thấy hình được đánh số 27.42, nên không có tệp bridge riêng.

## Kiểm tra vùng cắt

Cả 34 crop được render ở độ phân giải 2,5 lần và rà trực quan cạnh trang nguồn. Các vùng cắt đã được hiệu chỉnh để giữ trọn hình nhưng loại phần văn xuôi lọt vào mép. Lượt đối chiếu cuối bổ sung lề cho kích thước E27.13, nhãn nguồn và toàn mạch E27.31, mũi tên từ trường E27.45, nhãn trục $x$ của P27.64 và P27.81, cùng lề phải của đồ thị P27.78. Các chỉnh sửa trước đó giữ trọn vòng dây P27.65, nhãn tọa độ dưới của P27.71, hai đầu thanh ray của P27.63 và bỏ mẩu văn xuôi ở mép E27.25. Đáy quả nặng E27.33 đã được so trực tiếp với hình đầy đủ và không bị cắt.

- Mạch E27.31, E27.33, E27.43 và P27.56 giữ cả nguồn, điện trở, thanh, giá đỡ và công tắc.
- Hình E27.13, P27.64–P27.67, P27.71, Q27.12 và P27.81 giữ các trục tọa độ, điểm, chiều dòng/vận tốc và kích thước hình học.
- Hình P27.77 và P27.78 giữ đủ tên trục, đơn vị, vạch chia và dữ liệu vẽ.
- Hình P27.73 giữ trụ, trục cuộn, dòng điện, trường từ, dây cáp, vật treo và độ cao $h$.
- Hình Q27.12 giữ toàn bộ khối lập phương, các điểm $a$–$e$, véc-tơ vận tốc, trục $x,y,z$ và hướng từ trường.
- Hình MCAT giữ cả hai trạng thái spin của proton cùng mũi tên công chuyển trạng thái.

## Chú giải tiếng Anh trong hình

Các nhãn chữ tiếng Anh còn nằm bên trong hình được ghi một lần theo asset trong `docs/.vitepress/physics27-exercise-image-annotations.mjs`:

| Hình | Nhãn tiếng Anh | Chú giải tiếng Việt |
| --- | --- | --- |
| E27.29 | Magnetic field region | Vùng từ trường |
| E27.33 | Battery; Bar | Pin; Thanh dẫn |
| E27.37 | Hinge | Bản lề |
| E27.38 | Axis | Trục |
| P27.55 | Wire, mass M; B (vertical) | Dây dẫn, khối lượng M; B (thẳng đứng) |
| P27.81 | Wall | Tường |
| MCAT MRI | Proton; Work; M and B0 parallel: Low energy; M and B0 antiparallel: High energy | Proton; Công; Mômen từ M và B0 song song: Năng lượng thấp; Mômen từ M và B0 ngược chiều: Năng lượng cao |

Các caption tiếng Việt cho toàn bộ 34 asset được chuẩn hóa trong cùng module chú giải. Các ký hiệu toán học, tên điểm, số liệu và đơn vị được giữ nguyên. Không đưa caption tiếng Anh hoặc lời bài tập vào crop.
