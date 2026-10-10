## 2.2. Vận tốc tức thời và mối liên hệ với đạo hàm

Vận tốc trung bình là một công cụ hữu ích để đánh giá bức tranh tổng thể của một hành trình, nhưng nó hoàn toàn bất lực trong việc cho ta biết: *Ngay tại thời điểm này, vật đang chạy nhanh hay chậm, và đang tiến hay lùi?*

Một vận động viên bơi lội giành huy chương vàng cự ly $50\,\mathrm m$ tự do (Hình 2.4) là người có độ lớn vận tốc trung bình cao nhất trên cả chặng đua. Nhưng trong suốt $50\,\mathrm m$ ấy, có lúc người đó đạp chân tăng tốc mạnh mẽ sau cú xuất phát, có lúc bơi đều, và có lúc chạm đích với tốc độ khác hẳn. Để mô tả trạng thái chuyển động tại từng khoảnh khắc thời gian cá biệt, vật lý học khai sinh khái niệm **vận tốc tức thời** (*instantaneous velocity*).

![Hình 2.4: Cuộc thi bơi lội trên đường bơi 50 mét](img/young-02/hinh-2-4.png)

::: warning Một "thời điểm" kéo dài bao lâu?
Trong ngôn ngữ đời thường, người ta hay nói *"chờ tôi một thoáng"* hay *"chỉ trong chớp mắt"* để chỉ một khoảng thời gian rất ngắn. Trong toán học và vật lý học, **một thời điểm ($t$) không có bất kỳ độ kéo dài nào**; nó là một nhát cắt thời gian tuyệt đối, một điểm duy nhất trên trục số thời gian.
:::

---

### Định nghĩa giải tích của vận tốc tức thời

Để xác định vận tốc của chiếc xe đua ngay tại vị trí $P_1$ ($t_1$) ở Hình 2.1, ta quan sát vị trí $P_2$ ($t_2$) ở các khoảng thời gian $\Delta t = t_2 - t_1$ ngày càng thu hẹp lại: Từ $1\,\mathrm s$ xuống $0.1\,\mathrm s$, $0.01\,\mathrm s$, rồi $0.001\,\mathrm s$.

Khi khoảng thời gian $\Delta t$ co dần về $0$, độ dời $\Delta x$ cũng co dần về $0$. Tuy nhiên, tỷ số $\frac{\Delta x}{\Delta t}$ giữa hai lượng vô cùng bé ấy không hề triệt tiêu, mà tiệm cận đến một giá trị hữu hạn xác định. Giới hạn toán học này chính là **đạo hàm của tọa độ $x$ theo thời gian $t$**:

$$v_x = \lim_{\Delta t \to 0} \frac{\Delta x}{\Delta t} = \frac{dx}{dt}.\tag{2.3}$$

Thành phần vận tốc tức thời $v_x$ chính là **tốc độ biến thiên tức thời của tọa độ vị trí theo thời gian**:
- Nếu $v_x > 0$: Tọa độ $x$ đang tăng, vật chuyển động theo **chiều dương**.
- Nếu $v_x < 0$: Tọa độ $x$ đang giảm, vật chuyển động theo **chiều âm**.
- Nếu $v_x = 0$: Vật dừng lại tức thời tại thời điểm đó (đổi chiều chuyển động hoặc đứng yên).

![Hình 2.5: Dấu của vận tốc tức thời phụ thuộc vào cách chọn chiều dương hệ trục](img/young-02/hinh-2-5.png)

---

### Phân biệt rạch ròi: Vận tốc tức thời và Tốc độ tức thời

Trong đời sống, hai từ "vận tốc" và "tốc độ" thường bị dùng lẫn lộn như từ đồng nghĩa. Nhưng trong vật lý chuẩn tắc, chúng là hai khái niệm khác nhau về bản chất:
1. **Vận tốc tức thời ($v_x$):** Là một **đại lượng vector** (trong chuyển động 1D, được biểu thị bằng một số có dấu). Nó mang đầy đủ thông tin: Độ nhanh chậm VÀ chiều chuyển động.
2. **Tốc độ tức thời ($v$):** Là một **đại lượng vô hướng không âm**, chính là **độ lớn của vận tốc tức thời**:
   $$v = |v_x|.$$
   Đồng hồ đo tốc độ (*speedometer*) trên bảng táp-lô ô tô chỉ hiển thị tốc độ tức thời (ví dụ $80\,\mathrm{km/h}$); nó không hề biết bạn đang đi về phía bắc hay phía nam. Hai chiếc xe chạy ngược chiều nhau trên cùng một đoạn đường có thể có cùng tốc độ tức thời $20\,\mathrm{m/s}$, nhưng vận tốc tức thời của chúng mang dấu trái ngược: Chiếc này là $+20\,\mathrm{m/s}$ thì chiếc kia là $-20\,\mathrm{m/s}$.

::: warning Tốc độ trung bình KHÔNG PHẢI là độ lớn của vận tốc trung bình!
Đây là một cạm bẫy kinh điển:
- Vận tốc trung bình $= \dfrac{\text{Độ dời}}{\text{Thời gian}} = \dfrac{\Delta x}{\Delta t}$.
- Tốc độ trung bình $= \dfrac{\text{Tổng quãng đường}}{\text{Thời gian}} = \dfrac{s}{\Delta t}$.

Năm 2009, kình ngư César Cielo lập kỷ lục thế giới bơi $100.0\,\mathrm m$ trong $46.91\,\mathrm s$. Trong bể bơi tiêu chuẩn dài $50\,\mathrm m$, anh bơi đi rồi bơi về, chạm thành bể đúng tại điểm xuất phát ban đầu. Độ dời tổng cộng $\Delta x = 0 \implies$ **vận tốc trung bình bằng đúng 0**! Trong khi đó, tổng quãng đường bơi là $100\,\mathrm m \implies$ **tốc độ trung bình là $100.0 / 46.91 \approx 2.132\,\mathrm{m/s}$**.
:::

*Ứng dụng đời sống — Súng bắn tốc độ laser (LIDAR):* Cảnh sát giao thông sử dụng súng bắn tốc độ laser phát ra hàng trăm xung ánh sáng hồng ngoại cực ngắn trong khoảng thời gian chưa đầy $0.3\,\mathrm s$. Bằng cách đo thời gian xung phản xạ quay về từ thân xe để tính liên tiếp các khoảng cách, bộ vi xử lý thực hiện phép tính vi phân giới hạn $\Delta x / \Delta t$ tức thời để bắt chính xác tốc độ của xe tại thời điểm bị bắn.

---

### Ví dụ 2.1 — Vận tốc trung bình và tức thời

::: exercise Bài toán
Một con báo săn cheetah đang phục kích một đàn linh dương ở một vị trí cách xe quan sát của kiểm lâm $20\,\mathrm m$ về phía đông (Hình 2.6). Đúng thời điểm $t = 0$, con báo bắt đầu lao thẳng về phía đông để tấn công con linh dương cách xe $50\,\mathrm m$. Trong $2.0\,\mathrm s$ đầu tiên của đợt bứt tốc, tọa độ của con báo thay đổi theo quy luật hàm số:

$$x(t) = 20\,\mathrm m + (5.0\,\mathrm{m/s^2})t^2.$$

**(a)** Tính độ dời của con báo trong khoảng thời gian từ $t_1 = 1.0\,\mathrm s$ đến $t_2 = 2.0\,\mathrm s$.  
**(b)** Tính vận tốc trung bình trong khoảng thời gian đó.  
**(c)** Tìm vận tốc tức thời của con báo tại thời điểm $t_1 = 1.0\,\mathrm s$ bằng cách tính vận tốc trung bình trên các khoảng thời gian $\Delta t$ nhỏ dần: $0.1\,\mathrm s$, $0.01\,\mathrm s$ và $0.001\,\mathrm s$.  
**(d)** Thiết lập biểu thức giải tích của vận tốc tức thời theo thời gian bằng đạo hàm, từ đó tính vận tốc tức thời tại $t = 1.0\,\mathrm s$ và $t = 2.0\,\mathrm s$.
:::

![Hình 2.6: Phân tích chuyển động săn mồi của báo cheetah trên hệ trục tọa độ](img/young-02/hinh-2-6.png)

::: solution Hướng dẫn giải
**Nhận diện và thiết lập:**
Chọn trục $Ox$ hướng thẳng về phía đông, gốc $O$ đặt tại vị trí xe kiểm lâm. Chiều dương hướng từ xe tới đàn linh dương.
Ta dùng công thức độ dời (2.1), vận tốc trung bình (2.2) và đạo hàm vận tốc tức thời (2.3).

**Thực thi:**
**(a)** Tọa độ của báo tại hai thời điểm:
$$x(1.0\,\mathrm s) = 20 + 5.0(1.0)^2 = 25.0\,\mathrm m,$$
$$x(2.0\,\mathrm s) = 20 + 5.0(2.0)^2 = 20 + 5.0(4.0) = 40.0\,\mathrm m.$$
Độ dời của báo là:
$$\Delta x = x(2.0) - x(1.0) = 40.0\,\mathrm m - 25.0\,\mathrm m = +15.0\,\mathrm m.$$

**(b)** Vận tốc trung bình trong khoảng $1.0\,\mathrm s$ đó:
$$v_{\mathrm{av}-x} = \frac{\Delta x}{\Delta t} = \frac{15.0\,\mathrm m}{2.0\,\mathrm s - 1.0\,\mathrm s} = +15.0\,\mathrm{m/s}.$$

**(c)** Khảo sát quá trình tiệm cận giới hạn khi $\Delta t \to 0$:
- Với $\Delta t = 0.1\,\mathrm s \implies t_2 = 1.1\,\mathrm s$:
  $$x(1.1) = 20 + 5.0(1.1)^2 = 26.05\,\mathrm m \implies v_{\mathrm{av}-x} = \frac{26.05 - 25.0}{0.1} = 10.5\,\mathrm{m/s}.$$
- Với $\Delta t = 0.01\,\mathrm s \implies t_2 = 1.01\,\mathrm s$:
  $$x(1.01) = 20 + 5.0(1.01)^2 = 25.1005\,\mathrm m \implies v_{\mathrm{av}-x} = \frac{25.1005 - 25.0}{0.01} = 10.05\,\mathrm{m/s}.$$
- Với $\Delta t = 0.001\,\mathrm s \implies t_2 = 1.001\,\mathrm s$:
  $$x(1.001) = 20 + 5.0(1.001)^2 = 25.010005\,\mathrm m \implies v_{\mathrm{av}-x} = 10.005\,\mathrm{m/s}.$$

Khi $\Delta t$ tiến dần về $0$, vận tốc trung bình tiệm cận rõ ràng tới giá trị chính xác là **$10.0\,\mathrm{m/s}$**.

**(d)** Lấy đạo hàm trực tiếp của hàm vị trí:
$$v_x(t) = \frac{dx}{dt} = \frac{d}{dt}\left[20 + 5.0t^2\right] = 0 + (5.0)(2t) = (10.0\,\mathrm{m/s^2})t.$$

Thay số:
- Tại $t = 1.0\,\mathrm s$: $v_x(1.0) = 10.0 \times 1.0 = +10.0\,\mathrm{m/s}$ (hoàn toàn khớp với kết quả giới hạn ở câu c).
- Tại $t = 2.0\,\mathrm s$: $v_x(2.0) = 10.0 \times 2.0 = +20.0\,\mathrm{m/s}$.

**Đánh giá:** Vận tốc tức thời tăng đều từ $0$ lên $10\,\mathrm{m/s}$ rồi $20\,\mathrm{m/s}$ phản ánh sức bứt tốc kinh hoàng của loài báo săn (đạt $72\,\mathrm{km/h}$ chỉ sau đúng 2 giây). Vận tốc trung bình trong cả khoảng ($15.0\,\mathrm{m/s}$) nằm chính xác ở trung điểm giữa vận tốc đầu ($10.0\,\mathrm{m/s}$) và vận tốc cuối ($20.0\,\mathrm{m/s}$).
:::

---

### Ý nghĩa hình học: Vận tốc tức thời là độ dốc của tiếp tuyến trên đồ thị $x-t$

Trên đồ thị tọa độ – thời gian ($x-t$), khi khoảng thời gian $\Delta t$ co dần về $0$, điểm $p_2$ trượt dọc theo đường cong tiến sát đến điểm $p_1$ (Hình 2.7a, b).

Đường cát tuyến nối $p_1p_2$ trong quá trình đó dần xoay và trở thành **đường tiếp tuyến** của đường cong tại điểm $p_1$ (Hình 2.7c).

$$\text{Độ dốc của tiếp tuyến tại } p_1 = \left.\frac{dx}{dt}\right|_{t_1} = v_x(t_1).$$

![Hình 2.7: Quá trình chuyển từ độ dốc cát tuyến sang độ dốc tiếp tuyến](img/young-02/hinh-2-7.png)

Nguyên lý hình học cốt lõi: **Vận tốc tức thời tại một thời điểm bất kỳ bằng đúng độ dốc (hệ số góc) của tiếp tuyến với đồ thị $x-t$ tại thời điểm đó**:
- **Tiếp tuyến dốc lên sang phải:** Độ dốc dương $\implies v_x > 0$ (vật chuyển động theo chiều dương).
- **Tiếp tuyến nằm ngang:** Độ dốc bằng $0 \implies v_x = 0$ (vật dừng lại tức thời).
- **Tiếp tuyến dốc xuống sang phải:** Độ dốc âm $\implies v_x < 0$ (vật chuyển động theo chiều âm).
- Độ dốc càng dốc (độ lớn càng lớn), vật chuyển động càng nhanh; tiếp tuyến càng là là nằm ngang, vật chuyển động càng chậm (Hình 2.8).

![Hình 2.8: Tương quan giữa đồ thị x-t và chuyển động thực tế qua các thời điểm](img/young-02/hinh-2-8.png)

---

### Câu hỏi kiểm tra hiểu biết mục 2.2

::: exercise Câu hỏi kiểm tra
Hình 2.9 mô tả đồ thị vị trí theo thời gian ($x-t$) của một chất điểm.

![Hình 2.9: Đồ thị x-t với bốn điểm khảo sát P, Q, R, S](img/young-02/hinh-2-9.png)

**(a)** Hãy sắp xếp vận tốc tức thời $v_x$ tại các điểm P, Q, R, S theo thứ tự từ giá trị dương lớn nhất đến giá trị âm lớn nhất.  
**(b)** Những điểm nào có $v_x > 0$?  
**(c)** Những điểm nào có $v_x < 0$?  
**(d)** Những điểm nào có $v_x = 0$?  
**(e)** Hãy sắp xếp tốc độ tức thời tại các điểm theo thứ tự từ nhanh nhất đến chậm nhất.
:::

::: solution Lời giải
Bằng cách quan sát độ dốc tiếp tuyến tại từng điểm:
- **Tại P:** Tiếp tuyến dốc lên sang phải $\implies v_x > 0$ (vận tốc dương).
- **Tại Q và S:** Đây là các điểm cực trị (đỉnh cong) của đồ thị, tiếp tuyến nằm ngang hoàn toàn $\implies v_x = 0$.
- **Tại R:** Tiếp tuyến dốc xuống sang phải $\implies v_x < 0$ (vận tốc âm).

**(a)** Thứ tự đại số của vận tốc:
$$v_P > v_Q = v_S (= 0) > v_R.$$

**(b)** Điểm có $v_x > 0$ là: **P**.  
**(c)** Điểm có $v_x < 0$ là: **R**.  
**(d)** Điểm có $v_x = 0$ là: **Q và S**.

**(e) Tốc độ tức thời** là giá trị tuyệt đối của độ dốc ($|v_x|$). Quan sát hình vẽ, tại điểm R đường cong dốc đứng nhất (độ dốc âm rất dốc) $\implies |v_R|$ lớn nhất. Tiếp theo là P. Tại Q và S tốc độ triệt tiêu bằng 0.
Thứ tự tốc độ:
$$v_{\text{tốc độ, } R} > v_{\text{tốc độ, } P} > v_{\text{tốc độ, } Q} = v_{\text{tốc độ, } S} (= 0).$$
:::
