## Bài toán tổng hợp 30.61–30.68

::: exercise 30.61
Trong Hình P30.61, $\mathcal E=60{,}0\,\mathrm V$, $R_1=40{,}0\,\Omega$, $R_2=25{,}0\,\Omega$, $L=0{,}300\,\mathrm H$. Đóng $S$ tại $t=0$.

Ngay sau đóng, tìm (a) $v_{ab}$ trên $R_1$, (b) đầu cao thế hơn giữa $a,b$, (c) $v_{cd}$ trên cuộn, (d) đầu cao thế hơn giữa $c,d$.

Giữ công tắc đóng rất lâu rồi mở. Ngay sau mở, tìm (e) $v_{ab}$, (f) đầu cao thế hơn giữa $a,b$, (g) $v_{cd}$, (h) đầu cao thế hơn giữa $c,d$.

![Hình P30.61: Nhánh R1 song song với nhánh R2 nối tiếp cuộn cảm, được cấp bởi nguồn qua công tắc.](img/young-30/hinh-p30-61.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện áp có dấu là $v_{ab}=V_a-V_b$ và $v_{cd}=V_c-V_d$. Chọn dòng cuộn dương từ $c$ đến $d$.

**Hướng đi:**

- Ngay sau đóng, dòng cuộn bằng không nên $R_2$ chưa có điện áp. Nguồn đặt toàn bộ điện áp lên cuộn và lên nhánh $R_1$.
- Trước khi mở, dòng cuộn đã đạt $\mathcal E/R_2$. Ngay sau mở, dòng đó tiếp tục qua vòng gồm $R_1,R_2,L$.
- Giữ dấu điện áp theo đúng thứ tự hai điểm. Dòng qua $R_1$ sau mở đi ngược chiều từ $a$ đến $b$.

(a)–(d) Ngay sau đóng,

$$
v_{ab}=v_{cd}=+60{,}0\,\mathrm V.
$$

Điểm $a$ cao thế hơn $b$, điểm $c$ cao thế hơn $d$.

(e)–(h) Trước mở, dòng cuộn bằng

$$
I_0=\frac{\mathcal E}{R_2}=2{,}40\,\mathrm A.
$$

Sau mở, nó đi qua $R_2$ từ $a$ đến $c$, qua cuộn từ $c$ đến $d$, rồi trở về qua $R_1$ từ $b$ đến $a$. Vì thế

$$
\begin{aligned}
v_{ab} &= -I_0R_1=-96{,}0\,\mathrm V, \\
L\frac{di}{dt} &= -(R_1+R_2)i, \\
v_{cd} &= -(R_1+R_2)I_0 \\
&= -156\,\mathrm V.
\end{aligned}
$$

Điểm $b$ cao thế hơn $a$, còn $d$ cao thế hơn $c$. Độ lớn điện áp cuộn là 156 V. Dấu âm của $v_{cd}$ phù hợp với dòng cuộn đang giảm và cuộn đang cấp năng lượng cho hai điện trở.
:::

::: exercise 30.62
Dùng mạch Hình P30.61 với $\mathcal E=60{,}0\,\mathrm V$, $R_1=40{,}0\,\Omega$, $R_2=25{,}0\,\Omega$, $L=0{,}300\,\mathrm H$.

(a) Sau khi đóng công tắc, tại một thời điểm dòng cuộn tăng $50{,}0\,\mathrm{A/s}$. Tìm dòng $i_1$ qua $R_1$ và $i_2$ qua $R_2$. Gợi ý: Xét riêng vòng có nguồn và $R_1$, rồi vòng có nguồn, $R_2,L$.

(b) Sau khi công tắc đóng rất lâu, lại mở nó. Ngay sau mở, dòng qua $R_1$ bằng bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Trong giai đoạn có nguồn, hai nhánh chịu cùng điện áp nguồn. Sau mở, dòng cuộn chuyển sang vòng nối tiếp hai điện trở.

**Hướng đi:**

- Nhánh $R_1$ độc lập với sự biến thiên dòng ở nhánh cuộn khi nguồn lý tưởng vẫn nối vào.
- Điện áp cuộn tại thời điểm câu (a) bằng $L\,di_2/dt$, nên điện áp còn lại trên $R_2$ cho dòng nhánh đó.
- Ở câu (b), giữ dòng cuộn liên tục khi mở và xác định chiều trở về qua $R_1$.

(a) Ta có

$$
\begin{aligned}
i_1 &= \frac{60{,}0}{40{,}0}=1{,}50\,\mathrm A, \\
v_L &= L\frac{di_2}{dt}=15{,}0\,\mathrm V, \\
i_2 &= \frac{60{,}0-15{,}0}{25{,}0} \\
&= 1{,}80\,\mathrm A.
\end{aligned}
$$

(b) Dòng ổn định trước mở bằng $60{,}0/25{,}0=2{,}40\,\mathrm A$ trong cuộn. Ngay sau mở, dòng qua $R_1$ có cùng độ lớn 2,40 A nhưng đi từ $b$ đến $a$. Nếu vẫn lấy chiều dương từ $a$ đến $b$ thì $i_1=-2{,}40\,\mathrm A$.
:::

::: exercise 30.63
Trong Hình P30.63, $\mathcal E=36{,}0\,\mathrm V$, $R_0=50{,}0\,\Omega$, $R=150\,\Omega$, $L=4{,}00\,\mathrm H$.

(a) Đóng $S_1$, giữ $S_2$ mở. Ngay sau đóng, tìm dòng $i_0$ qua $R_0$, $v_{ac}$ và $v_{cb}$. (b) Tìm ba đại lượng ấy sau khi dòng đã ổn định, vẫn giữ $S_2$ mở. (c) Lập biểu thức ba đại lượng theo thời gian kể từ lúc đóng $S_1$, đối chiếu hai giới hạn và vẽ đồ thị.

![Hình P30.63: R0 nối tiếp với R và L khi S2 mở, còn S2 có thể nối tắt đoạn từ c đến b.](img/young-30/hinh-p30-63.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khi $S_2$ mở, cả ba phần tử nối tiếp và có cùng dòng. $v_{cb}$ là điện áp của cả $R$ lẫn $L$, không phải riêng cuộn.

**Hướng đi:**

- Dùng tổng điện trở $R_0+R$ trong nghiệm dòng tăng RL.
- Tính $v_{ac}=R_0i_0$, rồi dùng định luật vòng $v_{cb}=\mathcal E-v_{ac}$.
- Giữ nguyên vị trí hai đầu đo để kiểm tra các giới hạn đầu và cuối.

(a) Dòng đầu bằng không, nên $i_0=0$, $v_{ac}=0$ và $v_{cb}=36{,}0\,\mathrm V$.

(b) Dòng cuối bằng $36{,}0/200=0{,}180\,\mathrm A$. Khi đó $v_{ac}=9{,}00\,\mathrm V$ và $v_{cb}=27{,}0\,\mathrm V$.

(c) Đặt

$$
\begin{aligned}
\tau &= \frac{L}{R_0+R}=0{,}0200\,\mathrm s, \\
x(t) &= e^{-t/\tau}.
\end{aligned}
$$

Các hàm cần tìm là

$$
\begin{aligned}
I_\infty &= 0{,}180\,\mathrm A, \\
i_0(t) &= I_\infty[1-x(t)], \\
v_{ac}(t) &= (9{,}00\,\mathrm V)[1-x(t)], \\
v_{cb}(t) &= 27{,}0\,\mathrm V +(9{,}00\,\mathrm V)x(t).
\end{aligned}
$$

Tại $t=0$, $x=1$ cho đúng kết quả (a). Khi $t\to\infty$, $x\to0$ cho đúng kết quả (b).

![Lời giải 30.63: Dòng và điện áp trên R0 tăng theo thời gian, còn điện áp đoạn c-b giảm từ 36 V đến 27 V.](img/young-30/hinh-giai30-63.svg)
:::

::: exercise 30.64
Khi mạch Hình P30.63 đã có dòng ổn định với $S_1$ đóng, $S_2$ mở, đóng thêm $S_2$ và vẫn giữ $S_1$ đóng. Dùng các giá trị phần tử của bài 30.63.

(a) Ngay sau đóng $S_2$, tìm $v_{ac}$, $v_{cb}$ và các dòng qua $R_0,R,S_2$. (b) Tìm những đại lượng đó sau rất lâu. (c) Suy ba dòng theo thời gian từ lúc đóng $S_2$, đối chiếu hai giới hạn và vẽ đồ thị.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $S_2$ nối trực tiếp $c$ với $b$, nên đoạn gồm $R,L$ bị nối tắt ở hai đầu. Dòng cuộn vẫn liên tục và có thể lưu thông trong vòng kín qua $R,L,S_2$.

**Hướng đi:**

- Sau đóng, $v_{cb}=0$ và toàn bộ điện áp nguồn đặt lên $R_0$.
- Dòng qua $R$ bằng dòng cuộn, bắt đầu từ 0,180 A rồi suy giảm với hằng số thời gian $L/R$.
- Dùng định luật nút tại $c$ để suy dòng công tắc bằng dòng qua $R_0$ trừ dòng nhánh $R,L$.

Chọn các dòng qua $R$ và $S_2$ dương từ $c$ về $b$. Trong toàn bộ giai đoạn sau đóng,

$$
\begin{aligned}
v_{ac} &= 36{,}0\,\mathrm V, \\
v_{cb} &= 0, \\
i_{R_0} &= 0{,}720\,\mathrm A.
\end{aligned}
$$

(a) Ngay sau đóng, $i_R=0{,}180\,\mathrm A$ và $i_{S_2}=0{,}540\,\mathrm A$.

(b) Về lâu dài, dòng nhánh cuộn đã mất năng lượng trên $R$ nên $i_R=0$, còn $i_{S_2}=0{,}720\,\mathrm A$.

(c) Phương trình vòng nhánh bị nối tắt là $L\,di_R/dt+Ri_R=0$. Do đó

$$
\begin{aligned}
\tau_d &= \frac LR=0{,}0267\,\mathrm s, \\
i_R(t) &= (0{,}180\,\mathrm A)e^{-t/\tau_d}, \\
i_{S_2}(t) &= 0{,}720\,\mathrm A-i_R(t).
\end{aligned}
$$

Dòng qua $R_0$ có thể nhảy từ 0,180 A lên 0,720 A vì nhánh ấy không chứa cuộn cảm. Dòng cuộn giữ nguyên ngay lúc chuyển, rồi mới giảm liên tục.

![Lời giải 30.64: Dòng qua R0 không đổi sau chuyển mạch, dòng qua R giảm, còn dòng qua S2 tăng để thỏa định luật nút.](img/young-30/hinh-giai30-64.svg)
:::

::: exercise 30.65
Đóng công tắc của mạch Hình P30.65 tại $t=0$. Tìm số chỉ từng đồng hồ (a) ngay sau đóng, (b) rất lâu sau đóng. Các cuộn và đồng hồ được coi là lý tưởng.

![Hình P30.65: Nguồn 25,0 V cấp qua điện trở 40,0 ohm cho ba nhánh song song, gồm hai nhánh điện trở và cuộn cảm cùng một nhánh 15,0 ohm.](img/young-30/hinh-p30-65.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $A_1$ đo tổng dòng. $A_2,A_3,A_4$ lần lượt đo nhánh 5,0 Ω và 20,0 mH, nhánh 10,0 Ω và 10,0 mH, nhánh 15,0 Ω.

**Hướng đi:**

- Ngay sau đóng, hai dòng cuộn chưa tăng khỏi không, nên nguồn chỉ cấp qua 40,0 Ω và 15,0 Ω nối tiếp.
- Về lâu dài, các cuộn lý tưởng có điện áp bằng không. Ba điện trở nhánh mắc song song và bộ đó nối tiếp 40,0 Ω.
- Dùng điện áp chung ba nhánh để chia dòng, rồi cộng lại kiểm tra số chỉ tổng.

Ban đầu $i_1=25{,}0/(40{,}0+15{,}0)\,\mathrm A$. Ở trạng thái cuối,

$$
\begin{aligned}
\frac1{R_p} &= \frac1{5{,}0\,\Omega} +\frac1{10{,}0\,\Omega} +\frac1{15{,}0\,\Omega}, \\
i_1 &= \frac{25{,}0\,\mathrm V}{40{,}0\,\Omega+R_p}, \\
v_p &= i_1R_p.
\end{aligned}
$$

Chia $v_p$ cho từng điện trở nhánh cho các số chỉ sau:

| Đồng hồ | Ngay sau đóng | Rất lâu sau đóng |
| --- | --- | --- |
| $A_1$ | $0{,}455\,\mathrm A$ | $0{,}585\,\mathrm A$ |
| $A_2$ | $0$ | $0{,}319\,\mathrm A$ |
| $A_3$ | $0$ | $0{,}160\,\mathrm A$ |
| $A_4$ | $0{,}455\,\mathrm A$ | $0{,}106\,\mathrm A$ |

Độ lớn tự cảm của hai nhánh không ảnh hưởng hai giới hạn này, nhưng ảnh hưởng quá trình chuyển tiếp giữa chúng.
:::

::: exercise 30.66
Trong Hình P30.66, bỏ qua điện trở nguồn và các cuộn. Các tụ ban đầu chưa tích điện, công tắc ở vị trí 1 rất lâu. (a) Dòng trong mạch bằng bao nhiêu? (b) Chuyển đột ngột sang vị trí 2. Tìm điện tích cực đại mỗi tụ nhận được và thời gian từ lúc chuyển đến khi đạt điện tích ấy.

![Hình P30.66: Hai cuộn 15,0 mH và 5,0 mH nối tiếp được chuyển từ mạch nguồn sang hai tụ 25,0 và 35,0 microfarad nối tiếp.](img/young-30/hinh-p30-66.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Trước chuyển, cuộn mang dòng ổn định qua nguồn 75,0 V và điện trở 125,0 Ω. Sau chuyển, năng lượng trao đổi trong bộ LC lý tưởng.

**Hướng đi:**

- Cộng tự cảm nối tiếp, bỏ qua hỗ cảm giữa các cuộn trong mô hình mạch.
- Ghép hai tụ nối tiếp để tìm điện dung tương đương. Điện lượng trên hai tụ có cùng độ lớn vì nút giữa chúng ban đầu trung hòa.
- Dùng bảo toàn năng lượng và thời gian một phần tư chu kỳ từ cực đại dòng đến cực đại điện tích.

(a) Dòng đầu bằng

$$
I_0=\frac{75{,}0}{125{,}0}=0{,}600\,\mathrm A.
$$

(b) Bộ phần tử tương đương có

$$
\begin{aligned}
L_* &= 20{,}0\,\mathrm{mH}, \\
C_* &= \frac{C_1C_2}{C_1+C_2} \\
&= 14{,}6\,\mu\mathrm F.
\end{aligned}
$$

Khi dòng trở về không lần đầu,

$$
\begin{aligned}
Q_{\max} &= I_0\sqrt{L_*C_*} \\
&= 324\,\mu\mathrm C, \\
t_{\max} &= \frac\pi2\sqrt{L_*C_*} \\
&= 8{,}48\times10^{-4}\,\mathrm s.
\end{aligned}
$$

Mỗi tụ đều có điện tích cực đại 324 µC. Điện áp hai tụ khác nhau do điện dung của chúng khác nhau.
:::

::: exercise 30.67. Đo điện áp của ống dây
Một ống dây chưa biết $L$ mắc nối tiếp điện trở $10{,}0\,\Omega$, pin có điện trở trong không đáng kể và công tắc. Vôn kế lý tưởng đo điện áp $v_L$ trên toàn ống dây theo thời gian kể từ khi đóng. Dữ liệu như Hình P30.67. Đo được $v_L=50{,}0\,\mathrm V$ ngay sau đóng và $v_L=20{,}0\,\mathrm V$ sau rất lâu.

(a) Lập $v_L(t)$ bằng định luật vòng. (b) Tìm suất điện động pin. (c) Tìm điện áp điện trở 10,0 Ω và dòng ở trạng thái cuối. (d) Tìm điện trở riêng ống dây $R_L$. (e) Dùng biểu thức lý thuyết và đồ thị để suy $L$. Gợi ý: Tìm điện áp khi $t=\tau$, rồi đọc thời điểm đó trên hình.

![Hình P30.67: Điện áp đo trên ống dây giảm theo thời gian và tiến đến một giá trị khác không.](img/young-30/hinh-p30-67.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện áp đo gồm cả sụt áp điện trở dây quấn và điện áp tự cảm. Vì vậy điện áp cuối khác không không có nghĩa cuộn lý tưởng còn suất điện động tự cảm ở trạng thái ổn định.

**Hướng đi:**

- Mô hình ống dây bằng $R_L$ nối tiếp $L$, còn điện trở ngoài là $R$.
- Dùng nghiệm dòng với tổng điện trở $R+R_L$, rồi lấy điện áp nguồn trừ sụt áp điện trở ngoài.
- Từ hai giới hạn suy điện trở riêng trước khi dùng hằng số thời gian để tìm tự cảm.

(a) Đặt

$$
\begin{aligned}
I_\infty &= \frac{\mathcal E}{R+R_L}, \\
\tau &= \frac{L}{R+R_L}, \\
i(t) &= I_\infty(1-e^{-t/\tau}).
\end{aligned}
$$

Điện áp trên toàn ống dây là

$$
\begin{aligned}
v_L(t) &= \mathcal E-Ri(t) \\
&= R_LI_\infty+RI_\infty e^{-t/\tau}.
\end{aligned}
$$

(b)–(d) Ngay sau đóng, dòng bằng không nên $\mathcal E=v_L(0)=50{,}0\,\mathrm V$. Khi ổn định,

$$
\begin{aligned}
v_{R,\infty} &= 50{,}0-20{,}0 \\
&= 30{,}0\,\mathrm V, \\
I_\infty &= \frac{30{,}0}{10{,}0}=3{,}00\,\mathrm A, \\
R_L &= \frac{20{,}0}{3{,}00} \\
&= 6{,}67\,\Omega.
\end{aligned}
$$

(e) Khi $t=\tau$, điện áp bằng

$$
\begin{aligned}
v_L(\tau) &= 20{,}0+\frac{30{,}0}{e} \\
&\approx 31{,}0\,\mathrm V.
\end{aligned}
$$

Đọc đồ thị ở mức đó cho $\tau\approx2{,}4\,\mathrm{ms}$. Do đó

$$
\begin{aligned}
L &= (R+R_L)\tau \\
&\approx 4{,}0\times10^{-2}\,\mathrm H.
\end{aligned}
$$

![Lời giải 30.67: Các điểm điện áp đọc từ đồ thị phù hợp với mô hình suy giảm về 20 V và hằng số thời gian xấp xỉ 2,4 ms.](img/young-30/hinh-giai30-67.svg)

Giá trị tự cảm có độ chính xác của phép đọc hình, nên không nên ghi nhiều chữ số hơn mức đồ thị cho phép.
:::

::: exercise 30.68. Đo điện áp trên điện trở ngoài
Một ống dây chưa biết điện trở và tự cảm mắc nối tiếp điện trở $50{,}0\,\Omega$, pin $25{,}0\,\mathrm V$ có điện trở trong không đáng kể và công tắc. Vôn kế lý tưởng đo điện áp $v_R$ trên điện trở ngoài theo thời gian. Hình P30.68 cho dữ liệu. Điện áp ngay sau đóng bằng không và sau rất lâu bằng $25{,}0\,\mathrm V$.

(a) Tìm điện trở ống dây $R_L$. (b) Lập $v_R(t)$. (c) Tìm điện áp ở một hằng số thời gian, đọc $\tau$ và suy $L$. (d) Tìm năng lượng cuộn ở trạng thái cuối.

![Hình P30.68: Điện áp trên điện trở ngoài tăng từ không và tiến đến điện áp pin 25,0 V.](img/young-30/hinh-p30-68.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Ở trạng thái cuối, toàn bộ điện áp nguồn nằm trên điện trở ngoài. Dùng mô hình tham số đúng với các giá trị đo được cho trong đề.

**Hướng đi:**

- So điện áp cuối với điện áp nguồn để tìm sụt áp trên điện trở cuộn.
- Nhân nghiệm dòng tăng RL với điện trở ngoài để được điện áp đo.
- Tại một hằng số thời gian, điện áp đạt $1-e^{-1}$ giá trị cuối.

(a) Dòng cuối bằng $25{,}0/50{,}0=0{,}500\,\mathrm A$. Điện áp còn lại trên cuộn bằng không, nên $R_L=0$ trong mô hình dữ kiện này.

(b)–(c) Với $\tau=L/R$,

$$
\begin{aligned}
v_R(t) &= \mathcal E(1-e^{-t/\tau}), \\
v_R(\tau) &= \mathcal E(1-e^{-1}) \\
&= 15{,}8\,\mathrm V.
\end{aligned}
$$

Đồ thị cho thời điểm đạt mức ấy khoảng 8,0 ms. Vì vậy

$$
L=R\tau\approx0{,}400\,\mathrm H.
$$

(d) Năng lượng cuối là

$$
\begin{aligned}
U_{B,\infty} &= \frac12LI_\infty^2 \\
&\approx 5{,}00\times10^{-2}\,\mathrm J.
\end{aligned}
$$

![Lời giải 30.68: Các điểm đọc trên đồ thị phù hợp với điện áp tăng đến 25 V, qua mức 15,8 V ở khoảng 8,0 ms.](img/young-30/hinh-giai30-68.svg)
:::
