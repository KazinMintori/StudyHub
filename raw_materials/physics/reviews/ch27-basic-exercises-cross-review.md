# Rà chéo độc lập: Bài tập 27.1–27.60

## Phạm vi và đối chiếu nguồn

Đã đọc các trang in 909–914 (PDF 929–934), đối chiếu đề 27.1–27.60 và các tiểu mục trong hai bản dịch. Các hình có ý nghĩa về chiều dòng, từ trường và lực được kiểm tra trực tiếp trên trang PDF. Đặc biệt, đơn vị vi mô ở bài Hall và hướng quỹ đạo E27.14 được xác nhận bằng ảnh trang in thay vì dựa vào lớp trích xuất văn bản. Rà bổ sung các đơn vị lý thuyết 27.1–27.9 ở trang in 878–905 (PDF 898–925), gồm các callout, ví dụ, lời giải tự kiểm tra và giả thiết được nêu trong nguồn.

Verifier xác nhận đủ 30 mã bài 27.1–27.30 và 30 mã bài 27.31–27.60, mỗi bài có khối lời giải. Verifier cũng tính lại các trường hợp vectơ, từ thông, quỹ đạo, mạch và Hall được liệt kê dưới đây. Đây là bộ kiểm tra độc lập có chọn lọc, không phải chứng nhận tự động mọi con số trong 60 lời giải.

## Phát hiện cần sửa

### P1 đã khắc phục — 27.46: Mật độ electron lệch do đơn vị Hall và công thức

Trang in ghi suất điện động Hall là **131 μV**. Dấu μ bị mất trong văn bản trích xuất, nên cần giữ đơn vị này khi tính. Từ 27.45:

$$
I=ne v_d z_1y_1,
\qquad
V_H=v_dBz_1.
$$

Khử vận tốc trôi làm chiều rộng đo điện áp triệt tiêu:

$$
n=\frac{IB}{eV_Hy_1}
 =3{,}70\times10^{28}\,\mathrm{m^{-3}}.
$$

Bản nháp ban đầu nhân thêm $z_1$ trong tử và cho $3{,}70\times10^{25}\,\mathrm{m^{-3}}$. Bản hiện tại đã bỏ thừa số đó, dùng 131 μV và cho $3{,}70\times10^{28}\,\mathrm{m^{-3}}$.

### P1 đã khắc phục — 27.56: Mạch có nhánh song song và phải tính trọng lực

Hình P27.56 mắc điện trở $25\,\Omega$ nối tiếp với hai nhánh song song: điện trở cố định $10\,\Omega$ và thanh $10\,\Omega$. Do đó $R_{\mathrm{tổng}}=30\,\Omega$, dòng nguồn là $4{,}00\,\mathrm{A}$ và dòng qua thanh là $2{,}00\,\mathrm{A}$. Lực từ có độ lớn:

$$
F_B=ILB=(2{,}00)(0{,}850)(1{,}60)=2{,}72\,\mathrm{N}.
$$

Thanh nặng $2{,}60\,\mathrm{N}$, nên lực tổng chỉ còn $0{,}120\,\mathrm{N}$; khối lượng là $2{,}60/9{,}80=0{,}265\,\mathrm{kg}$. Trong cấu hình nâng thanh, gia tốc ban đầu hướng lên và có độ lớn $0{,}452\,\mathrm{m/s^2}$. Bản nháp ban đầu coi $25\,\Omega$ và $10\,\Omega$ nối tiếp, bỏ qua trọng lực, rồi cho $17{,}6\,\mathrm{m/s^2}$. Bản hiện tại đã sửa mạch và cân bằng lực. Chiều lên được suy ra từ cách đặt thanh trong cấu hình nâng mà lời giải nêu rõ.

### P2 đã khắc phục — 27.55: Thiếu chiều dòng điện cụ thể

Bản nháp ban đầu chỉ yêu cầu chọn dòng bằng quy tắc bàn tay phải. Đáp án nguồn cho chiều **từ phải sang trái**; bản hiện tại đã ghi rõ chiều này và kèm sơ đồ lực.

### P2 đã khắc phục — 27.59: Thiếu chiều lực từ theo hình

Bản nháp ban đầu nói lực dọc theo ray và đổi chiều khi đảo dòng, nhưng chưa nêu chiều ở cấu hình đang vẽ. Đáp án nguồn cho lực hướng **sang phải**; bản hiện tại đã nêu hướng đó. Công thức quãng đường và kết quả $1{,}96\times10^6\,\mathrm{m}$ khớp với tính lại.

## Các đối chiếu dấu và dữ liệu quan trọng

- **27.7:** Hai lực “theo $+y$” là các vectơ lực đầy đủ. Lực của proton theo $+x$ không có thành phần $z$, nên $B_y=0$. Hai thành phần đo còn lại cho $B_x=1{,}117\,\mathrm{T}$, $B_z=-0{,}936\,\mathrm{T}$, do đó $|B|=1{,}46\,\mathrm{T}$. Bản hiện tại có ràng buộc $B_y=0$ và kiểm tra được cả hai phép đo.
- **27.8:** Lực theo $x,y$ xác định $v_x=-106\,\mathrm{m/s}$, $v_y=-48{,}6\,\mathrm{m/s}$. $v_z$ song song với trường nên không suy ra được. Tích vô hướng $\vec v\cdot\vec F=0$ với mọi $v_z$.
- **27.45–27.46:** Đơn vị trên ảnh trang in là 53 μV và 131 μV. Kết quả 27.45 là $53{,}1\,\mu\mathrm V$. Bản OCR cũng làm rơi dấu μ ở đáp án A-17, nên không thể dùng bản trích xuất thô để kết luận đó là mV.
- **27.31:** Dòng ngưỡng $32{,}7\,\mathrm{A}$ và điện áp $817\,\mathrm{V}$ phù hợp với lực từ hướng lên do dòng chạy sang phải và trường hướng vào trang. Khi điện trở giảm, gia tốc cũng hướng lên.
- **27.33–27.34:** Dòng qua thanh cân từ phải chạy sang phải khi $a$ nối cực dương, tạo lực lên. Các tích có hướng trong ba hướng trường của 27.34 lần lượt cho lực nam, tây và thành phần tây-bắc như lời giải.
- **27.37–27.41:** Các độ lớn mômen cho 27.37–27.39 lần lượt khớp $0{,}420\,\mathrm{N\,m}$, $0{,}113\,\mathrm{N\,m}$ và $2{,}91\times10^2\,\mathrm{rad/s^2}$. Với 27.39, trục A2 là trục ngang song song cạnh dài $1{,}00\,\mathrm m$, đúng với công thức mômen quán tính đã dùng.
- **27.43–27.44:** Dòng nhánh, suất điện động ngược và công suất lần lượt khớp $1{,}13\,\mathrm A$, $3{,}69\,\mathrm A$, $98{,}2\,\mathrm V$, $362\,\mathrm W$; bài nối tiếp cho $4{,}69\,\mathrm A$ và $492\,\mathrm W$.
- **27.47–27.54:** Tính lại các thành phần Lorentz cho 27.48 được $(0,2{,}76,1{,}47)\,\mathrm{mN}$. Kết quả vùng quỹ đạo 27.49–27.54 khớp các giá trị $8{,}30\times10^6\,\mathrm{m/s}$, $0{,}139\,\mathrm T$, $4{,}81\times10^7\,\mathrm{C/kg}$ và khoảng tách $1{,}68\,\mathrm{mm}$ giữa hai đồng vị krypton kề nhau.
- **27.60:** Tích có hướng cho $F_x=1{,}82\,\mathrm N$, $F_y=-0{,}448\,\mathrm N$, $F_z=0$, và độ lớn tổng $1{,}88\,\mathrm N$.

27.37 còn lặp nhãn “(c)” hai lần trong lời giải, trước phần kiểm tra mômen vectơ. Đây là lỗi biên tập nhỏ, không đổi kết quả.

## Rà bổ sung lý thuyết và nội dung hiện đã sửa

- Đối chiếu trực tiếp các phần 27.1–27.9 cho thấy các ví dụ chính, phần ứng dụng sinh học, cảnh báo, chiến lược giải và câu tự kiểm tra đều có trong bản dịch. Câu hỏi mở đầu chương được để dạng câu hỏi như nguồn, không phải tiểu mục giải mẫu.
- Hai ghi chú nguồn đã được bổ sung để giữ đầy đủ lập luận sư phạm. Ngay sau phương trình (27.2), nguồn nói định luật lực từ là kết quả thực nghiệm, không được suy ra lý thuyết trong chương này. Sau phương trình (27.20), nguồn giải thích công thức dây dẫn vẫn đúng cho hạt tải âm hoặc khi có đồng thời hạt tải hai dấu. Điều này làm rõ cách dùng công thức với kim loại.
- Mục 27.5 giữ các giá trị $e/m$ và $m_e$ kèm ký hiệu sai số trong ngoặc, đồng thời đã bổ sung giải thích rằng $(11)$ biểu thị độ không chắc ở các chữ số cuối. Các con số là giá trị của ấn bản nguồn, không nên giới thiệu như cập nhật hiện hành.
- **27.7 đã được sửa đúng theo phép đo vectơ đầy đủ:** Vì proton đi theo $+x$ chịu lực hoàn toàn theo $+y$, thành phần lực $z=0$ buộc $B_y=0$. Trường duy nhất là $(1{,}117\hat i-0{,}936\hat k)\,\mathrm T$, có độ lớn $1{,}46\,\mathrm T$.
- **27.14–27.15 đã được sửa theo hình E27.14:** Electron đi lên ở điểm trái và cong theo chiều kim đồng hồ, nên $B$ hướng vào trang. Proton cần trường ngược chiều, hướng ra trang, với độ lớn $0{,}294\,\mathrm T$ và thời gian nửa vòng $1{,}11\times10^{-7}\,\mathrm s$. Đáp án A-17 in cho 27.15 là $0{,}160\,\mathrm{mT}$ hướng vào trang, sai cả độ lớn lẫn chiều; không nên dùng đáp án phụ lục này để thay cho phép tính từ hình và dữ kiện.
- Các sửa đổi hiện tại cho 27.46, 27.55, 27.56 và 27.59 đã được kiểm tra lại theo PDF và phép tính độc lập. Dấu μ ở các suất điện động Hall 27.45 và 27.46 cũng đã được nhìn trực tiếp trên trang, không dựa vào OCR.

## Chạy verifier

```powershell
& 'C:\Users\Ai\miniconda3\python.exe' -X utf8 raw_materials/physics/verify_chapter27_basic_cross.py
```

Kết quả: đủ mã bài nguồn/dịch và các phép kiểm tra vectơ, từ thông, chuyển động, mạch, Hall được chọn đều qua. Kiểm tra riêng mạch 27.56 cho $I_{\mathrm{bar}}=2{,}00\,\mathrm A$, $F_B=2{,}72\,\mathrm N$ và gia tốc trong trường hợp lực nâng hướng lên là $0{,}452\,\mathrm{m/s^2}$.

SHA-256 PDF nguồn `young-freedman-15.pdf`: `F4EA22DC8D5113F47EC8FD8A2B9F71F7BE78EE3DB069971AACE4B7CDA04175FF`.
