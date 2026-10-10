---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: quy-hoach-phan-tuyen-tinh
section: topic
title: "Quy hoạch phân tuyến tính"
description: "Bài toán cực tiểu tỉ số của hai hàm affine trên đa diện, hình học của các tập mức là những tia quay quanh một điểm chung, phép đổi biến đưa bài toán về đúng một LP cùng chứng minh hai chiều và trường hợp z = 0, trực giác tỉ số trung bình và tỉ số biên, bài toán phân tuyến tính tổng quát và mô hình tăng trưởng von Neumann."
---

Nhiều quyết định được đánh giá bằng một tỉ số chứ không bằng một tổng: Lợi ích trên chi phí, sản lượng trên vốn, lợi nhuận trên rủi ro. Khi cả tử số lẫn mẫu số đều là hàm affine của biến quyết định, ta có một **quy hoạch phân tuyến tính** (linear-fractional program). Hàm mục tiêu không lồi, nên thoạt nhìn bài toán có vẻ khó hơn LP. [Chủ đề về hàm tựa lồi](./toi-uu-tua-loi.md) đã cho một cách giải bằng phương pháp chia đôi. Bài giảng này giới thiệu một phương pháp tối ưu hơn: Một phép đổi biến đại số đưa bài toán về đúng một LP duy nhất mà không cần giải lặp.

## 1. Bài toán

Quy hoạch phân tuyến tính có dạng

$$
\begin{aligned}
\text{minimize}\quad & f_0(x) = \frac{c^Tx + d}{e^Tx + f}\\
\text{subject to}\quad & Gx \preceq h,\quad Ax = b,
\end{aligned}
$$

với miền của hàm mục tiêu là $\{x : e^Tx + f > 0\}$. Như đã thấy ở chủ đề trước, hàm phân tuyến tính vừa tựa lồi vừa tựa lõm, nên bài toán là một bài toán tựa lồi, và bài toán cực đại một hàm phân tuyến tính cũng vậy.

Xét bài toán thực tế sau đây xuyên suốt bài giảng: Một xưởng sản xuất hai sản phẩm với sản lượng $x_1, x_2$. Mỗi đơn vị sản phẩm thứ nhất mang lại lợi ích 1 và tốn chi phí 1, mỗi đơn vị sản phẩm thứ hai mang lại lợi ích 2 và tốn chi phí 0.5, ngoài ra có một lợi ích cố định 2 và một chi phí cố định 1. Xưởng muốn cực đại **tỉ số lợi ích trên chi phí**

$$
f(x) = \frac{x_1 + 2x_2 + 2}{x_1 + 0.5x_2 + 1},
$$

với các ràng buộc: Ràng buộc yêu cầu sản xuất ít nhất một đơn vị sản phẩm thứ nhất, $x_1 \ge 1$, sản phẩm thứ hai không âm, tổng công suất $x_1 + x_2 \le 6$, và nguyên liệu cho sản phẩm thứ hai chỉ đủ $x_2 \le 4$. Miền khả thi là tứ giác có bốn đỉnh $(1, 0)$, $(6, 0)$, $(2, 4)$ và $(1, 4)$.

## 2. Hình học: Các tập mức quay quanh một điểm

Tập mức $\{x : f(x) = t\}$ trong miền xác định là tập các điểm thỏa $c^Tx + d = t(e^Tx + f)$, tức

$$
(c - te)^Tx + (d - tf) = 0, \qquad e^Tx + f > 0 .
$$

Phương trình thứ nhất là một siêu phẳng, nên mọi tập mức đều phẳng, đúng với tính tựa tuyến tính. Nhưng khác với LP, các siêu phẳng ấy không song song với nhau. Mọi điểm làm cả tử số lẫn mẫu số bằng 0 đều thỏa phương trình với mọi $t$. Trong mặt phẳng, tử số và mẫu số bằng 0 tại một điểm chung $P$, và mọi đường mức đều đi qua $P$. Tập mức thật sự chỉ là nửa đường thẳng nằm trong miền $e^Tx + f > 0$, tức một **tia xuất phát từ $P$**. Khi $t$ thay đổi, tia quay quanh $P$.

Với ví dụ của xưởng, tử số và mẫu số cùng bằng 0 tại $P = (-\tfrac23, -\tfrac23)$. Cực đại $f$ nghĩa là quay tia theo chiều làm $t$ tăng cho tới khi nó sắp rời khỏi miền khả thi, giống như đẩy đường mức trong LP, chỉ khác là xoay thay vì tịnh tiến.

<FractionalLab />

Hình ảnh này giải thích vì sao nghiệm vẫn nằm ở một đỉnh, như với LP. Các giá trị tại bốn đỉnh là $\tfrac32$, $\tfrac87$, $\tfrac{12}{5}$ và $\tfrac{11}{4}$. Vậy giá trị lớn nhất là $\tfrac{11}{4} = 2.75$ tại $(1, 4)$, và giá trị nhỏ nhất là $\tfrac87 \approx 1.143$ tại $(6, 0)$.

## 3. Trực giác: Tỉ số trung bình và tỉ số biên

Vì sao nghiệm lại là $(1, 4)$, làm ít sản phẩm thứ nhất nhất có thể và nhiều sản phẩm thứ hai nhất có thể? Hãy so sánh tỉ số hiện tại với **tỉ số biên** của một hướng thay đổi. Nếu tăng $x$ theo hướng $v$ với $e^Tv > 0$, thì $f$ tăng khi và chỉ khi

$$
\frac{c^Tv}{e^Tv} > f(x),
$$

vì đạo hàm của $f$ theo hướng $v$ cùng dấu với $c^Tv - f(x)\,e^Tv$. Tỉ số biên của sản phẩm thứ hai là $\tfrac{2}{0.5} = 4$, lớn hơn mọi giá trị của $f$ trên miền, nên thêm sản phẩm thứ hai luôn có lợi. Tỉ số biên của sản phẩm thứ nhất là $\tfrac11 = 1$, nhỏ hơn $f$ tại mọi điểm khả thi, nên bớt sản phẩm thứ nhất luôn có lợi. Quy tắc này quen thuộc với bất kỳ ai từng tính điểm trung bình: Thêm một môn học có điểm cao hơn điểm trung bình hiện tại sẽ kéo điểm trung bình lên, và ngược lại.

## 4. Đổi biến để được một LP

Giả sử tập $\{x : Gx \preceq h,\ Ax = b,\ e^Tx + f > 0\}$ khác rỗng. Đặt

$$
y = \frac{x}{e^Tx + f}, \qquad z = \frac{1}{e^Tx + f}.
$$

Ý tưởng là chia mọi thứ cho mẫu số, để mẫu số trở thành hằng số 1. Bài toán phân tuyến tính tương đương với LP

$$
\begin{aligned}
\text{minimize}\quad & c^Ty + dz\\
\text{subject to}\quad & Gy - hz \preceq 0,\\
& Ay - bz = 0,\\
& e^Ty + fz = 1,\\
& z \ge 0,
\end{aligned}
$$

với biến $(y, z)$. Lập luận tương đương cần hai chiều, và chiều thứ hai có một trường hợp đặc biệt.

**Từ bài toán gốc sang LP.** Nếu $x$ khả thi thì cặp $(y, z)$ định nghĩa như trên khả thi cho LP: Nhân $Gx \preceq h$ với $z > 0$ cho $Gy \preceq hz$, và $e^Ty + fz = z(e^Tx + f) = 1$. Hàm mục tiêu cũng bằng nhau, $c^Ty + dz = \tfrac{c^Tx + d}{e^Tx + f} = f_0(x)$. Vậy giá trị tối ưu của LP không lớn hơn giá trị tối ưu của bài toán gốc.

**Từ LP về bài toán gốc.** Nếu $(y, z)$ khả thi cho LP với $z > 0$, thì $x = y/z$ khả thi cho bài toán gốc với cùng giá trị mục tiêu. Nếu $z = 0$, ta không chia được, nhưng khi đó $Gy \preceq 0$ và $Ay = 0$, nên $y$ là một hướng đi được mãi trong miền khả thi. Lấy một điểm khả thi $x_0$, mọi điểm $x_0 + \tau y$ với $\tau \ge 0$ đều khả thi, và khi $\tau \to \infty$, giá trị $f_0(x_0 + \tau y)$ tiến tới $c^Ty$, chính là giá trị của $(y, 0)$ trong LP. Vậy dù $z = 0$, giá trị của LP vẫn được xấp xỉ tùy ý bởi các điểm khả thi của bài toán gốc. Hai chiều gộp lại cho thấy hai bài toán có cùng giá trị tối ưu.

Với ví dụ của xưởng, viết bài toán cực đại thành LP: Cực đại $y_1 + 2y_2 + 2z$ với $-y_1 + z \le 0$, $-y_2 \le 0$, $y_1 + y_2 - 6z \le 0$, $y_2 - 4z \le 0$, $y_1 + 0.5y_2 + z = 1$ và $z \ge 0$. Một bộ giải LP trả về $(y_1, y_2, z) = (0.25, 1, 0.25)$ với giá trị $2.75$, và ta lấy lại $x = y/z = (1, 4)$. Không cần chia đôi, không cần thử đỉnh.

## 5. Bài toán phân tuyến tính tổng quát

Một mở rộng tự nhiên là cực tiểu giá trị lớn nhất của nhiều tỉ số,

$$
f_0(x) = \max_{i = 1, \ldots, r} \frac{c_i^Tx + d_i}{e_i^Tx + f_i},
$$

trên miền mà mọi mẫu số đều dương. Giá trị lớn nhất của các hàm tựa lồi là tựa lồi, nên bài toán vẫn tựa lồi và giải được bằng chia đôi. Với mỗi mức $t$, bài toán khả thi gồm các bất đẳng thức tuyến tính $c_i^Tx + d_i \le t(e_i^Tx + f_i)$, nên mỗi bước chia đôi là một LP khả thi. Lần này phép đổi biến ở mục 4 không còn dùng được, vì mỗi tỉ số có một mẫu số riêng, và không thể chia cho tất cả cùng lúc.

Một mô hình kinh tế kinh điển thuộc dạng này là **bài toán tăng trưởng von Neumann (von Neumann growth model)**: Một nền kinh tế gồm $n$ ngành sản xuất, mức độ hoạt động hiện tại là $x \succ 0$ và ở giai đoạn tiếp theo là $x^+$. Ràng buộc công nghệ đòi hỏi lượng hàng hóa tiêu thụ không vượt quá sản lượng sản xuất trước đó, $Bx^+ \preceq Ax$. Tốc độ tăng trưởng của từng ngành $i$ được đo bằng tỉ số $x_i^+/x_i$, và mục tiêu là tối đa hóa tốc độ tăng trưởng của ngành kém nhất trong toàn nền kinh tế: $\max \min_{i} (x_i^+/x_i)$. Bài toán này tương đương với cực tiểu giá trị lớn nhất của các tỉ số đã đổi dấu $\max_{i} (-x_i^+/x_i)$, đúng dạng quy hoạch phân tuyến tính tổng quát. Cần chú ý rằng bài toán có tính thuần nhất theo $(x, x^+)$, nên điều kiện ẩn $x \succ 0$ có thể chuẩn hóa thành điều kiện tường minh $x \succeq \mathbf{1}$.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Trên một đa giác bị chặn, hàm lồi bất kỳ chắc chắn đạt giá trị lớn nhất tại một đỉnh, nhưng giá trị nhỏ nhất thì không. Với hàm phân tuyến tính, cả hai đều đạt tại đỉnh. Điều gì tạo ra sự khác biệt này?

<details><summary>Xem lời giải thích</summary>

Mọi điểm $x$ của đa giác là tổ hợp lồi của các đỉnh. Với hàm tựa lồi, dạng Jensen biến thể cho $f(x) \le \max_i f(v_i)$, nên giá trị lớn nhất đạt tại một đỉnh. Hàm lồi là tựa lồi, nên điều này đúng với hàm lồi. Hàm phân tuyến tính còn tựa lõm, nên áp dụng lập luận ấy cho $-f$ cũng được $f(x) \ge \min_i f(v_i)$, tức giá trị nhỏ nhất cũng đạt tại một đỉnh. Một hàm lồi thông thường không tựa lõm, nên giá trị nhỏ nhất của nó có thể nằm bên trong, như hàm $\|x\|_2^2$ trên một hình vuông chứa gốc.

</details>

**Câu 2.** Bỏ ràng buộc công suất $x_1 + x_2 \le 6$ trong ví dụ của xưởng, miền khả thi trở thành không bị chặn. Giá trị nhỏ nhất của $f$ khi đó là bao nhiêu, có đạt được không, và LP sau phép đổi biến phản ánh điều đó thế nào?

<details><summary>Xem lời giải thích</summary>

Ta có $f(x) - 1 = \tfrac{1.5x_2 + 1}{x_1 + 0.5x_2 + 1} > 0$ trên miền, nên $f > 1$ ở mọi điểm khả thi. Mặt khác, dọc tia $(x_1, 0)$ với $x_1 \to \infty$, $f \to 1$. Vậy giá trị nhỏ nhất là 1 nhưng không đạt. LP sau phép đổi biến cho nghiệm $(y_1, y_2, z) = (1, 0, 0)$ với giá trị 1. Thành phần $z = 0$ báo hiệu rằng nghiệm không ứng với một điểm $x$ hữu hạn nào, mà ứng với hướng $y = (1, 0)$, hướng tiến ra vô cực mà dọc theo nó $f$ tiến tới giá trị tối ưu. Đây đúng là trường hợp đặc biệt ở mục 4.

</details>

**Câu 3.** Phép đổi biến ở mục 4 có còn dùng được khi tử số là một hàm lồi không affine, chẳng hạn cực tiểu $\dfrac{\|x\|_2^2 + 1}{e^Tx + f}$?

<details><summary>Xem lời giải thích</summary>

Có, với một chút thay đổi. Với $y = x/(e^Tx + f)$ và $z = 1/(e^Tx + f)$, tử số chia cho mẫu số trở thành $z\,p(y/z)$, với $p(x) = \|x\|_2^2 + 1$. Biểu thức $z\,p(y/z)$ là [phép phối cảnh](../bai-01-nhap-mon-toi-uu/phep-toan-giu-tinh-loi-cua-ham.md) của $p$, một hàm lồi theo $(y, z)$ với $z > 0$. Vậy bài toán trở thành một bài toán lồi, không còn là LP nhưng vẫn giải trực tiếp được. Ở đây nó cho $\tfrac{\|y\|_2^2}{z} + z$, và đây là dạng tổng quát thường gọi là bài toán phân thức lồi–lõm (convex-concave fractional program).

</details>

**Câu 4.** Trong mô phỏng, đường mẫu số bằng 0 nằm ngoài miền khả thi. Nếu miền khả thi chạm vào đường đó thì sao?

<details><summary>Xem lời giải thích</summary>

Khi mẫu số tiến tới 0 từ phía dương trong khi tử số dương, tỉ số tăng không giới hạn. Bài toán cực đại khi đó không bị chặn trên, còn bài toán cực tiểu không bị ảnh hưởng nếu tử số giữ dương. Điểm mà mẫu số bằng 0 nằm ngoài miền của hàm mục tiêu, nên giả thiết chuẩn mực của bài toán luôn đòi hỏi tập khả thi phải nằm hoàn toàn trong nửa không gian $\{e^Tx + f > 0\}$. Trong thực tế, mô hình nên được thiết lập sao cho mẫu số bị chặn dưới bởi một số dương, chẳng hạn chi phí luôn có một phần cố định, như chi phí cố định 1 trong ví dụ của xưởng.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Đổi biến và giải
Cực tiểu $f(x) = \dfrac{x_1 + x_2 + 1}{2x_1 + x_2 + 1}$ trên hình vuông $[0, 1]^2$. Viết LP sau phép đổi biến, giải bằng cách so các đỉnh, rồi kiểm tra lại nghiệm của LP.
:::

::: solution
Với $y = x/(2x_1 + x_2 + 1)$ và $z = 1/(2x_1 + x_2 + 1)$, LP là cực tiểu $y_1 + y_2 + z$ với $0 \le y_1 \le z$, $0 \le y_2 \le z$, $2y_1 + y_2 + z = 1$, $z \ge 0$. Bốn đỉnh của hình vuông cho $f(0, 0) = 1$, $f(1, 0) = \tfrac23$, $f(0, 1) = 1$ và $f(1, 1) = \tfrac34$, nên nghiệm là $(1, 0)$ với giá trị $\tfrac23$. Tại đó mẫu số bằng 3, nên $(y_1, y_2, z) = (\tfrac13, 0, \tfrac13)$, và giá trị LP là $\tfrac13 + 0 + \tfrac13 = \tfrac23$, khớp.
:::

::: exercise 2. Nhiều tỉ số
Viết bài toán khả thi ở mỗi bước chia đôi cho bài toán cực tiểu $\max\left\{\dfrac{x_1 + 1}{x_2 + 1},\ \dfrac{x_2 + 1}{x_1 + 1}\right\}$ trên miền $x_1 + 2x_2 \ge 3$, $x \succeq 0$. Đoán nghiệm và giá trị tối ưu bằng tính đối xứng của hàm mục tiêu.
:::

::: solution
Với mức $t$, bài toán khả thi là tìm $x \succeq 0$ với $x_1 + 2x_2 \ge 3$, $x_1 + 1 \le t(x_2 + 1)$ và $x_2 + 1 \le t(x_1 + 1)$, toàn bất đẳng thức tuyến tính, nên là một LP khả thi. Hàm mục tiêu luôn lớn hơn hoặc bằng 1, vì một trong hai tỉ số là nghịch đảo của tỉ số kia, và bằng 1 khi và chỉ khi $x_1 = x_2$. Điểm $x_1 = x_2 = 1$ thỏa $x_1 + 2x_2 = 3 \ge 3$, nên giá trị tối ưu là 1, đạt trên cả tia $x_1 = x_2 \ge 1$.
:::

::: exercise 3. Lấy lại nghiệm
Một bộ giải trả về nghiệm $(y_1, y_2, z) = (0.2, 0.6, 0.4)$ cho LP sau phép đổi biến của một bài toán phân tuyến tính. Nghiệm của bài toán gốc là gì? Nếu bộ giải trả về $(0.5, 0, 0)$ thì sao?
:::

::: solution
Trường hợp thứ nhất có $z = 0.4 > 0$, nên $x^\star = y/z = (0.5, 1.5)$. Trường hợp thứ hai có $z = 0$: Không có nghiệm $x^\star$ hữu hạn nào đạt giá trị tối ưu. Giá trị tối ưu chỉ được tiệm cận tới khi tiến từ một điểm khả thi ra vô cực theo hướng tia $(0.5, 0)$, tức theo hướng trục $x_1$.
:::

## Tóm tắt

Quy hoạch phân tuyến tính cực tiểu hay cực đại một tỉ số của hai hàm affine trên một đa diện. Hàm mục tiêu không lồi nhưng tựa tuyến tính: Mỗi tập mức là một phần siêu phẳng, và trong mặt phẳng là một tia quay quanh điểm chung nơi tử và mẫu cùng bằng 0. Cả giá trị lớn nhất lẫn nhỏ nhất trên một đa diện bị chặn đều đạt tại đỉnh.

Phép đổi biến $y = x/(e^Tx + f)$, $z = 1/(e^Tx + f)$ chuẩn hóa mẫu số về 1 và biến bài toán thành đúng một LP. Từ nghiệm của LP, ta lấy lại $x = y/z$ khi $z > 0$. Khi $z = 0$, nghiệm của LP chỉ ra một tia tiến ra vô cực, và giá trị tối ưu của bài toán gốc không đạt tại điểm hữu hạn. Với giá trị lớn nhất của nhiều tỉ số, phép đổi biến không còn dùng được, nhưng phương pháp chia đôi vẫn giải được bằng một dãy LP khả thi.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
