## Lab 12: Biểu đồ cho báo cáo và phương pháp kiểm định cấu trúc hình ảnh

Một hình lưu thành công vẫn có thể vẽ sai dữ liệu, thiếu đơn vị hoặc dùng trục gây hiểu nhầm. Ta sẽ tính bảng dùng để vẽ, xuất hình từ mã và kiểm lại cả số liệu lẫn cách trình bày.

---

## 1. Mục tiêu và bài toán thực tế

Xét bài toán thực tế: Một nhóm chuyên viên phân tích thị trường lưu trú du lịch cần xây dựng bộ trực quan hóa dữ liệu phục vụ báo cáo định kỳ tại vùng đô thị Santiago de Chile. Bản báo cáo phải giải quyết năm thách thức kỹ thuật cốt lõi:
1. Tổng hợp chuỗi thời gian lượt đánh giá theo tháng của từng quận từ hai bảng dữ liệu liên kết, nhận diện và loại bỏ các kỳ chưa trọn vẹn để tránh đưa ra kết luận sai về xu hướng suy giảm.
2. Thiết kế biểu đồ đường hoàn chỉnh với bốn thành phần chuẩn mực: Đường số liệu chính xác, tiêu đề nêu thông điệp phân tích rõ ràng, nhãn trục tung kèm đơn vị đo lường, và chú thích nguồn gốc dữ liệu minh bạch ở chân hình.
3. Thống kê tỷ lệ loại phòng nguyên căn (`Entire home/apt`) tại các quận đạt ngưỡng quy mô tối thiểu, chuyển đổi thành biểu đồ thanh ngang có nhãn giá trị trực tiếp trên thanh và trục hoành xuất phát từ gốc tọa độ 0.
4. Khám phá phân phối của chỉ số số ngày mở lịch trong năm (`availability_365`) bằng biểu đồ tần suất (histogram) với số khoảng chia xác định, bóc tách hai nhóm hành vi trái ngược và làm rõ lý do số bình quân đơn lẻ không thể đại diện cho dữ liệu có phân phối hai đỉnh.
5. Vạch trần kỹ thuật thao túng thị giác do việc cắt ngắn trục tung gây ra, sửa lại thành biểu đồ cột trung thực và xây dựng hàm kiểm định tự động cấu trúc hình ảnh bằng thư viện kiểm thử `assert`.

---

## 2. Dữ liệu thực hành và chuẩn bị môi trường

Để bảo đảm toàn bộ mã nguồn có thể thực thi độc lập và kiểm chứng ngoại tuyến (offline), bài thực hành sử dụng bộ dữ liệu mẫu giả lập chuẩn hóa được thiết kế dựa trên các quy luật thống kê của dữ liệu thực tế tại Santiago:
1. Bảng chỗ ở mẫu `DEMO_DS` (60 chỗ ở tại 6 quận: Santiago, Providencia, Las Condes, Ñuñoa, Lo Barnechea và Vitacura) với thông tin phân loại phòng và số ngày mở lịch.
2. Bảng đánh giá mẫu `DEMO_RV` (1.905 lượt đánh giá từ ngày 2024-01-10 đến 2026-07-01) liên kết với bảng chỗ ở qua mã định danh `listing_id`.
3. Thư mục lưu trữ hình ảnh `figures/` được khởi tạo tự động từ mã nguồn.

```python
import numpy as np
import pandas as pd
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path
from IPython.display import display

# Thiết lập hành vi Copy-on-Write an toàn cho pandas
if pd.__version__.startswith("2.") or pd.__version__.startswith("3."):
    pd.set_option("mode.copy_on_write", True)

# Địa chỉ snapshot dữ liệu thực tế tại Santiago de Chile phục vụ đối chiếu
SNAPSHOT_URL = (
    "https://data.insideairbnb.com/chile/rm/santiago/"
    "2026-06-29/visualisations/listings.csv"
)

# Mốc chụp dữ liệu chuẩn hóa của tập dữ liệu
SNAPSHOT = "2026-06-29"

# Khởi tạo thư mục chứa sản phẩm biểu đồ
Path("figures").mkdir(parents=True, exist_ok=True)

# Cấu hình phong cách đồ họa thống nhất cho toàn bộ bài thực hành
plt.rcParams["svg.fonttype"] = "path"
plt.rcParams.update(
    {
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.25,
        "font.size": 11,
    }
)

# 1. Bảng chỗ ở giả lập chuẩn hóa: 60 chỗ ở tại 6 quận với chu kỳ loại phòng cố định
_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)
_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}
DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

# 2. Bảng đánh giá giả lập chuẩn hóa: 1.905 lượt đánh giá liên kết qua listing_id
_dong = []
for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))
DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])
```

> [!NOTE]
> **Đối chiếu thực tế**: Khi xử lý tệp dữ liệu đầy đủ của thành phố Santiago, mốc chụp 2026-06-29 ghi nhận tổng cộng 188 tháng đánh giá tại quận Providencia với 2.810 lượt đánh giá trong tháng 06 năm 2026. Các bài tập dưới đây sử dụng dữ liệu mẫu giả lập nhằm bảo đảm khả năng tái lập và kiểm chứng ngoại tuyến hoàn toàn, tuyệt đối không suy diễn các con số này thành dữ liệu lịch sử của vùng đô thị Santiago.

---

## 3. Nội dung chi tiết bộ bài tập thực hành

<span id="data-lab-12-01"></span>
### Bài tập 1: Lọc dữ liệu theo quận và tổng hợp chuỗi đánh giá theo tháng

::: exercise Tổng hợp chuỗi đánh giá theo tháng
Trong phân tích chuỗi thời gian của từng địa bàn, bảng đánh giá (`rv`) chỉ lưu mã số chỗ ở (`listing_id`) và ngày tháng (`date`), còn tên địa bàn (`neighbourhood`) lại nằm ở bảng chỗ ở (`ds`). Cần liên kết hai bảng này để lọc ra các đánh giá thuộc quận mục tiêu, đếm số lượng theo chu kỳ tháng và loại bỏ tháng cuối cùng chưa trọn vẹn.

Hãy viết hàm `monthly_reviews(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series` thực hiện các yêu cầu:
1. Lấy tập hợp các mã định danh `id` của các chỗ ở thuộc quận `quan` trong bảng `ds`.
2. Lọc các dòng trong bảng `rv` có `listing_id` thuộc tập hợp mã định danh vừa tìm được.
3. Chuyển đổi cột `date` thành chỉ mục thời gian và tổng hợp số lượng đánh giá theo từng tháng bằng phương thức `resample("ME").size()`.
4. Loại bỏ phần tử tháng cuối cùng trong chuỗi vì theo giả thiết của biến thể này, kỳ cuối chưa được quan sát đủ, tránh tạo ra ảo giác sụt giảm mạnh về số đánh giá.
5. Trả về Series với chỉ mục là ngày cuối tháng (`DatetimeIndex`) và giá trị là số lượt đánh giá nguyên dương. Đảm bảo hàm không làm thay đổi hai DataFrame đầu vào.
:::

::: solution
#### Cách 1: Sử dụng tập hợp set để lọc mã và cắt lát chỉ mục cuối

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

_dong = []

for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))

DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])

# Bắt đầu lời giải

import pandas as pd


def monthly_reviews(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series:
    # 1. Trích xuất tập hợp các mã định danh thuộc quận mục tiêu
    tap_id = set(ds.loc[ds["neighbourhood"] == quan, "id"])

    # 2. Lọc các đánh giá có mã chỗ ở thuộc tập hợp trên
    rv_quan = rv[rv["listing_id"].isin(tap_id)]

    # 3. Đặt cột date làm chỉ mục và gom nhóm theo ngày cuối tháng
    thang = rv_quan.set_index("date").resample("ME").size()

    # 4. Loại bỏ tháng cuối cùng chưa trọn vẹn bằng cú pháp cắt lát
    return thang.iloc[:-1]


# Gọi thực nghiệm hàm với dữ liệu mẫu:
thang_pro_c1 = monthly_reviews(DEMO_RV, DEMO_DS, "Providencia")
display(
    f"Số tháng hợp lệ: {len(thang_pro_c1)}, tháng cuối: {thang_pro_c1.index[-1]:%Y-%m-%d}, số lượt: {thang_pro_c1.iloc[-1]}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Lấy tập ID chỗ ở thuộc quận rồi lọc review theo `isin`. `resample("ME").size()` đếm theo tháng và giữ các tháng nằm giữa hai đầu chuỗi. Bài này yêu cầu bỏ phần tử cuối theo giả thiết kỳ cuối chưa trọn. Không dùng thao tác đó cho mọi tập dữ liệu nếu chưa kiểm mốc quan sát.

#### Kết quả cách 1

| Kết quả |
| --- |
| Số tháng hợp lệ: 30, tháng cuối: 2026-06-30, số lượt: 15 |

#### Cách 2: Sử dụng chuỗi phương thức kết hợp phép lọc boolean trên chỉ mục

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

_dong = []

for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))

DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])

# Bắt đầu lời giải

import pandas as pd


def monthly_reviews(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series:
    # Lọc mã chỗ ở và nối chuỗi phương thức resample để tối ưu bộ nhớ
    danh_sach_id = ds.loc[ds["neighbourhood"] == quan, "id"].to_numpy()
    chuoi_thang = (
        rv.loc[rv["listing_id"].isin(danh_sach_id)]
        .set_index("date")
        .resample("ME")
        .size()
    )
    # Loại bỏ kỳ cuối cùng nếu chuỗi có từ hai mốc thời gian trở lên
    if len(chuoi_thang) >= 2:
        return chuoi_thang.iloc[:-1]
    return chuoi_thang


# Gọi thực nghiệm hàm với dữ liệu mẫu:
thang_pro_c2 = monthly_reviews(DEMO_RV, DEMO_DS, "Providencia")
display(
    f"Cách 2: Tổng số đánh giá = {thang_pro_c2.sum()}, độ dài chuỗi = {len(thang_pro_c2)}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Chuỗi phương thức gắn các bước lọc, đặt chỉ mục và tổng hợp trong một biểu thức. Mã quận được xác định từ bảng chỗ ở, không lấy từ vị trí dòng của review. Cách đếm vẫn là số đánh giá, không phải số đánh giá hoặc doanh thu của quận.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Tổng số đánh giá = 391, độ dài chuỗi = 30 |
#### So sánh cách dùng

Cách 1 mở rõ bước lọc quận, tổng hợp tháng và bỏ kỳ cuối theo yêu cầu đã cho. Cách 2 gom việc lọc và tổng hợp thành chuỗi phương thức. Khi thay dữ liệu, vẫn phải đối chiếu snapshot thay vì mặc nhiên coi mọi tháng còn lại đều trọn vẹn.

:::

---

<span id="data-lab-12-02"></span>
### Bài tập 2: Kiểm soát mốc chụp dữ liệu và nhận diện kỳ chưa trọn

::: exercise Lọc theo mốc chụp dữ liệu
Khi cập nhật dữ liệu từ các đợt phát hành định kỳ (snapshot releases), nhiều bản ghi có thể chứa ngày đánh giá rơi vào sau ngày công bố mốc chụp do độ trễ đồng bộ hệ thống, hoặc bản thân ngày chụp rơi vào giữa kỳ báo cáo (Ví dụ: Ngày 29 tháng 6 khiến tháng 6 thiếu 1 ngày). Cần xây dựng cơ chế kiểm soát mốc chụp tường minh để bảo đảm dữ liệu đưa vào biểu đồ hoàn toàn nhất quán.

Hãy viết hàm `monthly_reviews_with_cutoff(rv: pd.DataFrame, ds: pd.DataFrame, quan: str, snapshot: str = "2026-06-29") -> pd.Series` thực hiện:
1. Lọc bảng `rv` chỉ giữ các dòng có `date` nhỏ hơn hoặc bằng mốc thời gian `snapshot`.
2. Lọc các chỗ ở thuộc quận `quan` và tổng hợp theo tháng bằng `resample("ME").size()`.
3. Kiểm tra xem mốc `snapshot` có trùng với ngày cuối tháng hay không. Nếu `snapshot` rơi vào trước ngày cuối tháng của tháng đó, tháng đó chưa hoàn chỉnh và bắt buộc phải loại bỏ khỏi chuỗi báo cáo.
4. Trả về Series chuỗi tháng đã chuẩn hóa và không chứa kỳ cụt.
:::

::: solution
#### Cách 1: So sánh điều kiện boolean và kiểm tra ngày kết thúc tháng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

_dong = []

for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))

DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])

# Bắt đầu lời giải

import pandas as pd


def monthly_reviews_with_cutoff(
    rv: pd.DataFrame, ds: pd.DataFrame, quan: str, snapshot: str = "2026-06-29"
) -> pd.Series:
    snap_dt = pd.Timestamp(snapshot)
    tap_id = set(ds.loc[ds["neighbourhood"] == quan, "id"])

    # 1. Lọc bản ghi nằm trong mốc chụp và thuộc địa bàn yêu cầu
    dieu_kien = (rv["listing_id"].isin(tap_id)) & (rv["date"] <= snap_dt)
    rv_hop_le = rv.loc[dieu_kien]

    # 2. Gom nhóm theo tháng
    thang = rv_hop_le.set_index("date").resample("ME").size()

    # 3. Kiểm tra xem mốc chụp có rơi vào trước ngày cuối tháng cuối cùng không
    if len(thang) > 0 and snap_dt < thang.index[-1]:
        return thang.iloc[:-1]
    return thang


# Gọi thực nghiệm hàm với dữ liệu mẫu:
thang_cutoff_c1 = monthly_reviews_with_cutoff(
    DEMO_RV, DEMO_DS, "Providencia", "2026-06-29"
)
display(
    f"Mốc cắt 2026-06-29: Số tháng = {len(thang_cutoff_c1)}, tháng cuối = {thang_cutoff_c1.index[-1]:%Y-%m-%d}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Lọc ngày theo snapshot trước khi tổng hợp. So sánh mốc quan sát với ngày cuối tháng để quyết định kỳ nào đã đầy đủ. Một ngày có sự kiện cuối cùng không tự xác định thời điểm dữ liệu đã quan sát đến đâu.

#### Kết quả cách 1

| Kết quả |
| --- |
| Mốc cắt 2026-06-29: Số tháng = 29, tháng cuối = 2026-05-31 |

#### Cách 2: Sử dụng cắt lát chỉ mục thời gian và offset MonthEnd

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

_dong = []

for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))

DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])

# Bắt đầu lời giải

import pandas as pd


def monthly_reviews_with_cutoff(
    rv: pd.DataFrame, ds: pd.DataFrame, quan: str, snapshot: str = "2026-06-29"
) -> pd.Series:
    snap_dt = pd.Timestamp(snapshot)
    danh_sach_id = ds.loc[ds["neighbourhood"] == quan, "id"].to_numpy()

    # Cắt lát chuỗi thời gian trực tiếp trên bảng đánh giá đã sắp xếp
    rv_loc = (
        rv.loc[rv["listing_id"].isin(danh_sach_id)]
        .sort_values("date")
        .set_index("date")
        .loc[:snap_dt]
    )
    thang = rv_loc.resample("ME").size()

    # Xác định ngày cuối tháng trọn vẹn gần nhất
    ngay_cuoi_thang_chuan = (
        snap_dt - pd.offsets.MonthEnd(1)
        if snap_dt < (snap_dt + pd.offsets.MonthEnd(0))
        else snap_dt
    )
    return thang.loc[:ngay_cuoi_thang_chuan]


# Gọi thực nghiệm hàm với dữ liệu mẫu:
thang_cutoff_c2 = monthly_reviews_with_cutoff(
    DEMO_RV, DEMO_DS, "Providencia", "2026-06-29"
)
display(
    f"Cách 2: Tháng cuối trọn vẹn = {thang_cutoff_c2.index[-1]:%Y-%m-%d}, số lượt = {thang_cutoff_c2.iloc[-1]}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Đặt quy tắc giữ kỳ thành mặt nạ riêng giúp kiểm rõ cận thời gian. Hai cách phải cùng quy ước về ngày kết thúc, đặc biệt khi snapshot đúng ngày cuối tháng. Nếu ngày có giờ, cần xác định mốc là đầu ngày hay hết ngày thay vì so sánh ngầm theo nửa đêm.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Tháng cuối trọn vẹn = 2026-05-31, số lượt = 9 |
#### So sánh cách dùng

Cách 1 đặt bước kiểm tra snapshot gần thao tác tổng hợp để dễ đối chiếu mốc thời gian. Cách 2 làm rõ việc giữ các tháng đã hoàn tất. Chọn cách trình bày nào cũng phải phân biệt tháng chưa đủ ngày với tháng có số đánh giá thấp.

:::

---

<span id="data-lab-12-03"></span>
### Bài tập 3: Dựng biểu đồ đường hoàn chỉnh cho chuỗi thời gian

::: exercise Dựng biểu đồ đường đạt chuẩn xuất bản
Biểu đồ cần vẽ đúng chuỗi số liệu, có nhãn đơn vị và thông tin nguồn. Tiêu đề nêu một điều người đọc có thể kiểm ngay trên hình.

Hãy viết hàm `plot_line(thang: pd.Series, path: str) -> matplotlib.axes.Axes` thực hiện các yêu cầu:
1. Khởi tạo khung hình mới bằng giao diện hướng đối tượng `fig, ax = plt.subplots(figsize=(9, 3.5))`.
2. Vẽ một đường duy nhất thể hiện diễn biến của `thang` qua các mốc thời gian bằng `ax.plot(thang.index, thang.values)`.
3. Đặt tiêu đề cho biểu đồ nêu bật thông điệp phân tích (độ dài tiêu đề tối thiểu 15 ký tự).
4. Thiết lập nhãn trục tung có ghi rõ đơn vị tính (`Lượt đánh giá (lượt/tháng)`).
5. Ghi chú thích nguồn số liệu ở góc dưới khung hình bằng phương thức `fig.text(...)` với nội dung không rỗng.
6. Lưu tệp hình ảnh vào đường dẫn `path` với độ phân giải `dpi=150`, tùy chọn `bbox_inches="tight"` và trả về đối tượng `ax`.
:::

::: solution
#### Cách 1: Thiết lập từng thuộc tính qua giao diện hướng đối tượng cơ bản

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

_dong = []

for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))

DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])


def monthly_reviews(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series:
    # 1. Trích xuất tập hợp các mã định danh thuộc quận mục tiêu
    tap_id = set(ds.loc[ds["neighbourhood"] == quan, "id"])

    # 2. Lọc các đánh giá có mã chỗ ở thuộc tập hợp trên
    rv_quan = rv[rv["listing_id"].isin(tap_id)]

    # 3. Đặt cột date làm chỉ mục và gom nhóm theo ngày cuối tháng
    thang = rv_quan.set_index("date").resample("ME").size()

    # 4. Loại bỏ tháng cuối cùng chưa trọn vẹn bằng cú pháp cắt lát
    return thang.iloc[:-1]


thang_pro_c1 = monthly_reviews(DEMO_RV, DEMO_DS, "Providencia")

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import matplotlib.pyplot as plt


def plot_line(thang: pd.Series, path: str):
    # 1. Khởi tạo khung hình với kích thước chuẩn tỷ lệ ngang
    fig, ax = plt.subplots(figsize=(9, 3.5))

    # 2. Vẽ đường chuỗi thời gian
    ax.plot(
        thang.index,
        thang.values,
        color="#1976d2",
        linewidth=2,
        marker="o",
        markersize=3,
    )

    # 3. Đặt tiêu đề nêu thông điệp phân tích cụ thể
    ax.set_title(
        "Diễn biến số lượt đánh giá theo tháng tại quận Providencia (2024–2026)", pad=12
    )

    # 4. Gán nhãn trục tung kèm đơn vị đo lường
    ax.set_ylabel("Lượt đánh giá (lượt/tháng)")
    ax.set_xlabel("Thời gian ghi nhận")

    # 5. Chú thích nguồn gốc dữ liệu ở chân hình
    fig.text(
        0.12,
        -0.02,
        "Nguồn: Dữ liệu Inside Airbnb Santiago (mẫu giả lập chuẩn hóa 2024–2026)",
        fontsize=9,
        color="#555555",
    )

    # 6. Lưu tệp hình ảnh và trả về đối tượng Axes
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ax_line_c1 = plot_line(thang_pro_c1, "figures/providencia_thang_c1.png")
display(
    f"Đã lưu biểu đồ: Tiêu đề = '{ax_line_c1.get_title()}', nhãn y = '{ax_line_c1.get_ylabel()}'"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

`subplots` tạo Figure chứa Axes mới, rồi `plot` dùng chỉ mục tháng làm trục ngang và số đếm làm trục dọc. Ghi nhãn đơn vị và phạm vi dữ liệu để người đọc hiểu mỗi điểm. `savefig` ghi chính Figure này, tránh lưu nhầm hình đang hoạt động khác.

#### Kết quả cách 1

| Kết quả |
| --- |
| Đã lưu biểu đồ: Tiêu đề = 'Diễn biến số lượt đánh giá theo tháng tại quận Providencia (2024–2026)', nhãn y = 'Lượt đánh giá (lượt/tháng)' |

![Diễn biến số lượt đánh giá theo tháng tại quận Providencia](img/labs/lab-12/providencia-monthly-reviews.svg)

#### Cách 2: Tối ưu hóa lưới gióng và định dạng hiển thị ngày tháng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

_dong = []

for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))

DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])


def monthly_reviews(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series:
    # 1. Trích xuất tập hợp các mã định danh thuộc quận mục tiêu
    tap_id = set(ds.loc[ds["neighbourhood"] == quan, "id"])

    # 2. Lọc các đánh giá có mã chỗ ở thuộc tập hợp trên
    rv_quan = rv[rv["listing_id"].isin(tap_id)]

    # 3. Đặt cột date làm chỉ mục và gom nhóm theo ngày cuối tháng
    thang = rv_quan.set_index("date").resample("ME").size()

    # 4. Loại bỏ tháng cuối cùng chưa trọn vẹn bằng cú pháp cắt lát
    return thang.iloc[:-1]


thang_pro_c1 = monthly_reviews(DEMO_RV, DEMO_DS, "Providencia")

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_line(thang: pd.Series, path: str):
    fig, ax = plt.subplots(figsize=(9, 3.5))

    # Vẽ đường với kiểu nét thanh thoát và điểm nút trực quan
    ax.plot(
        thang.index,
        thang.values,
        color="#0d47a1",
        linewidth=1.8,
        marker="s",
        markersize=3.5,
        label="Số lượt đánh giá",
    )

    # Tinh chỉnh định dạng trục thời gian hiển thị tháng/năm
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%m/%Y"))
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))

    ax.set_title(
        "Số lượt đánh giá theo tháng tại quận Providencia duy trì đà tăng trưởng",
        pad=12,
    )
    ax.set_ylabel("Số lượt đánh giá (lượt/tháng)")
    ax.set_xlabel("Thời gian ghi nhận")

    # Gắn chú thích nguồn ở góc trái dưới
    fig.text(
        0.12,
        -0.03,
        "Nguồn: Inside Airbnb Santiago, dữ liệu chuẩn hóa phục vụ phân tích",
        fontsize=9,
        color="#424242",
    )

    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ax_line_c2 = plot_line(thang_pro_c1, "figures/providencia_thang_c2.png")
display(f"Cách 2: Đã lưu biểu đồ với {len(ax_line_c2.lines)} đường số liệu")

# Kết thúc lời giải
```

#### Giải thích cách 2

Gom thiết lập nhãn, nguồn và lưu hình trong một hàm giúp tạo lại biểu đồ theo cùng quy tắc. `bbox_inches="tight"` thu khung theo nội dung, còn `dpi` ảnh hưởng bản raster. Tiêu đề phải được dữ liệu hỗ trợ, không dùng câu quảng cáo để làm đường biến động có vẻ mạnh hơn.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Đã lưu biểu đồ với 1 đường số liệu |

![Diễn biến số lượt đánh giá theo tháng tại quận Providencia](img/labs/lab-12/providencia-monthly-reviews.svg)
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi vẽ nhanh đồ thị đường đơn giản để khảo sát xu hướng chuỗi thời gian trong quá trình khám phá. Cách 2 cần thiết khi muốn chuẩn hóa lưới trục, nhãn ngày tháng và đóng gói hàm vẽ nhằm xuất hình ảnh sắc nét cho báo cáo.

:::

---

<span id="data-lab-12-04"></span>
### Bài tập 4: Thống kê số lượng chỗ ở và tỷ lệ loại phòng nguyên căn theo quận

::: exercise Lập bảng tỷ lệ phân loại phòng
Để so sánh cơ cấu thị trường lưu trú giữa các địa bàn, cần tính toán tỷ lệ chỗ ở thuộc loại căn hộ hoặc nhà nguyên căn (`Entire home/apt`). Các quận có quy mô quá nhỏ (quá ít chỗ ở) thường có phương sai lớn và gây nhiễu cho biểu đồ, vì vậy cần áp dụng ngưỡng lọc quy mô `min_n` và sắp xếp tỷ lệ tăng dần để sẵn sàng cho biểu đồ thanh ngang.

Hãy viết hàm `share_entire(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame` thực hiện:
1. Nhóm dữ liệu theo cột quận `neighbourhood`.
2. Tính hai chỉ số cho mỗi quận:
   - `n`: Số lượng chỗ ở thuộc quận (tương đương kích thước nhóm).
   - `pct`: Tỷ lệ chỗ ở có `room_type == "Entire home/apt"` trên thang đo từ $0{,}0$ đến $1{,}0$ (trung bình của điều kiện boolean).
3. Lọc bỏ các quận có quy mô `n < min_n`.
4. Sắp xếp các quận còn lại theo giá trị `pct` tăng dần.
5. Trả về DataFrame có chỉ mục là tên quận và đúng hai cột `["n", "pct"]`. Tuyệt đối không thêm cột phụ làm biến đổi DataFrame `ds` ban đầu.
:::

::: solution
#### Cách 1: Sử dụng groupby với hàm tổng hợp tùy biến tường minh

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

# Bắt đầu lời giải

import pandas as pd


def share_entire(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    # 1. Gom nhóm và tính toán độc lập số lượng và tỷ lệ nguyên căn
    tk = ds.groupby("neighbourhood").agg(
        n=("id", "size"),
        pct=("room_type", lambda cot: (cot == "Entire home/apt").mean()),
    )

    # 2. Lọc theo ngưỡng số lượng tối thiểu và sắp xếp tăng dần theo tỷ lệ
    tk_loc = tk.loc[tk["n"] >= min_n].sort_values("pct", ascending=True)
    return tk_loc


# Gọi thực nghiệm hàm với dữ liệu mẫu (ngưỡng min_n = 5):
tk_nguyen_can_c1 = share_entire(DEMO_DS, min_n=5)
display(tk_nguyen_can_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Nhóm theo quận rồi tính số dòng và tỷ lệ `room_type == "Entire home/apt"`. Lọc `n >= min_n` sau khi tổng hợp để ngưỡng áp dụng cho quy mô quận. Tỷ lệ ở thang 0–1, nên 0,8 tương ứng 80%, không phải 0,8%.

#### Kết quả cách 1

| neighbourhood | n | pct |
| --- | --- | --- |
| Ñuñoa | 8 | 0.5 |
| Santiago | 20 | 0.65 |
| Providencia | 12 | 0.75 |
| Las Condes | 10 | 0.8 |
| Lo Barnechea | 6 | 1 |

#### Cách 2: Sử dụng phép gán tạm thời không biến đổi dữ liệu nguồn

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

# Bắt đầu lời giải

import pandas as pd


def share_entire(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    # Sử dụng assign trên bản sao để tính toán vector hóa nhanh chóng
    tk = (
        ds.assign(la_nguyen_can=ds["room_type"] == "Entire home/apt")
        .groupby("neighbourhood")
        .agg(n=("id", "size"), pct=("la_nguyen_can", "mean"))
    )
    return tk.loc[tk["n"] >= min_n].sort_values("pct")


# Gọi thực nghiệm hàm với dữ liệu mẫu:
tk_nguyen_can_c2 = share_entire(DEMO_DS, min_n=5)
display(
    f"Cách 2: Quận dẫn đầu tỷ lệ nguyên căn là {tk_nguyen_can_c2.index[-1]} ({tk_nguyen_can_c2['pct'].max():.1%})"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Tạo cột boolean rồi dùng named aggregation giúp tên `n` và `pct` đi cùng định nghĩa của chúng. Sắp tỷ lệ tăng dần là thứ tự dữ liệu cho biểu đồ thanh ngang tiếp theo. Mẫu số cần giữ đúng số dòng trong quận, kể cả khi một kiểu phòng không xuất hiện.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Quận dẫn đầu tỷ lệ nguyên căn là Lo Barnechea (100.0%) |
#### So sánh cách dùng

Hãy chọn Cách 1 khi bạn cần viết hàm tổng hợp tùy biến để trực tiếp kiểm soát công thức tính tỷ lệ trên từng nhóm dữ liệu. Cách 2 thuận tiện hơn khi muốn dùng named aggregation để đặt tên cột rõ ràng và sắp xếp sẵn thứ tự cho biểu đồ thanh.

:::

---

<span id="data-lab-12-05"></span>
### Bài tập 5: Dựng biểu đồ thanh ngang có nhãn tỷ lệ phần trăm và gốc tọa độ chuẩn

::: exercise Dựng biểu đồ thanh ngang chuẩn mực
Biểu đồ thanh ngang cho phép giữ tên quận dễ đọc. Trong bài này, trục bắt đầu từ 0 và mỗi thanh có nhãn giá trị để đối chiếu trực tiếp với bảng.

Hãy viết hàm `plot_share_barh(tk: pd.DataFrame, path: str) -> matplotlib.axes.Axes` thực hiện:
1. Nhận bảng thống kê `tk` từ Bài tập 4 và đường dẫn tệp lưu trữ `path`.
2. Khởi tạo khung hình `fig, ax = plt.subplots(figsize=(7, 4))`.
3. Vẽ các thanh ngang bằng `ax.barh` theo đúng thứ tự dòng của `tk`, với chiều dài thanh là `pct * 100` (thang phần trăm %).
4. Gắn nhãn giá trị trực tiếp trên mỗi thanh bằng phương thức `ax.bar_label(..., fmt="%.0f%%")`.
5. Thiết lập trục hoành bắt buộc bắt đầu từ 0 (`ax.set_xlim(left=0)`), nhãn trục hoành có đơn vị `%`.
6. Tiêu đề nêu thông điệp phân tích rõ ràng (độ dài tối thiểu 15 ký tự).
7. Lưu tệp hình ảnh vào `path` và trả về đối tượng `ax`.
:::

::: solution
#### Cách 1: Sử dụng barh cơ bản và bar_label tự động

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)


def share_entire(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    # 1. Gom nhóm và tính toán độc lập số lượng và tỷ lệ nguyên căn
    tk = ds.groupby("neighbourhood").agg(
        n=("id", "size"),
        pct=("room_type", lambda cot: (cot == "Entire home/apt").mean()),
    )

    # 2. Lọc theo ngưỡng số lượng tối thiểu và sắp xếp tăng dần theo tỷ lệ
    tk_loc = tk.loc[tk["n"] >= min_n].sort_values("pct", ascending=True)
    return tk_loc


tk_nguyen_can_c1 = share_entire(DEMO_DS, min_n=5)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import matplotlib.pyplot as plt


def plot_share_barh(tk: pd.DataFrame, path: str):
    # 1. Khởi tạo khung hình
    fig, ax = plt.subplots(figsize=(7, 4))

    # 2. Vẽ thanh ngang với độ dài thang đo phần trăm
    thanh = ax.barh(tk.index, tk["pct"] * 100, color="#2b5c8f", height=0.65)

    # 3. Gắn nhãn giá trị trực tiếp trên từng thanh
    ax.bar_label(thanh, fmt="%.0f%%", padding=4, fontsize=10)

    # 4. Bắt buộc trục hoành xuất phát từ 0 và mở rộng khoảng đệm bên phải
    ax.set_xlim(left=0, right=115)
    ax.set_xlabel("Tỷ lệ phòng nguyên căn (%)")

    # 5. Tiêu đề phản ánh thông điệp phân tích
    ax.set_title("Tỷ lệ phòng nguyên căn tại các quận có từ 5 chỗ ở trở lên", pad=12)

    # 6. Lưu tệp hình ảnh
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ax_barh_c1 = plot_share_barh(tk_nguyen_can_c1, "figures/pct_nguyen_can_c1.png")
display(
    f"Đã lưu biểu đồ thanh ngang: Số thanh = {len(ax_barh_c1.patches)}, giới hạn trục x = {ax_barh_c1.get_xlim()}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

`barh` tạo một thanh cho mỗi quận theo thứ tự bảng. Nhân tỷ lệ với 100 trước khi gắn nhãn phần trăm. Trục phải bắt đầu từ 0 để độ dài thanh phản ánh tỷ lệ, còn nhãn giá trị cho phép đọc con số mà không cần đo bằng mắt.

#### Kết quả cách 1

| Kết quả |
| --- |
| Đã lưu biểu đồ thanh ngang: Số thanh = 5, giới hạn trục x = (np.float64(0.0), np.float64(115.0)) |

![Tỷ lệ phòng nguyên căn tại các quận có từ 5 chỗ ở trở lên](img/labs/lab-12/entire-home-share-barh.svg)

#### Cách 2: Tùy biến màu sắc phân cấp và định dạng lề nhãn chữ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)


def share_entire(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    # 1. Gom nhóm và tính toán độc lập số lượng và tỷ lệ nguyên căn
    tk = ds.groupby("neighbourhood").agg(
        n=("id", "size"),
        pct=("room_type", lambda cot: (cot == "Entire home/apt").mean()),
    )

    # 2. Lọc theo ngưỡng số lượng tối thiểu và sắp xếp tăng dần theo tỷ lệ
    tk_loc = tk.loc[tk["n"] >= min_n].sort_values("pct", ascending=True)
    return tk_loc


tk_nguyen_can_c1 = share_entire(DEMO_DS, min_n=5)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import matplotlib.pyplot as plt


def plot_share_barh(tk: pd.DataFrame, path: str):
    fig, ax = plt.subplots(figsize=(7, 4))

    # Phân cấp màu sắc nổi bật cho quận có tỷ lệ cao nhất
    mau_sac = ["#4a7bb0" if p < tk["pct"].max() else "#1a4971" for p in tk["pct"]]
    thanh = ax.barh(tk.index, tk["pct"] * 100, color=mau_sac, height=0.6)

    ax.bar_label(thanh, fmt="%.1f%%", padding=5, color="#111111", weight="bold")
    ax.set_xlim(0, 115)
    ax.set_xlabel("Tỷ lệ phòng nguyên căn (%)")
    ax.set_title("Cơ cấu loại phòng nguyên căn phân hóa mạnh giữa các địa bàn", pad=12)

    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ax_barh_c2 = plot_share_barh(tk_nguyen_can_c1, "figures/pct_nguyen_can_c2.png")
display(f"Cách 2: Đã lưu biểu đồ với {len(ax_barh_c2.texts)} nhãn giá trị số liệu")

# Kết thúc lời giải
```

#### Giải thích cách 2

Thiết lập nhãn và lưu hình trong cùng hàm giữ biểu đồ tái lập. `bar_label` đặt chuỗi lên từng thanh theo đúng container trả về. Nếu nhãn sát mép, mở thêm khoảng trống trong giới hạn trục thay vì cắt chữ hoặc giảm tỷ lệ chữ quá nhỏ.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Đã lưu biểu đồ với 5 nhãn giá trị số liệu |

![Tỷ lệ phòng nguyên căn tại các quận có từ 5 chỗ ở trở lên](img/labs/lab-12/entire-home-share-barh.svg)
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi muốn tạo nhanh biểu đồ thanh ngang với thang đo bắt đầu từ 0 để so sánh trung thực các nhóm. Cách 2 thích hợp khi cần trau chuốt đồ thị để xuất bản, phân tầng màu sắc nhấn mạnh và căn chỉnh lề để nhãn không bị tràn.

:::

---

<span id="data-lab-12-06"></span>
### Bài tập 6: Dựng biểu đồ tần suất số ngày mở lịch và trích xuất hai nhóm hành vi

::: exercise Dựng histogram và nhận diện phân phối hai đỉnh
Chỉ số `availability_365` đại diện cho số ngày một chỗ ở mở lịch cho phép đặt phòng trong vòng 365 ngày tới. Phân phối của biến số này thường có dạng hai đỉnh (bimodal) rất đặc thù, tập trung dày đặc ở hai cực: Các chỗ ở khóa lịch hoàn toàn (0 ngày) và các chỗ ở mở lịch gần như quanh năm ($\ge 360$ ngày). Cần sử dụng biểu đồ tần suất (histogram) với số lượng khoảng chia xác định để làm nổi bật hiện tượng này, đồng thời trích xuất định lượng số lượng của hai nhóm hành vi.

Hãy viết hàm `plot_availability(avail: pd.Series, path: str, bins: int = 40) -> dict` thực hiện:
1. Loại bỏ các giá trị khuyết (`NaN`) trong Series `avail`.
2. Khởi tạo khung hình và vẽ biểu đồ tần suất bằng `ax.hist(..., bins=bins)`.
3. Đặt tiêu đề nêu rõ hiện tượng phân cực quan sát được (độ dài tối thiểu 15 ký tự).
4. Lưu tệp hình ảnh vào đường dẫn `path`.
5. Đếm số lượng chỗ ở có đúng 0 ngày mở lịch (`so_khoa`) và số lượng chỗ ở có từ 360 ngày mở lịch trở lên (`so_mo_quanh_nam`).
6. Trả về từ điển gồm đúng ba khóa: `"ax"` (đối tượng Axes), `"so_khoa"` (kiểu số nguyên int), và `"so_mo_quanh_nam"` (kiểu số nguyên int).
:::

::: solution
#### Cách 1: Sử dụng dropna và đếm bằng phép so sánh boolean trực tiếp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import pandas as pd
import matplotlib.pyplot as plt


def plot_availability(avail: pd.Series, path: str, bins: int = 40) -> dict:
    # 1. Loại bỏ ô khuyết để tránh cảnh báo phân tích
    du_lieu = avail.dropna()

    # 2. Khởi tạo khung hình và vẽ biểu đồ tần suất
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.hist(du_lieu, bins=bins, color="#0288d1", edgecolor="white", linewidth=0.5)

    # 3. Đặt tiêu đề và các nhãn trục
    ax.set_title(
        "Phân phối số ngày mở lịch trong năm tới: Tập trung tại hai cực", pad=12
    )
    ax.set_xlabel("Số ngày mở lịch trong năm (ngày)")
    ax.set_ylabel("Số lượng chỗ ở")

    # 4. Lưu tệp hình ảnh
    fig.savefig(path, dpi=150, bbox_inches="tight")

    # 5. Đếm số lượng hai nhóm hành vi đặc thù
    so_khoa = int((du_lieu == 0).sum())
    so_mo_quanh_nam = int((du_lieu >= 360).sum())

    return {
        "ax": ax,
        "so_khoa": so_khoa,
        "so_mo_quanh_nam": so_mo_quanh_nam,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_hist_c1 = plot_availability(
    DEMO_DS["availability_365"], "figures/availability_hist_c1.png", bins=40
)
display(
    f"Kết quả: {kq_hist_c1['so_khoa']} chỗ ở khóa lịch, {kq_hist_c1['so_mo_quanh_nam']} chỗ ở mở gần quanh năm"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Bỏ ô thiếu trước khi đưa `availability_365` vào histogram. `bins` quyết định cách chia khoảng, còn tổng tần suất phải bằng số giá trị hợp lệ. Đếm riêng giá trị 0 và từ 360 trở lên theo đúng cận của đề.

#### Kết quả cách 1

| Kết quả |
| --- |
| Kết quả: 7 chỗ ở khóa lịch, 13 chỗ ở mở gần quanh năm |

![Phân phối số ngày mở lịch trong năm tới](img/labs/lab-12/availability-365-hist.svg)

#### Cách 2: Xác định ranh giới khoảng chia tường minh bằng NumPy

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_availability(avail: pd.Series, path: str, bins: int = 40) -> dict:
    mang_du_lieu = avail.dropna().to_numpy()

    fig, ax = plt.subplots(figsize=(8, 3.5))
    # Tạo lưới ranh giới khoảng chia đều từ 0 đến 365
    ranh_gioi_bin = np.linspace(0, 365, bins + 1)
    ax.hist(
        mang_du_lieu,
        bins=ranh_gioi_bin,
        color="#0097a7",
        edgecolor="#ffffff",
        linewidth=0.5,
    )

    ax.set_title(
        "Phân phối hai đỉnh của số ngày mở lịch phản ánh hai nhóm vận hành", pad=12
    )
    ax.set_xlabel("Số ngày mở lịch trong năm (ngày)")
    ax.set_ylabel("Số lượng chỗ ở")

    fig.savefig(path, dpi=150, bbox_inches="tight")

    # Đếm nhanh bằng np.count_nonzero
    so_khoa = int(np.count_nonzero(mang_du_lieu == 0))
    so_mo_quanh_nam = int(np.count_nonzero(mang_du_lieu >= 360))

    return {
        "ax": ax,
        "so_khoa": so_khoa,
        "so_mo_quanh_nam": so_mo_quanh_nam,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_hist_c2 = plot_availability(
    DEMO_DS["availability_365"], "figures/availability_hist_c2.png", bins=40
)
display(f"Cách 2: Số thanh trên biểu đồ = {len(kq_hist_c2['ax'].patches)}")

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm trả cả Axes và hai số đếm giúp kiểm đối chiếu hình với bảng. Hai cụm trong histogram mô tả phân bố số ngày mở lịch của dữ liệu, không tự cho biết ý định chủ nhà hoặc số ngày thực sự có khách. Phải xem cả lựa chọn khoảng chia trước khi kết luận hình có hai đỉnh.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Số thanh trên biểu đồ = 40 |

![Phân phối số ngày mở lịch trong năm tới](img/labs/lab-12/availability-365-hist.svg)
#### So sánh cách dùng

Cách 1 thuận tiện để dựng histogram và kiểm tổng tần suất trên số quan sát hợp lệ. Cách 2 trả thêm số đếm tại hai vùng biên cùng đối tượng Axes để đối chiếu bảng với hình. Cách chia khoảng vẫn phải được giữ rõ trong báo cáo.

:::

---

<span id="data-lab-12-07"></span>
### Bài tập 7: Phân tích phân phối hai đỉnh và rủi ro khi chỉ dựa vào số bình quân

::: exercise Phân tích bản chất phân phối hai đỉnh
Khi dữ liệu có phân phối hai đỉnh (bimodal distribution), các số đo tóm tắt truyền thống như giá trị trung bình cộng (`mean`) hoặc trung vị (`median`) thường rơi vào khoảng giữa, nơi hầu như không có quan sát thực tế nào tồn tại. Hơn nữa, việc hiểu sai bản chất của `availability_365` có thể dẫn đến những kết luận sai lệch về thị trường.

Hãy viết hàm `analyze_bimodal_distribution(avail: pd.Series) -> dict` tính toán các chỉ số phân tích định lượng:
1. Giá trị trung bình (`mean`) và trung vị (`median`) của chuỗi dữ liệu.
2. Tỷ lệ phần trăm chỗ ở thuộc nhóm khóa lịch hoàn toàn ($= 0$ ngày).
3. Tỷ lệ phần trăm chỗ ở thuộc nhóm mở lịch quanh năm ($\ge 360$ ngày).
4. Tỷ lệ phần trăm chỗ ở nằm ở khoảng giữa ($0 < \text{availability} < 360$).
5. Giải thích bản chất vì sao không thể suy diễn tỷ lệ lấp đầy phòng hoặc hành vi đặt phòng của khách chỉ dựa trên chỉ số `availability_365`.
:::

::: solution
#### Cách 1: Sử dụng các phương thức thống kê mô tả cơ bản của pandas

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

# Bắt đầu lời giải

import pandas as pd


def analyze_bimodal_distribution(avail: pd.Series) -> dict:
    s = avail.dropna()
    n = len(s)

    # 1. Tính toán số đo trung tâm
    trung_binh = float(s.mean())
    trung_vi = float(s.median())

    # 2. Phân tách ba phân khúc hành vi
    so_khoa = int((s == 0).sum())
    so_mo_quanh_nam = int((s >= 360).sum())
    so_giua = int(((s > 0) & (s < 360)).sum())

    return {
        "mean": round(trung_binh, 2),
        "median": round(trung_vi, 2),
        "pct_khoa": round(so_khoa / n * 100, 2),
        "pct_mo_quanh_nam": round(so_mo_quanh_nam / n * 100, 2),
        "pct_giua": round(so_giua / n * 100, 2),
        "so_khoa": so_khoa,
        "so_mo_quanh_nam": so_mo_quanh_nam,
        "so_giua": so_giua,
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_bimodal_c1 = analyze_bimodal_distribution(DEMO_DS["availability_365"])
display(kq_bimodal_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Chia các giá trị theo điều kiện mở lịch đã nêu rồi đếm từng nhóm. Giữ số ô thiếu riêng để người đọc biết phần dữ liệu chưa vào phép tính. Những khoảng chọn để tóm tắt cần được ghi rõ, không được đổi ngưỡng cho phù hợp một câu chuyện có sẵn.

#### Kết quả cách 1

| Trường | Kết quả |
| --- | --- |
| mean | 180.57 |
| median | 191 |
| pct_khoa | 11.67 |
| pct_mo_quanh_nam | 21.67 |
| pct_giua | 66.67 |
| so_khoa | 7 |
| so_mo_quanh_nam | 13 |
| so_giua | 40 |

#### Cách 2: Sử dụng phân khoảng pd.cut để tổng hợp tần suất nhóm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

# Bắt đầu lời giải

import pandas as pd


def analyze_bimodal_distribution(avail: pd.Series) -> dict:
    s = avail.dropna()
    n = len(s)

    # Phân nhóm bằng các mốc biên xác định
    nhom = pd.cut(s, bins=[-1, 0, 359, 365], labels=["khoa", "giua", "mo_quanh_nam"])
    dem = nhom.value_counts()

    return {
        "mean": round(float(s.mean()), 2),
        "median": round(float(s.median()), 2),
        "pct_khoa": round(dem["khoa"] / n * 100, 2),
        "pct_mo_quanh_nam": round(dem["mo_quanh_nam"] / n * 100, 2),
        "pct_giua": round(dem["giua"] / n * 100, 2),
        "so_khoa": int(dem["khoa"]),
        "so_mo_quanh_nam": int(dem["mo_quanh_nam"]),
        "so_giua": int(dem["giua"]),
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_bimodal_c2 = analyze_bimodal_distribution(DEMO_DS["availability_365"])
display(
    f"Cách 2: Tỷ lệ hai cực = {kq_bimodal_c2['pct_khoa']}% khóa lịch và {kq_bimodal_c2['pct_mo_quanh_nam']}% mở quanh năm"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Các mặt nạ theo cột giúp kiểm lại từng cận dưới và cận trên. Báo số lượng và tỷ trọng với cùng mẫu số thay vì chỉ gọi một nhóm là áp đảo. Lịch đóng có thể do đã đặt, chủ nhà khóa ngày hoặc thiếu cập nhật, nên không đồng nhất với công suất phòng.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Tỷ lệ hai cực = 11.67% khóa lịch và 21.67% mở quanh năm |
#### So sánh cách dùng

Cách 1 mở từng điều kiện chia nhóm và giữ số ô thiếu riêng. Cách 2 trình bày các nhóm bằng mặt nạ cột để đối chiếu số lượng với tỷ trọng. Khi chọn cách làm, cần giữ nguyên các cận và mẫu số, không đổi ngưỡng giữa hai lời giải.

:::

---

<span id="data-lab-12-08"></span>
### Bài tập 8: Nhận diện biểu đồ gây hiểu sai và đo lường hệ số phóng đại thị giác

::: exercise Đo lường sự sai lệch khi cắt ngắn trục tung
Một thủ thuật trình bày trực quan thường bị lạm dụng trong các báo cáo thiếu trung thực là cắt ngắn trục tung (truncated vertical axis). Bằng cách thiết lập giới hạn dưới của trục $y$ sát với giá trị nhỏ nhất của dữ liệu thay vì bắt đầu từ 0, chênh lệch thực tế nhỏ sẽ bị khuếch đại lên gấp nhiều lần, khiến mắt người đọc có cảm giác về một khoảng cách khổng lồ.

Hãy viết hàm `visual_distortion_factor(data: pd.Series, y_min: float, y_max: float) -> dict` tính toán: Đặt $R_1$ là tỷ số giá trị và $R_2$ là tỷ số chiều cao hiển thị.
1. Tỷ số giá trị thực tế giữa nhóm cao nhất và nhóm thấp nhất:
$$
R_1 = \frac{v_{\max}}{v_{\min}}
$$
2. Chiều cao thị giác hiển thị của cột trên biểu đồ:
$$
h = v - y_{\min}
$$
3. Tỷ số chiều cao trực quan trên biểu đồ:
$$
R_2 = \frac{v_{\max} - y_{\min}}{v_{\min} - y_{\min}}
$$
4. Hệ số phóng đại sai lệch thị giác (Visual Distortion Factor):
$$
D = \frac{R_2}{R_1}
$$
5. Thử nghiệm với chuỗi tỷ lệ ba quận `Santiago` ($65\%$), `Providencia` ($75\%$), `Las Condes` ($80\%$) khi bị cắt ngắn với $y_{\min} = 60\%$ và $y_{\max} = 85\%$.
:::

::: solution
#### Cách 1: Tính toán tuần tự từ giá trị cực đại và cực tiểu của Series

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

# Bắt đầu lời giải

import pandas as pd


def visual_distortion_factor(data: pd.Series, y_min: float, y_max: float) -> dict:
    v_min = float(data.min())
    v_max = float(data.max())

    # 1. Tính tỷ số thực tế giữa giá trị cao nhất và thấp nhất
    r_thuc = v_max / v_min

    # 2. Tính chiều cao trực quan của hai cột trên khung vẽ
    h_min = v_min - y_min
    h_max = v_max - y_min

    # 3. Tính tỷ số thị giác và hệ số phóng đại
    r_thi_giac = h_max / h_min
    he_so = r_thi_giac / r_thuc

    return {
        "v_min": v_min,
        "v_max": v_max,
        "r_thuc": round(r_thuc, 3),
        "r_thi_giac": round(r_thi_giac, 3),
        "he_so": round(he_so, 3),
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
dulieu_sosanh = pd.Series(
    [65.0, 75.0, 80.0], index=["Santiago", "Providencia", "Las Condes"]
)
kq_dist_c1 = visual_distortion_factor(dulieu_sosanh, y_min=60.0, y_max=85.0)
display(kq_dist_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Tính phần trục còn lại sau khi cắt và so với toàn thang đo. Một chênh lệch số học giữ nguyên có thể chiếm tỷ lệ chiều cao lớn hơn trên hình bị cắt. Cần nêu cả giới hạn trục và giá trị dữ liệu để người đọc đối chiếu được.

#### Kết quả cách 1

| Trường | Kết quả |
| --- | --- |
| v_min | 65 |
| v_max | 80 |
| r_thuc | 1.231 |
| r_thi_giac | 4 |
| he_so | 3.25 |

![Biểu đồ cột bị cắt ngắn trục tung gây hiểu sai](img/labs/lab-12/misleading-truncated-bar.svg)

#### Cách 2: Đóng gói công thức vector hóa an toàn kiểm tra điều kiện biên

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

dulieu_sosanh = pd.Series(
    [65.0, 75.0, 80.0], index=["Santiago", "Providencia", "Las Condes"]
)

# Bắt đầu lời giải

import pandas as pd


def visual_distortion_factor(data: pd.Series, y_min: float, y_max: float) -> dict:
    vals = data.to_numpy()
    v_min, v_max = float(vals.min()), float(vals.max())

    # Kiểm tra tính hợp lệ của biên cắt trục tung
    if y_min >= v_min:
        raise ValueError(
            "Giới hạn dưới y_min phải nhỏ hơn giá trị nhỏ nhất của dữ liệu."
        )

    r_thuc = v_max / v_min
    r_thi_giac = (v_max - y_min) / (v_min - y_min)
    he_so = r_thi_giac / r_thuc

    return {
        "v_min": v_min,
        "v_max": v_max,
        "r_thuc": round(r_thuc, 3),
        "r_thi_giac": round(r_thi_giac, 3),
        "he_so": round(he_so, 3),
    }


# Gọi thực nghiệm hàm với dữ liệu mẫu:
kq_dist_c2 = visual_distortion_factor(dulieu_sosanh, y_min=60.0, y_max=85.0)
display(f"Cách 2: Hệ số phóng đại thị giác = {kq_dist_c2['he_so']} lần")

# Kết thúc lời giải
```

#### Giải thích cách 2

Đóng phép tính vào hàm giúp thử các mốc cắt khác nhau mà giữ dữ liệu. Kiểm giới hạn trục hợp lệ trước khi chia. Hệ số phóng đại hình ảnh mô tả cách trình bày, không phải mức tăng tương đối thật giữa hai nhóm.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Hệ số phóng đại thị giác = 3.25 lần |

![Biểu đồ cột bị cắt ngắn trục tung gây hiểu sai](img/labs/lab-12/misleading-truncated-bar.svg)
#### So sánh cách dùng

Hãy chọn Cách 1 khi muốn minh họa từng bước cơ chế bóp méo thị giác do cắt trục tung trên một ví dụ cụ thể để giảng giải. Cách 2 phù hợp khi cần xây dựng hàm kiểm định tự động có kiểm tra điều kiện biên cho nhiều bộ số liệu.

:::

---

<span id="data-lab-12-09"></span>
### Bài tập 9: Sửa biểu đồ cột thành biểu đồ trung thực có gốc tọa độ chuẩn

::: exercise Vẽ lại biểu đồ trung thực
Để khôi phục tính trung thực khoa học của số liệu, biểu đồ cột so sánh giữa các quận phải được vẽ lại với trục tung xuất phát từ đúng gốc tọa độ 0. Tiêu đề biểu đồ cũng cần được viết lại bằng văn phong khách quan, trung thực, phản ánh đúng tương quan giữa các địa bàn mà không dùng các từ ngữ giật gân, định kiến.

Hãy viết hàm `plot_honest_bars(pct: pd.Series, path: str) -> matplotlib.axes.Axes` thực hiện:
1. Nhận Series tỷ lệ % `pct` (chỉ mục là tên quận) và đường dẫn tệp `path`.
2. Khởi tạo khung hình `fig, ax = plt.subplots(figsize=(6, 3.5))`.
3. Vẽ biểu đồ cột đứng `ax.bar` cho từng quận theo đúng thứ tự của `pct`.
4. Bắt buộc thiết lập trục tung bắt đầu từ gốc 0 (`ax.set_ylim(bottom=0)`).
5. Đặt tiêu đề phản ánh đúng mức độ chênh lệch thực tế (độ dài tối thiểu 15 ký tự).
6. Lưu tệp hình ảnh vào `path` và trả về đối tượng `ax`.
7. Thảo luận các trường hợp ngoại lệ hiếm hoi được phép không bắt đầu trục từ 0.
:::

::: solution
#### Cách 1: Thiết lập trục tung bắt đầu từ 0 và tiêu đề khách quan

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

dulieu_sosanh = pd.Series(
    [65.0, 75.0, 80.0], index=["Santiago", "Providencia", "Las Condes"]
)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import matplotlib.pyplot as plt


def plot_honest_bars(pct: pd.Series, path: str):
    # 1. Khởi tạo khung hình
    fig, ax = plt.subplots(figsize=(6, 3.5))

    # 2. Vẽ các cột đứng
    thanh = ax.bar(pct.index, pct.values, color="#388e3c", width=0.55)

    # 3. Gắn nhãn giá trị trên đầu cột
    ax.bar_label(thanh, fmt="%.0f%%", padding=3, fontsize=10)

    # 4. Trục tung bắt buộc bắt đầu từ 0
    ax.set_ylim(bottom=0, top=100)
    ax.set_ylabel("Tỷ lệ nguyên căn (%)")

    # 5. Tiêu đề phản ánh tương quan khách quan
    ax.set_title(
        "Trục tung xuất phát từ 0: Phản ánh trung thực tương quan tỷ lệ", pad=12
    )

    # 6. Lưu tệp hình ảnh
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ax_honest_c1 = plot_honest_bars(dulieu_sosanh, "figures/honest_bars_c1.png")
display(
    f"Đã lưu biểu đồ trung thực: Giới hạn trục y = {ax_honest_c1.get_ylim()}, số cột = {len(ax_honest_c1.patches)}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Vẽ lại cùng giá trị và cùng thứ tự nhóm trên trục bắt đầu từ 0. Giữ nhãn phần trăm hoặc đơn vị ban đầu để việc so sánh không đổi đại lượng. Hình sửa cần cho thấy chênh lệch thật mà không thêm kết luận về nguyên nhân.

#### Kết quả cách 1

| Kết quả |
| --- |
| Đã lưu biểu đồ trung thực: Giới hạn trục y = (np.float64(0.0), np.float64(100.0)), số cột = 3 |

![Biểu đồ cột trung thực có trục tung xuất phát từ gốc 0](img/labs/lab-12/honest-zero-baseline-bar.svg)

#### Cách 2: Tùy biến giới hạn trên trục tung theo tỷ lệ 100% kèm nhãn số

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

dulieu_sosanh = pd.Series(
    [65.0, 75.0, 80.0], index=["Santiago", "Providencia", "Las Condes"]
)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import matplotlib.pyplot as plt


def plot_honest_bars(pct: pd.Series, path: str):
    fig, ax = plt.subplots(figsize=(6, 3.5))

    cot = ax.bar(
        pct.index,
        pct.values,
        color="#2e7d32",
        width=0.5,
        edgecolor="#1b5e20",
        linewidth=0.8,
    )
    ax.bar_label(cot, fmt="%.1f%%", padding=4, weight="bold")

    # Thiết lập thang đo đầy đủ 0-100% của đại lượng tỷ lệ
    ax.set_ylim(0, 105)
    ax.set_ylabel("Tỷ lệ phòng nguyên căn (%)")
    ax.set_title(
        "Tỷ lệ phòng nguyên căn giữa các quận có sự tương đồng đáng kể", pad=12
    )

    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax


# Gọi thực nghiệm hàm với dữ liệu mẫu:
ax_honest_c2 = plot_honest_bars(dulieu_sosanh, "figures/honest_bars_c2.png")
display(f"Cách 2: Đã lưu biểu đồ với tiêu đề: '{ax_honest_c2.get_title()}'")

# Kết thúc lời giải
```

#### Giải thích cách 2

Tạo Figure mới rồi đặt giới hạn, nhãn và lưu tệp trong hàm giúp tránh phụ thuộc hình đã vẽ trước. So sánh chiều cao cột với Series đầu vào bằng mã. Không chỉ kiểm rằng có ảnh được xuất ra, vì một ảnh lưu thành công vẫn có thể dùng sai dữ liệu hoặc sai thang đo.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Đã lưu biểu đồ với tiêu đề: 'Tỷ lệ phòng nguyên căn giữa các quận có sự tương đồng đáng kể' |

![Biểu đồ cột trung thực có trục tung xuất phát từ gốc 0](img/labs/lab-12/honest-zero-baseline-bar.svg)
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi cần sửa nhanh biểu đồ thanh về gốc 0 để loại bỏ ấn tượng sai lệch cho người xem. Cách 2 phù hợp khi đại lượng là tỷ lệ phần trăm cần thang chuẩn 100% và đòi hỏi nhãn số chi tiết để kiểm chứng dữ liệu.

:::

---

<span id="data-lab-12-10"></span>
### Bài tập 10: Tự động hóa kiểm tra cấu trúc biểu đồ bằng hệ thống khẳng định

::: exercise Kiểm định chất lượng biểu đồ tự động
Trong quy trình kỹ thuật dữ liệu tự động (CI/CD visual pipeline), ta không thể dùng mắt người để duyệt qua hàng trăm hình ảnh được sinh ra mỗi ngày. Cần xây dựng một hàm kiểm định chất lượng biểu đồ bằng mã nguồn (visual quality assurance) dựa trên các thuộc tính của đối tượng `matplotlib.axes.Axes` và hệ thống tệp lưu trữ.

Hãy viết hàm `validate_chart_structure(ax: matplotlib.axes.Axes, min_title_len: int = 15, require_ylabel: bool = False, require_xlabel: bool = False, require_zero_x: bool = False, require_zero_y: bool = False, min_patches: int = 0, min_lines: int = 0, saved_path: str = None) -> dict` thực hiện:
1. Kiểm tra tiêu đề tồn tại và có độ dài tối thiểu `min_title_len`.
2. Kiểm tra nhãn trục tung (`ylabel`) và nhãn trục hoành (`xlabel`) không được rỗng nếu có yêu cầu.
3. Kiểm tra gốc tọa độ trục hoành `ax.get_xlim()[0] == 0` (đối với biểu đồ thanh ngang) hoặc trục tung `ax.get_ylim()[0] == 0` (đối với biểu đồ cột đứng).
4. Kiểm tra số lượng đối tượng hình học: Số lượng thanh `len(ax.patches) >= min_patches` và số lượng đường `len(ax.lines) >= min_lines`.
5. Kiểm tra tệp hình ảnh tại đường dẫn `saved_path` đã được tạo thành công trên đĩa và có dung lượng lớn hơn 0 byte.
6. Trả về từ điển trạng thái chi tiết của từng tiêu chí và cờ tổng hợp `all_passed: bool`.
:::

::: solution
#### Cách 1: Kiểm tra tuần tự từng tiêu chí bằng toán tử logic

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

import matplotlib.pyplot as plt

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)


def share_entire(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    # 1. Gom nhóm và tính toán độc lập số lượng và tỷ lệ nguyên căn
    tk = ds.groupby("neighbourhood").agg(
        n=("id", "size"),
        pct=("room_type", lambda cot: (cot == "Entire home/apt").mean()),
    )

    # 2. Lọc theo ngưỡng số lượng tối thiểu và sắp xếp tăng dần theo tỷ lệ
    tk_loc = tk.loc[tk["n"] >= min_n].sort_values("pct", ascending=True)
    return tk_loc


tk_nguyen_can_c1 = share_entire(DEMO_DS, min_n=5)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)


def plot_share_barh(tk: pd.DataFrame, path: str):
    # 1. Khởi tạo khung hình
    fig, ax = plt.subplots(figsize=(7, 4))

    # 2. Vẽ thanh ngang với độ dài thang đo phần trăm
    thanh = ax.barh(tk.index, tk["pct"] * 100, color="#2b5c8f", height=0.65)

    # 3. Gắn nhãn giá trị trực tiếp trên từng thanh
    ax.bar_label(thanh, fmt="%.0f%%", padding=4, fontsize=10)

    # 4. Bắt buộc trục hoành xuất phát từ 0 và mở rộng khoảng đệm bên phải
    ax.set_xlim(left=0, right=115)
    ax.set_xlabel("Tỷ lệ phòng nguyên căn (%)")

    # 5. Tiêu đề phản ánh thông điệp phân tích
    ax.set_title("Tỷ lệ phòng nguyên căn tại các quận có từ 5 chỗ ở trở lên", pad=12)

    # 6. Lưu tệp hình ảnh
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax


ax_barh_c1 = plot_share_barh(tk_nguyen_can_c1, "figures/share-reference.png")

# Bắt đầu lời giải

from pathlib import Path
import matplotlib.axes


def validate_chart_structure(
    ax: matplotlib.axes.Axes,
    min_title_len: int = 15,
    require_ylabel: bool = False,
    require_xlabel: bool = False,
    require_zero_x: bool = False,
    require_zero_y: bool = False,
    min_patches: int = 0,
    min_lines: int = 0,
    saved_path: str = None,
) -> dict:
    # 1. Kiểm tra độ dài tiêu đề
    tieu_de = ax.get_title().strip()
    dat_tieu_de = len(tieu_de) >= min_title_len

    # 2. Kiểm tra nhãn các trục tọa độ
    dat_nhan_y = not require_ylabel or bool(ax.get_ylabel().strip())
    dat_nhan_x = not require_xlabel or bool(ax.get_xlabel().strip())

    # 3. Kiểm tra gốc tọa độ bắt đầu từ 0
    dat_goc_x = not require_zero_x or (ax.get_xlim()[0] == 0)
    dat_goc_y = not require_zero_y or (ax.get_ylim()[0] == 0)

    # 4. Kiểm tra số lượng đối tượng hình học trên đồ thị
    dat_patches = len(ax.patches) >= min_patches
    dat_lines = len(ax.lines) >= min_lines

    # 5. Kiểm tra tệp hình ảnh đã được ghi xuống đĩa
    dat_tep = True
    if saved_path:
        tep = Path(saved_path)
        dat_tep = tep.exists() and tep.stat().st_size > 0

    tat_ca_dat = all(
        [
            dat_tieu_de,
            dat_nhan_y,
            dat_nhan_x,
            dat_goc_x,
            dat_goc_y,
            dat_patches,
            dat_lines,
            dat_tep,
        ]
    )

    return {
        "has_title": dat_tieu_de,
        "has_ylabel": dat_nhan_y,
        "has_xlabel": dat_nhan_x,
        "has_zero_x": dat_goc_x,
        "has_zero_y": dat_goc_y,
        "has_patches": dat_patches,
        "has_lines": dat_lines,
        "has_file": dat_tep,
        "all_passed": tat_ca_dat,
    }


# Gọi thực nghiệm hàm kiểm tra biểu đồ thanh ngang Bài 5:
kiem_tra_c1 = validate_chart_structure(
    ax_barh_c1,
    min_title_len=15,
    require_xlabel=True,
    require_zero_x=True,
    min_patches=5,
    saved_path="figures/pct_nguyen_can_c1.png",
)
display(kiem_tra_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Đọc lại cấu trúc Axes để kiểm tiêu đề, nhãn, số đường hoặc thanh và giới hạn trục. Các `assert` kiểm những điều quan sát được trong hình, như số điểm và giá trị đã vẽ. Chúng không đánh giá thay người đọc về sự đúng mức của thông điệp.

#### Kết quả cách 1

| Trường | Kết quả |
| --- | --- |
| has_title | True |
| has_ylabel | True |
| has_xlabel | True |
| has_zero_x | True |
| has_zero_y | True |
| has_patches | True |
| has_lines | True |
| has_file | True |

#### Cách 2: Xây dựng bộ quy tắc kiểm định mở rộng theo dạng từ điển kiểm tra

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

import matplotlib.pyplot as plt

dulieu_sosanh = pd.Series(
    [65.0, 75.0, 80.0], index=["Santiago", "Providencia", "Las Condes"]
)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)


def plot_honest_bars(pct: pd.Series, path: str):
    # 1. Khởi tạo khung hình
    fig, ax = plt.subplots(figsize=(6, 3.5))

    # 2. Vẽ các cột đứng
    thanh = ax.bar(pct.index, pct.values, color="#388e3c", width=0.55)

    # 3. Gắn nhãn giá trị trên đầu cột
    ax.bar_label(thanh, fmt="%.0f%%", padding=3, fontsize=10)

    # 4. Trục tung bắt buộc bắt đầu từ 0
    ax.set_ylim(bottom=0, top=100)
    ax.set_ylabel("Tỷ lệ nguyên căn (%)")

    # 5. Tiêu đề phản ánh tương quan khách quan
    ax.set_title(
        "Trục tung xuất phát từ 0: Phản ánh trung thực tương quan tỷ lệ", pad=12
    )

    # 6. Lưu tệp hình ảnh
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax


ax_honest_c1 = plot_honest_bars(dulieu_sosanh, "figures/honest-reference.png")

# Bắt đầu lời giải

from pathlib import Path
import matplotlib.axes


def validate_chart_structure(
    ax: matplotlib.axes.Axes,
    min_title_len: int = 15,
    require_ylabel: bool = False,
    require_xlabel: bool = False,
    require_zero_x: bool = False,
    require_zero_y: bool = False,
    min_patches: int = 0,
    min_lines: int = 0,
    saved_path: str = None,
) -> dict:
    ket_qua = {
        "has_title": len(ax.get_title().strip()) >= min_title_len,
        "has_ylabel": not require_ylabel or bool(ax.get_ylabel().strip()),
        "has_xlabel": not require_xlabel or bool(ax.get_xlabel().strip()),
        "has_zero_x": not require_zero_x or (round(ax.get_xlim()[0], 5) == 0.0),
        "has_zero_y": not require_zero_y or (round(ax.get_ylim()[0], 5) == 0.0),
        "has_patches": len(ax.patches) >= min_patches,
        "has_lines": len(ax.lines) >= min_lines,
        "has_file": (
            bool(
                saved_path
                and Path(saved_path).is_file()
                and Path(saved_path).stat().st_size > 0
            )
            if saved_path
            else True
        ),
    }
    ket_qua["all_passed"] = all(ket_qua.values())
    return ket_qua


# Gọi thực nghiệm hàm kiểm tra biểu đồ cột trung thực Bài 9:
kiem_tra_c2 = validate_chart_structure(
    ax_honest_c1,
    min_title_len=15,
    require_ylabel=True,
    require_zero_y=True,
    min_patches=3,
    saved_path="figures/honest_bars_c1.png",
)
display(f"Cách 2: Trạng thái kiểm định toàn diện = {kiem_tra_c2['all_passed']}")

# Kết thúc lời giải
```

#### Giải thích cách 2

Đóng các điều kiện thành hàm kiểm giúp dùng lại cho nhiều hình. Điều kiện cần phù hợp từng loại biểu đồ, vì trục log hoặc biểu đồ đường có quy ước khác biểu đồ thanh. Kiểm tự động cấu trúc phải đi cùng xem hình để phát hiện chữ bị cắt, màu khó phân biệt hoặc nguồn ghi sai.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Trạng thái kiểm định toàn diện = True |
#### So sánh cách dùng

Hãy chọn Cách 1 khi viết kiểm thử đơn vị cho một đồ thị cụ thể để xác minh nhanh cấu trúc của các trục. Cách 2 cần thiết khi muốn xây dựng bộ quy tắc kiểm định tái sử dụng nhằm tự động hóa đánh giá chất lượng nhiều biểu đồ.

:::

---

<span id="data-lab-12-11"></span>
### Bài tập 11: So sánh phân phối giữa các nhóm trên biểu đồ ghép cùng thang đo

::: exercise Dựng biểu đồ ghép cùng thang đo
Khi so sánh phân phối của một đại lượng (như số ngày mở lịch `availability_365`) giữa hai địa bàn khác nhau (Ví dụ: Quận Providencia và quận Santiago), sai lầm phổ biến là vẽ hai biểu đồ độc lập với thang đo trục tung tự động co giãn riêng biệt. Khi đó, một cột cao ở biểu đồ quận nhỏ có thể chỉ chứa 5 chỗ ở nhưng lại trông đồ sộ ngang với cột chứa 20 chỗ ở của quận lớn, gây hiểu sai lệch hoàn toàn về quy mô. Cần sử dụng kỹ thuật biểu đồ con ghép đôi với tham số chia sẻ trục tung (`sharey=True`).

Hãy viết hàm `plot_comparative_groups(ds: pd.DataFrame, quan_a: str, quan_b: str, path: str, bins: int = 20) -> tuple` thực hiện:
1. Trích xuất Series `availability_365` không chứa `NaN` của quận `quan_a` và quận `quan_b`.
2. Khởi tạo khung hình gồm hai biểu đồ con nằm cạnh nhau với trục tung dùng chung: `fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)`.
3. Vẽ histogram cho `quan_a` trên `ax1` và cho `quan_b` trên `ax2` với cùng số lượng khoảng chia `bins`.
4. Đặt tiêu đề riêng cho từng biểu đồ con ghi rõ tên quận và số lượng quan sát $N$.
5. Đặt tiêu đề chung cho toàn bộ khung hình bằng `fig.suptitle(...)`.
6. Lưu tệp hình ảnh vào `path` và trả về bộ `(fig, (ax1, ax2))`.
:::

::: solution
#### Cách 1: Sử dụng subplots với tham số sharey và vẽ độc lập từng trục

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import pandas as pd
import matplotlib.pyplot as plt


def plot_comparative_groups(
    ds: pd.DataFrame, quan_a: str, quan_b: str, path: str, bins: int = 20
) -> tuple:
    # 1. Trích xuất dữ liệu của hai địa bàn khảo sát
    avail_a = ds.loc[ds["neighbourhood"] == quan_a, "availability_365"].dropna()
    avail_b = ds.loc[ds["neighbourhood"] == quan_b, "availability_365"].dropna()

    # 2. Khởi tạo biểu đồ ghép đôi chia sẻ trục tung
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)

    # 3. Vẽ phân phối cho quận A
    ax1.hist(avail_a, bins=bins, color="#1976d2", edgecolor="white", linewidth=0.5)
    ax1.set_title(f"Quận {quan_a} (N = {len(avail_a)})", fontsize=11)
    ax1.set_xlabel("Số ngày mở lịch (ngày)")
    ax1.set_ylabel("Số lượng chỗ ở")

    # 4. Vẽ phân phối cho quận B với cùng thang đo trục tung
    ax2.hist(avail_b, bins=bins, color="#f57c00", edgecolor="white", linewidth=0.5)
    ax2.set_title(f"Quận {quan_b} (N = {len(avail_b)})", fontsize=11)
    ax2.set_xlabel("Số ngày mở lịch (ngày)")

    # 5. Tiêu đề tổng quát cho toàn bộ khung so sánh
    fig.suptitle(
        "So sánh phân phối số ngày mở lịch trên cùng thang đo trục tung",
        y=1.02,
        fontsize=12,
    )

    # 6. Lưu tệp hình ảnh
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return fig, (ax1, ax2)


# Gọi thực nghiệm hàm với dữ liệu mẫu:
fig_comp_c1, (ax_pro_c1, ax_san_c1) = plot_comparative_groups(
    DEMO_DS, "Providencia", "Santiago", "figures/comparative_groups_c1.png", bins=20
)
display(f"Đã lưu biểu đồ ghép đôi: Cùng giới hạn trục y = {ax_pro_c1.get_ylim()}")

# Kết thúc lời giải
```

#### Giải thích cách 1

Đưa các nhóm lên những khung hình có cùng thang đo để chiều cao và độ dài so sánh được. Nếu từng khung tự chọn giới hạn, một biến động nhỏ có thể trông lớn như biến động ở nhóm khác. Giữ tên nhóm và đơn vị ở vị trí dễ đọc.

#### Kết quả cách 1

| Kết quả |
| --- |
| Đã lưu biểu đồ ghép đôi: Cùng giới hạn trục y = (np.float64(0.0), np.float64(4.2)) |

![So sánh phân phối số ngày mở lịch giữa hai quận trên cùng thang đo](img/labs/lab-12/comparative-groups-distribution.svg)

#### Cách 2: Tự động hóa tính toán khoảng chia dùng chung và đồng bộ đường gióng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

_QUAN = (
    ["Santiago"] * 20
    + ["Providencia"] * 12
    + ["Las Condes"] * 10
    + ["Ñuñoa"] * 8
    + ["Lo Barnechea"] * 6
    + ["Vitacura"] * 4
)

_CHU_KY_PHONG_RIENG = {
    "Santiago": 3,
    "Providencia": 4,
    "Las Condes": 5,
    "Ñuñoa": 2,
    "Lo Barnechea": 0,
    "Vitacura": 4,
}

DEMO_DS = pd.DataFrame(
    {
        "id": list(range(101, 161)),
        "neighbourhood": _QUAN,
        "room_type": [
            (
                "Private room"
                if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1
                else "Entire home/apt"
            )
            for k, q in enumerate(_QUAN)
        ],
        "availability_365": [
            0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20
            for k in range(60)
        ],
    }
)

from pathlib import Path

Path("figures").mkdir(parents=True, exist_ok=True)

# Bắt đầu lời giải

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot_comparative_groups(
    ds: pd.DataFrame, quan_a: str, quan_b: str, path: str, bins: int = 20
) -> tuple:
    s_a = ds.loc[ds["neighbourhood"] == quan_a, "availability_365"].dropna()
    s_b = ds.loc[ds["neighbourhood"] == quan_b, "availability_365"].dropna()

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)
    lưới_chia = np.linspace(0, 365, bins + 1)

    ax1.hist(s_a, bins=lưới_chia, color="#1565c0", edgecolor="#ffffff", linewidth=0.6)
    ax1.set_title(f"Địa bàn {quan_a} (N = {len(s_a)})", fontsize=11)
    ax1.set_xlabel("Số ngày mở lịch (ngày)")
    ax1.set_ylabel("Số lượng chỗ ở")

    ax2.hist(s_b, bins=lưới_chia, color="#e65100", edgecolor="#ffffff", linewidth=0.6)
    ax2.set_title(f"Địa bàn {quan_b} (N = {len(s_b)})", fontsize=11)
    ax2.set_xlabel("Số ngày mở lịch (ngày)")

    fig.suptitle(
        "Phân tích so sánh phân phối số ngày mở lịch giữa hai quận", y=1.02, fontsize=12
    )
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return fig, (ax1, ax2)


# Gọi thực nghiệm hàm với dữ liệu mẫu:
fig_comp_c2, (ax_pro_c2, ax_san_c2) = plot_comparative_groups(
    DEMO_DS, "Providencia", "Santiago", "figures/comparative_groups_c2.png", bins=20
)
display(f"Cách 2: Giới hạn trục y dùng chung = {ax_pro_c2.get_ylim()}")

# Kết thúc lời giải
```

#### Giải thích cách 2

Dùng `subplots` và các tùy chọn chia sẻ trục giúp thống nhất giới hạn một cách tường minh. Mã vẫn cần kiểm dữ liệu của từng nhóm và thứ tự kỳ. Khi đơn vị hai đại lượng khác nhau, không ép chúng vào cùng thang rồi diễn giải như cùng độ lớn.

#### Kết quả cách 2

| Kết quả |
| --- |
| Cách 2: Giới hạn trục y dùng chung = (np.float64(0.0), np.float64(4.2)) |

![So sánh phân phối số ngày mở lịch giữa hai quận trên cùng thang đo](img/labs/lab-12/comparative-groups-distribution.svg)
#### So sánh cách dùng

Cả hai cách dùng `sharey=True` để giữ cùng thang tần suất. Cách 2 còn dùng chung lưới khoảng từ 0 đến 365 ngày, giúp một khoảng ngày mang cùng ý nghĩa ở cả hai hình. Chọn cách này khi cần đối chiếu trực tiếp hình dạng hai phân phối.

:::

---

## 4. Tổng kết quy tắc thực hành trực quan hóa dữ liệu

| Nguyên tắc kỹ thuật | Quy chuẩn chuẩn mực | Lỗi thường gặp cần tránh | Hậu quả nếu vi phạm |
| :--- | :--- | :--- | :--- |
| Gốc tọa độ biểu đồ thanh/cột | Bắt buộc xuất phát từ 0 (`xlim[0] == 0` hoặc `ylim[0] == 0`) | Cắt ngắn trục tung để làm nổi bật chênh lệch | Phóng đại sai lệch thị giác gấp nhiều lần |
| Kỳ thời gian chưa trọn vẹn | Loại bỏ tháng hoặc quý cuối cùng chưa kết thúc | Giữ nguyên kỳ cụt trong chuỗi thời gian | Gây hiểu lầm về sự sụt giảm đột ngột |
| Nhãn đo lường và đơn vị | Ghi rõ đơn vị tính trên các trục tọa độ | Chỉ ghi tên biến viết tắt không có đơn vị | Người xem không hiểu thang đo số liệu |
| Phân phối hai đỉnh | Dùng biểu đồ tần suất phân tách các phân khúc | Chỉ báo cáo duy nhất giá trị trung bình cộng | Giá trị trung bình rơi vào vùng không có dữ liệu |
| So sánh nhiều nhóm | Sử dụng `sharey=True` hoặc đồng bộ thang đo | Để mỗi biểu đồ con tự co giãn trục độc lập | Độc giả nhận thức sai lệch về quy mô mẫu |
| Quy trình xuất bản tự động | Kiểm tra cấu trúc hình ảnh bằng câu lệnh khẳng định | Kiểm tra thủ công bằng mắt thường | Bỏ sót lỗi kỹ thuật khi chạy pipeline lớn |
