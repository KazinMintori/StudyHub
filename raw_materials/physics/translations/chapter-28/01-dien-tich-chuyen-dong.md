## 28.1 Từ trường của điện tích chuyển động

Một điện tích điểm $q$ chuyển động đều với vận tốc $\vec v$ tạo ra từ trường. Trong các ứng dụng, một dòng điện gồm rất nhiều điện tích chuyển động cùng nhau. Ta bắt đầu với một điện tích để thấy rõ từ trường phụ thuộc vào điện tích, vận tốc và vị trí đo như thế nào.

Gọi **điểm nguồn** là vị trí tức thời của điện tích. Gọi **điểm trường** $P$ là vị trí cần tìm từ trường. Véc-tơ $\vec r$ hướng từ điểm nguồn đến $P$, độ dài của nó là $r$, còn $\hat r=\vec r/r$ là véc-tơ đơn vị theo hướng đó. Ký hiệu $\phi$ là góc giữa vận tốc $\vec v$ và $\vec r$.

![Véc-tơ từ trường và đường sức quanh điện tích dương chuyển động đều](../img/young-28/hinh-28-01.png)

Hình 28.1: Từ trường vuông góc với mặt phẳng chứa vận tốc và hướng từ điện tích đến điểm đo. Độ lớn phụ thuộc vào góc $\phi$.

Thực nghiệm cho thấy độ lớn từ trường tỉ lệ với độ lớn điện tích $|q|$, tốc độ $v$, $\sin\phi$ và nghịch đảo bình phương khoảng cách $r$. Vì vậy, từ trường bằng không trên đường thẳng song song với vận tốc, nơi $\sin\phi=0$. Ở cùng khoảng cách, từ trường lớn nhất trên mặt phẳng vuông góc với vận tốc, nơi $\sin\phi=1$.

$$
B = \frac{\mu_0}{4\pi} \times\frac{|q|v\sin\phi}{r^2}. \tag{28.1}
$$

Hằng số $\mu_0$ được gọi là **hằng số từ** và đọc là “mu không”. Thừa số $4\pi$ trong mẫu được chọn phù hợp với cách viết định luật Coulomb và sẽ xuất hiện tự nhiên khi xét các nguồn có đối xứng.

Độ lớn của công thức trên chưa cho biết chiều của $\vec B$. Tích có hướng gói cả độ lớn lẫn hướng vào một biểu thức. Véc-tơ $\vec v\times\hat r$ vuông góc với mặt phẳng chứa $\vec v$ và $\vec r$. Nếu $q$ dương, chiều được xác định bằng quy tắc bàn tay phải. Nếu $q$ âm, dấu của $q$ đảo chiều từ trường.

$$
\vec B = \frac{\mu_0 q}{4\pi r^2} \left(\vec v \times \hat r\right). \tag{28.2}
$$

Các đường sức từ của điện tích dương chuyển động là những đường tròn có trục song song với $\vec v$. Chúng nằm trong các mặt phẳng vuông góc với vận tốc. Để xác định chiều, đặt ngón cái bàn tay phải theo $\vec v$. Các ngón tay khum lại theo chiều đường sức từ. Với điện tích âm, chiều của cả $\vec B$ lẫn đường sức đảo ngược.

Điện tích điểm ở đây chuyển động với vận tốc không đổi. Khi điện tích gia tốc, từ trường có cấu trúc phức tạp hơn. Trong dây dẫn, hạt tải có thể gia tốc tại chỗ dây uốn cong vì hướng chuyển động đổi chiều. Tuy nhiên, tốc độ trôi $v_d$ trong kim loại rất nhỏ. Gia tốc hướng tâm $v_d^2/r$ vì thế đủ nhỏ để bỏ qua trong các bài toán của chương này.

Đơn vị SI của từ trường là tesla, ký hiệu $\mathrm T$:

$$
\begin{aligned}
1\,\mathrm T &= 1\,\frac{\mathrm{N\,s}}{\mathrm{C\,m}} \\
&= 1\,\frac{\mathrm N}{\mathrm{A\,m}}.
\end{aligned} \tag{28.3}
$$

Từ các đơn vị này, đơn vị của $\mu_0$ có thể viết theo nhiều cách tương đương. Giá trị số của hằng số trong SI là:

$$
\begin{aligned}
\mu_0 &\approx 1{,}25663706\times10^{-6} \times\frac{\mathrm{N\,s^2}}{\mathrm{C^2}} \\
&= 1{,}25663706\times10^{-6} \times\frac{\mathrm{Wb}}{\mathrm{A\,m}} \\
&\approx 4\pi\times10^{-7} \times\frac{\mathrm{T\,m}}{\mathrm A}.
\end{aligned}
$$

Hằng số điện $\varepsilon_0$ và hằng số từ liên hệ với tốc độ ánh sáng trong chân không:

$$
\begin{aligned}
c &= \frac{1}{\sqrt{\varepsilon_0\mu_0}} \\
&= 2{,}998\times10^8\,\mathrm{m/s}.
\end{aligned} \tag{28.4}
$$

Sự liên hệ này cho thấy điện trường và từ trường có quan hệ sâu sắc trong bản chất của ánh sáng. Ta sẽ trở lại chủ đề ấy khi học sóng điện từ.

::: example Ví dụ 28.1 Lực giữa hai proton chuyển động ngược chiều
Hai proton chuyển động song song với trục $x$, ngược chiều nhau và cùng tốc độ $v$, với $v$ nhỏ so với tốc độ ánh sáng $c$. Tại thời điểm xét, proton dưới chuyển động theo $+x$, còn proton trên chuyển động theo $-x$. Khoảng cách giữa chúng là $r$. Hãy tìm lực điện, lực từ tác dụng lên proton trên và so sánh độ lớn.

![Hai proton chuyển động ngược chiều, cùng chịu lực điện và lực từ](../img/young-28/hinh-28-02.png)

Hình 28.2: Lực điện và lực từ giữa hai proton đang chuyển động.

Định luật Coulomb cho lực điện có độ lớn:

$$
F_E = \frac{1}{4\pi\varepsilon_0} \times\frac{q^2}{r^2}.
$$

Hai proton cùng dấu nên đẩy nhau. Lực điện lên proton trên hướng theo $+y$.

Proton dưới có $\vec v=v\hat{\imath}$, còn $\hat r=\hat{\jmath}$ hướng từ proton dưới đến proton trên. Dùng phương trình (28.2), từ trường do proton dưới tạo ra tại vị trí proton trên là:

$$
\begin{aligned}
\vec B &= \frac{\mu_0 qv}{4\pi r^2} \left(\hat{\imath}\times\hat{\jmath}\right) \\
&= \frac{\mu_0 qv}{4\pi r^2}\,\hat{k}.
\end{aligned}
$$

Proton trên chuyển động với $-v\hat{\imath}$. Lực từ lên nó là:

$$
\begin{aligned}
\vec F_B &= q\left(-v\hat{\imath}\right)\times\vec B \\
&= \frac{\mu_0 q^2v^2}{4\pi r^2}\,\hat{\jmath}.
\end{aligned}
$$

Lực từ cũng hướng theo $+y$, nên tương tác từ trong tình huống này là lực đẩy. Tỉ số hai độ lớn là:

$$
\begin{aligned}
\frac{F_B}{F_E} &= \frac{\mu_0q^2v^2}{4\pi r^2} \times\frac{4\pi\varepsilon_0r^2}{q^2} \\
&= \varepsilon_0\mu_0v^2 \\
&= \frac{v^2}{c^2}.
\end{aligned}
$$

Vì $v\ll c$, lực từ nhỏ hơn nhiều so với lực điện, dù cả hai đều đẩy proton trên lên trên.
:::

### Hệ quy chiếu khi mô tả lực

Các vận tốc, điện trường và từ trường trong Ví dụ 28.1 được mô tả trong hệ quy chiếu đứng yên như hình. Trong một hệ quy chiếu chuyển động cùng proton dưới, proton ấy đứng yên nên không có lực từ tác dụng lên nó trong hệ đó. Đây không phải là mâu thuẫn. Điện trường và từ trường thay đổi khi chuyển hệ quy chiếu, còn lực tổng hợp vẫn nhất quán. Sự hòa giải đầy đủ thuộc thuyết tương đối đặc biệt.

### Tự kiểm tra 28.1
Hai proton chuyển động song song cùng chiều với cùng tốc độ $v$. (a) Lực từ giữa chúng hút hay đẩy? (b) Lực tổng giữa chúng hút, đẩy hay bằng không? Giả sử $v$ nhỏ hơn nhiều so với $c$.

::: details Đáp án
(a) Lực từ hút. Từ trường do proton phía sau tạo ra tại proton phía trước giống chiều trong hình, nhưng vận tốc proton phía trước cùng chiều proton phía sau, nên lực $q\vec v\times\vec B$ đổi chiều so với Ví dụ 28.1. (b) Lực điện vẫn đẩy và lớn hơn lực từ theo tỉ số $F_B/F_E=v^2/c^2\ll1$. Vì vậy lực tổng vẫn đẩy.
:::
