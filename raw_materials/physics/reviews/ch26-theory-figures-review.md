# Rà soát hình Chương 26: Phần lý thuyết

## Phạm vi

Đối chiếu các hình được dẫn trong `00`–`08` với PDF nguồn `young-freedman-15.pdf`, sau đó tạo crop ở độ phân giải 2× và chú giải tiếng Việt cho chữ tiếng Anh nằm trong hình. Quy đổi trang dùng chỉ số trang PDF = số trang in + 20. Crop được xem qua contact sheet và đối chiếu trực tiếp với các trang nguồn khi khung hình hoặc nhãn có nguy cơ bị cắt.

Đã tạo 45 ảnh thuộc phạm vi này: hình mở đầu, Hình 26.1–26.26, hai hình ứng dụng điện cơ và máy tạo nhịp tim, năm hình tóm tắt theo tên đã thống nhất với root, cùng 11 hình câu hỏi thảo luận. Bộ này không gồm Hình 26.27 và các hình bài tập E/P do root phụ trách.

## Kiểm kê theo nguồn

| Nội dung trong raw | Trang in / PDF | Ảnh đã tạo |
|---|---:|---|
| Mở đầu | 844 / 864 | `mo-chuong.png` |
| Điện trở nối tiếp/song song | 845–849 / 865–869 | `hinh-26-01.png`–`hinh-26-05.png` |
| Quy tắc Kirchhoff | 849–853 / 869–873 | `hinh-26-06.png`–`hinh-26-12.png` |
| Dụng cụ đo điện | 854–858 / 874–878 | `hinh-26-13.png`–`hinh-26-19.png`, `ung-dung-dien-co.png` |
| Mạch RC | 859–861 / 879–881 | `hinh-26-20.png`–`hinh-26-23.png`, `ung-dung-may-tao-nhip-tim.png` |
| Phân phối điện | 863–865 / 883–885 | `hinh-26-24.png`–`hinh-26-26.png` |
| Tóm tắt | 867 / 887 | `tom-tat-noi-tiep-song-song.png`, `tom-tat-kirchhoff.png`, `tom-tat-dung-cu-do.png`, `tom-tat-mach-rc.png`, `tom-tat-phan-phoi-dien.png` |
| Câu hỏi thảo luận 4–10, 12, 14, 16, 18 | 869–870 / 889–890 | `hinh-q26-04.png`, `05`, `06`, `07`, `08`, `09`, `10`, `12`, `14`, `16`, `18` |

Các trang 862 và 866 không bổ sung ảnh thuộc danh sách raw hiện tại. Hình Q26.6 được định vị lại theo sơ đồ dòng điện ở cuối trang 889. Hình Q26.18 lấy đủ hai cấu hình tụ điện và nhãn `(a)`, `(b)`. Hình Q26.4, Q26.5 và Q26.14 được chỉnh khung để giữ đủ cực pin, mũi tên và bóng đèn mà không kèm đoạn văn bên cạnh.

## Crop và chú giải

Script `scripts/prepare-physics26-theory-assets.py` ghi các crop vào `docs/vat-ly-2/bai-giang/img/young-26/`. Bảng `docs/.vitepress/physics26-theory-image-annotations.mjs` có một mục cho từng crop trong phạm vi. Các nhãn và câu tiếng Anh trong sơ đồ mạch, quy ước dấu Kirchhoff, dụng cụ đo, đồ thị RC, hệ thống dây điện gia đình và hình tóm tắt đã được chú giải. Ảnh chụp không chứa chữ cần dịch được để mảng rỗng. Chú thích hình đặt ngoài ảnh không lặp lại trong bảng này.

Sau khi nhận phản hồi về các mép ảnh bị cắt, đã mở từng PNG trong phạm vi ở kích thước gốc và đối chiếu với ảnh trang PDF QA cho mọi trang có hình thuộc danh sách. Đã chỉnh lại 14 khung: Hình 26.1, 26.4, 26.19–26.21, cả năm hình tóm tắt, cùng Q26.8–Q26.10 và Q26.14. Các thay đổi khôi phục nhãn `(a)` và ký hiệu điện trở trên Hình 26.1, mạch song song đầy đủ ở Hình 26.4, nhãn suất điện động trên Hình 26.19, chú giải màu xanh ở Hình 26.20–26.21, toàn bộ năm sơ đồ tóm tắt và nhãn bóng đèn `B₁`, `B₂` của Q26.14. Các ảnh Q26.8–Q26.10 đã bỏ phần văn xuôi ngoài sơ đồ.

Đã bổ sung bản dịch cho tiêu đề các panel xuất hiện trong crop Hình 26.1, 26.4, 26.20 và 26.21. Ảnh gốc được dựng lại bằng script sau mỗi lần chỉnh khung. Năm hình tóm tắt giữ nguyên tên root cần để chèn vào `raw06`.

## Giới hạn

Đã dựng lại đủ 45 crop bằng `python scripts/prepare-physics26-theory-assets.py`. Chưa kiểm tra cách registry chung tải bảng chú giải mới, chưa xác nhận render trang bài giảng sau tích hợp. Hình 26.27 và ảnh E/P không nằm trong phạm vi công việc này.
