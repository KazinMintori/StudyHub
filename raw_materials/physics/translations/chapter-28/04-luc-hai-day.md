## 28.4 Lực giữa hai dây dẫn song song

Khi ta đã biết từ trường do dây thẳng dài tạo ra, có thể tính lực mà dây ấy tác dụng lên một dây khác. Hai dây dẫn gần nhau cùng tạo từ trường và cùng chịu lực từ. Trường hợp này xuất hiện trong thiết bị điện, nơi nhiều dây mang dòng điện chạy song song.

![Từ trường và lực giữa hai dây dẫn song song mang dòng điện](../img/young-28/hinh-28-09.png)

Hình 28.9: Từ trường của dây dưới tác dụng lực lên dây trên. Dòng điện cùng chiều hút nhau, còn dòng ngược chiều đẩy nhau.

Hai dây thẳng dài, song song, cách nhau khoảng $r$, mang dòng điện lần lượt là $I$ và $I'$. Từ trường do dây dưới tạo ra tại vị trí dây trên có độ lớn:

$$
B = \frac{\mu_0 I}{2\pi r}. \tag{28.11}
$$

Xét đoạn dài $L$ của dây trên. Dòng điện $I'$ trong dây chịu lực $F=I'LB$ vì từ trường vuông góc với dây. Thay độ lớn $B$ vừa tìm được, lực trên một đơn vị chiều dài là:

$$
\frac{F}{L} = \frac{\mu_0 I I'}{2\pi r}.
$$

Quy tắc bàn tay phải cho thấy dây trên bị kéo xuống, về phía dây dưới. Dây dưới cũng bị kéo lên, nên hai dây hút nhau khi dòng điện cùng chiều. Nếu đảo chiều một trong hai dòng điện, cả hai lực đổi chiều và hai dây đẩy nhau.

### Hằng số từ trong hệ SI

Trước năm 2018, ampere được định nghĩa sao cho hai dây thẳng song song dài vô hạn, cách nhau $1\,\mathrm m$, mỗi dây mang dòng $1\,\mathrm A$, hút nhau với lực chính xác $2\times10^{-7}\,\mathrm{N/m}$. Theo định nghĩa ấy, $\mu_0$ có giá trị chính xác $4\pi\times10^{-7}\,\mathrm{T\,m/A}$.

Thay giá trị cũ của $\mu_0$ vào phương trình (28.11), lực trên một đơn vị chiều dài của cấu hình chuẩn đó là:

$$
\begin{aligned}
\frac{F}{L} &= \frac{\mu_0}{2\pi} \times\frac{(1\,\mathrm A)(1\,\mathrm A)}{1\,\mathrm m} \\
&= 2\times10^{-7}\,\mathrm{N/m}.
\end{aligned}
$$

Hiện nay, coulomb được xác định từ điện tích nguyên tố $e$. Vì vậy, giá trị $\mu_0$ được đo thực nghiệm và có độ bất định tương đối khoảng $2\times10^{-10}$. Sai khác so với giá trị cũ rất nhỏ, nên ta vẫn có thể dùng $4\pi\times10^{-7}\,\mathrm{T\,m/A}$ trong các phép tính ở đây.

Các lực hút cũng xuất hiện giữa các phần của cùng một dây dẫn. Trong kim loại rắn, hiệu ứng này thường rất nhỏ. Nếu vật dẫn là chất lỏng hoặc plasma, lực hút có thể làm dòng vật chất co thắt. Hiện tượng ấy gọi là **hiệu ứng thắt dòng** (pinch effect) và từng được dùng trong một số kỹ thuật nghiên cứu phản ứng nhiệt hạch.

::: example Ví dụ 28.5 Lực giữa hai dây siêu dẫn
Hai dây thẳng, song song, cách nhau $r=4{,}5\,\mathrm{mm}$, mỗi dây mang dòng $I=I'=15\,000\,\mathrm A$ ngược chiều nhau. Hãy tính độ lớn lực mà mỗi dây tác dụng lên một đơn vị chiều dài của dây kia.

Hai dòng điện ngược chiều nên hai dây đẩy nhau. Độ lớn lực trên một đơn vị chiều dài được tính bằng phương trình (28.11):

![Sơ đồ hai dây song song cách nhau 4,5 mm trong Ví dụ 28.5](../img/young-28/hinh-28-10.png)

Hình 28.10: Hai dây siêu dẫn mang các dòng điện bằng nhau và ngược chiều.

$$
\begin{aligned}
\frac{F}{L} &= \frac{\mu_0 I^2}{2\pi r} \\
&= \frac{2\times10^{-7}}{4{,}5\times10^{-3}} \\
&\qquad\times(2{,}25\times10^8)\,\mathrm{N/m} \\
&= \frac{4{,}5\times10^1\,\mathrm N}{4{,}5\times10^{-3}\,\mathrm m} \\
&= 1{,}0\times10^4\,\mathrm{N/m}.
\end{aligned}
$$

Lực này lớn hơn một tấn trọng lượng trên mỗi mét chiều dài. Dòng điện và khoảng cách kiểu này xuất hiện trong nam châm siêu dẫn của máy gia tốc hạt, nên việc phân tích ứng suất cơ học là một phần quan trọng của thiết kế.
:::

### Tự kiểm tra 28.4

Một ống dây là dây dẫn quấn thành cuộn xoắn ốc. Xét cuộn dây đang có dòng điện như hình.

![Một ống dây mang dòng điện và các vòng dây quấn gần nhau](../img/young-28/tu-kiem-tra-28-04.png)

Hãy xác định lực từ mà (a) một vòng tác dụng lên vòng kề bên và (c) hai phía đối diện của cùng một vòng tác dụng lên nhau. Với mỗi trường hợp, lực hút, lực đẩy hay bằng không? Lực điện trong hai trường hợp (b) và (d) có lực hút, lực đẩy hay bằng không?

::: details Đáp án
(a) Các vòng kề nhau mang dòng cùng chiều nên hút nhau. (b) Dây trung hòa điện, vì nó chứa lượng điện tích dương và âm bằng nhau, nên lực điện tổng bằng không. (c) Hai phía đối diện của cùng một vòng mang dòng ngược chiều nên đẩy nhau. (d) Lực điện cũng bằng không vì dây vẫn trung hòa.

Vì vậy, lực từ kéo các vòng của ống dây lại gần nhau dọc theo trục cuộn dây, đồng thời đẩy chúng ra ngoài theo phương bán kính.
:::
