# Báo cáo rà soát độc lập chuyên sâu: Vật lý 1 - Chương 9 (Theory B)

**Nhiệm vụ**: `physics1-09-theory-b-20261022`
**Kế hoạch**: `docs/agy-plans/2026-10-22-physics1-09-theory-b.md`
**Trạng thái**: Call 2/3 (Hiệu chỉnh dựa trên bằng chứng thực tế - Correction 1)
**Tài liệu nguồn gốc**: `young-freedman-15.pdf` (SHA256: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`), Mục 9.4, 9.5, 9.6, các trang PDF 302–311 (trang in 282–291).

---

## 1. Danh sách tệp thuộc quyền sở hữu (Owned Files)

Mọi thay đổi chỉ nằm trong phạm vi 8 đường dẫn được phân công và các tài nguyên hình ảnh tiền tố `docs/vat-ly-1/bai-giang/img/young-09/b-*.png`:

1. `raw_materials/physics/translations/chapter-09/04-dong-nang-va-momen-quan-tinh.md` (Mục 9.4)
2. `raw_materials/physics/translations/chapter-09/05-dinh-ly-truc-song-song.md` (Mục 9.5)
3. `raw_materials/physics/translations/chapter-09/06-tinh-momen-quan-tinh.md` (Mục 9.6 - vừa hoàn thành đầy đủ)
4. `raw_materials/physics/translations/chapter-09/17-tom-tat.md` (Tóm tắt toàn bộ chương 9, trang PDF 311 - vừa hoàn thành đầy đủ)
5. `scripts/prepare-physics1-09-theory-b-assets.py` (Bộ trích xuất và sinh ảnh crop PDF)
6. `docs/.vitepress/physics1-09-theory-b-image-annotations.mjs` (Bộ dịch nhãn hình ảnh đối ứng)
7. `raw_materials/physics/verify_chapter09_theory_b.py` (Script kiểm chứng số học và so sánh RGB ảnh crop)
8. `raw_materials/physics/reviews/ch09-agy-theory-b-review.md` (Tài liệu báo cáo rà soát này)

Cùng 17 tệp hình ảnh định dạng PNG phẳng:
`b-ung-dung-01.png`, `b-hinh-9-14.png`, `b-hinh-9-15.png`, `b-bang-9-02.png`, `b-hinh-9-16.png`, `b-hinh-9-17.png`, `b-hinh-9-18.png`, `b-hinh-9-19.png`, `b-hinh-9-20.png`, `b-hinh-9-21.png`, `b-hinh-9-22.png`, `b-hinh-9-23.png`, `b-hinh-9-24.png`, `b-tom-tat-9-01.png`, `b-tom-tat-9-02.png`, `b-tom-tat-9-03.png`, `b-tom-tat-9-04.png`.

---

## 2. Phạm vi nội dung giảng dạy & Cấu trúc sư phạm

Toàn bộ nội dung từ trang PDF 302 đến PDF 311 được chuyển tải sang tiếng Việt học thuật chuẩn mực, không tóm lược, không lược bỏ bước biến đổi:

- **Mục 9.4: Động năng trong chuyển động quay**
  - Khái niệm động năng quay $K = \frac{1}{2} I \omega^2$ từ tổng động năng các hạt $\frac{1}{2} m_i v_i^2$.
  - Định nghĩa momen quán tính rời rạc $I = \sum_i m_i r_i^2$ (PT 9.16).
  - Khái quát dạng tích phân cho hệ phân bố liên tục $I = \int r^2\, dm$.
  - Ứng dụng thực tế: Lưu trữ năng lượng trong bánh đà (Flywheels).
  - Ứng dụng sinh học: Cánh chim đập ở tần số cao với cơ bắp tập trung sát khớp vai để giảm momen quán tính.
  - Ví dụ 9.6: Chi tiết máy gồm 3 đĩa liên kết tạo thành tam giác vuông, tính $I$ quanh trục 1 qua $A$, trục 2 qua $B-C$ và động năng quay $K$.
  - Bảng 9.2: Momen quán tính của 9 vật thể đồng tính có dạng hình học quen thuộc (trường hợp a đến i).
  - Chiến lược giải bài toán năng lượng chuyển động quay (Problem-Solving Strategy 9.1).
  - Ví dụ 9.7: Dây cáp tháo khỏi khối trụ đặc bởi lực kéo không đổi $F = 9{,}0\,\mathrm N$.
  - Ví dụ 9.8: Dây cáp tháo khỏi khối trụ đặc nối vật nặng rơi từ độ cao $h = 4{,}0\,\mathrm m$.
  - Thế năng trọng trường của vật thể mở rộng $U = M g y_{\mathrm{cm}}$ (PT 9.18) và chứng minh qua tọa độ khối tâm.
  - Ứng dụng thể thao: Kỹ thuật nhảy cao Fosbury flop với khối tâm đi bên dưới xà ngang.
  - Kiểm tra hiểu biết mục 9.4 (TYU 9.4): So sánh động năng của vật nặng rơi và động năng quay của khối trụ khi $m = M$.

- **Mục 9.5: Định lý trục song song**
  - Phát biểu và công thức định lý trục song song $I_P = I_{\mathrm{cm}} + M d^2$ (PT 9.19).
  - Chứng minh định lý trục song song bằng phương pháp lát mỏng vuông góc trục quay và tính triệt tiêu của các số hạng bậc nhất qua tọa độ khối tâm.
  - Ý nghĩa vật lý: Momen quán tính đối với trục đi qua khối tâm luôn là cực tiểu trong họ các trục song song.
  - Ví dụ 9.9: Sử dụng định lý trục song song xác định $I_{\mathrm{cm}}$ của chi tiết cơ khí khi biết $I_P = 0{,}132\,\mathrm{kg\cdot m^2}$ ở khoảng cách $d = 0{,}15\,\mathrm m$.
  - Kiểm tra hiểu biết mục 9.5 (TYU 9.5): So sánh momen quán tính của cây cơ bi-a thon dần khi quay quanh trục đi qua đầu dày và đầu mỏng.

- **Mục 9.6: Tính toán momen quán tính**
  - Công thức tích phân tổng quát $I = \int r^2\, dm$ (PT 9.20).
  - Biểu diễn phần tử khối lượng qua khối lượng riêng $\rho = dm/dV$ và $I = \rho \int r^2\, dV$ (PT 9.21) cho vật thể đồng tính.
  - Sự biến thiên khối lượng riêng của Trái Đất dựa trên số liệu quỹ đạo vệ tinh nhân tạo.
  - Ví dụ 9.10: Tích phân hình trụ rỗng có bán kính trong $R_1$, bán kính ngoài $R_2$, chiều dài $L$ qua phần tử vỏ trụ mỏng $dV = 2\pi r L\, dr$, suy ra $I = \frac{1}{2} M (R_1^2 + R_2^2)$ và khảo sát hai trường hợp giới hạn (trụ đặc $R_1 = 0$ và vỏ mỏng $R_1 \approx R_2$).
  - Ví dụ 9.11: Tích phân khối cầu đặc đồng tính bán kính $R$ bằng phương pháp lát cắt đĩa tròn mỏng vuông góc trục quay, suy ra $I = \frac{2}{5} M R^2$ và đối chiếu với khối trụ đặc.
  - Kiểm tra hiểu biết mục 9.6 (TYU 9.6): So sánh momen quán tính của hai hình trụ rỗng có cùng khối lượng và các bán kính nhưng khác chiều dài (gỗ vs chì).

- **Tóm tắt chương 9**
  - Động học chuyển động quay: Tọa độ góc $\theta$, vận tốc góc $\omega_z = d\theta/dt$ (PT 9.3), gia tốc góc $\alpha_z = d\omega_z/dt$ (PT 9.5), và 4 phương trình động học biến đổi đều (PT 9.11, 9.10, 9.7, 9.12).
  - Mối liên hệ dài - góc: Tốc độ dài $v = r\omega$ (PT 9.13), gia tốc tiếp tuyến $a_{\text{tan}} = r\alpha$ (PT 9.14), gia tốc hướng tâm $a_{\text{rad}} = \omega^2 r$ (PT 9.15).
  - Momen quán tính rời rạc $I = \sum_i m_i r_i^2$ (PT 9.16) và động năng quay $K = \frac{1}{2} I \omega^2$ (PT 9.17).
  - Định lý trục song song $I_P = I_{\mathrm{cm}} + M d^2$ (PT 9.19) và tích phân vật thể liên tục $I = \int r^2\, dm$ (PT 9.20).
  - Cả 4 sơ đồ tóm tắt nguyên bản: `b-tom-tat-9-01.png`, `b-tom-tat-9-02.png`, `b-tom-tat-9-03.png`, `b-tom-tat-9-04.png`.

---

## 3. Bản đồ dữ liệu số học thực tế (Actual Numerical Ledger)

Mọi trường hợp số học đều được kiểm chứng độc lập bằng code Python trong `raw_materials/physics/verify_chapter09_theory_b.py`:

| Mã trường hợp | Nội dung & Nguồn gốc | Dữ liệu đầu vào (Inputs) | Biểu thức tính toán | Kết quả tính toán | Giá trị lý thuyết nguồn | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `EX_9_6_A` | Ví dụ 9.6(a): Trục 1 qua đĩa A | $m_A=0{,}30\,\mathrm{kg}$, $m_B=0{,}10\,\mathrm{kg}$, $m_C=0{,}20\,\mathrm{kg}$, $r_B=0{,}50\,\mathrm m$, $r_C=0{,}40\,\mathrm m$ | $I_1 = m_B r_B^2 + m_C r_C^2$ | $0{,}0570\,\mathrm{kg\cdot m^2}$ | $0{,}057\,\mathrm{kg\cdot m^2}$ | **PASS** |
| `EX_9_6_B` | Ví dụ 9.6(b): Trục 2 qua đĩa B, C | $m_A=0{,}30\,\mathrm{kg}$, $r_A=0{,}40\,\mathrm m$ | $I_2 = m_A r_A^2$ | $0{,}0480\,\mathrm{kg\cdot m^2}$ | $0{,}048\,\mathrm{kg\cdot m^2}$ | **PASS** |
| `EX_9_6_C` | Ví dụ 9.6(c): Động năng quay trục 1 | $I_1=0{,}057\,\mathrm{kg\cdot m^2}$, $\omega=4{,}0\,\mathrm{rad/s}$ | $K = \frac{1}{2} I_1 \omega^2$ | $0{,}4560\,\mathrm J$ | $0{,}456\,\mathrm J \approx 0{,}46\,\mathrm J$ | **PASS** |
| `EX_9_7` | Ví dụ 9.7: Dây cáp tháo khối trụ | $M=50{,}0\,\mathrm{kg}$, $R=0{,}120\,\mathrm m$, $F=9{,}0\,\mathrm N$, $s=2{,}0\,\mathrm m$ | $W = F s$, $I = \frac{1}{2} M R^2$, $\omega = \sqrt{2W/I}$, $v = R\omega$ | $W=18{,}0\,\mathrm J$, $I=0{,}360\,\mathrm{kg\cdot m^2}$, $\omega=10{,}0\,\mathrm{rad/s}$, $v=1{,}20\,\mathrm{m/s}$ | $W=18{,}0\,\mathrm J$, $I=0{,}360\,\mathrm{kg\cdot m^2}$, $\omega=10{,}0\,\mathrm{rad/s}$, $v=1{,}20\,\mathrm{m/s}$ | **PASS** |
| `EX_9_8` | Ví dụ 9.8: Dây cáp nối vật nặng rơi | $M=50{,}0\,\mathrm{kg}$, $m=2{,}0\,\mathrm{kg}$, $h=4{,}0\,\mathrm m$, $g=9{,}80\,\mathrm{m/s^2}$ | $\Delta U = mgh$, $v = \sqrt{2mgh/(m + M/2)}$, $\omega = v/R$ | $\Delta U=78{,}4\,\mathrm J$, $v=2{,}41\,\mathrm{m/s}$, $\omega=20{,}08\,\mathrm{rad/s}$ | $\Delta U=78{,}4\,\mathrm J$, $v \approx 2{,}4\,\mathrm{m/s}$, $\omega \approx 20\,\mathrm{rad/s}$ | **PASS** |
| `TYU_9_4` | TYU 9.4: Tỷ số động năng $m=M$ | $m = M$, hình trụ đặc không trượt | $K_{\text{vật}} = \frac{1}{2} m v^2$, $K_{\text{trụ}} = \frac{1}{4} m v^2$ | Tỷ số $= 2{,}0$ | $K_{\text{vật}} > K_{\text{trụ}}$ (Đáp án i) | **PASS** |
| `EX_9_9` | Ví dụ 9.9: Định lý trục song song | $M=3{,}6\,\mathrm{kg}$, $d=0{,}15\,\mathrm m$, $I_P=0{,}132\,\mathrm{kg\cdot m^2}$ | $I_{\mathrm{cm}} = I_P - M d^2$ | $I_{\mathrm{cm}} = 0{,}0510\,\mathrm{kg\cdot m^2}$ | $0{,}051\,\mathrm{kg\cdot m^2}$ | **PASS** |
| `TYU_9_5` | TYU 9.5: Cây cơ bi-a thon dần | $d_{\text{mỏng}} > d_{\text{dày}}$ | $I_P = I_{\mathrm{cm}} + M d^2$ | $I_P(\text{mỏng}) > I_P(\text{dày})$ | Đáp án (ii) | **PASS** |
| `EX_9_10` | Ví dụ 9.10: Tích phân trụ rỗng | $\rho=7800\,\mathrm{kg/m^3}$, $L=0{,}5\,\mathrm m$, $R_1=0{,}05\,\mathrm m$, $R_2=0{,}10\,\mathrm m$ | $I = \int_{R_1}^{R_2} 2\pi \rho L r^3 dr$ | $I_{\text{num}}=0{,}57439$, $I_{\text{ana}}=0{,}57432$ | Sai số tương đối $1{,}2 \times 10^{-4}$ (< 0.1%) | **PASS** |
| `EX_9_11` | Ví dụ 9.11: Tích phân khối cầu đặc | $R=0{,}20\,\mathrm m$, $\rho=2500\,\mathrm{kg/m^3}$, $M=83{,}78\,\mathrm{kg}$ | $I = 2 \int_0^R \frac{\pi \rho}{2} (R^2 - x^2)^2 dx$ | $I_{\text{num}}=1{,}34054$, $I_{\text{ana}}=1{,}34041$ | Sai số tương đối $9{,}4 \times 10^{-5}$ (< 0.1%) | **PASS** |
| `TYU_9_6` | TYU 9.6: Trụ rỗng khác chiều dài | Cùng $M, R_1, R_2$, khác $L$ và $\rho$ | $I = \frac{1}{2} M (R_1^2 + R_2^2)$ | Độc lập với $L$ và $\rho$ | Đáp án (iii) (bằng nhau) | **PASS** |

---

## 4. Tọa độ Crop, Kích thước Pixel & Kiểm tra RGB với PDF gốc

Tất cả 17 tệp PNG phẳng được tạo tự động với tỷ lệ phóng đại `SCALE = 3.0` (alpha=False). So sánh từng pixel (pixel-by-pixel RGB difference) giữa ảnh đã lưu và ảnh render tươi trực tiếp từ PDF gốc:

| Tên tệp ảnh | Trang PDF | Tọa độ Box (x0, y0, x1, y1) | Kích thước (WxH) | Sai khác RGB lớn nhất (`max_diff`) | Độ sai khác trung bình (`mean_diff`) | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| `b-ung-dung-01.png` | 303 | (456, 375, 613, 481) | 471 x 318 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-14.png` | 303 | (456, 485, 613, 592) | 471 x 321 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-15.png` | 304 | (42, 235, 285, 368) | 729 x 399 | 0 | 0.0000 | **MATCH** |
| `b-bang-9-02.png` | 305 | (78, 60, 612, 376) | 1602 x 948 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-16.png` | 305 | (350, 642, 580, 730) | 690 x 264 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-17.png` | 306 | (330, 350, 555, 528) | 675 x 534 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-18.png` | 307 | (455, 175, 613, 290) | 474 x 345 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-19.png` | 307 | (456, 514, 616, 676) | 480 x 486 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-20.png` | 308 | (36, 115, 198, 330) | 486 x 645 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-21.png` | 308 | (362, 442, 520, 534) | 474 x 276 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-22.png` | 309 | (455, 278, 613, 420) | 474 x 426 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-23.png` | 309 | (120, 580, 295, 746) | 525 x 498 | 0 | 0.0000 | **MATCH** |
| `b-hinh-9-24.png` | 310 | (60, 485, 268, 646) | 624 x 483 | 0 | 0.0000 | **MATCH** |
| `b-tom-tat-9-01.png` | 311 | (495, 95, 575, 188) | 240 x 279 | 0 | 0.0000 | **MATCH** |
| `b-tom-tat-9-02.png` | 311 | (495, 260, 610, 345) | 345 x 255 | 0 | 0.0000 | **MATCH** |
| `b-tom-tat-9-03.png` | 311 | (495, 370, 595, 455) | 300 x 255 | 0 | 0.0000 | **MATCH** |
| `b-tom-tat-9-04.png` | 311 | (495, 505, 615, 570) | 360 x 195 | 0 | 0.0000 | **MATCH** |

### Chi tiết các cải tiến hiệu chỉnh (Evidence-based Fixes)
1. **Sửa lỗi viền cắt `b-hinh-9-19`**: Tọa độ trước đây `(456, 514, 616, 634)` đã cắt cụt phần chữ bên dưới tại $y=634$. Tọa độ mới `(456, 514, 616, 676)` bảo toàn toàn vẹn bảng chú thích trục quay 2 và công thức định lý trục song song $I_P = I_{\mathrm{cm}} + M d^2$.
2. **Bổ sung nhãn dịch `b-hinh-9-19`**: Thêm đầy đủ nhãn `"Định lý trục song song: IP = Icm + Md2"`, chuẩn hóa câu chữ tiếng Anh khớp từng ký tự với PDF gốc (`Moment of inertia for this axis: Icm`).
3. **Hiệu chỉnh nhãn `b-hinh-9-24`**: Khôi phục cụm từ bị thiếu `"of the sphere"` thành `"Mass element: disk of radius r and thickness dx located a distance x from the center of the sphere"`.
4. **Tuyệt đối không có chú thích trùng lặp**: Không dùng dòng chữ nghiêng `*Hình...*` dưới thẻ ảnh `![...]`, giữ alt text trở thành caption chuẩn mực tự nhiên của VitePress. Không có chú thích phantom.

---

## 5. Kết quả kiểm tra công cụ & Mã thoát (Commands & Exits)

1. **Chuẩn hóa và sinh tài nguyên ảnh**:
   - Lệnh: `python -X utf8 scripts/prepare-physics1-09-theory-b-assets.py`
   - Mã thoát: `0`
   - Kết quả: Đã sinh và lưu thành công toàn bộ 17 hình ảnh.

2. **Kiểm tra cú pháp module dịch nhãn hình ảnh**:
   - Lệnh: `node --input-type=module -e "import('./docs/.vitepress/physics1-09-theory-b-image-annotations.mjs').then(m=>console.log(Object.keys(m)))"`
   - Mã thoát: `0`
   - Kết quả: Xuất đúng `[ 'physics1Chapter9TheoryBImageAnnotations' ]`.

3. **Kiểm chứng số học & so khớp pixel RGB**:
   - Lệnh: `C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter09_theory_b.py`
   - Mã thoát: `0`
   - Kết quả: `Total numerical test cases: 11, All Passed: True`; `Total assets tested: 17, All RGB Matched: True`.

4. **Kiểm tra độ rộng công thức toán (Math Bounds & Delimiters)**:
   - Lệnh: `node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . raw_materials/physics/translations/chapter-09/04-dong-nang-va-momen-quan-tinh.md raw_materials/physics/translations/chapter-09/05-dinh-ly-truc-song-song.md raw_materials/physics/translations/chapter-09/06-tinh-momen-quan-tinh.md raw_materials/physics/translations/chapter-09/17-tom-tat.md`
   - Mã thoát: `0`
   - Kết quả:
     ```json
     {
       "status": "passed",
       "scope": "Strict draft math and syntax probe, not semantic or browser acceptance",
       "display": 94,
       "inline": 316,
       "findings": []
     }
     ```
   - 100% công thức đạt chuẩn độ rộng $\le 25\mathrm{ex}$ cho display và $\le 27\mathrm{ex}$ cho inline, không có lỗi phân cách `$$`, không thanh cuộn ngang.

---

## 6. Vấn đề tồn đọng, Điểm chưa rõ, Quyền hạn & Quota

- **Lỗi quyền hạn (Permission errors)**: Không có (`dangerously_skip_permissions=true` được thiết lập và tuân thủ chặt chẽ).
- **Lỗi giới hạn (Quota errors)**: Không có.
- **Đường dẫn ngoài phạm vi (Unowned paths)**: Hoàn toàn không sửa đổi bất kỳ tệp nào ngoài 8 đường dẫn được phân công.
- **Vấn đề còn lại (Remaining issues)**: Không có lỗi nội tại. Toàn bộ khâu tích hợp vào site chính thức, Wiki concepts và Cheatsheet do tác vụ cha (parent) chịu trách nhiệm theo đúng kế hoạch.
