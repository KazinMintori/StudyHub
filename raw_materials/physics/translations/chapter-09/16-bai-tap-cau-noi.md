## Bài tập cầu nối: Thanh mảnh đồng chất quay (A Rotating, Uniform Thin Rod)

### Bài tập cầu nối

Hình 9.25 mô tả một thanh mảnh đồng chất có khối lượng $M$ và chiều dài $L$. Thanh có thể là một chiếc gậy biểu diễn của người chỉ huy đội diễu hành (bỏ qua các nắp bọc cao su ở hai đầu).
(a) Sử dụng phương pháp tích phân để tính mômen quán tính của thanh đối với trục quay đi qua điểm $O$, cách một đầu thanh một khoảng tùy ý $h$.
(b) Ban đầu thanh đứng yên. Người ta truyền cho thanh một gia tốc góc không đổi có độ lớn $\alpha$ quanh trục đi qua điểm $O$. Hãy xác định công thực hiện lên thanh trong khoảng thời gian $t$.
(c) Tại thời điểm $t$, gia tốc dài của điểm trên thanh nằm xa trục quay nhất bằng bao nhiêu?

![Hình 9.25: Thanh mảnh đồng chất quay quanh trục vuông góc đi qua điểm O.](./img/young-09/c-hinh-9-25.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Thanh mảnh đồng chất: Khối lượng $M$, chiều dài $L$.
- Trục quay vuông góc với thanh tại điểm $O$, cách một đầu thanh một khoảng $h$.
- Gia tốc góc không đổi: $\alpha$, bắt đầu quay từ trạng thái nghỉ tại $t = 0$.
- Cần tìm:
  - (a) Mômen quán tính $I$ của thanh đối với trục qua $O$ bằng tích phân.
  - (b) Công $W$ thực hiện lên thanh trong khoảng thời gian $t$.
  - (c) Độ lớn gia tốc dài $a$ của điểm trên thanh xa trục $O$ nhất tại thời điểm $t$.

**Hướng đi:**
- **Nhận diện và thiết lập mục tiêu**:
  1. Các đại lượng mục tiêu cần xác định gồm mômen quán tính $I$, công cơ học $W$ và gia tốc toàn phần $a$.
  2. Để tính mômen quán tính bằng giải tích, chia thanh thành các phần tử vi phân chiều dài $dx$ mang khối lượng $dm = \lambda dx = \frac{M}{L}dx$. Chọn gốc tọa độ tại $O$ dọc theo thanh, cận tích phân trải dài từ $-h$ đến $L - h$.
  3. Tại thời điểm $t$, thanh quay với tốc độ góc $\omega = \alpha t$. Công thực hiện để tăng tốc thanh từ trạng thái nghỉ bằng đúng động năng quay của thanh tại thời điểm đó: $W = \Delta K = \frac{1}{2}I\omega^2$.
  4. Điểm xa trục quay nhất có khoảng cách cực đại $r_{\max} = \max(h, L - h)$ (khi $h \le L/2$, điểm đó là đầu xa ở khoảng cách $L - h$). Điểm này đồng thời có gia tốc tiếp tuyến $a_{\mathrm{tan}} = r_{\max}\alpha$ do quay biến đổi đều và gia tốc hướng tâm $a_{\mathrm{rad}} = r_{\max}\omega^2$ do chuyển động trên quỹ đạo tròn.
- **Thực hiện giải toán**:
  5. Tính tích phân xác định để tìm biểu thức giải tích của mômen quán tính $I$.
  6. Sử dụng kết quả $I$ để tính công $W$ theo $\alpha$ và $t$.
  7. Xác định hai thành phần gia tốc tiếp tuyến và hướng tâm, từ đó tính độ lớn gia tốc toàn phần.
- **Đánh giá kết quả**:
  8. Kiểm tra các trường hợp giới hạn đặc biệt khi trục quay ở đầu thanh ($h = 0$) và khi trục quay đi qua chính giữa thanh ($h = L/2$). Đối chiếu trực tiếp với định lý trục song song.
  9. Phân tích sự phụ thuộc thời gian của độ lớn gia tốc dài.

**Lời giải chi tiết:**

#### Nhận diện và thiết lập (Identify and Set Up)

1. Thiết lập hệ trục tọa độ một chiều $Ox$ dọc theo chiều dài của thanh, với gốc tọa độ $O$ đặt tại vị trí trục quay. Chiều dương hướng về phía đoạn thanh dài hơn (đoạn có chiều dài $L - h$).
2. Vì thanh đồng chất và tiết diện không đổi, mật độ khối lượng dài là:
$$
\lambda = \frac{M}{L}
$$
Phần tử chiều dài $dx$ chứa khối lượng vi phân:
$$
dm = \lambda\,dx = \frac{M}{L}\,dx
$$
Trục quay $O$ nằm cách một đầu khoảng $h$, do đó tọa độ hai đầu mút của thanh lần lượt là $x = -h$ và $x = L - h$. Cận tích phân lấy từ $x_1 = -h$ đến $x_2 = L - h$.
3. Ban đầu thanh đứng yên ($\omega_0 = 0$). Với gia tốc góc không đổi $\alpha$, tốc độ góc của thanh tại thời điểm $t$ là:
$$
\omega(t) = \alpha t
$$
Theo định lý động năng cho vật rắn quay quanh trục cố định, toàn bộ công thực hiện lên thanh chuyển thành động năng quay:
$$
\begin{aligned}
W &= K_2 - K_1 \\
&= \frac{1}{2}I\omega^2 \\
&= \frac{1}{2}I(\alpha t)^2.
\end{aligned}
$$
4. Xét trường hợp hình học tổng quát với $h \le L/2$ như minh họa ở Hình 9.25, điểm nằm xa trục quay nhất chính là đầu mút bên phải của thanh, cách trục quay một khoảng:
$$
r_{\max} = L - h
$$
Tại thời điểm $t$, điểm này có:
- Gia tốc tiếp tuyến: $a_{\mathrm{tan}} = r_{\max}\alpha = (L - h)\alpha$, đặc trưng cho sự tăng nhanh của tốc độ dài.
- Gia tốc hướng tâm: $a_{\mathrm{rad}} = r_{\max}\omega^2 = (L - h)\omega^2$, đặc trưng cho sự uốn cong liên tục của vector vận tốc theo quỹ đạo tròn.

#### Thực hiện giải toán (Execute)

5. **Tính mômen quán tính bằng tích phân (Ý a)**:
Định nghĩa mômen quán tính của phân bố khối lượng liên tục:
$$
\begin{aligned}
I &= \int x^2\,dm \\
&= \frac{M}{L}\int_{-h}^{L-h} x^2\,dx.
\end{aligned}
$$

Tính nguyên hàm và thay cận tích phân:
$$
\begin{aligned}
I &= \frac{M}{L}\left[ \frac{x^3}{3} \right]_{-h}^{L-h} \\
&= \frac{M}{3L}\left[ (L - h)^3 + h^3 \right].
\end{aligned}
$$

Khai triển hằng đẳng thức lập phương $(L - h)^3$ rồi cộng với $h^3$, hai số hạng đối nhau $-h^3$ và $+h^3$ triệt tiêu, thu được thừa số chung $L(L^2 - 3Lh + 3h^2)$.
Thay vào biểu thức của $I$, thừa số $L$ ở tử số và mẫu số triệt tiêu:
$$
I = \frac{M}{3}(L^2 - 3Lh + 3h^2)
$$

6. **Tính công thực hiện lên thanh trong thời gian $t$ (Ý b)**:
Tại thời điểm $t$, tốc độ góc là $\omega = \alpha t$. Toàn bộ công thực hiện lên thanh chuyển thành động năng quay:
$$
\begin{aligned}
W &= \frac{1}{2}I\omega^2 \\
&= \frac{1}{2}I(\alpha t)^2.
\end{aligned}
$$
Kết hợp với mômen quán tính $I = \frac{M}{3}(L^2 - 3Lh + 3h^2)$ đã xác định ở Ý a, ta thu được công thực hiện lên thanh:
$$
W = \frac{1}{2}I\alpha^2 t^2
$$

7. **Xác định gia tốc dài của điểm xa trục nhất (Ý c)**:
Tại thời điểm $t$, tốc độ góc đạt $\omega=\alpha t$. Nếu $0\le h\le L/2$ như cách chọn đầu thanh trong hình, đầu xa trục có bán kính $L-h$. Với vị trí trục bất kỳ trong thanh, bán kính lớn nhất là:

$$
r_{\max}=\max\{h,L-h\}.
$$

Hai thành phần gia tốc vuông góc của điểm xa nhất là:
$$
\begin{aligned}
&a_{\mathrm{tan}} = r_{\max}\alpha, \\
&a_{\mathrm{rad}} = r_{\max}\alpha^2 t^2.
\end{aligned}
$$

Độ lớn gia tốc toàn phần bằng căn bậc hai tổng bình phương hai thành phần:
$$
a = \sqrt{a_{\mathrm{tan}}^2 + a_{\mathrm{rad}}^2}
$$
Đặt thừa số chung $r_{\max}\alpha$ ra ngoài dấu căn:
$$
a = r_{\max}\alpha\sqrt{1 + \alpha^2 t^4}.
$$

Trong cấu hình $h\le L/2$, thay $r_{\max}=L-h$ thu được:

$$
a=(L-h)\alpha\sqrt{1+\alpha^2t^4}.
$$

#### Đánh giá và thảo luận (Evaluate)

8. **Kiểm tra các trường hợp giới hạn đặc biệt**:
- Trường hợp $h = 0$ (trục quay đi qua một đầu mút của thanh):
$$
I = \frac{1}{3}ML^2
$$
Kết quả này trùng khớp hoàn hảo với công thức giải tích chuẩn của thanh mảnh quay quanh một đầu.
- Trường hợp $h = L/2$ (trục quay đi qua chính giữa thanh, tức khối tâm):
Với $h = L/2$, biểu thức trong ngoặc là $L^2 - \frac{3}{2}L^2 + \frac{3}{4}L^2 = \frac{1}{4}L^2$:
$$
\begin{aligned}
I &= \frac{M}{3}\left( \frac{1}{4}L^2 \right) \\
&= \frac{1}{12}ML^2.
\end{aligned}
$$
Kết quả này hoàn toàn thống nhất với mômen quán tính khối tâm của thanh mảnh.
- Kiểm tra đối chiếu bằng định lý trục song song:
Khoảng cách từ trục quay $O$ đến khối tâm $CM$ của thanh (tại $L/2$) là $d = |h - L/2|$. Theo định lý Steiner:
$$
\begin{aligned}
I &= I_{\mathrm{cm}} + Md^2 \\
&= \frac{1}{12}ML^2 + Md^2.
\end{aligned}
$$
Khai triển $d^2 = h^2 - Lh + \frac{1}{4}L^2$, cộng vào và quy đồng mẫu số chung 12:
$$
I = \frac{M}{3}(L^2 - 3Lh + 3h^2)
$$
Hai phương pháp tích phân trực tiếp và định lý trục song song cho kết quả hoàn toàn trùng khớp.

9. **Tính chất biến thiên của gia tốc toàn phần**:
Với $\alpha>0$ và $r_{\max}>0$, độ lớn gia tốc tăng theo thời gian. Thành phần tiếp tuyến $r_{\max}\alpha$ không đổi, còn thành phần hướng tâm $r_{\max}\alpha^2t^2$ tăng theo bình phương thời gian. Vì vậy, vectơ gia tốc toàn phần lệch dần về phương hướng tâm và tăng độ lớn.

</details>
