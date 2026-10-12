<!-- Source: Section22.2, printed721–725, PDF741–745. -->

## 22.2. Tính điện thông

Muốn biến phát biểu định tính thành công cụ tính toán, ta cần phân biệt độ lớn trường, diện tích mặt và góc giữa trường với mặt. Một ví dụ chất lưu giúp xác định đúng đại lượng hình học cần dùng.

### Hình dung từ dòng chất lưu

Cho chất lưu chảy đều với vận tốc $\vec v$ qua một khung chữ nhật diện tích A. Khi mặt khung vuông góc dòng chảy, thể tích đi qua mỗi giây bằng vA. Nếu nghiêng khung, dòng chỉ nhìn thấy diện tích hình chiếu của khung lên mặt vuông góc với vận tốc.

![Hình 22.5: Diện tích vuông góc với dòng chảy và diện tích hình chiếu của khung nghiêng](../img/young-22/hinh-22-5.png)

Gọi φ là góc giữa vận tốc và **pháp tuyến** của khung. Hai cạnh hình chiếu không đổi, hai cạnh còn lại ngắn đi theo hệ số cosφ. Do đó:

$$
\begin{aligned}
A_\perp&=A\cos\varphi,\\
\frac{dV}{dt}&=vA\cos\varphi\\
&=v_\perp A.
\end{aligned}
$$

Khi $\varphi=90^\circ$, khung nằm dọc dòng, không có chất lưu xuyên qua. Ta định nghĩa vector diện tích $\vec A$ có độ lớn A và vuông góc mặt. Khi ấy:

$$
\frac{dV}{dt}=\vec v\cdot\vec A.
$$

Vector này đồng thời mô tả độ lớn diện tích và hướng của mặt trong không gian.

### Mặt phẳng trong điện trường đều

Thay vector vận tốc bằng vector điện trường để định nghĩa **điện thông**, ký hiệu $\Phi_E$, đọc là phi với chỉ số E. Với mặt phẳng diện tích A và điện trường đều:

$$
\Phi_E=EA\cos\varphi.
\tag{22.1}
$$

Ở đây φ là góc giữa trường và pháp tuyến đã chọn, không phải góc giữa trường và mặt phẳng. Các dạng tương đương là:

$$
\Phi_E=E_\perp A.
\tag{22.2}
$$

$$
\Phi_E=\vec E\cdot\vec A.
\tag{22.3}
$$

Diện tích lớn hơn có nhiều đường sức xuyên qua hơn. Với cùng diện tích và hướng, trường mạnh hơn cũng có nhiều đường sức hơn. Đây là cách hình dung điện thông, không phải phép đếm số đường sức có ý nghĩa tuyệt đối.

![Hình 22.6: Điện thông phụ thuộc góc giữa điện trường và vector diện tích](../img/young-22/hinh-22-6.png)

**Hình 22.6:** (a) Mặt hướng chính diện với trường, φ = 0, điện thông bằng EA. (b) Mặt nghiêng có điện thông EA cosφ. (c) Mặt nằm dọc trường, φ = 90°, điện thông bằng không.

Đơn vị SI của điện thông là $\mathrm{N\,m^2/C}$. Viết vector diện tích qua pháp tuyến đơn vị $\hat{\mathbf n}$:

$$
\vec A=A\hat{\mathbf n}.
\tag{22.4}
$$

Mỗi mặt phẳng có hai hướng pháp tuyến đối nhau, vì vậy phải nói rõ hướng đã chọn. Với **mặt kín**, quy ước luôn chọn pháp tuyến **hướng ra ngoài** thể tích được bao. Trường hướng ra cho điện thông dương, trường hướng vào cho điện thông âm.

### Mặt cong hoặc điện trường không đều

Khi trường thay đổi theo vị trí hoặc mặt bị cong, không thể lấy một giá trị E nhân với toàn diện tích. Chia mặt thành các phần rất nhỏ. Mỗi phần có diện tích dA và vector diện tích $d\vec A=\hat{\mathbf n}\,dA$. Trên phần nhỏ đó, điện thông là tích vô hướng của trường tại phần ấy với vector diện tích.

Với ba phần nhỏ để hình dung, tổng gần đúng là:

$$
\begin{aligned}
\Phi_E&\approx E_{\perp1}\Delta A_1\\
&\quad+E_{\perp2}\Delta A_2\\
&\quad+E_{\perp3}\Delta A_3.
\end{aligned}
$$

Chia ngày càng mịn rồi lấy giới hạn cho tích phân mặt:

$$
\begin{aligned}
\Phi_E&=\int_A E_\perp\,dA\\
&=\int_A\vec E\cdot d\vec A.
\end{aligned}
\tag{22.5}
$$

Với $E_\perp=E\cos\varphi$, cách viết thứ ba là tích phân $\int_A E\cos\varphi\,dA$.

Ba cách viết là cùng một đại lượng. Tùy hình học, một dạng có thể thuận tiện hơn các dạng còn lại. Tích phân cũng bằng giá trị trung bình có dấu của thành phần trường vuông góc mặt nhân với diện tích mặt.

### Ví dụ 22.1: Điện thông qua một đĩa

Đĩa bán kính 0,10 m có pháp tuyến đơn vị hợp góc 30° với điện trường đều $E=2.0\times10^3$ N/C. (a) Tìm điện thông. (b) Điện thông bằng bao nhiêu nếu quay đĩa để pháp tuyến vuông góc trường? (c) Nếu pháp tuyến cùng chiều trường thì sao?

![Hình 22.7: Pháp tuyến đĩa hợp góc 30 độ với điện trường](../img/young-22/hinh-22-7.png)

::: solution Chi tiết
**Xác định và thiết lập.** Mặt phẳng trong trường đều cho phép dùng (22.1). Đĩa không phải mặt kín, nên không có hướng “ra ngoài” mặc định. Hướng pháp tuyến đã được chỉ trong hình.

**Thực hiện.** Diện tích đĩa là $A=\pi(0.10)^2=0.0314$ m².

$$
\begin{aligned}
\Phi_{Ea}&=(2.0\times10^3)(0.0314)\cos30^\circ\\
&\approx54\,\mathrm{N\,m^2/C},\\
\Phi_{Eb}&=EA\cos90^\circ=0,\\
\Phi_{Ec}&=EA\cos0^\circ\\
&\approx63\,\mathrm{N\,m^2/C}.
\end{aligned}
$$

**Đánh giá.** Điện thông ở (b) nhỏ nhất, ở (c) lớn nhất. Cùng diện tích, chỉ thành phần trường vuông góc mặt góp phần vào điện thông.
:::

### Ứng dụng: Nước đi qua miệng cá nhám phơi

Khác cá mập trắng săn mồi, cá nhám phơi thu sinh vật phù du từ nước đi qua mang khi bơi. Miệng có thể rộng đến một mét, cho phép thông lượng nước rất lớn. Tích của tốc độ bơi với diện tích miệng có thể đạt khoảng 0,5 m³/s, tức 500 lít mỗi giây hoặc gần $5\times10^5$ gallon mỗi giờ. Tương tự, điện thông phụ thuộc độ lớn trường, diện tích và hướng tương đối giữa trường với mặt.

![Cá nhám phơi mở miệng để nước mang sinh vật phù du đi qua](../img/young-22/ung-dung-ca-nham.png)

### Ví dụ 22.2: Điện thông qua một lập phương

Một mặt lập phương tưởng tượng cạnh L nằm trong điện trường đều $\vec E$. Tìm điện thông qua từng mặt và qua toàn lập phương khi (a) hai mặt vuông góc trường và (b) lập phương quay góc θ quanh trục đứng.

![Hình 22.8: Các pháp tuyến ra ngoài của lập phương trước và sau khi quay](../img/young-22/hinh-22-8.png)

::: solution Chi tiết
**Xác định và thiết lập.** Mỗi mặt là phẳng, trường đều và diện tích bằng L². Dùng tích vô hướng với pháp tuyến ra ngoài cho từng mặt, rồi cộng sáu điện thông.

(a) Trường đi vào mặt 1, đi ra mặt 2 và song song bốn mặt còn lại:

$$
\begin{aligned}
\Phi_{E1}&=EL^2\cos180^\circ=-EL^2,\\
\Phi_{E2}&=EL^2\cos0^\circ=+EL^2,\\
\Phi_{E3}&=\Phi_{E4}=0,\\
\Phi_{E5}&=\Phi_{E6}=0.
\end{aligned}
$$

Điện thông tổng là:

$$
\begin{aligned}
\Phi_E&=\Phi_{E1}+\Phi_{E2}\\
&\quad+\Phi_{E3}+\Phi_{E4}\\
&\quad+\Phi_{E5}+\Phi_{E6}\\
&=(-EL^2+EL^2)\\
&\quad+(0+0)+(0+0)\\
&=0.
\end{aligned}
$$

(b) Sau khi quay, trường đi vào mặt 1 và 3, đi ra mặt 2 và 4. Các góc tương ứng là 180° − θ, θ, 90° + θ và 90° − θ:

$$
\begin{aligned}
\Phi_{E1}&=-EL^2\cos\theta,\\
\Phi_{E2}&=+EL^2\cos\theta,\\
\Phi_{E3}&=-EL^2\sin\theta,\\
\Phi_{E4}&=+EL^2\sin\theta,\\
\Phi_{E5}&=\Phi_{E6}=0.
\end{aligned}
$$

Từng cặp triệt tiêu, nên tổng vẫn bằng không. Đây là kết quả đã thấy ở Hình 22.3c. Khi tính điện thông qua mặt kín, phải giữ quy ước pháp tuyến ra ngoài ở tất cả các phần mặt.
:::

### Ví dụ 22.3: Điện thông qua một mặt cầu

Điện tích điểm $q=+3.0\,\mu\mathrm C$ ở tâm mặt cầu tưởng tượng bán kính $r=0.20$ m. Tìm điện thông qua mặt cầu.

![Hình 22.9: Trường và vector diện tích cùng hướng ra ngoài trên mặt cầu tâm tại nguồn](../img/young-22/hinh-22-9.png)

::: solution Chi tiết
**Xác định và thiết lập.** Mặt cong và hướng trường thay đổi nên dùng tích phân mặt (22.5). Tuy vậy, ở từng điểm trường luôn vuông góc mặt và hướng ra ngoài. Do đó $E_\perp=E$. Khoảng cách đến nguồn bằng nhau nên độ lớn E không đổi trên mặt cầu.

**Thực hiện.** Đưa E ra ngoài tích phân rồi lấy diện tích cầu:

$$
\begin{aligned}
\Phi_E&=E\int_A dA\\
&=\frac{q}{4\pi\varepsilon_0r^2}(4\pi r^2)\\
&=\frac q{\varepsilon_0}\\
&\approx3.4\times10^5\,\mathrm{N\,m^2/C}.
\end{aligned}
$$

**Đánh giá.** Bán kính triệt tiêu. Mặt cầu bán kính 2,0 m hoặc 200 m cũng có điện thông như vậy. Đối xứng của nguồn và mặt làm tích phân đơn giản. Quan hệ không phụ thuộc kích thước còn đúng cho mặt kín khác hình dạng, như sẽ được chứng minh ngay sau đây. Các bài biến thể của ví dụ nằm trong phần luyện tập cuối chương.
:::

::: exercise Câu hỏi ôn lại mục 22.2
Xếp bốn mặt sau theo điện thông từ dương nhất đến âm nhất. Đơn vị vector diện tích là m² và đơn vị trường là N/C:

- (i) Mặt chữ nhật có $\vec A=6\hat{\mathbf i}$ và $\vec E=4\hat{\mathbf j}$.
- (ii) Mặt tròn có $\vec A=3\hat{\mathbf j}$ và $\vec E=4\hat{\mathbf i}+2\hat{\mathbf j}$.
- (iii) Mặt vuông có $\vec A=3\hat{\mathbf i}+7\hat{\mathbf j}$ và $\vec E=4\hat{\mathbf i}-2\hat{\mathbf j}$.
- (iv) Mặt bầu dục có $\vec A=3\hat{\mathbf i}-7\hat{\mathbf j}$ và cùng trường như (iii).
:::

::: solution Giải thích
Tích vô hướng hai vector đơn vị cùng trục bằng 1, khác trục bằng không. Các điện thông tương ứng là 0, 6, −2 và 26 N m²/C. Vì vậy thứ tự là **(iv), (ii), (i), (iii)**. Hình dạng đường biên không thay thế được thông tin về vector diện tích và hướng trường.
:::
