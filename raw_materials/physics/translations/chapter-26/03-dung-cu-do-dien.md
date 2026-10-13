## 26.3. Dụng cụ đo điện

Muốn đo dòng điện chạy qua một linh kiện, ta phải đưa dụng cụ đo vào mạch. Việc đó có thể làm dòng điện thay đổi. Muốn đo hiệu điện thế giữa hai điểm, ta cũng phải nối dụng cụ vào hai điểm ấy. Bảng điều khiển ô tô, bộ sạc pin và nhiều thiết bị đo phổ thông dùng điện kế d’Arsonval để đo hiệu điện thế, dòng điện hoặc điện trở. Hiểu cách hoạt động của chúng giúp ta chọn đúng cách mắc và ước lượng sai lệch do dụng cụ gây ra.

### Điện kế d’Arsonval

Nhiều dụng cụ đo điện dùng một **điện kế d’Arsonval**. Bên trong điện kế có cuộn dây mảnh quay được trong từ trường của nam châm vĩnh cửu. Một lò xo gắn với cuộn dây tạo mômen kéo kim về vị trí không. Khi dòng điện chạy qua cuộn dây, từ trường tạo mômen làm kim lệch đi. Ở trạng thái cân bằng, độ lệch của kim tỉ lệ với dòng điện trong cuộn dây.

![Hình 26.13: Vôn kế và ampe kế dùng điện kế d’Arsonval](../img/young-26/hinh-26-13.png)

**Hình 26.13:** Vôn kế bên trái và ampe kế bên phải cùng dựa trên điện kế d’Arsonval. Sự khác nhau nằm ở cách nối các linh kiện bên trong.

![Hình 26.14: Cuộn dây quay, nam châm và lò xo trong điện kế d’Arsonval](../img/young-26/hinh-26-14.png)

**Hình 26.14:** Từ trường làm cuộn dây và kim quay ra khỏi vị trí không. Lò xo tạo mômen phục hồi, nhờ đó kim dừng ở vị trí biểu thị dòng điện.

Độ lệch lớn nhất của kim gọi là độ lệch toàn thang. Hai thông số quan trọng của điện kế là dòng điện toàn thang $I_{\mathrm{fs}}$ và điện trở cuộn dây $R_c$. Dòng điện toàn thang của một điện kế thường nằm trong khoảng từ $10\,\mathrm{\mu A}$ đến $10\,\mathrm{mA}$, còn điện trở cuộn dây thường từ $10\,\Omega$ đến $1000\,\Omega$.

Ví dụ, cuộn dây có $R_c=20{,}0\,\Omega$ và dòng toàn thang $I_{\mathrm{fs}}=1{,}00\,\mathrm{mA}$ thì hiệu điện thế toàn thang là:

$$
\begin{aligned}
&V_{\mathrm{fs}} = I_{\mathrm{fs}}R_c\\
&\quad =(1{,}00\times10^{-3}\,\mathrm A)(20{,}0\,\Omega)\\
&\quad =0{,}0200\,\mathrm V.
\end{aligned}
$$

### Ampe kế

Ampe kế đo dòng điện đi qua nó. Vì muốn đo dòng qua một linh kiện, ta mắc ampe kế **nối tiếp** với linh kiện ấy. Ampe kế lý tưởng có điện trở bằng không, nên việc thêm nó vào một nhánh không làm thay đổi dòng trong nhánh. Ampe kế thật luôn có điện trở hữu hạn, do đó điện trở ấy cần nhỏ để ảnh hưởng đến mạch không đáng kể.

![Hình 26.15: Nối điện kế với điện trở song song để đo dòng lớn](../img/young-26/hinh-26-15.png)

**Hình 26.15:** Cùng một điện kế có thể mắc song song với điện trở rẽ để tạo ampe kế hoặc mắc nối tiếp với điện trở phụ để tạo vôn kế.

Muốn đo dòng lớn hơn dòng toàn thang của điện kế, ta mắc thêm một điện trở nhỏ song song với cuộn dây. Điện trở này gọi là điện trở rẽ, ký hiệu $R_{\mathrm{sh}}$. Tại độ lệch toàn thang, dòng tổng $I_a$ chia làm dòng $I_{\mathrm{fs}}$ qua cuộn dây và dòng $I_a-I_{\mathrm{fs}}$ qua điện trở rẽ. Hai nhánh song song có cùng hiệu điện thế, vì vậy:

$$
\begin{aligned}
&I_{\mathrm{fs}}R_c = (I_a-I_{\mathrm{fs}})R_{\mathrm{sh}}.\end{aligned}
\tag{26.7}
$$

Suy ra điện trở rẽ cần dùng là:

$$
R_{\mathrm{sh}}=\frac{I_{\mathrm{fs}}R_c}{I_a-I_{\mathrm{fs}}}.
$$

#### Ví dụ 26.8: Thiết kế ampe kế

Hãy tìm điện trở rẽ để biến điện kế có dòng toàn thang $1{,}00\,\mathrm{mA}$ và điện trở cuộn dây $20{,}0\,\Omega$ thành ampe kế có thang đo từ $0$ đến $50{,}0\,\mathrm{mA}$.

**Tóm tắt đề bài:** $I_{\mathrm{fs}}=1{,}00\,\mathrm{mA}$, $R_c=20{,}0\,\Omega$ và $I_a=50{,}0\,\mathrm{mA}$.

**Hướng đi:**

- Dùng hiệu điện thế chung của hai nhánh song song. Dòng qua điện trở rẽ bằng dòng tổng trừ dòng toàn thang của cuộn dây.
- Từ hiệu điện thế trên cuộn dây, tính điện trở rẽ cần mắc.

**Thực hiện:** Thay các đại lượng đã cho vào phương trình (26.7):

$$
\begin{aligned}
&R_{\mathrm{sh}} = \frac{I_{\mathrm{fs}}R_c}{I_a-I_{\mathrm{fs}}}\\
&\quad =\frac{1{,}00}{50{,}0-1{,}00}(20{,}0\,\Omega)\\
&\quad =0{,}408\,\Omega.
\end{aligned}
$$

Điện trở tương đương của ampe kế là:

$$
\begin{aligned}
&R_{\mathrm{eq}} = \left(\frac{1}{R_c}+\frac{1}{R_{\mathrm{sh}}}\right)^{-1}\\
&\quad =0{,}400\,\Omega.
\end{aligned}
$$

Điện trở tương đương nhỏ hơn nhiều so với $R_c$, vì phần lớn dòng đi qua điện trở rẽ. Ở toàn thang, dòng qua điện kế là $1{,}00\,\mathrm{mA}$, dòng qua điện trở rẽ là $49{,}0\,\mathrm{mA}$, còn hiệu điện thế trên cả ampe kế là $0{,}0200\,\mathrm V$.

**Đánh giá:** Ampe kế có điện trở nhỏ như mong muốn, và dòng tổng toàn thang được chia đúng thành hai dòng nhánh.

**Ý chính:** Điện trở rẽ song song cho phép cuộn dây chỉ nhận dòng toàn thang, trong khi phần dòng còn lại đi qua nhánh rẽ.

### Vôn kế

Vôn kế đo hiệu điện thế giữa hai điểm, nên hai đầu vôn kế phải được nối vào chính hai điểm ấy. Cách mắc này là mắc **song song** với phần mạch cần đo. Vôn kế lý tưởng có điện trở vô hạn và không hút dòng điện. Vôn kế thật có điện trở hữu hạn, vì vậy cần có điện trở lớn để dòng qua vôn kế không làm thay đổi đáng kể các dòng khác.

Để mở rộng thang đo điện áp của điện kế, ta mắc điện trở phụ $R_s$ nối tiếp với cuộn dây. Với điện áp toàn thang $V_V$, dòng qua cuộn dây vẫn là $I_{\mathrm{fs}}$. Do đó:

$$
\begin{aligned}
&V_V = I_{\mathrm{fs}}(R_c+R_s).\end{aligned}
\tag{26.8}
$$

Từ đó, điện trở phụ bằng:

$$
R_s=\frac{V_V}{I_{\mathrm{fs}}}-R_c.
$$

#### Ví dụ 26.9: Thiết kế vôn kế

Hãy tìm điện trở nối tiếp cần mắc để biến điện kế có dòng toàn thang $1{,}00\,\mathrm{mA}$ và điện trở cuộn dây $20{,}0\,\Omega$ thành vôn kế có thang đo từ $0$ đến $10{,}0\,\mathrm V$.

**Tóm tắt đề bài:** $V_V=10{,}0\,\mathrm V$, $I_{\mathrm{fs}}=1{,}00\,\mathrm{mA}$ và $R_c=20{,}0\,\Omega$.

**Hướng đi:**

- Ở độ lệch toàn thang, dòng qua cuộn dây vẫn là $I_{\mathrm{fs}}$.
- Tính điện trở tổng cần có từ $V_V/I_{\mathrm{fs}}$, rồi trừ điện trở cuộn dây để tìm $R_s$.

**Thực hiện:**

$$
\begin{aligned}
&R_s = \frac{V_V}{I_{\mathrm{fs}}}-R_c\\
&\quad =\frac{10{,}0\,\mathrm V}{1{,}00\times10^{-3}\,\mathrm A}-20{,}0\,\Omega\\
&\quad =9980\,\Omega.
\end{aligned}
$$

Điện trở tương đương của vôn kế là $R_{\mathrm{eq}}=R_c+R_s=10\,000\,\Omega$. Ở toàn thang, cuộn dây có hiệu điện thế $0{,}0200\,\mathrm V$, còn điện trở nối tiếp chịu $9{,}98\,\mathrm V$.

**Đánh giá:** Điện trở lớn làm dòng mà vôn kế hút từ mạch nhỏ. Vì thế, vôn kế ít làm xáo trộn trạng thái mạch cần đo.

**Ý chính:** Điện trở nối tiếp giúp vôn kế đo điện áp cao hơn điện áp toàn thang của cuộn dây, đồng thời tạo điện trở vào lớn.

### Đo dòng điện, hiệu điện thế và điện trở

Để tìm điện trở $R$ của linh kiện hoặc công suất nó tiêu thụ, ta có thể đo đồng thời hiệu điện thế $V_{ab}$ trên linh kiện và dòng điện $I$ qua nó. Khi dụng cụ đo có điện trở thực, cần xét vị trí mắc.

![Hình 26.16: Hai cách mắc ampe kế và vôn kế khi đo điện trở](../img/young-26/hinh-26-16.png)

**Hình 26.16:** Trong cách mắc (a), ampe kế đo đúng dòng qua điện trở nhưng vôn kế còn đo độ giảm thế trên ampe kế. Trong cách mắc (b), vôn kế đo đúng hiệu điện thế trên điện trở nhưng ampe kế đo thêm dòng qua vôn kế.

Ở cách mắc (a), ampe kế nối tiếp với điện trở nên số chỉ của nó là dòng thật qua điện trở. Tuy nhiên, vôn kế đặt ngoài cả điện trở và ampe kế nên số chỉ gồm $V_{ab}$ cộng với độ giảm thế trên ampe kế. Ở cách mắc (b), vôn kế nối đúng vào hai đầu điện trở, nhưng ampe kế đặt phía trước nhánh nên số chỉ của nó bằng dòng qua điện trở cộng với dòng qua vôn kế.

#### Ví dụ 26.10: Đo điện trở, cách thứ nhất

Trong cách mắc Hình 26.16a, vôn kế chỉ $12{,}0\,\mathrm V$ và ampe kế chỉ $0{,}100\,\mathrm A$. Điện trở vôn kế là $R_V=10\,000\,\Omega$, còn điện trở ampe kế là $R_A=2{,}00\,\Omega$. Hãy tìm điện trở $R$ và công suất tỏa nhiệt trong điện trở.

**Tóm tắt đề bài:** $V=12{,}0\,\mathrm V$, $I=0{,}100\,\mathrm A$, $R_A=2{,}00\,\Omega$ và $R_V=10\,000\,\Omega$. Vôn kế đo điện trở $R$ nối tiếp với ampe kế.

**Hướng đi:**

- Ampe kế nối tiếp nên đọc đúng dòng qua $R$.
- Tính độ giảm thế trên ampe kế rồi trừ nó khỏi số chỉ vôn kế, vì vôn kế đặt ngoài cả hai linh kiện.

**Thực hiện:** Độ giảm thế trên ampe kế là:

$$
\begin{aligned}
&V_{bc} = IR_A\\
&\quad =(0{,}100\,\mathrm A)(2{,}00\,\Omega)\\
&\quad =0{,}200\,\mathrm V.
\end{aligned}
$$

Hiệu điện thế thực trên điện trở cần đo bằng số chỉ vôn kế trừ phần vừa tính:

$$
\begin{aligned}
&V_{ab} = V-V_{bc}\\
&\quad =12{,}0\,\mathrm V-0{,}200\,\mathrm V\\
&\quad =11{,}8\,\mathrm V.
\end{aligned}
$$

Vì dòng qua điện trở là $0{,}100\,\mathrm A$:

$$
\begin{aligned}
&R = \frac{V_{ab}}{I}\\
&\quad =\frac{11{,}8\,\mathrm V}{0{,}100\,\mathrm A}\\
&\quad =118\,\Omega.
\end{aligned}
$$

Công suất tỏa nhiệt trong điện trở là:

$$
\begin{aligned}
&P = V_{ab}I\\
&\quad =(11{,}8\,\mathrm V)(0{,}100\,\mathrm A)\\
&\quad =1{,}18\,\mathrm W.
\end{aligned}
$$

**Đánh giá:** Tính bằng $P=I^2R$ cũng cho $1{,}18\,\mathrm W$. Công suất phải tính từ hiệu điện thế và dòng thực qua điện trở, không dùng trực tiếp điện áp tổng của cả cụm.

**Ý chính:** Để đo điện trở và công suất theo cách mắc (a), ampe kế nối tiếp với điện trở còn vôn kế mắc song song với cả điện trở lẫn ampe kế. Cách này đo đúng dòng qua điện trở nhưng cần hiệu chỉnh số chỉ vôn kế.

#### Ví dụ 26.11: Đo điện trở, cách thứ hai

Giữ nguyên hai dụng cụ đo nhưng mắc theo Hình 26.16b. Vôn kế vẫn chỉ $12{,}0\,\mathrm V$ và ampe kế vẫn chỉ $0{,}100\,\mathrm A$. Hãy tìm điện trở $R$ và công suất tỏa nhiệt trong nó.

**Tóm tắt đề bài:** $V_{ab}=12{,}0\,\mathrm V$, $I_A=0{,}100\,\mathrm A$ và $R_V=10\,000\,\Omega$. Ampe kế đo tổng dòng qua điện trở và vôn kế.

**Hướng đi:**

- Tính dòng qua vôn kế từ hiệu điện thế và điện trở của nó.
- Trừ dòng ấy khỏi số chỉ ampe kế, vì ampe kế đo tổng dòng qua điện trở và vôn kế.

**Thực hiện:** Dòng qua vôn kế và dòng qua điện trở là:

$$
\begin{aligned}
&I_V = \frac{V_{ab}}{R_V}\\
&\quad =\frac{12{,}0\,\mathrm V}{10\,000\,\Omega}\\
&\quad =1{,}20\,\mathrm{mA},\\
&I = I_A-I_V\\
&\quad =0{,}100\,\mathrm A-0{,}00120\,\mathrm A\\
&\quad =0{,}0988\,\mathrm A.
\end{aligned}
$$

Do vôn kế mắc trực tiếp vào hai đầu điện trở:

$$
\begin{aligned}
&R = \frac{V_{ab}}{I}\\
&\quad =\frac{12{,}0\,\mathrm V}{0{,}0988\,\mathrm A}\\
&\quad \approx121\,\Omega.
\end{aligned}
$$

Công suất tỏa nhiệt trong điện trở là:

$$
\begin{aligned}
&P = V_{ab}I\\
&\quad =(12{,}0\,\mathrm V)(0{,}0988\,\mathrm A)\\
&\quad \approx1{,}19\,\mathrm W.
\end{aligned}
$$

**Đánh giá:** Nếu coi dụng cụ là lý tưởng, ta sẽ tính $R=120\,\Omega$ và $P=1{,}2\,\mathrm W$. Các giá trị hiệu chỉnh lần lượt là $121\,\Omega$ và $1{,}19\,\mathrm W$, khá gần vì điện trở ampe kế nhỏ và điện trở vôn kế lớn so với điện trở đang đo. Khi cần độ chính xác cao, phải tính cả ảnh hưởng của dụng cụ.

**Ý chính:** Ở cách mắc (b), vôn kế mắc song song với điện trở và ampe kế đặt phía sau nút phân nhánh. Vôn kế đo đúng hiệu điện thế trên điện trở, còn ampe kế đọc tổng dòng qua điện trở và vôn kế.

### Ôm kế và vôn kế cân bằng

Một cách đo điện trở khác là **ôm kế**. Nó gồm điện kế, điện trở phụ có thể điều chỉnh và một nguồn điện mắc nối tiếp. Nối điện trở cần đo giữa hai đầu $x$ và $y$ của ôm kế.

![Hình 26.17: Mạch ôm kế có điện trở điều chỉnh](../img/young-26/hinh-26-17.png)

**Hình 26.17:** Điện trở cần đo được nối giữa $x$ và $y$. Trước khi đo, chập hai đầu này rồi chỉnh điện trở phụ đến khi kim chỉ toàn thang, tức vạch $0\,\Omega$.

Trước mỗi phép đo, chập $x$ với $y$ để điện trở ngoài bằng không rồi chỉnh điện trở phụ đến khi kim lệch toàn thang. Khi hai đầu để hở, điện trở ngoài rất lớn, dòng gần bằng không và kim không lệch. Những giá trị ở giữa tạo độ lệch trung gian, nhờ đó thang đo có thể được hiệu chuẩn trực tiếp theo điện trở. Dòng lớn ứng với điện trở nhỏ, vì vậy chiều đọc của thang ôm ngược với thang dòng điện.

Khi cần độ chính xác cao, dụng cụ điện tử với số chỉ trực tiếp thường được ưu tiên. Vôn kế số có thể có điện trở vào cỡ $100\,\mathrm{M\Omega}$.

![Hình 26.18: Đồng hồ vạn năng số đo điện áp, dòng điện và điện trở](../img/young-26/hinh-26-18.png)

**Hình 26.18:** Đồng hồ vạn năng số có thể chuyển giữa thang đo điện áp, dòng điện và điện trở.

**Ứng dụng y sinh:** Trong phép đo điện cơ, một kim mảnh mang hai điện cực được đưa vào cơ ở bàn tay. Vôn kế nhạy đo hiệu điện thế giữa hai điện cực để bác sĩ khảo sát hoạt động điện của cơ, qua đó hỗ trợ chẩn đoán bệnh thần kinh cơ.

![Ứng dụng điện cơ: Kim đo có hai điện cực khảo sát hoạt động điện của cơ bàn tay](../img/young-26/ung-dung-dien-co.png)

Một dụng cụ khác là **chiết áp cân bằng**, dùng để đo suất điện động mà không rút dòng từ nguồn cần đo. Dây điện trở đều $ab$ được nối với nguồn chuẩn $\mathcal E_1$. Nguồn chưa biết $\mathcal E_2$ được mắc qua điện kế vào một tiếp điểm trượt $c$.

![Hình 26.19: Mạch chiết áp cân bằng suất điện động](../img/young-26/hinh-26-19.png)

**Hình 26.19:** Tiếp điểm trượt trên dây điện trở làm thay đổi điện trở đoạn dây $cb$. Điều chỉnh vị trí cho đến khi điện kế không lệch.

Khi điện kế không lệch, dòng qua nguồn cần đo bằng không. Gọi $I$ là dòng do nguồn chuẩn tạo ra trên dây. Khi đó, hiệu điện thế trên đoạn $cb$ cân bằng với suất điện động cần đo:

$$
\mathcal E_2=IR_{cb}.
$$

Ta hiệu chuẩn chiết áp bằng một nguồn có suất điện động đã biết. Sau đó, với nguồn chưa biết, đo chiều dài đoạn dây $cb$ tại điểm cân bằng. Dây đồng chất có điện trở tỉ lệ với chiều dài, nên ta suy ra suất điện động. Cách đo này cần hiệu điện thế trên toàn dây lớn hơn suất điện động cần đo.

Từ “chiết áp” cũng được dùng cho biến trở có con chạy, thường điều chỉnh bằng trục xoay và núm vặn.

#### Kiểm tra hiểu mục 26.3

Muốn đo dòng điện qua điện trở $2\,\Omega$ trong Hình 26.12 và hiệu điện thế trên chính điện trở ấy:

- **(a)** Ta mắc ampe kế và vôn kế như thế nào? (i) Cả hai mắc nối tiếp với điện trở. (ii) Ampe kế mắc nối tiếp với điện trở, vôn kế nối giữa hai đầu điện trở. (iii) Ampe kế nối giữa hai đầu điện trở, vôn kế mắc nối tiếp. (iv) Cả hai nối giữa hai đầu điện trở.
- **(b)** Điện trở của hai dụng cụ nên như thế nào? (i) Cả hai lớn hơn nhiều so với $2\,\Omega$. (ii) Điện trở ampe kế lớn hơn nhiều, điện trở vôn kế nhỏ hơn nhiều. (iii) Điện trở ampe kế nhỏ hơn nhiều, điện trở vôn kế lớn hơn nhiều. (iv) Cả hai nhỏ hơn nhiều so với $2\,\Omega$.

<details><summary>Lời giải kiểm tra hiểu</summary>

**Tóm tắt:** Cần đo dòng trong nhánh chứa điện trở $2\,\Omega$ và hiệu điện thế giữa hai đầu điện trở đó.

**Hướng đi:**

- Ampe kế mắc nối tiếp để dòng nhánh đi qua dụng cụ.
- Vôn kế mắc song song với điện trở để đo hiệu điện thế trên hai đầu nó.
- Điện trở ampe kế cần nhỏ và điện trở vôn kế cần lớn, vì các giá trị đó hạn chế ảnh hưởng của phép đo lên mạch.

Đáp án là (a) (ii) và (b) (iii). Ampe kế mắc nối tiếp với điện trở $2\,\Omega$, còn vôn kế mắc song song giữa hai đầu điện trở. Điện trở ampe kế nên nhỏ hơn nhiều so với $2\,\Omega$, còn điện trở vôn kế nên lớn hơn nhiều để dụng cụ ít làm thay đổi dòng và hiệu điện thế cần đo.

</details>

### Tóm tắt

- Điện kế d’Arsonval dựa vào độ lệch của cuộn dây, độ lệch tỉ lệ với dòng điện qua cuộn.
- Ampe kế mắc nối tiếp và cần có điện trở nhỏ. Điện trở rẽ song song cho phép mở rộng thang dòng.
- Vôn kế mắc song song và cần có điện trở lớn. Điện trở nối tiếp cho phép mở rộng thang điện áp.
- Khi đo điện trở và công suất, cần dùng dòng qua linh kiện và hiệu điện thế thực trên linh kiện. Điện trở trong của dụng cụ đo có thể làm thay đổi số chỉ.
- Ôm kế dùng dòng điện để xác định điện trở. Chiết áp cân bằng đo suất điện động tại vị trí dòng qua nguồn cần đo bằng không.

### Tài liệu tham khảo

Young, H. D., & Freedman, R. A. *University Physics with Modern Physics* (ấn bản 15, mục 26.3, tr. 854–858). Pearson.
