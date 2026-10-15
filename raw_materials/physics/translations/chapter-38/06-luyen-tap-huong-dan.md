## Luyện tập hướng dẫn

Trong phần này, dùng $h=6{,}626\times10^{-34}\,\mathrm{J\,s}$, $c=2{,}998\times10^8\,\mathrm{m/s}$ và $e=1{,}602\times10^{-19}\,\mathrm C$. Khối lượng nghỉ electron là $m_e=9{,}109\times10^{-31}\,\mathrm{kg}$, còn $\hbar=h/(2\pi)$.

### Photon và hiệu ứng quang điện

Trước nhóm bài này, hãy ôn các ví dụ 38.1–38.3. Phân biệt năng lượng một photon với năng lượng cả chùm truyền trong một giây, và phân biệt công thoát với thế hãm.

::: exercise VP38.3.1. Năng lượng mỗi photon và công suất laser

Một laser phát $2{,}13\times10^{16}$ photon mỗi giây, mỗi photon có bước sóng $625\,\mathrm{nm}$. Tìm (a) năng lượng và động lượng của một photon, (b) công suất phát của laser.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Bước sóng $\lambda=625\,\mathrm{nm}$ và số photon phát mỗi giây $\dot N=2{,}13\times10^{16}\,\mathrm{s^{-1}}$.

**Hướng đi:**

- Dùng $E=hc/\lambda$ và $p=h/\lambda$ cho một photon.
- Mỗi giây có $\dot N$ photon cùng năng lượng, nên tổng năng lượng phát mỗi giây là công suất $P=\dot NE$.

(a) Năng lượng photon là

$$
E=\frac{hc}{\lambda}\approx3{,}18\times10^{-19}\,\mathrm J.
$$

Độ lớn động lượng:

$$
\begin{aligned}
p&=\frac h\lambda\\
&\approx1{,}06\times10^{-27}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

Động lượng hướng theo chiều photon truyền.

(b) Công suất laser bằng

$$
P=\dot NE\approx6{,}77\times10^{-3}\,\mathrm W.
$$

Tăng số photon mỗi giây làm tăng công suất mà không cần đổi năng lượng từng photon nếu bước sóng giữ nguyên.

:::

::: exercise VP38.3.2. Tần số ngưỡng và động năng quang electron

Một kim loại có công thoát $4{,}55\,\mathrm{eV}$. Tìm (a) tần số nhỏ nhất của ánh sáng để phát quang electron, (b) tần số để quang electron có động năng cực đại $1{,}53\,\mathrm{eV}$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Công thoát $\Phi=4{,}55\,\mathrm{eV}$. Ở phần (b), $K_{\max}=1{,}53\,\mathrm{eV}$.

**Hướng đi:**

- Dùng phương trình quang điện $hf=\Phi+K_{\max}$ vì một photon cung cấp năng lượng để electron thoát ra và phần còn lại thành động năng.
- Tại ngưỡng, động năng cực đại bằng không. Khi tính theo joule, đổi các năng lượng electronvolt bằng hệ số $e$.

(a) Tần số ngưỡng là

$$
f_{\rm th}=\frac\Phi h\approx1{,}10\times10^{15}\,\mathrm{Hz}.
$$

(b) Năng lượng photon cần có là $6{,}08\,\mathrm{eV}$, nên

$$
\begin{aligned}
f&=\frac{\Phi+K_{\max}}h\\
&\approx1{,}47\times10^{15}\,\mathrm{Hz}.
\end{aligned}
$$

:::

::: exercise VP38.3.3. Đổi bước sóng chiếu và thế hãm

Trong thí nghiệm quang điện, thế hãm bằng $1{,}37\,\mathrm V$ khi cathode được chiếu ánh sáng bước sóng $475\,\mathrm{nm}$. Tìm (a) công thoát vật liệu theo electronvolt, (b) thế hãm khi giảm bước sóng xuống $425\,\mathrm{nm}$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** $\lambda_1=475\,\mathrm{nm}$, $V_{s1}=1{,}37\,\mathrm V$ và $\lambda_2=425\,\mathrm{nm}$. Thế hãm được dùng theo độ lớn dương.

**Hướng đi:**

- Dùng $K_{\max}=eV_s$ để đổi thế hãm thành động năng cực đại.
- Công thoát thuộc vật liệu và giữ nguyên khi đổi bước sóng. Tìm nó từ lần chiếu đầu, rồi dùng lại cho lần chiếu sau.

(a) Năng lượng photon đầu xấp xỉ $2{,}61\,\mathrm{eV}$. Do đó,

$$
\Phi=\frac{hc}{\lambda_1}-eV_{s1}.
$$

Kết quả là $\Phi\approx1{,}24\,\mathrm{eV}$.

(b) Lần chiếu sau cho

$$
eV_{s2}=\frac{hc}{\lambda_2}-\Phi.
$$

Suy ra $V_{s2}\approx1{,}68\,\mathrm V$. Bước sóng ngắn hơn làm năng lượng photon và động năng cực đại tăng, nên cần thế hãm lớn hơn.

:::

::: exercise VP38.3.4. Suy công thoát từ tốc độ electron

Một thí nghiệm cho tốc độ cực đại của quang electron bằng $6{,}95\times10^5\,\mathrm{m/s}$ khi cathode được chiếu tia tử ngoại bước sóng $306\,\mathrm{nm}$. Tìm (a) động năng cực đại theo electronvolt, (b) năng lượng photon theo electronvolt, (c) công thoát vật liệu.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** $v_{\max}=6{,}95\times10^5\,\mathrm{m/s}$ và $\lambda=306\,\mathrm{nm}$.

**Hướng đi:**

- Tốc độ electron nhỏ hơn nhiều so với $c$, nên dùng gần đúng $K_{\max}=m_ev_{\max}^2/2$.
- Tính năng lượng photon bằng $hc/\lambda$.
- Lấy năng lượng photon trừ động năng cực đại để tìm công thoát, theo bảo toàn năng lượng trong quá trình quang điện.

(a) Động năng cực đại bằng $K_{\max}\approx1{,}37\,\mathrm{eV}$.

(b) Năng lượng photon bằng $E\approx4{,}05\,\mathrm{eV}$.

(c) Công thoát là

$$
\Phi=E-K_{\max}\approx2{,}68\,\mathrm{eV}.
$$

Động năng cực đại chỉ là phần năng lượng còn lại sau khi electron vượt rào công thoát.

:::

### Tán xạ Compton và hủy cặp

Trước nhóm bài này, hãy ôn các ví dụ 38.5–38.6. Công thức dịch Compton chuẩn xét hạt tán xạ ban đầu tự do và đứng yên. Trong hủy cặp đối đầu đối xứng, tổng động lượng ban đầu bằng không.

::: exercise VP38.6.1. Độ dịch bước sóng ở góc nhỏ

Một thí nghiệm Compton dùng photon tia X bước sóng $0{,}251\,\mathrm{nm}$. Ở góc tán xạ $14{,}5^\circ$, bước sóng tăng bao nhiêu so với photon tới? Viết kết quả (a) theo nanômét và (b) theo phần trăm bước sóng tới.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Photon tán xạ từ electron tự do ban đầu đứng yên, với $\lambda=0{,}251\,\mathrm{nm}$ và $\phi=14{,}5^\circ$.

**Hướng đi:**

- Dùng $\Delta\lambda=\lambda_C(1-\cos\phi)$ với $\lambda_C=h/(m_ec)$.
- Lấy độ dịch chia bước sóng tới để tìm phần trăm. Độ dịch tuyệt đối chỉ phụ thuộc góc và khối lượng hạt tán xạ, còn phần trăm còn phụ thuộc bước sóng ban đầu.

Bước sóng Compton electron xấp xỉ $\lambda_C=2{,}426\times10^{-3}\,\mathrm{nm}$.

(a) Thay góc đã cho:

$$
\Delta\lambda\approx7{,}73\times10^{-5}\,\mathrm{nm}.
$$

(b) Tỉ số là $\Delta\lambda/\lambda\approx3{,}08\times10^{-4}$, nên bước sóng tăng khoảng $0{,}0308\%$.

:::

::: exercise VP38.6.2. Tần số tia X sau tán xạ

Thí nghiệm Compton dùng tia X tần số $1{,}260\times10^{18}\,\mathrm{Hz}$. Tìm tần số photon tán xạ ở góc (a) $90{,}00^\circ$ và (b) $180{,}0^\circ$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Tần số tới $f_0=1{,}260\times10^{18}\,\mathrm{Hz}$. Electron ban đầu đứng yên. Cần phân biệt tần số với bước sóng vì công thức dịch Compton cho hiệu bước sóng.

**Hướng đi:**

- Tìm bước sóng tới $\lambda=c/f_0$.
- Cộng độ dịch Compton để có $\lambda'$, rồi lấy $f'=c/\lambda'$.
- Góc vuông cho độ dịch $\lambda_C$, còn tán xạ ngược cho độ dịch lớn nhất $2\lambda_C$.

Ta có $\lambda\approx0{,}2379\,\mathrm{nm}$.

(a) Ở $90{,}00^\circ$,

$$
\begin{aligned}
f'&=\frac{c}{\lambda+\lambda_C}\\
&\approx1{,}247\times10^{18}\,\mathrm{Hz}.
\end{aligned}
$$

(b) Ở $180{,}0^\circ$,

$$
\begin{aligned}
f'&=\frac{c}{\lambda+2\lambda_C}\\
&\approx1{,}235\times10^{18}\,\mathrm{Hz}.
\end{aligned}
$$

Tần số photon giảm ở cả hai trường hợp vì một phần năng lượng được chuyển cho electron giật lùi.

:::

::: exercise VP38.6.3. Compton trên proton

Photon có thể tán xạ Compton từ proton đứng yên, có khối lượng $1{,}673\times10^{-27}\,\mathrm{kg}$. Với photon gamma bước sóng $2{,}50\times10^{-12}\,\mathrm m$, tức $2{,}50\,\mathrm{pm}$, góc tán xạ nào làm bước sóng tăng (a) $0{,}0100\%$ và (b) $0{,}0800\%$?

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Hạt tán xạ là proton, không phải electron. Bước sóng tới $\lambda=2{,}50\,\mathrm{pm}$.

**Hướng đi:**

- Dùng cùng quan hệ dịch Compton nhưng thay khối lượng electron bằng khối lượng proton.
- Đổi phần trăm thành tỉ số trước khi nhân với bước sóng tới.
- Giải $\cos\phi=1-\Delta\lambda/\lambda_{C,p}$, đồng thời giữ miền $0\le\phi\le\pi$.

Bước sóng Compton proton là

$$
\begin{aligned}
\lambda_{C,p}&=\frac{h}{m_pc}\\
&\approx1{,}321\times10^{-15}\,\mathrm m.
\end{aligned}
$$

(a) Độ dịch cần có bằng $10^{-4}\lambda$. Thay vào cho $\phi\approx35{,}8^\circ$.

(b) Độ dịch cần có bằng $8{,}00\times10^{-4}\lambda$. Kết quả là $\phi\approx121^\circ$.

Vì proton nặng hơn electron rất nhiều, độ dịch tuyệt đối ở cùng góc nhỏ hơn tương ứng.

:::

::: exercise VP38.6.4. Proton và phản proton hủy cặp

Phản proton có cùng khối lượng và năng lượng nghỉ $938{,}3\,\mathrm{MeV}$ như proton, nhưng điện tích bằng $-e$. Một proton và một phản proton ban đầu ở xa nhau, bay thẳng về phía nhau với cùng tốc độ rồi hủy thành hai photon.

Tìm năng lượng và bước sóng mỗi photon nếu động năng ban đầu của mỗi hạt (a) không đáng kể và (b) bằng $545\,\mathrm{MeV}$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Hai hạt ban đầu có cùng khối lượng nghỉ và vận tốc đối nhau. Hệ phòng thí nghiệm cũng là hệ khối tâm. Trạng thái cuối có đúng hai photon.

**Hướng đi:**

- Tổng động lượng ban đầu bằng không, nên hai photon phải truyền ngược chiều và có cùng độ lớn động lượng.
- Với photon, $E=pc$, nên hai năng lượng bằng nhau. Bảo toàn năng lượng cho mỗi photon nhận năng lượng toàn phần của một hạt ban đầu.
- Dùng $\lambda=hc/E$ sau khi đổi MeV sang joule.

(a) Động năng không đáng kể, nên mỗi photon có

$$
E_\gamma=938{,}3\,\mathrm{MeV}.
$$

Bước sóng tương ứng là $\lambda\approx1{,}32\times10^{-15}\,\mathrm m$.

(b) Năng lượng mỗi photon bằng tổng năng lượng nghỉ và động năng của một hạt:

$$
\begin{aligned}
E_\gamma&=E_0+K\\
&=1483{,}3\,\mathrm{MeV}.
\end{aligned}
$$

Khi đó $\lambda\approx8{,}36\times10^{-16}\,\mathrm m$. Cả năng lượng nghỉ lẫn động năng ban đầu đều góp vào năng lượng photon cuối.

:::

### Xung laser và độ bất định

Trước nhóm bài này, hãy ôn ví dụ 38.7. Các độ dài và thời gian đặc trưng được dùng như độ rộng tương ứng trong mô hình ước lượng của bài. Khi yêu cầu độ bất định nhỏ nhất, ta xét giới hạn bằng trong quan hệ bất định với cùng quy ước độ rộng. Không tự đồng nhất các độ rộng này với độ rộng nửa cực đại của mọi dạng xung.

::: exercise VP38.7.1. Photon trong một xung ngắn

Laser phát ánh sáng bước sóng $633\,\mathrm{nm}$ thành các xung truyền theo chiều $+x$, mỗi xung dài $7{,}00\times10^{-6}\,\mathrm m$. Với một photon trung bình trong xung, tìm (a) động lượng, (b) độ bất định động lượng nhỏ nhất theo $\mathrm{kg\,m/s}$ và theo phần trăm động lượng trung bình, (c) năng lượng, (d) độ bất định năng lượng nhỏ nhất theo joule và theo phần trăm năng lượng trung bình.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** $\lambda=633\,\mathrm{nm}$ và chiều dài xung $L=7{,}00\times10^{-6}\,\mathrm m$. Xét truyền theo một phương, lấy $\Delta x=L$ trong ước lượng này.

**Hướng đi:**

- Dùng $p=h/\lambda$ và $E=pc$ cho photon trung bình.
- Quan hệ vị trí–động lượng cho $\Delta p=\hbar/(2L)$ trong mô hình độ rộng được chọn.
- Với photon truyền theo cùng chiều, $E=cp$ là tuyến tính nên $\Delta E=c\Delta p$. Hai tỉ số bất định tương đối vì thế bằng nhau.

(a) Động lượng trung bình có độ lớn

$$
p\approx1{,}05\times10^{-27}\,\mathrm{kg\,m/s}.
$$

Hướng động lượng là $+x$.

(b) Độ bất định nhỏ nhất là

$$
\begin{aligned}
\Delta p&=\frac{\hbar}{2L}\\
&\approx7{,}53\times10^{-30}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

Tỉ số $\Delta p/p$ tương ứng khoảng $0{,}720\%$.

(c) Năng lượng trung bình là $E\approx3{,}14\times10^{-19}\,\mathrm J$.

(d) Độ bất định năng lượng nhỏ nhất là

$$
\begin{aligned}
\Delta E&=c\Delta p\\
&\approx2{,}26\times10^{-21}\,\mathrm J.
\end{aligned}
$$

Nó cũng bằng khoảng $0{,}720\%$ năng lượng trung bình.

:::

::: exercise VP38.7.2. Xung radar thời tiết

Một hệ radar thời tiết phát sóng vô tuyến thành xung, với tần số điển hình $3{,}00\,\mathrm{GHz}$. Độ bất định năng lượng nhỏ nhất của photon vô tuyến là $5{,}50\times10^{-29}\,\mathrm J$.

Tìm (a) thời gian mỗi xung, (b) chiều dài mỗi xung, (c) năng lượng photon trung bình, (d) độ bất định tần số nhỏ nhất. Biết $1\,\mathrm{GHz}=10^9\,\mathrm{Hz}$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** $f=3{,}00\times10^9\,\mathrm{Hz}$ và $\Delta E=5{,}50\times10^{-29}\,\mathrm J$. Xét mô hình xung đạt giới hạn độ rộng năng lượng–thời gian đã dùng trong chương.

**Hướng đi:**

- Dùng $\Delta t=\hbar/(2\Delta E)$ để tìm độ rộng thời gian trong mô hình giới hạn.
- Chiều dài xung truyền trong chân không là $L=c\Delta t$.
- Dùng $E=hf$ và $\Delta E=h\Delta f$ để liên hệ năng lượng trung bình với độ rộng phổ.

(a) Thời gian đặc trưng của xung là

$$
\Delta t\approx9{,}59\times10^{-7}\,\mathrm s.
$$

(b) Chiều dài xung bằng khoảng $2{,}87\times10^2\,\mathrm m$ với các hằng số đã nêu, tức khoảng $2{,}9\times10^2\,\mathrm m$.

(c) Năng lượng photon trung bình:

$$
E=hf\approx1{,}99\times10^{-24}\,\mathrm J.
$$

(d) Độ bất định tần số nhỏ nhất:

$$
\begin{aligned}
\Delta f&=\frac{\Delta E}h\\
&\approx8{,}30\times10^4\,\mathrm{Hz}.
\end{aligned}
$$

Kết quả cũng bằng $8{,}30\times10^{-5}\,\mathrm{GHz}$.

:::

::: exercise VP38.7.3. Suy bước sóng và thời gian từ độ rộng năng lượng

Một laser xung có độ bất định năng lượng photon nhỏ nhất $2{,}33\times10^{-20}\,\mathrm J$, bằng $6{,}70\%$ năng lượng photon trung bình. Tìm (a) bước sóng và tần số trung bình, (b) độ bất định tần số nhỏ nhất, (c) thời gian xung.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** $\Delta E=2{,}33\times10^{-20}\,\mathrm J$ và $\Delta E/E=0{,}0670$.

**Hướng đi:**

- Tìm năng lượng trung bình từ phần trăm đã cho trước khi suy tần số và bước sóng.
- Dùng tính tuyến tính $E=hf$ để chuyển độ bất định năng lượng thành độ bất định tần số.
- Xung được xét ở giới hạn nhỏ nhất tương ứng, nên dùng $\Delta t=\hbar/(2\Delta E)$ với quy ước của mô hình.

(a) Năng lượng trung bình là

$$
E=\frac{\Delta E}{0{,}0670}.
$$

Suy ra $\lambda\approx571\,\mathrm{nm}$ và $f\approx5{,}25\times10^{14}\,\mathrm{Hz}$ với các hằng số ở đầu phần.

(b) Độ bất định tần số nhỏ nhất là $\Delta f\approx3{,}52\times10^{13}\,\mathrm{Hz}$.

(c) Độ rộng thời gian xung là

$$
\Delta t\approx2{,}26\times10^{-15}\,\mathrm s.
$$

Giữ năng lượng trung bình không đổi mà làm xung ngắn hơn sẽ đòi hỏi phổ năng lượng rộng hơn trong cùng mô hình.

:::

::: exercise VP38.7.4. Năng lượng một xung có nhiều photon

Một chùm laser xung có năng lượng photon trung bình $2{,}39\,\mathrm{eV}$ và độ bất định năng lượng nhỏ nhất $0{,}0155\,\mathrm{eV}$. Mỗi xung có trung bình $5{,}00\times10^{12}$ photon.

Tìm (a) thời gian mỗi xung, (b) bước sóng ánh sáng, (c) năng lượng mỗi xung theo joule.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** $E=2{,}39\,\mathrm{eV}$, $\Delta E=0{,}0155\,\mathrm{eV}$ và $N=5{,}00\times10^{12}$.

**Hướng đi:**

- Đổi các năng lượng theo electronvolt sang joule trước khi dùng $\hbar$ theo đơn vị SI.
- Tìm thời gian xung từ giới hạn năng lượng–thời gian trong mô hình đã chọn.
- Bước sóng dùng năng lượng một photon, còn năng lượng cả xung bằng số photon nhân năng lượng trung bình mỗi photon.

(a) Thời gian xung bằng

$$
\begin{aligned}
\Delta t&=\frac{\hbar}{2\Delta E}\\
&\approx2{,}12\times10^{-14}\,\mathrm s.
\end{aligned}
$$

(b) Bước sóng trung bình là $\lambda=hc/E\approx519\,\mathrm{nm}$.

(c) Năng lượng trung bình mỗi xung, ký hiệu $E_x$, là

$$
\begin{aligned}
E_x&=NE\\
&\approx1{,}91\times10^{-6}\,\mathrm J.
\end{aligned}
$$

Đây là khoảng $1{,}91\,\mu\mathrm J$. Tiền tố micro tương ứng $10^{-6}$, nên không được đổi giá trị này thành $1{,}91\,\mathrm{mJ}$.

:::

### Bài tập cầu nối: Compton và electron giật lùi

::: exercise Bài cầu nối 38. Photon tán xạ ngược

Một photon tia X tán xạ từ electron tự do ban đầu đứng yên. Photon quay ngược lại ở góc $180^\circ$ và có bước sóng sau tán xạ $0{,}0830\,\mathrm{nm}$.

(a) Bước sóng tới bằng bao nhiêu? (b) Độ lớn động lượng và tốc độ electron sau va chạm bằng bao nhiêu? (c) Động năng electron bằng bao nhiêu? Hãy đối chiếu với phần năng lượng photon bị mất. Có thể dùng gần đúng phi tương đối tính cho electron nếu tốc độ thu được nhỏ hơn khoảng $0{,}1c$.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Electron đứng yên trước va chạm, $\phi=180^\circ$ và $\lambda'=0{,}0830\,\mathrm{nm}$. Chọn chiều dương theo photon tới.

**Hướng đi:**

- Dùng độ dịch Compton ngược $\lambda'-\lambda=2\lambda_C$ để tìm bước sóng ban đầu.
- Photon tán xạ có động lượng ngược chiều photon tới. Bảo toàn động lượng vì thế cho động lượng electron bằng tổng hai độ lớn động lượng photon.
- Tính tốc độ và động năng bằng công thức tương đối tính, rồi so với gần đúng $p_e=m_ev$ và $K=p_e^2/(2m_e)$.
- Bảo toàn năng lượng yêu cầu động năng electron bằng năng lượng photon tới trừ năng lượng photon tán xạ.

(a) Với $\lambda_C=h/(m_ec)$,

$$
\lambda=\lambda'-2\lambda_C\approx0{,}0781\,\mathrm{nm}.
$$

(b) Sơ đồ động lượng có photon tới theo chiều dương, photon cuối theo chiều âm và electron cuối theo chiều dương. Phương trình một chiều là

![Lời giải cầu nối: Photon tán xạ ngược, còn electron nhận động lượng theo chiều photon tới. Các mũi tên chỉ hướng, không theo tỉ lệ độ lớn.](img/young-38/loi-giai-38-cau-noi.svg)

$$
\frac h\lambda=-\frac h{\lambda'}+p_e.
$$

Suy ra

$$
\begin{aligned}
p_e&=\frac h\lambda+\frac h{\lambda'}\\
&\approx1{,}65\times10^{-23}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

Năng lượng toàn phần electron là

$$
E_e=\sqrt{(m_ec^2)^2+(p_ec)^2}.
$$

Từ $v=p_ec^2/E_e$, ta có $v\approx1{,}80\times10^7\,\mathrm{m/s}$, xấp xỉ $0{,}0602c$. Gần đúng phi tương đối tính cho $v\approx1{,}81\times10^7\,\mathrm{m/s}$, phù hợp với mức chính xác cần xét.

(c) Động năng từ bảo toàn năng lượng là

$$
\begin{aligned}
K&=\frac{hc}{\lambda}-\frac{hc}{\lambda'}\\
&\approx1{,}49\times10^{-16}\,\mathrm J.
\end{aligned}
$$

Tính bằng $E_e-m_ec^2$ cho cùng giá trị. Gần đúng $p_e^2/(2m_e)$ cũng cho $1{,}49\times10^{-16}\,\mathrm J$ ở ba chữ số có nghĩa. Photon đã mất đúng phần năng lượng chuyển thành động năng giật lùi của electron.

:::
