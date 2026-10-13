## Luyện tập có hướng dẫn

### Từ thông, định luật Faraday và định luật Lenz

Hãy ôn các Ví dụ 29.1, 29.2, 29.3 cùng hai Ví dụ định tính 29.7 và 29.8 trước khi làm bốn bài dưới đây.

::: exercise VP29.8.1
Một vòng dây tròn đơn có bán kính $2{,}40\,\mathrm{cm}$ nằm trong mặt phẳng $xy$. Từ trường đều biến đổi với tốc độ không đổi từ $0{,}140\,\mathrm T$ theo chiều $+z$ tại $t=0$ đến $0{,}110\,\mathrm T$ theo chiều $-z$ tại $t=2{,}00\,\mathrm s$. Chọn vector diện tích theo chiều $+z$.

(a) Tìm từ thông qua vòng tại hai thời điểm trên.

(b) Tìm độ lớn suất điện động cảm ứng trong thời gian từ trường biến đổi.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $r=0{,}0240\,\mathrm m$, $B_z(0)=0{,}140\,\mathrm T$, $B_z(2{,}00\,\mathrm s)=-0{,}110\,\mathrm T$. Tìm hai từ thông và độ lớn suất điện động.

**Hướng đi:**

- Dùng $A=\pi r^2$ và $\Phi_B=B_zA$ vì từ trường đều và vector diện tích hướng theo $+z$.
- Dùng định luật Faraday. Tốc độ biến thiên không đổi nên đạo hàm từ thông bằng hiệu từ thông chia cho khoảng thời gian.

Diện tích của vòng là

$$
A=\pi(0{,}0240)^2\,\mathrm{m^2}.
$$

(a) Dấu từ thông được quyết định bởi chiều từ trường so với vector diện tích:

$$
\begin{aligned}
&\Phi_B(0) = 0{,}140A = 2{,}53\times10^{-4}\,\mathrm{Wb},\\
&\Phi_B(2{,}00\,\mathrm s) = -0{,}110A = -1{,}99\times10^{-4}\,\mathrm{Wb}.
\end{aligned}
$$

(b) Từ thông giảm từ giá trị dương đến giá trị âm. Do đó

$$
|\mathcal E| = A\frac{0{,}140+0{,}110}{2{,}00} = 2{,}26\times10^{-4}\,\mathrm V.
$$
:::

::: exercise VP29.8.2
Một cuộn dây tròn có 455 vòng, bán kính $5{,}00\,\mathrm{cm}$ và điện trở $14{,}5\,\Omega$. Vector diện tích hướng theo $+z$. Từ trường đều hợp với chiều $+z$ một góc $20{,}0^\circ$. Độ lớn từ trường ban đầu là $0{,}0600\,\mathrm T$ và giảm với tốc độ

$$
\frac{dB}{dt}=-3{,}00\times10^{-3}\,\mathrm{T/s}.
$$

Tìm độ lớn của (a) suất điện động cảm ứng và (b) dòng điện cảm ứng trong cuộn.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $N=455$, $r=0{,}0500\,\mathrm m$, $R=14{,}5\,\Omega$, góc giữa từ trường và pháp tuyến là $20{,}0^\circ$. Tìm suất điện động và dòng điện khi độ lớn trường giảm đều.

**Hướng đi:**

- Dùng $\Phi_B=BA\cos20{,}0^\circ$ cho mỗi vòng vì chỉ thành phần từ trường vuông góc mặt vòng đóng góp vào từ thông.
- Nhân tốc độ biến thiên từ thông với $N$ vì 455 vòng nối tiếp có cùng diện tích và hướng.
- Dùng $I=|\mathcal E|/R$ vì điện trở toàn cuộn đã biết.

(a) Diện tích mỗi vòng là $A=\pi(0{,}0500)^2\,\mathrm{m^2}$. Góc và diện tích không đổi nên

$$
|\mathcal E| = NA\cos20{,}0^\circ\left|\frac{dB}{dt}\right| = 1{,}01\times10^{-2}\,\mathrm V.
$$

(b) Dòng cảm ứng có độ lớn

$$
I = \frac{|\mathcal E|}{14{,}5\,\Omega} = 6{,}95\times10^{-4}\,\mathrm A.
$$
:::

::: exercise VP29.8.3
Một cuộn dây vuông cạnh $4{,}00\,\mathrm{cm}$, gồm 875 vòng, nằm trong mặt phẳng $xy$. Từ trường đều biến đổi với tốc độ không đổi từ

$$
\begin{aligned}
&\vec B(0) = (0{,}200\,\mathrm T)\hat{\imath}\\
&\quad +(0{,}150\,\mathrm T)\hat{k}
\end{aligned}
$$

đến

$$
\begin{aligned}
&\vec B(3{,}00\,\mathrm s) = (0{,}300\,\mathrm T)\hat{\imath}\\
&\quad -(0{,}200\,\mathrm T)\hat{k}.
\end{aligned}
$$

Tại $t=2{,}00\,\mathrm s$, tìm (a) độ lớn suất điện động cảm ứng và (b) chiều dòng điện khi nhìn từ một điểm trên trục $+z$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Cuộn có $N=875$, diện tích mỗi vòng $A=(0{,}0400\,\mathrm m)^2$. Thành phần $B_z$ giảm từ $0{,}150\,\mathrm T$ đến $-0{,}200\,\mathrm T$ trong $3{,}00\,\mathrm s$.

**Hướng đi:**

- Chọn vector diện tích theo $+z$. Thành phần $B_x$ song song mặt cuộn nên không tạo từ thông qua cuộn.
- Dùng định luật Faraday với thành phần $B_z$. Tốc độ biến thiên không đổi nên suất điện động không phụ thuộc thời điểm trong khoảng đang xét.
- Dùng định luật Lenz để xác định chiều dòng tạo từ trường cảm ứng theo $+z$, chống lại sự giảm của $B_z$.

(a) Ta có

$$
\begin{aligned}
&\frac{dB_z}{dt} = \frac{-0{,}200-0{,}150}{3{,}00}\,\mathrm{T/s},\\
&\mathcal E = -NA\frac{dB_z}{dt} = 0{,}163\,\mathrm V.
\end{aligned}
$$

(b) Suất điện động dương theo chiều dương gắn với pháp tuyến $+z$. Dòng điện ngược chiều kim đồng hồ khi nhìn từ trục $+z$ về cuộn. Từ trường do dòng ấy sinh ra hướng theo $+z$.
:::

::: exercise VP29.8.4
Một cuộn có diện tích mỗi vòng $A$, gồm $N$ vòng, nằm trong mặt phẳng $xy$. Vector diện tích hướng theo $+z$. Cuộn đặt trong từ trường đều biến thiên theo thời gian:

$$
\vec B=(B_0\sin\omega t)\hat{k},
$$

với $\omega>0$ và $B_0$ là biên độ dương.

(a) Tìm suất điện động cảm ứng trong cuộn.

(b) Nhìn từ trục $+z$, dòng cảm ứng có chiều nào tại $t=0$ và $t=\pi/\omega$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Cuộn cố định có pháp tuyến $+z$ và từ thông mỗi vòng $\Phi_B=AB_0\sin\omega t$.

**Hướng đi:**

- Lấy đạo hàm từ thông trong định luật Faraday vì chỉ từ trường biến đổi.
- Dùng dấu của suất điện động theo quy ước chiều dương ngược chiều kim đồng hồ khi nhìn từ $+z$.

(a) Suất điện động là

$$
\mathcal E = -N\frac{d\Phi_B}{dt} = -\omega NAB_0\cos\omega t.
$$

(b) Tại $t=0$, suất điện động âm nên dòng chạy theo chiều kim đồng hồ. Tại $t=\pi/\omega$, suất điện động dương nên dòng chạy ngược chiều kim đồng hồ. Ở cả hai thời điểm, từ trường tức thời bằng không nhưng tốc độ biến thiên từ trường khác không.
:::

### Suất điện động do chuyển động

Hãy ôn Ví dụ 29.9 trước khi làm bốn bài dưới đây.

::: exercise VP29.9.1
Một thanh dẫn cô lập dài $8{,}00\,\mathrm{cm}$ đặt song song trục $x$. Thanh chuyển động theo chiều $+y$ với tốc độ $3{,}90\,\mathrm{m/s}$ trong từ trường đều có độ lớn $0{,}600\,\mathrm T$, hướng theo $-z$.

(a) Tìm độ lớn suất điện động do chuyển động trong thanh.

(b) Tìm độ lớn và hướng của điện trường được tạo ra trong thanh.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $L=0{,}0800\,\mathrm m$, vận tốc hướng $+y$, từ trường hướng $-z$. Thanh hở nên điện tích phân bố lại đến khi lực điện cân bằng lực từ.

**Hướng đi:**

- Dùng $|\mathcal E|=vBL$ vì thanh, vận tốc và từ trường vuông góc từng đôi.
- Dùng $\vec E=-\vec v\times\vec B$ từ điều kiện cân bằng điện tích trong thanh cô lập, để tìm cả độ lớn lẫn hướng điện trường.

(a) Suất điện động có độ lớn

$$
|\mathcal E| = (3{,}90)(0{,}600)(0{,}0800)\,\mathrm V = 0{,}187\,\mathrm V.
$$

(b) Tích có hướng $\vec v\times\vec B$ hướng theo $-x$. Điện trường cân bằng hướng theo $+x$ và có độ lớn

$$
E=vB=2{,}34\,\mathrm{V/m}.
$$
:::

::: exercise VP29.9.2
Trong máy phát thanh trượt ở Hình 29.15b, đảo chiều chuyển động để thanh đi sang trái. Thanh dài $5{,}00\,\mathrm{cm}$, chuyển động với tốc độ $2{,}40\,\mathrm{m/s}$ trong từ trường đều $0{,}150\,\mathrm T$. Điện trở mạch tại thời điểm xét là $0{,}0200\,\Omega$. Tìm dòng cảm ứng và chiều dòng chạy quanh mạch.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Thanh là cạnh phải của mạch, chuyển động sang trái trong từ trường hướng vào mặt hình. $L=0{,}0500\,\mathrm m$, $v=2{,}40\,\mathrm{m/s}$, $B=0{,}150\,\mathrm T$, $R=0{,}0200\,\Omega$.

**Hướng đi:**

- Dùng $|\mathcal E|=vBL$ và định luật Ohm vì thanh tạo suất điện động trong mạch kín có điện trở đã biết.
- Dùng Lenz. Diện tích mạch giảm nên dòng cảm ứng phải tạo từ trường vào mặt hình, duy trì từ thông đang giảm.

Ta có

$$
\begin{aligned}
&|\mathcal E| = 0{,}0180\,\mathrm V,\\
&I = \frac{0{,}0180}{0{,}0200}\,\mathrm A = 0{,}900\,\mathrm A.
\end{aligned}
$$

Dòng điện chạy theo chiều kim đồng hồ. Trên thanh chuyển động, dòng chạy từ đầu trên xuống đầu dưới.
:::

::: exercise VP29.9.3
Một thanh dẫn cô lập dài $8{,}00\,\mathrm{cm}$ song song trục $x$. Tại $t=0$, đầu $a$ ở gốc tọa độ, đầu $b$ ở $x=8{,}00\,\mathrm{cm}$, $y=z=0$. Thanh chuyển động với vận tốc không đổi

$$
\begin{aligned}
&\vec v = (1{,}50\,\mathrm{m/s})\hat{\imath}\\
&\quad +(2{,}00\,\mathrm{m/s})\hat{\jmath}
\end{aligned}
$$

trong từ trường đều

$$
\begin{aligned}
&\vec B = -(0{,}120\,\mathrm T)\hat{\imath}\\
&\quad +(0{,}150\,\mathrm T)\hat{k}.
\end{aligned}
$$

(a) Tìm độ lớn suất điện động cảm ứng trong thanh.

(b) Đầu nào có điện thế cao hơn?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Chiều từ $a$ đến $b$ là $+x$, độ dài $0{,}0800\,\mathrm m$. Vận tốc và từ trường có nhiều thành phần nên cần lấy đúng tích có hướng.

**Hướng đi:**

- Dùng tích phân của $\vec v\times\vec B$ dọc thanh. Chỉ thành phần theo $x$ góp vào suất điện động giữa hai đầu.
- Xác định đầu điện thế cao bằng chiều lực từ lên điện tích dương, hoặc bằng điện trường cân bằng $\vec E=-\vec v\times\vec B$.

Tích có hướng cho

$$
\begin{aligned}
&\vec v\times\vec B = (0{,}300\,\mathrm{V/m})\hat{\imath}\\
&\quad -(0{,}225\,\mathrm{V/m})\hat{\jmath}\\
&\quad +(0{,}240\,\mathrm{V/m})\hat{k}.
\end{aligned}
$$

(a) Thành phần dọc thanh không đổi nên

$$
|\mathcal E| = (0{,}300)(0{,}0800)\,\mathrm V = 2{,}40\times10^{-2}\,\mathrm V.
$$

(b) Lực từ lên điện tích dương có thành phần theo $+x$, hướng về đầu $b$. Điện tích dương dồn về đầu này, nên $V_b>V_a$. Hiệu điện thế là $V_b-V_a=0{,}0240\,\mathrm V$.
:::

::: exercise VP29.9.4
Lực từ tác dụng lên thanh trong máy phát thanh trượt có độ lớn $0{,}0600\,\mathrm N$ khi điện trở mạch bằng $0{,}750\,\Omega$. Thanh dài $0{,}190\,\mathrm m$. Từ trường đều $0{,}550\,\mathrm T$ vuông góc mặt phẳng máy phát. Tìm tốc độ của thanh.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $F_B=0{,}0600\,\mathrm N$, $R=0{,}750\,\Omega$, $L=0{,}190\,\mathrm m$, $B=0{,}550\,\mathrm T$. Tìm $v$.

**Hướng đi:**

- Dùng lực từ $F_B=IBL$ vì thanh vuông góc từ trường.
- Thay $I=vBL/R$ từ suất điện động chuyển động và định luật Ohm, rồi giải theo tốc độ.

$$
\begin{aligned}
&F_B = \frac{B^2L^2v}{R},\\
&v = \frac{F_BR}{B^2L^2} = 4{,}12\,\mathrm{m/s}.
\end{aligned}
$$
:::

### Điện trường cảm ứng

Hãy ôn Ví dụ 29.11 trước khi làm bốn bài dưới đây.

::: exercise VP29.11.1
Một ống dây dài có tiết diện $3{,}00\,\mathrm{cm^2}$. Dòng điện qua các vòng ống dây giảm với tốc độ $22{,}0\,\mathrm{A/s}$. Một vòng dây bán kính $3{,}10\,\mathrm{cm}$ bao quanh ống dây, song song các vòng của ống và có tâm trên trục ống. Độ lớn suất điện động cảm ứng trong vòng là $15{,}0\,\mu\mathrm V$.

(a) Tìm số vòng trên một mét chiều dài ống dây.

(b) Tìm độ lớn điện trường cảm ứng tại các điểm trên vòng dây bao quanh.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $A_s=3{,}00\times10^{-4}\,\mathrm{m^2}$, $|dI/dt|=22{,}0\,\mathrm{A/s}$, $r=0{,}0310\,\mathrm m$ và $|\mathcal E|=15{,}0\,\mu\mathrm V$.

**Hướng đi:**

- Dùng $B=\mu_0nI$ và từ thông qua tiết diện ống dây. Bỏ qua từ trường bên ngoài ống dài, nên không dùng toàn bộ diện tích vòng lớn để tính từ thông.
- Dùng $2\pi rE=|\mathcal E|$ vì điện trường cảm ứng tiếp tuyến và có cùng độ lớn trên đường tròn đồng tâm.

(a) Theo Faraday,

$$
\begin{aligned}
&|\mathcal E| = \mu_0nA_s\left|\frac{dI}{dt}\right|,\\
&n = \frac{|\mathcal E|}{\mu_0A_s|dI/dt|} = 1{,}81\times10^3\,\mathrm{m^{-1}}.
\end{aligned}
$$

(b) Trên vòng dây,

$$
E = \frac{15{,}0\times10^{-6}}{2\pi(0{,}0310)}\,\mathrm{V/m} = 7{,}70\times10^{-5}\,\mathrm{V/m}.
$$
:::

::: exercise VP29.11.2
Một vòng dây tròn bán kính $0{,}360\,\mathrm{cm}$ nằm trong mặt phẳng $xz$. Từ trường đều hướng theo trục $y$ giảm với tốc độ $0{,}0150\,\mathrm{T/s}$. Tìm độ lớn điện trường cảm ứng trên vòng dây.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $r=0{,}00360\,\mathrm m$, từ trường đều vuông góc mặt vòng, $|dB/dt|=0{,}0150\,\mathrm{T/s}$.

**Hướng đi:**

- Dùng từ thông $\Phi_B=B\pi r^2$ vì toàn bộ diện tích vòng nằm trong từ trường đều.
- Áp dụng Faraday trên đường tròn cố định. Đối xứng cho tích phân đường có độ lớn $2\pi rE$.

$$
\begin{aligned}
&2\pi rE = \pi r^2\left|\frac{dB}{dt}\right|,\\
&E = \frac r2\left|\frac{dB}{dt}\right| = 2{,}70\times10^{-5}\,\mathrm{V/m}.
\end{aligned}
$$
:::

::: exercise VP29.11.3
Một ống dây dài có tiết diện $4{,}00\,\mathrm{cm^2}$ và 965 vòng trên một mét, trục dọc theo $z$. Từ trường trong ống hướng theo $+z$. Một vòng dây bán kính $5{,}00\,\mathrm{cm}$ bao quanh ống, có tâm trên trục và nằm trong mặt phẳng $xy$. Tìm tốc độ biến thiên dòng điện trong ống nếu điện trường tại điểm $x=5{,}00\,\mathrm{cm}$, $y=z=0$ là

(a)

$$
\vec E=(1{,}20\times10^{-5}\,\mathrm{V/m})\hat{\jmath}.
$$

(b)

$$
\vec E=-(1{,}80\times10^{-5}\,\mathrm{V/m})\hat{\jmath}.
$$
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $n=965\,\mathrm{m^{-1}}$, $A_s=4{,}00\times10^{-4}\,\mathrm{m^2}$, $r=0{,}0500\,\mathrm m$. Cần tìm $dI/dt$ có dấu từ hướng và độ lớn điện trường tiếp tuyến.

**Hướng đi:**

- Chọn chiều đường tích phân ngược chiều kim đồng hồ khi nhìn từ $+z$. Tại điểm trên trục $+x$, chiều tiếp tuyến dương là $+y$.
- Dùng Faraday với từ thông $\Phi_B=\mu_0nIA_s$. Giữ dấu của thành phần $E_y$ để phân biệt dòng tăng và giảm.

Với quy ước trên,

$$
\begin{aligned}
&2\pi rE_y = -\mu_0nA_s\frac{dI}{dt},\\
&\frac{dI}{dt} = -\frac{2\pi rE_y}{\mu_0nA_s}.\end{aligned}
$$

(a) Khi $E_y>0$,

$$
\frac{dI}{dt}=-7{,}77\,\mathrm{A/s}.
$$

Dòng trong ống giảm. Điện trường cảm ứng có chiều tạo dòng chống lại sự giảm của từ trường theo $+z$.

(b) Khi $E_y<0$,

$$
\frac{dI}{dt}=11{,}7\,\mathrm{A/s}.
$$

Dòng trong ống tăng. Chiều điện trường cảm ứng đảo lại để chống sự tăng từ thông.
:::

::: exercise VP29.11.4
Một ống dây dài có 585 vòng trên một mét và tiết diện $2{,}70\,\mathrm{cm^2}$. Dòng điện trong ống phụ thuộc thời gian theo

$$
I(t)=(0{,}600\,\mathrm{A/s^2})t^2.
$$

Một vòng dây điện trở $0{,}600\,\Omega$ bao quanh ống, song song các vòng của ống và có tâm trên trục. Tìm dòng cảm ứng trong vòng tại $t=13{,}9\,\mathrm s$.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $n=585\,\mathrm{m^{-1}}$, $A_s=2{,}70\times10^{-4}\,\mathrm{m^2}$, $R=0{,}600\,\Omega$, dòng trong ống tăng theo bình phương thời gian.

**Hướng đi:**

- Lấy đạo hàm $I(t)$ vì suất điện động phụ thuộc tốc độ biến thiên từ thông, không phụ thuộc riêng giá trị dòng.
- Dùng $|\mathcal E|=\mu_0nA_s|dI/dt|$, rồi chia cho điện trở vòng để tìm dòng cảm ứng.

$$
\begin{aligned}
&\frac{dI}{dt} = (1{,}20\,\mathrm{A/s^2})t,\\
&\left.\frac{dI}{dt}\right|_{13{,}9\,\mathrm s} = 16{,}68\,\mathrm{A/s}.\end{aligned}
$$

Do đó độ lớn dòng trong vòng bao quanh là

$$
I_{\mathrm{c}} = \frac{\mu_0nA_s}{R}\left|\frac{dI}{dt}\right| = 5{,}52\times10^{-6}\,\mathrm A.
$$

Chiều dòng cảm ứng tạo từ trường ngược chiều từ trường của ống, vì từ trường trong ống đang tăng.
:::

## Bài toán cầu nối: Vòng dây vuông rơi qua ranh giới từ trường

::: exercise Bài cầu nối 29
Một vòng dây đồng vuông được đặt thẳng đứng và thả rơi từ trạng thái nghỉ. Ban đầu vòng nằm trong từ trường đều, nằm ngang và vuông góc mặt vòng. Vòng rơi dần vào vùng không có từ trường như hình dưới.

Cạnh vòng dài $s$, dây có đường kính $d$. Điện trở suất và khối lượng riêng của đồng lần lượt là $\rho_R$ và $\rho_m$.

Nếu vòng đạt tốc độ giới hạn khi cạnh trên vẫn còn trong vùng từ trường, hãy tìm biểu thức tốc độ ấy.

![Hình 29.28: Vòng dây vuông rơi từ vùng có từ trường đều hướng vào mặt hình xuống vùng không có từ trường.](img/young-29/hinh-bridge29-28.png)

### Các bước định hướng

1. Chuyển động gây suất điện động và dòng cảm ứng. Lực từ lên dòng chống lại trọng lực. Tại tốc độ giới hạn, lực từ hướng lên cân bằng trọng lực hướng xuống.
2. Xét khi toàn bộ vòng còn nằm trong từ trường. Có suất điện động cảm ứng không? Nếu có, suất điện động hướng theo chiều nào?
3. Xét khi chỉ cạnh trên còn ở trong từ trường. Có suất điện động cảm ứng không? Nếu có, suất điện động hướng theo chiều nào?
4. Khi có dòng cảm ứng, lực từ trên từng cạnh có hướng nào? Lực tổng lên vòng có hướng nào?
5. Khi vòng rơi với tốc độ $v$, hãy tính suất điện động, dòng điện và lực từ theo điện trở toàn vòng $R$.
6. Biểu diễn $R$ và khối lượng vòng bằng những đại lượng đã cho.
7. Dùng các kết quả trên để tìm tốc độ giới hạn.
8. Tốc độ giới hạn phụ thuộc độ lớn $B$ thế nào? Giải thích sự phụ thuộc ấy.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vòng vuông cạnh $s$ làm từ dây tròn đường kính $d$, có điện trở suất $\rho_R$ và khối lượng riêng $\rho_m$. Từ trường vuông góc mặt vòng. Tìm tốc độ giới hạn trong giai đoạn cạnh trên còn ở trong từ trường, còn cạnh dưới đã ra ngoài.

**Hướng đi:**

- Phân biệt giai đoạn cả vòng nằm trong từ trường với giai đoạn vòng đi qua ranh giới. Chỉ giai đoạn thứ hai có từ thông giảm và dòng cảm ứng.
- Dùng Faraday và định luật Ohm để biểu diễn dòng theo tốc độ rơi.
- Dùng lực từ trên cạnh trên. Hai lực ngang ở phần hai cạnh bên còn trong trường triệt tiêu, còn cạnh dưới ở ngoài trường không chịu lực từ.
- Dùng điện trở dây $R=\rho_R\ell/A_w$ và khối lượng $m=\rho_m\ell A_w$, với chiều dài dây $\ell=4s$.
- Áp dụng cân bằng lực $F_B=mg$ tại tốc độ giới hạn.

Khi cả vòng ở trong từ trường đều, từ thông không đổi. Suất điện động tổng quanh vòng bằng không, dù trên từng đoạn có thể xảy ra phân bố lại điện tích do lực từ.

Khi cạnh dưới đi ra ngoài, diện tích phần vòng nằm trong trường giảm. Với từ trường hướng vào mặt hình, dòng cảm ứng chạy theo chiều kim đồng hồ để tạo từ trường cùng chiều, chống lại sự giảm từ thông. Dòng ở cạnh trên hướng sang phải. Lực từ trên cạnh ấy hướng lên.

Nếu $h$ là chiều cao phần vòng còn trong vùng trường thì $dh/dt=-v$. Độ lớn suất điện động và dòng điện là

$$
\begin{aligned}
&|\mathcal E| = \left|B s\frac{dh}{dt}\right| = Bsv,\\
&I = \frac{Bsv}{R}.
\end{aligned}
$$

Hai cạnh bên có cùng chiều dài nằm trong trường và chịu hai lực ngang ngược chiều, nên tổng hai lực bằng không. Lực từ tổng theo phương thẳng đứng bằng lực lên cạnh trên:

$$
F_B = IBs = \frac{B^2s^2v}{R}.
$$

Tiết diện dây, điện trở vòng và khối lượng vòng là

$$
\begin{aligned}
&A_w = \frac{\pi d^2}{4},\\
&R = \rho_R\frac{4s}{A_w} = \frac{16\rho_Rs}{\pi d^2},\\
&m = \rho_m(4s)A_w = \rho_m\pi d^2s.
\end{aligned}
$$

Tại tốc độ giới hạn,

$$
\begin{aligned}
&\frac{B^2s^2v_{\mathrm{gh}}}{R} = mg,\\
&v_{\mathrm{gh}} = \frac{mgR}{B^2s^2} = \frac{16\rho_m\rho_Rg}{B^2}.
\end{aligned}
$$

Các thừa số $s$ và $d$ triệt tiêu. Tăng $B$ làm tốc độ giới hạn giảm theo $1/B^2$, vì cùng một tốc độ thì từ trường mạnh hơn vừa tạo dòng lớn hơn vừa tác dụng lực lớn hơn lên dòng ấy. Biểu thức chỉ áp dụng nếu vòng đạt tốc độ giới hạn trước khi cạnh trên ra khỏi vùng từ trường.
:::
