## Luyện tập hướng dẫn

### Nhiễu xạ một khe

::: exercise VP36.3.1
Laser bước sóng $645\,\mathrm{nm}$ truyền qua khe rộng $0{,}250\,\mathrm{mm}$. Quan sát hệ vân trên màn ở xa. Hai cực tiểu bậc hai ở hai phía vân trung tâm cách nhau $28{,}0\,\mathrm{mm}$. (a) Màn cách khe bao nhiêu? (b) Nếu bước sóng là $525\,\mathrm{nm}$, hai cực tiểu ấy cách nhau bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $a=0{,}250\,\mathrm{mm}$, $\lambda=645\,\mathrm{nm}$, $m=2$. Khoảng từ tâm tới mỗi cực tiểu là $y_2=14{,}0\,\mathrm{mm}$.

**Hướng đi:**

- Dùng $a\sin\theta_m=m\lambda$ vì đây là cực tiểu khe đơn.
- Dùng $y_m=R\tan\theta_m$ để giữ đúng hình học của màn phẳng.
- Giữ nguyên a và R khi thay bước sóng.

(a) Góc của cực tiểu bậc hai thỏa:

$$
\sin\theta_2=\frac{2\lambda}{a}=0{,}00516.
$$

Do đó:

$$
\begin{aligned}
R &= \frac{14{,}0\times10^{-3}}{\tan\theta_2}\,\mathrm m\\
&= 2{,}71314\,\mathrm m\\
&\approx 2{,}71\,\mathrm m.
\end{aligned}
$$

(b) Với bước sóng mới, tìm góc mới rồi dùng cùng khoảng màn:

$$
\begin{aligned}
\sin\theta'_2 &= \frac{2\lambda'}a,\\
W' &= 2R\tan\theta'_2\\
&= 22{,}7906\,\mathrm{mm}\\
&\approx 22{,}8\,\mathrm{mm}.
\end{aligned}
$$

Trong gần đúng góc nhỏ, khoảng cách này cũng bằng khoảng ban đầu nhân tỉ số hai bước sóng. Bước sóng giảm làm hệ vân co lại.
:::

::: exercise VP36.3.2
Chiếu laser vào khe rộng $0{,}221\,\mathrm{mm}$. Trên màn cách khe $5{,}00\,\mathrm m$, cực tiểu thứ ba cách tâm vân sáng trung tâm $45{,}7\,\mathrm{mm}$. Tìm (a) bước sóng laser và (b) góc giữa đường từ tâm khe tới vân tối thứ hai với trục của hệ vân.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $a=0{,}221\,\mathrm{mm}$, $R=5{,}00\,\mathrm m$, $y_3=45{,}7\,\mathrm{mm}$.

**Hướng đi:**

- Dùng $\tan\theta_3=y_3/R$ vì dữ kiện là vị trí trên màn.
- Dùng $a\sin\theta_m=m\lambda$ để suy bước sóng rồi góc của bậc hai.

(a) Từ vị trí vân tối:

$$
\begin{aligned}
\theta_3 &= \arctan(y_3/R),\\
\lambda &= \frac{a\sin\theta_3}{3}\\
&= 673{,}285\,\mathrm{nm}\\
&\approx 673\,\mathrm{nm}.
\end{aligned}
$$

(b) Thay bậc hai:

$$
\begin{aligned}
\theta_2 &= \arcsin(2\lambda/a)\\
&= 0{,}3491^\circ.
\end{aligned}
$$

Hai phía màn có các góc đối nhau, cùng độ lớn trên.
:::

::: exercise VP36.3.3
Tại một điểm của hệ vân nhiễu xạ khe đơn, các sóng thứ cấp từ hai mép khe có độ lệch pha $35{,}0\,\mathrm{rad}$. Khe rộng $0{,}250\,\mathrm{mm}$, ánh sáng có bước sóng $545\,\mathrm{nm}$. (a) Đường từ tâm khe tới điểm ấy tạo góc bao nhiêu với trục hệ vân? (b) Nếu cường độ tại tâm là $I_0$, cường độ tại điểm ấy bằng bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Độ lệch pha giữa hai mép là $\beta=35{,}0\,\mathrm{rad}$. Đối số trong biểu thức cường độ là $\alpha=\beta/2$.

**Hướng đi:**

- Dùng $\beta=2\pi a\sin\theta/\lambda$ vì hiệu đường đi giữa hai mép là $a\sin\theta$.
- Dùng $I/I_0=(\sin\alpha/\alpha)^2$ vì phải cộng đóng góp của toàn khe, không chỉ hai mép.

(a):

$$
\begin{aligned}
\sin\theta &= \frac{\beta\lambda}{2\pi a},\\
\theta &= 0{,}69579^\circ\\
&\approx 0{,}696^\circ.
\end{aligned}
$$

(b):

$$
\begin{aligned}
\alpha &= 17{,}5\,\mathrm{rad},\\
\frac I{I_0} &= \left(\frac{\sin17{,}5}{17{,}5}\right)^2\\
&= 0{,}00310807.
\end{aligned}
$$

Vậy $I\approx0{,}00311I_0$. Các góc trong hàm sin của biểu thức này được tính bằng radian.
:::

::: exercise VP36.3.4
Trong thí nghiệm nhiễu xạ khe đơn, khe rộng $0{,}185\,\mathrm{mm}$ và ánh sáng có bước sóng $576\,\mathrm{nm}$. (a) Tìm góc từ tâm khe tới vân tối đầu tiên. (b) Ở một nửa góc này, điểm quan sát nằm giữa tâm vân sáng có cường độ $I_0$ và cực tiểu có cường độ bằng không. Cường độ thực tại góc ấy có bằng $I_0/2$ không? Tính giá trị thực.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $a=0{,}185\,\mathrm{mm}$, $\lambda=576\,\mathrm{nm}$. Câu (b) hỏi cường độ tại góc bằng nửa góc cực tiểu, không yêu cầu nội suy tuyến tính.

**Hướng đi:**

- Dùng $\sin\theta_1=\lambda/a$ vì cực tiểu đầu có bậc một.
- Thay $\theta=\theta_1/2$ vào $\alpha=\pi a\sin\theta/\lambda$, rồi tính bình phương sinc.

(a):

$$
\begin{aligned}
\theta_1 &= \arcsin(\lambda/a)\\
&= 0{,}178391^\circ.
\end{aligned}
$$

(b) Tại $\theta=0{,}0891957^\circ$:

$$
\begin{aligned}
\alpha &= \frac{\pi a}{\lambda}\sin(\theta_1/2),\\
\frac I{I_0} &= \left(\frac{\sin\alpha}{\alpha}\right)^2\\
&= 0{,}405284.
\end{aligned}
$$

Vậy cường độ khoảng $0{,}405I_0$, không phải $0{,}500I_0$. Trong gần đúng góc nhỏ, đối số bằng $\pi/2$, cho cùng kết quả ở độ chính xác đang xét. Cường độ biến thiên theo bình phương sinc, không tuyến tính theo góc.
:::

### Cách tử và nhiễu xạ tia X

::: exercise VP36.5.1
Laser tới vuông góc một cách tử truyền qua có $825$ khe trên mỗi milimet. Vùng sáng bậc hai ở góc $41{,}0^\circ$ so với cực đại trung tâm. Tìm (a) bước sóng và (b) góc của các vùng sáng bậc một và bậc ba.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mật độ khe là $825\,\mathrm{mm^{-1}}$, nên khoảng khe là nghịch đảo mật độ. Hai khe kề nhau cùng được chiếu đồng pha.

**Hướng đi:**

- Dùng $d\sin\theta_m=m\lambda$ vì cực đại chính cách tử có pha của các khe trùng nhau.
- Kiểm tra $|m\lambda/d|\le1$ trước khi lấy hàm arcsin.

(a):

$$
\begin{aligned}
d &= \frac{10^{-3}}{825}\,\mathrm m,\\
\lambda &= \frac{d\sin41{,}0^\circ}{2}\\
&= 397{,}612\,\mathrm{nm}\\
&\approx 398\,\mathrm{nm}.
\end{aligned}
$$

(b):

$$
\begin{aligned}
\theta_1 &= \arcsin(\lambda/d)\\
&= 19{,}1^\circ,\\
\theta_3 &= \arcsin(3\lambda/d)\\
&= 79{,}8^\circ.
\end{aligned}
$$

Cả hai bậc đều tồn tại. Góc bậc ba rất lớn nên không dùng gần đúng góc nhỏ.
:::

::: exercise VP36.5.2
Cực đại bậc một của cách tử nhiễu xạ ở góc $24{,}0^\circ$ so với cực đại trung tâm. Ánh sáng bước sóng $625\,\mathrm{nm}$ tới vuông góc cách tử. Tìm (a) số khe trên mỗi milimet và (b) góc của vùng sáng bậc hai và bậc ba, nếu có.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $\lambda=625\,\mathrm{nm}$, $\theta_1=24{,}0^\circ$. Mật độ khe bằng $1/d$.

**Hướng đi:**

- Dùng $d=\lambda/\sin\theta_1$ vì cực đại đã biết có bậc một.
- Dùng $\sin\theta_m=m\sin\theta_1$ vì giữ cùng d và bước sóng.

(a):

$$
\begin{aligned}
\frac1d &= \frac{\sin24{,}0^\circ}{625\times10^{-9}}\,\mathrm{m^{-1}}\\
&= 650{,}779\,\mathrm{mm^{-1}}.
\end{aligned}
$$

Vậy cách tử có khoảng $651$ khe trên mỗi milimet.

(b):

$$
\begin{aligned}
\theta_2 &= \arcsin(2\sin24{,}0^\circ)\\
&= 54{,}4^\circ.
\end{aligned}
$$

Với bậc ba, biểu thức hình thức cho $\sin\theta_3=1{,}22021>1$. Không có cực đại bậc ba.
:::

::: exercise VP36.5.3
Các mặt mạng của một tinh thể cách nhau $0{,}165\,\mathrm{nm}$. Chiếu chùm tia X có bước sóng $0{,}124\,\mathrm{nm}$ vào tinh thể. (a) Cực đại giao thoa mạnh đầu tiên xuất hiện ở góc bao nhiêu giữa chùm tia và mặt mạng? (b) Ở những góc lớn hơn nào, nếu có, còn xuất hiện cực đại mạnh?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $d=0{,}165\,\mathrm{nm}$ và $\lambda=0{,}124\,\mathrm{nm}$. Góc được đo với mặt mạng, khác góc tới đo với pháp tuyến.

**Hướng đi:**

- Dùng $2d\sin\theta=m\lambda$ vì hiệu đường đi giữa hai mặt mạng liên tiếp là $2d\sin\theta$.
- Giữ các bậc nguyên dương cho sin không lớn hơn một.

(a) Với $m=1$:

$$
\begin{aligned}
\theta_1 &= \arcsin\frac{0{,}124}{2(0{,}165)}\\
&= 22{,}1^\circ.
\end{aligned}
$$

(b) Bậc hai cho:

$$
\begin{aligned}
\theta_2 &= \arcsin\frac{2(0{,}124)}{2(0{,}165)}\\
&= 48{,}7^\circ.
\end{aligned}
$$

Từ bậc ba trở lên, giá trị sin yêu cầu vượt một. Vì vậy chỉ còn một cực đại mạnh ở góc lớn hơn là $48{,}7^\circ$.
:::

::: exercise VP36.5.4
Trong thí nghiệm nhiễu xạ tia X, chỉ có một cực đại giao thoa mạnh, khi chùm tia hợp với mặt mạng góc $36{,}0^\circ$. Khoảng mặt mạng là $0{,}158\,\mathrm{nm}$. (a) Bước sóng tia X bằng bao nhiêu? (b) Muốn có ba cực đại mạnh, với cực đại thứ ba ở góc $88{,}0^\circ$, cần bước sóng bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xét các bậc Bragg dương. Chỉ có một cực đại nên cực đại đang thấy thuộc bậc một.

**Hướng đi:**

- Dùng $\lambda=2d\sin\theta/m$ vì mỗi cực đại mạnh có bậc Bragg xác định.
- Sau khi tìm bước sóng, kiểm tra số bậc thỏa $m\lambda\le2d$.

(a):

$$
\begin{aligned}
\lambda &= 2(0{,}158)\sin36{,}0^\circ\,\mathrm{nm}\\
&= 0{,}185740\,\mathrm{nm}\\
&\approx 0{,}186\,\mathrm{nm}.
\end{aligned}
$$

Tỉ số $2d/\lambda\approx1{,}70$ xác nhận không có bậc hai.

(b) Đặt cực đại ở $88{,}0^\circ$ là bậc ba:

$$
\begin{aligned}
\lambda' &= \frac{2d\sin88{,}0^\circ}{3}\\
&= 0{,}105269\,\mathrm{nm}\\
&\approx 0{,}105\,\mathrm{nm}.
\end{aligned}
$$

Các góc của ba bậc lần lượt là $19{,}5^\circ$, $41{,}8^\circ$ và $88{,}0^\circ$. Bậc bốn đòi hỏi sin lớn hơn một nên không xuất hiện.
:::

### Khẩu độ tròn và giới hạn phân giải

::: exercise VP36.6.1
Bạn muốn khảo sát bức xạ vô tuyến từ Mặt Trời ở bước sóng $1{,}70\,\mathrm{cm}$. Để thấy các chi tiết trên bề mặt không lớn hơn đường kính Trái Đất, giới hạn phân giải của kính phải là $9{,}00\times10^{-5}\,\mathrm{rad}$, khoảng $0{,}005^\circ$. Dùng tiêu chuẩn Rayleigh để tìm (a) đường kính nhỏ nhất của kính vô tuyến và (b) giới hạn phân giải của kính ấy ở bước sóng $21{,}1\,\mathrm{cm}$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Kính được mô hình hóa bằng khẩu độ tròn có đường kính D. Câu (b) giữ nguyên khẩu độ, chỉ đổi bước sóng.

**Hướng đi:**

- Dùng $\sin\theta=1{,}22\lambda/D$ vì tiêu chuẩn Rayleigh của khẩu độ tròn dùng bán kính góc của vòng tối đầu.
- Với D cố định, bước sóng tăng làm góc phân giải tối thiểu tăng.

(a):

$$
\begin{aligned}
D_{\min} &= \frac{1{,}22\lambda}{\sin\theta}\\
&= 230{,}444\,\mathrm m\\
&\approx 230\,\mathrm m.
\end{aligned}
$$

(b):

$$
\begin{aligned}
\theta' &= \arcsin\frac{1{,}22\lambda'}D\\
&= 1{,}11706\times10^{-3}\,\mathrm{rad}\\
&\approx 0{,}0640^\circ.
\end{aligned}
$$

Góc phân giải lớn hơn nghĩa là hai chi tiết phải xa nhau hơn theo góc mới được tách biệt.
:::

::: exercise VP36.6.2
Ống kính tele của máy ảnh có tiêu cự $0{,}250\,\mathrm m$ và khẩu độ lớn nhất $f/4{,}0$. Lấy bước sóng ánh sáng là $5{,}50\times10^{-7}\,\mathrm m$. (a) Nếu giới hạn phân giải chỉ do nhiễu xạ, vật có thể ở xa nhất bao nhiêu để phân giải được hai điểm cách nhau $5{,}00\,\mathrm{mm}$? (b) Hai điểm tương ứng trên ảnh qua ống kính cách nhau bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Chỉ số khẩu độ là $N=f/D=4{,}0$. Khoảng hai điểm vật là $s=5{,}00\,\mathrm{mm}$.

**Hướng đi:**

- Dùng $D=f/N$ vì độ mở được cho bằng chỉ số khẩu độ.
- Dùng tiêu chuẩn Rayleigh để tìm góc nhỏ nhất, rồi $s=u\tan\theta$ để tìm khoảng vật u.
- Dùng phương trình kính mỏng và độ phóng đại vì câu (b) hỏi khoảng cách trên ảnh.

(a):

$$
\begin{aligned}
D &= \frac{0{,}250}{4{,}0}\,\mathrm m\\
&= 0{,}0625\,\mathrm m,\\
\sin\theta &= \frac{1{,}22\lambda}D,\\
\theta &\approx 1{,}0736\times10^{-5}\,\mathrm{rad}.
\end{aligned}
$$

Khoảng vật lớn nhất là:

$$
\begin{aligned}
u_{\max} &= \frac{s}{\tan\theta}\\
&\approx 466\,\mathrm m.
\end{aligned}
$$

(b) Gọi v là khoảng ảnh. Với thấu kính mỏng:

$$
\begin{aligned}
v &= \frac{fu}{u-f},\\
s' &= \frac vu s\\
&\approx 2{,}685\,\mu\mathrm m\\
&\approx 2{,}7\,\mu\mathrm m.
\end{aligned}
$$

Vì $u\gg f$, lấy mặt phẳng ảnh gần tiêu diện cũng cho $s'\approx f\theta=2{,}684\,\mu\mathrm m$. Chênh lệch hai cách nhỏ hơn độ chính xác dữ kiện khẩu độ.
:::

::: exercise VP36.6.3
Một nguồn sáng điểm ở xa, chẳng hạn một ngôi sao, phát ánh sáng bước sóng $575\,\mathrm{nm}$. Khi ánh sáng đi vào máy ảnh có tiêu cự ống kính $135\,\mathrm{mm}$, ảnh nhiễu xạ trên bộ thu có đĩa Airy bán kính $0{,}0112\,\mathrm{mm}$. Tìm (a) đường kính khẩu độ và (b) chỉ số khẩu độ.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn ở xa tạo ảnh gần tiêu diện. Bán kính đĩa Airy trên ảnh là $\rho=0{,}0112\,\mathrm{mm}$.

**Hướng đi:**

- Dùng $\tan\theta_1=\rho/f$ để đổi kích thước trên bộ thu thành bán kính góc.
- Dùng $\sin\theta_1=1{,}22\lambda/D$ và $N=f/D$ vì khẩu độ được coi tròn.

(a):

$$
\begin{aligned}
\theta_1 &= \arctan(\rho/f),\\
D &= \frac{1{,}22\lambda}{\sin\theta_1}\\
&= 8{,}45558\,\mathrm{mm}\\
&\approx 8{,}46\,\mathrm{mm}.
\end{aligned}
$$

(b):

$$
\begin{aligned}
N &= \frac fD\\
&= 15{,}9658\\
&\approx 16{,}0.
\end{aligned}
$$

Ống kính đang làm việc ở khoảng khẩu độ $f/16$.
:::

::: exercise VP36.6.4
Một mục tiêu của thiên văn học là chế tạo kính trong không gian có thể phân giải hành tinh giống Trái Đất quay quanh sao khác. Hành tinh cách sao $1{,}5\times10^{11}\,\mathrm m$, bằng bán kính quỹ đạo Trái Đất quanh Mặt Trời. Kính có gương đường kính $8{,}0\,\mathrm m$. Theo tiêu chuẩn Rayleigh, hệ sao–hành tinh có thể ở xa nhất bao nhiêu nếu bước sóng dùng là (a) $690\,\mathrm{nm}$ và (b) $1400\,\mathrm{nm}$? Cho đáp số theo năm ánh sáng, với $1\,\mathrm{ly}=9{,}46\times10^{15}\,\mathrm m$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xét khoảng cách chiếu lên phương ngang đường ngắm bằng khoảng sao–hành tinh đã cho. Bỏ qua các hạn chế khác ngoài nhiễu xạ trong mô hình yêu cầu.

**Hướng đi:**

- Dùng tiêu chuẩn Rayleigh cho khẩu độ gương tròn.
- Dùng $L=s/\tan\theta$ vì hai vật ở xa có khoảng cách ngang s ứng với độ tách góc nhỏ.

Với cùng đường kính gương:

$$
\begin{aligned}
\theta &= \arcsin\frac{1{,}22\lambda}D,\\
L_{\max} &= \frac{s}{\tan\theta}\\
&\approx \frac{sD}{1{,}22\lambda}.
\end{aligned}
$$

(a) Ở bước sóng $690\,\mathrm{nm}$:

$$
\begin{aligned}
L_{\max} &= 150{,}689\,\mathrm{ly}\\
&\approx 1{,}5\times10^2\,\mathrm{ly}.
\end{aligned}
$$

(b) Ở bước sóng $1400\,\mathrm{nm}$:

$$
\begin{aligned}
L_{\max} &= 74{,}2681\,\mathrm{ly}\\
&\approx 74\,\mathrm{ly}.
\end{aligned}
$$

Bước sóng dài hơn làm giảm khoảng quan sát tối đa. Đây là giới hạn hình học do nhiễu xạ, chưa phải bảo đảm có thể tách tín hiệu hành tinh khỏi ánh sáng sao sáng hơn nhiều.
:::

### Bài cầu nối: Quan sát vũ trụ giãn nở

::: exercise Bài cầu nối 36
Một nhà thiên văn nhận dạng được phổ hydrogen từ một thiên hà, nhưng thấy các bước sóng lệch so với giá trị trong phòng thí nghiệm. Vạch $H_\alpha$ trong phòng thí nghiệm có bước sóng $656{,}3\,\mathrm{nm}$. Dùng cách tử truyền qua có $5758$ vạch trên mỗi centimét, nhà thiên văn đo được vân sáng bậc một của vạch ấy ở góc $\pm23{,}41^\circ$ so với vân trung tâm.

Thiên hà đang chuyển động nhanh bao nhiêu? Cho tốc độ theo mét trên giây và phần trăm tốc độ ánh sáng. Thiên hà tiến lại gần hay rời xa người quan sát?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Cần tìm bước sóng nhận được từ cách tử, sau đó dùng Doppler điện từ. Lấy vận tốc dọc đường ngắm là v dương khi nguồn rời xa.

**Hướng đi:**

- Dùng $d\sin\theta=\lambda_R$ vì đang đo cực đại bậc một ở tới vuông góc.
- Dùng quan hệ Doppler điện từ tương đối tính vì tốc độ cần tìm được suy từ tỉ số bước sóng.
- So bước sóng nhận được với bước sóng phát để xác định chiều chuyển động.

Khoảng giữa hai vạch cách tử là:

$$
d=\frac1{5758\times100}\,\mathrm m.
$$

Lấy độ lớn góc bậc một:

$$
\begin{aligned}
\lambda_R &= d\sin23{,}41^\circ\\
&= 690{,}011\,\mathrm{nm}.
\end{aligned}
$$

Đặt $q=\lambda_R/\lambda_S$ và $\beta=v/c$. Quan hệ Doppler theo quy ước chiều đang dùng là:

$$
\begin{aligned}
q &= \sqrt{\frac{1+\beta}{1-\beta}},\\
q^2(1-\beta) &= 1+\beta,\\
\beta &= \frac{q^2-1}{q^2+1}.
\end{aligned}
$$

Thay $\lambda_S=656{,}3\,\mathrm{nm}$:

$$
\begin{aligned}
q &= 1{,}0513645,\\
\beta &= 0{,}0500470,\\
v &\approx 1{,}50\times10^7\,\mathrm{m/s}.
\end{aligned}
$$

Tốc độ bằng khoảng $5{,}00\%$ tốc độ ánh sáng. Bước sóng nhận được lớn hơn bước sóng phát, nên phổ bị dịch đỏ và thiên hà đang rời xa theo phương đường ngắm. Dấu của tốc độ phù hợp phép so sánh hai bước sóng.
:::
