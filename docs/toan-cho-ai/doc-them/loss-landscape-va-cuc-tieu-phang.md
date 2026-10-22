---
title: "Cảnh quan mất mát, điểm yên ngựa và cực tiểu phẳng"
description: "Đọc Hessian, phân biệt độ nhạy tham số với dịch chuyển phân phối và hiểu bước xấp xỉ của SAM."
---

# Cảnh quan mất mát, điểm yên ngựa và cực tiểu phẳng

Hai nghiệm có cùng mất mát huấn luyện nhưng phản ứng khác nhau khi tham số bị thay đổi một chút. Để phân tích sự khác nhau, ta cần nhìn vào độ cong quanh nghiệm. Tuy nhiên, độ nhạy tham số và khả năng dự đoán trên dữ liệu mới là hai đại lượng khác nhau.

## 1. Hessian cho biết điều gì tại điểm dừng?

Giả sử hàm mất mát có đạo hàm bậc hai liên tục trong lân cận đang xét. Tại điểm dừng, gradient bằng 0. Hessian dương xác định là điều kiện đủ cho cực tiểu địa phương nghiêm ngặt. Hessian âm xác định cho cực đại địa phương nghiêm ngặt.

Nếu Hessian có cả trị riêng dương và âm, điểm dừng là điểm yên ngựa. Ngược lại, khi có trị riêng bằng 0, phép thử bậc hai có thể chưa kết luận được. Hàm $x^4$ vẫn có cực tiểu tại gốc dù đạo hàm bậc hai bằng 0.

Xét ví dụ hai biến:

$$
L(x,y)=x^2-y^2.
$$

Gốc là điểm dừng. Theo trục ngang, hàm tăng khi rời gốc. Theo trục dọc, hàm giảm. Nếu bắt đầu đúng tại gốc, hạ gradient xác định không tự di chuyển vì gradient bằng 0.

Hình dưới dùng hàm yên ngựa $g(x,y)=x^2+4xy+y^2$ để so sánh hai hướng qua gốc:

![Hình 1: Hai hướng qua một điểm yên ngựa có thể cho hai dấu độ cong khác nhau.](../../wiki/img/atlas/hessian.svg)

Trong không gian nhiều chiều, chỉ biết số chiều chưa đủ để xác định tỷ lệ điểm yên ngựa. Không thể mặc nhiên coi dấu các trị riêng là những lần tung đồng xu độc lập. Kết luận xác suất cần một mô hình phân bố Hessian và những giả thiết riêng.

## 2. Nhiễu của mini-batch có giúp thoát điểm yên ngựa không?

Với lô được lấy mẫu đều từ dữ liệu huấn luyện và hàm mục tiêu là trung bình mất mát từng mẫu, gradient mini-batch có kỳ vọng bằng gradient đầy đủ. Có thể viết:

$$
g_B(\theta)=\nabla L(\theta)+\xi_B.
$$

Ở đây $\xi_B$ là sai lệch do lấy mẫu. Nó có thể đưa tham số ra khỏi một vùng có gradient nhỏ. Nếu độ lệch có thành phần theo hướng độ cong âm, bước tối ưu tiếp theo có thể khuếch đại thành phần ấy.

Tuy nhiên, nhiễu mini-batch không nhất thiết có độ lớn như nhau theo mọi hướng. Vì vậy, không thể khẳng định SGD luôn thoát mọi điểm yên ngựa chỉ nhờ có nhiễu. Kết quả còn phụ thuộc cấu trúc bài toán, cách lấy mẫu và bước học.

## 3. Độ phẳng là một tính chất trong hệ tham số đã chọn

Giữ bán kính $\rho>0$ và chuẩn Euclid cố định. Một cách đo độ nhạy quanh $\theta$ là xét giá trị mất mát lớn nhất trong lân cận:

$$
M_\rho(\theta)=\max_{\|e\|_2\le\rho}L(\theta+e).
$$

Độ tăng tệ nhất so với điểm hiện tại là:

$$
S_\rho(\theta)=M_\rho(\theta)-L(\theta).
$$

Độ phẳng theo cách đo này phụ thuộc bán kính, chuẩn và cách tham số hóa. Dinh và cộng sự chỉ ra rằng các phép đổi tham số có thể thay đổi độ nhọn mà giữ nguyên hàm dự đoán. Vì vậy, độ nhọn riêng lẻ không tự quyết định khả năng tổng quát hóa.

Tại một điểm dừng trơn $\theta^*$, đặt $H=\nabla^2L(\theta^*)$. Với độ dời nhỏ, khai triển Taylor bậc hai cho:

$$
L(\theta^*+e)\approx L(\theta^*)+\frac12e^THe.
$$

Vì Hessian đối xứng, dạng toàn phương có cận:

$$
e^THe\le\lambda_{\max}(H)\|e\|_2^2.
$$

Cận này mô tả biến thiên của cùng một hàm mất mát khi thay tham số. Nó không đồng nhất sự thay đổi phân phối dữ liệu với một phép dịch chuyển tham số. Trong mạng ReLU, cũng cần thận trọng tại các điểm không khả vi bậc hai.

## 4. Một ví dụ tính được hoàn toàn

Xét họ hàm hai biến, với $a>0$:

$$
L_a(x,y)=\frac12(x^2+ay^2).
$$

Mọi hàm trong họ đều đạt cực tiểu 0 tại gốc. Dịch chuyển từ gốc tới $(0;0{,}01)$ cho:

$$
\begin{aligned}
L_1(0;0{,}01)&=0{,}00005,\\
L_{100}(0;0{,}01)&=0{,}005.
\end{aligned}
$$

Hàm thứ hai nhạy hơn theo hướng dọc trong hệ tọa độ này. Ví dụ chưa có tập kiểm thử hay phân bố dữ liệu, nên không thể dùng nó để kết luận mô hình nào dự đoán tốt hơn.

## 5. Bước xấp xỉ của SAM

SAM tìm tham số có mất mát thấp trong một lân cận bằng cách cực tiểu hóa $M_\rho(\theta)$. Đây nói chung vẫn là bài toán phi lồi, không mặc nhiên có cấu trúc lồi–lõm.

Đặt $g=\nabla L(\theta)$. Khi $g\ne0$, cực đại hóa xấp xỉ tuyến tính trên quả cầu Euclid cho độ dời:

$$
\hat e=\rho\frac{g}{\|g\|_2}.
$$

Đây là nghiệm của bài toán tuyến tính hóa, chưa chắc là điểm cực đại thật của hàm mất mát. Bước cập nhật bậc nhất dùng gradient tại điểm đã dịch:

$$
\theta_{\mathrm{new}}=\theta-\eta\nabla L(\theta+\hat e).
$$

Nếu $g=0$, công thức chuẩn hóa không xác định. Có thể đặt độ dời bằng 0 trong triển khai, nhưng khi đó xấp xỉ bậc nhất không cung cấp một hướng tăng. Hiệu quả dự đoán của thuật toán vẫn cần được đánh giá trên dữ liệu phù hợp.

## Câu hỏi ôn lại

Thay tọa độ bằng $\theta=cu$, với $c\ne0$, có giữ nguyên đạo hàm bậc hai theo tọa độ mới không?

::: details Xem lời giải
Không. Với $L(\theta)=\theta^2/2$, biểu thức theo $u$ là $c^2u^2/2$, nên đạo hàm bậc hai theo $u$ bằng $c^2$. Độ cong tọa độ thay đổi dù đây là cùng hàm được biểu diễn qua một phép đổi biến khả nghịch.
:::

## Tài liệu tham khảo

- P. Foret, A. Kleiner, H. Mobahi, B. Neyshabur. [Sharpness-Aware Minimization for Efficiently Improving Generalization](https://arxiv.org/abs/2010.01412), ICLR 2021.
- L. Dinh, R. Pascanu, S. Bengio, Y. Bengio. [Sharp Minima Can Generalize for Deep Nets](https://arxiv.org/abs/1703.04933), ICML 2017.
