## 2.1. Độ dời, thời gian và vận tốc trung bình

Để nghiên cứu chuyển động của một vật thể, bước đầu tiên và cơ bản nhất là thiết lập một **hệ tọa độ** gắn với một mốc quy chiếu xác định. 

Xét một chiếc xe đua tăng tốc trên một đường chạy thẳng tắp (Hình 2.1). Ta chọn trục tọa độ $Ox$ trùng với đường chạy, gốc $O$ đặt tại vạch xuất phát, và chiều dương $+x$ hướng theo chiều chuyển động về phía trước (sang phải). Vì kích thước của chiếc xe là rất nhỏ so với toàn bộ chiều dài đường đua, ta áp dụng mô hình **chất điểm** bằng cách chọn một điểm đại diện trên xe (chẳng hạn đầu xe) để biểu diễn vị trí của toàn bộ chiếc xe.

![Hình 2.1: Tọa độ vị trí của xe đua tại hai thời điểm khác nhau trên trục Ox](img/young-02/hinh-2-1.png)

Giả sử tại thời điểm $t_1 = 1.0\,\mathrm s$ sau khi xuất phát, đầu xe ở vị trí $P_1$ có tọa độ $x_1 = 19\,\mathrm m$. Đến thời điểm $t_2 = 4.0\,\mathrm s$, xe đã lao tới vị trí $P_2$ có tọa độ $x_2 = 277\,\mathrm m$.

Trong khoảng thời gian $\Delta t = t_2 - t_1 = 4.0\,\mathrm s - 1.0\,\mathrm s = 3.0\,\mathrm s$, tọa độ của xe đã biến thiên một lượng:

$$\Delta x = x_2 - x_1 = 277\,\mathrm m - 19\,\mathrm m = +258\,\mathrm m.\tag{2.1}$$

Đại lượng $\Delta x$ được gọi là **thành phần độ dời** (hay ngắn gọn là độ dời) của chất điểm dọc theo trục $x$. 

::: warning Bản chất của ký hiệu biến thiên $\Delta$ (Delta)
Ký hiệu $\Delta x$ không phải là tích của chữ cái $\Delta$ nhân với $x$. Trong toán học và vật lý, chữ cái Hy Lạp viết hoa $\Delta$ (delta) là một toán tử biểu thị **độ biến thiên**: Luôn lấy **giá trị lúc sau trừ đi giá trị lúc đầu**:
$$\Delta (\text{đại lượng}) = (\text{giá trị cuối}) - (\text{giá trị đầu}).$$
Tương tự, $\Delta t = t_2 - t_1$ là khoảng thời gian trôi qua giữa hai sự kiện (luôn là số dương).
:::

---

### Vận tốc trung bình (Average Velocity)

Để đo lường mức độ nhanh hay chậm của sự thay đổi vị trí, ta định nghĩa **thành phần vận tốc trung bình** dọc theo trục $x$ (ký hiệu $v_{\mathrm{tb}-x}$ hoặc $v_{\mathrm{av}-x}$) là tỷ số giữa độ dời và khoảng thời gian diễn ra độ dời đó:

$$v_{\mathrm{av}-x} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}.\tag{2.2}$$

Với chuyển động của chiếc xe đua ở trên:

$$v_{\mathrm{av}-x} = \frac{277\,\mathrm m - 19\,\mathrm m}{4.0\,\mathrm s - 1.0\,\mathrm s} = \frac{+258\,\mathrm m}{3.0\,\mathrm s} = +86\,\mathrm{m/s}.$$

Dấu cộng ($+$) của vận tốc trung bình cho biết tọa độ $x$ đang tăng dần theo thời gian, nghĩa là vật đang dịch chuyển theo **chiều dương của trục tọa độ** (sang phía bên phải).

Ngược lại, nếu một chiếc xe cứu hộ chạy lùi hoặc di chuyển ngược chiều từ vị trí $x_1 = 277\,\mathrm m$ ($t_1 = 16.0\,\mathrm s$) về lại vị trí $x_2 = 19\,\mathrm m$ ($t_2 = 25.0\,\mathrm s$) như ở Hình 2.2:

$$\Delta x = x_2 - x_1 = 19\,\mathrm m - 277\,\mathrm m = -258\,\mathrm m,$$
$$\Delta t = 25.0\,\mathrm s - 16.0\,\mathrm s = 9.0\,\mathrm s,$$
$$v_{\mathrm{av}-x} = \frac{\Delta x}{\Delta t} = \frac{-258\,\mathrm m}{9.0\,\mathrm s} \approx -29\,\mathrm{m/s}.$$

Dấu trừ ($-$) chỉ ra rằng vật đang chuyển động ngược chiều dương, tức theo **chiều âm của trục tọa độ**.

![Hình 2.2: Xe chuyển động theo chiều âm của trục tọa độ cho độ dời và vận tốc âm](img/young-02/hinh-2-2.png)

### Bảng 2.1 — Mối liên hệ giữa dấu của vận tốc và hướng chuyển động

| Chiều chuyển động thực tế | Độ biến thiên tọa độ $\Delta x$ | Dấu của vận tốc $v_x$ |
| :--- | :--- | :--- |
| Chuyển động theo chiều dương ($+x$) | Tăng dần ($\Delta x > 0$) | Dương ($v_x > 0$) |
| Chuyển động theo chiều âm ($-x$) | Giảm dần ($\Delta x < 0$) | Âm ($v_x < 0$) |
| Đứng yên tại một vị trí | Không đổi ($\Delta x = 0$) | Bằng 0 ($v_x = 0$) |

::: warning Dấu của vận tốc hoàn toàn phụ thuộc vào việc bạn chọn chiều dương hệ trục
Dấu dương hay âm của vận tốc không phải là bản chất tự thân bất biến của chiếc xe, mà phụ thuộc hoàn toàn vào hệ quy chiếu do người quan sát thiết lập. Nếu bạn chọn chiều dương $+x$ hướng sang bên trái, thì chiếc xe đua chạy sang phải sẽ mang vận tốc âm, còn chiếc xe cứu hộ chạy sang trái lại mang vận tốc dương! Một khi đã chọn hệ trục, bạn bắt buộc phải tuân thủ nhất quán quy ước dấu đó xuyên suốt bài toán.
:::

---

### Ý nghĩa hình học: Đồ thị tọa độ – thời gian ($x-t$)

Một phương thức trực quan và mạnh mẽ để nắm bắt chuyển động là biểu diễn vị trí $x$ dưới dạng hàm số của thời gian $t$ trên mặt phẳng tọa độ (đồ thị $x-t$, Hình 2.3).

Cần phân biệt rõ: **Đường cong trên đồ thị $x-t$ không phải là quỹ đạo hình học của chiếc xe trong không gian!** Xe vẫn đang chạy trên một đường thẳng tắp; đường cong trên đồ thị chỉ mô tả quy luật biến thiên của tọa độ vị trí theo thời gian.

![Hình 2.3: Ý nghĩa hình học của vận tốc trung bình — độ dốc của cát tuyến trên đồ thị x-t](img/young-02/hinh-2-3.png)

Xét hai điểm $p_1(t_1, x_1)$ và $p_2(t_2, x_2)$ trên đường cong:
- Đoạn thẳng nối $p_1$ và $p_2$ là một **cát tuyến** của đường cong đồ thị.
- Độ dốc (*slope*) của cát tuyến này bằng độ tăng theo trục đứng chia cho độ tăng theo trục ngang:
  $$\text{Độ dốc của cát tuyến } p_1p_2 = \frac{\Delta x}{\Delta t} = v_{\mathrm{av}-x}.$$

Về mặt toán học: **Vận tốc trung bình trong khoảng thời gian từ $t_1$ đến $t_2$ chính là hệ số góc (độ dốc) của đường cát tuyến nối hai điểm tương ứng trên đồ thị tọa độ – thời gian ($x-t$)**. Đơn vị của độ dốc là mét chia giây ($\mathrm{m/s}$), hoàn toàn chuẩn xác với đơn vị của vận tốc.

Vận tốc trung bình chỉ phụ thuộc vào trạng thái đầu và trạng thái cuối, hoàn toàn không quan tâm đến diễn biến chi tiết ở giữa hành trình. Một chiếc mô tô có thể phóng vượt qua xe đua rồi lại phanh gấp để cùng đến $P_2$ tại thời điểm $t_2$; cả hai xe khi đó đều có chung một vận tốc trung bình như nhau!

---

### Bảng 2.2 — Thang bậc độ lớn của vận tốc trong tự nhiên

| Chuyển động vật lý | Tốc độ điển hình ($\mathrm{m/s}$) | Ghi chú quy đổi |
| :--- | :--- | :--- |
| Ốc sên bò | $\sim 10^{-3}\,\mathrm{m/s}$ | $\sim 3.6\,\mathrm{m/h}$ |
| Người đi bộ thong thả | $1.4\,\mathrm{m/s}$ | $\approx 5.0\,\mathrm{km/h}$ |
| Vận động viên chạy nước rút $100\,\mathrm m$ | $10 - 12\,\mathrm{m/s}$ | Kỷ lục Usain Bolt $\approx 12.4\,\mathrm{m/s}$ ($44.7\,\mathrm{km/h}$) |
| Ô tô lưu thông trên cao tốc | $30\,\mathrm{m/s}$ | $108\,\mathrm{km/h}$ |
| Tốc độ âm thanh trong không khí ($20^\circ\mathrm C$) | $343\,\mathrm{m/s}$ | $\approx 1235\,\mathrm{km/h}$ (Mach 1) |
| Chuyển động nhiệt hỗn loạn của phân tử khí | $\approx 500\,\mathrm{m/s}$ | Cỡ vận tốc phân tử nitơ ở nhiệt độ phòng |
| Máy bay do thám siêu âm SR-71 Blackbird | $\approx 1000\,\mathrm{m/s}$ | Mach 3+ ($\approx 3600\,\mathrm{km/h}$) |
| Trạm Vũ trụ Quốc tế (ISS) bay quanh Trái Đất | $7700\,\mathrm{m/s}$ | Vận tốc vũ trụ cấp 1 ($\approx 27\,700\,\mathrm{km/h}$) |
| Tốc độ ánh sáng trong chân không ($c$) | $3.00 \times 10^8\,\mathrm{m/s}$ | Giới hạn tốc độ tối thượng của vũ trụ |

---

### Câu hỏi kiểm tra hiểu biết mục 2.1

::: exercise Câu hỏi kiểm tra
Năm chiếc xe A, B, C, D, E đều thực hiện hành trình chuyển động thẳng kéo dài đúng một giờ ($\Delta t = 1.0\,\mathrm h$). Chọn chiều dương $+x$ hướng về phía đông:
- **(i)** Xe A đi $50\,\mathrm{km}$ về phía đông.
- **(ii)** Xe B đi $50\,\mathrm{km}$ về phía tây.
- **(iii)** Xe C đi $60\,\mathrm{km}$ về phía đông rồi quay đầu đi $10\,\mathrm{km}$ về phía tây.
- **(iv)** Xe D đi $70\,\mathrm{km}$ về phía đông.
- **(v)** Xe E đi $20\,\mathrm{km}$ về phía tây rồi quay đầu đi $20\,\mathrm{km}$ về phía đông.

**(a)** Hãy sắp xếp vận tốc trung bình của các xe theo thứ tự từ giá trị dương lớn nhất đến giá trị âm lớn nhất.

**(b)** Những xe nào có cùng vận tốc trung bình?

**(c)** Xe nào có vận tốc trung bình bằng 0?
:::

::: solution Lời giải
Vì thời gian chuyển động của mọi xe đều bằng $\Delta t = 1.0\,\mathrm h$, vận tốc trung bình tỷ lệ thuận trực tiếp với độ dời $\Delta x$:
- Xe A: Đi theo hướng đông $\implies \Delta x_A = +50\,\mathrm{km} \implies v_{\mathrm{av}-x} = +50\,\mathrm{km/h}$.
- Xe B: Đi theo hướng tây $\implies \Delta x_B = -50\,\mathrm{km} \implies v_{\mathrm{av}-x} = -50\,\mathrm{km/h}$.
- Xe C: Đi $+60\,\mathrm{km}$ rồi $-10\,\mathrm{km} \implies \Delta x_C = 60 - 10 = +50\,\mathrm{km} \implies v_{\mathrm{av}-x} = +50\,\mathrm{km/h}$.
- Xe D: Đi theo hướng đông $\implies \Delta x_D = +70\,\mathrm{km} \implies v_{\mathrm{av}-x} = +70\,\mathrm{km/h}$.
- Xe E: Đi $-20\,\mathrm{km}$ rồi $+20\,\mathrm{km} \implies \Delta x_E = -20 + 20 = 0\,\mathrm{km} \implies v_{\mathrm{av}-x} = 0\,\mathrm{km/h}$.

**(a) Thứ tự sắp xếp đại số:**
$$v_D (+70\,\mathrm{km/h}) > v_A = v_C (+50\,\mathrm{km/h}) > v_E (0\,\mathrm{km/h}) > v_B (-50\,\mathrm{km/h}).$$

**(b) Xe A và xe C** có cùng vận tốc trung bình ($+50\,\mathrm{km/h}$) dù quãng đường xe C đi ($70\,\mathrm{km}$) dài hơn xe A ($50\,\mathrm{km}$).

**(c) Xe E** có vận tốc trung bình bằng 0 vì vị trí cuối trùng vị trí đầu (độ dời tổng cộng bằng 0), mặc dù chiếc xe đã tiêu tốn nhiên liệu để đi quãng đường tổng cộng $40\,\mathrm{km}$!
:::
