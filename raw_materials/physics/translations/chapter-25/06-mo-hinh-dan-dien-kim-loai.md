<!-- Phần 25.6, trang in 832–835. -->

## 25.6 Mô hình dẫn điện trong kim loại

Điện trở của kim loại bắt nguồn từ chuyển động của electron trong mạng tinh thể. Ta có thể xây dựng một mô hình vi mô đơn giản để nối mật độ electron, điện trường và thời gian giữa các va chạm với điện trở suất. Mô hình này dùng cơ học cổ điển và bỏ qua bản chất lượng tử của electron trong chất rắn, nên chỉ giải thích định tính và dự đoán gần đúng.

### Chuyển động ngẫu nhiên và chuyển động trôi

Trong tinh thể kim loại, mỗi nguyên tử góp một hoặc nhiều electron ngoài vào nhóm electron có thể chuyển động trong vật liệu. Các electron va chạm với các ion dương gần như đứng yên trong mạng tinh thể. Có thể hình dung chuyển động này như phân tử khí đi qua một lớp cát xốp.

Khi không có điện trường, electron đi theo đoạn thẳng giữa các va chạm nhưng hướng chuyển động phân bố ngẫu nhiên. Vận tốc trung bình có hướng của cả nhóm bằng không, nên không có dòng điện thuần. Khi có điện trường, mỗi electron vẫn chuyển động nhiệt ngẫu nhiên, đồng thời quỹ đạo bị lệch nhẹ và xuất hiện một vận tốc trôi có hướng. Hình 25.26 phóng đại độ cong quỹ đạo để biểu diễn độ trôi này.

Tốc độ do chuyển động ngẫu nhiên cỡ $10^6$ m/s, còn tốc độ trôi thường chỉ cỡ $10^{-4}$ m/s. Vì thế dòng điện không phải dòng electron chạy nhanh đồng loạt qua dây. Nó là độ lệch rất nhỏ của chuyển động ngẫu nhiên có sẵn. Thời gian trung bình giữa hai va chạm liên tiếp của một electron được gọi là thời gian tự do trung bình, ký hiệu $\tau$. Hình 25.27 dùng quả cầu lăn qua các chốt để gợi hình ảnh va chạm làm đổi hướng.

![Hình 25.26: Chuyển động ngẫu nhiên của electron khi không có trường và chuyển động trôi khi có điện trường](../img/young-25/hinh-25-26.png)

![Hình 25.27: Quả cầu lăn và đổi hướng khi va vào các chốt, mô hình hóa va chạm của electron](../img/young-25/hinh-25-27.png)

### Từ va chạm đến điện trở suất

Để nối mô hình với các đại lượng đo được, dùng định nghĩa điện trở suất và mật độ dòng điện:

$$
\rho=\frac EJ.
\tag{25.21}
$$

$$
\vec J=nq\vec v_d.
\tag{25.22}
$$

n là số electron tự do trong một đơn vị thể tích và q = −e là điện tích mỗi electron.

Xét một khoảng thời gian $\tau$ giữa các va chạm. Điện trường $\vec E$ tác dụng lực $\vec F=q\vec E$ lên hạt mang điện, nên gia tốc là:

$$
\vec a=\frac{\vec F}{m}
=\frac{q\vec E}{m}.
$$

Để dựng phép tính, tưởng tượng lúc đầu chưa có điện trường. Chuyển động hoàn toàn ngẫu nhiên và vận tốc trung bình có hướng của nhiều electron bằng không. Tại $t=0$, bật điện trường không đổi và tạm cho các va chạm ngừng tác dụng. Sau khoảng thời gian tự do trung bình $\tau$, cho các va chạm tác dụng trở lại.

Trong khoảng này, lực điện làm vận tốc mỗi electron đổi thêm $\vec a\tau$. Gọi $\vec v_0$ là vận tốc ngẫu nhiên của một electron tại thời điểm bắt đầu. Sau thời gian $\tau$, vận tốc của nó là:

$$
\vec v=\vec v_0+\vec a\tau.
$$

Lấy trung bình trên nhiều electron, các hướng ban đầu triệt tiêu nhau nên $\langle\vec v_0\rangle=0$. Phần vận tốc còn lại là độ trôi trung bình:

$$
\vec v_d=\frac{q\tau}{m}\vec E.
\tag{25.23}
$$

Với electron, $q=-e$, nên electron trôi ngược chiều điện trường. Mật độ dòng điện quy ước vẫn hướng cùng chiều điện trường, vì mật độ điện tích của hạt tải cũng âm.

Nếu có $n$ electron tự do trong một đơn vị thể tích, mật độ dòng điện là $\vec J=nq\vec v_d$. Thay vận tốc trôi:

$$
\begin{aligned}
&\vec J = nq\left(\frac{q\tau}{m}\vec E\right)\\
&\quad =\frac{nq^2\tau}{m}\vec E\\
&\quad =\frac{ne^2\tau}{m}\vec E.
\end{aligned}
$$

Theo định nghĩa ở công thức (25.21), điện trở suất là tỉ số độ lớn của điện trường và mật độ dòng điện.



Do đó, với mô hình electron cổ điển:

$$
\rho=\frac{m}{ne^2\tau}.
\tag{25.24}
$$

Điện trở suất giảm khi mật độ hạt tải $n$ hoặc thời gian tự do trung bình $\tau$ tăng. Nó tăng khi hạt tải nặng hơn. Nếu $n$ và $\tau$ không đổi theo độ lớn điện trường, $\rho$ cũng không đổi và vật liệu tuân theo định luật Ôm. Việc tưởng tượng tất cả electron bắt đầu cùng lúc chỉ là cách dựng phép tính. Nếu từng electron có thời điểm va chạm riêng, trung bình trên thời gian giữa va chạm vẫn cho cùng vận tốc trôi.

### Ảnh hưởng của nhiệt độ và giới hạn của mô hình

Trong tinh thể hoàn hảo lý tưởng, mô tả lượng tử cho phép electron chuyển động mà không va chạm vào nguyên tử đứng yên. Trong kim loại thật, ion mạng tinh thể dao động quanh vị trí cân bằng. Nhiệt độ tăng làm biên độ dao động lớn hơn, va chạm thường xuyên hơn và $\tau$ giảm. Vì $\rho=m/(ne^2\tau)$, mô hình dự đoán điện trở suất kim loại tăng theo nhiệt độ.

Ở chất siêu dẫn, gần đúng có thể xem không có va chạm không đàn hồi làm tiêu hao năng lượng. Khi đó $\tau$ tiến tới vô hạn và điện trở suất bằng không. Đây là mô tả khái quát, không phải phép suy ra đầy đủ cơ chế lượng tử của siêu dẫn.

Trong bán dẫn tinh khiết như silicon hoặc germanium, nhiệt độ tăng làm số hạt tải $n$ tăng rất nhanh. Sự tăng của $n$ lấn át sự giảm của $\tau$, nên điện trở suất giảm theo nhiệt độ. Ở nhiệt độ thấp, số hạt tải rất nhỏ và vật liệu có thể dẫn điện rất kém, gần như chất cách điện.

Electron nhận năng lượng từ điện trường khi chuyển động giữa các va chạm. Khi va chạm, chúng truyền một phần năng lượng cho nguyên tử vật liệu, làm nội năng và nhiệt độ tăng. Nếu điện trường đủ mạnh, electron có thể giải phóng thêm electron vốn liên kết với nguyên tử. Các electron mới tiếp tục va chạm và giải phóng hạt tải khác, tạo thác dòng điện. Quá trình này là một cơ chế đánh thủng điện môi.

### Ví dụ 25.11: Thời gian tự do trung bình trong đồng

Tính thời gian trung bình giữa các va chạm của electron trong đồng ở nhiệt độ phòng. Với đồng, mật độ electron tự do là $n=8{,}5\times10^{28}$ m⁻³ và điện trở suất $\rho=1{,}72\times10^{-8}$ Ω·m. Điện tích electron có độ lớn $e=1{,}60\times10^{-19}$ C, khối lượng $m=9{,}11\times10^{-31}$ kg.

**Xác định và lập kế hoạch:** Sắp xếp công thức điện trở suất để giải $\tau$. Các giá trị $n,\rho,e,m$ đều đã biết.

$$
\tau=\frac{m}{ne^2\rho}.
$$

**Thực hiện:**

$$
\begin{aligned}
&e^2 = 2{,}56\times10^{-38}\,\mathrm{C^2},\\
&ne^2 = 2{,}176\times10^{-9}\,\mathrm{C^2/m^3},\\
&ne^2\rho = 3{,}74272\times10^{-17}\,\mathrm{kg/s},\\
&\tau = \frac{9{,}11\times10^{-31}}{3{,}74272\times10^{-17}}\,\mathrm s\\
&\quad \approx2{,}4\times10^{-14}\,\mathrm s.
\end{aligned}
$$

**Đánh giá:** Số va chạm trung bình mỗi giây xấp xỉ nghịch đảo thời gian này:

$$
\frac1\tau\approx4{,}2\times10^{13}\,\mathrm{s^{-1}}.
$$

Điện trở suất của kim loại vì thế phản ánh mức độ thường xuyên electron bị tán xạ. Thời gian tự do càng dài thì điện trở suất càng nhỏ.

### Câu hỏi kiểm tra ngay sau mục 25.6

Yếu tố nào, nếu tăng lên, sẽ làm khó hơn việc tạo ra một dòng điện có độ lớn nhất định trong vật dẫn? Có thể có nhiều đáp án đúng.

- (i) Khối lượng của hạt mang điện chuyển động.
- (ii) Số hạt mang điện chuyển động trong mỗi mét khối.
- (iii) Độ lớn điện tích của mỗi hạt.
- (iv) Thời gian trung bình giữa các va chạm.

::: details Đáp án và lời giải
**Tóm tắt đề bài:** So sánh các yếu tố qua $\rho=m/(ne^2\tau)$. Ở cùng mật độ dòng điện, điện trở suất lớn hơn đòi hỏi điện trường lớn hơn.

**Hướng đi:**

- Tăng khối lượng $m$ làm $\rho$ tăng.
- Tăng $n$, độ lớn điện tích $e$ hoặc thời gian $\tau$ làm $\rho$ giảm.

Chỉ yếu tố (i) làm khó hơn việc tạo cùng dòng điện. Hạt nặng đáp ứng chậm hơn với điện trường, nên cần điện trường mạnh hơn để tạo cùng mật độ dòng.
:::
