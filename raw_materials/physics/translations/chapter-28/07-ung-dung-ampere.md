## 28.7 Ứng dụng định luật Ampere

Định luật Ampere giúp tìm từ trường khi hình học dòng điện tạo đủ đối xứng để chọn một đường kín đơn giản. Ba ví dụ tiêu biểu là dây trụ có dòng phân bố đều, ống dây dài và ống dây hình xuyến. Mỗi trường hợp đòi hỏi chọn đúng dòng điện được bao và nêu rõ nơi các kết quả gần đúng có hiệu lực.

### Chiến lược giải bài toán bằng định luật Ampere

Định luật Ampere luôn đúng trong điều kiện áp dụng, nhưng chỉ giúp tính trực tiếp $B$ khi phân bố dòng có đối xứng cao. Có thể giải theo chuỗi bước sau:

1. Xác định đại lượng cần tìm, thường là độ lớn và chiều của $\vec B$ theo vị trí.
2. Chọn đường kín đi qua điểm cần khảo sát. Đường này không nhất thiết là biên vật lý. Nó có thể nằm trong không khí, bên trong dây hoặc đi qua nhiều môi trường.
3. Tận dụng đối xứng để chọn đường sao cho trường tiếp tuyến và có độ lớn không đổi trên một đoạn. Trên các đoạn còn lại, cố gắng để trường vuông góc với đường đi hoặc gần bằng không.
4. Tính $\oint\vec B\cdot d\vec l$ bằng trường tổng tại từng điểm. Không bỏ trường do các dòng điện nằm ngoài đường kín.
5. Tính $I_{\mathrm{encl}}$ theo dấu. Khum ngón tay phải theo chiều tích phân, ngón cái xác định chiều dòng điện dương.
6. Dùng (28.20) để giải đại lượng cần tìm, rồi kiểm tra đơn vị và giới hạn theo vị trí.

Nếu $I_{\mathrm{encl}}=0$, tích phân bằng không, nhưng điều đó chỉ nói tổng các đóng góp triệt tiêu. Nó không khẳng định $\vec B=0$ tại từng điểm trên đường tích phân.

### Dây dẫn thẳng dài

![Đường sức tròn và đường tích phân bao quanh dây dẫn thẳng](../img/young-28/hinh-28-16.png)

Hình 28.16: Dòng chạy ra khỏi mặt giấy tạo trường ngược chiều kim đồng hồ.

Xét dây thẳng dài mang dòng $I$. Đối xứng trụ cho biết các đường sức là đường tròn đồng tâm. Trên đường tròn bán kính $r$, trường tiếp tuyến và có độ lớn không đổi. Chọn chiều tích phân cùng chiều trường để dòng bao là dương:

$$
\begin{aligned}
&\oint\vec B\cdot d\vec l = B\oint dl\\
&\quad =B(2\pi r)\\
&\quad =\mu_0I.
\end{aligned}
$$

Do đó:

$$
B=\frac{\mu_0I}{2\pi r}.
\tag{28.9}
$$

Định luật cũng xác định chiều trường qua chiều đi trên đường tích phân và dấu của dòng điện. Ví dụ, nếu dòng đi ra khỏi mặt giấy thì khum ngón tay theo dòng, trường quanh dây đi ngược chiều kim đồng hồ.

### Ví dụ 28.7: Trường của dây dẫn thẳng dài

Tìm trường do dây thẳng dài mang dòng $I$ bằng định luật Ampere. Ta chọn đường tròn bán kính $r$ đồng tâm với dây vì đối xứng trụ làm trường tiếp tuyến và có cùng độ lớn trên toàn đường. Khi đó:

$$
\begin{aligned}
&B(2\pi r) = \mu_0I,\\
&B = \frac{\mu_0I}{2\pi r}.
\end{aligned}
$$

Nếu chiều tích phân ngược hướng trường do dòng điện tạo ra, cả tích phân và dòng bao đều mang dấu âm. Độ lớn $B$ vẫn dương theo định nghĩa độ lớn.

### Ví dụ 28.8: Dây trụ đặc có dòng phân bố đều

![Đường tích phân bên trong và bên ngoài dây trụ mang dòng điện đều](../img/young-28/hinh-28-20.png)

Hình 28.20: Với $r<R$, dòng được bao chỉ chiếm phần diện tích bên trong đường tròn. Với $r>R$, đường đi bao toàn bộ dòng điện.

Một dây dẫn hình trụ bán kính $R$ mang dòng tổng $I$, phân bố đều trên tiết diện. Tìm $B(r)$ cả bên trong lẫn bên ngoài. Do đối xứng trụ, tại mỗi bán kính $r$ trường có độ lớn không đổi trên đường tròn đồng tâm và tiếp tuyến với đường ấy.

#### Bên trong dây, $r<R$

Mật độ dòng điện là dòng trên một đơn vị diện tích:

$$
J=\frac{I}{\pi R^2}.
$$

Đường tròn bán kính $r$ bao diện tích $\pi r^2$, nên dòng điện được bao là:

$$
I_{\mathrm{encl}}=J\pi r^2=I\frac{r^2}{R^2}.
$$

Áp dụng định luật Ampere trên đường tròn này:

$$
\begin{aligned}
&B(2\pi r) = \mu_0I\frac{r^2}{R^2},\\
&B(r) = \frac{\mu_0Ir}{2\pi R^2},\qquad r<R.
\end{aligned}
\tag{28.21}
$$

Trường tăng tuyến tính theo $r$ từ tâm đến bề mặt.

#### Bên ngoài dây, $r>R$

Đường tích phân bao toàn bộ dòng $I$. Vì vậy:

$$
\begin{aligned}
&B(2\pi r) = \mu_0I,\\
&B(r) = \frac{\mu_0I}{2\pi r},\qquad r>R.
\end{aligned}
\tag{28.22}
$$

Ở ngoài dây, trường giống trường của một dây thẳng mang toàn bộ dòng $I$ dọc theo trục. Kết quả này không phụ thuộc bán kính dây hay cách dòng phân bố theo bán kính, miễn phân bố vẫn có đối xứng trụ. Tại bề mặt, hai biểu thức khớp nhau:

$$
B(R)=\frac{\mu_0I}{2\pi R}.
$$

![Đồ thị trường tăng tuyến tính trong dây trụ và giảm nghịch đảo khoảng cách bên ngoài](../img/young-28/hinh-28-21.png)

Hình 28.21: Độ lớn trường liên tục tại mặt dây, tăng tuyến tính bên trong và giảm theo $1/r$ bên ngoài.

Đồ thị có điểm gấp độ dốc ở $r=R$, nhưng không có bước nhảy về độ lớn. Đây là một kiểm tra hữu ích cho việc ghép hai miền.

### Tự kiểm tra 28.7: Cáp đồng trục

![Cấu tạo của cáp đồng trục gồm dây trung tâm, lớp cách điện và ống dẫn ngoài](../img/young-28/ung-dung-cap-dong-truc.png)

Một cáp đồng trục có dòng $I$ chạy theo một chiều trong dây trung tâm. Dòng có cùng độ lớn nhưng ngược chiều chạy trong ống dẫn trụ ngoài và phân bố đều trên tiết diện vỏ. Hỏi trường từ ở bên ngoài cáp phụ thuộc vào khoảng cách $r$ thế nào.

**Lập luận:** Chọn đường tròn đồng tâm bán kính lớn hơn bán kính ngoài của cáp. Đối xứng yêu cầu trường ngoài tiếp tuyến và có độ lớn không đổi trên đường tròn. Dòng đại số được bao bằng không vì hai dòng triệt tiêu:

$$
I_{\mathrm{encl}}=I-I=0.
$$

Định luật Ampere cho $B(2\pi r)=0$, nên $B=0$ bên ngoài cáp trong mô hình đối xứng lý tưởng. Dòng ngoài không làm trường tại từng điểm biến mất riêng lẻ. Kết quả bằng không do dòng bao tổng bằng không và đối xứng làm $B$ không đổi trên đường tròn.

### Ví dụ 28.9: Trường bên trong ống dây dài

![Đường sức bên trong ống dây dài, gần đều ở vùng giữa](../img/young-28/hinh-28-22.png)

Hình 28.22: Ở gần trung điểm, các đường sức bên trong ống dây dài gần song song và cách đều. Với ống dây dài, một nửa số đường sức đi ra ở hai đầu, nửa còn lại rò qua phần dây quấn giữa trung điểm và đầu ống.

Một ống dây gồm các vòng dây quấn sít trên mặt trụ. Gọi $n$ là số vòng trên một đơn vị chiều dài. Tìm trường gần trung điểm của ống dây mang dòng $I$.

Khi ống dây dài hơn nhiều đường kính và các vòng quấn sít, trường bên trong gần đều, gần song song với trục. Trường bên ngoài gần trung điểm rất nhỏ. Chọn đường Ampere hình chữ nhật có một cạnh dài $L$ song song với trục và nằm trong ống dây, cạnh đối diện nằm ngoài vùng có trường đáng kể. Hai cạnh ngắn vuông góc với trường.

![Đường tích phân hình chữ nhật với một cạnh bên trong và một cạnh bên ngoài ống dây](../img/young-28/hinh-28-23.png)

Hình 28.23: Chỉ cạnh dài bên trong ống dây đóng góp đáng kể vào tích phân.

Trên cạnh trong, $\vec B$ song song $d\vec l$ và có độ lớn gần không đổi, nên đóng góp là $BL$. Hai cạnh ngắn vuông góc trường. Cạnh ngoài nằm nơi trường xấp xỉ không. Tổng tích phân là:

$$
\oint\vec B\cdot d\vec l\approx BL.
$$

Trong chiều dài $L$ có $nL$ vòng, mỗi vòng xuyên qua mặt chữ nhật một lần và mang dòng $I$. Do đó $I_{\mathrm{encl}}=nLI$. Định luật Ampere cho:

$$
\begin{aligned}
&BL = \mu_0nLI,\\
&B = \mu_0nI.
\end{aligned}
\tag{28.23}
$$

Cạnh trong không cần nằm trên trục. Kết quả vì vậy cho thấy trường ở vùng giữa gần như đồng đều trên toàn tiết diện. Trên trục, trường đạt giá trị lớn nhất ở tâm. Với ống dây rất dài, độ lớn ở mỗi đầu bằng một nửa giá trị tại tâm. Với ống dây hữu hạn, đây là xấp xỉ, như đường biểu diễn cho một ống dây dài bốn lần đường kính.

![Đồ thị trường dọc trục ống dây hữu hạn](../img/young-28/hinh-28-24.png)

Hình 28.24: Trường giảm ở hai đầu ống dây và bằng khoảng một nửa giá trị giữa ống trong mô hình dài.

### Ví dụ 28.10: Trường của ống dây hình xuyến

![Ba đường tròn Ampere trong và ngoài một ống dây hình xuyến](../img/young-28/hinh-28-25.png)

Hình 28.25: Đường 1 nằm trong lỗ, đường 2 nằm trong vùng lõi, còn đường 3 nằm phía ngoài các vòng dây.

Một ống dây hình xuyến được quấn sít với $N$ vòng mang dòng $I$. Bỏ qua độ nghiêng nhỏ của các vòng dây xoắn, mỗi vòng gần như nằm trong mặt phẳng vuông góc với trục lớn của xuyến. Đối xứng cho biết các đường sức là các đường tròn đồng tâm với trục xuyến.

**Đường 1, trong lỗ xuyến:** Đường đi không bao dòng điện. Vì thế $I_{\mathrm{encl}}=0$, và theo đối xứng $B=0$ trên đường này.

**Đường 3, phía ngoài xuyến:** Mỗi vòng dây xuyên qua mặt do đường 3 bao hai lần theo hai chiều ngược nhau. Tổng dòng đại số bằng không, do đó $B=0$ trong mô hình lý tưởng.

**Đường 2, trong lõi xuyến:** Đường tròn bán kính $r$ bao mỗi vòng dây một lần, nên $I_{\mathrm{encl}}=NI$. Trường tiếp tuyến và có độ lớn không đổi trên đường tròn:

$$
\begin{aligned}
&B(2\pi r) = \mu_0NI,\\
&B(r) = \frac{\mu_0NI}{2\pi r}.
\end{aligned}
\tag{28.24}
$$

Chiều trường theo quy tắc bàn tay phải gắn với chiều tích phân và chiều dòng trong các vòng. Trường trong lõi không đồng đều trên toàn tiết diện vì phụ thuộc khoảng cách $r$ đến trục xuyến. Nếu bề dày lõi nhỏ so với bán kính trung bình, có thể xem $r$ gần như không đổi. Khi đó $B\approx\mu_0nI$, với $n=N/(2\pi r)$ là số vòng trên một đơn vị chiều dài dọc lõi.

Trong xuyến thật, các vòng dây là những đoạn của một đường xoắn chứ không phải các vòng tròn hoàn hảo. Vì vậy trường ngoài không bằng không tuyệt đối. Ước lượng xuyến như một vòng dòng điện lớn cho trường ngoài nhỏ hơn trường trong khoảng hệ số $N/\pi$.

Các biểu thức của ống dây thẳng và ống dây hình xuyến được suy ra trong chân không. Với nhiều ứng dụng, chúng cũng gần đúng trong không khí hoặc trong lõi không từ tính, không siêu dẫn. Nếu lõi có tính chất từ đáng kể, cần tính đến từ hóa và dùng độ từ thẩm thích hợp.
