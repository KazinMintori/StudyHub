## Chuyển tọa độ sự kiện và vận tốc giữa hai hệ

Biến đổi Galileo giữ một thời gian chung cho mọi hệ, nhưng giãn thời gian và co chiều dài đã cho thấy giả thiết ấy không chính xác ở vận tốc lớn. Ta cần những quan hệ mới liên hệ không gian và thời gian của cùng một sự kiện.

### 1. Suy ra biến đổi tọa độ

Chọn hai hệ quán tính có các trục song song. Gốc O′ của $S'$ chuyển động với vận tốc $u$ theo chiều $+x$ của $S$. Hai gốc và hai số chỉ thời gian trùng nhau tại $t=t'=0$.

![Hình 37.15: Cùng một sự kiện P có tọa độ trong hai hệ, còn độ dài x′ được đo trong hệ nghỉ S′ của các mốc tạo nên nó.](../img/young-37/hinh-37-15.png)

Trong hệ $S$, gốc O′ ở vị trí $ut$. Khoảng từ O′ đến P có giá trị riêng $x'$ theo hệ $S'$, nên thành phần dọc chuyển động khi đo trong $S$ là $x'/\gamma$. Do đó,

$$
x=ut+\frac{x'}{\gamma}.
\tag{37.17}
$$

Vì $1/\gamma=\sqrt{1-u^2/c^2}$, đây cũng là quan hệ với hệ số căn của co chiều dài. Giải theo $x'$ cho

$$
x'=\frac{x-ut}{\sqrt{1-u^2/c^2}}.
\tag{37.18}
$$

Nguyên lý tương đối yêu cầu phép chuyển ngược có cùng dạng, chỉ đổi dấu vận tốc và đổi hai hệ. Vì vậy,

$$
x'=-ut'+\frac{x}{\gamma}.
\tag{37.19}
$$

Thay $x'=\gamma(x-ut)$ từ (37.18) vào (37.19), ta được

$$
ut'=\gamma ut-(\gamma-1/\gamma)x.
$$

Định nghĩa hệ số Lorentz cho $\gamma-1/\gamma=\gamma u^2/c^2$. Chia cho $u$ khi $u\ne0$, rồi lấy giới hạn liên tục ở $u=0$, cho

$$
t'=\frac{t-ux/c^2}{\sqrt{1-u^2/c^2}}.
\tag{37.20}
$$

Các kích thước vuông góc vận tốc không đổi. Gom lại, ta có **biến đổi tọa độ Lorentz**:

$$
\begin{aligned}
x'&=\gamma(x-ut),\\
y'&=y,\\
z'&=z,\\
t'&=\gamma(t-ux/c^2).
\end{aligned}
\tag{37.21}
$$

Khi các vận tốc đang xét nhỏ so với $c$, $\gamma$ gần một và hiệu chỉnh $ux/c^2$ có thể bỏ qua ở mức chính xác thích hợp. Ta tìm lại biến đổi Galileo.

Nói chung, cả tọa độ vị trí lẫn thời gian trong một hệ phụ thuộc vị trí và thời gian trong hệ kia. Bốn đại lượng $x,y,z,t$ cùng tạo nên tọa độ của một sự kiện trong **không thời gian**. Không thể giữ nguyên thời gian rồi chỉ đổi tọa độ không gian khi đang dùng biến đổi Lorentz.

### 2. Suy ra biến đổi vận tốc một chiều

Xét hạt chuyển động dọc trục $x$. Trong khoảng vi phân $dt$, hạt đi $dx$ trong hệ $S$. Lấy vi phân các phương trình tọa độ cho

$$
\begin{aligned}
dx'&=\gamma(dx-u\,dt),\\
dt'&=\gamma(dt-u\,dx/c^2).
\end{aligned}
$$

Chia hai biểu thức rồi chia cả tử và mẫu cho $dt$. Nhận ra $v_x=dx/dt$ và $v'_x=dx'/dt'$, ta được

$$
v'_x=\frac{v_x-u}{1-uv_x/c^2}.
\tag{37.22}
$$

Hệ số Lorentz triệt tiêu trong phép chia, nhưng hiệu chỉnh thời gian ở mẫu không triệt tiêu. Đây là điểm khác phép cộng Galileo.

Nếu $u$ và $v_x$ đều rất nhỏ so với $c$, mẫu gần một và $v'_x\approx v_x-u$. Nếu hạt là xung sáng có $v_x=c$, ta có

$$
\begin{aligned}
v'_x&=\frac{c-u}{1-u/c}\\
&=c.
\end{aligned}
$$

Ánh sáng vẫn có cùng tốc độ trong hai hệ. Đổi vai hai hệ và đổi $u$ thành $-u$ cho phép biến đổi ngược:

$$
v_x=\frac{v'_x+u}{1+uv'_x/c^2}.
\tag{37.23}
$$

Cũng có thể giải trực tiếp (37.22) theo $v_x$. Với $|u|<c$, một vật có tốc độ nhỏ hơn $c$ trong một hệ sẽ có tốc độ nhỏ hơn $c$ trong hệ kia.

### 3. Một cuộc chạy tiếp sức và cách chọn dấu

Trong Hình ứng dụng, coi vận động viên áo tím là vật đang được theo dõi. Hệ $S$ gắn với người xem bên đường chạy, còn hệ $S'$ gắn với vận động viên áo đỏ.

![Ứng dụng: Vận tốc của vận động viên áo tím được đo trong hệ người xem và trong hệ chuyển động cùng vận động viên áo đỏ.](../img/young-37/ung-dung-37-chay-tiep-suc.png)

Áo đỏ chạy sang trái trong ảnh. Muốn dùng quy ước $u>0$ của các công thức trên, ta chọn chiều $+x$ sang trái. Áo tím cũng chạy sang trái nên có $v_x>0$ trong hệ người xem. Nếu áo đỏ chạy nhanh hơn áo tím, $u>v_x$, thì $v'_x<0$: Áo tím lùi lại trong hệ áo đỏ.

Vận tốc chạy bộ nhỏ hơn nhiều so với $c$, nên hiệu chỉnh tương đối tính không đáng kể ở tình huống này. Hình giúp nhận rõ ba đại lượng khác nhau: Vận tốc hai hệ $u$, vận tốc vật trong $S$ là $v_x$, và vận tốc vật trong $S'$ là $v'_x$.

### 4. Cách giải bài toán biến đổi Lorentz

1. Xác định đại lượng cần tìm và hai hệ $S,S'$. Vẽ chiều trục và ghi rõ hệ nào có vận tốc $u$ đối với hệ kia.
2. Với bài tọa độ, lập danh sách các tọa độ của từng sự kiện trong từng hệ. Ghi rõ dữ kiện đã biết và ẩn cần tìm, không trộn hai sự kiện khác nhau.
3. Với bài vận tốc, phân biệt $u$, $v_x$ và $v'_x$. Chọn phép thuận hoặc ngược theo hệ mà dữ kiện được cho.
4. Nếu cần chuyển ngược tọa độ, đổi dấu $u$ và hoán đổi dấu phẩy. Kiểm tra sự kiện gốc vẫn được gán đúng.
5. Đánh giá bằng tính nhất quán của hệ và miền tốc độ. Kết quả khác trực giác vận tốc nhỏ chưa đủ để kết luận phép tính sai.

### Ví dụ 37.6: Tin mừng có được phát trước khi về đích không?

Mavis lái tàu qua vạch đích không gian với tốc độ $0{,}600c$ đối với vạch. Trong hệ tàu, đúng lúc đầu tàu qua vạch, đuôi tàu phát thông điệp “hoan hô”. Độ dài riêng tàu là $300\,\mathrm m$. Stanley đứng yên tại vạch đích xác định hai sự kiện xảy ra ở đâu và lúc nào?

**Nhận dạng và chuẩn bị:** Chọn $S$ gắn vạch đích, $S'$ gắn đầu tàu. Sự kiện 1 là đầu tàu qua vạch, chọn làm gốc của cả hai hệ. Sự kiện 2 là phát tin ở đuôi, có $x'=-300\,\mathrm m$, $t'=0$.

**Thực hiện:** Biến đổi ngược là

$$
\begin{aligned}
x&=\gamma(x'+ut'),\\
t&=\gamma(t'+ux'/c^2).
\end{aligned}
$$

Với $\gamma=1{,}25$, sự kiện 2 có $x=-375\,\mathrm m$ và $t=-0{,}750\,\mu\mathrm s$. Sự kiện 1 vẫn ở $x=0,t=0$.

**Đánh giá:** Trong hệ Mavis, hai sự kiện đồng thời. Stanley lại xác định tin đã được phát trước khi đầu tàu qua đích. Điều này không cho phép một hệ quả xảy ra trước nguyên nhân gây ra nó.

Tín hiệu nhanh nhất từ đầu tàu đến đuôi tàu cần $300/c=1{,}00\,\mu\mathrm s$ trong hệ tàu. Mavis không thể đợi đầu tàu vừa qua đích rồi gửi một lệnh khiến đuôi phát tin ngay cùng lúc trong hệ tàu. Lệnh ấy phải được gửi sớm hơn ít nhất một microgiây, nên việc phát tin đã được bố trí trước.

### Ví dụ 37.7: Đầu dò và tàu trinh sát

(a) Một tàu bay ra xa Trái Đất với tốc độ $0{,}900c$, rồi phóng đầu dò cùng chiều với tốc độ $0{,}700c$ đối với tàu. Tìm vận tốc đầu dò đối với Trái Đất. (b) Tàu trinh sát từ Trái Đất đuổi theo với tốc độ $0{,}950c$. Tìm vận tốc tàu trinh sát đối với tàu chính.

![Hình 37.16: Các vận tốc của tàu chính, đầu dò và tàu trinh sát phải được phân biệt theo hệ Trái Đất và hệ tàu chính.](../img/young-37/hinh-37-16.png)

**Nhận dạng và chuẩn bị:** Hệ $S$ gắn Trái Đất, $S'$ gắn tàu chính và $u=0{,}900c$. Phần (a) biết vận tốc trong $S'$, phần (b) biết vận tốc trong $S$.

**Thực hiện:** Phần (a) dùng phép biến đổi ngược, phần (b) dùng phép thuận:

$$
\begin{aligned}
\frac{v_{\rm probe}}c&=\frac{0{,}700+0{,}900}{1+0{,}700(0{,}900)}\\
&\approx0{,}982,\\
\frac{v'_{\rm scout}}c&=\frac{0{,}950-0{,}900}{1-0{,}950(0{,}900)}\\
&\approx0{,}345.
\end{aligned}
$$

**Đánh giá:** Phép cộng Galileo sẽ cho đầu dò đi ở $1{,}600c$, vượt giới hạn và không hợp lệ. Nó cũng cho vận tốc trinh sát đối với tàu chính chỉ $0{,}050c$, nhỏ hơn gần bảy lần kết quả tương đối tính.

### Câu hỏi tự kiểm tra 37.5

(a) Trong $S$, hai sự kiện P₁ và P₂ ở cùng các tọa độ $x,y,z$, nhưng P₁ xảy ra trước P₂. Trong $S'$ chuyển động theo chiều $+x$ với tốc độ $u$, sự kiện nào xảy ra trước?

(b) Trong $S$, hai sự kiện P₃ và P₄ cùng thời điểm, cùng tọa độ $y,z$, nhưng $x_3<x_4$. Trong $S'$, sự kiện nào xảy ra trước?

<details><summary>Xem đáp án và giải thích</summary>

(a) P₁ vẫn xảy ra trước. Vì $\Delta x=0$, hiệu thời gian là $\Delta t'=\gamma\Delta t>0$ khi lấy P₂ trừ P₁. Thứ tự của hai sự kiện cùng vị trí trong một hệ không đảo khi đổi sang hệ quán tính khác.

(b) P₄ xảy ra trước. Lấy P₄ trừ P₃, ta có $\Delta t=0$ và $\Delta x>0$, nên

$$
\Delta t'=-\frac{\gamma u\Delta x}{c^2}<0.
$$

Đây là một biểu hiện định lượng của tính tương đối của đồng thời.

</details>
