## Ghép bảng tra cứu và kiểm định quan hệ dữ liệu trong pandas

Bảng giá và bảng phí thường được lưu riêng. Ta cần ghép đúng phân khúc, kiểm tra khóa có bị lặp hay thiếu, rồi tính giá sau phí mà vẫn giữ đủ các dòng cần phân tích.

---

## 1. Thiết lập môi trường và dữ liệu thực hành

Để bảo đảm quy trình ghép bảng có thể kiểm chứng độc lập, môi trường thực hành được khởi tạo với bảng dữ liệu danh mục phòng 12 dòng (`DEMO`, đơn vị giá: CLP/đêm) và bảng tra cứu biểu phí dịch vụ (`phi`) gồm ba dòng tương ứng với ba phân khúc giá.

```python
import numpy as np
import pandas as pd

# 12 dòng dữ liệu mẫu giả lập danh mục phòng (đơn vị: CLP/đêm)
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


# Hàm phân loại dải giá hỗ trợ gán phân khúc
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

# Bảng tra cứu biểu phí dịch vụ theo phân khúc
phi = pd.DataFrame(
    {
        "phan_khuc": ["re", "trung", "cao"],
        "phi_dich_vu": [0.10, 0.13, 0.15],
    }
)

# Địa chỉ lưu trữ snapshot thực tế Inside Airbnb
SNAPSHOT_URL = (
    "https://data.insideairbnb.com/chile/rm/santiago/"
    "2026-06-29/visualisations/listings.csv"
)
```

> [!NOTE]
Biểu phí 10%, 13% và 15% là giả định của bài tập để luyện ghép bảng. Nó không phải biểu phí thực tế của nền tảng hoặc chủ nhà.

> **Đối chiếu thực tế**: Trên snapshot thực tế toàn thành phố Santiago gồm 18.534 niêm yết, bảng tra cứu biểu phí gồm 3 dòng được ghép vào bảng danh mục phòng. Sau khi thực hiện phép ghép trái, bảng kết quả giữ nguyên 18.534 dòng và ghi nhận chính xác 846 giá trị `NaN` ở cột `phi_dich_vu` (tương ứng đúng với 846 phòng bị khuyết giá nên không xác định được phân khúc). Mức giá trung vị sau khi tính cả phí dịch vụ của phân khúc trung bình đạt 61.897 CLP.

---

## 2. Nội dung chi tiết bài tập thực hành

<span id="data-lab-05-10"></span>
### Bài tập 10: Ghép bảng tra cứu biểu phí dịch vụ và kiểm định quan hệ với validate='m:1'

::: exercise Ghép bảng tra cứu và kiểm định quan hệ nhiều - một
Giả sử nền tảng đặt phòng áp dụng chính sách thu phí dịch vụ dựa trên phân khúc giá:
- Phân khúc rẻ: Mức phí 10% (0,10).
- Phân khúc trung bình: Mức phí 13% (0,13).
- Phân khúc cao: Mức phí 15% (0,15).

Cho bảng danh mục phòng `df` chứa cột `phan_khuc` và bảng tra cứu `phi` gồm hai cột `phan_khuc` và `phi_dich_vu`.

Hãy viết hàm `merge_fees(df: pd.DataFrame, phi: pd.DataFrame) -> dict` ghép hai bảng trên theo cột khóa `phan_khuc` bằng phương thức ghép trái (`how="left"`), kèm theo tham số kiểm định quan hệ `validate="m:1"`. Hàm trả về một từ điển gồm đúng ba khóa sau:
1. `m`: Đối tượng DataFrame sau khi ghép nối, giữ nguyên tất cả các cột của `df` và bổ sung thêm cột `phi_dich_vu`.
2. `so_dong_m`: Số nguyên (`int`) thể hiện tổng số dòng của bảng kết quả `m`.
3. `so_nan_phi`: Số nguyên (`int`) đếm số lượng giá trị `NaN` xuất hiện trong cột `phi_dich_vu` sau khi ghép.

Yêu cầu kỹ thuật:
- Thiết lập `validate="m:1"` để kiểm tra tính duy nhất của khóa trong bảng tra cứu bên phải. Nếu bảng tra cứu `phi` chứa khóa trùng lặp, phải để ngoại lệ `pd.errors.MergeError` được ném ra một cách tự nhiên (không tự ý bắt lỗi hay khử trùng lặp bên trong hàm).
- Không làm thay đổi cấu trúc và dữ liệu của hai DataFrame `df` và `phi` truyền vào.
:::

::: solution
#### Cách 1: Ghép trái và kiểm tra quan hệ nhiều dòng với một khóa tra cứu

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

phi = pd.DataFrame(
    {
        "phan_khuc": ["re", "trung", "cao"],
        "phi_dich_vu": [0.10, 0.13, 0.15],
    }
)

# Bắt đầu lời giải

import pandas as pd


def merge_fees(df: pd.DataFrame, phi: pd.DataFrame) -> dict:
    # 1. Thực hiện ghép trái với kiểm định quan hệ nhiều - một (many-to-one)
    m = pd.merge(df, phi, on="phan_khuc", how="left", validate="m:1")

    # 2. Đếm số dòng sau khi ghép
    so_dong_m = len(m)

    # 3. Đếm số lượng ô khuyết trong cột phí dịch vụ
    so_nan_phi = int(m["phi_dich_vu"].isna().sum())

    return {
        "m": m,
        "so_dong_m": so_dong_m,
        "so_nan_phi": so_nan_phi,
    }


# Gọi thử nghiệm hàm trên bảng DEMO và bảng tra cứu phi:
kq_merge_c1 = merge_fees(DEMO, phi)
print("Kết quả Cách 1:")
print("Số dòng sau ghép:", kq_merge_c1["so_dong_m"])
print("Số ô NaN ở cột phí:", kq_merge_c1["so_nan_phi"])
print("Các cột của bảng sau ghép:", list(kq_merge_c1["m"].columns))

# Kết thúc lời giải
```

##### Giải thích Cách 1

`on="phan_khuc"` chỉ khóa ghép chung. `how="left"` giữ các dòng của `df` ngay cả khi không tìm được mức phí. Với bảng phải có khóa duy nhất, mỗi dòng trái chỉ khớp nhiều nhất một dòng phải, nên DEMO vẫn có 12 dòng sau ghép.

`validate="m:1"` kiểm tra tính duy nhất của khóa bên phải. Ký hiệu `m` cho phép nhiều dòng trái cùng phân khúc, còn `1` yêu cầu một dòng tra cứu cho mỗi khóa. Nếu bỏ kiểm tra và để hai dòng phí cùng khóa, một dòng trái có thể sinh thành hai dòng kết quả. Bảng sẽ tăng số dòng và làm sai các phép tổng hợp tiếp theo.

`len(m)` đếm số dòng sau ghép. `.isna().sum()` trên cột phí đếm các khóa chưa khớp. Id 204 không có giá, dẫn đến phân khúc `None`, trong khi bảng `phi` không có khóa khuyết nên mức phí của dòng ấy là `NaN`. pandas có thể ghép hai khóa khuyết với nhau nếu cả hai phía đều có khóa khuyết, vì vậy kết luận này phụ thuộc đúng bảng tra cứu đang dùng.

##### Output Cách 1

| Đại lượng | Kết quả |
|---|---|
| `so_dong_m` | 12 |
| `so_nan_phi` | 1 |
| Cột được bổ sung | `phi_dich_vu` |
| Id chưa khớp phí | 204 |

#### Cách 2: Dùng phương thức merge và kiểm tra giá sau phí

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

phi = pd.DataFrame(
    {
        "phan_khuc": ["re", "trung", "cao"],
        "phi_dich_vu": [0.10, 0.13, 0.15],
    }
)

# Bắt đầu lời giải

import pandas as pd


def merge_fees(df: pd.DataFrame, phi: pd.DataFrame) -> dict:
    # Sử dụng phương thức .merge() của đối tượng DataFrame
    m = df.merge(phi, on="phan_khuc", how="left", validate="many_to_one")

    so_dong_m = len(m)
    so_nan_phi = int(m["phi_dich_vu"].isna().sum())

    return {
        "m": m,
        "so_dong_m": so_dong_m,
        "so_nan_phi": so_nan_phi,
    }


# Gọi thử nghiệm hàm trên bảng DEMO và bảng tra cứu phi:
kq_merge_c2 = merge_fees(DEMO, phi)
m_ket_qua = kq_merge_c2["m"]

# Tính toán giá tổng cộng gồm phí và trung vị giá theo phân khúc:
gia_tong = m_ket_qua["price"] * (1 + m_ket_qua["phi_dich_vu"])
trung_vi_gia_tong = gia_tong.groupby(m_ket_qua["phan_khuc"]).median().round(0)
print("Trung vị giá gồm phí theo phân khúc Cách 2:")
print(trung_vi_gia_tong)

# Thử nghiệm kích hoạt kiểm định validate='m:1' khi bảng tra cứu bị lỗi trùng khóa:
phi_trung = pd.concat([phi, phi.head(1)], ignore_index=True)
try:
    merge_fees(DEMO, phi_trung)
except pd.errors.MergeError:
    print(
        "Xác nhận: Ngoại lệ MergeError đã được kích hoạt thành công khi bảng tra cứu trùng khóa."
    )

# Kết thúc lời giải
```

##### Giải thích Cách 2

`df.merge(phi, ...)` là cách gọi cùng phép ghép từ đối tượng bảng trái. `validate="many_to_one"` viết đầy đủ cùng quy tắc với `"m:1"`. Hàm vẫn trả ba khóa theo đề và không thêm cột vào hai bảng nguồn.

Phần minh họa bên ngoài hàm lấy giá nhân với `1 + phi_dich_vu` để tính mức giá giả định gồm phí. Ví dụ phí 13% tương ứng hệ số `1.13`. `gia_tong.groupby(m_ket_qua["phan_khuc"]).median()` dùng khóa nhóm bên ngoài để tính trung vị theo phân khúc. `.round(0)` chỉ làm tròn bảng minh họa sau khi tính.

`pd.concat([phi, phi.head(1)], ignore_index=True)` cố tình thêm lại dòng đầu để tạo khóa trùng. Gọi hàm trong `try` ở phần minh họa sẽ đi tới nhánh `except pd.errors.MergeError`. Chính hàm `merge_fees` vẫn để ngoại lệ thoát ra theo yêu cầu, giúp nơi gọi quyết định cách báo lỗi.

##### Output Cách 2

| `phan_khuc` | Trung vị giá giả định gồm phí |
|---|---|
| `cao` | 155250.0 |
| `re` | 23650.0 |
| `trung` | 62150.0 |

Bảng ghép vẫn có 12 dòng, 1 mức phí khuyết. Thử bảng phí trùng khóa phát sinh `MergeError`.

#### So sánh hai cách

Hai cách ghép có cùng kết quả và cùng cơ chế kiểm tra khóa. Cách 1 tách rõ các bước đếm để người mới quan sát. Cách 2 bổ sung tình huống sử dụng kết quả và một ca kiểm tra khóa lỗi. Ba mức phí chỉ là giả định luyện tập. Giá sau phí chưa phải doanh thu thực tế vì chưa có số đêm đặt hoặc giao dịch.

:::
