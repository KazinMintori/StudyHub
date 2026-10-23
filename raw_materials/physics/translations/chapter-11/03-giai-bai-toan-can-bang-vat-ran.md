## 11.3 Giải Bài Toán Cân Bằng Vật Rắn

Hai nguyên lý nền tảng để giải quyết mọi bài toán cân bằng vật rắn là: Tổng vectơ của tất cả các ngoại lực tác dụng lên vật phải bằng không, và tổng vectơ mômen của các ngoại lực đó đối với một điểm bất kỳ phải bằng không. Đối với các bài toán phẳng trong mặt phẳng $xy$, hai nguyên lý này tương đương với ba phương trình đại số độc lập:

$$
\sum F_x = 0
\tag{11.6a}
$$

$$
\sum F_y = 0
\tag{11.6b}
$$

$$
\sum \tau_z = 0
\tag{11.6c}
$$

Trong đó, phương trình (11.6a) và (11.6b) thể hiện điều kiện thứ nhất, còn phương trình (11.6c) thể hiện điều kiện thứ hai. Nhờ tính độc lập của điểm quy chiếu khi tổng hợp lực bằng không, ta hoàn toàn có quyền tự do lựa chọn vị trí trục quay tính mômen lực $\tau_z$ tại bất kỳ điểm nào thuận tiện nhất. Điểm quy chiếu lý tưởng thường là giao điểm của đường tác dụng của càng nhiều lực chưa biết càng tốt, bởi vì cánh tay đòn của các lực đó bằng không, giúp triệt tiêu chúng khỏi phương trình mômen lực.

### Chiến Lược Giải Bài Toán 11.1: Cân Bằng Của Vật Rắn

- **Xác định (Identify)**:
  - Xác định rõ vật rắn hoặc hệ vật rắn cần khảo sát trạng thái cân bằng tĩnh.
  - Liệt kê chính xác các đại lượng đã biết và xác định rõ các ẩn số mục tiêu cần tìm (thường là độ lớn các lực chưa biết, các thành phần phản lực liên kết, vị trí đặt lực hoặc góc nghiêng).
- **Thiết lập (Set Up)**:
  - Vẽ sơ đồ vật tự do (free-body diagram) chi tiết và cô lập riêng cho vật rắn đang xét.
  - Vẽ đầy đủ tất cả các ngoại lực tác dụng lên vật tại đúng điểm đặt thực tế của chúng trên vật. Tuyệt đối không quy tụ tất cả các lực về một điểm như trong cơ học chất điểm, vì điểm đặt của lực quyết định trực tiếp cánh tay đòn và mômen lực.
  - Trọng lực của vật phải được vẽ đặt tại trọng tâm của vật (hoặc khối tâm đối với vật đồng chất trong trường trọng lực đều).
  - Chọn hệ trục tọa độ vuông góc $xy$ thuận lợi và quy ước chiều dương cho các trục cũng như chiều dương cho mômen lực (thường quy ước ngược chiều kim đồng hồ là dương).
  - Chọn một điểm quy chiếu thuận tiện nhất để thiết lập phương trình mômen lực.
- **Thực hiện (Execute)**:
  - Thiết lập ba phương trình cân bằng tĩnh theo hệ phương trình (11.6).
  - Giải hệ phương trình đại số để tìm các ẩn số mục tiêu. Trong một bài toán phẳng, ba phương trình độc lập cho phép xác định tối đa ba ẩn số vô hướng.
- **Đánh giá (Evaluate)**:
  - Kiểm tra dấu của các thành phần lực tìm được: Nếu một thành phần lực nhận giá trị âm, điều đó có nghĩa là chiều thực tế của lực ngược với chiều giả định ban đầu trên sơ đồ vật tự do.
  - Kiểm tra tính hợp lý của thứ nguyên, đơn vị và độ lớn vật lý của nghiệm số.
  - Kiểm tra chéo kết quả bằng cách viết lại phương trình mômen lực đối với một điểm quy chiếu thứ hai khác.

![](../img/young-11/a-hinh-11-08.png)

*Hình 11.8: Vận động viên ở tư thế plank: (a) Tư thế thực tế trên hai chiếc cân đo; (b) Sơ đồ vật tự do của vận động viên ở trạng thái cân bằng.*

::: example Ví dụ 11.2: Xác định trọng tâm cơ thể khi tập thể dục
Tư thế plank (Hình 11.8a) là một bài tập rất hữu hiệu để rèn luyện và tăng cường sức mạnh cho các nhóm cơ bụng, cơ lưng và cơ vai. Ta cũng có thể ứng dụng tư thế này để xác định vị trí trọng tâm của người tập. Một vận động viên thể dục có chiều cao $H = 1{,}80\,\text{m}$ thực hiện tư thế plank đứng yên thăng bằng. Khoảng cách nằm ngang giữa điểm tiếp xúc ngón chân với mặt sàn và điểm tiếp xúc bàn tay với mặt sàn là $L = 1{,}53\,\text{m}$. Người ta đặt hai chiếc cân ở dưới bàn tay và ngón chân. Cân đặt dưới bàn tay chỉ lực ép bằng $0{,}660 w$, trong khi cân đặt dưới ngón chân chỉ lực ép bằng $0{,}340 w$, với $w$ là tổng trọng lượng của vận động viên. Hãy xác định khoảng cách $L_{\mathrm{cg}}$ từ ngón chân đến trọng tâm của vận động viên theo mét và theo tỷ lệ phần trăm chiều cao cơ thể.

**Tóm tắt**:
- Chiều cao người tập: $H = 1{,}80\,\text{m}$.
- Khoảng cách giữa hai điểm tiếp xúc: $L = 1{,}53\,\text{m}$.
- Lực nâng tại ngón chân: $n_{\text{chân}} = 0{,}340 w$.
- Lực nâng tại bàn tay: $n_{\text{tay}} = 0{,}660 w$.
- Mục tiêu: Tìm $L_{\mathrm{cg}}$ từ ngón chân đến trọng tâm và tỷ số $L_{\mathrm{cg}} / H$.

**Hướng đi**:
- Người tập ở trạng thái đứng yên nên thỏa mãn hoàn toàn hai điều kiện cân bằng tĩnh.
- Chọn điểm quy chiếu để tính mômen lực tại ngón chân. Khi đó, cánh tay đòn của phản lực tại ngón chân bằng không, giúp phương trình mômen lực chỉ còn lại trọng lượng $w$ và lực nâng tại bàn tay.

**Các bước giải chi tiết**:
Sơ đồ vật tự do của vận động viên được mô tả trên Hình 11.8b. Gọi $n_1$ và $n_2$ lần lượt là lực nâng tại ngón chân và bàn tay:

$$
n_1 = 0{,}340 w
$$

$$
n_2 = 0{,}660 w
$$

Kiểm tra điều kiện thứ nhất theo phương thẳng đứng:

$$
n_1 + n_2 - w = 0
$$

Điều kiện thứ nhất được thỏa mãn tuyệt đối. Thiết lập phương trình mômen lực đối với điểm tiếp xúc ngón chân:

$$
-w L_{\mathrm{cg}} + n_2 L = 0
$$

Thay $n_2 = 0{,}660 w$ và $L = 1{,}53\,\text{m}$, ta có $0{,}660 \times 1{,}53 \approx 1{,}01$:

$$
-w L_{\mathrm{cg}} + 1{,}01 w = 0
$$

Triệt tiêu trọng lượng $w$ ở cả hai vế:

$$
L_{\mathrm{cg}} = 1{,}01\,\text{m}
$$

Tính tỷ lệ phần trăm khoảng cách này so với chiều cao toàn thân:

$$
\frac{L_{\mathrm{cg}}}{H} = \frac{1{,}01\,\text{m}}{1{,}80\,\text{m}} = 56{,}1\%
$$

**Đánh giá và kiểm tra**:
Trọng tâm của vận động viên nằm cách ngón chân khoảng $1{,}01\,\text{m}$, tức là ở mức xấp xỉ $56\%$ chiều cao cơ thể tính từ chân. Vị trí này nằm ngay phía dưới rốn một đoạn ngắn, hoàn toàn phù hợp với cấu tạo giải phẫu của cơ thể người.

Ta có thể kiểm tra chéo bằng cách tính mômen lực đối với điểm tiếp xúc bàn tay:

$$
w(L - L_{\mathrm{cg}}) - n_1 L = 0
$$

Với $n_1 = 0{,}340 w$, ta suy ra:

$$
L - L_{\mathrm{cg}} \approx 0{,}52\,\text{m}
$$

Từ đó, ta tìm được khoảng cách trọng tâm $L_{\mathrm{cg}} = 1{,}01\,\text{m}$, hoàn toàn khớp với kết quả ban đầu.
:::

![](../img/young-11/a-hinh-11-09.png)

*Hình 11.9: Bài toán chiếc thang của hiệp sĩ Lancelot: (a) Lancelot dừng lại ở một phần ba thang; (b) Sơ đồ vật tự do cho hệ thang và hiệp sĩ; (c) Lực tiếp xúc tổng hợp tại chân thang hợp với phương ngang một góc 75 độ, không trùng phương của thang.*

::: example Ví dụ 11.3: Chiếc thang có bị trượt không?
Hiệp sĩ Lancelot có trọng lượng $w_L = 800\,\text{N}$ đang leo lên một bức tường thành bằng một chiếc thang đồng chất dài $L = 5{,}0\,\text{m}$ và có trọng lượng $w_{\text{thang}} = 180\,\text{N}$ (Hình 11.9a). Chân thang tựa trên gờ đá bờ hào, còn đầu thang tựa vào bức tường thành thẳng đứng nhẵn bóng không có ma sát. Thang nghiêng một góc $\theta = 53{,}1^\circ$ so với phương nằm ngang. Hiệp sĩ tạm dừng lại khi leo được một phần ba chiều dài thang tính từ chân thang.

- (a) Hãy tìm độ lớn của phản lực pháp tuyến và lực ma sát nghỉ tác dụng lên chân thang.
- (b) Xác định hệ số ma sát nghỉ tối thiểu $\mu_s$ giữa chân thang và gờ đá để chiếc thang không bị trượt.
- (c) Xác định độ lớn và hướng của lực tiếp xúc tổng hợp tác dụng lên chân thang.

**Tóm tắt**:
- Chiều dài thang: $L = 5{,}0\,\text{m}$.
- Trọng lượng thang: $w_{\text{thang}} = 180\,\text{N}$.
- Trọng lượng Lancelot: $w_L = 800\,\text{N}$.
- Góc nghiêng của thang: $\theta = 53{,}1^\circ$.
- Vị trí Lancelot: Cách chân thang một đoạn $d_L = L/3$.
- Bức tường thành thẳng đứng không ma sát.

**Hướng đi**:
- Hệ vật gồm thang và hiệp sĩ đứng yên nên thỏa mãn hai điều kiện cân bằng tĩnh.
- Tường nhẵn không ma sát chỉ tác dụng lực pháp tuyến $n_1$ vuông góc với tường (hướng sang phải).
- Chân thang chịu phản lực pháp tuyến thẳng đứng $n_2$ và lực ma sát nghỉ $f_s$ hướng sang trái để chống lại xu hướng trượt ra xa tường.
- Chọn chân thang $B$ làm điểm tính mômen lực để triệt tiêu đồng thời cả hai ẩn số $n_2$ và $f_s$.

**Các bước giải chi tiết**:
Sơ đồ vật tự do của hệ được biểu diễn trên Hình 11.9b.

Các thông số hình học của thang:

$$
\cos 53{,}1^\circ = 0{,}600
$$

$$
\sin 53{,}1^\circ = 0{,}800
$$

Khoảng cách nằm ngang từ chân thang đến đầu trên của thang là $3{,}0\,\text{m}$. Chiều cao của đầu thang tựa vào tường là $4{,}0\,\text{m}$.

Vì thang đồng chất nên trọng tâm thang nằm ở chính giữa, cách chân thang một khoảng nằm ngang là $(1/2) \times 3{,}0\,\text{m} = 1{,}5\,\text{m}$. Hiệp sĩ Lancelot đứng ở vị trí một phần ba chiều dài thang, cách chân thang một khoảng nằm ngang là $(1/3) \times 3{,}0\,\text{m} = 1{,}0\,\text{m}$.

**(a) Tìm phản lực pháp tuyến và lực ma sát tại chân thang**:
Gọi $w_t = 180\,\text{N}$ là trọng lượng thang. Phương trình cân bằng lực theo phương thẳng đứng:

$$
n_2 - w_t - w_L = 0
$$

$$
n_2 = 180 + 800 = 980\,\text{N}
$$

Phương trình cân bằng lực theo phương nằm ngang:

$$
f_s - n_1 = 0 \implies f_s = n_1
$$

Thiết lập phương trình mômen lực đối với chân thang $B$:

$$
4{,}0 n_1 - \tau_w = 0
$$

Trong đó, mômen do trọng lượng thang là $(180)(1{,}5) = 270\,\text{N}\cdot\text{m}$, còn mômen do trọng lượng người là $(800)(1{,}0) = 800\,\text{N}\cdot\text{m}$. Tổng mômen của hai trọng lực là:

$$
\tau_w = 1070\,\text{N}\cdot\text{m}
$$

Thay vào phương trình mômen lực:

$$
4{,}0 n_1 = 1070\,\text{N}\cdot\text{m}
$$

$$
n_1 = \frac{1070\,\text{N}\cdot\text{m}}{4{,}0\,\text{m}} = 268\,\text{N}
$$

Từ phương trình cân bằng lực nằm ngang, ta suy ra:

$$
f_s = n_1 = 268\,\text{N}
$$

**(b) Tìm hệ số ma sát nghỉ tối thiểu**:
Theo định luật ma sát nghỉ, lực ma sát nghỉ thực tế không được vượt quá lực ma sát nghỉ cực đại: $f_s \le \mu_s n_2$. Do đó:

$$
\mu_s \ge \frac{f_s}{n_2} = \frac{267{,}5}{980} = 0{,}27
$$

Hệ số ma sát nghỉ tối thiểu cần thiết để giữ thang không trượt là $\mu_{s,\min} = 0{,}27$.

**(c) Lực tiếp xúc tổng hợp tại chân thang**:
Lực tiếp xúc tổng hợp $\vec{F}_B$ là hợp lực của phản lực pháp tuyến và lực ma sát nghỉ (Hình 11.9c):

$$
\vec{F}_B = f_s \hat{i} + n_2 \hat{j}
$$

Độ lớn của lực tiếp xúc:

$$
F_B = \sqrt{f_s^2 + n_2^2}
$$

$$
F_B = \sqrt{267{,}5^2 + 980^2}
$$

$$
F_B = 1020\,\text{N}
$$

Góc $\theta_B$ mà lực tiếp xúc hợp với phương nằm ngang được tính qua hàm lượng giác:

$$
\tan\theta_B = \frac{980}{267{,}5} = 3{,}66
$$

$$
\theta_B = 75^\circ
$$

**Đánh giá và kiểm tra**:
Quan sát Hình 11.9c cho thấy góc của lực tiếp xúc là $75^\circ$, lớn hơn đáng kể so với góc nghiêng $53{,}1^\circ$ của thân thang. Lực tiếp xúc tại chân thang tuyệt đối **không** hướng dọc theo thân thang. Nếu lực tiếp xúc hướng dọc theo thân thang, mômen tổng hợp đối với đầu thang sẽ không thể triệt tiêu.

Khi hiệp sĩ Lancelot tiếp tục trèo lên cao hơn, cánh tay đòn của trọng lượng hiệp sĩ đối với chân thang tăng dần lên, làm mômen lực lật tăng lên. Điều này đòi hỏi lực pháp tuyến $n_1$ của tường và lực ma sát nghỉ $f_s$ ở chân thang cũng phải tăng theo tương ứng. Do đó, hệ số ma sát yêu cầu sẽ càng ngày càng lớn và nguy cơ chiếc thang bị trượt càng tăng lên khi người leo lên các bậc thang phía trên.
:::

### Kết Cấu Siêu Tĩnh

Trong các ví dụ trên, số lượng ẩn số lực luôn bằng ba, vừa đúng bằng số phương trình cân bằng độc lập trong mặt phẳng. Tuy nhiên, trong đời sống thực tế ta thường gặp các hệ chịu lực có số lượng liên kết vượt quá số phương trình cân bằng.

Một ví dụ điển hình là chiếc bàn bốn chân đặt trên sàn nhà: Mỗi chân bàn chịu một phản lực pháp tuyến thẳng đứng từ mặt sàn, tổng cộng có bốn ẩn số lực. Thế nhưng trong không gian ba chiều, đối với hệ các lực song song chỉ có duy nhất ba phương trình cân bằng độc lập ($\sum F_y = 0$, $\sum \tau_x = 0$, $\sum \tau_z = 0$). Ba phương trình này không thể cho phép xác định duy nhất độ lớn lực tác dụng lên từng chân bàn riêng biệt. Một chiếc chân bàn bị hụt vài phần mười milimét có thể không chịu chút lực nào, trong khi ba chân còn lại gánh toàn bộ tải trọng.

Những cấu trúc như vậy được gọi là **kết cấu siêu tĩnh** (statically indeterminate structures). Để giải quyết trọn vẹn bài toán siêu tĩnh, mô hình vật rắn lý tưởng hoàn toàn bất lực. Ta bắt buộc phải từ bỏ giả thiết vật rắn tuyệt đối để chuyển sang khảo sát tính chất đàn hồi và biến dạng vi mô của từng bộ phận cấu trúc.

![](../img/young-11/a-hinh-11-10.png)

*Hình 11.10: Mô hình cơ học cánh tay người nâng quả tạ: (a) Cẳng tay nằm ngang chịu lực; (b) Sơ đồ vật tự do của cẳng tay, khoảng cách D được vẽ phóng đại để nhìn rõ các lực.*

::: example Ví dụ 11.4: Cân bằng cơ học khi tập tạ tay
Hình 11.10a mô tả một cánh tay người đang giữ một quả tạ ở tư thế cẳng tay nằm ngang. Cẳng tay ở trạng thái cân bằng tĩnh dưới tác dụng của ba lực: Trọng lượng $\vec{w}$ của quả tạ đặt tại bàn tay, lực căng $\vec{T}$ của gân cơ bắp tay nối với cơ nhị đầu kéo nghiêng một góc $\theta$ so với phương ngang, và lực tiếp xúc $\vec{E}$ do xương cánh tay trên tác dụng lên xương cẳng tay tại ổ khớp khuỷu tay. Bỏ qua trọng lượng của bản thân cẳng tay. Cho biết trọng lượng quả tạ $w$, góc nghiêng $\theta$, khoảng cách từ khớp khuỷu tay đến quả tạ là $L$, và khoảng cách từ khớp khuỷu tay đến điểm bám $A$ của gân cơ là $D$. Hãy tìm lực căng $T$ và hai thành phần lực $E_x, E_y$ do ổ khớp tác dụng lên cẳng tay.

**Tóm tắt**:
- Cẳng tay nằm ngang cân bằng.
- Trọng lượng tạ $w$ ở khoảng cách $L$ từ khuỷu tay.
- Gân cơ bám ở khoảng cách $D$, nghiêng góc $\theta$.
- Bỏ qua trọng lượng cẳng tay.
- Ẩn số: Lực căng $T$ và các thành phần $E_x, E_y$.

**Hướng đi**:
- Phân tích lực căng $\vec{T}$ và lực khớp $\vec{E}$ thành các thành phần nằm ngang và thẳng đứng (Hình 11.10b).
- Chọn khớp khuỷu tay làm điểm quy chiếu để tính mômen lực. Phương trình mômen quanh khớp khuỷu tay sẽ triệt tiêu hoàn toàn cả $E_x, E_y$ lẫn thành phần nằm ngang $T_x$, cho phép xác định trực tiếp $T$.
- Sau đó áp dụng điều kiện cân bằng lực để tìm $E_x$ và $E_y$.

**Các bước giải chi tiết**:
Sơ đồ vật tự do được vẽ trên Hình 11.10b. Các thành phần của lực căng gân cơ là:

$$
T_x = T \cos\theta
$$

$$
T_y = T \sin\theta
$$

Lấy mômen lực đối với khớp khuỷu tay (điểm quy chiếu $O$ tại ổ khớp):

$$
\tau_O = T_y D - w L = 0
$$

Thay $T_y = T \sin\theta$:

$$
(T \sin\theta) D - w L = 0
$$

Từ đó, ta tìm được biểu thức độ lớn lực căng của gân cơ:

$$
T = \frac{w L}{D \sin\theta}
$$

Áp dụng phương trình cân bằng lực theo phương nằm ngang:

$$
E_x + T \cos\theta = 0
$$

$$
E_x = -T \cos\theta
$$

Thay biểu thức của $T$ vừa tìm được vào:

$$
E_x = -\left(\frac{w L}{D \sin\theta}\right)\cos\theta
$$

$$
E_x = -\frac{w L}{D \tan\theta}
$$

Áp dụng phương trình cân bằng lực theo phương thẳng đứng:

$$
E_y + T_y - w = 0
$$

$$
E_y = w - T_y
$$

Vì từ phương trình mômen lực ta có $T_y = w L / D$:

$$
E_y = w - \frac{w L}{D}
$$

$$
E_y = -\left(\frac{L - D}{D}\right) w
$$

**Đánh giá và kiểm tra**:
Kết quả này mang lại những hiểu biết sinh cơ học hết sức sâu sắc:

- Vì điểm bám của gân cơ nằm rất sát khớp khuỷu tay nên $D$ nhỏ hơn rất nhiều so với chiều dài cẳng tay $L$ ($D \ll L$). Đồng thời góc nghiêng $\theta$ thường khá nhỏ nên $\sin\theta < 1$. Do đó, mẫu số $D \sin\theta$ rất bé so với tử số $w L$, khiến lực căng $T$ trong gân cơ bắp tay lớn hơn gấp nhiều lần trọng lượng $w$ của quả tạ. Chẳng hạn nếu $L = 35\,\text{cm}$, $D = 5\,\text{cm}$ và $\theta = 60^\circ$, lực căng gân cơ phải lên tới hơn $8$ lần trọng lượng quả tạ. Cơ bắp con người được cấu tạo để tạo ra các lực nội tại vô cùng lớn nhằm đổi lấy sự linh hoạt và phạm vi chuyển động rộng của bàn tay.
- Dấu âm xuất hiện trong biểu thức của $E_y$ chứng tỏ thành phần lực thẳng đứng này thực tế hướng thẳng xuống dưới, ngược với chiều giả định ban đầu. Xương cánh tay trên thực sự ép mạnh xuống cẳng tay tại ổ khớp khuỷu tay để ghì giữ cho cẳng tay không bị lật lên trên dưới tác dụng của lực kéo cực mạnh từ gân cơ nhị đầu.
:::

![](../img/young-11/a-hinh-11-11.png)

*Hình 11.11: Tấm biển quảng cáo gắn vào thanh ngang được nâng đỡ bởi dây cáp chéo và bản lề tại P.*

::: question Kiểm tra hiểu biết 11.3
Một tấm biển quảng cáo bằng kim loại có trọng lượng $w$ được treo cố định ở đầu mút của một thanh ngang có chiều dài $L$ và khối lượng không đáng kể (Hình 11.11). Thanh ngang được giữ thăng bằng bởi một sợi dây cáp chéo nối từ đầu thanh lên tường với góc nghiêng $\theta$ so với phương ngang, và một bản lề gắn vào tường tại điểm $P$. Hãy sắp xếp độ lớn của các lực sau đây theo thứ tự từ lớn nhất đến nhỏ nhất:

- (i) Trọng lượng $w$ của tấm biển quảng cáo.
- (ii) Lực căng $T$ trong sợi dây cáp chéo.
- (iii) Thành phần thẳng đứng của lực do bản lề tại $P$ tác dụng lên thanh.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án chính xác**: Thứ tự từ lớn đến nhỏ là (ii), (i), (iii).

**Giải thích chi tiết**:
Tình huống vật lý này hoàn toàn tương đương với mô hình ở Ví dụ 11.4, trong đó thanh ngang thay thế cho cẳng tay, bản lề $P$ thay thế cho khớp khuỷu tay, và dây cáp thay thế cho gân cơ nhị đầu. Điểm khác biệt duy nhất là điểm gắn của dây cáp nằm ở ngay đầu mút của thanh, do đó khoảng cách gắn cáp đúng bằng chiều dài thanh: $D = L$.

Vận dụng trực tiếp biểu thức lực căng từ Ví dụ 11.4 khi thay $D = L$:

$$
T = \frac{w L}{L \sin\theta} = \frac{w}{\sin\theta}
$$

Bởi vì góc nghiêng $0 < \theta < 90^\circ$ nên $\sin\theta < 1$. Do đó, lực căng trong dây cáp luôn lớn hơn trọng lượng của biển: $T > w$.

Thành phần thẳng đứng của lực do bản lề tác dụng lên thanh là:

$$
E_y = -\left(\frac{L - L}{L}\right) w = 0
$$

Như vậy, bản lề hoàn toàn không tác dụng lực thẳng đứng nào lên thanh ngang ($E_y = 0$). Để nhìn thấy điều này một cách trực quan, ta hãy tính mômen lực đối với điểm đầu mút bên phải của thanh: Tại điểm này, đường tác dụng của cả trọng lực $w$ lẫn lực căng dây cáp $T$ đều đi qua trục quay, do đó mômen của chúng đều bằng không. Lực duy nhất có thể gây ra mômen quanh đầu mút bên phải chính là thành phần thẳng đứng $E_y$ của bản lề. Để thanh cân bằng thì mômen này bắt buộc phải triệt tiêu, đồng nghĩa với việc $E_y = 0$.

Kết luận: Thứ tự độ lớn từ lớn nhất đến nhỏ nhất là lực căng dây cáp $T$, tiếp theo là trọng lượng biển $w$, và nhỏ nhất là thành phần lực thẳng đứng của bản lề $E_y = 0$. Tức là thứ tự (ii), (i), (iii).

</details>
:::
