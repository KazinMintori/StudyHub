---
course: xu-ly-du-lieu
lecture: phu-luc-a-numpy-nang-cao
section: lecture
title: "Phụ lục A: NumPy nâng cao"
prerequisites: ["mang", "vector-hoa", "broadcasting"]
lessonStatus: ready
hasChapterExercises: true
description: "Khám phá kiến trúc nội bộ của ndarray: Strides, cây phả hệ dtype, chia sẻ bộ nhớ np.shares_memory, broadcasting nâng cao, phương thức ufunc, mảng cấu trúc, Numba JIT và tệp ánh xạ bộ nhớ memmap."
---


<div class="lecture-notes-content">

Trong hầu hết các tác vụ phân tích dữ liệu hàng ngày, người lập trình thường tương tác với mảng NumPy như một khối số liệu hộp đen. Tuy nhiên, khi đối mặt với các bài toán dữ liệu lớn vượt ngưỡng dung lượng bộ nhớ RAM, các thuật toán đòi hỏi hiệu năng tính toán cao, hoặc khi cần giao tiếp trực tiếp với các thư viện viết bằng C và Fortran, việc thấu hiểu kiến trúc tầng sâu của đối tượng `ndarray` trở thành yếu tố then chốt.

NumPy đạt hiệu năng tính toán cao nhờ vào kiến trúc vùng nhớ khối liên tục kết hợp với bảng thông tin mô tả siêu dữ liệu (Metadata). Thay vì sao chép dữ liệu mỗi khi thực hiện chuyển dạng, NumPy thao tác trực tiếp trên các bước nhảy địa chỉ byte (`strides`), cho phép tái cấu trúc không gian dữ liệu với chi phí thời gian không đáng kể.

Phụ lục này trình bày các chủ đề nâng cao của NumPy: Cấu trúc nội bộ và cây phả hệ kiểu dữ liệu vô hướng, các phép biến đổi mảng nâng cao, cơ chế phương thức của `ufunc`, mảng cấu trúc nhị phân, các thuật toán sắp xếp chuyên sâu, kỹ thuật tăng tốc với Numba (tùy chọn) và ánh xạ bộ nhớ `memmap`.

---

## 1. Cấu trúc nội bộ của đối tượng `ndarray` và cây phả hệ kiểu dữ liệu

Mỗi đối tượng mảng `ndarray` trong NumPy được cấu thành từ hai phần tách biệt:
1. **Khối dữ liệu thô (Data buffer)**: Vùng nhớ RAM liên tục chứa các byte dữ liệu nhị phân nguyên thủy.
2. **Siêu dữ liệu mô tả (Metadata)**: Khối thông tin nhỏ gọn giải thích cách diễn giải các byte thô đó thành một cấu trúc nhiều chiều.

Khối siêu dữ liệu bao gồm bốn thuộc tính cốt lõi:
- `data`: Con trỏ trỏ đến địa chỉ ô nhớ byte đầu tiên của mảng.
- `dtype`: Kiểu dữ liệu, quy định mỗi phần tử chiếm bao nhiêu byte và được hiểu là số nguyên, số thực hay chuỗi nhị phân.
- `shape`: Bộ số nguyên quy định số lượng phần tử dọc theo từng trục.
- `strides`: Bộ số nguyên quy định **số byte cần nhảy qua trong bộ nhớ** để tiến thêm một vị trí dọc theo trục tương ứng.

```python
import numpy as np

# Tạo mảng 2 chiều 3 hàng, 4 cột với kiểu int32 (mỗi số chiếm 4 byte)
arr = np.arange(12, dtype=np.int32).reshape(3, 4)

print("Kích thước (shape):", arr.shape)     # (3, 4)
print("Kiểu dữ liệu (dtype):", arr.dtype)   # int32
print("Bước nhảy bộ nhớ (strides):", arr.strides) # (16, 4)
```

Hãy quan sát bước nhảy bộ nhớ `strides = (16, 4)`:
- Để di chuyển sang cột kế tiếp trên cùng một hàng, con trỏ cần dịch chuyển đúng 4 byte (đúng bằng kích thước của một số `int32`).
- Để di chuyển sang hàng kế tiếp tại cùng một vị trí cột, con trỏ cần dịch chuyển $4 \times 4 = 16$ byte (bằng kích thước của toàn bộ một hàng gồm 4 phần tử).

Chính nhờ cơ chế `strides`, thao tác chuyển vị ma trận `arr.T` trong NumPy diễn ra tức thì trong $O(1)$: NumPy hoán đổi bộ `strides` từ `(16, 4)` thành `(4, 16)` mà không cần sao chép hay dịch chuyển các byte dữ liệu trong RAM.

### Cây phả hệ kiểu dữ liệu vô hướng trong NumPy (Scalar type hierarchy)

Cần phân biệt rõ ràng giữa hai khái niệm:
1. **Đối tượng mô tả kiểu (`np.dtype`)**: Là đối tượng siêu dữ liệu gắn với mảng `ndarray`, quy định kích thước byte (itemsize), thứ tự byte (endianness) và cách diễn giải vùng nhớ đệm của toàn mảng.
2. **Kiểu vô hướng (NumPy scalar types)**: Là các kiểu giá trị khi trích xuất một phần tử đơn lẻ ra khỏi mảng (ví dụ `np.int32`, `np.float64`). Hệ thống kiểu vô hướng này kế thừa từ lớp cơ sở trừu tượng `np.generic`, không phải là lớp cha của đối tượng `np.dtype`.

Cây phân cấp kiểu vô hướng NumPy:
- `np.generic`: Lớp cơ sở của mọi kiểu vô hướng trong NumPy.
  - `np.number`: Kiểu số tổng quát.
    - `np.integer`: Số nguyên.
      - `np.signedinteger`: Số nguyên có dấu (`int8`, `int16`, `int32`, `int64`).
      - `np.unsignedinteger`: Số nguyên không dấu (`uint8`, `uint16`, `uint32`, `uint64`).
    - `np.inexact`: Số có sai số biểu diễn.
      - `np.floating`: Số thực dấu phẩy động (`float16`, `float32`, `float64`).
      - `np.complexfloating`: Số phức (`complex64`, `complex128`).

Hàm `np.issubdtype(a, b)` nhận hai tham số (kiểu vô hướng hoặc đối tượng dtype) và xác định xem `a` có phải là kiểu con của họ kiểu `b` trên cây phân cấp kiểu vô hướng hay không:

```python
# Kiểm tra quan hệ phả hệ kiểu vô hướng
print(np.issubdtype(arr.dtype, np.integer))   # True
print(np.issubdtype(np.float64, np.floating)) # True
print(np.issubdtype(np.float64, np.number))   # True
print(np.issubdtype(np.int32, np.floating))   # False
```

Kỹ thuật này giúp các hàm xử lý dữ liệu kiểm tra tính tương thích của đầu vào một cách tổng quát, thay vì phải so sánh thủ công với từng kiểu cụ thể như `arr.dtype == np.float32 or arr.dtype == np.float64`.

---

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-1 -->

::: example Kiểm tra tương thích kiểu dữ liệu bằng np.issubdtype

Khi xây dựng các hàm tính toán số học tổng quát, việc so sánh cứng với từng kiểu dữ liệu cụ thể dễ bỏ sót các biến thể hợp lệ khác. Hàm np.issubdtype cho phép kiểm tra quan hệ kế thừa trên cây phả hệ kiểu vô hướng của NumPy để xác định kiểu dữ liệu đầu vào.

```python
import numpy as np
import pandas as pd

# Tập hợp các kiểu dữ liệu đại diện
cac_kieu = [np.float32, np.float64, np.int32, np.int64, np.complex128]

bang_kq = pd.DataFrame({
    "kieu": [k.__name__ for k in cac_kieu],
    "la_so": [bool(np.issubdtype(k, np.number)) for k in cac_kieu],
    "la_so_thuc": [bool(np.issubdtype(k, np.floating)) for k in cac_kieu],
    "la_so_nguyen": [bool(np.issubdtype(k, np.integer)) for k in cac_kieu],
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| kieu | la&#95;so | la&#95;so&#95;thuc | la&#95;so&#95;nguyen |
| --- | --- | --- | --- |
| float32 | `True` | `True` | `False` |
| float64 | `True` | `True` | `False` |
| int32 | `True` | `False` | `True` |
| int64 | `True` | `False` | `True` |
| complex128 | `True` | `False` | `False` |

</div>

Hệ thống kiểu dữ liệu trong NumPy được cấu trúc theo một cây phân cấp kế thừa xuất phát từ lớp cơ sở `np.generic`. Khi viết các hàm xử lý tính toán số học, việc kiểm tra kiểu bằng toán tử so sánh bằng như `arr.dtype == np.float64` sẽ khiến hàm từ chối các kiểu số thực hợp lệ khác như `float32` hoặc `float16`.

`np.issubdtype(kieu_con, kieu_cha)` kiểm tra quan hệ kiểu. `np.number` bao gồm các họ số nguyên, số thực dấu phẩy động và số phức của NumPy. `np.inexact` là họ số có biểu diễn gần đúng, không có nghĩa mọi giá trị thuộc họ này đều mang phần thập phân khác 0.

Nhánh `np.inexact` tiếp tục phân tách thành kiểu số thực `np.floating` và số phức `np.complexfloating`. Bảng kết quả thể hiện rõ cấu trúc này: Cả `float32` và `float64` đều thuộc `np.floating` và `np.number`, trong khi các kiểu `int32` và `int64` thuộc `np.integer` và `np.number`. Kiểu `complex128` là số học nhưng không thuộc nhánh số thực hay số nguyên.

:::

<!-- /worked-example -->

## 2. Các phép biến đổi mảng nâng cao

### Thứ tự lưu trữ: Hàng trước (C-order) so với Cột trước (Fortran-order)

Trong bộ nhớ máy tính một chiều, ma trận hai chiều có thể được xếp phẳng theo hai quy ước:
1. **Thứ tự C (Row-Major / C-order)**: Các phần tử trên cùng một hàng nằm cạnh nhau trong bộ nhớ. Đây là chuẩn mặc định của C/C++ và Python.
2. **Thứ tự Fortran (Column-Major / F-order)**: Các phần tử trên cùng một cột nằm cạnh nhau trong bộ nhớ. Đây là chuẩn truyền thống của Fortran và MATLAB.

```python
arr_c = np.ones((1000, 1000), order="C")
arr_f = np.ones((1000, 1000), order="F")

print("Mảng C có c_contiguous không?", arr_c.flags.c_contiguous) # True
print("Mảng F có f_contiguous không?", arr_f.flags.f_contiguous) # True
```

### Kiểm tra chia sẻ bộ nhớ với `np.shares_memory`

Một trong những nguồn gốc gây lỗi nguy hiểm nhất trong NumPy là việc ngộ nhận giữa **khung nhìn (View)** và **bản sao độc lập (Copy)**. Nếu hai mảng cùng chia sẻ một khối nhớ đệm, thay đổi giá trị trên mảng này sẽ làm biến đổi ngầm mảng kia.

Hàm `np.shares_memory()` là công cụ chuẩn xác nhất để xác minh hai mảng có dùng chung vùng nhớ hay không:

```python
goc = np.arange(12).reshape(3, 4)

# 1. Reshape tạo một View chia sẻ bộ nhớ
doi_hinh = goc.reshape(2, 6)
print("Reshape có chia sẻ bộ nhớ không?", np.shares_memory(goc, doi_hinh)) # True

# 2. Phẳng hóa: ravel() so với flatten()
# ravel() trả về View nếu thứ tự yêu cầu tương thích với strides hiện tại
view_phang = goc.ravel()     # Mặc định order='C', tương thích với strides nên trả về View
sao_phang = goc.flatten()   # Luôn cấp phát vùng nhớ mới và tạo Copy độc lập

print("ravel() có chia sẻ bộ nhớ không?", np.shares_memory(goc, view_phang))   # True
print("flatten() có chia sẻ bộ nhớ không?", np.shares_memory(goc, sao_phang)) # False
```

Cơ chế tạo View hay Copy của phép làm phẳng:
- `ravel(order='C')`: Trả về một **View** nếu cấu trúc bước nhảy (`strides`) của mảng tương thích với thứ tự duyệt được yêu cầu (chẳng hạn mảng C-contiguous duyệt theo thứ tự C). Nếu thứ tự yêu cầu không khớp với bố cục bước nhảy hiện tại (ví dụ gọi `goc.T.ravel(order='C')` trên ma trận chuyển vị, hoặc mảng bị cắt lát gián cách), `ravel()` bắt buộc phải tạo một bản sao độc lập (Copy).
- `flatten()`: Luôn luôn cấp phát vùng nhớ mới và tạo một **Copy** độc lập, bất kể mảng có liên tục hay không.

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-2 -->

::: example Phân biệt mức độ chồng lấn bộ nhớ bằng shares_memory và may_share_memory

Khi thao tác cắt lát và chuyển dạng ma trận, việc xác định một mảng là khung nhìn hay bản sao quyết định tính độc lập của dữ liệu. Các hàm np.shares_memory và np.may_share_memory kiểm tra mức độ chồng lấn vùng nhớ giữa hai mảng.

```python
import numpy as np
import pandas as pd

goc = np.arange(6, dtype=np.int32)

# Tạo ba đối tượng dẫn xuất từ mảng gốc
cat_lat = goc[1:4]             # View cắt lát
chuyen_dang = goc.reshape(2, 3) # View chuyển dạng
sao_chep = goc.copy()          # Copy độc lập

bang_kq = pd.DataFrame([
    {
        "doi_tuong": "cat_lat",
        "shares_memory": bool(np.shares_memory(goc, cat_lat)),
        "may_share": bool(np.may_share_memory(goc, cat_lat)),
    },
    {
        "doi_tuong": "chuyen_dang",
        "shares_memory": bool(np.shares_memory(goc, chuyen_dang)),
        "may_share": bool(np.may_share_memory(goc, chuyen_dang)),
    },
    {
        "doi_tuong": "sao_chep",
        "shares_memory": bool(np.shares_memory(goc, sao_chep)),
        "may_share": bool(np.may_share_memory(goc, sao_chep)),
    },
])
print(bang_kq)
chan = goc[::2]
le = goc[1::2]
print("Hai lát chẵn/lẻ có thể chung bộ nhớ:", np.may_share_memory(chan, le))
print("Hai lát chẵn/lẻ thực sự chung ô nhớ:", np.shares_memory(chan, le))
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| doi&#95;tuong | shares&#95;memory | may&#95;share |
| --- | --- | --- |
| cat&#95;lat | `True` | `True` |
| chuyen&#95;dang | `True` | `True` |
| sao&#95;chep | `False` | `False` |

</div>

```text
Hai lát chẵn/lẻ có thể chung bộ nhớ: True
Hai lát chẵn/lẻ thực sự chung ô nhớ: False
```

Cơ chế khung nhìn (View) trong NumPy cho phép tạo ra các mảng mới trỏ chung vào khối nhớ đệm của mảng ban đầu kèm theo thông tin kích thước và bước nhảy (strides) tương ứng. Khi cắt lát `goc[1:4]` hoặc đổi dạng `goc.reshape(2, 3)`, dữ liệu không bị sao chép sang vùng nhớ mới, giúp tiết kiệm thời gian khởi tạo và dung lượng bộ nhớ.

`np.shares_memory` trả `True` khi hai mảng có phần dữ liệu thực sự chồng lấn. Nếu ghi vào phần chồng lấn, mảng kia sẽ nhìn thấy giá trị đổi. Nó không có nghĩa mọi ô của hai mảng đều trùng nhau. `.copy()` trong ví dụ tạo vùng dữ liệu độc lập nên phép kiểm tra cho `False`.

`np.may_share_memory` mặc định kiểm tra giới hạn vùng nhớ, nên `True` chỉ là có khả năng chồng lấn. Hai lát chẵn và lẻ có vùng bao địa chỉ giao nhau nhưng không dùng chung một phần tử nào. Vì vậy, phép kiểm tra nhanh cho `True`, còn `shares_memory` cho `False`.

:::

<!-- /worked-example -->

### Nối và tách mảng: `concatenate`, `split`, `np.r_` và `np.c_`

Bên cạnh các hàm nối truyền thống, NumPy cung cấp hai đối tượng tiện ích cú pháp mạnh mẽ là `np.r_` (xếp chồng theo hàng) và `np.c_` (xếp chồng theo cột):

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Nối theo cột thành ma trận 2 chiều
ma_tran_cot = np.c_[a, b]
print("Xếp chồng theo cột:\n", ma_tran_cot)

# Nối theo hàng thành vector dài
vector_hang = np.r_[a, b]
print("Xếp chồng theo hàng:\n", vector_hang)
```

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-3 -->

::: example Tách mảng thành các phần không đều bằng array_split

Khi phân chia mảng thành các khối để xử lý song song hoặc kiểm định chéo, tổng số phần tử không phải lúc nào cũng chia hết cho số phần mong muốn. Hàm np.array_split cho phép chia mảng thành các khối có kích thước chênh lệch không quá một phần tử.

```python
import numpy as np
import pandas as pd

# Mảng 10 phần tử cần chia thành 3 phần (10 không chia hết cho 3)
arr = np.arange(10)
cac_phan = np.array_split(arr, 3)

bang_kq = pd.DataFrame([
    {
        "khoi": i + 1,
        "kich_thuoc": len(p),
        "noi_dung": str(p.tolist()),
    }
    for i, p in enumerate(cac_phan)
])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| khoi | kich&#95;thuoc | noi&#95;dung |
| --- | --- | --- |
| 1 | 4 | &#91;0, 1, 2, 3&#93; |
| 2 | 3 | &#91;4, 5, 6&#93; |
| 3 | 3 | &#91;7, 8, 9&#93; |

</div>

Khi truyền số phần nguyên như `np.split(arr, 3)`, độ dài trên trục chia phải chia hết cho 3. Mảng 10 phần tử không thỏa nên lời gọi đó báo lỗi. `np.split` cũng nhận danh sách vị trí cắt như `[4, 7]`, khi đó có thể tạo các đoạn dài khác nhau.

Hàm `np.array_split` giải quyết tình huống trên bằng cách cho phép chia mảng thành các phần có kích thước gần bằng nhau. Khi mảng 10 phần tử được chia thành 3 phần, hàm phân bổ phần dư vào các khối đầu tiên, tạo ra khối thứ nhất có 4 phần tử và hai khối tiếp theo mỗi khối có 3 phần tử. Độ chênh lệch kích thước giữa các khối được giữ ở mức tối đa là một phần tử.

Các mảng con trả về từ `np.array_split` thường là các khung nhìn trỏ vào dữ liệu của mảng ban đầu. Dù không sao chép lại toàn bộ mảng dữ liệu, mỗi mảng con vẫn là một đối tượng Python độc lập sở hữu siêu dữ liệu riêng về kích thước, bước nhảy và con trỏ vùng đệm, do đó vẫn chiếm dụng một phần tài nguyên quản lý của tiến trình chứ không tiêu thụ mức bộ nhớ bằng không.

:::

<!-- /worked-example -->

### Lặp lại phần tử: Phân biệt `repeat` và `tile`

- `np.repeat`: Lặp lại **từng phần tử** liên tiếp nhau.
- `np.tile`: "Lát gạch", lặp lại **toàn bộ khối mảng** theo số lần quy định.

```python
x = np.array([1, 2])

print("np.repeat:", np.repeat(x, 3)) # [1, 1, 1, 2, 2, 2]
print("np.tile:", np.tile(x, 3))     # [1, 2, 1, 2, 1, 2]
```

### Chỉ mục nâng cao tương đương: `take` và `put`

Khi cần chọn hoặc gán giá trị dọc theo một trục xác định mà không muốn viết các biểu thức cắt lát phức tạp, ta dùng `take` và `put`:

```python
m = np.arange(12).reshape(3, 4)

# take: Trích xuất các hàng 0 và 2
hang_chon = m.take([0, 2], axis=0)
print("Kết quả take theo trục 0:\n", hang_chon)

# put: Gán giá trị tại các vị trí chỉ mục phẳng (flat indices)
v = np.zeros(5, dtype=int)
v.put([1, 3], [10, 30])
print("Kết quả put:", v) # [0, 10, 0, 30, 0]
```

---

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-4 -->

::: example Trích xuất và gán phần tử trên trục chỉ định với take và put_along_axis

Khi thao tác trên mảng đa chiều, việc trích xuất hoặc ghi đè phần tử theo chỉ mục trên một trục cụ thể đòi hỏi các biểu thức chỉ số phức tạp. Các hàm np.take và np.put_along_axis cung cấp phương thức thao tác trực tiếp trên trục chỉ định.

```python
import numpy as np
import pandas as pd

# Ma trận kích thước (3, 3)
ma_tran = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90],
])

# 1. take: Trích xuất hàng 0 và hàng 2 dọc theo trục 0
hang_trich = np.take(ma_tran, [0, 2], axis=0)
print("Hai hàng đã lấy:")
print(pd.DataFrame(hang_trich, columns=["c0", "c1", "c2"]))

# 2. put_along_axis: Gán giá trị 999 vào vị trí cột chỉ định trên từng hàng
vi_tri_cot = np.array([[0], [1], [2]]) # Cột 0 hàng 0, cột 1 hàng 1, cột 2 hàng 2
np.put_along_axis(ma_tran, vi_tri_cot, 999, axis=1)

bang_kq = pd.DataFrame(ma_tran, columns=["c0", "c1", "c2"])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

```text
Hai hàng đã lấy:
```

<div class="data-worked-table">

| c0 | c1 | c2 |
| --- | --- | --- |
| 10 | 20 | 30 |
| 70 | 80 | 90 |

</div>

<div class="data-worked-table">

| c0 | c1 | c2 |
| --- | --- | --- |
| 999 | 20 | 30 |
| 40 | 999 | 60 |
| 70 | 80 | 999 |

</div>

`np.take` hữu ích khi trục cần chọn được xác định bằng một tham số. Với `axis=0`, các chỉ số 0 và 2 chọn hai hàng. Có thể viết kết quả tương tự bằng `ma_tran[[0, 2]]`, nhưng `take` làm rõ trục trong các hàm nhận mảng có nhiều chiều.

Hàm `np.take` nhận tham số `axis` rõ ràng, hỗ trợ trích xuất dữ liệu dọc theo trục được chỉ định. Trong đoạn mã, lệnh `np.take(ma_tran, [0, 2], axis=0)` lấy ra hàng 0 và hàng 2 của ma trận để tạo thành một mảng mới kích thước `(2, 3)` mà không làm xáo trộn cấu trúc các chiều còn lại.

Đối với chiều ghi dữ liệu, hàm `np.put_along_axis` cho phép ghi đè giá trị tại chỗ theo các vị trí chỉ số tương ứng dọc theo trục chỉ định. Với mảng chỉ số `vi_tri_cot` và trục `axis=1`, giá trị 999 được gán trực tiếp vào các vị trí tương ứng trên từng hàng, tạo nên ma trận kết quả với giá trị mới xuất hiện trên đường chéo như thể hiện trong bảng số liệu.

:::

<!-- /worked-example -->

## 3. Cơ chế Broadcasting mở rộng

Broadcasting là quy tắc toán học cho phép thực hiện phép tính giữa hai mảng có kích thước khác nhau mà không cần tốn bộ nhớ nhân bản dữ liệu.

### Quy tắc căn lề kích thước (Broadcasting Rules)

So sánh kích thước của hai mảng từ **chiều cuối cùng lùi về trước**:
Hai chiều tương thích khi và chỉ khi:
1. Kích thước của chúng bằng nhau, hoặc
2. Một trong hai kích thước có độ dài bằng 1.

Nếu một mảng thiếu chiều, trục kích thước 1 sẽ được tự động bổ sung vào phía trước.

### Mở rộng trục bằng `np.newaxis`

Từ khóa `np.newaxis` (hoặc giá trị `None`) cho phép chèn một trục có kích thước 1 vào bất kỳ vị trí nào:

```python
vec_cot = np.array([10, 20, 30])[:, np.newaxis] # Shape (3, 1)
vec_hang = np.array([1, 2])                     # Shape (2,) -> Tương thích thành (1, 2)

# Ma trận kết quả có kích thước (3, 2)
bang_cong = vec_cot + vec_hang
print("Kết quả broadcasting mở rộng:\n", bang_cong)
```

Ta cũng có thể sử dụng broadcasting để gán giá trị đồng loạt cho một khối mảng con:

```python
bang = np.zeros((3, 4))
bang[:] = [1, 2, 3, 4] # Vector hàng được mở rộng và gán cho cả 3 hàng
print("Bảng sau khi gán bằng broadcasting:\n", bang)
```

---

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-5 -->

::: example Tính toán ma trận khoảng cách Euclid bằng broadcasting và np.newaxis

Tính khoảng cách giữa hai tập hợp điểm là phép toán cơ bản trong nhiều thuật toán máy học. Mở rộng trục bằng np.newaxis cho phép tận dụng cơ chế broadcasting để tính toán khoảng cách đôi một giữa các điểm dữ liệu.

```python
import numpy as np
import pandas as pd

# Tập A gồm 2 điểm trong không gian 2D, tập B gồm 2 tâm cụm
pts_a = np.array([[0.0, 0.0], [3.0, 4.0]])
pts_b = np.array([[1.0, 1.0], [0.0, 0.0]])

# Mở rộng trục để broadcasting: (2, 1, 2) trừ (1, 2, 2) ra (2, 2, 2)
diff = pts_a[:, np.newaxis, :] - pts_b[np.newaxis, :, :]
dists = np.sqrt(np.sum(diff**2, axis=-1))

bang_kq = pd.DataFrame(dists.round(2), columns=["b0", "b1"])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| b0 | b1 |
| --- | --- |
| 1.41 | 0.0 |
| 3.61 | 5.0 |

</div>

Bài toán tính khoảng cách đôi một giữa tập điểm $A$ kích thước $(N, D)$ và tập điểm $B$ kích thước $(M, D)$ xuất hiện trong các thuật toán như k-Means hay k-NN. Thay vì sử dụng các vòng lặp lồng nhau qua từng cặp điểm, cơ chế broadcasting của NumPy cho phép mở rộng các chiều có kích thước bằng 1 để thực hiện phép trừ đồng loạt trên các mảng đa chiều.

Bằng cách chèn `np.newaxis`, mảng `pts_a` được chuyển thành hình dạng `(2, 1, 2)` và `pts_b` thành `(1, 2, 2)`. Phép trừ `diff = pts_a[:, np.newaxis, :] - pts_b[np.newaxis, :, :]` sinh ra một mảng hiệu số 3 chiều có kích thước `(2, 2, 2)`. Cần hiểu rằng dù các mảng đầu vào không bị nhân bản trong bộ nhớ trước khi trừ, phép toán trừ mảng này bắt buộc phải cấp phát bộ nhớ mới cho mảng kết quả có kích thước $N \times M \times D$.

Tiếp theo, thao tác bình phương phần tử `diff**2`, tính tổng theo trục tọa độ cuối cùng `np.sum(..., axis=-1)` và lấy căn bậc hai `np.sqrt()` cho ra ma trận khoảng cách kích thước `(2, 2)`. Bảng kết quả hiển thị khoảng cách từ điểm `(0, 0)` đến `(1, 1)` là 1.41 và đến `(0, 0)` là 0.0, trong khi điểm `(3, 4)` cách `(0, 0)` một khoảng bằng 5.0. Bình phương `diff**2` cũng tạo một mảng trung gian. Khi N và M lớn, cần cân nhắc tính theo từng khối vì broadcasting không làm biến mất chi phí bộ nhớ của đầu ra.

:::

<!-- /worked-example -->

## 4. Phương thức của ufunc và Phân biệt hàm vector hóa

Hàm phổ quát (`ufunc`) là hàm thực hiện các phép toán theo từng phần tử được viết và biên dịch sẵn bằng ngôn ngữ C. Ngoài việc gọi trực tiếp `np.add(a, b)`, các ufunc hai ngôi còn sở hữu các phương thức đặc biệt mạnh mẽ:

### Các phương thức thể hiện của ufunc

1. **`reduce`**: Áp dụng toán tử dồn từ đầu đến cuối mảng:
   `np.add.reduce(arr)` tương đương với `arr.sum()`.
2. **`accumulate`**: Giữ lại các kết quả trung gian, tạo mảng tổng tích lũy:
   `np.add.accumulate([1, 2, 3, 4])` cho kết quả `[1, 3, 6, 10]`.
3. **`reduceat`**: Thực hiện thu gọn theo từng đoạn chỉ mục quy định:
   `np.add.reduceat([1, 2, 3, 4], [0, 2])` sẽ tính tổng cho đoạn từ vị trí 0 đến trước 2, và từ vị trí 2 đến hết, cho kết quả `[3, 7]`.
4. **`outer`**: Áp dụng toán tử lên mọi cặp phần tử khả dĩ giữa hai mảng:
   `np.multiply.outer([1, 2], [10, 20])` tạo bảng cửu chương kích thước $(2, 2)$.

```python
u_day = np.array([1, 2, 3, 4, 5])

print("Tích lũy dồn (accumulate):", np.add.accumulate(u_day))
print("Tích ngoài (outer):\n", np.multiply.outer(np.array([1, 2]), np.array([10, 20])))
```

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-6 -->

::: example Tính toán thu gọn từng đoạn với phương thức reduceat của ufunc

Khi cần tính tổng hoặc áp dụng phép toán thu gọn trên các đoạn chỉ số liên tiếp, phương thức reduceat của các ufunc hai ngôi thực hiện phép dồn trên từng khoảng chỉ mục được xác định.

```python
import numpy as np
import pandas as pd

vals = np.array([10, 20, 30, 40, 50, 60])
indices = [0, 2, 4]

# reduceat tính tổng dồn trên các khoảng [0:2], [2:4], [4:]
tong_doan = np.add.reduceat(vals, indices)

bang_kq = pd.DataFrame({
    "doan": ["0-1", "2-3", "4-5"],
    "tong": tong_doan,
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| doan | tong |
| --- | --- |
| 0-1 | 30 |
| 2-3 | 70 |
| 4-5 | 110 |

</div>

Các hàm phổ quát hai ngôi trong NumPy như `np.add` hoặc `np.maximum` sở hữu các phương thức riêng hỗ trợ các bài toán thu gọn dữ liệu. Trong khi phương thức `reduce` áp dụng phép toán dồn trên toàn bộ mảng, phương thức `reduceat` thực hiện thao tác này trên từng phân đoạn chỉ số được chỉ định bởi một mảng mốc.

Lệnh `np.add.reduceat(vals, [0, 2, 4])` chia mảng thành các phân đoạn tương ứng: Phân đoạn thứ nhất tính từ chỉ số 0 đến trước chỉ số 2 (tổng là 10 + 20 = 30), phân đoạn thứ hai tính từ chỉ số 2 đến trước chỉ số 4 (tổng là 30 + 40 = 70), và phân đoạn cuối tính từ chỉ số 4 đến hết mảng (tổng là 50 + 60 = 110). Bảng kết quả trả về đúng ba giá trị tương ứng cho ba đoạn.

Nếu hai mốc liên tiếp thỏa `indices[i] >= indices[i + 1]`, kết quả đoạn đó là `vals[indices[i]]`, không phải tổng của một lát cắt rỗng. Đoạn cuối vẫn được tính từ mốc cuối đến hết mảng. Vì vậy, danh sách mốc lặp hoặc giảm có cách diễn giải riêng, không giống việc bỏ qua những đoạn đó.

:::

<!-- /worked-example -->

### Phân biệt bản chất: `np.vectorize` / `frompyfunc` so với ufunc biên dịch sẵn

Cần phân biệt rõ ràng giữa hai cơ chế thực thi:
- **Không có cam kết về tốc độ**: `np.vectorize` và `np.frompyfunc` hoàn toàn không đưa ra cam kết nào về việc tăng tốc độ thực thi so với vòng lặp Python thông thường. Chúng chỉ là các lớp vỏ bọc tiện ích cú pháp (syntactic sugar) giúp hàm Python nhận đầu vào mảng và áp dụng quy tắc broadcasting.
- **Thực thi trên đối tượng so với ufunc số học**: Một ufunc tích hợp sẵn trong C (như `np.add`, `np.exp`) thao tác trực tiếp trên bộ đệm số nguyên thủy (`float64`, `int32`) bằng mã máy tối ưu hóa. Ngược lại, `np.vectorize` và `np.frompyfunc` thực hiện vòng lặp qua từng đối tượng Python (object execution), liên tục thực hiện đóng gói và mở gói đối tượng (boxing/unboxing) qua CPython C-API. Để đạt được tốc độ mã máy cho các hàm tính toán số học tùy biến, giải pháp là biên dịch hàm bằng công cụ JIT như Numba.

```python
def phep_tinh_rieng(x, y):
    return x * 2 + y

# frompyfunc nhận (hàm, số đầu vào, số đầu ra)
uf_rieng = np.frompyfunc(phep_tinh_rieng, 2, 1)
print("Kết quả frompyfunc:", uf_rieng([1, 2], [10, 20]))
```

---

## 5. Mảng cấu trúc (Structured Arrays) và Mảng bản ghi (Record Arrays)

Trong NumPy, mọi mảng `ndarray` (kể cả mảng cấu trúc) đều sở hữu **duy nhất một kiểu dữ liệu chung** (`arr.dtype`). Với **mảng cấu trúc (Structured array)**, kiểu dữ liệu chung này là một **kiểu phức hợp (Compound dtype)**: Một cấu trúc bản ghi quy định tên trường, kiểu dữ liệu của từng trường con và độ lệch byte (offset) trong từng phần tử.

Mỗi phần tử trong mảng cấu trúc là một bản ghi nhị phân có cùng kích thước byte (itemsize) và cùng tuân theo kiểu phức hợp đó, được lưu trữ nối tiếp nhau trong khối bộ nhớ liên tục.

### Định nghĩa kiểu dữ liệu phức hợp

Mỗi trường trong cấu trúc được định nghĩa bằng một tuple gồm tên trường và mã kiểu dữ liệu:
- `'i4'`: Số nguyên 32-bit (4 byte).
- `'f8'`: Số thực dấu phẩy động 64-bit (8 byte).
- `'U20'`: Chuỗi Unicode tối đa 20 ký tự.

```python
kieu_san_pham = np.dtype([
    ("id", "i4"),
    ("ten", "U20"),
    ("gia", "f8"),
    ("toa_do", "f8", (2,)) # Trường đa chiều chứa cặp tọa độ (x, y)
])

# Khởi tạo mảng cấu trúc
kho_hang = np.array([
    (101, "Ban phim", 45.5, (10.5, 20.0)),
    (102, "Chuot quang", 25.0, (12.0, 18.5))
], dtype=kieu_san_pham)

print("Mảng cấu trúc kho hàng:\n", kho_hang)
print("Cột giá sản phẩm:", kho_hang["gia"])
print("Tọa độ của sản phẩm đầu tiên:", kho_hang["toa_do"][0])
```

### Mảng bản ghi (`np.recarray`)

Mảng bản ghi là một lớp mở rộng cho phép người dùng truy cập các trường bằng cú pháp thuộc tính `kho_hang_rec.gia` thay vì cú pháp chỉ mục `kho_hang["gia"]`:

```python
kho_hang_rec = kho_hang.view(np.recarray)
print("Truy cập theo thuộc tính:", kho_hang_rec.ten)
```

Mảng cấu trúc là công cụ vô giá khi cần đọc và ghi trực tiếp các cấu trúc dữ liệu nhị phân từ tệp C hoặc luồng mạng mà không phải chịu chi phí tạo các đối tượng Python cồng kềnh.

---

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-7 -->

::: example Chuyển đổi mảng cấu trúc sang mảng bản ghi để truy cập trường bằng thuộc tính

Mảng cấu trúc lưu trữ dữ liệu nhị phân nhiều trường nhưng yêu cầu truy cập bằng chuỗi tên trường. Khung nhìn np.recarray cho phép đọc và ghi dữ liệu trực tiếp thông qua cú pháp thuộc tính mà không sao chép khối nhớ đệm.

```python
import numpy as np
import pandas as pd

# Định nghĩa kiểu phức hợp gồm định danh id và điểm số
dt_rec = np.dtype([("id", "i4"), ("diem", "f8")])
arr_struct = np.array([(1, 8.5), (2, 9.0), (3, 7.5)], dtype=dt_rec)

# Chuyển đổi thành mảng bản ghi qua khung nhìn
rec = arr_struct.view(np.recarray)

# Truy cập và chỉnh sửa trực tiếp bằng cú pháp thuộc tính
rec.diem = rec.diem + 0.5

bang_kq = pd.DataFrame({
    "id": rec.id,
    "diem_moi": rec.diem,
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| id | diem&#95;moi |
| --- | --- |
| 1.0 | 9.0 |
| 2.0 | 9.5 |
| 3.0 | 8.0 |

</div>

Mảng cấu trúc (Structured Array) trong NumPy cho phép tổ chức dữ liệu nhị phân gồm nhiều trường có kiểu dữ liệu khác nhau trong cùng một bản ghi. Tuy nhiên, việc truy xuất dữ liệu thông qua chuỗi khóa như `arr_struct["diem"]` có thể làm câu lệnh trở nên dài dòng khi kết hợp trong các biểu thức số học phức tạp.

Lớp `np.recarray` cung cấp giao diện mở rộng cho phép người dùng truy cập các trường dữ liệu bằng cú pháp thuộc tính dạng `rec.diem`. Lời gọi `arr_struct.view(np.recarray)` tạo ra một khung nhìn mới trỏ chung vào cùng khối nhớ đệm của mảng cấu trúc ban đầu, giúp việc đọc và ghi giá trị diễn ra trực tiếp trên cùng dữ liệu mà không cần tạo bản sao.

Khi thực hiện phép gán `rec.diem = rec.diem + 0.5`, dữ liệu trên mảng gốc được cập nhật đồng thời. Bảng kết quả xác nhận các điểm số mới lần lượt là 9.0, 9.5 và 8.0 tương ứng với các mã định danh. Cú pháp thuộc tính của mảng bản ghi mang lại sự thuận tiện khi lập trình mà vẫn duy trì khả năng tính toán số học trên khối nhớ nhị phân của NumPy.

:::

<!-- /worked-example -->

## 6. Các thuật toán sắp xếp chuyên sâu trong NumPy

Sắp xếp dữ liệu là bài toán nền tảng trong mọi hệ thống xử lý thông tin. NumPy hỗ trợ cả hai phương thức: Sắp xếp tại chỗ (`arr.sort()`) và sắp xếp gián tiếp trả về chỉ mục.

### Sắp xếp gián tiếp: `argsort` và `lexsort`

- `np.argsort`: Trả về mảng các chỉ mục sắp xếp theo thứ tự tăng dần.
- `np.lexsort`: Sắp xếp từ điển (Lexicographical sort) theo nhiều khóa ưu tiên.

**Quy tắc tối quan trọng của `lexsort`**: Khóa cuối cùng trong tuple truyền vào mới là **khóa sắp xếp ưu tiên chính**, trong khi khóa đầu tiên là khóa phụ:

```python
ho = np.array(["Tran", "Nguyen", "Le", "Nguyen"])
ten = np.array(["An", "Binh", "An", "An"])

# Sắp xếp ưu tiên theo Tên trước, nếu trùng tên thì xét đến Họ
# Do đó, 'ten' phải được đặt ở vị trí CUỐI CÙNG trong tuple!
chi_muc_sap_xep = np.lexsort((ho, ten))

print("Danh sách sau khi sắp xếp chuẩn mực:")
for i in chi_muc_sap_xep:
    print(f"- {ho[i]} {ten[i]}")
```

### Phân hoạch từng phần với `np.partition`

Trong nhiều bài toán thực tế, ta chỉ cần tìm ra $k$ phần tử nhỏ nhất (hoặc lớn nhất) trong một mảng triệu phần tử (ví dụ: Thuật toán $k$-láng giềng gần nhất - $k$-NN). Việc sắp xếp toàn bộ mảng bằng Quicksort hay Mergesort sẽ tốn chi phí $O(n \log n)$.

Thuật toán `np.partition` giải quyết bài toán này với độ phức tạp tuyến tính **$O(n)$**:
Nó sắp đặt mảng sao cho phần tử tại vị trí $k$ nằm đúng vị trí của nó nếu mảng được sắp xếp, toàn bộ các phần tử nhỏ hơn nó nằm ở phía trước, và toàn bộ các phần tử lớn hơn nó nằm ở phía sau (các phần tử trong từng vế không cần có thứ tự nội bộ):

```python
day_so = np.array([34, 12, 89, 5, 23, 71, 18, 45])

# Phân hoạch tìm 3 phần tử nhỏ nhất (vị trí k = 3)
phan_hoach = np.partition(day_so, 3)
print("Mảng sau phân hoạch tại k=3:", phan_hoach)
print("Ba phần tử nhỏ nhất là:", phan_hoach[:3]) # [5, 12, 18]
```

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-8 -->

::: example Phân hoạch mảng tại vị trí k với np.partition

Khi chỉ cần tìm k phần tử nhỏ nhất mà không yêu cầu sắp xếp toàn bộ mảng, hàm np.partition sắp xếp lại dữ liệu sao cho phần tử tại vị trí chỉ số k đứng đúng vị trí phân hoạch, tiết kiệm thời gian tính toán so với sắp xếp toàn phần.

```python
import numpy as np
import pandas as pd

day_so = np.array([45, 12, 89, 5, 23, 71, 18, 90])

# Phân hoạch tìm 3 phần tử nhỏ nhất (vị trí k = 3)
part = np.partition(day_so, 3)

bang_kq = pd.DataFrame([{
    "k3_nho_nhat": str(np.sort(part[:3]).tolist()),
    "phan_tu_tai_k": int(part[3]),
    "phan_con_lai": str(np.sort(part[4:]).tolist()),
}])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| k3&#95;nho&#95;nhat | phan&#95;tu&#95;tai&#95;k | phan&#95;con&#95;lai |
| --- | --- | --- |
| &#91;5, 12, 18&#93; | 23 | &#91;45, 71, 89, 90&#93; |

</div>

Các thuật toán sắp xếp toàn bộ mảng như Quicksort thường có độ phức tạp thời gian trung bình là $O(n \log n)$. Trong nhiều bài toán thực tế như tìm kiếm $k$ láng giềng gần nhất, người phân tích chỉ cần xác định nhóm $k$ phần tử nhỏ nhất mà không cần quan tâm đến trật tự nội bộ của toàn bộ các phần tử còn lại trong mảng.

Hàm `np.partition` nhận tham số `kth` dựa trên chỉ số bắt đầu từ 0 (0-based index). Hàm sắp đặt lại các phần tử sao cho phần tử tại vị trí `kth` nhận đúng giá trị mà nó sẽ có nếu toàn bộ mảng được sắp xếp thứ tự hoàn chỉnh. Toàn bộ các phần tử đứng trước vị trí này đều nhỏ hơn hoặc bằng nó, và toàn bộ các phần tử đứng sau vị trí này đều lớn hơn hoặc bằng nó.

Trong ví dụ với mảng ban đầu, lời gọi `np.partition(day_so, 3)` đưa ba phần tử nhỏ nhất là 5, 12 và 18 về các vị trí đầu mảng trước chỉ số 3. Phần tử tại vị trí chỉ số 3 nhận giá trị 23, và phần còn lại chứa các số lớn hơn gồm 45, 71, 89, 90. Các phần tử trong từng phía không bắt buộc phải theo thứ tự sắp xếp nội bộ, phản ánh đúng cơ chế phân hoạch từng phần của thuật toán.

:::

<!-- /worked-example -->

### Tìm kiếm nhị phân với `np.searchsorted`

Khi một mảng đã được sắp xếp tăng dần, `np.searchsorted(arr, gia_tri)` sẽ thực hiện tìm kiếm nhị phân với độ phức tạp **$O(\log n)$** để trả về vị trí chỉ mục mà tại đó giá trị có thể được chèn vào mà vẫn bảo toàn thứ tự:

```python
moc_nguong = np.array([10, 20, 30, 40, 50])
diem_so = np.array([5, 25, 45, 60])

vi_tri_chen = np.searchsorted(moc_nguong, diem_so)
print("Vị trí chèn tương ứng:", vi_tri_chen) # [0, 2, 4, 5]
```

Phương thức này chính là động cơ tính toán nền tảng phía sau hàm phân khoảng `pd.cut` và tính phân vị trong pandas.

---

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-9 -->

::: example Tìm vị trí phân nhóm nhị phân với np.searchsorted

Khi phân loại các giá trị đo lường liên tục vào các ngưỡng định mức đã sắp xếp, hàm np.searchsorted áp dụng thuật toán tìm kiếm nhị phân trên mảng ngưỡng để trả về chỉ số nhóm tương ứng của từng phần tử.

```python
import numpy as np
import pandas as pd

# Mảng các mốc ngưỡng điểm đã sắp xếp tăng dần
moc_diem = np.array([5.0, 6.5, 8.0, 9.0])
diem_thi = np.array([4.5, 5.0, 5.5, 7.2, 8.0, 8.5, 9.5])

# Tìm vị trí nhóm theo quy tắc nửa mở nửa đóng
nhom_idx = np.searchsorted(moc_diem, diem_thi, side="right")

bang_kq = pd.DataFrame({
    "diem": diem_thi,
    "nhom_idx": nhom_idx,
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| diem | nhom&#95;idx |
| --- | --- |
| 4.5 | 0.0 |
| 5.0 | 1.0 |
| 5.5 | 1.0 |
| 7.2 | 2.0 |
| 8.0 | 3.0 |
| 8.5 | 3.0 |
| 9.5 | 4.0 |

</div>

Phân nhóm dữ liệu liên tục vào các khoảng định mức là tác vụ quen thuộc trong xử lý số liệu. Nếu duyệt tuần tự từng phần tử qua các mốc ngưỡng bằng vòng lặp, chi phí thời gian sẽ tăng tuyến tính theo số lượng ngưỡng. Hàm `np.searchsorted` tận dụng trật tự tăng dần của mảng ngưỡng để xác định vị trí bằng thuật toán tìm kiếm nhị phân với độ phức tạp $O(\log M)$.

Với `side="right"`, chỉ số trả về là vị trí chèn sau những ngưỡng bằng giá trị cần xét. Vì thế, 5.0 thuộc nhóm 1 và 8.0 thuộc nhóm 3. Khi dùng các ngưỡng để phân nhóm như ở đây, khoảng giữa hai ngưỡng nhận biên trái và bỏ biên phải.

Bảng kết quả minh họa cụ thể sự phân loại này: Giá trị 4.5 nhỏ hơn mốc đầu tiên 5.0 nên nhận chỉ số nhóm 0, giá trị 5.5 rơi vào khoảng giữa 5.0 và 6.5 nên nhận nhóm 1, và giá trị 9.5 vượt qua mốc cao nhất 9.0 nên nhận nhóm 4. Hàm này là cơ chế tính toán nền tảng cho nhiều phép toán phân khoảng và tính hàm phân phối trong các thư viện khoa học dữ liệu.

:::

<!-- /worked-example -->

## 7. Tăng tốc độ tính toán số học với Numba (Tùy chọn bổ trợ / Optional)

Lưu ý: Numba là một thư viện bổ trợ độc lập (cài đặt ngoài, không thuộc gói phân phối chuẩn của NumPy). Khi một thuật toán số học không thể biểu diễn bằng các hàm vector hóa có sẵn của NumPy (chẳng hạn các vòng lặp đệ quy phụ thuộc trạng thái bước trước), Numba cung cấp giải pháp biên dịch JIT trực tiếp sang mã máy tối ưu hóa cao mà không cần viết mã C/C++.

### Biên dịch JIT ở chế độ `nopython=True`

Chế độ `@numba.njit` (tương đương `@numba.jit(nopython=True)`) ép buộc Numba phải biên dịch toàn bộ hàm thành mã máy thuần túy mà không nhờ tới môi trường thông dịch Python (Python C-API). Nếu hàm chứa cú pháp đối tượng không thể tối ưu hóa, Numba sẽ ném lỗi thay vì âm thầm rơi về chế độ thông dịch chậm:

```python
import numba

@numba.njit
def tinh_tong_numba(mang):
    tong = 0.0
    for i in range(len(mang)):
        tong += mang[i]
    return tong

du_lieu_lon = np.random.normal(size=1_000_000)
ket_qua = tinh_tong_numba(du_lieu_lon)
print("Tổng tính bằng Numba:", ket_qua)
```

### Tạo ufunc biên dịch nhanh với `@numba.vectorize`

Khác với `np.vectorize` của NumPy vốn chỉ lặp qua từng đối tượng Python và chịu chi phí đóng/mở gói (boxing overhead), decorator `@numba.vectorize` của Numba thực sự biên dịch hàm Python thành một ufunc số học thuần túy thao tác trực tiếp trên các khối số thô ở cấp độ mã máy C:

```python
@numba.vectorize(["float64(float64, float64)"])
def phep_nhan_cong_numba(x, y):
    return x * 2.5 + y

a_mang = np.ones(1000)
b_mang = np.ones(1000) * 5
print("Kết quả ufunc Numba:", phep_nhan_cong_numba(a_mang, b_mang)[0]) # 7.5
```

---

## 8. Tệp ánh xạ bộ nhớ (`np.memmap`) và tối ưu hóa tính liên tục

### Tệp ánh xạ bộ nhớ (`np.memmap`)

Khi tập dữ liệu mảng có dung lượng lớn vượt quá dung lượng bộ nhớ RAM vật lý của máy tính, việc gọi `np.load()` có thể dẫn đến lỗi tràn bộ nhớ (Out Of Memory - OOM).

Đối tượng `np.memmap` giải quyết vấn đề truy cập này bằng cách sử dụng cơ chế **bộ nhớ ảo (Virtual Memory)** của hệ điều hành: Mảng được lưu trực tiếp trên ổ đĩa cứng, và hệ điều hành chỉ nạp những trang bộ nhớ (Memory Pages) thực sự đang được đọc hoặc ghi vào RAM.

```python
import tempfile
import os

# Tạo mảng memmap tạm thời có kích thước (1000, 1000) kiểu float64 (~8MB)
with tempfile.NamedTemporaryFile(delete=False) as f_tam:
    ten_tep = f_tam.name

try:
    mmap_arr = np.memmap(
        ten_tep,
        dtype="float64",
        mode="w+",
        shape=(1000, 1000)
    )
    # Ghi dữ liệu trực tiếp lên đĩa thông qua cú pháp mảng
    mmap_arr[0, :5] = [1.1, 2.2, 3.3, 4.4, 5.5]
    mmap_arr.flush() # Đẩy toàn bộ thay đổi xuống đĩa cứng

    print("Đọc dữ liệu từ memmap:", mmap_arr[0, :5])
finally:
    # Dọn dẹp tài nguyên
    del mmap_arr
    if os.path.exists(ten_tep):
        os.remove(ten_tep)
```

**Giới hạn tiêu thụ RAM của các thao tác tiếp theo**: Cần lưu ý rằng `np.memmap` **không tự động bảo đảm mọi phép toán tiếp theo đều tốn ít RAM**. Nếu ta thực hiện các phép toán sinh ra mảng mới (chẳng hạn `mmap_arr + 1`, `mmap_arr * 2`, hoặc `mmap_arr.sum(axis=0)`), NumPy sẽ cấp phát một mảng `ndarray` thông thường trên bộ nhớ RAM vật lý để chứa kết quả. Khi dữ liệu gốc có dung lượng hàng chục Gigabyte, điều này sẽ lập tức gây ra lỗi tràn RAM (OOM). Do đó, khi làm việc với `memmap`, các phép tính phải được chia nhỏ thành từng khối (chunking), ghi trực tiếp vào một tệp memmap đích khác, hoặc chỉ thực hiện các phép tích lũy cục bộ.

<!-- worked-example phu-luc-a-numpy-nang-cao-worked-10 -->

::: example Đọc và cập nhật dữ liệu mảng trên đĩa bằng np.memmap và tempfile

Khi xử lý các ma trận có kích thước lớn, lớp np.memmap cho phép ánh xạ tệp nhị phân trên đĩa vào không gian địa chỉ bộ nhớ ảo của tiến trình, hỗ trợ nạp dữ liệu theo từng trang bộ nhớ khi truy cập thực tế.

```python
import os
import tempfile
import numpy as np
import pandas as pd

# Tạo tệp tạm thời an toàn cho môi trường đa nền tảng
with tempfile.NamedTemporaryFile(delete=False) as tmp:
    tep_tam = tmp.name

try:
    # Khởi tạo mảng memmap 3x3 kiểu float64 trực tiếp trên tệp đĩa
    mm = np.memmap(tep_tam, dtype="float64", mode="w+", shape=(3, 3))
    mm[:] = np.eye(3) * 5.0
    mm.flush()  # Đẩy toàn bộ thay đổi xuống đĩa

    # Đọc lại dữ liệu đường chéo chính từ tệp
    diag = np.diag(mm).copy()
    del mm  # Đóng kết nối tệp memmap

    bang_kq = pd.DataFrame({"duong_cheo": diag})
    print(bang_kq)
finally:
    if os.path.exists(tep_tam):
        os.remove(tep_tam)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| duong&#95;cheo |
| --- |
| 5.0 |
| 5.0 |
| 5.0 |

</div>

Khi mảng dữ liệu có dung lượng lớn, việc đọc toàn bộ tệp vào bộ nhớ RAM có thể làm cạn kiệt tài nguyên hệ thống. Lớp `np.memmap` cung cấp giải pháp làm việc với dữ liệu trên đĩa thông qua cơ chế ánh xạ bộ nhớ ảo của hệ điều hành, cho phép chỉ nạp các trang bộ nhớ thực sự được đọc hoặc ghi thay vì nạp toàn bộ mảng cùng một lúc.

`mode="w+"` tạo hoặc ghi đè tệp, nên ví dụ chỉ dùng một tệp tạm tự tạo. `flush()` yêu cầu ghi các thay đổi của ánh xạ về tệp, không phải lời bảo đảm riêng về độ bền vật lý của phần cứng. `del mm` bỏ tham chiếu hiện tại, nhưng ánh xạ có thể còn tồn tại nếu các view khác vẫn giữ nó.

Để làm việc an toàn với các tệp định dạng `.npy` lớn trên đĩa mà không làm tràn bộ nhớ, người phân tích cũng có thể sử dụng hàm `np.load` với tham số `mmap_mode="r"`. Bảng kết quả hiển thị dữ liệu đường chéo chính với giá trị 5.0 được trích xuất từ tệp tạm thời, chứng minh khả năng đọc ghi dữ liệu có kiểm soát thông qua cơ chế ánh xạ bộ nhớ.

:::

<!-- /worked-example -->

### Tối ưu hóa tính liên tục của bộ nhớ và Dòng bộ nhớ đệm (Cache Lines)

Phần cứng CPU hiện đại không đọc dữ liệu từ RAM theo từng byte đơn lẻ, mà nạp theo từng **dòng bộ nhớ đệm (Cache Line)** có kích thước 64 byte.

- Khi một mảng được xếp theo thứ tự C (`c_contiguous`), các phần tử trên cùng một hàng nằm liền kề nhau trong bộ nhớ. Khi CPU đọc phần tử `arr[i, 0]`, toàn bộ các phần tử `arr[i, 1]`, `arr[i, 2]` kế tiếp đã được nạp sẵn vào bộ nhớ đệm L1/L2 của CPU. Vì vậy, duyệt mảng theo từng hàng sẽ đạt tốc độ tối đa nhờ tận dụng hiện tượng trúng bộ nhớ đệm (Cache Hit).
- Trái lại, nếu duyệt theo từng cột trên một mảng C-contiguous lớn, mỗi bước nhảy sẽ cách nhau hàng nghìn byte (vượt kích thước một Cache Line), khiến CPU liên tục bị trượt bộ nhớ đệm (Cache Miss) và phải chờ nạp lại dữ liệu từ thanh RAM chậm chạp.

Truy cập các ô gần nhau trong bộ nhớ có thể giúp dùng bộ nhớ đệm hiệu quả hơn. Tuy nhiên, thứ tự duyệt còn phải phù hợp với thuật toán và thư viện được gọi. Hãy đo toàn bộ nhiệm vụ thay vì suy hiệu năng chỉ từ một giá trị stride.

---

## 10. Tổng kết

- Bộ nhớ mảng: Đọc đồng thời `shape`, `strides`, `dtype` và điều kiện dùng chung vùng dữ liệu.
- Kiểu dữ liệu: Phân biệt kiểu vô hướng kế thừa `np.generic` với đối tượng `np.dtype` mô tả cách lưu và diễn giải phần tử.
- Sao chép: `ravel` có thể dùng lại dữ liệu khi bố trí phù hợp. `flatten` tạo vùng chứa mới, nhưng với dtype object vẫn phải phân biệt bản sao nông của tham chiếu.
- Broadcasting: Có thể dùng lại đầu vào mà không nhân bản dữ liệu chỉ để lặp theo trục. Kết quả hoặc biểu thức trung gian vẫn có thể cần thêm RAM.
- Ufunc: Chọn `reduce`, `accumulate`, `outer` theo đầu ra cần dùng, không mặc định mọi dtype đều có cùng cơ chế thực thi.
- Biên dịch: `np.vectorize` không cam kết tăng tốc. Numba hữu ích với dạng hàm và kiểu dữ liệu được hỗ trợ, cần tách thời gian biên dịch khỏi thời gian chạy.
- Mảng cấu trúc: Một dtype phức hợp chung có thể chứa các trường khác kiểu. Cách bố trí và yêu cầu truy cập quyết định công cụ phù hợp.
- Sắp xếp: `argsort` trả vị trí, `lexsort` nhận khóa chính ở cuối, còn `partition` không sắp hết các phần tử của từng phía.
- Tệp lớn: `memmap` hỗ trợ truy cập theo trang, nhưng cần kiểm soát các phép toán trung gian để giữ giới hạn bộ nhớ.

## Tài liệu tham khảo

1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Appendix A: Advanced NumPy. URL: [https://wesmckinney.com/book/advanced-numpy](https://wesmckinney.com/book/advanced-numpy).
2. Tài liệu chính thức NumPy: *NumPy Reference - Internals, Indexing, and C-API*. URL: [https://numpy.org/doc/stable/reference/internals.html](https://numpy.org/doc/stable/reference/internals.html).
3. Tài liệu chính thức Numba: *Compiling Python code with JIT*. URL: [https://numba.readthedocs.io/](https://numba.readthedocs.io/).
4. Travis Oliphant, *Guide to NumPy*, Continuum Analytics. Chuyên khảo kinh điển về cấu trúc khối bộ nhớ ndarray và hệ thống ufunc.

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 9. Bài tập thực hành

::: exercise Bài tập 1: Phân biệt View và Copy khi biến đổi mảng
Cho mảng hai chiều sau:

```python
A = np.arange(12).reshape(3, 4)
```

1. Tạo mảng $B$ bằng cách chuyển vị $A$ (`B = A.T`). Kiểm tra xem $A$ và $B$ có dùng chung vùng nhớ hay không bằng `np.shares_memory`. Thay đổi giá trị tại $B[0, 0] = 99$ thì $A[0, 0]$ có biến đổi theo không?
2. So sánh tính chất chia sẻ bộ nhớ giữa `A.ravel()` và `A.flatten()`.
:::

::: solution Lời giải chi tiết
Mã nguồn thực hiện:

```python
import numpy as np

A = np.arange(12).reshape(3, 4)

# 1. Chuyển vị ma trận
B = A.T
print("B và A có chia sẻ bộ nhớ không?", np.shares_memory(A, B)) # True

B[0, 0] = 99
print("Giá trị A[0, 0] sau khi đổi B[0, 0]:", A[0, 0]) # 99

# 2. Phẳng hóa mảng
r = A.ravel()
f = A.flatten()

print("ravel có chia sẻ bộ nhớ với A không?", np.shares_memory(A, r))   # True
print("flatten có chia sẻ bộ nhớ với A không?", np.shares_memory(A, f)) # False
```

Giải thích chi tiết:
- Phép chuyển vị `A.T` chỉ đơn thuần hoán đổi hai số trong bộ `strides` từ `(16, 4)` thành `(4, 16)`, hoàn toàn không sao chép dữ liệu. Do đó $B$ là một View của $A$ và việc sửa $B$ sẽ làm thay đổi trực tiếp $A$.
- `ravel()` trả về một View khi các bước nhảy (`strides`) của mảng tương thích với thứ tự duyệt được chọn (như thứ tự C trên mảng C-contiguous). Nếu thứ tự duyệt không tương thích với bố cục bước nhảy hiện tại, `ravel()` sẽ bắt buộc tạo một bản sao. Trong khi đó, `flatten()` luôn luôn cấp phát một vùng nhớ mới và sao chép toàn bộ dữ liệu, bảo đảm tính độc lập tuyệt đối nhưng tiêu tốn thêm bộ nhớ RAM.
:::

::: exercise Bài tập 2: Sắp xếp đa tiêu chí và định vị nhị phân
Cho danh sách điểm thi của sinh viên gồm ba mảng: `ma_lop` (mã lớp), `diem_so` (điểm trung bình), và `id_sv` (mã định danh).
1. Sử dụng `np.lexsort` để sắp xếp danh sách sinh viên với tiêu chí ưu tiên cao nhất là `ma_lop` (tăng dần), và tiêu chí phụ khi trùng mã lớp là `diem_so` (tăng dần).
2. Cho mảng mốc học bổng đã sắp xếp `nguong = np.array([7.0, 8.0, 9.0])`. Hãy dùng `np.searchsorted` để phân loại một danh sách điểm mới vào các hạng học bổng tương ứng trong $O(\log n)$.
:::

::: solution Lời giải chi tiết
Mã nguồn thực hiện:

```python
import numpy as np

ma_lop = np.array(["K68A", "K68B", "K68A", "K68B", "K68A"])
diem_so = np.array([8.5, 7.0, 9.0, 8.0, 7.5])
id_sv = np.array([101, 102, 103, 104, 105])

# Trong np.lexsort, khóa ưu tiên chính phải đặt ở CUỐI CÙNG
chi_muc = np.lexsort((diem_so, ma_lop))

print("Danh sách sau sắp xếp đa tiêu chí:")
for i in chi_muc:
    print(f"Lớp: {ma_lop[i]}, Điểm: {diem_so[i]}, ID: {id_sv[i]}")

# Phân loại học bổng bằng searchsorted
nguong = np.array([7.0, 8.0, 9.0])
diem_moi = np.array([6.5, 7.5, 8.5, 9.5])
hang = np.searchsorted(nguong, diem_moi, side="right")

print("Hạng học bổng tương ứng (0: Không đạt, 1: Khá, 2: Giỏi, 3: Xuất sắc):", hang)
# Kết quả: [0, 1, 2, 3]
```
:::

::: exercise Bài tập 3: So sánh hiệu năng tính toán giữa Python thuần, `np.vectorize` và Numba
Viết hàm tính khoảng cách Euclid giữa hai mảng vector lớn $d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$. So sánh thời gian thực thi giữa hàm viết bằng `np.vectorize` với hàm biên dịch bằng `@numba.njit`.
:::

::: solution Lời giải chi tiết
Mã nguồn thực nghiệm:

```python
import numpy as np
import numba
import time

n = 500_000
x1 = np.random.normal(size=n)
y1 = np.random.normal(size=n)
x2 = np.random.normal(size=n)
y2 = np.random.normal(size=n)

# 1. Tiếp cận bằng np.vectorize
def khoang_cach_py(a, b, c, d):
    return np.sqrt((a - c)**2 + (b - d)**2)

vec_func = np.vectorize(khoang_cach_py)

t0 = time.time()
res_vec = vec_func(x1, y1, x2, y2)
t_vec = time.time() - t0

# 2. Tiếp cận bằng Numba JIT
@numba.njit
def khoang_cach_numba(a, b, c, d):
    ket_qua = np.empty(len(a))
    for i in range(len(a)):
        ket_qua[i] = np.sqrt((a[i] - c[i])**2 + (b[i] - d[i])**2)
    return ket_qua

# Chạy thử lần đầu để Numba biên dịch JIT
_ = khoang_cach_numba(x1[:10], y1[:10], x2[:10], y2[:10])

t1 = time.time()
res_numba = khoang_cach_numba(x1, y1, x2, y2)
t_numba = time.time() - t1

print(f"Thời gian chạy np.vectorize: {t_vec:.4f} giây")
print(f"Thời gian chạy Numba JIT:    {t_numba:.4f} giây")
print(f"Numba nhanh hơn khoảng:      {t_vec / t_numba:.1f} lần!")
```

Kết luận thực nghiệm:
Hàm Numba JIT thường chạy nhanh hơn `np.vectorize` từ 15 đến 30 lần. Điều này chứng minh rằng `np.vectorize` chỉ mang tính chất tiện lợi cú pháp và không thể thay thế việc biên dịch mã máy thực sự khi xử lý dữ liệu quy mô lớn.
:::

---

## Tài liệu tham khảo

1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Appendix A: Advanced NumPy. URL: [https://wesmckinney.com/book/advanced-numpy](https://wesmckinney.com/book/advanced-numpy).
2. Tài liệu chính thức NumPy: *NumPy Reference - Internals, Indexing, and C-API*. URL: [https://numpy.org/doc/stable/reference/internals.html](https://numpy.org/doc/stable/reference/internals.html).
3. Tài liệu chính thức Numba: *Compiling Python code with JIT*. URL: [https://numba.readthedocs.io/](https://numba.readthedocs.io/).
4. Travis Oliphant, *Guide to NumPy*, Continuum Analytics. Chuyên khảo kinh điển về cấu trúc khối bộ nhớ ndarray và hệ thống ufunc.

</div>
