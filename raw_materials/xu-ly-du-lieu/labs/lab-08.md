## Lab 8: Chuỗi thời gian - Quý, cửa sổ trượt và so sánh cùng kỳ

Một tổng số đánh giá theo tháng có thể giảm chỉ vì tháng đó ngắn hơn hoặc chưa được quan sát đủ. Bộ bài này dùng ngày, quý và cửa sổ trượt để kiểm tra phạm vi thời gian trước khi so sánh số liệu.

---

## 1. Mục tiêu và bài toán thực tế

Xét bài toán thực tế: Một nhóm nghiên cứu thị trường cần xây dựng báo cáo phân tích chuỗi thời gian về nhu cầu lưu trú du lịch tại vùng đô thị Santiago de Chile. Bản báo cáo cần trả lời các câu hỏi định lượng cốt lõi:
1. Tính toán thời lượng lưu trú của khách từ dữ liệu ngày nhận phòng và trả phòng, kiểm soát các trường hợp chuỗi ngày sai cú pháp hoặc không tồn tại trên lịch.
2. Xử lý giới hạn mốc chụp dữ liệu (snapshot cutoff), thiết lập chỉ mục thời gian đơn điệu tăng dần để tối ưu hóa các phép cắt lát theo chuỗi năm hoặc tháng.
3. Tổng hợp số liệu theo quý, nhận diện các kỳ chưa trọn vẹn (incomplete periods) để tránh rút ra các kết luận sai lệch về xu hướng tăng giảm.
4. Triệt tiêu biến động ngày trong tuần bằng kỹ thuật cửa sổ trượt 7 ngày, giải thích độ trễ của đỉnh trung bình trượt so với đỉnh số liệu thực tế.
5. Thực hiện phép so sánh cùng kỳ năm trước (Year-over-Year) và so sánh kỳ liền trước (Month-over-Month), đồng thời chuẩn hóa số liệu theo số ngày thực tế của từng tháng có tính đến năm nhuận.

---

## 2. Dữ liệu thực hành và chuẩn bị môi trường

Để bảo đảm toàn bộ mã nguồn có thể thực thi độc lập và kiểm chứng ngoại tuyến (offline), bài thực hành sử dụng ba tập dữ liệu mẫu:
1. Bảng đặt phòng nhỏ `DAT_DEMO` (4 dòng) với định dạng ngày `DD/MM/YYYY`, chứa cả ngày hợp lệ, ngày không tồn tại trên lịch và ô khuyết.
2. Bộ dữ liệu đánh giá giả lập `DEMO_REVIEWS` (11.425 dòng, giai đoạn 2019-01-01 đến 2026-07-01) được sinh theo quy luật chu kỳ tuần, mùa hè Nam bán cầu, giai đoạn giãn cách năm 2020 và ngày sự kiện kỷ lục.
3. Bảng phòng mẫu `LISTINGS_DEMO` (5 dòng) phục vụ tính toán khoảng cách từ lần đánh giá cuối cùng đến mốc chụp dữ liệu.

```python
import numpy as np
import pandas as pd
from IPython.display import display

# Thiết lập hành vi Copy-on-Write an toàn cho pandas
if pd.__version__.startswith("2."):
    pd.set_option("mode.copy_on_write", True)

# Địa chỉ snapshot dữ liệu thực tế tại Santiago de Chile phục vụ đối chiếu
SNAPSHOT_URL = (
    "https://data.insideairbnb.com/chile/rm/santiago/"
    "2026-06-29/visualisations/reviews.csv"
)

# Mốc chụp dữ liệu chuẩn hóa của tập dữ liệu
SNAPSHOT = "2026-06-29"

# 1. Bảng dữ liệu đặt phòng phục vụ kiểm tra cách đọc ngày và tính số đêm
DAT_DEMO = pd.DataFrame(
    {
        "vao": ["28/02/2026", "03/07/2026", "31/06/2026", None],
        "ra": ["03/03/2026", "06/07/2026", "05/07/2026", "12/07/2026"],
    },
    index=["D1", "D2", "D3", "D4"],
)


# 2. Bộ dữ liệu đánh giá giả lập theo quy luật cố định
def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")
_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]
DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})
DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])
DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

# 3. Bảng phòng mẫu phục vụ xác định chỗ ở ngừng hoạt động
LISTINGS_DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105],
        "name": [
            "Căn hộ trung tâm",
            "Phòng riêng Bellas Artes",
            "Loft Providencia",
            "Studio Recoleta",
            "Nhà cổ Brasil",
        ],
        "last_review": ["2026-05-15", "2025-01-10", "2026-07-02", "2024-11-20", None],
    }
)
```

> [!NOTE]
> **Đối chiếu thực tế**: Khi xử lý tệp snapshot đầy đủ của Santiago (690.112 dòng), có đúng 204 dòng đánh giá mang ngày sau mốc chụp 2026-06-29. Toàn bộ các ví dụ và bảng đối chiếu bên dưới được tính toán trực tiếp trên dữ liệu mẫu giả lập nhằm bảo đảm tính tái lập hoàn toàn, tuyệt đối không dùng số liệu giả lập để suy diễn về các sự kiện thực tế của thành phố Santiago.

---

## 3. Nội dung chi tiết bộ bài tập thực hành

<span id="data-lab-08-01"></span>
### Bài tập 1: Đọc chuỗi ngày tháng theo định dạng nguồn và tính số đêm lưu trú

::: exercise Tính số đêm lưu trú
Cho một DataFrame `dat` chứa thông tin các lượt đặt phòng với hai cột chuỗi `vao` (ngày nhận phòng) và `ra` (ngày trả phòng) theo định dạng ngày tháng châu Âu `DD/MM/YYYY`. Trong dữ liệu có thể xuất hiện ngày không tồn tại trên lịch (chẳng hạn ngày 31 tháng 6) hoặc giá trị khuyết (`None`).

Hãy viết hàm `calculate_stay_nights(dat: pd.DataFrame) -> pd.Series` thực hiện các thao tác:
1. Chuyển đổi hai cột `vao` và `ra` sang kiểu dữ liệu ngày giờ (`datetime64[ns]`), áp dụng định dạng `%d/%m/%Y` và cơ chế ép kiểu an toàn `errors="coerce"`.
2. Tính số đêm lưu trú của từng lượt đặt phòng bằng hiệu số giữa ngày trả phòng và ngày nhận phòng, trích xuất số ngày nguyên dưới dạng Series.
3. Nếu một trong hai ngày bị khuyết hoặc không thể chuyển đổi, số đêm lưu trú tương ứng phải nhận giá trị thiếu (`NaN`). Không làm thay đổi DataFrame `dat` đầu vào.
:::

::: solution
#### Cách 1: Chuyển đổi tuần tự từng cột bằng định dạng chuỗi tường minh

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

DAT_DEMO = pd.DataFrame(
    {
        "vao": ["28/02/2026", "03/07/2026", "31/06/2026", None],
        "ra": ["03/03/2026", "06/07/2026", "05/07/2026", "12/07/2026"],
    },
    index=["D1", "D2", "D3", "D4"],
)

# Bắt đầu lời giải

import pandas as pd


def calculate_stay_nights(dat: pd.DataFrame) -> pd.Series:
    # 1. Chuyển đổi cột ngày vào với định dạng DD/MM/YYYY, ép lỗi thành NaT
    vao_dt = pd.to_datetime(dat["vao"], format="%d/%m/%Y", errors="coerce")

    # 2. Chuyển đổi cột ngày ra với cùng định dạng
    ra_dt = pd.to_datetime(dat["ra"], format="%d/%m/%Y", errors="coerce")

    # 3. Trừ hai Series thời gian để nhận Timedelta rồi lấy số ngày nguyên
    so_dem = (ra_dt - vao_dt).dt.days
    return so_dem


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ket_qua_dem_c1 = calculate_stay_nights(DAT_DEMO)
display(ket_qua_dem_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

`to_datetime` đọc hai cột theo đúng `%d/%m/%Y`. `errors="coerce"` đổi chuỗi sai lịch hoặc ô thiếu thành `NaT`. Lấy ngày ra trừ ngày vào tạo `Timedelta`, rồi `.dt.days` lấy số ngày nguyên. Dòng có một ngày không hợp lệ nhận kết quả thiếu, không được biến thành 0 đêm.

#### Kết quả cách 1

| Chỉ mục | Giá trị |
| --- | --- |
| D1 | 3 |
| D2 | 3 |
| D3 | NaN |
| D4 | NaN |

#### Cách 2: Áp dụng cùng một quy tắc đọc cho cả hai cột

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

DAT_DEMO = pd.DataFrame(
    {
        "vao": ["28/02/2026", "03/07/2026", "31/06/2026", None],
        "ra": ["03/03/2026", "06/07/2026", "05/07/2026", "12/07/2026"],
    },
    index=["D1", "D2", "D3", "D4"],
)

# Bắt đầu lời giải

import pandas as pd


def calculate_stay_nights(dat: pd.DataFrame) -> pd.Series:
    # apply mặc định làm việc theo cột, dùng chung format và cách xử lý lỗi
    ngay = dat.loc[:, ["vao", "ra"]].apply(
        pd.to_datetime, format="%d/%m/%Y", errors="coerce"
    )
    so_dem = ngay["ra"].sub(ngay["vao"]).dt.days
    return so_dem


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ket_qua_dem_c2 = calculate_stay_nights(DAT_DEMO)
display(ket_qua_dem_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

`DataFrame.apply` mặc định chuyển từng cột vào hàm. Hai cột vì thế dùng cùng `format` và quy tắc lỗi trong một chỗ cấu hình. `.sub()` là phép trừ hai Series theo chỉ mục, sau đó `.dt.days` lấy số ngày. Cách này vẫn giữ định dạng bắt buộc, không thay bằng phỏng đoán `dayfirst`.

#### Kết quả cách 2

| Chỉ mục | Giá trị |
| --- | --- |
| D1 | 3 |
| D2 | 3 |
| D3 | NaN |
| D4 | NaN |
#### So sánh cách dùng

Cách 1 mở riêng bước chuyển đổi ngày vào và ngày ra, thuận tiện để quan sát cột nào chứa ngày sai. Cách 2 đặt cùng định dạng và quy tắc lỗi trong một lần cấu hình. Cả hai lời giải đều đang yêu cầu định dạng ngày/tháng/năm của đề.

:::

---

<span id="data-lab-08-02"></span>
### Bài tập 2: Phân biệt lỗi chuyển đổi ngày không hợp lệ với dữ liệu khuyết từ nguồn

::: exercise Phát hiện lỗi chuyển đổi ngày
Khi sử dụng `errors="coerce"`, cả ngày không tồn tại trên lịch (như ngày 31/06/2026) lẫn các ô vốn dĩ để trống trong nguồn (`None` hoặc `NaN`) đều trở thành `NaT`. Trong kiểm toán chất lượng dữ liệu, ta cần phân biệt hai tình huống này để lập danh sách các bản ghi nhập liệu sai.

Hãy viết hàm `detect_invalid_date_errors(dat: pd.DataFrame, vao_dt: pd.Series) -> pd.Series` nhận vào DataFrame gốc `dat` và Series `vao_dt` đã chuyển đổi. Hàm trả về một Series boolean đánh dấu `True` cho đúng các dòng có chuỗi ngày tồn tại trong nguồn nhưng không thể chuyển đổi thành ngày hợp lệ.
:::

::: solution
#### Cách 1: Kết hợp điều kiện logic bằng toán tử bitwise

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

DAT_DEMO = pd.DataFrame(
    {
        "vao": ["28/02/2026", "03/07/2026", "31/06/2026", None],
        "ra": ["03/03/2026", "06/07/2026", "05/07/2026", "12/07/2026"],
    },
    index=["D1", "D2", "D3", "D4"],
)

# Bắt đầu lời giải

import pandas as pd


def detect_invalid_date_errors(dat: pd.DataFrame, vao_dt: pd.Series) -> pd.Series:
    # Điều kiện: Cột chuyển đổi bị khuyết (NaT) VÀ Cột gốc có dữ liệu hợp lệ (notna)
    mat_na_loi = vao_dt.isna() & dat["vao"].notna()
    return mat_na_loi


# Gọi thực nghiệm hàm với dữ liệu mẫu:
vao_da_chuyen = pd.to_datetime(DAT_DEMO["vao"], format="%d/%m/%Y", errors="coerce")
ket_qua_loi_c1 = detect_invalid_date_errors(DAT_DEMO, vao_da_chuyen)
display(ket_qua_loi_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

`notna()` kiểm tra chuỗi ngày có tồn tại trong dữ liệu gốc. `isna()` kiểm tra kết quả chuyển đổi bị thiếu. Kết hợp hai mặt nạ bằng `&` chỉ giữ trường hợp có đầu vào nhưng không đọc được ngày. Ô vốn đã thiếu không bị gán thành lỗi nhập ngày.

#### Kết quả cách 1

| Chỉ mục | vao |
| --- | --- |
| D1 | False |
| D2 | False |
| D3 | True |
| D4 | False |

#### Cách 2: Sử dụng phép toán logic numpy logical_and tường minh

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

DAT_DEMO = pd.DataFrame(
    {
        "vao": ["28/02/2026", "03/07/2026", "31/06/2026", None],
        "ra": ["03/03/2026", "06/07/2026", "05/07/2026", "12/07/2026"],
    },
    index=["D1", "D2", "D3", "D4"],
)

# Bắt đầu lời giải

import numpy as np
import pandas as pd


def detect_invalid_date_errors(dat: pd.DataFrame, vao_dt: pd.Series) -> pd.Series:
    # Thực hiện phép toán logic AND bằng NumPy logical_and trên hai mảng boolean
    dieu_kien_nat = vao_dt.isna().to_numpy()
    dieu_kien_co_chuoi = dat["vao"].notna().to_numpy()
    ket_qua = np.logical_and(dieu_kien_nat, dieu_kien_co_chuoi)
    return pd.Series(ket_qua, index=dat.index, name=vao_dt.name)


# Gọi thực nghiệm hàm với dữ liệu mẫu:
vao_da_chuyen = pd.to_datetime(DAT_DEMO["vao"], format="%d/%m/%Y", errors="coerce")
ket_qua_loi_c2 = detect_invalid_date_errors(DAT_DEMO, vao_da_chuyen)
display(ket_qua_loi_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

Tách hai điều kiện thành những Series boolean có cùng chỉ mục giúp đọc rõ vai trò của mỗi vế. Phép kết hợp theo nhãn giữ kết quả ứng với đúng dòng ban đầu. Cần nhận Series ngày được tạo từ chính cột đang kiểm, tránh đưa một cột chuyển đổi có chỉ mục khác vào phép so sánh.

#### Kết quả cách 2

| Chỉ mục | vao |
| --- | --- |
| D1 | False |
| D2 | False |
| D3 | True |
| D4 | False |
#### So sánh cách dùng

Cú pháp dùng `&` ở Cách 1 đặt hai điều kiện pandas cạnh nhau và cần ngoặc cho từng phép so sánh. Cách 2 gọi `np.logical_and` để thể hiện phép kết hợp bằng tên hàm. Hai cách phải giữ cùng chỉ mục và cùng quy tắc xử lý ngày thiếu.

:::

---

<span id="data-lab-08-03"></span>
### Bài tập 3: Loại bỏ dòng sau mốc chụp dữ liệu và thiết lập chỉ mục thời gian

::: exercise Thiết lập chỉ mục thời gian và loại bỏ mốc tương lai
Trong các tệp dữ liệu nhật ký đánh giá, đôi khi xuất hiện các dòng có ngày ghi nhận sau thời điểm chụp dữ liệu (do lệch múi giờ của máy chủ hoặc ghi nhận trễ). Các dòng này cần được thống kê và loại bỏ trước khi thực hiện phân tích chuỗi thời gian.

Hãy viết hàm `prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict` nhận vào DataFrame `rv` chứa cột `date` (kiểu `datetime64`) và chuỗi mốc chụp `snapshot` dạng `"YYYY-MM-DD"`. Hàm trả về một từ điển gồm đúng hai khóa:
1. `so_dong_sau_moc`: Số nguyên (`int`) đếm số dòng có `date > snapshot`.
2. `r`: DataFrame chỉ gồm các dòng thỏa mãn `date <= snapshot`, đưa cột `date` làm chỉ mục (`set_index("date")`), sắp xếp chỉ mục tăng dần theo thời gian (`sort_index()`), giữ nguyên toàn bộ các cột còn lại và cột `date` không còn nằm trong danh sách cột dữ liệu. Không làm biến đổi DataFrame `rv` ban đầu.
:::

::: solution
#### Cách 1: Sử dụng mặt nạ boolean và phương thức đặt chỉ mục chuẩn mực

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"

# Bắt đầu lời giải

import pandas as pd


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
display(f"Số dòng sau mốc: {ket_qua_idx_c1['so_dong_sau_moc']}")
display(ket_qua_idx_c1["r"].head(3))

# Kết thúc lời giải
```

#### Giải thích cách 1

Đọc và kiểm ngày trước khi so sánh với mốc snapshot. Giữ các hàng không sau mốc, rồi `set_index` đưa ngày vào chỉ mục và `sort_index` sắp theo thời gian. Trả cả số dòng bị gắn cờ để người đọc biết phạm vi thay đổi. Việc lọc không chứng minh các dòng sau mốc chắc chắn là dữ liệu giả.

#### Kết quả cách 1

| date | listing_id |
| --- | --- |
| 2019-01-01 00:00:00 | 100 |
| 2019-01-01 00:00:00 | 101 |
| 2019-01-01 00:00:00 | 102 |

#### Cách 2: Sử dụng query với biến cục bộ và method chaining

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"

# Bắt đầu lời giải

import pandas as pd


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # Đếm số lượng dòng vượt mốc chụp dữ liệu
    so_dong_sau = int((rv["date"] > moc_tg).sum())

    # Truy vấn và thiết lập DatetimeIndex bằng chuỗi phương thức
    r = rv.query("date <= @moc_tg").set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ket_qua_idx_c2 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
display(f"Số dòng sau mốc: {ket_qua_idx_c2['so_dong_sau_moc']}")
display(ket_qua_idx_c2["r"].head(3))

# Kết thúc lời giải
```

#### Giải thích cách 2

Tách phần chuẩn bị ngày khỏi mặt nạ lọc giúp theo dõi từng bước trong chuỗi phương thức. `.loc` chọn các dòng thỏa điều kiện, còn `.copy()` làm rõ rằng bảng kết quả sẽ được xử lý riêng. Chỉ mục thời gian đã sắp là tiền đề để các bài sau cắt lát theo năm và tổng hợp theo lịch.

#### Kết quả cách 2

| date | listing_id |
| --- | --- |
| 2019-01-01 00:00:00 | 100 |
| 2019-01-01 00:00:00 | 101 |
| 2019-01-01 00:00:00 | 102 |
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi cần đếm chính xác số dòng bị loại và kiểm soát từng bước gán chỉ mục thời gian. Cách 2 thích hợp khi muốn tổ chức các bước lọc và sắp xếp thành chuỗi phương thức liền mạch, đồng thời tách riêng bản sao mới.

:::

---

<span id="data-lab-08-04"></span>
### Bài tập 4: Cắt lát chuỗi thời gian bằng nhãn chuỗi và đối chiếu số lượng đánh giá

::: exercise Cắt lát theo nhãn năm
Khi DataFrame đã có chỉ mục là `DatetimeIndex` được sắp xếp, pandas hỗ trợ tính năng cắt lát bằng chuỗi thời gian tự nhiên (partial string indexing). Ta có thể truyền trực tiếp chuỗi năm `"2019"` vào `.loc[]` để trích xuất toàn bộ dữ liệu của năm đó.

Hãy viết hàm `count_year(r: pd.DataFrame, nam: int) -> int` nhận vào bảng `r` có chỉ mục thời gian đã sắp xếp và một số nguyên `nam`. Hàm thực hiện cắt lát chuỗi `r.loc[str(nam)]` và trả về tổng số dòng thuộc về năm đó dưới dạng số nguyên (`int`).
:::

::: solution
#### Cách 1: Cắt lát nhãn chuỗi với len trực tiếp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def count_year(r: pd.DataFrame, nam: int) -> int:
    # Truy xuất toàn bộ các dòng thuộc năm chỉ định bằng nhãn chuỗi
    bang_nam = r.loc[str(nam)]
    return int(len(bang_nam))


# Gọi thực nghiệm hàm với dữ liệu mẫu:
so_rv_2019_c1 = count_year(ket_qua_idx_c1["r"], 2019)
so_rv_2021_c1 = count_year(ket_qua_idx_c1["r"], 2021)
display(f"Năm 2019: {so_rv_2019_c1} dòng, Năm 2021: {so_rv_2021_c1} dòng")

# Kết thúc lời giải
```

#### Giải thích cách 1

Với `DatetimeIndex`, `.loc[str(nam)]` chọn các nhãn thuộc năm đó, không phải chọn một vị trí dòng. `len` đếm số đánh giá trong lát cắt. Cần xử lý năm không có trong dữ liệu theo đúng đầu ra của đề, thay vì giả định năm nào cũng xuất hiện.

#### Kết quả cách 1

| Kết quả |
| --- |
| Năm 2019: 1317 dòng, Năm 2021: 952 dòng |

#### Cách 2: Trích xuất kích thước qua shape và kiểm chứng dải ngày

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def count_year(r: pd.DataFrame, nam: int) -> int:
    # Cắt lát tường minh theo nhãn chuỗi và lấy số dòng qua thuộc tính shape
    so_luong = r.loc[str(nam)].shape[0]
    return int(so_luong)


# Gọi thực nghiệm hàm với dữ liệu mẫu:
so_rv_2019_c2 = count_year(ket_qua_idx_c2["r"], 2019)
so_rv_2021_c2 = count_year(ket_qua_idx_c2["r"], 2021)
display(f"Năm 2019: {so_rv_2019_c2} dòng, Năm 2021: {so_rv_2021_c2} dòng")

# Kết thúc lời giải
```

#### Giải thích cách 2

So sánh thuộc tính `.index.year` với năm cần tìm tạo mặt nạ cùng độ dài bảng. Tổng các giá trị True hoặc số dòng sau lọc cho cùng số đánh giá. Cách viết này thể hiện trực tiếp điều kiện năm và thuận tiện khi muốn kết hợp thêm điều kiện theo tháng hoặc loại chỗ ở.

#### Kết quả cách 2

| Kết quả |
| --- |
| Năm 2019: 1317 dòng, Năm 2021: 952 dòng |
#### So sánh cách dùng

Hãy chọn Cách 1 khi chỉ mục đã là dạng thời gian và bạn chỉ cần cắt nhanh các bản ghi của một năm bằng nhãn chuỗi. Cách 2 thuận tiện hơn khi muốn kết hợp điều kiện năm với nhiều tiêu chí lọc khác trên cùng mặt nạ boolean.

:::

---

<span id="data-lab-08-05"></span>
### Bài tập 5: Tổng hợp dữ liệu theo quý và nhận diện kỳ chưa trọn

::: exercise Tổng hợp theo quý và loại bỏ kỳ chưa trọn
Trong pandas 3, bí danh `resample("QE")` (Quarter End) được sử dụng để tổng hợp dữ liệu theo quý và gán nhãn bằng ngày cuối cùng của quý (ngày 31/03, 30/06, 30/09, 31/12). Nếu thời điểm thu thập dữ liệu đứng trước ngày kết thúc quý, số lượng của quý đó sẽ bị thiếu hụt so với thực tế và được gọi là **kỳ chưa trọn** (incomplete period).

Hãy viết hàm `quarterly(r: pd.DataFrame, snapshot: str) -> dict` nhận vào bảng `r` và mốc chụp `snapshot`. Hàm trả về một từ điển gồm:
1. `quy`: Series kết quả của `r.resample("QE").size()`, chứa số lượng bản ghi của từng quý.
2. `quy_day_du`: Series trích xuất từ `quy` chỉ giữ lại các quý có nhãn ngày cuối quý nhỏ hơn hoặc bằng `snapshot`, tức loại bỏ quý chưa trọn cuối cùng nếu mốc chụp chưa chạm đến ngày cuối quý.
:::

::: solution
#### Cách 1: Sử dụng resample QE và lọc theo chỉ mục thời gian

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def quarterly(r: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tổng hợp số lượng đánh giá theo từng quý kết thúc bằng QE
    quy = r.resample("QE").size()

    # 2. Lọc bỏ quý chưa kết thúc bằng cách so sánh nhãn chỉ mục với mốc chụp
    quy_day_du = quy[quy.index <= moc_tg]

    return {
        "quy": quy,
        "quy_day_du": quy_day_du,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ket_qua_quy_c1 = quarterly(ket_qua_idx_c1["r"], SNAPSHOT)
display(ket_qua_quy_c1["quy"].tail(4))
display(f"Số quý đầy đủ: {len(ket_qua_quy_c1['quy_day_du'])}")

# Kết thúc lời giải
```

#### Giải thích cách 1

`resample` chia chỉ mục ngày thành các quý dương lịch, `.size()` đếm dòng trong từng quý. Quý chưa kết thúc tại mốc quan sát phải được nhận diện bằng ngày cuối kỳ. Đề có bước bỏ kỳ cuối trong dữ liệu đã cho, nhưng không được suy ra rằng kỳ cuối của mọi tập dữ liệu đều thiếu.

#### Kết quả cách 1

| date | Giá trị |
| --- | --- |
| 2025-09-30 00:00:00 | 486 |
| 2025-12-31 00:00:00 | 528 |
| 2026-03-31 00:00:00 | 904 |
| 2026-06-30 00:00:00 | 746 |

#### Cách 2: Sử dụng truncate để cắt lát chuỗi thời gian tường minh

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def quarterly(r: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    quy = r.resample("QE").size()
    # truncate cho phép cắt lát chuỗi thời gian có chỉ mục sắp xếp một cách an toàn
    quy_day_du = quy.truncate(after=moc_tg)

    return {
        "quy": quy,
        "quy_day_du": quy_day_du,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ket_qua_quy_c2 = quarterly(ket_qua_idx_c2["r"], SNAPSHOT)
display(ket_qua_quy_c2["quy"].tail(4))
display(f"Số quý đầy đủ: {len(ket_qua_quy_c2['quy_day_du'])}")

# Kết thúc lời giải
```

#### Giải thích cách 2

Chuẩn hóa nhãn kỳ giúp so sánh mốc kết thúc quý với snapshot một cách tường minh. Sau khi tổng hợp, chỉ chọn những kỳ đáp ứng điều kiện đầy đủ. Cần giữ phân biệt giữa nhãn ngày cuối quý và ngày đánh giá cuối cùng xuất hiện trong quý, vì ngày cuối có sự kiện không xác định độ phủ dữ liệu.

#### Kết quả cách 2

| date | Giá trị |
| --- | --- |
| 2025-09-30 00:00:00 | 486 |
| 2025-12-31 00:00:00 | 528 |
| 2026-03-31 00:00:00 | 904 |
| 2026-06-30 00:00:00 | 746 |
#### So sánh cách dùng

Cách 1 giúp quan sát nhãn cuối quý và bước bỏ kỳ cuối trong bộ dữ liệu đã cho. Cách 2 đối chiếu kết thúc kỳ với snapshot để chọn các quý đã trọn vẹn. Khi thay dữ liệu, hãy kiểm độ phủ thời gian trước khi quyết định bỏ một quý.

:::

---

<span id="data-lab-08-06"></span>
### Bài tập 6: Kiểm tra quy tắc lọc kỳ chưa trọn tại các mốc thời gian biên

::: exercise Kiểm định mốc thời gian biên của kỳ
Việc loại bỏ quý cuối cùng là do quý đó chưa trọn vẹn, không phải một quy tắc cứng nhắc bắt buộc phải bỏ quý cuối cùng trong mọi tập dữ liệu. Nếu mốc thu thập dữ liệu rơi đúng vào ngày kết thúc quý, quý đó hoàn toàn trọn vẹn và phải được giữ lại.

Cho một Series `dem_quy` gồm hai quý:
```python
dem_quy = pd.Series([100, 120], index=pd.to_datetime(["2026-03-31", "2026-06-30"]))
```
Hãy viết hàm `filter_complete_quarters(dem_quy: pd.Series, moc: str) -> pd.Series` nhận vào Series và chuỗi ngày `moc`. Hàm trả về Series chỉ giữ các quý đã kết thúc tại hoặc trước `moc`.
- Khi `moc = "2026-06-29"`: Trả về Series có đúng 1 quý (chỉ giữ Q1/2026).
- Khi `moc = "2026-06-30"`: Trả về Series có đủ 2 quý (giữ cả Q1/2026 và Q2/2026).
:::

::: solution
#### Cách 1: Sử dụng phép so sánh boolean trực tiếp với Timestamp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

# Bắt đầu lời giải

import pandas as pd


def filter_complete_quarters(dem_quy: pd.Series, moc: str) -> pd.Series:
    moc_tg = pd.Timestamp(moc)
    # Lọc các quý có ngày kết thúc nhỏ hơn hoặc bằng mốc chụp
    quy_hop_le = dem_quy[dem_quy.index <= moc_tg]
    return quy_hop_le


# Gọi thực nghiệm hàm với dữ liệu mẫu:
dem_quy_mau = pd.Series([100, 120], index=pd.to_datetime(["2026-03-31", "2026-06-30"]))
kq_bien_29_c1 = filter_complete_quarters(dem_quy_mau, "2026-06-29")
kq_bien_30_c1 = filter_complete_quarters(dem_quy_mau, "2026-06-30")
display(
    f"Mốc 29/06: Còn {len(kq_bien_29_c1)} quý, Mốc 30/06: Còn {len(kq_bien_30_c1)} quý"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

So sánh nhãn ngày kết thúc quý với mốc được phép báo cáo. Mặt nạ lọc trả lại đúng các quý đã kết thúc, giữ nhãn và số đếm. Khi mốc nằm đúng ngày cuối quý, phải đọc rõ quy ước về hết ngày đó, không tự loại thêm một quý.

#### Kết quả cách 1

| Kết quả |
| --- |
| Mốc 29/06: Còn 1 quý, Mốc 30/06: Còn 2 quý |

#### Cách 2: Sử dụng phương thức cắt lát nhãn với slice thời gian

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

# Bắt đầu lời giải

import pandas as pd


def filter_complete_quarters(dem_quy: pd.Series, moc: str) -> pd.Series:
    # Lấy toàn bộ các phần tử từ đầu đến mốc thời gian bằng cú pháp cắt lát
    quy_hop_le = dem_quy.loc[: pd.Timestamp(moc)]
    return quy_hop_le


# Gọi thực nghiệm hàm với dữ liệu mẫu:
dem_quy_mau = pd.Series([100, 120], index=pd.to_datetime(["2026-03-31", "2026-06-30"]))
kq_bien_29_c2 = filter_complete_quarters(dem_quy_mau, "2026-06-29")
kq_bien_30_c2 = filter_complete_quarters(dem_quy_mau, "2026-06-30")
display(
    f"Mốc 29/06: Còn {len(kq_bien_29_c2)} quý, Mốc 30/06: Còn {len(kq_bien_30_c2)} quý"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Đưa mốc về `Timestamp` rồi dùng phép chọn theo chỉ mục giúp điều kiện thời gian không phụ thuộc vị trí cuối của Series. Cách này vẫn đúng khi dữ liệu có nhiều kỳ sau mốc. Hai cách đều cần cùng quy ước gồm hay không gồm ngày biên để kết quả đối chiếu có ý nghĩa.

#### Kết quả cách 2

| Kết quả |
| --- |
| Mốc 29/06: Còn 1 quý, Mốc 30/06: Còn 2 quý |
#### So sánh cách dùng

Hãy chọn Cách 1 khi dữ liệu chưa chắc chắn được sắp xếp tuần tự hoặc cần kết hợp thêm điều kiện lọc phụ. Cách 2 là lựa chọn trực diện khi chỉ mục ngày đã sắp thứ tự và bạn muốn lấy ngay đoạn lịch sử hợp lệ bằng phép cắt lát.

:::

---

<span id="data-lab-08-07"></span>
### Bài tập 7: Xác định quý cao nhất toàn chuỗi và quý thấp nhất trong một giai đoạn

::: exercise Tìm kiếm cực trị theo quý
Trong phân tích xu hướng kinh doanh, chuyên viên dữ liệu cần xác định thời điểm thị trường đạt đỉnh cao nhất trong lịch sử và thời điểm chạm đáy trong giai đoạn khủng hoảng.

Hãy viết hàm `quarter_extremes(quy: pd.Series, bat_dau: str, ket_thuc: str) -> dict` nhận vào Series các quý trọn vẹn `quy` và hai chuỗi mốc năm `bat_dau`, `ket_thuc`. Hàm trả về một từ điển gồm đúng ba khóa:
1. `quy_dinh`: Đối tượng `pd.Timestamp` là nhãn của quý có số lượng đánh giá cao nhất trên toàn bộ chuỗi (`idxmax()`).
2. `quy_day`: Đối tượng `pd.Timestamp` là nhãn của quý có số lượng đánh giá thấp nhất trong giai đoạn cắt lát từ `bat_dau` đến `ket_thuc` (`idxmin()`).
3. `gia_tri_day`: Số nguyên (`int`) là số lượng đánh giá của quý chạm đáy đó.
:::

::: solution
#### Cách 1: Sử dụng idxmax toàn chuỗi và cắt lát tìm idxmin giai đoạn

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1


def quarterly(r: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tổng hợp số lượng đánh giá theo từng quý kết thúc bằng QE
    quy = r.resample("QE").size()

    # 2. Lọc bỏ quý chưa kết thúc bằng cách so sánh nhãn chỉ mục với mốc chụp
    quy_day_du = quy[quy.index <= moc_tg]

    return {
        "quy": quy,
        "quy_day_du": quy_day_du,
    }


ket_qua_quy_c1 = quarterly(ket_qua_idx_c1["r"], SNAPSHOT)
ket_qua_quy_c2 = ket_qua_quy_c1
quy_day_du_demo = ket_qua_quy_c1["quy_day_du"]

# Bắt đầu lời giải

import pandas as pd


def quarter_extremes(quy: pd.Series, bat_dau: str, ket_thuc: str) -> dict:
    # 1. Tìm nhãn thời gian của quý cao nhất toàn bộ chuỗi dữ liệu
    quy_dinh = quy.idxmax()

    # 2. Cắt lát chuỗi dữ liệu trong giai đoạn khảo sát chỉ định
    giai_doan = quy.loc[bat_dau:ket_thuc]

    # 3. Tìm nhãn và giá trị của quý chạm đáy trong giai đoạn đó
    quy_day = giai_doan.idxmin()
    gia_tri_day = int(giai_doan.loc[quy_day])

    return {
        "quy_dinh": quy_dinh,
        "quy_day": quy_day,
        "gia_tri_day": gia_tri_day,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
quy_day_du_demo = ket_qua_quy_c1["quy_day_du"]
cuc_tri_c1 = quarter_extremes(quy_day_du_demo, "2019", "2021")
display(cuc_tri_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Cắt giai đoạn cần so sánh trước khi tìm cực trị. `idxmax` và `idxmin` trả nhãn quý, còn `max` và `min` trả số đếm. Khi có nhiều quý cùng giá trị, các hàm tìm nhãn trả lần xuất hiện đầu, nên cần nêu quy tắc này trong báo cáo.

#### Kết quả cách 1

| Trường | Kết quả |
| --- | --- |
| quy_dinh | 2026-03-31 00:00:00 |
| quy_day | 2020-06-30 00:00:00 |
| gia_tri_day | 26 |

#### Cách 2: Sử dụng tổng hợp agg và tối ưu hóa truy xuất

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1


def quarterly(r: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tổng hợp số lượng đánh giá theo từng quý kết thúc bằng QE
    quy = r.resample("QE").size()

    # 2. Lọc bỏ quý chưa kết thúc bằng cách so sánh nhãn chỉ mục với mốc chụp
    quy_day_du = quy[quy.index <= moc_tg]

    return {
        "quy": quy,
        "quy_day_du": quy_day_du,
    }


ket_qua_quy_c1 = quarterly(ket_qua_idx_c1["r"], SNAPSHOT)
ket_qua_quy_c2 = ket_qua_quy_c1
quy_day_du_demo = ket_qua_quy_c1["quy_day_du"]

# Bắt đầu lời giải

import pandas as pd


def quarter_extremes(quy: pd.Series, bat_dau: str, ket_thuc: str) -> dict:
    quy_dinh = quy.idxmax()

    # Lấy phân đoạn cần khảo sát bằng lát cắt chuỗi
    phan_doan = quy.loc[bat_dau:ket_thuc]
    quy_day = phan_doan.idxmin()
    gia_tri_day = int(phan_doan.min())

    return {
        "quy_dinh": quy_dinh,
        "quy_day": quy_day,
        "gia_tri_day": gia_tri_day,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
cuc_tri_c2 = quarter_extremes(quy_day_du_demo, "2019", "2021")
display(cuc_tri_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

Việc gom nhãn và giá trị vào một dict giữ kết quả có tên trường rõ ràng. Đừng tìm cực trị trên toàn lịch sử rồi mới kiểm xem nhãn có thuộc giai đoạn được hỏi hay không. Dữ liệu rỗng sau khi giới hạn kỳ cần được nhận diện trước khi gọi hàm tìm cực trị.

#### Kết quả cách 2

| Trường | Kết quả |
| --- | --- |
| quy_dinh | 2026-03-31 00:00:00 |
| quy_day | 2020-06-30 00:00:00 |
| gia_tri_day | 26 |
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi cần tra cứu nhanh nhãn thời gian và giá trị cực trị qua từng lệnh đơn lẻ lúc khám phá. Cách 2 phù hợp hơn khi bạn muốn gom toàn bộ chỉ số vào một từ điển có cấu trúc rõ ràng để tiện xuất báo cáo.

:::

---

<span id="data-lab-08-08"></span>
### Bài tập 8: Tổng hợp dữ liệu theo ngày và điền đầy đủ các ngày không có lượt đánh giá

::: exercise Tổng hợp theo lịch ngày liên tục
Khác với phương thức `groupby` thông thường (chỉ giữ lại các ngày thực sự xuất hiện bản ghi dữ liệu), phương thức `resample("D").size()` tạo ra một lưới ngày lịch liên tục từ ngày đầu tiên đến ngày cuối cùng và tự động gán giá trị 0 cho những ngày không có lượt đánh giá nào.

Hãy viết hàm `daily_counts(r: pd.DataFrame, nam: int) -> pd.Series` nhận vào bảng `r` và một năm `nam`. Hàm thực hiện cắt lát năm trước rồi mới tổng hợp bằng `resample("D").size()` để tránh lãng phí bộ nhớ khi tạo các ngày ngoài phạm vi quan tâm. Kết quả trả về là Series số lượt đánh giá mỗi ngày trong năm đó.
:::

::: solution
#### Cách 1: Cắt lát năm trước rồi tổng hợp bằng resample ngày

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def daily_counts(r: pd.DataFrame, nam: int) -> pd.Series:
    # 1. Cắt lát năm trước để giới hạn phạm vi tính toán
    r_nam = r.loc[str(nam)]

    # 2. Tổng hợp theo ngày và tự động điền 0 cho ngày trống
    ngay_series = r_nam.resample("D").size()
    return ngay_series


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ngay_2025_c1 = daily_counts(ket_qua_idx_c1["r"], 2025)
display(
    f"Năm 2025 có {len(ngay_2025_c1)} ngày, cao nhất: {ngay_2025_c1.max()} đánh giá/ngày"
)
display(ngay_2025_c1.tail(3))

# Kết thúc lời giải
```

#### Giải thích cách 1

Tạo lịch ngày đầy đủ bằng `date_range`, đếm số đánh giá rồi `reindex` về lịch đó. `fill_value=0` ở đây có nghĩa là không có sự kiện trong log đã được quan sát, không phải cách điền tùy ý cho một phép đo bị thiếu. Ngày nhuận được lịch của pandas tính theo năm được chọn.

#### Kết quả cách 1

| date | Giá trị |
| --- | --- |
| 2025-12-29 00:00:00 | 7 |
| 2025-12-30 00:00:00 | 5 |
| 2025-12-31 00:00:00 | 5 |

#### Cách 2: Kết hợp resample tường minh và chuẩn hóa tần suất chỉ mục

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def daily_counts(r: pd.DataFrame, nam: int) -> pd.Series:
    # Cắt lát dải ngày trọn vẹn của năm rồi áp dụng resample
    ngay_dau = f"{nam}-01-01"
    ngay_cuoi = f"{nam}-12-31"
    r_nam = r.loc[ngay_dau:ngay_cuoi]

    chuoi_ngay = r_nam.resample("1D").size()
    return chuoi_ngay


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ngay_2025_c2 = daily_counts(ket_qua_idx_c2["r"], 2025)
display(
    f"Năm 2025 có {len(ngay_2025_c2)} ngày, cao nhất: {ngay_2025_c2.max()} đánh giá/ngày"
)
display(ngay_2025_c2.tail(3))

# Kết thúc lời giải
```

#### Giải thích cách 2

Tổng hợp theo ngày rồi căn về cùng lịch cho phép so sánh các năm theo cùng định nghĩa. Giữ chỉ mục ngày liên tục là điều kiện để cửa sổ bảy dòng ở bài sau tương ứng với bảy ngày. Không dùng số ngày có sự kiện làm mẫu số khi câu hỏi hỏi trung bình trên mọi ngày trong năm.

#### Kết quả cách 2

| date | Giá trị |
| --- | --- |
| 2025-12-29 00:00:00 | 7 |
| 2025-12-30 00:00:00 | 5 |
| 2025-12-31 00:00:00 | 5 |
#### So sánh cách dùng

Hãy chọn Cách 1 khi bạn muốn tạo sẵn khung lịch dương đầy đủ để kiểm soát việc điền số 0 cho những ngày không có sự kiện. Cách 2 thuận tiện khi chuỗi thời gian cần được chuẩn hóa tần suất trực tiếp trong bước tổng hợp mà không cần tạo lịch rời.

:::

---

<span id="data-lab-08-09"></span>
### Bài tập 9: Làm mượt chuỗi thời gian bằng cửa sổ trượt 7 ngày và nhận diện đỉnh điểm

::: exercise Làm mượt bằng cửa sổ trượt
Số đánh giá theo ngày có thể dao động. Cửa sổ trượt giúp nhìn mức trung bình trong một khoảng, nhưng không thay thế chuỗi đếm gốc khi cần tìm một ngày cụ thể.

Hãy viết hàm `rolling_peak(ngay: pd.Series, cua_so: int = 7) -> dict` nhận vào Series số đếm theo ngày liên tục và độ rộng cửa sổ. Hàm trả về từ điển gồm:
1. `tb`: Series trung bình trượt đối xứng tính bằng `ngay.rolling(cua_so, center=True).mean()`.
2. `ngay_dinh`: Đối tượng `pd.Timestamp` là ngày có giá trị trung bình trượt lớn nhất (`idxmax()`).
3. `gia_tri_dinh`: Giá trị số thực (`float`) của trung bình trượt tại ngày đỉnh đó.

Yêu cầu phân tích và trực quan hóa:
- Phân biệt rõ sự khác nhau giữa cửa sổ 7 hàng (`7 rows`) và cửa sổ 7 ngày (`7 days`).
- Giải thích tham số `min_periods` và nguyên nhân vì sao các giá trị ở đầu chuỗi nhận giá trị `NaN`.
- Giải thích hiện tượng đỉnh của đường trung bình trượt quá khứ (`center=False`) nằm lệch về phía sau đỉnh thực tế của từng ngày.
- Xuất biểu đồ trực quan hóa chuỗi thời gian lưu trữ tại `img/labs/lab-08/rolling-7d-2025.svg`.
:::

::: solution
#### Cách 1: Sử dụng cửa sổ trượt căn giữa đối xứng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1


def daily_counts(r: pd.DataFrame, nam: int) -> pd.Series:
    # 1. Cắt lát năm trước để giới hạn phạm vi tính toán
    r_nam = r.loc[str(nam)]

    # 2. Tổng hợp theo ngày và tự động điền 0 cho ngày trống
    ngay_series = r_nam.resample("D").size()
    return ngay_series


ngay_2025_c1 = daily_counts(ket_qua_idx_c1["r"], 2025)

# Bắt đầu lời giải

import pandas as pd


def rolling_peak(ngay: pd.Series, cua_so: int = 7) -> dict:
    # 1. Tính trung bình trượt căn giữa để làm mượt biến động
    tb = ngay.rolling(cua_so, center=True).mean()

    # 2. Tìm ngày đạt giá trị trung bình trượt cao nhất và giá trị tương ứng
    ngay_dinh = tb.idxmax()
    gia_tri_dinh = float(tb.loc[ngay_dinh])

    return {
        "tb": tb,
        "ngay_dinh": ngay_dinh,
        "gia_tri_dinh": gia_tri_dinh,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_rolling_c1 = rolling_peak(ngay_2025_c1, cua_so=7)
display(
    f"Đỉnh căn giữa: {kq_rolling_c1['ngay_dinh']:%Y-%m-%d} với giá trị {kq_rolling_c1['gia_tri_dinh']:.2f}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

`rolling(cua_so)` dùng số dòng, còn `mean()` tính trung bình trong mỗi cửa sổ. Trên lịch ngày liên tục ở bài trước, bảy dòng tương ứng bảy ngày. `min_periods` quy định số quan sát tối thiểu. Với `center=True`, nhãn được đặt giữa cửa sổ, nên phép tính có dùng những ngày phía sau nhãn và có thể thiếu ở cả hai đầu. Cách làm mượt này phù hợp mô tả lịch sử, không dùng như một dự báo chỉ biết quá khứ.

#### Kết quả cách 1

| Kết quả |
| --- |
| Đỉnh căn giữa: 2025-11-23 với giá trị 11.29 |

![Số đánh giá theo ngày năm 2025 và đường trung bình trượt 7 ngày](img/labs/lab-08/rolling-7d-2025.svg)

#### Cách 2: Sử dụng cửa sổ trượt quá khứ với tham số min_periods tường minh

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1


def daily_counts(r: pd.DataFrame, nam: int) -> pd.Series:
    # 1. Cắt lát năm trước để giới hạn phạm vi tính toán
    r_nam = r.loc[str(nam)]

    # 2. Tổng hợp theo ngày và tự động điền 0 cho ngày trống
    ngay_series = r_nam.resample("D").size()
    return ngay_series


ngay_2025_c1 = daily_counts(ket_qua_idx_c1["r"], 2025)

# Bắt đầu lời giải

import pandas as pd


def rolling_peak(ngay: pd.Series, cua_so: int = 7) -> dict:
    # Cửa sổ quá khứ yêu cầu đủ đúng cua_so ngày quan sát để tính toán
    tb = ngay.rolling(window=cua_so, min_periods=cua_so, center=False).mean()

    ngay_dinh = tb.idxmax()
    gia_tri_dinh = float(tb.loc[ngay_dinh])

    return {
        "tb": tb,
        "ngay_dinh": ngay_dinh,
        "gia_tri_dinh": gia_tri_dinh,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_rolling_c2 = rolling_peak(ngay_2025_c1, cua_so=7)
display(
    f"Đỉnh quá khứ: {kq_rolling_c2['ngay_dinh']:%Y-%m-%d} với giá trị {kq_rolling_c2['gia_tri_dinh']:.2f}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Tách chuỗi làm mượt và thao tác tìm đỉnh giúp đối chiếu cả nhãn ngày lẫn giá trị. Nếu chỉ mục có khoảng trống, cần lập lại lịch hoặc cân nhắc cửa sổ thời gian như `"7D"` với quy tắc biên rõ ràng. Đừng thay một cửa sổ bảy dòng bằng bảy ngày mà không kiểm cấu trúc chỉ mục.

#### Kết quả cách 2

| Kết quả |
| --- |
| Đỉnh quá khứ: 2025-11-26 với giá trị 11.29 |

![Số đánh giá theo ngày năm 2025 và đường trung bình trượt 7 ngày](img/labs/lab-08/rolling-7d-2025.svg)
#### So sánh cách dùng

Cửa sổ đặt ở giữa trong Cách 1 thích hợp để mô tả lại lịch sử, vì mỗi điểm dùng cả những ngày phía sau. Chọn cửa sổ kết thúc tại ngày đang xét của Cách 2 khi chỉ được dùng dữ liệu đã có tại thời điểm tính.

:::

---

<span id="data-lab-08-10"></span>
### Bài tập 10: So sánh cùng kỳ theo quý và khắc phục lỗi lệch chu kỳ

::: exercise So sánh cùng kỳ theo quý
Trong chuỗi quý liên tục, cùng kỳ năm trước nằm cách bốn quý. Vì vậy, cần dịch bốn kỳ bằng `shift(4)`, còn `shift(12)` sẽ lùi ba năm.

Hãy viết hàm `quarterly_yoy(quy_day_du: pd.Series) -> pd.Series` nhận vào Series các quý đầy đủ và tính tỷ lệ thay đổi cùng kỳ năm trước theo công thức:
$$
g_t = \frac{q_t}{q_{t-4}} - 1.
$$
Ở đây, $q_t$ là số đánh giá của quý đang xét, còn $q_{t-4}$ là số đánh giá của cùng quý năm trước. Hãy đối chiếu quý 1 năm 2025 bằng cách lọc bảng `rv` từ `2025-01-01` đến trước `2025-04-01`.
:::

::: solution
#### Cách 1: Sử dụng shift với bước nhảy 4 quý

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1


def quarterly(r: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tổng hợp số lượng đánh giá theo từng quý kết thúc bằng QE
    quy = r.resample("QE").size()

    # 2. Lọc bỏ quý chưa kết thúc bằng cách so sánh nhãn chỉ mục với mốc chụp
    quy_day_du = quy[quy.index <= moc_tg]

    return {
        "quy": quy,
        "quy_day_du": quy_day_du,
    }


ket_qua_quy_c1 = quarterly(ket_qua_idx_c1["r"], SNAPSHOT)
ket_qua_quy_c2 = ket_qua_quy_c1
quy_day_du_demo = ket_qua_quy_c1["quy_day_du"]

# Bắt đầu lời giải

import pandas as pd


def quarterly_yoy(quy_day_du: pd.Series) -> pd.Series:
    # Với dữ liệu theo quý, dịch chuyển 4 hàng tương ứng với đúng 1 năm trước
    cung_ky = quy_day_du / quy_day_du.shift(4) - 1.0
    return cung_ky


# Gọi thực nghiệm hàm với dữ liệu mẫu:
yoy_quy_c1 = quarterly_yoy(ket_qua_quy_c1["quy_day_du"])
display(yoy_quy_c1.tail(4))

# Đối chiếu độc lập với số liệu lọc trực tiếp trong bảng rv:
mask_q1_2025 = (DEMO_REVIEWS["date"] >= "2025-01-01") & (
    DEMO_REVIEWS["date"] < "2025-04-01"
)
so_dem_truc_tiep = int(mask_q1_2025.sum())
display(
    f"Đếm trực tiếp Q1/2025: {so_dem_truc_tiep}, Series quý: {ket_qua_quy_c1['quy_day_du'].loc['2025-03-31']}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Cùng kỳ theo quý nghĩa là so với quý cách bốn kỳ, không phải quý ngay trước. `pct_change(4)` trả mức thay đổi trên thang 0–1, cần nhân 100 khi trình bày phần trăm. Bốn kỳ đầu chưa có kỳ đối chiếu, nên kết quả thiếu là hợp lý.

#### Kết quả cách 1

| date | Giá trị |
| --- | --- |
| 2025-06-30 00:00:00 | 0.233333 |
| 2025-09-30 00:00:00 | 0.227273 |
| 2025-12-31 00:00:00 | 0.340102 |
| 2026-03-31 00:00:00 | 0.521886 |

#### Cách 2: Sử dụng phương thức pct_change chuyên dụng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1


def quarterly(r: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tổng hợp số lượng đánh giá theo từng quý kết thúc bằng QE
    quy = r.resample("QE").size()

    # 2. Lọc bỏ quý chưa kết thúc bằng cách so sánh nhãn chỉ mục với mốc chụp
    quy_day_du = quy[quy.index <= moc_tg]

    return {
        "quy": quy,
        "quy_day_du": quy_day_du,
    }


ket_qua_quy_c1 = quarterly(ket_qua_idx_c1["r"], SNAPSHOT)
ket_qua_quy_c2 = ket_qua_quy_c1
quy_day_du_demo = ket_qua_quy_c1["quy_day_du"]

# Bắt đầu lời giải

import pandas as pd


def quarterly_yoy(quy_day_du: pd.Series) -> pd.Series:
    # pct_change với periods=4 tính toán trực tiếp tỷ lệ thay đổi sau 4 kỳ
    cung_ky = quy_day_du.pct_change(periods=4)
    return cung_ky


# Gọi thực nghiệm hàm với dữ liệu mẫu:
yoy_quy_c2 = quarterly_yoy(ket_qua_quy_c2["quy_day_du"])
display(yoy_quy_c2.tail(4))

# Kết thúc lời giải
```

#### Giải thích cách 2

Tách giá trị hiện tại và giá trị dịch bốn kỳ bằng `shift(4)` làm rõ tử số và mẫu số. Phải dùng cùng lịch quý đầy đủ để bốn vị trí thực sự là một năm. Mẫu số bằng 0 không cho một tỷ lệ hữu hạn và cần được báo riêng thay vì diễn giải như tăng trưởng bình thường.

#### Kết quả cách 2

| date | Giá trị |
| --- | --- |
| 2025-06-30 00:00:00 | 0.233333 |
| 2025-09-30 00:00:00 | 0.227273 |
| 2025-12-31 00:00:00 | 0.340102 |
| 2026-03-31 00:00:00 | 0.521886 |
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi muốn tính nhanh tỷ lệ thay đổi trên chuỗi quý liên tục bằng phương thức có sẵn của pandas. Cách 2 thích hợp khi cần kiểm tra chặt chẽ mẫu số bằng 0 hoặc muốn giữ riêng mức chênh lệch tuyệt đối trước khi chia.

:::

---

<span id="data-lab-08-11"></span>
### Bài tập 11: So sánh theo tháng: So với kỳ liền trước và so với cùng kỳ năm trước

::: exercise Tính toán hai hệ quy chiếu so sánh
So tháng này với tháng trước và so cùng tháng năm trước dùng hai kỳ gốc khác nhau. Cần xác định câu hỏi trước khi chọn phép dịch kỳ và mẫu số.

Hãy viết hàm `period_changes(thang: pd.Series, moc: str) -> dict` nhận vào Series số đếm theo tháng (chỉ mục là ngày cuối tháng `pd.offsets.MonthEnd`) và nhãn tháng cần báo cáo `moc` (ví dụ: `"2026-05-31"`). Hàm trả về từ điển gồm:
1. `so_ky_truoc`: Tỷ lệ phần trăm thay đổi so với tháng liền trước (nhãn lùi 1 tháng).
2. `so_cung_ky`: Tỷ lệ phần trăm thay đổi so với cùng tháng năm trước (nhãn lùi 12 tháng).

Công thức tính phần trăm thay đổi:
$$
r = \left(\frac{a}{b} - 1\right)100.
$$

Trong công thức, $a$ là giá trị kỳ báo cáo và $b$ là giá trị kỳ gốc khác 0. Kết quả $r$ ở thang phần trăm.
:::

::: solution
#### Cách 1: Sử dụng MonthEnd offset để định vị nhãn kỳ gốc chính xác

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def period_changes(thang: pd.Series, moc: str) -> dict:
    moc_tg = pd.Timestamp(moc)

    # 1. Xác định nhãn ngày cuối tháng của kỳ liền trước và cùng kỳ năm trước
    nhan_ky_truoc = moc_tg - pd.offsets.MonthEnd(1)
    nhan_cung_ky = moc_tg - pd.offsets.MonthEnd(12)

    # 2. Lấy giá trị tương ứng từ Series tháng
    val_hien_tai = thang.loc[moc_tg]
    val_ky_truoc = thang.loc[nhan_ky_truoc]
    val_cung_ky = thang.loc[nhan_cung_ky]

    # 3. Tính phần trăm thay đổi không làm tròn
    so_ky_truoc = (val_hien_tai / val_ky_truoc - 1.0) * 100.0
    so_cung_ky = (val_hien_tai / val_cung_ky - 1.0) * 100.0

    return {
        "so_ky_truoc": float(so_ky_truoc),
        "so_cung_ky": float(so_cung_ky),
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
thang_series = ket_qua_idx_c1["r"].resample("ME").size()
kq_so_sanh_c1 = period_changes(thang_series, "2026-05-31")
display(f"Tháng 5/2026 so tháng trước: {kq_so_sanh_c1['so_ky_truoc']:+.1f}%")
display(f"Tháng 5/2026 so cùng kỳ: {kq_so_sanh_c1['so_cung_ky']:+.1f}%")

# Kết thúc lời giải
```

#### Giải thích cách 1

So sánh với kỳ trước và cùng kỳ là hai câu hỏi khác nhau. `shift(1)` lấy kỳ liền trước, còn dịch 12 tháng lấy cùng tháng năm trước nếu Series có lịch tháng liên tục. Giữ rõ mốc cần đọc trong kết quả, không lấy phần tử cuối theo vị trí nếu đề chỉ định một tháng cụ thể.

#### Kết quả cách 1

| Kết quả |
| --- |
| Tháng 5/2026 so cùng kỳ: +57.1% |

#### Cách 2: Sử dụng phương thức pct_change trên toàn chuỗi tháng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

thang_series = ket_qua_idx_c1["r"].resample("ME").size()
thang_4nam_demo = thang_series.loc["2022":"2025"]

# Bắt đầu lời giải

import pandas as pd


def period_changes(thang: pd.Series, moc: str) -> dict:
    moc_tg = pd.Timestamp(moc)

    # Tính toán toàn bộ chuỗi phần trăm thay đổi
    pct_1 = thang.pct_change(periods=1) * 100.0
    pct_12 = thang.pct_change(periods=12) * 100.0

    so_ky_truoc = float(pct_1.loc[moc_tg])
    so_cung_ky = float(pct_12.loc[moc_tg])

    return {
        "so_ky_truoc": so_ky_truoc,
        "so_cung_ky": so_cung_ky,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_so_sanh_c2 = period_changes(thang_series, "2026-05-31")
display(f"Tháng 5/2026 so tháng trước: {kq_so_sanh_c2['so_ky_truoc']:+.1f}%")
display(f"Tháng 5/2026 so cùng kỳ: {kq_so_sanh_c2['so_cung_ky']:+.1f}%")

# Kết thúc lời giải
```

#### Giải thích cách 2

Đóng gói các phép so sánh thành dict giúp báo cáo mang tên đại lượng rõ ràng. Kiểm tra sự tồn tại của kỳ gốc và giá trị mẫu số trước khi chia. Kết quả cho tháng hiện tại chỉ được báo như kết quả cả tháng khi phạm vi quan sát của tháng đó đã đầy đủ.

#### Kết quả cách 2

| Kết quả |
| --- |
| Tháng 5/2026 so cùng kỳ: +57.1% |
#### So sánh cách dùng

Hãy chọn Cách 1 khi bạn cần tra cứu chính xác một tháng cụ thể và kiểm tra tường minh sự tồn tại của các kỳ đối chiếu. Cách 2 phù hợp hơn khi muốn tính sẵn các chuỗi thay đổi trên toàn bộ lịch sử rồi mới trích xuất kết quả cần đọc.

:::

---

<span id="data-lab-08-12"></span>
### Bài tập 12: Chuẩn hóa độ dài tháng và xử lý năm nhuận khi so sánh chu kỳ tháng

::: exercise Điều chỉnh số ngày khác biệt của các tháng
Khi phân tích tính mùa vụ theo tháng, tháng 2 có số ngày ít hơn các tháng khác (28 ngày trong năm thường và 29 ngày trong năm nhuận). Nếu so sánh tổng số đánh giá thô, tháng 2 luôn xuất hiện mức sụt giảm giả tạo chỉ vì khoảng thời gian quan sát ngắn hơn 3 ngày (hoặc 2 ngày).

Cho chuỗi số đếm theo tháng của 4 năm liên tục từ 2022 đến 2025 (48 tháng). Hãy viết hàm `monthly_daily_rate(thang_4nam: pd.Series) -> dict` thực hiện:
1. Tính `tong`: Series tổng số đánh giá theo từng tháng trong 4 năm (chỉ mục là số nguyên từ 1 đến 12).
2. Tính `tb_ngay`: Series số đánh giá trung bình mỗi ngày theo từng tháng (chỉ mục từ 1 đến 12), bằng tổng số đánh giá của tháng đó chia cho tổng số ngày thực tế của tháng đó trong cả 4 năm (sử dụng thuộc tính `.index.days_in_month` có tính đến năm nhuận 2024).
3. Tính `chenh_tong`: Mức thay đổi tháng 2 so với tháng 1 theo tổng số đánh giá dạng tỷ lệ (`tong[2] / tong[1] - 1`).
4. Tính `chenh_ngay`: Mức thay đổi tháng 2 so với tháng 1 theo số đánh giá trung bình mỗi ngày dạng tỷ lệ (`tb_ngay[2] / tb_ngay[1] - 1`).
:::

::: solution
#### Cách 1: Sử dụng days_in_month và nhóm theo tháng lịch

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def monthly_daily_rate(thang_4nam: pd.Series) -> dict:
    # 1. Trích xuất số ngày thực tế của từng tháng trong chuỗi
    so_ngay = pd.Series(thang_4nam.index.days_in_month, index=thang_4nam.index)

    # 2. Gom nhóm theo số tháng trong năm (1 đến 12)
    thang_so = pd.Index(thang_4nam.index.month, name="thang")
    tong = thang_4nam.groupby(thang_so).sum()
    tong_ngay = so_ngay.groupby(thang_so).sum()

    # 3. Tính số đánh giá trung bình mỗi ngày của từng tháng
    tb_ngay = tong / tong_ngay

    # 4. Tính toán tỷ lệ thay đổi tháng 2 so với tháng 1
    chenh_tong = float(tong.loc[2] / tong.loc[1] - 1.0)
    chenh_ngay = float(tb_ngay.loc[2] / tb_ngay.loc[1] - 1.0)

    return {
        "tong": tong,
        "tb_ngay": tb_ngay,
        "chenh_tong": chenh_tong,
        "chenh_ngay": chenh_ngay,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
thang_4nam_demo = ket_qua_idx_c1["r"].resample("ME").size().loc["2022":"2025"]
kq_rate_c1 = monthly_daily_rate(thang_4nam_demo)
display(f"Chênh lệch theo tổng: {kq_rate_c1['chenh_tong']:.2%}")
display(f"Chênh lệch theo ngày: {kq_rate_c1['chenh_ngay']:.2%}")

# Kết thúc lời giải
```

#### Giải thích cách 1

Tháng 1 và tháng 2 không có cùng số ngày. Chia số đánh giá từng tháng cho số ngày lịch của chính tháng đó tạo tốc độ đánh giá trên một ngày. Thuộc tính `days_in_month` giữ đúng tháng 2 của năm nhuận, tránh viết cứng 28 ngày.

#### Kết quả cách 1

| Kết quả |
| --- |
| Chênh lệch theo ngày: -0.37% |

#### Cách 2: Tạo DataFrame trung gian với Named Aggregation

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

thang_series = ket_qua_idx_c1["r"].resample("ME").size()
thang_4nam_demo = thang_series.loc["2022":"2025"]

# Bắt đầu lời giải

import pandas as pd


def monthly_daily_rate(thang_4nam: pd.Series) -> dict:
    # Xây dựng bảng trung gian gồm số đánh giá và số ngày tương ứng
    df_thang = pd.DataFrame(
        {
            "so_danh_gia": thang_4nam,
            "so_ngay": thang_4nam.index.days_in_month,
            "thang": thang_4nam.index.month,
        }
    )

    # Tổng hợp đồng thời số lượng và số ngày
    bang_tong_hop = df_thang.groupby("thang").agg(
        tong_danh_gia=("so_danh_gia", "sum"),
        tong_so_ngay=("so_ngay", "sum"),
    )

    tong = bang_tong_hop["tong_danh_gia"]
    tb_ngay = bang_tong_hop["tong_danh_gia"] / bang_tong_hop["tong_so_ngay"]

    chenh_tong = float(tong.loc[2] / tong.loc[1] - 1.0)
    chenh_ngay = float(tb_ngay.loc[2] / tb_ngay.loc[1] - 1.0)

    return {
        "tong": tong,
        "tb_ngay": tb_ngay,
        "chenh_tong": chenh_tong,
        "chenh_ngay": chenh_ngay,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_rate_c2 = monthly_daily_rate(thang_4nam_demo)
display(f"Chênh lệch theo tổng: {kq_rate_c2['chenh_tong']:.2%}")
display(f"Chênh lệch theo ngày: {kq_rate_c2['chenh_ngay']:.2%}")

# Kết thúc lời giải
```

#### Giải thích cách 2

Tính cả tỷ lệ theo tổng tháng lẫn tỷ lệ theo số đánh giá mỗi ngày giúp thấy ảnh hưởng của độ dài tháng. Chúng có thể khác nhau mà không mâu thuẫn. Chỉ dùng số ngày lịch cho một tháng đã quan sát đủ, nếu dữ liệu kết thúc giữa tháng cần mẫu số là phạm vi quan sát tương ứng.

#### Kết quả cách 2

| Kết quả |
| --- |
| Chênh lệch theo ngày: -0.37% |
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi chỉ cần tính nhanh chỉ số đánh giá trung bình mỗi ngày theo số ngày thực tế của từng tháng. Cách 2 phù hợp khi bạn muốn xây dựng bảng tổng hợp hoàn chỉnh gồm cả số lượng và tốc độ để đối chiếu nhiều khía cạnh.

:::

---

<span id="data-lab-08-13"></span>
### Bài tập 13: Mở rộng 1: Điều tra ngày kỷ lục và vùng lân cận bằng chuỗi ngày

::: exercise Điều tra ngày kỷ lục
Trong chuỗi thời gian vận hành, các đỉnh đột biến thường gắn liền với sự kiện văn hóa hoặc lễ hội lớn. Để điều tra nguyên nhân, ta cần xác định ngày có số lượng đánh giá cao nhất toàn chuỗi và kiểm tra số lượng của các ngày xung quanh.

Hãy viết hàm `investigate_peak_day(r: pd.DataFrame) -> dict` nhận vào bảng `r` đã đánh chỉ mục thời gian. Hàm thực hiện:
1. Tổng hợp số đánh giá mỗi ngày của toàn bộ chuỗi bằng `r.resample("D").size()`.
2. Tìm ngày đạt số lượng đánh giá cao nhất toàn chuỗi `ngay_ky_luc` (`idxmax()`) và số lượng tại ngày đó `so_luong_ky_luc`.
3. Trích xuất một Series `vung_lan_can` gồm đúng 5 ngày liên tiếp nằm quanh ngày kỷ lục (từ 2 ngày trước đến 2 ngày sau ngày kỷ lục).
:::

::: solution
#### Cách 1: Sử dụng resample ngày và cắt lát bằng Timedelta

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def investigate_peak_day(r: pd.DataFrame) -> dict:
    # 1. Tổng hợp số đánh giá theo ngày toàn chuỗi
    chuoi_ngay = r.resample("D").size()

    # 2. Định vị ngày có số lượng đánh giá kỷ lục
    ngay_ky_luc = chuoi_ngay.idxmax()
    so_luong_ky_luc = int(chuoi_ngay.loc[ngay_ky_luc])

    # 3. Trích xuất vùng lân cận 5 ngày bằng khoảng thời gian Timedelta
    dau = ngay_ky_luc - pd.Timedelta(days=2)
    cuoi = ngay_ky_luc + pd.Timedelta(days=2)
    vung_lan_can = chuoi_ngay.loc[dau:cuoi]

    return {
        "ngay_ky_luc": ngay_ky_luc,
        "so_luong_ky_luc": so_luong_ky_luc,
        "vung_lan_can": vung_lan_can,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_dieu_tra_c1 = investigate_peak_day(ket_qua_idx_c1["r"])
display(
    f"Ngày kỷ lục: {kq_dieu_tra_c1['ngay_ky_luc']:%Y-%m-%d} với {kq_dieu_tra_c1['so_luong_ky_luc']} đánh giá"
)
display(kq_dieu_tra_c1["vung_lan_can"])

# Kết thúc lời giải
```

#### Giải thích cách 1

Đếm đánh giá theo từng ngày rồi tìm ngày có số đếm cao nhất. Nhãn ngày kỷ lục và số dòng của ngày đó là hai phần khác nhau của kết quả. Việc kiểm lại các bản ghi gốc giúp nhận biết một cụm nhập dữ liệu hoặc trùng khóa, không tự giải thích đó là ngày nhiều khách nhất.

#### Kết quả cách 1

| date | Giá trị |
| --- | --- |
| 2026-03-14 00:00:00 | 8 |
| 2026-03-15 00:00:00 | 8 |
| 2026-03-16 00:00:00 | 50 |
| 2026-03-17 00:00:00 | 8 |
| 2026-03-18 00:00:00 | 8 |

#### Cách 2: Sử dụng nlargest và cắt lát đối xứng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd


def sinh_so_danh_gia(ngay: pd.Timestamp) -> int:
    muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[
        ngay.year
    ]
    if ngay.year == 2020 and 3 <= ngay.month <= 6:
        muc = 0
    if ngay.month in (1, 2):
        muc += 2
    if ngay.dayofweek == 0:
        muc += 2
    if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
        muc += 6
    if ngay == pd.Timestamp("2026-03-16"):
        muc += 40
    return muc


_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")

_so = [sinh_so_danh_gia(ngay) for ngay in _ngay]

DEMO_REVIEWS = pd.DataFrame({"date": _ngay.repeat(_so)})

DEMO_REVIEWS.insert(0, "listing_id", [100 + k % 37 for k in range(len(DEMO_REVIEWS))])

DEMO_REVIEWS = DEMO_REVIEWS.sample(frac=1, random_state=8).reset_index(drop=True)

SNAPSHOT = "2026-06-29"


def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Tạo mặt nạ lọc các dòng hợp lệ tại hoặc trước mốc chụp
    mat_na_hop_le = rv["date"] <= moc_tg

    # 2. Đếm số dòng xuất hiện sau mốc chụp dữ liệu
    so_dong_sau = int((~mat_na_hop_le).sum())

    # 3. Lọc dữ liệu, gán cột date làm chỉ mục và sắp xếp đơn điệu tăng dần
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index(kind="mergesort")

    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r,
    }


ket_qua_idx_c1 = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
ket_qua_idx_c2 = ket_qua_idx_c1

# Bắt đầu lời giải

import pandas as pd


def investigate_peak_day(r: pd.DataFrame) -> dict:
    chuoi_ngay = r.resample("D").size()

    # Lấy ngày kỷ lục thông qua phương thức nlargest
    top_1 = chuoi_ngay.nlargest(1)
    ngay_ky_luc = top_1.index[0]
    so_luong_ky_luc = int(top_1.iloc[0])

    # Lấy vùng lân cận bằng chỉ số ngày đại số
    khoang_cach = pd.DateOffset(days=2)
    vung_lan_can = chuoi_ngay.loc[ngay_ky_luc - khoang_cach : ngay_ky_luc + khoang_cach]

    return {
        "ngay_ky_luc": ngay_ky_luc,
        "so_luong_ky_luc": so_luong_ky_luc,
        "vung_lan_can": vung_lan_can,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_dieu_tra_c2 = investigate_peak_day(ket_qua_idx_c2["r"])
display(
    f"Ngày kỷ lục: {kq_dieu_tra_c2['ngay_ky_luc']:%Y-%m-%d} với {kq_dieu_tra_c2['so_luong_ky_luc']} đánh giá"
)
display(kq_dieu_tra_c2["vung_lan_can"])

# Kết thúc lời giải
```

#### Giải thích cách 2

Gom các dấu kiểm vào một báo cáo giúp giữ lại số dòng, ngày và các thông tin đối chiếu. Tìm các chỗ ở hoặc bản ghi tạo nên đỉnh trước khi nêu một lời giải thích. Mỗi đánh giá là một sự kiện trong nguồn, không đồng nhất với một lần đặt phòng trong cùng ngày.

#### Kết quả cách 2

| date | Giá trị |
| --- | --- |
| 2026-03-14 00:00:00 | 8 |
| 2026-03-15 00:00:00 | 8 |
| 2026-03-16 00:00:00 | 50 |
| 2026-03-17 00:00:00 | 8 |
| 2026-03-18 00:00:00 | 8 |
#### So sánh cách dùng

Hãy chọn Cách 1 khi bạn chỉ cần xác định nhanh ngày đạt đỉnh kỷ lục và giá trị số đếm cao nhất trong chuỗi. Cách 2 cần thiết khi bạn muốn trích xuất các bản ghi gốc trong ngày đó nhằm kiểm tra dấu hiệu trùng lặp hoặc bất thường.

:::

---

<span id="data-lab-08-14"></span>
### Bài tập 14: Mở rộng 2: Tính khoảng cách thời gian từ lần đánh giá gần nhất

::: exercise Gắn cờ chỗ ở lâu chưa có đánh giá
Trong dữ liệu chỗ ở (`listings`), cột `last_review` ghi nhận ngày nhận đánh giá gần nhất. Một chỗ ở không nhận thêm đánh giá nào trong hơn 365 ngày tính đến mốc chụp dữ liệu có khả năng cao đã ngừng hoạt động hoặc rời khỏi nền tảng.

Cho DataFrame `listings` chứa cột `last_review`. Hãy viết hàm `days_since_last_review(listings: pd.DataFrame, snapshot: str) -> dict` thực hiện:
1. Chuyển đổi cột `last_review` sang kiểu `datetime64`.
2. Xác định `so_cho_o_ngoai_moc`: Số lượng chỗ ở có ngày đánh giá sau `snapshot`.
3. Lọc bỏ các chỗ ở ngoài mốc này, sau đó tính số ngày từ lần đánh giá gần nhất đến mốc chụp dữ liệu (`(pd.Timestamp(snapshot) - last_review).dt.days`).
4. Gán nhãn cờ boolean `co_khong_hoat_dong` bằng `True` nếu chỗ ở có số ngày trên 365 ngày hoặc chưa từng có đánh giá nào (`last_review` bị khuyết).
5. Trả về từ điển gồm: `so_cho_o_ngoai_moc`, `so_cho_o_tren_365_ngay` (đếm trên các chỗ ở có đánh giá và cách trên 365 ngày), và DataFrame kết quả `listings_gan_co`.
:::

::: solution
#### Cách 1: Xử lý tuần tự bằng các phép toán Series trực tiếp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

SNAPSHOT = "2026-06-29"

LISTINGS_DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105],
        "name": [
            "Căn hộ trung tâm",
            "Phòng riêng Bellas Artes",
            "Loft Providencia",
            "Studio Recoleta",
            "Nhà cổ Brasil",
        ],
        "last_review": ["2026-05-15", "2025-01-10", "2026-07-02", "2024-11-20", None],
    }
)

# Bắt đầu lời giải

import pandas as pd


def days_since_last_review(listings: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # 1. Ép kiểu dữ liệu thời gian an toàn
    df = listings.copy()
    df["last_review_dt"] = pd.to_datetime(df["last_review"], errors="coerce")

    # 2. Xác định các chỗ ở có ngày ghi nhận sau mốc chụp
    ngoai_moc_mask = df["last_review_dt"] > moc_tg
    so_ngoai_moc = int(ngoai_moc_mask.sum())

    # 3. Giữ lại các chỗ ở hợp lệ và tính số ngày trôi qua
    df_hop_le = df.loc[~ngoai_moc_mask].copy()
    so_ngay = (moc_tg - df_hop_le["last_review_dt"]).dt.days
    df_hop_le["so_ngay_tu_rv_cuoi"] = so_ngay

    # 4. Xác định chỗ ở trên 365 ngày và gắn cờ không hoạt động
    tren_365 = so_ngay > 365
    so_tren_365 = int(tren_365.sum())

    # Cờ không hoạt động: Hoặc trên 365 ngày hoặc chưa từng có review (khuyết)
    df_hop_le["co_khong_hoat_dong"] = tren_365 | df_hop_le["last_review_dt"].isna()

    return {
        "so_cho_o_ngoai_moc": so_ngoai_moc,
        "so_cho_o_tren_365_ngay": so_tren_365,
        "listings_gan_co": df_hop_le,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_last_rv_c1 = days_since_last_review(LISTINGS_DEMO, SNAPSHOT)
display(
    f"Ngoài mốc: {kq_last_rv_c1['so_cho_o_ngoai_moc']}, Trên 365 ngày: {kq_last_rv_c1['so_cho_o_tren_365_ngay']}"
)
display(
    kq_last_rv_c1["listings_gan_co"][
        ["name", "so_ngay_tu_rv_cuoi", "co_khong_hoat_dong"]
    ]
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Đọc `last_review` thành ngày rồi lấy snapshot trừ ngày đánh giá cuối. `.dt.days` cho số ngày đã trôi qua, còn chỗ ở chưa có ngày đánh giá giữ NaN. Khoảng thời gian dài không có đánh giá là một dấu hiệu cần khảo sát, không đủ chứng minh chỗ ở đã ngừng hoạt động.

#### Kết quả cách 1

| Chỉ mục | name | so_ngay_tu_rv_cuoi | co_khong_hoat_dong |
| --- | --- | --- | --- |
| 0 | Căn hộ trung tâm | 45 | False |
| 1 | Phòng riêng Bellas Artes | 535 | True |
| 3 | Studio Recoleta | 586 | True |
| 4 | Nhà cổ Brasil | NaN | True |

#### Cách 2: Sử dụng assign và phương thức vector hóa an toàn

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

SNAPSHOT = "2026-06-29"

LISTINGS_DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105],
        "name": [
            "Căn hộ trung tâm",
            "Phòng riêng Bellas Artes",
            "Loft Providencia",
            "Studio Recoleta",
            "Nhà cổ Brasil",
        ],
        "last_review": ["2026-05-15", "2025-01-10", "2026-07-02", "2024-11-20", None],
    }
)

# Bắt đầu lời giải

import pandas as pd
import numpy as np


def days_since_last_review(listings: pd.DataFrame, snapshot: str) -> dict:
    moc_tg = pd.Timestamp(snapshot)

    # Chuyển đổi và lọc các dòng hợp lệ trong một bước
    rev_dt = pd.to_datetime(listings["last_review"], errors="coerce")
    mask_ngoai = rev_dt > moc_tg
    so_ngoai_moc = int(mask_ngoai.sum())

    df_loc = listings.loc[~mask_ngoai].copy()
    rev_loc = rev_dt.loc[~mask_ngoai]

    so_ngay = (moc_tg - rev_loc).dt.days
    co_ngung = (so_ngay > 365) | rev_loc.isna()

    df_loc = df_loc.assign(
        so_ngay_tu_rv_cuoi=so_ngay,
        co_khong_hoat_dong=co_ngung,
    )

    so_tren_365 = int((so_ngay > 365).sum())

    return {
        "so_cho_o_ngoai_moc": so_ngoai_moc,
        "so_cho_o_tren_365_ngay": so_tren_365,
        "listings_gan_co": df_loc,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_last_rv_c2 = days_since_last_review(LISTINGS_DEMO, SNAPSHOT)
display(
    f"Ngoài mốc: {kq_last_rv_c2['so_cho_o_ngoai_moc']}, Trên 365 ngày: {kq_last_rv_c2['so_cho_o_tren_365_ngay']}"
)
display(
    kq_last_rv_c2["listings_gan_co"][
        ["name", "so_ngay_tu_rv_cuoi", "co_khong_hoat_dong"]
    ]
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Tạo các mặt nạ riêng cho ngày thiếu, ngày sau snapshot và ngày đã cũ giúp báo cáo phân biệt ba tình huống. Không gom mọi kết quả âm hoặc thiếu vào nhóm ngừng hoạt động. Quy tắc gắn cờ phải nêu rõ ngưỡng ngày và chỉ được dùng trong phạm vi nguồn đang xét.

#### Kết quả cách 2

| Chỉ mục | name | so_ngay_tu_rv_cuoi | co_khong_hoat_dong |
| --- | --- | --- | --- |
| 0 | Căn hộ trung tâm | 45 | False |
| 1 | Phòng riêng Bellas Artes | 535 | True |
| 3 | Studio Recoleta | 586 | True |
| 4 | Nhà cổ Brasil | NaN | True |
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi chỉ cần tính nhanh khoảng cách ngày giữa lần đánh giá cuối và mốc snapshot vào một cột số liệu. Cách 2 phù hợp hơn khi cần gắn cờ phân loại chi tiết để tách biệt giữa dữ liệu khuyết thiếu, mốc sai lệch và hồ sơ đã cũ.

:::

---

## 4. Tóm tắt các quy tắc xử lý chuỗi thời gian

| Khái niệm / Thao tác | Cú pháp khuyến nghị | Lưu ý nghiệp vụ và kỹ thuật |
| :--- | :--- | :--- |
| Ép kiểu ngày giờ | `pd.to_datetime(..., format=..., errors="coerce")` | Luôn chỉ định định dạng ngày và xử lý lỗi thành `NaT` |
| Cắt lát nhãn chuỗi | `r.loc["2025"]` hoặc `r.loc["2025-01":"2025-06"]` | Bắt buộc `DatetimeIndex` phải được sắp xếp đơn điệu tăng dần |
| Tổng hợp theo quý | `r.resample("QE").size()` | Bí danh `QE` thay thế `Q`, luôn kiểm tra kỳ chưa trọn cuối cùng |
| Lưới ngày liên tục | `r.loc[nam].resample("D").size()` | Cắt lát năm trước khi resample, tự động điền 0 cho ngày trống |
| Cửa sổ trượt 7 ngày | `ngay.rolling(7, center=True).mean()` | Phân biệt cửa sổ 7 hàng và 7 ngày, kiểm soát `min_periods` |
| So sánh cùng kỳ theo quý | `quy / quy.shift(4) - 1.0` | Dữ liệu quý dùng bước nhảy 4, tránh sao chép máy móc bước nhảy 12 của tháng |
| So sánh theo tháng | `period_changes(thang, moc)` | Phân biệt rõ giữa so kỳ trước (MoM) và so cùng kỳ năm trước (YoY) |
| Chuẩn hóa độ dài tháng | `tong_thang / tong_ngay_thuc_te` | Dùng `.index.days_in_month` để triệt tiêu ảnh hưởng của tháng 2 và năm nhuận |
