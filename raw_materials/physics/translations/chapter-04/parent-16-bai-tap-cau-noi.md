### Bài tập cầu nối: Mắt xích của một sợi xích (Links in a Chain)

Một sinh viên treo một sợi xích gồm ba mắt xích, mỗi mắt xích có khối lượng $m = 0{,}250\,\mathrm{kg}$, từ một sợi dây nhẹ. Sợi dây được buộc vào mắt xích trên cùng của chuỗi, và sợi xích không đung đưa. Cô sinh viên kéo sợi dây thẳng đứng lên phía trên, sao cho sợi dây tác dụng một lực kéo hướng lên có độ lớn $9{,}00\,\mathrm N$ lên sợi xích.
(a) Vẽ sơ đồ vật thể tự do cho toàn bộ sợi xích (xem như một vật thể duy nhất), và vẽ sơ đồ vật thể tự do cho từng mắt xích trong số ba mắt xích riêng biệt.
(b) Sử dụng các sơ đồ ở phần (a) cùng các định luật Newton để tìm:
(i) Gia tốc của sợi xích.
(ii) Lực do mắt xích trên cùng tác dụng lên mắt xích ở giữa.
(iii) Lực do mắt xích ở giữa tác dụng lên mắt xích dưới cùng.
Xem sợi dây là không có khối lượng.

#### Hướng dẫn giải (Solution Guide)

**Nhận diện và thiết lập (Identify and Set Up):**
1. Có bốn đối tượng được quan tâm trong bài toán này: Toàn bộ sợi xích xét như một thể thống nhất và ba mắt xích riêng lẻ. Đối với mỗi đối tượng trong số bốn đối tượng này, hãy liệt kê tất cả các ngoại lực tác dụng lên nó. Ngoại trừ lực hấp dẫn (trọng lực), danh sách lực của bạn chỉ được bao gồm các lực do những vật thể khác tiếp xúc trực tiếp với đối tượng đó tác dụng.
2. Một số lực trong danh sách của bạn tạo thành các cặp lực trực đối tác dụng và phản tác dụng theo định luật III Newton (chẳng hạn một cặp gồm lực do mắt xích trên tác dụng lên mắt xích giữa và lực do mắt xích giữa tác dụng ngược lại lên mắt xích trên). Hãy xác định tất cả các cặp lực trực đối như vậy.
3. Sử dụng các danh sách lực đã lập để vẽ sơ đồ vật thể tự do cho từng đối tượng trong số bốn đối tượng. Chọn hệ trục tọa độ phù hợp.
4. Dựa vào danh sách lực để xác định bài toán có bao nhiêu ẩn số cần tìm. Những ẩn số nào là các biến mục tiêu của bài toán?

**Thực hiện (Execute):**
5. Viết phương trình định luật II Newton cho từng đối tượng trong số bốn đối tượng, và viết phương trình định luật III Newton cho từng cặp lực tác dụng - phản tác dụng. Bạn cần có số phương trình độc lập ít nhất bằng số lượng ẩn số (đã xác định ở bước 4).
6. Giải hệ phương trình để tìm giá trị của các biến mục tiêu.

**Đánh giá (Evaluate):**
7. Bạn có thể kiểm tra kết quả bằng cách thay các giá trị vừa tìm được trở lại vào các phương trình ở bước 5. Điều này đặc biệt quan trọng nếu ở bước 5 bạn có nhiều phương trình hơn số phương trình tối thiểu đã dùng ở bước 6.
8. Hãy sắp xếp lực do sợi dây tác dụng lên sợi xích, lực do mắt xích trên tác dụng lên mắt xích giữa, và lực do mắt xích giữa tác dụng lên mắt xích dưới cùng theo thứ tự độ lớn từ nhỏ nhất đến lớn nhất. Thứ tự sắp xếp này có hợp lý về mặt vật lý hay không? Hãy giải thích.
9. Lặp lại bài toán cho trường hợp lực kéo hướng lên mà sợi dây tác dụng lên sợi xích chỉ bằng $7{,}35\,\mathrm N$. Thứ tự sắp xếp ở bước 8 có thay đổi không? Kết quả này có ý nghĩa vật lý như thế nào?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**
- Khối lượng mỗi mắt xích: $m = 0{,}250\,\mathrm{kg}$.
- Số mắt xích: 3 mắt (mắt 1 ở trên cùng, mắt 2 ở giữa, mắt 3 ở dưới cùng).
- Khối lượng toàn bộ sợi xích: $M = 3m = 0{,}750\,\mathrm{kg}$.
- Lực kéo của sợi dây hướng lên: $F_{\mathrm{rope}} = 9{,}00\,\mathrm N$.
- Gia tốc trọng trường: $g = 9{,}80\,\mathrm{m/s^2}$.
- Cần tìm:
  - (a) Vẽ sơ đồ vật thể tự do (FBD) cho toàn bộ chuỗi và cho từng mắt xích.
  - (b) Xác định gia tốc $a$, lực tiếp xúc $F_{12}$ (mắt 1 lên mắt 2) và $F_{23}$ (mắt 2 lên mắt 3).
  - So sánh thứ tự độ lớn các lực và phân tích trường hợp $F_{\mathrm{rope}} = 7{,}35\,\mathrm N$.

**Hướng đi:**
- Áp dụng định luật II Newton cho toàn bộ hệ: Trọng lượng của cả sợi xích là $W = Mg$. Vì các mắt xích liên kết cứng với nhau, gia tốc của cả hệ bằng gia tốc của từng mắt xích: $a = (F_{\mathrm{rope}} - W) / M$.
- Phân tích từng mắt xích riêng rẽ:
  - Mắt xích dưới cùng (mắt 3) chỉ chịu trọng lực $w_3 = mg$ hướng xuống và lực tiếp xúc do mắt 2 nâng lên $F_{23}$ hướng lên. Phương trình: $F_{23} - mg = ma$.
  - Mắt xích giữa (mắt 2) chịu trọng lực $w_2 = mg$ hướng xuống, lực do mắt 3 kéo xuống $F_{32}$ (với $F_{32} = F_{23}$ theo định luật III Newton), và lực nâng do mắt 1 tác dụng $F_{12}$ hướng lên.
  - Mắt xích trên cùng (mắt 1) chịu lực kéo $F_{\mathrm{rope}}$ hướng lên, trọng lực $w_1 = mg$ hướng xuống, và lực kéo xuống do mắt 2 tác dụng $F_{21}$ (với $F_{21} = F_{12}$).
- Đánh giá bản chất cơ học: Mỗi liên kết tiếp xúc chịu tải trọng tương ứng với toàn bộ phần khối lượng treo phía dưới nó.

**Lời giải chi tiết:**

![Sơ đồ lực toàn chuỗi và ba mắt xích.](/vat-ly-1/bai-giang/img/young-04/parent-solution-bridge.svg)

#### (a) Phân tích lực và thiết lập sơ đồ vật thể tự do (FBD)

Chọn trục thẳng đứng $Oy$ có chiều dương hướng lên trên cho tất cả các đối tượng.

1. **Sơ đồ vật thể tự do cho toàn bộ sợi xích (khối lượng $M = 3m = 0{,}750\,\mathrm{kg}$):**
Toàn bộ sợi xích chỉ chịu tác dụng của hai ngoại lực:
- Lực kéo hướng lên từ sợi dây: $\vec{F}_{\mathrm{rope}}$ đặt tại mắt xích trên cùng, hướng thẳng đứng lên trên ($+y$).
- Trọng lực tổng cộng của Trái Đất tác dụng lên cả chuỗi: $\vec{W} = M\vec{g}$ hướng thẳng đứng xuống dưới ($-y$), với độ lớn:
$$
\begin{aligned}
W &= Mg \\
&= (0{,}750\,\mathrm{kg})(9{,}80\,\mathrm{m/s^2}) \\
&= 7{,}35\,\mathrm N
\end{aligned}
$$
(Các lực tương tác giữa các mắt xích là nội lực của hệ sợi xích nên triệt tiêu lẫn nhau từng đôi một).

2. **Sơ đồ vật thể tự do cho mắt xích 3 (mắt xích dưới cùng, khối lượng $m = 0{,}250\,\mathrm{kg}$):**
- Trọng lực: $\vec{w}_3 = m\vec{g}$ hướng thẳng đứng xuống dưới, độ lớn $w_3 = mg = 2{,}45\,\mathrm N$.
- Lực tiếp xúc do mắt xích 2 tác dụng lên mắt xích 3: Ký hiệu $\vec{F}_{23}$, hướng thẳng đứng lên trên.

3. **Sơ đồ vật thể tự do cho mắt xích 2 (mắt xích ở giữa, khối lượng $m = 0{,}250\,\mathrm{kg}$):**
- Trọng lực: $\vec{w}_2 = m\vec{g}$ hướng xuống dưới, độ lớn $w_2 = 2{,}45\,\mathrm N$.
- Lực kéo tiếp xúc do mắt xích 3 tác dụng lên mắt xích 2: Ký hiệu $\vec{F}_{32}$, hướng thẳng đứng xuống dưới.
- Lực nâng tiếp xúc do mắt xích 1 tác dụng lên mắt xích 2: Ký hiệu $\vec{F}_{12}$, hướng thẳng đứng lên trên.
Theo định luật III Newton, cặp lực tương tác giữa mắt 2 và mắt 3 là cặp trực đối:
$$
F_{32} = F_{23}
$$

4. **Sơ đồ vật thể tự do cho mắt xích 1 (mắt xích trên cùng, khối lượng $m = 0{,}250\,\mathrm{kg}$):**
- Lực kéo của sợi dây: $\vec{F}_{\mathrm{rope}}$ hướng thẳng đứng lên trên, độ lớn $9{,}00\,\mathrm N$.
- Trọng lực: $\vec{w}_1 = m\vec{g}$ hướng xuống dưới, độ lớn $w_1 = 2{,}45\,\mathrm N$.
- Lực kéo tiếp xúc do mắt xích 2 tác dụng lên mắt xích 1: Ký hiệu $\vec{F}_{21}$, hướng thẳng đứng xuống dưới.
Theo định luật III Newton, cặp lực tương tác giữa mắt 1 và mắt 2 là cặp trực đối:
$$
F_{21} = F_{12}
$$

#### (b) Áp dụng các định luật Newton và tính toán các đại lượng mục tiêu

**(i) Tính gia tốc của sợi xích:**
Áp dụng định luật II Newton cho toàn thể sợi xích chuyển động tịnh tiến theo phương thẳng đứng:
$$
\sum F_y = F_{\mathrm{rope}} - W = Ma
$$
Suy ra gia tốc chuyển động:
$$
\begin{aligned}
a &= \frac{F_{\mathrm{rope}} - W}{M} \\
&= \frac{9{,}00\,\mathrm N - 7{,}35\,\mathrm N}{0{,}750\,\mathrm{kg}} \\
&= \frac{1{,}65\,\mathrm N}{0{,}750\,\mathrm{kg}} \\
&= 2{,}20\,\mathrm{m/s^2}
\end{aligned}
$$
Vì $a > 0$, sợi xích chuyển động nhanh dần đều thẳng đứng hướng lên trên với gia tốc $2{,}20\,\mathrm{m/s^2}$.

**(ii) Tính lực do mắt xích trên cùng tác dụng lên mắt xích ở giữa ($F_{12}$):**
Xét hệ gồm hai mắt xích dưới cùng (mắt 2 và mắt 3) có tổng khối lượng $m_{23} = 2m = 0{,}500\,\mathrm{kg}$. Ngoại lực tác dụng lên hệ này theo phương thẳng đứng gồm:
- Lực nâng hướng lên từ mắt 1: $\vec{F}_{12}$.
- Tổng trọng lượng hướng xuống: $W_{23} = 2mg = 4{,}90\,\mathrm N$.

Áp dụng định luật II Newton cho hệ hai mắt xích này:
$$
F_{12} - 2mg = 2ma
$$
Suy ra:
$$
\begin{aligned}
F_{12} &= 2m(g + a) \\
&= (0{,}500)(12{,}00)\,\mathrm N \\
&= 6{,}00\,\mathrm N
\end{aligned}
$$

**(iii) Tính lực do mắt xích ở giữa tác dụng lên mắt xích dưới cùng ($F_{23}$):**
Áp dụng định luật II Newton cho riêng mắt xích dưới cùng (mắt 3):
$$
F_{23} - mg = ma
$$
Suy ra:
$$
\begin{aligned}
F_{23} &= m(g + a) \\
&= (0{,}250)(12{,}00)\,\mathrm N \\
&= 3{,}00\,\mathrm N
\end{aligned}
$$

Kiểm tra lại cho mắt xích 1:
$$
\begin{aligned}
\sum F_{1y} &= F_{\mathrm{rope}} - mg - F_{21} \\
&= 9{,}00 - 2{,}45 - 6{,}00 \\
&= 0{,}55\,\mathrm N
\end{aligned}
$$
Mặt khác:
$$
ma = 0{,}55\,\mathrm N
$$
Hai phương trình cho cùng hợp lực lên mắt trên, phù hợp với gia tốc đã tìm từ toàn hệ.

#### Đánh giá và thảo luận mở rộng (Các bước 8 và 9)

**Bước 8: Xếp hạng độ lớn các lực:**
Các lực có độ lớn lần lượt là:
- Lực của mắt giữa lên mắt dưới: $F_{23} = 3{,}00\,\mathrm N$.
- Lực của mắt trên lên mắt giữa: $F_{12} = 6{,}00\,\mathrm N$.
- Lực của dây lên sợi xích: $F_{\mathrm{rope}} = 9{,}00\,\mathrm N$.

Sắp xếp theo thứ tự độ lớn từ nhỏ nhất đến lớn nhất:
$$
F_{23} < F_{12} < F_{\mathrm{rope}}
$$
Thứ tự này hoàn toàn hợp lý về mặt vật lý: Lực $F_{23}$ chỉ phải nâng và tăng tốc cho duy nhất 1 mắt xích bên dưới ($m$); lực $F_{12}$ phải nâng và tăng tốc cho 2 mắt xích bên dưới ($2m$); trong khi lực kéo của sợi dây $F_{\mathrm{rope}}$ phải gánh vác toàn bộ cả 3 mắt xích ($3m$). Tỷ lệ các lực đúng bằng tỷ lệ số mắt xích được kéo: $1 : 2 : 3$.

**Bước 9: Trường hợp lực kéo của dây bằng $7{,}35\,\mathrm N$:**
Trọng lượng tổng cộng của sợi xích là $W = 7{,}35\,\mathrm N$. Khi lực kéo hướng lên $F_{\mathrm{rope}} = 7{,}35\,\mathrm N$:
$$
\sum F_y = 0 \implies a = 0
$$
Sợi xích ở trạng thái cân bằng tĩnh (hoặc chuyển động thẳng đều). Khi đó, mỗi mắt xích chỉ cần đỡ đúng trọng lượng của các mắt xích treo bên dưới nó:
- Lực do mắt giữa tác dụng lên mắt dưới:
$$
F_{23} = mg = 2{,}45\,\mathrm N
$$
- Lực do mắt trên tác dụng lên mắt giữa:
$$
F_{12} = 2mg = 4{,}90\,\mathrm N
$$
- Lực của sợi dây:
$$
F_{\mathrm{rope}} = 3mg = 7{,}35\,\mathrm N
$$
Thứ tự xếp hạng vẫn giữ nguyên:
$$
F_{23} < F_{12} < F_{\mathrm{rope}}
$$
với các giá trị tương ứng là $2{,}45\,\mathrm N < 4{,}90\,\mathrm N < 7{,}35\,\mathrm N$.
Tỷ lệ giữa các lực vẫn tuyệt đối là $1 : 2 : 3$, vì dù có gia tốc hay đứng yên, số lượng mắt xích mà mỗi liên kết phải gánh đỡ ở bên dưới vẫn không đổi.

</details>
