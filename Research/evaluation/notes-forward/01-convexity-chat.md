Đoạn này nói rằng với một hàm **khả vi và lồi**, thông tin về đạo hàm tại một điểm có thể giúp ta so sánh giá trị hàm tại điểm ấy với giá trị ở mọi điểm khác. Vì thế, khi gradient bằng 0, ta kết luận được điểm đó là cực tiểu toàn cục.

Bạn đã biết đạo hàm. Với hàm nhiều biến, gradient \(\nabla f(x)\) là vectơ gồm các đạo hàm riêng tại \(x\). Số hạng

\[
\nabla f(x)^T(y-x)=\sum_{i=1}^n\frac{\partial f}{\partial x_i}(x)(y_i-x_i)
\]

là tích vô hướng giữa gradient và độ dời từ \(x\) đến \(y\). Do đó, \(f(x)+\nabla f(x)^T(y-x)\) là giá trị của hàm affine mô tả tiếp tuyến tại \(x\). Khi \(n=1\), biểu thức này chính là \(f(x)+f'(x)(y-x)\).

Khả vi cho ta xấp xỉ tuyến tính gần \(x\). Tính lồi cho kết luận mạnh hơn: biểu thức tiếp tuyến ấy là một **cận dưới với mọi \(y\in\mathbb R^n\)**, kể cả khi \(y\) ở xa \(x\). Đây là ý nghĩa của bất đẳng thức đầu tiên trong đoạn.

Vì sao tính lồi cho cận dưới đó? Theo định nghĩa tính lồi, với \(0<t\leq1\), điểm \(x+t(y-x)\) trên đoạn nối \(x\) với \(y\) thỏa mãn

\[
f(x+t(y-x))\leq(1-t)f(x)+tf(y).
\]

Trừ \(f(x)\), rồi chia cho \(t>0\), ta được

\[
\frac{f(x+t(y-x))-f(x)}t\leq f(y)-f(x).
\]

Cho \(t\to0^+\). Vì \(f\) khả vi, vế trái tiến đến \(\nabla f(x)^T(y-x)\). Chuyển vế cho ta đúng bất đẳng thức trong đoạn trích. Tính lồi được dùng để so sánh các điểm trên đoạn nối; tính khả vi được dùng để chuyển giới hạn thành biểu thức gradient.

Bây giờ xét \(x=x^\star\). Bất đẳng thức đúng với mọi \(y\), nên

\[
f(y)\geq f(x^\star)+\underbrace{\nabla f(x^\star)^T(y-x^\star)}_{=0}
=f(x^\star).
\]

Không có điểm nào trong toàn bộ \(\mathbb R^n\) cho giá trị thấp hơn \(f(x^\star)\). Đó chính là nghĩa của **cực tiểu toàn cục**. Chữ “toàn cục” đến từ việc bất đẳng thức đúng với *mọi* \(y\), không chỉ những điểm gần \(x^\star\).

**Ví dụ bổ sung:** Với \(f(u)=u^2\), tiếp tuyến tại \(x=1\) có giá trị \(1+2(y-1)=2y-1\). Hiệu giữa hàm và tiếp tuyến là

\[
y^2-(2y-1)=(y-1)^2\geq0,
\]

nên tiếp tuyến nằm dưới đồ thị trên toàn trục số. Tại \(x^\star=0\), đạo hàm bằng 0 và bất đẳng thức trở thành \(y^2\geq0\): \(0\) là điểm cực tiểu toàn cục.

Điều kiện lồi không thể bị bỏ qua trong lập luận này. Ví dụ bổ sung \(g(u)=-u^2\) có \(g'(0)=0\), nhưng \(g(1)=-1<g(0)=0\). Như vậy, riêng việc đạo hàm bằng 0 chưa đủ để kết luận cực tiểu.

Tôi đã viết note độc lập trong [02-convexity-study-note.md](/C:/Users/Ai/Documents/StudyHub/Research/evaluation/notes-forward/02-convexity-study-note.md).
