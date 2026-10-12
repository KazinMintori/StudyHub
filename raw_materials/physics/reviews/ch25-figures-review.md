# QA hình ảnh Chương 25

## Phạm vi và cách kiểm tra

Đã rà bộ crop Chương 25 bằng contact sheet và mở riêng các hình từng bị cắt chú giải hoặc nội dung đồ thị. Các vùng nghi vấn đã được đối chiếu trực tiếp với trang PDF gốc ở độ phân giải cao. Đã sửa crop trong `scripts/prepare-physics25-assets.py`, chạy lại script và kiểm tra các ảnh được sinh.

Theo yêu cầu bổ sung, đã crop năm sơ đồ bài tập E25.26–E25.30 từ trang in 839/PDF 859, cùng sáu hình P25.59, P25.62, P25.69–P25.72 từ trang in 841–842/PDF 861–862. Bộ sinh hiện tạo 51 ảnh: 40 hình chương/tóm tắt, năm hình bài tập E25 và sáu hình bài tập P25. Số trang trong script là trang in; chỉ số trang PyMuPDF bằng số trang in +19. Tọa độ clip bên dưới dùng điểm trang PDF, theo dạng `(x0, y0, x1, y1)`.

## Sổ crop và kết quả rà

| Ảnh | Trang in | Clip | Kết quả |
| --- | ---: | --- | --- |
| `mo-chuong` | 812 | (220, 0, 648, 245) | Ảnh mở chương giữ trọn chủ thể, không mang nhãn chữ trong crop. |
| `hinh-25-01` | 813 | (456, 315, 612, 580) | Bỏ phần caption chữ phía trên nhưng giữ hai vật dẫn, đường đi electron, các callout và câu giải thích lực. |
| `hinh-25-02` | 814 | (35, 112, 195, 410) | Giữ đủ hai panel hạt tải dương/âm và cả hai câu về dòng quy ước; không còn lẫn caption ở trên. |
| `hinh-25-03` | 814 | (35, 519, 195, 750) | Giữ mạch, tiết diện dòng và công thức $I=dQ/dt$; không còn câu caption ở trên, bóng đèn đã trọn. |
| `hinh-25-04` | 815 | (455, 590, 648, 741) | Ảnh bóng đèn và bình dung dịch trọn vẹn. |
| `hinh-25-05` | 817 | (455, 465, 615, 642) | Giữ ảnh mạch in và callout “Conducting paths (traces)”. |
| `hinh-25-06` | 818 | (35, 136, 195, 425) | Giữ cả ba đồ thị, đặc biệt panel siêu dẫn (c) và toàn bộ câu chú giải. |
| `anh-mang-myelin` | 818 | (0, 593, 192, 741) | Giữ ảnh vi thể và đủ nhãn Myelin/Axon. |
| `hinh-25-07` | 819 | (456, 356, 612, 476) | Đã mở rộng để có nhãn tiết diện A, E, J, I và câu “V = potential difference between ends”. |
| `hinh-25-08` | 820 | (0, 246, 192, 388) | Ảnh vòi cứu hỏa trọn vẹn, không lẫn phần văn bản ngoài ảnh. |
| `hinh-25-09` | 820 | (35, 470, 195, 537) | Đủ bốn callout mã màu: chữ số thứ nhất/hai, hệ số nhân và dung sai. |
| `hinh-25-10` | 821 | (95, 85, 420, 240) | Đã mở rộng phía dưới để giữ đủ đồ thị điôt và câu về dòng rất nhỏ theo chiều ngược. |
| `hinh-25-11` | 822 | (35, 238, 195, 502) | Đã thêm phần cuối panel (c), gồm trạng thái $I=J=E_{tot}=0$. |
| `hinh-25-12` | 822 | (0, 585, 192, 741) | Ảnh đài phun nước trọn vẹn. |
| `hinh-25-13` | 823 | (456, 244, 612, 430) | Bỏ caption bên ngoài; giữ sơ đồ nguồn hở và đủ câu chú giải dưới mạch. |
| `hinh-25-14` | 823 | (456, 534, 615, 750) | Bỏ caption ngoài hình; giữ mạch kín, dòng, lực và trọn callout về nguồn thực. |
| `hinh-25-15` | 824 | (35, 544, 195, 703) | Ảnh pin-bóng đèn trọn vẹn; caption ngoài ảnh được dịch ở Notes. |
| `anh-ca-duoi-dien` | 824 | (10, 247, 192, 349) | Ảnh cá đuối điện trọn vẹn, không có nhãn nội bộ. |
| `hinh-25-16` | 825 | (85, 561, 274, 633) | Mạch hở, vôn kế và ampe kế đủ. |
| `hinh-25-17` | 826 | (36, 76, 230, 180) | Đã mở rộng xuống dưới để giữ trọn tải R, nhánh ampe kế và nhãn đầu cực. |
| `hinh-25-18` | 826 | (312, 347, 567, 441) | Giữ đủ cả cách mắc meter (a) và (b). |
| `hinh-25-19` | 826 | (312, 642, 568, 760) | Đã mở rộng xuống dưới để giữ nhãn viết tay quanh mạch ngắn. |
| `hinh-25-20` | 827 | (456, 270, 612, 455) | Đã mở rộng đến trục đáy và O; giữ toàn đồ thị tăng/giảm điện thế. |
| `hinh-25-21` | 828 | (72, 120, 175, 178) | Crop riêng đồ họa phần tử mạch, các nhãn $V_a,V_b,a,b,I$ và dòng “Circuit element”; không lấy caption công thức phía trên. |
| `hinh-25-22` | 829 | (455, 168, 615, 530) | Đã mở rộng xuống để giữ trọn sơ đồ năng lượng và panel mạch pin/đèn pha ở dưới. |
| `hinh-25-23` | 829 | (455, 590, 615, 750) | Giữ đủ sơ đồ pin nhỏ và máy phát lớn cùng nhãn trong hình. |
| `hinh-25-24` | 830 | (312, 520, 572, 640) | Giữ sơ đồ và các nhãn viết tay $V_{ab}$, $V_{a'b'}$, $I^2r$, $\mathcal E I$, $R$. |
| `hinh-25-25` | 831 | (82, 622, 282, 756) | Giữ sơ đồ ngắn mạch và nhãn viết tay phía dưới. |
| `hinh-25-26` | 832 | (35, 317, 195, 555) | Đã mở rộng phía dưới để giữ “Net displacement”, cùng nhãn START/END của hai panel. |
| `hinh-25-27` | 832 | (35, 653, 195, 743) | Ẩn dụ quả bóng và chốt gỗ trọn vẹn. |
| `tom-tat-dong-dien` | 835 | (495, 98, 607, 160) | Hình trụ dòng điện, không có câu chữ tiếng Anh trong graphic. |
| `tom-tat-dien-tro-suat` | 835 | (492, 214, 602, 310) | Đã bỏ separator màu đỏ ở hàng trên, giữ trọn trục, độ dốc và câu về kim loại. |
| `tom-tat-dien-tro` | 835 | (493, 329, 602, 400) | Giữ nhãn điện thế cao/thấp và quan hệ $V$ với hai đầu dây. |
| `tom-tat-suat-dien-dong` | 835 | (494, 430, 609, 505) | Sơ đồ circuit, không có nhãn văn xuôi cần dịch. |
| `tom-tat-cong-suat` | 835 | (493, 527, 594, 580) | Giữ đủ callout công suất, điện áp, dòng điện và “Circuit element”. |
| `tom-tat-dan-dien` | 835 | (494, 623, 578, 662) | Giữ vector trường và nhãn “Net displacement”. |
| `hinh-q25-12` | 837 | (80, 659, 330, 749) | Đã mở rộng lên trên để giữ đủ panel (a)–(d), các nhãn I/V và gốc O. |
| `hinh-q25-14` | 837 | (386, 263, 578, 334) | Hai mạch và nhãn Bulb A/B trọn vẹn. |
| `hinh-q25-15` | 837 | (389, 458, 575, 535) | Đã mở rộng lên để có đủ đỉnh pin và hai panel; nhãn “Light bulb” chỉ chú giải một lần. |
| `hinh-q25-16` | 837 | (386, 625, 578, 710) | Đã mở rộng lên vừa đủ để giữ panel (a)/(b), pin, bóng đèn, ampe kế và vôn kế mà không kèm caption ngoài. |
| `hinh-e25-26` | 839 | (144, 360, 260, 422) | Crop sơ đồ đầy đủ, không gồm dòng đề/caption bên trái. |
| `hinh-e25-27` | 839 | (236, 453, 329, 516) | Crop trọn mạch có vôn kế lý tưởng nối tiếp. |
| `hinh-e25-28` | 839 | (160, 580, 273, 655) | Crop đủ nhánh ampe kế, pin với nội trở và tải 4 Ω. |
| `hinh-e25-29` | 839 | (242, 683, 326, 760) | Crop đủ vôn kế, pin, công tắc, R và ampe kế. |
| `hinh-e25-30` | 839 | (385, 140, 542, 220) | Crop trọn mạch hai pin, hai nội trở và các điểm a,b,c. |
| `hinh-p25-59` | 841 | (280, 375, 342, 449) | Crop đủ khối nón cụt và các ký hiệu $r_1$, $r_2$, $h$. |
| `hinh-p25-62` | 841 | (215, 646, 335, 720) | Giữ toàn mạch một vòng, các nút a–d, hai nguồn và điện trở trong. |
| `hinh-p25-69` | 841 | (468, 610, 615, 676) | Giữ hai bình trụ, ampe kế, nguồn và điện trở nối tiếp. |
| `hinh-p25-70` | 842 | (175, 164, 298, 206) | Giữ đầy đủ mạng R₁, R₂, C₁, C₂ và nguồn. |
| `hinh-p25-71` | 842 | (178, 274, 296, 316) | Giữ đầy đủ nhánh R₁, R₂, tụ điện và nguồn. |
| `hinh-p25-72` | 842 | (103, 441, 276, 532) | Giữ đồ thị, hai trục, các điểm dữ liệu và đường khớp. |

## Chú giải nhãn và giới hạn tích hợp

`docs/.vitepress/physics25-image-annotations.mjs` export `physics25ImageAnnotations` cho đủ 51 khóa `young-25/<stem>`. Các ảnh có chữ trong đồ họa có cặp Việt–Anh cho từng nhãn/callout, gồm cả câu nhiều dòng trong Hình 25.1, 25.2, 25.6, 25.10–25.14, 25.22, 25.26 và các đồ thị tóm tắt. Sáu hình P25 mới chỉ chứa ký hiệu/toán học nên dùng danh sách rỗng. Hình chụp hoặc sơ đồ chỉ có ký hiệu/toán học dùng danh sách rỗng. Cụm tiếng Anh trong caption ngoài đồ họa không được chép vào ảnh chú giải.

Đã chạy `scripts/prepare-physics25-assets.py`: script tạo 51 crop cùng bốn contact sheet. Đã xem contact sheet và mở riêng các hình có lỗi crop ban đầu, năm hình bài tập E25.26–30 và sáu hình P25 mới. Chưa nhập module vào runtime, chưa build hay kiểm tra responsive website. Raw, catalog, cấu hình, style và Git không bị sửa.
