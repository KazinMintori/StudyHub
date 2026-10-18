## Đọc hình và đối chiếu với dữ liệu

Một lệnh vẽ chạy được mới chỉ tạo ra hình. Ta còn phải kiểm tra hình có trả lời đúng câu hỏi và có cho người đọc thấy các điều kiện so sánh hay không.

### Biểu đồ thanh cho số lượng theo nhóm

![Hình 9.1: Số sản phẩm bán được của ba nhóm Sách, Vở và Bút.](img/lec-12/ban-theo-nhom.svg)

Mỗi thanh biểu diễn một nhóm hàng. Độ dài thanh tính từ mốc 0 biểu diễn số sản phẩm bán được. Thứ tự các nhóm không diễn tả thời gian, vì vậy không nối các đỉnh thanh thành một đường xu hướng.

::: exercise Tính tỷ trọng từ số lượng
Ba nhóm Sách, Vở và Bút lần lượt bán được 12, 8 và 5 sản phẩm. Hãy tính tổng số sản phẩm và tỷ trọng của từng nhóm. Nếu chuyển biểu đồ sang tỷ trọng, nhãn trục tung phải thay đổi thế nào?
:::

::: solution
Tổng số sản phẩm là 25. Chia từng số lượng cho 25 rồi nhân 100, ta được 48%, 32% và 20%. Trục đo phải ghi “Tỷ trọng sản phẩm (%)” thay cho “Số sản phẩm”. Tỷ trọng này dùng tổng số sản phẩm làm mẫu số, không dùng số nhóm hàng.

```python
import numpy as np
so_luong = np.array([12, 8, 5])
ty_trong = so_luong / so_luong.sum() * 100
assert so_luong.sum() == 25
np.testing.assert_allclose(ty_trong, [48, 32, 20])
```
:::

### Histogram đếm quan sát trong khoảng

![Hình 9.2: Phân phối mười mức giá với bốn khoảng có bề rộng bằng nhau.](img/lec-12/phan-phoi-gia.svg)

Histogram gom các giá trị số vào khoảng rồi đếm. Một cột có thể chứa nhiều giá trị khác nhau, nên không thể đọc lại từng quan sát chỉ từ hình. Trong hình này, các khoảng có cùng bề rộng và trục tung biểu diễn số mặt hàng.

::: exercise Kiểm tra biên khoảng
Cho dãy giá `[10, 12, 14, 16, 20, 20, 24, 28, 30, 36]`, đơn vị nghìn đồng, và các biên `[0, 10, 20, 30, 40]`. Hãy tính số quan sát trong từng khoảng theo quy tắc của `np.histogram`. Hai giá trị 20 thuộc khoảng nào?
:::

::: solution
Ba khoảng đầu nhận cận trái và không nhận cận phải. Khoảng cuối nhận cả cận phải. Số quan sát lần lượt là 0, 4, 4 và 2. Cả hai giá trị 20 thuộc khoảng từ 20 đến dưới 30, không thuộc khoảng từ 10 đến dưới 20.

```python
gia = np.array([10, 12, 14, 16, 20, 20, 24, 28, 30, 36])
tan_so, bien = np.histogram(gia, bins=[0, 10, 20, 30, 40])
assert tan_so.tolist() == [0, 4, 4, 2]
assert tan_so.sum() == len(gia)
```
:::

### Thang đo làm thay đổi độ dài nhìn thấy

![Hình 9.3: Cùng số lượng 98 và 100 sản phẩm, hai cách đặt mốc đầu trục tạo ra tỷ lệ chiều dài khác nhau.](img/lec-13/so-sanh-truc.svg)

Ở hình bên trái, chiều dài thanh được đo từ 0. Ở hình bên phải, đoạn được vẽ chỉ bắt đầu từ 97. Đọc số trên trục vẫn cho đúng hai giá trị, nhưng so sánh chiều dài thanh ở hình bên phải không còn là so sánh tỷ lệ 100 với 98.

::: exercise Phân biệt chênh lệch và tỷ lệ
Tính mức tăng từ 98 lên 100 sản phẩm theo đơn vị sản phẩm và theo phần trăm. Trong hình dùng mốc 97, hai đoạn thanh nhìn thấy có tỷ lệ chiều dài bao nhiêu? Vì sao không được dùng tỷ lệ ấy để nói số sản phẩm tăng gấp ba?
:::

::: solution
Mức tăng là 2 sản phẩm, tương đương khoảng 2,04% so với 98 sản phẩm ban đầu. Các đoạn thanh trong hình bên phải dài 1 và 3 đơn vị, nên tỷ lệ chiều dài là 3. Chúng biểu diễn phần vượt mốc 97, không biểu diễn toàn bộ số sản phẩm.

```python
import math
assert 100 - 98 == 2
assert math.isclose((100 - 98) / 98 * 100, 2.0408163265306123)
assert (100 - 97) / (98 - 97) == 3
```
:::

### Boxplot và các quan sát riêng lẻ

![Hình 9.4: Boxplot của hai nhóm giá, kèm từng quan sát để thấy rõ cỡ mẫu và điểm nằm ngoài râu.](img/lec-13/boxplot.svg)

Hộp tóm tắt trung vị và hai tứ phân vị. Với quy tắc râu bằng 1,5 lần khoảng tứ phân vị, ngưỡng lý thuyết và điểm cuối râu là hai đại lượng khác nhau. Điểm cuối râu phải là một quan sát còn nằm trong ngưỡng, không phải chính ngưỡng.

::: exercise Tính hộp, ngưỡng và râu
Nhóm A có giá `[10, 12, 14, 16, 100]`, còn nhóm B có giá `[20, 22, 24, 26, 28]`. Hãy tính trung vị, tứ phân vị và ngưỡng dưới, trên của nhóm A bằng quy tắc nội suy mặc định của pandas. Râu trên của A dừng ở đâu? Có đủ căn cứ kết luận 100 là dữ liệu sai không?
:::

::: solution
Nhóm A có tứ phân vị thứ nhất bằng 12, trung vị bằng 14 và tứ phân vị thứ ba bằng 16. Khoảng tứ phân vị bằng 4, nên hai ngưỡng là 6 và 22. Các quan sát còn trong ngưỡng chạy từ 10 đến 16, vì vậy râu trên dừng ở 16. Giá 100 nằm ngoài râu, nhưng hình chưa cho biết đó là lỗi nhập liệu hay một trường hợp hợp lệ có giá cao.

```python
import pandas as pd
nhom_a = pd.Series([10, 12, 14, 16, 100])
q1, trung_vi, q3 = nhom_a.quantile([0.25, 0.5, 0.75])
iqr = q3 - q1
duoi, tren = q1 - 1.5 * iqr, q3 + 1.5 * iqr
trong_nguong = nhom_a[nhom_a.between(duoi, tren)]
assert (q1, trung_vi, q3, iqr, duoi, tren) == (12, 14, 16, 4, 6, 22)
assert (trong_nguong.min(), trong_nguong.max()) == (10, 16)
```
:::
