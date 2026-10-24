### Bài tập cầu nối: Lò xo và ma sát trên mặt phẳng nghiêng

Một kiện hàng khối lượng $2{,}00\,\mathrm{kg}$ được thả từ trạng thái nghỉ trên mặt phẳng nghiêng góc $53{,}1^\circ$, tại vị trí cách đầu một lò xo dài $4{,}00\,\mathrm m$. Lò xo có độ cứng $1{,}20\times10^2\,\mathrm{N/m}$, khối lượng không đáng kể và được gắn cố định ở chân dốc. Hệ số ma sát nghỉ và ma sát trượt lần lượt là $\mu_s=0{,}400$ và $\mu_k=0{,}200$.

(a) Độ nén cực đại của lò xo bằng bao nhiêu?
(b) Kiện hàng bật ngược lên dốc. Khi nó dừng lại lần tiếp theo, nó cách vị trí thả ban đầu bao nhiêu?
(c) Nội năng của hệ kiện hàng và mặt phẳng nghiêng thay đổi bao nhiêu từ lúc thả đến khi kiện hàng đạt độ cao cực đại sau khi bật lên?

![Hình 7.25: Kiện hàng trượt xuống mặt phẳng nghiêng và nén lò xo ở chân dốc.](/vat-ly-1/bai-giang/img/young-07/r-exercises-fig-7-25.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Khối lượng $m=2{,}00\,\mathrm{kg}$, góc nghiêng $\theta=53{,}1^\circ$, khoảng cách ban đầu $d=4{,}00\,\mathrm m$.

- Độ cứng $k=120\,\mathrm{N/m}$, hệ số ma sát nghỉ $\mu_s=0{,}400$, hệ số ma sát trượt $\mu_k=0{,}200$.

- Tìm độ nén lớn nhất $x$, khoảng cách từ điểm dừng mới đến điểm thả, và độ tăng nội năng $\Delta U_{\mathrm{int}}$.

**Hướng đi:**

- Dùng $\Delta K+\Delta U_g+\Delta U_{\mathrm{el}}=W_f$, vì lực đàn hồi biến đổi còn ma sát trượt làm cơ năng giảm. Giữa các điểm đang xét, kiện hàng đều có tốc độ bằng không.

- Dùng $n=mg\cos\theta$ và $f_k=\mu_k n$, vì không có gia tốc vuông góc mặt dốc và kiện hàng trượt trên dốc. Ma sát luôn ngược chiều trượt, nên đổi chiều khi kiện hàng bật lên.

- Dùng $\Delta U_{\mathrm{int}}=f_k s$ với tổng quãng đường trượt $s$, vì cơ năng mất đi do ma sát chuyển thành nội năng của hệ tiếp xúc.

Có thể tổ chức lời giải theo các bước sau:

1. Xác định trọng lực, lực đàn hồi, ma sát và lực pháp tuyến. Lực đàn hồi không phải lực không đổi, nên phương pháp năng lượng giúp tránh việc phải tích phân phương trình chuyển động. Cơ năng có bảo toàn trong bất kỳ giai đoạn trượt nào không? Vì sao?

2. Vẽ giản đồ lực khi kiện hàng trượt xuống và khi trượt lên. Chọn trục tọa độ. Nếu lấy gốc tại đầu lò xo không biến dạng, thế năng đàn hồi có dạng $kx^2/2$.

3. Đánh dấu ba trạng thái: Lúc thả, lúc lò xo nén cực đại và lúc kiện hàng đạt vị trí cao nhất sau khi bật lên. Ban đầu giả sử kiện hàng không còn tiếp xúc lò xo ở trạng thái cuối, rồi kiểm tra giả sử này.

4. Liệt kê các ẩn số và xác định đại lượng cần tìm.

5. Tìm độ lớn ma sát. Độ lớn này có phụ thuộc chiều chuyển động hay việc kiện hàng đang tiếp xúc với lò xo không? Chiều ma sát có phụ thuộc các điều đó không?

6. Viết phương trình năng lượng giữa hai trạng thái đầu và giải phương trình bậc hai cho độ nén. Chọn nghiệm dương vì độ nén không âm.

7. Viết phương trình năng lượng từ trạng thái nén cực đại đến trạng thái dừng sau khi bật lên để tìm quãng đường bật lên.

8. Tính độ tăng nội năng trên toàn hành trình xuống rồi lên. Độ tăng này bằng độ giảm cơ năng.

9. Kiểm tra giả sử kiện hàng đã rời lò xo trước khi đạt vị trí cao nhất sau khi bật lên.

10. Tính tổng công của ma sát trên cả hành trình và đối chiếu với độ tăng nội năng ở bước 8.

![Giản đồ lực của kiện hàng trong hai giai đoạn trượt xuống dốc và trượt lên dốc, với ma sát đổi chiều.](/vat-ly-1/bai-giang/img/young-07/r-exercises-bridge-force-diagrams.png)

**Lời giải:**

Chọn trục dọc mặt dốc hướng xuống, gốc tại đầu lò xo không biến dạng. Các vị trí đầu, nén cực đại và cuối lần bật lên lần lượt là $-d$, $x$ và $x-L$, trong đó $L$ là quãng đường bật lên từ vị trí nén cực đại. Chọn thế năng trọng trường bằng không ở gốc tọa độ.

Lực pháp tuyến và độ lớn ma sát trượt là:

$$
n=mg\cos\theta\approx11{,}8\,\mathrm N.
$$

$$
f_k=\mu_kmg\cos\theta\approx2{,}35\,\mathrm N.
$$

Hai đại lượng này không đổi khi kiện hàng đổi chiều hoặc tiếp xúc với lò xo, vì lực đàn hồi song song mặt dốc. Chiều ma sát đổi theo chiều trượt. Lực pháp tuyến không sinh công vì vuông góc độ dời.

(a) Trước hết, kiện hàng bắt đầu trượt vì $mg\sin\theta>\mu_smg\cos\theta$. Từ vị trí thả đến vị trí nén cực đại, động năng ở cả hai đầu bằng không. Do đó:

$$
\Delta U_g=-mg(d+x)\sin\theta.
$$

$$
\Delta U_{\mathrm{el}}=\frac12kx^2.
$$

$$
W_f=-f_k(d+x).
$$

$$
\Delta U_g+\Delta U_{\mathrm{el}}=W_f.
$$

Đặt $A=mg(\sin\theta-\mu_k\cos\theta)$. Với dữ kiện đã cho, $A\approx13{,}3\,\mathrm N$. Phương trình trở thành:

$$
\frac12kx^2=A(d+x).
$$

Nghiệm dương là:

$$
\begin{aligned}
x&=\frac{A+\sqrt{A^2+2kAd}}{k}\\
&\approx1{,}06\,\mathrm m.
\end{aligned}
$$

Nghiệm còn lại âm nên không biểu diễn độ nén ở trạng thái đang xét.

(b) Ở độ nén cực đại, lực lò xo hướng lên có độ lớn khoảng $127\,\mathrm N$. Trọng lực dọc dốc và ma sát nghỉ cực đại có độ lớn tổng cộng khoảng $20{,}4\,\mathrm N$. Lò xo thắng được cả hai, nên kiện hàng thực sự bật lên.

Trong giai đoạn bật lên, gọi $B=mg(\sin\theta+\mu_k\cos\theta)$, với $B\approx18{,}0\,\mathrm N$. Giả sử lò xo đã hết biến dạng khi kiện hàng đạt vị trí cao nhất. Phương trình năng lượng cho:

$$
\frac12kx^2=BL.
$$

Vế trái là thế năng đàn hồi ban đầu của giai đoạn bật lên. Nó được dùng để tăng thế năng trọng trường một lượng $mgL\sin\theta$ và thắng ma sát bằng công $f_kL$. Nó không phải toàn bộ cơ năng khi vẫn chọn mốc trọng trường tại đầu lò xo không biến dạng.

$$
\begin{aligned}
L&=\frac{kx^2}{2B}\\
&\approx3{,}74\,\mathrm m.
\end{aligned}
$$

Vì $L>x$, kiện hàng đã rời lò xo trước khi dừng, đúng với giả sử. Khoảng cách từ điểm dừng mới đến vị trí thả là:

$$
\begin{aligned}
\Delta s&=d+x-L\\
&\approx1{,}32\,\mathrm m.
\end{aligned}
$$

Đây là vị trí dừng tức thời của lần bật lên, không phải trạng thái nghỉ vĩnh viễn. Vì độ dốc đủ lớn, kiện hàng có thể trượt xuống lần nữa.

(c) Tổng quãng đường trượt đến thời điểm đang xét là $s=d+x+L$. Bởi vậy:

$$
\begin{aligned}
\Delta U_{\mathrm{int}}&=f_k(d+x+L)\\
&\approx20{,}7\,\mathrm J.
\end{aligned}
$$

Tổng công của ma sát bằng $-20{,}7\,\mathrm J$. Hai trạng thái đầu và cuối đều có động năng bằng không, lò xo đều không biến dạng, nên cơ năng giảm một lượng $mg\Delta s\sin\theta$. Đại lượng này cũng bằng khoảng $20{,}7\,\mathrm J$, phù hợp với độ tăng nội năng.

</details>
