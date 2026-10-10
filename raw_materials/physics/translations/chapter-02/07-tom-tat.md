<!-- Chuyên đề: Chuyển động thẳng — Tóm tắt kiến thức cốt lõi -->

## Tóm tắt kiến thức cốt lõi Chương 2

Chương 2 đặt nền móng cho cơ học cổ điển thông qua việc mô tả chuyển động một chiều dọc theo một trục thẳng (động học một chiều). Toàn bộ chương xoay quanh ba đại lượng cơ bản: **Vị trí** $x(t)$, **vận tốc** $v_x(t)$, và **gia tốc** $a_x(t)$, được liên kết chặt chẽ với nhau thông qua phép tính vi tích phân và các phương trình động học.

---

### 1. Vận tốc trung bình và Vận tốc tức thời

- **Vận tốc trung bình** trên khoảng thời gian $\Delta t = t_2 - t_1$ là đại lượng vector đại số, đo bằng tỉ số giữa độ dời $\Delta x = x_2 - x_1$ và thời gian thực hiện:
  $$v_{\mathrm{tb}-x} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1}.\qquad\text{(2.2)}$$
  Về hình học, $v_{\mathrm{tb}-x}$ chính là **hệ số góc (độ dốc) của cát tuyến** nối hai điểm $(t_1, x_1)$ và $(t_2, x_2)$ trên đồ thị vị trí — thời gian $x(t)$.

- **Vận tốc tức thời** tại thời điểm $t$ là vận tốc tại một thời điểm xác định, được định nghĩa là đạo hàm bậc nhất của hàm vị trí theo thời gian:
  $$v_x = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}.\qquad\text{(2.3)}$$
  Về hình học, $v_x$ là **hệ số góc của tiếp tuyến** với đường cong $x(t)$ tại thời điểm $t$.

- **Tốc độ tức thời** là độ lớn vô hướng của vận tốc: $v = |v_x| \ge 0$. Tốc độ không bao giờ âm, trong khi vận tốc có dấu để chỉ hướng chuyển động.

![Sơ đồ tóm tắt vận tốc: Cát tuyến cho vận tốc trung bình và Tiếp tuyến cho vận tốc tức thời trên đồ thị x-t](img/young-02/tom-tat-van-toc.png)

**Hình 2.S1:** Đồ thị tọa độ theo thời gian $x(t)$. Độ dốc của đường cát tuyến nối $(t_1, x_1)$ và $(t_2, x_2)$ biểu diễn vận tốc trung bình $v_{\mathrm{tb}-x}$. Độ dốc của tiếp tuyến tại từng điểm biểu diễn vận tốc tức thời $v_x$.

---

### 2. Gia tốc trung bình và Gia tốc tức thời

- **Gia tốc trung bình** là tốc độ biến thiên của vận tốc trong khoảng thời gian $\Delta t$:
  $$a_{\mathrm{tb}-x} = \frac{\Delta v_x}{\Delta t} = \frac{v_{2x} - v_{1x}}{t_2 - t_1}.\qquad\text{(2.4)}$$
  Biểu diễn hình học: Hệ số góc của cát tuyến nối $(t_1, v_{1x})$ và $(t_2, v_{2x})$ trên đồ thị vận tốc — thời gian $v_x(t)$.

- **Gia tốc tức thời** là đạo hàm bậc nhất của vận tốc theo thời gian, đồng thời là đạo hàm bậc hai của tọa độ theo thời gian:
  $$a_x = \lim_{\Delta t \to 0} \frac{\Delta v_x}{\Delta t} = \frac{dv_x}{dt} = \frac{d^2x}{dt^2}.\qquad\text{(2.5)}$$
  Biểu diễn hình học: Hệ số góc của tiếp tuyến trên đồ thị $v_x(t)$, đồng thời quyết định độ cong (bề lõm) của đồ thị $x(t)$.

- **Quy tắc nhận diện nhanh tính chất chuyển động:**
  - Nếu $v_x$ và $a_x$ **cùng dấu** ($v_x \cdot a_x > 0$): Vật chuyển động **nhanh dần** (tốc độ $|v_x|$ tăng).
  - Nếu $v_x$ và $a_x$ **trái dấu** ($v_x \cdot a_x < 0$): Vật chuyển động **chậm dần** (tốc độ $|v_x|$ giảm).

![Sơ đồ tóm tắt gia tốc: Độ dốc tiếp tuyến của đồ thị v-t là gia tốc tức thời](img/young-02/tom-tat-gia-toc.png)

**Hình 2.S2:** Đồ thị vận tốc theo thời gian $v_x(t)$. Cát tuyến nối hai thời điểm cho gia tốc trung bình $a_{\mathrm{tb}-x}$, trong khi tiếp tuyến tại mỗi thời điểm cho gia tốc tức thời $a_x$.

---

### 3. Chuyển động biến đổi đều (Gia tốc không đổi: $a_x = \text{const}$)

Khi gia tốc không đổi, ta có hệ bốn phương trình động học kinh điển kết nối 5 đại lượng $(x - x_0, v_{0x}, v_x, a_x, t)$:

$$v_x = v_{0x} + a_x t,\qquad\text{(2.8)}$$

$$x = x_0 + v_{0x}t + \frac{1}{2}a_x t^2,\qquad\text{(2.12)}$$

$$v_x^2 = v_{0x}^2 + 2a_x(x - x_0),\qquad\text{(2.13)}$$

$$x - x_0 = \frac{1}{2}(v_{0x} + v_x)t.\qquad\text{(2.14)}$$

*(Lưu ý: Bộ phương trình này CHỈ có giá trị khi và chỉ khi gia tốc là một hằng số).*

![Sơ đồ tóm tắt chuyển động biến đổi đều: Vector gia tốc không đổi và khoảng cách tăng theo cấp số](img/young-02/tom-tat-gia-toc-khong-doi.png)

**Hình 2.S3:** Chuyển động thẳng biến đổi đều với gia tốc cố định $\vec a$. Khoảng cách giữa các vị trí sau những khoảng thời gian bằng nhau liên tục biến đổi theo quy luật bậc hai của thời gian.

---

### 4. Chuyển động rơi tự do

- Rơi tự do là chuyển động của một vật chỉ chịu tác dụng duy nhất của trọng lực (bỏ qua mọi lực cản của không khí).
- Mọi vật rơi tự do tại cùng một vị trí đều có cùng một gia tốc trọng trường hướng thẳng đứng xuống dưới với độ lớn:
  $$g \approx 9.80\,\mathrm{m/s^2}.$$
- Khi chọn trục $Oy$ hướng thẳng đứng lên trên, thành phần gia tốc là $a_y = -g = -9.80\,\mathrm{m/s^2}$.
- Tại đỉnh quỹ đạo của một vật được ném lên cao, vận tốc tức thời triệt tiêu ($v_y = 0$), nhưng gia tốc vẫn giữ nguyên $a_y = -g$.
- Chuyển động rơi tự do có tính đối xứng hoàn hảo về thời gian và độ lớn vận tốc khi đi lên và rơi xuống qua cùng một độ cao.

![Sơ đồ tóm tắt rơi tự do: Vector gia tốc luôn hướng xuống trong cả hai giai đoạn lên và xuống](img/young-02/tom-tat-roi-tu-do.png)

**Hình 2.S4:** Khi ném thẳng đứng lên cao, vector gia tốc trọng trường $\vec g$ luôn hướng thẳng đứng chúc xuống dưới tại mọi điểm trên quỹ đạo: Cả khi bay lên ($v_y > 0$), tại đỉnh cao nhất ($v_y = 0$), và khi rơi xuống ($v_y < 0$).

---

### 5. Chuyển động với gia tốc biến thiên — Phương pháp vi tích phân

Khi gia tốc phụ thuộc vào thời gian $a_x = a_x(t)$, ta tìm lại vận tốc và vị trí thông qua hai lần lấy tích phân xác định:

$$v_x(t) = v_{0x} + \int_0^t a_x(t')\, dt',\qquad\text{(2.17)}$$

$$x(t) = x_0 + \int_0^t v_x(t')\, dt'.\qquad\text{(2.18)}$$

Về mặt hình học:
- **Độ biến thiên vận tốc** $\Delta v_x$ bằng **diện tích hình thang cong** dưới đồ thị gia tốc — thời gian $a_x(t)$.
- **Độ dời** $\Delta x$ bằng **diện tích hình thang cong** dưới đồ thị vận tốc — thời gian $v_x(t)$.

![Sơ đồ tóm tắt tích phân: Diện tích dưới đồ thị gia tốc là độ biến thiên vận tốc](img/young-02/tom-tat-tich-phan.png)

**Hình 2.S5:** Ý nghĩa hình học của tích phân: Diện tích dải vi phân dưới đường cong gia tốc $a_x(t)$ biểu thị độ biến thiên vận tốc $dv_x = a_x dt$, và tổng diện tích dưới đồ thị cho độ biến thiên vận tốc toàn phần.
