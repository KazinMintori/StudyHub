## Bảo toàn động lượng khi đổi hệ quy chiếu

Nếu hai vật tương tác trong một hệ cô lập, tổng động lượng phải được bảo toàn. Là một định luật vật lý, kết luận ấy phải đúng trong mọi hệ quán tính. Nhưng khi vận tốc biến đổi theo Lorentz, biểu thức Newton $\vec p=m\vec v$ không còn làm các phép tính va chạm nhất quán giữa mọi hệ.

Ta cần thay định nghĩa động lượng, đồng thời giữ nguyên giới hạn Newton khi vận tốc nhỏ. Trong phần này, khối lượng $m$ luôn là khối lượng đo trong hệ nghỉ của hạt, còn gọi là khối lượng nghỉ.

### 1. Định nghĩa động lượng tương đối tính

Với hạt có khối lượng nghỉ dương $m$ và vận tốc $\vec v$, **động lượng tương đối tính** là

$$
\vec p=\frac{m\vec v}{\sqrt{1-v^2/c^2}}.
\tag{37.27}
$$

Động lượng cùng hướng vận tốc. Ở tốc độ nhỏ, mẫu số gần một và ta tìm lại gần đúng Newton. Khi tốc độ tiến đến $c$, độ lớn động lượng tăng không bị chặn.

![Hình 37.20: Động lượng tương đối tính lớn hơn mv ở cùng tốc độ và tăng không bị chặn khi v tiến gần c.](../img/young-37/hinh-37-20.png)

Biểu thức này được nêu ở đây như kết quả động lực học phù hợp với bảo toàn động lượng và thí nghiệm. Không thể suy ra nó bằng cách chỉ cộng các vận tốc theo Galileo.

### 2. Dạng đúng của định luật II Newton

Dạng tổng quát theo động lượng vẫn là

$$
\vec F=\frac{d\vec p}{dt}.
\tag{37.28}
$$

Thay động lượng mới vào cho

$$
\vec F=\frac d{dt}\left(\frac{m\vec v}{\sqrt{1-v^2/c^2}}\right).
\tag{37.29}
$$

Cả vận tốc lẫn mẫu số có thể phụ thuộc thời gian. Vì vậy, hợp lực không còn luôn bằng khối lượng nghỉ nhân gia tốc.

Nếu lực và vận tốc cùng một đường thẳng, lấy đạo hàm theo quy tắc tích cho

$$
F=\frac{ma}{(1-v^2/c^2)^{3/2}}.
\tag{37.30}
$$

Ở đây $F,a$ là các thành phần có dấu theo đường chuyển động. Với một lực dọc cố định, gia tốc giảm khi tốc độ tăng:

$$
a=\frac Fm(1-v^2/c^2)^{3/2}.
$$

Khi $v$ tiến gần $c$, gia tốc do lực hữu hạn tiến về không. Không thể dùng lực hữu hạn để đưa hạt có khối lượng nghỉ dương đến hoặc vượt $c$.

### 3. Hệ số Lorentz của hạt và cách gọi khối lượng

Đặt $\gamma=1/\sqrt{1-v^2/c^2}$ theo tốc độ hạt trong hệ đang xét. Đây vẫn là cùng hệ số Lorentz, nhưng vận tốc được dùng là tốc độ hệ nghỉ hạt đối với người quan sát. Nó cần được phân biệt với ký hiệu $u$ cho vận tốc hai hệ tùy ý ở các mục trước.

Ta có dạng gọn

$$
\vec p=\gamma m\vec v.
\tag{37.31}
$$

Trong lịch sử, người ta có thể gọi $m_r=\gamma m$ là “khối lượng tương đối tính”, rồi viết $\vec p=m_r\vec v$. Đại lượng này phụ thuộc hệ quy chiếu. Khối lượng nghỉ $m$ của cùng hạt vẫn không đổi.

Việc đổi tên không cho phép thay $m$ bằng $m_r$ trong mọi công thức Newton. Nói chung không có $\vec F=m_r\vec a$, và động năng cũng không bằng $m_rv^2/2$. Để tránh nhập nhằng, ta dùng $m$ bất biến và giữ rõ các hệ số Lorentz trong công thức.

Với một hệ nhiều hạt trong hệ khối tâm, chuyển động nội cũng đóng góp vào khối lượng của toàn hệ. Chẳng hạn, năng lượng chuyển động nhiệt của các phân tử làm khối lượng của khí nóng khác khí lạnh, dù khối lượng nghỉ mỗi phân tử không đổi. Không được chỉ cộng khối lượng nghỉ từng hạt rồi bỏ năng lượng nội và liên kết.

### 4. Lực dọc và lực ngang

Với lực cùng đường vận tốc, (37.30) viết thành

$$
F_\parallel=\gamma^3ma_\parallel.
\tag{37.32}
$$

Các máy gia tốc thẳng dùng lực dọc đường bay để tăng tốc hạt. Chúng có ứng dụng trong y học cũng như nghiên cứu hạt nhân và hạt cơ bản.

Trong nhiều máy gia tốc vòng, lực vuông góc vận tốc khiến hạt đổi hướng nhưng không đổi tốc độ. Khi đó hệ số Lorentz không đổi tức thời và

$$
F_\perp=\gamma ma_\perp.
\tag{37.33}
$$

Nếu chuyển động tròn đều, gia tốc hướng vào tâm và có độ lớn $a=v^2/R$. Lực vuông góc vận tốc không sinh công, nên không làm đổi động năng.

Trong trường hợp tổng quát, phân tích lực thành các thành phần dọc và ngang vận tốc tại thời điểm xét. Hai thành phần gia tốc tương ứng được chia cho $\gamma^3m$ và $\gamma m$. Vì các hệ số khác nhau, hướng gia tốc nói chung không trùng hướng hợp lực.

### Ví dụ 37.9: Electron chịu điện trường

Electron có khối lượng nghỉ $9{,}11\times10^{-31}\,\mathrm{kg}$ và điện tích $-1{,}60\times10^{-19}\,\mathrm C$ chuyển động ngược chiều điện trường đều có độ lớn $5{,}00\times10^5\,\mathrm{N/C}$. Bỏ qua các lực khác.

(a) Tìm độ lớn động lượng và gia tốc tại các tốc độ $0{,}010c$, $0{,}90c$ và $0{,}99c$. (b) Nếu lực có cùng độ lớn nhưng vuông góc vận tốc, các gia tốc bằng bao nhiêu?

**Nhận dạng và chuẩn bị:** Lực điện ngược chiều điện trường do electron mang điện âm. Vì electron đang chuyển động ngược điện trường, lực cùng hướng vận tốc ở phần (a). Độ lớn lực là

$$
F=|q|E=8{,}00\times10^{-14}\,\mathrm N.
$$

**Thực hiện:** Tính $p=\gamma mv$, $a_\parallel=F/(\gamma^3m)$ và $a_\perp=F/(\gamma m)$.

| $v/c$ | $\gamma$ | $p$ ($\mathrm{kg\,m/s}$) |
| --- | --- | --- |
| $0{,}010$ | $1{,}00005$ | $2{,}7\times10^{-24}$ |
| $0{,}90$ | $2{,}294$ | $5{,}6\times10^{-22}$ |
| $0{,}99$ | $7{,}089$ | $1{,}9\times10^{-21}$ |

| $v/c$ | $a_\parallel$ ($\mathrm{m/s^2}$) | $a_\perp$ ($\mathrm{m/s^2}$) |
| --- | --- | --- |
| $0{,}010$ | $8{,}8\times10^{16}$ | $8{,}8\times10^{16}$ |
| $0{,}90$ | $7{,}3\times10^{15}$ | $3{,}8\times10^{16}$ |
| $0{,}99$ | $2{,}5\times10^{14}$ | $1{,}2\times10^{16}$ |

**Đánh giá:** Ở tốc độ nhỏ nhất, hai gia tốc gần cùng giá trị Newton. Khi tăng tốc độ, gia tốc dọc giảm nhanh hơn gia tốc ngang. Với cùng độ lớn lực, tỉ số $a_\perp/a_\parallel=\gamma^2$.

Động lượng ở $0{,}99c$ lớn hơn ba lần động lượng ở $0{,}90c$, dù tốc độ chỉ tăng ít. Hệ số Lorentz làm động lượng khác ngày càng nhiều so với $mv$ khi đến gần giới hạn tốc độ.

### Câu hỏi tự kiểm tra 37.7

Khi tăng tốc độ một hạt lên gấp đôi, độ lớn động lượng tăng theo hệ số nào?

- (i) Đúng bằng 2.
- (ii) Lớn hơn 2.
- (iii) Một giá trị từ 1 đến 2, phụ thuộc khối lượng hạt.

<details><summary>Xem đáp án và giải thích</summary>

Chọn (ii), với điều kiện tốc độ ban đầu nhỏ hơn $c/2$ để có thể tăng gấp đôi mà vẫn dưới $c$. Tử số $mv$ tăng gấp đôi, còn mẫu $\sqrt{1-v^2/c^2}$ giảm. Vì vậy, động lượng tăng hơn gấp đôi.

Chỉ trong gần đúng tốc độ rất nhỏ so với $c$, mức tăng mới gần bằng hai lần.

</details>
