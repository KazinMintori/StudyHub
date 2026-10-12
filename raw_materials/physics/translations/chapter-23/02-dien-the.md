<!-- Source: Section23.2, printed754–759, PDF774–779. -->

## 23.2. Điện thế

Điện trường mô tả lực trên một đơn vị điện tích thử. Theo cách tương tự, ta muốn mô tả thế năng trên một đơn vị điện tích thử khác không. Đại lượng mới này là **điện thế**, ký hiệu V:

$$
\begin{aligned}
V&=\frac{U}{q_0},\\
U&=q_0V.
\end{aligned}
\tag{23.12}
$$

Thế năng và điện tích đều là số vô hướng, nên điện thế cũng là số vô hướng. Đơn vị SI là volt, đặt theo tên Alessandro Volta (1745–1827):

$$
1\,\mathrm V=1\,\frac{\mathrm J}{\mathrm C}.
$$

Điện thế thường dễ tính hơn điện trường vì không phải cộng vector. Sau khi tính điện thế, có thể dùng sự biến thiên theo vị trí để suy ra trường.

### Hiệu điện thế và công trên đơn vị điện tích

Chia hệ thức công của lực điện cho q₀:

$$
\begin{aligned}
\frac{W_{a\to b}}{q_0}&=-\frac{U_b-U_a}{q_0}\\
&=V_a-V_b
\end{aligned}
\tag{23.13}
$$

Hiệu $V_a-V_b$ là **điện thế của a so với b**, ký hiệu $V_{ab}$. Thứ tự chỉ số quyết định dấu. Nói “hiệu điện thế giữa a và b” mà không nêu điểm được lấy làm mốc có thể gây nhầm. Trong mạch điện, đại lượng ấy thường gọi là điện áp.

Chẳng hạn pin 1,5 V có điện thế cực dương cao hơn cực âm 1,5 V. Khi điện tích dương 1 C đi từ a đến b, công lực điện bằng $V_{ab}$ joule.

![Hình 23.11: Điện thế cực dương cao hơn cực âm của pin 1,5 V](../img/young-23/hinh-23-11.png)

Theo cách nhìn bằng lực ngoài, $V_{ab}$ cũng bằng công trên mỗi coulomb cần để đưa điện tích dương thật chậm **từ b đến a** chống lại lực điện. Ở đây chiều di chuyển đảo so với công lực điện vừa nói. Việc nói rõ chiều và lực nào sinh công giúp giữ đúng dấu.

Dụng cụ đo hiệu điện thế gọi là volt kế. Volt kế đo mức 1 mV là thông dụng, còn các phép đo nhạy được mô tả trong hệ dữ kiện này có thể đạt mức $10^{-12}$ V.

### Điện thế do nguồn điểm và nhiều nguồn

Chia (23.9) cho q₀:

$$
V=\frac{kq}{r}.
\tag{23.14}
$$

Mốc V = 0 chọn ở vô hạn. Nguồn q dương tạo điện thế dương tại mọi khoảng cách hữu hạn, nguồn âm tạo điện thế âm. Điện thế không phụ thuộc điện tích thử dùng để định nghĩa, tương tự điện trường không phụ thuộc nguồn thử.

Với hai nguồn, điện thế là $\frac{kq_1}{r_1}+\frac{kq_2}{r_2}$. Với n nguồn:

$$
\begin{aligned}
V&=k\frac{q_1}{r_1}
+k\frac{q_2}{r_2}\\
&\quad+\cdots+k\frac{q_n}{r_n}.
\end{aligned}
$$

Với chỉ số i chạy từ 1 đến n, viết gọn thành:

$$
V=k\sum_{i=1}^{n}\frac{q_i}{r_i}.
\tag{23.15}
$$

Chỉ số i chạy qua mọi nguồn, rᵢ là khoảng cách nguồn i đến điểm khảo sát. Đây là tổng đại số với dấu của điện tích. Với nguồn liên tục, chia thành điện tích nhỏ dq rồi lấy tích phân:

$$
V=k\int_{\mathrm{src}}\frac{dq}{r}.
\tag{23.16}
$$

Khoảng cách r trong tích phân thay đổi theo vị trí phần nguồn dq, còn điểm khảo sát giữ cố định. Mốc vô hạn dùng được khi điện thế tại vô hạn có thể xác định hữu hạn. Với phân bố kéo dài vô hạn, chẳng hạn dây vô hạn, không được mặc nhiên chọn mốc ấy. Khi đó phải chọn một điểm tham chiếu hữu hạn.

Điện thế tại điểm có thể tồn tại dù không có điện tích thử đặt ở đó. Nếu đặt q₀, thế năng tương tác liên quan hạt thử là q₀V. Điện thế của nguồn và thế năng của hệ chứa hạt thử là hai đại lượng khác nhau.

### Tính điện thế từ điện trường

Khi điện trường đã biết hoặc dễ tìm bằng Gauss, có thể dùng công trên một đơn vị điện tích:

$$
\begin{aligned}
W_{a\to b}&=q_0\int_a^b\vec E\cdot d\vec\ell\\
V_a-V_b&=\int_a^b\vec E\cdot d\vec\ell\\
&=\int_a^bE_\parallel\,d\ell
\end{aligned}
\tag{23.17}
$$

Tích phân không phụ thuộc đường đi trong điện trường tĩnh. Nếu tích phân từ a đến b dương, trường sinh công dương lên điện tích thử dương, thế năng của nó giảm và Vᵦ thấp hơn Vₐ.

Thành phần dọc đường là $E_\parallel=E\cos\varphi$, với φ là góc giữa trường và dịch chuyển. Vì vậy tích phân cuối cũng chính là tích phân $\int_a^b E\cos\varphi\,d\ell$.

Với nguồn điểm dương, đi ra xa cùng chiều trường làm V giảm về không. Đi vào ngược chiều trường làm V tăng. Với nguồn âm, trường hướng vào. Đi về nguồn làm V âm hơn, tức **giảm**. Đi ra xa làm V bớt âm, tức **tăng**.

![Hình 23.12: Đi cùng chiều trường của cả nguồn dương và nguồn âm đều làm V giảm](../img/young-23/hinh-23-12.png)

Quy tắc chung là đi cùng chiều trường thì điện thế giảm, đi ngược chiều trường thì điện thế tăng. Điện tích dương có lực hướng về phía V thấp hơn, còn điện tích âm có lực về phía V cao hơn. Cả hai đều có xu hướng giảm **thế năng** của hệ khi chuyển động do lực điện.

Đổi chiều tích phân cho cách viết tương đương:

$$
V_a-V_b=-\int_b^a\vec E\cdot d\vec\ell
\tag{23.18}
$$

Dấu trừ và hai cận đều đổi. Biểu thức này có thể đọc là công lực ngoài trên mỗi coulomb khi đưa điện tích thử dương chậm từ b đến a, vì lực ngoài trên mỗi coulomb là $-\vec E$.

Hiệu điện thế có đơn vị trường nhân chiều dài, nên:

$$
1\,\mathrm{V/m}=1\,\mathrm{N/C}.
$$

Volt trên mét thường được dùng làm đơn vị trường trong thực hành.

### Ứng dụng: Điện tâm đồ

Các điện cực của điện tâm đồ, viết tắt ECG hoặc EKG, đo hiệu điện thế giữa các vùng da khác nhau, điển hình không quá 1 mV. Những hiệu ấy phản ánh khác biệt điện thế giữa các vùng tim, cho phép khảo sát hoạt động điện điều khiển co bóp tim. Ở đây đại lượng được đo là **hiệu điện thế**, không phải điện thế tuyệt đối của một vùng da.

![Điện cực điện tâm đồ đo hiệu điện thế giữa các vùng da](../img/young-23/ung-dung-dien-tam-do.png)

### Electron volt

Với hạt điện tích q đi từ b đến a, biến thiên thế năng là $U_a-U_b=q(V_a-V_b)$. Một điện tích có độ lớn e đi qua hiệu điện thế 1 V có biến thiên thế năng với độ lớn $1.602\times10^{-19}$ J. Ta gọi lượng năng lượng ấy là **một electron volt**:

$$
1\,\mathrm{eV}=1.602\times10^{-19}\,\mathrm J.
$$

Các bội meV, keV, MeV, GeV và TeV thường được dùng. Electron volt là đơn vị **năng lượng**, còn volt là đơn vị **điện thế**. Hai đơn vị không thay nhau được.

Hạt mang điện Ne có biến thiên thế năng tính bằng eV bằng N lần hiệu điện thế tính bằng V, với dấu và chiều chuyển động được xét đúng. Chẳng hạn hạt α mang +2e đi từ điểm b đến a với Vₐ − Vᵦ = 1000 V có:

$$
\begin{aligned}
\Delta U&=(2e)(1000\,\mathrm V)\\
&=3.204\times10^{-16}\,\mathrm J\\
&=2000\,\mathrm{eV}.
\end{aligned}
$$

Electron volt cũng đo mọi dạng năng lượng khác, chẳng hạn động năng. “Proton một triệu electron volt” nghĩa là proton có động năng 1 MeV, bằng $1.602\times10^{-13}$ J. Máy gia tốc LHC gần Geneva được thiết kế để gia tốc proton đến động năng 7 TeV, tức $7\times10^{12}$ eV.

### Ứng dụng: Electron năng lượng cao trong xạ trị

Một phương pháp xạ trị dùng chùm electron động năng 4–20 MeV truyền năng lượng cho mô qua va chạm với các nguyên tử. Electron trong khoảng năng lượng này đi vào mô một độ sâu cỡ vài centimét trong mô hình được mô tả, nên có ứng dụng với khối u gần bề mặt, chẳng hạn ở da hoặc môi. Ví dụ cho thấy eV và MeV diễn tả năng lượng của từng hạt, không phải điện áp của toàn thiết bị.

![Thiết bị dùng chùm hạt năng lượng cao để truyền năng lượng cho mô](../img/young-23/ung-dung-xa-tri.png)

### Ví dụ 23.3: Lực điện và hiệu điện thế

Proton mang $+e=1.602\times10^{-19}$ C đi thẳng d = 0,50 m từ a đến b trong máy gia tốc tuyến tính. Trường đều hướng a đến b có độ lớn $E=1.5\times10^7$ V/m. Tìm (a) lực, (b) công lực điện, (c) Vₐ − Vᵦ.

::: solution Chi tiết
**Xác định và thiết lập.** F = eE. Trường đều cho lực không đổi và cùng chiều đường đi. Công bằng Fd, còn hiệu điện thế bằng W/e.

$$
\begin{aligned}
F&=eE=2.4\times10^{-12}\,\mathrm N,\\
W&=Fd=1.2\times10^{-12}\,\mathrm J\\
&=7.5\,\mathrm{MeV},\\
V_a-V_b&=\frac{W}{e}\\
&=7.5\times10^6\,\mathrm V\\
&=7.5\,\mathrm{MV}.
\end{aligned}
$$

**Đánh giá.** Cũng có thể tích phân trường dọc đường: Trường không đổi, góc bằng không, nên Vₐ − Vᵦ = Ed. Trường hướng a đến b nên V giảm theo chiều chuyển động. Sự trùng giá trị 7,5 MeV và 7,5 MV ở đây gắn với điện tích proton bằng e, không phải hai đơn vị giống nhau.
:::

### Ví dụ 23.4: Điện thế do lưỡng cực

Hai nguồn +12 nC và −12 nC cách 10,0 cm. Điểm a nằm giữa, cách nguồn dương 6,0 cm và nguồn âm 4,0 cm. Điểm b ở phía ngoài nguồn dương, cách hai nguồn lần lượt 4,0 cm và 14,0 cm. Điểm c trên trung trực, cách mỗi nguồn 13,0 cm. Tìm điện thế a,b,c.

![Hình 23.13: Điểm a, b và c trong điện thế của lưỡng cực](../img/young-23/hinh-23-13.png)

::: solution Chi tiết
**Xác định và thiết lập.** Đây là cấu hình đã tính trường ở Ví dụ 21.8. Điện thế chỉ cần cộng đại số các phần kqᵢ/rᵢ, dùng mốc vô hạn.

$$
\begin{aligned}
V_a&=k\frac{12\times10^{-9}}{0.060}\\
&\quad-k\frac{12\times10^{-9}}{0.040}\\
&=-900\,\mathrm V,\\
V_b&\approx1930\,\mathrm V,\\
V_c&=0.
\end{aligned}
$$

**Đánh giá.** a gần nguồn âm hơn nên thế âm. b gần nguồn dương hơn nên thế dương. c cách hai nguồn bằng nhau, nên hai thế trái dấu bù nhau. Tính điện thế đơn giản hơn cộng hai vector trường, nhưng V_c = 0 không có nghĩa trường tại c bằng không.
:::

### Ví dụ 23.5: Điện thế và thế năng

Đặt nguồn điểm +4,0 nC ở lần lượt a,b,c của Ví dụ 23.4. Tìm phần thế năng tương tác liên quan điện tích này.

::: solution Chi tiết
**Xác định và thiết lập.** Dùng U = qV, với V do các nguồn khác tạo ra và mốc ở vô hạn.

$$
\begin{aligned}
U_a&=(4.0\times10^{-9})(-900)\\
&=-3.6\times10^{-6}\,\mathrm J,\\
U_b&\approx7.7\times10^{-6}\,\mathrm J,\\
U_c&=0.
\end{aligned}
$$

**Đánh giá.** Đưa q từ c ra vô hạn cho tổng công lực điện bằng không theo mọi đường đi vì hai đầu có cùng thế năng. Nếu chọn đi dọc trung trực lưỡng cực, lực ở mỗi điểm vuông góc đường đi, nên công từng phần dịch chuyển cũng bằng không. Với một đường khác, công từng phần có thể khác không nhưng tổng vẫn bằng không.
:::

### Ví dụ 23.6: Tìm điện thế bằng tích phân

Dùng tích phân điện trường để tìm điện thế cách nguồn điểm q một khoảng r.

![Hình 23.14: Tích phân trường theo đường xuyên tâm từ a ra vô hạn](../img/young-23/hinh-23-14.png)

::: solution Chi tiết
**Xác định và thiết lập.** Chọn a ở khoảng cách r, b ở vô hạn có Vᵦ = 0. Có thể chọn đường đi bất kỳ, nhưng đường xuyên tâm làm tích vô hướng đơn giản nhất.

**Thực hiện.** Dùng s cho biến khoảng cách trong tích phân:

$$
\begin{aligned}
V(r)&=\int_r^\infty\frac{kq}{s^2}ds\\
&=\left[-\frac{kq}{s}\right]_r^\infty\\
&=\frac{kq}{r}.
\end{aligned}
$$

**Đánh giá.** Trùng (23.14) và dùng được với cả q dương hoặc âm. Tích phân điện trường từ a đến b cho Vₐ − Vᵦ, độc lập đường đi.
:::

### Ví dụ 23.7: Chuyển động qua hiệu điện thế

Hạt bụi có $m=5.0\times10^{-9}$ kg, tức 5,0 µg, mang q₀ = +2,0 nC, bắt đầu nghỉ ở a rồi đi thẳng đến b. Hai nguồn cố định +3,0 nC và −3,0 nC cách 3,0 cm. a cách nguồn dương 1,0 cm, nguồn âm 2,0 cm. b cách nguồn dương 2,0 cm, nguồn âm 1,0 cm. Chỉ lực điện sinh công. Tìm tốc độ ở b.

![Hình 23.15: Hạt đi từ a đến b trong trường không đều của hai nguồn trái dấu](../img/young-23/hinh-23-15.png)

::: solution Chi tiết
**Xác định và thiết lập.** Gia tốc thay đổi theo vị trí nên không dùng công thức gia tốc không đổi. Bảo toàn cơ năng với U = q₀V cho:

$$
\begin{aligned}
q_0V_a&=\frac12mv^2+q_0V_b,\\
v&=\sqrt{\frac{2q_0(V_a-V_b)}m}.
\end{aligned}
$$

**Thực hiện.** Cộng hai thế nguồn cho Vₐ = +1350 V và Vᵦ = −1350 V, nên hiệu bằng 2700 V. Thay vào được v ≈ 46 m/s.

**Đánh giá.** Hạt dương nhanh lên khi ra xa nguồn dương và đến gần nguồn âm. Trong biểu thức dưới căn, q₀ nhân volt có đơn vị joule, chia m cho m²/s², nên căn có đơn vị tốc độ. Các bài biến thể của những ví dụ nằm trong phần luyện tập cuối chương.
:::

::: exercise Câu hỏi ôn lại mục 23.2
Nếu điện thế tại một điểm bằng không, điện trường tại điểm đó có buộc bằng không không? Xét điểm c ở Ví dụ 23.4 và Ví dụ 21.8.
:::

::: solution Giải thích
Không. Tại c trên trung trực lưỡng cực, hai phần điện thế trái dấu bù nhau, nhưng hai vector trường không đối nhau và tổng trường hướng +x. Điện thế liên quan công cần để đưa một đơn vị điện tích từ mốc đến điểm đó, còn trường cho lực trên đơn vị điện tích tại chính điểm đó. Một giá trị V bằng không không xác định độ biến thiên V theo vị trí.
:::
