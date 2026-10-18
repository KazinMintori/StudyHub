## Quan sát cơ cấu nhóm trong một biểu đồ

![Hình 13.1: Giá trung bình của từng nhóm đều giảm, nhưng trung bình chung tăng khi tỷ trọng nhóm A tăng.](img/lec-14/co-cau-nhom.svg)

Giá trung bình của nhóm A giảm từ 8 xuống 7, còn nhóm B giảm từ 4 xuống 3 nghìn đồng. Tuy vậy, tỷ trọng quan sát thuộc nhóm A tăng từ 20% lên 80%. Vì nhóm A vẫn có giá cao hơn nhóm B ở cả hai kỳ, thay đổi cơ cấu có thể làm trung bình chung tăng.

::: exercise Giải thích hai chiều biến động
Mỗi kỳ có 100 quan sát. Ở kỳ trước, A có 20 quan sát và B có 80 quan sát. Ở kỳ sau, A có 80 quan sát và B có 20 quan sát. Dùng các trung bình nhóm trên hình để tính trung bình chung mỗi kỳ. Khẳng định “Giá tăng trong từng nhóm” có phù hợp với dữ liệu này không?
:::

::: solution
Tổng giá ở kỳ trước được tính từ số quan sát và trung bình của mỗi nhóm:

$$
T_0 = 20 \cdot 8 + 80 \cdot 4 = 480.
$$

Chia cho 100, ta được trung bình 4,8 nghìn đồng. Ở kỳ sau, tổng tương ứng là:

$$
T_1 = 80 \cdot 7 + 20 \cdot 3 = 620.
$$

Vì vậy trung bình chung kỳ sau bằng 6,2 nghìn đồng. Trung bình chung tăng, nhưng giá trung bình trong từng nhóm đều giảm. Hai kết quả trả lời những câu hỏi khác nhau vì dùng trọng số nhóm khác nhau.

```python
truoc = (20 * 8 + 80 * 4) / 100
sau = (80 * 7 + 20 * 3) / 100
assert (truoc, sau) == (4.8, 6.2)
assert 7 < 8 and 3 < 4 and sau > truoc
```

Để so sánh khi giữ cơ cấu cố định, có thể dùng tỷ trọng 20% và 80% ở cả hai kỳ. Khi đó trung bình kỳ sau là 3,8 nghìn đồng, giảm so với 4,8. Việc chọn cơ cấu tham chiếu cần được nêu rõ trong báo cáo.

```python
sau_cung_co_cau = 0.2 * 7 + 0.8 * 3
assert abs(sau_cung_co_cau - 3.8) < 1e-12
```
:::
