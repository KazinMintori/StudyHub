## Lab 13: Trực quan hóa nâng cao với seaborn, bản đồ địa lý và phản biện biểu đồ

Cùng một bảng giá, biểu đồ hộp cho biết mức giá giữa các nhóm, còn bản đồ cho biết phân bố theo quận. Số đánh giá theo năm lại đặt ra một câu hỏi khác: Mức thay đổi phụ thuộc thế nào vào năm được chọn để so sánh? Bảy bài dưới đây lần lượt kiểm tra các cách trình bày này bằng dữ liệu nhỏ có thể tính lại.

---

## Bối cảnh và snapshot dữ liệu tham chiếu

Các bài tập thực nghiệm trong bài học này đối chiếu trực tiếp với bộ dữ liệu lưu trữ công cộng của Inside Airbnb đối với thành phố Santiago, Chile:
- **Địa chỉ kho dữ liệu gốc**: `https://data.insideairbnb.com/chile/rm/santiago/`
- **Phiên bản snapshot tham chiếu**: Bản lưu trữ ngày 29 tháng 06 năm 2026 (`2026-06-29/visualisations/listings.csv`, `2026-06-29/visualisations/reviews.csv` và `2026-06-29/visualisations/neighbourhoods.geojson`).
- **Đơn vị đo lường**: Giá niêm yết được biểu diễn theo CLP/đêm. Giữ số khi tính toán và chọn mức làm tròn khi trình bày.
- **Hệ quy chiếu tọa độ không gian (CRS)**: Kiểm tra CRS của dữ liệu khi nạp bản đồ thật. Các hình chữ nhật giả lập bên dưới được gán EPSG:3857 để minh họa phép ghép và vẽ.

> [!NOTE]
> **Dữ liệu để thử chương trình**: `DEMO_DS` có 48 dòng chỗ ở ở năm quận. `DEMO_QUAN_BAN_DO` có sáu tên quận, thêm Pirque không có dòng chỗ ở trong mẫu. `DEMO_RV` chứa 3.900 đánh giá giả lập trong các năm 2014–2026.
>
> Các hình chữ nhật trong ví dụ là ranh giới giả lập, không phải vị trí hoặc hình dạng các quận Santiago. Các số đếm và mức giá chỉ mô tả mẫu này. Nhãn “chuyên nghiệp” và “cá nhân” trong code là tên quy ước theo ngưỡng số chỗ ở, không xác nhận nghề nghiệp, chất lượng dịch vụ hay hình thức pháp lý của chủ nhà.

### Khởi tạo môi trường và dữ liệu dùng chung

Toàn bộ các ví dụ và lời giải trong tài liệu sử dụng thư viện pandas, numpy, matplotlib, seaborn, shapely và geopandas:

```python
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from shapely.geometry import box
import geopandas as gpd

# Thiết lập giao diện đồ họa chuẩn mực
sns.set_theme(style="whitegrid")

# Bảng chỗ ở mẫu giả lập: 48 chỗ ở tại 5 quận
_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)
DEMO_DS = pd.DataFrame(
    {
        "id": range(201, 249),
        "neighbourhood": _QUAN,
        "room_type": [
            "Private room" if k % 4 == 1 else "Entire home/apt" for k in range(48)
        ],
        "price": [
            (
                None
                if k % 11 == 5
                else float(18000 + (k * 7919) % 90000 + (15000 if k % 3 == 0 else 0))
            )
            for k in range(48)
        ],
        "calculated_host_listings_count": [1 + (k * 5) % 9 for k in range(48)],
    }
)

# Danh sách 6 quận trên bản đồ ranh giới (bao gồm quận Pirque trắng dữ liệu)
DEMO_QUAN_BAN_DO = [
    "Santiago",
    "Providencia",
    "Las Condes",
    "Ñuñoa",
    "Lo Barnechea",
    "Pirque",
]

# Bảng đánh giá mẫu giả lập: Tái hiện diễn biến chuỗi thời gian 2014-2026
_SO_THEO_NAM = {
    2014: 40,
    2015: 70,
    2016: 120,
    2017: 210,
    2018: 330,
    2019: 420,
    2020: 90,
    2021: 150,
    2022: 380,
    2023: 520,
    2024: 610,
    2025: 700,
    2026: 260,
}
DEMO_RV = pd.DataFrame(
    {
        "date": [
            pd.Timestamp(f"{nam}-01-01")
            + pd.Timedelta(days=(k * 97) % (181 if nam == 2026 else 365))
            for nam, so in _SO_THEO_NAM.items()
            for k in range(so)
        ]
    }
)

print(
    "Khởi tạo môi trường thành công: Chỗ ở =",
    len(DEMO_DS),
    ", Quận bản đồ =",
    len(DEMO_QUAN_BAN_DO),
    ", Đánh giá =",
    len(DEMO_RV),
)
```

Bảng 13.0: Cấu trúc dữ liệu mẫu giả lập của danh sách chỗ ở (`DEMO_DS`):

| id | neighbourhood | room_type | price (CLP) | calculated_host_listings_count |
|---:|:---|:---|---:|---:|
| 201 | Santiago | Entire home/apt | 33,000 | 1 |
| 202 | Santiago | Private room | 25,919 | 6 |
| 203 | Santiago | Entire home/apt | 33,838 | 2 |
| 204 | Santiago | Entire home/apt | 56,757 | 7 |
| 205 | Santiago | Entire home/apt | 49,676 | 3 |
| 206 | Santiago | Entire home/apt | NaN | 8 |

---

## Bài 1: So sánh phân phối giá theo nhóm chủ nhà và loại phòng bằng boxplot với hue trên thang logarit

<span id="data-lab-13-01"></span>

::: exercise
**Mục tiêu**: Khảo sát phân phối giá lưu trú nhiều chiều bằng biểu đồ hộp (boxplot) của seaborn, kết hợp phân tầng màu sắc (`hue`) để so sánh hai nhóm quy mô chủ nhà theo từng loại phòng, rồi thực hành đọc giá trên thang log.

**Dữ liệu đầu vào**: Bảng dữ liệu chỗ ở `co_gia` đã loại bỏ các bản ghi khuyết giá (`price.dropna()`), gồm các cột:
- `price`: Mức giá niêm yết mỗi đêm (số thực dương).
- `room_type`: Loại chỗ ở (`Entire home/apt`, `Private room`).
- `kieu_host`: Nhóm chủ nhà (`chuyên nghiệp` nếu calculated_host_listings_count từ 5 trở lên, `cá nhân` nếu calculated_host_listings_count dưới 5).

**Thao tác yêu cầu**:
1. Xây dựng hàm `plot_price_box(co_gia: pd.DataFrame)` nhận bảng dữ liệu và trả về đối tượng `Axes`.
2. Tạo khung vẽ mới với kích thước `figsize=(8.5, 4)`.
3. Sử dụng hàm `sns.boxplot` với trục hoành là `price`, trục tung là `room_type`, và phân tầng màu sắc `hue="kieu_host"`.
4. Thiết lập thang đo logarit cho trục hoành bằng lệnh `ax.set_xscale("log")`.
5. Đặt tiêu đề rõ ràng phản ánh thông điệp phân tích (độ dài tối thiểu 15 ký tự), đặt nhãn trục hoành có đơn vị đo rõ ràng.
6. Bảo đảm chú giải đồ thị do tham số `hue` sinh ra hiển thị đúng hai nhóm giá trị `chuyên nghiệp` và `cá nhân`.
7. Trả lời câu hỏi phân tích: Ở từng loại phòng, hộp phân phối của nhóm chuyên nghiệp nằm lệch về phía nào? Hai nhóm chủ nhà có tách rời thành hai phân khúc giá riêng biệt hay không? Khi nào thang log hữu ích, và khi nào có thể giữ thang tuyến tính?

**Trường hợp biên cần chú ý**: Hàm phải hoạt động ổn định trên bảng dữ liệu chỉ có một loại phòng duy nhất hoặc khi một trong hai nhóm chủ nhà không có quan sát trong một phân khúc phòng.
:::

::: solution
### Đọc hộp trước khi đọc màu

Hộp trải từ tứ phân vị dưới Q1 đến tứ phân vị trên Q3, đường trong hộp là trung vị. Với `whis=1.5` mặc định, hai râu đi tới các quan sát xa nhất còn nằm trong hàng rào tương ứng. Râu không nhất thiết đi tới cực tiểu, cực đại của toàn bộ nhóm. Các quan sát ngoài râu được vẽ riêng.

Khoảng tứ phân vị được tính bằng:

$$
I = Q_3 - Q_1.
$$

Hàng rào dưới là:

$$
L = Q_1 - 1{,}5I.
$$

Hàng rào trên là:

$$
U = Q_3 + 1{,}5I.
$$

Thang log thích hợp khi cần xem các giá dương trải trên nhiều mức độ lớn hoặc so sánh theo tỷ lệ. Khoảng từ 10 đến 100 có cùng độ dài hiển thị với khoảng từ 100 đến 1000 trên thang log cơ số 10. Nó không biến mọi phân phối thành đối xứng và không bắt buộc cho mọi boxplot. Bài này dùng thang log để thực hành cách đọc đó.

Trên fixture, trung vị nhóm có từ năm chỗ ở cao hơn ở nguyên căn nhưng thấp hơn ở phòng riêng. Vì vậy không thể áp nhận xét cùng chiều cho cả hai loại phòng. Hai khoảng tứ phân vị có phần chồng lấn, nhưng điều đó không chứng minh nguyên nhân định giá hay quan hệ cạnh tranh giữa chủ nhà.

#### Cách 1: Sử dụng hàm seaborn.boxplot trực tiếp với giao diện Axes

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_price_box(co_gia: pd.DataFrame) -> plt.Axes:
    """Vẽ boxplot phân phối giá theo loại phòng và nhóm chủ nhà trên thang logarit.

    Tham số:
        co_gia: DataFrame chứa cột 'price', 'room_type' và 'kieu_host'.
    Trả về:
        Đối tượng Axes chứa biểu đồ đã được định dạng chuẩn mực.
    """
    fig, ax = plt.subplots(figsize=(8.5, 4))
    sns.boxplot(
        data=co_gia,
        x="price",
        y="room_type",
        hue="kieu_host",
        palette=["#3182bd", "#de2d26"],
        ax=ax,
    )
    ax.set_xscale("log")
    ax.set_title(
        "Phân phối giá theo loại phòng và nhóm chủ nhà trên thang logarit",
        fontsize=11,
        fontweight="bold",
    )
    ax.set_xlabel("Giá niêm yết mỗi đêm (CLP, thang logarit)")
    ax.set_ylabel("Loại phòng lưu trú")
    return ax


# Dữ liệu thử nghiệm minh họa
_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)
demo_ds = pd.DataFrame(
    {
        "id": range(201, 249),
        "neighbourhood": _QUAN,
        "room_type": [
            "Private room" if k % 4 == 1 else "Entire home/apt" for k in range(48)
        ],
        "price": [
            (
                None
                if k % 11 == 5
                else float(18000 + (k * 7919) % 90000 + (15000 if k % 3 == 0 else 0))
            )
            for k in range(48)
        ],
        "calculated_host_listings_count": [1 + (k * 5) % 9 for k in range(48)],
    }
)
co_gia_demo = demo_ds.dropna(subset=["price"]).assign(
    kieu_host=lambda d: (d["calculated_host_listings_count"] >= 5).map(
        {True: "chuyên nghiệp", False: "cá nhân"}
    )
)

ax_kq_c1 = plot_price_box(co_gia_demo)
print("Tiêu đề biểu đồ Cách 1:", ax_kq_c1.get_title())
print("Thang đo trục x:", ax_kq_c1.get_xscale())
print(
    "Các nhóm trong chú giải:",
    [t.get_text() for t in ax_kq_c1.get_legend().get_texts()],
)
plt.close(ax_kq_c1.figure)
```

##### Giải thích chi tiết Cách 1

`plt.subplots` tạo Figure và Axes để vẽ một hình độc lập. `sns.boxplot` đọc cột price cho trục ngang, room_type cho trục dọc và chia mỗi loại phòng theo hue. Mỗi hộp tóm tắt giá của một cặp loại phòng và nhóm quy ước.

`ax.set_xscale("log")` đổi cách đặt vị trí trên trục, nên chỉ dùng cho giá dương. Bước dropna trong ví dụ loại giá thiếu nhưng chưa tự loại giá bằng không hoặc âm từ một nguồn khác. Danh sách palette được gắn theo thứ tự hue mà seaborn suy ra. Màu hỗ trợ phân nhóm, còn nhãn chú giải vẫn cần để đọc đúng.

##### Kết quả thực thi Cách 1

| Thuộc tính đọc từ Axes | Kết quả trên fixture |
| --- | --- |
| get_xscale() | `log` |
| Tiêu đề | Phân phối giá theo loại phòng và nhóm chủ nhà trên thang logarit |
| Độ dài tiêu đề | 64 ký tự |
| Thứ tự chú giải | `["cá nhân", "chuyên nghiệp"]` theo thứ tự xuất hiện của fixture |
| Số nhóm có giá | 4 |

![Hình 13.1: Phân phối giá niêm yết theo loại phòng và nhóm chủ nhà trên thang logarit](/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-01-boxplot-gia-chu-nha.svg)

#### Cách 2: Kiểm soát thứ tự phân loại tường minh và tùy biến hộp nâng cao

```python
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_price_box_nang_cao(co_gia: pd.DataFrame) -> plt.Axes:
    """Vẽ boxplot với thứ tự phân loại cố định và định dạng chú giải nâng cao.

    Tham số:
        co_gia: DataFrame chứa cột 'price', 'room_type' và 'kieu_host'.
    Trả về:
        Đối tượng Axes đã tùy biến chuyên sâu.
    """
    fig, ax = plt.subplots(figsize=(8.5, 4))
    thu_tu_phong = ["Entire home/apt", "Private room"]
    thu_tu_host = ["cá nhân", "chuyên nghiệp"]
    sns.boxplot(
        data=co_gia,
        x="price",
        y="room_type",
        hue="kieu_host",
        order=thu_tu_phong,
        hue_order=thu_tu_host,
        palette={"cá nhân": "#2b8cbe", "chuyên nghiệp": "#e6550d"},
        width=0.6,
        showfliers=True,
        ax=ax,
    )
    ax.set_xscale("log")
    ax.set_title(
        "So sánh mức giá phân vị giữa chủ nhà chuyên nghiệp và cá nhân",
        fontsize=11,
        fontweight="bold",
    )
    ax.set_xlabel("Mức giá niêm yết (CLP/đêm, thang đo logarit)")
    ax.set_ylabel("Phân khúc phòng")
    ax.legend(title="Nhóm chủ nhà", loc="lower right", frameon=True)
    return ax


# Dữ liệu thử nghiệm minh họa
_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)
demo_ds = pd.DataFrame(
    {
        "id": range(201, 249),
        "neighbourhood": _QUAN,
        "room_type": [
            "Private room" if k % 4 == 1 else "Entire home/apt" for k in range(48)
        ],
        "price": [
            (
                None
                if k % 11 == 5
                else float(18000 + (k * 7919) % 90000 + (15000 if k % 3 == 0 else 0))
            )
            for k in range(48)
        ],
        "calculated_host_listings_count": [1 + (k * 5) % 9 for k in range(48)],
    }
)
co_gia_demo = demo_ds.dropna(subset=["price"]).assign(
    kieu_host=lambda d: (d["calculated_host_listings_count"] >= 5).map(
        {True: "chuyên nghiệp", False: "cá nhân"}
    )
)

ax_kq_c2 = plot_price_box_nang_cao(co_gia_demo)
print("Tiêu đề biểu đồ Cách 2:", ax_kq_c2.get_title())
print("Thang đo trục x Cách 2:", ax_kq_c2.get_xscale())
print(
    "Kiểm tra nhãn chú giải:", [t.get_text() for t in ax_kq_c2.get_legend().get_texts()]
)
plt.close(ax_kq_c2.figure)
```

##### Giải thích chi tiết Cách 2

`order` cố định thứ tự hai loại phòng và `hue_order` cố định thứ tự hai nhóm. Từ điển palette gắn một màu với từng nhãn thay vì phụ thuộc vị trí đầu tiên trong dữ liệu. Khi thiếu một nhóm, thứ tự danh mục khai báo vẫn giúp so sánh các hình giữa những lần chạy.

`width=0.6` chỉnh bề rộng nhóm hộp trên trục phân loại. `showfliers=True` giữ các điểm ngoài râu để người xem biết chúng tồn tại. Vị trí chú giải và khoảng cách chữ cần được rà lại khi tên nhóm hoặc số nhóm thay đổi. Những tùy chọn này không làm thay đổi số quan sát hoặc trung vị của từng nhóm.

##### Kết quả thực thi Cách 2

| room_type | Nhóm quy ước | n giá hợp lệ | Trung vị (CLP) | Q1 | Q3 |
| --- | --- | --- | --- | --- | --- |
| Entire home/apt | cá nhân | 15 | 64760.0 | 45570.0 | 85961.0 |
| Entire home/apt | chuyên nghiệp | 18 | 72637.0 | 40123.0 | 90056.75 |
| Private room | cá nhân | 5 | 104271.0 | 67651.0 | 114327.0 |
| Private room | chuyên nghiệp | 6 | 51813.0 | 37232.0 | 70165.0 |

#### So sánh hai cách

Cách 1 phù hợp để dựng và kiểm tra hình đầu tiên. Cách 2 thêm thứ tự và ánh xạ màu cố định cho việc so sánh nhiều hình. Các số trong bảng là thống kê của 44 giá hợp lệ trong fixture, không phải thống kê thị trường Santiago.

:::

---

## Bài 2: Ghép dữ liệu địa lý không gian với ranh giới quận, thống kê số chỗ ở và xử lý quận khuyết dữ liệu

<span id="data-lab-13-02"></span>

::: exercise
**Mục tiêu**: Thực hiện phép kết hợp dữ liệu bảng thống kê chỗ ở với bảng ranh giới hình học không gian của các quận (GeoDataFrame), thống kê số lượng chỗ ở thực tế của từng quận, kiểm tra quận không có dòng trong mẫu và giải thích khi nào có thể điền số đếm bằng 0.

**Dữ liệu đầu vào**:
- Bảng dữ liệu chỗ ở `ds`: Chứa cột `neighbourhood` (tên quận hành chính của từng chỗ ở).
- Bảng ranh giới địa lý `geo`: DataFrame hoặc GeoDataFrame chứa cột `neighbourhood` với các tên quận duy nhất không trùng lặp (ví dụ 6 quận: Santiago, Providencia, Las Condes, Ñuñoa, Lo Barnechea, Pirque).

**Thao tác yêu cầu**:
1. Xây dựng hàm `count_by_area(ds: pd.DataFrame, geo: pd.DataFrame) -> dict`.
2. Đếm số lượng chỗ ở theo từng quận từ bảng `ds`, đặt tên cột số lượng là `n`.
3. Thực hiện phép ghép trái `geo.merge(..., on="neighbourhood", how="left")` để giữ nguyên toàn bộ số dòng và thứ tự dòng ban đầu của bảng ranh giới `geo`.
4. Đếm số lượng quận có ranh giới trên bản đồ nhưng hoàn toàn không có chỗ ở nào trong bảng `ds` (số lượng ô `NaN` ngay sau phép ghép trái), lưu vào biến `so_quan_nan`.
5. Điền giá trị 0 cho cột `n` bằng phương thức `fillna(0)` và ép kiểu sang số nguyên `int`.
6. Không chỉnh sửa bảng dữ liệu `geo` đầu vào. Chỗ ở thuộc các quận không có tên trên bản đồ `geo` sẽ tự động bị loại bỏ khỏi bảng kết quả.
7. Trả về từ điển có đúng hai khóa:
   - `"so_quan_nan"`: Số nguyên biểu thị số quận trắng dữ liệu.
   - `"ban_do"`: Bảng sau khi ghép và điền 0, chứa toàn bộ các cột ban đầu của `geo` cộng thêm cột `n`.

**Trường hợp biên cần chú ý**: Bảng `ds` có thể không chứa bất kỳ chỗ ở nào của một số quận trên bản đồ, hoặc ngược lại chứa các chỗ ở có tên quận bị sai chính tả không khớp với `geo`. Phép ghép trái phải bảo toàn số hàng và thứ tự của `geo`.
:::

::: solution
### Khi nào điền số đếm bằng không?

`geo` có sáu tên quận, trong khi ds chỉ chứa năm tên. Ghép trái theo tên giữ các dòng ranh giới và thêm số đếm nếu có khóa khớp. Đây là phép ghép theo thuộc tính, không phải phép xác định một điểm nằm trong đa giác nào.

Pirque không có dòng trong fixture nên số đếm sau ghép là NaN. Sau khi kiểm tra tên khóa khớp và xác nhận phạm vi mẫu, ta có thể ghi số quan sát bằng 0. Nếu tên quận sai chính tả hoặc nguồn thu thập chưa bao phủ quận, NaN chưa đủ để kết luận không có chỗ ở. Các tên chỉ có trong ds nhưng không có trong geo không xuất hiện trên bảng kết quả và cần được kiểm tra riêng.

#### Cách 1: Sử dụng groupby kết hợp phép ghép merge và fillna tuần tự

```python
import pandas as pd


def count_by_area_buoc(ds: pd.DataFrame, geo: pd.DataFrame) -> dict:
    """Ghép số lượng chỗ ở vào bảng ranh giới địa lý theo cách tiếp cận tuần tự.

    Tham số:
        ds: DataFrame chứa cột 'neighbourhood'.
        geo: DataFrame hoặc GeoDataFrame chứa cột 'neighbourhood'.
    Trả về:
        Từ điển gồm 'so_quan_nan' và 'ban_do'.
    """
    dem = ds.groupby("neighbourhood", observed=False).size().reset_index(name="n")
    ban_do_raw = geo.merge(dem, on="neighbourhood", how="left")
    so_quan_nan = int(ban_do_raw["n"].isna().sum())
    ban_do = ban_do_raw.copy()
    ban_do["n"] = ban_do["n"].fillna(0).astype(int)
    return {"so_quan_nan": so_quan_nan, "ban_do": ban_do}


# Dữ liệu thử nghiệm minh họa
_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)
demo_ds = pd.DataFrame(
    {
        "id": range(201, 249),
        "neighbourhood": _QUAN,
    }
)
demo_quan_ban_do = [
    "Santiago",
    "Providencia",
    "Las Condes",
    "Ñuñoa",
    "Lo Barnechea",
    "Pirque",
]
geo_demo = pd.DataFrame(
    {
        "neighbourhood": demo_quan_ban_do,
        "neighbourhood_group": [None] * 6,
    }
)

kq_c1 = count_by_area_buoc(demo_ds, geo_demo)
print("Số quận không có chỗ ở (Cách 1):", kq_c1["so_quan_nan"])
print("Bảng kết quả sau khi ghép Cách 1:")
print(kq_c1["ban_do"])
```

##### Giải thích chi tiết Cách 1

`groupby(...).size()` đếm mọi dòng trong mỗi nhóm, kể cả dòng thiếu giá. `reset_index(name="n")` tạo bảng đếm hai cột để ghép. Vì bảng đếm có một dòng cho mỗi tên quận và geo có khóa duy nhất, phép ghép trái giữ sáu dòng bản đồ trong bài.

Đếm NaN ngay sau ghép giúp lưu được số quận không khớp trước khi điền. `fillna(0).astype(int)` chuyển cột số đếm thành số nguyên. Không áp quy tắc điền không này cho cột giá: Không biết giá không đồng nghĩa giá bằng không.

##### Kết quả thực thi Cách 1

| neighbourhood | n |
| --- | --- |
| Santiago | 18 |
| Providencia | 12 |
| Las Condes | 8 |
| Ñuñoa | 6 |
| Lo Barnechea | 4 |
| Pirque | 0 |

`so_quan_nan` bằng `1`, tổng n bằng `48`. Các cột ban đầu của geo được giữ.

#### Cách 2: Sử dụng Series.map vector hóa và kiểm tra tính toàn vẹn dữ liệu

```python
import pandas as pd


def count_by_area_map(ds: pd.DataFrame, geo: pd.DataFrame) -> dict:
    """Ghép số lượng chỗ ở bằng ánh xạ Series.map vector hóa.

    Tham số:
        ds: DataFrame chứa cột 'neighbourhood'.
        geo: DataFrame hoặc GeoDataFrame chứa cột 'neighbourhood'.
    Trả về:
        Từ điển gồm 'so_quan_nan' và 'ban_do'.
    """
    counts = ds["neighbourhood"].value_counts()
    ban_do = geo.copy()
    so_quan_nan = int((~ban_do["neighbourhood"].isin(counts.index)).sum())
    ban_do["n"] = ban_do["neighbourhood"].map(counts).fillna(0).astype(int)
    return {"so_quan_nan": so_quan_nan, "ban_do": ban_do}


# Dữ liệu thử nghiệm minh họa
_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)
demo_ds = pd.DataFrame({"neighbourhood": _QUAN})
geo_demo = pd.DataFrame(
    {
        "neighbourhood": [
            "Santiago",
            "Providencia",
            "Las Condes",
            "Ñuñoa",
            "Lo Barnechea",
            "Pirque",
        ],
        "neighbourhood_group": [None] * 6,
    }
)

kq_c2 = count_by_area_map(demo_ds, geo_demo)
print(kq_c2["ban_do"].to_string(index=False))
print(
    "Giá trị số chỗ ở của quận Pirque:",
    kq_c2["ban_do"].loc[kq_c2["ban_do"]["neighbourhood"] == "Pirque", "n"].item(),
)
```

##### Giải thích chi tiết Cách 2

Khi chỉ cần một chỉ số đếm, `value_counts()` tạo Series có chỉ mục là tên quận. `Series.map(counts)` tra số đếm tương ứng cho mỗi tên trong bảng ranh giới. Các tên không có trong Series nhận NaN để có thể đếm và xử lý theo cùng quy tắc.

Cách viết này tránh đưa thêm các cột không cần thiết vào phép ghép, nhưng vẫn phải tạo và tra cứu cấu trúc đếm. Không thể kết luận nó nhanh hơn merge trên mọi kích thước bảng nếu chưa đo. Cần giữ bản sao bảng đích và thứ tự dòng khi gán cột mới.

##### Kết quả thực thi Cách 2

| neighbourhood | n |
| --- | --- |
| Santiago | 18 |
| Providencia | 12 |
| Las Condes | 8 |
| Ñuñoa | 6 |
| Lo Barnechea | 4 |
| Pirque | 0 |

`so_quan_nan` cũng bằng `1`. Chỉ mục và các cột ranh giới được giữ để vẽ tiếp.

#### So sánh hai cách

Hai cách cùng ánh xạ số đếm lên tên quận. Merge thuận tiện khi cần thêm nhiều chỉ số trong một bảng tổng hợp. Map biểu đạt gọn việc tra một chỉ số theo khóa. Cả hai cần kiểm tra tên không khớp trước khi diễn giải các số không.

:::

---

## Bài 3: Xây dựng cặp bản đồ choropleth đối chiếu giá trung vị và quy mô nguồn cung chỗ ở

<span id="data-lab-13-03"></span>

::: exercise
**Mục tiêu**: Thiết kế và kết xuất cặp bản đồ phân bố màu sắc (choropleth map) song hành từ dữ liệu hình học tổng hợp (synthetic polygon GeoDataFrame), đối chiếu trực tiếp giữa mức giá trung vị và quy mô nguồn cung chỗ ở thực tế, qua đó nhận diện và giải thích bẫy diện tích địa lý (Geographical Area Bias) mà không suy diễn thiên kiến về an toàn hay mức độ ưa chuộng.

**Dữ liệu đầu vào**:
- Bảng chỗ ở `ds`: Chứa cột `neighbourhood` và cột `price`.
- Bảng ranh giới địa lý tổng hợp `geo_synth`: Đối tượng `GeoDataFrame` chứa 6 đa giác hình chữ nhật mô phỏng 6 quận (Santiago, Providencia, Las Condes, Ñuñoa, Lo Barnechea, Pirque) được khởi tạo bằng thư viện Shapely, hệ tọa độ chuẩn EPSG:3857.

**Thao tác yêu cầu**:
1. Xây dựng hàm `plot_dual_choropleth(ds: pd.DataFrame, geo: gpd.GeoDataFrame, path: str) -> gpd.GeoDataFrame`.
2. Tính toán hai chỉ số kinh tế song song cho từng quận:
   - Mức giá trung vị (`gia`): Tính trung vị của cột `price` sau khi bỏ giá trị khuyết.
   - Số lượng cơ sở lưu trú (`n`): Đếm số dòng của từng quận.
3. Ghép hai chỉ số trên vào bảng ranh giới `geo_synth`. Quận không có chỗ ở (Pirque) phải được điền 0 cho cột `n` và giữ `NaN` cho cột `gia`.
4. Tạo khung vẽ gồm hai đồ thị con nằm cạnh nhau (`1 hàng, 2 cột`) với kích thước `figsize=(13, 5.5)`.
5. Bản đồ thứ nhất (bên trái): Thể hiện mức giá trung vị (`gia`) với dải màu ấm `YlOrRd`, thiết lập màu xám nhạt (`#e0e0e0`) cho các quận không có dữ liệu giá (`missing_kwds`).
6. Bản đồ thứ hai (bên phải): Thể hiện quy mô nguồn cung (`n`) với dải màu lam `Blues`.
7. Tắt khung trục tọa độ (`ax.set_axis_off()`) trên cả hai bản đồ, ghi nhãn tên quận và giá trị tương ứng lên tâm hình học (centroid) của từng đa giác.
8. Bổ sung tiêu đề chung và dòng chú thích phương pháp luận ở góc dưới khung tranh.
9. Kết xuất biểu đồ ra tệp hình ảnh định dạng vector SVG tại đường dẫn `path`.

**Trường hợp biên cần chú ý**: Quận Pirque không có bất kỳ chỗ ở nào nên cột giá mang giá trị `NaN`, bản đồ giá phải xử lý tô màu xám phân biệt thay vì phát sinh lỗi render.
:::

::: solution
### Hai bản đồ trả lời hai câu hỏi

Bản đồ giá cho trung vị của những chỗ ở có giá, còn bản đồ số lượng cho số dòng chỗ ở được quan sát. Một quận có trung vị cao chưa chắc có nhiều niêm yết. Các giá trị này cũng chưa cho biết số lượt đặt phòng, mức độ an toàn hay sở thích của khách.

Các đa giác trong fixture đều là hình vuông cùng diện tích. Chúng giúp kiểm tra màu và phép ghép nhưng không minh họa khác biệt diện tích thực giữa các quận. Khi dùng ranh giới thật, diện tích mảng màu có thể ảnh hưởng mức chú ý của người xem. Bản đồ số lượng bổ sung quy mô, còn muốn so sánh mật độ phải tính số lượng trên một đơn vị diện tích phù hợp.

#### Cách 1: Dựng cặp bản đồ tuần tự với Shapely Box và GeoPandas Plot

```python
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from shapely.geometry import box
import geopandas as gpd


def tao_geo_tong_hop() -> gpd.GeoDataFrame:
    """Tạo GeoDataFrame mô phỏng lưới không gian 6 quận thành phố."""
    o_luoi = [
        box(0, 1, 1, 2),  # Santiago (trung tâm nội đô)
        box(1, 1, 2, 2),  # Providencia (khu thương mại)
        box(2, 1, 3, 2),  # Las Condes (khu tài chính)
        box(0, 0, 1, 1),  # Ñuñoa (khu dân cư)
        box(1, 0, 2, 1),  # Lo Barnechea (ngoại ô diện tích lớn)
        box(2, 0, 3, 1),  # Pirque (vùng đệm ngoại vi)
    ]
    return gpd.GeoDataFrame(
        {
            "neighbourhood": [
                "Santiago",
                "Providencia",
                "Las Condes",
                "Ñuñoa",
                "Lo Barnechea",
                "Pirque",
            ],
            "neighbourhood_group": [None] * 6,
        },
        geometry=o_luoi,
        crs="EPSG:3857",
    )


def plot_dual_choropleth(
    ds: pd.DataFrame, geo: gpd.GeoDataFrame, path: str
) -> gpd.GeoDataFrame:
    """Vẽ cặp bản đồ choropleth đối chiếu giá trung vị và số lượng chỗ ở."""
    kpi_gia = (
        ds.dropna(subset=["price"])
        .groupby("neighbourhood")["price"]
        .median()
        .reset_index(name="gia")
    )
    kpi_so = ds.groupby("neighbourhood").size().reset_index(name="n")
    kpi = pd.merge(kpi_so, kpi_gia, on="neighbourhood", how="left")
    ban_do = geo.merge(kpi, on="neighbourhood", how="left")
    ban_do["n"] = ban_do["n"].fillna(0).astype(int)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Bản đồ 1: Mức giá trung vị
    ban_do.plot(
        column="gia",
        cmap="YlOrRd",
        legend=True,
        edgecolor="#444",
        linewidth=0.8,
        ax=ax1,
        missing_kwds={"color": "#e0e0e0", "label": "Không có chỗ ở"},
        legend_kwds={"label": "Giá trung vị (CLP/đêm)", "shrink": 0.7},
    )
    ax1.set_title(
        "Bản đồ 1: Mức giá trung vị theo quận", fontsize=11, fontweight="bold"
    )
    ax1.set_axis_off()

    # Bản đồ 2: Quy mô nguồn cung
    ban_do.plot(
        column="n",
        cmap="Blues",
        legend=True,
        edgecolor="#444",
        linewidth=0.8,
        ax=ax2,
        legend_kwds={"label": "Số lượng chỗ ở niêm yết (n)", "shrink": 0.7},
    )
    ax2.set_title(
        "Bản đồ 2: Quy mô nguồn cung thực tế theo quận", fontsize=11, fontweight="bold"
    )
    ax2.set_axis_off()

    # Ghi nhãn trực tiếp trên tâm hình học của từng quận
    for _, row in ban_do.iterrows():
        pt = row.geometry.centroid
        gia_str = f"{row['gia']/1000:.0f}k" if pd.notna(row["gia"]) else "Trắng"
        ax1.text(
            pt.x,
            pt.y,
            f"{row['neighbourhood']}\n{gia_str}",
            ha="center",
            va="center",
            fontsize=8,
            color="#222",
        )
        ax2.text(
            pt.x,
            pt.y,
            f"{row['neighbourhood']}\nn={row['n']}",
            ha="center",
            va="center",
            fontsize=8,
            color="#222",
        )

    fig.suptitle(
        "Cặp bản đồ đối chiếu: Phân khúc giá và Quy mô nguồn cung (Tránh bẫy diện tích địa lý)",
        fontsize=13,
        fontweight="bold",
        y=0.98,
    )
    fig.text(
        0.02,
        0.02,
        "Lưu ý phương pháp luận: Quận diện tích lớn có giá cao nhưng nguồn cung ít, không suy diễn mức độ an toàn hay độ ưa chuộng từ giá.",
        fontsize=8,
        color="#555",
    )

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return ban_do


# Dữ liệu thử nghiệm minh họa
_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)
demo_ds = pd.DataFrame(
    {
        "id": range(201, 249),
        "neighbourhood": _QUAN,
        "price": [
            (
                None
                if k % 11 == 5
                else float(18000 + (k * 7919) % 90000 + (15000 if k % 3 == 0 else 0))
            )
            for k in range(48)
        ],
    }
)
geo_synth_demo = tao_geo_tong_hop()
duong_dan_svg = "docs/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-03-cap-ban-do-gia-va-so-luong.svg"
ban_do_kq_c1 = plot_dual_choropleth(demo_ds, geo_synth_demo, duong_dan_svg)
print("Kết xuất cặp bản đồ Cách 1 thành công. Số quận trên bản đồ:", len(ban_do_kq_c1))
```

##### Giải thích chi tiết Cách 1

`box` tạo các hình chữ nhật giả lập theo bốn tọa độ góc. Gán CRS không biến chúng thành vị trí thực của các quận. Với ví dụ này, centroid chỉ dùng để đặt nhãn ở giữa ô vuông. Trên bản đồ thật, centroid có thể nằm ngoài một đa giác lõm và không phải lúc nào cũng là vị trí nhãn thích hợp.

Sau khi tổng hợp, ghép trái giữ đủ sáu quận. `missing_kwds` đặt màu xám cho giá NaN để khác với một mức giá bằng không. Hai Axes có thanh màu riêng vì giá và số đếm khác đơn vị. Khi so sánh nhiều snapshot, cần xét thêm việc giữ cùng giới hạn thang màu cho cùng một chỉ số.

##### Kết quả thực thi Cách 1

| neighbourhood | n | Giá trung vị (CLP/đêm) |
| --- | --- | --- |
| Santiago | 18 | 59271.0 |
| Providencia | 12 | 67651.0 |
| Las Condes | 8 | 87029.5 |
| Ñuñoa | 6 | 72679.0 |
| Lo Barnechea | 4 | 63314.5 |
| Pirque | 0 | NaN |

![Hình 13.2: Bản đồ choropleth phân bố nguồn cung chỗ ở theo quận](/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-02-ban-do-so-cho-o.svg)

![Hình 13.3: Cặp bản đồ đối chiếu giá trung vị và quy mô nguồn cung chỗ ở](/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-03-cap-ban-do-gia-va-so-luong.svg)

#### Cách 2: Tự động hóa thanh màu liên tục với colorbar độc lập và định dạng SVG tối ưu

```python
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as mcolors
import numpy as np
import pandas as pd
from shapely.geometry import box
import geopandas as gpd


def plot_dual_choropleth_chuyen_nghiep(
    ds: pd.DataFrame, geo: gpd.GeoDataFrame, path: str
) -> gpd.GeoDataFrame:
    """Vẽ cặp bản đồ không gian với thanh tỷ lệ màu sắc chuẩn hóa và kiểm soát ngoại biên."""
    kpi = (
        ds.groupby("neighbourhood")
        .agg(gia=("price", "median"), n=("id", "size"))
        .reset_index()
    )
    ban_do = geo.merge(kpi, on="neighbourhood", how="left")
    ban_do["n"] = ban_do["n"].fillna(0).astype(int)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    # Căn chỉnh thanh màu cho bản đồ giá
    gia_hop_le = ban_do["gia"].dropna()
    norm_gia = mcolors.Normalize(vmin=gia_hop_le.min(), vmax=gia_hop_le.max())
    cmap_gia = cm.YlOrRd
    ban_do.plot(
        column="gia",
        cmap=cmap_gia,
        norm=norm_gia,
        edgecolor="#333",
        linewidth=0.7,
        missing_kwds={"color": "#eeeeee"},
        ax=ax1,
    )
    sm1 = cm.ScalarMappable(norm=norm_gia, cmap=cmap_gia)
    fig.colorbar(
        sm1,
        ax=ax1,
        orientation="horizontal",
        fraction=0.046,
        pad=0.04,
        label="Giá trung vị (CLP)",
    )
    ax1.set_title("Phân bố mức giá trung vị", fontsize=11, fontweight="bold")
    ax1.set_axis_off()

    # Căn chỉnh thanh màu cho bản đồ số lượng chỗ ở
    norm_n = mcolors.Normalize(vmin=0, vmax=ban_do["n"].max())
    cmap_n = cm.Blues
    ban_do.plot(
        column="n", cmap=cmap_n, norm=norm_n, edgecolor="#333", linewidth=0.7, ax=ax2
    )
    sm2 = cm.ScalarMappable(norm=norm_n, cmap=cmap_n)
    fig.colorbar(
        sm2,
        ax=ax2,
        orientation="horizontal",
        fraction=0.046,
        pad=0.04,
        label="Số lượng chỗ ở (n)",
    )
    ax2.set_title("Quy mô nguồn cung chỗ ở", fontsize=11, fontweight="bold")
    ax2.set_axis_off()

    fig.suptitle(
        "Khảo sát không gian đô thị: So sánh chất lượng phân khúc và dung lượng nguồn cung",
        fontsize=12,
        fontweight="bold",
    )
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return ban_do


def tao_geo_tong_hop() -> gpd.GeoDataFrame:
    """Tạo GeoDataFrame mô phỏng lưới không gian 6 quận thành phố."""
    o_luoi = [
        box(0, 1, 1, 2),  # Santiago (trung tâm nội đô)
        box(1, 1, 2, 2),  # Providencia (khu thương mại)
        box(2, 1, 3, 2),  # Las Condes (khu tài chính)
        box(0, 0, 1, 1),  # Ñuñoa (khu dân cư)
        box(1, 0, 2, 1),  # Lo Barnechea (ngoại ô diện tích lớn)
        box(2, 0, 3, 1),  # Pirque (vùng đệm ngoại vi)
    ]
    return gpd.GeoDataFrame(
        {
            "neighbourhood": [
                "Santiago",
                "Providencia",
                "Las Condes",
                "Ñuñoa",
                "Lo Barnechea",
                "Pirque",
            ],
            "neighbourhood_group": [None] * 6,
        },
        geometry=o_luoi,
        crs="EPSG:3857",
    )


_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)

demo_ds = pd.DataFrame(
    {
        "id": range(201, 249),
        "neighbourhood": _QUAN,
        "price": [
            (
                None
                if k % 11 == 5
                else float(18000 + (k * 7919) % 90000 + (15000 if k % 3 == 0 else 0))
            )
            for k in range(48)
        ],
    }
)

# Chạy ví dụ
geo_synth_demo = tao_geo_tong_hop()
ban_do_kq_c2 = plot_dual_choropleth_chuyen_nghiep(
    demo_ds,
    geo_synth_demo,
    "docs/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-03-cap-ban-do-gia-va-so-luong.svg",
)
print(ban_do_kq_c2[["neighbourhood", "n", "gia"]].to_string(index=False))
```

##### Giải thích chi tiết Cách 2

`Normalize(vmin, vmax)` ánh xạ giá trị số lên thang màu. `ScalarMappable` cung cấp đối tượng dùng để tạo colorbar riêng của Matplotlib. Các tham số orientation, fraction và pad điều chỉnh hướng, độ lớn và khoảng cách thanh màu với bản đồ.

Những thiết lập này điều chỉnh bố cục, không đổi số liệu tổng hợp. Giá và số đếm vẫn cần hai thanh màu có nhãn đơn vị khác nhau. SVG lưu các hình và đường dưới dạng vector, nhưng chữ, chú giải và tỉ lệ bố cục vẫn cần kiểm tra ở kích thước hiển thị thực tế.

##### Kết quả thực thi Cách 2

| Quận | n | Tỷ trọng trong 48 dòng (%) | Giá trung vị (CLP) |
| --- | --- | --- | --- |
| Santiago | 18 | 37.5 | 59271.0 |
| Providencia | 12 | 25.0 | 67651.0 |
| Las Condes | 8 | 16.7 | 87029.5 |
| Ñuñoa | 6 | 12.5 | 72679.0 |
| Lo Barnechea | 4 | 8.3 | 63314.5 |
| Pirque | 0 | 0.0 | NaN |

#### So sánh hai cách

Cách 1 để GeoPandas dựng phần lớn chú giải màu. Cách 2 điều khiển colorbar bằng các đối tượng Matplotlib riêng. Cả hai phải giữ Pirque có n bằng 0 và giá NaN. Trên mẫu, Las Condes có trung vị cao nhất còn Santiago có nhiều dòng nhất.

:::

---

## Bài 4: Thống kê chuỗi thời gian số lượng đánh giá theo chu kỳ hàng năm trong khoảng xác định

<span id="data-lab-13-04"></span>

::: exercise
**Mục tiêu**: Xử lý chuỗi thời gian chứa cột ngày tháng (`datetime64`), thực hiện tổng hợp tái lấy mẫu (resample) theo tần suất kết thúc năm dương lịch (`YE`), cắt lát dữ liệu trong một khoảng thời gian xác định và bảo đảm các năm không có quan sát nhận giá trị 0.

**Dữ liệu đầu vào**:
- Bảng đánh giá `rv`: Chứa cột `date` kiểu dữ liệu thời gian chuẩn `datetime64[ns]`.
- Hai tham số chuỗi biểu thị năm bắt đầu `bat_dau` (ví dụ `"2016"`) và năm kết thúc `ket_thuc` (ví dụ `"2025"`).

**Thao tác yêu cầu**:
1. Xây dựng hàm `yearly_counts(rv: pd.DataFrame, bat_dau: str, ket_thuc: str) -> pd.Series`.
2. Chuyển cột `date` thành chỉ mục thời gian DatetimeIndex, thực hiện phép tái lấy mẫu theo chu kỳ cuối năm dương lịch bằng cú pháp `resample("YE").size()`.
3. Cắt lát chuỗi dữ liệu trong dải thời gian từ `bat_dau` đến `ket_thuc` bằng cú pháp `.loc[bat_dau:ket_thuc]`.
4. Bảo đảm chỉ mục của Series kết quả là `DatetimeIndex` với các nhãn là ngày cuối cùng của từng năm (`YYYY-12-31`).
5. Không chỉnh sửa bảng dữ liệu `rv` đầu vào.
6. Giải thích vì sao khi thống kê sản lượng hàng năm, người phân tích cần tách rõ năm hiện tại chưa kết thúc khi so sánh với tổng các năm đầy đủ (như năm 2026 với mốc chụp snapshot vào tháng 6).

**Trường hợp biên cần chú ý**: Nếu trong khoảng thời gian có một năm hoàn toàn không có đánh giá nào, hàm `resample` phải giữ nguyên năm đó với số đếm bằng 0 thay vì làm mất chỉ mục của năm.
:::

::: solution
### Đếm đánh giá theo khoảng thời gian

Mỗi bản ghi đánh giá đóng góp một đơn vị vào năm chứa ngày của nó. Số đánh giá là một đại lượng quan sát được, không đồng nhất với số lượt đặt phòng. Muốn dùng nó để ước lượng giao dịch phải bổ sung giả định về việc khách để lại đánh giá.

Để so sánh các tổng năm trọn vẹn, bài này lấy 2016–2025 và tách năm 2026 chưa kết thúc khỏi dải đó. Có thể trình bày năm chưa trọn nếu gắn nhãn rõ, hoặc so cùng kỳ giữa các năm. Không được coi tổng chưa trọn và tổng đủ năm là cùng độ dài quan sát.

#### Cách 1: Sử dụng set_index kết hợp resample và cắt lát nhãn chuỗi

```python
import pandas as pd


def yearly_counts_resample(rv: pd.DataFrame, bat_dau: str, ket_thuc: str) -> pd.Series:
    """Đếm số lượng đánh giá theo từng năm trong khoảng xác định bằng resample.

    Tham số:
        rv: DataFrame chứa cột 'date' kiểu datetime64.
        bat_dau: Chuỗi năm bắt đầu (ví dụ '2016').
        ket_thuc: Chuỗi năm kết thúc (ví dụ '2025').
    Trả về:
        Series với chỉ mục DatetimeIndex biểu thị ngày cuối năm.
    """
    chuoi_nam = rv.set_index("date").resample("YE").size()
    return chuoi_nam.loc[bat_dau:ket_thuc]


# Dữ liệu thử nghiệm minh họa
_SO_THEO_NAM = {
    2014: 40,
    2015: 70,
    2016: 120,
    2017: 210,
    2018: 330,
    2019: 420,
    2020: 90,
    2021: 150,
    2022: 380,
    2023: 520,
    2024: 610,
    2025: 700,
    2026: 260,
}
demo_rv = pd.DataFrame(
    {
        "date": [
            pd.Timestamp(f"{nam}-01-01")
            + pd.Timedelta(days=(k * 97) % (181 if nam == 2026 else 365))
            for nam, so in _SO_THEO_NAM.items()
            for k in range(so)
        ]
    }
)

nam_kq_c1 = yearly_counts_resample(demo_rv, "2016", "2025")
print("Kết quả Cách 1 (Dải năm 2016-2025):")
print(nam_kq_c1)
```

##### Giải thích chi tiết Cách 1

`set_index("date")` đưa ngày vào DatetimeIndex để resample gom theo thời gian. `resample("YE").size()` đếm số dòng trong từng năm và gắn nhãn ngày cuối năm. Một năm không có dòng nhưng nằm giữa các năm có dữ liệu vẫn có nhóm với số đếm bằng 0.

Lát cắt `.loc[bat_dau:ket_thuc]` dùng chuỗi năm và bao gồm cả hai đầu. Hàm không sửa cột date trên bảng gốc. Resample chỉ phủ dải thời gian của dữ liệu, nên nếu cần các năm yêu cầu nằm ngoài dải này, phải tạo dải chỉ mục mục tiêu rồi reindex rõ ràng.

##### Kết quả thực thi Cách 1

| Ngày chỉ mục | Số đánh giá |
| --- | --- |
| 2016-12-31 | 120 |
| 2017-12-31 | 210 |
| 2018-12-31 | 330 |
| 2019-12-31 | 420 |
| 2020-12-31 | 90 |
| 2021-12-31 | 150 |
| 2022-12-31 | 380 |
| 2023-12-31 | 520 |
| 2024-12-31 | 610 |
| 2025-12-31 | 700 |

#### Cách 2: Trích xuất thuộc tính năm kết hợp reindex dải ngày liên tục

```python
import pandas as pd


def yearly_counts_reindex(rv: pd.DataFrame, bat_dau: str, ket_thuc: str) -> pd.Series:
    """Đếm số lượng đánh giá bằng trích xuất năm và tái chỉ mục dải ngày.

    Tham số:
        rv: DataFrame chứa cột 'date'.
        bat_dau: Chuỗi năm bắt đầu.
        ket_thuc: Chuỗi năm kết thúc.
    Trả về:
        Series có chỉ mục DatetimeIndex tương đương.
    """
    counts = rv["date"].dt.year.value_counts()
    start_y, end_y = int(bat_dau), int(ket_thuc)
    full_idx = pd.date_range(start=f"{start_y}-12-31", end=f"{end_y}-12-31", freq="YE")
    s = counts.reindex(range(start_y, end_y + 1), fill_value=0).astype(int)
    s.index = full_idx
    s.index.name = "date"
    s.name = None
    return s


_SO_THEO_NAM = {
    2014: 40,
    2015: 70,
    2016: 120,
    2017: 210,
    2018: 330,
    2019: 420,
    2020: 90,
    2021: 150,
    2022: 380,
    2023: 520,
    2024: 610,
    2025: 700,
    2026: 260,
}

demo_rv = pd.DataFrame(
    {
        "date": [
            pd.Timestamp(f"{nam}-01-01")
            + pd.Timedelta(days=(k * 97) % (181 if nam == 2026 else 365))
            for nam, so in _SO_THEO_NAM.items()
            for k in range(so)
        ]
    }
)

# Kiểm thử tính đồng nhất
nam_kq_c2 = yearly_counts_reindex(demo_rv, "2016", "2025")
print(nam_kq_c2.to_string())
```

##### Giải thích chi tiết Cách 2

`.dt.year` lấy năm từ từng ngày. `value_counts()` đếm năm, còn `pd.date_range(..., freq="YE")` tạo đầy đủ các mốc cuối năm yêu cầu. Tra `counts.get(dt.year, 0)` đặt số không cho năm không có trong bảng đếm.

Tạo dải năm riêng giúp biểu thị cả năm chưa có quan sát ở đầu hoặc cuối khoảng yêu cầu, khác với chỉ cắt dải resample đã có. Cả hai cách giả định cột ngày đã là dữ liệu thời gian hợp lệ. Ngày thiếu hoặc không phân tích được cần quy tắc xử lý trước bước tổng hợp.

##### Kết quả thực thi Cách 2

| Ngày chỉ mục | Số đánh giá |
| --- | --- |
| 2016-12-31 | 120 |
| 2017-12-31 | 210 |
| 2018-12-31 | 330 |
| 2019-12-31 | 420 |
| 2020-12-31 | 90 |
| 2021-12-31 | 150 |
| 2022-12-31 | 380 |
| 2023-12-31 | 520 |
| 2024-12-31 | 610 |
| 2025-12-31 | 700 |

#### So sánh hai cách

Cách 1 bám trực tiếp thao tác gom theo thời gian của pandas. Cách 2 dựng dải năm mục tiêu rồi tra số đếm. Trên fixture, hai cách trả mười mốc cuối năm từ 2016 đến 2025. Nếu chọn riêng năm 2026, số đếm là 260 nhưng phải ghi đây là dữ liệu chưa đủ năm.

:::

---

## Bài 5: Phân tích định lượng độ lệch tăng trưởng khi chọn mốc so sánh và phản biện kỳ gốc

<span id="data-lab-13-05"></span>

::: exercise
**Mục tiêu**: Xây dựng phép tính tỷ số số đánh giá giữa một năm đích với các năm cơ sở khác nhau, phân tích hiện tượng thao túng mốc so sánh (selective baseline / cherry-picking) và giải thích thông tin bị thiếu khi chỉ xem một kỳ gốc.

**Dữ liệu đầu vào**:
- Series chuỗi thời gian `nam`: Chỉ mục là `DatetimeIndex` biểu thị ngày cuối năm, giá trị là số lượng đánh giá tích lũy của năm đó.
- Tham số `nam_cuoi`: Năm mục tiêu cần so sánh (kiểu số nguyên, ví dụ `2025`).
- Tham số `cac_moc`: Danh sách các năm cơ sở cần đối chiếu (kiểu danh sách số nguyên, ví dụ `[2020, 2019, 2016]`).

**Thao tác yêu cầu**:
1. Xây dựng hàm `compare_baselines(nam: pd.Series, nam_cuoi: int, cac_moc: list) -> dict`.
2. Trích xuất số lượng đánh giá của năm `nam_cuoi`.
3. Duyệt qua từng năm mốc trong `cac_moc`, tính tỷ số $R = a/b$. Ở đây, $a$ là số đánh giá năm cuối và $b$ là số đánh giá năm mốc, với $b > 0$.
4. Trả về từ điển có khóa là năm mốc (số nguyên) và giá trị là tỷ số tăng trưởng (số thực float chính xác, không làm tròn), bảo toàn đúng thứ tự xuất hiện của `cac_moc`.
5. Không chỉnh sửa Series `nam` đầu vào.
6. Lập bảng so sánh định lượng và giải thích vì sao việc chỉ chọn duy nhất năm 2020 làm mốc so sánh lại tạo ra một kết luận phóng đại sai lệch.

**Trường hợp biên cần chú ý**: Mọi năm trong `cac_moc` và `nam_cuoi` đều được bảo đảm có mặt trong Series `nam`. Mẫu số luôn là số nguyên dương lớn hơn 0.
:::

::: solution
### Tỷ số đúng vẫn cần nói rõ kỳ gốc

Gọi a là số đánh giá năm cuối và b là số đánh giá năm mốc. Tỷ số a chia b mô tả năm cuối bằng bao nhiêu lần năm mốc. Mức tăng phần trăm là tỷ số đó trừ 1 rồi nhân 100. Hai cách diễn đạt khác nhau, nên cần ghi rõ đang báo tỷ số hay phần trăm tăng.

Trong fixture, 700 chia 90 xấp xỉ 7,78, còn 700 chia 420 xấp xỉ 1,67. Cả hai phép chia đều đúng, nhưng trả lời hai câu hỏi với hai mốc khác nhau. Chỉ hiển thị từ năm có số đếm thấp có thể làm người đọc thiếu bối cảnh. Các số giả lập này không chứng minh tốc độ phục hồi kinh tế hoặc nguyên nhân của mức thấp năm 2020.

#### Cách 1: Vòng lặp tra cứu boolean theo chỉ mục thời gian

```python
import pandas as pd


def compare_baselines_loop(nam: pd.Series, nam_cuoi: int, cac_moc: list) -> dict:
    """Tính tỷ số tăng trưởng so với các năm mốc theo cách duyệt tuần tự.

    Tham số:
        nam: Series có chỉ mục DatetimeIndex.
        nam_cuoi: Năm đích cần so sánh.
        cac_moc: Danh sách các năm làm kỳ gốc.
    Trả về:
        Từ điển {năm_mốc: tỷ_số_float}.
    """
    val_cuoi = float(nam[nam.index.year == nam_cuoi].iloc[0])
    ket_qua = {}
    for moc in cac_moc:
        val_moc = float(nam[nam.index.year == moc].iloc[0])
        ket_qua[moc] = val_cuoi / val_moc
    return ket_qua


# Dữ liệu thử nghiệm minh họa
_SO_THEO_NAM = {
    2014: 40,
    2015: 70,
    2016: 120,
    2017: 210,
    2018: 330,
    2019: 420,
    2020: 90,
    2021: 150,
    2022: 380,
    2023: 520,
    2024: 610,
    2025: 700,
    2026: 260,
}
demo_rv = pd.DataFrame(
    {
        "date": [
            pd.Timestamp(f"{nam}-01-01")
            + pd.Timedelta(days=(k * 97) % (181 if nam == 2026 else 365))
            for nam, so in _SO_THEO_NAM.items()
            for k in range(so)
        ]
    }
)
nam_demo = demo_rv.set_index("date").resample("YE").size()

ti_le_c1 = compare_baselines_loop(nam_demo, 2025, [2020, 2019, 2016])
print("Kết quả tính toán tỷ số tăng trưởng Cách 1:")
for moc, ti_so in ti_le_c1.items():
    print(f" - Năm 2025 so với năm {moc}: {ti_so:.2f} lần (tương đương {ti_so:.4f})")
```

##### Giải thích chi tiết Cách 1

`nam.index.year == nam_cuoi` tạo mặt nạ chọn năm cuối. `.iloc[0]` lấy một giá trị trong kết quả lọc và float chuyển nó thành số thực Python. Với mỗi năm mốc, hàm lọc tương tự rồi chia giá trị cuối cho giá trị mốc.

Vòng lặp duyệt cac_moc theo thứ tự đầu vào, nên từ điển giữ thứ tự đó. Các năm trong bài đã có đủ và số mốc dương, tránh lỗi lấy phần tử rỗng hoặc chia cho không. Không làm tròn trong hàm để phép tính tiếp theo dùng đủ độ chính xác số thực đang có, rồi chỉ làm tròn khi trình bày.

##### Kết quả thực thi Cách 1

| Năm mốc | Số đánh giá năm mốc | Số năm 2025 | Tỷ số, chưa làm tròn trong hàm |
| --- | --- | --- | --- |
| 2020 | 90 | 700 | 7.777777777777778 |
| 2019 | 420 | 700 | 1.6666666666666667 |
| 2016 | 120 | 700 | 5.833333333333333 |

![Hình 13.4: Biểu đồ gốc có lỗi chọn mốc so sánh phóng đại mức tăng trưởng](/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-04-hinh-loi-chon-ky-goc.svg)

#### Cách 2: Tái lập chỉ mục số nguyên và phép chia từ điển nén (Dict Comprehension)

```python
import pandas as pd


def compare_baselines_dict(nam: pd.Series, nam_cuoi: int, cac_moc: list) -> dict:
    """Tính tỷ số tăng trưởng thông qua Series chỉ mục số nguyên năm.

    Tham số:
        nam: Series có chỉ mục DatetimeIndex.
        nam_cuoi: Năm đích cần so sánh.
        cac_moc: Danh sách các năm làm kỳ gốc.
    Trả về:
        Từ điển kết quả.
    """
    nam_int = pd.Series(nam.values, index=nam.index.year)
    val_cuoi = float(nam_int.loc[nam_cuoi])
    return {moc: val_cuoi / float(nam_int.loc[moc]) for moc in cac_moc}


_SO_THEO_NAM = {
    2014: 40,
    2015: 70,
    2016: 120,
    2017: 210,
    2018: 330,
    2019: 420,
    2020: 90,
    2021: 150,
    2022: 380,
    2023: 520,
    2024: 610,
    2025: 700,
    2026: 260,
}

demo_rv = pd.DataFrame(
    {
        "date": [
            pd.Timestamp(f"{nam}-01-01")
            + pd.Timedelta(days=(k * 97) % (181 if nam == 2026 else 365))
            for nam, so in _SO_THEO_NAM.items()
            for k in range(so)
        ]
    }
)

nam_demo = demo_rv.set_index("date").resample("YE").size()

ti_le_c2 = compare_baselines_dict(nam_demo, 2025, [2020, 2019, 2016])
print(ti_le_c2)
```

##### Giải thích chi tiết Cách 2

Tạo Series có chỉ mục là năm giúp tránh lặp lại mặt nạ so sánh trên DatetimeIndex cho mỗi mốc. Dict comprehension duyệt cac_moc và tạo các cặp năm, tỷ số trong cùng thứ tự.

Cách này giả định mỗi năm chỉ có một giá trị tổng. Nếu nhiều dòng cùng năm, tra loc có thể trả Series thay vì một số. Chỉ mục số nguyên không tự bảo đảm thời gian tra cứu hằng số trong mọi trường hợp của pandas. Khi dùng lại, cần kiểm tra tính duy nhất của năm và cùng miền dữ liệu như Cách 1.

##### Kết quả thực thi Cách 2

| Năm mốc | Số đánh giá năm mốc | Số năm 2025 | Tỷ số, chưa làm tròn trong hàm |
| --- | --- | --- | --- |
| 2020 | 90 | 700 | 7.777777777777778 |
| 2019 | 420 | 700 | 1.6666666666666667 |
| 2016 | 120 | 700 | 5.833333333333333 |

#### So sánh hai cách

Cách 1 mở rõ từng bước lọc năm và chia số. Cách 2 chuẩn bị chỉ mục theo năm một lần để tra các mốc. Không gọi tỷ lệ giữa hai tỷ số với mốc khác nhau là “hệ số dối trá” của đồ họa: Muốn đánh giá mức phóng đại hình học phải định nghĩa hiệu ứng thị giác và hiệu ứng số liệu đang so sánh.

:::

---

## Bài 6: Thiết lập biểu đồ xu hướng trung thực dài hạn và hồ sơ phản biện biểu đồ thiên lệch

<span id="data-lab-13-06"></span>

::: exercise
**Mục tiêu**: Xây dựng hàm kết xuất biểu đồ xu hướng dài hạn trung thực, khắc phục triệt để các thủ thuật cắt gọt chuỗi thời gian, đánh dấu trực quan giai đoạn khủng hoảng ngoại sinh (đại dịch COVID-19), đồng thời lập hồ sơ phản biện lỗi (Chart Critique Dossier) bóc trần sự sai lệch của biểu đồ thiên kiến.

**Dữ liệu đầu vào**:
- Series chuỗi thời gian `nam`: Chỉ mục là `DatetimeIndex` biểu thị các năm trọn vẹn (ví dụ 10 năm từ 2016 đến 2025).
- Tham số `path`: Đường dẫn tệp hình ảnh đầu ra cần lưu trữ.
- Tham số `covid`: Tuple chứa khoảng năm diễn ra đại dịch (mặc định `(2020, 2021)`).

**Thao tác yêu cầu**:
1. Xây dựng hàm `plot_fixed_trend(nam: pd.Series, path: str, covid: tuple = (2020, 2021)) -> plt.Axes`.
2. Tạo khung vẽ mới với tỷ lệ chuẩn mực `figsize=(8.5, 3.8)`.
3. Vẽ một đường duy nhất biểu diễn toàn bộ các điểm dữ liệu của `nam` với trục hoành là số nguyên năm (`nam.index.year`).
4. Đánh dấu giai đoạn đại dịch bằng vùng bóng mờ `ax.axvspan(covid[0] - 0.5, covid[1] + 0.5, color="#fee0d2", alpha=0.6)` hoặc hộp chú thích chữ nổi bật.
5. Đặt tiêu đề khoa học khách quan (độ dài $\ge 15$ ký tự, không dùng từ ngữ giật gân, phóng đại), đặt nhãn trục tung rõ ràng.
6. Lưu biểu đồ ra tệp hình ảnh theo đường dẫn `path` với chất lượng cao (`dpi=150, bbox_inches="tight"`), và trả về đối tượng `Axes`.
7. Lập hồ sơ lỗi hoàn chỉnh cho biểu đồ gốc gồm 3 luận điểm: Lỗi chọn kỳ gốc, Lỗi từ ngữ giật gân so với bản chất số liệu, và Sự khác biệt căn bản của bản sửa trung thực.

**Trường hợp biên cần chú ý**: Hàm phải vẽ đầy đủ các năm trong Series đầu vào (không được tự ý cắt xén năm), vùng tô bóng `axvspan` phải bao trọn các năm đại dịch với khoảng mở rộng $\pm 0{,}5$ đơn vị để phủ kín bề rộng cột mốc năm.
:::

::: solution
### Bổ sung bối cảnh thay vì gán nguyên nhân

Hồ sơ phản biện cần chỉ ra ba điểm. Hình bắt đầu năm 2020 bỏ các năm trước đó nên người đọc không thấy số đếm năm 2019 là 420. Tiêu đề “bùng nổ” khiến tỷ số số đánh giá dễ bị đọc thành kết luận về toàn thị trường. Bản sửa hiển thị dải 2016–2025, giữ nhãn đơn vị và chỉ rõ kỳ gốc khi nêu tỷ số.

Có thể tô giai đoạn 2020–2021 như một mốc bối cảnh. Tuy nhiên dải màu không chứng minh đại dịch gây ra biến đổi trong fixture được dựng bằng code. Với dữ liệu thật, quan sát một mức giảm cùng thời điểm sự kiện cũng chưa đủ xác định quan hệ nhân quả.

#### Cách 1: Sử dụng Matplotlib axvspan và chú giải trực quan

```python
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def plot_fixed_trend(
    nam: pd.Series, path: str, covid: tuple = (2020, 2021)
) -> plt.Axes:
    """Vẽ biểu đồ xu hướng dài hạn trung thực có đánh dấu vùng biến cố ngoại sinh.

    Tham số:
        nam: Series chuỗi thời gian số đếm theo năm.
        path: Đường dẫn lưu tệp hình ảnh.
        covid: Tuple (năm_bắt_đầu, năm_kết_thúc) của giai đoạn biến cố.
    Trả về:
        Đối tượng Axes đã vẽ.
    """
    fig, ax = plt.subplots(figsize=(8.5, 3.8))
    years = nam.index.year
    ax.plot(
        years,
        nam.values,
        marker="o",
        color="#1f77b4",
        lw=2,
        markersize=6,
        label="Số đánh giá thực tế",
    )
    ax.axvspan(
        covid[0] - 0.5,
        covid[1] + 0.5,
        color="#fee0d2",
        alpha=0.6,
        label="Giai đoạn đại dịch COVID-19",
    )
    ax.set_title(
        "Xu hướng đánh giá dài hạn giai đoạn 2016–2025: Hồi phục sau đại dịch",
        fontsize=11,
        fontweight="bold",
    )
    ax.set_xlabel("Năm")
    ax.set_ylabel("Số lượt đánh giá hàng năm")
    ax.grid(True, linestyle="--", alpha=0.5)
    ax.legend(loc="upper left")

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg", bbox_inches="tight")
    return ax


# Dữ liệu thử nghiệm minh họa
_SO_THEO_NAM = {
    2014: 40,
    2015: 70,
    2016: 120,
    2017: 210,
    2018: 330,
    2019: 420,
    2020: 90,
    2021: 150,
    2022: 380,
    2023: 520,
    2024: 610,
    2025: 700,
    2026: 260,
}
demo_rv = pd.DataFrame(
    {
        "date": [
            pd.Timestamp(f"{nam}-01-01")
            + pd.Timedelta(days=(k * 97) % (181 if nam == 2026 else 365))
            for nam, so in _SO_THEO_NAM.items()
            for k in range(so)
        ]
    }
)
nam_sua = demo_rv.set_index("date").resample("YE").size().loc["2016":"2025"]
duong_dan_sua = "docs/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-05-ban-sua-trung-thuc-xu-huong.svg"

ax_kq_c1 = plot_fixed_trend(nam_sua, duong_dan_sua)
print("Kết xuất bản sửa Cách 1 thành công:")
print(" - Tiêu đề:", ax_kq_c1.get_title())
print(" - Số điểm trên đường:", len(ax_kq_c1.lines[0].get_xdata()))
print(" - Số vùng tô bóng:", len(ax_kq_c1.patches))
plt.close(ax_kq_c1.figure)
```

##### Giải thích chi tiết Cách 1

`ax.plot` vẽ các số đếm theo năm, còn marker giúp nhận ra từng quan sát năm. `axvspan` tô một khoảng trên trục x và phủ chiều cao vùng vẽ. Cộng hoặc trừ 0.5 ở hai đầu làm vùng tô bao quanh các mốc năm tương ứng.

Tiêu đề và nhãn trục phải nói đang đếm đánh giá, không phải đặt phòng. `savefig` lưu hình tại đường dẫn yêu cầu. Dung lượng tệp không phải tiêu chí xác nhận hình đã đúng: Cần kiểm tra có đủ điểm, chữ đọc được và phần tô không che các giá trị cần xem.

##### Kết quả thực thi Cách 1

| Kiểm tra | Kết quả trên fixture |
| --- | --- |
| Khoảng năm | 2016–2025, 10 giá trị |
| Năm 2019 | 420 |
| Năm 2020 | 90 |
| Năm 2025 | 700 |
| Chỉ số | Số đánh giá hàng năm |
| Vùng tô | 2020–2021 theo tham số covid |

![Hình 13.5: Bản sửa trung thực xu hướng đánh giá dài hạn và đánh dấu biến cố đại dịch](/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-05-ban-sua-trung-thuc-xu-huong.svg)

#### Cách 2: Bổ sung chú thích văn bản trực tiếp tại các mốc trọng yếu

```python
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd


def plot_fixed_trend_nang_cao(
    nam: pd.Series, path: str, covid: tuple = (2020, 2021)
) -> plt.Axes:
    """Vẽ biểu đồ xu hướng dài hạn với các chú thích số liệu trực quan tại các mốc ngoặt."""
    fig, ax = plt.subplots(figsize=(8.5, 4))
    years = nam.index.year
    ax.plot(
        years,
        nam.values,
        color="#08519c",
        lw=2.2,
        marker="s",
        markersize=5,
        label="Số lượng đánh giá",
    )
    ax.axvspan(
        covid[0] - 0.5,
        covid[1] + 0.5,
        color="#f0f0f0",
        edgecolor="#bdbdbd",
        linestyle="--",
        label="Mốc so sánh 2020–2021",
    )

    # Ghi chú văn bản tại các mốc trọng yếu
    ax.text(
        2020.5,
        nam.loc["2020-12-31"] + 30,
        "Mốc thấp của mẫu\n(90 lượt)",
        ha="center",
        fontsize=8,
        color="#a50f15",
        fontweight="bold",
    )
    ax.text(
        2019,
        nam.loc["2019-12-31"] + 25,
        "Đỉnh trước dịch\n(420 lượt)",
        ha="center",
        fontsize=8,
        color="#045a8d",
    )
    ax.text(
        2025,
        nam.loc["2025-12-31"] - 45,
        "Hiện tại\n(700 lượt)",
        ha="center",
        fontsize=8,
        color="#045a8d",
    )

    ax.set_title(
        "Số đánh giá theo năm trong dữ liệu minh họa", fontsize=11, fontweight="bold"
    )
    ax.set_xlabel("Năm quan sát")
    ax.set_ylabel("Số lượt đánh giá trong từng năm")
    ax.set_xticks(years)
    ax.grid(True, linestyle=":", alpha=0.6)
    ax.legend(loc="upper left", frameon=True)

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg", bbox_inches="tight")
    return ax


_SO_THEO_NAM = {
    2014: 40,
    2015: 70,
    2016: 120,
    2017: 210,
    2018: 330,
    2019: 420,
    2020: 90,
    2021: 150,
    2022: 380,
    2023: 520,
    2024: 610,
    2025: 700,
    2026: 260,
}

demo_rv = pd.DataFrame(
    {
        "date": [
            pd.Timestamp(f"{nam}-01-01")
            + pd.Timedelta(days=(k * 97) % (181 if nam == 2026 else 365))
            for nam, so in _SO_THEO_NAM.items()
            for k in range(so)
        ]
    }
)

nam_sua = demo_rv.set_index("date").resample("YE").size().loc["2016":"2025"]

duong_dan_sua = "docs/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-05-ban-sua-trung-thuc-xu-huong.svg"

ax_kq_c2 = plot_fixed_trend_nang_cao(nam_sua, duong_dan_sua)
assert len(ax_kq_c2.texts) >= 3
print("Cách 2 kiểm thử thành công: Đã tạo đủ các chú thích chữ tại các mốc ngoặt.")
plt.close(ax_kq_c2.figure)
```

##### Giải thích chi tiết Cách 2

`ax.text` đặt nội dung tại một tọa độ dữ liệu để đọc trực tiếp mốc đang được thảo luận. `set_xticks(years)` dùng các năm nguyên làm vạch chia, tránh một vạch nửa năm không có ý nghĩa với các tổng năm.

Chữ gắn vào tọa độ cần được kiểm tra lại khi dữ liệu thay đổi vì có thể trùng đường hoặc nhãn khác. Viền và màu của vùng tô chỉ giúp nhận diện giai đoạn. Chúng không cung cấp bằng chứng về một nguyên nhân kinh tế hoặc trạng thái “bình thường” của thị trường.

##### Kết quả thực thi Cách 2

| Nội dung phản biện | Cách đọc bản sửa |
| --- | --- |
| Kỳ gốc | Đọc cả các năm trước 2020 và đối chiếu nhiều mốc |
| Lời diễn giải | Nêu tỷ số của số đánh giá, tránh gọi đó là mức tăng của toàn thị trường |
| Giai đoạn tô màu | Mốc bối cảnh cần nêu rõ, không phải kiểm định nhân quả |
| Điểm đánh dấu | 2019 có 420, 2020 có 90, 2025 có 700 |

#### So sánh hai cách

Cách 1 đánh dấu giai đoạn bằng vùng tô. Cách 2 bổ sung nhãn tại những mốc cần đọc chính xác. Cả hai vẫn cần kiểm tra bố cục và câu kết luận sau khi đổi dữ liệu, và không thể tự bảo đảm một diễn giải đúng chỉ bằng cách kéo dài trục thời gian.

:::

---

## Bài 7: Bài mở rộng nâng cao: Phân tích không gian đa biến kết hợp quy mô nguồn cung và tỷ lệ nhóm chủ nhà theo quận

<span id="data-lab-13-07"></span>

::: exercise
**Mục tiêu**: Xây dựng thuật toán phân tích không gian đa chiều, tích hợp song song quy mô nguồn cung chỗ ở, mức giá trung vị và tỷ lệ niêm yết thuộc nhóm chủ nhà có từ năm chỗ ở theo từng đơn vị hành chính, trực quan hóa trên bản đồ phân vùng và phân tích cơ cấu thị trường mà không suy diễn thiên kiến nhân quả.

**Dữ liệu đầu vào**:
- Bảng chỗ ở `ds`: Chứa thông tin về quận `neighbourhood`, giá `price`, mã định danh `id` và số lượng chỗ ở của chủ nhà `calculated_host_listings_count`.
- Bảng ranh giới địa lý tổng hợp `geo`: Đối tượng `GeoDataFrame` chứa ranh giới 6 quận mô phỏng.

**Thao tác yêu cầu**:
1. Xây dựng hàm `analyze_spatial_concentration(ds: pd.DataFrame, geo: gpd.GeoDataFrame, path: str) -> gpd.GeoDataFrame`.
2. Phân loại chủ nhà thành hai nhóm: `chuyen_nghiep` (từ 5 chỗ ở trở lên) và `ca_nhan` (dưới 5 chỗ ở).
3. Tổng hợp dữ liệu theo từng quận:
   - Tổng số chỗ ở (`tong_cho_o`): Đếm số lượng cơ sở lưu trú.
   - Mức giá trung vị (`gia_trung_vi`): Tính trung vị giá niêm yết (bỏ giá trị khuyết).
   - Số lượng chỗ ở chuyên nghiệp (`so_chuyen_nghiep`): Đếm số chỗ ở do chủ nhà chuyên nghiệp quản lý.
   - Tỷ lệ chuyên nghiệp hóa (`ty_le_chuyen_nghiep`): Lấy số dòng thuộc nhóm chia tổng dòng rồi nhân 100, làm tròn một chữ số thập phân.
4. Ghép toàn bộ các chỉ số trên vào bảng ranh giới `geo`. Điền 0 cho các quận trắng dữ liệu (Pirque có `tong_cho_o = 0`, `so_chuyen_nghiep = 0`, `ty_le_chuyen_nghiep = 0.0%`).
5. Trực quan hóa bản đồ phân bố tỷ lệ chuyên nghiệp hóa với dải màu tím `Purples`, ghi nhãn tên quận, tỷ lệ phần trăm và quy mô mẫu $n$ lên tâm hình học của từng quận.
6. Lưu tệp bản đồ ra đường dẫn `path` định dạng vector SVG.
7. Cảnh báo phương pháp luận: Phân tích vì sao không được phép suy diễn quan hệ nhân quả (causality), mức độ an toàn (safety) hay mức độ ưa chuộng của khách hàng từ quy mô nguồn cung hay tỷ lệ chuyên nghiệp hóa.

**Trường hợp biên cần chú ý**: Phép chia tính tỷ lệ chuyên nghiệp hóa tại các quận có 0 chỗ ở sẽ phát sinh lỗi chia cho 0 (`0 / 0 = NaN`). Code dùng `0.0%` làm quy ước hiển thị khi n bằng 0. Phải ghi rõ đây không phải một tỷ lệ quan sát được.
:::

::: solution
### Đếm dòng chỗ ở, không đếm chủ nhà độc lập

Ngưỡng từ năm chỗ ở là quy ước phân nhóm cho bài này. Mỗi dòng được xếp theo calculated_host_listings_count, rồi ta đếm số dòng thuộc nhóm đó trong từng quận. Tỷ lệ thu được là phần niêm yết gắn với nhóm quy mô từ năm chỗ ở, không phải phần trăm số chủ nhà độc lập.

Với quận không có dòng, tỷ lệ có mẫu số bằng không nên chưa xác định. Code dùng 0.0 làm quy ước hiển thị và luôn phải đặt cạnh n bằng 0 để người đọc phân biệt với một quận có quan sát nhưng không có dòng đạt ngưỡng. Giá, số lượng và tỷ lệ nhóm chưa cho phép kết luận về an toàn, sự ưa chuộng, mức độ chuyên môn hay nguyên nhân định giá.

#### Cách 1: Tổng hợp đa hàm với pandas groupby kết hợp GeoPandas Plot

```python
from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd
from shapely.geometry import box
import geopandas as gpd


def analyze_spatial_concentration(
    ds: pd.DataFrame, geo: gpd.GeoDataFrame, path: str
) -> gpd.GeoDataFrame:
    """Phân tích cấu trúc nguồn cung và mức độ chuyên nghiệp hóa theo quận."""
    rows = []
    for ten_quan, nhom in ds.groupby("neighbourhood"):
        n = len(nhom)
        so_tu_5 = int((nhom["calculated_host_listings_count"] >= 5).sum())
        rows.append(
            {
                "neighbourhood": ten_quan,
                "tong_cho_o": n,
                "gia_trung_vi": nhom["price"].median(),
                "so_chuyen_nghiep": so_tu_5,
                "ty_le_chuyen_nghiep": round(so_tu_5 / n * 100, 1),
            }
        )
    grp = pd.DataFrame(rows)

    ban_do = geo.merge(grp, on="neighbourhood", how="left")
    ban_do["tong_cho_o"] = ban_do["tong_cho_o"].fillna(0).astype(int)
    ban_do["so_chuyen_nghiep"] = ban_do["so_chuyen_nghiep"].fillna(0).astype(int)
    ban_do["ty_le_chuyen_nghiep"] = ban_do["ty_le_chuyen_nghiep"].fillna(0.0)

    fig, ax = plt.subplots(figsize=(8, 6))
    ban_do.plot(
        column="ty_le_chuyen_nghiep",
        cmap="Purples",
        legend=True,
        edgecolor="#333",
        linewidth=0.8,
        ax=ax,
        legend_kwds={
            "label": "Tỷ lệ chỗ ở có chủ nhà từ 5 niêm yết (%)",
            "shrink": 0.75,
        },
    )
    ax.set_title(
        "Cơ cấu chỗ ở theo quy mô niêm yết của chủ nhà", fontsize=11, fontweight="bold"
    )
    ax.set_axis_off()

    for _, row in ban_do.iterrows():
        pt = row.geometry.centroid
        ax.text(
            pt.x,
            pt.y,
            f"{row['neighbourhood']}\n{row['ty_le_chuyen_nghiep']:.0f}%\n(n={row['tong_cho_o']})",
            ha="center",
            va="center",
            fontsize=8,
            color="#222",
        )

    fig.text(
        0.02,
        0.02,
        "Phân tích mở rộng: Nguồn cung và cơ cấu chủ nhà, không suy diễn chất lượng hay an toàn từ quy mô.",
        fontsize=8,
        color="#555",
    )

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return ban_do


# Dữ liệu thử nghiệm minh họa
_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)
demo_ds = pd.DataFrame(
    {
        "id": range(201, 249),
        "neighbourhood": _QUAN,
        "price": [
            (
                None
                if k % 11 == 5
                else float(18000 + (k * 7919) % 90000 + (15000 if k % 3 == 0 else 0))
            )
            for k in range(48)
        ],
        "calculated_host_listings_count": [1 + (k * 5) % 9 for k in range(48)],
    }
)
o_luoi = [
    box(0, 1, 1, 2),
    box(1, 1, 2, 2),
    box(2, 1, 3, 2),
    box(0, 0, 1, 1),
    box(1, 0, 2, 1),
    box(2, 0, 3, 1),
]
geo_synth_demo = gpd.GeoDataFrame(
    {
        "neighbourhood": [
            "Santiago",
            "Providencia",
            "Las Condes",
            "Ñuñoa",
            "Lo Barnechea",
            "Pirque",
        ],
        "neighbourhood_group": [None] * 6,
    },
    geometry=o_luoi,
    crs="EPSG:3857",
)

duong_dan_ext = "docs/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-06-mo-rong-khong-gian-da-chieu.svg"
ban_do_ext_c1 = analyze_spatial_concentration(demo_ds, geo_synth_demo, duong_dan_ext)
print(
    "Kết xuất bài mở rộng Cách 1 thành công. Cột dữ liệu:", list(ban_do_ext_c1.columns)
)
```

##### Giải thích chi tiết Cách 1

Vòng lặp lấy từng nhóm quận rồi tính ba số: Số dòng, trung vị giá và số dòng có chủ nhà từ 5 niêm yết. `len(nhom)` đếm cả dòng thiếu id. `.median()` bỏ giá thiếu và phép cộng các cờ boolean đếm số dòng thỏa điều kiện. Mỗi kết quả được thêm vào danh sách `rows`, rồi chuyển thành DataFrame.

Sau ghép vào ranh giới, số đếm của Pirque được điền không, còn giá trung vị giữ NaN. Nhãn bản đồ ghi đồng thời tỷ lệ và n để không che mất nhóm nhỏ. Các phần trăm ở bảng dưới được làm tròn một chữ số, còn nhãn trong code làm tròn về số nguyên nên có thể khác mức hiển thị trong bảng.

##### Kết quả thực thi Cách 1

| Quận | n | Số dòng có chủ nhà từ 5 chỗ ở | Tỷ lệ (%) | Trung vị (CLP) |
| --- | --- | --- | --- | --- |
| Santiago | 18 | 10 | 55.6 | 59271.0 |
| Providencia | 12 | 6 | 50.0 | 67651.0 |
| Las Condes | 8 | 5 | 62.5 | 87029.5 |
| Ñuñoa | 6 | 3 | 50.0 | 72679.0 |
| Lo Barnechea | 4 | 2 | 50.0 | 63314.5 |
| Pirque | 0 | 0 | 0.0 theo quy ước | NaN |

![Hình 13.6: Phân tích không gian đa thuộc tính kết hợp quy mô nguồn cung và tỷ lệ chuyên nghiệp hóa](/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-06-mo-rong-khong-gian-da-chieu.svg)

#### Cách 2: Vector hóa tính toán ma trận phân nhóm kinh doanh

```python
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
from shapely.geometry import box


def analyze_spatial_concentration_fast(
    ds: pd.DataFrame, geo: gpd.GeoDataFrame, path: str
) -> gpd.GeoDataFrame:
    """Phân tích cấu trúc nguồn cung và mức độ chuyên nghiệp hóa theo quận."""
    ds_kieu = ds.assign(
        kieu_host=(ds["calculated_host_listings_count"] >= 5).map(
            {True: "chuyen_nghiep", False: "ca_nhan"}
        )
    )
    grp = (
        ds_kieu.groupby("neighbourhood")
        .agg(
            tong_cho_o=("id", "size"),
            gia_trung_vi=("price", "median"),
            so_chuyen_nghiep=("kieu_host", lambda s: (s == "chuyen_nghiep").sum()),
        )
        .reset_index()
    )
    grp["ty_le_chuyen_nghiep"] = (
        grp["so_chuyen_nghiep"] / grp["tong_cho_o"] * 100
    ).round(1)

    ban_do = geo.merge(grp, on="neighbourhood", how="left")
    ban_do["tong_cho_o"] = ban_do["tong_cho_o"].fillna(0).astype(int)
    ban_do["so_chuyen_nghiep"] = ban_do["so_chuyen_nghiep"].fillna(0).astype(int)
    ban_do["ty_le_chuyen_nghiep"] = ban_do["ty_le_chuyen_nghiep"].fillna(0.0)

    fig, ax = plt.subplots(figsize=(8, 6))
    ban_do.plot(
        column="ty_le_chuyen_nghiep",
        cmap="Purples",
        legend=True,
        edgecolor="#333",
        linewidth=0.8,
        ax=ax,
        legend_kwds={
            "label": "Tỷ lệ chỗ ở có chủ nhà từ 5 niêm yết (%)",
            "shrink": 0.75,
        },
    )
    ax.set_title(
        "Cơ cấu chỗ ở theo quy mô niêm yết của chủ nhà", fontsize=11, fontweight="bold"
    )
    ax.set_axis_off()

    for _, row in ban_do.iterrows():
        pt = row.geometry.centroid
        ax.text(
            pt.x,
            pt.y,
            f"{row['neighbourhood']}\n{row['ty_le_chuyen_nghiep']:.0f}%\n(n={row['tong_cho_o']})",
            ha="center",
            va="center",
            fontsize=8,
            color="#222",
        )

    fig.text(
        0.02,
        0.02,
        "Phân tích mở rộng: Nguồn cung và cơ cấu chủ nhà, không suy diễn chất lượng hay an toàn từ quy mô.",
        fontsize=8,
        color="#555",
    )

    Path(path).parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, format="svg", bbox_inches="tight")
    plt.close(fig)
    return ban_do


_QUAN = (
    ["Santiago"] * 18
    + ["Providencia"] * 12
    + ["Las Condes"] * 8
    + ["Ñuñoa"] * 6
    + ["Lo Barnechea"] * 4
)

demo_ds = pd.DataFrame(
    {
        "id": range(201, 249),
        "neighbourhood": _QUAN,
        "price": [
            (
                None
                if k % 11 == 5
                else float(18000 + (k * 7919) % 90000 + (15000 if k % 3 == 0 else 0))
            )
            for k in range(48)
        ],
        "calculated_host_listings_count": [1 + (k * 5) % 9 for k in range(48)],
    }
)

o_luoi = [
    box(0, 1, 1, 2),
    box(1, 1, 2, 2),
    box(2, 1, 3, 2),
    box(0, 0, 1, 1),
    box(1, 0, 2, 1),
    box(2, 0, 3, 1),
]

geo_synth_demo = gpd.GeoDataFrame(
    {
        "neighbourhood": [
            "Santiago",
            "Providencia",
            "Las Condes",
            "Ñuñoa",
            "Lo Barnechea",
            "Pirque",
        ],
        "neighbourhood_group": [None] * 6,
    },
    geometry=o_luoi,
    crs="EPSG:3857",
)

duong_dan_ext = "docs/xu-ly-du-lieu/bai-giang/img/labs/lab-13/hinh-13-06-mo-rong-khong-gian-da-chieu.svg"

ban_do_ext_c2 = analyze_spatial_concentration_fast(
    demo_ds, geo_synth_demo, duong_dan_ext
)
print(ban_do_ext_c2.drop(columns="geometry").to_string(index=False))


def phan_nhom_chien_luoc_khong_gian(ban_do_ext: gpd.GeoDataFrame) -> pd.DataFrame:
    """Phân loại các quận vào ma trận chiến lược nguồn cung và chuyên nghiệp hóa."""
    df_quan = ban_do_ext.dropna(subset=["gia_trung_vi"]).copy()
    nguong_n = df_quan["tong_cho_o"].median()
    nguong_pro = df_quan["ty_le_chuyen_nghiep"].median()

    dieu_kien = [
        (df_quan["tong_cho_o"] >= nguong_n)
        & (df_quan["ty_le_chuyen_nghiep"] >= nguong_pro),
        (df_quan["tong_cho_o"] >= nguong_n)
        & (df_quan["ty_le_chuyen_nghiep"] < nguong_pro),
        (df_quan["tong_cho_o"] < nguong_n)
        & (df_quan["ty_le_chuyen_nghiep"] >= nguong_pro),
        (df_quan["tong_cho_o"] < nguong_n)
        & (df_quan["ty_le_chuyen_nghiep"] < nguong_pro),
    ]
    nhan_nhom = [
        "Quy mô lớn - Tỷ lệ từ ngưỡng trở lên",
        "Quy mô lớn - Tỷ lệ dưới ngưỡng",
        "Quy mô nhỏ - Tỷ lệ từ ngưỡng trở lên",
        "Quy mô nhỏ - Tỷ lệ dưới ngưỡng",
    ]
    df_quan["nhom_chien_luoc"] = np.select(
        dieu_kien, nhan_nhom, default="Chưa xác định"
    )
    return df_quan[
        [
            "neighbourhood",
            "tong_cho_o",
            "ty_le_chuyen_nghiep",
            "gia_trung_vi",
            "nhom_chien_luoc",
        ]
    ]


df_chien_luoc = phan_nhom_chien_luoc_khong_gian(ban_do_ext_c2)
print("Bảng phân nhóm chiến lược không gian:")
print(df_chien_luoc)
```

##### Giải thích chi tiết Cách 2

Hàm `analyze_spatial_concentration_fast` dùng named aggregation để tính cả ba chỉ số trong một phép nhóm. Phép `size` đếm dòng, `median` bỏ giá thiếu, còn hàm đếm cờ xác định số dòng đạt ngưỡng quy mô. Sau đó, ghép vào các đa giác và vẽ cùng chỉ số như Cách 1. Sau khi có bảng quận, phần phân loại là một bước mở rộng: Lấy trung vị của số dòng và trung vị của tỷ lệ nhóm trong các quận có giá làm hai ngưỡng rồi xét bốn tổ hợp cao/thấp.

`np.select` gán nhãn cho từng dòng theo các mặt nạ điều kiện. Ngưỡng phụ thuộc chính các quận được đưa vào, nên đây là một cách phân nhóm mô tả, không phải tiêu chuẩn nghề nghiệp hay khuyến nghị đầu tư. Với fixture, ngưỡng số dòng là 8 và ngưỡng tỷ lệ là 50.0. Dấu >= khiến các giá trị bằng ngưỡng thuộc phía cao.

##### Kết quả thực thi Cách 2

| Quận | n | Tỷ lệ nhóm từ 5 chỗ ở (%) | Phân nhóm theo hai ngưỡng |
| --- | --- | --- | --- |
| Santiago | 18 | 55.6 | Quy mô lớn, tỷ lệ từ ngưỡng trở lên |
| Providencia | 12 | 50.0 | Quy mô lớn, tỷ lệ từ ngưỡng trở lên |
| Las Condes | 8 | 62.5 | Quy mô lớn, tỷ lệ từ ngưỡng trở lên |
| Ñuñoa | 6 | 50.0 | Quy mô nhỏ, tỷ lệ từ ngưỡng trở lên |
| Lo Barnechea | 4 | 50.0 | Quy mô nhỏ, tỷ lệ từ ngưỡng trở lên |

Pirque có giá NaN nên bị loại khỏi bước phân nhóm mở rộng. Không có quận nào ở phía tỷ lệ dưới 50.0 trong fixture này.

#### So sánh hai cách

Bảng và bản đồ trả lời quy mô, giá và cơ cấu của từng quận. Bước phân nhóm thêm một nhãn tóm tắt theo hai ngưỡng của mẫu. Nhãn không đưa thêm bằng chứng về đặc điểm đô thị, kiểu khách hoặc hiệu quả kinh doanh. Dùng np.select không tự chứng minh cách này nhanh hơn nếu chưa đo.

:::

---

## Tài liệu tham khảo

- [IAI: Notebook thực hành](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
- [seaborn: Hàm boxplot](https://seaborn.pydata.org/generated/seaborn.boxplot.html).
- [GeoPandas: Vẽ bản đồ](https://geopandas.org/en/stable/docs/user_guide/mapping.html).
- [pandas: Tổng hợp dữ liệu theo thời gian](https://pandas.pydata.org/docs/user_guide/timeseries.html#resampling).
- [Inside Airbnb: Dữ liệu Santiago](https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv).
