# Rà soát chương 25, bài 25.59–25.82

## Phạm vi và nguồn đã đối chiếu

Đã đối chiếu bản dịch với văn bản trích xuất `qa/physics/full-source/pdf-0861.txt` đến `pdf-0863.txt`, tương ứng trang in 841–843, và xem các ảnh trang nguồn `qa/physics/chapter25/p841.png` đến `p843.png` cho hình mạch, đồ thị và lựa chọn MCAT. Ranh giới trang: 25.59–25.68 ở tr. 841; 25.69–25.74 ở tr. 842; 25.75–25.82 ở tr. 843.

Đã đọc `raw_materials/physics/math-format-guidelines.md`. Hai bản thảo giữ các đề 25.59–25.78 và passage cùng câu hỏi 25.79–25.82. Các lời giải đều có tóm tắt, hướng giải nêu công thức hoặc tính chất cần dùng và lý do, sau đó là phép tính hoặc lập luận. Script `verify_chapter25_59_82.py` chạy được và tính lại các kết quả số độc lập.

## Sổ đối chiếu theo ID

| ID | Trang | Nội dung đã kiểm | Kết quả |
| --- | ---: | --- | --- |
| 25.59 | 841 | Nón cụt, chia lát, tích phân điện trở và giới hạn (r_1=r_2) | Đủ (a), (b); công thức giới hạn khớp dây trụ. |
| 25.60 | 841 | Điện trở giữa hai mặt cầu, mật độ dòng theo bán kính, giới hạn khe hẹp | Đủ (a)–(c); dẫn xuất từ diện tích (4\pi r^2). |
| 25.61 | 841 | Hai trạng thái nạp/xả và chiều dòng qua pin | Đủ dữ kiện, chiều dòng, (a), (b); (r=0{,}36\,\Omega), (\mathcal E=8{,}94\,\mathrm V). |
| 25.62 | 841 | Mạch có pin 8 V, 4 V, điện trở trong; thêm pin 10,30 V ở đầu d | Đủ (a)–(c), đã đưa hình mạch. Kết quả kiểm tra: (V_{ad}=6{,}583\,\mathrm V), điện áp hai cực pin 4 V là (4{,}083\,\mathrm V), sau khi thêm pin là (3{,}871\,\mathrm V). |
| 25.63 | 841 | Mô hình điện trở cơ thể dạng trụ, dòng nguy hiểm 100 mA | Đủ (a)–(c); giữ lưu ý điện trở da được bỏ qua khi ngâm tay nước muối. |
| 25.64 | 841 | Nguồn 14 kV, điện trở người 10 kΩ, điện trở trong nguồn 2 kΩ | Đủ (a)–(c); tính dòng, công suất và điện trở trong tối thiểu. |
| 25.65 | 841 | Tiền điện bóng 75 W bật liên tục và tủ lạnh 400 W chạy 8 giờ/ngày | Đủ giá điện và lịch hoạt động; với 365 ngày/năm, kết quả lần lượt 78,84 USD và 140,16 USD. Ảnh đáp số in là 78,90 USD và 140,27 USD. Dùng 365,25 ngày cho 78,894 USD và 140,256 USD, rất gần các số in. Bản giải nêu rõ quy ước 365 ngày thay vì âm thầm khớp đáp số. |
| 25.66 | 841 | Cáp đồng 1,50 km, 220 V, công suất tỏa nhiệt 90,0 W | Đủ (a), (b); tính đường kính và điện trường. |
| 25.67 | 841 | Điện trở suất (a+bx^2), điện trở toàn thanh, điện trường giữa, điện trở hai nửa | Bản dịch giữ nguyên bán kính 1,10 cm như đề in. Kết quả theo đề: R = 0,171 mΩ, E giữa = 0,176 mV/m, hai nửa 0,0547 và 0,116 mΩ. Ảnh đáp số cho thấy các số tương ứng là 171 µΩ, 176 µV/m, 54,7 µΩ và 116 µΩ, phù hợp với phép tính; văn bản OCR đọc nhầm µ thành m. |
| 25.68 | 841 | So sánh đèn compact huỳnh quang 23 W và đèn sợi đốt 100 W trong 3 năm | Đủ công suất, tuổi thọ, giá bóng, 4 giờ/ngày và giá điện; tính số bóng cần mua nguyên chiếc. Chi phí xấp xỉ 19,06 USD và 39,54 USD, tiết kiệm 20,48 USD; (R=626\,\Omega) ở 120 V. |
| 25.69 | 841–842 | Hai ống nước hình trụ, một nước cất, một nước muối; salinity, tụ điện, công suất, nửa công suất điện trở nối tiếp | Đủ (a)–(d), giữ (r=5{,}00\) cm, (L=3{,}00\) cm, 10,0 V, 15,0 Ω, 484 mA và hằng số điện môi 80,4. Các kết quả kiểm tra lần lượt khoảng 4,25 ppt, 511 pC, 1,33 W và 1,60 ppt. |
| 25.70 | 842 | Mạch có hai tụ, trạng thái cuối, biết (Q_1) | Đủ hai ý; dùng nhánh tụ hở mạch ở trạng thái một chiều ổn định, được (Q_2=36{,}0\) mC và (R_1=22{,}0\,\Omega). |
| 25.71 | 842 | Mạch hai điện trở và một tụ, điện tích cuối | Đủ; (\mathcal E=6{,}67\) V. |
| 25.72 | 842 | Đồ thị (V_{ab}) theo I, tìm suất điện động, điện trở trong và tải tại 80% | Đủ (a), (b), có dẫn đọc giao điểm và hệ số góc của đường thẳng; (\mathcal E=36\) V, (r=2\,\Omega), (R=8\,\Omega). |
| 25.73 | 842 | Bảng số liệu A/B, đồ thị V–I và R–I, tính chất Ohm, công suất ở 4,00 V | Đủ (a)–(e), giữ toàn bộ dữ liệu. Fit bậc hai cho A để ước lượng điểm làm việc cho (P_A\approx9{,}36\) W; B cho (4{,}12\) W. Đây là nội suy từ dữ liệu hữu hạn, không phải một định luật chính xác cho A. |
| 25.74 | 842 | Bảng gauge/đường kính/dòng tối đa, tải 4200 W, chiều dài 42,0 m, 12 giờ/ngày | Đủ (a)–(d), giữ cả bảng dữ liệu và đơn giá 0,11 USD/kWh. Chọn gauge 8 làm dây nhỏ nhất đủ tải; tổn hao và tiết kiệm được tính từ điện trở đồng. |
| 25.75 | 842 | Điện trường hướng tâm trong điện trở trụ rỗng, tích phân hiệu điện thế và tìm điện trở suất | Đủ (a)–(d); giải thích chiều trường từ vỏ ngoài có thế cao về lõi. |
| 25.76 | 842 | Bóng tungsten, nhiệt độ phụ thuộc tuyến tính dòng điện, giải dòng ở 120 V và 60 V | Đủ (a)–(e), bao gồm gợi ý giải phương trình phi tuyến. Kết quả số được tính bằng tìm nghiệm dòng; (I_{120}\approx0{,}720\) A, (I_{60}\approx0{,}450\) A. |
| 25.77 | 843 | Thanh bán dẫn với (\rho(x)=\rho_0e^{-x/L}), tìm R, I, E(x), V(x), vẽ đồ thị | Đủ (a)–(d), giữ điều kiện đầu (V(0)=V_0), (V(L)=0); tích phân (V(x)) dùng điều kiện biên đúng. |
| 25.78 | 843 | Công suất tải theo R, hai giới hạn, cực đại và ba tải cụ thể | Đủ (a)–(d), có chứng minh đạo hàm đổi dấu; công suất tại 2, 4, 6 Ω lần lượt 227,6 W, 256 W, 245,8 W. |
| 25.79 | 843 | Giải thích bảng điện trở khi kéo và thả sợi tơ | Giữ đủ dữ liệu passage và bốn lựa chọn; chọn giải thích lớp phủ hút ẩm mỏng đi khi kéo, gần phục hồi khi co. |
| 25.80 | 843 | Tỉ số tiết diện lớp phủ ở 13 mm và 5 mm, giả thiết điện trở suất không đổi và phủ đồng đều | Giữ giả thiết; tính (A_{13}/A_5=(13/5)(9/102)=0{,}229\), gần (1/4), chọn (b). Ảnh đáp án đã được xem để xác nhận lựa chọn phân số. |
| 25.81 | 843 | Dòng lớn nhất với pin 9 V | Giữ các lựa chọn và dùng điện trở nhỏ nhất 9 GΩ; (I_{\max}=1\) nA, chọn (d). |
| 25.82 | 843 | Sợi tơ bị hút về vật mang điện dương lẫn âm | Giữ đủ quan sát và lựa chọn; giải thích phân cực cảm ứng của vật dẫn trung hòa, chọn (d). |

## Sai khác nguồn cần giữ minh bạch

Ở bài 25.67, đề trang 841 ghi bán kính **1,10 cm**. Phép tính từ dữ kiện đề cho R = 0,171 mΩ, E giữa = 0,176 mV/m, hai nửa 0,0547 mΩ và 0,116 mΩ. Ảnh đáp số phóng to tại `qa/physics/chapter25/appendix25-67.png` đọc rõ các tiền tố µ: 171 µΩ, 176 µV/m, 54,7 µΩ và 116 µΩ. Các giá trị khớp. Văn bản OCR đã chuyển ký hiệu µ thành m, nên không dùng riêng OCR để kết luận có sai khác.

Ở bài 25.65, đề không quy định số ngày trong một năm. Dùng 365 ngày cho kết quả 78,84 USD và 140,16 USD. Dùng 365,25 ngày cho 78,894 USD và 140,256 USD. Đáp số in là 78,90 USD và 140,27 USD, gần quy ước năm 365,25 ngày, với sai khác vài phần trăm đô la do làm tròn hoặc quy ước số ngày. Bản giải ghi rõ quy ước 365 ngày.

## Hình và giới hạn hoàn tất

Các vị trí hình cần gắn sau khi root tạo crop: P25.59 (hình nón cụt với h, r₁, r₂); P25.62 (sơ đồ mạch và nhãn nút); P25.69 (hai ống, pin, ampe kế và điện trở); P25.70 và P25.71 (các nhánh R–C); P25.72 (đồ thị điện áp đầu cực theo dòng điện, có đơn vị trên hai trục). Bản thảo hiện giữ liên kết dự kiến `hinh-p25-59.png`, `hinh-p25-62.png`, `hinh-p25-69.png`, `hinh-p25-70.png`, `hinh-p25-71.png`, `hinh-p25-72.png`. Tại lần kiểm tra này các file crop đó chưa có trong thư mục ảnh, vì vậy chưa thể kiểm tra crop thực tế hay chốt bản đồ chú giải tiếng Anh trên hình.

Phạm vi này chỉ hoàn tất bản thảo và phép tính độc lập cho bài 25.59–25.82. Chưa xác nhận các crop, bản đồ nhãn ảnh, tích hợp trang công khai, build toàn site hay chất lượng đầy đủ của chương 25. Không đánh dấu chương 25 hoàn tất.
