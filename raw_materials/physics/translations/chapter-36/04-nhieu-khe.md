## 36.4. Nhiễu xạ và giao thoa qua hệ nhiều khe

Trong các phần trước, ta đã khảo sát hai trường hợp giới hạn:
- Giao thoa của hai nguồn điểm (hoặc hai khe có bề rộng rất nhỏ), trong đó ta hoàn toàn bỏ qua ảnh hưởng của bề rộng khe.
- Nhiễu xạ của một khe đơn lẻ có bề rộng hữu hạn $a$.

Trong thực tế, mọi khe hẹp dùng trong thí nghiệm giao thoa đều có một bề rộng hữu hạn nhất định. Khi đó, sóng ánh sáng truyền qua mỗi khe vừa trải qua hiện tượng nhiễu xạ (do ánh sáng xuất phát từ các vị trí khác nhau trong cùng một khe), vừa trải qua hiện tượng giao thoa (do ánh sáng từ các khe khác nhau chồng chập lên nhau).

### Hai khe có bề rộng hữu hạn và hiện tượng bậc khuyết

![Hình 36.12: Xác định hệ vân cường độ cho hai khe có bề rộng hữu hạn a và khoảng cách d = 4a. (a) Đồ thị cường độ nhiễu xạ của một khe đơn có bề rộng a, với các cực tiểu tại md = ±1, ±2. (b) Đồ thị cường độ giao thoa của hai khe rất hẹp cách nhau d = 4a, với các cực đại tại mi = 0, ±1, ±2, ... (c) Đồ thị cường độ tổng hợp của hai khe có bề rộng hữu hạn: Các đỉnh giao thoa hai khe nằm bên trong “đường bao” nhiễu xạ một khe. Cứ mỗi cực đại giao thoa thứ tư ở hai bên lại bị triệt tiêu hoàn toàn (bậc khuyết). (d) Ảnh chụp hệ vân thực tế tương ứng với đồ thị (c).](../img/young-36/hinh-36-12.png)

Hình 36.12 minh họa cơ chế kết hợp giữa giao thoa và nhiễu xạ đối với hai khe:
- Hình 36.12a biểu diễn sự phân bố cường độ nhiễu xạ của một khe đơn có bề rộng $a$. Các vân tối nhiễu xạ xuất hiện tại các góc thỏa mãn $a\sin\theta = m_d \lambda$ với $m_d = \pm 1, \pm 2, \dots$ (chỉ số $d$ ký hiệu cho nhiễu xạ).
- Hình 36.12b biểu diễn hệ vân giao thoa thuần túy của hai khe rất hẹp cách nhau một khoảng $d = 4a$. Các đỉnh cực đại giao thoa xuất hiện tại các góc thỏa mãn $d\sin\theta = m_i \lambda$ với $m_i = 0, \pm 1, \pm 2, \dots$ (chỉ số $i$ ký hiệu cho giao thoa). Khoảng cách góc giữa hai cực tiểu nhiễu xạ lớn gấp 4 lần khoảng cách giữa hai cực đại giao thoa liền kề.
- Khi hai khe có bề rộng hữu hạn $a$ và cách nhau $d = 4a$ (Hình 36.12c), cường độ sáng tại mỗi điểm trên màn bằng tích của hàm giao thoa hai khe và hàm nhiễu xạ một khe:

$$
\begin{aligned}
I &= I_0 \cos^2\frac{\phi}{2} \\
&\quad \times \left[\frac{\sin(\beta/2)}{\beta/2}\right]^2
\end{aligned}
\tag{36.12}
$$

Trong đó:
- Đại lượng $\phi$ là độ lệch pha giữa hai sóng phát ra từ tâm của hai khe liền kề:

$$
\begin{aligned}
\phi &= \frac{2\pi}{\lambda} d \sin\theta
\end{aligned}
$$

- Đại lượng $\beta$ là tổng độ lệch pha giữa các sóng phát ra từ hai mép của cùng một khe:

$$
\begin{aligned}
\beta &= \frac{2\pi}{\lambda} a \sin\theta
\end{aligned}
$$

- Thừa số $\cos^2(\phi/2)$ tạo nên các vân giao thoa biến thiên nhanh với chu kỳ hẹp.
- Thừa số $[\frac{\sin(\beta/2)}{\beta/2}]^2$ đóng vai trò là một **đường bao nhiễu xạ** (diffraction envelope) biến thiên chậm hơn, điều biến biên độ của các đỉnh cực đại giao thoa.

**Hiện tượng bậc khuyết (Missing Orders)**:
Tại những góc $\theta$ mà một cực đại giao thoa trùng đúng vào vị trí của một cực tiểu nhiễu xạ, ánh sáng bị triệt tiêu hoàn toàn bởi thừa số nhiễu xạ. Khi đó, cực đại giao thoa tại bậc đó sẽ hoàn toàn biến mất khỏi màn quan sát.

Điều kiện đồng thời để có cực đại giao thoa và cực tiểu nhiễu xạ là:

$$
\begin{aligned}
d \sin\theta &= m_i \lambda \\
a \sin\theta &= m_d \lambda
\end{aligned}
$$

Lập tỷ số giữa hai phương trình, ta có:

$$
\begin{aligned}
\frac{d}{a} &= \frac{m_i}{m_d} \\
m_i &= \frac{d}{a} m_d
\end{aligned}
$$

Trong Hình 36.12c, với $d = 4a$, ta có $m_i = 4m_d$:
- Với $m_d = \pm 1$: Cực đại giao thoa bậc $m_i = \pm 4$ bị khuyết.
- Với $m_d = \pm 2$: Cực đại giao thoa bậc $m_i = \pm 8$ bị khuyết.

Như vậy, cứ mỗi cực đại thứ tư ở hai bên lại bị khuyết, hoàn toàn trùng khớp với bức ảnh chụp thực nghiệm ở Hình 36.12d.

Khe càng hẹp thì đường bao nhiễu xạ càng rộng, và cường độ của các vân giao thoa giảm đi càng chậm khi ra xa tâm.

### Hệ nhiều khe hẹp song song (Several Slits)

Xét một hệ gồm $N$ khe hẹp song song, mỗi khe cách khe liền kề một khoảng $d$ (Hình 36.13). Giả sử bề rộng mỗi khe rất nhỏ so với bước sóng ($a \ll \lambda$), nhờ đó sóng nhiễu xạ từ mỗi khe lan tỏa gần như đồng đều ra mọi hướng.

![Hình 36.13: Nhiễu xạ và giao thoa qua hệ tám khe hẹp song song. Khoảng cách giữa hai khe liền kề là d. Các tia sáng truyền theo góc θ tới thấu kính hội tụ để tạo ảnh trên màn quan sát ở tiêu diện. Cực đại giao thoa xuất hiện khi hiệu đường đi giữa hai khe liền kề d sin θ bằng một số nguyên lần bước sóng mλ.](../img/young-36/hinh-36-13.png)

**1. Vị trí các cực đại chính (Principal Maxima)**:
Các sóng truyền từ các khe liền kề tới điểm $P$ trên màn sẽ giao thoa tăng cường khi hiệu đường đi giữa hai khe liền kề bằng một số nguyên lần bước sóng:

$$
\begin{aligned}
d \sin\theta &= m \lambda
\end{aligned}
$$

Trong đó: Giá trị $m = 0, \pm 1, \pm 2, \dots$ là các số nguyên.

Điều này đồng nghĩa với việc độ lệch pha giữa hai khe liền kề $\phi = \frac{2\pi}{\lambda} d\sin\theta$ phải bằng một bội số nguyên của $2\pi$:

$$
\begin{aligned}
\phi &= 2m\pi
\end{aligned}
$$

Như vậy, **vị trí của các cực đại chính trong hệ $N$ khe hoàn toàn trùng với vị trí các cực đại của hệ hai khe có cùng khoảng cách $d$**.

![Hình 36.14: Giản đồ vectơ pha cho ánh sáng truyền qua hệ tám khe hẹp. (a) Khi độ lệch pha giữa các khe liền kề là ϕ = π (180°), các vectơ pha triệt tiêu nhau từng cặp, cường độ tổng hợp bằng không. (b) Khi ϕ = π/4 (45°), tám vectơ pha khép kín thành một hình bát giác đều, vectơ tổng bằng không. (c) Khi ϕ = π/2 (90°), tám vectơ pha tạo thành hai vòng vuông khép kín, vectơ tổng bằng không.](../img/young-36/hinh-36-14.png)

**2. Cơ chế hình thành cực đại hẹp và tích lũy độ lệch pha**:
Hình 36.15b biểu diễn kết quả tính toán chi tiết cho hệ gồm 8 khe. Các cực đại lớn, gọi là các **cực đại chính** (principal maxima), xuất hiện tại cùng các vị trí góc như hệ hai khe trên Hình 36.15a nhưng hẹp hơn rất nhiều. Cơ chế vật lý tạo nên độ hẹp sắc nét này là sự tích lũy độ lệch pha: Nếu độ lệch pha $\phi$ giữa hai khe liền kề hơi lệch một chút so với một bội số của $2\pi$, các sóng từ khe 1 và khe 2 chỉ hơi lệch pha một ít; tuy nhiên, độ lệch pha giữa khe 1 và khe 3 sẽ lớn hơn gấp đôi, giữa khe 1 và khe 4 sẽ còn lớn hơn nữa, và tiếp tục tích lũy tăng dần. Sự tích lũy độ lệch pha giữa các khe xa nhau dẫn đến sự triệt tiêu sóng một phần ngay cả ở những góc chỉ hơi lệch nhẹ so với góc của cực đại chính, tạo nên các đỉnh cực đại chính rất hẹp như trên Hình 36.15b. Khi số lượng khe tăng lên 16 khe (Hình 36.15c), các cực đại chính thậm chí còn hẹp hơn nữa.

**3. Sự xuất hiện của các cực tiểu giữa hai cực đại chính**:
Khác với hệ hai khe (chỉ có duy nhất một cực tiểu nằm giữa hai cực đại liền kề khi $\phi = \pi$), hệ nhiều khe có nhiều cực tiểu xen kẽ:
- Với hệ 8 khe:
  - Khi $\phi = \pi$: Các vectơ từ các khe liền kề ngược chiều nhau từng cặp và triệt tiêu nhau hoàn toàn (Hình 36.14a).
  - Khi $\phi = \pi/4$: Tám vectơ pha tạo thành một hình bát giác đều khép kín (Hình 36.14b), vectơ tổng bằng không.
  - Khi $\phi = \pi/2$: Tám vectơ pha khép thành hai vòng vuông liên tiếp (Hình 36.14c), vectơ tổng bằng không.

Câu hỏi: Hãy chứng minh rằng khi có $N$ khe hẹp, giữa mỗi cặp cực đại chính liền kề luôn có đúng $(N - 1)$ cực tiểu, và một cực tiểu xuất hiện bất cứ khi nào độ lệch pha $\phi$ giữa hai khe liền kề là một bội số nguyên của $2\pi/N$ (ngoại trừ các trường hợp $\phi$ là bội số nguyên của $2\pi$, vốn tạo thành cực đại chính)?

<details><summary>Xem chứng minh</summary>

Chứng minh:

Biên độ điện trường tổng hợp từ $N$ khe hẹp tại góc lệch $\theta$ được biểu diễn bằng tổng của $N$ vectơ pha có độ dài bằng nhau, trong đó mỗi vectơ pha lệch một góc $\phi = \frac{2\pi}{\lambda} d\sin\theta$ so với vectơ pha liền trước nó.

Cường độ sáng triệt tiêu (bằng không) khi và chỉ khi vectơ pha tổng hợp bằng không, tức là chuỗi $N$ vectơ pha khép kín lại thành một đa giác đều $N$ cạnh (hoặc lặp lại một số nguyên vòng đa giác khép kín).

Điều kiện để chuỗi $N$ vectơ pha khép kín là tổng góc quay sau $N$ vectơ phải bằng một bội số nguyên của $2\pi$:

$$
\begin{aligned}
N \phi &= p \times 2\pi \\
\phi &= p \frac{2\pi}{N}
\end{aligned}
$$

Trong đó: Giá trị $p$ là một số nguyên bất kỳ.

Tuy nhiên, nếu $p$ là một bội số nguyên của $N$ (tức là $p = kN$ với $k$ nguyên), thì $\phi = k \times 2\pi$. Khi đó, độ lệch pha giữa hai khe liền kề là một bội số của $2\pi$, toàn bộ $N$ vectơ pha đều cùng hướng dọc theo một đường thẳng, tạo thành đỉnh cực đại chính có cường độ cực đại $N^2 I_0$.

Do đó, các cực tiểu xuất hiện khi $p$ là số nguyên không chia hết cho $N$. Trong mỗi khoảng giữa hai cực đại chính liền kề (ứng với $p$ biến thiên từ $kN + 1$ đến $kN + N - 1$), có đúng $(N - 1)$ giá trị nguyên của $p$ không phải là bội số của $N$. Mỗi giá trị này tương ứng với một lần đa giác vectơ pha khép kín, tạo ra đúng $(N - 1)$ cực tiểu cường độ bằng không nằm xen kẽ giữa hai cực đại chính. Giữa các cực tiểu này là $(N - 2)$ cực đại phụ nhỏ; các cực đại phụ này trở nên rất nhỏ khi so với các cực đại chính lúc $N$ tăng lên.

</details>

![Hình 36.15: Đồ thị cường độ giao thoa của N khe hẹp cách đều nhau. (a) N = 2 khe: Giữa hai cực đại có một cực tiểu, chiều cao cực đại là 4I₀. (b) N = 8 khe: Các cực đại chính nằm tại cùng vị trí nhưng cao hơn (64I₀) và hẹp hơn rất nhiều, cách nhau bởi 7 cực tiểu. (c) N = 16 khe: Các cực đại thậm chí còn cao hơn nữa (256I₀) và rất sắc nét, cách nhau bởi 15 cực tiểu. Bề rộng của mỗi đỉnh cực đại chính tỷ lệ nghịch với N (tỷ lệ thuận với 1/N).](../img/young-36/hinh-36-15.png)

### Đặc tính năng lượng và độ sắc nét của hệ nhiều khe

Khi số lượng khe $N$ tăng lên:
- Tại các cực đại chính, $N$ sóng từ $N$ khe đều cùng pha, nên biên độ điện trường tổng hợp gấp $N$ lần biên độ của một khe: $E = N E_1$.
- Cường độ sáng tại đỉnh cực đại chính tỷ lệ với bình phương biên độ, tức là đạt giá trị $N^2 I_0$:
  - Với $N = 2$: Đỉnh cực đại có chiều cao $4I_0$ (Hình 36.15a).
  - Với $N = 8$: Đỉnh cực đại có chiều cao $64I_0$ (Hình 36.15b).
  - Với $N = 16$: Đỉnh cực đại có chiều cao $256I_0$ (Hình 36.15c).
- Theo định luật bảo toàn năng lượng, tổng công suất ánh sáng truyền qua toàn bộ hệ $N$ khe tỷ lệ thuận với $N$. Vì chiều cao mỗi cực đại chính tỷ lệ với $N^2$, **bề rộng góc của mỗi cực đại chính bắt buộc phải tỷ lệ nghịch với $N$ (tỷ lệ thuận với $1/N$)**:

$$
\begin{aligned}
\Delta\theta &\propto \frac{1}{N}
\end{aligned}
$$

Số khe $N$ càng lớn thì các cực đại chính càng hẹp, càng sáng và càng sắc nét. Đặc tính tập trung năng lượng vào các vạch rất hẹp này chính là cơ sở vật lý cho hoạt động của cách tử nhiễu xạ dùng trong quang phổ học.

### Câu hỏi tự kiểm tra 36.4

Giả sử hai khe hẹp, mỗi khe có bề rộng $a$, cách nhau một khoảng giữa hai tâm khe là $d = 2{,}5a$. Trong hệ vân giao thoa tạo bởi hai khe này, có xuất hiện các cực đại giao thoa bị khuyết hay không? Nếu có, đó là những cực đại nào? Nếu không, hãy giải thích lý do.

<details><summary>Xem đáp án và giải thích</summary>

Có. Các cực đại bị khuyết là $m_i = \pm 5, \pm 10, \pm 15, \dots$

Giải thích:

Một cực đại giao thoa bị khuyết khi nó thỏa mãn đồng thời hai điều kiện:
- Điều kiện cực đại giao thoa: Phương trình $d\sin\theta = m_i \lambda$ với $m_i = \pm 1, \pm 2, \dots$
- Điều kiện cực tiểu nhiễu xạ: Phương trình $a\sin\theta = m_d \lambda$ với $m_d = \pm 1, \pm 2, \dots$

Lập tỷ số giữa hai điều kiện, ta có mối liên hệ:

$$
\begin{aligned}
\frac{d}{a} &= \frac{m_i}{m_d}
\end{aligned}
$$

Thay giả thiết $d = 2{,}5a = \frac{5}{2}a$ vào biểu thức:

$$
\begin{aligned}
\frac{m_i}{m_d} &= 2{,}5 = \frac{5}{2} \\
m_i &= 2{,}5 m_d = \frac{5}{2} m_d
\end{aligned}
$$

Vì bậc giao thoa $m_i$ bắt buộc phải là một số nguyên, giá trị của $m_d$ phải là một số nguyên chẵn khác không:
- Với $m_d = \pm 2$: Ta có $m_i = \frac{5}{2} \times (\pm 2) = \pm 5$. Cực đại giao thoa bậc 5 bị khuyết vì trùng đúng vào cực tiểu nhiễu xạ bậc 2.
- Với $m_d = \pm 4$: Ta có $m_i = \frac{5}{2} \times (\pm 4) = \pm 10$. Cực đại giao thoa bậc 10 bị khuyết vì trùng đúng vào cực tiểu nhiễu xạ bậc 4.
- Tổng quát, mọi cực đại giao thoa có bậc là bội số của 5 ($m_i = \pm 5k$ với $k = 1, 2, 3, \dots$) đều bị khuyết hoàn toàn.

</details>
