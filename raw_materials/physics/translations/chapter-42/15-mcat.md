## Bài tập đoạn văn theo định dạng MCAT: Cảm biến nhiệt độ diode

**Đoạn văn mở đầu: Cảm biến nhiệt độ diode (Diode Temperature Sensor)**. Đặc tuyến dòng điện – điện áp của một diode chuyển tiếp p-n phân cực thuận phụ thuộc rất mạnh vào nhiệt độ, như được thể hiện trong hình vẽ. Nhờ tính chất này, các diode bán dẫn có thể được sử dụng làm cảm biến đo nhiệt độ điện tử. Trong vận hành thực tế, điện áp đặt vào được mạch điều khiển tự động điều chỉnh liên tục để giữ cho cường độ dòng điện chạy qua diode không đổi ở một giá trị quy định chuẩn, chẳng hạn như $100\,\mathrm{mA}$, và nhiệt độ của môi trường được xác định trực tiếp từ phép đo điện áp thuận tại dòng điện không đổi đó.

![Hình MCAT-42: Đặc tuyến dòng điện – điện áp của diode chuyển tiếp p-n khi phân cực thuận ở hai mốc nhiệt độ $T = 25^\circ\mathrm{C}$ và $T = 150^\circ\mathrm{C}$.](./img/young-42/hinh-doan-van-diot.png)

---

### 42.56

Độ nhạy của một nhiệt kế diode phụ thuộc vào mức độ thay đổi của điện áp đối với một độ biến thiên nhiệt độ cho trước, với cường độ dòng điện được giữ không đổi. Độ nhạy của nhiệt kế diode này, hoạt động ở dòng điện cố định $100\,\mathrm{mA}$, đối với độ biến thiên nhiệt độ từ $25^\circ\mathrm{C}$ đến $150^\circ\mathrm{C}$ bằng bao nhiêu?
(a) $+0{,}2\,\mathrm{mV/^\circ C}$;
(b) $+2{,}0\,\mathrm{mV/^\circ C}$;
(c) $-0{,}2\,\mathrm{mV/^\circ C}$;
(d) $-2{,}0\,\mathrm{mV/^\circ C}$.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tính độ nhạy $S = \frac{\Delta V}{\Delta T}$ của cảm biến nhiệt độ diode ở dòng không đổi $I = 100\,\mathrm{mA}$ khi nhiệt độ tăng từ $25^\circ\mathrm{C}$ lên $150^\circ\mathrm{C}$.

**Hướng đi:**

- **Đọc đồ thị tại dòng điện cố định**: Trên trục tung, kẻ đường nằm ngang ứng với dòng điện $I = 100\,\mathrm{mA} = 0{,}10\,\mathrm{A}$, gióng sang hai đường đặc tuyến nhiệt độ để đọc các giá trị điện áp thuận tương ứng.
- **Độ nhạy cảm biến**: Định nghĩa bằng tỉ số giữa độ biến thiên điện áp và độ biến thiên nhiệt độ: $S = \frac{V(150^\circ\mathrm{C}) - V(25^\circ\mathrm{C})}{150^\circ\mathrm{C} - 25^\circ\mathrm{C}}$.

Quan sát đồ thị thực nghiệm tại mốc dòng điện không đổi $I = 0{,}10\,\mathrm{A} = 100\,\mathrm{mA}$:
- Gióng sang đường cong màu xanh ở nhiệt độ $T_1 = 25^\circ\mathrm{C}$, ta đọc được giá trị điện áp thuận:
$$
V_1 \approx 0{,}77\,\mathrm{V}
$$
- Gióng sang đường cong màu đỏ ở nhiệt độ cao $T_2 = 150^\circ\mathrm{C}$, ta đọc được giá trị điện áp thuận:
$$
V_2 \approx 0{,}52\,\mathrm{V}
$$

Độ biến thiên điện áp là:

$$
\begin{aligned}
\Delta V &= V_2 - V_1 \\
&= 0{,}52\,\mathrm{V} - 0{,}77\,\mathrm{V} \\
&= -250\,\mathrm{mV}
\end{aligned}
$$

Độ biến thiên nhiệt độ tương ứng:

$$
\begin{aligned}
\Delta T &= 150^\circ\mathrm{C} - 25^\circ\mathrm{C} \\
&= 125^\circ\mathrm{C}
\end{aligned}
$$

Độ nhạy của nhiệt kế diode bằng:

$$
\begin{aligned}
S &= \frac{\Delta V}{\Delta T} \\
&= \frac{-250\,\mathrm{mV}}{125^\circ\mathrm{C}} \\
&= -2{,}0\,\mathrm{mV/^\circ C}
\end{aligned}
$$

Dấu âm cho thấy khi nhiệt độ tăng lên, điện áp mở của diode giảm tuyến tính với tốc độ khoảng $2{,}0\,\mathrm{mV}$ cho mỗi độ C tăng thêm, hoàn toàn phù hợp với tính chất vật lý chuẩn của diode silic.

![Hình 42.56: Đường chuẩn nhiệt độ tuyến tính của cảm biến diode ở dòng điện không đổi $100\,\mathrm{mA}$ với độ nhạy $S = -2{,}0\,\mathrm{mV/^\circ C}$.](./img/young-42/loi-giai-d-09.svg)

**Đáp án đúng:** **(d)**.

</details>

### 42.57

Phát biểu nào sau đây giải thích đúng nhất sự phụ thuộc nhiệt độ của đặc tuyến dòng điện – điện áp mà đồ thị thể hiện? Ở nhiệt độ cao hơn:
(a) Vùng cấm rộng hơn, do đó các cặp electron–lỗ trống có nhiều năng lượng hơn, làm cho dòng điện ở một điện áp cho trước lớn hơn.
(b) Có nhiều electron hơn có thể chuyển lên dải dẫn, làm cho dòng điện ở một điện áp cho trước lớn hơn.
(c) Toàn bộ các electron trong dải hóa trị chuyển lên dải dẫn, và diode hành xử như một kim loại và tuân theo định luật Ohm.
(d) Các nguyên tử tạp chất acceptor và donor được tự do di chuyển qua vật liệu, làm cho dòng điện ở một điện áp cho trước lớn hơn.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Lựa chọn phát biểu giải thích đúng bản chất vật lý của sự dịch chuyển đường đặc tuyến $I-V$ sang trái khi nhiệt độ tăng.

**Hướng đi:**

- **Cơ chế kích thích nhiệt hạt tải điện**: Phân tích sự phụ thuộc của mật độ hạt tải tự do và dòng bão hòa nghịch $I_S$ vào nhiệt độ tuyệt đối $T$.
- **Đánh giá các phương án**: Loại trừ các nhận định sai lệch về vùng cấm, tính chất kim loại, và sự dịch chuyển của ion tạp chất cố định.

**Phân tích bản chất vật lý:**

Cường độ dòng điện qua chuyển tiếp p-n tuân theo phương trình:

$$
I \approx I_S \mathrm{e}^{eV / kT}
$$

Dòng điện bão hòa nghịch $I_S$ phụ thuộc chủ yếu vào mật độ hạt tải điện thiểu số được sinh ra do kích thích nhiệt, tỉ lệ thuận với bình phương nồng độ hạt tải nội tại $n_i^2$:

$$
I_S \propto n_i^2 \propto T^3 \mathrm{e}^{-E_g / kT}
$$

- Khi nhiệt độ tăng lên, năng lượng dao động nhiệt của mạng tinh thể tăng mạnh, cung cấp đủ năng lượng cho **nhiều electron hơn ở dải hóa trị vượt qua vùng cấm để nhảy lên dải dẫn**, tạo ra các electron dẫn và lỗ trống tự do.
- Sự gia tăng đột biến của nồng độ hạt tải dẫn tới việc dòng bão hòa nghịch $I_S$ tăng theo hàm mũ đối với nhiệt độ.
- Mặc dù số hạng mẫu số $kT$ trong số mũ $\frac{eV}{kT}$ làm giảm độ dốc tương đối, sự tăng vọt áp đảo của $I_S$ khiến cho ở cùng một điện áp phân cực thuận $V$, cường độ dòng điện chạy qua diode ở nhiệt độ cao lớn hơn rất nhiều so với ở nhiệt độ thấp. Ngược lại, để duy trì cùng một dòng điện, điện áp rào thế cần đặt vào sẽ giảm đi.

**Phân tích các phương án:**
- **(a) Sai**: Khi nhiệt độ tăng, độ rộng vùng cấm $E_g$ thực tế bị thu hẹp lại một lượng nhỏ do giãn nở nhiệt mạng tinh thể (hiệu ứng Varshni), chứ không rộng hơn.
- **(b) Đúng**: Nhiệt độ cao kích thích nhiều electron hơn vượt qua vùng cấm lên dải dẫn, gia tăng mật độ hạt tải và làm tăng dòng điện tại một điện áp cho trước.
- **(c) Sai**: Ở nhiệt độ vận hành thông thường ($150^\circ\mathrm{C} \approx 423\,\mathrm{K}$), năng lượng nhiệt $kT \approx 0{,}036\,\mathrm{eV}$ vẫn nhỏ hơn rất nhiều so với độ rộng vùng cấm của silic ($E_g \approx 1{,}1\,\mathrm{eV}$), do đó chỉ một phân số rất nhỏ electron kích thích lên dải dẫn. Tinh thể không bao giờ chuyển hoàn toàn thành kim loại tuân theo định luật Ohm.
- **(d) Sai**: Các nguyên tử tạp chất acceptor và donor là các ion tạp chất cố định liên kết chặt chẽ trong mạng tinh thể silic, hoàn toàn không thể tự do di chuyển ở nhiệt độ này.

**Đáp án đúng:** **(b)**.

</details>

### 42.58

Nếu điện áp thay vì dòng điện được giữ không đổi, điều gì sẽ xảy ra đối với cường độ dòng điện khi nhiệt độ tăng từ $25^\circ\mathrm{C}$ lên $150^\circ\mathrm{C}$?
(a) Ban đầu dòng điện tăng, sau đó nó giảm.
(b) Dòng điện tăng.
(c) Dòng điện giảm, cuối cùng tiến dần về không.
(d) Dòng điện không thay đổi trừ khi điện áp cũng thay đổi.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dự đoán hành vi của cường độ dòng điện $I$ khi giữ nguyên điện áp thuận $V = \text{const}$ và tăng nhiệt độ từ $25^\circ\mathrm{C}$ lên $150^\circ\mathrm{C}$.

**Hướng đi:**

- **Quan sát hình học trên đồ thị $I-V$**: Xét một đường thẳng đứng tại vị trí điện áp $V$ cố định (ví dụ $V = 0{,}60\,\mathrm{V}$ hoặc $0{,}70\,\mathrm{V}$) và theo dõi sự thay đổi tung độ dòng điện khi chuyển từ đường $25^\circ\mathrm{C}$ sang đường $150^\circ\mathrm{C}$.
- **Hệ quả vật lý**: Hiện tượng tự kích nhiệt (thermal runaway) trong linh kiện bán dẫn khi giữ áp không đổi.

Xét đồ thị thực nghiệm tại một giá trị điện áp phân cực thuận cố định:
- Chẳng hạn, chọn điện áp cố định $V = 0{,}60\,\mathrm{V}$:
  - Ở $T = 25^\circ\mathrm{C}$, tung độ dòng điện tương ứng trên đường cong màu xanh rất nhỏ, chỉ khoảng $I \approx 0{,}006\,\mathrm{A} = 6\,\mathrm{mA}$.
  - Ở $T = 150^\circ\mathrm{C}$, tung độ dòng điện tương ứng trên đường cong màu đỏ vọt lên tới $I \approx 0{,}15\,\mathrm{A} = 150\,\mathrm{mA}$.
- Tại bất kỳ giá trị điện áp nào trong vùng làm việc, đường cong đặc tuyến ở $150^\circ\mathrm{C}$ luôn nằm phía trên và dịch hẳn sang trái so với đường cong ở $25^\circ\mathrm{C}$.

Do đó, khi giữ nguyên điện áp và tăng nhiệt độ, **cường độ dòng điện chạy qua diode luôn luôn tăng mạnh mẽ** (tăng đơn điệu theo nhiệt độ do dòng bão hòa $I_S(T)$ tăng theo hàm mũ).

**Đáp án đúng:** **(b)**.

</details>
