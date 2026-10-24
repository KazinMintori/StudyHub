### Bài tập cầu nối: Lò xo không tuân theo định luật Hooke

Một lò xo treo thẳng đứng có khối lượng không đáng kể. Khi đầu dưới bị kéo xuống một đoạn $x$ so với vị trí không biến dạng, lò xo tác dụng lực hướng lên có độ lớn $ax^2$, với $a>0$. Ban đầu lò xo không biến dạng. Gắn vật khối lượng $m$ vào đầu dưới rồi thả nhẹ từ nghỉ. Vật rơi xuống và làm lò xo dãn ra như Hình 6.29.

(a) Tìm tốc độ khi vật đã rơi đoạn $x_1$. (b) Tìm công suất của lực lò xo tại đó. (c) Tìm độ dãn cực đại $x_2$. (d) Vật có ở lại vị trí đó không?

![Hình 6.29: Vật gắn vào lò xo phi tuyến rồi được thả từ vị trí lò xo không biến dạng, chiều dương hướng xuống](/vat-ly-1/bai-giang/img/young-06/r-exercises-fig-6-29.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Xét vật trong hệ gắn với điểm treo cố định. Lấy $x=0$ tại vị trí ban đầu và chiều dương hướng xuống. Vật có $v_0=0$, chịu trọng lực $mg$ hướng xuống và lực lò xo $ax^2$ hướng lên.

Bỏ qua lực cản, ta cần tìm $v_1$, công suất $P_1$, $x_2$ và trạng thái chuyển động tại $x_2$.

**Hướng đi:** Có thể triển khai lần lượt theo chín bước sau.

1. Lực lò xo thay đổi theo vị trí. Vì vậy cần tích phân công của lực này và dùng định lý động năng, thay cho công thức của lực không đổi.
2. Vẽ sơ đồ lực của riêng vật, với trọng lực hướng xuống và lực lò xo hướng lên. Trên trục tọa độ hướng xuống, đánh dấu $0$, $x_1$ và $x_2$.
3. Phân biệt các tham số đã biết $m$, $a$, $g$, $x_1$ với các ẩn $v_1$, $P_1$, $x_2$. Ở phần (d), cần tìm hướng của hợp lực tại $x_2$.
4. Tính công lò xo từ $0$ đến một độ dãn $x$ bằng tích phân của thành phần lực $-ax^2$. Xác định dấu công khi vật đang đi xuống.
5. Tính công trọng lực trên cùng đoạn. Trọng lực cùng chiều độ dời nên công này dương.
6. Cho tổng công bằng độ biến thiên động năng để tìm tốc độ. Dùng $P=F_xv_x$ để tìm công suất. Tại độ dãn cực đại, tốc độ bằng không.
7. Để xét vật có ở lại điểm thấp nhất không, tính hợp lực tại đó. Vận tốc bằng không tại một thời điểm chưa bảo đảm gia tốc bằng không.
8. So sánh tốc độ với kết quả rơi tự do $\sqrt{2gx_1}$. Kiểm tra dấu công suất bằng hướng lực lò xo so với vận tốc đi xuống.
9. Tìm vị trí cân bằng từ điều kiện hợp lực bằng không và so sánh với $x_2$. Hai vị trí này cần phù hợp với kết luận về việc vật có đổi chiều hay không.

![Sơ đồ lực và trục tọa độ của bài cầu nối: Lực lò xo hướng lên, trọng lực hướng xuống, các mốc 0, x1 và x2 theo chiều dương hướng xuống](/vat-ly-1/bai-giang/img/young-06/bridge-6-force-axis-solution.svg)

**Lời giải:** (a) Gọi $u$ là biến lấy tích phân để phân biệt với tọa độ cuối $x$. Công lò xo khi vật đi xuống từ $0$ đến $x$ là

$$
\begin{aligned}
W_s&=\int_0^x(-au^2)\,du\\
&=-\frac{ax^3}{3}.
\end{aligned}
$$

Công này âm với $x>0$. Công của trọng lực là

$$
W_g=mgx.
$$

Theo định lý động năng, từ trạng thái nghỉ,

$$
\frac12mv^2=mgx-\frac{ax^3}{3}.
$$

Vì vậy tốc độ tại $x_1$ là

$$
v_1=\sqrt{2gx_1-\frac{2ax_1^3}{3m}}.
$$

Biểu thức áp dụng tại các vị trí vật thực sự đi tới. Trên lượt đi xuống đầu tiên, miền ấy là $0\le x_1\le x_2$, với $x_2$ được xác định ở phần (c).

(b) Trên lượt đi xuống, thành phần vận tốc là $v_x=v_1\ge0$, còn thành phần lực lò xo là $-ax_1^2$. Do đó,

$$
P_1=-ax_1^2v_1.
$$

Thay tốc độ từ phần (a),

$$
P_1=-ax_1^2\sqrt{2gx_1-\frac{2ax_1^3}{3m}}.
$$

Công suất âm tại các điểm bên trong lượt đi xuống, vì lực lò xo ngược chiều vận tốc. Lò xo nhận năng lượng từ vật. Tại hai điểm có tốc độ bằng không, công suất tức thời bằng không. Khi vật quay lên qua cùng $x_1$, công suất lò xo đổi sang dấu dương.

(c) Ở điểm dãn cực đại, $v=0$. Động năng đầu và cuối đều bằng không, nên

$$
mgx_2-\frac{ax_2^3}{3}=0.
$$

Nghiệm $x_2=0$ chỉ là vị trí xuất phát. Với điểm dãn cực đại cần tìm, $x_2>0$, nên chia phương trình cho $x_2$:

$$
mg-\frac{ax_2^2}{3}=0.
$$

Suy ra

$$
x_2=\sqrt{\frac{3mg}{a}}.
$$

(d) Tại điểm này, độ lớn lực lò xo là $ax_2^2=3mg$. Hợp lực có thành phần

$$
F_{\mathrm{net},x}=mg-ax_2^2=-2mg.
$$

Gia tốc hướng lên:

$$
\ddot x=-2g.
$$

Vật chỉ dừng tức thời rồi đổi chiều đi lên. Nó không ở lại vị trí dãn cực đại. Trong mô hình không có lực cản, chuyển động tiếp tục qua lại.

Để kiểm tra kết quả ở phần (a), so sánh với rơi tự do. Với $0<x_1<x_2$, số hạng bị trừ trong căn dương nên

$$
0<v_1<\sqrt{2gx_1}.
$$

Lực lò xo làm tốc độ nhỏ hơn tốc độ rơi tự do trên cùng độ giảm độ cao. Trong giới hạn $a\to0$ tại $x_1$ cố định, công thức trở về tốc độ rơi tự do. Dấu âm của công suất ở phần (b) cũng phù hợp với lực lò xo hướng ngược chuyển động xuống.

Cuối cùng, vị trí cân bằng thỏa

$$
mg-ax_{\mathrm{eq}}^2=0.
$$

$$
x_{\mathrm{eq}}=\sqrt{\frac{mg}{a}}.
$$

So sánh với điểm dãn cực đại:

$$
x_2=\sqrt3\,x_{\mathrm{eq}}>x_{\mathrm{eq}}.
$$

Vật đi qua vị trí cân bằng khi vẫn đang có vận tốc hướng xuống, rồi mới dừng ở vị trí thấp hơn. Tại đó hợp lực hướng lên, nhất quán với việc vật đổi chiều thay vì đứng yên.

</details>
