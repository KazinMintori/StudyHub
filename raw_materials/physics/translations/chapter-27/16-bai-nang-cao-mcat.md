## Bài toán thử thách và MCAT chương 27: Bài 27.81–27.85

### Bài toán thử thách

::: exercise 27.81 •••
Một hạt có điện tích $2{,}15\,\mu\mathrm{C}$ và khối lượng $3{,}20\times10^{-11}\,\mathrm{kg}$ ban đầu chuyển động theo chiều $+y$ với tốc độ $v_0=1{,}45\times10^5\,\mathrm{m/s}$. Hạt đi vào vùng có từ trường đều vuông góc mặt giấy và hướng vào trong như hình P27.81. Độ lớn từ trường là $0{,}420\,\mathrm{T}$. Vùng từ trường kéo dài $25{,}0\,\mathrm{cm}$ theo hướng chuyển động ban đầu. Một bức tường cách điểm vào $75{,}0\,\mathrm{cm}$, nên vùng không có từ trường dài $50{,}0\,\mathrm{cm}$. Trong vùng từ, hạt đi theo cung cong bán kính $R$, rồi ra khỏi vùng sau thời gian $t_1$ với độ lệch ngang $\Delta x_1$. Sau đó hạt đi qua vùng không từ trường và đập vào tường với độ lệch tổng $\Delta x$.

(a) Tìm bán kính $R$ của phần quỹ đạo cong. (b) Tìm thời gian $t_1$ mà hạt ở trong vùng từ trường. (c) Tìm độ lệch ngang $\Delta x_1$ tại điểm ra khỏi vùng từ trường. (d) Tìm độ lệch tổng $\Delta x$ tại tường.

![Hình P27.81: Hạt tích điện lệch khỏi phương ban đầu trong vùng từ trường.](img/young-27/hinh-p27-81.png)
:::

::: solution
**Tóm tắt đề bài:** $q=2{,}15\times10^{-6}\,\mathrm{C}$, $m=3{,}20\times10^{-11}\,\mathrm{kg}$, $v_0=1{,}45\times10^5\,\mathrm{m/s}$, $B=0{,}420\,\mathrm{T}$, chiều dài vùng từ $d=0{,}250\,\mathrm{m}$, khoảng cách tới tường $D=0{,}750\,\mathrm{m}$.

**Hướng đi:**
- Lực Lorentz vuông góc vận tốc nên tốc độ không đổi trong vùng từ, còn bán kính là $R=mv/(qB)$.
- Góc thoát $\phi$ được xác định từ tọa độ dọc ban đầu: $d=R\sin\phi$.
- Độ lệch ngang trong vùng từ là $R(1-\cos\phi)$. Sau đó, hạt bay thẳng với góc $\phi$ thêm quãng dọc $D-d$.

**Lời giải.** Tích có hướng $q\vec v\times\vec B$ hướng sang trái, tức chiều $+x$ trong hệ trục của hình. Dưới đây, các độ lệch được nêu theo độ lớn.

(a)

$$
R=\frac{mv_0}{qB}=5{,}14\,\mathrm{m}.
$$

(b) Ở mép vùng từ, $d=R\sin\phi$, do đó

$$
\begin{aligned}
\phi &= \sin^{-1}\left(\frac{0{,}250}{5{,}14}\right) \\
&= 0{,}0487\,\mathrm{rad}.
\end{aligned}
$$

Thời gian đi cung là

$$
\begin{aligned}
t_1 &= \frac{R\phi}{v_0} \\
&= 1{,}72\times10^{-6}\,\mathrm{s}.
\end{aligned}
$$

(c)

$$
\begin{aligned}
\Delta x_1 &= R(1-\cos\phi) \\
&= 6{,}08\times10^{-3}\,\mathrm{m}.
\end{aligned}
$$

(d) Trong vùng không có từ trường, quỹ đạo tiếp tuyến tại điểm thoát có hệ số góc $\tan\phi$. Do đó

$$
\begin{aligned}
\Delta x &= \Delta x_1+(D-d)\tan\phi \\
&= 3{,}05\times10^{-2}\,\mathrm{m}.
\end{aligned}
$$

Trên hình, chiều $+x$ hướng sang trái. Hạt đập vào tường lệch khoảng $3{,}05\,\mathrm{cm}$ theo $+x$.
:::

::: exercise 27.82 ••• CP
### Quỹ đạo cycloid
Một hạt khối lượng $m$, điện tích dương $q$, bắt đầu từ nghỉ tại gốc tọa độ như hình P27.82. Điện trường đều $\vec E$ hướng $+y$, còn từ trường đều $\vec B$ hướng ra khỏi trang giấy. Trong các tài liệu nâng cao, quỹ đạo này được chứng minh là một cycloid. Bán kính cong tại các điểm đỉnh bằng hai lần tọa độ $y$ của đỉnh ấy.

(a) Giải thích vì sao quỹ đạo có dạng chung như vậy và lặp lại. (b) Chứng minh tốc độ tại mọi điểm bằng $\sqrt{2qEy/m}$. Gợi ý: Dùng bảo toàn năng lượng. (c) Áp dụng định luật II Newton tại điểm đỉnh, đồng thời dùng bán kính cong tại đó bằng $2y$, để chứng minh tốc độ tại đỉnh là $2E/B$.

![Hình P27.82: Quỹ đạo cycloid của hạt tích điện trong điện trường và từ trường.](img/young-27/hinh-p27-82.png)
:::

::: solution
**Tóm tắt đề bài:** $q>0$, $\vec E=E\hat j$, $\vec B=B\hat k$, hạt bắt đầu từ nghỉ tại $y=0$.

**Hướng đi:**
- Điện trường làm tăng thành phần vận tốc theo $y$. Lực từ luôn vuông góc vận tốc, làm lệch quỹ đạo mà không sinh công.
- Bảo toàn năng lượng liên hệ tốc độ với độ cao.
- Ở đỉnh cycloid, gia tốc pháp tuyến hướng xuống tâm cong. Cân bằng lực theo phương tiếp tuyến và dùng bán kính cong đã cho.

**Lời giải.** (a) Ban đầu lực điện làm hạt chuyển động theo $+y$. Lực từ bẻ hướng vận tốc sang $+x$. Thành phần vận tốc theo $y$ lần lượt dương rồi âm, đưa hạt trở lại đường $y=0$, trong khi chuyển động trôi theo $+x$ tiếp tục. Quỹ đạo lặp thành các cung cycloid dọc theo hướng $\vec E\times\vec B$, vuông góc với điện trường.

(b) Lực từ vuông góc với $\vec v$, nên công của nó bằng không. Từ vị trí ban đầu đến độ cao $y$, công của điện trường là $qEy$. Bảo toàn năng lượng cho

$$
\begin{aligned}
\frac12 mv^2 &= qEy, \\
v &= \sqrt{\frac{2qEy}{m}}.
\end{aligned}
$$

(c) Ở đỉnh, vận tốc hướng ngang sang phải. Với $\vec B$ hướng ra khỏi trang, lực từ $q\vec v\times\vec B$ hướng xuống, còn lực điện hướng lên. Vì thế lực hướng tâm bằng $qvB-qE$. Bán kính cong là $2y$, nên định luật II Newton cho $m v^2/(2y)=qvB-qE$. Từ câu (b), $mv^2/(2y)=qE$. Do đó $qE=qvB-qE$, suy ra

$$
v=\frac{2E}{B}.
$$

Kết quả không phụ thuộc $m$ hay $q$, dù độ cao đỉnh được xác định bởi $y=2mE/(qB^2)$ khi kết hợp với câu (b).
:::

### Đoạn văn MCAT

::: info BIO: Từ trường và chụp cộng hưởng từ MRI
Chụp cộng hưởng từ (MRI) là một phương pháp tạo ảnh mạnh. Không giống chụp X-quang, MRI cho ảnh rõ của mô mềm mà không khiến người bệnh tiếp xúc với bức xạ có thể gây hại. Có thể hiểu sơ lược phương pháp này bằng cách áp dụng vật lý từ học cổ điển, tức vật lý phi lượng tử.

Điểm khởi đầu của MRI là cộng hưởng từ hạt nhân (NMR), một kỹ thuật dựa trên sự kiện proton trong hạt nhân nguyên tử có từ trường $\vec B$. Từ trường của proton bắt nguồn từ spin của nó. Vì mang điện, proton đang spin tương đương một dòng điện chạy trong một vòng dây. Giống vòng dây, proton có mômen từ $\vec M$, vì vậy nó chịu mômen lực khi đặt trong từ trường ngoài $\vec B_0$. Độ lớn của $M$ xấp xỉ $1{,}4\times10^{-26}\,\mathrm{J/T}$. Có thể xem proton ở một trong hai trạng thái. Mômen từ $\vec M$ song song hoặc ngược song song với từ trường đặt vào. Cần thực hiện công để lật proton từ trạng thái năng lượng thấp sang trạng thái năng lượng cao.

Một điểm quan trọng là từ trường tổng của mọi hạt nhân, ngoại trừ hydro chỉ có một proton, nhận đóng góp từ cả proton lẫn neutron. Nếu hạt nhân có số proton và neutron đều chẵn, chúng ghép cặp sao cho một nửa proton có spin theo một hướng, nửa còn lại theo hướng đối diện. Vì vậy mômen từ hạt nhân tổng bằng không. Chỉ hạt nhân có mômen từ tổng khác không mới có thể dùng cho MRI. Hydro là nguyên tố được chụp ảnh phổ biến nhất.

Hình minh họa hai hướng của mômen proton trong từ trường. Khi $\vec M$ song song $\vec B_0$ là trạng thái năng lượng thấp. Khi $\vec M$ ngược chiều $\vec B_0$, proton ở trạng thái năng lượng cao và cần công để chuyển sang.
:::

![Trạng thái spin của proton trong từ trường ngoài: Song song có năng lượng thấp, ngược chiều có năng lượng cao.](img/young-27/mcat-spin.png)

::: exercise 27.83
Nếu một proton đặt trong từ trường ngoài $2\,\mathrm{T}$ vuông góc với trục spin của proton, mômen lực lên proton bằng bao nhiêu? Chọn một đáp án trong các phương án dưới đây.

- (a) $0$.
- (b) $1{,}4\times10^{-26}\,\mathrm{N\,m}$.
- (c) $2{,}8\times10^{-26}\,\mathrm{N\,m}$.
- (d) $0{,}7\times10^{-26}\,\mathrm{N\,m}$.
:::

::: solution
**Tóm tắt đề bài:** $M=1{,}4\times10^{-26}\,\mathrm{J/T}$, $B=2\,\mathrm{T}$, góc giữa $\vec M$ và $\vec B$ là $90^\circ$.

**Hướng đi:**
- Độ lớn mômen lực từ là $\tau=MB\sin\theta$.
- Vì hai vectơ vuông góc, $\sin\theta=1$.

**Lời giải.**

$$
\begin{aligned}
\tau &= (1{,}4\times10^{-26})(2)(1) \\
&= 2{,}8\times10^{-26}\,\mathrm{N\,m}.
\end{aligned}
$$

Chọn (c).
:::

::: exercise 27.84
Nguyên tố nào sau đây là ứng viên cho MRI?

- (a) $^{12}_{6}\mathrm C$.
- (b) $^{16}_{8}\mathrm O$.
- (c) $^{40}_{20}\mathrm{Ca}$.
- (d) $^{31}_{15}\mathrm P$.
:::

::: solution
**Tóm tắt đề bài:** MRI cần hạt nhân có mômen từ tổng khác không. Hạt nhân có số proton và neutron đều chẵn có mômen từ bằng không theo mô hình ghép cặp trong đoạn dẫn.

**Hướng đi:**
- Đếm số neutron bằng số khối trừ số proton.
- Loại các hạt nhân có cả số proton và neutron đều chẵn.

**Lời giải.** Carbon-12 có 6 proton và 6 neutron. Oxygen-16 có 8 proton và 8 neutron, còn calcium-40 có 20 proton và 20 neutron. Cả ba đều là hạt nhân chẵn-chẵn. Phosphorus-31 có 15 proton và 16 neutron, nên còn một proton chưa ghép cặp và có thể có mômen từ tổng khác không.

Chọn (d), $^{31}_{15}\mathrm P$.
:::

::: exercise 27.85
Từ trường lớn dùng trong MRI có thể tạo lực lên các dòng điện trong cơ thể. Hiệu ứng này từng được đề xuất như một cách chụp ảnh các “dòng điện sinh học” trong cơ thể, chẳng hạn dòng điện chạy trong từng dây thần kinh. Với từ trường $2\,\mathrm{T}$, hãy ước lượng độ lớn lực cực đại lên một đoạn dây thần kinh hình trụ dài $1\,\mathrm{mm}$, đường kính $1{,}5\,\mathrm{mm}$. Giả sử toàn bộ dây thần kinh mang dòng do hiệu điện thế đặt vào $100\,\mathrm{mV}$, bằng điện thế hoạt động điển hình. Điện trở suất của dây thần kinh là $0{,}6\,\Omega\,\mathrm{m}$. Chọn một đáp án trong các phương án dưới đây.

- (a) $6\times10^{-7}\,\mathrm{N}$.
- (b) $1\times10^{-6}\,\mathrm{N}$.
- (c) $3\times10^{-4}\,\mathrm{N}$.
- (d) $0{,}3\,\mathrm{N}$.
:::

::: solution
**Tóm tắt đề bài:** $L=1{,}0\times10^{-3}\,\mathrm{m}$, $d=1{,}5\times10^{-3}\,\mathrm{m}$, $V=0{,}100\,\mathrm{V}$, $\rho=0{,}6\,\Omega\,\mathrm{m}$, $B=2\,\mathrm{T}$.

**Hướng đi:**
- Tính điện trở đoạn dây bằng $R=\rho L/A$, trong đó $A=\pi(d/2)^2$.
- Dùng định luật Ohm để tìm dòng điện.
- Lực cực đại đạt được khi dòng vuông góc từ trường: $F=ILB$.

**Lời giải.** Tiết diện dây thần kinh là $A=1{,}77\times10^{-6}\,\mathrm{m^2}$. Điện trở đoạn dây:

$$
\begin{aligned}
R &= \frac{\rho L}{A} \\
&= 3{,}40\times10^2\,\Omega.
\end{aligned}
$$

Dòng điện là $I=V/R=2{,}94\times10^{-4}\,\mathrm{A}$. Vì đề yêu cầu lực cực đại, lấy dòng vuông góc với trường:

$$
\begin{aligned}
F_{\max} &= ILB \\
&= 5{,}88\times10^{-7}\,\mathrm{N}.
\end{aligned}
$$

Chọn (a), $6\times10^{-7}\,\mathrm{N}$.
:::
