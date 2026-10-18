## Lab 06: Dữ liệu ngoài, đọc tệp chọn lọc, lưu trữ Parquet và truy vấn DuckDB

Một tệp có 90 cột nhưng bài toán chỉ cần năm cột. Ta sẽ đọc đúng phần cần dùng, lưu và đọc lại kết quả, ghép dữ liệu thời tiết theo ngày rồi kiểm tra bằng SQL. Các ví dụ nhỏ chạy độc lập để quan sát kiểu dữ liệu và kết quả từng bước.

## Bối cảnh và snapshot dữ liệu tham chiếu

Có thể thử cùng quy trình trên snapshot Inside Airbnb của Santiago ngày 29/06/2026. Cần phân biệt bảng rút gọn với bảng đầy đủ khi chọn tệp và cột:
- **Địa chỉ kho dữ liệu gốc**: `https://data.insideairbnb.com/chile/rm/santiago/`
- **Phiên bản snapshot tham chiếu**: Bản lưu trữ ngày 29 tháng 06 năm 2026 (`2026-06-29/visualisations/listings.csv`, `visualisations/reviews.csv`, và bảng đầy đủ 90 cột `data/listings.csv.gz`).
- **Nguồn dữ liệu thời tiết lịch sử**: Dịch vụ Open-Meteo Historical Weather API tại địa chỉ `https://archive-api.open-meteo.com/v1/archive`.

> [!NOTE]
> **Quy ước dữ liệu mẫu trong Lab 06**: Toàn bộ các bảng số liệu mẫu được khởi tạo trong tài liệu này là dữ liệu giả lập quy mô nhỏ. Mục đích của dữ liệu nhỏ là giúp người học đối chiếu từng bước tính toán, theo dõi sự thay đổi kiểu dữ liệu và kiểm tra độ chính xác của các câu lệnh SQL một cách độc lập mà không phụ thuộc vào kết nối mạng ngoài. Tuyệt đối không suy diễn các con số mẫu nhỏ này thành kết luận đại diện cho toàn bộ thị trường lưu trú thực tế tại Santiago.

### Khởi tạo dữ liệu dùng chung

Mọi bài tập sử dụng các cấu trúc dữ liệu mẫu giả lập đại diện cho tệp đánh giá, tệp chỗ ở đầy đủ và phản hồi thời tiết lịch sử:

```python
import json
import os
import tempfile
from pathlib import Path
import numpy as np
import pandas as pd
import duckdb

# Kích hoạt hành vi Copy-on-Write của pandas
if pd.__version__.startswith("2."):
    pd.set_option("mode.copy_on_write", True)

# 1. Dữ liệu đánh giá giả lập: 51 dòng phân bổ qua các năm
_danh_sach_ngay = []
for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong
_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

# 2. Dữ liệu chỗ ở đầy đủ giả lập: 6 chỗ ở với thông tin giá và ngày đánh giá đầu tiên
DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

# 3. Phản hồi thời tiết lịch sử mẫu: 10 ngày đầu tháng 01 năm 2025 tại Santiago
DEMO_WEATHER = {
    "latitude": -33.45,
    "longitude": -70.66,
    "timezone": "America/Santiago",
    "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
    "daily": {
        "time": [f"2025-01-{d:02d}" for d in range(1, 11)],
        "temperature_2m_max": [
            31.4,
            33.1,
            29.1,
            32.8,
            30.2,
            30.0,
            28.5,
            31.8,
            30.9,
            27.6,
        ],
    },
}

# Ghi sẵn các tệp vào thư mục hiện hành để phục vụ thực thi độc lập
DEMO_REVIEWS.to_csv("reviews.csv", index=False)
DEMO_LISTINGS_FULL[["id", "name", "room_type"]].to_csv("listings.csv", index=False)
DEMO_LISTINGS_FULL.to_csv("listings_full.csv", index=False)
Path("weather.json").write_text(
    json.dumps(DEMO_WEATHER, ensure_ascii=False, indent=2), encoding="utf-8"
)
```

---

## Bài 1: Đọc tệp bảng lớn có chọn lọc với tham số cột và ngày giờ

<span id="data-lab-06-01"></span>

::: exercise
**Mục tiêu**: Nắm vững phương pháp tối ưu hóa bộ nhớ khi nạp các tệp dữ liệu lớn bằng cách chỉ chọn đọc các cột cần thiết và chuyển đổi kiểu ngày giờ ngay trong quá trình nạp.

**Dữ liệu đầu vào**:
- Tệp dữ liệu chỗ ở đầy đủ `listings_full.csv` chứa nhiều cột thông tin.
- Danh sách các cột cần lấy: `["id", "room_type", "price", "first_review", "number_of_reviews"]`.
- Danh sách các cột định dạng thời gian cần chuyển đổi sang `datetime64`: `["first_review"]`.

**Thao tác yêu cầu**:
1. Triển khai hàm `read_selected(path, columns: list, date_columns: list) -> pd.DataFrame` sử dụng `pd.read_csv` với hai đối số trọng tâm: `usecols` để chỉ định danh sách cột và `parse_dates` để ép kiểu thời gian.
2. Đảm bảo các dòng có ô ngày trống được chuyển thành giá trị `NaT` thay vì chuỗi rỗng hoặc lỗi cú pháp.
3. Đo lường sự khác biệt về dung lượng bộ nhớ sử dụng giữa phương pháp đọc toàn bộ bảng và phương pháp chỉ đọc các cột được chọn.

**Trường hợp biên cần chú ý**:
- Không nạp toàn bộ bảng vào bộ nhớ rồi mới dùng cú pháp chọn lọc cột trên đối tượng DataFrame.
- Danh sách `date_columns` có thể rỗng hoặc là tập con của `columns`.
:::

::: solution
#### Cách 1: Đọc đúng cột cần dùng bằng read_csv

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL.to_csv("listings_full.csv", index=False)

# Bắt đầu lời giải


def read_selected(path, columns: list, date_columns: list) -> pd.DataFrame:
    # Đọc tệp có chọn lọc cột và chuyển đổi ngày giờ
    df = pd.read_csv(
        path, usecols=columns, parse_dates=date_columns if date_columns else False
    )
    return df


# Thực thi mẫu với tệp listings_full.csv
cot_can_doc = ["id", "room_type", "price", "first_review", "number_of_reviews"]
cot_ngay = ["first_review"]
bang_chon_loc = read_selected("listings_full.csv", cot_can_doc, cot_ngay)
print("Kích thước bảng:", bang_chon_loc.shape)
print("Kiểu dữ liệu first_review:", bang_chon_loc["first_review"].dtype)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`usecols=columns` yêu cầu trình đọc chỉ dựng các cột cần dùng trong DataFrame. Đọc CSV vẫn phải quét nội dung tệp, nên không thể suy ra chọn năm trong 90 cột sẽ chỉ đọc năm phần chín mươi số byte. Lợi ích trực tiếp là giảm số cột được lưu và xử lý trong bộ nhớ.

`parse_dates=date_columns` đề nghị pandas phân tích các cột ngày. Dữ liệu ngày ISO hợp lệ trong ví dụ được chuyển sang kiểu thời gian, còn ô ngày trống thành `NaT`. Khi danh sách ngày rỗng, mã truyền `False` để không yêu cầu chuyển đổi ngày. Với chuỗi ngày lỗi ngoài miền của bài, cần kiểm tra kiểu sau khi đọc thay vì mặc định cho rằng mọi chuỗi đã được chuyển thành công.

`.shape` trả cặp số dòng và số cột, nên `(6, 5)` xác nhận giữ đủ sáu chỗ ở nhưng chỉ lấy năm cột. Kiểu thời gian có thể là `datetime64[us]` hoặc `datetime64[ns]` tùy phiên bản và độ phân giải. Trong môi trường đã chạy kiểm tra, cột `first_review` là `datetime64[us]`, không phải số thực.

##### Output Cách 1

| `id` | `room_type` | `price` | `first_review` | `number_of_reviews` |
|---|---|---|---|---|
| 11 | Entire home/apt | `$45,647.00` | 2023-03-15 | 14 |
| 12 | Private room | `$18,500.00` | 2023-08-02 | 9 |
| 13 | Entire home/apt | `$1,120,000.00` | 2024-02-11 | 8 |
| 14 | Entire home/apt | `NaN` | 2023-11-20 | 4 |
| 15 | Entire home/apt | `$59,000.00` | 2025-01-02 | 6 |
| 16 | Private room | `$25,990.50` | `NaT` | 0 |

Bản in có `Kích thước bảng: (6, 5)` và `Kiểu dữ liệu first_review: datetime64[us]` trong môi trường kiểm tra.

#### Cách 2: Khai báo thêm kiểu dữ liệu khi đọc

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import pandas as pd

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL.to_csv("listings_full.csv", index=False)

cot_can_doc = ["id", "room_type", "price", "first_review", "number_of_reviews"]

cot_ngay = ["first_review"]

# Bắt đầu lời giải


def read_selected_v2(
    path, columns: list, date_columns: list, dtypes: dict = None
) -> pd.DataFrame:
    tep_nguon = Path(path)
    if not tep_nguon.exists():
        raise FileNotFoundError(f"Không tìm thấy tệp dữ liệu tại: {path}")

    # Xác định các cột ngày hợp lệ nằm trong danh sách cột yêu cầu
    cac_cot_ngay_hop_le = (
        [c for c in date_columns if c in columns] if date_columns else False
    )

    # Đọc dữ liệu với cấu hình kiểu tường minh
    ket_qua = pd.read_csv(
        tep_nguon, usecols=columns, parse_dates=cac_cot_ngay_hop_le, dtype=dtypes
    )
    return ket_qua


# Thực thi mẫu với việc cố định kiểu chuỗi cho mã định danh
bang_chon_loc_v2 = read_selected_v2(
    "listings_full.csv", cot_can_doc, cot_ngay, dtypes={"id": "string"}
)
print("Kiểu cột id sau khi ép chuỗi:", bang_chon_loc_v2["id"].dtype)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`Path(path)` biểu diễn đường dẫn thành đối tượng có các thao tác tệp. `.exists()` kiểm tra sự tồn tại trước khi đọc. Việc kiểm tra này giúp báo lỗi rõ vị trí tệp, còn pandas vẫn có thể phát sinh lỗi nếu tệp đổi trạng thái sau đó hoặc không thể đọc được.

`dtypes={"id": "string"}` đưa mã định danh về kiểu chuỗi ngay lúc đọc, hữu ích khi mã có số 0 ở đầu. Bảng vẫn hiển thị `11`, `12` nhưng các giá trị này là chuỗi, không còn dùng như số để cộng. Hàm lọc `date_columns` theo `columns` để chỉ phân tích những cột ngày có được chọn.

`dtype` không làm dữ liệu nhỏ hơn trong mọi trường hợp. Chọn kiểu dựa vào ý nghĩa cột và phạm vi giá trị, sau đó dùng `.memory_usage(deep=True)` để đo khi cần. Tham số `deep=True` giúp tính thêm bộ nhớ nội dung của dữ liệu chuỗi được lưu dưới dạng đối tượng, thay vì chỉ đếm vùng chứa tham chiếu.

##### Output Cách 2

| `id` | `room_type` | `price` | `first_review` | `number_of_reviews` |
|---|---|---|---|---|
| 11 | Entire home/apt | `$45,647.00` | 2023-03-15 | 14 |
| 12 | Private room | `$18,500.00` | 2023-08-02 | 9 |
| 13 | Entire home/apt | `$1,120,000.00` | 2024-02-11 | 8 |
| 14 | Entire home/apt | `NaN` | 2023-11-20 | 4 |
| 15 | Entire home/apt | `$59,000.00` | 2025-01-02 | 6 |
| 16 | Private room | `$25,990.50` | `NaT` | 0 |

Dòng kiểm tra riêng của Cách 2 là `Kiểu cột id sau khi ép chuỗi: string`. Cột id trong bảng trên được giữ ở kiểu chuỗi.

#### So sánh hai cách

Cách 1 đủ khi kiểu tự suy diễn phù hợp. Cách 2 bổ sung kiểm tra đường dẫn và cấu hình kiểu, thích hợp với quy trình cần lược đồ ổn định. Muốn so sánh giá trị hai bảng phải nhớ cột id đã có chủ ý khác kiểu. Dung lượng bộ nhớ cần được đo trên cùng dữ liệu và cùng cấu hình, không suy ra từ số cột đơn thuần.

:::

---

## Bài 2: Làm sạch cột giá tiền dạng chuỗi và chuẩn hóa kiểu số thực

<span id="data-lab-06-02"></span>

::: exercise
**Mục tiêu**: Xử lý chuỗi văn bản biểu diễn tiền tệ chứa ký hiệu đơn vị và dấu phân cách hàng nghìn, chuyển đổi thành số thực có thể tính toán toán học.

**Dữ liệu đầu vào**: Cột giá `price` dưới dạng một Series chuỗi: `["$45,647.00", "$18,500.00", "$1,120,000.00", None, "$59,000.00", "$25,990.50"]`.

**Thao tác yêu cầu**:
1. Triển khai hàm `clean_price(prices: pd.Series) -> pd.Series` để loại bỏ ký hiệu `$` và dấu phẩy `,`, sau đó chuyển đổi thành kiểu `float64`.
2. Bảo toàn các giá trị khuyết thiếu ban đầu dưới dạng `NaN` trong kết quả đầu ra.
3. Không làm thay đổi đối tượng Series ban đầu được truyền vào hàm.

**Trường hợp biên cần chú ý**:
- Nếu sử dụng `str.replace("$", "", regex=True)`, trong cú pháp biểu thức chính quy ký tự `$` có ý nghĩa là vị trí kết thúc chuỗi. Khi đó ký hiệu tiền tệ không bị xóa mà vị trí cuối chuỗi bị thay thế. Bắt buộc phải đặt `regex=False` khi thay thế ký tự thuần túy.
:::

::: solution
#### Cách 1: Xóa hai ký tự đã biết rồi ép sang float

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

# Bắt đầu lời giải


def clean_price(prices: pd.Series) -> pd.Series:
    # Bước 1: Loại bỏ ký hiệu đô la với regex=False
    s1 = prices.str.replace("$", "", regex=False)
    # Bước 2: Loại bỏ dấu phẩy phân tách hàng nghìn
    s2 = s1.str.replace(",", "", regex=False)
    # Bước 3: Chuyển đổi sang kiểu số thực float
    ket_qua = s2.astype(float)
    return ket_qua


# Thực thi mẫu trên cột giá của bảng chỗ ở
gia_sach = clean_price(DEMO_LISTINGS_FULL["price"])
print("Giá sau làm sạch:")
print(gia_sach.tolist())
print("Trung vị giá:", gia_sach.median())

# Kết thúc lời giải
```

##### Giải thích Cách 1

Hai lần `.str.replace(..., regex=False)` lần lượt xóa dấu `$` và dấu phẩy khỏi từng chuỗi. Cờ `regex=False` yêu cầu so khớp nguyên văn. Nếu dùng regex cho `$` mà không thoát ký tự, nó biểu diễn vị trí kết thúc chuỗi và không còn nghĩa ký hiệu tiền.

Sau bước này, chuỗi `$45,647.00` thành `45647.00`. `.astype(float)` phân tích chuỗi số thành số thực, giữ ô khuyết dưới dạng `NaN`. Nếu còn văn bản như `liên hệ`, cách này phát sinh lỗi thay vì tự đoán một giá trị. Đó là lựa chọn phù hợp khi định dạng đầu vào đã được quy định chặt.

`.median()` bỏ ô khuyết và lấy trung vị năm giá đã đọc được. Danh sách tăng dần là `18500`, `25990.5`, `45647`, `59000`, `1120000`, nên giá ở giữa bằng `45647.0`. Đây là trung vị mẫu sáu dòng, không phải giá đại diện cho cả thành phố.

##### Output Cách 1

| Vị trí | Chuỗi ban đầu | Giá số |
|---|---|---|
| 0 | `$45,647.00` | 45647.0 |
| 1 | `$18,500.00` | 18500.0 |
| 2 | `$1,120,000.00` | 1120000.0 |
| 3 | `None` | `NaN` |
| 4 | `$59,000.00` | 59000.0 |
| 5 | `$25,990.50` | 25990.5 |

Dòng in trung vị trả `45647.0`.

#### Cách 2: Gom ký tự cần xóa bằng regex và dùng to_numeric

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)


def clean_price(prices: pd.Series) -> pd.Series:
    # Bước 1: Loại bỏ ký hiệu đô la với regex=False
    s1 = prices.str.replace("$", "", regex=False)
    # Bước 2: Loại bỏ dấu phẩy phân tách hàng nghìn
    s2 = s1.str.replace(",", "", regex=False)
    # Bước 3: Chuyển đổi sang kiểu số thực float
    ket_qua = s2.astype(float)
    return ket_qua


gia_sach = clean_price(DEMO_LISTINGS_FULL["price"])

# Bắt đầu lời giải


def clean_price_v2(prices: pd.Series) -> pd.Series:
    # Loại bỏ đồng thời cả $ và dấu phẩy bằng một biểu thức chính quy gọn gàng
    chuoi_sach = prices.str.replace(r"[$,]", "", regex=True)
    # Chuyển đổi an toàn sang kiểu số thực
    ket_qua = pd.to_numeric(chuoi_sach, errors="coerce").astype(float)
    return ket_qua


# Thực thi mẫu phương pháp thứ hai
gia_sach_v2 = clean_price_v2(DEMO_LISTINGS_FULL["price"])
print(
    "Kiểm tra tính trùng khớp hai cách:",
    np.allclose(gia_sach.dropna(), gia_sach_v2.dropna()),
)

# Kết thúc lời giải
```

##### Giải thích Cách 2

Mẫu `r"[$,]"` là một nhóm ký tự, khớp một dấu đô la hoặc một dấu phẩy. Trong nhóm này, `$` được hiểu là ký tự cần xóa. `regex=True` yêu cầu pandas dùng mẫu đó để thực hiện thay thế. Một lời gọi ngắn hơn chưa chứng minh thời gian chạy ít hơn hai lần thay thế nguyên văn, vì regex cũng có chi phí xử lý.

`pd.to_numeric(..., errors="coerce")` chuyển chuỗi số thành số. Chuỗi không chuyển được sẽ trở thành giá trị khuyết. `.astype(float)` chuẩn hóa kiểu trả về theo đề. Khi làm dữ liệu thật, nên giữ thêm cờ chỉ những dòng vốn có dữ liệu nhưng chuyển đổi thất bại, để không nhầm lỗi định dạng với thiếu dữ liệu từ nguồn.

Lệnh `np.allclose` trong ví dụ so các giá hợp lệ của hai kết quả và trả `True`. Đây là kiểm tra số có dung sai, chưa kiểm tra đầy đủ chỉ mục và vị trí khuyết. Muốn xác nhận cả cấu trúc Series, cần đối chiếu thêm chỉ mục cùng mặt nạ `.isna()`.

##### Output Cách 2

| Vị trí | Chuỗi ban đầu | Giá số |
|---|---|---|
| 0 | `$45,647.00` | 45647.0 |
| 1 | `$18,500.00` | 18500.0 |
| 2 | `$1,120,000.00` | 1120000.0 |
| 3 | `None` | `NaN` |
| 4 | `$59,000.00` | 59000.0 |
| 5 | `$25,990.50` | 25990.5 |

Lệnh kiểm tra trong ví dụ in `Kiểm tra tính trùng khớp hai cách: True`.

#### So sánh hai cách

Cách 1 dừng khi gặp chuỗi số sai, giúp lộ rõ đầu vào không đúng quy định. Cách 2 cho phép tiếp tục xử lý nhưng phải theo dõi số giá trị bị chuyển thành khuyết. Cả hai đúng trên sáu chuỗi của bài. Chọn quy tắc báo lỗi theo yêu cầu dữ liệu trước khi cân nhắc tốc độ.

:::

---

## Bài 3: So sánh định dạng CSV và Parquet về kích thước tệp và bảo toàn kiểu dữ liệu

<span id="data-lab-06-03"></span>

::: exercise
**Mục tiêu**: So sánh hai hình thức lưu trữ tệp phổ biến trong kỹ thuật dữ liệu: Định dạng văn bản CSV và định dạng nhị phân hướng cột Parquet.

**Dữ liệu đầu vào**: Đối tượng DataFrame chỗ ở thu gọn gồm 5 cột kèm thông tin ngày giờ `first_review`.

**Thao tác yêu cầu**:
1. Triển khai hàm `save_formats(df: pd.DataFrame, folder) -> dict` để lưu bảng thành hai tệp: `t6.csv` và `t6.parquet` trong thư mục được chỉ định.
2. Đọc lại cả hai tệp vừa ghi (với `pd.read_csv` không dùng `parse_dates`, và `pd.read_parquet`).
3. Trả về từ điển kết quả chứa kích thước tệp theo byte (`size_csv`, `size_parquet`) và từ điển kiểu dữ liệu của các cột sau khi đọc lại (`dtypes_csv`, `dtypes_parquet`).

**Trường hợp biên cần chú ý**:
- Tệp Parquet đòi hỏi cài đặt engine nhị phân như `pyarrow`.
- Tệp CSV không thể tự lưu trữ siêu dữ liệu kiểu thời gian, do đó khi đọc lại mà không cấu hình, cột ngày sẽ bị suy giảm thành kiểu chuỗi hoặc object.
:::

::: solution
#### Cách 1: Ghi hai định dạng rồi đọc lại để kiểm tra

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import os

import pandas as pd

import tempfile

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL.to_csv("listings_full.csv", index=False)

cot_can_doc = ["id", "room_type", "price", "first_review", "number_of_reviews"]

cot_ngay = ["first_review"]


def read_selected(path, columns: list, date_columns: list) -> pd.DataFrame:
    # Đọc tệp có chọn lọc cột và chuyển đổi ngày giờ
    df = pd.read_csv(
        path, usecols=columns, parse_dates=date_columns if date_columns else False
    )
    return df


bang_chon_loc = read_selected("listings_full.csv", cot_can_doc, cot_ngay)

# Bắt đầu lời giải


def save_formats(df: pd.DataFrame, folder) -> dict:
    duong_dan_thu_muc = Path(folder)
    tep_csv = duong_dan_thu_muc / "t6.csv"
    tep_parquet = duong_dan_thu_muc / "t6.parquet"

    # Ghi tệp không kèm chỉ số dòng
    df.to_csv(tep_csv, index=False)
    df.to_parquet(tep_parquet, index=False)

    # Đọc lại để kiểm tra kiểu dữ liệu sau tái nạp
    doc_lai_csv = pd.read_csv(tep_csv)
    doc_lai_pq = pd.read_parquet(tep_parquet)

    ket_qua = {
        "size_csv": os.path.getsize(tep_csv),
        "size_parquet": os.path.getsize(tep_parquet),
        "dtypes_csv": {cot: str(doc_lai_csv[cot].dtype) for cot in doc_lai_csv.columns},
        "dtypes_parquet": {
            cot: str(doc_lai_pq[cot].dtype) for cot in doc_lai_pq.columns
        },
    }
    return ket_qua


# Thực thi mẫu với thư mục tạm
with tempfile.TemporaryDirectory() as thu_muc_tam:
    thong_so_luu_tru = save_formats(bang_chon_loc, thu_muc_tam)
    print("Dung lượng CSV (bytes):", thong_so_luu_tru["size_csv"])
    print("Dung lượng Parquet (bytes):", thong_so_luu_tru["size_parquet"])
    print(
        "Kiểu first_review trong CSV:", thong_so_luu_tru["dtypes_csv"]["first_review"]
    )
    print(
        "Kiểu first_review trong Parquet:",
        thong_so_luu_tru["dtypes_parquet"]["first_review"],
    )

# Kết thúc lời giải
```

##### Giải thích Cách 1

`Path(folder) / "t6.csv"` ghép tên tệp với thư mục đích. `index=False` yêu cầu không ghi thêm chỉ mục của DataFrame thành một cột dữ liệu. Hàm giả thiết thư mục đã tồn tại, như thư mục do `TemporaryDirectory` tạo trong ví dụ.

`.to_csv` lưu giá trị dưới dạng văn bản nhưng không kèm đầy đủ lược đồ kiểu của pandas. Vì `read_csv` trong bài không có `parse_dates`, cột ngày được đọc thành kiểu chuỗi hoặc `object`. `.to_parquet` dùng engine như `pyarrow` để lưu dữ liệu cùng thông tin kiểu, nên cột ngày của ví dụ giữ được độ phân giải khi đọc lại.

`os.path.getsize` trả kích thước tệp trên đĩa theo byte, khác với RAM của DataFrame. Tệp sáu dòng quá nhỏ để kết luận Parquet luôn gọn hơn CSV. Phần lược đồ và thông tin đầu cuối của Parquet có thể chiếm nhiều hơn dữ liệu được nén. Khả năng khôi phục kiểu cũng phụ thuộc kiểu nguồn, engine và phiên bản, không phải bảo đảm cho mọi đối tượng Python.

##### Output Cách 1

| Đại lượng | CSV | Parquet |
|---|---|---|
| Kích thước trong lần kiểm tra | 303 byte | 3671 byte |
| Kiểu `first_review` sau đọc | `str` | `datetime64[us]` |
| Ghi chỉ mục thành cột | Không | Không |

Số byte trên được chạy với pandas 3.0.5 và pyarrow 25.0.0. Phiên bản, metadata hoặc cách xuống dòng có thể làm kích thước tệp khác đi.

#### Cách 2: Tạo thư mục và dùng Path để đo kích thước

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import pandas as pd

import tempfile

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL.to_csv("listings_full.csv", index=False)

cot_can_doc = ["id", "room_type", "price", "first_review", "number_of_reviews"]

cot_ngay = ["first_review"]


def read_selected(path, columns: list, date_columns: list) -> pd.DataFrame:
    # Đọc tệp có chọn lọc cột và chuyển đổi ngày giờ
    df = pd.read_csv(
        path, usecols=columns, parse_dates=date_columns if date_columns else False
    )
    return df


bang_chon_loc = read_selected("listings_full.csv", cot_can_doc, cot_ngay)

# Bắt đầu lời giải


def save_formats_v2(df: pd.DataFrame, folder) -> dict:
    thu_muc = Path(folder)
    thu_muc.mkdir(parents=True, exist_ok=True)
    duong_dan_csv = thu_muc / "t6_v2.csv"
    duong_dan_pq = thu_muc / "t6_v2.parquet"

    # Ghi tệp định dạng nén tối ưu
    df.to_csv(duong_dan_csv, index=False)
    df.to_parquet(duong_dan_pq, index=False, compression="snappy")

    doc_csv = pd.read_csv(duong_dan_csv)
    doc_pq = pd.read_parquet(duong_dan_pq)

    return {
        "size_csv": duong_dan_csv.stat().st_size,
        "size_parquet": duong_dan_pq.stat().st_size,
        "dtypes_csv": {c: str(doc_csv[c].dtype) for c in doc_csv.columns},
        "dtypes_parquet": {c: str(doc_pq[c].dtype) for c in doc_pq.columns},
    }


# Thực thi mẫu phương pháp thứ hai
with tempfile.TemporaryDirectory() as thu_muc_tam_2:
    thong_so_v2 = save_formats_v2(bang_chon_loc, thu_muc_tam_2)
    print(
        "Tỷ lệ nén kích thước:",
        round(thong_so_v2["size_csv"] / thong_so_v2["size_parquet"], 2),
    )

# Kết thúc lời giải
```

##### Giải thích Cách 2

`.mkdir(parents=True, exist_ok=True)` tạo cả thư mục cha còn thiếu và không báo lỗi chỉ vì thư mục đã tồn tại. `.stat().st_size` lấy kích thước tệp qua đối tượng `Path`, có cùng đơn vị byte với `os.path.getsize`.

`compression="snappy"` chọn cách nén cho Parquet. Snappy là một lựa chọn cân bằng giữa nén và tốc độ, nhưng không hứa cho tệp nhỏ nhất. Đoạn mã vẫn gọi `read_parquet` để đọc bảng rồi xem các `.dtype`. Nó không chỉ đọc phần metadata và vẫn cần bộ nhớ cho dữ liệu đã nạp.

Tỷ số in ra là kích thước CSV chia kích thước Parquet. Giá trị nhỏ hơn 1 ở DEMO cho biết tệp CSV nhỏ hơn trong lần ghi này. Tên `t6_v2.csv` và `t6_v2.parquet` giúp giữ riêng các tệp của Cách 2, không ảnh hưởng nội dung bảng.

##### Output Cách 2

| Đại lượng | Kết quả lần kiểm tra |
|---|---|
| CSV / Parquet, làm tròn 2 chữ số | 0.08 |
| Kích thước CSV | 303 byte |
| Kích thước Parquet | 3671 byte |
| Kiểu ngày khi đọc Parquet | `datetime64[us]` |

#### So sánh hai cách

Hai cách cùng kiểm tra kích thước và kiểu sau khi đọc lại. Cách 2 bổ sung tạo thư mục và thao tác đường dẫn thống nhất. Với dữ liệu đủ lớn, Parquet có thể có lợi về nén và đọc chọn cột, nhưng phải đo trên trường hợp thực tế. Mức nén của sáu dòng chỉ dùng để hiểu cách đo, không dùng làm tỷ lệ dự báo.

:::

---

## Bài 4: Trích xuất dữ liệu API thời tiết lịch sử và lưu trữ phản hồi thô

<span id="data-lab-06-04"></span>

::: exercise
**Mục tiêu**: Xây dựng quy trình thu thập dữ liệu từ API thời tiết lịch sử của Open-Meteo, kiểm tra tính hợp lệ của đơn vị đo lường và thực hiện nguyên tắc lưu trữ phản hồi thô để phục vụ tái lập quy trình.

**Dữ liệu đầu vào**:
- Đối tượng từ điển phản hồi từ API thời tiết `payload` chứa thông tin kinh độ, vĩ độ, múi giờ và cấu trúc `daily` gồm các danh sách giá trị theo ngày.
- Đơn vị đo nhiệt độ tối đa được quy định trong `daily_units`.

**Thao tác yêu cầu**:
1. Triển khai hàm `weather_table(payload: dict, path) -> pd.DataFrame` để ghi toàn bộ cấu trúc phản hồi gốc ra tệp JSON tại đường dẫn `path`.
2. Chuyển đổi khối dữ liệu `daily` trong phản hồi thành một DataFrame với hai cột: `time` (chuỗi ngày) và `temperature_2m_max` (nhiệt độ tối đa trong ngày).
3. Triển khai hàm gọi mạng an toàn có tham số kiểm tra ngoại tuyến để không làm gián đoạn bài thực hành khi không có kết nối mạng.

**Trường hợp biên cần chú ý**:
- Phản hồi JSON thô phải được ghi với mã hóa UTF-8 và tham số `ensure_ascii=False` để giữ nguyên các ký tự đặc biệt.
- Kiểm tra tính nhất quán giữa đơn vị quy ước và dữ liệu thực tế: Đơn vị phải là `°C`.
:::

::: solution
#### Cách 1: Lưu JSON gốc rồi chuyển phần daily thành bảng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import json

import pandas as pd

import tempfile

DEMO_WEATHER = {
    "latitude": -33.45,
    "longitude": -70.66,
    "timezone": "America/Santiago",
    "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
    "daily": {
        "time": [f"2025-01-{d:02d}" for d in range(1, 11)],
        "temperature_2m_max": [
            31.4,
            33.1,
            29.1,
            32.8,
            30.2,
            30.0,
            28.5,
            31.8,
            30.9,
            27.6,
        ],
    },
}

# Bắt đầu lời giải


def weather_table(payload: dict, path) -> pd.DataFrame:
    duong_dan_tep = Path(path)
    duong_dan_tep.parent.mkdir(parents=True, exist_ok=True)

    # Ghi toàn bộ phản hồi thô ra đĩa
    with open(duong_dan_tep, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

    # Chuyển đổi phần daily thành bảng dữ liệu
    bang_thoi_tiet = pd.DataFrame(payload["daily"])
    return bang_thoi_tiet


# Thực thi mẫu với dữ liệu giả lập DEMO_WEATHER
with tempfile.TemporaryDirectory() as thu_muc_tam:
    tep_thoi_tiet = Path(thu_muc_tam) / "weather_scl_2025-01.json"
    df_thoi_tiet = weather_table(DEMO_WEATHER, tep_thoi_tiet)
    print("Số ngày trong bảng thời tiết:", len(df_thoi_tiet))
    print(
        "Nhiệt độ tối đa trung bình:",
        round(df_thoi_tiet["temperature_2m_max"].mean(), 2),
    )

# Kết thúc lời giải
```

##### Giải thích Cách 1

`Path(path).parent` lấy thư mục chứa tệp. `.mkdir(parents=True, exist_ok=True)` tạo nơi lưu nếu chưa có. Khối `with open(..., encoding="utf-8")` quản lý việc mở và đóng tệp ngay cả khi có lỗi trong quá trình ghi.

`json.dump(payload, f, ensure_ascii=False, indent=2)` lưu toàn bộ từ điển đã nhận, bao gồm tọa độ, múi giờ, đơn vị và các dãy ngày. `ensure_ascii=False` giữ ký tự như `°` dễ đọc trong tệp UTF-8. `indent=2` chỉ định cách trình bày thụt lề. Đây là bản lưu cấu trúc JSON đã giải mã, không phải bản sao từng byte của phản hồi HTTP.

`pd.DataFrame(payload["daily"])` tạo mỗi danh sách thành một cột. Hai danh sách phải có cùng độ dài để ghép đúng nhiệt độ với ngày. Cách cơ bản này giả thiết cấu trúc và đơn vị đã hợp lệ. Cần bước kiểm tra như Cách 2 khi phản hồi đến từ nguồn có thể thay đổi.

##### Output Cách 1

| `time` | `temperature_2m_max` (°C) |
|---|---|
| 2025-01-01 | 31.4 |
| 2025-01-02 | 33.1 |
| 2025-01-03 | 29.1 |
| 2025-01-04 | 32.8 |
| 2025-01-05 | 30.2 |
| 2025-01-06 | 30.0 |
| 2025-01-07 | 28.5 |
| 2025-01-08 | 31.8 |
| 2025-01-09 | 30.9 |
| 2025-01-10 | 27.6 |

Bảng có 10 ngày. Trung bình các nhiệt độ tối đa là `30.54 °C`.

#### Cách 2: Kiểm tra đơn vị và cho phép dùng phản hồi ngoại tuyến

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import json

import pandas as pd

DEMO_WEATHER = {
    "latitude": -33.45,
    "longitude": -70.66,
    "timezone": "America/Santiago",
    "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
    "daily": {
        "time": [f"2025-01-{d:02d}" for d in range(1, 11)],
        "temperature_2m_max": [
            31.4,
            33.1,
            29.1,
            32.8,
            30.2,
            30.0,
            28.5,
            31.8,
            30.9,
            27.6,
        ],
    },
}

# Bắt đầu lời giải


def fetch_weather_archive(
    latitude: float,
    longitude: float,
    start_date: str,
    end_date: str,
    offline_payload: dict = None,
) -> dict:
    # Nếu được cung cấp payload ngoại tuyến, sử dụng trực tiếp không qua mạng
    if offline_payload is not None:
        return offline_payload

    # Trường hợp gọi mạng thật qua thư viện urllib tiêu chuẩn
    import urllib.request
    import urllib.parse

    tham_so = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_max",
        "timezone": "America/Santiago",
    }
    url = f"https://archive-api.open-meteo.com/v1/archive?{urllib.parse.urlencode(tham_so)}"
    yeu_cau = urllib.request.Request(
        url, headers={"User-Agent": "StudyHub-DataLab/1.0"}
    )
    with urllib.request.urlopen(yeu_cau, timeout=30) as phan_hoi:
        du_lieu_json = json.loads(phan_hoi.read().decode("utf-8"))
    return du_lieu_json


def weather_table_v2(payload: dict, path, metadata: dict = None) -> pd.DataFrame:
    # Xác thực đơn vị đo lường nhiệt độ
    don_vi = payload.get("daily_units", {}).get("temperature_2m_max")
    if don_vi != "°C":
        raise ValueError(
            f"Đơn vị đo không phù hợp, kỳ vọng '°C', nhận được: '{don_vi}'"
        )

    tep = Path(path)
    tep.parent.mkdir(parents=True, exist_ok=True)
    tep.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    if metadata:
        tep_meta = tep.with_suffix(".meta.json")
        tep_meta.write_text(
            json.dumps(metadata, ensure_ascii=False, indent=2), encoding="utf-8"
        )

    return pd.DataFrame(payload["daily"])


# Thực thi mẫu với chế độ ngoại tuyến an toàn
payload_thu_thap = fetch_weather_archive(
    -33.45, -70.66, "2025-01-01", "2025-01-10", offline_payload=DEMO_WEATHER
)
df_thoi_tiet_v2 = weather_table_v2(
    payload_thu_thap, "weather_v2.json", metadata={"nguon": "Open-Meteo Archive"}
)
print(
    "Kiểm tra đơn vị thành công:", payload_thu_thap["daily_units"]["temperature_2m_max"]
)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`offline_payload` cho phép chạy lại bài bằng dữ liệu mẫu mà không gọi mạng. Nếu không truyền đối số đó, `urlencode(tham_so)` mã hóa các tham số trong URL, rồi `urlopen(..., timeout=30)` thực hiện yêu cầu mạng. `json.loads` chuyển nội dung phản hồi đã giải mã UTF-8 thành từ điển Python.

Trong `weather_table_v2`, hai lần `.get` đọc đơn vị mà không gây `KeyError` nếu thiếu trường. Nếu đơn vị không đúng `°C`, hàm phát sinh `ValueError` trước khi dùng nhiệt độ để tính toán. `write_text` lưu bản JSON có thể đọc lại. Nếu có `metadata`, `.with_suffix(".meta.json")` tạo một tệp thông tin phụ cạnh bản lưu chính.

Ví dụ truyền `DEMO_WEATHER` nên các con số dưới đây vẫn là dữ liệu giả lập. Chuỗi nguồn trong metadata không biến fixture thành quan sát thời tiết thực. Bảng trả về có cùng hai cột như Cách 1 và vẫn giữ `time` là chuỗi để ghép ở những bài sau.

##### Output Cách 2

| `time` | `temperature_2m_max` (°C) |
|---|---|
| 2025-01-01 | 31.4 |
| 2025-01-02 | 33.1 |
| 2025-01-03 | 29.1 |
| 2025-01-04 | 32.8 |
| 2025-01-05 | 30.2 |
| 2025-01-06 | 30.0 |
| 2025-01-07 | 28.5 |
| 2025-01-08 | 31.8 |
| 2025-01-09 | 30.9 |
| 2025-01-10 | 27.6 |

Dòng xác nhận của ví dụ là `Kiểm tra đơn vị thành công: °C`.

#### So sánh hai cách

Cách 1 mở rõ thao tác ghi tệp và lấy phần dữ liệu cần dùng. Cách 2 thêm kiểm tra đơn vị, metadata và lựa chọn nguồn ngoại tuyến để dễ tái lập. Nếu cần kiểm soát đầy đủ hơn, phải kiểm tra cả độ dài mảng, tên trường, phạm vi ngày và trạng thái phản hồi. Hai cách đều không được dùng dữ liệu mẫu để suy ra khí hậu thực tế.

:::

---

## Bài 5: Thống kê số lượng đánh giá theo ngày và xử lý ngày không có đánh giá

<span id="data-lab-06-05"></span>

::: exercise
**Mục tiêu**: Lọc các dòng đánh giá theo một khoảng thời gian cố định, gom nhóm theo từng ngày và tạo bảng đếm tần suất phục vụ ghép nối dữ liệu.

**Dữ liệu đầu vào**:
- Bảng đánh giá `rv` chứa cột `date` kiểu `datetime64`.
- Hai mốc thời gian lọc dạng chuỗi: `start` và `end` (định dạng `YYYY-MM-DD`).

**Thao tác yêu cầu**:
1. Triển khai hàm `reviews_per_day(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame` để lọc các dòng thỏa mãn `start <= date <= end` (bao gồm cả hai đầu khoảng).
2. Định dạng ngày thành chuỗi chuẩn `YYYY-MM-DD` bằng phương thức `dt.strftime("%Y-%m-%d")`.
3. Đếm số lượng dòng đánh giá cho từng ngày, sắp xếp theo thời gian tăng dần và thiết lập lại chỉ mục số nguyên `0, 1, 2...`.

**Trường hợp biên cần chú ý**:
- Những ngày nằm trong khoảng lọc nhưng không có lượt đánh giá nào phát sinh (ví dụ ngày `2025-01-05` trong dữ liệu mẫu) sẽ không xuất hiện trong kết quả của phép gom nhóm này.
- Giữ nguyên dữ liệu của bảng `rv` ban đầu, không thay đổi chỉ mục hay giá trị của DataFrame đầu vào.
:::

::: solution
#### Cách 1: Lọc khoảng ngày rồi nhóm các dòng có cùng ngày

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

# Bắt đầu lời giải


def reviews_per_day(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    # Bản sao an toàn để tránh cảnh báo Copy-on-Write
    du_lieu = rv.copy()
    ngay_bat_dau = pd.to_datetime(start)
    ngay_ket_thuc = pd.to_datetime(end)

    # Bước 1: Lọc các dòng nằm trong khoảng ngày yêu cầu
    dieu_kien = (du_lieu["date"] >= ngay_bat_dau) & (du_lieu["date"] <= ngay_ket_thuc)
    du_lieu_loc = du_lieu.loc[dieu_kien]

    # Bước 2: Gom nhóm theo chuỗi ngày và đếm số lượng
    chuoi_ngay = du_lieu_loc["date"].dt.strftime("%Y-%m-%d")
    dem_ngay = du_lieu_loc.groupby(chuoi_ngay).size().reset_index(name="so_review")

    # Bước 3: Đổi tên cột đồng nhất và sắp xếp thời gian tăng dần
    ket_qua = (
        dem_ngay.rename(columns={"date": "time"})
        .sort_values("time")
        .reset_index(drop=True)
    )
    return ket_qua


# Thực thi mẫu với khoảng ngày từ 2025-01-01 đến 2025-01-10
thong_ke_ngay = reviews_per_day(DEMO_REVIEWS, "2025-01-01", "2025-01-10")
print("Tổng số ngày có đánh giá:", len(thong_ke_ngay))
print("Tổng lượt đánh giá:", thong_ke_ngay["so_review"].sum())

# Kết thúc lời giải
```

##### Giải thích Cách 1

`pd.to_datetime(start)` và `pd.to_datetime(end)` tạo hai mốc để so sánh với cột `date`. Hai điều kiện dùng `>=` và `<=`, rồi ghép bằng `&`. Mỗi vế phải có ngoặc vì đây là phép toán trên toàn Series, không phải toán tử `and` của một giá trị boolean.

Với dữ liệu của bài đều ở mốc đầu ngày, điều kiện giữ cả ngày đầu và ngày cuối. Nếu cột chứa cả giờ, `end="2025-01-10"` chỉ biểu diễn nửa đêm bắt đầu ngày đó. Muốn bao phủ trọn ngày cuối trong một bài khác, cần chọn khoảng thời gian phù hợp thay vì cho rằng định dạng ngày đã giải quyết vấn đề giờ và múi giờ.

`.dt.strftime("%Y-%m-%d")` tạo khóa ngày dạng chuỗi ISO. `groupby(chuoi_ngay).size()` đếm số dòng của từng khóa, còn `reset_index(name="so_review")` đưa khóa ra thành cột. Đổi tên sang `time`, sắp theo ngày rồi đặt lại chỉ mục tạo đúng bảng hai cột theo đề. Ngày 05/01 không xuất hiện vì không có dòng đánh giá nào của ngày ấy.

##### Output Cách 1

| `time` | `so_review` |
|---|---|
| 2025-01-01 | 3 |
| 2025-01-02 | 5 |
| 2025-01-03 | 2 |
| 2025-01-04 | 6 |
| 2025-01-06 | 4 |
| 2025-01-07 | 7 |
| 2025-01-08 | 1 |
| 2025-01-09 | 5 |
| 2025-01-10 | 3 |

Kết quả có 9 ngày và tổng `so_review` bằng 36.

#### Cách 2: Đếm tần suất trực tiếp trên Series ngày

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)


def reviews_per_day(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    # Bản sao an toàn để tránh cảnh báo Copy-on-Write
    du_lieu = rv.copy()
    ngay_bat_dau = pd.to_datetime(start)
    ngay_ket_thuc = pd.to_datetime(end)

    # Bước 1: Lọc các dòng nằm trong khoảng ngày yêu cầu
    dieu_kien = (du_lieu["date"] >= ngay_bat_dau) & (du_lieu["date"] <= ngay_ket_thuc)
    du_lieu_loc = du_lieu.loc[dieu_kien]

    # Bước 2: Gom nhóm theo chuỗi ngày và đếm số lượng
    chuoi_ngay = du_lieu_loc["date"].dt.strftime("%Y-%m-%d")
    dem_ngay = du_lieu_loc.groupby(chuoi_ngay).size().reset_index(name="so_review")

    # Bước 3: Đổi tên cột đồng nhất và sắp xếp thời gian tăng dần
    ket_qua = (
        dem_ngay.rename(columns={"date": "time"})
        .sort_values("time")
        .reset_index(drop=True)
    )
    return ket_qua


thong_ke_ngay = reviews_per_day(DEMO_REVIEWS, "2025-01-01", "2025-01-10")

# Bắt đầu lời giải


def reviews_per_day_v2(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    ngay_dau = pd.to_datetime(start)
    ngay_cuoi = pd.to_datetime(end)

    # Lọc Series ngày trực tiếp
    cot_ngay_loc = rv.loc[(rv["date"] >= ngay_dau) & (rv["date"] <= ngay_cuoi), "date"]

    # Đếm tần suất xuất hiện của từng chuỗi ngày
    dem_tan_suat = cot_ngay_loc.dt.strftime("%Y-%m-%d").value_counts().sort_index()

    # Chuyển đổi Series thành DataFrame hai cột chuẩn
    ket_qua = dem_tan_suat.reset_index()
    ket_qua.columns = ["time", "so_review"]
    return ket_qua


# Thực thi mẫu phương pháp thứ hai
thong_ke_ngay_v2 = reviews_per_day_v2(DEMO_REVIEWS, "2025-01-01", "2025-01-10")
print("Kiểm tra tính trùng khớp kết quả:", thong_ke_ngay.equals(thong_ke_ngay_v2))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`rv.loc[điều_kiện, "date"]` chỉ lấy cột ngày của các dòng trong khoảng, nên không sao chép toàn bộ các cột của bảng như bước `rv.copy()` ở Cách 1. Đầu vào vẫn được giữ nguyên vì các bước sau chỉ tạo kết quả mới.

Sau khi định dạng ngày, `.value_counts()` đếm số lần mỗi chuỗi xuất hiện. Kết quả mặc định xếp theo tần suất, vì vậy phải thêm `.sort_index()` để đưa các ngày về thứ tự thời gian. Với chuỗi ISO có tháng và ngày đủ hai chữ số, thứ tự chữ cái cũng là thứ tự ngày.

`reset_index()` chuyển Series tần suất thành DataFrame. Gán `ket_qua.columns` xác định rõ tên hai cột `time` và `so_review`, tránh phụ thuộc tên mặc định theo phiên bản pandas. Ngày không có sự kiện vẫn không tự được sinh thêm.

##### Output Cách 2

| `time` | `so_review` |
|---|---|
| 2025-01-01 | 3 |
| 2025-01-02 | 5 |
| 2025-01-03 | 2 |
| 2025-01-04 | 6 |
| 2025-01-06 | 4 |
| 2025-01-07 | 7 |
| 2025-01-08 | 1 |
| 2025-01-09 | 5 |
| 2025-01-10 | 3 |

Ví dụ in `Kiểm tra tính trùng khớp kết quả: True`.

#### So sánh hai cách

Cách 1 mô tả riêng lọc, tạo khóa và tổng hợp nên dễ theo dõi. Cách 2 chọn ngay cột cần dùng và dùng thao tác đếm chuyên dụng, giảm các bản sao không cần thiết của bảng rộng. Hai cách đều trả các ngày có đánh giá. Lập lịch ngày liên tục rồi điền 0 là một yêu cầu khác và phải được nêu rõ.

:::

---

## Bài 6: Ghép nối thời tiết và đánh giá bằng phép ghép trái và đo lường tương quan

<span id="data-lab-06-06"></span>

::: exercise
**Mục tiêu**: Ghép nối hai nguồn dữ liệu không đồng nhất theo trục thời gian bằng phép ghép trái (Left Join), xử lý các giá trị khuyết thiếu và đo lường hệ số tương quan tuyến tính Pearson.

**Dữ liệu đầu vào**:
- Bảng thời tiết `weather` chứa các cột `time` (chuỗi ngày) và `temperature_2m_max` (nhiệt độ tối đa).
- Bảng thống kê đánh giá `per_day` tạo ra từ Bài 5 chứa cột `time` và `so_review`.

**Thao tác yêu cầu**:
1. Triển khai hàm `join_weather(weather: pd.DataFrame, per_day: pd.DataFrame) -> dict` sử dụng phép ghép trái `merge(..., on="time", how="left")` để giữ nguyên toàn bộ các ngày có trong bảng thời tiết.
2. Xác định số lượng ngày không có lượt đánh giá nào (các dòng có giá trị `NaN` ở cột `so_review`).
3. Tính hệ số tương quan Pearson giữa cột nhiệt độ tối đa `temperature_2m_max` và số lượt đánh giá `so_review`.
4. Trả về từ điển kết quả chứa DataFrame sau ghép nối `gop`, số ngày khuyết `so_thieu`, và hệ số tương quan `he_so`.

**Trường hợp biên cần chú ý**:
- Theo yêu cầu của bài này, giữ nguyên `NaN` khi phép ghép không tìm thấy ngày tương ứng. Không tự đổi thành 0, vì như vậy ta đang thay đổi tập cặp quan sát dùng để tính tương quan.
:::

::: solution
#### Cách 1: Ghép theo cột ngày và tính corr trên các cặp hợp lệ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)


def reviews_per_day(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    # Bản sao an toàn để tránh cảnh báo Copy-on-Write
    du_lieu = rv.copy()
    ngay_bat_dau = pd.to_datetime(start)
    ngay_ket_thuc = pd.to_datetime(end)

    # Bước 1: Lọc các dòng nằm trong khoảng ngày yêu cầu
    dieu_kien = (du_lieu["date"] >= ngay_bat_dau) & (du_lieu["date"] <= ngay_ket_thuc)
    du_lieu_loc = du_lieu.loc[dieu_kien]

    # Bước 2: Gom nhóm theo chuỗi ngày và đếm số lượng
    chuoi_ngay = du_lieu_loc["date"].dt.strftime("%Y-%m-%d")
    dem_ngay = du_lieu_loc.groupby(chuoi_ngay).size().reset_index(name="so_review")

    # Bước 3: Đổi tên cột đồng nhất và sắp xếp thời gian tăng dần
    ket_qua = (
        dem_ngay.rename(columns={"date": "time"})
        .sort_values("time")
        .reset_index(drop=True)
    )
    return ket_qua


thong_ke_ngay = reviews_per_day(DEMO_REVIEWS, "2025-01-01", "2025-01-10")

DEMO_WEATHER = {
    "latitude": -33.45,
    "longitude": -70.66,
    "timezone": "America/Santiago",
    "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
    "daily": {
        "time": [f"2025-01-{d:02d}" for d in range(1, 11)],
        "temperature_2m_max": [
            31.4,
            33.1,
            29.1,
            32.8,
            30.2,
            30.0,
            28.5,
            31.8,
            30.9,
            27.6,
        ],
    },
}

df_thoi_tiet = pd.DataFrame(DEMO_WEATHER["daily"])

# Bắt đầu lời giải


def join_weather(weather: pd.DataFrame, per_day: pd.DataFrame) -> dict:
    # Thực hiện ghép trái theo cột khóa time
    gop = weather.merge(per_day, on="time", how="left")

    # Đếm số lượng giá trị khuyết thiếu ở cột đánh giá
    so_thieu = int(gop["so_review"].isna().sum())

    # Tính toán hệ số tương quan Pearson
    he_so = float(gop["temperature_2m_max"].corr(gop["so_review"]))

    return {
        "gop": gop,
        "so_thieu": so_thieu,
        "he_so": he_so,
    }


# Thực thi mẫu ghép nối bảng thời tiết và bảng đánh giá
ket_qua_ghep = join_weather(df_thoi_tiet, thong_ke_ngay)
print("Số dòng sau ghép:", len(ket_qua_ghep["gop"]))
print("Số ngày khuyết đánh giá:", ket_qua_ghep["so_thieu"])
print("Hệ số tương quan Pearson:", round(ket_qua_ghep["he_so"], 3))

# Kết thúc lời giải
```

##### Giải thích Cách 1

`weather.merge(per_day, on="time", how="left")` giữ các ngày của bảng thời tiết rồi tìm số đánh giá theo cùng khóa. Ví dụ có mỗi ngày đúng một dòng ở mỗi bảng nên kết quả vẫn có 10 dòng. Nếu bảng đếm chứa khóa ngày trùng, phép ghép có thể tăng số dòng, vì vậy tính duy nhất của khóa cần được kiểm tra trong dữ liệu thật.

`.isna().sum()` trên `so_review` cho biết một ngày không khớp. Do có ô khuyết, cột số đếm có thể hiển thị bằng số thực như `3.0`. Giá trị ấy vẫn có nghĩa là ba đánh giá, không phải phép đếm phân số.

`Series.corr` mặc định tính hệ số Pearson và bỏ những cặp có ít nhất một giá trị khuyết. Ở đây có chín cặp được dùng, còn ngày 05/01 không tham gia. Hệ số khoảng `0.084` chỉ mô tả quan hệ tuyến tính yếu trong chín cặp của fixture. Nó không chứng minh nhiệt độ gây ra hoặc không gây ra thay đổi số đánh giá.

##### Output Cách 1

| `time` | Nhiệt độ tối đa (°C) | `so_review` |
|---|---|---|
| 2025-01-01 | 31.4 | 3.0 |
| 2025-01-02 | 33.1 | 5.0 |
| 2025-01-03 | 29.1 | 2.0 |
| 2025-01-04 | 32.8 | 6.0 |
| 2025-01-05 | 30.2 | `NaN` |
| 2025-01-06 | 30 | 4.0 |
| 2025-01-07 | 28.5 | 7.0 |
| 2025-01-08 | 31.8 | 1.0 |
| 2025-01-09 | 30.9 | 5.0 |
| 2025-01-10 | 27.6 | 3.0 |

Từ điển có `so_thieu = 1`. Giá trị `he_so` làm tròn ba chữ số là `0.084`.

#### Cách 2: Ghép bằng chỉ mục rồi kiểm tra số cặp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)


def reviews_per_day(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    # Bản sao an toàn để tránh cảnh báo Copy-on-Write
    du_lieu = rv.copy()
    ngay_bat_dau = pd.to_datetime(start)
    ngay_ket_thuc = pd.to_datetime(end)

    # Bước 1: Lọc các dòng nằm trong khoảng ngày yêu cầu
    dieu_kien = (du_lieu["date"] >= ngay_bat_dau) & (du_lieu["date"] <= ngay_ket_thuc)
    du_lieu_loc = du_lieu.loc[dieu_kien]

    # Bước 2: Gom nhóm theo chuỗi ngày và đếm số lượng
    chuoi_ngay = du_lieu_loc["date"].dt.strftime("%Y-%m-%d")
    dem_ngay = du_lieu_loc.groupby(chuoi_ngay).size().reset_index(name="so_review")

    # Bước 3: Đổi tên cột đồng nhất và sắp xếp thời gian tăng dần
    ket_qua = (
        dem_ngay.rename(columns={"date": "time"})
        .sort_values("time")
        .reset_index(drop=True)
    )
    return ket_qua


thong_ke_ngay = reviews_per_day(DEMO_REVIEWS, "2025-01-01", "2025-01-10")

DEMO_WEATHER = {
    "latitude": -33.45,
    "longitude": -70.66,
    "timezone": "America/Santiago",
    "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
    "daily": {
        "time": [f"2025-01-{d:02d}" for d in range(1, 11)],
        "temperature_2m_max": [
            31.4,
            33.1,
            29.1,
            32.8,
            30.2,
            30.0,
            28.5,
            31.8,
            30.9,
            27.6,
        ],
    },
}

df_thoi_tiet = pd.DataFrame(DEMO_WEATHER["daily"])

# Bắt đầu lời giải


def join_weather_v2(weather: pd.DataFrame, per_day: pd.DataFrame) -> dict:
    # Đặt time làm chỉ mục để ghép nối băm nhanh
    w_idx = weather.set_index("time")
    p_idx = per_day.set_index("time")

    # Ghép nối trái trên chỉ mục
    gop_idx = w_idx.join(p_idx, how="left").reset_index()

    so_thieu = int(gop_idx["so_review"].isna().sum())

    # Kiểm tra điều kiện tối thiểu để tính hệ số tương quan
    cac_dong_hop_le = gop_idx.dropna(subset=["temperature_2m_max", "so_review"])
    if len(cac_dong_hop_le) >= 2:
        he_so = float(
            cac_dong_hop_le["temperature_2m_max"].corr(cac_dong_hop_le["so_review"])
        )
    else:
        he_so = float("nan")

    return {
        "gop": gop_idx,
        "so_thieu": so_thieu,
        "he_so": he_so,
    }


# Thực thi mẫu phương pháp thứ hai
ket_qua_ghep_v2 = join_weather_v2(df_thoi_tiet, thong_ke_ngay)
print("Hệ số tương quan cách 2:", round(ket_qua_ghep_v2["he_so"], 3))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`set_index("time")` đưa khóa ngày thành chỉ mục. `.join(p_idx, how="left")` ghép theo các chỉ mục ấy, sau đó `reset_index()` đưa ngày về cột. Cách viết phù hợp khi bảng đã dùng ngày làm chỉ mục. Việc đổi chỉ mục riêng để ghép chưa tự bảo đảm nhanh hơn `merge`.

`dropna(subset=["temperature_2m_max", "so_review"])` xác định tường minh những dòng có đủ hai số để tính tương quan. Nếu còn ít hơn hai dòng, hàm trả `float("nan")`. Kể cả có hai dòng trở lên, nếu một biến không thay đổi thì hệ số Pearson vẫn chưa xác định và pandas trả `NaN`.

Cột `so_review` trong `gop` không được điền 0. Quy tắc này giữ đúng yêu cầu tính trên cặp quan sát có sẵn. Với một log sự kiện đầy đủ, lập lịch liên tục để diễn giải ngày không có sự kiện là 0 có thể hợp lý, nhưng sẽ tạo tập cặp và hệ số khác.

##### Output Cách 2

| `time` | Nhiệt độ tối đa (°C) | `so_review` |
|---|---|---|
| 2025-01-01 | 31.4 | 3.0 |
| 2025-01-02 | 33.1 | 5.0 |
| 2025-01-03 | 29.1 | 2.0 |
| 2025-01-04 | 32.8 | 6.0 |
| 2025-01-05 | 30.2 | `NaN` |
| 2025-01-06 | 30 | 4.0 |
| 2025-01-07 | 28.5 | 7.0 |
| 2025-01-08 | 31.8 | 1.0 |
| 2025-01-09 | 30.9 | 5.0 |
| 2025-01-10 | 27.6 | 3.0 |

Cách 2 cũng có 10 dòng, một số đếm khuyết và hệ số làm tròn `0.084`.

#### So sánh hai cách

Hai cách khác cách biểu diễn khóa ghép. Cách 1 dễ dùng với bảng còn cột ngày, Cách 2 thuận tiện với bảng đã có chỉ mục ngày và mở rõ kiểm tra số cặp. Trước khi diễn giải hệ số, cần xem số cặp hợp lệ, độ biến thiên, kỳ quan sát và dữ liệu khuyết. Tương quan không đo số đặt phòng và không xác lập quan hệ nhân quả.

:::

---

## Bài 7: Truy vấn trực tiếp trên tệp CSV và đếm đánh giá theo năm với DuckDB

<span id="data-lab-06-07"></span>

::: exercise
**Mục tiêu**: Sử dụng DuckDB để thực thi các truy vấn SQL trực tiếp trên tệp văn bản CSV mà không cần nạp toàn bộ dữ liệu vào đối tượng DataFrame của pandas.

**Dữ liệu đầu vào**: Đường dẫn tệp CSV đánh giá `reviews.csv` chứa các cột `listing_id` và `date`.

**Thao tác yêu cầu**:
1. Triển khai hàm `sql_reviews_by_year(reviews_path) -> pd.DataFrame` thực hiện một câu truy vấn SQL DuckDB duy nhất để trích xuất năm từ cột ngày và đếm tổng số dòng đánh giá cho từng năm.
2. Câu truy vấn sử dụng hàm `year(date)` để lấy giá trị năm, gom nhóm bằng `GROUP BY nam` và sắp xếp tăng dần theo năm `ORDER BY nam`.
3. Trả về kết quả dưới dạng một DataFrame gồm đúng hai cột: `nam` (kiểu số nguyên) và `n` (số lượng đánh giá kiểu số nguyên).

**Trường hợp biên cần chú ý**:
- Đường dẫn trong ví dụ cơ bản là đường dẫn tệp cục bộ đã biết. Dấu gạch xuôi `/` thống nhất cách viết đường dẫn nhưng không thoát ký tự SQL. Dùng tham số truy vấn khi truyền đường dẫn có thể chứa ký tự đặc biệt.
- Kết quả đếm từ SQL phải khớp tuyệt đối với kết quả thống kê bằng logic Python thuần hoặc pandas trên cùng tập dữ liệu.
:::

::: solution
#### Cách 1: Đếm theo năm trực tiếp trên tệp bằng DuckDB

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_REVIEWS.to_csv("reviews.csv", index=False)

# Bắt đầu lời giải


def sql_reviews_by_year(reviews_path) -> pd.DataFrame:
    # Chuẩn hóa đường dẫn tệp sang dạng chuỗi posix
    duong_dan = Path(reviews_path).as_posix()

    # Câu truy vấn SQL đếm theo năm
    cau_lenh = f"""
    SELECT year(date) AS nam, count(*) AS n
    FROM '{duong_dan}'
    GROUP BY nam
    ORDER BY nam
    """
    bang_ket_qua = duckdb.sql(cau_lenh).df()
    return bang_ket_qua


# Thực thi mẫu với tệp reviews.csv
bang_dem_nam = sql_reviews_by_year("reviews.csv")
print("Kết quả đếm theo năm qua DuckDB:")
print(bang_dem_nam)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`Path(reviews_path).as_posix()` chuẩn hóa dấu phân cách đường dẫn thành `/`. Trong câu SQL, `FROM 'đường_dẫn'` cho DuckDB đọc tệp CSV, còn `.df()` chuyển bảng kết quả thành DataFrame pandas. Không cần tạo trước một DataFrame chứa toàn bộ tệp chỉ để chạy phép tổng hợp này.

`year(date) AS nam` lấy năm và đặt tên cột. `COUNT(*) AS n` đếm mọi dòng của từng năm sau `GROUP BY nam`. `ORDER BY nam` là điều tạo thứ tự năm tăng dần trong đầu ra. Không nên dựa vào thứ tự tình cờ của phép nhóm.

Đọc CSV vẫn cần quét dữ liệu liên quan, nên không thể xem đây là lời hứa chỉ đọc vài khối byte hay không dùng RAM. Đoạn ghép chuỗi SQL cơ bản giả thiết đường dẫn cục bộ hợp lệ và không chứa dấu nháy đơn. `as_posix()` không thoát ký tự SQL. Cách 2 dùng tham số để truyền giá trị đường dẫn chắc chắn hơn.

##### Output Cách 1

| `nam` | `n` |
|---|---|
| 2023 | 3 |
| 2024 | 6 |
| 2025 | 40 |
| 2026 | 2 |

#### Cách 2: Truyền đường dẫn bằng tham số và khai báo kiểu đầu ra

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_REVIEWS.to_csv("reviews.csv", index=False)


def sql_reviews_by_year(reviews_path) -> pd.DataFrame:
    # Chuẩn hóa đường dẫn tệp sang dạng chuỗi posix
    duong_dan = Path(reviews_path).as_posix()

    # Câu truy vấn SQL đếm theo năm
    cau_lenh = f"""
    SELECT year(date) AS nam, count(*) AS n
    FROM '{duong_dan}'
    GROUP BY nam
    ORDER BY nam
    """
    bang_ket_qua = duckdb.sql(cau_lenh).df()
    return bang_ket_qua


bang_dem_nam = sql_reviews_by_year("reviews.csv")

# Bắt đầu lời giải


def sql_reviews_by_year_v2(reviews_path) -> pd.DataFrame:
    chuoi_tep = str(Path(reviews_path).resolve())

    # Tạo kết nối bộ nhớ độc lập
    ket_noi = duckdb.connect(database=":memory:")

    # Thực thi truy vấn với tham số vị trí an toàn
    truy_van = """
    SELECT CAST(year(date) AS INTEGER) AS nam,
           CAST(count(*) AS BIGINT) AS n
    FROM read_csv_auto(?)
    GROUP BY nam
    ORDER BY nam ASC
    """
    ket_qua = ket_noi.execute(truy_van, [chuoi_tep]).df()
    ket_noi.close()
    return ket_qua


# Thực thi mẫu phương pháp thứ hai
bang_dem_nam_v2 = sql_reviews_by_year_v2("reviews.csv")
print("Kiểm tra khớp tuyệt đối giữa hai cách:", bang_dem_nam.equals(bang_dem_nam_v2))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`duckdb.connect(database=":memory:")` mở một kết nối cơ sở dữ liệu trong bộ nhớ. Trong `read_csv_auto(?)`, dấu `?` là vị trí nhận giá trị. `execute(truy_van, [chuoi_tep])` truyền đường dẫn riêng với mã SQL, giúp xử lý đường dẫn có dấu cách hoặc ký tự đặc biệt mà không tự thêm dấu nháy.

`CAST(year(date) AS INTEGER)` chuẩn hóa năm thành số nguyên 32 bit trong DuckDB. `CAST(count(*) AS BIGINT)` dùng số nguyên 64 bit cho số đếm. `.df()` xuất kết quả, rồi `.close()` đóng kết nối sau khi đã lấy bảng.

Trên đoạn mã hiện tại, hai bảng có cùng năm và số đếm nhưng `bang_dem_nam.equals(bang_dem_nam_v2)` in `False`. Nguyên nhân là Cách 1 trả cột năm kiểu `int64`, Cách 2 ép về `int32`. `DataFrame.equals` so cả kiểu dữ liệu tương ứng, nên bằng nhau về giá trị chưa đủ. Muốn kiểm tra lược đồ giống nhau, hãy chuẩn hóa kiểu rồi mới so. Nếu chỉ kiểm tra giá trị, cần nêu rõ phép đối chiếu cho phép khác kiểu.

##### Output Cách 2

| `nam` | `n` |
|---|---|
| 2023 | 3 |
| 2024 | 6 |
| 2025 | 40 |
| 2026 | 2 |

Bản in đối chiếu của hai đoạn mã chưa chuẩn hóa cùng kiểu là `Kiểm tra khớp tuyệt đối giữa hai cách: False`.

#### So sánh hai cách

Cách 1 gọn cho truy vấn thử với tệp cục bộ đã biết. Cách 2 phù hợp hơn khi đường dẫn đến từ đối số hàm và cần kiểu đầu ra ổn định. Hai cách không khác số đánh giá đã đếm. Trong báo cáo kiểm thử, cần tách kiểm tra giá trị với kiểm tra lược đồ thay vì coi mọi `False` từ `.equals` là sai phép tổng hợp.

:::

---

## Bài 8: Phân biệt `COUNT(*)` và `COUNT(cột)` trong DuckDB trên tệp Parquet

<span id="data-lab-06-08"></span>

::: exercise
**Mục tiêu**: Nắm vững sự khác biệt ngữ nghĩa căn bản trong chuẩn SQL giữa hàm đếm bản ghi `COUNT(*)` và hàm đếm giá trị khác null `COUNT(tên_cột)` khi xử lý dữ liệu lưu trữ dưới định dạng Parquet.

**Dữ liệu đầu vào**: Tệp dữ liệu chỗ ở Parquet `listings.parquet` chứa các cột `room_type` và `first_review`.

**Thao tác yêu cầu**:
1. Triển khai hàm `sql_count_listings_and_reviews(parquet_path) -> pd.DataFrame` thực hiện truy vấn SQL trên tệp Parquet.
2. Với từng loại phòng `room_type`, tính toán hai đại lượng thống kê:
   - Tổng số chỗ ở: `COUNT(*) AS so_cho_o`.
   - Số lượng chỗ ở đã từng nhận ít nhất một đánh giá: `COUNT(first_review) AS so_co_danh_gia`.
3. Sắp xếp kết quả giảm dần theo tổng số chỗ ở `so_cho_o`, nếu bằng nhau thì sắp tăng dần theo `room_type`.

**Trường hợp biên cần chú ý**:
- Những chỗ ở mới niêm yết chưa có khách đánh giá sẽ có giá trị cột `first_review` là `NULL`. Hàm `COUNT(first_review)` phải bỏ qua các giá trị `NULL` này.
:::

::: solution
#### Cách 1: Đếm dòng và đếm giá trị không khuyết trong SQL

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL.to_csv("listings_full.csv", index=False)

cot_can_doc = ["id", "room_type", "price", "first_review", "number_of_reviews"]

cot_ngay = ["first_review"]


def read_selected(path, columns: list, date_columns: list) -> pd.DataFrame:
    # Đọc tệp có chọn lọc cột và chuyển đổi ngày giờ
    df = pd.read_csv(
        path, usecols=columns, parse_dates=date_columns if date_columns else False
    )
    return df


bang_chon_loc = read_selected("listings_full.csv", cot_can_doc, cot_ngay)

# Bắt đầu lời giải


def sql_count_listings_and_reviews(parquet_path) -> pd.DataFrame:
    tep_posix = Path(parquet_path).as_posix()

    cau_lenh = f"""
    SELECT room_type,
           COUNT(*) AS so_cho_o,
           COUNT(first_review) AS so_co_danh_gia
    FROM '{tep_posix}'
    GROUP BY room_type
    ORDER BY so_cho_o DESC, room_type ASC
    """
    return duckdb.sql(cau_lenh).df()


# Chuẩn bị tệp Parquet mẫu từ bảng chỗ ở
bang_chon_loc.to_parquet("listings.parquet", index=False)
thong_ke_loai_cho = sql_count_listings_and_reviews("listings.parquet")
print("Kết quả thống kê loại chỗ ở và đánh giá:")
print(thong_ke_loai_cho)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`COUNT(*)` đếm tất cả dòng của mỗi loại phòng. `COUNT(first_review)` chỉ đếm dòng có ô `first_review` khác `NULL`. Với fixture này, loại `Private room` có hai chỗ ở nhưng chỉ một ngày đánh giá đầu tiên đã biết, nên hai số đếm lần lượt là 2 và 1.

Tệp Parquet được tạo từ bảng đã phân tích cột ngày. Ô ngày thiếu thành `NaT` trong pandas và được lưu thành giá trị null có thể đếm đúng trong DuckDB. Nếu lưu chuỗi rỗng thay cho null, `COUNT(cột)` có thể đếm nó là một giá trị, vì vậy bước nạp và chuẩn hóa dữ liệu có ảnh hưởng trực tiếp đến kết quả.

`GROUP BY room_type` tạo một dòng cho mỗi loại. `ORDER BY so_cho_o DESC, room_type ASC` xếp loại có nhiều chỗ ở trước và dùng tên làm tiêu chí phụ khi hòa. Việc gọi trực tiếp tệp Parquet vẫn có đọc dữ liệu và giải mã theo nhu cầu truy vấn, không có nghĩa mọi khối nén đều được dùng nguyên trạng.

##### Output Cách 1

| `room_type` | `so_cho_o` | `so_co_danh_gia` |
|---|---|---|
| Entire home/apt | 4 | 4 |
| Private room | 2 | 1 |

#### Cách 2: Tạo view để đặt tên nguồn rồi tổng hợp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL.to_csv("listings_full.csv", index=False)

cot_can_doc = ["id", "room_type", "price", "first_review", "number_of_reviews"]

cot_ngay = ["first_review"]


def read_selected(path, columns: list, date_columns: list) -> pd.DataFrame:
    # Đọc tệp có chọn lọc cột và chuyển đổi ngày giờ
    df = pd.read_csv(
        path, usecols=columns, parse_dates=date_columns if date_columns else False
    )
    return df


bang_chon_loc = read_selected("listings_full.csv", cot_can_doc, cot_ngay)

bang_chon_loc.to_parquet("listings.parquet", index=False)


def sql_count_listings_and_reviews(parquet_path) -> pd.DataFrame:
    tep_posix = Path(parquet_path).as_posix()

    cau_lenh = f"""
    SELECT room_type,
           COUNT(*) AS so_cho_o,
           COUNT(first_review) AS so_co_danh_gia
    FROM '{tep_posix}'
    GROUP BY room_type
    ORDER BY so_cho_o DESC, room_type ASC
    """
    return duckdb.sql(cau_lenh).df()


thong_ke_loai_cho = sql_count_listings_and_reviews("listings.parquet")

# Bắt đầu lời giải


def sql_count_listings_and_reviews_v2(parquet_path) -> pd.DataFrame:
    con = duckdb.connect()
    duong_dan_chuan = Path(parquet_path).resolve().as_posix()

    # Đăng ký khung nhìn tạm thời từ tệp Parquet
    con.execute(
        f"CREATE VIEW v_listings AS SELECT * FROM read_parquet('{duong_dan_chuan}')"
    )

    truy_van = """
    SELECT room_type,
           COUNT(*) AS so_cho_o,
           COUNT(first_review) AS so_co_danh_gia
    FROM v_listings
    GROUP BY room_type
    ORDER BY so_cho_o DESC, room_type ASC
    """
    ket_qua = con.execute(truy_van).df()
    con.close()
    return ket_qua


# Thực thi mẫu phương pháp thứ hai
thong_ke_loai_cho_v2 = sql_count_listings_and_reviews_v2("listings.parquet")
print("Kiểm tra tính trùng khớp:", thong_ke_loai_cho.equals(thong_ke_loai_cho_v2))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`CREATE VIEW v_listings AS SELECT * FROM read_parquet(...)` đặt tên cho một câu truy vấn đọc tệp. View không tự tạo một bản sao dữ liệu được vật chất hóa. Những truy vấn sau có thể dùng tên `v_listings` để tránh lặp lại đường dẫn và cấu trúc nguồn.

Hai biểu thức `COUNT` vẫn giữ nguyên ý nghĩa như Cách 1. Sử dụng view giúp tách phần khai báo nguồn với phần phân tích, chứ không tự làm số đếm nhanh hơn. `.execute(...).df()` chạy truy vấn rồi lấy DataFrame, sau đó đóng kết nối cục bộ.

Hiệu `so_cho_o - so_co_danh_gia` cho biết số dòng thiếu ngày đánh giá đầu tiên. Trong fixture được dựng theo quy ước của bài, dòng đó là chỗ ở chưa có đánh giá. Khi dùng dữ liệu ngoài, cần kiểm tra quy ước của cột trước khi suy ra thiếu ngày đồng nghĩa chắc chắn chưa từng có đánh giá.

##### Output Cách 2

| `room_type` | `so_cho_o` | `so_co_danh_gia` |
|---|---|---|
| Entire home/apt | 4 | 4 |
| Private room | 2 | 1 |

Kiểm tra giữa hai bảng in `True`. Tổng toàn mẫu là 6 chỗ ở và 5 ô ngày đánh giá đầu tiên không khuyết.

#### So sánh hai cách

Cách 1 dễ theo dõi cho một truy vấn. Cách 2 hữu ích khi nhiều phép phân tích dùng chung một nguồn. Điểm cần nắm là `COUNT(*)` đếm dòng, `COUNT(cột)` đếm ô không null. Chúng có thể bằng nhau hoặc khác nhau tùy đúng cột và dữ liệu đang xét.

:::

---

## Bài 9: Ghép nối bảng DuckDB bằng phép JOIN và phân bổ đánh giá theo loại phòng

<span id="data-lab-06-09"></span>

::: exercise
**Mục tiêu**: Thực hiện phép ghép nối quan hệ (JOIN) giữa tệp đánh giá và tệp chỗ ở trực tiếp trong DuckDB để phân tích cơ cấu đánh giá theo loại phòng trong một năm cụ thể.

**Dữ liệu đầu vào**:
- Đường dẫn tệp đánh giá `reviews_path` (chứa `listing_id` và `date`).
- Đường dẫn tệp chỗ ở `listings_path` (chứa `id` và `room_type`).
- Năm phân tích `nam` (số nguyên, ví dụ `2025`).

**Thao tác yêu cầu**:
1. Triển khai hàm `sql_reviews_by_room_type(reviews_path, listings_path, nam: int) -> pd.DataFrame` thực hiện phép `INNER JOIN` giữa bảng đánh giá và bảng chỗ ở theo điều kiện khóa định danh.
2. Lọc các đánh giá có `year(date) = nam`.
3. Gom nhóm theo `room_type`, đếm số lượng đánh giá `count(*) AS n`.
4. Sắp xếp kết quả giảm dần theo `n`, trường hợp bằng nhau sắp tăng dần theo `room_type`.

**Trường hợp biên cần chú ý**:
- Ép kiểu tường minh khóa ghép nối giữa hai bảng: Mã chỗ ở có thể được lưu trữ dưới dạng chuỗi hoặc số nguyên lớn. Cần bảo đảm kiểu tương thích khi ghép nối bằng cú pháp `CAST(r.listing_id AS BIGINT) = CAST(l.id AS BIGINT)`.
- Các đánh giá thuộc về mã chỗ ở không tồn tại trong danh mục chỗ ở (như mã `99` trong dữ liệu mẫu) sẽ tự động bị loại bỏ trong phép ghép trong `INNER JOIN`.
:::

::: solution
#### Cách 1: Ghép từng đánh giá với loại phòng rồi đếm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_REVIEWS.to_csv("reviews.csv", index=False)

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL[["id", "name", "room_type"]].to_csv("listings.csv", index=False)

# Bắt đầu lời giải


def sql_reviews_by_room_type(reviews_path, listings_path, nam: int) -> pd.DataFrame:
    r_posix = Path(reviews_path).as_posix()
    l_posix = Path(listings_path).as_posix()

    cau_lenh = f"""
    SELECT l.room_type, count(*) AS n
    FROM '{r_posix}' r
    JOIN '{l_posix}' l ON CAST(r.listing_id AS BIGINT) = CAST(l.id AS BIGINT)
    WHERE year(r.date) = {nam}
    GROUP BY l.room_type
    ORDER BY n DESC, l.room_type ASC
    """
    return duckdb.sql(cau_lenh).df()


# Thực thi mẫu với năm 2025
danh_gia_theo_phong = sql_reviews_by_room_type("reviews.csv", "listings.csv", 2025)
print("Phân bổ đánh giá năm 2025 theo loại phòng:")
print(danh_gia_theo_phong)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`JOIN` trong câu SQL là `INNER JOIN`. Một đánh giá chỉ đi vào bảng ghép khi `r.listing_id` tìm được `l.id`. `CAST(... AS BIGINT)` đưa hai khóa về cùng kiểu số nguyên trước khi so, với giả thiết các mã đều chuyển được thành số.

`WHERE year(r.date) = nam` giữ đánh giá thuộc năm cần phân tích. `GROUP BY l.room_type` gom các đánh giá ghép được theo loại phòng, rồi `COUNT(*)` đếm số dòng đánh giá trong từng loại. Nếu một chỗ ở có nhiều đánh giá thì các đánh giá đều được đếm, không phải chỉ đếm một chỗ ở.

Trong năm 2025 có 40 đánh giá mẫu. Bốn đánh giá dùng mã 99 không có trong bảng chỗ ở nên bị bỏ bởi phép ghép trong. Kết quả còn 36 đánh giá, với 27 nguyên căn và 9 phòng riêng. Để số đếm không bị nhân lên, cần kiểm tra `id` duy nhất trong bảng chỗ ở trước khi ghép.

##### Output Cách 1

| `room_type` | `n` | Tỷ lệ trong 36 đánh giá ghép được |
|---|---|---|
| Entire home/apt | 27 | 75% |
| Private room | 9 | 25% |

#### Cách 2: Tách lọc năm và chuẩn hóa khóa thành các CTE

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_REVIEWS.to_csv("reviews.csv", index=False)

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL[["id", "name", "room_type"]].to_csv("listings.csv", index=False)


def sql_reviews_by_room_type(reviews_path, listings_path, nam: int) -> pd.DataFrame:
    r_posix = Path(reviews_path).as_posix()
    l_posix = Path(listings_path).as_posix()

    cau_lenh = f"""
    SELECT l.room_type, count(*) AS n
    FROM '{r_posix}' r
    JOIN '{l_posix}' l ON CAST(r.listing_id AS BIGINT) = CAST(l.id AS BIGINT)
    WHERE year(r.date) = {nam}
    GROUP BY l.room_type
    ORDER BY n DESC, l.room_type ASC
    """
    return duckdb.sql(cau_lenh).df()


danh_gia_theo_phong = sql_reviews_by_room_type("reviews.csv", "listings.csv", 2025)

# Bắt đầu lời giải


def sql_reviews_by_room_type_v2(reviews_path, listings_path, nam: int) -> pd.DataFrame:
    con = duckdb.connect()
    r_str = Path(reviews_path).resolve().as_posix()
    l_str = Path(listings_path).resolve().as_posix()

    truy_van = f"""
    WITH reviews_nam AS (
        SELECT CAST(listing_id AS BIGINT) AS listing_id
        FROM read_csv_auto('{r_str}')
        WHERE year(date) = {nam}
    ),
    listings_chuan AS (
        SELECT CAST(id AS BIGINT) AS id, room_type
        FROM read_csv_auto('{l_str}')
    )
    SELECT l.room_type, COUNT(*) AS n
    FROM reviews_nam r
    JOIN listings_chuan l ON r.listing_id = l.id
    GROUP BY l.room_type
    ORDER BY n DESC, l.room_type ASC
    """
    ket_qua = con.execute(truy_van).df()
    con.close()
    return ket_qua


# Thực thi mẫu phương pháp thứ hai
danh_gia_v2 = sql_reviews_by_room_type_v2("reviews.csv", "listings.csv", 2025)
print("Kiểm tra tính trùng khớp:", danh_gia_theo_phong.equals(danh_gia_v2))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`WITH reviews_nam AS (...)` đặt tên cho phần đánh giá đã lọc theo năm. `listings_chuan` chỉ lấy khóa và loại phòng cần dùng. Truy vấn chính sau đó ghép hai nguồn này và tổng hợp giống Cách 1. Các tên trung gian giúp đọc rõ quy trình mà không phải tạo các bảng pandas.

CTE là cách tổ chức câu SQL, chưa phải bằng chứng rằng DuckDB sẽ tạo bảng tạm hay chạy nhanh hơn. Bộ tối ưu có thể đẩy điều kiện lọc trong Cách 1 xuống trước phép ghép. Muốn biết kế hoạch thật, cần dùng `EXPLAIN` trên dữ liệu và phiên bản đang chạy.

`ORDER BY n DESC, l.room_type ASC` làm kết quả ổn định khi hai loại có cùng số đếm. Giá trị tỷ lệ trong bảng minh họa dùng mẫu số 36 là tổng số đánh giá ghép được, không dùng 40 và cũng không dùng sáu chỗ ở.

##### Output Cách 2

| `room_type` | `n` | Tỷ lệ trong 36 đánh giá ghép được |
|---|---|---|
| Entire home/apt | 27 | 75% |
| Private room | 9 | 25% |

Lệnh so sánh hai cách trả `True`. Có 4 trong 40 đánh giá năm 2025 không ghép được danh mục chỗ ở.

#### So sánh hai cách

Cách 1 thể hiện trực tiếp quan hệ hai bảng. Cách 2 dễ mở rộng khi cần nhiều bước lọc hoặc chuẩn hóa. Cả hai đang đếm đánh giá, nên tỷ trọng không thể diễn giải thành tỷ lệ đặt phòng, công suất sử dụng hoặc mức hài lòng. Số đánh giá bị loại do thiếu khóa cũng cần được báo cùng kết quả.

:::

---

## Bài 10: Lọc nhóm bằng mệnh đề HAVING trong DuckDB và kiểm chứng bằng pandas

<span id="data-lab-06-10"></span>

::: exercise
**Mục tiêu**: Phân biệt cơ chế lọc dòng bằng `WHERE` và cơ chế lọc nhóm sau tổng hợp bằng `HAVING` trong SQL, đồng thời đối chiếu kiểm chứng chéo kết quả truy vấn với công cụ phân tích pandas.

**Dữ liệu đầu vào**:
- Đường dẫn tệp đánh giá `reviews_path`.
- Năm lọc dữ liệu `nam` (ví dụ `2025`).
- Ngưỡng số lượng đánh giá tối thiểu `threshold` (ví dụ `5`).

**Thao tác yêu cầu**:
1. Triển khai hàm `sql_active_listings_having(reviews_path, nam: int, threshold: int) -> pd.DataFrame` sử dụng DuckDB.
2. Viết câu truy vấn lọc từng dòng theo năm bằng `WHERE year(date) = nam`, gom nhóm theo `listing_id` bằng `GROUP BY`, sau đó lọc các nhóm có số lượng đánh giá thỏa mãn `HAVING count(*) >= threshold`.
3. Sắp xếp kết quả giảm dần theo số lượng đánh giá `n`, nếu bằng nhau sắp tăng dần theo `listing_id`.
4. Viết mã kiểm chứng chéo độc lập bằng pandas sử dụng phương thức `value_counts()`.

**Trường hợp biên cần chú ý**:
- Mệnh đề `WHERE` chỉ lọc các bản ghi trước khi thực hiện gom nhóm, do đó không được đưa các hàm tổng hợp như `count(*)` vào mệnh đề `WHERE`.
- Ép kiểu cột `listing_id` sang số nguyên lớn `BIGINT` để bảo đảm tính nhất quán định dạng đầu ra.
:::

::: solution
#### Cách 1: Lọc dòng bằng WHERE rồi lọc nhóm bằng HAVING

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_REVIEWS.to_csv("reviews.csv", index=False)

# Bắt đầu lời giải


def sql_active_listings_having(reviews_path, nam: int, threshold: int) -> pd.DataFrame:
    r_posix = Path(reviews_path).as_posix()

    cau_lenh = f"""
    SELECT CAST(listing_id AS BIGINT) AS listing_id, count(*) AS n
    FROM '{r_posix}'
    WHERE year(date) = {nam}
    GROUP BY listing_id
    HAVING count(*) >= {threshold}
    ORDER BY n DESC, listing_id ASC
    """
    return duckdb.sql(cau_lenh).df()


# Thực thi mẫu tìm các chỗ ở có từ 5 đánh giá trở lên trong năm 2025
cho_o_tich_cuc = sql_active_listings_having("reviews.csv", 2025, 5)
print("Các chỗ ở có từ 5 đánh giá trở lên:")
print(cho_o_tich_cuc)

# Kiểm chứng chéo độc lập bằng pandas
dem_pandas = DEMO_REVIEWS.loc[
    DEMO_REVIEWS["date"].dt.year == 2025, "listing_id"
].value_counts()
cho_o_pandas = dem_pandas[dem_pandas >= 5].reset_index()
cho_o_pandas.columns = ["listing_id", "n"]
print("Kiểm chứng khớp với pandas:", cho_o_tich_cuc.equals(cho_o_pandas))

# Kết thúc lời giải
```

##### Giải thích Cách 1

`WHERE year(date) = nam` xét từng dòng trước khi tổng hợp. Sau `GROUP BY listing_id`, mỗi nhóm đại diện cho một mã chỗ ở. `HAVING COUNT(*) >= threshold` xét số dòng của cả nhóm, nên đúng nơi để yêu cầu ít nhất năm đánh giá.

Không thể đặt `COUNT(*) >= 5` vào `WHERE` của cùng cấp truy vấn vì tại bước lọc dòng chưa có các nhóm để đếm. `ORDER BY n DESC, listing_id ASC` quy định thứ tự giảm dần theo số đánh giá và tăng dần theo mã khi hòa.

Phần kiểm chứng pandas lấy cột mã của các đánh giá năm 2025, gọi `value_counts`, lọc số đếm đạt ngưỡng và đổi tên hai cột. Trên fixture, kết quả khớp SQL. Với dữ liệu có các nhóm hòa số đếm, cần sắp cả tiêu chí phụ phía pandas trước khi dùng `.equals`, vì cùng giá trị nhưng khác thứ tự dòng cũng có thể cho kết quả `False`.

##### Output Cách 1

| `listing_id` | `n` |
|---|---|
| 11 | 14 |
| 12 | 9 |
| 13 | 5 |

Kiểm chứng pandas trên fixture trả `True`. Mã 99 vẫn có thể được tính ở bài này vì chưa ghép với danh mục chỗ ở, nhưng không đạt ngưỡng 5.

#### Cách 2: Tổng hợp trong truy vấn con rồi lọc cột n

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_REVIEWS.to_csv("reviews.csv", index=False)


def sql_active_listings_having(reviews_path, nam: int, threshold: int) -> pd.DataFrame:
    r_posix = Path(reviews_path).as_posix()

    cau_lenh = f"""
    SELECT CAST(listing_id AS BIGINT) AS listing_id, count(*) AS n
    FROM '{r_posix}'
    WHERE year(date) = {nam}
    GROUP BY listing_id
    HAVING count(*) >= {threshold}
    ORDER BY n DESC, listing_id ASC
    """
    return duckdb.sql(cau_lenh).df()


cho_o_tich_cuc = sql_active_listings_having("reviews.csv", 2025, 5)

# Bắt đầu lời giải


def sql_active_listings_having_v2(
    reviews_path, nam: int, threshold: int
) -> pd.DataFrame:
    r_posix = Path(reviews_path).as_posix()

    cau_lenh = f"""
    SELECT listing_id, n
    FROM (
        SELECT CAST(listing_id AS BIGINT) AS listing_id, count(*) AS n
        FROM '{r_posix}'
        WHERE year(date) = {nam}
        GROUP BY listing_id
    ) tong_hop
    WHERE n >= {threshold}
    ORDER BY n DESC, listing_id ASC
    """
    return duckdb.sql(cau_lenh).df()


# Thực thi mẫu phương pháp thứ hai
cho_o_tich_cuc_v2 = sql_active_listings_having_v2("reviews.csv", 2025, 5)
print("Kiểm tra tính đồng nhất:", cho_o_tich_cuc.equals(cho_o_tich_cuc_v2))

# Kết thúc lời giải
```

##### Giải thích Cách 2

Truy vấn con tính `COUNT(*) AS n` cho mỗi chỗ ở trong năm. Ở truy vấn bao ngoài, mỗi dòng đầu vào đã là một nhóm được tổng hợp. Vì vậy `WHERE n >= threshold` của cấp ngoài là hợp lệ và có cùng ý nghĩa lọc nhóm với `HAVING` ở Cách 1.

Tên `tong_hop` là bí danh của bảng con, giúp phân biệt hai cấp truy vấn. Đưa điều kiện lọc năm vào cấp trong bảo đảm số đếm chỉ chứa đánh giá của năm cần lấy. Nếu lọc sai cấp hoặc bỏ điều kiện này, số đếm có thể gộp cả nhiều năm.

Hai dạng SQL đều giao việc tổng hợp cho DuckDB. Truy vấn con hữu ích khi điều kiện tiếp theo phải dùng nhiều cột tính được. Nó không tự giảm chi phí tính đếm vì bộ tối ưu có thể chọn kế hoạch tương tự cho cả hai cách.

##### Output Cách 2

| `listing_id` | `n` |
|---|---|
| 11 | 14 |
| 12 | 9 |
| 13 | 5 |

Bản in `Kiểm tra tính đồng nhất` giữa hai truy vấn là `True`.

#### So sánh hai cách

Cách 1 là dạng viết trực tiếp cho điều kiện trên nhóm. Cách 2 giúp nhìn rõ ranh giới giữa bảng đã tổng hợp và dữ liệu gốc. Chọn cách dễ bảo trì cho câu truy vấn đang có. Khi kiểm chứng bằng pandas, phải kiểm tra cả kiểu, thứ tự cột và thứ tự dòng trước khi kết luận hai kết quả khác nhau.

:::

---

## Bài 11: Bài mở rộng 1: Phân tích so sánh chuỗi thời tiết và đánh giá tháng 7

<span id="data-lab-06-11"></span>

::: exercise
**Mục tiêu**: Tái lập toàn bộ quy trình thu thập và ghép nối dữ liệu cho một khoảng thời gian đối chứng: Tháng 07 năm 2025 (mùa đông tại bán cầu Nam), đồng thời so sánh mức nhiệt độ và tính ổn định của mối liên hệ với tháng 01.

**Dữ liệu đầu vào**:
- Từ điển phản hồi thời tiết giả lập tháng 7 `DEMO_WEATHER_JULY` (nhiệt độ dao động thấp trong khoảng 11–16°C).
- Tập dữ liệu đánh giá giả lập tháng 7 `DEMO_REVIEWS_JULY`. Ngày đánh giá không được coi là ngày đặt phòng hoặc ngày lưu trú.

**Thao tác yêu cầu**:
1. Triển khai hàm `compare_july_weather_reviews(weather_payload: dict, rv: pd.DataFrame, start: str, end: str) -> dict` kết hợp các hàm đã xây dựng ở Bài 4, 5, 6.
2. Trích xuất bảng thời tiết, đếm đánh giá theo ngày, ghép nối bằng `LEFT JOIN` và đo lường hệ số tương quan tuyến tính.
3. So sánh mức nhiệt độ trung bình và số lượng ngày khuyết giữa tháng 1 và tháng 7.

**Trường hợp biên cần chú ý**:
- Nếu số lượng ngày quan sát có đánh giá nhỏ hơn 2, phép tính tương quan không thể thực hiện và phải trả về `NaN`.
:::

::: solution
#### Cách 1: Lặp lại quy trình ghép cho mười ngày tháng 7

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)


def reviews_per_day(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    # Bản sao an toàn để tránh cảnh báo Copy-on-Write
    du_lieu = rv.copy()
    ngay_bat_dau = pd.to_datetime(start)
    ngay_ket_thuc = pd.to_datetime(end)

    # Bước 1: Lọc các dòng nằm trong khoảng ngày yêu cầu
    dieu_kien = (du_lieu["date"] >= ngay_bat_dau) & (du_lieu["date"] <= ngay_ket_thuc)
    du_lieu_loc = du_lieu.loc[dieu_kien]

    # Bước 2: Gom nhóm theo chuỗi ngày và đếm số lượng
    chuoi_ngay = du_lieu_loc["date"].dt.strftime("%Y-%m-%d")
    dem_ngay = du_lieu_loc.groupby(chuoi_ngay).size().reset_index(name="so_review")

    # Bước 3: Đổi tên cột đồng nhất và sắp xếp thời gian tăng dần
    ket_qua = (
        dem_ngay.rename(columns={"date": "time"})
        .sort_values("time")
        .reset_index(drop=True)
    )
    return ket_qua


thong_ke_ngay = reviews_per_day(DEMO_REVIEWS, "2025-01-01", "2025-01-10")

# Bắt đầu lời giải

# Khởi tạo fixture đối chứng tháng 7
DEMO_WEATHER_JULY = {
    "latitude": -33.45,
    "longitude": -70.66,
    "timezone": "America/Santiago",
    "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
    "daily": {
        "time": [f"2025-07-{d:02d}" for d in range(1, 11)],
        "temperature_2m_max": [
            14.2,
            13.5,
            15.0,
            12.8,
            11.4,
            13.9,
            14.7,
            16.1,
            12.0,
            13.3,
        ],
    },
}

DEMO_REVIEWS_JULY = pd.DataFrame(
    {
        "listing_id": [11, 12, 11, 13, 14, 11, 15, 12, 13, 11, 12, 14],
        "date": pd.to_datetime(
            [
                "2025-07-01",
                "2025-07-01",
                "2025-07-02",
                "2025-07-03",
                "2025-07-04",
                "2025-07-04",
                "2025-07-06",
                "2025-07-07",
                "2025-07-08",
                "2025-07-09",
                "2025-07-09",
                "2025-07-10",
            ]
        ),
    }
)


def compare_july_weather_reviews(
    weather_payload: dict, rv: pd.DataFrame, start: str, end: str
) -> dict:
    # 1. Trích xuất bảng thời tiết
    b_thoi_tiet = pd.DataFrame(weather_payload["daily"])

    # 2. Đếm số lượng đánh giá theo ngày
    b_danh_gia = reviews_per_day(rv, start, end)

    # 3. Ghép nối trái
    b_gop = b_thoi_tiet.merge(b_danh_gia, on="time", how="left")
    so_thieu = int(b_gop["so_review"].isna().sum())

    # 4. Tính toán hệ số tương quan
    co_du_lieu = b_gop.dropna(subset=["temperature_2m_max", "so_review"])
    if len(co_du_lieu) > 1:
        he_so = float(co_du_lieu["temperature_2m_max"].corr(co_du_lieu["so_review"]))
    else:
        he_so = float("nan")

    return {
        "bang_thoi_tiet": b_thoi_tiet,
        "bang_danh_gia": b_danh_gia,
        "gop": b_gop,
        "so_ngay_thieu": so_thieu,
        "he_so_tuong_quan": he_so,
    }


# Thực thi mẫu phân tích tháng 7
ket_qua_thang_7 = compare_july_weather_reviews(
    DEMO_WEATHER_JULY, DEMO_REVIEWS_JULY, "2025-07-01", "2025-07-10"
)
print(
    "Nhiệt độ tối đa trung bình tháng 7:",
    round(ket_qua_thang_7["bang_thoi_tiet"]["temperature_2m_max"].mean(), 2),
)
print("Số ngày khuyết đánh giá tháng 7:", ket_qua_thang_7["so_ngay_thieu"])
print("Hệ số tương quan tháng 7:", round(ket_qua_thang_7["he_so_tuong_quan"], 3))

# Kết thúc lời giải
```

##### Giải thích Cách 1

`pd.DataFrame(weather_payload["daily"])` dựng bảng nhiệt độ theo ngày. `reviews_per_day` tái sử dụng quy tắc đếm của Bài 5. Ghép trái theo `time` giữ toàn bộ mười ngày thời tiết và để số đánh giá khuyết khi ngày đó không có trong bảng đếm.

`dropna` chọn các cặp đủ hai giá trị để tính `.corr()`. Điều kiện hơn một dòng chỉ kiểm tra số cặp tối thiểu, chưa bảo đảm tương quan xác định nếu một biến là hằng số. Với fixture tháng 7, còn chín cặp và hệ số làm tròn là `-0.576`.

Nhiệt độ tối đa trung bình `13.69 °C` được tính trên toàn bộ mười ngày thời tiết. Số đánh giá có tổng 12, còn hệ số chỉ dùng chín ngày có số đếm. Ba đại lượng không có cùng tập dòng tính toán, vì vậy cần nêu rõ mẫu số và quy tắc khuyết cho từng chỉ số.

##### Output Cách 1

| `time` | Nhiệt độ tối đa (°C) | `so_review` |
|---|---|---|
| 2025-07-01 | 14.2 | 2 |
| 2025-07-02 | 13.5 | 1 |
| 2025-07-03 | 15 | 1 |
| 2025-07-04 | 12.8 | 2 |
| 2025-07-05 | 11.4 | `NaN` |
| 2025-07-06 | 13.9 | 1 |
| 2025-07-07 | 14.7 | 1 |
| 2025-07-08 | 16.1 | 1 |
| 2025-07-09 | 12 | 2 |
| 2025-07-10 | 13.3 | 1 |

Kết quả in lần lượt là `13.69`, `1` ngày khuyết đánh giá và hệ số `-0.576`.

#### Cách 2: Tổng hợp các kết quả hai kỳ vào một bảng so sánh

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_WEATHER = {
    "latitude": -33.45,
    "longitude": -70.66,
    "timezone": "America/Santiago",
    "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
    "daily": {
        "time": [f"2025-01-{d:02d}" for d in range(1, 11)],
        "temperature_2m_max": [
            31.4,
            33.1,
            29.1,
            32.8,
            30.2,
            30.0,
            28.5,
            31.8,
            30.9,
            27.6,
        ],
    },
}

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_WEATHER_JULY = {
    "latitude": -33.45,
    "longitude": -70.66,
    "timezone": "America/Santiago",
    "daily_units": {"time": "iso8601", "temperature_2m_max": "°C"},
    "daily": {
        "time": [f"2025-07-{d:02d}" for d in range(1, 11)],
        "temperature_2m_max": [
            14.2,
            13.5,
            15.0,
            12.8,
            11.4,
            13.9,
            14.7,
            16.1,
            12.0,
            13.3,
        ],
    },
}

DEMO_REVIEWS_JULY = pd.DataFrame(
    {
        "listing_id": [11, 12, 11, 13, 14, 11, 15, 12, 13, 11, 12, 14],
        "date": pd.to_datetime(
            [
                "2025-07-01",
                "2025-07-01",
                "2025-07-02",
                "2025-07-03",
                "2025-07-04",
                "2025-07-04",
                "2025-07-06",
                "2025-07-07",
                "2025-07-08",
                "2025-07-09",
                "2025-07-09",
                "2025-07-10",
            ]
        ),
    }
)

# Bắt đầu lời giải


def analyze_weather_period(payload, reviews, start, end):
    weather = pd.DataFrame(payload["daily"])
    selected = reviews.loc[reviews["date"].between(start, end)]
    per_day = (
        selected.groupby(selected["date"].dt.strftime("%Y-%m-%d"))
        .size()
        .rename("so_review")
        .rename_axis("time")
        .reset_index()
    )
    joined = weather.merge(per_day, on="time", how="left", validate="one_to_one")
    return {
        "gop": joined,
        "so_thieu": int(joined["so_review"].isna().sum()),
        "he_so": float(joined["temperature_2m_max"].corr(joined["so_review"])),
    }


def summarize_seasonal_comparison(kq_thang1: dict, kq_thang7: dict) -> pd.DataFrame:
    chi_so = [
        "Nhiệt độ tối đa trung bình (°C)",
        "Tổng số lượt đánh giá quan sát",
        "Số ngày khuyết thiếu đánh giá",
        "Hệ số tương quan Pearson",
    ]
    gt_thang1 = [
        round(kq_thang1["gop"]["temperature_2m_max"].mean(), 2),
        int(kq_thang1["gop"]["so_review"].sum()),
        int(kq_thang1["so_thieu"]),
        round(kq_thang1["he_so"], 3),
    ]
    gt_thang7 = [
        round(kq_thang7["gop"]["temperature_2m_max"].mean(), 2),
        int(kq_thang7["gop"]["so_review"].sum()),
        int(kq_thang7["so_thieu"]),
        round(kq_thang7["he_so"], 3),
    ]

    return pd.DataFrame(
        {
            "Chỉ số đối chiếu": chi_so,
            "Tháng 01/2025": gt_thang1,
            "Tháng 07/2025": gt_thang7,
        }
    )


# Thực thi tổng hợp so sánh
thang_mot = analyze_weather_period(
    DEMO_WEATHER, DEMO_REVIEWS, "2025-01-01", "2025-01-10"
)
thang_bay = analyze_weather_period(
    DEMO_WEATHER_JULY, DEMO_REVIEWS_JULY, "2025-07-01", "2025-07-10"
)
bang_so_sanh = summarize_seasonal_comparison(thang_mot, thang_bay)
print("Bảng so sánh hai khoảng dữ liệu giả lập:")
print(bang_so_sanh)

# Kết thúc lời giải
```

##### Giải thích Cách 2

Hàm `summarize_seasonal_comparison` nhận kết quả của hai quy trình đã chạy, lấy cùng bốn chỉ số rồi đặt cạnh nhau. Các khóa `so_thieu`, `he_so` của tháng 1 và `so_ngay_thieu`, `he_so_tuong_quan` của tháng 7 khác tên, nên cần đọc đúng từng từ điển.

`.mean()` lấy trung bình nhiệt độ tối đa trong kỳ. `.sum()` cộng số đánh giá đã ghép, còn số ngày khuyết được lấy từ kết quả kiểm tra. `round` chỉ làm tròn bảng báo cáo. Nó không thay đổi dữ liệu nguồn dùng tính hệ số.

Các nhãn tháng trong bảng giúp phân biệt hai fixture. Hai kỳ chỉ gồm mười ngày mỗi tháng, nên không thể lấy chênh lệch này làm kết luận về cả mùa, khí hậu hoặc hành vi khách du lịch. Hệ số khác nhau cũng không chứng minh khác biệt về quan hệ nhân quả.

##### Output Cách 2

| Chỉ số | 01–10/01/2025 | 01–10/07/2025 |
|---|---|---|
| Trung bình nhiệt độ tối đa (°C) | 30.54 | 13.69 |
| Tổng số đánh giá đã quan sát | 36 | 12 |
| Ngày không ghép được số đếm | 1 | 1 |
| Pearson, làm tròn 3 chữ số | 0.084 | -0.576 |

#### So sánh hai cách

Cách 1 thực hiện phân tích kỳ tháng 7 từ dữ liệu đầu vào. Cách 2 là bước trình bày đối chiếu từ các kết quả đã tính, không phải một thuật toán khác thay thế toàn bộ quy trình. Cả hai đều hữu ích khi học cách chia việc thành hàm, nhưng cần giữ rõ phạm vi mười ngày và dữ liệu giả lập khi diễn giải.

:::

---

## Bài 12: Bài mở rộng 2: Truy vấn top chỗ ở nhận nhiều đánh giá nhất kèm tên định danh

<span id="data-lab-06-12"></span>

::: exercise
**Mục tiêu**: Xây dựng truy vấn phân tích thứ hạng trong DuckDB kết hợp thông tin định danh từ hai bảng quan hệ khác nhau, đồng thời kiểm chứng chéo thứ tự xếp hạng bằng công cụ pandas.

**Dữ liệu đầu vào**:
- Đường dẫn tệp đánh giá `reviews_path`.
- Đường dẫn tệp chỗ ở `listings_path` chứa cột `name` mô tả tên phòng.
- Năm lọc dữ liệu `nam` (ví dụ `2025`).
- Số lượng bản ghi giới hạn `limit` (mặc định lấy 5 chỗ ở đứng đầu).

**Thao tác yêu cầu**:
1. Triển khai hàm `sql_top_reviewed_listings(reviews_path, listings_path, nam: int, limit: int = 5) -> pd.DataFrame` sử dụng DuckDB.
2. Thực hiện ghép `INNER JOIN` giữa bảng đánh giá và bảng chỗ ở.
3. Gom nhóm theo cả hai trường `listing_id` và tên phòng `name`.
4. Đếm số lượng đánh giá, sắp xếp giảm dần theo số đánh giá `n`, nếu bằng nhau sắp tăng dần theo `listing_id`, và giới hạn đầu ra bằng mệnh đề `LIMIT`.

**Trường hợp biên cần chú ý**:
- Chú ý tính tương thích kiểu dữ liệu khi ghép khóa: `listing_id` có thể là chuỗi trong khi `id` là số nguyên.
- Đảm bảo việc gom nhóm bao gồm cả cột tên phòng `name` để câu lệnh SQL tuân thủ đúng chuẩn ANSI SQL.
:::

::: solution
#### Cách 1: Ghép tên chỗ ở và lấy các nhóm đứng đầu bằng SQL

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_REVIEWS.to_csv("reviews.csv", index=False)

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL[["id", "name", "room_type"]].to_csv("listings.csv", index=False)

# Bắt đầu lời giải


def sql_top_reviewed_listings(
    reviews_path, listings_path, nam: int, limit: int = 5
) -> pd.DataFrame:
    r_posix = Path(reviews_path).as_posix()
    l_posix = Path(listings_path).as_posix()

    cau_lenh = f"""
    SELECT CAST(r.listing_id AS BIGINT) AS listing_id,
           l.name,
           count(*) AS n
    FROM '{r_posix}' r
    JOIN '{l_posix}' l ON CAST(r.listing_id AS BIGINT) = CAST(l.id AS BIGINT)
    WHERE year(r.date) = {nam}
    GROUP BY r.listing_id, l.name
    ORDER BY n DESC, listing_id ASC
    LIMIT {limit}
    """
    return duckdb.sql(cau_lenh).df()


# Thực thi mẫu tìm top 5 chỗ ở năm 2025
top_5_cho_o = sql_top_reviewed_listings("reviews.csv", "listings.csv", 2025, 5)
print("Top 5 chỗ ở nhiều đánh giá nhất năm 2025:")
print(top_5_cho_o)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`JOIN` lấy tên ứng với mỗi mã chỗ ở trong các đánh giá năm cần phân tích. `GROUP BY r.listing_id, l.name` tạo nhóm cho từng cặp mã và tên để cả hai trường xuất hiện hợp lệ trong `SELECT`. Giả thiết quan trọng là mỗi id trong danh mục chỉ có một dòng tương ứng.

`COUNT(*) AS n` đếm đánh giá ghép được, rồi `ORDER BY n DESC, listing_id ASC` quy định cả thứ tự chính lẫn phụ. Hai chỗ ở 14 và 15 có cùng bốn đánh giá, nên mã 14 đứng trước. `LIMIT 5` chỉ lấy năm dòng đầu của kết quả đã xếp.

`LIMIT` không có nghĩa DuckDB chỉ đọc năm dòng tệp hay chỉ giữ năm nhóm trong mọi giai đoạn. Hệ quản trị vẫn phải xác định các số đếm để biết nhóm nào đứng đầu. Mã 99 không ghép được nên không thể xuất hiện trong bảng có tên chỗ ở.

##### Output Cách 1

| `listing_id` | `name` | `n` |
|---|---|---|
| 11 | Depto Lastarria | 14 |
| 12 | Pieza Bellavista | 9 |
| 13 | Loft Providencia | 5 |
| 14 | Casa Ñuñoa | 4 |
| 15 | Studio Centro | 4 |

#### Cách 2: Đếm trước trong pandas rồi ghép tên và xếp hạng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pathlib import Path

import duckdb

import pandas as pd

_danh_sach_ngay = []

for ngay, so_luong in zip(
    pd.date_range("2025-01-01", "2025-01-10"), [3, 5, 2, 6, 0, 4, 7, 1, 5, 3]
):
    _danh_sach_ngay += [ngay] * so_luong

_danh_sach_ngay += list(
    pd.to_datetime(
        [
            "2023-03-15",
            "2023-08-02",
            "2023-11-20",
            "2024-02-11",
            "2024-05-05",
            "2024-07-19",
            "2024-09-30",
            "2024-12-24",
            "2024-12-31",
            "2025-03-08",
            "2025-06-21",
            "2025-09-18",
            "2025-12-05",
            "2026-02-14",
            "2026-04-01",
        ]
    )
)

DEMO_REVIEWS = pd.DataFrame(
    {
        "listing_id": [
            [11, 12, 11, 13, 14, 11, 15, 12, 99][k % 9]
            for k in range(len(_danh_sach_ngay))
        ],
        "date": _danh_sach_ngay,
    }
)

DEMO_REVIEWS.to_csv("reviews.csv", index=False)

DEMO_LISTINGS_FULL = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio Centro",
            "Depto nuevo",
        ],
        "host_id": [501, 502, 501, 503, 504, 505],
        "neighbourhood_cleansed": [
            "Santiago",
            "Recoleta",
            "Providencia",
            "Ñuñoa",
            "Santiago",
            "Las Condes",
        ],
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
        ],
        "price": [
            "$45,647.00",
            "$18,500.00",
            "$1,120,000.00",
            None,
            "$59,000.00",
            "$25,990.50",
        ],
        "first_review": [
            "2023-03-15",
            "2023-08-02",
            "2024-02-11",
            "2023-11-20",
            "2025-01-02",
            None,
        ],
        "number_of_reviews": [14, 9, 8, 4, 6, 0],
        "review_scores_rating": [4.91, 4.75, 4.88, 5.0, 4.6, None],
    }
)

DEMO_LISTINGS_FULL[["id", "name", "room_type"]].to_csv("listings.csv", index=False)


def sql_top_reviewed_listings(
    reviews_path, listings_path, nam: int, limit: int = 5
) -> pd.DataFrame:
    r_posix = Path(reviews_path).as_posix()
    l_posix = Path(listings_path).as_posix()

    cau_lenh = f"""
    SELECT CAST(r.listing_id AS BIGINT) AS listing_id,
           l.name,
           count(*) AS n
    FROM '{r_posix}' r
    JOIN '{l_posix}' l ON CAST(r.listing_id AS BIGINT) = CAST(l.id AS BIGINT)
    WHERE year(r.date) = {nam}
    GROUP BY r.listing_id, l.name
    ORDER BY n DESC, listing_id ASC
    LIMIT {limit}
    """
    return duckdb.sql(cau_lenh).df()


top_5_cho_o = sql_top_reviewed_listings("reviews.csv", "listings.csv", 2025, 5)

# Bắt đầu lời giải


def top_reviewed_pandas(
    rv: pd.DataFrame, ls: pd.DataFrame, nam: int, limit: int = 5
) -> pd.DataFrame:
    # 1. Lọc đánh giá theo năm và đếm tần suất
    rv_nam = rv.loc[rv["date"].dt.year == nam].copy()
    dem = rv_nam["listing_id"].value_counts().reset_index()
    dem.columns = ["listing_id", "n"]

    # 2. Ghép nối lấy thông tin tên phòng
    ls_sub = ls[["id", "name"]].rename(columns={"id": "listing_id"})
    gop = dem.merge(ls_sub, on="listing_id", how="inner")

    # 3. Sắp xếp và lấy top đầu
    ket_qua = (
        gop[["listing_id", "name", "n"]]
        .sort_values(by=["n", "listing_id"], ascending=[False, True])
        .head(limit)
        .reset_index(drop=True)
    )

    return ket_qua


# Thực thi kiểm chứng chéo bằng pandas
top_5_pandas = top_reviewed_pandas(DEMO_REVIEWS, DEMO_LISTINGS_FULL, 2025, 5)
print("Kiểm tra khớp giữa DuckDB và pandas:", top_5_cho_o.equals(top_5_pandas))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`rv["date"].dt.year == nam` tạo điều kiện chọn năm. `value_counts` thu cột mã thành bảng số đếm trước khi ghép tên, nên bảng tham gia ghép phía đánh giá chỉ còn một dòng cho mỗi mã. Trên dữ liệu có nhiều đánh giá cho một chỗ ở, đây là một cách giảm kích thước bảng trung gian.

`ls[["id", "name"]]` chỉ lấy hai cột cần tra cứu. `rename` đưa tên khóa `id` về `listing_id`, rồi `merge(..., how="inner")` giữ các mã tìm được tên. `sort_values` nhận hai cột và hai chiều sắp xếp, bảo đảm giữ cùng quy tắc hòa với SQL. `.head(limit)` lấy giới hạn và `reset_index(drop=True)` đặt lại chỉ mục cho bảng kết quả.

Hàm dùng sắp xếp nhiều tiêu chí, không dùng `nlargest`. Đó là điều cần thiết để thể hiện rõ thứ tự mã khi số đếm bằng nhau. Khi đối chiếu với DuckDB, cùng kiểu dữ liệu và cùng thứ tự cột giúp `.equals` kiểm tra được toàn bộ bảng.

##### Output Cách 2

| `listing_id` | `name` | `n` |
|---|---|---|
| 11 | Depto Lastarria | 14 |
| 12 | Pieza Bellavista | 9 |
| 13 | Loft Providencia | 5 |
| 14 | Casa Ñuñoa | 4 |
| 15 | Studio Centro | 4 |

Kiểm tra giữa DuckDB và pandas trên fixture trả `True`.

#### So sánh hai cách

Cách 1 phù hợp khi muốn truy vấn trực tiếp các tệp và chỉ nhận bảng tổng hợp về pandas. Cách 2 mở rõ các bước đếm, ghép và xếp hạng, thuận tiện nếu DataFrame đã có sẵn trong bộ nhớ. Cả hai đòi hỏi quy tắc khóa và tiêu chí hòa giống nhau. Bảng xếp hạng số đánh giá không đồng nghĩa bảng xếp hạng số lượt đặt hoặc chất lượng chỗ ở.

:::
