# Đánh giá Độc lập: physics1-20-exercises-c-20261022

Tài liệu rà soát và kiểm định độc lập cho gói bài tập Chương 20 (Định luật II nhiệt động lực học) theo kế hoạch `docs/agy-plans/2026-10-22-physics1-20-exercises-c.md`.

---

## 1. Thông tin chung và Phạm vi thực hiện

- **Mã nhiệm vụ**: `physics1-20-exercises-c-20261022`
- **Worktree cô lập**: `C:\Users\Ai\.codex\worktrees\physics1-20-exercises-c-20261022\StudyHub`
- **Commit gốc (HEAD)**: `82cab982f2efaf7e4d6f00863509054243449edc`
- **Tài liệu nguồn gốc**: Giáo trình *University Physics with Modern Physics* (Hugh D. Young & Roger A. Freedman, tái bản lần thứ 15), Chương 20: *The Second Law of Thermodynamics*.
- **Tổng số đơn vị bài tập**: Đúng 36 đơn vị bài tập độc lập:
  - 12 bài luyện tập có hướng dẫn (Video Practice / Practice Problems): `VP20.1.1` đến `VP20.10.4`.
  - 23 câu hỏi thảo luận định tính và nhận thức sâu (Discussion Questions): `Q20.1` đến `Q20.23`.
  - 1 Bài tập cầu nối toàn diện (Bridging Problem) tích hợp truyền nhiệt, biến đổi pha và tính biến thiên entropy của hệ cô lập.

---

## 2. Danh mục chi tiết 36 bài tập và Giá trị kiểm chứng

### 2.1. Luyện tập có hướng dẫn (12 bài - `09-luyen-tap-huong-dan.md`)
- **VP20.1.1**: Động cơ nhiệt vận hành theo chu trình. Cho $|Q_{\mathrm{H}}| = 5000\text{ J}$, hiệu suất $e = 0{,}28$.
  - Tính công sinh ra: $W = e |Q_{\mathrm{H}}| = 1400\text{ J}$.
  - Nhiệt lượng xả ra nguồn lạnh: $|Q_{\mathrm{C}}| = |Q_{\mathrm{H}}| - W = 3600\text{ J}$.
- **VP20.1.2**: Động cơ sinh công $W = 3200\text{ J}$ và xả nhiệt $|Q_{\mathrm{C}}| = 6800\text{ J}$.
  - Nhiệt lượng nhận từ nguồn nóng: $|Q_{\mathrm{H}}| = W + |Q_{\mathrm{C}}| = 10000\text{ J}$.
  - Hiệu suất nhiệt: $e = W / |Q_{\mathrm{H}}| = 0{,}32$ ($32{,}0\%$).
- **VP20.1.3**: Động cơ có hiệu suất $e = 0{,}35$, xả ra nguồn lạnh $|Q_{\mathrm{C}}| = 5200\text{ J}$.
  - Nhiệt lượng nhận từ nguồn nóng: $|Q_{\mathrm{H}}| = |Q_{\mathrm{C}}| / (1 - e) = 8000\text{ J}$.
  - Công sinh ra: $W = |Q_{\mathrm{H}}| - |Q_{\mathrm{C}}| = 2800\text{ J}$.
- **VP20.1.4**: Nhà máy nhiệt điện công suất cơ học $P = 500\text{ MW}$, hiệu suất $e = 0{,}38$.
  - Tốc độ nhận nhiệt nóng: $\mathrm{d}Q_{\mathrm{H}}/\mathrm{d}t = P / e \approx 1315{,}8\text{ MW}$.
  - Tốc độ thải nhiệt lạnh: $\mathrm{d}Q_{\mathrm{C}}/\mathrm{d}t = \mathrm{d}Q_{\mathrm{H}}/\mathrm{d}t - P \approx 815{,}8\text{ MW}$.
- **VP20.4.1**: Chu trình Otto lý tưởng có tỷ số nén $r = 8{,}50$, khí 2 nguyên tử ($\gamma = 1{,}40$).
  - Hiệu suất lý thuyết: $e = 1 - r^{1-\gamma} = 1 - 8{,}50^{-0{,}40} \approx 0{,}575$ ($57{,}5\%$).
- **VP20.4.2**: Động cơ Otto có $r = 9{,}20$, nhiệt nhận vào mỗi chu trình là $|Q_{\mathrm{H}}| = 850\text{ J}$.
  - Hiệu suất: $e = 1 - 9{,}20^{-0{,}40} \approx 0{,}588$.
  - Công thực hiện: $W = e |Q_{\mathrm{H}}| \approx 500\text{ J}$.
  - Nhiệt xả ra: $|Q_{\mathrm{C}}| = |Q_{\mathrm{H}}| - W \approx 350\text{ J}$.
- **VP20.4.3**: Thiết kế động cơ Otto cần đạt hiệu suất lý thuyết $e = 0{,}620$ ($\gamma = 1{,}40$).
  - Tỷ số nén yêu cầu: $r = (1 - e)^{1/(1-\gamma)} = (0{,}380)^{-2{,}5} \approx 11{,}15 \approx 11{,}2$.
- **VP20.4.4**: Chu trình Otto với khí đơn nguyên tử ($\gamma = 5/3 \approx 1{,}67$), tỷ số nén $r = 6{,}00$.
  - Hiệu suất: $e = 1 - 6{,}00^{-2/3} \approx 0{,}697$ ($69{,}7\%$).
- **VP20.10.1**: Làm nóng đẳng tích $0{,}250\text{ mol}$ khí lý tưởng đơn nguyên tử từ $300\text{ K}$ lên $600\text{ K}$.
  - $C_V = \frac{3}{2} R \approx 12{,}471\text{ J/(mol}\cdot\text{K)}$.
  - Biến thiên entropy: $\Delta S = n C_V \ln(T_2/T_1) \approx +2{,}16\text{ J/K}$.
- **VP20.10.2**: Giãn nở đẳng nhiệt thuận nghịch $0{,}500\text{ mol}$ khí lý tưởng từ $V_1 = 2{,}00\text{ L}$ lên $V_2 = 6{,}00\text{ L}$.
  - Biến thiên entropy: $\Delta S = n R \ln(V_2/V_1) \approx +4{,}57\text{ J/K}$.
- **VP20.10.3**: Làm nguội đẳng áp $0{,}300\text{ mol}$ khí lý tưởng lưỡng nguyên tử từ $500\text{ K}$ về $350\text{ K}$.
  - $C_p = \frac{7}{2} R \approx 29{,}100\text{ J/(mol}\cdot\text{K)}$.
  - Biến thiên entropy: $\Delta S = n C_p \ln(T_2/T_1) \approx -3{,}11\text{ J/K}$.
- **VP20.10.4**: Giãn nở tự do đoạn nhiệt (giãn nở Joule) $1{,}00\text{ mol}$ khí lý tưởng vào chân không, thể tích tăng gấp 3 lần.
  - Do $Q = 0, W = 0 \implies \Delta U = 0 \implies T_2 = T_1$.
  - Trạng thái đầu và cuối trùng với quá trình giãn nở đẳng nhiệt.
  - Biến thiên entropy: $\Delta S = n R \ln(V_2/V_1) = 1{,}00 \times 8{,}314 \times \ln(3) \approx +9{,}13\text{ J/K} > 0$.

### 2.2. Câu hỏi thảo luận định tính (23 câu - `10-cau-hoi-thao-luan.md`)
- **Q20.1**: Chiều mũi tên thời gian nhiệt động lực học và các quá trình một chiều tự nhiên.
- **Q20.2**: Tính thuận nghịch cơ học lý tưởng so với tính bất thuận nghịch do ma sát và tiêu tán nhiệt.
- **Q20.3**: Phân tích phát biểu Kelvin–Planck: Tại sao không thể chuyển hóa toàn bộ nhiệt thành công tuần hoàn mà không xả nhiệt.
- **Q20.4**: So sánh nguyên lý biến đổi cơ năng thành nhiệt ($100\%$) và nhiệt thành cơ năng ($<100\%$).
- **Q20.5**: Phân tích phát biểu Clausius: Nhiệt không thể tự truyền từ vật lạnh sang vật nóng mà không có ngoại công.
- **Q20.6**: Máy lạnh xả nhiệt ra môi trường: Tại sao mở cửa tủ lạnh trong phòng kín lại làm phòng nóng lên.
- **Q20.7**: Động cơ nhiệt chạy bằng nước biển bề mặt ấm và đáy biển lạnh: Tính khả thi nhiệt động lực học (công nghệ OTEC) và giới hạn Carnot.
- **Q20.8**: Chu trình Otto và hiện tượng nổ sớm (kích nổ) do nhiệt độ cuối kỳ nén vượt quá nhiệt độ tự bốc cháy của nhiên liệu.
- **Q20.9**: So sánh động cơ Diesel và Otto: Tỷ số nén cao hơn của Diesel và lý do không kích nổ khi chỉ nén không khí.
- **Q20.10**: Động cơ Stirling: Khả năng đạt hiệu suất Carnot lý thuyết bằng tái sinh nhiệt và thách thức kỹ thuật truyền nhiệt.
- **Q20.11**: Định lý Carnot: Hiệu suất cực đại phụ thuộc duy nhất vào nhiệt độ hai nguồn nhiệt, độc lập với tác nhân công tác.
- **Q20.12**: Ý nghĩa nhiệt động lực học của độ không tuyệt đối ($0\text{ K}$) và định luật thứ ba nhiệt động lực học.
- **Q20.13**: Máy bơm nhiệt (Heat Pump): Hệ số hiệu năng COP sưởi ấm $K_{\text{sưởi}} = K_{\text{làm lạnh}} + 1 > 1$, ưu thế vượt trội so với sưởi điện trở.
- **Q20.14**: Entropy và mức độ vô trật tự phân tử vi mô; liên hệ với số vi trạng thái Boltzmann $S = k \ln W$.
- **Q20.15**: Giãn nở đoạn nhiệt tự do: $Q = 0$ nhưng $\Delta S > 0$ do tính bất thuận nghịch tuyệt đối của quá trình.
- **Q20.16**: Quá trình kết tinh và đóng băng: Entropy của chất lỏng giảm ($\Delta S < 0$), nhưng entropy môi trường tăng nhiều hơn, bảo toàn $\Delta S_{\text{vũ trụ}} > 0$.
- **Q20.17**: Sự sống và định luật II nhiệt động lực học: Sinh vật là hệ mở tiêu thụ năng lượng tự do để giảm entropy nội tại.
- **Q20.18**: Hòa trộn hai chất khí lý tưởng giống hệt nhau ở cùng nhiệt độ, áp suất (Nghịch lý Gibbs) và sự khác biệt khi hòa trộn hai khí khác nhau.
- **Q20.19**: Truyền nhiệt qua chênh lệch nhiệt độ hữu hạn: $\Delta S = Q(1/T_2 - 1/T_1) > 0$ vì $T_1 > T_2$.
- **Q20.20**: So sánh chu trình thuận nghịch và bất thuận nghịch cùng làm việc giữa hai nguồn nhiệt.
- **Q20.21**: Trực giác về entropy trong biến đổi trạng thái pha đẳng nhiệt: Tại sao chuyển pha thu nhiệt làm entropy tăng vọt.
- **Q20.22**: Động cơ vĩnh cửu loại 1 (vi phạm Định luật I) và loại 2 (vi phạm Định luật II).
- **Q20.23**: "Cái chết nhiệt" của vũ trụ (Heat Death): Trạng thái cân bằng nhiệt tối đa, entropy cực đại và không còn khả năng sinh công.

### 2.3. Bài tập cầu nối (1 bài - `16-bai-tap-cau-noi.md`)
- **Tóm tắt bài toán**: $0{,}600\text{ kg}$ nước ở $45{,}0^\circ\text{C}$ trộn với $0{,}0500\text{ kg}$ nước đá ở $-15{,}0^\circ\text{C}$ trong bình cách nhiệt.
- **Hằng số**: $c_{\mathrm{w}} = 4190\text{ J/(kg}\cdot\text{K)}$, $c_{\mathrm{i}} = 2100\text{ J/(kg}\cdot\text{K)}$, $L_f = 3{,}34 \times 10^5\text{ J/kg}$.
- **Phần (a)**:
  - $Q_1 = m_{\mathrm{i}} c_{\mathrm{i}} (0{,}0 - T_{\mathrm{i}}) = 1575\text{ J}$.
  - $Q_2 = m_{\mathrm{i}} L_f = 16700\text{ J}$.
  - $Q_{\text{thu}} = Q_1 + Q_2 = 18275\text{ J}$.
  - $Q_{\text{tỏa}} = m_{\mathrm{w}} c_{\mathrm{w}} (45{,}0 - 0{,}0) = 113130\text{ J} > Q_{\text{thu}} \implies$ Nước đá tan hoàn toàn.
  - Cân bằng nhiệt: $T = \frac{m_{\mathrm{w}} c_{\mathrm{w}} (45{,}0) - Q_{\text{thu}}}{(m_{\mathrm{w}} + m_{\mathrm{i}}) c_{\mathrm{w}}} \approx 34{,}8^\circ\text{C}$ ($307{,}98\text{ K}$).
- **Phần (b)**:
  - $\Delta S_1 = m_{\mathrm{i}} c_{\mathrm{i}} \ln(273{,}15 / 258{,}15) \approx +5{,}93\text{ J/K}$.
  - $\Delta S_2 = m_{\mathrm{i}} L_f / 273{,}15 \approx +61{,}14\text{ J/K}$.
  - $\Delta S_3 = m_{\mathrm{i}} c_{\mathrm{w}} \ln(307{,}98 / 273{,}15) \approx +25{,}14\text{ J/K}$.
  - $\Delta S_{\mathrm{i}} = \Delta S_1 + \Delta S_2 + \Delta S_3 \approx +92{,}21\text{ J/K}$.
  - $\Delta S_{\mathrm{w}} = m_{\mathrm{w}} c_{\mathrm{w}} \ln(307{,}98 / 318{,}15) \approx -81{,}69\text{ J/K}$.
  - $\Delta S_{\text{hệ}} = \Delta S_{\mathrm{i}} + \Delta S_{\mathrm{w}} \approx +10\text{ J/K}$ (giá trị chính xác: $+10{,}52\text{ J/K}$).
- **Bảo toàn cấu trúc Solution Guide**: Giữ đúng đầy đủ 7 bước hướng dẫn nhận diện, thiết lập, thực thi và đánh giá.

---

## 3. Kiểm định Tài sản Hình ảnh & Biên điểm ảnh (Image Crop Audit)

Tất cả 4 tệp hình ảnh được trích xuất trực tiếp từ file PDF nguồn chất lượng cao bằng `PyMuPDF` với hệ số phóng đại `scale = 3.0`, không gian màu RGB thuần (`alpha = False`):

| Tên tệp ảnh | Trang PDF | Tọa độ trích xuất `(x0, y0, x1, y1)` | Kích thước (px) | Biên trắng (Edge non-white px) | Nội dung |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `c-hinh-20-23.png` | 691 | `(65.0, 78.0, 323.0, 220.0)` | $774 \times 426$ | T: 0, B: 0, L: 0, R: 0 | Hỗn hợp nước đá – nước (Hình 20.23) |
| `c-hinh-20-06.png` | 668 | `(372.0, 480.0, 536.0, 702.0)` | $492 \times 666$ | T: 0, B: 0, L: 0, R: 0 | Đồ thị pV chu trình Otto (Hình 20.6) |
| `c-hinh-20-09.png` | 670 | `(66.0, 474.0, 566.0, 738.0)` | $1500 \times 792$ | T: 0, B: 0, L: 0, R: 0 | Sơ đồ năng lượng máy lạnh (Hình 20.9) |
| `c-hinh-20-13.png` | 674 | `(66.0, 470.0, 471.0, 736.0)` | $1215 \times 798$ | T: 0, B: 0, L: 0, R: 0 | Chu trình Carnot trên đồ thị pV (Hình 20.13) |

- **Kết quả kiểm tra biên**: Cả 4 ảnh đều có 0 điểm ảnh phi trắng trên toàn bộ 4 cạnh (trên, dưới, trái, phải). Không có bất kỳ hiện tượng cắt lẹm đồ họa hay viền đen.
- **Chú thích ảnh**: Mỗi hình đều có chú thích tiếng Việt chuẩn mực đặt ngay dưới ảnh, giải nghĩa toàn bộ thuật ngữ tiếng Anh gốc.

---

## 4. Nhật ký Thực thi Lệnh Kiểm tra (Verification Execution Log)

| Lệnh thực thi | Mã thoát (Exit code) | Kết quả kiểm tra |
| :--- | :--- | :--- |
| `C:/Users/Ai/miniconda3/python.exe -X utf8 scripts/prepare-physics1-20-exercises-c-assets.py` | `0` | Trích xuất thành công 4 ảnh PNG đạt chuẩn chất lượng cao. |
| `C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter20_exercises_c.py` | `0` | Xác minh thành công 12 bài VP, 23 bài Q, 1 bài Bridging và 4 ảnh PNG. |
| `node qa/physics1-priority/measure-math.mjs . raw_materials/physics/translations/chapter-20/09-luyen-tap-huong-dan.md raw_materials/physics/translations/chapter-20/10-cau-hoi-thao-luan.md raw_materials/physics/translations/chapter-20/16-bai-tap-cau-noi.md` | `0` | **Passed**: 110 công thức display $\le 25\text{ex}$, 483 công thức inline $\le 27\text{ex}$, 0 findings. |
| `node -e "import('./docs/.vitepress/physics1-20-exercises-c-image-annotations.mjs')..."` | `0` | Import thành công 4 mục chú thích hình ảnh. |

---

## 5. Danh mục 7 Tệp thuộc Quyền Sở hữu (Exact Owned Files)

1. `raw_materials/physics/translations/chapter-20/09-luyen-tap-huong-dan.md`
2. `raw_materials/physics/translations/chapter-20/10-cau-hoi-thao-luan.md`
3. `raw_materials/physics/translations/chapter-20/16-bai-tap-cau-noi.md`
4. `scripts/prepare-physics1-20-exercises-c-assets.py`
5. `docs/.vitepress/physics1-20-exercises-c-image-annotations.mjs`
6. `raw_materials/physics/verify_chapter20_exercises_c.py`
7. `raw_materials/physics/reviews/ch20-agy-exercises-c-review.md`

Tài sản hình ảnh đi kèm (tiền tố `c-` duy nhất):
- `docs/vat-ly-1/bai-giang/img/young-20/c-hinh-20-06.png`
- `docs/vat-ly-1/bai-giang/img/young-20/c-hinh-20-09.png`
- `docs/vat-ly-1/bai-giang/img/young-20/c-hinh-20-13.png`
- `docs/vat-ly-1/bai-giang/img/young-20/c-hinh-20-23.png`

---

## 6. Tuân thủ Quy chuẩn Định dạng và Văn phong StudyHub

- **Định dạng toán học**:
  - Không có công thức display nào vượt quá $25\text{ex}$.
  - Không có công thức inline nào vượt quá $27\text{ex}$.
  - Mọi dấu `$$` mở và đóng đều nằm độc lập trên dòng riêng ở cột 0 (`column 0`).
  - Không ngắt dòng giữa các toán tử cộng/trừ; chỉ bẻ dòng ở dấu quan hệ đẳng thức/bất đẳng thức trong môi trường `aligned`.
- **Văn phong tiếng Việt**:
  - Viết hoa chữ cái đầu tiên ngay sau dấu hai chấm (`:`).
  - Không sử dụng các từ ngữ suy đoán cảm tính AI hoặc lối viết nháp "nghĩ thành tiếng".
  - Tiếng Việt tự nhiên, chuẩn mực học thuật, câu văn gãy gọn và giàu tính sư phạm.
- **Ranh giới công việc**: Không chạm vào bất kỳ tệp nào ngoài danh sách 7 tệp sở hữu; không build toàn cục; không commit hay đẩy lên remote.
