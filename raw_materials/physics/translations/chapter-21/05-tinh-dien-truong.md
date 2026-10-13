<!-- Source: Section21.5, printed694–699, PDF714–719. -->

## 21.5. Tính điện trường

Điện tích thường phân bố trên cả một vật chứ không tập trung tại một điểm. Thanh nhựa, thanh thủy tinh hoặc trống tạo ảnh máy in đều mang điện trên bề mặt. Muốn xác định quỹ đạo hạt nhân trong máy gia tốc dùng cho xạ trị hoặc chuyển động hạt mang điện trong linh kiện bán dẫn, cần biết trường do phân bố nguồn tạo ra.

### Chồng chất các điện trường

Xem nguồn là tập các điện tích $q_1,q_2,q_3,\ldots$. Điều này phù hợp với việc điện tích được mang bởi electron và proton có kích thước rất nhỏ. Tại P, các nguồn tạo trường $\vec E_1,\vec E_2,\vec E_3,\ldots$. Điện tích thử $q_0$ chịu từng lực $q_0\vec E_i$. Với ba nguồn:

$$
\begin{aligned}
&\vec F_0 = \vec F_1+\vec F_2+\vec F_3\\
&\quad =q_0\vec E_1+q_0\vec E_2+q_0\vec E_3,\\
&\vec E = \frac{\vec F_0}{q_0}\\
&\quad =\vec E_1+\vec E_2+\vec E_3.
\end{aligned}
$$

Với $n$ nguồn, cộng tất cả những vector trường tại **cùng điểm P**:

$$
\begin{aligned}
&\vec E = \vec E_1+\vec E_2+\cdots+\vec E_n\\
&\quad =\sum_{i=1}^{n}\vec E_i.
\end{aligned}
$$

Đây là nguyên lý chồng chất điện trường. Chỉ số $i$ liệt kê từng nguồn, còn điểm khảo sát được giữ nguyên khi cộng.

![Hình 21.21: Cộng hai vector điện trường tại cùng điểm P](../img/young-21/hinh-21-21.png)

**Hình 21.21:** $q_1$ và $q_2$ tạo $\vec E_1$, $\vec E_2$ tại P. Tổng trường là đường chéo của phép cộng vector, không phải tổng độ dài hai mũi tên.

Với điện tích trên đường, trên mặt và trong thể tích, ta dùng lần lượt mật độ dài $\lambda$, mật độ mặt $\sigma$ và mật độ thể tích $\rho$:

$$
\begin{aligned}
&\lambda = \frac{dq}{d\ell},\\
&[\lambda] = \mathrm{C/m},\\
&\sigma = \frac{dq}{dA},\\
&[\sigma] = \mathrm{C/m^2},\\
&\rho = \frac{dq}{dV},\\
&[\rho] = \mathrm{C/m^3}.
\end{aligned}
$$

Các chữ Hy Lạp lần lượt được đọc là lambda, sigma và rho. Với mật độ đều, dùng lượng điện tích tổng chia chiều dài, diện tích hoặc thể tích tương ứng.

### Cách tổ chức phép tính

**Thiết lập.** Vẽ các nguồn và hệ trục, rồi đánh dấu rõ điểm P cần tính trường.

**Thực hiện.** Đổi đơn vị về SI và luôn phân biệt điểm nguồn S với điểm trường P. Nguồn dương tạo trường từ S ra P, nguồn âm tạo trường từ P về S. Cộng theo vector và khai thác đối xứng để loại các thành phần tự triệt tiêu.

Với nguồn liên tục, chọn phần điện tích nhỏ có thể coi là điểm, tính trường của phần đó tại P rồi tích phân từng thành phần. Có thể cần nhiều tích phân. Cận phải phủ đúng toàn nguồn, không đếm hai lần điện tích khi khai thác đối xứng.

**Đánh giá.** Xét hướng trường có phù hợp dấu nguồn và đối xứng không. Nếu trường phụ thuộc vị trí, thử những giới hạn có kết quả đã biết. Khi có thể, tìm cùng trường bằng một cách khác. Những kỹ thuật này cũng sẽ dùng để tính từ trường do điện tích chuyển động ở chương 28.

### Ví dụ 21.8: Trường của một lưỡng cực điện

Hai điện tích $q_1=+12\,\mathrm{nC}$ và $q_2=-12\,\mathrm{nC}$ cách $0.100\,\mathrm m$. Một cặp bằng nhau về độ lớn và trái dấu như vậy gọi là lưỡng cực điện. Tính trường của từng nguồn và tổng trường tại a, b, c trong Hình 21.22.

![Hình 21.22: Các điểm a, b, c quanh hai điện tích trái dấu](../img/young-21/hinh-21-22.png)

**Hình 21.22:** $q_1$ nằm bên trái $q_2$ trên trục x. a ở giữa, cách $q_1$ $6.0\,\mathrm{cm}$ và cách $q_2$ $4.0\,\mathrm{cm}$. b ở bên trái $q_1$ $4.0\,\mathrm{cm}$. c ở trên trung điểm, cách mỗi nguồn $13.0\,\mathrm{cm}$. Góc $\alpha$ trong tam giác có $\cos\alpha=5/13$.

::: solution Lời giải
**Xác định và thiết lập.** Với mỗi điểm, tính hai trường rồi cộng vector. Trường nguồn dương hướng ra, trường nguồn âm hướng vào.

**Thực hiện.** Chẳng hạn tại a:

$$
\begin{aligned}
&E_{1a} = 9.0\times10^9\frac{12\times10^{-9}}{(0.060)^2}\,\mathrm{N/C}\\
&\quad =3.0\times10^4\,\mathrm{N/C}.
\end{aligned}
$$

Tính tương tự cho các khoảng cách còn lại:

| Điểm | Trường do $q_1$ ($\mathrm{N/C}$) | Trường do $q_2$ ($\mathrm{N/C}$) |
| --- | --- | --- |
| a | $3.0\times10^4$ | $6.8\times10^4$ |
| b | $6.8\times10^4$ | $0.55\times10^4$ |
| c | $6.39\times10^3$ | $6.39\times10^3$ |

(a) Tại a, cả hai trường hướng sang phải:

$$
\begin{aligned}
&\vec E_a = (9.8\times10^4\,\mathrm{N/C})\hat{\mathbf i}.\end{aligned}
$$

(b) Tại b, trường nguồn dương hướng trái, trường nguồn âm hướng phải:

$$
\begin{aligned}
&\vec E_b = (-6.2\times10^4\,\mathrm{N/C})\hat{\mathbf i}.\end{aligned}
$$

(c) Tại c, hai thành phần ngang bằng nhau, còn hai thành phần đứng đối nhau:

$$
\begin{aligned}
&E_{1cx} = E_{2cx}\\
&\quad =(6.39\times10^3)\frac5{13}\,\mathrm{N/C}\\
&\quad =2.46\times10^3\,\mathrm{N/C},\\
&E_{cy} = 0,\\
&\vec E_c = (4.9\times10^3\,\mathrm{N/C})\hat{\mathbf i}.
\end{aligned}
$$

**Đánh giá bằng biểu thức vector.** Hai vector đơn vị từ nguồn đến c là:

$$
\begin{aligned}
&\hat{\mathbf r}_1 = \cos\alpha\hat{\mathbf i}+\sin\alpha\hat{\mathbf j},\\
&\hat{\mathbf r}_2 = -\cos\alpha\hat{\mathbf i}+\sin\alpha\hat{\mathbf j}.
\end{aligned}
$$

Vì $q_2=-q_1$ và hai khoảng cách bằng nhau:

$$
\begin{aligned}
&\vec E_c = \frac{k}{r^2}(q_1\hat{\mathbf r}_1+q_2\hat{\mathbf r}_2)\\
&\quad =\frac{kq_1}{r^2}(\hat{\mathbf r}_1-\hat{\mathbf r}_2)\\
&\quad =\frac{2kq_1}{r^2}\cos\alpha\hat{\mathbf i}\\
&\quad =\frac{2(9.0\times10^9)(12\times10^{-9})}{(0.13)^2}\\
&\quad\times\frac5{13}\,\mathrm{N/C}\,\hat{\mathbf i}\\
&\quad \approx(4.9\times10^3\,\mathrm{N/C})\hat{\mathbf i}.
\end{aligned}
$$

Kết quả trùng phép cộng thành phần. Ví dụ có các bài biến thể ở phần cuối chương.
:::

### Ví dụ 21.9: Điện trường trên trục vòng tích điện

Điện tích Q phân bố đều trên vòng dẫn bán kính a. Tìm trường tại P trên trục vòng, cách tâm một khoảng x.

![Hình 21.23: Phần điện tích nhỏ trên vòng và các thành phần trường tại P](../img/young-21/hinh-21-23.png)

**Hình 21.23:** Vòng có tâm O, trục x đi qua P. Đoạn nhỏ $ds$ mang điện $dQ$ ở cách P một khoảng $r=\sqrt{x^2+a^2}$. Hình biểu diễn trường cho nguồn dương.

::: solution Lời giải
**Xác định và thiết lập.** Chia vòng thành những đoạn rất nhỏ. Mỗi đoạn tạo một vector trường tại P. Hai đoạn đối diện có thành phần vuông góc trục bằng nhau và ngược chiều, nên trường tổng chỉ có thành phần x.

Mật độ dài và điện tích phần nhỏ là:

$$
\begin{aligned}
&\lambda = \frac{Q}{2\pi a},\\
&dQ = \lambda\,ds.
\end{aligned}
$$

**Thực hiện.** Mọi đoạn cách P cùng khoảng $r$:

$$
\begin{aligned}
&dE = k\frac{dQ}{x^2+a^2},\\
&\cos\alpha = \frac{x}{\sqrt{x^2+a^2}},\\
&dE_x = dE\cos\alpha\\
&\quad =\frac{k\lambda x}{(x^2+a^2)^{3/2}}\,ds.
\end{aligned}
$$

Tích phân phủ chu vi từ $s=0$ đến $2\pi a$. Hệ số ngoài $ds$ không đổi trên vòng:

$$
\begin{aligned}
&E_x = \frac{k\lambda x}{(x^2+a^2)^{3/2}}\int_0^{2\pi a}ds\\
&\quad =\frac{k\lambda x(2\pi a)}{(x^2+a^2)^{3/2}}.
\end{aligned}
$$

Thay $\lambda(2\pi a)=Q$:

$$
\begin{aligned}
&E_x = \frac{kQx}{(x^2+a^2)^{3/2}},\\
\end{aligned}
$$

Điện trường chỉ có thành phần dọc trục:

$$
\vec E=E_x\hat{\mathbf i}.
\tag{21.8}
$$

**Đánh giá.** Ở tâm $x=0$, trường bằng không vì các cặp đối diện triệt tiêu. Ở rất xa theo chiều $+x$, với $x\gg a$, mẫu gần bằng $x^3$, nên:

$$
\begin{aligned}
&\vec E\approx k\frac{Q}{x^2}\hat{\mathbf i}.\end{aligned}
$$

Vòng nhỏ so với khoảng cách tạo trường gần như điện tích điểm Q. Quy trình tổng quát là tìm thành phần của từng phần nhỏ rồi tích phân trên toàn nguồn. Ví dụ có bài biến thể ở phần cuối chương.
:::

### Ví dụ 21.10: Điện trường trên trung trực đoạn dây tích điện

Điện tích dương Q phân bố đều trên trục y từ $y=-a$ đến $y=+a$. Tìm trường tại P trên trục x, với $x>0$.

![Hình 21.24: Đoạn dây đối xứng qua gốc và điểm khảo sát trên trung trực](../img/young-21/hinh-21-24.png)

::: solution Lời giải
**Xác định và thiết lập.** Trục x là trung trực đoạn dây. Cặp phần tử ở y và $-y$ có thành phần đứng đối nhau, còn thành phần ngang cùng hướng. Mật độ dài là $\lambda=Q/(2a)$, điện tích phần nhỏ $dQ=\lambda\,dy$.

**Thực hiện.** Với phần tử tại y:

$$
\begin{aligned}
&r = \sqrt{x^2+y^2},\\
&dE = \frac{kQ}{2a}\frac{dy}{x^2+y^2},\\
&dE_x = \frac{kQ}{2a}\frac{x\,dy}{(x^2+y^2)^{3/2}},\\
&dE_y = -\frac{kQ}{2a}\frac{y\,dy}{(x^2+y^2)^{3/2}}.
\end{aligned}
$$

Cộng toàn đoạn bằng tích phân từ $-a$ đến $a$. Nguyên hàm thành phần ngang là $y/[x\sqrt{x^2+y^2}]$ khi $x>0$:

$$
\begin{aligned}
&E_x = \frac{kQ}{2a}\int_{-a}^{a}\frac{x\,dy}{(x^2+y^2)^{3/2}}\\
&\quad =\frac{kQ}{2a}\left[\frac{y}{x\sqrt{x^2+y^2}}\right]_{-a}^{a}\\
&\quad =\frac{kQ}{x\sqrt{x^2+a^2}}.
\end{aligned}
$$

Hàm dưới tích phân đứng là hàm lẻ trên khoảng đối xứng, nên:

$$
\begin{aligned}
&E_y = -\frac{kQ}{2a}\int_{-a}^{a}\frac{y\,dy}{(x^2+y^2)^{3/2}}\\
&\quad =0.
\end{aligned}
$$

Kết quả vector là:

$$
\begin{aligned}
&E_x = \frac{kQ}{x\sqrt{x^2+a^2}}.\end{aligned}
$$

Do thành phần đứng triệt tiêu, vector trường là:

$$
\vec E=E_x\hat{\mathbf i}.
\tag{21.9}
$$

Trường ra xa đoạn nếu mật độ dương, và hướng về đoạn nếu mật độ âm.

**Đánh giá.** Đối xứng cho phép dự đoán $E_y=0$ trước khi tích phân. Hai nửa đoạn góp thành phần ngang bằng nhau. Nếu $x\gg a$, trường trở về $kQ/x^2$, giống điện tích điểm.

Để xét đoạn rất dài, viết kết quả theo mật độ dài:

$$
\begin{aligned}
&E_x = \frac{2k\lambda}{x}\\
&\quad\times(1+x^2/a^2)^{-1/2}.
\end{aligned}
$$

Vector trường vẫn dọc trục x:

$$
\vec E=E_x\hat{\mathbf i}.
\tag{21.10}
$$

Khi $a\gg x$, bỏ $x^2/a^2$ so với 1, được trường dây dài vô hạn. Tại điểm cách dây một khoảng vuông góc r:

$$
\begin{aligned}
&E = \frac{|\lambda|}{2\pi\varepsilon_0r}.\end{aligned}
$$

Trường giảm như $1/r$, chậm hơn trường điện tích điểm giảm như $1/r^2$. Không có dây vô hạn thật, nhưng nếu điểm khảo sát gần phần giữa của dây dài, công thức này rất gần kết quả hữu hạn. Khi r bằng $1\%$ chiều dài toàn dây, chênh lệch nhỏ hơn $0.02\%$. Ví dụ có bài biến thể ở phần cuối chương.
:::

### Ví dụ 21.11: Điện trường trên trục đĩa tích điện đều

Đĩa cách điện bán kính R có mật độ mặt dương đều $\sigma$. Tìm trường trên trục, tại khoảng cách $x>0$ từ tâm.

![Hình 21.25: Chia đĩa thành những vòng đồng tâm để tính trường](../img/young-21/hinh-21-25.png)

::: solution Lời giải
**Xác định và thiết lập.** Xem đĩa là nhiều vòng đồng tâm và sử dụng kết quả của Ví dụ 21.9. Một vòng mỏng bán kính r, bề rộng $dr$ có diện tích $dA=2\pi r\,dr$ và điện tích $dQ=2\pi\sigma r\,dr$.

**Thực hiện.** Thay điện tích phần vòng và bán kính r vào (21.8):

$$
\begin{aligned}
&dE_x = k\frac{2\pi\sigma rx\,dr}{(x^2+r^2)^{3/2}}.\end{aligned}
$$

Tích phân bán kính từ 0 đến R, không từ $-R$ đến R vì mỗi vòng đã phủ toàn chu vi:

$$
\begin{aligned}
&E_x = \frac{\sigma x}{4\varepsilon_0}\int_0^R\frac{2r\,dr}{(x^2+r^2)^{3/2}}.\end{aligned}
$$

Đặt $u=x^2+r^2$, $du=2r\,dr$. Cận mới là $x^2$ và $x^2+R^2$:

$$
\begin{aligned}
&E_x = \frac{\sigma x}{4\varepsilon_0}\int_{x^2}^{x^2+R^2}u^{-3/2}\,du\\
&\quad =\frac{\sigma x}{2\varepsilon_0}\left(\frac1x-\frac1{\sqrt{x^2+R^2}}\right).
\end{aligned}
$$

Đặt $E_0=\frac{\sigma}{2\varepsilon_0}$ để tách hệ số không phụ thuộc vị trí. Phần còn lại là hệ số hình học:

$$
f(x)=1-\frac{x}{\sqrt{x^2+R^2}}.
$$

Vì vậy, điện trường có dạng:

$$
E_x=E_0 f(x).
\tag{21.11}
$$

**Đánh giá.** Khi $R\gg x$, số hạng trừ rất nhỏ:

$$
\begin{aligned}
&E\approx\frac{\sigma}{2\varepsilon_0}.\end{aligned}
\tag{21.12}
$$

Giới hạn mặt phẳng vô hạn không phụ thuộc khoảng cách đến mặt. Trường vuông góc mặt và hướng ra xa nếu mật độ dương. Với điểm phía bên kia, hướng đảo sang phía bên kia. Mật độ âm làm trường hai phía hướng về mặt. Mặt thật có thể dùng gần đúng này nếu kích thước lớn hơn nhiều khoảng cách từ điểm khảo sát đến mặt.
:::

### Ví dụ 21.12: Hai mặt phẳng tích điện trái dấu

Hai mặt phẳng vô hạn song song cách nhau d, có mật độ mặt $+\sigma$ và $-\sigma$. Tìm trường giữa hai mặt, phía trên mặt trên và phía dưới mặt dưới.

![Hình 21.26: Cộng trường hai mặt phẳng, trường ngoài triệt tiêu và trường trong cùng chiều](../img/young-21/hinh-21-26.png)

**Hình 21.26:** Mặt 1 phía dưới dương, mặt 2 phía trên âm. Trục y hướng từ mặt dương đến mặt âm. Hình là mặt cắt nhìn cạnh và chỉ biểu diễn một phần hai mặt vô hạn.

::: solution Lời giải
**Xác định và thiết lập.** Mỗi mặt riêng tạo độ lớn trường $\frac{\sigma}{2\varepsilon_0}$ ở cả hai phía. Cộng hai vector theo nguyên lý chồng chất.

**Thực hiện.** Trường mặt dương hướng ra xa mặt, còn trường mặt âm hướng về mặt. Giữa hai mặt, hai trường cùng hướng từ dương đến âm:

$$
\begin{aligned}
&\vec E = \frac{\sigma}{\varepsilon_0}\hat{\mathbf j}.\end{aligned}
$$

Ở phía trên mặt âm hoặc phía dưới mặt dương, hai trường bằng nhau và ngược chiều, nên tổng trường bằng không.

**Đánh giá.** Trong mô hình vô hạn, kết quả không phụ thuộc d. Với hai bản hữu hạn có khoảng cách nhỏ hơn nhiều kích thước bản, vùng giữa xa mép có trường gần đều. Đây là cơ sở cho mô hình trong Ví dụ 21.7.

Điện trường không phải vật chất chảy ra hoặc chảy vào điện tích. Không được suy luận trường một mặt bị mặt kia “chặn lại”. Mỗi trường thành phần chỉ phụ thuộc phân bố nguồn của nó, và tại mọi điểm phải cộng các vector thành phần.
:::

::: exercise Câu hỏi ôn lại mục 21.5
Trong Hình 21.24, nếu phân bố $+Q$ đều trên nửa đoạn $0<y<a$, còn $-Q$ đều trên nửa đoạn $-a<y<0$, trường tại P hướng (i) $+x$, (ii) $-x$, (iii) $+y$, (iv) $-y$, (v) bằng không, hay (vi) không thuộc các trường hợp đó?
:::

::: solution Giải thích
Chọn (iv). Ghép phần tử dương ở y với phần tử âm cùng độ lớn ở $-y$. Trường của phần dương có thành phần ngang dương, đứng âm. Trường của phần âm có thành phần ngang âm, đứng âm. Hai thành phần ngang triệt tiêu, còn thành phần đứng âm cộng lại.
:::
