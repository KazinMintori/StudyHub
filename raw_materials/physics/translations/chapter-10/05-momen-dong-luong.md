## 10.5 Mômen động lượng

Một quả bóng buộc dây có thể quay đều quanh tay dù vectơ động lượng của nó liên tục đổi hướng. Để mô tả sự chuyển động quanh một mốc, ta dùng mômen động lượng. Đại lượng này liên hệ với mômen lực theo cách động lượng liên hệ với hợp lực.

### Mômen động lượng của chất điểm

Với chất điểm có vectơ vị trí $\vec r$ đối với $O$ và động lượng $\vec p=m\vec v$, định nghĩa:

$$
\vec L=\vec r\times\vec p. \tag{10.24}
$$

Nếu $\phi$ là góc giữa $\vec r$ và $\vec v$, độ lớn:

$$
L=rmv\sin\phi=mvl. \tag{10.25}
$$

Ở đây, $l$ là khoảng cách vuông góc từ $O$ đến đường thẳng theo phương chuyển động của chất điểm tại thời điểm xét. Dùng quy tắc bàn tay phải để tìm chiều $\vec L$. Đơn vị là $\mathrm{kg\cdot m^2/s}$.

![Hình 10.23: Mômen động lượng của chất điểm vuông góc mặt phẳng chứa vectơ vị trí và động lượng.](../img/young-10/b-hinh-10-23.png)

Mômen động lượng phụ thuộc mốc $O$. Chất điểm không cần chuyển động tròn để có mômen động lượng. Một vật chuyển động thẳng vẫn có $L=mvl$ đối với một mốc nằm ngoài đường chuyển động.

### Mômen lực làm đổi mômen động lượng

Giữ mốc $O$ cố định trong hệ quán tính. Đặt $\vec A=d\vec r/dt$ và $\vec B=d\vec p/dt$. Quy tắc đạo hàm tích có hướng cho:

$$
\frac{d\vec L}{dt}=\vec A\times\vec p+\vec r\times\vec B.
$$

Số hạng đầu bằng không vì $\vec A=\vec v$ cùng phương với $\vec p=m\vec v$. Định luật II Newton cho $\vec B=\vec F$, nên:

$$
\frac{d\vec L}{dt}=\vec r\times\vec F=\vec\tau. \tag{10.26}
$$

Quan hệ này chỉ rõ vai trò của mômen ngoại lực. Muốn thay đổi vectơ mômen động lượng, cần một mômen tổng cộng khác không đối với cùng mốc đang dùng.

### Vật rắn quay quanh trục

Xét một lát mỏng vuông góc trục $z$ đi qua $O$. Phần tử $i$ cách trục $r_i$, chuyển động với tốc độ dài $r_i\omega_z$. Thành phần mômen động lượng của nó theo trục:

$$
L_{iz}=m_ir_i^2\omega_z. \tag{10.27}
$$

![Hình 10.24: Mỗi phần tử của lát mỏng đóng góp mômen động lượng theo trục quay.](../img/young-10/b-hinh-10-24.png)

Với hai phần tử, $L_z=L_{1z}+L_{2z}$. Với N phần tử, phép cộng đầy đủ là:

$$
L_z=L_{1z}+L_{2z}+\dots+L_{Nz}.
$$

Các phần tử cùng có vận tốc góc $\omega_z$, nên có thể đưa đại lượng này ra ngoài tổng:

$$
\begin{aligned}
L_z&=\sum_{i=1}^{N}L_{iz}\\
&=I\omega_z.
\end{aligned}
$$

Nếu vật đối xứng quanh trục quay, các thành phần mômen động lượng vuông góc trục triệt tiêu từng cặp. Khi ấy, cả vectơ mômen động lượng cùng phương với vectơ vận tốc góc:

$$
\vec L=I\vec\omega. \tag{10.28}
$$

![Hình 10.25: Hai phần tử đối xứng có các thành phần ngang của mômen động lượng đối nhau, còn các thành phần dọc trục cộng lại.](../img/young-10/b-hinh-10-25.png)

![Hình 10.26: Với trục đối xứng, quy tắc bàn tay phải cho cùng phương và chiều của vận tốc góc với mômen động lượng.](../img/young-10/b-hinh-10-26.png)

Không được áp dụng quan hệ vectơ này cho mọi trục của mọi vật. Nếu trục không phải trục đối xứng, $\vec L$ nói chung không song song với $\vec\omega$, dù thành phần theo trục vẫn là $L_z=I\omega_z$.

![Hình 10.27: Vật quay quanh trục không đối xứng có vectơ mômen động lượng lệch khỏi trục.](../img/young-10/b-hinh-10-27.png)

Khi vật như vậy quay với vận tốc góc không đổi về độ lớn, hướng $\vec L$ vẫn có thể đổi. Vì thế, vẫn cần mômen ngoại lực để duy trì kiểu chuyển động đó. Ở một bánh xe mất cân bằng, ổ trục phải cung cấp tác dụng này. Cân bằng bánh xe giúp trục quay trùng với trục quán tính thích hợp.

### Hệ nhiều phần và phương trình tổng quát

Với hai phần, tổng mômen động lượng là $\vec L=\vec L_1+\vec L_2$. Các mômen nội lực cùng đường nối triệt tiêu từng cặp khi cộng toàn hệ. Mở rộng phép cộng trên cho mọi phần tử, ta được:

$$
\sum\vec\tau_{\mathrm{ext}}=\frac{d\vec L}{dt}. \tag{10.29}
$$

Mômen ngoại lực và mômen động lượng phải được tính đối với cùng một mốc cố định trong hệ quán tính. Trong các bài quay quanh khối tâm, có thể dùng dạng tương ứng đối với khối tâm.

Nếu vật rắn quay quanh một trục đối xứng có phương không đổi và $I$ không đổi, đạo hàm $L_z=I\omega_z$ trở về $\sum\tau_z=I\alpha_z$. Với vật đổi hình, $I$ có thể thay đổi. Khi ấy, phương trình đạo hàm mômen động lượng vẫn dùng được nhưng không tự rút gọn thành $I\alpha_z$.

::: example Ví dụ 10.9: Mômen động lượng và mômen lực của quạt turbine

Quạt turbine có mômen quán tính $I=2{,}5\,\mathrm{kg\cdot m^2}$ quanh trục đối xứng. Khi khởi động, vận tốc góc là $\omega_z=At^2$, trong đó $A=40\,\mathrm{rad/s^3}$.

(a) Tìm mômen động lượng theo thời gian và tại $t=3{,}0\,\mathrm s$.

(b) Tìm mômen lực tổng cộng theo thời gian và tại thời điểm ấy.

**Tóm tắt đề bài:** $I$ và phương trục không đổi, nên chỉ cần thành phần theo trục $z$.

**Hướng đi:** Tính $L_z=I\omega_z$, rồi lấy đạo hàm theo thời gian để tìm mômen ngoại lực. Có thể kiểm tra bằng cách lấy đạo hàm vận tốc góc trước rồi nhân với $I$.

**Lời giải:**

$$
L_z=IAt^2.
$$

Hệ số $IA=100\,\mathrm{kg\cdot m^2/s^3}$. Tại $t=3{,}0\,\mathrm s$:

$$
L_z=900\,\mathrm{kg\cdot m^2/s}.
$$

Mômen ngoại lực:

$$
\tau_z=\frac{dL_z}{dt}=2IAt.
$$

Tại cùng thời điểm, $\tau_z=600\,\mathrm{N\cdot m}$. Mặt khác, $\alpha_z=2At$, nên $I\alpha_z$ cho đúng kết quả ấy.
:::

### Câu tự kiểm 10.5

Buộc bóng vào một đầu dây, giữ đầu kia và quay bóng theo đường tròn với tốc độ không đổi. Động lượng của bóng có không đổi không? Mômen động lượng đối với tay có không đổi không?

<details><summary>Xem giải thích</summary>

Động lượng không đổi về độ lớn nhưng liên tục đổi hướng, nên vectơ động lượng thay đổi. Trong mô hình quỹ đạo tròn phẳng và chỉ có hợp lực hướng tâm, mômen động lượng đối với tâm có độ lớn và hướng không đổi.

Lực hướng tâm khác không nhưng mômen đối với tâm bằng không, vì lực cùng đường với $\vec r$. Tình huống này phân biệt tác dụng làm đổi động lượng với tác dụng làm đổi mômen động lượng.

</details>
