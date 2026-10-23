## Tóm tắt chương 11: Trạng thái cân bằng và tính đàn hồi

## Các Điều Kiện Cân Bằng Của Vật Rắn

Để một vật rắn ở trạng thái cân bằng tĩnh học hoàn toàn, hai điều kiện độc lập sau đây bắt buộc phải được thỏa mãn đồng thời:

1. **Điều kiện thứ nhất (Cân bằng lực chuyển động tịnh tiến)**:
Tổng vector của tất cả các ngoại lực tác dụng lên vật rắn phải bằng không:
$$
\sum \vec{F} = \vec{0}
\tag{11.1}
$$

2. **Điều kiện thứ hai (Cân bằng momen lực quay)**:
Tổng vector của tất cả các momen lực do ngoại lực gây ra đối với một điểm quy chiếu tùy ý bất kỳ phải bằng không:
$$
\sum \vec{\tau} = \vec{0}
\tag{11.2}
$$

![Sơ đồ cân bằng lực và momen trên thanh](./img/young-11/b-tom-tat-11-can-bang.png)

Momen lực do trọng lượng của vật thể gây ra có thể được xác định bằng cách giả định toàn bộ trọng lượng của vật tập trung tại trọng tâm (Center of gravity). Nếu gia tốc trọng trường $\vec{g}$ có cùng độ lớn và cùng hướng tại mọi điểm trong không gian của vật thể, trọng tâm sẽ trùng hoàn toàn với khối tâm (Center of mass):
$$
\vec{r}_{\text{cm}} = \frac{\sum m_i \vec{r}_i}{\sum m_i}
\tag{11.4}
$$

## Ứng Suất, Biến Dạng và Định Luật Hooke

Định luật Hooke khẳng định: Trong miền biến dạng đàn hồi nhỏ, ứng suất (lực trên mỗi đơn vị diện tích) tỷ lệ thuận với biến dạng (độ biến dạng hình học tỉ đối). Hằng số tỷ lệ đặc trưng cho vật liệu được gọi là modun đàn hồi:
$$
\frac{\text{Stress}}{\text{Strain}} = \text{Modulus}
\tag{11.7}
$$

## Ứng Suất Kéo và Ứng Suất Nén

Ứng suất kéo là độ lớn của lực kéo vuông góc trên một đơn vị diện tích: $F_\perp / A$. Biến dạng kéo là độ dãn dài tỉ đối: $\Delta l / l_0$. Modun đàn hồi tương ứng với biến dạng kéo được gọi là modun Young, ký hiệu là $Y$:
$$
Y = \frac{\text{Tensile stress}}{\text{Tensile strain}}
$$
$$
Y = \frac{F_\perp / A}{\Delta l / l_0} = \frac{F_\perp l_0}{A \Delta l}
\tag{11.10}
$$

![Sơ đồ biến dạng kéo dọc trục](./img/young-11/b-tom-tat-11-keo-nen.png)

Ứng suất nén và biến dạng nén được định nghĩa hoàn toàn tương tự, với $\Delta l$ mang ý nghĩa là độ co ngắn lại của vật thể.

## Ứng Suất Khối

Áp suất trong một chất lưu tĩnh là lực nén vuông góc tác dụng lên mỗi đơn vị diện tích bề mặt:
$$
p = \frac{F_\perp}{A}
\tag{11.11}
$$

Ứng suất khối là độ biến thiên áp suất $\Delta p$. Biến dạng khối là độ biến thiên thể tích tỉ đối $\Delta V / V_0$. Modun đàn hồi tương ứng với ứng suất nén từ mọi phía được gọi là modun khối, ký hiệu là $B$:
$$
B = -\frac{\text{Bulk stress}}{\text{Bulk strain}}
$$
$$
B = -\frac{\Delta p}{\Delta V / V_0}
\tag{11.13}
$$

![Sơ đồ biến dạng nén thể tích khối](./img/young-11/b-tom-tat-11-the-tich.png)

Độ nén $k$ là đại lượng nghịch đảo của modun khối:
$$
k = \frac{1}{B} = -\frac{1}{V_0} \frac{\Delta V}{\Delta p}
$$

## Ứng Suất Trượt

Ứng suất trượt là lực tiếp tuyến trên mỗi đơn vị diện tích: $F_\parallel / A$, đối với một lực tác dụng tiếp tuyến song song với bề mặt tiếp xúc. Biến dạng trượt là độ dịch chuyển ngang $x$ của một mặt chia cho khoảng cách vuông góc $h$ giữa hai mặt đối diện: $x / h$.

Modun đàn hồi tương ứng với biến dạng trượt được gọi là modun trượt, ký hiệu là $S$:
$$
S = \frac{\text{Shear stress}}{\text{Shear strain}}
$$
$$
S = \frac{F_\parallel / A}{x / h} = \frac{F_\parallel h}{A x}
\tag{11.17}
$$

![Sơ đồ biến dạng trượt của khối](./img/young-11/b-tom-tat-11-truot.png)

## Các Giới Hạn Của Định Luật Hooke

- **Giới hạn tỷ lệ (Proportional limit)**: Là giá trị ứng suất cực đại mà tại đó ứng suất và biến dạng còn tỷ lệ thuận tuyến tính với nhau. Vượt qua giới hạn tỷ lệ, định luật Hooke không còn hiệu lực.
- **Giới hạn đàn hồi hay điểm chảy (Elastic limit / Yield point)**: Là ngưỡng ứng suất mà nếu vượt qua nó, vật thể sẽ bị biến dạng dẻo vĩnh viễn không thể tự phục hồi lại hình dạng ban đầu.
- **Giới hạn bền hay ứng suất đứt (Breaking stress / Ultimate strength)**: Là giá trị ứng suất lớn nhất mà vật liệu có thể chịu đựng được trước khi bị đứt gãy hoàn toàn.
