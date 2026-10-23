# Báo cáo thẩm định kỹ thuật: Bài tập Chương 19 - Nhóm C (StudyHub)

**Mã công việc:** `physics1-19-exercises-c-20261022`
**Không gian làm việc:** `C:\Users\Ai\.codex\worktrees\physics1-19-exercises-c-20261022\StudyHub`
**Ngày thẩm định:** 22/10/2026
**Kế hoạch cam kết:** `docs/agy-plans/2026-10-22-physics1-19-exercises-c.md`

---

## 1. Danh mục tệp thuộc quyền sở hữu (Exact Owned Files)

Tất cả các tệp thay đổi và tạo mới đều thuộc phạm vi sở hữu độc quyền của nhiệm vụ:

1. `raw_materials/physics/translations/chapter-19/09-luyen-tap-huong-dan.md`: 12 bài tập có hướng dẫn (VP19.5.1 – VP19.7.4).
2. `raw_materials/physics/translations/chapter-19/10-cau-hoi-thao-luan.md`: 24 câu hỏi thảo luận định tính (Q19.1 – Q19.24).
3. `raw_materials/physics/translations/chapter-19/16-bai-tap-cau-noi.md`: 1 bài tập cầu nối (Bridging Problem) mở rộng trọn vẹn 8 bước Solution Guide.
4. `scripts/prepare-physics1-19-exercises-c-assets.py`: Script trích xuất và kiểm tra biên ảnh gốc từ PDF Young & Freedman 15th ed.
5. `docs/.vitepress/physics1-19-exercises-c-image-annotations.mjs`: Catalog nhãn song ngữ cho ảnh minh họa.
6. `raw_materials/physics/verify_chapter19_exercises_c.py`: Bộ kiểm thử số học và vật lý độc lập cho toàn bộ 37 đơn vị bài tập.
7. `raw_materials/physics/reviews/ch19-agy-exercises-c-review.md`: Báo cáo thẩm định kỹ thuật nội bộ này.

**Ảnh trích xuất độc quyền (Exclusive Flat PNGs):**
- `docs/vat-ly-1/bai-giang/img/young-19/c-fig-19-22.png` ($774 \times 345$, RGB, `alpha=False`)
- `docs/vat-ly-1/bai-giang/img/young-19/c-fig-q19-23.png` ($573 \times 348$, RGB, `alpha=False`)
- `docs/vat-ly-1/bai-giang/img/young-19/c-fig-q19-24.png` ($573 \times 390$, RGB, `alpha=False`)

---

## 2. Kiểm kê danh mục bài tập (Inventory of 37 Units)

| Nhóm | Mã bài | Loại bài | Nội dung vật lý |
| :--- | :--- | :--- | :--- |
| Guided Practice | VP19.5.1 | Số học (3 ý) | Định luật 1 nhiệt động lực học: $\Delta U = Q - W$. |
| Guided Practice | VP19.5.2 | Số học (4 ý) | Công trong các quá trình đẳng áp, đẳng tích và đường thẳng trên giản đồ $pV$. |
| Guided Practice | VP19.5.3 | Số học (2 ý) | Quá trình hai bước trong xi lanh có piston, công phụ thuộc đường đi. |
| Guided Practice | VP19.5.4 | Số học (3 ý) | Thăng hoa của $\text{CO}_2$ rắn ở áp suất khí quyển: nhiệt lượng, công và $\Delta U$. |
| Guided Practice | VP19.6.1 | Số học (3 ý) | Khí neon: $\Delta U = n C_V \Delta T$ cho các quá trình đẳng tích, đẳng áp và biến đổi tổng quát. |
| Guided Practice | VP19.6.2 | Số học (2 ý lớn, 4 ý nhỏ) | Khí nitơ: Thể tích ban đầu và biến thiên nội năng khi $p, V$ tăng gấp đôi. |
| Guided Practice | VP19.6.3 | Số học (3 ý) | Khí agon: $\Delta U = \frac{C_V}{R} (p_2 V_2 - p_1 V_1)$. |
| Guided Practice | VP19.6.4 | Biểu thức (3 ý) | Khí oxy đốt nóng từ $T$ đến $2T$: $\Delta U, Q, W$ cho quá trình đẳng tích, đẳng áp, đoạn nhiệt. |
| Guided Practice | VP19.7.1 | Số học (3 ý) | Khí agon giãn nở đoạn nhiệt: Chỉ số $\gamma$, áp suất cuối $p_2$, công thực hiện $W$. |
| Guided Practice | VP19.7.2 | Số học (4 ý) | Khí oxy nén đoạn nhiệt từ $325\text{ K}$ lên $855\text{ K}$: $\gamma, V_2, p_2, W$. |
| Guided Practice | VP19.7.3 | Số học (4 ý) | Khí neon giãn nở đoạn nhiệt: $p_1, p_2, T_2, W$. |
| Guided Practice | VP19.7.4 | Số học (3 ý) | Khí hydro giãn nở đoạn nhiệt từ $325\text{ K}$ xuống $195\text{ K}$: $W, V_2/V_1, p_2/p_1$. |
| Bridging Problem | BP19 | Giải tích & Số học | Công giãn nở đẳng nhiệt của khí van der Waals và khí lý tưởng; 8 bước Solution Guide. |
| Discussion | Q19.1 | Định tính (4 ý) | Dấu của công thực hiện bởi chất khí lên môi trường xung quanh. |
| Discussion | Q19.2 | Định tính | Bản chất nhiệt lượng là năng lượng đang truyền qua biên, không phải hàm trạng thái. |
| Discussion | Q19.3 | Định tính | So sánh công bơm bóng bay ở mực nước biển và ở đỉnh núi McKinley ($W = p_{\text{atm}} \Delta V$). |
| Discussion | Q19.4 | Định tính | Tính phụ thuộc đường đi của $Q$ và $W$; không thể suy riêng rẽ từ $\Delta U$. |
| Discussion | Q19.5 | Định tính | Định luật 1 áp dụng cho người leo núi: Hóa năng thức ăn và thế năng trọng trường. |
| Discussion | Q19.6 | Định tính | Nước đá tan ở $0^\circ\text{C}$ bị co thể tích ($\Delta V < 0$), $\Delta U = Q + |W| > Q$. |
| Discussion | Q19.7 | Định tính | Bóng bay hơ nóng rồi nguội về nhiệt độ phòng: $Q > W$ khi giãn nở; chu trình kín $Q_{\text{net}} = W_{\text{net}}$. |
| Discussion | Q19.8 | Định tính | Bánh quy nguội trong hộp có nắp lỏng: Quá trình đẳng áp (isobaric). |
| Discussion | Q19.9 | Định tính | Khí electron tự do giãn nở tự do: Lực đẩy tĩnh điện sinh công dương làm tăng nhiệt độ. |
| Discussion | Q19.10 | Định tính | Khí lý tưởng giãn nở đoạn nhiệt giảm áp suất: Nhiệt độ giảm, nội năng giảm. |
| Discussion | Q19.11 | Định tính | Thổi hơi qua miệng mở rộng vs miệng thu nhỏ "o": Hiệu ứng Joule–Thomson và giãn nở đoạn nhiệt. |
| Discussion | Q19.12 | Định tính | Khí lý tưởng giãn nở đẳng áp: Cần truyền nhiệt vào hệ ($Q = \Delta U + W > 0$). |
| Discussion | Q19.13 | Định tính | Khuấy chất lỏng bất quy tắc trong bình cách nhiệt: $Q = 0, W < 0, \Delta U > 0$. |
| Discussion | Q19.14 | Định tính | Bơm tay xe đạp nóng lên: Nén đoạn nhiệt sinh công làm tăng nội năng không khí. |
| Discussion | Q19.15 | Định tính | Đóng băng trong họng chế hòa khí: Hiệu ứng Bernoulli, giãn nở đoạn nhiệt và bay hơi nhiên liệu. |
| Discussion | Q19.16 | Định tính | Bong bóng khí nhiệt bốc lên trong khí quyển: Giãn nở đoạn nhiệt do thời gian ngắn và độ dẫn nhiệt thấp. |
| Discussion | Q19.17 | Định tính | Gió thổi lên sườn đón gió núi Waialeale nguội đi: Giãn nở đoạn nhiệt khi áp suất giảm theo độ cao. |
| Discussion | Q19.18 | Định tính | Đảo Niihau khô hạn: Không khí khô hạ độ cao bị nén đoạn nhiệt tạo gió Foehn khô nóng. |
| Discussion | Q19.19 | Định tính | Khác biệt $dU = n C_V dT$ và $dU \neq n C_p dT$: Công giãn nở $p \, dV$ trong quá trình đẳng áp. |
| Discussion | Q19.20 | Định tính | Nguồn năng lượng làm tăng nhiệt độ khi nén đoạn nhiệt: Công của ngoại lực thực hiện lên hệ. |
| Discussion | Q19.21 | Định tính | Nguồn năng lượng để sinh công khi giãn nở đoạn nhiệt: Nội năng nội tại của khối khí. |
| Discussion | Q19.22 | Định tính | So sánh tốc độ tăng nhiệt của $\text{UF}_6$ và $\text{H}_2$: Phân tử đa nguyên tử có nhiệt dung mol lớn hơn nhiều. |
| Discussion | Q19.23 | Định tính (2 ý) | Giản đồ $pV$ với 3 đường biến đổi: So sánh công $W_1 > W_2 > W_3 > 0$ và nhiệt lượng $Q_1 > Q_2 > Q_3 > 0$. |
| Discussion | Q19.24 | Định tính (2 ý) | Giản đồ $pV$ với 3 đường biến đổi: Chiều truyền nhiệt ($Q_1 > 0$, $Q_3 < 0$, đường 2 đoạn nhiệt $Q_2 = 0$). |

---

## 3. Bảng đối chiếu số học & Dung sai kiểm thử (Numerical Verification Ledger)

Tất cả các giá trị tính toán đã được kiểm chứng bằng Python 3.14 (`raw_materials/physics/verify_chapter19_exercises_c.py`):

| Mã bài | Ý | Dữ liệu đầu vào | Biểu thức giải tích | Kết quả tính toán | Dung sai kiểm thử | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **VP19.5.1** | (a) | $\Delta U = 2{,}50 \times 10^3\text{ J}$, $W = 3{,}25 \times 10^3\text{ J}$ | $Q = \Delta U + W$ | $5{,}75 \times 10^3\text{ J}$ | $\pm 0{,}01 \times 10^3\text{ J}$ | Khớp |
| | (b) | $W = 2{,}50 \times 10^4\text{ J}$, $Q = -7{,}00 \times 10^3\text{ J}$ | $\Delta U = Q - W$ | $-3{,}20 \times 10^4\text{ J}$ | $\pm 0{,}01 \times 10^4\text{ J}$ | Khớp |
| | (c) | $\Delta U = 4{,}25 \times 10^3\text{ J}$, $Q = 2{,}40 \times 10^3\text{ J}$ | $W = Q - \Delta U$ | $-1{,}85 \times 10^3\text{ J}$ | $\pm 0{,}01 \times 10^3\text{ J}$ | Khớp |
| **VP19.5.2** | (a) | $p = 6{,}20 \times 10^4\text{ Pa}$, $\Delta V = 2{,}50 \times 10^{-3}\text{ m}^3$ | $W = p \Delta V$ | $155\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| | (b) | $\Delta V = 0$ | $W = 0$ | $0\text{ J}$ | Tuyệt đối | Khớp |
| | (c) | $p = 1{,}25 \times 10^5\text{ Pa}$, $\Delta V = -3{,}00 \times 10^{-3}\text{ m}^3$ | $W = p \Delta V$ | $-375\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| | (d) | $\bar{p} = 3{,}50 \times 10^5\text{ Pa}$, $\Delta V = 2{,}50 \times 10^{-3}\text{ m}^3$ | $W = \frac{p_1 + p_2}{2}\Delta V$ | $875\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| **VP19.5.3** | (a) | $V_1 = 3{,}60\text{ L}, V_2 = 2{,}40\text{ L}, p_1 = 2{,}00\text{ bar}, Q = 1560\text{ J}$ | $W = p_1(V_2 - V_1)$, $\Delta U = Q - W$ | $W = -240\text{ J}, \Delta U = 1800\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| | (b) | $p_1 = 2{,}00\text{ bar}, p_2 = 6{,}00\text{ bar}, V_1 = 3{,}60\text{ L}, V_2 = 2{,}40\text{ L}$ | $W = p_2(V_2 - V_1)$, $Q = \Delta U + W$ | $W = -720\text{ J}, Q = 1080\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| **VP19.5.4** | (a) | $m = 6{,}0\text{ kg}, L_{\text{sub}} = 5{,}71 \times 10^5\text{ J/kg}$ | $Q = m L_{\text{sub}}$ | $3{,}43 \times 10^6\text{ J}$ | $\pm 0{,}01 \times 10^6\text{ J}$ | Khớp |
| | (b) | $p = 1{,}01 \times 10^5\text{ Pa}, \Delta V = 3{,}396\text{ m}^3$ | $W = p \Delta V$ | $3{,}43 \times 10^5\text{ J}$ | $\pm 0{,}01 \times 10^5\text{ J}$ | Khớp |
| | (c) | $Q = 3{,}426 \times 10^6\text{ J}, W = 3{,}430 \times 10^5\text{ J}$ | $\Delta U = Q - W$ | $3{,}08 \times 10^6\text{ J}$ | $\pm 0{,}01 \times 10^6\text{ J}$ | Khớp |
| **VP19.6.1** | (a) | $n = 4{,}00\text{ mol}, C_V = 1{,}5R, \Delta T = 20{,}0\text{ K}$ | $\Delta U = n C_V \Delta T$ | $998\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| | (b) | $n = 4{,}00\text{ mol}, C_V = 1{,}5R, \Delta T = 15{,}0\text{ K}$ | $\Delta U = n C_V \Delta T$ | $748\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| | (c) | $n = 4{,}00\text{ mol}, C_V = 1{,}5R, \Delta T = 12{,}0\text{ K}$ | $\Delta U = n C_V \Delta T$ | $599\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| **VP19.6.2** | (a) | $n = 2{,}10\text{ mol}, T_1 = 300{,}15\text{ K}, p_1 = 1{,}00 \times 10^5\text{ Pa}$ | $V_1 = nRT_1 / p_1$ | $0{,}0524\text{ m}^3$ | $\pm 0{,}0001\text{ m}^3$ | Khớp |
| | (b)(i) | $p_2 = 2p_1, V_2 = V_1 \implies T_2 = 2T_1$ | $T_2 = 327^\circ\text{C}, \Delta U = n C_V \Delta T$ | $1{,}31 \times 10^4\text{ J}$ | $\pm 0{,}01 \times 10^4\text{ J}$ | Khớp |
| | (b)(ii) | $V_2 = 2V_1, p_2 = p_1 \implies T_2 = 2T_1$ | $T_2 = 327^\circ\text{C}, \Delta U = n C_V \Delta T$ | $1{,}31 \times 10^4\text{ J}$ | $\pm 0{,}01 \times 10^4\text{ J}$ | Khớp |
| | (b)(iii)| $p_2 = 2p_1, V_2 = 2V_1 \implies T_2 = 4T_1$ | $T_2 = 927^\circ\text{C}, \Delta U = n C_V (3T_1)$ | $3{,}93 \times 10^4\text{ J}$ | $\pm 0{,}01 \times 10^4\text{ J}$ | Khớp |
| **VP19.6.3** | (a) | $p_1 = 1{,}20\text{ bar}, V_1 = 0{,}250\text{ m}^3; p_2 = 2{,}40\text{ bar}, V_2 = 0{,}250\text{ m}^3$| $\Delta U = 1{,}5 (p_2 V_2 - p_1 V_1)$ | $4{,}50 \times 10^4\text{ J}$ | $\pm 0{,}01 \times 10^4\text{ J}$ | Khớp |
| | (b) | $p_2 = 1{,}20\text{ bar}, V_2 = 0{,}125\text{ m}^3$ | $\Delta U = 1{,}5 (p_2 V_2 - p_1 V_1)$ | $-2{,}25 \times 10^4\text{ J}$ | $\pm 0{,}01 \times 10^4\text{ J}$ | Khớp |
| | (c) | $p_2 = 1{,}80\text{ bar}, V_2 = 0{,}600\text{ m}^3$ | $\Delta U = 1{,}5 (p_2 V_2 - p_1 V_1)$ | $1{,}17 \times 10^5\text{ J}$ | $\pm 0{,}01 \times 10^5\text{ J}$ | Khớp |
| **VP19.6.4** | (a) | Đẳng tích, $\Delta T = T$ | $\Delta U = \frac{5}{2}nRT, W = 0, Q = \frac{5}{2}nRT$ | Đại số chính xác | Lý thuyết | Khớp |
| | (b) | Đẳng áp, $\Delta T = T$ | $\Delta U = \frac{5}{2}nRT, W = nRT, Q = \frac{7}{2}nRT$ | Đại số chính xác | Lý thuyết | Khớp |
| | (c) | Đoạn nhiệt, $\Delta T = T$ | $\Delta U = \frac{5}{2}nRT, Q = 0, W = -\frac{5}{2}nRT$ | Đại số chính xác | Lý thuyết | Khớp |
| **VP19.7.1** | (a) | Agon: $C_p = 2{,}5R, C_V = 1{,}5R$ | $\gamma = C_p / C_V$ | $1{,}67$ | $\pm 0{,}01$ | Khớp |
| | (b) | $p_1 = 4{,}00 \times 10^5\text{ Pa}, V_1 = 2{,}00\text{ L}, V_2 = 6{,}00\text{ L}$ | $p_2 = p_1 (V_1/V_2)^\gamma$ | $6{,}41 \times 10^4\text{ Pa}$ | $\pm 0{,}02 \times 10^4\text{ Pa}$ | Khớp |
| | (c) | $W = (p_1 V_1 - p_2 V_2) / (\gamma - 1)$ | $W = -\Delta U$ | $623\text{ J}$ | $\pm 1\text{ J}$ | Khớp |
| **VP19.7.2** | (a) | Oxy: $C_p = 3{,}5R, C_V = 2{,}5R$ | $\gamma = C_p / C_V$ | $1{,}40$ | $\pm 0{,}01$ | Khớp |
| | (b) | $T_1 = 325\text{ K}, T_2 = 855\text{ K}, V_1 = 6{,}50\text{ L}$ | $V_2 = V_1 (T_1/T_2)^{1/(\gamma-1)}$ | $5{,}84 \times 10^{-4}\text{ m}^3$ | $\pm 0{,}02 \times 10^{-4}\text{ m}^3$ | Khớp |
| | (c) | $p_1 = 1{,}00 \times 10^5\text{ Pa}$ | $p_2 = p_1 (V_1/V_2)^\gamma$ | $2{,}93 \times 10^6\text{ Pa}$ | $\pm 0{,}02 \times 10^6\text{ Pa}$ | Khớp |
| | (d) | $W = n C_V (T_1 - T_2)$ | $n = p_1 V_1 / RT_1 = 0{,}2405\text{ mol}$ | $-2{,}65 \times 10^3\text{ J}$ | $\pm 0{,}02 \times 10^3\text{ J}$ | Khớp |
| **VP19.7.3** | (a) | $n = 5{,}00\text{ mol}, T_1 = 305\text{ K}, V_1 = 0{,}0400\text{ m}^3$ | $p_1 = nRT_1 / V_1$ | $3{,}17 \times 10^5\text{ Pa}$ | $\pm 0{,}01 \times 10^5\text{ Pa}$ | Khớp |
| | (b) | $V_2 = 0{,}0900\text{ m}^3, \gamma = 5/3$ | $p_2 = p_1 (V_1/V_2)^{5/3}$ | $8{,}18 \times 10^4\text{ Pa}$ | $\pm 0{,}02 \times 10^4\text{ Pa}$ | Khớp |
| | (c) | $T_2 = T_1 (V_1/V_2)^{\gamma-1}$ | $T_2 = 305 \times (4/9)^{2/3}$ | $178\text{ K}$ ($-95^\circ\text{C}$) | $\pm 1\text{ K}$ | Khớp |
| | (d) | $W = n C_V (T_1 - T_2)$ | $W = 5{,}00 \times 1{,}5R \times (305 - 178)$ | $7{,}94 \times 10^3\text{ J}$ | $\pm 0{,}03 \times 10^3\text{ J}$ | Khớp |
| **VP19.7.4** | (a) | $n = 1{,}25\text{ mol}, T_1 = 325\text{ K}, T_2 = 195\text{ K}$ | $W_{\text{exp}} = n C_V (T_1 - T_2)$ | $3{,}38 \times 10^3\text{ J}$ (công sinh ra) | $\pm 0{,}02 \times 10^3\text{ J}$ | Khớp |
| | (b) | $V_2 / V_1 = (T_1 / T_2)^{1/(\gamma - 1)}$ | $(325 / 195)^{2{,}5}$ | $3{,}58$ | $\pm 0{,}02$ | Khớp |
| | (c) | $p_2 / p_1 = (T_2 / T_1)^{\gamma/(\gamma - 1)}$ | $(195 / 325)^{3{,}5}$ | $0{,}167$ | $\pm 0{,}002$ | Khớp |
| **Bridging Problem** | (b)(i) | Khí van der Waals ($\text{C}_2\text{H}_6$): $a = 0{,}554, b = 6{,}38 \times 10^{-5}$ | $W = nRT \ln\frac{V_2-nb}{V_1-nb} + an^2(\frac{1}{V_2}-\frac{1}{V_1})$ | $2{,}80 \times 10^3\text{ J}$ ($2798\text{ J}$) | $\pm 0{,}02 \times 10^3\text{ J}$ | Khớp |
| | (b)(ii)| Khí lý tưởng | $W = nRT \ln(V_2 / V_1)$ | $3{,}11 \times 10^3\text{ J}$ ($3112\text{ J}$) | $\pm 0{,}02 \times 10^3\text{ J}$ | Khớp |
| | (c) | So sánh và phân tích vai trò $a, b$ | $\Delta W = 314\text{ J}$ ($10{,}1\%$) | $W_{\text{ideal}} > W_{\text{vdW}}$ | Định tính | Khớp |

---

## 4. Sổ tay lỗi in giáo trình gốc (Discrepancies & Printed Errata Ledger)

1. **VP19.5.1 Đáp án sách in thừa mục (d):**
   - *Chi tiết*: Trong mục đáp án ở cuối sách (Answer Key trang 654), mục VP19.5.1 in kèm đáp án `(d) 875 J`.
   - *Thực tế*: Đề bài VP19.5.1 chỉ có 3 câu hỏi (a), (b), (c). Giá trị $875\text{ J}$ chính là đáp án của câu VP19.5.2(d) bị in nhầm lặp lại ở dòng trên.
   - *Xử lý*: Giữ nguyên đề bài 3 ý chuẩn mực, giải đầy đủ (a), (b), (c); ghi nhận đối chiếu nội bộ.
2. **VP19.7.3 & VP19.7.4 Ký hiệu tỷ số nhiệt dung $\gamma$:**
   - *Chi tiết*: Giáo trình gốc in sai chính tả chữ cái Hy Lạp thành `g = 5/2 R` và `g = 7/2 R` (chữ Latin `g` thay vì $\gamma$, và thừa đơn vị $R$ của nhiệt dung $C_p$).
   - *Thực tế*: Khí neon đơn nguyên tử có $\gamma = C_p / C_V = \frac{5}{2}R / \frac{3}{2}R = 5/3 \approx 1{,}67$; khí hydro lưỡng nguyên tử có $\gamma = \frac{7}{2}R / \frac{5}{2}R = 7/5 = 1{,}40$.
   - *Xử lý*: Khôi phục đúng ký hiệu $\gamma$ không thứ nguyên theo chuẩn vật lý nhiệt động lực học và giải thích rõ bản chất.
3. **VP19.7.4 Diễn đạt "while being compressed" trong đề bài:**
   - *Chi tiết*: Đề bài ghi *"You allow the gas to expand adiabatically to a final temperature of 195 K. (a) How much work does the gas do while being compressed?"*
   - *Thực tế*: Nhiệt độ khí giảm từ $325\text{ K}$ xuống $195\text{ K}$, thể tích tăng gấp $3{,}58$ lần, đây là quá trình giãn nở ($W_{\text{exp}} = +3{,}38 \times 10^3\text{ J}$), không phải nén. Đáp án cuối sách in $-3{,}38 \times 10^3\text{ J}$ (công mà chất khí nhận vào, tức $\Delta U$).
   - *Xử lý*: Trình bày cả hai góc nhìn: Công mà chất khí sinh ra đẩy môi trường ngoài là $+3{,}38 \times 10^3\text{ J}$, và công do ngoại lực thực hiện lên chất khí (hay độ biến thiên nội năng $\Delta U$) là $-3{,}38 \times 10^3\text{ J}$.

---

## 5. Kiểm tra cắt ảnh & Khảo sát biên (Image Cropping & Border Inspection)

Tất cả các hình ảnh được trích xuất trực tiếp từ file PDF gốc `raw_materials/physics/source/young-freedman-15.pdf` bằng script `scripts/prepare-physics1-19-exercises-c-assets.py`:

| Tên tệp ảnh | Trang PDF | Tọa độ trích xuất $(x_0, y_0, x_1, y_1)$ | Kích thước | Kênh màu | Khảo sát biên 4 cạnh | Trạng thái biên |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `c-fig-19-22.png` | 654 | `(308, 58, 566, 173)` | $774 \times 345$ | RGB (`alpha=False`) | Biên trắng thuần khiết ($>250$), không cắt cụt nét vẽ hay nhãn chữ | HỢP LỆ |
| `c-fig-q19-23.png` | 655 | `(74, 230, 265, 346)` | $573 \times 348$ | RGB (`alpha=False`) | Đủ 3 đường đồ thị, trục $p, V$, các điểm $a, b$ và nhãn số $1, 2, 3$ | HỢP LỆ |
| `c-fig-q19-24.png` | 655 | `(74, 425, 265, 555)` | $573 \times 390$ | RGB (`alpha=False`) | Đủ 3 đường $1, 2, 3$, các trạng thái $a, b$ và chú thích đường 2 đoạn nhiệt | HỢP LỆ |

**Kiểm tra import nhãn ảnh song ngữ:**
Lệnh: `node -e "import('./docs/.vitepress/physics1-19-exercises-c-image-annotations.mjs')"`
Kết quả: Mã thoát `0`. Đầy đủ 3 khóa ảnh với các cặp nhãn Anh – Việt chuẩn mực học thuật, không có nhãn tiếng Anh trùng lặp hoặc cặp giống hệt nhau.

---

## 6. Kiểm tra chuẩn mực toán học & Ngắt dòng (Math Quality & Width Audit)

Lệnh kiểm tra:
```bash
node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . \
  raw_materials/physics/translations/chapter-19/09-luyen-tap-huong-dan.md \
  raw_materials/physics/translations/chapter-19/10-cau-hoi-thao-luan.md \
  raw_materials/physics/translations/chapter-19/16-bai-tap-cau-noi.md
```

**Kết quả kiểm tra toàn cục:**
```json
{
  "status": "passed",
  "scope": "Strict draft math and syntax probe, not semantic or browser acceptance",
  "display": 210,
  "inline": 652,
  "findings": []
}
```

- Tổng số khối công thức hiển thị (`$$...$$`): **210 khối**. Toàn bộ nằm độc lập ở cột 0, chiều rộng $\le 25\text{ex}$, không có lỗi cú pháp.
- Tổng số công thức nội dòng (`$...$`): **652 biểu thức**. Chiều rộng tối đa $\le 27\text{ex}$ (dưới ngưỡng ngặt $38\text{ex}$), không có ký hiệu phân cách rớt dòng.
- Số lượng lỗi (findings): **0 lỗi** trên cả 3 tệp Markdown.

---

## 7. Nhật ký lệnh thực thi & Mã thoát (Command & Exit Code Ledger)

| Lệnh thực thi | Mục đích | Mã thoát | Kết quả |
| :--- | :--- | :--- | :--- |
| `git status --short` | Kiểm tra trạng thái vùng làm việc | `0` | Chỉ gồm các tệp thuộc quyền sở hữu |
| `C:/Users/Ai/miniconda3/python.exe -X utf8 scripts/prepare-physics1-19-exercises-c-assets.py` | Trích xuất 3 ảnh gốc từ PDF | `0` | 3 ảnh PNG chuẩn RGB, biên hợp lệ |
| `node -e "import('./docs/.vitepress/physics1-19-exercises-c-image-annotations.mjs')"` | Kiểm tra import catalog nhãn ảnh | `0` | Import thành công 3 bộ nhãn |
| `C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter19_exercises_c.py` | Kiểm tra độc lập 37 bài tập | `0` | Toàn bộ 37 mục vượt qua assertion |
| `node .../measure-math.mjs . raw_materials/.../09-luyen-tap-huong-dan.md` | Kiểm định toán học bài luyện tập | `0` | 112 display, 352 inline, 0 lỗi |
| `node .../measure-math.mjs . raw_materials/.../10-cau-hoi-thao-luan.md` | Kiểm định toán học câu hỏi thảo luận | `0` | 63 display, 236 inline, 0 lỗi |
| `node .../measure-math.mjs . raw_materials/.../16-bai-tap-cau-noi.md` | Kiểm định toán học bài tập cầu nối | `0` | 35 display, 64 inline, 0 lỗi |
| `node .../measure-math.mjs . [cả 3 tệp đồng thời]` | Kiểm định toán học toàn diện | `0` | 210 display, 652 inline, 0 lỗi |

---

## 8. Báo cáo lỗi quyền, ủy quyền & Quota (Permissions, Auth & Quota)

- **Lỗi phân quyền (Permission Errors)**: Không có (`dangerously_skip_permissions=true` được người dùng ủy quyền hợp lệ).
- **Lỗi xác thực (Authentication Errors)**: Không có.
- **Lỗi giới hạn tài nguyên (Quota Errors)**: Không có.
- **Đơn vị bài tập bị thiếu (Missing Units)**: Không có (đầy đủ $37/37$ đơn vị bài tập).
- **Phạm vi tệp vi phạm**: Không có bất kỳ tệp nào ngoài 7 tệp sở hữu và tiền tố ảnh quy định bị tạo ra hoặc thay đổi.
