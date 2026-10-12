<!-- Source: Section23.3, printed760–764, PDF780–784. -->

## 23.3. Tính điện thế

Có hai đường tính điện thế. Nếu biết phân bố nguồn, cộng các phần kq/r hoặc tích phân kdq/r. Nếu biết trường theo vị trí, tích phân trường giữa điểm khảo sát và một điểm tham chiếu. Một bài có thể cần kết hợp cả hai.

### Quy trình tính

1. Vẽ vị trí, độ lớn và dấu các nguồn, cùng hệ tọa độ. Nguồn có thể rời rạc hoặc liên tục.
2. Đánh dấu điểm cần tìm V. Có thể giữ tọa độ tổng quát để thu được một hàm điện thế.
3. Với nguồn điểm, cộng đại số các thế. Với nguồn liên tục, chọn phần tử điện tích và cận tích phân phủ toàn nguồn.
4. Nếu tích phân trường dễ hơn, chọn điểm tham chiếu b và dùng Vₐ − Vᵦ. Mốc vô hạn thường dùng cho hệ nguồn hữu hạn, còn nguồn kéo dài vô hạn có thể cần mốc hữu hạn.
5. Điện thế là vô hướng, nhưng tích phân trường vẫn cần tích vô hướng của trường với dịch chuyển. Không được bỏ hướng của hai vector trong bước ấy.
6. Xét đơn vị, dấu, giới hạn xa nguồn và đồ thị theo vị trí. Đi theo chiều trường phải làm điện thế giảm.

So với việc tính riêng các thành phần trường, tính điện thế thường đơn giản hơn. Phương pháp năng lượng và phương pháp lực đều dùng được, nhưng dữ kiện và đại lượng cần tìm quyết định cách thuận tiện.

### Ví dụ 23.8: Cầu dẫn tích điện

Cầu dẫn đặc bán kính R mang tổng điện tích q. Tìm điện thế trong và ngoài cầu.

::: solution Chi tiết
**Xác định và thiết lập.** Ví dụ 22.5 đã cho trường. Ngoài cầu, trường giống nguồn điểm q ở tâm. Trong vật liệu dẫn, trường bằng không. Chọn V = 0 ở vô hạn.

**Thực hiện.** Ngoài cầu và trên mặt:

$$
\begin{aligned}
V(r)&=\frac{kq}{r},\quad r\ge R,\\
V(R)&=\frac{kq}{R}.
\end{aligned}
$$

Trong cầu, tích phân trường giữa hai điểm bất kỳ bằng không, nên hiệu điện thế giữa chúng bằng không. Điện thế toàn cầu bằng giá trị ở mặt:

$$
V(r)=\frac{kq}{R},\quad r<R.
$$

**Đánh giá.** Với q dương, V là hằng số dương trong cầu rồi giảm theo 1/r ngoài cầu, liên tục tại R. Trường bằng không bên trong nhưng V không buộc bằng không. Trường ngoài giảm theo 1/r² và nhảy tại mặt. Các bài biến thể nằm trong phần cuối chương.
:::

![Hình 23.16: Trường bằng không và điện thế không đổi trong cầu dẫn](../img/young-23/hinh-23-16.png)

### Ion hóa và phóng điện vầng quang

Điện thế cao nhất đạt được của vật dẫn trong không khí bị giới hạn bởi sự ion hóa. Trong mô hình gần đúng này, không khí trở nên dẫn điện khi trường đạt cỡ $3\times10^6$ V/m, gọi là độ bền điện môi của không khí.

Với cầu dẫn dương, điện thế mặt $V_s=\frac{kq}{R}$ và trường mặt $E_s=\frac{kq}{R^2}$, nên $V_s=RE_s$. Nếu E_m là ngưỡng ion hóa, điện thế mặt giới hạn là:

$$
V_m=RE_m.
$$

Cầu bán kính 1 cm cho điện thế giới hạn xấp xỉ 30.000 V. Nạp thêm điện tích sẽ ion hóa không khí và làm phần điện tích bổ sung rò ra. Cầu bán kính 2 m có thể đạt cỡ 6 MV trong cùng mô hình. Vì vậy máy Van de Graaff dùng cực cầu bán kính lớn để đạt điện thế cao.

Ở đầu nhọn hoặc dây rất mảnh, bán kính cong nhỏ làm trường ngay ngoài mặt lớn dù điện thế chưa rất cao. Dòng điện và ánh sáng yếu đi kèm ion hóa cục bộ được gọi là **phóng điện vầng quang**, hay corona. Dây mảnh trong máy in laser và máy photocopy dùng hiện tượng này để phun điện tích lên trống tạo ảnh.

Khi muốn hạn chế vầng quang, có thể dùng bề mặt có bán kính cong lớn. Đầu tròn của cột thu sét cho phép tích lũy điện tích trước khi rò mạnh ra không khí. Khi khí quyển có điện tích dư trong giông, điện tích trái dấu có thể tập trung trên đầu cột. Đường dẫn kim loại nối xuống đất đưa điện tích của phóng điện đi qua cột. Cột kim loại trên đỉnh Empire State Building là một minh họa được dùng cho hiện tượng này, với mức tới khoảng 500 lần sét đánh mỗi năm trong hệ dữ kiện đang xét.

![Hình 23.17: Cột kim loại trên đỉnh Empire State Building nhận phóng điện sét](../img/young-23/hinh-23-17.png)

### Ví dụ 23.9: Hai bản song song trái dấu

Tìm điện thế ở độ cao y giữa hai bản song song đã xét ở mục 23.1. Trường đều hướng xuống, bản dưới chọn y = 0 và U = 0.

![Hình 23.18: Hai bản song song với bản dưới chọn y = 0](../img/young-23/hinh-23-18.png)

::: solution Chi tiết
**Xác định và thiết lập.** Từ U = q₀Ey và V = U/q₀, suy ra V theo y.

$$
\begin{aligned}
V(y)&=Ey,\\
V_a-V_b&=Ed,\\
E&=\frac{V_a-V_b}{d}.
\end{aligned}
$$

Điện thế giảm tuyến tính khi đi xuống cùng chiều trường. Khi hiệu điện thế giữ nguyên, hai bản gần nhau hơn cho trường lớn hơn.

**Đánh giá.** Tại bản dưới V = 0 nhưng bản vẫn mang mật độ điện tích −σ. Mốc điện thế bằng không được chọn tùy ý, không có nghĩa vật tại mốc phải trung hòa. Quan hệ $E = \frac{V_{ab}}{d}$ dùng ở trường đều của cấu hình phẳng này, không tự áp dụng cho hai cầu hoặc hai trụ đồng tâm có trường biến thiên.
:::

Trở lại câu hỏi hàn hồ quang, khi hiệu điện thế được giữ, khoảng cách nhỏ làm trường giữa dụng cụ và kim loại lớn hơn. Chọn (iii) trong mô hình của câu hỏi.

### Ví dụ 23.10: Dây dài và trụ dẫn dài

Tìm điện thế cách một dây rất dài có mật độ điện tích λ một khoảng r.

![Hình 23.19: Trường xuyên tâm ngoài dây dài và trụ dẫn dài](../img/young-23/hinh-23-19.png)

::: solution Chi tiết
**Xác định và thiết lập.** Trường chỉ có thành phần xuyên tâm $E_r=\frac{\lambda}{2\pi\varepsilon_0r}$. Tích phân theo đường xuyên tâm giữa hai khoảng cách rₐ,rᵦ:

$$
\begin{aligned}
V_a-V_b&=\frac{\lambda}{2\pi\varepsilon_0}
\int_{r_a}^{r_b}\frac{dr}{r}\\
&=\frac{\lambda}{2\pi\varepsilon_0}\ln\frac{r_b}{r_a}.
\end{aligned}
$$

Nếu đặt rᵦ ở vô hạn và Vᵦ = 0, logarit không hữu hạn. Do nguồn kéo dài vô hạn, mốc ấy không cho một điện thế hữu dụng. Chọn r₀ hữu hạn có V(r₀) = 0:

$$
V(r)=\frac{\lambda}{2\pi\varepsilon_0}\ln\frac{r_0}{r}.
$$

Với λ dương, r tăng làm V giảm, đúng chiều trường. Nếu là trụ dẫn dài bán kính R, cùng biểu thức dùng được **ngoài trụ**. Chọn r₀ = R thì V trên mặt bằng không, điện thế trong vật liệu dẫn cũng bằng không. Không kéo nhánh logarit vào vùng trong trụ dẫn.
:::

### Ví dụ 23.11: Vòng tích điện

Điện tích Q phân bố đều trên vòng mảnh bán kính a. Tìm điện thế tại P trên trục vòng, cách tâm x.

![Hình 23.20: Mọi phần điện tích vòng cách điểm trên trục cùng một khoảng](../img/young-23/hinh-23-20.png)

::: solution Chi tiết
**Xác định và thiết lập.** Chia vòng thành dq. Mọi phần nguồn cách P cùng khoảng $r=\sqrt{x^2+a^2}$, nên hệ số 1/r không thay đổi trong tích phân.

$$
\begin{aligned}
V(x)&=\frac{k}{\sqrt{x^2+a^2}}\int dq\\
&=\frac{kQ}{\sqrt{x^2+a^2}}.
\end{aligned}
$$

**Đánh giá.** Khi |x| lớn hơn nhiều a, điện thế gần kQ/|x| của nguồn điểm Q. Trên trục còn có thể tích phân trường đã tìm ở Ví dụ 21.9 để nhận cùng kết quả. Lợi ích của tính điện thế ở đây là không cần chiếu từng vector trường.
:::

### Ví dụ 23.12: Đoạn dây tích điện

Điện tích dương Q đều trên đoạn dài 2a dọc trục y, từ −a đến +a. Tìm điện thế tại P trên trục x, cách gốc x > 0.

![Hình 23.21: Phần tử dy của đoạn dây và khoảng cách đến P](../img/young-23/hinh-23-21.png)

::: solution Chi tiết
**Xác định và thiết lập.** Phần đoạn dy mang $dq=(Q/(2a))dy$. Khoảng cách đến P là $\sqrt{x^2+y^2}$, không giống nhau với mọi phần như vòng ở Ví dụ 23.11.

$$
\begin{aligned}
dV&=\frac{kQ}{2a}\frac{dy}{\sqrt{x^2+y^2}},\\
V(x)&=\frac{kQ}{2a}\int_{-a}^{a}
\frac{dy}{\sqrt{x^2+y^2}}.
\end{aligned}
$$

Nguyên hàm là $\ln(y+\sqrt{x^2+y^2})$ khi x > 0. Thay hai cận:

$$
V(x)=\frac{kQ}{2a}
\ln\frac{\sqrt{x^2+a^2}+a}{\sqrt{x^2+a^2}-a}.
$$

**Đánh giá.** Khi x tiến ra vô hạn, tỷ số trong logarit tiến về 1 nên V tiến về không, đúng mốc đã chọn. Đối xứng của nguồn giúp xét giới hạn, nhưng vẫn phải tích phân các khoảng cách khác nhau.
:::

::: exercise Câu hỏi sau Ví dụ 23.12
Dùng trường trên trục x đã tìm ở Ví dụ 21.10 để tính lại điện thế đoạn dây bằng tích phân trường từ P ra vô hạn.
:::

::: exercise Câu hỏi ôn lại mục 23.3
Nếu trường tại một điểm bằng không, điện thế tại đó có buộc bằng không không? Xét tâm vòng ở Ví dụ 23.11 và Ví dụ 21.9.
:::

::: solution Giải thích
Không. Ở tâm vòng, các vector trường bù nhau nhưng các phần điện thế cùng dấu cộng lại. Với mốc ở vô hạn, V(0) = kQ/a, khác không nếu Q khác không. Điện thế ấy liên quan công ngoài cần để đưa một điện tích dương từ vô hạn đến tâm vòng dương, dù lực cuối cùng tại tâm bằng không.
:::
