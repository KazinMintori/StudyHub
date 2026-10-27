<!-- Source: Problems21.81–21.92, printed714–715, PDF734–735. -->

### Bài tập tổng hợp tiếp theo

::: exercise 21.81 •••
Đĩa tích điện đều như Hình 21.25 có bán kính $2.50\,\mathrm{cm}$ và điện tích tổng $7.0\times10^{-12}\,\mathrm C$. (a) Tìm độ lớn và hướng trường trên trục tại $x=20.0\,\mathrm{cm}$. (b) Chứng tỏ khi $x\gg R$, (21.11) trở thành $E=Q/(4\pi\varepsilon_0x^2)$. (c) Trường ở (a) lớn hơn hay nhỏ hơn trường của điện tích điểm cùng Q cách $20.0\,\mathrm{cm}$? Giải thích bằng gần đúng ở (b). (d) Tìm chênh lệch phần trăm giữa hai trường tại $x=20.0\,\mathrm{cm}$ và $10.0\,\mathrm{cm}$.
:::

![Hình 21.25: Chia đĩa thành những vòng đồng tâm để tính trường](img/young-21/hinh-21-25.png)


<!-- detailed-solution:21.81 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Đĩa R = 0,0250 m, Q = $7.0\times10^{-12}$ C; xét x = 0,200 m và 0,100 m.

**Hướng đi:**

- Dùng trường đĩa, thay $\sigma=Q/(\pi R^2)$.
- Khai triển theo $R^2/x^2$ để so với điện tích điểm.
- So sánh trường cần chỉ rõ mẫu số khi tính phần trăm.

Đặt hệ số trường $E_0=Q/(2\pi\varepsilon_0R^2)$ và khoảng cách $\rho=\sqrt{x^2+R^2}$. Khi đó:

$$
E=E_0\left(1-\frac x\rho\right).
$$

(a) Tại x = 0,200 m, E = 1,56 N/C, hướng +x. (b) Với $u=R^2/x^2\ll1$, $(1+u)^{-1/2}\approx1-u/2$, nên:

$$
E\approx\frac{Q}{2\pi\varepsilon_0R^2}\frac{R^2}{2x^2} = \frac{kQ}{x^2}.
$$

(c) Đĩa cho trường nhỏ hơn nguồn điểm: Những phần xa tâm vừa cách P xa hơn vừa không hướng hoàn toàn theo trục. (d) Lấy phần trăm so với trường đĩa, $(E_{\mathrm{point}}-E_{\mathrm{disk}})/E_{\mathrm{disk}}$, được khoảng 1,17% tại 20,0 cm và 4,66% tại 10,0 cm. Nếu dùng trường điểm làm mẫu số, các giá trị tương ứng là 1,16% và 4,46%.
:::

::: exercise 21.82 •• CP
Cầu nhỏ khối lượng m, điện tích dương q gắn vào một đầu sợi lụa dài L. Đầu kia gắn vào mặt cách điện đứng rất lớn có mật độ mặt dương $\sigma$. Chứng tỏ ở cân bằng, góc dây so với mặt đứng là $\arctan[q\sigma/(2mg\varepsilon_0)]$.
:::


<!-- detailed-solution:21.82 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cầu dương q treo gần mặt phẳng lớn dương σ.

**Hướng đi:**

- Trường mặt lớn vuông góc mặt với $E=\sigma/(2\varepsilon_0)$.
- Cân bằng lực ngang và đứng để khử lực căng.

$$
\begin{aligned}
T\cos\theta &= mg, \\
T\sin\theta &= q\sigma/(2\varepsilon_0), \\
\theta &= \arctan\left(\frac{q\sigma}{2mg\varepsilon_0}\right).
\end{aligned}
$$

Góc không phụ thuộc L trong mô hình mặt phẳng vô hạn.
:::

::: exercise 21.83 •• CALC
Điện tích âm $-Q$ phân bố đều trên một phần tư đường tròn bán kính a ở góc phần tư thứ nhất, tâm cong tại gốc. Tìm $E_x,E_y$ tổng tại gốc.
:::


<!-- detailed-solution:21.83 -->
::: solution Chi tiết
**Tóm tắt đề bài:** −Q đều trên cung một phần tư ở góc phần tư I, bán kính a.

**Hướng đi:**

- Nguồn âm tạo trường tại gốc hướng về từng phần tử, nên cả hai thành phần dương.
- Phần tử có $dq=-2Q\,d\theta/\pi$, θ chạy 0 đến π/2.

$$
\begin{aligned}
E_x &= \frac{2kQ}{\pi a^2}\int_0^{\pi/2}\cos\theta\,d\theta, \\
E_y &= \frac{2kQ}{\pi a^2}\int_0^{\pi/2}\sin\theta\,d\theta, \\
E_x &= E_y \\
&= \frac{2kQ}{\pi a^2}.
\end{aligned}
$$
:::

::: exercise 21.84 •• CALC
Nửa vòng bán kính a nằm trong hai góc phần tư trên, tâm tại gốc. $+Q$ phân bố đều trên nửa bên trái, $-Q$ trên nửa bên phải như Hình P21.84. Tìm độ lớn và hướng trường tổng tại gốc.
:::

![Hình P21.84: Nửa vòng bên trái dương, bên phải âm](img/young-21/hinh-p21-84.png)


<!-- detailed-solution:21.84 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cung trái +Q, cung phải −Q, mỗi cung dài πa/2.

**Hướng đi:**

- Phần tử đối xứng có thành phần đứng đối nhau và thành phần ngang cùng hướng phải.
- Có thể cộng hai kết quả cung một phần tư.

Mỗi nửa cung góp thành phần x bằng $2kQ/(\pi a^2)$ và thành phần y bằng nhau ngược dấu. Vì vậy:

$$
\vec E = \frac{4kQ}{\pi a^2}\hat{\mathbf i}.
$$
:::

::: exercise 21.85 ••
Hai thanh không dẫn điện dài $1.20\,\mathrm m$ gặp nhau vuông góc. Một thanh có $+2.50\,\mu\mathrm C$ phân bố đều, thanh kia có $-2.50\,\mu\mathrm C$ như Hình P21.85. (a) Tìm trường tại P cách mỗi thanh $60.0\,\mathrm{cm}$. (b) Nếu thả electron tại P, tìm độ lớn và hướng tổng lực do các thanh.
:::

![Hình P21.85: Thanh ngang dương, thanh đứng âm và điểm P cách đều](img/young-21/hinh-p21-85.png)


<!-- detailed-solution:21.85 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai thanh vuông góc dài 1,20 m, điện tích ±2,50 µC, P cách trung điểm mỗi thanh 0,600 m.

**Hướng đi:**

- P trên trung trực mỗi thanh.
- Thanh ngang dương tạo trường xuống, thanh đứng âm tạo trường trái.
- Hai độ lớn bằng nhau, nên tổng tạo góc 225°.

$$
\begin{aligned}
E_0 &= \frac{kQ}{0.600\sqrt{0.600^2+0.600^2}}, \\
E &= \sqrt2E_0=6.25\times10^4\,\mathrm{N/C}, \\
F_e &= eE=1.00\times10^{-14}\,\mathrm N.
\end{aligned}
$$

Lực electron ngược trường, tạo góc 45° từ hướng phải.
:::

::: exercise 21.86 •
Hai mặt rất lớn song song cách $5.00\,\mathrm{cm}$. A có mật độ đều $-8.80\,\mu\mathrm{C/m^2}$. B ở bên phải A có mật độ đều $-11.6\,\mu\mathrm{C/m^2}$. Coi hai mặt vô hạn. Tìm trường tại (a) điểm cách A $4.00\,\mathrm{cm}$ về phải, (b) điểm cách A $4.00\,\mathrm{cm}$ về trái, (c) điểm cách B $4.00\,\mathrm{cm}$ về phải.
:::


<!-- detailed-solution:21.86 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai mặt âm A và B, độ lớn mật độ 8,80 và 11,6 µC/m², B ở phải A.

**Hướng đi:**

- Mỗi trường hướng về mặt âm.
- Giữa mặt lấy hiệu; ngoài hai mặt lấy tổng.
- Khoảng cách không ảnh hưởng độ lớn trong mô hình vô hạn.

$$
\begin{aligned}
E_{\mathrm{khe}} &= \frac{(11.6-8.80)\times10^{-6}}{2\varepsilon_0} \\
&= 1.58\times10^5\,\mathrm{N/C}, \\
E_{\mathrm{ngoai}} &= \frac{(11.6+8.80)\times10^{-6}}{2\varepsilon_0} \\
&= 1.15\times10^6\,\mathrm{N/C}.
\end{aligned}
$$

(a) Hướng phải. (b) Hướng phải. (c) Hướng trái.
:::

::: exercise 21.87 •• CP
Đĩa mỏng có lỗ tròn tại tâm, gọi là vành khăn, có bán kính trong $R_1$, ngoài $R_2$ và mật độ mặt dương đều $\sigma$, như Hình P21.87. (a) Tìm điện tích tổng. (b) Đặt vành trong mặt yz, tâm ở gốc. Tìm độ lớn và hướng trường tại điểm bất kỳ trên trục x, ở cả hai phía. (c) Chứng tỏ gần gốc, độ lớn trường gần tỷ lệ với khoảng cách đến tâm. “Đủ gần” cần thỏa điều kiện nào? (d) Hạt điểm khối lượng m, điện tích $-q$ chỉ được chuyển động trên trục x. Thả từ nghỉ tại $x=0.01R_1$, tìm tần số dao động. Ôn mục 14.2 và coi vành đứng yên.
:::

![Hình P21.87: Vành khăn tích điện và trục vuông góc x](img/young-21/hinh-p21-87.png)


<!-- detailed-solution:21.87 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Vành khăn có $R_2>R_1$, mật độ σ và hạt âm chỉ chuyển động trên trục.

**Hướng đi:**

- Vành bằng đĩa lớn trừ đĩa nhỏ, nên trừ hai trường đĩa.
- Gần tâm, khai triển theo $x^2/R_1^2$ cho trường tuyến tính.
- Lực lên hạt âm khi đó có dạng phục hồi để dùng dao động điều hòa.

(a) $Q=\pi\sigma(R_2^2-R_1^2)$. (b) Biểu thức có dấu dùng được cả hai phía:

Gọi hai khoảng cách đến các đường tròn biên là:

$$
\begin{aligned}
&r_1=\sqrt{x^2+R_1^2},\\
&r_2=\sqrt{x^2+R_2^2}.
\end{aligned}
$$

Khi trừ hai trường đĩa:

$$
E_x=\frac{\sigma x}{2\varepsilon_0}\left(\frac1{r_1}-\frac1{r_2}\right).
$$

Trường dương với x > 0, âm với x < 0, bằng không ở tâm. (c) Khi $|x|\ll R_1$:

$$
E_x\approx\frac{\sigma}{2\varepsilon_0}\left(\frac1{R_1}-\frac1{R_2}\right)x.
$$

(d) $F_x=-qE_x=-\kappa x$, với hệ số phục hồi dương. Tần số:

Hệ số phục hồi và tần số là:

$$
\kappa=\frac{q\sigma}{2\varepsilon_0}\left(\frac1{R_1}-\frac1{R_2}\right),
$$

$$
f=\frac1{2\pi}\sqrt{\frac\kappa m}.
$$

Biên độ ban đầu 0,01R₁ thỏa gần đúng nhỏ.
:::

::: exercise 21.88 ••• DATA CP: Thiết kế máy in phun
Máy in phun có thể phun liên tục hoặc theo từng giọt khi cần. Trong kiểu liên tục, các giọt từ đầu phun chuyển động nhanh tạo chữ trên giấy. Bạn thuộc nhóm thiết kế máy, với mỗi giọt mực khối lượng $1.4\times10^{-8}\,\mathrm g$, bay ngang đến giấy ở $50\,\mathrm{m/s}$. Bộ nạp lấy bớt electron để giọt có điện tích dương q. Giọt qua hai bản lệch hướng dài $2.0\,\mathrm{cm}$, có trường đứng đều $8.0\times10^4\,\mathrm{N/C}$. (a) Để giọt lệch $0.30\,\mathrm{mm}$ khi đến mép ra, cần q bao nhiêu và phải lấy bớt bao nhiêu electron? (b) Nếu đổi tốc độ giọt còn $25\,\mathrm{m/s}$, q cần bao nhiêu để cùng độ lệch?
:::


<!-- detailed-solution:21.88 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Giọt mực $m=1.4\times10^{-11}$ kg, bản dài 0,020 m, E = $8.0\times10^4$ N/C, cần lệch 0,00030 m.

**Hướng đi:**

- Thời gian trong bản L/v.
- Gia tốc đứng qE/m, nên độ lệch bằng qEt²/(2m).
- Điện tích dương do lấy bớt electron, số lấy bớt bằng q/e.

$$
\begin{aligned}
t &= 0.020/50 \\
&= 4.0\times10^{-4}\,\mathrm s, \\
q &= \frac{2md}{Et^2} \\
&= 6.6\times10^{-13}\,\mathrm C, \\
N &= q/e\approx4.1\times10^6.
\end{aligned}
$$

Giảm tốc độ một nửa làm thời gian gấp đôi, nên để cùng độ lệch cần điện tích còn một phần tư: $q=1.6\times10^{-13}$ C.
:::

::: exercise 21.89 •• DATA
Hai cầu nhỏ dương cách $0.400\,\mathrm m$. Đặt $q_1$ tại gốc, $q_2$ tại $x=+0.400\,\mathrm m$. Có cầu thứ ba $q_3=4.00\times10^{-6}\,\mathrm C$ và thiết bị đo chính xác vị trí, lực tổng. Tại $x=0.200\,\mathrm m$, lực lên $q_3$ là $4.50\,\mathrm N$ hướng $+x$. Chuyển đến $x=+0.600\,\mathrm m$, lực là $3.50\,\mathrm N$ hướng $+x$. (a) Tính $q_1,q_2$. (b) Tìm lực lên $q_3$ tại $x=-0.200\,\mathrm m$. (c) Ngoài vị trí vô cùng xa, đặt $q_3$ ở x nào để lực bằng không?
:::


<!-- detailed-solution:21.89 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai phép đo lực tại 0,200 m và 0,600 m cho hai ẩn $q_1,q_2$.

**Hướng đi:**

- Lần đầu trường hai nguồn đối chiều; lần sau cùng chiều.
- Lập hai phương trình Coulomb có dấu, không lấy độ lớn tổng trước khi lập hệ.

$$
\begin{aligned}
4.50 &= kq_3(q_1-q_2)/0.200^2, \\
3.50 &= \frac{kq_3q_1}{0.600^2} +\frac{kq_3q_2}{0.200^2}.
\end{aligned}
$$

Giải hệ cho $q_1\approx8.00$ µC và $q_2\approx3.00$ µC. Tại x = −0,200 m, hai lực cùng trái:

$$
\begin{aligned}
F_x &= -k\frac{q_3q_1}{(0.200)^2} -k\frac{q_3q_2}{(0.600)^2} \\
&= -7.50\,\mathrm N.
\end{aligned}
$$

Điểm không lực nằm giữa nguồn, $q_1/x^2=q_2/(0.400-x)^2$, cho x = 0,248 m.
:::

::: exercise 21.90 ••• DATA
Điện tích dương Q phân bố đều trên vòng dẫn rất mảnh bán kính a, như Hình 21.23. Đo E trên trục ở nhiều khoảng cách x. (a) Các số đo x lớn được vẽ thành $Ex^2$ theo x ở Hình P21.90a. Giải thích vì sao $Ex^2$ tiến đến hằng số khi x tăng, rồi dùng đồ thị tính Q. (b) Các số đo x nhỏ được vẽ thành $E/x$ theo x ở Hình P21.90b. Giải thích giới hạn hằng khi x tiến tới không, rồi dùng đồ thị tính a.
:::

![Hình 21.23: Phần điện tích nhỏ trên vòng và các thành phần trường tại P](img/young-21/hinh-21-23.png)

![Hình P21.90: Hai đồ thị đo trường vòng ở xa và gần tâm](img/young-21/hinh-p21-90.png)

**Hình P21.90:** (a) Trục đứng $Ex^2$ có đơn vị $\mathrm{N\,m^2/C}$. (b) Trục đứng $E/x$ có đơn vị $\mathrm{N/(C\,m)}$. Trục ngang đều là x tính bằng mét.


<!-- detailed-solution:21.90 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Đồ thị cho giới hạn xa của $Ex^2$ khoảng 50 N·m²/C và giới hạn gần của E/x khoảng 700 N/(C·m).

**Hướng đi:**

- Trường trục vòng ở xa trở thành kQ/x², còn gần tâm trở thành kQx/a³.
- Hai giới hạn tách riêng Q và a.

$$
\begin{aligned}
\lim_{x\to\infty}Ex^2 &= kQ, \\
Q &\approx 50/k=5.6\,\mathrm{nC}, \\
\lim_{x\to0}E/x &= kQ/a^3, \\
a &\approx (50/700)^{1/3} \\
&= 0.41\,\mathrm m.
\end{aligned}
$$

Độ chính xác đáp số bị giới hạn bởi việc đọc đồ thị, nên không giữ quá nhiều chữ số.
:::

::: exercise 21.91 ••• CP
Mặt phẳng vô hạn tích điện dương đều $\sigma$ có lỗ tròn bán kính R, nằm trong mặt xy, tâm lỗ tại gốc, trục $+z$ hướng lên. Hạt khối lượng m, điện tích $-q$ ban đầu nghỉ ở tâm lỗ, chỉ được chuyển động dọc z. Khi thả, hạt rơi. Càng xuống dưới, lực điện hút lên càng tăng. Nếu m đủ nhỏ, lực điện vượt trọng lượng làm hạt chậm lại, dừng rồi trở về vị trí đầu, lặp lại chuyển động. (a) Tìm trường ở độ sâu $\Delta$ dưới gốc. (b) Tìm khối lượng cực đại $m_{\max}$ để hạt không rơi mãi. (c) Với $m<m_{\max}$, tìm công lực điện khi hạt từ $z=0$ đến $z=-\Delta$. (d) Tìm công trọng lực trên cùng khoảng. (e) Tìm độ sâu cực đại theo $\alpha=m/m_{\max}$, dùng định lý công–động năng để tìm tốc độ theo độ sâu rồi xét lúc tốc độ bằng không. (f) Tốc độ tại $\Delta\le\Delta_{\max}$ bằng bao nhiêu? (g) Với $\sigma=1.00\,\mathrm{nC/cm^2}$, $R=10.0\,\mathrm{cm}$, $m=25.0\,\mathrm g$ và độ lớn điện tích $1.00\,\mu\mathrm C$, tìm $m_{\max},\Delta_{\max}$.
:::


<!-- detailed-solution:21.91 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mặt tích điện có lỗ, hạt âm rơi dọc trục lỗ dưới trọng lực.

**Hướng đi:**

- Trường mặt có lỗ bằng trường mặt đầy trừ trường đĩa lấp lỗ.
- Lực điện lên hạt âm hướng lên.
- Dùng tích phân công và định lý công–động năng để tìm điểm quay đầu.

(a) Ở độ sâu Δ:

$$
\vec E = -\frac{\sigma\Delta}{2\varepsilon_0\sqrt{\Delta^2+R^2}}\hat{\mathbf k}.
$$

(b) Lực điện giới hạn ở rất sâu là $q\sigma/(2\varepsilon_0)$. Ngưỡng khối lượng $m_{\max}=q\sigma/(2g\varepsilon_0)$. Muốn quay đầu cần **m nhỏ hơn ngưỡng này**, vì ở ngưỡng lực điện chỉ tiến đến trọng lực mà không vượt nó.

**(c), (d)**

Gọi $F_0=q\sigma/(2\varepsilon_0)$ là độ lớn lực điện giới hạn. Đặt $\ell=\sqrt{\Delta^2+R^2}-R$. Hai công là:

$$
\begin{aligned}
W_e&=-F_0\int_0^\Delta\frac{s\,ds}{\sqrt{s^2+R^2}}\\
&=-F_0\ell,\\
W_g&=mg\Delta.
\end{aligned}
$$

(e) Đặt $\alpha=m/m_{\max}<1$. Khi quay đầu, $W_e+W_g=0$:

$$
\begin{aligned}
\alpha\Delta &= \sqrt{\Delta^2+R^2}-R, \\
\alpha\Delta+R &= \sqrt{\Delta^2+R^2}, \\
(\alpha\Delta+R)^2 &= \Delta^2+R^2.
\end{aligned}
$$

Khai triển bình phương vế trái rồi khử cùng R² ở hai vế:

$$
\begin{aligned}
\alpha^2\Delta^2+2\alpha R\Delta &= \Delta^2, \\
(1-\alpha^2)\Delta^2 &= 2\alpha R\Delta.
\end{aligned}
$$

Nghiệm Δ = 0 là vị trí thả ban đầu. Điểm quay đầu thứ hai có Δ > 0. Với 0 < α < 1, chia hai vế cho Δ và cho 1 − α² được:

$$
\Delta_{\max}=\frac{2R\alpha}{1-\alpha^2}.
$$

Hai vế ở bước trước khi bình phương đều không âm, nên phép bình phương không thêm nghiệm trái dấu. Điều kiện α < 1 cũng bảo đảm độ sâu tìm được dương và hữu hạn.

(f)

Với độ dài phụ $\ell=\sqrt{\Delta^2+R^2}-R$ đã dùng khi tính công, tốc độ là:

$$
v=\sqrt{2g\left(\Delta-\frac\ell\alpha\right)}.
$$

Công thức áp dụng trong đoạn chuyển động có biểu thức dưới căn không âm.

(g) Đổi mật độ thành $10^{-5}$ C/m², được $m_{\max}=57.7$ g, $\alpha=0.434$ và $\Delta_{\max}=10.7$ cm.
:::

::: exercise 21.92 ••• CP
Hai thanh cách điện cứng dài L, khối lượng không đáng kể, nối tâm bằng bản lề không ma sát. Một thanh cố định nằm ngang trên trụ đứng, thanh kia quay tự do theo phương ngang. Mỗi đầu thanh có cầu nhỏ điện tích Q, khối lượng M. Khi thanh vuông góc, mômen tổng lên thanh động bằng không. Thanh cố định theo trục x, tâm bản lề tại gốc, thanh động quay theo chiều kim đồng hồ khi nhìn từ trên như Hình P21.92. Gọi góc giữa thanh là $\theta$. (a) Tìm lực $\vec F_1$ do cầu trái thanh cố định lên cầu phía trên bên phải thanh động theo $\theta$. (b) Tìm lực $\vec F_2$ do cầu phải thanh cố định lên cùng cầu đó. (c) Tìm mômen $\vec F_1$ quanh bản lề. (d) Tìm mômen $\vec F_2$. (e) Tính mômen tổng lên thanh động, kể cả đóng góp từ hai đầu. (f) Gần cân bằng $\theta=\pi/2$, đặt $\theta=\pi/2-\epsilon$. Dùng khai triển chuỗi lũy thừa ở Phụ lục B, giữ số hạng bậc thấp nhất theo $\epsilon$ để tìm mômen. (g) Với biên độ nhỏ, hệ là dao động xoắn. Từ kết quả trước, tìm tần số dao động nhỏ.
:::

![Hình P21.92: Bốn điện tích tại đầu hai thanh nối bằng bản lề](img/young-21/hinh-p21-92.png)


<!-- detailed-solution:21.92 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai thanh dài L, hai cầu trên mỗi thanh đều Q,M, tâm quay tại gốc.

**Hướng đi:**

- Tính lực của hai đầu thanh cố định lên một đầu thanh động, lấy tích có hướng với vector vị trí, rồi nhân hai vì hai đầu thanh động góp cùng mômen.
- Quy ước dưới đây đo θ ngược chiều kim đồng hồ; nếu chọn chiều quay đối lại, dấu thành phần y và mômen z đảo, còn tần số không đổi.

Đặt $u=\theta/2$, đầu đang xét tại $(L\cos\theta/2,L\sin\theta/2)$. Khoảng cách đến đầu trái và phải của thanh cố định lần lượt là L cosu, L sinu.

$$
\begin{aligned}
F_{1x} &= \frac{kQ^2}{L^2\cos u}, \\
F_{1y} &= \frac{kQ^2\sin u}{L^2\cos^2u}, \\
F_{2x} &= -\frac{kQ^2}{L^2\sin u}, \\
F_{2y} &= \frac{kQ^2\cos u}{L^2\sin^2u}, \\
\tau_{1z} &= -\frac{kQ^2\sin u}{2L\cos^2u}, \\
\tau_{2z} &= \frac{kQ^2\cos u}{2L\sin^2u}.
\end{aligned}
$$

Tổng cho hai đầu:

$$
\tau_z = \frac{kQ^2}{L}\left(\frac{\cos u}{\sin^2u}-\frac{\sin u}{\cos^2u}\right).
$$

Đặt $\theta=\pi/2-\epsilon$, nên $u=\pi/4-\epsilon/2$. Để thấy rõ số hạng bậc nhất, gọi:

$$
g(u)=\frac{\cos u}{\sin^2u}-\frac{\sin u}{\cos^2u}.
$$

Hai số hạng bằng nhau tại $u=\pi/4$, nên $g(\pi/4)=0$. Đạo hàm từng số hạng cho:

Tách $g=g_1-g_2$ với:

$$
\begin{aligned}
&g_1(u)=\frac{\cos u}{\sin^2u},\\
&g_2(u)=\frac{\sin u}{\cos^2u}.
\end{aligned}
$$

Đạo hàm từng hàm:

$$
g_1'(u)=-\frac1{\sin u}-\frac{2\cos^2u}{\sin^3u},
$$

$$
g_2'(u)=\frac1{\cos u}+\frac{2\sin^2u}{\cos^3u}.
$$

Do đó:

$$
\begin{aligned}
g'(u)&=g_1'(u)-g_2'(u),\\
g'(\pi/4)&=-6\sqrt2.
\end{aligned}
$$

Vì vậy, $g(u)\approx(-6\sqrt2)(-\epsilon/2)$, và:

$$
\tau_z\approx\frac{3\sqrt2kQ^2}{L}\epsilon.
$$

Khi thanh lệch theo chiều làm θ nhỏ hơn π/2, mômen dương làm θ tăng trở lại. Đây là mômen phục hồi. Với $I=2M(L/2)^2=ML^2/2$:

$$
f = \frac1{2\pi}\sqrt{\frac{6\sqrt2kQ^2}{ML^3}}.
$$
:::
