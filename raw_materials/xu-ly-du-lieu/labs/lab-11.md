## Lab 11: Kiểm tra phản hồi của mô hình ngôn ngữ

Một phản hồi có đúng cấu trúc JSON vẫn có thể đọc sai cảm xúc của người viết. Ta sẽ kiểm riêng cấu trúc, độ khớp với nhãn tay và các dấu hiệu cần xem lại trên bộ phản hồi mô phỏng, không cần gọi dịch vụ trả phí.

## Thông tin dữ liệu thực hành

Bộ bài tập sử dụng dữ liệu đánh giá chỗ ở Inside Airbnb với ảnh chụp ngày 29/06/2026 tại thành phố Santiago (Chile).
Tệp dữ liệu gốc công bố tại địa chỉ mạng: `https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/data/reviews.csv.gz`.

Nhằm phục vụ kiểm thử nhanh, độc lập môi trường và chạy trực tiếp không phụ thuộc kết nối mạng, các bài thực hành dưới đây sử dụng tập dữ liệu kiểm thử nhỏ gồm 240 bình luận giả lập `DEMO_RV` cho bài toán chọn mẫu, cùng bộ 10 đánh giá thực tế `REVIEWS`, tập nhãn tay chuẩn `GOLD` và tập phản hồi mô phỏng `LLM_OUT` có cài sẵn lỗi cấu trúc và ngữ nghĩa:

```python
import json
import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError, ConfigDict
from typing import Literal

_MAU_CAU = [
    "Great location, clean apartment and a very responsive host.",
    "Buena ubicación y departamento limpio, volvería sin duda.",
    "Ok",
    ".",
    "Nice",
    "Todo bien, gracias.",
    "The apartment was noisy at night but the view was amazing.",
    "Excelente anfitrión, muy atento a todo lo que necesitamos.",
    "Muy bueno",
    "Good value for money, close to the metro and supermarkets.",
]
DEMO_RV = pd.DataFrame(
    {
        "id": range(5000, 5240),
        "comments": [f"{_MAU_CAU[k % 10]} (#{k})" for k in range(240)],
    }
)

REVIEWS = {
    1: "Place is great for a family, all clean, good location, bit noisy as the main avenue is behind, but we had a great time.",
    2: "Apartment was irrelevant with pictures and not clean too so we cancelled our reservation. Alvaro helped us about cancellation process.",
    3: "Cristian fue muy amable en todo momento, el lugar como se describia. La zona con muy buena movilidad. Muy recomendable. Gracias Cristian",
    4: "Hermoso alojamiento! Lo pasamos re bien mi hija y yo. Es un poco ruidosa la zona si se abre la ventana. La vista es bella y esta muy bien ubicado. Sin duda volveriamos",
    5: "Great location but apartment needs some attention to detail. Cable TV and wifi was out of service. Communication with host was poor. Bedding was not optimal.",
    6: "Good WiFi, great location and centrally located. Shower was hot and had good pressure and there was enough space for two people for 6 days.",
    7: "Es tal cual las fotos, buena ubicacion, tranquilo y sin ruido. Es en un piso 15 por si le temen a las alturas.",
    8: ".",
    9: "Nice place in cool region. Very noisy environment and apartment is not very clean.",
    10: "location was great, wifi was spotty. But overall not a bad place.",
}

GOLD = {
    1: {"sentiment": "mixed", "language": "en"},
    2: {"sentiment": "negative", "language": "en"},
    3: {"sentiment": "positive", "language": "es"},
    4: {"sentiment": "mixed", "language": "es"},
    5: {"sentiment": "negative", "language": "en"},
    6: {"sentiment": "positive", "language": "en"},
    7: {"sentiment": "positive", "language": "es"},
    8: {"sentiment": "mixed", "language": "und"},
    9: {"sentiment": "mixed", "language": "en"},
    10: {"sentiment": "mixed", "language": "en"},
}

LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}

print(
    f"Khởi tạo thành công {len(DEMO_RV)} bình luận giả lập và {len(REVIEWS)} đánh giá đối chiếu."
)
```

Lưu ý: Mọi kết quả tính toán trên tập mẫu 240 dòng này là dữ liệu giả lập phục vụ kiểm chứng thuật toán, không đại diện cho quy mô và đặc trưng phân phối thực tế của toàn bộ thị trường Santiago.

---

## Danh mục bài tập thực hành

<span id="data-lab-11-01"></span>
### Bài 1: Chọn mẫu bình luận tái lập được theo độ dài tối thiểu

::: exercise
Xây dựng hàm chọn mẫu ngẫu nhiên có kiểm soát hạt giống từ bảng dữ liệu bình luận sau khi đã áp dụng bộ lọc độ dài tối thiểu.

Yêu cầu kỹ thuật:
- Đầu vào: Bảng `rv` kiểu `pd.DataFrame` chứa cột `comments` kiểu chuỗi, ngưỡng độ dài tối thiểu `do_dai_min` kiểu số nguyên (mặc định 50), số lượng mẫu `n` kiểu số nguyên (mặc định 100), và hạt giống ngẫu nhiên `seed` kiểu số nguyên (mặc định 42).
- Thao tác: Lọc các bản ghi có chiều dài văn bản lớn hơn hoặc bằng `do_dai_min`, sau đó thực hiện lấy mẫu ngẫu nhiên đúng `n` dòng thông qua phương thức `.sample(n=n, random_state=seed)`.
- Đầu ra: Trả về một `pd.DataFrame` chứa đầy đủ các cột và giữ nguyên chỉ số (index) gốc do phương thức `sample` sinh ra.
- Trường hợp biên: Không làm thay đổi bảng dữ liệu đầu vào. Đưa ra thông báo hoặc xử lý khi số lượng bản ghi sau khi lọc nhỏ hơn số lượng mẫu yêu cầu `n`.
- Phân tích kỹ thuật: Trình bày hiện tượng thiên lệch chọn mẫu (selection bias) khi loại bỏ các bình luận quá ngắn.
:::

::: solution
#### Cách 1: Lọc dữ liệu qua phép lập chỉ mục boolean và lấy mẫu ngẫu nhiên

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

_MAU_CAU = [
    "Great location, clean apartment and a very responsive host.",
    "Buena ubicación y departamento limpio, volvería sin duda.",
    "Ok",
    ".",
    "Nice",
    "Todo bien, gracias.",
    "The apartment was noisy at night but the view was amazing.",
    "Excelente anfitrión, muy atento a todo lo que necesitamos.",
    "Muy bueno",
    "Good value for money, close to the metro and supermarkets.",
]

DEMO_RV = pd.DataFrame(
    {
        "id": range(5000, 5240),
        "comments": [f"{_MAU_CAU[k % 10]} (#{k})" for k in range(240)],
    }
)

# Bắt đầu lời giải


def choose_sample(
    rv: pd.DataFrame, do_dai_min: int = 50, n: int = 100, seed: int = 42
) -> pd.DataFrame:
    """Lọc các dòng có độ dài bình luận tối thiểu và lấy mẫu ngẫu nhiên có hạt giống.

    Tham số rv: Bảng dữ liệu chứa cột comments.
    Tham số do_dai_min: Ngưỡng ký tự tối thiểu của bình luận.
    Tham số n: Số lượng dòng mẫu cần trích xuất.
    Tham số seed: Hạt giống ngẫu nhiên nhằm bảo đảm tính tái lập.
    """
    van_ban = rv.dropna(subset=["comments"]).copy()
    van_ban["comments"] = van_ban["comments"].str.replace("<br/>", " ", regex=False)
    loc_do_dai = van_ban.loc[van_ban["comments"].str.len().ge(do_dai_min)]
    mau_ngau_nhien = loc_do_dai.sample(n=n, random_state=seed)
    return mau_ngau_nhien


mau_co_ban = choose_sample(DEMO_RV, do_dai_min=50, n=100, seed=42)
print(
    f"Cách 1: Đã lấy {len(mau_co_ban)} dòng, 3 ID đầu tiên: {mau_co_ban['id'].head(3).tolist()}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Lọc dòng có văn bản, thay đúng thẻ xuống dòng được quy định rồi kiểm độ dài. `sample` dùng `random_state` để chọn lại cùng mẫu khi dữ liệu và phiên bản giữ nguyên. Kết quả chỉ đại diện cho miền văn bản qua bộ lọc, không tự đại diện cho mọi review.

#### Kết quả cách 1

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 1: Đã lấy 100 dòng, 3 ID đầu tiên: [5089, 5096, 5009] |

#### Cách 2: Kiểm soát ràng buộc số lượng bản ghi và trích xuất mẫu an toàn

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

_MAU_CAU = [
    "Great location, clean apartment and a very responsive host.",
    "Buena ubicación y departamento limpio, volvería sin duda.",
    "Ok",
    ".",
    "Nice",
    "Todo bien, gracias.",
    "The apartment was noisy at night but the view was amazing.",
    "Excelente anfitrión, muy atento a todo lo que necesitamos.",
    "Muy bueno",
    "Good value for money, close to the metro and supermarkets.",
]

DEMO_RV = pd.DataFrame(
    {
        "id": range(5000, 5240),
        "comments": [f"{_MAU_CAU[k % 10]} (#{k})" for k in range(240)],
    }
)


def choose_sample(
    rv: pd.DataFrame, do_dai_min: int = 50, n: int = 100, seed: int = 42
) -> pd.DataFrame:
    """Lọc các dòng có độ dài bình luận tối thiểu và lấy mẫu ngẫu nhiên có hạt giống.

    Tham số rv: Bảng dữ liệu chứa cột comments.
    Tham số do_dai_min: Ngưỡng ký tự tối thiểu của bình luận.
    Tham số n: Số lượng dòng mẫu cần trích xuất.
    Tham số seed: Hạt giống ngẫu nhiên nhằm bảo đảm tính tái lập.
    """
    van_ban = rv.dropna(subset=["comments"]).copy()
    van_ban["comments"] = van_ban["comments"].str.replace("<br/>", " ", regex=False)
    loc_do_dai = van_ban.loc[van_ban["comments"].str.len().ge(do_dai_min)]
    mau_ngau_nhien = loc_do_dai.sample(n=n, random_state=seed)
    return mau_ngau_nhien


mau_co_ban = choose_sample(DEMO_RV, do_dai_min=50, n=100, seed=42)

# Bắt đầu lời giải


def choose_sample_robust(
    rv: pd.DataFrame, do_dai_min: int = 50, n: int = 100, seed: int = 42
) -> pd.DataFrame:
    """Trích xuất mẫu có kiểm soát điều kiện biên và bảo toàn tính bất biến của bảng nguồn.

    Tham số rv: Bảng dữ liệu nguồn cần trích xuất mẫu.
    Tham số do_dai_min: Độ dài ký tự tối thiểu.
    Tham số n: Số dòng cần lấy mẫu.
    Tham số seed: Hạt giống sinh số ngẫu nhiên.
    """
    if "comments" not in rv.columns:
        raise KeyError("Bảng dữ liệu thiếu cột bắt buộc: comments")
    van_ban = rv.dropna(subset=["comments"]).copy()
    van_ban["comments"] = van_ban["comments"].str.replace("<br/>", " ", regex=False)
    bang_loc = van_ban.loc[van_ban["comments"].str.len().ge(do_dai_min)]
    if len(bang_loc) < n:
        raise ValueError(
            f"Số lượng bản ghi đạt chuẩn ({len(bang_loc)}) không đủ để lấy {n} mẫu."
        )
    return bang_loc.sample(n=n, random_state=seed).copy()


mau_chuan = choose_sample_robust(DEMO_RV, do_dai_min=50, n=100, seed=42)
print(
    f"Cách 2: Đã lấy {len(mau_chuan)} dòng, kiểm tra trùng khớp: {mau_co_ban['id'].equals(mau_chuan['id'])}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Kiểm số dòng đủ điều kiện trước khi lấy mẫu giúp báo lỗi có nghĩa thay vì âm thầm giảm cỡ mẫu. `.copy()` giữ vùng dữ liệu dùng để chuẩn hóa riêng. Ngưỡng độ dài có thể loại các nhận xét ngắn nhưng rõ ý, nên phải ghi bộ lọc khi báo chất lượng mô hình.

#### Kết quả cách 2

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 2: Đã lấy 100 dòng, kiểm tra trùng khớp: True |
#### So sánh cách dùng

Cách 1 giúp quan sát bộ lọc văn bản và việc lấy mẫu có hạt giống cố định. Cách 2 bổ sung bước kiểm tra số dòng đủ điều kiện để báo rõ khi không thể lấy đủ mẫu. Cả hai đều phải công bố ngưỡng độ dài đã dùng.

:::

---

<span id="data-lab-11-02"></span>
### Bài 2: Ước lượng số lượng token và chi phí tính toán trước khi gọi mô hình

::: exercise
Xây dựng hàm ước lượng tổng số lượng token đầu vào và tổng chi phí tài chính tương ứng cho một tập hợp các chuỗi văn bản dựa trên quy tắc ngón tay cái và đơn giá giả định.

Yêu cầu kỹ thuật:
- Đầu vào: Cột văn bản `comments` kiểu `pd.Series` chứa các chuỗi ký tự, và đơn giá `gia_moi_trieu` kiểu số thực biểu thị chi phí USD cho $1$ triệu token đầu vào (mặc định $0{,}25$ USD).
- Thao tác: Áp dụng quy tắc ngón tay cái tính số token của mỗi chuỗi bằng phép chia nguyên cho $4$ (`len(cmt) // 4`). Sau đó tính tổng số token trên toàn bộ các chuỗi. Chi phí được tính theo công thức:
Gọi tổng số token ước lượng là $N$ và đơn giá giả định trên một triệu token là $p$. Chi phí ước lượng cùng đơn vị tiền với đơn giá:

$$
C = \frac{Np}{10^6}.
$$
- Đầu ra: Trả về một từ điển (`dict`) gồm đúng hai khóa: `"tong_token"` kiểu số nguyên (`int`) và `"chi_phi"` kiểu số thực (`float`), không làm tròn.
- Trường hợp biên: Xử lý an toàn khi Series đầu vào rỗng (trả về 0 token và 0.0 chi phí). Phép chia nguyên phải được thực hiện trên từng dòng riêng biệt trước khi tính tổng, không lấy tổng chiều dài rồi mới chia cho 4.
:::

::: solution
#### Cách 1: Duyệt vòng lặp tích lũy từng dòng văn bản

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

# Bắt đầu lời giải


def estimate_cost(comments: pd.Series, gia_moi_trieu: float = 0.25) -> dict:
    """Ước lượng tổng số token và chi phí bằng vòng lặp cộng dồn từng dòng.

    Tham số comments: Chuỗi các đoạn văn bản đánh giá.
    Tham số gia_moi_trieu: Đơn giá USD cho một triệu token đầu vào.
    """
    tong_token = 0
    for cmt in comments:
        tong_token += len(str(cmt)) // 4
    chi_phi = tong_token * gia_moi_trieu / 1_000_000
    return {"tong_token": int(tong_token), "chi_phi": float(chi_phi)}


vi_du_chuoi = pd.Series(["abcdefg", "abcd", "abc"])
kq_uoc_tinh = estimate_cost(vi_du_chuoi, gia_moi_trieu=0.25)
print(
    f"Cách 1: Tổng token = {kq_uoc_tinh['tong_token']}, Chi phí = ${kq_uoc_tinh['chi_phi']:.8f}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Đếm độ dài văn bản rồi dùng quy tắc ước lượng token của đề. Nhân tổng token với đơn giá giả định cho chi phí ước tính, không phải số tiền đã thanh toán. Ước lượng này chưa thay thế tokenizer hay hóa đơn của nhà cung cấp.

#### Kết quả cách 1

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 1: Tổng token = 2, Chi phí = $0.00000050 |

#### Cách 2: Tính toán vector hóa trên pandas Series

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import pandas as pd

# Bắt đầu lời giải


def estimate_cost_vectorized(comments: pd.Series, gia_moi_trieu: float = 0.25) -> dict:
    """Ước lượng token và chi phí thông qua biểu thức vector hóa của pandas.

    Tham số comments: Series chứa văn bản đầu vào.
    Tham số gia_moi_trieu: Đơn giá USD tính trên mỗi triệu token.
    """
    if comments.empty:
        return {"tong_token": 0, "chi_phi": 0.0}
    tong_token = int((comments.astype(str).str.len() // 4).sum())
    chi_phi = float(tong_token * gia_moi_trieu / 1_000_000)
    return {"tong_token": tong_token, "chi_phi": chi_phi}


vi_du_chuoi = pd.Series(["abcdefg", "abcd", "abc"])
kq_mau_vector = estimate_cost_vectorized(vi_du_chuoi, gia_moi_trieu=0.25)
print(
    f"Cách 2: Tổng token = {kq_mau_vector['tong_token']}, Chi phí = ${kq_mau_vector['chi_phi']:.8f}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Tính theo Series làm rõ tổng ký tự và số bản ghi thay vì tích lũy thủ công. Tham số đơn giá cần giữ đơn vị trên một triệu token và thang tiền tệ đã nêu. Nếu thêm token đầu ra hoặc lời nhắc dùng chung, phải đưa chúng vào một giả thiết mới và báo riêng.

#### Kết quả cách 2

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 2: Tổng token = 2, Chi phí = $0.00000050 |
#### So sánh cách dùng

Hãy chọn Cách 1 khi bạn muốn theo dõi chi tiết độ dài ký tự và lượng token ước tính của từng phản hồi để kiểm chứng. Cách 2 phù hợp khi cần tính tổng chi phí dự kiến cho toàn bộ tập dữ liệu bằng các phép toán cột của pandas.

:::

---

<span id="data-lab-11-03"></span>
### Bài 3: Thiết lập lược đồ ràng buộc dữ liệu đầu ra với Pydantic

::: exercise
Xây dựng lớp lược đồ dữ liệu `ReviewInfo` kế thừa từ `BaseModel` của thư viện Pydantic nhằm kiểm soát định dạng, kiểu dữ liệu và danh mục giá trị cho phép của kết quả phân tích cảm xúc từ mô hình ngôn ngữ lớn.

Yêu cầu kỹ thuật:
- Định nghĩa kiểu tập hợp giá trị khía cạnh:
  `Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]`
- Định nghĩa lớp `ReviewInfo(BaseModel)` gồm đúng 4 trường bắt buộc, không có giá trị mặc định:
  1. `sentiment`: Nhận một trong ba giá trị thuộc `Literal["positive", "mixed", "negative"]`.
  2. `aspects_positive`: Danh sách các khía cạnh tích cực kiểu `list[Aspect]`.
  3. `aspects_negative`: Danh sách các khía cạnh tiêu cực kiểu `list[Aspect]`.
  4. `language`: Chuỗi ký tự định danh mã ngôn ngữ kiểu `str`.
- Hành vi kiểm định: Khi nạp dữ liệu hợp lệ, đối tượng được khởi tạo thành công và xuất dữ liệu thông qua phương thức `model_dump()`. Khi gặp nhãn ngoài danh mục, thiếu trường bắt buộc, hoặc sai kiểu dữ liệu, hệ thống bắt buộc phải ném ngoại lệ `ValidationError`. Tuyệt đối không tự ý sửa đổi dữ liệu sai lệch.
:::

::: solution
#### Cách 1: Khai báo lớp Pydantic tiêu chuẩn với kiểu chú thích Type Annotations

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

# Bắt đầu lời giải

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


mau_hop_le_json = (
    '{"sentiment": "mixed", "aspects_positive": ["location"], '
    '"aspects_negative": ["noise"], "language": "en"}'
)
doi_tuong_hop_le = ReviewInfo.model_validate_json(mau_hop_le_json)
print(
    f"Cách 1: Khởi tạo thành công, sentiment = {doi_tuong_hop_le.sentiment}, "
    f"aspects_negative = {doi_tuong_hop_le.aspects_negative}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Lược đồ định nghĩa các trường bắt buộc cùng miền nhãn cho cảm xúc, khía cạnh và ngôn ngữ. Kiểm từng trường giúp thấy phản hồi bị loại vì thiếu dữ liệu, sai kiểu hay nhãn ngoài danh mục. Một phản hồi qua lược đồ vẫn có thể gán cảm xúc sai so với văn bản.

#### Kết quả cách 1

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 1: Khởi tạo thành công, sentiment = mixed, aspects_negative = ['noise'] |

#### Cách 2: Khai báo lớp Pydantic nghiêm ngặt cấm trường thừa và chuẩn hóa chuỗi

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]

# Bắt đầu lời giải


class ReviewInfoStrict(BaseModel):
    """Lược đồ dữ liệu với chế độ kiểm soát nghiêm ngặt ngăn chặn trường dư thừa."""

    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


try:
    ReviewInfoStrict.model_validate_json(
        '{"sentiment": "happy", "aspects_positive": [], "aspects_negative": [], "language": "en"}'
    )
except ValidationError as loi_kiem_dinh:
    print(
        f"Cách 2: Chặn thành công nhãn ngoài danh mục. Chi tiết lỗi: {loi_kiem_dinh.errors()[0]['msg']}"
    )

# Kết thúc lời giải
```

#### Giải thích cách 2

Pydantic gom quy tắc cấu trúc vào một mô hình có thể dùng lại. `Literal` giới hạn các nhãn được chấp nhận, còn cấu hình trường thừa và chế độ kiểm kiểu phải được đọc cùng nhau. Ngoại lệ kiểm tra cho biết quy tắc nào không khớp, không chứng minh mô hình đã đọc đúng ý nghĩa câu.

#### Kết quả cách 2

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 2: Chặn thành công nhãn ngoài danh mục. Chi tiết lỗi: Input should be 'positive', 'mixed' or 'negative' |
#### So sánh cách dùng

Kiểm từng trường trong Cách 1 giúp hiểu vì sao một phản hồi bị loại. Cách 2 gom các ràng buộc vào mô hình Pydantic để dùng lại và đọc lỗi kiểm tra. Với cả hai, đúng lược đồ chưa chứng minh nhãn cảm xúc đúng với câu nhận xét.

:::

---

<span id="data-lab-11-04"></span>
### Bài 4: Kiểm định hàng loạt và phân tách bản ghi lỗi cấu trúc

::: exercise
Xây dựng hàm kiểm định hàng loạt các chuỗi phản hồi JSON từ mô hình ngôn ngữ lớn, phân tách độc lập các bản ghi đạt chuẩn vào nhóm hợp lệ và thu thập mã định danh của các bản ghi gặp lỗi lược đồ vào danh sách cảnh báo.

Yêu cầu kỹ thuật:
- Đầu vào: Từ điển `llm_out` có dạng `{id: raw_json_str}`, trong đó khóa `id` có thể là số nguyên hoặc chuỗi ký tự.
- Thao tác: Duyệt qua từng phần tử theo đúng thứ tự xuất hiện của từ điển. Gọi hàm kiểm định `ReviewInfo.model_validate_json(raw_json)`. Nếu hợp lệ, lưu đối tượng `ReviewInfo` vào từ điển `hop_le[id]`. Nếu phát sinh ngoại lệ `ValidationError` (do nhãn ngoài danh mục, thiếu trường hoặc chuỗi JSON bị hỏng), lưu mã định danh `id` vào danh sách `loi_schema`.
- Đầu ra: Trả về một từ điển gồm đúng hai khóa: `"hop_le"` (chứa từ điển các đối tượng đạt chuẩn) và `"loi_schema"` (chứa danh sách các `id` bị chặn theo thứ tự ban đầu).
- Trường hợp biên: Không thay đổi từ điển đầu vào. Khóa `id` dạng chuỗi phải được giữ nguyên kiểu dữ liệu ban đầu. Chuỗi JSON hỏng cú pháp cũng phải được nhận diện và xếp vào danh sách `loi_schema`.
:::

::: solution
#### Cách 1: Vòng lặp tường minh phân tách dữ liệu bằng khối try và except

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}

# Bắt đầu lời giải


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


ket_qua_kiem_dinh = validate_outputs(LLM_OUT)
print(
    f"Cách 1: Số lượng hợp lệ = {len(ket_qua_kiem_dinh['hop_le'])}, "
    f"Danh sách ID lỗi lược đồ = {ket_qua_kiem_dinh['loi_schema']}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Duyệt từng ID, giữ phản hồi hợp lệ và ghi riêng ID lỗi cấu trúc. Không để một phản hồi lỗi làm mất toàn bộ đợt đánh giá. Dữ liệu gốc cần được giữ để đọc lại nguyên nhân, thay vì chỉ giữ một tổng số lỗi.

#### Kết quả cách 1

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 1: Số lượng hợp lệ = 8, Danh sách ID lỗi lược đồ = [2, 5] |

#### Cách 2: Đóng gói nhật ký kiểm toán chi tiết nguyên nhân lỗi

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}

# Bắt đầu lời giải


def validate_outputs_with_audit(llm_out: dict) -> dict:
    """Kiểm tra lược đồ hàng loạt kết hợp trích xuất nhật ký lỗi cấu trúc chi tiết.

    Tham số llm_out: Từ điển chứa các phản hồi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    chi_tiet_loi = {}
    for rid, raw_text in llm_out.items():
        try:
            hop_le[rid] = ReviewInfo.model_validate_json(raw_text)
        except ValidationError as loi_val:
            loi_schema.append(rid)
            chi_tiet_loi[rid] = [
                {
                    "truong": err["loc"],
                    "kieu_loi": err["type"],
                    "thong_diep": err["msg"],
                }
                for err in loi_val.errors()
            ]
        except Exception as loi_khac:
            loi_schema.append(rid)
            chi_tiet_loi[rid] = [
                {
                    "truong": ("root",),
                    "kieu_loi": "json_decode_error",
                    "thong_diep": str(loi_khac),
                }
            ]
    return {"hop_le": hop_le, "loi_schema": loi_schema, "chi_tiet_loi": chi_tiet_loi}


kq_kiem_toan = validate_outputs_with_audit(LLM_OUT)
print(
    f"Cách 2: Ghi nhận {len(kq_kiem_toan['chi_tiet_loi'])} bản ghi lỗi với đầy đủ nhật ký kiểm toán."
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Báo cáo kiểm tra có thể giữ ID, trạng thái và thông tin lỗi cho mỗi phản hồi. Việc tách phần hợp lệ khỏi phần bị loại giúp tính đúng mẫu số ở bước sau. Không gọi tỷ lệ hợp lệ là độ chính xác cảm xúc, vì đây là hai phép đo khác nhau.

#### Kết quả cách 2

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 2: Ghi nhận 2 bản ghi lỗi với đầy đủ nhật ký kiểm toán. |
#### So sánh cách dùng

Hãy chọn Cách 1 khi bạn chỉ cần tách nhanh các phản hồi hợp lệ để chuyển tiếp sang bước đánh giá mà không cần ghi nhận sâu lỗi. Cách 2 cần thiết khi phải lưu chi tiết mã lỗi và lý do không đạt chuẩn để phục vụ kiểm toán lời nhắc.

:::

---

<span id="data-lab-11-05"></span>
### Bài 5: Đo lường độ chính xác phân loại cảm xúc so với nhãn tay chuẩn

::: exercise
Xây dựng hàm đo lường độ chính xác của nhãn cảm xúc do mô hình ngôn ngữ lớn dự đoán trên tập hợp các đầu ra hợp lệ bằng cách đối chiếu với tập nhãn tay chuẩn (gold standard).

Yêu cầu kỹ thuật:
- Đầu vào: Từ điển `du_doan` có dạng `{id: sentiment_str}` chứa các nhãn do mô hình dự đoán (chỉ gồm các bản ghi đã qua kiểm định lược đồ, có ít nhất một phần tử), và từ điển `gold` có dạng `{id: {"sentiment": str, ...}}` chứa nhãn tay chuẩn tương ứng với mọi `id` trong `du_doan`.
- Thao tác: So khớp giá trị `du_doan[id]` với `gold[id]["sentiment"]`. Đếm số lượng bản ghi có nhãn trùng khớp (`so_dung`), tính tỷ lệ chính xác (`acc = so_dung / len(du_doan)`), và thu thập danh sách các `id` dự đoán sai theo đúng thứ tự xuất hiện của `du_doan`.
- Đầu ra: Trả về từ điển gồm đúng ba khóa: `"so_dung"` kiểu số nguyên, `"acc"` kiểu số thực, và `"sai"` kiểu danh sách chứa các `id` dự đoán không chính xác.
- Phân tích kỹ thuật: Làm rõ sự khác biệt giữa mẫu số chỉ tính trên các bản ghi hợp lệ lược đồ ($8$ bản ghi) và mẫu số tính trên toàn bộ tập dữ liệu ban đầu ($10$ bản ghi).
:::

::: solution
#### Cách 1: So khớp tuần tự bằng phép lặp từ điển

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


ket_qua_kiem_dinh = validate_outputs(LLM_OUT)

GOLD = {
    1: {"sentiment": "mixed", "language": "en"},
    2: {"sentiment": "negative", "language": "en"},
    3: {"sentiment": "positive", "language": "es"},
    4: {"sentiment": "mixed", "language": "es"},
    5: {"sentiment": "negative", "language": "en"},
    6: {"sentiment": "positive", "language": "en"},
    7: {"sentiment": "positive", "language": "es"},
    8: {"sentiment": "mixed", "language": "und"},
    9: {"sentiment": "mixed", "language": "en"},
    10: {"sentiment": "mixed", "language": "en"},
}

tap_du_doan = {rid: obj.sentiment for rid, obj in ket_qua_kiem_dinh["hop_le"].items()}

# Bắt đầu lời giải


def sentiment_accuracy(du_doan: dict, gold: dict) -> dict:
    """Tính độ chính xác của nhãn cảm xúc so với nhãn tay chuẩn.

    Tham số du_doan: Từ điển nhãn cảm xúc dự đoán theo từng ID.
    Tham số gold: Từ điển nhãn tay chuẩn của chuyên viên đánh giá.
    """
    so_dung = 0
    sai = []
    for rid, nhan_du_doan in du_doan.items():
        nhan_chuan = gold[rid]["sentiment"]
        if nhan_du_doan == nhan_chuan:
            so_dung += 1
        else:
            sai.append(rid)
    do_chinh_xac = so_dung / len(du_doan) if du_doan else 0.0
    return {"so_dung": so_dung, "acc": float(do_chinh_xac), "sai": sai}


tap_du_doan = {rid: obj.sentiment for rid, obj in ket_qua_kiem_dinh["hop_le"].items()}
kq_do_luong = sentiment_accuracy(tap_du_doan, GOLD)
print(
    f"Cách 1: Số câu đúng = {kq_do_luong['so_dung']}/8, "
    f"Độ chính xác = {kq_do_luong['acc']:.1%}, Các ID dự đoán sai = {kq_do_luong['sai']}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Đối chiếu nhãn dự đoán với nhãn tay trên các ID cùng tồn tại. Đếm số khớp và số được đánh giá trước khi chia. Báo cả tỷ lệ trong tập hợp lệ lẫn tỷ lệ trên toàn mẫu khi đề yêu cầu, không che các phản hồi lỗi cấu trúc bằng cách bỏ chúng khỏi mẫu số mà không nói rõ.

#### Kết quả cách 1

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 1: Số câu đúng = 5/8, Độ chính xác = 62.5%, Các ID dự đoán sai = [4, 9, 10] |

#### Cách 2: Đối chiếu qua cấu trúc bảng pandas DataFrame

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

import pandas as pd

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


ket_qua_kiem_dinh = validate_outputs(LLM_OUT)

GOLD = {
    1: {"sentiment": "mixed", "language": "en"},
    2: {"sentiment": "negative", "language": "en"},
    3: {"sentiment": "positive", "language": "es"},
    4: {"sentiment": "mixed", "language": "es"},
    5: {"sentiment": "negative", "language": "en"},
    6: {"sentiment": "positive", "language": "en"},
    7: {"sentiment": "positive", "language": "es"},
    8: {"sentiment": "mixed", "language": "und"},
    9: {"sentiment": "mixed", "language": "en"},
    10: {"sentiment": "mixed", "language": "en"},
}

tap_du_doan = {rid: obj.sentiment for rid, obj in ket_qua_kiem_dinh["hop_le"].items()}

# Bắt đầu lời giải


def sentiment_accuracy_df(du_doan: dict, gold: dict) -> dict:
    """Tính độ chính xác cảm xúc thông qua đối tượng bảng pandas DataFrame.

    Tham số du_doan: Từ điển nhãn dự đoán.
    Tham số gold: Từ điển nhãn chuẩn.
    """
    records = []
    for rid, pred in du_doan.items():
        records.append({"id": rid, "pred": pred, "gold": gold[rid]["sentiment"]})
    df_so_sanh = pd.DataFrame(records)
    dung_mask = df_so_sanh["pred"] == df_so_sanh["gold"]
    so_dung = int(dung_mask.sum())
    acc = float(so_dung / len(df_so_sanh)) if len(df_so_sanh) > 0 else 0.0
    sai = df_so_sanh.loc[~dung_mask, "id"].tolist()
    return {"so_dung": so_dung, "acc": acc, "sai": sai}


kq_do_luong_df = sentiment_accuracy_df(tap_du_doan, GOLD)
print(
    f"Cách 2: Xác nhận độ chính xác = {kq_do_luong_df['acc']:.3f}, Sai lệch tại ID: {kq_do_luong_df['sai']}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Đưa nhãn dự đoán và tham chiếu thành hai cột giúp nhìn trực tiếp các ID không khớp. Phải căn theo ID, không ghép theo vị trí vì thứ tự hai dict hoặc hai bảng có thể khác. Nhãn tay cũng cần quy tắc gán nhất quán, nên đây là độ khớp với bộ tham chiếu đã cho.

#### Kết quả cách 2

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 2: Xác nhận độ chính xác = 0.625, Sai lệch tại ID: [4, 9, 10] |
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi dữ liệu ở dạng từ điển thuần túy và chỉ muốn tính nhanh tỷ lệ chính xác trên tập chung. Cách 2 trực quan hơn khi bạn cần đưa hai nguồn nhãn vào cùng một bảng để dễ quan sát và lọc các trường hợp gán sai.

:::

---

<span id="data-lab-11-06"></span>
### Bài 6: Phân loại lỗi ngữ nghĩa và quy chuẩn hóa hướng dẫn gán nhãn

::: exercise
Xây dựng hàm phân loại các trường hợp dự đoán sai thành các nhóm nguyên nhân ngữ nghĩa đặc thù dựa trên ngữ cảnh thực tế của văn bản đánh giá, đồng thời thiết lập cấu trúc bảng đối chiếu phục vụ cải tiến lời nhắc (prompt engineering) và hướng dẫn gán nhãn.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách mã lỗi `sai_ids` kiểu `list`, từ điển bài đánh giá gốc `reviews` kiểu `dict`, từ điển nhãn dự đoán `predictions` kiểu `dict`, và từ điển nhãn chuẩn `gold` kiểu `dict`.
- Thao tác: Trích xuất nội dung văn bản gốc cùng cặp nhãn đối lập cho từng ID bị gán sai (ID 4, 9, 10). Phân loại chính xác bản chất lỗi theo ba nhóm nguyên nhân:
  1. Bỏ sót ý chê do lời khen lấn át (ID 4).
  2. Bất đồng ranh giới phân loại do tính chất phức hợp (ID 9).
  3. Hiểu sai câu phủ định ngữ dụng (ID 10).
- Đầu ra: Trả về một `pd.DataFrame` chứa các cột `id`, `gold`, `llm`, `kieu_loi`, `ngu_canh_ngan`.
- Phân tích kỹ thuật: Giải thích vai trò của tài liệu Hướng dẫn gán nhãn (Annotation Guidelines) như một mốc tham chiếu thống nhất khi người gán nhãn xuất hiện bất đồng quan điểm.
:::

::: solution
#### Cách 1: Ánh xạ quy tắc phân loại lỗi qua từ điển danh mục

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

import pandas as pd

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


ket_qua_kiem_dinh = validate_outputs(LLM_OUT)

GOLD = {
    1: {"sentiment": "mixed", "language": "en"},
    2: {"sentiment": "negative", "language": "en"},
    3: {"sentiment": "positive", "language": "es"},
    4: {"sentiment": "mixed", "language": "es"},
    5: {"sentiment": "negative", "language": "en"},
    6: {"sentiment": "positive", "language": "en"},
    7: {"sentiment": "positive", "language": "es"},
    8: {"sentiment": "mixed", "language": "und"},
    9: {"sentiment": "mixed", "language": "en"},
    10: {"sentiment": "mixed", "language": "en"},
}

tap_du_doan = {rid: obj.sentiment for rid, obj in ket_qua_kiem_dinh["hop_le"].items()}


def sentiment_accuracy(du_doan: dict, gold: dict) -> dict:
    """Tính độ chính xác của nhãn cảm xúc so với nhãn tay chuẩn.

    Tham số du_doan: Từ điển nhãn cảm xúc dự đoán theo từng ID.
    Tham số gold: Từ điển nhãn tay chuẩn của chuyên viên đánh giá.
    """
    so_dung = 0
    sai = []
    for rid, nhan_du_doan in du_doan.items():
        nhan_chuan = gold[rid]["sentiment"]
        if nhan_du_doan == nhan_chuan:
            so_dung += 1
        else:
            sai.append(rid)
    do_chinh_xac = so_dung / len(du_doan) if du_doan else 0.0
    return {"so_dung": so_dung, "acc": float(do_chinh_xac), "sai": sai}


kq_do_luong = sentiment_accuracy(tap_du_doan, GOLD)

REVIEWS = {
    1: "Place is great for a family, all clean, good location, bit noisy as the main avenue is behind, but we had a great time.",
    2: "Apartment was irrelevant with pictures and not clean too so we cancelled our reservation. Alvaro helped us about cancellation process.",
    3: "Cristian fue muy amable en todo momento, el lugar como se describia. La zona con muy buena movilidad. Muy recomendable. Gracias Cristian",
    4: "Hermoso alojamiento! Lo pasamos re bien mi hija y yo. Es un poco ruidosa la zona si se abre la ventana. La vista es bella y esta muy bien ubicado. Sin duda volveriamos",
    5: "Great location but apartment needs some attention to detail. Cable TV and wifi was out of service. Communication with host was poor. Bedding was not optimal.",
    6: "Good WiFi, great location and centrally located. Shower was hot and had good pressure and there was enough space for two people for 6 days.",
    7: "Es tal cual las fotos, buena ubicacion, tranquilo y sin ruido. Es en un piso 15 por si le temen a las alturas.",
    8: ".",
    9: "Nice place in cool region. Very noisy environment and apartment is not very clean.",
    10: "location was great, wifi was spotty. But overall not a bad place.",
}

# Bắt đầu lời giải


def diagnose_semantic_errors(
    sai_ids: list, reviews: dict, predictions: dict, gold: dict
) -> pd.DataFrame:
    """Tạo bảng phân tích và phân loại bản chất lỗi ngữ nghĩa của các ca dự đoán sai.

    Tham số sai_ids: Danh sách các ID dự đoán sai.
    Tham số reviews: Từ điển văn bản đánh giá gốc.
    Tham số predictions: Từ điển nhãn dự đoán của mô hình.
    Tham số gold: Từ điển nhãn chuẩn của chuyên viên.
    """
    danh_muc_loi = {
        4: "Bỏ sót ý chê: Lời khen dài che khuất nhận xét tiêu cực về tiếng ồn",
        9: "Ranh giới nhập nhằng: Nhận xét khen địa điểm nhưng chê tiếng ồn và vệ sinh",
        10: "Hiểu sai phủ định: Cụm từ not a bad place mang nghĩa khen nhẹ nhưng bị đọc thành chê",
    }
    dong_du_lieu = []
    for rid in sai_ids:
        dong_du_lieu.append(
            {
                "id": rid,
                "gold": gold[rid]["sentiment"],
                "llm": predictions[rid],
                "kieu_loi": danh_muc_loi.get(rid, "Lỗi phân loại khác"),
                "ngu_canh_ngan": reviews[rid][:60] + "...",
            }
        )
    return pd.DataFrame(dong_du_lieu)


df_phan_loai = diagnose_semantic_errors(kq_do_luong["sai"], REVIEWS, tap_du_doan, GOLD)
print(f"Cách 1: Đã phân loại {len(df_phan_loai)} trường hợp lỗi ngữ nghĩa điển hình.")

# Kết thúc lời giải
```

#### Giải thích cách 1

Đọc nguyên văn các trường hợp không khớp trước khi đặt tên lỗi. Câu có cả khen và chê, phủ định hoặc khác biệt cách hiểu cần được mô tả bằng bằng chứng ngôn ngữ. Không suy ra nguyên nhân bên trong mô hình chỉ từ một nhãn sai.

#### Kết quả cách 1

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 1: Đã phân loại 3 trường hợp lỗi ngữ nghĩa điển hình. |

#### Cách 2: Tự động nhận diện cấu trúc ngữ nghĩa qua từ khóa đối lập và phủ định

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

import pandas as pd

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


ket_qua_kiem_dinh = validate_outputs(LLM_OUT)

GOLD = {
    1: {"sentiment": "mixed", "language": "en"},
    2: {"sentiment": "negative", "language": "en"},
    3: {"sentiment": "positive", "language": "es"},
    4: {"sentiment": "mixed", "language": "es"},
    5: {"sentiment": "negative", "language": "en"},
    6: {"sentiment": "positive", "language": "en"},
    7: {"sentiment": "positive", "language": "es"},
    8: {"sentiment": "mixed", "language": "und"},
    9: {"sentiment": "mixed", "language": "en"},
    10: {"sentiment": "mixed", "language": "en"},
}

tap_du_doan = {rid: obj.sentiment for rid, obj in ket_qua_kiem_dinh["hop_le"].items()}


def sentiment_accuracy(du_doan: dict, gold: dict) -> dict:
    """Tính độ chính xác của nhãn cảm xúc so với nhãn tay chuẩn.

    Tham số du_doan: Từ điển nhãn cảm xúc dự đoán theo từng ID.
    Tham số gold: Từ điển nhãn tay chuẩn của chuyên viên đánh giá.
    """
    so_dung = 0
    sai = []
    for rid, nhan_du_doan in du_doan.items():
        nhan_chuan = gold[rid]["sentiment"]
        if nhan_du_doan == nhan_chuan:
            so_dung += 1
        else:
            sai.append(rid)
    do_chinh_xac = so_dung / len(du_doan) if du_doan else 0.0
    return {"so_dung": so_dung, "acc": float(do_chinh_xac), "sai": sai}


kq_do_luong = sentiment_accuracy(tap_du_doan, GOLD)

REVIEWS = {
    1: "Place is great for a family, all clean, good location, bit noisy as the main avenue is behind, but we had a great time.",
    2: "Apartment was irrelevant with pictures and not clean too so we cancelled our reservation. Alvaro helped us about cancellation process.",
    3: "Cristian fue muy amable en todo momento, el lugar como se describia. La zona con muy buena movilidad. Muy recomendable. Gracias Cristian",
    4: "Hermoso alojamiento! Lo pasamos re bien mi hija y yo. Es un poco ruidosa la zona si se abre la ventana. La vista es bella y esta muy bien ubicado. Sin duda volveriamos",
    5: "Great location but apartment needs some attention to detail. Cable TV and wifi was out of service. Communication with host was poor. Bedding was not optimal.",
    6: "Good WiFi, great location and centrally located. Shower was hot and had good pressure and there was enough space for two people for 6 days.",
    7: "Es tal cual las fotos, buena ubicacion, tranquilo y sin ruido. Es en un piso 15 por si le temen a las alturas.",
    8: ".",
    9: "Nice place in cool region. Very noisy environment and apartment is not very clean.",
    10: "location was great, wifi was spotty. But overall not a bad place.",
}

# Bắt đầu lời giải


def analyze_error_patterns(
    sai_ids: list, reviews: dict, predictions: dict, gold: dict
) -> pd.DataFrame:
    """Phân tích mẫu lỗi tự động dựa trên dấu hiệu cú pháp và liên từ tương phản.

    Tham số sai_ids: Danh sách mã định danh sai.
    Tham số reviews: Bảng tra cứu văn bản gốc.
    Tham số predictions: Nhãn mô hình gán.
    Tham số gold: Nhãn chuẩn tham chiếu.
    """
    ket_qua = []
    for rid in sai_ids:
        text_lower = reviews[rid].lower()
        if "not a bad" in text_lower or "not bad" in text_lower:
            loai = "Hiểu sai phủ định ngữ dụng (Litotes)"
        elif (
            any(kw in text_lower for kw in ["ruidosa", "noisy"])
            and predictions[rid] == "positive"
        ):
            loai = "Bỏ sót khía cạnh tiếng ồn do thiên lệch từ ngữ tích cực"
        else:
            loai = "Xung đột trọng số giữa các khía cạnh khen và chê"
        ket_qua.append(
            {
                "id": rid,
                "gold": gold[rid]["sentiment"],
                "llm": predictions[rid],
                "mau_ngu_nghia": loai,
            }
        )
    return pd.DataFrame(ket_qua)


df_mau_loi = analyze_error_patterns(kq_do_luong["sai"], REVIEWS, tap_du_doan, GOLD)
print(
    f"Cách 2: Phân tích mẫu ngữ nghĩa tự động:\n{df_mau_loi[['id', 'mau_ngu_nghia']].to_string(index=False)}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Các từ khóa có thể gợi ý một loại lỗi để người đọc xem lại, nhưng không tự phân loại ngữ nghĩa đầy đủ. Bảng đối chiếu giữ văn bản, nhãn dự đoán, nhãn tay và ghi chú làm bằng chứng. Khi sửa hướng dẫn gán nhãn, kiểm lại trên dữ liệu khác thay vì chỉ tối ưu cho vài câu đã thấy.

#### Kết quả cách 2

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 2: Phân tích mẫu ngữ nghĩa tự động: |
| 2 |  id                                           mau_ngu_nghia |
| 3 |   4 Bỏ sót khía cạnh tiếng ồn do thiên lệch từ ngữ tích cực |
| 4 |   9        Xung đột trọng số giữa các khía cạnh khen và chê |
| 5 |  10                    Hiểu sai phủ định ngữ dụng (Litotes) |
#### So sánh cách dùng

Cách 1 thích hợp để đọc và giải thích từng trường hợp sai theo ngữ cảnh. Cách 2 dùng dấu hiệu từ khóa để chọn các câu cần xem lại. Kết quả sàng lọc này hỗ trợ việc đọc, không tự thay thế đánh giá ý nghĩa của câu.

:::

---

<span id="data-lab-11-07"></span>
### Bài 7: Thiết lập quy tắc hậu kiểm tự động phát hiện mâu thuẫn nội tại

::: exercise
Xây dựng hàm hậu kiểm tự động kiểm tra tính nhất quán logic giữa nhãn cảm xúc tổng thể và các danh sách khía cạnh chi tiết, gắn cờ các bản ghi tự mâu thuẫn mà không cần sử dụng nhãn tay đối chứng.

Yêu cầu kỹ thuật:
- Đầu vào: Từ điển `outputs` có dạng `{id: {"sentiment": str, "aspects_positive": list, "aspects_negative": list}}` (ví dụ từ phương thức `model_dump()` của các đối tượng hợp lệ).
- Thao tác: Kiểm tra quy tắc mâu thuẫn nội tại:
  1. Nếu `sentiment == "positive"` nhưng danh sách `aspects_negative` không rỗng: Vi phạm mâu thuẫn.
  2. Nếu `sentiment == "negative"` nhưng danh sách `aspects_positive` không rỗng: Vi phạm mâu thuẫn.
  3. Nếu `sentiment == "mixed"`: Không bao giờ vi phạm quy tắc này.
- Đầu ra: Trả về danh sách (`list`) chứa các `id` bị gắn cờ mâu thuẫn, giữ đúng thứ tự xuất hiện của từ điển ban đầu.
- Phân tích kỹ thuật: Đối chiếu danh sách các ID bị gắn cờ với các ca sai lệch thực tế ở Bài 5, làm rõ ưu điểm và giới hạn của quy tắc hậu kiểm tự động.
:::

::: solution
#### Cách 1: Kiểm tra cấu trúc rẽ nhánh điều kiện tuần tự

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


ket_qua_kiem_dinh = validate_outputs(LLM_OUT)

tap_dau_ra_dump = {
    rid: obj.model_dump() for rid, obj in ket_qua_kiem_dinh["hop_le"].items()
}

# Bắt đầu lời giải


def contradictions(outputs: dict) -> list:
    """Phát hiện các bản ghi tự mâu thuẫn giữa nhãn cảm xúc và danh sách khía cạnh.

    Tham số outputs: Từ điển các đối tượng thông tin đánh giá đã xuất dữ liệu.
    """
    danh_sach_vi_pham = []
    for rid, data in outputs.items():
        sentiment = data.get("sentiment")
        pos_aspects = data.get("aspects_positive", [])
        neg_aspects = data.get("aspects_negative", [])

        if sentiment == "positive" and len(neg_aspects) > 0:
            danh_sach_vi_pham.append(rid)
        elif sentiment == "negative" and len(pos_aspects) > 0:
            danh_sach_vi_pham.append(rid)

    return danh_sach_vi_pham


tap_dau_ra_dump = {
    rid: obj.model_dump() for rid, obj in ket_qua_kiem_dinh["hop_le"].items()
}
ds_mau_thuan = contradictions(tap_dau_ra_dump)
print(
    f"Cách 1: Quy tắc hậu kiểm phát hiện {len(ds_mau_thuan)} bản ghi mâu thuẫn: {ds_mau_thuan}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Kiểm những cặp nhãn có vẻ mâu thuẫn theo quy tắc đã định, chẳng hạn cảm xúc tích cực đi cùng khía cạnh chê. Danh sách ID gắn cờ là hàng đợi đọc lại, không phải toàn bộ các lỗi. Một câu có cảm xúc hỗn hợp hoặc nhận xét nhiều mặt có thể làm quy tắc đơn giản báo nhầm.

#### Kết quả cách 1

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 1: Quy tắc hậu kiểm phát hiện 2 bản ghi mâu thuẫn: [9, 10] |

#### Cách 2: Biểu thức kiểm định logic hàm mở rộng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


ket_qua_kiem_dinh = validate_outputs(LLM_OUT)

tap_dau_ra_dump = {
    rid: obj.model_dump() for rid, obj in ket_qua_kiem_dinh["hop_le"].items()
}


def contradictions(outputs: dict) -> list:
    """Phát hiện các bản ghi tự mâu thuẫn giữa nhãn cảm xúc và danh sách khía cạnh.

    Tham số outputs: Từ điển các đối tượng thông tin đánh giá đã xuất dữ liệu.
    """
    danh_sach_vi_pham = []
    for rid, data in outputs.items():
        sentiment = data.get("sentiment")
        pos_aspects = data.get("aspects_positive", [])
        neg_aspects = data.get("aspects_negative", [])

        if sentiment == "positive" and len(neg_aspects) > 0:
            danh_sach_vi_pham.append(rid)
        elif sentiment == "negative" and len(pos_aspects) > 0:
            danh_sach_vi_pham.append(rid)

    return danh_sach_vi_pham


ds_mau_thuan = contradictions(tap_dau_ra_dump)

# Bắt đầu lời giải


def is_contradictory_record(record: dict) -> bool:
    """Xác định một bản ghi đơn lẻ có vi phạm tính nhất quán logic hay không."""
    sentiment = record.get("sentiment")
    if sentiment == "positive" and bool(record.get("aspects_negative")):
        return True
    if sentiment == "negative" and bool(record.get("aspects_positive")):
        return True
    return False


def contradictions_functional(outputs: dict) -> list:
    """Lọc các ID vi phạm quy tắc hậu kiểm bằng hàm vị từ logic.

    Tham số outputs: Từ điển dữ liệu đầu ra cần thẩm định.
    """
    return [rid for rid, rec in outputs.items() if is_contradictory_record(rec)]


ds_mau_thuan_fn = contradictions_functional(tap_dau_ra_dump)
print(
    f"Cách 2: Xác nhận danh sách mâu thuẫn trùng khớp: {ds_mau_thuan == ds_mau_thuan_fn}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Tách hàm kiểm từng phản hồi khỏi thao tác lọc cả đợt giúp dùng lại cùng điều kiện. Quy tắc hậu kiểm không thay thế nhãn tham chiếu. Cần đo cả trường hợp bị gắn cờ đúng, gắn cờ nhầm và lỗi không bị gắn cờ nếu muốn đánh giá chất lượng của chính bộ kiểm.

#### Kết quả cách 2

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 2: Xác nhận danh sách mâu thuẫn trùng khớp: True |
#### So sánh cách dùng

Bạn nên chọn Cách 1 khi chỉ cần kiểm tra vài cặp mâu thuẫn đơn giản để đưa vào danh sách xem xét lại thủ công. Cách 2 phù hợp khi có bộ quy tắc phức tạp cần đóng gói thành hàm kiểm định riêng biệt để dễ bảo trì và mở rộng.

:::

---

<span id="data-lab-11-08"></span>
### Bài 8: Đối chiếu phản hồi mô hình thực nghiệm mở rộng với bộ mô phỏng

::: exercise
Thiết lập quy trình đánh giá toàn diện một bộ phản hồi mô hình mới (`LLM_RUN_2`) đã được tinh chỉnh lời nhắc nhằm khắc phục lỗi cấu trúc và ngữ nghĩa, đối chiếu các chỉ số chất lượng giữa hai đợt chạy mà không cần sử dụng khóa kết nối API thực tế.

Yêu cầu kỹ thuật:
- Đầu vào: Bộ phản hồi thứ hai `LLM_RUN_2` gồm 10 bản ghi JSON mô phỏng, tập nhãn tay `GOLD` và bộ phản hồi ban đầu `LLM_OUT`.
- Thao tác:
  1. Thẩm định tính hợp lệ của lược đồ trên toàn bộ 10 bản ghi của `LLM_RUN_2`.
  2. Đo lường độ chính xác phân loại cảm xúc so với `GOLD` trên cả tập hợp lệ và trên toàn bộ tập dữ liệu.
  3. Kiểm tra xem ca phủ định tại ID 10 ("not a bad place") có được phân loại chính xác hay không.
  4. Chạy quy tắc hậu kiểm tự động để xác nhận trạng thái mâu thuẫn nội tại.
- Đầu ra: Trả về từ điển báo cáo tổng hợp hoặc bảng `pd.DataFrame` đối chiếu các chỉ số giữa hai đợt chạy.
- Phân tích kỹ thuật: Nêu rõ ý nghĩa của việc lưu vết phản hồi thô (raw output trace) và quy trình kiểm thử hồi quy (regression testing) khi nâng cấp mô hình hoặc sửa đổi lời nhắc.
:::

::: solution
#### Cách 1: Thực thi tuần tự các hàm thẩm định và so sánh kết quả trực tiếp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}

GOLD = {
    1: {"sentiment": "mixed", "language": "en"},
    2: {"sentiment": "negative", "language": "en"},
    3: {"sentiment": "positive", "language": "es"},
    4: {"sentiment": "mixed", "language": "es"},
    5: {"sentiment": "negative", "language": "en"},
    6: {"sentiment": "positive", "language": "en"},
    7: {"sentiment": "positive", "language": "es"},
    8: {"sentiment": "mixed", "language": "und"},
    9: {"sentiment": "mixed", "language": "en"},
    10: {"sentiment": "mixed", "language": "en"},
}


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


def sentiment_accuracy(du_doan: dict, gold: dict) -> dict:
    """Tính độ chính xác của nhãn cảm xúc so với nhãn tay chuẩn.

    Tham số du_doan: Từ điển nhãn cảm xúc dự đoán theo từng ID.
    Tham số gold: Từ điển nhãn tay chuẩn của chuyên viên đánh giá.
    """
    so_dung = 0
    sai = []
    for rid, nhan_du_doan in du_doan.items():
        nhan_chuan = gold[rid]["sentiment"]
        if nhan_du_doan == nhan_chuan:
            so_dung += 1
        else:
            sai.append(rid)
    do_chinh_xac = so_dung / len(du_doan) if du_doan else 0.0
    return {"so_dung": so_dung, "acc": float(do_chinh_xac), "sai": sai}


def contradictions(outputs: dict) -> list:
    """Phát hiện các bản ghi tự mâu thuẫn giữa nhãn cảm xúc và danh sách khía cạnh.

    Tham số outputs: Từ điển các đối tượng thông tin đánh giá đã xuất dữ liệu.
    """
    danh_sach_vi_pham = []
    for rid, data in outputs.items():
        sentiment = data.get("sentiment")
        pos_aspects = data.get("aspects_positive", [])
        neg_aspects = data.get("aspects_negative", [])

        if sentiment == "positive" and len(neg_aspects) > 0:
            danh_sach_vi_pham.append(rid)
        elif sentiment == "negative" and len(pos_aspects) > 0:
            danh_sach_vi_pham.append(rid)

    return danh_sach_vi_pham


# Bắt đầu lời giải

LLM_RUN_2 = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": [], "aspects_negative": ["amenities", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": ["noise"], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": [], "aspects_negative": ["amenities", "host"], "language": "en"}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}


def evaluate_llm_run(raw_data: dict, gold_data: dict) -> dict:
    """Đánh giá toàn diện một đợt chạy của mô hình ngôn ngữ lớn.

    Tham số raw_data: Tập hợp chuỗi JSON thô do mô hình trả về.
    Tham số gold_data: Tập nhãn tay chuẩn.
    """
    kiem_dinh = validate_outputs(raw_data)
    hop_le = kiem_dinh["hop_le"]
    loi_schema = kiem_dinh["loi_schema"]

    du_doan = {rid: obj.sentiment for rid, obj in hop_le.items()}
    ket_qua_acc = (
        sentiment_accuracy(du_doan, gold_data)
        if du_doan
        else {"so_dung": 0, "acc": 0.0, "sai": []}
    )

    dump_data = {rid: obj.model_dump() for rid, obj in hop_le.items()}
    ds_mau_thuan = contradictions(dump_data)

    acc_toan_bo = ket_qua_acc["so_dung"] / len(raw_data) if raw_data else 0.0

    return {
        "tong_so": len(raw_data),
        "hop_le_count": len(hop_le),
        "loi_schema_count": len(loi_schema),
        "ty_le_hop_le": len(hop_le) / len(raw_data) if raw_data else 0.0,
        "acc_hop_le": ket_qua_acc["acc"],
        "acc_toan_bo": acc_toan_bo,
        "sai_ids": ket_qua_acc["sai"],
        "mau_thuan_ids": ds_mau_thuan,
        "id_10_status": (
            "Chính xác"
            if 10 in hop_le and hop_le[10].sentiment == gold_data[10]["sentiment"]
            else "Sai"
        ),
    }


bc_run_1 = evaluate_llm_run(LLM_OUT, GOLD)
bc_run_2 = evaluate_llm_run(LLM_RUN_2, GOLD)
print(
    f"Cách 1: Run 1 Acc (Hợp lệ) = {bc_run_1['acc_hop_le']:.1%}, Run 2 Acc (Hợp lệ) = {bc_run_2['acc_hop_le']:.1%}"
)

# Kết thúc lời giải
```

#### Giải thích cách 1

Đưa cùng tập nhãn tay vào mỗi lần đánh giá để so sánh các tỷ lệ trên cùng mẫu. Giữ tỷ lệ hợp lệ, độ khớp trong tập hợp lệ và độ khớp toàn mẫu thành các trường riêng. Kết quả của đợt phản hồi mô phỏng tốt hơn không chứng minh một lời nhắc mới sẽ luôn tốt hơn trên dữ liệu thực.

#### Kết quả cách 1

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 1: Run 1 Acc (Hợp lệ) = 62.5%, Run 2 Acc (Hợp lệ) = 100.0% |

#### Cách 2: Đóng gói đường ống đánh giá và xuất báo cáo so sánh đa tiêu chí

```python
# Dữ liệu mẫu và các hàm hỗ trợ

from pydantic import BaseModel, ValidationError, ConfigDict

from typing import Literal

import pandas as pd

Aspect = Literal["location", "cleanliness", "host", "noise", "amenities", "value"]


class ReviewInfo(BaseModel):
    """Lược đồ dữ liệu trích xuất thông tin đánh giá chỗ ở.

    Trường sentiment: Nhãn cảm xúc tổng thể gồm positive, mixed, hoặc negative.
    Trường aspects_positive: Danh sách khía cạnh tích cực được đề cập.
    Trường aspects_negative: Danh sách khía cạnh tiêu cực được đề cập.
    Trường language: Mã ngôn ngữ của bài đánh giá.
    """

    sentiment: Literal["positive", "mixed", "negative"]
    aspects_positive: list[Aspect]
    aspects_negative: list[Aspect]
    language: str


LLM_OUT = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": ["host"], "aspects_negative": ["photos", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities", "host"]}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "negative", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}

GOLD = {
    1: {"sentiment": "mixed", "language": "en"},
    2: {"sentiment": "negative", "language": "en"},
    3: {"sentiment": "positive", "language": "es"},
    4: {"sentiment": "mixed", "language": "es"},
    5: {"sentiment": "negative", "language": "en"},
    6: {"sentiment": "positive", "language": "en"},
    7: {"sentiment": "positive", "language": "es"},
    8: {"sentiment": "mixed", "language": "und"},
    9: {"sentiment": "mixed", "language": "en"},
    10: {"sentiment": "mixed", "language": "en"},
}


def validate_outputs(llm_out: dict) -> dict:
    """Kiểm tra hợp lệ hàng loạt các phản hồi JSON bằng lược đồ ReviewInfo.

    Tham số llm_out: Từ điển chứa cặp khóa id và giá trị chuỗi JSON thô.
    """
    hop_le = {}
    loi_schema = []
    for rid, raw_text in llm_out.items():
        try:
            doi_tuong = ReviewInfo.model_validate_json(raw_text)
            hop_le[rid] = doi_tuong
        except (ValidationError, Exception):
            loi_schema.append(rid)
    return {"hop_le": hop_le, "loi_schema": loi_schema}


def sentiment_accuracy(du_doan: dict, gold: dict) -> dict:
    """Tính độ chính xác của nhãn cảm xúc so với nhãn tay chuẩn.

    Tham số du_doan: Từ điển nhãn cảm xúc dự đoán theo từng ID.
    Tham số gold: Từ điển nhãn tay chuẩn của chuyên viên đánh giá.
    """
    so_dung = 0
    sai = []
    for rid, nhan_du_doan in du_doan.items():
        nhan_chuan = gold[rid]["sentiment"]
        if nhan_du_doan == nhan_chuan:
            so_dung += 1
        else:
            sai.append(rid)
    do_chinh_xac = so_dung / len(du_doan) if du_doan else 0.0
    return {"so_dung": so_dung, "acc": float(do_chinh_xac), "sai": sai}


def contradictions(outputs: dict) -> list:
    """Phát hiện các bản ghi tự mâu thuẫn giữa nhãn cảm xúc và danh sách khía cạnh.

    Tham số outputs: Từ điển các đối tượng thông tin đánh giá đã xuất dữ liệu.
    """
    danh_sach_vi_pham = []
    for rid, data in outputs.items():
        sentiment = data.get("sentiment")
        pos_aspects = data.get("aspects_positive", [])
        neg_aspects = data.get("aspects_negative", [])

        if sentiment == "positive" and len(neg_aspects) > 0:
            danh_sach_vi_pham.append(rid)
        elif sentiment == "negative" and len(pos_aspects) > 0:
            danh_sach_vi_pham.append(rid)

    return danh_sach_vi_pham


LLM_RUN_2 = {
    1: '{"sentiment": "mixed", "aspects_positive": ["cleanliness", "location"], "aspects_negative": ["noise"], "language": "en"}',
    2: '{"sentiment": "negative", "aspects_positive": [], "aspects_negative": ["amenities", "cleanliness"], "language": "en"}',
    3: '{"sentiment": "positive", "aspects_positive": ["host", "location"], "aspects_negative": [], "language": "es"}',
    4: '{"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": ["noise"], "language": "es"}',
    5: '{"sentiment": "negative", "aspects_positive": [], "aspects_negative": ["amenities", "host"], "language": "en"}',
    6: '{"sentiment": "positive", "aspects_positive": ["amenities", "location"], "aspects_negative": [], "language": "en"}',
    7: '{"sentiment": "positive", "aspects_positive": ["location"], "aspects_negative": [], "language": "es"}',
    8: '{"sentiment": "mixed", "aspects_positive": [], "aspects_negative": [], "language": "und"}',
    9: '{"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": ["noise", "cleanliness"], "language": "en"}',
    10: '{"sentiment": "mixed", "aspects_positive": ["location"], "aspects_negative": ["amenities"], "language": "en"}',
}


def evaluate_llm_run(raw_data: dict, gold_data: dict) -> dict:
    """Đánh giá toàn diện một đợt chạy của mô hình ngôn ngữ lớn.

    Tham số raw_data: Tập hợp chuỗi JSON thô do mô hình trả về.
    Tham số gold_data: Tập nhãn tay chuẩn.
    """
    kiem_dinh = validate_outputs(raw_data)
    hop_le = kiem_dinh["hop_le"]
    loi_schema = kiem_dinh["loi_schema"]

    du_doan = {rid: obj.sentiment for rid, obj in hop_le.items()}
    ket_qua_acc = (
        sentiment_accuracy(du_doan, gold_data)
        if du_doan
        else {"so_dung": 0, "acc": 0.0, "sai": []}
    )

    dump_data = {rid: obj.model_dump() for rid, obj in hop_le.items()}
    ds_mau_thuan = contradictions(dump_data)

    acc_toan_bo = ket_qua_acc["so_dung"] / len(raw_data) if raw_data else 0.0

    return {
        "tong_so": len(raw_data),
        "hop_le_count": len(hop_le),
        "loi_schema_count": len(loi_schema),
        "ty_le_hop_le": len(hop_le) / len(raw_data) if raw_data else 0.0,
        "acc_hop_le": ket_qua_acc["acc"],
        "acc_toan_bo": acc_toan_bo,
        "sai_ids": ket_qua_acc["sai"],
        "mau_thuan_ids": ds_mau_thuan,
        "id_10_status": (
            "Chính xác"
            if 10 in hop_le and hop_le[10].sentiment == gold_data[10]["sentiment"]
            else "Sai"
        ),
    }


# Bắt đầu lời giải


def evaluate_llm_pipeline(run_dict: dict, gold_data: dict) -> pd.DataFrame:
    """Tạo bảng so sánh đối chuẩn hiệu năng giữa nhiều đợt chạy mô hình khác nhau.

    Tham số run_dict: Từ điển chứa tên đợt chạy và bộ phản hồi thô tương ứng.
    Tham số gold_data: Tập nhãn tay chuẩn đối chiếu.
    """
    hang_bao_cao = []
    for ten_run, raw_dict in run_dict.items():
        so_lieu = evaluate_llm_run(raw_dict, gold_data)
        hang_bao_cao.append(
            {
                "Dot_chay": ten_run,
                "Tong_mau": so_lieu["tong_so"],
                "Loi_schema": so_lieu["loi_schema_count"],
                "Ty_le_schema": f"{so_lieu['ty_le_hop_le']:.1%}",
                "Acc_hop_le": f"{so_lieu['acc_hop_le']:.1%}",
                "Acc_toan_bo": f"{so_lieu['acc_toan_bo']:.1%}",
                "So_mau_thuan": len(so_lieu["mau_thuan_ids"]),
                "Xu_ly_ID_10": so_lieu["id_10_status"],
            }
        )
    return pd.DataFrame(hang_bao_cao)


df_so_sanh_runs = evaluate_llm_pipeline(
    {"Run 1 (Mô phỏng gốc)": LLM_OUT, "Run 2 (Cải tiến lời nhắc)": LLM_RUN_2}, GOLD
)
print(
    f"Cách 2: Bảng đối chuẩn kết quả giữa hai đợt chạy:\n{df_so_sanh_runs.to_string(index=False)}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

Gom các phép kiểm thành một hàm báo cáo giúp chạy lại cùng tiêu chí trên nhiều bộ phản hồi đã lưu. So sánh theo ID và giữ nguyên đầu ra thô để có thể kiểm lại. Chênh lệch hai tỷ lệ phần trăm được trình bày bằng điểm phần trăm, còn mức tăng tương đối dùng một phép chia khác.

#### Kết quả cách 2

| Dòng output | Nội dung |
| --- | --- |
| 1 | Cách 2: Bảng đối chuẩn kết quả giữa hai đợt chạy: |
| 2 |                  Dot_chay  Tong_mau  Loi_schema Ty_le_schema Acc_hop_le Acc_toan_bo  So_mau_thuan Xu_ly_ID_10 |
| 3 |      Run 1 (Mô phỏng gốc)        10           2        80.0%      62.5%       50.0%             2         Sai |
| 4 | Run 2 (Cải tiến lời nhắc)        10           0       100.0%     100.0%      100.0%             0   Chính xác |
#### So sánh cách dùng

Cách 1 mở các phép so sánh trên hai đợt phản hồi mô phỏng để thấy rõ từng mẫu số. Cách 2 đóng gói cùng tiêu chí vào hàm báo cáo. Chênh lệch trong ví dụ chưa chứng minh một lời nhắc mới tốt hơn trên dữ liệu thực tế.

:::

---

## Tài liệu tham khảo

- Inside Airbnb. Snapshot dữ liệu thị trường chỗ ở thành phố Santiago ngày 29/06/2026.
- Pydantic Documentation. Data validation and settings management using Python type annotations.
- Google DeepMind. Gemini API structured outputs with JSON Schema documentation.
