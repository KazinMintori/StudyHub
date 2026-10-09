---
course: xu-ly-du-lieu
lecture: bai-03-numpy
section: lecture
title: "NumPy & tư duy vector hóa"
prerequisites: ["mang","chi-muc","con-tro","vector-hoa","broadcasting"]
lessonStatus: ready
description: "Đọc shape, dtype và trục của ndarray; tính bằng ufunc, broadcasting và kiểm tra dữ liệu dùng chung."
---

Nếu Python thuần túy là một người quản lý linh hoạt có thể làm mọi việc, thì NumPy chính là cỗ máy gia công công nghiệp hạng nặng. Hầu như mọi thư viện dữ liệu và trí tuệ nhân tạo hiện đại — từ pandas, SciPy, Scikit-learn cho đến PyTorch hay TensorFlow — đều được xây dựng trên nền tảng cốt lõi của NumPy.

Để làm việc hiệu quả với dữ liệu lớn, ta không thể tiếp tục tư duy theo lối mòn của các vòng lặp tuần tự `for` và `while`. Người lập trình dữ liệu cần phải bước sang một cảnh giới tư duy mới: **Tư duy vector hóa** (Vectorized Thinking) — nhìn nhận dữ liệu dưới dạng các khối hình học đa chiều, thực thi phép toán đồng loạt trên toàn bộ không gian số liệu, và nắm rõ cách thức phần cứng máy tính luân chuyển dữ liệu trong bộ nhớ đệm.

## 1. Bản chất bộ nhớ và giải phẫu mảng đa chiều

Tại sao một vòng lặp tính toán trên danh sách Python lại chậm hơn từ 50 đến 100 lần so với một phép toán tương đương trên mảng NumPy?

Câu trả lời nằm ở kiến trúc bộ nhớ:
- Trong Python tiêu chuẩn, mỗi con số nguyên là một đối tượng `PyObject` hoàn chỉnh tiêu tốn tới 28 bytes bộ nhớ, chứa đựng thông tin kiểu dữ liệu và số lượng tham chiếu. Một `list` của Python thực chất là một mảng chứa các con trỏ trỏ tới những đối tượng nằm rải rác khắp nơi trong bộ nhớ heap. Khi duyệt qua danh sách, bộ vi xử lý (CPU) phải liên tục nhảy cóc qua các địa chỉ nhớ ngẫu nhiên (cache miss) và kiểm tra lại kiểu dữ liệu ở từng bước chân.
- Ngược lại, mảng đa chiều **`ndarray`** của NumPy lưu trữ toàn bộ các phần tử trong một khối bộ nhớ liên tục (contiguous memory buffer). Mọi phần tử đều có cùng một kiểu dữ liệu cố định (**`dtype`**). Điều này cho phép CPU nạp thẳng cả khối dữ liệu vào bộ nhớ đệm tốc độ cao (L1/L2 cache) và tận dụng các tập lệnh SIMD (Single Instruction, Multiple Data) để thực thi hàng loạt phép tính cùng một nhịp xung đồng hồ.

Hãy khảo sát mảng biểu diễn số lượng bán ra của 2 quầy hàng cho 3 sản phẩm:

```python
import numpy as np

A = np.array([[10, 20, 30], [40, 50, 60]], dtype=np.int64)
print(A.shape, A.ndim, A.size)    # (2, 3) 2 6
print(A.dtype)                  # int64
```

Ba thuộc tính hình học cơ bản của một mảng:
- **`shape = (2, 3)`**: Kích thước không gian của mảng gồm 2 hàng và 3 cột.
- **`ndim = 2`**: Số chiều hình học (số trục).
- **`size = 6`**: Tổng số phần tử bên trong mảng ($2 \times 3 = 6$).

Một điểm tế nhị mà sinh viên mới học thường nhầm lẫn: mảng 1 chiều `np.array([1, 2, 3])` có `shape = (3,)` và `ndim = 1`. Nó chỉ là một chuỗi 3 phần tử tuyến tính, hoàn toàn không phải là một ma trận hàng $1 \times 3$ (`shape = (1, 3)`) hay một ma trận cột $3 \times 1$ (`shape = (3, 1)`). Nhầm lẫn giữa vector 1 chiều và ma trận 2 chiều là nguồn cơn của rất nhiều lỗi sai kích thước khi tính toán đại số.

Về kiểu dữ liệu **`dtype`**, vì NumPy sử dụng kích thước bit cố định, ta phải luôn lưu ý đến hiện tượng **tràn số nguyên** (integer overflow):

```python
x = np.array([100], dtype=np.int8)
print((x * 2).tolist())          # [-56]: tràn int8
print((x.astype(np.int64) * 2).tolist())  # [200]
```

Kiểu `int8` chỉ biểu diễn được các số nguyên trong đoạn $[-128, 127]$. Khi lấy $100 \times 2 = 200$, con số vượt qua ngưỡng 127 và bị quay vòng thành $-56$. Đáng sợ hơn cả, NumPy thực hiện phép tính trong im lặng mà không hề ném ra cảnh báo hay ngoại lệ nào. Nếu dữ liệu đã bị tràn số, việc bạn gọi `.astype(np.int64)` sau đó chỉ đơn thuần là ép kiểu con số sai $-56$ sang kiểu lớn hơn, chứ không thể phục hồi lại con số $200$ ban đầu. Do đó, việc ép kiểu sang độ rộng phù hợp phải luôn được thực hiện **trước khi** tính toán.

## 2. Tư duy vector hóa và hàm phổ quát (ufunc)

**Vector hóa** là phương pháp loại bỏ các vòng lặp hiển thị ở tầng mã nguồn Python, giao phó toàn bộ khối lượng công việc tính toán cho các vòng lặp viết bằng mã C đã được tối ưu hóa ở tầng dưới.

Các toán tử số học cơ bản (`+`, `-`, `*`, `/`) cũng như các hàm toán học như `np.sqrt`, `np.exp`, `np.sin` đều là các **hàm phổ quát** (universal functions - ufunc). Chúng tự động áp dụng phép tính lên từng phần tử (element-wise) của mảng với tốc độ tối đa.

```python
print((A * 2).tolist())
print(np.sqrt(np.array([1.0, 4.0, 9.0])).tolist())  # [1.0, 2.0, 3.0]
print(A[A >= 40].tolist())       # [40, 50, 60]
print(np.where(A >= 40, A, 0).tolist())
```

Đoạn mã trên thể hiện hai công cụ lọc dữ liệu kinh điển:

1. **Lọc bằng mặt nạ Boolean (Boolean Indexing)**: Biểu thức so sánh `A >= 40` sinh ra một mảng chân lý có cùng kích thước với `A`. Khi đưa mặt nạ này vào chỉ mục `A[A >= 40]`, NumPy trích xuất các phần tử thỏa mãn điều kiện và duỗi thẳng kết quả thành một mảng 1 chiều chứa `[40, 50, 60]`.
2. **Chọn nhánh có điều kiện với `np.where`**: Hàm `np.where(dieu_kien, neu_dung, neu_sai)` hoạt động tương tự như toán tử ba ngôi `? :` trong C++ hoặc hàm `IF()` trong Excel, nhưng được vector hóa hoàn toàn. Ở ví dụ trên, hàm giữ nguyên các giá trị lớn hơn hoặc bằng 40 và thay thế các phần tử còn lại bằng 0, bảo toàn nguyên vẹn kích thước hình học ban đầu của mảng.

## 3. Cơ chế Broadcasting: Lan truyền kích thước ảo

Làm thế nào để cộng một mảng điều chỉnh 1 chiều gồm 3 phần tử `[1, 2, 3]` vào một ma trận 2 chiều kích thước $(2, 3)$? 

Trong đại số tuyến tính truyền thống, hai ma trận chỉ có thể cộng được với nhau khi chúng có cùng kích thước. Nhưng NumPy cung cấp cơ chế **Broadcasting** (lan truyền), cho phép tự động kéo dãn các mảng có kích thước nhỏ hơn để khớp với mảng lớn hơn trong lúc tính toán.

```python
d = np.array([1, 2, 3])
B = A + d
print(B.tolist())               # [[11, 22, 33], [41, 52, 63]]
print((A + np.array([[1], [2]])).tolist())
```

Điều kỳ diệu của Broadcasting nằm ở chỗ: **NumPy không hề nhân bản mảng `d` trong bộ nhớ RAM**. Thay vì tạo ra một ma trận sao chép thực sự, NumPy chỉ đơn giản điều chỉnh bước nhảy địa chỉ nhớ (stride = 0) ở trục tương ứng, khiến CPU đọc lại cùng một phần tử nhiều lần. Kỹ thuật này giúp tiết kiệm hàng gigabyte bộ nhớ khi làm việc với các mảng khổng lồ.

Quy tắc Broadcasting được xác định theo thuật toán hai bước chuẩn mực:

1. **Căn chỉnh từ phải sang trái**: Đặt các bộ kích thước (`shape`) thẳng hàng ở chiều cuối cùng (chiều ngoài cùng bên phải) và lùi dần về phía trước. Nếu một mảng có ít chiều hơn mảng kia, mảng đó được bổ sung các chiều có kích thước 1 vào bên trái.
2. **Điều kiện tương thích**: Tại mỗi trục so sánh, hai kích thước được coi là tương thích nếu và chỉ nếu:
   - Chúng có giá trị bằng nhau, HOẶC
   - Một trong hai kích thước có giá trị bằng 1.

Hãy phân tích phép cộng `A + d` ở ví dụ trên:
- Kích thước của `A`: `(2, 3)`
- Kích thước của `d`: `   (3,)` -> được tự động nâng chiều bên trái thành `(1, 3)`
- Chiều cuối: $3 = 3$ (khớp). Chiều đầu: $2$ và $1$ (chiều $1$ được kéo dãn thành $2$). Kết quả sinh ra mảng kích thước `(2, 3)`.

Nếu muốn cộng gia số riêng biệt cho từng hàng (ví dụ hàng 1 cộng thêm 1, hàng 2 cộng thêm 2), ta phải cung cấp mảng có kích thước `(2, 1)`. Lúc này chiều cuối là $1$ được kéo dãn thành $3$, hoàn toàn tương thích. Ngược lại, nếu bạn cố tình cộng một mảng có `shape = (2,)` vào `(2, 3)`, thuật toán căn chỉnh từ phải sang trái sẽ so sánh cặp chiều cuối cùng: $3$ và $2$. Do $3 \ne 2$ và không có chiều nào bằng 1, NumPy sẽ lập tức ném ra ngoại lệ `ValueError`.

<CodeIllustration type="broadcast" />

## 4. Trục tính toán (Axis) và các phép toán thu gọn

Khi gọi các hàm thống kê tổng hợp như `sum()`, `mean()`, `std()`, một câu hỏi muôn thuở khiến nhiều người bối rối là: **Tham số `axis=0` hay `axis=1` tính theo hàng hay theo cột?**

Một mẹo tư duy bản chất giúp bạn không bao giờ nhầm lẫn: **`axis` chính là trục bị nén lại và triệt tiêu**.

```python
print(A.sum(axis=0).tolist())    # [50, 70, 90]
print(A.sum(axis=1).tolist())    # [60, 150]
print(A.mean())                 # 35.0
print(A.mean(axis=1, keepdims=True).shape)  # (2, 1)
```

Hãy hình dung mảng `A` có kích thước `(2, 3)`:
- Khi truyền `axis=0`, ta đang yêu cầu nén trục 0 (trục có độ dài 2, tức trục hàng). Hai hàng bị ép xẹp lại với nhau, để lại 3 kết quả tương ứng cho 3 cột: `[10+40, 20+50, 30+60] = [50, 70, 90]`.
- Khi truyền `axis=1`, ta đang yêu cầu nén trục 1 (trục có độ dài 3, tức trục cột). Ba cột bị ép xẹp lại, để lại 2 kết quả tương ứng cho 2 hàng: `[10+20+30, 40+50+60] = [60, 150]`.

Tùy chọn **`keepdims=True`** giữ lại trục bị triệt tiêu dưới dạng kích thước 1 (tức `(2, 1)` thay vì `(2,)`). Điều này cực kỳ tiện lợi khi ta cần lấy mảng gốc trừ đi giá trị trung bình của từng hàng bằng cơ chế Broadcasting mà không cần phải gọi thêm hàm định hình lại.

Xét phép tính phương sai trên vector $v = [2, 4, 6]$:

```python
v = np.array([2.0, 4.0, 6.0])
print(v.var(), v.var(ddof=1))
```

Trung bình của dãy là $\bar{x} = (2 + 4 + 6) / 3 = 4$. Tổng bình phương độ lệch là $(2 - 4)^2 + (4 - 4)^2 + (6 - 4)^2 = 4 + 0 + 4 = 8$.
- **`v.var()` (mặc định `ddof=0`)**: Chia cho $N = 3$, cho phương sai quần thể $\sigma^2 = 8 / 3 \approx 2.67$.
- **`v.var(ddof=1)`**: Chia cho bậc tự do $N - 1 = 2$, cho phương sai mẫu hiệu chỉnh của Bessel $s^2 = 8 / 2 = 4.0$. Trong nghiên cứu khoa học và thống kê suy luận, khi làm việc với mẫu thu thập được, ta luôn cần thiết lập `ddof=1` để có ước lượng không chệch cho phương sai của quần thể.

## 5. Bản sao (Copy) và Khung nhìn (View): Quản trị vùng nhớ thực tế

Hiểu rõ khi nào NumPy tạo ra một mảng mới (Copy) và khi nào chỉ tạo ra một khung nhìn (View) vào vùng nhớ cũ là ranh giới giữa một lập trình viên tay mơ và một kỹ sư chuyên nghiệp.

```python
goc = np.array([10, 20, 30, 40])
lat = goc[1:3]
lat[0] = 99
print(goc.tolist())             # [10, 99, 30, 40]
doc_lap = goc[[0, 2]]
doc_lap[0] = -1
print(goc[0])                   # 10
rng = np.random.default_rng(7)
mau = rng.choice(goc, size=2, replace=False)
print(mau.shape)                # (2,)
```

Quy tắc bất di bất dịch của NumPy:
1. **Lát cắt cơ bản (Basic Slicing) tạo ra View**: Biểu thức `goc[1:3]` không cấp phát thêm bộ nhớ cho mảng mới. Biến `lat` chỉ là một góc nhìn khác trỏ vào cùng khối nhớ của `goc`. Khi bạn gán `lat[0] = 99`, bạn đang trực tiếp ghi đè lên phần tử thứ hai của mảng `goc`.
2. **Chỉ mục nâng cao (Fancy Indexing) tạo ra Copy**: Khi bạn truyền một danh sách chỉ số nguyên như `goc[[0, 2]]` hoặc một mảng Boolean, NumPy buộc phải sao chép dữ liệu sang một vùng nhớ độc lập hoàn toàn. Do đó việc thay đổi `doc_lap[0]` không hề ảnh hưởng tới mảng gốc.
3. Khi không chắc chắn hai mảng có dùng chung bộ nhớ hay không, hãy sử dụng hàm `np.shares_memory(a, b)` để kiểm tra chính xác.

Đối với việc sinh số ngẫu nhiên hoặc lấy mẫu phân tích, luôn sử dụng bộ tạo số ngẫu nhiên mới **`np.random.default_rng(seed)`** (sử dụng thuật toán PCG64 hiện đại) thay vì các hàm cũ như `np.random.seed()` hay `np.random.choice()` vốn dùng thuật toán Mersenne Twister cũ hơn và có trạng thái toàn cục dễ gây xung đột khi chạy đa luồng.

## 6. Bài tập tự luyện

::: exercise Thẩm định tính tương thích Broadcasting
Cho một mảng $M$ có kích thước `shape = (4, 3)`. Trong các mảng có kích thước sau đây, mảng nào có thể tham gia phép cộng Broadcasting với $M$? Giải thích cặn kẽ từng trường hợp:
1. `(3,)`
2. `(4,)`
3. `(4, 1)`
4. `(1, 3)`
:::

::: solution
Thực hiện so sánh từng chiều từ phải sang trái với `(4, 3)`:
1. `(3,)`: Được mở rộng ảo thành `(1, 3)`. Chiều cuối $3 = 3$, chiều trước $1$ tương thích với $4$. **Hợp lệ**.
2. `(4,)`: Được mở rộng thành `(1, 4)`. So sánh chiều cuối: $3 \ne 4$ và không có chiều nào bằng 1. **Thất bại** (báo lỗi ValueError).
3. `(4, 1)`: Chiều cuối $1$ tương thích với $3$, chiều trước $4 = 4$. **Hợp lệ**. Mảng này sẽ cộng giá trị của từng hàng vào các cột tương ứng.
4. `(1, 3)`: Chiều cuối $3 = 3$, chiều trước $1$ tương thích với $4$. **Hợp lệ**.
:::

::: exercise Kiểm chứng bảo toàn tổng qua phép nén trục
Với ma trận $A$ kích thước $(2, 3)$ ở mục 1, hãy chứng minh rằng tổng các phần tử sau khi nén theo trục 1 sẽ bằng đúng tổng của toàn bộ ma trận ban đầu.
:::

::: solution
Ma trận ban đầu:
$A = \begin{bmatrix} 10 & 20 & 30 \\ 40 & 50 & 60 \end{bmatrix}$

Thực hiện nén theo `axis=1` (cộng theo từng hàng):
- Hàng 0: $10 + 20 + 30 = 60$
- Hàng 1: $40 + 50 + 60 = 150$
Kết quả là mảng `[60, 150]`.

Lấy tổng của mảng kết quả này: $60 + 150 = 210$.
Tổng của toàn bộ mảng ban đầu `A.sum()` cũng chính bằng: $10 + 20 + 30 + 40 + 50 + 60 = 210$.
Phép toán bảo toàn hoàn toàn tổng đại số của hệ thống.
:::

::: exercise Bảo vệ mảng gốc trước cạm bẫy View
Một kỹ sư muốn trích xuất dữ liệu của tuần đầu tiên từ mảng doanh thu tháng để chuẩn hóa, nhưng phát hiện sau khi chuẩn hóa thì mảng doanh thu gốc của cả tháng cũng bị biến dạng theo. Đoạn mã lỗi ban đầu là: `tuan_mot = doanh_thu[0:7]`. Hãy sửa lại đoạn mã này để bảo đảm tính độc lập dữ liệu tuyệt đối.
:::

::: solution
Cần sử dụng phương thức sao chép tường minh:
`tuan_mot = doanh_thu[0:7].copy()`

Lát cắt `[0:7]` ban đầu chỉ tạo ra một khung nhìn (View) dùng chung vùng nhớ với `doanh_thu`. Việc thêm `.copy()` buộc NumPy phải cấp phát một vùng đệm bộ nhớ mới hoàn toàn cho `tuan_mot`, cắt đứt mọi liên kết chia sẻ bộ nhớ với mảng gốc.
:::

## 7. Nguồn và đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 4: NumPy Basics](https://wesmckinney.com/book/numpy-basics) và [Phụ lục A: Advanced NumPy](https://wesmckinney.com/book/advanced-numpy).
- Hướng dẫn chính thức của thư viện: [NumPy User Guide — Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html).
- [Bài giảng tham khảo môn Xử lý dữ liệu (iaidev)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-03-numpy.html).
