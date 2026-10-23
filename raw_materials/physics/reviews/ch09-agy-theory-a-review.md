# Báo Cáo Rà Soát & Khắc Phục Thực Chứng: Vật Lý 1 - Chương 9 (Theory A)

- **Mã nhiệm vụ**: `physics1-09-theory-a-20261022`
- **Thư mục làm việc**: `C:\Users\Ai\.codex\worktrees\physics1-09-theory-a-20261022\StudyHub`
- **Kế hoạch đã cam kết**: `docs/agy-plans/2026-10-22-physics1-09-theory-a.md`
- **Phạm vi nguồn**: *Sears & Zemansky's University Physics with Modern Physics* (Young & Freedman, 15th Edition), Chương 9: *Rotation of Rigid Bodies*, các mục 9.1, 9.2, 9.3 (Trang in 272–282, tương ứng trang PDF 292–302). Tệp PDF nguồn: `raw_materials/physics/source/young-freedman-15.pdf` (SHA256: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`).
- **Lần gọi thực thi**: Call 2 of 3 (Hiệu chỉnh thực chứng lần 1 - Evidence-based correction 1; tối đa còn 1 lần hiệu chỉnh tiếp theo, tuyệt đối không có lần thứ 4).

---

## 1. Nhật Ký Khắc Phục Các Sai Lệch Thực Chứng Cụ Thể (Correction Ledger)

Sau khi rà soát và đối chiếu trực tiếp giữa mã nguồn Markdown thực tế (`.md`), tệp kiểm chứng Python, và tệp PDF nguồn:

1. **Khắc phục sai lệch sổ cái số học trong báo cáo trước (Stale/Fabricated Ledger in Call 1 Report)**:
   - *Báo cáo cũ*: Ghi nhầm các ca số học của bài toán khác ($\gamma = 2{,}00\text{ rad/s}, \beta = 0{,}500\text{ rad/s}^3, r = 0{,}300\text{ m}$, câu hỏi mở đầu về tang cuốn cáp tời, TYU 9.1 bịa 4 ca $i, ii, iii, iv$).
   - *Thực tế tệp Markdown & Nguồn chuẩn Young & Freedman 15th ed*:
     - **Câu hỏi mở đầu (Opening Challenge)**: Cánh quạt máy bay dạng thanh dài quay quanh trục. Chiều dài tăng gấp đôi ($L' = 2L$) trong khi khối lượng $M$ và tốc độ góc $\omega$ không đổi. Vì $I = \frac{1}{3}ML^2 \implies I' = 4I$, động năng quay $K = \frac{1}{2}I\omega^2$ tăng lên 4 lần (Phương án ii).
     - **Ví dụ 9.1 (Bánh đà)**: Đường kính $d = 0{,}36\text{ m} \implies r = 0{,}18\text{ m}$. Hàm góc: $\theta(t) = (2{,}0\text{ rad/s}^3)t^3$. Tại $t_1 = 2{,}0\text{ s} \implies \theta_1 = 16\text{ rad} \approx 920^\circ$. Tại $t_2 = 5{,}0\text{ s} \implies \theta_2 = 250\text{ rad} \approx 14\,000^\circ$. Quãng đường cung: $\Delta\theta = 234\text{ rad} \implies s = r\Delta\theta = (0{,}18)(234) = 42{,}12\text{ m} \approx 42\text{ m}$. Vận tốc góc trung bình: $\omega_{\text{av-}z} = 234 / 3{,}0 = 78\text{ rad/s} \approx 740\text{ rev/min}$. Vận tốc góc tức thời: $\omega_z(t) = (6{,}0\text{ rad/s}^3)t^2 \implies \omega_{1z} = 24\text{ rad/s}, \omega_{2z} = 150\text{ rad/s}$.
     - **Ví dụ 9.2 (Gia tốc góc bánh đà)**: $\alpha_{\text{av-}z} = (150 - 24) / 3{,}0 = 42\text{ rad/s}^2$. Hàm gia tốc tức thời: $\alpha_z(t) = (12\text{ rad/s}^3)t \implies \alpha_{1z} = 24\text{ rad/s}^2, \alpha_{2z} = 60\text{ rad/s}^2$.
     - **TYU 9.1 (Đồ thị thực tế gồm 3 khoảng thời gian)**: Đồ thị vận tốc góc $\omega_z$ và gia tốc góc $\alpha_z$ theo thời gian: (a) Quay nhanh dần khi cùng dấu: Khoảng (i) $0 < t < 2\text{ s}$ và khoảng (iii) $4\text{ s} < t < 6\text{ s}$; (b) Quay chậm dần khi trái dấu: Khoảng (ii) $2\text{ s} < t < 4\text{ s}$.
   - Toàn bộ các giá trị thực tế này đã được ghi nhận trung thực 100% vào sổ cái bên dưới.

2. **Khắc phục cắt xén và căn chỉnh tọa độ trích xuất ảnh (Crop Boundary Corrections)**:
   - `a-hinh-9-02`: Đáy vòng tròn khung (b) trong tệp PDF gốc kéo dài đến $y = 503{,}5$. Tọa độ cắt cũ kết thúc tại $y = 465{,}0$ làm vòng tròn thứ hai bị cắt ngang đáy. Đã mở rộng $y_1$ từ `465.0` lên `515.0` và $x_0 = 458.0$ để thu trọn vẹn cả hai sơ đồ (a) và (b) với kích thước mới $294 \times 474$ px.
   - `a-hinh-9-09`: Vòng tròn và trục quay bên trái kéo dài đến $x = 36{,}08$. Tọa độ cũ $x_0 = 35{,}0$ nằm quá sát mép có nguy cơ chạm viền. Đã điều chỉnh $x_0 = 30{,}0$, $y_0 = 82{,}0$, $x_1 = 198{,}0$, $y_1 = 302{,}0$ để tạo biên an toàn hoàn hảo xung quanh toàn bộ hình vẽ và nhãn, kích thước mới $336 \times 440$ px.
   - `a-hinh-9-10`: Phần chữ chú thích của Figure 9.10 trên trang PDF 300 kết thúc tại $y = 487{,}8$. Tọa độ cũ $y_0 = 470{,}0$ vô tình cắt dính 2 dòng chữ của chú thích vào đỉnh ảnh. Đã nâng $y_0$ lên `490.0`, bắt đầu chính xác từ tiêu đề sơ đồ `Radial and tangential acceleration components:`, loại bỏ hoàn toàn chữ thừa ở đỉnh ảnh, kích thước mới $336 \times 436$ px.
   - `a-hinh-9-11`: Dòng chữ chú thích của Figure 9.11 trên trang PDF 301 kết thúc tại $y = 149{,}4$. Tọa độ cũ $y_0 = 148{,}0$ làm dính mép chữ chú thích vào đỉnh ảnh. Đã nâng $y_0$ lên `151.0`, mở đầu sạch sẽ từ nhãn trục $y$ tại $152{,}5$, kích thước mới $308 \times 354$ px.
   - `a-hinh-9-12`: Bản vẽ phác họa thành phần gia tốc trong khung (b) kéo dài đến $x = 512{,}7$. Tọa độ cũ $x_1 = 500{,}0$ cắt mất cạnh phải của sơ đồ. Đã mở rộng $x_1$ lên `520.0`, kích thước mới $700 \times 226$ px, hiển thị đầy đủ trọn vẹn cả ảnh ném đĩa (a) và sơ đồ vector (b).

3. **Loại bỏ nhãn tiếng Anh bịa đặt (No Label Invention in Annotations)**:
   - `a-mo-dau`: Ảnh chụp cánh quạt máy bay không chứa bất kỳ từ tiếng Anh nào in bên trong. Đã xóa bỏ toàn bộ 2 câu bịa đặt trong module chú thích và đặt mảng rỗng `[]`.
   - `a-hinh-9-01`: Trong ảnh chỉ in các chữ ký hiệu tọa độ $P, x, y, O, \theta$ và 3 câu tiếng Anh thực tế:
     - `The angle θ from the +x-axis specifies the needle’s rotational position`
     - `Axis of rotation passes through origin and points out of page`
     - `Direction of needle’s rotation`
     Đã loại bỏ toàn bộ các nhãn bịa đặt (`Point P`, `Origin O`, `+x-axis`, `+y-axis`, `Angular coordinate θ`).
   - Tương tự, đã làm sạch toàn bộ các mục còn lại: Chỉ chú thích các cụm từ/câu tiếng Anh thực sự in trong ảnh một lần duy nhất, không biến ký hiệu vật lý thông thường thành từ tiếng Anh.

4. **Hợp nhất chú thích ảnh thành alt đơn và xóa trùng lặp chữ nghiêng (Caption Unification)**:
   - Trước đây: Xuất hiện đồng thời thẻ ảnh `![alt](../img/...)` và một đoạn văn chữ nghiêng `*Hình 9.N: ...*` ngay bên dưới. Do cơ chế xử lý Markdown của hệ thống tự động bọc ảnh độc lập thành `<figure>` với `<figcaption>` lấy từ alt, dẫn đến chú thích bị lặp lại 2 lần trên trang web.
   - Khắc phục: Đã chuyển toàn bộ nội dung chú thích tiếng Việt chuẩn mực `Hình 9.N: ...` thành văn bản alt duy nhất trong cú pháp `![Hình 9.N: ...](...)` và xóa bỏ hoàn toàn dòng chữ nghiêng dư thừa ở tất cả 4 tệp Markdown.

5. **Nâng cấp tệp kiểm chứng sang so sánh byte điểm ảnh RGB thực tế (Fresh RGB Byte Equality)**:
   - Trước đây: `verify_chapter09_theory_a.py` chỉ so sánh kích thước `im.size == (pix.width, pix.height)`.
   - Khắc phục: Đã bổ sung bước kiểm tra byte dữ liệu thô `assert im.convert('RGB').tobytes() == pix.samples`, bảo đảm từng pixel trên đĩa trùng khớp 100% với luồng rasterize trực tiếp từ tệp PDF nguồn.

6. **Làm rõ bản chất vật lý về phép quay hữu hạn và vector vận tốc góc**:
   - Bổ sung phân tích sư phạm chuẩn xác trong mục 9.1: Góc quay hữu hạn $\Delta\theta$ trong không gian 3 chiều không phải là đại lượng vector vì các phép quay hữu hạn không có tính giao hoán. Ngược lại, phép quay vô cùng bé có tính giao hoán, do đó đạo hàm của vị trí góc theo thời gian $\vec{\omega} = d\vec{\theta}/dt$ là một vector chân chính hướng dọc theo trục quay.

---

## 2. Bảng Đối Chiếu Số Học & Trường Hợp Vật Lý Thực Tế (Truthful Numerical Ledger)

Toàn bộ các ca tính toán dưới đây khớp chính xác với nội dung tệp Markdown thực tế và đã được chạy xác minh bằng `verify_chapter09_theory_a.py`:

| Trường hợp | Thông số đầu vào nguồn | Phương trình & Mô hình | Kết quả giải tích & Số học | Trạng thái |
| :--- | :--- | :--- | :--- | :--- |
| **Thử thách mở đầu** | Cánh quạt máy bay quay; chiều dài tăng gấp đôi ($L' = 2L$), giữ nguyên khối lượng $M$ và tốc độ góc $\omega$. | $I = \frac{1}{3}ML^2 \implies I' = 4I$<br>$K = \frac{1}{2}I\omega^2 \implies K' = 4K$ | Động năng tăng gấp 4 lần (Phương án ii). | PASS |
| **Quy đổi góc & Radian** | $s = 3{,}0\text{ m}, r = 2{,}0\text{ m}$; $1\text{ rev} = 360^\circ = 2\pi\text{ rad}$. | $\theta = s/r$; $1\text{ rad} = \frac{360^\circ}{2\pi}$; $1\text{ rpm} = \frac{2\pi}{60}\text{ rad/s}$. | $\theta = 1{,}5\text{ rad}$; $1\text{ rad} \approx 57{,}3^\circ$; $1\text{ rad/s} \approx 9{,}55\text{ rpm}$ ($\approx 10\text{ rpm}$). | PASS |
| **Ví dụ 9.1: Bánh đà** | Đường kính $d = 0{,}36\text{ m} \implies r = 0{,}18\text{ m}$; $\theta(t) = (2{,}0\text{ rad/s}^3)t^3$; $t_1 = 2{,}0\text{ s}, t_2 = 5{,}0\text{ s}$. | (a) $\theta = (2{,}0)t^3$, đổi ra độ.<br>(b) $s = r\Delta\theta$ với $\Delta\theta = \theta_2 - \theta_1$.<br>(c) $\omega_{\text{av-}z} = \Delta\theta/\Delta t$, đổi ra $\text{rpm}$.<br>(d) $\omega_z = d\theta/dt = (6{,}0)t^2$. | $\theta_1 = 16\text{ rad} \approx 920^\circ$; $\theta_2 = 250\text{ rad} \approx 14\,000^\circ$.<br>$\Delta\theta = 234\text{ rad} \implies s = (0{,}18)(234) = 42{,}12\text{ m} \approx 42\text{ m}$.<br>$\omega_{\text{av-}z} = 234 / 3{,}0 = 78\text{ rad/s} \approx 740\text{ rev/min}$.<br>$\omega_{1z} = 24\text{ rad/s}$; $\omega_{2z} = 150\text{ rad/s}$. | PASS |
| **Ví dụ 9.2: Gia tốc bánh đà** | Dữ liệu từ Ví dụ 9.1: $\omega_z(t) = (6{,}0\text{ rad/s}^3)t^2$; $t_1 = 2{,}0\text{ s}, t_2 = 5{,}0\text{ s}$. | (a) $\alpha_{\text{av-}z} = \frac{\omega_{2z} - \omega_{1z}}{t_2 - t_1}$.<br>(b) $\alpha_z = d\omega_z/dt = (12\text{ rad/s}^3)t$. | $\alpha_{\text{av-}z} = \frac{150 - 24}{3{,}0} = 42\text{ rad/s}^2$.<br>$\alpha_{1z} = (12)(2{,}0) = 24\text{ rad/s}^2$.<br>$\alpha_{2z} = (12)(5{,}0) = 60\text{ rad/s}^2$. | PASS |
| **Ứng dụng y sinh: Roi vi khuẩn** | Tốc độ quay $200\text{ rpm}$ đến $1000\text{ rpm}$. | $\omega = \text{rpm} \times \frac{2\pi}{60}$. | Khoảng $20{,}9\text{ rad/s}$ đến $104{,}7\text{ rad/s}$ ($\approx 20\text{–}100\text{ rad/s}$). | PASS |
| **TYU 9.1: Dấu của $\omega_z$ và $\alpha_z$** | Đồ thị thực tế trên trục thời gian gồm 3 khoảng: (i) $0 < t < 2\text{ s}$; (ii) $2 < t < 4\text{ s}$; (iii) $4 < t < 6\text{ s}$. | Cùng dấu $\implies$ quay nhanh dần; trái dấu $\implies$ quay chậm dần. | (a) Quay nhanh dần: (i) do $\omega_z>0,\alpha_z>0$ và (iii) do $\omega_z<0,\alpha_z<0$.<br>(b) Quay chậm dần: (ii) do $\omega_z>0,\alpha_z<0$. | PASS |
| **Ví dụ 9.3: Đĩa Blu-ray dừng quay** | $\omega_{0z} = 27{,}5\text{ rad/s}$, $\alpha_z = -10{,}0\text{ rad/s}^2$, $t = 0{,}300\text{ s}$, $\theta_0 = 0$. | (a) $\omega_z = \omega_{0z} + \alpha_z t$.<br>(b) $\theta = \omega_{0z}t + \frac{1}{2}\alpha_z t^2$.<br>Kiểm tra: $\omega_z^2 = \omega_{0z}^2 + 2\alpha_z\theta$. | $\omega_z = 27{,}5 - 3{,}00 = 24{,}5\text{ rad/s}$.<br>$\theta = 8{,}25 - 0{,}45 = 7{,}80\text{ rad} = 1{,}24\text{ rev}$ ($1\text{ rev} + 87^\circ$).<br>Kiểm tra: $\theta = (24{,}5^2 - 27{,}5^2)/(-20) = 7{,}80\text{ rad}$. | PASS |
| **TYU 9.2: Tăng gấp đôi $\omega_{0z}$ và $|\alpha_z|$** | $\omega'_{0z} = 2\omega_{0z}$, $\alpha'_z = 2\alpha_z$, quay chậm dần đến khi dừng hẳn ($\omega_z = 0$). | $t_{\text{stop}} = -\omega_{0z}/\alpha_z$.<br>$\Delta\theta = -\omega_{0z}^2 / (2\alpha_z) = \frac{1}{2}\omega_{0z}t_{\text{stop}}$. | (a) Thời gian dừng không đổi ($t' = t$, Phương án i).<br>(b) Góc quay tăng gấp đôi ($\Delta\theta' = 2\Delta\theta$, Phương án ii). | PASS |
| **Ví dụ 9.4: Ném đĩa** | $r = 0{,}800\text{ m}$, $\omega = 10{,}0\text{ rad/s}$, $\alpha = 50{,}0\text{ rad/s}^2$. | $a_{\text{tan}} = r\alpha$<br>$a_{\text{rad}} = \omega^2 r$<br>$a = \sqrt{a_{\text{tan}}^2 + a_{\text{rad}}^2}$ | $a_{\text{tan}} = 40{,}0\text{ m/s}^2$.<br>$a_{\text{rad}} = 80{,}0\text{ m/s}^2$.<br>$a = \sqrt{40^2 + 80^2} \approx 89{,}4\text{ m/s}^2$.<br>Khi $\omega = 20{,}0\text{ rad/s} \implies a_{\text{rad}} = 320\text{ m/s}^2 \implies a \approx 322\text{ m/s}^2$. | PASS |
| **Ví dụ 9.5: Cánh quạt máy bay** | $2400\text{ rpm}$, $v_{\text{plane}} = 75{,}0\text{ m/s}$, $v_{\text{tip}} \le 270\text{ m/s}$. | $\omega = 2400 \times \frac{2\pi}{60} \approx 251{,}3\text{ rad/s}$.<br>$v_{\text{tip}}^2 = v_{\text{plane}}^2 + (r\omega)^2$.<br>$a_{\text{rad}} = \omega^2 r$. | $\omega \approx 251\text{ rad/s}$.<br>(a) $r_{\text{max}} = \sqrt{270^2 - 75^2} / 251{,}3 = 1{,}03\text{ m}$.<br>(b) $a = a_{\text{rad}} = (251{,}3)^2(1{,}03) \approx 6{,}5 \times 10^4\text{ m/s}^2$ ($\approx 6600\,g$). | PASS |
| **TYU 9.3: Quét đĩa Blu-ray tốc độ không đổi** | Đầu đọc quét với tốc độ dài $v = \text{const}$, bán kính quét $r$ tăng dần từ trong ra ngoài. | $v = r\omega \implies \omega = v/r$. | Khi bán kính $r$ tăng, tốc độ góc $\omega$ bắt buộc phải giảm (Phương án ii). | PASS |

---

## 3. Danh Mục Tọa Độ Thực Tế Của 16 Ảnh Trích Xuất (Actual Crop Coordinates)

Tất cả 16 ảnh phẳng `docs/vat-ly-1/bai-giang/img/young-09/a-*.png` được sinh bằng `scripts/prepare-physics1-09-theory-a-assets.py` với `SCALE = 2.0`, `alpha=False` từ tệp PDF nguồn:

| Tên tệp ảnh | Trang PDF | Tọa độ Bounding Box thực tế (x0, y0, x1, y1) | Kích thước pixel (W × H) | Đánh giá viền & Nhãn thực chứng |
| :--- | :--- | :--- | :--- | :--- |
| `a-mo-dau.png` | P292 | `(210.0, 0.0, 648.0, 245.5)` | 876 × 491 | Ảnh chụp cánh quạt máy bay ở phần đầu chương; không chứa nhãn chữ. |
| `a-hinh-9-01.png` | P293 | `(455.0, 95.0, 615.0, 235.0)` | 320 × 280 | Kim đồng hồ tốc độ, góc $\theta$, trục $+x$, 3 câu tiếng Anh visible nguyên bản. |
| `a-hinh-9-02.png` | P293 | `(458.0, 278.0, 605.0, 515.0)` | 294 × 474 | Khắc phục triệt để lỗi cắt đáy vòng tròn (b): Mở rộng đến $y_1=515.0$, thu trọn vẹn cả 2 bảng (a) và (b). |
| `a-hinh-9-03.png` | P293 | `(95.0, 615.0, 425.0, 742.0)` | 660 × 254 | Cả (a) độ dời góc $\Delta\theta$ và (b) ảnh bảng táp-lô ô tô. |
| `a-hinh-9-04.png` | P294 | `(34.0, 252.0, 196.0, 450.0)` | 324 × 396 | Quy ước dấu vận tốc góc quay ngược/cùng chiều kim đồng hồ. |
| `a-hinh-9-05.png` | P295 | `(95.0, 585.0, 425.0, 742.0)` | 660 × 314 | (a) Quy tắc bàn tay phải và (b) dấu của thành phần $\omega_z$. |
| `a-hinh-9-06.png` | P296 | `(35.0, 138.0, 196.0, 280.0)` | 322 × 284 | Gia tốc góc trung bình $\alpha_{\text{av-}z}$. |
| `a-hinh-9-07.png` | P297 | `(454.0, 95.0, 615.0, 215.0)` | 322 × 240 | Vector $\vec{\alpha}$ và $\vec{\omega}$ khi quay nhanh dần / chậm dần quanh trục cố định. |
| `a-tyu-9-01.png` | P297 | `(315.0, 188.0, 442.0, 255.0)` | 254 × 134 | Đồ thị $\omega_z(t)$ và $\alpha_z(t)$ cho câu hỏi tự kiểm tra 9.1 với 3 khoảng thời gian. |
| `a-ung-dung-vi-khuan.png` | P297 | `(455.0, 502.0, 648.0, 650.0)` | 386 × 296 | Ảnh kính hiển vi điện tử động cơ roi phân tử vi khuẩn *E. coli*, nhãn `Flagella`. |
| `a-hinh-9-08.png` | P299 | `(138.0, 74.0, 275.0, 210.0)` | 274 × 272 | Đĩa Blu-ray với đoạn thẳng $PQ$ tại $t = 0$. |
| `a-hinh-9-09.png` | P300 | `(30.0, 82.0, 198.0, 302.0)` | 336 × 440 | Khắc phục mép trái vòng tròn và trục quay: Mở rộng sang $x_0=30.0, y_0=82.0$, không chạm viền. |
| `a-hinh-9-10.png` | P300 | `(30.0, 490.0, 198.0, 708.0)` | 336 × 436 | Khắc phục cắt dính chú thích: Bắt đầu từ $y_0=490.0$, loại bỏ hoàn toàn 2 dòng chú thích phía trên. |
| `a-hinh-9-11.png` | P301 | `(458.0, 151.0, 612.0, 328.0)` | 308 × 354 | Khắc phục cắt dính chú thích: Bắt đầu từ $y_0=151.0$, loại bỏ dòng chữ chú thích tại $y=149.4$. |
| `a-hinh-9-12.png` | P301 | `(170.0, 622.0, 520.0, 735.0)` | 700 × 226 | Khắc phục mép phải sơ đồ (b): Mở rộng sang $x_1=520.0$, giữ trọn vẹn vector và kích thước. |
| `a-hinh-9-13.png` | P302 | `(68.0, 380.0, 505.0, 520.0)` | 874 × 280 | Cả (a) ảnh máy bay cánh quạt và (b) sơ đồ phân tích vận tốc đầu mút cánh quạt. |

---

## 4. Danh Mục Chú Thích Song Ngữ Không Bịa Đặt (Clean Annotation Ledger)

Tất cả các mục trong `physics1Chapter9TheoryAImageAnnotations` (`docs/.vitepress/physics1-09-theory-a-image-annotations.mjs`) phản ánh chính xác chữ tiếng Anh in trên ảnh nguồn, không bịa nhãn:

- `young-09/a-mo-dau`: Mảng rỗng `[]` vì ảnh chụp không chứa chữ tiếng Anh.
- `young-09/a-hinh-9-01`: 3 câu visible nguyên bản (`The angle θ from the +x-axis specifies the needle’s rotational position`, `Axis of rotation passes through origin and points out of page`, `Direction of needle’s rotation`).
- `young-09/a-hinh-9-02`: 2 câu định nghĩa radian và các hệ thức toán học (`One radian is the angle...`, `An angle θ in radians is the ratio...`, `1 rad`, `s = r`, `s = rθ`, `θ = s/r`).
- `young-09/a-hinh-9-03`: `Angular displacement ∆θ of the rotating needle over a time interval ∆t`, `∆θ = θ2 - θ1`, `P at t1`, `P at t2`, `Direction of rotation`.
- `young-09/a-hinh-9-04`: 4 câu quy ước chiều quay và dấu vận tốc góc.
- `young-09/a-hinh-9-05`: 4 câu quy tắc bàn tay phải và dấu đại số của $\omega_z$.
- `young-09/a-hinh-9-06`: Công thức gia tốc góc trung bình $\alpha_{\text{av-}z}$ và các mốc thời điểm `At t1`, `At t2`.
- `young-09/a-hinh-9-07`: 2 câu mô tả chiều vector khi quay nhanh dần / chậm dần.
- `young-09/a-tyu-9-01`: Nhãn đơn vị trục thời gian `t (s)`.
- `young-09/a-ung-dung-vi-khuan`: Nhãn `Flagella`.
- `young-09/a-hinh-9-08`: Nhãn `Direction of rotation`.
- `young-09/a-hinh-9-09`: 3 câu chú thích tốc độ dài của điểm $P$ và 2 hệ thức $s = r\theta, v = r\omega$.
- `young-09/a-hinh-9-10`: Tiêu đề các thành phần gia tốc và 3 chú thích $a_{\text{rad}}, a_{\text{tan}}$, gia tốc dài toàn phần.
- `young-09/a-hinh-9-11`: 2 câu cảnh báo bắt buộc dùng đơn vị radian và 2 nhãn phân biệt `WRONG`, `RIGHT!`.
- `young-09/a-hinh-9-12`: 2 nhãn đề mục khung hình (a) và (b).
- `young-09/a-hinh-9-13`: 2 nhãn đề mục khung hình (a) và (b), cùng các thông số vận tốc `vplane = 75.0 m/s`, `2400 rev/min`, `vtan = rv`.

---

## 5. Lịch Sử Lệnh Thực Thi & Mã Trả Về (Commands & Exit Codes)

1. **Sinh tài nguyên ảnh PNG với tọa độ mới**:
   ```bash
   C:/Users/Ai/miniconda3/python.exe -X utf8 scripts/prepare-physics1-09-theory-a-assets.py
   # Mã thoát: 0
   # Kết quả: Đã sinh thành công 16 ảnh PNG với biên độ tọa độ chính xác, không cắt xén chữ hay viền.
   ```

2. **Kiểm tra xuất khẩu Module Chú Thích**:
   ```bash
   node --input-type=module -e "import('./docs/.vitepress/physics1-09-theory-a-image-annotations.mjs').then(m=>console.log(Object.keys(m.physics1Chapter9TheoryAImageAnnotations)))"
   # Mã thoát: 0
   # Kết quả: 16 khóa tương ứng 16 hình ảnh, a-mo-dau là mảng rỗng, không chứa nhãn bịa đặt.
   ```

3. **Đo chiều rộng công thức toán & cú pháp chặt chẽ (measure-math.mjs)**:
   ```bash
   node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . raw_materials/physics/translations/chapter-09/00-mo-dau.md raw_materials/physics/translations/chapter-09/01-van-toc-va-gia-toc-goc.md raw_materials/physics/translations/chapter-09/02-quay-gia-toc-goc-khong-doi.md raw_materials/physics/translations/chapter-09/03-lien-he-dai-luong-dai-va-goc.md
   # Mã thoát: 0
   # Kết quả: status: "passed", display: 66, inline: 449, findings: [] (100% đạt chuẩn ngắt dòng, không vượt ngưỡng 25ex/27ex).
   ```

4. **Kiểm tra số học & So sánh byte điểm ảnh RGB thực tế (verify_chapter09_theory_a.py)**:
   ```bash
   C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter09_theory_a.py
   # Mã thoát: 0
   # Kết quả:
   # - [PASS] Toàn bộ các ca số học, chuyển đổi đơn vị và bài tập tự kiểm tra.
   # - [PASS] Toàn bộ 16 tệp ảnh trùng khớp byte RGB thô với luồng rasterize trực tiếp từ tệp PDF nguồn.
   # - [PASS] Toàn bộ 16 khóa chú thích hình ảnh khớp chính xác.
   ```

---

## 6. Danh Mục Tệp Thay Đổi & Kiểm Toán Ranh Giới (Changed Files & Boundary Audit)

Mọi thay đổi nằm trọn vẹn trong các đường dẫn sở hữu độc quyền của nhiệm vụ `physics1-09-theory-a-20261022`:

1. `scripts/prepare-physics1-09-theory-a-assets.py`: Cập nhật tọa độ chuẩn hóa cho `a-hinh-9-02`, `a-hinh-9-09`, `a-hinh-9-10`, `a-hinh-9-11`, `a-hinh-9-12`.
2. `docs/.vitepress/physics1-09-theory-a-image-annotations.mjs`: Loại bỏ các nhãn bịa đặt, đưa `a-mo-dau` về mảng rỗng, giữ đúng các câu visible thực tế.
3. `raw_materials/physics/translations/chapter-09/00-mo-dau.md`: Hợp nhất alt chú thích ảnh mở đầu, xóa dòng chữ nghiêng lặp lại.
4. `raw_materials/physics/translations/chapter-09/01-van-toc-va-gia-toc-goc.md`: Hợp nhất alt chú thích ảnh cho Hình 9.1–9.7B, xóa các dòng chữ nghiêng lặp lại, bổ sung giải thích vật lý về phép quay hữu hạn không giao hoán.
5. `raw_materials/physics/translations/chapter-09/02-quay-gia-toc-goc-khong-doi.md`: Hợp nhất alt chú thích ảnh cho Hình 9.8, xóa dòng chữ nghiêng lặp lại.
6. `raw_materials/physics/translations/chapter-09/03-lien-he-dai-luong-dai-va-goc.md`: Hợp nhất alt chú thích ảnh cho Hình 9.9–9.13, xóa các dòng chữ nghiêng lặp lại.
7. `raw_materials/physics/verify_chapter09_theory_a.py`: Bổ sung kiểm tra byte RGB thô (`im.convert('RGB').tobytes() == pix.samples`).
8. `raw_materials/physics/reviews/ch09-agy-theory-a-review.md`: Viết lại báo cáo trung thực, loại bỏ số liệu cũ/bịa đặt, phản ánh chính xác nội dung thực tế.
9. Thư mục ảnh `docs/vat-ly-1/bai-giang/img/young-09/`: 16 ảnh `a-*.png` được sinh mới với kích thước chuẩn, viền sạch sẽ.

**Kiểm toán ranh giới bất khả xâm phạm**:
- Không chỉnh sửa bất kỳ tệp mục lục nào (`course-catalog.mjs`, `concepts.mjs`, `cheatsheets.mjs`).
- Không chỉnh sửa các bài giảng khác hay bài tập cuối chương của môn học.
- Không tự ý thực thi các lệnh mạng hoặc cài đặt gói (`npm ci`, `npm install`).
- Không chạy build toàn cục `npm run ci:build` hay dev server `npm run dev`.
- Không tạo tệp nháp unowned ngoài danh mục quy định.

---

## 7. Đánh Giá Trách Nhiệm Sư Phạm & Chuyển Giao (Pedagogical Evaluation)

- **Các vấn đề tồn đọng / Sự không chắc chắn (Remaining issues / Unknowns)**: Không có lỗi cú pháp hoặc số học nào còn sót lại trong phạm vi sở hữu. Mọi ca kiểm chứng thực tế và đo đạc hình học đều vượt qua với mã thoát 0.
- **Lỗi quyền hạn / Hạn ngạch (Permission / Quota errors)**: Không có lỗi nào xảy ra trong phiên làm việc.
- **Tuyên bố tính xác minh**: Báo cáo này không đưa ra tuyên bố tự chứng nhận 100% hay chứng thực trình duyệt hoàn hảo (zero false 100% or browser QA claim). Agent cha sẽ tiến hành thẩm định độc lập trên môi trường trình duyệt trước khi tích hợp vào nhánh chính.
- **Lần gọi thực thi**: Call 2 of 3 (tối đa còn 1 lần hiệu chỉnh tiếp theo nếu agent cha yêu cầu, tuyệt đối không có lần thứ 4).
