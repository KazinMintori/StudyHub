### Bài tập cầu nối: Tốc độ trên quỹ đạo elip

Một sao chổi quay quanh Mặt Trời có khối lượng $m_S$, trên quỹ đạo elip có bán trục lớn $a$ và độ lệch tâm $e$.

(a) Tìm biểu thức tốc độ của sao chổi ở cận nhật và viễn nhật.

(b) Tính các tốc độ này cho sao chổi Halley, rồi tìm động năng, thế năng hấp dẫn và cơ năng toàn phần của sao chổi tại hai vị trí ấy. Khối lượng Halley là $2{,}2\times10^{14}\,\mathrm{kg}$. Các khoảng cách trong Ví dụ 13.9 là $8{,}80\times10^7\,\mathrm{km}$ ở cận nhật và $5{,}25\times10^9\,\mathrm{km}$ ở viễn nhật.

#### Các bước hướng dẫn

1. Phác họa tình huống, ghi mọi kích thước cần thiết và đánh dấu cận nhật, viễn nhật. Có thể dùng Hình 13.18 để xác định hình học quỹ đạo.
2. Liệt kê các đại lượng chưa biết và xác định những đại lượng cần tìm.
3. Giải thích vì sao cơ năng được bảo toàn khi sao chổi quay quanh Mặt Trời. Còn đại lượng nào được bảo toàn dọc quỹ đạo? Xét kết quả ở Mục 13.5.
4. Lập ít nhất hai phương trình chứa hai tốc độ chưa biết. Viết các khoảng cách Mặt Trời–sao chổi ở cận nhật và viễn nhật theo hình học của Hình 13.18.
5. Giải hệ để tìm hai tốc độ. So sánh kết quả, xác định tốc độ nào nhỏ hơn và giải thích tính hợp lý của kết luận.
6. Dùng kết quả ở bước 5 để tính hai tốc độ của Halley. Có thể dùng dữ liệu thiên văn ở Phụ lục F.
7. Dùng hai tốc độ để tính động năng, thế năng hấp dẫn và tổng cơ năng của Halley ở cả cận nhật lẫn viễn nhật.
8. Kiểm tra các công thức tốc độ ở phần (a) trong trường hợp riêng quỹ đạo tròn, $e=0$.
9. So sánh hai cơ năng tính ở phần (b). Giải thích vì sao chúng bằng nhau và ý nghĩa của dấu âm.

![Hình 13.18: Mặt Trời ở một tiêu điểm của elip. Hai khoảng cách cực trị bằng a(1 − e) và a(1 + e)](/vat-ly-1/bai-giang/img/young-13/r-theory-13-18.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Gọi khối lượng sao chổi là $m$, tốc độ ở cận nhật và viễn nhật lần lượt là $v_p$, $v_a$. Cần biểu diễn hai tốc độ theo $G$, $m_S$, $a$, $e$, rồi tính ba dạng năng lượng tại hai đầu quỹ đạo Halley.

Xét $0\le e<1$, coi Mặt Trời đứng yên vì $m\ll m_S$. Bỏ qua tương tác với các thiên thể khác và lấy mốc thế năng tại vô cực.

**Hướng đi:**

- Dùng hình học elip để xác định $r_p=a(1-e)$ và $r_a=a(1+e)$.
- Dùng bảo toàn cơ năng vì lực hấp dẫn là lực thế. Đây là phương trình thứ nhất nối hai tốc độ.
- Dùng bảo toàn mômen động lượng vì lực hút luôn dọc bán kính nên mômen lực đối với Mặt Trời bằng không. Tại hai đầu trục lớn, vận tốc vuông góc bán kính, cho phương trình thứ hai.
- Sau khi tìm tốc độ, tính $K=mv^2/2$ và $U=-Gm_Sm/r$ tại từng vị trí. So sánh tổng $K+U$ ở hai vị trí và xét giới hạn $e=0$.

**Lời giải:**

#### 1. Sơ đồ hình học và kích thước

Mặt Trời S ở một tiêu điểm, cách tâm hình học O một đoạn $ea$. Cận nhật P ở phía gần S, còn viễn nhật A ở đầu đối diện của trục lớn. Do đó,

$$
r_p=a(1-e),
$$

$$
r_a=a(1+e).
$$

![Sơ đồ phân tích: Vận tốc tiếp tuyến ở P (cận nhật) và A (viễn nhật), cùng các khoảng cách tới tiêu điểm S và tâm O](/vat-ly-1/bai-giang/img/young-13/solution-bridge-13-orbit.svg)

Các mũi tên vận tốc trong sơ đồ chỉ chiều tiếp tuyến. Không dùng chiều dài mũi tên để đọc một tỉ lệ tốc độ theo số đo trên hình.

#### 2. Các đại lượng cần tìm

Ở phần (a), hai ẩn cần xác định là $v_p$ và $v_a$. Ở phần (b), cần thêm $K_p$, $U_p$, $E_p$ tại cận nhật và $K_a$, $U_a$, $E_a$ tại viễn nhật. Các đại lượng $a$, $e$, $m_S$ đã cho hoặc suy ra từ hai khoảng cách của Halley.

#### 3. Hai định luật bảo toàn

Lực hấp dẫn không phụ thuộc thời gian và là lực thế, nên cơ năng của hệ Mặt Trời–sao chổi được bảo toàn trong mô hình này. Đặt $\mu=Gm_S$, rồi chia phương trình cơ năng cho khối lượng sao chổi:

$$
\frac12v_p^2-\frac{\mu}{r_p}=\frac12v_a^2-\frac{\mu}{r_a}.
$$

Lực còn là lực xuyên tâm. Vì vậy,

$$
\vec\tau=\vec r\times\vec F=\vec0.
$$

Mômen động lượng đối với S bảo toàn. Tại cận nhật và viễn nhật, vận tốc vuông góc với vector bán kính, nên

$$
mr_pv_p=mr_av_a.
$$

#### 4. Hệ phương trình cho hai tốc độ

Chia phương trình mômen động lượng cho khối lượng sao chổi, hệ cần giải trở thành

$$
\begin{aligned}
&v_p^2-v_a^2=2\mu\left(\frac1{r_p}-\frac1{r_a}\right),\\
&r_pv_p=r_av_a.
\end{aligned}
$$

Phương trình thứ hai cho

$$
v_a=\frac{r_p}{r_a}v_p.
$$

Thay vào phương trình thứ nhất:

$$
v_p^2\bigl(1-\frac{r_p^2}{r_a^2}\bigr)=\frac{2\mu(r_a-r_p)}{r_pr_a}.
$$

#### 5. Giải hệ và so sánh tốc độ

Trước hết xét $0<e<1$, khi đó $r_a>r_p$. Dùng hiệu hai bình phương ở vế trái rồi rút gọn thừa số $r_a-r_p$:

$$
v_p^2=\frac{2Gm_Sr_a}{r_p(r_a+r_p)}.
$$

Vì $r_a+r_p=2a$, suy ra

$$
v_p=\sqrt{\frac{Gm_S}{a}\frac{1+e}{1-e}}.
$$

Kết hợp với bảo toàn mômen động lượng,

$$
v_a=\sqrt{\frac{Gm_S}{a}\frac{1-e}{1+e}}.
$$

Cả hai căn được lấy dương vì đang xét tốc độ. Tỉ số hai tốc độ là

$$
\frac{v_p}{v_a}=\frac{1+e}{1-e}>1.
$$

Sao chổi nhanh hơn ở cận nhật và chậm hơn ở viễn nhật. Điều này phù hợp với việc thế năng thấp hơn khi ở gần Mặt Trời và cơ năng không đổi. Trường hợp tròn $e=0$ được xét riêng ở bước 8, không rút gọn một thừa số bằng không.

#### 6. Tốc độ của Halley ở hai đầu quỹ đạo

Đổi các khoảng cách sang mét:

$$
r_p=8{,}80\times10^{10}\,\mathrm m,
$$

$$
r_a=5{,}25\times10^{12}\,\mathrm m.
$$

Suy ra

$$
\begin{aligned}
a&=\frac{r_p+r_a}{2}\\
&=2{,}669\times10^{12}\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
e&=\frac{r_a-r_p}{r_a+r_p}\\
&\approx0{,}967029.
\end{aligned}
$$

Dùng $m_S=1{,}99\times10^{30}\,\mathrm{kg}$ và $G=6{,}67\times10^{-11}$ trong hệ SI. Đơn vị của $G$ là $\mathrm{N\,m^2/kg^2}$. Thay các giá trị chưa làm tròn vào biểu thức tốc độ:

$$
v_p\approx5{,}45\times10^4\,\mathrm{m/s},
$$

$$
v_a\approx9{,}13\times10^2\,\mathrm{m/s}.
$$

Tốc độ cận nhật lớn hơn khoảng $59{,}7$ lần tốc độ viễn nhật. Giữ thêm chữ số ở $e$ khi tính vì số nhỏ $1-e$ nằm trong mẫu của biểu thức $v_p$.

#### 7. Động năng, thế năng và cơ năng

Với $m=2{,}2\times10^{14}\,\mathrm{kg}$, dùng các tốc độ chưa làm tròn để tính động năng:

$$
K_p=\frac12mv_p^2\approx3{,}3\times10^{23}\,\mathrm J,
$$

$$
K_a=\frac12mv_a^2\approx9{,}2\times10^{19}\,\mathrm J.
$$

Thế năng tương tác của hệ tại mỗi vị trí là

$$
\begin{aligned}
U_p&=-\frac{Gm_Sm}{r_p}\\
&\approx-3{,}3\times10^{23}\,\mathrm J,
\end{aligned}
$$

$$
\begin{aligned}
U_a&=-\frac{Gm_Sm}{r_a}\\
&\approx-5{,}6\times10^{21}\,\mathrm J.
\end{aligned}
$$

Không lấy hai số đã làm tròn ở cận nhật để cộng, vì $K_p$ và $|U_p|$ rất gần nhau. Có thể rút biểu thức cơ năng trực tiếp trước khi thay số. Khi quy đồng động năng và thế năng về mẫu $2a(1-e)$, hệ số còn lại ở tử là $(1+e)-2=e-1$:

$$
\begin{aligned}
E_p&=\frac{\mu m(e-1)}{2a(1-e)}\\
&=-\frac{\mu m}{2a}.
\end{aligned}
$$

Ở viễn nhật cũng thu được

$$
E_a=-\frac{Gm_Sm}{2a}.
$$

Vì vậy,

$$
E_p=E_a\approx-5{,}5\times10^{21}\,\mathrm J.
$$

Khối lượng sao chổi được cho với hai chữ số có nghĩa, nên các năng lượng cuối được làm tròn tương ứng. Động năng và thế năng riêng lẻ thay đổi mạnh dọc quỹ đạo, còn tổng không đổi.

#### 8. Giới hạn quỹ đạo tròn

Khi $e=0$, hai khoảng cách đều bằng $a$. Từ điều kiện lực hướng tâm cho chuyển động tròn,

$$
v_p=v_a=\sqrt{\frac{Gm_S}{a}}.
$$

Hai biểu thức tốc độ elip cũng tiến tới cùng giá trị này khi $e\to0$. Như vậy kết quả phù hợp với công thức vận tốc quỹ đạo tròn.

#### 9. Ý nghĩa của cơ năng âm

Hai giá trị cơ năng bằng nhau vì hệ chỉ chịu tương tác hấp dẫn trong mô hình đang xét. Dấu âm gắn với mốc thế năng ở vô cực: Sao chổi chưa có đủ năng lượng để ra xa vô hạn.

Ở vô cực, $U\to0$ và động năng không thể âm. Trong khi đó, cơ năng hiện tại của Halley nhỏ hơn không, nên chuyển động bị giới hạn trên quỹ đạo liên kết. Muốn sao chổi vừa đủ thoát, cần tăng cơ năng ít nhất một lượng bằng $|E|$.

</details>
