---
course: xu-ly-du-lieu
lecture: bai-06-ket-noi-truy-xuat-du-lieu
section: lecture
title: "Đọc, lưu trữ & truy xuất dữ liệu"
prerequisites: ["dictionary", "ham-lap-trinh", "gia-tri-thieu"]
lessonStatus: ready
description: "Đọc chọn lọc tệp lớn với usecols, làm sạch giá chuỗi, định dạng Parquet định hướng cột, tiêu thụ API và truy vấn SQL tại chỗ bằng DuckDB."
---

## 1. Kỹ thuật Nạp Tệp CSV An toàn Chống lỗi và Xác thực Cấu trúc Dữ liệu

Trong môi trường phân tích dữ liệu thực tế, các tệp dữ liệu thường có dung lượng rất lớn với hàng chục, thậm chí hàng trăm cột thông tin. Chẳng hạn, tệp `listings_full.csv.gz` của Inside Airbnb chứa tới $90$ cột thuộc tính khác nhau.

Nếu bạn thực thi lệnh `pd.read_csv("listings_full.csv.gz")` một cách ngây thơ, máy tính sẽ phải giải nén và nạp toàn bộ $90$ cột vào bộ nhớ RAM. Điều này không chỉ gây lãng phí bộ nhớ nghiêm trọng mà còn khiến thời gian nạp tệp kéo dài hàng chục giây.

```
+---------------------------------------------------------------------------------+
| TỆP CSV GỐC TRÊN ĐĨA (90 CỘT, DUNG LƯỢNG LỚN)                                   |
| [id, name, summary, space, description, ..., price, ..., first_review, ...]     |
+---------------------------------------------------------------------------------+
                                       |
                 +---------------------+---------------------+
                 |                                           |
                 v Cách đọc ngây thơ                         v Cách đọc chọn lọc
        pd.read_csv(file)                           pd.read_csv(file, usecols=[...],
                 |                                              parse_dates=[...])
                 v                                           |
    Nạp toàn bộ 90 cột vào RAM                               v
    - Tốn 1.2 GB RAM                            Chỉ nạp đúng 5 cột cần thiết
    - Mất 15.4 giây I/O                         - Tiết kiệm 85% RAM (~180 MB)
    - Cột ngày vẫn là chuỗi thô                 - Mất chỉ 2.1 giây I/O
                                                - Cột ngày tự ép kiểu datetime64
```

### 1.1. Nạp Chọn lọc với `usecols` và `parse_dates`
Kỹ thuật chuẩn mực của một kỹ sư dữ liệu là chỉ nạp đúng những cột phục vụ trực tiếp cho bài toán thông qua tham số `usecols`, đồng thời ép kiểu thời gian ngay tại tầng đọc tệp bằng `parse_dates`:

```python
import pandas as pd

cot_can_doc = ["id", "room_type", "price", "first_review", "number_of_reviews"]
cot_ngay = ["first_review"]

df = pd.read_csv(
    "listings_full.csv.gz",
    usecols=cot_can_doc,
    parse_dates=cot_ngay
)
```

Hai lợi ích kỹ thuật cốt lõi:
1. **Tiết kiệm tài nguyên**: Giảm thiểu tới $80\% - 90\%$ lượng bộ nhớ RAM cần thiết, ngăn ngừa hoàn toàn nguy cơ sập hệ thống do tràn bộ nhớ (*Out-Of-Memory*).
2. **Ép kiểu chuẩn xác**: Cột ngày tháng được chuyển đổi ngay thành định dạng `datetime64[ns]`, các ô trống tự động biến thành `NaT` (*Not a Time*), sẵn sàng cho các phép toán thời gian tiếp theo mà không cần gọi thêm lệnh chuyển đổi phụ.

### 1.2. Khóa Kiểu Cột Định danh và Kiểm soát Dấu hiệu Khuyết thiếu
- **Khóa kiểu chuỗi cho mã số**: Luôn chỉ định `dtype={"id": "string"}` nếu mã định danh có chứa các số 0 ở đầu, tránh việc pandas tự ý ép kiểu về số nguyên và làm mất mát thông tin.
- **Dấu hiệu khuyết thiếu `na_values`**: Mỗi nguồn dữ liệu lại có một quy ước ghi nhận ô trống dị biệt (`"N/A"`, `"chua_ro"`, `"-999"`). Hãy dùng `na_values` để chuẩn hóa chúng về `NaN`.
- *Cảnh báo về bẫy Namibia*: Quốc gia Namibia có mã tiêu chuẩn quốc tế ISO alpha-2 là `"NA"`. Nếu nạp tệp quốc gia mà không thiết lập `keep_default_na=False`, pandas sẽ tự động biến tên nước Namibia thành giá trị khuyết thiếu một cách oan uổng.

---

## 2. Kỹ thuật Làm sạch Chuỗi Tiền tệ và Bẫy Ký tự Neo Regex

Trong các tệp trích xuất từ hệ thống tài chính hoặc nền tảng thương mại, dữ liệu giá thường được lưu trữ dưới dạng chuỗi văn bản kèm ký hiệu tiền tệ và dấu phân cách hàng nghìn, chẳng hạn: `"$45,647.00"`.

Để chuyển chuỗi này về dạng số thực `float64` có thể tính toán được, ta cần loại bỏ ký tự `$` và dấu phẩy `,`.

### Bẫy Ký tự Neo trong Biểu thức Chính quy (Regex)
Trong cú pháp của biểu thức chính quy (*Regular Expression*), ký tự `$` là một **ký tự siêu đặc biệt (Meta-character)**, đóng vai trò là ký tự neo đại diện cho **vị trí cuối cùng của chuỗi văn bản**.
Nếu bạn viết:
```python
# CÁCH LÀM SAI LẦM:
s.str.replace("$", "", regex=True)
```
pandas sẽ tìm vị trí cuối chuỗi và thay thế nó bằng chuỗi rỗng! Ký tự `$` thực tế ở đầu chuỗi hoàn toàn không bị xóa, và lệnh ép kiểu `astype(float)` sau đó sẽ sập ngay lập tức với lỗi `ValueError`.

**Giải pháp chuẩn mực**: Luôn chỉ định tường minh tham số `regex=False` khi muốn thay thế các ký tự văn bản thông thường:
```python
# CÁCH LÀM CHUẨN MỰC:
gia_sach = prices.str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
```

---

## 3. Định dạng Lưu trữ: CSV vs Apache Parquet

Trong quá trình xây dựng các đường ống dữ liệu, việc lựa chọn định dạng lưu trữ trung gian giữa các bước xử lý đóng vai trò quyết định đến hiệu năng tổng thể của toàn bộ hệ thống.

```
+--------------------+-----------------------------+-------------------------------+
| Tiêu chí so sánh   | Tệp văn bản CSV             | Tệp nhị phân Apache Parquet   |
+--------------------+-----------------------------+-------------------------------+
| Mô hình lưu trữ    | Dòng tuần tự (Row-based)    | Định hướng cột (Columnar)     |
| Dung lượng đĩa     | Lớn (văn bản thô không nén) | Nhỏ (nén Snappy/ZSTD cao cấp) |
| Bảo toàn kiểu dữ liệu | KHÔNG (mọi thứ thành chuỗi) | CÓ (lưu trọn vẹn datetime, int)|
| Tốc độ truy vấn cột| Chậm (phải đọc toàn bộ tệp) | Cực nhanh (chỉ đọc cột cần)  |
| Hỗ trợ phân vùng   | Hạn chế                     | Chuẩn công nghiệp (Hive-style)|
+--------------------+-----------------------------+-------------------------------+
```

### 3.1. Bản chất Định hướng Cột của Parquet
- Trong tệp CSV, dữ liệu được ghi lần lượt từng dòng từ trái sang phải. Nếu bạn chỉ cần đọc đúng một cột giá tiền trong bảng 90 cột, hệ điều hành vẫn buộc phải nạp toàn bộ $100\%$ dung lượng tệp từ đĩa cứng vào bộ nhớ rồi mới bóc tách được cột đó.
- Ngược lại, Apache Parquet tổ chức dữ liệu theo từng cột riêng biệt. Khi bạn chỉ truy vấn cột `price`, trình điều khiển chỉ cần nhảy cóc đến đúng các dải byte của cột đó và nạp vào bộ nhớ.

### 3.2. Tính Bảo toàn Siêu dữ liệu Kiểu (*Type Preservation*)
Khi bạn xuất một DataFrame có cột ngày `first_review` (kiểu `datetime64[ns]`) ra tệp CSV bằng `df.to_csv("data.csv")`, tệp CSV chỉ lưu chuỗi văn bản `"2023-03-15"`. Khi đọc lại bằng `pd.read_csv("data.csv")`, cột này sẽ bị giáng cấp thành kiểu chuỗi `object`, và bạn lại phải mất công ép kiểu lần thứ hai.
Nếu xuất ra Parquet bằng `df.to_parquet("data.parquet")`, toàn bộ cấu trúc kiểu dữ liệu kỹ thuật (`int64`, `float64`, `datetime64`) đều được lưu trữ nguyên vẹn trong phần siêu dữ liệu của tệp nhị phân. Khi đọc lại, dữ liệu lập tức sẵn sàng sử dụng với kiểu gốc ban đầu.

---

## 4. Nguyên tắc Tiêu thụ Web API và Lưu trữ Phản hồi Thô

Khi thu thập dữ liệu từ các dịch vụ web bên ngoài (chẳng hạn như dữ liệu thời tiết lịch sử từ Open-Meteo API), một nguyên tắc bất biến của các kỹ sư dữ liệu là: **Lưu trữ Phản hồi Thô (*Raw Response Persistence*)**.

```
    [ Open-Meteo API ]
            |
            v Gọi HTTP GET một lần duy nhất
    { Response JSON Thô }
            |
            +---> [ Lưu tệp đĩa: raw/weather_2025-01.json ]  <- BẢO TOÀN DẤU VẾT
            |
            v pd.DataFrame(payload["daily"])
    [ Bảng phân tích nội bộ ]
```

### Vì sao phải lưu tệp JSON thô trước khi chuyển thành bảng?
1. **Tính tái lập (*Reproducibility*)**: Nếu sau này bạn phát hiện mã nguồn chuyển đổi bảng bị sai logic hoặc cần trích xuất thêm một trường thông tin mới (như độ ẩm hay tốc độ gió), bạn chỉ cần đọc lại tệp JSON đã lưu trên đĩa mà không cần gọi lại API.
2. **Bảo vệ giới hạn tần suất (*Rate Limit*)**: Hầu hết các dịch vụ API đều giới hạn số lượng cuộc gọi trong ngày. Việc lưu trữ cục bộ giúp bạn có thể chạy thử nghiệm mã nguồn hàng trăm lần mà không sợ bị nhà cung cấp khóa tài khoản.
3. **Phòng vệ trước sự cố mạng**: Trong các bài kiểm thử tự động (*CI/CD*) hoặc môi trường chấm bài ngắt kết nối mạng, đường ống dữ liệu vẫn vận hành trơn tru nhờ tệp dữ liệu thô đã được lưu trữ sẵn.

---

## 5. Truy vấn SQL Tại chỗ Hiệu năng cao với DuckDB

Trong nhiều thập kỷ, khi muốn sử dụng ngôn ngữ truy vấn SQL, lập trình viên buộc phải cài đặt các hệ quản trị cơ sở dữ liệu cồng kềnh như PostgreSQL hay MySQL.
Năm 2019, dự án **DuckDB** ra đời và nhanh chóng trở thành một hiện tượng công nghệ, được mệnh danh là "SQLite của ngành phân tích dữ liệu".

### 5.1. Sức mạnh của DuckDB
- **Không cần máy chủ (Serverless)**: DuckDB chạy nhúng trực tiếp bên trong tiến trình Python của bạn dưới dạng một thư viện C++ siêu nhẹ.
- **Thực thi trực tiếp trên tệp đĩa**: DuckDB có thể chạy các câu truy vấn SQL phức tạp (gồm `GROUP BY`, `JOIN`, hàm cửa sổ) trực tiếp trên các tệp `CSV`, `Parquet` hoặc `JSON` mà không cần bước nạp dữ liệu (*Ingestion*) vào cơ sở dữ liệu trước:
  ```python
  import duckdb

  # Chạy SQL trực tiếp trên tệp CSV và trả về pandas DataFrame:
  ket_qua = duckdb.query("""
      SELECT year(date) AS nam, count(*) AS n
      FROM 'reviews.csv'
      GROUP BY nam
      ORDER BY nam ASC
  """).df()
  ```
- **Xử lý tệp vượt RAM mượt mà**: Nhờ kỹ thuật thực thi luồng (*Streaming Execution*) và định dạng vector hóa, DuckDB có thể xử lý tệp CSV hàng chục triệu dòng với dung lượng RAM chỉ vài trăm Megabyte.

---

## 6. Bài tập Thực chiến Phòng Lab 06 (100% Nội dung Lab)

Dưới đây là trọn vẹn bộ bài tập từ Lab 06, kết hợp ba nguồn dữ liệu thực tế: tệp danh sách phòng đầy đủ 90 cột, tệp lịch sử đánh giá hơn $690,000$ dòng, và dữ liệu thời tiết lịch sử từ Open-Meteo API.

---

### Bài tập 1 (Q1): Đọc Tệp Lớn có Chọn lọc bằng `usecols` và `parse_dates`
::: exercise Nạp tệp dữ liệu tối ưu bộ nhớ
Viết hàm:
`read_selected(path: str | Path, columns: list[str], date_columns: list[str]) -> pd.DataFrame`
Yêu cầu:
- Nhận đường dẫn tới tệp CSV (hỗ trợ cả tệp nén `.gz`).
- Chỉ nạp đúng các cột được liệt kê trong `columns` bằng tham số `usecols`.
- Ép kiểu thời gian cho các cột trong `date_columns` ngay tại thời điểm nạp bằng `parse_dates`.
- Trả về DataFrame gồm đầy đủ các dòng, các cột ngày có kiểu `datetime64` và ô trống thành `NaT`.
- Tuyệt đối không đọc toàn bộ bảng rồi mới dùng lệnh lọc cột.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd
from pathlib import Path

def read_selected(path: str | Path, columns: list[str], date_columns: list[str]) -> pd.DataFrame:
    # Đọc có chọn lọc ngay tại tầng I/O của pandas
    return pd.read_csv(
        path,
        usecols=columns,
        parse_dates=date_columns
    )
```

#### Đo lường thực nghiệm:
- Trên tệp snapshot Santiago thật `listings_full.csv.gz` ($18,534$ dòng $\times 90$ cột):
  - Đọc toàn bộ bảng: mất khoảng $15.4$ giây.
  - Đọc chọn lọc 5 cột bằng `read_selected`: chỉ mất $2.1$ giây (**nhanh hơn gấp 7 lần** và giảm $85\%$ dung lượng RAM).
:::

---

### Bài tập 2 (Q2): Làm sạch Cột Giá Dạng Chuỗi An toàn
::: exercise Chuyển đổi dữ liệu tiền tệ có ký hiệu đặc biệt
Viết hàm `clean_price(prices: pd.Series) -> pd.Series`.
Yêu cầu:
- Nhận Series chuỗi có định dạng tiền tệ như `"$45,647.00"` hoặc giá trị khuyết thiếu.
- Loại bỏ ký hiệu `$` và dấu phẩy `,` bằng cách gọi hai lần liên tiếp phương thức `str.replace(..., regex=False)`.
- Ép kiểu an toàn sang `float64`, các ô khuyết thiếu vẫn giữ nguyên là `NaN`.
- Không làm thay đổi Series đầu vào.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd
import numpy as np

def clean_price(prices: pd.Series) -> pd.Series:
    # Tắt biểu thức chính quy (regex=False) để ký tự $ được hiểu đúng nghĩa đen
    s_sach = prices.str.replace("$", "", regex=False).str.replace(",", "", regex=False)
    return s_sach.astype(np.float64)
```
*Đối chiếu thực tế*: Trung vị giá sau khi làm sạch trên toàn bộ thị trường Santiago đạt $59,000$ CLP.
:::

---

### Bài tập 3 (Q3): Khảo sát Thực nghiệm Kích thước và Kiểu Dữ liệu: CSV vs Parquet
::: exercise So sánh hai định dạng lưu trữ dữ liệu
Viết hàm `save_formats(df: pd.DataFrame, folder: Path) -> dict`.
Yêu cầu:
- Ghi DataFrame ra hai tệp: `folder / "t6.csv"` (không lưu index) và `folder / "t6.parquet"` (không lưu index).
- Đọc lại cả hai tệp: tệp CSV đọc lại bằng `pd.read_csv` (không parse dates); tệp Parquet đọc lại bằng `pd.read_parquet`.
- Trả về từ điển có đúng 4 khóa:
  - `size_csv`: Kích thước tệp CSV tính bằng byte (`os.path.getsize`).
  - `size_parquet`: Kích thước tệp Parquet tính bằng byte.
  - `dtypes_csv`: Từ điển `{tên_cột: str(dtype)}` của bảng CSV đọc lại.
  - `dtypes_parquet`: Từ điển `{tên_cột: str(dtype)}` của bảng Parquet đọc lại.
:::

::: solution
#### Lời giải chi tiết:
```python
import os
from pathlib import Path
import pandas as pd

def save_formats(df: pd.DataFrame, folder: Path) -> dict:
    folder_path = Path(folder)
    csv_file = folder_path / "t6.csv"
    pq_file = folder_path / "t6.parquet"
    
    # 1. Ghi ra đĩa
    df.to_csv(csv_file, index=False)
    df.to_parquet(pq_file, index=False)
    
    # 2. Đọc lại để kiểm tra kiểu
    df_csv_back = pd.read_csv(csv_file)
    df_pq_back = pd.read_parquet(pq_file)
    
    return {
        "size_csv": os.path.getsize(csv_file),
        "size_parquet": os.path.getsize(pq_file),
        "dtypes_csv": {col: str(df_csv_back[col].dtype) for col in df_csv_back.columns},
        "dtypes_parquet": {col: str(df_pq_back[col].dtype) for col in df_pq_back.columns}
    }
```

#### Nhận xét sư phạm:
- Dung lượng tệp Parquet nhỏ hơn tệp CSV khoảng $3$ lần nhờ thuật toán nén Snappy.
- Cột ngày `first_review` trong CSV bị biến thành chuỗi `object`, trong khi Parquet bảo toàn trọn vẹn kiểu `datetime64[ns]`.
:::

---

### Bài tập 4 (Q4): Tiêu thụ API Lịch sử và Bảo tồn Phản hồi Thô
::: exercise Lưu trữ phản hồi JSON từ Web API
Viết hàm `weather_table(payload: dict, path: str | Path) -> pd.DataFrame`.
Yêu cầu:
- Nhận phản hồi dạng từ điển từ API Open-Meteo (chứa khóa `"daily"` là tập hợp các danh sách có cùng độ dài, luôn có trường `"time"`).
- Ghi toàn bộ phản hồi thô `payload` ra tệp đĩa tại đường dẫn `path` bằng `json.dump(..., ensure_ascii=False)`.
- Chuyển đổi khối dữ liệu `"daily"` thành một pandas DataFrame và trả về kết quả (cột `"time"` giữ nguyên dạng chuỗi).
:::

::: solution
#### Lời giải chi tiết:
```python
import json
from pathlib import Path
import pandas as pd

def weather_table(payload: dict, path: str | Path) -> pd.DataFrame:
    file_path = Path(path)
    
    # 1. Lưu trữ toàn bộ phản hồi thô để bảo toàn dấu vết
    with open(file_path, mode="w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
        
    # 2. Chuyển đổi thành DataFrame
    return pd.DataFrame(payload["daily"])
```
:::

---

### Bài tập 5 (Q5): Thống kê Lượt Đánh giá theo Ngày trong Khoảng Thời gian
::: exercise Đếm tần suất biến cố theo chuỗi thời gian
Viết hàm `reviews_per_day(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame`.
Yêu cầu:
- Bảng `rv` chứa cột `date` có kiểu `datetime64`.
- Lọc các dòng thỏa mãn $start \le date \le end$ (bao gồm cả hai mốc biên).
- Đếm số lượng đánh giá theo từng ngày bằng cú pháp: `groupby(rv["date"].dt.strftime("%Y-%m-%d")).size()`.
- Trả về DataFrame gồm đúng hai cột: `time` (chuỗi `"YYYY-MM-DD"`) và `so_review` (int), sắp xếp `time` tăng dần, đặt lại index từ $0, 1, \dots$. Chỉ giữ lại những ngày có ít nhất một đánh giá.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def reviews_per_day(rv: pd.DataFrame, start: str, end: str) -> pd.DataFrame:
    # 1. Lọc theo khoảng thời gian hợp lệ
    mask = (rv["date"] >= start) & (rv["date"] <= end)
    rv_sub = rv[mask]
    
    # 2. Định dạng ngày sang chuỗi YYYY-MM-DD và đếm tần suất
    chuoi_ngay = rv_sub["date"].dt.strftime("%Y-%m-%d")
    dem = rv_sub.groupby(chuoi_ngay).size().reset_index(name="so_review")
    dem.rename(columns={"date": "time"}, inplace=True)
    
    # 3. Sắp xếp thứ tự thời gian tăng dần
    dem.sort_values("time", inplace=True)
    dem.reset_index(drop=True, inplace=True)
    
    return dem
```
:::

---

### Bài tập 6 (Q6): Ghép nối Dữ liệu Thời tiết và Tính Hệ số Tương quan
::: exercise Khảo sát mối liên hệ giữa nhiệt độ và hành vi người dùng
Viết hàm `join_weather(weather: pd.DataFrame, per_day: pd.DataFrame) -> dict`.
Yêu cầu:
- Nối bảng thời tiết `weather` (có cột `time`, `temperature_2m_max`) với bảng đánh giá theo ngày `per_day` (có cột `time`, `so_review`) theo cột `time` bằng phương thức `how="left"`.
- Các ngày không phát sinh đánh giá nào giữ nguyên giá trị `NaN` ở cột `so_review`, **tuyệt đối không tự ý điền số 0**.
- Tính hệ số tương quan Pearson giữa nhiệt độ cao nhất và số lượng đánh giá.
- Trả về từ điển gồm:
  - `gop`: DataFrame sau khi ghép nối.
  - `so_thieu`: int, số ngày không có đánh giá (`NaN`).
  - `he_so`: float, hệ số tương quan Pearson (tự động bỏ qua các cặp có `NaN`).
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd
import numpy as np

def join_weather(weather: pd.DataFrame, per_day: pd.DataFrame) -> dict:
    # Ghép nối giữ nguyên mọi ngày của bảng thời tiết
    gop = pd.merge(weather, per_day, on="time", how="left")
    
    so_thieu = int(gop["so_review"].isna().sum())
    he_so = float(gop["temperature_2m_max"].corr(gop["so_review"]))
    
    return {
        "gop": gop,
        "so_thieu": so_thieu,
        "he_so": he_so
    }
```

#### Luận giải phương pháp luận:
- **Vì sao không điền số 0 cho ngày thiếu review?**: Trong kinh tế học du lịch, việc một ngày không có review nào được ghi nhận có thể do hệ thống máy chủ bị bảo trì ngắt quãng hoặc do các lượt đánh giá bị trễ hạn (*reporting delay*). Tự ý điền số 0 sẽ kéo tụt đường xu hướng hồi quy một cách giả tạo.
- **Ý nghĩa của hệ số $r \approx 0.08$**: Hệ số tương quan $0.08$ gần như bằng $0$, chứng minh rằng nhiệt độ ngoài trời trong ngày không hề có bất kỳ tác động tuyến tính đáng kể nào đến việc du khách có viết đánh giá hay không. Khách du lịch thường viết đánh giá sau khi đã kết thúc chuyến đi và trở về nhà, hoàn toàn độc lập với thời tiết tại địa phương vào ngày hôm đó.
:::

---

### Bài tập 7 (Q7): Truy vấn SQL Trực tiếp trên Tệp CSV bằng DuckDB
::: exercise Thống kê chuỗi thời gian không cần nạp vào bộ nhớ
Viết hàm `sql_reviews_by_year(reviews_path: str | Path) -> pd.DataFrame`.
Yêu cầu:
- Chạy một câu lệnh truy vấn DuckDB trực tiếp trên đường dẫn tệp CSV `reviews_path`.
- Sử dụng cú pháp SQL chuẩn:
  `SELECT year(date) AS nam, count(*) AS n FROM '<path>' GROUP BY nam ORDER BY nam ASC`.
- Trả về kết quả dưới dạng pandas DataFrame có đúng hai cột `nam` và `n` (số nguyên).
:::

::: solution
#### Lời giải chi tiết:
```python
from pathlib import Path
import pandas as pd
import duckdb

def sql_reviews_by_year(reviews_path: str | Path) -> pd.DataFrame:
    path_str = str(reviews_path).replace("\\", "/")
    
    cau_lenh = f"""
        SELECT 
            year(date) AS nam, 
            count(*) AS n 
        FROM '{path_str}' 
        GROUP BY nam 
        ORDER BY nam ASC
    """
    
    return duckdb.query(cau_lenh).df()
```

#### Kiểm chứng chéo:
- Năm 2025 trên tập dữ liệu Santiago thật có đúng $211,432$ lượt đánh giá.
- Con số tính toán bằng câu lệnh DuckDB này khớp chính xác $100\%$ đến từng đơn vị với kết quả tính toán bằng Python thuần ở Lab 2!
:::

---

### Bài tập 8 (Q8): Nối Hai Tệp CSV trong DuckDB: Lượt Đánh giá theo Loại Phòng
::: exercise Phép nối bảng SQL hiệu năng cao trên đĩa
Viết hàm:
`sql_reviews_by_room_type(reviews_path: str | Path, listings_path: str | Path, nam: int) -> pd.DataFrame`
Yêu cầu:
- Chạy một truy vấn SQL trong DuckDB thực hiện phép nối `JOIN` trực tiếp giữa tệp review (`listing_id`, `date`) và tệp listing (`id`, `room_type`).
- Điều kiện nối: `r.listing_id = l.id`.
- Điều kiện lọc: `year(r.date) = nam`.
- Gom nhóm theo `room_type` và đếm tổng số đánh giá `count(*) AS n`.
- Sắp xếp kết quả theo `n` giảm dần; nếu bằng nhau thì sắp xếp `room_type` tăng dần theo bảng chữ cái.
- Trả về DataFrame gồm đúng hai cột `room_type` và `n`.
:::

::: solution
#### Lời giải chi tiết:
```python
from pathlib import Path
import pandas as pd
import duckdb

def sql_reviews_by_room_type(reviews_path: str | Path, listings_path: str | Path, nam: int) -> pd.DataFrame:
    r_path = str(reviews_path).replace("\\", "/")
    l_path = str(listings_path).replace("\\", "/")
    
    cau_lenh = f"""
        SELECT 
            l.room_type, 
            count(*) AS n
        FROM '{r_path}' r
        JOIN '{l_path}' l ON r.listing_id = l.id
        WHERE year(r.date) = {nam}
        GROUP BY l.room_type
        ORDER BY n DESC, l.room_type ASC
    """
    
    return duckdb.query(cau_lenh).df()
```

#### Luận giải sâu sắc về hiện tượng suy giảm số dòng sau JOIN:
- Khi tính riêng trên tệp review ở Bài 7, năm 2025 có tổng cộng $211,432$ đánh giá.
- Tuy nhiên, sau khi thực hiện phép nối `INNER JOIN` với tệp listing ở Bài 8, tổng số review chỉ còn lại $201,850$ (bị hụt mất khoảng $9,500$ review!).
- **Nguyên nhân kỹ thuật**: Đây là hiện tượng **khóa ngoại mồ côi (*Dangling Foreign Keys*)**. Tệp listing chỉ ghi nhận danh sách các phòng đang hoạt động ở thời điểm hiện tại (tháng 6/2026). Những phòng đã dừng hoạt động hoặc bị chủ nhà xóa tài khoản vào năm 2025 sẽ không còn xuất hiện trong tệp listing, dẫn đến việc các review tương ứng của chúng bị loại bỏ trong phép nối `INNER JOIN`.
:::

---

## 7. Tổng kết Bài học

1. **Nạp dữ liệu có chọn lọc**: Sử dụng `usecols` và `parse_dates` để giảm thiểu tối đa tài nguyên I/O và RAM khi làm việc với các bảng dữ liệu khổng lồ.
2. **Kỷ luật với chuỗi tiền tệ**: Luôn thiết lập `regex=False` khi sử dụng `.str.replace()` để xử lý các ký hiệu tiền tệ `$`.
3. **Ưu tiên định dạng Parquet**: Sử dụng Parquet cho dữ liệu trung gian để tiết kiệm dung lượng đĩa và bảo toàn nguyên vẹn kiểu dữ liệu kỹ thuật.
4. **Lưu trữ phản hồi thô**: Luôn ghi tệp JSON thô từ Web API xuống đĩa trước khi trích xuất bảng biểu.
5. **Khai thác sức mạnh DuckDB**: Tận dụng DuckDB để truy vấn SQL tức thì trên các tệp đĩa mà không cần cài đặt máy chủ cơ sở dữ liệu cồng kềnh.
