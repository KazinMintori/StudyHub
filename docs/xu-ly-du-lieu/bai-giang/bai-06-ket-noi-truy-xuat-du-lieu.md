---
course: xu-ly-du-lieu
lecture: bai-06-ket-noi-truy-xuat-du-lieu
section: lecture
title: "Đọc, lưu trữ & truy xuất dữ liệu"
prerequisites: ["dictionary","ham-lap-trinh","gia-tri-thieu"]
lessonStatus: ready
description: "Đọc CSV, JSON và SQL với kiểu dữ liệu rõ ràng; xử lý theo khối và kiểm tra dữ liệu từ API."
---

Một ngộ nhận dễ gặp khi mới tiếp cận khoa học dữ liệu là cho rằng dữ liệu luôn có sẵn dưới dạng các tệp CSV sạch sẽ nằm gọn trên máy tính cá nhân. Trong thế giới sản xuất thực tế, dữ liệu phân tán ở khắp mọi nơi: nằm trong các cơ sở dữ liệu quan hệ với hàng trăm triệu giao dịch, trong các luồng dữ liệu JSON phân cấp từ các dịch vụ web API, hoặc trong các kho lưu trữ dạng cột Parquet trên đám mây.

Nạp dữ liệu không đơn thuần là một thao tác đọc tệp kỹ thuật, mà là **cửa ải kiểm soát chất lượng đầu tiên** của toàn bộ quy trình. Nếu ta đọc sai kiểu dữ liệu ngay từ cổng vào, mọi mô hình phân tích hay thuật toán học máy ở các bước sau đều sẽ cho ra kết quả sai lệch.

Bài học này trang bị cho ta kỹ thuật nạp dữ liệu chuẩn mực và an toàn từ ba nguồn chủ lực: tệp văn bản CSV, tài liệu phân cấp JSON, và cơ sở dữ liệu quan hệ SQL. Đồng thời, ta sẽ làm chủ kỹ thuật xử lý tệp vượt dung lượng bộ nhớ RAM và nguyên tắc tiêu thụ API có trách nhiệm.

## 1. Đọc tệp CSV phòng thủ và kiểm định lược đồ

CSV là định dạng trao đổi đơn giản và phổ biến nhất, nhưng cũng là nơi phát sinh nhiều lỗi tiềm ẩn nhất. Vì tệp CSV không lưu thông tin kiểu dữ liệu, pandas phải tự suy đoán kiểu dựa trên các dòng đầu tiên. Quá trình suy đoán ngầm này rất dễ gây ra những sai lệch nghiêm trọng.

```python
import pandas as pd
from io import StringIO

text = "id,nhom,doanh_thu\n001,A,40\n002,A,60\n003,B,\n"
df = pd.read_csv(
    StringIO(text), dtype={"id": "string"}, na_values=["chua_co"]
)
print(df["id"].tolist())        # ['001', '002', '003']
print(df["doanh_thu"].isna().sum())  # 1
assert df["id"].is_unique
```

Ba kỹ thuật then chốt khi làm việc với CSV:

1. **Chủ động khóa kiểu định danh bằng `dtype`**: Cột `id` chứa các chuỗi `"001"`, `"002"`. Nếu không chỉ định `dtype={"id": "string"}`, pandas sẽ tự động ép về số nguyên $1, 2$ và làm mất vĩnh viễn các số 0 ở đầu.
2. **Kiểm soát dấu hiệu khuyết thiếu với `na_values`**: Mỗi hệ thống nguồn lại có một quy ước ghi nhận dữ liệu trống khác nhau: có nơi ghi là khoảng trắng, có nơi ghi `"chua_co"`, `"N/A"`, hoặc `"-999"`. Việc khai báo `na_values=["chua_co"]` giúp chuẩn hóa các quy ước dị biệt này về giá trị `NaN` duy nhất.
   Tuy nhiên, hãy hết sức cảnh giác với tham số mặc định: mã quốc gia của nước Namibia là `"NA"`. Nếu bạn đọc tệp dữ liệu quốc gia mà không tắt danh sách dấu hiệu thiếu mặc định (`keep_default_na=False`), toàn bộ dữ liệu của đất nước Namibia sẽ bị biến thành giá trị khuyết thiếu một cách oan uổng.
3. **Xác nhận tính bất biến ngay sau khi nạp**: Dòng lệnh `assert df["id"].is_unique` đóng vai trò một chiếc chốt an toàn. Nếu tệp dữ liệu bị trùng lặp khóa chính, chương trình sẽ dừng lại ngay lập tức thay vì để lỗi lan truyền sang các bước tính toán phía sau.

## 2. Kỹ thuật xử lý tệp vượt dung lượng RAM (Chunking)

Một bài toán thực tế thường gặp: máy tính của bạn chỉ có 16 GB bộ nhớ RAM, nhưng tệp CSV nhật ký giao dịch lại nặng tới 50 GB. Nếu bạn thực thi lệnh `pd.read_csv("nhat_ky.csv")`, hệ điều hành sẽ lập tức báo lỗi sập bộ nhớ `MemoryError` vì không đủ RAM để chứa toàn bộ bảng.

Giải pháp chuẩn mực của các kỹ sư là sử dụng tham số **`chunksize`** để chia tệp lớn thành các khối nhỏ vừa vặn với bộ nhớ:

```python
tong, dem = 0.0, 0
for chunk in pd.read_csv(StringIO(text), chunksize=2):
    values = chunk["doanh_thu"].dropna()
    tong += values.sum()
    dem += len(values)
tb = tong / dem if dem else None
print(tong, dem, tb)             # 100.0 2 50.0
```

Khi truyền `chunksize=2`, hàm `read_csv` không trả về một DataFrame duy nhất mà trả về một **trình lặp** (iterator). Mỗi vòng lặp chỉ nạp đúng 2 dòng vào RAM, xử lý xong sẽ giải phóng bộ nhớ để nạp 2 dòng kế tiếp.

Trong kỹ thuật này, có một cái bẫy toán học cực kỳ nguy hiểm mà nhiều người mắc phải: **Ngụy biện trung bình của các trung bình (Average of Averages Fallacy)**.

Giả sử ta có hai khối dữ liệu:
- Khối 1 chỉ có 1 phần tử: `[10]`, giá trị trung bình là 10.
- Khối 2 có 3 phần tử: `[20, 30, 40]`, giá trị trung bình là $(20+30+40)/3 = 30$.

Nếu bạn tính trung bình của từng khối rồi lấy trung bình của hai con số đó, bạn sẽ nhận được:
$$(10 + 30) / 2 = 20$$

Nhưng trung bình thực sự của toàn bộ 4 con số là:
$$(10 + 20 + 30 + 40) / 4 = 100 / 4 = 25$$

Con số 20 hoàn toàn sai lệch vì bạn đã vô tình gán trọng số cho khối 1 (chỉ có 1 phần tử) ngang bằng với khối 2 (có tới 3 phần tử). 

Do đó, khi xử lý theo từng khối, ta bắt buộc phải duy trì hai biến tích lũy trạng thái thống kê độc lập: **tổng đại số** (`tong += values.sum()`) và **tổng số lượng quan sát hợp lệ** (`dem += len(values)`). Phép chia tính trung bình chỉ được phép thực hiện duy nhất một lần ở bước tổng kết cuối cùng.

## 3. Dữ liệu phân cấp JSON và phẳng hóa bảng

JSON (JavaScript Object Notation) là định dạng thống trị trên web và các giao diện lập trình ứng dụng (API). Khác với CSV dạng bảng phẳng, JSON có cấu trúc cây lồng nhau (nested tree), nơi mỗi đối tượng có thể chứa các đối tượng con hoặc các mảng danh sách.

```python
import json

payload = '{"items":[{"id":"001","meta":{"nhom":"A"},"gia":20}]}'
obj = json.loads(payload)
bang = pd.json_normalize(obj["items"], sep="_")
print(bang.columns.tolist())     # ['id', 'gia', 'meta_nhom']
assert bang.loc[0, "meta_nhom"] == "A"
```

Hàm **`pd.json_normalize()`** là công cụ đắc lực giúp ta "phẳng hóa" cấu trúc cây phân cấp thành các cột của DataFrame. Tham số `sep="_"` quy định cách đặt tên cột mới cho các trường lồng nhau: trường `nhom` nằm bên trong đối tượng `meta` được tự động chuyển đổi thành cột `meta_nhom`.

Nếu một bản ghi chứa một danh sách các phần tử con (ví dụ một đơn hàng chứa danh sách nhiều món đồ), ta có thể sử dụng phương thức `df.explode()` để mở rộng mỗi phần tử con thành một hàng riêng biệt. Tuy nhiên, việc này sẽ làm nhân bản mã định danh của đơn hàng cha, đòi hỏi ta phải thiết lập khóa phức hợp để nhận diện từng dòng mới.

So sánh ba định dạng lưu trữ chủ lực:
- **CSV**: Định dạng văn bản thuần, con người đọc được trực tiếp, nhưng dung lượng cồng kềnh, tốc độ đọc ghi chậm và không lưu giữ thông tin kiểu dữ liệu.
- **JSON**: Hoàn hảo để biểu diễn dữ liệu phân cấp phức tạp và trao đổi qua mạng Internet, nhưng không tối ưu cho các phép tính tổng hợp thống kê trên quy mô lớn.
- **Parquet**: Định dạng nhị phân lưu trữ theo cột (columnar storage), hỗ trợ nén dữ liệu cực mạnh và lưu giữ toàn vẹn lược đồ kiểu dữ liệu. Parquet là tiêu chuẩn công nghiệp hiện đại cho các kho dữ liệu lớn (Data Lake / Data Warehouse).

## 4. Cơ sở dữ liệu SQL: Đẩy phép tính xuống nơi lưu trữ dữ liệu

Khi làm việc với các hệ thống dữ liệu doanh nghiệp, dữ liệu thường được lưu trữ trong các hệ quản trị cơ sở dữ liệu quan hệ (RDBMS) như PostgreSQL, MySQL hay SQLite.

Một sai lầm rất lớn của người mới học là viết câu lệnh `SELECT * FROM bang_du_lieu` để kéo toàn bộ hàng triệu dòng về máy tính rồi mới dùng pandas để lọc. Cách làm này gây lãng phí băng thông mạng nghiêm trọng và dễ làm tràn bộ nhớ máy tính cá nhân.

Quy tắc của kỹ sư dữ liệu là: **Đẩy phép tính xuống cơ sở dữ liệu (Pushdown Computation)**. Cơ sở dữ liệu được tối ưu hóa với hệ thống chỉ mục (Index) trên đĩa cứng. Hãy để máy chủ cơ sở dữ liệu thực hiện các phép lọc (`WHERE`) và phép tổng hợp (`GROUP BY`), ta chỉ kéo về máy kết quả tinh gọn cần thiết.

```python
import sqlite3

with sqlite3.connect(":memory:") as con:
    df.to_sql("ban_hang", con, index=False)
    query = "SELECT id, doanh_thu FROM ban_hang WHERE nhom = ?"
    chon = pd.read_sql_query(query, con, params=("A",))
print(chon["doanh_thu"].sum())    # 100.0
```

Hai quy tắc bảo mật và kỹ thuật sống còn:

1. **Tuyệt đối không dùng f-string để ghép câu lệnh SQL**: Nếu bạn viết `f"SELECT * FROM ban_hang WHERE nhom = '{user_input}'"`, hệ thống của bạn sẽ đứng trước nguy cơ bị tấn công hủy diệt bởi lỗ hổng **SQL Injection**. Kẻ xấu có thể truyền vào chuỗi `' OR '1'='1` để đánh cắp toàn bộ dữ liệu, hoặc nghiêm trọng hơn là câu lệnh xóa bảng `'; DROP TABLE ban_hang; --`.
2. **Luôn sử dụng câu lệnh tham số hóa (Parameterized Query)**: Cú pháp dấu hỏi chấm `WHERE nhom = ?` và truyền tham số qua tuple `params=("A",)` tách bạch hoàn toàn mã lệnh thực thi khỏi dữ liệu đầu vào. Trình điều khiển cơ sở dữ liệu sẽ tự động xử lý thoát ký tự an toàn trước khi thực thi.

## 5. Tiêu thụ dữ liệu từ API có trách nhiệm

Giao diện lập trình ứng dụng (API) là cánh cửa để thu thập dữ liệu động từ các dịch vụ bên ngoài qua giao thức mạng HTTP.

Khi làm việc với API, có ba nguyên tắc đạo đức và kỹ thuật cần tuân thủ:

1. **Nhận thức về phân trang (Pagination)**: Một API chuyên nghiệp không bao giờ trả về hàng triệu bản ghi trong một phản hồi duy nhất vì nguy cơ làm nghẽn máy chủ. Dữ liệu luôn được chia thành từng trang thông qua tham số số trang hoặc con trỏ (cursor). Ta phải viết vòng lặp kiểm tra trường `next` cho đến khi hết dữ liệu mới được coi là thu thập trọn vẹn.
2. **Kiểm tra hợp đồng dữ liệu phòng thủ**: Mỗi phản hồi nhận về từ mạng phải được kiểm tra cấu trúc nghiêm ngặt trước khi đưa vào bảng phân tích:

```python
pages = [
    {"items": [{"id": "001"}], "next": "page2"},
    {"items": [{"id": "002"}], "next": None},
]
records = []
for page in pages:
    if not isinstance(page.get("items"), list):
        raise ValueError("Thieu danh sach items")
    records.extend(page["items"])
api_df = pd.DataFrame(records)
assert api_df["id"].is_unique
print(len(api_df))               # 2
```

3. **Tôn trọng giới hạn tần suất (Rate Limiting)**: Mọi dịch vụ web đều áp đặt giới hạn số lượng yêu cầu mỗi phút. Nếu gửi yêu cầu quá dồn dập, máy chủ sẽ trả về lỗi HTTP 429 (Too Many Requests) hoặc chặn địa chỉ IP của bạn. Hãy luôn thiết lập khoảng nghỉ (`time.sleep`) hợp lý và áp dụng chiến lược thử lại lùi bước lũy thừa (exponential backoff) khi gặp sự cố mạng.

## 6. Bài tập tự luyện

::: exercise Thẩm định sai số trung bình theo khối
Giả sử ta đọc một tệp lớn chia thành hai khối: khối thứ nhất chỉ có 1 phần tử mang giá trị 10, khối thứ hai có 3 phần tử mang các giá trị 20, 30, 40.
1. Giá trị trung bình thực sự của toàn bộ 4 phần tử là bao nhiêu?
2. Nếu một người lấy trung bình của khối 1 cộng với trung bình của khối 2 rồi chia đôi, kết quả là bao nhiêu? Giải thích bản chất sai lầm của cách tính này.
:::

::: solution
1. Tổng thực tế của 4 phần tử là $10 + 20 + 30 + 40 = 100$. Số lượng quan sát là 4. Giá trị trung bình chuẩn xác là:
$$\frac{100}{4} = 25$$

2. Trung bình của khối 1 là 10. Trung bình của khối 2 là $(20 + 30 + 40) / 3 = 30$.
Trung bình của hai con số này là:
$$\frac{10 + 30}{2} = 20$$

Sai lầm ở đây là **ngụy biện đánh đồng trọng số**. Phép tính thứ hai đã coi khối 1 (chỉ có 1 phần tử) có tầm ảnh hưởng ngang bằng với khối 2 (có 3 phần tử). Để tính đúng trung bình qua nhiều khối dữ liệu, ta bắt buộc phải cộng dồn tổng giá trị và tổng số lượng phần tử độc lập, rồi chỉ chia một lần ở bước cuối cùng.
:::

::: exercise Xử lý mã quốc gia đặc biệt trong CSV
Một tệp CSV chứa danh sách mã bưu cục và quốc gia, trong đó có mã `"001"` và mã quốc gia của nước Namibia là `"NA"`. Hãy nêu hai cấu hình tham số bắt buộc khi gọi `pd.read_csv()` để dữ liệu không bị biến dạng.
:::

::: solution
Hai cấu hình cần thiết là:
1. `dtype={"ma_buu_cuc": "string"}`: Ngăn chặn pandas tự động ép kiểu mã `"001"` thành số nguyên $1$, giữ nguyên vẹn hai chữ số 0 ở đầu.
2. `keep_default_na=False` (hoặc định nghĩa danh sách `na_values` riêng không chứa `"NA"`): Ngăn chặn pandas tự động nhận diện chuỗi `"NA"` của nước Namibia thành giá trị khuyết thiếu `NaN`.
:::

::: exercise Hệ quả của việc mở rộng danh sách lồng nhau
Một bảng dữ liệu khách hàng có 3 bản ghi. Cột danh sách số điện thoại của 3 khách hàng này lần lượt chứa 2 số, 1 số và 3 số điện thoại con. Nếu ta thực hiện lệnh `df.explode()` để mỗi số điện thoại thành một dòng riêng biệt, bảng mới có bao nhiêu dòng? Mã định danh khách hàng có còn duy nhất không?
:::

::: solution
1. Bảng mới sẽ có tổng cộng $2 + 1 + 3 = 6$ dòng.
2. Mã định danh khách hàng ban đầu **không còn duy nhất** nữa, vì khách hàng thứ nhất sẽ xuất hiện lặp lại 2 lần và khách hàng thứ ba xuất hiện 3 lần. Để nhận diện duy nhất từng dòng trong bảng mới, ta cần thiết lập khóa phức hợp kết hợp giữa mã khách hàng và số thứ tự của số điện thoại.
:::

::: exercise Xử lý dữ liệu quy mô lớn vượt bộ nhớ RAM với Chunking và DuckDB
Giả sử hệ thống ghi nhận tệp nhật ký giao dịch `giao_dich_lon.csv` có hàng triệu dòng (dung lượng 10 GB), trong khi máy chủ của bạn chỉ có 4 GB RAM khả dụng. Mỗi dòng gồm các cột: `ma_gd`, `chi_nhanh`, `gia_tri`, `trang_thai`.
Yêu cầu:
1. Hãy viết chương trình tính tổng doanh thu và giá trị giao dịch trung bình của từng `chi_nhanh` cho các giao dịch thành công (`trang_thai == 'SUCCESS'` và `gia_tri > 0`).
2. Chương trình phải chạy mượt mà, tuyệt đối không được nạp toàn bộ tệp vào RAM cùng một lúc gây lỗi tràn bộ nhớ (*Out-Of-Memory* - OOM).
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Kỹ thuật đọc phân khối Chunking tích lũy trọng số)
Một cách người ta hay dùng trong pandas khi dữ liệu lớn hơn RAM là đọc từng khối dữ liệu bằng tham số `chunksize` và tích lũy trạng thái (*State Accumulation*):

```python
import pandas as pd
from collections import defaultdict

# Khởi tạo bộ tích lũy trạng thái: tổng tiền và số giao dịch
tong_tien = defaultdict(float)
so_giao_dich = defaultdict(int)

# Đọc từng khối 100,000 dòng một lượt, chỉ nạp các cột cần thiết
for chunk in pd.read_csv("giao_dich_lon.csv", chunksize=100_000, usecols=["chi_nhanh", "gia_tri", "trang_thai"]):
    # Lọc các dòng hợp lệ ngay trong khối bộ nhớ tạm
    mask = (chunk["trang_thai"] == "SUCCESS") & (chunk["gia_tri"] > 0)
    hop_le = chunk[mask]
    
    # Gom nhóm cục bộ trên khối
    nhom_khoi = hop_le.groupby("chi_nhanh")["gia_tri"].agg(["sum", "count"])
    
    # Tích lũy vào từ điển trạng thái toàn cục
    for chi_nhanh, row in nhom_khoi.iterrows():
        tong_tien[chi_nhanh] += row["sum"]
        so_giao_dich[chi_nhanh] += int(row["count"])

# Tính trung bình chuẩn tắc từ tổng dồn và đếm dồn
bao_cao_chunking = pd.DataFrame({
    "chi_nhanh": list(tong_tien.keys()),
    "tong_doanh_thu": list(tong_tien.values()),
    "so_don": [so_giao_dich[k] for k in tong_tien.keys()]
})
bao_cao_chunking["gia_trung_binh"] = bao_cao_chunking["tong_doanh_thu"] / bao_cao_chunking["so_don"]
print("Báo cáo Chunking:\n", bao_cao_chunking)
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Sử dụng DuckDB Engine với cơ chế Streaming Execution)
Trong các hệ thống phân tích hiện đại, giải pháp tối ưu vượt bậc là sử dụng DuckDB để đẩy thẳng câu truy vấn SQL xuống tệp dữ liệu (đặc biệt khi tệp được lưu ở định dạng Parquet theo cột):

```python
import duckdb

# DuckDB tự động chia luồng xử lý ngoài đĩa (Out-of-Core Processing)
# Tiêu thụ cực ít RAM và thực thi với tốc độ mã C/C++ đa luồng
sql_query = """
    SELECT 
        chi_nhanh,
        SUM(gia_tri) AS tong_doanh_thu,
        COUNT(*) AS so_don,
        AVG(gia_tri) AS gia_trung_binh
    FROM 'giao_dich_lon.parquet'
    WHERE trang_thai = 'SUCCESS' AND gia_tri > 0
    GROUP BY chi_nhanh
    ORDER BY tong_doanh_thu DESC
"""

# Chuyển đổi kết quả cuối cùng thành DataFrame chỉ mất vài miligiây
bao_cao_duckdb = duckdb.query(sql_query).to_df()
print("Báo cáo DuckDB Engine:\n", bao_cao_duckdb)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Nghịch lý lấy trung bình của các trung bình**: Sai lầm chết người của người mới là tính trung bình của từng chunk rồi lại lấy trung bình cộng của các giá trị trung bình đó:
  $$
  \bar{x}_{\text{chung}} \ne \frac{\bar{x}_1 + \bar{x}_2 + \dots + \bar{x}_k}{k}
  $$
  Công thức trên chỉ đúng khi mọi khối dữ liệu đều có số dòng hợp lệ bằng nhau tuyệt đối. Trong thực tế, các khối có số dòng hợp lệ khác nhau; do đó bắt buộc phải duy trì hai biến tích lũy riêng biệt: $\sum x$ và $\sum n$.
- **Ưu thế của Parquet và DuckDB**: Tệp CSV lưu trữ theo dạng dòng (*Row-oriented*) khiến chương trình phải đọc toàn bộ các ký tự của cả dòng trước khi lọc cột. Trong khi đó, định dạng Parquet lưu trữ theo cột (*Columnar*) kết hợp với cơ chế thực thi hình nón của DuckDB cho phép bỏ qua hàng tỷ byte dữ liệu của các cột không liên quan, tăng tốc độ xử lý từ 20 đến 50 lần.
:::

## 7. Nguồn và đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 6: Data Loading, Storage, and File Formats](https://wesmckinney.com/book/accessing-data).
- Tài liệu chính thức về công cụ IO: [pandas IO Tools — Text, CSV, JSON, SQL, Parquet](https://pandas.pydata.org/docs/user_guide/io.html).
- Hướng dẫn bảo mật cơ sở dữ liệu: [Python sqlite3 Module — Security Considerations](https://docs.python.org/3/library/sqlite3.html).
- [Bài giảng tham khảo môn Xử lý dữ liệu (iaidev)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-06-ket-noi-truy-xuat-du-lieu.html).
