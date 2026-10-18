## Khởi động pandas: Truy xuất theo nhãn, vị trí, căn chỉnh tự động và phân loại dải giá

Một nhãn chỉ mục và một vị trí hàng có thể trông giống nhau nhưng chọn ra kết quả khác. Ba bài sau luyện cách truy xuất, căn chỉnh hai bảng giá và chia dải giá có ranh giới rõ ràng.

---

## 1. Thiết lập môi trường và dữ liệu thực hành

Để bảo đảm toàn bộ quy trình thực hành có thể chạy độc lập, phần mở đầu sử dụng ba cấu trúc dữ liệu nhỏ gồm một chuỗi chỉ mục không liên tục, hai chuỗi khảo sát giá qua hai thời điểm và bảng dữ liệu mẫu 12 dòng (đơn vị: CLP/đêm). Bộ dữ liệu nhỏ này phản ánh đầy đủ các đặc tính của dữ liệu thực tế: Đa dạng loại phòng, chứa dữ liệu khuyết (`NaN`) và có các mức giá ở nhiều dải khác nhau.

```python
import numpy as np
import pandas as pd

# Chuỗi dữ liệu với chỉ mục số nguyên không liên tục phục vụ phân biệt nhãn và vị trí
s_demo = pd.Series([100, 200, 300], index=[2, 0, 5])

# Dữ liệu khảo sát giá qua hai thời điểm phục vụ bài toán căn chỉnh tự động
gia_cu = pd.Series({"A": 100.0, "B": 200.0, "C": 50.0})
gia_moi = pd.Series({"B": 220.0, "A": 90.0, "D": 70.0})

# Bảng dữ liệu mẫu 12 dòng (đơn vị: CLP/đêm)
DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
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

# Đường dẫn dữ liệu thực tế Inside Airbnb phục vụ đối chiếu quy mô lớn
SNAPSHOT_URL = (
    "https://data.insideairbnb.com/chile/rm/santiago/"
    "2026-06-29/visualisations/listings.csv"
)
```

> [!NOTE]
> **Đối chiếu thực tế**: Khi đối chiếu trên tập dữ liệu đầy đủ của vùng đô thị Santiago (18.534 dòng dữ liệu niêm yết), thị trường có đúng 846 phòng khuyết giá. Việc phân đoạn giá trên dữ liệu thực tế tạo ra ba dải quy mô: Phân khúc trung bình có 12.325 phòng, phân khúc cao có 3.703 phòng và phân khúc rẻ có 1.660 phòng. Các số liệu thực tế này được đưa vào để đối chiếu tính tổng quát của giải thuật, không dùng làm hằng số gán cứng trong mã nguồn.

---

## 2. Nội dung chi tiết các bài tập thực hành

<span id="data-lab-05-01"></span>
### Bài tập 1: Phân biệt truy xuất theo nhãn với loc và theo vị trí với iloc

::: exercise Phân biệt loc và iloc trên Series
Cho một đối tượng `pd.Series` tên là `s` có chỉ mục không trùng lặp, một giá trị nhãn `nhan` chắc chắn tồn tại trong chỉ mục và một chỉ số nguyên `vi_tri` hợp lệ biểu diễn vị trí hàng (có thể nhận giá trị âm như `-1`).

Hãy viết hàm `loc_iloc(s: pd.Series, nhan, vi_tri: int) -> dict` trả về một từ điển gồm đúng hai khóa sau:
1. `theo_nhan`: Giá trị của phần tử mang nhãn `nhan`, truy xuất thông qua thuộc tính `.loc`.
2. `theo_vi_tri`: Giá trị của phần tử ở vị trí `vi_tri`, truy xuất thông qua thuộc tính `.iloc`.

Yêu cầu kỹ thuật: Bắt buộc sử dụng `.loc` và `.iloc`, tuyệt đối không dùng cú pháp truy cập trực tiếp `s[...]` để tránh nhập nhằng khi chỉ mục mang kiểu số nguyên.
:::

::: solution
#### Cách 1: Tách từng bước truy xuất theo nhãn và theo vị trí

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

s_demo = pd.Series([100, 200, 300], index=[2, 0, 5])

# Bắt đầu lời giải

import pandas as pd


def loc_iloc(s: pd.Series, nhan, vi_tri: int) -> dict:
    # 1. Truy xuất phần tử theo giá trị nhãn của chỉ mục bằng .loc
    gia_tri_nhan = s.loc[nhan]

    # 2. Truy xuất phần tử theo vị trí thứ tự thực tế bằng .iloc
    gia_tri_vi_tri = s.iloc[vi_tri]

    # 3. Đóng gói kết quả vào từ điển chuẩn đầu ra
    return {
        "theo_nhan": gia_tri_nhan,
        "theo_vi_tri": gia_tri_vi_tri,
    }


# Gọi thử nghiệm hàm với chuỗi dữ liệu mẫu:
ket_qua_q1_c1 = loc_iloc(s_demo, 2, 2)
print("Kết quả Cách 1:", ket_qua_q1_c1)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`s.loc[nhan]` tra nhãn trong chỉ mục. Nhãn `2` nằm ở dòng đầu của `s_demo`, nên giá trị nhận được là `100`. `s.iloc[vi_tri]` đếm vị trí từ 0. Vị trí `2` là dòng thứ ba, có giá trị `300`. Hai số 2 giống nhau về cách viết nhưng giữ hai vai trò khác nhau.

Các biến `gia_tri_nhan` và `gia_tri_vi_tri` lưu hai kết quả trước khi `return` ghép chúng vào một từ điển. `return` kết thúc lời gọi hàm và giao từ điển cho nơi gọi. Với chỉ mục duy nhất như đề đã giả thiết, mỗi phép truy xuất trả về một giá trị đơn. Nếu bỏ giả thiết này, `.loc` có thể trả về nhiều phần tử.

`.iloc[-1]` chọn phần tử cuối, còn `.loc[-1]` yêu cầu nhãn `-1` thật sự tồn tại. Vị trí vượt phạm vi gây `IndexError`, nhãn không tồn tại gây `KeyError`. Không cần tự xử lý hai trường hợp ấy trong bài vì đầu vào đã được bảo đảm hợp lệ.

##### Output Cách 1

| Khóa trả về | Phép truy xuất | Giá trị |
|---|---|---|
| `theo_nhan` | `s_demo.loc[2]` | 100 |
| `theo_vi_tri` | `s_demo.iloc[2]` | 300 |

#### Cách 2: Trả trực tiếp từ điển kết quả

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

s_demo = pd.Series([100, 200, 300], index=[2, 0, 5])

# Bắt đầu lời giải

import pandas as pd


def loc_iloc(s: pd.Series, nhan, vi_tri: int) -> dict:
    # Trích xuất trực tiếp vào từ điển kết quả mà không cần biến trung gian
    return {
        "theo_nhan": s.loc[nhan],
        "theo_vi_tri": s.iloc[vi_tri],
    }


# Gọi thử nghiệm hàm với nhãn 0 và vị trí 0:
ket_qua_q1_c2 = loc_iloc(s_demo, 0, 0)
print("Kết quả Cách 2:", ket_qua_q1_c2)

# Kết thúc lời giải
```

##### Giải thích Cách 2

Hai phép truy xuất được đặt ngay trong biểu thức từ điển. Python tính từng giá trị rồi tạo từ điển có đúng hai khóa. Việc bỏ các biến trung gian không thay đổi quy tắc tìm nhãn hoặc đếm vị trí của pandas.

Lời gọi minh họa thứ hai dùng `nhan=0` và `vi_tri=0`. Nhãn `0` nằm ở dòng thứ hai nên `.loc[0]` trả `200`. Vị trí `0` là dòng đầu nên `.iloc[0]` trả `100`. Đừng dùng kết quả khác nhau của hai ví dụ để kết luận hai phiên bản hàm khác nhau về hành vi. Khi truyền cùng ba đối số, chúng trả cùng hai giá trị.

##### Output Cách 2

| Khóa trả về | Phép truy xuất | Giá trị |
|---|---|---|
| `theo_nhan` | `s_demo.loc[0]` | 200 |
| `theo_vi_tri` | `s_demo.iloc[0]` | 100 |

#### So sánh hai cách

Cách 1 thuận tiện khi đặt điểm dừng để xem từng giá trị. Cách 2 phù hợp với hàm ngắn đã rõ ý nghĩa. Cả hai thực hiện đúng hai lần truy xuất, nên không có cơ sở để coi cách viết ngắn hơn là một cải tiến thuật toán. Trong một số phiên bản NumPy, `print` hiển thị giá trị trong từ điển dưới dạng `np.int64(100)` thay vì `100`. Kiểu vô hướng NumPy này không làm thay đổi giá trị trong bảng.

:::

---

<span id="data-lab-05-02"></span>
### Bài tập 2: Cơ chế căn chỉnh tự động theo index khi tính toán số học

::: exercise Phép toán số học tự khớp theo nhãn chỉ mục
Cho hai đối tượng `pd.Series` số thực `gia_cu` và `gia_moi`, mỗi chuỗi đều có chỉ mục là tập hợp các nhãn duy nhất không trùng lặp.

Hãy viết hàm `align_change(gia_cu: pd.Series, gia_moi: pd.Series) -> dict` tính toán mức chênh lệch giá và trả về một từ điển gồm đúng hai khóa sau:
1. `thay_doi`: Đối tượng `pd.Series` kết quả của phép toán trừ `gia_moi - gia_cu`. Chỉ mục của Series này là hợp của hai chỉ mục ban đầu.
2. `so_nan`: Một số nguyên (`int`) đếm chính xác số lượng giá trị `NaN` xuất hiện trong Series `thay_doi`.

Yêu cầu kỹ thuật: Không sử dụng vòng lặp thủ công, không làm thay đổi dữ liệu của hai Series đầu vào.
:::

::: solution
#### Cách 1: Trừ trực tiếp hai Series rồi đếm ô khuyết

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

gia_cu = pd.Series({"A": 100.0, "B": 200.0, "C": 50.0})

gia_moi = pd.Series({"B": 220.0, "A": 90.0, "D": 70.0})

# Bắt đầu lời giải

import pandas as pd


def align_change(gia_cu: pd.Series, gia_moi: pd.Series) -> dict:
    # 1. Thực hiện phép trừ, pandas tự động căn chỉnh theo nhãn chỉ mục
    thay_doi = gia_moi - gia_cu

    # 2. Đếm số lượng ô mang giá trị khuyết NaN
    so_nan = int(thay_doi.isna().sum())

    # 3. Đóng gói kết quả trả về
    return {
        "thay_doi": thay_doi,
        "so_nan": so_nan,
    }


# Gọi thử nghiệm hàm với hai chuỗi giá khảo sát mẫu:
ket_qua_q2_c1 = align_change(gia_cu, gia_moi)
print("Kết quả Cách 1:")
print(ket_qua_q2_c1["thay_doi"])
print("Số ô NaN:", ket_qua_q2_c1["so_nan"])

# Kết thúc lời giải
```

##### Giải thích Cách 1

Phép trừ `gia_moi - gia_cu` tìm các phần tử có cùng nhãn trước khi tính. Ở nhãn A, phép tính là `90 - 100`, cho `-10`. Ở nhãn B, phép tính là `220 - 200`, cho `20`. Thứ tự B rồi A trong `gia_moi` không khiến chúng bị trừ nhầm theo vị trí.

Chỉ mục kết quả chứa cả A, B, C và D. C thiếu giá mới, D thiếu giá cũ nên hai phép tính ấy chưa có đủ dữ kiện và trả `NaN`. `.isna()` tạo một Series boolean đánh dấu ô khuyết. `.sum()` cộng các giá trị `True` như 1, rồi `int(...)` chuyển số đếm thành số nguyên Python theo yêu cầu đầu ra.

Hàm chỉ tạo kết quả tính toán mới và không gán ngược vào hai Series nguồn. Khi nhãn đại diện cho mã sản phẩm hoặc chỗ ở, việc giữ chỉ mục là điều giúp phép tính đi đúng đối tượng.

##### Output Cách 1

| Nhãn | `thay_doi` |
|---|---|
| A | -10.0 |
| B | 20.0 |
| C | `NaN` |
| D | `NaN` |

`so_nan = 2`.

#### Cách 2: Dùng phương thức sub để diễn đạt phép trừ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

gia_cu = pd.Series({"A": 100.0, "B": 200.0, "C": 50.0})

gia_moi = pd.Series({"B": 220.0, "A": 90.0, "D": 70.0})

# Bắt đầu lời giải

import pandas as pd


def align_change(gia_cu: pd.Series, gia_moi: pd.Series) -> dict:
    # Sử dụng phương thức .sub() của đối tượng Series
    thay_doi = gia_moi.sub(gia_cu)

    # Trích xuất số lượng ô khuyết thông qua tổng mảng boolean
    so_nan = int(thay_doi.isna().sum())

    return {
        "thay_doi": thay_doi,
        "so_nan": so_nan,
    }


# Gọi thử nghiệm hàm với hai chuỗi giá khảo sát mẫu:
ket_qua_q2_c2 = align_change(gia_cu, gia_moi)
print("Kết quả Cách 2:")
print(ket_qua_q2_c2["thay_doi"])
print("Số ô NaN:", ket_qua_q2_c2["so_nan"])

# Kết thúc lời giải
```

##### Giải thích Cách 2

`gia_moi.sub(gia_cu)` là cách gọi phương thức cho cùng phép trừ có căn chỉnh. Đối tượng đứng trước `.sub` là số bị trừ, đối số truyền vào là số trừ. Vì vậy không được đổi vị trí hai Series nếu vẫn muốn tính giá mới trừ giá cũ.

Sau phép trừ, chuỗi `.isna().sum()` vẫn đếm hai nhãn chưa có đủ hai mức giá. `.sub` còn nhận `fill_value` trong những bài toán có quy ước bù dữ liệu. Bài này không truyền đối số đó vì thiếu một mức giá chưa có nghĩa mức giá ấy bằng 0.

##### Output Cách 2

| Nhãn | `thay_doi` |
|---|---|
| A | -10.0 |
| B | 20.0 |
| C | `NaN` |
| D | `NaN` |

`so_nan = 2`.

#### So sánh hai cách

Cả hai cách có cùng quy tắc căn chỉnh và cùng kết quả. Toán tử `-` dễ đọc khi chỉ có một phép tính. `.sub()` tiện khi viết một chuỗi phương thức hoặc cần cấu hình rõ cách bù giá trị khuyết. Thêm `fill_value=0` sẽ đổi ý nghĩa bài toán, nên không thể xem đó là một bước tối ưu giữ nguyên kết quả.

:::

---

<span id="data-lab-05-03"></span>
### Bài tập 3: Phân loại dải giá bằng map với hàm tự định nghĩa

::: exercise Phân chia phân khúc giá phòng bằng map
Trong nghiên cứu thị trường lưu trú, các mức giá niêm yết được phân chia thành ba phân khúc:
1. Phân khúc rẻ (`"re"`): Giá phòng nhỏ hơn 30.000 CLP.
2. Phân khúc trung bình (`"trung"`): Giá phòng từ 30.000 CLP đến dưới 100.000 CLP.
3. Phân khúc cao (`"cao"`): Giá phòng từ 100.000 CLP trở lên.

Hãy viết hàm `phan_khuc(gia) -> str | None` nhận vào một giá trị số thực đại diện cho giá niêm yết (hoặc giá trị khuyết `np.nan`, `None`). Hàm trả về chuỗi tương ứng `"re"`, `"trung"`, `"cao"`, hoặc trả về `None` nếu giá trị đầu vào bị khuyết.

Yêu cầu kỹ thuật: Phải kiểm tra giá trị khuyết bằng `pd.isna` trước khi so sánh ngưỡng số học để tránh lỗi so sánh kiểu dữ liệu. Sau đó, áp dụng hàm này trên cột giá của bảng dữ liệu thông qua phương thức `map`.
:::

::: solution
#### Cách 1: Viết hàm phân loại một giá rồi áp dụng bằng map

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
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

# Bắt đầu lời giải

import numpy as np
import pandas as pd


def phan_khuc(gia):
    # Bước 1: Kiểm tra ô khuyết trước tiên bằng pd.isna
    if pd.isna(gia):
        return None

    # Bước 2: Kiểm tra các ngưỡng giá theo thứ tự tăng dần
    if gia < 30000.0:
        return "re"
    elif gia < 100000.0:
        return "trung"
    else:
        return "cao"


# Gọi thử nghiệm hàm với các trường hợp đơn lẻ:
print("Giá 25.000 CLP:", phan_khuc(25000.0))
print("Giá 30.000 CLP:", phan_khuc(30000.0))
print("Giá 99.999 CLP:", phan_khuc(99999.0))
print("Giá 100.000 CLP:", phan_khuc(100000.0))
print("Giá khuyết NaN:", phan_khuc(np.nan))

# Áp dụng hàm trên toàn bộ cột price của bảng DEMO:
phan_khuc_demo = DEMO["price"].map(phan_khuc)
print("Phân bố phân khúc trên 12 dòng DEMO:")
print(phan_khuc_demo.value_counts(dropna=False))

# Kết thúc lời giải
```

##### Giải thích Cách 1

`pd.isna(gia)` phải được xét trước các ngưỡng để ô khuyết trả `None`. Nếu để `np.nan` đi qua các phép so sánh `<`, nó không rơi vào hai nhánh đầu và có thể bị gán nhầm nhãn `cao`. Với `pd.NA`, dùng trực tiếp kết quả so sánh làm điều kiện còn có thể gây lỗi vì trạng thái đúng sai chưa xác định.

Sau khi loại trường hợp khuyết, hai nhánh kiểm tra theo thứ tự tăng dần. Giá `30000` không nhỏ hơn `30000`, nhưng nhỏ hơn `100000`, nên nhận `trung`. Giá `100000` đi tới nhánh cuối và nhận `cao`.

`DEMO["price"].map(phan_khuc)` gọi hàm với từng giá và giữ chỉ mục của cột giá trong Series mới. `.value_counts(dropna=False)` đếm cả nhãn khuyết, giúp kiểm tra đủ 12 dòng. Đây là quy tắc phân dải theo đề, chưa phải bước kiểm tra giá âm hoặc giá bất hợp lý.

##### Output Cách 1

Các lời gọi đơn lẻ lần lượt trả `re`, `trung`, `trung`, `cao`, `None` cho các giá `25000`, `30000`, `99999`, `100000`, `np.nan`.

| Nhãn phân khúc | Số dòng trên DEMO |
|---|---|
| `re` | 2 |
| `trung` | 5 |
| `cao` | 4 |
| Khuyết | 1 |

#### Cách 2: Dùng cut để phân khoảng cho cả cột

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import numpy as np

import pandas as pd

DEMO = pd.DataFrame(
    {
        "id": list(range(201, 213)),
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

# Bắt đầu lời giải

import numpy as np
import pandas as pd


def phan_khuc(gia):
    # Đóng gói hàm scalar để phục vụ kiểm tra đơn vị
    if pd.isna(gia):
        return None
    if gia < 30000.0:
        return "re"
    if gia < 100000.0:
        return "trung"
    return "cao"


# Gọi thử hàm trên giá trị đơn lẻ:
print("Kiểm tra phân khúc giá 100.000 CLP:", phan_khuc(100000.0))

# Trong thực tế, phân đoạn hàng loạt trên Series được thực hiện tối ưu bằng pd.cut:
danh_muc_cut = pd.cut(
    DEMO["price"],
    bins=[-np.inf, 30000.0, 100000.0, np.inf],
    right=False,
    labels=["re", "trung", "cao"],
)
print("Kết quả vector hóa bằng pd.cut:")
print(danh_muc_cut.value_counts(dropna=False))

# Kết thúc lời giải
```

##### Giải thích Cách 2

Hàm `phan_khuc` vẫn cung cấp giao diện cho một giá trị đơn. Khi cần chia cả cột theo các khoảng cố định, `pd.cut` nhận Series giá cùng danh sách biên `[-np.inf, 30000, 100000, np.inf]`. Bốn biên tạo ba khoảng, do đó phải truyền đúng ba nhãn.

`right=False` đóng đầu trái và mở đầu phải của từng khoảng. Vì vậy `30000` thuộc `trung`, còn `100000` thuộc `cao`. Các giá khuyết tiếp tục khuyết. `labels` làm kết quả có kiểu phân loại `category`, khác với Series chuỗi do `map` tạo ra.

`.value_counts(dropna=False)` ở cuối chỉ dùng để xem phân bố. Nó thường sắp theo số lần xuất hiện, nên thứ tự in `trung`, `cao`, `re` không có nghĩa biên phân khoảng bị đổi.

##### Output Cách 2

| Nhãn phân khúc | Số dòng trên DEMO |
|---|---|
| `re` | 2 |
| `trung` | 5 |
| `cao` | 4 |
| Khuyết | 1 |

#### So sánh hai cách

Cách 1 mở rõ từng nhánh và thuận tiện khi bổ sung quy tắc không thể diễn đạt bằng các khoảng số. Cách 2 mô tả trực tiếp bài toán phân khoảng cho cả cột và thường là lựa chọn phù hợp cho dữ liệu lớn. Muốn khẳng định nhanh hơn bao nhiêu phải đo trên dữ liệu và môi trường cụ thể. Khi đối chiếu hai kết quả, cần xét cả nhãn khuyết và sự khác nhau giữa kiểu chuỗi với kiểu `category`.

:::
