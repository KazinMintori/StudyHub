## 10.7 Con quay và tiến động

Giữ trục một bánh đà nằm ngang và chỉ đỡ một đầu. Nếu bánh không quay, đầu tự do rơi xuống. Nếu bánh quay nhanh, trục có thể chuyển động tròn gần nằm ngang quanh điểm đỡ. Chuyển động đổi hướng của trục ấy gọi là **tiến động**.

![Hình 10.32: Đầu tự do của trục con quay đi vòng quanh điểm tựa trong khi bánh đà vẫn tự quay quanh trục riêng.](../img/young-10/b-hinh-10-32.png)

Không có sự triệt tiêu trọng lực. Ta phải phân tích tác dụng của mômen trọng lực lên một vectơ mômen động lượng đã có sẵn, thay vì chỉ dự đoán hướng chuyển động từ hướng trọng lực.

### Bánh đà không tự quay

Chọn mốc $O$ tại điểm tựa không ma sát. Trọng lượng $\vec w$ tác dụng tại khối tâm, cách $O$ một đoạn $r$. Lực từ điểm tựa có mômen bằng không đối với $O$, còn trọng lực có mômen:

$$
\vec\tau=\vec r\times\vec w.
$$

Trong khoảng thời gian $dt$, mômen động lượng đổi một lượng:

$$
d\vec L=\vec\tau\,dt. \tag{10.32}
$$

![Hình 10.33: Khi bánh chưa tự quay, mômen trọng lực làm xuất hiện mômen động lượng theo trục ngang và con quay đổ xuống.](../img/young-10/b-hinh-10-33.png)

Ban đầu $\vec L=0$. Mômen trọng lực làm tăng mômen động lượng theo trục mà bánh bắt đầu đổ quanh nó. Các gia số liên tiếp cùng hướng khiến bánh đổ nhanh dần, cho đến khi gặp mặt đỡ hoặc bàn.

### Bánh đà đang quay nhanh

Nếu bánh quay quanh trục đối xứng, mômen động lượng tự quay gần đúng là $\vec L=I\vec\omega$, cùng phương trục bánh. Khi trục nằm ngang, mômen trọng lực vuông góc với trục, nên $d\vec L$ gần vuông góc với $\vec L$.

![Hình 10.34: Mômen trọng lực vuông góc với mômen động lượng tự quay làm vectơ mômen động lượng đổi hướng.](../img/young-10/b-hinh-10-34.png)

Một biến thiên vuông góc làm vectơ đổi hướng mà không làm đổi độ lớn ở bậc vi phân. Cơ chế tương tự lực hướng tâm làm đổi hướng động lượng của vật chuyển động tròn đều. Trong so sánh này, thay lực bằng mômen lực và thay động lượng bằng mômen động lượng.

### Tốc độ góc tiến động

Gọi $d\phi$ là góc quay nhỏ của trục trong thời gian $dt$. Trong giới hạn tiến động chậm, độ lớn mômen động lượng chủ yếu do tự quay, nên $L\approx I\omega$. Từ hình học vectơ:

$$
d\phi=\frac{|d\vec L|}{L}.
$$

![Hình 10.35: Gia số mômen động lượng vuông góc với vectơ ban đầu tạo góc tiến động nhỏ.](../img/young-10/b-hinh-10-35.png)

Với trục nằm ngang, độ lớn mômen trọng lực là $\tau=mgr$. Do đó:

$$
\begin{aligned}
\Omega&=\frac{d\phi}{dt}\\
&=\frac{\tau}{L}\\
&=\frac{mgr}{I\omega}.
\end{aligned} \tag{10.33}
$$

$\omega$ là tốc độ tự quay của bánh đà, còn $\Omega$ là tốc độ trục quay quanh điểm tựa. Bánh tự quay càng nhanh thì tiến động càng chậm khi các đại lượng khác giữ nguyên. Nếu ma sát làm bánh chậm dần, công thức dự đoán $\Omega$ tăng trong miền xấp xỉ còn phù hợp.

Trong tiến động đều với trục nằm ngang, khối tâm đi theo đường tròn ngang. Lực đỡ phải có thành phần đứng cân bằng $mg$ và thành phần ngang cung cấp lực hướng tâm $m\Omega^2r$. Vì vậy, lực từ điểm tựa không chỉ có phương thẳng đứng.

### Điều kiện xấp xỉ và chương động

Mô hình vừa dùng bỏ qua phần mômen động lượng do chính chuyển động tiến động. Điều này hợp lý khi:

$$
\Omega\ll\omega.
$$

Nếu tiến động không đủ chậm, không thể coi toàn bộ mômen động lượng chỉ nằm dọc trục tự quay. Trục có thể dao động lên xuống cùng với tiến động. Dao động bổ sung ấy gọi là chương động. Nó có thể thấy rõ hơn khi bánh đà quay chậm đi.

Trục quay Trái Đất cũng đổi hướng chậm. Trong mô hình mô tả ở đây, một chu kỳ tiến động có bậc khoảng $26000$ năm. Mômen động lượng tự quay lớn và mômen hấp dẫn bên ngoài tương đối nhỏ giải thích tốc độ thay đổi hướng nhỏ. Con số này chỉ biểu thị thang thời gian của hiện tượng.

::: example Ví dụ 10.13: Bánh đà tiến động

Hình 10.36 biểu diễn con quay nhìn từ trên. Bánh là trụ đặc đồng chất bán kính $R=3{,}0\,\mathrm{cm}$, khối tâm cách điểm tựa $r=2{,}0\,\mathrm{cm}$. Khối lượng trục không đáng kể.

(a) Xác định chiều tiến động trong hình.

(b) Nếu một vòng tiến động mất $4{,}0\,\mathrm s$, tìm tốc độ tự quay của bánh.

![Hình 10.36: Sơ đồ nhìn từ trên và giản đồ vectơ dùng xác định chiều tiến động cùng tốc độ tự quay.](../img/young-10/b-hinh-10-36.png)

**Tóm tắt đề bài:** $I=mR^2/2$, chu kỳ tiến động $T_p=4{,}0\,\mathrm s$. Trọng lực hướng vào trang trong hình nhìn từ trên.

**Hướng đi:** Dùng quy tắc bàn tay phải xác định hướng $\vec L$ và $\vec\tau$ trước khi kết luận chiều quay của trục. Từ chu kỳ tìm $\Omega$, rồi đảo công thức tiến động chậm để tìm $\omega$.

**Lời giải:**

(a) Theo chiều tự quay vẽ trong hình, $\vec L$ hướng sang trái. Vectơ vị trí khối tâm hướng sang phải, còn trọng lực hướng vào trang, nên $\vec\tau$ hướng lên trên trang. Cộng gia số $d\vec L$ theo hướng đó làm trục tiến động theo chiều kim đồng hồ khi nhìn từ trên.

(b) Tốc độ tiến động:

$$
\Omega=\frac{2\pi}{T_p}\approx1{,}57\,\mathrm{rad/s}.
$$

Thay mômen quán tính của trụ đặc vào công thức tiến động:

$$
\omega=\frac{2gr}{R^2\Omega}.
$$

Dùng $g=9{,}80\,\mathrm{m/s^2}$, đổi hai độ dài sang mét, thu được $\omega\approx277\,\mathrm{rad/s}$. Với độ chính xác của dữ kiện, báo khoảng $280\,\mathrm{rad/s}$, tương đương $2600$ vòng/phút.

Tỷ số $\Omega/\omega\approx0{,}0057$, tức khoảng $0{,}6\%$. Vì vậy, ví dụ nằm trong miền tiến động chậm mà phép suy ra đã giả thiết.
:::

### Câu tự kiểm 10.7

Tăng gấp đôi khối lượng bánh đà ở Hình 10.34, nhưng giữ nguyên các kích thước và tốc độ tự quay. Tốc độ góc tiến động thay đổi thế nào?

- (i) Tăng bốn lần.
- (ii) Tăng hai lần.
- (iii) Không đổi.
- (iv) Giảm còn một nửa.
- (v) Giảm còn một phần tư.

<details><summary>Xem giải thích</summary>

Chọn (iii). Cùng hình dạng và kích thước làm $I$ tỷ lệ với khối lượng. Tăng khối lượng gấp đôi làm cả trọng lượng lẫn mômen quán tính tăng gấp đôi. Do đó, tỷ số $mgr/(I\omega)$ không đổi khi $r$ và $\omega$ giữ nguyên.

</details>
