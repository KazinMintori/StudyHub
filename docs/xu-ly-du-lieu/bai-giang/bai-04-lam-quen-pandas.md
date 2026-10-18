---
course: xu-ly-du-lieu
lecture: bai-04-lam-quen-pandas
section: lecture
title: "Series, DataFrame và chỉ mục trong pandas"
prerequisites: ["dictionary", "mang"]
lessonStatus: ready
hasChapterExercises: true
description: "Cấu trúc dữ liệu Series và DataFrame, cơ chế căn chỉnh nhãn, lựa chọn với loc và iloc, Copy-on-Write, thống kê mô tả và 7 bài tập thực hành."
---


<div class="lecture-notes-content">

## 1. Giới thiệu cấu trúc dữ liệu trong pandas

Bạn nhận được bảng dữ liệu giá phòng cho thuê gồm nhiều cột: Mã căn hộ, loại phòng, số đêm lưu trú, đơn giá mỗi đêm và phí dọn dẹp. Một số căn hộ chưa ghi nhận phí dọn phòng hoặc để trống số đêm. Nếu dùng mảng hai chiều NumPy, việc kết hợp đồng thời chuỗi ký tự tên loại phòng và số thực đơn giá sẽ buộc toàn bộ mảng chuyển thành kiểu chuỗi hoặc đối tượng rời rạc, làm mất đi khả năng tính toán số học nhanh. Thư viện pandas giải quyết vấn đề này bằng cách cung cấp cấu trúc bảng hai chiều `DataFrame`, nơi mỗi cột lưu trữ một kiểu dữ liệu riêng biệt nhưng các hàng được kết nối chặt chẽ qua một hệ thống chỉ mục nhãn đồng nhất.

### 1.1. Cấu trúc Series: Mảng một chiều có nhãn
`Series` là đối tượng mảng một chiều gồm hai thành phần gắn kết chặt chẽ:
1. **Mảng giá trị (*values*)**: Vùng đệm dữ liệu số học hoặc đối tượng bên dưới, có kiểu dữ liệu `dtype` đồng nhất.
2. **Chỉ mục nhãn (*index*)**: Mảng các nhãn định danh đi kèm từng phần tử.

```python
import pandas as pd
import numpy as np

# Khởi tạo Series với chỉ mục mặc định (0, 1, 2, ...)
s1 = pd.Series([4.5, 7.2, -5.3, 3.0])

# Khởi tạo Series với chỉ mục nhãn tùy biến
s2 = pd.Series([100, 80, 60], index=["P01", "P02", "P03"])
print(s2)
# P01    100
# P02     80
# P03     60
# dtype: int64
```

Khác với danh sách Python, `Series` cho phép truy xuất phần tử theo nhãn tương tự từ điển: `s2["P01"]`. Đồng thời, `Series` hỗ trợ trọn vẹn các phép toán vector hóa của NumPy:
```python
s_gap_doi = s2 * 2
s_loc = s2[s2 >= 80]
```
Mọi phép toán số học đều tự động bảo lưu liên kết nhãn với giá trị tương ứng.

### 1.2. Cấu trúc DataFrame: Bảng dữ liệu hai chiều
`DataFrame` biểu diễn một bảng dữ liệu hai chiều có cấu trúc, gồm tập hợp các cột có tên nhãn cụ thể, trong đó mỗi cột có thể chứa một kiểu dữ liệu riêng biệt.

#### Khởi tạo DataFrame
DataFrame có thể được xây dựng từ nhiều nguồn dữ liệu:
- Từ một từ điển chứa các danh sách có cùng độ dài:
```python
du_lieu = {
    "khu_vuc": ["Bắc", "Bắc", "Nam", "Nam"],
    "nam": [2024, 2025, 2024, 2025],
    "doanh_thu": [150.5, 180.2, 210.0, 245.8]
}
df = pd.DataFrame(du_lieu, index=["HN1", "HN2", "SG1", "SG2"])
```
- Từ từ điển lồng nhau: Các khóa ngoài trở thành tên cột, các khóa trong trở thành nhãn hàng (*index*).

#### Thuộc tính và thao tác cơ bản
- `df.shape`: Tuple trả về số hàng và số cột `(so_hang, so_cot)`.
- `df.columns`: Đối tượng Index chứa danh sách tên các cột.
- `df.index`: Đối tượng Index chứa danh sách nhãn các hàng.
- `df.dtypes`: Series hiển thị kiểu dữ liệu của từng cột.
- `df.head(n)` và `df.tail(n)`: Xem nhanh $n$ dòng đầu tiên hoặc $n$ dòng cuối cùng của bảng.

Trích xuất một cột từ DataFrame bằng cú pháp ngoặc vuông `df["doanh_thu"]` hoặc truy cập thuộc tính `df.doanh_thu` sẽ trả về một đối tượng `Series`. Thêm một cột mới vào bảng được thực hiện bằng phép gán:
```python
df["thue"] = df["doanh_thu"] * 0.1
```
Xóa một cột khỏi bảng sử dụng câu lệnh `del df["thue"]` hoặc phương thức `.drop()`.

### 1.3. Đối tượng chỉ mục Index
Các đối tượng `Index` trong pandas chịu trách nhiệm lưu trữ nhãn trục (hàng và cột) và các siêu dữ liệu khác.

> [!IMPORTANT] Tính bất biến của Index
> Các đối tượng `Index` mang tính **bất biến** (*immutable*). Lập trình viên không thể chỉnh sửa riêng lẻ một nhãn bên trong Index:
> ```python
> idx = df.index
> idx[0] = "HN_MOI"  # TypeError: Index does not support mutable operations
> ```
> Tính bất biến này giúp bảo đảm an toàn dữ liệu, cho phép chia sẻ cùng một đối tượng `Index` giữa nhiều cấu trúc DataFrame và Series mà không sợ bị biến đổi ngoài tầm kiểm soát.

Đối tượng Index hỗ trợ đầy đủ các phép toán đại số tập hợp:
- `idx1.union(idx2)`: Tập hợp hợp.
- `idx1.intersection(idx2)`: Tập hợp giao.
- `idx1.difference(idx2)`: Tập hợp hiệu.
- `idx.is_unique`: Kiểm tra xem các nhãn chỉ mục có duy nhất hay không.

---

## 2. Các chức năng thiết yếu của pandas

### 2.1. Tái lập chỉ mục
Phương thức `.reindex()` tạo ra một đối tượng mới với dữ liệu được sắp xếp lại theo một chỉ mục nhãn mới. Nếu một nhãn mới không có trong dữ liệu ban đầu, pandas sẽ điền giá trị khuyết thiếu `NaN`:

```python
s = pd.Series([10, 20, 30], index=["a", "b", "c"])
s_moi = s.reindex(["a", "b", "c", "d"], fill_value=0)
# a    10
# b    20
# c    30
# d     0
```

Trong dữ liệu chuỗi thời gian, ta có thể nội suy các giá trị thiếu khi đổi chỉ mục bằng tham số `method`:
- `method="ffill"` (*forward fill*): Điền tiếp giá trị của quan sát trước đó về phía sau.
- `method="bfill"` (*backward fill*): Lấy giá trị của quan sát liền sau điền ngược về trước.

### 2.2. Loại bỏ dòng và cột với drop
Phương thức `.drop()` loại bỏ các nhãn chỉ định khỏi một trục và trả về một đối tượng mới:
```python
# Loại bỏ hàng theo nhãn (axis=0 mặc định)
df_bot_hang = df.drop(["HN1", "SG1"])

# Loại bỏ cột theo tên (axis=1 hoặc axis="columns")
df_bot_cot = df.drop(columns=["nam"])
```

### 2.3. Chỉ mục, lựa chọn và sàng lọc với loc và iloc
Để tránh mơ hồ giữa việc chọn theo nhãn danh nghĩa hay chọn theo vị trí số nguyên, pandas cung cấp hai toán tử chỉ mục chuyên dụng:

#### 1. Chọn theo nhãn với `.loc`
Toán tử `.loc[hang_nhan, cot_nhan]` tiếp nhận nhãn danh nghĩa:
```python
# Chọn một ô đơn lẻ
gia_tri = df.loc["HN1", "doanh_thu"]

# Chọn một tập hợp hàng và cột
bang_con = df.loc[["HN1", "SG1"], ["khu_vuc", "doanh_thu"]]

# Cắt lát theo nhãn: BAO GỒM CẢ ĐIỂM KẾT THÚC
lat_cat_loc = df.loc["HN1":"SG1", "khu_vuc":"doanh_thu"]
```

#### 2. Chọn theo vị trí số nguyên với `.iloc`
Toán tử `.iloc[hang_vi_tri, cot_vi_tri]` tiếp nhận chỉ số nguyên từ $0$ đến $n-1$:
```python
# Chọn hàng 0, cột 2
gia_tri = df.iloc[0, 2]

# Cắt lát theo vị trí: KHÔNG BAO GỒM ĐIỂM KẾT THÚC (chuẩn Python)
lat_cat_iloc = df.iloc[0:2, 1:3]
```

#### Cạm bẫy chỉ mục số nguyên
Xét Series có nhãn nguyên nhưng thứ tự nhãn khác vị trí:

```python
s = pd.Series([10, 20, 30], index=[2, 0, 1])
assert s[1] == s.loc[1] == 30
assert s.iloc[1] == 20
```

Trong trường hợp này, `s[1]` tìm nhãn 1 chứ không lấy phần tử thứ hai. `s[-1]` báo `KeyError` vì không có nhãn -1. Viết `.loc` và `.iloc` giúp thể hiện rõ ý định chọn theo nhãn hay vị trí.

#### Cạm bẫy gán chuỗi và cơ chế Copy-on-Write
Một thao tác dễ gây lỗi logic là viết câu lệnh gán hai lần ngoặc vuông (*chained indexing*):
```pycon
>>> phong_demo["gia"][phong_demo["gia"] < 50] = 50
```
Với `phong_demo` là DataFrame có cột `gia`, lần chọn đầu lấy một Series trung gian. Trong pandas 3 dùng Copy-on-Write, phép gán chuỗi này không cập nhật bảng gốc và phát cảnh báo thuộc loại `ChainedAssignmentError`. Đừng hiểu tên cảnh báo là bảo đảm chương trình luôn dừng bằng ngoại lệ, vì điều đó còn tùy cấu hình xử lý warning.

> [!TIP] Gán rõ bảng đích trong một bước
> Một cách cập nhật là dùng `.loc` với cả điều kiện hàng và tên cột:
> ```python
> phong_demo = pd.DataFrame({"gia": [40.0, 70.0]})
> phong_demo.loc[phong_demo["gia"] < 50, "gia"] = 50
> assert phong_demo["gia"].tolist() == [50.0, 70.0]
> ```

### 2.4. Số học và căn chỉnh dữ liệu tự động
Khi thực hiện các phép tính số học giữa hai đối tượng Series hoặc DataFrame, pandas tự động **căn chỉnh dữ liệu theo nhãn**:

```python
s1 = pd.Series([10, 20], index=["a", "b"])
s2 = pd.Series([30, 40], index=["b", "c"])
ket_qua_cong = s1 + s2
assert ket_qua_cong.loc["b"] == 50
assert ket_qua_cong.loc[["a", "c"]].isna().all()
```
Phép cộng $s_1 + s_2$ sẽ lấy hợp của toàn bộ các nhãn:
- Nhãn `"a"` chỉ có ở $s_1$, thiếu ở $s_2 \implies$ kết quả là `NaN`.
- Nhãn `"b"` có ở cả hai bên: $20 + 30 = 50$.
- Nhãn `"c"` chỉ có ở $s_2$, thiếu ở $s_1 \implies$ kết quả là `NaN`.

Muốn thay thế các giá trị khuyết thiếu bằng một hằng số khi tính toán, ta sử dụng các phương thức số học có tham số `fill_value`:
```python
s_tong = s1.add(s2, fill_value=0)
# a    10.0
# b    50.0
# c    40.0
```

#### Phép toán giữa DataFrame và Series (Broadcasting)
Theo mặc định, phép toán giữa DataFrame và Series khớp nhãn Series với tên cột rồi dùng lại các giá trị đó cho mỗi hàng. Muốn khớp với nhãn hàng, hãy chỉ định `axis="index"` hoặc `axis=0`:
```python
bang_so = pd.DataFrame({"A": [10, 20], "B": [30, 40]}, index=["r1", "r2"])
s_theo_hang = pd.Series([1, 2], index=["r1", "r2"])
df_tru = bang_so.sub(s_theo_hang, axis="index")
np.testing.assert_array_equal(df_tru.to_numpy(), [[9, 29], [18, 38]])
```

### 2.5. Áp dụng hàm và ánh xạ
- `df.apply(ham, axis=0)`: Áp dụng một hàm số lên từng cột (hoặc từng hàng nếu `axis=1`). Thường dùng cho các hàm tổng hợp hoặc biến đổi phức tạp.
- `ser.map(anh_xa)`: Ánh xạ từng phần tử của Series thông qua một từ điển tra cứu hoặc một hàm một đối số.
- `df.map(ham)`: Áp dụng một hàm lên từng ô đơn lẻ của toàn bộ DataFrame (thay thế phương thức `applymap` cũ).

```python
# Tra cứu phí theo loại phòng bằng map
bang_phi = {"Nguyên căn": 20, "Phòng riêng": 10}
phong_phi = pd.DataFrame({"loai": ["Nguyên căn", "Phòng riêng"]})
phong_phi["phi"] = phong_phi["loai"].map(bang_phi)
assert phong_phi["phi"].tolist() == [20, 10]
```

### 2.6. Sắp xếp và xếp hạng
- Sắp xếp theo chỉ mục nhãn: `df.sort_index(ascending=True)`.
- Sắp xếp theo giá trị cột: `df.sort_values(by="doanh_thu", ascending=False)`.
- Xếp hạng dữ liệu: Phương thức `.rank()` gán thứ hạng từ $1$ đến $n$ cho các phần tử. Khi các giá trị bằng nhau, tham số `method` quyết định cách giải quyết hòa vị:
  - `"average"` (mặc định): Lấy trung bình cộng các thứ hạng hòa (ví dụ hai số cùng nhỏ nhất chia nhau hạng 1 và 2 sẽ nhận hạng $1{,}5$).
  - `"min"`: Cùng nhận thứ hạng nhỏ nhất.
  - `"max"`: Cùng nhận thứ hạng lớn nhất.
  - `"first"`: Xếp hạng theo thứ tự xuất hiện trước trong dữ liệu.
  - `"dense"`: Tăng thứ hạng liền kề mà không bỏ qua bậc (hạng 1, hạng 1, tiếp theo là hạng 2).

---

## 3. Thống kê mô tả và tóm tắt dữ liệu

### 3.1. Các phương thức thống kê mô tả
pandas cung cấp đầy đủ các phương thức thống kê tổng hợp trên DataFrame:
- `df.sum(axis=0)`: Tính tổng theo từng cột.
- `df.mean(axis=1)`: Tính trung bình theo từng hàng.
- `df.describe()`: Bảng tóm tắt toàn diện gồm số lượng đếm, trung bình, độ lệch chuẩn, giá trị nhỏ nhất, các phân vị $25\%$, $50\%$ (trung vị), $75\%$, và giá trị lớn nhất.

#### Tham số `skipna` và `min_count`
Theo mặc định, các phương thức thống kê của pandas tự động bỏ qua các giá trị khuyết thiếu (`skipna=True`).
Tuy nhiên, cần đặc biệt lưu ý: Một Series toàn giá trị `NaN` khi gọi `.sum()` mặc định sẽ trả về $0{,}0$. Để bắt buộc phép tính phải có ít nhất một giá trị hợp lệ mới sinh ra kết quả, ta sử dụng tham số `min_count=1`:
```python
s_trong = pd.Series([np.nan, np.nan])
print(s_trong.sum())               # 0.0 (Nguy cơ gây hiểu lầm)
print(s_trong.sum(min_count=1))    # NaN (Phản ánh đúng dữ liệu khuyết)
```

### 3.2. Tương quan và hiệp phương sai
- `s1.corr(s2)`: Tính hệ số tương quan Pearson giữa hai Series.
- `df.corr()`: Ma trận tương quan giữa tất cả các cặp cột số học.
- `df.corrwith(s1)`: Tính tương quan giữa từng cột của DataFrame với một Series chỉ định.

### 3.3. Giá trị duy nhất, đếm tần suất và kiểm tra thành viên
- `ser.unique()`: Trả về một mảng NumPy chứa các giá trị phân biệt theo thứ tự xuất hiện.
- `ser.value_counts()`: Trả về Series thống kê tần suất xuất hiện của từng giá trị, sắp xếp giảm dần.
- `ser.isin(danh_sach)`: Trả về Series boolean kiểm tra từng ô có thuộc danh sách giá trị cho trước hay không.

---

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 5: Getting Started with pandas.
- The pandas Development Team. *pandas documentation: Indexing and selecting data & Copy-on-Write*. https://pandas.pydata.org/docs/user_guide/indexing.html
- Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN. *Học liệu môn học Lập trình xử lý dữ liệu: Bài 4 - Làm quen với pandas và Bài 5 - Series & DataFrame chuyên sâu*. Các bài tập thực hành trong bài giảng được biên soạn và chuẩn hóa dựa trên học liệu mở của IAI UET theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 4. Bài tập thực hành

<span id="iai-04-bai-1"></span>

::: exercise Bài tập 1: Chọn chỗ ở theo ngân sách và ngưỡng số đêm
Bảng dữ liệu giả lập về ba chỗ ở với giá thuê mỗi đêm và phí dọn dẹp một lần duy nhất cho mỗi lượt ở (đơn vị USD):

| Chỗ ở | Giá mỗi đêm | Phí dọn dẹp |
| :--- | :--- | :--- |
| a | 100 | 0 |
| b | 80 | 100 |
| c | 60 | 300 |

1. Tạo DataFrame `cho_o` biểu diễn bảng trên với chỉ mục là tên các chỗ ở `["a", "b", "c"]`.
2. Sử dụng phép toán trên Series để tính tổng số tiền cho một chuyến đi kéo dài 2 đêm và 7 đêm. Trong mỗi trường hợp, chỗ ở nào có tổng chi phí thấp nhất?
3. Từ bao nhiêu đêm trở lên thì chỗ ở `c` sẽ có tổng chi phí rẻ hơn cả `a` và `b`? Hãy lập luận bằng bất đẳng thức và kiểm tra lại bằng mã nguồn Python.
:::

::: solution Lời giải
1. Tạo DataFrame:
```python
import pandas as pd

cho_o = pd.DataFrame({
    "gia_dem": [100, 80, 60],
    "phi_don": [0, 100, 300]
}, index=["a", "b", "c"])
```
2. Với mỗi chỗ ở, gọi p là giá mỗi đêm và f là phí dọn dẹp một lần. Tổng tiền cho n đêm là:
   $$
   T(n) = pn + f.
   $$
   - Với chuyến đi 2 đêm ($n = 2$):
     - Chỗ ở `a`: $100 \times 2 + 0 = 200$ USD.
     - Chỗ ở `b`: $80 \times 2 + 100 = 260$ USD.
     - Chỗ ở `c`: $60 \times 2 + 300 = 420$ USD.
     - Lựa chọn rẻ nhất là chỗ ở `a`.
   - Với chuyến đi 7 đêm ($n = 7$):
     - Chỗ ở `a`: $100 \times 7 + 0 = 700$ USD.
     - Chỗ ở `b`: $80 \times 7 + 100 = 660$ USD.
     - Chỗ ở `c`: $60 \times 7 + 300 = 720$ USD.
     - Lựa chọn rẻ nhất là chỗ ở `b`.
3. Xác định số đêm tối thiểu để `c` rẻ hơn cả `a` và `b`:
   Gọi $n$ là số đêm lưu trú ($n$ là số nguyên dương):
   - Để `c` rẻ hơn `a`:
     $$
     \begin{aligned}
     60n + 300 &< 100n, \\
     40n &> 300, \\
     n &> 7{,}5.
     \end{aligned}
     $$
   - Để `c` rẻ hơn `b`:
     $$
     \begin{aligned}
     60n + 300 &< 80n + 100, \\
     20n &> 200, \\
     n &> 10.
     \end{aligned}
     $$
   Kết hợp hai điều kiện: $n > 10$. Vì số đêm là số nguyên nên số đêm lưu trú tối thiểu để `c` trở thành phương án tiết kiệm nhất là **11 đêm**.
   Kiểm tra số học:
   - Tại $n = 10$: `a` $= 1000$, `b` $= 900$, `c` $= 900$ (`b` và `c` bằng giá nhau).
   - Tại $n = 11$: `a` $= 1100$, `b` $= 980$, `c` $= 960$ (`c` rẻ nhất).
:::

<span id="iai-04-bai-2"></span>

::: exercise Bài tập 2: Phân biệt biến động giá và thay đổi tập mẫu quan sát
Một nghiên cứu theo dõi giá thuê của ba chỗ ở qua hai đợt thu thập dữ liệu (đơn vị USD/đêm):

| Chỗ ở | Lần 1 | Lần 2 |
| :--- | :--- | :--- |
| a | 100 | 110 |
| b | 200 | 210 |
| c | 300 | Chưa có giá (khuyết thiếu) |

1. Tạo DataFrame `df_gia` và tính giá trung bình của các giá đã biết ở mỗi lần thu thập.
2. Tính lại giá trung bình ở cả hai lần khi chỉ giới hạn khảo sát trên tập chỗ ở có mặt ở cả hai đợt (chỗ ở `a` và `b`).
3. Vì sao cách tính thứ nhất lại cho thấy giá trung bình của thị trường bị giảm, trong khi cách tính thứ hai cho thấy giá thực tế đang tăng? Bài học rút ra khi phân tích dữ liệu khuyết thiếu là gì?
:::

::: solution Lời giải
```python
import numpy as np
import pandas as pd

df_gia = pd.DataFrame({
    "lan_1": [100.0, 200.0, 300.0],
    "lan_2": [110.0, 210.0, np.nan]
}, index=["a", "b", "c"])

# 1. Trung bình trên các giá đã biết
tb_lan1 = df_gia["lan_1"].mean()  # (100 + 200 + 300) / 3 = 200.0
tb_lan2 = df_gia["lan_2"].mean()  # (110 + 210) / 2 = 160.0

# 2. Trung bình khi chỉ xét các chỗ ở có mặt ở cả hai lần (a và b)
tb_chung_lan1 = df_gia.loc[["a", "b"], "lan_1"].mean()  # (100 + 200) / 2 = 150.0
tb_chung_lan2 = df_gia.loc[["a", "b"], "lan_2"].mean()  # (110 + 210) / 2 = 160.0

print(f"Lần 1 toàn bộ: {tb_lan1}, Lần 2 toàn bộ: {tb_lan2}")
print(f"Lần 1 (a, b): {tb_chung_lan1}, Lần 2 (a, b): {tb_chung_lan2}")
```

3. Giải thích bản chất:
   - Ở cách tính thứ nhất, giá trung bình giảm từ $200$ xuống $160$ USD không phải vì giá phòng hạ nhiệt, mà do **sự thay đổi thành phần của tập mẫu quan sát**. Ở lần 1, mẫu có mặt căn hộ cao cấp `c` với giá $300$ USD kéo trung bình lên cao. Sang lần 2, căn hộ `c` bị khuyết thiếu dữ liệu, mẫu chỉ còn lại hai căn hộ giá thấp hơn.
   - Ở cách tính thứ hai trên cùng một tập đối tượng so sánh nhất quán (`a` và `b`), giá phòng thực tế tăng từ $150$ lên $160$ USD (mỗi phòng đều tăng đúng $10$ USD).
   - Bài học kinh nghiệm: Khi so sánh các chỉ số thống kê tổng hợp qua thời gian, phải luôn kiểm tra tính nhất quán của tập mẫu quan sát. Dữ liệu khuyết thiếu không ngẫu nhiên có thể bóp méo hoàn toàn kết luận kinh tế.
:::

<span id="iai-04-bai-3"></span>

::: exercise Bài tập 3: Lọc dữ liệu theo ngân sách và điều kiện kết hợp
Cho bảng dữ liệu `lua_chon` về các phòng cho thuê:
```python
lua_chon = pd.DataFrame({
    "loai": ["Nguyên căn", "Phòng riêng", "Nguyên căn", "Phòng riêng"],
    "gia": [90, 70, 120, 60]
}, index=["a", "b", "c", "d"])
```
Khách hàng đặt ra yêu cầu ngân sách: Nếu là phòng loại "Nguyên căn" thì giá phải $\le 100$ USD/đêm, còn nếu là loại "Phòng riêng" thì giá phải $\le 60$ USD/đêm.
1. Dự đoán bằng mắt những hàng nào thỏa mãn yêu cầu ngân sách trên.
2. Viết một mặt nạ boolean kết hợp toán tử logic để lọc ra các hàng thỏa mãn, chỉ hiển thị hai cột `loai` và `gia`.
:::

::: solution Lời giải
1. Phân tích từng dòng dữ liệu:
   - Hàng `a`: Loại "Nguyên căn", giá $90 \le 100 \implies$ Thỏa mãn.
   - Hàng `b`: Loại "Phòng riêng", giá $70 > 60 \implies$ Không thỏa mãn (mặc dù $70 \le 100$ nhưng đây là phòng riêng).
   - Hàng `c`: Loại "Nguyên căn", giá $120 > 100 \implies$ Không thỏa mãn.
   - Hàng `d`: Loại "Phòng riêng", giá $60 \le 60 \implies$ Thỏa mãn (nằm đúng trên biên ngân sách).
   - Danh sách hàng được chọn gồm `a` và `d`.
2. Mã lệnh lọc với toán tử `.loc`:
```python
mask = ((lua_chon["loai"] == "Nguyên căn") & (lua_chon["gia"] <= 100)) | \
       ((lua_chon["loai"] == "Phòng riêng") & (lua_chon["gia"] <= 60))

ket_qua = lua_chon.loc[mask, ["loai", "gia"]]
print(ket_qua)
```
   Kết quả trả về DataFrame gồm hai dòng `a` và `d` với đầy đủ hai cột `loai` và `gia`.
:::

<span id="iai-04-bai-4"></span>

::: exercise Bài tập 4: Sửa giá phòng và cạm bẫy phụ thuộc cột
Cho bảng dữ liệu ban đầu:
```python
df = pd.DataFrame({
    "loai": ["Nguyên căn", "Phòng riêng", "Nguyên căn"],
    "gia": [100.0, 50.0, np.nan]
}, index=["a", "b", "c"])
```
Yêu cầu: Tạo bảng báo giá mới `bao_gia` từ `df`. Áp dụng chính sách giảm giá $10\%$ cho tất cả các phòng loại "Nguyên căn", sau đó tính cột tiền thuê cho ba đêm `ba_dem = gia * 3`. Giữ nguyên bảng `df` ban đầu không bị biến đổi.
Một lập trình viên viết đoạn mã sau:
```python
bao_gia = df.copy()
bao_gia["ba_dem"] = bao_gia["gia"] * 3
mask = bao_gia["loai"] == "Nguyên căn"
gia_nguyen_can = bao_gia.loc[mask, "gia"]
gia_nguyen_can *= 0.9
```
1. Đoạn mã trên cho giá trị cột `ba_dem` của phòng `a` bằng bao nhiêu? Theo đúng yêu cầu bài toán, con số này phải bằng bao nhiêu?
2. Chỉ ra hai lỗi logic trong đoạn mã trên và viết lại đoạn mã chuẩn xác.
:::

::: solution Lời giải
1. Đoạn mã trên cho giá trị `ba_dem` của phòng `a` là $300{,}0$. Tuy nhiên, theo đúng yêu cầu nghiệp vụ, giá phòng `a` sau khi giảm $10\%$ còn $90{,}0$ USD, do đó tiền ba đêm phải là $90 \times 3 = 270{,}0$ USD.
2. Hai lỗi logic:
   - **Lỗi thứ tự tính toán**: Đoạn mã tính toán cột `ba_dem` trước khi thực hiện giảm giá. Các cột trong DataFrame lưu trữ giá trị tĩnh, không tự động cập nhật công thức như bảng tính Excel khi cột thành phần thay đổi.
   - **Lỗi gán trên đối tượng trích xuất**: Dòng `gia_nguyen_can = bao_gia.loc[mask, "gia"]` trích xuất một Series riêng biệt. Phép toán `gia_nguyen_can *= 0.9` chỉ biến đổi trên Series này mà không cập nhật ngược lại vào cột `gia` của `bao_gia` (do cơ chế bảo vệ Copy-on-Write).
3. Đoạn mã sửa lại chuẩn xác:
```python
bao_gia = df.copy()

# Bước 1: Giảm 10% giá phòng nguyên căn trực tiếp trên bảng
mask = bao_gia["loai"] == "Nguyên căn"
bao_gia.loc[mask, "gia"] = bao_gia.loc[mask, "gia"] * 0.9

# Bước 2: Tính toán cột tiền ba đêm sau khi giá đã được cập nhật
bao_gia["ba_dem"] = bao_gia["gia"] * 3

print("Bảng báo giá mới:")
print(bao_gia)
print("\nBảng gốc df vẫn được bảo toàn:")
print(df)
```
   Kết quả cho thấy `bao_gia.loc["a", "gia"]` $= 90{,}0$, `bao_gia.loc["a", "ba_dem"]` $= 270{,}0$, trong khi phòng `b` giữ nguyên $50{,}0$ và $150{,}0$, còn phòng `c` giữ nguyên `NaN`. Bảng `df` gốc không bị ảnh hưởng.
:::

<span id="iai-04-bai-5"></span>

::: exercise Bài tập 5: Bảo toàn mã định danh khi lưu trữ tệp CSV
Bảng dữ liệu `df` sử dụng các ký tự `"a"`, `"b"`, `"c"` làm nhãn chỉ mục hàng (*index*). Một kỹ sư xuất dữ liệu gửi cho đối tác bằng lệnh:
```python
bang_gui = df[["gia"]]
bang_gui.to_csv("bang_gui.csv", index=False)
```
1. Khi đối tác mở tệp `bang_gui.csv`, họ có biết từng giá tiền thuộc về mã chỗ ở nào không? Hãy mô tả nội dung của tệp CSV được sinh ra.
2. Hãy sửa lại cách lưu trữ để bảo đảm người nhận luôn đọc được đầy đủ cả mã chỗ ở lẫn giá tiền tương ứng.
:::

::: solution
Với `index=False`, tệp chỉ giữ cột giá mà không có các mã a, b, c. Vì người nhận không có bảng gốc, vị trí hàng không đủ để xác định mỗi giá thuộc chỗ ở nào.

Một cách là giữ chỉ mục và đặt tên cột mã khi xuất:

```python
from tempfile import TemporaryDirectory
from pathlib import Path
df_gui = pd.DataFrame({"gia":[100.0,50.0,np.nan]},index=["a","b","c"])
with TemporaryDirectory() as thu_muc:
    tep = Path(thu_muc)/"bang_gui.csv"
    df_gui.to_csv(tep,index=True,index_label="ma_cho_o")
    doc_lai = pd.read_csv(tep,index_col="ma_cho_o")
    assert doc_lai.index.tolist() == ["a","b","c"]
    np.testing.assert_allclose(doc_lai["gia"],[100,50,np.nan],equal_nan=True)
```

Cách khác là đưa mã thành cột dữ liệu trước khi dùng `index=False`:

```python
bang_gui_chuan = df_gui.rename_axis("ma_cho_o").reset_index()
assert bang_gui_chuan.columns.tolist() == ["ma_cho_o","gia"]
```

Khi lưu bảng thứ hai, dùng `bang_gui_chuan.to_csv(tep, index=False)` tại đường dẫn xuất mà bạn đã chọn. Hãy đọc lại tệp và kiểm các cặp mã–giá, không chỉ kiểm số hàng.
:::

<span id="iai-05-bai-1"></span>

::: exercise Bài tập 6: Gán cột khớp theo nhãn chỉ mục độc lập với thứ tự
Bảng `phong` quản lý danh sách các phòng với mã chỗ ở làm chỉ mục. Thông tin về phí dọn dẹp được đối tác cung cấp riêng dưới dạng hai danh sách Python độc lập có thứ tự bị xáo trộn:
```python
phong = pd.DataFrame({"gia": [100, 80, 60]}, index=["P1", "P2", "P3"])

ma_cho_o = ["P3", "P1", "P2"]
phi = [20, 10, 30]
```
Hãy thêm cột `phi` vào bảng `phong` sao cho giá trị phí luôn khớp chính xác với từng mã chỗ ở, kể cả khi thứ tự các hàng trong bảng `phong` bị thay đổi.
:::

::: solution Lời giải
Nếu gán trực tiếp danh sách `phi` bằng câu lệnh `phong["phi"] = phi`, pandas sẽ gán theo thứ tự vị trí vật lý từ trên xuống dưới, khiến `P1` nhận $20$, `P2` nhận $10$ và `P3` nhận $30$, dẫn đến sai lệch dữ liệu nghiêm trọng.

Giải pháp chuẩn xác là chuyển đổi danh sách thành một đối tượng `Series` có gắn kèm chỉ mục nhãn `ma_cho_o` trước khi gán:
```python
phong["phi"] = pd.Series(phi, index=ma_cho_o)
print(phong)
```

Kết quả:
```text
    gia  phi
P1  100   10
P2   80   30
P3   60   20
```
pandas tự động căn chỉnh theo nhãn: Mã `P1` nhận đúng phí $10$, `P2` nhận $30$ và `P3` nhận $20$. Kể cả khi ta đảo thứ tự các hàng trong bảng `phong` bằng lệnh `phong = phong.loc[["P3", "P1", "P2"]]`, phép gán vẫn duy trì sự toàn vẹn dữ liệu.
:::

<span id="iai-05-bai-2"></span>

::: exercise Bài tập 7: Tính toán chi phí có điều kiện và miễn phí dọn dẹp
Cho bảng `dat_cho` chứa thông tin về các lượt khách đặt phòng:
```python
dat_cho = pd.DataFrame({
    "gia": [100, 80, 60],
    "so_dem": [2, 7, 8],
    "phi": [20, 10, 15]
}, index=["P1", "P2", "P3"])
```
Chính sách ưu đãi của hệ thống: Khách lưu trú từ $7$ đêm trở lên được **miễn phí dọn dẹp hoàn toàn** (phí bằng 0). Phí dọn dẹp chỉ thu một lần duy nhất cho cả lượt ở.
Hãy tính tổng số tiền `tong` (gồm tiền phòng và phí dọn dẹp thực tế) cho từng lượt khách và thêm vào bảng `dat_cho`.
:::

::: solution Lời giải
Ta có thể thực hiện theo hai phương pháp chuẩn mực:

**Cách 1: Lập trình vector hóa với `.where()` (Khuyến nghị vì tối ưu tốc độ)**
```python
# Tính phí dọn dẹp sau miễn giảm: Nếu so_dem < 7 giữ nguyên phi, ngược lại bằng 0
phi_thuc_te = dat_cho["phi"].where(dat_cho["so_dem"] < 7, 0)
dat_cho["tong"] = dat_cho["gia"] * dat_cho["so_dem"] + phi_thuc_te
print(dat_cho)
```

**Cách 2: Áp dụng hàm theo từng hàng với `.apply()`**
```python
def tinh_tien_luot_o(hang):
    phi_ap_dung = 0 if hang["so_dem"] >= 7 else hang["phi"]
    return hang["gia"] * hang["so_dem"] + phi_ap_dung

dat_cho["tong"] = dat_cho.apply(tinh_tien_luot_o, axis=1)
```

Kết quả tính toán:
- Lượt `P1` (2 đêm $< 7$): $100 \times 2 + 20 = 220$ USD.
- Lượt `P2` (7 đêm $\ge 7$, miễn phí): $80 \times 7 + 0 = 560$ USD.
- Lượt `P3` (8 đêm $\ge 7$, miễn phí): $60 \times 8 + 0 = 480$ USD.
:::

<!--@include: ../../../raw_materials/xu-ly-du-lieu/practice/iai-a-chapter-5.md-->

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 5: Getting Started with pandas.
- The pandas Development Team. *pandas documentation: Indexing and selecting data & Copy-on-Write*. https://pandas.pydata.org/docs/user_guide/indexing.html
- Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN. *Học liệu môn học Lập trình xử lý dữ liệu: Bài 4 - Làm quen với pandas và Bài 5 - Series & DataFrame chuyên sâu*. Các bài tập thực hành trong bài giảng được biên soạn và chuẩn hóa dựa trên học liệu mở của IAI UET theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>
