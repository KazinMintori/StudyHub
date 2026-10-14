## 32.1. Phương trình Maxwell và sóng điện từ

Trong các chương trước, chúng ta đã nghiên cứu các khía cạnh khác nhau của điện trường và từ trường. Khi các trường không đổi theo thời gian, chẳng hạn như điện trường tĩnh do điện tích đứng yên tạo ra hoặc từ trường của dòng điện không đổi, ta có thể phân tích điện trường và từ trường một cách hoàn toàn độc lập mà không cần xét đến tương tác giữa chúng. Tuy nhiên, khi các trường biến thiên theo thời gian, chúng không còn độc lập nữa.

Định luật Faraday chỉ ra rằng: Một từ trường biến thiên theo thời gian đóng vai trò là nguồn sinh ra điện trường xoáy, thể hiện qua suất điện động cảm ứng trong các cuộn cảm và máy biến áp. Ngược lại, định luật Ampere với số hạng dòng điện dịch do James Clerk Maxwell bổ sung chỉ ra rằng: Một điện trường biến thiên theo thời gian đóng vai trò là nguồn sinh ra từ trường xoáy. Sự tương tác tương hỗ qua lại này giữa hai trường được tổng kết trọn vẹn trong hệ phương trình Maxwell.

Do đó, khi điện trường hoặc từ trường biến thiên theo thời gian trong một vùng không gian, một trường thuộc loại kia được cảm ứng sinh ra ở các vùng không gian lân cận. Từ đó, ta dự đoán có một nhiễu loạn gồm hai trường biến thiên có thể lan truyền từ vùng này sang vùng khác, ngay cả trong chân không. Maxwell đã đi tới dự đoán ấy khi xây dựng lý thuyết điện từ. Nhiễu loạn lan truyền như vậy mang đầy đủ tính chất của một quá trình sóng, và thuật ngữ chính xác được gọi là **sóng điện từ**.

Sóng điện từ thực sự tồn tại trong tự nhiên. Sóng vô tuyến, truyền hình, ánh sáng nhìn thấy, tia X và nhiều dạng bức xạ khác đều là những minh chứng cụ thể. Trọng tâm của mục này là làm sáng tỏ cách các nguyên lý điện từ học giải thích sự xuất hiện của sóng điện từ, đồng thời khảo sát các tính chất nền tảng của chúng.

### Mối liên hệ giữa điện, từ và ánh sáng

Tiến trình hiểu biết lý thuyết về sóng điện từ trong lịch sử trải qua một bước ngoặt. Vào đầu thế kỷ 19, vật lý học sử dụng hai hệ đơn vị đo điện tích hoàn toàn khác nhau: Một đơn vị dùng cho các hiện tượng tĩnh điện, và một đơn vị khác dùng cho các hiện tượng từ gắn với dòng điện. Trong hệ đo lường thời kỳ đó, hai đơn vị điện tích này có thứ nguyên vật lý khác nhau. Tỉ số giữa chúng mang thứ nguyên của vận tốc, và các phép đo thực nghiệm đã đem lại một giá trị phù hợp với vận tốc ánh sáng: $3{,}00 \times 10^8\,\mathrm{m/s}$. Ở thời điểm đó, các nhà vật lý chỉ xem đây là một sự trùng hợp kỳ lạ mà chưa thể tìm ra lời giải thích thỏa đáng.

Trong nỗ lực làm sáng tỏ bản chất của kết quả này, năm 1865, James Clerk Maxwell đã chứng minh bằng lý thuyết rằng một nhiễu loạn điện từ lan truyền trong chân không với tốc độ đúng bằng tốc độ ánh sáng. Từ đó, ông đưa ra kết luận mang tính thời đại: Ánh sáng bản chất là một dạng sóng điện từ.

Đồng thời, Maxwell nhận thấy rằng toàn bộ các định luật nền tảng của điện từ học có thể được phát biểu cô đọng thông qua bốn phương trình, ngày nay mang tên hệ phương trình Maxwell. Bốn phương trình này bao gồm: (1) Định luật Gauss cho điện trường, (2) Định luật Gauss cho từ trường khẳng định sự không tồn tại của đơn cực từ, (3) Định luật cảm ứng Faraday, và (4) Định luật Ampere mở rộng có dòng điện dịch:

$$
\begin{aligned}
\oint \vec{E} \cdot d\vec{A} &= \frac{Q_{\text{encl}}}{\epsilon_0},
\end{aligned}
\tag{29.18}
$$

$$
\begin{aligned}
\oint \vec{B} \cdot d\vec{A} &= 0,
\end{aligned}
\tag{29.19}
$$

$$
\begin{aligned}
\oint \vec{E} \cdot d\vec{l} &= -\frac{d\Phi_B}{dt},
\end{aligned}
\tag{29.20}
$$

$$
\begin{aligned}
\oint \vec{B} \cdot d\vec{l} &= \mu_0 \big( i_{\text{C}} \\
&\quad + \epsilon_0 \frac{d\Phi_E}{dt} \big)_{\text{encl}}.
\end{aligned}
\tag{29.21}
$$

Các tích phân Gauss được lấy trên mặt kín, với pháp tuyến hướng ra ngoài. $Q_{\text{encl}}$ là điện tích bên trong mặt đó. Hai tích phân lưu thông được lấy trên đường kín, với chiều đường và pháp tuyến mặt căng tuân quy tắc bàn tay phải. $\Phi_E$ và $\Phi_B$ là thông lượng qua mặt căng, còn $i_{\mathrm C}$ là dòng dẫn xuyên mặt.

Trong vật liệu tuyến tính, đồng nhất, đẳng hướng và không tổn hao, có thể dùng độ điện thẩm $\epsilon$ và độ từ thẩm $\mu$ thay các hằng số chân không, với điện tích và dòng dẫn tự do tương ứng. Gần đúng này xét tại tần số của sóng, bỏ qua tán sắc trong miền đang dùng.

Nếu hằng số vật liệu thay đổi theo vị trí, chúng phải nằm bên trong tích phân. Đặt $\vec D=\epsilon\vec E$ và $\vec H=\vec B/\mu$. Dạng thích hợp là:

$$
\begin{aligned}
&\oint\epsilon\vec E\cdot d\vec A=Q_{\mathrm f},\\
&\oint\frac{\vec B}{\mu}\cdot d\vec l\\
&=i_{\mathrm f}
 +\frac{d}{dt}\int\epsilon\vec E\cdot d\vec A.
\end{aligned}
$$

Ở đây $Q_{\mathrm f}$ và $i_{\mathrm f}$ lần lượt là điện tích và dòng tự do. Do đó, không kéo $\epsilon$ hoặc $\mu$ ra ngoài tích phân khi chúng không đồng nhất trên miền tích phân. Faraday và định luật Gauss cho từ trường vẫn giữ nguyên dạng.

![Hình 32.1: Nhà vật lý người Scotland James Clerk Maxwell (1831–1879), người giải thích bản chất điện từ của ánh sáng. Ông cũng có đóng góp lớn cho nhiệt động lực học, quang học, thiên văn học và nhiếp ảnh màu.](../img/young-32/hinh-32-01.png)

Albert Einstein từng đánh giá những cống hiến khoa học của Maxwell là thành tựu sâu sắc nhất và đem lại nhiều kết quả phong phú nhất mà nền vật lý học từng đạt được kể từ thời đại của Newton.

### Cơ chế phát bức xạ điện từ

Căn cứ vào hệ phương trình Maxwell, một điện tích điểm đứng yên chỉ sinh ra điện trường tĩnh mà không sinh ra từ trường. Khi một điện tích điểm chuyển động thẳng đều với vận tốc không đổi, nó tạo ra cả điện trường và từ trường, nhưng các trường này di chuyển cùng điện tích và không tách rời ra để tạo thành sóng truyền đi xa. Hệ phương trình Maxwell chỉ ra một điều kiện tiên quyết: Để một điện tích điểm có thể phát ra sóng điện từ, điện tích đó bắt buộc phải chuyển động có gia tốc. Thực tế chứng minh rằng trong mọi trường hợp có năng lượng điện từ bức xạ ra không gian, nguồn phát luôn luôn là các điện tích chuyển động có gia tốc.

![Hình 32.2: Trong phần (a), điện thoại di động truyền thông tin nhờ sóng điện từ phát ra từ các electron gia tốc trong mạch điện. (b) Dòng điện xoay chiều cường độ lớn trong đường dây tải điện làm các điện tích liên tục gia tốc đổi chiều, phát ra sóng điện từ gây tiếng ù trên đài radio ô tô khi đi gần.](../img/young-32/hinh-32-02.png)

Một phương thức cơ bản để khiến điện tích điểm phát sóng điện từ là kích thích cho nó dao động điều hòa. Khi dao động điều hòa, điện tích luôn có gia tốc ở hầu như mọi thời điểm, ngoại trừ những thời điểm nó đi qua vị trí cân bằng.

![Hình 32.3: Đường sức điện trường của điện tích dao động điều hòa tại năm thời điểm trong một chu kỳ T. Quỹ đạo điện tích nằm trong mặt phẳng hình vẽ. Ban đầu điện tích ở biên trên. Các mũi tên chỉ nếp uốn của đường sức truyền ra xa. Từ trường không được vẽ có các đường sức tròn, nằm trong các mặt phẳng vuông góc hình và có tâm trên trục dao động.](../img/young-32/hinh-32-03.png)

Đường sức điện trường không phải là các vật thể vật chất, nhưng ta có thể hình dung trực quan rằng chúng ứng xử tương tự như các sợi dây đàn hồi xuất phát từ điện tích điểm kéo dài vô tận ra không gian. Khi điện tích dao động lên xuống, các nếp uốn lượn được tạo ra và truyền dọc theo các đường sức này ra xa điện tích. Cần lưu ý rằng điện tích không phát sóng đồng đều theo mọi hướng: Cường độ sóng đạt giá trị cực đại theo phương vuông góc với trục dao động của điện tích, và hoàn toàn triệt tiêu dọc theo chính trục dao động. Đồng thời, một nhiễu loạn từ trường với các đường sức từ khép kín bao quanh trục dao động cũng lan truyền ra ngoài đồng bộ với điện trường. Do các nhiễu loạn điện và từ lan tỏa ra xa khỏi nguồn phát, thuật ngữ **bức xạ điện từ** được sử dụng hoán đổi đồng nghĩa với khái niệm **sóng điện từ**.

Sóng điện từ có bước sóng vĩ mô lần đầu tiên được tạo ra và kiểm chứng trong phòng thí nghiệm vào năm 1887 bởi nhà vật lý người Đức Heinrich Hertz. Để tạo nguồn sóng, ông sử dụng các điện tích dao động trong mạch LC. Sau đó, ông phát hiện sóng điện từ tạo thành bằng các mạch thu khác được điều chỉnh cộng hưởng ở cùng tần số. Hertz đã tạo ra sóng dừng điện từ, đo khoảng cách giữa hai nút sóng liền kề (bằng nửa bước sóng) để xác định bước sóng $\lambda$. Biết tần số cộng hưởng $f$ của mạch, ông tính được vận tốc truyền sóng theo hệ thức $v = \lambda f$ và xác nhận vận tốc này trùng khớp hoàn toàn với vận tốc ánh sáng, đem lại bằng chứng thực nghiệm trực tiếp khẳng định tiên đoán lý thuyết của Maxwell.

Giá trị chuẩn hiện đại của vận tốc ánh sáng trong chân không là $c = 299\,792\,458\,\mathrm{m/s}$. Đó là cơ sở định nghĩa độ dài tiêu chuẩn của một mét: Một mét là quãng đường ánh sáng truyền được trong khoảng thời gian $1/299\,792\,458$ giây. Trong hầu hết các bài toán tính toán thông thường, giá trị gần đúng $c = 3{,}00 \times 10^8\,\mathrm{m/s}$ có độ chính xác hoàn toàn thỏa đáng.

Tiếp nối phát hiện của Hertz, Guglielmo Marconi cùng nhiều nhà phát minh khác đã phát triển công nghệ truyền thông vô tuyến. Trong máy phát radio, các điện tích được điều khiển dao động dọc theo chiều dài của ăng-ten kim loại dẫn điện, tạo ra các trường nhiễu loạn bức xạ ra không gian xung quanh. Do có một lượng rất lớn electron cùng dao động đồng pha trong ăng-ten, sóng bức xạ có năng lượng lớn hơn rất nhiều so với một điện tích đơn lẻ và có thể truyền đi khoảng cách xa. Tại máy thu, ăng-ten cũng là một vật dẫn. Các trường của sóng tới tác dụng lực lên electron tự do, tạo dòng điện dao động. Mạch thu phát hiện, khuếch đại và xử lý dòng này thành tín hiệu.

### Thang sóng điện từ

Thang sóng điện từ bao trùm toàn bộ các sóng điện từ ở mọi tần số và bước sóng có thể có trong tự nhiên. Mặc dù có sự khác biệt rất lớn về cách thức tạo ra và ứng dụng thực tiễn, toàn bộ các bức xạ này đều có chung bản chất sóng điện từ và lan truyền trong chân không với cùng một tốc độ $c = 299\,792\,458\,\mathrm{m/s}$. Các sóng điện từ khác nhau về tần số $f$ và bước sóng $\lambda$, nhưng mối quan hệ nền tảng trong chân không luôn được thỏa mãn:

$$
\begin{aligned}
c &= \lambda f.
\end{aligned}
$$

![Hình 32.4: Thang sóng điện từ biểu diễn trên trục logarit đối với tần số và bước sóng. Ranh giới phân chia giữa các dải sóng mang tính quy ước tương đối.](../img/young-32/hinh-32-04.png)

Mắt người chỉ có thể cảm nhận trực tiếp một dải rất hẹp trong toàn bộ thang sóng điện từ, gọi là **ánh sáng nhìn thấy**. Dải này có bước sóng trải từ khoảng $380\,\mathrm{nm}$ đến $750\,\mathrm{nm}$ ($380 \times 10^{-9}\,\mathrm{m}$ đến $750 \times 10^{-9}\,\mathrm{m}$), tương ứng với tần số từ khoảng $790\,\mathrm{THz}$ đến $400\,\mathrm{THz}$ ($7{,}9 \times 10^{14}\,\mathrm{Hz}$ đến $4{,}0 \times 10^{14}\,\mathrm{Hz}$). Các vùng bước sóng khác nhau trong dải nhìn thấy kích thích thị giác con người tạo nên cảm nhận về các màu sắc khác nhau.

| Màu sắc | Dải bước sóng |
| :--- | :--- |
| Tím (Violet) | $380\text{–}450\,\mathrm{nm}$ |
| Lam (Blue) | $450\text{–}495\,\mathrm{nm}$ |
| Lục (Green) | $495\text{–}570\,\mathrm{nm}$ |
| Vàng (Yellow) | $570\text{–}590\,\mathrm{nm}$ |
| Da cam (Orange) | $590\text{–}620\,\mathrm{nm}$ |
| Đỏ (Red) | $620\text{–}750\,\mathrm{nm}$ |

Ánh sáng trắng thông thường chứa đồng thời mọi bước sóng trong vùng nhìn thấy. Bằng cách sử dụng các bộ lọc quang học hoặc nguồn phát chuyên dụng, ta có thể tách ra một dải bước sóng rất hẹp trong phạm vi vài nanomet, tạo ra ánh sáng gần đơn sắc. Một chùm sáng đơn sắc tuyệt đối chỉ gồm một bước sóng duy nhất là một sự lý tưởng hóa không thể đạt được trọn vẹn trong thực tế. Khi nói ánh sáng đơn sắc có bước sóng $550\,\mathrm{nm}$ trong một thí nghiệm, ta hiểu là một dải hẹp quanh $550\,\mathrm{nm}$. Ánh sáng phát ra từ nguồn laser có tính đơn sắc cao hơn rất nhiều so với bất kỳ nguồn sáng thông thường nào khác.

Các dạng sóng điện từ vô hình có tầm quan trọng không kém gì ánh sáng nhìn thấy:

- **Sóng vô tuyến**: Hệ thống truyền thông toàn cầu dựa vào sóng vô tuyến. Đài phát thanh điều biên (AM) sử dụng sóng có tần số từ $5{,}4 \times 10^5\,\mathrm{Hz}$ đến $1{,}6 \times 10^6\,\mathrm{Hz}$. Đài phát thanh điều tần (FM) phát ở dải tần cao hơn từ $8{,}8 \times 10^7\,\mathrm{Hz}$ đến $1{,}08 \times 10^8\,\mathrm{Hz}$.
- **Vi sóng**: Được sử dụng rộng rãi trong mạng di động không dây, Wi-Fi và hệ thống radar khí tượng ở các tần số gần $3 \times 10^9\,\mathrm{Hz}$.
- **Bức xạ hồng ngoại**: Nhiều máy ảnh hiện đại tích hợp bộ cảm biến phát chùm hồng ngoại: Bằng cách phân tích chùm tia phản xạ từ đối tượng, hệ thống tính toán khoảng cách và tự động điều chỉnh tiêu cự lấy nét.
- **Bức xạ tử ngoại**: Nhiều loài chim và côn trùng như ong mật có thể nhìn thấy bức xạ tử ngoại mà mắt người không thể quan sát được, hỗ trợ chúng định hướng tìm phấn hoa hoặc nhận diện bạn đời.
- **Tia X**: Có khả năng đâm xuyên qua mô mềm nhưng bị cản lại bởi xương và mô đặc, trở thành công cụ chẩn đoán không thể thiếu trong y học và nha khoa.
- **Tia gamma**: Là dạng bức xạ điện từ có bước sóng ngắn nhất và năng lượng photon cao nhất, phát ra từ phản ứng hạt nhân và được ứng dụng trong xạ trị y học để tiêu diệt các tế bào ung thư.

::: info Ứng dụng sinh học: Thị giác tử ngoại
Nhiều loài chim và côn trùng nhìn được bức xạ tử ngoại mà con người không thấy. Ảnh bên trái cho thấy hoa cúc mắt đen thuộc chi Rudbeckia dưới ánh sáng nhìn thấy. Ảnh bên phải được chụp bằng máy ảnh nhạy với tử ngoại và biểu diễn bằng màu giả.

Đốm nổi bật ở giữa hoa không hiện ra đối với mắt người nhưng giúp ong nhận biết nơi thụ phấn. Những loài chim có thị giác tử ngoại, như vẹt yến phụng, vẹt và công, cũng có thể nhận những hoa văn tử ngoại trên lông của nhau. Vì vậy, bộ lông có thể hiện nhiều chi tiết hơn đối với mắt chim so với mắt người.
:::

![Ứng dụng 32.1: Cùng một nhóm hoa dưới ánh sáng nhìn thấy và trong ảnh tử ngoại biểu diễn bằng màu giả.](../img/young-32/ung-dung-32-thi-giac-tu-ngoai.png)

### Câu hỏi tự kiểm tra 32.1

(a) Liệu có thể tồn tại một sóng thuần điện trường lan truyền qua chân không, tức là một sóng chỉ bao gồm điện trường biến thiên mà không có từ trường đi kèm?

(b) Liệu có thể tồn tại một sóng thuần từ trường, tức là một sóng chỉ bao gồm từ trường biến thiên mà không có điện trường đi kèm?

<details><summary>Xem đáp án và giải thích</summary>

(a) Không thể, và (b) cũng không thể.

Một sóng thuần điện trường đòi hỏi phải có điện trường biến thiên theo thời gian. Nhưng theo định luật Ampere mở rộng trong phương trình (29.21), một điện trường biến thiên theo thời gian bắt buộc phải sinh ra từ trường xoáy đi kèm. Vì vậy, một sóng thuần điện trường là điều không thể tồn tại trong tự nhiên.

Hoàn toàn tương tự, một sóng thuần từ trường cũng không thể tồn tại: Từ trường biến thiên theo thời gian trong sóng đó sẽ tự động sinh ra một điện trường xoáy đi kèm theo định luật cảm ứng Faraday trong phương trình (29.20). Do đó, điện trường và từ trường luôn gắn bó hữu cơ, tương hỗ và không thể tách rời trong sóng điện từ.

</details>
