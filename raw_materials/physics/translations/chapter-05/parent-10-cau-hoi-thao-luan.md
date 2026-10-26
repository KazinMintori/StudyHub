## Câu hỏi thảo luận

Nếu không có chỉ dẫn khác, coi các ròng rọc không ma sát và có khối lượng không đáng kể. Dây và cáp treo cũng được coi là không có khối lượng.

### Q5.1 Lực căng dây và phản lực của ghế tác dụng lên người tự kéo mình

Một người ngồi trên một chiếc ghế treo bằng một sợi dây. Sợi dây vắt qua một ròng rọc cố định gắn trên trần nhà và người đó cầm đầu dây còn lại bằng hai tay của mình. Lực căng trong sợi dây bằng bao nhiêu và ghế tác dụng lên người đó một lực bằng bao nhiêu? Vẽ giản đồ phân tích lực tự do (FBD) cho người đó.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Người có khối lượng $m$ (trọng lượng $w = mg$) ngồi trên ghế treo (khối lượng $m_{\mathrm{seat}}$, trọng lượng $w_{\mathrm{seat}}$). Dây vắt qua ròng rọc trên trần, người tự cầm đầu dây còn lại để giữ hệ cân bằng tĩnh. Bỏ qua ma sát ròng rọc và khối lượng dây. Tìm lực căng dây $T$, phản lực $n$ do ghế tác dụng lên người, và vẽ giản đồ phân tích lực.

**Hướng đi:**

1. Xét toàn bộ hệ thống gồm (người + ghế): Hệ được nâng đỡ bởi hai nhánh dây hướng lên từ ròng rọc. Do hệ đứng yên cân bằng nên tổng lực căng của hai nhánh dây phải cân bằng với tổng trọng lượng của người và ghế: $2T = w + w_{\mathrm{seat}}$. Từ đó tính được lực căng $T$.
2. Xét riêng người ngồi trên ghế: Các lực tác dụng lên người gồm có:
   - Lực căng $\vec{T}$ do sợi dây kéo tay người hướng lên trên.
   - Phản lực pháp tuyến $\vec{n}$ do mặt ghế đỡ người hướng lên trên.
   - Trọng lực $\vec{w}$ hướng thẳng đứng xuống dưới.
3. Thiết lập phương trình cân bằng cho người để tìm phản lực $n$.

**Lời giải:**

Xét trạng thái cân bằng của hệ thống:

![Giản đồ Q5.1: Lực căng và lực đỡ hướng lên, trọng lực hướng xuống.](/vat-ly-1/bai-giang/img/young-05/solution-s-q5-1-man-fbd.svg)
1. Xác định lực căng trong sợi dây:
Coi người và ghế là một hệ vật thể duy nhất có tổng trọng lượng $w_{\mathrm{total}} = w + w_{\mathrm{seat}}$. Hai đoạn dây treo đi ra từ ròng rọc đều chịu lực căng $T$ và cùng hướng thẳng đứng lên trên.

Điều kiện cân bằng tĩnh của hệ:
$$
2T - (w + w_{\mathrm{seat}}) = 0
$$

Suy ra lực căng trong sợi dây:
$$
T = \frac{w + w_{\mathrm{seat}}}{2}
$$

Trong trường hợp khối lượng của chiếc ghế rất nhỏ so với người ($w_{\mathrm{seat}} \approx 0$), lực căng dây là:
$$
T \approx \frac{w}{2}
$$

2. Xác định lực do ghế tác dụng lên người:
Xét riêng cơ thể người. Ba lực tác dụng lên người gồm:
- Lực kéo lên của sợi dây tác dụng vào hai bàn tay: $T$.
- Phản lực pháp tuyến do mặt ghế đẩy lên: $n$.
- Trọng lực của Trái Đất kéo xuống: $w = mg$.

Phương trình cân bằng lực theo phương thẳng đứng:
$$
T + n - w = 0
$$

Suy ra lực do ghế tác dụng lên người:
$$
\begin{aligned}
n &= w - T \\
&= w - \frac{w + w_{\mathrm{seat}}}{2} \\
&= \frac{w - w_{\mathrm{seat}}}{2}
\end{aligned}
$$

Khi khối lượng của ghế không đáng kể ($w_{\mathrm{seat}} \ll w$):
$$
n \approx \frac{w}{2}
$$

Nhận xét vật lý: Người chỉ cần dùng hai tay tác dụng một lực bằng một nửa trọng lượng cơ thể là có thể tự giữ mình lơ lửng trên không trung. Chiếc ghế cũng chỉ phải đỡ một nửa trọng lượng cơ thể người đó vì nửa còn lại đã được lực căng dây đỡ trực tiếp qua hai tay.

Với mô hình người chỉ tì lên mặt ghế và không được buộc vào ghế, cần $n\ge0$. Biểu thức tổng quát vì thế đòi hỏi trọng lượng ghế không vượt trọng lượng người. Khi bỏ qua trọng lượng ghế, cả lực căng và lực đỡ đều bằng $w/2$.

</details>

### Q5.2 Phân biệt độ lớn của lực pháp tuyến và trọng lượng

Người ta thường nói: "Về mặt tổng quát, lực pháp tuyến không bằng trọng lượng." Hãy nêu một ví dụ trong đó hai lực này có độ lớn bằng nhau, và ít nhất hai ví dụ trong đó hai lực này có độ lớn khác nhau.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Phân tích nhận định về mối quan hệ giữa độ lớn lực pháp tuyến $n$ và trọng lượng $w = mg$. Đưa ra một ví dụ $n = w$ và ít nhất hai ví dụ $n \ne w$.

**Hướng đi:**

1. Làm rõ bản chất vật lý: Trọng lực là lực hút hấp dẫn của Trái Đất tác dụng lên vật, luôn hướng thẳng đứng xuống tâm Trái Đất và có độ lớn cố định $w = mg$. Lực pháp tuyến là lực tiếp xúc đàn hồi giữa hai bề mặt, luôn vuông góc với mặt tiếp xúc và độ lớn của nó biến thiên tự do để thỏa mãn phương trình động lực học vuông góc với mặt tiếp xúc.
2. Tìm ví dụ cân bằng cơ bản: Một vật đặt trên sàn phẳng nằm ngang không chịu thêm lực thẳng đứng nào khác ($n = mg$).
3. Tìm các ví dụ làm thay đổi áp lực tiếp xúc: Mặt phẳng nghiêng, lực kéo/đẩy có thành phần thẳng đứng, hoặc chuyển động có gia tốc theo phương vuông góc với mặt tiếp xúc.

**Lời giải:**

Bản chất của hai lực:
Trọng lực $\vec{w}$ là lực trường hấp dẫn do Trái Đất tác dụng, có phương thẳng đứng hướng xuống và độ lớn $w = mg$. Phản lực pháp tuyến $\vec{n}$ là lực liên kết đàn hồi bề mặt, luôn vuông góc với mặt tiếp xúc và độ lớn phụ thuộc hoàn toàn vào các điều kiện động lực học cụ thể.

1. Ví dụ hai lực có độ lớn bằng nhau ($n = w$):
Một cuốn sách nằm yên trên mặt bàn phẳng nằm ngang và không chịu thêm bất kỳ lực nào khác tác dụng theo phương thẳng đứng.

Theo phương thẳng đứng, gia tốc bằng 0:
$$
n - w = 0 \implies n = mg
$$

2. Các ví dụ hai lực có độ lớn khác nhau ($n \ne w$):
- **Ví dụ 1 (Vật trên mặt phẳng nghiêng)**: Một chiếc hộp nằm trên mặt dốc nghiêng góc $\theta$ so với phương ngang ($0^\circ < \theta < 90^\circ$).
Phương trình cân bằng theo phương vuông góc với mặt dốc:
$$
n = w\cos\theta = mg\cos\theta
$$
Vì $\cos\theta < 1$ nên lực pháp tuyến luôn nhỏ hơn trọng lượng:
$$
n < w
$$

- **Ví dụ 2 (Vật chịu ngoại lực tác dụng xiên)**: Một kiện hàng nằm trên sàn ngang chịu lực kéo $\vec{F}$ hợp với phương ngang góc $\theta$ chếch lên trên.
Cân bằng lực theo phương thẳng đứng cho ta:
$$
n + F \sin\theta - w = 0
$$
Kéo theo:
$$
n = w - F \sin\theta < w
$$
Nếu lực $\vec{F}$ hướng chếch xuống dưới sàn, ta lại có:
$$
n = w + F \sin\theta > w
$$

- **Ví dụ 3 (Vật trong thang máy chuyển động có gia tốc)**: Một người đứng trên cân đặt trong thang máy đang chuyển động với gia tốc $\vec{a}$ theo phương thẳng đứng:
$$
n = m(g + a_y)
$$
Khi thang máy tăng tốc đi lên ($a_y > 0$), lực pháp tuyến lớn hơn trọng lượng ($n > mg$). Khi thang máy tăng tốc đi xuống ($a_y < 0$), lực pháp tuyến nhỏ hơn trọng lượng ($n < mg$).

Các biểu thức của lực pháp tuyến chỉ mô tả trạng thái còn tiếp xúc. Khi một phép tính cho $n<0$, phải xét việc mất tiếp xúc, không gán cho mặt bàn một lực kéo vật xuống.

</details>

### Q5.3 Hiện tượng võng của dây phơi quần áo

Một sợi dây phơi quần áo được căng ngang giữa hai chiếc cột. Dù sợi dây có được kéo căng đến mức nào đi chăng nữa, nó vẫn luôn bị võng xuống một chút ở đoạn giữa. Hãy giải thích tại sao.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Giải thích tại sao một sợi dây phơi căng giữa hai điểm cố định luôn bị võng xuống ở giữa mà không thể căng thẳng tuyệt đối theo phương ngang, dù lực căng dây có lớn đến đâu.

**Hướng đi:**

1. Sợi dây thực tế luôn có khối lượng xác định nên chịu lực hút của Trái Đất hướng thẳng đứng xuống dưới.
2. Để sợi dây (hoặc một phần tử của dây ở điểm giữa) đứng yên cân bằng, tổng hợp lực theo phương thẳng đứng tác dụng lên phần tử đó phải triệt tiêu.
3. Lực duy nhất có thể chống lại trọng lực là lực căng của sợi dây. Lực căng luôn tác dụng dọc theo tiếp tuyến của sợi dây.
4. Nếu sợi dây hoàn toàn thẳng ngang, góc lệch so với phương ngang bằng 0, khi đó thành phần thẳng đứng của lực căng bằng 0 và không thể cân bằng trọng lực.
5. Thiết lập điều kiện cân bằng để chỉ ra rằng lực căng sẽ tiến ra vô hạn nếu góc võng tiến về 0.

**Lời giải:**

Xét một sợi dây có khối lượng tổng cộng $m$ (trọng lượng $w = mg > 0$). Xét mô hình hai đầu dây cùng độ cao và hình dạng đối xứng. Sợi dây bị võng xuống ở điểm giữa và hợp với phương ngang một góc $\theta$ ở hai đầu treo.

Các lực tác dụng lên sợi dây gồm:
- Trọng lực $\vec{w}$ hướng thẳng đứng xuống dưới.
- Lực căng $\vec{T}$ ở hai đầu dây, mỗi lực hợp với phương ngang góc $\theta$ hướng lên.

Điều kiện cân bằng tĩnh theo phương thẳng đứng:
$$
2T \sin\theta - w = 0
$$

Suy ra lực căng trong sợi dây:
$$
T = \frac{w}{2\sin\theta}
$$

Phân tích trạng thái dây hoàn toàn thẳng ngang:
Nếu sợi dây hoàn toàn thẳng ngang thì góc võng $\theta = 0^\circ$. Khi đó:
$$
\sin\theta = \sin 0^\circ = 0
$$

Biểu thức lực căng đòi hỏi:
$$
\lim_{\theta\to0^+}\frac{w}{2\sin\theta}=+\infty
$$

Một lực căng lớn vô hạn là điều không tưởng trong thế giới thực vì mọi vật liệu đều có giới hạn bền hữu hạn và sẽ đứt trước khi lực căng đạt tới giá trị đó. Do đó, góc lệch $\theta$ bắt buộc phải lớn hơn $0$ để thành phần thẳng đứng $2T \sin\theta$ có thể cân bằng với trọng lượng hữu hạn của sợi dây. Vì vậy, dây phơi luôn luôn bị võng xuống ở giữa.

</details>

### Q5.4 Phân tích các lực tác dụng lên ô tô leo dốc đều

Bạn lái một chiếc ô tô lên một con dốc nghiêng với tốc độ không đổi. Hãy thảo luận về tất cả các lực tác dụng lên chiếc xe. Lực nào trực tiếp đẩy chiếc ô tô chuyển động lên dốc?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Ô tô đi lên dốc với tốc độ không đổi. Cần xác định các lực ngoài tác dụng lên toàn xe và lực đẩy xe lên dốc.

**Hướng đi:** Chọn toàn bộ ô tô làm hệ. Chỉ những tương tác với vật ngoài hệ mới xuất hiện trong phương trình hợp lực. Điểm lốp tiếp xúc đường không trượt, nên lực kéo tiếp tuyến ở bánh chủ động là ma sát nghỉ.

**Lời giải:** Trọng lực tác dụng thẳng đứng xuống dưới. Mặt đường tác dụng các phản lực pháp tuyến lên bánh xe và các lực tiếp tuyến tại chỗ tiếp xúc. Không khí và biến dạng tiếp xúc có thể tạo lực cản chuyển động. Tổng thành phần dọc dốc bằng không khi xe chạy thẳng đều.

Động cơ truyền mômen đến bánh chủ động. Lốp có xu hướng đẩy mặt đường xuống dốc, còn mặt đường tác dụng ma sát nghỉ lên lốp theo chiều lên dốc. Lực từ mặt đường này trực tiếp cung cấp lực kéo ngoài cho xe. Lực từ động cơ lên các bộ phận khác của chính xe là nội lực nếu xét toàn xe.

Trong mô hình gom lực cản dọc dốc thành $F_c$, gọi lực kéo tiếp tuyến tổng cộng là $f$. Điều kiện chạy đều là:

$$
f=mg\sin\theta+F_c.
$$

Lực tiếp tuyến ở từng bánh không nhất thiết có cùng chiều, nhưng tổng các lực ấy phải thỏa phương trình chuyển động. Không gán lực hướng lên dốc trực tiếp cho động cơ mà bỏ qua tương tác lốp với mặt đường.

</details>

### Q5.5 Phương án đo khối lượng phi hành gia trong môi trường không trọng lượng

Vì các lý do y tế, các phi hành gia ngoài không gian phải xác định khối lượng cơ thể của mình theo định kỳ. Hãy đề xuất một phương án đo khối lượng cơ thể trong môi trường dường như không trọng lượng.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cần đo khối lượng khi người và tàu cùng rơi tự do, nên không thể suy khối lượng từ trọng lượng biểu kiến bằng cách cân thông thường.

**Hướng đi:** Khối lượng vẫn quyết định gia tốc do một lực đã biết gây ra. Dùng định luật II Newton thay cho quan hệ cân tĩnh giữa lực đỡ và trọng lượng.

**Lời giải:** Có thể cố định người vào một ghế dẫn hướng, tác dụng một lực đã được hiệu chuẩn và đo gia tốc của hệ ghế cùng người. Gọi khối lượng ghế là $M$, khối lượng người là $m$, lực theo phương đo là $F$ và gia tốc là $a$. Khi bỏ qua lực cản trên dẫn hướng:

$$
F=(M+m)a.
$$

Suy ra:

$$
m=\frac Fa-M.
$$

Lực có thể được xác định bằng một lò xo đã hiệu chuẩn, còn gia tốc được suy từ vị trí đo theo thời gian. Phải trừ khối lượng ghế và xét các lực phụ nếu chúng không thể bỏ qua.

Hệ đo được coi là gần quán tính theo phương đo, với ảnh hưởng chuyển động của bệ đã được kiểm soát. Trạng thái không trọng lượng biểu kiến làm cân dựa vào lực đỡ không dùng được theo cách thông thường, nhưng không làm mất quán tính của người.

</details>

### Q5.6 So sánh lực đẩy hộp lên dốc theo phương ngang và phương song song với dốc

Để đẩy một chiếc hộp chuyển động lên một con dốc nghiêng, cách nào đòi hỏi lực tác dụng nhỏ hơn: Đẩy theo phương nằm ngang hay đẩy theo phương song song với mặt dốc? Tại sao?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

So sánh độ lớn lực cần thiết để đẩy một chiếc hộp trượt đều lên dốc nghiêng góc $\theta$ ($0^\circ < \theta < 90^\circ$): Lực $F_{\parallel}$ tác dụng song song với mặt dốc và lực $F_{\mathrm{horiz}}$ tác dụng theo phương ngang. Giải thích nguyên nhân vật lý.

**Hướng đi:**

1. Viết phương trình động lực học cho trường hợp đẩy song song với mặt dốc: Lực $F_{\parallel}$ chỉ cần thắng thành phần trọng lực dọc dốc $mg \sin\theta$ và lực ma sát trượt $f_{\mathrm{k}1} = \mu_{\mathrm{k}} n_1$, trong đó phản lực $n_1 = mg \cos\theta$.
2. Viết phương trình động lực học cho trường hợp đẩy theo phương nằm ngang: Lực $F_{\mathrm{horiz}}$ bị phân tách thành hai thành phần:
   - Thành phần dọc dốc $F_{\mathrm{horiz}} \cos\theta$ đẩy hộp lên dốc.
   - Thành phần vuông góc với dốc $F_{\mathrm{horiz}} \sin\theta$ đè thêm hộp vào mặt dốc, làm tăng phản lực pháp tuyến $n_2 = mg \cos\theta + F_{\mathrm{horiz}} \sin\theta$, kéo theo lực ma sát tăng mạnh.
3. So sánh độ lớn giữa $F_{\parallel}$ và $F_{\mathrm{horiz}}$ cho cả hai trường hợp có ma sát và không ma sát.

**Lời giải:**

Xét chiếc hộp khối lượng $m$ chuyển động thẳng đều lên mặt dốc nghiêng góc $\theta$ so với phương ngang.

1. Trường hợp 1: Đẩy theo phương song song với mặt dốc ($F_{\parallel}$):
Theo phương vuông góc với dốc:
$$
n_1 = mg \cos\theta
$$

Lực ma sát trượt:
$$
f_{\mathrm{k}1} = \mu_{\mathrm{k}} mg \cos\theta
$$

Phương trình cân bằng lực dọc theo mặt dốc:
$$
F_{\parallel} = mg \sin\theta + \mu_{\mathrm{k}} mg \cos\theta
$$

2. Trường hợp 2: Đẩy theo phương nằm ngang ($F_{\mathrm{horiz}}$):
Lực $\vec{F}_{\mathrm{horiz}}$ có thành phần dọc dốc $F_{\mathrm{horiz}} \cos\theta$ và thành phần đè vuông góc vào mặt dốc $F_{\mathrm{horiz}} \sin\theta$.

Theo phương vuông góc với mặt dốc:
$$
n_2 = mg \cos\theta + F_{\mathrm{horiz}} \sin\theta
$$

Lực ma sát trượt:
$$
f_{\mathrm{k}2} = \mu_{\mathrm{k}} n_2
$$

Phương trình cân bằng lực dọc theo mặt dốc:
$$
F_{\mathrm{horiz}} \cos\theta = mg \sin\theta + f_{\mathrm{k}2}
$$

Thay $n_2$ và biểu thức $F_{\parallel} = mg(\sin\theta + \mu_{\mathrm{k}}\cos\theta)$ vào, ta được:
$$
F_{\mathrm{horiz}}(\cos\theta - \mu_{\mathrm{k}}\sin\theta) = F_{\parallel}
$$

Suy ra:
$$
F_{\mathrm{horiz}} = \frac{F_{\parallel}}{\cos\theta - \mu_{\mathrm{k}}\sin\theta}
$$

3. So sánh:
- Khi không có ma sát ($\mu_{\mathrm{k}} = 0$):
$$
F_{\mathrm{horiz}} = \frac{mg\sin\theta}{\cos\theta} = mg\tan\theta
$$
(Vì $\cos\theta < 1$ với mọi $0^\circ < \theta < 90^\circ$).
- Khi có ma sát ($\mu_{\mathrm{k}} > 0$): Mẫu số $\cos\theta - \mu_{\mathrm{k}}\sin\theta$ nhỏ hơn $\cos\theta < 1$, khiến $F_{\mathrm{horiz}}$ càng lớn hơn $F_{\parallel}$.

Kết luận: Đẩy theo phương **song song với mặt dốc** luôn đòi hỏi lực tác dụng nhỏ hơn, vì toàn bộ lực đẩy được dùng trực tiếp để thắng trọng lực mà không bị lãng phí vào việc đè vật xuống mặt dốc làm tăng lực cản ma sát.

Biểu thức của lực đẩy ngang hữu hạn dương ở trên đòi hỏi $\cos\theta-\mu_k\sin\theta>0$. Nếu điều kiện này không thỏa, tăng lực đẩy ngang làm tăng lực ép và ma sát tới mức không thể duy trì chuyển động lên dốc đều chỉ bằng lực ấy.

</details>

### Q5.7 Chiếc cặp rơi tự do trong thang máy

Một người phụ nữ đứng trong thang máy buông tay khỏi chiếc cặp của mình, nhưng chiếc cặp không hề rơi xuống sàn thang máy mà vẫn lơ lửng tại chỗ. Thang máy đang chuyển động như thế nào?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Chiếc cặp được buông tay trong thang máy nhưng giữ nguyên vị trí tương đối so với sàn thang máy (không rơi xuống sàn). Xác định trạng thái chuyển động của thang máy.

**Hướng đi:**

1. Phân tích chuyển động của chiếc cặp trong hệ quy chiếu quán tính gắn với mặt đất: Khi người phụ nữ buông tay, lực tiếp xúc triệt tiêu, lực duy nhất tác dụng lên chiếc cặp là trọng lực của Trái Đất.
2. Theo định luật II Newton, chiếc cặp rơi tự do với gia tốc trọng trường $a_{\mathrm{briefcase}} = g$ hướng thẳng đứng xuống dưới.
3. Để khoảng cách giữa chiếc cặp và sàn thang máy không đổi, sàn thang máy bắt buộc phải có cùng gia tốc với chiếc cặp đối với mặt đất, tức là $\vec{a}_{\mathrm{elevator}} = \vec{g}$ hướng thẳng đứng xuống dưới.
4. Thảo luận về trạng thái vận tốc của thang máy (hướng chuyển động).

**Lời giải:**

Xét chuyển động trong hệ quy chiếu quán tính gắn với mặt đất:
Ngay khi người phụ nữ buông tay, chiếc cặp chỉ còn chịu tác dụng duy nhất của trọng lực của Trái Đất, do đó gia tốc của chiếc cặp đối với mặt đất là:
$$
\vec{a}_{\mathrm{briefcase}} = \vec{g}
$$

Để chiếc cặp không rơi về phía sàn thang máy (tức là gia tốc tương đối giữa chiếc cặp và sàn thang máy bằng 0), thang máy cũng phải có gia tốc bằng chính gia tốc của chiếc cặp:
$$
\vec{a}_{\mathrm{elevator}} = \vec{g}
$$

Nghĩa là thang máy đang ở trạng thái **rơi tự do** với gia tốc có độ lớn $g = 9{,}80\,\mathrm{m/s^2}$ hướng thẳng đứng xuống dưới (ví dụ cáp treo bị đứt).

Lưu ý về chiều chuyển động (véc-tơ vận tốc $\vec{v}$):
Gia tốc thẳng đứng xuống dưới $g$ không đồng nghĩa với việc thang máy nhất thiết phải đang di chuyển xuống dưới:
- Thang máy có thể đang di chuyển xuống dưới và tăng tốc với tốc độ tăng dần $g$.
- Thang máy có thể đang di chuyển lên trên và chậm dần với gia tốc hãm $g$.
- Thang máy có thể nhất thời đứng yên ở điểm cao nhất của một quỹ đạo ném đứng.

Trong mọi trường hợp kể trên, điều kiện cốt lõi duy nhất là véc-tơ gia tốc của thang máy là $\vec{a} = \vec{g}$ hướng thẳng đứng xuống dưới.

</details>

### Q5.8 Đẩy vật trên mặt phẳng nghiêng có ma sát đủ lớn

Một khối vật nằm yên trên mặt phẳng nghiêng có đủ lực ma sát để ngăn không cho nó tự trượt xuống. Để làm cho khối vật bắt đầu chuyển động, đẩy vật lên dốc hay đẩy vật xuống dốc sẽ dễ dàng hơn? Tại sao?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Vật nằm yên trên dốc nghiêng góc $\theta$ nhờ ma sát nghỉ: $\mu_{\mathrm{s}} mg \cos\theta \ge mg \sin\theta$. So sánh lực tối thiểu cần thiết để làm vật bắt đầu chuyển động: Đẩy lên dốc ($F_{\mathrm{up}}$) hay đẩy xuống dốc ($F_{\mathrm{down}}$).

**Hướng đi:**

1. Khi vật nằm yên, thành phần trọng lực kéo xuống dốc là $w_x = mg \sin\theta$. Lực ma sát nghỉ cực đại giữ vật là $f_{\mathrm{s},\max} = \mu_{\mathrm{s}} mg \cos\theta$. Vì vật không tự trượt nên $f_{\mathrm{s},\max} \ge mg \sin\theta$.
2. Để đẩy vật bắt đầu đi lên dốc: Lực ma sát nghỉ đổi chiều hướng xuống dốc để chống lại xu hướng trượt lên. Lực đẩy phải thắng cả trọng lực và ma sát nghỉ cực đại: $F_{\mathrm{up}} = mg \sin\theta + f_{\mathrm{s},\max}$.
3. Để đẩy vật bắt đầu đi xuống dốc: Lực ma sát nghỉ hướng lên dốc. Thành phần trọng lực $mg \sin\theta$ cùng chiều với lực đẩy hỗ trợ đẩy vật xuống. Lực đẩy chỉ cần bù phần còn thiếu: $F_{\mathrm{down}} = f_{\mathrm{s},\max} - mg \sin\theta$.
4. So sánh hai giá trị lực.

**Lời giải:**

Xét khối vật khối lượng $m$ trên mặt phẳng nghiêng góc $\theta$.

Phản lực pháp tuyến của mặt dốc:
$$
n = mg \cos\theta
$$

Độ lớn của lực ma sát nghỉ cực đại:
$$
f_{\mathrm{s},\max} = \mu_{\mathrm{s}} n = \mu_{\mathrm{s}} mg \cos\theta
$$

Vì khối vật nằm yên không tự trượt xuống, ta có:
$$
mg \sin\theta \le f_{\mathrm{s},\max}
$$

1. Để đẩy vật bắt đầu chuyển động lên dốc:
Xu hướng trượt tương đối là hướng lên trên, vì vậy lực ma sát nghỉ cực đại hướng xuống dọc theo dốc. Lực tác dụng $F_{\mathrm{up}}$ phải thắng cả ma sát và thành phần trọng lực kéo xuống:
$$
F_{\mathrm{up}} = mg \sin\theta + \mu_{\mathrm{s}} mg \cos\theta
$$

2. Để đẩy vật bắt đầu chuyển động xuống dốc:
Xu hướng trượt tương đối là hướng xuống dưới, vì vậy lực ma sát nghỉ cực đại hướng lên dọc theo dốc. Thành phần trọng lực $mg \sin\theta$ hỗ trợ đẩy vật xuống:
$$
F_{\mathrm{down}} + mg \sin\theta = f_{\mathrm{s},\max}
$$

Suy ra lực cần tác dụng:
$$
F_{\mathrm{down}} = mg(\mu_{\mathrm{s}}\cos\theta - \sin\theta)
$$

3. So sánh:
Hiệu số giữa hai lực:
$$
F_{\mathrm{up}} - F_{\mathrm{down}} = 2 mg \sin\theta > 0
$$

Do $mg \sin\theta > 0$, ta luôn có:
$$
F_{\mathrm{down}} < F_{\mathrm{up}}
$$

Kết luận: Đẩy vật **xuống dốc** cần lực nhỏ hơn, bởi vì thành phần trọng lực kéo xuống dốc hỗ trợ cho người đẩy, trong khi nếu đẩy lên dốc thì trọng lực lại chống lại lực đẩy cùng với lực ma sát.

</details>

### Q5.9 Gia tốc khi trượt lên và trượt xuống mặt dốc có ma sát

Một kiện hàng trượt lên một con dốc nghiêng và sau đó trượt ngược trở xuống sau khi dừng lại tức thời gần đỉnh dốc. Giữa bề mặt con dốc và kiện hàng có ma sát trượt. Đại lượng nào lớn hơn? (i) Gia tốc của kiện hàng khi đang đi lên dốc; (ii) gia tốc của kiện hàng khi đang trượt xuống dốc; (iii) cả hai bằng nhau. Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Kiện hàng trượt lên dốc rồi trượt xuống dốc, có ma sát trượt $\mu_{\mathrm{k}} > 0$. So sánh độ lớn gia tốc khi lên dốc $a_{\mathrm{up}}$ và khi xuống dốc $a_{\mathrm{down}}$. Chọn giữa (i), (ii) và (iii).

**Hướng đi:**

1. Áp dụng định luật II Newton cho chuyển động lên dốc: Vận tốc hướng lên dốc, do đó lực ma sát trượt $f_{\mathrm{k}}$ hướng xuống dốc. Thành phần trọng lực $mg \sin\theta$ cũng hướng xuống dốc. Hai lực cùng chiều tạo nên hợp lực cản chuyển động có độ lớn lớn.
2. Áp dụng định luật II Newton cho chuyển động xuống dốc: Vận tốc hướng xuống dốc, do đó lực ma sát trượt $f_{\mathrm{k}}$ hướng lên dốc. Thành phần trọng lực $mg \sin\theta$ hướng xuống dốc. Hai lực ngược chiều nhau nên hợp lực kéo vật xuống có độ lớn bị giảm bớt.
3. So sánh độ lớn gia tốc thu được.

**Lời giải:**

Xét mặt dốc nghiêng góc $\theta$ so với phương ngang. Phản lực pháp tuyến trong cả hai giai đoạn đều là $n = mg \cos\theta$, do đó độ lớn của lực ma sát trượt luôn không đổi:
$$
f_{\mathrm{k}} = \mu_{\mathrm{k}} mg \cos\theta
$$

1. Khi kiện hàng trượt lên dốc:
Vận tốc hướng lên dốc. Cả thành phần trọng lực $mg \sin\theta$ và lực ma sát trượt $f_{\mathrm{k}}$ đều hướng xuống dọc theo mặt dốc.

Hợp lực tác dụng lên kiện hàng hướng xuống dọc dốc:
$$
F_{\mathrm{up}} = mg(\sin\theta + \mu_{\mathrm{k}}\cos\theta)
$$

Độ lớn gia tốc hãm khi đi lên:
$$
a_{\mathrm{up}} = g(\sin\theta + \mu_{\mathrm{k}}\cos\theta)
$$

2. Khi kiện hàng trượt xuống dốc:
Vận tốc hướng xuống dốc. Thành phần trọng lực $mg \sin\theta$ hướng xuống dốc, còn lực ma sát trượt $f_{\mathrm{k}}$ hướng ngược lại lên dốc.

Hợp lực tác dụng lên kiện hàng hướng xuống dọc dốc:
$$
F_{\mathrm{down}} = mg(\sin\theta - \mu_{\mathrm{k}}\cos\theta)
$$

Độ lớn gia tốc khi đi xuống:
$$
a_{\mathrm{down}} = g(\sin\theta - \mu_{\mathrm{k}}\cos\theta)
$$

3. So sánh:
Vì $\mu_{\mathrm{k}} > 0$ và $\cos\theta > 0$, ta có:
$$
a_{\mathrm{up}} > a_{\mathrm{down}}
$$

Suy ra:
$$
a_{\mathrm{up}} > a_{\mathrm{down}}
$$

Kết luận: Lựa chọn đúng là **(i) Gia tốc của kiện hàng khi đang đi lên dốc lớn hơn**. Khi đi lên dốc, ma sát và trọng lực cùng hợp sức hãm chuyển động của vật, trong khi khi đi xuống dốc, ma sát lại cản trở và triệt tiêu bớt tác dụng gia tốc của trọng lực.

Đề đã cho vật tự trượt trở xuống sau lúc dừng. Điều đó yêu cầu thành phần trọng lực xuống dốc thắng được lực giữ cần thiết ở trạng thái nghỉ. Nếu ma sát nghỉ đủ lớn để giữ vật ở đỉnh, giai đoạn tự trượt xuống được nêu trong đề sẽ không xảy ra.

</details>

### Q5.10 Kéo hộp chếch lên tốn ít lực hơn đẩy hộp chếch xuống

Một thùng sách nằm yên trên sàn phẳng nằm ngang. Để kéo thùng sách di chuyển trên sàn với vận tốc không đổi, tại sao bạn lại tốn ít lực hơn nếu kéo sợi dây hợp với phương ngang một góc $\theta$ chếch lên trên so với việc đẩy thùng sách với cùng góc $\theta$ đó chếch xuống dưới?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Giải thích tại sao lực kéo $F_{\mathrm{pull}}$ chếch lên góc $\theta$ so với phương ngang nhỏ hơn lực đẩy $F_{\mathrm{push}}$ chếch xuống góc $\theta$ khi cùng làm một vật trượt thẳng đều trên sàn ngang.

**Hướng đi:**

1. Phân tích lực pháp tuyến $n$ do sàn tác dụng lên thùng sách trong hai trường hợp:
   - Khi kéo chếch lên: Thành phần thẳng đứng của lực kéo hướng lên nhấc bớt vật khỏi sàn, làm giảm $n$.
   - Khi đẩy chếch xuống: Thành phần thẳng đứng của lực đẩy hướng xuống đè thêm vật vào sàn, làm tăng $n$.
2. Mối liên hệ với ma sát trượt: $f_{\mathrm{k}} = \mu_{\mathrm{k}} n$. Vì ma sát trượt tỷ lệ thuận với phản lực pháp tuyến, phản lực nhỏ hơn sẽ kéo theo lực ma sát nhỏ hơn.
3. Thiết lập phương trình cân bằng phương ngang và so sánh hai lực.

**Lời giải:**

Xét thùng sách trọng lượng $w = mg$ chuyển động thẳng đều ($a = 0$) trên sàn ngang với hệ số ma sát trượt $\mu_{\mathrm{k}}$.

1. Khi kéo chếch lên trên góc $\theta$:
Lực kéo $\vec{F}_{\mathrm{pull}}$ có thành phần thẳng đứng hướng lên $F_{\mathrm{pull}} \sin\theta$.

Phương trình cân bằng theo phương thẳng đứng:
$$
n_{\mathrm{pull}} + F_{\mathrm{pull}} \sin\theta - w = 0
$$

Kéo theo phản lực pháp tuyến:
$$
n_{\mathrm{pull}} = w - F_{\mathrm{pull}} \sin\theta < w
$$

Lực ma sát trượt cản trở chuyển động:
$$
f_{\mathrm{k, pull}} = \mu_{\mathrm{k}}(w - F_{\mathrm{pull}}\sin\theta)
$$

Cân bằng lực theo phương ngang:
$$
F_{\mathrm{pull}} \cos\theta = f_{\mathrm{k, pull}}
$$

Suy ra:
$$
F_{\mathrm{pull}} = \frac{\mu_{\mathrm{k}} w}{\cos\theta + \mu_{\mathrm{k}}\sin\theta}
$$

2. Khi đẩy chếch xuống dưới góc $\theta$:
Lực đẩy $\vec{F}_{\mathrm{push}}$ có thành phần thẳng đứng hướng xuống $F_{\mathrm{push}} \sin\theta$, ép thêm thùng vào sàn.

Phương trình cân bằng theo phương thẳng đứng:
$$
n_{\mathrm{push}} - F_{\mathrm{push}} \sin\theta - w = 0
$$

Kéo theo phản lực pháp tuyến:
$$
n_{\mathrm{push}} = w + F_{\mathrm{push}} \sin\theta > w
$$

Lực ma sát trượt:
$$
f_{\mathrm{k, push}} = \mu_{\mathrm{k}}(w + F_{\mathrm{push}}\sin\theta)
$$

Cân bằng lực theo phương ngang:
$$
F_{\mathrm{push}} \cos\theta = f_{\mathrm{k, push}}
$$

Suy ra:
$$
F_{\mathrm{push}} = \frac{\mu_{\mathrm{k}} w}{\cos\theta - \mu_{\mathrm{k}}\sin\theta}
$$

3. Kết luận:
Vì bất đẳng thức $\mu_{\mathrm{k}}\sin\theta > -\mu_{\mathrm{k}}\sin\theta$ luôn thỏa mãn, ta có:
$$
F_{\mathrm{pull}} < F_{\mathrm{push}}
$$

Lực kéo nhỏ hơn là vì việc kéo chếch lên giúp nâng đỡ một phần trọng lượng của vật, làm giảm phản lực pháp tuyến từ sàn, qua đó làm giảm đáng kể lực cản ma sát trượt cần phải vượt qua. Ngược lại, việc đẩy chếch xuống lại nén vật chặt hơn vào sàn, làm tăng mạnh lực cản ma sát.

Công thức lực đẩy chếch xuống để chuyển động đều chỉ dùng khi $\cos\theta-\mu_k\sin\theta>0$. Đây là điều kiện để lực đẩy cần thiết hữu hạn và cùng chiều đã giả định.

</details>

### Q5.11 Khả năng thực hiện các hoạt động trong thế giới không có ma sát

Trong một thế giới giả định hoàn toàn không có lực ma sát, hoạt động nào sau đây bạn có thể thực hiện được (hoặc không thể thực hiện được)? Giải thích lập luận của bạn.

(a) Lái xe chạy quanh một khúc cua xa lộ không nghiêng (mặt đường bằng phẳng).

(b) Bật nhảy lên không trung từ tư thế đứng yên.

(c) Bắt đầu bước đi trên một vỉa hè nằm ngang.

(d) Leo lên một chiếc thang dựng thẳng đứng.

(e) Chuyển làn đường khi bạn đang lái xe.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Xét thế giới không có ma sát ($\mu = 0$). Phân tích tính khả thi của 5 hoạt động: (a) Cua xe trên đường phẳng; (b) Bật nhảy thẳng đứng; (c) Bắt đầu đi bộ trên đường ngang; (d) Leo thang thẳng đứng; (e) Đổi làn xe khi đang chạy.

**Hướng đi:**

Phân tích điều kiện lực cần thiết để thực hiện từng chuyển động:
1. Nếu chuyển động đòi hỏi lực tiếp tuyến song song với bề mặt tiếp xúc thì bắt buộc phải có ma sát (không thể thực hiện nếu $\mu = 0$).
2. Nếu chuyển động chỉ đòi hỏi lực vuông góc với bề mặt tiếp xúc (lực pháp tuyến đàn hồi) thì vẫn thực hiện được vì lực pháp tuyến tồn tại độc lập với ma sát.

**Lời giải:**

(a) **Lái xe chạy quanh khúc cua xa lộ không nghiêng**: **Không thực hiện được**.
Để xe chuyển động tròn quanh khúc cua, xe bắt buộc phải có gia tốc hướng tâm nằm ngang:
$$
a_{\mathrm{rad}} = \frac{v^2}{R}
$$
Trên mặt đường bằng phẳng không nghiêng, phản lực pháp tuyến $\vec{n}$ có phương thẳng đứng và không thể có thành phần nằm ngang. Lực duy nhất có thể hướng theo phương ngang cung cấp gia tốc hướng tâm là lực ma sát nghỉ giữa lốp xe và mặt đường. Khi không có ma sát, hợp lực nằm ngang bằng 0, chiếc xe sẽ tiếp tục chuyển động thẳng theo quán tính và trượt văng ra khỏi khúc cua.

(b) **Bật nhảy lên không trung từ tư thế đứng yên**: **Có thể thực hiện**.
Động tác bật nhảy yêu cầu một lực đẩy thẳng đứng hướng lên từ mặt đất tác dụng lên bàn chân để tạo gia tốc $a_y > 0$:
$$
n = m(g + a_y) > mg
$$
Lực đẩy này là phản lực pháp tuyến $\vec{n}$, có phương vuông góc với mặt đất nằm ngang. Phản lực pháp tuyến xuất phát từ tương tác đàn hồi và lực đẩy tĩnh điện giữa các phân tử bề mặt tiếp xúc chứ không cần đến lực ma sát. Miễn là người đó đứng thăng bằng ban đầu và chỉ tác dụng lực thẳng đứng xuống dưới, người đó hoàn toàn có thể bật nhảy lên không trung.

(c) **Bắt đầu bước đi trên một vỉa hè nằm ngang**: **Không thực hiện được**.
Để bắt đầu bước đi (tăng tốc từ trạng thái đứng yên $v = 0$ sang $v > 0$), người đó phải có một gia tốc nằm ngang hướng về phía trước. Theo định luật III Newton, bàn chân phải đạp vào mặt đất về phía sau, và mặt đất phải tác dụng trở lại một lực ma sát nghỉ hướng về phía trước để đẩy người đi. Nếu không có ma sát, bàn chân sẽ trượt tự do về phía sau tại chỗ giống như bước trên lớp băng nhẵn tuyệt đối và trọng tâm cơ thể không thể tăng tốc về phía trước.

(d) **Leo lên một chiếc thang dựng thẳng đứng**: **Có thể thực hiện**.
Các bậc thang nằm ngang. Khi bạn bước lên một bậc thang hoặc dùng tay kéo xuống một bậc thang, bề mặt tiếp xúc giữa bàn chân/bàn tay và bậc thang là mặt phẳng nằm ngang. Lực tác dụng lên bậc thang có phương thẳng đứng hướng xuống, do đó phản lực do bậc thang tác dụng lên chân/tay là phản lực pháp tuyến $\vec{n}$ hướng thẳng đứng lên trên. Lực này không đòi hỏi ma sát và đủ để nâng cơ thể leo lên từng bậc.

(e) **Chuyển làn đường khi đang lái xe**: **Không thực hiện được**.
Việc chuyển làn xe đòi hỏi phải tạo ra một gia tốc theo phương ngang vuông góc với hướng đi ban đầu để dịch chuyển vị trí của xe sang làn bên cạnh, sau đó lại cần một gia tốc ngược lại để triệt tiêu vận tốc ngang khi đã vào làn mới. Trên mặt đường phẳng, lực ngang duy nhất có thể điều hướng chiếc xe là lực ma sát nghỉ ngang tác dụng lên các bánh xe đổi hướng. Không có ma sát, việc xoay vô lăng không tạo ra bất kỳ lực đẩy ngang nào, và chiếc xe tiếp tục giữ nguyên làn chuyển động theo quán tính.

</details>

### Q5.12 Trơn trượt trong bồn tắm ướt và hai hệ số ma sát

Khi bạn đứng bằng chân trần trong một bồn tắm ướt, cảm giác bám chân ban đầu có vẻ khá chắc chắn, nhưng một cú trượt ngã nguy hiểm vẫn hoàn toàn có thể bất ngờ xảy ra. Hãy giải thích hiện tượng này dựa trên hai hệ số ma sát.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Giải thích vì sao có thể đứng khá vững trên đáy bồn ướt, nhưng một khi trượt thì khó dừng lại, dựa vào hai hệ số ma sát.

**Hướng đi:** Phân biệt giới hạn ma sát nghỉ với độ lớn ma sát khi đã trượt. Không đồng nhất hệ số ma sát với lực ma sát thực tế ở mọi thời điểm.

**Lời giải:** Khi bàn chân chưa trượt, ma sát nghỉ điều chỉnh để cân bằng lực tiếp tuyến cần thiết, miễn là:

$$
f_s\le\mu_s n.
$$

Nếu lực tiếp tuyến cần thiết vượt giới hạn ấy, chân bắt đầu trượt. Trong mô hình ma sát của bài, hệ số trượt nhỏ hơn hệ số nghỉ, nên lực ma sát sau khi trượt có thể thấp hơn giới hạn trước đó:

$$
f_k=\mu_k n,\qquad \mu_k<\mu_s.
$$

Vì thế, lực đủ để giữ tư thế trước lúc trượt có thể không còn đủ để chống lại chuyển động khi đã trượt. Đây là lý do cảm giác bám lúc đứng yên không bảo đảm chân sẽ dừng ngay khi bắt đầu dịch chuyển.

Không cần giả định một cơ chế vi mô cụ thể của màng nước hoặc một mức chênh lệch hệ số định lượng mà đề chưa cho. Điểm cần dùng là sự khác nhau giữa ngưỡng ma sát nghỉ và ma sát trượt.

</details>

### Q5.13 Lực đẩy kiện hàng trong thang máy đang chuyển động

Bạn đang đẩy một kiện hàng lớn từ phía sau ra phía trước của một thang máy chở hàng trong khi thang máy đang di chuyển giữa các tầng. Lực bạn phải tác dụng để đẩy kiện hàng di chuyển là nhỏ nhất trong trường hợp nào, và lớn nhất trong trường hợp nào: Khi thang máy đang tăng tốc đi lên, khi thang máy đang tăng tốc đi xuống, hay khi thang máy chuyển động với tốc độ không đổi? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

So sánh lực đẩy kiện hàng $F$ trượt đều trên sàn thang máy trong 3 trường hợp: Thang máy gia tốc đi lên ($a_y > 0$), gia tốc đi xuống ($a_y < 0$), và chuyển động thẳng đều ($a_y = 0$).

**Hướng đi:**

1. Viết phương trình định luật II Newton cho kiện hàng theo phương thẳng đứng đối với hệ quy chiếu gắn với mặt đất: $n - mg = ma_y$, kéo theo $n = m(g + a_y)$.
2. Lực ma sát trượt cản trở kiện hàng trượt trên sàn tỷ lệ thuận với phản lực pháp tuyến: $f_{\mathrm{k}} = \mu_{\mathrm{k}} n = \mu_{\mathrm{k}} m(g + a_y)$.
3. Để đẩy kiện hàng chuyển động với vận tốc không đổi so với sàn thang máy, lực đẩy cần tác dụng phải cân bằng với lực ma sát trượt: $F = f_{\mathrm{k}}$.
4. So sánh giá trị của $F$ theo dấu của $a_y$.

**Lời giải:**

Xét kiện hàng khối lượng $m$ trên sàn thang máy đang có gia tốc thẳng đứng $a_y$ (chọn trục $+y$ hướng lên trên).

Theo định luật II Newton cho kiện hàng theo phương thẳng đứng:
$$
\sum F_y = n - mg = m a_y
$$

Suy ra lực pháp tuyến do sàn thang máy tác dụng lên kiện hàng (trọng lượng biểu kiến):
$$
n = m(g + a_y)
$$

Để đẩy kiện hàng di chuyển thẳng đều dọc theo sàn thang máy, lực đẩy nằm ngang $\vec{F}$ cần tác dụng phải có độ lớn cân bằng với lực ma sát trượt giữa kiện hàng và sàn:
$$
F = \mu_{\mathrm{k}} m(g + a_y)
$$

Xét 3 trường hợp:
1. **Khi thang máy tăng tốc đi lên ($a_y > 0$)**:
$$
n = m(g + a_y) > mg
$$
Phản lực pháp tuyến đạt cực đại, do đó lực ma sát trượt lớn nhất. Vì vậy, lực cần tác dụng để đẩy kiện hàng là **LỚN NHẤT**.

2. **Khi thang máy tăng tốc đi xuống ($a_y < 0$, với $|a_y| < g$)**:
$$
n = m(g - |a_y|) < mg
$$
Phản lực pháp tuyến nhỏ hơn trọng lượng thực tế, do đó lực ma sát trượt giảm xuống mức thấp nhất. Vì vậy, lực cần tác dụng để đẩy kiện hàng là **NHỎ NHẤT**.

3. **Khi thang máy chuyển động với tốc độ không đổi ($a_y = 0$)**:
$$
n = mg \implies F = \mu_{\mathrm{k}} mg
$$
Lực cần tác dụng ở mức trung bình giữa hai trường hợp trên.

So sánh này giả sử kiện hàng vẫn tiếp xúc với sàn, tức $g+a_y\ge0$, và lực đẩy không có thành phần đứng đáng kể.

</details>

### Q5.14 Phản biện quan niệm "ma sát luôn cản trở chuyển động"

Người ta thường nói rằng "lực ma sát luôn luôn cản trở chuyển động." Hãy đưa ra ít nhất một ví dụ trong đó (a) lực ma sát nghỉ gây ra chuyển động, và (b) lực ma sát trượt gây ra chuyển động.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Phản biện quan niệm sai lầm rằng ma sát chỉ có tác dụng cản trở chuyển động. Đưa ra ví dụ chứng minh: (a) Lực ma sát nghỉ đóng vai trò là lực phát động gây ra chuyển động; (b) Lực ma sát trượt đóng vai trò là lực phát động làm vật chuyển động.

**Hướng đi:**

1. Làm rõ định nghĩa chính xác: Lực ma sát luôn cản trở **chuyển động tương đối** giữa hai bề mặt tiếp xúc, chứ không nhất thiết cản trở chuyển động của vật thể so với hệ quy chiếu quán tính mặt đất.
2. Tìm ví dụ cho (a): Chuyển động đi bộ của người, ô tô tăng tốc trên đường, hoặc một chiếc hộp đặt trên thùng xe tải đang tăng tốc.
3. Tìm ví dụ cho (b): Một kiện hàng được thả nhẹ lên một băng tải đang chạy, hoặc quả bóng bowling trượt trên sàn gỗ trước khi lăn thuần túy.

**Lời giải:**

Quan niệm "ma sát luôn cản trở chuyển động" là một phát biểu thiếu chính xác. Theo bản chất vật lý, lực ma sát chỉ cản trở **chuyển động tương đối** giữa hai bề mặt tiếp xúc. Trong nhiều trường hợp đối với hệ quy chiếu gắn với mặt đất, lực ma sát lại chính là lực phát động làm cho vật thể chuyển động:

(a) **Ví dụ lực ma sát nghỉ gây ra chuyển động**:
- **Người đi bộ hoặc chạy**: Khi bạn bước đi, cơ chân đẩy đế giày về phía sau đối với mặt đất. Để chống lại xu hướng trượt lùi tương đối này, mặt đất tác dụng một lực ma sát nghỉ $\vec{f}_{\mathrm{s}}$ hướng về phía trước lên đế giày. Theo định luật II Newton, chính lực ma sát nghỉ này là ngoại lực duy nhất theo phương ngang đẩy toàn bộ cơ thể bạn tăng tốc chuyển động về phía trước từ trạng thái đứng yên.
- **Chiếc hộp trên thùng xe tải**: Một chiếc hộp đặt đứng yên trên sàn thùng xe tải. Khi xe tải tăng tốc về phía trước, chiếc hộp có xu hướng trượt lùi về phía sau so với sàn xe. Lực ma sát nghỉ do sàn xe tác dụng lên hộp hướng về phía trước, truyền gia tốc làm cho chiếc hộp chuyển động cùng với xe tải.

(b) **Ví dụ lực ma sát trượt gây ra chuyển động**:
- **Kiện hàng thả lên băng chuyền đang chuyển động**: Xét một băng tải chuyển động thẳng đều với vận tốc không đổi $v_{\mathrm{belt}}$ hướng sang phải. Người ta thả nhẹ một kiện hàng đang đứng yên ($v = 0$) lên mặt băng tải.
Vì băng tải chạy nhanh hơn kiện hàng, bề mặt kiện hàng trượt lùi tương đối so với mặt băng tải. Lực ma sát trượt do băng tải tác dụng lên kiện hàng hướng về phía trước (sang phải).
Chính lực ma sát trượt này đóng vai trò lực phát động, tạo ra gia tốc nằm ngang:
$$
a_x = \frac{f_{\mathrm{k}}}{m} = \mu_{\mathrm{k}} g
$$
làm cho kiện hàng tăng tốc chuyển động từ trạng thái đứng yên cho đến khi đạt vận tốc bằng vận tốc của băng tải.

</details>

### Q5.15 Bản chất của lực trong chuyển động tròn đều và sự bảo toàn tốc độ

Nếu luôn có một hợp lực khác không tác dụng lên một chất điểm đang chuyển động tròn đều, tại sao tốc độ của chất điểm lại không hề thay đổi?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Chất điểm chuyển động tròn đều chịu hợp lực hướng tâm khác không ($\vec{F}_{\mathrm{net}} \ne \vec{0}$). Giải thích tại sao tốc độ (độ lớn của vận tốc $v = |\vec{v}|$) lại giữ nguyên không đổi.

**Hướng đi:**

1. Xem xét hướng hình học của hợp lực trong chuyển động tròn đều: Hợp lực hướng tâm $\vec{F}_{\mathrm{rad}}$ luôn có phương vuông góc với véc-tơ vận tốc tức thời $\vec{v}$ tại mọi thời điểm ($\vec{F}_{\mathrm{rad}} \perp \vec{v}$).
2. Phân tích công và định lý động năng: Công cơ học vi phân $dW = \vec{F} \cdot d\vec{r} = (\vec{F} \cdot \vec{v}) dt$. Tích vô hướng của hai véc-tơ vuông góc bằng 0, do đó lực không sinh công, động năng không đổi, kéo theo tốc độ không đổi.
3. Phân tích thành phần gia tốc: Gia tốc tiếp tuyến $a_{\mathrm{tan}} = dv/dt = 0$, gia tốc hướng tâm chỉ làm thay đổi phương hướng của véc-tơ vận tốc chứ không làm thay đổi độ lớn.

**Lời giải:**

Trong chuyển động tròn đều, hợp lực tác dụng lên chất điểm là lực hướng tâm $\vec{F}_{\mathrm{net}} = \vec{F}_{\mathrm{rad}}$, luôn hướng thẳng vào tâm của quỹ đạo tròn.

Nguyên nhân tốc độ của chất điểm không đổi có thể được giải thích một cách chặt chẽ qua hai khía cạnh:

1. **Khía cạnh công và động năng**:
Véc-tơ vận tốc tức thời $\vec{v}$ của chất điểm luôn có phương tiếp tuyến với đường tròn quỹ đạo. Vì bán kính luôn vuông góc với tiếp tuyến, hợp lực $\vec{F}_{\mathrm{net}}$ luôn vuông góc với véc-tơ vận tốc $\vec{v}$ tại mọi thời điểm:
$$
\vec{F}_{\mathrm{net}} \cdot \vec{v} = 0
$$

Công suất cơ học do lực sinh ra bằng 0:
$$
P = \frac{dW}{dt} = \vec{F}_{\mathrm{net}} \cdot \vec{v} = 0
$$

Theo định lý động năng, độ biến thiên động năng của chất điểm bằng công của hợp lực:
$$
\frac{dK}{dt} = \frac{d}{dt}\left(\frac{1}{2}mv^2\right) = 0
$$

Vì lực không sinh bất kỳ công nào lên chất điểm nên động năng của nó được bảo toàn, do đó tốc độ $v$ không hề thay đổi.

2. **Khía cạnh thành phần gia tốc**:
Gia tốc tổng cộng của chất điểm phân tích thành hai thành phần:
- Gia tốc tiếp tuyến $a_{\mathrm{tan}} = \frac{dv}{dt}$ chịu trách nhiệm làm thay đổi độ lớn của vận tốc (tốc độ).
- Gia tốc pháp tuyến (hướng tâm) $a_{\mathrm{rad}} = \frac{v^2}{R}$ chịu trách nhiệm làm thay đổi hướng của véc-tơ vận tốc.

Trong chuyển động tròn đều, hợp lực chỉ có thành phần hướng tâm mà hoàn toàn không có thành phần tiếp tuyến ($F_{\mathrm{tan}} = 0$), do đó:
$$
a_{\mathrm{tan}} = \frac{dv}{dt} = 0
$$

Như vậy, hợp lực khác không này chỉ liên tục bẻ cong hướng chuyển động của chất điểm để giữ nó trên đường tròn mà không làm thay đổi tốc độ chuyển động.

</details>

### Q5.16 Khúc cua nghiêng phủ băng và nguy cơ trượt của xe chạy chậm

Một khúc cua trên đường có góc nghiêng được tính toán và cắm biển tốc độ thiết kế là $80\,\mathrm{km/h}$. Tuy nhiên, mặt đường đang bị phủ một lớp băng trơn trượt, vì vậy bạn cẩn thận lái xe chậm hơn giới hạn tốc độ này. Điều gì có thể xảy ra với chiếc xe của bạn? Tại sao?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Xe đi chậm hơn tốc độ thiết kế trên khúc cua nghiêng có rất ít ma sát.

**Hướng đi:** Ở tốc độ thiết kế, thành phần ngang của phản lực cung cấp vừa đủ gia tốc hướng tâm mà không cần ma sát. Tốc độ khác đi làm điều kiện lực dọc mặt nghiêng thay đổi.

**Lời giải:** Gọi tốc độ thiết kế là $v_0$ và bán kính cua là $R$. Với góc nghiêng $\beta$:

$$
\tan\beta=\frac{v_0^2}{gR}.
$$

Khi xe chạy chậm hơn $v_0$, muốn duy trì đúng quỹ đạo và độ cao thì cần một lực ma sát hướng lên mặt nghiêng. Đặt độ lớn gia tốc hướng tâm cần có là $a=v^2/R$. Nếu gọi chiều lên mặt nghiêng là chiều dương, lực ma sát cần thiết là:

$$
f=m(g\sin\beta-a\cos\beta).
$$

Vì $v<v_0$, biểu thức này cho $f>0$, tức lực phải hướng lên mặt nghiêng. Mặt đường phủ băng có thể không cung cấp đủ lực ấy. Khi đó xe trượt xuống phần thấp của mặt đường, tức về phía trong khúc cua. Chạy chậm hơn tốc độ thiết kế không tự bảo đảm xe giữ được quỹ đạo trên một mặt nghiêng gần như không ma sát.

</details>

### Q5.17 Dây treo con lắc quay tròn trong mặt phẳng ngang có thể nằm ngang tuyệt đối không

Bạn quay một quả bóng buộc ở đầu một sợi dây nhẹ theo một quỹ đạo tròn trong mặt phẳng nằm ngang với tốc độ không đổi. Sợi dây có bao giờ nằm ngang thực sự được không? Nếu không, nó sẽ nghiêng chếch lên trên hay chếch xuống dưới so với phương ngang? Tại sao?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Quả bóng chuyển động tròn đều trong mặt phẳng nằm ngang nhờ sợi dây kéo. Khảo sát xem sợi dây có thể nằm ngang tuyệt đối ($\beta = 0^\circ$ so với phương ngang) hay không, và xác định hướng nghiêng của dây (chếch lên hay chếch xuống so với điểm treo) kèm giải thích.

**Hướng đi:**

1. Liệt kê các lực thực tế tác dụng lên quả bóng: Trọng lực $\vec{w} = m\vec{g}$ hướng thẳng đứng xuống dưới và lực căng $\vec{T}$ của sợi dây hướng dọc theo sợi dây về phía điểm treo (hoặc tay cầm).
2. Quả bóng chuyển động trong mặt phẳng nằm ngang, do đó gia tốc thẳng đứng bằng 0 ($a_y = 0$).
3. Để triệt tiêu trọng lực $mg > 0$, bắt buộc phải có một thành phần lực hướng thẳng đứng lên trên.
4. Vì chỉ có lực căng dây tác dụng lên quả bóng, thành phần thẳng đứng $T_y$ của lực căng phải hướng lên và thỏa mãn $T_y = mg$.
5. Phân tích điều kiện hình học: Nếu dây nằm ngang thì $T_y = 0$ (mâu thuẫn). Suy ra dây phải nghiêng chếch xuống dưới từ tay cầm đến quả bóng (quả bóng nằm thấp hơn điểm treo).

**Lời giải:**

Sợi dây **không thể nằm ngang thực sự** trong trường trọng lực của Trái Đất.

1. Giải thích tại sao dây không thể nằm ngang:
Quả bóng có khối lượng $m$ luôn chịu tác dụng của trọng lực $\vec{w} = m\vec{g}$ hướng thẳng đứng xuống dưới.

Lực duy nhất còn lại tác dụng lên quả bóng là lực căng $\vec{T}$ của sợi dây, có phương dọc theo sợi dây.

Vì quả bóng chuyển động trong một mặt phẳng nằm ngang cố định nên gia tốc theo phương thẳng đứng bằng 0 ($a_y = 0$). Theo định luật I Newton, tổng các lực theo phương thẳng đứng phải triệt tiêu:
$$
T_y - mg = 0 \implies T_y = mg
$$

Điều này đòi hỏi lực căng dây bắt buộc phải có một thành phần hướng thẳng đứng lên trên khác không ($T_y > 0$).
Nếu sợi dây nằm ngang hoàn toàn, góc hợp bởi sợi dây và phương ngang bằng 0, khi đó:
$$
T_y = T \sin 0^\circ = 0
$$
Khi đó không có bất kỳ lực nào nâng đỡ quả bóng chống lại trọng lực, và quả bóng buộc phải rơi xuống. Để có $T_y = mg$ khi góc nghiêng tiến dần về 0 thì lực căng $T = mg / \sin\theta$ phải tiến ra vô hạn, điều không thể xảy ra trong thực tế.

2. Hướng nghiêng của sợi dây:
Vì lực căng tác dụng lên quả bóng phải có thành phần hướng lên trên ($T_y > 0$) về phía điểm treo (bàn tay giữ), điểm treo cố định trên trục thẳng đứng qua tâm quỹ đạo phải luôn **nằm cao hơn quả bóng**.
Nói cách khác, từ điểm treo nhìn ra quả bóng, sợi dây sẽ **nghiêng chếch xuống dưới so với phương ngang** (quả bóng chuyển động ở mặt phẳng nằm bên dưới điểm giữ).

</details>

### Q5.18 Lý do không đưa lực ly tâm vào giản đồ phân tích lực tự do

Lực ly tâm không được đưa vào các giản đồ phân tích lực tự do (FBD) trong các bài toán động lực học chuẩn mực. Hãy giải thích tại sao.



![Hình 5.34: Chuyển động quanh khúc cua và giản đồ lực trong hệ gắn với đất.](/vat-ly-1/bai-giang/img/young-05/r-exercises-ref-figure-5-34.png)

![Hình 5.35: Giản đồ lực tác dụng lên máy bay nghiêng cánh để bay vòng.](/vat-ly-1/bai-giang/img/young-05/r-exercises-ref-figure-5-35.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Giải thích vì sao các giản đồ lực được viện dẫn không đưa thêm lực ly tâm.

**Hướng đi:** Xác định hệ quy chiếu trước khi liệt kê lực. Trong hệ quán tính gắn với đất, hợp lực thực phải bằng khối lượng nhân gia tốc hướng tâm.

**Lời giải:** Những hình đang xét phân tích chuyển động trong hệ quán tính. Các lực thực như trọng lực, lực căng, phản lực và ma sát tạo nên hợp lực hướng vào tâm. Gia tốc là kết quả của hợp lực đó, không đòi hỏi thêm một lực hướng ra ngoài để cân bằng.

Nếu vừa dùng định luật Newton với gia tốc hướng tâm vừa đặt thêm lực ly tâm vào cùng giản đồ quán tính, phương trình sẽ tính thêm một lực không có trong mô hình ấy.

Trong hệ quay, có thể đưa lực quán tính ly tâm vào phương trình nếu đồng thời dùng đúng gia tốc và các lực quán tính của hệ quay. Vì vậy, kết luận ở đây áp dụng cho các giản đồ trong hệ quán tính được nêu ở câu hỏi, không phải một lệnh cấm cho mọi cách chọn hệ quy chiếu.

</details>

### Q5.19 Thí nghiệm nút cao su quay tròn và quỹ đạo khi buông tay

Một giáo sư quay một chiếc nút cao su theo một quỹ đạo tròn trong mặt phẳng nằm ngang ở đầu một sợi dây trước cả lớp học. Thầy nói với Caroline, một sinh viên ngồi ở hàng ghế đầu tiên, rằng thầy sẽ buông tay thả sợi dây ra ngay vào thời điểm chiếc nút cao su nằm đối diện trực diện trước mặt cô ấy. Caroline có cần phải lo lắng chiếc nút cao su sẽ bay đập trúng mặt mình không?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dây được buông khi nút cao su ở điểm trên đường tròn trực tiếp trước mặt Caroline. Cần xác định hướng chuyển động ngay khi lực căng mất đi.

**Hướng đi:** Vận tốc của chuyển động tròn theo tiếp tuyến. Buông dây làm mất lực giữ quỹ đạo, nhưng không đột ngột quay vận tốc sang phương bán kính.

**Lời giải:** Trong mô hình đang xét, nút không bay thẳng ra theo bán kính về phía Caroline. Tại điểm buông, vận tốc của nó tiếp tuyến với đường tròn, vuông góc với đường bán kính đi qua điểm ấy.

Theo phương ngang, khi lực căng không còn, nút tiếp tục đi theo hướng tiếp tuyến ban đầu. Trọng lực vẫn làm nó rơi theo phương đứng. Vì vậy, hướng bay ban đầu lệch sang bên, thay vì hướng thẳng từ tâm quay qua nút đến mặt Caroline.

Kết luận được suy từ vị trí và thời điểm buông đã nêu trong câu hỏi. Không dùng ý tưởng có một lực ly tâm thực làm nút đổi hướng đột ngột ra xa tâm khi dây được buông.

</details>

### Q5.20 Thiết kế hình dạng dải uốn lượn lộn đầu trong tàu lượn siêu tốc

Để giữ các lực tác dụng lên hành khách nằm trong giới hạn chịu đựng sinh lý cho phép, nhiều đường ray tàu lượn siêu tốc có vòng lộn đầu (loop-the-loop) không được thiết kế dưới dạng hình tròn hoàn hảo, mà thay vào đó có bán kính cong ở đáy vòng lộn lớn hơn nhiều so với bán kính cong ở đỉnh vòng lộn (đường cong hình giọt nước dạng clothoid). Hãy giải thích nguyên nhân.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Giải thích lợi ích của bán kính cong nhỏ ở đỉnh và lớn ở đáy vòng lộn trong việc giới hạn lực tác dụng lên hành khách.

**Hướng đi:** Tốc độ thường lớn hơn ở đáy. Gia tốc hướng tâm phụ thuộc cả tốc độ lẫn bán kính cong cục bộ. Cần xét phản lực lên hành khách ở từng vị trí, không chỉ nhìn hình dạng vòng.

**Lời giải:** Trong mô hình hành khách chịu trọng lực và lực đỡ của ghế, ở đáy vòng, gia tốc hướng lên nên:

$$
n_b=m\left(g+\frac{v_b^2}{R_b}\right).
$$

Vì tốc độ ở đáy lớn, chọn bán kính $R_b$ lớn giúp giảm thành phần $mv_b^2/R_b$ và lực ép lên người.

Ở đỉnh vòng, gia tốc hướng xuống. Khi lực đỡ cũng hướng về tâm:

$$
n_t=m\left(\frac{v_t^2}{R_t}-g\right).
$$

Một bán kính đỉnh nhỏ hơn cho phép đạt gia tốc hướng tâm cần thiết dù tốc độ ở đỉnh đã giảm. Kết hợp hai bán kính giúp tránh phải tăng quá lớn tốc độ ở đáy chỉ để đáp ứng điều kiện ở đỉnh.

Để thấy sự bất lợi của vòng tròn hoàn hảo bán kính $R$, bỏ qua tổn hao năng lượng. Chênh lệch độ cao đỉnh–đáy là $2R$, nên:

$$
v_b^2=v_t^2+4gR.
$$

Nếu ở đỉnh chỉ vừa đủ $v_t^2=gR$ để lực đỡ không âm, thì ở đáy $v_b^2=5gR$ và $n_b=6mg$. Đây là kết quả của mô hình lực, không phải một giới hạn sinh lý chung cho mọi hành khách hoặc mọi thời gian chịu lực.

</details>

### Q5.21 Phân biệt ảnh chụp chớp sáng rơi trong chân không và rơi trong không khí

Một quả bóng tennis được thả rơi từ trạng thái đứng yên tại miệng trên của một ống thủy tinh hình trụ cao. Lần thứ nhất, không khí bên trong ống được hút chân không hoàn toàn để không có lực cản không khí. Lần thứ hai, không khí được nạp trở lại vào trong ống. Bạn quan sát hai bức ảnh chụp chớp sáng nhiều lần (multiflash) của hai lần thả đó. Bạn có thể phân biệt được bức ảnh nào thuộc về lần thả nào không? Nếu có, bằng cách nào?

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** So hai ảnh chụp các vị trí của bóng sau những khoảng thời gian bằng nhau, một lần trong chân không và một lần có không khí.

**Hướng đi:** Khoảng cách giữa hai ảnh liên tiếp phản ánh tốc độ trung bình trong khoảng ấy. Gia tốc không đổi và gia tốc giảm dần cho hai quy luật khoảng cách khác nhau.

**Lời giải:** Trong chân không, bóng thả từ nghỉ có $y=gt^2/2$ nếu chọn chiều xuống dương. Với các lần chụp cách đều nhau một khoảng $\Delta t$, quãng đường giữa lần thứ $k-1$ và lần thứ $k$ là:

$$
\Delta y_k=\frac12g(2k-1)(\Delta t)^2.
$$

Các khoảng cách đầu tiên theo tỉ lệ $1:3:5$, và độ tăng của khoảng cách là không đổi.

Có không khí, lực cản tăng khi tốc độ tăng, nên gia tốc rơi nhỏ hơn $g$ và giảm dần. Khoảng cách giữa các ảnh tăng chậm hơn. Nếu thời gian đủ dài để tốc độ gần giới hạn, các khoảng cách ấy gần bằng nhau.

Do đó có thể nhận ra hai lần thả khi ảnh thể hiện đủ rõ ảnh hưởng của lực cản. Nếu ảnh quá ngắn hoặc độ phân giải không đủ để thấy sai khác, không nên chỉ dựa vào cảm giác về độ giãn của một vài vệt.

</details>

### Q5.22 So sánh tốc độ khi ném thẳng đứng lên và rơi trở lại

Bạn ném một quả bóng chày thẳng đứng lên trên với tốc độ ban đầu $v_0$. Khi quả bóng rơi trở lại đúng điểm mà bạn đã ném nó, tốc độ rơi của nó so với $v_0$ như thế nào trong hai trường hợp: (a) Khi không có lực cản không khí; (b) Khi có lực cản không khí? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Ném bóng thẳng đứng lên với tốc độ ban đầu $v_0$. So sánh tốc độ rơi về điểm ném $v_f$ với $v_0$ trong hai trường hợp: (a) Bỏ qua lực cản không khí; (b) Có lực cản không khí.

**Hướng đi:**

1. Áp dụng định luật bảo toàn cơ năng cho trường hợp (a): Trọng lực là lực thế, không có lực không thế sinh công nên cơ năng bảo toàn.
2. Áp dụng định lý biến thiên cơ năng cho trường hợp (b): Lực cản không khí là lực không thế luôn sinh công âm trong suốt cả quá trình bay lên và rơi xuống, làm tiêu hao cơ năng thành nhiệt năng.
3. So sánh động năng ở vị trí ban đầu và vị trí rơi về để rút ra kết luận về tốc độ.

**Lời giải:**

(a) **Khi không có lực cản không khí**:
Tốc độ rơi trở lại **bằng $v_0$** ($v_f = v_0$).
Giải thích: Lực duy nhất tác dụng lên quả bóng trong suốt chuyển động là trọng lực. Vì trọng lực là một lực thế (conservative force), cơ năng tổng cộng của hệ quả bóng - Trái Đất được bảo toàn nguyên vẹn:
$$
E = K + U = \text{const}
$$
Khi quả bóng rơi trở về đúng độ cao ban đầu, thế năng hấp dẫn không đổi ($U_f = U_i$). Do cơ năng bảo toàn, động năng của quả bóng khi trở về cũng phải bằng động năng ban đầu:
$$
K_f = K_i \implies v_f = v_0
$$

(b) **Khi có lực cản không khí**:
Tốc độ rơi trở lại **nhỏ hơn $v_0$** ($v_f < v_0$).
Giải thích: Lực cản không khí $\vec{f}_{\mathrm{drag}}$ là một lực không thế (lực tiêu tán), luôn có hướng ngược chiều với véc-tơ vận tốc tức thời của quả bóng:
- Khi quả bóng bay lên, véc-tơ vận tốc hướng lên, lực cản hướng xuống, sinh công âm: $W_{\mathrm{drag, up}} < 0$.
- Khi quả bóng rơi xuống, véc-tơ vận tốc hướng xuống, lực cản hướng lên, tiếp tục sinh công âm: $W_{\mathrm{drag, down}} < 0$.

Tổng công do lực cản không khí sinh ra trong toàn bộ hành trình khứ hồi là một số âm:
$$
W_{\mathrm{drag}} = W_{\mathrm{up}} + W_{\mathrm{down}} < 0
$$

Theo định lý biến thiên cơ năng:
$$
E_f - E_i = W_{\mathrm{drag}} < 0
$$

Khi trở về độ cao ném ban đầu, thế năng không đổi ($U_f = U_i$), vì vậy động năng lúc rơi về bắt buộc phải nhỏ hơn động năng ban đầu:
$$
K_f < K_i \implies v_f < v_0
$$

Một phần năng lượng cơ học ban đầu đã bị chuyển hóa không thuận nghịch thành nội năng (nhiệt năng) làm nóng quả bóng và không khí xung quanh, do đó tốc độ khi rơi về luôn nhỏ hơn tốc độ ném ban đầu.

</details>

### Q5.23 So sánh thời gian bay lên và thời gian rơi xuống khi có lực cản không khí

Bạn ném một quả bóng chày thẳng đứng lên trên. Nếu không bỏ qua lực cản không khí, thời gian quả bóng bay từ điểm ném lên đến độ cao cực đại so với thời gian nó rơi từ độ cao cực đại trở về điểm ném như thế nào? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Có xét lực cản không khí. So thời gian đi từ điểm ném lên đỉnh và từ đỉnh trở về đúng độ cao điểm ném.

**Hướng đi:** Ở cùng một độ cao dưới đỉnh, bóng ở nhánh xuống đã mất thêm cơ năng do lực cản so với lúc đi qua độ cao ấy trên nhánh lên. Vì hai nhánh đi qua cùng các độ cao, có thể so thời gian bằng tốc độ tại từng độ cao.

**Lời giải:** Gọi $u(y)$ là tốc độ lúc đi lên qua độ cao $y$, còn $d(y)$ là tốc độ lúc đi xuống qua cùng độ cao. Với lực cản tiêu tán năng lượng trong không khí đứng yên:

$$
u(y)>d(y)
$$

ở các độ cao thấp hơn đỉnh mà lực cản có tác dụng. Đi qua cùng một đoạn độ cao nhỏ, thời gian bằng độ dài đoạn đó chia tốc độ. Vì tốc độ nhánh xuống nhỏ hơn, thời gian nhánh xuống lớn hơn.

Nếu độ cao tăng thêm cực đại là $H$, viết theo độ lớn vận tốc:

$$
t_{\mathrm{up}}=\int_0^H\frac{dy}{u(y)},
$$

$$
t_{\mathrm{down}}=\int_0^H\frac{dy}{d(y)}.
$$

Suy ra $t_{\mathrm{up}}<t_{\mathrm{down}}$. Ở đỉnh, cả hai tốc độ cùng tiến về không, nhưng các tích phân thời gian vẫn hữu hạn trong mô hình chuyển động này. Về lực, khi bóng đi lên thì trọng lực và lực cản cùng hãm chuyển động. Khi bóng đi xuống, lực cản chống lại trọng lực.

</details>

### Q5.24 So sánh hai quả bóng tennis rỗng và chứa đầy nước khi thả rơi

Bạn có hai quả bóng tennis hoàn toàn giống hệt nhau về kích thước và vỏ ngoài, nhưng một quả được bơm đầy nước vào bên trong. Bạn thả cả hai quả bóng cùng lúc từ tầng thượng của một tòa nhà cao tầng. Nếu bỏ qua lực cản không khí, quả bóng nào chạm đất trước? Nếu không bỏ qua lực cản không khí thì sao? Hãy giải thích.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Hai quả bóng cùng hình dạng và thể tích bên ngoài, nhưng một quả chứa nước (khối lượng lớn $m_{\mathrm{heavy}}$) và một quả rỗng chứa không khí (khối lượng nhỏ $m_{\mathrm{light}}$). So sánh thời gian chạm đất khi thả từ tòa nhà cao: (a) Không có lực cản không khí; (b) Có lực cản không khí.

**Hướng đi:**

1. Khi không có lực cản không khí: Cả hai quả bóng chỉ chịu tác dụng của trọng lực. Gia tốc rơi tự do $a = mg / m = g$, không phụ thuộc vào khối lượng.
2. Khi có lực cản không khí: Vì hai quả bóng có cùng hình dạng hình học và kích thước bề mặt, tại cùng một tốc độ rơi $v$, chúng chịu cùng một lực cản không khí $f_{\mathrm{drag}} = D v^2$.
3. Phương trình gia tốc: $a = g - f_{\mathrm{drag}} / m$. Quả bóng nặng hơn chịu gia tốc cản $f_{\mathrm{drag}} / m$ nhỏ hơn, do đó gia tốc thực tế của nó lớn hơn tại mọi tốc độ.
4. Tốc độ giới hạn: Giá trị $v_{\mathrm{t}} = \sqrt{mg / D}$ của quả bóng nặng lớn hơn quả bóng nhẹ.

**Lời giải:**

1. **Trường hợp bỏ qua lực cản không khí**:
Cả hai quả bóng sẽ **chạm đất cùng lúc**.
Giải thích: Theo định luật II Newton, gia tốc của một vật rơi tự do chỉ chịu tác dụng của trọng lực là:
$$
a = \frac{\sum F}{m} = \frac{mg}{m} = g
$$
Gia tốc này hoàn toàn độc lập với khối lượng của vật thể. Vì cả hai quả bóng được thả đồng thời từ cùng một độ cao với vận tốc ban đầu bằng 0 và có cùng gia tốc $g$, chúng sẽ có vận tốc và quãng đường rơi hoàn toàn như nhau tại mọi thời điểm, do đó chạm đất đồng thời.

2. **Trường hợp không bỏ qua lực cản không khí**:
Quả bóng **chứa đầy nước chạm đất trước**.
Giải thích:
Hai quả bóng có cùng hình dạng hình cầu, cùng đường kính và cùng chất liệu vỏ ngoài, vì vậy tại bất kỳ tốc độ rơi $v$ nào, chúng đều chịu cùng một độ lớn lực cản không khí:
$$
f_{\mathrm{drag}} = D v^2
$$
với hệ số cản $D$ là như nhau cho cả hai quả bóng.

Phương trình động lực học cho từng quả bóng:
$$
a = g - \frac{f_{\mathrm{drag}}}{m}
$$

Vì quả bóng chứa nước có khối lượng lớn hơn so với quả bóng rỗng ($m_{\mathrm{water}} > m_{\mathrm{empty}}$), số hạng gia tốc cản của nó nhỏ hơn:
$$
\frac{f_{\mathrm{drag}}}{m_{\mathrm{water}}} < \frac{f_{\mathrm{drag}}}{m_{\mathrm{empty}}}
$$

Do đó, tại cùng một tốc độ, gia tốc rơi của quả bóng chứa nước luôn lớn hơn gia tốc rơi của quả bóng rỗng:
$$
a_{\mathrm{water}} > a_{\mathrm{empty}}
$$

Ngoài ra, tốc độ giới hạn (khi lực cản cân bằng trọng lực) của quả bóng chứa nước lớn hơn nhiều:
$$
v_{\mathrm{t}} = \sqrt{\frac{mg}{D}} \propto \sqrt{m}
$$

Quả bóng chứa nước ít bị ảnh hưởng bởi lực cản không khí hơn so với quán tính của nó, duy trì gia tốc rơi lớn hơn trong suốt quãng đường và đạt tốc độ rơi cao hơn, vì vậy nó sẽ chạm đất trước quả bóng rỗng.

</details>

### Q5.25 Đồ thị gia tốc theo thời gian của vật rơi có lực cản không khí

Một quả bóng được thả rơi từ trạng thái đứng yên và chịu lực cản của không khí trong khi rơi. Đồ thị nào trong Hình Q5.25 biểu diễn đúng nhất gia tốc của quả bóng theo thời gian?

![Hình Q5.25: Năm phương án đồ thị gia tốc theo thời gian.](/vat-ly-1/bai-giang/img/young-05/r-exercises-fig-q5-25.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Bóng bắt đầu rơi từ nghỉ, có lực cản. Cần chọn đồ thị gia tốc theo thời gian trong Hình Q5.25.

**Hướng đi:** Chọn chiều xuống dương. Lực cản ban đầu bằng không, rồi tăng khi tốc độ tăng. Hợp lực và gia tốc vì thế giảm dần về không khi bóng tiến tới tốc độ giới hạn.

**Lời giải:** Chọn phương án (d). Lúc vừa thả, $a(0)=g$. Trong khi bóng nhanh dần:

$$
a=g-\frac{F_c}{m}.
$$

Độ lớn lực cản $F_c$ tăng từ không, làm gia tốc giảm. Ở giới hạn rơi đều, $F_c=mg$ và gia tốc tiến về không.

Trong hình, (a) là gia tốc dương không đổi. Các phương án (b) và (c) tăng từ không, trái với điều kiện lúc thả. Phương án (e) giảm nhưng còn một giá trị dương khác không ở phía sau. Chỉ (d) thể hiện gia tốc dương giảm về không như yêu cầu.

</details>

### Q5.26 Đồ thị thành phần vận tốc thẳng đứng theo thời gian

Một quả bóng được thả rơi từ trạng thái đứng yên và chịu lực cản của không khí trong khi rơi. Đồ thị nào trong Hình Q5.26 biểu diễn đúng nhất thành phần vận tốc theo phương thẳng đứng của quả bóng theo thời gian, nếu quy ước chiều dương $+y$ hướng thẳng đứng xuống dưới?

![Hình Q5.26: Năm phương án đồ thị thành phần vận tốc đứng theo thời gian.](/vat-ly-1/bai-giang/img/young-05/r-exercises-fig-q5-26.png)

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Bóng được thả từ nghỉ và rơi trong không khí. Chọn chiều thẳng đứng xuống là dương, rồi chọn đồ thị vận tốc theo thời gian trong Hình Q5.26.

**Hướng đi:** Vận tốc bắt đầu bằng không. Độ dốc đồ thị là gia tốc, ban đầu bằng $g$ rồi giảm khi lực cản tăng. Khi gần tốc độ giới hạn, độ dốc tiến về không.

**Lời giải:** Chọn phương án (a). Vận tốc tăng từ $v(0)=0$, nhưng tăng ngày càng chậm. Đồ thị có độ dốc dương và giảm dần, rồi tiến về đường nằm ngang ở tốc độ giới hạn.

Phương án (b) mô tả vận tốc giảm từ một giá trị ban đầu dương. Phương án (c) có độ dốc tăng, còn (d) có độ dốc không đổi. Phương án (e) cũng không xuất phát từ trạng thái nghỉ. Vì vậy các phương án ấy không mô tả chuyển động đã cho.

Tốc độ tiến tới giá trị không đổi không có nghĩa bóng đứng yên. Nó vẫn rơi xuống, trong khi lực cản gần cân bằng với trọng lực.

</details>

### Q5.27 Quãng đường nằm ngang của quả bóng chày khi bay lên và khi rơi xuống

Khi một quả bóng chày bị đánh bay đi chuyển động trong không khí có lực cản, quả bóng sẽ di chuyển được quãng đường theo phương ngang lớn hơn trong giai đoạn nào? (i) Trong giai đoạn đang bay lên tới độ cao cực đại; (ii) trong giai đoạn đang rơi từ độ cao cực đại trở lại mặt đất; (iii) cả hai giai đoạn bằng nhau. Hãy giải thích dựa trên các lực tác dụng lên quả bóng.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** So quãng đường ngang khi bóng bay lên đỉnh và khi từ đỉnh trở về độ cao mặt đất ban đầu, trong không khí đứng yên có lực cản.

**Hướng đi:** Lực cản làm vận tốc ngang giảm, còn trọng lực luôn hướng xuống. Để so hai quãng đường, cần xét cả hình dạng quỹ đạo, vì thời gian của hai nhánh không bằng nhau.

**Lời giải:** Chọn (i), quãng đường ngang khi đi lên lớn hơn. Chọn $x$ theo hướng phóng ngang và $y$ hướng lên. Viết lực cản dưới dạng ngược chiều vận tốc với hệ số không âm $\kappa(v)$. Hai phương trình thành phần là:

$$
ma_x=-\kappa(v)v_x,
$$

$$
ma_y=-mg-\kappa(v)v_y.
$$

Vì $v_x>0$, thành phần $v_x$ giảm dần. Nếu dùng mô hình lực cản tỉ lệ bình phương tốc độ, hệ số ở đây là $\kappa(v)=Dv$.

Độ dốc quỹ đạo là $dy/dx=v_y/v_x$. Lấy đạo hàm theo $x$ cho:

$$
\begin{aligned}
\frac{d^2y}{dx^2}&=\frac{a_yv_x-a_xv_y}{v_x^3}\\
&=-\frac{g}{v_x^2}.
\end{aligned}
$$

Hai thành phần lực cản triệt tiêu trong tử số, nhưng lực cản vẫn làm $v_x$ giảm. Do đó độ cong xuống, tính theo cùng một đoạn ngang, tăng dần trong hành trình.

Từ đỉnh, hai nhánh cùng bắt đầu với độ dốc bằng không. Xét hai đoạn ngang dài bằng nhau về hai phía của đỉnh, nhánh xuống có $v_x$ nhỏ hơn nên tụt độ cao nhiều hơn. Vì thế nó trở về độ cao mặt đất sau một đoạn ngang ngắn hơn nhánh lên. Chỉ lập luận rằng vận tốc ngang ở nhánh xuống nhỏ hơn, mà bỏ qua chênh lệch thời gian, chưa đủ để so hai quãng đường.

</details>

### Q5.28 Quỹ đạo tiệm cận thẳng đứng của vật ném chịu lực cản không khí

Một quả bóng được ném ra từ mép của một vách đá cao. Người ta khẳng định rằng: "Bất kể quả bóng được ném đi theo góc nào, do lực cản của không khí, cuối cùng quả bóng cũng sẽ chuyển động theo phương thẳng đứng hướng xuống." Hãy chứng minh tính đúng đắn của nhận định này.

<details>
<summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Giải thích xu hướng hướng xuống thẳng đứng của vật ném từ vách cao khi thời gian rơi đủ dài và có lực cản không khí.

**Hướng đi:** Trọng lực không duy trì chuyển động ngang. Lực cản làm vận tốc ngang tắt dần, còn chuyển động đứng tiến tới tốc độ giới hạn khi trọng lực cân bằng lực cản.

**Lời giải:** Chọn trục $x$ nằm ngang và trục $y$ hướng xuống. Với lực cản ngược vận tốc:

$$
m\frac{dv_x}{dt}=-\kappa(v)v_x,
$$

$$
m\frac{dv_y}{dt}=mg-\kappa(v)v_y.
$$

Thành phần ngang bị giảm độ lớn vì không có lực ngoài duy trì nó. Khi chuyển động tiến tới trạng thái giới hạn, $v_x\to0$, còn $v_y\to v_t>0$, với:

$$
\kappa(v_t)v_t=mg.
$$

Trong mô hình lực cản $F_c=Dv^2$, tốc độ giới hạn là:

$$
v_t=\sqrt{\frac{mg}{D}}.
$$

Vì vậy, theo quy ước chiều xuống dương đã chọn:

$$
\vec v\longrightarrow(0,v_t).
$$

Hướng vận tốc tiến tới thẳng đứng xuống dưới, không phụ thuộc việc ban đầu bóng được ném chếch lên, ngang hay chếch xuống. Đây là xu hướng khi vật có đủ thời gian để tiến gần trạng thái giới hạn. Với một độ cao hữu hạn, không nhất thiết thành phần ngang đã bằng đúng không trước lúc chạm đất.

</details>
