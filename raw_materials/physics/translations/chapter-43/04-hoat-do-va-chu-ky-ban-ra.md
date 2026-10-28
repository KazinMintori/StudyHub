## 43.4 Hoạt độ và chu kỳ bán rã

Khi khảo sát một lượng xác định các hạt nhân thuộc một đồng vị phóng xạ cụ thể, nếu không có thêm hạt nhân mới nào được sinh ra, số lượng hạt nhân chưa phân rã sẽ giảm dần theo thời gian. Sự sụt giảm này tuân theo quy luật thống kê: Không có cách nào dự đoán chính xác thời điểm một hạt nhân cụ thể sẽ phân rã. Hơn nữa, những thay đổi về môi trường vật lý hay hóa học xung quanh, chẳng hạn như phản ứng hóa học, đốt nóng hay làm lạnh, đều không gây ảnh hưởng đáng kể đến tốc độ phân rã. Tốc độ này biến thiên trong một dải rất rộng giữa các đồng vị khác nhau.

### Tốc độ phân rã phóng xạ

Gọi $N(t)$ là số lượng hạt nhân phóng xạ rất lớn có trong mẫu tại thời điểm $t$, và gọi $dN(t)$ là biến thiên của số hạt nhân đó trong khoảng thời gian ngắn $dt$. Vì số hạt nhân giảm dần theo thời gian, đại lượng $dN(t)$ luôn nhận giá trị âm. Ký hiệu $N(t)$ được dùng để phân biệt rõ với số neutron $N$ của hạt nhân.

Số phân rã diễn ra trong khoảng thời gian $dt$ là $-dN(t)$. Tốc độ biến thiên tức thời của $N(t)$ là đạo hàm $dN(t)/dt$, mang giá trị âm. Do đó, lượng đại số $-dN(t)/dt$ được định nghĩa là tốc độ phân rã hay hoạt độ (activity) của mẫu. Khi số lượng hạt nhân trong mẫu càng nhiều, số phân rã xảy ra trong mỗi đơn vị thời gian càng lớn. Hoạt độ của mẫu tỉ lệ thuận trực tiếp với số hạt nhân $N(t)$ hiện diện ở thời điểm khảo sát, liên hệ qua một hằng số tỉ lệ $\lambda$:

$$
-\frac{dN(t)}{dt} = \lambda N(t) \tag{43.16}
$$

Hằng số $\lambda$ được gọi là hằng số phân rã (decay constant), mang giá trị đặc trưng riêng biệt cho từng đồng vị phóng xạ. Giá trị $\lambda$ lớn tương ứng với quá trình phân rã diễn ra nhanh, còn giá trị $\lambda$ nhỏ tương ứng với quá trình phân rã chậm. Biến đổi phương trình trên cho thấy $\lambda$ chính là tỉ số giữa số phân rã trong một đơn vị thời gian và số hạt nhân phóng xạ còn lại. Về mặt ý nghĩa xác suất: Hằng số phân rã $\lambda$ biểu thị xác suất trên mỗi đơn vị thời gian để một hạt nhân bất kỳ phân rã.

Dạng toán học của phương trình vi phân này hoàn toàn tương tự bài toán phóng điện của tụ điện qua điện trở. Tích phân hai vế từ thời điểm ban đầu $t = 0$ với số hạt nhân ban đầu $N(0) = N_0$, quy luật suy giảm số hạt nhân theo thời gian có dạng:

$$
N(t) = N_0 e^{-\lambda t} \tag{43.17}
$$

![Hình 43.8: Số hạt nhân chưa phân rã giảm theo hàm mũ và còn một nửa sau mỗi chu kỳ bán rã.](/vat-ly-2/bai-giang/img/young-43/hinh-43-08.png)

Trục ngang biểu diễn thời gian t, trục đứng biểu diễn số hạt nhân $N(t)$. Các mức $N_0/2$, $N_0/4$, $N_0/8$ và $N_0/16$ tương ứng với các chu kỳ bán rã liên tiếp.

Hàm số này mô tả đường cong suy giảm theo hàm mũ. Do hoạt độ tại mỗi thời điểm luôn tỉ lệ thuận với số hạt nhân, $-dN(t)/dt = \lambda N(t)$, hoạt độ của mẫu phóng xạ cũng suy giảm theo hàm mũ cùng dạng với số hạt nhân.

Chu kỳ bán rã $T_{1/2}$ là khoảng thời gian cần thiết để số lượng hạt nhân phóng xạ giảm đi một nửa so với lượng ban đầu $N_0$. Sau mỗi khoảng thời gian $T_{1/2}$ kế tiếp, một nửa số hạt nhân còn lại sẽ tiếp tục phân rã. Số hạt nhân còn lại sau các chu kỳ bán rã liên tiếp lần lượt là $N_0/2$, $N_0/4$, $N_0/8$, và cứ tiếp tục như vậy.

Thiết lập tỉ số $N(t)/N_0 = 1/2$ tại thời điểm $t = T_{1/2}$ trong phương trình suy giảm hàm mũ, ta thu được:

$$
\frac{1}{2} = e^{-\lambda T_{1/2}}
$$

Lấy logarit tự nhiên hai vế và giải ra chu kỳ bán rã:

$$
T_{1/2} = \frac{\ln 2}{\lambda} = \frac{0{,}693}{\lambda} \tag{43.18}
$$

Thời gian sống trung bình $T_{\text{mean}}$, thường gọi ngắn gọn là thời gian sống (lifetime), của một hạt nhân hay một hạt không bền là khoảng thời gian để số hạt nhân giảm đi $e$ lần, tức giảm còn $1/e$ giá trị ban đầu. Đại lượng này tỉ lệ thuận với chu kỳ bán rã:

$$
T_{\text{mean}} = \frac{1}{\lambda} = \frac{T_{1/2}}{\ln 2} \tag{43.19}
$$

Với $\ln 2 \approx 0{,}693$, ta có biểu thức tính gần đúng:

$$
T_{\text{mean}} \approx \frac{T_{1/2}}{0{,}693}
$$

Trong vật lý hạt cơ bản, tuổi thọ của một hạt không bền thường được mô tả thông qua thời gian sống trung bình thay vì chu kỳ bán rã.

Do hoạt độ $-dN(t)/dt$ tại mọi thời điểm bằng $\lambda N(t)$, hoạt độ cũng biến thiên theo hàm số thời gian dưới dạng $e^{-\lambda t}$. Sau mỗi chu kỳ bán rã, hoạt độ của mẫu giảm còn một nửa, một phần tư, một phần tám so với hoạt độ ban đầu.

::: info Lưu ý: Một chu kỳ bán rã chưa thể đảm bảo mức an toàn
Đôi khi xuất hiện quan niệm chưa chính xác cho rằng mọi mẫu phóng xạ đều trở nên an toàn sau khi trải qua một chu kỳ bán rã. Nếu một lượng chất thải phóng xạ ban đầu có hoạt độ cao gấp 10 lần ngưỡng an toàn cho phép, sau một chu kỳ bán rã hoạt độ giảm một nửa nhưng vẫn còn vượt ngưỡng an toàn tới 5 lần. Thậm chí sau ba chu kỳ bán rã, mẫu vẫn còn $12{,}5\%$ lượng phóng xạ ban đầu, tức vẫn cao hơn ngưỡng an toàn $25\%$. Số hạt nhân phóng xạ và hoạt độ chỉ tiến dần về 0 khi thời gian tiến ra vô hạn.
:::

Một đơn vị phổ biến thường dùng để đo hoạt độ là curie, ký hiệu là $\mathrm{Ci}$, được định nghĩa bằng đúng $3{,}70 \times 10^{10}\text{ phân rã/giây}$. Giá trị này xấp xỉ bằng hoạt độ của một gam đồng vị radium-226. Trong hệ đơn vị quốc tế SI, đơn vị của hoạt độ là becquerel, ký hiệu là $\mathrm{Bq}$. Một becquerel tương ứng với một phân rã trên mỗi giây:

$$
1\text{ Bq} = 1\text{ phân rã/s}
$$

Mối liên hệ giữa hai đơn vị đo:

$$
1\text{ Ci} = 3{,}70 \times 10^{10}\text{ Bq}
$$

### Ví dụ 43.8: Hoạt độ của đồng vị cobalt-57

Đồng vị $^{57}\text{Co}$ phân rã bằng cơ chế bắt electron thành đồng vị $^{57}\text{Fe}$ với chu kỳ bán rã là $272\text{ ngày}$. Hạt nhân $^{57}\text{Fe}$ được tạo ra ở trạng thái kích thích, và gần như tức thời phát ra tia gamma mà đầu dò có thể phát hiện được.

a) Tìm thời gian sống trung bình và hằng số phân rã của $^{57}\text{Co}$.

b) Nếu hoạt độ của nguồn phát bức xạ $^{57}\text{Co}$ hiện tại là $2{,}00\text{ }\mu\text{Ci}$, nguồn này chứa bao nhiêu hạt nhân $^{57}\text{Co}$?

c) Hoạt độ của nguồn sau 1 năm là bao nhiêu?

#### Bài giải

**Xác định và Thiết lập**: Bài toán sử dụng mối liên hệ giữa hằng số phân rã $\lambda$, thời gian sống trung bình $T_{\text{mean}}$, chu kỳ bán rã $T_{1/2}$, và hoạt độ $-dN(t)/dt$. Trong phần (a), ta đổi chu kỳ bán rã sang giây rồi tính $\lambda$ và $T_{\text{mean}}$. Trong phần (b), số hạt nhân $N(t)$ được tính từ hoạt độ qua hệ thức hoạt độ tức thời. Trong phần (c), số hạt nhân còn lại và hoạt độ sau thời gian 1 năm được xác định qua định luật phân rã hàm mũ.

**Thực hiện**:

A) Đổi chu kỳ bán rã từ đơn vị ngày sang đơn vị giây:

$$
T_{1/2} = (272)(86400\text{ s})
$$

Kết quả tính toán:

$$
T_{1/2} = 2{,}35 \times 10^7\text{ s}
$$

Thời gian sống trung bình và hằng số phân rã được xác định qua chu kỳ bán rã:

$$
T_{\text{mean}} = \frac{T_{1/2}}{\ln 2}
$$

Thay số với $T_{1/2} = 2{,}35008 \times 10^7\text{ s}$:

$$
T_{\text{mean}} = 3{,}39 \times 10^7\text{ s}
$$

Đổi ra đơn vị ngày:

$$
T_{\text{mean}} = 392\text{ ngày}
$$

Hằng số phân rã là nghịch đảo của thời gian sống trung bình:

$$
\lambda = \frac{1}{T_{\text{mean}}}
$$

Thay giá trị thời gian sống trung bình thu được:

$$
\lambda = 2{,}95 \times 10^{-8}\text{ s}^{-1}
$$

b) Hoạt độ đã cho của nguồn là $2{,}00\text{ }\mu\text{Ci}$, đổi sang đơn vị phân rã trên giây:

$$
-\frac{dN(t)}{dt} = 2{,}00\text{ }\mu\text{Ci}
$$

Quy đổi về đơn vị becquerel:

$$
-\frac{dN(t)}{dt} = 7{,}40 \times 10^4\text{ Bq}
$$

Vì hoạt độ liên hệ với số hạt nhân qua phương trình $-dN(t)/dt = \lambda N(t)$, số hạt nhân hiện có trong nguồn là:

$$
N(t) = \frac{-dN(t)/dt}{\lambda}
$$

Thay số với hoạt độ và hằng số phân rã đã biết, ta thu được:

$$
N(t) = 2{,}51 \times 10^{12}
$$

Như vậy nguồn chứa $2{,}51 \times 10^{12}$ hạt nhân $^{57}\text{Co}$.

c) Một năm chuẩn quy ước có $t = 3{,}156 \times 10^7\text{ s}$. Tích số mũ có giá trị $-\lambda t = -0{,}931$. Tỉ số giữa số hạt nhân còn lại tại thời điểm $t = 1\text{ năm}$ và số hạt nhân ban đầu là:

$$
\frac{N(t)}{N_0} = e^{-\lambda t}
$$

Tính lũy thừa với số mũ $-\lambda t = -0{,}931$:

$$
\frac{N(t)}{N_0} = 0{,}394
$$

Số hạt nhân đã giảm còn $0{,}394$ lần giá trị ban đầu. Do hoạt độ tỉ lệ thuận với số hạt nhân, hoạt độ của nguồn sau 1 năm cũng giảm theo đúng hệ số này:

$$
A = 0{,}394 \times 2{,}00\text{ }\mu\text{Ci}
$$

Kết quả hoạt độ sau 1 năm:

$$
A = 0{,}788\text{ }\mu\text{Ci}
$$

**Đánh giá:** Số hạt nhân tìm được ở phần (b) tương đương với $4{,}17 \times 10^{-12}\text{ mol}$, ứng với khối lượng chỉ $2{,}38 \times 10^{-10}\text{ g}$. Đây là khối lượng nhỏ hơn rất nhiều so với giới hạn đo của các cân phân tích nhạy nhất. Sau một chu kỳ bán rã $272\text{ ngày}$, số hạt nhân giảm còn $N_0/2$, và sau hai chu kỳ bán rã tức $544\text{ ngày}$, số hạt nhân giảm còn $N_0/4$. Kết quả phần (c) cho thấy sau 365 ngày, số hạt nhân còn lại nằm giữa $N_0/2$ và $N_0/4$, hoàn toàn nhất quán với dự đoán định tính.

**Khái niệm quan trọng**: Vì quá trình phân rã phóng xạ là một hiện tượng thống kê, cả số hạt nhân phóng xạ $N(t)$ lẫn hoạt độ $-dN(t)/dt$ của mẫu đều suy giảm theo hàm mũ theo thời gian. Cả $N(t)$ và $-dN(t)/dt$ đều giảm đi một nửa sau mỗi chu kỳ bán rã, và giảm đi $e$ lần sau mỗi khoảng thời gian sống trung bình.

### Định tuổi bằng đồng vị phóng xạ

Một ứng dụng quan trọng của hiện tượng phóng xạ là định tuổi các mẫu khảo cổ và địa chất bằng cách đo nồng độ các đồng vị phóng xạ. Ví dụ quen thuộc nhất là phương pháp định tuổi bằng carbon phóng xạ. Đồng vị không bền $^{14}\text{C}$ được tạo ra liên tục trong khí quyển nhờ các phản ứng hạt nhân do tia vũ trụ bắn phá, tạo nên một tỉ lệ nhỏ $^{14}\text{C}$ ổn định trong lượng $\text{CO}_2$ của khí quyển. Thực vật hấp thụ carbon từ nguồn này qua quang hợp, duy trì tỉ lệ $^{14}\text{C}$ giống như trong khí quyển. Khi sinh vật chết đi, quá trình trao đổi chất ngừng lại, lượng $^{14}\text{C}$ tồn đọng phân rã $\beta^-$ thành $^{14}\text{N}$ với chu kỳ bán rã $5730\text{ năm}$. Bằng cách đo tỉ lệ $^{14}\text{C}$ còn lại trong di tích sinh vật, ta có thể xác định sinh vật đó đã chết cách đây bao lâu.

Một khó khăn của phương pháp định tuổi bằng carbon là nồng độ $^{14}\text{C}$ trong khí quyển có biến động nhỏ qua các thời kỳ địa chất dài. Việc hiệu chỉnh được thực hiện dựa trên các dữ liệu độc lập khác, chẳng hạn như số đo vòng sinh trưởng hàng năm của thân cây cổ thụ. Các kỹ thuật phóng xạ tương tự cũng được áp dụng với các đồng vị khác để định tuổi mẫu địa chất. Một số loại đá chứa đồng vị phóng xạ potassium $^{40}\text{K}$, có chu kỳ bán rã tổng cộng $1{,}248 \times 10^9\text{ năm}$. Trong đó, một nhánh phân rã (bắt electron và phân rã $\beta^+$ với tỉ lệ khoảng $10{,}7\%$) biến đổi $^{40}\text{K}$ thành đồng vị khí argon bền $^{40}\text{Ar}$. Trong khi đó, nhánh phân rã $\beta^-$ chính tạo thành $^{40}\text{Ca}$. Tuổi của mẫu đá địa chất được xác định bằng phương pháp định tuổi kali - agon thông qua việc đo tỉ số giữa nồng độ $^{40}\text{Ar}$ tích tụ trong cấu trúc tinh thể đá và lượng $^{40}\text{K}$ còn lại.

### Ví dụ 43.9: Định tuổi bằng carbon phóng xạ

Trước năm 1900, hoạt độ trên mỗi đơn vị khối lượng của carbon trong khí quyển do sự hiện diện của $^{14}\text{C}$ đạt giá trị trung bình khoảng $0{,}255\text{ Bq}$ trên mỗi gam carbon.

a) Tỉ lệ phần trăm số nguyên tử carbon là đồng vị $^{14}\text{C}$ trong khí quyển trước năm 1900 là bao nhiêu?

b) Khi phân tích một mẫu khảo cổ chứa $500\text{ mg}$ carbon, người ta ghi nhận được 174 phân rã trong thời gian 1 giờ. Giả sử hoạt độ trên mỗi gam carbon lúc sinh vật chết bằng giá trị trung bình của khí quyển nói trên, tuổi của mẫu vật là bao nhiêu?

#### Bài giải

**Xác định và Thiết lập**: Ý tưởng quan trọng là hoạt độ hiện tại của một mẫu sinh học chứa $^{14}\text{C}$ liên hệ trực tiếp với khoảng thời gian đã trôi qua kể từ khi sinh vật ngừng hấp thụ carbon từ khí quyển và hoạt độ ban đầu tại thời điểm đó. Trong phần (a), ta tìm số hạt nhân $^{14}\text{C}$ từ hoạt độ riêng của 1 gam carbon bằng hằng số phân rã $\lambda$, rồi so sánh với tổng số nguyên tử carbon trong 1 gam dựa vào khối lượng mol trung bình của carbon ($12{,}011\text{ g/mol}$). Trong phần (b), ta tính hoạt độ ban đầu của 500 mg carbon, xác định tỉ số hoạt độ hiện tại so với ban đầu, rồi giải phương trình suy giảm hàm mũ để tìm thời gian $t$.

**Thực hiện**:

A) Đổi chu kỳ bán rã $T_{1/2} = 5730\text{ năm}$ sang đơn vị giây, với $1\text{ năm} = 3{,}156 \times 10^7\text{ s}$:

$$
T_{1/2} = 1{,}808 \times 10^{11}\text{ s}
$$

Hằng số phân rã của đồng vị carbon-14 là:

$$
\lambda = \frac{\ln 2}{T_{1/2}}
$$

Thay giá trị chu kỳ bán rã bằng giây:

$$
\lambda = 3{,}83 \times 10^{-12}\text{ s}^{-1}
$$

Số hạt nhân $^{14}\text{C}$ có trong 1 gam carbon được xác định từ hoạt độ $0{,}255\text{ Bq} = 0{,}255\text{ s}^{-1}$:

$$
N(t) = \frac{-dN/dt}{\lambda}
$$

Thực hiện phép tính, số hạt nhân $^{14}\text{C}$ có trong 1 gam là:

$$
N(t) = 6{,}65 \times 10^{10}
$$

Tổng số nguyên tử carbon trong 1 gam (ứng với $1/12{,}011\text{ mol}$) là:

$$
N_{\text{tổng}} = \frac{N_{\mathrm{A}}}{12{,}011}
$$

Thay hằng số Avogadro $N_{\mathrm{A}} = 6{,}022 \times 10^{23}\text{ mol}^{-1}$, ta thu được:

$$
N_{\text{tổng}} = 5{,}01 \times 10^{22}
$$

Tỉ số giữa số nguyên tử $^{14}\text{C}$ và tổng số nguyên tử carbon là:

$$
\frac{N(^{14}\text{C})}{N_{\text{tổng}}} = \frac{6{,}65 \times 10^{10}}{5{,}01 \times 10^{22}}
$$

Tỉ số thu được:

$$
\frac{N(^{14}\text{C})}{N_{\text{tổng}}} = 1{,}33 \times 10^{-12}
$$

Chỉ có khoảng 4 nguyên tử carbon-14 trong mỗi $3 \times 10^{12}$ nguyên tử carbon.

b) Hoạt độ trên mỗi gam carbon tại thời điểm sinh vật chết ($t = 0$) là $a_0 = 0{,}255\text{ Bq/g}$. Đổi ra đơn vị phân rã trên giờ với $3600\text{ s/h}$:

$$
a_0 = 918\text{ h}^{-1}\cdot\text{g}^{-1}
$$

Hoạt độ ban đầu của lượng $m = 0{,}500\text{ g}$ carbon trong mẫu là:

$$
A_0 = m a_0
$$

Thay số tính toán:

$$
A_0 = 459\text{ h}^{-1}
$$

Hoạt độ quan sát được hiện tại là $A(t) = 174\text{ h}^{-1}$. Vì hoạt độ tỉ lệ thuận với số hạt nhân phóng xạ, tỉ số hoạt độ bằng đúng tỉ số số lượng hạt nhân:

$$
\frac{N(t)}{N_0} = \frac{174}{459}
$$

Giá trị tỉ số:

$$
\frac{N(t)}{N_0} = 0{,}379
$$

Giải phương trình $N(t) = N_0 e^{-\lambda t}$ để tìm tuổi $t$ của mẫu vật:

$$
t = -\frac{\ln(N(t)/N_0)}{\lambda}
$$

Thay số với $\ln(0{,}379) = -0{,}9702$:

$$
t = 2{,}53 \times 10^{11}\text{ s}
$$

Đổi thời gian từ đơn vị giây sang đơn vị năm:

$$
t = 8020\text{ năm}
$$

**Đánh giá:** Sau $8020\text{ năm}$, hoạt độ của $^{14}\text{C}$ đã giảm từ 459 xuống còn 174 phân rã mỗi giờ. Sinh vật này đã chết và ngừng trao đổi khí $\text{CO}_2$ với khí quyển cách đây khoảng $8000\text{ năm}$.

**Khái niệm quan trọng**: Để định tuổi một mẫu vật bằng phương pháp phóng xạ, người ta đo hoạt độ hiện tại của mẫu và xác định hoạt độ của mẫu đó tại thời điểm hình thành. Tuổi của mẫu tỉ lệ thuận với logarit tự nhiên của tỉ số giữa hai hoạt độ này.

### Nguy cơ bức xạ trong nhà ở

Một mối nguy hiểm cho sức khỏe tại một số khu vực dân cư là sự tích tụ khí radon $^{222}\text{Rn}$ trong các ngôi nhà. Đây là một chất khí phóng xạ trơ, không màu, không mùi. Chu kỳ bán rã của $^{222}\text{Rn}$ trong chuỗi phân rã của $^{238}\text{U}$ chỉ là $3{,}82\text{ ngày}$. Mặc dù chu kỳ bán rã ngắn, khí radon không tự biến mất hoàn toàn khỏi ngôi nhà vì nó liên tục được sinh ra từ sự phân rã của $^{226}\text{Ra}$, một nguyên tố hiện diện với lượng vết trong đất đá nền nhà. Đây là một trạng thái cân bằng động, trong đó tốc độ sinh ra bằng đúng tốc độ phân rã.

Lý do khiến $^{222}\text{Rn}$ gây nguy hiểm lớn hơn các đồng vị khác trong chuỗi phân rã là vì nó tồn tại ở thể khí. Trong suốt chu kỳ bán rã $3{,}82\text{ ngày}$, khí radon có thể khuếch tán từ lòng đất xâm nhập vào nhà ở. Khi một hạt nhân $^{222}\text{Rn}$ phân rã trong phổi, nó phát ra một hạt $\alpha$ gây tổn thương tế bào và tạo thành hạt nhân con polonium $^{218}\text{Po}$. Hạt nhân con này là một chất rắn hoạt động hóa học, có xu hướng bám lại trên mô phổi cho đến khi tiếp tục phân rã, giải phóng thêm các hạt $\alpha$ tiếp theo trong chuỗi phân rã $^{238}\text{U}$.

Để so sánh hoạt độ thể tích với tác động lâu dài, xét bộ ước lượng phơi nhiễm radon sau. Mặc dù có những khu vực ghi nhận mức cá biệt lên tới $3500\text{ pCi/L}$, giá trị hoạt độ thể tích trung bình dùng trong phép so sánh của $^{222}\text{Rn}$ trong không khí nhà ở tại Mỹ vào khoảng $1{,}5\text{ pCi/L}$ (tương đương hơn một nghìn phân rã mỗi giây trong một căn phòng có kích thước trung bình). Phơi nhiễm liên tục suốt đời ở mức độ này được ước tính có thể làm giảm tuổi thọ khoảng 40 ngày. Để so sánh đối chứng: Hút một bao thuốc lá mỗi ngày làm giảm tuổi thọ khoảng 6 năm. Trong khi đó, lượng phát thải trung bình từ tất cả các nhà máy điện hạt nhân trên toàn cầu ước tính làm giảm tuổi thọ trong khoảng từ $0{,}01$ đến 5 ngày (đã tính cả những thảm họa lớn như Chernobyl năm 1986 và Fukushima năm 2011).

### Kiểm tra hiểu biết 43.4

Mẫu nào sau đây chứa số lượng hạt nhân lớn hơn: Mẫu $^{240}\text{Pu}$ có hoạt độ $5{,}00\text{ }\mu\text{Ci}$ (chu kỳ bán rã $6560\text{ năm}$) hay mẫu $^{243}\text{Am}$ có hoạt độ $4{,}45\text{ }\mu\text{Ci}$ (chu kỳ bán rã $7370\text{ năm}$)?

(i) Mẫu $^{240}\text{Pu}$.

(ii) Mẫu $^{243}\text{Am}$.

(iii) Cả hai mẫu đều chứa số lượng hạt nhân bằng nhau.

::: details Giải thích
**Đáp án đúng**: (iii).

Hoạt độ $-dN(t)/dt$ của một mẫu phóng xạ là tích của số hạt nhân $N(t)$ và hằng số phân rã $\lambda = (\ln 2)/T_{1/2}$. Do đó, số hạt nhân có trong mẫu là:

$$
N(t) = \frac{-dN(t)/dt}{\ln 2} T_{1/2}
$$

Lập tỉ số giữa số hạt nhân của $^{240}\text{Pu}$ và $^{243}\text{Am}$, thừa số $\ln 2$ bị triệt tiêu:

$$
\frac{N_{\text{Pu}}}{N_{\text{Am}}} = \frac{A_{\text{Pu}} T_{1/2,\text{Pu}}}{A_{\text{Am}} T_{1/2,\text{Am}}}
$$

Thay các giá trị hoạt độ và chu kỳ bán rã vào tỉ số:

$$
\frac{N_{\text{Pu}}}{N_{\text{Am}}} = \frac{(5{,}00)(6560)}{(4{,}45)(7370)}
$$

Tích ở tử số là $5{,}00 \times 6560 = 32800$, tích ở mẫu số là $4{,}45 \times 7370 = 32796{,}5$. Tỉ số thu được trong phạm vi độ chính xác ba chữ số có nghĩa đã cho là:

$$
\frac{N_{\text{Pu}}}{N_{\text{Am}}} = 1{,}00
$$

Hai mẫu chứa số lượng hạt nhân bằng nhau trong phạm vi độ chính xác đã cho ($1{,}00$). Vì đồng vị $^{243}\text{Am}$ có chu kỳ bán rã dài hơn nên tốc độ phân rã chậm hơn. Điều này dẫn đến hoạt độ đo được nhỏ hơn so với mẫu $^{240}\text{Pu}$.
:::
