## Luyện tập có hướng dẫn

Hệ thống bài luyện tập có hướng dẫn bao gồm các bài biến thể bám sát ví dụ mẫu (Variation Problems), giúp củng cố phương pháp phân tích thành phần vector và tích vô hướng.

![Tài nguyên học tập đa phương tiện](/vat-ly-1/bai-giang/img/young-01/r-exercises-guided-media-qr.png)


Nhóm bài tập đầu tiên phát triển từ **Ví dụ 1.7 (Mục 1.8)** về phép cộng vector độ dời bằng phương pháp phân tích thành phần. Hãy ôn lại dữ liệu và bảng thành phần của Ví dụ 1.7 trước khi thực hiện:
- Vector $\vec A$ có độ lớn $72{,}4\,\mathrm m$, hướng $32{,}0^\circ$ đông so với bắc ($A_x = 38{,}37\,\mathrm m$ và $A_y = 61{,}40\,\mathrm m$).
- Vector $\vec B$ có độ lớn $57{,}3\,\mathrm m$, hướng $36{,}0^\circ$ nam so với tây ($B_x = -46{,}36\,\mathrm m$ và $B_y = -33{,}68\,\mathrm m$).
- Vector $\vec C$ có độ lớn $17{,}8\,\mathrm m$, hướng chính nam ($C_x = 0{,}00\,\mathrm m$ và $C_y = -17{,}80\,\mathrm m$).
- Vector tổng hợp $\vec R = \vec A + \vec B + \vec C$ có thành phần $R_x = -7{,}99\,\mathrm m$ và $R_y = 9{,}92\,\mathrm m$.

### VP1.7.1: Tìm vector thứ tư để triệt tiêu tổng ba vector

Xét ba vector $\vec A$, $\vec B$ và $\vec C$ trong Ví dụ 1.7. Nếu một vector thứ tư $\vec D$ được cộng vào tổng $\vec A + \vec B + \vec C$, kết quả thu được bằng không:

$$
\vec A + \vec B + \vec C + \vec D = \vec 0.
$$

Hãy tìm độ lớn và hướng của $\vec D$. Biểu diễn hướng của $\vec D$ bằng một góc đo ngược chiều kim đồng hồ từ trục $+x$, và cho biết góc này nằm trong góc phần tư nào.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cho ba vector từ Ví dụ 1.7 với vector tổng hợp $\vec R = \vec A + \vec B + \vec C$ có $R_x = -7{,}99\,\mathrm m$ và $R_y = +9{,}92\,\mathrm m$. Cần tìm độ lớn và góc định hướng $\theta_D$ của vector $\vec D$ thỏa mãn $\vec R + \vec D = \vec 0$.

**Hướng đi:**

- Điều kiện tổng vector bằng không đồng nghĩa với việc vector $\vec D$ là vector đối của vector tổng hợp: $\vec D = -\vec R$.
- Từng thành phần tọa độ của $\vec D$ phải bằng số đối của thành phần tương ứng của $\vec R$: $D_x = -R_x$ và $D_y = -R_y$.
- Độ lớn $D$ được tính bằng định lý Pythagoras: $D = \sqrt{D_x^2 + D_y^2}$.
- Xác định góc phần tư dựa vào dấu của $D_x$ và $D_y$, sau đó tính góc định hướng ngược chiều kim đồng hồ từ trục $+x$.

**Lời giải:**

Các thành phần tọa độ của vector $\vec D$ là:

$$
\begin{aligned}
D_x &= -R_x \\
&= -(-7{,}99\,\mathrm m) \\
&= +7{,}99\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
D_y &= -R_y \\
&= -(+9{,}92\,\mathrm m) \\
&= -9{,}92\,\mathrm m.
\end{aligned}
$$

Độ lớn của vector $\vec D$ là:

$$
\begin{aligned}
D &= \sqrt{D_x^2 + D_y^2} \\
&= \sqrt{7{,}99^2 + (-9{,}92)^2}\,\mathrm m \\
&= 12{,}7\,\mathrm m.
\end{aligned}
$$

Xác định góc phần tư và hướng: Vì $D_x > 0$ và $D_y < 0$, vector $\vec D$ nằm ở góc phần tư thứ tư (Góc phần tư IV).

Góc nhọn hợp với trục hoành dương là:

$$
\begin{aligned}
\alpha &= \arctan\left(\frac{|D_y|}{D_x}\right) \\
&= \arctan\left(\frac{9{,}92\,\mathrm m}{7{,}99\,\mathrm m}\right) \\
&\approx 51{,}1^\circ.
\end{aligned}
$$

Góc định hướng $\theta_D$ đo theo chiều ngược chiều kim đồng hồ từ trục $+x$ là:

$$
\begin{aligned}
\theta_D &= 360^\circ - 51{,}1^\circ \\
&= 308{,}9^\circ \\
&\approx 309^\circ.
\end{aligned}
$$

Vậy vector $\vec D$ có độ lớn $12{,}7\,\mathrm m$, hướng $309^\circ$ ngược chiều kim đồng hồ từ trục $+x$ (thuộc góc phần tư IV).

</details>

### VP1.7.2: Độ lớn và hướng của hiệu vector tổng hợp

Xét ba vector $\vec A$, $\vec B$ và $\vec C$ trong Ví dụ 1.7. Hãy tính độ lớn và hướng của vector $\vec S = \vec A - \vec B + \vec C$. Biểu diễn hướng của $\vec S$ bằng một góc đo ngược chiều kim đồng hồ từ trục $+x$, và cho biết góc này nằm trong góc phần tư nào. (Gợi ý: Các thành phần của $-\vec B$ chính là số đối của các thành phần tương ứng của $\vec B$).

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cho ba vector $\vec A = (38{,}37; 61{,}40)\,\mathrm m$, $\vec B = (-46{,}36; -33{,}68)\,\mathrm m$, $\vec C = (0{,}00; -17{,}80)\,\mathrm m$. Cần tìm độ lớn $S$ và góc định hướng $\theta_S$ của vector $\vec S = \vec A - \vec B + \vec C$.

**Hướng đi:**

- Phép trừ vector được thực hiện trực tiếp trên từng thành phần tọa độ: $S_x = A_x - B_x + C_x$ và $S_y = A_y - B_y + C_y$.
- Thành phần của $-\vec B$ đổi dấu so với thành phần của $\vec B$, biến phép trừ thành phép cộng số đối.
- Tính độ lớn $S = \sqrt{S_x^2 + S_y^2}$ và xác định góc phần tư từ dấu của các thành phần tọa độ.

**Lời giải:**

Tính các thành phần của vector $\vec S$:

$$
\begin{aligned}
S_x &= A_x - B_x + C_x \\
&= (38{,}37 + 46{,}36 + 0)\,\mathrm m \\
&= 84{,}73\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
S_y &= A_y - B_y + C_y \\
&= 61{,}40 + 33{,}68 - 17{,}80 \\
&= 77{,}28\,\mathrm m.
\end{aligned}
$$

Độ lớn của vector $\vec S$ là:

$$
\begin{aligned}
S &= \sqrt{S_x^2 + S_y^2} \\
&= \sqrt{84{,}73^2 + 77{,}28^2}\,\mathrm m \\
&\approx 115\,\mathrm m.
\end{aligned}
$$

Xác định góc phần tư và hướng: Vì $S_x > 0$ và $S_y > 0$, vector $\vec S$ nằm ở góc phần tư thứ nhất (Góc phần tư I).

Góc định hướng $\theta_S$ đo theo chiều ngược chiều kim đồng hồ từ trục $+x$ là:

$$
\begin{aligned}
\theta_S &= \arctan\left(\frac{S_y}{S_x}\right) \\
&= \arctan\left(\frac{77{,}28\,\mathrm m}{84{,}73\,\mathrm m}\right) \\
&\approx 42{,}4^\circ.
\end{aligned}
$$

Vậy vector $\vec S$ có độ lớn $115\,\mathrm m$, hướng $42{,}4^\circ$ so với trục $+x$ (thuộc góc phần tư I).

</details>

### VP1.7.3: Phép nhân vô hướng với vector và tổng vector

Xét ba vector $\vec A$, $\vec B$ và $\vec C$ trong Ví dụ 1.7.

(a) Tìm các thành phần của vector $\vec T = \vec A + \vec B + 2\vec C$.

(b) Tìm độ lớn và hướng của $\vec T$. Biểu diễn hướng bằng góc đo ngược chiều kim đồng hồ từ trục $+x$, và cho biết góc này nằm trong góc phần tư nào.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dữ liệu ba vector: $\vec A = (38{,}37; 61{,}40)\,\mathrm m$, $\vec B = (-46{,}36; -33{,}68)\,\mathrm m$, $\vec C = (0{,}00; -17{,}80)\,\mathrm m$. Xét tổ hợp tuyến tính $\vec T = \vec A + \vec B + 2\vec C$.

**Hướng đi:**

- Phép nhân vector với số vô hướng làm nhân các thành phần tương ứng với số đó: Thành phần của $2\vec C$ là $2C_x$ và $2C_y$.
- Thành phần của $\vec T$ bằng tổng các thành phần tương ứng: $T_x = A_x + B_x + 2C_x$ và $T_y = A_y + B_y + 2C_y$.
- Tính độ lớn $T = \sqrt{T_x^2 + T_y^2}$ và dùng hàm lượng giác để xác định góc định hướng.

**Lời giải:**

**(a)** Các thành phần tọa độ của vector $\vec T$:

$$
\begin{aligned}
T_x &= A_x + B_x + 2C_x \\
&= (38{,}37 - 46{,}36 + 0)\,\mathrm m \\
&= -7{,}99\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
T_y &= A_y + B_y + 2C_y \\
&= 61{,}40 - 33{,}68 - 35{,}60 \\
&= -7{,}88\,\mathrm m.
\end{aligned}
$$

**(b)** Độ lớn và hướng của vector $\vec T$:

Độ lớn của $\vec T$ là:

$$
\begin{aligned}
T &= \sqrt{T_x^2 + T_y^2} \\
&= \sqrt{125{,}93}\,\mathrm m \\
&\approx 11{,}2\,\mathrm m.
\end{aligned}
$$

Xác định góc phần tư và hướng: Vì $T_x < 0$ và $T_y < 0$, vector $\vec T$ nằm ở góc phần tư thứ ba (Góc phần tư III).

Góc nhọn so với trục hoành âm $-x$ là:

$$
\begin{aligned}
\beta &= \arctan\left(\frac{|T_y|}{|T_x|}\right) \\
&= \arctan\left(\frac{7{,}88\,\mathrm m}{7{,}99\,\mathrm m}\right) \\
&\approx 44{,}6^\circ.
\end{aligned}
$$

Góc định hướng $\theta_T$ đo ngược chiều kim đồng hồ từ trục $+x$ là:

$$
\begin{aligned}
\theta_T &= 180^\circ + 44{,}6^\circ \\
&= 224{,}6^\circ \\
&\approx 225^\circ.
\end{aligned}
$$

Vậy vector $\vec T$ có độ lớn $11{,}2\,\mathrm m$, hướng $225^\circ$ ngược chiều kim đồng hồ từ trục $+x$ (thuộc góc phần tư III).

</details>

### VP1.7.4: Xác định độ dời thứ hai của người đi bộ

Một người đi bộ thực hiện độ dời $\vec A$ như trong Ví dụ 1.7. Sau đó, người ấy thực hiện độ dời thứ hai sao cho vị trí cuối cùng cách điểm xuất phát ban đầu $38{,}0\,\mathrm m$, theo hướng lệch $37{,}0^\circ$ về phía tây so với bắc. Hãy tìm độ lớn và hướng của độ dời thứ hai này. Biểu diễn hướng bằng góc đo ngược chiều kim đồng hồ từ trục $+x$, và cho biết góc này nằm trong góc phần tư nào.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ dời đầu tiên là $\vec A = (38{,}37; 61{,}40)\,\mathrm m$. Độ dời tổng hợp $\vec R_{\text{net}} = \vec A + \vec D_2$ có độ lớn $R_{\text{net}} = 38{,}0\,\mathrm m$ theo hướng $37{,}0^\circ$ tây so với bắc. Cần tìm độ lớn $D_2$ và hướng của độ dời thứ hai $\vec D_2$.

**Hướng đi:**

- Hướng bắc tương ứng trục $+y$ ($90^\circ$). Hướng lệch tây $37{,}0^\circ$ tương ứng góc định hướng $\theta_{\text{net}} = 90^\circ + 37{,}0^\circ = 127{,}0^\circ$ đo từ trục $+x$.
- Phân tích $\vec R_{\text{net}}$ thành hai thành phần tọa độ theo phương ngang và phương đứng.
- Sử dụng quan hệ cộng vector $\vec R_{\text{net}} = \vec A + \vec D_2$ để suy ra $\vec D_2 = \vec R_{\text{net}} - \vec A$.
- Tính độ lớn $D_2$ và góc phần tư của $\vec D_2$.

**Lời giải:**

Các thành phần của vector độ dời tổng hợp $\vec R_{\text{net}}$ là:

$$
\begin{aligned}
R_{\text{net}, x} &= 38{,}0\cos(127{,}0^\circ)\,\mathrm m \\
&= -38{,}0\sin(37{,}0^\circ)\,\mathrm m \\
&\approx -22{,}87\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
R_{\text{net}, y} &= (38{,}0\,\mathrm m)\sin(127{,}0^\circ) \\
&= (38{,}0\,\mathrm m)\cos(37{,}0^\circ) \\
&\approx 30{,}35\,\mathrm m.
\end{aligned}
$$

Các thành phần của độ dời thứ hai $\vec D_2 = \vec R_{\text{net}} - \vec A$:

$$
\begin{aligned}
D_{2x} &= R_{\text{net}, x} - A_x \\
&= -22{,}87\,\mathrm m - 38{,}37\,\mathrm m \\
&= -61{,}24\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
D_{2y} &= R_{\text{net}, y} - A_y \\
&= 30{,}35\,\mathrm m - 61{,}40\,\mathrm m \\
&= -31{,}05\,\mathrm m.
\end{aligned}
$$

Độ lớn của độ dời thứ hai là:

$$
\begin{aligned}
D_2 &= \sqrt{D_{2x}^2 + D_{2y}^2} \\
&= \sqrt{4714{,}4}\,\mathrm m \\
&\approx 68{,}7\,\mathrm m.
\end{aligned}
$$

Xác định góc phần tư và hướng: Vì $D_{2x} < 0$ và $D_{2y} < 0$, vector $\vec D_2$ nằm ở góc phần tư thứ ba (Góc phần tư III).

Góc nghiêng so với trục âm $-x$ là:

$$
\begin{aligned}
\gamma &= \arctan\left(\frac{|D_{2y}|}{|D_{2x}|}\right) \\
&= \arctan\left(\frac{31{,}05\,\mathrm m}{61{,}24\,\mathrm m}\right) \\
&\approx 26{,}9^\circ.
\end{aligned}
$$

Góc định hướng đo ngược chiều kim đồng hồ từ trục $+x$ là:

$$
\begin{aligned}
\theta_{D2} &= 180^\circ + 26{,}9^\circ \\
&= 206{,}9^\circ \\
&\approx 207^\circ.
\end{aligned}
$$

Vậy độ dời thứ hai có độ lớn $68{,}7\,\mathrm m$, hướng $207^\circ$ ngược chiều kim đồng hồ từ trục $+x$ (thuộc góc phần tư III).

</details>

Nhóm bài tập tiếp theo vận dụng kiến thức tích vô hướng từ **Ví dụ 1.9 và Ví dụ 1.10 (Mục 1.10)**:
- Tích vô hướng qua độ lớn và góc kẹp: $\vec A \cdot \vec B = AB\cos\phi$.
- Tích vô hướng qua các thành phần tọa độ: Đặt $P=\vec A\cdot\vec B$, ta có:

$$
P = A_xB_x+A_yB_y+A_zB_z.
$$

Đặt $A_1=A_x$, $A_2=A_y$, $A_3=A_z$ và tương tự cho $B_i$, dạng viết gọn là:

$$
P = \sum_{i=1}^{3} A_iB_i.
$$

### VP1.10.1: Tính tích vô hướng từ các thành phần hướng địa lý

Vector $\vec A$ có độ lớn $5{,}00$ và hợp góc $36{,}9^\circ$ về phía nam so với đông. Vector $\vec B$ có độ lớn $6{,}40$ và hợp góc $20{,}0^\circ$ về phía tây so với bắc.

(a) Chọn chiều dương của trục $x$ hướng về phía đông và chiều dương của trục $y$ hướng về phía bắc. Hãy tìm các thành phần của $\vec A$ và $\vec B$.

(b) Tính tích vô hướng $\vec A \cdot \vec B$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Vector $\vec A$ có độ lớn $5{,}00$, lệch $36{,}9^\circ$ nam so với đông. Vector $\vec B$ có độ lớn $6{,}40$, lệch $20{,}0^\circ$ tây so với bắc. Trục $+x$ hướng đông, trục $+y$ hướng bắc. Cần tìm các thành phần tọa độ và tính $\vec A \cdot \vec B$.

**Hướng đi:**

- Chiều đông là $+x$ và nam là $-y$, góc của $\vec A$ là $\theta_A = -36{,}9^\circ$.
- Chiều bắc là $+y$ và tây là $-x$, góc của $\vec B$ so với trục $+x$ là $\theta_B = 110{,}0^\circ$.
- Dùng công thức $A_x = A\cos\theta, A_y = A\sin\theta$ để tìm các thành phần.
- Tính tích vô hướng bằng tổng tích các thành phần: $\vec A \cdot \vec B = A_x B_x + A_y B_y$.

**Lời giải:**

**(a)** Các thành phần tọa độ của hai vector:

Đối với vector $\vec A$:

$$
\begin{aligned}
A_x &= A\cos(-36{,}9^\circ) \\
&= 5{,}00\cos(36{,}9^\circ) \\
&\approx 4{,}00,
\end{aligned}
$$

$$
\begin{aligned}
A_y &= A\sin(-36{,}9^\circ) \\
&= -5{,}00\sin(36{,}9^\circ) \\
&\approx -3{,}00.
\end{aligned}
$$

Đối với vector $\vec B$: Góc hợp bởi $\vec B$ và trục $+x$ là $\theta_B = 110{,}0^\circ$. Do đó:

$$
\begin{aligned}
B_x &= B\cos(110{,}0^\circ) \\
&= -6{,}40\sin(20{,}0^\circ) \\
&\approx -2{,}19,
\end{aligned}
$$

$$
\begin{aligned}
B_y &= B\sin(110{,}0^\circ) \\
&= 6{,}40\cos(20{,}0^\circ) \\
&\approx 6{,}01.
\end{aligned}
$$

**(b)** Tích vô hướng $\vec A \cdot \vec B$:

Áp dụng biểu thức tính tích vô hướng theo thành phần tọa độ:

$$
\begin{aligned}
\vec A \cdot \vec B &= A_x B_x + A_y B_y \\
&= -8{,}756 - 18{,}042 \\
&\approx -26{,}8.
\end{aligned}
$$

Kiểm tra bằng góc kẹp giữa hai vector: Góc kẹp giữa hai vector là $\phi = 146{,}9^\circ$. Khi đó:

$$
\begin{aligned}
\vec A \cdot \vec B &= AB\cos\phi \\
&= 32{,}0\cos(146{,}9^\circ) \\
&\approx -26{,}8.
\end{aligned}
$$

Cả hai cách tính đều cho kết quả trùng khớp.

</details>

### VP1.10.2: Tích vô hướng và góc giữa hai vector trong mặt phẳng

Vector $\vec C$ có độ lớn $6{,}50$ và tạo góc $55{,}0^\circ$ đo ngược chiều kim đồng hồ từ trục $+x$ về phía trục $+y$. Vector $\vec D$ có các thành phần $D_x = +4{,}80$ và $D_y = -8{,}40$.

(a) Tính tích vô hướng $\vec C \cdot \vec D$.

(b) Tìm góc $\phi$ giữa hai vector $\vec C$ và $\vec D$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cho vector $\vec C$ có độ lớn $C = 6{,}50$, góc $\theta_C = 55{,}0^\circ$. Vector $\vec D$ có $D_x = 4{,}80$ và $D_y = -8{,}40$. Cần tính $\vec C \cdot \vec D$ và góc $\phi$ giữa hai vector.

**Hướng đi:**

- Chuyển đổi vector $\vec C$ sang dạng thành phần tọa độ qua $C_x = C\cos\theta_C$ và $C_y = C\sin\theta_C$.
- Tính tích vô hướng bằng công thức tọa độ: $\vec C \cdot \vec D = C_x D_x + C_y D_y$.
- Tính độ lớn của vector $\vec D$: $D = \sqrt{D_x^2 + D_y^2}$.
- Sử dụng hệ thức định nghĩa $\vec C \cdot \vec D = CD\cos\phi$ để giải ra góc $\phi$.

**Lời giải:**

**(a)** Tích vô hướng $\vec C \cdot \vec D$:

Các thành phần của vector $\vec C$ là:

$$
C_x = 6{,}50\cos(55{,}0^\circ) \approx 3{,}73,
$$

$$
C_y = 6{,}50\sin(55{,}0^\circ) \approx 5{,}32.
$$

Tích vô hướng giữa hai vector là:

$$
\begin{aligned}
\vec C \cdot \vec D &= C_x D_x + C_y D_y \\
&= 17{,}89 - 44{,}72 \\
&\approx -26{,}8.
\end{aligned}
$$

**(b)** Góc $\phi$ giữa hai vector:

Độ lớn của vector $\vec D$ là:

$$
\begin{aligned}
D &= \sqrt{D_x^2 + D_y^2} \\
&= \sqrt{4{,}80^2 + (-8{,}40)^2} \\
&\approx 9{,}67.
\end{aligned}
$$

Cosin của góc $\phi$ là:

$$
\begin{aligned}
\cos\phi &= \frac{\vec C \cdot \vec D}{CD} \\
&= \frac{-26{,}83}{(6{,}50)(9{,}675)} \\
&\approx -0{,}4266.
\end{aligned}
$$

Suy ra góc $\phi$ giữa hai vector:

$$
\begin{aligned}
\phi &= \arccos(-0{,}4266) \\
&\approx 115^\circ.
\end{aligned}
$$

Góc tù này hoàn toàn phù hợp với dấu âm của tích vô hướng.

</details>

### VP1.10.3: Tìm góc giữa hai vector ba chiều

Vector $\vec A$ có các thành phần $A_x = -5{,}00$, $A_y = 3{,}00$, $A_z = 0$. Vector $\vec B$ có các thành phần $B_x = 2{,}50$, $B_y = 4{,}00$, $B_z = -1{,}50$. Hãy tìm góc giữa hai vector này.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cho hai vector trong không gian ba chiều: $\vec A = (-5{,}00; 3{,}00; 0)$ và $\vec B = (2{,}50; 4{,}00; -1{,}50)$. Cần tìm góc $\phi$ giữa chúng.

**Hướng đi:**

- Trong không gian ba chiều, tích vô hướng được tính qua: $A_x B_x + A_y B_y + A_z B_z$.
- Tính độ lớn của từng vector: $A = \sqrt{A_x^2 + A_y^2 + A_z^2}$ và $B = \sqrt{B_x^2 + B_y^2 + B_z^2}$.
- Tìm cosin của góc kẹp qua công thức: $\cos\phi = \frac{\vec A \cdot \vec B}{AB}$, rồi tính $\phi = \arccos(\cos\phi)$.

**Lời giải:**

Tính tích vô hướng của hai vector qua các thành phần:

$$
\begin{aligned}
\vec A \cdot \vec B &= -12{,}50 + 12{,}00 + 0 \\
&= -0{,}500.
\end{aligned}
$$

Độ lớn của từng vector:

$$
\begin{aligned}
A &= \sqrt{A_x^2 + A_y^2 + A_z^2} \\
&= \sqrt{34{,}00} \\
&\approx 5{,}83,
\end{aligned}
$$

$$
\begin{aligned}
B &= \sqrt{B_x^2 + B_y^2 + B_z^2} \\
&= \sqrt{24{,}50} \\
&\approx 4{,}95.
\end{aligned}
$$

Cosin của góc giữa hai vector:

$$
\begin{aligned}
\cos\phi &= \frac{\vec A \cdot \vec B}{AB} \\
&= \frac{-0{,}500}{(5{,}831)(4{,}950)} \\
&\approx -0{,}01732.
\end{aligned}
$$

Góc giữa hai vector là:

$$
\begin{aligned}
\phi &= \arccos(-0{,}01732) \\
&\approx 91{,}0^\circ.
\end{aligned}
$$

Góc $\phi$ hơi lớn hơn $90^\circ$ một lượng nhỏ, phù hợp với giá trị tích vô hướng âm gần bằng không.

</details>

### VP1.10.4: Xác định thành phần lực và góc tác dụng từ công cơ học

Nếu một lực $\vec F$ tác dụng lên một vật khi vật thực hiện độ dời $\vec s$, thì công do lực đó thực hiện bằng tích vô hướng của $\vec F$ và $\vec s$:

$$
W = \vec F \cdot \vec s.
$$

Một vật thực hiện độ dời $\vec s = (4{,}00\,\mathrm m)\hat{\mathbf i} + (5{,}00\,\mathrm m)\hat{\mathbf j}$. Trong quá trình chuyển động, vật chịu tác dụng của lực $\vec F$ có thành phần $x$ là $F_x = -12{,}0\,\mathrm N$ ($1\,\mathrm N = 1\,\text{newton}$ là đơn vị SI của lực). Công do lực này thực hiện là $26{,}0\,\mathrm{N\cdot m} = 26{,}0\,\mathrm J$ ($1\,\mathrm J = 1\,\text{joule}$ là đơn vị SI của công).

(a) Tìm thành phần $y$ của lực $\vec F$.

(b) Tìm góc giữa lực $\vec F$ và độ dời $\vec s$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Độ dời $\vec s = (4{,}00; 5{,}00)\,\mathrm m$. Lực tác dụng có $F_x = -12{,}0\,\mathrm N$ và thực hiện công $W = 26{,}0\,\mathrm J$. Cần tìm thành phần $F_y$ và góc $\phi$ giữa $\vec F$ và $\vec s$.

**Hướng đi:**

- Áp dụng biểu thức công theo thành phần tọa độ: $W = F_x s_x + F_y s_y$. Từ dữ kiện đã biết, lập phương trình bậc nhất đối với ẩn $F_y$.
- Tính độ lớn của vector độ dời $s = \sqrt{s_x^2 + s_y^2}$ và độ lớn của lực $F = \sqrt{F_x^2 + F_y^2}$.
- Sử dụng định nghĩa công qua tích vô hướng $W = F s \cos\phi$ để giải ra cosin và góc $\phi$.

**Lời giải:**

**(a)** Tìm thành phần $y$ của lực $\vec F$:

Biểu thức công theo thành phần tọa độ là:

$$
W = F_x s_x + F_y s_y.
$$

Thay các giá trị bằng số vào phương trình:

$$
26{,}0 = -48{,}0 + 5{,}00 F_y.
$$

Chuyển vế để tìm thành phần $F_y$:

$$
\begin{aligned}
5{,}00 F_y &= 26{,}0 + 48{,}0 \\
&= 74{,}0,
\end{aligned}
$$

$$
F_y = \frac{74{,}0}{5{,}00} = +14{,}8\,\mathrm N.
$$

**(b)** Tìm góc giữa lực $\vec F$ và độ dời $\vec s$:

Độ lớn của vector độ dời $\vec s$ và lực $\vec F$ là:

$$
\begin{aligned}
s &= \sqrt{s_x^2 + s_y^2} \\
&= \sqrt{4{,}00^2 + 5{,}00^2}\,\mathrm m \\
&\approx 6{,}40\,\mathrm m,
\end{aligned}
$$

$$
\begin{aligned}
F &= \sqrt{F_x^2 + F_y^2} \\
&= \sqrt{(-12{,}0)^2 + 14{,}8^2}\,\mathrm N \\
&\approx 19{,}1\,\mathrm N.
\end{aligned}
$$

Áp dụng định nghĩa tích vô hướng:

$$
\begin{aligned}
\cos\phi &= \frac{W}{Fs} \\
&= \frac{26{,}0\,\mathrm J}{(19{,}05\,\mathrm N)(6{,}403\,\mathrm m)} \\
&\approx 0{,}2131.
\end{aligned}
$$

Góc giữa lực và độ dời là:

$$
\phi = \arccos(0{,}2131) \approx 77{,}7^\circ.
$$

Vậy thành phần $y$ của lực là $+14{,}8\,\mathrm N$ và góc giữa lực với độ dời là $77{,}7^\circ$.

</details>
