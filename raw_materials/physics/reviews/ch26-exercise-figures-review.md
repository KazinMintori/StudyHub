# Rà soát hình bài tập Chương 26

Đã đối chiếu 50 hình bài tập với bản PDF *University Physics with Modern Physics*, 15th edition, tại các trang in 870–877. Chỉ số trang PDF dùng trong script bằng số trang in cộng 19. Mỗi crop đã được xem ở kích thước gốc cùng trang chứa hình để kiểm tra sơ đồ, nhãn, dấu cực, mũi tên, đơn vị và phần văn bản lân cận.

## Kiểm kê hình theo trang in

| Trang in | Hình trong crop | Số hình |
| --- | --- | ---: |
| 870 | E26.1, E26.2, E26.5, E26.6, E26.7, E26.11 | 6 |
| 871 | E26.13, E26.14, E26.15, E26.16, E26.17, E26.18, E26.19, E26.20, E26.22, E26.23 | 10 |
| 872 | E26.24, E26.25, E26.26, E26.29, E26.30, E26.31, E26.32 | 7 |
| 873 | E26.34, E26.41, E26.45, E26.47, E26.49 | 5 |
| 874 | P26.54, P26.56, P26.57, P26.58, P26.59, P26.60, P26.62, P26.63, P26.64 | 9 |
| 875 | P26.66, P26.67, P26.69, P26.70, P26.71, P26.73, P26.74, P26.75 | 8 |
| 876 | P26.78, P26.81, P26.82, P26.83, P26.84 | 5 |
| **Tổng** | **50 hình duy nhất** | **50** |

Trang 877 không có hình mới trong nhóm bài tập này. Bài 26.85 dẫn lại hình P26.83, nên bản dịch dùng lại crop đó. Các bài 26.86–26.88 không dẫn hình mạch riêng.

## Đối chiếu với bốn tệp bài tập

| Tệp nguồn | Lượt chèn hình | Mã hình duy nhất | Kết quả |
| --- | ---: | ---: | --- |
| `09-bai-tap-01-32.md` | 26 | 23 | Đủ crop cho mọi tham chiếu. E26.11 được dùng cho bài 26.11–26.12; E26.26 được dùng cho bài 26.26–26.28. |
| `10-bai-tap-33-60.md` | 11 | 11 | Đủ crop cho mọi tham chiếu. |
| `11-bai-tong-hop-61-80.md` | 12 | 12 | Đủ crop cho mọi tham chiếu. |
| `12-bai-nang-cao-mcat.md` | 5 | 4 | Đủ crop cho mọi tham chiếu. P26.83 được dùng lại ở bài 26.85 theo chỉ dẫn của bản in. |

Tổng cộng có 54 lượt chèn và 50 mã hình riêng. Tất cả 50 mã trong bốn tệp đều khớp với 50 mục của script tạo ảnh, 50 tệp PNG và 50 khóa chú giải. Không có tham chiếu thiếu tệp hoặc crop thừa ngoài các tham chiếu.

## Kết quả xem hình

Các crop giữ đủ cấu trúc mạch, nhãn linh kiện, đầu nối, cực nguồn, chiều dòng điện và đơn vị cần thiết để đọc bài. Đồ thị P26.78 giữ đủ nhãn trục và đơn vị thời gian. Mạng vô hạn P26.83 giữ các nút, nhánh lặp, ký hiệu tiếp tục và kích thước đoạn. Các crop không còn lấy phần lời bài tập hoặc tiêu đề hình đi kèm. Sau khi tạo ảnh, script cắt phần nền trắng thừa ở viền ngoài và chừa 5 pixel quanh nội dung để hình dễ đọc hơn trên màn hình nhỏ.

Đã chỉnh các vùng cắt bị thiếu dây hoặc nhãn ở E26.7, E26.16, E26.25, E26.26, E26.30, E26.32, P26.54, P26.62, P26.64 và P26.78. Đã kiểm lại riêng E26.26 để giữ đủ ba nhánh và E26.57 để giữ trọn thanh dẫn bên phải cùng mọi nhánh nguồn.

## Chú giải tiếng Anh trong hình

Các từ hoặc câu tiếng Anh còn nằm bên trong hình được chú giải trong `docs/.vitepress/physics26-exercise-image-annotations.mjs`:

| Hình | Nhãn trong ảnh | Chú giải tiếng Việt |
| --- | --- | --- |
| E26.19 | Water | Nước |
| E26.34 | Shunt | Điện trở shunt |
| E26.49 | Switch S in position 1; Switch S in position 2 | Công tắc S ở vị trí 1; Công tắc S ở vị trí 2 |
| P26.58 | Ice | Băng |
| P26.69 | Dielectric fill, constant K, resistivity ρ | Chất điện môi có hằng số điện môi K và điện trở suất ρ |
| P26.83 | and so on | Tiếp tục tương tự |

Các ký hiệu, biến, tên điểm và đơn vị là thành phần toán học hoặc vật lý của sơ đồ nên được giữ nguyên. Không còn câu văn tiếng Anh chưa chú giải trong các crop đã kiểm tra.
