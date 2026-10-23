## 11.4. Ứng Suất, Biến Dạng và Modun Đàn Hồi



Mô hình vật rắn tuyệt đối là một sự lý tưởng hóa hữu ích trong tĩnh học, nhưng trong thực tế, các vật thể không bao giờ cứng tuyệt đối. Mọi vật thể thực đều bị kéo dãn, nén ép hoặc xoắn vặn khi chịu tác dụng của ngoại lực. Các biến dạng này thường mang ý nghĩa kỹ thuật then chốt mà người kỹ sư không thể bỏ qua.



![Ba dạng biến dạng cơ bản](../img/young-11/b-hinh-11-12.png)



Hình 11.12: Ba dạng biến dạng cơ bản của vật thể dưới tác dụng của ngoại lực: (a) Dây đàn guitar chịu ứng suất kéo, bị dãn dài khi vặn trục lên dây; (b) Thân tàu ngầm chịu ứng suất khối dưới áp suất nén từ mọi phía của nước biển; (c) Dải ruy-băng chịu ứng suất trượt khi chịu hai lực song song tác dụng ngược chiều làm lệch các lớp vật liệu.



![Biến dạng khi bóp mũi](../img/young-11/b-hinh-11-13.png)



Hình 11.13: Khi bóp vào đầu mũi, lực tác dụng trên mỗi đơn vị diện tích nén các mô mềm được gọi là ứng suất. Biến dạng hình học sinh ra tương ứng được gọi là biến dạng đàn hồi.



### Khái Niệm Mở Đầu và Định Luật Hooke Tổng Quát



Khi một vật thể chịu tác dụng của các lực biến dạng, ta quan sát thấy hai đại lượng vật lý đặc trưng:

- **Ứng suất (Stress)**: Là đại lượng đo độ lớn của lực gây biến dạng tính trên một đơn vị diện tích bề mặt chịu lực.

- **Biến dạng (Strain)**: Là đại lượng đo mức độ biến dạng tương đối về mặt hình học của vật thể so với kích thước ban đầu. Biến dạng là tỉ số giữa hai đại lượng cùng thứ nguyên nên là một đại lượng không thứ nguyên.



Thực nghiệm cho thấy: Nếu lực tác dụng đủ nhỏ để biến dạng không vượt quá giới hạn đàn hồi của vật liệu, ứng suất luôn tỷ lệ thuận với biến dạng. Mối quan hệ này là dạng tổng quát của định luật Hooke:

$$

\frac{\text{Stress}}{\text{Strain}} = \text{Modulus}

\tag{11.7}

$$



Trong đó:

- Đại lượng ở tử số là ứng suất gây biến dạng.

- Đại lượng ở mẫu số là biến dạng tương đối sinh ra.

- Tỉ số giữa ứng suất và biến dạng được gọi là **modun đàn hồi** (Elastic modulus).



Modun đàn hồi đặc trưng cho bản chất của vật liệu cấu tạo nên vật thể, không phụ thuộc vào kích thước hay hình dạng hình học của vật. Một vật liệu có modun đàn hồi càng lớn thì càng cứng và càng khó bị biến dạng; để tạo ra cùng một độ biến dạng, vật liệu đó đòi hỏi một ứng suất lớn hơn nhiều so với vật liệu mềm.



Vì biến dạng là một số thuần túy không có thứ nguyên, đơn vị đo của modun đàn hồi trong hệ SI trùng với đơn vị của ứng suất: Đó là Newton trên mét vuông ($\text{N/m}^2$), được đặt tên là Pascal ($\text{Pa}$):

$$

1\text{ Pa} = 1\text{ N/m}^2

$$



Trong kỹ thuật cơ khí và công nghiệp, người ta cũng thường sử dụng các tiền tố lớn như Megapascal ($1\text{ MPa} = 10^6\text{ Pa}$) hoặc Gigapascal ($1\text{ GPa} = 10^9\text{ Pa}$). Trong hệ đo lường Anh–Mỹ, đơn vị của ứng suất là pound trên inch vuông ($\text{psi} = \text{lb/in}^2$):

$$

1\text{ psi} \approx 6895\text{ Pa}

$$



Dưới đây, ta sẽ lần lượt xem xét ba dạng ứng suất và biến dạng cơ bản: Ứng suất kéo – nén dọc trục, ứng suất khối và ứng suất trượt.



### Ứng Suất Kéo, Ứng Suất Nén và Modun Young



Hiện tượng biến dạng đàn hồi đơn giản nhất là sự kéo dãn dọc trục của một thanh vật liệu đồng chất.



![Thanh chịu ứng suất kéo](../img/young-11/b-hinh-11-14.png)



Hình 11.14: Vật thể chịu ứng suất kéo. Hai lực kéo cùng phương, ngược chiều và có cùng độ lớn $F_\perp$ tác dụng vuông góc lên hai mặt đáy có tiết diện $A$. Hợp lực tác dụng lên toàn vật bằng không nên vật đứng yên, nhưng vật bị biến dạng dãn dài từ chiều dài ban đầu $l_0$ thành $l = l_0 + \Delta l$.



Xét một thanh đồng chất có tiết diện ngang ban đầu là $A$ và chiều dài ban đầu $l_0$. Khi ta tác dụng vào hai đầu thanh hai lực kéo có cùng độ lớn $F_\perp$ theo phương dọc trục nhưng ngược chiều nhau: Hợp lực tác dụng lên thanh bằng không, do đó thanh không bị gia tốc chuyển động tịnh tiến. Tuy nhiên, liên kết nội tại giữa các phân tử bị kéo căng, khiến thanh dãn ra một đoạn $\Delta l$ và đạt chiều dài mới $l = l_0 + \Delta l$.



Ứng suất kéo (Tensile stress, ký hiệu $\sigma$) tại mỗi tiết diện ngang vuông góc với trục của thanh được định nghĩa là tỉ số giữa lực kéo vuông góc $F_\perp$ và diện tích tiết diện ngang $A$:

$$

\sigma = \frac{F_\perp}{A}

\tag{11.8}

$$



Biến dạng kéo (Tensile strain, ký hiệu $\epsilon$) được định nghĩa là độ dãn dài tỉ đối trên mỗi đơn vị chiều dài ban đầu của vật thể:

$$

\epsilon = \frac{l - l_0}{l_0} = \frac{\Delta l}{l_0}

\tag{11.9}

$$



Khi định luật Hooke được thỏa mãn, tỉ số giữa ứng suất kéo và biến dạng kéo là một hằng số đối với một vật liệu xác định. Hằng số tỷ lệ này được gọi là **modun Young**, ký hiệu là $Y$:

$$

Y = \frac{\sigma}{\epsilon} = \frac{F_\perp / A}{\Delta l / l_0}

$$

$$

Y = \frac{F_\perp l_0}{A \Delta l}

\tag{11.10}

$$



Từ công thức trên, ta có thể suy ra độ dãn dài $\Delta l$ của một thanh chịu kéo:

$$

\Delta l = \frac{F_\perp l_0}{A Y}

$$



![Vật thể chịu ứng suất nén](../img/young-11/b-hinh-11-15.png)



Hình 11.15: Vật thể chịu ứng suất nén. Các lực nén có độ lớn $F_\perp$ hướng vào trong ép lên hai mặt đầu có diện tích $A$. Độ co ngắn của thanh là khoảng dịch chuyển $\Delta l$, chiều dài thanh giảm từ $l_0$ xuống $l = l_0 - \Delta l$.



Khi các ngoại lực ở hai đầu thanh là lực đẩy hướng vào trong thay vì lực kéo ra ngoài, thanh bị nén dọc trục và chịu ứng suất nén (Compressive stress). Biến dạng nén (Compressive strain) được định nghĩa hoàn toàn tương tự biến dạng kéo, nhưng $\Delta l$ mang ý nghĩa là độ co ngắn lại của thanh: Chiều dài mới của thanh là $l = l_0 - \Delta l$.



Với đa số các vật liệu đồng chất và đẳng hướng (như thép, đồng thau, nhôm), định luật Hooke và công thức (11.10) nghiệm đúng cho cả trường hợp kéo lẫn nén với cùng một giá trị modun Young $Y$.



Tuy nhiên, có những vật liệu composite hoặc vật liệu giòn không thể hiện tính chất đối xứng này. Chẳng hạn, bê tông, gạch vữa và đá tự nhiên có khả năng chịu ứng suất nén cực kỳ tốt, nhưng lại rất dễ nứt vỡ khi chịu ứng suất kéo có độ lớn tương đương.



Chính vì lý do này, các nền văn minh cổ đại như người Babylon, Assyria và La Mã khi xây dựng các công trình bằng đá đã thiết kế kết cấu vòm (arch) cho các cửa sổ, cổng thành và cầu cống: Trọng lượng của các khối đá bên trên sẽ nén chặt các khối đá của vòm lại với nhau, biến ứng lực trong kết cấu thành lực nén thuần túy và triệt tiêu hoàn toàn ứng suất kéo gây gãy vỡ.



Bảng 11.1 dưới đây liệt kê các giá trị thực nghiệm tiêu biểu của modun Young $Y$, modun khối $B$ và modun trượt $S$ cho một số vật liệu thông dụng:



| Vật liệu | Modun Young $Y$ ($\text{Pa}$) | Modun khối $B$ ($\text{Pa}$) | Modun trượt $S$ ($\text{Pa}$) |

| :--- | :--- | :--- | :--- |

| Nhôm (Aluminum) | $7{,}0 \times 10^{10}$ | $7{,}5 \times 10^{10}$ | $2{,}5 \times 10^{10}$ |

| Đồng thau (Brass) | $9{,}0 \times 10^{10}$ | $6{,}0 \times 10^{10}$ | $3{,}5 \times 10^{10}$ |

| Đồng đỏ (Copper) | $11 \times 10^{10}$ | $14 \times 10^{10}$ | $4{,}4 \times 10^{10}$ |

| Sắt (Iron) | $21 \times 10^{10}$ | $16 \times 10^{10}$ | $7{,}7 \times 10^{10}$ |

| Chì (Lead) | $1{,}6 \times 10^{10}$ | $4{,}1 \times 10^{10}$ | $0{,}6 \times 10^{10}$ |

| Niken (Nickel) | $21 \times 10^{10}$ | $17 \times 10^{10}$ | $7{,}8 \times 10^{10}$ |

| Cao su silicone | $0{,}001 \times 10^{10}$ | $0{,}2 \times 10^{10}$ | $0{,}0002 \times 10^{10}$ |

| Thép (Steel) | $20 \times 10^{10}$ | $16 \times 10^{10}$ | $7{,}5 \times 10^{10}$ |

| Gân (Tendon, điển hình) | $0{,}12 \times 10^{10}$ | — | — |



![Gân chày trước](../img/young-11/b-ung-dung-11-gan-chan.png)



Ứng dụng sinh học: Modun Young của gân chày trước. Gân chày trước liên kết bàn chân với bó cơ lớn chạy dọc xương cẳng chân. Kết quả đo đạc thực nghiệm cho thấy gân này có modun Young khoảng $1{,}2 \times 10^9\text{ Pa}$, nhỏ hơn nhiều so với các kim loại trong Bảng 11.1. Nhờ đó, gân có thể dãn dài đáng kể (lên đến 2,5% chiều dài ban đầu) để tiêu tán và lưu trữ thế năng đàn hồi trong các hoạt động đi bộ và chạy nhảy.



![Dầm chịu uốn và mặt cắt dầm chữ I](../img/young-11/b-hinh-11-16.png)



Hình 11.16: Sự kết hợp giữa ứng suất nén và kéo trong kết cấu dầm: (a) Dầm chịu tải trọng uốn cong, dầm bị nén ở mặt trên và bị kéo ở mặt dưới, riêng trục trung hòa không chịu kéo cũng không chịu nén; (b) Mặt cắt dầm chữ I có hai bản biên rộng ở trên và dưới để chịu phần lớn ứng suất nén và kéo, phần bụng dầm mỏng giúp giảm tối đa trọng lượng kết cấu.



::: example Ví dụ 11.5: Ứng suất kéo, biến dạng và độ dãn dài của thanh thép

Một thanh thép dài $2{,}0\text{ m}$ có tiết diện ngang $0{,}30\text{ cm}^2$. Thanh được treo thẳng đứng từ một giá đỡ cố định ở đầu trên, và một chiếc máy phay có khối lượng $550\text{ kg}$ được móc vào đầu dưới của thanh. Hãy xác định ứng suất tác dụng lên thanh, biến dạng kéo tương ứng và độ dãn dài của thanh thép. Bỏ qua trọng lượng bản thân của thanh.



**Tóm tắt**:

- Chiều dài ban đầu: $l_0 = 2{,}0\text{ m}$.

- Tiết diện ngang: $A = 0{,}30\text{ cm}^2$ (tức $3{,}0 \times 10^{-5}\text{ m}^2$).

- Khối lượng máy móc: $m = 550\text{ kg}$.

- Gia tốc trọng trường: $g = 9{,}8\text{ m/s}^2$.

- Modun Young của thép (tra Bảng 11.1): $Y = 20 \times 10^{10}\text{ Pa}$.



**Hướng dẫn giải**:

- Thanh thép chịu ứng suất kéo dọc trục do trọng lượng của máy móc treo ở đầu dưới.

- Lực kéo tác dụng vuông góc lên mặt cắt ngang: $F_\perp = m g$.

- Tính ứng suất kéo theo công thức (11.8): $\sigma = F_\perp / A$.

- Tính biến dạng kéo từ định luật Hooke (11.10): $\epsilon = \sigma / Y$.

- Tính độ dãn dài của thanh: $\Delta l = \epsilon l_0$.



**Lời giải chi tiết**:

Trọng lượng của máy móc tác dụng lên thanh thép:

$$

F_\perp = m g

$$

$$

F_\perp = (550\text{ kg})(9{,}8\text{ m/s}^2)

$$

$$

F_\perp = 5390\text{ N}

$$



Ứng suất kéo tác dụng lên mặt cắt ngang của thanh:

$$

\sigma = \frac{F_\perp}{A}

$$

$$

\sigma = \frac{5390\text{ N}}{3{,}0 \times 10^{-5}\text{ m}^2}

$$

$$

\sigma \approx 1{,}8 \times 10^8\text{ Pa}

$$



Biến dạng kéo dọc trục của thanh:

$$

\epsilon = \frac{\sigma}{Y}

$$

$$

\epsilon = \frac{1{,}8 \times 10^8\text{ Pa}}{20 \times 10^{10}\text{ Pa}}

$$

$$

\epsilon = 9{,}0 \times 10^{-4}

$$



Độ dãn dài tổng cộng của thanh:

$$

\Delta l = \epsilon l_0

$$

$$

\Delta l = (9{,}0 \times 10^{-4})(2{,}0\text{ m})

$$

$$

\Delta l = 1{,}8 \times 10^{-3}\text{ m}

$$

Giá trị này tương đương với $1{,}8\text{ mm}$.



**Đánh giá**: Độ dãn dài chỉ $1{,}8\text{ mm}$ dưới tải trọng hơn nửa tấn là minh chứng rõ ràng cho độ cứng vững của vật liệu thép. Trọng lượng bản thân của thanh thép chỉ khoảng $4{,}7\text{ kg}$, rất nhỏ so với tải trọng $550\text{ kg}$ nên việc bỏ qua nó là hoàn toàn chính xác.

:::



### Ứng Suất Khối, Biến Dạng Khối và Modun Khối



Khi một vật thể ngập sâu trong một chất lưu (chất lỏng hoặc chất khí), chất lưu tác dụng lực ép vuông góc lên toàn bộ bề mặt của vật thể từ mọi hướng.



Lực ép vuông góc trên một đơn vị diện tích tại một điểm trong chất lưu được gọi là **áp suất** (Pressure), ký hiệu là $p$:

$$

p = \frac{F_\perp}{A}

\tag{11.11}

$$



Đơn vị của áp suất trong hệ SI là Pascal ($\text{Pa}$). Một đơn vị áp suất quen thuộc khác trong khí quyển học là atmosphere ($\text{atm}$):

$$

1\text{ atm} = 1{,}013 \times 10^5\text{ Pa}

$$

$$

1\text{ atm} \approx 14{,}7\text{ lb/in}^2

$$



![Vật thể chịu ứng suất khối](../img/young-11/b-hinh-11-17.png)



Hình 11.17: Vật thể chịu ứng suất khối. Khi áp suất môi trường tăng từ $p_0$ lên $p = p_0 + \Delta p$, các lực vuông góc $F_\perp$ phân bố đều nén vật từ mọi phía. Thể tích của vật thể giảm từ thể tích ban đầu $V_0$ xuống thể tích mới $V = V_0 + \Delta V$ (với $\Delta V < 0$).



Khi áp suất tác dụng lên vật thể thay đổi một lượng $\Delta p = p - p_0$, lượng biến thiên áp suất này đóng vai trò là **ứng suất khối** (Bulk stress):

$$

\text{Bulk stress} = \Delta p

$$



Dưới tác dụng của ứng suất khối, thể tích của vật thể thay đổi một lượng $\Delta V$. **Biến dạng khối** (Bulk strain) được định nghĩa là độ biến thiên thể tích tỉ đối so với thể tích ban đầu $V_0$:

$$

\text{Bulk strain} = \frac{\Delta V}{V_0}

\tag{11.12}

$$



Khi định luật Hooke được thỏa mãn, biến dạng khối tỷ lệ thuận với ứng suất khối. Modun đàn hồi tương ứng được gọi là **modun khối** (Bulk modulus), ký hiệu là $B$:

$$

B = -\frac{\text{Bulk stress}}{\text{Bulk strain}}

$$

$$

B = -\frac{\Delta p}{\Delta V / V_0}

\tag{11.13}

$$



Dấu trừ trong công thức (11.13) xuất hiện vì khi áp suất tăng ($\Delta p > 0$), thể tích của vật thể bị ép co lại ($\Delta V < 0$). Dấu trừ này đảm bảo cho modun khối $B$ luôn là một đại lượng dương.



Nghịch đảo của modun khối được gọi là **độ nén** (Compressibility), ký hiệu là $k$:

$$

k = \frac{1}{B} = -\frac{1}{V_0} \frac{\Delta V}{\Delta p}

\tag{11.14}

$$



Đơn vị của độ nén $k$ là nghịch đảo của áp suất: $\text{Pa}^{-1}$ hoặc $\text{atm}^{-1}$. Vật liệu nào có modun khối $B$ càng nhỏ thì độ nén $k$ càng lớn, đồng nghĩa với việc vật liệu đó càng dễ bị nén ép lại dưới áp suất cao.



Bảng 11.2 liệt kê giá trị độ nén $k$ của một số chất lỏng phổ biến ở nhiệt độ phòng:



| Chất lỏng | Độ nén $k$ ($\text{Pa}^{-1}$) | Độ nén $k$ ($\text{atm}^{-1}$) |

| :--- | :--- | :--- |

| Cacbon đisunfua ($\text{CS}_2$) | $93 \times 10^{-11}$ | $94 \times 10^{-6}$ |

| Rượu etylic ($\text{C}_2\text{H}_5\text{OH}$) | $110 \times 10^{-11}$ | $111 \times 10^{-6}$ |

| Glyxerin | $21 \times 10^{-11}$ | $21 \times 10^{-6}$ |

| Thủy ngân | $3{,}7 \times 10^{-11}$ | $3{,}8 \times 10^{-6}$ |

| Nước | $45{,}8 \times 10^{-11}$ | $46{,}4 \times 10^{-6}$ |



Chẳng hạn, độ nén của nước là $46{,}4 \times 10^{-6}\text{ atm}^{-1}$, nghĩa là cứ mỗi khi áp suất tăng thêm $1\text{ atm}$, thể tích nước chỉ giảm đi $46{,}4$ phần triệu ($0{,}00464\%$). Do đó, trong hầu hết các bài toán thủy lực thông thường, nước và các chất lỏng có thể xem là gần như không nén được.



![Cá cần câu biển sâu Melanocetus johnsonii](../img/young-11/b-ung-dung-11-ca-can-cau.png)



Ứng dụng sinh học: Ứng suất khối tác dụng lên cá cần câu (*Melanocetus johnsonii*). Loài cá này sinh sống ở độ sâu tới $1000\text{ m}$ dưới đáy đại dương, nơi áp suất chất lỏng đạt xấp xỉ $100\text{ atm}$. Cá cần câu chịu được ứng suất khối cực lớn này nhờ cơ thể không chứa các khoang khí bên trong (như bóng hơi), khác biệt hoàn toàn với các loài cá ở tầng nước nông. Những cá thể lớn nhất có chiều dài khoảng $12\text{ cm}$.



::: example Ví dụ 11.6: Ứng suất khối và biến dạng khối của dầu trong máy ép thủy lực

Một máy ép thủy lực chứa $0{,}25\text{ m}^3$ ($250\text{ L}$) dầu truyền động. Hãy tìm độ giảm thể tích của lượng dầu này khi áp suất trong hệ thống tăng thêm $\Delta p = 1{,}6 \times 10^7\text{ Pa}$ (tương đương khoảng $160\text{ atm}$ hay $2300\text{ psi}$). Biết rằng modun khối của dầu là $B = 5{,}0 \times 10^9\text{ Pa}$ (khoảng $5{,}0 \times 10^4\text{ atm}$), và độ nén tương ứng là $k = 1/B$ ( \times 10^{-6}\text{ atm}^{-1}$).



**Tóm tắt**:

- Thể tích ban đầu: $V_0 = 0{,}25\text{ m}^3$ ($250\text{ L}$).

- Độ tăng áp suất: $\Delta p = 1{,}6 \times 10^7\text{ Pa}$ (khoảng $160\text{ atm}$).

- Modun khối của dầu: $B = 5{,}0 \times 10^9\text{ Pa}$.



- Độ nén: $k = 20 \times 10^{-6}\text{ atm}^{-1}$.



**Hướng dẫn giải**:

- Bài toán yêu cầu tính độ biến thiên thể tích $\Delta V$ khi biết độ tăng áp suất và các thông số đàn hồi của chất lỏng.

- Ta có thể giải bằng hai cách tương đương: Sử dụng modun khối $B$ theo công thức (11.13) hoặc sử dụng độ nén $k$ theo công thức (11.14).



**Lời giải chi tiết**:

Cách 1: Sử dụng công thức định nghĩa modun khối (11.13):

$$

\Delta V = -\frac{V_0 \Delta p}{B}

$$


\Delta V = -\frac{(0{,}25)(1{,}6 \times 10^7)}{5{,}0 \times 10^9}



\Delta V = -8{,}0 \times 10^{-4}\text{ m}^3


Kết quả này tương đương với $-0{,}80\text{ L}$.



Cách 2: Sử dụng độ nén $k$ và đơn vị atmosphere:

$$

\Delta V = -k V_0 \Delta p

$$


\Delta V = -(20 \times 10^{-6})(40)



\Delta V = -8{,}0 \times 10^{-4}\text{ m}^3


Kết quả cũng tương đương với $-0{,}80\text{ L}$.



Độ giảm thể tích tỉ đối của khối dầu:

$$

\frac{\Delta V}{V_0} = \frac{-8{,}0 \times 10^{-4}}{0{,}25}

$$

$$

\frac{\Delta V}{V_0} = -0{,}0032

$$

Độ biến thiên thể tích này tương đương với mức giảm $-0{,}32\%$.



**Đánh giá**: Giá trị âm của $\Delta V$ khẳng định thể tích chất lỏng giảm đi khi áp suất tăng. Mặc dù áp suất tăng thêm $160\text{ atm}$ là một con số rất lớn trong thực tế, thể tích dầu chỉ giảm một lượng rất nhỏ $0{,}32\%$, chứng minh tính chất khó nén của dầu thủy lực.

:::



### Ứng Suất Trượt, Biến Dạng Trượt và Modun Trượt



Dạng ứng suất cơ bản thứ ba là ứng suất trượt (Shear stress). Dạng biến dạng này xuất hiện khi các ngoại lực tác dụng tiếp tuyến với các mặt ngoài của vật thể thay vì vuông góc.



![Vật thể chịu ứng suất trượt](../img/young-11/b-hinh-11-18.png)



Hình 11.18: Vật thể chịu ứng suất trượt. Hai lực tiếp tuyến có độ lớn $F_\parallel$ tác dụng song song với hai mặt đối diện có diện tích $A$. Khoảng cách vuông góc giữa hai mặt là $h$. Dưới tác dụng của ngẫu lực trượt, mặt trên bị dịch chuyển ngang một đoạn $x$ so với mặt đáy cố định, tạo thành góc trượt $\phi$.



Xét một khối hộp vật liệu có chiều cao $h$ giữa hai mặt đối diện, mỗi mặt có diện tích $A$. Ta đặt vào hai mặt đối diện này hai lực tiếp tuyến cùng độ lớn $F_\parallel$, ngược chiều nhau.



Ứng suất trượt (ký hiệu $\tau$) được định nghĩa là tỉ số giữa lực tiếp tuyến $F_\parallel$ và diện tích bề mặt $A$ mà lực đó tác dụng:

$$

\tau = \frac{F_\parallel}{A}

\tag{11.15}

$$



Dưới tác dụng của ứng suất trượt, mặt trên bị dịch chuyển một khoảng $x$ theo phương tiếp tuyến so với mặt đáy. Biến dạng trượt (ký hiệu $\gamma$) được định nghĩa là tỉ số giữa độ dịch chuyển ngang $x$ và khoảng cách vuông góc $h$ giữa hai mặt:

$$

\gamma = \frac{x}{h} = \tan\phi

\tag{11.16}

$$



Trong thực tế, khi các biến dạng là đàn hồi và nhỏ, góc lệch $\phi$ (tính bằng radian) rất nhỏ nên ta có thể lấy xấp xỉ $\tan\phi \approx \phi$. Do đó, biến dạng trượt cũng chính là góc trượt $\phi$ tính theo radian.



Tỉ số giữa ứng suất trượt và biến dạng trượt trong vùng đàn hồi được gọi là **modun trượt** (Shear modulus), ký hiệu là $S$:

$$

S = \frac{\tau}{\gamma} = \frac{F_\parallel / A}{x / h}

$$

$$

S = \frac{F_\parallel h}{A x}

\tag{11.17}

$$



Từ Bảng 11.1, ta nhận thấy rằng đối với hầu hết các vật liệu kim loại, modun trượt $S$ thường có độ lớn vào khoảng từ một phần ba đến một nửa modun Young $Y$:

$$

S \approx \frac{1}{3} Y \dots \frac{1}{2} Y

$$



Điều này cho thấy một vật thể thường dễ bị biến dạng trượt hoặc xoắn vặn hơn so với biến dạng kéo hoặc nén dọc trục.



::: example Ví dụ 11.7: Ứng suất trượt và lực cắt trong trận động đất

Một bức tượng điêu khắc ngoài trời được gắn chặt trên một tấm đế bằng đồng thau dày $0{,}50\text{ cm}$ và có dạng hình vuông cạnh $0{,}80\text{ m}$. Khi xảy ra động đất, bức tượng làm xuất hiện các lực trượt tác dụng lên các cạnh của tấm đế. Hãy tính độ lớn của lực tác dụng lên mỗi cạnh của tấm đế nếu độ dịch chuyển ngang $x$ đo được là $0{,}16\text{ mm}$.



**Tóm tắt**:

- Kích thước mặt vuông của tấm đế: $L = 0{,}80\text{ m}$, chiều cao $h = 0{,}80\text{ m}$.

- Độ dày của tấm đế: $t = 0{,}50\text{ cm}$ ($0{,}0050\text{ m}$).

- Độ dịch chuyển ngang: $x = 0{,}16\text{ mm}$ ($1{,}6 \times 10^{-4}\text{ m}$).

- Modun trượt của đồng thau (tra Bảng 11.1): $S = 3{,}5 \times 10^{10}\text{ Pa}$.



**Hướng dẫn giải**:

- Trong Hình 11.18, chiều cao giữa hai bề mặt chịu biến dạng trượt chính là chiều dài cạnh của tấm vuông: $h = 0{,}80\text{ m}$.

- Diện tích mặt chịu lực $A$ của mỗi cạnh bằng tích của chiều dài cạnh và độ dày tấm đế: $A = L \cdot t$.

- Tính biến dạng trượt theo công thức (11.16): $\gamma = x / h$.

- Tính ứng suất trượt cần thiết từ định luật Hooke (11.17): $\tau = \gamma S$.

- Suy ra lực cắt tiếp tuyến tác dụng lên mép cạnh: $F_\parallel = \tau A$.



**Lời giải chi tiết**:

Diện tích mặt cắt của mỗi mép cạnh tấm đế:

$$

A = L t

$$

$$

A = (0{,}80\text{ m})(0{,}0050\text{ m})

$$

$$

A = 4{,}0 \times 10^{-3}\text{ m}^2

$$



Biến dạng trượt sinh ra trên tấm đế:

$$

\gamma = \frac{x}{h}

$$

$$

\gamma = \frac{1{,}6 \times 10^{-4}\text{ m}}{0{,}80\text{ m}}

$$

$$

\gamma = 2{,}0 \times 10^{-4}

$$



Ứng suất trượt tương ứng trong vật liệu đồng thau:

$$

\tau = \gamma S

$$


\tau = (2{,}0 \times 10^{-4})(3{,}5 \times 10^{10})



\tau = 7{,}0 \times 10^6\text{ Pa}




Lực tiếp tuyến tác dụng lên mỗi cạnh của tấm đế:

$$

F_\parallel = \tau A

$$


F_\parallel = (7{,}0 \times 10^6)(4{,}0 \times 10^{-3})



F_\parallel = 2{,}8 \times 10^4\text{ N}




**Đánh giá**: Lực cắt sinh ra trong trận động đất lên tới $28\text{ kN}$ (tương đương trọng lượng của một vật nặng gần 3 tấn). Giá trị lực rất lớn này xuất phát từ hai yếu tố: Modun trượt của đồng thau rất lớn ($3{,}5 \times 10^{10}\text{ Pa}$) và tấm đế có tiết diện chịu cắt tương đối dày.

:::



### Kiểm Tra Mức Độ Hiểu Mục 11.4



Một thanh đồng có tiết diện ngang $0{,}500\text{ cm}^2$ và chiều dài $1{,}00\text{ m}$ bị kéo dãn một đoạn $2{,}00 \times 10^{-2}\text{ mm}$. Một thanh thép có cùng diện tích tiết diện ngang $0{,}500\text{ cm}^2$ nhưng chiều dài ban đầu chỉ là $0{,}100\text{ m}$ bị kéo dãn một đoạn $2{,}00 \times 10^{-3}\text{ mm}$.



(a) Thanh nào có biến dạng kéo lớn hơn?

- (i) Thanh đồng.

- (ii) Thanh thép.

- (iii) Biến dạng kéo của hai thanh là như nhau.



(b) Thanh nào chịu ứng suất kéo lớn hơn?

- (i) Thanh đồng.

- (ii) Thanh thép.

- (iii) Ứng suất kéo của hai thanh là như nhau.



<details>

<summary>Xem lời giải thích</summary>



**Đáp án**: (a) chọn phương án (iii); (b) chọn phương án (ii).



**Giải thích chi tiết**:

- Đối với câu (a):

Biến dạng kéo của thanh đồng:

$$

\begin{aligned}

\epsilon_{\text{Cu}} &= \frac{\Delta l_{\text{Cu}}}{l_{0,\text{Cu}}} \\

&= \frac{2{,}00 \times 10^{-5}\text{ m}}{1{,}00\text{ m}} \\

&= 2{,}00 \times 10^{-5}

\end{aligned}

$$

Biến dạng kéo của thanh thép:

$$

\begin{aligned}

\epsilon_{\text{steel}} &= \frac{\Delta l_{\text{steel}}}{l_{0,\text{steel}}} \\

&= \frac{2{,}00 \times 10^{-6}\text{ m}}{0{,}100\text{ m}} \\

&= 2{,}00 \times 10^{-5}

\end{aligned}

$$

Mặc dù thanh đồng có độ dãn dài $\Delta l$ lớn gấp 10 lần thanh thép, chiều dài ban đầu $l_0$ của nó cũng lớn gấp 10 lần. Do đó, tỉ số $\Delta l / l_0$ của hai thanh hoàn toàn bằng nhau. Vì vậy, biến dạng kéo của hai thanh là như nhau.



- Đối với câu (b):

Theo định luật Hooke, ứng suất kéo liên hệ với biến dạng kéo qua modun Young:

$$

\sigma = Y \epsilon

$$

Tra cứu Bảng 11.1, ta có:

$$

Y_{\text{steel}} = 20 \times 10^{10}\text{ Pa}

$$

$$

Y_{\text{Cu}} = 11 \times 10^{10}\text{ Pa}

$$

Vì thép có modun Young lớn hơn đồng ($Y_{\text{steel}} > Y_{\text{Cu}}$) trong khi biến dạng kéo của hai thanh là như nhau:


\sigma_{\text{steel}} = Y_{\text{steel}} \epsilon_{\text{steel}}



\sigma_{\text{steel}} = (20 \times 10^{10})(2{,}00 \times 10^{-5})



\sigma_{\text{steel}} = 4{,}0 \times 10^6\text{ Pa}



\sigma_{\text{Cu}} = Y_{\text{Cu}} \epsilon_{\text{Cu}}



\sigma_{\text{Cu}} = (11 \times 10^{10})(2{,}00 \times 10^{-5})



\sigma_{\text{Cu}} = 2{,}2 \times 10^6\text{ Pa}


Thanh thép chịu ứng suất kéo lớn hơn đáng kể so với thanh đồng để tạo ra cùng một tỉ lệ dãn dài.

</details>
