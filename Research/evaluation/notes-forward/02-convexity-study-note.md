# Hàm lồi khả vi và cực tiểu toàn cục

Nguồn: đoạn thử nghiệm tự viết do người học cung cấp. Các chứng minh và ví dụ dưới đây là phần giải thích bổ sung. Note dành cho người đã biết đạo hàm.

## Phát biểu và ký hiệu

Giả sử \(f:\mathbb R^n\to\mathbb R\) khả vi và lồi. Khi đó, với mọi \(x,y\in\mathbb R^n\),

\[
f(y)\geq f(x)+\nabla f(x)^T(y-x).
\tag{1}
\]

Gradient \(\nabla f(x)\) là vectơ các đạo hàm riêng của \(f\) tại \(x\). Dấu \(T\) chỉ phép chuyển vị; biểu thức \(\nabla f(x)^T(y-x)\) là tích vô hướng, có giá trị bằng

\[
\sum_{i=1}^n\frac{\partial f}{\partial x_i}(x)(y_i-x_i).
\]

Một điểm \(x^\star\) là **điểm cực tiểu toàn cục** nếu \(f(y)\geq f(x^\star)\) với mọi \(y\in\mathbb R^n\). Trong các giả thiết trên, nếu \(\nabla f(x^\star)=0\), thì \(x^\star\) là điểm cực tiểu toàn cục.

## Vì sao tiếp tuyến cho cận dưới trên toàn miền?

Hàm affine

\[
L_x(y)=f(x)+\nabla f(x)^T(y-x)
\]

mô tả tiếp tuyến tại \(x\). Khả vi cho phép dùng \(L_x\) để xấp xỉ \(f\) gần \(x\). Bất đẳng thức (1) nói thêm rằng \(L_x(y)\) không vượt quá \(f(y)\) ở bất kỳ điểm \(y\) nào. Kết luận về cận dưới trên toàn miền cần tính lồi.

Để chứng minh (1), cố định hai điểm bất kỳ \(x,y\). Tính lồi có nghĩa là, với \(t\in[0,1]\),

\[
f((1-t)x+ty)\leq(1-t)f(x)+tf(y).
\]

Vì \((1-t)x+ty=x+t(y-x)\), với \(t>0\) ta trừ \(f(x)\) và chia cho \(t\) mà không đổi chiều bất đẳng thức:

\[
\frac{f(x+t(y-x))-f(x)}t\leq f(y)-f(x).
\]

Khả vi tại \(x\) cho

\[
\lim_{t\to0^+}\frac{f(x+t(y-x))-f(x)}t
=\nabla f(x)^T(y-x).
\]

Lấy giới hạn rồi chuyển vế thu được (1). Hai điểm đã được chọn tùy ý, nên kết quả đúng với mọi \(x,y\in\mathbb R^n\).

## Vì sao gradient bằng 0 đủ để kết luận cực tiểu?

Chiến lược là so sánh \(f(x^\star)\) với giá trị hàm ở một điểm \(y\) tùy ý. Áp dụng (1) tại \(x=x^\star\):

\[
f(y)\geq f(x^\star)+\nabla f(x^\star)^T(y-x^\star).
\]

Điều kiện \(\nabla f(x^\star)=0\) triệt tiêu số hạng tuyến tính. Do đó,

\[
f(y)\geq f(x^\star)\qquad\text{với mọi }y\in\mathbb R^n.
\]

Đây là đúng định nghĩa cực tiểu toàn cục. Tính lồi cho phép có bất đẳng thức so sánh với mọi điểm; gradient bằng 0 làm cận dưới bằng chính \(f(x^\star)\).

## Ví dụ bổ sung có hai biến

Xét \(f(u,v)=u^2+v^2\), một hàm khả vi và lồi trên \(\mathbb R^2\). Để kiểm tra tính lồi trực tiếp, đặt \(a,b\in\mathbb R^2\). Với \(t\in[0,1]\),

\[
(1-t)\|a\|^2+t\|b\|^2-\|(1-t)a+tb\|^2
=t(1-t)\|a-b\|^2\geq0,
\]

nên hàm bình phương độ dài thỏa định nghĩa tính lồi.

Gradient của \(f\) là \(\nabla f(u,v)=(2u,2v)^T\). Tại \(x=(1,0)^T\), với \(y=(p,q)^T\), cận dưới tiếp tuyến là

\[
f(x)+\nabla f(x)^T(y-x)=1+2(p-1)=2p-1.
\]

Hiệu giữa giá trị hàm và cận dưới bằng

\[
p^2+q^2-(2p-1)=(p-1)^2+q^2\geq0.
\]

Phép tính cho thấy cận dưới đúng với mọi \(p,q\). Tại \(x^\star=(0,0)^T\), gradient bằng 0; khi đó cận dưới là 0, và \(p^2+q^2\geq0=f(x^\star)\). Vì thế \(x^\star\) là điểm cực tiểu toàn cục.

## Giới hạn của kết luận

Nếu bỏ tính lồi, gradient bằng 0 có thể không cho cực tiểu. Ví dụ bổ sung \(g(u)=-u^2\) có \(g'(0)=0\), nhưng \(g(1)=-1<g(0)=0\). Đây là phản ví dụ cho việc chỉ dùng điều kiện điểm dừng.

Phát biểu không bảo đảm rằng một điểm có gradient bằng 0 luôn tồn tại. Chẳng hạn, hàm lồi khả vi \(h(u)=u\) không có điểm như vậy và không có cực tiểu trên \(\mathbb R\).

Phát biểu cũng không bảo đảm cực tiểu là duy nhất. Hàm hằng \(k(u)=0\) thỏa các giả thiết và có gradient bằng 0 ở mọi điểm; mọi điểm đều là cực tiểu toàn cục.
