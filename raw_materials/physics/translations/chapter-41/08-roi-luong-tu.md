## 41.8 Vướng lượng tử

Sau cấu trúc nguyên tử và quang phổ, ta xét hàm sóng của một hệ gồm hai hạt đồng nhất, chẳng hạn hai electron trong heli. Các chỉ số 1 và 2 đánh dấu hai biến tọa độ trong biểu diễn hàm sóng. Chúng không phải những dấu hiệu vật lý dùng để nhận diện từng electron.

Hàm sóng mô tả trạng thái của cả hai hạt phụ thuộc đồng thời vào tọa độ $(x_1, y_1, z_1)$ của hạt 1 và tọa độ $(x_2, y_2, z_2)$ của hạt 2. Ta dùng các vector vị trí $\vec{r}_1 = x_1\hat{i} + y_1\hat{j} + z_1\hat{k}$ và $\vec{r}_2 = x_2\hat{i} + y_2\hat{j} + z_2\hat{k}$ để biểu diễn không gian. Tương tự như trường hợp một hạt, nếu hệ hai hạt có tổng năng lượng $E$ xác định, hàm sóng phụ thuộc thời gian toàn phần $\Psi \equiv \Psi(\vec{r}_1, \vec{r}_2, t)$ có thể tách thành tích của hàm sóng không gian không phụ thuộc thời gian $\psi(\vec{r}_1, \vec{r}_2)$ và một thừa số thời gian:

$$
\Psi = \psi(\vec{r}_1, \vec{r}_2) e^{-iEt/\hbar} \tag{41.49}
$$

Phương pháp tách biến cho phép ta thử biểu diễn hàm sóng không gian $\psi(\vec{r}_1, \vec{r}_2)$ dưới dạng tích của một hàm sóng mô tả hạt 1 và một hàm sóng mô tả hạt 2. Giả sử hạt 1 ở trạng thái $A$ có hàm sóng đơn hạt $\psi_A$, và hạt 2 ở trạng thái $B$ có hàm sóng đơn hạt $\psi_B$. Trong nguyên tử heli, một electron có thể ở trạng thái spin hướng lên ($n = 1$, $l = 0$, $m_l = 0$, $m_s = +1/2$) và electron kia ở trạng thái spin hướng xuống ($n = 1$, $l = 0$, $m_l = 0$, $m_s = -1/2$). Phỏng đoán ban đầu theo phương pháp tách biến có dạng:

$$
\psi(\vec{r}_1, \vec{r}_2) = \psi_A(\vec{r}_1)\psi_B(\vec{r}_2) \tag{41.50}
$$

Tuy nhiên, phương trình (41.50) không thể đúng về mặt vật lý vì hai hạt 1 và 2 là các hạt đồng nhất và hoàn toàn không thể phân biệt được. Ta có thể khẳng định chắc chắn rằng trong hệ có một hạt ở trạng thái $A$ và một hạt ở trạng thái $B$, nhưng về nguyên tắc ta hoàn toàn không thể chỉ ra hạt nào đang ở trạng thái nào (ta không có bất kỳ cách nào để "đánh dấu" từng hạt).

Để phản ánh tính không phân biệt được, ta tổ hợp hai số hạng dạng phương trình (41.50). Số hạng thứ nhất gán trạng thái $A$ cho tọa độ 1 và $B$ cho tọa độ 2. Số hạng thứ hai hoán đổi hai cách gán ấy.

Khi trạng thái $A,B$ phân biệt cả spin, các hàm đơn hạt còn chứa thừa số spin được lược khỏi ký hiệu. Quy tắc hoán đổi dưới đây áp dụng cho trạng thái đầy đủ, gồm cả không gian và spin. Phần không gian riêng của hai electron có thể đối xứng nếu phần spin phản đối xứng.

Đặt $\psi_{AB} \equiv \psi_A(\vec{r}_1)\psi_B(\vec{r}_2)$ và $\psi_{BA} \equiv \psi_B(\vec{r}_1)\psi_A(\vec{r}_2)$. Hàm sóng hai hạt được xét có dạng:

$$
\psi(\vec{r}_1, \vec{r}_2) = \frac{\psi_{AB} \pm \psi_{BA}}{\sqrt{2}} \tag{41.51}
$$

Hệ số $1/\sqrt{2}$ trong phương trình (41.51) đảm bảo rằng nếu $\psi_A$ và $\psi_B$ đã được chuẩn hóa và trực giao với nhau, hàm sóng toàn phần $\psi(\vec{r}_1, \vec{r}_2)$ cũng sẽ được chuẩn hóa. Hai số hạng $\psi_{AB}$ và $\psi_{BA}$ xuất hiện với độ lớn bằng nhau, thể hiện rằng hai khả năng (hạt 1 ở $A$, hạt 2 ở $B$ hoặc hạt 1 ở $B$, hạt 2 ở $A$) có xác suất hoàn toàn ngang nhau.

Làm thế nào để xác định dấu $\pm$ trong phương trình (41.51) là dấu cộng hay dấu trừ? Nếu hai hạt là hai electron, hoặc hai hạt bất kỳ có spin bán nguyên $1/2$, nguyên lý loại trừ Pauli đòi hỏi ta bắt buộc phải chọn dấu trừ:

$$
\psi(\vec{r}_1, \vec{r}_2) = \frac{\psi_{AB} - \psi_{BA}}{\sqrt{2}} \tag{41.52}
$$

Để kiểm tra điều này, giả sử ta đòi hỏi cả hai hạt cùng chiếm một trạng thái $A$. Khi đó ta thay $\psi_B$ bằng $\psi_A$ trong phương trình (41.52):

$$
\psi = \frac{\psi_{AA} - \psi_{AA}}{\sqrt{2}} = 0
$$

Hàm sóng triệt tiêu đồng nhất nói lên rằng đòi hỏi này không thể thực hiện được. Kết quả này hoàn toàn phù hợp với nguyên lý loại trừ Pauli: Không có hai electron nào, và nói chung không có hai hạt spin-1/2 đồng nhất nào, có thể cùng chiếm một trạng thái lượng tử.

### Phép đo và "tác động ma quái từ xa"

Hàm sóng trong phương trình (41.52) gợi lại cách biểu diễn sóng dừng trong hộp thế một chiều ở Mục 40.6. Sóng dừng được tổ hợp từ hai sóng chạy có biên độ bằng nhau, truyền theo hai chiều ngược nhau của trục $x$. Hai thành phần ấy gắn với động lượng dương và âm.

Đây là phép so sánh để hình dung chồng chập, không phải khẳng định rằng phổ đo động lượng của hạt bị giam chỉ gồm hai giá trị. Khi đo một đại lượng, trạng thái sau phép đo được điều kiện hóa theo kết quả thu được. Cách mô tả này thường được gọi là **sụp đổ hàm sóng** (collapse).

Hiện tượng sụp đổ hàm sóng tương tự cũng xảy ra trong hệ hai hạt của chúng ta. Giả sử ta thực hiện phép đo trên một hạt (gọi là hạt 1) và xác định được nó đang ở trạng thái $A$. Phép đo này làm hàm sóng ở phương trình (41.52) lập tức sụp đổ về trạng thái $\psi(\vec{r}_1, \vec{r}_2) = \psi_A(\vec{r}_1)\psi_B(\vec{r}_2)$. Biểu thức này mô tả hạt 1 ở trạng thái $A$, đồng thời cũng mô tả hạt 2 ở trạng thái $B$. Kéo theo đó, ngay sau phép đo, hạt 2 bắt buộc phải ở trạng thái $B$, mặc dù ta chưa hề thực hiện bất kỳ phép đo trực tiếp nào trên hạt 2. Nói cách khác, việc đo trạng thái của một hạt đã làm thay đổi trạng thái của hạt kia. Schrödinger đã mô tả tình huống đặc biệt này bằng cách gọi hai hạt là **vướng lượng tử** (entangled).

Trong nguyên tử heli có đường kính khoảng $0{,}1\,\text{nm}$, hai electron ở gần nhau và tương tác qua lực đẩy Coulomb. Sự liên hệ giữa các phép đo trên chúng vì thế có thể gợi đến tương tác trực tiếp giữa các hạt.

Tuy nhiên, điều đáng chú ý là khi thí nghiệm đo đạc tương tự được thực hiện trên một cặp hạt vướng lượng tử đã tách xa nhau trong không gian, kết quả thu được vẫn hoàn toàn giống như khi chúng ở cạnh nhau: Nếu ta đo hạt 1 thấy ở trạng thái $A$ và sau đó đo hạt 2, ta luôn thấy hạt 2 ở trạng thái $B$. Nếu ta đo hạt 1 thấy ở trạng thái $B$ và sau đó đo hạt 2, ta luôn thấy hạt 2 ở trạng thái $A$. Như vậy, việc đo trạng thái của một hạt quyết định trạng thái của hạt kia, ngay cả khi hai hạt ở xa và tương tác trực tiếp giữa chúng có thể bỏ qua (Hình 41.27). Hiện tượng này đã được kiểm chứng thực nghiệm với các hạt vướng lượng tử cách xa nhau hơn $1200\,\text{km}$! Các thí nghiệm ở khoảng cách rất lớn này được thực hiện với các photon thay vì electron. Tương tự như electron, photon cũng có spin, và các trạng thái spin hướng lên hay spin hướng xuống tương ứng với phân cực tròn trái và phân cực tròn phải. Điểm khác biệt duy nhất là photon là hạt có spin 1, không phải spin-1/2, và không tuân theo nguyên lý loại trừ Pauli. Hàm sóng toàn phần của hai photon phải đối xứng dưới phép hoán đổi. Trong cách ghép hai trạng thái đơn hạt đầy đủ như phương trình (41.51), ta dùng tổ hợp dấu cộng. Điều này không có nghĩa mọi trạng thái phân cực rối của hai photon đều phải có cùng một dạng.

![Hình 41.27: Với trạng thái hai hạt và cùng cơ sở đo đang xét, biết kết quả trên một hạt cho phép dự đoán kết quả tương ứng trên hạt còn lại. Tương quan này vẫn được quan sát khi hai phép đo ở xa nhau.](../img/young-41/hinh-41-27.png)

Những kết quả này mâu thuẫn trực tiếp với quan niệm về tính định vị (locality), tức là ý niệm cho rằng một hạt chỉ phản ứng với các lực hoặc trường tác dụng tại chính vị trí của nó, chứ không phải tại một điểm khác trong không gian. Ta đã sử dụng tính định vị khi biểu diễn trọng lực tác dụng lên hạt có khối lượng $m$ là $\vec{F}_g = m\vec{g}$, trong đó $\vec{g}$ là gia tốc trọng trường tại chính điểm đặt hạt. Ta cũng áp dụng tính định vị khi viết lực điện $\vec{F}_E = q\vec{E}$ và lực từ $\vec{F}_B = q\vec{v}\times\vec{B}$ tác dụng lên hạt mang điện $q$ chuyển động với vận tốc $\vec{v}$, trong đó $\vec{E}$ và $\vec{B}$ lần lượt là điện trường và từ trường tại đúng vị trí của hạt. Thế nhưng, tương tác giữa hai hạt vướng lượng tử ở cách xa nhau dường như không tuân theo tính định vị. Vì lý do này, Albert Einstein đã gọi kết quả của các thí nghiệm như ở Hình 41.27 là "tác động ma quái từ xa" (spooky action at a distance). Dù có vẻ kỳ lạ, cơ học lượng tử dường như có bản chất phi định vị nội tại.

Điều làm cho những kết quả này trở nên ấn tượng hơn nữa là dù hai hạt vướng lượng tử cách xa nhau bao nhiêu, dường như có độ trễ bằng không giữa thời điểm ta thực hiện phép đo trên một hạt và thời điểm trạng thái của hạt kia thay đổi theo. Thoạt nhìn, điều này dường như vi phạm một luận điểm nền tảng của thuyết tương đối hẹp: Không có tín hiệu thuộc bất kỳ dạng nào (sóng vô tuyến, xung ánh sáng, hay chùm hạt) có thể truyền nhanh hơn tốc độ ánh sáng trong chân không $c$. Nếu việc đo trạng thái của hạt 1 ở Hình 41.27 khiến trạng thái của hạt 2 thay đổi tức thời, liệu ta có thể chế tạo một "đài phát thanh lượng tử" (quantum radio) để truyền tín hiệu nhanh hơn tốc độ ánh sáng, với hạt 1 đóng vai trò máy phát và hạt 2 là máy thu?

Câu trả lời là **không**. "Thông điệp" trong đài phát thanh lượng tử của ta sẽ là kết quả đo hạt 1 do một nhà vật lý (hãy gọi là Primo) thực hiện tại vị trí của hạt đó. Phép đo của Primo làm sụp đổ hàm sóng của hai hạt, và kết quả thu được là hạt 1 ở trạng thái $A$ hoặc trạng thái $B$. Một nhà vật lý khác (hãy gọi là Secondo) tại vị trí của hạt 2 sẽ đo thấy hạt 2 ở trạng thái $B$ nếu Primo đo được hạt 1 ở trạng thái $A$, và thấy hạt 2 ở trạng thái $A$ nếu Primo đo được hạt 1 ở trạng thái $B$. Tuy nhiên, Secondo hoàn toàn không có cách nào biết được kết quả của mình là do Primo đã đo trước, hay do chính Secondo tự thực hiện phép đo độc lập trên hạt 2 mà Primo chưa hề đo. Secondo chỉ có thể xác định được điều này về sau, chẳng hạn bằng cách gửi tin nhắn trao đổi qua lại với Primo. Phương thức liên lạc đối chiếu đó sử dụng các tín hiệu truyền đi với tốc độ ánh sáng chứ không thể tức thời. Do đó, đài phát thanh lượng tử của ta không thể truyền bất kỳ thông tin nào và hoàn toàn không cho phép liên lạc với tốc độ nhanh hơn tốc độ ánh sáng $c$.

### Máy tính lượng tử

Một ứng dụng thực tiễn của hiện tượng vướng lượng tử là máy tính lượng tử. Trong một máy tính thông thường (cổ điển), bộ nhớ được cấu thành từ các bit. Mỗi bit chỉ có hai giá trị có thể (chẳng hạn 0 hoặc 1), do đó một bộ nhớ máy tính gồm $N$ bit có thể có bất kỳ cấu hình nào trong số $2^N$ cấu hình khác nhau. Tình huống này tương tự như các đồng xu có thể nằm ngửa hoặc sấp, ví dụ 4 đồng xu có thể có $2^4 = 16$ khả năng.

Trong máy tính lượng tử, các bit cổ điển được thay thế bằng các qubit (viết tắt của "quantum bit"). Một ví dụ về qubit là một electron có spin-1/2: Nó có thể ở trạng thái spin hướng lên ($m_s = +1/2$), trạng thái spin hướng xuống ($m_s = -1/2$), hoặc ở một tổ hợp chồng chập bất kỳ của các trạng thái này:

$$
|\psi\rangle = c_0 |0\rangle + c_1 |1\rangle
$$

trong đó $c_0$ và $c_1$ là các hệ số phức thỏa mãn điều kiện chuẩn hóa $|c_0|^2 + |c_1|^2 = 1$.

Hệ $N$ qubit có $2^N$ cấu hình cơ sở. Một trạng thái thuần có thể là tổ hợp chồng chập của các cấu hình ấy, và có thể là trạng thái rối. Tương tự bốn đồng xu có 16 cấu hình, bốn qubit có 16 trạng thái cơ sở, nhưng còn có các tổ hợp biên độ phức giữa chúng.

Khả năng điều khiển biên độ và giao thoa mở ra những cách thực hiện một số phép tính, chẳng hạn các bài toán liên quan đến mật mã. Một phép đo không trả lại đồng thời mọi cấu hình hay mọi biên độ. Phát triển máy tính lượng tử là hướng ứng dụng của những đặc tính này.

### Câu tự kiểm tra 41.8

Hạt 1 là một electron có thể ở trạng thái $C$ hoặc $D$. Hạt 2 là một proton có thể ở trạng thái $E$ hoặc $F$. Xét hàm sóng sau của hệ hai hạt này:

$$
\psi = \frac{\psi_{CE} + \psi_{CF}}{\sqrt{2}}
$$

Giả sử các trạng thái đơn hạt đã chuẩn hóa và hai trạng thái $E,F$ trực giao. Dùng ký hiệu $\psi_{CE} \equiv \psi_C(\vec{r}_1)\psi_E(\vec{r}_2)$ và $\psi_{CF} \equiv \psi_C(\vec{r}_1)\psi_F(\vec{r}_2)$.

(a) Hàm sóng này có phải là một hàm sóng hợp lệ mô tả hệ hai hạt này không?

(b) Nếu có, trạng thái này có phải là một trạng thái vướng lượng tử không?

::: details Lời giải chi tiết
**Đáp án:** Phần (a) có. Phần (b) không.

**Lập luận chi tiết**:
- **Ý (a)**: Electron và proton là hai loại hạt phân biệt được, nên không phải phản đối xứng hóa hàm sóng bằng cách hoán đổi chúng. Hai số hạng trực giao có cùng hệ số $1/\sqrt2$, vì thế tổng xác suất bằng 1. Hàm sóng đã cho là một trạng thái hợp lệ.
- **Ý (b)**: Ta nhận thấy hàm sóng có thể đặt thừa số chung $\psi_C(\vec{r}_1)$ ra ngoài:

$$
\psi = \psi_C(\vec{r}_1) \phi_2(\vec{r}_2)
$$

với hàm sóng trạng thái của hạt 2 là:

$$
\phi_2(\vec{r}_2) = \frac{\psi_E(\vec{r}_2) + \psi_F(\vec{r}_2)}{\sqrt{2}}
$$

Biểu thức này cho thấy hàm sóng của hệ là một **trạng thái tích** (product state), trong đó trạng thái của electron và trạng thái của proton hoàn toàn độc lập với nhau. Nếu ta chỉ đo trạng thái của riêng electron, ta chắc chắn $100\%$ nhận được kết quả là trạng thái $C$. Phép đo tiếp theo trên proton sẽ cho kết quả là $E$ hoặc $F$ với xác suất bằng nhau ($50\%$), hoàn toàn giống như khi ta chưa từng đo trạng thái của electron trước đó. Tương tự, nếu ta đo trạng thái của proton trước, kết quả đo đó cũng không hề ảnh hưởng đến phép đo trạng thái của electron sau đó (kết quả đo electron vẫn luôn chắc chắn là $C$). Vì kết quả đo trên hai hạt là hoàn toàn độc lập, hệ hai hạt này **không ở trạng thái vướng lượng tử**.
:::
