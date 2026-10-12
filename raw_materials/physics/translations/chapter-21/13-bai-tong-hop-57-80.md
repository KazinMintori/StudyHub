<!-- Source: Problems21.57–21.80, printed712–714, PDF732–734. -->

## Bài tập tổng hợp

::: exercise 21.57 •••
Bốn nguồn giống nhau Q đặt tại các đỉnh hình vuông cạnh L. (a) Vẽ mọi lực tác dụng lên một nguồn. (b) Tìm độ lớn và hướng tổng lực do ba nguồn còn lại lên nguồn đó.
:::


<!-- detailed-solution:21.57 -->
::: solution Chi tiết
![Ba lực đẩy trên một điện tích ở đỉnh hình vuông](img/young-21/loi-giai-21-57.svg)
**Tóm tắt đề bài:** Bốn nguồn Q tại đỉnh vuông cạnh L, xét một đỉnh.

**Hướng đi:**

- Hai nguồn kề gây lực dọc hai cạnh, mỗi lực $F_0=kQ^2/L^2$.
- Nguồn chéo cách $L\sqrt2$ gây lực $F_0/2$ dọc đường chéo.
- Đối xứng làm tổng nằm trên đường chéo hướng ra xa tâm.

$$
\begin{aligned}
F&=\sqrt2F_0+F_0/2\\
&=\frac{kQ^2}{L^2}\left(\sqrt2+\frac12\right).
\end{aligned}
$$

Sơ đồ lực gồm hai mũi tên theo hai cạnh ra ngoài và một mũi tên theo đường chéo ra ngoài. Không gộp chúng trước khi thể hiện từng nguồn.

![Ba lực đẩy trên một điện tích ở đỉnh hình vuông](img/young-21/loi-giai-21-57.svg)

:::

::: exercise 21.58 •••
Nguồn $2.50\,\mu\mathrm C$ ở gốc và nguồn $-3.50\,\mu\mathrm C$ ở $x=0.600\,\mathrm m$, như Hình P21.58. Tìm vị trí trên trục x mà tổng lực lên điện tích nhỏ $+q$ bằng không.
:::

![Hình P21.58: Hai nguồn trái dấu cách 0,600 mét](img/young-21/hinh-p21-58.png)


<!-- detailed-solution:21.58 -->
::: solution Chi tiết
**Tóm tắt đề bài:** +2,50 µC tại gốc, −3,50 µC tại 0,600 m.

**Hướng đi:**

- Giữa hai nguồn trái dấu, hai trường cùng hướng nên không có điểm không trường.
- Điểm phải nằm ngoài về phía nguồn yếu hơn, tức x < 0.

Đặt $r=-x>0$, khoảng cách đến nguồn âm là $r+0.600$:

$$
\begin{aligned}
2.50/r^2&=3.50/(r+0.600)^2,\\
\frac{r+0.600}{r}&=\sqrt{3.50/2.50},\\
x&=-\frac{0.600}{\sqrt{3.50/2.50}-1}\\
&=-3.27\,\mathrm m.
\end{aligned}
$$
:::

::: exercise 21.59 ••
$q_1=+5.00\,\mathrm{nC}$ tại gốc và $q_2=-2.00\,\mathrm{nC}$ tại $x=4.00\,\mathrm{cm}$. (a) Đặt $q_3=+6.00\,\mathrm{nC}$ ở $(4.00\,\mathrm{cm},3.00\,\mathrm{cm})$, tìm thành phần x và y của tổng lực lên nó. (b) Tìm độ lớn và hướng lực đó.
:::


<!-- detailed-solution:21.59 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Nguồn cần xét +6,00 nC ở (4,00;3,00) cm; nguồn gốc dương và nguồn tại (4,00;0) cm âm.

**Hướng đi:**

- Nguồn gốc cách 5,00 cm đẩy theo vector đơn vị (4/5,3/5).
- Nguồn âm phía dưới cách 3,00 cm chỉ hút xuống.
- Cộng thành phần rồi lấy độ lớn.

$$
\begin{aligned}
F_x&=\frac{k(5.00)(6.00)10^{-18}}{0.0500^2}\frac45\\
&=8.63\times10^{-5}\,\mathrm N,\\
F_y&=\frac{k(5.00)(6.00)10^{-18}}{0.0500^2}\frac35\\
&\quad-\frac{k(2.00)(6.00)10^{-18}}{0.0300^2}\\
&=-5.52\times10^{-5}\,\mathrm N.
\end{aligned}
$$

Độ lớn $1.02\times10^{-4}$ N, hướng $32.6^\circ$ dưới +x.
:::

::: exercise 21.60 •• CP
Hai cầu giống nhau khối lượng m treo bằng dây lụa dài L như Hình P21.60, có điện tích $q_1=q_2=q$. Bán kính cầu rất nhỏ so với khoảng cách nên coi là điểm. Chứng tỏ khi góc $\theta$ nhỏ, khoảng cách cân bằng là:

$$
\begin{aligned}
d&=\left(\frac{q^2L}{2\pi\varepsilon_0mg}\right)^{1/3}.
\end{aligned}
$$

Gợi ý: Với góc nhỏ, $\tan\theta\approx\sin\theta$.
:::

![Hình P21.60: Hai cầu cùng điện tích treo từ một điểm và đẩy nhau](img/young-21/hinh-p21-60.png)


<!-- detailed-solution:21.60 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai cầu bằng nhau treo từ một điểm, khoảng cách d và góc lệch nhỏ θ.

**Hướng đi:**

- Cân bằng đứng cho $T\cos\theta=mg$, ngang cho $T\sin\theta=kq^2/d^2$.
- Chia hai phương trình để bỏ lực căng, rồi dùng hình học d = 2L sinθ và gần đúng góc nhỏ.

$$
\begin{aligned}
\tan\theta&=\frac{kq^2}{mgd^2},\\
\frac d{2L}&\approx\tan\theta,\\
d^3&=\frac{2kq^2L}{mg},\\
d&=\left(\frac{q^2L}{2\pi\varepsilon_0mg}\right)^{1/3}.
\end{aligned}
$$

Không dùng gần đúng này nếu góc lớn.
:::

::: exercise 21.61 ••• CP
Hai cầu nhỏ $m=15.0\,\mathrm g$ treo từ cùng điểm bằng dây lụa $L=1.20\,\mathrm m$, như Hình P21.60. Cho hai cầu điện tích âm bằng nhau q, mỗi dây lệch $25.0^\circ$ so với phương thẳng đứng. (a) Vẽ lực trên mỗi cầu, coi cầu là điểm. (b) Tìm độ lớn q. (c) Rút cả hai dây còn $0.600\,\mathrm m$, giữ điện tích không đổi. Góc lệch mới bằng bao nhiêu? Có thể giải số bằng cách thử và điều chỉnh góc đến khi phương trình tự nhất quán.
:::

![Hình P21.60: Hai cầu cùng điện tích treo từ một điểm và đẩy nhau](img/young-21/hinh-p21-60.png)


<!-- detailed-solution:21.61 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Khối lượng m = 0,0150 kg, L = 1,20 m, θ = 25,0°, sau đó L giảm còn 0,600 m.

**Hướng đi:**

- Góc 25° không đủ nhỏ để thay sin bằng tan.
- Dùng hai phương trình cân bằng chính xác và d = 2L sinθ.

$$
\begin{aligned}
q^2&=\frac{mg(2L\sin\theta)^2\tan\theta}{k},\\
|q|&=2.80\,\mu\mathrm C.
\end{aligned}
$$

Sơ đồ mỗi cầu gồm mg xuống, T dọc dây lên và lực điện ngang ra ngoài. Giữ q, m không đổi khi thay L:

$$
\begin{aligned}
\sin^2\theta_2\tan\theta_2&=\frac{L_1^2}{L_2^2}\\
&\quad\times\sin^2\theta_1\tan\theta_1.
\end{aligned}
$$

Thế $L_1/L_2=2$ và giải phương trình đơn điệu trên $(0,\pi/2)$ cho $\theta_2\approx39.5^\circ$.
:::

::: exercise 21.62 •• CP
Cầu nhỏ mang $q=5.00\,\mu\mathrm C$, khối lượng $0.500\,\mathrm g$, đang đi ngang về đông ở độ cao $60.0\,\mathrm{cm}$ so với đất. Khi vào vùng điện trường đều có độ lớn E, tốc độ là $2.00\,\mathrm{m/s}$. Tìm E nếu tốc độ ngay trước khi chạm đất là $5.00\,\mathrm{m/s}$.
:::


<!-- detailed-solution:21.62 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cầu q = 5,00 µC, m = 0,500 g, cao 0,600 m, ban đầu bay ngang 2,00 m/s và chạm đất ở 5,00 m/s.

**Hướng đi:**

- Định lý công–động năng chỉ xác định công điện, còn độ lớn E cần biết cả hướng trường và độ dời theo hướng đó.
- Đề chưa nêu hướng trường, nên không có một giá trị E duy nhất từ dữ kiện hiện có.

Ví dụ, nếu trường hướng thẳng xuống, gia tốc xuống là $g+qE/m$:

$$
\begin{aligned}
E&=\frac mq\left[\frac{v_f^2-v_0^2}{2h}-g\right]\\
&=770\,\mathrm{N/C}.
\end{aligned}
$$

Nếu trường nằm ngang hướng đông, thời gian rơi là $t=\sqrt{2h/g}$, vận tốc đứng cuối có bình phương $2gh$. Khi đó:

$$
\begin{aligned}
v_{xf}&=\sqrt{v_f^2-2gh},\\
E&=\frac{m(v_{xf}-v_0)}{qt}\\
&=468\,\mathrm{N/C}.
\end{aligned}
$$

Hai mô hình đều đạt tốc độ cuối đã cho nhưng cho E khác nhau, chứng minh cần bổ sung hướng trường trước khi chọn đáp số.
:::

::: exercise 21.63 •• CP
Quả cầu nhựa $12.3\,\mathrm g$ được buộc bằng dây rất nhẹ dài $28.6\,\mathrm{cm}$ vào tường đứng, như Hình P21.63. Trong phòng có trường đều nằm ngang. Cho cầu điện tích dư $-1.11\,\mu\mathrm C$, nó đứng yên với dây lệch $17.4^\circ$ so với tường. Tìm độ lớn và hướng trường.
:::

![Hình P21.63: Cầu âm đứng yên với dây lệch 17,4 độ khỏi tường](img/young-21/hinh-p21-63.png)


<!-- detailed-solution:21.63 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cầu âm −1,11 µC nặng 12,3 g, dây lệch 17,4° về phía phải tường.

**Hướng đi:**

- Lực điện phải ngang ra khỏi tường.
- Cân bằng hai thành phần lực căng cho $|q|E=mg\tan\theta$.
- Vì q âm, trường ngược lực điện.

$$
\begin{aligned}
E&=\frac{(0.0123)(9.8)\tan17.4^\circ}{1.11\times10^{-6}}\\
&=3.41\times10^4\,\mathrm{N/C}.
\end{aligned}
$$

Trường hướng trái, về phía tường. Chiều dài dây không đi vào cân bằng lực ở góc đã cho.
:::

::: exercise 21.64 •• CP
Cầu nhỏ dương q, khối lượng m được thả từ nghỉ trong trường đều hướng lên có độ lớn E, đủ để cầu đi lên. Thời gian đi lên quãng d bằng bao nhiêu theo q, m, d, E và g?
:::


<!-- detailed-solution:21.64 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cầu dương từ nghỉ, trường đều lên, tổng gia tốc lên.

**Hướng đi:**

- Lực điện và trọng lực ngược nhau.
- Định luật Newton cho $a=(qE-mg)/m$, rồi động học với vận tốc đầu bằng không.

$$
\begin{aligned}
t&=\sqrt{\frac{2d}{a}}\\
&=\sqrt{\frac{2md}{qE-mg}}.
\end{aligned}
$$

Điều kiện $qE>mg$ chính là điều kiện cầu gia tốc lên. Nếu bằng nhau, cầu từ nghỉ không đi lên.
:::

::: exercise 21.65 ••
Cọ bóng bay lên tóc làm electron chuyển sang bóng, khiến bóng âm. Gần trần, electron dư của bóng đẩy electron trong trần, tạo phía dương gần bóng hơn. Mô hình tương tác bằng hai điện tích điểm bằng nhau về độ lớn và trái dấu, cách $500\,\mu\mathrm m$, bỏ điện tích âm xa hơn trong trần. (a) Với bóng thường nặng $4\,\mathrm g$, ước lượng điện tích tối thiểu để bám trần. (b) Vì bóng dễ bám sau cọ xát, giả sử điện tích đạt gấp 10 giá trị tối thiểu. Ước lượng số electron đã chuyển sang bóng.
:::


<!-- detailed-solution:21.65 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Bóng 4 g được giữ bởi hai điện tích trái dấu bằng độ lớn, cách 500 µm.

**Hướng đi:**

- Điện tích tối thiểu khi lực hút vừa bằng trọng lượng.
- Đây là ước lượng nên giữ độ chính xác tương ứng giả thiết khối lượng và khoảng cách.

$$
\begin{aligned}
q_{\min}&=\sqrt{mgd^2/k}\\
&\approx1.0\,\mathrm{nC},\\
N&=10q_{\min}/e\\
&\sim6\times10^{10}.
\end{aligned}
$$

Electron chuyển sang bóng tạo điện tích âm; phần trần gần bóng có điện tích hưởng ứng dương.
:::

::: exercise 21.66 ••
Một xu Mỹ nặng $2.5\,\mathrm g$ gồm $97.5\%$ kẽm và $2.5\%$ đồng. (a) Gần đúng xu là kẽm nguyên chất, khối lượng mol $65.38\,\mathrm{g/mol}$ và 30 electron mỗi nguyên tử, ước lượng tổng số electron. (b) Ước lượng tổng điện tích electron. (c) Proton có điện tích tổng dương cùng độ lớn. Ước lượng lực giữa hai vật mang độ lớn điện tích đó, cách $2\,\mathrm{cm}$. (d) Ước lượng số lá trên cây sồi cao $60\,\mathrm{ft}$. (e) Một rừng gồm những cây đó theo lưới vuông, mỗi cây cách cây bên cạnh $10\,\mathrm m$, cần rộng bao nhiêu để số lá bằng số electron trong một xu? (f) So sánh diện tích ấy với diện tích bề mặt Trái Đất.
:::


<!-- detailed-solution:21.66 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Xu 2,5 g gần đúng là kẽm; cần nối số electron với ước lượng diện tích rừng.

**Hướng đi:**

- Số nguyên tử từ khối lượng mol, mỗi nguyên tử có 30 electron.
- Sau đó dùng điện tích tổng cho Coulomb.
- Phần rừng là bài ước lượng, cần nêu số lá giả định mỗi cây.

$$
\begin{aligned}
N_e&=30\,\frac{2.5}{65.38}N_A\\
&\approx6.9\times10^{23},\\
Q_e&=-N_ee\\
&\approx-1.1\times10^5\,\mathrm C,\\
F&=\frac{kQ_e^2}{(0.02)^2}\\
&\approx2.8\times10^{23}\,\mathrm N.
\end{aligned}
$$

Với cây cao 60 ft, lấy ước lượng $5\times10^4$ lá mỗi cây. Cần khoảng $1.4\times10^{19}$ cây. Mỗi cây chiếm ô 100 m², nên rừng rộng khoảng $1.4\times10^{21}$ m². So với diện tích Trái Đất $4\pi R_E^2\approx5.1\times10^{14}$ m², lớn hơn khoảng $2.7\times10^6$ lần. Thay giả thiết số lá làm thay đổi phần ước lượng cuối, không thay đổi số electron của xu.
:::

::: exercise 21.67 ••
Hai hạt có $q_1=0.500\,\mathrm{nC}$ và $q_2=8.00\,\mathrm{nC}$ cách $1.20\,\mathrm m$. Tại điểm nào trên đường nối chúng tổng trường bằng không?
:::


<!-- detailed-solution:21.67 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai nguồn dương 0,500 nC và 8,00 nC cách 1,20 m.

**Hướng đi:**

- Chỉ giữa hai nguồn mới có hai trường đối hướng.
- Gọi x là khoảng cách từ nguồn nhỏ, cân bằng hai độ lớn rồi lấy căn.

$$
\begin{aligned}
\frac{0.500}{x^2}&=\frac{8.00}{(1.20-x)^2},\\
1.20-x&=4x,\\
x&=0.240\,\mathrm m.
\end{aligned}
$$
:::

::: exercise 21.68 ••
Nguồn $-3.00\,\mathrm{nC}$ ở $x=1.20\,\mathrm m$, nguồn Q ở $x=-0.600\,\mathrm m$. Q có dấu và độ lớn nào để tổng trường tại gốc là (a) $45.0\,\mathrm{N/C}$ hướng $+x$ hoặc (b) cùng độ lớn hướng $-x$?
:::


<!-- detailed-solution:21.68 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Nguồn âm −3,00 nC bên phải tạo trường phải tại gốc; Q nằm bên trái.

**Hướng đi:**

- Trường nguồn đã biết tại gốc là +18,7 N/C.
- Nguồn Q phải bổ sung trường để đạt thành phần mục tiêu ±45,0 N/C.

$$
\begin{aligned}
Q&=\frac{(E_*-18.7)(0.600)^2}{k}.
\end{aligned}
$$

Ở đây $E_*$ là thành phần trường mục tiêu. (a) Với $E_*=+45.0$ N/C, $Q=+1.05$ nC. (b) Với $E_*=-45.0$ N/C, $Q=-2.55$ nC. Dấu đã được suy ra bằng trường có dấu, không lấy giá trị tuyệt đối trước khi cộng.
:::

::: exercise 21.69 •••
$+Q$ ở gốc, $+4Q$ trên trục x cách gốc d. Điện tích thứ ba q phải đặt ở đâu, có dấu và độ lớn nào để cả ba cùng cân bằng?
:::


<!-- detailed-solution:21.69 -->
::: solution Chi tiết
**Tóm tắt đề bài:** +Q ở 0, +4Q ở d; cần cả ba điện tích cân bằng.

**Hướng đi:**

- Nguồn thứ ba phải âm và nằm giữa để hút hai nguồn ngoài ngược lực đẩy của chúng.
- Vị trí phải là điểm trường không do hai nguồn ngoài, rồi độ lớn q từ cân bằng một nguồn ngoài.

$$
\begin{aligned}
Q/x^2&=4Q/(d-x)^2,\\
x&=d/3,\\
\frac{kQ|q|}{(d/3)^2}&=\frac{4kQ^2}{d^2},\\
q&=-4Q/9.
\end{aligned}
$$

Thế giá trị này cũng cân bằng nguồn 4Q. Cân bằng lực không tự bảo đảm cân bằng bền.
:::

::: exercise 21.70 ••
Nguồn $-3.00\,\mathrm{nC}$ ở gốc, nguồn $2.00\,\mathrm{nC}$ ở $(0,4.00\,\mathrm{cm})$. (a) Đặt nguồn thứ ba $5.00\,\mathrm{nC}$ tại $(3.00\,\mathrm{cm},4.00\,\mathrm{cm})$, tìm thành phần x và y của tổng lực lên nó. (b) Tìm độ lớn và hướng lực.
:::


<!-- detailed-solution:21.70 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Nguồn cần xét +5,00 nC ở (3,00;4,00) cm, nguồn gốc âm và nguồn trên y dương.

**Hướng đi:**

- Nguồn gốc hút theo hướng (−3/5,−4/5), khoảng cách 5,00 cm.
- Nguồn dương ở cùng y đẩy sang phải, khoảng cách 3,00 cm.

$$
\begin{aligned}
F_x&=-\frac35\frac{k(3.00)(5.00)10^{-18}}{0.0500^2}\\
&\quad+\frac{k(2.00)(5.00)10^{-18}}{0.0300^2}\\
&=6.75\times10^{-5}\,\mathrm N,\\
F_y&=-\frac45\frac{k(3.00)(5.00)10^{-18}}{0.0500^2}\\
&=-4.31\times10^{-5}\,\mathrm N.
\end{aligned}
$$

Độ lớn $8.01\times10^{-5}$ N, góc $32.6^\circ$ dưới +x.
:::

::: exercise 21.71 •
Ba nguồn điểm giống nhau q ở ba đỉnh hình vuông cạnh L. Tìm độ lớn và hướng tổng lực lên $-3q$ đặt (a) tại tâm hoặc (b) tại đỉnh còn trống. Trong mỗi trường hợp, vẽ sơ đồ lực do từng nguồn.
:::


<!-- detailed-solution:21.71 -->
::: solution Chi tiết
![Các lực hút lên −3q tại tâm và tại đỉnh còn trống](img/young-21/loi-giai-21-71.svg)
**Tóm tắt đề bài:** Ba nguồn q ở ba đỉnh, nguồn −3q ở tâm hoặc đỉnh trống.

**Hướng đi:**

- Sơ đồ lực có ba lực hút về từng nguồn.
- Tại tâm, dùng đối xứng của bốn đỉnh đầy đủ rồi bỏ lực của đỉnh trống.
- Tại đỉnh trống, hai lực theo cạnh cộng thành đường chéo và lực nguồn chéo cùng hướng.

(a) Mỗi lực tại tâm có độ lớn $6kq^2/L^2$. Tổng ba lực bằng âm lực đỉnh bị bỏ, nên hướng ra xa đỉnh trống với cùng độ lớn ấy.

(b) Hai lực cạnh có độ lớn $3kq^2/L^2$, lực chéo bằng nửa giá trị đó:

$$
\begin{aligned}
F&=\frac{3kq^2}{L^2}\left(\sqrt2+\frac12\right).
\end{aligned}
$$

Hướng về tâm hình vuông.

![Các lực hút lên −3q tại tâm và tại đỉnh còn trống](img/young-21/loi-giai-21-71.svg)

:::

::: exercise 21.72 •••
Giữ hai nguồn $q_1,q_2$ cách $4.50\,\mathrm{cm}$. Nguồn $Q=-1.75\,\mu\mathrm C$, khối lượng $5.00\,\mathrm g$, ban đầu cách mỗi nguồn $3.00\,\mathrm{cm}$ như Hình P21.72, được thả từ nghỉ. Gia tốc đầu của Q là $324\,\mathrm{m/s^2}$ hướng lên, song song đường nối $q_1,q_2$. Tìm $q_1,q_2$.
:::

![Hình P21.72: Nguồn Q ở trên trung trực, gia tốc đầu hướng lên](img/young-21/hinh-p21-72.png)


<!-- detailed-solution:21.72 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Q âm ở bên trái trung trực, cách hai nguồn 0,0300 m; nguồn trên $q_1$, nguồn dưới $q_2$ cách 0,0450 m.

**Hướng đi:**

- Gia tốc chỉ lên nghĩa là hai thành phần ngang triệt tiêu.
- Hai khoảng cách bằng nhau nên $q_2=-q_1$.
- Q âm phải bị hút về nguồn trên dương và bị nguồn dưới âm đẩy lên.

Góc mỗi lực có thành phần đứng bằng $0.0225/0.0300$ lần độ lớn. Do đó:

$$
\begin{aligned}
ma&=2\frac{k|Q|q_1}{r^2}\frac{0.0225}{r},\\
q_1&=+6.18\times10^{-8}\,\mathrm C,\\
q_2&=-6.18\times10^{-8}\,\mathrm C.
\end{aligned}
$$
:::

::: exercise 21.73 •• CP: Độ mạnh lực điện
Tưởng tượng hai túi proton, mỗi túi $1.0\,\mathrm g$, đặt ở hai cực bắc và nam Trái Đất. (a) Mỗi túi có bao nhiêu proton? (b) Tính lực hút hấp dẫn và lực đẩy điện giữa chúng. (c) Những lực ấy có đủ để cảm nhận nếu cầm một túi không?
:::


<!-- detailed-solution:21.73 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Mỗi túi proton 0,0010 kg, cách nhau một đường kính Trái Đất.

**Hướng đi:**

- Số proton bằng m chia khối lượng proton.
- Điện tích túi bằng Ne.
- Lực điện và hấp dẫn đều dùng cùng khoảng cách $2R_E$, nhưng phụ thuộc điện tích hoặc khối lượng khác nhau.

$$
\begin{aligned}
N&=m/m_p\approx6.0\times10^{23},\\
F_g&=Gm^2/(2R_E)^2\\
&\approx4.1\times10^{-31}\,\mathrm N,\\
F_e&=k(Ne)^2/(2R_E)^2\\
&\approx5.1\times10^5\,\mathrm N.
\end{aligned}
$$

Lực điện rất dễ cảm nhận, lực hấp dẫn giữa hai túi không thể cảm nhận trực tiếp.
:::

::: exercise 21.74 ••• CP
Hai cầu rất nhỏ $6.80\,\mathrm{mg}$ có điện tích cùng độ lớn $72.0\,\mathrm{nC}$ nhưng trái dấu, treo từ cùng móc trần bằng dây nhẹ dài $0.530\,\mathrm m$. Bật trường đều nằm ngang hướng trái, hai cầu đứng yên với góc giữa dây $58.0^\circ$ như Hình P21.74. (a) Cầu bên phải hay bên trái mang điện dương? (b) Độ lớn E bằng bao nhiêu?
:::

![Hình P21.74: Hai cầu trái dấu trong điện trường hướng trái](img/young-21/hinh-p21-74.png)


<!-- detailed-solution:21.74 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Hai cầu trái dấu treo với nửa góc giữa dây 29,0°, trường hướng trái.

**Hướng đi:**

- Trường phải kéo hai cầu ra ngoài để thắng lực hút giữa chúng.
- Vì vậy cầu trái dương, cầu phải âm.
- Cân bằng ngang của một cầu gồm lực trường ra ngoài, lực hút Coulomb vào trong và thành phần lực căng vào trong.

$$
\begin{aligned}
d&=2L\sin29.0^\circ,\\
qE&=mg\tan29.0^\circ+kq^2/d^2,\\
E&=2.96\times10^3\,\mathrm{N/C}.
\end{aligned}
$$
:::

::: exercise 21.75 •• CP
Trong mô hình nguyên tử hydrogen, electron chuyển động tròn bán kính $5.29\times10^{-11}\,\mathrm m$ quanh proton đứng yên. Tốc độ electron bằng bao nhiêu?
:::


<!-- detailed-solution:21.75 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Electron tròn bán kính $5.29\times10^{-11}$ m quanh proton đứng yên.

**Hướng đi:**

- Lực Coulomb đóng vai trò lực hướng tâm, nên $ke^2/r^2=m_ev^2/r$.
- Không cộng thêm một “lực hướng tâm” khác vào Coulomb.

$$
\begin{aligned}
v&=\sqrt{\frac{ke^2}{m_er}}\\
&=2.19\times10^6\,\mathrm{m/s}.
\end{aligned}
$$
:::

::: exercise 21.76 ••• CP
Đĩa bán kính R với mật độ mặt dương đều $\sigma$ nằm ngang trên bàn. Cầu nhựa nhỏ khối lượng M, điện tích dương Q lơ lửng đứng yên trên tâm nhờ lực đẩy Coulomb. (a) Tìm lực hướng lên tổng cộng theo độ cao z. (b) Độ cao cân bằng h bằng bao nhiêu? Biểu diễn theo hằng số không thứ nguyên $\omega=2\varepsilon_0Mg/(Q\sigma)$. (c) Với $M=100\,\mathrm g$, $Q=1\,\mu\mathrm C$, $R=5\,\mathrm{cm}$ và $\sigma=10\,\mathrm{nC/cm^2}$, h bằng bao nhiêu?
:::


<!-- detailed-solution:21.76 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Cầu dương trên trục đĩa dương, cần cân bằng với trọng lực.

**Hướng đi:**

- Trường đĩa cho lực điện hướng lên; trừ trọng lực để có tổng lực.
- Cân bằng là tổng bằng không, rồi giải theo h với tham số không thứ nguyên đã cho.

$$
\begin{aligned}
F_z(z)&=\frac{Q\sigma}{2\varepsilon_0}\\
&\quad-\frac{Q\sigma z}{2\varepsilon_0\sqrt{z^2+R^2}}\\
&\quad-Mg,\\
\frac h{\sqrt{h^2+R^2}}&=1-\omega,\\
h&=\frac{R(1-\omega)}{\sqrt{\omega(2-\omega)}}.
\end{aligned}
$$

Độ cao dương hữu hạn cần $0<\omega<1$. Với dữ kiện, $\omega=0.174$ và $h=0.0734$ m, khoảng 7,34 cm.
:::

::: exercise 21.77 •• CP
Proton được phóng vào trường đều hướng thẳng đứng lên có độ lớn E. Vận tốc đầu có độ lớn $v_0$, hợp với phương ngang góc $\alpha$ hướng xuống. (a) Tìm độ hạ thấp cực đại $h_{\max}$ so với độ cao đầu, bỏ trọng lực. (b) Sau quãng ngang d nào proton trở lại độ cao đầu? (c) Phác quỹ đạo. (d) Tính $h_{\max},d$ với $E=500\,\mathrm{N/C}$, $v_0=4.00\times10^5\,\mathrm{m/s}$, $\alpha=30.0^\circ$.
:::


<!-- detailed-solution:21.77 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Proton ban đầu đi chếch xuống, trường đều hướng lên, bỏ trọng lực.

**Hướng đi:**

- Gia tốc đứng là $a=eE/m_p$, vận tốc ngang giữ nguyên.
- Dùng động học đứng cho độ hạ thấp cực đại và thời gian trở về cùng độ cao.

$$
\begin{aligned}
v_{0x}&=v_0\cos\alpha,\\
v_{0y}&=-v_0\sin\alpha,\\
h_{\max}&=\frac{mv_0^2\sin^2\alpha}{2eE},\\
t_{\mathrm{ret}}&=\frac{2mv_0\sin\alpha}{eE},\\
d&=\frac{mv_0^2\sin2\alpha}{eE}.
\end{aligned}
$$

Quỹ đạo parabol cong lên. Số cụ thể là $h_{\max}=0.418$ m và d = 2,89 m.
:::

::: exercise 21.78 •••
Vật nhỏ khối lượng m, điện tích q, tốc độ đầu $5.00\times10^3\,\mathrm{m/s}$ được phóng vào trường giữa bản kim loại song song dài $26.0\,\mathrm{cm}$ như Hình P21.78. Trường hướng xuống, độ lớn $800\,\mathrm{N/C}$, bằng không ngoài bản. Khoảng cách hai bản đủ lớn để vật không chạm bản dưới. Sau khi qua trường, vật lệch xuống $d=1.25\,\mathrm{cm}$ và đến bản thu cách mép ra $56.0\,\mathrm{cm}$. Bỏ trọng lực và lực cản. Tính tỷ số q/m.
:::

![Hình P21.78: Vật bị lệch trong trường rồi bay đến bản thu](img/young-21/hinh-p21-78.png)


<!-- detailed-solution:21.78 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Vật qua bản dài L = 0,260 m rồi bay tự do thêm D = 0,560 m, lệch xuống d = 0,0125 m.

**Hướng đi:**

- Vận tốc ngang không đổi.
- Độ lệch có hai phần: Gia tốc trong bản và chuyển động đứng đều sau bản.
- Phải cộng cả hai, không coi tổng quãng đường đều có trường.

$$
\begin{aligned}
t_1&=L/v_0,\\
t_2&=D/v_0,\\
d&=\frac12at_1^2+(at_1)t_2,\\
a&=qE/m,\\
q/m&=\frac{2dv_0^2}{EL(L+2D)}\\
&=2.18\times10^3\,\mathrm{C/kg}.
\end{aligned}
$$

Vật lệch cùng hướng trường xuống nên q dương.
:::

::: exercise 21.79 •• CALC
Q dương phân bố đều trên trục x từ 0 đến a. Nguồn dương q tại $x=a+r$, cách đầu đoạn r như Hình P21.79. (a) Tính $E_x,E_y$ do Q tại các điểm trục x với $x>a$. (b) Tính độ lớn và hướng lực Q lên q. (c) Chứng tỏ với $r\gg a$, độ lớn lực gần bằng $Qq/(4\pi\varepsilon_0r^2)$ và giải thích.
:::

![Hình P21.79: Điện tích đều trên đoạn trục x và điện tích điểm ở bên phải](img/young-21/hinh-p21-79.png)


<!-- detailed-solution:21.79 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Q đều trên 0 ≤ ξ ≤ a; điểm khảo sát x > a.

**Hướng đi:**

- Phần nguồn $dQ=(Q/a)d\xi$ cách điểm trường $x-\xi$.
- Mọi trường đều hướng +x, nên tích phân một thành phần.
- Dùng ξ cho tọa độ nguồn để không lẫn với x của điểm khảo sát.

$$
\begin{aligned}
E_x&=\frac{kQ}{a}\int_0^a\frac{d\xi}{(x-\xi)^2}\\
&=\frac{kQ}{a}\left(\frac1{x-a}-\frac1x\right),\\
E_y&=0.
\end{aligned}
$$

Tại x = a + r:

$$
\begin{aligned}
\vec F&=\frac{kQq}{a}\left(\frac1r-\frac1{r+a}\right)\hat{\mathbf i}\\
&=\frac{kQq}{r(r+a)}\hat{\mathbf i}.
\end{aligned}
$$

Khi r ≫ a, $r+a\approx r$ nên lực gần $kQq/r^2$, vì đoạn nhìn từ xa gần như một nguồn điểm.
:::

::: exercise 21.80 •• CALC
Q dương phân bố đều trên trục y từ 0 đến a. Nguồn điểm $-q$ trên trục x dương cách gốc x, như Hình P21.80. (a) Tính $E_x,E_y$ do Q tại điểm trục x dương. (b) Tính $F_x,F_y$ lên điện tích $-q$. (c) Chứng tỏ khi $x\gg a$:

$$
\begin{aligned}
F_x&\approx-\frac{Qq}{4\pi\varepsilon_0x^2},\\
F_y&\approx+\frac{Qqa}{8\pi\varepsilon_0x^3}.
\end{aligned}
$$

Giải thích kết quả.
:::

![Hình P21.80: Đoạn nguồn dương trên y và nguồn âm trên x](img/young-21/hinh-p21-80.png)


<!-- detailed-solution:21.80 -->
::: solution Chi tiết
**Tóm tắt đề bài:** Q dương đều trên 0 ≤ y ≤ a; điểm (x,0), điện tích tại đó −q.

**Hướng đi:**

- Trường phần tử nguồn hướng theo $(x,-y)$, nên một thành phần phải và một thành phần xuống.
- Tích phân hai thành phần, rồi nhân với −q để có lực.

$$
\begin{aligned}
E_x&=\frac{kQ}{a}\int_0^a\frac{x\,dy}{(x^2+y^2)^{3/2}}\\
&=\frac{kQ}{x\sqrt{x^2+a^2}},\\
E_y&=-\frac{kQ}{a}\int_0^a\frac{y\,dy}{(x^2+y^2)^{3/2}}\\
&=-\frac{kQ}{a}\left(\frac1x-\frac1{\sqrt{x^2+a^2}}\right).
\end{aligned}
$$

Do đó $F_x=-qE_x<0$, $F_y=-qE_y>0$. Khi x ≫ a, dùng $(1+a^2/x^2)^{-1/2}\approx1-a^2/(2x^2)$:

$$
\begin{aligned}
F_x\approx-kQq/x^2,\\
F_y\approx kQqa/(2x^3).
\end{aligned}
$$

Thành phần ngang gần lực nguồn điểm Q, còn thành phần đứng nhỏ hơn một bậc khoảng cách vì nguồn trải lên phía trên.
:::
