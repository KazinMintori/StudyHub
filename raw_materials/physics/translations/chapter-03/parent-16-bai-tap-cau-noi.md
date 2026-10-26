### Bài tập cầu nối: Phóng bóng lên một mặt dốc

Một quả bóng được phóng với tốc độ ban đầu $v_0$ theo góc $\phi$ phía trên mặt dốc. Mặt dốc nghiêng góc $\theta$ so với phương ngang như Hình 3.37. Bỏ qua sức cản không khí.

(a) Tìm khoảng cách đo dọc mặt dốc từ điểm phóng đến điểm bóng chạm dốc.

(b) Góc $\phi$ nào làm khoảng cách ấy lớn nhất?

![Hình 3.37: Bóng được phóng với góc phi so với mặt dốc, còn mặt dốc hợp phương ngang góc theta.](/vat-ly-1/bai-giang/img/young-03/r-exercises-figure-3-37.png)

#### Các bước hướng dẫn

1. Vì sao có thể dùng mô hình chuyển động ném khi không có sức cản? Mục tiêu là tìm giao điểm nào giữa quỹ đạo parabol và mặt dốc?
2. Chọn các trục $x$, $y$ và gốc tọa độ. Nếu chưa rõ cách chọn, vận dụng cách đặt trục trong chuyển động ném ở Mục 3.3.
3. Trong phương trình ném xiên, góc phóng được đo từ phương ngang. Góc ấy liên hệ thế nào với $\theta$ và $\phi$? Các thành phần vận tốc ban đầu bằng bao nhiêu?
4. Viết phương trình liên hệ $x$ và $y$ của các điểm trên mặt dốc. Đây là bước hình học và lượng giác.
5. Viết tọa độ $x$ và $y$ của bóng theo thời gian $t$.
6. Khi bóng chạm dốc, tọa độ thỏa phương trình ở bước 4. Từ điều kiện ấy, bóng chạm dốc lúc nào sau khi phóng?
7. Dùng kết quả bước 6 để tìm tọa độ điểm rơi. Khoảng cách từ điểm phóng tới đó, đo dọc mặt dốc, bằng bao nhiêu?
8. Dùng phép tính vi phân để tìm góc $\phi$ làm khoảng cách từ điểm phóng tới điểm rơi lớn nhất.
9. Xét lại các kết quả khi $\theta=0$, tức mặt dốc trở thành mặt phẳng ngang. Chúng có khớp kết quả đã biết không? Vì sao phải khớp?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Giữ $v_0>0$, $g>0$ và xét mặt dốc lên về phía trước như hình. Miền góc là

$$
0\le\theta<90^\circ,
$$

$$
0<\phi<90^\circ-\theta.
$$

Miền này bảo đảm bóng được phóng phía trên mặt dốc và có thành phần vận tốc ngang hướng về phía trên dốc. Giả sử mặt dốc đủ dài và trọng trường đều. Khoảng cách cần cực đại được đo trên mặt dốc, không phải theo phương ngang.

**Hướng đi:**

- Dùng trục ngang và trục đứng để gia tốc chỉ xuất hiện trong phương trình đứng. Độ nghiêng của dốc được đưa vào phương trình hình học.
- Tìm nghiệm thời gian chạm dốc khác không. Nghiệm bằng không chỉ là điểm phóng, chưa phải lần rơi trở lại.
- Đổi tọa độ ngang thành độ dài trên dốc trước khi tối ưu. Khi lấy đạo hàm, giữ tốc độ phóng và góc nghiêng dốc cố định.

**Lời giải:**

#### 1. Xác định chuyển động cần xét

Bóng chỉ chịu gia tốc trọng trường không đổi, nên quỹ đạo trong hệ gắn với đất là parabol. Điểm cần tìm là giao điểm thứ hai của parabol với đường thẳng biểu diễn mặt dốc. Giao điểm thứ nhất là điểm phóng.

#### 2. Chọn hệ tọa độ

Đặt gốc tại điểm phóng, chiều $x$ dương nằm ngang về phía dốc lên và chiều $y$ dương hướng thẳng đứng lên. Khi đó

$$
a_x=0,\qquad a_y=-g.
$$

Mặt dốc nghiêng nhưng trục đứng vẫn theo phương trọng lực. Vì thế không cần phân tích trọng lực theo mặt dốc trong cách giải này.

#### 3. Đổi góc phóng và tách vận tốc

Gọi góc phóng so với phương ngang là $\alpha$. Hai góc trong hình cho

$$
\alpha=\theta+\phi.
$$

Các thành phần ban đầu là

$$
v_{0x}=v_0\cos\alpha,
$$

$$
v_{0y}=v_0\sin\alpha.
$$

Không dùng $\phi$ thay cho $\alpha$ trong các thành phần theo trục ngang và đứng, vì $\phi$ được đo từ mặt dốc.

#### 4. Viết phương trình mặt dốc

Đường thẳng đi qua gốc và nghiêng góc $\theta$ so với trục ngang có phương trình

$$
y=x\tan\theta.
$$

Trong miền góc đã chọn, điểm rơi phía trên dốc có $x>0$ và độ dài dọc dốc bằng $x/\cos\theta$.

#### 5. Viết tọa độ theo thời gian

Với tọa độ ban đầu bằng không,

$$
x(t)=v_0\cos\alpha\,t,
$$

$$
y(t)=v_0\sin\alpha\,t-\frac12gt^2.
$$

Hai phương trình dùng cùng một thời gian, vì chúng mô tả hai thành phần của cùng chuyển động.

#### 6. Tìm thời điểm chạm dốc

Thay hai tọa độ vào điều kiện mặt dốc. Để giữ phép biến đổi gọn, đặt

$$
B=\sin\alpha-\cos\alpha\tan\theta.
$$

Điều kiện giao điểm trở thành

$$
0=v_0Bt-\frac12gt^2.
$$

Ngoài nghiệm $t=0$, nghiệm dương là $t_f=2v_0B/g$. Dùng công thức hiệu hai góc,

$$
\begin{aligned}
B&=\frac{\sin(\alpha-\theta)}{\cos\theta}\\
&=\frac{\sin\phi}{\cos\theta}.
\end{aligned}
$$

Vì thế

$$
t_f=\frac{2v_0\sin\phi}{g\cos\theta}.
$$

Giá trị này dương trong miền góc đã chọn. Bóng có độ cao trên mặt dốc dương giữa hai nghiệm, nên nghiệm này là lần đầu bóng trở lại mặt dốc sau khi phóng.

#### 7. Tìm điểm rơi và tầm xa trên dốc

Tọa độ điểm rơi được xác định bởi

$$
x_f=v_0\cos\alpha\,t_f,
$$

$$
y_f=x_f\tan\theta.
$$

Gọi $R$ là khoảng cách dọc mặt dốc. Từ hình học,

$$
R=\frac{x_f}{\cos\theta}.
$$

Thay thời gian và góc phóng cho kết quả phần (a),

$$
R=\frac{2v_0^2\cos(\theta+\phi)\sin\phi}{g\cos^2\theta}.
$$

Tọa độ ngang chỉ bằng $R\cos\theta$. Nhầm hai độ dài ấy sẽ làm mất một thừa số $\cos\theta$ trong mẫu.

#### 8. Tìm góc cho tầm xa lớn nhất

Với $\theta$ cố định, đặt hệ số dương

$$
K=\frac{2v_0^2}{g\cos^2\theta}.
$$

Khi đó $R=K\cos(\theta+\phi)\sin\phi$. Dùng công thức tích thành tổng, đặt

$$
F(\phi)=\frac{2R}K.
$$

Ta được

$$
F(\phi)=\sin(\theta+2\phi)-\sin\theta.
$$

Lấy đạo hàm theo góc tính bằng radian,

$$
F'(\phi)=2\cos(\theta+2\phi).
$$

Trong miền góc đang xét, điểm dừng duy nhất thỏa

$$
\theta+2\phi=90^\circ.
$$

Do đó kết quả phần (b) là

$$
\phi_{\mathrm{opt}}=45^\circ-\frac\theta2.
$$

Góc này nằm bên trong miền cho phép. Tại đó, đạo hàm bậc hai của $F$ bằng $-4<0$. Khi $\phi$ tiến tới hai đầu miền cho phép, $R$ đều tiến về không. Vì vậy đây là cực đại toàn miền, không chỉ là một nghiệm của phương trình đạo hàm.

Tầm xa lớn nhất có thể rút gọn thành

$$
R_{\max}=\frac{v_0^2}{g(1+\sin\theta)}.
$$

Góc so với phương ngang khi tối ưu là $45^\circ+\theta/2$, lớn hơn $45^\circ$ khi dốc nghiêng lên, dù góc đo từ mặt dốc lại nhỏ hơn $45^\circ$.

#### 9. Kiểm tra trường hợp mặt phẳng ngang

Với $\theta=0$, góc đo từ mặt dốc chính là góc đo từ phương ngang. Công thức tầm xa trở thành

$$
R=\frac{v_0^2\sin2\phi}g.
$$

Góc tối ưu là $45^\circ$ và tầm xa lớn nhất là $v_0^2/g$. Đây là kết quả ném xiên khi điểm rơi cùng độ cao điểm phóng, đúng với hình học của giới hạn mặt dốc ngang.

</details>
