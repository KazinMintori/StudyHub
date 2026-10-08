---
course: xac-suat-thong-ke
lecture: 03-ky-vong-phuong-sai
section: lecture
title: "Kỳ vọng, phương sai & mẫu dữ liệu"
prerequisites: ["ky-vong","phuong-sai","mau-tong-the"]
lessonStatus: ready
---


## 1. Kỳ vọng là trung bình theo xác suất

Giả sử $X$ nhận hữu hạn các giá trị phân biệt $x_1,\ldots,x_k$, với xác suất tương ứng $p_i=P(X=x_i)$. Kỳ vọng cộng các giá trị đã nhân với xác suất:

$$
\begin{aligned}
E[X]&=x_1p_1+x_2p_2+\cdots+x_kp_k\\
&=\sum_{i=1}^k x_i p_i.
\end{aligned}
$$

Chỉ số $i$ chạy qua các giá trị có thể nhận, không chạy qua các quan sát trong một mẫu. Cách viết $\sum_x xP(X=x)$ cũng có nghĩa là cộng qua tất cả giá trị $x$ có thể nhận. Với vô hạn đếm được, cần kiểm tra điều kiện tồn tại kỳ vọng, chẳng hạn tổng giá trị tuyệt đối có trọng số hữu hạn. Kỳ vọng không nhất thiết là một giá trị $X$ có thể nhận.

Ví dụ $X$ bằng 0 hoặc 2 với xác suất $\frac12$ mỗi giá trị: $E[X]=0\cdot\frac12+2\cdot\frac12=1$, dù $X$ không bao giờ bằng 1.

Tính tuyến tính: $E[aX+bY]=aE[X]+bE[Y]$ khi các kỳ vọng tồn tại. Không cần độc lập để dùng tính tuyến tính này.

## 2. Phương sai đo độ phân tán

$$\operatorname{Var}(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2.$$

Trong ví dụ trên, $E[X^2]=2$ nên phương sai bằng $2-1^2=1$. Độ lệch chuẩn là căn phương sai: $\sigma=1$.

Khi đổi thang đo: $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$. Cộng hằng số đổi trung tâm nhưng không đổi độ phân tán. Với hai biến độc lập có phương sai hữu hạn, phương sai của tổng bằng tổng phương sai. Nếu không độc lập cần tính hiệp phương sai.

## 3. Từ tổng thể sang mẫu

Tham số như trung bình tổng thể $\mu$ thường chưa biết. Từ mẫu $x_1,\ldots,x_n$, trung bình mẫu là:

$$\bar x=\frac{x_1+x_2+\cdots+x_n}{n}=\frac1n\sum_{i=1}^n x_i.$$

Ở đây $i$ chạy qua $n$ quan sát của mẫu. Mỗi quan sát có cùng trọng số $\frac1n$.

Một ước lượng phương sai tổng thể không chệch khi mẫu độc lập cùng phân phối và phương sai hữu hạn là:

$$s^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2,\quad n>1.$$

Tử số là $(x_1-\bar x)^2+\cdots+(x_n-\bar x)^2$: lấy độ lệch của từng quan sát, bình phương rồi cộng. Chỉ mẫu số đổi từ $n$ sang $n-1$ khi dùng ước lượng không chệch này.

Với mẫu [1,2,3], trung bình bằng 2 và tổng bình phương độ lệch bằng 2. Phương sai mẫu chia $n-1$ bằng 1. Nếu mô tả chính ba số này như toàn bộ tổng thể, chia n sẽ cho $\frac{2}{3}$. Hai mục tiêu khác nhau nên hai mẫu số khác nhau.

## 4. Kết luận phải đi cùng cách lấy mẫu

- Mẫu ngẫu nhiên phù hợp giúp kết luận về tổng thể, trong khi mẫu thuận tiện có thể bị lệch.
- Cỡ mẫu lớn không tự sửa được cách chọn mẫu sai.
- Vì trung bình có thể bị kéo bởi ngoại lệ, hãy xem thêm trung vị và phân bố dữ liệu.
- Ước lượng điểm cho một giá trị. Khoảng tin cậy và kiểm định cần thêm mô hình cùng giả định cụ thể, được học ở phần tiếp theo của lộ trình.

<details><summary>Tự kiểm tra: mọi điểm dữ liệu tăng thêm 10 thì trung bình và phương sai thay đổi thế nào?</summary>

Trung bình tăng 10. Phương sai không đổi vì độ lệch quanh trung bình giữ nguyên.

</details>
