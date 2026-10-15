## 32.5. Sóng dừng điện từ

Sóng điện từ có thể phản xạ khi gặp bề mặt của một vật dẫn lý tưởng như tấm kim loại dẫn điện tốt, hoặc khi gặp mặt phân cách giữa hai môi trường điện môi trong suốt khác nhau. Khi sóng tới và sóng phản xạ có cùng tần số, cùng phân cực và bằng nhau về biên độ, sự chồng chất của chúng tạo sóng dừng điện từ, tương tự như hiện tượng sóng dừng trên sợi dây đàn hồi có một đầu cố định.

Giả sử đặt một tấm dẫn điện lý tưởng (điện trở suất bằng không) trong mặt phẳng $yz$ tại vị trí $x = 0$. Một sóng điện từ phân cực phẳng lan truyền theo chiều âm trục $x$ tiến tới đập vào bề mặt này. Tại bề mặt của một vật dẫn lý tưởng, điện trường không thể có thành phần tiếp tuyến khác không, vì các điện tích tự do đáp ứng với điện trường và thiết lập dòng điện mặt. Trong giới hạn dẫn điện lý tưởng, điều kiện biên đòi hỏi điện trường tiếp tuyến tổng cộng bằng không. Do đó, thành phần tiếp tuyến của điện trường tổng cộng tại mọi điểm trên bề mặt vật dẫn trong mặt phẳng $yz$ bắt buộc phải luôn bằng không.

Sóng tới mang điện trường biến thiên đập vào bề mặt kim loại sẽ kích thích các dòng điện cảm ứng dao động trên lớp bề mặt. Chính các dòng điện mặt này phát ra một sóng điện từ mới, lan truyền ngược trở lại theo chiều dương trục $x$, đóng vai trò là sóng phản xạ. Điện trường tổng cộng trong không gian và trên bề mặt vật dẫn bằng tổng vector của điện trường sóng tới và điện trường sóng phản xạ.

Xét sóng tới phân cực theo trục $y$, truyền theo chiều âm trục $x$:

$$
\begin{aligned}
E_{y,\text{inc}} &= E_{\max} \times \cos(kx + \omega t), \\
B_{z,\text{inc}} &= -B_{\max} \times \cos(kx + \omega t)
\end{aligned}
$$

Sóng phản xạ do dòng cảm ứng trên mặt phẳng $x = 0$ phát ra truyền theo chiều dương trục $x$:

$$
\begin{aligned}
E_{y,\text{ref}} &= -E_{\max} \times \cos(kx - \omega t), \\
B_{z,\text{ref}} &= -B_{\max} \times \cos(kx - \omega t)
\end{aligned}
$$

Dấu trừ trước biên độ điện trường phản xạ đảm bảo rằng tại mặt phẳng $x = 0$, hai điện trường tới và phản xạ luôn ngược pha và triệt tiêu lẫn nhau tại mọi thời điểm:

$$
\begin{aligned}
E_y(0, t) &= E_{y,\text{inc}}(0, t) + E_{y,\text{ref}}(0, t) \\
&= E_{\max} \cos(\omega t) - E_{\max} \cos(-\omega t) \\
&= 0
\end{aligned}
$$

Theo nguyên lý chồng chất, điện trường và từ trường tổng cộng tại tọa độ $x$ bất kỳ là:

$$
\begin{aligned}
E_y &= E_{\max} [\cos(kx + \omega t) \\
&\qquad - \cos(kx - \omega t)], \\
B_z &= -B_{\max} [\cos(kx + \omega t) \\
&\qquad + \cos(kx - \omega t)]
\end{aligned}
$$

Áp dụng các công thức biến đổi lượng giác:

$$
\begin{aligned}
\cos(A + B) - \cos(A - B) &= -2 \sin A \sin B, \\
\cos(A + B) + \cos(A - B) &= 2 \cos A \cos B
\end{aligned}
$$

Ta thu được phương trình của điện trường trong sóng dừng điện từ:

$$
E_y(x, t) &= -2E_{\max} \times \sin kx \sin \omega t \tag{32.34}
$$

Phương trình của từ trường trong sóng dừng điện từ là:

$$
B_z(x, t) &= -2B_{\max} \times \cos kx \cos \omega t \tag{32.35}
$$

Biểu thức của điện trường cho thấy tại các mặt phẳng vuông góc với trục $x$ mà $\sin kx = 0$, điện trường luôn triệt tiêu ở mọi thời điểm. Điều kiện $\sin kx = 0$ tương ứng với $kx = 0, \pi, 2\pi, \dots$ Vì số sóng $k = 2\pi/\lambda$, tọa độ của các mặt phẳng nút điện trường là:

$$
x = 0, \frac{\lambda}{2}, \lambda, \frac{3\lambda}{2}, \dots \tag{32.36}
$$

Các mặt phẳng này được gọi là mặt phẳng nút của điện trường $\vec{E}$. Nằm xen kẽ chính giữa hai mặt phẳng nút liên tiếp là các mặt phẳng mà $\sin kx = \pm 1$. Tại đó, độ lớn điện trường đạt giá trị cực đại $2E_{\max}$ hai lần trong mỗi chu kỳ dao động. Đó là các mặt phẳng bụng của điện trường.

Đối với từ trường, điều kiện để từ trường triệt tiêu tại mọi thời điểm là $\cos kx = 0$, tức $kx = \pi/2, 3\pi/2, 5\pi/2, \dots$ Do đó, tọa độ các mặt phẳng nút của từ trường $\vec{B}$ là:

$$
x = \frac{\lambda}{4}, \frac{3\lambda}{4}, \frac{5\lambda}{4}, \dots \tag{32.37}
$$

Các mặt phẳng bụng của từ trường nằm chính giữa các mặt phẳng nút của nó, đặc biệt là ngay tại bề mặt vật dẫn $x = 0$.

![Hình 32.22: Cấu trúc điện trường và từ trường của sóng dừng điện từ phân cực thẳng tại thời điểm góc pha thời gian bằng 135 độ.](../img/young-32/hinh-32-22.png)

Từ trường không hề triệt tiêu tại bề mặt vật dẫn $x = 0$. Dòng điện mặt cảm ứng làm triệt tiêu điện trường tiếp tuyến lại chính là nguồn sinh ra từ trường tiếp tuyến tại bề mặt này. Tương tự sự xen kẽ giữa nút áp suất và nút li độ trong sóng âm dừng, nút điện trường và nút từ trường là hai họ mặt phẳng khác nhau. Khoảng cách giữa hai mặt phẳng nút liên tiếp của cùng một trường bằng một nửa bước sóng ($\lambda/2$). Mặt phẳng nút của trường này trùng với mặt phẳng bụng của trường kia: Nút của $\vec{E}$ là bụng của $\vec{B}$, và ngược lại.

Về mặt thời gian, điện trường biến thiên theo $\sin \omega t$, trong khi từ trường biến thiên theo $\cos \omega t$. Do đó, dao động của điện trường và từ trường tại mỗi điểm có cả hai biên độ khác không lệch pha nhau $90^\circ$ theo thời gian. Tại nút của một trường, trường đó luôn bằng không và không có pha dao động để so sánh. Tại những thời điểm mà $\sin \omega t = 0$, điện trường triệt tiêu đồng loạt trên toàn bộ không gian, còn từ trường đạt độ lớn cực đại cục bộ. Ngược lại, khi $\cos \omega t = 0$, từ trường triệt tiêu trên toàn bộ không gian, còn điện trường đạt độ lớn cực đại cục bộ. Tính chất này hoàn toàn khác biệt so với sóng chạy đơn hướng, nơi điện trường và từ trường biến thiên đồng pha cả về không gian lẫn thời gian.

Các phương trình sóng dừng trên thỏa mãn trọn vẹn phương trình sóng một chiều và hệ phương trình Maxwell trong chân không.

### Sóng dừng trong hộp cộng hưởng

Xét một hộp cộng hưởng giới hạn bởi hai mặt phẳng dẫn điện lý tưởng song song, đặt vuông góc với trục $x$ tại $x = 0$ và $x = L$. Hệ này tương tự như một sợi dây đàn cố định hai đầu.

Vì cả hai thành kim loại đều là vật dẫn lý tưởng, điện trường tiếp tuyến bắt buộc phải triệt tiêu tại cả hai biên $x = 0$ và $x = L$. Điều kiện $E_y(L, t) = 0$ đòi hỏi $\sin k L = 0$, tức là $k L = n\pi$ với $n = 1, 2, 3, \dots$ Khoảng cách $L$ giữa hai thành phải bằng một số nguyên lần nửa bước sóng:

$$
L = n \frac{\lambda}{2}
$$

Hệ thống chỉ cho phép các mode dao động riêng với các bước sóng gián đoạn:

$$
\lambda_n = \frac{2L}{n} \quad (n = 1, 2, 3, \dots) \tag{32.38}
$$

Các tần số dao động riêng tương ứng là:

$$
\begin{aligned}
f_n &= \frac{c}{\lambda_n} \\
&= n \frac{c}{2L} \\
\end{aligned} \tag{32.39}
$$

Mỗi mode sóng riêng đặc trưng bởi một tần số, một dạng phân bố trường và một hệ thống nút bụng xác định. Bằng cách đo khoảng cách giữa các vị trí nút, người ta xác định được bước sóng. Khi biết trước tần số, việc đo đạc này cho phép tính chính xác tốc độ lan truyền của sóng điện từ. Hertz đã dùng phương pháp này vào những năm 1880 trong các thí nghiệm khảo sát sóng điện từ.

Sóng điện từ cũng phản xạ tại mặt phân cách giữa hai môi trường cách điện có tính chất điện môi hoặc từ khác nhau. Tình huống này tương tự sóng cơ học gặp điểm nối giữa hai sợi dây có cùng lực căng nhưng mật độ khối lượng dài khác nhau. Hiện tượng ánh sáng phản xạ một phần và truyền qua một phần tại mặt kính cửa sổ là một ví dụ quen thuộc.

![Hình 32.23: Lò vi sóng thiết lập sóng dừng với bước sóng 12,2 cm, được nước trong thức ăn hấp thụ mạnh. Khoảng cách các nút là 6,1 cm. Đĩa xoay đưa thức ăn qua các vùng điện trường khác nhau, giúp tránh để một phần thức ăn mãi ở nút điện trường.](../img/young-32/hinh-32-23.png)

::: example Ví dụ 32.6: Cường độ trong sóng dừng
Hãy xác định cường độ của sóng dừng điện từ biểu diễn bởi phương trình của $E_y(x, t)$ và $B_z(x, t)$.

**Nhận dạng và chuẩn bị:** Cường độ sóng $I$ bằng độ lớn của giá trị trung bình theo thời gian của vector Poynting: $I = |\langle \vec{S} \rangle| = S_{\text{av}}$. Ta tính biểu thức tức thời của $\vec{S}(x, t)$ từ định nghĩa tích có hướng $\vec{S} = \frac{1}{\mu_0} \vec{E} \times \vec{B}$, sau đó lấy giá trị trung bình của vector này theo thời gian trong một chu kỳ sóng.

**Lời giải:**

Thay các hàm sóng vào biểu thức vector Poynting:

$$
\begin{aligned}
\vec{S}(x, t) &= \frac{1}{\mu_0} \vec{E} \times \vec{B} \\
&= \frac{1}{\mu_0} [-\hat{\jmath} 2 E_{\max}] \times [\sin kx \sin \omega t] \times [-\hat{k} 2 B_{\max}] \times [\cos kx \cos \omega t] \\
&= \hat{\imath} \frac{E_{\max} B_{\max}}{\mu_0} \times (2 \sin kx \cos kx) \times (2 \sin \omega t \cos \omega t)
\end{aligned}
$$

Áp dụng hệ thức $\sin 2A = 2 \sin A \cos A$:

$$
S_x(x, t) &= \frac{E_{\max} B_{\max}}{\mu_0} \times \sin 2kx \sin 2\omega t
$$

Giá trị trung bình theo thời gian của hàm sin trong một hoặc nhiều chu kỳ nguyên vẹn luôn bằng không: $\langle \sin 2\omega t \rangle = 0$. Do đó, vector Poynting trung bình theo thời gian bằng không tại mọi điểm: $\langle \vec{S}(x, t) \rangle = \vec{0}$, kéo theo cường độ bức xạ triệt tiêu:

$$
\begin{aligned}
I &= |\langle \vec{S} \rangle| \\
&= S_{\text{av}} \\
&= 0
\end{aligned}
$$

**Đánh giá:** Kết quả này phản ánh bản chất của sóng dừng: Hai sóng chạy có cùng biên độ và tần số truyền ngược chiều nhau làm triệt tiêu dòng năng lượng thuần khi lấy trung bình theo thời gian. Dòng năng lượng tức thời vẫn có thể đổi chiều và vận chuyển năng lượng giữa các vùng lân cận. Khi truyền công suất đến một vật nhận, cần hạn chế phản xạ làm giảm dòng năng lượng thuần hướng tới vật nhận.
Cần lưu ý: Cường độ bức xạ $I$ là độ lớn của vector trung bình theo thời gian $I = |\langle \vec{S} \rangle| = 0$, chứ không phải giá trị trung bình của độ lớn $\langle |\vec{S}| \rangle$. Vì $|\sin 2\omega t| \ge 0$, giá trị trung bình của độ lớn $\langle |S_x| \rangle$ có thể dương khi $\sin 2kx\ne0$, đặc trưng cho biên độ dao động năng lượng qua lại tại mỗi vị trí. Sóng dừng lý tưởng không đồng nghĩa với sự tiêu tán năng lượng thành nhiệt. Phản xạ toàn phần đổi hướng dòng năng lượng, làm dòng trung bình thuần triệt tiêu. Sự tiêu tán đòi hỏi điện trở hoặc một cơ chế tổn hao trong vật chất.
:::

::: example Ví dụ 32.7: Sóng dừng trong hộp cộng hưởng
Sóng dừng điện từ được thiết lập trong một hộp cộng hưởng có hai thành dẫn điện lý tưởng đặt song song cách nhau $1{,}50\,\mathrm{cm}$. (a) Hãy tính bước sóng dài nhất $\lambda_1$ và tần số thấp nhất $f_1$ của sóng dừng có thể tồn tại trong hộp. (b) Với sóng dừng có bước sóng này, điện trường $\vec{E}$ đạt độ lớn cực đại ở đâu và triệt tiêu ở đâu? Từ trường $\vec{B}$ đạt cực đại ở đâu và triệt tiêu ở đâu?

**Nhận dạng và chuẩn bị:** Trong hộp cộng hưởng, hai thành kim loại đóng vai trò là hai mặt phẳng nút cố định của điện trường $\vec{E}$. Bước sóng dài nhất và tần số thấp nhất tương ứng với mode cơ bản $n = 1$. Khoảng cách hai thành khi đó bằng đúng một nửa bước sóng. Các mặt phẳng bụng của trường này chính là mặt phẳng nút của trường kia.

**Lời giải:**

(a) Bước sóng và tần số của mode cơ bản $n = 1$:

$$
\lambda_1 = 2L = 2(1{,}50\,\mathrm{cm}) = 3{,}00\,\mathrm{cm}
$$

Tần số dao động tương ứng:

$$
\begin{aligned}
f_1 &= \frac{c}{2L} \\
&= \frac{3{,}00 \times 10^8\,\mathrm{m/s}}{2(1{,}50 \times 10^{-2}\,\mathrm{m})} \\
&= 1{,}00 \times 10^{10}\,\mathrm{Hz} \\
&= 10\,\mathrm{GHz}
\end{aligned}
$$

(b) Với $n = 1$, chiều dài hộp đúng bằng một nửa bước sóng:

Điện trường có các mặt phẳng nút ($\vec{E} = 0$) tại hai thành hộp kim loại ($x = 0$ và $x = 1{,}50\,\mathrm{cm}$). Điện trường đạt độ lớn cực đại tại mặt phẳng bụng nằm chính giữa hai thành hộp, tại tọa độ $x = 0{,}75\,\mathrm{cm}$.

Từ trường có mặt phẳng nút ($\vec{B} = 0$) tại mặt phẳng chính giữa hộp ($x = 0{,}75\,\mathrm{cm}$). Từ trường đạt độ lớn cực đại tại hai mặt phẳng bụng nằm ngay trên bề mặt kim loại của hai thành hộp ($x = 0$ và $x = 1{,}50\,\mathrm{cm}$).

**Đánh giá:** Một ứng dụng thực tiễn của hộp cộng hưởng là tạo ra điện trường dao động mạnh ở tần số xác định để khảo sát tính chất vi mô của mẫu vật. Để mẫu chịu tác dụng của điện trường mạnh nhất, người ta bố trí mẫu vật đặt tại trung tâm hộp, nơi có bụng của điện trường $\vec{E}$.
:::

### Câu hỏi tự kiểm 32.5

Trong sóng dừng được mô tả ở Ví dụ 32.7, có tồn tại vị trí nào trong hộp cộng hưởng mà mật độ năng lượng luôn bằng không ở mọi thời điểm hay không? Nếu có thì ở đâu, nếu không thì vì sao?

<details><summary>Xem đáp án và giải thích</summary>

Đáp án là không có vị trí nào trong hộp cộng hưởng mà mật độ năng lượng đồng nhất bằng không ở mọi thời điểm, mặc dù tại một thời điểm tức thời riêng biệt thì mật độ năng lượng tại một vị trí nút có thể bằng không.

Giải thích:

Tại bề mặt hai thành hộp kim loại ($x = 0$ và $x = L$), điện trường luôn triệt tiêu ở mọi thời điểm ($\vec{E} = 0$), nên mật độ năng lượng điện trường $u_E = \frac{1}{2}\epsilon_0 E^2$ luôn bằng không. Tuy nhiên, từ trường tại hai thành hộp lại dao động với biên độ cực đại: $B_z = -2B_{\max} \cos \omega t$. Vào những thời điểm $\cos \omega t \ne 0$, từ trường khác không nên mật độ năng lượng từ trường $u_B = B^2/(2\mu_0) > 0$. Chỉ tại các thời điểm tức thời mà $\cos \omega t = 0$ (ứng với $\omega t = \pi/2, 3\pi/2, \dots$) thì từ trường mới triệt tiêu tức thời và đưa tổng mật độ năng lượng $u = u_E + u_B = 0$.

Ngược lại, tại mặt phẳng trung tâm nằm giữa hai thành hộp ($x = L/2$), từ trường luôn triệt tiêu ở mọi thời điểm ($\vec{B} = 0$), nên $u_B$ luôn bằng không. Nhưng tại đây, điện trường lại dao động với biên độ cực đại $E_y = -2E_{\max} \sin \omega t$. Mật độ năng lượng điện trường $u_E$ khác không hầu hết thời gian, chỉ triệt tiêu tức thời tại các thời điểm $\sin \omega t = 0$ (ứng với $\omega t = 0, \pi, 2\pi, \dots$).

Vì dao động của điện trường và từ trường lệch pha nhau $90^\circ$ theo thời gian ($\sin \omega t$ và $\cos \omega t$), không tồn tại bất kỳ điểm nào trong không gian mà cả điện trường và từ trường đồng thời triệt tiêu ở mọi thời điểm. Do đó, không có điểm nào có mật độ năng lượng đồng nhất bằng không theo thời gian, dù tại một thời điểm tức thời xác định, năng lượng tại một điểm nút có thể bằng không.

</details>
