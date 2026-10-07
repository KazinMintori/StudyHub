# A. Ánh xạ co và điểm bất động

## Lời giảng

“Contraction mapping” trong đoạn này là **ánh xạ co**. Ký hiệu \(\mathbb R\) chỉ tập các số thực, và \(T\) biến một số thực thành một số thực. Với hai số thực \(x,y\), khoảng cách giữa chúng là \(|x-y|\). Ánh xạ \(T\) là ánh xạ co khi tồn tại **một hằng số dùng chung** \(c\), với \(0\le c<1\), sao cho

\[
|T(x)-T(y)|\le c|x-y|\qquad\text{với mọi }x,y\in\mathbb R.
\]

Ta phải chọn được cùng một \(c\) cho tất cả các cặp điểm, chứ không chọn lại \(c\) mỗi khi thay \(x,y\). Khi \(x\ne y\), khoảng cách sau khi áp dụng \(T\) không vượt quá một tỉ lệ nhỏ hơn 1 của khoảng cách ban đầu. Khi \(x=y\), hai khoảng cách đều bằng 0, nên định nghĩa dùng dấu \(\le\).

Với \(T(x)=0.4x+3\), số 3 triệt tiêu khi lấy hiệu:

\[
|T(x)-T(y)|=|0.4x+3-(0.4y+3)|=0.4|x-y|.
\]

Vì vậy có thể chọn \(c=0.4\), đáp ứng \(0\le c<1\) cho mọi \(x,y\).

**Điểm bất động** là một số \(x^\star\) mà \(T\) giữ nguyên: \(T(x^\star)=x^\star\). Để tìm nó, ta giải

\[
0.4x^\star+3=x^\star
\quad\Longrightarrow\quad
3=0.6x^\star
\quad\Longrightarrow\quad
x^\star=5.
\]

Phép chia hợp lệ vì \(0.6\ne0\). Thế lại, \(T(5)=0.4\cdot5+3=5\), đúng với định nghĩa điểm bất động.

## Note ngắn

Với khoảng cách \(|x-y|\) trên tập số thực \(\mathbb R\), **ánh xạ co** là ánh xạ \(T:\mathbb R\to\mathbb R\) thỏa \(|T(x)-T(y)|\le c|x-y|\) với mọi \(x,y\), trong đó có một hằng số \(c\in[0,1)\) dùng chung cho tất cả các cặp điểm.

Với \(T(x)=0.4x+3\), hai số hạng 3 triệt tiêu khi lấy hiệu, nên \(|T(x)-T(y)|=0.4|x-y|\). Vì vậy chọn được hệ số co \(c=0.4\).

**Điểm bất động** \(x^\star\) thỏa \(T(x^\star)=x^\star\). Giải \(0.4x^\star+3=x^\star\), chuyển \(0.4x^\star\) sang vế phải, được \(3=0.6x^\star\). Chia cho \(0.6\ne0\) cho \(x^\star=5\); thế lại có \(T(5)=5\).
