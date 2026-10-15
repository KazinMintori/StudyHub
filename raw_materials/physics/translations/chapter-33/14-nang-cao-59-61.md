## Bài tập nâng cao 33.59–33.61

::: exercise 33.59
Cáp quang có lõi trụ mảnh đường kính $d$, chiết suất $n_1$, và vỏ có $n_2<n_1$. Tia bị giữ trong lõi khi góc tới tại thành không nhỏ hơn góc giới hạn. Hình P33.59 mô tả tia trong cáp đã uốn tới giới hạn trước khi bắt đầu rò sáng. Bán kính cong của đường giữa lõi là $R$.

(a) Dựng tam giác vuông có các đỉnh $a,b,c$ như hình để tìm góc tới $\theta$ của tia tại thành ngoài.

(b) Tìm bán kính cong giới hạn theo $n_1,n_2,d$.

(c) Lõi dày $50{,}0\,\mathrm{\mu m}$, có $n_1=1{,}4475$, còn $n_2=1{,}4440$. Tìm bán kính cong nhỏ nhất.

(d) Tia đi qua chiều dài cáp $1{,}00\,\mathrm{km}$ uốn tới giới hạn, theo đường xiên cực đại như hình. Vì phản xạ nhiều lần, tia đi thêm bao nhiêu so với $1{,}00\,\mathrm{km}$? Giữ đủ chữ số trong các bước trung gian.

(e) Ánh sáng mất thêm bao nhiêu thời gian để truyền qua đoạn cáp đó so với đi $1{,}00\,\mathrm{km}$ trong không khí?

![Hình P33.59: Tia tiếp tuyến với biên trong và phản xạ tại biên ngoài của lõi quang bị uốn cong.](img/young-33/hinh-p33-59.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Bán kính biên trong và biên ngoài lần lượt là $R_i=R-d/2$ và $R_o=R+d/2$. Điểm $c$ là tâm cong. Tia đi qua $a$ và tiếp tuyến với biên trong tại $b$.

**Hướng đi:**

- Trong tam giác vuông $cba$, khoảng cách từ tâm tới tia là $R_i$, còn cạnh huyền là $R_o$. Vì thế tỉ số hai bán kính xác định sin của góc tới tại $a$.
- Ghép điều kiện này với Snell tại góc giới hạn để tìm $R$.
- Với câu (d), so sánh chiều dài một dây cung giữa hai lần phản xạ với chiều dài cung tương ứng của đường giữa lõi.
- Với câu (e), phải tính cả tốc độ giảm trong lõi và phần đường tăng do tia đi xiên.

(a) Vì $cb$ vuông góc với tia:

$$
\begin{aligned}
\sin\theta &= \frac{cb}{ca} \\
&= \frac{R_i}{R_o} \\
&= \frac{R-d/2}{R+d/2}.
\end{aligned}
$$

(b) Tại giới hạn, $\sin\theta=n_2/n_1$. Đặt $\eta=n_2/n_1$ để viết gọn bước nhân chéo:

$$
\begin{aligned}
R-d/2 &= \eta(R+d/2), \\
(n_1-n_2)R &= \frac{(n_1+n_2)d}{2}, \\
R_{\rm crit} &= \frac{(n_1+n_2)d}{2(n_1-n_2)}.
\end{aligned}
$$

Tăng $R$ làm góc tới tăng, nên điều kiện giữ tia là $R\ge R_{\rm crit}$ trong mô hình tia giới hạn này. Phát biểu rằng góc tới không được lớn hơn góc giới hạn sẽ đảo điều kiện vật lý. Phản xạ toàn phần cần góc tới lớn hơn ngưỡng, với trường hợp bằng ngưỡng là cận giới hạn.

(c) Thay số bằng mét:

$$
\begin{aligned}
d &= 50{,}0\times10^{-6}\,\mathrm m, \\
R_{\rm crit} &= 0{,}02065357\,\mathrm m \\
&= 2{,}07\,\mathrm{cm}.
\end{aligned}
$$

(d) Xét cáp có độ cong giới hạn không đổi dọc đoạn đang xét, và tia liên tiếp đi theo các dây cung tiếp tuyến biên trong. Gọi $\alpha$ là nửa góc ở tâm chắn một dây cung. Khi đó:

$$
\begin{aligned}
\cos\alpha &= \frac{R_i}{R_o} \\
&= \frac{n_2}{n_1}, \\
\alpha &= 3{,}985198^\circ.
\end{aligned}
$$

Giữa hai lần phản xạ liên tiếp, tia đi quãng đường $\ell$, còn cung đường giữa lõi có chiều dài $s$:

$$
\begin{aligned}
\ell &= 2R_o\sin\alpha, \\
s &= 2R\alpha.
\end{aligned}
$$

Trong biểu thức độ dài cung, $\alpha$ phải tính bằng radian. Từ $2R=R_o+R_i$ suy ra:

$$
\begin{aligned}
\chi &= \frac\ell s =\frac{2\sin\alpha}{(1+\cos\alpha)\alpha} \\
&= \frac{\tan(\alpha/2)}{\alpha/2} \\
&= 1{,}0004033513.
\end{aligned}
$$

Với chiều dài đường giữa lõi $L=1000\,\mathrm m$:

$$
\begin{aligned}
L_{\rm tia} &= \chi L, \\
\Delta L &= (\chi-1)L \\
&= 0{,}403\,\mathrm m.
\end{aligned}
$$

Tia đi thêm khoảng $40\,\mathrm{cm}$. Kết quả này ứng với hình học uốn đều và đường tia giới hạn đã nêu. Nếu chỉ một phần cáp bị uốn hoặc đường tia khác, phải tính theo chiều dài từng đoạn tương ứng.

(e) Tốc độ trong lõi là $c/n_1$. Lấy chiết suất không khí bằng 1:

$$
\begin{aligned}
\Delta t &= \frac{n_1\chi L}{c}-\frac Lc \\
&= \frac{L(n_1\chi-1)}c \\
&= 1{,}49\times10^{-6}\,\mathrm s \\
&= 1{,}49\,\mathrm{\mu s}.
\end{aligned}
$$
:::

::: exercise 33.60
Cầu vồng hình thành khi ánh sáng Mặt Trời khúc xạ và phản xạ trong các giọt nước gần hình cầu. Hình P33.60 cho tia đi vào tại $A$, phản xạ một lần tại $B$, rồi đi ra tại $C$. Các góc tới và khúc xạ ở mỗi điểm được ký hiệu như hình.

(a) Chứng minh góc tới tại $B$ và tại $C$ đều bằng góc khúc xạ tại $A$, còn góc khúc xạ tại $C$ bằng góc tới tại $A$.

(b) Cộng các độ đổi hướng ở $A,B,C$ để chứng minh góc lệch toàn phần, tính bằng radian, là $\Delta=\pi+2\theta_a^A-4\theta_b^A$.

(c) Dùng Snell viết $\Delta$ theo góc tới ban đầu và chiết suất nước $n$.

(d) Cầu vồng sáng ở hướng mà góc lệch dừng theo góc tới. Chứng minh giá trị góc tới $\theta_1$ tại đó thỏa mãn:

$$
\cos^2\theta_1=\frac{n^2-1}{3}.
$$

Có thể dùng công thức đạo hàm của hàm arcsin để xét điều kiện này.

(e) Với ánh sáng tím, $n=1{,}342$, còn với ánh sáng đỏ, $n=1{,}330$. Tính $\theta_1$ và $\Delta$ cho từng màu. Đối chiếu bán kính góc của cầu vồng bậc một ở Hình 33.19d. Màu đỏ hay màu tím nằm cao hơn trên chân trời?

![Hình P33.60: Đường tia tạo cầu vồng bậc một với hai lần khúc xạ và một lần phản xạ nội.](img/young-33/hinh-p33-60.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Đặt $i=\theta_a^A$ và $r=\theta_b^A$. Không khí có chiết suất xấp xỉ 1. Các pháp tuyến tại mặt giọt nước đều đi qua tâm cầu.

**Hướng đi:**

- Dùng các tam giác cân nối tâm với hai điểm gặp mặt cầu để truyền quan hệ góc từ $A$ đến $B,C$.
- Cộng góc đổi hướng của từng lần khúc xạ và phản xạ, thay vì đọc góc lệch trực tiếp từ hình.
- Dùng Snell để loại $r$, rồi lấy đạo hàm theo $i$ để tìm hướng tập trung tia.
- Phân biệt góc đổi hướng $\Delta$ với bán kính góc cầu vồng quanh điểm đối nhật.

(a) Nếu $O$ là tâm giọt, tam giác $OAB$ cân vì $OA=OB$. Vì vậy góc tia với pháp tuyến ở $B$ bằng $r$. Phản xạ tại $B$ giữ nguyên góc này. Tam giác $OBC$ cũng cân nên góc tới ở $C$ bằng $r$:

$$
\begin{aligned}
\theta_a^B &= r, \\
\theta_a^C &= r.
\end{aligned}
$$

Snell tại $A$ cho $\sin i=n\sin r$. Tại $C$, quan hệ ngược lại cho $\sin\theta_b^C=n\sin r=\sin i$. Với các góc khúc xạ nằm trong miền vật lý, $\theta_b^C=i$.

(b) Mỗi lần khúc xạ làm tia đổi hướng $i-r$. Một lần phản xạ nội làm tia đổi hướng $\pi-2r$. Tổng cộng:

$$
\Delta = 2(i-r)+(\pi-2r) = \pi+2i-4r.
$$

(c):

$$
\begin{aligned}
r &= \arcsin\!\left(\frac{\sin i}{n}\right), \\
\Delta(i) &= \pi+2i \\
-4\arcsin\! &\left(\frac{\sin i}{n}\right).
\end{aligned}
$$

(d) Lấy đạo hàm Snell với $n$ cố định:

$$
\begin{aligned}
\frac{dr}{di} &= \frac{\cos i}{n\cos r}, \\
\frac{d\Delta}{di} &= 2-\frac{4\cos i}{n\cos r}.
\end{aligned}
$$

Đạo hàm bằng 0 khi $n\cos r=2\cos i$. Bình phương, rồi dùng $n\sin r=\sin i$:

$$
\begin{aligned}
n^2\cos^2r &= 4\cos^2i, \\
n^2-\sin^2i &= 4\cos^2i, \\
n^2-1 &= 3\cos^2i.
\end{aligned}
$$

Suy ra hệ thức cần chứng minh. Quanh góc dừng, một khoảng góc tới tạo ra khoảng góc ló hẹp, nên mật độ tia theo góc tăng lên và tạo vành sáng.

(e):

| Đại lượng | Ánh sáng tím | Ánh sáng đỏ |
| --- | --- | --- |
| Góc tới dừng $\theta_1$ | $58{,}888^\circ$ | $59{,}585^\circ$ |
| Góc khúc xạ $r$ | $39{,}641^\circ$ | $40{,}422^\circ$ |
| Góc đổi hướng $\Delta$ | $139{,}213^\circ$ | $137{,}484^\circ$ |
| Bán kính góc $180^\circ-\Delta$ | $40{,}787^\circ$ | $42{,}516^\circ$ |

Hai bán kính góc làm tròn thành $40{,}8^\circ$ và $42{,}5^\circ$, phù hợp Hình 33.19d. Màu đỏ ở ngoài và cao hơn màu tím trên cung phía trên chân trời.
:::

::: exercise 33.61
Cầu vồng bậc hai được tạo bởi tia trải qua hai lần phản xạ nội trong giọt nước hình cầu như Hình 33.19e. Dùng hình học của bài 33.60.

(a) Biểu diễn góc đổi hướng toàn phần $\Delta$ theo góc tới ban đầu $\theta_a^A$ và chiết suất $n$.

(b) Tìm góc tới $\theta_2$ tại đó đạo hàm của $\Delta$ theo góc tới bằng 0.

(c) Dùng chiết suất tím $1{,}342$ và đỏ $1{,}330$ để tính $\theta_2,\Delta$. Đối chiếu Hình 33.19e. Màu đỏ hay màu tím cao hơn trên chân trời? Giải thích.

![Hình 33.19: Cầu vồng bậc hai ở phần e hình thành với hai lần phản xạ nội và có thứ tự màu đảo ngược cầu vồng bậc một.](img/young-33/hinh-33-19.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Đặt $i=\theta_a^A$, $r$ là góc khúc xạ trong giọt. Tia có hai lần khúc xạ và hai lần phản xạ nội.

**Hướng đi:**

- Cộng hai góc khúc xạ $i-r$ và hai góc phản xạ $\pi-2r$.
- Dùng điều kiện đạo hàm bằng 0 như ở bài 33.60, với hệ số của $r$ thay đổi.
- Đọc bán kính góc từ hướng quay ngược, vì góc đổi hướng có hướng của tia bậc hai vượt $180^\circ$.

(a):

$$
\begin{aligned}
\Delta &= 2(i-r)+2(\pi-2r) \\
&= 2\pi+2i-6r, \\
r &= \arcsin\!\left(\frac{\sin i}{n}\right).
\end{aligned}
$$

Ở đây $\Delta$ là tổng góc quay có hướng cộng dọc đường tia. Nó không phải góc nhỏ không định hướng giữa hai vectơ, vốn luôn không vượt $180^\circ$.

(b):

$$
\frac{d\Delta}{di} =2-\frac{6\cos i}{n\cos r}.
$$

Đạo hàm bằng 0 khi $n\cos r=3\cos i$.

Bình phương và dùng Snell:

$$
\begin{aligned}
n^2-\sin^2i &= 9\cos^2i, \\
n^2-1 &= 8\cos^2i, \\
\cos^2\theta_2 &= \frac{n^2-1}{8}.
\end{aligned}
$$

(c):

| Đại lượng | Ánh sáng tím | Ánh sáng đỏ |
| --- | --- | --- |
| Góc tới dừng $\theta_2$ | $71{,}554^\circ$ | $71{,}940^\circ$ |
| Góc khúc xạ $r$ | $44{,}981^\circ$ | $45{,}630^\circ$ |
| Góc đổi hướng có hướng $\Delta$ | $233{,}222^\circ$ | $230{,}101^\circ$ |
| Bán kính góc $\Delta-180^\circ$ | $53{,}222^\circ$ | $50{,}101^\circ$ |

Các bán kính góc lần lượt là $53{,}2^\circ$ cho tím và $50{,}1^\circ$ cho đỏ. Màu tím ở ngoài và cao hơn màu đỏ, đảo thứ tự của cầu vồng bậc một. Sau hai lần phản xạ, năng lượng còn lại nhỏ hơn vì một phần ánh sáng đã khúc xạ thoát ra ở mỗi lần gặp mặt sau, nên cầu vồng bậc hai mờ hơn.
:::
