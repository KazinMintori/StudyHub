## Luyện tập có hướng dẫn

### Trường của sóng và sự truyền trong vật liệu

Ôn Ví dụ 32.1–32.2 trước khi giải bốn bài sau. Phân biệt biên độ với giá trị tức thời, và xác định hướng truyền bằng tích có hướng của hai trường.

::: exercise VP32.2.1
Một sóng điện từ hình sin trong chân không có biên độ từ trường $4{,}30\times10^{-3}\,\mathrm T$ và số sóng $2{,}50\times10^6\,\mathrm{rad/m}$. Tại một vị trí và thời điểm, điện trường hướng theo $-y$, từ trường hướng theo $+x$.

(a) Tìm biên độ điện trường. (b) Tìm bước sóng. (c) Tìm tần số. (d) Xác định hướng truyền.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết $B_{\max}$, $k$ và hướng tức thời của hai trường. Cần tìm $E_{\max}$, $\lambda$, $f$ và hướng truyền.

**Hướng đi:**

- Dùng $E_{\max}=cB_{\max}$ vì sóng truyền trong chân không.
- Dùng $k=2\pi/\lambda$ và $f=c/\lambda$ vì số sóng mô tả tốc độ thay đổi pha theo vị trí.
- Dùng $\vec E\times\vec B$ vì tích này cho hướng dòng năng lượng của sóng chạy.

(a) Biên độ điện trường:

$$
E_{\max} = cB_{\max} = 1{,}29\times10^6\,\mathrm{V/m}.
$$

(b), (c) Bước sóng và tần số:

$$
\begin{aligned}
\lambda &= \frac{2\pi}{k} \\
&= 2{,}51\times10^{-6}\,\mathrm m, \\
f &= \frac c\lambda \\
&= 1{,}19\times10^{14}\,\mathrm{Hz}.
\end{aligned}
$$

(d) Với $\hat{\mathbf x}$, $\hat{\mathbf y}$, $\hat{\mathbf z}$ là các vector đơn vị dọc ba trục:

$$
(-\hat{\mathbf y})\times\hat{\mathbf x}
=\hat{\mathbf z}.
$$

Sóng truyền theo chiều dương trục $z$.
:::

::: exercise VP32.2.2
Điện trường của một sóng điện từ hình sin trong chân không có dạng sau. Đặt $\theta=ky-\omega t$:

$$
\begin{aligned}
\vec E(y,t) &= \hat{\mathbf x}E_{\max}\cos\theta, \\
E_{\max} &= 2{,}45\times10^6\,\mathrm{V/m}, \\
k &= 6{,}50\times10^6\,\mathrm{rad/m}.
\end{aligned}
$$

(a) Tìm bước sóng. (b) Tìm tần số góc $\omega$. (c) Xác định hướng truyền. (d) Viết hàm sóng của từ trường.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Sóng có điện trường dọc $x$ và pha $ky-\omega t$. Các dữ kiện biên độ và số sóng đã cho.

**Hướng đi:**

- Dùng $\lambda=2\pi/k$ và $\omega=ck$ vì vận tốc pha trong chân không bằng $c$.
- Theo dõi mặt pha không đổi để xác định hướng truyền, vì dấu của số hạng thời gian quyết định chiều chuyển động của pha.
- Chọn hướng $\vec B$ để $\vec E\times\vec B$ cùng hướng truyền, rồi dùng $B_{\max}=E_{\max}/c$.

(a), (b):

$$
\begin{aligned}
\lambda &= \frac{2\pi}{k} \\
&= 9{,}67\times10^{-7}\,\mathrm m, \\
\omega &= ck \\
&= 1{,}95\times10^{15}\,\mathrm{rad/s}.
\end{aligned}
$$

(c) Trên một mặt pha, $ky-\omega t$ không đổi. Vì vậy $y$ tăng khi $t$ tăng, nên sóng truyền theo $+y$.

(d) Tích $\hat{\mathbf x}\times(-\hat{\mathbf z})=\hat{\mathbf y}$ cho hướng từ trường cần chọn. Hai trường cùng pha:

$$
\begin{aligned}
B_{\max} &= \frac{E_{\max}}c \\
&= 8{,}17\times10^{-3}\,\mathrm T, \\
\vec B(y,t) &= -\hat{\mathbf z}B_{\max} \times\cos(ky-\omega t).
\end{aligned}
$$

Khi hàm cosin âm, cả hai vector trường đổi chiều, còn hướng truyền vẫn giữ nguyên.
:::

::: exercise VP32.2.3
Một laser nha khoa phát sóng điện từ hình sin truyền trong chân không theo $+x$, có bước sóng $2{,}94\,\mu\mathrm m$. Tại $x=0$, $t=0$, điện trường hướng theo $+y$ và đạt biên độ $E_{\max}=4{,}20\,\mathrm{MV/m}$.

Tìm độ lớn và hướng của (a) từ trường tại $x=0$, $t=0$, (b) điện trường tại $x=1{,}85\,\mu\mathrm m$, $t=0$, (c) từ trường tại vị trí và thời điểm ở (b).
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết bước sóng, hướng truyền và giá trị trường cực đại tại gốc. Cần giữ đúng dấu của hàm sóng ở vị trí mới.

**Hướng đi:**

- Chọn pha ban đầu bằng không vì điện trường tại gốc đạt cực đại dương.
- Dùng $k=2\pi/\lambda$ để tính pha ở vị trí mới.
- Dùng $B=E/c$ cho các thành phần có dấu, vì hai trường của sóng chạy cùng pha.

Đặt $\theta=kx-\omega t$. Hàm sóng có thể viết:

$$
\begin{aligned}
E_y(x,t) &= E_{\max}\cos\theta, \\
B_z(x,t) &= \frac{E_{\max}}c\cos\theta.
\end{aligned}
$$

Hướng $+z$ của từ trường tại gốc bảo đảm $\vec E\times\vec B$ hướng theo $+x$.

(a):

$$
B_z(0,0) = \frac{E_{\max}}c = 0{,}0140\,\mathrm T.
$$

Từ trường có độ lớn $0{,}0140\,\mathrm T$ và hướng theo $+z$.

(b) Với $x=1{,}85\,\mu\mathrm m$, $t=0$:

$$
\begin{aligned}
kx &= 2\pi\frac{1{,}85}{2{,}94} \\
&= 3{,}9537\,\mathrm{rad}, \\
E_y &= E_{\max}\cos(kx) \\
&= -2{,}89\times10^6\,\mathrm{V/m}.
\end{aligned}
$$

Điện trường có độ lớn $2{,}89\,\mathrm{MV/m}$ và hướng theo $-y$.

(c):

$$
B_z = \frac{E_y}c = -9{,}63\times10^{-3}\,\mathrm T.
$$

Từ trường có độ lớn $9{,}63\,\mathrm{mT}$ và hướng theo $-z$. Hai vector cùng đảo dấu nên tích có hướng vẫn hướng theo $+x$.
:::

::: exercise VP32.2.4
Ánh sáng của một bút laser đỏ có bước sóng trong chân không $6{,}35\times10^{-7}\,\mathrm m$. Khi truyền vào vật liệu trong suốt có độ từ thẩm tương đối $1{,}00$, bước sóng giảm còn $3{,}47\times10^{-7}\,\mathrm m$.

Tìm (a) tần số trong chân không, (b) tần số trong vật liệu, (c) vận tốc trong vật liệu và (d) hằng số điện môi của vật liệu.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết hai bước sóng và $\mu_r=1$. Cần tìm tần số, vận tốc và $\varepsilon_r$ tại tần số ánh sáng đang xét.

**Hướng đi:**

- Dùng $f=c/\lambda_0$ để xác định tần số nguồn.
- Giữ tần số qua mặt phân cách đứng yên, vì trường ở hai bên phải dao động đồng bộ theo thời gian.
- Dùng $v=f\lambda$ và $v=c/\sqrt{\varepsilon_r\mu_r}$ cho mô hình vật liệu tuyến tính, đồng nhất, đẳng hướng và tổn hao không đáng kể.

(a), (b):

$$
\begin{aligned}
f_0 &= \frac c{\lambda_0} \\
&= 4{,}72\times10^{14}\,\mathrm{Hz}, \\
f_{\mathrm m} &= f_0.
\end{aligned}
$$

(c):

$$
v = f_0\lambda_{\mathrm m} = 1{,}64\times10^8\,\mathrm{m/s}.
$$

(d) Vì $\mu_r=1$:

$$
\begin{aligned}
\varepsilon_r &= \left(\frac cv\right)^2 \\
&= \left(\frac{\lambda_0}{\lambda_{\mathrm m}}\right)^2 \\
&= 3{,}35.
\end{aligned}
$$

Đây là hằng số điện môi tại tần số đang xét, không nhất thiết bằng giá trị đo ở trạng thái tĩnh.
:::

### Năng lượng và công suất truyền

Ôn Ví dụ 32.3–32.4 trước khi giải bốn bài sau. Sóng có trường không đổi phía sau mặt sóng và sóng hình sin có cách lấy trung bình khác nhau.

::: exercise VP32.4.1
Một sóng điện từ không hình sin có điện trường và từ trường đồng đều như mô hình sóng phẳng có mặt sóng. Độ lớn vector Poynting là $11{,}0\,\mathrm{W/m^2}$.

(a) Tìm độ lớn điện trường và từ trường. (b) Tìm mật độ năng lượng trong sóng.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Trường trong vùng phía sau mặt sóng không đổi, với $S=11{,}0\,\mathrm{W/m^2}$.

**Hướng đi:**

- Dùng $S=EB/\mu_0$ và $E=cB$ vì đây là sóng phẳng trong chân không.
- Không dùng hệ số $1/2$ của trung bình sóng hình sin, vì trường đang xét có độ lớn không đổi.
- Dùng $S=uc$ để tìm mật độ năng lượng.

(a):

$$
\begin{aligned}
S &= \frac{E^2}{\mu_0c}, \\
E &= \sqrt{\mu_0cS} \\
&= 64{,}4\,\mathrm{V/m}, \\
B &= \frac Ec \\
&= 2{,}15\times10^{-7}\,\mathrm T.
\end{aligned}
$$

(b):

$$
u = \frac Sc = 3{,}67\times10^{-8}\,\mathrm{J/m^3}.
$$

Điện trường và từ trường đóng góp bằng nhau vào $u$.
:::

::: exercise VP32.4.2
Một sóng hình sin trong chân không có hai trường:

$$
\begin{aligned}
E_y &= E_{\max}\cos(kx-\omega t), \\
B_z &= B_{\max}\cos(kx-\omega t).
\end{aligned}
$$

Tìm vector Poynting tại (a) $x=0$, $t=0$, (b) $x=\lambda/4$, $t=0$, (c) $x=\lambda/4$, $t=\pi/(4\omega)$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Sóng truyền theo $+x$, cần tính dòng năng lượng tức thời ở ba cặp vị trí và thời điểm.

**Hướng đi:**

- Nhân hai trường qua $\vec S=(\vec E\times\vec B)/\mu_0$, vì đề hỏi giá trị tức thời.
- Dùng $k\lambda=2\pi$ để thay vị trí vào pha.

Đặt $S_0=E_{\max}B_{\max}/\mu_0$. Khi đó:

$$
\vec S=\hat{\mathbf x}S_0\cos^2(kx-\omega t).
$$

(a) Pha bằng không:

$$
\vec S(0,0)=\hat{\mathbf x}S_0.
$$

(b) Pha bằng $\pi/2$:

$$
\vec S(\lambda/4,0)=\vec0.
$$

(c) Pha bằng $\pi/2-\pi/4=\pi/4$:

$$
\vec S=\frac{S_0}{2}\hat{\mathbf x}.
$$

Vector Poynting không đảo chiều khi hai trường cùng đổi dấu.
:::

::: exercise VP32.4.3
Một đài trên mặt đất phát sóng vô tuyến hình sin đều theo mọi hướng trong bán cầu phía trên. Máy bay ở ngay trên đài, cao $12{,}5\,\mathrm{km}$, đo được biên độ điện trường $0{,}360\,\mathrm{V/m}$.

(a) Tìm biên độ từ trường và cường độ bức xạ tại máy bay. (b) Tìm tổng công suất phát của đài.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn phát đều trên bán cầu, khoảng cách đến máy bay là $r=12{,}5\,\mathrm{km}$.

**Hướng đi:**

- Dùng $B_{\max}=E_{\max}/c$ và cường độ trung bình của sóng hình sin.
- Nhân cường độ với diện tích bán cầu $2\pi r^2$, vì nguồn chỉ phát vào nửa không gian đã nêu.

(a):

$$
\begin{aligned}
B_{\max} &= \frac{E_{\max}}c \\
&= 1{,}20\times10^{-9}\,\mathrm T, \\
I &= \frac12\varepsilon_0cE_{\max}^2 \\
&= 1{,}72\times10^{-4}\,\mathrm{W/m^2}.
\end{aligned}
$$

(b):

$$
P = I(2\pi r^2) = 1{,}69\times10^5\,\mathrm W.
$$

Nếu thay bán cầu bằng mặt cầu thì công suất sẽ bị nhân sai thêm hai lần.
:::

::: exercise VP32.4.4
Mặt Trời phát ánh sáng đều theo mọi hướng, được mô hình hóa bằng sóng hình sin. Khoảng cách đến Trái Đất là $1{,}50\times10^{11}\,\mathrm m$. Cường độ ánh sáng ở đỉnh khí quyển là $1{,}36\,\mathrm{kW/m^2}$.

(a) Tìm biên độ điện trường và từ trường tại đỉnh khí quyển. (b) Tìm tổng công suất bức xạ của Mặt Trời.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết cường độ trung bình $I$ trên mặt cầu bán kính bằng khoảng cách đến Trái Đất.

**Hướng đi:**

- Giải $I=\varepsilon_0cE_{\max}^2/2$ vì dữ kiện là cường độ trung bình.
- Dùng $P=4\pi r^2I$ vì bức xạ phân bố trên toàn mặt cầu.

(a):

$$
\begin{aligned}
E_{\max} &= \sqrt{\frac{2I}{\varepsilon_0c}} \\
&= 1{,}01\times10^3\,\mathrm{V/m}, \\
B_{\max} &= \frac{E_{\max}}c \\
&= 3{,}38\times10^{-6}\,\mathrm T.
\end{aligned}
$$

(b):

$$
P = 4\pi r^2I = 3{,}85\times10^{26}\,\mathrm W.
$$
:::

### Sóng đứng điện từ

Ôn Ví dụ 32.6–32.7 trước khi giải bốn bài sau. Trong sóng đứng, hai trường vuông pha theo thời gian và các mặt nút của chúng lệch nhau một phần tư bước sóng.

::: exercise VP32.7.1
Xét sóng đứng:

$$
\begin{aligned}
E_y(x,t) &= -2E_{\max}\sin(kx) \times\sin(\omega t), \\
B_z(x,t) &= -2B_{\max}\cos(kx) \times\cos(\omega t).
\end{aligned}
$$

(a) Tìm độ lớn lớn nhất của vector Poynting ở mọi vị trí và thời điểm. Tìm vector Poynting tại $x=\lambda/8$ ở các thời điểm (b) $t=0$, (c) $t=\pi/(3\omega)$, (d) $t=3\pi/(4\omega)$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biên độ $E_{\max}$ và $B_{\max}$ thuộc mỗi sóng thành phần, còn các trường tổng có hệ số hai.

**Hướng đi:**

- Dùng tích có hướng để giữ dấu dòng năng lượng, vì sóng đứng trao đổi năng lượng theo cả hai chiều.
- Dùng $\sin2a=2\sin a\cos a$ để tách hệ số vị trí và thời gian.

Đặt $S_0=E_{\max}B_{\max}/\mu_0$. Tích hai trường cho:

$$
\begin{aligned}
S_x &= 4S_0\sin(kx)\cos(kx) \times\sin(\omega t)\cos(\omega t) \\
&= S_0\sin(2kx)\sin(2\omega t).
\end{aligned}
$$

(a) Hai hàm sin cùng có độ lớn tối đa bằng một, nên:

$$
|\vec S|_{\max}=S_0.
$$

Tại $x=\lambda/8$, ta có $\sin(2kx)=1$. Do đó:

$$
\begin{aligned}
\text{(b)}\quad\vec S &= \vec0, \\
\text{(c)}\quad\vec S &= \frac{\sqrt3}{2}S_0\hat{\mathbf x}, \\
\text{(d)}\quad\vec S &= -S_0\hat{\mathbf x}.
\end{aligned}
$$

Hai kết quả cuối cho hai chiều chuyển năng lượng đối lập. Trung bình của vector qua cả chu kỳ bằng không, dù giá trị tức thời có thể khác không.
:::

::: exercise VP32.7.2
Trong một sóng đứng điện từ phân cực thẳng, biên độ từ trường tại mặt vật dẫn là $1{,}20\times10^{-7}\,\mathrm T$. Mặt nút từ trường gần vật dẫn nhất cách vật dẫn $3{,}60\,\mathrm{mm}$.

(a) Tìm bước sóng. (b) Tìm tần số. (c) Tìm biên độ điện trường ở mặt nút từ trường đầu tiên.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mặt vật dẫn là bụng từ trường và nút điện trường. Khoảng cách đến nút từ trường đầu tiên bằng $\lambda/4$.

**Hướng đi:**

- Dùng cấu trúc nút, bụng để suy bước sóng từ khoảng cách đã đo.
- Dùng $f=c/\lambda$.
- Phân biệt biên độ của trường tổng với biên độ của từng sóng chạy, vì từ trường tại tường bằng $2B_{\max}$.

(a), (b):

$$
\begin{aligned}
\lambda &= 4(3{,}60\,\mathrm{mm}) \\
&= 14{,}4\,\mathrm{mm}, \\
f &= \frac c\lambda \\
&= 2{,}08\times10^{10}\,\mathrm{Hz}.
\end{aligned}
$$

(c) Ở nút từ trường đầu tiên, điện trường đạt bụng. Biên độ này là $2E_{\max}$, trong khi biên độ từ trường tại tường là $2B_{\max}$. Tỉ số vẫn bằng $c$:

$$
E_{\mathrm{bụng}} = cB_{\mathrm{tường}} = 36{,}0\,\mathrm{V/m}.
$$

Đây là quan hệ giữa hai biên độ tại hai vị trí khác nhau. Không áp dụng $E=cB$ cho hai giá trị tức thời tại cùng điểm của sóng đứng.
:::

::: exercise VP32.7.3
Một hốc có hai mặt dẫn song song tại $x=0$ và $x=4{,}56\,\mathrm{cm}$ chứa sóng đứng điện từ.

(a) Tìm ba tần số thấp nhất và bước sóng tương ứng. (b) Tìm vị trí các mặt nút điện trường của từng mode.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khoảng cách giữa hai tường là $L=4{,}56\,\mathrm{cm}$. Cả hai tường đều phải là nút điện trường.

**Hướng đi:**

- Dùng $L=n\lambda_n/2$ vì mỗi mode chứa một số nguyên nửa bước sóng.
- Bắt đầu từ $n=1,2,3$ để có ba tần số thấp nhất.
- Dùng $x_j=jL/n$ với $j=0,1,\ldots,n$ vì các nút điện trường cách nhau $\lambda_n/2$.

(a):

$$
\lambda_n=\frac{2L}{n},\qquad f_n=\frac{nc}{2L}.
$$

Các kết quả:

| Mode | Bước sóng | Tần số |
| --- | --- | --- |
| 1 | 9,12 cm | 3,29 GHz |
| 2 | 4,56 cm | 6,58 GHz |
| 3 | 3,04 cm | 9,87 GHz |

(b) Vị trí nút điện trường, đo bằng centimét:

- Mode 1 có $x=0$ và $x=4{,}56$.
- Mode 2 có $x=0$, $x=2{,}28$ và $x=4{,}56$.
- Mode 3 có $x=0$, $x=1{,}52$, $x=3{,}04$ và $x=4{,}56$.

Hai tường là nút chung của mọi mode, còn số nút trong hốc tăng theo số mode.
:::

::: exercise VP32.7.4
Một lò vi sóng tạo sóng đứng có bước sóng $12{,}2\,\mathrm{cm}$ giữa hai tường dẫn song song cách nhau $48{,}8\,\mathrm{cm}$.

(a) Tìm tần số sóng. (b) Tìm số mặt bụng điện trường giữa hai tường.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Biết $\lambda$ và chiều dài hốc $L$. Tường dẫn là nút điện trường.

**Hướng đi:**

- Dùng $f=c/\lambda$ vì sóng truyền trong không khí với tốc độ xấp xỉ $c$.
- Đếm số nửa bước sóng $n=2L/\lambda$, vì mỗi khoảng giữa hai nút liên tiếp chứa một bụng.

(a):

$$
f=\frac c\lambda=2{,}46\times10^9\,\mathrm{Hz}.
$$

(b):

$$
n=\frac{2L}{\lambda}=\frac{2(48{,}8)}{12{,}2}=8.
$$

Có tám mặt bụng điện trường giữa hai tường. Các vị trí là $x_j=(2j+1)\lambda/4$, với $j=0,1,\ldots,7$.
:::

## Bài cầu nối: Phát hiện sóng điện từ

::: exercise Bài cầu nối 32
Một vòng dây tròn có thể dùng làm anten vô tuyến. Anten có đường kính $18{,}0\,\mathrm{cm}$, đặt cách nguồn $2{,}50\,\mathrm{km}$. Nguồn có tần số $95{,}0\,\mathrm{MHz}$ và tổng công suất $55{,}0\,\mathrm{kW}$. Hướng vòng dây và phân cực của sóng được chỉ trên Hình 32.24. Giả sử nguồn phát đều theo mọi hướng.

Tìm biên độ suất điện động cảm ứng trong vòng dây.

![Hình 32.24: Vòng anten trong mặt phẳng xy nhận từ thông của từ trường dọc z](img/young-32/hinh-bridge32-01.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Anten một vòng có bán kính $a=0{,}0900\,\mathrm m$. Mặt vòng vuông góc từ trường của sóng. Biết công suất nguồn, khoảng cách và tần số.

**Hướng đi:**

- Dùng $I=P/(4\pi r^2)$ vì nguồn phát đều trên mặt cầu.
- Tìm $B_{\max}$ từ cường độ trung bình của sóng hình sin.
- Dùng $\Phi_B=AB(t)$ trong gần đúng trường đồng đều trên vòng, vì kích thước vòng nhỏ so với bước sóng.
- Lấy đạo hàm từ thông theo định luật Faraday. Tốc độ biến thiên có hệ số $\omega=2\pi f$.

Cường độ sóng tại anten:

$$
I = \frac{P}{4\pi r^2} = 7{,}00\times10^{-4}\,\mathrm{W/m^2}.
$$

Biên độ từ trường:

$$
\begin{aligned}
B_{\max} &= \sqrt{\frac{2\mu_0I}{c}} \\
&= 2{,}42\times10^{-9}\,\mathrm T.
\end{aligned}
$$

Diện tích vòng:

$$
A=\pi a^2=2{,}54\times10^{-2}\,\mathrm{m^2}.
$$

Chọn gốc pha tại anten để $B_z=B_{\max}\cos(\omega t)$. Trong gần đúng trường đồng đều:

$$
\begin{aligned}
\Phi_B(t) &= AB_{\max}\cos(\omega t), \\
\mathcal E(t) &= -\frac{d\Phi_B}{dt} \\
&= A\omega B_{\max}\sin(\omega t).
\end{aligned}
$$

Biên độ cần tìm:

$$
\begin{aligned}
\mathcal E_{\max} &= A(2\pi f)B_{\max} \\
&= 3{,}68\times10^{-2}\,\mathrm V \\
&= 36{,}8\,\mathrm{mV}.
\end{aligned}
$$

Bước sóng khoảng $3{,}16\,\mathrm m$, lớn hơn đường kính vòng. Suất điện động ở mức vài chục millivolt có thể tạo tín hiệu đầu vào cho máy thu. Mức tín hiệu hữu ích còn phụ thuộc trở kháng anten, tải, hướng đặt và nhiễu.
:::
