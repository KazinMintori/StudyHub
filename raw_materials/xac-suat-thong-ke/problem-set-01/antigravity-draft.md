---
course: xac-suat-thong-ke
section: problem-set
title: "Problem Set 01: Câu hỏi và dữ liệu"
---

# Problem Set 01: Câu hỏi và dữ liệu

Tài liệu này hệ thống hóa các bài tập nền tảng về tư duy dữ liệu và suy luận thống kê thực nghiệm. Trọng tâm của bài học là rèn luyện chuỗi liên kết logic chặt chẽ:

$$\text{Câu hỏi nghiên cứu} \longrightarrow \text{Đơn vị quan sát \& biến số} \longrightarrow \text{Quá trình tạo dữ liệu} \longrightarrow \text{Khung dữ liệu \& mức chi tiết} \longrightarrow \text{Phân tích} \longrightarrow \text{Khẳng định hợp lệ}$$

## Mục tiêu học tập

Sau khi hoàn thành bộ bài tập này, sinh viên có khả năng:

1. Thực hiện thuần thục các phép biến đổi số học bằng tay để nhận diện rõ vai trò của mẫu số, tỷ trọng phân bổ, tác động của phép gộp nhóm và bản chất của phép đo lặp lại.
2. Phân biệt rành mạch bốn loại khẳng định trong khoa học dữ liệu gồm tóm tắt mô tả, tổng quát hóa, dự đoán và khẳng định nhân quả, đồng thời nhận diện chuẩn xác giới hạn khi dữ liệu thực nghiệm chỉ hỗ trợ một mối liên hệ tương quan.
3. Truy vết ngược từ một khẳng định hoặc kết luận để chất vấn quá trình thu thập và phát sinh dữ liệu (data generating process).
4. Xác định chuẩn xác đơn vị quan sát, danh sách biến số, giá trị thực tế, thang đo thống kê và mức độ chi tiết (granularity) của từng hàng trong bảng dữ liệu.
5. Nhận thức rõ ràng việc số lượng hàng trong bảng dữ liệu không mặc nhiên đồng nhất với số đơn vị quan sát độc lập.
6. Đọc hiểu và phân tích cấu trúc cơ bản của một bảng dữ liệu (DataFrame), phân biệt bản chất giữa thang đo thống kê và kiểu dữ liệu phần mềm (software dtype).

### Yêu cầu thực hiện chung

- Trình bày câu trả lời bằng lập luận logic hoàn chỉnh, không chỉ ghi nhãn danh mục ngắn gọn.
- Khi nhận định dữ liệu chưa đủ cơ sở để hỗ trợ kết luận, cần chỉ rõ bước suy luận nào vượt quá bằng chứng thực nghiệm hoặc quá trình thu thập dữ liệu còn khiếm khuyết điểm gì.
- Khi tiếp cận bảng dữ liệu có nhiều hàng, luôn đặt ba câu hỏi then chốt: Mỗi hàng đại diện cho thực thể nào, đối tượng nào đang được đo lặp lại, và câu hỏi nghiên cứu hướng tới việc đếm loại đơn vị nào?
- Với các bài tập lập trình cơ bản, chỉ sử dụng các thao tác kiểm tra cấu trúc dữ liệu nền tảng gồm `head()`, `shape`, `columns` và `dtypes`.
- Phạm vi kiến thức tập trung hoàn toàn vào nền tảng tư duy dữ liệu, không đòi hỏi các công thức xác suất nâng cao hay lý thuyết suy diễn phức tạp.

---

## Phần A: Tính tay

### Bài 1: Từ số đếm đến tỷ lệ: Mẫu số làm thay đổi câu chuyện

Một trung tâm dữ liệu sử dụng hai loại máy chủ khác nhau để vận hành hệ thống. Bảng số liệu ghi nhận trong một tháng hoạt động như sau:

| Loại máy chủ | Số máy đang vận hành | Số máy gặp sự cố |
| :--- | :---: | :---: |
| Máy chủ A | $2.400$ | $48$ |
| Máy chủ B | $700$ | $21$ |

Yêu cầu thực hiện bằng tính toán thủ công và ghi rõ từng bước biến đổi:

1. Nếu chỉ nhìn vào số lượng máy gặp sự cố tuyệt đối, loại máy chủ nào có nhiều máy gặp sự cố hơn?
2. Hãy tính tỷ lệ máy gặp sự cố của từng loại máy chủ dưới ba dạng biểu diễn:
   - Dạng phân số tối giản.
   - Dạng tỷ lệ phần trăm.
   - Dạng số máy gặp sự cố tính trên $1.000$ máy đang vận hành.
3. Sau khi đưa về mẫu số thích hợp để so sánh công bằng, loại máy chủ nào có tỷ lệ máy gặp sự cố cao hơn?
4. Giải thích bằng một câu ngắn gọn vì sao việc so sánh $48$ với $21$ trả lời một câu hỏi hoàn toàn khác so với việc so sánh hai tỷ lệ vừa tính được.
5. Viết một câu tóm tắt khách quan được dữ liệu trên hỗ trợ trực tiếp.
6. Một kỹ sư hệ thống nhận định: "Dùng loại máy chủ B làm tăng nguy cơ sự cố." Nhận định này đã đi xa hơn kết quả tính toán ở trên như thế nào?

::: tip Gợi ý
Hãy chú ý phân biệt rõ giữa số lượng máy móc bị ảnh hưởng với tần suất rủi ro trên mỗi đơn vị máy. Quy mô tuyệt đối phản ánh khối lượng công việc bảo trì, trong khi tỷ lệ phản ánh mức độ tin cậy tương đối của từng dòng phần cứng.
:::

::: solution Lời giải
1. So sánh số đếm tuyệt đối:
   Nếu chỉ quan sát số lượng máy gặp sự cố mà không xét đến quy mô vận hành, loại máy chủ A có số máy gặp sự cố nhiều hơn ($48$ máy so với $21$ máy của loại B). Cần lưu ý rằng đây là số lượng cá thể máy bị hỏng hóc, không đồng nhất với tổng số sự kiện lỗi phát sinh trong suốt tháng.

2. Tính toán tỷ lệ máy gặp sự cố cho từng loại:
   - Đối với loại máy chủ A:
     $$\text{Tỷ lệ}_A = \frac{48}{2.400} = \frac{1}{50} = 2\%$$
     Quy đổi trên $1.000$ máy vận hành:
     $$2\% \times 1.000 = 20\text{ máy gặp sự cố trên } 1.000\text{ máy}$$
   - Đối với loại máy chủ B:
     $$\text{Tỷ lệ}_B = \frac{21}{700} = \frac{3}{100} = 3\%$$
     Quy đổi trên $1.000$ máy vận hành:
     $$3\% \times 1.000 = 30\text{ máy gặp sự cố trên } 1.000\text{ máy}$$

3. So sánh sau khi chuẩn hóa mẫu số:
   Khi so sánh trên cùng một quy mô cơ sở, loại máy chủ B có tỷ lệ gặp sự cố cao hơn ($3\%$ so với $2\%$, tương đương $30$ máy so với $20$ máy trên mỗi $1.000$ máy vận hành).

4. Phân biệt ý nghĩa câu hỏi:
   Việc so sánh $48$ với $21$ trả lời câu hỏi về tổng gánh nặng sửa chữa thực tế tại phòng máy, trong khi việc so sánh $3\%$ với $2\%$ trả lời câu hỏi về xác suất hoặc mức độ rủi ro tương đối của một máy chủ thuộc từng chủng loại.

5. Câu tóm tắt được dữ liệu hỗ trợ trực tiếp:
   Trong tháng khảo sát tại trung tâm dữ liệu, tỷ lệ máy chủ gặp sự cố ở dòng B là $3\%$, cao hơn tỷ lệ $2\%$ được ghi nhận ở dòng máy chủ A.

6. Đánh giá nhận định của kỹ sư:
   Khẳng định "dùng loại máy chủ B làm tăng nguy cơ sự cố" là một khẳng định nhân quả mang tính can thiệp. Dữ liệu hiện tại chỉ là số liệu quan sát mô tả trong một tháng duy nhất, chưa loại trừ các yếu tố gây nhiễu quan trọng như môi trường tải công việc, thời gian đã qua sử dụng, độ thông gió của khu vực đặt máy hoặc vị trí lắp đặt trên các tủ rack.
:::

---

### Bài 2: Tốt hơn trong từng nhóm, tệ hơn khi gộp

Hai hệ thống phần mềm A và B được triển khai thử nghiệm để giải quyết hai nhóm tác vụ có độ phức tạp khác nhau gồm tác vụ dễ và tác vụ khó. Kết quả ghi nhận như sau:

| Loại tác vụ | Hệ thống A | Hệ thống B |
| :--- | :---: | :---: |
| Tác vụ dễ | $9$ thành công trên $10$ tác vụ | $80$ thành công trên $100$ tác vụ |
| Tác vụ khó | $20$ thành công trên $100$ tác vụ | $1$ thành công trên $10$ tác vụ |

Yêu cầu thực hiện bằng tính toán thủ công:

1. Tính tỷ lệ thành công của hệ thống A và hệ thống B trong nhóm tác vụ dễ.
2. Tính tỷ lệ thành công của hệ thống A và hệ thống B trong nhóm tác vụ khó.
3. Trong từng nhóm tác vụ riêng biệt, hệ thống nào đạt tỷ lệ thành công cao hơn?
4. Tiến hành gộp chung toàn bộ tác vụ lại và tính:
   - Tổng số tác vụ và tổng số lần thành công của hệ thống A.
   - Tổng số tác vụ và tổng số lần thành công của hệ thống B.
   - Tỷ lệ thành công tổng thể của mỗi hệ thống.
5. Sau khi gộp toàn bộ, hệ thống nào có tỷ lệ thành công cao hơn? Kết luận này có cùng chiều với kết quả ở câu 3 hay không?
6. Điền các số liệu cụ thể vào hai nhận định sau:
   - "Trong từng loại tác vụ, hệ thống [...] tốt hơn hệ thống [...]."
   - "Khi gộp toàn bộ tác vụ, hệ thống [...] lại có tỷ lệ thành công cao hơn hệ thống [...]."
7. Dựa vào mẫu số và tỷ trọng phân bổ khối lượng công việc của hai loại tác vụ, hãy giải thích cơ chế dẫn đến hiện tượng đảo chiều này.
8. Nếu bảng dữ liệu ban đầu ghi nhận một hàng cho mỗi tổ hợp (hệ thống $\times$ loại tác vụ), còn bảng dữ liệu gộp chỉ ghi nhận một hàng cho mỗi hệ thống, thông tin nào đã bị mất đi?

::: tip Gợi ý
Hiện tượng đảo chiều này là nghịch lý Simpson (Simpson's paradox). Hãy xem xét tỷ lệ thành công tổng thể như một trung bình có trọng số, trong đó trọng số chính là tỷ lệ số tác vụ dễ hoặc khó mà mỗi hệ thống phải đảm nhận.
:::

::: solution Lời giải
1. Tỷ lệ thành công trong nhóm tác vụ dễ:
   - Hệ thống A:
     $$\text{Tỷ lệ}_{A, \text{dễ}} = \frac{9}{10} = 90\%$$
   - Hệ thống B:
     $$\text{Tỷ lệ}_{B, \text{dễ}} = \frac{80}{100} = 80\%$$

2. Tỷ lệ thành công trong nhóm tác vụ khó:
   - Hệ thống A:
     $$\text{Tỷ lệ}_{A, \text{khó}} = \frac{20}{100} = 20\%$$
   - Hệ thống B:
     $$\text{Tỷ lệ}_{B, \text{khó}} = \frac{1}{10} = 10\%$$

3. So sánh trong từng phân nhóm:
   Trong từng phân nhóm độc lập, hệ thống A đều vượt trội hơn hệ thống B ($90\% > 80\%$ ở tác vụ dễ và $20\% > 10\%$ ở tác vụ khó).

4. Tổng hợp số liệu khi gộp chung hai loại tác vụ:
   - Hệ thống A:
     $$\text{Tổng số tác vụ} = 10 + 100 = 110$$
     $$\text{Tổng số thành công} = 9 + 20 = 29$$
     $$\text{Tỷ lệ thành công chung}_A = \frac{29}{110} \approx 26{,}36\%$$
   - Hệ thống B:
     $$\text{Tổng số tác vụ} = 100 + 10 = 110$$
     $$\text{Tổng số thành công} = 80 + 1 = 81$$
     $$\text{Tỷ lệ thành công chung}_B = \frac{81}{110} \approx 73{,}64\%$$

5. So sánh sau khi gộp:
   Sau khi gộp chung, hệ thống B có tỷ lệ thành công cao hơn hẳn hệ thống A ($73{,}64\%$ so với $26{,}36\%$). Kết luận này hoàn toàn đảo chiều so với nhận định ở câu 3.

6. Điền câu nhận định hoàn chỉnh:
   - "Trong từng loại tác vụ, hệ thống A tốt hơn hệ thống B với tỷ lệ thành công tương ứng là $90\%$ so với $80\%$ ở tác vụ dễ, và $20\%$ so với $10\%$ ở tác vụ khó."
   - "Khi gộp toàn bộ tác vụ, hệ thống B lại có tỷ lệ thành công cao hơn hệ thống A với kết quả $73{,}64\%$ so với $26{,}36\%$."

7. Giải thích cơ chế đảo chiều theo mẫu số và trọng số:
   Tỷ lệ thành công chung thực chất là trung bình có trọng số của tỷ lệ thành công trên từng loại tác vụ:
   $$\text{Tỷ lệ chung} = \text{Tỷ lệ}_{\text{dễ}} \times \frac{N_{\text{dễ}}}{N_{\text{tổng}}} + \text{Tỷ lệ}_{\text{khó}} \times \frac{N_{\text{khó}}}{N_{\text{tổng}}}$$
   Hệ thống A phải gánh vác phần lớn là tác vụ khó với trọng số lên tới $\frac{100}{110}$ (chiếm khoảng $90{,}9\%$ khối lượng), loại tác vụ vốn có xác suất thành công tự nhiên rất thấp. Ngược lại, hệ thống B được phân công chủ yếu là tác vụ dễ với trọng số $\frac{100}{110}$, loại tác vụ có xác suất thành công cao. Sự chênh lệch nghiêm trọng về cơ cấu phân bổ tác vụ đã kéo tụt tỷ lệ bình quân của hệ thống A và nâng cao tỷ lệ của hệ thống B.

8. Mất mát thông tin khi gộp bảng:
   Bảng tổng hợp đã xóa bỏ hoàn toàn biến độ khó của tác vụ, làm mất đi bức tranh về năng lực thực tế của từng hệ thống trên các điều kiện vận hành cụ thể và che giấu sự bất cân xứng trong quá trình phân phối khối lượng công việc.
:::

---

### Bài 3: Một trung bình hay hai trung bình? Phép đo lặp và trọng số

Trong một thử nghiệm đo đạc pin lưu trữ năng lượng, ba bộ pin được theo dõi nhiệt độ hoạt động. Do sự cố gián đoạn ghi nhận dữ liệu tại hiện trường, số lượng phép đo thu thập được giữa các bộ pin không đồng đều:

| Bộ pin | Các giá trị nhiệt độ ghi nhận ($\,^{\circ}\mathrm{C}$) |
| :--- | :--- |
| Bộ pin P1 | $10$, $14$ |
| Bộ pin P2 | $20$, $20$, $20$, $20$ |
| Bộ pin P3 | $30$ |

Yêu cầu thực hiện bằng tính toán thủ công:

1. Thử nghiệm bao gồm bao nhiêu bộ pin? Nếu mỗi giá trị nhiệt độ được ghi lại thành một hàng trong bảng dữ liệu thì có tất cả bao nhiêu hàng quan sát?
2. Hãy tính nhiệt độ trung bình riêng của từng bộ pin P1, P2 và P3.
3. Tính giá trị trung bình của ba giá trị trung bình theo từng bộ pin:
   $$\bar{x}_{\text{pin}} = \frac{\bar{x}_{\text{P1}} + \bar{x}_{\text{P2}} + \bar{x}_{\text{P3}}}{3}$$
4. Bỏ qua ranh giới định danh giữa các bộ pin, hãy tính giá trị trung bình của toàn bộ $7$ phép đo nhiệt độ ban đầu.
5. Hai kết quả tính được ở câu 3 và câu 4 có bằng nhau hay không?
6. Trong phép tính ở câu 3, đơn vị nào được gán trọng số ngang nhau: Bộ pin hay phép đo? Trong phép tính ở câu 4 thì trọng số thuộc về đơn vị nào?
7. Giải thích vì sao việc có "$7$ hàng dữ liệu" không đồng nghĩa với việc chúng ta có "$7$ bộ pin độc lập".
8. Nếu câu hỏi nghiên cứu là "nhiệt độ điển hình của một bộ pin", phép tính nào phản ánh sát hơn mục tiêu nghiên cứu? Nếu câu hỏi là "nhiệt độ điển hình của một phép đo được ghi lại", câu trả lời thay đổi thế nào, và vì sao sự thiếu hụt dữ liệu khiến cả hai ước lượng này đều bị hạn chế?

::: tip Gợi ý
Khi các đơn vị quan sát có số lần đo lặp lại khác nhau, phép tính trung bình gộp toàn bộ sẽ vô tình trao quyền chi phối cho những đơn vị có nhiều phép đo nhất.
:::

::: solution Lời giải
1. Xác định số lượng thực thể và số hàng dữ liệu:
   Thử nghiệm có chính xác $3$ bộ pin thực tế. Nếu mỗi phép đo ghi nhận một hàng, bảng dữ liệu sẽ có tổng cộng $7$ hàng quan sát ($2$ hàng cho P1, $4$ hàng cho P2 và $1$ hàng cho P3).

2. Nhiệt độ trung bình của từng bộ pin:
   - Bộ pin P1:
     $$\bar{x}_{\text{P1}} = \frac{10 + 14}{2} = \frac{24}{2} = 12\,^{\circ}\mathrm{C}$$
   - Bộ pin P2:
     $$\bar{x}_{\text{P2}} = \frac{20 + 20 + 20 + 20}{4} = \frac{80}{4} = 20\,^{\circ}\mathrm{C}$$
   - Bộ pin P3:
     $$\bar{x}_{\text{P3}} = \frac{30}{1} = 30\,^{\circ}\mathrm{C}$$

3. Trung bình của các trung bình theo bộ pin:
   $$\bar{x}_{\text{pin}} = \frac{12 + 20 + 30}{3} = \frac{62}{3} \approx 20{,}67\,^{\circ}\mathrm{C}$$

4. Trung bình gộp của toàn bộ $7$ phép đo:
   $$\bar{x}_{\text{đo}} = \frac{10 + 14 + 20 + 20 + 20 + 20 + 30}{7} = \frac{134}{7} \approx 19{,}14\,^{\circ}\mathrm{C}$$

5. So sánh hai kết quả:
   Hai kết quả này hoàn toàn khác nhau ($20{,}67\,^{\circ}\mathrm{C} \neq 19{,}14\,^{\circ}\mathrm{C}$).

6. Phân tích trọng số gán cho các đơn vị:
   - Trong câu 3: Mỗi bộ pin được trao trọng số ngang nhau là $\frac{1}{3}$. Do đó, mỗi phép đo của P1 đóng góp $\frac{1}{6}$ vào kết quả chung, mỗi phép đo của P2 chỉ đóng góp $\frac{1}{12}$, trong khi phép đo duy nhất của P3 đóng góp tới $\frac{1}{3}$.
   - Trong câu 4: Mỗi phép đo riêng lẻ được trao trọng số ngang nhau là $\frac{1}{7}$. Vì vậy, bộ pin P2 chiếm tới $\frac{4}{7}$ tổng trọng số của kết quả, P1 chiếm $\frac{2}{7}$, còn P3 chỉ chiếm $\frac{1}{7}$.

7. Sự khác biệt giữa hàng dữ liệu và đơn vị độc lập:
   Bảy hàng dữ liệu xuất phát từ việc đo đạc lặp lại trên cùng $3$ đối tượng vật lý. Các quan sát thu được từ cùng một bộ pin có tính tương quan nội tại chặt chẽ, phụ thuộc vào đặc tính riêng của khối pin đó chứ không cung cấp thông tin độc lập mới như việc lấy mẫu thêm một bộ pin hoàn toàn mới.

8. Đánh giá câu hỏi nghiên cứu và hạn chế do mất dữ liệu:
   - Với mục tiêu tìm "nhiệt độ điển hình của một bộ pin": Phép tính trung bình của các trung bình ở câu 3 phù hợp hơn, vì đơn vị quan tâm là từng bộ pin và mỗi bộ pin cần có tiếng nói bình đẳng.
   - Với mục tiêu tìm "nhiệt độ điển hình của một phép đo được ghi lại": Phép tính gộp ở câu 4 phản ánh đúng trung bình của các lần đo cụ thể.
   - Hạn chế do mất dữ liệu: Sự cố mất dữ liệu tại hiện trường thường không mang tính ngẫu nhiên thuần túy (chẳng hạn P3 chỉ có $1$ phép đo có thể do pin bị quá nhiệt sớm dẫn đến thiết bị tự ngắt). Do số phép đo quá ít và không cân bằng, việc gán trọng số đều cho các pin (câu 3) có thể bị chi phối nặng bởi một phép đo duy nhất thiếu tin cậy của P3, trong khi việc gộp chung (câu 4) lại bị chi phối gần như hoàn toàn bởi hành vi riêng của bộ pin P2.
:::

---

### Bài 4: Từ dữ liệu từng sinh viên đến bảng liên hợp bằng tay

Một cuộc khảo sát thực hiện trên $10$ sinh viên nhằm tìm hiểu sở thích và kinh nghiệm lập trình. Dữ liệu gốc thu thập được lưu trữ như sau:

| `student_id` | `season` | `mts_beach` | `coding_exp` |
| :---: | :---: | :---: | :---: |
| 01 | Spring | Beach | No |
| 02 | Spring | Mountains | Yes |
| 03 | Summer | Beach | No |
| 04 | Summer | Beach | Yes |
| 05 | Summer | Mountains | No |
| 06 | Fall | Mountains | Yes |
| 07 | Fall | Mountains | No |
| 08 | Winter | Beach | Yes |
| 09 | Winter | Mountains | No |
| 10 | Winter | Beach | No |

Ý nghĩa các biến số trong bảng:
- `student_id`: Mã định danh sinh viên tham gia khảo sát.
- `season`: Mùa yêu thích trong năm gồm mùa xuân (`Spring`), mùa hè (`Summer`), mùa thu (`Fall`) và mùa đông (`Winter`).
- `mts_beach`: Địa điểm nghỉ dưỡng ưa thích gồm vùng núi (`Mountains`) hoặc bãi biển (`Beach`).
- `coding_exp`: Trải nghiệm lập trình đã có gồm có (`Yes`) hoặc chưa (`No`).

Yêu cầu thực hiện bằng tính toán thủ công:

1. Đơn vị quan sát của bảng dữ liệu gốc là gì? Bảng này có bao nhiêu quan sát (observations)?
2. Tự lập bằng tay bảng đếm liên hợp hai chiều giữa `season` và `mts_beach`, điền đầy đủ các ô cùng tổng hàng và tổng cột. Giữ cấu trúc khung đếm chuẩn sau để điền:

| Mùa (`season`) | Vùng núi (`Mountains`) | Bãi biển (`Beach`) | Tổng cộng (`Total`) |
| :--- | :---: | :---: | :---: |
| Mùa xuân (`Spring`) | | | |
| Mùa hè (`Summer`) | | | |
| Mùa thu (`Fall`) | | | |
| Mùa đông (`Winter`) | | | |
| Tổng cộng (`Total`) | | | $10$ |

3. Với mỗi mùa khảo sát, hãy tính tỷ lệ phần trăm sinh viên trong hàng đó lựa chọn bãi biển (`Beach`).
4. Nếu chỉ giữ lại bảng liên hợp hai chiều ở câu 2, ta còn có thể biết được sinh viên mang mã số 04 có kinh nghiệm lập trình (`coding_exp = Yes`) hay không?
5. Có thể khôi phục lại thứ tự ban đầu của $10$ sinh viên từ bảng đếm liên hợp hay không? Giải thích lý do.
6. So sánh mức độ chi tiết (granularity) giữa hai cấu trúc dữ liệu:
   - Bảng dữ liệu gốc: Một hàng biểu diễn thực thể nào?
   - Bảng tổng hợp liên hợp: Một ô biểu diễn thông tin gì?
7. Viết một câu giải thích tại sao việc gộp dữ liệu không chỉ làm bảng ngắn hơn mà còn làm thay đổi căn bản những loại câu hỏi nghiên cứu có thể trả lời.

::: tip Gợi ý
Khi chuyển đổi từ bảng dữ liệu vi mô sang bảng đếm vĩ mô, các thuộc tính cá thể không nằm trong danh sách phân nhóm sẽ bị triệt tiêu hoàn toàn.
:::

::: solution Lời giải
1. Đơn vị quan sát và số lượng hàng:
   Đơn vị quan sát của bảng gốc là một cá thể sinh viên cụ thể tham gia khảo sát. Bảng dữ liệu có đúng $10$ quan sát, tương ứng với $10$ sinh viên.

2. Bảng đếm liên hợp hai chiều `season` $\times$ `mts_beach`:

| Mùa (`season`) | Vùng núi (`Mountains`) | Bãi biển (`Beach`) | Tổng cộng (`Total`) |
| :--- | :---: | :---: | :---: |
| Mùa xuân (`Spring`) | $1$ | $1$ | $2$ |
| Mùa hè (`Summer`) | $1$ | $2$ | $3$ |
| Mùa thu (`Fall`) | $2$ | $0$ | $2$ |
| Mùa đông (`Winter`) | $1$ | $2$ | $3$ |
| Tổng cộng (`Total`) | $5$ | $5$ | $10$ |

3. Tỷ lệ lựa chọn bãi biển theo từng mùa:
   - Mùa xuân:
     $$\text{Tỷ lệ}_{\text{Spring}} = \frac{1}{2} = 50\%$$
   - Mùa hè:
     $$\text{Tỷ lệ}_{\text{Summer}} = \frac{2}{3} \approx 66{,}67\%$$
   - Mùa thu:
     $$\text{Tỷ lệ}_{\text{Fall}} = \frac{0}{2} = 0\%$$
   - Mùa đông:
     $$\text{Tỷ lệ}_{\text{Winter}} = \frac{2}{3} \approx 66{,}67\%$$

4. Truy vấn thuộc tính cá thể từ bảng gộp:
   Không thể biết được. Trong bảng liên hợp hai chiều, biến `coding_exp` và mã định danh `student_id` đã bị loại bỏ hoàn toàn khỏi không gian biểu diễn.

5. Khôi phục thứ tự ban đầu của sinh viên:
   Không thể khôi phục được. Phép tính đếm tần số đã gom gộp các cá thể sinh viên thành những số đếm vô danh, làm biến mất toàn bộ dấu vết về danh tính và thứ tự xuất hiện ban đầu của từng người.

6. So sánh mức độ chi tiết:
   - Bảng dữ liệu gốc: Một hàng biểu diễn đầy đủ các thuộc tính của một cá thể sinh viên duy nhất.
   - Bảng tổng hợp liên hợp: Một ô biểu diễn số lượng sinh viên đồng thời mang một tổ hợp giá trị xác định của hai biến phân loại.

7. Tác động của việc gộp dữ liệu:
   Việc gộp dữ liệu đánh đổi thông tin chi tiết ở cấp độ cá thể để lấy bức tranh tổng quan ở cấp độ nhóm, do đó tước bỏ khả năng phân tích các thuộc tính riêng lẻ của từng đối tượng hoặc kiểm tra mối liên hệ với các biến số không tham gia vào cấu trúc gộp.
:::

---

## Phần B: Đánh giá lập luận

### Bài 5: Người vừa bỏ thuốc có vẻ kém khỏe hơn

Một nghiên cứu quan sát tiến hành khảo sát và so sánh tình trạng sức khỏe giữa những người đang duy trì thói quen hút thuốc với những người gần đây đã bỏ thuốc. Sau khi phân nhóm và hiệu chỉnh theo độ tuổi cùng giới tính, các nhà nghiên cứu ghi nhận rằng nhóm người vừa bỏ thuốc có các chỉ số sức khỏe trung bình kém hơn so với nhóm người vẫn đang hút thuốc.

Một bài viết bình luận về kết quả này và đưa ra kết luận: "Bỏ thuốc làm sức khỏe xấu đi."

1. Kết quả được mô tả ở trên cho biết điều gì về mối liên hệ quan sát được giữa tình trạng hút thuốc và sức khỏe?
2. Khẳng định "bỏ thuốc làm sức khỏe xấu đi" thuộc loại khẳng định nào trong bốn loại cơ bản (tóm tắt mô tả, tổng quát hóa, dự đoán, khẳng định nhân quả)?
3. Vì sao bước chuyển từ mối liên hệ quan sát được ở câu 1 sang kết luận ở câu 2 không được bảo đảm chỉ bởi dữ liệu quan sát?
4. Hãy mô tả một quá trình tạo dữ liệu hợp lý trong đó tình trạng sức khỏe kém xuất hiện trước, rồi chính sự suy giảm sức khỏe đó thúc đẩy một số người quyết định bỏ thuốc.
5. Hãy viết lại kết luận thành một câu tóm tắt khiêm tốn hơn nhưng hoàn toàn phù hợp với dữ liệu đã thu thập.
6. Nếu muốn trả lời câu hỏi "điều gì sẽ xảy ra với sức khỏe nếu một người quyết định bỏ thuốc thay vì tiếp tục hút", vì sao việc chỉ đơn thuần thu thập thêm nhiều hàng dữ liệu vào cùng một thiết kế nghiên cứu quan sát vẫn không giải quyết được vấn đề?

::: tip Gợi ý
Đây là bài tập phân tích phương pháp luận nghiên cứu và tư duy dữ liệu, không nhằm mục đích đưa ra các khuyến nghị y khoa. Hãy tập trung vào hiện tượng đảo ngược chiều nhân quả (reverse causality) trong các nghiên cứu quan sát không can thiệp.
:::

::: solution Lời giải
1. Mối liên hệ quan sát được:
   Kết quả nghiên cứu chỉ ra một mối liên hệ tương quan nghịch trong tập mẫu quan sát: Nhóm những người vừa bỏ thuốc có mức độ sức khỏe trung bình kém hơn nhóm những người đang tiếp tục hút thuốc.

2. Phân loại khẳng định:
   Câu "bỏ thuốc làm sức khỏe xấu đi" là một khẳng định nhân quả (causal claim). Khẳng định này gán việc từ bỏ thuốc lá làm nguyên nhân trực tiếp dẫn tới hệ quả là sức khỏe bị suy giảm.

3. Giới hạn của dữ liệu quan sát:
   Dữ liệu thu được là dữ liệu quan sát thụ động, không có sự can thiệp phân bổ ngẫu nhiên hành vi hút hay bỏ thuốc. Mối liên hệ thống kê quan sát được không thể loại trừ khả năng tồn tại các biến gây nhiễu tiềm ẩn hoặc chiều nhân quả diễn ra ngược lại với giả định ban đầu.

4. Cơ chế tạo dữ liệu với chiều nhân quả ngược:
   Trong thực tế, nhiều người hút thuốc lâu năm chỉ quyết định từ bỏ thuốc lá khi cơ thể bắt đầu xuất hiện các triệu chứng bệnh tật rõ rệt hoặc sau khi nhận chẩn đoán xấu từ bác sĩ. Do đó, tình trạng sức khỏe kém đã phát sinh từ trước và đóng vai trò là động lực thúc đẩy họ bỏ thuốc, chứ không phải hành động bỏ thuốc làm cho họ bị suy giảm sức khỏe.

5. Viết lại kết luận phù hợp:
   "Trong nhóm đối tượng được khảo sát, những người vừa từ bỏ thuốc lá có các chỉ số sức khỏe trung bình kém hơn so với những người vẫn đang tiếp tục hút thuốc."

6. Lý do số lượng hàng lớn không giải quyết được vấn đề:
   Việc tăng kích thước mẫu (thêm nhiều hàng dữ liệu) chỉ giúp làm giảm sai số ngẫu nhiên do chọn mẫu, nhưng không thể xóa bỏ sai lệch hệ thống bắt nguồn từ thiết kế nghiên cứu. Chừng nào việc bỏ thuốc vẫn là quyết định tự phát của đối tượng dựa trên tình trạng thể chất sẵn có, sự thiên lệch do nhân quả ngược vẫn sẽ tồn tại trong dữ liệu.
:::

---

### Bài 6: "Cha mẹ nên bớt kiểm soát"?

Một công trình nghiên cứu theo dõi sự phát triển ở trẻ nhỏ ghi nhận rằng những đứa trẻ có lượng mỡ cơ thể cao hơn thường có xu hướng có mẹ được đánh giá là có hành vi kiểm soát con cái chặt chẽ hơn trong sinh hoạt hằng ngày. Từ kết quả này, một bài báo đã đưa ra lời khuyên rằng các bậc cha mẹ có con thừa cân nên giảm bớt sự kiểm soát đối với con mình.

1. Phát hiện thực tế của nghiên cứu mô tả điều gì về mối quan hệ giữa hai biến số đang được quan sát?
2. Lời khuyên của bài báo ngầm chứa một khẳng định nhân quả nào?
3. Hãy chỉ ra chính xác bước chuyển lập luận từ mối liên hệ quan sát được sang khẳng định nhân quả mang tính can thiệp.
4. Hãy đưa ra hai cơ chế tạo dữ liệu độc lập khác nhau cũng có thể tạo ra cùng mối liên hệ quan sát được nói trên mà không cần giả định rằng "kiểm soát nhiều dẫn đến tăng mỡ cơ thể".
5. Hãy viết một tiêu đề hoặc câu kết luận thay thế hoàn toàn chuẩn xác với dữ liệu mà không đi xa hơn phạm vi quan sát.
6. Nếu nghiên cứu chỉ bao gồm các gia đình tự nguyện đăng ký tham gia tại một cơ sở y tế duy nhất, nhận định "mọi trẻ em đều có xu hướng như vậy" đã phạm phải bước suy luận vượt cấp nào ngoài vấn đề nhân quả?

::: tip Gợi ý
Đây là bài tập thuần túy về phân tích thống kê và suy luận thực nghiệm, không đưa ra lời khuyên chăm sóc trẻ. Hãy xem xét cả khả năng nhân quả ngược lẫn sự hiện diện của các yếu tố kinh tế, xã hội đóng vai trò biến gây nhiễu.
:::

::: solution Lời giải
1. Mô tả mối liên hệ quan sát được:
   Nghiên cứu ghi nhận một mối tương quan thuận giữa hai biến số quan sát: Trong nhóm trẻ em được khảo sát, mức độ kiểm soát của người mẹ có xu hướng tăng đồng hành với tỷ lệ mỡ cơ thể của đứa trẻ.

2. Khẳng định nhân quả ngầm định:
   Lời khuyên của bài báo ngầm định rằng hành vi kiểm soát của cha mẹ là nguyên nhân trực tiếp làm tăng lượng mỡ cơ thể của trẻ, do đó việc can thiệp bằng cách giảm kiểm soát sẽ tạo ra tác động làm giảm lượng mỡ cơ thể.

3. Điểm đứt gãy trong bước chuyển lập luận:
   Tác giả bài báo đã đồng nhất hóa mối tương quan đồng biến quan sát được với một mối quan hệ nhân quả có thể can thiệp. Việc hai biến số biến thiên cùng chiều không đồng nghĩa với việc tác động vào biến này sẽ làm biến đổi biến kia.

4. Hai cơ chế tạo dữ liệu thay thế:
   - Cơ chế nhân quả ngược: Trẻ em có cơ địa dễ tăng cân hoặc đã bắt đầu thừa cân từ trước khiến cha mẹ lo lắng cho sức khỏe của con, từ đó họ chủ động thiết lập chế độ giám sát và can thiệp chặt chẽ hơn vào khẩu phần ăn uống.
   - Cơ chế biến gây nhiễu chung: Áp lực kinh tế hoặc điều kiện sinh sống tại các khu dân cư thiếu không gian vận động an toàn vừa khiến trẻ em ít có cơ hội tập luyện ngoài trời (dẫn tới tích tụ mỡ), vừa khiến cha mẹ luôn trong trạng thái lo âu và có xu hướng kiểm soát hành vi của con khắt khe hơn.

5. Tiêu đề hoặc câu kết luận thay thế phù hợp:
   "Khảo sát mối liên hệ giữa mức độ kiểm soát của cha mẹ và chỉ số mỡ cơ thể ở trẻ em."

6. Lỗi suy luận tổng quát hóa vượt cấp:
   Nhận định trên đã phạm lỗi tổng quát hóa quá mức (over-generalization). Nhóm các gia đình chủ động tình nguyện đăng ký tham gia nghiên cứu tại một cơ sở y tế cụ thể có thể mang những đặc trưng riêng biệt về nhận thức hoặc mối quan tâm sức khỏe, không đại diện công bằng cho toàn thể quần thể trẻ em nói chung.
:::

---

### Bài 7: Boot camp và tái phạm

Một chương trình phục hồi nhân phẩm trong trại giam cho phép các phạm nhân đủ điều kiện được quyền tự nguyện đăng ký tham gia một khóa huấn luyện kỷ luật tập trung ("boot camp"). Theo dõi sau khi mãn hạn tù, ban quản lý ghi nhận rằng những người đã hoàn thành trọn vẹn khóa boot camp có tỷ lệ tái phạm và quay trở lại nhà tù thấp hơn đáng kể so với nhóm tù nhân còn lại.

Một người phát ngôn tuyên bố: "Chương trình boot camp đã giúp làm giảm tỷ lệ tái phạm."

1. Hãy viết một câu tóm tắt khách quan mà dữ liệu thực nghiệm trên trực tiếp hỗ trợ.
2. Phát biểu "chương trình boot camp đã giúp làm giảm tỷ lệ tái phạm" thuộc loại khẳng định nào?
3. Hãy mô tả bằng lời chuỗi phân nhánh hình thành nên các nhóm đối tượng được so sánh: Ai có cơ hội tham gia, ai tự nguyện đăng ký, ai hoàn thành khóa học, và ai nằm trong nhóm tù nhân còn lại.
4. Hai nhóm đối tượng được so sánh có thể đã mang những điểm khác biệt căn bản nào ngay từ trước khi chương trình bắt đầu? Hãy nêu ít nhất hai khả năng cụ thể.
5. Giải thích lý do vì sao yếu tố "tự nguyện tham gia" và điều kiện "hoàn thành" là những rào cản đặc biệt nghiêm trọng khi đánh giá kết luận nhân quả.
6. Giả sử ban quản lý thu thập thêm dữ liệu trên $100.000$ phạm nhân bằng đúng quy trình tự nguyện nói trên. Số lượng hàng dữ liệu rất lớn đó có tự động biến kết luận thành mối liên hệ nhân quả hay không? Giải thích rõ lý do.
7. Hãy viết một kết luận thận trọng và chuẩn mực hơn mà người phát ngôn viên có thể sử dụng trước công chúng.

::: tip Gợi ý
Hãy chú ý đến hai nguồn sai lệch kinh điển trong thống kê xã hội: Sai lệch tự lựa chọn (self-selection bias) và sai lệch sống sót hoặc bỏ cuộc giữa chừng (survivorship / attrition bias).
:::

::: solution Lời giải
1. Câu tóm tắt được dữ liệu hỗ trợ trực tiếp:
   Trong nhóm tù nhân được theo dõi sau khi mãn hạn tù, những cá nhân chủ động đăng ký và hoàn thành khóa huấn luyện boot camp có tỷ lệ tái phạm thấp hơn so với nhóm những người không tham gia hoặc không hoàn thành khóa học.

2. Phân loại khẳng định:
   Tuyên bố của người phát ngôn là một khẳng định nhân quả (causal claim), gán hiệu quả của chương trình huấn luyện là nguyên nhân trực tiếp làm giảm hành vi tái phạm.

3. Chuỗi phân nhánh tạo dữ liệu thực nghiệm:
   - Toàn bộ quần thể phạm nhân được sàng lọc sơ bộ để xác định những người đủ điều kiện tham gia.
   - Nhóm đủ điều kiện đưa ra quyết định cá nhân: Một số người chủ động tình nguyện đăng ký, số còn lại từ chối tham gia.
   - Trong số những người đăng ký: Một số người kiên trì vượt qua khó khăn để hoàn thành khóa học, trong khi một số khác bỏ cuộc hoặc bị kỷ luật giữa chừng.
   - Nhóm đối chứng so sánh ("nhóm còn lại") bị gộp chung gồm: Những người không đủ điều kiện, những người từ chối tham gia, và cả những người đã bỏ cuộc giữa chừng.

4. Hai khác biệt căn bản sẵn có trước khi tham gia chương trình:
   - Động lực phục thiện và ý chí cá nhân: Những người chủ động xin tham gia một khóa kỷ luật nghiêm ngặt vốn đã có ý thức muốn làm lại cuộc đời cao hơn hẳn ngay từ đầu.
   - Mức độ vi phạm và tiền án tiền sự: Những người được xét duyệt và dám thử sức với chương trình thường có mức độ nguy hiểm xã hội thấp hơn hoặc có nhân thân ít phức tạp hơn so với mặt bằng chung.

5. Rào cản từ tính tự nguyện và tiêu chuẩn hoàn thành:
   - Tính tự nguyện tạo ra sai lệch tự lựa chọn (self-selection bias): Hai nhóm được so sánh không tương đương nhau về các đặc tính nền tảng ngay từ thời điểm xuất phát.
   - Tiêu chuẩn hoàn thành tạo ra sai lệch sống sót (survivorship bias): Việc chỉ đo lường những người hoàn thành khóa học đã loại bỏ những đối tượng nản chí hoặc dễ tái phạm ra khỏi nhóm can thiệp, dồn các cá thể có nguy cơ cao này sang nhóm còn lại, từ đó thổi phồng thành tích của chương trình.

6. Tác động của quy mô mẫu lớn ($100.000$ quan sát):
   Số lượng hàng lớn không thể biến một kết luận tương quan thành khẳng định nhân quả. Dữ liệu dù lớn đến đâu vẫn được sinh ra từ một quy trình có sai lệch hệ thống (systematic bias). Việc tăng kích thước mẫu chỉ làm cho ước lượng trở nên chính xác hơn về một giá trị đã bị chệch, chứ không sửa chữa được khiếm khuyết trong thiết kế nghiên cứu.

7. Kết luận thận trọng của người phát ngôn:
   "Số liệu theo dõi cho thấy nhóm phạm nhân tự nguyện đăng ký và hoàn tất khóa huấn luyện boot camp có tỷ lệ tái phạm sau mãn hạn thấp hơn so với các nhóm phạm nhân khác. Tuy nhiên, chúng tôi cần triển khai thêm các đánh giá chuyên sâu để xác định rõ mức độ đóng góp thực tế của chương trình bên cạnh các yếu tố về động lực cá nhân của người tham gia."
:::

---

## Phần C: Cấu trúc dữ liệu

### Bài 8: Cùng được lưu bằng số, nhưng không cùng loại biến

Một hệ thống quản trị dữ liệu học tập lưu trữ bốn cột thông tin sau:

| Tên cột (`column`) | Một vài giá trị minh họa | Ý nghĩa thực tế |
| :--- | :--- | :--- |
| `student_id` | $24001234$, $24001235$, $24001236$ | Mã số sinh viên |
| `satisfaction` | $1$, $2$, $3$, $4$, $5$ | Mức độ hài lòng từ "rất không hài lòng" đến "rất hài lòng" |
| `num_siblings` | $0$, $1$, $2$, $3$, $\dots$ | Số anh chị em ruột |
| `temperature_c` | $21{,}4$; $21{,}9$; $22{,}1$; $\dots$ | Nhiệt độ phòng học đo bằng $\,^{\circ}\mathrm{C}$ |

Phần mềm máy tính có thể lưu trữ ba cột đầu tiên bằng kiểu số nguyên (`int64`) và cột cuối cùng bằng kiểu số thực (`float64`).

1. Hãy phân loại thang đo thống kê của từng cột theo chuẩn mực khoa học dữ liệu gồm biến định tính định danh, định tính thứ bậc, định lượng rời rạc và định lượng liên tục.
2. Với những cột nào thì phép toán lấy hiệu số giữa hai giá trị mang ý nghĩa định lượng tự nhiên trong thực tế? Với những cột nào các con số chủ yếu đóng vai trò là nhãn định danh hoặc mã hóa mức độ?
3. Có nên tính giá trị trung bình cộng cho cột `student_id` hay không? Hãy giải thích lý do về mặt bản chất mà không viện dẫn các quy định kỹ thuật của phần mềm.
4. Nếu chuyển đổi toàn bộ giá trị trong cột `satisfaction` thành các nhãn chữ tương ứng gồm `"very dissatisfied"`, `"dissatisfied"`, `"neutral"`, `"satisfied"`, `"very satisfied"`, thang đo thống kê của biến này có bị thay đổi hay không?
5. Nếu cột `student_id` được phần mềm hiển thị kiểu dữ liệu `dtype = int64`, điều đó cho chúng ta biết thông tin gì và hoàn toàn không cho biết thông tin gì về mặt ý nghĩa thống kê?
6. Hãy viết một quy tắc ngắn gọn trong một câu giúp phân biệt rạch ròi giữa thang đo thống kê (statistical variable type) và kiểu dữ liệu phần mềm (software dtype).

::: tip Gợi ý
Đừng để các con số đánh lừa trực giác. Một biến số có thể mang hình thức biểu diễn là những chữ số nguyên nhưng bên trong lại chỉ đóng vai trò phân loại danh mục hoặc đánh dấu thứ tự ưu tiên.
:::

::: solution Lời giải
1. Phân loại thang đo thống kê cho từng biến:
   - `student_id`: Biến định tính định danh (nominal categorical), đóng vai trò mã định danh duy nhất (identifier) cho từng cá thể.
   - `satisfaction`: Biến định tính thứ bậc (ordinal categorical), các mức độ có quan hệ thứ tự rõ ràng nhưng khoảng cách giữa các mức không có đơn vị đo lường vật lý cụ thể.
   - `num_siblings`: Biến định lượng rời rạc (discrete quantitative), nhận các giá trị đếm nguyên và các phép toán chênh lệch mang ý nghĩa cụ thể.
   - `temperature_c`: Biến định lượng liên tục (continuous quantitative), có thể nhận các giá trị thập phân trên thang đo khoảng nhiệt độ.

2. Ý nghĩa của phép trừ và vai trò của các con số:
   - Phép toán hiệu số có ý nghĩa định lượng tự nhiên đối với hai cột `num_siblings` (cho biết một sinh viên có nhiều hơn sinh viên khác bao nhiêu người em) và `temperature_c` (cho biết nhiệt độ chênh lệch bao nhiêu độ).
   - Đối với `student_id`, các con số chỉ đóng vai trò là nhãn định danh phân biệt giữa các cá thể. Đối với `satisfaction`, các con số $1$ đến $5$ chỉ là phép mã hóa thứ bậc quy ước để biểu thị mức độ hài lòng tăng dần.

3. Vấn đề tính trung bình cho `student_id`:
   Hoàn toàn không nên tính trung bình cộng cho `student_id`. Mã số sinh viên thực chất là một chuỗi ký tự định danh được sắp đặt theo quy ước quản lý hành chính. Giá trị trung bình của các mã định danh không đại diện cho bất kỳ xu hướng trung tâm hay thuộc tính thực tế nào của tập thể sinh viên.

4. Thay đổi biểu diễn trong cột `satisfaction`:
   Thang đo thống kê không thay đổi. Biến số này vẫn giữ nguyên bản chất là một biến định tính thứ bậc (ordinal categorical) vì trật tự logic tự nhiên giữa các mức độ vẫn được bảo toàn nguyên vẹn.

5. Ý nghĩa của thông tin `dtype = int64`:
   Thông tin `dtype = int64` chỉ cho biết máy tính phân bổ bộ nhớ $64$ bit để lưu trữ dữ liệu dưới dạng số nguyên và cho phép thực thi các phép toán số học cấp thấp của bộ xử lý. Nó hoàn toàn không cho biết ý nghĩa thống kê của cột, không xác nhận liệu đây là mã định danh, thứ bậc xếp hạng hay số đếm thực nghiệm.

6. Quy tắc phân biệt cốt lõi:
   Thang đo thống kê phản ánh ý nghĩa thực tế và các phép toán hợp lệ trên biến số trong thế giới thực, trong khi kiểu dữ liệu phần mềm chỉ quy định cách thức bộ nhớ máy tính lưu trữ và quản lý các bit dữ liệu.
:::

---

### Bài 9: Palmer Penguins: Đọc cấu trúc trước khi phân tích

Bộ dữ liệu nghiên cứu về chim cánh cụt tại quần đảo Palmer là một ví dụ mẫu mực để tiếp cận cấu trúc bảng dữ liệu, phân loại biến số và nhận diện đơn vị quan sát.

#### Khởi tạo môi trường và đọc dữ liệu bằng Python

Đối với người học chưa có kinh nghiệm lập trình pandas, các khái niệm cơ bản được tiếp cận như sau:
- Cài đặt thư viện: Mở cửa sổ dòng lệnh và cài đặt qua công cụ pip bằng lệnh `pip install pandas`.
- Nạp thư viện: Sử dụng câu lệnh `import pandas as pd` để nạp toàn bộ công cụ xử lý bảng và quy ước đặt tên ngắn gọn là `pd`.
- Tệp định dạng CSV (Comma-Separated Values): Định dạng tệp văn bản thuần túy lưu trữ dữ liệu dạng bảng, trong đó mỗi dòng là một hàng và các cột được phân tách bằng dấu phẩy.
- Cấu trúc `DataFrame`: Cấu trúc dữ liệu dạng bảng hai chiều trung tâm của pandas, chứa các hàng và các cột có nhãn định danh.
- Hàm đọc dữ liệu `pd.read_csv()`: Đọc nội dung tệp CSV từ đường dẫn máy cục bộ hoặc từ liên kết mạng và chuyển đổi thành DataFrame.
- Phép gán biến: Biểu thức `penguins = pd.read_csv(...)` có chức năng lưu trữ bảng dữ liệu vừa đọc vào một biến có tên gọi là `penguins`.
- Phân biệt phương thức (method) và thuộc tính (property): Phương thức `.head()` đòi hỏi cặp ngoặc tròn vì nó thực hiện một hành động tính toán hoặc trích xuất, trong khi các thuộc tính `.shape`, `.columns`, `.dtypes` chỉ đơn thuần truy xuất metadata đặc tính sẵn có của bảng nên không dùng ngoặc tròn.
- Hàm `print()`: Hiển thị trực tiếp kết quả ra màn hình làm việc.
- Ký hiệu `NaN` (Not a Number): Đại diện cho các ô dữ liệu bị khuyết thiếu (missing data) trong quá trình nghiên cứu thực địa.
- Các kiểu dữ liệu phần mềm cơ bản: `float64` là số thực dấu phẩy động $64$ bit, `int64` là số nguyên $64$ bit, `str` hoặc `object` là chuỗi văn bản hoặc kiểu tham chiếu chung trong pandas.

Mã nguồn thực thi và tài nguyên lưu trữ:
- Đoạn mã Python: [`/materials/xac-suat-thong-ke/problem-set-01/penguins.py`](file:///materials/xac-suat-thong-ke/problem-set-01/penguins.py)
- Tệp dữ liệu CSV gốc: [`/materials/xac-suat-thong-ke/problem-set-01/penguins.csv`](file:///materials/xac-suat-thong-ke/problem-set-01/penguins.csv)
- Nhật ký kết quả văn bản: [`/materials/xac-suat-thong-ke/problem-set-01/output.txt`](file:///materials/xac-suat-thong-ke/problem-set-01/output.txt)
- Hình ảnh giao diện đầu ra: `img/problem-set-01/penguins-head.png`

```python
import pandas as pd

url = "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/main/inst/extdata/penguins.csv"
penguins = pd.read_csv(url)

print(penguins.head())
print(penguins.shape)
print(penguins.columns)
print(penguins.dtypes)
```

#### Kết quả thực thi thực tế từ thư viện pandas

Dưới đây là bốn kết quả in ra màn hình được ghi nhận từ môi trường thực thi:

1. Đầu ra của lệnh trích xuất các hàng đầu tiên `print(penguins.head())`:
```text
  species     island  bill_length_mm  ...  body_mass_g     sex  year
0  Adelie  Torgersen            39.1  ...       3750.0    male  2007
1  Adelie  Torgersen            39.5  ...       3800.0  female  2007
2  Adelie  Torgersen            40.3  ...       3250.0  female  2007
3  Adelie  Torgersen             NaN  ...          NaN     NaN  2007
4  Adelie  Torgersen            36.7  ...       3450.0  female  2007

[5 rows x 8 columns]
```

Để thuận tiện quan sát trên mọi kích cỡ màn hình di động, $5$ quan sát đầu tiên của bảng được chia nhỏ thành hai bảng chi tiết hoàn chỉnh:

*Phần 1: Thông tin định danh và kích thước mỏ chim cánh cụt:*

| Chỉ số dòng | Loài chim (`species`) | Hòn đảo (`island`) | Chiều dài mỏ (`bill_length_mm`) | Độ sâu mỏ (`bill_depth_mm`) |
| :---: | :--- | :--- | :---: | :---: |
| 0 | Adelie | Torgersen | $39{,}1$ | $18{,}7$ |
| 1 | Adelie | Torgersen | $39{,}5$ | $17{,}4$ |
| 2 | Adelie | Torgersen | $40{,}3$ | $18{,}0$ |
| 3 | Adelie | Torgersen | $\text{NaN}$ | $\text{NaN}$ |
| 4 | Adelie | Torgersen | $36{,}7$ | $19{,}3$ |

*Phần 2: Kích thước cánh, khối lượng, giới tính và năm khảo sát:*

| Chỉ số dòng | Chiều dài vây cánh (`flipper_length_mm`) | Khối lượng cơ thể (`body_mass_g`) | Giới tính (`sex`) | Năm khảo sát (`year`) |
| :---: | :---: | :---: | :---: | :---: |
| 0 | $181{,}0$ | $3.750{,}0$ | male | $2007$ |
| 1 | $186{,}0$ | $3.800{,}0$ | female | $2007$ |
| 2 | $195{,}0$ | $3.250{,}0$ | female | $2007$ |
| 3 | $\text{NaN}$ | $\text{NaN}$ | $\text{NaN}$ | $2007$ |
| 4 | $193{,}0$ | $3.450{,}0$ | female | $2007$ |

2. Đầu ra của thuộc tính kích thước `print(penguins.shape)`:
```text
(344, 8)
```

3. Đầu ra của thuộc tính danh sách cột `print(penguins.columns)`:
```text
Index(['species', 'island', 'bill_length_mm', 'bill_depth_mm',
       'flipper_length_mm', 'body_mass_g', 'sex', 'year'],
      dtype='str')
```

4. Đầu ra của thuộc tính kiểu dữ liệu phần mềm `print(penguins.dtypes)`:
```text
species                  str
island                   str
bill_length_mm       float64
bill_depth_mm        float64
flipper_length_mm    float64
body_mass_g          float64
sex                      str
year                   int64
dtype: object
```
*Lưu ý quan trọng*: Dòng chữ `dtype: object` ở cuối cùng là kiểu dữ liệu nội bộ của bản thân đối tượng Series chứa kết quả kiểm tra `dtypes`, hoàn toàn không phải là kiểu dữ liệu của các cột gốc trong DataFrame.

#### Câu hỏi phân tích

1. Thuộc tính `penguins.shape` cho biết số lượng hàng và số lượng cột. Vì sao chỉ từ hai con số $(344, 8)$ này, chúng ta vẫn chưa thể khẳng định mỗi hàng đại diện cho thực thể cụ thể nào?
2. Dựa vào ngữ cảnh nghiên cứu và danh mục các cột, hãy xác định đơn vị quan sát chuẩn xác của một hàng trong bảng.
3. Phân loại thang đo thống kê cho các biến số sau: `species`, `island`, `bill_length_mm`, `body_mass_g`, `year`.
4. Đối chiếu câu trả lời ở câu 3 với kết quả của `penguins.dtypes`. Hãy chọn ra hai cột minh họa rõ nét việc kiểu dữ liệu phần mềm và thang đo thống kê trả lời hai câu hỏi hoàn toàn khác biệt.
5. Nếu tiến hành mã hóa biến phân loại `species` bằng các con số gồm $\text{Adelie} = 1$, $\text{Chinstrap} = 2$, $\text{Gentoo} = 3$, cột dữ liệu mới này có trở thành biến định lượng rời rạc hay không? Giải thích lý do.
6. Nếu thay thế biến số thực nghiệm `bill_length_mm` bằng ba mức phân loại có thứ tự gồm $\text{short} < \text{medium} < \text{long}$, hãy chỉ rõ:
   - Thang đo thống kê của biến số mới hình thành.
   - Một loại thông tin định lượng quan trọng đã bị mất đi so với phép đo ban đầu.
7. Chỉ dựa vào tệp dữ liệu CSV độc lập, chúng ta có thể nắm bắt đầy đủ quy trình các cá thể chim cánh cụt được tìm kiếm, tiếp cận và đo đạc ngoài tự nhiên hay không? Hãy nêu ít nhất hai câu hỏi then chốt về quá trình tạo dữ liệu mà bạn muốn làm sáng tỏ trước khi tổng quát hóa kết luận ra toàn thể quần thể chim cánh cụt.

::: tip Gợi ý
Đừng nhầm lẫn giữa cấu trúc lưu trữ và quy trình thực nghiệm. Kiểu dữ liệu số của năm hoặc mã hóa danh mục không biến đổi bản chất logic của biến số đó trong thống kê.
:::

::: solution Lời giải
1. Giới hạn của thông tin kích thước `shape`:
   Cặp số $(344, 8)$ chỉ biểu thị kích thước hình học của ma trận dữ liệu ($344$ hàng và $8$ cột). Nó hoàn toàn không cung cấp ý nghĩa thực nghiệm: Mỗi hàng là một cá thể động vật, một lần đo lặp, hay một số liệu tổng hợp của một đàn chim.

2. Xác định đơn vị quan sát:
   Đơn vị quan sát của bảng là một cá thể chim cánh cụt trưởng thành được khảo sát tại quần đảo Palmer trong một đợt thu thập dữ liệu thực địa.

3. Phân loại thang đo thống kê:
   - `species`: Biến định tính định danh (nominal categorical), chỉ loài chim.
   - `island`: Biến định tính định danh (nominal categorical), chỉ hòn đảo nơi cá thể sinh sống.
   - `bill_length_mm`: Biến định lượng liên tục (continuous quantitative), đo kích thước vật lý bằng milimét.
   - `body_mass_g`: Biến định lượng liên tục (continuous quantitative), đo trọng lượng cơ thể tính bằng gam.
   - `year`: Biến định lượng rời rạc biểu diễn thời gian (discrete quantitative time variable), đánh dấu các mốc năm theo lịch.

4. Minh họa sự khác biệt giữa dtype và thang đo thống kê:
   - Cột `year`: Có `dtype = int64` nhưng về mặt thống kê không phải là đại lượng đếm số lượng sự vật; nó đóng vai trò là biến định lượng rời rạc định vị mốc thời gian khảo sát.
   - Cột `species`: Có `dtype = str` (hoặc `object` tùy phiên bản pandas). Phần mềm chỉ nhận biết đây là các chuỗi văn bản thô, trong khi về thống kê đây là một biến định tính định danh gồm ba danh mục xác định.

5. Đánh giá phép mã hóa số học cho loài chim:
   Cột mới vẫn là biến định tính định danh. Việc thay thế các chữ cái bằng số $1, 2, 3$ chỉ là phép gán nhãn đại diện quy ước. Các phép toán số học như tính trung bình cộng hoặc khoảng cách chênh lệch giữa loài $1$ và loài $2$ hoàn toàn không mang ý nghĩa định lượng.

6. Chuyển đổi biến `bill_length_mm` thành ba mức:
   - Thang đo mới: Biến định tính thứ bậc (ordinal categorical) do tồn tại quan hệ trật tự $\text{short} < \text{medium} < \text{long}$.
   - Thông tin bị mất: Mất đi độ dài chính xác tính bằng milimét và khoảng cách định lượng tuyệt đối giữa các cá thể. Chúng ta không còn biết hai cá thể cùng nằm ở nhóm $\text{short}$ chênh lệch nhau bao nhiêu milimét, hay một con chim ở nhóm $\text{long}$ dài hơn con chim ở nhóm $\text{medium}$ bao nhiêu.

7. Quy trình tạo dữ liệu và hai câu hỏi cần làm rõ:
   Tệp CSV độc lập không thể cung cấp đầy đủ bức tranh về quy trình chọn mẫu tại hiện trường. Hai câu hỏi then chốt về quá trình tạo dữ liệu gồm:
   - Phương pháp bắt gặp và lấy mẫu: Các nhà khoa học đã tiếp cận các cá thể chim cánh cụt theo cơ chế chọn mẫu ngẫu nhiên hay chỉ chọn những tổ chim nằm gần trạm nghiên cứu, hoặc những con chim di chuyển chậm dễ bắt?
   - Tính độc lập của các quan sát: Trong $344$ hàng dữ liệu thu thập qua các năm $2007, 2008, 2009$, có cá thể nào được đánh dấu và đo lặp lại qua các năm hay mỗi hàng đảm bảo là một cá thể hoàn toàn tách biệt?
:::

---

### Bài 10: Quốc gia hay quốc gia–năm? Phép đo lặp nằm ở đâu?

Một nghiên cứu vĩ mô sử dụng bối cảnh dữ liệu về sự biến đổi kinh tế xã hội theo thời gian của các quốc gia. Xét một trích đoạn bảng thu nhỏ sau:

| `country` | `year` | `life_expectancy` | `population` | `region` |
| :--- | :---: | :---: | :---: | :--- |
| Vietnam | $2000$ | | | Asia |
| Vietnam | $2010$ | | | Asia |
| Japan | $2000$ | | | Asia |
| Japan | $2010$ | | | Asia |
| Kenya | $2000$ | | | Africa |
| Kenya | $2010$ | | | Africa |

Các ô giá trị số liệu được cố ý để trống nhằm tập trung vào việc đánh giá cấu trúc dữ liệu và mức độ chi tiết của các hàng.

1. Bảng dữ liệu trên có bao nhiêu hàng (observations)? Đơn vị quan sát của một hàng được xác định chính xác nhất là gì?
2. Có bao nhiêu quốc gia khác nhau xuất hiện trong bảng? Những quốc gia nào đang được tiến hành đo lặp lại theo thời gian?
3. Vì sao nhận định "$6$ hàng dữ liệu" không đồng nhất với việc chúng ta đang có dữ liệu từ "$6$ quốc gia độc lập"?
4. Cột `country` là đơn vị quan sát hay là một biến số trong bảng? Hãy giải thích vì sao hai khái niệm này không thể đánh đồng làm một.
5. Hãy phân loại thang đo thống kê cho bốn biến số: `year`, `life_expectancy`, `population`, `region`.
6. Nếu câu hỏi nghiên cứu là "quốc gia nào có tuổi thọ trung bình cao nhất vào năm $2010$?", mức độ chi tiết quốc gia–năm của bảng có đủ để trả lời về mặt cấu trúc hay không? Cần phân biệt tính đầy đủ về mặt cấu trúc với việc trả lời bằng số liệu thực tế như thế nào khi bảng đang để trống giá trị?
7. Nếu câu hỏi nghiên cứu đổi thành "quốc gia nào có tuổi thọ trung bình cao nhất trong cả giai đoạn?", bạn có thể chuyển đổi bảng này thành bảng có mức chi tiết một hàng cho mỗi quốc gia hay không? Khi đó thông tin chi tiết nào đã bị gộp đi, và vì sao việc chỉ quan sát hai mốc thời gian không phản ánh đầy đủ trung bình thực tế của toàn bộ giai đoạn?
8. Nếu câu hỏi nghiên cứu là "tuổi thọ thay đổi như thế nào theo thời gian trong cùng một quốc gia?", vì sao việc gộp sớm dữ liệu thành một hàng cho mỗi quốc gia sẽ phá hủy hoàn toàn dữ liệu cần thiết để trả lời câu hỏi?
9. Thuộc tính `region = Asia` được lặp lại ở nhiều hàng khác nhau trong bảng. Vì sao điều đó không đồng nghĩa với việc bảng dữ liệu bị trùng lặp (duplicate)?

::: tip Gợi ý
Đơn vị quan sát là sự kết hợp định danh tạo nên tính độc nhất cho mỗi hàng. Hãy phân biệt rõ giữa việc bảng dữ liệu có cấu trúc phù hợp với việc các ô số liệu có sẵn giá trị để tính toán.
:::

::: solution Lời giải
1. Số hàng và đơn vị quan sát chính xác:
   Bảng dữ liệu có đúng $6$ hàng quan sát. Đơn vị quan sát chính xác nhất của một hàng là một thực thể kết hợp quốc gia–năm (country-year), tức là một quốc gia cụ thể tại một năm xác định.

2. Số lượng quốc gia và phép đo lặp:
   Bảng chỉ ghi nhận $3$ quốc gia khác nhau gồm Vietnam, Japan và Kenya. Cả ba quốc gia này đều đang được đo lặp lại ở hai mốc thời gian là năm $2000$ và năm $2010$.

3. Sự khác biệt giữa số hàng và số quốc gia độc lập:
   Sáu hàng dữ liệu chỉ tương ứng với $3$ thực thể quốc gia độc lập. Các quan sát thuộc cùng một quốc gia tại các thời điểm khác nhau có tính phụ thuộc lịch sử và liên kết nội tại chặt chẽ, không thể coi là các quan sát độc lập ngẫu nhiên trong các mô hình suy luận.

4. Phân biệt `country` là biến số hay đơn vị quan sát:
   `country` là một biến số (variable) lưu trữ giá trị tên gọi của đối tượng. Đơn vị quan sát là toàn bộ thực thể mà một hàng mô tả (ở đây là cặp quốc gia–năm). Biến số là một thuộc tính đo lường được trên đơn vị quan sát, không phải chính bản thân đơn vị quan sát đó.

5. Phân loại thang đo thống kê cho các biến:
   - `year`: Biến định lượng rời rạc định vị thời gian (discrete quantitative time variable).
   - `life_expectancy`: Biến định lượng liên tục (continuous quantitative), đo lường số năm kỳ vọng sống.
   - `population`: Biến định lượng rời rạc (discrete quantitative), biểu diễn quy mô dân số dưới dạng số đếm cá thể người.
   - `region`: Biến định tính định danh (nominal categorical), phân loại các khu vực địa lý.

6. Đánh giá tính đầy đủ về cấu trúc so với tính toán số học:
   - Về mặt cấu trúc: Mức chi tiết quốc gia–năm là hoàn toàn đầy đủ và chuẩn xác để trả lời câu hỏi. Ta có thể lọc riêng các hàng có `year = 2010` và tiến hành so sánh cột `life_expectancy` giữa các quốc gia.
   - Phân biệt với tính toán thực tế: Cấu trúc phù hợp chỉ đảm bảo rằng mô hình dữ liệu có khả năng đáp ứng câu hỏi nghiên cứu. Việc các ô số liệu đang để trống có nghĩa là ta chưa có giá trị bằng số cụ thể để đưa ra câu trả lời định lượng cuối cùng.

7. Chuyển đổi mức chi tiết và hạn chế khi chỉ có hai mốc:
   - Hoàn toàn có thể gộp nhóm theo `country` và tính trung bình cộng của `life_expectancy` giữa hai năm để tạo thành bảng mới có mức chi tiết một hàng cho mỗi quốc gia.
   - Khi đó, thông tin về xu hướng diễn tiến theo thời gian (tăng, giảm hay đi ngang giữa hai năm $2000$ và $2010$) sẽ bị xóa bỏ hoàn toàn.
   - Việc chỉ quan sát hai mốc thời gian cách nhau $10$ năm chỉ phản ánh trung bình cộng của đúng hai điểm nút đó, hoàn toàn không đại diện cho mức trung bình của toàn bộ giai đoạn nếu trong suốt mười năm đó tuổi thọ có những biến động phức tạp (chẳng hạn dịch bệnh hay khủng hoảng y tế xảy ra vào giai đoạn giữa).

8. Nguy cơ từ việc gộp sớm dữ liệu:
   Câu hỏi về sự thay đổi theo thời gian đòi hỏi thông tin về sự biến thiên nội tại trong cùng một quốc gia (within-country variation). Việc gộp sớm dữ liệu thành một hàng cho mỗi quốc gia sẽ san phẳng toàn bộ chuỗi thời gian thành một giá trị tổng kết đơn lẻ, triệt tiêu trục thời gian `year`, làm mất đi dữ liệu cần thiết để tính toán hiệu số hoặc đánh giá tốc độ phát triển.

9. Phân biệt lặp giá trị phân loại và trùng lặp hàng (duplicate):
   Giá trị `region = Asia` xuất hiện ở nhiều hàng vì đây là một biến phân loại cấp cao mà nhiều quốc gia cùng chia sẻ. Bảng dữ liệu chỉ bị trùng lặp khi toàn bộ tất cả các biến trên hai hàng có giá trị giống hệt nhau, hoặc khi cùng một đơn vị quan sát (ví dụ cùng một cặp Vietnam–$2000$) xuất hiện nhiều hơn một lần.
:::

---

## Tài liệu tham khảo

- Dự án dữ liệu thực nghiệm Palmer Penguins: [Palmer Archipelago (Antarctica) penguin data](https://allisonhorst.github.io/palmerpenguins/)
- Hướng dẫn nhập xuất dữ liệu trong thư viện pandas: [pandas Getting Started: Reading and writing tabular data](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html)
- Tài liệu kỹ thuật chính thức của pandas DataFrame: [pandas.DataFrame API Reference](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
