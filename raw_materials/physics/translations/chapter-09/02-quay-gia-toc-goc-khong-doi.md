## Chuyển động quay với gia tốc góc không đổi

Trong động học chuyển động thẳng, trường hợp chuyển động có gia tốc không đổi mang tính quy luật đặc biệt trực quan và đơn giản. Điều này cũng hoàn toàn đúng đối với chuyển động quay quanh một trục cố định. Khi gia tốc góc là một hằng số, chúng ta có thể thiết lập các phương trình mô tả vận tốc góc và vị trí góc theo cùng một phương pháp giải tích đã áp dụng cho chuyển động thẳng biến đổi đều.

Thực chất, các phương trình chúng ta sắp suy biến dưới đây hoàn toàn tương đồng về mặt toán học với các phương trình chuyển động thẳng nếu thay thế tọa độ $x$ bằng $\theta$, vận tốc $v_x$ bằng $\omega_z$, và gia tốc $a_x$ bằng $\alpha_z$.

### Thiết lập các phương trình động học góc

Xét một vật rắn quay quanh trục cố định với gia tốc góc $\alpha_z$ không đổi theo thời gian. Giả sử tại thời điểm ban đầu $t = 0$, vật có tọa độ góc ban đầu là $\theta_0$ và vận tốc góc ban đầu là $\omega_{0z}$. Tại thời điểm $t$ muộn hơn, vật đạt vận tốc góc $\omega_z$ và tọa độ góc $\theta$.

Vì gia tốc góc không đổi, giá trị tức thời $\alpha_z$ bằng giá trị trung bình trên khoảng thời gian từ $0$ đến $t$. Từ phương trình định nghĩa (9.4), ta có:
$$
\alpha_z = \frac{\omega_z - \omega_{0z}}{t - 0}
$$
suy ra phương trình vận tốc góc theo thời gian:
$$
\omega_z = \omega_{0z} + \alpha_z t
\tag{9.7}
$$

Trong phương trình (9.7), tích số $\alpha_z t$ đại diện cho độ biến thiên tổng cộng của vận tốc góc trong khoảng thời gian từ $0$ đến $t$.

Vì gia tốc góc $\alpha_z$ không đổi, vận tốc góc $\omega_z$ biến thiên tuyến tính theo thời gian. Do đó, vận tốc góc trung bình $\omega_{\text{av-}z}$ trong khoảng thời gian này đúng bằng trung bình cộng của vận tốc góc đầu và vận tốc góc cuối:
$$
\omega_{\text{av-}z} = \frac{\omega_{0z} + \omega_z}{2}
\tag{9.8}
$$

Mặt khác, theo định nghĩa chung, vận tốc góc trung bình bằng độ dời góc chia cho khoảng thời gian:
$$
\omega_{\text{av-}z} = \frac{\theta - \theta_0}{t - 0} = \frac{\theta - \theta_0}{t}
\tag{9.9}
$$

Đồng nhất hai vế của phương trình (9.8) và (9.9) rồi nhân cả hai vế với $t$, ta nhận được phương trình liên hệ giữa vị trí góc và vận tốc góc:
$$
\theta - \theta_0 = \frac{1}{2}(\omega_{0z} + \omega_z)t
\tag{9.10}
$$

Để nhận được hệ thức liên hệ trực tiếp giữa vị trí góc $\theta$ và thời gian $t$ mà không chứa biến số vận tốc góc $\omega_z$, chúng ta thay biểu thức $\omega_z = \omega_{0z} + \alpha_z t$ từ phương trình (9.7) vào phương trình (9.10):
$$
\begin{aligned}
\theta - \theta_0 &= \frac{2\omega_{0z} + \alpha_z t}{2}\,t \\
&= \omega_{0z}t + \frac{1}{2}\alpha_z t^2
\end{aligned}
$$
tức là:
$$
\theta = \theta_0 + \omega_{0z}t + \frac{1}{2}\alpha_z t^2
\tag{9.11}
$$

Phương trình (9.11) gồm ba phần. Đại lượng $\theta_0$ là vị trí góc tại thời điểm đầu $t=0$. Số hạng $\omega_{0z}t$ là góc quay nếu vận tốc góc giữ nguyên giá trị ban đầu. Số hạng $\frac{1}{2}\alpha_z t^2$ biểu thị phần góc quay tăng thêm hoặc giảm đi do gia tốc góc không đổi.

Bằng cách khử thời gian $t$ giữa phương trình (9.7) và (9.11), chúng ta tìm được hệ thức độc lập với thời gian: Rút thời gian $t = (\omega_z - \omega_{0z})/\alpha_z$ từ phương trình (9.7) rồi thay vào phương trình (9.10), thu được:
$$
2\alpha_z(\theta - \theta_0) = \omega_z^2 - \omega_{0z}^2
$$
suy ra hệ thức độc lập với thời gian:
$$
\omega_z^2 = \omega_{0z}^2 + 2\alpha_z(\theta - \theta_0)
\tag{9.12}
$$

::: warning Lưu ý: Điều kiện gia tốc góc không đổi
Cần luôn ghi nhớ rằng toàn bộ các phương trình (9.7), (9.10), (9.11) và (9.12) chỉ nghiệm đúng khi gia tốc góc $\alpha_z$ là hằng số. Tuyệt đối không được áp dụng các hệ thức này cho các bài toán mà gia tốc góc biến thiên theo thời gian.
:::

Bảng 9.1 tổng hợp sự tương đồng hoàn hảo giữa các phương trình chuyển động quay quanh trục cố định với gia tốc góc không đổi và các phương trình chuyển động thẳng với gia tốc dài không đổi.

*Bảng 9.1: So sánh chuyển động thẳng và chuyển động quay với gia tốc không đổi.*

<div class="lecture-data-table">

| Chuyển động thẳng với gia tốc dài không đổi | Chuyển động quay quanh trục cố định với gia tốc góc không đổi |
| --- | --- |
| <span class="table-cell-label">Chuyển động thẳng với gia tốc dài không đổi</span> $a_x = \text{hằng số}$ | <span class="table-cell-label">Chuyển động quay quanh trục cố định với gia tốc góc không đổi</span> $\alpha_z = \text{hằng số}$ |
| <span class="table-cell-label">Chuyển động thẳng với gia tốc dài không đổi</span> $v_x = v_{0x} + a_x t$ | <span class="table-cell-label">Chuyển động quay quanh trục cố định với gia tốc góc không đổi</span> $\omega_z = \omega_{0z} + \alpha_z t$ (9.7) |
| <span class="table-cell-label">Chuyển động thẳng với gia tốc dài không đổi</span> $x = x_0 + v_{0x}t + \frac{1}{2}a_x t^2$ | <span class="table-cell-label">Chuyển động quay quanh trục cố định với gia tốc góc không đổi</span> $\theta = \theta_0 + \omega_{0z}t + \frac{1}{2}\alpha_z t^2$ (9.11) |
| <span class="table-cell-label">Chuyển động thẳng với gia tốc dài không đổi</span> $v_x^2 = v_{0x}^2 + 2a_x(x - x_0)$ | <span class="table-cell-label">Chuyển động quay quanh trục cố định với gia tốc góc không đổi</span> $\omega_z^2 = \omega_{0z}^2 + 2\alpha_z(\theta - \theta_0)$ (9.12) |
| <span class="table-cell-label">Chuyển động thẳng với gia tốc dài không đổi</span> $x - x_0 = \frac{1}{2}(v_{0x} + v_x)t$ | <span class="table-cell-label">Chuyển động quay quanh trục cố định với gia tốc góc không đổi</span> $\theta - \theta_0 = \frac{1}{2}(\omega_{0z} + \omega_z)t$ (9.10) |

</div>

::: example Ví dụ 9.3: Chuyển động quay với gia tốc góc không đổi
**Bài toán**: Sau khi xem xong một bộ phim trên đĩa Blu-ray, đĩa đang quay chậm dần để dừng hẳn. Vận tốc góc của đĩa tại thời điểm $t = 0$ là $27{,}5\text{ rad/s}$ và gia tốc góc là một hằng số bằng $-10{,}0\text{ rad/s}^2$. Một đoạn thẳng $PQ$ vẽ trên mặt đĩa nằm dọc theo trục $+x$ tại thời điểm $t = 0$ (Hình 9.8).

![Hình 9.8: Đoạn thẳng PQ trên mặt đĩa Blu-ray quay tại thời điểm $t = 0$.](../img/young-09/a-hinh-9-08.png)

(a) Vận tốc góc của đĩa tại thời điểm $t = 0{,}300\text{ s}$ bằng bao nhiêu?

(b) Tại thời điểm này, đoạn thẳng $PQ$ hợp với trục $+x$ một góc bằng bao nhiêu?

**Tóm tắt**:
- Vận tốc góc ban đầu: $\omega_{0z} = 27{,}5\text{ rad/s}$.
- Gia tốc góc không đổi: $\alpha_z = -10{,}0\text{ rad/s}^2$.
- Vị trí góc ban đầu: $\theta_0 = 0$.
- Thời điểm khảo sát: $t = 0{,}300\text{ s}$.

**Hướng đi**:
- Vì gia tốc góc của đĩa là hằng số, chúng ta có thể áp dụng toàn bộ các phương trình trong Bảng 9.1.
- Ở câu (a), áp dụng phương trình (9.7) để tìm vận tốc góc $\omega_z$ tại thời điểm $t = 0{,}300\text{ s}$.
- Ở câu (b), áp dụng phương trình (9.11) để tìm tọa độ góc $\theta$, sau đó đổi phần góc dư sang đơn vị độ để xác định góc hợp với trục $+x$.

**Lời giải**:

(a) Từ phương trình (9.7), với $\omega_{0z} = 27{,}5\text{ rad/s}$ và $\alpha_z t = -3{,}00\text{ rad/s}$, tại thời điểm $t = 0{,}300\text{ s}$ ta có:
$$
\begin{aligned}
\omega_z &= \omega_{0z} + \alpha_z t \\
&= 24{,}5\text{ rad/s}
\end{aligned}
$$

(b) Từ phương trình (9.11), với $\theta_0 = 0$, $\omega_{0z}t = 8{,}25\text{ rad}$ và $\frac{1}{2}\alpha_z t^2 = -0{,}45\text{ rad}$, tọa độ góc của đoạn thẳng $PQ$ là:
$$
\begin{aligned}
\theta &= \theta_0 + \omega_{0z}t + \frac{1}{2}\alpha_z t^2 \\
&= 7{,}80\text{ rad}
\end{aligned}
$$

Đổi góc quay ra số vòng:
$$
\begin{aligned}
\theta &= \frac{7{,}80}{2\pi}\text{ rev} \\
&\approx 1{,}24\text{ rev}
\end{aligned}
$$

Như vậy, đĩa đã quay được 1 vòng trọn vẹn cộng thêm $0{,}24$ vòng. Góc quay thêm này tương ứng với:
$$
0{,}24\text{ rev} \cdot 360^\circ/\text{rev} \approx 87^\circ
$$
Do đó, đoạn thẳng $PQ$ hợp với chiều dương trục $x$ một góc $87^\circ$.

**Đánh giá**:
Kết quả ở câu (a) cho thấy vận tốc góc đã giảm từ $27{,}5\text{ rad/s}$ xuống $24{,}5\text{ rad/s}$, hoàn toàn phù hợp với thực tế chuyển động chậm dần vì $\alpha_z < 0$.

Chúng ta có thể kiểm tra chéo kết quả câu (b) bằng cách sử dụng phương trình (9.12):
$$
\omega_z^2 = \omega_{0z}^2 + 2\alpha_z(\theta - \theta_0)
$$
Giải phương trình này theo $\theta$:
$$
\begin{aligned}
\theta &= \theta_0 + \frac{\omega_z^2 - \omega_{0z}^2}{2\alpha_z} \\
&= \frac{24{,}5^2 - 27{,}5^2}{2(-10{,}0)}\text{ rad} \\
&= \frac{-156{,}0}{-20{,}0}\text{ rad} \\
&= 7{,}80\text{ rad}
\end{aligned}
$$
Kết quả hoàn toàn trùng khớp với cách tính trước đó.

**Trọng tâm tư duy**:
Các phương trình quay với gia tốc góc không đổi có cùng cấu trúc với các phương trình chuyển động thẳng có gia tốc không đổi. Phép tương ứng là thay $x$ bằng $\theta$, $v_x$ bằng $\omega_z$ và $a_x$ bằng $\alpha_z$.
:::

::: info Câu hỏi tự kiểm tra mục 9.2
Giả sử đĩa Blu-ray trong Ví dụ 9.3 ban đầu quay nhanh gấp đôi ($\omega_{0z} = 55{,}0\text{ rad/s}$ thay vì $27{,}5\text{ rad/s}$) và bị hãm với gia tốc góc có độ lớn gấp đôi ($\alpha_z = -20{,}0\text{ rad/s}^2$ thay vì $-10{,}0\text{ rad/s}^2$).

(a) So với tình huống trong Ví dụ 9.3, thời gian để đĩa dừng lại hoàn toàn sẽ như thế nào?
- (i) Bằng đúng khoảng thời gian cũ.
- (ii) Gấp đôi thời gian cũ.
- (iii) Gấp 4 lần thời gian cũ.
- (iv) Bằng một nửa thời gian cũ.
- (v) Bằng một phần tư thời gian cũ.

(b) So với tình huống trong Ví dụ 9.3, đĩa sẽ quay được bao nhiêu vòng trước khi dừng lại hẳn?
- (i) Cùng số vòng quay như cũ.
- (ii) Gấp đôi số vòng quay cũ.
- (iii) Gấp 4 lần số vòng quay cũ.
- (iv) Bằng một nửa số vòng quay cũ.
- (v) Bằng một phần tư số vòng quay cũ.

<details><summary>Xem lời giải thích</summary>

**Đáp án đúng**:
- **(a): (i)**.
- **(b): (ii)**.

Khi đĩa dừng hẳn, vận tốc góc triệt tiêu: $\omega_z = 0$.

Từ phương trình (9.7), thời gian hãm dừng là:
$$
t = \frac{\omega_z - \omega_{0z}}{\alpha_z} = -\frac{\omega_{0z}}{\alpha_z}
$$

Khi vận tốc góc ban đầu $\omega_{0z}$ tăng gấp đôi và gia tốc góc $\alpha_z$ cũng tăng độ lớn gấp đôi, tỉ số của chúng không đổi:
$$
\begin{aligned}
t_{\text{mới}} &= -\frac{2\omega_{0z}}{2\alpha_z} \\
&= -\frac{\omega_{0z}}{\alpha_z} = t_{\text{cũ}}
\end{aligned}
$$
Do đó thời gian hãm dừng hoàn toàn không đổi, tương ứng với phương án (a)(i).

Góc quay cho đến khi dừng lại được xác định từ phương trình (9.10) với $\omega_z = 0$:
$$
\begin{aligned}
\theta - \theta_0 &= \frac{1}{2}(\omega_{0z} + 0)t \\
&= \frac{1}{2}\omega_{0z}t
\end{aligned}
$$

Vì thời gian $t$ không đổi trong khi vận tốc góc ban đầu $\omega_{0z}$ tăng gấp đôi, góc quay $\theta - \theta_0$ (và do đó số vòng quay) sẽ tăng gấp đôi, tương ứng với phương án (b)(ii). Kết luận tương tự cũng thu được trực tiếp nếu sử dụng phương trình (9.12).

</details>
:::
