### Bài tập cầu nối: Cú rơi của Green Lantern

Green Lantern bước khỏi đỉnh một tòa nhà cao và rơi tự do từ trạng thái nghỉ xuống đất. Trong 1,00 s cuối cùng, anh rơi hết một nửa tổng quãng đường từ đỉnh xuống đất, như Hình 2.30. Chiều cao h của tòa nhà bằng bao nhiêu?

![Hình 2.30: Green Lantern rơi từ trạng thái nghỉ và đi hết nửa chiều cao cuối cùng trong 1,00 s](/vat-ly-1/bai-giang/img/young-02/hinh-2-30.png)

#### Các câu hỏi hướng dẫn

1. Rơi tự do từ trạng thái nghỉ cho biết điều gì về gia tốc và vận tốc ban đầu?
2. Chọn chiều dương của trục y. Cách thuận tiện là chọn giống Mục 2.5 khi xét vật rơi tự do.
3. Chia chuyển động thành hai phần, từ đỉnh tới nửa chiều cao và từ đó xuống đất. Phần thứ hai kéo dài 1,00 s. Cần biết điều gì về chuyển động tại điểm giữa để tìm h? Chọn hai phương trình, một cho mỗi phần, để tìm h. Có thể có nhiều cách chọn.
4. Dùng hai phương trình để giải h. Vì chiều cao là số dương, kết quả phải dương.
5. Dùng công thức rơi tự do tìm thời gian từ đỉnh tới nửa chiều cao và từ đỉnh xuống đất. Nếu h đúng, thời gian thứ hai phải lớn hơn thời gian thứ nhất đúng 1,00 s. Nếu không, hãy xem lại phép giải.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vật rơi từ trạng thái nghỉ trong trọng trường không đổi, bỏ qua lực cản. Khoảng thời gian đi hết nửa chiều cao cuối là τ = 1,00 s. Tìm chiều cao dương h, với g = 9,80 m/s².

**Hướng đi:**

- Chọn trục y hướng lên và gốc tại đỉnh tòa nhà. Gia tốc có thành phần −g, còn tọa độ điểm giữa và mặt đất lần lượt là −h/2 và −h.
- Dùng hệ thức không chứa thời gian cho nửa đầu vì biết vận tốc đầu bằng không và muốn tìm vận tốc tại điểm giữa.
- Dùng công thức độ dời của chuyển động gia tốc không đổi cho nửa sau vì đã biết thời gian τ. Vận tốc đầu của phần này chính là vận tốc cuối của phần trước.
- Giải phương trình với điều kiện h > 0, rồi tính độc lập hai thời điểm để đối chiếu điều kiện chênh lệch 1,00 s.

**Lời giải:**

1. Rơi tự do cho gia tốc không đổi hướng xuống. Xuất phát nghỉ cho vận tốc đầu bằng không.

2. Với trục đã chọn, gia tốc là:

$$
a_y=-g.
$$

3. Gọi vận tốc tại điểm giữa là vₘ. Trong nửa đầu:

$$
v_m^2=2(-g)\left(-\frac h2\right)=gh.
$$

Vì vật đang đi xuống, chọn nghiệm âm:

$$
v_m=-\sqrt{gh}.
$$

Độ dời của nửa sau là −h/2. Áp dụng phương trình tọa độ với vận tốc đầu vₘ và khoảng thời gian τ:

$$
-\frac h2=v_m\tau-\frac12g\tau^2.
$$

Thay vₘ vào và đổi dấu:

$$
\frac h2=\sqrt{gh}\,\tau+\frac12g\tau^2.
$$

4. Đặt u là đại lượng có đơn vị thời gian:

$$
u=\sqrt{\frac hg}>0.
$$

Chia phương trình trước cho g rồi nhân với 2:

$$
u^2=2u\tau+\tau^2.
$$

Giải phương trình bậc hai:

$$
u=(1\pm\sqrt2)\tau.
$$

Nghiệm chứa dấu trừ âm, nên không thỏa u > 0. Vì vậy:

$$
u=(1+\sqrt2)\tau.
$$

Chiều cao là:

$$
\begin{aligned}
h&=gu^2\\
&=(1+\sqrt2)^2g\tau^2\\
&=(3+2\sqrt2)g\tau^2.
\end{aligned}
$$

Tích gτ² có đơn vị mét. Với τ = 1,00 s và g = 9,80 m/s²:

$$
\begin{aligned}
h&=(3+2\sqrt2)(9{,}80)\,\mathrm m\\
&\approx57{,}1\,\mathrm m.
\end{aligned}
$$

5. Gọi t₁ là thời gian từ đỉnh tới điểm giữa, còn T là tổng thời gian rơi. Từ h/2 = gt₁²/2:

$$
\begin{aligned}
t_1&=\sqrt{\frac hg}\\
&=(1+\sqrt2)\tau\\
&\approx2{,}414\,\mathrm s.
\end{aligned}
$$

Từ h = gT²/2:

$$
\begin{aligned}
T&=\sqrt{\frac{2h}{g}}\\
&=(2+\sqrt2)\tau\\
&\approx3{,}414\,\mathrm s.
\end{aligned}
$$

Do đó:

$$
T-t_1=\tau=1{,}00\,\mathrm s.
$$

Khoảng thời gian đi hết nửa chiều cao cuối đúng bằng dữ kiện. Tổng thời gian rơi lớn hơn thời gian từ đỉnh tới điểm giữa 1,00 s.

</details>
