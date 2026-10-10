## 2.4. Chuyển động thẳng với gia tốc không đổi

Trường hợp chuyển động có gia tốc đơn giản và quan trọng nhất trong cơ học cổ điển là **chuyển động trên đường thẳng với gia tốc không đổi** ($a_x = \text{const}$), còn gọi là chuyển động thẳng biến đổi đều.

Khi gia tốc là hằng số, vận tốc của chất điểm biến thiên với tốc độ hoàn toàn đều đặn theo thời gian. Ta bắt gặp mô hình này ở khắp mọi nơi trong tự nhiên và kỹ thuật:
- Một vật thể rơi tự do trong trường trọng lực gần mặt đất khi lực cản không khí không đáng kể;
- Một chiếc ô tô đạp phanh gấp với lực hãm ma sát trượt không đổi;
- Một máy bay chiến đấu phản lực được máy phóng hơi nước đẩy vọt đi trên boong tàu sân bay.

![Hình 2.15: Vị trí, vận tốc và gia tốc của chất điểm tại các thời điểm cách đều nhau](img/young-02/hinh-2-15.png)

Trên Hình 2.15, sau những khoảng thời gian bằng nhau $\Delta t$, vận tốc của chất điểm tăng thêm những lượng bằng nhau $\Delta v_x = a_x\Delta t$. Tuy nhiên, quãng đường đi được trong mỗi khoảng thời gian lại ngày càng dài hơn, vì vận tốc tức thời của vật ngày càng lớn!

---

### Hệ bốn phương trình động học cốt lõi

Vì gia tốc $a_x$ là hằng số không đổi trên toàn bộ hành trình, giá trị gia tốc trung bình trên bất kỳ khoảng thời gian nào cũng bằng chính gia tốc tức thời $a_x$:

$$a_x = \frac{v_{2x} - v_{1x}}{t_2 - t_1}.\tag{2.7}$$

Chọn thời điểm ban đầu $t_1 = 0$ với vận tốc ban đầu $v_{1x} = v_{0x}$, và thời điểm khảo sát lúc sau $t_2 = t$ với vận tốc tương ứng $v_{2x} = v_x$:

$$v_x = v_{0x} + a_xt.\tag{2.8}$$

Phương trình (2.8) biểu thị quy luật tuyến tính: Vận tốc lúc sau bằng vận tốc ban đầu cộng với lượng biến thiên tích lũy $a_xt$. Trên đồ thị vận tốc – thời gian ($v_x-t$), phương trình này là một **đường thẳng** có hệ số góc bằng $a_x$ và tung độ gốc bằng $v_{0x}$ (Hình 2.17).

![Hình 2.16: Đồ thị gia tốc theo thời gian — diện tích hình chữ nhật là độ biến thiên vận tốc](img/young-02/hinh-2-16.png)

![Hình 2.17: Đồ thị vận tốc theo thời gian — diện tích hình thang là độ dời](img/young-02/hinh-2-17.png)

### Phương trình tọa độ vị trí theo thời gian

Để tìm vị trí $x(t)$, ta xuất phát từ định nghĩa vận tốc trung bình:

$$v_{\mathrm{av}-x} = \frac{x - x_0}{t}.\tag{2.9}$$

Chỉ riêng trong trường hợp đặc biệt khi gia tốc không đổi (vận tốc biến thiên hoàn toàn tuyến tính theo thời gian), vận tốc trung bình trong khoảng từ $0$ đến $t$ bằng đúng **trung bình cộng của vận tốc đầu và vận tốc cuối**:

$$v_{\mathrm{av}-x} = \frac{v_{0x} + v_x}{2}.\tag{2.10}$$

Thay biểu thức $v_x = v_{0x} + a_xt$ từ (2.8) vào (2.10):

$$v_{\mathrm{av}-x} = \frac{v_{0x} + (v_{0x} + a_xt)}{2} = v_{0x} + \frac{1}{2}a_xt.\tag{2.11}$$

Đồng nhất (2.9) với (2.11), ta rút ra phương trình tọa độ vị trí:

$$x = x_0 + v_{0x}t + \frac{1}{2}a_xt^2.\tag{2.12}$$

Phương trình (2.12) là một hàm số bậc hai của thời gian $t$. Trên đồ thị vị trí – thời gian ($x-t$), đường biểu diễn là một **nhánh parabol** (Hình 2.18 và Hình 2.19):
- Nếu $a_x > 0$: Parabol có bề lõm quay lên trên.
- Nếu $a_x < 0$: Parabol có bề lõm quay xuống dưới.
- Nếu $a_x = 0$: Số hạng bậc hai triệt tiêu, đồ thị thoái hóa thành đường thẳng $x = x_0 + v_{0x}t$ (chuyển động thẳng đều).

![Hình 2.18: Đồ thị tọa độ x theo thời gian là đường parabol](img/young-02/hinh-2-18.png)

![Hình 2.19: So sánh chuyển động thẳng đều và chuyển động có gia tốc không đổi](img/young-02/hinh-2-19.png)

*Ý nghĩa hình học của độ dời qua tích phân diện tích:*
Quan sát Hình 2.17, độ dời $\Delta x = x - x_0$ chính bằng diện tích hình thang dưới đường đồ thị $v_x-t$. Ta có thể tách hình thang thành hai phần:
- Diện tích hình chữ nhật bên dưới: $v_{0x}t$ (quãng đường đi được nếu giữ nguyên vận tốc ban đầu).
- Diện tích tam giác vuông bên trên: $\frac{1}{2}(t)(a_xt) = \frac{1}{2}a_xt^2$ (quãng đường dôi ra do gia tốc làm tăng vận tốc).
Tổng diện tích chính là $x - x_0 = v_{0x}t + \frac{1}{2}a_xt^2$, hoàn toàn trùng khớp với (2.12)!

---

### Phương trình độc lập với thời gian (Hệ thức Torricelli)

Trong vô số bài toán thực tế, đề bài cho biết quãng đường và vận tốc nhưng không hề đề cập đến thời gian $t$. Để thiết lập mối liên hệ trực tiếp không phụ thuộc thời gian, ta rút $t = \frac{v_x - v_{0x}}{a_x}$ từ (2.8) rồi thế vào (2.12):

$$x - x_0 = v_{0x}\left(\frac{v_x - v_{0x}}{a_x}\right) + \frac{1}{2}a_x\left(\frac{v_x - v_{0x}}{a_x}\right)^2.$$

Nhân cả hai vế với $2a_x$ và khai triển hằng đẳng thức:

$$2a_x(x - x_0) = 2v_{0x}v_x - 2v_{0x}^2 + v_x^2 - 2v_{0x}v_x + v_{0x}^2 = v_x^2 - v_{0x}^2.$$

Ta thu được hệ thức độc lập với thời gian kinh điển:

$$v_x^2 = v_{0x}^2 + 2a_x(x - x_0).\tag{2.13}$$

Một hệ thức bổ trợ hữu ích khác nhận được khi ghép (2.9) và (2.10):

$$x - x_0 = \left(\frac{v_{0x} + v_x}{2}\right)t.\tag{2.14}$$

### Bảng 2.5 — Bộ 4 phương trình chuyển động thẳng biến đổi đều

| Phương trình | Số hiệu | Đại lượng vắng mặt (không cần biết) |
| :--- | :--- | :--- |
| $v_x = v_{0x} + a_xt$ | (2.8) | Vắng mặt tọa độ vị trí ($x - x_0$). |
| $x = x_0 + v_{0x}t + \frac{1}{2}a_xt^2$ | (2.12) | Vắng mặt vận tốc lúc sau ($v_x$). |
| $v_x^2 = v_{0x}^2 + 2a_x(x - x_0)$ | (2.13) | Vắng mặt thời gian ($t$). |
| $x - x_0 = \frac{1}{2}(v_{0x} + v_x)t$ | (2.14) | Vắng mặt gia tốc ($a_x$). |

::: tip Bí quyết thực chiến chọn phương trình trong chớp mắt
Mỗi phương trình trong Bảng 2.5 chỉ chứa đúng 4 trong số 5 đại lượng động học cốt lõi: $\Delta x, v_{0x}, v_x, a_x, t$.
Khi đọc đề bài, hãy tự hỏi: **Đại lượng nào đề bài KHÔNG CHO mà cũng KHÔNG YÊU CẦU TÌM?**
- Không cần $\Delta x \implies$ chọn ngay (2.8).
- Không cần $v_x \implies$ chọn ngay (2.12).
- Không cần $t \implies$ chọn ngay (2.13) (không bao giờ phải mất công giải phương trình bậc hai qua ẩn $t$!).
- Không cần $a_x \implies$ chọn ngay (2.14).
:::

---

### Ứng dụng thực tiễn — Khoảng cách phanh ô tô và Thử nghiệm gia tốc cực hạn

![Hình ứng dụng: Đại tá John Stapp trên xe trượt tên lửa chịu gia tốc cực lớn](img/young-02/ung-dung-gia-toc-lon.png)

1. **Vật lý an toàn giao thông — Khoảng cách phanh tỷ lệ với bình phương vận tốc:**
   Khi một chiếc xe đang chạy với vận tốc ban đầu $v_0$ và tài xế đạp phanh khẩn cấp tạo gia tốc hãm $a_x = -a$ (không đổi), xe dừng lại hoàn toàn khi $v_x = 0$. Áp dụng hệ thức (2.13):
   $$0^2 = v_0^2 + 2(-a)d \implies d = \frac{v_0^2}{2a}.$$
   Khoảng cách dừng xe $d$ **tỷ lệ thuận với bình phương vận tốc đầu ($v_0^2$)**!
   - Nếu bạn chạy xe ở tốc độ $50\,\mathrm{km/h}$, khoảng cách phanh mất khoảng $14\,\mathrm m$.
   - Nếu bạn tăng tốc lên gấp đôi ($100\,\mathrm{km/h}$), khoảng cách phanh không phải tăng gấp đôi mà tăng vọt lên **gấp bốn lần ($56\,\mathrm m$)**!
   Đây là minh chứng vật lý đanh thép giải thích tại sao phóng nhanh vượt ẩu lại làm giảm thảm khốc khả năng xử lý va chạm.

2. **Giới hạn chịu đựng gia tốc của con người (Đại tá John Stapp):**
   Trong những năm 1950, bác sĩ Không quân Hoa Kỳ John Stapp đã tự mình ngồi lên chiếc xe trượt đẩy bằng động cơ tên lửa để kiểm tra giới hạn sinh lý của phi công. Chiếc xe trượt tăng tốc lên $188\,\mathrm{m/s}$ ($678\,\mathrm{km/h}$) rồi bị máng nước hãm phanh dừng lại chỉ trong $1.4\,\mathrm s$, tạo ra gia tốc hãm kỷ lục lên tới $440\,\mathrm{m/s^2}$ (gấp $45$ lần gia tốc trọng trường $g$). Thí nghiệm lịch sử này chứng minh con người có thể sống sót sau các vụ va chạm cực mạnh nếu ghế ngồi và đai an toàn được thiết kế đúng chuẩn cơ học.

---

### Ví dụ 2.4 — Tính toán với gia tốc không đổi

::: exercise Bài toán
Một người lái mô tô đang chuyển động thẳng về phía đông. Vừa qua khỏi biển báo giới hạn tốc độ của thị trấn, người đó bắt đầu tăng ga với gia tốc cố định $4.0\,\mathrm{m/s^2}$ (Hình 2.20). Đúng tại thời điểm $t = 0$, chiếc xe cách biển báo ranh giới $5.0\,\mathrm m$ về phía đông và đang có vận tốc $15.0\,\mathrm{m/s}$.

**(a)** Xác định tọa độ vị trí và vận tốc của người lái xe tại thời điểm $t = 2.0\,\mathrm s$.  
**(b)** Khi tốc độ của xe đạt $25.0\,\mathrm{m/s}$, người đó đang ở vị trí cách biển báo ranh giới bao xa?
:::

![Hình 2.20: Chuyển động tăng tốc của người lái mô tô qua biển báo ranh giới](img/young-02/hinh-2-20.png)

::: solution Hướng dẫn giải
**Nhận diện và thiết lập:**
Chọn trục $Ox$ hướng thẳng về phía đông, gốc $O$ đặt tại vị trí biển báo ranh giới thị trấn. Chiều dương hướng về phía đông.
Dữ kiện đã biết:
- Vị trí ban đầu: $x_0 = +5.0\,\mathrm m$;
- Vận tốc ban đầu: $v_{0x} = +15.0\,\mathrm{m/s}$;
- Gia tốc: $a_x = +4.0\,\mathrm{m/s^2}$ (hằng số không đổi).

**Thực thi câu (a):**
Áp dụng trực tiếp phương trình vị trí (2.12) và phương trình vận tốc (2.8) tại $t = 2.0\,\mathrm s$:
$$x(2.0\,\mathrm s) = x_0 + v_{0x}t + \frac{1}{2}a_xt^2 = 5.0 + (15.0)(2.0) + \frac{1}{2}(4.0)(2.0)^2 = 5.0 + 30.0 + 8.0 = 43.0\,\mathrm m.$$
$$v_x(2.0\,\mathrm s) = v_{0x} + a_xt = 15.0 + (4.0)(2.0) = 15.0 + 8.0 = 23.0\,\mathrm{m/s}.$$

**Thực thi câu (b):**
Ở câu này, ta cần tìm vị trí $x$ khi biết $v_x = 25.0\,\mathrm{m/s}$, không cần biết thời gian $t$. Áp dụng ngay hệ thức độc lập thời gian (2.13):
$$v_x^2 = v_{0x}^2 + 2a_x(x - x_0) \implies x = x_0 + \frac{v_x^2 - v_{0x}^2}{2a_x}.$$

Thay số:
$$x = 5.0\,\mathrm m + \frac{(25.0\,\mathrm{m/s})^2 - (15.0\,\mathrm{m/s})^2}{2(4.0\,\mathrm{m/s^2})} = 5.0 + \frac{625 - 225}{8.0} = 5.0 + \frac{400}{8.0} = 5.0 + 50.0 = 55.0\,\mathrm m.$$

**Đánh giá:** 
Kiểm tra lại: Thời gian để tăng tốc từ $15\,\mathrm{m/s}$ lên $25\,\mathrm{m/s}$ là $t = \frac{v_x - v_{0x}}{a_x} = \frac{25 - 15}{4.0} = 2.5\,\mathrm s$. Thế $t = 2.5\,\mathrm s$ vào (2.12): $x = 5.0 + 15(2.5) + 0.5(4.0)(2.5)^2 = 5.0 + 37.5 + 12.5 = 55.0\,\mathrm m$. Kết quả hoàn toàn trùng khớp, nhưng hệ thức (2.13) giúp ta giải quyết bài toán chỉ trong một dòng duy nhất!
:::

---

### Ví dụ 2.5 — Bài toán đuổi bắt giữa hai xe có gia tốc khác nhau

::: exercise Bài toán
Một chiếc ô tô con chạy quá tốc độ với vận tốc không đổi $15.0\,\mathrm{m/s}$ ($54\,\mathrm{km/h}$) qua một khu vực trường học có biển giới hạn tốc độ $10.0\,\mathrm{m/s}$ ($36\,\mathrm{km/h}$). Đúng lúc ô tô lướt qua biển báo, một cảnh sát giao thông đi mô tô đang dừng tại đó bắt đầu nổ máy đuổi theo với gia tốc không đổi $3.0\,\mathrm{m/s^2}$ (Hình 2.21a).

**(a)** Sau bao lâu kể từ lúc xuất phát thì cảnh sát đuổi kịp chiếc ô tô?  
**(b)** Tại thời điểm đuổi kịp, tốc độ của xe cảnh sát là bao nhiêu?  
**(c)** Khi đó, mỗi xe đã đi được quãng đường bao xa tính từ biển báo?
:::

![Hình 2.21: Hai xe chuyển động đuổi bắt nhau và giao điểm của hai đồ thị vị trí](img/young-02/hinh-2-21.png)

::: solution Hướng dẫn giải
**Nhận diện và thiết lập:**
Chọn gốc tọa độ $O$ tại biển báo ranh giới trường học, chiều dương trục $Ox$ hướng theo chiều chuyển động của hai xe. Thời điểm ban đầu $t = 0$ là lúc ô tô chạy ngang qua xe cảnh sát.
Cả hai xe đều xuất phát từ $x_0 = 0$:
- Ô tô chuyển động thẳng đều: $a_{Ox} = 0$, vận tốc $v_{O0x} = 15.0\,\mathrm{m/s}$ $\implies$ Phương trình chuyển động: $x_O(t) = v_{O0x}t = 15.0t$.
- Mô tô cảnh sát chuyển động nhanh dần đều từ trạng thái nghỉ: $v_{P0x} = 0$, gia tốc $a_{Px} = 3.0\,\mathrm{m/s^2}$ $\implies$ Phương trình chuyển động: $x_P(t) = \frac{1}{2}a_{Px}t^2 = 1.5t^2$.

**Thực thi câu (a):**
Hai xe gặp nhau (cảnh sát đuổi kịp ô tô) khi và chỉ khi **chúng có cùng tọa độ vị trí**:
$$x_P(t) = x_O(t) \iff \frac{1}{2}a_{Px}t^2 = v_{O0x}t \iff t\left(\frac{1}{2}a_{Px}t - v_{O0x}\right) = 0.$$

Phương trình cho hai nghiệm:
1. $t = 0$: Thời điểm ban đầu khi chiếc ô tô vượt qua xe cảnh sát tại vạch xuất phát.
2. Thời điểm cảnh sát đuổi kịp:
   $$t = \frac{2v_{O0x}}{a_{Px}} = \frac{2(15.0\,\mathrm{m/s})}{3.0\,\mathrm{m/s^2}} = 10.0\,\mathrm s.$$

**Thực thi câu (b):**
Vận tốc của xe cảnh sát tại thời điểm $t = 10.0\,\mathrm s$:
$$v_{Px} = v_{P0x} + a_{Px}t = 0 + (3.0\,\mathrm{m/s^2})(10.0\,\mathrm s) = 30.0\,\mathrm{m/s}\quad (108\,\mathrm{km/h}).$$

**Thực thi câu (c):**
Quãng đường mỗi xe đi được:
$$x_O = (15.0\,\mathrm{m/s})(10.0\,\mathrm s) = 150\,\mathrm m,$$
$$x_P = \frac{1}{2}(3.0\,\mathrm{m/s^2})(10.0\,\mathrm s)^2 = 1.5 \times 100 = 150\,\mathrm m.$$

**Đánh giá bản chất sâu sắc:**
Quan sát thấy: Tại thời điểm gặp nhau, vận tốc của cảnh sát ($30.0\,\mathrm{m/s}$) **gấp đúng 2 lần** vận tốc của chiếc ô tô ($15.0\,\mathrm{m/s}$)!
Đây hoàn toàn không phải là sự trùng hợp ngẫu nhiên. Vì hai xe đi cùng một quãng đường trong cùng một khoảng thời gian, nên vận tốc trung bình của chúng phải bằng nhau:
- Vận tốc trung bình của ô tô chạy đều là $v_O$.
- Vận tốc trung bình của cảnh sát xuất phát từ nghỉ là $\frac{0 + v_P}{2} = \frac{v_P}{2}$.
Đồng nhất hai vận tốc trung bình: $\frac{v_P}{2} = v_O \implies v_P = 2v_O$. Quy luật này luôn đúng cho mọi giá trị gia tốc trong mô hình đuổi bắt từ trạng thái nghỉ!
:::

---

### Câu hỏi kiểm tra hiểu biết mục 2.4

::: exercise Câu hỏi kiểm tra
Trong bốn đồ thị vận tốc – thời gian ($v_x-t$) ở hình dưới đây, đồ thị nào mô tả chính xác nhất diễn biến chuyển động của người lái xe ô tô và viên cảnh sát trong Ví dụ 2.5?

![Hình câu hỏi: Các phương án đồ thị vận tốc theo thời gian](img/young-02/cau-hoi-2-4.png)
:::

::: solution Lời giải
Đáp án đúng là **(b)**.

*Phân tích bản chất:*
1. Chiếc ô tô chạy với vận tốc không đổi $15\,\mathrm{m/s}$, do đó đồ thị vận tốc của nó phải là một **đường thẳng nằm ngang**.
2. Mô tô cảnh sát tăng tốc với gia tốc không đổi $a_{Px} = 3.0\,\mathrm{m/s^2}$ từ trạng thái nghỉ ($v_0 = 0$), do đó đồ thị của nó là một **đường thẳng dốc lên xuất phát từ gốc tọa độ**.
3. Tại thời điểm $t = 10\,\mathrm s$ khi hai xe gặp nhau, diện tích hình thang dưới hai đồ thị bằng nhau (cùng bằng quãng đường $150\,\mathrm m$), và tung độ của cảnh sát ($30\,\mathrm{m/s}$) cao gấp đôi tung độ của ô tô ($15\,\mathrm{m/s}$). Đồ thị (b) thể hiện chính xác tuyệt đối các tính chất này.
:::
