## Lab 4: Lập hồ sơ phân tích một quận bằng pandas

Một bảng niêm yết chứa nhiều quận, loại phòng và mức giá. Ta sẽ lọc riêng một quận, lập hồ sơ giá và cơ cấu phòng, rồi kiểm tra ảnh hưởng của các ô thiếu. Mỗi phép tính đều được đối chiếu trên dữ liệu nhỏ trước khi dùng với snapshot đầy đủ.

---

## 1. Mục tiêu và bối cảnh thực tế

Xét bài toán thực tế: Một nhà đầu tư cần bản hồ sơ cô đọng về thị trường quận Ñuñoa thuộc vùng đô thị Santiago de Chile. Bản hồ sơ cần giải đáp: Quy mô nguồn cung của quận là bao nhiêu, giá thuê so với mặt bằng toàn thành phố cao hay thấp, cơ cấu phòng tập trung ở loại hình nào, và dữ liệu có điểm dị biệt hay giá trị khuyết nào ảnh hưởng đến quyết định đầu tư.

### Mục tiêu kỹ thuật cốt lõi
1. Thói quen 5 bước khám phá dữ liệu: Thực thi các lệnh tổng quan ban đầu và rút trích trực tiếp số liệu định lượng từ kết quả đầu ra, thay vì chỉ quan sát thụ động.
2. Trích xuất và lọc đa điều kiện: Phân biệt chính xác giữa `df["cột"]` (trả về Series), `df[["cột1", "cột2"]]` (trả về DataFrame), `df[mask]` (lọc hàng) và `df.loc[mask, "cột"]` (truy xuất đúng ô cần thao tác), đồng thời kết hợp nhiều điều kiện logic bằng toán tử bitwise `&` và phương thức `nsmallest`.
3. Cập nhật dữ liệu an toàn và đồng bộ cột phụ thuộc: Sử dụng `.loc[hàng, cột]` để sửa đổi bảng dữ liệu an toàn, hiểu rõ nguyên lý một cột trong DataFrame chỉ lưu trữ giá trị tĩnh đã tính toán chứ không tự động cập nhật như ô tính bảng tính.
4. Phân tích tác động của dữ liệu khuyết (NaN): Tính toán tỷ lệ dựa trên giá trị boolean và phân biệt rõ vai trò của mẫu số, tránh ngộ nhận khi dữ liệu chứa giá trị thiếu.
5. Đóng gói xuất bản và kiểm chứng bất biến: Xuất kết quả phân tích ra tệp CSV chuẩn hóa, đọc lại tệp và kiểm tra tính toàn vẹn dữ liệu thông qua các phép kiểm bất biến độc lập.

---

## 2. Dữ liệu thực hành và thiết lập môi trường

Để bảo đảm toàn bộ quy trình thực hành có thể chạy độc lập, bài thực hành sử dụng bộ dữ liệu mẫu gồm 12 dòng (`DEMO`, đơn vị giá: CLP/đêm). Bộ dữ liệu nhỏ này phản ánh đầy đủ các đặc tính của dữ liệu thực tế: Nhiều quận khác nhau, đa dạng loại phòng, chứa dữ liệu khuyết (`NaN`) và có giá trị ngoại lai.

Trong pandas 3, cơ chế Copy-on-Write (CoW) đã trở thành hành vi mặc định của toàn bộ thư viện, bảo đảm các đối tượng dẫn xuất hành xử độc lập khi ghi mà không cần thiết lập tùy chọn thủ công.

```python
import numpy as np
import pandas as pd
from IPython.display import display

# Địa chỉ lưu trữ snapshot thực tế phục vụ đối chiếu và mở rộng
SNAPSHOT_URL = (
    "https://data.insideairbnb.com/chile/rm/santiago/"
    "2026-06-29/visualisations/listings.csv"
)

# 12 dòng dữ liệu mẫu giả lập (đơn vị: CLP/đêm)
DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()
```

`ds_quan` giữ sáu dòng của Ñuñoa để dùng trong các bài tiếp theo. Trong Jupyter, `display(bang)` hiển thị DataFrame thành bảng có tên cột và chỉ mục. Các bảng kết quả dưới lời giải dùng cùng dữ liệu này.
> [!NOTE]
> **Đối chiếu thực tế**: Khi phân tích trên snapshot thực tế Santiago (18.534 dòng, 19 cột), toàn bộ thành phố có 846 chỗ ở khuyết giá. Riêng quận Ñuñoa chiếm 1.813 chỗ ở (khoảng 9,8% thị trường), với trung vị giá toàn quận đạt 60.981 CLP. Các con số đối chiếu thực tế được đưa vào nhằm giúp bạn kiểm chứng tính mở rộng của thuật toán, tuyệt đối không dùng làm hằng số cứng trong mã nguồn giải thuật.

---

## 3. Nội dung chi tiết bộ bài tập thực hành

<span id="data-lab-04-01"></span>
### Bài tập 1: Trích xuất cột, lọc hàng và tính tỷ lệ trên bảng dữ liệu

::: exercise Chọn cột, chọn hàng và tính tỷ lệ
Cho một DataFrame `df` chứa ít nhất ba cột: `name`, `room_type` và `price` (kiểu số thực, có thể chứa giá trị khuyết `NaN`). Hãy viết hàm `select_basics(df)` trả về một từ điển (`dict`) gồm đúng 5 khóa sau:
1. `cot_gia`: Đối tượng Series chứa dữ liệu của cột `price`.
2. `bang_con`: Đối tượng DataFrame gồm đúng hai cột `name` và `price` theo đúng thứ tự đó.
3. `ty_le_private`: Một số thực (`float`) biểu diễn tỷ lệ các dòng có `room_type == "Private room"` trên tổng số dòng của bảng.
4. `nguyen_can`: Đối tượng DataFrame chứa tất cả các dòng có `room_type == "Entire home/apt"` với đầy đủ các cột ban đầu, được trích xuất bằng cú pháp mặt nạ `df[mask]`.
5. `gia_nguyen_can`: Đối tượng Series chứa giá trị cột `price` của đúng các dòng nguyên căn nói trên, được trích xuất bằng cú pháp `.loc[mask, "price"]`.

Yêu cầu kỹ thuật: Giữ nguyên chỉ mục dòng (`index`) và thứ tự gốc của DataFrame. Không được làm biến đổi dữ liệu trên `df` truyền vào.
:::

::: solution
#### Cách 1: Trích xuất trực tiếp bằng chỉ mục và mặt nạ boolean cơ bản

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def select_basics(df: pd.DataFrame) -> dict:
    # 1. Trích xuất một cột trả về đối tượng Series
    cot_gia = df["price"]

    # 2. Truyền một danh sách tên cột để trích xuất DataFrame con
    bang_con = df[["name", "price"]]

    # 3. Tính tỷ lệ bằng cách lấy trung bình cộng trên mảng boolean
    ty_le_private = float((df["room_type"] == "Private room").mean())

    # 4. Lọc hàng bằng cú pháp ngoặc vuông với mặt nạ điều kiện
    mask_nc = df["room_type"] == "Entire home/apt"
    nguyen_can = df[mask_nc]

    # 5. Truy xuất chính xác cột mục tiêu của các hàng thỏa mãn bằng .loc
    gia_nguyen_can = df.loc[mask_nc, "price"]

    return {
        "cot_gia": cot_gia,
        "bang_con": bang_con,
        "ty_le_private": ty_le_private,
        "nguyen_can": nguyen_can,
        "gia_nguyen_can": gia_nguyen_can,
    }


ket_qua = select_basics(DEMO)
display(ket_qua["bang_con"])
print("Tỷ lệ phòng riêng:", ket_qua["ty_le_private"])

# Kết thúc lời giải
```

#### Giải thích cách 1

Một tên cột trong `df["price"]` chọn một Series, còn danh sách tên trong `df[["name", "price"]]` chọn DataFrame hai cột. Dấu ngoặc ngoài là thao tác chọn, danh sách bên trong xác định thứ tự cột. Hai kết quả giữ chỉ mục dòng ban đầu.

`df["room_type"] == "Private room"` tạo Series Boolean. Lấy `mean()` của nó cho tỷ lệ vì mỗi True đóng góp `1`, mỗi False đóng góp `0`. Mẫu có bốn phòng riêng trên mười hai dòng, nên tỷ lệ bằng một phần ba. Mặt nạ `mask_nc` chọn nguyên căn. `df[mask_nc]` giữ đủ cột, còn `.loc[mask_nc, "price"]` chỉ lấy giá tại các dòng đó.

#### Kết quả cách 1

| index | name | price |
| --- | --- | --- |
| 0 | Depto Plaza Ñuñoa | 45000.0 |
| 1 | Pieza cerca metro | 18000.0 |
| 2 | Loft Irarrázaval | 72000.0 |
| 3 | Depto sin price | NaN |
| 4 | Dormitorio simple | 2500.0 |
| 5 | Casa familiar | 60000.0 |
| 6 | Studio Providencia | 80000.0 |
| 7 | Pieza Providencia | 30000.0 |
| 8 | Depto Centro | 40000.0 |
| 9 | Hostal Centro | 12000.0 |
| 10 | Pieza Centro | NaN |
| 11 | Hotel boutique | 95000.0 |

Dòng in riêng là `Tỷ lệ phòng riêng: 0.3333333333333333`. `cot_gia` có shape `(12,)`, `bang_con` có shape `(12, 2)`, `nguyen_can` có shape `(6, 6)` và `gia_nguyen_can` có shape `(6,)`.

#### Cách 2: Sử dụng các phương thức tường minh và chuẩn hóa chỉ mục

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def select_basics(df: pd.DataFrame) -> dict:
    # Truy xuất tường minh trục hàng và cột bằng .loc
    cot_gia = df.loc[:, "price"]

    # Sử dụng filter để trích xuất danh sách cột một cách an toàn
    bang_con = df.filter(items=["name", "price"])

    # Sử dụng phương thức so sánh .eq() để tạo Series boolean
    mask_private = df["room_type"].eq("Private room")
    ty_le_private = float(mask_private.mean())

    # Xác định các hàng nguyên căn và lọc theo lát cắt
    mask_entire = df["room_type"].eq("Entire home/apt")
    nguyen_can = df.loc[mask_entire]
    gia_nguyen_can = df.loc[mask_entire, "price"]

    return {
        "cot_gia": cot_gia,
        "bang_con": bang_con,
        "ty_le_private": ty_le_private,
        "nguyen_can": nguyen_can,
        "gia_nguyen_can": gia_nguyen_can,
    }


ket_qua = select_basics(DEMO)
display(ket_qua["bang_con"])
print("Tỷ lệ phòng riêng:", ket_qua["ty_le_private"])

# Kết thúc lời giải
```

#### Giải thích cách 2

`.loc[:, "price"]` chọn mọi hàng và một cột, nên trả Series. `filter(items=["name", "price"])` chọn cột theo tên và thứ tự trong danh sách. Khác cú pháp ngoặc vuông với danh sách, filter bỏ qua tên cột không có. Bài này đã bảo đảm có đủ cột, nên hai cách trả cùng bảng.

`.eq("Private room")` là phương thức so sánh bằng, tương đương biểu thức `==` ở đây. Mặt nạ nguyên căn được dùng lại cho cả bảng đầy đủ và Series giá. Kết quả trả về trong từ điển giữ riêng các đối tượng có vai trò khác nhau. Hàm chỉ đọc, không gán vào df nên không thay đổi các giá trị của bảng truyền vào.

#### Kết quả cách 2

| index | name | price |
| --- | --- | --- |
| 0 | Depto Plaza Ñuñoa | 45000.0 |
| 1 | Pieza cerca metro | 18000.0 |
| 2 | Loft Irarrázaval | 72000.0 |
| 3 | Depto sin price | NaN |
| 4 | Dormitorio simple | 2500.0 |
| 5 | Casa familiar | 60000.0 |
| 6 | Studio Providencia | 80000.0 |
| 7 | Pieza Providencia | 30000.0 |
| 8 | Depto Centro | 40000.0 |
| 9 | Hostal Centro | 12000.0 |
| 10 | Pieza Centro | NaN |
| 11 | Hotel boutique | 95000.0 |

`ty_le_private` bằng `0.3333333333333333`. Các chỉ mục của sáu dòng nguyên căn là `0, 2, 3, 5, 6, 8`.

#### So sánh hai cách

Hai cách cùng chọn cột, lọc dòng và tính tỷ lệ. Cách 1 phù hợp khi học những cú pháp cơ bản. Cách 2 dùng phương thức có tên và chỉ rõ trục chọn bằng loc. Sự ngắn dài của câu lệnh không tạo một bằng chứng về tốc độ.

:::

---

<span id="data-lab-04-02"></span>
### Bài tập 2: Thói quen 5 bước khám phá dữ liệu và rút trích chỉ số thống kê

::: exercise Khám phá tổng quan bảng dữ liệu
Khi tiếp cận một tập dữ liệu bảng mới, một chuyên viên xử lý dữ liệu cần thực hiện thói quen 5 bước tiêu chuẩn:
1. Kiểm tra kích thước bảng qua thuộc tính `.shape`.
2. Lấy mẫu ngẫu nhiên các dòng bằng `.sample()`.
3. Kiểm tra kiểu dữ liệu và số lượng giá trị hợp lệ bằng `.info()`.
4. Xem bảng tóm tắt thống kê mô tả phân phối giá bằng `.describe()`.
5. Đếm phân bố tần suất của các loại hình chỗ ở bằng `.value_counts()`.

Hãy viết hàm `extract_5step_metrics(df)` nhận vào DataFrame và tự động rút trích ra 4 chỉ số dưới dạng từ điển:
- `so_dong`: Tổng số dòng của bảng dữ liệu.
- `so_cot`: Tổng số cột của bảng dữ liệu.
- `so_thieu_price`: Số lượng ô bị khuyết giá trị trong cột `price`.
- `so_loai_phong`: Số lượng các loại hình phòng khác nhau xuất hiện trong cột `room_type`.
:::

::: solution
#### Cách 1: Sử dụng các thuộc tính và hàm tính toán cơ bản

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def extract_5step_metrics(df: pd.DataFrame) -> dict:
    # Bước 1: Rút trích số dòng và số cột từ shape
    so_dong = len(df)
    so_cot = df.shape[1]

    # Bước 2 & 3: Đếm số giá trị khuyết bằng isna()
    so_thieu_price = int(df["price"].isna().sum())

    # Bước 4 & 5: Đếm số lượng loại phòng phân biệt qua value_counts()
    so_loai_phong = len(df["room_type"].value_counts())

    return {
        "so_dong": so_dong,
        "so_cot": so_cot,
        "so_thieu_price": so_thieu_price,
        "so_loai_phong": so_loai_phong,
    }


display(pd.DataFrame([extract_5step_metrics(DEMO)]))

# Kết thúc lời giải
```

#### Giải thích cách 1

`len(df)` đếm số dòng và `df.shape[1]` đọc số cột. `df["price"].isna()` tạo mặt nạ giá thiếu, còn `.sum()` cộng số vị trí True. Có hai giá thiếu, ở chỉ mục `3` và `10`, nên `so_thieu_price` bằng `2`.

`value_counts()` tạo một số đếm cho mỗi loại phòng xuất hiện. Lấy `len` của Series đếm cho số loại, bằng `4` trên cột chuỗi trong mẫu. Các kiểu `int` trong từ điển giúp người dùng sau này nhận số đếm thông thường. Bảng này tóm tắt bốn chỉ số, không thay thế việc xem mẫu bằng sample, kiểu bằng info và phân phối bằng describe.

#### Kết quả cách 1

| so_dong | so_cot | so_thieu_price | so_loai_phong |
| --- | --- | --- | --- |
| 12 | 6 | 2 | 4 |

#### Cách 2: Đọc trực tiếp kích thước và đếm giá trị phân biệt bằng nunique

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def extract_5step_metrics(df: pd.DataFrame) -> dict:
    # Rút trích trực tiếp bộ kích thước bảng
    n_rows, n_cols = df.shape

    # Đếm số lượng ô rỗng bằng isnull()
    missing_price = int(df["price"].isnull().sum())

    # Sử dụng nunique() để đếm số giá trị phân biệt
    n_room_types = int(df["room_type"].nunique())

    return {
        "so_dong": n_rows,
        "so_cot": n_cols,
        "so_thieu_price": missing_price,
        "so_loai_phong": n_room_types,
    }


display(pd.DataFrame([extract_5step_metrics(DEMO)]))

# Kết thúc lời giải
```

#### Giải thích cách 2

`n_rows, n_cols = df.shape` tách tuple kích thước thành hai số. `isnull()` là tên khác của `isna()`, nên cho cùng mặt nạ thiếu. Hàm `.nunique()` đếm số giá trị phân biệt, mặc định bỏ qua giá trị thiếu, trả số loại trực tiếp mà không cần lập bảng tần suất đầy đủ.

Chọn nunique khi chỉ cần số loại giúp câu lệnh thể hiện đúng mục tiêu. Chọn value_counts khi còn cần biết số lượng từng loại. Với cột phân loại categorical có các mức chưa xuất hiện, cần để ý miền danh mục khi so sánh với độ dài một bảng đếm. Dữ liệu mẫu dùng các chuỗi thực sự xuất hiện nên hai phép đếm loại khớp nhau.

#### Kết quả cách 2

| so_dong | so_cot | so_thieu_price | so_loai_phong |
| --- | --- | --- | --- |
| 12 | 6 | 2 | 4 |

#### So sánh hai cách

Cách 1 tận dụng bảng tần suất để đếm loại. Cách 2 hỏi trực tiếp số giá trị phân biệt qua nunique. Cả hai trả cùng bốn chỉ số trên DEMO. Chưa có bước nào trong hai hàm tự kiểm tra chất lượng của mọi cột hoặc tính đủ mọi thống kê thăm dò.

:::

---

<span id="data-lab-04-03"></span>
### Bài tập 3: Lọc hồ sơ theo quận và tính tỷ trọng thị trường

::: exercise Cắt riêng bảng dữ liệu quận mục tiêu
Viết hàm `filter_district(df: pd.DataFrame, ten_quan: str) -> dict` để trích xuất toàn bộ dữ liệu của một quận cụ thể và đo lường quy mô của quận đó trong toàn thành phố.

Hàm nhận vào DataFrame `df` và chuỗi tên quận `ten_quan` (ví dụ: `"Ñuñoa"`). Kết quả trả về là một từ điển gồm đúng hai khóa:
- `bang`: Đối tượng DataFrame gồm toàn bộ các dòng thuộc về quận được chỉ định, giữ nguyên đầy đủ mọi cột ban đầu cũng như chỉ mục gốc.
- `ty_trong`: Số thực biểu diễn tỷ lệ số chỗ ở của quận đó so với tổng số chỗ ở của toàn bảng `df`.

Trường hợp biên: Nếu tên quận không tồn tại trong bảng dữ liệu, khóa `bang` phải trả về một DataFrame rỗng nhưng vẫn giữ nguyên vẹn cấu trúc các cột của bảng gốc, và `ty_trong` có giá trị là `0.0`. Không được làm thay đổi DataFrame đầu vào.
:::

::: solution
#### Cách 1: Sử dụng phép so sánh mảng chuỗi truyền thống

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def filter_district(df: pd.DataFrame, ten_quan: str) -> dict:
    # Tạo mặt nạ lọc theo tên quận
    mask = df["neighbourhood"] == ten_quan
    bang = df[mask]

    # Tính tỷ trọng thị trường an toàn khi bảng có dữ liệu
    tong_so = len(df)
    ty_trong = float(len(bang) / tong_so) if tong_so > 0 else 0.0

    return {"bang": bang, "ty_trong": ty_trong}


ket_qua = filter_district(DEMO, "Ñuñoa")
display(ket_qua["bang"][["id", "room_type", "price"]])
print("Tỷ trọng chỗ ở:", ket_qua["ty_trong"])

# Kết thúc lời giải
```

#### Giải thích cách 1

Mặt nạ `df["neighbourhood"] == ten_quan` có một giá trị Boolean cho mỗi dòng. `df[mask]` giữ các dòng True với toàn bộ cột và chỉ mục gốc. Với tên `Ñuñoa`, sáu dòng đầu của DEMO được chọn.

Tỷ trọng lấy `len(bang)` chia `len(df)`, tức `6 / 12 = 0.5` trên tập mẫu. Điều kiện `tong_so > 0` tránh chia cho không nếu bảng đầu vào rỗng. Nếu tên quận không tồn tại, phép lọc trả bảng không dòng nhưng vẫn giữ cấu trúc các cột, và số dòng được chọn bằng `0` nên tỷ trọng cũng bằng `0.0`.

#### Kết quả cách 1

| index | id | room_type | price |
| --- | --- | --- | --- |
| 0 | 101 | Entire home/apt | 45000.0 |
| 1 | 102 | Private room | 18000.0 |
| 2 | 103 | Entire home/apt | 72000.0 |
| 3 | 104 | Entire home/apt | NaN |
| 4 | 105 | Private room | 2500.0 |
| 5 | 106 | Entire home/apt | 60000.0 |

Dòng in riêng là `Tỷ trọng chỗ ở: 0.5`. Hàm giữ cả sáu cột trong `bang`, bảng trên chỉ hiển thị ba cột để đối chiếu.

#### Cách 2: Sử dụng phương thức .eq() và tính trung bình trực tiếp trên mặt nạ boolean

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def filter_district(df: pd.DataFrame, ten_quan: str) -> dict:
    # Sử dụng .eq() để tạo Series boolean
    mask = df["neighbourhood"].eq(ten_quan)
    bang = df.loc[mask]

    # Lấy trung bình cộng của mặt nạ boolean để có ngay tỷ trọng
    ty_trong = float(mask.mean()) if len(df) > 0 else 0.0

    return {"bang": bang, "ty_trong": ty_trong}


ket_qua = filter_district(DEMO, "Ñuñoa")
display(ket_qua["bang"][["id", "room_type", "price"]])
print("Tỷ trọng chỗ ở:", ket_qua["ty_trong"])

# Kết thúc lời giải
```

#### Giải thích cách 2

`.eq(ten_quan)` tạo cùng mặt nạ so sánh tên, và `.loc[mask]` ghi rõ rằng mặt nạ dùng cho trục hàng. `mask.mean()` tính tỷ lệ số dòng True trong toàn bảng, tương đương số dòng quận chia tổng số dòng vì cột tên quận của mẫu không khuyết.

Nhánh `len(df) > 0` đặt tỷ trọng `0.0` khi không có dòng. Hàm không tự chuẩn hóa tên, nên khác dấu, khoảng trắng hoặc cách viết vẫn có thể không khớp. `Ñuñoa` cần được truyền đúng như dữ liệu. Kết quả không đặt lại chỉ mục, giúp truy về dòng gốc khi rà soát.

#### Kết quả cách 2

| index | id | room_type | price |
| --- | --- | --- | --- |
| 0 | 101 | Entire home/apt | 45000.0 |
| 1 | 102 | Private room | 18000.0 |
| 2 | 103 | Entire home/apt | 72000.0 |
| 3 | 104 | Entire home/apt | NaN |
| 4 | 105 | Private room | 2500.0 |
| 5 | 106 | Entire home/apt | 60000.0 |

`ty_trong` bằng `0.5`, tức `50%` của DEMO, không phải `50%` thị trường Santiago.

#### So sánh hai cách

Cách 1 tính tử số và mẫu số bằng số dòng. Cách 2 lấy trung bình của chính mặt nạ chọn. Hai cách tương đương trên cột tên quận không thiếu của mẫu. Khi dữ liệu tên quận có thiếu, cần thống nhất cách tính mẫu số trước khi dùng mẹo Boolean.

:::

---

<span id="data-lab-04-04"></span>
### Bài tập 4: Lọc kết hợp đa điều kiện logic bằng toán tử bitwise

::: exercise Đếm số chỗ ở phân khúc cạnh tranh mục tiêu
Nhà đầu tư đặt câu hỏi cụ thể: *"Tại quận Ñuñoa, hiện có bao nhiêu căn **nguyên căn** với mức giá thuê **từ 60.000 CLP trở xuống** mỗi đêm?"*

Hãy viết hàm `count_segment(listings: pd.DataFrame, room_type: str = "Entire home/apt", gia_toi_da: float = 60000.0) -> int`.
Hàm nhận vào DataFrame của một quận (chứa các cột `room_type` và `price`) cùng hai tham số ngưỡng lọc. Kết quả trả về là một số nguyên (`int`): Số lượng dòng thỏa mãn đồng thời cả hai điều kiện:
1. Cột `room_type` có giá trị đúng bằng tham số truyền vào.
2. Cột `price` có giá trị nhỏ hơn hoặc bằng `gia_toi_da`.

Ràng buộc kỹ thuật: Các chỗ ở bị khuyết giá (`NaN`) tuyệt đối không được tính vào kết quả. Nếu bảng đầu vào rỗng, hàm trả về 0. Bắt buộc sử dụng mặt nạ boolean vector hóa, không dùng vòng lặp `for`.
:::

::: solution
#### Cách 1: Sử dụng toán tử bitwise & kết hợp cặp ngoặc đơn bắt buộc

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def count_segment(
    listings: pd.DataFrame,
    room_type: str = "Entire home/apt",
    gia_toi_da: float = 60000.0,
) -> int:
    if len(listings) == 0:
        return 0

    # Bắt buộc bao quanh mỗi biểu thức so sánh bằng dấu ngoặc đơn
    mask = (listings["room_type"] == room_type) & (listings["price"] <= gia_toi_da)
    return int(mask.sum())


display(pd.DataFrame([{"so_cho_o": count_segment(ds_quan)}]))

# Kết thúc lời giải
```

#### Giải thích cách 1

Mỗi điều kiện so sánh tạo một Series Boolean. Dấu `&` kết hợp theo từng vị trí và chỉ cho True khi loại phòng đúng đồng thời giá không vượt ngưỡng. Ngoặc quanh từng điều kiện bảo đảm Python nhóm đúng biểu thức trước khi kết hợp.

Trên cột float64 của mẫu, `NaN <= 60000` là False nên dòng thiếu giá không được tính. `.sum()` của mặt nạ là số dòng thỏa mãn. Hai mã `101` và `106` là nguyên căn có giá lần lượt `45000`, `60000`. Giá đúng bằng ngưỡng được giữ vì đề yêu cầu “từ ngưỡng trở xuống”, tức dùng `<=`.

#### Kết quả cách 1

| so_cho_o |
| --- |
| 2 |

#### Cách 2: Tách điều kiện thành các biến trung gian bằng .eq() và .le()

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def count_segment(
    listings: pd.DataFrame,
    room_type: str = "Entire home/apt",
    gia_toi_da: float = 60000.0,
) -> int:
    if len(listings) == 0:
        return 0

    # Sử dụng .eq() và .le() để biểu đạt mạch lạc
    mask_type = listings["room_type"].eq(room_type)
    mask_price = listings["price"].le(gia_toi_da)

    return int((mask_type & mask_price).sum())


display(pd.DataFrame([{"so_cho_o": count_segment(ds_quan)}]))

# Kết thúc lời giải
```

#### Giải thích cách 2

`.eq(room_type)` tạo mặt nạ đúng loại, còn `.le(gia_toi_da)` tạo mặt nạ giá nhỏ hơn hoặc bằng ngưỡng. Đặt chúng vào hai biến giúp đọc hoặc kiểm tra từng điều kiện trước khi dùng `mask_type & mask_price` để kết hợp.

`int(...)` chuyển kết quả đếm sang số nguyên Python. Cả hai mặt nạ có cùng chỉ mục vì được tạo từ cùng một DataFrame. Không dùng `and` cho hai Series, vì and yêu cầu một giá trị đúng/sai cho toàn đối tượng trong khi ở đây cần quyết định riêng cho từng dòng.

#### Kết quả cách 2

| so_cho_o |
| --- |
| 2 |

#### So sánh hai cách

Hai cách thực hiện cùng phép lọc vector hóa. Cách 1 viết biểu thức trực tiếp, Cách 2 đặt tên từng điều kiện bằng phương thức so sánh. Hai dòng đạt điều kiện có thể được đối chiếu bằng chính mã phòng, không chỉ bằng tổng số `2`.

:::

---

<span id="data-lab-04-05"></span>
### Bài tập 5: Truy xuất top chỗ ở giá thấp nhất bằng nsmallest và gắn cờ bất thường

::: exercise Tìm n chỗ ở có mức giá thấp nhất quận
Viết hàm `cheapest(listings: pd.DataFrame, n: int = 5) -> pd.DataFrame` nhận vào bảng dữ liệu của một quận (chứa các cột `name` và `price`, có thể chứa `NaN`). Tham số `n` là số nguyên dương và không vượt quá số dòng có giá hợp lệ.

Hàm trả về một DataFrame gồm đúng $n$ dòng có giá thấp nhất, chỉ giữ lại hai cột `name` và `price` theo đúng thứ tự đó. Kết quả được sắp xếp theo mức giá tăng dần và phải bảo toàn chỉ mục dòng ban đầu. Trong trường hợp các dòng có mức giá bằng nhau, ưu tiên giữ thứ tự dòng xuất hiện trước trong bảng.

Đồng thời, hãy đưa ra nhận xét chuyên môn về giá trị nhỏ nhất tìm được trên dữ liệu thực tế.
:::

::: solution
#### Cách 1: Sử dụng phương thức nsmallest

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def cheapest(listings: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    # Trong miền n đã cho, kết quả đủ n giá hợp lệ và giữ index gốc
    top_cheap = listings.nsmallest(n, "price")
    return top_cheap[["name", "price"]]


display(cheapest(ds_quan, n=5))

# Kết thúc lời giải
```

#### Giải thích cách 1

`nsmallest(n, "price")` chọn tối đa n dòng có giá nhỏ nhất và xếp giá tăng dần. Trong miền n của đề, n không vượt số giá hợp lệ của quận. Mặc định `keep="first"` ưu tiên dòng xuất hiện trước khi các giá bằng nhau.

Kết quả còn toàn bộ cột, nên dòng trả về chọn lại `name` và `price` theo đúng thứ tự yêu cầu. Chỉ mục gốc được giữ, thể hiện qua thứ tự `4, 1, 0, 5, 2`. Giá nhỏ nhất trong DEMO là `2500.0` CLP. Đây là giá giả lập để kiểm thử, không phải kết luận về mức giá thực tế. Với dữ liệu thật, cần kiểm tra đơn vị, loại phòng và bản ghi trước khi diễn giải một giá quá thấp.

#### Kết quả cách 1

| index | name | price |
| --- | --- | --- |
| 4 | Dormitorio simple | 2500.0 |
| 1 | Pieza cerca metro | 18000.0 |
| 0 | Depto Plaza Ñuñoa | 45000.0 |
| 5 | Casa familiar | 60000.0 |
| 2 | Loft Irarrázaval | 72000.0 |

#### Cách 2: Lọc bỏ giá trị thiếu và sắp xếp với thuật toán ổn định

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def cheapest(listings: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    # Loại bỏ giá trị khuyết, sắp xếp ổn định và lấy n dòng đầu
    sorted_df = (
        listings.dropna(subset=["price"])
        .sort_values(by="price", ascending=True, kind="stable")
        .head(n)
    )
    return sorted_df.loc[:, ["name", "price"]]


display(cheapest(ds_quan, n=5))

# Kết thúc lời giải
```

#### Giải thích cách 2

`dropna(subset=["price"])` chỉ bỏ dòng thiếu ở cột giá, không loại vì các cột khác có thiếu. `sort_values(..., kind="stable")` xếp giá tăng dần và giữ thứ tự tương đối của các dòng hòa giá. `head(n)` sau đó lấy n dòng đầu, còn `.loc[:, ["name", "price"]]` khóa hai cột đầu ra.

Cách này diễn đạt rõ từng bước loại giá thiếu, sắp xếp và cắt đầu danh sách. Nó sắp toàn bộ các dòng hợp lệ dù chỉ cần một số dòng đầu. Giữ chỉ mục gốc giúp đối chiếu trực tiếp với bảng ban đầu và phát hiện xem dòng thiếu giá có vô tình lọt vào kết quả hay không.

#### Kết quả cách 2

| index | name | price |
| --- | --- | --- |
| 4 | Dormitorio simple | 2500.0 |
| 1 | Pieza cerca metro | 18000.0 |
| 0 | Depto Plaza Ñuñoa | 45000.0 |
| 5 | Casa familiar | 60000.0 |
| 2 | Loft Irarrázaval | 72000.0 |

#### So sánh hai cách

Cách 1 dùng thao tác chọn cực trị nhỏ nhất, thường thích hợp khi chỉ cần một ít dòng đầu từ bảng lớn. Cách 2 sắp toàn bộ để quan sát thứ tự rõ ràng. Chúng cho cùng năm dòng trên mẫu và cùng quy tắc giữ thứ tự hòa giá, nhưng cần đo trên dữ liệu thực nếu muốn kết luận chênh lệch thời gian.

:::

---

<span id="data-lab-04-06"></span>
### Bài tập 6: Cập nhật giá trị bằng .loc và đồng bộ hóa cột phụ thuộc

::: exercise Mô phỏng chính sách giảm giá và tính lại báo giá 3 đêm
Nhà đầu tư muốn mô phỏng một chiến lược giá mới: Áp dụng mức giảm giá $10\%$ cho toàn bộ các chỗ ở thuộc loại hình **nguyên căn** (`Entire home/apt`), đồng thời tính toán tổng số tiền thuê cho kỳ nghỉ **3 đêm**.

Hãy viết hàm `discount_quote(listings: pd.DataFrame, room_type: str = "Entire home/apt", giam: float = 0.10) -> pd.DataFrame`.
Hàm nhận vào DataFrame quận (có các cột `id`, `room_type`, `price`) và tỷ lệ giảm giá `giam` ($0 \le \text{giam} < 1$).
Kết quả trả về là một DataFrame mới gồm đúng 4 cột theo thứ tự: `id`, `room_type`, `price`, `tien_3_dem`.
- Cột `price` của các dòng thỏa mãn loại phòng được giảm theo biểu thức $\text{giá mới} = \text{giá cũ} \times (1 - \text{giam})$ bằng cú pháp `.loc[mask, "price"]`. Các dòng khác giữ nguyên giá.
- Cột `tien_3_dem` được tính bằng $\text{price} \times 3$, căn cứ trên **mức giá sau khi đã giảm**. Các ô có giá `NaN` vẫn giữ nguyên là `NaN`.

Ràng buộc: Tuyệt đối không làm thay đổi DataFrame `listings` gốc (thao tác trên một bản sao `.copy()`). Không sử dụng cú pháp hai lần ngoặc vuông.
:::

::: solution
#### Cách 1: Thao tác tuần tự bằng .loc và gán cột mới

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def discount_quote(
    listings: pd.DataFrame, room_type: str = "Entire home/apt", giam: float = 0.10
) -> pd.DataFrame:
    # 1. Tạo bản sao độc lập để không ảnh hưởng dữ liệu gốc
    df_quote = listings[["id", "room_type", "price"]].copy()

    # 2. Tạo mặt nạ lọc các căn hộ mục tiêu
    mask = df_quote["room_type"] == room_type

    # 3. Cập nhật giá trực tiếp vào bảng thông qua .loc
    df_quote.loc[mask, "price"] = df_quote.loc[mask, "price"] * (1.0 - giam)

    # 4. Tính toán cột phụ thuộc từ mức giá mới đã cập nhật
    df_quote["tien_3_dem"] = df_quote["price"] * 3

    return df_quote


display(discount_quote(ds_quan))

# Kết thúc lời giải
```

#### Giải thích cách 1

Hàm chọn ba cột đầu vào rồi `.copy()` để tạo bảng làm việc riêng. Mặt nạ chọn dòng nguyên căn. `.loc[mask, "price"]` xuất hiện ở cả vế trái và vế phải của phép gán, nên dữ liệu được đọc, nhân hệ số giảm rồi ghi vào đúng cột của bảng này trong một thao tác chọn hàng/cột rõ ràng.

Với `giam=0.10`, hệ số còn lại là `0.9`. Sau khi cập nhật, hàm mới tính `tien_3_dem = price * 3`, nên mã `101` có giá mới `40500` và tiền ba đêm `121500`. Cột tiền ba đêm là giá trị đã tính, không phải công thức tự cập nhật như ô bảng tính. Nếu đổi giá sau đó, phải tính lại cột phụ thuộc.

#### Kết quả cách 1

| id | room_type | price | tien_3_dem |
| --- | --- | --- | --- |
| 101 | Entire home/apt | 40500.0 | 121500.0 |
| 102 | Private room | 18000.0 | 54000.0 |
| 103 | Entire home/apt | 64800.0 | 194400.0 |
| 104 | Entire home/apt | NaN | NaN |
| 105 | Private room | 2500.0 | 7500.0 |
| 106 | Entire home/apt | 54000.0 | 162000.0 |

#### Cách 2: Sử dụng toán tử kết hợp và phương thức .assign()

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def discount_quote(
    listings: pd.DataFrame, room_type: str = "Entire home/apt", giam: float = 0.10
) -> pd.DataFrame:
    df_quote = listings[["id", "room_type", "price"]].copy()
    mask = df_quote["room_type"].eq(room_type)

    # Sử dụng toán tử nhân gán kết hợp trên lát cắt .loc
    df_quote.loc[mask, "price"] *= 1.0 - giam

    # Gán cột phụ thuộc bằng biểu thức lambda thông qua .assign()
    return df_quote.assign(tien_3_dem=lambda x: x["price"] * 3)


display(discount_quote(ds_quan))

# Kết thúc lời giải
```

#### Giải thích cách 2

`.eq(room_type)` tạo mặt nạ như phép so sánh bằng. Phép nhân gán trên `.loc[mask, "price"]` vẫn chỉ rõ một lần chọn hàng và cột của bảng đích. Các dòng không thỏa mặt nạ giữ nguyên giá, còn giá NaN vẫn là NaN sau phép nhân.

`assign(tien_3_dem=lambda x: x["price"] * 3)` tạo cột trong một DataFrame trả về. Lambda nhận bảng x đang có giá đã giảm, vì bước cập nhật thực hiện trước lời gọi assign. Đặt phép tính phụ thuộc ở cuối bảo đảm không vô tình dùng giá cũ để báo tổng tiền. Tỷ lệ giam trong ví dụ nằm trong miền từ `0` đến dưới `1` như đề yêu cầu.

#### Kết quả cách 2

| id | room_type | price | tien_3_dem |
| --- | --- | --- | --- |
| 101 | Entire home/apt | 40500.0 | 121500.0 |
| 102 | Private room | 18000.0 | 54000.0 |
| 103 | Entire home/apt | 64800.0 | 194400.0 |
| 104 | Entire home/apt | NaN | NaN |
| 105 | Private room | 2500.0 | 7500.0 |
| 106 | Entire home/apt | 54000.0 | 162000.0 |

#### So sánh hai cách

Hai cách cùng tạo bảng riêng, giảm đúng dòng rồi tính tiền dựa trên giá mới. Cách 1 dùng phép gán cột trực tiếp, Cách 2 dùng assign để tạo kết quả trả về. Chúng giữ giá thiếu thay vì thay bằng không, nên không tạo báo giá giả cho chỗ chưa biết giá.

:::

---

<span id="data-lab-04-07"></span>
### Bài tập 7: So sánh ngưỡng thống kê và phân tích độ lệch mẫu số do dữ liệu khuyết (NaN)

::: exercise Phân tích tác động của NaN lên tỷ lệ giá dưới ngưỡng
Một thước đo phổ biến để đánh giá tính cạnh tranh của một quận là so sánh giá thuê từng chỗ ở trong quận với mức giá trung vị của toàn thành phố (`med_tp = df["price"].median()`). Ta muốn xác định tỷ lệ chỗ ở của quận có giá **thấp hơn** mức trung vị thành phố.

Hãy viết hàm `share_below(prices: pd.Series, nguong: float) -> dict` nhận vào một Series giá (có thể chứa `NaN`, có ít nhất một giá hợp lệ) và ngưỡng so sánh `nguong`.
Hàm trả về một từ điển gồm đúng 3 khóa:
1. `ty_le_tho`: Tỷ lệ tính trực tiếp theo cách thô bằng cách lấy trung bình trên toàn bộ các dòng `(prices < nguong).mean()`.
2. `ty_le_sach`: Tỷ lệ tính sạch, trong đó mẫu số chỉ bao gồm các dòng **thực sự có giá trị giá hợp lệ** (loại bỏ `NaN`).
3. `so_thieu`: Số lượng giá trị `NaN` xuất hiện trong chuỗi `prices`.

Giải thích rõ nguyên nhân dẫn đến sự chênh lệch giữa hai tỷ lệ này.
:::

::: solution
#### Cách 1: Sử dụng mean trực tiếp và phương thức dropna()

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def share_below(prices: pd.Series, nguong: float) -> dict:
    # 1. Tính toán thô: Mẫu số bao gồm cả các dòng khuyết giá
    ty_le_tho = float((prices < nguong).mean())

    # 2. Chỉ xét hàng có giá: Lọc bỏ NaN trước khi tính tỷ lệ
    gia_sach = prices.dropna()
    ty_le_sach = float((gia_sach < nguong).mean()) if len(gia_sach) > 0 else 0.0

    # 3. Đếm số lượng giá trị thiếu
    so_thieu = int(prices.isna().sum())

    return {
        "ty_le_tho": ty_le_tho,
        "ty_le_sach": ty_le_sach,
        "so_thieu": so_thieu,
    }


display(pd.DataFrame([share_below(ds_quan["price"], DEMO["price"].median())]))

# Kết thúc lời giải
```

#### Giải thích cách 1

`DEMO["price"].median()` bỏ hai NaN và cho ngưỡng thành phố bằng `42500.0`. Trong Ñuñoa có hai giá dưới ngưỡng, là `18000` và `2500`. Với cột float64 của fixture, so sánh NaN với ngưỡng cho False, nên `(prices < nguong).mean()` lấy tử số `2` nhưng mẫu số toàn sáu dòng.

`dropna()` tạo Series chỉ còn năm giá đọc được. So sánh trên Series này cho cùng tử số `2`, nhưng mẫu số đúng với câu hỏi “trong các chỗ có giá” là `5`, nên tỷ lệ sạch bằng `0.4`. `isna().sum()` ghi riêng một giá thiếu để người đọc biết phạm vi của tỷ lệ.

#### Kết quả cách 1

| ty_le_tho | ty_le_sach | so_thieu |
| --- | --- | --- |
| 0.333333 | 0.4 | 1 |

`ty_le_tho` là `2/6`, còn `ty_le_sach` là `2/5`. Bảng hiển thị đã rút gọn số chữ số của tỷ lệ thứ nhất.

#### Cách 2: Phân tích mẫu số tường minh bằng .lt() và .notna()

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def share_below(prices: pd.Series, nguong: float) -> dict:
    so_thieu = int(prices.isnull().sum())

    # Tạo mặt nạ boolean các phần tử nhỏ hơn ngưỡng
    mask_below = prices.lt(nguong)
    ty_le_tho = float(mask_below.mean())

    # Đếm số phần tử hợp lệ làm mẫu số chuẩn mực
    so_hop_le = int(prices.notna().sum())
    ty_le_sach = float(mask_below.sum() / so_hop_le) if so_hop_le > 0 else 0.0

    return {
        "ty_le_tho": ty_le_tho,
        "ty_le_sach": ty_le_sach,
        "so_thieu": so_thieu,
    }


display(pd.DataFrame([share_below(ds_quan["price"], DEMO["price"].median())]))

# Kết thúc lời giải
```

#### Giải thích cách 2

`.lt(nguong)` tương đương phép so sánh nhỏ hơn. `mask_below.sum()` đếm số dòng thực sự dưới ngưỡng. `prices.notna().sum()` đếm năm giá hợp lệ làm mẫu số, nên hàm không cần tạo Series giá đã bỏ thiếu chỉ để tính tỷ lệ này.

`isnull()` là tên khác của isna và cho số giá thiếu như Cách 1. Kết luận về tỷ lệ thô đang dựa trên cột float64 chứa `np.nan` trong DEMO. Với kiểu nullable Float64 và `pd.NA`, phép so sánh có thể tạo Boolean thiếu rồi mean bỏ qua chúng. Vì thế cần kiểm tra dtype và quy tắc thiếu thay vì khẳng định mọi phép so sánh pandas đều đưa NaN vào mẫu số giống nhau.

#### Kết quả cách 2

| ty_le_tho | ty_le_sach | so_thieu |
| --- | --- | --- |
| 0.333333 | 0.4 | 1 |

#### So sánh hai cách

Cách 1 tạo tập giá hợp lệ rồi tính tỷ lệ. Cách 2 đếm riêng tử số và mẫu số để tránh tạo Series lọc. Hai cách trả `0.4` trên mẫu, đồng thời ghi số thiếu để không che mất một dòng chưa biết giá.

:::

---

<span id="data-lab-04-08"></span>
### Bài tập 8: Phân tích cơ cấu loại phòng và tỷ lệ khuyết dữ liệu

::: exercise Tổng hợp phân bố loại hình và tỷ lệ dữ liệu thiếu
Viết hàm `room_mix(listings: pd.DataFrame) -> dict` nhận vào bảng dữ liệu của một quận (chứa cột `room_type` kiểu chuỗi không khuyết và cột `price` kiểu số thực có thể chứa `NaN`).

Hàm trả về một từ điển gồm đúng hai thành phần:
1. `co_cau`: Một đối tượng Series biểu diễn tỷ lệ phân bổ của các loại hình phòng, được tạo bởi phương thức `value_counts(normalize=True)`. Chỉ mục của Series là tên các loại phòng, giá trị là tỷ lệ trong khoảng $[0, 1]$.
2. `thieu_pct`: Một số thực biểu diễn phần trăm số dòng bị thiếu giá trong quận (thang đo $0$ đến $100$), được làm tròn đến đúng 2 chữ số thập phân.
:::

::: solution
#### Cách 1: Sử dụng value_counts(normalize=True) và phép toán boolean

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def room_mix(listings: pd.DataFrame) -> dict:
    # 1. Chuẩn hóa tần suất loại phòng về tỷ lệ tổng bằng 1.0
    co_cau = listings["room_type"].value_counts(normalize=True)

    # 2. Tính phần trăm số ô bị khuyết giá và làm tròn 2 chữ số
    thieu_pct = round(float(listings["price"].isna().mean() * 100), 2)

    return {"co_cau": co_cau, "thieu_pct": thieu_pct}


ket_qua = room_mix(ds_quan)
display(ket_qua["co_cau"].rename("ty_le").to_frame())
print("Tỷ lệ thiếu giá (%):", ket_qua["thieu_pct"])

# Kết thúc lời giải
```

#### Giải thích cách 1

`value_counts(normalize=True)` đếm từng loại rồi chia cho tổng số loại phòng được quan sát. Do cột room_type của đề không thiếu, mẫu số là đủ sáu dòng quận. Bốn nguyên căn cho tỷ lệ `4/6`, hai phòng riêng cho tỷ lệ `2/6`. Các giá trị Series nằm trên thang 0–1.

`price.isna()` đánh dấu một giá thiếu. Lấy mean cho tỷ lệ `1/6`, nhân `100` chuyển sang phần trăm rồi `round(..., 2)` thành `16.67`. Khi trình bày, `rename("ty_le").to_frame()` đặt tên và chuyển Series thành DataFrame một cột để notebook hiển thị bảng rõ ràng.

#### Kết quả cách 1

| room_type | ty_le |
| --- | --- |
| Entire home/apt | 0.666667 |
| Private room | 0.333333 |

Dòng in riêng là `Tỷ lệ thiếu giá (%): 16.67`.

#### Cách 2: Sử dụng groupby kết hợp xử lý trường hợp bảng rỗng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

import pandas as pd


def room_mix(listings: pd.DataFrame) -> dict:
    tong_so = len(listings)
    if tong_so == 0:
        return {"co_cau": pd.Series(dtype=float), "thieu_pct": 0.0}

    # Tính cơ cấu bằng groupby và sắp xếp giảm dần
    co_cau = (
        listings.groupby("room_type", observed=False).size() / tong_so
    ).sort_values(ascending=False)

    thieu_pct = round(float(listings["price"].isnull().sum() / tong_so * 100), 2)
    return {"co_cau": co_cau, "thieu_pct": thieu_pct}


ket_qua = room_mix(ds_quan)
display(ket_qua["co_cau"].rename("ty_le").to_frame())
print("Tỷ lệ thiếu giá (%):", ket_qua["thieu_pct"])

# Kết thúc lời giải
```

#### Giải thích cách 2

`groupby("room_type", observed=False).size()` đếm số dòng từng loại và giữ tên loại ở chỉ mục. Chia Series số đếm cho `tong_so` chuẩn hóa về tỷ lệ. `sort_values(ascending=False)` đặt nhóm lớn hơn trước. Với cột chuỗi của DEMO, hai nhóm và hai tỷ lệ khớp Cách 1.

Hàm tính tỷ lệ thiếu từ số ô thiếu chia tổng dòng, rồi làm tròn trên thang phần trăm. Nếu bảng rỗng, nhánh đầu trả Series rỗng và tỷ lệ `0.0` theo quy ước kỹ thuật. Với dữ liệu categorical, observed=False có thể giữ cả mức danh mục chưa xuất hiện, nên khi dùng lại phải phân biệt danh mục khai báo và loại thật sự có quan sát.

#### Kết quả cách 2

| room_type | ty_le |
| --- | --- |
| Entire home/apt | 0.666667 |
| Private room | 0.333333 |

Dòng in riêng là `Tỷ lệ thiếu giá (%): 16.67`.

#### So sánh hai cách

Cách 1 dùng công cụ chuyên đếm cơ cấu, Cách 2 khai triển cơ cấu thành số đếm theo nhóm chia quy mô. Chúng trả cùng kết quả trên bảng không rỗng. Quy ước `0.0` khi không có dòng ở Cách 2 cần được ghi rõ, vì không có quan sát không đồng nghĩa thị trường có tỷ lệ thiếu bằng không.

:::

---

<span id="data-lab-04-09"></span>
### Bài tập 9: Đóng gói hồ sơ quận xuất file CSV và kiểm chứng tính bất biến

::: exercise Xuất bản báo cáo hồ sơ quận ra tệp CSV và kiểm tra tính toàn vẹn
Hãy hoàn thiện bức tranh phân tích bằng cách viết hàm `export_profile(listings: pd.DataFrame, ten_quan: str, path) -> pd.DataFrame`.
Hàm nhận vào DataFrame của quận, tên quận và đường dẫn tệp lưu trữ `path`.
Hàm thực hiện các bước:
1. Tổng hợp các chỉ số thành một DataFrame **đúng một dòng** với đúng 5 cột theo thứ tự sau:
   - `quan`: Chuỗi tên quận (`ten_quan`).
   - `so_cho_o`: Số nguyên biểu diễn tổng số chỗ ở của quận.
   - `gia_trung_vi`: Số thực biểu diễn trung vị giá thuê (bỏ qua `NaN`).
   - `ty_le_nguyen_can`: Số thực biểu diễn tỷ lệ chỗ ở nguyên căn, làm tròn 3 chữ số thập phân.
   - `ty_le_thieu_gia_pct`: Số thực biểu diễn phần trăm dòng thiếu giá, làm tròn 2 chữ số thập phân.
2. Ghi DataFrame này ra đĩa cứng dưới định dạng CSV bằng `to_csv(path, index=False, encoding="utf-8")`.
3. Đọc lại tệp CSV vừa ghi bằng `pd.read_csv(path)` và trả về DataFrame đã đọc để kiểm tra các bất biến.
:::

::: solution
#### Cách 1: Khởi tạo DataFrame từ danh sách từ điển và xuất file

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

from pathlib import Path
import pandas as pd


def export_profile(listings: pd.DataFrame, ten_quan: str, path) -> pd.DataFrame:
    # 1. Tính toán các chỉ số thành phần
    so_cho_o = len(listings)
    gia_trung_vi = float(listings["price"].median())
    ty_le_nguyen_can = round(
        float((listings["room_type"] == "Entire home/apt").mean()), 3
    )
    ty_le_thieu_gia_pct = round(float(listings["price"].isna().mean() * 100), 2)

    # 2. Đóng gói vào một dòng dữ liệu duy nhất
    ho_so = pd.DataFrame(
        [
            {
                "quan": ten_quan,
                "so_cho_o": so_cho_o,
                "gia_trung_vi": gia_trung_vi,
                "ty_le_nguyen_can": ty_le_nguyen_can,
                "ty_le_thieu_gia_pct": ty_le_thieu_gia_pct,
            }
        ]
    )

    # 3. Ghi ra tệp không lưu cột chỉ mục và đọc lại
    ho_so.to_csv(path, index=False, encoding="utf-8")
    doc_lai = pd.read_csv(path)
    return doc_lai


display(export_profile(ds_quan, "Ñuñoa", "ho-so-nunoa.csv"))

# Kết thúc lời giải
```

#### Giải thích cách 1

Hàm tính năm trường trước khi tạo DataFrame một dòng từ danh sách chứa một từ điển. `median()` bỏ giá NaN, nên năm giá hợp lệ trong quận có trung vị `45000`. Tỷ lệ nguyên căn là `4/6` được làm tròn thành `0.667`, còn phần trăm thiếu giá là `16.67`.

`to_csv(..., index=False, encoding="utf-8")` ghi tên cột và dữ liệu nhưng không thêm chỉ mục dòng thành cột CSV. UTF-8 giữ tên Ñuñoa đúng ký tự. `read_csv(path)` đọc lại thành bảng để đối chiếu tên cột, số dòng và các giá trị. Các tỷ lệ đã làm tròn dùng để báo cáo, không nên dùng thay dữ liệu gốc khi cần tính toán chính xác hơn.

#### Kết quả cách 1

| quan | so_cho_o | gia_trung_vi | ty_le_nguyen_can | ty_le_thieu_gia_pct |
| --- | --- | --- | --- | --- |
| Ñuñoa | 6 | 45000.0 | 0.667 | 16.67 |

#### Cách 2: Khởi tạo có định kiểu dữ liệu tường minh khi đọc lại bằng dtype

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

ds_quan = DEMO.loc[DEMO["neighbourhood"].eq("Ñuñoa")].copy()

# Bắt đầu lời giải

from pathlib import Path
import pandas as pd


def export_profile(listings: pd.DataFrame, ten_quan: str, path) -> pd.DataFrame:
    # Đóng gói dữ liệu dạng cột sang danh sách giá trị
    du_lieu = {
        "quan": [ten_quan],
        "so_cho_o": [int(len(listings))],
        "gia_trung_vi": [float(listings["price"].median())],
        "ty_le_nguyen_can": [
            round(float(listings["room_type"].eq("Entire home/apt").mean()), 3)
        ],
        "ty_le_thieu_gia_pct": [
            round(float(listings["price"].isnull().sum() / len(listings) * 100), 2)
        ],
    }
    ho_so = pd.DataFrame(du_lieu)

    # Ghi tệp mã hóa UTF-8 chuẩn mực
    ho_so.to_csv(path, index=False, encoding="utf-8")

    # Đọc lại với schema kiểu dữ liệu định nghĩa trước
    schema_types = {
        "quan": str,
        "so_cho_o": int,
        "gia_trung_vi": float,
        "ty_le_nguyen_can": float,
        "ty_le_thieu_gia_pct": float,
    }
    return pd.read_csv(path, dtype=schema_types)


display(export_profile(ds_quan, "Ñuñoa", "ho-so-nunoa.csv"))

# Kết thúc lời giải
```

#### Giải thích cách 2

Từ điển `du_lieu` chứa một danh sách một phần tử cho mỗi cột, nên pd.DataFrame tạo đúng một dòng. Đây là cách dựng bảng theo cột, khác với từ điển biểu diễn một dòng ở Cách 1. Các phép tính dùng cùng dữ liệu và mức làm tròn.

`schema_types` ánh xạ tên cột sang kiểu mong muốn khi đọc lại CSV. Đối số `dtype=schema_types` giúp cột `so_cho_o` được đọc thành số nguyên và các thống kê thành số thực. Kiểu dữ liệu đọc không được suy ra chỉ từ hình dạng chữ trên màn hình. Bảng trả về sau đọc là đối tượng có thể dùng để kiểm tra các điều kiện như số cột, đơn vị và tính không âm của số đếm.

#### Kết quả cách 2

| quan | so_cho_o | gia_trung_vi | ty_le_nguyen_can | ty_le_thieu_gia_pct |
| --- | --- | --- | --- | --- |
| Ñuñoa | 6 | 45000.0 | 0.667 | 16.67 |

#### So sánh hai cách

Hai cách ghi cùng nội dung CSV và đọc lại thành một dòng hồ sơ. Cách 1 để pandas suy kiểu, Cách 2 chỉ định kiểu khi đọc. CSV không lưu toàn bộ thông tin dtype như một định dạng có schema, nên bước đọc lại và đối chiếu vẫn cần thiết.

:::

---

<span id="data-lab-04-10"></span>
### Bài tập 10 (mở rộng 1): Tự động hóa lập hồ sơ quận qua tham số cấu hình

::: exercise Thiết kế pipeline lập hồ sơ tái sử dụng cho quận bất kỳ
Trong thực tế phát triển phần mềm và phân tích dữ liệu, ta không viết mã nguồn cố định (hardcode) tên một quận trong toàn bộ logic tính toán. Thay vào đó, toàn bộ quy trình từ Bài tập 2 đến Bài tập 8 cần được trừu tượng hóa thành một hàm pipeline có thể tái sử dụng cho bất kỳ quận nào chỉ bằng cách thay đổi một tham số cấu hình `ten_quan`.

Hãy thiết kế hàm `profile_district_pipeline(df: pd.DataFrame, ten_quan: str) -> dict` nhận vào DataFrame toàn thành phố và tên một quận mục tiêu (chẳng hạn `"Providencia"` hoặc `"Santiago"`).
Hàm tự động tính toán và trả về một từ điển tổng kết hồ sơ quận gồm các khóa: `quan`, `so_cho_o`, `ty_trong`, `gia_trung_vi`, `ty_le_nguyen_can`. Hãy chạy thử nghiệm và so sánh hồ sơ giữa các quận.
:::

::: solution
#### Cách 1: Thiết kế hàm pipeline tuần tự

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import numpy as np
import pandas as pd


def profile_district_pipeline(df: pd.DataFrame, ten_quan: str) -> dict:
    sub = df[df["neighbourhood"] == ten_quan]
    n_sub = len(sub)
    n_total = len(df)

    if n_sub == 0:
        return {
            "quan": ten_quan,
            "so_cho_o": 0,
            "ty_trong": 0.0,
            "gia_trung_vi": np.nan,
            "ty_le_nguyen_can": 0.0,
        }

    return {
        "quan": ten_quan,
        "so_cho_o": n_sub,
        "ty_trong": round(float(n_sub / n_total), 3) if n_total > 0 else 0.0,
        "gia_trung_vi": float(sub["price"].median()),
        "ty_le_nguyen_can": round(
            float((sub["room_type"] == "Entire home/apt").mean()), 3
        ),
    }


display(pd.DataFrame([profile_district_pipeline(DEMO, "Providencia")]))

# Kết thúc lời giải
```

#### Giải thích cách 1

Hàm nhận tên quận qua `ten_quan` thay vì gắn cố định một tên trong thân hàm. Sau lọc, n_sub là số dòng quận và n_total là số dòng toàn bảng. Nhánh `n_sub == 0` trả quy mô và các tỷ lệ bằng `0.0`, còn trung vị là NaN để biểu thị chưa có giá quan sát được.

Với Providencia, hai mức giá `80000` và `30000` cho trung vị `55000`. Hai dòng trên mười hai dòng toàn mẫu cho tỷ trọng khoảng `0.167` sau làm tròn. Một trong hai dòng là nguyên căn nên tỷ lệ nguyên căn bằng `0.5`. Từ điển có tên trường giúp ghép nhiều lời gọi thành một DataFrame so sánh quận.

#### Kết quả cách 1

| quan | so_cho_o | ty_trong | gia_trung_vi | ty_le_nguyen_can |
| --- | --- | --- | --- | --- |
| Providencia | 2 | 0.167 | 55000.0 | 0.5 |

#### Cách 2: Thiết kế pipeline với các phương thức vector hóa trên Series

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import numpy as np
import pandas as pd


def profile_district_pipeline(df: pd.DataFrame, ten_quan: str) -> dict:
    mask = df["neighbourhood"].eq(ten_quan)
    sub = df.loc[mask]
    n_sub = len(sub)

    if n_sub == 0:
        return {
            "quan": ten_quan,
            "so_cho_o": 0,
            "ty_trong": 0.0,
            "gia_trung_vi": np.nan,
            "ty_le_nguyen_can": 0.0,
        }

    return {
        "quan": ten_quan,
        "so_cho_o": n_sub,
        "ty_trong": round(float(mask.mean()), 3),
        "gia_trung_vi": float(sub["price"].median()),
        "ty_le_nguyen_can": round(
            float(sub["room_type"].eq("Entire home/apt").mean()), 3
        ),
    }


display(pd.DataFrame([profile_district_pipeline(DEMO, "Providencia")]))

# Kết thúc lời giải
```

#### Giải thích cách 2

Cách thứ hai tạo mặt nạ bằng `.eq(ten_quan)`, rồi dùng `.loc[mask]` lấy bảng quận. Khi quận tồn tại, `mask.mean()` tính trực tiếp phần số dòng được chọn trên toàn bảng không thiếu tên quận. Việc tính trung vị và cơ cấu sau đó chỉ dùng `sub`.

Nhánh rỗng nằm trước phép mean nên tên quận không có trong dữ liệu nhận kết quả quy ước rõ ràng. Để so sánh thêm một quận, chỉ cần đổi đối số trong lời gọi, không sửa công thức. Tuy nhiên gói nhiều bước thành một hàm chưa làm chúng chạy tự động cho mọi quận. Nếu cần hồ sơ tất cả quận, có thể thiết kế phép tổng hợp theo nhóm riêng.

#### Kết quả cách 2

| quan | so_cho_o | ty_trong | gia_trung_vi | ty_le_nguyen_can |
| --- | --- | --- | --- | --- |
| Providencia | 2 | 0.167 | 55000.0 | 0.5 |

#### So sánh hai cách

Cách 1 dùng số dòng để tính tỷ trọng, Cách 2 dùng trung bình mặt nạ. Chúng giữ cùng câu hỏi và các trường kết quả. Tỷ trọng `0.167` mô tả DEMO, nên không được lẫn với các số đối chiếu của snapshot thực tế ở đầu lab.

:::

---

<span id="data-lab-04-11"></span>
### Bài tập 11 (mở rộng 2): Tìm quận quy mô lớn có giá trung vị thấp nhất bằng groupby

::: exercise Khảo sát nhóm thị trường quy mô lớn bằng groupby
Tìm quận có giá thuê trung vị thấp nhất trong số các quận đạt ngưỡng quy mô. Dùng ngưỡng ít nhất 3 chỗ ở trên DEMO và ít nhất 300 chỗ ở khi mở rộng sang snapshot Santiago. Ngưỡng xét số dòng chỗ ở, kể cả dòng thiếu giá.

Hãy viết hàm `find_affordable_popular_district(df: pd.DataFrame, min_listings: int = 3) -> tuple` sử dụng phương thức `groupby("neighbourhood")["price"].agg(["median", "size"])`.
Hàm trả về một bộ giá trị gồm `(tên_quận, giá_trung_vị, số_chỗ_ở)`. Sau đó, hãy kiểm chứng lại kết quả bằng cách lọc trực tiếp dữ liệu của quận đó.
:::

::: solution
#### Cách 1: Sử dụng chuỗi phương thức groupby, agg và lọc điều kiện

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def find_affordable_popular_district(df: pd.DataFrame, min_listings: int = 3) -> tuple:
    # 1. Nhóm theo quận và tính đồng thời trung vị và quy mô
    summary = df.groupby("neighbourhood")["price"].agg(["median", "size"])

    # 2. Lọc các quận có quy mô đạt yêu cầu tối thiểu
    filtered = summary[summary["size"] >= min_listings]

    # 3. Lấy quận có giá trung vị thấp nhất
    cheapest_row = filtered.nsmallest(1, "median").iloc[0]

    return cheapest_row.name, float(cheapest_row["median"]), int(cheapest_row["size"])


ket_qua = find_affordable_popular_district(DEMO, min_listings=3)
display(pd.DataFrame([ket_qua], columns=["quan", "gia_trung_vi", "so_cho_o"]))

# Kết thúc lời giải
```

#### Giải thích cách 1

`groupby("neighbourhood")["price"].agg(["median", "size"])` tạo một dòng cho mỗi quận với hai phép tổng hợp. Median bỏ giá thiếu, còn size đếm mọi dòng kể cả dòng thiếu giá. Điều này bám đúng yêu cầu ngưỡng số chỗ ở, không phải ngưỡng số giá hợp lệ.

Sau lọc size từ `3` trở lên, Providencia có hai dòng bị loại. Ñuñoa có sáu dòng và trung vị `45000`, Santiago có bốn dòng và trung vị `40000`. `nsmallest(1, "median")` lấy dòng có trung vị thấp nhất. `.iloc[0]` đọc dòng kết quả rồi hàm trả tên ở row.name cùng hai thống kê dưới dạng tuple.

#### Kết quả cách 1

| quan | gia_trung_vi | so_cho_o |
| --- | --- | --- |
| Santiago | 40000.0 | 4 |

#### Cách 2: Sử dụng named aggregation kết hợp truy vấn query()

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def find_affordable_popular_district(df: pd.DataFrame, min_listings: int = 3) -> tuple:
    # Gom nhóm với tên cột kết quả được đặt tường minh
    grouped = (
        df.groupby("neighbourhood")
        .agg(
            gia_trung_vi=("price", "median"),
            so_cho_o=("price", "size"),
        )
        .query("so_cho_o >= @min_listings")
        .sort_values(by="gia_trung_vi", ascending=True)
    )
    first_district = grouped.iloc[0]
    return (
        first_district.name,
        float(first_district["gia_trung_vi"]),
        int(first_district["so_cho_o"]),
    )


ket_qua = find_affordable_popular_district(DEMO, min_listings=3)
display(pd.DataFrame([ket_qua], columns=["quan", "gia_trung_vi", "so_cho_o"]))

# Kết thúc lời giải
```

#### Giải thích cách 2

Named aggregation đặt tên cột kết quả ngay trong lời gọi agg. `gia_trung_vi=("price", "median")` xác định cột nguồn và phép tính, còn `so_cho_o=("price", "size")` xác định số dòng. `.query("so_cho_o >= @min_listings")` đọc biến Python min_listings nhờ dấu `@`.

Hàm xếp các nhóm đạt ngưỡng theo trung vị tăng dần rồi lấy nhóm đầu. Đây là phép sắp xếp toàn bộ nhóm đạt điều kiện, trong khi Cách 1 chỉ yêu cầu một cực trị. Cả hai đoạn mã hiện giả định có ít nhất một nhóm đạt ngưỡng và có trung vị xác định. Nếu không có, cần thiết kế thêm kết quả rỗng thay vì truy cập `.iloc[0]`.

#### Kết quả cách 2

| quan | gia_trung_vi | so_cho_o |
| --- | --- | --- |
| Santiago | 40000.0 | 4 |

#### So sánh hai cách

Hai cách giữ đúng khác biệt giữa quy mô nhóm và số giá hợp lệ. Cách 1 dùng nsmallest để tìm một nhóm, Cách 2 đặt tên cột rõ hơn và tạo thứ tự đầy đủ. Với dữ liệu mẫu, lọc lại Santiago cho bốn dòng và ba giá hợp lệ `40000`, `12000`, `95000`, xác nhận trung vị `40000`.

:::

---

<span id="data-lab-04-12"></span>
### Bài tập 12 (mở rộng 3): Phân tích bản chất bộ nhớ và khắc phục bẫy gán chuỗi (ChainedAssignmentError)

::: exercise Phân tích cơ chế gán chuỗi hai lần ngoặc vuông
Một đoạn mã do công cụ AI sinh ra để giảm $10\%$ giá cho các chỗ ở nguyên căn như sau:

```python
# Trích xuất bảng con quận Ñuñoa từ dữ liệu DEMO
nu = DEMO[DEMO["neighbourhood"] == "Ñuñoa"]
bao_gia = nu[["id", "room_type", "price"]].copy()
bao_gia["price"][bao_gia["room_type"] == "Entire home/apt"] *= 0.9
```
Khi chạy đoạn mã trên trên pandas 3 (bật Copy-on-Write mặc định), hệ thống đưa ra cảnh báo hoặc kích hoạt `ChainedAssignmentError`, và kiểm tra lại thì thấy bảng `bao_gia` hoàn toàn không thay đổi giá trị.
1. Hãy giải thích bản chất kiến trúc bộ nhớ vì sao bảng `bao_gia` không đổi.
2. Viết hàm `safe_apply_discount(df: pd.DataFrame, room_type: str, giam: float) -> pd.DataFrame` khắc phục lỗi này bằng hai phương pháp chuẩn mực.
:::

::: solution
#### Cách 1: Sử dụng phương thức .loc gán đơn tầng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import pandas as pd


def safe_apply_discount(df: pd.DataFrame, room_type: str, giam: float) -> pd.DataFrame:
    # 1. Tạo bản sao dữ liệu an toàn
    out = df.copy()

    # 2. Sử dụng .loc để gán giá trị tại đúng tọa độ hàng và cột trong một bước duy nhất
    mask = out["room_type"] == room_type
    out.loc[mask, "price"] = out.loc[mask, "price"] * (1.0 - giam)

    return out


display(safe_apply_discount(DEMO, "Entire home/apt", 0.1)[["id", "price"]])

# Kết thúc lời giải
```

#### Giải thích cách 1

Chuỗi gán hai lần chọn `bao_gia["price"][mask]` làm việc qua một Series trung gian. Trong cơ chế Copy-on-Write của pandas 3, sửa đối tượng trung gian không cập nhật bảng cha theo cách đó. `.copy()` khi tạo bao_gia không biến phép gán chuỗi thành một phép gán hợp lệ vào bảng.

Hàm sửa bằng `.loc[mask, "price"]` ở ngay bảng đích out. Nhờ vậy phép gán xác định cả hàng lẫn cột của đối tượng cần sửa trong một bước. `out = df.copy()` giữ bảng đầu vào nguyên vẹn. Trên toàn DEMO, sáu nguyên căn có giá được nhân `0.9`, còn các loại khác giữ nguyên. Giá thiếu vẫn không có giá để báo.

#### Kết quả cách 1

| index | id | price |
| --- | --- | --- |
| 0 | 101 | 40500.0 |
| 1 | 102 | 18000.0 |
| 2 | 103 | 64800.0 |
| 3 | 104 | NaN |
| 4 | 105 | 2500.0 |
| 5 | 106 | 54000.0 |
| 6 | 107 | 72000.0 |
| 7 | 108 | 30000.0 |
| 8 | 109 | 36000.0 |
| 9 | 110 | 12000.0 |
| 10 | 111 | NaN |
| 11 | 112 | 95000.0 |

#### Cách 2: Sử dụng phép toán vector hóa np.where

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
        "name": [
            "Depto Plaza Ñuñoa",
            "Pieza cerca metro",
            "Loft Irarrázaval",
            "Depto sin price",
            "Dormitorio simple",
            "Casa familiar",
            "Studio Providencia",
            "Pieza Providencia",
            "Depto Centro",
            "Hostal Centro",
            "Pieza Centro",
            "Hotel boutique",
        ],
        "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
        "room_type": [
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Entire home/apt",
            "Private room",
            "Entire home/apt",
            "Shared room",
            "Private room",
            "Hotel room",
        ],
        "price": [
            45000.0,
            18000.0,
            72000.0,
            np.nan,
            2500.0,
            60000.0,
            80000.0,
            30000.0,
            40000.0,
            12000.0,
            np.nan,
            95000.0,
        ],
        "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
    }
)

# Bắt đầu lời giải

import numpy as np
import pandas as pd


def safe_apply_discount(df: pd.DataFrame, room_type: str, giam: float) -> pd.DataFrame:
    out = df.copy()
    mask = out["room_type"].eq(room_type)

    # Thay thế giá trị dựa trên điều kiện không thông qua lát cắt trung gian
    out["price"] = np.where(mask, out["price"] * (1.0 - giam), out["price"])

    return out


display(safe_apply_discount(DEMO, "Entire home/apt", 0.1)[["id", "price"]])

# Kết thúc lời giải
```

#### Giải thích cách 2

`np.where(mask, out["price"] * (1.0 - giam), out["price"])` chọn theo từng vị trí giữa hai nhánh. Vị trí True lấy giá giảm, vị trí False lấy giá cũ. Kết quả là một ndarray cùng độ dài, được gán lại cho toàn cột price của out, nên không có đối tượng con làm đích ghi.

Hai nhánh giá được tính trước khi np.where chọn. Với dữ liệu float64 của bài, cách này giữ NaN và thứ tự vị trí dòng. NumPy làm việc theo vị trí, không tự căn nhãn Series như nhiều phép toán pandas. Vì vậy mặt nạ và cả hai mảng giá phải được tạo từ đúng cùng bảng, cùng thứ tự. Nếu mở rộng sang dtype nullable, cần kiểm tra thêm cách chuyển dtype và dữ liệu thiếu.

#### Kết quả cách 2

| index | id | price |
| --- | --- | --- |
| 0 | 101 | 40500.0 |
| 1 | 102 | 18000.0 |
| 2 | 103 | 64800.0 |
| 3 | 104 | NaN |
| 4 | 105 | 2500.0 |
| 5 | 106 | 54000.0 |
| 6 | 107 | 72000.0 |
| 7 | 108 | 30000.0 |
| 8 | 109 | 36000.0 |
| 9 | 110 | 12000.0 |
| 10 | 111 | NaN |
| 11 | 112 | 95000.0 |

#### So sánh hai cách

Cách 1 cập nhật những ô được chọn bằng loc và giữ cách diễn đạt theo nhãn của pandas. Cách 2 dựng toàn bộ cột mới bằng phép chọn của NumPy rồi gán một lần. Cả hai khắc phục gán chuỗi trên bảng mẫu và không đổi DEMO, nhưng không nên gọi Cách 2 nhanh hơn nếu chưa đo cả quy trình.

:::

---

## 4. Bảng tổng kết kỹ thuật cốt lõi

| Khái niệm và thao tác | Cú pháp chuẩn mực | Lợi ích kỹ thuật | Ứng dụng ở các bài sau |
| :--- | :--- | :--- | :--- |
| Thói quen 5 bước | `.shape`, `.sample()`, `.info()`, `.describe()`, `.value_counts()` | Nắm bắt quy mô, kiểu dữ liệu, mức độ khuyết và phân bố dữ liệu trong 30 giây đầu tiên. | Đánh giá ban đầu mọi tập dữ liệu mới và kiểm chứng kết quả do AI sinh ra. |
| Trích xuất cột và hàng | `df["cột"]`, `df[["a", "b"]]`, `df[mask]`, `df.loc[mask, "cột"]` | Phân biệt kiểu trả về Series và DataFrame. Chọn đúng hàng và cột khi cần cập nhật giá trị. | Toàn bộ các thao tác xử lý dữ liệu từ Bài 5 trở đi. |
| Lọc kết hợp đa điều kiện | `(cond1) & (cond2)` | Kết hợp các điều kiện logic trên mảng boolean bằng toán tử bitwise với cặp ngoặc đơn bắt buộc. | Phân đoạn khách hàng, lọc bản ghi theo tiêu chí phức tạp. |
| Top phần tử | `df.nsmallest(n, "cột")` | Thuật toán heap hiệu năng cao, bảo toàn chỉ mục và tự động xử lý giá trị khuyết `NaN`. | Tìm top sản phẩm, chỗ ở giá rẻ, bài toán xếp hạng. |
| Cập nhật dữ liệu an toàn | `df.loc[mask, "cột"] = giá_trị` | Cập nhật trực tiếp vào bộ nhớ bảng gốc, loại bỏ hoàn toàn bẫy gán chuỗi `ChainedAssignmentError`. | Khâu làm sạch dữ liệu (Bài 10) và tiền xử lý biến đặc trưng. |
| Ảnh hưởng của mẫu số | `.dropna()` trước khi tính tỷ lệ | Tránh ngộ nhận do phép so sánh `NaN` trả về `False` làm thổi phồng mẫu số giả tạo. | Thống kê tỷ lệ chuyển đổi, tỷ lệ lỗi trong bài toán thực tế. |
| Đóng gói và xuất bản | `df.to_csv("path.csv", index=False)` | Tạo tệp dữ liệu phẳng chuẩn hóa, không thừa cột chỉ mục, kiểm chứng bất biến khi nạp lại. | Xuất kết quả phân tích, kết nối đường ống dữ liệu (pipeline). |

---

## 5. Tài liệu tham khảo

1. **Wes McKinney** (2022). *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter (3rd Edition)*. O'Reilly Media. Chương 5: Getting Started with pandas.
2. **pandas Development Team** (2024–2026). *pandas Documentation: Indexing and selecting data & Copy-on-Write User Guide*. Truy cập tại: `https://pandas.pydata.org/docs/`.
3. **Inside Airbnb** (2026). *Santiago de Chile Data Snapshot (2026-06-29)*. Lưu trữ mã nguồn mở phục vụ nghiên cứu và phân tích dữ liệu đô thị.
