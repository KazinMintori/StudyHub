---
course: toan-cho-ai
lecture: on-luyen
topic: quy-hoach-tuyen-tinh
section: topic
title: "Quy hoạch tuyến tính và phân loại bài toán"
description: "LP tổng quát, nửa không gian, đường mức, hai ví dụ giải bằng đỉnh và phân biệt tuyến tính, lồi, phi lồi."
---

Một mục tiêu tuyến tính không có điểm trũng trong không gian đầy đủ. Tuy vậy, khi đặt nó trên một miền bị giới hạn, ta có thể tìm được điểm tốt nhất. Hai ví dụ dưới đây cho thấy chính hình học của ràng buộc quyết định vị trí nghiệm.

## 1. Dạng tổng quát của LP

Quy hoạch tuyến tính có mục tiêu tuyến tính và các ràng buộc affine. Dạng bất đẳng thức là

$$
\begin{aligned}
&\min_x c^Tx,\\
&Ax\le b.
\end{aligned}
$$

Mục tiêu và từng hàng ràng buộc được khai triển thành

$$
\begin{aligned}
c^Tx &= c_1x_1+\cdots+c_nx_n, \\
(Ax)_i &= a_{i1}x_1+\cdots+a_{in}x_n \le b_i,\quad i=1,\ldots,m.
\end{aligned}
$$

Trong hai chiều, $ax+by=c$ là đường thẳng có pháp tuyến $(a,b)$ khi $(a,b)\ne(0,0)$. Bất đẳng thức $ax+by\le c$ chọn một phía của đường này. Muốn xác định phía nào, thử một điểm không nằm trên đường. Hướng pháp tuyến làm $ax+by$ tăng, nên phía thỏa dấu $\le$ nằm theo hướng ngược lại.

## 2. Ví dụ trên miền tam giác

Xét bài min $x-y$ trên miền $D$ xác định bởi

$$
\begin{aligned}
x+y &\le 1, \\
-x &\le 0, \\
-y &\le 0.
\end{aligned}
$$

Miền $D$ là tam giác có ba đỉnh $O=(0,0)$, $A=(1,0)$ và $B=(0,1)$. Các đường mức $x-y=c$ song song, có pháp tuyến $(1,-1)$. Trượt đường mức theo chiều làm $c$ giảm, đường cuối cùng còn chạm miền đi qua $B$.

| Đỉnh | Giá trị $x-y$ |
| --- | --- |
| $(0,0)$ | $0$ |
| $(1,0)$ | $1$ |
| $(0,1)$ | $-1$ |

Có thể chứng minh mà không cần hình. Từ $y\le1-x$ và $x\ge0$,

$$
\begin{aligned}
x-y &\ge x-(1-x) \\
&= 2x-1 \\
&\ge -1.
\end{aligned}
$$

Điểm $(0,1)$ khả thi và đạt $-1$, nên đó là nghiệm tối ưu duy nhất. Cách dùng cận dưới rồi tìm điểm đạt cận sẽ xuất hiện trở lại trong đối ngẫu.

## 3. Ví dụ trên miền năm đỉnh

Xét bài toán

$$
\begin{aligned}
&\min_{x,y}(-3x-2y),\\
&x+y\le6,\\
&0\le x\le4,\quad0\le y\le3.
\end{aligned}
$$

Hình chữ nhật $[0,4]\times[0,3]$ bị đường $x+y=6$ cắt góc trên bên phải. Miền còn lại có năm đỉnh. Khi xét LP trên một đa giác bị chặn, luôn có ít nhất một đỉnh đạt tối ưu, nên tính đủ năm giá trị:

| Đỉnh | $-3x-2y$ |
| --- | --- |
| $(0,0)$ | $0$ |
| $(4,0)$ | $-12$ |
| $(4,2)$ | $-16$ |
| $(3,3)$ | $-15$ |
| $(0,3)$ | $-6$ |

Vậy giá trị tối ưu là $-16$ tại $(4,2)$. Một chứng nhận ngắn là

$$
\begin{aligned}
3x+2y &= x+2(x+y) \\
&\le 4+2\cdot6 \\
&= 16.
\end{aligned}
$$

Đẳng thức đòi hỏi đồng thời $x=4$ và $x+y=6$, nên nghiệm duy nhất là $(4,2)$. Ta đã phối hợp hai ràng buộc bằng các hệ số không âm để tạo một cận cho mục tiêu.

<MathLab type="lp" />

Mô phỏng trên dùng một đa diện khác để quan sát khi đổi hướng mục tiêu. Một cạnh có thể chứa nhiều nghiệm tối ưu nếu đường mức song song với cạnh ấy. Vì thế kết luận “có một đỉnh tối ưu” không có nghĩa “mọi nghiệm tối ưu đều là đỉnh”.

## 4. Quy hoạch lồi và bài toán phi lồi

Hàm $g$ trên miền lồi là hàm lồi nếu, với mọi $x,y$ trong miền và $t\in[0,1]$,

$$
g(tx+(1-t)y) \le tg(x) + (1-t)g(y).
$$

Điểm $tx+(1-t)y$ chạy trên đoạn nối hai đầu mút. Bất đẳng thức nói đồ thị không cao hơn dây cung.

Nếu $f$ và các $f_i$ đều lồi, thì bài min $f(x)$ dưới các ràng buộc $f_i(x)\le b_i$ là bài toán lồi. Nếu có thêm đẳng thức, dạng chuẩn yêu cầu chúng affine. LP là một trường hợp của quy hoạch lồi.

**Phi tuyến không đồng nghĩa phi lồi.** Bình phương tối thiểu có mục tiêu bậc hai nhưng vẫn lồi. Một bài không thỏa các điều kiện lồi của dạng biểu diễn hiện tại có thể thật sự phi lồi, hoặc có thể cần đổi biến để nhận ra một biểu diễn lồi tương đương. Phải kiểm cấu trúc trước khi phân loại.

## 5. Bài tập tự luyện

::: exercise Đọc chứng nhận cận dưới
Trong bài năm đỉnh, nếu bỏ ràng buộc $x\le4$ nhưng giữ các ràng buộc khác, chứng nhận cũ còn dùng được không? Hãy tìm nghiệm mới.
:::

::: solution
Không còn được dùng bước $x\le4$. Từ $3x+2y=3(x+y)-y$, ta được $3x+2y\le18$ vì $x+y\le6$ và $y\ge0$. Điểm $(6,0)$ khả thi, đạt cận 18. Vì vậy bài min đạt $-18$ tại $(6,0)$.
:::

Nền tảng hình học được trình bày kỹ hơn ở [tập lồi, hàm lồi và nghiệm tối ưu](./tinh-loi-va-toi-uu.md).


