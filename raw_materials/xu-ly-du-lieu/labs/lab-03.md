## Lab 03: NumPy và tư duy vector hóa trong xử lý dữ liệu


Lấy một phần của mảng có thể tạo view hoặc bản sao. Sự khác biệt xuất hiện rõ khi sửa kết quả và quan sát mảng ban đầu. Các bài dùng mảng nhỏ để kiểm tra từng phần tử, bước nhảy bộ nhớ, quy tắc broadcasting và cách lấy mẫu.

Ma trận và các bảng giá trong bộ bài là dữ liệu giả lập. Đơn vị giá của từng bảng được ghi ngay trong đề.

### Khởi tạo dữ liệu dùng chung

Mọi bài tập sử dụng chung ma trận $A$ kích thước 4 hàng $\times$ 3 cột với kiểu số nguyên 64-bit (`np.int64`):

```python
import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)
```


Khi hiển thị trực quan dưới dạng bảng toán học:

$$
A = \begin{bmatrix}
10 & 12 & 11 \\
20 & 21 & 24 \\
30 & 33 & 31 \\
40 & 44 & 42
\end{bmatrix}
$$

---

## Bài 1: Đọc cấu trúc mảng, bước nhảy bộ nhớ và khoảng cách byte

<span id="data-lab-03-01"></span>

::: exercise
**Mục tiêu**: Nắm vững cấu trúc mô tả siêu dữ liệu (metadata) của đối tượng mảng `ndarray`, hiểu rõ quy tắc sắp xếp dữ liệu theo thứ tự hàng (C-contiguous) trong bộ nhớ và cơ chế tính toán độ lệch địa chỉ (byte offset).

**Dữ liệu đầu vào**: Ma trận $A$ kích thước $4 \times 3$, kiểu `np.int64`.

**Thao tác yêu cầu**:
1. Đọc và xác định bốn thuộc tính cấu trúc cơ bản của $A$: Kích thước (`shape`), kích thước mỗi phần tử tính theo byte (`itemsize`), số byte của các phần tử logic trong mảng (`nbytes`), và bước nhảy bộ nhớ (`strides`).
2. Tính khoảng cách địa chỉ tính theo byte (`offset`) từ vị trí bắt đầu của phần tử đầu tiên $A[0, 0]$ đến phần tử $A[3, 1]$ dựa vào chỉ số hàng, chỉ số cột và bước nhảy `strides`.
3. Chuyển đổi ma trận $A$ sang kiểu số nguyên 32-bit (`np.int32`) tạo thành mảng mới $A_{32}$. So sánh dung lượng dữ liệu (`nbytes`) và bước nhảy (`strides`) của $A_{32}$ so với $A$.
4. Đóng gói quy trình trên thành một hàm tái sử dụng `array_layout(matrix: np.ndarray, row: int, col: int) -> dict` tuân thủ đúng quy chuẩn cấu trúc dữ liệu, hỗ trợ ma trận hai chiều bất kỳ.

**Trường hợp biên cần chú ý**:
- Chỉ số `row` và `col` phải nằm trong phạm vi hợp lệ của ma trận ($0 \le \text{row} < \text{nrows}$ và $0 \le \text{col} < \text{ncols}$).
- Không ghi cứng các hằng số kích thước của $A$ vào thân hàm.
:::

::: solution
#### Cách 1: Thao tác tuần tự trực tiếp trên thuộc tính đối tượng ndarray

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np

# 1. Truy xuất các thuộc tính cấu trúc của ma trận A
shape_a = A.shape
byte_moi_so = A.itemsize
byte_du_lieu = A.nbytes
buoc = A.strides

# 2. Tính độ lệch byte của phần tử A[3, 1] từ bước nhảy
hang_can_tim = 3
cot_can_tim = 1
offset = hang_can_tim * buoc[0] + cot_can_tim * buoc[1]

# 3. Tạo mảng với kiểu dữ liệu int32
A32 = A.astype(np.int32)
byte_du_lieu_32 = A32.nbytes
buoc_32 = A32.strides

# Kết thúc lời giải

print(
    {
        "shape": shape_a,
        "itemsize": byte_moi_so,
        "nbytes": byte_du_lieu,
        "strides": buoc,
        "offset": offset,
        "int32_nbytes": byte_du_lieu_32,
        "int32_strides": buoc_32,
    }
)
```

#### Giải thích cách 1

`shape` ghi số phần tử theo từng trục, ở đây là bốn hàng và ba cột. `itemsize` cho biết mỗi số `int64` cần tám byte. Có mười hai phần tử nên `nbytes` bằng `96`. Đây là số byte của các phần tử logic, không bao gồm toàn bộ bộ nhớ dành cho đối tượng Python và thông tin quản lý mảng.

Ma trận được khởi tạo liền theo hàng, nên sang cột kế tiếp cần tám byte và sang hàng kế tiếp cần ba lần tám, tức hai mươi bốn byte. `strides` vì thế là `(24, 8)`. Độ lệch của ô `[3, 1]` bằng ba bước hàng cộng một bước cột, tức `80` byte. `astype(np.int32)` tạo mảng kiểu mới có phần tử bốn byte, nên dung lượng phần tử giảm còn `48` byte. Các giá trị nhỏ trong mẫu chuyển kiểu mà không đổi giá trị.

#### Kết quả cách 1

| Thuộc tính | A (int64) | A32 (int32) |
| --- | --- | --- |
| shape | `(4, 3)` | `(4, 3)` |
| itemsize | 8 byte | 4 byte |
| nbytes | 96 byte | 48 byte |
| strides | `(24, 8)` | `(12, 4)` |

Biến `offset` bằng `80` byte, tính từ vị trí phần tử `A[0, 0]`.

#### Cách 2: Đóng gói hàm chuẩn hóa array_layout với kiểm soát ràng buộc dữ liệu

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np


def array_layout(matrix: np.ndarray, row: int, col: int) -> dict:
    """Đọc cấu trúc bộ nhớ và tính toán độ lệch byte của phần tử chỉ định.

    Tham số:
        matrix: Mảng hai chiều kiểu số nguyên, định dạng bộ nhớ C-contiguous.
        row: Chỉ số hàng hợp lệ, không âm.
        col: Chỉ số cột hợp lệ, không âm.

    Trả về:
        Từ điển chứa shape, itemsize, nbytes, strides, offset và mảng int32.
    """
    if matrix.ndim != 2:
        raise ValueError("Yêu cầu ma trận đầu vào phải có đúng 2 chiều.")
    if not (0 <= row < matrix.shape[0] and 0 <= col < matrix.shape[1]):
        raise IndexError(
            f"Chỉ số ({row}, {col}) vượt quá kích thước ma trận {matrix.shape}."
        )

    # Tính toán độ lệch byte trực tiếp từ bước nhảy
    strides = matrix.strides
    offset = int(row * strides[0] + col * strides[1])

    return {
        "shape": matrix.shape,
        "itemsize": matrix.itemsize,
        "nbytes": matrix.nbytes,
        "strides": strides,
        "offset": offset,
        "int32_array": matrix.astype(np.int32),
    }


print(array_layout(A, 3, 1))

# Kết thúc lời giải
```

#### Giải thích cách 2

`array_layout` nhận ma trận cùng chỉ số hàng, cột cần khảo sát và trả về một từ điển. Kiểm tra `matrix.ndim != 2` từ chối đầu vào không phải bảng hai trục. Điều kiện tiếp theo yêu cầu chỉ số không âm và nhỏ hơn số phần tử ở trục tương ứng, nên chặn truy cập vượt phạm vi trước khi tính địa chỉ.

Hàm đọc trực tiếp `matrix.strides` rồi tính `row * strides[0] + col * strides[1]`. Không ghi cứng số cột hay số byte, vì view hoặc kiểu dữ liệu khác có bước nhảy khác. Mảng `int32_array` được tạo bởi `astype`, còn các trường còn lại mô tả mảng ban đầu. Chuyển sang số nguyên hẹp hơn chỉ bảo toàn giá trị khi các giá trị nằm trong miền biểu diễn của kiểu mới.

#### Kết quả cách 2

| Thuộc tính | A (int64) | A32 (int32) |
| --- | --- | --- |
| shape | `(4, 3)` | `(4, 3)` |
| itemsize | 8 byte | 4 byte |
| nbytes | 96 byte | 48 byte |
| strides | `(24, 8)` | `(12, 4)` |

Trường `offset` trong từ điển bằng `80`. Trường `int32_array` giữ cùng bốn hàng giá trị của A với `dtype=int32`.

#### So sánh hai cách

Cách 1 phơi bày từng phép đọc thuộc tính để đối chiếu bằng tay. Cách 2 nhận chỉ số qua tham số và bổ sung kiểm tra phạm vi. Cả hai đọc cùng thông tin, không phải đo mức sử dụng bộ nhớ của toàn bộ tiến trình.

:::

---

## Bài 2: Lát cắt mảng đa chiều và tính chất view chia sẻ bộ nhớ

<span id="data-lab-03-02"></span>

::: exercise
**Mục tiêu**: Nắm vững cú pháp lát cắt bước nhảy (strided slicing) trên mảng hai chiều, phân biệt cách quản lý vùng nhớ thông qua cơ chế View, và tính toán tọa độ ánh xạ ngược về mảng gốc.

**Dữ liệu đầu vào**: Ma trận $A$ kích thước $4 \times 3$, kiểu `np.int64`.

**Thao tác yêu cầu**:
1. Tạo ma trận con $V$ gồm các hàng chỉ mục 1, 3 và các cột chỉ mục 0, 2 của $A$, bắt buộc sử dụng duy nhất một lát cắt cho mỗi chiều không gian.
2. Dự đoán giá trị các phần tử, kích thước (`shape`), và bước nhảy (`strides`) của $V$.
3. Xác định phần tử $V[1, 1]$ tương ứng với ô nào trong ma trận gốc $A$, và tính khoảng cách byte từ đầu vùng đệm dữ liệu của $A$ đến ô này.
4. Kiểm tra xem $V$ có thực sự dùng chung vùng nhớ với $A$ hay không bằng hàm `np.shares_memory(A, V)` và kiểm tra thuộc tính con trỏ dữ liệu gốc (`base`).
5. Đóng gói thành hàm `slice_view(matrix: np.ndarray) -> dict` tuân thủ đúng quy chuẩn dữ liệu.

**Trường hợp biên cần chú ý**:
- Không được sửa đổi giá trị các phần tử trong $V$.
- Ma trận đầu vào cần có ít nhất 4 hàng và 3 cột để lát cắt bước nhảy hoạt động ổn định.
:::

::: solution
#### Cách 1: Sử dụng cú pháp lát cắt bước nhảy và truy xuất trực tiếp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np

# 1. Tạo lát cắt V với một cú pháp slice cho mỗi chiều
V = A[1::2, 0::2]

# 2. Thu thập siêu dữ liệu của V
shape_v = V.shape
strides_v = V.strides

# 3. Tính độ lệch từ đầu mảng A đến ô V[1, 1] (tức A[3, 2])
hang_goc = 1 + 1 * 2  # Chỉ số 3
cot_goc = 0 + 1 * 2  # Chỉ số 2
offset_v11 = hang_goc * A.strides[0] + cot_goc * A.strides[1]

# 4. Kiểm tra chia sẻ vùng nhớ chung
dung_chung = np.shares_memory(A, V)
dung_chung_base = V.base is A

# Kết thúc lời giải

print("View:", V)
print("Offset:", offset_v11)
print("Shared memory:", dung_chung)
```

#### Giải thích cách 1

Lát cắt `1::2` chọn các hàng bắt đầu từ chỉ số `1`, mỗi lần tăng `2`, nên lấy hàng `1` và `3`. Lát cắt `0::2` tương tự lấy cột `0` và `2`. Kết quả V có hai hàng, hai cột và chứa các giá trị của đúng bốn giao điểm này.

Lát cắt cơ bản tạo view, nên bước hàng của V là hai lần bước hàng A, tức `48` byte. Bước cột là hai lần tám, tức `16` byte. Ô `V[1, 1]` quy ngược về `A[3, 2]`, cách phần tử đầu A một khoảng `88` byte. `np.shares_memory(A, V)` kiểm tra thực sự có vùng nhớ dùng chung. Trên A sở hữu dữ liệu của mẫu, `V.base is A` cũng là `True`, nhưng kiểm tra `base` không đủ cho mọi chuỗi view.

#### Kết quả cách 1

| Hàng của V | Cột 0 | Cột 1 |
| --- | --- | --- |
| 0 | 20 | 24 |
| 1 | 40 | 42 |

| Thuộc tính | Kết quả |
| --- | --- |
| shape_v | `(2, 2)` |
| strides_v | `(48, 16)` |
| offset_v11 | 88 byte từ A[0, 0] |
| dung_chung | `True` |
| dung_chung_base | `True` trên A của mẫu |

#### Cách 2: Đóng gói hàm slice_view kiểm soát ma trận tổng quát

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np


def slice_view(matrix: np.ndarray) -> dict:
    """Trích xuất lát cắt bước nhảy và phân tích siêu dữ liệu chia sẻ bộ nhớ.

    Tham số:
        matrix: Mảng hai chiều kiểu số nguyên, kích thước tối thiểu 4 hàng và 3 cột.

    Trả về:
        Từ điển chứa view, shape, strides, offset_v11 và shares_memory.
    """
    if matrix.ndim != 2:
        raise ValueError("Yêu cầu ma trận đầu vào phải có 2 chiều.")
    if matrix.shape[0] < 4 or matrix.shape[1] < 3:
        raise ValueError(
            f"Kích thước ma trận {matrix.shape} không đủ để cắt hàng [1, 3] và cột [0, 2]."
        )

    # Tạo lát cắt bước nhảy hai chiều
    view = matrix[1::2, 0::2]

    # Tính tọa độ thực tế của view[1, 1] trên ma trận gốc
    orig_row = 1 + 1 * 2
    orig_col = 0 + 1 * 2
    offset_v11 = orig_row * matrix.strides[0] + orig_col * matrix.strides[1]

    return {
        "view": view,
        "shape": view.shape,
        "strides": view.strides,
        "offset_v11": offset_v11,
        "shares_memory": bool(np.shares_memory(matrix, view)),
    }


print(slice_view(A))

# Kết thúc lời giải
```

#### Giải thích cách 2

`slice_view` yêu cầu đầu vào có hai trục, ít nhất bốn hàng và ba cột. Những điều kiện này bảo đảm vị trí `view[1, 1]` tồn tại. Phép cắt vẫn dùng các điểm bắt đầu và bước nhảy cố định của đề, còn độ lệch được tính từ bước nhảy thực tế của mảng truyền vào.

Từ điển trả về gồm chính view và các thuộc tính để kiểm chứng. `bool(np.shares_memory(matrix, view))` chuyển kết quả kiểm tra thành Boolean Python. Hàm không gán giá trị vào view. Nếu nơi gọi sửa một phần tử của `view`, giá trị tại ô tương ứng trong mảng gốc có thể thay đổi vì chúng chia sẻ dữ liệu.

#### Kết quả cách 2

| Hàng của V | Cột 0 | Cột 1 |
| --- | --- | --- |
| 0 | 20 | 24 |
| 1 | 40 | 42 |

| Trường kết quả | Giá trị |
| --- | --- |
| shape | `(2, 2)` |
| strides | `(48, 16)` |
| offset_v11 | 88 |
| shares_memory | `True` |

#### So sánh hai cách

Cách 1 minh họa quan hệ giữa chỉ số và vùng nhớ. Cách 2 đóng gói phép khảo sát với điều kiện đầu vào rõ ràng. Cả hai tạo view, nên không dành một bản sao riêng cho bốn phần tử được chọn.

:::

---

## Bài 3: Phân biệt view và bản sao độc lập khi đột biến dữ liệu

<span id="data-lab-03-03"></span>

::: exercise
**Mục tiêu**: Hiểu rõ ranh giới kỹ thuật giữa phép lập chỉ mục cơ bản (Basic Slicing tạo View) và phép lập chỉ mục nâng cao (Advanced Fancy Indexing tạo Copy), kiểm soát hoàn toàn tác dụng phụ khi gán giá trị (mutation side-effects).

**Dữ liệu đầu vào**: Bản sao độc lập $B = A.\mathrm{copy}()$ của ma trận $A$.

**Thao tác yêu cầu**:
1. Khảo sát hiện tượng đột biến dữ liệu:
   - Tạo $V = B[:, 1:3]$ (sử dụng lát cắt slicing).
   - Tạo $C = B[:, [1, 2]]$ (sử dụng danh sách chỉ mục fancy indexing).
   - Dự đoán và quan sát giá trị hàng đầu tiên $B[0]$ sau lệnh gán $C[0, 0] = -9$.
   - Dự đoán và quan sát giá trị hàng đầu tiên $B[0]$ sau lệnh gán tiếp theo $V[0, 0] = -1$.
   - Giải thích bản chất tại sao hai thao tác trên lại mang lại hành vi khác nhau hoàn toàn.
2. Xây dựng phương pháp trích xuất mảng $D$ chứa cột 1 và 2 của $B$ sao cho mọi thao tác chỉnh sửa trên $D$ hoàn toàn độc lập và không làm biến đổi mảng gốc $B$.
3. Đóng gói hàm `copy_columns(matrix: np.ndarray) -> np.ndarray` bảo đảm tính độc lập bộ nhớ tuyệt đối.

**Trường hợp biên cần chú ý**:
- Mảng đầu vào phải có ít nhất 1 hàng và 3 cột.
- Kiểm tra tính độc lập bộ nhớ bằng `not np.shares_memory(result, matrix)`.
:::

::: solution
#### Cách 1: Thực nghiệm gán giá trị và sao chép tường minh qua copy()

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np

# Khởi tạo bản sao độc lập của A
B = A.copy()

# Tạo View và Fancy Indexing Copy
V = B[:, 1:3]  # View
C = B[:, [1, 2]]  # Copy

# Thao tác 1: Gán trên bản sao C
C[0, 0] = -9
# Kết quả B[0] vẫn giữ nguyên là [10, 12, 11]

# Thao tác 2: Gán trên View V
V[0, 0] = -1
# Kết quả B[0] bị thay đổi thành [10, -1, 11]

# Tạo mảng D độc lập an toàn chứa cột 1 và 2
D = B[:, 1:3].copy()
D[0, 0] = 999
# Giá trị của B hoàn toàn không bị ảnh hưởng bởi D

# Kết thúc lời giải

print("Original:", A)
print("View parent:", B)
print("Fancy-index copy:", C)
print("Explicit copy:", D)
```

#### Giải thích cách 1

`B = A.copy()` tạo vùng dữ liệu riêng trước khi làm thí nghiệm, nên A giữ nguyên. `V = B[:, 1:3]` là lát cắt cơ bản dùng chung dữ liệu với B. `C = B[:, [1, 2]]` dùng danh sách chỉ mục nâng cao, tạo một bản sao các cột được chọn.

Gán `C[0, 0] = -9` chỉ sửa bản sao C, nên hàng đầu B còn `[10, 12, 11]`. Gán tiếp `V[0, 0] = -1` sửa cùng ô dữ liệu với `B[0, 1]`, khiến hàng đầu B thành `[10, -1, 11]`. Cuối cùng `.copy()` trên lát cắt tạo D độc lập. Gán `D[0, 0] = 999` không truyền sang B.

#### Kết quả cách 1

| Thời điểm | B[0] | Giá trị vừa gán |
| --- | --- | --- |
| Sau khi gán C | `[10, 12, 11]` | `C[0, 0] = -9` |
| Sau khi gán V | `[10, -1, 11]` | `V[0, 0] = -1` |
| Sau khi gán D | `[10, -1, 11]` | `D[0, 0] = 999` |

#### Cách 2: Đóng gói hàm copy_columns bảo đảm độc lập bộ nhớ tuyệt đối

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np


def copy_columns(matrix: np.ndarray) -> np.ndarray:
    """Trích xuất cột 1 và 2 của ma trận dưới dạng bản sao bộ nhớ độc lập.

    Tham số:
        matrix: Mảng hai chiều kiểu số bất kỳ, có ít nhất một hàng và ba cột.

    Trả về:
        Mảng con hai chiều gồm cột 1 và 2, hoàn toàn không chia sẻ vùng nhớ với mảng gốc.
    """
    if matrix.ndim != 2:
        raise ValueError("Yêu cầu ma trận đầu vào phải có đúng 2 chiều.")
    if matrix.shape[1] < 3:
        raise ValueError(
            f"Ma trận cần có ít nhất 3 cột, hiện tại có {matrix.shape[1]} cột."
        )

    # Trích xuất lát cắt và thực hiện nhân bản vùng đệm dữ liệu tường minh
    result = matrix[:, 1:3].copy()

    # Xác minh tính toàn vẹn bộ nhớ
    if np.shares_memory(result, matrix):
        raise RuntimeError(
            "Lỗi kỹ thuật: Kết quả vẫn đang chia sẻ bộ nhớ với mảng gốc."
        )

    return result


print(copy_columns(A))

# Kết thúc lời giải
```

#### Giải thích cách 2

`copy_columns` kiểm tra số trục và số cột, sau đó lấy cột `1`, `2` bằng lát cắt rồi gọi `.copy()` một cách tường minh. Giá trị trả về là một ndarray mới với cùng số hàng và hai cột. Không có phép gán nào vào `matrix` trong hàm.

`np.shares_memory(result, matrix)` được dùng như phép kiểm chứng tính độc lập vùng dữ liệu. Nếu còn chia sẻ, hàm phát sinh `RuntimeError` thay vì trả một kết quả trái yêu cầu. Khi truyền A nguyên vẹn, các giá trị trả về là bốn cặp cột ở bảng dưới. Việc sao chép có chi phí bộ nhớ tương ứng với số phần tử được chọn, đổi lại cho phép sửa kết quả độc lập.

#### Kết quả cách 2

| Hàng kết quả | Cột 0 (A cột 1) | Cột 1 (A cột 2) |
| --- | --- | --- |
| 0 | 12 | 11 |
| 1 | 21 | 24 |
| 2 | 33 | 31 |
| 3 | 44 | 42 |

`np.shares_memory(copy_columns(A), A)` cho `False`.

#### So sánh hai cách

Cách 1 dùng các lần gán để chứng minh tác động của view và copy. Cách 2 đáp ứng trực tiếp nhu cầu lấy hai cột độc lập để xử lý tiếp. Việc hai mảng có cùng giá trị không cho biết chúng có dùng chung vùng dữ liệu hay không.

:::

---

## Bài 4: Chọn phần tử nâng cao: Boolean mask, fancy indexing và lưới trực giao np.ix_

<span id="data-lab-03-04"></span>

::: exercise
**Mục tiêu**: Làm chủ ba kỹ thuật trích xuất phần tử nâng cao trong NumPy mà không dùng vòng lặp `for`: Mặt nạ logic Boolean, Cặp mảng chỉ mục tọa độ (Coordinate Fancy Indexing), và Lưới chỉ mục trực giao `np.ix_`. Giải thích bản chất sự khác biệt về kích thước (`shape`) của các kết quả.

**Dữ liệu đầu vào**: Ma trận $A$ kích thước $4 \times 3$, kiểu `np.int64`.

**Thao tác yêu cầu**:
1. Trích xuất toàn bộ các phần tử là số chẵn trong $A$ theo thứ tự duyệt từng hàng (row-major order) vào mảng `so_chan`.
2. Trích xuất đồng thời hai phần tử rời rạc $A[0, 1]$ và $A[2, 2]$ bằng cặp mảng chỉ mục vào mảng `hai_o`.
3. Trích xuất ma trận con kích thước $2 \times 2$ gồm cột 1, 2 tại các hàng 0, 2 bằng hàm tạo lưới trực giao `np.ix_` vào mảng `bon_o`.
4. Ghi lại kích thước (`shape`) của cả ba kết quả và giải thích cặn kẽ bản chất toán học tại sao chúng lại có số chiều và hình dạng khác nhau.
5. Đóng gói thành hàm `select_elements(matrix: np.ndarray) -> dict` tuân thủ đúng quy chuẩn dữ liệu.

**Trường hợp biên cần chú ý**:
- Không sử dụng bất kỳ vòng lặp `for` hay biểu thức comprehension nào.
- Các kết quả trích xuất phải giữ nguyên kiểu dữ liệu và không chia sẻ bộ nhớ với ma trận đầu vào.
:::

::: solution
#### Cách 1: Áp dụng cú pháp trực tiếp của NumPy theo từng yêu cầu trích xuất

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np

# 1. Trích xuất các số chẵn theo thứ tự hàng bằng Boolean Mask
mat_na_chan = A % 2 == 0
so_chan = A[mat_na_chan]

# 2. Trích xuất hai ô rời rạc bằng cặp mảng chỉ mục tọa độ
hang_chon = [0, 2]
cot_chon = [1, 2]
hai_o = A[hang_chon, cot_chon]

# 3. Trích xuất bốn ô giao điểm bằng lưới trực giao np.ix_
bon_o = A[np.ix_([0, 2], [1, 2])]

# Kết thúc lời giải

print("Paired selection:", hai_o)
print("Cartesian selection:", bon_o)
```

#### Giải thích cách 1

`A % 2 == 0` tạo mặt nạ Boolean cùng shape với A. Mỗi ô đúng tương ứng một số chẵn. `A[mat_na_chan]` gom các ô đúng theo thứ tự hàng vào mảng một trục, nên tám số chẵn có shape `(8,)`.

Với hai danh sách chỉ mục bằng nhau về độ dài, `A[hang_chon, cot_chon]` ghép phần tử theo từng vị trí: Cặp thứ nhất là `(0, 1)`, cặp thứ hai là `(2, 2)`. Kết quả chỉ có hai số `12`, `31`. Ngược lại, `np.ix_([0, 2], [1, 2])` dựng chỉ mục để lấy mọi giao điểm của hai hàng và hai cột, cho bảng hai hàng hai cột.

#### Kết quả cách 1

| Kết quả | Giá trị | shape |
| --- | --- | --- |
| so_chan | `[10, 12, 20, 24, 30, 40, 44, 42]` | `(8,)` |
| hai_o | `[12, 31]` | `(2,)` |
| bon_o, hàng 0 | `[12, 11]` | `(2, 2)` cho toàn bảng |
| bon_o, hàng 1 | `[33, 31]` |  |

#### Cách 2: Đóng gói hàm select_elements kết hợp kỹ thuật broadcasting tọa độ thay thế np.ix_

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np


def select_elements(matrix: np.ndarray) -> dict:
    """Trích xuất phần tử theo ba cơ chế: Boolean mask, fancy indexing và lưới tọa độ.

    Tham số:
        matrix: Mảng hai chiều kiểu số nguyên, kích thước tối thiểu 3 hàng và 3 cột.

    Trả về:
        Từ điển chứa so_chan (1D), hai_o (1D) và bon_o (2D).
    """
    if matrix.ndim != 2:
        raise ValueError("Yêu cầu ma trận đầu vào phải có 2 chiều.")
    if matrix.shape[0] < 3 or matrix.shape[1] < 3:
        raise ValueError("Ma trận cần có kích thước tối thiểu 3x3.")

    # 1. Lọc phần tử chẵn qua Boolean Mask
    so_chan = matrix[matrix % 2 == 0]

    # 2. Chọn hai phần tử tọa độ [0, 1] và [2, 2]
    hai_o = matrix[[0, 2], [1, 2]]

    # 3. Lấy giao điểm 4 ô bằng kỹ thuật broadcasting chỉ mục thay thế np.ix_
    rows = np.array([0, 2])[:, np.newaxis]  # shape (2, 1)
    cols = np.array([1, 2])[np.newaxis, :]  # shape (1, 2)
    bon_o = matrix[rows, cols]  # shape (2, 2)

    return {"so_chan": so_chan, "hai_o": hai_o, "bon_o": bon_o}


ket_qua = select_elements(A)
for ten, mang in ket_qua.items():
    print(ten, mang)

# Kết thúc lời giải
```

#### Giải thích cách 2

`select_elements` kiểm tra đầu vào có hai trục và đủ ba hàng, ba cột cho các chỉ số cố định. Hai kết quả đầu dùng cùng mặt nạ và cặp chỉ mục như Cách 1. Với kết quả thứ ba, hàm tạo mảng hàng shape `(2, 1)` và mảng cột shape `(1, 2)` bằng `np.newaxis`.

Khi hai mảng chỉ mục được broadcasting, chúng tạo lưới tọa độ shape `(2, 2)`, tương đương lưới của `np.ix_`. Cả ba cách lấy phần tử trong hàm đều thuộc lập chỉ mục nâng cao và cho bản sao dữ liệu. Vòng lặp cuối chỉ in các kết quả đã tính, không phải vòng lặp dùng để chọn từng phần tử của A.

#### Kết quả cách 2

| Kết quả | Giá trị | shape |
| --- | --- | --- |
| so_chan | `[10, 12, 20, 24, 30, 40, 44, 42]` | `(8,)` |
| hai_o | `[12, 31]` | `(2,)` |
| bon_o, hàng 0 | `[12, 11]` | `(2, 2)` cho toàn bảng |
| bon_o, hàng 1 | `[33, 31]` |  |

#### So sánh hai cách

Cách 1 dùng np.ix_ để biểu đạt trực tiếp giao của các hàng và cột. Cách 2 khai triển cơ chế lưới bằng cách thêm trục. Cần phân biệt chọn cặp tọa độ với chọn mọi giao điểm, vì chúng khác cả số phần tử lẫn shape.

:::

---

## Bài 5: Cơ chế phát sóng broadcasting và phép cộng theo chiều không gian

<span id="iai-03-bai-5"></span>
<span id="data-lab-03-05"></span>

::: exercise
**Mục tiêu**: Nắm vững nguyên lý và thuật toán căn lề chiều (Trailing Dimensions Alignment) của cơ chế phát sóng Broadcasting trong NumPy, thực hiện các phép toán cộng trừ ma trận theo từng chiều mà không dùng vòng lặp.

**Dữ liệu đầu vào**:
- Ma trận $A$ kích thước $4 \times 3$, kiểu `np.int64`.
- Vector cộng theo cột: $b = \text{np.array}([1, 2, 3])$.
- Vector cộng theo hàng: $d = \text{np.array}([10, 20, 30, 40])$.

**Thao tác yêu cầu**:
1. Tạo ma trận $K$ qua hai bước cộng vector hóa:
   - Bước 1: Từ $A$, cộng các giá trị $1, 2, 3$ lần lượt vào các cột $0, 1, 2$.
   - Bước 2: Trên kết quả vừa thu được, cộng các giá trị $10, 20, 30, 40$ lần lượt vào các hàng $0, 1, 2, 3$.
   Ví dụ: Ô `K[1, 2]` nhận giá trị gốc 24, phần cộng theo cột là 3 và phần cộng theo hàng là 20. Kết quả là 47. Hãy tính thêm cả hàng đầu tiên của K để đối chiếu với mã.
2. Ghi rõ kích thước (`shape`) của từng mảng tham gia trong phép toán ở mỗi bước.
3. Giải thích tại sao phép cộng trực tiếp `A + d` phát sinh lỗi `ValueError`, và chỉ rõ cách khắc phục.
4. Đóng gói hàm `broadcast_add(matrix: np.ndarray, column_add: np.ndarray, row_add: np.ndarray) -> np.ndarray` áp dụng cho ma trận và các vector có kích thước bất kỳ.

**Trường hợp biên cần chú ý**:
- Không làm thay đổi dữ liệu của ma trận gốc $A$.
- Hỗ trợ cả số nguyên lẫn số thực.
- Không giả định số hàng bằng số cột của ma trận.
:::

::: solution
#### Cách 1: Thực hiện phép cộng hai bước kết hợp biến đổi trục bằng reshape

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

# Bắt đầu lời giải

import numpy as np

b = np.array([1, 2, 3])
d = np.array([10, 20, 30, 40])

# Bước 1: Cộng vector b vào từng cột của A
# Shape của A là (4, 3), shape của b là (3,). Kết quả bước 1 có shape (4, 3).
K1 = A + b

# Bước 2: Chuyển d thành ma trận cột có shape (4, 1) và cộng theo hàng
d_cot = d.reshape(-1, 1)  # shape (4, 1)
K = K1 + d_cot  # shape (4, 3)
np.testing.assert_array_equal(K[0], [21, 24, 24])
print("Hàng đầu của K:", K[0])

# Kết thúc lời giải
```

#### Giải thích cách 1

`b` có shape `(3,)`, khớp số cột nên mỗi hàng của A được cộng cùng ba số `1`, `2`, `3`. `K1` vẫn có shape `(4, 3)`. Vector `d` có bốn phần tử nhưng chưa có trục cột, nên phải đổi thành shape `(4, 1)` bằng `reshape(-1, 1)` trước khi cộng theo hàng.

Số `-1` trong reshape yêu cầu NumPy suy ra độ dài trục đó từ số phần tử, còn `1` đặt một cột. Sau cộng, ô `K[1, 2]` bằng giá `24` cộng `3` rồi cộng `20`, được `47`. `np.testing.assert_array_equal` kiểm tra chính xác hàng đầu `[21, 24, 24]` và phát sinh lỗi nếu sai. Phép `A + d` không hợp lệ vì trục cuối có độ dài `3` và `4`, không bằng nhau và không có trục nào bằng `1`.

#### Kết quả cách 1

| Hàng | K, cột 0 | K, cột 1 | K, cột 2 |
| --- | --- | --- | --- |
| 0 | 21 | 24 | 24 |
| 1 | 41 | 43 | 47 |
| 2 | 61 | 65 | 64 |
| 3 | 81 | 86 | 85 |

Dòng in của đoạn mã là `Hàng đầu của K: [21 24 24]`.

#### Cách 2: Đóng gói hàm broadcast_add vector hóa một dòng với toán tử np.newaxis

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

A = np.array([[10, 12, 11], [20, 21, 24], [30, 33, 31], [40, 44, 42]], dtype=np.int64)

b = np.array([1, 2, 3])

d = np.array([10, 20, 30, 40])

# Bắt đầu lời giải

import numpy as np


def broadcast_add(
    matrix: np.ndarray, column_add: np.ndarray, row_add: np.ndarray
) -> np.ndarray:
    """Cộng vector vào cột và hàng của ma trận bằng cơ chế broadcasting vector hóa.

    Tham số:
        matrix: Mảng hai chiều kiểu số hữu hạn không rỗng.
        column_add: Mảng 1 chiều có độ dài bằng số cột của matrix.
        row_add: Mảng 1 chiều có độ dài bằng số hàng của matrix.

    Trả về:
        Mảng hai chiều mới có cùng shape với matrix.
    """
    if matrix.ndim != 2:
        raise ValueError("Yêu cầu ma trận đầu vào phải có 2 chiều.")
    nrows, ncols = matrix.shape

    col_vec = np.asarray(column_add)
    row_vec = np.asarray(row_add)

    if col_vec.ndim != 1 or col_vec.size != ncols:
        raise ValueError(
            f"Vector cột cần có 1 chiều độ dài {ncols}, hiện tại {col_vec.shape}."
        )
    if row_vec.ndim != 1 or row_vec.size != nrows:
        raise ValueError(
            f"Vector hàng cần có 1 chiều độ dài {nrows}, hiện tại {row_vec.shape}."
        )

    # Áp dụng biểu thức vector hóa một dòng duy nhất
    # row_vec[:, np.newaxis] mở rộng shape từ (nrows,) thành (nrows, 1)
    return matrix + col_vec + row_vec[:, np.newaxis]


ket_qua = broadcast_add(A, b, d)
np.testing.assert_array_equal(ket_qua[0], [21, 24, 24])
print(ket_qua)

# Kết thúc lời giải
```

#### Giải thích cách 2

`broadcast_add` nhận ma trận cùng vector cộng theo cột và vector cộng theo hàng. `nrows, ncols = matrix.shape` đọc kích thước thực tế. `np.asarray` cho phép chuẩn hóa hai vector đầu vào thành ndarray trước khi kiểm tra chúng có một trục và đủ số phần tử.

Biểu thức `row_vec[:, np.newaxis]` đổi shape `(nrows,)` thành `(nrows, 1)` để mỗi hàng nhận đúng một số cộng. Hàm trả `matrix + col_vec + row_vec[:, np.newaxis]`, tạo kết quả mới và không gán vào ma trận gốc. Việc kiểm tra độ dài hai vector ngăn trường hợp phép toán vẫn chạy nhưng áp dụng sai ý nghĩa hàng/cột.

#### Kết quả cách 2

| Hàng | K, cột 0 | K, cột 1 | K, cột 2 |
| --- | --- | --- | --- |
| 0 | 21 | 24 | 24 |
| 1 | 41 | 43 | 47 |
| 2 | 61 | 65 | 64 |
| 3 | 81 | 86 | 85 |

#### So sánh hai cách

Cách 1 chia hai phép cộng để quan sát các shape trung gian. Cách 2 kiểm tra tham số rồi viết biểu thức tổng hợp dùng lại cho bảng khác. Cả hai dùng broadcasting và cho cùng K, không cần tạo bản lặp đầy đủ của các vector bằng tile.

:::

---

## Bài 6: Chuẩn hóa dữ liệu theo hàng và khắc phục lỗi sai trục axis

<span id="data-lab-03-06"></span>

::: exercise
**Mục tiêu**: Phát hiện và khắc phục lỗi logic tiềm ẩn khi thực hiện phép toán thu gọn (reduction) theo trục `axis` kết hợp với broadcasting, hiểu rõ tầm quan trọng của việc duy trì số chiều không gian (`keepdims`).

**Dữ liệu đầu vào**: Bảng giá giả lập của 3 chỗ ở qua 3 kỳ thu thập (đơn vị USD/đêm):

```python
import numpy as np

gia = np.array([[40, 50, 60], [60, 60, 60], [30, 60, 90]], dtype=np.float64)
```


Khi viết dưới dạng ma trận toán học:

$$
\text{gia} = \begin{bmatrix}
40.0 & 50.0 & 60.0 \\
60.0 & 60.0 & 60.0 \\
30.0 & 60.0 & 90.0
\end{bmatrix}
$$

**Tình huống lỗi thực tế**: Đoạn mã dưới đây thực thi thành công mà không báo lỗi, nhưng kết quả tính toán lại sai lệch hoàn toàn so với yêu cầu toán học:

```python
tb_sai = gia.mean(axis=1)
sai = gia - tb_sai
```


**Thao tác yêu cầu**:
1. Phân tích kích thước (`shape`) của `tb_sai` và chỉ ra cơ chế phát sóng ngầm định đã khiến phép tính `gia - tb_sai` bị sai bản chất như thế nào.
2. Sửa lại đoạn mã để tính toán chính xác ma trận độ lệch chuẩn hóa `chenh_lech`, sao cho giá của mỗi chỗ ở được trừ đi đúng giá trị trung bình của chính chỗ ở đó.
3. Kiểm tra điều kiện: Giá trị trung bình của từng hàng sau khi chuẩn hóa phải xấp xỉ 0 (`np.allclose(chenh_lech.mean(axis=1), 0)`).
4. Đóng gói hàm `center_rows(prices: np.ndarray) -> tuple` trả về bộ đôi `(trung_binh_hang, chenh_lech)` với `trung_binh_hang` có shape `(N, 1)` và `chenh_lech` có cùng kích thước với mảng đầu vào.

**Trường hợp biên cần chú ý**:
- Hỗ trợ ma trận không vuông (số hàng khác số cột).
- Với ma trận chỉ có 1 cột, độ lệch của mọi phần tử phải bằng 0.
:::

::: solution
#### Cách 1: Sửa lỗi trực tiếp bằng tham số keepdims=True

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

import numpy as np

gia = np.array([[40, 50, 60], [60, 60, 60], [30, 60, 90]], dtype=np.float64)

# Sửa lỗi: Giữ nguyên số chiều không gian (keepdims=True) để có shape (3, 1)
trung_binh_hang = gia.mean(axis=1, keepdims=True)

# Thực hiện phép trừ broadcasting chuẩn xác theo hàng
chenh_lech = gia - trung_binh_hang

# Kết thúc lời giải

print("Row means:", trung_binh_hang)
print("Centered values:", chenh_lech)
```

#### Giải thích cách 1

`gia.mean(axis=1)` thu gọn trục cột, tạo một trung bình cho mỗi hàng. Nếu không giữ số trục, kết quả có shape `(3,)`. Khi trừ khỏi bảng vuông `(3, 3)`, NumPy ghép trục cuối nên vô tình trừ theo cột, dù các số là trung bình hàng.

`keepdims=True` giữ trục đã thu gọn với độ dài `1`, nên `trung_binh_hang` có shape `(3, 1)`. Bây giờ mỗi hàng trừ đúng trung bình của chính nó. Hàng `[40, 50, 60]` trừ `50` thành `[-10, 0, 10]`, hàng hằng `60` thành toàn `0`, và hàng `[30, 60, 90]` thành `[-30, 0, 30]`. Đây là phép đưa tâm mỗi hàng về không, không phải chia cho độ lệch chuẩn.

#### Kết quả cách 1

| Hàng | Trung bình | Độ lệch cột 0 | Độ lệch cột 1 | Độ lệch cột 2 |
| --- | --- | --- | --- | --- |
| 0 | 50.0 | −10.0 | 0.0 | 10.0 |
| 1 | 60.0 | 0.0 | 0.0 | 0.0 |
| 2 | 60.0 | −30.0 | 0.0 | 30.0 |

`trung_binh_hang.shape` bằng `(3, 1)`, còn `chenh_lech.shape` bằng `(3, 3)`. Trung bình của ba hàng độ lệch đều bằng `0.0`.

#### Cách 2: Đóng gói hàm center_rows tổng quát hóa với kỹ thuật mở rộng trục lát cắt

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

gia = np.array([[40, 50, 60], [60, 60, 60], [30, 60, 90]], dtype=np.float64)

# Bắt đầu lời giải

import numpy as np


def center_rows(prices: np.ndarray) -> tuple:
    """Chuẩn hóa dữ liệu theo hàng bằng cách trừ đi trung bình của mỗi hàng.

    Tham số:
        prices: Mảng hai chiều kiểu số thực hoặc số nguyên, không rỗng.

    Trả về:
        Tuple gồm (trung_binh_hang, chenh_lech):
        - trung_binh_hang: Mảng 2D float có shape (số_hàng, 1).
        - chenh_lech: Mảng 2D float có cùng shape với prices.
    """
    arr = np.asarray(prices, dtype=np.float64)
    if arr.ndim != 2:
        raise ValueError("Yêu cầu mảng đầu vào phải có đúng 2 chiều.")
    if arr.size == 0:
        raise ValueError("Mảng đầu vào không được rỗng.")

    # Tính trung bình theo hàng và định hình lại thành vector cột (N, 1)
    row_means = arr.mean(axis=1)[:, np.newaxis]
    deviations = arr - row_means

    return row_means, deviations


trung_binh, do_lech = center_rows(gia)
print("Trung bình từng hàng:", trung_binh)
print("Độ lệch:", do_lech)

# Kết thúc lời giải
```

#### Giải thích cách 2

`np.asarray(prices, dtype=np.float64)` chuẩn hóa đầu vào sang kiểu số thực để phép lấy trung bình phù hợp cả dữ liệu nguyên. Hàm kiểm tra hai trục và không rỗng trước khi tính. `arr.mean(axis=1)[:, np.newaxis]` thực hiện hai bước tương đương keepdims: Tính trung bình hàng rồi thêm một trục có độ dài `1`.

Hàm trả tuple `(row_means, deviations)`, vì vậy nơi gọi dùng hai tên để nhận hai mảng. Phép trừ tạo mảng kết quả mới, không sửa `prices`. Khi kiểm tra số thực, `np.allclose(do_lech.mean(axis=1), 0)` phù hợp hơn yêu cầu mọi giá trị phải bằng không tuyệt đối, vì phép tính dấu phẩy động có thể để lại sai số nhỏ.

#### Kết quả cách 2

| Hàng | Trung bình | Độ lệch cột 0 | Độ lệch cột 1 | Độ lệch cột 2 |
| --- | --- | --- | --- | --- |
| 0 | 50.0 | −10.0 | 0.0 | 10.0 |
| 1 | 60.0 | 0.0 | 0.0 | 0.0 |
| 2 | 60.0 | −30.0 | 0.0 | 30.0 |

`np.allclose(do_lech.mean(axis=1), 0)` cho `True`.

#### So sánh hai cách

Cách 1 giữ trục ngay khi thu gọn bằng keepdims. Cách 2 thêm lại trục sau khi thu gọn và gom kiểm tra đầu vào vào hàm. Cả hai làm cùng một phép biến đổi. Bảng vuông che giấu lỗi shape, nên hãy kiểm tra thêm bảng không vuông khi dùng lại hàm.

:::

---

## Bài 7: Phân tích hiệu năng: Vòng lặp Python thuần và vector hóa NumPy

<span id="data-lab-03-07"></span>

::: exercise
**Mục tiêu**: Đo lường và giải thích cặn kẽ bản chất chênh lệch hiệu năng giữa vòng lặp thông dịch của Python thuần và phép toán vector hóa trên mảng NumPy, phân tích dưới góc độ kiến trúc vùng nhớ liền kề (contiguous buffer) và tối ưu hóa phần cứng (SIMD).

**Dữ liệu đầu vào**:
Xét bài toán nhân đôi mọi phần tử của một dãy số nguyên:
1. Phương pháp 1: Vòng lặp list comprehension trên danh sách Python (`nhan_list`).
2. Phương pháp 2: Vòng lặp list comprehension trên đối tượng `ndarray` (`nhan_for_array`).
3. Phương pháp 3: Phép toán vector hóa mảng `x * 2` trên `ndarray` (`nhan_array`).

**Thao tác yêu cầu**:
1. Triển khai cả ba phương pháp và kiểm tra tính tương đương kết quả số học trên mảng nhỏ ($N = 10$) và mảng lớn ($N = 100\,000$).
2. Đo thời gian thực thi bằng hàm `timeit.repeat` (lấy thời gian nhỏ nhất trong 3 lần đo lặp lại và nêu giới hạn của phép đo), lập bảng đối chiếu kết quả đo đạc.
3. Trả lời ba câu hỏi phân tích bản chất:
   - Câu hỏi 1: Phương pháp nào vẫn chạy vòng lặp bên trong tầng thông dịch của Python?
   - Câu hỏi 2: Việc chuyển đổi danh sách Python thành đối tượng `ndarray` nhưng vẫn dùng vòng lặp `for` có giúp chương trình chạy nhanh hơn không? Giải thích nguyên nhân dưới góc độ đóng gói đối tượng (boxing/unboxing).
   - Câu hỏi 3: Tỷ lệ chênh lệch thời gian giữa các phương pháp thay đổi như thế nào khi tăng kích thước từ $N = 10$ lên $N = 100\,000$? Giải thích dựa trên chi phí thông dịch (interpreter overhead) và vector hóa phần cứng (SIMD).

**Trường hợp biên cần chú ý**:
- Dữ liệu thử nghiệm phải được chuẩn bị hoàn tất trước khi kích hoạt bộ đếm thời gian.
- Không so sánh tỷ lệ tốc độ bằng các con số giả định, mà phải dựa trên số đo thực tế của môi trường chạy.
:::

::: solution
#### Cách 1: Đo lường thực nghiệm trực tiếp bằng timeit.repeat

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

import numpy as np
from timeit import repeat


def nhan_list(xs):
    return [v * 2 for v in xs]


def nhan_for_array(x):
    return [v * 2 for v in x]


def nhan_array(x):
    return x * 2


# Chạy thử nghiệm và đo lường trên hai quy mô kích thước
for n in (10, 100_000):
    x = np.arange(n, dtype=np.int64)
    xs = x.tolist()

    # Kiểm tra tính tương đương số học
    assert nhan_list(xs) == nhan_array(x).tolist()
    assert nhan_for_array(x) == nhan_array(x).tolist()

    so_lan = 100 if n == 10 else 5
    print(f"Quy mô dữ liệu n = {n:,}:")
    for ten, ham, dau_vao in [
        ("Vòng for trên list", nhan_list, xs),
        ("Vòng for trên ndarray", nhan_for_array, x),
        ("Phép toán vector hóa ndarray", nhan_array, x),
    ]:
        t = min(repeat(lambda: ham(dau_vao), number=so_lan, repeat=3)) / so_lan
        print(f"  {ten}: {t * 1e6:.2f} us/lan")

# Kết thúc lời giải
```

#### Giải thích cách 1

Ba hàm đều nhân mỗi số với `2`, nhưng hai comprehension vẫn lặp ở mức Python. Đổi list thành ndarray rồi tiếp tục dùng `for` chưa loại bỏ việc xử lý từng phần tử trong Python. Với dtype số của mẫu, biểu thức `x * 2` giao phép toán mảng cho vòng lặp đã biên dịch của NumPy.

`repeat(..., number=so_lan, repeat=3)` đo ba đợt, mỗi đợt thực hiện `so_lan` lời gọi. Mỗi số trả về là thời gian của cả đợt, nên cần chia cho `so_lan` để ra thời gian một lượt. `min` chọn đợt nhanh nhất để giảm ảnh hưởng của một số đợt bị trì hoãn, không loại sạch mọi nhiễu. Mảng và list được tạo trước phép đo, nên số đo chưa gồm thời gian chuyển đổi dữ liệu.

#### Kết quả cách 1

Lần chạy kiểm chứng cho các số dưới đây, đơn vị µs/lượt. Đây là đầu ra minh họa của lần đo, không phải hằng số kỳ vọng:

| n | Comprehension trên list | Comprehension trên ndarray | x * 2 |
| --- | --- | --- | --- |
| 10 | 0.23 | 1.05 | 0.62 |
| 100000 | 2758.28 | 6202.08 | 37.40 |

#### Cách 2: Xây dựng hàm đo chuẩn hóa benchmark_vectorization tự động tính hệ số gia tốc

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

import numpy as np
from timeit import repeat


def benchmark_vectorization(sizes=(10, 100_000)) -> dict:
    """Đo lường thời gian thực thi và tính toán hệ số gia tốc của vector hóa.

    Tham số:
        sizes: Tuple các quy mô kích thước mảng cần khảo sát.

    Trả về:
        Từ điển chứa thời gian thực thi (µs) và tỷ số gia tốc (speedup) cho từng quy mô.
    """
    results = {}

    for n in sizes:
        x = np.arange(n, dtype=np.int64)
        xs = x.tolist()

        runs = 100 if n <= 1000 else 5
        t_list = min(repeat(lambda: [v * 2 for v in xs], number=runs, repeat=3)) / runs
        t_for_arr = (
            min(repeat(lambda: [v * 2 for v in x], number=runs, repeat=3)) / runs
        )
        t_vec = min(repeat(lambda: x * 2, number=runs, repeat=3)) / runs

        results[n] = {
            "list_comprehension_us": t_list * 1e6,
            "for_on_ndarray_us": t_for_arr * 1e6,
            "vectorized_us": t_vec * 1e6,
            "speedup_vs_list": t_list / t_vec,
            "speedup_vs_for_ndarray": t_for_arr / t_vec,
        }

    return results


print(benchmark_vectorization(sizes=(10, 100000)))

# Kết thúc lời giải
```

#### Giải thích cách 2

`benchmark_vectorization` nhận các kích thước ở `sizes` và trả một từ điển có khóa là kích thước. Với mỗi kích thước, hàm chuẩn bị ndarray và list tương ứng, chọn số lượt đo rồi ghi thời gian của ba thao tác dưới dạng µs/lượt. `lambda` tạo một lời gọi không đối số để bộ đo thực thi lặp lại.

`speedup_vs_list` lấy thời gian của list chia thời gian vector hóa. Tỷ số lớn hơn `1` nghĩa là vector hóa nhanh hơn trong đúng phép đo đó, nhỏ hơn `1` nghĩa là chậm hơn. NumPy có chi phí khởi động phép toán và cấp mảng kết quả, nên với mảng rất nhỏ chi phí này có thể chiếm phần lớn thời gian. Việc có dùng SIMD hay không phụ thuộc phép toán, bản dựng và CPU, không được suy ra chỉ từ tên ndarray.

#### Kết quả cách 2

Lần chạy hàm kiểm chứng tạo các giá trị sau, đã làm tròn để đọc:

| n | List (µs) | For ndarray (µs) | Vector (µs) | Tỷ số list/vector |
| --- | --- | --- | --- | --- |
| 10 | 0.199 | 0.995 | 0.597 | 0.33 |
| 100000 | 2825.64 | 6459.56 | 32.58 | 86.73 |

Ở n = 100000, tỷ số vòng for trên ndarray so với vector khoảng `198.27` trong lần đo này.

#### So sánh hai cách

Hai cách đo cùng ba thao tác. Cách 1 in bảng ngay, còn Cách 2 giữ số đo và tỷ số trong một cấu trúc để xử lý tiếp. Không so các con số giữa hai lần chạy như thể môi trường không đổi. Khi đánh giá cả quy trình, cần đo thêm chi phí đọc dữ liệu, chuyển kiểu và chuyển list thành mảng.

:::

---

## Bài 8: Thống kê mô tả dữ liệu giá và lấy mẫu ngẫu nhiên không hoàn lại

<span id="data-lab-03-08"></span>

::: exercise
**Mục tiêu**: Tính trung bình, trung vị và độ lệch chuẩn của một dãy giá. Quan sát tác động của giá cao lên các chỉ số, rồi lấy mẫu ngẫu nhiên không hoàn lại bằng bộ sinh của NumPy.

**Dữ liệu đầu vào**: Dãy giá của 5 chỗ ở giả lập là `[40, 50, 60, 70, 380]`, tính bằng USD mỗi đêm.

**Thao tác yêu cầu**:
1. Tính toán giá trị trung bình (`mean`), trung vị (`median`), và độ lệch chuẩn tổng thể (`std` với bậc tự do `ddof=0`) của mảng bằng NumPy.
2. Tính tỷ lệ phần trăm (`share`) các chỗ ở có mức giá không vượt quá 70 USD/đêm.
3. Rút ngẫu nhiên một mẫu gồm 3 chỗ ở không hoàn lại (`replace=False`) sử dụng bộ tạo số ngẫu nhiên `np.random.default_rng(seed=42)`, trích xuất các giá trị trong mẫu và tính trung bình mẫu.
4. Đóng gói quy trình trên thành hàm `price_statistics(prices: np.ndarray, threshold: float = 70.0, sample_size: int = 3, seed: int = 42) -> dict` tuân thủ đúng quy chuẩn dữ liệu.
5. Trả lời cặn kẽ bốn câu hỏi định tính thực tiễn trong phân tích dữ liệu:
   - Trong báo cáo thực tế, nên dùng giá trị trung bình hay trung vị để mô tả mức giá điển hình của tập dữ liệu này? Vì sao?
   - Có nên loại bỏ ngay giá trị 380 USD/đêm chỉ vì nó cao vượt trội so với các quan sát còn lại hay không?
   - Giá trị trung bình mẫu rút ra có nhất thiết phải bằng trung bình của toàn bộ 5 chỗ ở không? Việc cố định hạt giống `seed` có bảo đảm mẫu thu được mang tính đại diện hoàn hảo hay không?
   - Khi đã có toàn bộ dữ liệu hợp lệ trong bộ nhớ, việc lấy mẫu ngẫu nhiên có cần thiết để tính giá trung bình không? Khi nào việc trích xuất một mẫu nhỏ vẫn mang lại giá trị kỹ thuật thực tế?

**Trường hợp biên cần chú ý**:
- Không sửa đổi mảng đầu vào và không can thiệp vào bộ sinh số ngẫu nhiên toàn cục.
- Giữ cùng phiên bản NumPy, cấu hình bộ sinh, seed và chuỗi lời gọi để đối chiếu kết quả giữa các lần chạy.
:::

::: solution
#### Cách 1: Tính toán tuần tự bằng các hàm thống kê cơ bản của NumPy

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

import numpy as np

gia_dem = np.array([40, 50, 60, 70, 380], dtype=np.float64)

# 1. Tính toán các đại lượng thống kê mô tả
trung_binh = float(np.mean(gia_dem))
trung_vi = float(np.median(gia_dem))
do_lech_chuan = float(np.std(gia_dem, ddof=0))

# 2. Tính tỷ lệ giá không vượt quá 70 USD
ty_le = float(np.mean(gia_dem <= 70.0))

# 3. Lấy mẫu ngẫu nhiên không hoàn lại 3 phần tử với seed 42
rng = np.random.default_rng(42)
chi_muc = rng.choice(len(gia_dem), size=3, replace=False)
mau = gia_dem[chi_muc]
tb_mau = float(np.mean(mau))

# Kết thúc lời giải

print(
    {
        "mean": trung_binh,
        "median": trung_vi,
        "std": do_lech_chuan,
        "share": ty_le,
        "indices": chi_muc,
        "sample": mau,
        "sample_mean": tb_mau,
    }
)
```

#### Giải thích cách 1

`np.mean`, `np.median` và `np.std(..., ddof=0)` lần lượt tính trung bình, trung vị và độ lệch chuẩn tổng thể. Tổng năm giá bằng `600`, nên trung bình là `120`. Trung vị là phần tử thứ ba sau sắp xếp, bằng `60`. Tổng bình phương độ lệch so với `120` bằng `85000`, chia `5` được phương sai `17000`, lấy căn cho độ lệch chuẩn khoảng `130.384` USD.

`gia_dem <= 70.0` tạo bốn giá trị True và một False, nên trung bình Boolean bằng `0.8`. `default_rng(42)` tạo một bộ sinh cục bộ. `choice(len(gia_dem), size=3, replace=False)` chọn ba chỉ mục khác nhau, rồi lập chỉ mục lấy ba giá tương ứng. Với chuỗi lời gọi và phiên bản NumPy đang kiểm tra, các chỉ mục là `[4, 0, 3]`.

#### Kết quả cách 1

| Chỉ số | Kết quả |
| --- | --- |
| mean | 120.0 |
| median | 60.0 |
| std, ddof=0 | 130.38404810405297 |
| share | 0.8 (80%) |
| indices | `[4, 0, 3]` |
| sample | `[380.0, 40.0, 70.0]` |
| sample_mean | 163.33333333333334 |

#### Cách 2: Đóng gói hàm price_statistics kiểm soát ràng buộc dữ liệu và hạt giống ngẫu nhiên

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

gia_dem = np.array([40, 50, 60, 70, 380], dtype=np.float64)

# Bắt đầu lời giải

import numpy as np


def price_statistics(
    prices: np.ndarray, threshold: float = 70.0, sample_size: int = 3, seed: int = 42
) -> dict:
    """Tính toán thống kê mô tả và trích xuất mẫu ngẫu nhiên không hoàn lại.

    Tham số:
        prices: Mảng 1 chiều chứa các mức giá không âm, không rỗng.
        threshold: Ngưỡng giá cần tính tỷ lệ phần trăm.
        sample_size: Kích thước mẫu cần rút (1 <= sample_size <= len(prices)).
        seed: Hạt giống sinh số ngẫu nhiên không âm.

    Trả về:
        Từ điển chứa mean, median, std, share, indices, sample và sample_mean.
    """
    arr = np.asarray(prices, dtype=np.float64)
    if arr.ndim != 1 or arr.size == 0:
        raise ValueError("Mảng giá phải là mảng 1 chiều không rỗng.")
    if not (1 <= sample_size <= arr.size):
        raise ValueError(
            f"sample_size {sample_size} phải nằm trong khoảng [1, {arr.size}]."
        )

    # Tính các tham số thống kê mô tả tổng thể
    mean_val = float(np.mean(arr))
    median_val = float(np.median(arr))
    std_val = float(np.std(arr, ddof=0))
    share_val = float(np.mean(arr <= threshold))

    # Rút mẫu ngẫu nhiên độc lập
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(arr), size=sample_size, replace=False)
    sample_arr = arr[indices]
    sample_mean_val = float(np.mean(sample_arr))

    return {
        "mean": mean_val,
        "median": median_val,
        "std": std_val,
        "share": share_val,
        "indices": indices,
        "sample": sample_arr,
        "sample_mean": sample_mean_val,
    }


print(price_statistics(gia_dem))

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm nhận giá, ngưỡng, kích thước mẫu và seed, rồi trả từ điển chứa cả thống kê lẫn các mảng mẫu. `np.asarray(..., dtype=np.float64)` chuẩn hóa kiểu số. Hai kiểm tra tiếp theo yêu cầu mảng một trục không rỗng và số phần tử mẫu nằm từ `1` đến kích thước mảng.

Các kết quả thống kê được chuyển thành `float` Python, còn `indices` và `sample` vẫn là ndarray. `replace=False` cấm chọn lại cùng một chỉ mục, không cấm hai quan sát khác nhau có cùng giá. Seed chỉ giúp lặp lại lựa chọn khi giữ cùng cấu hình bộ sinh và chuỗi lời gọi. Nó không bảo đảm một mẫu ba dòng đại diện hoàn hảo, cũng không tự kiểm chứng giá cao là sai dữ liệu.

#### Kết quả cách 2

| Chỉ số | Kết quả |
| --- | --- |
| mean | 120.0 |
| median | 60.0 |
| std, ddof=0 | 130.38404810405297 |
| share | 0.8 (80%) |
| indices | `[4, 0, 3]` |
| sample | `[380.0, 40.0, 70.0]` |
| sample_mean | 163.33333333333334 |

#### So sánh hai cách

Cách 1 cho thấy từng biến trung gian, Cách 2 đóng gói cùng quy trình với tham số và kiểm tra kích thước. Trung vị `60` mô tả vị trí giữa của năm giá, còn trung bình `120` tính cả ảnh hưởng của giá `380`. Chưa có bằng chứng để xóa `380` hoặc gán nó cho một loại chỗ ở cụ thể. Nếu đã có toàn bộ năm giá, có thể tính trung bình trực tiếp mà không cần lấy mẫu.

:::

---

## Tổng kết bài học

| Chủ đề kỹ thuật | Khái niệm trọng tâm | Bản chất cần ghi nhớ |
| :--- | :--- | :--- |
| Cấu trúc mảng | `shape`, `dtype`, `strides`, `nbytes` | Mảng C-contiguous như mảng $A$ ban đầu lưu trữ dữ liệu liền kề, còn các view bước nhảy có thể không liên tục. |
| Lát cắt và view | `A[1::2, 0::2]`, `np.shares_memory` | View dùng chung dữ liệu với mảng gốc. Nó vẫn cần bộ nhớ cho thông tin quản lý, nhưng không sao chép toàn bộ phần tử. Sửa view có thể làm đổi mảng gốc. |
| Phân biệt view và copy | Lập chỉ mục lát cắt vs Lập chỉ mục mảng | Lát cắt cơ bản tạo view. Lấy phần tử bằng danh sách hoặc mảng chỉ mục nâng cao tạo bản sao dữ liệu. |
| Kỹ thuật chọn lọc | Mặt nạ boolean, mảng chỉ mục, `np.ix_` | Mặt nạ cùng shape với A lấy các phần tử thành mảng 1D. Hai mảng chỉ mục có thể chọn các cặp tọa độ hoặc tạo lưới giao điểm. |
| Phát sóng (broadcasting) | Trailing dimension alignment, `np.newaxis` | So sánh các trục từ phải qua trái. Hai độ dài phải bằng nhau hoặc một trong hai bằng 1 để phép toán mảng có thể broadcasting. |
| Hiệu năng thực thi | Vòng lặp ở mã máy, chi phí xử lý từng phần tử | Nhiều phép toán trên dtype số dùng vòng lặp đã biên dịch. Việc dùng SIMD phụ thuộc phép toán, bản dựng và CPU. Cần đo cả chi phí chuẩn bị dữ liệu khi so sánh toàn quy trình. |
| Thống kê và lấy mẫu | Median vs Mean, `Generator`, Outliers | Trung vị ít nhạy với độ lớn của một giá cực đoan. Seed giúp tái lập lựa chọn khi giữ cùng cấu hình và chuỗi lời gọi, nhưng không bảo đảm tính đại diện của mẫu. |

---

## Tài liệu tham khảo

1. McKinney, W. (2022). *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter* (3rd ed.). O'Reilly Media.
2. Oliphant, T. E. (2006). *A Guide to NumPy*. Trelgol Publishing.
3. NumPy Developers. (2026). *NumPy Reference and User Guide (Version 2.x)*. `https://numpy.org/doc/stable/`
4. Harris, C. R., Millman, K. J., van der Walt, S. J., et al. (2020). Array programming with NumPy. *Nature*, 585(7825), 357–362.
5. Inside Airbnb. (2026). *Santiago, Chile Data Listings & Visualisations Snapshot*. `https://data.insideairbnb.com/chile/rm/santiago/`

- NumPy Developers. [CPU/SIMD optimizations](https://numpy.org/doc/stable/reference/simd/index.html).
