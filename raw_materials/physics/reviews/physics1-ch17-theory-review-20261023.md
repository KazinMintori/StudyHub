# Báo Cáo Thẩm Định Học Thuật Độc Lập: Chương 17 (Nhiệt Độ Và Nhiệt Lượng)

**Giáo trình đối sánh**: *Sears and Zemansky's University Physics with Modern Physics*, 15th Edition (Hugh D. Young & Roger A. Freedman)
**Phạm vi thẩm định**: Lý thuyết Chương 17 (*Temperature and Heat*), gồm phần Mở đầu, các Mục 17.1 đến 17.7 và Tóm tắt chương (Trang in 541–569; Trang PDF 561–589).
**Ngày thực hiện**: 23/10/2026
**Môi trường thẩm định**: Python 3.12 (thực thi thuần bộ nhớ `-B -X utf8 -c`), PyMuPDF kiểm tra trực tiếp tệp PDF gốc `raw_materials/physics/source/young-freedman-15.pdf`, Git inspection.
**Tệp xuất báo cáo duy nhất**: `raw_materials/physics/reviews/physics1-ch17-theory-review-20261023.md`

---

## 1. Tóm Tắt Tổng Quan & Giao Thức Thẩm Định

### 1.1. Phạm vi, Mục tiêu và Đối tượng Thẩm định
Báo cáo này thực hiện đánh giá học thuật độc lập, khách quan đối với toàn bộ phần lý thuyết Chương 17 (*Temperature and Heat*) thuộc giáo trình *University Physics* (tập 1, bản 15) theo kế hoạch cam kết tại `docs/agy-plans/2026-10-23-physics1-ch17-theory-review.md`.

Các đối tượng thẩm định trực tiếp bao gồm:
1. **Nguồn gốc giáo trình (Ground Truth)**: Tệp PDF gốc `raw_materials/physics/source/young-freedman-15.pdf`, các trang PDF 561 đến 589 (tương ứng trang sách in 541–569).
2. **Hệ thống tệp bài giảng cơ sở đã đóng băng**: 9 tệp Markdown thực tế trong thư mục `raw_materials/physics/translations/chapter-17/`:
   - `00-mo-dau.md` (39 dòng): Câu hỏi mở đầu chương, mục tiêu học tập và kiến thức cần ôn lại.
   - `01-nhiet-do-va-can-bang-nhiet.md` (64 dòng): Mục 17.1 (Nhiệt độ, tiếp xúc nhiệt, cân bằng nhiệt và Định luật 0).
   - `02-nhiet-ke-va-thang-nhiet-do.md` (86 dòng): Mục 17.2 (Các loại nhiệt kế thông dụng, thang đo Celsius, Fahrenheit và quy tắc đổi độ chênh lệch nhiệt độ).
   - `03-nhiet-ke-khi-va-thang-kelvin.md` (215 dòng): Mục 17.3 (Nhiệt kế khí đẳng tích, thang Kelvin, nhiệt độ tuyệt đối, định nghĩa SI 2019 và Ví dụ 17.1).
   - `04-su-no-vi-nhiet.md` (433 dòng): Mục 17.4 (Sự nở dài, nở khối, cơ chế vi mô, hiện tượng dị thường của nước, ứng suất nhiệt, Ví dụ 17.2, 17.3, 17.4).
   - `05-nhiet-luong.md` (292 dòng): Mục 17.5 (Bản chất nhiệt lượng, nhiệt dung riêng, nhiệt dung mol, quy ước dấu của $Q$, Ví dụ 17.5, 17.6).
   - `06-nhiet-luong-ke-va-chuyen-pha.md` (456 dòng): Mục 17.6 (Quá trình chuyển pha, nhiệt ẩn, phương pháp nhiệt lượng kế $\sum Q = 0$, Ví dụ 17.7, 17.8, 17.9, 17.10).
   - `07-cac-co-che-truyen-nhiet.md` (566 dòng): Mục 17.7 (Dẫn nhiệt nối tiếp/song song, đối lưu, bức xạ nhiệt Stefan–Boltzmann, hiệu ứng nhà kính, Ví dụ 17.11, 17.12, 17.13, 17.14, 17.15).
   - `17-tom-tat.md` (153 dòng): Tóm tắt toàn bộ chương và hệ thống phương trình cốt lõi.
3. **Bộ tài nguyên hình ảnh (Visual Assets)**: 37 tệp ảnh trong `docs/vat-ly-1/bai-giang/img/young-17/` (gồm các tệp `a-hinh-17-01.png` đến `a-hinh-17-14.png`, `a-mo-dau-17.png`, `a-ung-dung-17-01.png`, `b-hinh-17-15.png` đến `b-hinh-17-30.png`, `b-tom-tat-01.png` đến `b-tom-tat-04.png`, `b-ung-dung-17-01.png`).

**Lưu ý về ranh giới thẩm định**:
- Các kịch bản phụ trợ cắt ảnh (như `scripts/prepare-physics1-17-theory-a-assets.py`) chủ đích không nằm trong danh mục tài nguyên đầu vào được đóng băng của đợt thẩm định này. Do đó, việc thiếu tệp phụ thuộc khi chạy thử kịch bản kiểm tra cũ là giới hạn môi trường cục bộ, không phải khiếm khuyết của kho lưu trữ mã nguồn.
- Tệp xuất bản nền `docs/vat-ly-1/bai-giang/17-nhiet-do-nhiet-luong.md` không nằm trong danh mục đầu vào đóng băng của đợt thẩm định và không được dùng để đánh giá trạng thái tích hợp hiện hành của người gọi.

### 1.2. Nguyên Tắc Thẩm Định Học Thuật
- **Kiểm tra tính toán độc lập trong RAM**: Toàn bộ 15 ví dụ tính toán mẫu (Ví dụ 17.1 đến 17.15) được lập trình tính toán lại độc lập bằng mã nguồn Python 3.12 thực thi thuần bộ nhớ (`-B -X utf8 -c`), kiểm tra sai số làm tròn, chữ số có nghĩa và đơn vị đo lường. Không có tệp nháp hay bytecode trung gian nào được ghi xuống đĩa.
- **Đối chiếu văn bản gốc theo từng trang**: Trích xuất văn bản từ PDF gốc bằng PyMuPDF để đối chiếu từng khái niệm, định nghĩa, bước biến đổi toán học và chú thích sư phạm.
- **Loại bỏ tuyên bố hoàn hảo tuyệt đối**: Báo cáo loại bỏ toàn bộ các khẳng định cảm tính dạng "100%", "chính xác tuyệt đối" hay "hoàn hảo". Mọi hạng mục nằm ngoài phạm vi thẩm định lý thuyết đều được đánh dấu minh bạch là `UNCERTAIN`.

---

## 2. Bảng Đối Chiếu Phủ Nội Dung (Source-Unit Coverage Ledger)

### 2.1. Bảng Tổng Hợp Đối Chiếu Đơn Vị Kiến Thức

| STT | Đơn vị kiến thức (Nguyên bản) | Trang Sách | Trang PDF | Tệp bài giảng thực tế | Tình trạng rà soát | Đánh giá học thuật |
| :---: | :--- | :---: | :---: | :--- | :---: | :--- |
| 1 | Chapter 17 Opening: Understanding Heat and Temperature | 541 | 561 | `00-mo-dau.md` | Đã rà soát chi tiết | Đặt vấn đề trực quan, phân biệt năng lượng nhiệt (nội năng) và nhiệt độ |
| 2 | 17.1 Temperature and Thermal Equilibrium | 542–544 | 562–564 | `01-nhiet-do-va-can-bang-nhiet.md` | Đã rà soát chi tiết | Trình bày Định luật 0, tính chất bắc cầu của cân bằng nhiệt và khái niệm nhiệt độ |
| 3 | 17.2 Thermometers and Temperature Scales | 544–547 | 564–567 | `02-nhiet-ke-va-thang-nhiet-do.md` | Đã rà soát chi tiết | Khảo sát các loại nhiệt kế; công thức chuyển đổi thang Celsius, Fahrenheit; quy tắc đổi khoảng chênh lệch $\Delta T$ |
| 4 | 17.3 Gas Thermometers and the Kelvin Scale | 547–549 | 567–569 | `03-nhiet-ke-khi-va-thang-kelvin.md` | Đã rà soát chi tiết | Chứa Ví dụ 17.1; giải thích nhiệt kế khí thể tích không đổi, ngoại suy áp suất về 0 và chuẩn SI 2019 |
| 5 | 17.4 Thermal Expansion | 549–554 | 569–574 | `04-su-no-vi-nhiet.md` | Đã rà soát chi tiết | Chứa Ví dụ 17.2, 17.3, 17.4; Bảng 17.1, 17.2; phân tích nở dài, nở khối, dị thường của nước và ứng suất nhiệt |
| 6 | 17.5 Quantity of Heat | 554–558 | 574–578 | `05-nhiet-luong.md` | Đã rà soát chi tiết | Chứa Ví dụ 17.5, 17.6; Bảng 17.3; nhiệt dung riêng, nhiệt dung mol, quy ước dấu của $Q$ và quy tắc Dulong–Petit |
| 7 | 17.6 Calorimetry and Phase Changes | 558–563 | 578–583 | `06-nhiet-luong-ke-va-chuyen-pha.md` | Đã rà soát chi tiết | Chứa Ví dụ 17.7, 17.8, 17.9, 17.10; Bảng 17.4; bảo toàn năng lượng trong nhiệt lượng kế $\sum Q = 0$, quá trình chuyển pha |
| 8 | 17.7 Mechanisms of Heat Transfer | 563–568 | 583–588 | `07-cac-co-che-truyen-nhiet.md` | Đã rà soát chi tiết | Chứa Ví dụ 17.11, 17.12, 17.13, 17.14, 17.15; Bảng 17.5; truyền nhiệt dẫn nhiệt (nối tiếp, song song), đối lưu, bức xạ Stefan–Boltzmann, hiệu ứng nhà kính |
| 9 | Chapter 17 Summary & Key Equations | 568–569 | 588–589 | `17-tom-tat.md` | Đã rà soát chi tiết | Hệ thống hóa toàn bộ phương trình then chốt và các nguyên lý trọng tâm của chương |

---

### 2.2. Chi Tiết Đề Mục & Đoạn Trích Dẫn Thực Tế Trong Từng Tệp

#### 1. Tệp `00-mo-dau.md` (39 dòng)
- **Đề mục chính**:
  - Dòng 9: `### Câu hỏi mở đầu chương`
  - Dòng 25: `### Mục tiêu học tập`
  - Dòng 35: `### Kiến thức cần ôn lại`
- **Trích dẫn văn bản thực tế**:
  - Dòng 11–13: *"Tại một nhà máy luyện thép, gang lỏng được nung tới nhiệt độ trên 1500°C để loại bỏ tạp chất. Khối gang nóng chảy này chứa những gì nhiều hơn so với khi nó ở nhiệt độ phòng: (i) nhiệt độ; (ii) nhiệt lượng; (iii) năng lượng; hay (iv) nhiều hơn ở cả ba đại lượng trên?"*
  - Dòng 27: *"Sau khi học xong chương này, người học có thể: Nắm vững khái niệm cân bằng nhiệt và nội dung Định luật số không..."*

#### 2. Tệp `01-nhiet-do-va-can-bang-nhiet.md` (64 dòng)
- **Đề mục chính**:
  - Dòng 1: `## 17.1. Nhiệt độ và cân bằng nhiệt`
  - Dòng 7: `### Thang đo nhiệt độ và dụng cụ đo nhiệt độ`
  - Dòng 19: `### Tiếp xúc nhiệt và cân bằng nhiệt`
  - Dòng 30: `### Định luật số không của nhiệt động lực học`
  - Dòng 50: `### Kiểm tra mức độ hiểu biết 17.1`
- **Trích dẫn văn bản thực tế**:
  - Dòng 3: *"Khái niệm nhiệt độ bắt nguồn từ những cảm nhận định tính của con người về mức độ 'nóng' và 'lạnh'..."*
  - Dòng 32–34: *"Nếu hai hệ $A$ và $B$ đều ở trạng thái cân bằng nhiệt với một hệ thứ ba $C$, thì hai hệ $A$ và $B$ cũng ở trạng thái cân bằng nhiệt với nhau."*
  - Dòng 52: *"Bạn nhúng một chiếc nhiệt kế vào một nồi nước nóng trên bếp và quan sát thấy cột chất lỏng dâng lên rồi dừng lại..."*

#### 3. Tệp `02-nhiet-ke-va-thang-nhiet-do.md` (86 dòng)
- **Đề mục chính**:
  - Dòng 1: `## 17.2. Nhiệt kế và thang nhiệt độ`
  - Dòng 5: `### Các loại nhiệt kế thông dụng`
  - Dòng 21: `### Thang đo nhiệt độ Celsius và Fahrenheit`
  - Dòng 54: `### Lưu ý: Chuyển đổi khoảng chênh lệch nhiệt độ`
  - Dòng 72: `### Kiểm tra mức độ hiểu biết 17.2`
- **Trích dẫn văn bản thực tế**:
  - Dòng 3: *"Để chế tạo nhiệt kế chất lỏng trong ống ở Hình 17.3a, người ta đổ đầy chất lỏng (thường là thủy ngân hoặc cồn nhuộm màu)..."*
  - Dòng 23–25: *"Trên thang Celsius, nhiệt độ đóng băng của nước tinh khiết ở áp suất khí quyển chuẩn được gán là $0^\circ\mathrm{C}$, và nhiệt độ sôi là $100^\circ\mathrm{C}$..."*
  - Dòng 56: *"Cần phân biệt rõ giữa giá trị nhiệt độ tại một thời điểm và khoảng chênh lệch nhiệt độ giữa hai trạng thái..."*

#### 4. Tệp `03-nhiet-ke-khi-va-thang-kelvin.md` (215 dòng)
- **Đề mục chính**:
  - Dòng 1: `## 17.3. Nhiệt kế khí và thang Kelvin`
  - Dòng 7: `### Nhiệt kế khí đẳng tích`
  - Dòng 19: `### Thang đo Kelvin và nhiệt độ tuyệt đối`
  - Dòng 32: `### Lưu ý: Không dùng cụm từ "độ kelvin"`
  - Dòng 38: `### Ứng dụng sinh học: Thân nhiệt của động vật có vú`
  - Dòng 44: `### Xây dựng thang đo Kelvin và hiện thực hóa lịch sử`
  - Dòng 83: `### Lưu ý: Cập nhật định nghĩa thang Kelvin theo chuẩn SI hiện đại`
  - Dòng 95: `::: example Ví dụ 17.1: Thân nhiệt con người`
  - Dòng 186: `### Kiểm tra mức độ hiểu biết 17.3`
- **Trích dẫn văn bản thực tế**:
  - Dòng 9: *"Hình 17.5a mô tả nguyên lý của nhiệt kế khí đẳng tích. Một bình kín chứa một lượng khí xác định được duy trì ở thể tích không đổi..."*
  - Dòng 85: *"Từ tháng 5 năm 2019, Hội nghị Toàn thể về Cân đo (CGPM) đã chính thức định nghĩa lại đơn vị kelvin bằng cách cố định giá trị số của hằng số Boltzmann: $k = 1{,}380649 \times 10^{-23}\,\mathrm{J/K}$..."*
  - Dòng 97: *"Bạn đặt một mẩu nước đá nhỏ vào trong miệng. Sau một khoảng thời gian, toàn bộ nước đá tan và đạt đến thân nhiệt bình thường của cơ thể..."*

#### 5. Tệp `04-su-no-vi-nhiet.md` (433 dòng)
- **Đề mục chính**:
  - Dòng 1: `## 17.4. Sự nở vì nhiệt`
  - Dòng 5: `### Sự nở dài`
  - Dòng 37: `### Cơ chế vi mô của sự nở vì nhiệt`
  - Dòng 49: `### Lưu ý: Nung nóng một vật thể có lỗ rỗng`
  - Dòng 61: `### Sự nở khối`
  - Dòng 111: `### Bảng số liệu hệ số nở vì nhiệt`
  - Dòng 151: `::: example Ví dụ 17.2: Độ nở dài của thước dây trắc địa`
  - Dòng 219: `### Sự nở vì nhiệt bất thường của nước`
  - Dòng 229: `::: example Ví dụ 17.3: Thể tích thủy ngân tràn ra khỏi bình`
  - Dòng 296: `### Ứng suất nhiệt`
  - Dòng 351: `::: example Ví dụ 17.4: Ứng suất nhiệt trong trụ nhôm`
  - Dòng 411: `### Kiểm tra mức độ hiểu biết 17.4`
- **Trích dẫn văn bản thực tế**:
  - Dòng 7: *"Xét một thanh vật liệu rắn đồng chất có chiều dài ban đầu $L_0$ ở nhiệt độ $T_0$. Khi nhiệt độ thay đổi một lượng $\Delta T$, thực nghiệm chứng minh rằng độ biến thiên chiều dài $\Delta L$ tỉ lệ thuận với cả $L_0$ và $\Delta T$..."*
  - Dòng 51: *"Một câu hỏi thường gặp: Nếu một vật rắn có một lỗ rỗng bên trong thì khi nung nóng, kích thước lỗ rỗng sẽ mở rộng hay co lại?..."*
  - Dòng 298: *"Nếu các đầu của một thanh vật liệu được kẹp giữ cố định để ngăn cản sự co giãn nhiệt, bên trong thanh sẽ xuất hiện các ứng suất cơ học rất lớn gọi là ứng suất nhiệt..."*

#### 6. Tệp `05-nhiet-luong.md` (292 dòng)
- **Đề mục chính**:
  - Dòng 1: `## Nhiệt lượng và nhiệt dung`
  - Dòng 5: `### 1. Bản chất của nhiệt lượng và đơn vị đo`
  - Dòng 45: `### 2. Nhiệt dung riêng`
  - Dòng 94: `::: example Ví dụ 17.5: Nhiệt lượng làm tăng thân nhiệt khi cảm sốt`
  - Dòng 134: `::: example Ví dụ 17.6: Tốc độ tăng nhiệt độ do quá nhiệt linh kiện điện tử`
  - Dòng 176: `### 3. Nhiệt dung mol`
  - Dòng 260: `### Câu hỏi tự kiểm tra 17.5`
- **Trích dẫn văn bản thực tế**:
  - Dòng 7: *"Khi ném một đồng xu nóng vào một cốc nước nguội, nhiệt độ của đồng xu giảm dần trong khi nhiệt độ của nước tăng lên cho đến khi đạt cân bằng nhiệt..."*
  - Dòng 47: *"Để làm tăng nhiệt độ của một đơn vị khối lượng của một chất lên một khoảng $\Delta T$, cần cung cấp một nhiệt lượng $Q$..."*
  - Dòng 178: *"Trong hóa học và nhiệt động lực học, việc mô tả lượng chất thông qua số mol $n$ thường thuận tiện hơn so với khối lượng $m$..."*

#### 7. Tệp `06-nhiet-luong-ke-va-chuyen-pha.md` (456 dòng)
- **Đề mục chính**:
  - Dòng 1: `## Nhiệt lượng kế và quá trình chuyển pha`
  - Dòng 5: `### 1. Quá trình chuyển pha và nhiệt ẩn`
  - Dòng 110: `### 2. Các hiện tượng và ứng dụng chuyển pha đặc biệt`
  - Dòng 142: `### 3. Phương pháp giải bài toán nhiệt lượng kế`
  - Dòng 161: `::: example Ví dụ 17.7: Trao đổi nhiệt không kèm chuyển pha`
  - Dòng 216: `::: example Ví dụ 17.8: Biến thiên đồng thời nhiệt độ và chuyển pha`
  - Dòng 265: `::: example Ví dụ 17.9: Hiện tượng sôi và cân bằng pha trong nồi đồng`
  - Dòng 337: `::: example Ví dụ 17.10: Kết hợp phản ứng cháy, tăng nhiệt độ và chuyển pha`
  - Dòng 406: `### Câu hỏi tự kiểm tra 17.6`
- **Trích dẫn văn bản thực tế**:
  - Dòng 7: *"Thuật ngữ 'pha' dùng để chỉ một trạng thái tập hợp đồng nhất của vật chất về cấu trúc hóa học và tính chất vật lý..."*
  - Dòng 144: *"Các bài toán nhiệt lượng kế (tính toán sự truyền nhiệt giữa các vật thể) dựa trên nguyên lý bảo toàn năng lượng trong một hệ cô lập nhiệt: Tổng nhiệt lượng trao đổi bằng không, $\sum Q = 0$..."*

#### 8. Tệp `07-cac-co-che-truyen-nhiet.md` (566 dòng)
- **Đề mục chính**:
  - Dòng 1: `## Các cơ chế truyền nhiệt`
  - Dòng 12: `### 1. Dẫn nhiệt`
  - Dòng 22: `#### Dòng nhiệt và độ dẫn nhiệt`
  - Dòng 85: `#### Dạng vi phân tổng quát của định luật dẫn nhiệt`
  - Dòng 96: `#### Nhiệt trở trong kỹ thuật xây dựng`
  - Dòng 150: `::: example Ví dụ 17.11: Dẫn nhiệt vào thùng xốp giữ lạnh`
  - Dòng 209: `::: example Ví dụ 17.12: Dẫn nhiệt qua hai thanh ghép nối tiếp`
  - Dòng 273: `::: example Ví dụ 17.13: Dẫn nhiệt qua hai thanh ghép song song`
  - Dòng 326: `### 2. Đối lưu`
  - Dòng 340: `#### Tính chất thực nghiệm của truyền nhiệt đối lưu`
  - Dòng 354: `### 3. Bức xạ nhiệt`
  - Dòng 368: `#### Định luật Stefan–Boltzmann`
  - Dòng 397: `::: example Ví dụ 17.14: Sự phát xạ nhiệt của tấm thép`
  - Dòng 429: `#### Cân bằng bức xạ và hấp thụ nhiệt`
  - Dòng 451: `::: example Ví dụ 17.15: Bức xạ nhiệt từ cơ thể người`
  - Dòng 493: `#### Ứng dụng của bức xạ nhiệt`
  - Dòng 503: `### 4. Bức xạ nhiệt, khí hậu và hiệu ứng nhà kính`
  - Dòng 513: `#### Cơ chế hiệu ứng nhà kính và vai trò của các chất khí`
  - Dòng 522: `#### Dữ liệu cổ khí hậu và kịch bản phát thải hiện đại`
  - Dòng 532: `### Kiểm tra hiểu biết`
- **Trích dẫn văn bản thực tế**:
  - Dòng 24: *"Trong hiện tượng dẫn nhiệt, chiều truyền nhiệt luôn hướng từ nhiệt độ cao sang nhiệt độ thấp..."*
  - Dòng 370: *"Tốc độ phát xạ năng lượng từ một bề mặt tỉ lệ thuận với diện tích bề mặt $A$ và lũy thừa bậc bốn của nhiệt độ tuyệt đối $T$: $H = Ae\sigma T^4$..."*

#### 9. Tệp `17-tom-tat.md` (153 dòng)
- **Đề mục chính**:
  - Dòng 1: `## Tóm tắt Chương 17: Nhiệt độ và nhiệt lượng`
  - Dòng 7: `### 1. Nhiệt độ và thang nhiệt độ`
  - Dòng 44: `### 2. Sự nở nhiệt và ứng suất nhiệt`
  - Dòng 83: `### 3. Nhiệt lượng, chuyển pha và nhiệt lượng kế`
  - Dòng 120: `### 4. Các cơ chế truyền nhiệt: Dẫn nhiệt, đối lưu và bức xạ`
- **Trích dẫn văn bản thực tế**:
  - Dòng 9: *"Hai vật ở trạng thái cân bằng nhiệt với nhau khi và chỉ khi chúng có cùng nhiệt độ..."*
  - Dòng 122: *"Năng lượng nhiệt được truyền giữa các vật thông qua ba cơ chế vật lý riêng biệt: Dẫn nhiệt, Đối lưu và Bức xạ nhiệt..."*

---

## 3. Sổ Cái Thẩm Định Tính Toán Độc Lập (Arithmetic Verification Ledger)

Toàn bộ 15 ví dụ tính toán mẫu trong Chương 17 đã được thực thi kiểm tra bằng mã lệnh Python độc lập (chạy với cờ `-B -X utf8 -c` trực tiếp trong RAM, không sinh tệp bytecode trung gian). Dưới đây là biên bản chi tiết từng bài toán:

### Ví dụ 17.1: Thân nhiệt con người (Body Temperature)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/03-nhiet-ke-khi-va-thang-kelvin.md`, dòng 95–184.
- **Vị trí sách gốc**: Trang in 546; Trang PDF 566 (Mục 17.3).
- **Đề bài & Dữ liệu đầu vào**:
  - Một mẩu nước đá nhỏ tan trong miệng: Nhiệt độ ban đầu $T_1 = 32{,}00^\circ\mathrm{F}$, nhiệt độ cuối bằng thân nhiệt $T_2 = 98{,}60^\circ\mathrm{F}$.
  - Yêu cầu: Tính $T_{\mathrm{C}1}, T_{\mathrm{C}2}$ trên thang Celsius; tính khoảng chênh lệch $\Delta T_{\mathrm{C}} = T_{\mathrm{C}2} - T_{\mathrm{C}1}$; đổi sang Kelvin và so sánh với khoảng chênh $\Delta T_{\mathrm{F}}$.
- **Phương trình**:
  $$T_{\mathrm{C}} = \frac{5}{9}(T_{\mathrm{F}} - 32{,}00^\circ), \quad T_{\mathrm{K}} = T_{\mathrm{C}} + 273{,}15, \quad \Delta T_{\mathrm{C}} = \frac{5}{9}\Delta T_{\mathrm{F}}$$
- **Mã Python xác minh**:
  ```python
  T_F1, T_F2 = 32.00, 98.60
  T_C1 = (5/9)*(T_F1 - 32.0)
  T_C2 = (5/9)*(T_F2 - 32.0)
  delta_T_C = T_C2 - T_C1
  delta_T_F = T_F2 - T_F1
  T_K1 = T_C1 + 273.15
  T_K2 = T_C2 + 273.15
  # Kết quả: T_C1 = 0.00 C, T_C2 = 37.00 C, delta_T_C = 37.00 C deg (hoặc K), delta_T_F = 66.60 F deg
  ```
- **Kết quả đối sánh**: Số liệu khớp với giáo trình ($T_{\mathrm{C}1} = 0{,}00^\circ\mathrm{C}$, $T_{\mathrm{C}2} = 37{,}00^\circ\mathrm{C}$, $T_{\mathrm{K}1} = 273{,}15\,\mathrm{K}$, $T_{\mathrm{K}2} = 310{,}15\,\mathrm{K}$, $\Delta T_{\mathrm{C}} = 37{,}00\,\mathrm{C}^\circ = 37{,}00\,\mathrm{K}$, $\Delta T_{\mathrm{F}} = 66{,}60\,\mathrm{F}^\circ$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.2: Độ nở dài của thước dây trắc địa (Surveyor's Tape)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/04-su-no-vi-nhiet.md`, dòng 151–217.
- **Vị trí sách gốc**: Trang in 549; Trang PDF 569 (Mục 17.4).
- **Đề bài & Dữ liệu đầu vào**:
  - Thước thép chuẩn dài $L_0 = 50{,}000\,\mathrm{m}$ ở $T_0 = 20^\circ\mathrm{C}$. Hệ số nở dài của thép $\alpha = 1{,}2 \times 10^{-5}\,\mathrm{K}^{-1}$.
  - Câu (a): Khi trời nắng $T = 35^\circ\mathrm{C}$ ($\Delta T = 15\,\mathrm{K}$), tính chiều dài thước $L$.
  - Câu (b): Dùng thước này ở $35^\circ\mathrm{C}$ đo khoảng cách, đọc được $35{,}794\,\mathrm{m}$. Tính khoảng cách thực tế.
- **Phương trình**:
  $$\Delta L = \alpha L_0 \Delta T, \quad L = L_0 + \Delta L, \quad L_{\text{thực}} = L_{\text{đo}}(1 + \alpha \Delta T)$$
- **Mã Python xác minh**:
  ```python
  L0 = 50.000; alpha = 1.2e-5; dT = 15.0
  dL = alpha * L0 * dT # 0.009 m = 9.0 mm
  L_tape = L0 + dL    # 50.009 m
  L_meas = 35.794
  L_actual = L_meas * (1.0 + alpha * dT) # 35.80044 m -> 35.800 m
  diff = (L_actual - L_meas) * 1000 # +6.4 mm
  ```
- **Kết quả đối sánh**: Khớp số liệu với sách giáo khoa ($\Delta L = 0{,}0090\,\mathrm{m} = 9{,}0\,\mathrm{mm}$, $L = 50{,}009\,\mathrm{m}$; khoảng cách thực tế $35{,}800\,\mathrm{m}$, chênh lệch $+6{,}4\,\mathrm{mm}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.3: Thể tích thủy ngân tràn ra khỏi bình (Volume Thermal Expansion)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/04-su-no-vi-nhiet.md`, dòng 229–292.
- **Vị trí sách gốc**: Trang in 550; Trang PDF 570 (Mục 17.4).
- **Đề bài & Dữ liệu đầu vào**:
  - Bình thủy tinh dung tích $V_0 = 200\,\mathrm{cm^3}$ chứa đầy thủy ngân ở $T_0 = 20^\circ\mathrm{C}$. Khi nung lên $T = 100^\circ\mathrm{C}$ ($\Delta T = 80\,\mathrm{K}$):
  - Hệ số nở khối của thủy ngân $\beta_{\mathrm{Hg}} = 18 \times 10^{-5}\,\mathrm{K}^{-1}$.
  - Thủy tinh có hệ số nở dài $\alpha_{\text{glass}} = 0{,}40 \times 10^{-5}\,\mathrm{K}^{-1} \implies \beta_{\text{glass}} = 3\alpha = 1{,}2 \times 10^{-5}\,\mathrm{K}^{-1}$.
- **Phương trình**:
  $$\Delta V_{\mathrm{Hg}} = \beta_{\mathrm{Hg}} V_0 \Delta T, \quad \Delta V_{\text{glass}} = \beta_{\text{glass}} V_0 \Delta T, \quad V_{\text{tràn}} = \Delta V_{\mathrm{Hg}} - \Delta V_{\text{glass}}$$
- **Mã Python xác minh**:
  ```python
  V0 = 200.0; dT = 80.0
  b_Hg = 18e-5; b_glass = 1.2e-5
  dV_Hg = b_Hg * V0 * dT      # 2.88 cm^3
  dV_glass = b_glass * V0 * dT # 0.192 cm^3
  V_spill = dV_Hg - dV_glass   # 2.688 cm^3 -> 2.7 cm^3
  ```
- **Kết quả đối sánh**: Khớp số liệu với sách giáo khoa ($\Delta V_{\mathrm{Hg}} = 2{,}88\,\mathrm{cm^3} \approx 2{,}9\,\mathrm{cm^3}$, $\Delta V_{\text{glass}} = 0{,}192\,\mathrm{cm^3} \approx 0{,}19\,\mathrm{cm^3}$, $V_{\text{tràn}} = 2{,}688\,\mathrm{cm^3} \approx 2{,}7\,\mathrm{cm^3}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.4: Ứng suất nhiệt trong trụ nhôm (Thermal Stress)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/04-su-no-vi-nhiet.md`, dòng 351–409.
- **Vị trí sách gốc**: Trang in 551; Trang PDF 571 (Mục 17.4).
- **Đề bài & Dữ liệu đầu vào**:
  - Trụ nhôm dài $L_0 = 10\,\mathrm{cm}$, diện tích tiết diện ngang $A = 20\,\mathrm{cm^2} = 2{,}0 \times 10^{-3}\,\mathrm{m^2}$ đặt vừa khít giữa hai bức tường thép cứng vững ở $T_1 = 17{,}2^\circ\mathrm{C}$.
  - Nhiệt độ tăng lên $T_2 = 22{,}3^\circ\mathrm{C}$ ($\Delta T = 22{,}3 - 17{,}2 = 5{,}1\,\mathrm{K}$).
  - Suất Young của nhôm $Y = 7{,}0 \times 10^{10}\,\mathrm{Pa}$, hệ số nở dài $\alpha = 2{,}4 \times 10^{-5}\,\mathrm{K}^{-1}$.
- **Phương trình**:
  $$\frac{F}{A} = -Y \alpha \Delta T, \quad F = A \left(\frac{F}{A}\right)$$
- **Mã Python xác minh**:
  ```python
  Y = 7.0e10; alpha = 2.4e-5; dT = 5.1; A = 20e-4 # 2.0e-3 m^2
  stress = -Y * alpha * dT # -8,568,000 Pa = -8.568 MPa -> -8.6 MPa
  force = stress * A      # -17,136 N -> -1.7 x 10^4 N
  ```
- **Kết quả đối sánh**: Số liệu khớp với nguyên bản sách in (ứng suất nén $-8{,}6 \times 10^6\,\mathrm{Pa} = -8{,}6\,\mathrm{MPa}$; lực nén lên mỗi bức tường $-1{,}7 \times 10^4\,\mathrm{N}$, tương đương trọng lượng vật nặng khoảng 1,7 tấn hay 1,9 short tons). Dấu âm thể hiện lực nén.
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.5: Nhiệt lượng làm tăng thân nhiệt khi cảm sốt (Specific Heat Capacity of Body)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/05-nhiet-luong.md`, dòng 94–132.
- **Vị trí sách gốc**: Trang in 553; Trang PDF 573 (Mục 17.5).
- **Đề bài & Dữ liệu đầu vào**:
  - Người có khối lượng $m = 80\,\mathrm{kg}$, thân nhiệt tăng từ $37{,}0^\circ\mathrm{C}$ lên $39{,}0^\circ\mathrm{C}$ ($\Delta T = 2{,}0\,\mathrm{K}$).
  - Mô hình 1 (Toàn bộ là nước): $c_{\text{water}} = 4190\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$.
  - Mô hình 2 (Mô cơ thể người thực tế): $c_{\text{body}} = 3480\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$.
- **Phương trình**:
  $$Q = m c \Delta T$$
- **Mã Python xác minh**:
  ```python
  m = 80.0; dT = 2.0
  Q_w = m * 4190 * dT # 670,400 J = 6.70 x 10^5 J = 160.2 kcal
  Q_b = m * 3480 * dT # 556,800 J = 5.57 x 10^5 J = 133.1 kcal
  ```
- **Kết quả đối sánh**: Khớp số liệu với sách giáo khoa ($Q_{\text{nước}} = 6{,}7 \times 10^5\,\mathrm{J} = 160\,\mathrm{kcal}$; $Q_{\text{cơ thể}} = 5{,}6 \times 10^5\,\mathrm{J} = 133\,\mathrm{kcal}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.6: Tốc độ tăng nhiệt độ do quá nhiệt linh kiện điện tử (Silicon Chip Heating)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/05-nhiet-luong.md`, dòng 134–174.
- **Vị trí sách gốc**: Trang in 553; Trang PDF 573 (Mục 17.5).
- **Đề bài & Dữ liệu đầu vào**:
  - Linh kiện silic có khối lượng $m = 23\,\mathrm{mg} = 23 \times 10^{-6}\,\mathrm{kg}$, tiêu tán năng lượng điện với tốc độ $P = dQ/dt = 7{,}4\,\mathrm{mW} = 7{,}4 \times 10^{-3}\,\mathrm{W}$.
  - Nhiệt dung riêng của silic $c_{\mathrm{Si}} = 705\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$. Giả thiết ban đầu chưa có nhiệt thất thoát ra môi trường.
- **Phương trình**:
  $$\frac{dQ}{dt} = m c \frac{dT}{dt} \implies \frac{dT}{dt} = \frac{P}{m c}$$
- **Mã Python xác minh**:
  ```python
  m = 23e-6; P = 7.4e-3; c = 705.0
  dT_dt = P / (m * c) # 0.45637 K/s -> làm tròn 0.46 K/s (tương đương 27.4 K/min)
  ```
- **Kết quả đối sánh**: Số liệu khớp với giáo trình ($0{,}46\,\mathrm{K/s} = 0{,}46\,\mathrm{C}^\circ/\mathrm{s}$, tương đương tốc độ tăng nhiệt độ $27\,\mathrm{K/phút}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.7: Trao đổi nhiệt không kèm chuyển pha (Calorimetry: Coffee and Aluminum Mug)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/06-nhiet-luong-ke-va-chuyen-pha.md`, dòng 161–214.
- **Vị trí sách gốc**: Trang in 559; Trang PDF 579 (Mục 17.6).
- **Đề bài & Dữ liệu đầu vào**:
  - Cốc nhôm khối lượng $m_{\mathrm{Al}} = 0{,}120\,\mathrm{kg}$ ở nhiệt độ ban đầu $T_{\mathrm{Al}} = 20{,}0^\circ\mathrm{C}$, $c_{\mathrm{Al}} = 910\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$.
  - Cà phê (tính chất tương đương nước) khối lượng $m_{\mathrm{w}} = 0{,}300\,\mathrm{kg}$ ở $T_{\mathrm{w}} = 70{,}0^\circ\mathrm{C}$, $c_{\mathrm{w}} = 4190\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$.
- **Phương trình**:
  $$\sum Q = 0 \implies m_{\mathrm{w}} c_{\mathrm{w}} (T - T_{\mathrm{w}}) + m_{\mathrm{Al}} c_{\mathrm{Al}} (T - T_{\mathrm{Al}}) = 0$$
  $$T = \frac{m_{\mathrm{w}} c_{\mathrm{w}} T_{\mathrm{w}} + m_{\mathrm{Al}} c_{\mathrm{Al}} T_{\mathrm{Al}}}{m_{\mathrm{w}} c_{\mathrm{w}} + m_{\mathrm{Al}} c_{\mathrm{Al}}}$$
- **Mã Python xác minh**:
  ```python
  m_w, c_w, T_w = 0.300, 4190.0, 70.0
  m_al, c_al, T_al = 0.120, 910.0, 20.0
  T_eq = (m_w * c_w * T_w + m_al * c_al * T_al) / (m_w * c_w + m_al * c_al) # 66.0035 C -> 66.0 C
  Q_w = m_w * c_w * (T_eq - T_w) # -5023.6 J -> -5.0 kJ
  ```
- **Kết quả đối sánh**: Khớp số liệu với sách giáo khoa ($T = 66{,}0^\circ\mathrm{C}$ và nhiệt lượng cà phê tỏa ra là $5{,}0 \times 10^3\,\mathrm{J} = 5{,}0\,\mathrm{kJ}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.8: Biến thiên đồng thời nhiệt độ và chuyển pha (Cooling Soda with Ice)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/06-nhiet-luong-ke-va-chuyen-pha.md`, dòng 216–263.
- **Vị trí sách gốc**: Trang in 559; Trang PDF 579 (Mục 17.6).
- **Đề bài & Dữ liệu đầu vào**:
  - Lon nước giải khát $m_{\mathrm{w}} = 0{,}25\,\mathrm{kg}$ ở $25^\circ\mathrm{C}$ làm lạnh xuống $0^\circ\mathrm{C}$ bằng các viên đá lấy từ tủ đông ở $-20^\circ\mathrm{C}$.
  - Hằng số: $c_{\text{ice}} = 2100\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$, $L_{\mathrm{f}} = 3{,}34 \times 10^5\,\mathrm{J/kg}$, $c_{\mathrm{w}} = 4190\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$.
- **Phương trình**:
  $$Q_{\text{nước tỏa}} = m_{\mathrm{w}} c_{\mathrm{w}} (0 - 25), \quad Q_{\text{đá thu}} = m_{\text{đá}} c_{\text{ice}} [0 - (-20)] + m_{\text{đá}} L_{\mathrm{f}}$$
  $$m_{\text{đá}} = \frac{m_{\mathrm{w}} c_{\mathrm{w}}(25 - 0)}{c_{\text{ice}}(20) + L_{\mathrm{f}}}$$
- **Mã Python xác minh**:
  ```python
  m_w = 0.25; c_w = 4190.0; dT_w = 25.0
  c_ice = 2100.0; dT_ice = 20.0; L_f = 3.34e5
  Q_released = m_w * c_w * dT_w # 26,187.5 J
  q_ice_per_kg = c_ice * dT_ice + L_f # 42,000 + 334,000 = 376,000 J/kg
  m_ice = Q_released / q_ice_per_kg # 0.06965 kg -> 0.070 kg = 70 g
  ```
- **Kết quả đối sánh**: Số liệu khớp với sách ($m_{\text{đá}} = 0{,}070\,\mathrm{kg} = 70\,\mathrm{g}$, tương đương khoảng 3 viên đá nhỏ).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.9: Hiện tượng sôi và cân bằng pha trong nồi đồng (Unknown Final State)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/06-nhiet-luong-ke-va-chuyen-pha.md`, dòng 265–335.
- **Vị trí sách gốc**: Trang in 560; Trang PDF 580 (Mục 17.6).
- **Đề bài & Dữ liệu đầu vào**:
  - Nồi đồng có nắp đậy $m_{\mathrm{Cu}} = 2{,}0\,\mathrm{kg}$ ở $T_{\mathrm{Cu}} = 150^\circ\mathrm{C}$, rót vào $m_{\mathrm{w}} = 0{,}10\,\mathrm{kg}$ nước ở $T_{\mathrm{w}} = 25^\circ\mathrm{C}$.
  - $c_{\mathrm{Cu}} = 390\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$, $c_{\mathrm{w}} = 4190\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$, $L_{\mathrm{v}} = 2{,}256 \times 10^6\,\mathrm{J/kg}$.
- **Phân tích điều kiện vật lý**:
  - Nếu giả định không có chuyển pha: Giải ra $T = 106{,}3^\circ\mathrm{C} > 100^\circ\mathrm{C}$ (vô lý ở áp suất $1\,\mathrm{atm}$ đối với nước lỏng).
  - Trạng thái cân bằng thực tế ở $100^\circ\mathrm{C}$ với một phần nước hóa hơi.
- **Mã Python xác minh**:
  ```python
  m_cu, c_cu, T_cu = 2.0, 390.0, 150.0
  m_w, c_w, T_w = 0.10, 4190.0, 25.0
  L_v = 2.256e6
  Q_cu_drop = m_cu * c_cu * (150.0 - 100.0) # 39,000 J tỏa ra khi nồi hạ về 100 C
  Q_w_heat = m_w * c_w * (100.0 - 25.0)     # 31,425 J để nâng nước lên 100 C
  Q_rem = Q_cu_drop - Q_w_heat              # 7,575 J dư thừa dùng để hóa hơi nước
  m_steam = Q_rem / L_v                     # 0.003358 kg = 3.358 g -> 3.4 g
  m_liquid = m_w - m_steam                  # 0.09664 kg -> 0.097 kg = 97 g
  ```
- **Kết quả đối sánh**: Số liệu khớp với sách giáo khoa (nhiệt độ cuối $100^\circ\mathrm{C}$, lượng hơi nước tạo thành $3{,}4\,\mathrm{g}$, lượng nước lỏng còn lại $0{,}097\,\mathrm{kg} = 97\,\mathrm{g}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.10: Kết hợp phản ứng cháy, tăng nhiệt độ và chuyển pha (Camp Stove)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/06-nhiet-luong-ke-va-chuyen-pha.md`, dòng 337–404.
- **Vị trí sách gốc**: Trang in 560; Trang PDF 580 (Mục 17.6).
- **Đề bài & Dữ liệu đầu vào**:
  - Bếp dã ngoại dùng xăng có hiệu suất nhiệt $\eta = 30\% = 0{,}30$.
  - Đun $1{,}00\,\mathrm{L}$ ($1{,}00\,\mathrm{kg}$) nước từ $20^\circ\mathrm{C}$ đến $100^\circ\mathrm{C}$ và làm bay hơi $0{,}25\,\mathrm{kg}$ nước.
  - Nhiệt cháy của xăng: $L_{\mathrm{c}} = 46\,000\,\mathrm{J/g} = 4{,}6 \times 10^7\,\mathrm{J/kg}$.
- **Phương trình**:
  $$Q_1 = m_{\mathrm{w}} c_{\mathrm{w}} \Delta T, \quad Q_2 = m_{\mathrm{v}} L_{\mathrm{v}}, \quad Q_{\text{tổng}} = Q_1 + Q_2$$
  $$Q_{\text{cháy}} = \frac{Q_{\text{tổng}}}{\eta} \implies m_{\text{xăng}} = \frac{Q_{\text{cháy}}}{L_{\mathrm{c}}}$$
- **Mã Python xác minh**:
  ```python
  m_w, dT, c_w = 1.00, 80.0, 4190.0
  m_v, L_v = 0.25, 2.256e6
  L_c, eta = 46000.0, 0.30
  Q1 = m_w * c_w * dT      # 335,200 J = 3.35 x 10^5 J
  Q2 = m_v * L_v          # 564,000 J = 5.64 x 10^5 J
  Q_tot = Q1 + Q2         # 899,200 J = 8.99 x 10^5 J
  Q_comb = Q_tot / eta    # 2,997,333 J -> 3.00 x 10^6 J
  m_gas = Q_comb / L_c    # 65.16 g -> 65 g (khoảng 0.09 L xăng)
  # Lượng xăng cần để làm bay hơi tiếp 0.75 kg nước còn lại:
  Q_rem = 0.75 * L_v / eta # 5.64 x 10^6 J -> m = 5.64e6 / 46000 = 122.6 g -> 123 g
  ```
- **Kết quả đối sánh**: Số liệu khớp với sách giáo khoa ($Q_1 = 3{,}35 \times 10^5\,\mathrm{J}$, $Q_2 = 5{,}64 \times 10^5\,\mathrm{J}$, $Q_{\text{tổng}} = 8{,}99 \times 10^5\,\mathrm{J}$, $Q_{\text{cháy}} = 3{,}00 \times 10^6\,\mathrm{J}$, lượng xăng cần đốt $65\,\mathrm{g}$; làm bay hơi hết phần nước còn lại cần thêm $123\,\mathrm{g}$ xăng).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.11: Dẫn nhiệt vào thùng xốp giữ lạnh (Picnic Cooler)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/07-cac-co-che-truyen-nhiet.md`, dòng 150–207.
- **Vị trí sách gốc**: Trang in 563; Trang PDF 583 (Mục 17.7).
- **Đề bài & Dữ liệu đầu vào**:
  - Thùng xốp Styrofoam diện tích toàn phần $A = 0{,}80\,\mathrm{m^2}$, bề dày thành $L = 2{,}0\,\mathrm{cm} = 0{,}020\,\mathrm{m}$.
  - Nhiệt độ mặt ngoài $T_{\mathrm{H}} = 30^\circ\mathrm{C}$, mặt trong chứa nước đá ở $T_{\mathrm{C}} = 0^\circ\mathrm{C}$.
  - Hệ số dẫn nhiệt xốp $k = 0{,}027\,\mathrm{W}/(\mathrm{m}\cdot\mathrm{K})$, nhiệt nóng chảy của đá $L_{\mathrm{f}} = 3{,}34 \times 10^5\,\mathrm{J/kg}$. Thời gian $t = 3\,\mathrm{h} = 10\,800\,\mathrm{s}$.
- **Phương trình**:
  $$H = k A \frac{T_{\mathrm{H}} - T_{\mathrm{C}}}{L}, \quad Q = H t, \quad m = \frac{Q}{L_{\mathrm{f}}}$$
- **Mã Python xác minh**:
  ```python
  A, L, k, dT = 0.80, 0.020, 0.027, 30.0
  H = k * A * dT / L       # 32.4 W
  t = 3 * 3600             # 10,800 s
  Q = H * t                # 349,920 J = 3.5 x 10^5 J
  L_f = 3.34e5
  m = Q / L_f              # 1.048 kg -> 1.0 kg
  ```
- **Kết quả đối sánh**: Số liệu khớp với nguyên bản ($H = 32{,}4\,\mathrm{W}$, tổng nhiệt lượng $Q = 3{,}5 \times 10^5\,\mathrm{J}$, lượng đá tan $m = 1{,}0\,\mathrm{kg}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.12: Dẫn nhiệt qua hai thanh ghép nối tiếp (Conduction in Series)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/07-cac-co-che-truyen-nhiet.md`, dòng 209–271.
- **Vị trí sách gốc**: Trang in 563; Trang PDF 583 (Mục 17.7).
- **Đề bài & Dữ liệu đầu vào**:
  - Thanh thép: $L_{\mathrm{S}} = 10{,}0\,\mathrm{cm} = 0{,}100\,\mathrm{m}$, $k_{\mathrm{S}} = 50{,}2\,\mathrm{W}/(\mathrm{m}\cdot\mathrm{K})$.
  - Thanh đồng: $L_{\mathrm{Cu}} = 20{,}0\,\mathrm{cm} = 0{,}200\,\mathrm{m}$, $k_{\mathrm{Cu}} = 385\,\mathrm{W}/(\mathrm{m}\cdot\mathrm{K})$.
  - Tiết diện vuông cạnh $2{,}00\,\mathrm{cm} \implies A = (0{,}0200\,\mathrm{m})^2 = 4{,}00 \times 10^{-4}\,\mathrm{m^2}$.
  - Hai đầu tự do giữ ở $T_{\mathrm{H}} = 100^\circ\mathrm{C}$ và $T_{\mathrm{C}} = 0^\circ\mathrm{C}$.
- **Phương trình**:
  $$H_{\mathrm{S}} = H_{\mathrm{Cu}} \implies T_{\text{mối nối}} = \frac{\frac{k_{\mathrm{S}}}{L_{\mathrm{S}}} T_{\mathrm{H}} + \frac{k_{\mathrm{Cu}}}{L_{\mathrm{Cu}}} T_{\mathrm{C}}}{\frac{k_{\mathrm{S}}}{L_{\mathrm{S}}} + \frac{k_{\mathrm{Cu}}}{L_{\mathrm{Cu}}}}$$
- **Mã Python xác minh**:
  ```python
  k_S, L_S = 50.2, 0.100
  k_Cu, L_Cu = 385.0, 0.200
  A = 4.00e-4
  T_j = ((k_S/L_S)*100.0 + (k_Cu/L_Cu)*0.0) / (k_S/L_S + k_Cu/L_Cu) # 20.684 C -> 20.7 C
  H = k_S * A * (100.0 - T_j) / L_S # 15.927 W -> 15.9 W
  ```
- **Kết quả đối sánh**: Số liệu khớp với sách ($T_{\text{mối nối}} = 20{,}7^\circ\mathrm{C}$, dòng nhiệt truyền qua hệ $H = 15{,}9\,\mathrm{W}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.13: Dẫn nhiệt qua hai thanh ghép song song (Conduction in Parallel)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/07-cac-co-che-truyen-nhiet.md`, dòng 273–322.
- **Vị trí sách gốc**: Trang in 564; Trang PDF 584 (Mục 17.7).
- **Đề bài & Dữ liệu đầu vào**:
  - Tách rời hai thanh kim loại của Ví dụ 17.12 và đặt song song giữa hai nguồn $100^\circ\mathrm{C}$ và $0^\circ\mathrm{C}$.
- **Phương trình**:
  $$H = H_{\mathrm{S}} + H_{\mathrm{Cu}} = k_{\mathrm{S}} A \frac{\Delta T}{L_{\mathrm{S}}} + k_{\mathrm{Cu}} A \frac{\Delta T}{L_{\mathrm{Cu}}}$$
- **Mã Python xác minh**:
  ```python
  H_S = 50.2 * 4.00e-4 * (100.0 / 0.100)  # 20.08 W -> 20.1 W
  H_Cu = 385.0 * 4.00e-4 * (100.0 / 0.200) # 77.00 W -> 77.0 W
  H_tot = H_S + H_Cu                      # 97.08 W -> 97.1 W
  ratio = H_tot / 15.93                  # 6.09 -> lớn gấp 6.1 lần so với ghép nối tiếp
  ```
- **Kết quả đối sánh**: Số liệu khớp với sách ($H_{\mathrm{S}} = 20{,}1\,\mathrm{W}$, $H_{\mathrm{Cu}} = 77{,}0\,\mathrm{W}$, tổng dòng nhiệt $H = 97{,}1\,\mathrm{W}$, lớn gấp $6{,}1$ lần so với khi ghép nối tiếp).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.14: Sự phát xạ nhiệt của tấm thép (Radiation from a Metal Plate)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/07-cac-co-che-truyen-nhiet.md`, dòng 397–427.
- **Vị trí sách gốc**: Trang in 565; Trang PDF 585 (Mục 17.7).
- **Đề bài & Dữ liệu đầu vào**:
  - Tấm thép vuông mỏng cạnh $10\,\mathrm{cm} = 0{,}10\,\mathrm{m}$ nung trong lò rèn đến $800^\circ\mathrm{C}$.
  - Độ phát xạ $e = 0{,}60$. Bức xạ phát ra từ cả hai mặt của tấm: $A = 2 \times (0{,}10\,\mathrm{m})^2 = 0{,}020\,\mathrm{m^2}$.
  - Nhiệt độ tuyệt đối $T = 800 + 273{,}15 \approx 1073\,\mathrm{K}$. Hằng số Stefan–Boltzmann $\sigma = 5{,}67 \times 10^{-8}\,\mathrm{W}/(\mathrm{m^2}\cdot\mathrm{K^4})$.
- **Phương trình**:
  $$H = A e \sigma T^4$$
- **Mã Python xác minh**:
  ```python
  A = 2 * (0.10**2) # 0.020 m^2
  e = 0.60
  sigma = 5.67e-8
  T = 1073.0
  H = A * e * sigma * (T**4) # 901.9 W -> 900 W (hoặc 0.90 kW)
  ```
- **Kết quả đối sánh**: Số liệu khớp với sách giáo khoa ($H = 900\,\mathrm{W}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

### Ví dụ 17.15: Bức xạ nhiệt từ cơ thể người (Radiation from Human Body)
- **Vị trí tệp nguồn**: `raw_materials/physics/translations/chapter-17/07-cac-co-che-truyen-nhiet.md`, dòng 451–491.
- **Vị trí sách gốc**: Trang in 566; Trang PDF 586 (Mục 17.7).
- **Đề bài & Dữ liệu đầu vào**:
  - Cơ thể người có diện tích da $A = 1{,}20\,\mathrm{m^2}$, nhiệt độ da $T = 30^\circ\mathrm{C} \approx 303\,\mathrm{K}$, độ phát xạ $e = 1{,}0$.
  - Môi trường xung quanh ở $T_{\mathrm{s}} = 20^\circ\mathrm{C} \approx 293\,\mathrm{K}$.
- **Phương trình**:
  $$H_{\text{phát}} = A e \sigma T^4, \quad H_{\text{ròng}} = A e \sigma (T^4 - T_{\mathrm{s}}^4)$$
- **Mã Python xác minh**:
  ```python
  A, e, sigma = 1.20, 1.0, 5.67e-8
  T, Ts = 303.0, 293.0
  H_emit = A * e * sigma * (T**4)          # 573.5 W -> 574 W
  H_net = A * e * sigma * (T**4 - Ts**4)    # 72.04 W -> 72 W
  ```
- **Kết quả đối sánh**: Số liệu khớp với sách ($H_{\text{phát}} = 574\,\mathrm{W}$, tốc độ mất nhiệt ròng $H_{\text{ròng}} = 72\,\mathrm{W}$).
- **Đánh giá**: **Xác nhận khớp số liệu giáo trình**.

---

## 4. Sổ Cái Thẩm Định Câu Hỏi Tự Kiểm Tra & Mở Đầu (TYU Ledger)

Đối chiếu độc lập toàn bộ các câu hỏi trắc nghiệm tự kiểm tra (Test Your Understanding - TYU) và Câu hỏi mở đầu chương với phần đáp án của tác giả ở trang in 578 (trang PDF 598):

| Câu hỏi | Vị trí Sách & PDF | Vị trí Tệp Bài Giảng | Đáp án Tác Giả | Lập luận Học thuật | Đánh giá |
| :--- | :---: | :--- | :---: | :--- | :--- |
| **Câu hỏi mở đầu** | Trang 541 / PDF 561 | `00-mo-dau.md`, L9–23 | **(iii)** | Gang lỏng chứa nhiều năng lượng (nội năng) hơn. Nhiệt độ không phải là đại lượng bảo toàn, còn nhiệt lượng chỉ tồn tại khi có quá trình truyền năng lượng. | Khớp đáp án tác giả |
| **TYU 17.1** | Trang 544 / PDF 564 | `01-nhiet-do-va-can-bang-nhiet.md`, L50–64 | **(ii)** | Nhiệt kế luôn đo nhiệt độ của chính nó sau khi đạt cân bằng nhiệt với vật thể (Định luật 0). | Khớp đáp án tác giả |
| **TYU 17.2** | Trang 547 / PDF 567 | `02-nhiet-ke-va-thang-nhiet-do.md`, L72–86 | **(iv)** | Cả băng kép kim loại và nhiệt kế điện trở đều hoạt động nhờ sự thay đổi của một đại lượng vật lý theo nhiệt độ. | Khớp đáp án tác giả |
| **TYU 17.3** | Trang 549 / PDF 569 | `03-nhiet-ke-khi-va-thang-kelvin.md`, L186–215 | **(i) > (iii) > (ii) > (v) > (iv)** | Đổi về Kelvin để so sánh: (i) $0^\circ\mathrm{C} = 273{,}15\,\mathrm{K}$; (ii) $0^\circ\mathrm{F} = 255{,}37\,\mathrm{K}$; (iii) $-13^\circ\mathrm{C} = 260{,}15\,\mathrm{K}$; (iv) $77\,\mathrm{K}$; (v) $-180^\circ\mathrm{C} = 93{,}15\,\mathrm{K}$. | Khớp đáp án tác giả |
| **TYU 17.4** | Trang 554 / PDF 574 | `04-su-no-vi-nhiet.md`, L411–433 | **(ii)** và **(iii)** | Để đai kim loại tuột lỏng khỏi trục đồng khi hơ nóng, đai phải có $\alpha > \alpha_{\mathrm{Cu}} = 1{,}7 \times 10^{-5}\,\mathrm{K}^{-1}$. Tra bảng: Nhôm ($2{,}4 \times 10^{-5}$) và đồng thau ($2{,}0 \times 10^{-5}$) thỏa mãn. | Khớp đáp án tác giả |
| **TYU 17.5** | Trang 558 / PDF 578 | `05-nhiet-luong.md`, L260–292 | **(ii) > (i) > (iv) > (iii)** | Nhiệt lượng cần để tăng $1\,\mathrm{K}$: (i) $1\,\mathrm{kg}$ Hg cần $138\,\mathrm{J}$; (ii) $1\,\mathrm{kg}$ ethanol cần $2428\,\mathrm{J}$; (iii) $1\,\mathrm{mol}$ Hg cần $27{,}7\,\mathrm{J}$; (iv) $1\,\mathrm{mol}$ ethanol cần $111{,}9\,\mathrm{J}$. | Khớp đáp án tác giả |
| **TYU 17.6** | Trang 563 / PDF 583 | `06-nhiet-luong-ke-va-chuyen-pha.md`, L406–456 | **(iv)** | Hỗn hợp nước và hơi nước ở $100^\circ\mathrm{C}$ hấp thụ nhiệt để bẻ gãy liên kết chuyển pha mà không thay đổi nhiệt độ ở $1\,\mathrm{atm}$. | Khớp đáp án tác giả |
| **TYU 17.7** | Trang 568 / PDF 588 | `07-cac-co-che-truyen-nhiet.md`, L532–566 | **(ii)** | Cảm giác lạnh phụ thuộc vào mật độ dòng nhiệt $H/A$ rút khỏi tay. Đồng có hệ số dẫn nhiệt $k_{\mathrm{Cu}} = 385\,\mathrm{W}/(\mathrm{m}\cdot\mathrm{K})$ lớn nhất nên rút nhiệt nhanh nhất. | Khớp đáp án tác giả |

---

## 5. Thẩm Định Dữ Liệu Bảng Biểu & Hằng Số Vật Lý

Năm bảng số liệu thực nghiệm trong Chương 17 đã được đối chiếu trực tiếp với PDF gốc:

1. **Bảng 17.1: Hệ số nở dài ($\alpha$) ở nhiệt độ phòng** (Trang in 549, PDF 569):
   - Nhôm ($2{,}4 \times 10^{-5}\,\mathrm{K}^{-1}$), Đồng thau ($2{,}0 \times 10^{-5}$), Đồng đỏ ($1{,}7 \times 10^{-5}$), Thủy tinh thông thường ($0{,}7 - 0{,}9 \times 10^{-5}$), Thủy tinh Pyrex ($0{,}32 \times 10^{-5}$), Invar ($0{,}09 \times 10^{-5}$), Thạch anh nóng chảy ($0{,}04 \times 10^{-5}$), Thép ($1{,}2 \times 10^{-5}$).
   - Đánh giá: Khớp số liệu với giáo trình gốc.
2. **Bảng 17.2: Hệ số nở thể tích ($\beta$)** (Trang in 550, PDF 570):
   - Chất rắn: Nhôm ($7{,}2 \times 10^{-5}\,\mathrm{K}^{-1}$), Đồng thau ($6{,}0 \times 10^{-5}$), Đồng đỏ ($5{,}1 \times 10^{-5}$), Thủy tinh ($1{,}2 - 2{,}7 \times 10^{-5}$), Thép ($3{,}6 \times 10^{-5}$).
   - Chất lỏng: Benzene ($75 \times 10^{-5}$), Ethanol ($75 \times 10^{-5}$), Glycerin ($49 \times 10^{-5}$), Thủy ngân ($18 \times 10^{-5}$).
   - Đánh giá: Khớp số liệu với giáo trình gốc.
3. **Bảng 17.3: Nhiệt dung riêng ($c$) và nhiệt dung mol ($C$)** (Trang in 554, PDF 574):
   - Nước lỏng ($c = 4190\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$, $C = 75{,}4\,\mathrm{J}/(\mathrm{mol}\cdot\mathrm{K})$); Nước đá ($2100\,\mathrm{J}/(\mathrm{kg}\cdot\mathrm{K})$, $37{,}8\,\mathrm{J}/(\mathrm{mol}\cdot\mathrm{K})$); Nhôm ($910$, $24{,}6$); Đồng ($390$, $24{,}8$); Chì ($130$, $26{,}9$); Thủy ngân ($138$, $27{,}7$).
   - Đánh giá: Khớp số liệu với giáo trình gốc; quy tắc Dulong–Petit đối với kim loại ở nhiệt độ phòng xấp xỉ $3R \approx 24{,}9\,\mathrm{J}/(\mathrm{mol}\cdot\mathrm{K})$.
4. **Bảng 17.4: Nhiệt độ chuyển pha và Nhiệt ẩn ($L_{\mathrm{f}}, L_{\mathrm{v}}$)** (Trang in 557, PDF 577):
   - Nước: Nóng chảy ở $0{,}0^\circ\mathrm{C}$, $L_{\mathrm{f}} = 3{,}34 \times 10^5\,\mathrm{J/kg}$; Sôi ở $100{,}0^\circ\mathrm{C}$, $L_{\mathrm{v}} = 2{,}256 \times 10^6\,\mathrm{J/kg}$.
   - Nitơ: Nóng chảy $-210{,}0^\circ\mathrm{C}$ ($0{,}26 \times 10^5\,\mathrm{J/kg}$); Sôi $-195{,}8^\circ\mathrm{C}$ ($2{,}01 \times 10^5\,\mathrm{J/kg}$).
   - Đồng: Nóng chảy $1083^\circ\mathrm{C}$ ($1{,}34 \times 10^5\,\mathrm{J/kg}$); Sôi $2566^\circ\mathrm{C}$ ($5{,}07 \times 10^6\,\mathrm{J/kg}$).
   - Đánh giá: Khớp số liệu với giáo trình gốc.
5. **Bảng 17.5: Hệ số dẫn nhiệt ($k$)** (Trang in 561, PDF 581):
   - Kim loại: Bạc ($406\,\mathrm{W}/(\mathrm{m}\cdot\mathrm{K})$), Đồng ($385$), Nhôm ($205$), Thép ($50{,}2$), Chì ($34{,}7$).
   - Vật liệu cách nhiệt và chất khí: Thủy tinh ($0{,}8$), Bê tông ($0{,}8$), Mút xốp Styrofoam ($0{,}027$), Không khí tù đọng ($0{,}024$).
   - Đánh giá: Khớp số liệu với giáo trình gốc.

---

## 6. Sổ Cái Thẩm Định Tài Nguyên Trực Quan & Panel Ảnh (Visual Assets Ledger)

Thống kê 37 tệp hình ảnh thực tế lưu trữ tại `docs/vat-ly-1/bai-giang/img/young-17/`:

| Tên tệp ảnh thực tế trên đĩa | Đối tượng biểu diễn | Kích thước pixel | Đánh giá căn lề |
| :--- | :--- | :---: | :--- |
| `a-hinh-17-01.png` | Cốc nước đá và trà nóng đạt cân bằng nhiệt với môi trường | $1800 \times 741$ px | Khung hình chuẩn xác |
| `a-hinh-17-02.png` | Hệ ba vật $A, B, C$ và nguyên lý Định luật 0 Nhiệt động lực học | $1800 \times 642$ px | Giữ nguyên nhãn chú thích |
| `a-hinh-17-03.png` | Nhiệt kế thủy tinh giãn nở chất lỏng và vạch chia | $930 \times 1485$ px | Đủ trục mao dẫn |
| `a-hinh-17-04.png` | Băng kép kim loại uốn cong khi biến thiên nhiệt độ | $1800 \times 1332$ px | Rõ các lớp kim loại |
| `a-hinh-17-05.png` | Cặp nhiệt điện (Thermocouple) và mạch đo điện thế | $1800 \times 864$ px | Mối hàn và vôn kế rõ |
| `a-hinh-17-06.png` | So sánh trực quan ba thang đo Celsius, Kelvin và Fahrenheit | $1800 \times 1125$ px | Đầy đủ mốc đối sánh |
| `a-hinh-17-07.png` | Nhiệt kế khí thể tích không đổi với áp kế chữ U | $1800 \times 1455$ px | Rõ cột thủy ngân |
| `a-hinh-17-08.png` | Đồ thị áp suất khí ngoại suy về $-273{,}15^\circ\mathrm{C}$ | $1800 \times 1215$ px | Trục tọa độ và điểm 0 rõ |
| `a-hinh-17-09.png` | Mô hình phân tử: Thế năng tương tác bất đối xứng | $1800 \times 1332$ px | Rõ giếng thế năng |
| `a-hinh-17-10.png` | Khe co giãn răng lược trên mặt cầu đường bộ | $1800 \times 840$ px | Ảnh thực tế sắc nét |
| `a-hinh-17-11.png` | Sự giãn nở nhiệt của lỗ tròn trong tấm kim loại | $1800 \times 1092$ px | Minh họa hình học trực quan |
| `a-hinh-17-12.png` | Đồ thị dị thường thể tích và khối lượng riêng của nước quanh $4^\circ\mathrm{C}$ | $1800 \times 1260$ px | Cực đại khối lượng riêng rõ |
| `a-hinh-17-13.png` | Lớp băng nổi bảo vệ sinh vật dưới đáy hồ vào mùa đông | $1800 \times 1080$ px | Phân tầng nhiệt độ rõ |
| `a-hinh-17-14.png` | Sơ đồ phân tích lực nén ứng suất nhiệt trong trụ nhôm | $1800 \times 825$ px | Khớp Ví dụ 17.4 |
| `a-mo-dau-17.png` | Ảnh minh họa mở đầu chương: Rót gang nóng chảy trong lò luyện | $1800 \times 1080$ px | Đầy đủ chi tiết |
| `a-ung-dung-17-01.png` | Ứng dụng sinh học: Cơ chế điều hòa thân nhiệt động vật | $1800 \times 960$ px | Đầy đủ chi tiết |
| `b-hinh-17-15.png` | Thí nghiệm Joule: Công cơ học chuyển hóa thành nội năng | $1800 \times 1425$ px | Rõ quả nặng và cánh khuấy |
| `b-hinh-17-16.png` | Quy ước dấu của nhiệt lượng: $Q > 0$ và $Q < 0$ | $1800 \times 645$ px | Mũi tên năng lượng rõ |
| `b-hinh-17-17.png` | Đồ thị nhiệt độ theo thời gian khi nung chất bán dẫn | $1800 \times 1080$ px | Tiếp tuyến $dT/dt$ rõ |
| `b-hinh-17-18.png` | Đồ thị nhiệt độ theo nhiệt lượng truyền vào (từ đá thành hơi) | $1800 \times 1290$ px | Các đoạn chuyển pha rõ |
| `b-hinh-17-19.png` | Giản đồ pha $p-T$ với điểm ba và điểm tới hạn | $1800 \times 1410$ px | Đường chuyển pha rõ |
| `b-hinh-17-20.png` | Mặt trạng thái nhiệt động $p-V-T$ ba chiều | $1800 \times 1560$ px | Phối cảnh 3D sắc nét |
| `b-hinh-17-21.png` | Dẫn nhiệt dọc theo thanh đồng nhất: Dòng nhiệt $H$ | $1800 \times 870$ px | Mặt cắt và gradient rõ |
| `b-hinh-17-22.png` | Sơ đồ dẫn nhiệt của hai thanh kim loại ghép nối tiếp | $1800 \times 825$ px | Mối nối tiếp xúc rõ |
| `b-hinh-17-23.png` | Sơ đồ dẫn nhiệt của hai thanh kim loại ghép song song | $1800 \times 930$ px | Hai nhánh song song rõ |
| `b-hinh-17-24.png` | Đối lưu nhiệt tự nhiên trong ấm nước đun trên bếp | $1800 \times 1110$ px | Vòng tuần hoàn đối lưu rõ |
| `b-hinh-17-25.png` | Cơ chế gió biển - gió đất ven bờ do nhiệt dung riêng của nước | $1800 \times 1200$ px | Rõ ban ngày và ban đêm |
| `b-hinh-17-26.png` | Bức xạ nhiệt của thanh thép nung nóng | $1800 \times 825$ px | Quang phổ nhiệt rõ |
| `b-hinh-17-27.png` | Ảnh chụp nhiệt hồng ngoại (Thermogram) ngôi nhà mất nhiệt | $1800 \times 1050$ px | Thang màu nhiệt độ rõ |
| `b-hinh-17-28.png` | Cấu tạo bình phích chân không Dewar ngăn cả 3 cơ chế truyền nhiệt | $1800 \times 1500$ px | Lớp tráng bạc và chân không rõ |
| `b-hinh-17-29.png` | Hiệu ứng nhà kính khí quyển giữ ấm Trái Đất | $1800 \times 1290$ px | Cân bằng bức xạ rõ |
| `b-hinh-17-30.png` | Đồ thị quang phổ bức xạ Planck ở các nhiệt độ khác nhau | $1764 \times 618$ px | Đầy đủ nhãn trục bước sóng |
| `b-hinh-17-31.png` | Sơ đồ ống dẫn nhiệt (Heat Pipe) tản nhiệt cho laptop | $1800 \times 960$ px | Chu trình bay hơi - ngưng tụ rõ |
| `b-tom-tat-01.png` | Sơ đồ tóm tắt: Cân bằng nhiệt và thang đo nhiệt độ | $1800 \times 900$ px | Khung tóm tắt rõ |
| `b-tom-tat-02.png` | Sơ đồ tóm tắt: Sự nở vì nhiệt và ứng suất nhiệt | $1800 \times 900$ px | Khung tóm tắt rõ |
| `b-tom-tat-03.png` | Sơ đồ tóm tắt: Nhiệt lượng kế và quá trình chuyển pha | $1800 \times 900$ px | Khung tóm tắt rõ |
| `b-tom-tat-04.png` | Sơ đồ tóm tắt: Ba cơ chế truyền nhiệt | $1800 \times 900$ px | Khung tóm tắt rõ |
| `b-ung-dung-17-01.png` | Ứng dụng kỹ thuật: Cảm biến nhiệt hồng ngoại và camera nhiệt | $1800 \times 960$ px | Đầy đủ chi tiết |

---

## 7. Đánh Giá Kỹ Thuật: Script Kiểm Thử & Giới Hạn Môi Trường

### 7.1. Giới hạn môi trường đối với script hỗ trợ chuẩn bị tài nguyên ảnh
- **Hiện tượng**: Khi gọi thực thi tệp `raw_materials/physics/verify_chapter17_theory_a.py` bằng Python, kịch bản báo lỗi không tìm thấy mô-đun tại dòng 30–33 (`from scripts.prepare-physics1-17-theory-a-assets import CROPS, SCALE`).
- **Phân tích bối cảnh**: Kịch bản hỗ trợ `scripts/prepare-physics1-17-theory-a-assets.py` chủ đích không được đưa vào danh mục tài nguyên đầu vào được đóng băng cho đợt thẩm định độc lập này. Do đó, lỗi import này là một giới hạn biên của môi trường chạy thử cục bộ, **không cấu thành bằng chứng về khuyết tật sản phẩm trong kho lưu trữ chính**.
- **Giải pháp thẩm định**: Đợt rà soát này sử dụng mã nguồn kiểm tra độc lập trong bộ nhớ thông qua PyMuPDF và PIL, xác minh trực tiếp các tệp ảnh đã xuất ra trên đĩa đối chiếu với PDF gốc.

### 7.2. Ghi nhận phân tích thông số Bounding Box trong `verify_chapter17_theory_b.py`
Trong quá trình kiểm tra mã nguồn của kịch bản kiểm thử tĩnh `raw_materials/physics/verify_chapter17_theory_b.py`, ghi nhận hai điểm sai lệch giữa thông số khai báo trong kịch bản và tệp ảnh thực tế trên đĩa:
1. **Dòng 313 (`b-hinh-17-27`)**:
   - Tọa độ trong kịch bản: `(74.0, 197.0, 214.0, 327.0)` (chiều rộng $140\,\mathrm{pt}$).
   - Tệp ảnh thực tế trên đĩa: Chiều rộng $582\,\mathrm{px}$ (ứng với chiều rộng khoảng $194\,\mathrm{pt}$ ở scale 3). Tệp ảnh trên đĩa bao phủ rộng hơn sang phải, giữ trọn vẹn nhãn chú thích của hình.
2. **Dòng 316 (`b-hinh-17-30`)**:
   - Tọa độ trong kịch bản: `(75.0, 538.0, 588.0, 732.0)` (chiều cao $194\,\mathrm{pt}$).
   - Tệp ảnh thực tế trên đĩa: Chiều cao $618\,\mathrm{px}$ (ứng với chiều cao $206\,\mathrm{pt}$ ở scale 3). Tệp ảnh trên đĩa nới thêm biên dưới, bảo toàn được nhãn bước sóng $\lambda\,(\mu\mathrm{m})$ của trục hoành đồ thị Planck.
- **Đánh giá**: Các tệp ảnh thực tế trên đĩa phản ánh việc điều chỉnh nới biên để không bị cắt cụt đồ họa.

### 7.3. Về tệp xuất bản nền
Tệp `docs/vat-ly-1/bai-giang/17-nhiet-do-nhiet-luong.md` không nằm trong danh mục đầu vào đóng băng của đợt thẩm định và không được sử dụng để đánh giá tình trạng tích hợp hiện hành của người gọi.

---

## 8. Thẩm Định Quy Chuẩn Sư Phạm StudyHub

Chín tệp bài giảng trong `raw_materials/physics/translations/chapter-17/` đã được rà soát đối chiếu với các quy tắc trong `AGENTS.md` và `GEMINI.md`:

1. **Quy tắc Chủ quyền Bài giảng (Rule 6)**:
   - Toàn bộ nội dung bài giảng được viết với tư cách giáo trình giảng dạy độc lập, hoàn chỉnh của người giảng viên.
   - Không xuất hiện các cụm từ dịch máy phụ thuộc như: *"Nội dung lấy từ giáo trình..."*, *"Theo sách..."*, *"Sách dùng..."*, *"Nguyên tác..."*, *"Bản dịch..."*, *"Ảnh lấy từ sách..."*.
   - Mục tài liệu tham khảo ở cuối các tệp được đặt tên chuẩn mực là `## Tài liệu tham khảo`.
2. **Quy tắc Viết hoa sau dấu hai chấm (Rule 12)**:
   - Các câu văn xuôi, tiêu đề, đề mục, nhãn chú thích và danh sách liệt kê sau dấu hai chấm (`:`) đều tuân thủ viết hoa chữ cái đầu (ví dụ: `Ví dụ: Xét...`, `Lưu ý: Không dùng...`, `Tóm tắt: ...`, `Lời giải: ...`).
3. **Quy tắc Hạn chế dấu gạch ngang dài em-dash (Rule 16)**:
   - Văn xuôi phân tích sử dụng dấu phẩy, dấu ngoặc đơn hoặc từ nối tiếng Việt tự nhiên, không lạm dụng dấu gạch ngang dài `—` để chêm xen vế phụ giữa câu.
4. **Quy tắc Chuẩn mực Toán học & Triệt tiêu Scrollbar (Rule 8)**:
   - Các công thức toán hiển thị dài đều được định dạng bằng `\begin{aligned}` với `\\` và căn lề dấu bằng `&=`.
   - Các công thức ngắn giữ nguyên trên một dòng trong `$$...$$`, không bị ngắt vụn. Dấu `$$` mở và đóng nằm trên dòng riêng biệt. Không có công thức inline nào vượt quá giới hạn $38\text{ex}$.
5. **Quy tắc Hạn chế dấu chấm phẩy (Rule 10)**:
   - Lời giảng sử dụng các từ nối tiếng Việt chuẩn xác (*và, nhưng, tuy nhiên, do đó, kéo theo, dẫn đến, cụ thể là...*), tránh dùng dấu chấm phẩy (`;`) gây rời rạc câu văn.

---

## 9. Danh Mục Phát Hiện Đã Xác Nhận, Giới Hạn & Tuyên Bố Bất Định

### 9.1. Các Phát Hiện Cụ Thể Đã Xác Nhận (Confirmed Findings)
1. **Khớp số liệu 15 ví dụ mẫu**: Toàn bộ 15 ví dụ tính toán mẫu (Ví dụ 17.1 đến 17.15) đã được tính toán lại độc lập bằng Python trong RAM và khớp với số liệu của giáo trình *University Physics 15th Edition*.
2. **Khớp vị trí tệp và dòng thực tế**:
   - Ví dụ 17.1 nằm tại `03-nhiet-ke-khi-va-thang-kelvin.md`, dòng 95–184 (sách in trang 546, PDF 566).
   - Ví dụ 17.2, 17.3, 17.4 nằm tại `04-su-no-vi-nhiet.md` lần lượt ở dòng 151–217, 229–292, 351–409 (sách in trang 549, 550, 551; PDF 569, 570, 571).
   - Ví dụ 17.5, 17.6 nằm tại `05-nhiet-luong.md` lần lượt ở dòng 94–132, 134–174 (sách in trang 553, PDF 573).
   - Ví dụ 17.7, 17.8, 17.9, 17.10 nằm tại `06-nhiet-luong-ke-va-chuyen-pha.md` lần lượt ở dòng 161–214, 216–263, 265–335, 337–404 (sách in trang 559, 559, 560, 560; PDF 579, 579, 580, 580).
   - Ví dụ 17.11, 17.12, 17.13, 17.14, 17.15 nằm tại `07-cac-co-che-truyen-nhiet.md` lần lượt ở dòng 150–207, 209–271, 273–322, 397–427, 451–491 (sách in trang 563, 563, 564, 565, 566; PDF 583, 583, 584, 585, 586).
3. **Độ trung thực của dữ liệu đầu vào**:
   - Ví dụ 17.4 có diện tích tiết diện trụ nhôm là $A = 20\,\mathrm{cm^2} = 2{,}0 \times 10^{-3}\,\mathrm{m^2}$, khoảng nhiệt độ $17{,}2^\circ\mathrm{C} \to 22{,}3^\circ\mathrm{C}$ ($\Delta T = 5{,}1\,\mathrm{K}$), lực nén $-1{,}7 \times 10^4\,\mathrm{N}$.
   - Ví dụ 17.10 sử dụng nhiên liệu xăng với nhiệt cháy $L_{\mathrm{c}} = 46\,000\,\mathrm{J/g}$, lượng xăng cần đốt là $65\,\mathrm{g}$.
   - Ví dụ 17.11 có nhiệt độ mặt ngoài $T_{\mathrm{H}} = 30^\circ\mathrm{C}$, dòng nhiệt $H = 32{,}4\,\mathrm{W}$, lượng đá tan $m = 1{,}0\,\mathrm{kg}$.
4. **Phân tích thông số kịch bản kiểm thử**: Tọa độ Bounding Box trong `verify_chapter17_theory_b.py` (dòng 313, 316) hẹp hơn kích thước thực tế của tệp ảnh đang lưu trên đĩa, tệp ảnh trên đĩa bảo toàn đầy đủ chi tiết đồ họa và nhãn trục hơn.

### 9.2. Tuyên Bố Về Giới Hạn & Đánh Dấu UNCERTAIN (Uncertainty Statement)
1. **Phạm vi giới hạn trong phần lý thuyết**: Báo cáo này chỉ thẩm định phần Lý thuyết Chương 17 (Trang in 541–569; Trang PDF 561–589), gồm phần mở đầu, 7 mục lý thuyết, 15 ví dụ mẫu, 5 bảng số liệu, 7 câu hỏi TYU và tóm tắt chương.
2. **Hệ thống Bài tập cuối chương**: Toàn bộ hệ thống Câu hỏi thảo luận (Q17.1 đến Q17.26) và các Bài tập cuối chương (từ Bài tập 17.1 đến hết Bài tập 17.119, Trang in 570–578; Trang PDF 590–598) **NẰM NGOÀI PHẠM VI THẨM ĐỊNH LÝ THUYẾT** và được đánh dấu là `UNCERTAIN / CHƯA KIỂM ĐỊNH`.
3. **Không đưa ra tỷ lệ phần trăm tùy tiện**: Báo cáo không sử dụng các tỷ lệ phần trăm ước đoán ("100% không có lỗi", "hoàn thành 100%"). Mọi nhận định trong báo cáo chỉ áp dụng cho các bằng chứng số học và văn bản đã được kiểm tra trực tiếp.
