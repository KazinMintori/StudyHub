---
course: xu-ly-du-lieu
lecture: bai-03-numpy
section: lecture
title: "Mảng NumPy và tính toán trên mảng"
prerequisites: ["list", "ham-lap-trinh"]
lessonStatus: ready
hasChapterExercises: true
description: "Cấu trúc ndarray, cơ chế bộ nhớ strides, ufuncs, lập trình vector hóa, đại số tuyến tính, mô phỏng bước đi ngẫu nhiên và 6 bài tập IAI."
---


<div class="lecture-notes-content">

## 1. Cấu trúc mảng đa chiều ndarray trong NumPy

Bạn cần trừ cùng một giá trị hiệu chuẩn khỏi một dãy số đo nhiệt độ. Viết một vòng lặp Python là cách trực tiếp, nhưng khi dãy dài, việc xử lý từng đối tượng có thể tốn thêm thời gian. NumPy cung cấp `ndarray` để tổ chức mảng và gọi các phép toán số học trên cả mảng. Bài này giải thích cách lưu trữ, cách chọn phần tử và những điều kiện giúp phép toán đó giảm công việc ở tầng Python.

### 1.1. So sánh cơ chế bộ nhớ của Python list và ndarray
Trước hết cần phân biệt các giá trị được lưu trực tiếp với các tham chiếu tới đối tượng:

- **Danh sách Python (`list`)**: Trong CPython, list giữ một dãy tham chiếu tới các đối tượng. Nhiều vị trí có thể cùng trỏ tới một đối tượng. Khi duyệt, chương trình truy cập các đối tượng qua tham chiếu, nên kích thước và cách dùng chung đối tượng đều ảnh hưởng đến bộ nhớ thực tế.
- **Mảng NumPy (`ndarray`)**: Với dtype số thông thường, vùng dữ liệu lưu trực tiếp các giá trị theo cùng một dtype. Mảng `int64` liên tục theo thứ tự C đặt các số liền nhau, mỗi số chiếm 8 byte. Tuy nhiên, một view có thể truy cập vùng đệm bằng bước nhảy khác, và dtype `object` vẫn lưu tham chiếu tới đối tượng Python.

Số byte của các phần tử nhìn thấy trong một mảng được tính bằng:
$$
\text{nbytes} = \text{size} \times \text{itemsize}
$$

Một triệu phần tử `int64` có `nbytes` bằng 8.000.000 byte, tức 8 MB theo hệ thập phân, hoặc khoảng 7,63 MiB. Con số này chưa gồm siêu dữ liệu. Với view, `nbytes` cũng không cho biết lượng bộ nhớ mới được cấp phát. Muốn so với list phải đo trong cùng môi trường và tránh đếm lặp các đối tượng dùng chung.

### 1.2. Khởi tạo mảng ndarray
NumPy cung cấp nhiều phương thức khởi tạo mảng:
```python
import numpy as np

# Tạo mảng từ danh sách
arr1 = np.array([1, 2, 3, 4])

# Tạo mảng toàn số không hoặc số một
zeros_arr = np.zeros((3, 4), dtype=np.float64)  # 3 hàng, 4 cột
ones_arr = np.ones((2, 3), dtype=np.int32)

# Tạo mảng chưa khởi tạo giá trị (nhận giá trị rác trong RAM)
empty_arr = np.empty((2, 2))

# Tạo dãy số cách đều
range_arr = np.arange(10, 30, 5)  # array([10, 15, 20, 25])

# Tạo ma trận đơn vị
eye_arr = np.eye(3)
```

### 1.3. Kiểu dữ liệu (dtype) và giới hạn số nguyên {#_1-3-kieu-du-lieu-dtype-va-cam-bay-tran-so-nguyen}
Mỗi mảng `ndarray` có một thuộc tính `dtype` quy định kiểu dữ liệu đồng nhất của mọi phần tử trong mảng:
- Kiểu số nguyên có dấu: `int8` ($-128$ đến $127$), `int16`, `int32`, `int64`.
- Kiểu số nguyên không dấu: `uint8` ($0$ đến $255$), `uint16`, `uint32`, `uint64`.
- Kiểu số thực: `float16`, `float32`, `float64` (chuẩn IEEE 754).
- Kiểu logic: `bool` (`True` hoặc `False`, chiếm 1 byte mỗi phần tử).

Chuyển đổi kiểu dữ liệu được thực hiện qua phương thức `.astype()`. Theo mặc định, phương thức này tạo ra một bản sao mới trong bộ nhớ (`copy=True`). Nếu truyền `copy=False`, NumPy chỉ trả về chính mảng ban đầu khi kiểu dữ liệu và thứ tự sắp xếp bộ nhớ đã hoàn toàn trùng khớp, ngược lại phương thức vẫn tạo một bản sao mới:
```python
arr_float = np.array([1.2, 3.8, -2.5])
arr_int = arr_float.astype(np.int32)  # array([1, 3, -2]) - cắt bỏ phần thập phân
```

> [!WARNING] Ép kiểu trước khi tính toán
> Trong kiểu số nguyên cố định byte (như `int8`), nếu một phép toán vượt ra ngoài giới hạn cho phép, giá trị sẽ bị tràn nhị phân âm thầm mà không ném lỗi. Nếu ta thực hiện phép tính trước rồi mới ép kiểu, kết quả đã bị sai lệch từ trước:
> ```python
> x = np.array([50, 100, 120], dtype=np.int8)
> a = (x * 2).astype(np.int16)  # Sai: Tràn số trong int8 trước khi đổi kiểu!
> b = x.astype(np.int16) * 2     # Đúng: Đổi kiểu sang int16 rồi mới nhân đôi
> ```

<!-- worked-example bai-03-numpy-worked-1 -->

::: example Nhận diện hiện tượng tràn số nguyên và nâng kiểu dữ liệu với astype

Một phép đo được lưu bằng `int8`, chỉ biểu diễn số nguyên từ -128 đến 127. Ta cần nhân đôi các giá trị 60, 80 và 100. Ví dụ đối chiếu việc nhân ngay trong `int8` với chuyển sang `int32` trước khi nhân.

```python
import numpy as np

mang_int8 = np.array([60, 80, 100], dtype=np.int8)

tran_so = mang_int8 * np.int8(2)
an_toan = mang_int8.astype(np.int32) * 2

print(f"Mảng int8 gốc:               {mang_int8}")
print(f"Nhân 2 trên int8 (tràn số):  {tran_so}")
print(f"Nâng lên int32 rồi nhân 2:   {an_toan}")
print(f"Phần tử 80 biến thành số âm: {tran_so[1] < 0}")
```

Kết quả khi chạy đoạn mã trên:

```text
Mảng int8 gốc:               [ 60  80 100]
Nhân 2 trên int8 (tràn số):  [120 -96 -56]
Nâng lên int32 rồi nhân 2:   [120 160 200]
Phần tử 80 biến thành số âm: True
```

Kiểu dữ liệu `np.int8` chỉ sử dụng đúng 8 bit có dấu, do đó miền giá trị của nó bị giới hạn trong khoảng từ -128 đến 127. Khi ta nhân số 80 với 2, kết quả toán học là 160 vượt quá giới hạn trên 127.

NumPy giữ nguyên kích thước 8 bit của mảng kết quả, dẫn đến hiện tượng tràn bit nhị phân vòng ngược thành số âm -96. Hiện tượng này diễn ra âm thầm và không phát sinh ngoại lệ nào, khiến các phép tính tiếp theo nhận số liệu sai lệch.

Nếu nhân trước rồi gọi `astype(np.int32)`, giá trị -96 đã xuất hiện trong mảng trung gian. Ép kiểu sau đó giữ lại giá trị -96 dưới dạng `int32`, không khôi phục được 160. Vì vậy, thời điểm đổi kiểu là một phần của phép tính.

Cách làm đúng là gọi phương thức `astype(np.int32)` ngay từ mảng ban đầu để mở rộng kích thước ô nhớ lên 4 byte trước khi nhân 2. Kết quả `an_toan` giữ trọn vẹn giá trị 160 và 200, bảo đảm tính toàn vẹn của dữ liệu số học.

:::

<!-- /worked-example -->

### 1.4. Phép toán số học vector hóa trên mảng
Khi áp dụng các phép toán số học (`+`, `-`, `*`, `/`, `**`) giữa các mảng cùng kích thước hoặc giữa mảng với một số vô hướng, NumPy thực thi phép tính **theo từng phần tử** (*element-wise*):
```python
arr = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]])
print(arr * arr)
# [[ 1.  4.  9.]
#  [16. 25. 36.]]

print(1 / arr)
print(arr ** 0.5)
```
Vòng lặp số học được thực hiện trong mã thư viện đã biên dịch thay vì lặp từng bước ở tầng Python. Một số phép toán trên phần cứng phù hợp còn có thể dùng SIMD để xử lý nhiều phần tử trong một lệnh máy. Điều này không bảo đảm mọi phép toán dùng SIMD hoặc nhiều luồng.

### 1.5. Chỉ mục cơ bản, cắt lát và bản chất của View
Truy xuất mảng 2 chiều trong NumPy sử dụng cặp chỉ số ngăn cách bởi dấu phẩy `arr[hang, cot]`, thay vì hai lần ngoặc vuông `arr[hang][cot]` như danh sách lồng nhau của Python.

Điểm khác biệt căn bản giữa Python `list` và NumPy `ndarray`:
- Cắt lát trên danh sách Python luôn tạo ra một **bản sao mới** (*copy*).
- Cắt lát trên mảng NumPy tạo ra một **khung nhìn** (*View*). View không cấp phát vùng đệm dữ liệu mới mà dùng chung vùng nhớ với mảng gốc.

```python
A = np.array([10, 20, 30, 40, 50])
v = A[1:4]   # v là một View trỏ vào các phần tử 20, 30, 40
v[0] = 999   # Sửa phần tử đầu tiên của v
print(A)     # [ 10, 999,  30,  40,  50] -> Mảng gốc A bị thay đổi!
```
Nếu bạn muốn chỉnh sửa trên lát cắt mà không ảnh hưởng tới mảng ban đầu, bắt buộc phải sao chép dữ liệu tường minh bằng phương thức `.copy()`:
```python
v_doc_lap = A[1:4].copy()
```

### 1.6. Cơ chế bộ nhớ của reshape: Phân biệt View và Copy
Một câu hỏi cốt lõi trong kỹ thuật dữ liệu: Khi gọi phương thức `.reshape()`, kết quả thu được là một View dùng chung bộ nhớ hay là một bản sao Copy mới?

NumPy quản lý cấu trúc mảng thông qua hai thuộc tính:
- `shape`: Tuple chứa kích thước của từng chiều.
- `strides`: Tuple chứa số byte cần dịch chuyển trong bộ nhớ để bước sang phần tử kế tiếp của từng chiều.

#### Ví dụ dùng chung bộ nhớ (Sharing Memory - View)
Xét mảng hai chiều $A$ gồm 12 số nguyên 64-bit ($3 \times 4$), được lưu trữ liên tục theo hàng (*C-contiguous*):
```python
A = np.arange(12).reshape(3, 4)
# A có shape=(3, 4) và strides=(32, 8) (bước hàng là 4*8=32 byte, bước cột là 8 byte)

B = A.reshape(4, 3)
```
Vì dữ liệu gốc vốn đã nằm liên tiếp trong bộ nhớ theo thứ tự $0, 1, \dots, 11$, NumPy có thể thỏa mãn hình dạng mới $(4, 3)$ chỉ bằng cách tạo một đối tượng metadata mới với `shape=(4, 3)` và `strides=(24, 8)`. Không có byte dữ liệu nào bị sao chép. Ta kiểm chứng việc dùng chung vùng đệm bộ nhớ bằng hàm:
```python
np.shares_memory(A, B)  # Trả về True
```

#### Ví dụ không dùng chung bộ nhớ (Non-Sharing Memory - Copy)
Xét mảng chuyển vị của $A$:
```python
T = A.T  # T có shape=(4, 3) nhưng strides=(8, 32)
```
Mảng $T$ là một View của $A$, nhưng các phần tử theo thứ tự đọc hàng của nó không còn nằm liên tiếp trong bộ nhớ vật lý. Thuộc tính `T.flags['C_CONTIGUOUS']` trả về `False`.

Nếu bây giờ ta yêu cầu làm phẳng mảng $T$ thành một mảng một chiều:
```python
C = T.reshape(-1)
```
NumPy không thể biểu diễn một mảng một chiều đọc theo hàng từ $T$ chỉ bằng một bước nhảy `stride` cố định trên vùng nhớ phân tán đó. Do đó, NumPy **bắt buộc phải cấp phát một vùng nhớ mới trong RAM** và sao chép toàn bộ các giá trị vào đó theo thứ tự mới:
```python
np.shares_memory(T, C)  # Trả về False
```

> [!IMPORTANT] Quy tắc kiểm chứng vùng nhớ chuẩn mực
> Để kiểm tra hai mảng có dùng chung bộ nhớ hay không, luôn sử dụng hàm `np.shares_memory(arr1, arr2)`. Tuyệt đối không dùng phép so sánh `C.base is A`. Thuộc tính `.base` có thể trỏ tới một đối tượng trung gian hoặc trả về `None`, không phản ánh chính xác trạng thái đệm dữ liệu.
> Đồng thời, **không khẳng định mọi mảng ndarray đều liên tục trong bộ nhớ**. Các lát cắt có bước nhảy khác một (`A[::2]`) hoặc mảng chuyển vị (`A.T`) là các mảng không liên tục (*non-contiguous*).

<!-- worked-example bai-03-numpy-worked-2 -->

::: example Kiểm tra tính liên tục bộ nhớ và quan hệ dùng chung vùng đệm

Chuyển vị đổi cách các hàng và cột tham chiếu vào vùng dữ liệu. Vùng đệm gốc vẫn có thể được dùng chung, nhưng thứ tự duyệt theo hàng đã khác. Ta dùng `np.shares_memory` để kiểm tra việc chuyển vị và làm phẳng trong một trường hợp cụ thể.

```python
import numpy as np

A = np.arange(6, dtype=np.int32).reshape(2, 3)
T = A.T
C = T.reshape(-1)

print(f"A liên tục theo hàng (C-contiguous): {A.flags['C_CONTIGUOUS']}")
print(f"T chuyển vị liên tục theo hàng:     {T.flags['C_CONTIGUOUS']}")
print(f"A và T dùng chung bộ nhớ (View):     {np.shares_memory(A, T)}")
print(f"T và C dùng chung bộ nhớ:            {np.shares_memory(T, C)}")
```

Kết quả khi chạy đoạn mã trên:

```text
A liên tục theo hàng (C-contiguous): True
T chuyển vị liên tục theo hàng:     False
A và T dùng chung bộ nhớ (View):     True
T và C dùng chung bộ nhớ:            False
```

Mảng ban đầu `A` có kích thước 2 hàng 3 cột với cờ `C_CONTIGUOUS` mang giá trị `True`, chứng tỏ 6 số nguyên từ 0 đến 5 được đặt nối tiếp nhau trong RAM. Mảng chuyển vị `T = A.T` hoán đổi các trục nhưng vẫn dùng chung vùng đệm gốc với bước nhảy `strides` đã biến đổi.

Hàm `np.shares_memory(A, T)` trả về `True`, xác nhận thao tác chuyển vị chỉ thay đổi siêu dữ liệu mà không tốn chi phí sao chép mảng. Tuy nhiên, thuộc tính `C_CONTIGUOUS` của `T` lúc này đã chuyển thành `False` vì các phần tử theo chiều đọc hàng không còn nằm liền kề trong bộ nhớ.

Khi yêu cầu làm phẳng `T` thành mảng một chiều bằng lệnh `T.reshape(-1)`, NumPy nhận thấy bước nhảy chuyển vị không thể biểu diễn trực tiếp thành một mảng một chiều liên tục trên cùng vùng đệm đó. Trình thông dịch buộc phải cấp phát một mảng mới `C` và sao chép dữ liệu sang.

Kết quả kiểm tra `np.shares_memory(T, C)` trả về `False`, chứng minh `C` là một bản sao độc lập. Tuy nhiên, việc `reshape` cấp phát bộ nhớ mới trong ví dụ này không đồng nghĩa mọi phép chuyển vị hoặc thay đổi hình dạng đều tạo bản sao, bởi cơ chế View hay Copy phụ thuộc hoàn toàn vào cấu trúc bước nhảy `strides` của mảng cụ thể.

:::

<!-- /worked-example -->

### 1.7. Chỉ mục boolean
Chỉ mục boolean cho phép trích xuất các phần tử thỏa mãn một biểu thức điều kiện vị từ:
```python
ten = np.array(["An", "Bình", "An", "Cường"])
diem = np.array([[8, 9], [5, 6], [7, 10], [4, 5]])

# Tạo mặt nạ boolean
mask = ten == "An"  # array([True, False, True, False])

# Lọc các hàng tương ứng với mặt nạ
print(diem[mask])
# [[ 8  9]
#  [ 7 10]]
```

Khi kết hợp nhiều điều kiện logic, bắt buộc phải dùng các toán tử bit:
- Toán tử VÀ: `&`
- Toán tử HOẶC: `|`
- Toán tử PHỦ ĐỊNH: `~`
Mỗi điều kiện con phải được bọc trong cặp ngoặc đơn `()` để tránh lỗi ưu tiên toán tử:
```python
mask_hop = (ten == "An") | (ten == "Cường")
```

Gán giá trị qua mặt nạ boolean giúp biến đổi trực tiếp các phần tử thỏa mãn điều kiện:
```python
diem[diem < 5] = 5  # Mọi điểm dưới 5 được nâng lên 5
```

### 1.8. Chỉ mục mảng số nguyên (Fancy Indexing)
Fancy Indexing là thuật ngữ chỉ việc sử dụng một mảng hoặc danh sách các số nguyên để chọn các phần tử theo thứ tự bất kỳ:
```python
arr = np.zeros((8, 4))
for i in range(8):
    arr[i] = i

# Chọn các hàng 4, 3, 0 theo đúng thứ tự chỉ định
chon = arr[[4, 3, 0]]
```

> [!CAUTION] Fancy Indexing luôn tạo bản sao
> Khác với cắt lát thông thường, **Fancy Indexing luôn luôn sao chép dữ liệu sang một vùng nhớ mới**, hoàn toàn không bao giờ tạo ra View. Mọi thao tác gán lên mảng kết quả của Fancy Indexing sẽ không làm ảnh hưởng tới mảng gốc trừ khi thực hiện phép gán trực tiếp: `arr[[4, 3]] = 999`.

Để chọn một vùng chữ nhật gồm các hàng và cột giao nhau, ta sử dụng hàm hỗ trợ `np.ix_`:
```python
arr = np.arange(16).reshape((4, 4))
# Chọn hàng 1, 3 và cột 0, 2
vung_chon = arr[np.ix_([1, 3], [0, 2])]
# [[ 4  6]
#  [12 14]]
```

<!-- worked-example bai-03-numpy-worked-3 -->

::: example Trích xuất phần tử phân tán bằng chỉ mục mảng số nguyên

Khác với cắt lát cơ bản chỉ trích xuất các đoạn phần tử cách đều, chỉ mục mảng số nguyên (fancy indexing) cho phép chọn các hàng hoặc phần tử theo một thứ tự tùy ý bất kỳ. Tuy nhiên, fancy indexing luôn tạo ra một bản sao mới thay vì một khung nhìn, nên các thay đổi trên mảng trích xuất sẽ không phản chiếu vào mảng ban đầu. Ta đối chiếu hành vi này để tránh nhầm lẫn trong quá trình gán giá trị.

```python
import numpy as np

bang_diem = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
    [15, 25, 35],
])

chi_so_hang = np.array([3, 0, 2])
trich_xuat = bang_diem[chi_so_hang]

trich_xuat[0, 0] = 999

print("Mảng trích xuất sau khi sửa phần tử [0, 0]:")
print(trich_xuat)
print(f"Phần tử gốc tại hàng 3, cột 0:   {bang_diem[3, 0]}")
print(f"Dùng chung vùng nhớ với bảng gốc: {np.shares_memory(bang_diem, trich_xuat)}")
```

Kết quả khi chạy đoạn mã trên:

```text
Mảng trích xuất sau khi sửa phần tử [0, 0]:
[[999  25  35]
 [ 10  20  30]
 [ 70  80  90]]
Phần tử gốc tại hàng 3, cột 0:   15
Dùng chung vùng nhớ với bảng gốc: False
```

Mảng `bang_diem` đại diện cho ma trận gồm 4 hàng và 3 cột. Biến `chi_so_hang` chứa mảng số nguyên `[3, 0, 2]` chỉ định thứ tự các hàng cần rút trích.

Cú pháp `bang_diem[chi_so_hang]` trích xuất đồng thời hàng 3, hàng 0 và hàng 2 thành một mảng mới có kích thước 3 hàng 3 cột. Thứ tự các hàng trong mảng kết quả hoàn toàn trùng khớp với thứ tự các chỉ số được truyền vào.

Sau khi trích xuất, ta thử gán giá trị 999 vào phần tử đầu tiên của `trich_xuat`. Khi kiểm tra lại mảng gốc `bang_diem[3, 0]`, giá trị vẫn giữ nguyên là 15 ban đầu chứ không bị biến đổi thành 999.

Hàm `np.shares_memory` trả về `False`, khẳng định fancy indexing luôn sao chép dữ liệu sang vùng nhớ độc lập. Nếu muốn chỉnh sửa trực tiếp trên mảng gốc bằng fancy indexing, ta phải gán trực tiếp vào mảng gốc với cú pháp `bang_diem[chi_so_hang] = gia_tri_moi`.

:::

<!-- /worked-example -->

### 1.9. Chuyển vị mảng và hoán đổi trục
Chuyển vị là một trường hợp đặc biệt của việc tạo View:
- Thuộc tính `.T`: Hoán đổi hai trục của mảng 2 chiều.
- Phương thức `arr.swapaxes(truc1, truc2)`: Hoán đổi hai trục chỉ định trên mảng nhiều chiều.

Chuyển vị chỉ thay đổi thuộc tính `shape` và đảo thứ tự của `strides`, hoàn toàn không tốn thời gian di chuyển dữ liệu trong RAM.

---

## 2. Sinh số ngẫu nhiên giả

Mô-đun `numpy.random` cung cấp các thuật toán sinh số ngẫu nhiên tối ưu hóa cho mảng nhiều chiều. Từ phiên bản NumPy hiện đại, giao diện bộ sinh ngẫu nhiên `default_rng` được khuyến nghị sử dụng:

```python
# Khởi tạo bộ sinh số ngẫu nhiên với hạt giống cố định
rng = np.random.default_rng(seed=42)

# Sinh mảng phân phối chuẩn tắc (trung bình 0, độ lệch chuẩn 1)
chuan = rng.standard_normal(size=(3, 3))

# Sinh số thực phân phối đều trong đoạn [0, 1)
deu = rng.uniform(low=0.0, high=10.0, size=5)

# Sinh số nguyên ngẫu nhiên trong khoảng [a, b)
nguyen = rng.integers(low=1, high=100, size=(2, 4))

# Lấy mẫu ngẫu nhiên không lặp lại từ một mảng có sẵn
tap_goc = np.array([10, 20, 30, 40, 50, 60])
mau = rng.choice(tap_goc, size=3, replace=False)
```

Tham số `replace=False` bảo đảm mỗi phần tử chỉ được chọn tối đa một lần. Việc cố định hạt giống ngẫu nhiên `seed` giúp kết quả tính toán có tính tái lập (*reproducibility*), hỗ trợ kiểm thử và chia sẻ mã nguồn.

---

<!-- worked-example bai-03-numpy-worked-4 -->

::: example Sinh dữ liệu phân phối ngẫu nhiên với np.random.default_rng

Trong mô phỏng thống kê và kiểm thử mô hình học máy, các tập dữ liệu ngẫu nhiên cần phải tái lập được để kiểm tra thuật toán. Khung làm việc hiện đại của NumPy khuyến khích sử dụng bộ sinh số default_rng với hạt giống cố định thay vì các hàm toàn cục cũ. Ta sinh mẫu số nguyên và mẫu phân phối chuẩn để theo dõi các đặc trưng thống kê.

```python
import numpy as np

rng = np.random.default_rng(seed=42)

so_nguyen = rng.integers(low=10, high=50, size=5)
phan_phoi_chuan = rng.normal(loc=0.0, scale=1.0, size=5)

print(f"Mẫu số nguyên ngẫu nhiên: {so_nguyen}")
print(f"Mẫu phân phối chuẩn:     {np.round(phan_phoi_chuan, 3)}")
print(f"Trung bình mẫu:          {np.mean(phan_phoi_chuan):.3f}")
```

Kết quả khi chạy đoạn mã trên:

```text
Mẫu số nguyên ngẫu nhiên: [13 40 36 27 27]
Mẫu phân phối chuẩn:     [ 0.941 -1.951 -1.302  0.128 -0.316]
Trung bình mẫu:          -0.500
```

Hàm `np.random.default_rng` khởi tạo một đối tượng Generator độc lập sử dụng thuật toán PCG64. Việc cố định tham số `seed=42` bảo đảm chuỗi số ngẫu nhiên sinh ra có thể tái lập được khi chạy lại mã nguồn.

Phương thức `rng.integers(low=10, high=50, size=5)` sinh ra 5 số nguyên ngẫu nhiên trong khoảng nửa mở `[10, 50)`. Điểm chặn trên 50 không bao giờ xuất hiện trong kết quả.

Phương thức `rng.normal(loc=0.0, scale=1.0, size=5)` sinh mẫu gồm 5 số thực tuân theo phân phối chuẩn Gauss với kỳ vọng `loc` bằng không và độ lệch chuẩn `scale` bằng một.

Để chạy lại đúng chuỗi số, cần giữ cùng bộ sinh, trạng thái khởi tạo, thứ tự lời gọi và môi trường tương thích. Chỉ thêm một lệnh lấy số từ `rng` trước `normal` cũng làm kết quả phía sau đổi đi. Seed không phải cam kết rằng mọi phiên bản thư viện tương lai sẽ cho cùng từng bit.

:::

<!-- /worked-example -->

## 3. Các hàm phổ quát ufunc

Hàm phổ quát (*Universal Function* hay `ufunc`) là một hàm thực thi các phép toán trên từng phần tử của mảng `ndarray`. ufunc được biên dịch trực tiếp bằng C, có khả năng ép kiểu tự động và hỗ trợ phát sóng (*broadcasting*).

### 3.1. Các hàm ufunc một ngôi
Tiếp nhận một mảng đầu vào và trả về một mảng kết quả cùng kích thước:
- `np.abs()`, `np.fabs()`: Giá trị tuyệt đối của từng phần tử.
- `np.sqrt()`: Căn bậc hai (tương đương `arr ** 0.5`).
- `np.square()`: Bình phương từng phần tử.
- `np.exp()`: Hàm mũ $e^x$.
- `np.log()`, `np.log10()`, `np.log2()`: Logarit tự nhiên, cơ số 10 và cơ số 2.
- `np.sign()`: Trả về dấu của số: $1$ (dương), $0$ (bằng không), và $-1$ (âm).
- `np.ceil()`, `np.floor()`: Làm tròn lên và làm tròn xuống số nguyên gần nhất.
- `np.isnan()`: Trả về mảng boolean đánh dấu các giá trị không xác định `NaN` (*Not a Number*).
- `np.isfinite()`: Kiểm tra các giá trị hữu hạn (không phải `NaN` và không phải dương hoặc âm vô cực).

<!-- worked-example bai-03-numpy-worked-5 -->

::: example Phân tách phần nguyên và phần thập phân của mảng với np.modf

Một tọa độ được ghi bằng độ thập phân. Ta cần tách phần nguyên và phần lẻ để tiếp tục đổi đơn vị. `np.modf` trả cả hai mảng, đồng thời cho thấy cách hàm xử lý tọa độ âm.

```python
import numpy as np

toa_do = np.array([105.8542, 21.0285, -10.5500], dtype=np.float64)
phan_thap_phan, phan_nguyen = np.modf(toa_do)

for i in range(len(toa_do)):
    print(f"Gốc: {toa_do[i]:>9.4f} -> Nguyên: {phan_nguyen[i]:>6.1f}, "
          f"Thập phân: {phan_thap_phan[i]:>7.4f}")
```

Kết quả khi chạy đoạn mã trên:

```text
Gốc:  105.8542 -> Nguyên:  105.0, Thập phân:  0.8542
Gốc:   21.0285 -> Nguyên:   21.0, Thập phân:  0.0285
Gốc:  -10.5500 -> Nguyên:  -10.0, Thập phân: -0.5500
```

Hàm ufunc một ngôi `np.modf` nhận vào một mảng số thực và trả về một cặp gồm hai mảng riêng biệt: Mảng thứ nhất chứa phần thập phân và mảng thứ hai chứa phần nguyên.

Cần lưu ý thứ tự trả về của `np.modf`: Mảng phần thập phân được đặt ở vị trí đầu tiên, còn mảng phần nguyên được đặt ở vị trí thứ hai. Dấu của hai thành phần này luôn được bảo lưu đồng nhất với dấu của số gốc ban đầu.

Đối với số âm `-10.55`, hàm bóc tách thành phần nguyên `-10.0` và thành phần thập phân `-0.55`. Đây là điểm khác biệt so với hàm lấy sàn `np.floor` vốn làm tròn về phía âm vô cùng thành `-11.0`.

`np.modf` trả hai kết quả cùng lúc theo thứ tự phần lẻ rồi phần nguyên. Cần giữ đúng thứ tự khi giải nén. Trong ví dụ, cộng lại hai phần của mỗi giá trị sẽ khôi phục tọa độ ban đầu trong giới hạn làm tròn số thực.

:::

<!-- /worked-example -->

### 3.2. Các hàm ufunc hai ngôi
Tiếp nhận hai mảng đầu vào và thực hiện phép toán theo từng cặp phần tử:
- `np.add()`, `np.subtract()`, `np.multiply()`, `np.divide()`: Cộng, trừ, nhân, chia mảng.
- `np.maximum()`, `np.minimum()`: Tìm giá trị lớn nhất và nhỏ nhất giữa từng cặp phần tử tương ứng của hai mảng.
- `np.copysign()`: Sao chép dấu của mảng thứ hai sang các giá trị của mảng thứ nhất.
- `np.mod()`: Phép chia lấy phần dư theo từng phần tử.

---

## 4. Lập trình hướng mảng

Lập trình hướng mảng là phong cách thay thế các vòng lặp duyệt phần tử bằng các biểu thức mảng ngắn gọn.

### 4.1. Biểu diễn logic điều kiện với `np.where`
Hàm `np.where(dieu_kien, neu_dung, neu_sai)` là phiên bản vector hóa của biểu thức ba ngôi `x if dieu_kien else y`:
```python
diem = np.array([4.5, 7.0, 8.5, 3.0, 9.0])
ket_qua = np.where(diem >= 5.0, "Đạt", "Trượt")
# array(['Trượt', 'Đạt', 'Đạt', 'Trượt', 'Đạt'], dtype='<U5')
```
Ta cũng có thể truyền mảng số học vào các nhánh để tính toán giá trị tương ứng:
```python
# Nếu điểm dưới 5 thì cộng 1 điểm khuyến khích, ngược lại giữ nguyên
diem_moi = np.where(diem < 5.0, diem + 1.0, diem)
```

<!-- worked-example bai-03-numpy-worked-6 -->

::: example Phân loại dữ liệu theo nhiều điều kiện với np.select

Trong nghiệp vụ định giá hoặc phân loại khách hàng, ta thường phải gán nhãn dựa trên nhiều khoảng giá trị khác nhau. Việc sử dụng hàm np.where lồng nhau qua ba hoặc bốn cấp sẽ khiến biểu thức trở nên rối rắm và khó bảo trì. Hàm np.select cho phép khai báo danh sách các điều kiện logic song song với danh sách kết quả tương ứng một cách mạch lạc.

```python
import numpy as np

diem_so = np.array([4.5, 6.8, 8.2, 9.5, 7.0])

dieu_kien = [
    diem_so >= 9.0,
    diem_so >= 8.0,
    diem_so >= 6.5,
    diem_so >= 5.0,
]
nhan = ["Xuất sắc", "Giỏi", "Khá", "Trung bình"]
mac_dinh = "Yếu"

xep_loai = np.select(dieu_kien, nhan, default=mac_dinh)

for d, xl in zip(diem_so, xep_loai):
    print(f"Điểm {d:>4.1f}: xếp loại {xl}")
```

Kết quả khi chạy đoạn mã trên:

```text
Điểm  4.5: xếp loại Yếu
Điểm  6.8: xếp loại Khá
Điểm  8.2: xếp loại Giỏi
Điểm  9.5: xếp loại Xuất sắc
Điểm  7.0: xếp loại Khá
```

Hàm `np.select` tiếp nhận ba tham số: Danh sách các mảng điều kiện boolean `dieu_kien`, danh sách các nhãn kết quả tương ứng `nhan`, và giá trị mặc định `default` khi không có điều kiện nào thỏa mãn.

Khi thực thi, `np.select` duyệt qua các điều kiện theo thứ tự danh sách và chọn giá trị tương ứng với điều kiện đầu tiên có chân trị `True` cho từng phần tử. Chẳng hạn điểm 9.5 thỏa mãn ngay điều kiện đầu tiên nên nhận nhãn Xuất sắc.

Các mảng điều kiện đã được tính trước khi truyền vào `np.select`. Hàm chọn kết quả theo điều kiện khớp đầu tiên, nhưng không ngăn việc tính các điều kiện phía sau. Nếu một biểu thức chứa phép chia cho không, phép chia vẫn xảy ra và có thể phát sinh cảnh báo hoặc ngoại lệ tùy kiểu dữ liệu.

Kết quả in ra thể hiện sự phân cấp rõ ràng cho từng mức điểm. So với cú pháp `np.where` lồng nhau, `np.select` giúp cấu trúc mã nguồn trong sáng và thuận tiện khi cần bổ sung thêm các bậc phân loại mới.

:::

<!-- /worked-example -->

### 4.2. Các phương thức toán học và thống kê
NumPy hỗ trợ các hàm thống kê tổng hợp trên toàn bộ mảng hoặc dọc theo một trục xác định:

| Phương thức | Ý nghĩa toán học |
| :--- | :--- |
| `sum()` | Tổng toàn bộ các phần tử |
| `mean()` | Trung bình cộng số học |
| `std()`, `var()` | Độ lệch chuẩn và phương sai |
| `min()`, `max()` | Giá trị nhỏ nhất và lớn nhất |
| `argmin()`, `argmax()` | Vị trí chỉ số của phần tử nhỏ nhất và lớn nhất |
| `cumsum()` | Tổng tích lũy từ phần tử đầu tiên |
| `cumprod()` | Tích tích lũy từ phần tử đầu tiên |

#### Tham số `axis` và `keepdims`
Khi tính toán trên mảng 2 chiều:
- `axis=0`: Tổng hợp dọc theo các hàng (tính kết quả cho từng cột).
- `axis=1`: Tổng hợp ngang qua các cột (tính kết quả cho từng hàng).

```python
M = np.array([[10, 12, 11],
              [20, 21, 24],
              [30, 33, 31]])

# Tính trung bình từng hàng
tb_hang = M.mean(axis=1, keepdims=True)
# shape của tb_hang là (3, 1), cho phép trừ trực tiếp M - tb_hang bằng broadcasting
```

<!-- worked-example bai-03-numpy-worked-7 -->

::: example Định tâm mảng dọc theo trục và bảo toàn bậc chiều với keepdims

Ta muốn trừ trung bình từng cột khỏi một bảng số đo. `keepdims=True` giữ lại trục đã tổng hợp với kích thước 1, giúp nhìn rõ chiều mà kết quả sẽ được broadcast. Ví dụ cũng đối chiếu cách giữ chiều khi tính trung bình từng hàng.

```python
import numpy as np

du_lieu = np.array([
    [10.0, 20.0, 30.0],
    [40.0, 50.0, 60.0],
])

tb_giam = np.mean(du_lieu, axis=0)
tb_giu = np.mean(du_lieu, axis=0, keepdims=True)
dinh_tam = du_lieu - tb_giu

print(f"Kích thước mảng gốc:            {du_lieu.shape}")
print(f"Kích thước trung bình giảm bậc: {tb_giam.shape}")
print(f"Kích thước trung bình giữ bậc:  {tb_giu.shape}")
print("Mảng sau khi trừ trung bình (định tâm):")
print(dinh_tam)
tb_hang = du_lieu.mean(axis=1, keepdims=True)
print("Trung bình từng hàng, shape:", tb_hang.shape)
print("Định tâm theo hàng:")
print(du_lieu - tb_hang)
```

Kết quả khi chạy đoạn mã trên:

```text
Kích thước mảng gốc:            (2, 3)
Kích thước trung bình giảm bậc: (3,)
Kích thước trung bình giữ bậc:  (1, 3)
Mảng sau khi trừ trung bình (định tâm):
[[-15. -15. -15.]
 [ 15.  15.  15.]]
Trung bình từng hàng, shape: (2, 1)
Định tâm theo hàng:
[[-10.   0.  10.]
 [-10.   0.  10.]]
```

Ma trận `du_lieu` có kích thước 2 hàng 3 cột. Khi tính trung bình theo trục `axis=0`, NumPy thực hiện cộng dồn dọc theo các hàng để thu được giá trị trung bình cho từng cột.

Theo mặc định, mảng `tb_giam` bị giảm bậc thành mảng một chiều có kích thước `(3,)`. Ngược lại, khi truyền thêm tham số `keepdims=True`, mảng `tb_giu` vẫn duy trì đủ 2 chiều với kích thước `(1, 3)`.

Trong phép trừ theo cột này, cả `(3,)` và `(1, 3)` đều broadcast được với `(2, 3)`. Lợi ích của `keepdims` rõ hơn khi tính theo hàng. `axis=1` với `keepdims=True` cho `(2, 1)`, còn nếu bỏ tham số thì chỉ còn `(2,)`, không khớp với chiều cuối bằng 3 của bảng.

Thao tác trừ trung bình này là bước định tâm dữ liệu (centering) quanh mốc không, chứ chưa phải một phép chuẩn hóa Z-score hoàn chỉnh vốn đòi hỏi phải chia tiếp cho độ lệch chuẩn. Kết quả in ra xác nhận mỗi cột đều có giá trị đối xứng [-15.0, 15.0] quanh điểm cân bằng.

:::

<!-- /worked-example -->

### 4.3. Các phương thức cho mảng boolean
Trên mảng boolean, các giá trị `True` được coi là $1$ và `False` được coi là $0$:
- Đếm số lượng phần tử thỏa mãn điều kiện:
```python
so_luong_lon = (M > 20).sum()  # Đếm có bao nhiêu ô lớn hơn 20
```
- `arr.any()`: Kiểm tra xem có **ít nhất một** giá trị `True` hay không.
- `arr.all()`: Kiểm tra xem **toàn bộ** các giá trị có phải là `True` hay không.

### 4.4. Sắp xếp mảng
- Sắp xếp tại chỗ: Phương thức `arr.sort(axis=...)` làm thay đổi trực tiếp mảng gốc.
- Sắp xếp trả về bản sao: Hàm `np.sort(arr)` giữ nguyên mảng gốc và trả về mảng mới.
- Tìm chỉ số sắp xếp: Hàm `np.argsort(arr)` trả về mảng các chỉ số nguyên quy định thứ tự sắp xếp tăng dần, thuận tiện khi cần sắp xếp đồng thời nhiều mảng dữ liệu liên quan.

### 4.5. Đại số tập hợp trên mảng
NumPy cung cấp các hàm tập hợp 1 chiều xử lý mảng với tốc độ vượt trội:
- `np.unique(arr)`: Trả về các giá trị phân biệt trong mảng và đã được sắp xếp tăng dần.
- `np.isin(arr, tap_hop)`: Kiểm tra từng phần tử của mảng có thuộc một tập hợp giá trị cho trước hay không, trả về mảng boolean.
- `np.intersect1d(x, y)`: Tìm phần giao của hai mảng.
- `np.union1d(x, y)`: Tìm phần hợp của hai mảng.
- `np.setdiff1d(x, y)`: Tìm phần hiệu (các phần tử có trong `x` nhưng không có trong `y`).

---

<!-- worked-example bai-03-numpy-worked-8 -->

::: example Tìm giá trị duy nhất và kiểm tra thành viên với np.unique và np.isin

Một nhật ký ghi lặp lại các mã HTTP. Ta cần đếm mỗi mã và lấy vị trí của các mã thuộc danh sách cảnh báo. `unique`, `isin` và `where` lần lượt giải quyết ba bước đó trên cùng một mảng.

```python
import numpy as np

ma_loi = np.array([404, 200, 500, 404, 200, 404, 503])
canh_bao = np.array([500, 502, 503])

cac_loai, so_lan = np.unique(ma_loi, return_counts=True)
la_nguy_hiem = np.isin(ma_loi, canh_bao)
vi_tri_su_co = np.where(la_nguy_hiem)[0]

print("Tần suất xuất hiện của từng mã lỗi:")
for loai, dem in zip(cac_loai, so_lan):
    print(f"  Mã {loai}: {dem} lần")
print(f"Số lượng sự cố thuộc diện cảnh báo: {np.sum(la_nguy_hiem)}")
print(f"Vị trí chỉ số của các sự cố cảnh báo: {vi_tri_su_co}")
```

Kết quả khi chạy đoạn mã trên:

```text
Tần suất xuất hiện của từng mã lỗi:
  Mã 200: 2 lần
  Mã 404: 3 lần
  Mã 500: 1 lần
  Mã 503: 1 lần
Số lượng sự cố thuộc diện cảnh báo: 2
Vị trí chỉ số của các sự cố cảnh báo: [2 6]
```

Hàm `np.unique` duyệt qua mảng `ma_loi` để loại bỏ các phần tử trùng lặp và sắp xếp các giá trị theo thứ tự tăng dần. Tham số `return_counts=True` yêu cầu hàm trả về đồng thời mảng `so_lan` ghi nhận số lần xuất hiện tương ứng của từng mã.

Kết quả cho thấy mã 200 xuất hiện 2 lần, mã 404 xuất hiện 3 lần, mã 500 xuất hiện 1 lần và mã 503 xuất hiện 1 lần. Đây là giải pháp đếm tần suất hiệu quả khi dữ liệu nằm ở dạng mảng số học đồng nhất.

Hàm `np.isin(ma_loi, canh_bao)` kiểm tra từng phần tử của `ma_loi` có thuộc tập danh sách `canh_bao` hay không và trả về mảng boolean có cùng kích thước. Phép tính `np.sum(la_nguy_hiem)` đếm được đúng 2 sự cố thuộc nhóm máy chủ.

Hàm `np.where(la_nguy_hiem)[0]` xác định chính xác vị trí chỉ số của các sự cố là vị trí số 2 và số 6. Quy trình kết hợp này cung cấp công cụ lọc và khoanh vùng sự cố nhanh chóng cho các luồng dữ liệu giám sát hệ thống.

:::

<!-- /worked-example -->

## 5. Nhập và xuất tệp với mảng

NumPy sở hữu định dạng nhị phân chuyên dụng `.npy` và `.npz` để lưu trữ dữ liệu mảng trực tiếp xuống đĩa, bảo toàn toàn bộ cấu trúc `shape` và `dtype` mà không bị sai số làm tròn như tệp văn bản CSV:

```python
arr = np.arange(10)

# Lưu một mảng đơn lẻ ra tệp .npy
np.save("mang_luu.npy", arr)

# Nạp mảng từ tệp .npy
arr_doc = np.load("mang_luu.npy")

# Lưu nhiều mảng vào tệp nén .npz
np.savez_compressed("du_lieu_kho.npz", a=arr, b=arr*2)

# Nạp tệp .npz (truy xuất dạng từ điển)
du_lieu = np.load("du_lieu_kho.npz")
print(du_lieu["a"])
print(du_lieu["b"])
```

---

<!-- worked-example bai-03-numpy-worked-9 -->

::: example Đóng gói và nạp nhiều mảng với tệp lưu trữ npz bằng np.savez

Trong các quy trình huấn luyện học máy, ta thường cần lưu trữ đồng thời tập đặc trưng X và nhãn mục tiêu y vào một tệp duy nhất để tiện chia sẻ và lưu trữ. Việc lưu ra nhiều tệp riêng lẻ dễ gây thất lạc hoặc lệch số lượng bản ghi giữa các tập. Hàm np.savez cho phép đóng gói nhiều mảng có nhãn vào một tệp lưu trữ định dạng .npz an toàn.

```python
import tempfile
from pathlib import Path
import numpy as np

X = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]], dtype=np.float32)
y = np.array([0, 1, 0], dtype=np.int32)

with tempfile.NamedTemporaryFile(suffix=".npz", delete=False) as f:
    duong_dan = Path(f.name)

try:
    np.savez(duong_dan, dac_trung=X, nhan=y)
    with np.load(duong_dan) as du_lieu_nap:
        cac_khoa = list(du_lieu_nap.files)
        X_nap = du_lieu_nap["dac_trung"]
        y_nap = du_lieu_nap["nhan"]
        print(f"Các khóa trong tệp: {cac_khoa}")
        print(f"Khớp mảng X: {np.array_equal(X_nap, X)}, kích thước {X_nap.shape}")
        print(f"Khớp mảng y: {np.array_equal(y_nap, y)}, kích thước {y_nap.shape}")
finally:
    duong_dan.unlink(missing_ok=True)
```

Kết quả khi chạy đoạn mã trên:

```text
Các khóa trong tệp: ['dac_trung', 'nhan']
Khớp mảng X: True, kích thước (3, 2)
Khớp mảng y: True, kích thước (3,)
```

Đoạn mã khởi tạo ma trận đặc trưng `X` có kích thước 3 hàng 2 cột và vector nhãn `y` gồm 3 số nguyên. Hàm `tempfile.NamedTemporaryFile` tạo đường dẫn tệp tạm có phần mở rộng `.npz` trên ổ đĩa.

Hàm `np.savez` nhận đường dẫn tệp và các mảng dữ liệu dưới dạng tham số từ khóa `dac_trung=X` và `nhan=y`. Định dạng `.npz` thực chất là một tệp lưu trữ zip không nén chứa các tệp `.npy` riêng lẻ bên trong. Nếu người dùng muốn nén dữ liệu để tiết kiệm dung lượng đĩa, hàm `np.savez_compressed` sẽ là lựa chọn phù hợp.

Khi đọc lại bằng hàm `np.load`, đối tượng trả về hoạt động tương tự như một từ điển. Thuộc tính `files` liệt kê danh sách các khóa đã lưu gồm `dac_trung` và `nhan`. Dữ liệu được nạp theo cơ chế lười biếng, chỉ nạp vào bộ nhớ khi ta truy xuất đến khóa cụ thể.

Hàm `np.array_equal` xác nhận các mảng nạp lại hoàn toàn trùng khớp với dữ liệu gốc ban đầu. Việc giải phóng tệp tạm trong khối `finally` bảo đảm dọn dẹp tài nguyên sau khi kết thúc quá trình kiểm thử.

:::

<!-- /worked-example -->

## 6. Đại số tuyến tính

Các phép toán ma trận trong NumPy được ủy thác cho thư viện Fortran tiêu chuẩn cao (BLAS/LAPACK):

### 6.1. Nhân ma trận với toán tử `@`
Toán tử `@` (được giới thiệu từ Python 3.5) biểu diễn phép nhân ma trận chuẩn mực, thay thế cho hàm `np.dot()`:
```python
X = np.array([[1.0, 2.0], [3.0, 4.0]])
Y = np.array([[5.0, 6.0], [7.0, 8.0]])

tich_ma_tran = X @ Y
# [[19. 22.]
#  [43. 50.]]
```

### 6.2. Các hàm trong mô-đun `numpy.linalg`
- `numpy.linalg.inv(A)`: Tính ma trận nghịch đảo của ma trận vuông $A$.
- `numpy.linalg.solve(A, b)`: Giải hệ phương trình đại số tuyến tính $Ax = b$ mà không cần tính ma trận nghịch đảo rõ ràng, giúp tăng độ chính xác số trị và tiết kiệm bộ nhớ.
- `numpy.linalg.qr(A)`: Phân rã ma trận thành tích $Q R$ (với $Q$ là ma trận trực giao và $R$ là ma trận tam giác trên).
- `numpy.linalg.svd(A)`: Phân rã giá trị suy biến $U, \Sigma, V^T$.
- `numpy.linalg.det(A)`: Tính định thức của ma trận vuông.
- `numpy.linalg.eig(A)`: Tìm trị riêng và vector riêng.

---

<!-- worked-example bai-03-numpy-worked-10 -->

::: example Giải hệ phương trình tuyến tính và phân tích QR bằng numpy.linalg

Xét hai phương trình có hai ẩn. Ta cần tìm nghiệm và kiểm tra bằng cách thế vào hệ ban đầu. Sau đó, phép phân tích QR minh họa một cách tách ma trận hệ số thành hai ma trận có cấu trúc rõ hơn.

```python
import numpy as np

# Hệ phương trình Ax = b:
#  2x + 1y = 8
#  1x + 3y = 11
A = np.array([[2.0, 1.0], [1.0, 3.0]])
b = np.array([8.0, 11.0])

x = np.linalg.solve(A, b)
Q, R = np.linalg.qr(A)

print(f"Nghiệm tìm được: x = {x[0]:.4f}, y = {x[1]:.4f}")
print(f"Kiểm tra lại A @ x = b: {np.allclose(A @ x, b)}")
print(f"Tích Q @ R khớp với A:  {np.allclose(Q @ R, A)}")
print(f"R là ma trận tam giác trên: {abs(R[1, 0]) < 1e-12}")
```

Kết quả khi chạy đoạn mã trên:

```text
Nghiệm tìm được: x = 2.6000, y = 2.8000
Kiểm tra lại A @ x = b: True
Tích Q @ R khớp với A:  True
R là ma trận tam giác trên: True
```

Đoạn mã thiết lập hệ phương trình tuyến tính hai ẩn số $Ax = b$, trong đó ma trận hệ số $A$ có kích thước 2x2 và vector vế phải $b$ có 2 phần tử. Nghiệm toán học chính xác của hệ là $x = 2.6$ và $y = 2.8$.

Hàm `np.linalg.solve` sử dụng thuật toán phân tích LU kết hợp khử Gauss của thư viện LAPACK để tìm nghiệm trực tiếp. Cả hai phương pháp `solve` và tính nghịch đảo ma trận `inv` đều có chung điều kiện suy biến khi định thức ma trận bằng không. Tuy nhiên, `solve` tránh được việc tính toán tường minh ma trận nghịch đảo, nhờ đó giảm bớt số phép tính số học và hạn chế sự tích lũy sai số dấu phẩy động.

`np.linalg.qr` tách ma trận `A` thành ma trận trực giao `Q` và ma trận tam giác trên `R`. Biểu thức `Q @ R` nhân hai ma trận lại. `np.allclose` kiểm tra các phần tử có gần với `A` trong dung sai cho phép, thay vì đòi từng số thực bằng nhau tuyệt đối.

Kết quả in ra xác nhận nghiệm thu được thỏa mãn phương trình ban đầu và phần tử dưới đường chéo của ma trận $R$ xấp xỉ bằng không. Đây là các công cụ đại số tuyến tính căn bản phục vụ xây dựng các thuật toán phân tích dữ liệu nhiều chiều.

:::

<!-- /worked-example -->

## 7. Nghiên cứu tình huống: Mô phỏng bước đi ngẫu nhiên

Một bước đi ngẫu nhiên đơn giản xuất phát từ vị trí $0$, tại mỗi bước di chuyển sang trái ($-1$) hoặc sang phải ($+1$) với xác suất ngang nhau $p = 0{,}5$.

### 7.1. Mô phỏng một bước đi ngẫu nhiên
So sánh giữa cách viết vòng lặp Python thuần và cách viết vector hóa trong NumPy:

```python
# Cách viết vector hóa trong NumPy:
n_buoc = 1000
rng = np.random.default_rng(seed=42)
buoc = np.where(rng.integers(0, 2, size=n_buoc) > 0, 1, -1)
vi_tri = np.cumsum(buoc)

print(f"Vị trí nhỏ nhất: {vi_tri.min()}, Vị trí lớn nhất: {vi_tri.max()}")
```

### 7.2. Mô phỏng đồng thời 5.000 bước đi ngẫu nhiên
Thay vì dùng vòng lặp mô phỏng từng bước đi một, NumPy cho phép mô phỏng đồng thời $5\,000$ bước đi độc lập, mỗi bước đi kéo dài $1\,000$ bước, chỉ bằng một mảng 2 chiều:

```python
n_luot = 5000
n_buoc = 1000

# Sinh đồng thời 5.000 x 1.000 bước đi
buoc_nhieu = np.where(rng.integers(0, 2, size=(n_luot, n_buoc)) > 0, 1, -1)
buoc_di = np.cumsum(buoc_nhieu, axis=1)

print(f"Kích thước mảng mô phỏng: {buoc_di.shape}")  # (5000, 1000)
```

Ta có thể tính toán thời điểm đầu tiên mỗi bước đi chạm tới khoảng cách cách gốc ít nhất 30 bước (vượt ngưỡng $+30$ hoặc $-30$):
```python
vuot_nguong_30 = np.abs(buoc_di) >= 30
co_vuot_nguong = vuot_nguong_30.any(axis=1)

print(f"Số lượng bước đi chạm ngưỡng 30: {co_vuot_nguong.sum()}")

# argmax dọc theo axis=1 trả về chỉ số đầu tiên gặp giá trị True
thoi_diem_cham = vuot_nguong_30[co_vuot_nguong].argmax(axis=1)
print(f"Thời gian chạm ngưỡng trung bình: {thoi_diem_cham.mean():.1f} bước")
```

---

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 4: NumPy Basics: Arrays and Vectorized Computation.
- Charles R. Harris và cộng sự. *Array programming with NumPy*. Nature, tập 585, trang 357–362, năm 2020.
- NumPy Developers. *NumPy Reference Documentation: Copies and Views*. https://numpy.org/doc/stable/user/basics.copies.html
- Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN. *Học liệu môn học Lập trình xử lý dữ liệu: Bài 3 - NumPy: Mảng và tư duy vector hoá*. Các bài tập thực hành 1–6 trong bài giảng được biên soạn và chuẩn hóa dựa trên học liệu mở của IAI UET theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 8. Bài tập thực hành

<span id="iai-03-bai-1"></span>

::: exercise Bài tập 1: Thời điểm đổi kiểu dữ liệu và tràn số nguyên
Cần nhân đôi các số trong mảng sau:
```python
x = np.array([50, 100, 120], dtype=np.int8)
a = (x * 2).astype(np.int16)
b = x.astype(np.int16) * 2
```
1. Dự đoán giá trị của mảng `a` và mảng `b`. Cách nào cho kết quả đúng với phép tính số học kỳ vọng?
2. Tính dung lượng bộ nhớ `nbytes` của `x`, `a`, và `b`.
3. Giải thích vì sao việc chuyển đổi sang kiểu dữ liệu `int16` ở mảng `a` vẫn cho kết quả sai lệch.
:::

::: solution Lời giải
1. Dự đoán giá trị:
   - `a`: `[100, -56, -16]`
   - `b`: `[100, 200, 240]`
   - Cách `b` cho kết quả đúng với phép tính số học kỳ vọng.
2. Dung lượng bộ nhớ:
   - Kiểu `int8` chiếm 1 byte mỗi phần tử. Mảng `x` có 3 phần tử nên `x.nbytes = 3 * 1 = 3` byte.
   - Kiểu `int16` chiếm 2 byte mỗi phần tử. Mảng `a` và `b` có 3 phần tử nên `a.nbytes = b.nbytes = 3 * 2 = 6` byte.
3. Giải thích nguyên nhân sai lệch:
   - Ở biểu thức `a = (x * 2).astype(np.int16)`, phép nhân `x * 2` được thực hiện trước trên kiểu dữ liệu gốc `int8` (miền giá trị từ $-128$ đến $127$). Khi nhân $100 \times 2 = 200$ và $120 \times 2 = 240$, các giá trị này vượt quá ngưỡng $127$ nên bị tràn số nhị phân thành $200 - 256 = -56$ và $240 - 256 = -16$. Phương thức `.astype(np.int16)` thực hiện sau đó chỉ làm nhiệm vụ chuyển đổi các giá trị đã bị sai lệch sang `int16`.
   - Ở biểu thức `b`, mảng `x` được chuyển đổi sang kiểu `int16` trước (miền giá trị từ $-32\,768$ đến $32\,767$), sau đó phép nhân đôi diễn ra an toàn mà không bị tràn số. Bài học: Luôn nâng cấp kiểu dữ liệu trước khi thực hiện các phép tính có nguy cơ vượt ngưỡng.
:::

<span id="iai-03-bai-2"></span>

::: exercise Bài tập 2: Thay thế vòng lặp for bằng phép toán mảng vector hóa
Đoạn mã Python sau tính bình phương chênh lệch của từng cặp số:
```python
x = np.array([10, 12, 11, 20])
y = np.array([12, 11, 15, 20])
ket_qua = []
for u, v in zip(x, y):
    ket_qua.append((v - u) ** 2)
```
1. Tính toán giá trị của danh sách `ket_qua`.
2. Viết lại phép tính trên bằng một biểu thức NumPy duy nhất, không sử dụng vòng lặp `for`.
3. Bản viết lại vẫn phải tính toán trên từng cặp số. Vì sao đối với các mảng dữ liệu lớn, biểu thức NumPy lại có tốc độ thực thi vượt trội hơn rất nhiều so với vòng lặp Python?
:::

::: solution Lời giải
1. Tính toán thủ công:
   - Cặp $(10, 12)$: $(12 - 10)^2 = 2^2 = 4$.
   - Cặp $(12, 11)$: $(11 - 12)^2 = (-1)^2 = 1$.
   - Cặp $(11, 15)$: $(15 - 11)^2 = 4^2 = 16$.
   - Cặp $(20, 20)$: $(20 - 20)^2 = 0^2 = 0$.
   - Kết quả: `[4, 1, 16, 0]`.
2. Viết lại bằng biểu thức NumPy:
```python
ket_qua_np = (y - x) ** 2
```
3. Giải thích nguyên nhân chênh lệch tốc độ:
   - Vòng lặp `for` của Python phải thông dịch từng lệnh bytecode ở mỗi vòng lặp, kiểm tra kiểu động của từng đối tượng và cấp phát các đối tượng số nguyên Python bọc ngoài (*boxed objects*).
   - Biểu thức `(y - x) ** 2` gọi các phép toán mảng đã biên dịch. Nó vẫn xử lý từng cặp giá trị, nhưng giảm công việc gọi lệnh và xử lý đối tượng ở mỗi lượt Python. Truy cập liên tiếp có thể giúp sử dụng bộ nhớ đệm. Hiệu năng thực tế và việc dùng SIMD còn phụ thuộc dtype, bố trí mảng, phép toán và phần cứng.
:::

<span id="iai-03-bai-3"></span>

::: exercise Bài tập 3: Xác định vị trí phần tử trong bộ nhớ từ Strides
Cho mảng hai chiều $A$ gồm các số nguyên 64-bit:
```python
A = np.array([[10, 12, 11],
              [20, 21, 24],
              [30, 33, 31],
              [40, 44, 42]], dtype=np.int64)
```
Mảng $A$ có kích thước `shape = (4, 3)` và bước nhảy `strides = (24, 8)` (đơn vị byte).
1. Phần tử $A[1, 2]$ cách vị trí bắt đầu vùng dữ liệu của $A$ bao nhiêu byte?
2. Một phần tử nằm cách vị trí bắt đầu vùng dữ liệu $80$ byte mang giá trị nào và tương ứng với chỉ số hàng, cột nào?
3. Nếu ta chuyển đổi mảng sang kiểu số nguyên 32-bit: `B = A.astype(np.int32)`. Kích thước `shape` và bước nhảy `strides` của mảng $B$ bằng bao nhiêu? Giải thích vì sao `shape` không đổi nhưng `strides` lại thay đổi.
:::

::: solution Lời giải
1. Gọi O là độ lệch byte, $s_0$ là bước nhảy hàng và $s_1$ là bước nhảy cột. Với chỉ số hàng i và cột j:
   $$
   O = i s_0 + j s_1
   $$
   Với phần tử $A[1, 2]$:
   $$
   \begin{aligned}
   O &= 1 \cdot 24 + 2 \cdot 8, \\
   &= 40\,\mathrm{byte}.
   \end{aligned}
   $$
2. Tìm chỉ số từ độ lệch $80$ byte:
   - Chỉ số hàng $i = 80 // 24 = 3$ (vì $3 \times 24 = 72$, phần dư là $8$).
   - Chỉ số cột $j = (80 - 72) // 8 = 8 // 8 = 1$.
   - Phần tử tương ứng là $A[3, 1]$, có giá trị bằng $44$.
3. Khi chuyển sang `int32`:
   - Kích thước của mỗi phần tử giảm từ 8 byte xuống 4 byte (`itemsize = 4`).
   - `shape` vẫn giữ nguyên là `(4, 3)` vì cấu trúc số hàng và số cột không đổi.
   - Bước nhảy `strides` thay đổi: Bước cột bằng kích thước một phần tử là $4$ byte, trong khi bước hàng bằng 3 cột $\times 4$ byte $= 12$ byte. Như vậy, `B.strides = (12, 4)`.
:::

<span id="iai-03-bai-4"></span>

::: exercise Bài tập 4: Xác định các ô của View và kiểm chứng bộ nhớ dùng chung
Cho mảng $A$ tương tự bài trước:
```python
A = np.array([[10, 12, 11],
              [20, 21, 24],
              [30, 33, 31],
              [40, 44, 42]], dtype=np.int64)

V = A[::2, 1:]
```
1. Xác định các giá trị và kích thước `V.shape` của mảng $V$.
2. Tính bước nhảy `V.strides`. Phần tử đầu tiên của $V$ cách vị trí bắt đầu vùng dữ liệu của $A$ bao nhiêu byte?
3. Nếu thực hiện phép gán `V[1, 0] = 999`, phần tử nào của mảng $A$ sẽ bị thay đổi? Giải thích bằng vị trí trong bộ nhớ.
:::

::: solution Lời giải
1. Lát cắt `::2` lấy các hàng với bước nhảy 2, tức là chọn hàng 0 và hàng 2. Lát cắt `1:` lấy các cột từ chỉ số 1 trở đi, tức là chọn cột 1 và cột 2.
   - Hàng 0 của $V$ là hàng 0 của $A$ lấy cột 1, 2: `[12, 11]`.
   - Hàng 1 của $V$ là hàng 2 của $A$ lấy cột 1, 2: `[33, 31]`.
   - Giá trị của $V$: `[[12, 11], [33, 31]]`.
   - Kích thước: `V.shape = (2, 2)`.
2. Bước nhảy `V.strides`:
   - Để nhảy từ hàng 0 sang hàng 1 của $V$, trong mảng gốc $A$ ta phải nhảy qua 2 hàng. Mỗi hàng của $A$ tốn 24 byte, nên bước nhảy hàng của $V$ là $2 \times 24 = 48$ byte.
   - Bước nhảy cột của $V$ vẫn là khoảng cách giữa hai cột liên tiếp, tương ứng với $8$ byte.
   - Vậy `V.strides = (48, 8)`.
   - Phần tử đầu tiên của $V$ chính là $A[0, 1]$. Độ lệch byte so với đầu mảng $A$ bằng $0 \times 24 + 1 \times 8 = 8$ byte.
3. Phần tử $V[1, 0]$ tương ứng với hàng 1, cột 0 của $V$:
   - Hàng 1 của $V$ tương ứng với hàng 2 của $A$.
   - Cột 0 của $V$ tương ứng với cột 1 của $A$.
   - Do đó, $V[1, 0]$ ánh xạ trực tiếp tới phần tử $A[2, 1]$. Khi gán `V[1, 0] = 999`, giá trị $33$ của $A[2, 1]$ sẽ bị ghi đè thành $999$.
:::

<span id="iai-03-bai-6"></span>

::: exercise Bài tập 6: Sửa lỗi phép trừ trung bình hàng do hiểu sai Broadcasting
Một bạn sinh viên muốn chuẩn hóa mảng dữ liệu $M$ bằng cách lấy mỗi phần tử trừ đi giá trị trung bình của hàng chứa nó:
```python
M = np.array([[10, 12, 11],
              [20, 21, 24],
              [30, 33, 31]])

tb = M.mean(axis=1)
chenh_lech = M - tb
```
Ví dụ: Hàng đầu tiên $[10, 12, 11]$ có trung bình là $11$, kết quả mong muốn là $[-1, 1, 0]$.
1. Chạy thử đoạn mã trên cho thấy chương trình không báo lỗi nhưng kết quả lại tính sai. Hãy giải thích nguyên nhân gây ra lỗi logic này.
2. Hãy sửa lại đoạn mã để phép tính cho kết quả đúng và kiểm chứng giá trị của hàng đầu tiên.
:::

::: solution Lời giải
1. Nguyên nhân lỗi logic:
   - Mảng $M$ có kích thước `shape = (3, 3)`.
   - Lệnh `tb = M.mean(axis=1)` tính trung bình theo hàng, nhưng trả về một mảng một chiều có `shape = (3,)`.
   - Theo quy tắc phát sóng của NumPy, khi thực hiện `M - tb`, mảng $1$ chiều `tb` được căn chỉnh theo trục cuối cùng (trục cột), tức là `tb` được coi như một hàng $(1, 3)$ và kéo dài dọc theo 3 hàng. Kết quả là mỗi cột của $M$ bị trừ đi phần tử tương ứng của `tb`, hoàn toàn trái ngược với ý muốn ban đầu là trừ theo từng hàng.
2. Sửa lại đoạn mã:
   Cần giữ nguyên số chiều của mảng kết quả trung bình bằng tham số `keepdims=True` để `tb` có `shape = (3, 1)`. Khi đó NumPy sẽ kéo dài cột trung bình ngang qua 3 cột của mỗi hàng:
```python
tb_chuan = M.mean(axis=1, keepdims=True)  # shape = (3, 1)
chenh_lech = M - tb_chuan
```
   Kiểm tra hàng đầu tiên:
   - Trung bình hàng: $(10 + 12 + 11) / 3 = 11$.
   - Chênh lệch: $[10 - 11, 12 - 11, 11 - 11] = [-1, 1, 0]$. Phép tính hoàn toàn chính xác.
:::





<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-03">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-03.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 4: NumPy Basics: Arrays and Vectorized Computation.
- Charles R. Harris và cộng sự. *Array programming with NumPy*. Nature, tập 585, trang 357–362, năm 2020.
- NumPy Developers. *NumPy Reference Documentation: Copies and Views*. https://numpy.org/doc/stable/user/basics.copies.html
- Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN. *Học liệu môn học Lập trình xử lý dữ liệu: Bài 3 - NumPy: Mảng và tư duy vector hoá*. Các bài tập thực hành 1–6 trong bài giảng được biên soạn và chuẩn hóa dựa trên học liệu mở của IAI UET theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
