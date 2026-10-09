---
course: xu-ly-du-lieu
lecture: bai-14-ke-chuyen-bang-du-lieu
section: lecture
title: "Trình bày & thẩm định một phân tích dữ liệu"
prerequisites: ["ky-vong","gia-tri-thieu","thong-ke-mo-ta","ket-luan-nhan-qua"]
lessonStatus: ready
description: "Nghệ thuật kể chuyện bằng dữ liệu có trách nhiệm: cấu trúc Kim tự tháp Minto, bóc trần nghịch lý Simpson, chuẩn hóa ngôn ngữ đo lường và quy trình thẩm định 4 bước."
---

Chúng ta bước vào bài giảng tổng kết của toàn bộ môn học. Đến thời điểm này, bạn đã làm chủ một chuỗi kỹ năng kỹ nghệ dữ liệu toàn diện: từ việc hiểu sâu cấu trúc bộ nhớ của NumPy, thao tác với DataFrame và cơ chế Copy-on-Write của pandas, xử lý chuỗi và dữ liệu thời gian, làm sạch dữ liệu quan hệ chéo bảng, đến việc kiểm soát chất lượng đầu ra của mô hình ngôn ngữ lớn và xây dựng các biểu đồ chuẩn mực. Tuy nhiên, toàn bộ khối lượng công việc kỹ thuật đồ sộ đó sẽ trở nên vô nghĩa nếu khâu cuối cùng bị gãy đổ: **khâu phiên dịch kết quả tính toán thành kết luận khoa học và truyền tải chúng tới những người ra quyết định**.

Trong thực tế, một bản báo cáo có thể chứa những con số hoàn toàn chính xác về mặt số học nhưng lại dẫn dắt người đọc tới những hành động sai lầm nghiêm trọng. Điều này thường xuất phát từ việc người phân tích không bóc tách sự biến động trong cơ cấu nhóm, sử dụng từ ngữ giật gân vượt quá bằng chứng, đánh tráo giữa số lượng và tỷ lệ, hoặc vội vã quy kết một mối tương quan thuần túy thành quan hệ nhân quả.

Bài học kết khóa này tích hợp toàn bộ kiến thức của chương trình thành một khung phương pháp luận hoàn chỉnh: cấu trúc lập luận Kim tự tháp Minto, bản chất toán học của Nghịch lý Simpson, chuẩn mực diễn đạt đúng mức giữa phần trăm và điểm phần trăm, và quy trình thẩm định 4 bước để thẩm định độc lập bất kỳ báo cáo dữ liệu nào, đặc biệt là các báo cáo do trí tuệ nhân tạo sinh ra.

---

## 1. Cấu trúc giao tiếp dữ liệu: Nguyên lý Kim tự tháp Minto

Khi trình bày một phân tích kỹ thuật phức tạp cho ban lãnh đạo hay các đối tác nghiệp vụ, một sai lầm kinh điển của các kỹ sư là trình bày theo trình tự thời gian mà họ đã làm: bắt đầu từ việc tải dữ liệu ra sao, làm sạch thế nào, gặp bao nhiêu lỗi kỹ thuật, rồi mới đưa ra kết luận ở trang cuối cùng. Cách tiếp cận này khiến người nghe kiệt sức trước khi nắm bắt được thông điệp chính.

Phương pháp luận **Kim tự tháp Minto (The Minto Pyramid Principle)** của Barbara Minto đảo ngược hoàn toàn quy trình này theo cấu trúc từ trên xuống (Top-Down):

```
       [1. KẾT LUẬN ĐIỀU HÀNH]  <--- Thông điệp quan trọng nhất (Takeaway)
                 │
       [2. BẰNG CHỨNG ĐỊNH LƯỢNG]  <--- Số liệu, so sánh và đồ thị minh chứng
                 │
       [3. PHẠM VI & GIỚI HẠN]  <--- Điều kiện áp dụng, ngoại lệ, cảnh báo
                 │
    [4. CHI TIẾT PHƯƠNG PHÁP]  <--- Cỡ mẫu, mã nguồn, phụ lục kỹ thuật
```

1. **Đỉnh kim tự tháp (Kết luận điều hành)**: Đưa ra ngay thông điệp cốt lõi và câu trả lời trực tiếp cho câu hỏi của bên đặt hàng (ví dụ: *"Giá thuê điển hình ở Santiago là 59.000 CLP/đêm, thấp hơn đáng kể so với mức bình quân 118.000 CLP"*).
2. **Tầng thứ hai (Bằng chứng định lượng)**: Cung cấp các số liệu thống kê chủ chốt và biểu đồ trực quan hỗ trợ trực tiếp cho kết luận (ví dụ: *"Phân phối giá bị lệch phải bởi 177 giá trị cực đoan; trung vị phản ánh đúng phong độ thị trường vì gần như không bị ảnh hưởng bởi ngoại lai"*).
3. **Tầng thứ ba (Phạm vi và Giới hạn)**: Nêu rõ ranh giới của kết luận để người ra quyết định không hiểu sai (ví dụ: *"Kết luận chỉ áp dụng cho giá niêm yết một đêm, chưa bao gồm phí dọn dẹp và phí dịch vụ"*).
4. **Đáy kim tự tháp (Chi tiết phương pháp và Phụ lục)**: Ghi lại các thông số kỹ thuật phục vụ việc kiểm toán độc lập (ví dụ: *"Phân tích dựa trên 17.688 căn hộ hợp lệ ở mốc chụp 29/06/2026 sau khi loại bỏ 846 căn hộ khuyết thiếu giá trong báo cáo qa_report"*).

Cấu trúc này giúp người quản lý bận rộn nắm bắt ngay hành động cần làm trong 30 giây đầu tiên, trong khi các chuyên gia kiểm toán vẫn có đầy đủ căn cứ kỹ thuật ở các tầng dưới để thẩm định độ tin cậy.

---

## 2. Chuẩn mực ngôn từ: Lời đúng mức (Calibrated Language) vs Phóng đại (Hyperbole)

Khoa học dữ liệu là một bộ môn thực nghiệm đòi hỏi sự khiêm nhường trước sự thật khách quan. Một nhà khoa học dữ liệu xuất sắc phải biết kìm chế cám dỗ sử dụng những tính từ khoa trương để làm cho kết quả của mình trông có vẻ "ấn tượng".

### Đối chiếu các cặp diễn đạt: Đúng mức và Quá mức

| Số liệu quan sát được | Diễn đạt quá mức (Thiên lệch / Giật gân) | Diễn đạt đúng mức (Khoa học / Chuẩn mực) | Lý do hiệu chỉnh |
| :--- | :--- | :--- | :--- |
| **+53.7% YoY** (T5/2026 so với T5/2025) | *"Thị trường bùng nổ thần kỳ, vượt mọi kỷ lục lịch sử"* | *"Thị trường ghi nhận mức tăng trưởng mạnh mẽ 53.7% so với cùng kỳ năm trước"* | Mức tăng 53.7% là mạnh mẽ, nhưng việc dùng từ "thần kỳ" hay "vượt mọi kỷ lục" là võ đoán khi chưa có dữ liệu 10 năm. |
| **+3.0% MoM** (T5/2026 so với T4/2026) | *"Bứt phá thần tốc trong tháng 5"* | *"Lượng đánh giá tháng 5 tăng nhẹ 3.0% so với tháng liền trước"* | Mức tăng 3.0% giữa hai tháng liên tiếp là một biến động bình thường, tuyệt đối không thể gọi là "bứt phá thần tốc". |
| **Hệ số tương quan $r = 0.081$** giữa nhiệt độ và số đánh giá | *"Nhiệt độ thời tiết quyết định rõ rệt tới lượng khách đặt phòng"* | *"Tương quan tuyến tính giữa nhiệt độ và lượng đánh giá là rất yếu ($r = 0.081$), không có ý nghĩa thực tiễn"* | Hệ số $r < 0.1$ biểu thị mối liên hệ hầu như bằng không; quy kết "quyết định rõ rệt" là hoàn toàn sai bản chất toán học. |
| **Đúng 1 chỗ ở** đòi hỏi ở tối thiểu 730 đêm | *"Nhiều chủ nhà đang áp đặt các quy định cho thuê kỳ quặc"* | *"Ghi nhận một trường hợp cá biệt đòi hỏi thời gian lưu trú tối thiểu 730 đêm cần được gắn cờ xem xét"* | Một trường hợp đơn lẻ không đại diện cho "nhiều chủ nhà". |
| **Nhóm tiếng Tây Ban Nha chiếm 65.4%** (dùng quy tắc từ khóa thô) | *"Chắc chắn 2/3 lượng du khách đến từ các nước nói tiếng Tây Ban Nha"* | *"Khoảng 65.4% nhận xét được viết bằng tiếng Tây Ban Nha theo bộ lọc từ khóa ban đầu, cần kiểm chứng thêm trên mẫu chuẩn"* | Quy tắc từ khóa thô chưa được kiểm định độ chính xác; ngôn ngữ đánh giá chưa đồng nhất tuyệt đối với quốc tịch du khách. |

### Phân biệt rạch ròi: Phần trăm (%) và Điểm phần trăm (pp)

Một sự nhầm lẫn tai hại trong báo cáo kinh tế là việc đánh đồng giữa **thay đổi tương đối (%)** và **chênh lệch tuyệt đối (điểm phần trăm - percentage points)**:

Giả sử tỷ lệ căn hộ bị hủy phòng giảm từ $5\%$ ở Quý 1 xuống còn $4\%$ ở Quý 2:
- **Chênh lệch tuyệt đối**:
  $$
  4\% - 5\% = -1\% \implies \text{Giảm 1 điểm phần trăm}
  $$
- **Thay đổi tương đối**:
  $$
  \frac{4\% - 5\%}{5\%} = \frac{-0.01}{0.05} = -0.20 = -20\% \implies \text{Giảm 20\% so với mức ban đầu}
  $$

Nếu người viết viết ẩu: *"Tỷ lệ hủy phòng giảm 1%"*, người đọc trong ngành kiểm toán sẽ hiểu là giảm $1\%$ của mức $5\%$ ban đầu, tức là còn $5\% \times (1 - 0.01) = 4.95\%$. Sai lệch này có thể làm méo mó các mô hình dự báo tài chính hàng tỷ đồng. Hãy luôn viết rõ cụm từ **điểm phần trăm** khi trừ hai giá trị tỷ lệ cho nhau.

---

## 3. Nghịch lý Simpson: Sự đảo chiều của trung bình gộp do biến động cơ cấu

Hiện tượng kỳ thú và nguy hiểm nhất trong phân tích dữ liệu tổng hợp là **Nghịch lý Simpson (Simpson's Paradox)**: Một quy luật hay xu hướng xuất hiện đồng nhất trong từng nhóm thành phần riêng rẽ có thể bị **đảo ngược hoàn toàn** khi dữ liệu được gộp chung lại.

### Mô hình toán học về sự dịch chuyển trọng số

Xét giá trung bình của một thị trường gồm hai phân khúc (phân khúc cao cấp và phân khúc giá rẻ) qua hai kỳ khảo sát:

$$
\text{Giá trung bình gộp: } \bar{X}_{\text{gộp}} = \frac{\sum (n_i \times \bar{X}_i)}{\sum n_i} = \sum w_i \bar{X}_i \quad \text{với} \quad w_i = \frac{n_i}{N}
$$

Hãy quan sát bảng số liệu thực nghiệm sau:

| Kỳ khảo sát | Phân khúc | Số chỗ ở ($n$) | Tỷ trọng cơ cấu ($w$) | Giá trung bình ($\bar{X}$) | Tổng giá trị ($n \times \bar{X}$) | Giá trung bình gộp ($\bar{X}_{\text{gộp}}$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **Kỳ 1 (Tháng 9)** | Cao cấp | 100 | $50.0\%$ | 60.0 nghìn | 6.000 | \multirow{2}{*}{\textbf{45.0 nghìn}} |
| | Giá rẻ | 100 | $50.0\%$ | 30.0 nghìn | 3.000 | |
| **Kỳ 2 (Tháng 6)** | Cao cấp | 80 | $26.7\%$ | **66.0 nghìn** ($+10\%$) | 5.280 | \multirow{2}{*}{\textbf{41.8 nghìn} (GIẢM!)} |
| | Giá rẻ | 220 | $73.3\%$ | **33.0 nghìn** ($+10\%$) | 7.260 | |

```
Từng phân khúc riêng lẻ:
- Phân khúc cao cấp: Tăng từ 60 lên 66 nghìn (+10%)
- Phân khúc giá rẻ:  Tăng từ 30 lên 33 nghìn (+10%)

Trung bình gộp toàn thị trường:
- Kỳ 1 (Tháng 9): (100*60 + 100*30) / 200 = 45.0 nghìn
- Kỳ 2 (Tháng 6): (80*66 + 220*33) / 300  = 41.8 nghìn  <--- GIẢM 7.1%!
```

### Bản chất của Nghịch lý
Tất cả các chủ nhà ở mọi phân khúc đều đồng loạt tăng giá $10\%$. Không có bất kỳ ai giảm giá. Thế nhưng giá trung bình gộp của toàn thành phố lại ghi nhận mức giảm từ $45.0$ xuống $41.8$ nghìn!

Nguyên nhân xuất phát hoàn toàn từ **sự thay đổi cơ cấu mẫu**:
- Ở Kỳ 1, tỷ lệ căn hộ giá rẻ chỉ chiếm $50\%$ nguồn cung.
- Ở Kỳ 2, tỷ lệ căn hộ giá rẻ đã tăng vọt lên chiếm $73.3\%$ nguồn cung.

Sự bùng nổ số lượng của phân khúc giá rẻ đã kéo trọng số $w_{\text{rẻ}}$ tăng vọt, đè bẹp mức tăng giá $10\%$ của từng nhóm và kéo tụt con số bình quân chung.

**Bài học sư phạm sống còn**: Khi so sánh hai mốc chụp (snapshot) hoặc hai giai đoạn lịch sử trong bài tập lớn hay dự án thực tế, nếu thấy một chỉ số tổng hợp biến thiên bất thường, điều đầu tiên phải làm là **kiểm tra cơ cấu tỷ trọng của các nhóm thành phần**. Nếu cơ cấu bị dịch chuyển, việc chỉ nhìn vào con số trung bình gộp sẽ dẫn tới những quyết định kinh doanh hoàn toàn sai lầm.

---

## 4. Quy trình thẩm định phân tích dữ liệu 4 bước (Data Audit Framework)

Khi đối diện với một báo cáo phân tích, đặc biệt là các báo cáo do mô hình trí tuệ nhân tạo (AI) tạo ra tự động, kỹ sư dữ liệu phải thực hiện quy trình kiểm toán 4 bước nghiêm ngặt:

```
[Bước 1: TRUY SỐ]       ---> Tính lại con số từ dữ liệu gốc, đối soát từng phép đếm.
        │
[Bước 2: PHƯƠNG PHÁP]   ---> Kiểm tra mẫu số, cơ cấu trọng số, biến gây nhiễu.
        │
[Bước 3: DIỄN GIẢI]     ---> Soát xét tính đúng mức của từ ngữ; phân biệt tương quan vs nhân quả.
        │
[Bước 4: PHÁN QUYẾT]    ---> Bác bỏ, sửa đổi, hoặc bổ sung phân tích phân tầng.
```

1. **Bước 1 · Truy số (Check the Numbers)**: Chạy lại mã nguồn từ bảng thô để xem con số được trích dẫn có thực sự tồn tại hay không. Nếu số liệu bịa đặt, bác bỏ ngay lập tức.
2. **Bước 2 · Kiểm tra phương pháp (Methodological Audit)**: Đánh giá xem đại lượng đo lường có đại diện đúng cho khái niệm cần chứng minh không. Chẳng hạn: số lượng đánh giá (`number_of_reviews_ltm`) chỉ là biến đại diện cho *lượng khách lưu trú*, hoàn toàn không phản ánh mức độ *khách yêu thích* (muốn đo mức độ yêu thích phải dùng điểm số đánh giá `review_scores_rating`).
3. **Bước 3 · Đánh giá diễn giải (Interpretive Scrutiny)**: Kiểm tra xem lời kết luận có vượt quá phạm vi bằng chứng không. Có đang dùng từ ngữ giật gân, võ đoán hay không.
4. **Bước 4 · Phán quyết & Viết lại đúng mức (Verdict & Revision)**: Đưa ra phán quyết chính thức (Giữ nguyên / Sửa cách diễn đạt / Bác bỏ hoàn toàn), sau đó soạn thảo lại câu kết luận theo cấu trúc Kim tự tháp Minto.

---

## 5. Hệ thống bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 14)

Hệ thống bài tập dưới đây rèn luyện kỹ năng thực hành kể chuyện dữ liệu, tính toán nghịch lý Simpson và triển khai quy trình thẩm định báo cáo độc lập.

### Thiết lập môi trường và Dữ liệu thử nghiệm

```python
import numpy as np
import pandas as pd

# Bảng dữ liệu mô phỏng nghịch lý Simpson
BANG_SIMPSON = pd.DataFrame({
    "ky": ["T9", "T9", "T6", "T6"],
    "phan_khuc": ["cao", "re", "cao", "re"],
    "n": [100, 100, 80, 220],
    "gia_tb": [60.0, 30.0, 66.0, 33.0], # Mỗi phân khúc đều tăng giá 10%
})

# Dữ liệu chỗ ở mẫu dùng cho bài toán thẩm định
DEMO_DS = pd.DataFrame({
    "id": range(301, 313),
    "calculated_host_listings_count": [1, 7, 2, 12, 5, 1, 3, 9, 1, 6, 2, 4],
    "number_of_reviews_ltm": [8, 20, 14, 31, 9, 0, 22, 16, 5, 12, 18, 10],
    "review_scores_rating": [4.9, 4.6, 4.95, 4.7, 4.5, None, 4.85, 4.6, 4.9, 4.55, 4.8, 4.75],
})
```

---

### Bài 1: Sắp xếp đoạn văn báo cáo theo Cấu trúc Kim tự tháp Minto

::: exercise Yêu cầu nghiệp vụ
Cho 4 câu văn rời rạc thuộc một mục báo cáo về giá thuê tại Santiago:
- **Câu A**: *"Con số dựa trên 17.688 chỗ ở có giá hợp lệ ở mốc chụp 29/06/2026; 846 chỗ ở không có giá đã được loại và ghi trong qa_report."*
- **Câu B**: *"Giá thuê điển hình ở Santiago là 59.000 CLP/đêm (khoảng 1,65 triệu đồng), thấp hơn mức trung bình 118.000 CLP."*
- **Câu C**: *"Trung vị ít bị ảnh hưởng bởi giá ngoại lai: 177 giá trị cực đoan đã gắn cờ làm trung bình cao hơn 44% nhưng gần như không làm thay đổi trung vị."*
- **Câu D**: *"Kết luận chỉ áp dụng cho giá niêm yết một đêm, chưa gồm phí vệ sinh/dịch vụ; giá thực tế khách trả có thể cao hơn."*

Hãy sắp xếp lại 4 câu này thành một danh sách biến `thu_tu` theo đúng cấu trúc Kim tự tháp Minto: (1) Kết luận chính $\to$ (2) Bằng chứng định lượng $\to$ (3) Phạm vi và giới hạn $\to$ (4) Chi tiết phương pháp.
:::

::: solution
#### Lời giải chuẩn xác

```python
# Sắp xếp theo Kim tự tháp: B (Kết luận) -> C (Bằng chứng) -> D (Giới hạn) -> A (Phương pháp)
thu_tu = ["B", "C", "D", "A"]
```

#### Phân tích sư phạm chuyên sâu
- **B (Đỉnh kim tự tháp)**: Đưa ra ngay thông điệp chủ đạo: con số giá thuê điển hình (trung vị) là 59.000 CLP.
- **C (Tầng bằng chứng)**: Giải thích vì sao chọn con số trung vị thay vì trung bình (bằng chứng về 177 giá trị cực đoan).
- **D (Tầng giới hạn)**: Nêu ranh giới của nhận định: giá chưa gồm phí phụ thu.
- **A (Tầng phương pháp)**: Cung cấp chi tiết cỡ mẫu 17.688 căn hộ phục vụ kiểm toán ở cuối mục hoặc trong phụ lục.
:::

---

### Bài 2: Đánh giá tính đúng mức của ngôn từ trong các cặp câu kết luận

::: exercise Yêu cầu nghiệp vụ
Với mỗi cặp số liệu và lời văn dưới đây, hãy gán nhãn `"vua"` (diễn đạt đúng mức) hoặc `"qua"` (diễn đạt quá mức, phóng đại) vào từ điển `nhan`:
1. `+53.7% YoY`: *"Thị trường tăng trưởng mạnh so với cùng kỳ"*
2. `+3.0% MoM`: *"Bứt phá thần tốc trong tháng 5"*
3. `Hệ số tương quan r = 0.081`: *"Nhiệt độ ngày ảnh hưởng rõ rệt tới lượng đánh giá"*
4. `Đúng 1 chỗ ở đòi ở tối thiểu 730 đêm`: *"Một vài ca cực đoan cần gắn cờ"*
5. `Nhóm es chiếm 65.4% (quy tắc từ khóa thô)`: *"Chắc chắn 2/3 khách nói tiếng Tây Ban Nha"*
:::

::: solution
#### Lời giải chuẩn xác

```python
nhan = {
    1: "vua", # +53.7% so cùng kỳ là tăng trưởng mạnh
    2: "qua", # +3.0% giữa hai tháng chỉ là tăng nhẹ, không thể gọi là bứt phá thần tốc
    3: "qua", # r = 0.081 là tương quan hầu như không có, không thể nói là ảnh hưởng rõ rệt
    4: "vua", # Gắn cờ ca cực đoan là hành vi thận trọng đúng mức
    5: "qua"  # Dùng từ "chắc chắn" khi quy tắc từ khóa chưa được kiểm định là võ đoán
}
```

#### Phân tích sư phạm chuyên sâu
Việc nhận diện các từ ngữ "quá mức" giúp sinh viên rèn luyện tác phong khoa học: từ chối các mỹ từ tiếp thị và trung thành với mức độ tin cậy mà dữ liệu thực tế cho phép.
:::

---

### Bài 3: Tính toán giá trung bình gộp (Có trọng số)

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `pooled_means(bang: pd.DataFrame, ky: str = "ky", n: str = "n", gia: str = "gia_tb") -> pd.Series` nhận vào bảng dữ liệu phân khúc qua các kỳ.

Hàm tính toán và trả về một Series:
- Chỉ mục là các kỳ (`ky`).
- Giá trị là **giá trung bình gộp có trọng số** của kỳ đó theo công thức:
  $$
  \bar{X}_{\text{gộp}} = \frac{\sum (n \times \text{gia})}{\sum n}
  $$
Tuyệt đối không lấy trung bình cộng giản đơn các dòng và không làm thay đổi bảng dữ liệu đầu vào.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def pooled_means_co_ban(bang: pd.DataFrame, ky: str = "ky", n: str = "n", gia: str = "gia_tb") -> pd.Series:
    # 1. Tính tổng giá trị của từng dòng
    tong_tien_dong = bang[n] * bang[gia]
    
    # 2. Gom nhóm tính tổng tiền và tổng số lượng theo kỳ
    tong_tien_ky = tong_tien_dong.groupby(bang[ky]).sum()
    tong_n_ky = bang[n].groupby(bang[ky]).sum()
    
    # 3. Chia lấy trung bình có trọng số
    gia_gop = tong_tien_ky / tong_n_ky
    return gia_gop
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Vector hóa một dòng)

```python
def pooled_means(bang: pd.DataFrame, ky: str = "ky", n: str = "n", gia: str = "gia_tb") -> pd.Series:
    return (bang[n] * bang[gia]).groupby(bang[ky]).sum() / bang.groupby(ky)[n].sum()
```

#### Phân tích so sánh & Trực giác bản chất
- Đoạn mã trên phản ánh đúng định nghĩa toán học của kỳ vọng phân phối có trọng số. Nếu người dùng gọi `bang.groupby(ky)[gia].mean()`, pandas sẽ tính trung bình cộng giản đơn ($(66 + 33)/2 = 49.5$), hoàn toàn bỏ qua việc phân khúc rẻ có tới 220 căn hộ trong khi phân khúc đắt chỉ có 80 căn hộ.
:::

---

### Bài 4: Tính toán tỷ trọng cơ cấu của một phân khúc

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `segment_share(bang: pd.DataFrame, phan_khuc: str, ky: str = "ky", nhom: str = "phan_khuc", n: str = "n") -> pd.Series` nhận vào bảng dữ liệu và tên của một phân khúc cụ thể (ví dụ `"re"`).

Hàm tính toán và trả về Series:
- Chỉ mục là các kỳ.
- Giá trị là **tỷ trọng số chỗ ở** của phân khúc đó trong từng kỳ (tổng $n$ của phân khúc chia cho tổng $n$ của kỳ đó, thang đo từ 0 đến 1). Kỳ nào không có phân khúc đó thì tỷ trọng bằng 0.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def segment_share(bang: pd.DataFrame, phan_khuc: str, ky: str = "ky", nhom: str = "phan_khuc", n: str = "n") -> pd.Series:
    # Tổng số lượng toàn kỳ
    tong_n_ky = bang.groupby(ky)[n].sum()
    
    # Lọc lấy số lượng của phân khúc cần tính
    bang_pk = bang.loc[bang[nhom] == phan_khuc]
    n_pk_ky = bang_pk.groupby(ky)[n].sum()
    
    # Khớp vào toàn bộ các kỳ (điền 0 nếu kỳ đó vắng bóng phân khúc)
    ty_trong = (n_pk_ky.reindex(tong_n_ky.index, fill_value=0) / tong_n_ky)
    return ty_trong
```

#### Phân tích sư phạm chuyên sâu
Khi chạy trên bảng `BANG_SIMPSON` với phân khúc `"re"`, kết quả cho thấy tỷ trọng căn hộ giá rẻ đã tăng từ $50.0\%$ (Kỳ T9) lên $73.3\%$ (Kỳ T6). Đây chính là bằng chứng định lượng bóc trần nguyên nhân vì sao giá trung bình gộp lại giảm dù từng nhóm đều tăng giá.
:::

---

### Bài 5: Thẩm định kết luận (Bước 1: Truy số từ dữ liệu thô)

::: exercise Yêu cầu nghiệp vụ
Một báo cáo do AI sinh ra đưa ra kết luận: *"Chủ nhà chuyên nghiệp được khách yêu thích hơn so với chủ nhà cá nhân, với 15,5 so với 12,7 đánh giá/năm."*
Để thẩm định bước 1 (Truy số), hãy viết hàm `reviews_by_host_type(ds: pd.DataFrame, nguong: int = 5) -> pd.Series` nhận vào bảng chỗ ở `ds` có cột `calculated_host_listings_count` và `number_of_reviews_ltm`.

Hàm thực hiện:
- Gom nhóm theo điều kiện boolean: `calculated_host_listings_count >= nguong` (tuyệt đối không thêm cột vào `ds`).
- Tính giá trị trung bình của cột `number_of_reviews_ltm` cho từng nhóm.
- Trả về Series có chỉ mục là các giá trị boolean `False` và `True`.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def reviews_by_host_type(ds: pd.DataFrame, nguong: int = 5) -> pd.Series:
    la_chuyen_nghiep = ds["calculated_host_listings_count"].ge(nguong)
    return ds.groupby(la_chuyen_nghiep)["number_of_reviews_ltm"].mean()
```

#### Phân tích so sánh & Trực giác bản chất
- Kết quả chạy trên snapshot thật tại Santiago cho ra đúng con số: nhóm chuyên nghiệp đạt 15.5 và nhóm cá nhân đạt 12.7 đánh giá/năm. Như vậy, bước 1 (Truy số) xác nhận rằng các con số toán học là có thật, không phải ảo giác bịa số.
:::

---

### Bài 6: Thẩm định kết luận (Bước 2 và Bước 3: Phán quyết chuyên gia)

::: exercise Yêu cầu nghiệp vụ
Dựa trên kết quả ở Bài 5, hãy chọn **một** phán quyết chuẩn xác nhất về mặt khoa học dữ liệu cho kết luận trên:
- **A.** "Giữ nguyên vì số đúng thì kết luận đúng."
- **B.** "Sửa cách diễn đạt: số đo là LƯỢNG ĐÁNH GIÁ (biến đại diện cho lượng đặt phòng), không đo 'yêu thích'; muốn nói yêu thích phải dùng điểm đánh giá, vì vậy viết lại thành 'có nhiều đánh giá hơn' và kiểm thêm theo từng nhóm."
- **C.** "Bác bỏ do số liệu sai."

Gán lựa chọn của bạn vào biến `phan_quyet` (chuỗi `"A"`, `"B"` hoặc `"C"`).
:::

::: solution
#### Phán quyết chuẩn xác

```python
phan_quyet = "B"
```

#### Phân tích sư phạm chuyên sâu: Lý do phán quyết và Bước 4
- **Tại sao không chọn A?**
  Số liệu 15.5 và 12.7 là đúng, nhưng con số này đo lường **số lượng đánh giá trong năm** (`number_of_reviews_ltm`). Lượng đánh giá cao chỉ chứng minh căn hộ đó có nhiều lượt khách ra vào (lượng đặt phòng cao), hoàn toàn không chứng minh khách hàng "yêu thích" căn hộ đó hơn. Một căn hộ giá rẻ ở bến xe có thể có 50 lượt khách/năm nhưng điểm đánh giá chỉ 3.5 sao, trong khi một biệt thự nghỉ dưỡng chỉ đón 5 đoàn khách/năm nhưng đạt tuyệt đối 5.0 sao. Đánh đồng số lượt đánh giá với sự "yêu thích" là lỗi ngụy biện đánh tráo khái niệm.
- **Tại sao không chọn C?**
  Số liệu không hề sai, ta không thể bác bỏ sạch trơn công sức tính toán.
- **Kết luận viết lại đúng mức (Bước 4)**:
  > *"Tại Santiago, các chỗ ở thuộc sở hữu của chủ nhà chuyên nghiệp ghi nhận lượng đánh giá bình quân cao hơn nhóm cá nhân (15.5 so với 12.7 lượt/năm), phản ánh tần suất đón khách cao hơn. Tuy nhiên, về mức độ hài lòng (điểm số đánh giá), hai nhóm không có sự khác biệt đáng kể (đều đạt trung vị 4.8 sao)."*
:::

---

### Bài tự làm mở rộng: Quy trình thẩm định báo cáo AI toàn diện

::: exercise Đề bài mở rộng
Hãy đóng vai một chuyên gia thẩm định dữ liệu độc lập, thiết lập danh mục kiểm toán 4 bước dưới dạng một danh sách kiểm tra (Audit Checklist) có thể thực thi tự động bằng Python để rà soát toàn bộ các câu kết luận trong một báo cáo phân tích kinh doanh.
:::

::: solution
#### Mã nguồn khung thẩm định tự động

```python
class KiemToanBaoCaoAI:
    def __init__(self, df_goc: pd.DataFrame):
        self.df = df_goc
        self.nhat_ky = []
        
    def kiem_toan_tuyen_bo(self, id_tuyen_bo: str, noi_dung: str, ham_truy_so, dieu_kien_phuong_phap, tu_khoa_cam: list):
        ho_so = {"id": id_tuyen_bo, "tuyen_bo": noi_dung, "trang_thai": "DAT", "ghi_chu": []}
        
        # 1. Bước 1: Truy số
        try:
            so_lieu = ham_truy_so(self.df)
            ho_so["so_thuc_te"] = so_lieu
        except Exception as e:
            ho_so["trang_thai"] = "BAC_BO"
            ho_so["ghi_chu"].append(f"Lỗi truy số: Không thể tái lập số liệu ({e})")
            self.nhat_ky.append(ho_so)
            return
            
        # 2. Bước 2: Kiểm tra phương pháp
        if not dieu_kien_phuong_phap(self.df):
            ho_so["trang_thai"] = "CAN_SUA"
            ho_so["ghi_chu"].append("Phương pháp có tì vết: Mất cân bằng cơ cấu hoặc chọn mốc thiên lệch")
            
        # 3. Bước 3: Rà soát ngôn từ phóng đại
        for tu in tu_khoa_cam:
            if tu.lower() in noi_dung.lower():
                ho_so["trang_thai"] = "CAN_SUA"
                ho_so["ghi_chu"].append(f"Ngôn từ quá mức: Chứa từ khóa phóng đại '{tu}'")
                
        self.nhat_ky.append(ho_so)
        
    def xuat_bao_cao(self):
        return pd.DataFrame(self.nhat_ky)

# Thử nghiệm thẩm định trên tuyên bố của Bài 5
kiem_toan = KiemToanBaoCaoAI(DEMO_DS)
kiem_toan.kiem_toan_tuyen_bo(
    id_tuyen_bo="TB_01",
    noi_dung="Chủ nhà chuyên nghiệp được khách yêu thích hơn hẳn, bùng nổ 15.5 đánh giá",
    ham_truy_so=lambda df: reviews_by_host_type(df).to_dict(),
    dieu_kien_phuong_phap=lambda df: "review_scores_rating" in df.columns, # Kiểm tra xem có dùng đúng cột đo sự yêu thích
    tu_khoa_cam=["hơn hẳn", "bùng nổ", "thần kỳ", "chắc chắn"]
)

print("KẾT QUẢ KIỂM TOÁN ĐỘC LẬP:")
print(kiem_toan.xuat_bao_cao().to_string(index=False))
```

#### Bình luận chuyên môn
Khung kiểm toán trên biến việc đọc báo cáo thành một quy trình kỹ nghệ có cấu trúc. Khi làm việc với các hệ thống AI sinh báo cáo tự động, một lớp kiểm toán độc lập bằng quy tắc là chốt chặn an toàn bắt buộc để bảo vệ doanh nghiệp trước các quyết định đầu tư sai lầm.
:::

---

## 6. Tổng kết và Đọc thêm

| Trụ cột kể chuyện | Khái niệm phương pháp luận | Bài học sư phạm & Đạo đức |
| :--- | :--- | :--- |
| **Kim tự tháp Minto** | Kết luận $\to$ Bằng chứng $\to$ Giới hạn $\to$ Phương pháp | Tôn trọng thời gian của người nghe; đưa thông điệp cốt lõi lên hàng đầu. |
| **Nghịch lý Simpson** | $\bar{X} = \sum w_i \bar{X}_i$; cơ cấu $w_i$ dịch chuyển | Không bao giờ tin vào con số trung bình gộp khi cơ cấu tỷ trọng giữa hai kỳ thay đổi. |
| **Ngôn ngữ đúng mức** | Phân biệt $\%$ và điểm phần trăm; tương quan vs nhân quả | Khiêm nhường trước số liệu; từ chối các tính từ giật gân, phóng đại. |
| **Quy trình thẩm định 4 bước** | Truy số $\to$ Phương pháp $\to$ Diễn giải $\to$ Phán quyết | Trách nhiệm học thuật thuộc về con người; luôn kiểm toán độc lập các báo cáo do AI tạo. |

### Tài liệu tham khảo học thuật

- Barbara Minto, *The Pyramid Principle: Logic in Writing and Thinking*, Financial Times / Prentice Hall.
- Edward H. Simpson, *The Interpretation of Interaction in Contingency Tables*, Journal of the Royal Statistical Society, 1951.
- Judea Pearl & Dana Mackenzie, *The Book of Why: The New Science of Cause and Effect*, Basic Books, 2018.
- Darrell Huff, *How to Lie with Statistics*, W. W. Norton & Company.
- Hệ thống bài giảng thực hành: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
