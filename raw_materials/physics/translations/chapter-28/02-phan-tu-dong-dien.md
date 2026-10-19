## 28.2 Từ trường của một phần tử dòng điện

Khi nhiều điện tích chuyển động, mỗi điện tích góp một phần vào từ trường tổng. Vì từ trường là véc-tơ, ta cộng các đóng góp theo quy tắc cộng véc-tơ. Với hai nguồn:

$$
\vec B_{\mathrm{tot}} = \vec B_1+\vec B_2. \tag{28.5}
$$

Với $N$ nguồn, cách viết tường minh là:

$$
\vec B_{\mathrm{tot}} = \vec B_1+\vec B_2 +\cdots+\vec B_N.
$$

Ta dùng nguyên lý chồng chất để tính từ trường do một đoạn rất ngắn của dây dẫn mang dòng điện tạo ra. Gọi $A$ là diện tích tiết diện dây, $d\ell$ là độ dài đoạn dây, $n$ là mật độ hạt tải điện và $q$ là điện tích của mỗi hạt. Đoạn dây có thể tích $A\,d\ell$, nên số hạt tải trong đoạn ấy là $nA\,d\ell$. Nếu các hạt cùng trôi với tốc độ $v_d$, độ lớn điện tích chuyển động tương đương là:

$$
|dQ| = n|q|A\,d\ell.
$$

Các vận tốc nhiệt ngẫu nhiên phân bố theo nhiều hướng nên đóng góp từ trường của chúng triệt tiêu trung bình. Phần từ trường còn lại tương ứng với chuyển động có hướng của các hạt tải.

![Véc-tơ từ trường do một phần tử dòng điện tạo ra và các đường sức từ quanh trục dòng điện](../img/young-28/hinh-28-03.png)

Hình 28.3: Từ trường của phần tử dòng điện có dạng tương tự từ trường của một điện tích chuyển động.

Độ lớn từ trường của đoạn nhỏ được tính từ công thức cho điện tích chuyển động. Thay điện tích bằng $|dQ|$ và tốc độ bằng $v_d$, ta có:

$$
\begin{aligned}
dB &= \frac{\mu_0}{4\pi} \frac{|dQ|v_d\sin\phi}{r^2} \\
&= \frac{\mu_0}{4\pi} n|q|A v_d \frac{d\ell\sin\phi}{r^2}.
\end{aligned}
$$

Dòng điện là lượng điện tích quy ước đi qua tiết diện trong một đơn vị thời gian. Với các hạt tải có cùng tốc độ trôi, độ lớn dòng điện là $I=n|q|v_dA$. Thay tích này vào biểu thức trên, ta được định luật Biot–Savart ở dạng độ lớn:

$$
dB = \frac{\mu_0 I}{4\pi} \frac{d\ell\sin\phi}{r^2}.
$$

Véc-tơ dòng điện luôn chỉ theo chiều dòng điện quy ước. Với hạt tải âm, vận tốc trôi ngược chiều dòng điện nhưng điện tích $q$ cũng mang dấu âm, nên $q\vec v_d$ vẫn cùng chiều dòng điện. Vì thế, biểu thức dùng $I\,d\vec\ell$ mô tả đúng hướng từ trường dù dòng điện do electron hay ion dương tạo ra.

Gọi $\hat r$ là véc-tơ đơn vị hướng từ phần tử dòng điện đến điểm đo. Hướng của từ trường được xác định bằng tích có hướng $d\vec\ell\times\hat r$. Từ trường vuông góc với mặt phẳng chứa phần tử dây và đường nối phần tử dây với điểm đo.

$$
d\vec B = \frac{\mu_0 I}{4\pi r^2} \left(d\vec\ell \times \hat r\right). \tag{28.6}
$$

Các đường sức của phần tử dòng điện là những vòng tròn nằm trong các mặt phẳng vuông góc với $d\vec\ell$. Ngón cái bàn tay phải chỉ theo chiều dòng điện, các ngón tay khum theo chiều đường sức từ. Khi quan sát một mạch hoàn chỉnh, ta không thể tách riêng một phần tử dòng điện để đo. Ta kiểm tra định luật bằng cách tính trường của cả mạch rồi so sánh với phép đo.

Nếu đặt vật liệu gần dây dẫn, sự từ hóa của vật liệu có thể bổ sung thêm từ trường. Phần bổ sung thường nhỏ nếu vật liệu không phải sắt từ. Trường biến thiên theo thời gian và vật liệu siêu dẫn tạo ra những vấn đề khác, dành cho phần sau của chương.

### Từ trường của toàn bộ mạch

Để tìm từ trường của cả dây, ta chia dây thành các đoạn vi phân. Mỗi đoạn tạo một véc-tơ $d\vec B$ tại điểm cần xét. Từ trường tổng là tích phân véc-tơ trên toàn đường dây mang dòng điện:

$$
\vec B = \frac{\mu_0 I}{4\pi} \int_{\mathrm{wire}} \frac{d\vec\ell\times\hat r}{r^2}. \tag{28.7}
$$

Tích phân này là phép cộng liên tục các đóng góp trên toàn bộ dây. Nếu các véc-tơ $d\vec B$ cùng hướng, ta có thể cộng độ lớn. Nếu hướng khác nhau, phải phân tích thành phần rồi cộng theo từng trục.

### Ứng dụng: Từ trường của các hành tinh

![So sánh kích thước Trái Đất và Sao Mộc trong ứng dụng về từ trường hành tinh](../img/young-28/ung-dung-tu-truong-hanh-tinh.png)

Trái Đất tạo từ trường nhờ các dòng điện lưu thông trong phần lõi nóng chảy có khả năng dẫn điện. Sự quay của hành tinh khuấy trộn vật chất dẫn điện ấy. Trái Đất quay hết một vòng trong khoảng 24 giờ.

Các dòng điện bên trong Sao Mộc mạnh hơn. Sao Mộc lớn hơn Trái Đất, có phần bên trong chủ yếu là hiđrô lỏng dẫn điện tốt dưới áp suất lớn, đồng thời quay nhanh hơn. Một vòng quay của Sao Mộc kéo dài khoảng 10 giờ. Ở cùng khoảng cách từ tâm hành tinh, độ lớn từ trường của Sao Mộc vào khoảng $2\times10^4$ lần từ trường của Trái Đất.

### Chiến lược giải 28.1: Tính từ trường

**Nhận diện.** Định luật Biot–Savart phù hợp khi cần tìm từ trường tại điểm $P$ do phần tử dòng điện hoặc dây dẫn có hình dạng bất kỳ tạo ra.

**Thiết lập.** Vẽ dây và điểm đo. Chọn một phần tử $d\vec\ell$ theo đúng chiều dòng điện quy ước. Vẽ $\hat r$ từ phần tử đến $P$, rồi xác định đại lượng cần tìm, thường là $\vec B$.

**Thực hiện.** Dùng phương trình (28.5) hoặc (28.6) để viết đóng góp của từng phần tử. Cộng các đóng góp theo véc-tơ, bằng cách tích phân trực tiếp hoặc tính từng thành phần. Nếu đối xứng buộc một thành phần bằng không, nêu rõ đối xứng đó trước khi bỏ thành phần ấy.

Với một dây gồm nhiều đoạn đơn giản, có thể tính từ trường của từng đoạn rồi cộng các véc-tơ. Hãy tận dụng đối xứng khi nó làm giảm số thành phần cần tính.

**Đánh giá.** Kiểm tra hướng bằng quy tắc bàn tay phải. Xét các giới hạn xa hoặc gần nguồn và đối chiếu với dự đoán đối xứng.

::: example Ví dụ 28.2 Từ trường của một đoạn dây
Một dây đồng mang dòng điện ổn định $I=125\,\mathrm A$. Xét đoạn dây dài $d\ell=1{,}0\,\mathrm{cm}$ như Hình 28.4. Tìm từ trường do đoạn dây này tạo ra tại điểm cách nó $r=1{,}2\,\mathrm m$ trong hai trường hợp sau. Trường hợp (a), điểm $P_1$ nằm ngang bên cạnh đoạn dây, theo phương vuông góc với dây. Trường hợp (b), điểm $P_2$ nằm trong mặt phẳng $xy$, theo hướng tạo góc $30^\circ$ so với chiều $-x$.

![Đoạn dây mang dòng điện 125 A và hai điểm đo P₁, P₂](../img/young-28/hinh-28-04.png)

Hình 28.4: Hai vị trí đo từ trường của cùng một đoạn dây ngắn.

Trong hình, dòng điện quy ước hướng theo $-x$, nên $d\vec\ell=-d\ell\,\hat\imath$. Ở $P_1$, véc-tơ đơn vị từ đoạn dây đến điểm đo là $\hat r_1=\hat\jmath$. Vì vậy:

$$
\begin{aligned}
\vec B_1 &= \frac{\mu_0 I}{4\pi r^2} \left(d\vec\ell\times\hat r_1\right) \\
&= -\frac{\mu_0 I d\ell}{4\pi r^2}\,\hat k.
\end{aligned}
$$

Thay $\mu_0/(4\pi)=1{,}0\times10^{-7}\,\mathrm{T\,m/A}$, $d\ell=1{,}0\times10^{-2}\,\mathrm m$ và $r=1{,}2\,\mathrm m$:

$$
\vec B_1 = -8{,}7\times10^{-8}\,\hat k\,\mathrm T.
$$

Tại $P_2$, véc-tơ đơn vị là $\hat r_2=-\cos30^\circ\,\hat\imath+\sin30^\circ\,\hat\jmath$. Khi tính tích có hướng, thành phần theo $x$ triệt tiêu, còn thành phần theo $y$ tạo hướng $-z$:

$$
\begin{aligned}
\vec B_2 &= \frac{\mu_0 I}{4\pi r^2} \left[-d\ell\,\hat\imath\times\hat r_2\right] \\
&= -\frac{\mu_0 I d\ell\sin30^\circ}{4\pi r^2}\,\hat k \\
&= -4{,}3\times10^{-8}\,\hat k\,\mathrm T.
\end{aligned}
$$

Ở cả hai điểm, từ trường hướng vào mặt phẳng $xy$. Kết quả này phù hợp với Hình 28.3: Mặt phẳng $xy$ tương ứng với mặt phẳng màu be, nhưng chiều dòng điện trong ví dụ ngược với chiều phần tử trong hình nên chiều từ trường cũng đảo lại.
:::

### Tự kiểm tra 28.2

Một phần tử dòng điện nằm tại gốc tọa độ và có dòng điện hướng theo $+y$. Hãy xếp bốn điểm $(i)$ $(L,0,0)$, $(ii)$ $(0,L,0)$, $(iii)$ $(0,0,L)$ và $(iv)$ $(L/\sqrt2,L/\sqrt2,0)$ theo độ lớn từ trường do phần tử tạo ra, từ lớn nhất đến nhỏ nhất.

::: details Đáp án
Độ lớn từ trường tỉ lệ với $\sin\phi/r^2$. Cả bốn điểm cách gốc một khoảng $L$. Tại (i) và (iii), $\phi=90^\circ$ nên $\sin\phi=1$. Tại (ii), điểm nằm dọc chiều dòng điện nên $\phi=0$ và từ trường bằng không. Tại (iv), $\phi=45^\circ$ nên $\sin\phi=1/\sqrt2$. Thứ tự là (i) và (iii) đồng hạng, tiếp đến (iv), cuối cùng là (ii).
:::
