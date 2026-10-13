## 29.7 Dòng điện dịch và phương trình Maxwell

Từ trường biến thiên sinh điện trường. Chiều ngược lại cũng đúng: điện trường biến thiên sinh từ trường. Mối liên hệ này giải thích sự tồn tại của sóng điện từ, bao gồm sóng radio, tia gamma, ánh sáng nhìn thấy và các dạng bức xạ khác.

### Mở rộng định luật Ampère

Định luật Ampère ở dạng đã học là:

$$
\oint\vec B\cdot d\vec\ell=\mu_0 I_{\mathrm{encl}}.
$$

Xét tụ điện đang nạp. Dòng dẫn tức thời $i_C$ đi vào một bản và ra khỏi bản kia, làm điện tích trên hai bản tăng. Điện trường $\vec E$ giữa hai bản vì thế cũng tăng. Ta dùng chữ thường $i$ và $v$ cho các đại lượng tức thời có thể biến thiên.

Chọn một đường tròn làm đường tích phân của định luật Ampère. Nếu mặt căng là mặt phẳng cắt dây dẫn, dòng bao bởi mặt bằng $i_C$. Nếu mặt căng phình qua khe giữa hai bản tụ, không có dòng dẫn nào xuyên qua mặt ấy. Cùng một đường tích phân vì vậy cho hai giá trị khác nhau của dòng bao, một mâu thuẫn của dạng Ampère cũ.

Để giải thích điều xảy ra giữa hai bản, xét tụ phẳng có diện tích bản $A$, khoảng cách $d$, điện dung $C$ và điện áp tức thời $v$. Bỏ qua hiệu ứng bờ và xem điện trường trong khe là đều. Trong chân không, $C=\varepsilon_0A/d$. Nếu khe tụ chứa vật liệu có điện thẩm $\varepsilon$, thay $\varepsilon_0$ bằng $\varepsilon$. Điện áp tức thời là $v=Ed$. Thay vào $q=Cv$, rồi dùng $\Phi_E=EA$:

$$
\begin{aligned}
&q = Cv\\
&\quad = \frac{\varepsilon A}{d}(Ed) \\
&\quad = \varepsilon EA=\varepsilon\Phi_E.
\end{aligned}
\tag{29.12}
$$

Tốc độ tăng điện tích chính là dòng dẫn $i_C=dq/dt$. Lấy đạo hàm (29.12) theo thời gian:

$$
\begin{aligned}
&i_C = \frac{dq}{dt} \\
&\quad =\varepsilon\frac{d\Phi_E}{dt}.
\end{aligned}
\tag{29.13}
$$

Nhà vật lý Scotland James Clerk Maxwell đưa khái niệm dòng dịch vào năm 1865. Đây là dòng điện tương đương dùng để tính hiệu ứng của điện trường biến thiên, chứ không phải dòng dẫn của điện tích qua khe tụ. Dòng dịch qua một diện tích được ký hiệu $i_D$:

$$
i_D=\varepsilon\frac{d\Phi_E}{dt}.
\tag{29.14}
$$

Thông lượng điện biến thiên trong khe tụ đóng vai trò tương đương một dòng điện trong định luật Ampère. Ta cộng dòng dịch với dòng dẫn để được:

$$
\begin{aligned}
&\oint\vec B\cdot d\vec\ell = \mu_0(i_C)_{\mathrm{encl}}\\
&\quad+\mu_0(i_D)_{\mathrm{encl}}.
\end{aligned}
\tag{29.15}
$$

Với mặt phẳng, $i_D=0$. Với mặt cong qua khe tụ, $i_C=0$, còn dòng dịch bằng dòng dẫn của mặt phẳng. Vì vậy cả hai mặt cho cùng giá trị tích phân. Trong vật liệu từ, dạng này còn dùng được khi độ từ hóa tỉ lệ với trường ngoài, miễn là thay $\mu_0$ bằng $\mu$.

Nếu điện trường đều trên diện tích $A$, mật độ dòng dịch là $j_D=i_D/A$. Vì $\Phi_E=EA$, suy ra:

$$
j_D=\varepsilon\frac{dE}{dt}.
\tag{29.16}
$$

Dòng dịch cũng mở rộng cách hiểu quy tắc nút Kirchhoff. Tại bản tụ, dòng dẫn đi vào bản nhưng không có dòng dẫn đi ra. Khi tính dòng dịch đi ra khỏi phía bên kia, dòng tổng quát vẫn liên tục, nên có thể nói dòng điện đi qua tụ.

![Hình29.22: Tụ đang nạp với hai mặt căng cùng đường biên, mặt phẳng cắt dòng dẫn còn mặt cong chứa dòng dịch](../img/young-29/hinh-29-22.png)

### Dòng dịch tạo từ trường

Dòng dịch có ý nghĩa vật lý hay chỉ là cách sửa công thức? Xét hai bản tụ tròn bán kính $R$ và một đường tròn đồng tâm bán kính $r<R$ nằm giữa hai bản. Mật độ dòng dịch bằng $i_D/(\pi R^2)$. Vì thế dòng dịch bị bao bởi đường tròn bán kính $r$ bằng mật độ ấy nhân diện tích $\pi r^2$. Tính đối xứng cho tích phân từ trường bằng $2\pi rB$, và khi tụ đang nạp thì $i_D=i_C$:

$$
\begin{aligned}
&2\pi rB = \mu_0\frac{r^2}{R^2}i_C,\\
&B = \frac{\mu_0}{2\pi}\frac{r}{R^2}i_C.\end{aligned}
\tag{29.17}
$$

Từ trường giữa hai bản bằng không trên trục và tăng tuyến tính theo khoảng cách $r$. Ở ngoài mép bản, trường giống trường do một dây dẫn liên tục tạo ra. Đo đạc xác nhận từ trường giữa hai bản có thật và phù hợp với dự đoán này. Dòng dịch vì thế thể hiện một nguồn từ trường thực.

![Hình29.23: Tụ tròn đang nạp với dòng dịch giữa hai bản và từ trường bao quanh trục](../img/young-29/hinh-29-23.png)

### Bốn phương trình Maxwell

Các phương trình dưới đây được nêu cho điện tích và dòng điện trong không gian trống. Trường hợp có điện môi hoặc vật liệu từ cần điều chỉnh thêm. Định luật Gauss cho điện trường:

$$
\oint\vec E\cdot d\vec A=\frac{Q_{\mathrm{encl}}}{\varepsilon_0}.
\tag{29.18}
$$

Định luật Gauss cho từ trường:

$$
\oint\vec B\cdot d\vec A=0.
\tag{29.19}
$$

Phương trình thứ hai biểu thị rằng không có đơn cực từ làm nguồn từ trường. Hai phương trình tích phân đường còn lại là định luật Faraday và định luật Ampère–Maxwell, trong đó đường tích phân được giữ cố định trong hệ quy chiếu khảo sát.

Định luật Faraday:

$$
\oint\vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt}.
\tag{29.20}
$$

Định luật Ampère–Maxwell:

$$
\begin{aligned}
&\oint\vec B\cdot d\vec\ell \\
&\quad =\mu_0(i_C)_{\mathrm{encl}}+\mu_0\varepsilon_0\left(\frac{d\Phi_E}{dt}\right)_{\mathrm{encl}}.
\end{aligned}
\tag{29.21}
$$

Điện trường tổng tại một điểm có thể gồm phần tĩnh $\vec E_c$ do các điện tích đứng yên và phần cảm ứng không tĩnh điện $\vec E_n$:

$$
\vec E=\vec E_c+\vec E_n.
$$

Phần tĩnh bảo toàn nên tích phân đường kín của nó bằng không. Vì vậy, trong Faraday có thể dùng điện trường tổng mà phần tĩnh không làm đổi kết quả. Tương tự, phần cảm ứng không góp vào thông lượng qua mặt kín trong định luật Gauss theo lập luận của chương. Các phương trình Maxwell dùng điện trường tổng, không cần tách riêng hai thành phần.

### Tính đối xứng và sóng điện từ

Trong không gian trống không có điện tích và dòng dẫn, hai phương trình Gauss cùng có thông lượng bằng không. Hai phương trình tích phân đường cũng có dạng đối xứng: từ trường biến thiên sinh điện trường, còn điện trường biến thiên sinh từ trường. Viết thông lượng tường minh, ta được:

$$
\begin{aligned}
    &\oint\vec E\cdot d\vec\ell = -\frac{d}{dt}\\
    &\qquad\left(\int\vec B\cdot d\vec A\right).\\
    &\oint\vec B\cdot d\vec\ell = \mu_0\varepsilon_0\frac{d}{dt}\\
    &\qquad\int\vec E\cdot d\vec A.
\end{aligned}
$$

Một trường biến thiên có thể sinh trường kia ở vùng lân cận. Hai trường biến thiên lan truyền qua không gian, kể cả nơi không có vật chất, tạo thành sóng điện từ. Ánh sáng, sóng radio và truyền hình, hồng ngoại, tử ngoại và tia X là các dạng sóng điện từ.

Từ phương trình Maxwell có thể suy ra định luật Coulomb từ định luật Gauss và định luật Biot–Savart từ định luật Ampère. Ghép thêm lực Lorentz tác dụng lên điện tích $q$ chuyển động với vận tốc $\vec v$:

$$
\vec F=q(\vec E+\vec v\times\vec B).
\tag{29.24}
$$

Như vậy, bộ Maxwell cùng lực Lorentz chứa các quan hệ cơ bản giữa trường điện từ, nguồn của trường và lực lên điện tích. Nếu có đơn cực từ, phương trình Gauss cho từ trường sẽ có điện tích từ ở vế phải và định luật Faraday sẽ có thêm dòng đơn cực từ. Hiện chưa tìm thấy đơn cực từ. Độ cô đọng và sức khái quát của tổng hợp Maxwell thường được đặt bên cạnh các định luật Newton và nhiệt động lực học, cũng như các tổng hợp lớn của vật lý hiện đại.

![Hình29.24: Bốn phương trình Maxwell trong không gian trống, thông lượng mặt kín bằng không và tích phân đường đối xứng của hai trường](../img/young-29/hinh-29-24.png)

### Tự kiểm 29.7

(a) Phương trình Maxwell nào giải thích hoạt động của đầu đọc thẻ tín dụng? (b) Phương trình nào mô tả từ trường do dây dẫn mang dòng không đổi tạo ra?

::: details Lời giải
(a) Định luật Faraday. Khi dải từ của thẻ quẹt qua đầu đọc, từ thông qua cuộn dây thay đổi và cảm ứng dòng. (b) Định luật Ampère–Maxwell, vì nó liên hệ từ trường với dòng dẫn và dòng dịch.
:::
