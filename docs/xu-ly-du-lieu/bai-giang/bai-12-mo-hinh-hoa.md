---
course: xu-ly-du-lieu
lecture: bai-12-mo-hinh-hoa
section: lecture
title: "Từ bảng dữ liệu đến mô hình thống kê và dự đoán"
prerequisites: ["dataframe", "thong-ke-mo-ta"]
lessonStatus: ready
hasChapterExercises: true
description: "Kết nối dữ liệu bảng với mô hình học máy và thống kê: Chuẩn bị ma trận đặc trưng, công thức mô hình hóa Patsy, hồi quy OLS và chuỗi thời gian với statsmodels, quy trình scikit-learn chống rò rỉ dữ liệu."
---


<div class="lecture-notes-content">

Một trong những mục tiêu tối hậu của quy trình xử lý dữ liệu là chuyển giao tri thức từ dạng bảng quan sát sang các cấu trúc toán học có khả năng giải thích quy luật hoặc dự báo tương lai. Các thư viện như pandas cung cấp nền tảng chuẩn mực cho việc nạp, làm sạch và tổng hợp dữ liệu, nhưng bản thân DataFrame không phải là một mô hình thống kê hay thuật toán học máy.

Để đưa dữ liệu vào các thư viện chuyên sâu như `statsmodels` hay `scikit-learn`, người xử lý dữ liệu cần giải quyết ba yêu cầu kỹ thuật:
1. **Biến đổi hình thức**: Chuyển các cột nhãn, chuỗi văn bản và biến phân loại thành ma trận số học thuần nhất (Design Matrix).
2. **Đặc tả quan hệ toán học**: Mô tả cấu trúc hồi quy, các tương tác phi tuyến và phép biến đổi biến số một cách tường minh và cô đọng.
3. **Bảo toàn tính toàn vẹn của bằng chứng**: Ngăn chặn hiện tượng rò rỉ thông tin từ tập kiểm thử vào tập huấn luyện trong quá trình tiền xử lý.

Bài giảng này trình bày cầu nối kỹ thuật giữa cấu trúc bảng của pandas với các thư viện mô hình hóa trong hệ sinh thái Python: Cú pháp công thức của Patsy, suy diễn thống kê với statsmodels, và kiến trúc đường ống của scikit-learn.

---

## 1. Giao diện kết nối giữa pandas và mã nguồn mô hình

Hầu hết các thư viện thống kê và học máy ở tầng lõi đều yêu cầu đầu vào là mảng số thực hai chiều của NumPy hoặc ma trận thưa của SciPy, với cấu trúc:
$$
X \in \mathbb{R}^{n \times p}, \quad y \in \mathbb{R}^{n}
$$
Trong đó $n$ là số lượng quan sát, $p$ là số lượng đặc trưng đầu vào, và mỗi phần tử trong ma trận đều phải là một con số có kiểu dữ liệu thuần nhất (thường là `float64` hoặc `float32`).

### Chuyển đổi DataFrame sang mảng NumPy

Phương thức chuẩn mực để trích xuất mảng số học từ DataFrame là gọi `.to_numpy()`:

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "dien_tich": [40, 55, 60, 75, 80, 95, 100, 120],
    "so_phong": [1, 2, 2, 3, 3, 4, 4, 5],
    "quan": ["CauGiay", "CauGiay", "DongDa", "DongDa", "TayHo", "TayHo", "CauGiay", "TayHo"],
    "gia": [1.8, 2.5, 2.7, 3.4, 3.9, 4.6, 4.8, 5.9]
})

# Trích xuất ma trận đặc trưng định lượng
X_so = df[["dien_tich", "so_phong"]].to_numpy()
y_so = df["gia"].to_numpy()

print("Kiểu dữ liệu ma trận X:", X_so.dtype)
print("Kích thước ma trận X:", X_so.shape) # (8, 2)
```

Cột số chứa giá trị khuyết thiếu (`NaN` chuẩn IEEE 754) khi chuyển sang mảng NumPy qua `.to_numpy()` vẫn giữ kiểu số thực `float64`, chứ không bị ép thành kiểu `object`. Mảng chỉ bị chuyển thành `object` khi cột dữ liệu chứa chuỗi văn bản hỗn hợp, kiểu dữ liệu không đồng nhất hoặc đối tượng tùy ý của Python. Tuy nhiên, các thuật toán ước lượng ma trận thường không chấp nhận giá trị `NaN`, nên việc xử lý khuyết thiếu trước khi đưa vào mô hình vẫn là bước kỹ thuật bắt buộc.

<!-- worked-example bai-12-mo-hinh-hoa-worked-1 -->

::: example Trích xuất mảng số học bằng to_numpy với lọc kiểu số

Khi chuẩn bị ma trận đặc trưng cho các thư viện tính toán số học, nếu DataFrame chứa các cột văn bản hoặc đối tượng hỗn hợp, phương thức to_numpy sẽ ép kiểu mảng kết quả về object. Ta sử dụng select_dtypes để lọc các cột có kiểu số học và chỉ định tường minh tham số dtype=np.float64 khi chuyển đổi.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "dien_tich": [45.0, 60.0, 80.0],
    "so_phong": [1, 2, 3],
    "quan": ["DongDa", "TayHo", "CauGiay"],
})

# Lọc các cột số học và trích xuất mảng float64 thuần nhất
X_so = df.select_dtypes(include=[np.number]).to_numpy(dtype=np.float64)

bang_kq = pd.DataFrame({
    "dien_tich": X_so[:, 0],
    "so_phong": X_so[:, 1],
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| dien&#95;tich | so&#95;phong |
| --- | --- |
| 45.0 | 1.0 |
| 60.0 | 2.0 |
| 80.0 | 3.0 |

</div>

Bảng `df` có hai cột số và một cột chuỗi. Nếu gọi `df.to_numpy()` cho cả bảng, mảng cần một kiểu chung có thể chứa cả chuỗi và số, nên trong ví dụ này nó có kiểu `object`. Trước khi đưa vào phép tính số, ta chọn các cột cần dùng rồi chỉ định kiểu đầu ra.

`select_dtypes(include=[np.number])` chọn các cột theo kiểu số. `to_numpy(dtype=np.float64)` sau đó cho mảng `(3, 2)`, trong đó số phòng cũng được chuyển sang số thực. Nó không tự chọn đúng đặc trưng theo ý nghĩa. Một cột mã khách hàng lưu bằng số cũng có thể lọt qua bộ lọc này.

Mảng kết quả chỉ còn giá trị, không còn nhãn hàng và tên cột. Cần giữ thứ tự cột nhất quán khi đưa dữ liệu mới vào mô hình. `dtype` không bảo đảm mảng liên tục theo hàng, cũng không xử lý mọi ô thiếu. Yêu cầu cụ thể về kiểu số, mảng thưa và giá trị thiếu phụ thuộc bộ ước lượng.

:::

<!-- /worked-example -->

### Mã hóa biến phân loại với `pd.get_dummies` và phụ thuộc tuyến tính {#ma-hoa-bien-phan-loai-voi-pd-get-dummies-va-bay-bien-gia}

Biến phân loại (Categorical variable) như quận, khu vực, nhóm sản phẩm không thể đưa trực tiếp vào phép nhân ma trận. Phương pháp chuẩn mực là tạo ra các **biến giả (Dummy variables / One-hot encoding)**: Mỗi mức của biến phân loại trở thành một cột nhị phân mang giá trị 0 hoặc 1.

Tuy nhiên, nếu một biến có $k$ mức phân loại và ta tạo đủ cả $k$ cột biến giả trong mô hình có chứa số hạng tự do (intercept $\beta_0$), tổng của $k$ cột này sẽ luôn bằng 1 trên mọi dòng quan sát:
$$
\sum_{i=1}^k D_i = D_1 + D_2 + \dots + D_k = 1
$$
Hệ quả là cột hằng số tự do và $k$ cột biến giả trở nên phụ thuộc tuyến tính hoàn toàn với nhau. Hiện tượng này được gọi là **Bẫy biến giả (Dummy Variable Trap)** hoặc hiện tượng cộng tuyến hoàn hảo (Perfect Multicollinearity). Khi đó, ma trận $X^T X$ không khả nghịch, khiến phép tính nghiệm OLS bị suy biến do ma trận khuyết hạng.

Giải pháp toán học: Trong các mô hình tuyến tính có số hạng tự do, ta loại bỏ một mức làm **mức tham chiếu (Reference level / Baseline)** bằng tham số `drop_first=True`:

```python
# Tạo biến giả và loại bỏ mức tham chiếu đầu tiên
df_dummies = pd.get_dummies(df, columns=["quan"], drop_first=True, dtype=float)
print("Các cột sau khi tạo biến giả an toàn:")
print(df_dummies.columns.tolist())
# Kết quả gồm 'quan_DongDa', 'quan_TayHo', trong khi 'CauGiay' đóng vai trò mức tham chiếu
```

Cần lưu ý rằng `drop_first=True` không phải là yêu cầu bắt buộc cho mọi mô hình học máy. Ví dụ, trong các mô hình cây quyết định (Decision Trees, Random Forest, Gradient Boosting) hoặc các mô hình hồi quy có thành phần chính quy hóa (như Ridge hoặc Lasso với điều kiện phù hợp), việc giữ lại toàn bộ các cột biến giả không làm thuật toán bị lỗi suy biến đại số và có thể giúp việc phân nhánh hoặc diễn giải diễn ra cân xứng.

---

<!-- worked-example bai-12-mo-hinh-hoa-worked-2 -->

::: example Mã hóa biến phân loại với pd.get_dummies và xử lý giá trị khuyết thiếu

Khi mã hóa biến phân loại bằng pd.get_dummies, hành vi mặc định là bỏ qua các giá trị khuyết thiếu NaN, khiến dòng khuyết nhận giá trị 0 ở tất cả các cột biến giả. Tham số dummy_na=True tạo riêng một cột cho trạng thái khuyết thiếu, kết hợp drop_first=True để loại bỏ mức cơ sở và tránh hiện tượng đa cộng tuyến hoàn hảo.

```python
import pandas as pd

s_quan = pd.Series(["CauGiay", "DongDa", None, "TayHo"], name="quan")

# Mã hóa biến giả, giữ lại cột cho giá trị khuyết thiếu và loại mức nền đầu
df_dummies = pd.get_dummies(
    s_quan,
    prefix="quan",
    dummy_na=True,
    drop_first=True,
    dtype=int,
)

bang_kq = df_dummies.reset_index(drop=True)
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| quan&#95;DongDa | quan&#95;TayHo | quan&#95;nan |
| --- | --- | --- |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 0 | 0 | 1 |
| 0 | 1 | 0 |

</div>

Biến phân loại đại diện cho các nhóm định tính như địa danh hành chính, ngành nghề hay loại hình dịch vụ. Trong các bài toán học máy, ta không thể gán các con số nguyên tùy ý cho các nhóm này vì phép gán sẽ vô tình áp đặt một trật tự thứ bậc nhân tạo lên các nhóm vốn bình đẳng. Phương pháp biến giả (One-hot encoding) giải quyết vấn đề này bằng cách tách mỗi mức phân loại thành một cột nhị phân độc lập.

Trong dữ liệu thực tế, các trường phân loại thường xuyên xuất hiện giá trị khuyết thiếu. Nếu gọi `pd.get_dummies` mà không chỉ định `dummy_na=True`, pandas sẽ bỏ qua các giá trị `NaN`, khiến dòng khuyết mang giá trị 0 ở tất cả các cột biến giả. Khi kết hợp với `drop_first=True`, dòng khuyết thiếu sẽ bị trùng mã hóa với mức tham chiếu cơ sở, gây sai lệch thông tin trong quá trình ước lượng hệ số.

Thiết lập `dummy_na=True` giúp tạo thêm cột `quan_nan` để ghi nhận riêng trạng thái mất thông tin. Khi kết hợp với `drop_first=True`, mức đầu tiên theo thứ tự chữ cái là `CauGiay` được chọn làm mức tham chiếu và loại bỏ khỏi bảng, trong khi các mức `DongDa`, `TayHo` và `nan` đều có cột chỉ báo nhị phân riêng. Tham số `dtype=int` giúp các cột này nhận giá trị số nguyên 0 và 1, sẵn sàng cho các phép tính toán tiếp theo.

:::

<!-- /worked-example -->

## 2. Xây dựng đặc tả mô hình với Patsy

Trong phân tích thống kê và kinh tế lượng, việc ghép nối thủ công từng cột biến giả và biến đổi logarit bằng mã lệnh pandas thường gây rườm rà và dễ nhầm lẫn. Thư viện **Patsy** cung cấp cú pháp ngôn ngữ công thức (Formula Language) mô phỏng chuẩn ngôn ngữ R/S-language, giúp người phân tích đặc tả cấu trúc mô hình hồi quy một cách tường minh.

### Cú pháp công thức cơ bản và Số hạng tự do (Intercept)

Cú pháp chuẩn của một công thức Patsy có dạng:
$$
y \sim x_0 + x_1 + \dots + x_p
$$
Vế trái là biến phụ thuộc mục tiêu, còn vế phải là tập hợp các biến giải thích.

Mặc định, Patsy luôn tự động bổ sung một cột toàn số 1 mang tên `Intercept` vào ma trận đặc trưng. Nếu muốn loại bỏ số hạng tự do này trong các bài toán hồi quy đi qua gốc tọa độ, ta thêm `+ 0` hoặc `- 1` vào vế phải của công thức:

```python
import patsy

# 1. Mô hình có số hạng tự do mặc định
y1, X1 = patsy.dmatrices("gia ~ dien_tich + so_phong", data=df)
print("Tên các cột trong mô hình có Intercept:")
print(X1.design_info.column_names) # ['Intercept', 'dien_tich', 'so_phong']

# 2. Loại bỏ số hạng tự do
y2, X2 = patsy.dmatrices("gia ~ dien_tich + so_phong + 0", data=df)
print("Tên các cột trong mô hình không có Intercept:")
print(X2.design_info.column_names) # ['dien_tich', 'so_phong']
```

<!-- worked-example bai-12-mo-hinh-hoa-worked-3 -->

::: example Ánh xạ đặc tả mô hình sang tập dữ liệu mới bằng build_design_matrices

Khi triển khai mô hình hồi quy, ma trận thiết kế của tập dữ liệu mới cần giữ đúng cấu trúc cột và mức tham chiếu đã học từ tập huấn luyện. Hàm build_design_matrices của Patsy nhận design_info từ tập huấn luyện để chuyển đổi tập kiểm thử mới, bảo đảm tính nhất quán về kích thước và thứ tự cột.

```python
import numpy as np
import pandas as pd
import patsy

df_train = pd.DataFrame({
    "dien_tich": [50.0, 80.0, 100.0],
    "quan": ["CauGiay", "DongDa", "TayHo"],
    "gia": [2.5, 3.8, 5.0],
})

df_new = pd.DataFrame({
    "dien_tich": [65.0, 90.0],
    "quan": ["DongDa", "CauGiay"],
})

# Huấn luyện công thức trên tập train để thu được design_info
y_tr, X_tr = patsy.dmatrices("gia ~ dien_tich + C(quan)", data=df_train)

# Tái áp dụng đặc tả design_info lên tập dữ liệu mới
X_new = patsy.build_design_matrices([X_tr.design_info], df_new)[0]

bang_kq = pd.DataFrame(X_new, columns=X_tr.design_info.column_names)
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| Intercept | C(quan)&#91;T.DongDa&#93; | C(quan)&#91;T.TayHo&#93; | dien&#95;tich |
| --- | --- | --- | --- |
| 1.0 | 1.0 | 0.0 | 65.0 |
| 1.0 | 0.0 | 0.0 | 90.0 |

</div>

Thư viện Patsy cung cấp ngôn ngữ công thức để định nghĩa mô hình hồi quy dạng `y ~ x + C(cat)`. Khi gọi `patsy.dmatrices`, hàm không chỉ xuất ra ma trận số học mà còn đính kèm thuộc tính `design_info` chứa toàn bộ cấu trúc định danh cột, mức tham chiếu phân loại và các thông tin chuyển đổi đi kèm. Thuộc tính này đóng vai trò là chuẩn giao tiếp cấu trúc giữa tập dữ liệu huấn luyện và các tập dữ liệu dự báo tương lai.

Nếu người phân tích gọi lại `patsy.dmatrices` một cách độc lập trên tập kiểm thử mới `df_new`, rủi ro phát sinh khi tập mới không xuất hiện đầy đủ các mức phân loại như tập huấn luyện. Chẳng hạn khi tập mới chỉ có `DongDa` và `CauGiay` mà thiếu `TayHo`, việc gọi công thức mới sẽ tạo ra ít cột hơn, khiến ma trận mới không khớp với số lượng hệ số mà mô hình đã học.

Hàm `patsy.build_design_matrices` khắc phục sự cố này bằng cách nhận đối tượng `design_info` của tập huấn luyện và áp đặt cấu trúc cột đó lên dữ liệu mới. Bảng kết quả cho thấy ma trận mới luôn duy trì đúng 4 cột gồm `Intercept`, `C(quan)[T.DongDa]`, `C(quan)[T.TayHo]` và `dien_tich`. Dòng mang giá trị `CauGiay` nhận số 0 ở cả hai cột quận giả do là mức tham chiếu, bảo đảm mô hình tính toán giá trị dự đoán nhất quán. Nếu dữ liệu mới có một mức phân loại chưa từng thấy trong dữ liệu huấn luyện, hàm có thể báo lỗi. Giữ cấu trúc cột không đồng nghĩa tự biết cách mã hóa mọi mức mới.

:::

<!-- /worked-example -->

### Các phép biến đổi dữ liệu trong công thức

Patsy cho phép áp dụng trực tiếp các hàm số toán học lên các cột dữ liệu ngay trong công thức:

- **Hàm số chuẩn**: Ta có thể viết `np.log(dien_tich)` hoặc `np.sqrt(dien_tich)`.
- **Số hạng tương tác (`:`) và mở rộng (`*`)**: Ký hiệu `x1:x2` đại diện cho **số hạng tương tác thuần túy** giữa $x_1$ và $x_2$ (tương ứng với tích $x_1 x_2$). Ký hiệu `x1 * x2` là cú pháp viết tắt mở rộng cả hiệu ứng chính và tương tác: `x1 * x2` tương đương với `x1 + x2 + x1:x2`.
- **Bảo vệ toán tử số học bằng `I()`**: Trong công thức Patsy, dấu cộng (`+`) là ký hiệu phân tách các biến, còn dấu hai chấm (`:`) là tương tác biến. Nếu muốn cộng hoặc nhân hai biến theo nghĩa số học thực sự, ta bắt buộc phải bọc biểu thức vào hàm định danh `I(x0 + x1)` hoặc `I(x0 * x1)`.
- **Chuẩn hóa biến số**: Các hàm biến đổi như `standardize(x)` (đưa về trung bình 0, phương sai 1) hoặc `center(x)` (đưa về trung bình 0) có thể được nhúng trực tiếp vào công thức.

```python
y_trans, X_trans = patsy.dmatrices(
    "gia ~ np.log(dien_tich) + I(so_phong + 1)",
    data=df
)
print("Các đặc trưng sau biến đổi:")
print(X_trans.design_info.column_names)
```

<!-- worked-example bai-12-mo-hinh-hoa-worked-4 -->

::: example Chuẩn hóa và tạo số hạng tương tác trong công thức Patsy

Khi các biến giải thích có thang đo chênh lệch lớn, việc chuẩn hóa giúp đưa các đặc trưng về cùng một tỷ lệ biến thiên. Hàm standardize trong Patsy tính toán giá trị Z-score trực tiếp trong công thức, kết hợp toán tử hai chấm để tạo số hạng tương tác giữa hai biến giải thích.

```python
import numpy as np
import pandas as pd
import patsy

df = pd.DataFrame({
    "dien_tich": [40.0, 60.0, 80.0, 100.0],
    "so_phong": [1.0, 2.0, 3.0, 4.0],
})

# Công thức kết hợp chuẩn hóa biến liên tục và số hạng tương tác thuần túy
cong_thuc = "standardize(dien_tich) + so_phong + standardize(dien_tich):so_phong"
X = patsy.dmatrix(cong_thuc, data=df)

bang_kq = pd.DataFrame({
    "dt_std": np.round(X[:, 1], 2),
    "so_phong": X[:, 2],
    "tuong_tac": np.round(X[:, 3], 2),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| dt&#95;std | so&#95;phong | tuong&#95;tac |
| --- | --- | --- |
| -1.34 | 1.0 | -1.34 |
| -0.45 | 2.0 | -0.89 |
| 0.45 | 3.0 | 1.34 |
| 1.34 | 4.0 | 5.37 |

</div>

Khi các biến số trong mô hình có miền giá trị chênh lệch đáng kể, ví dụ diện tích dao động từ 40 đến 100 trong khi số phòng ngủ chỉ từ 1 đến 4, độ lớn của các hệ số hồi quy sẽ phụ thuộc trực tiếp vào đơn vị đo lường ban đầu. Hàm `standardize()` trong Patsy hỗ trợ chuẩn hóa biến số về dạng Z-score bằng cách trừ đi giá trị trung bình và chia cho độ lệch chuẩn.

Điểm kỹ thuật quan trọng là hàm `standardize()` của Patsy sử dụng công thức độ lệch chuẩn tổng thể với bậc tự do điều chỉnh `ddof=0`. Cụ thể với 4 quan sát diện tích gồm 40, 60, 80 và 100, giá trị trung bình là 70 và độ lệch chuẩn tính theo `ddof=0` là 22.36068, chứ không phải độ lệch chuẩn mẫu 25.82 theo `ddof=1`. Các giá trị chuẩn hóa thu được lần lượt là -1.34, -0.45, 0.45 và 1.34, đối xứng qua mốc 0.

Toán tử dấu hai chấm `:` trong Patsy định nghĩa số hạng tương tác thuần túy giữa hai đặc trưng, tương đương với tích số học giữa giá trị chuẩn hóa của diện tích và số phòng ngủ. Khác với toán tử nhân `*` vốn sinh ra cả hiệu ứng chính lẫn số hạng tương tác, dấu hai chấm cho phép người nghiên cứu kiểm soát chính xác các biến đưa vào mô hình mà không làm phát sinh các cột dư thừa ngoài ý muốn.

:::

<!-- /worked-example -->

### Xử lý biến phân loại tự động với `C()`

Khi một cột trong DataFrame chứa dữ liệu dạng chuỗi văn bản hoặc kiểu `category`, Patsy sẽ tự động nhận diện và mã hóa thành các biến giả với cơ chế loại bỏ mức tham chiếu mặc định. Ta cũng có thể chỉ định rõ ràng bằng hàm bọc `C(bien)`:

```python
y_cat, X_cat = patsy.dmatrices(
    "gia ~ dien_tich + C(quan)",
    data=df
)
print("Ma trận thiết kế với biến phân loại quận:")
print(X_cat.design_info.column_names)
# Kết quả: ['Intercept', 'C(quan)[T.DongDa]', 'C(quan)[T.TayHo]', 'dien_tich']
```

Mức đầu tiên theo thứ tự bảng chữ cái (`CauGiay`) được chọn làm mức nền tham chiếu. Hệ số của `C(quan)[T.DongDa]` khi ước lượng sẽ phản ánh mức chênh lệch giá thuê trung bình của quận Đống Đa so với quận Cầu Giấy khi giữ nguyên diện tích.

---

<!-- worked-example bai-12-mo-hinh-hoa-worked-5 -->

::: example Chỉ định mức tham chiếu cho biến phân loại với Treatment

Mặc định Patsy chọn mức tham chiếu của biến phân loại theo thứ tự bảng chữ cái. Hàm Treatment cho phép người phân tích chỉ định mức tham chiếu cơ sở phù hợp với mục tiêu nghiên cứu, giúp các hệ số hồi quy phản ánh trực tiếp mức chênh lệch giá so với nhóm nền.

```python
import numpy as np
import pandas as pd
import patsy
from patsy import Treatment

df = pd.DataFrame({
    "quan": ["CauGiay", "DongDa", "TayHo", "TayHo"],
    "gia": [2.5, 3.2, 4.5, 4.8],
})

# Chỉ định tường minh Tây Hồ làm mức tham chiếu cơ sở
cong_thuc = "gia ~ C(quan, Treatment(reference='TayHo'))"
y, X = patsy.dmatrices(cong_thuc, data=df)

bang_kq = pd.DataFrame(X, columns=["Intercept", "CauGiay", "DongDa"])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| Intercept | CauGiay | DongDa |
| --- | --- | --- |
| 1.0 | 1.0 | 0.0 |
| 1.0 | 0.0 | 1.0 |
| 1.0 | 0.0 | 0.0 |
| 1.0 | 0.0 | 0.0 |

</div>

Mô hình đang dùng mã hóa Treatment cùng một cột hằng `Intercept`. Nếu giữ đủ ba cột chỉ báo, tổng của chúng sẽ bằng cột hằng, tạo phụ thuộc tuyến tính. Patsy biểu diễn ba nhóm bằng hai cột chỉ báo và chọn nhóm còn lại làm mốc tham chiếu.

Trong nhiều tình huống nghiên cứu, người phân tích muốn so sánh mức giá của các khu vực khác với một khu vực chuẩn cụ thể, chẳng hạn chọn `TayHo` làm mốc đối chiếu. Cú pháp `Treatment(reference='TayHo')` cho phép ấn định trực tiếp nhóm tham chiếu. Cần hiểu rõ rằng trong mô hình hồi quy tuyến tính với biến phụ thuộc là giá thô, hệ số hồi quy của các nhóm thể hiện mức chênh lệch giá thô tuyệt đối tính theo đơn vị giá, chứ không biểu thị tỷ lệ phần trăm chiết khấu và không đại diện cho nhận định toàn diện về thị trường bất động sản thực tế.

Hai hàng `TayHo` nhận 0 ở cả hai cột chỉ báo. `CauGiay` nhận `(1, 0)`, còn `DongDa` nhận `(0, 1)`. Mã rút gọn tên cột khi in bảng cho dễ đọc. Đây mới là ma trận thiết kế, chưa phải kết quả ước lượng hệ số. Thay mốc làm đổi cách diễn giải các hệ số, không tự làm đổi dữ liệu gốc.

:::

<!-- /worked-example -->

## 3. Giới thiệu thư viện statsmodels

Nếu như scikit-learn tập trung vào độ chính xác dự báo (Predictive Accuracy), thì **statsmodels** lại là thư viện chuyên sâu cho **suy diễn thống kê (Statistical Inference)**: Đánh giá độ tin cậy của các hệ số hồi quy, kiểm định giả thuyết và phân tích các quá trình chuỗi thời gian.

### Ước lượng mô hình tuyến tính (OLS)

Mô hình hồi quy tuyến tính cổ điển có dạng:
$$
y = X \beta + \epsilon
$$
OLS chọn tham số để tổng bình phương phần dư nhỏ nhất. Khi các cột của X độc lập tuyến tính, nghiệm là duy nhất và có thể biểu diễn bằng công thức dưới đây. Trong mã thực tế, thư viện dùng các phương pháp số phù hợp, không cần tự tính nghịch đảo.

$$
\hat{\beta} = (X^T X)^{-1} X^T y.
$$

Theo định lý Gauss–Markov, ước lượng OLS là ước lượng tuyến tính không chệch tốt nhất (BLUE - Best Linear Unbiased Estimator) khi thỏa mãn 4 điều kiện:
1. Tuyến tính về tham số: $y = X\beta + \epsilon$.
2. Kỳ vọng có điều kiện của sai số bằng 0 (Strict Exogeneity): $\mathbb{E}[\epsilon \mid X] = 0$.
3. Phương sai sai số thuần nhất và không có tự tương quan (Spherical errors): $\operatorname{Var}(\epsilon \mid X) = \sigma^2 I$.
4. Ma trận X có hạng cột đầy đủ. Nếu X có k cột thì hạng bằng k, nghĩa là không có cột phụ thuộc tuyến tính hoàn toàn vào các cột còn lại.

Sai số có phân phối chuẩn không phải giả thiết của định lý Gauss–Markov. Nếu bổ sung phân phối chuẩn có điều kiện theo X cùng các điều kiện trên và còn bậc tự do phần dư, ta có các kiểm định t, F chính xác trong mô hình chuẩn. Các kết quả tiệm cận cần thêm điều kiện xác suất, không tự có chỉ vì mẫu lớn. Việc tính nghiệm hoặc đánh giá dự đoán cũng không bắt buộc phần dư phải chuẩn.

statsmodels cung cấp hai hướng tiếp cận để huấn luyện mô hình:
1. **API mảng số (`statsmodels.api`)**: Truyền ma trận $X$ và vector $y$ thuần túy (phải tự bổ sung cột hằng số bằng `sm.add_constant(X)`).
2. **API công thức (`statsmodels.formula.api` - viết tắt là `smf`)**: Truyền DataFrame và chuỗi công thức Patsy trực quan.

```python
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Huấn luyện mô hình hồi quy tuyến tính bằng công thức
mo_hinh = smf.ols("gia ~ dien_tich + C(quan)", data=df).fit()

# Xem bảng tóm tắt kết quả
print(mo_hinh.summary())
```

<!-- worked-example bai-12-mo-hinh-hoa-worked-6 -->

::: example Trích xuất hệ số, sai số chuẩn và khoảng tin cậy từ hồi quy OLS

Sau khi huấn luyện mô hình OLS bằng statsmodels, người phân tích cần trích xuất các đại lượng thống kê suy diễn có cấu trúc. Các thuộc tính params, bse, pvalues và phương thức conf_int cung cấp phương tiện lấy hệ số, sai số chuẩn, giá trị kiểm định và khoảng tin cậy dưới dạng bảng dữ liệu.

```python
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.DataFrame({
    "dien_tich": [40.0, 55.0, 70.0, 85.0, 100.0],
    "gia": [1.9, 2.6, 3.4, 4.1, 4.9],
})

# Huấn luyện mô hình hồi quy OLS
ket_qua = smf.ols("gia ~ dien_tich", data=df).fit()

# Trích xuất các đại lượng thống kê suy diễn cốt lõi
ci = ket_qua.conf_int(alpha=0.05)
bang_kq = pd.DataFrame({
    "bien": ket_qua.params.index,
    "he_so": ket_qua.params.round(4).values,
    "sai_so": ket_qua.bse.round(4).values,
    "p_value": ket_qua.pvalues.round(4).values,
    "khoang_95": [
        f"[{a:.4f}, {b:.4f}]" for a, b in zip(ci[0], ci[1])
    ],
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| bien | he&#95;so | sai&#95;so | p&#95;value | khoang&#95;95 |
| --- | --- | --- | --- | --- |
| Intercept | -0.12 | 0.0488 | 0.0908 | &#91;-0.2752, 0.0352&#93; |
| dien&#95;tich | 0.05 | 0.0007 | 0.0 | &#91;0.0479, 0.0521&#93; |

</div>

Mô hình hồi quy bình phương tối thiểu thông thường (OLS) trong statsmodels cung cấp các công cụ suy diễn thống kê dựa trên phân phối xác suất. Khi gọi phương thức `fit()`, đối tượng trả về chứa các tham số ước lượng cùng các đại lượng đo lường độ bất định đi kèm. Thuộc tính `params` lưu trữ các hệ số hồi quy điểm được tối ưu hóa từ mẫu dữ liệu.

`params` lưu các hệ số ước lượng, còn `bse` lưu sai số chuẩn của từng hệ số. Với dữ liệu này, hệ số diện tích là 0.05 và sai số chuẩn làm tròn là 0.0007. `pvalues` là kết quả kiểm định hệ số bằng 0 theo mô hình. Một giá trị được in là 0.0 sau khi làm tròn không phải xác suất đúng bằng 0.

`conf_int(alpha=0.05)` cho khoảng tin cậy 95%, với hệ số diện tích xấp xỉ `[0.0479, 0.0521]`. Với mẫu nhỏ này, cách suy diễn t cổ điển cần các giả định phù hợp về sai số, gồm tính độc lập, phương sai không đổi và phân phối chuẩn có điều kiện. Năm quan sát minh họa chưa đủ để xác lập quan hệ nhân quả về thị trường nhà ở.

:::

<!-- /worked-example -->

### Đọc và thẩm định bảng tóm tắt kết quả (Model Summary)

Bảng báo cáo của statsmodels chứa các chỉ số học thuật cốt lõi cần được diễn giải chuẩn xác:

1. **Hệ số hồi quy (`coef`)**: Ước lượng điểm của $\beta_j$. Ví dụ nếu hệ số của `dien_tich` là `0.045`, điều này có nghĩa là khi diện tích tăng thêm $1\,\mathrm{m}^2$, giá nhà dự kiến tăng trung bình $0{,}045$ tỷ đồng trong điều kiện các yếu tố khác giữ nguyên.
2. **Sai số chuẩn (`std err`)**: Đo lường độ bất định của ước lượng hệ số do biến thiên mẫu ngẫu nhiên.
3. **Thống kê t (`t`) và Giá trị p (`P>|t|`)**: Kiểm định giả thuyết không $H_0: \beta_j = 0$. Nếu giá trị $p < 0{,}05$, ta bác bỏ giả thuyết không và kết luận biến giải thích có ý nghĩa thống kê ở mức ý nghĩa 5%.
4. **Hệ số xác định ($R^2$ và $R^2$ hiệu chỉnh)**:
   Với n quan sát, trước hết tính trung bình của biến mục tiêu:

   $$
   \bar y = \frac{y_1 + y_2 + \cdots + y_n}{n}.
   $$

   Gọi phần dư là $r_i = y_i-\hat y_i$ và độ lệch quanh trung bình là $d_i = y_i-\bar y$. Hai tổng bình phương được khai triển như sau:

   $$
   S_e = r_1^2+r_2^2+\cdots+r_n^2.
   $$

   $$
   S_t = d_1^2+d_2^2+\cdots+d_n^2.
   $$

   Viết gọn bằng ký hiệu tổng, $S_e=\sum_{i=1}^n r_i^2$ và $S_t=\sum_{i=1}^n d_i^2$. Khi $S_t>0$, hệ số xác định là:

   $$
   R^2 = 1-\frac{S_e}{S_t}.
   $$

   Chỉ số này so sánh sai số dự đoán với cách dùng cùng một trung bình cho mọi quan sát. Trên tập ngoài mẫu, nó có thể âm. R² hiệu chỉnh còn tính đến số tham số, nhưng không thay việc đánh giá trên dữ liệu chưa dùng để chọn mô hình.
5. **Giá trị dự đoán (`fittedvalues`) và Phần dư (`resid`)**:
   Phần dư $e_i = y_i - \hat{y}_i$ phản ánh phần sai lệch mà mô hình chưa giải thích được.

<!-- worked-example bai-12-mo-hinh-hoa-worked-7 -->

::: example Ước lượng sai số chuẩn vững trước phương sai thay đổi với HC3

Khi phần dư vi phạm giả định phương sai đồng nhất, sai số chuẩn OLS thông thường sẽ bị chệch. Phương thức get_robustcov_results với tùy chọn HC3 giúp tính toán lại sai số chuẩn vững trước hiện tượng phương sai thay đổi, cải thiện độ tin cậy của các kiểm định thống kê trên mẫu nhỏ.

```python
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

df = pd.DataFrame({
    "x": [10.0, 20.0, 30.0, 40.0, 50.0, 60.0],
    "y": [12.0, 18.0, 35.0, 32.0, 65.0, 58.0],
})

# Huấn luyện mô hình OLS tiêu chuẩn
ols_fit = smf.ols("y ~ x", data=df).fit()

# Tái ước lượng ma trận hiệp phương sai với chuẩn vững HC3
ols_hc3 = ols_fit.get_robustcov_results(cov_type="HC3")

bang_kq = pd.DataFrame({
    "bien": ols_fit.params.index,
    "he_so": ols_fit.params.round(3).values,
    "se_goc": ols_fit.bse.round(3).values,
    "se_hc3": np.round(ols_hc3.bse, 3),
    "p_goc": ols_fit.pvalues.round(3).values,
    "p_hc3": np.round(ols_hc3.pvalues, 3),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| bien | he&#95;so | se&#95;goc | se&#95;hc3 | p&#95;goc | p&#95;hc3 |
| --- | --- | --- | --- | --- | --- |
| Intercept | -0.133 | 8.125 | 5.338 | 0.988 | 0.981 |
| x | 1.051 | 0.209 | 0.224 | 0.007 | 0.009 |

</div>

Trong mô hình tuyến tính với kỳ vọng sai số có điều kiện bằng 0 và ma trận thiết kế đủ hạng, OLS có thể vẫn không chệch khi phương sai sai số thay đổi. Tuy nhiên, công thức sai số chuẩn cổ điển không còn phù hợp. Điều này ảnh hưởng cách tính khoảng tin cậy và kiểm định, không tự làm đổi các hệ số đã ước lượng.

Phương pháp ma trận hiệp phương sai vững trước hiện tượng phương sai thay đổi (Heteroskedasticity-Consistent Standard Errors) cung cấp công thức hiệu chỉnh sai số chuẩn. Khi áp dụng `get_robustcov_results(cov_type='HC3')`, hệ số ước lượng của `x` vẫn giữ nguyên là 1.051, trong khi sai số chuẩn của `x` tăng từ 0.209 lên 0.224, khiến giá trị p-value tăng tương ứng từ 0.007 lên 0.009. Đồng thời, sai số chuẩn của `Intercept` lại giảm từ 8.125 xuống 5.338.

Chuẩn HC3 đưa vào trọng số điều chỉnh đòn bẩy nhằm cải thiện chất lượng suy diễn trên các mẫu dữ liệu có quy mô vừa và nhỏ. Tuy nhiên, HC3 không phải là giải pháp tối ưu trong mọi bối cảnh và không thể khắc phục các vi phạm nghiêm trọng khác như biến nội sinh hay tự tương quan chuỗi. Do đó, việc sử dụng sai số chuẩn vững cần đi kèm với các bước kiểm tra chẩn đoán mô hình cẩn trọng.

:::

<!-- /worked-example -->

### Ước lượng quá trình chuỗi thời gian trong statsmodels

Bên cạnh các mô hình cắt ngang, statsmodels sở hữu hệ thống công cụ cho dữ liệu chuỗi thời gian trong module `statsmodels.tsa`.

Xét mô hình tự hồi quy bậc 1, ký hiệu là $\text{AR}(1)$:
$$
Y_t = c + \phi_1 Y_{t-1} + \epsilon_t
$$
Mô hình này dự báo giá trị hiện tại dựa trên giá trị của chính nó ở kỳ liền trước:

```python
from statsmodels.tsa.ar_model import AutoReg

# Sinh chuỗi số liệu mô phỏng quá trình AR(1) thực thụ: Y_t = c + phi * Y_{t-1} + eps_t
np.random.seed(42)
n = 100
c = 2.0
phi = 0.7
eps = np.random.normal(0, 1, n)
du_lieu_ts = np.zeros(n)
du_lieu_ts[0] = c / (1 - phi) + eps[0]
for t in range(1, n):
    du_lieu_ts[t] = c + phi * du_lieu_ts[t-1] + eps[t]

# Huấn luyện mô hình tự hồi quy với độ trễ 1 kỳ
mo_hinh_ar = AutoReg(du_lieu_ts, lags=1).fit()

print("Hệ số tự hồi quy phi_1 ước lượng:", round(float(mo_hinh_ar.params[1]), 4))

# Dự báo 5 bước tiếp theo vào tương lai
du_bao = mo_hinh_ar.predict(start=n, end=n+4)
print("Dự báo 5 mốc tiếp theo:", np.round(du_bao, 2))
```

---

## 4. Giới thiệu thư viện scikit-learn và ngăn rò rỉ dữ liệu {#_4-gioi-thieu-thu-vien-scikit-learn-va-cam-bay-ro-ri-du-lieu}

Trong khi statsmodels hướng tới suy diễn thống kê, **scikit-learn** tập trung vào khả năng khái quát hóa trên dữ liệu mới chưa từng thấy (Generalization) và chuẩn hóa quy trình học có giám sát và không giám sát.

### Giao diện Estimator chuẩn mực

Trong scikit-learn, các họ thuật toán tuân thủ phân định giao diện rõ ràng:
- `fit(X, y)`: Học các tham số từ tập dữ liệu huấn luyện.
- `predict(X)`: Áp dụng các tham số đã học để suy diễn nhãn hoặc giá trị cho dữ liệu mới (dành cho các mô hình dự đoán như `LinearRegression`, `Ridge`).
- `transform(X)`: Biến đổi dữ liệu đặc trưng (dành cho các bộ tiền xử lý như `StandardScaler`).

Cần lưu ý: Không phải mọi đối tượng trong scikit-learn đều có cả hai phương thức `predict` và `transform`. Các transformer chỉ có `transform`, trong khi các estimator dự đoán chỉ có `predict`.

<!-- worked-example bai-12-mo-hinh-hoa-worked-8 -->

::: example Phân biệt fit, transform và fit_transform trên bộ tiền xử lý StandardScaler

Kiến trúc scikit-learn phân định ranh giới rõ ràng giữa việc học tham số phân phối và việc áp dụng phép biến đổi lên dữ liệu. Sử dụng đúng fit_transform trên tập huấn luyện và transform trên tập kiểm thử ngăn ngừa hiện tượng rò rỉ phân phối giữa các tập dữ liệu.

```python
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Dữ liệu tập huấn luyện và tập kiểm thử độc lập
X_train = np.array([[10.0], [20.0], [30.0]])
X_test = np.array([[20.0], [40.0]])

scaler = StandardScaler()

# 1. fit_transform trên tập huấn luyện: học mu=20, sigma=8.16 và biến đổi
X_tr_scaled = scaler.fit_transform(X_train)

# 2. transform trên tập kiểm thử: bắt buộc dùng mu và sigma cũ của train
X_te_scaled = scaler.transform(X_test)

bang_kq = pd.DataFrame({
    "x_test_goc": X_test.ravel(),
    "x_test_chuan": np.round(X_te_scaled.ravel(), 2),
    "mu_train": [scaler.mean_[0]] * len(X_test),
    "sigma_train": [np.round(scaler.scale_[0], 2)] * len(X_test),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| x&#95;test&#95;goc | x&#95;test&#95;chuan | mu&#95;train | sigma&#95;train |
| --- | --- | --- | --- |
| 20.0 | 0.0 | 20.0 | 8.16 |
| 40.0 | 2.45 | 20.0 | 8.16 |

</div>

Thư viện scikit-learn tổ chức các lớp tiền xử lý theo cấu trúc hướng đối tượng nhất quán. Lớp `StandardScaler` thực hiện chuẩn hóa dữ liệu bằng cách đưa biến số về dạng có giá trị trung bình bằng 0 và độ lệch chuẩn bằng 1. Phương thức `fit` quét qua dữ liệu đầu vào để ghi nhận giá trị trung bình vào thuộc tính `mean_` và độ lệch chuẩn vào thuộc tính `scale_`.

`StandardScaler` tính phương sai với `ddof=0`. Ba giá trị huấn luyện 10, 20, 30 có trung bình 20 và độ lệch chuẩn xấp xỉ 8.16. `fit_transform` học hai đại lượng này rồi biến đổi chính dữ liệu huấn luyện. Nếu một cột không đổi, hệ số chia của cột đó được đặt là 1 thay vì chia cho 0.

Khi chuyển sang tập kiểm thử `X_test`, nguyên tắc bắt buộc là chỉ sử dụng phương thức `transform`. Khi đó, các mẫu kiểm thử được chuẩn hóa hoàn toàn dựa trên giá trị trung bình 20.0 và độ lệch chuẩn 8.16 đã học từ tập huấn luyện. Giá trị 20.0 của tập kiểm thử trở thành 0.00 và giá trị 40.0 trở thành 2.45, bảo đảm không làm biến dạng thang đo tham chiếu và tránh hiện tượng rò rỉ dữ liệu.

:::

<!-- /worked-example -->

### Phân chia tập huấn luyện và kiểm thử (Train/Test Split)

Để đánh giá năng lực của mô hình, ta phân tách dữ liệu thành hai tập:
1. **Tập huấn luyện (Training Set)**: Dùng để thuật toán học các trọng số.
2. **Tập kiểm thử (Testing Set)**: Đóng vai trò là tập đánh giá độc lập, không tham gia vào khâu huấn luyện.

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_thuc = df[["dien_tich", "so_phong"]]
y_thuc = df["gia"]

X_train, X_test, y_train, y_test = train_test_split(
    X_thuc, y_thuc,
    test_size=0.25,
    random_state=42
)
```

Việc phân chia ngẫu nhiên thuần túy (`train_test_split`) không tự động tạo ra tính độc lập thống kê giữa hai tập dữ liệu. Nếu dữ liệu có cấu trúc chuỗi thời gian, việc chia ngẫu nhiên sẽ làm rò rỉ dữ liệu tương lai vào tập huấn luyện. Tương tự, nếu dữ liệu có cấu trúc nhóm (chẳng hạn nhiều bản ghi thuộc cùng một người dùng hay bệnh nhân), việc xáo trộn ngẫu nhiên sẽ để lọt quan sát của cùng một thực thể vào cả hai tập. Đối với các bài toán này, việc phân chia cần tuân theo trật tự thời gian (Temporal Split) hoặc phân chia theo nhóm (`GroupKFold`).

<!-- worked-example bai-12-mo-hinh-hoa-worked-9 -->

::: example Phân chia dữ liệu có phân tầng theo nhãn với tham số stratify

Khi dữ liệu có phân bổ nhãn không đồng đều, phân chia ngẫu nhiên thuần túy có thể dẫn đến việc tập kiểm thử thiếu hụt các mẫu thuộc nhóm thiểu số. Tham số stratify trong train_test_split hỗ trợ phân tầng mẫu nhằm xấp xỉ tỷ lệ các nhóm nhãn giữa các tập con.

```python
import pandas as pd
from sklearn.model_selection import train_test_split

# Giả lập tập dữ liệu gồm 10 mẫu với tỷ lệ nhãn 8 bình thường (0) và 2 bất thường (1)
df = pd.DataFrame({
    "dac_trung": range(10),
    "nhan": [0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
})

# Phân chia có phân tầng với stratify
train, test = train_test_split(
    df,
    test_size=0.4,
    random_state=42,
    stratify=df["nhan"],
)

bang_kq = pd.DataFrame({
    "tap": ["Goc", "Train", "Test"],
    "tong_mau": [len(df), len(train), len(test)],
    "so_nhan_0": [
        int((df["nhan"] == 0).sum()),
        int((train["nhan"] == 0).sum()),
        int((test["nhan"] == 0).sum()),
    ],
    "so_nhan_1": [
        int((df["nhan"] == 1).sum()),
        int((train["nhan"] == 1).sum()),
        int((test["nhan"] == 1).sum()),
    ],
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| tap | tong&#95;mau | so&#95;nhan&#95;0 | so&#95;nhan&#95;1 |
| --- | --- | --- | --- |
| Goc | 10 | 8 | 2 |
| Train | 6 | 5 | 1 |
| Test | 4 | 3 | 1 |

</div>

Hàm `train_test_split` là công cụ phân chia mẫu phổ biến trong học máy. Phép lấy mẫu ngẫu nhiên không hoàn lại mặc định hoạt động tốt trên các tập dữ liệu lớn có phân phối nhãn cân bằng. Tuy nhiên, khi đối mặt với dữ liệu có tỷ lệ nhãn chênh lệch lớn, việc bốc thăm ngẫu nhiên hoàn toàn có thể làm phân bố nhãn giữa tập huấn luyện và tập kiểm thử bị sai lệch đáng kể.

Tham số `stratify=df['nhan']` kích hoạt cơ chế lấy mẫu phân tầng. Hàm sẽ chia các bản ghi theo từng nhóm nhãn trước khi tiến hành chọn mẫu ngẫu nhiên vào tập kiểm thử theo tỷ lệ chỉ định `test_size=0.4`. Do số lượng mẫu là các số nguyên cụ thể, tỷ lệ phân chia thực tế tại mỗi nhóm nhãn sẽ được làm tròn số nguyên gần nhất chứ không bảo đảm khớp chính xác 40% trên từng nhóm nhỏ.

Bảng kết quả thể hiện cụ thể sự phân bổ: Tập gốc gồm 8 mẫu nhãn 0 và 2 mẫu nhãn 1. Sau khi phân chia, tập huấn luyện có 5 mẫu nhãn 0 và 1 mẫu nhãn 1, trong khi tập kiểm thử có 3 mẫu nhãn 0 và 1 mẫu nhãn 1. Cả hai tập con đều có đại diện của cả hai nhóm nhãn, hỗ trợ quá trình huấn luyện và đánh giá mô hình diễn ra đầy đủ. Cách chia này không giữ thứ tự thời gian hoặc giữ các quan sát của cùng một đối tượng ở một phía. Với dữ liệu thời gian hay nhiều hàng từ một người, cần chọn cách tách phù hợp để tránh thông tin đi từ tập kiểm thử sang huấn luyện.

:::

<!-- /worked-example -->

### Rò rỉ dữ liệu trong tiền xử lý (Data Preprocessing Leakage)

Một tình huống dễ mắc phải trong các dự án khoa học dữ liệu là việc **thực hiện tiền xử lý trên toàn bộ tập dữ liệu trước khi phân chia train/test**.

Hãy xem xét quy trình chuẩn hóa thang đo Z-score:
$$
z = \frac{x - \mu}{\sigma}
$$
Trong đó $\mu$ là giá trị trung bình và $\sigma$ là độ lệch chuẩn của biến số.

- **Sai lầm gây rò rỉ**: Người làm gọi `StandardScaler().fit_transform(X)` trên toàn bộ bảng dữ liệu gồm cả tập train và test. Khi đó, giá trị $\mu$ và $\sigma$ đã mang theo thông tin phân phối của cả tập kiểm thử. Tập kiểm thử không còn là dữ liệu độc lập, làm sai lệch tính khách quan của việc đánh giá mô hình.
- **Quy chuẩn đúng đắn**: Bộ chuẩn hóa chỉ được phép học tham số $\mu_{\text{train}}$ và $\sigma_{\text{train}}$ trên **duy nhất tập huấn luyện**. Sau đó, ta dùng chính cặp tham số $\mu_{\text{train}}, \sigma_{\text{train}}$ này để biến đổi dữ liệu trên tập kiểm thử:
  $$
  z_{\text{test}} = \frac{x_{\text{test}} - \mu_{\text{train}}}{\sigma_{\text{train}}}
  $$

Lưu ý rằng sự rò rỉ dữ liệu phá vỡ quy trình đánh giá khách quan, dù nó không nhất thiết làm tăng điểm số trong mọi mẫu dữ liệu cụ thể.

### Đóng gói an toàn bằng `Pipeline`

Để khép kín quy trình tiền xử lý, scikit-learn cung cấp cấu trúc **`Pipeline`**. Đường ống này gắn các bước tiền xử lý với mô hình ước lượng thành một thực thể:

```python
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error

# Xây dựng đường ống khép kín
duong_ong = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge(alpha=1.0))
])

# Khi gọi fit trên đường ống:
# 1. scaler chỉ fit và transform trên X_train
# 2. model học trọng số trên ma trận X_train đã chuẩn hóa
duong_ong.fit(X_train, y_train)

# Khi gọi predict trên X_test:
# Đường ống tự động dùng mu và sigma của X_train để transform X_test trước khi dự báo
y_du_doan = duong_ong.predict(X_test)

sai_so_mse = mean_squared_error(y_test, y_du_doan)
print("Sai số toàn phương trung bình (MSE) trên tập kiểm thử:", sai_so_mse)
```

`Pipeline` bảo đảm các bước tiền xử lý chỉ được học trên tập huấn luyện của từng fold đánh giá. Tuy nhiên, `Pipeline` không thể ngăn chặn mọi dạng rò rỉ: Nếu việc rò rỉ phát sinh từ khâu tạo đặc trưng dùng nhãn mục tiêu (target leakage) hoặc do phân tách sai cấu trúc dữ liệu trước khi đưa vào đường ống, sai lệch vẫn sẽ tồn tại.

---

<!-- worked-example bai-12-mo-hinh-hoa-worked-10 -->

::: example Tích hợp tiền xử lý và mô hình hồi quy với ColumnTransformer và Pipeline

Dữ liệu dạng bảng thường kết hợp cả biến số liên tục và biến phân loại chuỗi ký tự. Cấu trúc ColumnTransformer kết hợp Pipeline cho phép phân luồng tiền xử lý độc lập cho từng nhóm cột và tích hợp với mô hình dự báo trong một chuỗi xử lý khép kín.

```python
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

df = pd.DataFrame({
    "dien_tich": [45.0, 60.0, 80.0, 100.0],
    "quan": ["DongDa", "TayHo", "CauGiay", "DongDa"],
    "gia": [2.1, 3.2, 4.3, 4.9],
})

# Phân luồng tiền xử lý cho từng nhóm đặc trưng
tien_xu_ly = ColumnTransformer(transformers=[
    ("num", StandardScaler(), ["dien_tich"]),
    ("cat", OneHotEncoder(drop="first", sparse_output=False), ["quan"]),
])

# Đóng gói tiền xử lý và mô hình hồi quy vào một Pipeline khép kín
pipeline = Pipeline(steps=[
    ("preprocessor", tien_xu_ly),
    ("regressor", Ridge(alpha=1.0)),
])

# Huấn luyện toàn bộ chuỗi xử lý
pipeline.fit(df[["dien_tich", "quan"]], df["gia"])
du_doan = pipeline.predict(df[["dien_tich", "quan"]])

bang_kq = pd.DataFrame({
    "dien_tich": df["dien_tich"],
    "quan": df["quan"],
    "gia_thuc": df["gia"],
    "gia_du_doan": np.round(du_doan, 2),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| dien&#95;tich | quan | gia&#95;thuc | gia&#95;du&#95;doan |
| --- | --- | --- | --- |
| 45.0 | DongDa | 2.1 | 2.47 |
| 60.0 | TayHo | 3.2 | 3.23 |
| 80.0 | CauGiay | 4.3 | 4.08 |
| 100.0 | DongDa | 4.9 | 4.71 |

</div>

Trong các dự án học máy dạng bảng, dữ liệu đầu vào thường bao gồm các cột định lượng cần chuẩn hóa thang đo cùng các cột định tính cần mã hóa biến giả. Nếu tiến hành các bước tiền xử lý rời rạc bên ngoài, việc theo dõi các tham số biến đổi và tái áp dụng lên dữ liệu mới rất dễ phát sinh sai sót kỹ thuật hoặc làm rò rỉ dữ liệu trong quá trình kiểm định.

Lớp `ColumnTransformer` cho phép chỉ định bộ biến đổi riêng biệt cho từng danh sách cột cụ thể. Trong đoạn mã, nhánh `num` áp dụng `StandardScaler` cho cột `dien_tich`, còn nhánh `cat` áp dụng `OneHotEncoder(drop='first', sparse_output=False)` cho cột `quan`. Các đặc trưng sau khi biến đổi được ghép nối thành ma trận số học hoàn chỉnh và chuyển tiếp vào mô hình `Ridge`.

Chuỗi xử lý `Pipeline` đóng gói toàn bộ quy trình từ dữ liệu thô đến đầu ra dự báo. Bảng kết quả hiển thị các giá trị dự đoán được tính toán trực tiếp trên chính tập dữ liệu huấn luyện, phản ánh độ khớp của mô hình với dữ liệu đã học chứ chưa đo lường khả năng tổng quát hóa trên mẫu độc lập bên ngoài. Cấu trúc đường ống giúp mã nguồn gọn gàng và hạn chế rủi ro tính toán sai lệch khi vận hành. `OneHotEncoder` trong cấu hình này sẽ báo lỗi khi gặp một quận chưa có trong tập học. Cần quyết định cách xử lý mức mới trước khi triển khai, chẳng hạn cấu hình `handle_unknown` phù hợp và xem lại ý nghĩa của nhóm tham chiếu.

:::

<!-- /worked-example -->

## 6. Tổng kết

| Thư viện và Công cụ | Vai trò trong quy trình | Điểm lưu ý thực hành |
| :--- | :--- | :--- |
| **pandas to Model** | `to_numpy()`, `get_dummies()` | Cột số chứa `NaN` vẫn giữ kiểu `float64`. Tham số `drop_first=True` áp dụng cho mô hình tuyến tính có intercept để tránh bẫy biến giả. |
| **Patsy Formulas** | `dmatrices("y ~ x0 + C(cat)")` | Ngôn ngữ công thức trực quan, tự động chèn `Intercept`. Dùng `:` cho tương tác và `*` để mở rộng cả hiệu ứng chính lẫn tương tác. |
| **statsmodels** | `smf.ols()`, `AutoReg()` | Hỗ trợ suy diễn thống kê với sai số chuẩn, kiểm định t, F và mô hình hóa chuỗi thời gian. Giả thiết chuẩn chỉ cần thiết cho suy diễn mẫu hữu hạn. |
| **scikit-learn** | `Pipeline`, `fit`, `predict`, `transform` | Phân tách transformer và predictor. Dùng `Pipeline` để khép kín tiền xử lý, nhưng cần kiểm soát cấu trúc dữ liệu để tránh rò rỉ trước đường ống. |

## Tài liệu tham khảo

- [Patsy: Chuẩn hóa trong công thức](https://patsy.readthedocs.io/en/latest/builtins-reference.html).
- [statsmodels: Sai số chuẩn vững](https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.OLSResults.get_robustcov_results.html).


1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Chapter 12: Introduction to Modeling Libraries in Python. URL: [https://wesmckinney.com/book/modeling-libraries](https://wesmckinney.com/book/modeling-libraries).
2. Tài liệu chính thức Patsy: *Describing statistical models in Python*. URL: [https://patsy.readthedocs.io/](https://patsy.readthedocs.io/).
3. Tài liệu chính thức statsmodels: *Econometric and statistical modeling with Python*. URL: [https://www.statsmodels.org/stable/index.html](https://www.statsmodels.org/stable/index.html).
4. Tài liệu chính thức scikit-learn: *Machine Learning in Python*. URL: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 5. Bài tập thực hành

::: exercise Bài tập 1: Đặc tả ma trận mô hình bằng Patsy
Một tập dữ liệu khách hàng bao gồm ba đặc trưng: Thu nhập hàng năm (`income`), tuổi (`age`), và trình độ học vấn (`education` với các mức: `"HighSchool"`, `"Bachelor"`, `"Master"`).
1. Viết công thức Patsy dự đoán biến chi tiêu (`spending`) sử dụng biến đổi logarit của thu nhập, bình phương của tuổi, và biến phân loại học vấn với mức tham chiếu mặc định.
2. Viết đoạn mã kiểm tra danh sách tên các cột sinh ra trong ma trận thiết kế $X$.
:::

::: solution Lời giải chi tiết
Mã nguồn thực hiện:

```python
import pandas as pd
import patsy
import numpy as np

df_kh = pd.DataFrame({
    "income": [30000, 50000, 80000, 120000],
    "age": [22, 35, 45, 50],
    "education": ["HighSchool", "Bachelor", "Master", "Bachelor"],
    "spending": [5000, 12000, 25000, 40000]
})

# Công thức Patsy: Dùng np.log cho income, I(age**2) cho bình phương tuổi, C(education) cho học vấn
cong_thuc = "spending ~ np.log(income) + I(age**2) + C(education)"
y_kh, X_kh = patsy.dmatrices(cong_thuc, data=df_kh)

print("Tên các cột trong ma trận thiết kế:")
for col in X_kh.design_info.column_names:
    print("-", col)
```

Giải thích chi tiết:
- `Intercept`: Cột số hạng tự do mặc định.
- `C(education)[T.HighSchool]`, `C(education)[T.Master]`: Các cột biến giả được tạo ra. Mức `"Bachelor"` đứng đầu bảng chữ cái nên được chọn làm mức tham chiếu ngầm định.
- `np.log(income)`: Biến đổi logarit thu nhập.
- `I(age**2)`: Cần dùng hàm bọc `I()` để bảo vệ toán tử lũy thừa số học `**` khỏi quy ước phân tích cú pháp của Patsy.
:::

::: exercise Bài tập 2: Đọc hiểu và thẩm định bảng hồi quy statsmodels
Hãy huấn luyện một mô hình hồi quy tuyến tính OLS bằng statsmodels giải thích giá nhà dựa trên diện tích và quận, sau đó in ra hệ số xác định $R^2$ cùng p-value của từng biến. Giải thích ý nghĩa của p-value đối với việc đánh giá tính phù hợp của mô hình.
:::

::: solution Lời giải chi tiết
Mã nguồn thực hiện:

```python
import statsmodels.formula.api as smf

df_nha = pd.DataFrame({
    "dien_tich": [40, 55, 60, 75, 80, 95, 100, 120],
    "quan": ["CauGiay", "CauGiay", "DongDa", "DongDa", "TayHo", "TayHo", "CauGiay", "TayHo"],
    "gia": [1.8, 2.5, 2.7, 3.4, 3.9, 4.6, 4.8, 5.9]
})

mo_hinh_nha = smf.ols("gia ~ dien_tich + C(quan)", data=df_nha).fit()

print(f"Hệ số xác định R-squared: {mo_hinh_nha.rsquared:.4f}")
print("Bảng giá trị p-value của các biến giải thích:")
for ten_bien, p_val in mo_hinh_nha.pvalues.items():
    print(f"- {ten_bien}: {p_val:.5f}")
```

Diễn giải học thuật:
- Giá trị $R^2 > 0{,}98$ chứng tỏ diện tích và vị trí quận giải thích được hơn 98% sự biến thiên của giá nhà trong mẫu dữ liệu khảo sát này.
- Giá trị p-value đo lường xác suất quan sát được một hệ số hồi quy có độ lệch lớn như thực tế nếu giả thiết không $\beta_j = 0$ là đúng. Nếu p-value nhỏ hơn ngưỡng danh định 0,05, ta có đủ bằng chứng thống kê để kết luận rằng biến số đó thực sự có ảnh hưởng mang tính hệ thống lên giá nhà, loại trừ khả năng sai khác thuần túy do ngẫu nhiên mẫu.
:::

::: exercise Bài tập 3: Khắc phục lỗi rò rỉ dữ liệu trong scikit-learn
Một lập trình viên tạo dữ liệu mẫu và viết đoạn mã tiền xử lý như sau:

```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

X_mau, y_mau = make_regression(n_samples=100, n_features=5, noise=5.0, random_state=42)

# Tiền xử lý bị lỗi: Chuẩn hóa trên toàn bộ tập dữ liệu trước khi chia tách
scaler = StandardScaler()
X_toan_bo = scaler.fit_transform(X_mau)
X_train, X_test, y_train, y_test = train_test_split(X_toan_bo, y_mau, test_size=0.3, random_state=42)
mo_hinh_ro_ri = Ridge().fit(X_train, y_train)
diem_ro_ri = mo_hinh_ro_ri.score(X_test, y_test)
print("Điểm R^2 với quy trình rò rỉ:", diem_ro_ri)
```

Chỉ rõ lỗi phương pháp luận trong đoạn mã trên và viết lại bằng `Pipeline` chuẩn mực để loại trừ rò rỉ.
:::

::: solution Lời giải chi tiết
Phân tích lỗi phương pháp luận:
Lập trình viên đã gọi `scaler.fit_transform(X_mau)` trên toàn bộ dữ liệu trước khi phân tách `train_test_split`. Lệnh này tính toán giá trị trung bình $\mu$ và độ lệch chuẩn $\sigma$ của toàn thể tập hợp (bao gồm cả các quan sát sẽ rơi vào tập kiểm thử). Đây là hiện tượng **Rò rỉ dữ liệu (Data Leakage)**: Thông tin phân phối của tương lai đã lọt vào quy trình chuẩn bị dữ liệu của tập huấn luyện.

Đoạn mã được sửa đổi chuẩn mực bằng `Pipeline`:

```python
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.pipeline import Pipeline

X_mau, y_mau = make_regression(n_samples=100, n_features=5, noise=5.0, random_state=42)

# 1. Phân tách tập huấn luyện và kiểm thử TRƯỚC TIÊN
X_train, X_test, y_train, y_test = train_test_split(
    X_mau, y_mau, test_size=0.3, random_state=42
)

# 2. Đóng gói quy trình tiền xử lý và mô hình vào Pipeline
duong_ong_chuan = Pipeline([
    ("scaler", StandardScaler()),
    ("model", Ridge())
])

# 3. Huấn luyện đường ống trên tập train (chỉ fit scaler trên X_train)
duong_ong_chuan.fit(X_train, y_train)

# 4. Đánh giá độc lập trên tập test
diem_danh_gia = duong_ong_chuan.score(X_test, y_test)
print("Điểm R^2 trên tập kiểm thử độc lập:", diem_danh_gia)
```
:::

---

## Tài liệu tham khảo

1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Chapter 12: Introduction to Modeling Libraries in Python. URL: [https://wesmckinney.com/book/modeling-libraries](https://wesmckinney.com/book/modeling-libraries).
2. Tài liệu chính thức Patsy: *Describing statistical models in Python*. URL: [https://patsy.readthedocs.io/](https://patsy.readthedocs.io/).
3. Tài liệu chính thức statsmodels: *Econometric and statistical modeling with Python*. URL: [https://www.statsmodels.org/stable/index.html](https://www.statsmodels.org/stable/index.html).
4. Tài liệu chính thức scikit-learn: *Machine Learning in Python*. URL: [https://scikit-learn.org/stable/](https://scikit-learn.org/stable/).

</div>
