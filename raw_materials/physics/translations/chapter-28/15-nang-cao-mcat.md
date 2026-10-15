## Bài nâng cao 28.76–28.80

::: exercise 28.76 ••• CALC
Vỏ trụ bán kính $R$, dài $W$, mang điện tích phân bố đều $Q$ và quay quanh trục với tốc độ góc $\omega$. Tâm trụ ở gốc $O$, trục trụ trùng trục $x$ như Hình P28.76. (a) Tìm mật độ điện tích mặt $\sigma$.

(b) Tìm dòng vi phân $dI$ của một dải vòng tròn rộng $dx$ tại tọa độ $x$.

(c) Dùng công thức trường trên trục vòng dây để viết $d\vec B$ tại gốc do dải ấy.

(d) Tích phân tìm trường tại gốc.

![Hình P28.76: Vỏ trụ tích điện quay được chia thành những dải vòng tròn rộng dx.](img/young-28/hinh-p28-76.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vỏ trụ có bán kính $R$, chiều dài $W$, điện tích đều $Q$. Các dải vòng nằm từ $x=-W/2$ đến $x=+W/2$.

**Hướng đi:**

- Chia vỏ thành các vòng, vì trường trên trục của từng vòng đã biết.
- Điện tích của dải bằng mật độ mặt nhân diện tích dải. Dòng của dải bằng điện tích ấy chia chu kỳ quay.
- Các trường tại tâm trụ cùng phương trục, nên cộng bằng tích phân theo $x$, giữ khoảng cách từ vòng đến điểm đo.

(a) Diện tích mặt bên là $2\pi RW$:

$$
\sigma=\frac{Q}{2\pi RW}.
$$

(b) Dải rộng $dx$ có điện tích:

$$
\begin{aligned}
dQ &= \sigma\,2\pi R\,dx \\
&= \frac QW\,dx.
\end{aligned}
$$

Với chu kỳ $T=2\pi/\omega$, dòng vi phân là:

$$
\begin{aligned}
dI &= \frac{dQ}{T} \\
&= \frac{Q\omega}{2\pi W}\,dx.
\end{aligned}
$$

(c) Vòng nằm cách gốc một khoảng $|x|$. Trường trên trục do vòng ấy là:

$$
\begin{aligned}
d\vec B &= \frac{\mu_0R^2\,dI}{2(x^2+R^2)^{3/2}}\hat i \\
&= \frac{\mu_0Q\omega R^2}{4\pi W} \times\frac{dx}{(x^2+R^2)^{3/2}}\hat i.
\end{aligned}
$$

Đã chọn chiều quay dương quanh $+x$. Dấu của $Q$ quyết định chiều dòng quy ước và chiều trường.

(d) Cộng từ hai đầu vỏ trụ:

$$
\begin{aligned}
B_x(O) &= \frac{\mu_0Q\omega R^2}{4\pi W}\mathcal K, \\
\mathcal K &= \int_{-W/2}^{W/2} \frac{dx}{(x^2+R^2)^{3/2}}.
\end{aligned}
$$

Để tính $\mathcal K$, dùng nguyên hàm:

$$
F(x)=\frac{x}{R^2\sqrt{x^2+R^2}}.
$$

Tích phân $\mathcal K$ bằng $F(W/2)-F(-W/2)$. Sau khi thay hai cận, ta được:

$$
\begin{aligned}
B_x(O) &= \frac{\mu_0Q\omega}{4\pi}\left[R^2+(W/2)^2\right]^{-1/2}, \\
\vec B(O) &= B_x(O)\hat i.
\end{aligned}
$$
:::

::: exercise 28.77 ••• CALC
Khi một phân bố điện tích rắn, có tổng điện tích $Q$ và khối lượng $M$, quay quanh một trục, mômen từ $\vec M_{\mathrm{từ}}$ tỉ lệ với mômen động lượng $\vec L$:

$$
\begin{aligned}
\vec M_{\mathrm{từ}} &= \gamma\vec L, \\
\gamma &= g\frac{Q}{2M}.
\end{aligned}
$$

$\gamma$ là tỉ số hồi chuyển từ, còn $g$ là hệ số không có đơn vị. Xét vỏ cầu bán kính $R$, khối lượng $M$, điện tích $Q$ phân bố đều, tâm tại $O$, quay quanh trục $z$ với tốc độ góc $\omega$.

(a) Dải mỏng ở góc cực $\theta$ đo từ $+z$ có bề rộng $R\,d\theta$ và bán kính vòng $r=R\sin\theta$ như Hình P28.77. Tìm dòng vi phân $dI$ theo $Q,\omega,R,\theta,d\theta$.

(b) Với diện tích vòng $A=\pi r^2$, mômen vi phân là $d\mu=A\,dI$. Tìm $d\mu$.

(c) Tích phân tìm mômen từ của vỏ.

(d) Tìm độ lớn mômen động lượng.

(e) Tìm $\gamma$.

(f) Tìm hệ số $g$ của vỏ cầu.

![Hình P28.77: Dải mỏng trên vỏ cầu tích điện quay tạo thành một vòng dòng điện.](img/young-28/hinh-p28-77.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vỏ cầu có điện tích và khối lượng phân bố đều. Trục quay là $z$, góc cực chạy từ $0$ đến $\pi$.

**Hướng đi:**

- Dải có diện tích bằng chu vi vòng nhân bề rộng, nên lấy đúng thừa số $\sin\theta$.
- Dòng của dải bằng điện tích qua một chu kỳ quay. Mômen từ của dải dùng diện tích vòng mà dòng bao quanh, khác diện tích bề mặt dải.
- Cộng mômen của các dải theo trục $z$. Tính mômen động lượng của vỏ cầu rồi lấy tỉ số để tìm $\gamma,g$.

(a) Mật độ mặt và diện tích dải là:

$$
\begin{aligned}
\sigma &= \frac{Q}{4\pi R^2}, \\
dA_{\mathrm{dải}} &= 2\pi R^2\sin\theta\,d\theta, \\
dQ &= \frac Q2\sin\theta\,d\theta.
\end{aligned}
$$

Sau mỗi chu kỳ $2\pi/\omega$, điện tích này đi qua cùng một vị trí. Vì vậy:

$$
dI=\frac{Q\omega}{4\pi}\sin\theta\,d\theta.
$$

(b) Diện tích vòng được bao là $\pi R^2\sin^2\theta$, nên:

$$
d\mu=\frac{Q\omega R^2}{4}\sin^3\theta\,d\theta.
$$

(c) Mọi vòng có mômen cùng phương trục quay. Tích phân góc là:

$$
\begin{aligned}
\mathcal I &= \int_0^\pi\sin^3\theta\,d\theta, \\
\mathcal I &= \int_{-1}^{1}(1-u^2)\,du \\
&= \left[u-\frac{u^3}{3}\right]_{-1}^{1} \\
&= \frac43,
\end{aligned}
$$

trong đó đã đặt $u=\cos\theta$. Do đó:

$$
\vec M_{\mathrm{từ}}=\frac{Q\omega R^2}{3}\hat k.
$$

(d) Với khối lượng phân bố đều, một dải có $dm=(M/2)\sin\theta\,d\theta$. Khoảng cách dải đến trục bằng $R\sin\theta$. Vì vậy:

$$
\begin{aligned}
I_z &= \frac{MR^2}{2}\int_0^\pi\sin^3\theta\,d\theta \\
&= \frac23MR^2, \\
L &= I_z\omega=\frac23MR^2\omega.
\end{aligned}
$$

(e) So sánh hai vector theo cùng trục:

$$
\gamma=\frac{Q}{2M}.
$$

Tỉ số có dấu theo $Q$. Với điện tích âm, mômen từ ngược hướng mômen động lượng.

(f) Đối chiếu với $\gamma=gQ/(2M)$:

$$
g=1.
$$
:::

::: exercise 28.78 ••• CALC
Định luật Biot–Savart cho dòng mặt có thể viết:

$$
\vec B=\frac{\mu_0}{4\pi}
\int\frac{\sigma\vec v\times\hat r}{r^2}\,da,
$$

trong đó $\sigma$ là mật độ điện tích mặt tại chỗ, $\vec v$ là vận tốc điện tích và $da$ là phần tử diện tích. Dùng biểu thức này để giải lại bài 28.76.

(a) Viết $\sigma$.

(b) Tìm vector từ phần tử ở $(x,R\cos\phi,R\sin\phi)$ đến gốc.

(c) Tìm vận tốc phần tử.

(d) Tính $\vec v\times\hat r$.

(e) Với $da=R\,dx\,d\phi$, viết tích phân kép và tính trường tại tâm.

(f) So sánh với kết quả bài 28.76.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vỏ trụ của bài 28.76 có tâm ở gốc, trục $x$, bán kính $R$, dài $W$, điện tích $Q$ đều và tốc độ góc $\omega$.

**Hướng đi:**

- Giữ vector khoảng cách theo chiều từ nguồn đến điểm đo, vì đảo nó sẽ đảo chiều tích có hướng.
- Dùng $\vec v=\vec\omega\times\vec r_{\mathrm{vị\ trí}}$ để tìm vận tốc quay quanh $x$.
- Tích phân theo $\phi$ trước. Đối xứng làm các thành phần ngang trục triệt tiêu, chỉ còn thành phần $x$.

(a) Mật độ điện tích mặt là:

$$
\sigma=\frac{Q}{2\pi RW}.
$$

(b) Vector từ phần tử đến gốc là:

$$
\begin{aligned}
\vec r &= -x\hat i-R\cos\phi\hat j -R\sin\phi\hat k, \\
r &= \sqrt{x^2+R^2}.
\end{aligned}
$$

(c) Chọn $\vec\omega=\omega\hat i$. Từ tích có hướng của vận tốc góc và vector vị trí:

$$
\vec v = -\omega R\sin\phi\hat j +\omega R\cos\phi\hat k.
$$

(d) Tính từng thành phần thay vì suy chiều từ một vị trí riêng:

$$
\begin{aligned}
(\vec v\times\hat r)_x &= \frac{\omega R^2}{\sqrt{x^2+R^2}}, \\
(\vec v\times\hat r)_y &= -\frac{\omega xR\cos\phi}{\sqrt{x^2+R^2}}, \\
(\vec v\times\hat r)_z &= -\frac{\omega xR\sin\phi}{\sqrt{x^2+R^2}}.
\end{aligned}
$$

(e) Thay $da=R\,dx\,d\phi$ và $r^2=x^2+R^2$. Đặt $r(x)=\sqrt{x^2+R^2}$. Mỗi thành phần có cùng mẫu số $r(x)^3$. Gọi $D$ là miền tích phân có các cận $-W/2\le x\le W/2$ và $0\le\phi\le2\pi$. Tích phân kép của từng thành phần là:

$$
\begin{aligned}
B_x &= \frac{\mu_0\sigma\omega R^3}{4\pi} \times\iint_D \frac{d\phi\,dx}{r(x)^3}, \\
B_y &= -\frac{\mu_0\sigma\omega R^2}{4\pi} \times\iint_D \frac{x\cos\phi\,d\phi\,dx}{r(x)^3}, \\
B_z &= -\frac{\mu_0\sigma\omega R^2}{4\pi} \times\iint_D \frac{x\sin\phi\,d\phi\,dx}{r(x)^3}.
\end{aligned}
$$

Các tích phân góc của $\cos\phi$ và $\sin\phi$ đều bằng không, nên $B_y=B_z=0$. Tích phân góc trong $B_x$ bằng $2\pi$:

$$
\begin{aligned}
B_x &= \frac{\mu_0\sigma\omega R^3}{2} \times\int_{-W/2}^{W/2}\frac{dx}{r(x)^3} \\
&= \frac{\mu_0\sigma\omega RW}{2}\left[R^2+(W/2)^2\right]^{-1/2} \\
&= \frac{\mu_0Q\omega}{4\pi}\left[R^2+(W/2)^2\right]^{-1/2}.
\end{aligned}
$$

(f) Vì vậy trường tại tâm đúng bằng biểu thức thu được khi chia vỏ thành các vòng:

$$
\begin{aligned}
B_x(O) &= \frac{\mu_0Q\omega}{4\pi}\left[R^2+(W/2)^2\right]^{-1/2}, \\
\vec B(O) &= B_x(O)\hat i.
\end{aligned}
$$
:::

::: exercise 28.79 ••• CP
Hai dây dẫn dài, thẳng, có khối lượng dài $\lambda$, được treo bằng dây treo để nằm ngang, song song và cách nhau $d$. Hai đầu phía sau được nối bằng dây dẫn điện trở nhỏ, chùng. Tụ đã tích điện có điện dung $C$ được mắc vào hai đầu phía trước bằng các dây nối cũng chùng, điện trở nhỏ như Hình P28.79. Bản dương ban đầu mang $+Q_0$, bản âm mang $-Q_0$.

Khi nối mạch, lực đẩy từ làm hai dây nhận vận tốc ngang ban đầu có độ lớn $v_0$. Thời gian phóng tụ rất nhỏ so với thời gian để dây dịch chuyển đáng kể. (a) Chứng minh:

$$
v_0=\frac{\mu_0Q_0^2}{4\pi\lambda RCd},
$$

trong đó $R$ là tổng điện trở mạch.

(b) Tìm độ cao $h$ mà mỗi dây dâng lên sau khi nối mạch.

![Hình P28.79: Tụ phóng qua hai dây song song, tạo xung lực từ đẩy hai dây ra xa nhau.](img/young-28/hinh-p28-79.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng phóng tụ đi theo hai chiều ngược nhau trên hai dây. Trong thời gian phóng, coi khoảng cách $d$ không đổi. Điện trở toàn mạch $R$, điện dung $C$, điện tích ban đầu $Q_0$.

**Hướng đi:**

- Dùng dòng phóng tụ theo thời gian của mạch RC, vì lực từ phụ thuộc bình phương dòng.
- Tích phân lực theo thời gian để lấy xung lực, thay vì nhân lực ban đầu với một thời gian phóng tùy chọn.
- Xét một đoạn dây bất kỳ. Chiều dài triệt tiêu khi chia xung lực cho khối lượng đoạn dây.
- Sau xung, dùng bảo toàn cơ năng của chuyển động nâng lên để tìm độ cao ở vị trí dừng tức thời.

(a) Dòng điện trong mạch là:

$$
\begin{aligned}
I(t) &= \frac{Q_0}{RC}e^{-t/(RC)}, \\
\frac{F(t)}{L} &= \frac{\mu_0I(t)^2}{2\pi d}.
\end{aligned}
$$

Với đoạn dây dài $L$, khối lượng là $\lambda L$. Xung lực cho:

$$
\begin{aligned}
\lambda L v_0 &= \int_0^\infty F(t)\,dt, \\
v_0 &= \frac{\mu_0}{2\pi\lambda d} \int_0^\infty I(t)^2\,dt.
\end{aligned}
$$

Gọi $S$ là tích phân bình phương dòng theo thời gian. Ta tính riêng đại lượng này:

$$
\begin{aligned}
S &= \int_0^\infty I(t)^2\,dt, \\
S &= \frac{Q_0^2}{R^2C^2} \times\int_0^\infty e^{-2t/(RC)}\,dt \\
&= \frac{Q_0^2}{R^2C^2}\frac{RC}{2} \\
&= \frac{Q_0^2}{2RC}.
\end{aligned}
$$

Thay lại vào xung lực:

$$
v_0=\frac{\mu_0Q_0^2}{4\pi\lambda RCd}.
$$

(b) Khi dòng đã tắt, động năng ban đầu chuyển thành thế năng trọng trường trong quá trình dây nâng lên. Ở vị trí dâng cao nhất của chuyển động này:

$$
\begin{aligned}
\frac12\lambda Lv_0^2 &= \lambda Lgh, \\
h &= \frac{v_0^2}{2g} \\
&= \frac1{2g}\left(\frac{\mu_0Q_0^2}{4\pi\lambda RCd}\right)^2.
\end{aligned}
$$

Khối lượng dài ảnh hưởng vận tốc nhận được trong xung, còn chiều dài đoạn dây đã chọn không ảnh hưởng kết quả.
:::

::: exercise 28.80 •••
Một dải cách điện rộng, dài, mang điện tích mặt đều $\sigma$ trên mặt trên. Các con lăn ở hai đầu làm dải chạy sang phải với tốc độ không đổi $v$. Tính độ lớn và chiều của từ trường tại điểm ngay phía trên dải. Xét điểm gần mặt dải và rất xa hai mép cũng như hai đầu, để dải chuyển động được xem như mặt dòng điện vô hạn của bài 28.69.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện tích mặt $\sigma$ chuyển động cùng dải với vận tốc $v$. Bỏ qua ảnh hưởng hai mép và hai đầu trong vùng xét.

**Hướng đi:**

- Dòng ở đây do điện tích chuyển động cùng vật cách điện, không cần điện tích tự do dẫn điện trong vật.
- Mật độ dòng mặt bằng điện tích mặt nhân vận tốc, có đơn vị ampere trên mét.
- Dùng kết quả mặt dòng vô hạn, thay mật độ dòng mặt $nI$ bằng $\sigma v$.

Chọn dải nằm trong mặt phẳng $xy$, chạy theo $+x$, phía trên là $+z$. Mật độ dòng mặt:

$$
\vec K=\sigma v\hat i.
$$

Trường ngay phía trên có dạng:

$$
\vec B=-\frac{\mu_0\sigma v}{2}\hat j.
$$

Độ lớn là $\mu_0|\sigma|v/2$. Với $\sigma>0$, trường nằm ngang, vuông góc chiều chạy và theo $-y$ trong hệ trục vừa chọn. Nếu điện tích mặt âm, chiều trường đảo.
:::

## Đoạn dẫn và câu hỏi MCAT

::: info BIO: Nghiên cứu vi khuẩn có từ tính
Một số vi khuẩn chứa các chuỗi hạt sắt từ song song với trục dài của chúng. Các chuỗi này hoạt động như nam châm thanh nhỏ, định hướng vi khuẩn theo từ trường Trái Đất.

Trong một thí nghiệm nghiên cứu phản ứng của những vi khuẩn ấy với từ trường, dây đồng đường kính $1{,}0\,\mathrm{mm}$ được quấn đều thành một tầng vòng xoắn. Ống dây dài $40\,\mathrm{cm}$, đường kính $12\,\mathrm{cm}$. Dây có một tầng cách điện rất mỏng. Các vòng được quấn sao cho hai vòng kề vừa chạm nhau.

Ống dây tạo từ trường được đặt trong một hộp che chắn khỏi những từ trường khác. Mẫu vi khuẩn có từ tính được đặt trong ống dây. Mômen lực lên một vi khuẩn tỉ lệ với độ lớn từ trường và với sin của góc giữa trục dài của vi khuẩn và hướng trường.
:::

::: exercise 28.81
Dòng điện trong dây phải bằng bao nhiêu để vi khuẩn chịu từ trường có độ lớn $150\,\mu\mathrm T$?

- (a) $0{,}095\,\mathrm A$.
- (b) $0{,}12\,\mathrm A$.
- (c) $0{,}30\,\mathrm A$.
- (d) $14\,\mathrm A$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Bước vòng bằng đường kính dây $1{,}0\,\mathrm{mm}$. Cần $B=150\,\mu\mathrm T$ trong mô hình ống dây dài.

**Hướng đi:**

- Các vòng vừa chạm nhau, nên số vòng trên một đơn vị chiều dài bằng nghịch đảo đường kính dây.
- Dùng $B=\mu_0nI$ ở bên trong ống dây để tìm dòng.

Mật độ vòng và số vòng của ống là:

$$
\begin{aligned}
n &= \frac1{1{,}0\times10^{-3}} \\
&= 1{,}0\times10^3\,\mathrm{m^{-1}}, \\
N &= nL=400.
\end{aligned}
$$

Dòng điện cần có:

$$
\begin{aligned}
I &= \frac B{\mu_0n} \\
&= 0{,}119\,\mathrm A \\
&\approx 0{,}12\,\mathrm A.
\end{aligned}
$$

Chọn (b).
:::

::: exercise 28.82
Để dùng mẫu lớn hơn, người thí nghiệm chế tạo ống dây có cùng chiều dài, loại dây và khoảng cách giữa các vòng, nhưng đường kính gấp đôi. So sánh mômen lực từ cực đại lên vi khuẩn trong ống mới với ống ban đầu, giả sử dòng điện trong hai ống bằng nhau. Mômen cực đại trong ống mới là:

- (a) Gấp đôi mômen trong ống ban đầu.
- (b) Bằng một nửa mômen trong ống ban đầu.
- (c) Bằng mômen trong ống ban đầu.
- (d) Bằng một phần tư mômen trong ống ban đầu.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Chiều dài, bước vòng và dòng không đổi. Chỉ đường kính khuôn trụ tăng gấp đôi.

**Hướng đi:**

- Trong mô hình ống dây dài, trường phụ thuộc $n,I$, không phụ thuộc đường kính.
- Mật độ vòng không đổi vì bước vòng không đổi.
- Với cùng vi khuẩn, mômen cực đại tỉ lệ với độ lớn trường khi sin của góc bằng một.

Ta có:

$$
\begin{aligned}
n_{\mathrm{mới}} &= n_{\mathrm{cũ}}, \\
B_{\mathrm{mới}} &= \mu_0nI=B_{\mathrm{cũ}}, \\
\tau_{\max,\mathrm{mới}} &= \tau_{\max,\mathrm{cũ}}.
\end{aligned}
$$

Chọn (c). Kết luận dùng mô hình ống dây dài bỏ qua hiệu ứng mép đang áp dụng cho các câu hỏi này.
:::

::: exercise 28.83
Lấy ống dây ra khỏi hộp che chắn và đặt ở nơi trường Trái Đất có độ lớn $50\,\mu\mathrm T$, hướng ngang. Đặt mẫu vi khuẩn ở tâm ống và dùng đúng dòng đã tạo trường $150\,\mu\mathrm T$ trong phòng thí nghiệm. Vi khuẩn chịu từ trường:

- (a) Vẫn bằng $150\,\mu\mathrm T$.
- (b) Bằng $200\,\mu\mathrm T$.
- (c) Nằm giữa $100$ và $200\,\mu\mathrm T$, tùy hướng ống dây.
- (d) Nằm giữa $50$ và $150\,\mu\mathrm T$, tùy hướng ống dây.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Trường của ống có độ lớn $B_s=150\,\mu\mathrm T$, trường Trái Đất $B_T=50\,\mu\mathrm T$. Góc giữa hai trường phụ thuộc cách đặt ống.

**Hướng đi:**

- Từ trường tuân theo nguyên lý chồng chất, nên phải cộng hai vector.
- Tổng lớn nhất khi hai trường cùng hướng, nhỏ nhất khi chúng ngược hướng.
- Các hướng trung gian cho những độ lớn nằm giữa hai giới hạn ấy.

Với góc $\alpha$ giữa hai trường:

$$
B^2 = B_s^2+B_T^2 +2B_sB_T\cos\alpha.
$$

Vì $-1\le\cos\alpha\le1$:

$$
\begin{aligned}
B_{\min} &= B_s-B_T=100\,\mu\mathrm T, \\
B_{\max} &= B_s+B_T=200\,\mu\mathrm T.
\end{aligned}
$$

Chọn (c).
:::
