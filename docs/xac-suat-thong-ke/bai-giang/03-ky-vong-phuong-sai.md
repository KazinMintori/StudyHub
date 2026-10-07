---
course: xac-suat-thong-ke
lecture: 03-ky-vong-phuong-sai
section: lecture
title: "Kỳ vọng, phương sai & mẫu dữ liệu"
prerequisites: ["ky-vong","phuong-sai","mau-tong-the"]
lessonStatus: ready
---


## 1. Kỳ vọng là trung bình theo xác suất

Với biến ngẫu nhiên rời rạc, $E[X]=\sum_x xP(X=x)$. Mỗi giá trị được nhân với xác suất của nó. Kỳ vọng không nhất thiết là một giá trị X có thể nhận.

Ví dụ X bằng 0 hoặc 2 với xác suất 1/2 mỗi giá trị: $E[X]=0\times1/2+2\times1/2=1$, dù X không bao giờ bằng 1.

Tính tuyến tính: $E[aX+bY]=aE[X]+bE[Y]$ khi các kỳ vọng tồn tại. Không cần độc lập để dùng tính tuyến tính này.

## 2. Phương sai đo độ phân tán

$$\operatorname{Var}(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2.$$

Trong ví dụ trên, $E[X^2]=2$ nên phương sai bằng $2-1^2=1$. Độ lệch chuẩn là căn phương sai: $\sigma=1$.

Khi đổi thang đo: $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$. Cộng hằng số đổi trung tâm nhưng không đổi độ phân tán. Với hai biến độc lập có phương sai hữu hạn, phương sai của tổng bằng tổng phương sai; nếu không độc lập cần tính hiệp phương sai.

## 3. Từ tổng thể sang mẫu

Tham số như trung bình tổng thể $\mu$ thường chưa biết. Từ mẫu $x_1,\ldots,x_n$, trung bình mẫu là:

$$\bar x=\frac1n\sum_{i=1}^n x_i.$$

Một ước lượng phương sai tổng thể không chệch khi mẫu độc lập cùng phân phối và phương sai hữu hạn là:

$$s^2=\frac1{n-1}\sum_{i=1}^n(x_i-\bar x)^2,\quad n>1.$$

Với mẫu [1,2,3], trung bình bằng 2 và tổng bình phương độ lệch bằng 2. Phương sai mẫu chia n−1 bằng 1. Nếu mô tả chính ba số này như toàn bộ tổng thể, chia n sẽ cho 2/3. Hai mục tiêu khác nhau nên hai mẫu số khác nhau.

## 4. Kết luận phải đi cùng cách lấy mẫu

- Mẫu ngẫu nhiên phù hợp giúp kết luận về tổng thể; mẫu thuận tiện có thể bị lệch.
- Cỡ mẫu lớn không tự sửa được cách chọn mẫu sai.
- Trung bình có thể bị kéo bởi ngoại lệ; hãy xem thêm trung vị và phân bố dữ liệu.
- Ước lượng điểm cho một giá trị; khoảng tin cậy và kiểm định cần thêm mô hình cùng giả định cụ thể, được học ở phần tiếp theo của lộ trình.

<details><summary>Tự kiểm tra: mọi điểm dữ liệu tăng thêm 10 thì trung bình và phương sai thay đổi thế nào?</summary>

Trung bình tăng 10; phương sai không đổi vì độ lệch quanh trung bình giữ nguyên.

</details>
