---
course: xu-ly-du-lieu
lecture: bai-08-ghep-bang-chuyen-dang
section: lecture
title: "Chỉ mục phân cấp, ghép bảng và chuyển dạng"
prerequisites: ["dataframe", "chi-muc"]
lessonStatus: ready
hasChapterExercises: true
description: "Làm chủ chỉ mục phân cấp MultiIndex, các phép ghép bảng quan hệ merge và join, kỹ thuật nối trục concat, ghép chồng combine_first, cùng các phép chuyển dạng stack/unstack và pivot/melt."
---


<div class="lecture-notes-content">

Để phân tích dữ liệu hiệu quả, người làm dữ liệu cần kết nối các nguồn bảng rời rạc bằng các phép toán quan hệ. Đồng thời, cấu trúc bảng cũng cần chuyển đổi linh hoạt giữa dạng dài (*Long format*) và dạng rộng (*Wide format*) cho các bước vẽ đồ thị hay huấn luyện mô hình. Bài học này trình bày có hệ thống các kỹ thuật: Tổ chức dữ liệu đa chiều bằng chỉ mục phân cấp, ghép bảng quan hệ, nối trục và xoay hình dạng bảng trong pandas.

---

## 1. Chỉ mục phân cấp (Hierarchical Indexing / MultiIndex)

Chỉ mục phân cấp (*Hierarchical Indexing*, được hiện thực hóa qua lớp `MultiIndex` trong pandas) là cơ chế cho phép bạn sở hữu hai hoặc nhiều tầng chỉ mục trên cùng một trục. Nhờ đó, ta có thể thao tác với dữ liệu nhiều chiều (3 chiều, 4 chiều) trong khuôn khổ của cấu trúc DataFrame hai chiều quen thuộc.

### 1.1. Khởi tạo và trích chọn dữ liệu với `.loc`

Ta có thể khởi tạo một `MultiIndex` từ danh sách các bộ giá trị (*tuples*), mảng song song, hoặc tích Descartes giữa các tập nhãn (*product*):

```python
import numpy as np
import pandas as pd

# Khởi tạo MultiIndex từ danh sách các cặp (khu_vuc, nam)
cac_cap = [
    ("Bắc", 2025), ("Bắc", 2026),
    ("Nam", 2025), ("Nam", 2026)
]
chi_muc = pd.MultiIndex.from_tuples(cac_cap, names=["khu_vuc", "nam"])

du_lieu = pd.Series([120, 150, 200, 260], index=chi_muc)
print("Series với chỉ mục phân cấp:")
print(du_lieu)
```

Điểm mạnh vượt trội của `MultiIndex` là khả năng **trích chọn bộ phận (Partial Indexing)**:
- Truy xuất tầng ngoài cùng: Cú pháp `du_lieu.loc["Bắc"]` sẽ trích xuất toàn bộ dữ liệu của khu vực Bắc dưới dạng một Series thông thường với chỉ mục là `nam`.
- Truy xuất phần tử cụ thể: Truyền một bộ giá trị `du_lieu.loc[("Bắc", 2026)]`.
- Truy xuất tầng bên trong: Sử dụng toán tử cắt lát kết hợp với `pd.IndexSlice`:

```python
print("Dữ liệu khu vực Bắc:")
print(du_lieu.loc["Bắc"])
assert du_lieu.loc[("Bắc", 2026)] == 150
```

### 1.2. Đảo và sắp xếp các tầng chỉ mục

Khi làm việc với chỉ mục phân cấp, thứ tự sắp xếp của các tầng đóng vai trò quyết định đến hiệu năng truy xuất:
- `swaplevel()`: Hoán đổi vị trí giữa hai tầng chỉ mục cụ thể.
- `sort_index(level=...)`: Sắp xếp các giá trị theo thứ tự từ điển tại một tầng được chỉ định.

> [!TIP] Nguyên tắc sắp xếp chỉ mục phân cấp
> Các phép trích chọn bộ phận và cắt lát dải nhãn trên `MultiIndex` sẽ đạt hiệu năng cao nhất và không bao giờ gặp cảnh báo lỗi khi chỉ mục đã được sắp xếp từ điển tăng dần bằng phương thức `sort_index()`.

```python
du_lieu_dao = du_lieu.swaplevel("khu_vuc", "nam").sort_index()
print("Series sau khi đảo tầng và sắp xếp:")
print(du_lieu_dao)
assert du_lieu_dao.index.names == ["nam", "khu_vuc"]
```

### 1.3. Thống kê tổng hợp theo tầng chỉ mục

Thay vì phải phá vỡ cấu trúc bảng, các phương thức thống kê tổng hợp của pandas cho phép thực hiện phép tính trực tiếp trên một tầng chỉ mục thông qua phương thức `groupby(level=...)`:

```python
# Tính tổng doanh thu theo từng khu vực bất kể năm:
tong_theo_khu = du_lieu.groupby(level="khu_vuc").sum()
print("Tổng doanh thu theo khu vực:")
print(tong_theo_khu)
assert tong_theo_khu["Bắc"] == 270
assert tong_theo_khu["Nam"] == 460
```

### 1.4. Chuyển đổi qua lại giữa cột và chỉ mục

Hai phương thức cơ bản giúp luân chuyển dữ liệu giữa các cột thông thường và chỉ mục:
- `set_index([cot_1, cot_2])`: Đưa một hoặc nhiều cột hiện tại lên làm chỉ mục phân cấp (sử dụng `drop=False` nếu muốn giữ lại các cột đó trong phần thân dữ liệu).
- `reset_index()`: Đưa các tầng chỉ mục trở lại thành các cột dữ liệu thông thường, chuyển chỉ mục hàng về dạng số tự tăng `RangeIndex`.

---

## 2. Ghép và nối các tập dữ liệu (Combining and Merging)

Việc kết hợp nhiều bảng dữ liệu được thực hiện thông qua ba cơ chế toán học rạch ròi: Phép ghép theo kiểu cơ sở dữ liệu quan hệ (`merge`), phép nối dọc theo một trục tọa độ (`concat`), và phép ghép bù đắp dữ liệu khuyết (`combine_first`).

### 2.1. Phép ghép bảng kiểu cơ sở dữ liệu với `pd.merge`

Hàm `pd.merge()` kết nối các hàng của hai DataFrame dựa trên một hoặc nhiều khóa chung (*keys*), tương đương với mệnh đề `JOIN` trong ngôn ngữ SQL:
- `on`: Tên cột làm khóa ghép khi cả hai bảng đều dùng chung một tên cột.
- `left_on`, `right_on`: Chỉ định tên cột khóa riêng biệt khi hai bảng đặt tên cột khác nhau.
- `how`: Phương thức ghép nối:
  - `"inner"` (mặc định): Phép giao (*Inner Join*), chỉ giữ lại các bản ghi có khóa xuất hiện đồng thời ở cả hai bảng.
  - `"left"`: Phép ghép trái (*Left Join*), giữ lại toàn bộ các hàng của bảng bên trái, còn các hàng không tìm thấy đối tác bên phải sẽ nhận giá trị `NaN`.
  - `"right"`: Phép ghép phải (*Right Join*), giữ lại toàn bộ các hàng của bảng bên phải.
  - `"outer"`: Phép hợp (*Outer Join*), giữ lại toàn bộ các bản ghi của cả hai bảng, trong đó phần thiếu ở mỗi bên được điền `NaN`.
- `suffixes=("_trai", "_phai")`: Hậu tố tự động gán vào tên các cột không phải khóa nhưng bị trùng tên giữa hai bảng.

#### Bản số ghép nối và nhân số hàng (Merge Cardinality)
Quan hệ giữa các bảng khi ghép có thể thuộc một trong bốn dạng bản số:
- **Một - Một (1:1)**: Mỗi giá trị khóa xuất hiện duy nhất một lần ở mỗi bảng.
- **Một - Nhiều (1:N) hoặc Nhiều - Một (N:1)**: Khóa ở một bảng là duy nhất (chẳng hạn bảng danh mục sản phẩm), còn ở bảng kia xuất hiện lặp lại (bảng nhật ký giao dịch).
- **Nhiều - Nhiều (N:M)**: Khóa xuất hiện lặp lại ở cả hai bảng. Khi một giá trị khóa xuất hiện $m$ lần ở bảng trái và $n$ lần ở bảng phải, phép ghép sẽ tạo ra tích Descartes nội bộ gồm $m \times n$ hàng cho riêng giá trị khóa đó.

#### Hành vi của khóa mang giá trị khuyết thiếu (`NaN`)
Trong ngôn ngữ SQL chuẩn, `NULL` biểu thị dữ liệu chưa biết nên biểu thức so sánh `NULL = NULL` trả về `UNKNOWN`, làm cho các hàng mang khóa `NULL` không bao giờ ghép khớp với nhau. Ngược lại, trong pandas `pd.merge()`, giá trị khuyết thiếu (`NaN`) mặc định được đối xử như hai giá trị bằng nhau. Nếu cả hai bảng đều chứa các hàng mang khóa `NaN`, phép ghép sẽ nối các dòng `NaN` lại với nhau và sinh ra tích Descartes giữa các bản ghi thiếu khóa:

```python
bang_a = pd.DataFrame({"khoa": ["K1", "K1", np.nan], "gt_a": [1, 2, 3]})
bang_b = pd.DataFrame({"khoa": ["K1", "K1", np.nan], "gt_b": [10, 20, 30]})

# Khóa 'K1' sinh 2x2 = 4 hàng, khóa NaN sinh 1x1 = 1 hàng: Tổng 5 hàng
bang_ghep_khoa = pd.merge(bang_a, bang_b, on="khoa", how="inner")
print("Bảng ghép với khóa có NaN và trùng lặp:")
print(bang_ghep_khoa)
assert len(bang_ghep_khoa) == 5
assert bang_ghep_khoa["khoa"].isna().sum() == 1
```

Nếu bài toán nghiệp vụ không coi các bản ghi thiếu khóa là cùng một thực thể, bạn cần lọc bỏ hoặc xử lý `NaN` trên cột khóa trước khi thực hiện ghép bảng.

```python
bang_sinh_vien = pd.DataFrame({
    "ma_sv": ["SV01", "SV02", "SV03"],
    "ho_ten": ["An", "Bình", "Cường"],
    "khoa": ["CNTT", "Kinh tế", "CNTT"]
})

bang_diem = pd.DataFrame({
    "ma_sv": ["SV01", "SV02", "SV04"],
    "diem_gpa": [3.6, 3.2, 3.8]
})

# Ghép toàn bộ sinh viên và điểm số bằng phép Left Join
df_hop_nhat = pd.merge(bang_sinh_vien, bang_diem, on="ma_sv", how="left")
print("Bảng sau phép Left Join:")
print(df_hop_nhat)
assert len(df_hop_nhat) == 3
assert pd.isna(df_hop_nhat.loc[df_hop_nhat["ma_sv"] == "SV03", "diem_gpa"].iloc[0])
```

### 2.2. Kiểm thực cấu trúc ghép nối với tham số `validate`

Một trong những sai lầm nghiêm trọng nhất khi ghép bảng là **hiện tượng bùng nổ số hàng do tích Descartes ngầm** (*Cartesian Explosion*). Giả sử bạn muốn gắn thông tin danh mục vào bảng đơn hàng (kỳ vọng quan hệ nhiều - một). Nếu vô tình bảng danh mục bị trùng lặp khóa, mỗi đơn hàng sẽ bị nhân đôi hoặc nhân ba số dòng, làm sai lệch toàn bộ báo cáo doanh thu kế toán!

Để phòng vệ tuyệt đối, pandas cung cấp tham số `validate`:
- `validate="one_to_one"`: Kiểm tra khóa ở cả hai bảng đều là duy nhất tuyệt đối.
- `validate="one_to_many"`: Khóa ở bảng trái là duy nhất, bảng phải có thể lặp.
- `validate="many_to_one"`: Khóa ở bảng trái có thể lặp, bảng phải bắt buộc là duy nhất.
- `validate="many_to_many"`: Cho phép quan hệ nhiều - nhiều ở cả hai bên.

Nếu cấu trúc khóa thực tế vi phạm khai báo, pandas sẽ lập tức ném ra lỗi `MergeError` để dừng tiến trình, ngăn chặn việc sản sinh dữ liệu sai:

```python
try:
    # Bảng tra cứu không được phép trùng lặp khóa:
    tra_cuu_loi = pd.DataFrame({"ma_sv": ["SV01", "SV01"], "hoc_bong": [500, 700]})
    pd.merge(bang_sinh_vien, tra_cuu_loi, on="ma_sv", validate="many_to_one")
except pd.errors.MergeError:
    print("Bắt lỗi thành công: Khóa bảng tra cứu bị trùng lặp!")
```

### 2.3. Ghép nối dựa trên chỉ mục hàng (`join`)

Khi một hoặc cả hai bảng muốn sử dụng chính chỉ mục hàng (*Index*) làm khóa ghép, ta có thể chỉ định `left_index=True` hoặc `right_index=True`. Ngoài ra, phương thức tiện ích `df.join()` mặc định sử dụng chỉ mục hàng để ghép nối, rất thuận tiện khi hợp nhất nhiều DataFrame có chung chỉ mục.

### 2.4. Nối dữ liệu dọc theo trục với `pd.concat`

Khác với `merge` dựa trên giá trị khóa, hàm `pd.concat()` thực hiện thao tác dán ghép vật lý các mảng dữ liệu dọc theo một trục tọa độ:
- `axis=0` (mặc định): Nối theo chiều dọc (thêm các hàng mới vào bên dưới).
- `axis=1`: Nối theo chiều ngang (thêm các cột mới vào bên phải).
- `join="inner"`: Chỉ giữ lại các cột (hoặc hàng) xuất hiện ở cả hai bên, trong khi `join="outer"` (mặc định) giữ lại tất cả và điền `NaN` vào phần chênh lệch.
- `ignore_index=True`: Xóa bỏ chỉ mục cũ và đánh số lại chỉ mục từ $0$ đến $N-1$, loại trừ nguy cơ trùng lặp chỉ mục hàng.
- `keys=[...]`: Tạo một tầng chỉ mục phân cấp mới ở ngoài cùng để đánh dấu xuất xứ của từng khối dữ liệu được ghép:

```python
thang_1 = pd.DataFrame({"doanh_thu": [100, 150]}, index=["SP1", "SP2"])
thang_2 = pd.DataFrame({"doanh_thu": [120, 180]}, index=["SP1", "SP2"])

# Nối theo chiều dọc và phân tầng theo tháng
df_noi = pd.concat([thang_1, thang_2], keys=["T1", "T2"])
print("Bảng nối với MultiIndex:")
print(df_noi)
assert df_noi.loc[("T2", "SP1"), "doanh_thu"] == 120
```

### 2.5. Ghép chồng dữ liệu có phần khuyết bằng `combine_first`

Trong các bài toán làm sạch dữ liệu, ta thường có một nguồn dữ liệu chính nhưng bị khuyết thiếu một số ô, và một nguồn dữ liệu phụ dùng để chắp vá. Phương thức `df1.combine_first(df2)` sẽ thực hiện cơ chế: Giữ nguyên các giá trị hợp lệ của `df1`, và chỉ lấy giá trị từ `df2` để lấp đầy những vị trí mà `df1` đang mang giá trị `NaN`:

```python
du_lieu_chinh = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5], index=list("abcde"))
du_lieu_phu = pd.Series([1.0, 9.9, 3.0, 9.9, 9.9], index=list("abcde"))

ket_qua_va = du_lieu_chinh.combine_first(du_lieu_phu)
print("Dữ liệu sau khi vá ô trống:")
print(ket_qua_va)
assert ket_qua_va["a"] == 1.0
assert ket_qua_va["b"] == 2.5
```

---

## 3. Chuyển dạng và xoay bảng (Reshaping and Pivoting)

Cấu trúc hình học của dữ liệu quyết định khả năng tính toán và trực quan hóa:
- **Dạng dài (Long format / Tidy data)**: Mỗi quan sát là một hàng riêng biệt, các biến số được biểu diễn bằng cột định danh và cột giá trị. Định dạng này lý tưởng cho các thư viện phân tích nhóm và đồ họa hiện đại như Seaborn.
- **Dạng rộng (Wide format)**: Các mức giá trị của một biến được trải rộng thành các cột riêng biệt, thuận tiện cho mắt người đọc báo cáo tổng hợp.

### 3.1. Chuyển dạng với `stack` và `unstack`

Cặp phương thức `stack()` và `unstack()` luân chuyển dữ liệu qua lại giữa cột và hàng dựa trên chỉ mục phân cấp:
- `unstack()`: Nhấc một tầng của chỉ mục hàng (*Row Index*) xoay lên làm tiêu đề cột (*Column Header*), biến bảng từ dạng dài thành dạng rộng hơn.
- `stack()`: Gom các tiêu đề cột nén ngược trở lại thành một tầng của chỉ mục hàng, biến bảng từ dạng rộng thành dạng dài hơn.

```python
bang_goc = pd.DataFrame(
    [[10, 20], [30, 40]],
    index=["Hà Nội", "Đà Nẵng"],
    columns=["Quý 1", "Quý 2"]
)

# Chuyển từ dạng rộng sang dạng dài bằng stack:
bang_dai = bang_goc.stack()
print("Bảng sau khi stack:")
print(bang_dai)

# Khôi phục lại dạng ban đầu bằng unstack:
bang_khoi_phuc = bang_dai.unstack()
assert bang_khoi_phuc.equals(bang_goc)
```

### 3.2. Chuyển dạng dài sang dạng rộng với `pivot`

Phương thức `pivot(index=..., columns=..., values=...)` cho phép tái cấu trúc một bảng dạng dài thành bảng dạng rộng dựa trên các cột nghiệp vụ:
- `index`: Cột sẽ trở thành chỉ mục hàng của bảng mới.
- `columns`: Cột có các giá trị phân loại sẽ được bung ra thành các tiêu đề cột mới.
- `values`: Cột chứa dữ liệu số học sẽ được điền vào phần thân bảng.

```python
nhat_ky_gia = pd.DataFrame({
    "ngay": ["2026-01-01", "2026-01-01", "2026-01-02", "2026-01-02"],
    "ma_cp": ["FPT", "VNM", "FPT", "VNM"],
    "gia_dong_cua": [120, 75, 122, 74]
})

bang_gia_rong = nhat_ky_gia.pivot(index="ngay", columns="ma_cp", values="gia_dong_cua")
print("Bảng giá dạng rộng:")
print(bang_gia_rong)
assert bang_gia_rong.loc["2026-01-02", "FPT"] == 122
```

> [!WARNING] Điều kiện tiên quyết của `pivot`
> Phương thức `pivot` bắt buộc mỗi cặp `(index, columns)` chỉ được xuất hiện duy nhất một lần. Nếu tồn tại nhiều bản ghi trùng lặp cho cùng một cặp chỉ mục và cột, `pivot` sẽ báo lỗi `ValueError`. Trong tình huống có dữ liệu trùng lặp cần tổng hợp, ta bắt buộc phải sử dụng `pivot_table` (sẽ học ở bài học tổng hợp nhóm).

### 3.3. Chuyển dạng rộng sang dạng dài với `melt`

Ngược lại với `pivot`, phương thức `pd.melt()` cho phép nén nhiều cột thành một cặp cột duy nhất gồm "tên thuộc tính" và "giá trị":
- `id_vars`: Danh sách các cột đóng vai trò là mã định danh, được giữ nguyên vị trí.
- `value_vars`: Danh sách các cột cần nén lại thành hàng (nếu bỏ qua, pandas sẽ nén toàn bộ các cột còn lại).
- `var_name`: Tên của cột mới lưu trữ tên các thuộc tính cũ.
- `value_name`: Tên của cột mới lưu trữ giá trị số học.

```python
bang_doanh_so = pd.DataFrame({
    "chi_nhanh": ["CN1", "CN2"],
    "Thang1": [500, 700],
    "Thang2": [600, 800]
})

bang_chay_dai = pd.melt(
    bang_doanh_so,
    id_vars=["chi_nhanh"],
    value_vars=["Thang1", "Thang2"],
    var_name="thoi_gian",
    value_name="doanh_so"
)
print("Bảng sau khi melt:")
print(bang_chay_dai)
assert len(bang_chay_dai) == 4
assert bang_chay_dai["doanh_so"].sum() == 2600
```

---

## 5. Tổng kết

1. **Làm chủ chỉ mục phân cấp**: Sử dụng `MultiIndex` để quản lý dữ liệu nhiều chiều trên cấu trúc hai chiều, đồng thời nên gọi `sort_index()` để tối ưu hóa hiệu năng trích chọn bộ phận với `.loc`.
2. **Kỷ luật khi ghép bảng với `merge`**: Luôn định hình rõ mối quan hệ giữa các bảng ($1-1$, $1-N$, $N-1$) và sử dụng tham số `validate` để ngăn ngừa nguy cơ bùng nổ số hàng do tích Descartes ngoài ý muốn.
3. **Phân biệt rạch ròi giữa `merge` và `concat`**: Sử dụng `merge` khi cần kết nối dữ liệu dựa trên giá trị của các cột khóa chung, còn sử dụng `concat` khi cần dán ghép các mảng dữ liệu vật lý dọc theo chiều hàng hoặc chiều cột.
4. **Vá dữ liệu với `combine_first`**: Tận dụng cơ chế ghép chồng để lấp đầy các ô trống trong bảng dữ liệu chính bằng thông tin từ nguồn phụ trợ mà không ghi đè lên các giá trị hợp lệ đã có.
5. **Linh hoạt chuyển dạng dữ liệu**: Sử dụng `stack`/`unstack` cho cấu trúc có chỉ mục phân cấp, đồng thời chuyển đổi thuần thục giữa dạng dài và dạng rộng bằng `pivot` và `melt` để đáp ứng yêu cầu của từng giai đoạn phân tích.

---

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 8: Data Wrangling: Join, Combine, and Reshape](https://wesmckinney.com/book/data-wrangling).
- Tài liệu chính thức pandas: [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html) & [Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html).
- Hadley Wickham, *Tidy Data*, Journal of Statistical Software, 2014.
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 4. Bài tập rèn luyện

<span id="iai-05-bai-4"></span>

::: exercise Bài tập 1: Ghép trái khi khóa lặp ở cả hai bảng
Cho hai bảng dữ liệu độc lập về hệ thống phòng nghỉ và khu vực địa lý:

Bảng `trai`:

| id | khu |
| :--- | :--- |
| P1 | A |
| P2 | A |
| P3 | B |

Bảng `phai`:

| khu | vung |
| :--- | :--- |
| A | Bắc |
| A | Trung tâm |

Hãy viết câu lệnh ghép hai bảng trên bằng phương thức `Left Join` trên cột khóa `khu`. Xác định rõ cấu trúc, số lượng hàng và giá trị cụ thể của từng hàng trong bảng kết quả. Giải thích cơ chế khớp dòng của thuật toán.
:::

::: solution Lời giải
Câu lệnh thực thi trong pandas:

```python
trai = pd.DataFrame({
    "id": ["P1", "P2", "P3"],
    "khu": ["A", "A", "B"]
})

phai = pd.DataFrame({
    "khu": ["A", "A"],
    "vung": ["Bắc", "Trung tâm"]
})

ket_qua_ghep = trai.merge(phai, on="khu", how="left")
print("Bảng kết quả sau phép Left Join:")
print(ket_qua_ghep)

assert len(ket_qua_ghep) == 5
assert ket_qua_ghep["vung"].tolist() == ["Bắc", "Trung tâm", "Bắc", "Trung tâm", np.nan] or \
       set(zip(ket_qua_ghep["id"], ket_qua_ghep["vung"])) == {
           ("P1", "Bắc"), ("P1", "Trung tâm"),
           ("P2", "Bắc"), ("P2", "Trung tâm"),
           ("P3", np.nan)
       }
```

Bảng kết quả gồm chính xác $5$ hàng theo thứ tự:
1. `(P1, A, Bắc)`
2. `(P1, A, Trung tâm)`
3. `(P2, A, Bắc)`
4. `(P2, A, Trung tâm)`
5. `(P3, B, NaN)`

**Phân tích cơ chế kỹ thuật**:
- Hàng đầu tiên của bảng trái (`P1`, `A`) khớp với hai hàng có mã `A` bên bảng phải, do đó sản sinh ra hai hàng tương ứng với vùng `Bắc` và `Trung tâm`.
- Hàng thứ hai của bảng trái (`P2`, `A`) cũng khớp với hai hàng bên bảng phải, tiếp tục sản sinh thêm hai hàng.
- Hàng thứ ba của bảng trái (`P3`, `B`) không tìm thấy mã `B` ở bảng phải. Tuy nhiên, vì sử dụng phương thức ghép `how="left"`, toàn bộ các hàng của bảng trái bắt buộc phải được bảo toàn. Do đó, dòng `P3` được giữ lại và trường thuộc tính `vung` được điền giá trị khuyết thiếu `NaN`.
:::

---




<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-05-merge">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-05-merge.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 8: Data Wrangling: Join, Combine, and Reshape](https://wesmckinney.com/book/data-wrangling).
- Tài liệu chính thức pandas: [Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html) & [Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html).
- Hadley Wickham, *Tidy Data*, Journal of Statistical Software, 2014.
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
