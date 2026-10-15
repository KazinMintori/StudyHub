## Bài tập cầu nối

::: exercise Bài cầu nối 39: Các ngôi sao nóng và những đám mây hydrogen
Một tinh vân phát xạ như Tinh vân Rosette (Hình 39.36) bao gồm một đám mây khí hydrogen bao quanh một ngôi sao rất nóng có nhiệt độ bề mặt là $15\,100\,\mathrm{K}$.

![Hình 39.36: Tinh vân Rosette. Bức xạ bước sóng ngắn từ các sao nóng ở trung tâm kích thích khí hydro, làm đám mây phát sáng.](img/young-39/hinh-39-36.png)

(a) Ngôi sao này có mật độ phát xạ phổ cực đại tại bước sóng nào? Bước sóng này thuộc vùng nào của quang phổ điện từ?

(b) Hầu hết năng lượng bức xạ bởi một vật đen tập trung ở các bước sóng nằm trong khoảng từ một nửa đến ba lần bước sóng phát xạ cực đại $\lambda_{\max}$. Nếu một nguyên tử hydrogen ở gần ngôi sao ở câu (a) ban đầu ở trạng thái cơ bản, số lượng tử chính $n$ của mức năng lượng cao nhất mà nguyên tử có thể bị kích thích lên bởi một photon trong dải bước sóng này là bao nhiêu?

(c) Màu đỏ đặc trưng của tinh vân phát xạ chủ yếu do các nguyên tử hydrogen thực hiện bước chuyển từ mức $n = 3$ về mức $n = 2$ và phát ra photon có bước sóng $656{,}3\,\mathrm{nm}$ (vạch $H_{\alpha}$). Trong mô hình Bohr được lý giải dưới góc độ sóng de Broglie, bước sóng của electron trên quỹ đạo ứng với các mức $n = 2$ và $n = 3$ bằng bao nhiêu? So sánh bước sóng de Broglie này với bước sóng của photon phát xạ.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Ngôi sao nóng có nhiệt độ bề mặt $T = 15\,100\,\mathrm{K}$, dải bước sóng bức xạ chủ yếu $[\lambda_{\max}/2, 3\lambda_{\max}]$, nguyên tử hydro ban đầu ở trạng thái cơ bản $n_1 = 1$.

**Hướng đi:**

- Xác định bước sóng phát xạ cực đại $\lambda_{\max}$ theo định luật dịch chuyển Wien $\lambda_{\max} = b / T$.
- Tìm giới hạn dải bước sóng $[\lambda_{\min}, \lambda_{\max,\text{band}}]$. Photon có năng lượng lớn nhất ứng với bước sóng ngắn nhất $\lambda_{\min}$.
- Tính năng lượng cực đại của photon $E_{,\max} = hc / \lambda_{\min}$ và tìm mức lượng tử cao nhất $n$ thỏa mãn điều kiện kích thích $\Delta E \le E_{,\max}$.
- Áp dụng điều kiện sóng dừng de Broglie trên quỹ đạo tròn $2\pi r_n = n \lambda_e$ để tính bước sóng electron trên quỹ đạo Bohr $n=2$ và $n=3$.

(a) Theo định luật dịch chuyển Wien, bước sóng ứng với mật độ phát xạ phổ cực đại của một vật đen ở nhiệt độ $T = 15\,100\,\mathrm{K}$ là:

$$
\begin{aligned}
\lambda_{\max} &= \frac{b}{T} \\
&= \frac{2{,}898 \times 10^{-3}\,\mathrm{m\cdot K}}{15\,100\,\mathrm{K}} \\
&\approx 1{,}919 \times 10^{-7}\,\mathrm{m} \\
&\approx 192\,\mathrm{nm}.
\end{aligned}
$$

Vì bước sóng này nhỏ hơn giới hạn dưới của ánh sáng nhìn thấy ($380\,\mathrm{nm}$), bức xạ cực đại của ngôi sao thuộc vùng **tử ngoại** (ultraviolet, cụ thể là vùng tử ngoại chân không xa).

(b) Dải bước sóng tập trung phần lớn năng lượng bức xạ của ngôi sao có cận dưới:

$$
\lambda_{\min} = \frac{\lambda_{\max}}{2} \approx 96{,}0\,\mathrm{nm},
$$

và cận trên:

$$
\begin{aligned}
\lambda_{\max,\text{band}} &= 3\lambda_{\max} \\
&\approx 575{,}8\,\mathrm{nm}.
\end{aligned}
$$

Trong dải bước sóng này, photon mang năng lượng lớn nhất ứng với bước sóng ngắn nhất $\lambda_{\min} = 95{,}96\,\mathrm{nm}$:

$$
\begin{aligned}
E_{,\max} &= \frac{hc}{\lambda_{\min}} \\
&= \frac{1240\,\mathrm{eV\cdot nm}}{95{,}96\,\mathrm{nm}} \\
&\approx 12{,}92\,\mathrm{eV}.
\end{aligned}
$$

Nguyên tử hydrogen ban đầu ở mức cơ bản $n = 1$ có năng lượng $E_1 = -13{,}606\,\mathrm{eV}$. Khi hấp thụ photon, nguyên tử chuyển lên mức năng lượng cao hơn $n$ với độ chênh lệch năng lượng:

$$
\begin{aligned}
\Delta E &= E_n - E_1 \\
&= 13{,}61\,\mathrm{eV}\left(1 - \frac{1}{n^2}\right).
\end{aligned}
$$

Để quá trình hấp thụ photon kích thích xảy ra, năng lượng chuyển mức không được vượt quá năng lượng photon tối đa có trong dải:

$$
\begin{aligned}
\Delta E &\le E_{,\max} \\
&\approx 12{,}92\,\mathrm{eV}.
\end{aligned}
$$

Biến đổi bất đẳng thức:

$$
\begin{aligned}
1 - \frac{1}{n^2} &\le 0{,}9496, \\
\frac{1}{n^2} &\ge 0{,}0504, \\
n^2 &\le 19{,}84, \\
n &\le 4{,}45.
\end{aligned}
$$

Vì số lượng tử chính $n$ bắt buộc phải là một số nguyên dương, giá trị lớn nhất mà nguyên tử có thể đạt tới là **$n = 4$**.

Kiểm tra lại:

Chuyển mức lên $n = 4$ cần năng lượng:
$$
\begin{aligned}
\Delta E_{1\to 4} &= 13{,}61\left(1 - \frac{1}{16}\right) \\
&\approx 12{,}76\,\mathrm{eV},
\end{aligned}
$$

Tương ứng với photon có bước sóng $\lambda = \frac{1239{,}84}{12{,}76} \approx 97{,}2\,\mathrm{nm}$ (nằm trong dải bức xạ).
Chuyển mức lên $n = 5$ cần năng lượng:
$$
\begin{aligned}
\Delta E_{1\to 5} &= 13{,}61\left(1 - \frac{1}{25}\right) \\
&\approx 13{,}06\,\mathrm{eV},
\end{aligned}
$$

Tương ứng với photon có bước sóng $\lambda = \frac{1239{,}84}{13{,}06} \approx 94{,}9\,\mathrm{nm} < 96{,}0\,\mathrm{nm}$ (nằm ngoài dải bức xạ chủ yếu).

(c) Trong mô hình sóng de Broglie, quỹ đạo Bohr thứ $n$ là một sóng dừng trên đường tròn chu vi $2\pi r_n$, chứa đúng $n$ lần bước sóng de Broglie của electron:

$$
\begin{aligned}
2\pi r_n &= n \lambda_e \\
\implies \lambda_e &= \frac{2\pi r_n}{n}.
\end{aligned}
$$

Mặt khác, bán kính quỹ đạo Bohr thứ $n$ liên hệ với bán kính Bohr $a_0 \approx 0{,}05292\,\mathrm{nm}$ theo hệ thức $r_n = n^2 a_0$. Do đó:

$$
\lambda_e = \frac{2\pi (n^2 a_0)}{n} = 2\pi n a_0.
$$

Tính bước sóng de Broglie của electron ở các mức:

Với mức $n = 2$:
$$
\begin{aligned}
\lambda_{e,2} &= 2\pi (2) a_0 = 4\pi a_0 \\
&\approx 4\pi(0{,}05292\,\mathrm{nm}) \\
&\approx 0{,}665\,\mathrm{nm}.
\end{aligned}
$$
Với mức $n = 3$:
$$
\begin{aligned}
\lambda_{e,3} &= 2\pi (3) a_0 = 6\pi a_0 \\
&\approx 6\pi(0{,}05292\,\mathrm{nm}) \\
&\approx 0{,}997\,\mathrm{nm}.
\end{aligned}
$$

So sánh với bước sóng của photon phát xạ trong vạch đỏ $H_{\alpha}$ ($\lambda_\gamma = 656{,}3\,\mathrm{nm}$):

$$
\begin{aligned}
\frac{\lambda_\gamma}{\lambda_{e,3}} &= \frac{656{,}3\,\mathrm{nm}}{0{,}997\,\mathrm{nm}} \\
&\approx 658.
\end{aligned}
$$

Bước sóng của photon phát ra dài hơn bước sóng de Broglie của chính electron phát ra nó tới gần một nghìn lần. Điều này xuất phát từ bản chất: Photon có khối lượng nghỉ bằng không và truyền đi với tốc độ ánh sáng mang năng lượng nhỏ ($1{,}89\,\mathrm{eV}$ ứng với $\lambda$ lớn), trong khi electron bị giam hãm trong không gian hạ nanômét của nguyên tử có động lượng lớn, tạo nên bước sóng vật chất cực ngắn theo hệ thức de Broglie.
:::
