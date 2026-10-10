---
course: xu-ly-du-lieu
lecture: bai-03-numpy
section: lecture
title: "NumPy & tư duy vector hóa"
prerequisites: ["mang", "chi-muc", "con-tro", "vector-hoa", "broadcasting"]
lessonStatus: ready
description: "Cấu trúc bộ nhớ ndarray, strides, cơ chế view vs copy, broadcasting, ufunc và đo lường hiệu năng tính toán ma trận."
---

## 1. Giải phẫu Bộ nhớ Nội tại của Mảng Đa chiều (`ndarray`)

Nếu Python thuần túy là một người điều phối linh hoạt, thì NumPy chính là cỗ máy tính toán hạng nặng của toàn bộ hệ sinh thái Khoa học Dữ liệu và Trí tuệ Nhân tạo. Mọi cấu trúc bảng của pandas hay tensor của PyTorch, TensorFlow đều lấy cảm hứng trực tiếp từ kiến trúc của **`np.ndarray`**.

Để làm chủ NumPy, ta không thể tiếp tục nhìn mảng như một danh sách lồng nhau thông thường, mà phải hiểu rõ cách thức hệ thống quản lý mảng ở tầng bộ nhớ máy tính.

<DataDiagram name="ndarray-memory" />

Một đối tượng `ndarray` trong NumPy gồm hai thành phần tách biệt hoàn toàn:
1. **Khối dữ liệu thô (*Data Buffer*)**: Một mảng 1 chiều liên tục trong bộ nhớ RAM, lưu trữ các byte nhị phân của dữ liệu theo chuẩn ngôn ngữ C hoặc Fortran.
2. **Khối tiêu đề siêu dữ liệu (*Array Metadata*)**: Chứa các thông số mô tả hình học của mảng:
   - **`dtype`**: Kiểu dữ liệu và số byte cho mỗi phần tử (ví dụ `int64` chiếm 8 bytes, `int32` chiếm 4 bytes).
   - **`shape`**: Bộ giá trị tuple mô tả số lượng phần tử trên mỗi trục hình học (ví dụ ma trận 4 hàng 3 cột có `shape = (4, 3)`).
   - **`strides`**: Bộ giá trị tuple xác định số byte cần bước qua trong bộ nhớ để nhảy sang phần tử tiếp theo trên từng trục.

### 1.1. Công thức Định vị Địa chỉ Byte bằng `strides`
Giả sử ta có ma trận hai chiều $A$ gồm $M$ hàng và $N$ cột, lưu trữ theo chuẩn liên tục hàng của C (*C-contiguous*). Khi đó:
- Bước nhảy giữa hai cột liền kề trong cùng một hàng là:
  $$\text{strides}[1] = \text{itemsize}$$
- Bước nhảy giữa hai hàng liền kề là kích thước của toàn bộ một hàng:
  $$\text{strides}[0] = N \times \text{itemsize}$$

Để truy cập phần tử tại vị trí hàng $i$, cột $j$ (ký hiệu $A[i, j]$), bộ vi xử lý không cần duyệt qua các con trỏ phân tán mà chỉ cần tính toán trực tiếp độ lệch byte (*Byte Offset*) từ con trỏ đầu dữ liệu:
$$\text{Offset}(i, j) = i \times \text{strides}[0] + j \times \text{strides}[1]$$

Với ma trận $A$ kích thước $(4, 3)$, kiểu `int64` (`itemsize = 8`):
- `strides` là $(3 \times 8, 8) = (24, 8)$.
- Vị trí ô $A[3, 1]$ cách đầu mảng một khoảng:
  $$\text{Offset}(3, 1) = 3 \times 24 + 1 \times 8 = 72 + 8 = 80 \text{ bytes}$$

### 1.2. Dung lượng Dữ liệu và Chuyển đổi Kiểu
Dung lượng dữ liệu thuần túy của mảng (chưa tính phần siêu dữ liệu của Python) được tính bằng:
$$\text{nbytes} = \text{size} \times \text{itemsize} = (\prod_{k} \text{shape}[k]) \times \text{itemsize}$$
Với ma trận $A$ kích thước $(4, 3)$ kiểu `int64`, tổng số phần tử là $12$, do đó $\text{nbytes} = 12 \times 8 = 96 \text{ bytes}$.

Nếu ta chuyển đổi kiểu dữ liệu sang `int32` thông qua `A.astype(np.int32)`:
- Kích thước mỗi phần tử giảm một nửa: `itemsize = 4 bytes`.
- Dung lượng dữ liệu giảm một nửa: $\text{nbytes} = 12 \times 4 = 48 \text{ bytes}$.
- Bước nhảy thu hẹp một nửa: `strides = (12, 4)`.

---

## 2. Khung nhìn (View) vs Bản sao (Copy): Bản chất và Hiểm họa

Một trong những ưu điểm vượt trội giúp NumPy xử lý dữ liệu lớn với tốc độ chớp nhoáng là cơ chế **Khung nhìn (*View*)**. Tuy nhiên, nếu không phân biệt rõ khi nào NumPy tạo View và khi nào tạo Bản sao (*Copy*), bạn sẽ gặp phải những lỗi biến đổi dữ liệu ngầm cực kỳ tai hại.

<DataDiagram name="view-copy" />

### 2.1. Lát cắt cơ bản (Slicing) luôn tạo View
Khi bạn cắt lát một mảng bằng cú pháp `start:stop:step` (chẳng hạn `V = A[1::2, 0::2]`), NumPy **không hề sao chép dữ liệu**. Thay vào đó, nó tạo ra một đối tượng `ndarray` mới với siêu dữ liệu riêng (con trỏ đầu trỏ tới ô bắt đầu của lát cắt, `shape` mới và `strides` mới), nhưng **dùng chung nguyên vẹn khối dữ liệu đệm ban đầu**.

Hàm `np.shares_memory(A, V)` sẽ trả về `True`. Nếu bạn thực hiện phép gán `V[0, 0] = -1`, giá trị tương ứng trong mảng gốc `A` sẽ lập tức bị biến đổi thành `-1`.

### 2.2. Chỉ mục mảng nâng cao (Fancy Indexing) luôn tạo Bản sao
Khi bạn truyền một danh sách chỉ số nguyên (như `C = A[:, [1, 2]]`) hoặc một mặt nạ logic Boolean (như `M = A[A > 20]`), NumPy buộc phải gom các phần tử nằm rải rác không theo quy luật bước nhảy tuyến tính cố định. Do đó, NumPy **bắt buộc phải cấp phát một vùng nhớ hoàn toàn mới** và sao chép các giá trị sang:
- `np.shares_memory(A, C)` trả về `False`.
- Phép gán `C[0, 0] = -9` chỉ sửa trên vùng nhớ mới của `C`, mảng gốc `A` hoàn toàn nguyên vẹn.

---

## 3. Quy tắc Duỗi mảng (Broadcasting) Đa chiều

Broadcasting là cơ chế cho phép NumPy thực hiện các phép toán số học giữa các mảng có hình dạng (`shape`) khác nhau mà không cần sao chép lặp lại dữ liệu trong bộ nhớ.

### 3.1. Quy tắc Đối chiếu Kích thước từ Phải sang Trái
Để hai mảng có thể phối hợp tính toán cùng nhau, NumPy tiến hành so sánh kích thước của các trục hình học **từ phải sang trái (bắt đầu từ chiều cuối cùng)**:
1. Hai chiều được coi là tương thích nếu kích thước của chúng **bằng nhau**, hoặc **một trong hai chiều có kích thước bằng 1**.
2. Nếu một mảng có số chiều ít hơn mảng kia, mảng thiếu chiều sẽ được tự động **bổ sung các chiều có kích thước 1 về phía bên trái**.
3. Nếu ở bất kỳ vị trí đối chiếu nào, kích thước hai chiều khác nhau và không có chiều nào bằng 1, NumPy sẽ lập tức ném ra ngoại lệ `ValueError: operands could not be broadcast together`.

### 3.2. Bẫy Kích thước Ma trận và Vector Hàng/Cột
Xét ma trận $A$ có kích thước $(4, 3)$ và vector $d$ có 4 phần tử:
```python
A = np.zeros((4, 3))
d = np.array([10, 20, 30, 40])  # shape = (4,)
```
Nếu bạn viết `A + d`, phép tính sẽ **báo lỗi ngay lập tức**:
- Trục cuối của $A$ là $3$, trục cuối của $d$ là $4$.
- Do $3 \ne 4$ và không có chiều nào bằng 1, quy tắc broadcasting bị vi phạm!

Để cộng theo từng hàng, ta bắt buộc phải nâng vector $d$ thành một ma trận cột có kích thước $(4, 1)$ bằng cú pháp `d[:, np.newaxis]` hoặc `d[:, None]`:
- Chiều của $A$: `(4, 3)`
- Chiều của $d$: `(4, 1)`
- Đối chiếu từ phải sang trái: trục cuối ($3$ và $1$) tương thích; trục trước ($4$ và $4$) tương thích $\to$ Phép tính hợp lệ!

### 3.3. Bẫy Trừ Trung bình theo Hàng và Tham số `keepdims=True`
Một bài toán chuẩn hóa dữ liệu kinh điển là trừ mỗi hàng của ma trận cho giá trị trung bình của chính hàng đó (*Row Centering*):
$$\tilde{x}_{ij} = x_{ij} - \bar{x}_{i*} \quad \text{với } \bar{x}_{i*} = \frac{1}{N}\sum_{j=1}^N x_{ij}$$

Nếu viết:
```python
tb = A.mean(axis=1)  # shape = (4,) -> Mảng 1 chiều!
ket_qua = A - tb     # LỖI NGHIỆM TRỌNG HOẶC SAI KẾT QUẢ!
```
- Nếu ma trận không vuông ($4 \times 3$), lệnh trên sẽ ném ra lỗi `ValueError` như đã phân tích.
- Nếu ma trận vô tình là ma trận vuông $3 \times 3$, `A - tb` sẽ **chạy được mà không báo lỗi**, nhưng do đối chiếu từ phải sang trái, mảng `(3,)` sẽ bị ngầm hiểu thành `(1, 3)` và trừ dọc theo cột thay vì trừ theo hàng! Toàn bộ kết quả khoa học bị sai lệch âm thầm.

Cách xử lý chuẩn mực của chuyên gia là luôn sử dụng `keepdims=True`:
```python
tb = A.mean(axis=1, keepdims=True)  # shape = (4, 1)
ket_qua = A - tb                    # Bảo đảm trừ chính xác từng hàng!
```

---

## 4. Tại sao Vector hóa Lại Nhanh Hơn Vòng lặp Python?

Để chứng minh sức mạnh của NumPy, hãy so sánh ba cách tiếp cận nhân đôi từng phần tử trên mảng $100,000$ số nguyên:
1. **Cách 1**: Vòng lặp trên danh sách Python: `[x * 2 for x in ds]`.
2. **Cách 2**: Vòng lặp `for` trên mảng NumPy: `[x * 2 for x in arr]`.
3. **Cách 3**: Phép toán vector hóa của NumPy: `arr * 2`.

Kết quả đo đạc thực nghiệm trên phần cứng máy tính hiện đại:
- Cách 1 (`for` trên list): mất khoảng $4,500 \mu\text{s}$.
- Cách 2 (`for` trên ndarray): mất khoảng $8,200 \mu\text{s}$ (thậm chí **chậm gần gấp đôi** so với danh sách thuần!).
- Cách 3 (`arr * 2` vector hóa): chỉ mất khoảng $35 \mu\text{s}$ (**nhanh hơn hơn 120 lần** so với vòng lặp!).

### Ba lý do cốt lõi tạo nên sự vượt trội:
1. **Tránh chi phí đóng/mở hộp (*Unboxing Overhead*)**: Trong vòng lặp Python, mỗi khi truy cập một phần tử trong mảng NumPy, CPython phải bóc tách giá trị số nguyên 64-bit từ bộ nhớ C rồi đóng gói nó vào một đối tượng `PyLongObject` hoàn chỉnh trên heap, rồi lại giải nén khi tính toán. Chi phí này làm vòng lặp `for` trên `ndarray` trở nên chậm chạp một cách thảm hại.
2. **Tính cục bộ bộ nhớ (*Spatial Locality*)**: Vùng đệm liên tục cho phép CPU nạp thẳng các khối 64 bytes (Cache Line) vào bộ nhớ đệm L1/L2, giảm thiểu tối đa hiện tượng trượt bộ nhớ đệm (*Cache Miss*).
3. **Chỉ thị SIMD (Single Instruction, Multiple Data)**: Các bộ vi xử lý hiện đại sở hữu các thanh ghi mở rộng (AVX2, AVX-512). Phép toán `arr * 2` biên dịch thành mã máy C có thể nhân đồng thời 4 đến 8 số nguyên 64-bit chỉ trong một xung nhịp CPU duy nhất.

---

## 5. Bài tập Thực chiến Phòng Lab 03 (100% Nội dung Lab)

Dưới đây là toàn bộ các bài tập thực hành từ Lab 03, với đầy đủ yêu cầu, hợp đồng hàm, kiểm chứng dữ liệu và lời giải hai tầng chi tiết.

### Dữ liệu mẫu dùng trong bài tập
Ma trận chuẩn $A$ gồm 4 hàng, 3 cột:
```python
import numpy as np

A = np.array([[10, 12, 11],
              [20, 21, 24],
              [30, 33, 31],
              [40, 44, 42]], dtype=np.int64)
```

---

### Bài tập 1 (Q1): Khảo sát Cấu trúc Bố trí Ô nhớ và Độ lệch Byte
::: exercise Phân tích siêu dữ liệu và tính byte offset của phần tử
Viết hàm `array_layout(matrix: np.ndarray, row: int, col: int) -> dict`.
Yêu cầu:
- Nhận ma trận số nguyên 2 chiều C-contiguous; `row`, `col` là các chỉ số hợp lệ.
- Trả về từ điển có đúng các khóa:
  - `shape`: Kích thước hình học của ma trận.
  - `itemsize`: Số byte của mỗi phần tử.
  - `nbytes`: Tổng dung lượng dữ liệu tính bằng byte.
  - `strides`: Tuple bước nhảy byte trên từng trục.
  - `offset`: Khoảng cách byte từ đầu mảng đến phần tử `[row, col]`.
  - `int32_array`: Mảng chứa cùng giá trị nhưng có kiểu `int32`.
- Không ghi cứng kích thước hay kiểu của ma trận $A$. Thử nghiệm với `A[3, 1]`.
:::

::: solution
#### Lời giải chi tiết:
```python
import numpy as np

def array_layout(matrix: np.ndarray, row: int, col: int) -> dict:
    # 1. Trích xuất siêu dữ liệu mảng
    shape = matrix.shape
    itemsize = matrix.itemsize
    nbytes = matrix.nbytes
    strides = matrix.strides
    
    # 2. Tính toán độ lệch byte theo công thức bước nhảy
    offset = row * strides[0] + col * strides[1]
    
    # 3. Ép kiểu an toàn sang int32
    int32_arr = matrix.astype(np.int32)
    
    return {
        "shape": shape,
        "itemsize": itemsize,
        "nbytes": nbytes,
        "strides": strides,
        "offset": offset,
        "int32_array": int32_arr
    }
```

#### Dự đoán và Phân tích bản chất:
- Với mảng $A$ ban đầu:
  - `shape = (4, 3)`, `itemsize = 8` bytes, `nbytes = 4 * 3 * 8 = 96` bytes.
  - `strides = (3 * 8, 8) = (24, 8)`.
  - Phần tử $A[3, 1]$ có độ lệch: $3 \times 24 + 1 \times 8 = 80$ bytes.
- Khi chuyển sang `int32`:
  - `itemsize` giảm từ 8 xuống 4 bytes.
  - `nbytes` giảm từ 96 xuống 48 bytes.
  - `strides` đổi thành $(3 \times 4, 4) = (12, 4)$.
:::

---

### Bài tập 2 (Q2): Lát cắt Tạo Khung nhìn (Slicing View)
::: exercise Khảo sát bước nhảy và chia sẻ bộ nhớ của khung nhìn
Viết hàm `slice_view(matrix: np.ndarray) -> dict`.
Yêu cầu:
- Nhận ma trận số nguyên 2 chiều có ít nhất 4 hàng, 3 cột.
- Sử dụng slicing lấy các hàng bắt đầu từ 1 với bước nhảy 2 (`1::2`), và các cột bắt đầu từ 0 với bước nhảy 2 (`0::2`).
- Trả về từ điển chứa:
  - `view`: Mảng kết quả sau khi cắt lát (bắt buộc phải chia sẻ bộ nhớ với ma trận gốc).
  - `shape`: Tuple kích thước của view.
  - `strides`: Tuple bước nhảy của view.
  - `offset_v11`: Độ lệch byte tính từ **đầu ma trận gốc** đến phần tử `view[1, 1]`.
  - `shares_memory`: Boolean kiểm tra việc dùng chung bộ nhớ với ma trận gốc.
:::

::: solution
#### Lời giải chi tiết:
```python
import numpy as np

def slice_view(matrix: np.ndarray) -> dict:
    # Cắt lát bước nhảy 2 trên cả 2 chiều
    v = matrix[1::2, 0::2]
    
    # Phần tử view[1, 1] thực chất tương ứng với ô matrix[3, 2] trong ma trận gốc
    # Do đó offset được tính từ đầu ma trận gốc: 3 * strides[0] + 2 * strides[1]
    offset_v11 = 3 * matrix.strides[0] + 2 * matrix.strides[1]
    
    return {
        "view": v,
        "shape": v.shape,
        "strides": v.strides,
        "offset_v11": offset_v11,
        "shares_memory": np.shares_memory(matrix, v)
    }
```

#### Phân tích sư phạm:
- Với ma trận $A$, lát cắt lấy hàng 1, 3 và cột 0, 2:
  $$\text{view} = \begin{bmatrix} 20 & 24 \\ 40 & 42 \end{bmatrix}$$
- Kích thước của view là `(2, 2)`.
- Do bước nhảy trên mỗi trục đều tăng gấp đôi, `strides` của view trở thành $(24 \times 2, 8 \times 2) = (48, 16)$.
- Phần tử `view[1, 1]` là số $42$, nằm tại vị trí hàng 3 cột 2 của $A$. Độ lệch byte từ đầu mảng $A$ là:
  $$\text{Offset} = 3 \times 24 + 2 \times 8 = 72 + 16 = 88 \text{ bytes}$$
- `np.shares_memory(A, v)` trả về `True`.
:::

---

### Bài tập 3 (Q3): Phân biệt View và Copy khi Thao tác Cột
::: exercise Trích xuất cột an toàn chống biến đổi dữ liệu ngầm
Quan sát đoạn mã thực nghiệm sau:
```python
B = A.copy()
V = B[:, 1:3]       # Lát cắt slicing
C = B[:, [1, 2]]    # Chỉ mục mảng fancy indexing
C[0, 0] = -9
print("Sau khi sửa C:", B[0])
V[0, 0] = -1
print("Sau khi sửa V:", B[0])
```
1. Dự đoán giá trị của `B[0]` sau mỗi lần gán và giải thích nguyên nhân.
2. Viết hàm `copy_columns(matrix: np.ndarray) -> np.ndarray` nhận ma trận số hữu hạn và trả về một bản sao độc lập chứa cột 1 và cột 2, bảo đảm việc chỉnh sửa kết quả không bao giờ làm thay đổi ma trận đầu vào.
:::

::: solution
#### 1. Dự đoán và Giải thích:
- **Sau khi gán `C[0, 0] = -9`**: `B[0]` vẫn giữ nguyên là `[10, 12, 11]`.
  - *Giải thích*: Cú pháp `B[:, [1, 2]]` truyền một danh sách chỉ số cột, kích hoạt cơ chế Fancy Indexing. NumPy sao chép dữ liệu ra một vùng nhớ mới cho `C`, do đó sửa `C` hoàn toàn không ảnh hưởng tới `B`.
- **Sau khi gán `V[0, 0] = -1`**: `B[0]` bị biến đổi thành `[10, -1, 11]`.
  - *Giải thích*: Cú pháp `B[:, 1:3]` là lát cắt cơ bản, tạo ra một View dùng chung vùng đệm bộ nhớ với `B`. Phần tử `V[0, 0]` trỏ thẳng vào ô `B[0, 1]`, do đó phép gán này làm mảng gốc `B` bị sửa đổi ngay lập tức.

#### 2. Hiện thực hàm `copy_columns`:
```python
import numpy as np

def copy_columns(matrix: np.ndarray) -> np.ndarray:
    # Cách 1: Slicing kết hợp gọi tường minh .copy()
    return matrix[:, 1:3].copy()

    # Cách 2: Hoặc tận dụng cơ chế Fancy Indexing tự sao chép
    # return matrix[:, [1, 2]]
```
:::

---

### Bài tập 4 (Q4): Kỹ thuật Chọn Phần tử: Mask, Fancy Indexing và Lưới `np.ix_`
::: exercise Trích xuất phần tử không dùng vòng lặp
Viết hàm `select_elements(matrix: np.ndarray) -> dict`.
Yêu cầu không sử dụng vòng lặp `for` hay comprehension, trả về từ điển chứa:
- `so_chan`: Mảng 1 chiều chứa tất cả các số chẵn trong ma trận, sắp xếp theo thứ tự duyệt từng hàng (dùng mặt nạ Boolean).
- `hai_o`: Mảng 1 chiều gồm đúng hai phần tử tại tọa độ `[0, 1]` và `[2, 2]` (dùng hai mảng chỉ mục).
- `bon_o`: Ma trận con kích thước $2 \times 2$ gồm giao điểm của các hàng `[0, 2]` và các cột `[1, 2]` (dùng `np.ix_`).
:::

::: solution
#### Lời giải chi tiết:
```python
import numpy as np

def select_elements(matrix: np.ndarray) -> dict:
    # 1. Lọc số chẵn bằng mặt nạ Boolean (kết quả co về 1D)
    mask = (matrix % 2 == 0)
    so_chan = matrix[mask]
    
    # 2. Chọn 2 ô rời rạc bằng Fancy Indexing theo cặp tọa độ (hàng, cột)
    hai_o = matrix[[0, 2], [1, 2]]
    
    # 3. Chọn vùng giao lưới 2x2 bằng tích Descartes của np.ix_
    bon_o = matrix[np.ix_([0, 2], [1, 2])]
    
    return {
        "so_chan": so_chan,
        "hai_o": hai_o,
        "bon_o": bon_o
    }
```

#### Phân tích hình học về Shape:
- `so_chan` có `shape = (8,)`: Mặt nạ logic làm phẳng dữ liệu vì số lượng phần tử thỏa mãn điều kiện ở mỗi hàng có thể không đồng đều.
- `hai_o` có `shape = (2,)`: Truyền hai mảng chỉ mục `[0, 2]` và `[1, 2]` chọn lần lượt hai điểm $(0, 1)$ và $(2, 2)$ trong không gian số học.
- `bon_o` có `shape = (2, 2)`: `np.ix_` tạo ra tích Descartes giữa 2 hàng và 2 cột, trả về một khối ma trận con $2 \times 2$.
:::

---

### Bài tập 5 (Q5): Phép toán Cộng Tích lũy Hai Chiều bằng Broadcasting
::: exercise Duỗi mảng hai chiều không dùng vòng lặp
Cho ma trận $A$ kích thước $(4, 3)$. Viết hàm:
`broadcast_add(matrix: np.ndarray, column_add: np.ndarray, row_add: np.ndarray) -> np.ndarray`
Trong đó:
- `column_add` là mảng 1D dài bằng số cột, dùng để cộng vào từng cột tương ứng.
- `row_add` là mảng 1D dài bằng số hàng, dùng để cộng vào từng hàng tương ứng.
- Trả về ma trận cùng kích thước với `matrix`, trong đó mỗi ô:
  $$\text{Result}[i, j] = \text{matrix}[i, j] + \text{column\_add}[j] + \text{row\_add}[i]$$
:::

::: solution
#### Lời giải chi tiết:
```python
import numpy as np

def broadcast_add(matrix: np.ndarray, column_add: np.ndarray, row_add: np.ndarray) -> np.ndarray:
    # 1. column_add có shape (N,), cộng vào matrix (M, N) tự động khớp trục cuối
    # 2. row_add có shape (M,), cần mở rộng thành (M, 1) bằng [:, None] để cộng dọc theo hàng
    return matrix + column_add + row_add[:, np.newaxis]
```

#### Phân tích vì sao `matrix + row_add` bị lỗi:
- `matrix` có kích thước $(4, 3)$.
- `row_add` là vector 1 chiều có kích thước $(4,)$.
- Theo quy tắc đối chiếu từ phải sang trái, chiều cuối cùng của ma trận là $3$, chiều cuối của vector là $4$. Vì $3 \ne 4$ và không có chiều nào bằng 1, NumPy không thể tự đoán lập trình viên muốn cộng dọc hay cộng ngang và ném ra lỗi `ValueError`.
- Việc thêm trục `row_add[:, np.newaxis]` đưa kích thước về $(4, 1)$. Khi đó chiều cuối là $1$ đối chiếu với $3$ sẽ tự động được sao chép mở rộng (duỗi mảng) hợp lệ.
:::

---

### Bài tập 6 (Q6): Chuẩn hóa Dữ liệu theo Hàng (Row Centering)
::: exercise Phát hiện và khắc phục lỗi lệch trục tính toán
Cho mảng giá phòng qua 3 kỳ thu thập:
```python
gia = np.array([[40, 50, 60],
                [60, 60, 60],
                [30, 60, 90]], dtype=np.float64)
```
Một kỹ sư viết đoạn mã sau để trừ mỗi hàng cho giá trị trung bình của chính hàng đó:
```python
tb_sai = gia.mean(axis=1)
sai = gia - tb_sai
print(sai)
```
1. Hãy chạy thử và giải thích vì sao đoạn mã trên cho kết quả sai hoàn toàn về mặt logic toán học.
2. Viết hàm `center_rows(prices: np.ndarray) -> tuple[np.ndarray, np.ndarray]` trả về `(trung_binh_hang, do_lech)` với `trung_binh_hang` có shape `(M, 1)` và `do_lech` có shape `(M, N)`.
:::

::: solution
#### 1. Giải phẫu lỗi sai:
- Lệnh `gia.mean(axis=1)` tính trung bình theo hàng, cho ra các giá trị $[50, 60, 60]$, nhưng trả về mảng 1 chiều có `shape = (3,)`.
- Do ma trận `gia` là ma trận vuông $(3, 3)$, khi thực hiện `gia - tb_sai`, NumPy đối chiếu trục cuối: vector `(3,)` được ngầm coi là vector hàng `(1, 3)` và **bị trừ dọc theo từng cột**!
- Kết quả thu được không phải là trừ trung bình của từng chỗ ở, mà là lấy từng chỗ ở trừ đi vector $[50, 60, 60]$, dẫn đến độ lệch của hàng đầu tiên bị tính sai thành:
  $$[40 - 50, 50 - 60, 60 - 60] = [-10, -10, 0] \quad (\text{Kết quả đúng phải là } [-10, 0, 10])$$

#### 2. Hiện thực hàm `center_rows` chuẩn xác:
```python
import numpy as np

def center_rows(prices: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    # Sử dụng keepdims=True để duy trì shape (M, 1)
    trung_binh_hang = prices.mean(axis=1, keepdims=True)
    
    # Broadcasting (M, N) - (M, 1) bảo đảm trừ chính xác từng hàng
    chenh_lech = prices - trung_binh_hang
    
    return trung_binh_hang, chenh_lech
```

Kiểm tra bất biến toán học: Trung bình cộng các độ lệch trên mỗi hàng sau khi chuẩn hóa bắt buộc phải xấp xỉ bằng 0:
```python
assert np.allclose(chenh_lech.mean(axis=1), 0, atol=1e-12)
```
:::

---

### Bài tập 7 (Q7): Đo lường Thực nghiệm Hiệu năng Tính toán
::: exercise Đo thời gian thực thi và so sánh cơ chế hoạt động
Chạy đoạn mã đo đạc sau trên hệ thống của bạn và quan sát kết quả:
```python
from timeit import repeat
import numpy as np

def nhan_list(xs):
    return [v * 2 for v in xs]

def nhan_for_array(x):
    return [v * 2 for v in x]

def nhan_array(x):
    return x * 2

for n in (10, 100_000):
    x = np.arange(n, dtype=np.int64)
    xs = x.tolist()
    so_lan = 100 if n == 10 else 5
    print(f"\n--- Quy mô n = {n:,} ---")
    for ten, ham, dau_vao in [("for trên list", nhan_list, xs),
                             ("for trên ndarray", nhan_for_array, x),
                             ("Vector hóa ndarray", nhan_array, x)]:
        t = min(repeat(lambda: ham(dau_vao), number=so_lan, repeat=3)) / so_lan
        print(f"{ten:<22}: {t * 1e6:>10.2f} µs/lần")
```
Trả lời các câu hỏi:
1. Vì sao vòng lặp `for` duyệt trên `ndarray` lại chạy chậm hơn cả `for` trên danh sách Python thuần?
2. Phép toán vector hóa nhanh hơn nhờ những yếu tố nào ở tầng phần cứng?
:::

::: solution
#### Phân tích & Trả lời từ Giảng viên:
1. **Nguyên nhân vòng `for` trên `ndarray` chạy chậm nhất**:
   - Trong `list`, các con trỏ đã trỏ sẵn tới các đối tượng `PyObject`. Khi lặp qua danh sách, Python chỉ cần tăng con trỏ và lấy trực tiếp đối tượng ra tính toán.
   - Trong `ndarray`, dữ liệu được lưu dưới dạng số nguyên C thô (primitive int64). Mỗi khi vòng lặp `for` duyệt qua một chỉ mục, Python bắt buộc phải thực hiện thao tác **đóng hộp (*boxing*)**: cấp phát một vùng nhớ heap mới, tạo đối tượng `PyLongObject` và chép giá trị số nguyên vào đó. Việc cấp phát hàng trăm nghìn đối tượng ngắn hạn liên tục làm nghẽn bộ quản lý bộ nhớ của Python, khiến hiệu năng sụt giảm nghiêm trọng.

2. **Cơ chế gia tốc của phép toán vector hóa**:
   - Phép toán `x * 2` thực thi hoàn toàn trong thư viện C đã được biên dịch tối ưu hóa cao độ, không cần gọi tới trình thông dịch Python trong suốt quá trình duyệt mảng.
   - Vùng nhớ liên tục kích hoạt bộ nạp trước (*hardware prefetcher*) của CPU, đưa dữ liệu vào bộ nhớ đệm L1/L2 với tốc độ băng thông cực đại.
   - Trình biên dịch C tự động vector hóa mã nguồn bằng các thanh ghi SIMD, nhân đồng loạt nhiều phần tử cùng lúc trong một chu kỳ xung nhịp.
:::

---

### Bài tập 8 (Q8): Thống kê Phân phối Giá và Kỹ thuật Lấy mẫu Ngẫu nhiên
::: exercise Tính toán thống kê mô tả và trích xuất mẫu kiểm tra
Cho mảng giá phòng gồm 5 quan sát (USD/đêm):
```python
gia_dem = np.array([40, 50, 60, 70, 380], dtype=np.float64)
```
Viết hàm:
`price_statistics(prices: np.ndarray, threshold: float = 70.0, sample_size: int = 3, seed: int = 42) -> dict`
Yêu cầu:
- Tính `mean`, `median`, và độ lệch chuẩn tổng thể `std` (với `ddof=0`).
- Tính tỷ lệ `share` các phòng có giá $\le threshold$ (thang đo $0.0 - 1.0$).
- Sử dụng bộ sinh số ngẫu nhiên mới của NumPy: `rng = np.random.default_rng(seed)`.
- Rút ngẫu nhiên một mẫu gồm `sample_size` phần tử không hoàn lại (`replace=False`) thông qua hàm `rng.choice`.
- Trả về từ điển gồm: `mean`, `median`, `std`, `share`, `indices` (mảng chỉ số), `sample` (mảng giá lấy mẫu), và `sample_mean`.
:::

::: solution
#### Lời giải chuẩn mực:
```python
import numpy as np

def price_statistics(prices: np.ndarray, threshold: float = 70.0, sample_size: int = 3, seed: int = 42) -> dict:
    # 1. Thống kê mô tả toàn thể
    mean_val = float(np.mean(prices))
    median_val = float(np.median(prices))
    std_val = float(np.std(prices, ddof=0))
    
    # 2. Tỷ lệ giá dưới ngưỡng
    share_val = float(np.mean(prices <= threshold))
    
    # 3. Lấy mẫu ngẫu nhiên không hoàn lại có tái lập
    rng = np.random.default_rng(seed)
    indices = rng.choice(len(prices), size=sample_size, replace=False)
    sample_arr = prices[indices]
    sample_mean_val = float(np.mean(sample_arr))
    
    return {
        "mean": mean_val,
        "median": median_val,
        "std": std_val,
        "share": share_val,
        "indices": indices,
        "sample": sample_arr,
        "sample_mean": sample_mean_val
    }
```
:::

---

### Bài tập 9 (Thảo luận & Diễn giải): Bản chất Thống kê và Kỷ luật Xử lý Ngoại lai
::: exercise Bốn câu hỏi chuyên sâu về phương pháp luận nghiên cứu
Dựa trên kết quả tính toán của mảng giá `[40, 50, 60, 70, 380]`, hãy trả lời:
1. Trong báo cáo phân tích thị trường, bạn sẽ chọn giá trị trung bình ($120$) hay trung vị ($60$) để mô tả mức giá điển hình của các chỗ ở này? Vì sao?
2. Có nên loại bỏ mức giá $380$ chỉ vì nó cao vượt trội so với các phòng còn lại hay không?
3. Trung bình mẫu với cỡ mẫu $3$ có nhất thiết bằng trung bình toàn thể không? Việc cố định hạt giống `seed=42` có bảo đảm mẫu thu được mang tính đại diện cho toàn bộ thị trường hay không?
4. Khi ta đã nắm trong tay toàn bộ dữ liệu hợp lệ, việc lấy mẫu ngẫu nhiên có còn cần thiết để tính toán chỉ số hay không? Khi nào việc rút mẫu vẫn phát huy giá trị to lớn?
:::

::: solution
#### Luận giải Sư phạm từ Giảng viên:

1. **Lựa chọn Trung vị làm đại diện thị trường**:
   - Bốn trong số năm căn phòng có giá nằm trong khoảng từ $40$ đến $70$ USD, và trung vị là $60$ USD. Mức giá trung bình cộng bị kéo vọt lên $120$ USD hoàn toàn là do sự hiện diện của một căn phòng duy nhất có giá $380$ USD.
   - Con số $120$ USD không phản ánh đúng thực tế của đại đa số người tiêu dùng (không có bất kỳ căn phòng nào có giá quanh ngưỡng $120$ USD). Vì vậy, trung vị là chỉ số trung thực và bền vững nhất để mô tả mức giá điển hình của phân khúc này.

2. **Không được tùy tiện xóa bỏ ngoại lai $380$**:
   - Con số $380$ USD hoàn toàn có thể là một quan sát thực tế hợp lệ: đó là một căn penthouse cao cấp, một biệt thự nguyên căn hoặc một phòng hạng sang phục vụ khách VIP.
   - Ngoại lai là dữ liệu thật, không phải lỗi nhập liệu. Nếu ta xóa bỏ nó, tổng dung lượng thị trường và doanh thu thực tế sẽ bị tính thiếu hụt nghiêm trọng. Thay vì xóa bỏ, nhà phân tích chuyên nghiệp sẽ tiến hành phân tầng thị trường (*Market Segmentation*): tách riêng nhóm phòng tiêu chuẩn ($40 - 70$) và nhóm phòng cao cấp ($380$) để đánh giá độc lập.

3. **Bản chất của Hạt giống ngẫu nhiên (*Random Seed*)**:
   - Trung bình mẫu rút ra ngẫu nhiên (chẳng hạn 3 phần tử $[70, 40, 60]$ có trung bình là $56.67$) thường sẽ khác với trung bình toàn thể ($120$) do sai số chọn mẫu (*Sampling Error*).
   - Việc cố định `seed = 42` **chỉ bảo đảm tính tái lập của mã nguồn (*Reproducibility*)** để hai lập trình viên chạy mã trên hai máy tính khác nhau đều thu được cùng một chuỗi kết quả. Cố định seed hoàn toàn **không bảo đảm tính đại diện của mẫu**. Nếu không may hạt giống ngẫu nhiên bốc trúng ngoại lai $380$, trung bình mẫu có thể bị méo mó nghiêm trọng.

4. **Giá trị của việc rút mẫu trong Kỷ nguyên Dữ liệu Lớn**:
   - Khi đã có toàn bộ dữ liệu sạch trong bộ nhớ, ta không cần lấy mẫu để tính toán các chỉ số thống kê mô tả vì thuật toán vector hóa có thể quét qua hàng chục triệu dòng trong vài giây.
   - Tuy nhiên, kỹ thuật lấy mẫu ngẫu nhiên vẫn đóng vai trò sinh tử trong hai trường hợp:
     - **Thẩm định chất lượng thủ công (*Sanity Check / QA Audit*)**: Con người không thể đọc hết một triệu dòng dữ liệu. Ta rút ngẫu nhiên $100$ bản ghi để chuyên viên nghiệp vụ kiểm tra chéo tính hợp lý.
     - **Phát triển đường ống xử lý (*Prototyping*)**: Khi xây dựng các mô hình huấn luyện phức tạp hoặc biến đổi chuỗi tốn kém, ta chạy thử nghiệm trên một mẫu ngẫu nhiên $1\%$ để tinh chỉnh mã nguồn nhanh chóng trước khi đưa toàn bộ dữ liệu khổng lồ vào vận hành.
:::

---

## 6. Tổng kết Bài học

1. **Hiểu rõ bộ nhớ**: `ndarray` là một khối đệm liên tục được điều khiển bởi siêu dữ liệu `shape`, `dtype` và `strides`. Mọi phép tính toán địa chỉ đều quy về bước nhảy byte tuyến tính.
2. **Cảnh giác trước View**: Slicing luôn tạo khung nhìn chia sẻ bộ nhớ. Bất kỳ phép gán nào trên View cũng sẽ làm biến dạng mảng gốc. Khi cần độc lập, hãy gọi `.copy()` hoặc dùng Fancy Indexing.
3. **Thành thạo Broadcasting**: Luôn so sánh kích thước từ phải sang trái. Sử dụng `keepdims=True` hoặc thêm trục bằng `[:, np.newaxis]` để kiểm soát chính xác chiều tính toán.
4. **Tuyệt đối không dùng vòng `for` trên mảng**: Hãy tận dụng các hàm phổ quát `ufunc` và toán tử vector hóa để kích hoạt sức mạnh tính toán song song SIMD ở tầng mã máy C.
