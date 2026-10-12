<!-- Source: Problems22.45–22.66, printed744–746, PDF764–766. -->

### Phân bố điện tích không đều

::: exercise 22.45 ••• CALC
Vỏ cầu cách điện có bán kính trong a, ngoài b. Trong vật liệu, mật độ thể tích $\rho(r)=\alpha/r$ với α dương. **(a)** Tìm độ lớn trường ở a < r < b theo α và a. **(b)** Đặt nguồn điểm q tại tâm hốc. Tìm dấu và độ lớn q để trường ở a < r < b không đổi, rồi tìm giá trị trường ấy.
:::

<!-- detailed-solution:22.45 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mật độ đối xứng cầu giảm theo 1/r trong lớp a < r < b.

**Hướng đi:**

- Tích phân $dQ=\rho(s)4\pi s^2ds$ vì mật độ không đều.
- Gauss cho $E_r=kQ_{\mathrm{trong}}/r^2$. Nguồn ở tâm có thể triệt tiêu số hạng phụ thuộc $1/r^2$.

**(a)**

$$
\begin{aligned}
Q_{\mathrm{trong}}&=4\pi\alpha\int_a^r s\,ds\\
&=2\pi\alpha(r^2-a^2),\\
E_r&=\frac{\alpha}{2\varepsilon_0}
\left(1-\frac{a^2}{r^2}\right).
\end{aligned}
$$

**(b)** Thêm q cho:

$$
E_r=\frac{\alpha}{2\varepsilon_0}
+\frac{k(q-2\pi\alpha a^2)}{r^2}.
$$

Chọn $q=+2\pi\alpha a^2$ làm số hạng sau bằng không. Trường khi ấy có độ lớn α/(2$\varepsilon_0$), hướng ra ở toàn vùng vật liệu.
:::

::: exercise 22.46 •• CP — Mô hình nguyên tử Thomson
Trong mô hình Thomson đầu thế kỷ XX, electron âm nằm trong một khối cầu vật chất dương, giống các hạt chocolate trong khối bột bánh. Xét một electron khối lượng m, điện tích −e, coi là nguồn điểm, nằm trong cầu dương đều có điện tích +e và bán kính R. **(a)** Giải thích vì sao cân bằng ở tâm. **(b)** Giả sử vật chất dương gần như không cản chuyển động, chứng tỏ khi lệch tâm ít hơn R, electron dao động điều hòa và tìm tần số. Ôn dạng lực dao động ở mục 14.2. **(c)** Mô hình giả sử tần số ánh sáng phát ra bằng tần số dao động electron. Để phát ánh sáng đỏ $4.57\times10^{14}$ Hz, R phải bằng bao nhiêu? So với kích thước nguyên tử thật cỡ $10^{-10}$ m. **(d)** Nếu lệch ban đầu lớn hơn R, electron có dao động không và có điều hòa không? Việc phát hiện hạt nhân nhỏ cỡ $10^{-14}$–$10^{-15}$ m đã bác bỏ giả thiết điện tích dương trải đều trong cả thể tích nguyên tử.
:::

<!-- detailed-solution:22.46 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Electron âm chuyển động trong trường của cầu dương đều, không có lực cản trong mô hình.

**Hướng đi:**

- Trong cầu, trường tỷ lệ với vector vị trí. Nhân −e tạo lực phục hồi tỷ lệ với độ lệch.
- So sánh với $\vec F=-m\omega^2\vec r$ để xác định tần số.

**(a)** Tâm có trường bằng không. Lệch sang phía nào, electron cũng bị hút về tâm. **(b)**

$$
\begin{aligned}
\vec E&=\frac{ke}{R^3}\vec r,\\
\vec F&=-\frac{ke^2}{R^3}\vec r,\\
f&=\frac1{2\pi}\sqrt{\frac{ke^2}{mR^3}}.
\end{aligned}
$$

**(c)** Đảo biểu thức tần số, dùng khối lượng electron:

$$
\begin{aligned}
R&=\left(\frac{ke^2}{4\pi^2m_ef^2}\right)^{1/3}\\
&=3.13\times10^{-10}\,\mathrm m.
\end{aligned}
$$

Giá trị cùng bậc kích thước nguyên tử. Điều đó chưa chứng minh mô hình đúng. **(d)** Nếu thả từ nghỉ ngoài cầu, lực hút vẫn đưa electron về và xuyên qua tâm rồi sang phía đối diện, nên có dao động trong mô hình không cản. Tuy nhiên ngoài cầu lực tỷ lệ với $1/r^2$, không tỷ lệ với độ lệch, nên toàn chuyển động không điều hòa. Phát hiện hạt nhân cho thấy điện tích dương tập trung trong vùng nhỏ, thay vì trải đều như giả thiết Thomson.
:::

::: exercise 22.47 •• CALC
Phân bố cầu đối xứng có $\rho(r)=\rho_0(1-r/R)$ khi 0 ≤ r ≤ R, bằng không khi r ≥ R, với $\rho_0=3Q/(\pi R^3)>0$. **(a)** Chứng tỏ điện tích tổng Q. **(b)** Chứng tỏ trường ngoài giống nguồn Q ở tâm. **(c)** Tìm trường trong. **(d)** Vẽ độ lớn trường theo r. **(e)** Tìm vị trí và giá trị trường cực đại.
:::

<!-- detailed-solution:22.47 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mật độ giảm tuyến tính từ ρ₀ ở tâm xuống không tại R.

**Hướng đi:**

- Tích phân các lớp cầu để tìm điện tích được bao, rồi áp dụng Gauss.
- Lấy đạo hàm trường trong theo r để tìm cực đại, vì ngoài cầu trường giảm theo $1/r^2$.

$$
\begin{aligned}
Q_{\mathrm{trong}}(r)&=4\pi\rho_0\int_0^r
\left(s^2-\frac{s^3}{R}\right)ds\\
&=4\pi\rho_0\left(\frac{r^3}{3}-\frac{r^4}{4R}\right).
\end{aligned}
$$

Thay r = R cho $Q_{\mathrm{tổng}}=\pi\rho_0R^3/3=Q$. Với u = r/R, trường trong là:

$$
E=\frac{kQ}{R^2}(4u-3u^2).
$$

Trường ngoài là kQ/r², hướng ra. Đạo hàm theo u bằng hệ số dương nhân (4 − 6u), nên:

$$
\begin{aligned}
r_{\max}&=2R/3,\\
E_{\max}&=\frac{4kQ}{3R^2}.
\end{aligned}
$$

Đồ thị tăng từ không, đạt cực đại trong cầu, giảm về kQ/R² ở mặt rồi tiếp tục giảm bên ngoài.

![Đồ thị trường của cầu có mật độ giảm tuyến tính theo bán kính](img/young-22/loi-giai-22-47.svg)
:::

::: exercise 22.48 ••
**(a)** Cần bao nhiêu electron dư phân bố đều trong quả cầu nhựa cô lập đường kính 30,0 cm để trường ngay ngoài mặt có độ lớn 1390 N/C? **(b)** Trường cách mặt 10,0 cm ra ngoài bằng bao nhiêu?
:::

<!-- detailed-solution:22.48 -->
::: solution Chi tiết
**Tóm tắt đề bài:** R = 0,150 m, nguồn âm do electron dư.

**Hướng đi:**

- Trường ngoài cho $|Q|=ER^2/k$, số electron bằng |Q|/e.
- Điểm thứ hai cách tâm 0,250 m, dùng cùng tổng Q.

**(a)** $N=2.17\times10^{10}$ electron. **(b)** $E=1390(0.150/0.250)^2=500$ N/C, hướng về tâm.
:::

::: exercise 22.49 •• CALC
Trụ cách điện rất dài bán kính R có mật độ dương $\rho(r)=\alpha(1-r/R)$, đối xứng trụ, α có đơn vị C/m³. Suy ra E(r) ở r < R và r > R. Hai kết quả có khớp tại r = R không?
:::

<!-- detailed-solution:22.49 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mật độ thay đổi theo khoảng cách đến trục.

**Hướng đi:**

- Lớp trụ mỏng dài ℓ có thể tích $2\pi s\ell\,ds$, không phải thể tích lớp cầu.
- Dùng Gauss trụ sau khi tích phân điện tích theo bán kính.

$$
\begin{aligned}
\lambda_{\mathrm{trong}}(r)&=2\pi\alpha
\int_0^r\left(s-\frac{s^2}{R}\right)ds,\\
E_{\mathrm{trong}}&=\frac{\alpha}{\varepsilon_0}
\left(\frac r2-\frac{r^2}{3R}\right),\\
\lambda_{\mathrm{tổng}}&=\pi\alpha R^2/3,\\
E_{\mathrm{ngoài}}&=\frac{\alpha R^2}{6\varepsilon_0r}.
\end{aligned}
$$

Tại R, cả hai bằng αR/(6$\varepsilon_0$). Trường hướng ra và liên tục tại mặt trụ.
:::

::: exercise 22.50 •• CALC
Cầu cách điện đặc bán kính R có mật độ $\rho(r)=\rho_0(1-r/R)>0$ trong cầu, đối xứng cầu. **(a)** Suy ra E(r) bên trong. **(b)** Bên ngoài. **(c)** Tìm r làm trường cực đại.
:::

<!-- detailed-solution:22.50 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cùng dạng mật độ như Bài 22.47, nhưng ρ₀ được cho trực tiếp.

**Hướng đi:**

- Tích phân $4\pi s^2\rho(s)ds$ để tìm điện tích được bao.
- Dùng Gauss cầu rồi đạo hàm nhánh trong để tìm cực đại.

$$
\begin{aligned}
E_{\mathrm{trong}}&=\frac{\rho_0}{\varepsilon_0}
\left(\frac r3-\frac{r^2}{4R}\right),\\
Q_{\mathrm{tổng}}&=\pi\rho_0R^3/3,\\
E_{\mathrm{ngoài}}&=\frac{\rho_0R^3}{12\varepsilon_0r^2},\\
r_{\max}&=2R/3.
\end{aligned}
$$

Hai nhánh khớp tại r = R và trường hướng ra.
:::

::: exercise 22.51 • CALC — Tấm có mật độ không đều
Tấm cách điện dày 2d có hai mặt x = ±d, song song mặt yz. Kích thước theo y,z rất lớn so với d, coi vô hạn. Mật độ $\rho(x)=\rho_0(x/d)^2$ với ρ₀ dương. Dùng Gauss tìm độ lớn và hướng trường ở mọi điểm.
:::

<!-- detailed-solution:22.51 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mật độ chẵn theo x, trường chỉ có thành phần x và đổi dấu qua mặt trung tâm.

**Hướng đi:**

- Với x > 0 trong tấm, chọn hộp Gauss hai đáy ±x có diện tích A.
- Điện thông là 2AE(x), điện tích được bao là $2A\int_0^x\rho(s)ds$.
- Ngoài tấm, cận tích phân dừng ở d vì không có thêm điện tích.

Trong tấm, kể cả x âm:

$$
E_x=\frac{\rho_0x^3}{3\varepsilon_0d^2}.
$$

Phía x > d, $E_x=\rho_0d/(3\varepsilon_0)$. Phía x < −d, $E_x=-\rho_0d/(3\varepsilon_0)$. Trường bằng không ở tâm, hướng ra xa mặt phẳng trung tâm, liên tục ở hai biên.
:::

::: exercise 22.52 • CALC
Mật độ cầu đối xứng là $\rho(r)=\rho_0[1-4r/(3R)]$ khi r ≤ R và bằng không khi r ≥ R, với ρ₀ dương. **(a)** Tìm tổng điện tích. **(b)** Tìm trường ở r ≥ R. **(c)** Tìm trường ở r ≤ R. **(d)** Vẽ độ lớn trường. **(e)** Tìm vị trí và giá trị trường cực đại.
:::

<!-- detailed-solution:22.52 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mật độ dương gần tâm và âm khi r > 3R/4.

**Hướng đi:**

- Cộng điện tích với dấu bằng tích phân lớp cầu. Không thay mật độ bằng độ lớn của nó.
- Gauss cho trường ngoài từ tổng điện tích, còn trường trong từ điện tích từng bán kính.

$$
\begin{aligned}
Q_{\mathrm{trong}}(r)&=\frac{4\pi\rho_0}{3}
\left(r^3-\frac{r^4}{R}\right),\\
Q_{\mathrm{tổng}}&=0,\\
E_{\mathrm{ngoài}}&=0,\\
E_{\mathrm{trong}}&=\frac{\rho_0r}{3\varepsilon_0}
\left(1-\frac rR\right).
\end{aligned}
$$

Trong cầu trường hướng ra, dù mật độ ở phần ngoài âm. Lấy đạo hàm r(1 − r/R) cho cực đại tại r = R/2, với $E_{\max}=\rho_0R/(12\varepsilon_0)$. Đồ thị bằng không ở tâm và mặt, đạt cực đại giữa hai vị trí ấy, rồi bằng không ngoài cầu.

![Đồ thị trường của phân bố cầu có điện tích tổng bằng không](img/young-22/loi-giai-22-52.svg)
:::

::: exercise 22.53 •
**(a)** Cầu cách điện bán kính a có mật độ đều ρ, tâm ở vector $\vec b$. Chứng tỏ trường trong cầu là $\vec E=\rho(\vec r-\vec b)/(3\varepsilon_0)$. **(b)** Cầu lớn bán kính R có hốc cầu bán kính a, tâm hốc lệch tâm cầu lớn một khoảng b, với a < b < R và hốc nằm trọn trong cầu. Vật liệu còn lại có mật độ đều ρ. Tìm độ lớn, hướng trường trong hốc và chứng tỏ trường đều. Gợi ý: Chồng chất với kết quả (a).
:::

![Hình P22.53: Hốc cầu lệch tâm trong quả cầu cách điện](img/young-22/hinh-p22-53.png)

<!-- detailed-solution:22.53 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Chọn gốc tại tâm cầu lớn, vector b hướng đến tâm hốc.

**Hướng đi:**

- Trường trong cầu đều phụ thuộc độ lệch so với **tâm riêng** của cầu.
- Tạo hốc bằng chồng cầu lớn mật độ +ρ với cầu nhỏ mật độ −ρ, rồi cộng vector trường ở điểm trong hốc.

**(a)** Khoảng cách vector từ tâm cầu nhỏ đến điểm là $\vec r-\vec b$. Kết quả cầu đều cho biểu thức cần chứng minh. **(b)**

$$
\begin{aligned}
\vec E&=\frac{\rho\vec r}{3\varepsilon_0}
-\frac{\rho(\vec r-\vec b)}{3\varepsilon_0}\\
&=\frac{\rho\vec b}{3\varepsilon_0}.
\end{aligned}
$$

Độ lớn là ρb/(3$\varepsilon_0$) nếu ρ dương, hướng từ tâm cầu lớn đến tâm hốc. Không còn phụ thuộc r nên trường đều trong toàn hốc. Điều kiện hốc nằm trọn còn đòi hỏi a + b < R.
:::

::: exercise 22.54 •
Trụ cách điện đặc rất dài bán kính R có hốc trụ xuyên dọc, bán kính a. Trục hốc lệch trục trụ một khoảng b, với a < b < R và hốc nằm trọn trong trụ. Vật liệu còn lại có mật độ đều ρ. Tìm độ lớn, hướng trường trong hốc và chứng tỏ trường đều. Gợi ý: Xem Bài 22.53.
:::

![Hình P22.54: Hốc trụ lệch trục trong trụ tích điện](img/young-22/hinh-p22-54.png)

<!-- detailed-solution:22.54 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Vector b nối từ trục trụ lớn đến trục hốc trong mặt cắt ngang.

**Hướng đi:**

- Chồng trụ lớn +ρ với trụ nhỏ −ρ để tạo hốc.
- Trường trong trụ đều là $\rho\vec r_\perp/(2\varepsilon_0)$, khác hệ số 1/3 của cầu.

$$
\begin{aligned}
\vec E&=\frac{\rho\vec r_\perp}{2\varepsilon_0}
-\frac{\rho(\vec r_\perp-\vec b)}{2\varepsilon_0}\\
&=\frac{\rho\vec b}{2\varepsilon_0}.
\end{aligned}
$$

Trường đều, độ lớn ρb/(2$\varepsilon_0$), hướng đến trục hốc khi ρ dương. Hốc nằm trọn cần a + b < R.
:::

### Bài tập dữ liệu và ứng dụng

::: exercise 22.55 •• DATA
Thí nghiệm thứ nhất đo trường ở khoảng cách r đến dây đều dài ℓ với ℓ ≫ r. Thí nghiệm thứ hai đo trường ở r > R của cầu cách điện đều bán kính R = 8,00 mm. Bảng cho hai bộ dữ liệu nhưng chưa ghi bộ nào ứng với nguồn nào. Với mỗi bộ, vẽ Er² theo r và Er theo r. **(a)** Xác định nguồn của bộ A và B, giải thích. **(b)** Dùng đồ thị tìm λ của dây và ρ của cầu.

| r (cm) | E_A ($10^5$ N/C) | E_B ($10^5$ N/C) |
| --- | --- | --- |
| 1,00 | 2,72 | 5,45 |
| 1,50 | 1,79 | 2,42 |
| 2,00 | 1,34 | 1,34 |
| 2,50 | 1,07 | 0,861 |
| 3,00 | 0,902 | 0,605 |
| 3,50 | 0,770 | 0,443 |
| 4,00 | 0,677 | 0,335 |
:::

<!-- detailed-solution:22.55 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Bảy cặp khoảng cách và trường, bán kính cầu 0,00800 m.

**Hướng đi:**

- Dây dài có E ∝ 1/r nên Er gần hằng số.
- Ngoài cầu có E ∝ 1/r² nên Er² gần hằng số.
- Đổi r sang m trước khi suy ra hằng số và các mật độ.

![Bốn đồ thị Er và Er² cho hai bộ dữ liệu A, B](img/young-22/loi-giai-22-55.svg)

**(a)** A có Er gần $2.70\times10^3$ N m/C, nên là dây. B có Er² gần 54,1 N m²/C, nên là cầu. **(b)** Lấy trung bình những tích đã biến đổi để giảm ảnh hưởng làm tròn dữ liệu:

$$
\begin{aligned}
\lambda&=\frac{Er}{2k}\approx1.50\times10^{-7}\,\mathrm{C/m},\\
Q&=\frac{Er^2}{k},\\
\rho&=\frac{3Q}{4\pi R^3}\\
&\approx2.81\times10^{-3}\,\mathrm{C/m^3}.
\end{aligned}
$$

Đây là độ lớn các mật độ vì bảng chỉ cho độ lớn trường. Muốn xác định dấu cần biết hướng trường đo được.
:::

::: exercise 22.56 •• DATA
Đo trường tại r < R trong một cầu cách điện đều có mật độ ρ. Dựa vào đồ thị Hình P22.56, tính ρ.
:::

![Hình P22.56: Trường tăng tuyến tính theo khoảng cách trong cầu](img/young-22/hinh-p22-56.png)

<!-- detailed-solution:22.56 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Đồ thị cho E ≈ $7.5\times10^4$ N/C tại r = 10 mm.

**Hướng đi:**

- Trong cầu đều, $E=|\rho|r/(3\varepsilon_0)$.
- Hệ số góc E/r của đồ thị cho độ lớn mật độ. Đổi mm sang m.

$$
\begin{aligned}
|\rho|&=3\varepsilon_0\frac{7.5\times10^4}{0.010}\\
&\approx2.0\times10^{-4}\,\mathrm{C/m^3}.
\end{aligned}
$$

Nếu trường hướng ra, ρ dương. Đồ thị độ lớn đơn độc chưa xác định dấu.
:::

::: exercise 22.57 •• DATA
Cầu bán kính R = 6,00 mm có mật độ không đều theo Hình P22.57. Tính trường tại r bằng **(i)** 1,00 mm, **(ii)** 3,00 mm, **(iii)** 5,00 mm, **(iv)** 7,00 mm.
:::

![Hình P22.57: Mật độ theo ba vùng bán kính, lần lượt 10, 4 và −2 µC/m³](img/young-22/hinh-p22-57.png)

<!-- detailed-solution:22.57 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Các lớp 0–2 mm, 2–4 mm và 4–6 mm có mật độ 10, 4 và −2 µC/m³.

**Hướng đi:**

- Cộng điện tích của từng lớp nằm bên trong điểm khảo sát, giữ dấu mật độ.
- Lớp từ a đến b có điện tích $4\pi\rho(b^3-a^3)/3$.
- Sau đó dùng $E_r=kQ_{\mathrm{trong}}/r^2$.

**(i)** Chỉ có phần lớp đầu: E = 376 N/C. **(ii)** Bao hết lớp đầu và phần lớp thứ hai đến 3 mm: E = 653 N/C. **(iii)** Bao hai lớp đầu và phần lớp âm đến 5 mm: E = 274 N/C. Ba trường đều hướng ra.

**(iv)** Điện tích tổng tỷ lệ với:

$$
\begin{aligned}
10(2^3)&+4(4^3-2^3)\\
&-2(6^3-4^3)=0.
\end{aligned}
$$

Vì thế trường ở 7 mm bằng không. Các số trong phép so cuối dùng cùng đơn vị mm và µC/m³, nên chỉ dùng để xác nhận tổng bằng không. Khi tính giá trị trường, đã đổi sang SI.
:::

::: exercise 22.58 •• BIO
Khi ong mật bay, không khí lấy bớt electron khỏi lông, làm ong dương. Hoa âm có thể kéo phấn nhảy lên ong dù ong chưa chạm phấn. **(a)** Ước lượng đường kính đĩa giữa hoa cúc. **(b)** Ong mất 75.000 electron có điện tích bao nhiêu? **(c)** Ong đậu ở một mép đĩa, tìm trường của ong tại mép đối diện, coi ong là vỏ cầu mỏng có điện tích đều. **(d)** Một hạt phấn cần lực 10 pN để rời nhị. Ước lượng điện tích hạt phấn ở mép xa để nó rời nhị và nhảy đến ong.
:::

<!-- detailed-solution:22.58 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Số electron bị lấy bớt cho điện tích dương. Đường kính hoa cần được ước lượng.

**Hướng đi:**

- Chọn và nêu rõ giả thiết kích thước, vì đề không cho một đường kính duy nhất.
- Ngoài vỏ cầu đều, dùng trường nguồn điểm. Hạt phấn phải âm để chịu lực hút về ong.

**(a)** Chọn d ≈ 1 cm làm ước lượng cho đĩa giữa một bông cúc nhỏ. **(b)** $Q=75000e=1.20\times10^{-14}$ C. **(c)**

$$
\begin{aligned}
E&\approx kQ/d^2=1.08\,\mathrm{N/C},\\
|q_{\mathrm{phấn}}|&\approx F/E\\
&=9.3\times10^{-12}\,\mathrm C.
\end{aligned}
$$

**(d)** Điện tích cần xấp xỉ **−9,3 pC** với ước lượng kích thước đã chọn. Nếu chọn đường kính d khác, trường tỷ lệ 1/d² và độ lớn điện tích phấn cần tỷ lệ d². Không nên coi số ước lượng là phép đo chính xác.
:::

::: exercise 22.59 •• CP CALC
Trụ cách điện rất dài bán kính $R_c$ có mật độ $\rho(r)=(1-r/R_c)\rho_0$. Hạt điện tích −Q, khối lượng M quay tròn quanh trụ ở bán kính $R_o>R_c$. **(a)** Tìm mật độ dài λ của trụ. **(b)** Tìm chu kỳ theo $R_o$. Gợi ý: Dùng Gauss tìm lực điện đóng vai trò hướng tâm.
:::

<!-- detailed-solution:22.59 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hạt âm chuyển động ngoài trụ dương có mật độ không đều.

**Hướng đi:**

- Tích phân tiết diện để tìm λ trước khi dùng trường ngoài trụ.
- Lực Coulomb là chính lực hướng tâm, không cộng thêm một lực hướng tâm riêng.

$$
\begin{aligned}
\lambda&=2\pi\rho_0\int_0^{R_c}
\left(r-\frac{r^2}{R_c}\right)dr\\
&=\pi\rho_0R_c^2/3,\\
\frac{Mv^2}{R_o}&=\frac{Q\lambda}{2\pi\varepsilon_0R_o},\\
T&=2\pi R_o\sqrt{\frac{2\pi\varepsilon_0M}{Q\lambda}}.
\end{aligned}
$$

Tốc độ không phụ thuộc bán kính quỹ đạo trong mô hình này, nên chu kỳ tỷ lệ với $R_o$.
:::

::: exercise 22.60 •• CP
**(a)** Chứng tỏ thành phần lực điện vuông góc một mặt phẳng mang mật độ đều σ là $F_\perp=\sigma\Phi_E$, với Φ là điện thông của **trường ngoài** qua mặt đó. **(b)** Một bán cầu cách điện bán kính R mang điện tích Q đều trên mặt tròn phẳng, nằm phía trên mặt phẳng rất lớn có mật độ đều σ. Trục bán cầu thẳng đứng. Khối lượng M phải bằng bao nhiêu để đứng yên? **(c)** Nếu mật độ trên mặt tròn và mặt lớn đều 100 µC/m², R = 3,00 cm, M = 100 g, gia tốc hướng lên bằng bao nhiêu?
:::

<!-- detailed-solution:22.60 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Lực do trường ngoài tác dụng lên điện tích mặt. Mặt mang Q của bán cầu là mặt tròn phẳng.

**Hướng đi:**

- Phần tử diện tích dA mang dq = σ dA, nên tích phân thành phần lực cho σ nhân điện thông ngoài.
- Ở (b), trường mặt vô hạn đều. Cân bằng lực điện hướng lên với trọng lượng.
- Ở (c), phải trừ g khi chuyển lực điện sang gia tốc tổng.

**(a)**

$$
\begin{aligned}
F_\perp&=\int E_\perp\,dq\\
&=\sigma\int E_\perp\,dA\\
&=\sigma\Phi_E.
\end{aligned}
$$

Không dùng trường do chính phần điện tích mặt đang xét tạo ra như một trường ngoài gây lực lên toàn hệ. **(b)** Nếu Q và σ cùng dấu, lực điện hướng lên có độ lớn Qσ/(2$\varepsilon_0$). Vì thế $M=Q\sigma/(2g\varepsilon_0)$. Nếu trái dấu, lực điện cũng hướng xuống nên không có cân bằng này.

**(c)** $Q=\sigma\pi R^2$, lực điện bằng 1,60 N. Gia tốc tổng:

$$
a_z=\frac{\sigma^2\pi R^2}{2M\varepsilon_0}-g
=6.17\,\mathrm{m/s^2}.
$$
:::

## Bài tập nâng cao

::: exercise 22.61 ••• CALC
Cầu cách điện tích điện đều, bán kính r, điện tích +Q, ở tâm một trụ rỗng thành mỏng bán kính R > r và chiều dài L > 2r. Trụ không dẫn điện và không mang điện tích tổng. **(a)** Tìm điện thông ra qua mặt bên, bỏ hai đáy. Gợi ý: Trục z theo trục trụ, gốc tại tâm cầu, phần diện tích bên là dA = 2πR dz. **(b)** Tìm điện thông hướng lên qua đáy trên. **(c)** Hướng xuống qua đáy dưới. **(d)** Cộng điện thông ba phần. **(e)** Kiểm tra sự phù hợp với Gauss.
:::

<!-- detailed-solution:22.61 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Toàn mặt trụ ở ngoài cầu tích điện, nên trường nguồn giống trường Q ở tâm.

**Hướng đi:**

- Trên mặt bên, chỉ thành phần theo bán kính trụ xuyên qua mặt.
- Tích phân theo z cho mặt bên. Dùng tích phân vòng trên đáy hoặc đối xứng hai đáy và Gauss để đối chiếu.

Trên mặt bên, khoảng cách đến tâm là $\sqrt{R^2+z^2}$ và thành phần vuông góc là $kQR/(R^2+z^2)^{3/2}$. Vì vậy:

$$
\begin{aligned}
\Phi_{\mathrm{bên}}&=2\pi kQR^2\\
&\quad\times\int_{-L/2}^{L/2}\frac{dz}{(R^2+z^2)^{3/2}}\\
&=\frac Q{\varepsilon_0}
\frac{L}{\sqrt{L^2+4R^2}}.
\end{aligned}
$$

Đặt h = L/2. Trên đáy trên, thành phần đứng là $kQh/(s^2+h^2)^{3/2}$, phần diện tích vòng là 2πs ds. Tích phân s từ 0 đến R cho:

$$
\begin{aligned}
\Phi_{\mathrm{trên}}&=\frac{Q}{2\varepsilon_0}
\left(1-\frac{L}{\sqrt{L^2+4R^2}}\right),\\
\Phi_{\mathrm{dưới}}&=\Phi_{\mathrm{trên}}.
\end{aligned}
$$

Điện thông ở đáy dưới được đo hướng xuống, tức hướng ra ngoài, nên cũng dương. Cộng ba phần được Q/$\varepsilon_0$, đúng Gauss vì trụ bao toàn bộ Q.
:::

::: exercise 22.62 ••• CP CALC
Điện tích tổng dương Q có phân bố cầu đối xứng bán kính R, với mật độ:

- Khi 0 ≤ r ≤ R/2, $\rho(r)=3\alpha r/(2R)$.
- Khi R/2 ≤ r ≤ R, $\rho(r)=\alpha[1-(r/R)^2]$.
- Khi r ≥ R, mật độ bằng không.

Hằng số α dương có đơn vị C/m³. **(a)** Tìm α theo Q,R. **(b)** Dùng Gauss tìm độ lớn trường trong cả ba vùng, biểu diễn theo Q. **(c)** Phần điện tích trong R/2 ≤ r ≤ R chiếm tỷ lệ nào của Q? **(d)** Tìm E tại R/2. **(e)** Electron thả từ nghỉ trong một trong ba vùng dao động nhưng không điều hòa. Giải thích.
:::

<!-- detailed-solution:22.62 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mật độ có hai biểu thức nối liên tục tại R/2.

**Hướng đi:**

- Tích phân điện tích riêng cho từng vùng, rồi cộng để tìm Q.
- Trong vùng ngoài của cầu, phải giữ cả điện tích vùng trong đã được bao.
- Chỉ sau khi tìm điện tích theo r mới chia diện tích Gauss để có E.

**(a)** Hai phần điện tích là:

$$
\begin{aligned}
Q_1&=\frac{3\pi\alpha R^3}{32},\\
Q_2&=\frac{47\pi\alpha R^3}{120},\\
Q&=\frac{233\pi\alpha R^3}{480},\\
\alpha&=\frac{480Q}{233\pi R^3}.
\end{aligned}
$$

**(b)** Đặt u = r/R. Với 0 ≤ u ≤ 1/2, tích phân mật độ cho $Q_{\mathrm{trong}}=(720Q/233)u^4$. Do đó:

$$
E_1=\frac{kQ}{R^2}\frac{720u^2}{233}.
$$

Với 1/2 ≤ u ≤ 1:

$$
\begin{aligned}
Q_{\mathrm{trong}}&=Q_1+4\pi\alpha\\
&\quad\times\int_{R/2}^{r}\left(s^2-\frac{s^4}{R^2}\right)ds\\
&=\frac Q{233}\\
&\quad\times(640u^3-384u^5-23),\\
E_2&=\frac{kQ}{233R^2}\\
&\quad\times\left(640u-384u^3-\frac{23}{u^2}\right).
\end{aligned}
$$

Với u ≥ 1, $E_3=kQ/r^2$. Trường hướng ra, bằng không tại tâm và liên tục ở hai điểm nối.

**(c)** $Q_2/Q=188/233\approx80.7\%$. **(d)** $E(R/2)=180kQ/(233R^2)$. **(e)** Electron chịu lực hút về tâm và trong mô hình không mất năng lượng sẽ chuyển động qua lại. Lực không tỷ lệ tuyến tính với độ lệch, chẳng hạn trong vùng trong cùng E ∝ r², nên dao động không điều hòa. Nếu thả đúng tâm r = 0, electron đứng yên tại cân bằng. Kết luận dao động áp dụng cho vị trí ban đầu lệch tâm.
:::

## Bài đọc và câu hỏi kiểu MCAT

### Che chắn bức xạ trong không gian

Bức xạ không gian gồm các hạt mang điện năng lượng cao do Mặt Trời phát ra. Khi có bùng phát Mặt Trời, cường độ có thể tăng đến mức nguy hiểm đối với con người. Một phương án được đề xuất là đặt các quả cầu tích điện lớn phía trên khu sinh sống và làm việc trên Mặt Trăng hoặc Mars. Trường mạnh của các cầu sẽ làm lệch những hạt mang điện.

Mỗi cầu có thể có cấu tạo tương tự bóng Mylar, với một lớp dẫn điện mỏng ở mặt ngoài mang điện tích dương hoặc âm. Đường kính điển hình trong mô hình này là 5 m. Các câu sau khảo sát mô hình điện trường, không đánh giá đầy đủ hiệu quả kỹ thuật của phương án che chắn.

::: exercise 22.63
Để đẩy electron của bức xạ bùng phát, mỗi cầu cần tạo trường có độ lớn $1\times10^6$ N/C ở cách tâm 25 m. Điện tích cần trên mỗi cầu là **(a)** −0,07 C, **(b)** −8 mC, **(c)** −80 µC, hay **(d)** $-1\times10^{-20}$ C?
:::

<!-- detailed-solution:22.63 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Trường ngoài cầu tại r = 25 m, cần đẩy electron âm.

**Hướng đi:**

- Cầu phải âm để đẩy electron, nên Q âm.
- Trường ngoài cầu cho $|Q|=Er^2/k$.

$$
Q=-\frac{(10^6)(25)^2}{k}\approx-0.070\,\mathrm C.
$$

Chọn **(a)**.
:::

::: exercise 22.64
Độ lớn trường ngay ngoài mặt cầu ấy là **(a)** 0, **(b)** $10^6$ N/C, **(c)** $10^7$ N/C, hay **(d)** $10^8$ N/C?
:::

<!-- detailed-solution:22.64 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Đường kính 5 m nên bán kính mặt cầu bằng 2,5 m.

**Hướng đi:**

- Ngoài cầu, E tỷ lệ 1/r².
- Khoảng cách từ 25 m xuống 2,5 m giảm mười lần, nên trường tăng một trăm lần.

$$
E(R^+)=10^6(25/2.5)^2=10^8\,\mathrm{N/C}.
$$

Chọn **(d)**.
:::

::: exercise 22.65
Trường ngay ngoài cầu có hướng **(a)** tiếp tuyến mặt, **(b)** vuông góc mặt và hướng vào cầu, **(c)** vuông góc mặt và hướng ra, hay **(d)** không có trường ngay ngoài mặt?
:::

<!-- detailed-solution:22.65 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mặt cầu dẫn mang điện âm ở cân bằng tĩnh điện.

**Hướng đi:**

- Trường tại mặt dẫn phải vuông góc, nếu không điện tích sẽ chuyển động tiếp tuyến.
- Điện tích âm cho trường hướng vào.

Chọn **(b)**. Electron có lực ngược chiều trường nên bị đẩy ra, phù hợp mục tiêu ở Bài 22.63.
:::

::: exercise 22.66
Trường trong cầu âm vừa mô tả có tính chất nào? **(a)** Hướng từ tâm ra mặt và lớn nhất ở tâm. **(b)** Hướng từ mặt vào tâm và lớn nhất ở mặt. **(c)** Bằng không. **(d)** Không đổi nhưng khác không.
:::

<!-- detailed-solution:22.66 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cầu là vỏ dẫn mỏng với điện tích dư trên mặt ngoài, không chứa nguồn trong hốc.

**Hướng đi:**

- Trong vật liệu dẫn cân bằng, trường bằng không.
- Hốc kín không chứa nguồn riêng cũng có trường bằng không. Không được thay mô hình bằng quả cầu cách điện tích điện trong thể tích.

Chọn **(c)**.
:::
