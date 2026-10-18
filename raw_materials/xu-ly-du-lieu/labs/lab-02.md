## Lab 02: Xử lý dữ liệu bằng thư viện chuẩn Python

Khi đọc CSV bằng Python, giá và ngày tháng ban đầu thường vẫn là chuỗi. Ta sẽ lần lượt chuyển giá sang số, phân biệt giá 0 với giá thiếu, tổng hợp theo khu vực rồi ghi báo cáo. Hai cách giải trong bộ bài này đều dùng thư viện chuẩn Python.

## Thông tin dữ liệu thực hành

Bài thực hành mô phỏng bài toán phân tích thị trường chỗ ở phục vụ doanh nghiệp lữ hành, dựa trên tập dữ liệu Inside Airbnb với ảnh chụp ngày 29/06/2026 tại thành phố Santiago (Chile).

Tệp dữ liệu gốc công bố tại các địa chỉ mạng:
- Danh sách chỗ ở (`listings.csv`): `https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv`
- Danh sách đánh giá du khách (`reviews.csv`): `https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/reviews.csv`

Nhằm bảo đảm khả năng chạy độc lập tại chỗ và kiểm tra biên nhanh chóng, các bài tập dưới đây sử dụng tập dữ liệu giả lập 6 dòng với cấu trúc phản ánh đầy đủ các trường hợp thực tế như giá trị bị khuyết hoặc giá trị bằng không:

```python
DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)
```

Lưu ý: Mọi kết quả tính toán trên tập mẫu 6 dòng này là dữ liệu giả lập phục vụ kiểm chứng thuật toán, không phản ánh toàn bộ quy mô thực tế của thành phố Santiago.

---

## Danh mục bài tập thực hành

<span id="data-lab-02-01"></span>
### Bài 1: Định dạng số liệu nâng cao với chuỗi f-string

::: exercise
Thực hành kỹ thuật định dạng số liệu kinh tế và tỷ lệ thống kê bằng chuỗi ký tự f-string trong Python.
Cho giá trị trung bình `gia_tb = 118199.6` (đơn vị CLP) và tỷ lệ `ty_le = 0.178`. Hãy tạo chuỗi `ket_qua` có định dạng `"Giá TB: 118,200 CLP"` bằng cú pháp phân tách hàng nghìn không lấy phần thập phân (`:,.0f`), đồng thời tạo chuỗi `ty_le_chu` có định dạng `"17.8%"` bằng cú pháp phần trăm một chữ số thập phân (`:.1%`).

Yêu cầu kỹ thuật:
- Đầu vào: Số thực `gia_tb` và số thực `ty_le`.
- Thao tác: Áp dụng cú pháp định dạng f-string với các đặc tả định dạng `:,.0f` và `:.1%`.
- Đầu ra: Hai chuỗi ký tự đã được định dạng chuẩn xác.
- Trường hợp biên: Giá trị số bằng không hoặc các số thực có chu kỳ thập phân vô hạn.
:::

::: solution
#### Cách 1: Áp dụng trực tiếp cú pháp f-string trong biểu thức

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

gia_tb = 118199.6
ty_le = 0.178
ket_qua = f"Giá TB: {gia_tb:,.0f} CLP"
ty_le_chu = f"{ty_le:.1%}"
print(ket_qua)
print(ty_le_chu)

# Kết thúc lời giải
```

#### Giải thích cách 1

Trong f-string, biểu thức giữa `{}` được tính trước rồi định dạng theo phần sau dấu hai chấm. Với `gia_tb`, dấu `,` thêm dấu phân cách hàng nghìn, `.0f` hiển thị số thực với không chữ số sau dấu thập phân. Giá trị `118199.6` vì thế được hiển thị thành `118,200`.

Đặc tả `.1%` nhận tỷ lệ trên thang 0–1, nhân với `100` khi hiển thị và thêm dấu `%`. Do đó `0.178` thành `17.8%`. Hai biến kết quả là chuỗi dùng để đọc hoặc đưa vào báo cáo, còn `gia_tb` và `ty_le` vẫn giữ nguyên kiểu số và giá trị ban đầu.

#### Kết quả cách 1

```text
Giá TB: 118,200 CLP
17.8%
```

#### Cách 2: Đóng gói các hàm định dạng có tham số tùy biến

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải


def format_currency(amount: float, currency: str = "CLP") -> str:
    """Định dạng số tiền với dấu phẩy phân cách hàng nghìn và làm tròn nguyên."""
    return f"Giá TB: {amount:,.0f} {currency}"


def format_percent(ratio: float, decimals: int = 1) -> str:
    """Định dạng tỷ lệ số thực sang chuỗi phần trăm."""
    return f"{ratio:.{decimals}%}"


print(format_currency(118199.6))
print(format_percent(0.178))

# Kết thúc lời giải
```

#### Giải thích cách 2

`format_currency` nhận số tiền ở `amount`, đơn vị ở `currency` và trả một chuỗi. Nếu không truyền đơn vị, giá trị mặc định là `"CLP"`. `format_percent` nhận tỷ lệ và số chữ số thập phân. Phần `{decimals}` nằm bên trong đặc tả định dạng cho phép chọn mức làm tròn từ đối số.

Hai lời gọi mẫu truyền đúng các số của Cách 1 nên trả đúng hai chuỗi đó. Hàm không đổi đơn vị tiền tệ hay tỷ giá, chỉ thay nhãn và cách hiển thị. Chẳng hạn truyền `currency="USD"` chỉ ghi thêm chữ USD, không chuyển một số tiền CLP sang USD.

#### Kết quả cách 2

```text
Giá TB: 118,200 CLP
17.8%
```

#### So sánh hai cách

Cách 1 phù hợp với một vị trí hiển thị. Cách 2 gom quy tắc định dạng để các báo cáo dùng nhất quán. Đặt biểu thức trong hàm tăng khả năng tái sử dụng, không chứng minh thời gian thực thi thấp hơn.

:::

---

<span id="data-lab-02-02"></span>
### Bài 2: Xử lý giá trị khuyết và phân biệt None với số không

::: exercise
Trong xử lý dữ liệu, giá trị `None` biểu diễn sự vắng mặt của thông tin (missing data), trong khi số `0` là một phép đo có ý nghĩa thực tế (ví dụ: Chỗ ở miễn phí hoặc chương trình khuyến mại).
Cho danh sách `gia = [52000, None, 78000, 0]`. Hãy sử dụng cú pháp danh sách thu gọn (list comprehension) để trích xuất các giá trị hợp lệ (loại bỏ `None` nhưng giữ lại số `0`), sau đó tính giá trị trung bình cộng của các phần tử hợp lệ này.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách chứa số nguyên, số thực và giá trị `None`.
- Thao tác: Lọc bằng điều kiện `is not None`, sau đó tính tổng bằng `sum()` và chia cho `len()`.
- Đầu ra: Danh sách các giá trị hợp lệ `gia_co` và số thực trung bình cộng `tb`.
- Trường hợp biên: Danh sách rỗng hoặc danh sách chỉ chứa toàn bộ phần tử `None`.
:::

::: solution
#### Cách 1: Sử dụng list comprehension với điều kiện is not None

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

gia = [52000, None, 78000, 0]
gia_co = [g for g in gia if g is not None]
tb = sum(gia_co) / len(gia_co)
print(f"Giá hợp lệ: {gia_co}")
print(f"Giá trung bình: {tb:.1f}")

# Kết thúc lời giải
```

#### Giải thích cách 1

List comprehension đọc từng `g` trong `gia` và chỉ giữ khi `g is not None`. Điều kiện này hỏi giá trị có phải đối tượng `None` hay không, nên giữ nguyên số `0`. Danh sách hợp lệ là `[52000, 78000, 0]`, có tổng `130000` và ba phần tử.

`sum(gia_co)` cộng các số, `len(gia_co)` đếm số quan sát. Phép chia cho kết quả khoảng `43333.3333`, còn `:.1f` chỉ làm tròn khi in thành `43333.3`. Nếu dùng `if g`, số `0` cũng bị loại do được đánh giá là sai trong điều kiện, khiến tập dữ liệu và mẫu số bị thay đổi.

#### Kết quả cách 1

```text
Giá hợp lệ: [52000, 78000, 0]
Giá trung bình: 43333.3
```

#### Cách 2: Đóng gói hàm xử lý an toàn danh sách rỗng

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải


def filter_and_mean(values: list) -> tuple[list[float | int], float | None]:
    """Lọc các phần tử khác None và tính trung bình số học an toàn."""
    valid_elements = [v for v in values if v is not None]
    if not valid_elements:
        return [], None
    average_value = sum(valid_elements) / len(valid_elements)
    return valid_elements, average_value


gia_hop_le_vi_du, trung_binh_vi_du = filter_and_mean([52000, None, 78000, 0])
print(f"Danh sách: {gia_hop_le_vi_du} | Trung bình: {trung_binh_vi_du:.1f}")

# Kết thúc lời giải
```

#### Giải thích cách 2

`filter_and_mean` tạo danh sách `valid_elements` bằng cùng quy tắc giữ mọi phần tử khác `None`. Nhánh `if not valid_elements` kiểm tra danh sách có rỗng hay không. Nếu rỗng, hàm trả bộ `([], None)` để biểu thị chưa có trung bình, thay vì thực hiện phép chia cho `0`.

Khi có dữ liệu, hàm trả hai phần theo thứ tự: Danh sách số hợp lệ và trung bình của danh sách đó. Phép gán hai biến ở nơi gọi tách bộ kết quả để sử dụng riêng. Hàm giả định các phần tử khác `None` là số, nên chuỗi chưa chuyển kiểu cần được xử lý trước khi truyền vào.

#### Kết quả cách 2

```text
Danh sách: [52000, 78000, 0] | Trung bình: 43333.3
```

#### So sánh hai cách

Cả hai giữ đúng giá bằng không. Cách 1 làm rõ phép lọc và phép tính trên đầu vào đã có số hợp lệ. Cách 2 bổ sung quy ước trả về khi không có số nào để tính, phù hợp cho dữ liệu có thể rỗng.

:::

---

<span id="data-lab-02-03"></span>
### Bài 3: Đối chiếu tập hợp phòng giữa hai thời điểm bằng phép toán set

::: exercise
Doanh nghiệp du lịch cần theo dõi biến động thị trường giữa hai lần thu thập dữ liệu (snapshots).
Cho hai tập mã phòng `thang_3 = {101, 102, 103, 104}` và `thang_6 = {102, 104, 105}`. Hãy xác định danh sách các phòng đã biến mất trong tháng 6 (có ở tháng 3 nhưng không còn ở tháng 6) và danh sách các phòng mới xuất hiện ở tháng 6 (có ở tháng 6 nhưng chưa từng xuất hiện ở tháng 3).

Yêu cầu kỹ thuật:
- Đầu vào: Hai đối tượng tập hợp `set` chứa mã số nguyên định danh phòng.
- Thao tác: Áp dụng phép toán hiệu tập hợp (set difference).
- Đầu ra: Hai tập hợp kết quả `bien_mat` và `moi_them`.
- Trường hợp biên: Hai tập hợp trùng khớp hoàn toàn hoặc một trong hai tập hợp rỗng.
:::

::: solution
#### Cách 1: Sử dụng toán tử trừ tập hợp trực tiếp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

thang_3 = {101, 102, 103, 104}
thang_6 = {102, 104, 105}
bien_mat = thang_3 - thang_6
moi_them = thang_6 - thang_3
print(f"Phòng biến mất: {bien_mat}")
print(f"Phòng mới thêm: {moi_them}")

# Kết thúc lời giải
```

#### Giải thích cách 1

Phép hiệu `thang_3 - thang_6` duyệt các mã trong tập thứ nhất và giữ mã không có trong tập thứ hai. Kết quả chứa `101` và `103`. Đổi thứ tự toán hạng thành `thang_6 - thang_3` trả về các mã chỉ có trong tháng 6, ở đây là `105`.

Tập hợp không chứa phần tử trùng và không quy định thứ tự trình bày. Vì thế thứ tự các số khi in tập không phải tiêu chí kiểm tra đáp án. Các tên `bien_mat` và `moi_them` mô tả sự vắng hoặc có mặt trong hai snapshot, chưa cho biết chỗ ở thực sự đóng cửa hay mới bắt đầu kinh doanh.

#### Kết quả cách 1

| Kết quả | Các mã |
| --- | --- |
| bien_mat | `{101, 103}` |
| moi_them | `{105}` |

#### Cách 2: Sử dụng các phương thức có tên của lớp set

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải


def compare_snapshots(before: set, after: set) -> dict[str, set]:
    """So sánh hai tập hợp định danh phòng ở hai thời điểm khác nhau."""
    return {
        "disappeared": before.difference(after),
        "added": after.difference(before),
        "retained": before.intersection(after),
    }


ket_qua_ss = compare_snapshots({101, 102, 103, 104}, {102, 104, 105})
print(f"Biến mất: {ket_qua_ss['disappeared']} | Mới thêm: {ket_qua_ss['added']}")

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm `compare_snapshots` nhận hai tập `before`, `after` và trả một từ điển gồm ba tập. `before.difference(after)` là hiệu theo chiều trước trừ sau. `after.difference(before)` tính chiều ngược lại. `before.intersection(after)` tìm những mã xuất hiện ở cả hai thời điểm.

Phương thức trả các tập mới và không xóa phần tử khỏi hai tập đầu vào. Trong mẫu, phần giao là `{102, 104}`. Bảng băm giúp tra cứu một phần tử có thời gian trung bình hằng số, nhưng phép hiệu toàn bộ vẫn phải xét nhiều phần tử. Không được gán độ phức tạp hằng số cho việc so sánh cả hai snapshot.

#### Kết quả cách 2

| Trường kết quả | Các mã |
| --- | --- |
| disappeared | `{101, 103}` |
| added | `{105}` |
| retained | `{102, 104}` |

#### So sánh hai cách

Hai cách tính cùng hai hiệu tập hợp. Cách 2 bổ sung phần giao và đặt tên các kết quả để dùng tiếp trong báo cáo. Chỉ biết một mã biến mất chưa đủ kết luận chủ nhà dừng kinh doanh, vì còn có thể do thay đổi thu thập hoặc phạm vi dữ liệu.

:::

---

<span id="data-lab-02-04"></span>
### Bài 4: Đọc tệp CSV và quản lý ngữ cảnh an toàn

::: exercise
Viết hàm `read_listings(path)` nhận vào đường dẫn tệp CSV và trả về danh sách các từ điển (`list[dict]`), trong đó mỗi từ điển biểu diễn một dòng dữ liệu chỗ ở với các khóa là tên cột.
Hàm phải sử dụng câu lệnh quản lý ngữ cảnh `with open` với bảng mã UTF-8 để bảo đảm tệp luôn được đóng an toàn. Toàn bộ giá trị đọc lên phải được giữ ở dạng chuỗi nguyên bản. Trường hợp tệp chỉ có dòng tiêu đề mà không có dữ liệu, hàm phải trả về danh sách rỗng `[]`.

Yêu cầu kỹ thuật:
- Đầu vào: Đường dẫn tệp dạng chuỗi văn bản hoặc đối tượng `Path`.
- Thao tác: Dùng `csv.DictReader` đọc từng dòng bản ghi.
- Đầu ra: Danh sách từ điển `list[dict]`.
- Trường hợp biên: Tệp chỉ chứa duy nhất một dòng tiêu đề hoặc chứa các ký tự có dấu quốc tế.
:::

::: solution
#### Cách 1: Sử dụng csv.DictReader và khối with open tiêu chuẩn

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

from pathlib import Path

Path("listings.csv").write_text(DEMO_CSV, encoding="utf-8")

# Bắt đầu lời giải

import csv

# Khởi tạo tệp CSV trên đĩa để phục vụ đọc dữ liệu trực tiếp
with open("listings.csv", mode="w", encoding="utf-8") as f:
    f.write(DEMO_CSV)


def read_listings(path: str) -> list[dict]:
    """Đọc tệp CSV và trả về danh sách các từ điển biểu diễn từng dòng."""
    with open(path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


rows = read_listings("listings.csv")
print(f"Số dòng đọc được: {len(rows)}")
print("Bản ghi đầu tiên:", rows[0]["name"], "-", rows[0]["price"], "CLP")

# Kết thúc lời giải
```

#### Giải thích cách 1

`open(..., mode="w", encoding="utf-8")` tạo tệp thử nghiệm từ chuỗi CSV. Khi đọc, `csv.DictReader` dùng dòng đầu làm các khóa của từng từ điển. `list(reader)` đọc hết các dòng còn lại và lưu chúng trong danh sách, nên kết quả có sáu phần tử.

Mô đun `csv` không tự chuyển chuỗi giá thành số ở đây. `rows[0]["price"]` vẫn là chuỗi `"100"`, còn ô giá trống ở dòng thứ ba là `""`. Khối `with` đóng tệp khi ra khỏi phạm vi, kể cả khi thân khối phát sinh ngoại lệ. Điều này khác với việc phải tự gọi `close` ở cuối.

#### Kết quả cách 1

```text
Số dòng đọc được: 6
Bản ghi đầu tiên: Phong A - 100 CLP
```

#### Cách 2: Sử dụng pathlib.Path kết hợp tham số newline an toàn

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

from pathlib import Path

Path("listings.csv").write_text(DEMO_CSV, encoding="utf-8")

# Bắt đầu lời giải

import csv
from pathlib import Path


def read_listings(path: str | Path) -> list[dict]:
    """Đọc tệp CSV an toàn với newline='' và hỗ trợ đối tượng Path."""
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"Không tìm thấy tệp dữ liệu: {path}")
    with file_path.open(mode="r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


rows_pathlib = read_listings(Path("listings.csv"))
print(f"Số bản ghi đọc qua Pathlib: {len(rows_pathlib)}")

# Kết thúc lời giải
```

#### Giải thích cách 2

`Path(path)` chuẩn hóa đối số đường dẫn thành đối tượng `Path`. `exists()` kiểm tra sự tồn tại trước khi mở và nhánh lỗi phát sinh `FileNotFoundError` với thông báo rõ đường dẫn. `file_path.open` nhận các tham số tương tự `open` của Python.

Với tệp CSV, `newline=""` giao việc xử lý ký tự kết thúc dòng cho mô đun `csv`, giúp đọc đúng các trường có xuống dòng bên trong dấu nháy. UTF-8 quyết định cách giải mã văn bản, còn `newline` quyết định xử lý xuống dòng. Chúng giải quyết hai việc khác nhau. `list(csv.DictReader(f))` vẫn nạp toàn bộ bản ghi vào bộ nhớ.

#### Kết quả cách 2

```text
Số bản ghi đọc qua Pathlib: 6
```

| id | name | price |
| --- | --- | --- |
| `"1"` | `"Phong A"` | `"100"` |
| `"2"` | `"Phong B"` | `"50"` |
| `"3"` | `"Phong C"` | `""` |

#### So sánh hai cách

Cách 1 giới thiệu chu trình tạo và đọc một tệp. Cách 2 thêm hỗ trợ đường dẫn dạng Path và xử lý xuống dòng theo yêu cầu của CSV. Cả hai trả danh sách chứa giá trị chuỗi, nên vẫn cần bước chuyển kiểu cho việc tính toán.

:::

---

<span id="data-lab-02-05"></span>
### Bài 5: Chuyển đổi kiểu số thực và bắt ngoại lệ có chủ đích

::: exercise
Trong các tệp CSV thực tế, dữ liệu số thường bị lẫn các ô trống `""`, khoảng trắng, giá trị thiếu `None`, hoặc chuỗi ký tự đặc biệt như `"N/A"`. Nếu trực tiếp gọi `float(val)`, chương trình sẽ dừng do ngoại lệ `ValueError` hoặc `TypeError`.
Hãy viết hàm `to_float(value)`: Nếu `value` là chuỗi số hoặc số thực hợp lệ thì trả về `float`, còn nếu là `None`, chuỗi rỗng `""` hoặc chuỗi không chuyển đổi được thì trả về `None`. Bắt đúng hai loại ngoại lệ `ValueError` và `TypeError`. Giữ nguyên giá trị `0.0`.

Yêu cầu kỹ thuật:
- Đầu vào: Một giá trị bất kỳ từ trường dữ liệu CSV.
- Thao tác: Bọc lệnh ép kiểu trong khối `try/except (ValueError, TypeError)`.
- Đầu ra: Số thực `float` hoặc giá trị `None`.
- Trường hợp biên: Chuỗi `"0"` phải chuyển thành số thực `0.0`, tuyệt đối không trả về `None`.
:::

::: solution
#### Cách 1: Bắt trực tiếp hai ngoại lệ dự kiến trong khối try except

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải


def to_float(value) -> float | None:
    """Chuyển đổi chuỗi sang số thực an toàn bằng try except."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


print("Chuyển chuỗi hợp lệ '12.5':", to_float("12.5"))
print("Chuyển giá trị số không '0':", to_float("0"))
print("Chuyển giá trị None:", to_float(None))

# Kết thúc lời giải
```

#### Giải thích cách 1

`float(value)` thử chuyển giá trị thành số thực. Chuỗi `"12.5"` chuyển thành `12.5`, chuỗi `"0"` thành `0.0`. Chuyển `None` gây `TypeError`, còn chuỗi không phân tích thành số như `"abc"` gây `ValueError`.

Khối `except (ValueError, TypeError)` chỉ bắt hai lỗi đã dự kiến và trả `None` để biểu thị giá thiếu hoặc không đọc được. Các lỗi ngoài danh sách vẫn được truyền ra. Số `0.0` được trả trực tiếp từ `float`, không đi qua một kiểm tra đúng/sai nên không bị mất.

#### Kết quả cách 1

```text
Chuyển chuỗi hợp lệ '12.5': 12.5
Chuyển giá trị số không '0': 0.0
Chuyển giá trị None: None
```

#### Cách 2: Tiền xử lý chuỗi ký tự kết hợp bắt ngoại lệ chặt chẽ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


print("Chuyển chuỗi có khoảng trắng ' 12.5 ':", to_float(" 12.5 "))
print("Chuyển chuỗi 'N/A':", to_float("N/A"))

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm tách riêng trường hợp `None` trước khi chuyển kiểu. Nếu đầu vào là chuỗi, `strip()` bỏ khoảng trắng ở hai đầu. `cleaned.upper() == "N/A"` nhận diện dấu báo thiếu không phân biệt hoa thường. Chuỗi rỗng hoặc dấu báo thiếu được trả về `None` trước khi gọi `float`.

Với chuỗi số, phần còn lại vẫn là `float(cleaned)` và hai ngoại lệ dự kiến. `float` vốn đã chấp nhận khoảng trắng ngoài một chuỗi số, nên `strip()` chủ yếu làm rõ quy tắc chuẩn hóa, không tạo ra một tốc độ đã được chứng minh. Hai hàm đều còn chấp nhận các chuỗi đặc biệt như `"nan"` hoặc `"inf"`. Nếu bài toán yêu cầu số hữu hạn, cần thêm kiểm tra hữu hạn riêng.

#### Kết quả cách 2

```text
Chuyển chuỗi có khoảng trắng ' 12.5 ': 12.5
Chuyển chuỗi 'N/A': None
```

#### So sánh hai cách

Cách 1 ngắn và tận dụng cơ chế ngoại lệ. Cách 2 thể hiện rõ các dấu báo thiếu và bước chuẩn hóa chuỗi trước khi chuyển kiểu. Cả hai giữ giá bằng không, nhưng việc xác định một mức giá hợp lệ về nghiệp vụ vẫn cần quy tắc bổ sung.

:::

---

<span id="data-lab-02-06"></span>
### Bài 6: Làm sạch cột giá và tính toán số lượng bản ghi khuyết thiếu

::: exercise
Áp dụng hàm `to_float` đã viết ở Bài 5 lên toàn bộ danh sách phòng chỗ ở đọc được từ CSV.
Hãy tạo danh sách `gia` chứa giá đã chuyển đổi của mọi phòng (bao gồm cả `None`), trích xuất danh sách `gia_hop_le` chỉ chứa các giá trị khác `None`, và tính toán số lượng phòng không khai báo giá `so_thieu`.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách từ điển `rows` đọc từ tệp CSV.
- Thao tác: Sử dụng list comprehension áp dụng `to_float` cho cột `price`, sau đó lọc các phần tử `is not None`.
- Đầu ra: Danh sách `gia`, danh sách `gia_hop_le` và số nguyên `so_thieu`.
- Trường hợp biên: Mọi phòng đều có giá hợp lệ (`so_thieu = 0`) hoặc mọi phòng đều thiếu giá.
:::

::: solution
#### Cách 1: Sử dụng hai lượt comprehension tuần tự

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


gia = [to_float(row["price"]) for row in rows]

# Bắt đầu lời giải

gia = [to_float(r["price"]) for r in rows]
gia_hop_le = [g for g in gia if g is not None]
so_thieu = len(gia) - len(gia_hop_le)
print(f"Tổng số phòng: {len(gia)}")
print(f"Số phòng có giá hợp lệ: {len(gia_hop_le)}")
print(f"Số phòng thiếu giá: {so_thieu}")

# Kết thúc lời giải
```

#### Giải thích cách 1

Comprehension thứ nhất đọc trường `price` của từng bản ghi rồi gọi `to_float`. Danh sách `gia` giữ đủ sáu vị trí, kể cả vị trí thứ ba có giá thiếu. Comprehension thứ hai chỉ lấy những số khác `None` để tạo danh sách phục vụ thống kê.

Số giá thiếu là chênh lệch giữa độ dài hai danh sách. Mẫu có sáu dòng, năm giá đọc được và một giá thiếu, nên `so_thieu` bằng `1`. Giá `0.0` vẫn nằm trong danh sách hợp lệ vì điều kiện xét danh tính `None`, không xét giá trị có đúng trong điều kiện hay không.

#### Kết quả cách 1

| Chỉ số | Giá trị |
| --- | --- |
| Tổng số dòng | 6 |
| Giá đã chuyển | `[100.0, 50.0, None, 150.0, 0.0, 300.0]` |
| Giá hợp lệ | `[100.0, 50.0, 150.0, 0.0, 300.0]` |
| Số giá thiếu | 1 |

#### Cách 2: Duyệt một lượt đơn tích lũy đồng thời

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


gia = [to_float(row["price"]) for row in rows]

# Bắt đầu lời giải


def clean_price_column(records: list[dict]) -> dict:
    """Làm sạch cột giá qua một lượt duyệt duy nhất để phân loại giá trị."""
    all_prices = []
    valid_prices = []
    missing_count = 0
    for record in records:
        parsed_price = to_float(record.get("price"))
        all_prices.append(parsed_price)
        if parsed_price is not None:
            valid_prices.append(parsed_price)
        else:
            missing_count += 1
    return {
        "all_prices": all_prices,
        "valid_prices": valid_prices,
        "n_missing": missing_count,
    }


ket_qua_lam_sach = clean_price_column(rows)
print(
    f"Phòng hợp lệ: {len(ket_qua_lam_sach['valid_prices'])} | Khuyết thiếu: {ket_qua_lam_sach['n_missing']}"
)

# Kết thúc lời giải
```

#### Giải thích cách 2

`clean_price_column` duyệt mỗi bản ghi một lần và gọi `to_float` đúng một lần cho bản ghi đó. Kết quả luôn được thêm vào `all_prices`. Nếu khác `None`, nó còn được thêm vào `valid_prices`, nếu bằng `None` thì tăng bộ đếm `missing_count`.

`record.get("price")` trả `None` khi thiếu khóa, cho phép dùng chung quy tắc chuyển đổi của hàm trước. Từ điển trả về đặt tên cho cả ba kết quả, nên nơi gọi có thể lấy danh sách đầy đủ hoặc danh sách để tính thống kê. Vòng lặp một lượt gom các bước phân loại, nhưng vẫn lưu cả hai danh sách và cần bộ nhớ tỷ lệ với số bản ghi.

#### Kết quả cách 2

| Chỉ số | Giá trị |
| --- | --- |
| Tổng số dòng | 6 |
| Giá đã chuyển | `[100.0, 50.0, None, 150.0, 0.0, 300.0]` |
| Giá hợp lệ | `[100.0, 50.0, 150.0, 0.0, 300.0]` |
| Số giá thiếu | 1 |

#### So sánh hai cách

Cách 1 tách bước chuyển kiểu và bước lọc, thuận tiện quan sát dữ liệu trung gian. Cách 2 gom bước phân loại và đếm trong một lượt duyệt. Hai cách cho cùng ba kết quả trên mẫu, và đều chỉ gọi hàm chuyển kiểu một lần cho mỗi dòng.

:::

---

<span id="data-lab-02-07"></span>
### Bài 7: Thống kê tóm tắt phân phối: Số quan sát, giá trung bình và trung vị

::: exercise
Viết hàm `summarize_prices(prices: list[float | None]) -> dict` nhận vào danh sách giá (chứa cả các phần tử `None`). Hãy bỏ qua các phần tử `None`, giữ lại các phần tử số (bao gồm cả số `0.0`).
Trả về một từ điển có đúng 4 khóa:
- `n_valid`: Số lượng phần tử có giá trị hợp lệ.
- `n_missing`: Số lượng phần tử bị khuyết (`None`).
- `mean`: Giá trị trung bình cộng của các phần tử hợp lệ.
- `median`: Giá trị trung vị của các phần tử hợp lệ.
Nếu danh sách không có bất kỳ phần tử hợp lệ nào, `mean` và `median` phải nhận giá trị `None`. Không thực hiện làm tròn số trong hàm này.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách `prices` chứa số thực hoặc `None`.
- Thao tác: Lọc giá trị hợp lệ, sắp xếp để tìm trung vị, tính trung bình cộng.
- Đầu ra: Từ điển chứa đúng 4 khóa theo quy chuẩn.
- Trường hợp biên: Danh sách rỗng `[]` trả về `{"n_valid": 0, "n_missing": 0, "mean": None, "median": None}`.
:::

::: solution
#### Cách 1: Tách hàm trung vị riêng biệt và tính toán tóm tắt

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


gia = [to_float(row["price"]) for row in rows]

# Bắt đầu lời giải


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


def summarize_prices(prices: list[float | None]) -> dict:
    valid = [p for p in prices if p is not None]
    n_v = len(valid)
    n_m = len(prices) - n_v
    if n_v == 0:
        return {"n_valid": 0, "n_missing": n_m, "mean": None, "median": None}
    mean_val = sum(valid) / n_v
    median_val = trung_vi(valid)
    return {"n_valid": n_v, "n_missing": n_m, "mean": mean_val, "median": median_val}


tom_tat_gia_c1 = summarize_prices(gia)
print("Tóm tắt giá tập dữ liệu mẫu (Cách 1):", tom_tat_gia_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

`trung_vi` dùng `sorted(xs)` tạo danh sách tăng dần mà không đổi danh sách đầu vào. Với số phần tử lẻ, chỉ số `n // 2` trỏ vào phần tử chính giữa. Với số phần tử chẵn, hai chỉ số `n // 2 - 1` và `n // 2` trỏ vào cặp giữa để lấy trung bình của chúng.

`summarize_prices` lọc `None` rồi tính số hợp lệ và số thiếu. Mẫu có các giá tăng dần `[0.0, 50.0, 100.0, 150.0, 300.0]`, nên phần tử giữa là `100.0`. Tổng năm giá bằng `600.0`, chia `5` cho trung bình `120.0`. Khi không có giá hợp lệ, cả hai thống kê trả `None`, còn số lượng vẫn được ghi đầy đủ.

#### Kết quả cách 1

| n_valid | n_missing | mean | median |
| --- | --- | --- | --- |
| 5 | 1 | 120.0 | 100.0 |

#### Cách 2: Sắp xếp danh sách tại chỗ và tìm trung vị trực tiếp

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


gia = [to_float(row["price"]) for row in rows]

# Bắt đầu lời giải


def summarize_prices(prices: list[float | None]) -> dict:
    """Tóm tắt phân phối giá bằng cách lọc số thực và tìm trung vị trực tiếp."""
    valid_prices = []
    missing_count = 0
    for p in prices:
        if p is not None:
            valid_prices.append(float(p))
        else:
            missing_count += 1
    count_valid = len(valid_prices)
    if count_valid == 0:
        return {"n_valid": 0, "n_missing": missing_count, "mean": None, "median": None}
    valid_prices.sort()
    avg_price = sum(valid_prices) / count_valid
    if count_valid % 2 == 1:
        med_price = valid_prices[count_valid // 2]
    else:
        med_price = (
            valid_prices[count_valid // 2 - 1] + valid_prices[count_valid // 2]
        ) / 2.0
    return {
        "n_valid": count_valid,
        "n_missing": missing_count,
        "mean": avg_price,
        "median": med_price,
    }


tom_tat_gia_c2 = summarize_prices(gia)
print("Tóm tắt giá tập dữ liệu mẫu (Cách 2):", tom_tat_gia_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm thứ hai tạo danh sách số hợp lệ và đếm giá thiếu ngay trong vòng lặp. Mỗi số hợp lệ được chuyển sang `float`. `valid_prices.sort()` thay đổi chính danh sách mới tạo, còn danh sách `prices` truyền vào không bị sắp xếp lại.

Sau sắp xếp, hàm áp dụng cùng hai trường hợp chẵn/lẻ để tìm trung vị. Việc đưa thuật toán vào cùng hàm tránh thêm một bản sao do gọi `sorted` trên danh sách đã lọc. Tuy nhiên phép sắp xếp vẫn có chi phí tăng theo số giá, và không thể kết luận toàn bộ hàm nhanh hơn chỉ từ số dòng mã. Bốn khóa trả về giữ đúng số đếm và các thống kê chưa làm tròn.

#### Kết quả cách 2

| n_valid | n_missing | mean | median |
| --- | --- | --- | --- |
| 5 | 1 | 120.0 | 100.0 |

#### So sánh hai cách

Cách 1 tách hàm trung vị để học và tái sử dụng. Cách 2 tính trực tiếp trên danh sách nội bộ, tránh thêm một danh sách sắp xếp. Cả hai trả `None` cho thống kê không xác định và giữ `0.0` là một quan sát hợp lệ.

:::

---

<span id="data-lab-02-08"></span>
### Bài 8: Truy vết bản ghi có giá trị cực đại với khóa so sánh tùy biến

::: exercise
Viết hàm `most_expensive(records: list[dict]) -> str | None` nhận vào danh sách các bản ghi chỗ ở, trong đó mỗi bản ghi có trường `id` (dạng chuỗi) và trường `price` (đã là số thực hoặc `None`).
Hàm tìm và trả về mã `id` của phòng có giá cao nhất bằng cách sử dụng hàm `max(..., key=...)`.
Bỏ qua các bản ghi có giá `None`, nhưng giữ lại các phòng có giá bằng `0`. Nếu có nhiều phòng đồng giá cao nhất, hàm phải trả về phòng xuất hiện đầu tiên trong danh sách. Nếu không có bất kỳ phòng nào có giá hợp lệ, hàm trả về `None`.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách từ điển `records`.
- Thao tác: Áp dụng hàm `max()` với tham số `key` tùy biến.
- Đầu ra: Chuỗi `id` của phòng đắt nhất hoặc `None`.
- Trường hợp biên: Toàn bộ danh sách đều có giá `None` hoặc danh sách rỗng.
:::

::: solution
#### Cách 1: Lọc phòng có giá trước khi gọi hàm max với biểu thức lambda

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


# Bắt đầu lời giải

# Tạo danh sách bản ghi có trường giá dạng số thực từ rows
phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def most_expensive(records: list[dict]) -> str | None:
    """Tìm id phòng có giá cao nhất bằng max với key tùy biến."""
    co_gia = [r for r in records if r.get("price") is not None]
    if not co_gia:
        return None
    return max(co_gia, key=lambda r: r["price"])["id"]


id_dat_nhat_c1 = most_expensive(phong_co_gia_so)
print("Mã phòng đắt nhất (Cách 1):", id_dat_nhat_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Danh sách `phong_co_gia_so` giữ mã phòng, khu vực và giá đã chuyển kiểu. Trong hàm, bước lọc chỉ bỏ các bản ghi có `price is None`. `max(co_gia, key=lambda r: r["price"])` so sánh giá của từng bản ghi nhưng trả về toàn bộ bản ghi thắng, sau đó `["id"]` lấy mã.

`lambda` là một hàm ngắn nhận bản ghi `r` và trả giá để làm khóa so sánh. Khi nhiều bản ghi cùng đạt giá lớn nhất, `max` trả bản ghi xuất hiện đầu tiên. Nhánh `if not co_gia` tránh gọi `max` với danh sách rỗng. Trong mẫu, phòng `6` có giá `300.0` lớn nhất.

#### Kết quả cách 1

| Kết quả | Giá trị |
| --- | --- |
| id trả về | `"6"` |
| Giá dùng để đối chiếu | 300.0 |

#### Cách 2: Duyệt tuyến tính một lượt với cơ chế hòa điểm ổn định

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


# Bắt đầu lời giải


def most_expensive(records: list[dict]) -> str | None:
    """Tìm id phòng đắt nhất qua duyệt tuyến tính, giữ phần tử đầu tiên khi hòa điểm."""
    best_id = None
    max_price = float("-inf")
    for r in records:
        p = r.get("price")
        if p is not None and p > max_price:
            max_price = p
            best_id = r.get("id")
    return best_id


id_dat_nhat_c2 = most_expensive(phong_co_gia_so)
print("Mã phòng đắt nhất (Cách 2):", id_dat_nhat_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm duyệt từng bản ghi, giữ hai biến là mã tốt nhất và giá lớn nhất đã gặp. Mốc `float("-inf")` nhỏ hơn mọi mức giá hữu hạn trong bài, nên giá hợp lệ đầu tiên sẽ thay mốc. Mỗi lần gặp giá lớn hơn giá đang giữ, hàm cập nhật cả hai biến.

Điều kiện dùng `>` thay vì `>=` là điểm giữ thứ tự hòa điểm. Một giá bằng cực đại hiện tại không ghi đè mã đã tìm trước. Hàm không tạo danh sách bản ghi hợp lệ trung gian và chỉ lưu hai biến trạng thái. Với đầu vào rỗng hoặc toàn `None`, không có lần cập nhật nào nên trả `None`.

#### Kết quả cách 2

| Kết quả | Giá trị |
| --- | --- |
| id trả về | `"6"` |
| Giá lớn nhất được theo dõi | 300.0 |

#### So sánh hai cách

Hai cách đều xét số bản ghi theo một lượt tìm cực đại. Cách 1 thuận tiện khi dùng khóa so sánh của Python. Cách 2 tránh lưu danh sách lọc, vì thế tiết kiệm phần bộ nhớ trung gian đó. Trường hợp giá hòa nhau vẫn giữ bản ghi đầu ở cả hai cách.

:::

---

<span id="data-lab-02-09"></span>
### Bài 9: Tổng hợp và đếm tần suất theo nhóm phân loại

::: exercise
Viết hàm `count_by_area(records: list[dict]) -> dict[str, int]` nhận vào danh sách các bản ghi chỗ ở, trong đó mỗi bản ghi có trường `neighbourhood` là chuỗi không rỗng.
Hàm trả về một từ điển có dạng `{tên_khu: số_lượng_phòng}` bằng kỹ thuật từ điển cộng dồn. Hàm đếm toàn bộ các dòng xuất hiện, không phụ thuộc vào giá. Danh sách đầu vào rỗng phải trả về từ điển rỗng `{}`.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách từ điển chứa trường `neighbourhood`.
- Thao tác: Lặp qua từng bản ghi và cộng dồn số lượng vào từ điển.
- Đầu ra: Từ điển tần suất theo khu vực.
- Trường hợp biên: Danh sách rỗng hoặc tên khu vực chứa các ký tự có dấu quốc tế.
:::

::: solution
#### Cách 1: Sử dụng vòng lặp for và phương thức dict.get()

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))

# Bắt đầu lời giải


def count_by_area(records: list[dict]) -> dict[str, int]:
    """Đếm số phòng theo từng khu vực bằng từ điển cộng dồn."""
    counts = {}
    for r in records:
        area = r.get("neighbourhood")
        if area:
            counts[area] = counts.get(area, 0) + 1
    return counts


dem_khu_vuc_c1 = count_by_area(rows)
print("Số phòng theo khu vực (Cách 1):", dem_khu_vuc_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Mỗi lần đọc một bản ghi, hàm lấy tên khu vực bằng `r.get("neighbourhood")`. Nếu tên không rỗng, `counts.get(area, 0)` lấy số đếm đã có hoặc dùng `0` cho lần xuất hiện đầu. Cộng `1` rồi gán lại cập nhật đúng nhóm.

Hàm không xem cột giá, nên phòng thiếu giá ở Norte vẫn được tính vào nguồn cung. Mỗi khu có hai bản ghi trong sáu dòng, và từ điển trả về có ba khóa. Nếu đầu vào rỗng, vòng lặp không chạy và từ điển khởi tạo rỗng được trả nguyên vẹn.

#### Kết quả cách 1

| neighbourhood | Số dòng |
| --- | --- |
| Centro | 2 |
| Norte | 2 |
| Sur | 2 |

#### Cách 2: Sử dụng lớp Counter từ thư viện chuẩn collections

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))

# Bắt đầu lời giải

from collections import Counter


def count_by_area(records: list[dict]) -> dict[str, int]:
    """Đếm tần suất phòng bằng collections.Counter."""
    areas = [r["neighbourhood"] for r in records if r.get("neighbourhood")]
    counter = Counter(areas)
    return dict(counter)


dem_khu_vuc_c2 = count_by_area(rows)
print("Số phòng theo khu vực (Cách 2):", dem_khu_vuc_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

Comprehension tạo danh sách `areas` gồm tên khu vực không rỗng. `Counter(areas)` nhận một đối tượng có thể lặp và cộng số lần xuất hiện của mỗi tên. `dict(counter)` chuyển cấu trúc đếm đó thành từ điển thông thường để đáp ứng kiểu kết quả của đề.

Counter cung cấp thêm `most_common(n)` khi cần đọc `n` nhóm có số đếm cao. Trong bài này chưa cần gọi phương thức đó. Đoạn mã vẫn tạo một danh sách tên trung gian, vì vậy ngắn hơn không đồng nghĩa cần ít bộ nhớ hơn cách cộng dồn trực tiếp. Kết quả đếm vẫn bao gồm các dòng thiếu giá.

#### Kết quả cách 2

| neighbourhood | Số dòng |
| --- | --- |
| Centro | 2 |
| Norte | 2 |
| Sur | 2 |

#### So sánh hai cách

Cách 1 cho thấy thao tác tăng bộ đếm và không cần danh sách tên trung gian. Cách 2 diễn đạt ý định đếm bằng công cụ có sẵn. Chúng trả cùng tần suất, và việc chọn cách nào tùy nhu cầu đọc mã hoặc dùng tiếp các tiện ích của Counter.

:::

---

<span id="data-lab-02-10"></span>
### Bài 10: Tính giá trị trung vị theo từng khu vực địa lý

::: exercise
Viết hàm `median_by_area(records: list[dict]) -> dict[str, float | None]` nhận vào danh sách các bản ghi chứa trường `neighbourhood` (chuỗi không rỗng) và `price` (đã là số thực hoặc `None`).
Hàm tính và trả về giá trị trung vị cho **mọi khu vực** xuất hiện trong dữ liệu. Khu vực nào xuất hiện nhưng không có bất kỳ giá hợp lệ nào thì nhận giá trị `None`. Danh sách đầu vào rỗng trả về `{}`.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách bản ghi chỗ ở.
- Thao tác: Gom nhóm danh sách giá hợp lệ theo từng khu vực, sau đó áp dụng hàm `trung_vi`.
- Đầu ra: Từ điển `{tên_khu: giá_trung_vị}`.
- Trường hợp biên: Khu vực chỉ có giá `None`, hoặc khu vực chỉ có duy nhất 1 bản ghi.
:::

::: solution
#### Cách 1: Gom nhóm danh sách bằng từ điển thông thường

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


# Bắt đầu lời giải


def median_by_area(records: list[dict]) -> dict[str, float | None]:
    """Tính giá trung vị của từng khu vực xuất hiện trong dữ liệu."""
    grouped = {}
    for r in records:
        area = r.get("neighbourhood")
        if not area:
            continue
        if area not in grouped:
            grouped[area] = []
        p = r.get("price")
        if p is not None:
            grouped[area].append(float(p))
    result = {}
    for area, prices in grouped.items():
        result[area] = trung_vi(prices) if prices else None
    return result


trung_vi_khu_c1 = median_by_area(phong_co_gia_so)
print("Giá trung vị theo khu vực (Cách 1):", trung_vi_khu_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Từ điển `grouped` lưu mỗi tên khu vực kèm một danh sách giá. Danh sách được tạo ngay khi khu vực xuất hiện, trước khi kiểm tra giá. Vì thế khu vực toàn giá thiếu vẫn có mặt với danh sách rỗng và sau đó nhận trung vị `None`.

Giá khác `None` được chuyển thành `float` rồi thêm vào đúng danh sách. Ở lượt sau, hàm gọi `trung_vi(prices)` cho từng nhóm có giá. Centro có hai giá `50` và `100` nên trung vị `75`. Norte chỉ còn giá `150`, còn Sur giữ cả `0` và `300`, nên hai khu sau đều có trung vị `150`.

#### Kết quả cách 1

| Khu vực | Giá hợp lệ | Trung vị |
| --- | --- | --- |
| Centro | `[100.0, 50.0]` | 75.0 |
| Norte | `[150.0]` | 150.0 |
| Sur | `[0.0, 300.0]` | 150.0 |

#### Cách 2: Sử dụng collections.defaultdict để gom nhóm danh mục

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


# Bắt đầu lời giải

from collections import defaultdict


def median_by_area(records: list[dict]) -> dict[str, float | None]:
    """Tính giá trung vị theo khu vực bằng collections.defaultdict."""
    grouped = defaultdict(list)
    seen_areas = set()
    for r in records:
        area = r.get("neighbourhood")
        if not area:
            continue
        seen_areas.add(area)
        p = r.get("price")
        if p is not None:
            grouped[area].append(float(p))
    result = {}
    for area in seen_areas:
        prices = grouped[area]
        if not prices:
            result[area] = None
        else:
            prices.sort()
            n = len(prices)
            if n % 2 == 1:
                result[area] = prices[n // 2]
            else:
                result[area] = (prices[n // 2 - 1] + prices[n // 2]) / 2.0
    return result


trung_vi_khu_c2 = median_by_area(phong_co_gia_so)
print("Giá trung vị theo khu vực (Cách 2):", trung_vi_khu_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

`defaultdict(list)` tạo một danh sách mới khi lần đầu truy cập một khóa chưa có. `seen_areas` ghi lại mọi khu đã xuất hiện, kể cả khu không có giá hợp lệ. Đây là lý do hàm vẫn trả đủ nhóm khi cột giá của một nhóm toàn `None`.

Với mỗi khu, hàm sắp xếp danh sách nội bộ rồi chọn một phần tử giữa hoặc trung bình hai phần tử giữa. Duyệt một `set` không bảo đảm thứ tự tên khu, nên thứ tự khóa của từ điển in ra có thể khác Cách 1. Bảng dưới sắp tên khu để dễ so sánh giá trị, không coi thứ tự in của từ điển là một phần đáp án.

#### Kết quả cách 2

| Khu vực | Giá hợp lệ | Trung vị |
| --- | --- | --- |
| Centro | `[100.0, 50.0]` | 75.0 |
| Norte | `[150.0]` | 150.0 |
| Sur | `[0.0, 300.0]` | 150.0 |

#### So sánh hai cách

Hai cách có cùng quy tắc xử lý nhóm không có giá. Cách 1 tái sử dụng hàm trung vị. Cách 2 giảm nhánh khởi tạo danh sách nhờ defaultdict nhưng viết lại phép tính trung vị. Nếu cần thứ tự báo cáo cố định, hãy sắp các tên khu trước khi trình bày.

:::

---

<span id="data-lab-02-11"></span>
### Bài 11: Kiểm định chất lượng dữ liệu và kiểm tra chéo hai cột quan hệ

::: exercise
Viết hàm `review_qa(records: list[dict]) -> dict[str, int]` nhận vào danh sách các bản ghi dữ liệu, trong đó trường `number_of_reviews` là chuỗi số nguyên và `last_review` là chuỗi ngày tháng hoặc chuỗi rỗng `""`.
Hàm thực hiện quy tắc kiểm tra chất lượng dữ liệu (Data Quality Assurance):
- `n_zero`: Tổng số bản ghi có `number_of_reviews == "0"`.
- `n_inconsistent`: Trong số các bản ghi có 0 đánh giá đó, có bao nhiêu bản ghi mà trường `last_review` lại khác rỗng (bất thường về tính nhất quán).
Hàm tuyệt đối không tự ý sửa dữ liệu. Danh sách đầu vào rỗng phải trả về `{"n_zero": 0, "n_inconsistent": 0}`.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách bản ghi đọc từ CSV.
- Thao tác: Kiểm tra điều kiện phụ thuộc logic giữa hai trường dữ liệu.
- Đầu ra: Từ điển chứa hai chỉ số kiểm định chất lượng `n_zero` và `n_inconsistent`.
- Trường hợp biên: Toàn bộ dữ liệu đều nhất quán hoặc danh sách rỗng.
:::

::: solution
#### Cách 1: Duyệt vòng lặp for với các câu lệnh điều kiện tuần tự

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))

# Bắt đầu lời giải


def review_qa(records: list[dict]) -> dict[str, int]:
    """Kiểm tra chéo giữa số lượng đánh giá và ngày đánh giá gần nhất."""
    n_zero = 0
    n_inconsistent = 0
    for r in records:
        num_reviews = str(r.get("number_of_reviews", "")).strip()
        last_rev = str(r.get("last_review", "")).strip()
        if num_reviews == "0":
            n_zero += 1
            if last_rev != "":
                n_inconsistent += 1
    return {"n_zero": n_zero, "n_inconsistent": n_inconsistent}


ket_qua_qa_c1 = review_qa(rows)
print("Kết quả kiểm định chất lượng (Cách 1):", ket_qua_qa_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Hai bộ đếm bắt đầu từ `0`. `str(...).strip()` chuẩn hóa giá trị đọc từ CSV thành chuỗi không có khoảng trắng hai đầu. Nếu số đánh giá bằng `"0"`, hàm tăng `n_zero`, rồi mới kiểm tra ngày đánh giá có khác chuỗi rỗng hay không để tăng `n_inconsistent`.

Trên mẫu, các phòng mã `1` và `3` có số đánh giá `0` và đều để trống ngày, nên kết quả là hai dòng không có đánh giá và không có dòng mâu thuẫn. Việc tăng một bộ đếm không sửa bản ghi. Một trường hợp bị gắn cờ chỉ nói vi phạm quy tắc đang kiểm tra, chưa xác định nguyên nhân lỗi ở đâu.

#### Kết quả cách 1

| n_zero | n_inconsistent |
| --- | --- |
| 2 | 0 |

#### Cách 2: Sử dụng lọc danh sách kết hợp hàm sum trên biểu thức generator

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))

# Bắt đầu lời giải


def review_qa(records: list[dict]) -> dict[str, int]:
    """Kiểm tra chéo chất lượng dữ liệu bằng lọc danh sách và biểu thức đếm."""
    zero_reviews = [
        r for r in records if str(r.get("number_of_reviews", "")).strip() == "0"
    ]
    n_zero = len(zero_reviews)
    n_inconsistent = sum(
        1 for r in zero_reviews if str(r.get("last_review", "")).strip() != ""
    )
    return {"n_zero": n_zero, "n_inconsistent": n_inconsistent}


ket_qua_qa_c2 = review_qa(rows)
print("Kết quả kiểm định chất lượng (Cách 2):", ket_qua_qa_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

Comprehension `zero_reviews` giữ đúng tập bản ghi có số đánh giá bằng chuỗi `"0"` sau chuẩn hóa. `len(zero_reviews)` đếm tập này. Biểu thức generator phát ra số `1` cho mỗi dòng trong tập có ngày không rỗng, và `sum` cộng các số đó thành `n_inconsistent`.

Khác Cách 1, hàm lưu danh sách các dòng có không đánh giá rồi duyệt danh sách đó thêm một lượt. Đổi lại, hai phép đếm được tách rõ. Hai cột đầu vào trong bài được giả định là chuỗi CSV. Nếu nguồn có `None`, dấu báo thiếu khác hoặc số đánh giá không hợp lệ, cần quy tắc chuẩn hóa riêng trước khi kiểm tra quan hệ giữa hai cột.

#### Kết quả cách 2

| n_zero | n_inconsistent |
| --- | --- |
| 2 | 0 |

#### So sánh hai cách

Cách 1 kiểm tra cả hai điều kiện trong một lượt và dùng hai số đếm. Cách 2 giữ tập bản ghi được chọn để có thể xem lại. Cả hai chỉ báo chất lượng dữ liệu, không tự kết luận rằng một cơ chế đồng bộ cụ thể đã gây lỗi.

:::

---

<span id="data-lab-02-12"></span>
### Bài 12: Đóng gói và lưu trữ báo cáo phân tích ra tệp JSON

::: exercise
Viết hàm `save_report(report: dict, path: str | Path) -> dict` ghi từ điển báo cáo ra tệp tin định dạng JSON với bảng mã UTF-8.
Yêu cầu bắt buộc:
- Thiết lập tham số `ensure_ascii=False` để bảo tồn nguyên vẹn các ký tự tiếng Việt và tiếng Tây Ban Nha.
- Thiết lập tham số `indent=2` để tệp JSON có bố cục thụt đầu dòng dễ đọc.
- Sau khi ghi xong, hàm phải mở lại tệp bằng `json.load()` và trả về từ điển đọc lại để xác nhận tệp đã được ghi thành công và không bị hỏng cấu trúc.

Yêu cầu kỹ thuật:
- Đầu vào: Từ điển báo cáo `report` và đường dẫn tệp tin `path`.
- Thao tác: Dùng `json.dump()` để xuất tệp và `json.load()` để đọc lại.
- Đầu ra: Từ điển đọc lại từ tệp.
- Trường hợp biên: Đường dẫn tệp chứa ký tự có dấu hoặc đường dẫn thuộc đối tượng `Path`.
:::

::: solution
#### Cách 1: Sử dụng khối lệnh with open tiêu chuẩn với json.dump và json.load

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


gia = [to_float(row["price"]) for row in rows]

phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


def summarize_prices(prices: list[float | None]) -> dict:
    valid = [p for p in prices if p is not None]
    n_v = len(valid)
    n_m = len(prices) - n_v
    if n_v == 0:
        return {"n_valid": 0, "n_missing": n_m, "mean": None, "median": None}
    mean_val = sum(valid) / n_v
    median_val = trung_vi(valid)
    return {"n_valid": n_v, "n_missing": n_m, "mean": mean_val, "median": median_val}


def most_expensive(records: list[dict]) -> str | None:
    """Tìm id phòng có giá cao nhất bằng max với key tùy biến."""
    co_gia = [r for r in records if r.get("price") is not None]
    if not co_gia:
        return None
    return max(co_gia, key=lambda r: r["price"])["id"]


def median_by_area(records: list[dict]) -> dict[str, float | None]:
    """Tính giá trung vị của từng khu vực xuất hiện trong dữ liệu."""
    grouped = {}
    for r in records:
        area = r.get("neighbourhood")
        if not area:
            continue
        if area not in grouped:
            grouped[area] = []
        p = r.get("price")
        if p is not None:
            grouped[area].append(float(p))
    result = {}
    for area, prices in grouped.items():
        result[area] = trung_vi(prices) if prices else None
    return result


def review_qa(records: list[dict]) -> dict[str, int]:
    """Kiểm tra chéo giữa số lượng đánh giá và ngày đánh giá gần nhất."""
    n_zero = 0
    n_inconsistent = 0
    for r in records:
        num_reviews = str(r.get("number_of_reviews", "")).strip()
        last_rev = str(r.get("last_review", "")).strip()
        if num_reviews == "0":
            n_zero += 1
            if last_rev != "":
                n_inconsistent += 1
    return {"n_zero": n_zero, "n_inconsistent": n_inconsistent}


tom_tat_gia_c1 = summarize_prices(gia)
id_dat_nhat_c1 = most_expensive(phong_co_gia_so)
trung_vi_khu_c1 = median_by_area(phong_co_gia_so)
ket_qua_qa_c1 = review_qa(rows)

# Bắt đầu lời giải

import json

# Chuẩn bị từ điển báo cáo tổng hợp từ kết quả các bài trước
bao_cao_tong_hop = {
    "thanh_pho": "Santiago",
    "so_phong": len(rows),
    "gia": tom_tat_gia_c1,
    "id_dat_nhat": id_dat_nhat_c1,
    "gia_trung_vi_theo_khu": trung_vi_khu_c1,
    "review_qa": ket_qua_qa_c1,
}


def save_report(report: dict, path: str) -> dict:
    """Ghi báo cáo ra tệp JSON và đọc lại để xác nhận tính toàn vẹn."""
    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    with open(path, mode="r", encoding="utf-8") as f:
        return json.load(f)


bao_cao_doc_lai_c1 = save_report(bao_cao_tong_hop, "report_santiago.json")
print(
    "Đã ghi và đọc lại JSON thành công cho thành phố:", bao_cao_doc_lai_c1["thanh_pho"]
)

# Kết thúc lời giải
```

#### Giải thích cách 1

`bao_cao_tong_hop` tập hợp các kết quả trước thành một từ điển có cấu trúc. `json.dump(report, f, ensure_ascii=False, indent=2)` ghi cấu trúc đó vào tệp đang mở. `ensure_ascii=False` giữ chữ Unicode đọc được, còn `indent=2` xuống dòng và thụt lề hai khoảng trắng để người đọc dễ theo dõi.

`json.load(f)` đọc nội dung JSON thành đối tượng Python rồi trả về. Việc đọc lại cho phép so sánh những trường quan trọng như `so_phong`, thay vì chỉ tin rằng lệnh ghi không báo lỗi. Với dữ liệu mẫu, tên thành phố vẫn là `Santiago` và số phòng vẫn là `6`. Đối tượng phải gồm các kiểu JSON biểu diễn được, không thể ghi trực tiếp mọi đối tượng Python.

#### Kết quả cách 1

```text
Đã ghi và đọc lại JSON thành công cho thành phố: Santiago
```

| Trường đọc lại | Giá trị |
| --- | --- |
| thanh_pho | `"Santiago"` |
| so_phong | 6 |
| gia.n_valid | 5 |
| gia.mean | 120.0 |
| gia.median | 100.0 |
| id_dat_nhat | `"6"` |

#### Cách 2: Quản lý đường dẫn bằng pathlib.Path có kiểm tra thư mục cha

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


gia = [to_float(row["price"]) for row in rows]

phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


def summarize_prices(prices: list[float | None]) -> dict:
    valid = [p for p in prices if p is not None]
    n_v = len(valid)
    n_m = len(prices) - n_v
    if n_v == 0:
        return {"n_valid": 0, "n_missing": n_m, "mean": None, "median": None}
    mean_val = sum(valid) / n_v
    median_val = trung_vi(valid)
    return {"n_valid": n_v, "n_missing": n_m, "mean": mean_val, "median": median_val}


def most_expensive(records: list[dict]) -> str | None:
    """Tìm id phòng có giá cao nhất bằng max với key tùy biến."""
    co_gia = [r for r in records if r.get("price") is not None]
    if not co_gia:
        return None
    return max(co_gia, key=lambda r: r["price"])["id"]


def median_by_area(records: list[dict]) -> dict[str, float | None]:
    """Tính giá trung vị của từng khu vực xuất hiện trong dữ liệu."""
    grouped = {}
    for r in records:
        area = r.get("neighbourhood")
        if not area:
            continue
        if area not in grouped:
            grouped[area] = []
        p = r.get("price")
        if p is not None:
            grouped[area].append(float(p))
    result = {}
    for area, prices in grouped.items():
        result[area] = trung_vi(prices) if prices else None
    return result


def review_qa(records: list[dict]) -> dict[str, int]:
    """Kiểm tra chéo giữa số lượng đánh giá và ngày đánh giá gần nhất."""
    n_zero = 0
    n_inconsistent = 0
    for r in records:
        num_reviews = str(r.get("number_of_reviews", "")).strip()
        last_rev = str(r.get("last_review", "")).strip()
        if num_reviews == "0":
            n_zero += 1
            if last_rev != "":
                n_inconsistent += 1
    return {"n_zero": n_zero, "n_inconsistent": n_inconsistent}


tom_tat_gia_c1 = summarize_prices(gia)
id_dat_nhat_c1 = most_expensive(phong_co_gia_so)
trung_vi_khu_c1 = median_by_area(phong_co_gia_so)
ket_qua_qa_c1 = review_qa(rows)

bao_cao_tong_hop = {
    "thanh_pho": "Santiago",
    "so_phong": len(rows),
    "gia": tom_tat_gia_c1,
    "id_dat_nhat": id_dat_nhat_c1,
    "gia_trung_vi_theo_khu": trung_vi_khu_c1,
    "review_qa": ket_qua_qa_c1,
}

# Bắt đầu lời giải

import json
from pathlib import Path


def save_report(report: dict, path: str | Path) -> dict:
    """Ghi tệp JSON an toàn với Pathlib kèm kiểm tra thư mục cha."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with file_path.open(mode="w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    with file_path.open(mode="r", encoding="utf-8") as f:
        return json.load(f)


bao_cao_doc_lai_c2 = save_report(bao_cao_tong_hop, Path("report_santiago_p.json"))
print("Xác nhận số phòng ghi trong tệp JSON:", bao_cao_doc_lai_c2["so_phong"])

# Kết thúc lời giải
```

#### Giải thích cách 2

`Path(path)` cho phép nơi gọi truyền chuỗi hoặc đối tượng Path. `file_path.parent` lấy thư mục chứa tệp. `mkdir(parents=True, exist_ok=True)` tạo cả các thư mục cha còn thiếu và chấp nhận trường hợp thư mục đã tồn tại.

Phần mở, ghi, đóng và đọc lại JSON giữ cùng quy tắc của Cách 1. `with` bảo đảm tệp ghi đã đóng trước khi mở để đọc. Giá trị trả về là báo cáo vừa được giải mã, không phải chỉ đường dẫn tới tệp. Lời gọi với `Path("report_santiago_p.json")` vì thế cho phép truy cập ngay trường `so_phong` để kiểm tra.

#### Kết quả cách 2

```text
Xác nhận số phòng ghi trong tệp JSON: 6
```

| Trường đọc lại | Giá trị |
| --- | --- |
| thanh_pho | `"Santiago"` |
| so_phong | 6 |
| review_qa.n_zero | 2 |
| review_qa.n_inconsistent | 0 |

#### So sánh hai cách

Cách 1 đủ khi thư mục đích đã tồn tại. Cách 2 thêm xử lý cấu trúc thư mục và giao diện đường dẫn. Cả hai kiểm tra việc đọc lại trên dữ liệu mẫu, nhưng tên gọi hàm không phải bằng chứng rằng mọi kiểu hoặc mọi lỗi hệ thống tệp đều đã được xử lý.

:::

---

<span id="data-lab-02-13"></span>
### Bài 13: Bảng xếp hạng khu vực theo trung vị giá có lọc ngưỡng mẫu tối thiểu

::: exercise
Viết hàm `rank_areas(records: list[dict], min_valid: int = 100) -> list[dict]` nhận danh sách các bản ghi chỗ ở có trường `neighbourhood` và trường `price` đã làm sạch thành số thực hoặc `None`.
Quy định xếp hạng:
- Chỉ giữ lại các khu vực có số lượng giá hợp lệ đạt tối thiểu từ `min_valid` trở lên.
- Xếp hạng theo tiêu chí đa tầng: Giá trung vị (`median_price`) giảm dần, trường hợp có hai khu vực có cùng giá trung vị thì xếp theo tên khu vực (`neighbourhood`) tăng dần theo thứ tự từ điển chuỗi Python.
- Trả về danh sách các từ điển gồm đúng ba khóa `neighbourhood` (chuỗi), `n_valid` (số nguyên) và `median_price` (số thực).
- Nếu không có khu vực nào đạt ngưỡng, trả về danh sách rỗng `[]`.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách bản ghi `records` và số nguyên ngưỡng mẫu `min_valid`.
- Thao tác: Gom nhóm giá, lọc ngưỡng kích thước, sắp xếp đa tiêu chí.
- Đầu ra: Danh sách từ điển kết quả xếp hạng.
- Trường hợp biên: Hòa điểm về trung vị, hoặc dữ liệu đầu vào không đủ mẫu.
:::

::: solution
#### Cách 1: Gom nhóm bằng từ điển thông thường và sắp xếp bằng tuple khóa

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


# Bắt đầu lời giải


def rank_areas(records: list[dict], min_valid: int = 100) -> list[dict]:
    """Xếp hạng khu vực theo trung vị giá giảm dần, hòa điểm thì xếp tên tăng dần."""
    grouped = {}
    for r in records:
        area = r.get("neighbourhood")
        p = r.get("price")
        if area and p is not None:
            if area not in grouped:
                grouped[area] = []
            grouped[area].append(float(p))
    qualified = []
    for area, prices in grouped.items():
        if len(prices) >= min_valid:
            med = trung_vi(prices)
            qualified.append(
                {"neighbourhood": area, "n_valid": len(prices), "median_price": med}
            )
    qualified.sort(key=lambda r: (-r["median_price"], r["neighbourhood"]))
    return qualified


xep_hang_c1 = rank_areas(phong_co_gia_so, min_valid=2)
print("Bảng xếp hạng khu vực với min_valid=2 (Cách 1):", xep_hang_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Hàm gom các giá hợp lệ theo khu vực rồi chỉ đưa nhóm đạt `min_valid` vào bảng xếp hạng. Với đối số `2`, Norte bị loại vì chỉ có một giá hợp lệ, dù có hai dòng chỗ ở. Centro và Sur đều có hai giá nên đủ điều kiện.

`qualified.sort(key=lambda r: (-r["median_price"], r["neighbourhood"]))` dùng một tuple làm khóa. Thành phần âm của trung vị khiến giá lớn hơn đứng trước khi sắp tăng dần. Chỉ khi hai trung vị bằng nhau, Python mới xét thành phần tên khu tăng dần. Kết quả vì thế đặt Sur có trung vị `150.0` trước Centro có trung vị `75.0`.

#### Kết quả cách 1

| Hạng | neighbourhood | n_valid | median_price |
| --- | --- | --- | --- |
| 1 | Sur | 2 | 150.0 |
| 2 | Centro | 2 | 75.0 |

#### Cách 2: Sử dụng defaultdict và tính toán trung vị tại chỗ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

import csv
from io import StringIO

rows = list(csv.DictReader(StringIO(DEMO_CSV)))


def to_float(value) -> float | None:
    """Chuyển đổi kiểu số thực có kiểm tra khoảng trắng và chuỗi rỗng."""
    if value is None:
        return None
    if isinstance(value, str):
        cleaned = value.strip()
        if not cleaned or cleaned.upper() == "N/A":
            return None
        try:
            return float(cleaned)
        except (ValueError, TypeError):
            return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


phong_co_gia_so = [
    {"id": r["id"], "neighbourhood": r["neighbourhood"], "price": to_float(r["price"])}
    for r in rows
]


def trung_vi(xs: list[float]) -> float | None:
    ordered = sorted(xs)
    n = len(ordered)
    if n == 0:
        return None
    if n % 2 == 1:
        return ordered[n // 2]
    return (ordered[n // 2 - 1] + ordered[n // 2]) / 2.0


# Bắt đầu lời giải

from collections import defaultdict


def rank_areas(records: list[dict], min_valid: int = 100) -> list[dict]:
    """Xếp hạng khu vực đa tiêu chí bằng defaultdict và tính trung vị tại chỗ."""
    if min_valid <= 0:
        raise ValueError("Ngưỡng min_valid phải là số nguyên dương.")
    groups = defaultdict(list)
    for r in records:
        area = r.get("neighbourhood")
        p = r.get("price")
        if area and p is not None:
            groups[area].append(float(p))
    ranking = []
    for area, prices in groups.items():
        count_p = len(prices)
        if count_p >= min_valid:
            prices.sort()
            if count_p % 2 == 1:
                med = prices[count_p // 2]
            else:
                med = (prices[count_p // 2 - 1] + prices[count_p // 2]) / 2.0
            ranking.append(
                {"neighbourhood": area, "n_valid": count_p, "median_price": med}
            )
    ranking.sort(key=lambda item: (-item["median_price"], item["neighbourhood"]))
    return ranking


xep_hang_c2 = rank_areas(phong_co_gia_so, min_valid=2)
print("Bảng xếp hạng khu vực với min_valid=2 (Cách 2):", xep_hang_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

`defaultdict(list)` gom giá mà không cần nhánh khởi tạo danh sách cho từng khu. Hàm kiểm tra `min_valid <= 0` để từ chối ngưỡng không dương. Mỗi nhóm đủ mẫu được sắp xếp, rồi tính trung vị theo trường hợp số lượng chẵn hoặc lẻ.

`ranking.sort` dùng đúng tuple khóa như Cách 1 để giữ thứ tự xếp hạng. Danh sách trả về chỉ có ba khóa cho mỗi khu, không đưa các giá gốc vào báo cáo. Việc sắp danh sách giá tại chỗ chỉ sửa những danh sách mới tạo trong hàm, không đổi thứ tự bản ghi ở đầu vào.

#### Kết quả cách 2

| Hạng | neighbourhood | n_valid | median_price |
| --- | --- | --- | --- |
| 1 | Sur | 2 | 150.0 |
| 2 | Centro | 2 | 75.0 |

#### So sánh hai cách

Hai cách giữ cùng tiêu chí đủ mẫu và hòa điểm. Cách 1 dùng lại hàm trung vị, Cách 2 tính tại nơi gom nhóm và có kiểm tra ngưỡng. Ngưỡng `2` chỉ phục vụ fixture nhỏ, không tự là một tiêu chuẩn đủ đại diện cho thị trường thực tế.

:::

---

<span id="data-lab-02-14"></span>
### Bài 14: Thống kê chuỗi thời gian đánh giá du khách qua các năm

::: exercise
Viết hàm `review_counts_by_year(records: list[dict]) -> dict[str, int]` nhận vào danh sách các dòng dữ liệu đánh giá từ tệp `reviews.csv`.
Mỗi dòng chứa trường `date` có định dạng `YYYY-MM-DD` hoặc chuỗi rỗng `""`.
Yêu cầu:
- Bỏ qua các dòng có `date == ""` hoặc thiếu trường ngày tháng.
- Trích xuất năm bằng kỹ thuật cắt chuỗi ký tự 4 vị trí đầu tiên `date[:4]`.
- Đếm tổng số lượng đánh giá của từng năm. Không tự ý lọc trùng lặp bản ghi.
- Trả về một từ điển `{năm: số_đánh_giá}` với các khóa năm được sắp xếp tăng dần từ quá khứ đến hiện tại. Danh sách rỗng trả về `{}`.

Yêu cầu kỹ thuật:
- Đầu vào: Danh sách dòng đánh giá.
- Thao tác: Cắt chuỗi ngày tháng và cộng dồn số lượng theo năm.
- Đầu ra: Từ điển thời gian với các khóa được sắp xếp tăng dần.
- Trường hợp biên: Toàn bộ ngày đều rỗng hoặc định dạng ngày không đủ 4 ký tự.
:::

::: solution
#### Cách 1: Sử dụng kỹ thuật cắt chuỗi và từ điển cộng dồn

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

# Tập dữ liệu đánh giá mẫu để kiểm thử hàm
mau_danh_gia = [
    {"listing_id": "1", "date": "2026-01-01"},
    {"listing_id": "2", "date": "2025-12-31"},
    {"listing_id": "3", "date": "2026-01-01"},
    {"listing_id": "4", "date": ""},
]


def review_counts_by_year(records: list[dict]) -> dict[str, int]:
    """Đếm số đánh giá theo năm và sắp xếp khóa tăng dần."""
    counts = {}
    for r in records:
        date_str = r.get("date", "")
        if date_str:
            year = date_str[:4]
            counts[year] = counts.get(year, 0) + 1
    sorted_counts = {y: counts[y] for y in sorted(counts.keys())}
    return sorted_counts


nam_danh_gia_c1 = review_counts_by_year(mau_danh_gia)
print("Số lượng đánh giá theo năm (Cách 1):", nam_danh_gia_c1)

# Kết thúc lời giải
```

#### Giải thích cách 1

Mỗi bản ghi có ngày không rỗng đóng góp một lượt vào năm ở bốn ký tự đầu. `counts.get(year, 0) + 1` cộng số đánh giá cho năm đó. Hai đánh giá cùng ngày vẫn là hai bản ghi và được tính hai lần, đúng yêu cầu không tự bỏ trùng.

`sorted(counts.keys())` sắp các khóa năm trước khi tạo từ điển kết quả. Với chuỗi năm đủ bốn chữ số, thứ tự chuỗi trùng với thứ tự thời gian. Đoạn cắt chuỗi chỉ trích tiền tố, không chứng minh ngày tồn tại trong lịch. Nếu nguồn có ngày sai định dạng, phải xác thực ngày trước khi dùng kết quả như thống kê theo năm.

#### Kết quả cách 1

| Năm | Số đánh giá |
| --- | --- |
| 2025 | 1 |
| 2026 | 2 |

#### Cách 2: Sử dụng Counter từ danh sách năm đã lọc

```python
# Dữ liệu mẫu và các hàm hỗ trợ

mau_danh_gia = [
    {"listing_id": "1", "date": "2026-01-01"},
    {"listing_id": "2", "date": "2025-12-31"},
    {"listing_id": "3", "date": "2026-01-01"},
    {"listing_id": "4", "date": ""},
]

# Bắt đầu lời giải

from collections import Counter


def review_counts_by_year(records: list[dict]) -> dict[str, int]:
    """Đếm chuỗi thời gian đánh giá qua Counter và sắp xếp khóa tăng dần."""
    valid_years = [
        r["date"][:4] for r in records if r.get("date") and len(r["date"]) >= 4
    ]
    counter = Counter(valid_years)
    return {year: counter[year] for year in sorted(counter.keys())}


nam_danh_gia_c2 = review_counts_by_year(mau_danh_gia)
print("Số lượng đánh giá theo năm (Cách 2):", nam_danh_gia_c2)

# Kết thúc lời giải
```

#### Giải thích cách 2

`valid_years` là danh sách các tiền tố năm sau khi bỏ ngày rỗng và những chuỗi ngắn hơn bốn ký tự. `Counter(valid_years)` cộng tần suất từng năm. Comprehension cuối duyệt khóa đã sắp để tạo từ điển thường theo thứ tự tăng dần.

Kiểm tra độ dài ngăn một chuỗi rất ngắn bị coi là năm, nhưng vẫn chưa xác nhận đúng định dạng `YYYY-MM-DD` hay ngày hợp lệ. `Counter` giúp viết rõ thao tác đếm, trong khi danh sách năm trung gian vẫn dùng bộ nhớ tỷ lệ với số đánh giá. Mẫu có một dòng năm 2025, hai dòng năm 2026 và một dòng ngày trống bị bỏ qua.

#### Kết quả cách 2

| Năm | Số đánh giá |
| --- | --- |
| 2025 | 1 |
| 2026 | 2 |

#### So sánh hai cách

Cách 1 thể hiện từng bước cập nhật bộ đếm. Cách 2 dùng Counter và thêm lọc chuỗi quá ngắn. Trên nguồn đã bảo đảm định dạng ngày, hai cách trả cùng số đếm. Nếu nguồn không bảo đảm, cắt bốn ký tự không thay thế việc phân tích và xác thực ngày.

:::

---

<span id="data-lab-02-15"></span>
### Bài 15: Phân tích định lượng và suy luận nhân quả: Ngoại lai và bẫy thời gian chưa đầy đủ

::: exercise
Thực hiện phân tích chuyên sâu về mặt phương pháp luận và lập luận thống kê từ dữ liệu thực tế:
1. So sánh giá trị trung bình (mean) và giá trị trung vị (median) trên thị trường lưu trú. Giải thích vai trò của các giá trị ngoại lai (outliers), chẳng hạn trường hợp phòng có giá 97 triệu CLP/đêm.
2. Vì sao việc sử dụng điều kiện `if price:` là một sai sót kỹ thuật nghiêm trọng trong làm sạch dữ liệu so với `if price is not None:`?
3. Khi phát hiện dữ liệu có `number_of_reviews == "0"` nhưng lại xuất hiện ngày đánh giá gần nhất, vì sao nhà phân tích dữ liệu chuyên nghiệp phải lập báo cáo QA thay vì tự ý xóa bỏ bản ghi?
4. Trong phân tích chuỗi thời gian, vì sao không thể so sánh số lượng đánh giá của năm 2026 (snapshot ngày 29/06/2026) với cả năm 2025 để kết luận thị trường du lịch đang suy giảm?

Yêu cầu kỹ thuật:
- Đầu vào: Các kết quả số liệu thống kê thu được từ toàn bộ bài lab.
- Thao tác: Lập ma trận phân tích rủi ro kỹ thuật và xây dựng hàm kiểm tra tính hợp lệ của suy luận chuỗi thời gian.
- Đầu ra: Bản phân tích lập luận chặt chẽ và hàm cảnh báo bẫy dữ liệu thời gian chưa đầy đủ.
- Ranh giới kiểm chứng: Phân biệt rõ sự suy thoái kinh tế thực sự với sự biến động cơ học do độ dài chu kỳ thu thập dữ liệu bị cắt cụt.
:::

::: solution
#### Cách 1: Xây dựng ma trận phân loại rủi ro kỹ thuật và lập luận học thuật

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

# Ma trận phân loại các rủi ro kỹ thuật trong xử lý dữ liệu du lịch
bang_rui_ro = [
    {
        "Rui_ro": "Ngoại lai bóp méo trung bình",
        "Bieu_hien": "Giá 97 triệu CLP kéo trung bình tăng vọt",
        "Giai_phap": "Sử dụng trung vị thay vì trung bình",
    },
    {
        "Rui_ro": "Bẫy kiểm tra falsy",
        "Bieu_hien": "Dùng if price làm mất giá 0.0 hợp lệ",
        "Giai_phap": "Bắt buộc dùng if price is not None",
    },
    {
        "Rui_ro": "Xóa dòng bất thường tùy tiện",
        "Bieu_hien": "0 review nhưng có ngày đánh giá",
        "Giai_phap": "Lập báo cáo QA và gắn cờ dữ liệu",
    },
    {
        "Rui_ro": "Bẫy so sánh dữ liệu bị cắt cụt",
        "Bieu_hien": "Năm 2026 chỉ có 6 tháng so với cả năm 2025",
        "Giai_phap": "So sánh cùng kỳ hoặc chuẩn hóa theo ngày",
    },
]
print("Số lượng hạng mục phân tích rủi ro:", len(bang_rui_ro))

# Kết thúc lời giải
```

#### Giải thích cách 1

`bang_rui_ro` lưu bốn tình huống cùng biểu hiện và cách xử lý đề xuất. `len(bang_rui_ro)` đếm số mục, nên dòng in chỉ là số `4`. Nó không tính trung bình, trung vị hay phát hiện một xu hướng thị trường. Các mục là danh sách kiểm tra cần đối chiếu với số liệu thực tế.

Điểm quan trọng là chọn phép đo phù hợp câu hỏi. Trung bình dùng toàn bộ mức giá nên nhạy với giá rất lớn. Trung vị mô tả vị trí giữa, không tự thay cho mọi mục tiêu phân tích. `None` biểu thị thiếu thông tin còn `0` là giá trị số cần kiểm tra theo nghiệp vụ. Dòng vi phạm quan hệ giữa số đánh giá và ngày phải được lưu dấu để truy nguyên, không tự xóa chỉ vì khác kỳ vọng.

#### Kết quả cách 1

```text
Số lượng hạng mục phân tích rủi ro: 4
```

| Mục cần kiểm tra | Giới hạn cần nêu |
| --- | --- |
| Ngoại lai | Kiểm tra đơn vị và bản ghi trước khi loại |
| Giá bằng 0 | Không đồng nhất với None |
| Số đánh giá và ngày | Gắn cờ quan hệ không nhất quán |
| So sánh năm | Đối chiếu cùng khoảng thời gian quan sát |

#### Cách 2: Lập trình hàm cảnh báo bẫy suy luận chuỗi thời gian chưa đầy đủ

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải


def danh_gia_bien_dong_thoi_gian(counts_by_year: dict[str, int]) -> dict:
    """Đánh giá tính hợp lệ của việc so sánh biến động số liệu qua các năm."""
    years = sorted(counts_by_year.keys())
    if len(years) < 2:
        return {"canh_bao": "Không đủ dữ liệu hai năm", "ket_luan_hop_le": False}
    latest_year = years[-1]
    return {
        "nam_moi_nhat": latest_year,
        "so_luong_moi_nhat": counts_by_year[latest_year],
        "canh_bao": f"Năm {latest_year} có thể chưa đủ 12 tháng",
        "ket_luan_hop_le": False,
    }


ket_qua_danh_gia = danh_gia_bien_dong_thoi_gian({"2025": 1000, "2026": 550})
print("Đánh giá chuỗi thời gian:", ket_qua_danh_gia)

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm sắp các năm, yêu cầu có ít nhất hai năm rồi lấy năm mới nhất. Với từ điển mẫu, `latest_year` là `"2026"` và số đếm tương ứng là `550`. Hàm trả `ket_luan_hop_le=False` kèm lời cảnh báo thận trọng, thay vì biến chênh lệch hai tổng thành kết luận thị trường tăng hay giảm.

Chỉ số đếm theo năm không chứa ngày kết thúc thu thập. Do đó hàm chưa thể tự xác định năm nào đủ mười hai tháng, và câu cảnh báo dùng chữ “có thể”. Snapshot ngày 29/06/2026 chưa quan sát trọn năm 2026. So sánh cùng kỳ cần cùng khoảng ngày và quy tắc thu thập. Chuẩn hóa theo ngày giúp điều chỉnh độ dài quan sát nhưng không tự loại ảnh hưởng mùa vụ hay thay đổi bao phủ dữ liệu.

#### Kết quả cách 2

| Trường | Giá trị |
| --- | --- |
| nam_moi_nhat | `"2026"` |
| so_luong_moi_nhat | 550 |
| canh_bao | Năm 2026 có thể chưa đủ 12 tháng |
| ket_luan_hop_le | `False` |

#### So sánh hai cách

Cách 1 là khung lập luận để đọc kết quả của cả lab. Cách 2 minh họa một kiểm tra có thể tự động hóa, nhưng thiếu thông tin thời gian để xác nhận tính đầy đủ. Chúng không phải hai thuật toán tương đương cho một phép tính. Muốn kết luận xu hướng, phải bổ sung mốc quan sát và giả định so sánh.

:::

---

## Tài liệu tham khảo

1. Lutz, M. (2013). *Learning Python: Powerful Object-Oriented Programming* (5th ed.). O'Reilly Media.
2. Python Software Foundation. (2026). *The Python Standard Library: Các mô đun `csv`, `json`, `collections` và `pathlib`*. Python 3.12 Documentation.
3. Inside Airbnb. (2026). *Santiago Data Assumptions and Data Dictionary*. Inside Airbnb Open Data.
