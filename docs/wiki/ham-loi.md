---
title: "Hàm lồi"
wikiTerm: ham-loi
prev: false
next: false
---

# Hàm lồi

Giả sử ta trộn hai phương án sản xuất. Nếu chi phí tại phương án trộn không vượt trung bình có trọng số của hai chi phí ban đầu, hàm chi phí có thể mang **tính lồi**. Tính chất này phải đúng trên toàn miền lồi đang xét.

<WikiUsage />

![Hình 1: Dây cung nằm phía trên đồ thị của hàm lồi.](./img/atlas/convex.svg)

## Giải thích kỹ thuật

Với $x,y$ trong miền lồi và $\theta\in[0,1]$, đặt $z=\theta x+(1-\theta)y$. Hàm $f$ là lồi khi:

$$
f(z)\le\theta f(x)+(1-\theta)f(y).
$$

Hình học của điều kiện này là đồ thị nằm không cao hơn dây cung nối hai điểm trên đồ thị. Nếu bất đẳng thức nghiêm với mọi hai điểm phân biệt và $0<\theta<1$, hàm là lồi nghiêm.

Với hàm khả vi trên miền mở lồi, một điều kiện tương đương là mặt phẳng tiếp tuyến luôn nằm dưới đồ thị:

$$
f(y)\ge f(x)+\nabla f(x)^T(y-x).
$$

Với hàm có đạo hàm bậc hai liên tục, tính lồi tương đương Hessian nửa xác định dương ở mọi điểm. Điều kiện này không chỉ nói Hessian có các phần tử dương.

Trong bài toán cực tiểu hàm lồi trên miền khả thi lồi, mọi cực tiểu địa phương là cực tiểu toàn cục. Tuy nhiên, nghiệm chưa chắc tồn tại. Hàm $e^x$ trên toàn trục số có cận dưới 0 nhưng không đạt giá trị đó.

## Ví dụ có lời giải

Lấy $f(x)=x^2$, hai điểm $x=-1$, $y=2$ và $\theta=1/2$. Trung điểm là $z=1/2$. Khi đó:

$$
\begin{aligned}
f(z)&=1/4,\\
\tfrac12f(x)+\tfrac12f(y)&=5/2.
\end{aligned}
$$

Đồ thị tại trung điểm nằm dưới dây cung. Để chứng minh cho mọi cặp, dùng đạo hàm bậc hai $f''(x)=2>0$, không dựa riêng vào ví dụ số này.

Một hàm tuyến tính vừa lồi vừa lõm. Lồi không có nghĩa đồ thị phải cong hoặc phải có đúng một đáy.

## Câu hỏi ôn lại

Tính lồi nghiêm có tự bảo đảm tồn tại đúng một nghiệm tối ưu không?

::: details Xem lời giải
Không. Nó bảo đảm nhiều nhất một nghiệm trên miền khả thi lồi. Muốn có đúng một nghiệm, cần thêm điều kiện bảo đảm nghiệm đạt được, chẳng hạn tính liên tục trên tập compact khác rỗng.
:::

## Đọc tiếp

- [Tập lồi](./tap-loi.md)
- [Gradient](./gradient.md)
- [Hessian](./hessian.md)
- [Cực tiểu cục bộ và toàn cục](./cuc-tieu-cuc-bo.md)

## Tài liệu tham khảo

- [S. Boyd và L. Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/).
