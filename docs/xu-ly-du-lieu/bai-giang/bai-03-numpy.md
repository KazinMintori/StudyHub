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
- Đối chiếu từ phải sang trái: Trục cuối ($3$ và $1$) tương thích; trục trước ($4$ và $4$) tương thích $\to$ Phép tính hợp lệ!

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
- Cách 1 (`for` trên list): Mất khoảng $4,500 \mu\text{s}$.
- Cách 2 (`for` trên ndarray): Mất khoảng $8,200 \mu\text{s}$ (thậm chí **chậm gần gấp đôi** so với danh sách thuần!).
- Cách 3 (`arr * 2` vector hóa): Chỉ mất khoảng $35 \mu\text{s}$ (**nhanh hơn hơn 120 lần** so với vòng lặp!).

### Ba lý do cốt lõi tạo nên sự vượt trội:
1. **Tránh chi phí đóng/mở hộp (*Unboxing Overhead*)**: Trong vòng lặp Python, mỗi khi truy cập một phần tử trong mảng NumPy, CPython phải bóc tách giá trị số nguyên 64-bit từ bộ nhớ C rồi đóng gói nó vào một đối tượng `PyLongObject` hoàn chỉnh trên heap, rồi lại giải nén khi tính toán. Chi phí này làm vòng lặp `for` trên `ndarray` trở nên chậm chạp một cách thảm hại.
2. **Tính cục bộ bộ nhớ (*Spatial Locality*)**: Vùng đệm liên tục cho phép CPU nạp thẳng các khối 64 bytes (Cache Line) vào bộ nhớ đệm L1/L2, giảm thiểu tối đa hiện tượng trượt bộ nhớ đệm (*Cache Miss*).
3. **Chỉ thị SIMD (Single Instruction, Multiple Data)**: Các bộ vi xử lý hiện đại sở hữu các thanh ghi mở rộng (AVX2, AVX-512). Phép toán `arr * 2` biên dịch thành mã máy C có thể nhân đồng thời 4 đến 8 số nguyên 64-bit chỉ trong một xung nhịp CPU duy nhất.

---

## 5. Bài tập Thực chiến Phòng Lab 03 (100% Nội dung Lab) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 6. Tổng kết Bài học

1. **Hiểu rõ bộ nhớ**: `ndarray` là một khối đệm liên tục được điều khiển bởi siêu dữ liệu `shape`, `dtype` và `strides`. Mọi phép tính toán địa chỉ đều quy về bước nhảy byte tuyến tính.
2. **Cảnh giác trước View**: Slicing luôn tạo khung nhìn chia sẻ bộ nhớ. Bất kỳ phép gán nào trên View cũng sẽ làm biến dạng mảng gốc. Khi cần độc lập, hãy gọi `.copy()` hoặc dùng Fancy Indexing.
3. **Thành thạo Broadcasting**: Luôn so sánh kích thước từ phải sang trái. Sử dụng `keepdims=True` hoặc thêm trục bằng `[:, np.newaxis]` để kiểm soát chính xác chiều tính toán.
4. **Tuyệt đối không dùng vòng `for` trên mảng**: Hãy tận dụng các hàm phổ quát `ufunc` và toán tử vector hóa để kích hoạt sức mạnh tính toán song song SIMD ở tầng mã máy C.
