# Rà chéo Chương 26 trước tích hợp

## Phạm vi và giới hạn

Đã đọc lại raw `00`–`10`, `docs/.vitepress/physics-dc-course.mjs`, `docs/.vitepress/physics-dc-foundations.mjs`, cùng phần PDF nguồn có trang in 844–874 (PDF 864–894). Đã đối chiếu trực quan các sơ đồ E26.26, P26.57–P26.60 trên trang nguồn và tính lại độc lập các mạng P26.57, P26.59, P26.60 cùng các biến thể E26.26–E26.28 bằng Python.

**Không thể kết luận toàn chương đã hoàn tất:** Raw `11`–`12` nằm ngoài phạm vi và vẫn đang được hoàn thiện. Báo cáo này không đánh giá định dạng công thức trong raw10 vì file đang được root bẻ dòng. Việc kiểm tra câu chữ sau dấu hai chấm chỉ áp dụng cho raw00–09.

## Phát hiện cần xử lý

### P1 — Hình P26.57 bị crop và chú thích bỏ sót điện trở nhánh giữa

Lời giải số học P26.57(a) trong raw đúng: $V_{ab}=+2/9\,\mathrm V$. Tuy nhiên, chú thích **Hình P26.57** nói ba nhánh nguồn mỗi nhánh có điện trở 1 Ω, còn sơ đồ đầy đủ ở PDF trang 894 (trang in 874) có thêm điện trở 3 Ω nối tiếp trên nhánh giữa, cùng các điện trở ở hai thanh đứng. Crop hiện tại `docs/vat-ly-2/bai-giang/img/young-26/hinh-p26-57.png` chỉ cho thấy phần trái của hình, nên người học không thể đọc đủ mạng để tự dựng phương trình. Cần giữ trọn sơ đồ trong crop và bổ sung điện trở 3 Ω vào chú thích.

Đối chiếu MNA khi để hở a–b: vòng ngoài có tổng điện trở $9\,\Omega$ và hai nguồn 12 V, 8 V đối kháng, nên dòng vòng là $4/9\,\mathrm A$, chạy theo chiều $TL\to BL\to BR\to TR\to TL$. Chọn $BL=0\,\mathrm V$, ta được $V_{TL}=16/9\,\mathrm V$, $V_a=8/9\,\mathrm V$, $V_{BR}=-76/9\,\mathrm V$, $V_{TR}=-88/9\,\mathrm V$ và $V_{MR}=-28/3\,\mathrm V$. Nhánh b hở nên dòng qua điện trở 1 Ω, pin 10 V và điện trở 3 Ω bằng không. Do cực dương của pin ở phía b, $V_b=V_{MR}+10=2/3\,\mathrm V$, suy ra $V_{ab}=2/9\,\mathrm V$. Tại nút MR, kiểm tra KCL cho $(V_{MR}-V_{TR})/1+(V_{MR}-V_{BR})/2=0$.

Hệ nút mở (sáu nút vòng ngoài, lấy $V_{BL}=0$) là:

$$
\begin{aligned}
\frac{V_{TL}-V_a}{2}+V_{TL}-V_{TR}-12&=0,\\
\frac{V_a-V_{TL}}{2}+\frac{V_a}{2}&=0,\\
V_{TR}-V_{TL}+12+V_{TR}-V_{MR}&=0,\\
V_{MR}-V_{TR}+\frac{V_{MR}-V_{BR}}{2}&=0,\\
\frac{V_{BR}-V_{MR}}{2}+V_{BR}+8&=0.
\end{aligned}
$$

Nhánh giữa nối với đầu hở b có dòng $I_b=(V_b-V_{MR}-10)/4=0$. Đây là điều kiện dùng để suy ra $V_b$ sau khi giải các nút vòng ngoài.

Khi nối tắt a–b, lời giải raw cũng khớp MNA toàn mạng dưới đây. Dòng qua pin 12 V có độ lớn $13/28\,\mathrm A\approx0{,}464\,\mathrm A$ từ phải sang trái.

### P1 — Crop E26.26 cắt nhánh trên, ảnh được dùng lại cho 26.27–26.28

Raw09 dùng `hinh-e26-26.png` cho cả 26.26–26.28. Crop hiện có cắt mép trên của nhánh trên. PDF trang 892 (trang in 872) cho thấy đầy đủ nhánh trên gồm 2 Ω, pin 10 V và 3 Ω, nhánh giữa gồm 1 Ω, pin 5 V và 4 Ω, cùng điện trở đáy 10 Ω. Mép crop làm các nhãn và phần tử nhánh trên khó đọc, nên ba bài dựa vào cùng hình đều bị ảnh hưởng. Cần kiểm tra lại khung ảnh từ trang PDF đầy đủ.

## Đối chiếu số học độc lập

| Bài | Kiểm tra | Kết quả đối chiếu |
|---|---|---|
| E26.26 | Chọn $V=V_L-V_R$, ba dòng trái sang phải lần lượt là $(V-10)/5$, $(V-5)/5$, $V/10$. | $V=6{,}00\,\mathrm V$. Dòng nhánh trên, giữa, dưới là $-0{,}800$, $+0{,}200$, $+0{,}600\,\mathrm A$. Tại các điểm a, b: $V_{ab}=-3{,}20\,\mathrm V$. Khớp raw. |
| E26.27 | Đảo pin trên, nên suất điện động nhánh trên theo chiều trái sang phải là $-10\,\mathrm V$. | $V=-2{,}00\,\mathrm V$. Dòng ba nhánh là $+1{,}60$, $-1{,}40$, $-0{,}200\,\mathrm A$. $V_{ab}=+10{,}4\,\mathrm V$. Khớp raw. |
| E26.28 | Pin giữa 15 V có cực dương bên trái. | $V=10{,}0\,\mathrm V$. Dòng ba nhánh là $0$, $-1{,}00$, $+1{,}00\,\mathrm A$. $V_{ab}=+4{,}00\,\mathrm V$. Khớp raw. |
| P26.57(a), b để hở | MNA sáu nút vòng ngoài; điện thế đầu hở b suy từ nhánh giữa có dòng bằng không. | Với $BL=0$, $V_{TL}=16/9$, $V_a=8/9$, $V_{TR}=-88/9$, $V_{MR}=-28/3$, $V_{BR}=-76/9\,\mathrm V$. Nhánh b hở cho $V_b=V_{MR}+10=2/3\,\mathrm V$, nên $V_{ab}=+2/9\,\mathrm V$. Khớp raw. |
| P26.57(b) | MNA toàn mạng sau khi nối tắt a–b. | Có 6 nút vật lý (BL, TL, A=a=b, TR, MR, BR) và 7 nhánh. Chọn BL = 0 V. Các nút lần lượt $V_{TL}=25/14$, $V_A=6/7$, $V_{TR}=-39/4$, $V_{MR}=-65/7$, $V_{BR}=-59/7\,\mathrm V$. Nhánh trên có 1 Ω nối tiếp nguồn 12 V cực dương trái, nên $I_{12}=V_{TL}-V_{TR}-12=-13/28\,\mathrm A$. Dòng thực là $0{,}464\,\mathrm A$ từ phải sang trái, khớp raw. |
| P26.58 | Tổ hợp song song 20 Ω, 10 Ω, 20 Ω nối tiếp 15 Ω, 10 Ω, 5 Ω; nguồn 45 V. | $R_p=5{,}00\,\Omega$, $I=45/35=1{,}286\,\mathrm A$, điện áp cụm song song $6{,}429\,\mathrm V$, công suất trên điện trở đặt trong băng $2{,}066\,\mathrm W$. Tốc độ nóng chảy $6{,}19\times10^{-6}\,\mathrm{kg/s}=0{,}00619\,\mathrm{g/s}$. Khớp raw sau làm tròn. |
| P26.59 | Mạng có 3 nút và 5 nhánh; nút phải làm mốc. Nguồn 12 V có cực dương trái, nguồn 9 V có cực dương phải; hai điện trở 1 Ω nằm nối tiếp từng nguồn ở nhánh giữa. | $V_L=1{,}7062\,\mathrm V$, $V_M=-8{,}1517\,\mathrm V$. Theo mũi tên trên hình, $I_1=V_M+9=0{,}8483\,\mathrm A$, $I_2=V_M-V_L+12=2{,}1422\,\mathrm A$, $I_3=V_L/10=0{,}1706\,\mathrm A$. Khớp raw. |
| P26.60 | Mạng 2 nút, 3 nhánh. Cực dương của nguồn 24 V và nguồn $\mathcal E$ đều ở trên. | Điện áp nút trên–dưới là $7(1{,}80)=12{,}6\,\mathrm V$. Dòng xuống nhánh 24 V là $(12{,}6-24)/3=-3{,}80\,\mathrm A$. KCL cho dòng xuống nhánh $\mathcal E$ là $2{,}00\,\mathrm A$, vậy $\mathcal E=12{,}6-2(2{,}00)=8{,}60\,\mathrm V$. Khớp raw. |

Các phương trình MNA cho P26.57(b), lấy BL làm mốc và biểu diễn các điện trở nối tiếp nguồn bằng dòng nhánh, là:

$$
\begin{aligned}
\frac{V_{TL}-V_A}{2}+V_{TL}-V_{TR}-12&=0,\\
\frac{V_A-V_{TL}}{2}+\frac{V_A}{2}+\frac{V_A-V_{MR}-10}{4}&=0,\\
V_{TR}-V_{TL}+12+V_{TR}-V_{MR}&=0,\\
V_{MR}-V_{TR}+\frac{V_{MR}-V_{BR}}{2}+\frac{V_{MR}-V_A+10}{4}&=0,\\
\frac{V_{BR}-V_{MR}}{2}+V_{BR}+8&=0.
\end{aligned}
$$

Trong nhánh giữa, tổng điện trở là $1+3=4\,\Omega$. Bỏ điện trở 3 Ω sẽ không còn cho nghiệm nút trên $25/14\,\mathrm V$ và nút trên phải $-39/4\,\mathrm V$ đang ghi trong raw.

## Các mục đã kiểm tra, chưa thấy sai lệch trọng yếu

- Raw01–05 lần lượt bao quát các mục 26.1–26.5; các ví dụ chính 26.1–26.14 đều có mặt. Raw08 có đủ Q26.1–Q26.21. Raw09 và raw10 có các bài 26.1–26.60. Đây chỉ là kiểm kê trong phạm vi đã đọc, không xác nhận phần raw11–12.
- Raw07 có 13 bài kèm 13 lời giải; 12 mục dùng nhãn “Hướng đi”, còn bài cầu nối mở bằng “Nhận diện và bố trí”. Raw08 có 21 câu hỏi, 21 lời giải và 21 hướng đi. Raw09 có 32 bài, lời giải và hướng đi tương ứng. Raw10 có 28 bài, lời giải và hướng đi tương ứng. Việc đếm cấu trúc này không thay cho kiểm tra từng phép tính trong toàn bộ tập bài.
- Mô tả đo điện trong raw03 phân biệt đúng vị trí mắc và ảnh hưởng của ampe kế, vôn kế thực. Hai cách đo điện trở dùng đúng dòng/điện áp hiệu chỉnh. Phần chiết áp nêu điều kiện dòng qua nhánh nguồn cần đo bằng không ở cân bằng.
- Phần R-C raw04 giữ đúng điều kiện đầu tụ chưa nạp, nguồn lý tưởng không đổi, dấu dòng khi phóng và cân bằng năng lượng. Công thức năng lượng của tụ khi nạp bắt đầu từ trạng thái chưa tích điện được đặt đúng phạm vi.
- Raw05 giữ các trị số 120/240 V trong bối cảnh mô hình Bắc Mỹ/châu Âu, nói rõ điện áp hình sin là hiệu dụng, và ghi các số liệu dây dẫn là dữ kiện mô hình chứ không phải quy tắc lắp đặt hiện hành. Không thấy câu khuyến khích tự sửa hệ thống dây điện.
- Cheatsheet trong `physics-dc-course.mjs` chỉ chứa công thức, định nghĩa và điều kiện, không lẫn câu hỏi hay lời giải bài tập. Tám slide tóm lược các kết quả chính. Các khái niệm trong `physics-dc-foundations.mjs` có ví dụ và điều kiện dùng cơ bản phù hợp; các quy tắc Kirchhoff giới hạn trường hợp không có suất điện động cảm ứng chưa tính.
- Một chỗ lặp câu nhỏ trong raw01, ngay trước (26.4): “Do $V_{ab}=I_1R_1=I_2R_2$, tỉ số hai dòng là” rồi ngay sau là “Với hai điện trở mắc song song, tỉ số dòng điện là”. Có thể bỏ một trong hai lời dẫn.
- Công thức $P=VI$ trong mục `distribution` của cheatsheet nói áp dụng cho mạch một chiều hoặc tải thuần trở trong mô hình xoay chiều. Nếu $P$ ở đây là công suất trung bình của mạch xoay chiều, nên ghi rõ $V$ và $I$ là giá trị hiệu dụng. Phần raw05 đã phân biệt điện áp hiệu dụng, còn mô tả cheatsheet chưa nói rõ quy ước đó.
- Trong raw00–09, không thấy cụm “theo sách”, “bản dịch”, câu nghĩ thành tiếng, khẳng định tần suất lỗi người học không có căn cứ, dấu chấm phẩy hoặc dấu gạch ngang dài trong văn xuôi. Những dấu hai chấm văn xuôi được rà đều theo sau bằng chữ hoa. Raw10 không được rà định dạng theo yêu cầu đang bẻ dòng.
