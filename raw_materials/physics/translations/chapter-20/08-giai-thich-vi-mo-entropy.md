<!-- Source: Section20.8, printed665–668, PDF685–688. -->

## 20.8. Giải thích vi mô của entropy

Ở mục trước, ta đã tiếp cận entropy dưới góc độ nhiệt động lực học vĩ mô cổ điển thông qua nhiệt lượng trao đổi thuận nghịch $dQ$ và nhiệt độ tuyệt đối $T$. Tuy nhiên, bản chất vật lý thực sự của entropy chỉ được phơi bày trọn vẹn khi ta nhìn sâu vào cấu trúc vi mô của vật chất: Vị trí, vận tốc và trạng thái chuyển động hỗn loạn của hàng tỷ tỷ phân tử cấu tạo nên hệ.

### Trạng thái vĩ mô và trạng thái vi mô

Để làm sáng tỏ mối liên hệ giữa thế giới vi mô và các đại lượng nhiệt động vĩ mô, ta phân biệt hai khái niệm then chốt:
- **Trạng thái vĩ mô (macroscopic state)**: Được xác định bởi các thông số đo lường được ở quy mô lớn như áp suất $p$, thể tích $V$, nhiệt độ $T$, hoặc tổng số lượng kết quả quan sát được (chẳng hạn như tổng số mặt ngửa khi tung các đồng xu).
- **Trạng thái vi mô (microscopic state)**: Là sự mô tả chi tiết, chính xác tuyệt đối trạng thái của từng hạt riêng lẻ trong hệ tại một thời điểm nhất định (vị trí tọa độ và vector vận tốc của từng phân tử, hoặc mặt sấp/ngửa của từng đồng xu cụ thể).

Một trạng thái vĩ mô xác định có thể tương ứng với rất nhiều trạng thái vi mô khác nhau. Số lượng các trạng thái vi mô tương ứng với cùng một trạng thái vĩ mô được gọi là **bội số trạng thái vi mô** (multiplicity / thermodynamic probability), ký hiệu là $w$.

### Mô hình bốn đồng xu

Xét một mô hình đơn giản gồm $N = 4$ đồng xu giống nhau được đánh dấu từ 1 đến 4 (Hình 20.21). Mỗi đồng xu có hai trạng thái khả dĩ: Ngửa (N) hoặc Sấp (S).
Tổng số trạng thái vi mô của hệ bốn đồng xu là:

$$
2^4 = 16
$$

Các trạng thái vi mô này phân bố vào 5 trạng thái vĩ mô khác nhau tùy theo tổng số mặt ngửa:

![Hình 20.21: Toàn bộ các trạng thái vi mô và vĩ mô của hệ gồm bốn đồng xu](../img/young-20/b-hinh-20-21.png)

*Hình 20.21: Toàn bộ các trạng thái vi mô có thể có của bốn đồng xu. Mỗi trạng thái vĩ mô có thể tương ứng với nhiều trạng thái vi mô khác nhau. Trạng thái có tính hỗn loạn cao nhất (hai ngửa, hai sấp) sở hữu số trạng thái vi mô lớn nhất ($w = 6$).*

Bảng phân bố chi tiết các trạng thái:

| Ngửa | Số cách | Xác suất |
| ---: | ---: | ---: |
| 4 | 1 | $1/16$ |
| 3 | 4 | $4/16$ |
| 2 | 6 | $6/16$ |
| 1 | 4 | $4/16$ |
| 0 | 1 | $1/16$ |
| Tổng | 16 | $1$ |

Các trạng thái vi mô được liệt kê tường minh, với N là ngửa và S là sấp:

- Bốn ngửa: NNNN, xác suất6,25%.
- Ba ngửa: NNNS, NNSN, NSNN, SNNN, xác suất25,0%.
- Hai ngửa: NNSS, NSNS, NSSN, SNNS, SNSN, SSNN, xác suất37,5%.
- Một ngửa: NSSS, SNSS, SSNS, SSSN, xác suất25,0%.
- Không ngửa: SSSS, xác suất6,25%.

Nếu ta bỏ bốn đồng xu vào một chiếc hộp, lắc mạnh rồi mở nắp ra:
- Khả năng xuất hiện trạng thái có trật tự tuyệt đối (toàn ngửa hoặc toàn sấp) là rất nhỏ: Chỉ $1/16$.
- Khả năng xuất hiện trạng thái hỗn độn nhất (2 ngửa, 2 sấp) là lớn nhất: Chiếm tới $6/16 = 37{,}5\%$.

Khi số lượng hạt $N$ tăng lên:
- Với $N = 100$ đồng xu: Tổng số trạng thái vi mô là $2^{100} \approx 1{,}27 \times 10^{30}$. Số trạng thái vi mô của trạng thái trật tự (100 ngửa) vẫn chỉ là $w = 1$, trong khi trạng thái cân bằng nhất (50 ngửa, 50 sấp) có tới $w \approx 10^{29}$ trạng thái vi mô. Xác suất để ngẫu nhiên lắc được 100 mặt ngửa là $1/2^{100} \approx 10^{-30}$, nhỏ đến mức thực tế không bao giờ có thể xảy ra.
- Với một khối khí thông thường chứa cỡ số Avogadro hạt ($N \approx 10^{23}$ phân tử): Phân bố thống kê tập trung cực kỳ sắc nét xung quanh trạng thái vĩ mô có số trạng thái vi mô $w$ cực đại. Trạng thái vĩ mô cân bằng nhiệt động chính là trạng thái sở hữu bội số vi mô $w$ áp đảo tuyệt đối so với mọi trạng thái khác.

### Công thức Boltzmann cho entropy

Nhà vật lý người Áo Ludwig Boltzmann (1844–1906) đã khám phá ra mối liên hệ định lượng giữa entropy vĩ mô $S$ và số trạng thái vi mô $w$. Mối liên hệ này được khắc ghi trên bia mộ của ông tại Vienna:

$$
S = k \ln w
$$

Trong đó:
- $w$ là số trạng thái vi mô tương ứng với trạng thái vĩ mô đang xét (một đại lượng không thứ nguyên, $w \ge 1$).
- $k = 1{,}381 \times 10^{-23}\,\mathrm{J/K}$ là hằng số Boltzmann ($k = R/N_A$).

Hàm logarit tự nhiên $\ln$ mang ý nghĩa vật lý cốt lõi: Nếu ta ghép hai hệ độc lập 1 và 2 lại với nhau:
- Theo lý thuyết xác suất, số trạng thái vi mô của hệ hợp nhất là tích số: $w = w_1 \times w_2$.
- Theo tính chất cộng được của các đại lượng nhiệt động vĩ mô, entropy của hệ hợp nhất phải bằng tổng hai entropy thành phần: $S = S_1 + S_2$.

Do tính chất $\ln(w_1 w_2) = \ln w_1 + \ln w_2$, hàm logarit là hàm toán học duy nhất thỏa mãn đồng thời hai yêu cầu này.

Độ biến thiên entropy của một hệ chuyển từ trạng thái vĩ mô 1 (có $w_1$ trạng thái vi mô) sang trạng thái vĩ mô 2 (có $w_2$ trạng thái vi mô) là:

$$
\begin{aligned}
\Delta S &= S_2 - S_1 \\
&= k \ln \frac{w_2}{w_1}
\end{aligned}
$$

Hệ thức trên cho thấy: Nếu hệ biến đổi sang một trạng thái vĩ mô có số trạng thái vi mô lớn hơn ($w_2 > w_1$), độ biến thiên entropy của hệ sẽ mang dấu dương ($\Delta S > 0$). Chiều tự phát của các quá trình tự nhiên chính là chiều tiến tới trạng thái có xác suất thống kê lớn nhất, tức là trạng thái có số trạng thái vi mô cực đại.

::: example Ví dụ 20.11: Tính biến thiên entropy theo quan điểm vi mô
Sử dụng công thức Boltzmann để tính độ biến thiên entropy trong quá trình giãn nở tự do của $n\,\mathrm{mol}$ khí lý tưởng ở nhiệt độ $T$ từ thể tích $V$ sang thể tích $2V$ như đã mô tả trong Ví dụ 20.8 (Hình 20.22).

**Tóm tắt**:
- Số mol khí: $n\,\mathrm{mol}$
- Số phân tử khí: $N = n N_A$
- Thể tích ban đầu: $V$; thể tích cuối: $2V$
- Nhiệt độ $T$ không đổi.

**Hướng đi**:
- Trong quá trình giãn nở tự do, khối khí không sinh công ngoại lực và không trao đổi nhiệt nên động năng trung bình và tốc độ của các phân tử không thay đổi. Trạng thái vận tốc của các phân tử giữ nguyên.
- Tuy nhiên, mỗi phân tử có không gian chuyển động tăng gấp đôi, do đó số vị trí không gian khả dĩ cho mỗi phân tử tăng lên 2 lần.
- Xét hệ gồm $N$ phân tử độc lập, số trạng thái vi mô tổng cộng của hệ sau khi giãn nở sẽ tăng lên $2^N$ lần.
- Áp dụng công thức biến thiên entropy vi mô để tính $\Delta S$.

![Hình 20.22: Số trạng thái vi mô tăng thêm $2^N$ lần khi thể tích khối khí tăng gấp đôi](../img/young-20/b-hinh-20-22.png)

*Hình 20.22: Trong quá trình giãn nở tự do của $N$ phân tử khí làm thể tích tăng gấp đôi, số trạng thái vi mô khả dĩ tăng lên một thừa số bằng $2^N$.*

**Các bước tính toán**:
Gọi $w_1$ là số trạng thái vi mô của toàn hệ khi khối khí chiếm thể tích $V$ (Hình 20.22a).
Sau khi vách ngăn bị phá vỡ, thể tích khối khí tăng thành $2V$ (Hình 20.22b). Mỗi phân tử trong số $N$ phân tử có số trạng thái vị trí tăng gấp đôi, vì vậy số trạng thái vi mô $w_2$ của khối khí khi chiếm thể tích $2V$ là:

$$
w_2 = 2^N w_1
$$

Tỷ số trạng thái vi mô là:

$$
\frac{w_2}{w_1} = 2^N
$$

Áp dụng công thức biến thiên entropy vi mô:

$$
\begin{aligned}
\Delta S &= k \ln(2^N) \\
&= N k \ln 2
\end{aligned}
$$

Vì số phân tử là $N = n N_A$ và hằng số Boltzmann là $k = R/N_A$, ta có:

$$
\begin{aligned}
N k &= (n N_A)\left(\frac{R}{N_A}\right) \\
&= n R
\end{aligned}
$$

Thay vào biểu thức trên, ta nhận được:

$$
\Delta S = n R \ln 2
$$

**Đánh giá kết quả**:
Ta nhận được kết quả hoàn toàn trùng khớp với kết quả suy ra từ phương pháp nhiệt động lực học vĩ mô trong Ví dụ 20.8 ($\Delta S = n R \ln 2$). Điều đáng kinh ngạc là phép tính vi mô này được thực hiện trực tiếp từ cấu trúc không gian của các phân tử mà không cần viện dẫn đến bất kỳ con đường nhiệt động lực học thuận nghịch tưởng tượng nào.
:::

### Ứng dụng: Sự cuộn gập của chuỗi phân tử polymer trong dung dịch

Khái niệm entropy vi mô đóng vai trò quyết định trong việc giải thích hình dạng và tính chất cơ lý của các vật liệu polymer và phân tử sinh học (như protein và DNA).

Một phân tử polyethylene, loại nhựa phổ biến nhất hiện nay, là một chuỗi polymer dài gồm hàng nghìn mắt xích monomer $\mathrm{C_2H_4}$ liên kết với nhau bằng các liên kết cộng hóa trị carbon–carbon (Hình ứng dụng 20.2). Tại mỗi liên kết đơn $\mathrm{C-C}$, các nhóm nguyên tử có thể tự do quay quanh trục liên kết một góc tương đối.

![Hình ứng dụng 20.2: Sự cuộn gập tự phát của chuỗi phân tử polymer trong dung dịch để tối đa hóa entropy](../img/young-20/b-ung-dung-20-02.png)

*Hình ứng dụng 20.2: Sự cuộn gập của các chuỗi polymer trong dung dịch. Một phân tử polyethylene là một chuỗi dài các mắt xích $\mathrm{C_2H_4}$. Chỉ có một số rất ít cấu hình làm chuỗi polymer duỗi thẳng hoàn toàn (trật tự cao, entropy thấp). Ngược lại, có vô số cấu hình xoắn gập ngẫu nhiên (cuộn rối) có cùng năng lượng. Do đó, chuỗi polymer tự phát co cuộn lại trong dung dịch để đạt trạng thái có entropy cực đại.*

Xét hai trạng thái cấu hình của chuỗi polymer trong dung dịch:
- **Cấu hình duỗi thẳng hoàn toàn**: Để toàn bộ chuỗi duỗi thẳng tắp từ đầu đến cuối, mọi liên kết $\mathrm{C-C}$ dọc theo mạch chính đều phải nằm ở các góc xoay xác định nghiêm ngặt. Trạng thái vĩ mô này chỉ tương ứng với một số lượng cực kỳ nhỏ các trạng thái vi mô ($w$ rất nhỏ, entropy rất thấp).
- **Cấu hình cuộn rối ngẫu nhiên**: Có hàng triệu cách xoay ngẫu nhiên các liên kết khác nhau trong không gian mà vẫn tạo thành một búi cuộn có kích thước tương đương ($w$ khổng lồ, entropy cực cao).

Theo nguyên lý thứ hai, hệ luôn có xu hướng tự phát chuyển dịch về trạng thái có số trạng thái vi mô lớn nhất. Do đó, khi hòa tan trong dung dịch, các chuỗi polymer sẽ tự động co cụm và cuộn rối lại thành những búi tròn ngẫu nhiên. Khi ta tác dụng ngoại lực kéo căng một sợi cao su, ta đang cưỡng bức các chuỗi polymer chuyển từ cấu hình cuộn rối (entropy cao) sang cấu hình duỗi thẳng (entropy thấp). Ngay khi buông tay, lực đàn hồi entropy sẽ lập tức kéo các chuỗi polymer co rút trở lại hình dạng cuộn rối ban đầu.

### Tự kiểm tra kiến thức mục 20.8

Một lượng khí lý tưởng gồm $N$ phân tử giãn nở đến thể tích gấp đôi thể tích ban đầu. Hỏi trong trường hợp nào tỷ số giữa số trạng thái vi mô cuối và đầu $w_2/w_1$ có giá trị lớn hơn: (i) Quá trình giãn nở đẳng nhiệt, hay (ii) Quá trình giãn nở đoạn nhiệt thuận nghịch? Hay tỷ số $w_2/w_1$ trong hai trường hợp là như nhau?

<details>
<summary>Xem lời giải thích</summary>

**Đáp án**: Trường hợp (i) giãn nở đẳng nhiệt có tỷ số $w_2/w_1$ lớn hơn.

**Giải thích chi tiết**:
- Đối với trường hợp (i) giãn nở đẳng nhiệt: Nhiệt độ của khối khí được giữ không đổi ($T_2 = T_1$), vì vậy phân bố vận tốc của các phân tử không thay đổi. Trong khi đó, thể tích tăng gấp đôi làm số trạng thái vị trí không gian của mỗi phân tử tăng gấp hai lần. Theo Ví dụ 20.11, tỷ số trạng thái vi mô là:

$$
\frac{w_2}{w_1} = 2^N
$$

kéo theo $\Delta S = N k \ln 2 > 0$.
- Đối với trường hợp (ii) giãn nở đoạn nhiệt thuận nghịch: Theo Ví dụ 20.7, quá trình đoạn nhiệt thuận nghịch là quá trình đẳng entropy, do đó độ biến thiên entropy bằng không:

$$
\Delta S = 0
$$

Từ công thức Boltzmann $\Delta S = k \ln(w_2/w_1) = 0$, ta suy ra:

$$
\frac{w_2}{w_1} = 1
$$

- Bản chất vật lý của trường hợp (ii) là: Khi khối khí giãn nở sinh công đoạn nhiệt, nội năng suy giảm khiến nhiệt độ của khối khí hạ thấp. Vận tốc và động năng của các phân tử giảm đi, làm thu hẹp số trạng thái vi mô về mặt vận tốc. Sự suy giảm số trạng thái vi mô về vận tốc triệt tiêu chính xác sự gia tăng số trạng thái vi mô về vị trí không gian, khiến tổng số trạng thái vi mô $w$ của khối khí hoàn toàn không đổi ($w_2 = w_1$).
- Do đó, tỷ số $w_2/w_1$ trong quá trình giãn đẳng nhiệt ($2^N$) lớn hơn rất nhiều so với trong quá trình giãn đoạn nhiệt thuận nghịch ($1$).
</details>
