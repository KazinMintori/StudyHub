## 40.5. Dao động tử điều hòa

Màng nhĩ dao động khi nhận sóng âm, còn mặt đất dao động trong một trận động đất. Ở thang vi mô, phân tử khí rung động sau va chạm, proton và neutron trong hạt nhân kích thích có thể dao động tương đối, còn trường vi sóng làm các phân tử nước quay đổi hướng.

Các chuyển động ấy không phải đều là dao động điều hòa lý tưởng. Tuy nhiên, gần một vị trí cân bằng bền, thế năng thường gần một parabol. Vì vậy, dao động tử điều hòa lượng tử là mô hình cơ sở để khảo sát nhiều hệ vi mô.

### Mô hình lực và dự đoán khoảng cách mức

Xét hạt khối lượng $m$ chuyển động trên trục $x$ dưới tác dụng của lực bảo toàn

$$
F_x=-k'x.
$$

Hằng số lực được ký hiệu $k'$ để phân biệt với số sóng $k$. Chọn thế năng bằng không tại vị trí cân bằng:

$$
U(x)=\frac12k'x^2.
$$

Trong mô tả Newton, tần số góc và tần số của dao động là

$$
\omega=\sqrt{\frac{k'}{m}},
\qquad f=\frac{\omega}{2\pi}.
$$

Với biên độ $A$, cơ năng bằng

$$
E=\frac12k'A^2.
$$

![Hình 40.23: Thế năng parabol của dao động tử. Hai giao điểm giữa đường cơ năng E và parabol cho các biên độ cổ điển −A và A. Trong mô tả lượng tử, hạt có xác suất xuất hiện cả ngoài khoảng này.](../img/young-40/hinh-40-23.png)

Trong điện từ học cổ điển, electron dao động với tần số góc $\omega$ phát bức xạ cùng tần số góc ấy. Điều này gợi ý rằng một chuyển mức giữa hai mức kề nhau của dao động tử lượng tử có thể phát photon với năng lượng

$$
hf=\hbar\omega=\hbar\sqrt{\frac{k'}{m}}.
\tag{40.43}
$$

Đây cũng là khoảng cách mức Planck đã dùng khi xây dựng định luật bức xạ. Nhưng lập luận tương ứng với dao động cổ điển mới là dự đoán. Ta cần phương trình Schrödinger và điều kiện biên để xác định mức năng lượng thực sự.

### Điều kiện biên chọn ra những năng lượng nào?

Viết $\psi=\psi(x)$ và dùng dấu phẩy để chỉ đạo hàm theo $x$. Phương trình Schrödinger không phụ thuộc thời gian trở thành

$$
-\frac{\hbar^2}{2m}\psi''
+\frac12k'x^2\psi=E\psi.
\tag{40.44}
$$

Các nghiệm vật lý phải chuẩn hóa được. Thế năng tăng không giới hạn khi $|x|$ lớn, nên hàm sóng của trạng thái liên kết phải tiến về không khi $|x|\to\infty$. Khác với giếng thành đứng, ở đây không có một bức tường hữu hạn để áp điều kiện $\psi=0$ ngay tại biên độ cổ điển.

Chuyển vế phương trình trên:

$$
\psi''=\frac{2m}{\hbar^2}
\left(\frac12k'x^2-E\right)\psi.
\tag{40.45}
$$

Ở ngoài miền cổ điển, $k'x^2/2>E$. Vì hệ số trong ngoặc dương, $\psi''$ và $\psi$ cùng dấu. Khi $\psi>0$, đồ thị cong lên. Khi $\psi<0$, đồ thị cong xuống.

![Hình 40.24: Bốn cách tiếp diễn của nghiệm trong miền thế năng lớn hơn cơ năng. Chỉ đường d tiến dần về trục hoành khi x tăng, phù hợp với điều kiện biên của trạng thái liên kết.](../img/young-40/hinh-40-24.png)

Xét một điểm $x>A$ mà tại đó $\psi$ dương. Độ dốc là $\psi'$, còn $\psi''$ quyết định độ dốc thay đổi như thế nào.

- Với đường a, độ dốc đã dương và còn tăng. Hàm tăng không giới hạn, nên không thể là hàm sóng chuẩn hóa.
- Với đường b, độ dốc ban đầu âm nhưng độ cong dương quá lớn. Độ dốc chuyển sang dương rồi tăng, khiến hàm cũng phân kỳ lên.
- Với đường c, độ dốc âm nhưng độ cong dương quá nhỏ để ngăn hàm vượt qua trục hoành. Khi $\psi$ chuyển sang âm, $\psi''$ cũng âm và hàm phân kỳ xuống.
- Với đường d, độ dốc và độ cong vừa đủ để hàm giảm dần về không. Khi $x$ tăng, hàm cùng các đạo hàm cần thiết đều tắt dần.

Muốn nghiệm có dạng chấp nhận được ở cả hai phía vô hạn, năng lượng không thể nhận giá trị tùy ý. Điều kiện biên chỉ được thỏa ở những mức

$$
\begin{aligned}
E_n&=\left(n+\frac12\right)\hbar\omega\\
&=\left(n+\frac12\right)\hbar\sqrt{\frac{k'}{m}}.
\end{aligned}
\tag{40.46}
$$

Ở đây $n=0,1,2,\ldots$. Các mức đầu là

$$
\begin{aligned}
E_0&=\frac12\hbar\omega,\\
E_1&=\frac32\hbar\omega,\\
E_2&=\frac52\hbar\omega,\\
E_3&=\frac72\hbar\omega.
\end{aligned}
$$

![Công thức 40.46: Năng lượng của dao động tử được quyết định bởi số lượng tử n, khối lượng hạt m và hằng số lực k′. Tần số góc ω cũng là tần số góc của dao động Newton tương ứng.](../img/young-40/cong-thuc-40-46.png)

Trạng thái cơ bản được đánh số $n=0$, khác với quy ước $n=1$ cho mức thấp nhất của hạt trong hộp. Khoảng cách giữa mọi cặp mức liền nhau đều bằng $\hbar\omega$. Có vô hạn mức vì thế năng parabol không có giới hạn trên.

![Hình 40.25: Sáu mức thấp nhất của dao động tử điều hòa. Mức thấp nhất có năng lượng ℏω/2 và mọi khoảng cách mức kề nhau đều bằng ℏω.](../img/young-40/hinh-40-25.png)

### Ví dụ 40.8: Nguyên tử sodium dao động trong tinh thể

Một nguyên tử sodium khối lượng $3{,}82\times10^{-26}\,\mathrm{kg}$ dao động trong tinh thể. Thế năng tăng $0{,}0075\,\mathrm{eV}$ khi nguyên tử lệch khỏi vị trí cân bằng $0{,}014\,\mathrm{nm}$. Xem nguyên tử như một dao động tử điều hòa.

(a) Tìm tần số góc theo mô tả Newton. (b) Tìm khoảng cách giữa hai mức dao động liền nhau, theo đơn vị electron-volt. (c) Tìm bước sóng photon phát ra khi chuyển xuống mức liền kề và xác định miền phổ.

**Nhận dạng:** Độ tăng thế năng cùng độ lệch cho hằng số lực. Hằng số ấy xác định cả tần số cổ điển lẫn khoảng cách mức lượng tử.

**Chuẩn bị:** Chọn gốc thế năng tại cân bằng. Dùng $U=k'x^2/2$, sau đó tính $\omega$, $\hbar\omega$ và $\lambda=hc/\Delta E$ theo đúng thứ tự.

**Thực hiện:** Đổi thế năng sang joule:

$$
U\approx1{,}2\times10^{-21}\,\mathrm J.
$$

Thay giá trị đã làm tròn này và độ lệch $x=0{,}014\times10^{-9}\,\mathrm m$:

$$
k'=\frac{2U}{x^2}\approx12{,}2\,\mathrm{N/m}.
$$

(a) Tần số góc là

$$
\begin{aligned}
\omega&=\sqrt{\frac{k'}{m}}\\
&\approx1{,}79\times10^{13}\,\mathrm{rad/s}.
\end{aligned}
$$

(b) Khoảng cách giữa hai mức liền nhau:

$$
\begin{aligned}
\Delta E&=\hbar\omega\\
&\approx1{,}89\times10^{-21}\,\mathrm J\\
&\approx0{,}0118\,\mathrm{eV}.
\end{aligned}
$$

(c) Photon mang đúng phần năng lượng dao động bị mất:

$$
\begin{aligned}
\lambda&=\frac{hc}{\Delta E}\\
&\approx1{,}05\times10^{-4}\,\mathrm m\\
&=105\,\mathrm{\mu m}.
\end{aligned}
$$

Đây là bức xạ hồng ngoại.

**Đánh giá:** Hằng số lực giữa các nguyên tử có thể chỉ cỡ vài đến vài chục newton trên mét, cùng bậc với một số lò xo gia dụng hoặc đồ chơi lò xo. Tuy nhiên, khối lượng nguyên tử rất nhỏ nên tần số dao động rất cao. Đo phổ bức xạ chuyển mức giúp xác định dao động của phân tử.

### Hàm sóng trạng thái cơ bản

Các hàm sóng của dao động tử là những hàm Hermite, mỗi hàm gồm một đa thức nhân với một hàm mũ Gaussian. Với trạng thái cơ bản,

$$
\psi_0(x)=Ce^{-\sqrt{mk'}\,x^2/(2\hbar)}.
\tag{40.47}
$$

Hằng số $C$ dùng để chuẩn hóa hàm sóng. Ta không dùng chữ $A$ cho hệ số này vì $A$ đã chỉ biên độ dao động Newton.

Đặt

$$
\alpha=\frac{\sqrt{mk'}}{\hbar}
=\frac{m\omega}{\hbar}.
$$

Điều kiện chuẩn hóa trên toàn trục là

$$
\int_{-\infty}^{\infty}|\psi_0(x)|^2\,dx=1.
$$

Với $\alpha>0$, tích phân Gaussian cho

$$
\int_{-\infty}^{\infty}e^{-\alpha x^2}\,dx
=\sqrt{\frac{\pi}{\alpha}}.
$$

Vì vậy, có thể chọn hệ số thực dương

$$
C=\left(\frac{\alpha}{\pi}\right)^{1/4}.
$$

<details><summary>Kiểm tra hàm Gaussian thỏa phương trình Schrödinger</summary>

Lấy đạo hàm hai lần:

$$
\psi_0'=-\alpha x\psi_0.
$$

$$
\psi_0''=(\alpha^2x^2-\alpha)\psi_0.
$$

Thế vào vế trái của phương trình (40.44). Hệ số của $x^2\psi_0$ bằng không vì

$$
\frac{\hbar^2\alpha^2}{2m}=\frac{k'}{2}.
$$

Phần còn lại bằng

$$
\frac{\hbar^2\alpha}{2m}\psi_0
=\frac12\hbar\omega\psi_0.
$$

Do đó, hàm Gaussian là nghiệm với năng lượng $E_0=\hbar\omega/2$. Việc kiểm tra này xác nhận cả dạng nghiệm và giá trị năng lượng cơ bản.

</details>

### So sánh phân bố lượng tử với chuyển động Newton

Với mỗi mức $E_n$, giao điểm của đường ngang năng lượng với parabol cho biên độ $A_n$ của dao động Newton có cùng cơ năng:

$$
\frac12k'A_n^2=\left(n+\frac12\right)\hbar\omega.
\tag{40.48}
$$

Bốn hàm sóng đầu tiên lần lượt có $1$, $2$, $3$ và $4$ cực trị hữu hạn. Tổng quát, hàm ở mức $n$ có $n+1$ cực trị. Mỗi đồ thị bên dưới còn đánh dấu hai biên độ cổ điển ứng với cùng năng lượng.

![Hình 40.26, n = 0: Hàm sóng trạng thái cơ bản không có nút bên trong. Hai đường nét đứt đánh dấu biên độ cổ điển, nhưng hàm sóng vẫn kéo dài ra ngoài.](../img/young-40/hinh-40-26-n0.png)

![Hình 40.26, n = 1: Hàm sóng có một nút và hai cực trị. Hàm khác không cả ở một phần miền bên ngoài biên độ cổ điển.](../img/young-40/hinh-40-26-n1.png)

![Hình 40.26, n = 2: Hàm sóng có hai nút và ba cực trị hữu hạn.](../img/young-40/hinh-40-26-n2.png)

![Hình 40.26, n = 3: Hàm sóng có ba nút và bốn cực trị hữu hạn.](../img/young-40/hinh-40-26-n3.png)

Bình phương độ lớn của các hàm sóng cho mật độ xác suất tìm thấy hạt. Các đường màu lam trong hình 40.27 biểu diễn phân bố cổ điển khi chọn một thời điểm ngẫu nhiên trong chu kỳ. Hạt cổ điển chuyển động chậm gần biên độ nên xác suất xuất hiện ở đó cao hơn.

![Hình 40.27, n = 0: Mật độ xác suất lượng tử màu lục tập trung quanh cân bằng. Phân bố Newton màu lam lại tăng mạnh gần hai biên độ.](../img/young-40/hinh-40-27-n0.png)

![Hình 40.27, n = 1: Mật độ xác suất lượng tử có nút tại tâm, trong khi đường Newton không có nút ấy.](../img/young-40/hinh-40-27-n1.png)

![Hình 40.27, n = 2: Mật độ xác suất dao động theo vị trí. Trung bình trên nhiều gợn sẽ gần phân bố cổ điển hơn khi số lượng tử tăng.](../img/young-40/hinh-40-27-n2.png)

![Hình 40.27, n = 3: Các đỉnh và nút lượng tử vẫn tồn tại, nhưng dáng bao của phân bố tiến gần dự đoán Newton.](../img/young-40/hinh-40-27-n3.png)

Hình 40.28 cho trường hợp $n=10$. So sánh trên thang không phân giải từng gợn nhỏ, sự phù hợp với phân bố Newton rõ hơn. Đây là một biểu hiện của sự tương ứng giữa mô tả lượng tử và mô tả cổ điển ở số lượng tử lớn.

![Hình 40.28: Phân bố lượng tử ở n = 10 cùng phân bố Newton có chung cơ năng. Khi làm trơn các gợn, hai dự đoán gần nhau hơn so với ở các mức thấp.](../img/young-40/hinh-40-28.png)

Khoảng cách giữa các nút tăng khi đi xa tâm. Theo mô tả Newton, thế năng tăng làm động năng và độ lớn động lượng giảm. Liên hệ de Broglie $\lambda=h/p$ vì thế cho bước sóng dài hơn ở gần biên độ. Cách đọc này giải thích định tính vì sao các nút thưa dần.

### Vì sao năng lượng thấp nhất không bằng không?

Hạt cổ điển có thể đứng yên đúng tại vị trí cân bằng và có năng lượng bằng không. Nhưng không có nghiệm dao động tử chuẩn hóa với $E=0$. Một trạng thái có cả vị trí lẫn động lượng xác định tuyệt đối cũng không phù hợp nguyên lý bất định.

Để thấy định lượng mối liên hệ, xét dao động Newton có cơ năng bằng $E_0=\hbar\omega/2$. Tại biên độ, toàn bộ cơ năng là thế năng. Tại cân bằng, toàn bộ là động năng. Do đó,

$$
\begin{aligned}
A&=\sqrt{\frac{\hbar}{m\omega}}\\
&=\frac{\hbar^{1/2}}{k'^{1/4}m^{1/4}}.
\end{aligned}
$$

$$
v_{\max}=\frac{\hbar^{1/2}k'^{1/4}}{m^{3/4}}.
$$

$$
p_{\max}=\hbar^{1/2}k'^{1/4}m^{1/4}.
$$

Với phân bố Gaussian lượng tử ở trạng thái cơ bản, các độ lệch chuẩn là

$$
\begin{aligned}
&\Delta x=\frac{A}{\sqrt2},\\
&\Delta p_x=\frac{p_{\max}}{\sqrt2}.
\end{aligned}
$$

Vì $Ap_{\max}=\hbar$, tích hai độ bất định bằng

$$
\Delta x\,\Delta p_x=\frac{\hbar}{2}.
$$

Trạng thái cơ bản đạt đúng giới hạn nhỏ nhất cho phép. Cần phân biệt $A$ và $p_{\max}$ của dao động cổ điển đối chiếu với các độ lệch chuẩn $\Delta x$ và $\Delta p_x$ của phân bố lượng tử.

### Khi thế năng thực không hoàn toàn là parabol

Thế năng tương tác giữa hai nguyên tử trong một phân tử hai nguyên tử có một cực tiểu tại khoảng cách cân bằng $r_0$. Khi hai nguyên tử ở rất xa nhau, đường thế năng dần phẳng, vì lực tương tác giảm về không.

![Hình 40.29: Thế năng U của phân tử hai nguyên tử và parabol xấp xỉ gần khoảng cách cân bằng r₀. Năng lượng cần để tách rời phân tử từ đáy giếng là U∞.](../img/young-40/hinh-40-29.png)

Gần cực tiểu, một parabol có thể xấp xỉ tốt đường thế năng thực. Dao động nhỏ của phân tử vì vậy gần dao động điều hòa, với các mức gần dạng (40.46). Khi dao động lớn, độ lệch khỏi parabol có ý nghĩa và không thể tiếp tục giả sử các mức luôn cách đều.

### Câu hỏi tự kiểm tra 40.5

Một hệ lượng tử ban đầu ở trạng thái cơ bản hấp thụ một photon để lên trạng thái kích thích thứ nhất. Nó tiếp tục hấp thụ photon thứ hai để lên trạng thái kích thích thứ hai. Với hệ nào sau đây, photon thứ hai có bước sóng lớn hơn photon thứ nhất?

1. Dao động tử điều hòa.
2. Nguyên tử hydrogen.
3. Hạt trong hộp.

<details><summary>Xem đáp án và giải thích</summary>

Chọn **2**.

Dao động tử có các khoảng cách mức bằng nhau, nên hai photon có cùng năng lượng và cùng bước sóng.

Với hydrogen, khoảng cách giữa các mức giảm khi số lượng tử tăng. Chuyển từ $n=2$ lên $n=3$ cần năng lượng nhỏ hơn chuyển từ $n=1$ lên $n=2$. Photon thứ hai vì thế có bước sóng dài hơn.

Với hạt trong hộp, $E_n$ tỉ lệ với $n^2$. Khoảng cách từ mức $n=2$ đến $n=3$ lớn hơn khoảng cách từ mức $n=1$ đến $n=2$. Photon thứ hai có bước sóng ngắn hơn.

</details>
