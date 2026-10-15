## Năng lượng cần để tiến gần tốc độ ánh sáng

Định luật công–động năng được xây dựng từ định luật chuyển động. Khi động lượng và quan hệ lực–gia tốc thay đổi, ta phải tính lại động năng. Điểm xuất phát vẫn là công của lực dọc đường đi, không phải thay một “khối lượng mới” vào biểu thức động năng Newton.

### 1. Suy ra động năng từ công

Xét chuyển động thẳng dọc trục $x$. Hợp lực dọc vận tốc thực hiện công từ $x_1$ đến $x_2$:

$$
W=\int_{x_1}^{x_2}F\,dx.
$$

Đặt $q=1-v_x^2/c^2$ để viết gọn mẫu của quan hệ lực. Thay $F=ma/q^{3/2}$ vào cho

$$
W=\int_{x_1}^{x_2}\frac{ma}{q^{3/2}}\,dx.
\tag{37.34}
$$

Nếu hạt bắt đầu từ nghỉ và kết thúc với tốc độ $v$, công ấy chính là động năng $K$. Ta cần đổi biến tích phân từ $x$ sang $v_x$. Vì $a=dv_x/dt$ và $v_x=dx/dt$,

$$
a\,dx=v_x\,dv_x.
$$

Do đó,

$$
K=\int_0^v\frac{mv_x}{q^{3/2}}\,dv_x.
\tag{37.35}
$$

Để mở bước tích phân, dùng $q=1-v_x^2/c^2$. Khi đó $dq=-2v_x\,dv_x/c^2$. Hai cận theo $q$ lần lượt là 1 và $q_f=1-v^2/c^2$. Vì $\int q^{-3/2}dq=-2q^{-1/2}$, ta được

$$
K=mc^2(q_f^{-1/2}-1).
$$

**Động năng tương đối tính** vì thế là

$$
\begin{aligned}
K&=\frac{mc^2}{\sqrt{1-v^2/c^2}}-mc^2\\
&=(\gamma-1)mc^2.
\end{aligned}
\tag{37.36}
$$

Khi $v$ tiến gần $c$, động năng tăng không bị chặn. Đây là cách biểu diễn bằng năng lượng của giới hạn tốc độ đối với hạt có khối lượng nghỉ dương.

![Hình 37.21: Động năng tương đối tính và động năng Newton gần nhau ở tốc độ nhỏ, nhưng khác rất lớn khi v tiến gần c.](../img/young-37/hinh-37-21.png)

### 2. Giới hạn Newton

Với $F=(1+x)^n$, ba hệ số đầu của khai triển nhị thức là $a_0=1$, $a_1=n$ và

$$
a_2=\frac{n(n-1)}2.
$$

Viết tường minh các số hạng đầu:

$$
F=a_0+a_1x+a_2x^2+\cdots.
$$

Đặt $b=v/c$. Với $b$ nhỏ, trường hợp $n=-1/2$, $x=-b^2$ cho

$$
\gamma=1+\frac12b^2+\frac38b^4+\cdots.
$$

Thay vào $K=(\gamma-1)mc^2$ và nhân từng số hạng. Đặt tên cho số hạng Newton và hiệu chỉnh bậc bốn lần lượt là

$$
K_{\rm N}=\frac12mv^2,
$$

$$
K_4=\frac38\frac{mv^4}{c^2}.
$$

Khai triển động năng khi ấy là

$$
K=K_{\rm N}+K_4+\cdots.
\tag{37.37}
$$

Số hạng đầu là động năng Newton. Các hiệu chỉnh chứa lũy thừa cao hơn của $v/c$, nên có thể bỏ qua khi tốc độ đủ nhỏ so với mức chính xác cần đạt. Biểu thức tương đối tính giữ được thành công của cơ học Newton trong miền ấy.

### 3. Năng lượng nghỉ và năng lượng toàn phần

Động năng trong (37.36) là hiệu giữa một số hạng phụ thuộc chuyển động và một năng lượng $mc^2$ không phụ thuộc chuyển động. Ta gọi $E_0=mc^2$ là **năng lượng nghỉ**. Năng lượng toàn phần là

$$
\begin{aligned}
E&=K+mc^2\\
&=\frac{mc^2}{\sqrt{1-v^2/c^2}}\\
&=\gamma mc^2.
\end{aligned}
\tag{37.38}
$$

Khi hạt đứng yên, $K=0$ nhưng $E=mc^2$ vẫn khác không. Năng lượng nghỉ được kiểm tra qua các quá trình biến đổi hạt. Chẳng hạn, pion trung hòa có thể phân rã thành bức xạ điện từ. Nếu pion ban đầu đứng yên, tổng năng lượng bức xạ bằng năng lượng nghỉ ban đầu của nó.

Trong các quá trình tạo hoặc hủy hạt, tổng khối lượng nghỉ riêng lẻ có thể thay đổi. Năng lượng toàn phần của hệ cô lập vẫn bảo toàn. Nếu tổng năng lượng nghỉ giảm, phần năng lượng ngoài năng lượng nghỉ phải tăng một lượng tương ứng, và ngược lại.

Vì vậy, bảo toàn khối lượng theo nghĩa cổ điển và bảo toàn năng lượng cần được đặt trong một mô tả rộng hơn. Không được khẳng định tổng khối lượng nghỉ của các hạt luôn bảo toàn riêng trong mọi phản ứng.

Trong phân hạch hạt nhân uranium, tổng khối lượng nghỉ các mảnh có thể nhỏ hơn khối lượng nghỉ hạt nhân ban đầu. Năng lượng chênh lệch có thể trở thành động năng, bức xạ và nhiệt. Ở nhà máy điện hạt nhân, nhiệt được dùng tạo hơi để vận hành turbine và máy phát.

![Ứng dụng: Phòng điều khiển nhà máy điện hạt nhân theo dõi quá trình chuyển một phần năng lượng nghỉ hạt nhân thành nhiệt và năng lượng phát điện.](../img/young-37/ung-dung-37-nang-luong-hat-nhan.png)

### 4. Liên hệ trực tiếp năng lượng với động lượng

Từ $E=\gamma mc^2$ và $p=\gamma mv$, ta có

$$
\left(\frac{E}{mc^2}\right)^2=\frac1{1-v^2/c^2},
$$

$$
\left(\frac{p}{mc}\right)^2=\frac{v^2/c^2}{1-v^2/c^2}.
$$

Lấy hiệu hai biểu thức rồi nhân với $m^2c^4$ cho

$$
E^2=(mc^2)^2+(pc)^2.
\tag{37.39}
$$

Ở trạng thái nghỉ $p=0$, ta tìm lại $E=mc^2$. Hệ thức cũng cho phép một hạt có năng lượng và động lượng dù khối lượng nghỉ bằng không. Khi $m=0$,

$$
E=pc.
\tag{37.40}
$$

Hạt không khối lượng có năng lượng dương không có hệ nghỉ và truyền trong chân không ở tốc độ $c$. Photon là ví dụ sẽ được nghiên cứu ở chương sau. Sự phát và hấp thụ photon đi kèm thay đổi năng lượng và động lượng của nguyên tử hoặc hạt nhân.

### Ví dụ 37.10: Electron được gia tốc qua điện thế

(a) Tính năng lượng nghỉ electron theo joule và electronvolt. Cho $m_e=9{,}109\times10^{-31}\,\mathrm{kg}$ và $e=1{,}602\times10^{-19}\,\mathrm C$. (b) Tìm tốc độ electron bắt đầu từ nghỉ khi đi qua độ tăng điện thế $20{,}0\,\mathrm{kV}$ hoặc $5{,}00\,\mathrm{MV}$.

**Nhận dạng và chuẩn bị:** Dùng $E_0=m_ec^2$. Công lực điện làm electron tăng động năng $e\Delta V$ vì điện tích electron là $-e$. Trong phép tính này, dùng $c=2{,}998\times10^8\,\mathrm{m/s}$.

**Thực hiện:** Phần (a) cho

$$
E_0\approx8{,}187\times10^{-14}\,\mathrm J.
$$

Chia cho năng lượng tương đương một electronvolt, ta được $E_0\approx5{,}11\times10^5\,\mathrm{eV}=0{,}511\,\mathrm{MeV}$.

Ở (b), bảo toàn năng lượng cho

$$
\gamma=1+\frac{e\Delta V}{E_0}.
$$

Sau đó dùng $v/c=\sqrt{1-1/\gamma^2}$:

| Độ tăng điện thế | $\gamma$ | Tốc độ |
| --- | --- | --- |
| $20{,}0\,\mathrm{kV}$ | $1{,}039$ | $0{,}272c$ |
| $5{,}00\,\mathrm{MV}$ | $10{,}78$ | $0{,}996c$ |

Trường hợp $20{,}0\,\mathrm{kV}$ cho tốc độ khoảng $8{,}15\times10^7\,\mathrm{m/s}$. Các điện thế cao như trường hợp thứ hai được dùng trong những hệ tạo tia X năng lượng cao.

**Đánh giá:** Động năng $20{,}0\,\mathrm{keV}$ nhỏ hơn 4% năng lượng nghỉ electron, còn $5{,}00\,\mathrm{MeV}$ lớn hơn nhiều năng lượng nghỉ. Vì thế, trường hợp sau cho tốc độ rất gần $c$.

Phải phân biệt ba năng lượng: Electron có năng lượng nghỉ khoảng $0{,}511\,\mathrm{MeV}$, electron được gọi là “electron 5 MeV” có động năng $5{,}00\,\mathrm{MeV}$, và năng lượng toàn phần của nó khoảng $5{,}51\,\mathrm{MeV}$. Đơn vị điện thế là volt, còn đơn vị năng lượng ở đây là electronvolt.

### Ví dụ 37.11: Va chạm tạo pion

Hai proton có cùng khối lượng nghỉ $m_p=1{,}67\times10^{-27}\,\mathrm{kg}$ bay ngược chiều với cùng tốc độ. Chúng va chạm và vẫn tồn tại, đồng thời tạo một pion trung hòa có khối lượng nghỉ $m_\pi=2{,}40\times10^{-28}\,\mathrm{kg}$. Nếu cả ba hạt đều đứng yên sau va chạm, tìm tốc độ ban đầu mỗi proton.

![Hình 37.22: Hai proton có động lượng ban đầu đối nhau. Ở trạng thái cuối được xét, tổng động năng ban đầu trở thành năng lượng nghỉ của pion mới.](../img/young-37/hinh-37-22.png)

**Nhận dạng và chuẩn bị:** Tổng động lượng ban đầu bằng không nên trạng thái cuối cả ba hạt đứng yên phù hợp bảo toàn động lượng. Bảo toàn năng lượng toàn phần liên hệ hai năng lượng ban đầu với tổng năng lượng nghỉ cuối.

**Thực hiện:** Ta có

$$
2\gamma m_pc^2=2m_pc^2+m_\pi c^2.
$$

Do đó,

$$
\gamma=1+\frac{m_\pi}{2m_p}\approx1{,}072.
$$

Tốc độ ban đầu là

$$
v=c\sqrt{1-\frac1{\gamma^2}}\approx0{,}360c.
$$

**Đánh giá:** Động năng mỗi proton khoảng $67{,}4\,\mathrm{MeV}$ khi tính trực tiếp từ các khối lượng và hằng số đã làm tròn. Tổng của hai giá trị bằng khoảng $135\,\mathrm{MeV}$, đúng bằng năng lượng nghỉ pion trong cùng phép tính.

Động năng không bảo toàn riêng trong va chạm này. Năng lượng toàn phần và động lượng đều bảo toàn, còn động năng ban đầu chuyển thành năng lượng nghỉ của hạt mới. Mỗi proton vẫn giữ nguyên khối lượng nghỉ của nó.

### Câu hỏi tự kiểm tra 37.8

Một proton bắt đầu từ nghỉ, chịu lực không đổi luôn cùng hướng chuyển động. So với động năng tăng trong mét đầu tiên, động năng tăng khi đi thêm một mét ở tốc độ gần $0{,}99c$ là bao nhiêu?

- (i) Bằng nhau.
- (ii) Lớn hơn.
- (iii) Nhỏ hơn.

<details><summary>Xem đáp án và giải thích</summary>

Chọn (i). Công của lực không đổi trên mỗi quãng đường một mét bằng nhau, nên theo định lý công–động năng, động năng tăng như nhau.

Ở tốc độ gần $c$, cùng một phần động năng tăng thêm chỉ làm tốc độ tăng ít hơn. Câu hỏi hỏi độ tăng động năng, không hỏi độ tăng tốc độ.

</details>
