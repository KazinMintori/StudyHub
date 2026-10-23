# Báo Cáo Thẩm Định Độc Lập — Physics 1 Chapter 11 Theory A (Call 3 of 3)

**Mã phiên làm việc**: `physics1-11-theory-a-20261022`
**Thư mục làm việc cô lập**: `C:\Users\Ai\.codex\worktrees\physics1-11-theory-a-20261022\StudyHub`
**Tài liệu nguồn gốc**: `raw_materials/physics/source/young-freedman-15.pdf` (SHA256: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`)
**Phạm vi nội dung**: Chương 11, các mục 11.1, 11.2, 11.3; trang PDF 357–365 (trang in 337–345).

---

## 1. Sổ Nhật Ký Các Tệp Thuộc Quyền Sở Hữu Độc Quyền (Owned Files Ledger)

| STT | Tệp tin | Trạng thái | Mô tả nội dung |
| :--- | :--- | :--- | :--- |
| 1 | `raw_materials/physics/translations/chapter-11/00-mo-dau.md` | Hoàn thành | Mở đầu chương 11, bối cảnh thực tế cầu máng La Mã Pont du Gard, câu hỏi thách thức, mục tiêu học tập (11.1–11.5). |
| 2 | `raw_materials/physics/translations/chapter-11/01-dieu-kien-can-bang.md` | Hoàn thành | Mục 11.1: Điều kiện cân bằng vật rắn, điều kiện 1 (11.1), điều kiện 2 (11.2), cân bằng tĩnh vs chuyển động tịnh tiến đều, Kiểm tra hiểu biết 11.1. |
| 3 | `raw_materials/physics/translations/chapter-11/02-trong-tam.md` | Hoàn thành | Mục 11.2: Trọng tâm, mômen trọng lực, tọa độ thành phần khối tâm (11.3), vectơ khối tâm (11.4), mômen trọng lực tổng hợp (11.5), chứng minh trọng tâm trùng khối tâm trong trường trọng lực đều, ứng dụng tháp đôi Petronas, Ví dụ 11.1 (tấm ván bắc cầu), quy tắc mặt chân đế, hộp thận trọng chọn điểm quy chiếu, Kiểm tra hiểu biết 11.2. |
| 4 | `raw_materials/physics/translations/chapter-11/03-giai-bai-toan-can-bang-vat-ran.md` | Hoàn thành | Mục 11.3: Phương pháp giải bài toán cân bằng vật rắn, Ví dụ 11.2 (trọng tâm cơ thể người đi bộ), quy ước vẽ lực tiếp xúc tại điểm tiếp xúc (Hộp thận trọng), Ví dụ 11.3 (cái thang dựa tường), kết cấu siêu tĩnh (bàn 4 chân), Ví dụ 11.4 (cẳng tay nâng tạ), Kiểm tra hiểu biết 11.3 (biển quảng cáo treo cáp). |
| 5 | `scripts/prepare-physics1-11-theory-a-assets.py` | Hoàn thành | Script trích xuất ảnh nguyên gốc từ PDF không che viền, `SCALE=3.0`, `alpha=False`, từ điển `CROPS` chứa 12 ảnh. |
| 6 | `docs/.vitepress/physics1-11-theory-a-image-annotations.mjs` | Hoàn thành | Từ điển chú thích nhãn hình ảnh `physics1Chapter11TheoryAImageAnnotations` dịch nhãn tiếng Anh sang tiếng Việt cho 12 ảnh. |
| 7 | `raw_materials/physics/verify_chapter11_theory_a.py` | Hoàn thành | Bộ script kiểm thử độc lập 5/5: Tính toán vật lý, so khớp RGB byte-for-byte với PDF, kiểm tra chú thích, quy chuẩn văn phong và kiểm tra độ rộng toán học. |
| 8 | `raw_materials/physics/reviews/ch11-agy-theory-a-review.md` | Hoàn thành | Báo cáo thẩm định tư nhân và nhật ký số liệu thực tế này. |
| 9–20 | `docs/vat-ly-1/bai-giang/img/young-11/a-*.png` (12 tệp) | Hoàn thành | 12 tệp ảnh trích xuất nguyên bản độ phân giải cao, tiền tố độc quyền `a-`. |

---

## 2. Bản Đồ Bao Phủ Nội Dung Nguồn (Source Unit Coverage Mapping)

| Mục nguồn | Trang PDF | Trang in | Nội dung chi tiết được giảng dạy đầy đủ | Hình ảnh / Công thức gốc |
| :--- | :--- | :--- | :--- | :--- |
| **Chapter 11 Opener** | 357 | 337 | - Mở đầu: Tầm quan trọng của cân bằng tĩnh trong kiến trúc và sinh cơ học.<br>- Cầu máng dẫn nước La Mã Pont du Gard: Khả năng chịu nén của đá khối, lực nén dọc vòm cong truyền tải vào mố trụ.<br>- Câu hỏi thử thách mở đầu: Cơ chế hoạt động của vòm đá Pont du Gard và 4 phương án lựa chọn.<br>- 5 mục tiêu học tập chuẩn hóa của toàn bộ chương 11. | - Ảnh mở đầu: `a-mo-dau.png` (Pont du Gard). |
| **11.1 Conditions for Equilibrium** | 358–359 | 338–339 | - Khái niệm cân bằng: Gia tốc khối tâm bằng không và gia tốc góc bằng không.<br>- Điều kiện 1: $\sum \vec{F} = \vec{0}$ (11.1) — Không có xu hướng tịnh tiến.<br>- Điều kiện 2: $\sum \vec{\tau} = \vec{0}$ (11.2) — Không có xu hướng quay.<br>- Điểm quy chiếu tính mômen: Bất kỳ điểm nào trong không gian khi điều kiện 1 đã thỏa mãn.<br>- Phân biệt cân bằng tĩnh (vật đứng yên) và cân bằng động (chuyển động thẳng đều không quay).<br>- Kiểm tra hiểu biết 11.1: 4 cấu hình lực tác dụng (a, b, c, d), phân tích chi tiết điều kiện 1 và 2. | - Hình 11.1: `a-hinh-11-01.png`<br>- Phương trình (11.1): $\sum \vec{F} = \vec{0}$<br>- Phương trình (11.2): $\sum \vec{\tau} = \vec{0}$ |
| **11.2 Center of Gravity** | 359–362 | 339–342 | - Định nghĩa trọng tâm: Điểm đặt của tổng trọng lực $\vec{w}$ sao cho mômen tổng hợp tương đương.<br>- Chứng minh hình thức: $\tau_{zi} = -x_i w_i \implies \tau_z = -\sum x_i w_i = -x_{\mathrm{cg}} w$.<br>- Hệ phương trình tọa độ khối tâm: (11.3) và phương trình vectơ khối tâm: (11.4).<br>- Biểu thức mômen trọng lực tổng hợp: $\vec{\tau} = \vec{r}_{\mathrm{cm}} \times \vec{w}$ (11.5).<br>- Chứng minh trọng tâm (cg) trùng với khối tâm (cm) khi gia tốc trọng trường $\vec{g}$ đều.<br>- Ứng dụng thực tế: Tháp đôi Petronas (cao 452 m, chênh lệch $g$ là 0,014%, trọng tâm lệch xuống dưới khối tâm khoảng 2 cm).<br>- Phương pháp tìm trọng tâm bằng thực nghiệm treo dây dọi.<br>- Ví dụ 11.1: Cậu bé đi trên tấm ván nhô ra mép vực (đầy đủ Tóm tắt, Hướng đi, Tính toán, Kiểm tra tính nhất quán với gốc tọa độ khác, và phân tích mở rộng khi người lớn 60 kg bước ra).<br>- Hộp khái niệm cốt lõi: Điều kiện ổn định dựa trên diện tích mặt chân đế.<br>- Hộp thận trọng: Tính độc lập của tổng mômen lực đối với điểm quy chiếu.<br>- Kiểm tra hiểu biết 11.2: Cân bằng thước mét gắn hòn đá trên con đội tam giác. | - Hình 11.2: `a-hinh-11-02.png`<br>- Hình 11.3: `a-hinh-11-03.png`<br>- Hình 11.4: `a-hinh-11-04.png`<br>- Hình 11.5: `a-hinh-11-05.png`<br>- Hình 11.6: `a-hinh-11-06.png`<br>- Hình 11.7: `a-hinh-11-07.png`<br>- Phương trình (11.3), (11.4), (11.5) |
| **11.3 Solving Rigid-Body Equilibrium Problems** | 362–365 | 342–345 | - Chiến lược 3 bước giải bài toán cân bằng vật rắn: Chuẩn bị (hệ trục, sơ đồ vật tự do), Thiết lập phương trình ($\sum F_x = 0, \sum F_y = 0, \sum \tau = 0$), Đánh giá kết quả.<br>- Ví dụ 11.2: Xác định trọng tâm cơ thể người đi bộ bằng hai bàn cân (tính $x_{\mathrm{cg}}$, đối chiếu với trục quay bên kia, mở rộng cho tư thế đứng thẳng).<br>- Hộp thận trọng: Vẽ lực tiếp xúc tại đúng điểm tiếp xúc hình học.<br>- Ví dụ 11.3: Cái thang tựa tường thẳng đứng nhẵn (đầy đủ các bước giải, $n_2, n_1, f_s, \mu_s, F_B, \theta_B$, chứng minh lực tiếp xúc không hướng dọc thân thang).<br>- Phân tích kết cấu siêu tĩnh: Bàn 4 chân trên sàn nhà, giới hạn của mô hình vật rắn lý tưởng.<br>- Ví dụ 11.4: Cân bằng cơ học cẳng tay người nâng quả tạ (tính tổng quát theo chữ $T, E_x, E_y$, bản chất giải phẫu cơ nhị đầu và khớp khuỷu tay).<br>- Kiểm tra hiểu biết 11.3: Biển quảng cáo treo dây cáp chéo và bản lề tại $P$, so sánh thứ tự độ lớn $T > w > E_y = 0$. | - Hình 11.8: `a-hinh-11-08.png`<br>- Hình 11.9: `a-hinh-11-09.png`<br>- Hình 11.10: `a-hinh-11-10.png`<br>- Hình 11.11: `a-hinh-11-11.png` |

---

## 3. Sổ Số Liệu Vật Lý & Kiểm Tra Đại Số (Physics & Numerics Verification Ledger)

Tất cả các phép tính số học và giải tích dưới đây đã được lập trình và xác minh độc lập bằng mã nguồn Python `raw_materials/physics/verify_chapter11_theory_a.py`:

### Ví dụ 11.1 (Đi trên tấm ván bắc cầu)
- **Dữ liệu đầu vào**: Khối lượng tấm ván $M = 90{,}0\,\text{kg}$, chiều dài ván $L = 6{,}0\,\text{m}$, khoảng cách giữa hai giá đỡ $D = 1{,}5\,\text{m}$.
- **Khoảng cách nhô ra ngoài**: $L - D = 4{,}5\,\text{m}$.
- **Trọng tâm tấm ván tính từ giá đỡ bên trái**: $L/2 = 3{,}0\,\text{m}$.
- **Cánh tay đòn trọng lực ván quanh giá đỡ bên phải**: $x_P = L/2 - D = 3{,}0 - 1{,}5 = 1{,}5\,\text{m}$.
- **Cánh tay đòn trọng lực cậu bé quanh giá đỡ bên phải**: $x_T = (L - D)/2 = 4{,}5/2 = 2{,}25\,\text{m}$.
- **Cân bằng mômen quanh giá đỡ bên phải (khi giá đỡ bên trái bắt đầu nhấc lên, $n_1 = 0$)**:
  $$M g (D/2) = m g \frac{L - D}{2} \implies m = M \frac{D}{L - D}$$
- **Kết quả tính**: $m = 90{,}0 \times \frac{1{,}5}{4{,}5} = 30{,}0\,\text{kg}$.
- **Kiểm tra tính nhất quán với gốc tọa độ đặt tại giá đỡ bên phải**:
  $$x_{\mathrm{cg}} = \frac{-M (D/2) + m (L - D)/2}{M + m} = 0 \implies m = 30{,}0\,\text{kg}$$
- **Mở rộng người lớn $m_{\mathrm{adult}} = 60{,}0\,\text{kg}$**:
  $$x_{\max} = \frac{M (D/2)}{m_{\mathrm{adult}}} = \frac{90{,}0 \times 0{,}75}{60{,}0} = 1{,}125\,\text{m}$$
  (Chỉ đi được một nửa quãng đường của phần ván nhô ra).

### Ví dụ 11.2 (Xác định trọng tâm cơ thể người đi bộ)
- **Dữ liệu đầu vào**: Số đọc cân bên trái $w_1 = 380\,\text{N}$, số đọc cân bên phải $w_2 = 320\,\text{N}$, chiều dài ván $L = 2{,}00\,\text{m}$.
- **Tổng trọng lượng**: $w = w_1 + w_2 = 380 + 320 = 700\,\text{N}$.
- **Khoảng cách trọng tâm tính từ cân bên trái**:
  $$x = \frac{w_2 L}{w} = \frac{320 \times 2{,}00}{700} = 0{,}9142857\,\text{m} \approx 0{,}914\,\text{m}$$
- **Khoảng cách trọng tâm tính từ cân bên phải (trục quay thay thế)**:
  $$x' = \frac{w_1 L}{w} = \frac{380 \times 2{,}00}{700} = 1{,}085714\,\text{m} \approx 1{,}09\,\text{m}$$
  Xác minh: $x + x' = 0{,}9142857 + 1{,}085714 = 2{,}000000\,\text{m} = L$.
- **Người đứng thẳng**: Chiều cao $h = 1{,}80\,\text{m}$, khoảng cách từ trục khớp đến đỉnh đầu $L_{\mathrm{pivot}} = 1{,}53\,\text{m}$.
  Trọng tâm trên trục khớp: $0{,}660 \times 1{,}53\,\text{m} = 1{,}0098\,\text{m} \approx 1{,}01\,\text{m}$.
  Tỷ lệ chiều cao: $1{,}0098 / 1{,}80 = 0{,}561 = 56{,}1\%$.

### Ứng dụng tháp đôi Petronas
- **Chiều cao**: $h = 452\,\text{m}$, bán kính Trái Đất $R_E = 6{,}37 \times 10^6\,\text{m}$.
- **Chênh lệch gia tốc trọng trường**:
  $$\frac{\Delta g}{g} \approx \frac{2 h}{R_E} = \frac{2 \times 452}{6{,}37 \times 10^6} = 1{,}419 \times 10^{-4} = 0{,}014\%$$
- **Độ lệch trọng tâm so với khối tâm**: Trọng tâm nằm thấp hơn khối tâm khoảng $2\,\text{cm}$ ($0{,}02\,\text{m}$).

### Ví dụ 11.3 (Chiếc thang tựa tường có bị trượt không?)
- **Dữ liệu đầu vào**: Chiều dài thang $L = 5{,}0\,\text{m}$, chân thang cách tường $d = 3{,}0\,\text{m}$, trọng lượng thang $w_l = 180\,\text{N}$ tại trung điểm thang, trọng lượng người $w_p = 800\,\text{N}$ tại vị trí $1/3$ từ đỉnh thang.
- **Chiều cao đầu thang tựa tường**: $h = \sqrt{L^2 - d^2} = \sqrt{5{,}0^2 - 3{,}0^2} = 4{,}0\,\text{m}$.
- **Cánh tay đòn trọng lượng thang quanh chân thang**: $d/2 = 1{,}5\,\text{m}$.
- **Cánh tay đòn trọng lượng người quanh chân thang**: $d/3 = 1{,}0\,\text{m}$.
- **Cân bằng lực thẳng đứng**: $n_2 - w_l - w_p = 0 \implies n_2 = 180 + 800 = 980\,\text{N}$.
- **Cân bằng mômen quanh chân thang $B$**:
  $$4{,}0 n_1 - (180 \times 1{,}5) - (800 \times 1{,}0) = 0 \implies 4{,}0 n_1 = 270 + 800 = 1070\,\text{N}\cdot\text{m}$$
  $$n_1 = \frac{1070}{4{,}0} = 267{,}5\,\text{N} \approx 268\,\text{N}$$
- **Cân bằng lực nằm ngang**: $f_s - n_1 = 0 \implies f_s = 267{,}5\,\text{N} \approx 268\,\text{N}$.
- **Hệ số ma sát nghỉ tối thiểu để không bị trượt**:
  $$\mu_s \ge \frac{f_s}{n_2} = \frac{267{,}5}{980} \approx 0{,}272959 \approx 0{,}27$$
- **Độ lớn lực tiếp xúc tại chân thang**:
  $$F_B = \sqrt{f_s^2 + n_2^2} = \sqrt{267{,}5^2 + 980^2} = \sqrt{71556{,}25 + 960400} \approx 1015{,}93\,\text{N} \approx 1020\,\text{N}$$
- **Góc nghiêng của lực tiếp xúc chân thang**:
  $$\theta_B = \arctan\left(\frac{n_2}{f_s}\right) = \arctan\left(\frac{980}{267{,}5}\right) \approx 74{,}72^\circ \approx 75^\circ$$
- **Góc nghiêng của thân thang**:
  $$\theta_{\mathrm{thang}} = \arctan\left(\frac{4{,}0}{3{,}0}\right) \approx 53{,}13^\circ$$
  Xác minh: $\theta_B = 75^\circ \ne \theta_{\mathrm{thang}} = 53{,}1^\circ$, lực tiếp xúc không hướng dọc thân thang.

### Ví dụ 11.4 (Cân bằng cơ học khi tập tạ tay)
- **Phương trình mômen quanh khớp khuỷu tay $O$**:
  $$\tau_O = (T \sin\theta) D - w L = 0 \implies T = \frac{w L}{D \sin\theta}$$
- **Phương trình cân bằng phương ngang**:
  $$E_x + T \cos\theta = 0 \implies E_x = -T \cos\theta = -\frac{w L}{D \tan\theta}$$
- **Phương trình cân bằng phương thẳng đứng**:
  $$E_y + T \sin\theta - w = 0 \implies E_y = w - T \sin\theta = w - \frac{w L}{D} = -w \left(\frac{L - D}{D}\right)$$
  (Dấu âm chỉ rõ $E_y$ hướng thẳng đứng xuống dưới vì $L > D$).

### Kiểm tra hiểu biết (Test Your Understanding)
- **TYU 11.1**: Hai lực tác dụng lên một vật. Điều kiện cân bằng tĩnh đòi hỏi $\sum \vec{F} = \vec{0}$ và $\sum \vec{\tau} = \vec{0}$, tức là hai lực phải cùng độ lớn, ngược chiều và cùng nằm trên một đường tác dụng $\implies$ **Phương án (a)**.
- **TYU 11.2**: Thước mét dài $1{,}00\,\text{m}$ khối lượng $m$, hòn đá khối lượng $m$ ở đầu trái $x = 0$. Khối tâm thước ở $x = 0{,}50\,\text{m}$.
  $$x_{\mathrm{cg}} = \frac{m(0) + m(0{,}50\,\text{m})}{2m} = 0{,}25\,\text{m} \implies \text{\textbf{Phương án (ii)}: Bằng } 0{,}25\,\text{m}$$
- **TYU 11.3**: Biển quảng cáo treo ở đầu thanh dài $L$, cáp nối tại đầu mút ($D = L$).
  $$T = \frac{w}{\sin\theta} > w \quad (\text{vì } 0 < \theta < 90^\circ \implies \sin\theta < 1)$$
  $$E_y = -w \left(\frac{L - L}{L}\right) = 0$$
  Thứ tự độ lớn: $T > w > E_y = 0 \implies$ **Thứ tự (ii), (i), (iii)**.

---

## 4. Nhật Ký Trích Xuất Ảnh & So Khớp Byte-for-Byte RGB

Tất cả 12 hình ảnh được trích xuất từ `raw_materials/physics/source/young-freedman-15.pdf` bằng PyMuPDF tại `SCALE = 3.0`, `alpha=False` và lưu trữ dưới tiền tố độc quyền `a-`:

| Tên ảnh | Trang PDF | Tọa độ cắt gốc $(x_0, y_0, x_1, y_1)$ (pt) | Kích thước xuất (px) | Khoảng trắng mép lớn nhất (px) | Kết quả so khớp RGB với PDF |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `a-mo-dau.png` | 357 | `(0.0, 0.0, 438.5, 245.5)` | $1316 \times 737$ | 0 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-01.png` | 358 | `(35.0, 105.0, 195.0, 508.0)` | $480 \times 1209$ | 6 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-02.png` | 359 | `(455.0, 323.0, 612.0, 547.0)` | $471 \times 672$ | 5 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-03.png` | 360 | `(35.0, 128.0, 193.0, 238.5)` | $474 \times 332$ | 4 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-04.png` | 360 | `(35.0, 328.0, 184.0, 533.0)` | $447 \times 615$ | 6 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-05.png` | 360 | `(235.0, 610.0, 541.0, 742.0)` | $918 \times 396$ | 8 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-06.png` | 361 | `(134.0, 308.0, 281.0, 405.0)` | $441 \times 291$ | 5 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-07.png` | 361 | `(455.0, 451.0, 611.0, 489.0)` | $468 \times 114$ | 4 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-08.png` | 362 | `(46.0, 505.0, 283.0, 724.0)` | $711 \times 657$ | 7 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-09.png` | 363 | `(97.0, 579.0, 591.0, 723.0)` | $1482 \times 432$ | 8 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-10.png` | 364 | `(35.0, 510.0, 485.0, 712.0)` | $1350 \times 606$ | 9 px | Trùng khớp 100% byte-for-byte |
| `a-hinh-11-11.png` | 365 | `(452.0, 97.0, 611.0, 221.0)` | $477 \times 372$ | 6 px | Trùng khớp 100% byte-for-byte |

- **Toàn bộ 12 ảnh**: Khoảng trắng mép ngoài đều $\le 9\,\text{px}$, vượt trội so với ngưỡng tối đa cho phép $24\,\text{px}$.
- **Độ trung thực RGB**: 100% mẫu pixel byte-for-byte trùng khớp tuyệt đối giữa ảnh lưu đĩa và vùng render trực tiếp từ PDF nguồn.

---

## 5. Thẩm Định Từ Điển Chú Thích Nhãn Ảnh (`physics1-11-theory-a-image-annotations.mjs`)

- **Tệp xuất**: `docs/.vitepress/physics1-11-theory-a-image-annotations.mjs`
- **Hằng số xuất**: `physics1Chapter11TheoryAImageAnnotations`
- **Số lượng hình ảnh có chú thích**: 12 hình (khớp 100% với danh mục ảnh trích xuất).
- **Tổng số cặp nhãn thuật ngữ dịch**: 30 cặp `[Tiếng Việt, Tiếng Anh]`.
- **Kiểm tra tính hợp lệ**:
  - Không có bất kỳ cặp nhãn nào bị trùng lặp nguyên văn (không có `conductor (conductor)`).
  - Không có nhãn tiếng Anh nào bị lặp lại bên trong cùng một hình.
  - Các ký tự đặc biệt được dịch chính xác theo đúng ngữ cảnh sơ đồ vật lý học thuật.

---

## 6. Thẩm Định Cú Pháp Toán Học & Văn Phong Tiếng Việt

- **Công cụ đo đạc**: `qa/physics1-priority/measure-math.mjs`
- **Số lượng công thức hiển thị (display math `$$...$$`)**: 90 công thức.
  - Chiều rộng tối đa: $\le 25{,}0\,\text{ex}$ (đạt chuẩn hiển thị trên thiết bị di động hẹp).
- **Số lượng công thức nội dòng (inline math `$...$`)**: 242 công thức.
  - Chiều rộng tối đa: $\le 27{,}0\,\text{ex}$.
- **Tổng số lỗi vi phạm độ rộng (findings)**: **0 lỗi** (`status: passed`).
- **Quy tắc dấu hai chấm (`:`)**: Kiểm tra tự động 100% dòng văn xuôi, tiêu đề mục, danh sách và chú thích hình ảnh — không có bất kỳ chữ cái thường nào xuất hiện ngay sau dấu hai chấm.
- **Rà soát từ ngữ cấm (Forbidden Phrases)**: Không xuất hiện bất kỳ cụm từ trích dẫn thụ động nào kiểu *“theo sách”, “giáo trình gốc”, “bản dịch”, “ảnh nguyên gốc”, “hình trong sách”, “sách dùng”, “nguyên tác”*.
- **Hệ thống nhãn phương trình**: Đầy đủ các phương trình chuẩn hóa có nhãn `\tag{11.1}`, `\tag{11.2}`, `\tag{11.3}`, `\tag{11.4}`, `\tag{11.5}`.

---

## 7. Nhật Ký Lệnh Kiểm Thử & Mã Thoát (Commands & Exits Ledger)

| Lệnh thực thi | Mục đích | Mã thoát (Exit code) | Kết quả ghi nhận |
| :--- | :--- | :--- | :--- |
| `C:/Users/Ai/miniconda3/python.exe -X utf8 scripts/prepare-physics1-11-theory-a-assets.py` | Tạo toàn bộ 12 ảnh trích xuất PNG | `0` | 12/12 ảnh được lưu với kích thước pixel chuẩn xác. |
| `node --input-type=module -e "import('./docs/.vitepress/physics1-11-theory-a-image-annotations.mjs').then(m=>console.log(Object.keys(m)))"` | Kiểm tra cú pháp ES Module của tệp chú thích | `0` | Export hợp lệ `physics1Chapter11TheoryAImageAnnotations`. |
| `node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . raw_materials/physics/translations/chapter-11/00-mo-dau.md raw_materials/physics/translations/chapter-11/01-dieu-kien-can-bang.md raw_materials/physics/translations/chapter-11/02-trong-tam.md raw_materials/physics/translations/chapter-11/03-giai-bai-toan-can-bang-vat-ran.md` | Đo đạc độ rộng công thức MathJax | `0` | `passed`, 90 display, 242 inline, 0 findings. |
| `C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter11_theory_a.py` | Chạy bộ kiểm thử toàn diện 5 thành phần | `0` | `ALL VERIFICATIONS PASSED CLEANLY (5/5)`. |

---

## 8. Tuyên Bố Trung Thực Về Tính Hoàn Tất & Giới Hạn Phạm Vi

1. **Tính hoàn tất của phạm vi giao phó**:
   - Toàn bộ nội dung lý thuyết, mục tiêu học tập, câu hỏi thử thách mở đầu, định nghĩa, chứng minh hình thức, ứng dụng thực tế, Ví dụ 11.1–11.4 và Kiểm tra hiểu biết 11.1–11.3 trong các mục 11.1, 11.2, 11.3 (trang PDF 357–365) đã được biên soạn và giảng dạy độc lập, đầy đủ, không cắt xén, không thay thế đề bài.
   - Toàn bộ 8 tệp thuộc quyền sở hữu độc quyền đã hoàn thành và lưu trữ trên đĩa.
   - Không có thay đổi nào được thực hiện ra ngoài các đường dẫn sở hữu độc quyền.
2. **Giới hạn trách nhiệm sư phạm**:
   - Báo cáo này không đưa ra tuyên bố tự chứng nhận 100% về giao diện trình duyệt (không có browser QA self-certification). Toàn bộ khâu kiểm tra giao diện trực quan trên trình duyệt (browser view) và tích hợp hệ thống do parent agent và quy trình CI trên đám mây của StudyHub đảm nhiệm.
   - Không thực hiện bất kỳ lệnh git commit, push, deploy, build toàn cục (`npm run ci:build`) hay cài đặt gói phần mềm nào theo đúng các ràng buộc nghiêm ngặt của dự án.
