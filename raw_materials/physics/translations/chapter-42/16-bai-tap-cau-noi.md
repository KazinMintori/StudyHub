## Bài tập cầu nối: Dao động phân tử và vùng cấm bán dẫn

### Bài tập cầu nối

Ở nhiệt độ $80\,\mathrm{K}$, độ rộng vùng cấm trong chất bán dẫn indi antimonua ($\mathrm{InSb}$) là $0{,}230\,\mathrm{eV}$. Một photon phát ra bởi một phân tử hydro florua ($\mathrm{HF}$) thực hiện bước chuyển dao động – quay từ trạng thái $(n = 1, l = 0)$ sang $(n = 0, l = 1)$ bị hấp thụ bởi một electron ở đỉnh của dải hóa trị trong $\mathrm{InSb}$.
(a) Trạng thái cuối của electron nằm cách mép trên của vùng cấm (tức đáy dải dẫn, tính theo $\mathrm{eV}$) một khoảng bằng bao nhiêu?
(b) Xác suất để trạng thái cuối đó vốn đã bị chiếm bởi một electron khác bằng bao nhiêu?
Tần số dao động của $\mathrm{HF}$ là $1{,}24 \times 10^{14}\,\mathrm{Hz}$, khối lượng của nguyên tử hydro là $1{,}67 \times 10^{-27}\,\mathrm{kg}$, khối lượng của nguyên tử flo là $3{,}15 \times 10^{-26}\,\mathrm{kg}$, và khoảng cách cân bằng giữa hai hạt nhân là $0{,}092\,\mathrm{nm}$. Giả sử rằng năng lượng Fermi của $\mathrm{InSb}$ nằm chính giữa vùng cấm.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Bán dẫn $\mathrm{InSb}$ ở $T = 80\,\mathrm{K}$ có $E_g = 0{,}230\,\mathrm{eV}$, $E_F$ ở giữa dải cấm. Phân tử $\mathrm{HF}$ phát photon trong bước chuyển $(n,l)=(1,0)$ sang $(n,l)=(0,1)$ với $f = 1{,}24 \times 10^{14}\,\mathrm{Hz}$, $m_{\mathrm{H}} = 1{,}67 \times 10^{-27}\,\mathrm{kg}$, $m_{\mathrm{F}} = 3{,}15 \times 10^{-26}\,\mathrm{kg}$, $r_0 = 0{,}092\,\mathrm{nm}$. Electron đỉnh dải hóa trị hấp thụ photon.
(a) Tính khoảng cách năng lượng từ trạng thái cuối đến đáy dải dẫn $E_c$.
(b) Tính xác suất chiếm $f(E)$ của trạng thái cuối.

**Hướng đi:**

- **Mômen quán tính và mức năng lượng phân tử $\mathrm{HF}$**: Tính khối lượng rút gọn $\mu = \frac{m_{\mathrm{H}} m_{\mathrm{F}}}{m_{\mathrm{H}} + m_{\mathrm{F}}}$ và mômen quán tính $I = \mu r_0^2$.
- **Năng lượng photon phát xạ**: Quá trình chuyển từ $n=1 \to 0$ giải phóng lượng tử dao động $hf$, nhưng chuyển từ $l=0 \to 1$ hấp thu lượng tử quay $\frac{\hbar^2}{I}$. Do đó $E_{\mathrm{ph}} = hf - \frac{\hbar^2}{I}$.
- **Trạng thái cuối của electron trong bán dẫn**: Chọn gốc thế năng tại đỉnh dải hóa trị $E_v = 0$. Khi đó đáy dải dẫn ở $E_c = E_g = 0{,}230\,\mathrm{eV}$ và mức Fermi nằm ở $E_F = \frac{E_g}{2} = 0{,}115\,\mathrm{eV}$. Electron hấp thụ photon nhận toàn bộ năng lượng $E_{\mathrm{ph}}$, đạt mức năng lượng $E = E_{\mathrm{ph}}$.
- **Phân bố Fermi–Dirac**: Tính $f(E) = \frac{1}{\mathrm{e}^{(E - E_F)/kT} + 1}$ ở nhiệt độ $T = 80\,\mathrm{K}$.

#### Hướng dẫn giải (Solution Guide)

**Nhận diện và Thiết lập:**
1. Bài toán này kết hợp những kiến thức đã học về các bước chuyển mức năng lượng phân tử trong Mục 42.2, về phân bố Fermi–Dirac trong Mục 42.5, và về chất bán dẫn trong Mục 42.6.
2. Phương trình năng lượng tổng hợp dao động – quay xác định mức năng lượng của các trạng thái phân tử ban đầu và trạng thái cuối. Độ chênh lệch giữa năng lượng ban đầu và năng lượng cuối của phân tử bằng năng lượng $E_{\mathrm{ph}}$ của photon phát ra. Năng lượng này được truyền trọn vẹn cho electron dải hóa trị của $\mathrm{InSb}$ khi hấp thụ photon. Xác suất để trạng thái cuối bị chiếm giữ được xác định bởi hàm phân bố Fermi–Dirac.

**Thực hiện giải:**
3. Tính mômen quán tính $I$ và năng lượng lượng tử dao động $hf$ đối với phân tử $\mathrm{HF}$ từ các dữ liệu số đã cho. (Lưu ý: Không nhầm lẫn giữa tần số dao động thường $f$ và tần số góc $\omega = 2\pi f$).
4. Tính năng lượng trạng thái đầu và trạng thái cuối của phân tử $\mathrm{HF}$. (Lưu ý: Năng lượng dao động tăng hay giảm? Năng lượng quay tăng hay giảm?).
5. Tìm năng lượng truyền cho electron trong $\mathrm{InSb}$. Xác định vị trí năng lượng trạng thái cuối của electron này so với đáy dải dẫn.
6. Xác định xác suất để trạng thái cuối trong $\mathrm{InSb}$ vốn đã bị chiếm giữ trước đó.

**Đánh giá:**
7. Bước chuyển phân tử của $\mathrm{HF}$ có được phép theo quy tắc chọn lọc quang học hay không? Độ biến thiên nào lớn hơn: Biến thiên năng lượng dao động hay biến thiên năng lượng quay?
8. Liệu electron được kích thích trong $\mathrm{InSb}$ có khả năng bị chặn không thể đi vào trạng thái ở dải dẫn (do nguyên lý loại trừ Pauli) hay không?

#### 1. Nhận diện và Thiết lập các đại lượng vật lý

Hệ thống kết hợp ba hiện tượng lượng tử nền tảng:
- Quá trình phát xạ photon từ bước chuyển dao động – quay phân tử $\mathrm{HF}$.
- Sự hấp thụ quang học tạo cặp hạt tải trong chất bán dẫn $\mathrm{InSb}$.
- Thống kê Fermi–Dirac điều khiển xác suất chiếm trạng thái lượng tử của electron.

#### 2. Thực hiện tính toán chi tiết

**Bước 3: Tính khối lượng rút gọn, mômen quán tính và lượng tử dao động của phân tử $\mathrm{HF}$:**

Khối lượng rút gọn của phân tử $\mathrm{HF}$ là:

$$
\mu = \frac{m_{\mathrm{H}} m_{\mathrm{F}}}{m_{\mathrm{H}} + m_{\mathrm{F}}}
$$

Thay số với $m_{\mathrm{H}} = 1{,}67 \times 10^{-27}\,\mathrm{kg}$ và $m_{\mathrm{F}} = 3{,}15 \times 10^{-26}\,\mathrm{kg}$:

$$
\mu \approx 1{,}5859 \times 10^{-27}\,\mathrm{kg}
$$

Mômen quán tính của phân tử đối với trục quay đi qua khối tâm là:

$$
I = \mu r_0^2
$$

Thay khoảng cách cân bằng $r_0=0{,}092\,\mathrm{nm}$, tức $9{,}2 \times 10^{-11}\,\mathrm{m}$:
$$
I \approx 1{,}342 \times 10^{-47}\,\mathrm{kg\cdot m^2}
$$
Hằng số năng lượng quay tương ứng bằng:

$$
\begin{aligned}
\frac{\hbar^2}{I} &\approx 8{,}285 \times 10^{-22}\,\mathrm{J} \\
&\approx 0{,}005171\,\mathrm{eV}
\end{aligned}
$$

Lượng tử năng lượng dao động tính từ tần số $f = 1{,}24 \times 10^{14}\,\mathrm{Hz}$:

$$
\begin{aligned}
hf &\approx 8{,}2163 \times 10^{-20}\,\mathrm{J} \\
&\approx 0{,}51282\,\mathrm{eV}
\end{aligned}
$$

**Bước 4: Tính năng lượng trạng thái đầu, trạng thái cuối và photon phát xạ:**

Mức năng lượng tổng quát dao động – quay của phân tử hai nguyên tử là:

$$
E(n, l) = E_{\text{vib}} + E_{\text{rot}}
$$

Trong đó thành phần dao động và quay lần lượt là:

$$
E_{\text{vib}} = \left(n + \frac{1}{2}\right)hf
$$

$$
E_{\text{rot}} = \frac{l(l+1)\hbar^2}{2I}
$$

- Năng lượng trạng thái ban đầu $(n = 1, l = 0)$:
$$
E_i = \frac{3}{2}hf
$$
- Năng lượng trạng thái cuối cùng $(n = 0, l = 1)$:
$$
E_f = \frac{1}{2}hf + \frac{\hbar^2}{I}
$$

Trong quá trình này, năng lượng dao động giảm đi một lượng $hf$, trong khi năng lượng quay tăng thêm một lượng $\frac{\hbar^2}{I}$. Theo định luật bảo toàn năng lượng, năng lượng của photon phát xạ bằng:

$$
\begin{aligned}
E_{\mathrm{ph}} &= E_i - E_f \\
&= hf - \frac{\hbar^2}{I} \\
&\approx 0{,}508\,\mathrm{eV}
\end{aligned}
$$

**Bước 5: Xác định vị trí năng lượng trạng thái cuối của electron (Phần a):**

Electron trong chất bán dẫn $\mathrm{InSb}$ ban đầu nằm ở đỉnh dải hóa trị $E_v = 0$. Sau khi hấp thụ trọn vẹn photon có năng lượng $E_{\mathrm{ph}} \approx 0{,}508\,\mathrm{eV}$, electron chuyển lên trạng thái có năng lượng:

$$
\begin{aligned}
E &= E_v + E_{\mathrm{ph}} \\
&\approx 0{,}508\,\mathrm{eV}
\end{aligned}
$$

Mép trên của vùng cấm chính là đáy của dải dẫn, có năng lượng $E_c = E_g = 0{,}230\,\mathrm{eV}$. Khoảng cách năng lượng từ trạng thái cuối của electron đến đáy dải dẫn là:

$$
\begin{aligned}
\Delta E_c &= E - E_c \\
&\approx 0{,}278\,\mathrm{eV}
\end{aligned}
$$

Trạng thái cuối nằm sâu bên trong dải dẫn, cách đáy dải dẫn một khoảng $0{,}278\,\mathrm{eV}$.

**Bước 6: Xác định xác suất chiếm của trạng thái cuối (Phần b):**

Năng lượng Fermi nằm chính giữa vùng cấm:

$$
\begin{aligned}
E_F &= \frac{E_g}{2} \\
&= 0{,}115\,\mathrm{eV}
\end{aligned}
$$

Khoảng cách năng lượng từ trạng thái cuối $E$ tới mức Fermi $E_F$ là:

$$
E - E_F \approx 0{,}3927\,\mathrm{eV}
$$

Nhiệt năng ở nhiệt độ $T = 80\,\mathrm{K}$ là:

$$
\begin{aligned}
kT &\approx 1{,}1045 \times 10^{-21}\,\mathrm{J} \\
&\approx 0{,}006894\,\mathrm{eV}
\end{aligned}
$$

Tỉ số số mũ trong phân bố Fermi–Dirac:

$$
\frac{E - E_F}{kT} \approx 56{,}96
$$


Xác suất để trạng thái này vốn đã bị chiếm bởi một electron khác trước khi hấp thụ photon là:

$$
\begin{aligned}
f(E) &= \frac{1}{\mathrm{e}^{(E - E_F)/kT} + 1} \\
&\approx 1{,}84 \times 10^{-25}
\end{aligned}
$$


![Hình 42.BTCN: Sơ đồ dải năng lượng của $\mathrm{InSb}$ minh họa bước chuyển quang học của electron hấp thụ photon phân tử $\mathrm{HF}$.](./img/young-42/loi-giai-d-10.svg)

#### 3. Đánh giá và Thảo luận

**Điểm hướng dẫn 7: Tính cho phép của bước chuyển và so sánh năng lượng:**
- Bước chuyển phân tử của $\mathrm{HF}$ hoàn toàn được phép theo các quy tắc chọn lọc quang học lưỡng cực điện:
  - Biến thiên số lượng tử dao động: $\Delta n = 0 - 1 = -1$ (thỏa mãn $\Delta n = \pm 1$).
  - Biến thiên số lượng tử quay: $\Delta l = 1 - 0 = +1$ (thỏa mãn $\Delta l = \pm 1$).
- So sánh độ lớn biến thiên năng lượng:
  - Biến thiên năng lượng dao động là $|\Delta E_{\text{vib}}| = hf \approx 0{,}513\,\mathrm{eV}$.
  - Gọi $E_r$ là độ tăng năng lượng quay. Khi đó $E_r=\hbar^2/I$, có giá trị khoảng $0{,}00517\,\mathrm{eV}$.
  Biến thiên năng lượng dao động lớn gấp xấp xỉ $100$ lần biến thiên năng lượng quay. Năng lượng photon phát xạ chủ yếu được quyết định bởi lượng tử dao động của liên kết hóa học.

**Điểm hướng dẫn 8: Khả năng bị chặn bởi nguyên lý Pauli:**

Xác suất trạng thái cuối đã bị chiếm chỉ khoảng $1{,}84\times10^{-25}$. Trong mô hình cân bằng đã cho, khả năng bị chặn riêng do sự chiếm trạng thái này vì thế rất nhỏ. Nó vẫn khác không, và kết quả chưa xác định toàn bộ hiệu suất hấp thụ quang học.

Kết quả phần (a) là khoảng $0{,}278\,\mathrm{eV}$ phía trên đáy dải dẫn. Kết quả phần (b) là xác suất khoảng $1{,}84\times10^{-25}$.

</details>
