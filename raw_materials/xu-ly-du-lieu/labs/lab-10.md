## Lab 10: Kiểm tra chất lượng và làm sạch dữ liệu chéo bảng

Hai bảng có thể đọc được nhưng chưa khớp về mã chỗ ở, ngày hoặc cách đếm đánh giá. Ta sẽ lập các phép kiểm, giữ dấu vết dòng bị gắn cờ và phân biệt phát hiện vấn đề với quyết định sửa dữ liệu.

## Bối cảnh và snapshot dữ liệu tham chiếu

Các bài tập thực hành trong bài học này đối chiếu trực tiếp với bộ dữ liệu lưu trữ công cộng của Inside Airbnb đối với thành phố Santiago, Chile:
- **Địa chỉ kho dữ liệu gốc**: `https://data.insideairbnb.com/chile/rm/santiago/`
- **Phiên bản snapshot tham chiếu**: Bản lưu trữ ngày 29 tháng 06 năm 2026 (`2026-06-29/visualisations/listings.csv` và `2026-06-29/visualisations/reviews.csv`).
- **Đơn vị đo lường**: Giá phòng trong bảng chỗ ở được niêm yết bằng đồng Peso Chile (CLP/đêm) làm tròn đến số nguyên, và trong một số kịch bản giá đa kỳ thử nghiệm, giá được quy đổi theo đơn vị USD/đêm.

> [!NOTE]
> **Quy ước dữ liệu mẫu trong Lab 10**: Nhằm phục vụ mục đích kiểm chứng từng bước thuật toán, tính toán nhẩm đối chiếu bằng tay và chạy kiểm thử tức thì trong môi trường tạm thời, tài liệu cung cấp hai bảng dữ liệu mẫu giả lập kích thước nhỏ (`DEMO_DS` gồm 6 chỗ ở và `DEMO_RV` gồm 18 đánh giá). Toàn bộ các hiện tượng thực tế của snapshot lớn (đánh giá sau mốc công bố, trùng cặp mã và ngày, lệch cửa sổ 12 tháng) đều được tái lập hoàn chỉnh trong mẫu nhỏ này. Tuyệt đối không suy diễn các con số thống kê của mẫu nhỏ thành đặc tính của toàn bộ thị trường lưu trú Santiago.

### Khởi tạo môi trường và dữ liệu dùng chung

Toàn bộ các ví dụ và lời giải trong tài liệu sử dụng thư viện pandas và numpy với cấu hình hành vi sao chép an toàn (Copy-on-Write):

```python
import numpy as np
import pandas as pd

# Thiết lập mốc chụp công bố và mốc bắt đầu cửa sổ 12 tháng
MOC = "2026-06-29"
LTM_BAT_DAU = "2025-06-30"

# Bảng đánh giá mẫu giả lập (18 đánh giá, 2 cột listing_id và date)
DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

# Bảng chỗ ở mẫu giả lập (6 chỗ ở, đầy đủ các cột dẫn xuất và ngày đánh giá cuối)
DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)

print(
    "Khởi tạo dữ liệu mẫu thành công: Chỗ ở =",
    len(DEMO_DS),
    ", Đánh giá =",
    len(DEMO_RV),
)
```

Bảng 10.0: Cấu trúc dữ liệu mẫu giả lập của danh sách chỗ ở (`DEMO_DS`):

| id | name | number_of_reviews | number_of_reviews_ltm | last_review |
|---:|:---|---:|---:|:---|
| 11 | Depto Lastarria | 7 | 4 | 2026-06-30 |
| 12 | Pieza Bellavista | 4 | 2 | 2026-07-01 |
| 13 | Loft Providencia | 4 | 1 | 2025-07-01 |
| 14 | Casa Ñuñoa | 2 | 2 | 2026-06-30 |
| 15 | Studio nuevo | 0 | 0 | NaT |
| 16 | Hab Centro | 1 | 0 | 2021-02-02 |

---

## Bài 1: Điền khuyết có căn cứ cho biến đếm tần suất và so sánh với điểm đánh giá

<span id="data-lab-10-01"></span>

::: exercise
**Mục tiêu**: Phân tích bản chất nghiệp vụ của biến đếm tần suất đánh giá trung bình mỗi tháng (`reviews_per_month`), thực hiện điền khuyết giá trị 0 có căn cứ logic vững chắc khi số lượt đánh giá bằng 0, bảo toàn chỉ mục ban đầu và không làm thay đổi bảng dữ liệu gốc. Đối chiếu với nguyên tắc không điền 0 cho biến đo lường chất lượng (điểm đánh giá chỗ ở).

**Dữ liệu đầu vào**: Bảng dữ liệu chỗ ở thử nghiệm `ds_demo_rpm` gồm 4 chỗ ở:
- Chỗ ở 1 và 3 chưa từng có lượt đánh giá nào (`number_of_reviews == 0`), cột `reviews_per_month` đang nhận giá trị `NaN`.
- Chỗ ở 2 có 5 lượt đánh giá với tần suất đã biết 1.45 đánh giá/tháng.
- Chỗ ở 4 có 2 lượt đánh giá nhưng cột `reviews_per_month` bị khuyết do lỗi trích xuất dữ liệu.

**Thao tác yêu cầu**:
1. Xây dựng hàm tạo Series `rpm` từ cột `reviews_per_month`, điền giá trị 0.0 cho các chỗ ở có `number_of_reviews` bằng 0.
2. Giữ nguyên chỉ mục ban đầu của bảng, tuyệt đối không chỉnh sửa bảng dữ liệu đầu vào.
3. Bảo toàn nguyên vẹn giá trị `NaN` tại chỗ ở 4 (chỗ ở đã có đánh giá nhưng thiếu số liệu tần suất).
4. Phân tích nguyên nhân vì sao việc điền 0 là hợp lý đối với biến tần suất nhưng không được phép áp dụng đối với điểm đánh giá sao (review rating score).

**Trường hợp biên cần chú ý**: Phải giữ nguyên chỉ mục của DataFrame đầu vào, kể cả khi chỉ mục không liên tục hoặc là dạng chuỗi ký tự.
:::

::: solution
#### Cách 1: Sử dụng phép gán trên bản sao chỉ mục điều kiện

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

# Bắt đầu lời giải


def dien_rpm_co_can_cu_buoc(ds: pd.DataFrame) -> pd.Series:
    """Điền 0 cho reviews_per_month khi number_of_reviews bằng 0 theo cách tuần tự.

    Tham số:
        ds: DataFrame chứa cột 'number_of_reviews' và 'reviews_per_month'.
    Trả về:
        Series kiểu số thực cùng chỉ mục với ds, đã được điền 0 có căn cứ logic.
    """
    rpm = ds["reviews_per_month"].copy()
    chua_co_danh_gia = ds["number_of_reviews"].eq(0)
    rpm.loc[chua_co_danh_gia] = 0.0
    return rpm


# Dữ liệu thử nghiệm minh họa
ds_demo_rpm = pd.DataFrame(
    {
        "id": [11, 12, 13, 14],
        "number_of_reviews": [0, 5, 0, 2],
        "reviews_per_month": [np.nan, 1.45, np.nan, np.nan],
    },
    index=["N1", "N2", "N3", "N4"],
)

rpm_ket_qua_c1 = dien_rpm_co_can_cu_buoc(ds_demo_rpm)
print("Kết quả điền khuyết Cách 1:")
print(rpm_ket_qua_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Tạo bản sao của cột trước khi gán để giữ dữ liệu gốc. Mặt nạ chỉ chọn chỗ ở có số đánh giá bằng 0 và tốc độ đánh giá đang thiếu. Điền 0 ở đúng các dòng đó theo giả thiết của bài, không lan sang dòng đã có đánh giá hoặc mọi cột giá trị thiếu.

#### Kết quả cách 1

| Chỉ mục | reviews_per_month |
| --- | --- |
| N1 | 0 |
| N2 | 1.45 |
| N3 | 0 |
| N4 | NaN |

#### Cách 2: Sử dụng phương thức mask vector hóa

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

ds_demo_rpm = pd.DataFrame(
    {
        "id": [11, 12, 13, 14],
        "number_of_reviews": [0, 5, 0, 2],
        "reviews_per_month": [np.nan, 1.45, np.nan, np.nan],
    },
    index=["N1", "N2", "N3", "N4"],
)


def dien_rpm_co_can_cu_buoc(ds: pd.DataFrame) -> pd.Series:
    """Điền 0 cho reviews_per_month khi number_of_reviews bằng 0 theo cách tuần tự.

    Tham số:
        ds: DataFrame chứa cột 'number_of_reviews' và 'reviews_per_month'.
    Trả về:
        Series kiểu số thực cùng chỉ mục với ds, đã được điền 0 có căn cứ logic.
    """
    rpm = ds["reviews_per_month"].copy()
    chua_co_danh_gia = ds["number_of_reviews"].eq(0)
    rpm.loc[chua_co_danh_gia] = 0.0
    return rpm


rpm_ket_qua_c1 = dien_rpm_co_can_cu_buoc(ds_demo_rpm)

# Bắt đầu lời giải


def dien_rpm_co_can_cu_mask(ds: pd.DataFrame) -> pd.Series:
    """Điền 0 cho reviews_per_month bằng phương thức mask vector hóa.

    Tham số:
        ds: DataFrame chứa cột 'number_of_reviews' và 'reviews_per_month'.
    Trả về:
        Series kiểu số thực đã điền 0 có căn cứ.
    """
    return ds["reviews_per_month"].mask(ds["number_of_reviews"].eq(0), 0.0)


rpm_ket_qua_c2 = dien_rpm_co_can_cu_mask(ds_demo_rpm)
assert rpm_ket_qua_c1.equals(
    rpm_ket_qua_c2
), "Hai phương pháp phải cho kết quả đồng nhất"
print("Kết quả điền khuyết Cách 2 (vector hóa): Khớp hoàn toàn")

# Kết thúc lời giải
```

#### Giải thích cách 2

`mask` thay giá trị ở nơi điều kiện là True và giữ các vị trí còn lại. Điều kiện được tính theo cùng chỉ mục của bảng. Cách viết tập trung quy tắc thay thế vào một biểu thức, nhưng vẫn cần giải thích vì sao giá trị 0 có ý nghĩa cho đúng nhóm dòng đang xét.

#### Kết quả cách 2

```text
Kết quả điền khuyết Cách 2 (vector hóa): Khớp hoàn toàn
```
#### So sánh cách dùng

Hãy chọn Cách 1 khi muốn gán trực tiếp giá trị theo từng lát cắt điều kiện cụ thể trên cột đang xử lý cục bộ. Cách 2 phù hợp hơn khi muốn thể hiện quy tắc thay thế bằng phương thức hàm nhất quán và giữ nguyên vẹn mảng dữ liệu ban đầu.

:::

---

## Bài 2: Điền giá trị thiếu theo nhóm phân loại và cờ đánh dấu

<span id="data-lab-10-02"></span>

::: exercise
**Mục tiêu**: Ước lượng các giá trị bị khuyết trong cột giá lưu trú (`price`) bằng giá trị trung vị của từng loại phòng (`room_type`), đồng thời tạo cờ boolean `gia_da_dien` để lưu vết nguồn gốc dữ liệu, đo lường và giải thích sự dịch chuyển của giá trị trung bình mẫu.

**Dữ liệu đầu vào**: Bảng dữ liệu chỗ ở `ds_demo_gia` gồm 5 hàng thuộc ba loại phòng `Entire home/apt`, `Private room` và `Shared room`. Hai chỗ ở bị thiếu giá trong các nhóm có sẵn dữ liệu giá.

**Thao tác yêu cầu**:
1. Tạo Series `gia_uoc_luong`: Giữ nguyên giá đã biết, điền mỗi ô thiếu bằng trung vị giá của các chỗ ở có cùng `room_type`.
2. Tạo Series boolean `gia_da_dien`: Mang giá trị `True` tại các hàng có giá được điền và `False` tại các hàng giữ giá gốc.
3. Tính toán và so sánh giá trị trung bình của giá đã biết so với giá trị trung bình sau khi điền.
4. Nêu rõ lưu ý bắt buộc khi công bố báo cáo thống kê dựa trên dữ liệu đã qua điền khuyết.

**Trường hợp biên cần chú ý**: Nếu trong bảng tồn tại một loại phòng mà toàn bộ các hàng đều bị thiếu giá, trung vị của nhóm đó là `NaN`, Series kết quả phải giữ nguyên giá trị `NaN` thay vì phát sinh lỗi.
:::

::: solution
#### Cách 1: Tính từ điển trung vị và ánh xạ tuần tự

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

# Bắt đầu lời giải


def dien_gia_nhom_vong_lap(ds: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Điền trung vị giá theo từng loại phòng theo cách tiếp cận ánh xạ từ điển.

    Tham số:
        ds: DataFrame chứa cột 'price' (số thực) và 'room_type' (chuỗi phân loại).
    Trả về:
        Tuple gồm (gia_uoc_luong, gia_da_dien).
    """
    trung_vi_nhom = ds.groupby("room_type")["price"].median()
    gia_uoc = ds["price"].copy()
    gia_da_dien = ds["price"].isna()
    for room_type, median_val in trung_vi_nhom.items():
        mat_na = gia_da_dien & (ds["room_type"] == room_type)
        gia_uoc.loc[mat_na] = median_val
    return gia_uoc, gia_da_dien


# Dữ liệu thử nghiệm minh họa
ds_demo_gia = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105],
        "room_type": [
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Private room",
            "Shared room",
        ],
        "price": [60000.0, np.nan, 30000.0, np.nan, 20000.0],
    }
)

gia_uoc_c1, co_dien_c1 = dien_gia_nhom_vong_lap(ds_demo_gia)
print("Trung bình giá đã biết ban đầu:", ds_demo_gia["price"].mean())
print("Trung bình giá sau khi điền khuyết:", gia_uoc_c1.mean())

# Kết thúc lời giải
```

#### Giải thích cách 1

Duyệt từng nhóm loại phòng, tính trung vị từ những giá đã có rồi chỉ điền vào ô thiếu trong nhóm. Giữ lại cả dấu kiểm giá vốn đã thiếu để phân biệt số quan sát với số đã ước lượng. Nhóm không có một giá hợp lệ không thể tự cung cấp trung vị.

#### Kết quả cách 1

| Kết quả |
| --- |
| 40000 |

#### Cách 2: Sử dụng groupby kết hợp transform vector hóa

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

ds_demo_gia = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105],
        "room_type": [
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Private room",
            "Shared room",
        ],
        "price": [60000.0, np.nan, 30000.0, np.nan, 20000.0],
    }
)


def dien_gia_nhom_vong_lap(ds: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Điền trung vị giá theo từng loại phòng theo cách tiếp cận ánh xạ từ điển.

    Tham số:
        ds: DataFrame chứa cột 'price' (số thực) và 'room_type' (chuỗi phân loại).
    Trả về:
        Tuple gồm (gia_uoc_luong, gia_da_dien).
    """
    trung_vi_nhom = ds.groupby("room_type")["price"].median()
    gia_uoc = ds["price"].copy()
    gia_da_dien = ds["price"].isna()
    for room_type, median_val in trung_vi_nhom.items():
        mat_na = gia_da_dien & (ds["room_type"] == room_type)
        gia_uoc.loc[mat_na] = median_val
    return gia_uoc, gia_da_dien


gia_uoc_c1, co_dien_c1 = dien_gia_nhom_vong_lap(ds_demo_gia)

# Bắt đầu lời giải


def dien_gia_nhom_transform(ds: pd.DataFrame) -> tuple[pd.Series, pd.Series]:
    """Điền trung vị giá theo loại phòng bằng transform vector hóa.

    Tham số:
        ds: DataFrame chứa cột 'price' và 'room_type'.
    Trả về:
        Tuple gồm (gia_uoc_luong, gia_da_dien).
    """
    trung_vi_theo_hang = ds.groupby("room_type")["price"].transform("median")
    gia_uoc = ds["price"].fillna(trung_vi_theo_hang)
    gia_da_dien = ds["price"].isna()
    return gia_uoc, gia_da_dien


gia_uoc_c2, co_dien_c2 = dien_gia_nhom_transform(ds_demo_gia)
assert gia_uoc_c1.equals(gia_uoc_c2) and co_dien_c1.equals(
    co_dien_c2
), "Hai phương pháp phải đồng nhất"
print("Xác nhận Cách 2: Vector hóa thành công")

# Kết thúc lời giải
```

#### Giải thích cách 2

`groupby(...).transform("median")` trả một trung vị tương ứng với từng dòng nguồn. `fillna` hoặc mặt nạ sau đó chỉ thay ô thiếu, giữ giá đã quan sát. `transform` có cùng chỉ mục với bảng, thuận tiện hơn việc ghép một bảng tổng hợp nhỏ trở lại từng dòng.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Vector hóa thành công
```
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi muốn xem trước bảng trung vị từng nhóm hoặc cần lưu từ điển quy tắc để áp dụng cho dữ liệu mới. Cách 2 thuận tiện hơn khi muốn điền giá trị đại diện trực tiếp trên bảng nguồn nhờ khả năng giữ nguyên chỉ mục của transform.

:::

---

## Bài 3: Quy tắc kiểm tra tính hợp lệ của giá với bảng cờ boolean

<span id="data-lab-10-03"></span>

::: exercise
**Mục tiêu**: Xây dựng hàm kiểm định tính hợp lệ của cột giá phòng, tạo lập DataFrame gồm ba cột cờ boolean độc lập: `thieu`, `khong_duong`, `cao`. Phân biệt rạch ròi giữa giá trị bị khuyết và giá trị vi phạm biên nghiệp vụ ($\le 0$), bảo toàn chỉ mục ban đầu và tương thích với cả kiểu số thực chuẩn `float64` lẫn kiểu số thực cho phép khuyết `Float64`.

**Dữ liệu đầu vào**: Bảng dữ liệu kiểm thử `gia_thu` gồm 6 hàng với các giá trị: `np.nan`, `0.0`, `-5000.0`, `100000.0`, `150000.0`, `250000.0`, chỉ mục không liên tục `["P6", "P2", "P9", "P1", "P5", "P3"]`, cùng ngưỡng kiểm tra giá cao là 120,000.0 CLP.

**Thao tác yêu cầu**:
1. Cột `thieu`: Đánh dấu `True` nếu giá trị bị khuyết (`NaN` hoặc `<NA>`).
2. Cột `khong_duong`: Đánh dấu `True` nếu giá có tồn tại nhưng có giá trị $\le 0$.
3. Cột `cao`: Đánh dấu `True` nếu giá có tồn tại và lớn hơn ngưỡng chỉ định.
4. Bảo đảm các cột cờ có kiểu dữ liệu boolean chuẩn (`bool`), không chứa bất kỳ giá trị thiếu nào, và giữ nguyên chỉ mục của bảng đầu vào.

**Trường hợp biên cần chú ý**: Tại các hàng có giá trị bị khuyết, cờ `khong_duong` và `cao` bắt buộc phải nhận giá trị `False`, tuyệt đối không được để giá trị khuyết lan truyền sang kết quả cờ.
:::

::: solution
#### Cách 1: Xây dựng từng cột cờ bằng biểu thức điều kiện tuần tự

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

# Bắt đầu lời giải


def kiem_gia_tuan_tu(d: pd.DataFrame, nguong: float) -> pd.DataFrame:
    """Kiểm tra tính hợp lệ của giá và trả về ba cột cờ boolean tuần tự.

    Tham số:
        d: DataFrame chứa cột 'price'.
        nguong: Giá trị ngưỡng trần (float).
    Trả về:
        DataFrame gồm ba cột boolean: thieu, khong_duong, cao.
    """
    gia = d["price"]
    co_thieu = gia.isna()
    co_khong_duong = gia.notna() & (gia <= 0)
    co_cao = gia.notna() & (gia > nguong)
    ket_qua = pd.DataFrame(
        {
            "thieu": co_thieu.astype(bool),
            "khong_duong": co_khong_duong.fillna(False).astype(bool),
            "cao": co_cao.fillna(False).astype(bool),
        },
        index=d.index,
    )
    return ket_qua


# Bảng thử nghiệm kiểm tra tính hợp lệ
gia_thu = pd.DataFrame(
    {
        "price": [np.nan, 0.0, -5000.0, 100000.0, 150000.0, 250000.0],
    },
    index=["P6", "P2", "P9", "P1", "P5", "P3"],
)

co_gia_c1 = kiem_gia_tuan_tu(gia_thu, 120000.0)
print("Kết quả bảng cờ kiểm tra Cách 1:")
print(co_gia_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Xây từng cờ kiểm theo điều kiện giá thiếu, không dương hoặc vượt ngưỡng. Các cờ có thể chồng nhau, nên tổng số cờ không nhất thiết bằng số dòng lỗi phân biệt. Trả bảng cờ giữ chỉ mục để có thể đối chiếu chính xác bản ghi gốc.

#### Kết quả cách 1

| Chỉ mục | thieu | khong_duong | cao |
| --- | --- | --- | --- |
| P6 | True | False | False |
| P2 | False | True | False |
| P9 | False | True | False |
| P1 | False | False | False |
| P5 | False | False | True |
| P3 | False | False | True |

#### Cách 2: Đóng gói từ điển vector hóa tương thích kiểu nullable

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

gia_thu = pd.DataFrame(
    {
        "price": [np.nan, 0.0, -5000.0, 100000.0, 150000.0, 250000.0],
    },
    index=["P6", "P2", "P9", "P1", "P5", "P3"],
)


def kiem_gia_tuan_tu(d: pd.DataFrame, nguong: float) -> pd.DataFrame:
    """Kiểm tra tính hợp lệ của giá và trả về ba cột cờ boolean tuần tự.

    Tham số:
        d: DataFrame chứa cột 'price'.
        nguong: Giá trị ngưỡng trần (float).
    Trả về:
        DataFrame gồm ba cột boolean: thieu, khong_duong, cao.
    """
    gia = d["price"]
    co_thieu = gia.isna()
    co_khong_duong = gia.notna() & (gia <= 0)
    co_cao = gia.notna() & (gia > nguong)
    ket_qua = pd.DataFrame(
        {
            "thieu": co_thieu.astype(bool),
            "khong_duong": co_khong_duong.fillna(False).astype(bool),
            "cao": co_cao.fillna(False).astype(bool),
        },
        index=d.index,
    )
    return ket_qua


co_gia_c1 = kiem_gia_tuan_tu(gia_thu, 120000.0)

# Bắt đầu lời giải


def kiem_gia(d: pd.DataFrame, nguong: float) -> pd.DataFrame:
    """Hàm kiểm tra giá chuẩn mực trả về ba cờ boolean vector hóa.

    Tham số:
        d: DataFrame chứa cột 'price' (float64 hoặc Float64).
        nguong: Ngưỡng giá xem xét.
    Trả về:
        DataFrame gồm ba cột cờ thieu, khong_duong, cao.
    """
    p = d["price"]
    hop_le = p.notna()
    return pd.DataFrame(
        {
            "thieu": ~hop_le,
            "khong_duong": (hop_le & (p <= 0)).fillna(False).astype(bool),
            "cao": (hop_le & (p > nguong)).fillna(False).astype(bool),
        },
        index=d.index,
    )


co_gia_c2 = kiem_gia(gia_thu, 120000.0)
assert co_gia_c1.equals(co_gia_c2), "Kết quả hai cách phải hoàn toàn đồng nhất"
print("Xác nhận Cách 2: Tương thích hoàn toàn")

# Kết thúc lời giải
```

#### Giải thích cách 2

Biểu thức boolean theo cột thể hiện cùng bộ quy tắc cho toàn bảng. Tên cột cờ nên mô tả điều đã kiểm, thay vì gọi mọi dòng là chắc chắn sai. Ngưỡng là lựa chọn kiểm tra cần ghi lại, không phải bằng chứng tự động rằng giá cao phải bị xóa.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Tương thích hoàn toàn
```
#### So sánh cách dùng

Hãy chọn Cách 1 khi cần kiểm tra từng điều kiện riêng lẻ và theo dõi số bản ghi vi phạm sau mỗi phép so sánh. Cách 2 phù hợp khi bạn muốn gom các tiêu chí vào một từ điển tập trung để dễ bảo trì và xuất bảng kiểm toán.

:::

---

## Bài 4: Phân vị ngoại lai, loại bỏ hàng và chặn giá Winsorization

<span id="data-lab-10-04"></span>

::: exercise
**Mục tiêu**: Tính toán hai ngưỡng sàng lọc ngoại lai kinh điển: Ngưỡng khoảng tứ phân vị IQR ($Q_3 + 1.5 	imes 	ext{IQR}$) và ngưỡng phân vị 99% (P99) trên tập hợp các giá dương đã biết. Xây dựng bảng so sánh `so_sanh` đối chiếu tác động của ba chiến lược xử lý: Giữ nguyên giá dương, loại bỏ hàng vượt P99, và chặn giá tại P99 (Winsorization) lên số lượng quan sát, giá trị trung bình và giá trị trung vị.

**Dữ liệu đầu vào**: Bảng dữ liệu chỗ ở `ds_demo_phan_vi` gồm 12 hàng với các mức giá dương, giá khuyết và giá âm.

**Thao tác yêu cầu**:
1. Lọc tập hợp các giá trị dương đã biết ($p > 0$).
2. Xác định các phân vị $Q_1$, $Q_3$, khoảng tứ phân vị $	ext{IQR} = Q_3 - Q_1$, và ngưỡng trên $	ext{nguong\_iqr} = Q_3 + 1.5 	imes 	ext{IQR}$. Đếm số giá trị vượt ngưỡng IQR.
3. Tính ngưỡng phân vị 99% $	ext{nguong\_p99} = p.	ext{quantile}(0.99)$.
4. Lập bảng `so_sanh` gồm 3 hàng (`co_gia_duong`, `bo_tren_p99`, `chan_p99`) và 3 cột (`so_cho_o`, `trung_binh`, `trung_vi`).
5. Phân tích sự đánh đổi giữa việc loại bỏ hàng quan sát so với việc can thiệp chặn giá.

**Trường hợp biên cần chú ý**: Mọi phép tính ngưỡng và thống kê mô tả bắt buộc chỉ thực hiện trên tập giá dương đã biết, tuyệt đối không tính giá khuyết hoặc giá $\le 0$ như giá trị 0.
:::

::: solution
#### Cách 1: Lọc dữ liệu tuần tự và tổng hợp thủ công

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

# Bắt đầu lời giải


def phan_vi_chan_gia_buoc(ds: pd.DataFrame) -> tuple[float, int, float, pd.DataFrame]:
    """Tính ngưỡng ngoại lai và lập bảng so sánh ba chiến lược theo cách tuần tự.

    Tham số:
        ds: DataFrame chứa cột 'price'.
    Trả về:
        Tuple gồm (nguong_iqr, so_vuot_iqr, nguong_p99, so_sanh).
    """
    gia_duong = ds.loc[ds["price"] > 0, "price"].dropna()
    q1 = gia_duong.quantile(0.25)
    q3 = gia_duong.quantile(0.75)
    iqr = q3 - q1
    nguong_iqr = float(q3 + 1.5 * iqr)
    so_vuot_iqr = int((gia_duong > nguong_iqr).sum())
    nguong_p99 = float(gia_duong.quantile(0.99))

    # 1. Giữ nguyên giá dương
    n_duong = len(gia_duong)
    tb_duong = float(gia_duong.mean())
    tv_duong = float(gia_duong.median())

    # 2. Bỏ giá trên P99
    gia_bo = gia_duong[gia_duong <= nguong_p99]
    n_bo = len(gia_bo)
    tb_bo = float(gia_bo.mean())
    tv_bo = float(gia_bo.median())

    # 3. Chặn giá tại P99
    gia_chan = gia_duong.copy()
    gia_chan[gia_chan > nguong_p99] = nguong_p99
    n_chan = len(gia_chan)
    tb_chan = float(gia_chan.mean())
    tv_chan = float(gia_chan.median())

    so_sanh = pd.DataFrame(
        {
            "so_cho_o": [n_duong, n_bo, n_chan],
            "trung_binh": [tb_duong, tb_bo, tb_chan],
            "trung_vi": [tv_duong, tv_bo, tv_chan],
        },
        index=["co_gia_duong", "bo_tren_p99", "chan_p99"],
    )

    return nguong_iqr, so_vuot_iqr, nguong_p99, so_sanh


# Dữ liệu thử nghiệm minh họa
ds_demo_phan_vi = pd.DataFrame(
    {
        "price": [
            10000.0,
            20000.0,
            30000.0,
            40000.0,
            50000.0,
            60000.0,
            70000.0,
            80000.0,
            90000.0,
            500000.0,
            np.nan,
            -100.0,
        ],
    }
)

iqr_c1, n_iqr_c1, p99_c1, bang_c1 = phan_vi_chan_gia_buoc(ds_demo_phan_vi)
print(f"Ngưỡng IQR: {iqr_c1:.2f}, Số vượt: {n_iqr_c1}, Ngưỡng P99: {p99_c1:.2f}")
print(bang_c1.round(2))

# Kết thúc lời giải
```

#### Giải thích cách 1

Tính P99 từ phần giá hợp lệ trước khi đếm dòng vượt ngưỡng. Tạo hai kết quả riêng cho bỏ hàng và chặn giá vì chúng thay đổi dữ liệu theo hai cách khác nhau. Giữ ngưỡng cùng số dòng bị tác động để người đọc đánh giá mức thay đổi.

#### Kết quả cách 1

| Chỉ mục | so_cho_o | trung_binh | trung_vi |
| --- | --- | --- | --- |
| co_gia_duong | 10 | 95000 | 55000 |
| bo_tren_p99 | 9 | 50000 | 50000 |
| chan_p99 | 10 | 91310 | 55000 |

#### Cách 2: Sử dụng phương thức clip kết hợp tổng hợp vector hóa

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

ds_demo_phan_vi = pd.DataFrame(
    {
        "price": [
            10000.0,
            20000.0,
            30000.0,
            40000.0,
            50000.0,
            60000.0,
            70000.0,
            80000.0,
            90000.0,
            500000.0,
            np.nan,
            -100.0,
        ],
    }
)


def phan_vi_chan_gia_buoc(ds: pd.DataFrame) -> tuple[float, int, float, pd.DataFrame]:
    """Tính ngưỡng ngoại lai và lập bảng so sánh ba chiến lược theo cách tuần tự.

    Tham số:
        ds: DataFrame chứa cột 'price'.
    Trả về:
        Tuple gồm (nguong_iqr, so_vuot_iqr, nguong_p99, so_sanh).
    """
    gia_duong = ds.loc[ds["price"] > 0, "price"].dropna()
    q1 = gia_duong.quantile(0.25)
    q3 = gia_duong.quantile(0.75)
    iqr = q3 - q1
    nguong_iqr = float(q3 + 1.5 * iqr)
    so_vuot_iqr = int((gia_duong > nguong_iqr).sum())
    nguong_p99 = float(gia_duong.quantile(0.99))

    # 1. Giữ nguyên giá dương
    n_duong = len(gia_duong)
    tb_duong = float(gia_duong.mean())
    tv_duong = float(gia_duong.median())

    # 2. Bỏ giá trên P99
    gia_bo = gia_duong[gia_duong <= nguong_p99]
    n_bo = len(gia_bo)
    tb_bo = float(gia_bo.mean())
    tv_bo = float(gia_bo.median())

    # 3. Chặn giá tại P99
    gia_chan = gia_duong.copy()
    gia_chan[gia_chan > nguong_p99] = nguong_p99
    n_chan = len(gia_chan)
    tb_chan = float(gia_chan.mean())
    tv_chan = float(gia_chan.median())

    so_sanh = pd.DataFrame(
        {
            "so_cho_o": [n_duong, n_bo, n_chan],
            "trung_binh": [tb_duong, tb_bo, tb_chan],
            "trung_vi": [tv_duong, tv_bo, tv_chan],
        },
        index=["co_gia_duong", "bo_tren_p99", "chan_p99"],
    )

    return nguong_iqr, so_vuot_iqr, nguong_p99, so_sanh


iqr_c1, n_iqr_c1, p99_c1, bang_c1 = phan_vi_chan_gia_buoc(ds_demo_phan_vi)

# Bắt đầu lời giải


def phan_vi_chan_gia_clip(ds: pd.DataFrame) -> tuple[float, int, float, pd.DataFrame]:
    """Tính ngưỡng ngoại lai và lập bảng so sánh bằng clip vector hóa.

    Tham số:
        ds: DataFrame chứa cột 'price'.
    Trả về:
        Tuple gồm (nguong_iqr, so_vuot_iqr, nguong_p99, so_sanh).
    """
    p = ds.loc[ds["price"] > 0, "price"].dropna()
    q1, q3 = p.quantile(0.25), p.quantile(0.75)
    nguong_iqr = float(q3 + 1.5 * (q3 - q1))
    so_vuot_iqr = int((p > nguong_iqr).sum())
    nguong_p99 = float(p.quantile(0.99))

    p_bo = p[p <= nguong_p99]
    p_chan = p.clip(upper=nguong_p99)

    du_lieu_so_sanh = {
        "co_gia_duong": (len(p), float(p.mean()), float(p.median())),
        "bo_tren_p99": (len(p_bo), float(p_bo.mean()), float(p_bo.median())),
        "chan_p99": (len(p_chan), float(p_chan.mean()), float(p_chan.median())),
    }
    so_sanh = pd.DataFrame.from_dict(
        du_lieu_so_sanh, orient="index", columns=["so_cho_o", "trung_binh", "trung_vi"]
    )
    return nguong_iqr, so_vuot_iqr, nguong_p99, so_sanh


iqr_c2, n_iqr_c2, p99_c2, bang_c2 = phan_vi_chan_gia_clip(ds_demo_phan_vi)
pd.testing.assert_frame_equal(bang_c1, bang_c2)
print("Xác nhận Cách 2: Kết quả khớp tuyệt đối")

# Kết thúc lời giải
```

#### Giải thích cách 2

`clip(upper=nguong)` thay giá vượt ngưỡng bằng ngưỡng mà giữ số dòng. Lọc bằng mặt nạ lại làm giảm cỡ mẫu. Hai kết quả không thể xem là cùng một dữ liệu sau làm sạch, và không có quy tắc thống kê nào tự cho phép chặn mọi giá cao trong mọi bài toán.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Kết quả khớp tuyệt đối
```
#### So sánh cách dùng

Cách 1 đặt ngưỡng và các phương án xử lý cạnh nhau để thấy số dòng, trung bình và trung vị thay đổi thế nào. Cách 2 mở rõ thao tác chặn bằng `clip`. Giá vượt P99 chỉ là dấu hiệu cần xem xét, chưa đủ để kết luận đó là lỗi.

:::

---

## Bài 5: Phân biệt bản ghi nhập lặp và các sự kiện trùng thuộc tính

<span id="data-lab-10-05"></span>

::: exercise
**Mục tiêu**: Phân biệt ranh giới kỹ thuật giữa bản ghi nhập lặp (khi có khóa định danh duy nhất của đánh giá `review_id`) với hiện tượng trùng thuộc tính trong bảng rút gọn chỉ có cặp `(listing_id, date)`. Thực hiện khử trùng an toàn khi có khóa riêng và đếm số lượng dòng trùng lặp trong bảng rút gọn.

**Dữ liệu đầu vào**:
1. Bảng mẫu đầy đủ `mau_rv` gồm 4 dòng, có khóa định danh riêng `review_id`, trong đó mã R1 xuất hiện hai lần với cùng mã chỗ ở, ngày và nội dung bình luận.
2. Bảng rút gọn `rv_rut_gon` gồm 5 dòng, chỉ lưu hai thuộc tính `listing_id` và `date`.

**Thao tác yêu cầu**:
1. Trên `mau_rv`: Khử trùng bản nhập lặp bằng `drop_duplicates(subset=["review_id"])`, tạo bảng `rv_khong_lap` giữ nguyên 3 đánh giá phân biệt.
2. Trên `rv_rut_gon`: Tính toán `so_lap_sau_dau` (số dòng lặp lại sau lần xuất hiện đầu tiên) và `so_hang_nhom_lap` (tổng số dòng thuộc tất cả các nhóm có sự lặp lại).
3. Giải thích lý do vì sao chưa thể kết luận các dòng trùng cặp `(listing_id, date)` là bản ghi lỗi trong tập dữ liệu rút gọn.

**Trường hợp biên cần chú ý**: Phải giữ nguyên vẹn bảng đầu vào, không xóa hàng của bảng rút gọn khi chưa có khóa định danh duy nhất.
:::

::: solution
#### Cách 1: Sử dụng tham số keep trong duplicated và drop_duplicates

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

# Bắt đầu lời giải


def xu_ly_trung_lap_co_ban(
    mau_rv: pd.DataFrame, rv_rut_gon: pd.DataFrame
) -> tuple[pd.DataFrame, int, int]:
    """Khử trùng trên khóa riêng và đếm số lượng dòng trùng theo cặp thuộc tính.

    Tham số:
        mau_rv: DataFrame có cột 'review_id'.
        rv_rut_gon: DataFrame có cột 'listing_id' và 'date'.
    Trả về:
        Tuple gồm (rv_khong_lap, so_lap_sau_dau, so_hang_nhom_lap).
    """
    rv_khong_lap = mau_rv.drop_duplicates(subset=["review_id"]).copy()
    cap = ["listing_id", "date"]
    so_lap_sau_dau = int(rv_rut_gon.duplicated(subset=cap, keep="first").sum())
    so_hang_nhom_lap = int(rv_rut_gon.duplicated(subset=cap, keep=False).sum())
    return rv_khong_lap, so_lap_sau_dau, so_hang_nhom_lap


# Dữ liệu thử nghiệm minh họa
mau_rv_demo = pd.DataFrame(
    {
        "review_id": ["R1", "R2", "R1", "R3"],
        "listing_id": ["P1", "P1", "P1", "P2"],
        "date": pd.to_datetime(["2026-06-28"] * 4),
        "noi_dung": ["Yên tĩnh", "Sạch sẽ", "Yên tĩnh", "Thuận tiện"],
    }
)

rv_rut_gon_demo = pd.DataFrame(
    {
        "listing_id": [11, 11, 12, 12, 12],
        "date": pd.to_datetime(
            ["2025-08-10", "2025-08-10", "2026-01-05", "2026-01-05", "2026-01-05"]
        ),
    }
)

rv_sach_c1, lap_sau_c1, nhom_lap_c1 = xu_ly_trung_lap_co_ban(
    mau_rv_demo, rv_rut_gon_demo
)
print("Số đánh giá sau khử trùng khóa riêng:", len(rv_sach_c1))
print(f"Số lặp sau lần đầu: {lap_sau_c1}, Tổng số hàng thuộc nhóm lặp: {nhom_lap_c1}")

# Kết thúc lời giải
```

#### Giải thích cách 1

`duplicated` tìm các dòng trùng theo những cột đã chọn, còn `drop_duplicates` thực hiện một quyết định loại dòng. Có mã review phân biệt thì có thể kiểm bản nhập lặp theo mã đó. Chỉ có `listing_id` và ngày chưa đủ phân biệt hai người cùng đánh giá trong một ngày.

#### Kết quả cách 1

| Kết quả |
| --- |
| 3 |

#### Cách 2: Sử dụng groupby để phân tích kích thước nhóm lặp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

mau_rv_demo = pd.DataFrame(
    {
        "review_id": ["R1", "R2", "R1", "R3"],
        "listing_id": ["P1", "P1", "P1", "P2"],
        "date": pd.to_datetime(["2026-06-28"] * 4),
        "noi_dung": ["Yên tĩnh", "Sạch sẽ", "Yên tĩnh", "Thuận tiện"],
    }
)

rv_rut_gon_demo = pd.DataFrame(
    {
        "listing_id": [11, 11, 12, 12, 12],
        "date": pd.to_datetime(
            ["2025-08-10", "2025-08-10", "2026-01-05", "2026-01-05", "2026-01-05"]
        ),
    }
)


def xu_ly_trung_lap_co_ban(
    mau_rv: pd.DataFrame, rv_rut_gon: pd.DataFrame
) -> tuple[pd.DataFrame, int, int]:
    """Khử trùng trên khóa riêng và đếm số lượng dòng trùng theo cặp thuộc tính.

    Tham số:
        mau_rv: DataFrame có cột 'review_id'.
        rv_rut_gon: DataFrame có cột 'listing_id' và 'date'.
    Trả về:
        Tuple gồm (rv_khong_lap, so_lap_sau_dau, so_hang_nhom_lap).
    """
    rv_khong_lap = mau_rv.drop_duplicates(subset=["review_id"]).copy()
    cap = ["listing_id", "date"]
    so_lap_sau_dau = int(rv_rut_gon.duplicated(subset=cap, keep="first").sum())
    so_hang_nhom_lap = int(rv_rut_gon.duplicated(subset=cap, keep=False).sum())
    return rv_khong_lap, so_lap_sau_dau, so_hang_nhom_lap


rv_sach_c1, lap_sau_c1, nhom_lap_c1 = xu_ly_trung_lap_co_ban(
    mau_rv_demo, rv_rut_gon_demo
)

# Bắt đầu lời giải


def xu_ly_trung_lap_nang_cao(
    mau_rv: pd.DataFrame, rv_rut_gon: pd.DataFrame
) -> tuple[pd.DataFrame, int, int]:
    """Phân tích trùng lặp bằng kỹ thuật nhóm groupby.

    Tham số:
        mau_rv: DataFrame có cột 'review_id'.
        rv_rut_gon: DataFrame có hai cột 'listing_id' và 'date'.
    Trả về:
        Tuple gồm (rv_khong_lap, so_lap_sau_dau, so_hang_nhom_lap).
    """
    rv_khong_lap = mau_rv.loc[~mau_rv["review_id"].duplicated()].copy()
    tan_suat = rv_rut_gon.groupby(["listing_id", "date"]).size()
    nhom_bi_lap = tan_suat[tan_suat > 1]
    so_hang_nhom_lap = int(nhom_bi_lap.sum())
    so_lap_sau_dau = int((nhom_bi_lap - 1).sum())
    return rv_khong_lap, so_lap_sau_dau, so_hang_nhom_lap


rv_sach_c2, lap_sau_c2, nhom_lap_c2 = xu_ly_trung_lap_nang_cao(
    mau_rv_demo, rv_rut_gon_demo
)
assert (
    lap_sau_c1 == lap_sau_c2 and nhom_lap_c1 == nhom_lap_c2
), "Kết quả hai cách phải đồng nhất"
print("Xác nhận Cách 2: Phân tích kích thước nhóm hoàn tất")

# Kết thúc lời giải
```

#### Giải thích cách 2

Tách phép đếm trùng khỏi phép loại dòng để báo cáo được cả hiện tượng lẫn quyết định. `keep=False` đánh dấu mọi thành viên của nhóm trùng, còn `keep="first"` giữ một dòng đại diện. Kết quả phải ghi rõ đang đếm dòng tham gia nhóm hay số dòng vượt quá một đại diện.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Phân tích kích thước nhóm hoàn tất
```
#### So sánh cách dùng

Cách 1 thể hiện trực tiếp thao tác nhận diện và xử lý mã review bị lặp. Cách 2 giúp xem quy mô các nhóm lặp trước khi quyết định giữ dòng nào. Không dùng sự trùng ngày và mã chỗ ở làm bằng chứng duy nhất rằng hai review là một.

:::

---

## Bài 6: Kiểm tra miền thời gian và bảng cờ kiểm tra đánh giá

<span id="data-lab-10-06"></span>

::: exercise
**Mục tiêu**: Kiểm tra miền thời gian của bảng đánh giá (`time_domain`), xác định ngày sớm nhất, ngày muộn nhất và số lượng đánh giá rơi vào sau mốc công bố. Xây dựng bảng cờ kiểm tra chi tiết (`kiem_reviews`) cho từng dòng đánh giá theo các quy tắc kiểm tra ngày khuyết, ngày sau mốc và mã chỗ ở không khớp, sau đó áp dụng phép kiểm tra tổng hợp `any(axis=1)`.

**Dữ liệu đầu vào**: Bảng đánh giá mẫu `DEMO_RV` (18 dòng), danh sách mã chỗ ở hợp lệ từ `DEMO_DS["id"]`, và mốc chụp công bố `MOC = "2026-06-29"`.

**Thao tác yêu cầu**:
1. Viết hàm `time_domain(rv: pd.DataFrame, moc: str) -> dict` trả về từ điển đúng ba khóa: `ngay_dau` (Timestamp), `ngay_cuoi` (Timestamp), và `so_sau_moc` (int).
2. Viết hàm `kiem_reviews(r: pd.DataFrame, ids, moc: str) -> pd.DataFrame` trả về DataFrame 3 cột boolean: `ngay_thieu`, `sau_moc`, `id_khong_khop`.
3. Tính toán tổng số lượt gắn cờ và số dòng vi phạm ít nhất một cờ bằng phương thức `any(axis=1)`.
4. Phân tích chính sách xử lý đối với các đánh giá sau mốc chụp và nguyên tắc không tùy tiện thay đổi mốc công bố.

**Trường hợp biên cần chú ý**: Các đánh giá có ngày đúng bằng mốc chụp công bố (`date == moc`) vẫn thuộc phạm vi hợp lệ, cờ `sau_moc` bắt buộc nhận giá trị `False`. Khi ngày bị khuyết, cờ `sau_moc` phải là `False`.
:::

::: solution
#### Cách 1: Kiểm tra miền và cờ tuần tự từng bước

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)

# Bắt đầu lời giải


def time_domain_buoc(rv: pd.DataFrame, moc: str) -> dict:
    """Kiểm tra miền thời gian của bảng đánh giá tuần tự.

    Tham số:
        rv: DataFrame chứa cột 'date' kiểu datetime64.
        moc: Chuỗi ngày mốc định dạng 'YYYY-MM-DD'.
    Trả về:
        Dict gồm ngay_dau, ngay_cuoi, so_sau_moc.
    """
    ngay = rv["date"].dropna()
    moc_ts = pd.Timestamp(moc)
    return {
        "ngay_dau": ngay.min(),
        "ngay_cuoi": ngay.max(),
        "so_sau_moc": int((ngay > moc_ts).sum()),
    }


def kiem_reviews_buoc(r: pd.DataFrame, ids, moc: str) -> pd.DataFrame:
    """Tạo bảng cờ kiểm tra đánh giá theo từng bước.

    Tham số:
        r: DataFrame chứa 'listing_id' và 'date'.
        ids: Tập hợp hoặc Series các mã chỗ ở hợp lệ.
        moc: Mốc chụp công bố.
    Trả về:
        DataFrame gồm ba cột cờ boolean: ngay_thieu, sau_moc, id_khong_khop.
    """
    moc_ts = pd.Timestamp(moc)
    co_ngay_thieu = r["date"].isna()
    co_sau_moc = r["date"].notna() & (r["date"] > moc_ts)
    co_id_khong_khop = ~r["listing_id"].isin(ids)

    return pd.DataFrame(
        {
            "ngay_thieu": co_ngay_thieu.astype(bool),
            "sau_moc": co_sau_moc.astype(bool),
            "id_khong_khop": co_id_khong_khop.astype(bool),
        },
        index=r.index,
    )


mien_c1 = time_domain_buoc(DEMO_RV, MOC)
co_rv_c1 = kiem_reviews_buoc(DEMO_RV, DEMO_DS["id"], MOC)
print("Miền thời gian Cách 1:", mien_c1)
print("Tổng lượt gắn cờ:", co_rv_c1.sum().to_dict())
print("Số dòng có ít nhất một cờ:", int(co_rv_c1.any(axis=1).sum()))

# Kết thúc lời giải
```

#### Giải thích cách 1

Chuyển mốc so sánh thành `Timestamp`, rồi tính ngày nhỏ nhất, lớn nhất và số ngày vượt mốc. Phép `>` không gồm chính ngày mốc theo yêu cầu. Trả ba chỉ số có tên để không nhầm số dòng sau mốc với độ dài khoảng thời gian.

#### Kết quả cách 1

| Trường | Kết quả |
| --- | --- |
| ngay_thieu | 0 |
| sau_moc | 3 |
| id_khong_khop | 0 |

#### Cách 2: Đóng gói kiểm tra vector hóa kết hợp isin

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)


def time_domain_buoc(rv: pd.DataFrame, moc: str) -> dict:
    """Kiểm tra miền thời gian của bảng đánh giá tuần tự.

    Tham số:
        rv: DataFrame chứa cột 'date' kiểu datetime64.
        moc: Chuỗi ngày mốc định dạng 'YYYY-MM-DD'.
    Trả về:
        Dict gồm ngay_dau, ngay_cuoi, so_sau_moc.
    """
    ngay = rv["date"].dropna()
    moc_ts = pd.Timestamp(moc)
    return {
        "ngay_dau": ngay.min(),
        "ngay_cuoi": ngay.max(),
        "so_sau_moc": int((ngay > moc_ts).sum()),
    }


def kiem_reviews_buoc(r: pd.DataFrame, ids, moc: str) -> pd.DataFrame:
    """Tạo bảng cờ kiểm tra đánh giá theo từng bước.

    Tham số:
        r: DataFrame chứa 'listing_id' và 'date'.
        ids: Tập hợp hoặc Series các mã chỗ ở hợp lệ.
        moc: Mốc chụp công bố.
    Trả về:
        DataFrame gồm ba cột cờ boolean: ngay_thieu, sau_moc, id_khong_khop.
    """
    moc_ts = pd.Timestamp(moc)
    co_ngay_thieu = r["date"].isna()
    co_sau_moc = r["date"].notna() & (r["date"] > moc_ts)
    co_id_khong_khop = ~r["listing_id"].isin(ids)

    return pd.DataFrame(
        {
            "ngay_thieu": co_ngay_thieu.astype(bool),
            "sau_moc": co_sau_moc.astype(bool),
            "id_khong_khop": co_id_khong_khop.astype(bool),
        },
        index=r.index,
    )


mien_c1 = time_domain_buoc(DEMO_RV, MOC)

co_rv_c1 = kiem_reviews_buoc(DEMO_RV, DEMO_DS["id"], MOC)

# Bắt đầu lời giải


def time_domain(rv: pd.DataFrame, moc: str) -> dict:
    """Kiểm tra miền thời gian của bảng đánh giá chuẩn mực.

    Tham số:
        rv: DataFrame chứa cột 'date'.
        moc: Mốc chụp công bố (chuỗi 'YYYY-MM-DD').
    Trả về:
        Dict có đúng ba khóa ngay_dau, ngay_cuoi, so_sau_moc.
    """
    d = rv["date"]
    return {
        "ngay_dau": d.min(),
        "ngay_cuoi": d.max(),
        "so_sau_moc": int((d > pd.Timestamp(moc)).sum()),
    }


def kiem_reviews(r: pd.DataFrame, ids, moc: str) -> pd.DataFrame:
    """Tạo bảng cờ boolean kiểm tra đánh giá vector hóa.

    Tham số:
        r: DataFrame có 'listing_id' và 'date'.
        ids: Danh sách mã chỗ ở hợp lệ.
        moc: Mốc công bố.
    Trả về:
        DataFrame gồm ba cột cờ boolean.
    """
    d = r["date"]
    moc_ts = pd.Timestamp(moc)
    return pd.DataFrame(
        {
            "ngay_thieu": d.isna(),
            "sau_moc": (d.notna() & (d > moc_ts)).fillna(False).astype(bool),
            "id_khong_khop": (~r["listing_id"].isin(ids)).astype(bool),
        },
        index=r.index,
    )


mien_c2 = time_domain(DEMO_RV, MOC)
co_rv_c2 = kiem_reviews(DEMO_RV, DEMO_DS["id"], MOC)
assert mien_c1 == mien_c2 and co_rv_c1.equals(
    co_rv_c2
), "Kết quả hai cách phải đồng nhất"
print("Xác nhận Cách 2: Kiểm tra miền thời gian và cờ hoàn tất")

# Kết thúc lời giải
```

#### Giải thích cách 2

Các phép tổng hợp trên Series ngày tránh duyệt từng dòng trong Python. Cột ngày phải được đọc đúng trước khi gọi hàm. Ngày vượt mốc cần gắn cờ để đối chiếu phạm vi thu thập, không được tự suy ra nguyên nhân hoặc lặng lẽ sửa ngày.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Kiểm tra miền thời gian và cờ hoàn tất
```
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi làm việc tương tác để xem nhanh mốc thời gian biên và kiểm tra sơ bộ độ bao phủ dữ liệu. Cách 2 phù hợp khi cần đóng gói các quy tắc kiểm tra vào một hàm dùng chung để tự động hóa khâu tiền xử lý.

:::

---

## Bài 7: Kiểm tra toàn vẹn khóa ngoại và đánh giá mồ côi

<span id="data-lab-10-07"></span>

::: exercise
**Mục tiêu**: Kiểm tra tính toàn vẹn tham chiếu khóa ngoại giữa bảng đánh giá (`reviews.listing_id`) và bảng chỗ ở (`listings.id`). Phát hiện các dòng đánh giá mồ côi (orphan reviews) không thể liên kết với bất kỳ chỗ ở hợp lệ nào.

**Dữ liệu đầu vào**: Bảng đánh giá mẫu `DEMO_RV` (18 dòng), bảng chỗ ở `DEMO_DS` (6 chỗ ở), và bảng chỗ ở giả định bị thiếu chỗ ở mã 11 `ds_thieu = DEMO_DS[DEMO_DS["id"] != 11]`.

**Thao tác yêu cầu**:
1. Viết hàm `orphan_reviews(rv: pd.DataFrame, ds: pd.DataFrame) -> int` đếm số dòng đánh giá có `listing_id` không tồn tại trong `ds["id"]`.
2. Kiểm thử hàm trên dữ liệu chuẩn và trên bảng chỗ ở bị khuyết để xác nhận mọi đánh giá mồ côi đều được đếm đủ.
3. Giải thích lý do vì sao một kết quả kiểm tra bằng 0 vi phạm vẫn bắt buộc phải được ghi nhận trang trọng vào báo cáo QA.

**Trường hợp biên cần chú ý**: Nếu cùng một mã chỗ ở mồ côi xuất hiện nhiều lần trong bảng đánh giá, mỗi dòng vi phạm đều phải được đếm riêng rẽ, không dùng `nunique`.
:::

::: solution
#### Cách 1: Sử dụng toán tử đảo ngược trên phương thức isin

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)

# Bắt đầu lời giải


def orphan_reviews_isin(rv: pd.DataFrame, ds: pd.DataFrame) -> int:
    """Đếm số đánh giá mồ côi bằng phương thức isin.

    Tham số:
        rv: DataFrame chứa cột 'listing_id'.
        ds: DataFrame chứa cột 'id'.
    Trả về:
        Số lượng dòng đánh giá không tìm thấy chỗ ở tương ứng (int).
    """
    danh_sach_id = ds["id"]
    mat_na_mo_coi = ~rv["listing_id"].isin(danh_sach_id)
    return int(mat_na_mo_coi.sum())


# Dữ liệu thử nghiệm
ds_thieu = DEMO_DS[DEMO_DS["id"] != 11]
so_mo_coi_chuan = orphan_reviews_isin(DEMO_RV, DEMO_DS)
so_mo_coi_thieu = orphan_reviews_isin(DEMO_RV, ds_thieu)
print("Số đánh giá mồ côi trên dữ liệu chuẩn:", so_mo_coi_chuan)
print("Số đánh giá mồ côi khi khuyết chỗ ở 11:", so_mo_coi_thieu)

# Kết thúc lời giải
```

#### Giải thích cách 1

`isin(ds["id"])` kiểm tra mã chỗ ở của từng dòng đánh giá có trong bảng danh mục hay không. Đảo mặt nạ bằng `~` rồi cộng boolean đếm số dòng không khớp. Một mã không khớp lặp ba lần vẫn tạo ba dòng được đếm.

#### Kết quả cách 1

| Kết quả |
| --- |
| 7 |

#### Cách 2: Sử dụng phép ghép nối Anti-Join

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)

ds_thieu = DEMO_DS[DEMO_DS["id"] != 11]


def orphan_reviews_isin(rv: pd.DataFrame, ds: pd.DataFrame) -> int:
    """Đếm số đánh giá mồ côi bằng phương thức isin.

    Tham số:
        rv: DataFrame chứa cột 'listing_id'.
        ds: DataFrame chứa cột 'id'.
    Trả về:
        Số lượng dòng đánh giá không tìm thấy chỗ ở tương ứng (int).
    """
    danh_sach_id = ds["id"]
    mat_na_mo_coi = ~rv["listing_id"].isin(danh_sach_id)
    return int(mat_na_mo_coi.sum())


so_mo_coi_chuan = orphan_reviews_isin(DEMO_RV, DEMO_DS)

so_mo_coi_thieu = orphan_reviews_isin(DEMO_RV, ds_thieu)

# Bắt đầu lời giải


def orphan_reviews(rv: pd.DataFrame, ds: pd.DataFrame) -> int:
    """Đếm số đánh giá mồ côi bằng kỹ thuật anti-join.

    Tham số:
        rv: DataFrame chứa cột 'listing_id'.
        ds: DataFrame chứa cột 'id'.
    Trả về:
        Số lượng đánh giá mồ côi (int).
    """
    ghep = rv[["listing_id"]].merge(
        ds[["id"]], left_on="listing_id", right_on="id", how="left", indicator=True
    )
    return int((ghep["_merge"] == "left_only").sum())


so_c2_chuan = orphan_reviews(DEMO_RV, DEMO_DS)
so_c2_thieu = orphan_reviews(DEMO_RV, ds_thieu)
assert (
    so_mo_coi_chuan == so_c2_chuan and so_mo_coi_thieu == so_c2_thieu
), "Hai cách phải cho kết quả đồng nhất"
print("Xác nhận Cách 2: Anti-join hoàn tất")

# Kết thúc lời giải
```

#### Giải thích cách 2

Phép ghép có chỉ báo hoặc đối chiếu tập khóa làm rõ phía nào thiếu bản ghi. Phải giữ đơn vị đếm là dòng đánh giá, không đổi thành số mã khác nhau nếu đề không yêu cầu. Các khóa thiếu cũng cần được hiểu theo quy tắc của bài trước khi gọi kết quả là toàn vẹn.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Anti-join hoàn tất
```
#### So sánh cách dùng

Hãy chọn Cách 1 khi bạn chỉ cần đếm nhanh số lượng dòng đánh giá mang mã chỗ ở không tồn tại trong danh mục nguồn. Cách 2 hữu ích hơn khi cần giữ lại toàn bộ các cột thông tin của bản ghi mồ côi để truy vết nguyên nhân sai lệch khóa ngoại.

:::

---

## Bài 8: Đánh giá ứng viên khóa tự nhiên trên tập thuộc tính

<span id="data-lab-10-08"></span>

::: exercise
**Mục tiêu**: Đánh giá tính khả thi của việc sử dụng tập thuộc tính sẵn có `(listing_id, date)` làm khóa tự nhiên trong bảng đánh giá thông qua hàm `duplicate_pairs`. Xác định số lượng bản ghi bị trùng lặp theo danh sách cột chỉ định mà không làm biến đổi bảng đầu vào.

**Dữ liệu đầu vào**: Bảng đánh giá mẫu `DEMO_RV` (18 dòng), danh sách cột kiểm tra mặc định `cot = ["listing_id", "date"]`.

**Thao tác yêu cầu**:
1. Viết hàm `duplicate_pairs(rv: pd.DataFrame, cot: list = None) -> int` nhận bảng và danh sách cột ứng viên làm khóa, trả về số dòng lặp lại sau lần xuất hiện đầu tiên (`duplicated(subset=cot)`).
2. Kiểm tra trên danh sách mặc định `["listing_id", "date"]` và danh sách đơn thuộc tính `["listing_id"]`.
3. Giải thích hệ quả kỹ thuật nếu người xử lý dữ liệu vội vàng gọi `drop_duplicates(subset=["listing_id", "date"])`.

**Trường hợp biên cần chú ý**: Hàm chỉ đếm số lượng, tuyệt đối không chỉnh sửa dữ liệu, không xóa dòng của bảng đầu vào.
:::

::: solution
#### Cách 1: Đếm số lượng phần tử trùng lặp với duplicated

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)

# Bắt đầu lời giải


def duplicate_pairs_duplicated(rv: pd.DataFrame, cot: list = None) -> int:
    """Đếm số dòng lặp lại theo danh sách cột bằng phương thức duplicated.

    Tham số:
        rv: DataFrame cần kiểm tra.
        cot: Danh sách các cột ứng viên làm khóa (mặc định: listing_id và date).
    Trả về:
        Số lượng dòng lặp lại sau lần đầu tiên (int).
    """
    if cot is None:
        cot = ["listing_id", "date"]
    return int(rv.duplicated(subset=cot).sum())


lap_c1_cap = duplicate_pairs_duplicated(DEMO_RV)
lap_c1_id = duplicate_pairs_duplicated(DEMO_RV, ["listing_id"])
print("Số dòng lặp theo cặp (listing_id, date):", lap_c1_cap)
print("Số dòng lặp theo riêng listing_id:", lap_c1_id)

# Kết thúc lời giải
```

#### Giải thích cách 1

`duplicated` với hai cột mã chỗ ở và ngày xác định các cặp giống nhau. Chọn `keep=False` khi đếm mọi dòng tham gia cặp lặp. Đó là phép kiểm khóa tự nhiên được đề xuất, chưa phải bằng chứng tất cả những đánh giá đó là bản sao.

#### Kết quả cách 1

| Kết quả |
| --- |
| 13 |

#### Cách 2: So sánh độ dài trước và sau khi loại trừ giá trị trùng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)


def duplicate_pairs_duplicated(rv: pd.DataFrame, cot: list = None) -> int:
    """Đếm số dòng lặp lại theo danh sách cột bằng phương thức duplicated.

    Tham số:
        rv: DataFrame cần kiểm tra.
        cot: Danh sách các cột ứng viên làm khóa (mặc định: listing_id và date).
    Trả về:
        Số lượng dòng lặp lại sau lần đầu tiên (int).
    """
    if cot is None:
        cot = ["listing_id", "date"]
    return int(rv.duplicated(subset=cot).sum())


lap_c1_cap = duplicate_pairs_duplicated(DEMO_RV)

lap_c1_id = duplicate_pairs_duplicated(DEMO_RV, ["listing_id"])

# Bắt đầu lời giải


def duplicate_pairs(rv: pd.DataFrame, cot: list = None) -> int:
    """Đếm số dòng lặp bằng cách đối chiếu độ dài tập duy nhất.

    Tham số:
        rv: DataFrame đánh giá.
        cot: Danh sách cột khóa ứng viên.
    Trả về:
        Số lượng dòng lặp lại (int).
    """
    if cot is None:
        cot = ["listing_id", "date"]
    so_dong_duy_nhat = len(rv.drop_duplicates(subset=cot))
    return int(len(rv) - so_dong_duy_nhat)


lap_c2_cap = duplicate_pairs(DEMO_RV)
lap_c2_id = duplicate_pairs(DEMO_RV, ["listing_id"])
assert (
    lap_c1_cap == lap_c2_cap and lap_c1_id == lap_c2_id
), "Hai cách phải cho kết quả đồng nhất"
print("Xác nhận Cách 2: Đối chiếu độ dài thành công")

# Kết thúc lời giải
```

#### Giải thích cách 2

Nhóm theo cặp khóa rồi đếm kích thước giúp xem phân bố các nhóm lặp. Tổng kích thước nhóm lớn hơn một khác với tổng số dòng dư sau khi giữ một đại diện. Giữ đúng định nghĩa cần trả và kiểm cả một cặp xuất hiện ba lần để thấy sự khác nhau.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Đối chiếu độ dài thành công
```
#### So sánh cách dùng

Cách 1 kiểm từng dòng có tham gia một cặp khóa lặp hay không. Cách 2 đếm qua kích thước nhóm để đối chiếu cùng đại lượng. Tổng số dòng tham gia nhóm lặp khác số dòng dư sau khi giữ một đại diện của mỗi nhóm.

:::

---

## Bài 9: Đối chiếu cột dẫn xuất tổng số đánh giá với con số tự đếm

<span id="data-lab-10-09"></span>

::: exercise
**Mục tiêu**: Kiểm tra tính nhất quán giữa cột dẫn xuất có sẵn `number_of_reviews` trong bảng `listings` với số dòng thực tế đếm được từ bảng `reviews`. Thiết lập bảng đối chiếu 3 cột `nguon`, `dem_ca_file`, `den_moc` cho toàn bộ các chỗ ở, phân tích ảnh hưởng của chính sách cắt mốc thời gian lên tính nhất quán của cột dẫn xuất.

**Dữ liệu đầu vào**: Bảng đánh giá mẫu `DEMO_RV` (18 dòng), bảng chỗ ở `DEMO_DS` (6 chỗ ở), mốc công bố `MOC = "2026-06-29"`.

**Thao tác yêu cầu**:
1. Viết hàm `review_count_check(rv: pd.DataFrame, ds: pd.DataFrame) -> dict` trả về từ điển đúng hai khóa:
   - `dem_that`: Series kiểu số nguyên cùng chỉ mục với `ds`, thể hiện số dòng đánh giá thực tế của từng chỗ ở trên toàn bộ bảng `rv`, chỗ ở chưa có đánh giá nào phải nhận giá trị 0.
   - `so_lech_tong`: Số lượng chỗ ở có `number_of_reviews` khác với `dem_that`.
2. Viết hàm `doi_chieu_so_danh_gia(rv: pd.DataFrame, ds: pd.DataFrame, moc: str) -> pd.DataFrame` trả về DataFrame có chỉ mục là `ds["id"]` và ba cột: `nguon`, `dem_ca_file`, `den_moc`.
3. Phân tích nguyên nhân vì sao `nguon` khớp 100% với `dem_ca_file` nhưng lại có sự chênh lệch so với `den_moc`.

**Trường hợp biên cần chú ý**: Các chỗ ở có 0 đánh giá (như Studio nuevo mã 15) bắt buộc phải có giá trị đếm bằng 0, tuyệt đối không được để giá trị `NaN` trong kết quả đối chiếu.
:::

::: solution
#### Cách 1: Sử dụng groupby kết hợp reindex căn chỉnh chỉ mục

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)

# Bắt đầu lời giải


def review_count_check_reindex(rv: pd.DataFrame, ds: pd.DataFrame) -> dict:
    """Đối chiếu tổng số đánh giá bằng groupby và reindex tuần tự.

    Tham số:
        rv: DataFrame chứa 'listing_id'.
        ds: DataFrame chứa 'id' và 'number_of_reviews'.
    Trả về:
        Dict gồm 'dem_that' (Series) và 'so_lech_tong' (int).
    """
    dem_nhom = rv.groupby("listing_id").size()
    dem_theo_id = dem_nhom.reindex(ds["id"], fill_value=0)
    dem_that = pd.Series(dem_theo_id.values, index=ds.index, dtype=int)
    so_lech = int((ds["number_of_reviews"] != dem_that).sum())
    return {"dem_that": dem_that, "so_lech_tong": so_lech}


def doi_chieu_so_danh_gia_buoc(
    rv: pd.DataFrame, ds: pd.DataFrame, moc: str
) -> pd.DataFrame:
    """Tạo bảng đối chiếu ba cột số lượng đánh giá theo từng phạm vi.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        moc: Mốc chụp công bố.
    Trả về:
        DataFrame có chỉ mục là ds['id'] và ba cột nguon, dem_ca_file, den_moc.
    """
    moc_ts = pd.Timestamp(moc)
    dem_ca_file = (
        rv.groupby("listing_id").size().reindex(ds["id"], fill_value=0).astype(int)
    )
    dem_den_moc = (
        rv[rv["date"] <= moc_ts]
        .groupby("listing_id")
        .size()
        .reindex(ds["id"], fill_value=0)
        .astype(int)
    )
    nguon = ds.set_index("id")["number_of_reviews"].astype(int)

    return pd.DataFrame(
        {
            "nguon": nguon,
            "dem_ca_file": dem_ca_file.values,
            "den_moc": dem_den_moc.values,
        },
        index=ds["id"],
    )


kq_q4_c1 = review_count_check_reindex(DEMO_RV, DEMO_DS)
bang_dc_c1 = doi_chieu_so_danh_gia_buoc(DEMO_RV, DEMO_DS, MOC)
print("Số chỗ ở lệch tổng số đánh giá:", kq_q4_c1["so_lech_tong"])
print(bang_dc_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Đếm review theo mã chỗ ở rồi `reindex` theo thứ tự ID của bảng danh mục. Điền 0 cho ID không xuất hiện trong log vì đang đếm số sự kiện của bảng đã cung cấp. So sánh với cột tính sẵn cho biết hai nguồn đếm có khớp trên cùng phạm vi hay không.

#### Kết quả cách 1

| id | nguon | dem_ca_file | den_moc |
| --- | --- | --- | --- |
| 11 | 7 | 7 | 6 |
| 12 | 4 | 4 | 3 |
| 13 | 4 | 4 | 4 |
| 14 | 2 | 2 | 1 |
| 15 | 0 | 0 | 0 |
| 16 | 1 | 1 | 1 |

#### Cách 2: Sử dụng phương thức map và gán giá trị mặc định

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)


def review_count_check_reindex(rv: pd.DataFrame, ds: pd.DataFrame) -> dict:
    """Đối chiếu tổng số đánh giá bằng groupby và reindex tuần tự.

    Tham số:
        rv: DataFrame chứa 'listing_id'.
        ds: DataFrame chứa 'id' và 'number_of_reviews'.
    Trả về:
        Dict gồm 'dem_that' (Series) và 'so_lech_tong' (int).
    """
    dem_nhom = rv.groupby("listing_id").size()
    dem_theo_id = dem_nhom.reindex(ds["id"], fill_value=0)
    dem_that = pd.Series(dem_theo_id.values, index=ds.index, dtype=int)
    so_lech = int((ds["number_of_reviews"] != dem_that).sum())
    return {"dem_that": dem_that, "so_lech_tong": so_lech}


def doi_chieu_so_danh_gia_buoc(
    rv: pd.DataFrame, ds: pd.DataFrame, moc: str
) -> pd.DataFrame:
    """Tạo bảng đối chiếu ba cột số lượng đánh giá theo từng phạm vi.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        moc: Mốc chụp công bố.
    Trả về:
        DataFrame có chỉ mục là ds['id'] và ba cột nguon, dem_ca_file, den_moc.
    """
    moc_ts = pd.Timestamp(moc)
    dem_ca_file = (
        rv.groupby("listing_id").size().reindex(ds["id"], fill_value=0).astype(int)
    )
    dem_den_moc = (
        rv[rv["date"] <= moc_ts]
        .groupby("listing_id")
        .size()
        .reindex(ds["id"], fill_value=0)
        .astype(int)
    )
    nguon = ds.set_index("id")["number_of_reviews"].astype(int)

    return pd.DataFrame(
        {
            "nguon": nguon,
            "dem_ca_file": dem_ca_file.values,
            "den_moc": dem_den_moc.values,
        },
        index=ds["id"],
    )


kq_q4_c1 = review_count_check_reindex(DEMO_RV, DEMO_DS)

bang_dc_c1 = doi_chieu_so_danh_gia_buoc(DEMO_RV, DEMO_DS, MOC)

# Bắt đầu lời giải


def review_count_check(rv: pd.DataFrame, ds: pd.DataFrame) -> dict:
    """Hàm đối chiếu tổng số đánh giá chuẩn mực bằng map vector hóa.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
    Trả về:
        Dict gồm dem_that và so_lech_tong.
    """
    dem = rv.groupby("listing_id").size()
    dem_that = ds["id"].map(dem).fillna(0).astype(int)
    so_lech = int((ds["number_of_reviews"] != dem_that).sum())
    return {"dem_that": dem_that, "so_lech_tong": so_lech}


def doi_chieu_so_danh_gia(rv: pd.DataFrame, ds: pd.DataFrame, moc: str) -> pd.DataFrame:
    """Tạo bảng đối chiếu số lượng đánh giá vector hóa.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        moc: Mốc chụp công bố.
    Trả về:
        DataFrame gồm ba cột nguon, dem_ca_file, den_moc.
    """
    dem_tat_ca = rv.groupby("listing_id").size()
    dem_cat_moc = rv.loc[rv["date"] <= pd.Timestamp(moc)].groupby("listing_id").size()

    return pd.DataFrame(
        {
            "nguon": ds.set_index("id")["number_of_reviews"],
            "dem_ca_file": ds["id"].map(dem_tat_ca).fillna(0).astype(int).values,
            "den_moc": ds["id"].map(dem_cat_moc).fillna(0).astype(int).values,
        },
        index=ds["id"],
    )


kq_q4_c2 = review_count_check(DEMO_RV, DEMO_DS)
bang_dc_c2 = doi_chieu_so_danh_gia(DEMO_RV, DEMO_DS, MOC)
assert kq_q4_c1["dem_that"].equals(kq_q4_c2["dem_that"]) and bang_dc_c1.equals(
    bang_dc_c2
)
print("Xác nhận Cách 2: Đối chiếu cột dẫn xuất thành công")

# Kết thúc lời giải
```

#### Giải thích cách 2

Ghép bảng đếm theo ID rồi căn lại chỉ mục giữ cho kết quả đi cùng từng dòng danh mục. Khóa bảng tra cần đủ tính duy nhất để phép ghép không nhân bản dòng. Dấu lệch chưa chứng minh một trong hai bảng sai, vì chúng có thể dùng phạm vi thời gian hoặc tiêu chí giữ review khác nhau.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Đối chiếu cột dẫn xuất thành công
```
#### So sánh cách dùng

Hãy chọn Cách 1 khi bạn muốn tạo một chuỗi đếm độc lập được căn chỉnh chuẩn xác theo chỉ mục của bảng danh mục để làm phép trừ. Cách 2 thuận tiện hơn khi muốn gắn thêm cột đối chiếu trực tiếp vào khung dữ liệu hiện có để tiện quan sát.

:::

---

## Bài 10: Đối chiếu cột đánh giá 12 tháng gần nhất và phân tích định nghĩa cửa sổ

<span id="data-lab-10-10"></span>

::: exercise
**Mục tiêu**: Kiểm tra tính nhất quán của cột dẫn xuất `number_of_reviews_ltm` (Last Twelve Months: 12 tháng gần nhất) bằng cách tự đếm số dòng trong cửa sổ thời gian. Khảo sát và so sánh hai quy ước cửa sổ: Cửa sổ mở không chặn trên (`ket_thuc=None`) theo mặc định của tài liệu gốc, và cửa sổ đóng có chặn trên tại mốc công bố (`ket_thuc=moc`).

**Dữ liệu đầu vào**: Bảng đánh giá mẫu `DEMO_RV`, bảng chỗ ở `DEMO_DS`, ngày bắt đầu cửa sổ `LTM_BAT_DAU = "2025-06-30"`, mốc công bố `MOC = "2026-06-29"`.

**Thao tác yêu cầu**:
1. Viết hàm `ltm_mismatch(rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str | None = None) -> dict` trả về từ điển đúng ba khóa:
   - `ltm_that`: Series kiểu số nguyên cùng chỉ mục với `ds`, thể hiện số đánh giá thỏa mãn điều kiện thời gian.
   - `do_lech`: Series kiểu số nguyên cùng chỉ mục với `ds`, tính bằng `number_of_reviews_ltm − ltm_that`.
   - `so_lech_ltm`: Số lượng chỗ ở có `do_lech` khác 0.
2. Viết hàm `doi_chieu_12_thang_co_dinh(rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str) -> tuple[pd.Series, pd.Series]` thực hiện đối chiếu trên khoảng đóng 12 tháng cố định $[2025-06-30, 2026-06-29]$, trả về `(dem_12_thang, lech_12_thang)` với `lech_12_thang = dem_12_thang − number_of_reviews_ltm`.
3. Phân tích phân bố của độ lệch và giải thích vì sao độ lệch tập trung ở giá trị $-1$.

**Trường hợp biên cần chú ý**: Mặc định `ket_thuc=None` không được chặn trên (lấy toàn bộ các đánh giá từ `bat_dau` trở về sau). Khi có `ket_thuc`, khoảng thời gian bao gồm cả hai ngày biên.
:::

::: solution
#### Cách 1: Lọc dữ liệu điều kiện và tính toán tuần tự

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)

# Bắt đầu lời giải


def ltm_mismatch_buoc(
    rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str | None = None
) -> dict:
    """Tính số đánh giá LTM và đo độ lệch theo cách tiếp cận tuần tự.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        bat_dau: Chuỗi ngày bắt đầu (gồm cả ngày này).
        ket_thuc: Chuỗi ngày kết thúc tùy chọn (None nếu không chặn trên).
    Trả về:
        Dict gồm ltm_that, do_lech, so_lech_ltm.
    """
    mat_na = rv["date"] >= pd.Timestamp(bat_dau)
    if ket_thuc is not None:
        mat_na = mat_na & (rv["date"] <= pd.Timestamp(ket_thuc))

    dem_nhom = rv[mat_na].groupby("listing_id").size()
    ltm_that = pd.Series(
        dem_nhom.reindex(ds["id"], fill_value=0).values, index=ds.index, dtype=int
    )
    do_lech = ds["number_of_reviews_ltm"] - ltm_that
    so_lech_ltm = int((do_lech != 0).sum())
    return {"ltm_that": ltm_that, "do_lech": do_lech, "so_lech_ltm": so_lech_ltm}


def doi_chieu_12_thang_co_dinh_buoc(
    rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str
) -> tuple[pd.Series, pd.Series]:
    """Đối chiếu khoảng đóng 12 tháng cố định tuần tự.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        bat_dau, ket_thuc: Hai đầu mút của khoảng ngày.
    Trả về:
        Tuple gồm (dem_12_thang, lech_12_thang).
    """
    mat_na = (rv["date"] >= pd.Timestamp(bat_dau)) & (
        rv["date"] <= pd.Timestamp(ket_thuc)
    )
    dem = (
        rv[mat_na]
        .groupby("listing_id")
        .size()
        .reindex(ds["id"], fill_value=0)
        .astype(int)
    )
    dem.index = ds["id"]
    nguon = ds.set_index("id")["number_of_reviews_ltm"].astype(int)
    lech = dem - nguon
    return dem, lech


kq_ltm_c1 = ltm_mismatch_buoc(DEMO_RV, DEMO_DS, LTM_BAT_DAU)
dem12_c1, lech12_c1 = doi_chieu_12_thang_co_dinh_buoc(
    DEMO_RV, DEMO_DS, LTM_BAT_DAU, MOC
)
print("Kết quả LTM không chặn trên Cách 1:")
print("Số chỗ ở lệch LTM:", kq_ltm_c1["so_lech_ltm"])
print("Độ lệch từng chỗ ở:", kq_ltm_c1["do_lech"].tolist())

# Kết thúc lời giải
```

#### Giải thích cách 1

Lọc ngày theo cận dưới gồm chính ngày bắt đầu. Nếu có cận trên, áp dụng thêm điều kiện gồm ngày kết thúc. Đếm theo ID rồi căn về bảng danh mục, sau đó lấy số tính sẵn trừ số vừa đếm. Để `ket_thuc=None` có nghĩa không chặn trên, đúng như yêu cầu biến thể này.

#### Kết quả cách 1

| Vị trí | Kết quả |
| --- | --- |
| 0 | -1 |
| 1 | -1 |
| 2 | 0 |
| 3 | 0 |
| 4 | 0 |
| 5 | 0 |

#### Cách 2: Sử dụng phương thức between và vector hóa

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)


def ltm_mismatch_buoc(
    rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str | None = None
) -> dict:
    """Tính số đánh giá LTM và đo độ lệch theo cách tiếp cận tuần tự.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        bat_dau: Chuỗi ngày bắt đầu (gồm cả ngày này).
        ket_thuc: Chuỗi ngày kết thúc tùy chọn (None nếu không chặn trên).
    Trả về:
        Dict gồm ltm_that, do_lech, so_lech_ltm.
    """
    mat_na = rv["date"] >= pd.Timestamp(bat_dau)
    if ket_thuc is not None:
        mat_na = mat_na & (rv["date"] <= pd.Timestamp(ket_thuc))

    dem_nhom = rv[mat_na].groupby("listing_id").size()
    ltm_that = pd.Series(
        dem_nhom.reindex(ds["id"], fill_value=0).values, index=ds.index, dtype=int
    )
    do_lech = ds["number_of_reviews_ltm"] - ltm_that
    so_lech_ltm = int((do_lech != 0).sum())
    return {"ltm_that": ltm_that, "do_lech": do_lech, "so_lech_ltm": so_lech_ltm}


def doi_chieu_12_thang_co_dinh_buoc(
    rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str
) -> tuple[pd.Series, pd.Series]:
    """Đối chiếu khoảng đóng 12 tháng cố định tuần tự.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        bat_dau, ket_thuc: Hai đầu mút của khoảng ngày.
    Trả về:
        Tuple gồm (dem_12_thang, lech_12_thang).
    """
    mat_na = (rv["date"] >= pd.Timestamp(bat_dau)) & (
        rv["date"] <= pd.Timestamp(ket_thuc)
    )
    dem = (
        rv[mat_na]
        .groupby("listing_id")
        .size()
        .reindex(ds["id"], fill_value=0)
        .astype(int)
    )
    dem.index = ds["id"]
    nguon = ds.set_index("id")["number_of_reviews_ltm"].astype(int)
    lech = dem - nguon
    return dem, lech


kq_ltm_c1 = ltm_mismatch_buoc(DEMO_RV, DEMO_DS, LTM_BAT_DAU)

dem12_c1, lech12_c1 = doi_chieu_12_thang_co_dinh_buoc(
    DEMO_RV, DEMO_DS, LTM_BAT_DAU, MOC
)

# Bắt đầu lời giải


def ltm_mismatch(
    rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str | None = None
) -> dict:
    """Hàm đối chiếu LTM chuẩn mực hỗ trợ cả hai quy ước cửa sổ.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        bat_dau: Ngày bắt đầu.
        ket_thuc: Ngày kết thúc tùy chọn.
    Trả về:
        Dict gồm ltm_that, do_lech, so_lech_ltm.
    """
    ts_bat_dau = pd.Timestamp(bat_dau)
    if ket_thuc is None:
        loc_rv = rv.loc[rv["date"] >= ts_bat_dau]
    else:
        loc_rv = rv.loc[rv["date"].between(ts_bat_dau, pd.Timestamp(ket_thuc))]

    dem = loc_rv.groupby("listing_id").size()
    ltm_that = ds["id"].map(dem).fillna(0).astype(int)
    ltm_that.index = ds.index
    do_lech = ds["number_of_reviews_ltm"] - ltm_that
    so_lech_ltm = int((do_lech != 0).sum())
    return {"ltm_that": ltm_that, "do_lech": do_lech, "so_lech_ltm": so_lech_ltm}


def doi_chieu_12_thang_co_dinh(
    rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str
) -> tuple[pd.Series, pd.Series]:
    """Đối chiếu khoảng đóng 12 tháng vector hóa.

    Tham số:
        rv: DataFrame đánh giá.
        ds: DataFrame chỗ ở.
        bat_dau, ket_thuc: Chuỗi ngày biên.
    Trả về:
        Tuple gồm (dem_12_thang, lech_12_thang).
    """
    loc_rv = rv.loc[rv["date"].between(pd.Timestamp(bat_dau), pd.Timestamp(ket_thuc))]
    dem = loc_rv.groupby("listing_id").size()
    dem_12 = ds["id"].map(dem).fillna(0).astype(int)
    dem_12.index = ds["id"]
    lech_12 = dem_12 - ds.set_index("id")["number_of_reviews_ltm"]
    return dem_12, lech_12


kq_ltm_c2 = ltm_mismatch(DEMO_RV, DEMO_DS, LTM_BAT_DAU)
dem12_c2, lech12_c2 = doi_chieu_12_thang_co_dinh(DEMO_RV, DEMO_DS, LTM_BAT_DAU, MOC)
assert kq_ltm_c1["so_lech_ltm"] == kq_ltm_c2["so_lech_ltm"] and dem12_c1.equals(
    dem12_c2
)
print("Xác nhận Cách 2: Đối chiếu LTM thành công")

# Kết thúc lời giải
```

#### Giải thích cách 2

Tách mặt nạ thời gian, bảng đếm và phép đối chiếu giúp kiểm lại từng giả thiết về 12 tháng. Xem cả phân bố độ lệch, không chỉ đếm số dòng khác 0. Nếu thay cận trên bằng snapshot, phải tính lại và ghi đó là một định nghĩa cửa sổ khác.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Đối chiếu LTM thành công
```
#### So sánh cách dùng

Cách 1 giúp tái hiện phép đếm từ mốc bắt đầu mà chưa chặn phía sau snapshot. Cách 2 dùng một khoảng ngày cố định. Khi có review mang ngày sau snapshot, hai quy tắc có thể cho số đếm khác nhau và cần được ghi rõ trong báo cáo.

:::

---

## Bài 11: Đóng gói báo cáo kiểm tra chất lượng dữ liệu

<span id="data-lab-10-11"></span>

::: exercise
**Mục tiêu**: Đóng gói toàn bộ các chỉ số kiểm định chất lượng dữ liệu chéo bảng thành một báo cáo chuẩn mực `qa_report` gồm đúng ba cột, ghi xuất ra tệp định dạng CSV và đọc lại để kiểm tra tính nguyên vẹn. Xây dựng hàm `tom_tat_co` tính toán tỷ lệ phần trăm vi phạm theo từng bảng và trích xuất danh sách các dòng bị gắn cờ kèm dữ liệu gốc.

**Dữ liệu đầu vào**:
1. Từ điển số liệu kiểm tra `so_lieu`: Chứa số dòng vi phạm của các quy tắc (`review_sau_moc`, `review_mo_coi`, `trung_theo_cap`, `lech_tong_review`, `lech_ltm`).
2. Từ điển ghi chú nghiệp vụ `ghi_chu`: Chứa diễn giải tương ứng của từng quy tắc.

**Thao tác yêu cầu**:
1. Viết hàm `qa_report(so_dong: dict, ghi_chu: dict, path) -> pd.DataFrame` tạo DataFrame gồm ba cột `quy_tac`, `so_dong`, `ghi_chu`. Bảo toàn thứ tự khóa của `so_dong`, giữ nguyên các quy tắc có 0 dòng vi phạm, điền chuỗi rỗng `""` cho quy tắc không có ghi chú. Xuất tệp CSV với `index=False` và đọc lại bằng `pd.read_csv(path, keep_default_na=False)`.
2. Viết hàm `tom_tat_co(co: pd.DataFrame, ten_bang: str) -> pd.DataFrame` trả về bảng tổng kết gồm các cột: `quy_tac`, `bang`, `so_hang`, `tong_hang`, `ty_le_pct`.
3. Trích xuất các hàng có ít nhất một cờ vi phạm bằng `co.any(axis=1)` và ghép nối với dữ liệu gốc bằng `join`.

**Trường hợp biên cần chú ý**: Khi ghi và đọc lại CSV, tham số `keep_default_na=False` giúp chuỗi ghi chú rỗng không bị pandas tự động chuyển thành giá trị `NaN`.
:::

::: solution
#### Cách 1: Xây dựng bảng từ danh sách bản ghi tuần tự

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)


def kiem_reviews_buoc(r: pd.DataFrame, ids, moc: str) -> pd.DataFrame:
    """Tạo bảng cờ kiểm tra đánh giá theo từng bước.

    Tham số:
        r: DataFrame chứa 'listing_id' và 'date'.
        ids: Tập hợp hoặc Series các mã chỗ ở hợp lệ.
        moc: Mốc chụp công bố.
    Trả về:
        DataFrame gồm ba cột cờ boolean: ngay_thieu, sau_moc, id_khong_khop.
    """
    moc_ts = pd.Timestamp(moc)
    co_ngay_thieu = r["date"].isna()
    co_sau_moc = r["date"].notna() & (r["date"] > moc_ts)
    co_id_khong_khop = ~r["listing_id"].isin(ids)

    return pd.DataFrame(
        {
            "ngay_thieu": co_ngay_thieu.astype(bool),
            "sau_moc": co_sau_moc.astype(bool),
            "id_khong_khop": co_id_khong_khop.astype(bool),
        },
        index=r.index,
    )


def kiem_reviews(r: pd.DataFrame, ids, moc: str) -> pd.DataFrame:
    """Tạo bảng cờ boolean kiểm tra đánh giá vector hóa.

    Tham số:
        r: DataFrame có 'listing_id' và 'date'.
        ids: Danh sách mã chỗ ở hợp lệ.
        moc: Mốc công bố.
    Trả về:
        DataFrame gồm ba cột cờ boolean.
    """
    d = r["date"]
    moc_ts = pd.Timestamp(moc)
    return pd.DataFrame(
        {
            "ngay_thieu": d.isna(),
            "sau_moc": (d.notna() & (d > moc_ts)).fillna(False).astype(bool),
            "id_khong_khop": (~r["listing_id"].isin(ids)).astype(bool),
        },
        index=r.index,
    )


co_rv_c1 = kiem_reviews_buoc(DEMO_RV, DEMO_DS["id"], MOC)
co_rv_c2 = kiem_reviews(DEMO_RV, DEMO_DS["id"], MOC)

# Bắt đầu lời giải

import tempfile
from pathlib import Path


def qa_report_records(so_dong: dict, ghi_chu: dict, path) -> pd.DataFrame:
    """Tạo và ghi báo cáo QA từ danh sách bản ghi tuần tự.

    Tham số:
        so_dong: Dict {ten_quy_tac: so_dong_vi_pham}.
        ghi_chu: Dict {ten_quy_tac: chuoi_ghi_chu}.
        path: Đường dẫn lưu tệp CSV.
    Trả về:
        DataFrame đọc lại từ tệp CSV vừa ghi.
    """
    ban_ghi = []
    for quy_tac, so in so_dong.items():
        note = ghi_chu.get(quy_tac, "")
        ban_ghi.append({"quy_tac": quy_tac, "so_dong": int(so), "ghi_chu": str(note)})
    df = pd.DataFrame(ban_ghi)
    df.to_csv(path, index=False, encoding="utf-8")
    return pd.read_csv(path, keep_default_na=False)


def tom_tat_co_buoc(co: pd.DataFrame, ten_bang: str) -> pd.DataFrame:
    """Tạo bảng tóm tắt tỷ lệ cờ vi phạm tuần tự.

    Tham số:
        co: DataFrame các cột cờ boolean.
        ten_bang: Tên bảng dữ liệu ('listings' hoặc 'reviews').
    Trả về:
        DataFrame tóm tắt tỷ lệ.
    """
    tong = len(co)
    hang = []
    for col in co.columns:
        so_vi_pham = int(co[col].sum())
        ty_le = round((so_vi_pham / tong) * 100, 2) if tong > 0 else 0.0
        hang.append(
            {
                "quy_tac": col,
                "bang": ten_bang,
                "so_hang": so_vi_pham,
                "tong_hang": tong,
                "ty_le_pct": ty_le,
            }
        )
    return pd.DataFrame(hang)


# Dữ liệu mẫu thử nghiệm
so_lieu_demo = {
    "review_sau_moc": 3,
    "review_mo_coi": 0,
    "trung_theo_cap": 3,
    "lech_tong_review": 0,
    "lech_ltm": 2,
}
ghi_chu_demo = {
    "review_sau_moc": "date > mốc công bố 2026-06-29",
    "review_mo_coi": "listing_id không có trong listings",
    "trung_theo_cap": "không xóa do không phải khóa tự nhiên",
    "lech_tong_review": "cột dẫn xuất so với số tự đếm",
    "lech_ltm": "khác định nghĩa mốc 12 tháng",
}

with tempfile.TemporaryDirectory() as thu_muc_tam:
    duong_dan_tam = Path(thu_muc_tam) / "qa_report_c1.csv"
    bao_cao_c1 = qa_report_records(so_lieu_demo, ghi_chu_demo, duong_dan_tam)
    bang_tt_c1 = tom_tat_co_buoc(co_rv_c1, "reviews")
    print("Nội dung báo cáo QA Cách 1:")
    print(bao_cao_c1)
    print("Bảng tóm tắt cờ vi phạm Cách 1:")
    print(bang_tt_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Dựng từng bản ghi báo cáo theo thứ tự khóa của dict số dòng. Quy tắc có số dòng bằng 0 vẫn phải xuất hiện để phân biệt đã kiểm và không kiểm. `to_csv(index=False)` bỏ chỉ mục phụ, rồi đọc lại tệp để xác nhận cấu trúc xuất ra.

#### Kết quả cách 1

| Chỉ mục | quy_tac | bang | so_hang | tong_hang | ty_le_pct |
| --- | --- | --- | --- | --- | --- |
| 0 | ngay_thieu | reviews | 0 | 18 | 0 |
| 1 | sau_moc | reviews | 3 | 18 | 16.67 |
| 2 | id_khong_khop | reviews | 0 | 18 | 0 |

#### Cách 2: Sử dụng phương thức khởi tạo DataFrame từ từ điển và chuỗi thao tác

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

MOC = "2026-06-29"

LTM_BAT_DAU = "2025-06-30"

DEMO_RV = pd.DataFrame(
    {
        "listing_id": [
            11,
            11,
            11,
            11,
            11,
            11,
            11,
            12,
            12,
            12,
            12,
            13,
            13,
            13,
            13,
            14,
            14,
            16,
        ],
        "date": pd.to_datetime(
            [
                "2019-03-01",
                "2024-12-01",
                "2025-06-30",
                "2025-08-10",
                "2025-08-10",
                "2026-06-29",
                "2026-06-30",
                "2010-11-13",
                "2025-06-30",
                "2026-01-05",
                "2026-07-01",
                "2023-04-04",
                "2023-04-04",
                "2023-04-04",
                "2025-07-01",
                "2025-12-24",
                "2026-06-30",
                "2021-02-02",
            ]
        ),
    }
)

DEMO_DS = pd.DataFrame(
    {
        "id": [11, 12, 13, 14, 15, 16],
        "name": [
            "Depto Lastarria",
            "Pieza Bellavista",
            "Loft Providencia",
            "Casa Ñuñoa",
            "Studio nuevo",
            "Hab Centro",
        ],
        "number_of_reviews": [7, 4, 4, 2, 0, 1],
        "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
        "last_review": pd.to_datetime(
            ["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]
        ),
    }
)


def kiem_reviews_buoc(r: pd.DataFrame, ids, moc: str) -> pd.DataFrame:
    """Tạo bảng cờ kiểm tra đánh giá theo từng bước.

    Tham số:
        r: DataFrame chứa 'listing_id' và 'date'.
        ids: Tập hợp hoặc Series các mã chỗ ở hợp lệ.
        moc: Mốc chụp công bố.
    Trả về:
        DataFrame gồm ba cột cờ boolean: ngay_thieu, sau_moc, id_khong_khop.
    """
    moc_ts = pd.Timestamp(moc)
    co_ngay_thieu = r["date"].isna()
    co_sau_moc = r["date"].notna() & (r["date"] > moc_ts)
    co_id_khong_khop = ~r["listing_id"].isin(ids)

    return pd.DataFrame(
        {
            "ngay_thieu": co_ngay_thieu.astype(bool),
            "sau_moc": co_sau_moc.astype(bool),
            "id_khong_khop": co_id_khong_khop.astype(bool),
        },
        index=r.index,
    )


def kiem_reviews(r: pd.DataFrame, ids, moc: str) -> pd.DataFrame:
    """Tạo bảng cờ boolean kiểm tra đánh giá vector hóa.

    Tham số:
        r: DataFrame có 'listing_id' và 'date'.
        ids: Danh sách mã chỗ ở hợp lệ.
        moc: Mốc công bố.
    Trả về:
        DataFrame gồm ba cột cờ boolean.
    """
    d = r["date"]
    moc_ts = pd.Timestamp(moc)
    return pd.DataFrame(
        {
            "ngay_thieu": d.isna(),
            "sau_moc": (d.notna() & (d > moc_ts)).fillna(False).astype(bool),
            "id_khong_khop": (~r["listing_id"].isin(ids)).astype(bool),
        },
        index=r.index,
    )


co_rv_c1 = kiem_reviews_buoc(DEMO_RV, DEMO_DS["id"], MOC)
co_rv_c2 = kiem_reviews(DEMO_RV, DEMO_DS["id"], MOC)

so_lieu_demo = {
    "review_sau_moc": 3,
    "review_mo_coi": 0,
    "trung_theo_cap": 3,
    "lech_tong_review": 0,
    "lech_ltm": 2,
}

ghi_chu_demo = {
    "review_sau_moc": "date > mốc công bố 2026-06-29",
    "review_mo_coi": "listing_id không có trong listings",
    "trung_theo_cap": "không xóa do không phải khóa tự nhiên",
    "lech_tong_review": "cột dẫn xuất so với số tự đếm",
    "lech_ltm": "khác định nghĩa mốc 12 tháng",
}


def qa_report_records(so_dong: dict, ghi_chu: dict, path) -> pd.DataFrame:
    """Tạo và ghi báo cáo QA từ danh sách bản ghi tuần tự.

    Tham số:
        so_dong: Dict {ten_quy_tac: so_dong_vi_pham}.
        ghi_chu: Dict {ten_quy_tac: chuoi_ghi_chu}.
        path: Đường dẫn lưu tệp CSV.
    Trả về:
        DataFrame đọc lại từ tệp CSV vừa ghi.
    """
    ban_ghi = []
    for quy_tac, so in so_dong.items():
        note = ghi_chu.get(quy_tac, "")
        ban_ghi.append({"quy_tac": quy_tac, "so_dong": int(so), "ghi_chu": str(note)})
    df = pd.DataFrame(ban_ghi)
    df.to_csv(path, index=False, encoding="utf-8")
    return pd.read_csv(path, keep_default_na=False)


def tom_tat_co_buoc(co: pd.DataFrame, ten_bang: str) -> pd.DataFrame:
    """Tạo bảng tóm tắt tỷ lệ cờ vi phạm tuần tự.

    Tham số:
        co: DataFrame các cột cờ boolean.
        ten_bang: Tên bảng dữ liệu ('listings' hoặc 'reviews').
    Trả về:
        DataFrame tóm tắt tỷ lệ.
    """
    tong = len(co)
    hang = []
    for col in co.columns:
        so_vi_pham = int(co[col].sum())
        ty_le = round((so_vi_pham / tong) * 100, 2) if tong > 0 else 0.0
        hang.append(
            {
                "quy_tac": col,
                "bang": ten_bang,
                "so_hang": so_vi_pham,
                "tong_hang": tong,
                "ty_le_pct": ty_le,
            }
        )
    return pd.DataFrame(hang)


import tempfile
from pathlib import Path

with tempfile.TemporaryDirectory() as report_folder:
    bao_cao_c1 = qa_report_records(
        so_lieu_demo, ghi_chu_demo, Path(report_folder) / "reference.csv"
    )
bang_tt_c1 = tom_tat_co_buoc(co_rv_c1, "reviews")

# Bắt đầu lời giải


def qa_report(so_dong: dict, ghi_chu: dict, path) -> pd.DataFrame:
    """Hàm tạo báo cáo QA chuẩn mực của hệ thống.

    Tham số:
        so_dong: Dict số dòng vi phạm.
        ghi_chu: Dict ghi chú nghiệp vụ.
        path: Đường dẫn tệp đích.
    Trả về:
        DataFrame đọc lại từ file.
    """
    danh_sach_qt = list(so_dong.keys())
    df = pd.DataFrame(
        {
            "quy_tac": danh_sach_qt,
            "so_dong": [int(so_dong[k]) for k in danh_sach_qt],
            "ghi_chu": [str(ghi_chu.get(k, "")) for k in danh_sach_qt],
        }
    )
    df.to_csv(path, index=False, encoding="utf-8")
    return pd.read_csv(path, keep_default_na=False)


def tom_tat_co(co: pd.DataFrame, ten_bang: str) -> pd.DataFrame:
    """Tạo bảng tóm tắt tỷ lệ cờ vi phạm vector hóa.

    Tham số:
        co: DataFrame boolean các cờ.
        ten_bang: Tên bảng.
    Trả về:
        DataFrame tóm tắt gồm quy_tac, bang, so_hang, tong_hang, ty_le_pct.
    """
    bao_cao = pd.DataFrame(
        {
            "bang": ten_bang,
            "so_hang": co.sum().astype(int),
            "tong_hang": len(co),
            "ty_le_pct": (co.mean() * 100).round(2),
        }
    )
    return bao_cao.rename_axis("quy_tac").reset_index()


with tempfile.TemporaryDirectory() as thu_muc_tam:
    duong_dan_tam = Path(thu_muc_tam) / "qa_report_c2.csv"
    bao_cao_c2 = qa_report(so_lieu_demo, ghi_chu_demo, duong_dan_tam)
    bang_tt_c2 = tom_tat_co(co_rv_c2, "reviews")
    assert bao_cao_c1.equals(bao_cao_c2) and bang_tt_c1.equals(
        bang_tt_c2
    ), "Kết quả hai cách phải đồng nhất tuyệt đối"
    print("Xác nhận Cách 2: Xuất báo cáo và tóm tắt cờ thành công")

# Kết thúc lời giải
```

#### Giải thích cách 2

Tạo DataFrame trực tiếp từ dữ liệu có cấu trúc giảm bước ghép từng dòng. `ghi_chu.get(..., "")` cho ghi chú rỗng khi chưa có nội dung, không làm mất quy tắc. `keep_default_na=False` khi đọc lại giữ chuỗi rỗng thay vì đổi thành NaN.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Xuất báo cáo và tóm tắt cờ thành công
```
#### So sánh cách dùng

Hãy chọn Cách 1 khi các chỉ số kiểm tra được thu thập rời rạc và bạn muốn chủ động ghép từng dòng theo thứ tự sẵn có. Cách 2 thích hợp khi dữ liệu đã có sẵn dạng từ điển và bạn muốn tạo ngay bảng tổng kết để xuất tệp CSV.

:::

---

## Bài 12: Tách nhóm khóa có giá trị mâu thuẫn trước khi hợp nhất

<span id="data-lab-10-12"></span>

::: exercise
**Mục tiêu**: Xử lý dữ liệu bảng giá nhập `gia_nhap` thu thập từ nhiều đợt xuất khác nhau theo khóa tổ hợp `(id, ky)`. Phân tách dữ liệu thành hai bảng riêng biệt: Bảng `gia_gop` gồm đúng một hàng cho mỗi khóa không có mâu thuẫn, và bảng `gia_can_xem` lưu giữ toàn bộ các hàng của những khóa có từ hai giá trị đã biết khác nhau.

**Dữ liệu đầu vào**: Bảng `gia_nhap` gồm 9 hàng, có ba cột `id`, `ky`, `gia` (USD/đêm) với các kịch bản: Hai giá giống nhau, một giá đã biết kèm một ô thiếu, toàn bộ ô thiếu, và hai giá đã biết khác nhau.

**Thao tác yêu cầu**:
1. Xác định điều kiện mâu thuẫn: Một khóa `(id, ky)` bị coi là mâu thuẫn khi và chỉ khi nó có từ 2 giá trị đã biết khác nhau trở lên (`s.dropna().nunique() > 1`).
2. Xây dựng bảng `gia_gop`: Chứa các khóa không mâu thuẫn (mỗi khóa đúng một hàng). Nếu khóa có một giá đã biết và ô thiếu, giữ giá đã biết, còn nếu nhóm toàn ô thiếu, giữ nguyên `NaN`.
3. Xây dựng bảng `gia_can_xem`: Giữ nguyên toàn bộ các dòng của các khóa có mâu thuẫn giá để phục vụ thẩm định chuyên sâu.
4. Bảo đảm không làm thay đổi bảng dữ liệu ban đầu `gia_nhap`.

**Trường hợp biên cần chú ý**: Trường hợp một khóa có một giá 110 và một giá trị `NaN` không cấu thành mâu thuẫn, chỉ phản ánh một đợt xuất thiếu thông tin.
:::

::: solution
#### Cách 1: Phân tách nhóm bằng vòng lặp và tập hợp giá trị duy nhất

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

# Bắt đầu lời giải


def tach_gia_mau_thuan_vong_lap(
    gia_nhap: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Tách nhóm giá mâu thuẫn bằng vòng lặp nhóm tuần tự.

    Tham số:
        gia_nhap: DataFrame chứa 'id', 'ky', 'gia'.
    Trả về:
        Tuple gồm (gia_gop, gia_can_xem).
    """
    df = gia_nhap.copy()
    nhom = df.groupby(["id", "ky"])
    hang_can_xem = []
    hang_gop = []

    for (ma_id, ma_ky), grp in nhom:
        gia_khong_na = grp["gia"].dropna().unique()
        if len(gia_khong_na) > 1:
            hang_can_xem.append(grp)
        else:
            val = gia_khong_na[0] if len(gia_khong_na) == 1 else np.nan
            hang_gop.append({"id": ma_id, "ky": ma_ky, "gia": val})

    gia_can_xem = (
        pd.concat(hang_can_xem).sort_index()
        if hang_can_xem
        else pd.DataFrame(columns=["id", "ky", "gia"])
    )
    gia_gop = pd.DataFrame(hang_gop)
    return gia_gop, gia_can_xem


# Dữ liệu thử nghiệm minh họa
gia_nhap_demo = pd.DataFrame(
    {
        "id": ["P1", "P2", "P3", "P4", "P1", "P2", "P3", "P4", "P1"],
        "ky": ["T6", "T6", "T6", "T6", "T6", "T6", "T6", "T6", "T5"],
        "gia": [120.0, 90.0, np.nan, np.nan, 120.0, 95.0, 110.0, np.nan, 100.0],
    }
)

gop_c1, xem_c1 = tach_gia_mau_thuan_vong_lap(gia_nhap_demo)
print("Bảng hợp nhất gia_gop Cách 1:")
print(gop_c1)
print("Các hàng mâu thuẫn gia_can_xem Cách 1:")
print(xem_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Nhóm các bản ghi có cùng khóa rồi xem số mức giá phân biệt. Những nhóm có nhiều giá phải được giữ riêng để đối chiếu, không chọn tùy ý dòng đầu rồi gọi là làm sạch. Các dòng không mâu thuẫn có thể chuyển sang bước gộp theo đúng quy tắc đã nêu.

#### Kết quả cách 1

| Chỉ mục | id | ky | gia |
| --- | --- | --- | --- |
| 1 | P2 | T6 | 90 |
| 5 | P2 | T6 | 95 |

#### Cách 2: Sử dụng transform vector hóa và lọc chỉ mục

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

gia_nhap_demo = pd.DataFrame(
    {
        "id": ["P1", "P2", "P3", "P4", "P1", "P2", "P3", "P4", "P1"],
        "ky": ["T6", "T6", "T6", "T6", "T6", "T6", "T6", "T6", "T5"],
        "gia": [120.0, 90.0, np.nan, np.nan, 120.0, 95.0, 110.0, np.nan, 100.0],
    }
)


def tach_gia_mau_thuan_vong_lap(
    gia_nhap: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Tách nhóm giá mâu thuẫn bằng vòng lặp nhóm tuần tự.

    Tham số:
        gia_nhap: DataFrame chứa 'id', 'ky', 'gia'.
    Trả về:
        Tuple gồm (gia_gop, gia_can_xem).
    """
    df = gia_nhap.copy()
    nhom = df.groupby(["id", "ky"])
    hang_can_xem = []
    hang_gop = []

    for (ma_id, ma_ky), grp in nhom:
        gia_khong_na = grp["gia"].dropna().unique()
        if len(gia_khong_na) > 1:
            hang_can_xem.append(grp)
        else:
            val = gia_khong_na[0] if len(gia_khong_na) == 1 else np.nan
            hang_gop.append({"id": ma_id, "ky": ma_ky, "gia": val})

    gia_can_xem = (
        pd.concat(hang_can_xem).sort_index()
        if hang_can_xem
        else pd.DataFrame(columns=["id", "ky", "gia"])
    )
    gia_gop = pd.DataFrame(hang_gop)
    return gia_gop, gia_can_xem


gop_c1, xem_c1 = tach_gia_mau_thuan_vong_lap(gia_nhap_demo)

# Bắt đầu lời giải


def tach_gia_mau_thuan(gia_nhap: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Tách nhóm giá mâu thuẫn bằng kỹ thuật transform vector hóa.

    Tham số:
        gia_nhap: DataFrame có 'id', 'ky', 'gia'.
    Trả về:
        Tuple gồm (gia_gop, gia_can_xem).
    """
    df = gia_nhap.copy()
    so_gia_rieng = df.groupby(["id", "ky"])["gia"].transform(
        lambda s: s.dropna().nunique()
    )
    gia_can_xem = df[so_gia_rieng > 1].copy()

    khong_mau_thuan = df[so_gia_rieng <= 1]
    gia_gop = (
        khong_mau_thuan.sort_values(by=["id", "ky", "gia"], na_position="last")
        .drop_duplicates(subset=["id", "ky"], keep="first")
        .reset_index(drop=True)
    )
    return gia_gop, gia_can_xem


gop_c2, xem_c2 = tach_gia_mau_thuan(gia_nhap_demo)
assert len(gop_c1) == len(gop_c2) and len(xem_c1) == len(
    xem_c2
), "Hai cách phải cho kết quả đồng nhất"
print("Xác nhận Cách 2: Tách nhóm mâu thuẫn vector hóa hoàn tất")

# Kết thúc lời giải
```

#### Giải thích cách 2

`nunique` và `transform` tạo cờ mâu thuẫn tương ứng từng dòng. Phép chọn bằng cờ giữ cả nhóm để kiểm tra nguồn, ngày hoặc đơn vị. Cần thống nhất cách xử lý giá thiếu khi đếm mức giá, vì một ô thiếu không tự mang một mức giá mới.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Tách nhóm mâu thuẫn vector hóa hoàn tất
```
#### So sánh cách dùng

Cách 1 mở từng nhóm chỗ ở và ngày để xem các mức giá mâu thuẫn. Cách 2 gắn cùng quy tắc kiểm lên bảng để lọc các dòng liên quan. Hãy giữ cả giá trị gốc và cờ mâu thuẫn trước khi quyết định cách gộp.

:::

---

## Bài 13: Điền mốt, truyền giá trị phía trước theo nhóm và nội suy thời gian

<span id="data-lab-10-13"></span>

::: exercise
**Mục tiêu**: Làm chủ ba phương pháp điền khuyết nâng cao cho từng loại cấu trúc dữ liệu đặc thù:
1. Điền mốt (mode - giá trị xuất hiện nhiều nhất) cho biến phân loại danh mục `loai`.
2. Sắp xếp dữ liệu theo khóa đa cấp `(id, ky)` và truyền giá trị đã biết phía trước (`ffill`) riêng biệt theo từng chỗ ở với giới hạn `limit=1` trên bảng `lich_gia`.
3. Nội suy theo khoảng cách thời gian (`method="time"`) trên chuỗi thời gian `nhiet_do` có chỉ mục ngày không cách đều, bảo đảm không ngoại suy ngoài miền quan sát.

**Dữ liệu đầu vào**:
1. Series `loai_demo` gồm 5 chỗ ở, chỗ ở P4 bị thiếu loại phòng.
2. Bảng `lich_demo` gồm 8 hàng chưa được sắp xếp, ghi nhận giá qua 4 kỳ của hai chỗ ở P1 và P2.
3. Series `nhiet_do_demo` ghi nhận nhiệt độ qua các ngày không liên tục (ngày 01, 02, 05, 07, 08 tháng 06 năm 2026).

**Thao tác yêu cầu**:
1. Tạo Series `loai_dien`: Điền ô thiếu bằng giá trị mốt của các loại phòng đã biết.
2. Tạo DataFrame `lich_dien`: Sắp xếp theo `id` rồi `ky`, thêm cột `dien` bằng giá trị phía trước của cùng chỗ ở, tối đa một ô thiếu liên tiếp (`limit=1`).
3. Tạo Series `noi_suy`: Nội suy giá trị theo khoảng cách thời gian thực tế giữa các mốc ngày.

**Trường hợp biên cần chú ý**:
- Nếu không nhóm theo `id` trước khi `ffill`, giá của chỗ ở này sẽ bị truyền nhầm sang chỗ ở khác.
- Tại ngày cuối cùng của chuỗi thời gian (ngày 08/06), vì không có mốc dữ liệu phía sau để nội suy nên bắt buộc phải giữ nguyên `NaN`.
:::

::: solution
#### Cách 1: Xử lý tuần tự từng bước logic

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

# Bắt đầu lời giải


def dien_khuyet_chuyen_sau_buoc(
    loai: pd.Series, lich_gia: pd.DataFrame, nhiet_do: pd.Series
) -> tuple[pd.Series, pd.DataFrame, pd.Series]:
    """Thực hiện ba kỹ thuật điền khuyết chuyên sâu theo cách tuần tự.

    Tham số:
        loai: Series biến phân loại.
        lich_gia: DataFrame chưa sắp xếp có 'id', 'ky', 'gia'.
        nhiet_do: Series có DatetimeIndex không cách đều.
    Trả về:
        Tuple gồm (loai_dien, lich_dien, noi_suy).
    """
    # 1. Điền mốt
    gia_tri_mot = loai.mode()[0]
    loai_dien = loai.fillna(gia_tri_mot)

    # 2. Sắp xếp và ffill theo nhóm
    lich_dien = lich_gia.sort_values(by=["id", "ky"]).reset_index(drop=True)
    cot_dien = []
    for _, grp in lich_dien.groupby("id", sort=False):
        cot_dien.append(grp["gia"].ffill(limit=1))
    lich_dien["dien"] = pd.concat(cot_dien).values

    # 3. Nội suy theo thời gian
    noi_suy = nhiet_do.interpolate(method="time", limit_area="inside")

    return loai_dien, lich_dien, noi_suy


# Dữ liệu thử nghiệm minh họa
loai_demo = pd.Series(
    ["Nguyên căn", "Phòng riêng", "Nguyên căn", None, "Nguyên căn"],
    index=["P1", "P2", "P3", "P4", "P5"],
)
lich_demo = pd.DataFrame(
    {
        "id": ["P2", "P1", "P1", "P2", "P1", "P2", "P1", "P2"],
        "ky": [3, 1, 4, 1, 2, 2, 3, 4],
        "gia": [np.nan, 100.0, 130.0, np.nan, np.nan, 200.0, np.nan, np.nan],
    }
)
nhiet_do_demo = pd.Series(
    [18.0, np.nan, np.nan, 24.0, np.nan],
    index=pd.to_datetime(
        ["2026-06-01", "2026-06-02", "2026-06-05", "2026-06-07", "2026-06-08"]
    ),
)

loai_c1, lich_c1, ns_c1 = dien_khuyet_chuyen_sau_buoc(
    loai_demo, lich_demo, nhiet_do_demo
)
print("Kết quả điền mốt Cách 1:", loai_c1)
print("Kết quả ffill theo nhóm Cách 1:", lich_c1)
print("Kết quả nội suy thời gian Cách 1:", ns_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Mốt, giá trước đó và nội suy dùng những giả thiết khác nhau. Mốt dựa vào giá trị xuất hiện nhiều trong một nhóm, forward fill dùng quan sát trước, còn nội suy dùng vị trí giữa các mốc đã có. Kiểm thứ tự thời gian và ranh giới từng nhóm trước khi điền.

#### Kết quả cách 1

| Chỉ mục | Giá trị |
| --- | --- |
| 2026-06-01 00:00:00 | 18 |
| 2026-06-02 00:00:00 | 19 |
| 2026-06-05 00:00:00 | 22 |
| 2026-06-07 00:00:00 | 24 |
| 2026-06-08 00:00:00 | NaN |

#### Cách 2: Sử dụng các phương thức chuyên dụng của pandas

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

loai_demo = pd.Series(
    ["Nguyên căn", "Phòng riêng", "Nguyên căn", None, "Nguyên căn"],
    index=["P1", "P2", "P3", "P4", "P5"],
)

lich_demo = pd.DataFrame(
    {
        "id": ["P2", "P1", "P1", "P2", "P1", "P2", "P1", "P2"],
        "ky": [3, 1, 4, 1, 2, 2, 3, 4],
        "gia": [np.nan, 100.0, 130.0, np.nan, np.nan, 200.0, np.nan, np.nan],
    }
)

nhiet_do_demo = pd.Series(
    [18.0, np.nan, np.nan, 24.0, np.nan],
    index=pd.to_datetime(
        ["2026-06-01", "2026-06-02", "2026-06-05", "2026-06-07", "2026-06-08"]
    ),
)


def dien_khuyet_chuyen_sau_buoc(
    loai: pd.Series, lich_gia: pd.DataFrame, nhiet_do: pd.Series
) -> tuple[pd.Series, pd.DataFrame, pd.Series]:
    """Thực hiện ba kỹ thuật điền khuyết chuyên sâu theo cách tuần tự.

    Tham số:
        loai: Series biến phân loại.
        lich_gia: DataFrame chưa sắp xếp có 'id', 'ky', 'gia'.
        nhiet_do: Series có DatetimeIndex không cách đều.
    Trả về:
        Tuple gồm (loai_dien, lich_dien, noi_suy).
    """
    # 1. Điền mốt
    gia_tri_mot = loai.mode()[0]
    loai_dien = loai.fillna(gia_tri_mot)

    # 2. Sắp xếp và ffill theo nhóm
    lich_dien = lich_gia.sort_values(by=["id", "ky"]).reset_index(drop=True)
    cot_dien = []
    for _, grp in lich_dien.groupby("id", sort=False):
        cot_dien.append(grp["gia"].ffill(limit=1))
    lich_dien["dien"] = pd.concat(cot_dien).values

    # 3. Nội suy theo thời gian
    noi_suy = nhiet_do.interpolate(method="time", limit_area="inside")

    return loai_dien, lich_dien, noi_suy


loai_c1, lich_c1, ns_c1 = dien_khuyet_chuyen_sau_buoc(
    loai_demo, lich_demo, nhiet_do_demo
)

# Bắt đầu lời giải


def dien_khuyet_chuyen_sau(
    loai: pd.Series, lich_gia: pd.DataFrame, nhiet_do: pd.Series
) -> tuple[pd.Series, pd.DataFrame, pd.Series]:
    """Thực hiện điền mốt, ffill theo nhóm và nội suy thời gian vector hóa.

    Tham số:
        loai: Series phân loại.
        lich_gia: DataFrame lịch giá.
        nhiet_do: Series thời gian.
    Trả về:
        Tuple gồm (loai_dien, lich_dien, noi_suy).
    """
    loai_dien = loai.fillna(loai.mode().iloc[0])

    lich_dien = lich_gia.sort_values(by=["id", "ky"]).reset_index(drop=True)
    lich_dien["dien"] = lich_dien.groupby("id")["gia"].ffill(limit=1)

    noi_suy = nhiet_do.interpolate(method="time", limit_area="inside")
    return loai_dien, lich_dien, noi_suy


loai_c2, lich_c2, ns_c2 = dien_khuyet_chuyen_sau(loai_demo, lich_demo, nhiet_do_demo)
assert loai_c1.equals(loai_c2) and lich_c1.equals(lich_c2) and ns_c1.equals(ns_c2)
print("Xác nhận Cách 2: Toàn bộ ba phương pháp điền khuyết hoàn tất")

# Kết thúc lời giải
```

#### Giải thích cách 2

Các phương thức theo nhóm và chỉ mục giúp áp dụng quy tắc nhất quán. Không để forward fill chảy từ chỗ ở này sang chỗ ở khác hoặc dùng dữ liệu tương lai trong bài toán dự báo. Nội suy ở giữa hai mốc có căn cứ khác với ngoại suy ra đầu hoặc cuối chuỗi.

#### Kết quả cách 2

```text
Xác nhận Cách 2: Toàn bộ ba phương pháp điền khuyết hoàn tất
```
#### So sánh cách dùng

Cách 1 mở riêng từng thao tác điền mốt, lan truyền giá và nội suy. Cách 2 thể hiện các phép xử lý theo nhóm và chỉ mục. Cả hai vẫn cần giả thiết phù hợp, thứ tự thời gian đúng và giới hạn nhóm rõ ràng trước khi điền.

:::

---

## Tổng kết bài học và hướng dẫn thực hành chuyên sâu

Quy trình kiểm định chất lượng và làm sạch dữ liệu chéo bảng đòi hỏi sự kết hợp chặt chẽ giữa tư duy thống kê toán học và sự thấu hiểu sâu sắc bản chất nghiệp vụ dữ liệu:

1. **Điền khuyết có căn cứ**: Chỉ điền 0 cho biến đếm khi hiện tượng chắc chắn chưa từng phát sinh, còn đối với biến đo lường chất lượng hoặc giá cả, việc điền trung vị theo nhóm phân loại phải luôn đi kèm cờ đánh dấu nguồn gốc dữ liệu.
2. **Kiểm tra biên và ngoại lai**: Phân biệt rõ ràng giữa giá thiếu (vắng mặt thông tin) với giá không dương (lỗi logic nghiệp vụ). Trên phân phối lệch phải mạnh, ngưỡng phân vị P99 mang lại khả năng khoanh vùng rà soát thực tế hơn nhiều so với ngưỡng tứ phân vị IQR.
3. **Bản chất của khóa tự nhiên**: Tuyệt đối không nhầm lẫn giữa sự kiện độc lập trùng thuộc tính với bản ghi nhập lặp từ cơ sở dữ liệu. Không tự ý gọi `drop_duplicates` trên các thuộc tính không phải là khóa tự nhiên.
4. **Đối soát cột dẫn xuất**: Luôn kiểm tra định nghĩa biên thời gian và phạm vi tích lũy của nhà cung cấp trước khi vội vã đưa ra kết luận rằng cột số liệu bị sai sót.
5. **Chuẩn hóa báo cáo kiểm định**: Duy trì đầy đủ các bài kiểm tra đạt chuẩn (kết quả bằng 0 vi phạm) để bảo đảm tính toàn diện và khả năng kiểm toán của hồ sơ dữ liệu.
