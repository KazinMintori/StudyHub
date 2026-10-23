# Báo Cáo Rà Soát Học Thuật & Kiểm Thử Kỹ Thuật (Truthful Review Report)
## Nhiệm Vụ: Physics 1 Chapter 20 Theory B (Call 3 of 3)

- **Mã nhiệm vụ**: `physics1-20-theory-b-20261022`
- **Thời gian hoàn thành**: 2026-10-22
- **Thư mục làm việc độc lập**: `C:\Users\Ai\.codex\worktrees\physics1-20-theory-b-20261022\StudyHub`
- **Kế hoạch thực thi**: `docs/agy-plans/2026-10-22-physics1-20-theory-b.md`
- **Tình trạng chứng nhận**: Không tự cấp chứng chỉ 100% hay kiểm thử giao diện trình duyệt trực quan. Toàn bộ kết quả dựa trên các script kiểm thử số học, đối soát điểm ảnh RGB độc lập và kiểm tra cú pháp toán tự động.

---

## 1. Danh Mục Tệp Thuộc Quyền Sở Hữu (Owned Files)

Tất cả các tệp dưới đây được tạo lập và chỉnh sửa độc quyền trong phạm vi nhiệm vụ, tuân thủ nghiêm ngặt ranh giới không can thiệp vào các tệp ngoài phạm vi:

1. `raw_materials/physics/translations/chapter-20/05-nguyen-ly-thu-hai.md`
2. `raw_materials/physics/translations/chapter-20/06-chu-trinh-carnot.md`
3. `raw_materials/physics/translations/chapter-20/07-entropy.md`
4. `raw_materials/physics/translations/chapter-20/08-giai-thich-vi-mo-entropy.md`
5. `raw_materials/physics/translations/chapter-20/17-tom-tat.md`
6. `scripts/prepare-physics1-20-theory-b-assets.py`
7. `docs/.vitepress/physics1-20-theory-b-image-annotations.mjs`
8. `raw_materials/physics/verify_chapter20_theory_b.py`
9. `raw_materials/physics/reviews/ch20-agy-theory-b-review.md`
10. Bộ 21 tệp ảnh trích xuất phẳng định dạng PNG tại `docs/vat-ly-1/bai-giang/img/young-20/b-*.png`.

---

## 2. Phạm Vi Bao Phủ Nguồn Gốc (Source Unit Coverage)

Toàn bộ nội dung lý thuyết từ trang in 651–670 (tương ứng trang PDF 671–690) của giáo trình *Sears and Zemansky's University Physics with Modern Physics (15th Edition)* đã được chuyển tải đầy đủ sang tiếng Việt học thuật chuẩn mực:

- **Mục 20.5: Nguyên lý thứ hai nhiệt động lực học (PDF 671–673)**
  - Tự phát và tính một chiều của các quá trình nhiệt động tự nhiên.
  - Phát biểu Kelvin–Planck (dạng động cơ): Tính bất khả thi của động cơ đạt hiệu suất $100\%$.
  - Phát biểu Clausius (dạng máy lạnh): Tính bất khả thi của việc truyền nhiệt tự phát từ vật lạnh sang vật nóng mà không tiêu thụ công.
  - Chứng minh sự tương đương chặt chẽ giữa hai phát biểu bằng phương pháp phản chứng (ghép động cơ lý tưởng với máy lạnh thông thường và ngược lại).
  - Tự kiểm tra kiến thức mục 20.5 (TYU 20.5).

- **Mục 20.6: Chu trình Carnot (PDF 673–679)**
  - Phân tích nguyên nhân làm giảm hiệu suất trong động cơ thực (ma sát, truyền nhiệt qua chênh lệch nhiệt độ hữu hạn).
  - Bốn giai đoạn của chu trình Carnot cho khí lý tưởng (giãn đẳng nhiệt, giãn đoạn nhiệt, nén đẳng nhiệt, nén đoạn nhiệt).
  - Thiết lập công thức hiệu suất nhiệt $e_{\text{Carnot}} = 1 - T_C/T_H = (T_H - T_C)/T_H$.
  - Ví dụ 20.2: Tính $Q_C, W, e$ cho động cơ Carnot hoạt động giữa $500\,\mathrm K$ và $350\,\mathrm K$.
  - Hộp lưu ý quan trọng: Bắt buộc sử dụng thang nhiệt độ tuyệt đối Kelvin.
  - Ví dụ 20.3: Tính chi tiết các thông số trạng thái ($p, V$) tại 4 điểm và bảng năng lượng $Q, W, \Delta U$ cho từng giai đoạn và toàn chu trình của $0{,}200\,\mathrm{mol}$ khí lưỡng nguyên tử.
  - Máy lạnh Carnot: Hệ số làm lạnh cực đại $K_{\text{Carnot}} = T_C / (T_H - T_C)$.
  - Ví dụ 20.4: Vận hành chu trình trong Ví dụ 20.3 theo chiều ngược lại làm máy lạnh.
  - Định lý Carnot và chứng minh tính tối ưu cực đại bằng phản chứng (Hình 20.15).
  - Thang nhiệt độ tuyệt đối Kelvin dựa trên chu trình Carnot và mốc điểm ba của nước ($273{,}16\,\mathrm K$).
  - Tự kiểm tra kiến thức mục 20.6 (TYU 20.6: Động cơ chế tạo bằng đồng).

- **Mục 20.7: Entropy (PDF 679–685)**
  - Khái niệm entropy như thước đo định lượng cho mức độ hỗn loạn (disorder / randomness) của hệ.
  - Định nghĩa định lượng: $dS = dQ/T$ đối với quá trình thuận nghịch.
  - Biến thiên entropy trong quá trình đẳng nhiệt thuận nghịch: $\Delta S = Q/T$.
  - Ví dụ 20.5: Biến thiên entropy khi làm nóng chảy $1{,}00\,\mathrm{kg}$ nước đá ở $0^\circ\mathrm C$.
  - Ví dụ 20.6: Biến thiên entropy khi đun nóng $1{,}00\,\mathrm{kg}$ nước từ $0^\circ\mathrm C$ lên $100^\circ\mathrm C$.
  - Ví dụ 20.7: Biến thiên entropy trong quá trình đoạn nhiệt thuận nghịch ($\Delta S = 0$).
  - Ví dụ 20.8: Biến thiên entropy của khí lý tưởng trong quá trình giãn nở tự do vào chân không ($\Delta S = n R \ln 2$).
  - Ví dụ 20.9: Tính biến thiên entropy của chất tác công trong chu trình Carnot ($\Delta S_{\text{net}} = 0$).
  - Định lý Clausius cho chu trình thuận nghịch kín: $\oint dQ/T = 0$, chứng minh entropy là hàm trạng thái độc lập với đường đi.
  - Phương pháp tính biến thiên entropy trong các quá trình không thuận nghịch bằng đường đi thuận nghịch thay thế.
  - Ví dụ 20.10: Biến thiên entropy khi trộn không thuận nghịch hai khối nước $100^\circ\mathrm C$ và $0^\circ\mathrm C$.
  - Nguyên lý tăng entropy: $\Delta S \ge 0$ đối với hệ cô lập.
  - Ứng dụng thực tế: Biến thiên entropy trong cơ thể sinh vật sống (Hình ứng dụng 20.1) và sự khuếch tán mực trong nước (Hình 20.20).
  - Tự kiểm tra kiến thức mục 20.7 (TYU 20.7: Sự phân tách nhiệt độ tự phát).

- **Mục 20.8: Giải thích vi mô của entropy (PDF 685–688)**
  - Phân biệt trạng thái vĩ mô (macrostate) và trạng thái vi mô (microstate). Khái niệm bội số vi mô $w$.
  - Mô hình bốn đồng xu: Bảng chi tiết 16 trạng thái vi mô phân bố vào 5 trạng thái vĩ mô. Trực giác về sự chuyển dịch tự nhiên về trạng thái có $w$ lớn nhất.
  - Quy luật số lớn khi $N = 100$ và $N \approx 10^{23}$ hạt.
  - Công thức Boltzmann: $S = k \ln w$ và ý nghĩa cơ bản của hàm logarit.
  - Ví dụ 20.11: Suy dẫn công thức biến thiên entropy vi mô khi khối khí giãn nở thể tích gấp đôi ($\Delta S = n R \ln 2$), đối chiếu với Ví dụ 20.8.
  - Ứng dụng: Sự co cuộn tự phát của chuỗi phân tử polymer trong dung dịch và lực đàn hồi entropy trong cao su (Hình ứng dụng 20.2).
  - Tự kiểm tra kiến thức mục 20.8 (TYU 20.8: So sánh $w_2/w_1$ giữa giãn đẳng nhiệt và giãn đoạn nhiệt).

- **Tóm tắt Chương 20 (PDF 689–690)**
  - Khái quát hóa toàn bộ 8 đơn vị kiến thức trọng tâm của chương: Quá trình thuận nghịch/không thuận nghịch, Động cơ nhiệt & hiệu suất, Chu trình Otto & tỷ số nén, Máy lạnh & hệ số làm lạnh, Hai phát biểu của nguyên lý 2, Chu trình Carnot & máy lạnh Carnot, Entropy vĩ mô & nguyên lý tăng entropy, Entropy vi mô & công thức Boltzmann.
  - Dừng lại chính xác trước mục *Guided Practice* theo đúng yêu cầu đề bài.

---

## 3. Bảng Đối Soát Số Học & Kiểm Thử Đại Số (Numerical Ledger)

Toàn bộ các phép tính toán số học, biến đổi đại số và đơn vị đo lường trong bài giảng đã được lập trình và đối soát bằng code Python trong `raw_materials/physics/verify_chapter20_theory_b.py`:

| Bài toán / Ví dụ | Đại lượng đầu vào | Công thức tính toán | Kết quả tính toán Python | Giá trị trong giáo trình | Kết luận |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **Ví dụ 20.2** | $Q_H = 2000\,\mathrm J$<br>$T_H = 500\,\mathrm K$<br>$T_C = 350\,\mathrm K$ | $Q_C = -Q_H (T_C/T_H)$<br>$W = Q_H + Q_C$<br>$e = 1 - T_C/T_H$ | $Q_C = -1400\,\mathrm J$<br>$W = 600\,\mathrm J$<br>$e = 30{,}0\%$ | $-1400\,\mathrm J$<br>$600\,\mathrm J$<br>$30\%$ | **PASS** |
| **Ví dụ 20.3** | $n = 0{,}200\,\mathrm{mol}$<br>$\gamma = 1{,}40; C_V = 20{,}8$<br>$T_H = 500\,\mathrm K, T_C = 300\,\mathrm K$<br>$p_a = 10^6\,\mathrm{Pa}, V_b = 2V_a$ | $V_a = n R T_H / p_a$<br>$V_c = V_b (T_H/T_C)^{1/(\gamma-1)}$<br>$p_c = n R T_C / V_c$<br>$V_d = V_a (T_H/T_C)^{1/(\gamma-1)}$<br>$p_d = n R T_C / V_d$ | $V_a = 8{,}314 \times 10^{-4}\,\mathrm m^3$<br>$V_b = 16{,}63 \times 10^{-4}\,\mathrm m^3$<br>$p_b = 5{,}00 \times 10^5\,\mathrm{Pa}$<br>$V_c = 59{,}63 \times 10^{-4}\,\mathrm m^3$<br>$p_c = 0{,}8367 \times 10^5\,\mathrm{Pa}$<br>$V_d = 29{,}82 \times 10^{-4}\,\mathrm m^3$<br>$p_d = 1{,}673 \times 10^5\,\mathrm{Pa}$ | $8{,}31 \times 10^{-4}\,\mathrm m^3$<br>$16{,}6 \times 10^{-4}\,\mathrm m^3$<br>$5{,}00 \times 10^5\,\mathrm{Pa}$<br>$59{,}6 \times 10^{-4}\,\mathrm m^3$<br>$0{,}837 \times 10^5\,\mathrm{Pa}$<br>$29{,}8 \times 10^{-4}\,\mathrm m^3$<br>$1{,}67 \times 10^5\,\mathrm{Pa}$ | **PASS** |
| **Ví dụ 20.3 (công)** | Như trên | $W_{ab} = n R T_H \ln 2$<br>$W_{bc} = n C_V (T_H - T_C)$<br>$W_{cd} = n R T_C \ln(V_d/V_c)$<br>$W_{da} = n C_V (T_C - T_H)$<br>$W_{\text{net}} = W_{ab}+W_{bc}+W_{cd}+W_{da}$ | $W_{ab} = 576{,}3\,\mathrm J$<br>$W_{bc} = 832{,}0\,\mathrm J$<br>$W_{cd} = -345{,}8\,\mathrm J$<br>$W_{da} = -832{,}0\,\mathrm J$<br>$W_{\text{net}} = 230{,}5\,\mathrm J$<br>$e = 40{,}0\%$ | $576\,\mathrm J$<br>$832\,\mathrm J$<br>$-346\,\mathrm J$<br>$-832\,\mathrm J$<br>$230\,\mathrm J$<br>$40\%$ | **PASS** |
| **Ví dụ 20.4** | $Q_C = +346\,\mathrm J$<br>$|W| = 230\,\mathrm J$<br>$T_H = 500\,\mathrm K, T_C = 300\,\mathrm K$ | $K = |Q_C|/|W|$<br>$K_{\text{Carnot}} = T_C/(T_H - T_C)$ | $K = 1{,}504$<br>$K_{\text{Carnot}} = 1{,}500$ | $1{,}50$<br>$1{,}50$ | **PASS** |
| **TYU 20.6** | $T_C = 300\,\mathrm K$<br>$T_H \le 1356\,\mathrm K$ | $e_{\max} = 1 - T_C/T_H$ | $e_{\max} = 77{,}88\%$ | $78\% < 85\%$ | **PASS** |
| **Ví dụ 20.5** | $m = 1{,}00\,\mathrm{kg}$<br>$L_f = 3{,}34 \times 10^5\,\mathrm{J/kg}$<br>$T = 273\,\mathrm K$ | $Q = m L_f$<br>$\Delta S = Q / T$ | $Q = 3{,}34 \times 10^5\,\mathrm J$<br>$\Delta S = 1223{,}44\,\mathrm{J/K}$ | $3{,}34 \times 10^5\,\mathrm J$<br>$1{,}22 \times 10^3\,\mathrm{J/K}$ | **PASS** |
| **Ví dụ 20.6** | $m = 1{,}00\,\mathrm{kg}$<br>$c = 4190\,\mathrm{J/(kg\cdot K)}$<br>$T_1 = 273\,\mathrm K, T_2 = 373\,\mathrm K$ | $\Delta S = m c \ln(T_2/T_1)$ | $\Delta S = 1307{,}73\,\mathrm{J/K}$ | $1{,}31 \times 10^3\,\mathrm{J/K}$ | **PASS** |
| **Ví dụ 20.9** | $Q_H = 2000\,\mathrm J, T_H = 500\,\mathrm K$<br>$Q_C = -1400\,\mathrm J, T_C = 350\,\mathrm K$ | $\Delta S_H = Q_H/T_H$<br>$\Delta S_C = Q_C/T_C$<br>$\Delta S_{\text{net}} = \Delta S_H + \Delta S_C$ | $\Delta S_H = +4{,}0\,\mathrm{J/K}$<br>$\Delta S_C = -4{,}0\,\mathrm{J/K}$<br>$\Delta S_{\text{net}} = 0{,}0\,\mathrm{J/K}$ | $+4{,}0\,\mathrm{J/K}$<br>$-4{,}0\,\mathrm{J/K}$<br>$0$ | **PASS** |
| **Ví dụ 20.10** | $m_1 = m_2 = 1{,}00\,\mathrm{kg}$<br>$T_H = 373\,\mathrm K, T_C = 273\,\mathrm K$<br>$c = 4190\,\mathrm{J/(kg\cdot K)}$ | $T_{\text{cb}} = (T_H+T_C)/2$<br>$\Delta S_{\text{nóng}} = m c \ln(T_{\text{cb}}/T_H)$<br>$\Delta S_{\text{lạnh}} = m c \ln(T_{\text{cb}}/T_C)$<br>$\Delta S_{\text{tổng}} = \Delta S_H + \Delta S_C$ | $T_{\text{cb}} = 323\,\mathrm K$<br>$\Delta S_{\text{nóng}} = -603{,}1\,\mathrm{J/K}$<br>$\Delta S_{\text{lạnh}} = +704{,}7\,\mathrm{J/K}$<br>$\Delta S_{\text{tổng}} = +101{,}6\,\mathrm{J/K}$ | $323\,\mathrm K$<br>$-603\,\mathrm{J/K}$<br>$+705\,\mathrm{J/K}$<br>$+102\,\mathrm{J/K}$ | **PASS** |
| **Mục 20.8** | $N = 4$ đồng xu | $w = \binom{4}{k}, k \in [0..4]$<br>$\sum w = 2^4$ | $w = [1, 4, 6, 4, 1]$<br>$\sum w = 16$ | $[1, 4, 6, 4, 1]$<br>$16$ | **PASS** |

---

## 4. Kiểm Thử Trích Xuất Hình Ảnh & Đối Soát Điểm Ảnh RGB (Image Crop & RGB Audit)

21 hình ảnh minh họa đã được trích xuất trực tiếp từ tệp PDF gốc `young-freedman-15.pdf` với độ phóng đại `SCALE = 2.0` (tương đương 144 DPI) và không dùng kênh alpha (`alpha=False`). Toàn bộ ảnh trên đĩa đã được kiểm tra so khớp từng điểm ảnh (pixel-by-pixel RGB difference) đối chứng với một luồng render PDF tươi mới (fresh in-memory render) từ PyMuPDF:

| Tên tệp ảnh | Trang PDF | Bounding Box tọa độ gốc PDF $(x_0, y_0, x_1, y_1)$ | Kích thước điểm ảnh thực tế (px) | Chênh lệch RGB tối đa so với PDF gốc |
| :--- | :---: | :---: | :---: | :---: |
| `b-hinh-20-11.png` | 672 | `(38, 480, 405, 871)` | $734 \times 782$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-12.png` | 673 | `(398, 626, 591, 768)` | $386 \times 284$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-13.png` | 674 | `(154, 532, 599, 798)` | $890 \times 532$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-14.png` | 675 | `(352, 440, 522, 574)` | $340 \times 268$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-15.png` | 678 | `(215, 60, 575, 240)` | $720 \times 360$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-16.png` | 678 | `(398, 452, 592, 619)` | $388 \times 334$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-17.png` | 679 | `(398, 420, 592, 581)` | $388 \times 322$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-18.png` | 682 | `(38, 592, 302, 732)` | $528 \times 280$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-19.png` | 683 | `(186, 212, 573, 338)` | $774 \times 252$ | 0 (Khớp tuyệt đối) |
| `b-ung-dung-20-01.png` | 684 | `(398, 300, 592, 407)` | $388 \times 214$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-20.png` | 685 | `(188, 52, 523, 207)` | $670 \times 310$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-21.png` | 686 | `(418, 172, 578, 768)` | $320 \times 1192$ | 0 (Khớp tuyệt đối) |
| `b-hinh-20-22.png` | 687 | `(38, 624, 303, 754)` | $530 \times 260$ | 0 (Khớp tuyệt đối) |
| `b-ung-dung-20-02.png` | 688 | `(418, 412, 582, 722)` | $328 \times 620$ | 0 (Khớp tuyệt đối) |
| `b-tt-thuan-nghich.png` | 689 | `(465, 88, 592, 153)` | $254 \times 130$ | 0 (Khớp tuyệt đối) |
| `b-tt-dong-co-nhiet.png`| 689 | `(465, 276, 592, 341)` | $254 \times 130$ | 0 (Khớp tuyệt đối) |
| `b-tt-chu-trinh-otto.png`| 689 | `(465, 458, 592, 523)` | $254 \times 130$ | 0 (Khớp tuyệt đối) |
| `b-tt-may-lanh.png` | 689 | `(465, 626, 592, 696)` | $254 \times 140$ | 0 (Khớp tuyệt đối) |
| `b-tt-nguyen-ly-2.png` | 690 | `(465, 80, 592, 150)` | $254 \times 140$ | 0 (Khớp tuyệt đối) |
| `b-tt-chu-trinh-carnot.png`| 690 | `(465, 274, 592, 374)` | $254 \times 200$ | 0 (Khớp tuyệt đối) |
| `b-tt-vi-mo-entropy.png` | 690 | `(452, 650, 592, 730)` | $280 \times 160$ | 0 (Khớp tuyệt đối) |

- **Xử lý đặc thù hình 20.15**: Trong PDF trang 678, chú thích hình nằm ở cột trái dưới cùng, nhưng sơ đồ thực tế nằm ở góc trên cùng bên phải (`x=215..575, y=60..240`). Tọa độ đã được định vị chính xác và trích xuất trọn vẹn toàn bộ sơ đồ 3 khối nhiệt động học.
- **Xử lý hình 20.14**: Sơ đồ phác thảo dòng năng lượng trong Ví dụ 20.2 nằm tại tọa độ `(352, 440, 522, 574)` trang 675, đã trích xuất đầy đủ $Q_H, Q_C, W$.

---

## 5. Kết Quả Kiểm Thử Quy Chuẩn Toán Học (`measure-math.mjs`)

Lệnh kiểm thử quy chuẩn toán học từ kho StudyHub ưu tiên đã được chạy trên toàn bộ 5 tệp Markdown bài giảng:
```bash
node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . \
  raw_materials/physics/translations/chapter-20/05-nguyen-ly-thu-hai.md \
  raw_materials/physics/translations/chapter-20/06-chu-trinh-carnot.md \
  raw_materials/physics/translations/chapter-20/07-entropy.md \
  raw_materials/physics/translations/chapter-20/08-giai-thich-vi-mo-entropy.md \
  raw_materials/physics/translations/chapter-20/17-tom-tat.md
```

- **Mã thoát (Exit code)**: `0`
- **Số công thức hiển thị (Display equations)**: `79`
- **Số công thức nội dòng (Inline equations)**: `501`
- **Tổng số lỗi vi phạm (Findings count)**: `0`
- **Chi tiết tiêu chuẩn đạt được**:
  - 100% dấu phân cách `$$` bắt đầu tại cột 0 (column 0) trên dòng riêng biệt, không có thụt lề hay khoảng trắng thừa.
  - Không có công thức inline nào vượt quá $27\text{ex}$.
  - Không có công thức display nào vượt quá $25\text{ex}$. Toàn bộ các chuỗi biến đổi nhiều bước được tách dòng bằng `\begin{aligned}` với dấu căn lề `&=` đặt tại dấu quan hệ.
  - Không có liên kết cục bộ chứa đường dẫn máy tính (`file:///` hoặc `C:\Users`).
  - Không có dòng ký hiệu đô la đơn lẻ bị cô lập.

---

## 6. Lịch Sử Thực Thi Lệnh & Mã Thoát (Commands & Exits)

1. `python -X utf8 scripts/prepare-physics1-20-theory-b-assets.py`: **Mã thoát 0**. Trích xuất thành công 21/21 ảnh PNG.
2. `node -e "import('./docs/.vitepress/physics1-20-theory-b-image-annotations.mjs').then(...)"`: **Mã thoát 0**. Nạp thành công 21 khóa chú thích hình ảnh.
3. `node C:/.../measure-math.mjs`: **Mã thoát 0**. Đạt chuẩn 0 lỗi cú pháp toán.
4. `python -X utf8 raw_materials/physics/verify_chapter20_theory_b.py`: **Mã thoát 0**. Toàn bộ 10 hạng mục kiểm thử số học, điểm ảnh RGB và cú pháp toán học đều đạt trạng thái `PASS`.
5. `git status --short`: **Mã thoát 0**. Xác nhận chỉ có các tệp thuộc quyền sở hữu được thay đổi hoặc tạo mới.

---

## 7. Ranh Giới Phạm Vi & Ghi Chú Hoàn Thành (Scope Boundary & Status)

- **Các phần không thuộc phạm vi phân công**: Các bài tập cuối chương (*Discussion Questions, Exercises, Problems*) và phần *Guided Practice* trên trang PDF 690 không thuộc phạm vi nhiệm vụ lý thuyết B và được loại trừ theo đúng phân công.
- **Tích hợp Catalog**: Tệp chú thích hình ảnh được xuất ra dưới dạng module độc lập `docs/.vitepress/physics1-20-theory-b-image-annotations.mjs`, sẵn sàng để tệp catalog dùng chung nhập khẩu mà không gây xung đột sửa đổi đồng thời.
- **Quyền hạn & Quota**: Quota và DNS phân giải hoạt động bình thường, không gặp bất kỳ lỗi từ chối quyền hạn hay lỗi mạng nào.
- **Kết luận**: Toàn bộ nhiệm vụ lý thuyết B Chương 20 đã hoàn tất đầy đủ, chính xác, độc lập và trung thực.
