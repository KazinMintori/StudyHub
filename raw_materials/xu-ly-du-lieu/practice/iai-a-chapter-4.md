## Thực hành mảng và bộ nhớ

Tám bài dưới đây dùng cùng một mảng số nguyên. Giữ `A` nguyên vẹn, các phép gán thử nghiệm thực hiện trên bản sao.

```python
import numpy as np
A = np.array([[10, 12, 11], [20, 21, 24],
              [30, 33, 31], [40, 44, 42]], dtype=np.int64)
```

### Đọc cấu trúc mảng

::: exercise Thực hành NumPy 1
Ghi `shape`, `itemsize`, `nbytes`, `strides` của A. Tính độ lệch byte của `A[3, 1]`. Nếu chuyển sang `int32`, dung lượng dữ liệu và bước nhảy thay đổi thế nào?
:::

::: solution
```python
assert A.shape == (4, 3) and A.itemsize == 8
assert A.nbytes == 96 and A.strides == (24, 8)
offset_31 = 3 * A.strides[0] + A.strides[1]
B32 = A.astype(np.int32)
assert offset_31 == 80
assert B32.nbytes == 48 and B32.strides == (12, 4)
```

Mảng được tạo theo thứ tự C, nên mỗi hàng có ba phần tử, còn các cột liền nhau cách 8 byte. Chuyển dtype không đổi số hàng hay số cột, nhưng mỗi giá trị chỉ còn chiếm 4 byte. `nbytes` đếm byte của các phần tử nhìn thấy, không bao gồm siêu dữ liệu của đối tượng mảng.
:::

### Truy vết một lát cắt

::: exercise Thực hành NumPy 2
Tạo `V` từ hàng 1, 3 và cột 0, 2 bằng một lát cắt trên mỗi trục. Dự đoán giá trị, shape, strides và vị trí của `V[1, 1]` trong A. Kiểm tra bộ nhớ dùng chung.
:::

::: solution
```python
V = A[1::2, ::2]
np.testing.assert_array_equal(V, [[20, 24], [40, 42]])
assert V.shape == (2, 2) and V.strides == (48, 16)
assert np.shares_memory(A, V)
assert V[1, 1] == A[3, 2]
assert 3 * A.strides[0] + 2 * A.strides[1] == 88
```

Mỗi bước trên trục hàng bỏ qua một hàng, nên bước nhảy hàng tăng gấp đôi. Trục cột cũng nhảy qua từng hai phần tử. Phần tử cuối của V là `A[3, 2]`, cách đầu vùng dữ liệu A 88 byte.
:::

### So sánh lát cắt và mảng chỉ mục

::: exercise Thực hành NumPy 3
Đặt `B = A.copy()`, `V = B[:, 1:3]`, `C = B[:, [1, 2]]`. Dự đoán `B[0]` sau `C[0, 0] = -9`, rồi sau `V[0, 0] = -1`. Tạo D có hai cột đó nhưng sửa D không đổi B.
:::

::: solution
```python
B = A.copy()
V, C = B[:, 1:3], B[:, [1, 2]]
C[0, 0] = -9
np.testing.assert_array_equal(B[0], [10, 12, 11])
V[0, 0] = -1
np.testing.assert_array_equal(B[0], [10, -1, 11])
D = B[:, 1:3].copy()
assert not np.shares_memory(D, B)
truoc = B.copy()
D[0, 0] = 999
np.testing.assert_array_equal(B, truoc)
np.testing.assert_array_equal(A[0], [10, 12, 11])
```

Danh sách chỉ mục `[1, 2]` dùng advanced indexing và tạo bản sao dữ liệu. Lát cắt `1:3` dùng chung bộ nhớ, nên gán qua V tác động lên B. Hai biểu thức chọn cùng cột không nhất thiết có cùng quan hệ bộ nhớ.
:::

### Phân biệt chọn theo cặp và tích hàng–cột

::: exercise Thực hành NumPy 4
Không dùng vòng lặp, lấy số chẵn trong A theo thứ tự hàng, lấy hai ô `A[0, 1]`, `A[2, 2]`, rồi lấy các cột 1, 2 của cả hai hàng 0, 2 bằng `np.ix_`. Nêu shape từng kết quả.
:::

::: solution
```python
so_chan = A[A % 2 == 0]
hai_o = A[[0, 2], [1, 2]]
bon_o = A[np.ix_([0, 2], [1, 2])]
np.testing.assert_array_equal(so_chan, [10, 12, 20, 24, 30, 40, 44, 42])
np.testing.assert_array_equal(hai_o, [12, 31])
np.testing.assert_array_equal(bon_o, [[12, 11], [33, 31]])
assert (so_chan.shape, hai_o.shape, bon_o.shape) == ((8,), (2,), (2, 2))
assert all(not np.shares_memory(A, x) for x in [so_chan, hai_o, bon_o])
```

Hai mảng chỉ mục trực tiếp ghép từng vị trí với nhau, nên chỉ lấy hai ô. `np.ix_` mở hai dãy chỉ mục thành các trục để lấy mọi tổ hợp hàng và cột đã chọn.
:::

### Cộng theo cả hai trục

::: exercise Thực hành NumPy 5
Cộng 1, 2, 3 vào lần lượt ba cột của A, rồi cộng 10, 20, 30, 40 vào lần lượt bốn hàng. Tính K bằng phép toán mảng và giải thích vì sao `A + d` không thực hiện được yêu cầu theo hàng.
:::

::: solution
```python
b = np.array([1, 2, 3])
d = np.array([10, 20, 30, 40])
K = A + b + d[:, None]
np.testing.assert_array_equal(K, [[21, 24, 24], [41, 43, 47],
                                [61, 65, 64], [81, 86, 85]])
assert b.shape == (3,) and d[:, None].shape == (4, 1)
```

Trục cuối của A có độ dài 3. Dãy b dài 3 phù hợp với các cột, còn d dài 4 không khớp trục cuối. Thêm trục mới biến d thành bốn hàng, mỗi hàng một giá trị để dùng lại trên ba cột.
:::

### Sửa phép trừ chạy được nhưng sai trục

::: exercise Thực hành NumPy 6
Cho `gia = [[40, 50, 60], [60, 60, 60], [30, 60, 90]]`, kiểu `float64`. Đoạn `gia - gia.mean(axis=1)` chạy được nhưng chưa trừ trung bình của chính hàng chứa mỗi giá. Hãy sửa và kiểm tra trung bình các hàng sau khi trừ.
:::

::: solution
```python
gia = np.array([[40, 50, 60], [60, 60, 60], [30, 60, 90]], dtype=np.float64)
trung_binh_hang = gia.mean(axis=1, keepdims=True)
chenh_lech = gia - trung_binh_hang
assert trung_binh_hang.shape == (3, 1)
np.testing.assert_allclose(chenh_lech, [[-10, 0, 10], [0, 0, 0], [-30, 0, 30]])
np.testing.assert_allclose(chenh_lech.mean(axis=1), 0, atol=1e-12)
```

Kết quả giảm trục mà không giữ chiều có shape `(3,)`, nên được ghép với các cột của mảng vuông. `keepdims=True` giữ mỗi trung bình ở một hàng riêng với shape `(3, 1)`.
:::

### Đo thời gian trên cùng một nhiệm vụ

::: exercise Thực hành NumPy 7
So sánh nhân đôi bằng comprehension trên list, comprehension trên ndarray và phép `x * 2`, với 10 và 100.000 phần tử. Tạo dữ liệu trước khi đo, mỗi cách tạo đầu ra mới. Dùng thời gian nhỏ nhất trong ba lần lặp, giải thích kết quả quan sát được mà không ấn định tỷ lệ nhanh hơn.
:::

::: solution
```python
from timeit import repeat
def nhan_list(xs):
    return [v * 2 for v in xs]
def nhan_for_array(x):
    return [v * 2 for v in x]
def nhan_array(x):
    return x * 2

def do_thoi_gian(n):
    x = np.arange(n, dtype=np.int64)
    xs = x.tolist()
    np.testing.assert_array_equal(nhan_list(xs), nhan_array(x))
    np.testing.assert_array_equal(nhan_for_array(x), nhan_array(x))
    so_lan = 100 if n == 10 else 5
    return {ten: min(repeat(lambda: ham(du_lieu), number=so_lan, repeat=3)) / so_lan
            for ten, ham, du_lieu in [("list", nhan_list, xs),
                                     ("for_array", nhan_for_array, x),
                                     ("array", nhan_array, x)]}

for n in (10, 100_000):
    print(n, do_thoi_gian(n))
```

Hai comprehension vẫn lặp và xử lý từng giá trị ở tầng Python. Phép toán mảng chuyển vòng lặp số học sang mã thư viện đã biên dịch. Với mảng nhỏ, chi phí gọi hàm và tạo đầu ra có thể chiếm tỷ trọng lớn. Thời gian đo còn phụ thuộc máy và trạng thái hệ thống, nên cần báo chính kết quả đã đo.
:::

### Thống kê và lấy mẫu

::: exercise Thực hành NumPy 8
Với giá `[40, 50, 60, 70, 380]` USD/đêm, tính trung bình, trung vị, độ lệch chuẩn mặc định của NumPy và tỷ lệ giá không quá 70. Dùng seed 42 lấy ba chỉ mục không lặp rồi tính trung bình mẫu. Giá 380 có phải bị xóa không? Seed cố định có bảo đảm mẫu đại diện không?
:::

::: solution
```python
gia_dem = np.array([40, 50, 60, 70, 380], dtype=float)
rng = np.random.default_rng(42)
chi_muc = rng.choice(len(gia_dem), size=3, replace=False)
mau = gia_dem[chi_muc]
assert gia_dem.mean() == 120 and np.median(gia_dem) == 60
np.testing.assert_allclose(gia_dem.std(), np.sqrt(17000))
assert (gia_dem <= 70).mean() == 0.8
assert len(np.unique(chi_muc)) == 3
np.testing.assert_array_equal(mau, [380, 40, 70])
assert np.isclose(mau.mean(), 490 / 3)
```

Độ lệch chuẩn ở đây dùng mẫu số là số phần tử vì `ddof=0`. Trung vị 60 mô tả vị trí giữa của dãy và ít chịu ảnh hưởng của giá 380 hơn trung bình. Tuy vậy, một giá cao chưa chứng minh đó là lỗi. Seed giúp lặp lại phép lấy mẫu trong cùng môi trường, không bảo đảm tính đại diện. Khi đã có toàn bộ dữ liệu hợp lệ, không cần lấy mẫu để tính trung bình toàn bộ, nhưng đọc mẫu vẫn hữu ích khi kiểm tra nội dung từng dòng.
:::
