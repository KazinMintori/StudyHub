## Lab 7: Chuỗi, regex và danh sách tiện nghi

Một cột văn bản có thể chứa khoảng trắng thừa, thẻ xuống dòng, giá viết dưới dạng chuỗi hoặc danh sách JSON. Ta sẽ làm sạch từng dạng, kiểm lại những chuỗi không chuyển đổi được và trích thông tin theo quy tắc rõ ràng. Các ví dụ cũng cho thấy vì sao có một từ khóa chưa đủ để suy ra ý kiến của người viết.

## Thông tin dữ liệu thực hành

Tập bài tập sử dụng dữ liệu chỗ ở và đánh giá của Inside Airbnb với ảnh chụp dữ liệu (snapshot) ngày 29/06/2026 tại thành phố Santiago (Chile).
Tệp dữ liệu đánh giá đầy đủ được lưu trữ tại: `https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/reviews.csv.gz` (gồm 690.112 đoạn văn bản trong cột `comments`).
Tệp dữ liệu chỗ ở đầy đủ được lưu trữ tại: `https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/listings.csv.gz` (gồm 18.534 chỗ ở trong cột `amenities`).

Lưu ý: Các số liệu tính toán trên các tập dữ liệu nhỏ dưới đây là dữ liệu kiểm thử giả lập (synthetic fixtures), phục vụ mục đích kiểm định tính đúng đắn của giải thuật và không đại diện cho các chỉ số thống kê toàn cục của thị trường Santiago. Biểu thức chính quy chỉ đóng vai trò là một quy tắc mẫu có phạm vi giới hạn, không thay thế cho các bộ nhận diện ngôn ngữ chuyên sâu. Thao tác thay thế chuỗi `<br/>` trong bài chỉ áp dụng cho đúng thẻ ngắt dòng nguyên văn đã biết, không dùng để phân tích cú pháp HTML tổng quát.

```python
import json
import re
import numpy as np
import pandas as pd
from IPython.display import display

# Dữ liệu kiểm thử giả lập 16 đoạn đánh giá đại diện
DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

# Dữ liệu kiểm thử chuyển đổi giá tiền
DEMO_PRICES = pd.Series(["$1,200.00", " $850.00 ", None, "liên hệ", "từ $500"])
DEMO_PRICES_TEST = pd.Series(
    ["$2,450.00", " $95 ", "$24,50.00", "khoảng $300.00", "$95.5", None]
)

# Dữ liệu kiểm thử danh sách tiện nghi JSON
DEMO_LISTINGS = pd.DataFrame(
    {
        "amenities": [
            '["Wifi", "Air conditioning"]',
            '["Wifi, free", "Kitchen"]',
            "[]",
            '["Kitchen"]',
            '["Heating"]',
        ]
    },
    index=[101, 102, 103, 104, 105],
)

# Dữ liệu kiểm thử phân biệt danh sách rỗng và giá trị khuyết thiếu
DEMO_DS_NHO = pd.Series(
    [
        ["Wifi", "Wifi", "Kitchen"],
        ["Kitchen"],
        [],
        None,
        ["Wifi"],
    ],
    index=["P1", "P2", "P3", "P4", "P5"],
)

PAT_ES = r"ción|ñ|muy|excelente|departamento"
PAT_GAN = r"(?:cerca de la |cerca del |cerca de |near the |near )([A-Za-zÁ-Úá-úñÑ]+)"
PAT_GIA = r"\$(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d{2})?"
```

---

## Danh mục bài tập thực hành

<span id="data-lab-07-01"></span>
### Bài 1: Chuẩn hoá chuỗi văn bản trước khi đếm tần suất

::: exercise
Thực hiện thao tác chuẩn hoá định dạng cơ bản cho cột chuỗi ký tự bằng cách loại bỏ khoảng trắng dư thừa ở hai đầu và chuyển toàn bộ về chữ thường. Không tự ý loại bỏ dấu câu nếu quy tắc chưa yêu cầu.

Yêu cầu kỹ thuật:
- Tình huống: Chuỗi văn bản nhập liệu thường xuất hiện khoảng trắng thừa hoặc viết hoa không đồng nhất như `"  Wifi "`, `"wifi"`, `"WIFI!"`, `"wi-fi"`.
- Thao tác: Dùng phương thức `.str.strip()` kết hợp `.str.lower()`.
- Đầu ra: Trả về Series mới đã được chuẩn hoá, giữ nguyên chỉ mục và bảo toàn giá trị khuyết thiếu.
- Trường hợp biên: Dữ liệu chứa phần tử `None` hoặc `np.nan` phải tiếp tục giữ nguyên trạng thái khuyết thiếu sau khi xử lý.
:::

::: solution
#### Cách 1: Chuẩn hóa trực tiếp một Series

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

# Bắt đầu lời giải

s = pd.Series(["  Wifi ", "wifi", "WIFI!", "wi-fi"])
s_chuan = s.str.strip().str.lower()
print("Kết quả chuẩn hoá Cách 1:")
print(s_chuan.tolist())
print(f"Số lượng phần tử bằng đúng wifi: {(s_chuan == 'wifi').sum()}")

# Kết thúc lời giải
```

##### Giải thích Cách 1

`.str` cho phép gọi cùng một phép xử lý chuỗi trên từng ô của Series. `.strip()` bỏ khoảng trắng, dấu tab hoặc ký tự xuống dòng ở hai đầu, rồi `.lower()` đổi chữ hoa thành chữ thường. Chuỗi phương thức đọc từ trái sang phải theo thứ tự biến đổi.

Dấu chấm than trong `WIFI!` nằm trong nội dung cần giữ, nên kết quả là `wifi!`. Dấu nối trong `wi-fi` cũng không bị bỏ. Do đó `(s_chuan == "wifi").sum()` chỉ đếm hai dòng bằng đúng `wifi`, không phải mọi cách viết có thể chỉ cùng tiện nghi.

Các phương thức tạo kết quả mới và giữ chỉ mục. Ô khuyết vẫn ở trạng thái khuyết, còn chuỗi rỗng là một chuỗi có thật, khác ô thiếu dữ liệu. Quy tắc này chỉ chuẩn hóa khoảng trắng ngoài và kiểu chữ, chưa xử lý dấu câu hoặc đồng nhất từ đồng nghĩa.

##### Output Cách 1

| Vị trí | Đầu vào | Kết quả |
|---|---|---|
| 0 | `"  Wifi "` | `wifi` |
| 1 | `wifi` | `wifi` |
| 2 | `WIFI!` | `wifi!` |
| 3 | `wi-fi` | `wi-fi` |

Lệnh đếm bằng đúng `wifi` trả `2`.

#### Cách 2: Đưa quy tắc chuẩn hóa vào một hàm dùng lại

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

# Bắt đầu lời giải


def normalize(s: pd.Series) -> pd.Series:
    """Loại bỏ khoảng trắng hai đầu và chuyển thành chữ thường.

    Tham số s: Series chuỗi nguồn cần chuẩn hoá.
    Trả về: Series chuỗi mới cùng chỉ mục, bảo toàn giá trị khuyết thiếu.
    """
    return s.str.strip().str.lower()


mau_chuoi = pd.Series(["  Wifi ", "wifi", "WIFI!", "wi-fi"])
ket_qua_q1 = normalize(mau_chuoi)
print("Kết quả từ hàm normalize:")
print(ket_qua_q1.tolist())
print(
    f"Kiểm tra bảo toàn giá trị khuyết thiếu: {normalize(pd.Series([' A ', None])).isna().tolist()}"
)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`normalize(s)` nhận Series đầu vào và trả ngay kết quả `.str.strip().str.lower()`. Hàm không nhận tên cột, nên người gọi có thể truyền bất kỳ cột chuỗi nào mà vẫn dùng cùng quy tắc. Việc đặt logic trong hàm giúp sửa hoặc kiểm thử một nơi thay vì chép hai phép xử lý ở nhiều chỗ.

Phần kiểm tra `normalize(pd.Series([" A ", None])).isna()` tạo hai cờ thiếu dữ liệu. Chuỗi đầu thành `a`, nên cờ đầu là `False`. Ô thứ hai vẫn thiếu, nên cờ sau là `True`. Kết quả `[False, True]` kiểm tra trạng thái khuyết, không phải hai chuỗi trả về.

`.lower()` không phải quy tắc đồng nhất mọi cách viết của Unicode hoặc mọi tên tiện nghi. Nếu cần ghép tên từ nhiều ngôn ngữ, có thể phải thống nhất thêm quy tắc mã hóa hoặc dùng `casefold`, nhưng phải kiểm tra tác động trước khi đổi yêu cầu của bài.

##### Output Cách 2

| Vị trí | Đầu vào | Kết quả |
|---|---|---|
| 0 | `"  Wifi "` | `wifi` |
| 1 | `wifi` | `wifi` |
| 2 | `WIFI!` | `wifi!` |
| 3 | `wi-fi` | `wi-fi` |

Kiểm tra ô khuyết in `[False, True]`.

#### So sánh hai cách

Hai cách dùng cùng hai thao tác chuỗi nên cho cùng giá trị. Cách 1 dễ quan sát trên một cột. Cách 2 giúp dùng lại và kiểm thử thống nhất, chứ không tự làm phép xử lý chạy nhanh hơn. Chỉ bổ sung quy tắc loại dấu câu nếu mục tiêu dữ liệu thật sự yêu cầu.

:::

---

<span id="data-lab-07-02"></span>
### Bài 2: Bẫy giá trị thiếu và ký tự đặc biệt trong so khớp chuỗi

::: exercise
Phân tích hiện tượng lỗi logic khi kiểm tra sự tồn tại của chuỗi con trên cột có chứa giá trị khuyết thiếu hoặc chứa ký tự đặc biệt của biểu thức chính quy.

Yêu cầu kỹ thuật:
- Tình huống: Cách xử lý ô thiếu của `s.str.contains("centro")` mặc định phụ thuộc kiểu chuỗi và phiên bản pandas. Cần đặt `na=False` để mọi dòng thiếu nhận cờ không khớp rõ ràng khi đếm hoặc lọc. Ngoài ra, chuỗi tìm kiếm như `"50.000"` nếu không chỉ định `regex=False` sẽ coi dấu chấm là ký tự đại diện cho mọi ký tự.
- Thao tác: Thiết lập rõ ràng hai tham số `regex=False` và `na=False` trong phương thức `.str.contains()`.
- Đầu ra: Trả về số lượng dòng nguyên vẹn chứa đúng chuỗi con chỉ định dưới dạng số nguyên int.
- Trường hợp biên: Tìm kiếm phân biệt hoa thường và chuỗi chứa dấu chấm số thập phân.
:::

::: solution
#### Cách 1: Tạo cờ chứa chuỗi nguyên văn rồi cộng số cờ đúng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

# Bắt đầu lời giải

t = pd.Series(["depto centro", None, "casa con vista"])
so_dong_co_centro = int(t.str.contains("centro", regex=False, na=False).sum())
print(f"Số dòng chứa từ centro: {so_dong_co_centro}")

# Kết thúc lời giải
```

##### Giải thích Cách 1

`str.contains("centro", regex=False, na=False)` hỏi mỗi dòng có chứa đúng chuỗi con `centro` hay không. `regex=False` tắt cách hiểu ký tự đặc biệt của regex, còn `na=False` coi dòng thiếu dữ liệu là không khớp. Kết quả là mặt nạ rõ trạng thái đúng sai cho từng dòng.

`.sum()` cộng các cờ đúng để đếm số dòng khớp. Một dòng có từ lặp nhiều lần vẫn chỉ đóng góp 1, vì `contains` trả một cờ cho cả dòng. `int(...)` đưa số đếm về kiểu số nguyên Python. Phép tìm kiếm vẫn phân biệt hoa thường vì không truyền `case=False`.

Không nên cho rằng mọi cách gọi `contains` mặc định đều làm `.sum()` lỗi. Cách biểu diễn giá trị khuyết phụ thuộc kiểu chuỗi và phiên bản pandas, và phép cộng thường bỏ qua ô thiếu. Đặt `na=False` ở đây giúp quy tắc mặt nạ nhất quán và dễ dùng trong các bước lọc tiếp theo.

##### Output Cách 1

| Dòng | Nội dung | Khớp `centro` |
|---|---|---|
| 0 | `depto centro` | `True` |
| 1 | Khuyết | `False` |
| 2 | `casa con vista` | `False` |

Số dòng chứa `centro` là `1`.

#### Cách 2: Viết hàm đếm với chuỗi tìm kiếm làm tham số

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

# Bắt đầu lời giải


def count_contains(s: pd.Series, tu: str) -> int:
    """Đếm số dòng chứa chuỗi con theo so khớp nguyên văn an toàn.

    Tham số s: Series chuỗi nguồn cần kiểm tra.
    Tham số tu: Chuỗi con cần tìm kiếm nguyên văn.
    Trả về: Số nguyên biểu diễn số dòng thoả mãn điều kiện.
    """
    return int(s.str.contains(tu, regex=False, na=False).sum())


vi_du_t = pd.Series(["depto centro", None, "casa con vista"])
ket_qua_q2 = count_contains(vi_du_t, "centro")
print(f"Đếm từ centro trong vi_du_t: {ket_qua_q2}")

vi_du_gia = pd.Series(["giá 50.000", "giá 50,000"])
print(f"Đếm chuỗi 50.000 nguyên văn: {count_contains(vi_du_gia, '50.000')}")

# Kết thúc lời giải
```

##### Giải thích Cách 2

`count_contains(s, tu)` tách dữ liệu và từ khóa khỏi quy tắc so khớp. Nhờ `regex=False`, từ khóa như `50.000` yêu cầu đúng dấu chấm. Nếu bật regex, dấu `.` có nghĩa một ký tự bất kỳ và có thể khớp cả `50,000`.

`na=False` cho phép cộng cờ hoặc dùng mặt nạ mà không cần thay ô thiếu bằng một chuỗi giả trước. Việc thay thiếu thành chuỗi rỗng có thể hữu ích ở bài khác, nhưng sẽ thay đổi giá trị dữ liệu và cần được cân nhắc riêng.

Hai lần gọi minh họa dùng hai bộ dữ liệu khác nhau. Lần đầu tìm `centro` và có một dòng khớp. Lần sau tìm `50.000` trong hai chuỗi giá, chỉ chuỗi có dấu chấm được tính. So khớp nguyên văn dựa vào ký tự của chuỗi, không phải thao tác so byte hay một phép chuẩn hóa tiền tệ.

##### Output Cách 2

| Lời gọi | Số dòng khớp |
|---|---|
| `count_contains(vi_du_t, "centro")` | 1 |
| `count_contains(vi_du_gia, "50.000")` | 1 |

#### So sánh hai cách

Cách 1 dùng trực tiếp trên một tình huống. Cách 2 cho phép dùng lại với nhiều từ khóa mà vẫn giữ quy tắc khuyết và dấu câu. Cả hai đang đếm dòng chứa chuỗi con. Nếu cần đếm số lần xuất hiện trong mỗi dòng hoặc cần khớp cả từ, phải chọn phép xử lý và mẫu khác.

:::

---

<span id="data-lab-07-03"></span>
### Bài 3: Chuyển đổi định dạng số tiền và phát hiện lỗi đọc dữ liệu

::: exercise
Thực hiện chuyển đổi cột dữ liệu giá tiền từ định dạng chuỗi ký tự sang số thực, đồng thời gắn cờ nhận diện các dòng có dữ liệu nhưng sai quy cách chuyển đổi.

Yêu cầu kỹ thuật:
- Tình huống: Giá tiền dạng chuỗi có thể chứa ký hiệu `$`, dấu phẩy phân cách hàng nghìn, khoảng trắng, hoặc văn bản tự do như `"liên hệ"`, `"từ $500"`.
- Thao tác: Loại bỏ ký hiệu `$` và dấu phẩy `,`, dùng `pd.to_numeric(..., errors='coerce')` để chuyển đổi sang số thực. Sau đó so sánh điều kiện dữ liệu ban đầu không khuyết thiếu nhưng số thực nhận giá trị `NaN` để đánh dấu cờ lỗi đọc.
- Đầu ra: Trả về DataFrame gồm ba cột: `gia` (chuỗi gốc), `gia_so` (số thực sau chuyển đổi) và `loi_doc` (giá trị boolean đánh dấu lỗi).
- Trường hợp biên: Giá trị `None` ban đầu là thiếu tự nhiên, không tính là lỗi đọc (`loi_doc = False`).
:::

::: solution
#### Cách 1: Làm sạch chuỗi rồi giữ cờ chuyển đổi thất bại

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

# Bắt đầu lời giải

gia_raw = pd.Series(["$1,200.00", " $850.00 ", None, "liên hệ", "từ $500"])
gia_clean = (
    gia_raw.str.strip()
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)
gia_num = pd.to_numeric(gia_clean, errors="coerce")
loi = gia_raw.notna() & gia_num.isna()

df_gia_cach1 = pd.DataFrame({"gia": gia_raw, "gia_so": gia_num, "loi_doc": loi})
display(df_gia_cach1)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`.str.strip()` bỏ khoảng trắng ở hai đầu, rồi hai lần `.replace(..., regex=False)` xóa ký hiệu đô la và dấu phẩy. `pd.to_numeric(..., errors="coerce")` thử đọc chuỗi còn lại như một số. Các chữ `liên hệ` và tiền tố `từ` không bị xóa, nên hai dòng đó không chuyển được.

`gia_raw.notna()` đánh dấu nơi nguồn thật sự có dữ liệu. `gia_num.isna()` đánh dấu nơi kết quả số đang khuyết. Phép `&` chỉ giữ cờ đúng nếu đồng thời có dữ liệu gốc và chuyển đổi thất bại. Vì vậy ô `None` không bị báo lỗi đọc.

`pd.DataFrame({...})` ghép ba Series theo cùng chỉ mục để giữ chuỗi gốc cạnh số và cờ lỗi. `display` trong notebook hiển thị bảng với tiêu đề cột và từng hàng, giúp nhìn đúng dòng phải rà lại thay vì chỉ biết có hai ô khuyết mới.

##### Output Cách 1

| Vị trí | `gia` | `gia_so` | `loi_doc` |
|---|---|---|---|
| 0 | `$1,200.00` | 1200.0 | `False` |
| 1 | `" $850.00 "` | 850.0 | `False` |
| 2 | Khuyết | `NaN` | `False` |
| 3 | `liên hệ` | `NaN` | `True` |
| 4 | `từ $500` | `NaN` | `True` |

#### Cách 2: Đóng gói chuyển đổi và chẩn đoán trong cùng hàm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

DEMO_PRICES = pd.Series(["$1,200.00", " $850.00 ", None, "liên hệ", "từ $500"])

# Bắt đầu lời giải


def parse_price(gia: pd.Series) -> pd.DataFrame:
    """Chuyển đổi chuỗi giá tiền sang số thực và gắn cờ các dòng lỗi định dạng.

    Tham số gia: Series chuỗi giá tiền cần xử lý.
    Trả về: DataFrame gồm cột gia gốc, gia_so sau chuyển đổi và cờ loi_doc.
    """
    gia_sach = (
        gia.str.strip()
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )
    gia_so = pd.to_numeric(gia_sach, errors="coerce")
    loi_doc = gia.notna() & gia_so.isna()
    return pd.DataFrame({"gia": gia, "gia_so": gia_so, "loi_doc": loi_doc})


df_ket_qua_gia = parse_price(DEMO_PRICES)
display(df_ket_qua_gia)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`parse_price(gia)` nhận một Series giá và tạo hai Series mới là `gia_so` và `loi_doc`. Kết quả DataFrame giữ cột `gia` gốc để người học truy lại nguyên nhân của từng cờ lỗi. Chỉ mục được pandas căn chỉnh khi dựng bảng, nên các Series phải cùng xuất phát từ đầu vào đó.

`errors="coerce"` không xác thực quy cách tiền tệ trước khi đọc số. Chẳng hạn xóa dấu phẩy trong một chuỗi viết sai dấu nhóm vẫn có thể tạo một số đọc được. Bài tiếp theo dùng `fullmatch` để kiểm tra toàn bộ cấu trúc, đây là mục tiêu khác với chỉ thử chuyển sang số.

Hàm không tự lấy `500` từ chuỗi `từ $500`, vì điều đó sẽ bỏ mất ý nghĩa giá bắt đầu từ một ngưỡng. Giữ lỗi để kiểm tra phù hợp hơn việc âm thầm diễn giải lại quy tắc dữ liệu.

##### Output Cách 2

| Vị trí | `gia` | `gia_so` | `loi_doc` |
|---|---|---|---|
| 0 | `$1,200.00` | 1200.0 | `False` |
| 1 | `" $850.00 "` | 850.0 | `False` |
| 2 | Khuyết | `NaN` | `False` |
| 3 | `liên hệ` | `NaN` | `True` |
| 4 | `từ $500` | `NaN` | `True` |

#### So sánh hai cách

Cách 1 giúp theo dõi từng Series trung gian. Cách 2 giữ một giao diện đầu vào và một bảng chẩn đoán dùng lại được. Hai cách có cùng thuật toán, chưa có khác biệt hiệu năng được đo. Điều cốt lõi là tách dữ liệu vốn thiếu với dữ liệu hiện diện nhưng không đọc được.

:::

---

<span id="data-lab-07-04"></span>
### Bài 4: Xác thực toàn bộ chuỗi định dạng tiền tệ bằng biểu thức chính quy

::: exercise
Kiểm tra tính hợp lệ toàn diện của chuỗi biểu diễn số tiền bằng cách đối chiếu toàn bộ cấu trúc với mẫu biểu thức chính quy quy định, tránh việc chỉ kiểm tra một phần chuỗi gây lọt dữ liệu sai.

Yêu cầu kỹ thuật:
- Tình huống: Một chuỗi như `"$24,50.00"` đặt sai dấu phẩy, `"khoảng $300.00"` thừa từ ngữ, hoặc `"$95.5"` thiếu một chữ số thập phân đều là chuỗi không hợp lệ. Nếu dùng `.str.contains()` hoặc `.str.extract()`, phần con `$300.00` vẫn có thể bị nhận nhầm là hợp lệ.
- Thao tác: Dùng `s.str.strip().str.fullmatch(pattern, na=False)` với mẫu `PAT_GIA = r"\$(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d{2})?"`.
- Đầu ra: Series kiểu boolean cùng chỉ mục, trả về `True` nếu toàn bộ chuỗi khớp hoàn toàn với mẫu quy chuẩn.
- Trường hợp biên: Chuỗi có khoảng trắng ở hai đầu cần được gọt bỏ trước khi đối chiếu, giá trị khuyết thiếu trả về `False`.
:::

::: solution
#### Cách 1: Kiểm tra toàn bộ chuỗi với fullmatch

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

# Bắt đầu lời giải

gia_test = pd.Series(
    ["$2,450.00", " $95 ", "$24,50.00", "khoảng $300.00", "$95.5", None]
)
pat_gia = r"\$(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d{2})?"
hop_le_cach1 = gia_test.str.strip().str.fullmatch(pat_gia, na=False)
df_kiem_tra_gia = pd.DataFrame({"chuoi_gia": gia_test, "hop_le": hop_le_cach1})
display(df_kiem_tra_gia)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`.str.strip()` chuẩn hóa hai đầu trước khi kiểm tra. `.str.fullmatch(pat_gia, na=False)` yêu cầu toàn bộ chuỗi còn lại phù hợp mẫu, nên một đoạn con `$300.00` nằm trong `khoảng $300.00` không đủ làm cả dòng hợp lệ. `na=False` cho đầu vào thiếu cờ `False`.

Trong mẫu, `\$` khớp dấu đô la thật. Nhánh `\d{1,3}(?:,\d{3})+` nhận một đến ba chữ số đầu, theo sau là ít nhất một nhóm dấu phẩy và đúng ba chữ số. Nhánh `\d+` nhận số không có dấu nhóm. Dấu `|` chọn một trong hai dạng đó.

Cụm `(?:\.\d{2})?` cho phép bỏ hẳn phần thập phân hoặc dùng dấu chấm với đúng hai chữ số. Vì thế `$95` hợp lệ, còn `$95.5` không hợp lệ. `(?:...)` gom các thành phần mẫu mà không tạo thêm nhóm bắt để trích dữ liệu.

##### Output Cách 1

| Vị trí | Chuỗi giá | `hop_le` |
|---|---|---|
| 0 | `$2,450.00` | `True` |
| 1 | `" $95 "` | `True` |
| 2 | `$24,50.00` | `False` |
| 3 | `khoảng $300.00` | `False` |
| 4 | `$95.5` | `False` |
| 5 | Khuyết | `False` |

#### Cách 2: Đưa mẫu kiểm tra thành tham số của hàm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

DEMO_PRICES_TEST = pd.Series(
    ["$2,450.00", " $95 ", "$24,50.00", "khoảng $300.00", "$95.5", None]
)

PAT_GIA = r"\$(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d{2})?"

# Bắt đầu lời giải


def validate_price_fullmatch(s: pd.Series, pattern: str = PAT_GIA) -> pd.Series:
    """Xác thực toàn bộ chuỗi có tuân thủ cấu trúc giá tiền hợp lệ hay không.

    Tham số s: Series chuỗi cần kiểm tra.
    Tham số pattern: Biểu thức chính quy quy chuẩn cấu trúc số tiền.
    Trả về: Series kiểu bool đánh dấu tính hợp lệ của từng dòng.
    """
    return s.str.strip().str.fullmatch(pattern, na=False)


ket_qua_hop_le = validate_price_fullmatch(DEMO_PRICES_TEST)
display(pd.DataFrame({"gia_test": DEMO_PRICES_TEST, "hop_le": ket_qua_hop_le}))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`validate_price_fullmatch(s, pattern=PAT_GIA)` dùng mẫu mặc định nhưng cho phép truyền mẫu khác khi quy tắc dữ liệu đổi. Hàm trả Series cờ có cùng chỉ mục, nên có thể dùng trực tiếp để chọn các dòng cần kiểm tra bằng `s[~kết_quả]`.

Giữ mẫu ở một nơi giúp tránh việc hai cột được kiểm tra bằng hai quy tắc hơi khác nhau. Tuy nhiên, thay mẫu là thay tiêu chuẩn chấp nhận dữ liệu, không phải chỉ thay cách viết code. Mẫu đang dùng chưa nhận số âm, ký hiệu tiền khác hoặc dấu phẩy thập phân.

`fullmatch` kiểm tra toàn chuỗi theo cơ chế của thư viện regex. Không nên diễn giải nó đơn giản thành việc tự gắn hai ký tự `^` và `$`, vì các neo có quy tắc riêng, chẳng hạn với ký tự xuống dòng. Điều cần nắm ở đây là cả chuỗi phải được mẫu bao phủ.

##### Output Cách 2

| Vị trí | Chuỗi giá | `hop_le` |
|---|---|---|
| 0 | `$2,450.00` | `True` |
| 1 | `" $95 "` | `True` |
| 2 | `$24,50.00` | `False` |
| 3 | `khoảng $300.00` | `False` |
| 4 | `$95.5` | `False` |
| 5 | Khuyết | `False` |

#### So sánh hai cách

Hai cách xác thực cùng một mẫu nên cho cùng sáu cờ. Cách 1 thuận tiện để thử và hiểu từng mảnh regex. Cách 2 giúp tái sử dụng tiêu chuẩn. Kiểm tra hợp lệ chỉ cho biết đúng cú pháp đã quy định, chưa chứng minh mức giá hợp lý hay đúng đơn vị tiền.

:::

---

<span id="data-lab-07-05"></span>
### Bài 5: Khảo sát tổng quan cột chữ và phân bố độ dài văn bản

::: exercise
Thực hiện khảo sát tổng thể trên một cột văn bản lớn để đánh giá số lượng giá trị khuyết thiếu, đo lường độ dài ký tự và nhận diện các đoạn văn bản quá ngắn ít mang lại giá trị phân tích.

Yêu cầu kỹ thuật:
- Tình huống: Trong tập dữ liệu đánh giá thực tế, một số dòng bị bỏ trống hoặc chỉ chứa một ký tự dấu câu như `"."`, `"Ok"`. Khảo sát độ dài trung vị và các chuỗi ngắn giúp chọn quy tắc xử lý phù hợp với mục tiêu phân tích.
- Thao tác: Đếm số lượng `NaN`, tính độ dài chuỗi bằng `.str.len()`, tính giá trị trung vị trên các dòng có dữ liệu và đếm số dòng có độ dài nhỏ hơn ngưỡng quy định.
- Đầu ra: Trả về từ điển gồm 4 khóa: `so_nan` (int), `so_con` (int), `do_dai_tv` (float) và `so_ngan` (int).
- Trường hợp biên: Dữ liệu mẫu rỗng hoặc chuỗi rỗng có độ dài bằng 0.
:::

::: solution
#### Cách 1: Tính riêng từng chỉ số của cột văn bản

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

# Bắt đầu lời giải

so_nan_c1 = int(DEMO_COMMENTS.isna().sum())
c_hop_le = DEMO_COMMENTS.dropna()
so_con_c1 = int(len(c_hop_le))
do_dai_chuoi = c_hop_le.str.len()
do_dai_tv_c1 = float(do_dai_chuoi.median())
so_ngan_c1 = int((do_dai_chuoi < 20).sum())

print(f"Số giá trị khuyết thiếu: {so_nan_c1}")
print(f"Số dòng có dữ liệu: {so_con_c1}")
print(f"Trung vị độ dài ký tự: {do_dai_tv_c1}")
print(f"Số đoạn ngắn hơn 20 ký tự: {so_ngan_c1}")

# Kết thúc lời giải
```

##### Giải thích Cách 1

`.isna().sum()` đếm một ô khuyết. `.dropna()` lấy 15 dòng còn có dữ liệu, nhưng không loại chuỗi rỗng, dấu chấm hoặc từ `Ok`. Vì vậy `so_con` là số dòng không khuyết, chưa phải số đánh giá đủ nội dung cho mọi mục đích phân tích.

`.str.len()` đo số ký tự trong từng chuỗi. Chuỗi rỗng có độ dài 0 và vẫn tham gia thống kê. `.median()` lấy trung vị 15 độ dài, được `39.0`. Ba chuỗi dưới 20 ký tự là `.`, `Ok` và chuỗi rỗng. Phép `< 20` không tính một chuỗi dài đúng 20 ký tự.

Dữ liệu tại bước này chưa thay thẻ `<br/>`, nên các ký tự của thẻ cũng nằm trong độ dài. Với Unicode, số ký tự được thư viện đếm không luôn bằng số ký tự người đọc cảm nhận nếu có dấu tổ hợp. Cần giữ cùng bước chuẩn hóa trước khi so các chỉ số giữa hai tập.

##### Output Cách 1

| Khóa kết quả | Giá trị |
|---|---|
| `so_nan` | 1 |
| `so_con` | 15 |
| `do_dai_tv` | 39.0 |
| `so_ngan` | 3 |

#### Cách 2: Đưa ngưỡng độ dài vào hàm khảo sát

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

# Bắt đầu lời giải


def text_overview(comments: pd.Series, nguong_ngan: int = 20) -> dict:
    """Khảo sát số lượng khuyết thiếu, trung vị độ dài và số lượng đoạn văn ngắn.

    Tham số comments: Series văn bản cần khảo sát.
    Tham số nguong_ngan: Ngưỡng độ dài ký tự dùng để xác định đoạn văn bản ngắn.
    Trả về: Từ điển chứa các chỉ số thống kê tổng quan.
    """
    so_nan = int(comments.isna().sum())
    c = comments.dropna()
    so_con = int(len(c))
    do_dai = c.str.len()
    do_dai_tv = float(do_dai.median()) if so_con > 0 else 0.0
    so_ngan = int((do_dai < nguong_ngan).sum())
    return {
        "so_nan": so_nan,
        "so_con": so_con,
        "do_dai_tv": do_dai_tv,
        "so_ngan": so_ngan,
    }


tong_quan_demo = text_overview(DEMO_COMMENTS, nguong_ngan=20)
print("Hồ sơ thống kê văn bản từ text_overview:")
print(tong_quan_demo)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`nguong_ngan=20` là giá trị mặc định nhưng người gọi có thể đổi mà không sửa thân hàm. Hàm vẫn chỉ tính `.str.len()` một lần rồi dùng Series độ dài đó cho cả trung vị và số chuỗi ngắn.

Điều kiện `if so_con > 0` xử lý trường hợp không còn dòng nào sau khi bỏ khuyết. Đoạn mã quy ước trả `do_dai_tv=0.0` trong trường hợp ấy. Cần phân biệt đây là giá trị quy ước của hàm với trung vị của một mẫu rỗng, vốn không được xác định. Khi làm báo cáo, có thể cần trả `NaN` để tránh nhầm mẫu rỗng với tập toàn chuỗi rỗng.

Từ điển có đúng bốn khóa giúp người gọi kiểm tra hoặc ghép vào báo cáo chất lượng. `int` và `float` cố định kiểu vô hướng ở giao diện trả về, còn dữ liệu nguồn được giữ nguyên.

##### Output Cách 2

| Khóa kết quả | Giá trị |
|---|---|
| `so_nan` | 1 |
| `so_con` | 15 |
| `do_dai_tv` | 39.0 |
| `so_ngan` | 3 |

#### So sánh hai cách

Cách 1 mở rõ cách tính và dữ liệu ở từng bước. Cách 2 thuận tiện để chạy cùng một khảo sát trên nhiều cột hoặc nhiều ngưỡng. Các con số là thông tin mô tả, chưa tự đưa ra quy tắc xóa văn bản. Cần quyết định mục tiêu phân tích trước khi loại các chuỗi ngắn.

:::

---

<span id="data-lab-07-06"></span>
### Bài 6: Làm sạch thẻ ngắt dòng HTML đã biết và kiểm chứng bảo toàn độ dài

::: exercise
Thực hiện thay thế đúng chuỗi thẻ ngắt dòng `<br/>` trong văn bản bằng một dấu cách, bảo toàn tính nguyên vẹn của văn bản gốc và kiểm chứng bằng công thức toán học về độ dài ký tự.

Yêu cầu kỹ thuật:
- Tình huống: Hệ thống Airbnb lưu các vị trí xuống dòng bằng chuỗi cố định `"<br/>"`. Mỗi thẻ này gồm đúng 5 ký tự. Khi thay một thẻ bằng 1 dấu cách, độ dài của văn bản sẽ giảm đi đúng 4 ký tự và số lượng dấu cách tăng thêm đúng 1.
- Thao tác: Đếm số dòng chứa `"<br/>"`, dùng `.str.replace("<br/>", " ", regex=False)` để thay thế, bảo toàn giá trị khuyết thiếu và chỉ mục.
- Đầu ra: Trả về từ điển gồm hai khóa: `so_br` (int) và `c_sach` (Series chuỗi đã được làm sạch).
- Trường hợp biên: Không thay thế các thẻ HTML khác ngoài quy cách như `"<br>"` hay `"<p>"`, giữ nguyên giá trị `NaN`.
:::

::: solution
#### Cách 1: Đếm dòng có thẻ rồi thay đúng chuỗi br

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

# Bắt đầu lời giải

so_br_c1 = int(DEMO_COMMENTS.str.contains("<br/>", regex=False, na=False).sum())
c_sach_c1 = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
con_br = int(c_sach_c1.str.contains("<br/>", regex=False, na=False).sum())
print(f"Số dòng chứa br ban đầu: {so_br_c1}")
print(f"Số dòng chứa br sau làm sạch: {con_br}")

# Kết thúc lời giải
```

##### Giải thích Cách 1

`str.contains("<br/>", regex=False, na=False)` trả một cờ cho mỗi dòng. `.sum()` vì thế cho số dòng có ít nhất một thẻ, không phải tổng số thẻ. DEMO có ba dòng như vậy, trong đó dòng chỉ mục 6 chứa hai thẻ.

`str.replace("<br/>", " ", regex=False)` thay mỗi lần xuất hiện đúng chuỗi đã biết bằng một dấu cách. Những thẻ khác như `<br>` giữ nguyên. Việc chọn dấu cách giúp hai từ ở hai phía không bị dính liền sau khi bỏ thẻ.

Phép kiểm tra sau thay thế cho biết còn bao nhiêu dòng chứa đúng thẻ cũ. Kết quả 0 xác nhận đã xử lý hết dạng đang xét. Nó không chứng minh văn bản không còn mọi thẻ HTML khác.

##### Output Cách 1

| Chỉ số | Giá trị |
|---|---|
| Dòng có ít nhất một `<br/>` trước xử lý | 3 |
| Dòng còn đúng thẻ ấy sau xử lý | 0 |
| Tổng số thẻ trong ba dòng | 4 |

#### Cách 2: Gói quy tắc và kiểm tra mức giảm độ dài

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

# Bắt đầu lời giải


def clean_br(comments: pd.Series) -> dict:
    """Thay thế chính xác thẻ <br/> bằng một khoảng trắng và thống kê số dòng chứa thẻ.

    Tham số comments: Series chuỗi nguồn cần làm sạch.
    Trả về: Từ điển chứa số dòng phát hiện so_br và Series đã làm sạch c_sach.
    """
    so_br = int(comments.str.contains("<br/>", regex=False, na=False).sum())
    c_sach = comments.str.replace("<br/>", " ", regex=False)
    return {"so_br": so_br, "c_sach": c_sach}


ket_qua_br = clean_br(DEMO_COMMENTS)
print(f"Số dòng có thẻ br: {ket_qua_br['so_br']}")
print("Mẫu dòng số 6 sau khi làm sạch:")
print(f"'{ket_qua_br['c_sach'].iloc[6]}'")

# Kiểm chứng tính giảm độ dài: Mỗi lần xuất hiện giảm đúng 4 ký tự
c_khong_nan = DEMO_COMMENTS.dropna()
so_the_tong = c_khong_nan.str.count("<br/>").sum()
do_dai_giam = (
    c_khong_nan.str.len().sum() - ket_qua_br["c_sach"].dropna().str.len().sum()
)
print(
    f"Tổng số thẻ br xuất hiện: {so_the_tong}, Độ dài giảm: {do_dai_giam} ký tự (Khớp 4 * {so_the_tong} = {4 * so_the_tong})"
)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`clean_br` trả cả số dòng có thẻ lẫn Series đã làm sạch, giúp giữ phép biến đổi cùng thông tin kiểm tra. Trong phần kiểm chứng, `.str.count("<br/>")` đếm số lần xuất hiện trong mỗi dòng, rồi `.sum()` cộng lại thành tổng bốn thẻ. Mẫu này không có ký tự regex làm đổi cách hiểu chuỗi cần tìm.

Mỗi thẻ gồm năm ký tự và được thay bằng một dấu cách, nên mỗi lần thay giảm bốn ký tự. Bốn lần thay làm tổng độ dài giảm 16. Đếm dòng với `contains` và đếm lần xuất hiện với `count` là hai phép đo khác nhau, dù cùng làm việc trên một chuỗi thẻ.

Đối chiếu độ dài là một cách kiểm tra tác động cụ thể của phép biến đổi. Nó chưa chứng minh nội dung được hiểu đúng về ngữ nghĩa. Dòng thiếu dữ liệu vẫn thiếu sau xử lý, không bị biến thành chữ `None` hoặc chuỗi rỗng.

##### Output Cách 2

| Đại lượng | Output |
|---|---|
| `so_br` | 3 |
| Tổng số thẻ | 4 |
| Tổng độ dài giảm | 16 ký tự |
| Dòng chỉ mục 6 sau xử lý | `Nice host. Near Movistar Arena! Recommended.` |

#### So sánh hai cách

Cách 1 phù hợp để quan sát một phép thay thế đã biết. Cách 2 bổ sung hàm dùng lại và một kiểm tra độc lập bằng độ dài. Cả hai chỉ xử lý đúng chuỗi `<br/>`. Làm sạch HTML tổng quát cần công cụ phân tích cấu trúc và quy tắc giữ nội dung rõ ràng.

:::

---

<span id="data-lab-07-07"></span>
### Bài 7: Xây dựng quy tắc từ khoá nhận diện ngôn ngữ văn bản

::: exercise
Thiết lập một quy tắc xấp xỉ sử dụng biểu thức chính quy từ khoá để phân loại sơ bộ các đoạn đánh giá bằng tiếng Tây Ban Nha và đo lường tỷ lệ bao phủ của quy tắc.

Yêu cầu kỹ thuật:
- Tình huống: Santiago là thành phố sử dụng tiếng Tây Ban Nha. Có thể xây dựng một bộ từ khoá đặc trưng ban đầu gồm `PAT_ES = r"ción|ñ|muy|excelente|departamento"` để làm mốc phân loại cơ sở.
- Thao tác: Kiểm tra sự xuất hiện của mẫu không phân biệt hoa thường bằng `comments.str.contains(pattern, case=False, na=False)`.
- Đầu ra: Trả về từ điển gồm hai khóa: `la_es` (Series boolean cùng chỉ mục) và `ty_le_es` (float biểu thị tỷ lệ dòng thoả mãn trên tổng số dòng đầu vào).
- Trường hợp biên: Giá trị khuyết thiếu nhận giá trị `False`, phân tích rõ các trường hợp nhận diện nhầm (như câu tiếng Anh chứa từ mượn) và trường hợp bỏ sót (câu tiếng Tây Ban Nha không chứa từ khoá trong danh sách).
:::

::: solution
#### Cách 1: Tìm các dấu hiệu bằng contains

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
c_sach_full = c_sach_demo.copy()

PAT_ES = r"ción|ñ|muy|excelente|departamento"

# Bắt đầu lời giải

c_sach_demo = DEMO_COMMENTS.dropna().str.replace("<br/>", " ", regex=False)
la_es_c1 = c_sach_demo.str.contains(PAT_ES, case=False, na=False)
ty_le_es_c1 = float(la_es_c1.sum() / len(c_sach_demo))
print(f"Số dòng nhận diện tiếng Tây Ban Nha: {la_es_c1.sum()}/{len(c_sach_demo)}")
print(f"Tỷ lệ bao phủ: {ty_le_es_c1:.3f}")

# Kết thúc lời giải
```

##### Giải thích Cách 1

`PAT_ES` dùng dấu `|` để chọn một trong các đoạn `ción`, `ñ`, `muy`, `excelente`, `departamento`. `.str.contains(..., case=False, na=False)` chỉ cần một đoạn khớp ở bất kỳ vị trí nào để trả `True`. `case=False` cho phép nhận cả `Excelente` và `excelente`.

Ví dụ bỏ ô khuyết rồi thay `<br/>` trước khi phân loại, nên mẫu số là 15, không phải toàn bộ 16 dòng ban đầu. Chuỗi rỗng vẫn nằm trong mẫu số và không khớp. Bảy cờ đúng tạo tỷ lệ `7 / 15`.

Tỷ lệ này đo phần văn bản khớp một quy tắc từ khóa, không đo độ chính xác nhận diện ngôn ngữ. Câu `The departamento was great, near the mall.` khớp dù mạch câu chủ yếu là tiếng Anh. Câu `Todo perfecto. Volvería sin duda.` không khớp dù là tiếng Tây Ban Nha. Hai ví dụ cho thấy cả nhận nhầm lẫn bỏ sót.

##### Output Cách 1

| Kết quả trên c_sach_demo | Số dòng |
|---|---|
| Khớp quy tắc `PAT_ES` | 7 |
| Không khớp quy tắc | 8 |
| Tổng dòng không khuyết được xét | 15 |

Tỷ lệ `7 / 15` làm tròn ba chữ số là `0.467`.

#### Cách 2: Trả cờ từng dòng và tỷ lệ từ một hàm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
c_sach_full = c_sach_demo.copy()

PAT_ES = r"ción|ñ|muy|excelente|departamento"

# Bắt đầu lời giải


def language_flag(comments: pd.Series, pattern: str = PAT_ES) -> dict:
    """Tạo cờ nhận diện ngôn ngữ theo quy tắc từ khoá và tính tỷ lệ bao phủ.

    Tham số comments: Series chuỗi cần phân loại.
    Tham số pattern: Biểu thức chính quy chứa các từ khoá đặc trưng.
    Trả về: Từ điển chứa cờ la_es kiểu bool và tỷ lệ ty_le_es.
    """
    la_es = comments.str.contains(pattern, case=False, na=False)
    ty_le_es = float(la_es.sum() / len(comments)) if len(comments) > 0 else 0.0
    return {"la_es": la_es, "ty_le_es": ty_le_es}


ket_qua_es = language_flag(c_sach_demo)
print(
    f"Kết quả phân loại ngôn ngữ: {ket_qua_es['la_es'].sum()} dòng, tỷ lệ {ket_qua_es['ty_le_es']:.3f}"
)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`language_flag` nhận cả Series và mẫu, nên có thể thử một bộ dấu hiệu mới mà không thay các bước tính tỷ lệ. `la_es` giữ chỉ mục đầu vào để các phép lọc phía sau chọn đúng văn bản. `la_es.sum()` đếm cờ đúng, còn `len(comments)` là mẫu số của lần gọi.

Nhánh `if len(comments) > 0 else 0.0` tránh chia cho 0 khi đầu vào rỗng. Số 0 khi đó là quy ước trả về của hàm, không phải bằng chứng không có tiếng Tây Ban Nha trong một quần thể đã quan sát.

Lần gọi đang dùng `c_sach_demo` đã bỏ khuyết nên giữ tỷ lệ như Cách 1. Nếu gọi hàm trên Series gốc có một ô khuyết, `na=False` làm cờ ở ô ấy sai nhưng `len` vẫn tính dòng đó, khiến tỷ lệ thành `7 / 16`. Cần chọn và công bố mẫu số trước khi so sánh các kết quả.

##### Output Cách 2

| Kết quả trên c_sach_demo | Số dòng |
|---|---|
| Khớp quy tắc `PAT_ES` | 7 |
| Không khớp quy tắc | 8 |
| Tổng dòng không khuyết được xét | 15 |

Tỷ lệ `7 / 15` làm tròn ba chữ số là `0.467`.

#### So sánh hai cách

Hai cách dùng cùng quy tắc xấp xỉ. Cách 2 giúp giữ cờ và tỷ lệ trong một cấu trúc dùng lại, chưa biến quy tắc thành mô hình nhận diện ngôn ngữ chính xác. Nên gọi hai nhóm là khớp và không khớp quy tắc khi diễn giải, thay vì mặc nhiên coi đó là hai ngôn ngữ đã được xác nhận.

:::

---

<span id="data-lab-07-08"></span>
### Bài 8: So sánh trung vị độ dài văn bản theo nhóm ngôn ngữ

::: exercise
Thực hiện phân nhóm dữ liệu văn bản theo cờ nhận diện ngôn ngữ và so sánh chỉ số độ dài trung vị của hai nhóm mà không sử dụng vòng lặp Python.

Yêu cầu kỹ thuật:
- Tình huống: Người phân tích cần tìm hiểu xem các đánh giá bằng ngôn ngữ bản địa có xu hướng viết dài hơn hoặc ngắn hơn so với các đánh giá bằng ngôn ngữ khác hay không.
- Thao tác: Dùng mặt nạ boolean `flag` để lọc hai tập con `comments[flag]` và `comments[~flag]`, sau đó gọi phương thức `.str.len().median()` trên từng tập.
- Đầu ra: Trả về từ điển gồm hai khóa: `len_es` (float) và `len_khac` (float).
- Trường hợp biên: Series đầu vào không chứa giá trị khuyết thiếu và mỗi nhóm có ít nhất một dòng dữ liệu.
:::

::: solution
#### Cách 1: Tính độ dài một lần rồi lọc hai nhóm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
c_sach_full = c_sach_demo.copy()

PAT_ES = r"ción|ñ|muy|excelente|departamento"


def language_flag(comments: pd.Series, pattern: str = PAT_ES) -> dict:
    """Tạo cờ nhận diện ngôn ngữ theo quy tắc từ khoá và tính tỷ lệ bao phủ.

    Tham số comments: Series chuỗi cần phân loại.
    Tham số pattern: Biểu thức chính quy chứa các từ khoá đặc trưng.
    Trả về: Từ điển chứa cờ la_es kiểu bool và tỷ lệ ty_le_es.
    """
    la_es = comments.str.contains(pattern, case=False, na=False)
    ty_le_es = float(la_es.sum() / len(comments)) if len(comments) > 0 else 0.0
    return {"la_es": la_es, "ty_le_es": ty_le_es}


ket_qua_es = language_flag(c_sach_demo)
flag_es = ket_qua_es["la_es"]
flag_es_demo = flag_es.copy()

# Bắt đầu lời giải

do_dai_series = c_sach_demo.str.len()
flag_es = ket_qua_es["la_es"]

len_es_c1 = float(do_dai_series[flag_es].median())
len_khac_c1 = float(do_dai_series[~flag_es].median())

print(f"Trung vị độ dài nhóm es: {len_es_c1} ký tự")
print(f"Trung vị độ dài nhóm khác: {len_khac_c1} ký tự")

# Kết thúc lời giải
```

##### Giải thích Cách 1

`c_sach_demo.str.len()` đo độ dài của văn bản đã làm sạch thẻ. `flag_es` là Series cờ cùng chỉ mục. Dùng `do_dai_series[flag_es]` lấy độ dài của các dòng khớp, còn `~flag_es` đảo `True` và `False` để chọn các dòng không khớp.

`.median()` sắp theo giá trị độ dài để tìm điểm giữa, không dựa vào thứ tự văn bản trong bảng. Nhóm bảy dòng khớp có trung vị `47.0`. Nhóm tám dòng không khớp có trung vị là trung bình hai độ dài giữa, được `34.5`.

Mặt nạ cần có chỉ mục tương ứng với cột văn bản. Không lấy một mảng cờ từ bảng đã sắp khác thứ tự rồi coi nó tự khớp theo vị trí. Đây là lý do giữ các Series và chỉ mục xuyên suốt quy trình.

##### Output Cách 1

| Nhóm cờ | Số dòng | Trung vị độ dài |
|---|---|---|
| `True` | 7 | 47.0 |
| `False` | 8 | 34.5 |

#### Cách 2: Viết hàm so sánh độ dài theo Series cờ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
c_sach_full = c_sach_demo.copy()

PAT_ES = r"ción|ñ|muy|excelente|departamento"


def language_flag(comments: pd.Series, pattern: str = PAT_ES) -> dict:
    """Tạo cờ nhận diện ngôn ngữ theo quy tắc từ khoá và tính tỷ lệ bao phủ.

    Tham số comments: Series chuỗi cần phân loại.
    Tham số pattern: Biểu thức chính quy chứa các từ khoá đặc trưng.
    Trả về: Từ điển chứa cờ la_es kiểu bool và tỷ lệ ty_le_es.
    """
    la_es = comments.str.contains(pattern, case=False, na=False)
    ty_le_es = float(la_es.sum() / len(comments)) if len(comments) > 0 else 0.0
    return {"la_es": la_es, "ty_le_es": ty_le_es}


ket_qua_es = language_flag(c_sach_demo)
flag_es = ket_qua_es["la_es"]
flag_es_demo = flag_es.copy()

# Bắt đầu lời giải


def median_length_by_flag(comments: pd.Series, flag: pd.Series) -> dict:
    """So sánh độ dài trung vị giữa hai nhóm phân loại theo cờ boolean.

    Tham số comments: Series chuỗi không chứa giá trị khuyết thiếu.
    Tham số flag: Series kiểu bool cùng chỉ mục với comments.
    Trả về: Từ điển chứa trung vị độ dài len_es và len_khac.
    """
    len_es = float(comments[flag].str.len().median()) if flag.any() else 0.0
    len_khac = float(comments[~flag].str.len().median()) if (~flag).any() else 0.0
    return {"len_es": len_es, "len_khac": len_khac}


ket_qua_do_dai = median_length_by_flag(c_sach_demo, flag_es)
print("Kết quả so sánh trung vị độ dài từ median_length_by_flag:")
print(ket_qua_do_dai)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`median_length_by_flag` nhận văn bản và cờ thành hai đối số để dùng lại cho bất kỳ quy tắc phân nhóm nào. `comments[flag].str.len().median()` chọn đúng nhóm rồi đo độ dài và tính trung vị. `(~flag).any()` kiểm tra có ít nhất một dòng trong nhóm đối diện hay không.

Các nhánh điều kiện trong hàm trả `0.0` khi không có dòng của một nhóm. Đây là giá trị dự phòng do mã lựa chọn, không phải trung vị toán học của mẫu rỗng. Theo giả thiết của bài, mỗi nhóm đều có dữ liệu nên hai nhánh dự phòng chưa được dùng.

Hàm gọi `.str.len()` trên hai tập con thay vì tính một Series độ dài chung như Cách 1. Hai cách có cùng kết quả trên dữ liệu đã cho. Việc đóng gói giúp tái sử dụng, nhưng không đủ để khẳng định hiệu năng tốt hơn.

##### Output Cách 2

| Nhóm cờ | Số dòng | Trung vị độ dài |
|---|---|---|
| `True` | 7 | 47.0 |
| `False` | 8 | 34.5 |

#### So sánh hai cách

Cách 1 thuận tiện khi cần dùng lại cột độ dài cho nhiều thống kê. Cách 2 có giao diện rõ để tích hợp vào quy trình phân nhóm. Hai trung vị chỉ mô tả những nhóm do quy tắc từ khóa tạo ra trong mẫu này. Chưa thể suy ra người dùng một ngôn ngữ nói chung viết dài hơn.

:::

---

<span id="data-lab-07-09"></span>
### Bài 9: Trích xuất thực thể vị trí đứng sau từ chỉ phương hướng

::: exercise
Sử dụng biểu thức chính quy có nhóm bắt để trích xuất từ đầu tiên đứng ngay sau các cụm từ chỉ phương hướng và khoảng cách lân cận trong đánh giá phòng.

Yêu cầu kỹ thuật:
- Tình huống: Khách lưu trú thường đề cập đến vị trí xung quanh qua các cụm từ như `"cerca de"`, `"cerca del"`, `"cerca de la"`, `"near"`, `"near the"`. Ta cần trích xuất từ đơn đứng liền sau cụm từ này để thống kê các địa danh thường gặp.
- Thao tác: Dùng `s.str.extract(pattern, expand=False)` với mẫu chứa nhóm không bắt `(?:...)` cho cụm từ chỉ hướng và nhóm bắt `([A-Za-zÁ-Úá-úñÑ]+)` cho từ mục tiêu.
- Đầu ra: Trả về từ điển gồm hai khóa: `gan` (Series chuỗi kết quả trích xuất, giữ nguyên chỉ mục và chữ hoa thường) và `so_trich` (số nguyên biểu thị số dòng trích xuất thành công).
- Trường hợp biên: Mẫu phân biệt hoa thường theo đúng định nghĩa, các dòng không khớp hoặc giá trị khuyết thiếu trả về `NaN`.
:::

::: solution
#### Cách 1: Trích nhóm bắt đầu tiên sau cụm chỉ vị trí

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
c_sach_full = c_sach_demo.copy()

PAT_GAN = r"(?:cerca de la |cerca del |cerca de |near the |near )([A-Za-zÁ-Úá-úñÑ]+)"

# Bắt đầu lời giải

c_sach_full = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
gan_c1 = c_sach_full.str.extract(PAT_GAN, expand=False)
so_trich_c1 = int(gan_c1.notna().sum())

print(f"Số dòng trích xuất thành công: {so_trich_c1}")
print("Năm giá trị trích xuất đầu tiên:")
print(gan_c1.dropna().head(5).tolist())

# Kết thúc lời giải
```

##### Giải thích Cách 1

`str.extract(PAT_GAN, expand=False)` tìm lần khớp đầu tiên trong mỗi dòng và trả nội dung của nhóm bắt. Các cụm `cerca de la`, `cerca del`, `cerca de`, `near the`, `near` nằm trong nhóm không bắt `(?:...)`, nên không trở thành dữ liệu đầu ra.

Nhóm `([A-Za-zÁ-Úá-úñÑ]+)` lấy một hoặc nhiều ký tự trong các khoảng đã viết. Mẫu hỗ trợ các từ minh họa ở đây nhưng không bao phủ mọi chữ cái Unicode hoặc mọi cách viết tên riêng. `expand=False` trả Series khi có một nhóm bắt, giúp giữ cùng chỉ mục với cột nguồn.

Mẫu phân biệt hoa thường. Vì vậy `Near Movistar Arena` với N hoa không được nhận bởi nhánh `near`, còn `cerca de Movistar Arena` cho từ `Movistar`. Chỉ lấy một từ cũng có nghĩa tên nhiều từ bị cắt. Đếm ô không khuyết đo số lần quy tắc trích được chữ, chưa đo số địa danh được xác minh.

##### Output Cách 1

| Chỉ mục gốc | Từ trích xuất |
|---|---|
| 0 | `metro` |
| 1 | `metro` |
| 5 | `todo` |
| 8 | `estación` |
| 10 | `muchos` |
| 11 | `mall` |
| 12 | `centro` |
| 13 | `metro` |
| 15 | `Movistar` |

`so_trich = 9`. Năm giá trị đầu sau khi bỏ khuyết là `metro`, `metro`, `todo`, `estación`, `muchos`.

#### Cách 2: Gói quy tắc trích và số dòng khớp trong một hàm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
c_sach_full = c_sach_demo.copy()

PAT_GAN = r"(?:cerca de la |cerca del |cerca de |near the |near )([A-Za-zÁ-Úá-úñÑ]+)"

# Bắt đầu lời giải


def extract_near(comments: pd.Series, pattern: str = PAT_GAN) -> dict:
    """Trích xuất từ đầu tiên đứng ngay sau cụm từ chỉ vị trí lân cận.

    Tham số comments: Series văn bản cần trích xuất.
    Tham số pattern: Biểu thức chính quy chứa đúng một nhóm bắt thực thể.
    Trả về: Từ điển chứa Series gan và số lượng dòng trích thành công so_trich.
    """
    gan = comments.str.extract(pattern, expand=False)
    so_trich = int(gan.notna().sum())
    return {"gan": gan, "so_trich": so_trich}


ket_qua_trich = extract_near(c_sach_full)
print(f"Tổng số dòng trích xuất được: {ket_qua_trich['so_trich']}")
print(f"Ví dụ dòng 0 (metro): {ket_qua_trich['gan'].iloc[0]}")
print(f"Ví dụ dòng 5 (todo): {ket_qua_trich['gan'].iloc[5]}")
print(f"Ví dụ dòng 15 (Movistar): {ket_qua_trich['gan'].iloc[15]}")

# Kết thúc lời giải
```

##### Giải thích Cách 2

Hàm `extract_near` nhận mẫu qua đối số để có thể điều chỉnh quy tắc độc lập với logic đếm. `gan.notna().sum()` chỉ cộng những dòng có kết quả trích, còn các dòng không khớp tiếp tục mang giá trị khuyết trong Series `gan`.

Thứ tự các nhánh tiền tố có ý nghĩa. Đặt `cerca de la ` trước `cerca de ` giúp mẫu dài được thử trước, nên đoạn `cerca de la estación` lấy `estación` thay vì lấy nhầm `la` từ một nhánh ngắn hơn. Dấu cách cuối mỗi tiền tố cũng là một phần phải khớp.

Kết quả vẫn có các từ `todo` và `muchos`, vốn không phải tên địa điểm. Mẫu chỉ nhận cấu trúc chữ theo quy tắc, không hiểu ngữ nghĩa. Đó là lý do cần xem bảng kết quả và có bước lọc hoặc xác minh ở bài tiếp theo.

##### Output Cách 2

| Chỉ mục gốc | Từ trích xuất |
|---|---|
| 0 | `metro` |
| 1 | `metro` |
| 5 | `todo` |
| 8 | `estación` |
| 10 | `muchos` |
| 11 | `mall` |
| 12 | `centro` |
| 13 | `metro` |
| 15 | `Movistar` |

Các lệnh minh họa riêng in dòng 0 là `metro`, dòng 5 là `todo`, dòng 15 là `Movistar`.

#### So sánh hai cách

Cách 1 thuận tiện để thử trực tiếp một regex và đọc các giá trị đầu. Cách 2 giữ quy tắc cùng số đo khớp trong một hàm dùng lại. Cả hai cần kiểm tra các trường hợp không khớp, từ không phải địa danh và tên nhiều từ trước khi dùng đầu ra làm dữ liệu vị trí.

:::

---

<span id="data-lab-07-10"></span>
### Bài 10: Tổng hợp tần suất địa danh và phát hiện trường hợp khớp nhầm

::: exercise
Tổng hợp bảng tần suất các từ được trích xuất từ bài tập trước, nhận diện các trường hợp khớp nhầm cấu trúc ngữ pháp và lọc bỏ chúng thông qua danh sách từ dừng.

Yêu cầu kỹ thuật:
- Tình huống: Biểu thức chính quy nhận diện chuẩn cấu trúc `"cerca de X"` nhưng không hiểu nghĩa của từ. Trong tiếng Tây Ban Nha, `"todo"` nghĩa là "mọi thứ" và `"muchos"` nghĩa là "nhiều", hoàn toàn không phải tên địa danh.
- Thao tác: Chuyển toàn bộ từ trích xuất sang chữ thường, loại bỏ giá trị khuyết thiếu `NaN`, loại bỏ các từ nằm trong danh sách dừng `bo_qua` và lấy `n` từ xuất hiện nhiều nhất bằng `.value_counts().head(n)`.
- Đầu ra: Trả về Series có chỉ mục là từ (chữ thường) và giá trị là số lần xuất hiện (int) sắp xếp giảm dần.
- Trường hợp biên: Tham số `bo_qua` nhận một tuple các chuỗi viết thường, mặc định là rỗng `()`.
:::

::: solution
#### Cách 1: Quan sát bảng tần suất trước khi quyết định lọc

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

# Bắt đầu lời giải

gan_demo = pd.Series(
    [
        "metro",
        "Metro",
        None,
        "todo",
        "estación",
        "metro",
        "Movistar",
        "muchos",
        "movistar",
    ]
)
gan_sach_c1 = gan_demo.dropna().str.lower()
tan_suat_c1 = gan_sach_c1.value_counts().head(5)
print("Bảng tần suất ban đầu chưa lọc từ dừng:")
print(tan_suat_c1)

gan_khong_tu_dung = gan_sach_c1.loc[~gan_sach_c1.isin(["todo", "muchos"])]
tan_suat_da_loc = gan_khong_tu_dung.value_counts().head(2)
print("Hai từ có tần suất cao nhất sau khi lọc:")
print(tan_suat_da_loc)

# Kết thúc lời giải
```

##### Giải thích Cách 1

`gan_demo` là một mẫu nhỏ để khảo sát phép đếm. `.dropna()` bỏ ô không trích được từ. `.str.lower()` gộp `metro` với `Metro`, đồng thời gộp `Movistar` với `movistar`, để không chia một dạng chữ thành nhiều khóa đếm.

`.value_counts()` đếm mỗi giá trị phân biệt và xếp theo số lần giảm dần. `.head(5)` lấy năm giá trị đầu, không phải năm dòng nguồn. Các từ hòa một lần xuất hiện chưa được yêu cầu xếp theo bảng chữ cái, nên không nên dựa vào thứ tự hòa khi viết quy tắc xử lý sau đó.

Bảng chưa lọc làm lộ `todo` và `muchos`. Cần phân biệt bước chẩn đoán này với đầu ra cuối đã loại từ dừng. Có tần suất xuất hiện không chứng minh một từ là tên địa danh. Bước tiếp theo phải áp dụng danh sách đã quyết định loại.

##### Output Cách 1

| Từ | Số lần |
|---|---|
| `metro` | 3 |
| `movistar` | 2 |
| `todo` | 1 |
| `estación` | 1 |
| `muchos` | 1 |

#### Cách 2: Thêm danh sách từ dừng và giới hạn số kết quả

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

gan_demo = pd.Series(
    [
        "metro",
        "Metro",
        None,
        "todo",
        "estación",
        "metro",
        "Movistar",
        "muchos",
        "movistar",
    ]
)

# Bắt đầu lời giải


def top_places(gan: pd.Series, n: int = 8, bo_qua: tuple = ()) -> pd.Series:
    """Lập bảng tần suất các từ trích xuất, hỗ trợ loại trừ danh sách từ dừng.

    Tham số gan: Series chuỗi kết quả trích xuất.
    Tham số n: Số lượng từ phổ biến nhất cần lấy.
    Tham số bo_qua: Tuple chứa các từ dừng cần loại bỏ khỏi bảng xếp hạng.
    Trả về: Series tần suất có chỉ mục là từ viết thường, sắp xếp giảm dần.
    """
    s = gan.dropna().str.lower()
    if bo_qua:
        s = s[~s.isin(bo_qua)]
    return s.value_counts().head(n)


top_chua_loc = top_places(gan_demo, n=5)
print("Top 5 từ trước khi lọc từ dừng:")
print(top_chua_loc)

top_da_loc = top_places(gan_demo, n=2, bo_qua=("todo", "muchos"))
print("\nTop 2 địa danh thực tế sau khi lọc todo và muchos:")
print(top_da_loc)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`bo_qua=()` mặc định là tuple rỗng, nghĩa là chưa loại từ nào. Nếu người gọi truyền các từ dừng, `s.isin(bo_qua)` đánh dấu từ thuộc danh sách và `~` đảo mặt nạ để chỉ giữ phần còn lại. Việc đổi chữ thường được làm trước, nên danh sách từ dừng cũng cần ở dạng chữ thường.

Sau lọc, `.value_counts().head(n)` mới đếm và giới hạn. Với `n=2`, `bo_qua=("todo", "muchos")`, kết quả có `metro` ba lần và `movistar` hai lần. `estación` không bị loại, nhưng đứng ngoài hai vị trí đầu vì chỉ có một lần.

Việc bỏ hai từ dừng không xác nhận mọi từ còn lại là tên địa điểm thật. Chẳng hạn `metro` là một danh từ chỉ phương tiện hoặc nhà ga theo ngữ cảnh, còn `Movistar` mới chỉ là một phần tên đã trích. Kết quả cần được kiểm tra theo mục đích phân tích.

##### Output Cách 2

Lần gọi chưa truyền từ dừng trả bảng năm từ như Cách 1. Lần gọi có lọc và lấy hai từ đầu trả:

| Từ | Số lần |
|---|---|
| `metro` | 3 |
| `movistar` | 2 |

#### So sánh hai cách

Cách 1 giúp phát hiện các từ cần rà soát trước khi chốt danh sách lọc. Cách 2 thực hiện quy tắc lọc có thể lặp lại bằng đối số hàm. Chỉ bước quan sát bảng chưa lọc chưa hoàn thành yêu cầu đầu ra có từ dừng. Khi cần kết quả cuối, phải áp dụng cùng danh sách và cùng giới hạn ở cả hai cách.

:::

---

<span id="data-lab-07-11"></span>
### Bài 11: Phân rã danh sách tiện nghi JSON bằng phương thức explode

::: exercise
Thực hiện đọc và phân rã cột thuộc tính tiện nghi lưu dưới dạng chuỗi JSON thành các dòng dữ liệu riêng biệt bằng phương thức explode, chú ý xử lý các trường hợp tên tiện nghi có chứa dấu phẩy.

Yêu cầu kỹ thuật:
- Tình huống: Cột `amenities` trong bảng dữ liệu chỗ ở lưu một mảng JSON dưới dạng chuỗi văn bản như `'["Wifi", "Air conditioning"]'`. Một số mục tiện nghi chứa sẵn dấu phẩy trong tên như `"Wifi, free"`, nên tuyệt đối không được dùng phương thức cắt chuỗi bằng dấu phẩy thông thường.
- Thao tác: Dùng `json.loads` trong hàm ánh xạ để chuyển chuỗi thành danh sách Python, sau đó dùng `Series.explode()` để phân rã mỗi phần tử của danh sách thành một dòng độc lập, giữ nguyên chỉ mục mã chỗ ở.
- Đầu ra: Trả về một tuple gồm hai Series: `(ds, muc)`, trong đó `ds` là Series các danh sách Python và `muc` là Series các mục tiện nghi sau khi phân rã đã loại bỏ phần tử rỗng.
- Trường hợp biên: Dòng chứa danh sách rỗng `'[]'` hoặc giá trị khuyết thiếu cần được xử lý an toàn mà không làm dừng chương trình.
:::

::: solution
#### Cách 1: Giải mã JSON rồi tách từng phần tử danh sách

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import json

import pandas as pd

DEMO_LISTINGS = pd.DataFrame(
    {
        "amenities": [
            '["Wifi", "Air conditioning"]',
            '["Wifi, free", "Kitchen"]',
            "[]",
            '["Kitchen"]',
            '["Heating"]',
        ]
    },
    index=[101, 102, 103, 104, 105],
)

# Bắt đầu lời giải

ds_c1 = DEMO_LISTINGS["amenities"].map(json.loads)
muc_c1 = ds_c1.explode().dropna()

print(f"Tổng số chỗ ở khảo sát: {len(ds_c1)}")
print(f"Tổng số lượt tiện nghi sau khi explode: {len(muc_c1)}")
print("Bảng đếm tiện nghi phổ biến Cách 1:")
print(muc_c1.value_counts())

# Kết thúc lời giải
```

##### Giải thích Cách 1

`map(json.loads)` gọi bộ giải mã JSON cho từng chuỗi trong cột. Chuỗi `'["Wifi, free", "Kitchen"]'` trở thành một danh sách có đúng hai phần tử. Dấu phẩy bên trong tên `Wifi, free` được bộ giải mã giữ nguyên vì nằm trong một chuỗi JSON, khác với dấu phân cách hai phần tử.

`.explode()` tạo một dòng cho mỗi phần tử danh sách và lặp lại chỉ mục của chỗ ở gốc. Với danh sách rỗng, pandas tạo một ô khuyết trong kết quả trung gian. `.dropna()` loại ô ấy, nên chỉ còn sáu dòng tiện nghi từ năm chỗ ở.

Cách cơ bản giả thiết các chuỗi đều là mảng JSON hợp lệ. Nếu gặp chuỗi JSON sai hoặc ô thiếu, `json.loads` trực tiếp có thể phát sinh lỗi. Bảng mẫu không có những đầu vào đó, nên mã chạy được nhưng chưa đủ để kết luận đã kiểm soát mọi trường hợp biên.

##### Output Cách 1

| Tiện nghi | Số lần xuất hiện |
|---|---|
| Kitchen | 2 |
| Wifi | 1 |
| Air conditioning | 1 |
| Wifi, free | 1 |
| Heating | 1 |

Có 5 chỗ ở và 6 dòng tiện nghi sau `explode().dropna()`.

#### Cách 2: Tách hàm giải mã và trả cả danh sách lẫn bảng dài

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import json

import pandas as pd

DEMO_LISTINGS = pd.DataFrame(
    {
        "amenities": [
            '["Wifi", "Air conditioning"]',
            '["Wifi, free", "Kitchen"]',
            "[]",
            '["Kitchen"]',
            '["Heating"]',
        ]
    },
    index=[101, 102, 103, 104, 105],
)

# Bắt đầu lời giải


def parse_amenities_explode(
    df: pd.DataFrame, col: str = "amenities"
) -> tuple[pd.Series, pd.Series]:
    """Giải mã chuỗi JSON và phân rã các mục tiện nghi thành từng dòng độc lập.

    Tham số df: DataFrame chứa dữ liệu chỗ ở.
    Tham số col: Tên cột chứa chuỗi JSON mảng tiện nghi.
    Trả về: Tuple gồm Series danh sách Python ds và Series các mục tiện nghi muc.
    """

    def safe_loads(val):
        if pd.isna(val):
            return []
        try:
            return json.loads(val)
        except Exception:
            return []

    ds = df[col].map(safe_loads)
    muc = ds.explode().dropna()
    return ds, muc


ds_demo, muc_demo = parse_amenities_explode(DEMO_LISTINGS)
print("Kết quả phân tích tiện nghi từ parse_amenities_explode:")
print(f"Số lượng chỗ ở có danh sách: {len(ds_demo)}")
print(
    f"Kiểm tra có tên tiện nghi chứa dấu phẩy: {muc_demo.str.contains(',', regex=False).any()}"
)
display(muc_demo.to_frame(name="ten_tien_nghi"))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`safe_loads` được định nghĩa bên trong hàm để xử lý mỗi ô. Với mã đang minh họa, ô khuyết hoặc chuỗi gây lỗi được quy về danh sách rỗng. `ds` giữ một danh sách cho mỗi chỗ ở. Biến `muc` là Series dài sau khi tách và bỏ ô khuyết. Trả cả hai giúp chọn đúng đơn vị phân tích ở các bài sau.

Cách xử lý lỗi này cho quy trình tiếp tục chạy nhưng làm mất phân biệt giữa không liệt kê tiện nghi, thiếu dữ liệu và JSON lỗi. Khi dữ liệu thật cần kiểm toán, nên báo hoặc lưu cờ lỗi riêng thay vì âm thầm coi mọi trường hợp là danh sách rỗng. Đồng thời phải kiểm tra JSON giải mã thành danh sách, vì JSON hợp lệ cũng có thể là một số hoặc từ điển.

`muc_demo.str.contains(",", regex=False).any()` trả `True`, xác nhận vẫn có tên tiện nghi chứa dấu phẩy. `to_frame(name="ten_tien_nghi")` đổi Series thành bảng một cột để hiển thị đúng các hàng có cùng chỉ mục chỗ ở.

##### Output Cách 2

| Chỉ mục chỗ ở | Tên tiện nghi |
|---|---|
| 101 | Wifi |
| 101 | Air conditioning |
| 102 | Wifi, free |
| 102 | Kitchen |
| 104 | Kitchen |
| 105 | Heating |

Kiểm tra tên có chứa dấu phẩy trả `True`. Chỗ ở 103 có danh sách rỗng nên không xuất hiện trong bảng dài sau khi bỏ ô khuyết.

#### So sánh hai cách

Cách 1 mở rõ giải mã và tách hàng, phù hợp với mẫu JSON đã bảo đảm hợp lệ. Cách 2 trả cả hai dạng dữ liệu và có nhánh xử lý lỗi, nhưng quy tắc quy lỗi thành danh sách rỗng cần được chấp nhận rõ. Trong cả hai cách, không được dùng `split(",")` để thay bộ giải mã JSON.

:::

---

<span id="data-lab-07-12"></span>
### Bài 12: Tính tỷ lệ chỗ ở có tiện nghi và bảo toàn mẫu số phân tích

::: exercise
Thực hiện tính toán tỷ lệ chỗ ở cung cấp tiện nghi Wifi trên toàn bộ tập dữ liệu, bảo đảm giữ đúng mẫu số tổng thể bao gồm cả những chỗ ở có danh sách tiện nghi rỗng.

Yêu cầu kỹ thuật:
- Tình huống: Chỗ ở có danh sách tiện nghi rỗng `'[]'` không liệt kê tiện nghi nào trong dữ liệu. Khi tính tỷ lệ chỗ ở có Wifi, mẫu số bắt buộc phải là toàn bộ số lượng chỗ ở trong bảng, không được lấy mẫu số là số dòng sau khi explode hay loại bỏ các chỗ ở có danh sách rỗng.
- Thao tác: Kiểm tra từng chỗ ở có chứa phần tử `"Wifi"` trong danh sách hay không để tạo cờ boolean `co_wifi`, sau đó tính tỷ lệ bằng tổng số chỗ ở có Wifi chia cho tổng số dòng của bảng dữ liệu.
- Đầu ra: Trả về từ điển gồm các khóa: `co_tien_nghi` (Series boolean per listing), `so_cho_o_co` (int), `tong_cho_o` (int) và `ty_le` (float).
- Trường hợp biên: Chỗ ở có mục `"Wifi, free"` không được tính gộp vào mục `"Wifi"` nếu quy tắc yêu cầu khớp chính xác tên tiện nghi.
:::

::: solution
#### Cách 1: Tạo cờ một lần cho mỗi chỗ ở rồi tính tỷ lệ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import json

import pandas as pd

DEMO_LISTINGS = pd.DataFrame(
    {
        "amenities": [
            '["Wifi", "Air conditioning"]',
            '["Wifi, free", "Kitchen"]',
            "[]",
            '["Kitchen"]',
            '["Heating"]',
        ]
    },
    index=[101, 102, 103, 104, 105],
)


def parse_amenities_explode(
    df: pd.DataFrame, col: str = "amenities"
) -> tuple[pd.Series, pd.Series]:
    """Giải mã chuỗi JSON và phân rã các mục tiện nghi thành từng dòng độc lập.

    Tham số df: DataFrame chứa dữ liệu chỗ ở.
    Tham số col: Tên cột chứa chuỗi JSON mảng tiện nghi.
    Trả về: Tuple gồm Series danh sách Python ds và Series các mục tiện nghi muc.
    """

    def safe_loads(val):
        if pd.isna(val):
            return []
        try:
            return json.loads(val)
        except Exception:
            return []

    ds = df[col].map(safe_loads)
    muc = ds.explode().dropna()
    return ds, muc


ds_demo, muc_demo = parse_amenities_explode(DEMO_LISTINGS)

# Bắt đầu lời giải

co_wifi_c1 = ds_demo.map(lambda lst: "Wifi" in lst)
so_co_wifi_c1 = int(co_wifi_c1.sum())
tong_so_c1 = int(len(DEMO_LISTINGS))
ty_le_c1 = float(so_co_wifi_c1 / tong_so_c1)

print(f"Số chỗ ở có Wifi: {so_co_wifi_c1}/{tong_so_c1}")
print(f"Tỷ lệ chỗ ở có Wifi: {ty_le_c1:.1%}")

# Kết thúc lời giải
```

##### Giải thích Cách 1

`ds_demo` là Series danh sách còn giữ một dòng cho mỗi chỗ ở. `lambda lst: "Wifi" in lst` hỏi danh sách có phần tử bằng đúng chuỗi `Wifi` hay không. Hai tên `Wifi` và `Wifi, free` khác nhau, nên chỗ ở 102 không được tính theo quy tắc này.

`.sum()` trên cờ boolean đếm số chỗ ở có tiện nghi. `len(DEMO_LISTINGS)` lấy mẫu số từ bảng chỗ ở gốc, gồm cả dòng có danh sách rỗng. Trong năm dòng, chỉ chỗ ở 101 có đúng mục `Wifi`, nên tỷ lệ là `1 / 5`, bằng `0.2`.

Không lấy `len(muc_demo)` làm mẫu số vì mỗi dòng ở bảng dài là một lượt liệt kê tiện nghi, khác đơn vị chỗ ở. Chỗ ở có nhiều tiện nghi sẽ đóng góp nhiều dòng trong bảng dài, còn chỗ ở có danh sách rỗng biến mất sau bước bỏ ô khuyết.

##### Output Cách 1

| Chỉ mục chỗ ở | Có đúng mục `Wifi` |
|---|---|
| 101 | `True` |
| 102 | `False` |
| 103 | `False` |
| 104 | `False` |
| 105 | `False` |

Ví dụ in `Số chỗ ở có Wifi: 1/5` và `Tỷ lệ chỗ ở có Wifi: 20.0%`.

#### Cách 2: Đóng gói quy tắc tiện nghi mục tiêu và mẫu số

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import json

import pandas as pd

DEMO_LISTINGS = pd.DataFrame(
    {
        "amenities": [
            '["Wifi", "Air conditioning"]',
            '["Wifi, free", "Kitchen"]',
            "[]",
            '["Kitchen"]',
            '["Heating"]',
        ]
    },
    index=[101, 102, 103, 104, 105],
)


def parse_amenities_explode(
    df: pd.DataFrame, col: str = "amenities"
) -> tuple[pd.Series, pd.Series]:
    """Giải mã chuỗi JSON và phân rã các mục tiện nghi thành từng dòng độc lập.

    Tham số df: DataFrame chứa dữ liệu chỗ ở.
    Tham số col: Tên cột chứa chuỗi JSON mảng tiện nghi.
    Trả về: Tuple gồm Series danh sách Python ds và Series các mục tiện nghi muc.
    """

    def safe_loads(val):
        if pd.isna(val):
            return []
        try:
            return json.loads(val)
        except Exception:
            return []

    ds = df[col].map(safe_loads)
    muc = ds.explode().dropna()
    return ds, muc


ds_demo, muc_demo = parse_amenities_explode(DEMO_LISTINGS)

# Bắt đầu lời giải


def calculate_amenity_rate(
    df: pd.DataFrame, target_amenity: str = "Wifi", col: str = "amenities"
) -> dict:
    """Tính tỷ lệ chỗ ở có tiện nghi chỉ định trên toàn bộ mẫu số khảo sát.

    Tham số df: DataFrame dữ liệu chỗ ở.
    Tham số target_amenity: Tên tiện nghi cần kiểm tra sự hiện diện.
    Tham số col: Tên cột chứa dữ liệu JSON tiện nghi.
    Trả về: Từ điển chứa cờ boolean và các số liệu tỷ lệ tổng thể.
    """
    ds, muc = parse_amenities_explode(df, col=col)
    co_tien_nghi = ds.map(lambda lst: target_amenity in lst)
    so_cho_o_co = int(co_tien_nghi.sum())
    tong_cho_o = int(len(df))
    ty_le = float(so_cho_o_co / tong_cho_o) if tong_cho_o > 0 else 0.0
    return {
        "co_tien_nghi": co_tien_nghi,
        "so_cho_o_co": so_cho_o_co,
        "tong_cho_o": tong_cho_o,
        "ty_le": ty_le,
    }


ket_qua_ty_le_wifi = calculate_amenity_rate(DEMO_LISTINGS, "Wifi")
print(f"Số chỗ ở có Wifi: {ket_qua_ty_le_wifi['so_cho_o_co']}")
print(f"Tổng số chỗ ở trong mẫu: {ket_qua_ty_le_wifi['tong_cho_o']}")
print(f"Tỷ lệ chính xác: {ket_qua_ty_le_wifi['ty_le']:.1%}")
display(ket_qua_ty_le_wifi["co_tien_nghi"].to_frame(name="co_wifi"))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`target_amenity` cho phép thay tên cần kiểm tra, còn `col` chọn cột JSON. Hàm dùng `parse_amenities_explode` để có Series danh sách `ds`, sau đó kiểm tra phần tử trên từng danh sách. Biến `muc` được trả từ hàm hỗ trợ không được dùng làm mẫu số.

`so_cho_o_co`, `tong_cho_o` và `ty_le` tách rõ số đạt, tổng số và phép chia. `co_tien_nghi` giữ cờ cùng chỉ mục để người gọi kiểm tra từng chỗ ở. Với bảng rỗng, mã quy ước tỷ lệ bằng `0.0` để tránh chia cho 0. Trong báo cáo, cần chỉ rõ không có mẫu quan sát thay vì diễn giải giá trị dự phòng ấy như một tỷ lệ ước lượng.

Bài này dùng năm chuỗi JSON đã biết, bao gồm một danh sách rỗng. Nếu có dữ liệu khuyết hoặc JSON lỗi bị hàm hỗ trợ quy thành rỗng, tỷ lệ có thể bị diễn giải sai là đã biết chắc không có tiện nghi. Bài tiếp theo tách riêng trạng thái chưa có thông tin để chọn mẫu số phù hợp.

##### Output Cách 2

| Chỉ mục chỗ ở | Có đúng mục `Wifi` |
|---|---|
| 101 | `True` |
| 102 | `False` |
| 103 | `False` |
| 104 | `False` |
| 105 | `False` |

Từ điển trả `so_cho_o_co = 1`, `tong_cho_o = 5`, `ty_le = 0.2`. Định dạng phần trăm `.1%` hiển thị `20.0%`.

#### So sánh hai cách

Hai cách cùng đếm sự hiện diện nhị phân trên mỗi chỗ ở. Cách 2 giúp đổi tiện nghi và lấy đầy đủ thông tin kiểm tra trong một lần gọi. Lợi ích chính là làm rõ giao diện và mẫu số, không phải biến số lượt liệt kê tiện nghi thành số chỗ ở.

:::

---

<span id="data-lab-07-13"></span>
### Bài 13: Phân biệt danh sách rỗng và dữ liệu khuyết thiếu khi tính tỷ lệ

::: exercise
Phân biệt bản chất thống kê giữa trạng thái danh sách tiện nghi rỗng `[]` (không có tiện nghi nào được liệt kê) và giá trị khuyết thiếu `None` (chưa thu thập được dữ liệu), từ đó tính toán tỷ lệ trên nhóm đã có thông tin.

Yêu cầu kỹ thuật:
- Tình huống: Xét một bảng nhỏ gồm 5 chỗ ở: P1 có danh sách `["Wifi", "Wifi", "Kitchen"]`, P2 có `["Kitchen"]`, P3 có danh sách rỗng `[]`, P4 nhận giá trị `None` và P5 có `["Wifi"]`.
- Thao tác: Xác định số chỗ ở đã có thông tin `so_da_biet` (các dòng có dữ liệu khác `None`/`NaN`), sau đó tính tỷ lệ chỗ ở có Wifi `ty_le_da_biet` trên nhóm này. Lưu ý rằng P1 liệt kê lặp hai lần `"Wifi"` nhưng chỉ tính là một chỗ ở có tiện nghi.
- Đầu ra: Trả về từ điển gồm: `so_da_biet` (int), `ty_le_da_biet` (float) và `so_khuyet` (int).
- Trường hợp biên: Danh sách rỗng `[]` được tính vào `so_da_biet`, trong khi `None` bị loại khỏi mẫu số của nhóm đã biết.
:::

::: solution
#### Cách 1: Lọc các danh sách không khuyết rồi kiểm tra Wifi

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_DS_NHO = pd.Series(
    [
        ["Wifi", "Wifi", "Kitchen"],
        ["Kitchen"],
        [],
        None,
        ["Wifi"],
    ],
    index=["P1", "P2", "P3", "P4", "P5"],
)

# Bắt đầu lời giải

da_biet_c1 = DEMO_DS_NHO.notna()
so_da_biet_c1 = int(da_biet_c1.sum())
ds_hop_le_c1 = DEMO_DS_NHO[da_biet_c1]
co_wifi_tap_con = ds_hop_le_c1.map(
    lambda x: "Wifi" in x if isinstance(x, list) else False
)
so_co_wifi_c1 = int(co_wifi_tap_con.sum())
ty_le_tap_con_c1 = float(so_co_wifi_c1 / so_da_biet_c1)

print(f"Số chỗ ở đã biết thông tin: {so_da_biet_c1}")
print(f"Số chỗ ở có Wifi trong nhóm đã biết: {so_co_wifi_c1}")
print(f"Tỷ lệ trên nhóm đã biết: {ty_le_tap_con_c1:.1%}")

# Kết thúc lời giải
```

##### Giải thích Cách 1

`.notna()` trả `True` cho danh sách rỗng `[]` vì đó là một giá trị đã được cung cấp, và trả `False` cho ô `None`. Vì vậy bốn dòng P1, P2, P3, P5 thuộc nhóm đã biết. P4 được giữ ở trạng thái chưa biết, không tự kết luận có hoặc không có Wifi.

Phép kiểm tra `"Wifi" in x` chỉ trả một cờ, kể cả danh sách P1 chứa Wifi hai lần. Tổng cờ đúng là hai chỗ ở P1 và P5. Mẫu số đã biết là bốn, nên tỷ lệ bằng `0.5`, không phải tỷ lệ trong toàn bộ năm chỗ ở.

`isinstance(x, list)` trong hàm ẩn danh kiểm tra kiểu trước khi thử thành viên. Theo miền dữ liệu của bài, ô không khuyết là danh sách. Nếu dữ liệu thật có giá trị khác kiểu nhưng không khuyết, cần báo lỗi hoặc tách cờ riêng, thay vì tự coi đó là bằng chứng không có tiện nghi.

##### Output Cách 1

| Chỉ mục | Đã biết danh sách | Có `Wifi` trong nhóm đã biết |
|---|---|---|
| P1 | `True` | `True` |
| P2 | `True` | `False` |
| P3 | `True` | `False` |
| P4 | `False` | Chưa biết |
| P5 | `True` | `True` |

Kết quả in có `so_da_biet = 4`, số có Wifi trong nhóm là `2`, tỷ lệ `50.0%`.

#### Cách 2: Trả đồng thời số đã biết, số khuyết và tỷ lệ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

DEMO_DS_NHO = pd.Series(
    [
        ["Wifi", "Wifi", "Kitchen"],
        ["Kitchen"],
        [],
        None,
        ["Wifi"],
    ],
    index=["P1", "P2", "P3", "P4", "P5"],
)

# Bắt đầu lời giải


def analyze_amenity_completeness(ds: pd.Series, target: str = "Wifi") -> dict:
    """Phân biệt danh sách rỗng với dữ liệu khuyết thiếu và tính tỷ lệ tiện nghi.

    Tham số ds: Series chứa danh sách các tiện nghi của từng chỗ ở.
    Tham số target: Tên tiện nghi cần kiểm tra.
    Trả về: Từ điển chứa số lượng đã biết, số khuyết và tỷ lệ tiện nghi tương ứng.
    """
    so_da_biet = int(ds.notna().sum())
    so_khuyet = int(ds.isna().sum())
    ds_da_biet = ds.dropna()
    co_target = ds_da_biet.map(
        lambda lst: target in lst if isinstance(lst, list) else False
    )
    ty_le_da_biet = float(co_target.sum() / so_da_biet) if so_da_biet > 0 else 0.0
    return {
        "so_da_biet": so_da_biet,
        "so_khuyet": so_khuyet,
        "ty_le_da_biet": ty_le_da_biet,
    }


ket_qua_day_du = analyze_amenity_completeness(DEMO_DS_NHO, target="Wifi")
print("Kết quả phân tích từ analyze_amenity_completeness:")
print(f"Số chỗ ở đã biết thông tin: {ket_qua_day_du['so_da_biet']}")
print(f"Số chỗ ở khuyết thiếu dữ liệu: {ket_qua_day_du['so_khuyet']}")
print(f"Tỷ lệ có Wifi trên nhóm đã biết: {ket_qua_day_du['ty_le_da_biet']:.1%}")

# Kết thúc lời giải
```

##### Giải thích Cách 2

Hàm tính `.notna().sum()` và `.isna().sum()` trên cùng Series để tách bốn dòng có dữ liệu khỏi một dòng khuyết. `.dropna()` tạo tập dùng để hỏi thành viên, nhờ vậy phép `in` không bị áp vào `None`.

`co_target.sum() / so_da_biet` dùng đúng tập đã biết làm mẫu số. Phần tử trùng trong một danh sách không tăng tử số vì mỗi dòng chỉ cho một cờ boolean. Nếu không có dòng đã biết, nhánh dự phòng trả `0.0`. Đó là lựa chọn giao diện của mã, không phải kết luận xác suất khi chưa có thông tin.

Từ điển không trả tỷ lệ có Wifi của toàn bộ quần thể năm dòng vì chưa biết P4. Thay P4 bằng danh sách rỗng sẽ là bổ sung một giả thiết về dữ liệu, chứ không phải chỉ làm sạch kiểu.

##### Output Cách 2

| Khóa trả về | Output |
|---|---|
| `so_da_biet` | 4 |
| `so_khuyet` | 1 |
| `ty_le_da_biet` | 0.5 |

#### So sánh hai cách

Cách 1 cho thấy rõ mặt nạ và tập con được chọn. Cách 2 gói các chỉ số bao phủ cùng tỷ lệ để khó bỏ sót lượng dữ liệu khuyết khi báo cáo. Cả hai giữ phân biệt danh sách rỗng với chưa có danh sách, và chỉ đếm một lần cho mỗi chỗ ở có tiện nghi.

:::

---

<span id="data-lab-07-14"></span>
### Bài 14: Kiểm chứng tín hiệu từ khoá đa ngữ trên các nhóm đánh giá

::: exercise
Xây dựng hai tín hiệu từ khoá đa ngữ đại diện cho mạng Internet (`wifi|internet`) và bãi đỗ xe (`parking|estacionamiento`), tính toán tỷ lệ xuất hiện của từng tín hiệu trên hai phân nhóm ngôn ngữ và kiểm chứng phản biện giả thuyết về sự hài lòng của khách hàng.

Yêu cầu kỹ thuật:
- Tình huống: Người ta thường đặt giả thuyết rằng "đếm số đánh giá chứa từ khoá wifi là đếm số khách hàng hài lòng về mạng". Cần chứng minh tính phiến diện của nhận định này bằng cách chỉ ra các đánh giá phàn nàn dịch vụ mạng yếu cũng chứa từ khoá đó.
- Thao tác: Áp dụng phương thức `.str.contains()` không phân biệt hoa thường với hai mẫu regex trên hai tập con ngôn ngữ, tính tỷ lệ phần trăm theo từng nhóm.
- Đầu ra: Trả về DataFrame đối chiếu gồm 3 cột: `tin_hieu`, `ty_le_nhom_es` và `ty_le_nhom_khac`.
- Trường hợp biên: Xử lý an toàn khi một trong hai nhóm ngôn ngữ không có quan sát nào.
:::

::: solution
#### Cách 1: Tạo các cờ từ khóa rồi tính theo từng nhóm

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
c_sach_full = c_sach_demo.copy()

PAT_ES = r"ción|ñ|muy|excelente|departamento"


def language_flag(comments: pd.Series, pattern: str = PAT_ES) -> dict:
    """Tạo cờ nhận diện ngôn ngữ theo quy tắc từ khoá và tính tỷ lệ bao phủ.

    Tham số comments: Series chuỗi cần phân loại.
    Tham số pattern: Biểu thức chính quy chứa các từ khoá đặc trưng.
    Trả về: Từ điển chứa cờ la_es kiểu bool và tỷ lệ ty_le_es.
    """
    la_es = comments.str.contains(pattern, case=False, na=False)
    ty_le_es = float(la_es.sum() / len(comments)) if len(comments) > 0 else 0.0
    return {"la_es": la_es, "ty_le_es": ty_le_es}


ket_qua_es = language_flag(c_sach_demo)
flag_es = ket_qua_es["la_es"]
flag_es_demo = flag_es.copy()

# Bắt đầu lời giải

pat_wifi = r"wifi|internet"
pat_park = r"parking|estacionamiento"

flag_es_demo = ket_qua_es["la_es"]
c_demo = c_sach_demo

co_w = c_demo.str.contains(pat_wifi, case=False, na=False)
co_p = c_demo.str.contains(pat_park, case=False, na=False)

c_es = c_demo[flag_es_demo]
c_khac = c_demo[~flag_es_demo]

ty_le_w_es = co_w[flag_es_demo].sum() / len(c_es) if len(c_es) > 0 else 0.0
ty_le_w_khac = co_w[~flag_es_demo].sum() / len(c_khac) if len(c_khac) > 0 else 0.0

print(f"Tỷ lệ nhắc Wifi ở nhóm es: {ty_le_w_es:.1%}")
print(f"Tỷ lệ nhắc Wifi ở nhóm khác: {ty_le_w_khac:.1%}")

ty_le_p_es = co_p[flag_es_demo].mean() if len(c_es) > 0 else 0.0
ty_le_p_khac = co_p[~flag_es_demo].mean() if len(c_khac) > 0 else 0.0
bang_tin_hieu = pd.DataFrame(
    {
        "tin_hieu": ["wifi_internet", "parking_estacionamiento"],
        "ty_le_nhom_es": [round(float(ty_le_w_es), 3), round(float(ty_le_p_es), 3)],
        "ty_le_nhom_khac": [
            round(float(ty_le_w_khac), 3),
            round(float(ty_le_p_khac), 3),
        ],
    }
)
display(bang_tin_hieu)

# Kết thúc lời giải
```

##### Giải thích Cách 1

Dấu `|` trong `wifi|internet` và `parking|estacionamiento` nối các lựa chọn tìm kiếm. `case=False` cho phép nhận `WiFi`, còn `na=False` xác định cờ không khớp cho ô thiếu. Mỗi dòng chỉ đóng góp một cờ cho mỗi tín hiệu, kể cả khi nhắc từ khóa nhiều lần.

`flag_es_demo` chọn bảy dòng khớp quy tắc ngôn ngữ của Bài 7, `~flag_es_demo` chọn tám dòng còn lại. Cờ từ khóa được lọc bằng cùng mặt nạ, rồi tổng cờ chia cho số dòng của từng nhóm. Các điều kiện độ dài nhóm giúp tránh chia cho 0. Mẫu đang dùng đã bỏ ô khuyết trước khi tạo các nhóm.

Chỉ một dòng không khớp quy tắc ngôn ngữ có từ khóa Wifi, cho tỷ lệ `1 / 8` bằng `12.5%`. Không có dòng nào nhắc các từ khóa bãi đỗ xe. Đây là các cờ khớp quy tắc trên fixture, không phải hai nhóm ngôn ngữ được xác nhận hoặc bằng chứng về sự hài lòng.

##### Output Cách 1

| `tin_hieu` | `ty_le_nhom_es` | `ty_le_nhom_khac` |
|---|---|---|
| `wifi_internet` | 0.0 | 0.125 |
| `parking_estacionamiento` | 0.0 | 0.0 |

Các lệnh in Wifi trong đoạn minh họa trả `0.0%` cho nhóm cờ đúng và `12.5%` cho nhóm cờ sai. Cờ `co_p` của bãi đỗ xe đều `False` trong mẫu này.

#### Cách 2: Đưa cả hai tín hiệu vào một bảng kết quả

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

DEMO_COMMENTS = pd.Series(
    [
        "Excelente ubicación, muy cerca del metro.",
        "Great place near the metro, very clean.",
        "Todo perfecto.<br/>Volvería sin duda.",
        ".",
        None,
        "El departamento está cerca de todo, muy cómodo.",
        "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
        "Ok",
        "Muy buena estadía cerca de la estación Baquedano.",
        "Lovely apartment, close to everything.",
        "Departamento limpio y cerca de muchos restaurantes.",
        "The departamento was great, near the mall.",
        "Atención excelente, cerca del centro.",
        "WiFi rápido, near the metro station.",
        "",
        "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
    ],
    name="comments",
)

c_sach_demo = DEMO_COMMENTS.str.replace("<br/>", " ", regex=False)
c_sach_full = c_sach_demo.copy()

PAT_ES = r"ción|ñ|muy|excelente|departamento"


def language_flag(comments: pd.Series, pattern: str = PAT_ES) -> dict:
    """Tạo cờ nhận diện ngôn ngữ theo quy tắc từ khoá và tính tỷ lệ bao phủ.

    Tham số comments: Series chuỗi cần phân loại.
    Tham số pattern: Biểu thức chính quy chứa các từ khoá đặc trưng.
    Trả về: Từ điển chứa cờ la_es kiểu bool và tỷ lệ ty_le_es.
    """
    la_es = comments.str.contains(pattern, case=False, na=False)
    ty_le_es = float(la_es.sum() / len(comments)) if len(comments) > 0 else 0.0
    return {"la_es": la_es, "ty_le_es": ty_le_es}


ket_qua_es = language_flag(c_sach_demo)
flag_es = ket_qua_es["la_es"]
flag_es_demo = flag_es.copy()

# Bắt đầu lời giải


def multilingual_keyword_signals(
    comments: pd.Series, flag_es: pd.Series
) -> pd.DataFrame:
    """Phân tích tỷ lệ xuất hiện các tín hiệu từ khoá đa ngữ trên hai phân nhóm.

    Tham số comments: Series văn bản đã làm sạch.
    Tham số flag_es: Series kiểu bool phân loại nhóm ngôn ngữ tiếng Tây Ban Nha.
    Trả về: DataFrame so sánh tỷ lệ nhắc đến từng tín hiệu giữa hai nhóm.
    """
    pat_wifi = r"wifi|internet"
    pat_parking = r"parking|estacionamiento"

    co_wifi = comments.str.contains(pat_wifi, case=False, na=False)
    co_parking = comments.str.contains(pat_parking, case=False, na=False)

    es_comments = comments[flag_es]
    khac_comments = comments[~flag_es]

    ty_le_wifi_es = (
        float(co_wifi[flag_es].sum() / len(es_comments))
        if len(es_comments) > 0
        else 0.0
    )
    ty_le_wifi_khac = (
        float(co_wifi[~flag_es].sum() / len(khac_comments))
        if len(khac_comments) > 0
        else 0.0
    )

    ty_le_park_es = (
        float(co_parking[flag_es].sum() / len(es_comments))
        if len(es_comments) > 0
        else 0.0
    )
    ty_le_park_khac = (
        float(co_parking[~flag_es].sum() / len(khac_comments))
        if len(khac_comments) > 0
        else 0.0
    )

    return pd.DataFrame(
        {
            "tin_hieu": ["wifi_internet", "parking_estacionamiento"],
            "ty_le_nhom_es": [round(ty_le_wifi_es, 3), round(ty_le_park_es, 3)],
            "ty_le_nhom_khac": [round(ty_le_wifi_khac, 3), round(ty_le_park_khac, 3)],
        }
    )


df_tin_hieu = multilingual_keyword_signals(c_sach_demo, flag_es_demo)
display(df_tin_hieu)

# Kết thúc lời giải
```

##### Giải thích Cách 2

`multilingual_keyword_signals` tính hai cờ riêng và bốn tỷ lệ theo cặp tín hiệu, nhóm cờ. Các cột tỷ lệ giữ dạng số từ 0 đến 1. `.round(..., 3)` trong lúc dựng bảng chỉ giới hạn số chữ số báo cáo, nên `0.125` vẫn tương ứng `12.5%`.

Series `flag_es` phải có chỉ mục phù hợp với `comments` để mặt nạ chọn đúng dòng. Hàm dựa vào các nhóm đã có, không nhận diện lại ngôn ngữ. Nhánh nhóm rỗng trả tỷ lệ `0.0` theo quy ước mã, nên khi dùng kết quả ngoài bài mẫu cần báo thêm số dòng mỗi nhóm.

Các câu `WiFi rất chậm` và `el wifi no funcionaba` vẫn chứa từ khóa dù đang phàn nàn. Vì vậy chỉ số đo việc nhắc đến từ hoặc đoạn chữ, không đo hướng cảm xúc. Kết quả bằng 0 cũng chỉ nói không tìm thấy mẫu chữ đã quy định, chưa chứng minh tiện nghi không tồn tại hoặc người viết không quan tâm.

##### Output Cách 2

| `tin_hieu` | `ty_le_nhom_es` | `ty_le_nhom_khac` |
|---|---|---|
| `wifi_internet` | 0.0 | 0.125 |
| `parking_estacionamiento` | 0.0 | 0.0 |

#### So sánh hai cách

Cách 1 mở rõ mặt nạ của từng tín hiệu và mẫu số từng nhóm. Cách 2 trả đồng thời hai tín hiệu đúng cấu trúc bảng theo đề. Trước khi diễn giải chênh lệch giữa nhóm, cần xem số dòng, kiểm tra lỗi phân nhóm và đọc ngữ cảnh, thay vì suy ra quốc tịch, mức quan tâm hoặc hài lòng từ cờ từ khóa.

:::

---

<span id="data-lab-07-15"></span>
### Bài 15: Trích xuất số đo diện tích từ chuỗi văn bản tự do với nhiều quy chuẩn viết

::: exercise
Xây dựng biểu thức chính quy để trích xuất số đo diện tích phòng (đơn vị m²) từ trường văn bản tự do, hỗ trợ các cách viết thông dụng như `45 m2`, `30m²`, `45.5 m2`, `45,5 m²` và loại trừ các chuỗi mã không hợp lệ như `30m2x`.

Yêu cầu kỹ thuật:
- Tình huống: Người cho thuê mô tả diện tích phòng bằng nhiều quy chuẩn khác nhau: Dùng ký tự số 2 (`m2`) hoặc ký tự số mũ (`m²`), có hoặc không có dấu cách, dùng dấu chấm hoặc dấu phẩy phân cách phần thập phân. Tuy nhiên, các chuỗi mã hàng như `"30m2x"` không được coi là diện tích.
- Thao tác: Dùng biểu thức chính quy `r"(?i)\b(\d+(?:[.,]\d+)?)\s*(?:m2|m²)\b"`, chuẩn hoá dấu phẩy thập phân thành dấu chấm, rồi ép kiểu sang số thực `float`.
- Đầu ra: Trả về Series số thực biểu diễn diện tích phòng, gán `NaN` cho các dòng không chứa thông tin diện tích hợp lệ.
- Trường hợp biên: Dùng biên từ `\b` để ngăn ngừa việc khớp một phần trong các từ dài hơn, chuẩn hoá dấu phẩy trước khi gọi `pd.to_numeric()`.
:::

::: solution
#### Cách 1: Trích phần số rồi chuẩn hóa dấu thập phân

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

# Bắt đầu lời giải

mau_phong = pd.Series(
    [
        "Căn hộ 45 m2 thoáng mát",
        "Phòng 30m² trung tâm",
        "Studio 45.5 m2 sạch sẽ",
        "Chỗ ở 45,5 m² đẹp",
        "Mã phòng 30m2x không nhận",
        "Không ghi diện tích",
    ]
)

pat_dien_tich = r"(?i)\b(\d+(?:[.,]\d+)?)\s*(?:m2|m²)\b"
so_trich_raw = mau_phong.str.extract(pat_dien_tich, expand=False)
dien_tich_c1 = pd.to_numeric(
    so_trich_raw.str.replace(",", ".", regex=False), errors="coerce"
)

df_dien_tich_c1 = pd.DataFrame({"mo_ta": mau_phong, "dien_tich_m2": dien_tich_c1})
display(df_dien_tich_c1)

# Kết thúc lời giải
```

##### Giải thích Cách 1

Cờ `(?i)` đặt quy tắc không phân biệt hoa thường. Nhóm bắt `(\d+(?:[.,]\d+)?)` lấy một dãy chữ số và phần thập phân tùy chọn viết bằng dấu chấm hoặc dấu phẩy. Chỉ phần số được trả về, vì phần đơn vị `(?:m2|m²)` là nhóm không bắt.

`\s*` nhận không hoặc nhiều ký tự khoảng trắng, nên `45 m2` và `30m²` đều khớp. Biên từ `\b` sau đơn vị chặn mẫu `30m2x`, vì ký tự x vẫn tiếp tục cùng một từ. Các biên này giúp xử lý các ca trong đề, không thay thế việc kiểm tra mọi cú pháp số có thể gặp.

`str.extract(..., expand=False)` trả phần số của lần khớp đầu tiên trong mỗi dòng. `.str.replace(",", ".", regex=False)` đưa dấu thập phân về dấu chấm. `pd.to_numeric(..., errors="coerce")` chuyển phần số thành dữ liệu tính toán được và giữ dòng không khớp ở trạng thái khuyết.

##### Output Cách 1

| Vị trí | Mô tả | `dien_tich_m2` |
|---|---|---|
| 0 | Căn hộ 45 m2 thoáng mát | 45.0 |
| 1 | Phòng 30m² trung tâm | 30.0 |
| 2 | Studio 45.5 m2 sạch sẽ | 45.5 |
| 3 | Chỗ ở 45,5 m² đẹp | 45.5 |
| 4 | Mã phòng 30m2x không nhận | `NaN` |
| 5 | Không ghi diện tích | `NaN` |

#### Cách 2: Gói trích diện tích thành hàm trả Series số

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from IPython.display import display

import pandas as pd

mau_phong = pd.Series(
    [
        "Căn hộ 45 m2 thoáng mát",
        "Phòng 30m² trung tâm",
        "Studio 45.5 m2 sạch sẽ",
        "Chỗ ở 45,5 m² đẹp",
        "Mã phòng 30m2x không nhận",
        "Không ghi diện tích",
    ]
)

# Bắt đầu lời giải


def extract_area(s: pd.Series) -> pd.Series:
    """Trích xuất giá trị diện tích m2 từ chuỗi mô tả tự do và đổi sang số thực.

    Tham số s: Series chuỗi mô tả phòng.
    Trả về: Series số thực kiểu float biểu diễn diện tích mét vuông.
    """
    pat = r"(?i)\b(\d+(?:[.,]\d+)?)\s*(?:m2|m²)\b"
    raw = s.str.extract(pat, expand=False)
    clean_num = raw.str.replace(",", ".", regex=False)
    return pd.to_numeric(clean_num, errors="coerce")


ket_qua_dien_tich = extract_area(mau_phong)
display(pd.DataFrame({"mo_ta": mau_phong, "dien_tich_m2": ket_qua_dien_tich}))

# Kết thúc lời giải
```

##### Giải thích Cách 2

`extract_area` đặt mẫu, kết quả trích `raw` và chuỗi số đã chuẩn hóa `clean_num` trong cùng một hàm. Kết quả giữ chỉ mục của cột mô tả, nên có thể ghép trở lại đúng dòng chỗ ở trong DataFrame.

Chuyển dấu phẩy ở đây chỉ có nghĩa dấu phẩy thập phân theo miền của bài. Nếu dữ liệu còn dùng dấu phẩy để nhóm hàng nghìn, quy tắc cần được làm rõ trước khi thay thế. Tương tự, nếu một câu có nhiều diện tích, `extract` chỉ lấy lần khớp đầu, chưa biết đó là diện tích phòng, ban công hay đất.

Biểu thức chưa quy định số âm, khoảng giá trị, ký hiệu khoa học hoặc mọi ràng buộc số viết sai. Nó có thể khớp một phần của những dạng ngoài miền đã mô tả. Khi mở rộng, cần thêm ca kiểm thử và kiểm tra miền giá trị, không chỉ thêm nhiều nhánh regex rồi mặc định mọi đầu ra đều đúng về ngữ nghĩa.

##### Output Cách 2

| Vị trí | Mô tả | `dien_tich_m2` |
|---|---|---|
| 0 | Căn hộ 45 m2 thoáng mát | 45.0 |
| 1 | Phòng 30m² trung tâm | 30.0 |
| 2 | Studio 45.5 m2 sạch sẽ | 45.5 |
| 3 | Chỗ ở 45,5 m² đẹp | 45.5 |
| 4 | Mã phòng 30m2x không nhận | `NaN` |
| 5 | Không ghi diện tích | `NaN` |

#### So sánh hai cách

Hai cách cùng trích được bốn số và để hai dòng còn lại khuyết. Cách 1 mở rõ từng bước để quan sát chuỗi trung gian. Cách 2 tạo một thao tác dùng lại cho cột mô tả. Cả hai chỉ xác nhận các dạng diện tích đã quy định, không chứng minh đơn vị và con số mô tả đúng thực tế.

:::
