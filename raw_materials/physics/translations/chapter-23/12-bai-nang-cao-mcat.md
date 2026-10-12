<!-- Source: Problems23.71–23.86, printed778–780, PDF798–800. -->

### Thanh tích điện và hệ nhiều nguồn

::: exercise 23.71 • CALC
Thanh mảnh dài a có tổng Q đều theo chiều dài, mốc điện thế ở vô hạn. Tìm V tại **(a)** P cách đầu phải thanh một khoảng x về phải, **(b)** R cách đầu phải thanh một khoảng y phía trên. **(c)** Xét gần đúng khi x hoặc y lớn hơn nhiều a.
:::

![Hình P23.71: Đoạn tích điện, điểm P bên phải và R phía trên đầu phải](img/young-23/hinh-p23-71.png)

<!-- detailed-solution:23.71 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Chọn ξ đo từ đầu phải về trái, 0 ≤ ξ ≤ a. Phần điện tích dq = (Q/a)dξ.

**Hướng đi:**

- Điện thế từng phần là kdq/r.
- P có khoảng cách x + ξ, còn R có khoảng cách $\sqrt{y^2+\xi^2}$.
- Khi khảo sát xa, kiểm tra dạng điện thế của nguồn điểm tổng Q.

$$
\begin{aligned}
V_P&=\frac{kQ}{a}\int_0^a\frac{d\xi}{x+\xi}\\
&=\frac{kQ}{a}\ln\frac{x+a}{x},\\
V_R&=\frac{kQ}{a}\int_0^a\frac{d\xi}{\sqrt{y^2+\xi^2}}\\
&=\frac{kQ}{a}\ln\frac{a+\sqrt{a^2+y^2}}y.
\end{aligned}
$$

Với x ≫ a, V_P ≈ kQ/x. Với y ≫ a, V_R ≈ kQ/y. Thanh nhìn từ xa tương đương một nguồn điểm về phần điện thế chính.
:::

::: exercise 23.72 ••• CP CALC
Thanh cứng khối lượng M, dài L, mang điện tích dương đều Q, quay tự do quanh gốc trong trường đều $\vec E=E\hat{\mathbf j}$. θ là góc thanh với +y như Hình P23.72. Bỏ trọng lực vì lực điện lớn hơn nhiều. **(a)** Viết V(y), với V(0) = V₀. **(b)** Tìm thế năng theo θ,V₀ bằng tích phân V dq. **(c)** Chọn V₀ thế nào để U = 0 khi θ = 0? **(d)** Thả nghỉ từ θ = 90°, tìm tốc độ góc khi qua θ = 0. **(e)** Với góc ban đầu nhỏ, tìm tần số dao động quanh θ = 0.
:::

![Hình P23.72: Thanh tích điện quay quanh gốc, góc θ đo với hướng trường +y](img/young-23/hinh-p23-72.png)

<!-- detailed-solution:23.72 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Phần thanh cách trục s có y = s cosθ và dq = (Q/L)ds. Mômen quán tính thanh quanh đầu là ML²/3.

**Hướng đi:**

- Trường đều +y cho V(y) giảm tuyến tính theo y.
- Tích phân thế năng của từng phần dq, không coi toàn Q nằm ở đầu thanh.
- Bảo toàn năng lượng quay cho tốc độ góc. Đạo hàm thế năng cho mômen phục hồi để xét dao động nhỏ.

**(a)** V(y) = V₀ − Ey. **(b)**

$$
\begin{aligned}
U(\theta)&=\frac QL\int_0^L(V_0-Es\cos\theta)ds\\
&=QV_0-\frac{QEL}{2}\cos\theta.
\end{aligned}
$$

**(c)** V₀ = EL/2. Khi ấy U = QEL(1 − cosθ)/2. **(d)** Tại 90°, U = QEL/2. Khi qua 0°, U = 0:

$$
\begin{aligned}
\frac12I\omega^2&=QEL/2,\\
\omega&=\sqrt{3QE/(ML)}.
\end{aligned}
$$

**(e)** Mômen lực là $\tau=-QEL\sin\theta/2$. Với |θ| nhỏ, sinθ ≈ θ, nên mômen phục hồi tuyến tính. Từ Iθ̈ = τ:

$$
f=\frac1{2\pi}\sqrt{\frac{3QE}{2ML}}.
$$

Tần số này chỉ áp dụng dao động góc nhỏ.
:::

::: exercise 23.73 ••• CP — Mô hình lực mạnh bằng lò xo
Hạt α có hai proton và hai neutron, đường kính cỡ 1 fm. Hai proton +e đẩy nhau, còn neutron không mang điện. Tương tác mạnh phải giữ hạt nhân khỏi tách ra. Trong mô hình thô, thay tương tác hút bằng lò xo Hooke giữa hai proton, bỏ neutron, chiều dài cân bằng riêng của lò xo bằng không. **(a)** Viết U theo khoảng cách d. **(b)** Tối thiểu hóa để tìm d₀. **(c)** Nếu d₀ = 1,00 fm, tìm độ cứng. **(d)** Tìm năng lượng lưu trong hệ theo eV. **(e)** Với khối lượng proton $1.67\times10^{-27}$ kg, nếu lò xo đứt, hạt α tan rã và hai proton bay ngược chiều, tìm tốc độ cuối.
:::

<!-- detailed-solution:23.73 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Gọi κ là độ cứng lò xo để phân biệt với hằng số Coulomb k. Khoảng cách d₀ là cân bằng của cả lực hút và lực đẩy.

**Hướng đi:**

- Thế năng gồm phần đàn hồi κd²/2 và phần đẩy điện ke²/d.
- Cân bằng là U′ = 0. Xét U″ để biết cực tiểu.
- Khi tính tốc độ, hai proton cùng khối lượng chia động năng đều, không dồn toàn năng lượng vào một hạt.

$$
\begin{aligned}
U(d)&=\frac12\kappa d^2+ke^2/d,\\
U'(d)&=\kappa d-ke^2/d^2,\\
d_0&=(ke^2/\kappa)^{1/3},\\
U''(d_0)&=3\kappa>0.
\end{aligned}
$$

Với d₀ = 1 fm, κ ≈ $2.31\times10^{17}$ N/m. Ở cân bằng, κd₀² = ke²/d₀, nên:

$$
\begin{aligned}
U(d_0)&=\frac{3ke^2}{2d_0}\\
&=2.16\,\mathrm{MeV}.
\end{aligned}
$$

Nếu toàn năng lượng lưu trong hệ chuyển thành động năng hai proton, $m_pv^2=U(d_0)$ cho v = $1.44\times10^7$ m/s mỗi proton. Đây là điều kiện năng lượng cần nêu cho mô hình tan rã này. Nếu chỉ bỏ lực lò xo và phần năng lượng đàn hồi bị mang ra ngoài khi đứt, chỉ còn năng lượng điện ke²/d₀ truyền thành động năng, cho tốc độ khoảng $1.17\times10^7$ m/s. Không thể chọn giữa hai cách phân bố năng lượng chỉ từ việc nói lực lò xo biến mất.
:::

::: exercise 23.74 •
Cầu kim loại R₁ mang Q₁, mốc V ở vô hạn. **(a)** Tìm trường và thế tại mặt. Sau đó nối bằng dây dẫn dài, mảnh với cầu R₂ ở cách vài mét, ban đầu trung hòa. Khi đạt cân bằng, bỏ lượng điện tích nhỏ trên dây. Tìm **(b)** điện tích mỗi cầu, **(c)** thế mỗi cầu, **(d)** trường tại từng mặt.
:::

<!-- detailed-solution:23.74 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai cầu xa nhau so với bán kính, bỏ tương tác gần và điện tích dây trong mô hình.

**Hướng đi:**

- Trước nối, dùng kết quả cầu dẫn đơn.
- Sau nối, toàn hệ dẫn đẳng thế, đồng thời tổng điện tích hai cầu bằng Q₁.
- Trường tại mặt bằng thế chung chia bán kính riêng của cầu.

**(a)** $E_{r1}=kQ_1/R_1^2$, V₁ = kQ₁/R₁. **(b), (c)**

$$
\begin{aligned}
Q'_1+Q'_2&=Q_1,\\
Q'_1/R_1&=Q'_2/R_2,\\
Q'_1&=\frac{Q_1R_1}{R_1+R_2},\\
Q'_2&=\frac{Q_1R_2}{R_1+R_2},\\
V_1=V_2&=\frac{kQ_1}{R_1+R_2}.
\end{aligned}
$$

**(d)** Các thành phần xuyên tâm có dấu là Eᵣ₁ = V/R₁, Eᵣ₂ = V/R₂. Với Q₁ dương, trường ra và mạnh hơn tại cầu nhỏ hơn. Với Q₁ âm, trường vào, độ lớn vẫn tỷ lệ nghịch bán kính.
:::

::: exercise 23.75 •
Hạt α ở rất xa có động năng 9,50 MeV, đi thẳng vào hạt nhân chì đứng yên, số hiệu nguyên tử 82. Tìm khoảng cách gần nhất. Coi hạt nhân cố định và là nguồn điểm, hạt α là hạt nhân heli số hiệu nguyên tử 2.
:::

<!-- detailed-solution:23.75 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai điện tích +2e và +82e đẩy nhau, chạm ngưỡng quay đầu theo đường xuyên tâm.

**Hướng đi:**

- Ở rất xa, thế năng bằng không. Tại khoảng cách gần nhất, động năng của hạt α bằng không trong va chạm thẳng tâm.
- Đổi MeV sang joule để dùng Coulomb trong SI.

$$
\begin{aligned}
K_0&=9.50\times10^6e,\\
r_{\min}&=\frac{k(2e)(82e)}{K_0}\\
&=2.49\times10^{-14}\,\mathrm m.
\end{aligned}
$$
:::

### Bài tập gradient và dữ liệu

::: exercise 23.76 • CALC
Trong vùng có $V(x,y,z)=A(x^2-3y^2+z^2)$. **(a)** Suy ra trường. **(b)** Khi điện tích thử 1,50 µC đi từ (0,0,0,250 m) đến gốc, công đo được $6.00\times10^{-5}$ J. Tìm A. **(c)** Tìm trường ở điểm đầu. **(d)** Chứng tỏ các đường đẳng thế trong mặt phẳng song song xz là những đường tròn khi mức thế tương ứng tồn tại. **(e)** Tìm bán kính đường V = 1280 V ở y = 2,00 m.
:::

<!-- detailed-solution:23.76 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Điện thế tại gốc bằng không, còn tại điểm đầu là A(0,250)².

**Hướng đi:**

- Lấy âm đạo hàm riêng cho trường.
- Công q(V_đầu − V_cuối) cho A.
- Giữ y hằng rồi viết phương trình mức V theo x,z để nhận đường tròn và điều kiện tồn tại.

**(a)** Eₓ = −2Ax, Eᵧ = +6Ay, E_z = −2Az. **(b)** A = 640 V/m². **(c)** Trường là −320 V/m theo z, hai thành phần kia bằng không.

**(d)** Trên mặt y = y₀:

$$
x^2+z^2=V/A+3y_0^2.
$$

Vế phải dương cho đường tròn, bằng không cho một điểm, âm thì không có đường mức. **(e)** Bán kính √14 m ≈ 3,74 m.
:::

::: exercise 23.77 •• DATA
Trong vùng cách gốc không quá 2,00 m, điện thế có dạng $V=Ax^l+By^m+Cz^n+D$. Các hằng số có đơn vị để x,y,z tính bằng m và V bằng volt. Dữ liệu đo như sau. **(a)** Tìm A,B,C,D,l,m,n. **(b)** Tìm V và độ lớn trường tại gốc, (0,50 m,0,50 m,0,50 m), (1,00 m,1,00 m,1,00 m).

| Điểm (m) | V (V) | Eₓ (V/m) | Eᵧ (V/m) | E_z (V/m) |
| --- | --- | --- | --- | --- |
| (0,0,0) | 10,0 | 0 | 0 | 0 |
| (1,00,0,0) | 4,0 | 12,0 | 0 | 0 |
| (0,1,00,0) | 6,0 | 0 | 12,0 | 0 |
| (0,0,1,00) | 8,0 | 0 | 0 | 12,0 |
:::

<!-- detailed-solution:23.77 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Dữ liệu trên từng trục tách riêng số hạng theo tọa độ đó.

**Hướng đi:**

- Giá trị ở gốc cho D.
- Hiệu điện thế từ gốc đến tọa độ 1 m cho hệ số A,B,C.
- Thành phần trường ở cùng điểm cho tích hệ số với số mũ, nên suy số mũ từ E = −∂V.

Ở gốc D = 10 V. Trên x = 1 m, A = −6,0 V/m² và −Al = 12,0 cho l = 2. Tương tự B = −4,0 V/m³, m = 3, C = −2,0 V/m⁶, n = 6. Hàm thu được là:

$$
V=10-6x^2-4y^3-2z^6.
$$

Tọa độ trong biểu thức này đo bằng m. Các thành phần trường là 12x, 12y², 12z⁵ theo V/m. Kết quả phần (b):

| Điểm | V | Độ lớn E |
| --- | --- | --- |
| Gốc | 10,0 V | 0 |
| (0,50;0,50;0,50) m | 7,97 V | 6,72 V/m |
| (1,00;1,00;1,00) m | −2,00 V | 20,8 V/m |

Những điểm yêu cầu đều nằm trong phạm vi bán kính 2,00 m đã cho.
:::

::: exercise 23.78 ••• DATA
Cầu nhỏ cố định mang Q chưa biết. Bắn hạt m = $4.00\times10^{-4}$ kg, q = $5.00\times10^{-8}$ C từ xa thẳng vào tâm cầu. Khối lượng cầu lớn hơn nhiều, coi đứng yên. Mọi khoảng cách đo lớn hơn nhiều bán kính hai vật, nên coi nguồn điểm. Đồ thị v² theo 1/x được khớp bởi:

$$
v^2=400\,\mathrm{m^2/s^2}
-\frac{15.75\,\mathrm{m^3/s^2}}x.
$$

**(a)** Giải thích vì sao đồ thị thẳng. **(b)** Tìm tốc độ đầu ở rất xa. **(c)** Tìm Q. **(d)** Tìm khoảng cách gần nhất, vẫn giả sử lớn hơn nhiều bán kính vật.
:::

![Hình P23.78: Đồ thị bình phương tốc độ theo nghịch đảo khoảng cách](img/young-23/hinh-p23-78.png)

<!-- detailed-solution:23.78 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Trục ngang là 1/x, hệ số chặn 400, hệ số góc −15,75 trong SI.

**Hướng đi:**

- Bảo toàn cơ năng cho v² = v₀² − 2kQq/(mx), tuyến tính theo 1/x.
- Hệ số chặn cho v₀, hệ số góc cho Q. Điểm quay đầu có v² = 0.

**(a)** Quan hệ thẳng xuất phát từ thế năng nguồn điểm tỷ lệ 1/x. **(b)** v₀ = 20,0 m/s. **(c)** Q = +7,01 µC. Dấu dương phù hợp hạt dương chậm lại do lực đẩy. **(d)** $x_{\min}=15.75/400=0.0394$ m, tức 3,94 cm.
:::

::: exercise 23.79 ••• DATA — Thí nghiệm giọt dầu Millikan
Robert Millikan đo điện tích electron trong các thí nghiệm 1909–1913. Những giọt dầu rất nhỏ, cỡ $10^{-4}$ mm, được phun giữa hai bản nằm ngang cách d, có điện áp V_AB tạo trường xuống. Giọt có thể nhận điện tích âm do ma sát hoặc ion hóa bởi tia X, phóng xạ, rồi được quan sát bằng kính hiển vi.

**(a)** Bỏ lực đẩy nổi không khí, chứng tỏ giọt bán kính r đứng yên khi độ lớn điện tích là $|q|=4\pi\rho r^3gd/(3V_{AB})$, với ρ là mật độ dầu. **(b)** Không đo r trực tiếp. Khi tắt trường, giọt rơi với tốc độ giới hạn v_t, lực cản Stokes 6πηrv cân bằng trọng lượng. Chứng tỏ công thức điện tích theo v_t bên dưới. **(c)** Tính điện tích bốn giọt trong bảng, với d = 1,00 mm, ρ = 824 kg/m³, η = $1.81\times10^{-5}$ N s/m², g = 9,80 m/s². **(d)** Giả sử điện tích giọt −ne. Giọt 2 có độ lớn nhỏ nhất trong 300 giọt đo, coi nó dư đúng một electron. Suy n cho những giọt khác. **(e)** Tính e từ từng giọt rồi lấy trung bình.

$$
|q|=\frac{18\pi d}{V_{AB}}
\sqrt{\frac{\eta^3v_t^3}{2\rho g}}.
$$

| Giọt | V_AB (V) | v_t ($10^{-5}$ m/s) |
| --- | --- | --- |
| 1 | 9,16 | 2,54 |
| 2 | 4,57 | 0,767 |
| 3 | 12,32 | 4,39 |
| 4 | 6,28 | 1,52 |
:::

<!-- detailed-solution:23.79 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Giọt âm chịu lực điện lên, trọng lực xuống. Mật độ ρ và độ nhớt η đã biết, bỏ lực nổi như giả thiết.

**Hướng đi:**

- Cân bằng tĩnh điện cho |q|V_AB/d = mg.
- Khi tắt trường, tốc độ giới hạn cho 6πηrv_t = mg để suy r.
- Ghép hai phép đo loại r, sau đó dùng giả thiết lượng tử hóa để suy số nguyên n.

**(a)** Khối lượng $m=4\pi\rho r^3/3$ cho công thức đã nêu. **(b)**

$$
\begin{aligned}
6\pi\eta rv_t&=\frac{4\pi\rho r^3g}{3},\\
r^2&=\frac{9\eta v_t}{2\rho g},\\
|q|&=\frac{4\pi\rho g d}{3V_{AB}}
\left(\frac{9\eta v_t}{2\rho g}\right)^{3/2}\\
&=\frac{18\pi d}{V_{AB}}
\sqrt{\frac{\eta^3v_t^3}{2\rho g}}.
\end{aligned}
$$

**(c)–(e)** Các điện tích thực âm. Từ tỷ số độ lớn so với giọt 2, các số electron là 3,1,5,2:

| Giọt | q ($10^{-19}$ C) | n | e suy ra ($10^{-19}$ C) |
| --- | --- | --- | --- |
| 1 | −4,79 | 3 | 1,60 |
| 2 | −1,59 | 1 | 1,59 |
| 3 | −8,09 | 5 | 1,62 |
| 4 | −3,23 | 2 | 1,62 |

Giá trị trung bình e ≈ $1.61\times10^{-19}$ C. Các tỷ số không nguyên hoàn toàn vì dữ liệu có sai số đo và làm tròn. Việc lấy giọt nhỏ nhất bằng một electron là giả thiết được cho trong câu hỏi, không phải kết luận từ riêng bốn hàng dữ liệu.
:::

## Bài tập nâng cao

::: exercise 23.80 ••• CALC
Vành khăn trong mặt xy, tâm tại gốc, bán kính trong a, ngoài b, mật độ mặt σ. **(a)** Tìm V ở mọi điểm trục z, mốc vô hạn. **(b)** Lấy đạo hàm tìm trường. **(c)** Cho a tiến về 0 và b ra vô hạn, chứng tỏ trường trở thành trường mặt phẳng vô hạn. **(d)** Với a = 5,00 cm, b = 10,0 cm, tổng điện tích +1,00 µC, tìm V ở gốc. **(e)** Hạt m = 1,00 g, q = +1,00 µC ở gốc được đẩy lệch rất nhẹ, đi dọc z. Tìm tốc độ cuối ở xa. Khối lượng vành lớn hơn nhiều khối lượng hạt.
:::

![Hình P23.80: Vành khăn tích điện trong xy và trục đối xứng z](img/young-23/hinh-p23-80.png)

<!-- detailed-solution:23.80 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Vành được chia thành vòng bán kính r từ a đến b, dq = 2πσr dr.

**Hướng đi:**

- Tích phân điện thế từng vòng, rồi lấy âm đạo hàm theo z.
- Giới hạn mặt vô hạn áp dụng cho trường. Mốc thế ở vô hạn không còn hữu hạn khi nguồn kéo dài vô hạn.
- Hạt dương ở tâm vành dương là cân bằng không bền theo z. Độ giảm qV chuyển thành động năng khi lệch khỏi tâm.

**(a)**

$$
\begin{aligned}
V(z)&=2\pi k\sigma\int_a^b
\frac{r\,dr}{\sqrt{z^2+r^2}}\\
&=\frac{\sigma\sqrt{z^2+b^2}}{2\varepsilon_0}\\
&\quad-\frac{\sigma\sqrt{z^2+a^2}}{2\varepsilon_0}.
\end{aligned}
$$

**(b)** Trường chỉ có thành phần z:

$$
\begin{aligned}
E_z&=\frac{\sigma z}{2\varepsilon_0\sqrt{z^2+a^2}}\\
&\quad-\frac{\sigma z}{2\varepsilon_0\sqrt{z^2+b^2}}.
\end{aligned}
$$

**(c)** Khi a → 0,b → ∞, z khác không, thành phần trở thành σ/(2$\varepsilon_0$) ở z > 0 và −σ/(2$\varepsilon_0$) ở z < 0. **(d)** Dùng σ = Q/[π(b² − a²)]:

$$
V(0)=\frac{2kQ}{a+b}=1.20\times10^5\,\mathrm V.
$$

**(e)** Ở xa V → 0, nên $mv_\infty^2/2=qV(0)$ cho v∞ = 15,5 m/s. Nếu không có lệch dù nhỏ và hạt ở chính xác z = 0 với v = 0, nó vẫn ở cân bằng. “Đẩy lệch rất nhẹ” chọn nhánh rời điểm cân bằng không bền.
:::

::: exercise 23.81 ••• BIO
Tế bào tim được mô hình hóa thành vỏ trụ dài 100 µm, đường kính ngoài 20,0 µm, màng dày 1,00 µm. Ion kali chuyển qua màng, để điện tích dương mặt ngoài và âm mặt trong. Khi nghỉ, thế bên trong thấp hơn ngoài 90,0 mV. **(a)** Nếu tổng điện tích tế bào bằng không, tìm độ lớn điện tích mỗi mặt. Bỏ hiệu ứng đầu trụ. **(b)** Tìm trường ngay trong màng sát mặt trong. **(c)** Khi khử cực, ion natri đi qua kênh làm thế trong cao hơn ngoài 20,0 mV. Coi điện tích chuyển từ mặt ngoài sang trong, tìm lượng điện tích chuyển. **(d)** Nếu do Na⁺ thực hiện, tìm số ion.
:::

![Hình P23.81: Hai mặt tích điện trái dấu của màng tế bào hình trụ](img/young-23/hinh-p23-81.png)

<!-- detailed-solution:23.81 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Bán kính a = 9,00 µm, b = 10,0 µm, chiều dài ℓ = 100 µm. Điện tích hai mặt bằng độ lớn, trái dấu.

**Hướng đi:**

- Màng dùng mô hình điện cực trụ đồng trục, |ΔV| = |λ| ln(b/a)/(2π$\varepsilon_0$).
- Điện tích tổng một mặt bằng λℓ. Trường sát mặt trong có r = a, vẫn ở phần màng, không ở chất lỏng bên trong.
- Chuyển thế trong từ −90 mV lên +20 mV cần thay đổi 110 mV, không chỉ 20 mV.

Đặt hệ số $C_\mathrm{trụ}=2\pi\varepsilon_0\ell/\ln(b/a)$:

$$
\begin{aligned}
|Q_{\mathrm{nghỉ}}|&=C_\mathrm{trụ}(0.0900)\\
&=4.75\times10^{-15}\,\mathrm C,\\
E(a^+)&=\frac{0.0900}{a\ln(b/a)}\\
&=94.9\,\mathrm{kV/m},\\
\Delta Q&=C_\mathrm{trụ}(0.110)\\
&=5.81\times10^{-15}\,\mathrm C,\\
N_{\mathrm{Na^+}}&=\Delta Q/e\\
&\approx3.63\times10^4.
\end{aligned}
$$

Trường nghỉ hướng từ mặt ngoài dương về mặt trong âm. Điện tích dương chuyển vào làm đảo dấu hiệu điện thế như mô tả.
:::

::: exercise 23.82 ••• CALC
Ống cách điện rỗng, thành mỏng R, dài L, có tổng Q đều trên mặt bên. **(a)** Tìm V ở mọi điểm trục ống, gốc tại tâm ống, mốc vô hạn. **(b)** Chứng tỏ khi L nhỏ hơn nhiều R, kết quả trở thành thế trục vòng bán kính R. **(c)** Từ V tìm trường ở mọi điểm trục.
:::

<!-- detailed-solution:23.82 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Chọn z dọc trục, phần vòng tại ζ mang dq = (Q/L)dζ, với −L/2 ≤ ζ ≤ L/2.

**Hướng đi:**

- Mỗi vòng có thế trục k dq chia khoảng cách $\sqrt{R^2+(z-\zeta)^2}$.
- Tích phân theo ζ. Đổi biến u = z − ζ cho nguyên hàm logarit.
- Đối xứng cho trường trên trục chỉ theo z, nên đạo hàm V đủ tìm thành phần ấy.

Đặt h = L/2 và $r_\pm=\sqrt{R^2+(z\pm h)^2}$. Khi đó:

$$
\begin{aligned}
V(z)&=\frac{kQ}{L}\int_{-h}^h
\frac{d\zeta}{\sqrt{R^2+(z-\zeta)^2}}\\
&=\frac{kQ}{L}\ln\frac{z+h+r_+}{z-h+r_-},\\
E_z&=\frac{kQ}{L}\left(\frac1{r_-}-\frac1{r_+}\right).
\end{aligned}
$$

Các biểu thức dưới logarit dương vì R > 0. **(b)** Khi L ≪ R, mọi vòng nằm gần tâm theo chiều trục và tích phân có độ dài L nhân gần một giá trị không đổi, nên $V\approx kQ/\sqrt{R^2+z^2}$. Đây là thế trục vòng. Trường ở tâm ống bằng không vì r₊ = r₋.
:::

::: exercise 23.83 ••• CP
Va chạm hạt nhân thường lệch tâm hơn thẳng tâm. Hạt α ở Bài 23.75 có động lượng đầu p₀, mômen động lượng đối với hạt nhân chì đứng yên L = p₀b. Tìm khoảng cách gần nhất với b = $1.00\times10^{-12}$ m, rồi b = $1.00\times10^{-13}$ m và $1.00\times10^{-14}$ m.
:::

<!-- detailed-solution:23.83 -->
::: solution Chi tiết
**Tóm tắt đề bài:** K₀ = 9,50 MeV, tương tác đẩy Coulomb. Có mômen động lượng khác không nên ở điểm gần nhất hạt vẫn có vận tốc tiếp tuyến.

**Hướng đi:**

- Tại r_min, thành phần vận tốc xuyên tâm bằng không, còn thành phần tiếp tuyến được xác định bởi L = mrv_t.
- Bảo toàn năng lượng gồm cả động năng tiếp tuyến, không đặt toàn tốc độ bằng không như va chạm thẳng tâm.
- Dùng p₀² = 2mK₀ để thay L bằng b và giải phương trình bậc hai theo r.

Đặt A = k(2e)(82e), $r_0=A/K_0$, chính là khoảng cách thẳng tâm ở Bài 23.75:

$$
\begin{aligned}
K_0&=A/r+L^2/(2mr^2),\\
r^2-r_0r-b^2&=0,\\
r_{\min}&=\frac{r_0+\sqrt{r_0^2+4b^2}}2.
\end{aligned}
$$

Với r₀ = $2.49\times10^{-14}$ m, các khoảng cách gần nhất theo thứ tự là **$1.01\times10^{-12}$ m, $1.13\times10^{-13}$ m và $2.84\times10^{-14}$ m**. Nghiệm âm không phải khoảng cách. Khi b → 0, kết quả trở về r₀, đúng va chạm thẳng tâm.
:::

## Bài đọc và câu hỏi kiểu MCAT

### Phân tích vật liệu bằng ion

Phổ tán xạ ngược Rutherford, viết tắt RBS, khảo sát cấu trúc và thành phần vật liệu bằng chùm ion năng lượng cao, thường là heli. Chùm được bắn vào mẫu. Phân bố góc và năng lượng của các ion bị tán xạ bởi nguyên tử mẫu cung cấp thông tin về thành phần mẫu.

Một máy gia tốc tĩnh điện tandem có thể tạo chùm này. Ion heli âm He⁻ bắt đầu ở điện thế 0, được hút đến vùng giữa có điện thế dương cao. Trường trong ống gia tốc được coi không đổi. Ở giữa, các electron bị tách khỏi ion, làm nó thành He²⁺. Ion dương sau đó bị vùng giữa đẩy đến đầu kia có điện thế 0, tiếp tục nhận động năng. Các câu sau dùng mô hình ấy, coi động năng đầu và phần năng lượng thay đổi do quá trình tách electron nhỏ so với động năng gia tốc.

::: exercise 23.84
Muốn ion heli sau máy có động năng 3,0 MeV, điện thế vùng giữa phải bằng bao nhiêu? **(a)** −3,0 MV, **(b)** +3,0 MV, **(c)** +1,5 MV, hay **(d)** +1,0 MV?
:::

<!-- detailed-solution:23.84 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Ion đầu mang −e, sau vùng giữa mang +2e, hai đầu máy ở V = 0.

**Hướng đi:**

- Chặng đầu ion âm đến +V nhận động năng eV.
- Chặng sau ion +2e đi từ +V về 0 nhận thêm 2eV.
- Cộng năng lượng hai chặng, không chỉ tính chặng sau.

K = 3eV. Để K = 3,0 MeV, cần V = +1,0 MV. Chọn **(d)**.
:::

::: exercise 23.85
Ion He²⁺ đến gần cỡ 10 fm từ tâm hạt nhân mẫu có thể gây phản ứng hạt nhân thay vì chỉ tán xạ. Ion có K = 3,0 MeV đi thẳng vào hạt nhân được coi cố định. Điện tích hạt nhân nhỏ nhất để ion không đến gần hơn 10 fm là **(a)** 2e, **(b)** 11e, **(c)** 20e, hay **(d)** 22e?
:::

<!-- detailed-solution:23.85 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hạt α mang +2e, hạt nhân mang +Ze với Z nguyên.

**Hướng đi:**

- Điểm quay đầu cần thế năng Coulomb ít nhất bằng động năng tại r = 10 fm.
- Tìm ngưỡng Z rồi lấy số nguyên nhỏ nhất không thấp hơn ngưỡng.

$$
\begin{aligned}
\frac{2kZe^2}{r}&\ge K,\\
Z&\ge\frac{Kr}{2ke^2}\\
&\approx10.4.
\end{aligned}
$$

Z nhỏ nhất là 11, nên chọn **(b)**. Làm tròn ngưỡng xuống 10 sẽ không thỏa điều kiện ngăn đến gần hơn.
:::

::: exercise 23.86
Máy tandem điển hình có điện thế giữa cực đại 6,0 MV. Khoảng cách từ một đầu ống đến vùng giữa là 12 m. Độ lớn trường trung bình là **(a)** 41.000 V/m, **(b)** 250.000 V/m, **(c)** 500.000 V/m, hay **(d)** 6.000.000 V/m?
:::

<!-- detailed-solution:23.86 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Một nửa ống có chênh thế 6,0 MV trên chiều dài 12 m.

**Hướng đi:**

- Trường trung bình dọc đường lấy độ lớn chênh thế chia chiều dài.
- Không dùng toàn chiều dài hai nửa máy cho chênh thế một nửa.

$$
E_{\mathrm{tb}}=\frac{6.0\times10^6}{12}
=5.0\times10^5\,\mathrm{V/m}.
$$

Chọn **(c)**.
:::
