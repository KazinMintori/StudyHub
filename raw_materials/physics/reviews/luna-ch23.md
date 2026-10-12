# Luna độc lập: Rà chương 23 Điện thế

Ngày rà: 12-10-2026. Phạm vi: Bản dịch trong `raw_materials/physics/translations/chapter-23/`, bài Notes và năm topic của `docs/vat-ly-2/bai-giang/02-dien-the/`, Wiki điện thế và các hình được dùng trong chương. Đối chiếu PDF Young & Freedman ấn bản 15, chương in trang 747–780, cùng phụ lục đáp số A-15–A-16. Số trang PDF một-based là trang in + 20; tệp trích xuất trong `qa/physics/full-source/pdf-NNNN.txt` dùng số PDF một-based.

## Kết luận cần xử lý

**Lỗi crop P23.65 đã được xử lý trong lúc rà soát.** Bản ảnh cập nhật tại `docs/vat-ly-2/bai-giang/img/young-23/hinh-p23-65.png` hiện hiển thị đầy đủ nhãn điện áp `50.0 kV` và `Airflow`, khớp trang nguồn in 777 (PDF 797, ảnh `qa/physics/chapter23/p777.png`). Mình đã xem lại crop sau sửa. Hình được dẫn ở `raw_materials/physics/translations/chapter-23/11-bai-tong-hop-51-70.md:369`, trong bài 23.65 ở dòng 365. Parent đã chạy lại kiểm tra glossary nhãn ảnh sau cập nhật.

Các điểm nghi vấn đã được đối chiếu trực tiếp với nguồn. Năm mục 23.21/56/63/73/83 đều khớp; hướng điện trường ngoài ở 23.41(e) đã được bổ sung; câu Caution 23.2 về điểm không có điện tích thử nằm tại `02-dien-the.md:82`. Không còn phát hiện thiếu trong các mục đã rà.

- **Bài 23.21, trang in 774/PDF 794.** Đề cho $V_B-V_A=+12.0$ V, $y_B-y_A=0.0700$ m nên $E_y=-171$ V/m. Với $y_B-y_C=0.100$ m, $V_B-V_C=+17.1$ V. Bản dịch tại `09-bai-tap-01-25.md:461–` giữ đúng thứ tự hiệu điện thế; đáp số ghi cả chiều đảo dấu ở `13-dap-so.md:45`.
- **Bài 23.56, trang in 776/PDF 796.** Nguồn nói người cọ chân trên thảm nhận electron và mang điện âm, rồi câu cuối hỏi số electron tích tụ/lost khi cọ chân. Bản dịch tại `11-bai-tong-hop-51-70.md:137–` nêu đây là ước lượng, chọn $d\approx1$ mm, $E=3$ MV/m, diện tích hiệu dụng $1$ cm², suy ra $|Q|\approx2.7$ nC và $N\approx1.7\times10^{10}$. Phần giải nói rõ cấu hình âm là **nhận thêm electron**, giải quyết mâu thuẫn câu chữ của đề mà không đổi dấu điện tích.
- **Bài 23.63, trang in 777/PDF 797.** Hình nguồn đặt màn cách mép ra của bản 12.0 cm. Tính lại với $L=6.0$ cm, $d=2.0$ cm, $v_0=6.50\times10^6$ m/s, $|\Delta V|=22.0$ V cho độ lệch trong bản 0.824 cm, góc ra 15.4° và độ lệch màn 4.12 cm. Bản dịch và đáp số cùng dùng đúng khoảng cách từ mép ra ở `11-bai-tong-hop-51-70.md:304–310` và `13-dap-so.md:66`.
- **Bài 23.73, trang in 778/PDF 798.** Mô hình có $U(d)=\frac12\kappa d^2+ke^2/d$, nên $d_0=(ke^2/\kappa)^{1/3}$ và $U(d_0)=3ke^2/(2d_0)=2.16$ MeV. Nếu toàn bộ năng lượng này thành động năng của hai proton giống nhau thì mỗi proton có $v=1.44\times10^7$ m/s. Đề chỉ nói lò xo đứt, không mô tả phần năng lượng đàn hồi được truyền đi hay tiêu tán. Bản dịch `12-bai-nang-cao-mcat.md:76–` nêu hai cách phân bố năng lượng và đánh dấu giả thiết của mỗi tốc độ.
- **Bài 23.83, trang in 779/PDF 799.** Bảo toàn năng lượng với động năng tiếp tuyến tại điểm gần nhất cho $K_0=A/r+L^2/(2mr^2)$, $A=k(2e)(82e)$; thay $L=p_0b$ và $p_0^2=2mK_0$ được $r^2-r_0r-b^2=0$. Nghiệm dương trong bản dịch cho lần lượt $1.01\times10^{-12}$ m, $1.13\times10^{-13}$ m và $2.84\times10^{-14}$ m. Phần giải `12-bai-nang-cao-mcat.md:414–` cũng kiểm tra giới hạn $b\to0$ trở về bài va chạm thẳng tâm.

## Sổ đối chiếu độ bao phủ

| Thành phần | Nguồn chương | Bản dịch quan sát được | Kết quả |
| --- | --- | --- | --- |
| Mở đầu và mục tiêu học tập | Trang in 747 | `00-mo-dau.md` | Có tình huống hàn hồ quang, câu hỏi mở đầu và mục tiêu |
| Phần lý thuyết | 5 mục, 23 công thức đánh số | `01`–`05` | Đủ 5 mục và các thẻ `23.1`–`23.23` |
| Ví dụ | 14 ví dụ | `01`–`05` | Đủ tiêu đề Ví dụ 23.1–23.14 |
| Hình có số chương | 27 hình | `01`–`05` | Đủ Hình 23.1–23.27; hình mở đầu, tóm tắt và ứng dụng được dẫn riêng |
| Luyện tập có hướng dẫn | Trang in 771–772 | `07-luyen-tap-huong-dan.md` | Các biến thể và bài cầu nối có hướng dẫn |
| Câu hỏi thảo luận | 22 câu | `08-cau-hoi-thao-luan.md` | Đủ Q23.1–Q23.22, lời giải theo sau từng câu |
| Bài tập đánh số | 86 câu, gồm bài chọn lọc và bài nâng cao | `09`–`12` | Có đủ ID 23.1–23.86; cả bài chẵn và lẻ đều có hộp lời giải chi tiết |
| Biến thể và bài cầu nối | 12 biến thể, 1 bài nối chương | `07`, `12` | Sổ đáp án và các lời giải được giữ |
| Hộp lời giải chi tiết | 121 hộp | `07`–`12` | Bộ kiểm tra xác nhận đủ marker cho 86 bài, 22 câu hỏi, 12 biến thể và 1 bài cầu nối |
| Đáp số | Trang in 780 và phụ lục A-15–A-16 | `13-dap-so.md` | Bảng tra cứu tách đáp số bài lẻ theo cách trình bày của nguồn. Cả 86 bài, gồm bài chẵn và lẻ, đều có lời giải chi tiết trong các hộp gập riêng. |
| Topic Notes | 5 chủ đề | `02-dien-the/` | Có đủ trang thế năng, điện thế, tính điện thế, mặt đẳng thế và gradient |
| Kiến thức nền/Wiki | Điện thế, thế năng, gradient và khái niệm phụ trợ | `physics-potential-course.mjs`, `concepts.mjs`, `wiki-content.mjs`, `docs/wiki/` | ID và nội dung định nghĩa/giải thích kỹ thuật đều hiện diện; trang Wiki Điện thế giải thích $V=0$ không kéo theo $E=0$ |

Các phép đếm trên được kiểm lại trực tiếp trong 14 tệp dịch. Chúng xác nhận cấu trúc và ID; bản thân số lượng không chứng minh dịch hết mọi ý nghĩa trong nguồn.

Chi tiết đối chiếu từng ID 23.1–23.86, Q23.1–Q23.22, các biến thể hướng dẫn, bài nối chương, ứng dụng và Caution được lưu trong [exercise-ledger.md](C:/Users/Ai/Documents/StudyHub/qa/physics/reviews/ch23/exercise-ledger.md). Sổ này ghi phạm vi trang nguồn đã đọc, các điểm cần xem bằng ảnh và hai điểm đã sửa sau trao đổi với reviewer khác.

## Tính toán, hình và cách kiểm tra

Chạy lại `raw_materials/physics/verify_chapter23.py`: đầu ra báo đạt 20 nhóm kiểm tra số học, tích phân và đạo hàm cho lý thuyết. Chạy lại `raw_materials/physics/verify_chapter23_solutions.py`: đầu ra báo đạt 118 nhóm kiểm tra số, tích phân và đạo hàm; script xác nhận 121 marker lời giải. Đã xem các ảnh trang nguồn trực tiếp tại `qa/physics/chapter23/p772.png`–`p780.png`, các contact sheet chương và crop riêng P23.63/P23.65/P23.81. Crop P23.65 sau cập nhật giữ đủ nhãn như trang nguồn.

Các crop P23.63 và P23.81 giữ đủ hình, kích thước và nhãn. Trong `qa/physics/image-label-review.json`, bộ rà nhãn ghi nhận 87 hình có bảng giải nghĩa, 266 cặp nhãn và không có hình bỏ sót trên toàn bộ phạm vi được quét. Các mục chương 23 trong `docs/.vitepress/physics-image-labels.mjs` có bản dịch tiếng Việt cho nhãn chữ. Crop P23.65 đã được mở rộng, ảnh cập nhật hiện đủ nhãn `50.0 kV` và `Airflow`, và image-label audit đã chạy lại.

Cheatsheet của môn đặt trong `docs/.vitepress/physics-potential-course.mjs` tập trung vào định nghĩa, tính chất, công thức và điều kiện áp dụng. Các điều kiện dễ dùng sai đã được ghi cạnh công thức, gồm mốc vô hạn cho nguồn hữu hạn, giới hạn của công thức trường đều, đối xứng cầu, và việc không lấy đạo hàm ngoài trục từ điện thế chỉ biết trên trục. Không thấy lệch số học đáng kể với các kết quả đã tính lại.

## Giới hạn

Đây là lượt rà độc lập theo bản dịch, ảnh trang PDF render sẵn, nội dung OCR để định vị, các phép tính được mã hóa và các bài có dấu hiệu mơ hồ. Không đọc lại từng câu của 34 trang nguồn ở độ phóng đại đầy đủ để chứng nhận rằng mọi sắc thái văn xuôi, mọi chú thích nhỏ trong mọi hình và mọi chứng minh đã được giữ nguyên. Bộ kiểm tra số hiện tập trung vào các công thức trung tâm và các đáp án số, không thay thế việc dò từng dòng lời giải. Vì vậy kết luận là **độ bao phủ cấu trúc và các điểm nghi vấn đã nêu được kiểm tra, chưa phải xác nhận dịch thuật pháp chứng cho từng câu**.







## Disposition sau lượt kiểm tra tích hợp

Đã xem lại crop P23.65 đã mở rộng: 50,0 kV và nhãn Airflow đều nằm trọn trong ảnh, khớp Hình P23.65 trang in 777. Đã đọc lại Bài 23.41(e) tại `raw_materials/physics/translations/chapter-23/10-bai-tap-26-50.md` và đối chiếu trang nguồn 775: thành phần xuyên tâm ngoài là $k(q-Q)/r^2$, chiều ra/vào phụ thuộc dấu của $q-Q$, và trường bằng không khi $q=Q$.

Rà logic chi tiết các lời giải 23.72, 23.73 và 23.83. Với 23.72, mômen phục hồi, mômen quán tính và tần số dao động góc nhỏ nhất quán. Với 23.73, cực tiểu có $U\prime\prime(d_0)=3\kappa>0$; các giá trị năng lượng/tốc độ lần lượt 2,16 MeV và $1,44\times10^7$ m/s đúng với giả thiết toàn năng lượng truyền thành động năng. Cách diễn giải thứ hai được gắn rõ với giả thiết năng lượng đàn hồi không truyền sang các proton. Với 23.83, bảo toàn năng lượng tại điểm gần nhất phải giữ động năng tiếp tuyến; phương trình bậc hai và ba nghiệm đã được tính lại bằng Python, khớp các giá trị in trong lời giải. Không phát hiện lỗi logic mới trong các mục khó đã lấy mẫu.
