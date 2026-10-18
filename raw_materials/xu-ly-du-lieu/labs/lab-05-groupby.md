## Phân tích nhóm với groupby, transform, pivot table và mở rộng cấp quận

Sau khi phân loại dải giá, ta cần đếm chỗ ở, tính trung vị giá và tổng hợp lượt đánh giá theo nhóm. Những bài sau giúp chọn giữa `agg`, `transform` và `pivot_table`, đồng thời giữ rõ mỗi kết quả đại diện cho chỗ ở, nhóm chủ nhà hay quận.

---

## 1. Thiết lập môi trường và dữ liệu thực hành

Để bảo đảm toàn bộ quy trình phân tích nhóm có thể thực thi độc lập, môi trường thực hành được khởi tạo với bảng dữ liệu mẫu gồm 12 dòng (`DEMO`, đơn vị giá: CLP/đêm). Bảng này bao gồm định danh phòng, tên quận, giá niêm yết, số lượt đánh giá trong 12 tháng qua (`number_of_reviews_ltm`) và tổng số lượng niêm yết của chủ nhà (`calculated_host_listings_count`).

```python
import numpy as np
import pandas as pd

# 12 dòng dữ liệu mẫu giả lập (đơn vị: CLP/đêm)
DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


# Hàm phân loại dải giá hỗ trợ tạo cột phân khúc
def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


# Bổ sung cột phân khúc giá cho bảng dữ liệu mẫu
DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Địa chỉ lưu trữ snapshot thực tế Inside Airbnb
SNAPSHOT_URL = (
    "https://data.insideairbnb.com/chile/rm/santiago/"
    "2026-06-29/visualisations/listings.csv"
)
```

> [!NOTE]
> **Đối chiếu thực tế**: Trên snapshot thực tế toàn thành phố Santiago gồm 18.534 niêm yết, phân khúc trung bình có 12.325 phòng với trung bình cột số đánh giá 12 tháng gần nhất xấp xỉ 15,4 lượt, trong khi phân khúc cao có mức giá trung vị đạt 145.318 CLP. Tỷ lệ chỗ ở do nhóm chủ nhà có nhãn chuyên nghiệp đăng chiếm 35,8% toàn thành phố với giá trung vị 65.078 CLP, trong khi nhóm chủ nhà cá nhân ghi nhận 12,7 lượt đánh giá trung bình. Toàn thành phố có 16.850 chỗ ở tập trung tại 8 quận lớn đạt quy mô từ 300 phòng trở lên.

---

## 2. Nội dung chi tiết các bài tập thực hành

<span id="data-lab-05-04"></span>
### Bài tập 4: Thống kê đặc trưng các phân khúc giá bằng agg đặt tên

::: exercise Thống kê ba phân khúc giá
Cho một DataFrame `df` chứa ít nhất bốn cột: `id`, `phan_khuc` (chuỗi hoặc giá trị khuyết), `price` và `number_of_reviews_ltm`.

Hãy viết hàm `segment_stats(df: pd.DataFrame) -> pd.DataFrame` nhóm bảng dữ liệu theo `phan_khuc` và áp dụng phương thức `.agg()` với đúng ba cột được đặt tên tường minh theo thứ tự sau:
1. `so_phong`: Số lượng phòng trong phân khúc, tính bằng `("id", "size")`.
2. `gia_trung_vi`: Mức giá trung vị của phân khúc, tính bằng `("price", "median")`.
3. `review_nam_tb`: Số lượt đánh giá trung bình trong năm qua, tính bằng `("number_of_reviews_ltm", "mean")`.

Yêu cầu kỹ thuật: Chỉ mục của DataFrame kết quả là các phân khúc giá hiện diện trong bảng (các dòng khuyết phân khúc tự động bị loại bỏ theo mặc định của phép nhóm). Không làm tròn số liệu trong hàm và không làm biến đổi DataFrame `df` đầu vào.
:::

::: solution
#### Cách 1: Nhóm theo phân khúc và đặt tên từng cột tổng hợp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Bắt đầu lời giải

import pandas as pd


def segment_stats(df: pd.DataFrame) -> pd.DataFrame:
    # Nhóm theo phân khúc và tổng hợp đồng thời ba chỉ số với tên cột tùy chỉnh
    ket_qua = df.groupby("phan_khuc", observed=True).agg(
        so_phong=("id", "size"),
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"),
    )
    return ket_qua


# Gọi thử nghiệm hàm trên dữ liệu mẫu DEMO:
bang_thong_ke_c1 = segment_stats(DEMO)
print("Kết quả thống kê Cách 1:")
print(bang_thong_ke_c1)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`df.groupby("phan_khuc", observed=True)` xác định các nhóm hiện có. Các dòng khuyết khóa nhóm bị bỏ qua theo mặc định, nên dòng id 204 không được đưa vào ba nhóm giá. `observed=True` còn giúp chỉ giữ các nhóm có quan sát khi cột đã có kiểu `category`.

Trong `.agg`, mỗi tên bên trái là một cột kết quả. Tuple `("id", "size")` chọn cột `id` và đếm số dòng, kể cả khi một ô `id` khuyết. Đổi `size` thành `count` sẽ đổi quy tắc thành đếm ô không khuyết. `median` và `mean` tổng hợp cột số và bỏ qua giá trị khuyết theo quy tắc của pandas.

Ở phân khúc cao, bốn giá là `100000`, `120000`, `150000`, `210000`. Trung vị là trung bình hai giá ở giữa, bằng `135000`. Tổng số đánh giá của nhóm là 14, chia cho 4 được `3.5`. Bảng kết quả chỉ có một dòng cho mỗi phân khúc, không còn một dòng cho mỗi chỗ ở.

##### Output Cách 1

| `phan_khuc` | `so_phong` | `gia_trung_vi` | `review_nam_tb` |
|---|---|---|---|
| `cao` | 4 | 135000.0 | 3.5 |
| `re` | 2 | 21500.0 | 6.0 |
| `trung` | 5 | 55000.0 | 17.0 |

#### Cách 2: Đặt thứ tự phân khúc trước khi tổng hợp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Bắt đầu lời giải

import pandas as pd


def segment_stats(df: pd.DataFrame) -> pd.DataFrame:
    # Tạo bản sao cục bộ để thiết lập thứ tự phân loại có trật tự
    df_loc = df.dropna(subset=["phan_khuc"]).copy()
    thu_tu = ["re", "trung", "cao"]
    df_loc["phan_khuc"] = pd.Categorical(
        df_loc["phan_khuc"], categories=thu_tu, ordered=True
    )

    ket_qua = df_loc.groupby("phan_khuc", observed=True).agg(
        so_phong=("id", "size"),
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"),
    )
    return ket_qua


# Gọi thử nghiệm hàm trên dữ liệu mẫu DEMO:
bang_thong_ke_c2 = segment_stats(DEMO)
print("Kết quả thống kê Cách 2:")
print(bang_thong_ke_c2)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`dropna(subset=["phan_khuc"])` chỉ loại dòng thiếu khóa nhóm. `.copy()` tạo bảng làm việc để phép gán sau đó không sửa `df`. `pd.Categorical` khai báo rõ ba nhãn hợp lệ và thứ tự `re`, `trung`, `cao`. Với `ordered=True`, thứ tự này có ý nghĩa khi sắp xếp hoặc so sánh các nhãn phân loại.

Ba phép tổng hợp trong `.agg` giữ nguyên ý nghĩa của Cách 1. Điểm thêm là bảng được trình bày theo thứ tự dải giá thay vì thứ tự chữ cái. Yêu cầu của đề chỉ nhận các nhóm có mặt trong dữ liệu. Vì vậy với đầu vào không có đủ ba dải, cần dùng chế độ nhóm chỉ lấy các giá trị đã quan sát, thay vì tạo thêm hàng rỗng cho danh mục vắng mặt.

DEMO có đủ cả ba phân khúc nên bảng dưới đây chứa đủ ba hàng. Việc đổi kiểu phân loại đòi hỏi đầu vào thật sự chỉ có các nhãn đã khai báo. Một nhãn nằm ngoài danh mục sẽ thành giá trị khuyết và cần được phát hiện trước khi phân tích.

##### Output Cách 2

| `phan_khuc` | `so_phong` | `gia_trung_vi` | `review_nam_tb` |
|---|---|---|---|
| `re` | 2 | 21500.0 | 6.0 |
| `trung` | 5 | 55000.0 | 17.0 |
| `cao` | 4 | 135000.0 | 3.5 |

#### So sánh hai cách

Cách 1 đáp ứng trực tiếp nhu cầu tổng hợp. Cách 2 phù hợp khi cần một thứ tự phân khúc nhất quán trong báo cáo, nhưng phát sinh bước sao chép và đổi kiểu. Lợi ích chính là cấu trúc và thứ tự đầu ra, không phải một bảo đảm về tốc độ. Cả hai phải giữ nguyên số tính được trong hàm, chỉ làm tròn khi trình bày.

:::

---

<span id="data-lab-05-05"></span>
### Bài tập 5: Phân nhóm theo số niêm yết và so sánh giá cùng lượt đánh giá

::: exercise Phân loại host và so sánh nhóm
Một host được quy ước là "chuyên nghiệp" nếu có số lượng niêm yết quản lý từ ngưỡng `nguong` trở lên (mặc định là 5 phòng).

Đây là nhãn phân nhóm của bài tập, không phải bằng chứng về nghề nghiệp hay chất lượng dịch vụ của chủ nhà. Tỷ lệ được tính trên các dòng chỗ ở, không phải trên số chủ nhà phân biệt. Số đánh giá cũng chưa phải số đặt phòng hay doanh thu.

Hãy viết hàm `pro_host_summary(df: pd.DataFrame, nguong: int = 5) -> dict` nhận vào bảng dữ liệu chứa ít nhất các cột `calculated_host_listings_count`, `price` và `number_of_reviews_ltm`. Hàm trả về một từ điển gồm đúng ba khóa sau:
1. `chuyen`: Đối tượng Series kiểu boolean biểu diễn điều kiện `calculated_host_listings_count >= nguong`, có cùng chỉ mục và thứ tự với bảng `df`.
2. `ty_le_chuyen`: Một số thực (`float`) thể hiện tỷ lệ số dòng thuộc về chủ nhà chuyên nghiệp trên tổng số dòng của bảng.
3. `so_sanh`: DataFrame phân nhóm theo biến boolean `chuyen` với hai cột được đặt tên:
   - `gia_trung_vi = ("price", "median")`
   - `review_nam_tb = ("number_of_reviews_ltm", "mean")`

Yêu cầu kỹ thuật: Tuyệt đối không được thêm cột mới vào DataFrame `df` truyền vào. Phải thực hiện phép nhóm trực tiếp thông qua đối tượng Series bên ngoài, ví dụ `df.groupby(chuyen)`.
:::

::: solution
#### Cách 1: Tạo mặt nạ đạt ngưỡng rồi nhóm bằng Series ngoài

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Bắt đầu lời giải

import pandas as pd


def pro_host_summary(df: pd.DataFrame, nguong: int = 5) -> dict:
    # 1. Tạo Series boolean độc lập từ cột số lượng niêm yết
    chuyen = df["calculated_host_listings_count"] >= nguong

    # 2. Tính tỷ lệ dòng thuộc chủ nhà chuyên nghiệp
    ty_le_chuyen = float(chuyen.mean())

    # 3. Nhóm trực tiếp bằng Series rời bên ngoài để bảo vệ bất biến của bảng gốc
    so_sanh = df.groupby(chuyen, observed=True).agg(
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"),
    )

    return {
        "chuyen": chuyen,
        "ty_le_chuyen": ty_le_chuyen,
        "so_sanh": so_sanh,
    }


# Gọi thử nghiệm hàm trên dữ liệu mẫu DEMO:
kq_host_c1 = pro_host_summary(DEMO, 5)
print("Tỷ lệ host chuyên nghiệp Cách 1:", kq_host_c1["ty_le_chuyen"])
print("Bảng so sánh Cách 1:")
print(kq_host_c1["so_sanh"])

# Kết thúc lời giải
```

##### Giải thích Cách 1

Phép so sánh `>= nguong` tạo một Series boolean có cùng chỉ mục với `df`. Mỗi `True` chỉ cho biết dòng chỗ ở thuộc chủ nhà có số niêm yết đạt ngưỡng quy ước. Nó không đếm số chủ nhà phân biệt và không xác nhận nghề nghiệp của họ.

`chuyen.mean()` lấy trung bình các cờ 0 và 1. Trên DEMO, sáu cờ đúng trong 12 dòng cho `0.5`. `float` chuyển kết quả sang số thực Python. `df.groupby(chuyen)` dùng Series ấy làm khóa ngoài, nên không cần thêm cột vào bảng nguồn. Nếu tạo khóa nhóm từ nơi khác, phải bảo đảm chỉ mục của nó khớp với `df`.

Trong nhóm `False`, có sáu dòng nhưng một giá bị khuyết. `median` dùng năm giá còn lại `18000`, `25000`, `30000`, `99999`, `150000`, nên trung vị bằng `30000`. Trung bình số đánh giá dùng cả sáu giá trị đã có, cho `5.5`. Nhóm `True` có tổng 78 lượt đánh giá trên sáu dòng, cho `13.0`.

##### Output Cách 1

| Khóa nhóm | `gia_trung_vi` | `review_nam_tb` |
|---|---|---|
| `False` | 30000.0 | 5.5 |
| `True` | 80000.0 | 13.0 |

`ty_le_chuyen = 0.5`, tương ứng 6 trong 12 dòng đạt ngưỡng 5.

#### Cách 2: Đặt tên rõ ràng cho Series khóa nhóm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Bắt đầu lời giải

import pandas as pd


def pro_host_summary(df: pd.DataFrame, nguong: int = 5) -> dict:
    # Tạo Series boolean và đặt tên tường minh cho trục phân nhóm
    chuyen = df["calculated_host_listings_count"].ge(nguong)
    chuyen.name = "chuyen"

    ty_le_chuyen = float(chuyen.mean())

    # Nhóm qua Series có tên giúp chỉ mục của bảng so sánh rõ ràng
    so_sanh = df.groupby(chuyen, observed=False).agg(
        gia_trung_vi=("price", "median"),
        review_nam_tb=("number_of_reviews_ltm", "mean"),
    )

    return {
        "chuyen": chuyen,
        "ty_le_chuyen": ty_le_chuyen,
        "so_sanh": so_sanh,
    }


# Gọi thử nghiệm hàm trên dữ liệu mẫu DEMO:
kq_host_c2 = pro_host_summary(DEMO, 5)
print("Tỷ lệ host chuyên nghiệp Cách 2:", kq_host_c2["ty_le_chuyen"])
print("Bảng so sánh Cách 2:")
print(kq_host_c2["so_sanh"])

# Kết thúc lời giải
```

##### Giải thích Cách 2

`.ge(nguong)` là dạng gọi phương thức của phép so sánh lớn hơn hoặc bằng. `chuyen.name = "chuyen"` đặt tên cho Series vừa tạo, không đổi tên hoặc dữ liệu của cột `calculated_host_listings_count` trong `df`.

Khi pandas dùng Series có tên làm khóa nhóm, chỉ mục của bảng tổng hợp mang tên `chuyen`. Điều này giúp người đọc phân biệt khóa phân loại với cột số niêm yết ban đầu. `observed` không tạo khác biệt trên Series boolean thông thường của ví dụ, vì đây không phải cột `category` có các mức chưa xuất hiện.

Từ điển đầu ra giữ cả mặt nạ từng dòng, tỷ lệ và bảng so sánh. Người gọi có thể dùng mặt nạ để lọc cùng bảng ban đầu hoặc dùng `so_sanh` để báo cáo mà không phải tính lại tiêu chí.

##### Output Cách 2

| Khóa nhóm | `gia_trung_vi` | `review_nam_tb` |
|---|---|---|
| `False` | 30000.0 | 5.5 |
| `True` | 80000.0 | 13.0 |

`ty_le_chuyen = 0.5`, tương ứng 6 trong 12 dòng đạt ngưỡng 5.

#### So sánh hai cách

Hai cách dùng cùng tiêu chí và cùng phép tổng hợp. Cách 2 làm tên trục nhóm dễ đọc hơn, còn lượng công việc tính toán gần tương tự Cách 1. Các chênh lệch ở bảng chỉ mô tả DEMO theo nhãn quy ước. Số đánh giá chưa phải số đặt phòng, doanh thu hoặc thước đo đầy đủ về hiệu quả vận hành.

:::

---

<span id="data-lab-05-06"></span>
### Bài tập 6: Gắn quy mô quận vào từng dòng bằng transform và lọc quận lớn

::: exercise Gắn quy mô quận và lọc bảng
Khác với phương thức `agg` làm thu gọn số dòng về số lượng nhóm, phương thức `transform` tính toán trên từng nhóm nhưng trả về kết quả có độ dài và chỉ mục hoàn toàn khớp với DataFrame ban đầu.

Hãy viết hàm `big_districts(df: pd.DataFrame, nguong: int = 300) -> dict` nhận vào bảng dữ liệu chứa ít nhất cột `neighbourhood` (tên quận) và cột `id`. Hàm trả về một từ điển gồm đúng hai khóa sau:
1. `n_quan`: Đối tượng Series chứa quy mô số lượng phòng của quận tương ứng với mỗi dòng, tính toán bằng `df.groupby("neighbourhood")["id"].transform("size")`, có cùng chỉ mục và thứ tự với `df`.
2. `df_dong`: Đối tượng DataFrame gồm các dòng thuộc về những quận có tổng số phòng đạt từ `nguong` trở lên. Giữ nguyên đúng các cột, chỉ mục và thứ tự dòng ban đầu của `df`.

Yêu cầu kỹ thuật: Không được thêm cột `n_quan` vào `df` cũng như vào `df_dong`.
:::

::: solution
#### Cách 1: Dùng transform để đưa số dòng của nhóm về từng hàng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Bắt đầu lời giải

import pandas as pd


def big_districts(df: pd.DataFrame, nguong: int = 300) -> dict:
    # 1. Tính quy mô quận cho từng dòng bằng transform("size")
    n_quan = df.groupby("neighbourhood")["id"].transform("size")

    # 2. Tạo mặt nạ lọc các dòng thuộc quận đạt quy mô yêu cầu
    mask = n_quan >= nguong

    # 3. Trích xuất bảng con và giữ nguyên cấu trúc cột ban đầu
    df_dong = df[mask].copy()

    return {
        "n_quan": n_quan,
        "df_dong": df_dong,
    }


# Gọi thử nghiệm hàm với ngưỡng 4 phòng trên dữ liệu DEMO:
kq_quan_c1 = big_districts(DEMO, 4)
print("Độ dài Series n_quan:", len(kq_quan_c1["n_quan"]))
print("Các giá trị n_quan mẫu:", list(kq_quan_c1["n_quan"]))
print("Số dòng thỏa mãn quy mô >= 4:", len(kq_quan_c1["df_dong"]))

# Kết thúc lời giải
```

##### Giải thích Cách 1

`groupby("neighbourhood")["id"]` chọn cột để tổng hợp trong từng quận. `transform("size")` đếm số dòng của nhóm rồi đặt số đếm ấy tại mọi vị trí thuộc nhóm. Kết quả vẫn dài 12 và đi cùng chỉ mục của DEMO. `size` đếm dòng, nên không phụ thuộc việc giá hay một ô `id` có bị khuyết hay không.

Mặt nạ `n_quan >= nguong` vì thế có thể dùng ngay để lọc `df`. Ở ngưỡng 4, cả năm dòng Santiago và bốn dòng Providencia được giữ. Hai dòng Ñuñoa và một dòng Vitacura không đạt ngưỡng. `.copy()` trả một bảng kết quả riêng với đúng các cột ban đầu.

Đừng nhầm `transform("size")` với `groupby.size()`. Lệnh thứ hai chỉ tạo một số đếm cho mỗi quận, nên không thể dùng trực tiếp như mặt nạ từng dòng của bảng 12 dòng.

##### Output Cách 1

| Các vị trí dòng | `n_quan` | Giữ với ngưỡng 4 |
|---|---|---|
| 0–4 | 5 | Có |
| 5–8 | 4 | Có |
| 9–10 | 2 | Không |
| 11 | 1 | Không |

Series `n_quan` là `[5, 5, 5, 5, 5, 4, 4, 4, 4, 2, 2, 1]`. `df_dong` có 9 dòng.

#### Cách 2: Chọn cột nhóm và lọc bằng loc

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Bắt đầu lời giải

import pandas as pd


def big_districts(df: pd.DataFrame, nguong: int = 300) -> dict:
    # Sử dụng chính cột phân nhóm để tính quy mô giúp tiết kiệm vùng nhớ
    n_quan = df.groupby("neighbourhood")["neighbourhood"].transform("size")

    # Lọc các dòng thỏa mãn ngưỡng mà không sinh thêm cột trong lược đồ bảng
    df_dong = df.loc[n_quan.ge(nguong)].copy()

    return {
        "n_quan": n_quan,
        "df_dong": df_dong,
    }


# Gọi thử nghiệm hàm với ngưỡng 4 phòng trên dữ liệu DEMO:
kq_quan_c2 = big_districts(DEMO, 4)
print("Số quận lớn thỏa mãn:", kq_quan_c2["df_dong"]["neighbourhood"].nunique())

# Kết thúc lời giải
```

##### Giải thích Cách 2

Trong phép `size`, dùng cột `neighbourhood` thay cột `id` vẫn đếm số dòng của cùng các nhóm. Cách viết này không cần cột `id` để thực hiện phép đếm, nhưng không tự chứng minh tiết kiệm bộ nhớ hơn.

`.ge(nguong)` tạo mặt nạ như toán tử `>=`. `df.loc[mặt_nạ]` chọn các dòng có cờ đúng và giữ nguyên cột, nhãn chỉ mục cùng thứ tự của chúng. Không có phép gán `n_quan` vào bảng nên lược đồ đầu ra không xuất hiện cột phụ.

Lời gọi `.nunique()` trong ví dụ đếm số tên quận phân biệt trong bảng đã lọc. Nó trả `2`, khác với `len(df_dong)` là `9`. Một số đếm đại diện cho nhóm, số kia đại diện cho dòng chỗ ở.

##### Output Cách 2

| Các vị trí dòng | `n_quan` | Giữ với ngưỡng 4 |
|---|---|---|
| 0–4 | 5 | Có |
| 5–8 | 4 | Có |
| 9–10 | 2 | Không |
| 11 | 1 | Không |

Lệnh in ở cuối Cách 2 trả `Số quận lớn thỏa mãn: 2`. Bảng con vẫn có 9 dòng.

#### So sánh hai cách

Hai cách đều dùng `transform` để tránh phải ghép một bảng số đếm trở lại bảng gốc. Cách 1 mở rõ biến mặt nạ, Cách 2 dùng `.loc` và phương thức so sánh. Ngưỡng 4 chỉ phục vụ DEMO. Ngưỡng 300 của bài thực tế là tiêu chí chọn nhóm đủ lớn, không phải bằng chứng rằng các quận nhỏ chứa dữ liệu sai.

:::

---

<span id="data-lab-05-07"></span>
### Bài tập 7: Bảng chéo tương tác phân khúc giá và kiểu host bằng pivot table

::: exercise Bảng chéo hai chiều pivot table
Để kiểm tra xem ưu thế về lượt đánh giá của chủ nhà chuyên nghiệp có đồng nhất trên mọi phân khúc giá hay không, chuyên viên cần xây dựng bảng tổng hợp chéo hai chiều.

Hãy viết hàm `segment_host_pivot(df: pd.DataFrame) -> pd.DataFrame` nhận vào bảng dữ liệu chứa ít nhất ba cột: `phan_khuc` (chuỗi hoặc khuyết), `chuyen` (boolean) và `number_of_reviews_ltm`. Hàm trả về một bảng xoay chiều (`pivot_table`) thỏa mãn các đặc tả:
1. `index="phan_khuc"`: Các hàng đại diện cho các phân khúc giá.
2. `columns="chuyen"`: Các cột đại diện cho trạng thái chủ nhà chuyên nghiệp (`False` và `True`).
3. `values="number_of_reviews_ltm"`: Cột số liệu cần tổng hợp.
4. `aggfunc="mean"`: Hàm tính giá trị trung bình cộng.

Yêu cầu kỹ thuật: Tổ hợp hàng và cột nào không có dữ liệu thực tế sẽ nhận giá trị `NaN` theo hành vi mặc định. Không làm tròn số liệu trong hàm và không làm biến đổi DataFrame `df` đầu vào.
:::

::: solution
#### Cách 1: Lập bảng chéo trực tiếp bằng pivot_table

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Bắt đầu lời giải

import pandas as pd


def segment_host_pivot(df: pd.DataFrame) -> pd.DataFrame:
    # Xây dựng bảng chéo hai chiều thông qua pivot_table
    bang_cheo = df.pivot_table(
        index="phan_khuc",
        columns="chuyen",
        values="number_of_reviews_ltm",
        aggfunc="mean",
    )
    return bang_cheo


# Chuẩn bị dữ liệu thử nghiệm có đủ cột phan_khuc và chuyen:
demo_pv = DEMO.copy()
demo_pv["chuyen"] = demo_pv["calculated_host_listings_count"] >= 5

# Gọi thử nghiệm hàm trên dữ liệu mẫu:
pv_c1 = segment_host_pivot(demo_pv)
print("Kết quả bảng chéo Cách 1:")
print(pv_c1.round(2))

# Kết thúc lời giải
```

##### Giải thích Cách 1

`index="phan_khuc"` đặt phân khúc trên hàng và `columns="chuyen"` đặt hai cờ chủ nhà trên cột. `values` chỉ cột số đánh giá cần tính. `aggfunc="mean"` tính trung bình cho mỗi cặp phân khúc và cờ, nên nhiều chỗ ở có cùng cặp khóa được thu thành một ô.

Để thử hàm, `demo_pv = DEMO.copy()` tạo bảng riêng rồi mới bổ sung cột `chuyen`. Bản thân `segment_host_pivot` không sửa bảng nhận vào. Ở ô `trung` × `True`, ba số đánh giá là 20, 15 và 30, có trung bình `65 / 3`, xấp xỉ `21.67` khi hiển thị.

Ô `re` × `True` là `NaN` vì DEMO không có dòng nào thuộc tổ hợp ấy. Điền 0 vào đây sẽ mang nghĩa có quan sát và trung bình bằng 0, khác với không có quan sát. `.round(2)` chỉ tạo bản hiển thị làm tròn, không đổi phép tính trong hàm.

##### Output Cách 1

| `phan_khuc` | `False` | `True` |
|---|---|---|
| `cao` | 1.00 | 4.33 |
| `re` | 6.00 | `NaN` |
| `trung` | 10.00 | 21.67 |

#### Cách 2: Nhóm hai khóa rồi đưa khóa thứ hai lên cột

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

demo_pv = DEMO.copy()
demo_pv["chuyen"] = demo_pv["calculated_host_listings_count"] >= 5

# Bắt đầu lời giải

import pandas as pd


def segment_host_pivot(df: pd.DataFrame) -> pd.DataFrame:
    # Thực hiện groupby trên hai khóa phân loại rồi chuyển trục bằng unstack
    bang_cheo = (
        df.groupby(["phan_khuc", "chuyen"], observed=False)["number_of_reviews_ltm"]
        .mean()
        .unstack(level="chuyen")
    )
    return bang_cheo


# Gọi thử nghiệm hàm trên dữ liệu mẫu:
pv_c2 = segment_host_pivot(demo_pv)
print("Kết quả bảng chéo Cách 2:")
print(pv_c2.round(2))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`groupby(["phan_khuc", "chuyen"])["number_of_reviews_ltm"].mean()` tạo một Series có chỉ mục hai cấp. Mỗi khóa chỉ mục lúc này là một cặp, chẳng hạn `("trung", True)`.

`.unstack(level="chuyen")` chuyển cấp `chuyen` từ chỉ mục lên cột. Các cặp chưa có quan sát trở thành ô khuyết trong bảng chữ nhật. Đây là bước thay đổi cách trình bày kết quả, không phải tính một trung bình khác.

Trong DEMO, `phan_khuc` là chuỗi nên tùy chọn `observed` không thêm các danh mục phân loại vắng mặt. Nếu chuyển khóa sang `category`, cần đặt rõ quy tắc giữ nhóm và xử lý hàng toàn khuyết trước khi đối chiếu với `pivot_table`.

##### Output Cách 2

| `phan_khuc` | `False` | `True` |
|---|---|---|
| `cao` | 1.00 | 4.33 |
| `re` | 6.00 | `NaN` |
| `trung` | 10.00 | 21.67 |

#### So sánh hai cách

`pivot_table` diễn đạt ngắn gọn mục tiêu tạo bảng chéo. `groupby` rồi `unstack` mở rõ hai bước tổng hợp và đổi trục, hữu ích khi cần nhiều phép tổng hợp khác nhau. Cả hai bảng mô tả lượt đánh giá trong DEMO. Chênh lệch giữa hai cột không xác lập quan hệ nhân quả hay chất lượng dịch vụ.

:::

---

<span id="data-lab-05-08"></span>
### Bài tập 8: Tìm phòng có giá niêm yết cao nhất trong từng quận bằng transform

::: exercise Tìm phòng đắt nhất theo quận
Trong các bài toán định vị phân khúc bất động sản cao cấp, chuyên viên cần lọc ra các phòng giữ mức giá niêm yết kỷ lục trong từng quận lớn (`df_dong` từ Bài tập 6).

Hãy viết hàm `top_price_by_district(df: pd.DataFrame) -> pd.DataFrame` nhận vào bảng dữ liệu chứa ít nhất các cột `id`, `name`, `neighbourhood` và `price`. Hàm trả về một DataFrame chứa các dòng có giá phòng đạt mức tối đa của quận tương ứng.

Yêu cầu kỹ thuật:
1. Sử dụng phương thức `transform("max")` trên cột `price` theo nhóm `neighbourhood` để tìm mức giá trần của quận.
2. Nếu trong một quận có nhiều phòng cùng đạt mức giá tối đa ngang nhau, giữ lại toàn bộ các phòng đó. Bỏ qua các dòng có giá trị khuyết `NaN`.
:::

::: solution
#### Cách 1: So sánh từng giá với giá lớn nhất của quận

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

# Bắt đầu lời giải

import pandas as pd


def top_price_by_district(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Tính giá tối đa của từng quận và phát tán về từng dòng
    gia_max_quan = df.groupby("neighbourhood")["price"].transform("max")

    # 2. Tạo mặt nạ boolean xác định các phòng đạt mức giá kỷ lục
    mask = df["price"] == gia_max_quan

    # 3. Lọc và trả về các dòng thỏa mãn
    return df[mask].copy()


# Chuẩn bị dữ liệu hai quận lớn từ bảng DEMO:
df_quan_lon = DEMO[DEMO["neighbourhood"].isin(["Santiago", "Providencia"])].copy()

# Gọi thử nghiệm hàm:
kq_top_c1 = top_price_by_district(df_quan_lon)
print("Kết quả phòng đắt nhất Cách 1:")
print(kq_top_c1[["id", "name", "neighbourhood", "price"]])

# Kết thúc lời giải
```

##### Giải thích Cách 1

`transform("max")` tính giá lớn nhất theo quận rồi đưa giá ấy về từng dòng. Trong Santiago, mọi dòng được so với `120000`. Trong Providencia, mọi dòng được so với `100000`. Phép `==` vì thế trả một mặt nạ đúng tại các chỗ ở đạt mức lớn nhất của chính quận mình.

Phép so sánh được thực hiện trên từng dòng, nên nếu hai chỗ ở cùng đạt mức lớn nhất thì cả hai cờ đều đúng. Dùng `idxmax` chỉ lấy một vị trí sẽ không đáp ứng yêu cầu giữ tất cả trường hợp hòa giá.

Các phép cực đại bỏ qua giá khuyết khi nhóm còn giá hợp lệ. Dòng có giá `NaN` không bằng mức cực đại, nên bị loại. Nếu toàn bộ giá của một quận đều khuyết, cách này không trả chỗ ở nào của quận đó. Kết quả `.copy()` giữ các cột và chỉ mục của những dòng được chọn.

##### Output Cách 1

| Chỉ mục gốc | `id` | `neighbourhood` | `price` |
|---|---|---|---|
| 2 | 203 | Santiago | 120000.0 |
| 7 | 208 | Providencia | 100000.0 |

Cách 1 còn in cột `name`, lần lượt là `Loft Parque Forestal` và `Loft Pedro de Valdivia`.

#### Cách 2: Loại giá khuyết trước rồi lọc bằng eq

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

df_quan_lon = DEMO.loc[DEMO["neighbourhood"].isin(["Santiago", "Providencia"])].copy()

# Bắt đầu lời giải

import pandas as pd


def top_price_by_district(df: pd.DataFrame) -> pd.DataFrame:
    # Lọc bỏ giá trị khuyết trước khi xác định mức giá cao nhất
    df_hop_le = df.dropna(subset=["price"])
    gia_max = df_hop_le.groupby("neighbourhood")["price"].transform("max")

    return df_hop_le.loc[df_hop_le["price"].eq(gia_max)].copy()


# Gọi thử nghiệm hàm:
kq_top_c2 = top_price_by_district(df_quan_lon)
print("Kết quả phòng đắt nhất Cách 2:")
print(kq_top_c2[["id", "neighbourhood", "price"]])

# Kết thúc lời giải
```

##### Giải thích Cách 2

`dropna(subset=["price"])` tạo bảng chỉ gồm các dòng có giá. Chỉ cột `price` tham gia điều kiện loại dòng, nên một ô khuyết ở cột khác không khiến chỗ ở bị loại khỏi phép tìm giá lớn nhất.

Sau bước đó, phép nhóm và `transform("max")` giữ cùng cơ chế với Cách 1. `.eq(gia_max)` là dạng phương thức của phép so sánh bằng và vẫn căn chỉnh theo chỉ mục. `.loc` lấy mọi dòng thỏa điều kiện, bao gồm tất cả trường hợp hòa giá.

Bản in ở cuối chọn ba cột `id`, `neighbourhood`, `price` để dễ xem. Hàm thật sự vẫn trả toàn bộ các cột của các dòng được chọn, nên việc không in tên ở ví dụ này không làm mất cột `name` trong giá trị trả về.

##### Output Cách 2

| Chỉ mục gốc | `id` | `neighbourhood` | `price` |
|---|---|---|---|
| 2 | 203 | Santiago | 120000.0 |
| 7 | 208 | Providencia | 100000.0 |

#### So sánh hai cách

Cách 1 ngắn và đủ cho quy tắc giá khuyết của đề. Cách 2 thể hiện rõ việc loại dòng chưa có giá, nhưng phải tạo thêm bảng trung gian. Tỷ lệ khuyết có thể ảnh hưởng hiệu năng, nên cần đo trước khi gọi một cách là nhanh hơn. Hai cách cùng giữ được các chỗ ở đồng giá cao nhất.

:::

---

<span id="data-lab-05-09"></span>
### Bài tập 9: Phân tích cơ cấu phân khúc giá theo từng quận lớn

::: exercise Cơ cấu phân khúc giá theo quận
Để đánh giá định vị thị trường của từng quận, ban quản lý cần nắm rõ tỷ trọng phần trăm của ba phân khúc giá (`re`, `trung`, `cao`) trong các chỗ ở đã xác định được phân khúc của từng quận lớn.

Hãy viết hàm `segment_share_by_district(df: pd.DataFrame) -> pd.DataFrame` nhận vào bảng dữ liệu chứa ít nhất các cột `neighbourhood` và `phan_khuc`. Hàm trả về một DataFrame biểu diễn tỷ trọng cơ cấu:
1. Chỉ mục dòng: Tên các quận lớn (`neighbourhood`).
2. Các cột: Đầy đủ ba phân khúc theo đúng thứ tự `["re", "trung", "cao"]`.
3. Giá trị ô: Tỷ trọng số phòng thuộc phân khúc đó trong các dòng của quận đã xác định được phân khúc (tổng mỗi hàng bằng 1,0 tương đương 100%). Nếu một phân khúc không có phòng nào trong quận, giá trị ô nhận 0,0. Những dòng khuyết phân khúc không tham gia mẫu số này. Khi diễn giải cơ cấu toàn bộ nguồn cung, cần báo riêng tỷ lệ khuyết phân khúc.
:::

::: solution
#### Cách 1: Tạo bảng tần suất và chuẩn hóa theo hàng bằng crosstab

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

df_quan_lon = DEMO.loc[DEMO["neighbourhood"].isin(["Santiago", "Providencia"])].copy()

# Bắt đầu lời giải

import pandas as pd


def segment_share_by_district(df: pd.DataFrame) -> pd.DataFrame:
    # 1. Tính bảng tần suất chéo và chuẩn hóa theo hàng
    bang_ty_trong = pd.crosstab(
        df["neighbourhood"],
        df["phan_khuc"],
        normalize="index",
    )

    # 2. Bảo đảm đủ ba cột phân khúc ngay cả khi có phân khúc vắng mặt
    for col in ["re", "trung", "cao"]:
        if col not in bang_ty_trong.columns:
            bang_ty_trong[col] = 0.0

    # 3. Sắp xếp lại thứ tự cột theo đúng chuẩn kinh tế
    return bang_ty_trong[["re", "trung", "cao"]]


# Gọi thử nghiệm hàm trên tập các quận lớn:
share_c1 = segment_share_by_district(df_quan_lon)
print("Cơ cấu phân khúc Cách 1:")
print(share_c1.round(3))

# Kết thúc lời giải
```

##### Giải thích Cách 1

`pd.crosstab` đếm các cặp quận và phân khúc. `normalize="index"` chia từng ô cho tổng số đếm của hàng, nên kết quả là tỷ lệ từ 0 đến 1. Trong Providencia, bốn dòng chia thành 1 rẻ, 2 trung, 1 cao, cho hàng `0.25`, `0.50`, `0.25`.

Vòng lặp chỉ bổ sung một cột phân khúc nếu cột ấy chưa tồn tại trong toàn bộ bảng chéo. Gán `0.0` biểu thị không có quan sát thuộc phân khúc đó. Việc chọn lại danh sách cột ở dòng `return` bảo đảm thứ tự luôn là `re`, `trung`, `cao`.

Cần đọc đúng mẫu số khi có phân khúc khuyết. `crosstab` trong đoạn mã này bỏ dòng thiếu phân khúc. Santiago có năm dòng nhưng chỉ bốn dòng xác định được dải giá, nên hàng dưới đây đang chuẩn hóa trên bốn dòng đó. Nếu yêu cầu tỷ trọng trên toàn bộ năm dòng, ba tỷ trọng là `0.2`, `0.4`, `0.2` và còn `0.2` khuyết phân khúc. Không được diễn giải hai mẫu số này như nhau.

##### Output Cách 1

| `neighbourhood` | `re` | `trung` | `cao` |
|---|---|---|---|
| Providencia | 0.25 | 0.50 | 0.25 |
| Santiago | 0.25 | 0.50 | 0.25 |

#### Cách 2: Đếm từng cặp khóa rồi chia theo tổng của hàng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
        "name": [
            "Depto Central",
            "Pieza Bellas Artes",
            "Loft Parque Forestal",
            "Estudio sin precio",
            "Habitacion Santa Lucia",
            "Depto Providencia",
            "Suite Costanera",
            "Loft Pedro de Valdivia",
            "Habitacion Manuel Montt",
            "Casa Nunoa",
            "Loft Plaza Egaña",
            "Villa Vitacura",
        ],
        "neighbourhood": ["Santiago"] * 5
        + ["Providencia"] * 4
        + ["Ñuñoa"] * 2
        + ["Vitacura"],
        "price": [
            25000.0,
            45000.0,
            120000.0,
            np.nan,
            60000.0,
            30000.0,
            99999.0,
            100000.0,
            18000.0,
            55000.0,
            150000.0,
            210000.0,
        ],
        "number_of_reviews_ltm": [10, 20, 3, 0, 15, 8, 12, 6, 2, 30, 1, 4],
        "calculated_host_listings_count": [1, 6, 12, 2, 5, 1, 1, 7, 3, 9, 1, 20],
    }
)


def phan_khuc_gia(gia):
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    return "cao"


DEMO["phan_khuc"] = DEMO["price"].map(phan_khuc_gia)

df_quan_lon = DEMO.loc[DEMO["neighbourhood"].isin(["Santiago", "Providencia"])].copy()

# Bắt đầu lời giải

import pandas as pd


def segment_share_by_district(df: pd.DataFrame) -> pd.DataFrame:
    # Đếm số lượng phòng theo từng cặp quận và phân khúc
    dem = (
        df.groupby(["neighbourhood", "phan_khuc"], observed=False)
        .size()
        .unstack(fill_value=0)
    )

    # Chuẩn hóa tỷ trọng bằng cách chia cho tổng số dòng của từng quận
    tong_hang = dem.sum(axis=1)
    bang_ty_trong = dem.div(tong_hang, axis=0)

    # Bổ sung các cột phân khúc còn thiếu nếu có
    for col in ["re", "trung", "cao"]:
        if col not in bang_ty_trong.columns:
            bang_ty_trong[col] = 0.0

    return bang_ty_trong[["re", "trung", "cao"]]


# Gọi thử nghiệm hàm trên tập các quận lớn:
share_c2 = segment_share_by_district(df_quan_lon)
print("Cơ cấu phân khúc Cách 2:")
print(share_c2.round(3))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`.groupby(["neighbourhood", "phan_khuc"]).size()` tạo số đếm cho từng cặp khóa. `.unstack(fill_value=0)` đưa phân khúc lên cột và điền 0 cho tổ hợp không có dòng. `fill_value=0` ở đây điền số đếm vắng mặt, chưa phải điền mức giá hoặc số đánh giá bị thiếu.

`dem.sum(axis=1)` cộng theo chiều ngang để lấy tổng số đếm của từng quận. `dem.div(tong_hang, axis=0)` căn chỉnh mẫu số theo chỉ mục quận rồi chia mọi ô trong cùng hàng cho mẫu số tương ứng. Nếu bỏ `axis=0`, pandas có thể căn Series mẫu số theo cột, không đúng mục đích.

Phép nhóm mặc định cũng bỏ khóa phân khúc bị khuyết. Vì vậy bảng dưới đây có cùng mẫu số đã biết như Cách 1. Với dữ liệu ngoài DEMO, phải quyết định giữ một nhóm khuyết, loại khỏi mẫu số hay báo tỷ lệ khuyết riêng trước khi khẳng định tổng mỗi hàng bằng 1.

##### Output Cách 2

| `neighbourhood` | `re` | `trung` | `cao` |
|---|---|---|---|
| Providencia | 0.25 | 0.50 | 0.25 |
| Santiago | 0.25 | 0.50 | 0.25 |

#### So sánh hai cách

Cách 1 chuyên dùng cho bảng chéo tỷ trọng. Cách 2 cho thấy rõ số đếm, tổng hàng và phép chia, thuận tiện để kiểm tra mẫu số hoặc bổ sung trọng số. Hai cách hiện cùng xử lý dòng khuyết bằng cách loại khỏi nhóm. Cần đối chiếu yêu cầu về mẫu số toàn quận trước khi dùng bảng trong báo cáo.

:::
