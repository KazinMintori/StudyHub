## 30.4. Mạch R-L

Cuộn dây thông thường có điện trở dây quấn. Ngoại lệ là cuộn siêu dẫn trong miền làm việc thích hợp. Điện trở $R$ của mạch có thể là điện trở riêng mắc thêm hoặc điện trở dây quấn. Mạch chứa cả $R$ và tự cảm $L$ được gọi là **mạch RL**. Với điện áp hữu hạn, dòng cuộn không thể nhảy tức thời khi đóng hoặc chuyển mạch.

Việc phân tích mạch R-L giúp ta hiểu rõ quy luật biến thiên của dòng điện theo thời gian và hằng số thời gian của mạch. Đồng thời, phân tích này làm sáng tỏ sự phân bổ năng lượng giữa công suất phát của nguồn, nhiệt lượng tỏa ra trên điện trở và năng lượng tích lũy trong từ trường của cuộn cảm.

---

### Cách phân tích mạch có cuộn cảm

Điện áp, dòng và điện tích có thể biến thiên theo thời gian, nhưng các định luật Kirchhoff vẫn áp dụng tại từng thời điểm trong mô hình mạch tập trung. Quy trình phân tích gồm các bước sau:

1. Vẽ sơ đồ, đặt tên các đại lượng đã biết và chưa biết. Dùng định luật nút sớm để giảm số dòng độc lập.
2. Xác định đại lượng cần tìm và điều kiện đầu, đặc biệt dòng qua từng cuộn ngay trước chuyển mạch.
3. Chọn chiều vòng và viết định luật vòng. Khi đi qua cuộn theo chiều dòng giả định, số hạng điện áp trong tổng biến thiên thế là $-L\,di/dt$. Đi ngược chiều đó cho số hạng $+L\,di/dt$.
4. Giải phương trình cho các đại lượng đích. Dùng định luật Lenz và các giới hạn đầu, cuối để xét chiều điện áp cuộn có chống biến thiên dòng hay không.

### Dòng tăng sau khi đóng nguồn

Xét mạch điện ở Hình 30.11. Mạch gồm một nguồn điện có suất điện động $\mathcal E$ và điện trở trong không đáng kể, nối với một điện trở $R$, một cuộn cảm $L$ và hai công tắc $S_1, S_2$. Ban đầu cả hai công tắc đều mở và dòng điện trong mạch bằng không.

![Hình 30.11: Sơ đồ mạch điện R-L với hai công tắc cho phép khảo sát quá trình tăng và giảm của dòng điện.](../img/young-30/hinh-30-11.png)

Tại thời điểm $t = 0$, ta đóng công tắc $S_1$ trong khi công tắc $S_2$ vẫn mở. Nhánh chứa nguồn, điện trở và cuộn cảm tạo thành một mạch kín. Dòng điện bắt đầu tăng từ giá trị không. Khi dòng điện tăng, từ thông qua cuộn cảm biến thiên, làm xuất hiện suất điện động tự cảm $\mathcal E_L = -L(di/dt)$. Theo định luật Lenz, suất điện động này có chiều chống lại sự tăng của dòng điện.

Để tìm dòng $i(t)$, áp dụng quy tắc vòng Kirchhoff. Xuất phát từ cực âm nguồn và đi ngược chiều kim đồng hồ theo vòng có dòng được đánh dấu trong Hình 30.11:
1. Đi qua nguồn từ cực âm sang cực dương: Điện thế tăng một lượng $+\mathcal E$.
2. Đi qua điện trở $R$ theo chiều dòng điện: Điện thế giảm một lượng $-iR$.
3. Đi qua cuộn cảm $L$ theo chiều dòng điện đang tăng: Suất điện động tự cảm có chiều ngược chiều dòng điện, làm điện thế giảm một lượng $-L(di/dt)$.

Tổng các độ biến thiên điện thế quanh vòng kín bằng không:

$$
\mathcal E - iR - L\frac{di}{dt} = 0 \tag{30.12}
$$

Phương trình (30.12) là phương trình vi phân cơ bản mô tả sự tăng dòng điện trong mạch R-L. Tại thời điểm ban đầu $t = 0$, dòng điện chưa kịp xuất hiện nên $i = 0$. Khi đó độ giảm thế trên điện trở bằng không, và toàn bộ suất điện động của nguồn đặt lên cuộn cảm:

$$
\left(\frac{di}{dt}\right)_{t=0} = \frac{\mathcal E}{L}
$$

Tốc độ tăng dòng ban đầu hoàn toàn do suất điện động $\mathcal E$ và độ tự cảm $L$ quyết định. Nếu cuộn cảm có độ tự cảm $L$ rất lớn, tốc độ tăng dòng ban đầu sẽ rất nhỏ.

Khi dòng điện $i$ tăng dần, số hạng $iR$ lớn lên, khiến hiệu điện thế đặt vào hai đầu cuộn cảm giảm đi. Do đó, tốc độ tăng dòng $di/dt$ giảm dần theo thời gian:

$$
\frac{di}{dt} = \frac{\mathcal E - iR}{L} = \frac{\mathcal E}{L} - \frac{R}{L}i \tag{30.13}
$$

Sau một thời gian đủ dài, dòng điện đạt trạng thái dừng ổn định. Khi dòng điện không còn biến thiên, tốc độ tăng dòng bằng không ($di/dt = 0$). Từ phương trình (30.13), ta tìm được cường độ dòng điện cực đại ổn định trong mạch:

$$
I = \frac{\mathcal E}{R}
$$

Lúc này cuộn cảm hoạt động như một dây dẫn thuần túy (với điện trở bằng không), và dòng điện hoàn toàn bị giới hạn bởi điện trở $R$.

![Hình 30.12: Mạch khi đóng S1 và đồ thị dòng điện tăng dần đến giá trị ổn định.](../img/young-30/hinh-30-12.png)

Để tìm biểu thức chính xác của $i(t)$, ta biến đổi phương trình vi phân (30.13) bằng cách tách biến:

$$
\frac{di}{i - (\mathcal E/R)} = -\frac{R}{L}dt
$$

Lấy tích phân hai vế từ thời điểm ban đầu $t' = 0$ (khi $i' = 0$) đến thời điểm $t$ (khi dòng điện đạt giá trị $i$):

$$
\begin{aligned}
\int_0^i \frac{di'}{i' - (\mathcal E/R)} &= -\frac{R}{L}\int_0^t dt' \\
&= -\frac{R}{L}t
\end{aligned}
$$

Thực hiện tích phân ở vế trái:

$$
\begin{aligned}
\ln \frac{i - \mathcal E/R}{-\mathcal E/R} &= \ln\left(1 - \frac{iR}{\mathcal E}\right) \\
&= -\frac{R}{L}t
\end{aligned}
$$

Lấy hàm mũ hai vế của phương trình:

$$
1 - \frac{iR}{\mathcal E} = e^{-(R/L)t}
$$

Từ đó, ta giải ra cường độ dòng điện $i$ tại thời điểm $t$:

$$
\begin{aligned}
i(t) &= \frac{\mathcal E}{R}\left(1 - e^{-(R/L)t}\right) \\
&= I\left(1 - e^{-(R/L)t}\right)
\end{aligned} \tag{30.14}
$$

Đạo hàm phương trình (30.14) theo thời gian cho ta tốc độ tăng dòng điện tại mọi thời điểm:

$$
\frac{di}{dt} = \frac{\mathcal E}{L}e^{-(R/L)t} \tag{30.15}
$$

Quan sát phương trình (30.15), ta thấy tại $t = 0$, $di/dt = \mathcal E/L$, còn khi $t \to \infty$, $di/dt \to 0$, hoàn toàn phù hợp với các phân tích định tính trước đó.

---

### Hằng số thời gian của mạch R-L

Trong phương trình (30.14) và (30.15), đại lượng $L/R$ có thứ nguyên của thời gian. Ta định nghĩa **hằng số thời gian** của mạch R-L là:

$$
\tau = \frac{L}{R} \tag{30.16}
$$

Ta có thể kiểm tra thứ nguyên của $\tau$: Vì đơn vị của độ tự cảm là henry ($1\text{ H} = 1\ \Omega\cdot\text{s}$), nên đơn vị của $L/R$ là $(\Omega\cdot\text{s})/\Omega = \text{s}$ (giây).

Ý nghĩa vật lý của hằng số thời gian $\tau$ trong phương trình (30.16):
- Sau khoảng thời gian $t = \tau$, dòng điện trong mạch đạt giá trị:

  $$
\begin{aligned}
i(\tau) &= I(1 - e^{-1}) \\
&\approx I(1 - 0{,}368) \\
&= 0{,}632 I
\end{aligned}
$$

  Tức là dòng điện tăng đến khoảng $63{,}2\%$ giá trị cực đại cuối cùng.
- Sau khoảng thời gian $t = 2\tau$, dòng điện đạt $I(1 - e^{-2}) \approx 86{,}5\% I$.
- Sau khoảng thời gian $t = 5\tau$, dòng điện đạt $I(1 - e^{-5}) \approx 99{,}3\% I$, xem như đã đạt đến giá trị dừng ổn định.

Sau $10\tau$, dòng đạt khoảng 99,995% giá trị cuối. Với cùng điện trở $R=100\,\Omega$, tự cảm $L=10\,\mathrm H$ cho $\tau=0{,}10\,\mathrm s$. Nếu giảm tự cảm xuống $0{,}010\,\mathrm H$ thì $\tau=0{,}10\,\mathrm{ms}$, nên dòng tiến đến trạng thái ổn định nhanh hơn nhiều.

Nếu điện trở $R$ rất lớn, hằng số thời gian $\tau = L/R$ sẽ rất nhỏ, dòng điện tăng lên giá trị cực đại rất nhanh. Ngược lại, nếu độ tự cảm $L$ lớn, thời gian cần thiết để dòng điện đạt trạng thái ổn định sẽ dài hơn.

::: tip Lưu ý quan trọng: Dòng điện qua cuộn cảm không thể biến thiên đột ngột
Cường độ dòng điện $i$ qua cuộn cảm luôn là một hàm liên tục theo thời gian, không bao giờ có thể nhảy bậc tức thời. Nếu dòng điện thay đổi đột ngột trong thời gian $dt \to 0$, tốc độ $di/dt$ sẽ tiến tới vô cùng, dẫn đến suất điện động tự cảm lớn vô hạn, điều này không thể xảy ra trong thực tế. Trái lại, đạo hàm $di/dt$ hoàn toàn có thể biến đổi gián đoạn khi ta đóng hoặc ngắt các khóa chuyển mạch.
:::

---

### Cân bằng năng lượng khi dòng điện tăng

Ta có thể hiểu sâu hơn bản chất vật lý của mạch R-L thông qua định luật bảo toàn năng lượng. Nhân cả hai vế của phương trình vòng Kirchhoff (30.12) với cường độ dòng điện tức thời $i$:

$$
\mathcal E i = i^2 R + Li\frac{di}{dt} \tag{30.17}
$$

Phương trình (30.17) biểu diễn sự cân bằng công suất tại mỗi thời điểm trong mạch:
- Số hạng $\mathcal E i$: Là công suất tức thời do nguồn điện cung cấp cho mạch.
- Số hạng $i^2 R$: Là tốc độ tỏa nhiệt Joule trên điện trở $R$.
- Số hạng $Li(di/dt)$: Là tốc độ tích lũy năng lượng từ trường trong cuộn cảm, bởi vì:
  $$
  \frac{d}{dt}\left(\frac{1}{2}Li^2\right) = Li\frac{di}{dt}
  $$

Như vậy, toàn bộ năng lượng mà nguồn điện cung cấp không bị tiêu tán hoàn toàn thành nhiệt, mà một phần được chuyển hóa và tích trữ dưới dạng năng lượng từ trường trong lòng cuộn cảm. Khi dòng điện đạt giá trị cực đại $I$, tốc độ $di/dt = 0$, toàn bộ công suất của nguồn lúc này chuyển thành nhiệt tỏa ra trên điện trở.

---

### Sự giảm dòng điện trong mạch R-L

Bây giờ, giả sử công tắc $S_1$ trong Hình 30.11 đã được đóng trong một thời gian dài, dòng điện qua điện trở và cuộn cảm đã đạt giá trị ổn định $I_0 = \mathcal E/R$. Năng lượng tích trữ trong cuộn cảm tại thời điểm này là $U_0 = \frac{1}{2}LI_0^2$.

Tại thời điểm ta chọn làm mốc $t = 0$, ta đóng công tắc $S_2$ để tạo một mạch vòng kín nối tắt qua cuộn cảm và điện trở, đồng thời mở công tắc $S_1$ để ngắt nguồn điện ra khỏi mạch.

![Hình 30.13: Đồ thị cường độ dòng điện i theo thời gian trong quá trình dòng điện suy giảm qua điện trở và cuộn cảm.](../img/young-30/hinh-30-13.png)

Dòng điện qua mạch không lập tức giảm về không. Khi dòng điện bắt đầu giảm, tốc độ $di/dt$ mang dấu âm, cuộn cảm phát sinh suất điện động tự cảm cùng chiều với dòng điện cũ nhằm duy trì dòng điện chạy qua nó.

Áp dụng quy tắc vòng Kirchhoff cho mạch kín gồm $R$ và $L$ (không còn nguồn $\mathcal E$):

$$
-iR - L\frac{di}{dt} = 0
$$

Biến đổi và tách biến:

$$
\frac{di}{i} = -\frac{R}{L}dt
$$

Lấy tích phân hai vế từ $t' = 0$ (khi $i' = I_0$) đến thời điểm $t$ (khi dòng điện là $i$):

$$
\int_{I_0}^i \frac{di'}{i'} = -\frac{R}{L}\int_0^t dt'
$$

$$
\ln\left(\frac{i}{I_0}\right) = -\frac{R}{L}t
$$

Lấy hàm mũ hai vế, ta nhận được quy luật suy giảm dòng điện:

$$
i(t) = I_0 e^{-(R/L)t} = I_0 e^{-t/\tau} \tag{30.18}
$$

Trong đó $\tau = L/R$ vẫn là hằng số thời gian của mạch. Sau một khoảng thời gian bằng $\tau$, dòng điện giảm xuống còn $1/e \approx 36{,}8\%$ giá trị ban đầu $I_0$. Sau $2\tau$, dòng điện còn $13{,}5\%$, sau $5\tau$ còn $0{,}67\%$, và sau $10\tau$ chỉ còn $0{,}0045\% I_0$.

Để khảo sát năng lượng trong quá trình suy giảm dòng, ta nhân phương trình vi phân với $i$:

$$
0 = i^2 R + Li\frac{di}{dt} \tag{30.19}
$$

Vì dòng điện đang giảm nên $di/dt < 0$, kéo theo số hạng $Li(di/dt) = \frac{d}{dt}(\frac{1}{2}Li^2)$ mang dấu âm. Phương trình (30.19) khẳng định rằng: Năng lượng từ trường dự trữ trong cuộn cảm giảm đi với tốc độ chính bằng tốc độ tỏa nhiệt $i^2 R$ trên điện trở. Toàn bộ năng lượng từ trường ban đầu $U_0 = \frac{1}{2}LI_0^2$ cuối cùng được giải phóng hoàn toàn thành nhiệt năng trên điện trở $R$.

Có thể so sánh các đồ thị này với quá trình nạp, phóng tụ trong mạch RC ở chương 26. Cả hai đều tiến đến trạng thái cuối theo hàm mũ, nhưng hằng số thời gian của RC là $RC$, còn của RL là $L/R$.

---

### Các ví dụ minh họa và câu hỏi tự kiểm

::: example Ví dụ 30.6: Phân tích sự tăng dòng trong mạch R-L
Một thiết bị điện tử nhạy cảm có điện trở $R = 175\ \Omega$ cần được nối với một nguồn suất điện động có điện trở trong không đáng kể thông qua một công tắc. Thiết bị được thiết kế để hoạt động ổn định ở dòng điện $36\text{ mA}$. Tuy nhiên, để tránh làm hỏng các linh kiện vi mạch bên trong, dòng điện qua thiết bị trong $58\ \mu\text{s}$ đầu tiên sau khi đóng công tắc không được vượt quá $4{,}9\text{ mA}$. Do đó, người ta mắc nối tiếp thiết bị với một cuộn cảm như trong sơ đồ Hình 30.11, trong đó công tắc được đóng là $S_1$.
1. Cần chọn nguồn có suất điện động $\mathcal E$ bằng bao nhiêu?
2. Cần chọn cuộn cảm có độ tự cảm $L$ bằng bao nhiêu để thỏa mãn yêu cầu khống chế dòng ban đầu?
3. Tính hằng số thời gian $\tau$ của mạch R-L này.

**Nhận dạng và chuẩn bị:**
Bài toán khảo sát quá trình tăng dòng điện trong mạch R-L. Cường độ dòng điện cuối cùng ở trạng thái ổn định là $I = \mathcal E/R$. Với $R = 175\ \Omega$ và yêu cầu $I = 36\text{ mA} = 0{,}036\text{ A}$, ta xác định được suất điện động $\mathcal E$. Để thỏa mãn điều kiện $i \le 4{,}9\text{ mA}$ tại $t = 58\ \mu\text{s} = 58 \times 10^{-6}\text{ s}$, ta sử dụng phương trình tăng dòng (30.14) để tìm ẩn số duy nhất là độ tự cảm $L$. Sau đó tính hằng số thời gian $\tau = L/R$.

**Lời giải:**
1. Khi dòng điện đã đạt trạng thái ổn định, cuộn cảm không còn cản trở dòng điện:

   $$
\begin{aligned}
\mathcal E &= IR \\
&= (0{,}036\text{ A})(175\ \Omega) \\
&= 6{,}3\text{ V}
\end{aligned}
$$

2. Từ phương trình tăng dòng $i = (\mathcal E/R)(1 - e^{-(R/L)t})$, ta biến đổi để giải $L$:

   $$
   1 - \frac{iR}{\mathcal E} = e^{-(R/L)t}
   $$

   Lấy logarit tự nhiên hai vế:

   $$
\begin{aligned}
\ln &\left(1 - \frac{iR}{\mathcal E}\right) = -\frac{Rt}{L} \\
L &= \frac{-Rt}{\ln(1 - iR/\mathcal E)}
\end{aligned}
$$

   Thay các giá trị số vào biểu thức:
   $$
\begin{aligned}
1 - \frac{iR}{\mathcal E} &= 1 - \frac{0{,}8575\text{ V}}{6{,}3\text{ V}} \\
&= 1 - 0{,}13611 \\
&= 0{,}86389
\end{aligned}
$$

   Từ đó tính được độ tự cảm $L$:
   $$
\begin{aligned}
L &= \frac{-(175\ \Omega)(58\ \mu\text{s})}{\ln(0{,}86389)} \\
&= \frac{-0{,}01015}{-0{,}14631} \\
&\approx 0{,}06937\text{ H} \\
&\approx 69\text{ mH}
\end{aligned}
$$

Giá trị vừa tính là tự cảm nhỏ nhất để dòng không vượt ngưỡng ở thời điểm yêu cầu. Một tự cảm lớn hơn cũng làm dòng tăng chậm hơn nếu các tham số khác giữ nguyên.

3. Dùng tự cảm đã làm tròn $69\,\mathrm{mH}$, hằng số thời gian là:

   $$
\begin{aligned}
\tau &= \frac{L}{R} \\
&= \frac{69 \times 10^{-3}\text{ H}}{175\ \Omega} \\
&\approx 3{,}9 \times 10^{-4}\text{ s} = 390\ \mu\text{s}
\end{aligned}
$$

**Đánh giá:**
Khoảng thời gian $58\ \mu\text{s}$ nhỏ hơn nhiều so với hằng số thời gian $\tau = 390\ \mu\text{s}$. Trong $58\ \mu\text{s}$, dòng điện chỉ tăng từ 0 lên $4{,}9\text{ mA}$, chiếm một phần nhỏ so với dòng ổn định $36\text{ mA}$. Sau một hằng số thời gian $\tau = 390\ \mu\text{s}$, dòng điện đạt khoảng $(1 - 1/e)I \approx 0{,}632 \times 36\text{ mA} = 23\text{ mA}$. Cuộn cảm đóng vai trò làm chậm tốc độ tăng của dòng điện trong mạch, bảo vệ các linh kiện nhạy cảm.
:::

---

::: example Ví dụ 30.7: Năng lượng trong mạch RL
Khi dòng trong mạch RL đang suy giảm, sau 2,3 hằng số thời gian, bao nhiêu phần năng lượng từ trường ban đầu đã bị tiêu tán trên điện trở?

**Nhận dạng và chuẩn bị:**
Dòng suy giảm theo (30.18), còn năng lượng cuộn tỉ lệ với bình phương dòng. Vì vậy cần tính năng lượng còn lại, rồi lấy năng lượng đầu trừ phần ấy.

**Lời giải:**
Với $\tau=L/R$,

$$
\begin{aligned}
i(t) &= I_0e^{-t/\tau}, \\
U(t) &= \frac12Li(t)^2 \\
&= U_0e^{-2t/\tau}, \\
U_0 &= \frac12LI_0^2.
\end{aligned}
$$

Tại $t=2{,}3\tau$,

$$
\begin{aligned}
\frac{U(t)}{U_0} &= e^{-4{,}6} \\
&\approx 0{,}010, \\
\frac{U_{\mathrm{diss}}}{U_0} &= 1-e^{-4{,}6} \\
&\approx 0{,}990.
\end{aligned}
$$

Khoảng 1,0% năng lượng còn ở cuộn và 99,0% đã chuyển thành nhiệt trên điện trở.

**Đánh giá:**
Dùng các giá trị làm tròn của Ví dụ 30.6, $L=69\,\mathrm{mH}$, $I_0=36\,\mathrm{mA}$ và $\tau\approx390\,\mu\mathrm s$:

$$
\begin{aligned}
U_0 &= \frac12LI_0^2 \\
&\approx 4{,}5\times10^{-5}\,\mathrm J, \\
U_{\mathrm{diss}} &\approx 0{,}990U_0 \\
&\approx 4{,}4\times10^{-5}\,\mathrm J, \\
t &= 2{,}3\tau \\
&\approx 0{,}90\,\mathrm{ms}.
\end{aligned}
$$

Mạch có thể chuyển đến trạng thái gần tắt trong thời gian chưa đến 1 ms. Ước lượng một chu trình bật–tắt gồm hai giai đoạn tương tự cho khoảng 1,8 ms. Các mạng chuyển mạch viễn thông tốc độ cao cần thời gian ngắn hơn, nên cần hằng số thời gian nhỏ hơn. Ngưỡng được gọi là gần bật hoặc gần tắt phải gắn với yêu cầu cụ thể của mạch.

Cuộn cảm làm dòng giảm dần sau khi tách nguồn. Trong giai đoạn đó, năng lượng từ trường được giải phóng thành nhiệt trên điện trở.
:::

---

::: exercise Câu hỏi tự kiểm 30.4
Xét mạch điện R-L ở Hình 30.11:
1. Khi công tắc $S_1$ đóng và công tắc $S_2$ mở, dấu đại số của các hiệu điện thế $v_{ab}$ và $v_{bc}$ là gì?
   - (i) $v_{ab} > 0, v_{bc} > 0$.
   - (ii) $v_{ab} > 0, v_{bc} < 0$.
   - (iii) $v_{ab} < 0, v_{bc} > 0$.
   - (iv) $v_{ab} < 0, v_{bc} < 0$.
2. Khi công tắc $S_1$ mở, công tắc $S_2$ đóng và dòng điện đang chạy theo chiều mũi tên trong hình, dấu đại số của $v_{ab}$ và $v_{bc}$ là gì?
   - (i) $v_{ab} > 0, v_{bc} > 0$.
   - (ii) $v_{ab} > 0, v_{bc} < 0$.
   - (iii) $v_{ab} < 0, v_{bc} > 0$.
   - (iv) $v_{ab} < 0, v_{bc} < 0$.

<details>
<summary>Đáp án và giải thích</summary>

**Đáp án:**
1. Lựa chọn (i): $v_{ab} > 0, v_{bc} > 0$.
2. Lựa chọn (ii): $v_{ab} > 0, v_{bc} < 0$.

**Giải thích chi tiết:**
Hiệu điện thế $v_{ab}$ được định nghĩa là điện thế tại điểm $a$ trừ điện thế tại điểm $b$ ($v_{ab} = v_a - v_b$), và tương tự $v_{bc} = v_b - v_c$.
- Trong cả hai trường hợp, dòng điện đều chạy qua điện trở từ điểm $a$ sang điểm $b$. Theo định luật Ohm, dòng điện luôn đi từ nơi có điện thế cao sang nơi có điện thế thấp, do đó $v_a > v_b$, nghĩa là $v_{ab} = iR > 0$ trong cả hai trường hợp.
- Khi $S_1$ đóng và $S_2$ mở: Dòng điện qua cuộn cảm đi từ $b$ sang $c$ và đang tăng ($di/dt > 0$). Suất điện động tự cảm chống lại sự tăng này nên hướng từ $c$ về $b$, làm cho đầu $b$ có điện thế cao hơn đầu $c$ ($v_b > v_c$). Vì vậy $v_{bc} > 0$.
- Khi $S_1$ mở và $S_2$ đóng: Dòng điện qua cuộn cảm vẫn đi từ $b$ sang $c$ nhưng đang giảm dần ($di/dt < 0$). Suất điện động tự cảm có xu hướng duy trì dòng điện cũ nên hướng từ $b$ sang $c$, làm cho đầu $c$ có điện thế cao hơn đầu $b$ ($v_c > v_b$). Vì vậy $v_{bc} < 0$.
</details>
:::
