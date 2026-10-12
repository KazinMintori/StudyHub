# Rà soát Luyện tập có hướng dẫn Chương 26

## Phạm vi và nguồn đối chiếu

Đã đối chiếu nguyên văn các bài VP26.2.1–VP26.2.4, VP26.7.1–VP26.7.4, VP26.13.1–VP26.13.4 và Bài cầu nối 26.27 với qa/physics/full-source/pdf-0888.txt cùng PDF gốc. Trang in 868 tương ứng PDF một-based 888, tức chỉ số trang PDF 887. Đã mở trực tiếp các sơ đồ trong PDF, không chỉ dựa vào OCR:

| Sơ đồ | Trang in / PDF | Đã kiểm tra trực tiếp |
| --- | --- | --- |
| Hình 26.1(a)–(d) | 845 / 865 | Quan hệ nối tiếp và song song của bốn cấu hình. |
| Hình 26.6a | 849 / 869 | Hai nhánh nguồn cùng cấp dòng vào nút a, cực dương của hai nguồn hướng về phía nút trên. |
| Hình 26.9a | 851 / 871 | Cực tính hai nguồn, chiều giả định của I1, I2, I3 và cách các dòng gặp tại hai nút. |
| Hình 26.10a | 851 / 871 | Cực dương ban đầu của hai pin ở bên trái; chiều vòng và các điện trở nối tiếp 2 Ω, 3 Ω, 4 Ω, 7 Ω. |
| Hình 26.12 | 853 / 873 | Vị trí các nút a–d, bốn nhánh 1 Ω, nhánh b–d, chiều dòng giả định và chiều các vòng. |
| Hình 26.27 | 868 / 888 | Hai tụ 2,40 μF và 3,60 μF nối tiếp, vôn kế 4,58×10⁴ Ω mắc song song với điện trở 655 Ω. Trang PDF xác nhận ký hiệu là μF và μC, không phải mF hoặc mC. |

## Độ bao phủ

| Đơn vị | Trạng thái | Nội dung |
| --- | --- | --- |
| Luyện tập điện trở | Đạt | Giữ các câu hỏi, lựa chọn cấu hình, giá trị linh kiện, suất điện động, điện trở trong không đáng kể, các dòng và công suất cần tìm. Mỗi câu có đề riêng và lời giải gập. |
| Luyện tập Kirchhoff | Đạt | Giữ chiều dòng và cực tính được nêu, các giá trị nguồn và điện trở, đầy đủ mục tiêu Vab, r1, r2, công suất từng nhánh và ba dòng I1, I2, I3. |
| Luyện tập mạch RC | Đạt | Giữ đủ dữ kiện và các phần hỏi. Ký hiệu vi mô được đối chiếu trực tiếp trên trang PDF: 3,20 μF; 2,20 μF và 4,20 μC; 8,00 μF, 5,50 μC, 1,10 μC; 6,40 μF. |
| Bài cầu nối 26.27 | Đạt | Giữ đủ đề bốn phần, sơ đồ, ba bước Nhận diện và bố trí, bốn bước Thực hiện, bước Đánh giá và gợi ý đối chiếu tốc độ mất năng lượng với công suất tỏa nhiệt. Lời giải còn kiểm tra độc lập đạo hàm dU/dt. |

Trong PDF, hướng dẫn lời giải của Bài cầu nối có tám bước đánh số: Ba bước Nhận diện và bố trí, bốn bước Thực hiện và một bước Đánh giá. Bản dịch giữ đủ tám bước được in và không thêm bước thứ chín.

## Kiểm tra số và mạch

Đã chạy python -X utf8 -I raw_materials/physics/verify_chapter26_guided.py. Bộ kiểm tra dùng phép giải nút với ma trận dẫn nạp cho các mạng điện trở, MNA cho các mạch có nguồn lý tưởng, sau đó kiểm tra KCL, hiệu điện thế nút và cân bằng công suất. Mạch RC được tính độc lập bằng các nghiệm hàm mũ. Kết quả: Tất cả kiểm tra đều đạt.

Các kết quả chính:

- VP26.2.1: Điện trở tương đương lần lượt là 7,00 Ω, 0,571 Ω, 2,33 Ω và 0,857 Ω.
- VP26.2.2: Dòng qua pin là 8,18 A. Dòng qua R1 là 6,00 A, còn dòng qua R2 và R3 đều là 2,18 A.
- VP26.2.3: Công suất pin là 54,6 W. Công suất trên R1, R2, R3 lần lượt là 20,6 W, 18,0 W và 16,0 W.
- VP26.2.4: Công suất pin là 9,84 W. Công suất trên R1, R2, R3 lần lượt là 5,98 W, 2,08 W và 1,78 W.
- VP26.7.1: Sau khi đảo pin 4 V, dòng là 1,00 A, Vab = 7,00 V, hai suất điện động cấp tổng cộng 16,0 W, bằng công suất tỏa nhiệt trong bốn điện trở.
- VP26.7.2: Vab = 7,75 V, r1 = 1,25 Ω và r2 = 0,926 Ω. Hai nhánh nguồn cho cùng điện áp nút.
- VP26.7.3: Năm công suất lần lượt là 33,4 W, 18,8 W, 2,09 W, 52,2 W và 25,0 W. Tổng công suất điện trở bằng công suất nguồn 13 V.
- VP26.7.4: I1 = (E2 − 2E1)/(3R), I2 = (E1 − 2E2)/(3R), I3 = −(E1 + E2)/(3R). KCL được kiểm tra với các chiều giả định trong hình.
- VP26.13.1: Q cuối = 28,8 μC, I ban đầu = 0,900 μA, τ = 32,0 s. Sau 18,0 s, q/Qcuối = 0,430 và i/Iban đầu = 0,570.
- VP26.13.2: Tụ đạt điện tích 1,20 μC sau 11,0 s. Dòng khi ấy có độ lớn 0,136 μA.
- VP26.13.3: R = 1,32 MΩ. Dòng ban đầu là 0,521 μA, còn dòng ở 17,0 s là 0,104 μA.
- VP26.13.4: Điện tích khi ngắt khỏi mạch nạp là 61,2 μC. Sau khi phóng 70,0 s qua điện trở mới, điện tích còn 9,89 μC.
- Bài cầu nối: Ceq = 1,44 μF, Req = 645,8 Ω, U0 = 9,39 μJ, dU/dt lúc đầu = −20,2 mW, thời điểm U = U0/e là 0,465 ms, và tại thời điểm đó dU/dt = −7,43 mW. Kết quả đạo hàm năng lượng bằng kết quả công suất tiêu tán.

## Trạng thái bàn giao

Ảnh trang PDF tạm thời dùng để đọc sơ đồ đã được gỡ khỏi thư mục làm việc. Bản dịch đang tham chiếu ảnh dự kiến trong img/young-26/. Chưa có crop hình để dựng trang và kiểm tra hiển thị, nên việc render ở 320 px còn chờ bộ ảnh của chương và build chung. Đây chỉ là phần luyện tập cùng bài cầu nối trong vùng nguyên liệu. Chưa tích hợp Notes, catalog hoặc xác nhận toàn bộ Chương 26 hoàn tất.
