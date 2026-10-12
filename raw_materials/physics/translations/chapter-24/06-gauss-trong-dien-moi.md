<!-- Source: Section24.6, printed801–802/PDF821–822. -->

## Định luật Gauss trong điện môi

Gauss với ε₀ luôn đếm **toàn bộ điện tích**, gồm điện tích tự do và điện tích liên kết. Trong điện môi tuyến tính, có thể viết lại định luật để chỉ cần điện tích tự do ở vế phải. Ta suy dạng ấy từ tụ phẳng đã xét.

### Mặt Gauss đi qua biên dẫn và điện môi

Chọn một hộp nhỏ cắt qua bản dẫn dương và mặt điện môi gần bản. Hai mặt chính có diện tích A. Mặt trái nằm trong vật dẫn nên trường bằng không. Mặt phải nằm trong điện môi có trường E vuông góc. Bốn mặt bên có trường tiếp tuyến, nên không góp điện thông.

![Hình 24.22: Hộp Gauss nằm một nửa trong vật dẫn, một nửa trong điện môi](../img/young-24/hinh-24-22.png)

Hộp bao điện tích tự do +σA và điện tích liên kết −σᵢA. Gauss cho:

$$
EA=\frac{(\sigma-\sigma_i)A}{\varepsilon_0}.
\tag{24.21}
$$

Quan hệ này còn chứa hai đại lượng chưa biết E,σᵢ. Dùng đáp ứng tuyến tính σᵢ = σ(1 − 1/K) để có σ − σᵢ = σ/K. Do đó:

$$
KEA=\frac{\sigma A}{\varepsilon_0}.
\tag{24.22}
$$

Vế phải bây giờ chỉ chứa điện tích tự do trên bản dẫn. Vế trái là điện thông của **K nhân điện trường**, không phải điện thông của riêng điện trường.

### Dạng tích phân

Đối với điện môi tuyến tính, đẳng hướng được xét, dạng tổng quát là:

$$
\oint K\vec E\cdot d\vec A
=\frac{Q_{\mathrm{tự\ do,\ trong}}}{\varepsilon_0}.
\tag{24.23}
$$

$Q_{\mathrm{tự\ do,\ trong}}$ là tổng đại số điện tích tự do bên trong mặt kín, không gồm điện tích liên kết. Pháp tuyến vẫn hướng ra ngoài.

K có thể khác nhau trên các phần mặt nằm trong các điện môi khác nhau. Khi ấy phải dùng K đúng tại từng điểm và giữ trong tích phân. Chỉ kéo K ra ngoài nếu nó không đổi trên toàn phần mặt được tích phân. Dạng này cần đáp ứng tuyến tính, tức K không phụ thuộc độ lớn trường. Với các trường không quá mạnh, điều kiện ấy đúng cho nhiều điện môi thông thường.

Gauss ban đầu vẫn đúng:

$$
\oint\vec E\cdot d\vec A
=\frac{Q_{\mathrm{tổng,\ trong}}}{\varepsilon_0}.
$$

Hai vế phải khác loại điện tích. Không thay ε₀ bằng Kε₀ nhưng vẫn lấy tổng gồm điện tích liên kết, vì khi đó đã tính tác dụng phân cực hai lần.

### Ví dụ 24.12 — Tụ cầu được lấp bằng dầu cách điện

Tụ cầu ở Ví dụ 24.3 có hai bán kính rₐ,rᵦ. Lấp toàn khe bằng dầu cách điện có hằng số K. Dùng Gauss tìm điện dung.

::: solution Chi tiết
**Xác định và thiết lập.** Điện môi đồng đều không làm mất đối xứng cầu. Chọn mặt cầu bán kính r trong khe. Trên đó K,E không đổi và trường theo pháp tuyến.

$$
\begin{aligned}
KE(4\pi r^2)&=Q/\varepsilon_0,\\
E(r)&=\frac{Q}{4\pi K\varepsilon_0r^2}\\
&=\frac{Q}{4\pi\varepsilon r^2}.
\end{aligned}
$$

So với chân không ở cùng Q, trường còn một phần K, nên hiệu điện thế cũng còn một phần K. Tích phân xuyên tâm cho:

$$
\begin{aligned}
V_{ab}&=\frac{Q}{4\pi\varepsilon}
\left(\frac1{r_a}-\frac1{r_b}\right),\\
C&=Q/V_{ab}\\
&=4\pi K\varepsilon_0\frac{r_ar_b}{r_b-r_a}\\
&=4\pi\varepsilon\frac{r_ar_b}{r_b-r_a}.
\end{aligned}
$$

**Đánh giá.** Điện dung gấp K lần giá trị chân không khi điện môi lấp toàn khe. Nếu chỉ lấp một phần, phải xét hình học và các vùng riêng, không dùng một K chung để nhân toàn C₀.
:::

::: exercise Câu hỏi ôn lại mục 24.6
Một nguồn điểm q dương nằm sâu trong khối điện môi rất lớn, đồng đều, hằng số K. Ở điểm cách nguồn r trong điện môi, độ lớn trường là **(i)** kq/r², **(ii)** Kkq/r², **(iii)** kq/(Kr²), hay **(iv)** không đáp án nào?
:::

::: solution Giải thích
Chọn **(iii)**. Mặt cầu đồng tâm có KE·4πr² = q/ε₀, nên E = kq/(Kr²). Mô hình khối rất lớn bỏ ảnh hưởng biên. Nếu q âm thì trường hướng vào và độ lớn dùng |q|.
:::
