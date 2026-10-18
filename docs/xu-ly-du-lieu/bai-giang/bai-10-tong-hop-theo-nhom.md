---
course: xu-ly-du-lieu
lecture: bai-10-tong-hop-theo-nhom
section: lecture
title: "Tổng hợp dữ liệu và phép toán theo nhóm"
prerequisites: ["dataframe", "gia-tri-thieu"]
lessonStatus: ready
hasChapterExercises: true
description: "Mô hình Tách - Áp dụng - Gộp (Split-Apply-Combine), các phép toán tổng hợp agg, biến đổi transform, lọc nhóm filter, phương thức apply tổng quát, tính trung bình gia quyền, bảng pivot và bảng chéo crosstab."
---


<div class="lecture-notes-content">

Trong phân tích dữ liệu, việc tính toán các đại lượng thống kê trên toàn bộ tập dữ liệu (chẳng hạn giá trị trung bình hay độ lệch chuẩn của toàn bộ bảng) thường chỉ cung cấp một góc nhìn rất khái quát. Những hiểu biết sâu sắc nhất về mặt nghiệp vụ chỉ xuất hiện khi ta bóc tách dữ liệu thành các phân khúc nhỏ hơn: So sánh năng suất theo từng phòng ban, đo lường mức chi tiêu theo từng nhóm khách hàng, hay theo dõi biến động giá theo từng vùng địa lý.

Để thực hiện các thao tác này một cách khoa học, nhà thống kê học Hadley Wickham (2011) đã chuẩn hóa mô hình **Tách - Áp dụng - Gộp (Split-Apply-Combine)**. Thay vì viết các vòng lặp thủ công chậm chạp, thư viện pandas cung cấp công cụ `groupby` để thực thi mô hình này với hiệu năng cao. Nội dung bài học tập trung vào cơ chế gom nhóm, tổng hợp nhiều chỉ số với `agg`, gán kết quả nhóm về từng dòng với `transform`, và lọc phân khúc với `filter`. Đồng thời, bài giảng hướng dẫn chi tiết phương thức `apply` cùng hai công cụ tổng hợp đa chiều là bảng pivot và bảng chéo.

---

## 1. Tư duy về các thao tác nhóm (Split-Apply-Combine)

Mô hình Tách - Áp dụng - Gộp phân rã bài toán xử lý nhóm thành ba pha toán học rạch ròi:
1. **Tách (Split)**: Bảng dữ liệu được chia cắt thành các nhóm con (*groups*) độc lập dựa trên một hoặc nhiều khóa phân loại.
2. **Áp dụng (Apply)**: Một hàm xử lý (tính toán thống kê, chuẩn hóa, hoặc lọc dòng) được áp dụng độc lập trên từng nhóm con.
3. **Gộp (Combine)**: Toàn bộ các kết quả riêng lẻ từ từng nhóm được thu gom và ghép nối lại thành một cấu trúc dữ liệu mới duy nhất.

### 1.1. Khởi tạo `groupby` và cơ chế đánh giá trì hoãn (Lazy Evaluation)

Trong pandas, việc gọi `df.groupby("khoa")` chưa thực thi bất kỳ phép tính số học nào ngay lập tức. Đây là một đối tượng trì hoãn (*Lazy Evaluation*): Pandas chỉ quét qua các cột khóa để phân nhóm các chỉ mục hàng. Phép tính chỉ thực sự diễn ra khi bạn gọi một hàm tổng hợp cụ thể như `.mean()`, `.sum()` hay `.agg()`.

```python
import numpy as np
import pandas as pd

bang_nhan_su = pd.DataFrame({
    "phong_ban": ["Kỹ thuật", "Kỹ thuật", "Kinh doanh", "Kinh doanh", "Kỹ thuật"],
    "chuc_danh": ["Lập trình viên", "Kiểm thử", "Chuyên viên", "Trưởng nhóm", "Lập trình viên"],
    "luong": [2000, 1500, 1800, 2500, 2200],
    "thuong": [300, 150, 400, 600, 350]
})

# Khởi tạo đối tượng gom nhóm theo phòng ban
nhom_pb = bang_nhan_su.groupby("phong_ban")
print("Đối tượng gom nhóm:", nhom_pb)

# Phép tính trung bình chỉ thực thi tại bước này:
print(nhom_pb["luong"].mean())
```

### 1.2. Duyệt qua từng nhóm

Đối tượng `groupby` hỗ trợ giao thức lặp (*iteration protocol*), trả về các cặp gồm `(ten_nhom, bang_nhom)`. Mỗi `bang_nhom` là một DataFrame hoàn chỉnh chứa toàn bộ các dòng thuộc về nhóm đó:

```python
for ten, bang in bang_nhan_su.groupby("phong_ban"):
    print(f"=== Nhóm: {ten} ===")
    print(bang[["chuc_danh", "luong"]])
```

### 1.3. Chọn cột và tập con các cột

- Khi chọn một cột bằng cú pháp ngoặc vuông đơn `df.groupby("phong_ban")["luong"]`, kết quả là một đối tượng `SeriesGroupBy`. Khi tính tổng hợp, nó trả về một Series.
- Khi truyền một danh sách các cột `df.groupby("phong_ban")[["luong", "thuong"]]`, kết quả là một `DataFrameGroupBy`. Khi tính tổng hợp, nó trả về một DataFrame.

### 1.4. Gom nhóm bằng từ điển, Series, hàm và tầng chỉ mục

Khóa gom nhóm không nhất thiết phải là một cột có sẵn trong bảng. Pandas cho phép gom nhóm bằng nhiều phương tiện linh hoạt:
- **Gom nhóm bằng từ điển**: Ánh xạ từng nhãn chỉ mục sang một nhóm mới:
```python
anh_xa = {"Kỹ thuật": "Khối Sản phẩm", "Kinh doanh": "Khối Doanh thu"}
print(bang_nhan_su.set_index("phong_ban").groupby(anh_xa)["luong"].mean())
```
- **Gom nhóm bằng hàm Python**: Bất kỳ hàm số nào nhận giá trị của chỉ mục hàng và trả về tên nhóm đều có thể làm khóa. Chẳng hạn nhóm các từ theo độ dài chuỗi bằng hàm `len`.
- **Gom nhóm theo tầng chỉ mục (Index Levels)**: Với các DataFrame có chỉ mục phân cấp `MultiIndex`, ta chỉ định tham số `level=0` hoặc `level="ten_tang"` để gom nhóm theo tầng mong muốn.

---

## 2. Tổng hợp dữ liệu (Data Aggregation)

Tổng hợp (*Aggregation*) là quá trình rút gọn một mảng nhiều giá trị số học của một nhóm thành một giá trị vô hướng duy nhất (như tổng, trung bình, hay độ lệch chuẩn).

### 2.1. Các hàm tổng hợp tích hợp sẵn

Pandas tối ưu hóa bằng mã C/Cython cho các hàm tổng hợp phổ biến: Các hàm `count()` (đếm giá trị khác NA), `sum()`, `mean()`, `median()`, `std()`, `var()`, `min()`, `max()`, `prod()`, `first()`, `last()`.

### 2.2. Phương thức đa năng `agg` và đặt tên cột tổng hợp

Phương thức `agg()` (hoặc `aggregate()`) cho phép thực thi linh hoạt nhiều phép toán:
- Áp dụng danh sách các hàm: Dùng cú pháp `nhom_pb["luong"].agg(["mean", "std", "count"])`.
- Áp dụng các hàm khác nhau cho từng cột khác nhau bằng từ điển:
```python
nhom_pb.agg({
    "luong": ["min", "max"],
    "thuong": "sum"
})
```
- **Cú pháp đặt tên cột tổng hợp (Named Aggregation)**: Cú pháp hiện đại giúp chỉ định tường minh tên cột đầu ra kèm theo cột gốc và hàm tương ứng, loại bỏ hoàn toàn các tiêu đề cột phân cấp phức tạp:

```python
ket_qua_tong_hop = bang_nhan_su.groupby("phong_ban").agg(
    luong_trung_binh=("luong", "mean"),
    luong_cao_nhat=("luong", "max"),
    tong_tien_thuong=("thuong", "sum"),
    so_nhan_su=("luong", "count")
)
print("Bảng tổng hợp với Named Aggregation:")
print(ket_qua_tong_hop)
assert ket_qua_tong_hop.loc["Kinh doanh", "tong_tien_thuong"] == 1000
```

### 2.3. Trả về kết quả không có chỉ mục nhóm với `as_index=False`

Mặc định, các khóa nhóm sẽ trở thành chỉ mục hàng của bảng kết quả. Nếu muốn các khóa nhóm tiếp tục nằm ở dạng cột thông thường giống như kết quả của câu lệnh `GROUP BY` trong SQL, ta chỉ định tham số `as_index=False`:

```python
df_sql_style = bang_nhan_su.groupby("phong_ban", as_index=False)["luong"].mean()
print(df_sql_style)
assert "phong_ban" in df_sql_style.columns
```

---

## 3. Phép biến đổi nhóm và lọc nhóm (Transforms and Filters)

Trong khi các hàm tổng hợp `agg()` rút gọn mỗi nhóm thành một dòng duy nhất, nhiều bài toán phân tích đòi hỏi phải giữ nguyên toàn bộ số lượng dòng ban đầu.

### 3.1. Phương thức `transform` và phân bổ kết quả nhóm về từng dòng

Phương thức `transform()` áp dụng một hàm lên từng nhóm nhưng trả về một đối tượng có **kích thước và chỉ mục hoàn toàn trùng khớp với DataFrame ban đầu**. Kết quả tính toán của từng nhóm được gán cùng giá trị cho toàn bộ các hàng thuộc về nhóm đó.

Ứng dụng kinh điển nhất của `transform` là tính toán độ lệch so với trung bình nhóm hoặc chuẩn hóa Z-score nội bộ nhóm:
$$
z_i = \frac{x_i - \bar{x}_{\text{nhóm}}}{s_{\text{nhóm}}}
$$

```python
# Tính mức chênh lệch lương của từng nhân viên so với mức trung bình của phòng ban mình
luong_tb_nhom = bang_nhan_su.groupby("phong_ban")["luong"].transform("mean")
bang_nhan_su["chenh_lech_luong"] = bang_nhan_su["luong"] - luong_tb_nhom

print("Bảng sau khi bổ sung chênh lệch lương nội bộ nhóm:")
print(bang_nhan_su[["phong_ban", "chuc_danh", "luong", "chenh_lech_luong"]])

# Tổng chênh lệch trong mỗi nhóm luôn bằng 0
np.testing.assert_allclose(bang_nhan_su.groupby("phong_ban")["chenh_lech_luong"].sum(), 0.0)
```

### 3.2. Lọc nhóm với `filter`

Phương thức `filter()` nhận vào một hàm trả về giá trị logic `True` hoặc `False`. Hàm này được gọi trên từng nhóm. Nếu nhóm thỏa mãn điều kiện, toàn bộ các hàng của nhóm đó sẽ được giữ lại, còn ngược lại thì toàn bộ nhóm bị loại bỏ khỏi bảng dữ liệu:

```python
# Chỉ giữ lại các phòng ban có từ 3 nhân sự trở lên:
phong_dong_nguoi = bang_nhan_su.groupby("phong_ban").filter(lambda g: len(g) >= 3)
print("Các phòng ban có từ 3 nhân sự trở lên:")
print(phong_dong_nguoi)
assert set(phong_dong_nguoi["phong_ban"].unique()) == {"Kỹ thuật"}
```

---

## 4. Phương thức Apply tổng quát: Tách - Áp dụng - Gộp linh hoạt

Phương thức `apply()` là công cụ tổng quát nhất của đối tượng `groupby`. Trong khi `agg` bắt buộc phải trả về giá trị vô hướng và `transform` bắt buộc phải trả về mảng cùng kích thước, `apply()` cho phép hàm tự do trả về một giá trị vô hướng, một Series, hoặc thậm chí một DataFrame con có kích thước tùy ý.

Pandas sẽ tự động ghép nối các mảnh kết quả này lại với nhau dọc theo trục tương ứng.

```python
def lay_top_nhan_vien(df_nhom, n=1, cot="luong"):
    """Trả về top n nhân viên có lương cao nhất trong nhóm."""
    return df_nhom.sort_values(by=cot, ascending=False).head(n)

top_1_moi_phong = bang_nhan_su.groupby("phong_ban", group_keys=False).apply(
    lay_top_nhan_vien, n=1, include_groups=False
)
print("Nhân viên có lương cao nhất mỗi phòng ban:")
print(top_1_moi_phong[["chuc_danh", "luong"]])
assert len(top_1_moi_phong) == 2
```

### 4.1. Khử khóa nhóm với `group_keys=False`

Mặc định, `apply()` sẽ gắn thêm tên nhóm vào chỉ mục để tạo thành chỉ mục phân cấp `MultiIndex`. Khi muốn giữ nguyên chỉ mục hàng nguyên bản của bảng dữ liệu, ta thiết lập tham số `group_keys=False`.

### 4.2. Phân tích theo khoảng và tứ phân vị (Bucket Analysis)

Bằng cách kết hợp `pd.qcut` hoặc `pd.cut` với `groupby`, ta có thể phân tích dữ liệu theo các phân khúc thu nhập hoặc nhóm tuổi:

```python
du_lieu_khach = pd.DataFrame({
    "chi_tieu": np.random.uniform(10, 500, 100),
    "so_lan_mua": np.random.randint(1, 20, 100)
})

# Chia chi tiêu thành 4 khoảng tứ phân vị có số lượng khách bằng nhau:
phan_vi_chi_tieu = pd.qcut(du_lieu_khach["chi_tieu"], 4)
thong_ke_phan_vi = du_lieu_khach.groupby(phan_vi_chi_tieu, observed=False)["so_lan_mua"].agg(["count", "mean"])
print(thong_ke_phan_vi)
assert len(thong_ke_phan_vi) == 4
```

### 4.3. Bốn ví dụ kỹ thuật chuyên sâu với `apply`

#### Ví dụ 1: Điền giá trị khuyết thiếu bằng giá trị đặc thù của từng nhóm
Thay vì điền giá trị trung bình của toàn bộ bảng, ta điền giá trị trung bình riêng của từng bang hoặc từng nhóm sản phẩm:
```python
bang_thieu = pd.DataFrame({
    "khu": ["A", "A", "A", "B", "B"],
    "gia": [100.0, 120.0, np.nan, 200.0, np.nan]
})
dien_theo_khu = bang_thieu.groupby("khu")["gia"].transform(lambda x: x.fillna(x.mean()))
assert dien_theo_khu.iloc[2] == 110.0
assert dien_theo_khu.iloc[4] == 200.0
```

#### Ví dụ 2: Lấy mẫu ngẫu nhiên độc lập theo từng nhóm
Trích xuất ngẫu nhiên đúng $k$ quan sát từ mỗi nhóm để phục vụ kiểm toán hoặc cân bằng mẫu nghiên cứu:
```python
mau_nhom = bang_nhan_su.groupby("phong_ban", group_keys=False).apply(lambda g: g.sample(n=1, random_state=42))
assert len(mau_nhom) == 2
```

#### Ví dụ 3: Giá trị trung bình gia quyền theo nhóm (Group Weighted Average)
Muốn tính doanh thu bình quân trên mỗi đơn vị hàng đã bán, cần dùng số lượng bán làm trọng số của đơn giá. Với n dòng dữ liệu, gọi giá và số lượng ở dòng i là $P_i$ và $Q_i$. Tổng doanh thu V và tổng số lượng Q được khai triển như sau:
$$
V = P_1Q_1 + P_2Q_2 + \cdots + P_nQ_n.
$$

$$
Q = Q_1+Q_2+\cdots+Q_n.
$$

Viết gọn, $V=\sum_{i=1}^n P_iQ_i$ và $Q=\sum_{i=1}^n Q_i$. Với Q dương, giá bình quân trên một đơn vị hàng là:

$$
\bar P = \frac{V}{Q}.
$$

**Điều kiện xác định của mẫu số**: Phép tính trung bình gia quyền chỉ có nghĩa khi tổng trọng số dương $\sum_{i=1}^n Q_i > 0$ và mọi trọng số đều không âm ($Q_i \ge 0$). Nếu một nhóm có tổng sản lượng bằng 0 hoặc trọng số bị khuyết toàn bộ, mẫu số bằng 0 sẽ dẫn đến phép chia không xác định (`ZeroDivisionError` hoặc `NaN`). Do đó, hàm tính toán cần kiểm tra điều kiện mẫu số trước khi chia:

```python
df_ban_hang = pd.DataFrame({
    "loai": ["Điện tử", "Điện tử", "Gia dụng", "Gia dụng"],
    "don_gia": [100, 200, 50, 80],
    "so_luong": [10, 2, 20, 5]
})

def tinh_tb_gia_quyen(g):
    tong_luong = g["so_luong"].sum()
    if tong_luong <= 0 or pd.isna(tong_luong):
        return np.nan
    return (g["don_gia"] * g["so_luong"]).sum() / tong_luong

tb_gia_quyen = df_ban_hang.groupby("loai").apply(tinh_tb_gia_quyen, include_groups=False)
print("Đơn giá trung bình gia quyền theo loại sản phẩm:")
print(tb_gia_quyen)
assert np.isclose(tb_gia_quyen["Điện tử"], (100*10 + 200*2) / 12)
assert np.isclose(tb_gia_quyen["Gia dụng"], (50*20 + 80*5) / 25)
```

#### Ví dụ 4: Ước lượng mô hình hồi quy tuyến tính theo từng nhóm
Áp dụng phép hồi quy tuyến tính $y = ax + b$ riêng rẽ cho từng nhóm dữ liệu bằng thư viện NumPy:

```python
df_kinh_te = pd.DataFrame({
    "vung": ["A", "A", "A", "B", "B", "B"],
    "quang_cao": [1, 2, 3, 1, 2, 3],
    "doanh_thu": [2.1, 4.2, 5.9, 1.5, 3.1, 4.4]
})

def hoi_quy_nhom(g):
    # Ước lượng hệ số góc và hệ số tự do: y = a*x + b
    a, b = np.polyfit(g["quang_cao"], g["doanh_thu"], deg=1)
    return pd.Series({"he_so_goc": a, "he_so_tu_do": b})

ket_qua_hoi_quy = df_kinh_te.groupby("vung").apply(hoi_quy_nhom, include_groups=False)
print("Hệ số hồi quy theo từng vùng:")
print(ket_qua_hoi_quy)
assert ket_qua_hoi_quy.loc["A", "he_so_goc"] > ket_qua_hoi_quy.loc["B", "he_so_goc"]
```

---

## 5. Bảng Pivot và Bảng chéo (Pivot Tables and Cross-Tabulation)

Bảng Pivot và Bảng chéo là hai công cụ tổng hợp đa chiều cao cấp, thường xuyên xuất hiện trong các báo cáo kinh doanh.

### 5.1. Bảng Pivot với `pd.pivot_table`

Khác với hàm `pivot` cơ bản vốn bị lỗi khi gặp dữ liệu trùng lặp khóa, hàm `pivot_table` cho phép gom nhóm và áp dụng hàm tổng hợp số học:
- `values`: Cột dữ liệu số học cần tổng hợp.
- `index`: Danh sách các cột sẽ làm chỉ mục hàng.
- `columns`: Danh sách các cột sẽ làm tiêu đề cột mới.
- `aggfunc`: Hàm tổng hợp (mặc định là `"mean"`).
- `fill_value`: Giá trị thay thế cho các ô khuyết thiếu phát sinh (thường là 0).
- `margins=True`: Tự động tính toán thêm dòng và cột tổng cộng (*All*):

```python
bang_pivot = pd.pivot_table(
    bang_nhan_su,
    values="luong",
    index="phong_ban",
    columns="chuc_danh",
    aggfunc="mean",
    fill_value=0,
    margins=True
)
print("Bảng Pivot lương trung bình:")
print(bang_pivot)
assert bang_pivot.loc["Kỹ thuật", "Lập trình viên"] == 2100
```

### 5.2. Bảng chéo với `pd.crosstab`

Hàm `pd.crosstab()` là trường hợp đặc biệt của bảng Pivot, được thiết kế chuyên biệt để đếm **tần số xuất hiện đồng thời (Frequency Counts)** giữa hai hoặc nhiều biến phân loại:
- `margins=True`: Thêm dòng và cột tổng số lượng quan sát.
- `normalize`: Chuẩn hóa tần số thành tỷ lệ phần trăm:
  - `normalize="all"`: Chia cho tổng số quan sát của toàn bộ bảng.
  - `normalize="index"`: Chia theo tổng số của từng hàng (tổng mỗi hàng bằng 100%).
  - `normalize="columns"`: Chia theo tổng số của từng cột (tổng mỗi cột bằng 100%).

```python
df_khao_sat_xe = pd.DataFrame({
    "quoc_gia": ["Mỹ", "Mỹ", "Nhật", "Nhật", "Đức", "Nhật"],
    "loai_xe": ["Xăng", "Điện", "Điện", "Xăng", "Xăng", "Điện"]
})

bang_tan_so = pd.crosstab(
    df_khao_sat_xe["quoc_gia"],
    df_khao_sat_xe["loai_xe"],
    margins=True
)
print("Bảng chéo tần số loại xe theo quốc gia:")
print(bang_tan_so)
assert bang_tan_so.loc["Nhật", "Điện"] == 2
assert bang_tan_so.loc["All", "All"] == 6
```

---

## 7. Tổng kết

1. **Hiểu rõ ba pha Split-Apply-Combine**: Phân biệt rạch ròi giữa việc tách nhóm, áp dụng hàm xử lý và gộp kết quả. Đối tượng `groupby` hoạt động theo cơ chế đánh giá trì hoãn và chỉ tính toán khi được gọi hàm cụ thể.
2. **Khai thác Named Aggregation**: Sử dụng cú pháp `agg(ten_moi=('cot', 'ham'))` để tạo ra các bảng tổng hợp sạch sẽ, có tên cột tường minh và không bị chỉ mục phân cấp phức tạp.
3. **Phân biệt `agg` và `transform`**: Sử dụng `agg` khi cần rút gọn mỗi nhóm thành một dòng giá trị thống kê, còn sử dụng `transform` khi cần gán kết quả của nhóm về từng dòng để chuẩn hóa hoặc tính chênh lệch nội bộ nhóm.
4. **Lọc nhóm với `filter`**: Loại trừ toàn bộ các nhóm không thỏa mãn điều kiện logic dựa trên đặc tính tổng thể của nhóm.
5. **Linh hoạt xử lý với `apply`**: Áp dụng các hàm tùy biến tự do để giải quyết các bài toán phức tạp như lấy mẫu ngẫu nhiên theo nhóm, tính trung bình gia quyền hay ước lượng mô hình hồi quy.
6. **Tổng hợp đa chiều với Pivot và Crosstab**: Sử dụng `pivot_table` để tổng hợp số học trên ma trận hai chiều, đồng thời sử dụng `crosstab` để đo lường tần số xuất hiện đồng thời và phân tích bảng tiếp liên.

---

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 10: Data Aggregation and Group Operations](https://wesmckinney.com/book/data-aggregation).
- Tài liệu chính thức pandas: [Tài liệu hướng dẫn Group by: Split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html).
- Hadley Wickham, *The Split-Apply-Combine Strategy for Data Analysis*, Journal of Statistical Software, 2011.
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 6. Bài tập rèn luyện

<span id="iai-05-bai-3"></span>

::: exercise Bài tập 1: Tính giá trung bình chung từ thống kê nhóm
Một báo cáo thị trường lưu trú cung cấp dữ liệu giá phòng đã biết (USD/đêm) của hai khu vực A và B như sau:

| Khu vực | Giá trung bình ($\bar{x}_k$) | Số lượng giá đã biết ($n_k$) |
| :--- | :--- | :--- |
| Khu A | 100 | 2 |
| Khu B | 200 | 8 |

Từ bảng tổng hợp trên, hãy tính giá trung bình của toàn bộ $10$ quan sát đã biết trên toàn thị trường. Phân tích nguyên nhân vì sao con số $150$ là một sai lầm nghiêm trọng trong thống kê.
:::

::: solution Lời giải
### 1. Phân tích bản chất toán học
Nếu một người lấy trung bình cộng đơn giản của hai số trung bình khu:
$$
\frac{100 + 200}{2} = 150
$$
Phép tính này cho hai trung bình nhóm trọng số bằng nhau, trong khi đề yêu cầu trung bình trên từng giá quan sát được. Hai câu hỏi chỉ cho cùng kết quả trong những trường hợp thích hợp, chẳng hạn khi hai nhóm có cùng số giá hợp lệ. Ở đây cần dùng số quan sát của mỗi nhóm làm trọng số.

Trong thực tế:
- Tổng giá trị của 2 phòng ở khu A là: $100 \times 2 = 200\text{ USD}$.
- Tổng giá trị của 8 phòng ở khu B là: $200 \times 8 = 1600\text{ USD}$.
- Tổng giá trị của toàn bộ 10 phòng là: $200 + 1600 = 1800\text{ USD}$.

Giá trị trung bình chuẩn xác của toàn bộ 10 quan sát phải là giá trị **trung bình gia quyền (Weighted Average)** theo quy mô mẫu:
$$
\begin{aligned}
\bar x &= \frac{100\cdot2+200\cdot8}{2+8}, \\
&= \frac{1800}{10}, \\
&= 180.
\end{aligned}
$$

Điều kiện xác định của công thức là tổng quy mô mẫu ở mẫu số phải dương ($\sum_{k=1}^m n_k > 0$) và các trọng số thành phần không âm ($n_k \ge 0$). Nếu thị trường không có quan sát nào ($n_A + n_B = 0$), mẫu số bằng 0 và giá trung bình chung không xác định.

### 2. Kiểm chứng bằng mã nguồn Python

```python
bang_khu = pd.DataFrame({
    "khu": ["A", "B"],
    "gia_tb": [100.0, 200.0],
    "so_luong": [2, 8]
})

# Tính tổng tiền và tổng số lượng
tong_tien = (bang_khu["gia_tb"] * bang_khu["so_luong"]).sum()
tong_so_luong = bang_khu["so_luong"].sum()
assert tong_so_luong > 0, "Mẫu số phải lớn hơn 0"
gia_tb_chung = tong_tien / tong_so_luong

print("Tổng giá trị toàn thị trường:", tong_tien)
print("Tổng số lượng phòng:", tong_so_luong)
print("Giá trung bình thực tế toàn thị trường:", gia_tb_chung)

assert gia_tb_chung == 180.0
```

Con số $180$ phản ánh đúng thực tế vì khu B có mức giá cao hơn ($200$) và chiếm tới $80\%$ quy mô thị trường ($8/10$ phòng), do đó trọng tâm của phân phối giá bị kéo lệch mạnh về phía $200$.
:::

---




<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-05-groupby">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-05-groupby.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 10: Data Aggregation and Group Operations](https://wesmckinney.com/book/data-aggregation).
- Tài liệu chính thức pandas: [Tài liệu hướng dẫn Group by: Split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html).
- Hadley Wickham, *The Split-Apply-Combine Strategy for Data Analysis*, Journal of Statistical Software, 2011.
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
