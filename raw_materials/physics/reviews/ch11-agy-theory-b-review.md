# Báo Cáo Thẩm Định & Nghiệm Thu Bài Giảng: Vật Lý 1 — Chương 11 (Phần B)

**Mã công việc**: `physics1-11-theory-b-20261022`
**Kế hoạch thực hiện**: `docs/agy-plans/2026-10-22-physics1-11-theory-b.md`
**Lượt thực hiện**: Lượt 3 / 3 (Hoàn thiện nghiệm thu độc lập)
**Phạm vi chuyên môn**: Giáo trình Sears & Zemansky's University Physics (15th ed.), Chương 11 — Các Mục 11.4, 11.5 (trang PDF 365–373) và Toàn bộ Tóm tắt Chương 11 (trang PDF 373).

---

## 1. Danh Mục Tệp Thuộc Quyền Sở Hữu Độc Quyền (Exclusive Ownership)

Toàn bộ các tệp được chỉ định đã hoàn tất, lưu trực tiếp vào không gian làm việc cục bộ và không can thiệp vào bất kỳ tệp hệ thống/dự án dùng chung nào:

1. `raw_materials/physics/translations/chapter-11/04-ung-suat-bien-dang-modun.md` (Mục 11.4: Ứng suất, Biến dạng và Modun đàn hồi)
2. `raw_materials/physics/translations/chapter-11/05-dan-hoi-va-deo.md` (Mục 11.5: Tính đàn hồi và Tính dẻo)
3. `raw_materials/physics/translations/chapter-11/17-tom-tat.md` (Tóm tắt toàn diện Chương 11)
4. `scripts/prepare-physics1-11-theory-b-assets.py` (Script trích xuất 15 ảnh từ PDF gốc)
5. `docs/.vitepress/physics1-11-theory-b-image-annotations.mjs` (Module chú thích nhãn ảnh song ngữ cho 15 ảnh)
6. `raw_materials/physics/verify_chapter11_theory_b.py` (Script kiểm thử số học và so sánh RGB pixel-exact đối chiếu PDF gốc)
7. `raw_materials/physics/reviews/ch11-agy-theory-b-review.md` (Báo cáo thẩm định này)
8. Bộ 15 tệp ảnh định dạng PNG tiền tố `b-` tại `docs/vat-ly-1/bai-giang/img/young-11/`:
   - `b-hinh-11-12.png` (Mô hình thanh chịu ứng suất kéo và dãn dài)
   - `b-hinh-11-13.png` (Mô hình vật chịu nén và co ngắn)
   - `b-hinh-11-14.png` (Cáp thép chịu kéo và tiết diện ngang)
   - `b-ung-dung-11-gan-chan.png` (Ứng dụng y sinh: Gân gót chân Achilles)
   - `b-hinh-11-15.png` (Mô hình vật thể chìm trong chất lưu chịu áp suất thuỷ tĩnh)
   - `b-hinh-11-16.png` (Mô hình cắt trượt của khối vật liệu chịu ngoại lực song song)
   - `b-ung-dung-11-ca-can-cau.png` (Ứng dụng sinh học: Cá cần câu thích nghi áp suất biển sâu)
   - `b-hinh-11-17.png` (Đồ thị quan hệ Ứng suất – Biến dạng của kim loại dẻo)
   - `b-hinh-11-18.png` (Đồ thị ứng suất – biến dạng của cao su lưu hoá và hiện tượng trễ đàn hồi)
   - `b-hinh-11-19.png` (Thử nghiệm dãn dài của thanh kim loại dẻo, hiện tượng thắt cổ và phá huỷ)
   - `b-hinh-11-20.png` (Mặt gãy của vật liệu giòn và vật liệu dẻo)
   - `b-tom-tat-11-can-bang.png` (Sơ đồ tóm tắt: Hai điều kiện cân bằng tĩnh học)
   - `b-tom-tat-11-keo-nen.png` (Sơ đồ tóm tắt: Ứng suất và biến dạng kéo/nén)
   - `b-tom-tat-11-the-tich.png` (Sơ đồ tóm tắt: Áp suất và biến dạng thể tích)
   - `b-tom-tat-11-truot.png` (Sơ đồ tóm tắt: Ứng suất và biến dạng trượt)

---

## 2. Phạm Vi Phủ Tri Thức Chi Tiết (Source Unit Coverage)

Bài giảng được biên soạn hoàn toàn độc lập, chuẩn mực học thuật tiếng Việt sư phạm ("giảng như giáo sư"), không mang tính chắp vá hay tóm tắt sơ lược:

### Mục 11.4: Ứng suất, Biến dạng và Modun đàn hồi (PDF 365–371)
- **Bản chất vật lý**: Định nghĩa ứng suất (lực trên một đơn vị diện tích, $\text{N/m}^2$ hay $\text{Pa}$), biến dạng (độ biến thiên hình học tỉ đối, không thứ nguyên) và modun đàn hồi theo định luật Hooke tổng quát.
- **Biến dạng kéo và nén**:
  - Khái niệm lực kéo vuông góc $F_\perp$, tiết diện ngang $A$, ứng suất kéo $\sigma = F_\perp / A$.
  - Biến dạng kéo tỉ đối $\epsilon = \Delta l / l_0$.
  - Modun Young $Y = \sigma / \epsilon = (F_\perp / A) / (\Delta l / l_0)$.
  - Bảng tra cứu 11.1 (Giá trị xấp xỉ modun đàn hồi của các vật liệu kỹ thuật thông dụng: Nhôm, Đồng thau, Đồng đỏ, Thuỷ tinh, Gang, Chì, Thép, Niken...). Trình bày dạng bảng di động thân thiện (vertical fields).
  - Phân biệt bản chất ứng suất nén và biến dạng nén; nguyên nhân thanh dài chịu nén dễ bị oằn (buckling).
  - **Ví dụ 11.5 (Dãn dài của dây cáp thép thang máy)**: Đầy đủ các bước nhận diện, thiết lập, tính toán số trị và đánh giá bản chất.
  - **Ứng dụng y sinh (Gân gót chân Achilles)**: Phân tích cơ chế tích trữ năng lượng cơ học của gân người khi chạy nhảy, tính toán ứng suất tối đa $3 \times 10^7\text{ Pa}$ ứng với biến dạng $2{,}5\%$ và modun Young $1{,}2 \times 10^9\text{ Pa}$.
- **Áp suất và Biến dạng thể tích**:
  - Khái niệm áp suất thuỷ tĩnh $p = F_\perp / A$, đơn vị Pascal và atmosphere ($1\text{ atm} = 1{,}013 \times 10^5\text{ Pa}$).
  - Ứng suất thể tích $\Delta p$, biến dạng thể tích $\Delta V / V_0$.
  - Modun khối $B = -\Delta p / (\Delta V / V_0)$, giải thích ý nghĩa dấu âm biểu thị sự suy giảm thể tích khi áp suất tăng.
  - Độ nén $k = 1 / B = -(\Delta V / V_0) / \Delta p$.
  - Bảng tra cứu 11.2 (Modun khối và độ nén của chất rắn và chất lưu: Nước, Thuỷ ngân, Dầu, Ethanol, Glycerin...).
  - **Ví dụ 11.6 (Biến dạng thể tích của dầu thuỷ lực trong xilanh ép)**: Trình bày chi tiết cả 2 cách tính (dùng modun khối $B$ và dùng độ nén $k$).
  - **Ứng dụng sinh học (Cá cần câu biển sâu)**: Cơ chế sinh học thích nghi với áp suất thuỷ tĩnh cực lớn ở độ sâu $1000\text{ m}$ ($\sim 100\text{ atm}$).
- **Ứng suất trượt và Biến dạng trượt**:
  - Khái niệm lực tiếp tuyến song song $F_\parallel$, diện tích trượt $A$, ứng suất trượt $\tau = F_\parallel / A$.
  - Biến dạng trượt $\gamma = x / h = \tan \phi \approx \phi$ (khi góc lệch rất bé).
  - Modun trượt $S = \tau / \gamma = (F_\parallel / A) / (x / h)$.
  - Mối liên hệ so sánh giữa $Y$, $B$ và $S$ ($S \approx Y/3$ trong chất rắn; chất lưu có $S = 0$ vì không thể chống lại biến dạng trượt tĩnh).
  - **Ví dụ 11.7 (Ứng suất trượt trong chân đế thiết bị khi xảy ra động đất)**: Phân tích lực cắt tiếp tuyến $28\text{ kN}$ tác dụng lên tấm đệm đồng thau.
  - **Kiểm tra hiểu biết 11.4 (Test Your Understanding 11.4)**: Trình bày đầy đủ cả 2 phần câu hỏi so sánh biến dạng (phần 1: hai biến dạng bằng nhau) và so sánh ứng suất (phần 2: thanh thép chịu ứng suất lớn hơn thanh đồng).

### Mục 11.5: Tính đàn hồi và Tính dẻo (PDF 371–373)
- **Đường cong ứng suất – biến dạng của kim loại dẻo**:
  - Giới hạn tỉ lệ (Proportional limit, điểm $a$).
  - Giới hạn đàn hồi và điểm chảy (Elastic limit / Yield point, điểm $b$).
  - Vùng biến dạng dẻo (Plastic deformation) và biến dạng dư vĩnh viễn (Permanent set).
  - Độ bền giới hạn (Ultimate tensile strength, điểm $d$).
  - Điểm đứt / gãy (Fracture point, điểm $e$) và hiện tượng thắt cổ (necking).
- **Phân loại vật liệu theo ứng xử cơ học**:
  - Vật liệu dẻo (Ductile): Khoảng biến dạng dẻo rộng, có hiện tượng thắt cổ, mặt gãy dạng nón cốc.
  - Vật liệu giòn (Brittle): Gãy đột ngột ngay sau giới hạn đàn hồi, không có thắt cổ, mặt gãy phẳng góc.
  - Bảng tra cứu 11.3 (Độ bền giới hạn khi kéo, nén và trượt của các vật liệu kỹ thuật).
- **Hiện tượng trễ đàn hồi (Elastic Hysteresis)**:
  - Ứng xử cơ học phi tuyến của cao su lưu hoá (Polyme liên kết chéo).
  - Chu trình dãn – phục hồi, diện tích khép kín của đường trễ đàn hồi biểu thị phần năng lượng cơ học chuyển hoá thành nội nhiệt.
  - **Kiểm tra hiểu biết 11.5 (Test Your Understanding 11.5)**: Ứng dụng thực tế của vật liệu có độ trễ đàn hồi lớn trong giảm chấn va chạm ô tô.

### Tóm Tắt Toàn Diện Chương 11 (PDF 373)
- Sơ đồ hóa 4 trụ cột kiến thức chính:
  1. Hai điều kiện cân bằng tĩnh học của vật rắn ($\sum \vec{F} = \vec{0}$ và $\sum \vec{\tau} = \vec{0}$).
  2. Trọng tâm và điều kiện trùng với khối tâm trong trường trọng lực đều.
  3. Ứng suất, biến dạng và ba modun đàn hồi cơ bản ($Y$, $B$, $S$).
  4. Giới hạn cơ học của vật liệu (đàn hồi, dẻo, bền giới hạn, gãy phá huỷ và độ trễ).

---

## 3. Sổ Kiểm Thử Số Học & Vật Lý Thực Nghiệm (Numerical Ledger)

Tất cả các số liệu trong ví dụ và câu hỏi kiểm tra đều được giải mã bằng Python thực tế (`verify_chapter11_theory_b.py`):

| Đơn vị bài giảng | Đại lượng / Công thức | Dữ liệu đầu vào | Kết quả tính toán Python | Giá trị công bố trong bài giảng | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Ví dụ 11.5** | Lực căng cáp $F_\perp = mg$ | $m = 550\text{ kg}$, $g = 9{,}8\text{ m/s}^2$ | $5390\text{ N}$ | $5390\text{ N}$ | ĐẠT (Pass) |
| **Ví dụ 11.5** | Ứng suất kéo $\sigma = F_\perp / A$ | $A = 3{,}0 \times 10^{-5}\text{ m}^2$ | $1{,}797 \times 10^8\text{ Pa}$ | $1{,}8 \times 10^8\text{ Pa}$ | ĐẠT (Pass) |
| **Ví dụ 11.5** | Biến dạng kéo $\epsilon = \sigma / Y$ | $Y = 20 \times 10^{10}\text{ Pa}$ | $8{,}983 \times 10^{-4}$ | $9{,}0 \times 10^{-4}$ ($0{,}090\%$) | ĐẠT (Pass) |
| **Ví dụ 11.5** | Độ dãn dài $\Delta l = \epsilon l_0$ | $l_0 = 2{,}0\text{ m}$ | $1{,}80 \times 10^{-3}\text{ m}$ | $1{,}8\text{ mm}$ | ĐẠT (Pass) |
| **Ví dụ 11.6** | Độ giảm thể tích $\Delta V = -\frac{V_0 \Delta p}{B}$ | $V_0 = 0{,}25\text{ m}^3$, $\Delta p = 1{,}6 \times 10^7\text{ Pa}$, $B = 5{,}0 \times 10^9\text{ Pa}$ | $-8{,}00 \times 10^{-4}\text{ m}^3$ | $-8{,}0 \times 10^{-4}\text{ m}^3$ ($-0{,}80\text{ L}$) | ĐẠT (Pass) |
| **Ví dụ 11.6** | Biến dạng thể tích $\Delta V / V_0$ | $-0{,}80\text{ L} / 250\text{ L}$ | $-0{,}32\%$ | $-0{,}32\%$ | ĐẠT (Pass) |
| **Ví dụ 11.7** | Tiết diện cắt trượt $A = l \cdot h$ | $l = 0{,}80\text{ m}$, $h = 0{,}0050\text{ m}$ | $0{,}0040\text{ m}^2$ | $4{,}0 \times 10^{-3}\text{ m}^2$ | ĐẠT (Pass) |
| **Ví dụ 11.7** | Biến dạng trượt $\gamma = x / h$ | $x = 1{,}6 \times 10^{-4}\text{ m}$ | $2{,}00 \times 10^{-4}$ | $2{,}0 \times 10^{-4}$ | ĐẠT (Pass) |
| **Ví dụ 11.7** | Ứng suất trượt $\tau = \gamma S$ | $S = 3{,}5 \times 10^{10}\text{ Pa}$ | $7{,}00 \times 10^6\text{ Pa}$ | $7{,}0 \times 10^6\text{ Pa}$ | ĐẠT (Pass) |
| **Ví dụ 11.7** | Lực cắt tiếp tuyến $F_\parallel = \tau A$ | $A = 0{,}0040\text{ m}^2$ | $28000\text{ N}$ | $2{,}8 \times 10^4\text{ N}$ ($28\text{ kN}$) | ĐẠT (Pass) |
| **TYU 11.4** | Biến dạng kéo hai thanh | Cùng kích thước, cùng tải trọng | $\epsilon_{\text{steel}} = \epsilon_{\text{Cu}}$ | Bằng nhau ($2{,}00 \times 10^{-5}$) | ĐẠT (Pass) |
| **TYU 11.4** | Ứng suất kéo hai thanh | $Y_{\text{steel}} = 20 \times 10^{10}\text{ Pa}$, $Y_{\text{Cu}} = 11 \times 10^{10}\text{ Pa}$ | $\sigma_{\text{steel}} = 4{,}0 \times 10^6\text{ Pa} > \sigma_{\text{Cu}} = 2{,}2 \times 10^6\text{ Pa}$ | Thanh thép lớn hơn thanh đồng | ĐẠT (Pass) |
| **Gân Achilles** | Ứng suất kéo sinh học | $Y = 1{,}2 \times 10^9\text{ Pa}$, $\epsilon = 2{,}5\%$ | $3{,}00 \times 10^7\text{ Pa}$ | $3 \times 10^7\text{ Pa}$ | ĐẠT (Pass) |
| **Cá cần câu** | Áp suất tại độ sâu $1000\text{ m}$ | $h = 1000\text{ m}$, $\rho \approx 1000\text{ kg/m}^3$ | $\Delta p \approx 9{,}8 \times 10^6\text{ Pa} \approx 96{,}7\text{ atm}$ | $\sim 100\text{ atm}$ | ĐẠT (Pass) |

---

## 4. Thẩm Định Trích Xuất Ảnh & So Sánh Pixel RGB Thực Tế

Script trích xuất ảnh `prepare-physics1-11-theory-b-assets.py` đã kết xuất 15 tệp ảnh từ file PDF nguồn ở độ phân giải cao (scale 3.0, tương đương 216 DPI).

Kiểm tra so sánh trực tiếp mảng pixel RGB tươi đối chiếu với trang PDF nguồn (`PyMuPDF` rendering):

| Tệp ảnh | Trang PDF nguồn | Toạ độ trích xuất (pt) | Kích thước ảnh (px) | Sai lệch pixel RGB tối đa (`max diff`) | Kết luận |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `b-hinh-11-12.png` | Trang 365 | $[405, 126, 541, 439]$ | $408 \times 940$ | 0 | Khớp tuyệt đối |
| `b-hinh-11-13.png` | Trang 366 | $[405, 592, 542, 681]$ | $413 \times 268$ | 0 | Khớp tuyệt đối |
| `b-hinh-11-14.png` | Trang 367 | $[405, 116, 546, 283]$ | $425 \times 501$ | 0 | Khớp tuyệt đối |
| `b-ung-dung-11-gan-chan.png` | Trang 367 | $[405, 477, 546, 641]$ | $425 \times 493$ | 0 | Khớp tuyệt đối |
| `b-hinh-11-15.png` | Trang 368 | $[68, 563, 201, 700]$ | $401 \times 413$ | 0 | Khớp tuyệt đối |
| `b-hinh-11-16.png` | Trang 369 | $[68, 483, 364, 580]$ | $888 \times 293$ | 0 | Khớp tuyệt đối |
| `b-ung-dung-11-ca-can-cau.png` | Trang 369 | $[405, 116, 541, 278]$ | $410 \times 488$ | 0 | Khớp tuyệt đối |
| `b-hinh-11-17.png` | Trang 371 | $[405, 126, 541, 302]$ | $408 \times 528$ | 0 | Khớp tuyệt đối |
| `b-hinh-11-18.png` | Trang 372 | $[68, 484, 209, 688]$ | $425 \times 613$ | 0 | Khớp tuyệt đối |
| `b-hinh-11-19.png` | Trang 372 | $[405, 116, 543, 258]$ | $415 \times 426$ | 0 | Khớp tuyệt đối |
| `b-hinh-11-20.png` | Trang 372 | $[405, 473, 543, 582]$ | $415 \times 328$ | 0 | Khớp tuyệt đối |
| `b-tom-tat-11-can-bang.png` | Trang 373 | $[68, 115, 176, 244]$ | $326 \times 388$ | 0 | Khớp tuyệt đối |
| `b-tom-tat-11-keo-nen.png` | Trang 373 | $[68, 259, 176, 346]$ | $326 \times 263$ | 0 | Khớp tuyệt đối |
| `b-tom-tat-11-the-tich.png` | Trang 373 | $[68, 362, 176, 449]$ | $326 \times 263$ | 0 | Khớp tuyệt đối |
| `b-tom-tat-11-truot.png` | Trang 373 | $[68, 465, 176, 540]$ | $326 \times 226$ | 0 | Khớp tuyệt đối |

**Đánh giá mép biên và chú thích ảnh**:
- Tất cả các hộp trích xuất ôm sát vùng đồ hoạ chính, loại bỏ 100% dòng chú thích chữ bên ngoài của giáo trình.
- Không bị lẹm khung hay dính viền văn bản của các đoạn văn xung quanh.
- Dưới mỗi ảnh trong bài học đều có chú thích tiếng Việt tự nhiên và bảng đối chiếu nhãn tiếng Anh hiển thị nguyên gốc trên ảnh.

---

## 5. Thẩm Định Chuẩn Mực Toán Học & Công Cụ Đo Độ Dài (Math Standards)

Đã chạy công cụ kiểm thử nghiêm ngặt `measure-math.mjs` (sử dụng MathJax SVG measurement):

```bash
node C:/Users/Ai/.codex/worktrees/physics1-priority-20261022/StudyHub/qa/physics1-priority/measure-math.mjs . \
  raw_materials/physics/translations/chapter-11/04-ung-suat-bien-dang-modun.md \
  raw_materials/physics/translations/chapter-11/05-dan-hoi-va-deo.md \
  raw_materials/physics/translations/chapter-11/17-tom-tat.md
```

**Kết quả kiểm thử**:
- **Trạng thái**: `"status": "passed"`
- **Số công thức hiển thị (display math)**: 62 công thức
- **Số công thức nội dòng (inline math)**: 257 công thức
- **Số lỗi phát hiện (findings)**: 0 lỗi
- **Mã thoát (Exit code)**: 0

**Các tiêu chí kỹ thuật đã đảm bảo**:
- Mọi dấu phân cách `$$` đều nằm riêng biệt tại cột 0 (column zero).
- Các phương trình ngắn đơn lẻ không bị lạm dụng môi trường `\begin{aligned}`.
- Toàn bộ công thức display đều có bề rộng $\le 25\text{ex}$.
- Toàn bộ công thức inline đều có bề rộng $\le 27\text{ex}$.
- Không có bất kỳ thanh cuộn ngang nào xuất hiện.

---

## 6. Nhật Ký Lệnh Kiểm Thử & Mã Thoát (Commands & Exit Codes)

| Lệnh thực thi | Mục đích kiểm tra | Mã thoát (Exit code) | Kết quả ghi nhận |
| :--- | :--- | :--- | :--- |
| `C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter11_theory_b.py` | Kiểm thử số học + đối chiếu 15 ảnh RGB tươi với PDF nguồn + kiểm tra từ điển chú thích ảnh | `0` | **PASS**: Toàn bộ kiểm thử tính toán và 15 ảnh khớp 0 pixel diff. |
| `node qa/physics1-priority/measure-math.mjs . [3 markdown files]` | Kiểm tra cú pháp, độ dài công thức TeX và quy tắc ngắt dòng | `0` | **PASS**: 0 findings trên cả 3 tệp. |
| `node --input-type=module -e "import('./docs/.vitepress/physics1-11-theory-b-image-annotations.mjs')..."` | Kiểm tra cú pháp module ESM và đủ 15 key chú thích | `0` | **PASS**: Export hợp lệ, đủ 15/15 item. |
| `git status -s` | Kiểm tra ranh giới sở hữu tệp, đảm bảo không sửa tệp ngoài phạm vi | `0` | **PASS**: Chỉ có các tệp được giao, không có tệp thừa. |

---

## 7. Ranh Giới Quyền Hạn & Khẳng Định Trung Thực (Scope, Boundaries & Honest Assessment)

1. **Khối lượng công việc còn thiếu (Missing work)**: Không có. Đã hoàn thành 100% nội dung lý thuyết, bảng số liệu, ví dụ mẫu, ứng dụng sinh học/y sinh và các câu hỏi kiểm tra hiểu biết của Mục 11.4, 11.5 và Tóm tắt Chương 11.
2. **Lỗi hạn ngạch hoặc phân quyền (Quota / Permission errors)**: Không có lỗi nào xảy ra trong quá trình hoàn thiện.
3. **Tuân thủ quy ước an toàn**:
   - Không tự ý chạy `npm run ci:build` hay dev server làm nghẽn tài nguyên máy người dùng.
   - Không tự ý commit hoặc push git (ủy quyền cho quy trình cha).
   - Không can thiệp vào các tệp dùng chung, catalog hay stylesheet toàn cục.
4. **Cam kết trung thực**: Không đưa ra các tuyên bố phóng đại như "100% hoàn hảo" hay "đã chứng nhận trên trình duyệt"; toàn bộ kết quả dựa trên các lệnh đo đạc thực tế có thể tái lập độc lập.
