## 1.6. Ước lượng và bậc độ lớn

Biết độ chính xác của con số biểu diễn đại lượng vật lý là điều cần thiết. Tuy nhiên, ngay cả một ước lượng rất thô vẫn có thể cung cấp thông tin định hướng hữu ích. Có những tình huống ta biết rõ quy luật vật lý để tính đại lượng nhưng buộc phải phỏng đoán dữ kiện đầu vào. Cũng có những trường hợp phép tính chính xác quá phức tạp, nên ta chủ động áp dụng các phép gần đúng thô. Trong cả hai trường hợp, kết quả thu được là một ước lượng, nhưng vẫn mang giá trị thực tiễn cao dù có thể sai khác gấp đôi, gấp mười hoặc hơn.

Những phép tính gần đúng như vậy được gọi là **ước lượng bậc độ lớn**. Nhà vật lý hạt nhân người Mỹ gốc Ý Enrico Fermi (1901–1954) gọi chúng là những “phép tính trên mặt sau phong bì”.

Các bài tập 1.15–1.20 ở cuối chương thuộc dạng ước lượng bậc độ lớn. Phần lớn các bài toán dạng này cần đưa ra phỏng đoán hợp lý về dữ liệu ban đầu. Ngay cả khi kết quả chênh lệch một hệ số mười, con số thu được vẫn cung cấp bức tranh tổng thể đáng tin cậy để đưa ra các quyết định kỹ thuật kịp thời.

### Ví dụ 1.4: Ước lượng bậc độ lớn của một tỷ đô la vàng

::: exercise Ví dụ 1.4: Ước lượng bậc độ lớn của một tỷ đô la vàng
Bạn đang viết một cuốn tiểu thuyết phiêu lưu, trong đó nhân vật chính tìm cách bỏ trốn cùng số vàng thoi trị giá một tỷ đô la ($10^9\,\text{USD}$) cất giấu trong một chiếc va li. Một người bình thường có thể mang vác nổi số vàng ấy không? Và số vàng ấy có thể chứa vừa vặn trong một chiếc va li thông thường không?
:::

::: solution Lời giải
**Tóm tắt đề bài**:
- Tổng giá trị vàng: $10^9\,\text{USD}$.
- Đơn giá giả định của vàng: Khoảng $1400\,\text{USD/oz}$ (tương đương khoảng $100\,\text{USD}$ cho $1/14\,\text{oz}$).
- Quy đổi khối lượng: $1\,\text{oz} \approx 30\,\mathrm g$.
- Khối lượng riêng của nước: $\rho_{\text{nước}} \approx 10^3\,\mathrm{kg/m^3}$.
- Khối lượng riêng ước tính của vàng: $\rho_{\text{vàng}} \approx 10^4\,\mathrm{kg/m^3}$ (lấy gần đúng bằng 10 lần khối lượng riêng của nước).
- Cần ước lượng: Tổng khối lượng $m$ và tổng thể tích $V$ của số vàng.

**Hướng đi**:
- Tìm khối lượng vàng mà $100\,\text{USD}$ có thể mua được, sau đó nhân với $10^7$ để ra khối lượng của $10^9\,\text{USD}$.
- Từ khối lượng và khối lượng riêng ước tính của kim loại nặng, suy ra thể tích tương ứng: $V = m / \rho$.

**Lời giải chi tiết**:
Bước 1. Ước lượng tổng khối lượng vàng:
   Một ounce vàng có khối lượng khoảng $30\,\mathrm g$. Với đơn giá khoảng $1400\,\text{USD/oz}$, số tiền $100\,\text{USD}$ mua được khoảng $1/14\,\text{oz}$, tức xấp xỉ $2\,\mathrm g$ vàng.
   Số tiền một tỷ đô la ($10^9\,\text{USD}$) lớn gấp $10^7$ lần số tiền $100\,\text{USD}$. Do đó tổng khối lượng vàng là:

$$
\begin{aligned}
m &\approx (2\,\mathrm g)\times10^7 \\
&= 2\times10^7\,\mathrm g \\
&= 2\times10^4\,\mathrm{kg}.
\end{aligned}
$$

Khối lượng này tương đương $20$ tấn (khoảng $20$ ton theo đơn vị Anh). Rõ ràng không có người nào có thể mang vác nổi khối lượng khổng lồ này.

Bước 2. Ước lượng thể tích vàng:
   Vàng là kim loại rất đặc. Lấy khối lượng riêng ước lượng theo bậc độ lớn là $\rho \approx 10^4\,\mathrm{kg/m^3}$. Thể tích số vàng chiếm chỗ là:

$$
\begin{aligned}
V &\approx \frac{m}{\rho} \\
&= \frac{2\times10^4\,\mathrm{kg}}{10^4\,\mathrm{kg/m^3}} \\
&= 2\,\mathrm{m^3}.
\end{aligned}
$$

Thể tích $2\,\mathrm{m^3}$ lớn hơn nhiều thể tích của một chiếc va li.

**Đánh giá**:
Cả hai khía cạnh khối lượng và thể tích đều khẳng định tình tiết trong tiểu thuyết là hoàn toàn phi thực tế. Nhân vật không thể nhấc nổi và chiếc va li cũng không thể chứa hết số vàng.
Hãy thử lại với những viên kim cương năm carat, tức $1\,\mathrm g$ mỗi viên, giả sử mỗi viên trị giá $500\,000\,\text{USD}$. Với dữ kiện giá trị này, cần $2000$ viên để đạt một tỷ đô la. Tổng khối lượng chỉ là $2\,\mathrm{kg}$, nên trở ngại mang vác đã được khắc phục. Muốn quyết định chúng có vừa va li hay không, còn cần ước lượng thể tích và cách sắp xếp các viên kim cương.
:::

### Câu hỏi tự kiểm tra hiểu bài 1.6

::: exercise Câu hỏi tự kiểm tra 1.6: Ước lượng tổng số răng của sinh viên trên giảng đường
Bạn có thể ước lượng tổng số răng trong miệng của tất cả các sinh viên đang theo học tại trường đại học của mình không?
(Gợi ý: Hãy đếm số răng của chính mình, rồi ước lượng số sinh viên trong trường.)
:::

::: solution Lời giải chi tiết
**Lời giải ước lượng theo bậc độ lớn**:
Bước 1. Một người trưởng thành thông thường có $32$ chiếc răng (tính cả răng khôn), tức vào khoảng $30$ chiếc răng:

$$
N_{\text{răng/người}} \approx 3\times 10^1.
$$

Bước 2. Kết quả phụ thuộc số sinh viên thực tế của trường. Để minh họa phép ước lượng, giả sử trường có khoảng $10^4$ sinh viên:

$$
N_{\text{sinh viên}} \approx 10^4.
$$

Bước 3. Tổng số lượng răng của toàn bộ sinh viên trong trường:

$$
\begin{aligned}
N_{\text{tổng}} &\approx N_{\text{răng/người}}N_{\text{sinh viên}} \\
&\approx (3\times 10^1)(10^4) \\
&= 3\times 10^5.
\end{aligned}
$$

Con số này tương ứng khoảng $300\,000$ chiếc răng.

**Đánh giá**:
Bậc độ lớn của tổng số răng là khoảng vài trăm nghìn chiếc (cỡ $10^5$ chiếc răng). Dù số lượng sinh viên ở mỗi trường có thể khác nhau, cần thay số sinh viên ước lượng của trường đang xét vào phép tính. Con số minh họa trên không phải thống kê về một trường cụ thể.
:::
