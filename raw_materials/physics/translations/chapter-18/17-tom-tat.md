## Tổng kết chương 18

### Phương trình trạng thái

Phương trình trạng thái liên hệ áp suất $p$, thể tích $V$ và nhiệt độ tuyệt đối $T$ của một lượng chất xác định. Nó mô tả các trạng thái cân bằng, trong đó áp suất và nhiệt độ được xác định đồng đều theo mô hình đang dùng.

Với khí lý tưởng:

$$
pV=nRT.
$$

Hằng số khí $R$ giống nhau đối với mọi loại khí lý tưởng. Khi dùng SI, áp suất tính bằng pascal, thể tích bằng mét khối, nhiệt độ bằng kelvin và $n$ bằng mol.

![Sơ đồ tổng kết 18.1: Các đường đẳng nhiệt của khí lý tưởng trên giản đồ áp suất và thể tích.](./img/young-18/b-tom-tat-18-01.png)

### Lượng chất và khối lượng phân tử

Khối lượng mol $M$ là khối lượng trên một mol chất. Với $n$ mol:

$$
m_{\mathrm{tổng}}=nM.
$$

Hằng số Avogadro $N_A$ cho số thực thể trên một mol. Nếu $m$ là khối lượng một phân tử:

$$
\begin{aligned}
M &= N_Am, \\
N &= nN_A.
\end{aligned}
$$

Phải phân biệt $M$ với $m$, đồng thời phân biệt số mol $n$ với số phân tử $N$.

![Sơ đồ tổng kết 18.2: Cấu trúc vi mô của một chất có thể gồm các ion sắp xếp thành mạng, như natri clorua.](./img/young-18/b-tom-tat-18-02.png)

### Mô hình động học phân tử

Áp suất khí xuất phát từ trao đổi động lượng giữa các phân tử và thành bình. Với khí lý tưởng cân bằng có chuyển động đẳng hướng:

$$
pV=\frac23K_{\mathrm{tr}}.
$$

Tổng động năng tịnh tiến và động năng tịnh tiến trung bình của một phân tử:

$$
\begin{aligned}
K_{\mathrm{tr}}&=\frac32nRT,\\
\overline K&=\frac32kT.
\end{aligned}
$$

Hằng số Boltzmann $k=R/N_A$. Phương trình khí lý tưởng theo số phân tử là:

$$
pV=NkT.
$$

Tốc độ căn quân phương:

$$
\begin{aligned}
v_{\mathrm{rms}} &= \sqrt{\frac{3kT}{m}} \\
&= \sqrt{\frac{3RT}{M}}.
\end{aligned}
$$

Ở cùng nhiệt độ, động năng tịnh tiến trung bình mỗi phân tử bằng nhau, nhưng phân tử nhẹ chuyển động nhanh hơn về tốc độ căn quân phương.

![Sơ đồ tổng kết 18.3: Va chạm đàn hồi với thành bình đảo chiều thành phần vận tốc vuông góc thành.](./img/young-18/b-tom-tat-18-03.png)

Với mô hình phân tử cầu cứng bán kính $r$, tiết diện va chạm là $\sigma=4\pi r^2$ và mật độ số là $\nu=N/V$. Quãng đường tự do trung bình:

$$
\lambda=\frac{1}{\sqrt2\,\nu\sigma}.
$$

Thời gian tự do trung bình trong xấp xỉ dùng tốc độ $v$:

$$
\tau=\frac{\lambda}{v}.
$$

### Nhiệt dung và các bậc tự do

Trong miền mà các bậc tự do tương ứng được kích hoạt và mô hình cổ điển phân bố đều năng lượng phù hợp:

- Khí lý tưởng đơn nguyên tử có $C_V=3R/2$.
- Khí lý tưởng lưỡng nguyên tử, có tịnh tiến và hai bậc tự do quay nhưng chưa có đóng góp dao động đáng kể, có $C_V=5R/2$.
- Chất rắn đơn nguyên tử trong giới hạn nhiệt độ đủ cao của mô hình dao động cổ điển có nhiệt dung mol xấp xỉ $3R$.

Các giá trị này gắn với mô hình và miền nhiệt độ, không phải những hằng số áp dụng cho mọi chất ở mọi nhiệt độ. Khi nhiệt độ thấp, một số bậc tự do bị đóng băng lượng tử và nhiệt dung giảm.

![Sơ đồ tổng kết 18.4: Nhiệt dung hydro thay đổi khi các bậc tự do tịnh tiến, quay và dao động lần lượt tham gia.](./img/young-18/b-tom-tat-18-04.png)

### Phân bố tốc độ Maxwell–Boltzmann

Hàm $f(v)$ là mật độ phân bố tốc độ. Tỉ phần phân tử có tốc độ trong khoảng từ $v$ đến $v+dv$ xấp xỉ $f(v)dv$. Toàn bộ phân bố được chuẩn hóa:

$$
\int_0^\infty f(v)\,dv=1.
$$

Đặt $b=m/(2kT)$ và hệ số chuẩn hóa $A=4b^{3/2}/\sqrt\pi$. Phân bố có dạng:

$$
f(v)=Av^2e^{-bv^2}.
$$

Miền tốc độ là $v\ge0$.

Tỉ phần có tốc độ từ $v_1$ đến $v_2$ là:

$$
P_{12}=\int_{v_1}^{v_2}f(v)\,dv.
$$

Muốn tìm số phân tử trong khoảng đó, nhân $P_{12}$ với tổng số phân tử $N$.

![Sơ đồ tổng kết 18.5: Diện tích dưới đường phân bố trên một khoảng tốc độ cho tỉ phần phân tử trong khoảng đó.](./img/young-18/b-tom-tat-18-05.png)

### Pha và cân bằng pha

Giản đồ pha biểu diễn các miền áp suất và nhiệt độ mà pha rắn, lỏng hoặc hơi bền. Các đường biên cho điều kiện hai pha cùng tồn tại cân bằng. Tại điểm ba, cả ba pha có thể cùng tồn tại.

Đường hóa hơi kết thúc ở điểm tới hạn. Khi tiến đến điểm này, sự khác biệt giữa pha lỏng và pha hơi giảm dần rồi mất đi. Ở miền vượt điểm tới hạn, có thể đi liên tục giữa các tính chất kiểu khí và kiểu lỏng mà không qua một đường cân bằng hai pha.

![Sơ đồ tổng kết 18.6: Các miền pha, các đường nóng chảy, thăng hoa, hóa hơi, điểm ba và điểm tới hạn.](./img/young-18/b-tom-tat-18-06.png)
