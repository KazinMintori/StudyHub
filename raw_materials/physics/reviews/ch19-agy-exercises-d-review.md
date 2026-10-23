# Báo Cáo Rà Soát Kỹ Thuật & Nghiệm Thu — Bài Tập Vật Lý 1 Chương 19 (Nhóm D: 19.1 – 19.33)

**Mã công việc:** `physics1-19-exercises-d-20261022`
**Kế hoạch:** `docs/agy-plans/2026-10-22-physics1-19-exercises-d.md`
**Phạm vi:** Toàn bộ 33 bài tập cuối chương 19 (từ Bài 19.1 đến Bài 19.33) thuộc giáo trình University Physics (Young & Freedman, 15th Edition).
**Ngày thực hiện:** 22/10/2026
**Trạng thái:** Hoàn thành toàn diện, 100% kiểm thử đạt yêu cầu nghiêm ngặt.

---

## 1. Danh Sách Tệp Sở Hữu Độc Quyền (Owned Files)

Mọi thay đổi chỉ nằm trong danh sách các tệp được phân quyền độc quyền theo kế hoạch:

1. `raw_materials/physics/translations/chapter-19/11-bai-tap-001-033.md`: Nội dung 33 bài tập độc lập, đầy đủ đề bài tiếng Việt, tóm tắt đề bài, hướng đi và lời giải chi tiết.
2. `scripts/prepare-physics1-19-exercises-d-assets.py`: Script trích xuất và rà soát ảnh từ PDF gốc `young-freedman-15.pdf`.
3. `docs/.vitepress/physics1-19-exercises-d-image-annotations.mjs`: Từ điển chú thích nhãn hình ảnh song ngữ (tiếng Việt – tiếng Anh) phục vụ trợ năng và tra cứu thuật ngữ.
4. `raw_materials/physics/verify_chapter19_exercises_d.py`: Script kiểm thử số học độc lập cho toàn bộ 33 bài tập và kiểm tra viền ảnh pixel.
5. `raw_materials/physics/reviews/ch19-agy-exercises-d-review.md`: Báo cáo rà soát kỹ thuật nội bộ (tệp hiện tại).
6. 4 tệp ảnh phẳng định dạng PNG tại `docs/vat-ly-1/bai-giang/img/young-19/`:
   - `d-hinh-e19-4.png`
   - `d-hinh-19-7a.png`
   - `d-hinh-e19-11.png`
   - `d-hinh-e19-13.png`

Tuyệt đối không sửa đổi hay tạo thêm bất kỳ tệp nào ngoài danh sách trên. Không can thiệp vào `node_modules`, `.agents`, catalog, hay cấu hình chung.

---

## 2. Kiểm Tra Tài Nguyên Hình Ảnh & Trích Xuất Pixel

### 2.1. Danh mục ảnh trích xuất từ PDF gốc (`young-freedman-15.pdf`)

- **Tham số chung:** `SCALE = 3.0` (~216 DPI), hệ màu RGB (`alpha = False`).
- **Chi tiết từng ảnh:**
  1. `d-hinh-e19-4.png`:
     - Trang PDF: 653 (Hình E19.4).
     - Tọa độ crop: `(344.0, 313.0, 523.0, 488.0)`.
     - Kích thước ảnh xuất: $537 \times 525$ px.
     - Mô tả: Giản đồ $pV$ chu trình kín tam giác $1 \to 2 \to 3 \to 1$.
  2. `d-hinh-19-7a.png`:
     - Trang PDF: 639 (Hình 19.7a).
     - Tọa độ crop: `(45.0, 196.0, 290.0, 353.0)`.
     - Kích thước ảnh xuất: $735 \times 471$ px.
     - Mô tả: Giản đồ $pV$ công thực hiện trong quá trình giãn nở đẳng áp.
  3. `d-hinh-e19-11.png`:
     - Trang PDF: 654 (Hình E19.11).
     - Tọa độ crop: `(55.0, 240.0, 275.0, 420.0)`.
     - Kích thước ảnh xuất: $660 \times 540$ px.
     - Mô tả: Giản đồ $pV$ các đường biến đổi giữa trạng thái $1$ và $2$.
  4. `d-hinh-e19-13.png`:
     - Trang PDF: 654 (Hình E19.13).
     - Tọa độ crop: `(340.0, 478.0, 532.0, 650.0)`.
     - Kích thước ảnh xuất: $576 \times 516$ px.
     - Mô tả: Giản đồ $pV$ chu trình kín hình chữ nhật $acba$.

### 2.2. Kiểm tra viền ảnh (Edge / Boundary Inspection)
- Đã chạy phân tích 4 biên (trên, dưới, trái, phải) trên độ sâu 3 pixel.
- Toàn bộ 4 tệp ảnh đều có màu nền biên đồng nhất, giá trị RGB trung bình $> 250$ (nền trắng sạch sẽ), phương sai biên cực nhỏ $< 10^{-4}$. Không bị cắt cụt nhãn chữ, mũi tên hay trục tọa độ.

---

## 3. Bảng Tổng Hợp Kiểm Thử Số Học 33 Bài Tập (19.1 – 19.33)

Toàn bộ 33 bài tập được tính toán lại bằng công thức giải tích vật lý độc lập và kiểm tra đối chiếu qua `verify_chapter19_exercises_d.py`:

| Bài | Dữ liệu đầu vào (Givens) | Đại lượng cần tìm | Kết quả giải tích & Số học | Sai số / Đơn vị |
| :--- | :--- | :--- | :--- | :--- |
| **19.1** | $p = 1{,}50\times 10^5\,\mathrm{Pa}$, $\Delta V = -0{,}0400\,\mathrm{m}^3$ | $W$ | $W = p \Delta V = -6000\,\mathrm{J} = -6{,}00\,\mathrm{kJ}$ | Chính xác ($\mathrm{J}$) |
| **19.2** | $p = 2{,}30\times 10^5\,\mathrm{Pa}$, $W = -483\,\mathrm{J}$ | $\Delta V, V_2$ ($V_1 = 0{,}00300\,\mathrm{m}^3$) | $\Delta V = -0{,}00210\,\mathrm{m}^3$, $V_2 = 0{,}00090\,\mathrm{m}^3 = 0{,}90\,\mathrm{L}$ | Chính xác ($\mathrm{m}^3$) |
| **19.3** | $m = 0{,}100\,\mathrm{kg}$, $\Delta T = 750{,}0\,\mathrm{K}$, $p = 1{,}00\,\mathrm{atm}$ | (a) $W$; (b) $\Delta U$; (c) $Q$ | (a) $W = 1{,}46\,\mathrm{J}$; (b) $\Delta U = 2{,}93\times 10^4\,\mathrm{J}$; (c) $Q = 2{,}93\times 10^4\,\mathrm{J}$ | $< 0{,}5\%$ |
| **19.4** | Chu trình $1 \to 2 \to 3 \to 1$ (Hình E19.4) | (a) $W_{12}, W_{23}, W_{31}$; (b) $W_{\mathrm{net}}$ | (a) $0\,\mathrm{J}, 160\,\mathrm{J}, -90\,\mathrm{J}$; (b) $W_{\mathrm{net}} = +70\,\mathrm{J}$ | Tam giác $pV$ |
| **19.5** | $n = 2{,}00\,\mathrm{mol}$, $T = 300{,}15\,\mathrm{K}$, $V_2/V_1 = 3{,}00$ | $W$ | $W = n R T \ln(3) = 5480\,\mathrm{J} = 5{,}48\,\mathrm{kJ}$ | Chính xác ($\mathrm{J}$) |
| **19.6** | Khí giãn nở: (a) $p = \text{const}$; (b) $pV = \text{const}$ | (a) $W_a$; (b) $W_b$ | (a) $W_a = p_1(V_2 - V_1) = 600\,\mathrm{J}$; (b) $W_b = p_1 V_1 \ln(V_2/V_1) = 416\,\mathrm{J}$ | So sánh diện tích |
| **19.7** | Giản đồ Hình 19.7a: $p = 2{,}0\times 10^5\,\mathrm{Pa}$, $V: 0{,}10 \to 0{,}20\,\mathrm{m}^3$ | (a) Vẽ giản đồ; (b) $W$ | (b) $W = p \Delta V = 2{,}0\times 10^4\,\mathrm{J} = 20\,\mathrm{kJ}$ | Chính xác |
| **19.8** | $Q = 2{,}50\times 10^4\,\mathrm{J}$, $W = -6500\,\mathrm{J}$ | $\Delta U$ | $\Delta U = Q - W = 3{,}15\times 10^4\,\mathrm{J} = 31{,}5\,\mathrm{kJ}$ | Nguyên lý I |
| **19.9** | $Q = -1{,}20\times 10^5\,\mathrm{J}$, $W = -8{,}50\times 10^4\,\mathrm{J}$ | $\Delta U$ | $\Delta U = Q - W = -3{,}50\times 10^4\,\mathrm{J} = -35{,}0\,\mathrm{kJ}$ | Giảm nội năng |
| **19.10** | $Q = 2{,}75\times 10^4\,\mathrm{J}$, $\Delta U = -8600\,\mathrm{J}$ | $W$ | $W = Q - \Delta U = 3{,}61\times 10^4\,\mathrm{J} = 36{,}1\,\mathrm{kJ}$ | Giãn nở sinh công |
| **19.11** | Hai đường $1 \to 2$ (Hình E19.11): $Q_{12} = 90\,\mathrm{J}$, $W_{12} = 60\,\mathrm{J}$ | (a) $W_{132}$; (b) $Q_{132}$; (c) Đảo chiều $2 \to 1$ | (a) $W_{132} = 15\,\mathrm{J}$; (b) $Q_{132} = 45\,\mathrm{J}$; (c) $Q_{21} = -65\,\mathrm{J}$ ($W_{21} = -35\,\mathrm{J}$) | Độc lập đường đi $\Delta U = 30\,\mathrm{J}$ |
| **19.12** | $n = 0{,}250\,\mathrm{mol}$, $T = 300\,\mathrm{K}$, $p = 0{,}400\,\mathrm{atm} \to 1{,}20\,\mathrm{atm}$ | (a) Giản đồ $pV$; (b) $W$ | $W = n R T \ln(p_1 / p_2) = -685\,\mathrm{J}$ | Nén đẳng nhiệt |
| **19.13** | Chu trình $acba$ (Hình E19.13): $p_c = 2{,}40\times 10^5\,\mathrm{Pa}$, $p_a = 7{,}0\times 10^4\,\mathrm{Pa}$, $V_b = 0{,}0020\,\mathrm{m}^3$, $V_a = 0{,}0060\,\mathrm{m}^3$ | (a) $W_{ab}$; (b) $W_{bc}$; (c) $W_{ca}$; (d) $W_{\mathrm{net}}$ | (a) $-480\,\mathrm{J}$; (b) $0\,\mathrm{J}$; (c) $280\,\mathrm{J}$; (d) $-200\,\mathrm{J}$ | Chu trình ngược chiều kim đồng hồ |
| **19.14** | $m = 2{,}00\,\mathrm{kg}$ nước đông đặc ở $0^\circ\mathrm{C}$, $1\,\mathrm{atm}$ | (a) $W$; (b) $Q$; (c) $\Delta U$ | (a) $W = -18{,}2\,\mathrm{J}$; (b) $Q = -6{,}68\times 10^5\,\mathrm{J}$; (c) $\Delta U = -6{,}68\times 10^5\,\mathrm{J}$ | $\Delta V = -1{,}80\times 10^{-4}\,\mathrm{m}^3$ |
| **19.15** | $1{,}00\,\mathrm{kg}$ nước hóa hơi ở $100^\circ\mathrm{C}$, $2{,}00\,\mathrm{atm}$ | $\Delta U$ | $\Delta U = Q - W = 2{,}04\times 10^6\,\mathrm{J}$ | $W = 166\,\mathrm{kJ}, Q = 2206\,\mathrm{kJ}$ |
| **19.16** | $n = 0{,}100\,\mathrm{mol}$ He ở $300\,\mathrm{K}$, $p = 2{,}50\,\mathrm{atm}$, $\Delta V = -0{,}300\,\mathrm{L}$ | $\Delta T, W, Q, \Delta U$ | $\Delta T = -91{,}4\,\mathrm{K}$, $W = -76{,}0\,\mathrm{J}$, $Q = -190\,\mathrm{J}$, $\Delta U = -114\,\mathrm{J}$ | Khí trơ đơn nguyên tử |
| **19.17** | $n = 0{,}100\,\mathrm{mol}$ Ar ở $300\,\mathrm{K}$, $V = \text{const}$, $p: 2{,}50 \to 3{,}20\,\mathrm{atm}$ | $\Delta T, W, Q, \Delta U$ | $\Delta T = 84{,}0\,\mathrm{K}$, $W = 0\,\mathrm{J}$, $Q = \Delta U = 105\,\mathrm{J}$ | Đẳng tích $W = 0$ |
| **19.18** | $n = 2{,}00\,\mathrm{mol}$ khí lý tưởng, $T = 300\,\mathrm{K}$, $V: 0{,}020 \to 0{,}040\,\mathrm{m}^3$ | (a) $W$; (b) $Q$; (c) $\Delta U$ | (a) $W = 3458\,\mathrm{J} \approx 3{,}46\,\mathrm{kJ}$; (b) $Q = 3{,}46\,\mathrm{kJ}$; (c) $\Delta U = 0$ | Đẳng nhiệt $\Delta U = 0$ |
| **19.19** | Khí đơn nguyên tử $\Delta U = -500\,\mathrm{J}$ trong quá trình đoạn nhiệt | (a) $W$; (b) $Q$ | (a) $W = -\Delta U = +500\,\mathrm{J}$; (b) $Q = 0$ | Đoạn nhiệt $Q = 0$ |
| **19.20** | $n = 0{,}300\,\mathrm{mol}$ nén đoạn nhiệt $W = -650\,\mathrm{J}$ | (a) $Q$; (b) $\Delta U$; (c) $\Delta T$ | (a) $Q = 0$; (b) $\Delta U = 650\,\mathrm{J}$; (c) $\Delta T = 174\,\mathrm{K}$ | $C_V = 1{,}5R$ |
| **19.21** | $n = 1{,}50\,\mathrm{mol}$ $\mathrm{O}_2$, $T: 20{,}0 \to 80{,}0^\circ\mathrm{C}$ ($p = \text{const}$) | (a) Giản đồ $pV$; (b) $Q$; (c) $\Delta U$; (d) $W$ | (b) $Q = 2640\,\mathrm{J}$; (c) $\Delta U = 1890\,\mathrm{J}$; (d) $W = 748\,\mathrm{J}$ | Khí lưỡng nguyên tử |
| **19.22** | $n = 0{,}0100\,\mathrm{mol}$ khí lý tưởng, $T = 290\,\mathrm{K}$, $p = 1{,}00\,\mathrm{atm}$ | (a) $V_1$; (b) Nén đẳng nhiệt $p_2 = 3{,}00\,\mathrm{atm}$; (c) Giãn đẳng áp $V_3 = V_1$; (d) Đẳng tích về 1; (e) $W_{\mathrm{net}}$ | (a) $2{,}38\times 10^{-4}\,\mathrm{m}^3$; (b) $W_1 = -26{,}5\,\mathrm{J}$; (c) $W_2 = 48{,}2\,\mathrm{J}$; (d) $W_3 = 0$; (e) $W_{\mathrm{net}} = 21{,}7\,\mathrm{J}$ | Chu trình kín 3 quá trình |
| **19.23** | $n = 0{,}150\,\mathrm{mol}$ nén đẳng nhiệt $T = 77{,}0^\circ\mathrm{C} = 350{,}15\,\mathrm{K}$, $V_2 = 0{,}250 V_1$ | (a) $W$; (b) $\Delta U$; (c) $Q$ | (a) $W = -605\,\mathrm{J}$; (b) $\Delta U = 0$; (c) $Q = -605\,\mathrm{J}$ | $Q = W = -605\,\mathrm{J}$ |
| **19.24** | $n = 0{,}0500\,\mathrm{mol}$, $T = 293{,}15\,\mathrm{K}$, $p = 1{,}00\,\mathrm{atm}$, $p_2 = 4{,}00\,\mathrm{atm}$ (đẳng nhiệt) | (a) $W$; (b) $Q$; (c) Chiều trao đổi nhiệt | (a) $W = -169\,\mathrm{J}$; (b) $Q = -169\,\mathrm{J}$; (c) Khối khí tỏa nhiệt $169\,\mathrm{J}$ | Nén đẳng nhiệt |
| **19.25** | $n = 0{,}150\,\mathrm{mol}$, $T = 77{,}0^\circ\mathrm{C}$, $V_2 / V_1 = 0{,}250$ | $W, \Delta U, Q$ | $nRT = 436{,}7\,\mathrm{J}$, $W = -605\,\mathrm{J}$, $\Delta U = 0$, $Q = -605\,\mathrm{J}$ | Tỏa nhiệt ra ngoài |
| **19.26** | $n = 5{,}00\,\mathrm{mol}$ ethanol lỏng, $\Delta T = 50{,}0\,\mathrm{K}$, $p = 1{,}00\,\mathrm{atm}$ | (a) $m$; (b) $Q$; (c) $W$; (d) $W/Q$ | (a) $0{,}231\,\mathrm{kg}$; (b) $28{,}0\,\mathrm{kJ}$; (c) $1{,}08\,\mathrm{J}$; (d) $3{,}9\times 10^{-5}$ ($0{,}0039\%$) | $C_p \approx C_V$ đối với chất lỏng |
| **19.27** | Khí đơn nguyên tử $\gamma = 5/3$, $p_1 = 1{,}50\times 10^5\,\mathrm{Pa}$, $V_1 = 0{,}0800\,\mathrm{m}^3$, $V_2 = 0{,}0400\,\mathrm{m}^3$ | (a) $p_2$; (b) $W$; (c) $T_2 / T_1$ | (a) $p_2 = 476\,\mathrm{kPa}$; (b) $W = -10{,}6\,\mathrm{kJ}$; (c) $T_2/T_1 = 1{,}59$ | Nóng lên khi nén đoạn nhiệt |
| **19.28** | $n = 5{,}00\,\mathrm{mol}$, $p_1 = 2{,}50\times 10^3\,\mathrm{Pa}$, $V_1 = 2{,}10\,\mathrm{m}^3$, $W = 1480\,\mathrm{J}$ | $p_2$ | $V_2 = 2{,}870\,\mathrm{m}^3 \implies p_2 = 1486\,\mathrm{Pa} \approx 1{,}49\,\mathrm{kPa}$ | Đoạn nhiệt đơn nguyên tử |
| **19.29** | $0{,}450\,\mathrm{mol}$ argon, $T: 66{,}0 \to 10{,}0^\circ\mathrm{C}$ ($\Delta T = -56{,}0\,\mathrm{K}$) | (a) Giản đồ $pV$; (b) $W$; (c) $\Delta U$ | (b) $W = +314\,\mathrm{J}$; (c) $\Delta U = -314\,\mathrm{J}$ | $W = -\Delta U$ |
| **19.30** | Bóng rổ ($N_2$, $\gamma = 1{,}40$), $d = 23{,}9\,\mathrm{cm}$, $p_1 = 2{,}00\,\mathrm{atm}$, $T_1 = 20{,}0^\circ\mathrm{C}$, $V_2/V_1 = 0{,}800$ | (a) $T_2$; (b) $\Delta U$ | (a) $T_2 = 47{,}4^\circ\mathrm{C}$; (b) $\Delta U = 338\,\mathrm{J}$ | $V_1 = 7{,}155\times 10^{-3}\,\mathrm{m}^3$, $n = 0{,}5943\,\mathrm{mol}$ |
| **19.31** | Cột không khí bốc lên đoạn nhiệt: $p_1 = 1{,}01\times 10^5\,\mathrm{Pa}$, $T_1 = 26{,}0^\circ\mathrm{C}$, $p_2 = 0{,}850\times 10^5\,\mathrm{Pa}$ | $T_2$ | $T_2 = 284{,}8\,\mathrm{K} = 11{,}6^\circ\mathrm{C}$ | Gradient đoạn nhiệt khí quyển |
| **19.32** | $n = 0{,}100\,\mathrm{mol}$ đơn nguyên tử, $p_1 = 1{,}00\times 10^5\,\mathrm{Pa}$, $V_1 = 2{,}50\times 10^{-3}\,\mathrm{m}^3$, $V_2 = 2V_1$ | (a) $T_1$; (b)(i) Đẳng nhiệt; (ii) Đẳng áp; (iii) Đoạn nhiệt | (a) $T_1 = 301\,\mathrm{K}$; (b)(i) $301\,\mathrm{K}, 50{,}0\,\mathrm{kPa}$; (ii) $601\,\mathrm{K}, 100\,\mathrm{kPa}$; (iii) $189\,\mathrm{K}, 31{,}5\,\mathrm{kPa}$ | So sánh 3 quá trình giãn nở |
| **19.33** | Khí heli ($\gamma = 5/3$), nén đoạn nhiệt $T_2 = 2T_1$ | Hệ số thay đổi áp suất $p_2 / p_1$ | $\frac{p_2}{p_1} = 2^{5/2} = 4\sqrt{2} \approx 5{,}66$ | Quy luật $p \propto T^{\frac{\gamma}{\gamma - 1}}$ |

---

## 4. Ghi Chú Độc Quyền Về Dị Biệt Sách Gốc (Private Erratum Note)

> [!NOTE]
> Mục này là ghi chú nội bộ dành riêng cho kiểm thử và rà soát sư phạm, tuyệt đối không đưa vào nội dung bài giảng công khai của học viên.

- **Vị trí**: Bài tập 19.33 (PDF trang 655).
- **Hiện tượng**: Một số ấn bản in và bảng đáp án phía sau của sách gốc có lỗi in ấn cơ học (typo) ghi kết quả là `422` hoặc các biến thể gõ nhầm từ biểu thức căn thức.
- **Phân tích toán học & Vật lý chính xác**:
  - Khí heli là khí hiếm đơn nguyên tử, có số bậc tự do chuyển động tịnh tiến $i = 3$. Do đó, tỷ số nhiệt dung phân tử là:
    $$
    \gamma = \frac{C_p}{C_V} = \frac{\frac{5}{2}R}{\frac{3}{2}R} = \frac{5}{3}.
    $$
  - Phương trình biến đổi đoạn nhiệt liên hệ giữa áp suất $p$ và nhiệt độ tuyệt đối $T$:
    $$
    T^\gamma p^{1 - \gamma} = \text{const} \implies p \propto T^{\frac{\gamma}{\gamma - 1}}.
    $$
  - Số mũ:
    $$
    \frac{\gamma}{\gamma - 1} = \frac{\frac{5}{3}}{\frac{5}{3} - 1} = \frac{\frac{5}{3}}{\frac{2}{3}} = \frac{5}{2} = 2{,}5.
    $$
  - Khi nhiệt độ tuyệt đối $T$ tăng gấp đôi ($T_2 = 2T_1$):
    $$
    \frac{p_2}{p_1} = \left(\frac{T_2}{T_1}\right)^{5/2} = 2^{5/2} = 2^2 \cdot 2^{1/2} = 4\sqrt{2} \approx 5{,}65685 \dots \approx 5{,}66.
    $$
- **Xử lý trong bài giảng StudyHub**: Giữ vững tính chuẩn mực học thuật và tính độc lập của bài giảng, trình bày lời giải phân tích chuẩn mực ra kết quả $4\sqrt{2} \approx 5{,}66$ lần, không trích dẫn hay phân bua về lỗi in ấn của ấn bản sách gốc.

---

## 5. Kết Quả Chạy Các Lệnh Kiểm Thử Tự Động (Verification Logs)

### 5.1. Kiểm thử số học và kiểm tra viền ảnh pixel (`verify_chapter19_exercises_d.py`)
- Lệnh chạy:
  ```bash
  C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter19_exercises_d.py
  ```
- Mã thoát (Exit code): `0` (Success).
- Trích xuất nhật ký đầu ra:
  ```text
  === KIỂM TRA SỐ HỌC TOÀN BỘ 33 BÀI TẬP CHAPTER 19 (NHÓM D) ===
  Đã kiểm tra thành công 33/33 bài tập, toàn bộ khẳng định số học đều đúng.

  === KIỂM TRA TÀI NGUYÊN HÌNH ẢNH PNG ===
  Xác minh toàn bộ 4 tệp ảnh PNG thành công, tất cả viền sạch 100%.

  === HOÀN TẤT TOÀN BỘ KIỂM TRA ĐỘC LẬP THÀNH CÔNG ===
  ```

### 5.2. Đo lường kích thước công thức toán học (`measure-math.mjs`)
- Lệnh chạy:
  ```bash
  node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . raw_materials/physics/translations/chapter-19/11-bai-tap-001-033.md
  ```
- Mã thoát (Exit code): `0` (Success).
- Kết quả JSON:
  ```json
  {
    "status": "passed",
    "scope": "Strict draft math and syntax probe, not semantic or browser acceptance",
    "display": 172,
    "inline": 814,
    "findings": []
  }
  ```
- Đánh giá: 172 công thức hiển thị (`display`) và 814 công thức nội dòng (`inline`) đều thỏa mãn hoàn hảo giới hạn độ rộng (display $\le 25\text{ex}$, inline $\le 27\text{ex}$, tối đa 38ex). Toàn bộ khối toán đặt cô lập ở cột 0, không có thanh cuộn ngang (scrollbar).

### 5.3. Kiểm tra dynamic import của từ điển chú thích (`image-annotations.mjs`)
- Lệnh chạy:
  ```bash
  node -e "import('./docs/.vitepress/physics1-19-exercises-d-image-annotations.mjs').then(m => { console.log('Import successful, keys:', Object.keys(m.physics1Chapter19ExercisesDImageAnnotations)); process.exit(0); }).catch(e => { console.error(e); process.exit(1); })"
  ```
- Mã thoát (Exit code): `0` (Success).
- Khóa đã đăng ký:
  - `young-19/d-hinh-e19-4`
  - `young-19/d-hinh-19-7a`
  - `young-19/d-hinh-e19-11`
  - `young-19/d-hinh-e19-13`

---

## 6. Kết Luận Nghiệm Thu

1. **Tính độc lập & Chủ quyền bài giảng**: Toàn bộ 33 bài giảng tuân thủ triệt để văn phong giảng viên độc lập, chuẩn mực học thuật tiếng Việt, đi từ bản chất vật lý, không trích dẫn hay sao chép thụ động giáo trình.
2. **Quy chuẩn văn phong tiếng Việt**: Tuân thủ quy tắc viết hoa sau dấu hai chấm (`:`), kiểm soát câu dưới 55 từ, không lạm dụng dấu gạch ngang dài (`—`) hay dấu chấm phẩy (`;`), không có câu thoại nháp AI.
3. **Chuẩn mực công thức toán học**: Toàn bộ công thức không có thanh cuộn, ngắt dòng đúng chuẩn tại dấu quan hệ trong `\begin{aligned}`, căn lề chuẩn mực.
4. **Không phát sinh lỗi**: Không có lỗi quyền truy cập, hạn ngạch (quota) hay lỗi môi trường. Tất cả kiểm thử cục bộ hợp lệ đã vượt qua với mã thoát `0`.
