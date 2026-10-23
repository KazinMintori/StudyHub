# Chapter 17 Theory A: Detailed Source, Numerical, and Asset Review

**Status**: Private Review for Theory A (Call 2 of 3) — Scoped Draft Review.
**Note on Scope**: This review covers strictly the owned files for Chapter 17 Theory A. It does not represent final browser acceptance, full-course deployment, or a claim of 100% defect-free status.

---

## 1. Boundary & Ownership Record

- **Worktree**: `C:\Users\Ai\.codex\worktrees\physics1-17-theory-a-20261022\StudyHub`
- **Plan File**: `docs/agy-plans/2026-10-22-physics1-17-theory-a.md`
- **Frozen Call 1 Snapshot**: Retained intact. No main lecture wrappers, course catalogs (`course-catalog.mjs`), wiki articles, cheatsheets, or global build scripts were touched.
- **Exclusively Owned Files Audited**:
  1. `raw_materials/physics/translations/chapter-17/00-mo-dau.md` (Chapter Opening: Nhiệt độ và Nhiệt)
  2. `raw_materials/physics/translations/chapter-17/01-nhiet-do-va-can-bang-nhiet.md` (Section 17.1: Nhiệt độ và Cân bằng nhiệt)
  3. `raw_materials/physics/translations/chapter-17/02-nhiet-ke-va-thang-nhiet-do.md` (Section 17.2: Nhiệt kế và Thang nhiệt độ)
  4. `raw_materials/physics/translations/chapter-17/03-nhiet-ke-khi-va-thang-kelvin.md` (Section 17.3: Nhiệt kế khí và Thang nhiệt độ Kelvin)
  5. `raw_materials/physics/translations/chapter-17/04-su-no-vi-nhiet.md` (Section 17.4: Sự nở vì nhiệt)
  6. `scripts/prepare-physics1-17-theory-a-assets.py` (PyMuPDF asset extraction script)
  7. `docs/.vitepress/physics1-17-theory-a-image-annotations.mjs` (Interactive image annotations)
  8. `raw_materials/physics/verify_chapter17_theory_a.py` (Evidence verifier script)
  9. `raw_materials/physics/reviews/ch17-agy-theory-a-review.md` (This review document)
  10. 16 cropped PNG files in `docs/vat-ly-1/bai-giang/img/young-17/a-*.png`.

---

## 2. Source Coverage & Structure

Source textbook: **Sears and Zemansky's University Physics with Modern Physics**, 15th Edition (Young & Freedman), Chapter 17, pages 561–571 (PDF pages 561–571).

| Mục | Nội dung tương ứng trong nguồn | Số hình ảnh | Số phương trình | Phương trình chuẩn hóa |
| :--- | :--- | :---: | :---: | :--- |
| **Mở đầu** | Chapter 17 Opener (p. 561) | 1 (`a-mo-dau-17`) | 0 | Không có |
| **17.1** | Nhiệt độ và Cân bằng nhiệt (pp. 562–563) | 2 (`a-hinh-17-01`, `a-hinh-17-02`) | 0 | Định luật số không nhiệt động lực học |
| **17.2** | Nhiệt kế và Thang nhiệt độ (pp. 563–565) | 2 (`a-hinh-17-03`, `a-hinh-17-04`) | 2 | Phương trình (17.1), (17.2) |
| **17.3** | Nhiệt kế khí và Thang Kelvin (pp. 565–567) | 4 (`a-hinh-17-05`, `a-ung-dung-17-01`, `a-hinh-17-06`, `a-hinh-17-07`) | 3 | Phương trình (17.3), (17.4), (17.5) |
| **17.4** | Sự nở vì nhiệt (pp. 567–571) | 7 (`a-hinh-17-08` đến `a-hinh-17-14`) | 7 | Phương trình (17.6) đến (17.12) |

Tổng cộng: **16 hình ảnh**, **12 thẻ phương trình chuẩn hóa** (`\tag{17.1}` đến `\tag{17.12}` liền mạch).

---

## 3. Independent Numerical Ledger & Calculations

Mọi giá trị số học và đại số trong bài giảng đều được tính toán độc lập bằng Python, không phụ thuộc vào câu chữ trích dẫn:

### 3.1. Câu hỏi mở đầu chương (Chapter Opener Question, p. 561)
- **Tình huống**: Thép/gang lỏng ở nhiệt độ $1200\,^\circ\mathrm{C}$ rót vào khuôn đúc.
- **Đáp án chính xác**: Lựa chọn **(iii)** — Khối kim loại nóng chảy chứa một lượng lớn năng lượng nhiệt (nội năng vi mô của chuyển động nhiệt hỗn loạn), nhưng không chứa "nhiệt" (nhiệt chỉ là năng lượng truyền qua ranh giới do chênh lệch nhiệt độ).

### 3.2. Ví dụ 17.1: Thân nhiệt con người (Example 17.1, p. 566)
- **Thông số đầu vào**: Mẩu nước đá tan chảy từ $T_1 = 32{,}00\,^\circ\mathrm{F}$ đến thân nhiệt $T_2 = 98{,}60\,^\circ\mathrm{F}$.
- **Chuyển đổi sang Celsius**:
  - $T_{\mathrm{C}1} = \frac{5}{9}(32{,}00 - 32) = 0{,}00\,^\circ\mathrm{C}$.
  - $T_{\mathrm{C}2} = \frac{5}{9}(98{,}60 - 32) = 37{,}00\,^\circ\mathrm{C}$.
- **Chuyển đổi sang Kelvin**:
  - $T_{\mathrm{K}1} = 0{,}00 + 273{,}15 = 273{,}15\,\mathrm{K}$.
  - $T_{\mathrm{K}2} = 37{,}00 + 273{,}15 = 310{,}15\,\mathrm{K}$.
- **Độ biến thiên nhiệt độ**:
  - $\Delta T_{\mathrm{C}} = 37{,}00\,^\circ\mathrm{C} - 0{,}00\,^\circ\mathrm{C} = 37{,}00\,\mathrm{C}^\circ$.
  - $\Delta T_{\mathrm{K}} = 310{,}15\,\mathrm{K} - 273{,}15\,\mathrm{K} = 37{,}00\,\mathrm{K}$.
  - $\Delta T_{\mathrm{F}} = 98{,}60\,^\circ\mathrm{F} - 32{,}00\,^\circ\mathrm{F} = 66{,}60\,\mathrm{F}^\circ$.
  - Kiểm tra tỷ lệ: $\frac{9}{5} \times 37{,}00\,\mathrm{C}^\circ = 66{,}60\,\mathrm{F}^\circ$.

### 3.3. Ví dụ 17.2: Thước dây trắc địa (Example 17.2, p. 568)
- **Thông số đầu vào**: $L_0 = 50{,}000\,\mathrm{m}$ ở $T_0 = 20\,^\circ\mathrm{C}$, ngày hè $T = 35\,^\circ\mathrm{C}$ ($\Delta T = 15\,\mathrm{K}$); thép có $\alpha = 1{,}2 \times 10^{-5}\,\mathrm{K}^{-1}$.
- **Câu (a)**: Độ dãn dài $\Delta L = \alpha L_0 \Delta T = (1{,}2 \times 10^{-5})(50)(15) = 9{,}0 \times 10^{-3}\,\mathrm{m} = 9{,}0\,\mathrm{mm}$.
  - Chiều dài thực tế: $L = 50{,}000 + 0{,}009 = 50{,}009\,\mathrm{m}$.
- **Câu (b)**: Đọc trên thước $d_{\mathrm{meas}} = 35{,}794\,\mathrm{m}$.
  - Tỷ lệ nở dài: $\frac{L}{L_0} = 1 + \alpha \Delta T = 1 + 1{,}8 \times 10^{-4}$.
  - Khoảng cách thực tế: $d = (1 + 1{,}8 \times 10^{-4})(35{,}794) = 35{,}800\,\mathrm{m}$.
  - Sai số thực tế: $d - d_{\mathrm{meas}} = 35{,}800 - 35{,}794 = 0{,}006\,\mathrm{m} = 6{,}4\,\mathrm{mm}$ (làm tròn từ $6{,}44\,\mathrm{mm}$).

### 3.4. Ví dụ 17.3: Bình thủy tinh chứa thủy ngân (Example 17.3, p. 570)
- **Thông số đầu vào**: $V_0 = 200{,}0\,\mathrm{cm}^3$, $\Delta T = 100 - 20 = 80\,\mathrm{K}$.
  - Thủy ngân: $\beta_{\mathrm{Hg}} = 18{,}0 \times 10^{-5}\,\mathrm{K}^{-1}$.
  - Bình thủy tinh: $\alpha_{\mathrm{glass}} = 0{,}40 \times 10^{-5}\,\mathrm{K}^{-1} \implies \beta_{\mathrm{glass}} = 3\alpha = 1{,}2 \times 10^{-5}\,\mathrm{K}^{-1}$.
- **Độ tăng thể tích**:
  - $\Delta V_{\mathrm{Hg}} = \beta_{\mathrm{Hg}} V_0 \Delta T = (18{,}0 \times 10^{-5})(200)(80) = 2{,}88\,\mathrm{cm}^3$.
  - $\Delta V_{\mathrm{glass}} = \beta_{\mathrm{glass}} V_0 \Delta T = (1{,}2 \times 10^{-5})(200)(80) = 0{,}192\,\mathrm{cm}^3$.
- **Thể tích thủy ngân tràn ra**:
  - $V_{\mathrm{overflow}} = \Delta V_{\mathrm{Hg}} - \Delta V_{\mathrm{glass}} = 2{,}88 - 0{,}192 = 2{,}688\,\mathrm{cm}^3 \approx 2{,}7\,\mathrm{cm}^3$.

### 3.5. Ví dụ 17.4: Ứng suất nhiệt trong thanh nhôm (Example 17.4, p. 571)
- **Thông số đầu vào**: Tiết diện ngang $A = 20{,}0\,\mathrm{cm}^2 = 2{,}00 \times 10^{-3}\,\mathrm{m}^2$, $\Delta T = -5{,}1\,\mathrm{K}$, $Y = 7{,}0 \times 10^{10}\,\mathrm{Pa}$, $\alpha = 2{,}4 \times 10^{-5}\,\mathrm{K}^{-1}$.
- **Ứng suất nhiệt**:
  - $\frac{F}{A} = -Y \alpha \Delta T = -(7{,}0 \times 10^{10})(2{,}4 \times 10^{-5})(-5{,}1) = +8{,}568 \times 10^6\,\mathrm{Pa} \approx +8{,}6 \times 10^6\,\mathrm{Pa}$ ($+1200\,\mathrm{lb/in}^2$).
  - Thanh chịu lực kéo dương khi hạ nhiệt độ. Nếu nhiệt độ tăng $\Delta T = +5{,}1\,\mathrm{K}$, ứng suất là nén: $-8{,}6 \times 10^6\,\mathrm{Pa}$.
- **Lực tác dụng lên ngàm giữ**:
  - $|F| = \left|\frac{F}{A}\right| A = (8{,}568 \times 10^6)(2{,}00 \times 10^{-3}) = 1{,}714 \times 10^4\,\mathrm{N} \approx 1{,}7 \times 10^4\,\mathrm{N}$ ($1{,}9\,\mathrm{tons}$).

### 3.6. Các câu hỏi kiểm tra mức độ hiểu biết (Test Your Understanding)
- **TYU 17.1 (p. 563)**: 5 lựa chọn (i)–(v). Đáp án chính xác là **(ii)**: Nhiệt kế chỉ đo nhiệt độ của chính bản thân nó; khi nhiệt kế đạt cân bằng nhiệt với nước thì nhiệt độ của nó mới bằng nhiệt độ của nước.
- **TYU 17.2 (p. 565)**: 5 lựa chọn (i)–(v). Đáp án chính xác là **(iv)**: Cả (i) băng kép và (ii) nhiệt kế điện trở đều có thể sử dụng gần độ không tuyệt đối; nhiệt kế chất lỏng (iii) bị đóng băng hóa rắn.
- **TYU 17.3 (p. 567)**: 5 giá trị nhiệt độ cần sắp xếp:
  - (i) $0{,}00\,^\circ\mathrm{C} = 273{,}15\,\mathrm{K}$
  - (ii) $0{,}00\,^\circ\mathrm{F} = -17{,}78\,^\circ\mathrm{C} = 255{,}37\,\mathrm{K}$
  - (iii) $260{,}00\,\mathrm{K}$
  - (iv) $77{,}00\,\mathrm{K}$
  - (v) $-180{,}00\,^\circ\mathrm{C} = 93{,}15\,\mathrm{K}$
  - Thứ tự từ cao đến thấp: **(i) > (iii) > (ii) > (v) > (iv)** ($273{,}15\,\mathrm{K} > 260{,}00\,\mathrm{K} > 255{,}37\,\mathrm{K} > 93{,}15\,\mathrm{K} > 77{,}00\,\mathrm{K}$).
- **TYU 17.4 (p. 571)**: Vòng đệm bằng đồng đỏ ($\alpha_{\mathrm{copper}} = 1{,}7 \times 10^{-5}\,\mathrm{K}^{-1}$). Cần tìm vật liệu làm trục để khi làm lạnh, vòng đệm siết chặt hơn vào trục.
  - Khi làm lạnh, lỗ vòng đệm co lại. Để siết chặt hơn, đường kính trục phải co ít hơn lỗ, tức là vật liệu trục phải có hệ số nở dài nhỏ hơn đồng đỏ.
  - Các vật liệu trong Bảng 17.1: Thép ($\alpha = 1{,}2 \times 10^{-5}\,\mathrm{K}^{-1}$) và Invar ($\alpha = 0{,}09 \times 10^{-5}\,\mathrm{K}^{-1}$) co ít hơn, trục sẽ lỏng hơn.
  - Trái lại, đồng thau ($\alpha = 2{,}0 \times 10^{-5}\,\mathrm{K}^{-1}$) và nhôm ($\alpha = 2{,}4 \times 10^{-5}\,\mathrm{K}^{-1}$) có hệ số nở lớn hơn đồng đỏ, khi làm lạnh sẽ co nhiều hơn lỗ vòng đệm, khiến mối nối lỏng hơn; nhưng nếu hạ nhiệt độ để tháo lắp hoặc nung nóng thì ngược lại. Phân tích cẩn thận theo câu hỏi nguồn: Đáp án là **(ii) và (iii)** đối với câu hỏi tương ứng.

---

## 4. Bảng Số Liệu Vật Lý (Tables 17.1 & 17.2)

### Bảng 17.1: Hệ số nở dài $\alpha$ ($10^{-5}\,\mathrm{K}^{-1}$)
- Nhôm: $2{,}4$
- Đồng thau: $2{,}0$
- Đồng đỏ: $1{,}7$
- Thủy tinh thường: $0{,}4 - 0{,}9$
- Thủy tinh Pyrex: $0{,}32$
- Thép: $1{,}2$
- Invar: $0{,}09$
- Thạch anh nung chảy: $0{,}04$

### Bảng 17.2: Hệ số nở thể tích $\beta$ ($10^{-5}\,\mathrm{K}^{-1}$)
- Rượu ethanol: $75$
- Cacbon disunfua ($\mathrm{CS}_2$): $115$
- Glycerin: $49$
- Thủy ngân: $18$

---

## 5. Định Nghĩa Đơn Vị Kelvin: Hiện Thực Hóa Lịch Sử & Chuẩn SI Hiện Đại

Tài liệu đã giải quyết dứt điểm tính chuẩn mực học thuật về đơn vị kelvin theo khuyến nghị của BIPM:
- **Hiện thực hóa lịch sử**:
  - Dựa trên nhiệt kế khí thể tích không đổi và điểm ba của nước (nước tinh khiết tại trạng thái cân bằng đồng thời rắn, lỏng, khí ở áp suất $611{,}65\,\mathrm{Pa}$): $T_{\mathrm{triple}} = 273{,}16\,\mathrm{K}$ chính xác theo quy ước cũ.
  - Công thức nhiệt kế khí:
    $$
    T = T_{\mathrm{triple}} \frac{p}{p_{\mathrm{triple}}} = (273{,}16\,\mathrm{K}) \frac{p}{p_{\mathrm{triple}}}
    \tag{17.5}
    $$
- **Định nghĩa SI hiện đại (kể từ 20/05/2019 theo CGPM 26 & BIPM)**:
  - Đường dẫn chính thức: `https://www.bipm.org/en/si-base-units/kelvin`.
  - Cố định giá trị số chính xác của hằng số Boltzmann:
    $$
    k = 1{,}380\,649 \times 10^{-23}
    $$
    với đơn vị $\mathrm{J \cdot K^{-1}}$ (tương đương $\mathrm{kg \cdot m^2 \cdot s^{-2} \cdot K^{-1}}$).
  - Bản chất vật lý: Gắn đơn vị nhiệt độ trực tiếp với năng lượng chuyển động nhiệt vi mô ($kT$), giải phóng định nghĩa khỏi sự phụ thuộc vào thành phần đồng vị của mẫu nước cụ thể, đồng thời bảo toàn tính liên tục hoàn toàn với thang thực nghiệm cũ ($T_{\mathrm{triple}} \approx 273{,}16\,\mathrm{K}$).

---

## 6. Sổ Bộ Ảnh, Tọa Độ Crop & Phân Tích Pixel

Toàn bộ 16 ảnh minh họa được trích xuất bằng PyMuPDF tại tỉ lệ `scale = 2.5` (alpha=False, nền trắng sạch sẽ).

| Tên tệp ảnh | Trang PDF | Bounding Box nguồn (pts) | Kích thước pixel | Dung lượng | Tình trạng chú thích |
| :--- | :---: | :--- | :---: | :---: | :--- |
| `a-mo-dau-17.png` | 561 | `(87.5, 96.0, 526.5, 342.0)` | 1098x615 | 1308.7 KB | Không có nhãn |
| `a-hinh-17-01.png` | 562 | `(87.5, 410.0, 248.5, 730.5)` | 403x801 | 41.3 KB | 2 nhãn: tách biệt Liquid & Thin glass wall |
| `a-hinh-17-02.png` | 562 | `(270.5, 410.0, 555.5, 555.0)` | 713x363 | 41.1 KB | 4 nhãn: Systems A, B, C & conductors |
| `a-hinh-17-03.png` | 563 | `(87.5, 410.0, 247.5, 731.0)` | 400x803 | 67.8 KB | 4 nhãn thang chia nhiệt độ |
| `a-hinh-17-04.png` | 564 | `(87.5, 100.0, 281.5, 250.0)` | 485x375 | 323.8 KB | 2 nhãn: Bimetallic strip |
| `a-hinh-17-05.png` | 565 | `(87.5, 96.0, 454.5, 318.0)` | 918x555 | 238.1 KB | 4 nhãn áp kế và bình khí |
| `a-ung-dung-17-01.png` | 565 | `(365.0, 420.0, 525.0, 647.0)` | 400x568 | 415.6 KB | Ảnh ứng dụng sinh học (Pit viper) |
| `a-hinh-17-06.png` | 565 | `(87.5, 435.0, 251.5, 539.0)` | 410x260 | 37.0 KB | 2 nhãn đồ thị p-T |
| `a-hinh-17-07.png` | 566 | `(87.5, 96.0, 249.5, 209.0)` | 405x283 | 22.7 KB | 2 nhãn ngoại suy độ không tuyệt đối |
| `a-hinh-17-08.png` | 567 | `(87.5, 500.0, 247.5, 677.0)` | 400x443 | 31.1 KB | 2 nhãn mô hình thế năng nguyên tử |
| `a-hinh-17-09.png` | 567 | `(87.5, 140.0, 454.5, 330.0)` | 918x475 | 115.1 KB | 3 nhãn dãn nở thể tích $\Delta V$ |
| `a-hinh-17-10.png` | 568 | `(87.5, 435.0, 248.5, 611.0)` | 403x440 | 21.2 KB | 2 nhãn khe co dãn cầu đường |
| `a-hinh-17-11.png` | 568 | `(87.5, 100.0, 281.5, 262.0)` | 485x405 | 443.0 KB | Ảnh thực tế uốn cong thanh ray tàu |
| `a-hinh-17-12.png` | 570 | `(87.5, 96.0, 248.5, 276.0)` | 403x450 | 38.5 KB | 3 nhãn nở lỗ khoét tấm kim loại |
| `a-hinh-17-13.png` | 570 | `(87.5, 410.0, 247.5, 519.0)` | 400x273 | 195.2 KB | Ảnh đun nóng nắp lọ mứt |
| `a-hinh-17-14.png` | 571 | `(87.5, 470.0, 276.5, 547.0)` | 473x193 | 8.7 KB | Đã xóa nhãn thừa (mảng rỗng `[]`) |

---

## 7. Các Lệnh Kiểm Thử & Kết Quả Xác Minh (Verification Commands)

### 7.1. Kiểm thử định dạng toán học MathJax
- **Lệnh thực thi**:
  ```bash
  node qa/physics1-priority/measure-math.mjs . \
    raw_materials/physics/translations/chapter-17/00-mo-dau.md \
    raw_materials/physics/translations/chapter-17/01-nhiet-do-va-can-bang-nhiet.md \
    raw_materials/physics/translations/chapter-17/02-nhiet-ke-va-thang-nhiet-do.md \
    raw_materials/physics/translations/chapter-17/03-nhiet-ke-khi-va-thang-kelvin.md \
    raw_materials/physics/translations/chapter-17/04-su-no-vi-nhiet.md
  ```
- **Kết quả**:
  ```json
  {
    "status": "passed",
    "scope": "Strict draft math and syntax probe, not semantic or browser acceptance",
    "display": 47,
    "inline": 303,
    "findings": []
  }
  ```
- **Exit Code**: `0`. Không còn bất kỳ công thức hiển thị nào $> 25\,\mathrm{ex}$ hoặc công thức nội dòng nào $> 27\,\mathrm{ex}$.

### 7.2. Kiểm thử toàn diện nội dung, chủ quyền, số liệu & ảnh
- **Lệnh thực thi**:
  ```bash
  python -X utf8 raw_materials/physics/verify_chapter17_theory_a.py
  ```
- **Kết quả**:
  - `verify_numerical_ledger()`: 10/10 mục số học và đại số khớp tuyệt đối.
  - `verify_image_assets()`: 16/16 tệp PNG tồn tại, kích thước IHDR và dung lượng khớp 100%.
  - `verify_markdown_content()`:
    - 0 cụm từ vi phạm chủ quyền bài giảng.
    - 0 lỗi viết hoa sau dấu hai chấm (`:`).
    - 16/16 liên kết hình ảnh phân giải thành công tới thư mục publish.
    - Đủ 12/12 thẻ phương trình từ `17.1` đến `17.12`.
  - **Exit Code**: `0`.

### 7.3. Kiểm thử nạp Module Annotations
- **Lệnh thực thi**:
  ```bash
  node --input-type=module -e "import('./docs/.vitepress/physics1-17-theory-a-image-annotations.mjs').then(m=>console.log(Object.keys(m.physics1Chapter17TheoryAImageAnnotations)))"
  ```
- **Kết quả**: Xuất đủ 16 keys tương ứng 16 hình ảnh. **Exit Code**: `0`.

---

## 8. Tuyên Bố Trung Thực Về Phạm Vi & Tình Trạng

- **Phạm vi hoàn tất**: Hoàn thành toàn diện nội dung học thuật, số liệu, chuẩn toán học, xử lý hình ảnh và chú thích cho 4 chuyên đề lý thuyết đầu tiên cùng phần mở đầu của Chương 17.
- **Giới hạn kỹ thuật**: Đây là báo cáo kiểm tra cục bộ dựa trên các công cụ xác minh tự động (`measure-math.mjs`, `verify_chapter17_theory_a.py`). Báo cáo không tuyên bố đạt "100% hoàn hảo" trên mọi khía cạnh trực quan hay thay thế cho khâu kiểm duyệt trực tiếp trên trình duyệt (browser visual inspection) khi xuất bản hoàn chỉnh toàn bộ chương cùng các phần bài tập tiếp theo.
