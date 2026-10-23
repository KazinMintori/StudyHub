### Bài tập cầu nối

Một thanh đồng đặc, đồng tính, nằm ngang có chiều dài ban đầu $l_0$, diện tích tiết diện ngang $A$, suất Young $Y$, suất khối $B$, suất trượt $S$, và khối lượng $m$. Thanh được đỡ bởi một khớp quay không ma sát ở đầu bên phải và bởi một sợi dây cáp gắn tại điểm cách đầu bên trái của thanh một khoảng $l_0/4$ (Hình 11.21). Cả khớp quay và dây cáp đều được gắn sao cho lực của chúng phân bố đều trên toàn bộ tiết diện ngang của thanh. Dây cáp hợp với thanh một góc $\theta$ và nén thanh lại.

a) Tìm lực căng của dây cáp.

b) Tìm độ lớn và hướng của lực do khớp quay tác dụng lên đầu bên phải của thanh. Độ lớn này so với lực căng dây cáp như thế nào? Góc tạo bởi lực khớp quay so với phương ngang như thế nào khi so sánh với góc $\theta$?

c) Tìm độ thay đổi chiều dài của thanh do các ứng suất gây ra bởi dây cáp và khớp quay tác dụng lên thanh. (Biết độ thay đổi chiều dài là rất nhỏ so với chiều dài ban đầu $l_0$).

d) Kết quả ở câu (c) sẽ tăng lên theo hệ số nào nếu thanh đồng đặc dài gấp đôi nhưng có cùng diện tích tiết diện ngang?

![Hình 11.21: Sơ đồ thanh đồng chịu lực căng dây cáp và đỡ bởi khớp quay.](./img/young-11/c-fig-11-21.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Thanh đồng đồng chất dài $l_0$, tiết diện A, khối lượng m. Bản lề ở đầu phải. Dây buộc cách đầu trái $l_0/4$, kéo lên phải, hợp phương ngang góc θ. Các môđun Y, B, S đã cho, biến dạng nhỏ.

**Hướng đi:**

1. Vẽ trọng lực tại giữa thanh, lực căng tại điểm buộc và lực bản lề ở đầu phải. Giữ đúng điểm đặt để lập mômen.
2. Chọn ẩn là T, hai thành phần lực bản lề, góc lực và độ thay đổi chiều dài. Chỉ ba đại lượng lực cần giải từ cân bằng.
3. Dùng cân bằng lực, mômen và quan hệ nén dọc trục theo Y. B không dùng vì thanh không bị nén đều mọi phía. S không trực tiếp cho độ biến dạng dọc trục.
4. Lấy mômen quanh bản lề để loại lực bản lề, rồi cân bằng theo hai phương.
5. So sánh lực qua các thành phần lượng giác và so sánh góc qua hàm tang trong miền góc nhọn.
6. Kiểm tra tổng lực nâng bằng trọng lượng và xác định đúng đoạn thanh chịu nén. Thanh có thể chịu uốn, nhưng ở đây tính phần đổi chiều dài do ứng suất dọc trục trong mô hình biến dạng nhỏ.

**Lời giải chi tiết:**

(a) Chọn chiều ngược kim đồng hồ là dương. Trọng lực cách bản lề $l_0/2$ gây mômen dương. Thành phần đứng của dây cách bản lề $3l_0/4$ gây mômen âm:

$$
mg\frac{l_0}{2}-T\sin\theta\frac{3l_0}{4}=0.
$$

Vậy:

$$
T=\frac{2mg}{3\sin\theta}.
$$

(b) Chọn x sang phải, y lên trên. Cân bằng lực cho:

$$
\begin{aligned}
&F_x+T\cos\theta=0,\\
&F_y+T\sin\theta-mg=0.
\end{aligned}
$$

Thành phần ngang $F_x=-2mg/(3\tan\theta)$ hướng trái. Thành phần đứng $F_y=mg/3$ hướng lên. Lực bản lề có độ lớn:

$$
F=\frac{mg}{3}\sqrt{1+4\cot^2\theta}.
$$

Có thể so sánh với lực căng bằng tỉ số:

$$
\frac FT=\sqrt{\cos^2\theta+\tfrac14\sin^2\theta}.
$$

Với $0<\theta<90^\circ$, tỉ số nhỏ hơn 1, nên $F<T$. Gọi φ là góc lực bản lề hợp với phương ngang hướng trái. Khi đó:

$$
\tan\phi=\frac{F_y}{|F_x|}=\frac12\tan\theta.
$$

Hàm tang tăng trong miền góc nhọn, vì vậy $\phi<\theta$.

(c) Đoạn từ đầu trái tới điểm buộc dây không chịu lực nén dọc trục. Đoạn từ điểm buộc tới bản lề có chiều dài $l_c=3l_0/4$, chịu lực nén có độ lớn:

$$
P=T\cos\theta=\frac{2mg}{3}\cot\theta.
$$

Ứng suất pháp trên đoạn này là $P/A$. Quan hệ biến dạng dọc trục cho độ thay đổi chiều dài có dấu:

$$
\Delta l=-\frac{Pl_c}{AY}.
$$

Dấu âm biểu thị co ngắn. Thay P và $l_c$:

$$
\Delta l=-\frac{mgl_0}{2AY}\cot\theta.
$$

Độ co ngắn là $|\Delta l|=mgl_0\cot\theta/(2AY)$. Không dùng toàn bộ $l_0$ làm chiều dài chịu nén, vì phần bên trái điểm buộc không truyền lực dọc trục.

(d) Cùng vật liệu và tiết diện, tăng chiều dài hai lần làm khối lượng tăng hai lần. Trong công thức biến dạng, cả m lẫn $l_0$ đều tăng hai lần, nên:

$$
|\Delta l'|=4|\Delta l|.
$$

Kết quả giả thiết góc dây giữ nguyên và biến dạng vẫn nhỏ.

Cuối cùng, dây đỡ $T\sin\theta=2mg/3$, bản lề đỡ $mg/3$. Tổng đúng bằng mg. Dây gánh phần lớn tải vì điểm buộc gần khối tâm hơn so với bản lề, nên cần lực đứng lớn hơn để cân bằng mômen.

</details>
