---
course: xu-ly-du-lieu
lecture: bai-05-series-dataframe-chuyen-sau
section: lecture
title: "Series & DataFrame chuyên sâu"
prerequisites: ["chi-muc", "gia-tri-thieu", "ky-vong", "phuong-sai"]
lessonStatus: ready
description: "Cơ chế căn chỉnh Index, Split-Apply-Combine với groupby/agg/transform, bảng chéo pivot_table và ghép bảng an toàn với merge validate."
---

## 1. Cơ chế Căn chỉnh Index và Phân kỳ giữa `.loc` và `.iloc`

### 1.1. Bản chất của Index: Nhãn Ngữ nghĩa khác với Vị trí Bộ nhớ
Điểm độc đáo nhất và cũng là nguồn gốc gây ra nhiều bất ngờ nhất cho người mới học pandas chính là: **pandas luôn tự động căn chỉnh dữ liệu theo nhãn chỉ mục (Index Alignment)**, hoàn toàn không phụ thuộc vào vị trí dòng trong bộ nhớ.

```
            Series A (Giá cũ)                 Series B (Giá mới)
        +-------+--------+                +-------+--------+
        | Index | Giá trị |                | Index | Giá trị |
        +-------+--------+                +-------+--------+
        |  "A"  |  100   |                |  "B"  |  220   |
        |  "B"  |  200   |                |  "A"  |   90   |
        |  "C"  |   50   |                |  "D"  |   70   |
        +-------+--------+                +-------+--------+
                         \               /
                          v             v
                    PHÉP TRỪ TỰ ĐỘNG CĂN CHỈNH: B - A
        +-------+-----------------------------+---------+
        | Index | Phép toán tương ứng         | Kết quả |
        +-------+-----------------------------+---------+
        |  "A"  | 90 (từ B) - 100 (từ A)      |   -10   |
        |  "B"  | 220 (từ B) - 200 (từ A)     |    20   |
        |  "C"  | NaN (thiếu ở B) - 50 (từ A) |   NaN   |
        |  "D"  | 70 (từ B) - NaN (thiếu ở A) |   NaN   |
        +-------+-----------------------------+---------+
```

Trong phép trừ `B - A`, pandas không lấy dòng 1 trừ dòng 1 như NumPy! Nó đi tìm phần tử có cùng nhãn `"A"` ở cả hai bên ($90 - 100 = -10$), và phần tử có cùng nhãn `"B"` ($220 - 200 = 20$). Các nhãn chỉ xuất hiện ở một phía (nhãn `"C"` chỉ có ở $A$, nhãn `"D"` chỉ có ở $B$) do thiếu toán hạng đối ứng nên kết quả tự động trở thành `NaN`.
Index của Series kết quả là **hợp của hai tập nhãn (*Union of indexes*)**: `{"A", "B", "C", "D"}`.

### 1.2. Phân định Tuyệt đối giữa `.loc` và `.iloc`
Khi một bảng dữ liệu có Index là các số nguyên không liên tục (ví dụ sau khi xáo trộn hoặc lọc dòng): `index = [2, 0, 5]`:
- **`s.loc[nhan]`**: Tra cứu theo **nhãn định danh**. `s.loc[2]` tìm phần tử có nhãn bằng số `2` (đứng ở dòng đầu tiên).
- **`s.iloc[vi_tri]`**: Tra cứu theo **vị trí số nguyên vật lý** trong mảng ($0, 1, \dots, n-1$ hoặc $-1$ từ cuối). `s.iloc[2]` lấy phần tử ở dòng thứ ba (mang nhãn `5`).

Trong môi trường sản xuất, ta không bao giờ dùng cú pháp nhập nhằng `s[2]`. Luôn luôn chỉ định tường minh `.loc` khi làm việc với nhãn nghiệp vụ và `.iloc` khi đếm vị trí tương đối.

---

## 2. Mô hình Chia để trị: `groupby`, `agg` và `transform`

Trong phân tích dữ liệu, hầu hết các câu hỏi nghiệp vụ đều tuân theo mô hình **Split-Apply-Combine (Tách nhóm - Áp dụng - Gộp kết quả)** do Hadley Wickham hệ thống hóa:
1. **Split**: Chia dữ liệu thành các nhóm độc lập dựa trên một hoặc nhiều biến phân loại (ví dụ: chia theo quận hoặc theo phân khúc giá).
2. **Apply**: Áp dụng một hàm tính toán lên từng nhóm.
3. **Combine**: Gộp kết quả của các nhóm thành một cấu trúc dữ liệu mới.

```
                      BẢNG GỐC BAN ĐẦU (12 dòng)
                                 |
                                 v  groupby("phan_khuc")
            +--------------------+--------------------+
            |                    |                    |
            v                    v                    v
       Nhóm "re"            Nhóm "trung"         Nhóm "cao"
            |                    |                    |
            +--------------------+--------------------+
                                 |
               +-----------------+-----------------+
               |                                   |
               v Dùng .agg(...)                    v Dùng .transform(...)
      THU GỌN KÍCH THƯỚC (3 dòng)           BẢO TOÀN KÍCH THƯỚC (12 dòng)
     +-----------+--------------+          Mỗi dòng nhận đúng giá trị
     | phan_khuc | gia_trung_vi |          thống kê của nhóm chứa nó.
     +-----------+--------------+          (Dùng để gắn cờ hoặc chuẩn hóa)
     | re        |   21,500.0   |
     | trung     |   55,000.0   |
     | cao       |  120,000.0   |
     +-----------+--------------+
```

### 2.1. Cú pháp Đặt tên Cột Tổng hợp (Named Aggregation)
Thay vì dùng cú pháp cũ trả về MultiIndex phức tạp, pandas hỗ trợ cú pháp đặt tên cột trực tiếp cực kỳ tường minh:
```python
thong_ke = df.groupby("phan_khuc").agg(
    so_phong=("id", "size"),
    gia_trung_vi=("price", "median"),
    review_nam_tb=("number_of_reviews_ltm", "mean")
)
```
Mỗi tham số là một tuple gồm `("tên_cột_nguồn", "hàm_tổng_hợp")`. Bảng kết quả trả về các cột phẳng, đúng tên nghiệp vụ mong muốn và sẵn sàng xuất bản.

### 2.2. Điểm Khác biệt Sống còn giữa `agg` và `transform`
- **`agg` (Aggregate)**: Làm **suy giảm số chiều dữ liệu**. Nếu có 10 nhóm, kết quả trả về đúng 10 dòng đại diện.
- **`transform`**: **Bảo tồn nguyên vẹn số dòng của bảng ban đầu**. Hàm tính toán chỉ số cho từng nhóm rồi phát tán (*broadcast*) ngược lại cho từng bản ghi thuộc nhóm đó.

Ví dụ: Bạn muốn biết mỗi phòng trọ nằm trong một quận có quy mô bao nhiêu phòng, để từ đó lọc bỏ các phòng thuộc các quận quá nhỏ ($< 300$ phòng):
```python
# Gắn quy mô quận vào từng dòng (Series cùng độ dài với bảng gốc):
n_quan = df.groupby("neighbourhood")["id"].transform("size")

# Lọc các dòng thuộc quận lớn mà không làm biến dạng cấu trúc bảng:
df_quan_lon = df[n_quan >= 300]
```
Nếu dùng `agg("size")`, bạn chỉ nhận được một bảng danh sách quận và số đếm, không thể lọc trực tiếp trên các dòng của bảng gốc.

---

## 3. Bảng chéo Hai chiều (`pivot_table`) và Phát hiện Biến ẩn

Khi cần khảo sát mối quan hệ giữa hai biến phân loại độc lập lên một biến đo lường liên tục, công cụ chuẩn mực là `pivot_table`:
- **`index`**: Biến phân nhóm theo chiều dọc (các hàng).
- **`columns`**: Biến phân nhóm theo chiều ngang (các cột).
- **`values`**: Cột dữ liệu cần tổng hợp.
- **`aggfunc`**: Phép toán thống kê (mặc định là `"mean"`).

```python
pv = df.pivot_table(
    index="phan_khuc",
    columns="chuyen",
    values="number_of_reviews_ltm",
    aggfunc="mean"
)
```

### Ý nghĩa kinh tế lượng: Kiểm soát Biến ẩn Ngoại sinh (*Confounder*)
Xét câu hỏi: *"Các chủ nhà chuyên nghiệp (sở hữu $\ge 5$ phòng) có hoạt động hiệu quả hơn chủ nhà cá nhân không?"*
- Nếu chỉ so sánh một chiều đơn giản qua `groupby("chuyen")`, ta thấy chủ nhà chuyên nghiệp có số lượt đánh giá trung bình cao hơn ($15.2$ so với $12.7$).
- Tuy nhiên, khi tách ma trận hai chiều bằng `pivot_table` theo từng phân khúc giá: ta phát hiện ở cùng phân khúc cao cấp, số review của chủ nhà chuyên nghiệp và cá nhân là tương đương nhau.
- Sở dĩ số liệu chung của nhóm chuyên nghiệp cao hơn là vì họ tập trung tới $80\%$ cơ sở tại các quận trung tâm du lịch sầm uất (nơi có lưu lượng khách tự nhiên rất lớn). Địa điểm quận chính là một **biến ẩn ngoại sinh (*Confounding Variable*)**. `pivot_table` giúp bóc tách và phân lập các hiệu ứng này một cách minh bạch.

---

## 4. Hợp nhất Bảng Dữ liệu (`merge`) và Kỷ luật `validate`

### 4.1. Bốn Kiểu Ghép Nối Đại số Quan hệ
Khi kết hợp bảng `df_trai` với bảng `df_phai` theo khóa liên kết `on="khoa"`:
- `how="left"`: Giữ trọn vẹn mọi dòng của bảng trái. Bảng phải không khớp sẽ điền `NaN`.
- `how="right"`: Giữ trọn vẹn mọi dòng của bảng phải.
- `how="inner"`: Chỉ giữ lại các dòng mà khóa xuất hiện ở cả hai bảng (phép giao).
- `how="outer"`: Giữ lại toàn bộ các dòng của cả hai bảng (phép hợp).

### 4.2. Vũ khí Phòng thủ Toàn vẹn Dữ liệu: `validate="m:1"`
Trong các đường ống xử lý dữ liệu doanh nghiệp, một trong những thảm họa kinh hoàng nhất là lỗi **Nhân bản số dòng ngoài tầm kiểm soát (*Row Explosion / Cartesian Bug*)**.
Giả sử bạn có bảng giao dịch gồm $18,534$ dòng, và bạn muốn ghép thêm bảng biểu phí dịch vụ theo phân khúc gồm 3 dòng (`re: 10%`, `trung: 13%`, `cao: 15%`).
Nếu vô tình bảng biểu phí bị lỗi hệ thống và xuất hiện hai dòng cùng mang nhãn `"trung"`, một phép ghép `how="left"` thông thường sẽ nhân đôi mỗi giao dịch ở phân khúc trung! Bảng kết quả sẽ phình to lên thành $30,000$ dòng và toàn bộ báo cáo doanh thu tài chính bị đội lên gấp bội mà không hề có bất kỳ thông báo lỗi nào!

Để ngăn chặn thảm họa này, pandas cung cấp tham số kiểm định **`validate`**:
- `validate="1:1"`: Kiểm tra khóa ở cả hai bảng đều phải là duy nhất.
- `validate="1:m"`: Khóa ở bảng trái là duy nhất, bảng phải có thể lặp lại.
- **`validate="m:1"`**: Khóa ở bảng trái có thể lặp lại nhiều lần, nhưng **khóa ở bảng tra cứu bên phải BẮT BUỘC phải là duy nhất**.

```python
# Nếu bảng phi có khóa phân khúc bị trùng lặp,
# pandas sẽ lập tức dừng chương trình và ném lỗi pd.errors.MergeError!
m = pd.merge(df, phi, on="phan_khuc", how="left", validate="m:1")
```

---

## 5. Bài tập Thực chiến Phòng Lab 05 (100% Nội dung Lab)

Dưới đây là trọn vẹn các bài tập từ Lab 05, đi sâu vào cấu trúc thị trường phòng trọ Santiago theo hai trục phân tích: **Phân khúc giá** và **Kiểu chủ nhà (Cá nhân vs Chuyên nghiệp)**.

### Dữ liệu mẫu dùng trong bài tập
Bảng giả lập 12 dòng `DEMO` chứa đầy đủ các tình huống nghiệp vụ:
```python
import numpy as np
import pandas as pd

DEMO = pd.DataFrame({
    "id": list(range(201, 213)),
    "neighbourhood": ["Santiago"] * 5 + ["Providencia"] * 4 + ["Ñuñoa"] * 2 + ["Vitacura"],
    "price": [25000.0, 45000.0, 120000.0, np.nan, 60000.0,
              30000.0, 99999.0, 100000.0, 18000.0,
              55000.0, 150000.0, 210000.0],
    "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
    "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
})
```

---

### Bài tập 1 (Q1): Khởi động: Phân biệt `loc` theo Nhãn và `iloc` theo Vị trí
::: exercise Tra cứu phần tử qua hai hệ thống chỉ mục
Cho một Series có Index không trùng lặp:
```python
s = pd.Series([100, 200, 300], index=[2, 0, 5])
```
Viết hàm `loc_iloc(s: pd.Series, nhan: any, vi_tri: int) -> dict`.
Yêu cầu trả về từ điển có đúng hai khóa:
- `theo_nhan`: Phần tử mang nhãn `nhan` (dùng `.loc`).
- `theo_vi_tri`: Phần tử ở vị trí thứ `vi_tri` (dùng `.iloc`).
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def loc_iloc(s: pd.Series, nhan, vi_tri: int) -> dict:
    return {
        "theo_nhan": s.loc[nhan],
        "theo_vi_tri": s.iloc[vi_tri]
    }
```
*Phân tích*: Với `nhan = 2` và `vi_tri = 2`:
- `s.loc[2]` trả về `100` (dòng đầu tiên có nhãn bằng 2).
- `s.iloc[2]` trả về `300` (dòng thứ 3 ở vị trí chỉ số 2).
:::

---

### Bài tập 2 (Q2): Cơ chế Alignment: Phép toán Tự động Khớp theo Index
::: exercise Tính toán độ lệch giá giữa hai thời kỳ
Cho hai Series giá phòng:
```python
gia_cu = pd.Series({"A": 100, "B": 200, "C": 50})
gia_moi = pd.Series({"B": 220, "A": 90, "D": 70})
```
Viết hàm `align_change(gia_cu: pd.Series, gia_moi: pd.Series) -> dict`.
Yêu cầu trả về từ điển gồm:
- `thay_doi`: Series kết quả của phép trừ `gia_moi - gia_cu`.
- `so_nan`: int, tổng số lượng giá trị `NaN` xuất hiện trong kết quả.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def align_change(gia_cu: pd.Series, gia_moi: pd.Series) -> dict:
    thay_doi = gia_moi - gia_cu
    so_nan = int(thay_doi.isna().sum())
    return {
        "thay_doi": thay_doi,
        "so_nan": so_nan
    }
```

#### Giải thích cơ chế:
- Nhãn `"A"`: $90 - 100 = -10$.
- Nhãn `"B"`: $220 - 200 = 20$.
- Nhãn `"C"` chỉ có ở `gia_cu`, nhãn `"D"` chỉ có ở `gia_moi` $\to$ cả hai đều biến thành `NaN`. Do đó `so_nan = 2`.
:::

---

### Bài tập 3 (Q3): Sinh Cột Phân loại Bằng `map` với Hàm Nghiệp vụ
::: exercise Phân khúc giá chỗ ở phòng thủ
Viết hàm `phan_khuc(gia: any) -> str | None`.
Quy tắc phân khúc:
- `pd.isna(gia)` hoặc `None` $\to$ trả về `None`.
- $gia < 30,000 \to$ `"re"`.
- $30,000 \le gia < 100,000 \to$ `"trung"` (đúng $30,000$ là `"trung"`, $99,999$ vẫn là `"trung"`).
- $gia \ge 100,000 \to$ `"cao"` (đúng $100,000$ là `"cao"`).
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def phan_khuc(gia):
    if pd.isna(gia) or gia is None:
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    else:
        return "cao"
```
*Áp dụng vào bảng*: `df["phan_khuc"] = df["price"].map(phan_khuc)`.
:::

---

### Bài tập 4 (Q4): Tổng hợp Đa Cột với `groupby` và `agg` Đặt tên
::: exercise Lập báo cáo chỉ số theo ba phân khúc giá
Viết hàm `segment_stats(df: pd.DataFrame) -> pd.DataFrame`.
Yêu cầu:
- Thực hiện `groupby("phan_khuc")` (bỏ qua các dòng bị thiếu phân khúc).
- Sử dụng `agg` với ba cột đặt tên theo đúng thứ tự:
  - `so_phong = ("id", "size")`
  - `gia_trung_vi = ("price", "median")`
  - `review_nam_tb = ("number_of_reviews_ltm", "mean")`
- Index kết quả là các phân khúc có mặt, không sửa DataFrame đầu vào.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def segment_stats(df: pd.DataFrame) -> pd.DataFrame:
    # Lọc bỏ các dòng thiếu phân khúc trước khi nhóm nếu cần
    df_valid = df.dropna(subset=["phan_khuc"])
    
    return df_valid.groupby("phan_khuc").agg(
        so_phong=("id", "size"),
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean")
    )
```
*Nhận xét trên dữ liệu Santiago thật*: Phân khúc `"trung"` chiếm tỷ trọng áp đảo ($12,325$ phòng), và số review trung bình của phân khúc này đạt cao nhất ($\approx 15.4$ review/năm), cho thấy đây là phân khúc thanh khoản tốt nhất của thị trường.
:::

---

### Bài tập 5 (Q5): Phân tích Mô hình Chủ nhà Chuyên nghiệp
::: exercise Khảo sát sự khác biệt giữa chủ nhà cá nhân và chuyên nghiệp
Viết hàm `pro_host_summary(df: pd.DataFrame, nguong: int = 5) -> dict`.
Quy ước: Chủ nhà có $\ge nguong$ cơ sở lưu trú được coi là "chuyên nghiệp".
Yêu cầu trả về từ điển gồm:
- `chuyen`: Series Boolean `calculated_host_listings_count >= nguong`, cùng index với `df`.
- `ty_le_chuyen`: float, tỷ lệ các dòng thuộc chủ nhà chuyên nghiệp.
- `so_sanh`: DataFrame tổng hợp từ `df.groupby(chuyen)` với hai cột đặt tên: `gia_trung_vi = ("price", "median")` và `review_nam_tb = ("number_of_reviews_ltm", "mean")`.
- **Tuyệt đối không thêm cột vào DataFrame `df` đầu vào**.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def pro_host_summary(df: pd.DataFrame, nguong: int = 5) -> dict:
    chuyen = df["calculated_host_listings_count"] >= nguong
    ty_le_chuyen = float(chuyen.mean())
    
    # Nhóm trực tiếp trên Series Boolean bên ngoài mà không làm đổi bảng gốc
    so_sanh = df.groupby(chuyen).agg(
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean")
    )
    
    return {
        "chuyen": chuyen,
        "ty_le_chuyen": ty_le_chuyen,
        "so_sanh": so_sanh
    }
```
:::

---

### Bài tập 6 (Q6): Gắn Thông tin Quy mô Nhóm bằng `transform`
::: exercise Bảo toàn cấu trúc dòng để lọc nhóm lớn
Viết hàm `big_districts(df: pd.DataFrame, nguong: int = 300) -> dict`.
Yêu cầu trả về từ điển gồm:
- `n_quan`: Series số dòng của quận chứa mỗi dòng, tạo bằng `df.groupby("neighbourhood")["id"].transform("size")`, cùng index và độ dài với `df`.
- `df_dong`: DataFrame các dòng thuộc về những quận có quy mô $\ge nguong$ dòng. Không thêm cột `n_quan` vào kết quả.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def big_districts(df: pd.DataFrame, nguong: int = 300) -> dict:
    n_quan = df.groupby("neighbourhood")["id"].transform("size")
    df_dong = df[n_quan >= nguong]
    
    return {
        "n_quan": n_quan,
        "df_dong": df_dong
    }
```
*Đối chiếu thực tế*: Trên toàn thành phố Santiago, có $16,850$ phòng thuộc về 8 quận lớn nhất có quy mô từ $300$ phòng trở lên.
:::

---

### Bài tập 7 (Q7): Phân tích Ma trận Hai chiều với `pivot_table`
::: exercise Bóc tách tương tác giữa phân khúc giá và kiểu chủ nhà
Viết hàm `segment_host_pivot(df: pd.DataFrame) -> pd.DataFrame`.
Yêu cầu:
- Tạo bảng `pivot_table` với:
  - `index = "phan_khuc"`
  - `columns = "chuyen"`
  - `values = "number_of_reviews_ltm"`
  - `aggfunc = "mean"`
- Các ô tổ hợp không có dữ liệu để nguyên giá trị `NaN` mặc định.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def segment_host_pivot(df: pd.DataFrame) -> pd.DataFrame:
    return df.pivot_table(
        index="phan_khuc",
        columns="chuyen",
        values="number_of_reviews_ltm",
        aggfunc="mean"
    )
```

#### Luận giải sư phạm:
- Tại phân khúc `"trung"`, chủ nhà chuyên nghiệp có số review trung bình cao hơn rõ rệt ($16.5$ so với $14.8$).
- Tuy nhiên, tại phân khúc `"cao"`, chủ nhà cá nhân lại có mức đánh giá tương đương hoặc nhỉnh hơn khi được chăm sóc tỉ mỉ từng chi tiết. Bảng chéo chứng minh không thể đưa ra một kết luận cào bằng cho toàn bộ thị trường.
:::

---

### Bài tập 8 (Q8): Nối Bảng Tra cứu và Bảo vệ Tính Toàn vẹn với `validate="m:1"`
::: exercise Ghép bảng biểu phí dịch vụ và ngăn chặn trùng khóa
Cho bảng biểu phí dịch vụ theo phân khúc:
```python
phi = pd.DataFrame({
    "phan_khuc": ["re", "trung", "cao"],
    "phi_dich_vu": [0.10, 0.13, 0.15]
})
```
Viết hàm `merge_fees(df: pd.DataFrame, phi: pd.DataFrame) -> dict`.
Yêu cầu:
- Nối bảng `df` với bảng `phi` theo cột `phan_khuc`, sử dụng phương thức `how="left"` và bắt buộc thiết lập **`validate="m:1"`**.
- Trả về từ điển gồm:
  - `m`: DataFrame sau khi ghép nối.
  - `so_dong_m`: int, tổng số dòng của `m`.
  - `so_nan_phi`: int, số lượng giá trị `NaN` trong cột `phi_dich_vu`.
- Nếu bảng `phi` có khóa phân khúc bị trùng, để mặc định ngoại lệ `pd.errors.MergeError` được ném ra để cảnh báo hệ thống.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def merge_fees(df: pd.DataFrame, phi: pd.DataFrame) -> dict:
    m = pd.merge(df, phi, on="phan_khuc", how="left", validate="m:1")
    so_dong_m = len(m)
    so_nan_phi = int(m["phi_dich_vu"].isna().sum())
    
    return {
        "m": m,
        "so_dong_m": so_dong_m,
        "so_nan_phi": so_nan_phi
    }
```

#### Giải thích bản chất:
1. `so_dong_m` luôn bằng đúng số dòng ban đầu của `df` ($18,534$ trên dữ liệu thật). Điều này chứng minh không có dòng nào bị nhân đôi.
2. Cột `phi_dich_vu` xuất hiện $846$ giá trị `NaN` vì đúng $846$ phòng này ban đầu bị thiếu giá (`price` là `NaN`), dẫn đến `phan_khuc` là `None` và không thể khớp với bất kỳ dòng nào trong bảng biểu phí.
3. Tham số `validate="m:1"` là tấm lá chắn thép: nếu vô tình bảng `phi` có hai dòng cùng là `"trung"`, pandas sẽ lập tức báo lỗi `MergeError` thay vì âm thầm nhân bản số dòng của dữ liệu.
:::

---

### Bài tập 9 (Mở rộng E1 & E2): Thống kê Đỉnh và Cơ cấu Quận
::: exercise Hai bài tập mở rộng nâng cao năng lực phân tích
1. **Tìm phòng đắt nhất từng quận**: Trên tập dữ liệu các quận lớn (`df_dong`), sử dụng `transform("max")` để lọc ra các căn phòng có mức giá cao nhất của từng quận.
2. **Cơ cấu phân khúc theo quận**: Sử dụng `crosstab` hoặc `pivot_table` để tính tỷ trọng phần trăm của 3 phân khúc giá trong từng quận. Quận nào có tỷ trọng phân khúc cao cấp dẫn đầu?
:::

::: solution
#### Lời giải:
```python
# 1. Tìm phòng đắt nhất từng quận bằng transform("max")
gia_max_quan = df_dong.groupby("neighbourhood")["price"].transform("max")
phong_dat_nhat = df_dong[df_dong["price"] == gia_max_quan][["id", "neighbourhood", "price"]]
print("Các phòng đắt nhất từng quận:\n", phong_dat_nhat.drop_duplicates(subset=["neighbourhood"]))

# 2. Cơ cấu phân khúc theo quận
co_cau_quan = pd.crosstab(
    df_dong["neighbourhood"],
    df_dong["phan_khuc"],
    normalize="index"
)
print("Cơ cấu phân khúc:\n", (co_cau_quan * 100).round(1))
```
*Kết luận*: Quận **Lo Barnechea** và **Vitacura** dẫn đầu toàn thành phố với tỷ trọng phân khúc cao cấp chiếm tới $> 60\%$ tổng số phòng.
:::

---

## 6. Tổng kết Bài học

1. **Hiểu rõ Index Alignment**: Phép toán giữa hai Series luôn tự động so khớp theo nhãn chỉ mục. Khi nhãn bị lệch, kết quả sẽ sinh ra `NaN`.
2. **Phân biệt `agg` và `transform`**: `agg` dùng để thu gọn và tóm tắt theo nhóm; `transform` dùng để tính toán và phát tán ngược lại từng dòng mà không làm thay đổi kích thước bảng ban đầu.
3. **Phân tích đa chiều với `pivot_table`**: Luôn kiểm tra các tương tác chéo để tránh cào bằng số liệu và nhận diện các biến ẩn ngoại sinh.
4. **Kỷ luật `validate="m:1"` khi nối bảng**: Luôn kiểm định quan hệ khóa ngoại khi thực hiện `pd.merge()` để bảo vệ đường ống dữ liệu khỏi lỗi nhân bản số dòng.
