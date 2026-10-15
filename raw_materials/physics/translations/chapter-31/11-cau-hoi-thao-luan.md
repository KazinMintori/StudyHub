## Câu hỏi thảo luận

::: exercise Q31.1
Mạng điện sinh hoạt gia đình ở phần lớn các nước Tây Âu được cung cấp ở mức điện áp hiệu dụng $240\,\mathrm V$, thay vì mức $120\,\mathrm V$ vốn là tiêu chuẩn phổ biến tại Hoa Kỳ và Canada. Hãy phân tích các ưu điểm và nhược điểm của từng hệ thống điện áp này.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** So sánh hai tiêu chuẩn điện áp mạng điện dân dụng $240\,\mathrm V$ và $120\,\mathrm V$ về mặt hiệu quả truyền tải và mức độ an toàn.

**Hướng đi:**

- **Công thức công suất**: Dùng $P = V_{\mathrm{rms}} I_{\mathrm{rms}} \cos\phi$ để khảo sát mối liên hệ giữa điện áp và cường độ dòng điện khi công suất truyền tải và hệ số công suất không đổi.
- **Định luật Joule–Lenz**: Dùng $P_{\mathrm{loss}} = I_{\mathrm{rms}}^2 R$ để đánh giá sự thay đổi hao phí tỏa nhiệt trên đường dây khi dòng điện giảm.
- **Khảo sát an toàn điện**: Nhận định về mức độ nguy hiểm đối với cơ thể người ở các cấp điện áp dân dụng.

(a) Đối với hệ thống điện áp $240\,\mathrm V$:

- Ưu điểm: Để cung cấp cùng một công suất điện $P$ với hệ số công suất $\cos\phi$ cho trước, cường độ dòng điện hiệu dụng chạy trong dây dẫn giảm đi một nửa so với hệ thống $120\,\mathrm V$:

$$
I_{\mathrm{rms}} = \frac{P}{V_{\mathrm{rms}}\cos\phi}.
$$

Hao phí tỏa nhiệt trên đường dây dẫn có điện trở $R$ tỉ lệ với bình phương cường độ dòng điện theo định luật Joule–Lenz:

$$
P_{\mathrm{loss}} = I_{\mathrm{rms}}^2 R.
$$

Với cùng công suất $P$, hệ số công suất và điện trở đường dây $R$ cố định, dòng điện giảm một nửa làm hao phí tỏa nhiệt giảm đi bốn lần ($1/4$). Điều này giúp giảm độ sụt áp trên đường dây và nâng cao hiệu suất truyền tải điện năng.

- Nhược điểm: Điện áp hiệu dụng $240\,\mathrm V$ tạo ra điện trường và nguy cơ dòng điện qua người cao hơn khi xảy ra tiếp xúc điện so với $120\,\mathrm V$. Cần lưu ý rằng cả hai mức điện áp $120\,\mathrm V$ và $240\,\mathrm V$ đều có thể gây điện giật và chấn thương nghiêm trọng.

(b) Đối với hệ thống điện áp $120\,\mathrm V$:

- Ưu điểm: Mức điện áp chạm cực đại thấp hơn so với hệ thống $240\,\mathrm V$, do đó trong cùng điều kiện tiếp xúc, cường độ dòng điện chạy qua cơ thể người sẽ nhỏ hơn. Tuy nhiên cả hai cấp điện áp đều nguy hiểm đến tính mạng.
- Nhược điểm: Để cung cấp cùng một mức công suất tiêu thụ $P$ với cùng hệ số công suất, dòng điện hiệu dụng trong đường dây lớn gấp đôi, kéo theo hao phí nhiệt trên cùng điện trở đường dây lớn gấp bốn lần.
:::

::: exercise Q31.2
Dòng điện trong đường dây xoay chiều đổi chiều $120$ lần mỗi giây, và giá trị trung bình theo thời gian của cường độ dòng điện bằng không. Hãy giải thích tại sao năng lượng điện vẫn có thể được truyền tải liên tục trong hệ thống này.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng điện xoay chiều có giá trị trung bình bằng 0 và đổi chiều liên tục. Cần giải thích cơ chế truyền tải công suất điện từ nguồn đến nơi tiêu thụ.

**Hướng đi:**

- **Công thức công suất tức thời**: Dùng $p(t) = v(t)i(t)$ để biểu diễn tốc độ truyền năng lượng tại mỗi thời điểm.
- **Công thức công suất trung bình**: Dùng $P_{\mathrm{av}} = V_{\mathrm{rms}} I_{\mathrm{rms}} \cos\phi$ để tính năng lượng trung bình truyền tải trong một chu kỳ.
- **Mô hình trường điện từ**: Dùng vector Poynting để giải thích cơ chế lan truyền năng lượng trong không gian quanh dây dẫn.

Công suất tức thời truyền tải từ nguồn đến tải được tính bằng tích của điện áp tức thời và cường độ dòng điện tức thời:

$$
p(t) = v(t) i(t).
$$

Giả sử điện áp nguồn biến thiên điều hòa $v(t) = V\cos(\omega t)$ và dòng điện trong mạch là $i(t) = I\cos(\omega t - \phi)$. Khi truyền tải công suất hữu ích đến tải (với góc lệch pha thỏa mãn $|\phi| < 90^\circ$), điện áp và dòng điện cùng dấu trong phần lớn thời gian của mỗi chu kỳ. Khi cả điện áp và dòng điện cùng mang giá trị âm, tích số của chúng vẫn mang giá trị dương:

$$
p(t) > 0.
$$

Giá trị công suất trung bình truyền tải trong một chu kỳ được xác định bởi

$$
P_{\mathrm{av}} = V_{\mathrm{rms}} I_{\mathrm{rms}} \cos\phi.
$$

Đại lượng này phụ thuộc vào tích các giá trị hiệu dụng và cosin góc lệch pha, hoàn toàn khác không dù giá trị trung bình của riêng cường độ dòng điện bằng không ($\overline{i} = 0$).

Về mặt vi mô, năng lượng điện không được truyền đi bằng sự dịch chuyển tịnh tiến một chiều của các electron tự do dọc theo toàn bộ chiều dài đường dây. Thay vào đó, nguồn điện xoay chiều thiết lập một điện từ trường biến thiên lan truyền trong không gian xung quanh dây dẫn với tốc độ gần bằng tốc độ ánh sáng. Năng lượng được truyền tải thông qua vector Poynting của trường điện từ. Các electron trong dây dẫn chỉ cần dao động qua lại quanh vị trí cân bằng dưới tác dụng của điện trường để tiếp nhận và chuyển giao năng lượng đó cho tải tiêu thụ.
:::

::: exercise Q31.3
Trong mạch điện xoay chiều, tại sao công suất tiêu thụ trung bình trên một cuộn cảm thuần hoặc một tụ điện luôn bằng không, trong khi trên điện trở thuần thì đại lượng này luôn khác không?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Giải thích vì sao công suất trung bình trên cuộn cảm thuần và tụ điện bằng không, còn trên điện trở thuần thì dương.

**Hướng đi:**

- **Công thức công suất trung bình**: Dùng $P_{\mathrm{av}} = V_{\mathrm{rms}} I_{\mathrm{rms}} \cos\phi$ để xác định công suất tiêu thụ của từng phần tử qua hệ số công suất.
- **Quan hệ pha**: Khảo sát góc lệch pha $\phi$ giữa điện áp và dòng điện trên điện trở, cuộn cảm và tụ điện.
- **Chu trình năng lượng**: Phân tích sự khác biệt giữa quá trình tích trữ, hoàn trả năng lượng từ trường hoặc điện trường và sự tỏa nhiệt Joule không thuận nghịch.

(a) Đối với điện trở thuần $R$: Điện áp tức thời và cường độ dòng điện luôn cùng pha với nhau, tương ứng với góc lệch pha $\phi = 0$. Công suất tức thời tại mọi thời điểm là

$$
p_R(t) = i^2(t) R \ge 0.
$$

Điện năng được biến đổi không thuận nghịch thành nội năng (nhiệt Joule) trong mạng tinh thể của điện trở. Do đó, công suất tiêu thụ trung bình trong một chu kỳ luôn mang giá trị dương:

$$
P_{\mathrm{av}} = I_{\mathrm{rms}}^2 R > 0.
$$

(b) Đối với cuộn cảm thuần $L$: Điện áp sớm pha $90^\circ$ ($\pi/2\,\mathrm{rad}$) so với dòng điện, tức $\phi = +\pi/2$. Hệ số công suất bằng

$$
\cos\phi = \cos\left(\frac{\pi}{2}\right) = 0.
$$

Trong một phần tư chu kỳ khi dòng điện tăng, nguồn điện cung cấp năng lượng để thiết lập từ trường trong cuộn cảm ($p > 0$). Trong một phần tư chu kỳ tiếp theo khi dòng điện giảm, từ trường suy giảm và cuộn cảm hoàn trả toàn bộ năng lượng đã tích lũy về lại cho nguồn điện ($p < 0$). Năng lượng được trao đổi qua lại tuần hoàn mà không bị tiêu tán thành nhiệt.

(c) Đối với tụ điện thuần dung $C$: Điện áp trễ pha $90^\circ$ so với dòng điện, tức $\phi = -\pi/2$. Hệ số công suất bằng

$$
\cos\phi = \cos\left(-\frac{\pi}{2}\right) = 0.
$$

Tương tự cuộn cảm, tụ điện tích lũy năng lượng dưới dạng điện trường giữa hai bản tụ khi điện áp tăng, sau đó phóng điện hoàn trả toàn bộ năng lượng về mạch khi điện áp giảm. Do đó công suất tiêu thụ trung bình trong một chu kỳ hoàn chỉnh của cả cuộn cảm thuần và tụ điện đều bằng không.
:::

::: exercise Q31.4
Hệ thức giữa dòng điện và điện tích của tụ điện được thiết lập là $i = dq/dt$. Khi điện tích trên bản bên trái của tụ điện mang dấu dương nhưng đang giảm dần theo thời gian, hệ thức $i = dq/dt$ có còn đúng không, hay phải chuyển thành $i = -dq/dt$? Hệ thức $i = dq/dt$ có còn đúng khi bản bên phải mang điện tích dương và đang tăng hoặc giảm độ lớn không? Giải thích.

![Hình 31.9: Mạch tụ điện, đồ thị và quy ước dấu dòng điện, điện tích](img/young-31/hinh-31-09.png)

:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Kiểm tra tính tổng quát và quy ước dấu của hệ thức vi phân $i = dq/dt$ trong mọi giai đoạn nạp và phóng điện của tụ điện.

**Hướng đi:**

- **Định nghĩa cường độ dòng điện**: Dùng $i = dq/dt$ theo quy ước chiều dương đi vào bản cực tích điện $q$.
- **Khảo sát dấu đạo hàm**: Xét dấu đại số của $dq/dt$ trong các quá trình nạp và phóng điện để biện minh tính đúng đắn của phương trình vi phân.

Trong việc thiết lập phương trình mạch điện, ta chọn $q(t)$ là giá trị đại số của điện tích trên bản cực bên trái của tụ điện, và chiều dương quy ước của dòng điện $i(t)$ là chiều đi vào bản cực bên trái này.

(a) Khi bản bên trái mang điện tích dương ($q > 0$) nhưng độ lớn đang giảm dần theo thời gian: Đạo hàm theo thời gian của điện tích mang giá trị âm:

$$
\frac{dq}{dt} < 0.
$$

Theo hệ thức đại số $i = dq/dt$, cường độ dòng điện sẽ nhận giá trị âm ($i < 0$). Giá trị âm này thể hiện rằng dòng điện thực tế có chiều ngược với chiều dương quy ước, tức là điện tích dương đang dịch chuyển ra khỏi bản bên trái (chạy theo chiều kim đồng hồ quanh mạch). Do đó, hệ thức $i = dq/dt$ vẫn hoàn toàn đúng về mặt giải tích, ta không được đổi dấu thành $i = -dq/dt$.

(b) Khi bản cực bên phải mang điện tích dương:

Theo định luật bảo toàn điện tích, điện tích trên bản bên trái lúc này nhận giá trị âm ($q < 0$).

- Nếu độ lớn điện tích bản bên phải đang tăng: Độ lớn phần điện tích âm trên bản bên trái tăng lên, đồng nghĩa với giá trị đại số $q(t)$ càng âm hơn, dẫn đến $dq/dt < 0$. Khi đó hệ thức cho $i < 0$, tương ứng dòng điện thực tế tiếp tục đi ra khỏi bản bên trái để nạp thêm điện tích dương vào bản bên phải.
- Nếu độ lớn điện tích bản bên phải đang giảm: Giá trị đại số $q(t)$ của bản bên trái tăng dần từ giá trị âm trở về không, dẫn đến $dq/dt > 0$. Hệ thức tự động cho $i > 0$, tương ứng dòng điện thực tế chạy vào bản bên trái để trung hòa điện tích âm.

Hệ thức $i = dq/dt$ là một phương trình vi phân đại số liên tục. Dấu của dòng điện tự động phản ánh đúng chiều dịch chuyển vật lý của điện tích thông qua dấu của đạo hàm $dq/dt$ trong mọi trạng thái của mạch.
:::

::: exercise Q31.5
Đèn huỳnh quang thường sử dụng một cuộn cảm, gọi là chấn lưu (ballast), để giới hạn cường độ dòng điện chạy qua ống đèn. Tại sao việc sử dụng cuộn cảm lại phù hợp hơn so với việc dùng một điện trở thuần cho mục đích này?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** So sánh hiệu quả năng lượng và chức năng khởi động giữa việc dùng cuộn cảm và dùng điện trở thuần để làm chấn lưu hạn chế dòng trong đèn huỳnh quang.

**Hướng đi:**

- **Khảo sát trở kháng và cảm kháng**: So sánh cơ chế cản trở dòng điện của điện trở thuần $R$ và cảm kháng $X_L = \omega L$.
- **Định luật Joule–Lenz**: Dùng $P_{\mathrm{loss}} = I_{\mathrm{rms}}^2 R$ để đánh giá tổn hao nhiệt vô ích.
- **Định luật cảm ứng điện từ Faraday**: Dùng $\mathcal E_L = -L di/dt$ để giải thích sự tạo thành xung điện áp cao mồi hồ quang.

(a) Về mặt tiết kiệm năng lượng:

Khi ống đèn huỳnh quang đã mồi sáng, chất khí bên trong bị ion hóa và thể hiện đặc tính điện trở vi phân âm, nghĩa là điện áp trên vùng phóng điện giảm khi dòng điện tăng trong miền vận hành này. Nếu không có linh kiện hạn dòng mắc nối tiếp, dòng điện sẽ tăng mất kiểm soát và phá hủy bóng đèn.

- Nếu sử dụng điện trở thuần $R$: Điện trở cản trở dòng điện bằng cách tiêu tán năng lượng điện thành nhiệt lượng vô ích theo định luật Joule–Lenz:

$$
P_{\mathrm{loss}} = I_{\mathrm{rms}}^2 R.
$$

Nhiệt lượng này làm nóng máng đèn, gây lãng phí một phần lớn điện năng tiêu thụ và làm giảm đáng kể hiệu suất chiếu sáng của bộ đèn.

- Nếu sử dụng cuộn cảm $L$: Cuộn cảm cản trở dòng điện xoay chiều thông qua cảm kháng:

$$
X_L = \omega L = 2\pi f L.
$$

Trong mô hình cuộn cảm lý tưởng, điện áp sớm pha $90^\circ$ so với dòng điện. Vì vậy công suất trung bình cuộn cảm hấp thụ bằng không:

$$
P_{\mathrm{av}} = 0.
$$

Cuộn cảm lý tưởng hạn dòng mà không tiêu tán năng lượng. Chấn lưu thực tế vẫn có tổn hao trên dây quấn và lõi, nhưng tránh được phần công suất nhiệt mà một điện trở hạn dòng tương đương phải tiêu thụ.

(b) Về mặt hỗ trợ đánh lửa khởi động:

Khi bắt đầu bật đèn, rơle mồi (tắc te) đóng rồi ngắt đột ngột dòng điện chạy qua cuộn cảm. Tốc độ suy giảm dòng điện $|di/dt|$ rất lớn làm cuộn cảm phát sinh một xung suất điện động tự cảm:

$$
\mathcal E_L = -L \frac{di}{dt}.
$$

Xung điện áp rất cao này đặt lên hai đầu ống huỳnh quang, kích hoạt ion hóa chất khí và phóng điện hồ quang ban đầu. Điện trở thuần không thể tạo ra xung điện áp mồi này.
:::

::: exercise Q31.6
Hệ thức hiệu điện thế tức thời giữa hai đầu một cuộn cảm thuần là $v_{ab} = L di/dt$. Bằng định luật cảm ứng Faraday, hãy giải thích tại sao điểm $a$ có điện thế cao hơn điểm $b$ khi dòng điện $i$ có chiều đi từ $a$ sang $b$ và đang tăng dần độ lớn. Khi dòng điện có chiều đi từ $a$ sang $b$ nhưng đang giảm dần độ lớn, hệ thức $v_{ab} = L di/dt$ có còn đúng không, hay phải đổi thành $v_{ab} = -L di/dt$? Khi dòng điện chạy theo chiều ngược lại và đang tăng hoặc giảm độ lớn thì sao?

![Hình 31.8: Cuộn cảm với hai đầu a, b và quan hệ pha](img/young-31/hinh-31-08.png)

:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vận dụng định luật Faraday và định luật Lenz để giải thích dấu của hiệu điện thế hai đầu cuộn cảm thuần $v_{ab} = L di/dt$ trong các trường hợp dòng điện tăng, giảm và đổi chiều.

**Hướng đi:**

- **Định luật cảm ứng Faraday và định luật Lenz**: Dùng $\mathcal E = -L di/dt$ để xác định chiều của suất điện động tự cảm chống lại sự biến thiên dòng điện.
- **Định luật Ohm cho đoạn mạch**: Thiết lập liên hệ giữa hiệu điện thế ngoài $v_{ab}$ và suất điện động tự cảm để bảo toàn tính nhất quán về dấu.

(a) Khi dòng điện $i$ chạy từ $a$ sang $b$ và đang tăng dần độ lớn ($di/dt > 0$):

Từ thông do dòng điện sinh ra trong lòng các vòng dây của cuộn cảm đang tăng lên. Theo định luật Lenz, cuộn cảm phát sinh một suất điện động tự cảm có chiều chống lại sự tăng của dòng điện ban đầu, tức là có xu hướng đẩy các hạt tải điện theo chiều từ $b$ về $a$.

Vì cuộn cảm thuần có điện trở trong bằng không ($r = 0$), hiệu điện thế toàn phần giữa hai đầu dây phải cân bằng chính xác với suất điện động tự cảm chống lại này để dòng điện tiếp tục biến thiên:

$$
v_a - v_b = v_{ab} = L \frac{di}{dt}.
$$

Vì $di/dt > 0$, ta có $v_{ab} > 0$, nghĩa là điện thế ở điểm $a$ cao hơn điện thế ở điểm $b$ ($v_a > v_b$). Nguồn điện ngoài phải cung cấp một điện thế cao hơn ở cực vào $a$ để thắng được suất điện động tự cảm cản trở.

(b) Khi dòng điện chạy từ $a$ sang $b$ nhưng đang giảm dần độ lớn ($di/dt < 0$):

Theo định luật Lenz, suất điện động tự cảm lúc này có xu hướng duy trì dòng điện cũ, tức là hỗ trợ đẩy dòng điện theo chiều từ $a$ sang $b$. Điểm $b$ sẽ đóng vai trò như cực dương của nguồn điện tự cảm, kéo theo điện thế tại $b$ cao hơn điện thế tại $a$ ($v_b > v_a \implies v_{ab} < 0$).

Hệ thức $v_{ab} = L di/dt$ vẫn hoàn toàn chính xác về mặt đại số, bởi vì khi $di/dt < 0$, giá trị của $v_{ab}$ tự động mang dấu âm. Ta không được đổi dấu công thức thành $v_{ab} = -L di/dt$.

(c) Khi dòng điện chạy theo chiều ngược lại (từ $b$ sang $a$):

Lúc này giá trị đại số của dòng điện quy ước theo chiều từ $a$ sang $b$ là $i < 0$.

- Nếu độ lớn dòng điện đang tăng: Dòng điện càng âm hơn, kéo theo $di/dt < 0$, phương trình cho $v_{ab} < 0$, tương ứng $v_b > v_a$.
- Nếu độ lớn dòng điện đang giảm: Dòng điện tăng dần từ giá trị âm về không, kéo theo $di/dt > 0$, phương trình cho $v_{ab} > 0$, tương ứng $v_a > v_b$.

Hệ thức $v_{ab} = L di/dt$ là biểu thức đại số nhất quán, tự động cho dấu chính xác của hiệu điện thế trong mọi trường hợp.
:::

::: exercise Q31.7
Hệ số công suất của một mạch xoay chiều RLC mắc nối tiếp có thể bằng không được không? Hãy lập luận và biện minh câu trả lời dựa trên các cơ sở vật lý thực tế.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Đánh giá tính khả thi về mặt vật lý của điều kiện hệ số công suất bằng không ($\cos\phi = 0$) trong mạch RLC nối tiếp.

**Hướng đi:**

- **Công thức hệ số công suất**: Dùng $\cos\phi = R/Z$ để xác định điều kiện cần để hệ số công suất triệt tiêu.
- **Khảo sát mạch lý tưởng**: Xét trường hợp $R = 0$ khi mạch lệch khỏi tần số cộng hưởng.
- **Khảo sát mạch thực tế**: Đánh giá điện trở thuần và tổn hao luôn tồn tại ở tần số hữu hạn.

Hệ số công suất của mạch xoay chiều RLC nối tiếp được xác định bởi:

$$
\cos\phi = \frac{R}{Z},
$$

$$
Z = \sqrt{R^2 + X_{\mathrm d}^2},
$$

với hiệu điện kháng $X_{\mathrm d} = X_L - X_C$.

(a) Trường hợp lý tưởng hóa $R = 0$ không cộng hưởng:

Nếu mạch gồm các linh kiện lý tưởng không có điện trở thuần ($R = 0$) và hoạt động ở tần số lệch khỏi tần số cộng hưởng ($X_L \ne X_C$):

Trở kháng toàn mạch là $Z = |X_L - X_C| > 0$. Góc lệch pha giữa điện áp và dòng điện là $\phi = +90^\circ$ (khi $X_L > X_C$) hoặc $\phi = -90^\circ$ (khi $X_C > X_L$). Khi đó:

$$
\cos\phi = \frac{R}{Z} = 0.
$$

Mạch hoàn toàn không tiêu thụ công suất tác dụng trung bình ($P_{\mathrm{av}} = 0$).

(b) Trường hợp mạch thực tế:

Trong mô hình mạch có tổn hao, điện trở tương đương $R$ là số dương. Tổn hao có thể đến từ dây quấn, lõi từ, điện môi và dây nối.

Vì $R > 0$ và trở kháng $Z = \sqrt{R^2 + (X_L - X_C)^2} > 0$ là hữu hạn, hệ số công suất luôn nhận giá trị dương:

$$
\cos\phi = \frac{R}{Z} > 0.
$$

Do đó, ở tần số hữu hạn, mạch có $R>0$ và trở kháng hữu hạn có hệ số công suất dương.
:::

::: exercise Q31.8
Trong một mạch điện xoay chiều RLC mắc nối tiếp, điện áp tức thời giữa hai đầu tụ điện có thể vượt quá điện áp tức thời của nguồn tại cùng thời điểm đó hay không? Điều này có thể xảy ra với điện áp tức thời trên cuộn cảm không? Trên điện trở thuần thì sao? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khảo sát xem điện áp tức thời trên tụ điện $v_C(t)$, trên cuộn cảm $v_L(t)$ và trên điện trở $v_R(t)$ có thể có độ lớn lớn hơn điện áp tức thời của nguồn $v(t)$ tại cùng một thời điểm hay không.

**Hướng đi:**

- **Định luật Kirchhoff về điện áp**: Dùng hệ thức tức thời $v(t) = v_R(t) + v_L(t) + v_C(t)$ tại mỗi thời điểm.
- **Quan hệ pha giữa các phần tử**: Sử dụng tính chất ngược pha của điện áp tức thời trên cuộn cảm và tụ điện.
- **Phản ví dụ số trị**: Xét trạng thái cụ thể ngoài cộng hưởng để chứng minh điện áp tức thời trên điện trở có thể vượt quá điện áp nguồn.

Theo định luật Kirchhoff, tại mỗi thời điểm tức thời $t$, tổng đại số điện áp trên từng phần tử nối tiếp luôn bằng điện áp tức thời của nguồn:

$$
v(t) &= v_R(t) + v_L(t) + v_C(t).
$$

(a) Đối với tụ điện và cuộn cảm: Điện áp tức thời trên tụ điện hoặc trên cuộn cảm hoàn toàn có thể vượt quá điện áp tức thời của nguồn.

Nguyên nhân là điện áp tức thời trên cuộn cảm $v_L(t)$ và điện áp tức thời trên tụ điện $v_C(t)$ dao động ngược pha nhau $180^\circ$ ($\pi\,\mathrm{rad}$). Đặt dòng điện trong mạch là $i(t) = I\cos(\omega t)$, ta có:

$$
v_L(t) = -V_L \sin(\omega t),
$$

$$
v_C(t) = V_C \sin(\omega t).
$$

Tổng tức thời của chúng là:

$$
v_L(t) &+ v_C(t) = (V_C - V_L)\sin(\omega t).
$$

Tại những thời điểm điện áp nguồn bằng không ($v(t) = 0$), nếu dòng điện trong mạch khác không thì các điện áp tức thời $v_L(t)$ và $v_C(t)$ vẫn khác không và có thể có độ lớn rất lớn. Khi đó $|v_L(t)| > |v(t)| = 0$ và $|v_C(t)| > |v(t)| = 0$. Đặc biệt, chỉ khi mạch ở trạng thái cộng hưởng chính xác ($X_L = X_C$), biên độ điện áp trên cuộn cảm và trên tụ điện mới bằng nhau, $V_L = V_C$. Nếu ở tần số này mà cảm kháng lớn hơn nhiều so với điện trở ($X_L = X_C \gg R$), biên độ điện áp $V_L$ và $V_C$ có thể lớn gấp nhiều lần biên độ nguồn $V$.

(b) Đối với điện trở thuần:

Về mặt giá trị tức thời: Giá trị tức thời $|v_R(t)|$ hoàn toàn có thể lớn hơn $|v(t)|$.

Xét mạch của Ví dụ 31.4 với $V_R=30\,\mathrm V$, $V_L=60\,\mathrm V$ và $V_C=20\,\mathrm V$. Chọn $i(t)=I\cos(\omega t)$. Tại thời điểm có $\omega t=0{,}6435\,\mathrm{rad}$, điện áp tức thời của nguồn đi qua giá trị $v(t) = 0\,\mathrm V$. Tại đúng thời điểm đó, các điện áp tức thời thành phần nhận giá trị, $v_R(t) = 24\,\mathrm V$, $v_L(t) = -36\,\mathrm V$ và $v_C(t) = 12\,\mathrm V$.
Tổng tức thời thỏa mãn định luật Kirchhoff:

$$
\begin{aligned}
v_R(t) + v_L(t) + v_C(t) &= 24\,\mathrm V - 36\,\mathrm V + 12\,\mathrm V \\
&= 0\,\mathrm V = v(t).
\end{aligned}
$$

Tại thời điểm này, $|v_R(t)| = 24\,\mathrm V > |v(t)| = 0\,\mathrm V$. Như vậy điện áp tức thời trên điện trở thuần hoàn toàn có thể lớn hơn điện áp tức thời của nguồn.

Tuy nhiên, nếu xét về mặt biên độ đỉnh theo thời gian, biên độ điện áp trên điện trở thuần luôn bị chặn trên bởi biên độ nguồn:

$$
V_R = I R = \frac{V R}{Z} \le V.
$$

với $Z = \sqrt{R^2 + (X_L - X_C)^2} \ge R$.

Dấu bằng chỉ xảy ra khi mạch xảy ra cộng hưởng chính xác ($X_L = X_C$), khi đó $V_R = V$.
:::

::: exercise Q31.9
Trong mạch điện xoay chiều RLC mắc nối tiếp, góc lệch pha $\phi$ và hệ số công suất $\cos\phi$ sẽ bằng bao nhiêu khi điện trở thuần nhỏ hơn rất nhiều so với cảm kháng hoặc dung kháng, và mạch đang hoạt động ở tần số cách xa tần số cộng hưởng? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xác định góc lệch pha $\phi$ và hệ số công suất $\cos\phi$ khi $R \ll |X_L - X_C|$ trong điều kiện mạch hoạt động xa cộng hưởng.

**Hướng đi:**

- **Công thức góc lệch pha**: Dùng $\tan\phi = (X_L - X_C)/R$ để khảo sát giới hạn của góc lệch pha khi $R \to 0$.
- **Công thức hệ số công suất**: Dùng $\cos\phi = R/Z$ để đánh giá tỷ lệ công suất tác dụng khi điện trở rất nhỏ so với hiệu điện kháng.
- **Phân loại chế độ mạch**: Phân biệt trường hợp mạch mang tính cảm kháng ($\omega > \omega_0$) và dung kháng ($\omega < \omega_0$).

Góc lệch pha giữa điện áp nguồn và dòng điện trong mạch RLC nối tiếp được xác định bởi:

$$
\tan\phi = \frac{X_L - X_C}{R}.
$$

Hệ số công suất tương ứng là:

$$
\cos\phi = \frac{R}{Z},
$$

$$
Z = \sqrt{R^2 + X_{\mathrm d}^2},
$$

với $X_{\mathrm d} = X_L - X_C$.

Vì mạch hoạt động ở tần số cách xa tần số cộng hưởng, hiệu số giữa cảm kháng và dung kháng $|X_L - X_C|$ có độ lớn đáng kể. Do giả thiết điện trở thuần rất nhỏ ($R \ll |X_L - X_C|$), mẫu số trong công thức tính $\tan\phi$ tiến rất gần về không. Ta xét hai trường hợp cụ thể. (a) Khi tần số nguồn cao hơn tần số cộng hưởng ($\omega > \omega_0$):

Cảm kháng chiếm ưu thế ($X_L \gg X_C$), do đó $X_L - X_C > 0$. Khi $R \to 0$, ta có:

$$
\tan\phi \to +\infty
$$

$$
\implies \phi \approx +90^\circ = +\frac{\pi}{2}\,\mathrm{rad}.
$$

Điện áp nguồn sớm pha xấp xỉ $90^\circ$ so với dòng điện trong mạch. Mạch mang tính cảm kháng vượt trội.

(b) Khi tần số nguồn thấp hơn tần số cộng hưởng ($\omega < \omega_0$):

Dung kháng chiếm ưu thế ($X_C \gg X_L$), do đó $X_L - X_C < 0$. Khi $R \to 0$, ta có:

$$
\tan\phi \to -\infty
$$

$$
\implies \phi \approx -90^\circ = -\frac{\pi}{2}\,\mathrm{rad}.
$$

Điện áp nguồn trễ pha xấp xỉ $90^\circ$ so với dòng điện trong mạch. Mạch mang tính dung kháng vượt trội.

Trong cả hai trường hợp trên, hệ số công suất đều tiệm cận về không:

$$
\cos\phi \approx \frac{R}{|X_L - X_C|} \approx 0.
$$

Mạch hầu như không tiêu thụ công suất tác dụng trung bình từ nguồn điện mà chủ yếu dao động trao đổi công suất phản kháng tích trữ giữa nguồn và các trường năng lượng.
:::

::: exercise Q31.10
Khi một mạch RLC mắc nối tiếp được cấp điện bởi nguồn xoay chiều có điện áp hiệu dụng $120\,\mathrm V$, điện áp giới hạn cho phép của tụ điện vẫn có thể bị vượt quá ngay cả khi tụ điện đó có điện áp danh định định mức lên tới $200\,\mathrm V$ hoặc $400\,\mathrm V$. Bằng cơ chế vật lý nào mà hiện tượng này có thể xảy ra?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Giải thích vì sao tụ điện chịu áp $200\,\mathrm V$ hoặc $400\,\mathrm V$ vẫn có thể bị đánh thủng khi mắc vào nguồn xoay chiều có điện áp hiệu dụng chỉ $120\,\mathrm V$.

**Hướng đi:**

- **Mối liên hệ giữa biên độ và giá trị hiệu dụng**: Dùng $V = V_{\mathrm{rms}}\sqrt{2}$ để xác định biên độ điện áp đỉnh của nguồn.
- **Hiện tượng cộng hưởng nối tiếp**: Dùng điều kiện $X_L \approx X_C$ để xác định dòng điện cực đại trong mạch.
- **Hệ số phẩm chất của mạch**: Dùng $Q = X_C/R = (1/R)\sqrt{L/C}$ để giải thích sự khuếch đại điện áp hiệu dụng trên tụ điện.

Hiện tượng này bắt nguồn từ hai yếu tố vật lý kết hợp. (a) Sự chênh lệch giữa giá trị hiệu dụng và giá trị biên độ đỉnh của nguồn: Điện áp danh định của nguồn điện dân dụng là giá trị hiệu dụng $V_{\mathrm{rms}} = 120\,\mathrm V$. Biên độ điện áp đỉnh của nguồn điện biến thiên điều hòa là:

$$
\begin{aligned}
V &= V_{\mathrm{rms}}\sqrt{2} \\
&\approx 120\times1{,}414 \approx 170\,\mathrm V.
\end{aligned}
$$

(b) Hiện tượng khuếch đại điện áp tại vùng tần số cộng hưởng:

Cường độ dòng điện hiệu dụng chạy qua mạch nối tiếp phụ thuộc vào trở kháng toàn mạch:

$$
I_{\mathrm{rms}} = \frac{V_{\mathrm{rms}}}{Z},
$$

$$
Z = \sqrt{R^2 + X_{\mathrm d}^2},
$$

với $X_{\mathrm d} = \omega L - 1/(\omega C)$.

Khi tần số của nguồn xoay chiều tiến đến gần hoặc trùng khớp với tần số góc cộng hưởng riêng của mạch:

$$
\omega \approx \omega_0 = \frac{1}{\sqrt{LC}}.
$$

Cảm kháng và dung kháng triệt tiêu lẫn nhau ($X_L \approx X_C$), trở kháng của toàn mạch giảm xuống mức tối thiểu, bằng đúng điện trở thuần, $Z \approx R$. Khi đó dòng điện trong mạch đạt giá trị cực đại:

$$
I_{\mathrm{rms,max}} = \frac{V_{\mathrm{rms}}}{R}.
$$

Điện áp hiệu dụng đặt lên hai bản tụ điện bằng:

$$
\begin{aligned}
V_{C,\mathrm{rms}} &= I_{\mathrm{rms,max}} X_C \\
&= V_{\mathrm{rms}} \frac{X_C}{R} = Q V_{\mathrm{rms}}.
\end{aligned}
$$

Trong đó đại lượng:

$$
Q = \frac{1}{R}\sqrt{\frac{L}{C}}
$$

được gọi là hệ số phẩm chất của mạch nối tiếp. Nếu mạch có điện trở thuần $R$ rất nhỏ so với dung kháng $X_C$, hệ số phẩm chất $Q$ có thể dễ dàng đạt các giá trị từ $5$ đến $10$ hoặc cao hơn. Khi đó:

- Với $Q = 5$, điện áp hiệu dụng trên tụ là $V_{C,\mathrm{rms}} = 5 \times 120\,\mathrm V = 600\,\mathrm V$, với biên độ đỉnh lên tới $600\sqrt{2} \approx 849\,\mathrm V$.
- Mức điện áp đỉnh này vượt xa giới hạn cách điện danh định $200\,\mathrm V$ hoặc $400\,\mathrm V$ của tụ điện, phá vỡ lớp điện môi giữa hai bản cực và gây nổ hoặc hỏng tụ điện hoàn toàn.
:::

::: exercise Q31.11
Một máy sấy tóc thường được mô hình hóa đơn giản như một điện trở thuần. Tuy nhiên, vì máy sấy có các cuộn dây trong bộ phận đốt nóng và có cuộn dây bên trong động cơ quay cánh quạt, máy sấy thực tế còn có độ tự cảm đáng kể. Về mặt định tính, việc tính thêm độ tự cảm này vào mô hình sẽ làm tăng hay làm giảm các giá trị của $R$, $I_{\mathrm{rms}}$ và công suất tiêu thụ trung bình $P$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Đánh giá ảnh hưởng định tính của độ tự cảm $L$ trong máy sấy tóc lên điện trở thuần $R$, cường độ dòng điện hiệu dụng $I_{\mathrm{rms}}$ và công suất trung bình $P$.

**Hướng đi:**

- **Cấu tạo vật liệu của điện trở thuần**: Dùng công thức điện trở dây dẫn $R = \rho l/S$ để xác định tính bất biến của $R$.
- **Công thức trở kháng**: Dùng $Z = \sqrt{R^2 + (\omega L)^2}$ để đánh giá sự tăng trở kháng khi có thêm cảm kháng.
- **Định luật Ohm và công thức công suất**: Dùng $I_{\mathrm{rms}} = V_{\mathrm{rms}}/Z$ và $P = I_{\mathrm{rms}}^2 R$ để so sánh dòng điện và công suất tiêu thụ trong mô hình mạch tuyến tính cố định $R, V_{\mathrm{rms}}, \omega$.

Mô hình so sánh chuẩn tắc: Giữ cố định điện trở thuần $R$, điện áp hiệu dụng nguồn $V_{\mathrm{rms}}$ và tần số góc $\omega$, khảo sát ảnh hưởng khi tính thêm một độ tự cảm lý tưởng $L$ vào sơ đồ mạch nối tiếp.

(a) Đối với điện trở thuần $R$: Điện trở thuần $R$ được quyết định bởi vật liệu, chiều dài và tiết diện của dây đốt nóng và cuộn dây theo công thức $R = \rho l/S$. Giá trị điện trở này không thay đổi khi tính thêm độ tự cảm $L$ vào mô hình. Do đó giá trị $R$ giữ nguyên không đổi.

(b) Đối với cường độ dòng điện hiệu dụng $I_{\mathrm{rms}}$:

Khi tính thêm độ tự cảm $L$, mạch có thêm cảm kháng $X_L = \omega L > 0$. Trở kháng toàn phần của máy sấy tăng lên từ $Z = R$ thành:

$$
Z = \sqrt{R^2 + (\omega L)^2} > R.
$$

Với điện áp hiệu dụng $V_{\mathrm{rms}}$ của nguồn không đổi, cường độ dòng điện hiệu dụng chạy qua máy sấy sẽ giảm xuống:

$$
\begin{aligned}
I_{\mathrm{rms}} &= \frac{V_{\mathrm{rms}}}{Z} \\
&= \frac{V_{\mathrm{rms}}}{\sqrt{R^2 + (\omega L)^2}} \\
&< \frac{V_{\mathrm{rms}}}{R}.
\end{aligned}
$$

(c) Đối với công suất tiêu thụ trung bình $P$:

Trong mô hình mạch tuyến tính có điện trở cố định $R$, công suất tiêu thụ trung bình được xác định bởi:

$$
P = I_{\mathrm{rms}}^2 R = \frac{V_{\mathrm{rms}}^2 R}{R^2 + (\omega L)^2}.
$$

Vì mẫu số tăng thêm số hạng $(\omega L)^2$ trong khi $R$ và $V_{\mathrm{rms}}$ không đổi, công suất tiêu thụ trung bình $P$ giảm đi so với khi chỉ có điện trở thuần ($V_{\mathrm{rms}}^2 / R$). Ta cũng thấy điều này từ $P = V_{\mathrm{rms}} I_{\mathrm{rms}} \cos\phi$: Cả dòng điện $I_{\mathrm{rms}}$ và hệ số công suất $\cos\phi = R/Z$ đều giảm, do đó công suất trung bình $P$ giảm. Lưu ý rằng mô hình so sánh này không đồng nhất cơ năng của động cơ thực tế với nhiệt Joule của dây quấn.
:::

::: exercise Q31.12
Một bóng đèn sợi đốt và một tụ điện phẳng có lớp điện môi bằng không khí được mắc nối tiếp với nhau vào một nguồn điện xoay chiều. Điều gì sẽ xảy ra với độ sáng của bóng đèn khi ta chèn một tấm chất điện môi vào giữa hai bản của tụ điện? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Đánh giá sự thay đổi độ sáng của bóng đèn mắc nối tiếp với tụ điện khi chèn tấm điện môi vào giữa hai bản tụ.

**Hướng đi:**

- **Công thức điện dung của tụ điện phẳng**: Dùng $C = K C_0$ để xác định sự tăng điện dung khi chèn điện môi có hằng số $K > 1$.
- **Công thức dung kháng**: Dùng $X_C = 1/(\omega C)$ để suy ra sự giảm dung kháng.
- **Công thức trở kháng và định luật Joule–Lenz**: Dùng $Z = \sqrt{R^2 + X_C^2}$ và $P = I_{\mathrm{rms}}^2 R$ để đánh giá sự tăng dòng điện và độ sáng bóng đèn.

(a) Biến đổi của điện dung và dung kháng: Điện dung ban đầu của tụ điện phẳng chứa không khí là $C_0$. Khi chèn một tấm chất điện môi có hằng số điện môi $K > 1$ vào lấp đầy khoảng không gian giữa hai bản cực, điện dung của tụ điện tăng lên $K$ lần:

$$
C = K C_0 > C_0.
$$

Dung kháng của tụ điện trong mạch xoay chiều tỉ lệ nghịch với điện dung $C$:

$$
X_C = \frac{1}{\omega C} = \frac{1}{\omega K C_0}.
$$

Do điện dung $C$ tăng lên, dung kháng $X_C$ của tụ điện sẽ giảm đi.

(b) Biến đổi của dòng điện và độ sáng bóng đèn:

Mô hình hóa bóng đèn sợi đốt bằng điện trở thuần $R$. Trở kháng của mạch nối tiếp gồm bóng đèn và tụ điện là

$$
Z = \sqrt{R^2 + X_C^2}.
$$

Khi $X_C$ giảm, trở kháng toàn mạch $Z$ giảm theo. Vì điện áp hiệu dụng của nguồn $V_{\mathrm{rms}}$ được giữ cố định, cường độ dòng điện hiệu dụng chạy qua mạch sẽ tăng lên:

$$
I_{\mathrm{rms}} = \frac{V_{\mathrm{rms}}}{Z}.
$$

Độ sáng của bóng đèn sợi đốt phụ thuộc trực tiếp vào công suất tỏa nhiệt trên dây tóc bóng đèn:

$$
P_{\mathrm{bulb}} = I_{\mathrm{rms}}^2 R.
$$

Vì cường độ dòng điện hiệu dụng $I_{\mathrm{rms}}$ tăng lên, công suất nhiệt tỏa ra trên bóng đèn tăng, kéo theo nhiệt độ dây tóc tăng và độ sáng của bóng đèn tăng lên rõ rệt (đèn sáng hơn).
:::

::: exercise Q31.13
Một cuộn dây quấn quanh một ống trụ rỗng và một bóng đèn sợi đốt được mắc nối tiếp vào một nguồn điện xoay chiều. Điều gì sẽ xảy ra với độ sáng của bóng đèn khi ta luồn một thanh sắt vào bên trong lòng ống trụ? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khảo sát sự thay đổi độ sáng của bóng đèn mắc nối tiếp với cuộn cảm khi luồn thanh sắt vào trong lòng ống dây rỗng.

**Hướng đi:**

- **Tính chất vật liệu sắt từ**: Xét sự tăng từ thông liên kết để suy ra độ tự cảm tăng khi luồn thanh sắt trong miền chưa bão hòa.
- **Công thức cảm kháng**: Dùng $X_L = \omega L$ để xác định sự tăng cảm kháng.
- **Công thức trở kháng và công suất tỏa nhiệt**: Dùng $Z = \sqrt{(R+r)^2 + X_L^2}$ và $P = I_{\mathrm{rms}}^2 R$ để suy ra sự giảm dòng điện và làm tối bóng đèn.

(a) Biến đổi của độ tự cảm và cảm kháng:

Khi ống dây có lõi là không khí, độ tự cảm của cuộn dây là $L_0$. Sắt là vật liệu sắt từ. Trong miền chưa bão hòa, lõi sắt làm tăng từ thông liên kết của cuộn dây.

Khi luồn thanh sắt vào bên trong lòng ống dây, khả năng tập trung và gia tăng từ thông của cuộn cảm tăng lên vượt bậc, dẫn đến độ tự cảm của cuộn dây tăng vọt:

$$
L > L_0.
$$

Cảm kháng của cuộn dây tỉ lệ thuận với độ tự cảm $L$:

$$
X_L = \omega L = 2\pi f L.
$$

Do đó, cảm kháng $X_L$ của cuộn cảm tăng lên rất lớn.

(b) Ảnh hưởng lên độ sáng bóng đèn:

Trở kháng toàn phần của mạch nối tiếp gồm bóng đèn (điện trở $R$) và cuộn dây (có điện trở thuần nhỏ $r$) là

$$
Z = \sqrt{(R + r)^2 + X_L^2}.
$$

Khi $X_L$ tăng mạnh, trở kháng toàn mạch $Z$ tăng lên tương ứng. Dưới điện áp nguồn không đổi, cường độ dòng điện hiệu dụng chạy qua đèn giảm mạnh:

$$
I_{\mathrm{rms}} = \frac{V_{\mathrm{rms}}}{Z}.
$$

Công suất phát sáng của bóng đèn phụ thuộc vào bình phương cường độ dòng điện:

$$
P_{\mathrm{bulb}} = I_{\mathrm{rms}}^2 R.
$$

Do dòng điện hiệu dụng giảm mạnh, công suất tỏa nhiệt trên dây tóc bóng đèn giảm đi đáng kể, làm cho bóng đèn tối đi rõ rệt, thậm chí có thể gần như tắt hẳn nếu cảm kháng đủ lớn.
:::

::: exercise Q31.14
Một mạch điện gồm một bóng đèn, một tụ điện và một cuộn cảm mắc nối tiếp với nhau vào một nguồn điện xoay chiều. Điều gì sẽ xảy ra với độ sáng của bóng đèn khi ta tháo bỏ cuộn cảm ra khỏi mạch? Điều gì sẽ xảy ra khi ta giữ cuộn cảm trong mạch nhưng tháo bỏ tụ điện? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khảo sát sự thay đổi độ sáng của bóng đèn trong mạch RLC nối tiếp khi lần lượt tháo bỏ cuộn cảm hoặc tháo bỏ tụ điện (nối tắt hai đầu linh kiện được tháo).

**Hướng đi:**

- **Công thức trở kháng mạch R-L-C nối tiếp**: Dùng $Z_0 = \sqrt{R^2 + (X_L - X_C)^2}$ làm cơ sở so sánh ban đầu.
- **Trở kháng khi tháo linh kiện**: Thiết lập $Z_1 = \sqrt{R^2 + X_C^2}$ khi tháo cuộn cảm và $Z_2 = \sqrt{R^2 + X_L^2}$ khi tháo tụ điện.
- **Biện luận điều kiện**: So sánh $(X_L - X_C)^2$ với $X_C^2$ và $X_L^2$ để kết luận điều kiện làm đèn sáng hơn, tối đi hoặc giữ nguyên độ sáng.

Lưu ý rằng khái niệm "tháo bỏ linh kiện" ở đây được hiểu theo nghĩa kỹ thuật chuẩn mực là loại bỏ linh kiện và nối tắt đoạn mạch đó lại bằng dây dẫn lý tưởng. Nếu ngắt bỏ linh kiện mà để hở mạch, dòng điện trong mạch hở sẽ lập tức bằng không và bóng đèn sẽ tắt hẳn.

Trở kháng ban đầu của mạch nối tiếp là

$$
Z_0 = \sqrt{R^2 + (X_L - X_C)^2}.
$$

Độ sáng của bóng đèn tăng hay giảm phụ thuộc vào việc trở kháng mới nhỏ hơn hay lớn hơn $Z_0$.

(a) Khi tháo bỏ cuộn cảm (mạch chỉ còn bóng đèn nối tiếp với tụ điện):

Trở kháng mới của mạch là

$$
Z_1 = \sqrt{R^2 + X_C^2}.
$$

Ta so sánh $(X_L - X_C)^2$ với $X_C^2$:

$$
(X_L - X_C)^2 - X_C^2 = X_L^2 - 2X_L X_C = X_L(X_L - 2X_C).
$$

- Nếu ban đầu $X_L > 2X_C$: Ta có $Z_0 > Z_1$. Khi tháo cuộn cảm, trở kháng mạch giảm, dòng điện tăng lên và bóng đèn sẽ sáng hơn.
- Nếu ban đầu $X_L < 2X_C$ (bao gồm trường hợp mạch đang ở trạng thái cộng hưởng $X_L = X_C$): Ta có $Z_0 < Z_1$. Khi tháo cuộn cảm, trở kháng mạch tăng lên, dòng điện giảm đi và bóng đèn sẽ tối đi.
- Nếu ban đầu $X_L = 2X_C$: Trở kháng không đổi ($Z_1 = Z_0$), độ sáng của bóng đèn giữ nguyên.

(b) Khi tháo bỏ tụ điện và giữ cuộn cảm (mạch chỉ còn bóng đèn nối tiếp với cuộn cảm):

Trở kháng mới của mạch là

$$
Z_2 = \sqrt{R^2 + X_L^2}.
$$

Ta so sánh $(X_L - X_C)^2$ với $X_L^2$:

$$
(X_L - X_C)^2 - X_L^2 = X_C^2 - 2X_L X_C = X_C(X_C - 2X_L).
$$

- Nếu ban đầu $X_C > 2X_L$: Trở kháng giảm ($Z_2 < Z_0$), dòng điện tăng và bóng đèn sáng hơn.
- Nếu ban đầu $X_C < 2X_L$ (bao gồm trường hợp cộng hưởng $X_L = X_C$): Trở kháng tăng ($Z_2 > Z_0$), dòng điện giảm và bóng đèn tối đi.
- Nếu ban đầu $X_C = 2X_L$: Trở kháng không đổi, độ sáng bóng đèn giữ nguyên.
:::

::: exercise Q31.15
Một mạch điện gồm một bóng đèn, một tụ điện và một cuộn cảm mắc nối tiếp vào một nguồn điện xoay chiều. Liệu có thể tháo bỏ cả tụ điện và cuộn cảm ra khỏi mạch (nối tắt hai đầu của chúng) mà độ sáng của bóng đèn vẫn hoàn toàn không thay đổi hay không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xác định điều kiện để việc loại bỏ cả cuộn cảm và tụ điện không làm thay đổi độ sáng của bóng đèn trong mạch RLC nối tiếp.

**Hướng đi:**

- **Điều kiện bảo toàn độ sáng**: Thiết lập phương trình đẳng trở kháng $Z = Z' = R$ với nguồn và điện trở đèn cố định.
- **Hiện tượng cộng hưởng điện**: Giải phương trình $(X_L - X_C)^2 = 0$ để suy ra điều kiện $X_L = X_C$ tại tần số góc $\omega_0 = 1/\sqrt{LC}$. Điều này hoàn toàn có thể xảy ra, với một điều kiện duy nhất là trước khi tháo bỏ, mạch điện xoay chiều ban đầu đang hoạt động ở đúng tần số cộng hưởng.

Chứng minh:

Trở kháng ban đầu của mạch RLC nối tiếp chứa bóng đèn có điện trở $R$ là

$$
Z = \sqrt{R^2 + (X_L - X_C)^2}.
$$

Khi tháo bỏ cả cuộn cảm lẫn tụ điện và nối kín mạch bằng dây dẫn, tải tiêu thụ chỉ còn lại duy nhất điện trở thuần $R$ của bóng đèn. Trở kháng mới của mạch lúc này là

$$
Z' = R.
$$

Độ sáng của bóng đèn phụ thuộc vào công suất tỏa nhiệt $P = I_{\mathrm{rms}}^2 R = (V_{\mathrm{rms}}/Z)^2 R$. Do điện áp nguồn và điện trở đèn không đổi, để độ sáng bóng đèn không thay đổi thì cường độ dòng điện hiệu dụng phải giữ nguyên, tương đương với điều kiện trở kháng toàn mạch không đổi:

$$
Z = Z'
$$

$$
\iff \sqrt{R^2 + X_{\mathrm d}^2} = R,
$$

với $X_{\mathrm d} = X_L - X_C$.

Bình phương hai vế và rút gọn, ta thu được

$$
(X_L - X_C)^2 = 0
$$

$$
\iff X_L = X_C.
$$

Điều này đồng nghĩa với việc tần số góc của nguồn điện phải bằng chính xác tần số góc cộng hưởng riêng của hệ:

$$
\omega = \frac{1}{\sqrt{LC}}.
$$

Ở trạng thái cộng hưởng này, điện áp trên cuộn cảm và điện áp trên tụ điện luôn ngược pha nhau $180^\circ$ và có biên độ bằng nhau tại mọi thời điểm, do đó tác dụng cản trở dòng điện của cảm kháng và dung kháng đã tự triệt tiêu lẫn nhau hoàn toàn. Trở kháng của mạch ban đầu đã bằng đúng điện trở thuần $R$. Vì vậy, việc tháo bỏ đồng thời cả hai linh kiện không làm thay đổi trở kháng của mạch, và độ sáng của bóng đèn được bảo toàn tuyệt đối.
:::

::: exercise Q31.16
Máy biến áp có thể sử dụng được với dòng điện một chiều không đổi (DC) hay không? Hãy giải thích rõ cơ chế vật lý. Điều gì sẽ xảy ra nếu một máy biến áp được thiết kế cho điện áp xoay chiều $120\,\mathrm V$ lại bị đấu nhầm vào đường dây điện một chiều $120\,\mathrm V$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Giải thích nguyên lý hoạt động của máy biến áp đối với dòng một chiều, và dự đoán hậu quả khi cấp điện áp một chiều $120\,\mathrm V$ vào máy biến áp được thiết kế cho mạng xoay chiều $120\,\mathrm V$.

**Hướng đi:**

- **Định luật cảm ứng Faraday**: Dùng $\mathcal E_2 = -N_2 (d\Phi_B/dt)$ để chứng minh từ trường không biến thiên trong chế độ DC không tạo ra suất điện động cảm ứng.
- **Khảo sát trở kháng theo tần số**: So sánh trở kháng cuộn sơ cấp $Z_{\mathrm{ac}} \approx \omega L$ với điện trở thuần $R_{\mathrm{cu}}$ khi tần số $\omega = 0$.
- **Định luật Ohm và Joule–Lenz**: Dùng $I_{\mathrm{dc}} = V_{\mathrm{dc}}/R_{\mathrm{cu}}$ và $P = I_{\mathrm{dc}}^2 R_{\mathrm{cu}}$ để dự báo dòng điện quá tải và nguy cơ cháy cuộn dây.

(a) Máy biến áp không thể hoạt động với dòng điện một chiều không đổi:

Máy biến áp hoạt động dựa trên hiện tượng cảm ứng điện từ hỗ cảm giữa hai cuộn dây qua lõi từ khép kín. Theo định luật cảm ứng Faraday, suất điện động cảm ứng sinh ra ở cuộn thứ cấp tỉ lệ thuận với tốc độ biến thiên của từ thông trong lõi thép:

$$
\mathcal E_2 = -N_2 \frac{d\Phi_B}{dt}.
$$

Khi cấp điện bởi dòng điện một chiều không đổi (DC), dòng điện trong cuộn sơ cấp có cường độ ổn định theo thời gian ($di_1/dt = 0$). Từ trường do nó sinh ra trong lõi từ là từ trường tĩnh, kéo theo tốc độ biến thiên của từ thông qua cuộn thứ cấp bằng không:

$$
\frac{d\Phi_B}{dt} = 0 \implies \mathcal E_2 = 0.
$$

Do đó, ở trạng thái dừng không có bất kỳ điện áp hay dòng điện nào được truyền sang mạch thứ cấp. Máy biến áp hoàn toàn không thể làm biến đổi điện áp của dòng điện một chiều.

(b) Hậu quả khi đấu máy biến áp $120\,\mathrm V$ xoay chiều vào nguồn $120\,\mathrm V$ một chiều:

- Trong chế độ xoay chiều bình thường: Cuộn sơ cấp có độ tự cảm rất lớn ($L$), tạo ra một cảm kháng rất cao $X_L = \omega L = 2\pi f L$. Ngay cả khi mạch thứ cấp để hở, cảm kháng này hạn chế dòng điện chạy trong cuộn sơ cấp ở mức dòng từ hóa rất nhỏ an toàn:

$$
\begin{aligned}
I_{\mathrm{rms}} &\approx \frac{V_{\mathrm{rms}}}{\sqrt{R_{\mathrm{cu}}^2 + X_L^2}} \\
&\approx \frac{V_{\mathrm{rms}}}{X_L}.
\end{aligned}
$$

- Trong chế độ một chiều: Tần số bằng không ($\omega = 0$), do đó cảm kháng triệt tiêu hoàn toàn:

$$
X_L = 0.
$$

Cuộn sơ cấp lúc này chỉ còn lại duy nhất điện trở thuần $R_{\mathrm{cu}}$ của dây quấn đồng. Để giảm thiểu hao phí trong vận hành, dây quấn máy biến áp luôn được chế tạo có điện trở thuần rất bé, vì vậy dòng điện một chiều có thể rất lớn.

Cường độ dòng điện một chiều chạy qua cuộn sơ cấp sẽ tăng vọt lên mức cực đại theo định luật Ohm:

$$
I_{\mathrm{dc}} = \frac{V_{\mathrm{dc}}}{R_{\mathrm{cu}}} = \frac{120\,\mathrm V}{R_{\mathrm{cu}}} \gg I_{\mathrm{ac}}.
$$

Dòng điện khổng lồ này sinh ra công suất tỏa nhiệt Joule cực lớn:

$$
P = I_{\mathrm{dc}}^2 R_{\mathrm{cu}}.
$$

Lượng nhiệt phát sinh nhanh chóng đốt cháy lớp men cách điện của dây quấn, gây hiện tượng ngắn mạch, phá hủy hoàn toàn máy biến áp và có nguy cơ cao bốc cháy hoặc làm nhảy aptomat bảo vệ mạng điện.
:::

::: exercise Q31.17
Một máy biến áp lý tưởng có $N_1$ vòng dây ở cuộn sơ cấp và $N_2$ vòng dây ở cuộn thứ cấp. Nếu ta chỉ tăng gấp đôi số vòng dây của cuộn thứ cấp, hãy xác định. (a) Biên độ điện áp ở cuộn thứ cấp thay đổi theo thừa số nào?

(b) Điện trở tương đương của mạch thứ cấp quy đổi về phía sơ cấp thay đổi theo thừa số nào?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xác định sự thay đổi của biên độ điện áp thứ cấp và điện trở phản xạ về sơ cấp khi số vòng dây thứ cấp tăng gấp đôi ($N_2' = 2N_2$).

**Hướng đi:**

- **Hệ thức máy biến áp lý tưởng**: Dùng $V_2 / V_1 = N_2 / N_1$ để xác định tỉ số biến đổi điện áp theo số vòng dây.
- **Công thức phản xạ trở kháng**: Dùng $R_{\mathrm{eff}} = (N_1/N_2)^2 R$ để xác định điện trở tải quy đổi về phía cuộn sơ cấp.

(a) Biến đổi của biên độ điện áp ở cuộn thứ cấp: Đối với máy biến áp lý tưởng, tỉ số giữa biên độ điện áp hai cuộn dây bằng tỉ số số vòng dây tương ứng:

$$
\frac{V_2}{V_1} = \frac{N_2}{N_1}
$$

$$
\implies V_2 = \left(\frac{N_2}{N_1}\right) V_1.
$$

Khi giữ nguyên số vòng dây sơ cấp $N_1$ và biên độ điện áp sơ cấp $V_1$, việc tăng gấp đôi số vòng dây thứ cấp ($N_2' = 2 N_2$) sẽ làm biên độ điện áp ở cuộn thứ cấp thay đổi theo:

$$
V_2' = \left(\frac{2 N_2}{N_1}\right) V_1 = 2 V_2.
$$

Biên độ điện áp ở cuộn thứ cấp tăng gấp đôi, tức là thay đổi theo thừa số $2$.

(b) Biến đổi của điện trở tương đương quy đổi về phía sơ cấp:

Xét tải thuần trở $R$ mắc cố định vào mạch thứ cấp. Theo định luật bảo toàn công suất cho máy biến áp lý tưởng ($V_1 I_1 = V_2 I_2$), bản thân điện trở tải $R$ ở thứ cấp không đổi, nhưng điện trở tương đương $R_{\mathrm{eff}}$ mà nguồn điện ở phía cuộn sơ cấp nhìn thấy được xác định bởi:

$$
\begin{aligned}
R_{\mathrm{eff}} &= \frac{V_1}{I_1} \\
&= \frac{V_2 / (N_2/N_1)}{I_2 (N_2/N_1)} \\
&= \left(\frac{N_1}{N_2}\right)^2 \frac{V_2}{I_2} \\
&= \left(\frac{N_1}{N_2}\right)^2 R.
\end{aligned}
$$

Khi số vòng dây thứ cấp tăng gấp đôi thành $N_2' = 2 N_2$, điện trở tương đương quy đổi về phía sơ cấp mới là:

$$
\begin{aligned}
R_{\mathrm{eff}}' &= \left(\frac{N_1}{2 N_2}\right)^2 R \\
&= \frac{1}{4}\left(\frac{N_1}{N_2}\right)^2 R \\
&= \frac{1}{4} R_{\mathrm{eff}}.
\end{aligned}
$$

Điện trở tương đương của mạch thứ cấp quy đổi về phía cuộn sơ cấp giảm đi bốn lần, tức là thay đổi theo thừa số $1/4$.
:::

::: exercise Q31.18
Một cuộn cảm, một tụ điện và một điện trở thuần được mắc nối tiếp với nhau vào một nguồn điện xoay chiều. Nếu điện trở thuần, độ tự cảm và điện dung đều được tăng gấp đôi, hãy xác định các đại lượng sau thay đổi theo thừa số nào (và tăng hay giảm). (a) Tần số góc cộng hưởng.

(b) Cảm kháng ở một tần số nguồn cho trước.

(c) Dung kháng ở một tần số nguồn cho trước.

(d) Trở kháng toàn mạch có tăng gấp đôi hay không?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Đánh giá sự thay đổi của $\omega_0$, $X_L$, $X_C$ và $Z$ khi đồng thời tăng gấp đôi $R$, $L$ và $C$ ($R' = 2R, L' = 2L, C' = 2C$).

**Hướng đi:**

- **Công thức tần số góc cộng hưởng**: Dùng $\omega_0 = 1/\sqrt{LC}$ để xác định sự thay đổi của tần số cộng hưởng riêng.
- **Công thức cảm kháng và dung kháng**: Dùng $X_L = \omega L$ và $X_C = 1/(\omega C)$ ở tần số $\omega$ cho trước.
- **Công thức trở kháng toàn phần**: Dùng $Z = \sqrt{R^2 + (X_L - X_C)^2}$ để kiểm tra điều kiện đẳng thức $Z' = 2Z$.

Theo giả thiết, các thông số mới của linh kiện là $R' = 2R$, $L' = 2L$ và $C' = 2C$.

(a) Tần số góc cộng hưởng:

Tần số góc cộng hưởng ban đầu là:

$$
\omega_0 = \frac{1}{\sqrt{LC}}.
$$

Khi thay các thông số mới vào:

$$
\begin{aligned}
\omega_0' &= \frac{1}{\sqrt{L' C'}} \\
&= \frac{1}{\sqrt{(2L)(2C)}} = \frac{\omega_0}{2}.
\end{aligned}
$$

Tần số góc cộng hưởng thay đổi theo thừa số $1/2$, tức là giảm đi một nửa.

(b) Cảm kháng ở tần số góc $\omega$ cho trước của nguồn:

$$
X_L' = \omega L' = 2\omega L = 2 X_L.
$$

Cảm kháng thay đổi theo thừa số $2$, tức là tăng gấp đôi.

(c) Dung kháng ở tần số góc $\omega$ cho trước của nguồn:

$$
\begin{aligned}
X_C' &= \frac{1}{\omega(2C)} \\
&= \frac{1}{2\omega C} = \frac{1}{2} X_C.
\end{aligned}
$$

Dung kháng thay đổi theo thừa số $1/2$, tức là giảm đi một nửa.

(d) Khảo sát trở kháng toàn mạch $Z$:

Trở kháng toàn phần của mạch ban đầu là:

$$
Z = \sqrt{R^2 + (X_L - X_C)^2}.
$$

Trở kháng mới của mạch là:

$$
\begin{aligned}
Z' &= \sqrt{(R')^2 + X_{\mathrm{new}}^2} \\
&= \sqrt{4R^2 + X_{\mathrm{new}}^2},
\end{aligned}
$$

với $X_{\mathrm{new}} = 2 X_L - X_C / 2$. Để trở kháng tăng gấp đôi, ta cần $Z' = 2Z$, tương đương với:

$$
\begin{aligned}
4R^2 + &\left(2 X_L - \frac{X_C}{2}\right)^2 \\
&= 4\left[R^2 + (X_L - X_C)^2\right].
\end{aligned}
$$

Triệt tiêu $4R^2$ ở cả hai vế:

$$
 \le ft(2 X_L - \frac{X_C}{2}\right)^2 = 4(X_L - X_C)^2.
$$

Khai triển hai vế:

$$
4 X_L^2 - 2 X_L X_C + \frac{1}{4} X_C^2 = 4 X_L^2 - 8 X_L X_C + 4 X_C^2.
$$

Rút gọn các số hạng $4 X_L^2$:

$$
6 X_L X_C = \frac{15}{4} X_C^2
$$

$$
\iff \frac{X_L}{X_C} = \frac{5}{8}.
$$

Do đó đẳng thức $Z' = 2Z$ chỉ xảy ra tại tần số thỏa mãn tỉ số cảm kháng và dung kháng $X_L / X_C = 5/8$. Đối với một tần số bất kỳ nói chung, trở kháng toàn mạch không tăng gấp đôi ($Z' \ne 2Z$). Đặc biệt, nếu mạch ban đầu ở trạng thái cộng hưởng tại tần số nguồn cố định ($X_L = X_C \ne 0$), thì các giá trị cảm kháng và dung kháng ban đầu đều khác không. Khi tăng gấp đôi các thông số ở cùng tần số nguồn đó, mạch mới có $X_L' = 2X_L$ và $X_C' = X_C / 2 = X_L / 2$, dẫn đến hiệu điện kháng mới là $X_L' - X_C' = \frac{3}{2}X_L \ne 0$. Mạch mới không còn ở trạng thái cộng hưởng và $Z' = \sqrt{4R^2 + \frac{9}{4}X_L^2} > 2R = 2Z$.
:::

::: exercise Q31.19
Ta muốn làm tăng gấp đôi tần số góc cộng hưởng của một mạch xoay chiều RLC mắc nối tiếp bằng cách chỉ thay đổi các phần tử thích hợp trong mạch theo cùng một tỉ lệ như nhau. (a) Ta cần phải thay đổi các phần tử mạch nào? (b) Cần thay đổi chúng theo tỉ lệ (thừa số) bằng bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xác định các phần tử cần thay đổi và tỉ lệ thay đổi đồng nhất để tăng gấp đôi tần số góc cộng hưởng $\omega_0$ của mạch RLC nối tiếp.

**Hướng đi:**

- **Công thức tần số góc cộng hưởng**: Dùng $\omega_0 = 1/\sqrt{LC}$ để nhận diện các phần tử ảnh hưởng đến tần số cộng hưởng.
- **Tính chất độc lập với điện trở**: Xác định $R$ không ảnh hưởng đến $\omega_0$.
- **Thiết lập phương trình tỉ lệ**: Đặt $L' = k L$ và $C' = k C$ rồi giải phương trình $\omega_0' = 2\omega_0$ để tìm hệ số tỉ lệ $k$.

(a) Các phần tử mạch cần thay đổi:

Tần số góc cộng hưởng của mạch RLC nối tiếp được xác định bởi biểu thức

$$
\omega_0 = \frac{1}{\sqrt{LC}}.
$$

Đại lượng này chỉ phụ thuộc vào độ tự cảm $L$ của cuộn cảm và điện dung $C$ của tụ điện, hoàn toàn không phụ thuộc vào điện trở thuần $R$ của mạch. Do đó, để thay đổi tần số góc cộng hưởng, các phần tử thích hợp cần thay đổi là cuộn cảm (độ tự cảm $L$) và tụ điện (điện dung $C$), trong khi điện trở thuần $R$ được giữ nguyên.

(b) Tỉ lệ thay đổi cần thiết:

Giả sử ta thay đổi cả độ tự cảm và điện dung theo cùng một thừa số tỉ lệ dương $k$, nghĩa là

$$
L' = k L \quad \text{và} \quad C' = k C.
$$

Tần số góc cộng hưởng mới của mạch sẽ là

$$
\begin{aligned}
\omega_0' &= \frac{1}{\sqrt{L' C'}} \\
&= \frac{1}{\sqrt{(k L)(k C)}} = \frac{\omega_0}{k}.
\end{aligned}
$$

Theo yêu cầu đề bài, tần số góc cộng hưởng mới phải tăng gấp đôi so với giá trị ban đầu, tức là

$$
\omega_0' = 2 \omega_0
$$

$$
\iff \frac{\omega_0}{k} = 2 \omega_0.
$$

Suy ra giá trị của thừa số tỉ lệ là

$$
k = \frac{1}{2} = 0{,}5.
$$

Vậy ta cần giảm cả độ tự cảm $L$ và điện dung $C$ đi một nửa, tức là nhân giá trị của cả hai phần tử này với thừa số $1/2$ (hoặc $0{,}5$).
:::
