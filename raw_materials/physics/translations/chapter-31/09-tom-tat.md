## Tổng kết chương

### Giản đồ pha và giá trị hiệu dụng

Nguồn xoay chiều hình sin tạo suất điện động thay đổi tuần hoàn. Vector pha quay ngược chiều kim đồng hồ với tốc độ góc bằng tần số góc của đại lượng. Hình chiếu ngang tại từng thời điểm cho giá trị tức thời.

![Tổng kết 31.1: Hình chiếu vector pha dòng lên trục ngang xác định dòng tức thời.](img/young-31/tom-tat-31-01-gian-do-pha.png)

Với biên độ dòng $I$ và biên độ điện áp $V$ hình sin:

$$
\begin{aligned}
I_{\mathrm{rav}} &= \frac2\pi I\approx0{,}637I, \\
I_{\mathrm{rms}} &= \frac I{\sqrt2}, \\
V_{\mathrm{rms}} &= \frac V{\sqrt2}.
\end{aligned}
$$

Dòng trung bình trước chỉnh lưu bằng không. Trung bình chỉnh lưu và hiệu dụng là hai đại lượng khác nhau.

### Pha điện áp so với dòng

Chọn dòng làm mốc pha:

$$
\begin{aligned}
i &= I\cos\omega t, \\
v &= V\cos(\omega t+\phi).
\end{aligned}
$$

![Tổng kết 31.2: Góc giữa vector điện áp và vector dòng xác định độ lệch pha, còn hình chiếu điện áp theo dòng quyết định công suất trung bình.](img/young-31/tom-tat-31-02-pha-dien-ap.png)

Góc dương nghĩa điện áp sớm dòng. Góc âm nghĩa điện áp trễ dòng.

### Điện trở và điện kháng

![Tổng kết 31.3: Ba mạch một phần tử minh họa điện trở, cuộn cảm và tụ chịu điện áp xoay chiều.](img/young-31/tom-tat-31-03-dien-khang.png)

Điện áp điện trở cùng pha dòng. Điện áp cuộn cảm thuần sớm 90 độ. Điện áp tụ thuần trễ 90 độ.

$$
\begin{aligned}
V_R &= IR, \\
V_L &= IX_L,\qquad X_L=\omega L, \\
V_C &= IX_C,\qquad X_C=\frac1{\omega C}.
\end{aligned}
$$

Các quan hệ biên độ trên cũng đúng khi đồng loạt đổi sang hiệu dụng. Quan hệ tức thời $v=iR$ chỉ áp dụng trực tiếp cho điện trở.

### Mạch RLC nối tiếp

![Tổng kết 31.4: Tam giác vector điện áp của mạch RLC có cạnh điện trở vuông góc cạnh điện kháng tổng.](img/young-31/tom-tat-31-04-mach-rlc.png)

Với điện kháng tổng $X=X_L-X_C$:

$$
\begin{aligned}
Z &= \sqrt{R^2+X^2}, \\
V &= IZ, \\
\tan\phi &= \frac XR.
\end{aligned}
$$

Điện áp tức thời nguồn bằng tổng ba điện áp tức thời. Biên độ nguồn là độ lớn tổng vector pha, không phải tổng số học ba biên độ.

### Công suất

![Tổng kết 31.5: Công suất tức thời có thể đổi dấu, nhưng giá trị trung bình phụ thuộc thành phần điện áp cùng pha dòng.](img/young-31/tom-tat-31-05-cong-suat.png)

$$
\begin{aligned}
p &= vi, \\
P_{\mathrm{av}} &= \frac12VI\cos\phi \\
&= V_{\mathrm{rms}}I_{\mathrm{rms}}\cos\phi.
\end{aligned}
$$

Hệ số công suất là $\cos\phi$. Với RLC nối tiếp, hệ số bằng $R/Z$. Điện trở tiêu tán công suất trung bình, còn cuộn cảm và tụ lý tưởng chỉ tích trữ rồi trả năng lượng.

### Cộng hưởng

![Tổng kết 31.6: Ba đường cộng hưởng có cùng vị trí đỉnh nhưng khác độ cao và độ rộng vì điện trở khác nhau.](img/young-31/tom-tat-31-06-cong-huong.png)

Với nguồn có biên độ cố định, dòng RLC nối tiếp lớn nhất tại

$$
\omega_0=\frac1{\sqrt{LC}}.
$$

Ở cộng hưởng, hai điện kháng bằng nhau, $Z=R$ và điện áp nguồn cùng pha dòng. Hai điện áp cuộn cảm và tụ bằng nhau về biên độ nhưng ngược pha, nên triệt tiêu trong tổng.

### Máy biến áp

![Tổng kết 31.7: Hai cuộn dùng chung từ thông trong lõi để đổi điện áp và dòng theo tỉ số số vòng.](img/young-31/tom-tat-31-07-may-bien-ap.png)

Với máy lý tưởng và mô hình tải thuần trở:

$$
\begin{aligned}
\frac{V_2}{V_1} &= \frac{N_2}{N_1}, \\
V_1I_1 &= V_2I_2.
\end{aligned}
$$

Điện áp và dòng phải cùng là biên độ hoặc cùng là hiệu dụng. Tăng điện áp đi kèm giảm dòng. Điện trở tải nhìn từ sơ cấp bằng điện trở thứ cấp chia bình phương tỉ số vòng thứ cấp trên sơ cấp.
