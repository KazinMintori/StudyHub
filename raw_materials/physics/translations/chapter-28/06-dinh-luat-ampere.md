## 28.6 Định luật Ampere

Định luật Biot–Savart tính trường bằng cách cộng đóng góp của từng phần tử dòng điện. Với phân bố dòng có đối xứng cao, ta có thể tìm trường nhanh hơn bằng cách tích phân thành phần tiếp tuyến của $\vec B$ trên một đường kín. Định luật Ampere liên hệ tích phân ấy với dòng điện xuyên qua mặt được đường kín bao quanh.

Định luật Gauss cho điện trường xét thông lượng qua một mặt kín để liên hệ điện trường với điện tích bên trong. Thông lượng từ qua mọi mặt kín lại luôn bằng không, nên định luật Gauss cho từ trường không cho ta cách tính trực tiếp trường do một dòng điện cụ thể. Định luật Ampere dùng một đại lượng khác: Tích phân đường của thành phần trường song song với đường đi.

### Tích phân đường kín quanh dây thẳng dài

Với dây dẫn thẳng rất dài mang dòng $I$, đường sức từ là các đường tròn đồng tâm quanh dây. Ở khoảng cách $r$, độ lớn trường là $B=\mu_0I/(2\pi r)$. Chọn đường tích phân là đường tròn bán kính $r$ có tâm trên dây.

![Ba đường tích phân cho thấy dấu tích phân Ampere phụ thuộc chiều đi và dòng điện được bao](../img/young-28/hinh-28-16.png)

Hình 28.16: Đường kín bao dây cho tích phân $+\mu_0I$ hoặc $-\mu_0I$ tùy chiều đi. Đường không bao dây cho tích phân bằng không.

Trên đường tròn đồng tâm, $\vec B$ tiếp tuyến với đường đi và có độ lớn không đổi. Nếu đi theo chiều cùng hướng trường, tích phân là:

$$
\begin{aligned}
\oint\vec B\cdot d\vec l &= \oint B\,dl \\
&= B(2\pi r) \\
&= \frac{\mu_0I}{2\pi r}(2\pi r) \\
&= \mu_0I.
\end{aligned}
$$

Giá trị không phụ thuộc bán kính đường tròn. Nếu đi theo chiều ngược trường, tích vô hướng đổi dấu và tích phân bằng $-\mu_0I$.

Để xác định dấu dòng điện, khum các ngón tay phải theo chiều tích phân. Ngón cái chỉ chiều dòng điện dương xuyên qua mặt do đường kín bao. Với đường đi ngược chiều kim đồng hồ khi nhìn vào mặt giấy, dòng hướng ra khỏi mặt giấy là dương. Dòng đi vào mặt giấy là âm.

Nếu đường kín không bao dây, tích phân vẫn có thể bằng không dù $\vec B$ khác không trên nhiều đoạn. Trong hình (c), các cung tròn đóng góp trái dấu. Hai đoạn thẳng nối cung vuông góc với trường nên đóng góp bằng không. Tích phân tổng triệt tiêu.

Gọi bán kính hai cung là $r_1$ và $r_2$. Trên cung thứ nhất, đóng góp là $B_1(2\pi r_1)=\mu_0I$. Trên cung đi ngược chiều trường, đóng góp là $-B_2(2\pi r_2)=-\mu_0I$. Vì hai đoạn thẳng vuông góc với trường, tổng tích phân bằng:

$$
\begin{aligned}
\oint\vec B\cdot d\vec l &= \mu_0I-\mu_0I \\
&= 0.
\end{aligned}
$$

### Vì sao dạng tổng quát không phụ thuộc hình dạng đường đi

![Đường kín bất kỳ cho thấy góc quét tổng phụ thuộc đường có bao dây hay không](../img/young-28/hinh-28-17.png)

Hình 28.17: Thành phần tiếp tuyến của trường được viết qua độ biến thiên góc nhìn từ dây đến phần tử đường đi.

Với dây thẳng dài, ở mỗi điểm cách dây một khoảng $r$, trường có độ lớn $B=\mu_0I/(2\pi r)$. Gọi $\phi$ là góc giữa $d\vec l$ và $\vec B$. Tích phân vi phân là:

$$
\vec B\cdot d\vec l=B\,dl\cos\phi.
$$

Từ hình học, $dl\cos\phi=r\,d\theta$, với $d\theta$ là góc có đỉnh trên dây mà phần tử $d\vec l$ chắn ra. Vì vậy:

$$
\begin{aligned}
\oint\vec B\cdot d\vec l &= \oint\frac{\mu_0I}{2\pi r}(r\,d\theta) \\
&= \frac{\mu_0I}{2\pi}\oint d\theta.
\end{aligned}
$$

Nếu đường kín bao dây một lần, tia nối dây với điểm đang chạy quanh đường quét tổng góc $2\pi$. Nếu đường kín không bao dây, tổng độ biến thiên góc bằng không nên tích phân bằng không. Khi đường bao dây, dấu của $I$ theo quy tắc bàn tay phải. Vì vậy:

$$
\oint\vec B\cdot d\vec l=\mu_0I.
\tag{28.19}
$$

Điều quan trọng không phải đường đi tròn hay méo. Điều quyết định tích phân là dòng điện đại số được đường kín bao quanh.

### Phát biểu tổng quát của định luật Ampere

![Quy tắc bàn tay phải và dòng điện đại số được một đường kín bao quanh](../img/young-28/hinh-28-18.png)

Hình 28.18: Chiều khum ngón tay theo đường tích phân xác định chiều dòng điện dương qua mặt.

Nếu đường kín bao nhiều dây, từ trường tổng trên đường đi là tổng vectơ trường của từng dây. Do tính tuyến tính của tích phân, tích phân tổng bằng tổng các tích phân riêng. Mỗi dây được bao góp dòng điện với dấu theo quy tắc bàn tay phải. Dây không bị bao vẫn có thể tạo trường tại mọi điểm trên đường, nhưng đóng góp của nó vào tích phân quanh đường kín bằng không.

Gọi $I_{\mathrm{encl}}$ là tổng đại số các dòng điện xuyên qua một mặt bất kỳ được giới hạn bởi đường tích phân. Định luật Ampere viết:

$$
\oint\vec B\cdot d\vec l=\mu_0I_{\mathrm{encl}}.
\tag{28.20}
$$

Định luật đúng cho các đường kín và dây dẫn có hình dạng bất kỳ trong điều kiện từ tĩnh. Trong phạm vi này, dòng điện phải không đổi theo thời gian và không có điện trường biến thiên theo thời gian. Khi điện trường biến thiên, phương trình cần thêm số hạng dòng điện dịch, nội dung được xét ở phần tiếp theo của điện từ học.

![Dòng điện trái dấu bằng nhau xuyên qua mặt khiến tích phân quanh đường bao bằng không](../img/young-28/hinh-28-19.png)

Hình 28.19: Hai dòng điện bằng nhau, ngược chiều làm $I_{\mathrm{encl}}=0$. Tích phân bằng không nhưng từ trường dọc đường không nhất thiết bằng không.

### Không đồng nhất tích phân Ampere với công cơ học

Trong tĩnh điện, tích phân đường kín của điện trường bằng không, liên hệ với tính bảo toàn của lực điện tĩnh. Tích phân $\oint\vec B\cdot d\vec l$ có ý nghĩa khác. Nó đếm dòng điện đại số xuyên qua mặt được đường kín bao, chứ không đo công của lực từ.

Lực từ lên điện tích chuyển động là $\vec F=q\vec v\times\vec B$. Lực này phụ thuộc vận tốc và luôn vuông góc với vận tốc, nên không thể xem là lực thế chỉ phụ thuộc vị trí. Vì vậy không thể suy ra tính bảo toàn của lực từ từ giá trị của tích phân Ampere.

### Tự kiểm tra 28.6

Một đường sức từ đỏ đi xuyên qua tâm của một nam châm vĩnh cửu. Nam châm không nối với nguồn suất điện động. Hãy xác định chiều của dòng điện tổng hợp bị đường sức ấy bao.

**Lập luận:** Đi dọc đường sức theo chiều ngược kim đồng hồ. Tại mọi điểm, $\vec B$ và $d\vec l$ cùng chiều nên $\vec B\cdot d\vec l>0$. Tích phân quanh đường dương, do đó $I_{\mathrm{encl}}>0$. Theo quy tắc bàn tay phải, dòng điện tổng hợp hướng ra khỏi mặt giấy. Vì ngoài nam châm không có dòng điện, các dòng vi mô tương ứng nằm bên trong vật liệu nam châm.
