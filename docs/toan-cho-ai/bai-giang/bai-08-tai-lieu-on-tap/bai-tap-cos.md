---
course: toan-cho-ai
lecture: bai-08-tai-lieu-on-tap
topic: bai-tap-cos
section: topic
title: "Giải bài toán ba biến có hàm cos"
description: "Gradient, Hessian, đa thức đặc trưng đã hiệu chỉnh, tính lồi nghiêm, phương trình sin x=7x/4 và hai chứng nhận nghiệm duy nhất."
---

Thành phần $\cos x$ không lồi trên toàn trục thực. Tuy nhiên, thêm một hàm có độ cong âm cục bộ vào một mục tiêu toàn phương vẫn có thể cho hàm lồi, nếu phần toàn phương đủ mạnh. Bài tập cuối Buổi 1, được giải tiếp trong Buổi 3, minh họa chính điều này.

## 1. Đề bài và gradient

Tìm giá trị nhỏ nhất trên $\mathbb R^3$ của

$$
f(x,y,z)=2x^2+2xy+y^2+xz+2z^2+\cos x.
$$

Đạo hàm theo từng biến là

$$
\begin{aligned}
f_x&=4x+2y+z-\sin x,\\
f_y&=2x+2y,\\
f_z&=x+4z.
\end{aligned}
$$

Các thành phần gradient cho hệ điểm dừng

$$
\begin{aligned}
4x+2y+z-\sin x&=0,\\
2x+2y&=0,\\
x+4z&=0.
\end{aligned}
$$

## 2. Hessian và tính xác định dương

Đạo hàm của $-\sin x$ là $-\cos x$, nên

$$
H=\nabla^2 f=\begin{bmatrix}
4-\cos x&2&1\\
2&2&0\\
1&0&4
\end{bmatrix}.
$$

Đặt $c=\cos x\in[-1,1]$. Các định thức con chính đầu theo tiêu chuẩn Sylvester là

$$
\begin{aligned}
\Delta_1&=4-c\ge3>0,\\
\Delta_2&=2(4-c)-4\\
&=4-2c\ge2>0,\\
\Delta_3&=\det H\\
&=14-8c\ge6>0.
\end{aligned}
$$

Vì $H$ đối xứng và cả ba định thức con chính đầu dương, $H\succ0$ với mọi $x$. Do đó $f$ lồi nghiêm trên toàn $\mathbb R^3$. Kiểm tra này không chỉ xét tại gốc tọa độ.

## 3. Đa thức đặc trưng

Giữ cách tiếp cận qua trị riêng của buổi học, dùng $\chi_H(t)=\det(H-tI)$. Khai triển đúng là

$$
\begin{aligned}
\chi_H(t)&=-t^3+(10-c)t^2\\
&\quad-(27-6c)t+(14-8c),\\
c&=\cos x.
\end{aligned}
$$

Với $t\le0$, số hạng $-t^3$ không âm, số hạng $(10-c)t^2$ không âm, số hạng $-(27-6c)t$ không âm, còn $14-8c>0$. Vì thế $\chi_H(t)>0$ trên nửa trục không dương. Ma trận đối xứng có đủ ba trị riêng thực, nên không trị riêng nào không dương. Đây là một cách khác chứng minh PD.

::: info Hiệu chỉnh các hệ số đại số
Lưu ý: Đa thức đặc trưng của Hessian phải chứa $\cos x$, đồng thời hai hệ số của các bậc thấp là 27 và 14 như khai triển phía trên (thay vì $\sin x$ hay các hệ số 29 và 22 thường gặp trong các bản tính nháp chưa chuẩn hóa).
:::

## 4. Giải hệ điểm dừng

Hai phương trình cuối cho $y=-x$ và $z=-x/4$. Thay vào phương trình đầu:

$$
\begin{aligned}
4x-2x-\frac x4-\sin x&=0,\\
\frac74x-\sin x&=0.
\end{aligned}
$$

Ta biết $|\sin x|\le|x|$. Nếu $x\ne0$, phương trình trên đòi hỏi

$$
\frac74|x|=|\sin x|\le|x|,
$$

mâu thuẫn vì $7/4>1$. Do đó $x=0$, kéo theo $y=z=0$. Gradient bằng không tại gốc và $f$ lồi nghiêm, nên đây là nghiệm tối ưu toàn cục duy nhất. Giá trị tối ưu là $f(0,0,0)=1$.

## 5. Chứng nhận trực tiếp bằng hoàn thành bình phương

Có thể giải mà không tính đa thức đặc trưng:

$$
f(x,y,z)=(y+x)^2+2(z+x/4)^2+\frac78x^2+\cos x.
$$

Với mỗi $x$ cố định, hai bình phương được cực tiểu hóa bằng $y=-x$, $z=-x/4$. Bài còn lại là min $F(x)=7x^2/8+\cos x$, có

$$
F''(x)=\frac74-\cos x\ge\frac34>0.
$$

Một cận trực tiếp còn mạnh hơn về mặt kiểm chứng là $\cos x\ge1-x^2/2$. Nó suy ra từ

$$
1-\cos x=2\sin^2(x/2)\le x^2/2.
$$

Vì vậy

$$
\begin{aligned}
f(x,y,z)&\ge1+\frac38x^2+(y+x)^2+2(z+x/4)^2\\
&\ge1.
\end{aligned}
$$

Đẳng thức buộc $x=0$, rồi $y=z=0$. Cận này đồng thời chứng minh giá trị tối ưu, sự đạt nghiệm và tính duy nhất.

## 6. Bài tập tự luyện

::: exercise Vai trò của thành phần lượng giác
Nếu chỉ nhìn $\cos x$ không lồi rồi kết luận $f$ không lồi, lập luận sai ở đâu?
:::

::: solution
Tính lồi của tổng phụ thuộc tổng Hessian. Một số hạng không lồi có thể được bù bởi độ cong dương của các số hạng còn lại. Trong bài này, sau khi khử $y,z$, độ cong nhỏ nhất của $F$ vẫn ít nhất $3/4$. Vì vậy phải kiểm cả biểu thức, không phân loại tổng chỉ từ một số hạng.
:::
