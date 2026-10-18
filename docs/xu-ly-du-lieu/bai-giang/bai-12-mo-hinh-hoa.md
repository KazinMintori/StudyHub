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

### Mã hóa biến phân loại với `pd.get_dummies` và Bẫy biến giả

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

## 4. Giới thiệu thư viện scikit-learn và Cạm bẫy rò rỉ dữ liệu

Trong khi statsmodels hướng tới suy diễn thống kê, **scikit-learn** tập trung vào khả năng khái quát hóa trên dữ liệu mới chưa từng thấy (Generalization) và chuẩn hóa quy trình học có giám sát và không giám sát.

### Giao diện Estimator chuẩn mực

Trong scikit-learn, các họ thuật toán tuân thủ phân định giao diện rõ ràng:
- `fit(X, y)`: Học các tham số từ tập dữ liệu huấn luyện.
- `predict(X)`: Áp dụng các tham số đã học để suy diễn nhãn hoặc giá trị cho dữ liệu mới (dành cho các mô hình dự đoán như `LinearRegression`, `Ridge`).
- `transform(X)`: Biến đổi dữ liệu đặc trưng (dành cho các bộ tiền xử lý như `StandardScaler`).

Cần lưu ý: Không phải mọi đối tượng trong scikit-learn đều có cả hai phương thức `predict` và `transform`. Các transformer chỉ có `transform`, trong khi các estimator dự đoán chỉ có `predict`.

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

## 6. Tổng kết

| Thư viện và Công cụ | Vai trò trong quy trình | Điểm lưu ý thực hành |
| :--- | :--- | :--- |
| **pandas to Model** | `to_numpy()`, `get_dummies()` | Cột số chứa `NaN` vẫn giữ kiểu `float64`. Tham số `drop_first=True` áp dụng cho mô hình tuyến tính có intercept để tránh bẫy biến giả. |
| **Patsy Formulas** | `dmatrices("y ~ x0 + C(cat)")` | Ngôn ngữ công thức trực quan, tự động chèn `Intercept`. Dùng `:` cho tương tác và `*` để mở rộng cả hiệu ứng chính lẫn tương tác. |
| **statsmodels** | `smf.ols()`, `AutoReg()` | Hỗ trợ suy diễn thống kê với sai số chuẩn, kiểm định t, F và mô hình hóa chuỗi thời gian. Giả thiết chuẩn chỉ cần thiết cho suy diễn mẫu hữu hạn. |
| **scikit-learn** | `Pipeline`, `fit`, `predict`, `transform` | Phân tách transformer và predictor. Dùng `Pipeline` để khép kín tiền xử lý, nhưng cần kiểm soát cấu trúc dữ liệu để tránh rò rỉ trước đường ống. |

## Tài liệu tham khảo

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
