## Tổng kết chương 19

### Nhiệt lượng và công trong quá trình nhiệt động

Một hệ nhiệt động có thể trao đổi năng lượng với môi trường bằng truyền nhiệt hoặc bằng công. Khi hệ có áp suất $p$ và biến đổi thể tích từ $V_1$ đến $V_2$, công do hệ thực hiện trong quá trình cân bằng hoặc gần cân bằng là:

$$
W=\int_{V_1}^{V_2}p\,dV.
$$

Trên đồ thị áp suất theo thể tích, tích phân là diện tích có dấu dưới đường quá trình. Giãn nở cho $W>0$, còn nén cho $W<0$, tức môi trường thực hiện công dương lên hệ.

Nếu áp suất không đổi:

$$
W=p(V_2-V_1).
$$

![Sơ đồ tổng kết 19.1: Công của khí giãn nở được biểu diễn bằng diện tích có dấu dưới đường quá trình trên giản đồ áp suất và thể tích.](./img/young-19/b-tom-tat-19-01.png)

Nhiệt lượng hệ nhận và công hệ thực hiện phụ thuộc cả trạng thái đầu, trạng thái cuối lẫn đường đi qua các trạng thái trung gian. Chỉ biết hai trạng thái đầu và cuối chưa đủ để tìm riêng $Q$ hoặc $W$.

### Nguyên lý thứ nhất của nhiệt động lực học

Với quy ước $Q>0$ khi hệ nhận nhiệt và $W>0$ khi hệ thực hiện công:

$$
\Delta U=Q-W.
$$

Ở một bước biến đổi vô cùng nhỏ:

$$
dU=\delta Q-\delta W.
$$

Ký hiệu $dU$ biểu thị vi phân của hàm trạng thái. Ký hiệu $\delta Q,\delta W$ nhấn mạnh rằng nhiệt lượng và công là các đại lượng trao đổi phụ thuộc đường đi.

Chẳng hạn, hệ nhận $150\,\mathrm J$ nhiệt lượng và thực hiện $100\,\mathrm J$ công thì nội năng tăng $50\,\mathrm J$.

![Sơ đồ tổng kết 19.2: Hệ nhận nhiệt lượng, thực hiện công và thay đổi nội năng theo nguyên lý thứ nhất.](./img/young-19/b-tom-tat-19-02.png)

Nội năng phụ thuộc trạng thái của hệ. Độ biến thiên nội năng giữa hai trạng thái không phụ thuộc cách thực hiện quá trình. Hệ cô lập không trao đổi nhiệt hoặc công với môi trường, nên nội năng không đổi.

### Bốn quá trình thường gặp

- Đoạn nhiệt: Không truyền nhiệt qua biên hệ, nên $Q=0$ và $\Delta U=-W$.
- Đẳng tích: Thể tích không đổi, nên công do thay đổi thể tích bằng không. Khi không có dạng công khác, $\Delta U=Q$.
- Đẳng áp: Áp suất không đổi và công bằng $p(V_2-V_1)$.
- Đẳng nhiệt: Nhiệt độ không đổi. Đẳng nhiệt không đồng nghĩa không truyền nhiệt.

Với khí lý tưởng, nội năng chỉ phụ thuộc nhiệt độ. Vì vậy, quá trình đẳng nhiệt của khí lý tưởng có $\Delta U=0$ và $Q=W$. Kết luận này về nội năng không áp dụng nguyên vẹn cho mọi chất thực.

![Sơ đồ tổng kết 19.3: So sánh các đường đẳng tích, đẳng áp, đẳng nhiệt và đoạn nhiệt xuất phát từ cùng trạng thái.](./img/young-19/b-tom-tat-19-03.png)

### Nội năng và nhiệt dung của khí lý tưởng

Nhiệt dung mol đẳng tích $C_V$ xác định độ biến thiên nội năng theo nhiệt độ:

$$
dU=nC_V\,dT.
$$

Nếu $C_V$ gần như không đổi trong khoảng nhiệt độ:

$$
\Delta U=nC_V(T_2-T_1).
$$

Khí lý tưởng có hai nhiệt dung mol liên hệ bởi:

$$
C_p=C_V+R.
$$

Tỉ số nhiệt dung là đại lượng không có đơn vị:

$$
\gamma=\frac{C_p}{C_V}.
$$

Ở đẳng áp, một phần nhiệt lượng nhận vào được dùng để thực hiện công giãn nở. Vì vậy, để tăng cùng nhiệt độ, khí cần nhận nhiều nhiệt hơn so với đẳng tích và có $C_p>C_V$.

![Sơ đồ tổng kết 19.4: Hai cách tăng nhiệt độ khí lý tưởng, ở thể tích không đổi hoặc áp suất không đổi.](./img/young-19/b-tom-tat-19-04.png)

### Quá trình đoạn nhiệt của khí lý tưởng

Đối với quá trình đoạn nhiệt thuận nghịch hoặc gần cân bằng của khí lý tưởng có nhiệt dung mol gần như không đổi:

$$
TV^{\gamma-1}=\text{hằng số},
$$

và:

$$
pV^\gamma=\text{hằng số}.
$$

Điều kiện thuận nghịch hoặc gần cân bằng là cần thiết khi dùng các đường quá trình này. Việc một hệ không nhận nhiệt, tự nó, chưa bảo đảm mọi quá trình đều thỏa $pV^\gamma=\text{hằng số}$.

Công do khí thực hiện có thể viết theo hai nhiệt độ:

$$
W=nC_V(T_1-T_2).
$$

Đặt $\Delta(pV)=p_1V_1-p_2V_2$, là hiệu hai tích áp suất và thể tích tại trạng thái đầu và cuối. Khi đó:

$$
\begin{aligned}
W&=\frac{C_V}{R}\Delta(pV)\\
&=\frac{\Delta(pV)}{\gamma-1}.
\end{aligned}
$$

Trong giãn nở đoạn nhiệt, khí sinh công và nội năng giảm. Với khí lý tưởng, nhiệt độ vì vậy giảm. Khi nén đoạn nhiệt, môi trường thực hiện công lên khí, làm nội năng và nhiệt độ tăng.

![Sơ đồ tổng kết 19.5: Giãn nở đoạn nhiệt có nhiệt lượng trao đổi bằng không và nội năng giảm đúng bằng công do khí thực hiện.](./img/young-19/b-tom-tat-19-05.png)
