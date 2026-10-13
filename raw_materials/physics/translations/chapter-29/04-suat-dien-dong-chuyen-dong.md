## 29.4. Suất điện động chuyển động

Một thanh dẫn có thể tạo suất điện động khi chuyển động trong từ trường, dù không có pin nối vào nó. Ta có thể hiểu nguồn suất điện động bằng cách xét lực từ tác dụng lên các điện tích linh động bên trong thanh.

### Điện tích tách ra ở hai đầu thanh

Xét thanh dẫn dài $L$ chuyển động sang phải với tốc độ không đổi $v$ trong từ trường đều $\vec B$ hướng vào trang. Vận tốc, thanh và từ trường đôi một vuông góc. Một điện tích dương $q$ trong thanh chịu lực từ hướng dọc thanh từ đầu $b$ lên đầu $a$, có độ lớn $qvB$. Vì vậy, điện tích dương dồn lên đầu $a$, còn điện tích âm dồn lên đầu $b$.

![Hình 29.15: Lực từ tách điện tích trong thanh dẫn chuyển động và tạo dòng khi mạch kín.](../img/young-29/hinh-29-15.png)
Sự phân bố điện tích tạo ra điện trường $\vec E$ bên trong thanh, hướng từ $a$ về $b$. Điện tích tiếp tục tách ra cho đến khi lực điện hướng xuống cân bằng lực từ hướng lên:

$$
\begin{aligned}
qE&=qvB,\\
E&=vB.
\end{aligned}
$$

Độ chênh điện thế giữa hai đầu thanh bằng độ lớn điện trường nhân với chiều dài thanh. Do đó:

$$
\begin{aligned}
V_{ab}&=V_a-V_b\\
&=EL\\
&=vBL.
\end{aligned}
\tag{29.5}
$$

Đầu $a$ có điện thế cao hơn đầu $b$. Hiệu điện thế này tồn tại ngay cả khi thanh chưa nối thành mạch kín. Thanh chuyển động riêng lẻ đã có suất điện động, giống như một pin vẫn có suất điện động khi hai cực chưa nối với mạch ngoài.

### Thanh trượt trong mạch kín

Khi thanh trượt trên hai thanh ray đứng yên để tạo mạch kín, lực từ trực tiếp chỉ tác dụng lên điện tích trong thanh chuyển động. Điện tích ở hai đầu thanh tái phân bố dọc theo mạch đứng yên và tạo điện trường trong phần mạch ấy. Dòng điện chạy từ thế thấp lên thế cao trong thanh, tức từ $b$ lên $a$, rồi từ $a$ về $b$ qua mạch ngoài.

Suất điện động chuyển động trong cấu hình vuông góc nói trên có độ lớn:

$$
\mathcal E=vBL.
\tag{29.6}
$$

Nếu điện trở toàn mạch là $R$, định luật Ohm cho $I=\mathcal E/R=vBL/R$. Suất điện động này có bản chất là công trên một đơn vị điện tích của lực phi tĩnh bên trong thanh. Khi mạch ngoài được nối, dòng chạy trong thanh theo chiều từ $b$ lên $a$ và trong phần mạch còn lại theo chiều ngược lại.

Có thể tìm chiều cảm ứng bằng định luật Lenz ngay cả khi thanh chưa tạo mạch kín. Hãy tưởng tượng nối hai đầu thanh để hoàn thành mạch, tìm chiều dòng sẽ xuất hiện, rồi suy ra đầu nào là cực dương. Trong thanh, chiều từ cực âm sang cực dương là chiều của suất điện động.

### Suất điện động chuyển động trong trường hợp tổng quát

Xét vật dẫn có hình dạng bất kỳ chuyển động trong từ trường có thể không đều. Trong phần này, từ trường tại mỗi điểm được giả thiết không biến đổi theo thời gian. Mỗi phần tử dây $d\vec\ell$ đóng góp một suất điện động bằng thành phần lực từ trên một đơn vị điện tích dọc theo phần tử ấy.

Với vector vận tốc $\vec v$ của phần tử và từ trường tại chính vị trí đó:

$$
d\mathcal E=(\vec v\times\vec B)\cdot d\vec\ell.
$$

Cộng các đóng góp quanh đường dẫn kín ta được:

$$
\mathcal E=\oint (\vec v\times\vec B)\cdot d\vec\ell.
\tag{29.7}
$$

Trong điều kiện từ trường không đổi theo thời gian, tốc độ biến thiên từ thông qua vòng chuyển động bằng số đối của tích phân ở (29.7). Vì vậy biểu thức này tương đương với định luật Faraday, dù hình thức hai công thức khác nhau.

Nếu dây đứng yên trong từ trường biến thiên, mọi phần tử có $\vec v=0$ và (29.7) không mô tả được suất điện động cảm ứng. Khi đó phải dùng định luật Faraday với đạo hàm từ thông. Không thể coi biểu thức suất điện động do chuyển động là công thức thay thế cho mọi hiện tượng cảm ứng.

![Hình 29.16: Suất điện động toàn vòng bằng tích phân đóng góp của các phần tử dây.](../img/young-29/hinh-29-16.png)
Biểu thức tích phân này tương đương định luật Faraday đối với vòng dẫn đang chuyển động. Khi từ trường tại mỗi điểm không đổi theo thời gian, tốc độ thay đổi từ thông qua vòng bằng số đối của tích phân trong công thức (29.7). Nếu vật dẫn đứng yên nhưng từ trường thay đổi theo thời gian, không thể chỉ dùng biểu thức suất điện động chuyển động này. Khi ấy phải dùng định luật Faraday dạng $\mathcal E=-d\Phi_B/dt$.

### Ví dụ 29.9. Suất điện động chuyển động trong máy phát thanh trượt

Thanh trượt trong Hình 29.15 dài $0{,}10\,\mathrm m$, chuyển động với tốc độ $2{,}5\,\mathrm{m/s}$ trong từ trường đều $0{,}60\,\mathrm T$. Điện trở toàn mạch là $0{,}030\,\Omega$. Hãy tìm suất điện động, dòng điện và lực từ tác dụng lên thanh.

**Hướng đi hợp lý:** Dùng công thức (29.6) để tìm suất điện động. Sau đó dùng định luật Ohm để tìm dòng. Chiều dòng trong thanh đã được xác định từ phân cực ở hai đầu. Dùng lực từ lên đoạn dây mang dòng để tìm lực và kiểm tra chiều bằng định luật Lenz.

$$
\begin{aligned}
\mathcal E&=vBL\\
&=(2{,}5)(0{,}60)(0{,}10)\\
&=0{,}15\,\mathrm V.
\end{aligned}
$$

Dòng điện có độ lớn:

$$
\begin{aligned}
I&=\frac{\mathcal E}{R}\\
&=\frac{0{,}15}{0{,}030}\\
&=5{,}0\,\mathrm A.
\end{aligned}
$$

Chiều dòng trong thanh từ $b$ lên $a$. Theo $\vec F=I\vec L\times\vec B$, lực từ hướng sang trái, ngược chiều chuyển động. Vì $\vec L$ vuông góc với $\vec B$, độ lớn lực là:

$$
\begin{aligned}
F&=ILB\\
&=(5{,}0)(0{,}10)(0{,}60)\\
&=0{,}30\,\mathrm N.
\end{aligned}
$$

Lực cản từ phù hợp với định luật Lenz: Nó chống lại sự tăng diện tích và từ thông gây ra dòng cảm ứng.

### Ví dụ 29.10. Đĩa Faraday

Một đĩa dẫn điện bán kính $R$ nằm trong mặt phẳng $xy$ và quay đều với vector vận tốc góc theo chiều $+z$, có độ lớn $\omega$. Từ trường đều, không đổi và hướng theo $+z$. Hãy tìm suất điện động giữa tâm đĩa và vành ngoài.

![Hình 29.17: Đĩa dẫn quay trong từ trường tạo suất điện động giữa tâm và vành.](../img/young-29/hinh-29-17.png)
**Hướng đi hợp lý:** Mỗi điểm trên đĩa chuyển động với tốc độ phụ thuộc khoảng cách $r$ đến trục. Chia đường bán kính từ tâm đến vành thành các đoạn nhỏ $dr$. Tính suất điện động trên từng đoạn rồi tích phân.

Tại bán kính $r$, tốc độ tiếp tuyến là $v=\omega r$. Véc-tơ $\vec v$ vuông góc với $\vec B$, nên lực từ trên một đơn vị điện tích có độ lớn $vB=\omega rB$ và hướng xuyên tâm. Chọn phần tử $d\vec\ell$ hướng từ tâm ra vành, khi đó:

$$
\begin{aligned}
d\mathcal E&=(\vec v\times\vec B)\cdot d\vec\ell\\
&=\omega Br\,dr.
\end{aligned}
$$

Cộng các đoạn từ $r=0$ đến $r=R$:

$$
\begin{aligned}
\mathcal E&=\int_0^R\omega Br\,dr\\
&=\frac{1}{2}\omega BR^2.
\end{aligned}
$$

Có thể khép kín mạch bằng hai chổi tiếp xúc cố định trên đĩa và trục dẫn điện. Thiết bị này gọi là đĩa Faraday hay máy phát đồng cực. Nó tạo suất điện động không đổi theo thời gian và dòng một chiều. Dấu của suất điện động giữa tâm và vành phụ thuộc chiều quay và hướng từ trường.

### Tự kiểm tra Mục 29.4

Từ trường Trái Đất gần xích đạo được xem là nằm ngang, hướng về phía bắc. Cầm một thanh kim loại và đi về phía đông. (a) Cần đặt thanh theo hướng đông–tây, bắc–nam hay thẳng đứng để suất điện động giữa hai đầu lớn nhất? (b) Hướng nào cho suất điện động bằng không? (c) Cần đi theo hướng nào để suất điện động bằng không với mọi cách đặt thanh: Hướng tây, bắc, nam, thẳng lên hay thẳng xuống?

<details>
<summary>Đáp án</summary>

(a) Đặt thanh thẳng đứng. Khi ấy véc-tơ chiều dài thanh song song với $\vec v\times\vec B$, nên suất điện động lớn nhất. (b) Cả hai hướng nằm ngang, đông–tây hoặc bắc–nam, đều cho suất điện động bằng không vì véc-tơ thanh vuông góc với $\vec v\times\vec B$. (c) Đi về phía bắc hoặc phía nam. Khi đó $\vec v$ song song hoặc ngược chiều $\vec B$, nên $\vec v\times\vec B=0$ bất kể thanh đặt theo hướng nào.

</details>
