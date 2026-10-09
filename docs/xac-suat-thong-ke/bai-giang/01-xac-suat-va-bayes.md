---
course: xac-suat-thong-ke
lecture: 01-xac-suat-va-bayes
section: lecture
title: "Xác suất có điều kiện & Bayes"
prerequisites: ["tap-hop", "khong-gian-mau", "xac-suat-co-dieu-kien", "doc-lap"]
lessonStatus: ready
description: "Không gian mẫu, tiên đề xác suất, bản chất của xác suất có điều kiện, tính độc lập thống kê và định lý Bayes trong suy luận dữ liệu."
---

Giả sử một xét nghiệm y tế chẩn đoán một căn bệnh hiếm có độ nhạy lên tới 99% (người có bệnh thì 99% xét nghiệm ra dương tính). Nếu một người đi khám ngẫu nhiên và nhận kết quả dương tính, xác suất người đó thực sự mắc bệnh có phải là 99% không?

Câu trả lời gây kinh ngạc của lý thuyết xác suất là: **hoàn toàn không**, xác suất thực tế người này mắc bệnh có thể chưa đầy 2%! 

Trực giác thông thường của con người thường thất bại trước các con số tỷ lệ vì ta hay đánh đồng điều kiện suy luận: ta nhầm lẫn giữa "xác suất dương tính khi đã có bệnh" với "xác suất có bệnh khi đã nhận kết quả dương tính". Bài học này sẽ trang bị công cụ toán học nền tảng để giải mã nghịch lý đó: **xác suất có điều kiện** và **định lý Bayes** — trái tim của suy luận thống kê và các mô hình học máy hiện đại.

## 1. Không gian mẫu và quy tắc cộng xác suất

Mọi bài toán xác suất đều khởi đầu từ một phép thử ngẫu nhiên. Tập hợp tất cả các kết cục sơ cấp có thể xảy ra của phép thử được gọi là **không gian mẫu**, ký hiệu là $\Omega$. Một **biến cố** $A$ là một tập con của không gian mẫu ($A \subseteq \Omega$).

Năm 1933, nhà toán học Andrey Kolmogorov đã đặt nền móng cho lý thuyết xác suất hiện đại bằng ba tiên đề:
1. **Tính không âm:** Với mọi biến cố $A$, xác suất $P(A) \ge 0$.
2. **Tính chuẩn hóa:** Toàn bộ không gian mẫu có xác suất bằng 1, tức $P(\Omega) = 1$.
3. **Tính cộng tính:** Nếu dãy các biến cố $A_1, A_2, \ldots$ xung khắc từng đôi một (nghĩa là không thể cùng xảy ra, $A_i \cap A_j = \emptyset$ với mọi $i \ne j$), thì xác suất của biến cố hợp bằng tổng các xác suất:
   $$P\left(\bigcup_{i=1}^\infty A_i\right) = \sum_{i=1}^\infty P(A_i).$$

Từ các tiên đề này, xét hai biến cố bất kỳ $A$ và $B$. Khi ta tính xác suất của biến cố hợp $A \cup B$ (nghĩa là $A$ xảy ra, hoặc $B$ xảy ra, hoặc cả hai cùng xảy ra), ta có quy tắc cộng tổng quát:

$$P(A \cup B) = P(A) + P(B) - P(A \cap B).$$

::: derivation Mở rộng bước biến đổi
Tại sao lại phải trừ đi số hạng $P(A \cap B)$? 

Khi ta lấy diện tích của $A$ cộng với diện tích của $B$, vùng giao nhau $A \cap B$ (những kết cục thuộc về cả hai biến cố) đã bị cộng hai lần. Vì vậy, ta bắt buộc phải trừ đi một lần để giữ đúng số đếm. 

Chỉ khi $A$ và $B$ là hai biến cố **xung khắc** ($A \cap B = \emptyset$), phần giao mới có xác suất $P(A \cap B) = 0$, và công thức trở về dạng giản lược quen thuộc: $P(A \cup B) = P(A) + P(B)$.
:::

## 2. Xác suất có điều kiện: Bản chất là thu hẹp thế giới quan sát

Trong đời sống thực tế, ta hiếm khi đưa ra phán đoán trong trạng thái hoàn toàn mù mờ thông tin. Thông tin mới xuất hiện sẽ làm thay đổi khả năng xảy ra của các biến cố.

Giả sử ta quan tâm đến biến cố $A$, nhưng được biết thêm rằng biến cố $B$ đã xảy ra ($P(B) > 0$). Xác suất của $A$ khi đã biết $B$ xảy ra được gọi là **xác suất có điều kiện**, ký hiệu là $P(A \mid B)$, và được định nghĩa bởi:

$$P(A \mid B) = \frac{P(A \cap B)}{P(B)}.$$

Bản chất của xác suất có điều kiện là **cắt lát và tái định vị không gian mẫu**. Ban đầu, toàn bộ vũ trụ kết cục là $\Omega$ với tổng xác suất là 1. Khi thông tin $B$ đã xảy ra xuất hiện:
- Mọi kết cục nằm ngoài $B$ lập tức trở nên bất khả thi và bị loại bỏ hoàn toàn.
- Tập hợp $B$ trở thành "vũ trụ mới" thu nhỏ của chúng ta. Mọi phép so sánh tỷ lệ bây giờ phải lấy $B$ làm mẫu số.
- Trong vũ trụ mới $B$ đó, phần duy nhất mà biến cố $A$ có thể xảy ra chính là phần giao $A \cap B$.

Từ định nghĩa trên, ta thu được **quy tắc nhân xác suất**:

$$P(A \cap B) = P(A \mid B)P(B) = P(B \mid A)P(A).$$

Điều này phản ánh một quy luật tự nhiên: để hai biến cố cùng xảy ra, trước hết biến cố thứ nhất phải xuất hiện, sau đó biến cố thứ hai xuất hiện trong điều kiện biến cố thứ nhất đã thành hiện thực.

## 3. Độc lập thống kê và sự khác biệt sống còn với xung khắc

Hai biến cố $A$ và $B$ được gọi là **độc lập thống kê** nếu việc biết $B$ xảy ra hoàn toàn không cung cấp thêm bất kỳ thông tin nào làm thay đổi khả năng xảy ra của $A$:

$$P(A \mid B) = P(A).$$

Thay điều kiện này vào quy tắc nhân, ta có định nghĩa tương đương và đối xứng cho tính độc lập:

$$P(A \cap B) = P(A)P(B).$$

::: warning Bẫy ngộ nhận: Độc lập không đồng nghĩa với xung khắc
Đây là một trong những ngộ nhận tai hại nhất của người học xác suất: nhầm lẫn giữa tính độc lập ($P(A \cap B) = P(A)P(B)$) và tính xung khắc ($A \cap B = \emptyset$).

- **Xung khắc** là một mối quan hệ hình học: hai tập hợp không có điểm chung. Nếu $A$ và $B$ xung khắc và đều có xác suất dương, thì chúng **không bao giờ độc lập**! Bởi vì nếu biết $B$ đã xảy ra, ta biết chắc chắn 100% $A$ không thể xảy ra ($P(A \mid B) = 0 \ne P(A)$). Việc biết $B$ đã mang lại lượng thông tin tối đa về $A$.
- **Độc lập** đòi hỏi hai tập hợp **bắt buộc phải có phần giao nhau**: $P(A \cap B) = P(A)P(B) > 0$. Tỷ lệ phần giao bên trong $B$ đúng bằng tỷ lệ của $A$ trong toàn bộ không gian mẫu $\Omega$.
:::

## 4. Công thức xác suất toàn phần: Chia để trị

Trong thực tế, một biến cố $A$ có thể xảy ra thông qua nhiều con đường, nhiều kịch bản khác nhau.

Giả sử không gian mẫu $\Omega$ được chia thành $n$ kịch bản loại trừ lẫn nhau $B_1, B_2, \ldots, B_n$ sao cho chúng phủ kín toàn bộ không gian:
- $B_i \cap B_j = \emptyset$ với mọi $i \ne j$ (không kịch bản nào xảy ra đồng thời).
- $\bigcup_{i=1}^n B_i = \Omega$ (chắc chắn một trong các kịch bản phải xảy ra).

Tập hợp $\{B_1, \ldots, B_n\}$ như vậy được gọi là một **phân hoạch** của không gian mẫu. Khi đó, xác suất của một biến cố $A$ bất kỳ được tính bằng tổng xác suất của $A$ dưới từng kịch bản:

$$P(A) = \sum_{i=1}^n P(A \cap B_i) = \sum_{i=1}^n P(A \mid B_i)P(B_i).$$

Đây là một cách người ta hay dùng trong thực tế để tính xác suất của những bài toán phức tạp: thay vì tính trực tiếp một biến cố khó, ta chẻ nhỏ bài toán theo các giả thuyết nền tảng khả dĩ, tính xác suất cục bộ trong từng giả thuyết, rồi lấy trung bình có trọng số theo xác suất xuất hiện của từng giả thuyết đó.

## 5. Định lý Bayes: Đảo ngược chiều suy luận

Định lý Bayes, mang tên nhà toán học Thomas Bayes, là hệ quả trực tiếp từ quy tắc nhân và công thức xác suất toàn phần. 

Trong khoa học, ta thường dễ dàng đo lường chiều thuận: "Nếu giả thuyết $B_k$ đúng, thì khả năng quan sát thấy dữ liệu $A$ là bao nhiêu?" ($P(A \mid B_k)$). Nhưng điều ta thực sự khao khát trong suy luận lại là chiều nghịch: "Khi đã tận mắt quan sát thấy dữ liệu $A$, thì xác suất giả thuyết $B_k$ là đúng bằng bao nhiêu?" ($P(B_k \mid A)$).

Định lý Bayes cho phép ta thực hiện bước đảo chiều kỳ diệu đó:

$$P(B_k \mid A) = \frac{P(A \mid B_k)P(B_k)}{P(A)} = \frac{P(A \mid B_k)P(B_k)}{\sum_{i=1}^n P(A \mid B_i)P(B_i)}.$$

Ba thành phần cốt lõi của công thức Bayes:
1. **Xác suất tiên nghiệm (Prior)** $P(B_k)$: Mức độ tin tưởng ban đầu vào giả thuyết $B_k$ trước khi thu thập dữ liệu mới.
2. **Độ hợp lý (Likelihood)** $P(A \mid B_k)$: Khả năng dữ liệu $A$ xuất hiện nếu giả thuyết $B_k$ thực sự đúng.
3. **Xác suất hậu nghiệm (Posterior)** $P(B_k \mid A)$: Niềm tin được cập nhật dành cho giả thuyết $B_k$ sau khi đã tiếp nhận bằng chứng $A$.

### 5.1. Giải mã nghịch lý xét nghiệm y tế bằng số đếm tự nhiên

Để thấy sức mạnh của định lý Bayes và giải thích trọn vẹn câu hỏi mở đầu bài giảng, hãy xem xét một ví dụ y khoa cụ thể:
- Trong một cộng đồng, tỷ lệ mắc căn bệnh hiếm $B$ là $0{,}1\%$ (nghĩa là $P(B) = 0{,}001$; tỷ lệ người khỏe mạnh $P(\neg B) = 0{,}999$).
- Xét nghiệm có độ nhạy $99\%$: nếu có bệnh, xác suất nhận kết quả dương tính là $P(+ \mid B) = 0{,}99$.
- Xét nghiệm có tỷ lệ dương tính giả $5\%$: người hoàn toàn khỏe mạnh vẫn có xác suất bị báo nhầm dương tính là $P(+ \mid \neg B) = 0{,}05$.

Một người được chọn ngẫu nhiên đi xét nghiệm và nhận kết quả dương tính (+). Xác suất người này thực sự mang bệnh $P(B \mid +)$ là bao nhiêu?

Áp dụng định lý Bayes:
$$P(+) = P(+ \mid B)P(B) + P(+ \mid \neg B)P(\neg B) = 0{,}99 \times 0{,}001 + 0{,}05 \times 0{,}999 = 0{,}00099 + 0{,}04995 = 0{,}05094.$$

$$P(B \mid +) = \frac{P(+ \mid B)P(B)}{P(+)} = \frac{0{,}00099}{0{,}05094} \approx 0{,}0194 = 1{,}94\%!$$

Một kết quả gây sửng sốt: dù xét nghiệm có độ nhạy 99%, một người nhận kết quả dương tính vẫn có tới hơn $98\%$ khả năng là hoàn toàn khỏe mạnh!

::: example Biến đổi trực quan bằng bảng tần số 100.000 người
Một cách người ta hay dùng trong thực tế để không bao giờ bị rối loạn bởi các con số thập phân là quy đổi toàn bộ bài toán về một quần thể cụ thể, ví dụ $100.000$ người:

| Tình trạng thực tế | Số lượng người | Kết quả dương tính (+) | Kết quả âm tính (-) |
| :--- | ---:| ---:| ---:|
| **Có bệnh ($B$)** | $100$ | $99$ | $1$ |
| **Không bệnh ($\neg B$)** | $99.900$ | $4.995$ | $94.905$ |
| **Tổng cộng** | $100.000$ | **$5.094$** | $94.906$ |

Quan sát bảng số đếm:
1. Trong $100.000$ người, chỉ có đúng $100$ người có bệnh. Vì độ nhạy là $99\%$, có $99$ người có bệnh nhận kết quả dương tính.
2. Có tới $99.900$ người không có bệnh. Dù tỷ lệ dương tính giả chỉ là $5\%$, nhưng $5\%$ của một số lượng người khỏe mạnh khổng lồ sẽ tạo ra tới $4.995$ ca dương tính giả!
3. Tổng số người cầm tờ giấy kết quả dương tính trên tay là $99 + 4.995 = 5.094$ người.
4. Trong số $5.094$ người dương tính đó, chỉ có vỏn vẹn $99$ người thực sự có bệnh. 

Xác suất người có kết quả dương tính thực sự mắc bệnh là:
$$\frac{99}{5.094} \approx 1{,}94\%.$$
:::

Trực giác của ta bị đánh lừa vì ta chỉ chú ý đến con số độ nhạy $99\%$ mà quên mất **tỷ lệ nền (base rate)**: căn bệnh quá hiếm trong cộng đồng ($0{,}1\%$), khiến cho số lượng người dương tính giả từ nhóm khỏe mạnh áp đảo hoàn toàn số lượng người dương tính thật!

## 6. Minh họa tương tác

Dưới đây là công cụ mô phỏng cập nhật xác suất Bayes. Bạn có thể thay đổi xác suất tiên nghiệm và độ nhạy để quan sát sự dịch chuyển của xác suất hậu nghiệm:

<CodeIllustration type="bayes" />

## 7. Các bẫy suy luận cần cảnh giác

Trong lập luận hàng ngày và phân tích dữ liệu, hãy luôn tự rà soát hai cạm bẫy sau:

1. **Bẫy công tố viên (Prosecutor's Fallacy):** Đồng nhất $P(\text{Chứng cứ} \mid \text{Vô tội})$ với $P(\text{Vô tội} \mid \text{Chứng cứ})$. Việc một dấu vết AND tại hiện trường chỉ xuất hiện ở 1 trên 1 triệu người vô tội không có nghĩa là người mang dấu vết đó có 99,9999% khả năng phạm tội. Ta vẫn cần nhân với tỷ lệ tiên nghiệm của nghi phạm trong dân số.
2. **Bỏ qua xác suất tiên nghiệm (Base Rate Neglect):** Đánh giá độ tin cậy của một thuật toán phân loại (như bộ lọc spam, hệ thống phát hiện gian lận thẻ) chỉ dựa trên độ chính xác cục bộ mà bỏ qua tần suất xuất hiện thực tế của hành vi gian lận.

## 8. Bài tập tự luyện

### Bài 1. Phân biệt độc lập và xung khắc qua bảng dữ liệu

::: exercise
Một lớp học gồm 100 sinh viên. Trong đó có 40 sinh viên đạt điểm Giỏi môn Toán (biến cố $M$), 30 sinh viên đạt điểm Giỏi môn Tin học (biến cố $C$), và 12 sinh viên đạt điểm Giỏi ở cả hai môn.

1. Hai biến cố $M$ và $C$ có xung khắc nhau không? Vì sao?
2. Hai biến cố $M$ và $C$ có độc lập thống kê với nhau không? Chứng minh bằng công thức.
3. Nếu chọn ngẫu nhiên một sinh viên đạt điểm Giỏi môn Tin học, xác suất sinh viên này cũng đạt điểm Giỏi môn Toán là bao nhiêu?
:::

::: hint
Lập tỷ lệ xác suất $P(M)$, $P(C)$, và $P(M \cap C)$. Kiểm tra xem tích $P(M)P(C)$ có bằng $P(M \cap C)$ không.
:::

::: solution
1. $M$ và $C$ **không xung khắc** vì có 12 sinh viên đạt điểm Giỏi cả hai môn, tức $M \cap C \ne \emptyset$ và $P(M \cap C) = \frac{12}{100} = 0{,}12 > 0$.

2. Ta tính xác suất của từng biến cố:
   - $P(M) = \frac{40}{100} = 0{,}40$.
   - $P(C) = \frac{30}{100} = 0{,}30$.
   - Tích hai xác suất: $P(M) \times P(C) = 0{,}40 \times 0{,}30 = 0{,}12$.
   
   Vì $P(M \cap C) = 0{,}12 = P(M)P(C)$, nên hai biến cố $M$ và $C$ **độc lập thống kê** với nhau. Việc một sinh viên giỏi Tin không làm thay đổi xác suất sinh viên đó giỏi Toán.

3. Xác suất giỏi Toán khi biết đã giỏi Tin là:
   $$P(M \mid C) = \frac{P(M \cap C)}{P(C)} = \frac{0{,}12}{0{,}30} = 0{,}40.$$
   Kết quả đúng bằng $P(M) = 0{,}40$, hoàn toàn phù hợp với kết luận hai biến cố độc lập ở câu 2.
:::

### Bài 2. Bộ lọc thư rác Naive Bayes trong thực tế

::: exercise
Một hệ thống lọc thư điện tử ghi nhận: trong hộp thư của người dùng, $20\%$ tổng số thư là thư rác (spam, ký hiệu $S$), còn $80\%$ là thư hợp lệ (ham, ký hiệu $H$).
- Từ khóa "khuyến mãi" xuất hiện trong $70\%$ các thư rác.
- Từ khóa "khuyến mãi" chỉ xuất hiện trong $5\%$ các thư hợp lệ.

Một bức thư mới gửi đến có chứa từ khóa "khuyến mãi" (biến cố $K$). Hãy tính xác suất bức thư này là thư rác.
:::

::: hint
Áp dụng công thức xác suất toàn phần để tính $P(K)$, sau đó dùng định lý Bayes để tính $P(S \mid K)$.
:::

::: solution
Ta có các thông số ban đầu:
- $P(S) = 0{,}20$; $P(H) = 0{,}80$.
- $P(K \mid S) = 0{,}70$; $P(K \mid H) = 0{,}05$.

Bước 1: Tính xác suất xuất hiện từ "khuyến mãi" trong một bức thư bất kỳ theo công thức xác suất toàn phần:
$$P(K) = P(K \mid S)P(S) + P(K \mid H)P(H) = 0{,}70 \times 0{,}20 + 0{,}05 \times 0{,}80 = 0{,}14 + 0{,}04 = 0{,}18.$$

Bước 2: Áp dụng định lý Bayes để tính xác suất thư là spam khi đã thấy từ "khuyến mãi":
$$P(S \mid K) = \frac{P(K \mid S)P(S)}{P(K)} = \frac{0{,}14}{0{,}18} = \frac{7}{9} \approx 77{,}78\%.$$

Như vậy, sự xuất hiện của từ khóa "khuyến mãi" đã cập nhật niềm tin của hệ thống: từ tỷ lệ ban đầu $20\%$ (prior) vọt lên thành gần $78\%$ (posterior). Hệ thống có thể tự tin chuyển bức thư này vào hòm thư rác.
:::

[Bài tiếp theo: Biến ngẫu nhiên & phân phối](/xac-suat-thong-ke/bai-giang/02-bien-ngau-nhien.md).
