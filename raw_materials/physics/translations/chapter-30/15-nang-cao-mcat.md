## Bài nâng cao

::: exercise 30.69
Một ống dây dài có $N_1$ vòng, bán kính $b$, bao quanh ống dây đồng trục hẹp hơn có $N_2$ vòng, bán kính $a<b$. Hai ống được nối ở đầu xa để dòng đi dọc cuộn ngoài rồi trở về qua cuộn trong như Hình P30.69.

(a) Khi nguồn ngoài cấp dòng $I$ theo hình, từ thông qua mỗi vòng cuộn trong bằng bao nhiêu, lấy hướng sang phải là dương? (b) Tìm từ thông qua mỗi vòng cuộn ngoài. (c) Tìm tự cảm nhìn từ hai đầu dây nối ra mạch ngoài. (d) Tự cảm thay đổi thế nào nếu đảo chiều quấn cuộn trong?

(e) Với cấu hình ban đầu, tính tự cảm khi chiều dài $\ell=20{,}0\,\mathrm{cm}$, $a=1{,}00\,\mathrm{cm}$, $b=2{,}00\,\mathrm{cm}$, $N_1=1200$, $N_2=750$. (f) Dùng cùng dữ kiện để tính cấu hình ở (d).

![Hình P30.69: Hai ống dây đồng trục nối tiếp tại đầu xa, với dòng qua các cuộn tạo trường ngược chiều trong cấu hình ban đầu.](img/young-30/hinh-p30-69.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai ống đủ dài để bỏ qua hiệu ứng đầu. Dòng có cùng độ lớn trong cả hai cuộn nhưng tạo trường ngược nhau ở vùng lõi chung. Chọn trường do cuộn ngoài hướng sang phải.

**Hướng đi:**

- Chia tiết diện thành vùng trong bán kính $a$ và vành giữa $a,b$, vì cuộn trong chỉ tạo trường ở vùng thứ nhất trong mô hình ống dài.
- Tính từ thông hình học theo cùng hướng sang phải, rồi xét chiều móc vòng khi cộng suất điện động của hai cuộn nối tiếp.
- Kiểm tra tự cảm bằng năng lượng từ trường của hai vùng. Năng lượng là một cách xác định dấu hỗ cảm mà không phụ thuộc cách gọi các đầu dây.

(a) Trong lõi chung,

$$
\begin{aligned}
B_{\mathrm{trong}} &= \frac{\mu_0I}{\ell}(N_1-N_2), \\
\Phi_2 &= B_{\mathrm{trong}}\pi a^2.
\end{aligned}
$$

(b) Trong vành $a<r<b$, trường chỉ do cuộn ngoài tạo ra. Từ thông qua vòng cuộn ngoài gồm hai phần:

$$
\begin{aligned}
\Phi_1 &= B_{\mathrm{trong}}\pi a^2 +\frac{\mu_0N_1I}{\ell}\pi(b^2-a^2) \\
&= \frac{\mu_0I\pi}{\ell}(N_1b^2-N_2a^2).
\end{aligned}
$$

(c) Đặt $\kappa=\mu_0\pi/\ell$. Các tự cảm riêng và hỗ cảm có độ lớn

$$
\begin{aligned}
L_1 &= \kappa N_1^2b^2, \\
L_2 &= \kappa N_2^2a^2, \\
M &= \kappa N_1N_2a^2.
\end{aligned}
$$

Trong cấu hình đối nhau, tự cảm nối tiếp là

$$
\begin{aligned}
L_- &= L_1+L_2-2M \\
&= \kappa N_1^2b^2 +\kappa N_2^2a^2 -2\kappa N_1N_2a^2.
\end{aligned}
$$

Cũng có thể suy từ $LI=N_1\Phi_1-N_2\Phi_2$. Dấu trừ xuất hiện vì cuộn trong được đi qua theo chiều quấn đối với cuộn ngoài. Không được cộng hai từ thông đã chọn cùng pháp tuyến mà bỏ qua chiều nối tiếp này.

Để đối chiếu, năng lượng hai vùng là

$$
\begin{aligned}
U_a &= \frac{B_{\mathrm{trong}}^2}{2\mu_0}\pi a^2\ell, \\
U_b &= \frac{B_{\mathrm{vành}}^2}{2\mu_0}\pi(b^2-a^2)\ell, \\
B_{\mathrm{vành}} &= \frac{\mu_0N_1I}{\ell}, \\
L_- &= \frac{2(U_a+U_b)}{I^2}.
\end{aligned}
$$

Kết quả trùng biểu thức hỗ cảm ở trên và luôn không âm.

(d) Khi đảo chiều quấn cuộn trong, hai trường hỗ trợ nhau. Khi ấy

$$
\begin{aligned}
L_+ &= L_1+L_2+2M \\
&= \kappa N_1^2b^2 +\kappa N_2^2a^2 +2\kappa N_1N_2a^2.
\end{aligned}
$$

(e)–(f) Thay các kích thước sang mét và giữ số vòng chính xác,

$$
\begin{aligned}
L_- &= 8{,}93\,\mathrm{mH}, \\
L_+ &= 16{,}0\,\mathrm{mH}.
\end{aligned}
$$

Cuộn ngoài còn có trường trong vành giữa hai ống, nên ngay cả khi hai số vòng bằng nhau, cấu hình đối nhau vẫn có tự cảm khác không nếu $a<b$.
:::

::: exercise 30.70. Đo mức chất lỏng bằng điện cảm
Một bồn được quấn dây để hoạt động như cuộn cảm. Điện cảm thay đổi từ $L_0$ khi rỗng, với độ từ thẩm tương đối bằng 1, đến $L_f$ khi đầy chất lỏng có độ từ thẩm tương đối $K_m$. Mạch điện tử đo điện cảm đến năm chữ số có nghĩa để suy mức chất lỏng.

Bốn mặt bên của bồn có chiều rộng $W$, chiều cao $D$. Mức chất lỏng là $d$ như Hình P30.70. Bỏ qua hiệu ứng mép và ảnh hưởng từ của thành bồn.

(a) Suy $d$ theo $L,L_0,L_f,D$. (b) Tính điện cảm đến năm chữ số có nghĩa khi bồn chứa oxy lỏng ở các mức một phần tư, một nửa, ba phần tư và đầy. Cho $L_0=0{,}63000\,\mathrm H$, độ cảm từ của oxy lỏng $\chi_m=1{,}52\times10^{-3}$. (c) Lặp lại cho thủy ngân, với độ cảm từ trong Bảng 28.1. (d) Thiết bị thực dụng hơn với chất lỏng nào?

![Hình P30.70: Các vòng dây bao quanh bồn có phần không khí và phần chất lỏng, nối với mạch đo điện cảm.](img/young-30/hinh-p30-70.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Trường trong bồn song song với mặt phân cách ngang như cấu hình quấn dây trong hình. Hai phần tiết diện đóng góp từ thông theo tỉ lệ chiều cao của chúng.

**Hướng đi:**

- Trong mô hình bỏ qua mép, cường độ từ trường $H$ ở hai phần giống nhau, còn $B=\mu H$ khác nhau theo môi trường.
- Cộng từ thông qua phần không khí và phần chất lỏng để được điện cảm tuyến tính theo $d/D$.
- Dùng $K_m=1+\chi_m$ và làm tròn kết quả cuối đến năm chữ số có nghĩa.

(a) Đặt $f=d/D$. Từ thông móc vòng, và do đó điện cảm, tỉ lệ với độ từ thẩm trung bình theo tiết diện:

$$
\begin{aligned}
L &= L_0[(1-f)+K_mf] \\
&= L_0+f(L_f-L_0), \\
d &= D\frac{L-L_0}{L_f-L_0}.
\end{aligned}
$$

Công thức suy mức cần $L_f\ne L_0$. Nếu hai môi trường có cùng độ từ thẩm thì điện cảm không mang thông tin về mức chất lỏng.

(b)–(c) Với oxy lỏng, dùng $\chi_m=1{,}52\times10^{-3}$. Với thủy ngân, Bảng 28.1 cho $\chi_m=-2{,}9\times10^{-5}$. Công thức tính là

$$
L=L_0(1+\chi_m f).
$$

| Mức bồn | Oxy lỏng (H) | Thủy ngân (H) |
| --- | --- | --- |
| Một phần tư | 0,63024 | 0,63000 |
| Một nửa | 0,63048 | 0,62999 |
| Ba phần tư | 0,63072 | 0,62999 |
| Đầy | 0,63096 | 0,62998 |

(d) Oxy lỏng có độ cảm từ lớn hơn về độ lớn, nên làm điện cảm thay đổi rõ hơn khi mức chất lỏng thay đổi. Với thủy ngân, làm tròn đến năm chữ số có nghĩa đã khiến mức rỗng và một phần tư cho cùng giá trị. Hai mức một nửa và ba phần tư cũng không phân biệt được bằng các số đã làm tròn. Vì thế phép đo mức này thực dụng hơn với oxy lỏng trong mô hình và độ phân giải đã nêu.
:::

::: exercise 30.71
Trong Hình P30.71, đóng $S$ tại $t=0$. Nhánh cuộn có dòng $i_1$, nhánh tụ có dòng $i_2$ và điện tích $q_2$. Tụ ban đầu chưa tích điện.

(a) Suy $i_1(t),i_2(t),q_2(t)$ theo $\mathcal E,L,C,R_1,R_2,t$. Sau đó dùng $\mathcal E=48\,\mathrm V$, $L=8{,}0\,\mathrm H$, $C=20\,\mu\mathrm F$, $R_1=25\,\Omega$, $R_2=5000\,\Omega$.

(b) Tìm dòng đầu trong mỗi nhánh. (c) Tìm hai dòng sau rất lâu và giải thích “rất lâu” nghĩa là bao lâu. (d) Tìm thời điểm hai dòng bằng nhau, với hai chữ số có nghĩa. Gợi ý: Có thể khai triển các hàm mũ. (e) Tìm dòng $i_1$ trong điều kiện (d). (f) Tìm thời điểm dòng tổng nguồn bằng nửa giá trị cuối, với hai chữ số có nghĩa. Gợi ý: Phác hai dòng theo thời gian để chọn xấp xỉ phù hợp.

![Hình P30.71: Nhánh điện trở và cuộn cảm mắc song song với nhánh điện trở và tụ điện trên cùng nguồn.](img/young-30/hinh-p30-71.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nguồn lý tưởng giữ điện áp hai nhánh không đổi. Mỗi nhánh có một quá trình chuyển tiếp độc lập, RL và RC.

**Hướng đi:**

- Áp nghiệm dòng tăng RL cho nhánh 1 và nghiệm nạp tụ RC cho nhánh 2, với các điều kiện đầu bằng không tương ứng.
- Hai nhánh có hằng số thời gian khác nhau, nên phải xét cả hai khi nói đến trạng thái cuối.
- Hai dòng bằng nhau rất sớm, cho phép dùng khai triển mũ bậc nhất. Dòng tổng đạt nửa giá trị cuối muộn hơn, khi dòng nhánh tụ đã nhỏ so với dòng nhánh cuộn.

(a) Đặt $\tau_L=L/R_1$, $\tau_C=R_2C$. Từ phương trình vòng từng nhánh,

$$
\begin{aligned}
L\frac{di_1}{dt}+R_1i_1 &= \mathcal E, \\
R_2\frac{dq_2}{dt}+\frac{q_2}{C} &= \mathcal E.
\end{aligned}
$$

Tích phân với $i_1(0)=0$ và $q_2(0)=0$ cho

$$
\begin{aligned}
i_1(t) &= \frac{\mathcal E}{R_1}(1-e^{-t/\tau_L}), \\
q_2(t) &= \mathcal EC(1-e^{-t/\tau_C}), \\
i_2(t) &= \frac{dq_2}{dt} \\
&= \frac{\mathcal E}{R_2}e^{-t/\tau_C}.
\end{aligned}
$$

(b) Ngay sau đóng, $i_1(0)=0$ và $i_2(0)=9{,}60\,\mathrm{mA}$.

(c) Về lâu dài, $i_1\to1{,}92\,\mathrm A$, $i_2\to0$. Hai hằng số thời gian là $\tau_L=0{,}32\,\mathrm s$ và $\tau_C=0{,}10\,\mathrm s$. “Rất lâu” đòi hỏi thời gian lớn hơn nhiều cả hai, đặc biệt lớn hơn nhiều 0,32 s. Mức gần trạng thái cuối cụ thể phụ thuộc sai số chấp nhận được.

(d) Phương trình hai dòng bằng nhau là

$$
1{,}92(1-e^{-t/0{,}32}) \qquad=0{,}00960e^{-t/0{,}10}.
$$

Các thời gian trong số mũ được tính bằng giây. Ở thời gian rất ngắn,

$$
\begin{aligned}
i_1 &\approx (6{,}00\,\mathrm{A/s})t, \\
i_2 &\approx 0{,}00960\,\mathrm A -(0{,}0960\,\mathrm{A/s})t.
\end{aligned}
$$

Giải các biểu thức bậc nhất cho khoảng 1,57 ms. Giải phương trình mũ đầy đủ cho 1,579 ms. Với hai chữ số có nghĩa,

$$
t_1=1{,}6\,\mathrm{ms}.
$$

(e) Dùng thời điểm chưa làm tròn trong nghiệm dòng cho $i_1=i_2\approx9{,}4\,\mathrm{mA}$.

(f) Dòng cuối của nguồn bằng 1,92 A. Khi tổng dòng đạt 0,960 A, nhánh tụ đã có dòng rất nhỏ. Xấp xỉ $i_1=0{,}960\,\mathrm A$ cho

$$
\begin{aligned}
1-e^{-t_2/0{,}32} &\approx \frac12, \\
t_2 &\approx 0{,}32\ln2\,\mathrm s \\
&\approx 0{,}22\,\mathrm s.
\end{aligned}
$$

Giữ cả dòng nhánh tụ trong phương trình tổng cho khoảng 0,22146 s, vẫn làm tròn thành 0,22 s theo yêu cầu.
:::

## Bài đọc và câu hỏi MCAT: Mất siêu dẫn trong nam châm MRI

Nam châm mang dòng rất lớn tạo trường mạnh, gần đều cho máy chụp cộng hưởng từ MRI. Một mô hình nam châm điển hình là ống dây dài 2,0 m, đường kính 1,0 m, tự cảm 4,4 H và dòng 750 A. Dây dẫn thông thường mang dòng ấy sẽ tỏa nhiệt rất lớn. Vì vậy phần lớn các nam châm này dùng dây siêu dẫn, được làm lạnh bằng heli lỏng ở nhiệt độ ngay dưới điểm sôi 4,2 K.

Sau khi thiết lập dòng, nguồn được tách ra và hai đầu nam châm nối với nhau bằng đoạn dây siêu dẫn. Dòng tiếp tục lưu thông không có điện trở chừng nào heli giữ nam châm đủ lạnh.

Trong một số tình huống hiếm, một đoạn dây mất siêu dẫn và xuất hiện điện trở. Nhiệt Joule ở đoạn này làm sôi một phần heli. Các đoạn dây khác nóng lên và cũng mất siêu dẫn, tạo thêm nhiệt. Nhiệt hóa hơi của heli lỏng chỉ $20{,}9\,\mathrm{kJ/kg}$, nên quá trình có thể làm heli sôi rất nhanh.

Sự kiện mất siêu dẫn dây chuyền này được gọi là sự cố quench và có thể làm hỏng nam châm. Heli hóa hơi tạo thể tích khí lớn, gây nguy cơ thiếu oxy và làm áp suất tăng nhanh, thậm chí gây nổ. Điều đó giải thích yêu cầu duy trì điện trở bằng không khi vận hành, đồng thời có cơ cấu phát hiện sự cố và ngắt dòng kịp thời.

::: exercise 30.72
Nam châm MRI điển hình trong bài đọc có khoảng bao nhiêu vòng dây?

(a) 1100. (b) 3000. (c) 4000. (d) 22000.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** $L=4{,}4\,\mathrm H$, $\ell=2{,}0\,\mathrm m$, bán kính $r=0{,}50\,\mathrm m$. Chọn phương án gần số vòng suy ra từ mô hình ống dây.

**Hướng đi:**

- Dùng $L=\mu_0N^2A/\ell$ với $A=\pi r^2$ để ước lượng số vòng.
- Dòng 750 A không cần để tìm số vòng từ hình học và tự cảm trong mô hình tuyến tính.

$$
\begin{aligned}
N &= \sqrt{\frac{L\ell}{\mu_0\pi r^2}} \\
&\approx 3{,}0\times10^3.
\end{aligned}
$$

Chọn (b).
:::

::: exercise 30.73
Nếu một phần nam châm mất siêu dẫn và điện trở đột ngột tăng từ không lên giá trị không đổi $0{,}005\,\Omega$, sau bao lâu dòng còn một nửa?

(a) 4,7 phút. (b) 10 phút. (c) 15 phút. (d) 30 phút.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Cuộn có $L=4{,}4\,\mathrm H$, điện trở mới không đổi, nguồn đã tách ra.

**Hướng đi:**

- Dùng dòng suy giảm RL với hằng số thời gian $L/R$.
- Giải điều kiện dòng giảm nửa, rồi đổi giây sang phút để chọn đáp án.

$$
\begin{aligned}
t_{1/2} &= \frac LR\ln2 \\
&\approx 610\,\mathrm s \\
&\approx 10\,\mathrm{min}.
\end{aligned}
$$

Chọn (b). Thời gian không phụ thuộc dòng đầu nếu chỉ hỏi tỉ lệ còn lại và $L,R$ không đổi.
:::

::: exercise 30.74
Nếu quench tiếp diễn, heli sôi đi và ngày càng nhiều phần nam châm mất siêu dẫn, thời gian dòng giảm còn một nửa thay đổi thế nào?

(a) Ngắn hơn vì điện trở tăng. (b) Dài hơn vì điện trở tăng. (c) Không đổi. (d) Không đủ dữ kiện.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện trở tiếp tục tăng so với mô hình điện trở không đổi ở bài 30.73. Giữ tự cảm theo mô hình bài đọc.

**Hướng đi:**

- Dùng phương trình suy giảm $L\,di/dt=-R(t)i$, thay vì gán một hằng số thời gian cố định cho điện trở biến thiên.
- So tích phân điện trở theo thời gian để xác định tốc độ giảm dòng.

$$
\begin{aligned}
A(t) &= \frac1L\int_0^tR(s)\,ds, \\
\frac{i(t)}{I_0} &= e^{-A(t)}.
\end{aligned}
$$

Điện trở tăng làm tích phân đạt $L\ln2$ sớm hơn so với việc giữ điện trở ở giá trị ban đầu. Dòng giảm nửa nhanh hơn. Chọn (a).
:::

::: exercise 30.75
Nếu toàn bộ năng lượng từ trường trong nam châm chuyển thành nhiệt, khối lượng heli lỏng hóa hơi là bao nhiêu?

(a) 27 kg. (b) 38 kg. (c) 60 kg. (d) 110 kg.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dùng $L=4{,}4\,\mathrm H$, $I=750\,\mathrm A$ và nhiệt hóa hơi riêng $20{,}9\times10^3\,\mathrm{J/kg}$. Giả sử toàn bộ năng lượng cuộn dùng để hóa hơi.

**Hướng đi:**

- Tính năng lượng từ trường $LI^2/2$.
- Chia năng lượng cho nhiệt hóa hơi riêng, với cả hai cùng dùng joule.

$$
\begin{aligned}
U_B &= \frac12LI^2 \\
&\approx 1{,}24\times10^6\,\mathrm J, \\
m &= \frac{U_B}{\mathcal L_v} \\
&\approx 59\,\mathrm{kg}.
\end{aligned}
$$

Phương án gần nhất là 60 kg. Chọn (c).
:::
