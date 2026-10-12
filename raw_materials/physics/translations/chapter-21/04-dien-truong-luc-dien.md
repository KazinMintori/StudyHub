<!-- Source: Section21.4, printed690–694, PDF710–714. -->

## 21.4. Điện trường và lực điện

Khi hai hạt mang điện tương tác trong không gian trống, mỗi hạt nhận biết sự có mặt của hạt kia như thế nào? Khái niệm điện trường giúp mô tả tương tác này qua hai bước và diễn đạt lại định luật Coulomb theo cách rất hữu ích.

### Từ tương tác giữa hai vật đến điện trường

Xét hai vật dương A và B đẩy nhau. B có điện tích $q_0$, chịu lực $\vec F_0$ do A. Có thể xem đây là tác dụng từ xa, không cần hai vật tiếp xúc. Lực hấp dẫn cũng từng được nhìn theo cách đó. Nhưng một cách hình dung khác là A làm thay đổi những tính chất của không gian xung quanh, rồi B đáp ứng sự thay đổi tại vị trí nó đang ở và chịu lực.

Lấy B đi, gọi vị trí cũ của nó là P. A vẫn tạo **điện trường** ở P cũng như ở những điểm lân cận, dù P không có điện tích. Nếu đặt điện tích điểm $q_0$ vào P, trường tại đó tác dụng lực $\vec F_0$ lên nó. Điện trường là phần trung gian trong cách mô tả sự tương tác giữa A và $q_0$.

![Hình 21.15: Nguồn điện tích tạo trường rồi trường tác dụng lên điện tích thử](../img/young-21/hinh-21-15.png)

**Hình 21.15:** (a) A và B tác dụng hai lực đối nhau. (b) B được lấy đi, vị trí của nó được gọi là P. (c) A vẫn tạo trường $\vec E$ tại P, và điện tích thử đặt ở P chịu lực $\vec F_0$. Trường là lực trên một đơn vị điện tích thử.

$q_0$ cũng tạo điện trường và trường ấy tác dụng lực $-\vec F_0$ lên A. Với mỗi lực, một vật đóng vai trò nguồn và vật kia chịu lực. Một điện tích tạo trường quanh nó nhưng không tự chịu hợp lực do chính nó tạo ra. Cũng như một vật không tự nâng được mình lên trần bằng cách kéo thắt lưng, ta không thêm “lực của chính hạt lên chính hạt” vào sơ đồ lực.

Muốn khảo sát trường tại một điểm, đặt một vật mang điện nhỏ gọi là **điện tích thử** ở đó. Nếu nó chịu lực điện, điểm đó có điện trường do các nguồn khác tạo. Điện tích thử cần đủ nhỏ để không làm thay đổi đáng kể phân bố nguồn.

Điện trường là đại lượng vector vì lực điện là vector. Định nghĩa tại một điểm là:

$$
\begin{aligned}
\vec E&=\frac{\vec F_0}{q_0}.
\end{aligned}
\tag{21.3}
$$

Đơn vị SI của độ lớn điện trường là newton trên coulomb, $\mathrm{N/C}$. Nếu biết trường tại điểm đặt điện tích điểm, lực là:

$$
\begin{aligned}
\vec F_0&=q_0\vec E.
\end{aligned}
\tag{21.4}
$$

Nếu $q_0>0$, lực cùng chiều trường. Nếu $q_0<0$, lực ngược chiều trường.

![Hình 21.16: Lực trên điện tích dương và âm trong cùng một điện trường](../img/young-21/hinh-21-16.png)

**Hình 21.16:** Nguồn Q tạo cùng vector trường tại vị trí khảo sát. Điện tích thử dương chịu lực cùng chiều $\vec E$, điện tích thử âm chịu lực ngược chiều. Đổi dấu điện tích thử làm đổi chiều lực, không đổi chiều trường của Q.

### So sánh với trường hấp dẫn

Ta đã quen hệ thức lực hấp dẫn lên khối lượng thử $m_0$:

$$
\begin{aligned}
\vec F_g&=m_0\vec g.
\end{aligned}
\tag{21.5}
$$

Chia cho $m_0$ cho $\vec g=\vec F_g/m_0$, tức lực hấp dẫn trên một đơn vị khối lượng. Có thể xem $\vec g$ là trường hấp dẫn do Trái Đất tạo, rồi trường ấy gây lực lên khối lượng thử. Trường hấp dẫn không phụ thuộc khối lượng thử, tương tự điện trường của nguồn không phụ thuộc điện tích thử.

::: warning Phạm vi của hệ thức lực điện
$\vec F_0=q_0\vec E$ dùng trực tiếp cho điện tích điểm tại điểm có trường $\vec E$. Với vật có kích thước đáng kể, trường có thể khác nhau về độ lớn và hướng trên từng phần của vật. Khi đó cần cộng lực của các phần, không lấy một vector trường tùy ý nhân toàn bộ điện tích.
:::

### Điện trường của một điện tích điểm

Gọi S là điểm đặt điện tích nguồn $q$, còn P là điểm cần tính trường. Vector $\vec r$ đi từ S đến P. Khoảng cách $r=|\vec r|$ và vector đơn vị $\hat{\mathbf r}=\vec r/r$ cũng luôn hướng từ nguồn đến điểm khảo sát.

Độ lớn lực lên điện tích thử tại P là $F_0=k|qq_0|/r^2$. Chia cho độ lớn điện tích thử cho:

$$
\begin{aligned}
E&=k\frac{|q|}{r^2}.
\end{aligned}
\tag{21.6}
$$

Biểu thức vector giữ cả dấu nguồn:

$$
\begin{aligned}
\vec E&=k\frac{q}{r^2}\hat{\mathbf r}.
\end{aligned}
\tag{21.7}
$$

Trường hướng ra xa nguồn dương, cùng chiều $\hat{\mathbf r}$, và hướng về nguồn âm, ngược chiều $\hat{\mathbf r}$.

![Hình 21.17: Điểm nguồn S, điểm khảo sát P và hướng điện trường](../img/young-21/hinh-21-17.png)

**Hình 21.17:** (a) $\hat{\mathbf r}$ luôn đi từ S đến P. (b) Nếu $q>0$, $\vec E$ cùng chiều $\hat{\mathbf r}$. (c) Nếu $q<0$, $\vec E$ ngược chiều $\hat{\mathbf r}$. Nguồn q tạo trường, còn trường tác dụng lên $q_0$ đặt ở P.

Trường tại P tồn tại dù có hay không điện tích thứ hai để chịu tác dụng. Nó phụ thuộc điện tích nguồn ở S và vị trí P.

![Hình 21.18: Các vector trường quanh một điện tích điểm dương hoặc âm](../img/young-21/hinh-21-18.png)

**Hình 21.18:** Trường dương tỏa ra, trường âm hướng vào. Độ lớn giảm khi khoảng cách đến nguồn tăng.

Điện trường không chỉ là một vector duy nhất mà là một vector gắn với mỗi điểm trong không gian, tức một **trường vector**. Trong hệ trục vuông góc, các thành phần được viết $E_x(x,y,z)$, $E_y(x,y,z)$ và $E_z(x,y,z)$. Trường vận tốc gió là một ví dụ tương tự: Độ lớn và hướng có thể thay đổi từ điểm này sang điểm khác trong khí quyển.

Nếu mọi vector trường trong một vùng có cùng độ lớn và hướng, ta gọi đó là **điện trường đều**. Một trường hợp quan trọng là vùng vật liệu của vật dẫn ở cân bằng tĩnh điện. Nếu bên trong có trường khác không, electron tự do chịu lực và có chuyển động tổng. Nhưng tĩnh điện đòi hỏi không có chuyển động tổng như vậy, nên trường bên trong vật liệu dẫn phải bằng không. Kết luận này không tự nói trường trong một lỗ rỗng nằm trong vật dẫn cũng bằng không.

### Ứng dụng sinh học: Khả năng cảm nhận điện của cá mập

Cá mập có thể tìm cá ẩn dưới cát đáy biển nhờ cảm nhận trường rất yếu do sự co cơ của con mồi. Những ống chứa chất dạng gel trong cơ thể cá mập kết thúc ở các lỗ trên da. Trường cỡ $5\times10^{-7}\,\mathrm{N/C}$ gây dòng điện tích trong ống và kích hoạt tín hiệu thần kinh. Các ống hướng khác nhau cho phép cảm nhận những thành phần khác nhau của vector trường, từ đó xác định hướng.

![Các lỗ cảm nhận điện trên da cá mập](../img/young-21/ung-dung-ca-map.png)

### Hai bước của bài toán điện trường

Trước hết, tính trường do phân bố nguồn. Tiếp theo, xét lực và chuyển động của điện tích đặt trong trường ấy. Bước thứ hai thường kết hợp tương tác điện với định luật Newton. Ba ví dụ sau minh họa cả việc tính trường và việc dùng trường đã biết để tìm chuyển động.

### Ví dụ 21.5: Độ lớn trường của điện tích điểm

Tìm độ lớn trường tại điểm cách điện tích $q=4.0\,\mathrm{nC}$ một khoảng $2.0\,\mathrm m$.

::: solution Lời giải
**Xác định và thiết lập.** Đã biết điện tích nguồn và khoảng cách, dùng (21.6).

$$
\begin{aligned}
E&=9.0\times10^9\frac{4.0\times10^{-9}}{(2.0)^2}\,\mathrm{N/C}\\
&=9.0\,\mathrm{N/C}.
\end{aligned}
$$

**Đánh giá.** Nếu đặt điện tích $1.0\,\mathrm C$ tại điểm đó mà giữ phân bố nguồn, nó chịu lực $9.0\,\mathrm N$. Với $2.0\,\mathrm C$, lực là $18\,\mathrm N$. Trường của nguồn không đổi, còn lực tỷ lệ với điện tích thử.
:::

### Ví dụ 21.6: Vector trường của điện tích điểm

Nguồn $q=-8.0\,\mathrm{nC}$ đặt tại gốc. Tìm vector điện trường tại $x=1.2\,\mathrm m$, $y=-1.6\,\mathrm m$.

![Hình 21.19: Vector từ nguồn âm tại gốc đến điểm khảo sát](../img/young-21/hinh-21-19.png)

::: solution Lời giải
**Xác định và thiết lập.** Tìm khoảng cách và vector đơn vị từ nguồn đến điểm P trước khi thay vào (21.7).

$$
\begin{aligned}
r&=\sqrt{(1.2)^2+(-1.6)^2}\,\mathrm m\\
&=2.0\,\mathrm m,\\
\hat{\mathbf r}&=\frac{(1.2\,\mathrm m)\hat{\mathbf i}+(-1.6\,\mathrm m)\hat{\mathbf j}}{2.0\,\mathrm m}\\
&=0.60\hat{\mathbf i}-0.80\hat{\mathbf j}.
\end{aligned}
$$

**Thực hiện.** Hệ số có dấu là:

$$
\begin{aligned}
\frac{kq}{r^2}&=9.0\times10^9\frac{-8.0\times10^{-9}}{(2.0)^2}\,\mathrm{N/C}\\
&=-18\,\mathrm{N/C}.
\end{aligned}
$$

Nhân với vector đơn vị:

$$
\begin{aligned}
\vec E&=(-18\,\mathrm{N/C})(0.60\hat{\mathbf i}-0.80\hat{\mathbf j})\\
&\approx(-11\,\mathrm{N/C})\hat{\mathbf i}\\
&\quad+(14\,\mathrm{N/C})\hat{\mathbf j}.
\end{aligned}
$$

**Đánh giá.** Nguồn âm nên trường hướng từ P về nguồn, ngược $\hat{\mathbf r}$. Bạn có thể tính tiếp độ lớn và góc hướng từ hai thành phần. Khi xác định $\hat{\mathbf r}$, luôn lấy từ nguồn đến điểm trường, rồi để dấu q quyết định có đảo chiều hay không.
:::

### Ví dụ 21.7: Electron trong điện trường đều

Hai bản dẫn song song cách $1.0\,\mathrm{cm}$ nối với pin $100\,\mathrm V$. Điện trường giữa chúng gần đều, hướng lên với $E=1.00\times10^4\,\mathrm{N/C}$. Một electron có điện tích $-e=-1.60\times10^{-19}\,\mathrm C$ và khối lượng $m=9.11\times10^{-31}\,\mathrm{kg}$ được thả từ nghỉ tại bản trên.

(a) Gia tốc bằng bao nhiêu? (b) Tốc độ và động năng khi đi $1.0\,\mathrm{cm}$ đến bản dưới bằng bao nhiêu? (c) Thời gian đi quãng đó là bao lâu?

![Hình 21.20: Điện trường đều hướng lên giữa hai bản dẫn và lực lên electron hướng xuống](../img/young-21/hinh-21-20.png)

**Hình 21.20:** Bản dưới dương, bản trên âm. Mũi tên mảnh chỉ điện trường. Trục y hướng lên, gốc tại bản trên. Khoảng cách trong hình được phóng lớn so với kích thước hai bản để nhìn rõ.

::: solution Lời giải
**Xác định và thiết lập.** Dùng lực điện, định luật II Newton, động năng và phương trình động học gia tốc không đổi. Vì electron mang điện âm, lực hướng xuống, ngược trường. Ban đầu $y_0=0$, $v_{0y}=0$.

**Thực hiện (a).**

$$
\begin{aligned}
a_y&=F_y/m=-eE/m\\
&=-\frac{(1.60)(1.00)}{9.11}\\
&\quad\times10^{16}\,\mathrm{m/s^2}\\
&=-1.76\times10^{15}\,\mathrm{m/s^2}.
\end{aligned}
$$

(b) Electron chỉ đi theo y. Ở $y=-1.0\times10^{-2}\,\mathrm m$:

$$
\begin{aligned}
|v_y|&=\sqrt{2a_yy}\\
&=\sqrt{2(-1.76)(-1.0)10^{13}}\,\mathrm{m/s}\\
&=5.9\times10^6\,\mathrm{m/s}.
\end{aligned}
$$

Vận tốc hướng xuống nên $v_y=-5.9\times10^6\,\mathrm{m/s}$. Động năng:

$$
\begin{aligned}
K&=\frac12mv^2\\
&=\frac12(9.11)(5.9)^2\\
&\quad\times10^{-19}\,\mathrm J\\
&\approx1.6\times10^{-17}\,\mathrm J.
\end{aligned}
$$

(c)

$$
\begin{aligned}
t&=\frac{v_y-v_{0y}}{a_y}\\
&=\frac{-5.9\times10^6}{-1.76\times10^{15}}\,\mathrm s\\
&=3.4\times10^{-9}\,\mathrm s.
\end{aligned}
$$

**Đánh giá.** Gia tốc, tốc độ, động năng và thời gian của hạt dưới nguyên tử có thang giá trị rất khác những vật thông thường như bóng chày hay ô tô. Dấu điện tích quyết định lực cùng hay ngược chiều trường.
:::

::: exercise Câu hỏi ôn lại mục 21.4
(a) Một điện tích điểm âm đi thẳng về phía một điện tích điểm dương cố định. Yếu tố nào của lực điện lên điện tích âm giữ nguyên: (i) Độ lớn, (ii) hướng, (iii) cả hai, hay (iv) không yếu tố nào?

(b) Nếu điện tích âm chuyển động trên đường tròn quanh điện tích dương, yếu tố nào giữ nguyên theo bốn lựa chọn trên?
:::

::: solution Giải thích
(a) Chọn (ii). Lực luôn hướng về nguồn dương trên cùng đường thẳng, nhưng tăng độ lớn khi khoảng cách giảm.

(b) Chọn (i). Khoảng cách không đổi nên độ lớn lực không đổi, còn hướng liên tục thay đổi để luôn chỉ về nguồn dương.
:::
