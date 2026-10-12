# Rà soát bài tập Chương 26.33–26.60

## Ranh giới nguồn

Phạm vi bắt đầu ở Bài 26.33 trên trang in 872, PDF một-based 892 (`qa/physics/full-source/pdf-0892.txt`). Phần được giao kết thúc ở Bài 26.60 trên trang in 874, PDF 894 (`pdf-0894.txt`). Bài 26.61 và 26.62 xuất hiện ngay sau 26.60 trên cùng trang in 874 nhưng nằm ngoài phạm vi. Các Bài 26.24–26.32 ở đầu trang 872 cũng không thuộc bản dịch.

Đã đọc toàn bộ phần trích văn bản 892–894 và render trực tiếp ba trang PDF. Một số đơn vị trong OCR văn bản thô bị mất nét chữ Hy Lạp. Ảnh nguồn xác nhận Bài 26.33 dùng $500\,\mathrm{\mu A}$, Bài 26.36 cho hệ số góc $5{,}00\,\mathrm{\mu F}$, Bài 26.41 dùng tụ $15{,}0$ và $20{,}0\,\mathrm{\mu F}$, Bài 26.45 có tụ pF và điện tích nC, Bài 26.47 dùng tụ $15$, $20$, $10\,\mathrm{\mu F}$, Bài 26.49 có $C=5{,}90\,\mathrm{\mu F}$ và số đo $110\,\mathrm{\mu C}$, Bài 26.50 có $C=6{,}00\,\mathrm{\mu F}$. Bản dịch giữ các tiền tố như trên ảnh, không theo chữ m dễ bị OCR nhầm.

Để giải Bài 26.55, đã xem thêm Hình 26.6a trên trang in 849, PDF 869. Cả hai nguồn đều có cực dương ở phía trên trong sơ đồ đó. Với số liệu riêng của Bài 26.55, $\mathcal E_2=36\,\mathrm V$ lớn hơn $\mathcal E_1=24\,\mathrm V$, nên dòng đi lên qua nhánh $\mathcal E_2$ và đi xuống qua nhánh $\mathcal E_1$.

## Bản đồ hình và nhãn

Các crop dự kiến nằm trong `docs/vat-ly-2/bai-giang/img/young-26/`. Thư mục ảnh chưa có các crop này khi viết báo cáo. Bản dịch đã đặt các đường dẫn tương ứng và viết caption tiếng Việt bên ngoài hình. Chú giải cho chữ và dấu cực nằm trong ảnh cần root bổ sung sau khi crop.

| Hình | Trang in / PDF | Crop dự kiến | Nội dung cần giữ |
| --- | --- | --- | --- |
| E26.34 | 872 / 892 | `hinh-e26-34.png` | Cuộn galvanometer $R_G$, điện trở nối tiếp $R$ và shunt mắc song song. |
| 26.20a | Trang lý thuyết trước đó | `hinh-26-20.png` | Nguồn, công tắc, $R$, $C$ mắc nối tiếp. Bài 26.38 và 26.40 cùng tham chiếu sơ đồ này. |
| E26.41 | 873 / 893 | `hinh-e26-41.png` | Hai tụ $15$ và $20\,\mathrm{\mu F}$ mắc song song, cực tính nạp ban đầu, công tắc, điện trở $50$ và $30\,\Omega$. |
| E26.45 | 873 / 893 | `hinh-e26-45.png` | Ba tụ $20$, $10$, $15\,\mathrm{pF}$, dấu cực trên từng tụ, công tắc và điện trở $25\,\Omega$. Cực tính làm các hiệu điện thế cùng chiều phóng. |
| E26.47 | 873 / 893 | `hinh-e26-47.png` | Tụ $15\,\mathrm{\mu F}$ song song với điện trở $25\,\Omega$ bên trái. Sau điện trở $75\,\Omega$ có nhánh $20\,\mathrm{\mu F}$ nối tiếp $50\,\Omega$, và nhánh hai điện trở $25\,\Omega$, tụ $10\,\mathrm{\mu F}$ song song với điện trở phía trên. Nguồn $100\,\mathrm V$, công tắc và ampe kế. |
| E26.49 | 873 / 893 | `hinh-e26-49.png` | Công tắc hai vị trí, nguồn $\mathcal E$, tụ $C$ và điện trở $R$. Vị trí 1 nối nhánh phóng, vị trí 2 nối nhánh nạp. |
| P26.54 | 874 / 894 | `hinh-p26-54.png` | $R_1$ nối tiếp $R_2$ trong một nhánh song song với $R_3$, cả cụm nối tiếp $R_4$ và nguồn. |
| P26.56 | 874 / 894 | `hinh-p26-56.png` | Hai điện trở song song nối tiếp với điện trở thứ ba. |
| P26.57 | 874 / 894 | `hinh-p26-57.png` | Hai thanh điện trở hai bên; điểm $a,b$ hở; ba nhánh nguồn $12$, $10$, $8\,\mathrm V$, mỗi nhánh có $1\,\Omega$. Cực dương các nguồn ở trái. |
| P26.58 | 874 / 894 | `hinh-p26-58.png` | Điện trở $20\,\Omega$ đặt trong băng và mắc song song với $10$ và $20\,\Omega$. Cụm nối tiếp với $15$, $10$, $5\,\Omega$ và nguồn $45\,\mathrm V$. |
| P26.59 | 874 / 894 | `hinh-p26-59.png` | Ba nhánh giữa hai nút, điện trở $5$, $8$, $10\,\Omega$, hai nguồn $12$ và $9\,\mathrm V$, hai điện trở $1\,\Omega$, mũi tên $I_1,I_2,I_3$. Cực dương 12 V ở trái, cực dương 9 V ở phải. |
| P26.60 | 874 / 894 | `hinh-p26-60.png` | Ba nhánh song song, nguồn $24\,\mathrm V$ với $3\,\Omega$, nguồn $\mathcal E$ với $2\,\Omega$, và điện trở $7\,\Omega$. Cực dương nguồn ở phía trên. |

## Kiểm tra tính toán

Chạy `python -I raw_materials/physics/verify_chapter26_33_60.py`, toàn bộ assertion được mã hóa đều qua. Script kiểm tra các giá trị số của bài galvanometer, ảnh hưởng của điện trở vôn kế, hằng số thời gian và trạng thái đầu/cuối của tụ, công suất, các mạng Kirchhoff và đơn vị RC. Mạch 26.57 và 26.59 được giải bằng phương trình nút để giữ đúng cực tính và dấu dòng.

Kết quả chính:

- Bài 26.33: $R_{sh}=0{,}641\,\Omega$ và điện trở nối tiếp vôn kế $975\,\Omega$. Bài 26.34 cần điện trở nối tiếp khoảng $12{,}9\,\Omega$ cùng shunt $0{,}0250\,\Omega$.
- Bài 26.35: Số chỉ vôn kế là $17{,}9\,\mathrm V$, giá trị thật là $22{,}7\,\mathrm V$, sai thấp khoảng $21{,}4\%$.
- Bài 26.36–26.42: $C_{26.36}=7{,}21\,\mathrm{\mu F}$; $\tau_{26.37}=2{,}89\,\mathrm s$; $t_{26.38}=151\,\mathrm{\mu s}$; Bài 26.41 cho $t=4{,}21\,\mathrm{ms}$ và $i=0{,}125\,\mathrm A$; Bài 26.42 có $\tau=11{,}098\,\mathrm s$.
- Bài 26.47: Ampe kế chỉ $0{,}938\,\mathrm A$ ngay sau khi đóng mạch và $0{,}606\,\mathrm A$ ở trạng thái ổn định. Tụ được xem như dây dẫn tại $t=0^+$ và như mạch hở ở $t\to\infty$.
- Bài 26.49: $Q_f=165{,}2\,\mathrm{\mu C}$, $R\approx464\,\Omega$ và thời gian đạt $99\%$ là $12{,}6\,\mathrm{ms}$. Bài 26.50 cho $q=199{,}8\,\mathrm{\mu C}$ khi dòng có độ lớn $0{,}180\,\mathrm A$.
- Bài 26.54–26.60: $R_3\approx12{,}1\,\Omega$ ở Bài 26.54; $P_{max}=72\,\mathrm W$ ở Bài 26.56; $V_{ab}=0{,}222\,\mathrm V$ khi hở và dòng qua pin 12 V là $0{,}464\,\mathrm A$ từ phải sang trái khi nối tắt $a,b$ ở Bài 26.57; Bài 26.58 làm tan băng khoảng $0{,}00619\,\mathrm{g/s}$; Bài 26.59 cho $I_1=0{,}848\,\mathrm A$, $I_2=2{,}14\,\mathrm A$, $I_3=0{,}171\,\mathrm A$ theo các mũi tên; Bài 26.60 cần $\mathcal E=8{,}60\,\mathrm V$ với cực dương ở trên.

## Giới hạn

Phạm vi rà soát là đề và lời giải Bài 26.33–26.60. Crop và nhãn tiếng Việt trên ảnh còn chờ, vì vậy báo cáo chưa xác nhận hiển thị sau tích hợp hoặc bề rộng công thức trên điện thoại. So sánh dây 12 gauge ở Bài 26.52 chỉ dùng mốc $20\,\mathrm A$ của mô hình mục 26.5, không thay thế quy định lắp đặt tại địa phương.
