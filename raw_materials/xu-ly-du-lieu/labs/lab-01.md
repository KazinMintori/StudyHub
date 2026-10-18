## Lab 01: Môi trường tính toán tương tác và cấu trúc dữ liệu bảng

Một notebook có thể chạy được trong phiên hiện tại nhưng báo lỗi sau khi khởi động lại. Các bài dưới đây giúp kiểm tra thứ tự chạy, trạng thái biến và cách đọc kết quả trên một bảng dữ liệu nhỏ.

## Thông tin dữ liệu thực hành

Bộ bài tập sử dụng dữ liệu chỗ ở Inside Airbnb với ảnh chụp dữ liệu (snapshot) ngày 29/06/2026 tại thành phố Santiago (Chile).
Có thể tải [bảng chỗ ở rút gọn của snapshot](https://data.insideairbnb.com/chile/rm/santiago/2026-06-29/visualisations/listings.csv) để thử lại với dữ liệu đầy đủ.

Nhằm phục vụ kiểm thử nhanh, độc lập môi trường và chạy trực tiếp không phụ thuộc kết nối mạng, các bài thực hành dưới đây sử dụng tập dữ liệu kiểm thử nhỏ gồm 6 dòng giả lập. Tập dữ liệu này phản ánh đúng cấu trúc và các trường hợp đặc biệt như giá trị khuyết thiếu hoặc giá trị bằng không:

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

Lưu ý: Các số liệu tính toán trên 6 dòng này là dữ liệu kiểm thử giả lập, không đại diện cho toàn bộ quy mô thị trường thực tế của thành phố Santiago.

---

## Danh mục bài tập thực hành

<span id="data-lab-01-01"></span>
### Bài 1: Thứ tự thực thi ô mã nguồn và ngoại lệ NameError

::: exercise
Tìm hiểu nguyên lý vận hành của không gian tên (namespace) trong tiến trình thực thi của sổ tay tương tác. Hãy giải thích vì sao khi thực thi một ô mã nguồn truy xuất biến trước khi ô định nghĩa biến đó được chạy, môi trường sẽ ném ra ngoại lệ `NameError`.

Yêu cầu kỹ thuật:
- Tình huống: Ô A định nghĩa biến `so_phong_gia_dinh = 4`. Ô B thực hiện lệnh `print("Số phòng gia đình hiện có:", so_phong_gia_dinh)`.
- Thao tác: Quan sát hiện tượng khi chạy ô B trước ô A trong một phiên làm việc mới. Sau đó chạy tuần tự ô A rồi đến ô B.
- Đầu ra: Trình bày cơ chế bắt lỗi và truy xuất an toàn thông qua việc kiểm tra không gian tên.
- Trường hợp biên: Phiên làm việc vừa khởi động lại (Restart session) làm mất sạch các biến lưu trữ trong bộ nhớ tạm.
:::

::: solution
#### Cách 1: Chạy tuần tự theo trật tự tự nhiên từ trên xuống dưới

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

# Thực thi tuần tự từ Cell A đến Cell B
so_phong_gia_dinh = 4
print("Số phòng gia đình hiện có:", so_phong_gia_dinh)

# Kết thúc lời giải
```

#### Giải thích cách 1

Phép gán đưa tên `so_phong_gia_dinh` vào không gian tên của phiên làm việc. Khi chạy dòng `print`, Python tra cứu tên đó rồi truyền giá trị `4` cho hàm in. `print` ghép các đối số bằng một dấu cách theo mặc định, nên ta thấy nhãn và số trên cùng một dòng.

Thứ tự trên trang không quyết định trạng thái thực tế. Nếu chỉ chạy ô có `print` trong một phiên mới, Python chưa có tên biến và phát sinh `NameError`. Hãy chạy ô gán trước, rồi mới chạy ô đọc biến. Khởi động lại kernel xóa trạng thái của tiến trình cũ, nên cần chạy lại các ô khởi tạo.

#### Kết quả cách 1

```text
Số phòng gia đình hiện có: 4
```

#### Cách 2: Kiểm tra sự tồn tại của biến trong không gian tên với try và except

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải


def safe_access_variable(var_name: str, scope: dict) -> object:
    """Truy xuất biến an toàn kèm xử lý ngoại lệ NameError khi biến chưa tồn tại.

    Tham số var_name: Tên biến cần tra cứu.
    Tham số scope: Không gian tên (namespace) dùng để tra cứu biến.
    """
    try:
        if var_name not in scope:
            raise NameError(
                f"Biến '{var_name}' chưa được định nghĩa trong phiên làm việc."
            )
        return scope[var_name]
    except NameError as error:
        print(f"Bắt ngoại lệ thành công: {error}")
        return None


khong_gian_ten = {"so_phong_gia_dinh": 4}
ket_qua = safe_access_variable("so_phong_gia_dinh", khong_gian_ten)
print(f"Giá trị truy xuất: {ket_qua}")

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm nhận tên cần tìm ở `var_name` và một từ điển tra cứu ở `scope`. Biểu thức `var_name not in scope` kiểm tra khóa, còn `scope[var_name]` lấy giá trị. Ví dụ truyền một từ điển tự tạo chứa giá trị `4`, vì vậy hàm trả về `4` và không đi vào nhánh xử lý lỗi.

Nếu khóa vắng mặt, `raise NameError(...)` chủ động tạo ngoại lệ để khối `except NameError as error` bắt lại, in thông báo và trả về `None`. Đây là phép tra cứu trên từ điển được truyền vào, không tự quét mọi phạm vi của Python. Khi Python tra cứu một tên thông thường, phạm vi tích hợp sẵn cũng có thể được xét sau các phạm vi cục bộ, bao quanh và toàn cục.

#### Kết quả cách 2

```text
Giá trị truy xuất: 4
```

#### So sánh hai cách

Cách 1 giải quyết việc phụ thuộc giữa các ô bằng thứ tự chạy. Cách 2 minh họa cách tra cứu một tên và phản hồi khi tên vắng mặt. Hàm tra cứu không thay thế việc khởi tạo đúng dữ liệu và không làm notebook tự chạy những ô bị bỏ qua.

:::

---

<span id="data-lab-01-02"></span>
### Bài 2: Trạng thái tích lũy của biến trong tiến trình tính toán

::: exercise
Thực hiện thí nghiệm quan sát tính cộng dồn của biến trạng thái khi một ô mã nguồn được chạy lặp lại nhiều lần. Đối chiếu giá trị của biến đếm trong hai tình huống: Chạy một ô tăng biến 3 lần liên tiếp và chạy toàn bộ từ đầu đến cuối (Restart session and Run all).

Yêu cầu kỹ thuật:
- Đầu vào: Biến đếm `dem` khởi tạo bằng `0`, ô tăng biến thực hiện phép toán `dem = dem + 1`.
- Thao tác: Dự đoán chính xác giá trị của `dem` sau khi kích hoạt ô tăng biến 3 lần. Tiếp theo, dự đoán giá trị của `dem` khi người dùng chọn lệnh `Restart & Run all`.
- Đầu ra: Hai số nguyên đại diện cho kết quả dự đoán `du_doan_3_lan` và `du_doan_run_all`.
- Trường hợp biên: Tránh nhầm lẫn giữa việc chạy lại một ô đơn lẻ với việc khởi động lại toàn bộ tiến trình.
:::

::: solution
#### Cách 1: Ghi nhận kết quả dự đoán thủ công qua việc theo dõi phiên chạy

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải

dem = 0
for _ in range(3):
    dem += 1
du_doan_3_lan = dem

dem_run_all = 0
dem_run_all += 1
du_doan_run_all = dem_run_all

print(f"Sau 3 lần chạy cell tăng: {du_doan_3_lan}")
print(f"Sau khi Restart và chạy lại toàn bộ: {du_doan_run_all}")

# Kết thúc lời giải
```

#### Giải thích cách 1

`dem = 0` tạo trạng thái ban đầu. `range(3)` sinh ba lượt lặp, và mỗi lượt `dem += 1` lấy giá trị hiện tại cộng thêm một. Vì thế chuỗi giá trị lần lượt là `1`, `2`, `3`. Biến `du_doan_3_lan` giữ kết quả sau cả ba lượt.

Phần sau dùng biến mới `dem_run_all`, khởi tạo lại từ `0` và chỉ tăng một lần. Hai biến riêng giúp thấy rõ hai kịch bản. Trong notebook thực tế, chạy lại riêng ô tăng dùng tiếp trạng thái hiện có, còn Restart rồi Run all bắt đầu từ trạng thái sạch và chạy mỗi ô một lần.

#### Kết quả cách 1

```text
Sau 3 lần chạy cell tăng: 3
Sau khi Restart và chạy lại toàn bộ: 1
```

#### Cách 2: Lập trình hàm mô phỏng cơ chế lưu trữ trạng thái của kernel

```python
# Dữ liệu mẫu và các hàm hỗ trợ

# Bắt đầu lời giải


def simulate_counter(num_runs: int, reset_initial: bool = False) -> int:
    """Mô phỏng cơ chế lưu trạng thái biến tích lũy của kernel qua nhiều lần thực thi.

    Tham số num_runs: Số lượt thực thi cell tăng biến.
    Tham số reset_initial: Cờ tái khởi động trạng thái bộ nhớ về 0.
    """
    counter_state = 0
    for _ in range(num_runs):
        counter_state += 1
    return counter_state


ket_qua_3_lan = simulate_counter(3)
ket_qua_run_all = simulate_counter(1)
print(f"Mô phỏng 3 lượt: {ket_qua_3_lan} | Mô phỏng một lượt sạch: {ket_qua_run_all}")

# Kết thúc lời giải
```

#### Giải thích cách 2

`simulate_counter` nhận `num_runs` là số lượt tăng và trả về một số nguyên. Biến `counter_state` nằm trong thân hàm, được tạo lại với giá trị `0` mỗi lần gọi. Do đó `simulate_counter(3)` trả về `3`, còn lời gọi độc lập `simulate_counter(1)` trả về `1`.

Vòng `for _ in range(num_runs)` không sử dụng số thứ tự của từng lượt, nên đặt tên `_` cho biến lặp. Hàm mô phỏng số lần tăng trong một lần gọi, không tự lưu trạng thái giữa các lần gọi. Muốn mô phỏng một kernel duy trì trạng thái, phải truyền trạng thái cũ vào hoặc giữ nó trong một đối tượng riêng.

#### Kết quả cách 2

```text
Mô phỏng 3 lượt: 3 | Mô phỏng một lượt sạch: 1
```

#### So sánh hai cách

Cách 1 thể hiện hai tình huống bằng những biến cụ thể. Cách 2 cho phép đổi số lượt chạy qua đối số để thử thêm tình huống. Việc đặt phép tính trong hàm giúp kiểm tra độc lập, không phải một tối ưu về tốc độ.

:::

---

<span id="data-lab-01-03"></span>
### Bài 3: Đọc kích thước bảng và xác định nhóm chiếm đa số

::: exercise
Nạp dữ liệu danh sách chỗ ở vào cấu trúc bảng `DataFrame` của thư viện pandas. Hãy trích xuất tổng số lượng bản ghi (số dòng) và xác định tên loại phòng xuất hiện với tần suất lớn nhất trong bảng dữ liệu đang sử dụng.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi dữ liệu phân tách bằng dấu phẩy `DEMO_CSV` chứa 6 dòng chỗ ở mẫu.
- Thao tác: Sử dụng `pd.read_csv()` để chuyển đổi văn bản sang DataFrame. Dùng thuộc tính `shape` để lấy số dòng và phương thức `value_counts()` trên cột `room_type`.
- Đầu ra: Biến số nguyên `so_dong` và biến chuỗi `loai_nhieu_nhat`.
- Trường hợp biên: Trường hợp bảng rỗng không có dòng nào hoặc nhiều loại phòng có cùng số lượng cao nhất.
:::

::: solution
#### Cách 1: Sử dụng các thuộc tính và phương thức cơ bản của pandas

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

# Bắt đầu lời giải

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))
so_dong = ds.shape[0]
dem_loai = ds["room_type"].value_counts()
loai_nhieu_nhat = dem_loai.idxmax()

print(f"Tổng số dòng: {so_dong}")
print(f"Loại phòng phổ biến nhất: {loai_nhieu_nhat}")

# Kết thúc lời giải
```

#### Giải thích cách 1

`StringIO(DEMO_CSV)` biến chuỗi CSV thành một đối tượng đọc được giống tệp. `pd.read_csv` đọc dòng tiêu đề thành tên cột và sáu dòng sau thành DataFrame. `ds.shape` là bộ `(6, 7)`, nên `ds.shape[0]` cho số dòng `6`.

`ds["room_type"]` chọn một cột dưới dạng Series. `value_counts()` đếm từng loại và mặc định sắp xếp giảm dần theo số lượng, bỏ qua giá trị thiếu. Series đếm có các nhãn là tên loại phòng. `idxmax()` trả về nhãn gắn với số đếm lớn nhất, chứ không trả về chính số đếm. Mẫu có bốn nguyên căn và hai phòng riêng, nên đáp án là `Entire home/apt`.

#### Kết quả cách 1

```text
Tổng số dòng: 6
Loại phòng phổ biến nhất: Entire home/apt
```

#### Cách 2: Xây dựng hàm trích xuất hồ sơ bảng có kiểm tra ca biên

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

# Bắt đầu lời giải


def get_table_profile(df: pd.DataFrame, category_col: str) -> dict:
    """Hồ sơ hóa kích thước bảng và nhận diện danh mục chiếm tỷ trọng lớn nhất.

    Tham số df: Bảng dữ liệu pandas DataFrame.
    Tham số category_col: Tên cột danh mục cần đếm tần suất.
    """
    total_rows = len(df)
    if total_rows == 0 or category_col not in df.columns:
        return {"total_rows": 0, "top_category": None, "frequency": 0}
    counts = df[category_col].value_counts()
    if counts.empty:
        return {"total_rows": total_rows, "top_category": None, "frequency": 0}
    top_name = str(counts.index[0])
    top_count = int(counts.iloc[0])
    return {"total_rows": total_rows, "top_category": top_name, "frequency": top_count}


thong_tin = get_table_profile(ds, "room_type")
print(f"Hồ sơ bảng: {thong_tin}")

# Kết thúc lời giải
```

#### Giải thích cách 2

Hàm `get_table_profile(df, category_col)` đóng gói số dòng, nhóm đứng đầu và tần suất vào một từ điển. `len(df)` đếm dòng. Với cột có dữ liệu, `counts.index[0]` lấy tên nhóm đầu tiên và `counts.iloc[0]` lấy số đếm tại vị trí đầu tiên. Ép qua `str` và `int` làm rõ kiểu của hai giá trị trả về.

Nhánh `counts.empty` xử lý cột toàn giá trị thiếu. Việc kiểm tra trước khi lấy phần tử đầu tránh lỗi truy cập Series rỗng. Với nhiều nhóm hòa điểm, đoạn mã chọn nhóm đứng đầu Series đếm. Nếu ứng dụng cần quy tắc hòa điểm cố định theo tên, phải sắp xếp thêm theo tên thay vì suy ra từ tần suất.

#### Kết quả cách 2

```text
Hồ sơ bảng: {'total_rows': 6, 'top_category': 'Entire home/apt', 'frequency': 4}
```

| room_type | Số dòng |
| --- | --- |
| Entire home/apt | 4 |
| Private room | 2 |

#### So sánh hai cách

Cách 1 phù hợp để đọc trực tiếp một bảng đã biết cấu trúc. Cách 2 tạo kết quả có tên trường để dùng trong báo cáo và bổ sung các nhánh xử lý dữ liệu thiếu. Chúng dùng cùng phép đếm, nên không có cơ sở kết luận cách đóng gói thành hàm chạy nhanh hơn.

:::

---

<span id="data-lab-01-04"></span>
### Bài 4: Tính tỷ lệ phần trăm theo nhóm và làm tròn số thập phân

::: exercise
Từ Series số lượng `dem_loai` đã tính ở Bài 3, hãy lập trình tính toán Series `ty_le` biểu diễn tỷ lệ phần trăm (thang đo từ 0 đến 100) của từng loại phòng. Kết quả phải được làm tròn đến đúng 1 chữ số thập phân.

Yêu cầu kỹ thuật:
- Đầu vào: Series `dem_loai` chứa số lượng phòng theo từng loại.
- Thao tác: Lấy từng phần tử chia cho tổng số quan sát, nhân với 100, sau đó gọi phương thức làm tròn `round(1)`.
- Đầu ra: Đối tượng `pd.Series` có chỉ mục giữ nguyên tên loại phòng và giá trị là số thực phần trăm.
- Trường hợp biên: Tổng tỷ lệ cộng lại phải nằm trong khoảng cho phép từ 99.5% đến 100.5% để xử lý sai số làm tròn số học.
:::

::: solution
#### Cách 1: Tính toán bằng biểu thức vector hóa trực tiếp

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

dem_loai = ds["room_type"].value_counts()

# Bắt đầu lời giải

# Tính toán tỷ lệ phần trăm trực tiếp trên Series đếm tần suất
ty_le = (dem_loai / dem_loai.sum() * 100).round(1)
print("Tỷ lệ phần trăm theo loại phòng:")
print(ty_le)

# Kết thúc lời giải
```

#### Giải thích cách 1

`dem_loai.sum()` cộng hai tần suất để có tổng `6`. Phép chia Series cho số `6` áp dụng cho từng nhóm mà vẫn giữ chỉ mục tên loại phòng. Nhân `100` đổi tỷ lệ trên thang 0–1 thành phần trăm trên thang 0–100.

`round(1)` tạo Series kết quả với mỗi giá trị làm tròn một chữ số thập phân. Bốn trên sáu dòng thành `66.7`, còn hai trên sáu thành `33.3`. Các giá trị vẫn là số thực, không phải chuỗi có dấu `%`. Chỉ thêm ký hiệu phần trăm khi trình bày để tránh làm mất khả năng tính toán tiếp.

#### Kết quả cách 1

| room_type | Tỷ lệ (%) |
| --- | --- |
| Entire home/apt | 66.7 |
| Private room | 33.3 |

#### Cách 2: Đóng gói hàm tính toán an toàn có kiểm tra mẫu số

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

dem_loai = ds["room_type"].value_counts()

# Bắt đầu lời giải


def calculate_percentages(counts: pd.Series, decimals: int = 1) -> pd.Series:
    """Tính toán phân phối tỷ lệ phần trăm từ Series tần suất với kiểm tra mẫu số an toàn.

    Tham số counts: Series chứa số lượng quan sát của từng nhóm.
    Tham số decimals: Số chữ số làm tròn sau dấu phẩy thập phân.
    """
    if not isinstance(counts, pd.Series):
        raise TypeError("Đầu vào phải là một đối tượng pandas Series.")
    total_observations = counts.sum()
    if total_observations == 0:
        return pd.Series(0.0, index=counts.index, dtype=float)
    percentages = (counts / total_observations) * 100.0
    return percentages.round(decimals)


ty_le_chuan = calculate_percentages(dem_loai, decimals=1)
print(f"Kết quả tỷ lệ chuẩn hóa:\n{ty_le_chuan}")

# Kết thúc lời giải
```

#### Giải thích cách 2

`calculate_percentages` nhận Series tần suất ở `counts` và số chữ số làm tròn ở `decimals`. `isinstance(counts, pd.Series)` kiểm tra loại đối tượng trước khi gọi các phương thức của Series. Nếu tổng tần suất bằng `0`, hàm trả Series số `0.0` với cùng chỉ mục, tránh tạo kết quả chia cho không.

Ở nhánh còn lại, hàm tính từng tỷ lệ bằng cùng biểu thức của Cách 1 và gọi `round(decimals)`. Đối số `decimals=1` trong lời gọi cho đúng mức làm tròn của đề. Hàm giả định các tần suất không âm. Với nhiều nhóm, tổng các tỷ lệ đã làm tròn có thể lệch khỏi `100`, nên cần kiểm tra quy tắc làm tròn theo số nhóm thay vì coi tổng luôn chính xác.

#### Kết quả cách 2

| room_type | Tỷ lệ (%) |
| --- | --- |
| Entire home/apt | 66.7 |
| Private room | 33.3 |

#### So sánh hai cách

Cách 1 ngắn và trực diện trên một Series hợp lệ. Cách 2 phù hợp khi nhận dữ liệu từ nhiều nơi vì có kiểm tra kiểu và quy ước khi tổng bằng không. Cả hai trả cùng phần trăm trên mẫu đang xét.

:::

---

<span id="data-lab-01-05"></span>
### Bài 5: Trực quan hóa phân phối tần suất bằng biểu đồ thanh ngang

::: exercise
Thực hiện vẽ biểu đồ thanh ngang (horizontal bar chart) trực quan hóa số lượng chỗ ở theo từng loại phòng từ Series `dem_loai`. Biểu đồ cần được sắp xếp theo thứ tự tăng dần từ dưới lên trên để nhóm chiếm đa số hiển thị nổi bật ở vị trí cao nhất.

Yêu cầu kỹ thuật:
- Đầu vào: Series `dem_loai`.
- Thao tác: Gọi phương thức sắp xếp `sort_values()` và vẽ đồ thị thanh ngang thông qua `plot.barh()`.
- Đầu ra: Hình vẽ matplotlib hoàn chỉnh có tiêu đề, nhãn trục hoành và nhãn trục tung rõ ràng.
- Trường hợp biên: Kiểm soát kích thước hình vẽ vừa vặn, không để chữ tràn ra ngoài viền lề.
:::

::: solution
#### Cách 1: Sử dụng phương thức vẽ đồ thị tích hợp của pandas

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

dem_loai = ds["room_type"].value_counts()

# Bắt đầu lời giải

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(6, 3))
dem_loai.sort_values().plot.barh(ax=ax, color="#1E93AB")
ax.set_title("Số lượng chỗ ở theo loại phòng")
ax.set_xlabel("Số lượng chỗ ở")
ax.set_ylabel("Loại phòng")
fig.tight_layout()

# Kết thúc lời giải

plt.show()
```

#### Giải thích cách 1

`plt.subplots(figsize=(6, 3))` trả về một hình `fig` và một hệ trục `ax`, với kích thước tính bằng inch. `sort_values()` sắp số đếm tăng dần trước khi `plot.barh(ax=ax, ...)` vẽ thanh ngang trên hệ trục đã tạo.

Vị trí đầu tiên của thanh ngang nằm dưới cùng, nên phòng riêng có số đếm `2` ở dưới và nguyên căn có số đếm `4` ở trên. `set_title`, `set_xlabel`, `set_ylabel` đặt tiêu đề và đơn vị đọc trục. `fig.tight_layout()` điều chỉnh khoảng cách để nhãn vừa trong hình. Trong notebook, hình được hiển thị ở đầu ra ô mã, không phải bảng văn bản.

#### Kết quả cách 1

Biểu đồ có hai thanh. Bảng sau ghi đúng dữ liệu và thứ tự của các thanh để đối chiếu với hình:

| Vị trí thanh | Loại phòng | Độ dài |
| --- | --- | --- |
| Dưới | Private room | 2 |
| Trên | Entire home/apt | 4 |

#### Cách 2: Tùy biến biểu đồ qua giao diện hướng đối tượng của matplotlib

```python
# Dữ liệu mẫu và các hàm hỗ trợ

import matplotlib.pyplot as plt

DEMO_CSV = (
    "id,name,neighbourhood,room_type,price,number_of_reviews,last_review\n"
    "1,Phong A,Centro,Entire home/apt,100,0,\n"
    "2,Phong B,Centro,Private room,50,2,2026-05-10\n"
    "3,Phong C,Norte,Entire home/apt,,0,\n"
    "4,Phong D,Norte,Entire home/apt,150,1,2026-06-01\n"
    "5,Phong E,Sur,Private room,0,3,2026-05-30\n"
    "6,Phong F,Sur,Entire home/apt,300,2,2026-06-10\n"
)

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

dem_loai = ds["room_type"].value_counts()

# Bắt đầu lời giải


def plot_horizontal_distribution(
    counts: pd.Series, title: str, xlabel: str, ylabel: str
):
    """Vẽ biểu đồ thanh ngang kèm nhãn số liệu trực tiếp trên từng thanh.

    Tham số counts: Series chứa số lượng từng nhóm.
    Tham số title: Tiêu đề biểu đồ.
    Tham số xlabel, ylabel: Nhãn các trục tọa độ.
    """
    sorted_counts = counts.sort_values()
    fig, ax = plt.subplots(figsize=(7, 3.2))
    bars = ax.barh(
        sorted_counts.index, sorted_counts.values, color="#1E93AB", edgecolor="none"
    )
    ax.bar_label(bars, padding=4, fmt="%d", fontsize=9)
    ax.set_title(title, fontsize=11, fontweight="bold", pad=10)
    ax.set_xlabel(xlabel, fontsize=10)
    ax.set_ylabel(ylabel, fontsize=10)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    return fig, ax


fig, ax = plot_horizontal_distribution(
    dem_loai,
    title="Phân bố cơ cấu loại phòng chỗ ở",
    xlabel="Số lượng chỗ ở",
    ylabel="Loại phòng",
)

# Kết thúc lời giải

plt.show()
```

#### Giải thích cách 2

Hàm nhận Series đếm cùng ba chuỗi dùng làm tiêu đề và nhãn trục. `ax.barh(sorted_counts.index, sorted_counts.values, ...)` truyền tường minh tên nhóm cho trục dọc và số lượng cho chiều dài thanh. Giá trị trả về `bars` là tập các hình chữ nhật dùng để gắn nhãn.

`ax.bar_label(bars, padding=4, fmt="%d")` in số nguyên ở đầu thanh và đặt nhãn cách thanh bốn điểm. `ax.spines[...]` truy cập đường viền của hệ trục, còn `set_visible(False)` ẩn hai viền trên và phải. Hàm trả `(fig, ax)` để nơi gọi tiếp tục lưu hình hoặc điều chỉnh trục. Hàm không tính lại tần suất và không đổi dữ liệu đếm.

#### Kết quả cách 2

Các nhãn `2` và `4` xuất hiện ngay cạnh đầu thanh:

| Vị trí thanh | Loại phòng | Độ dài |
| --- | --- | --- |
| Dưới | Private room | 2 |
| Trên | Entire home/apt | 4 |

#### So sánh hai cách

Cách 1 dùng pandas để chuyển Series thành hình với ít thao tác. Cách 2 dùng giao diện đối tượng của Matplotlib để điều chỉnh nhãn và đường viền. Khác biệt nằm ở khả năng trình bày và tái sử dụng, không ở kết quả đếm.

:::

---

<span id="data-lab-01-06"></span>
### Bài 6: Đóng gói hàm phân tích tùy biến theo cấu trúc bảng kết quả

::: exercise
Viết hàm `analyze_question(data: pd.DataFrame) -> dict` nhận bảng chỗ ở và trả một từ điển gồm đúng ba khóa. Trường `question` là chuỗi câu hỏi, `table` là DataFrame kết quả và `unit` là chuỗi đơn vị. Bảng kết quả phải có ít nhất một cột, các tên cột là chuỗi không rỗng và không trùng nhau.

Yêu cầu kỹ thuật:
- Đầu vào: DataFrame `data` chứa các cột như `neighbourhood`, `room_type`, `price`, `number_of_reviews`.
- Thao tác: Lựa chọn câu hỏi thực tế (ví dụ: Quận nào sở hữu số lượng chỗ ở nhiều nhất?). Tổng hợp số liệu từ tham số `data`, tuyệt đối không đọc biến toàn cục bên ngoài và không chỉnh sửa dữ liệu gốc tại chỗ (in-place mutation).
- Đầu ra: Từ điển chứa đúng ba khóa `{"question": str, "table": pd.DataFrame, "unit": str}`.
- Trường hợp biên: Khi đầu vào là DataFrame rỗng 0 dòng `data.iloc[:0]`, hàm phải trả về bảng kết quả 0 dòng nhưng phải bảo toàn đầy đủ các cột đã định nghĩa.
:::

::: solution
#### Cách 1: Sử dụng value_counts và reset_index định danh cột

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

# Bắt đầu lời giải


def analyze_question(data: pd.DataFrame) -> dict:
    """Phân tích số lượng chỗ ở theo từng quận huyện từ dữ liệu bảng.

    Cột bảng kết quả:
    - neighbourhood (str): Tên khu vực hành chính.
    - count (int): Số lượng chỗ ở ghi nhận.
    """
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Dữ liệu đầu vào phải là một pandas DataFrame.")
    if data.empty or "neighbourhood" not in data.columns:
        empty_table = pd.DataFrame(columns=["neighbourhood", "count"])
        return {
            "question": "Quận nào sở hữu số lượng chỗ ở niêm yết nhiều nhất?",
            "table": empty_table,
            "unit": "chỗ ở",
        }
    counts = data["neighbourhood"].value_counts().reset_index()
    counts.columns = ["neighbourhood", "count"]
    return {
        "question": "Quận nào sở hữu số lượng chỗ ở niêm yết nhiều nhất?",
        "table": counts,
        "unit": "chỗ ở",
    }


ket_qua_e1 = analyze_question(ds)
print(f"Câu hỏi: {ket_qua_e1['question']} | Đơn vị: {ket_qua_e1['unit']}")
print(ket_qua_e1["table"])

# Kết thúc lời giải
```

#### Giải thích cách 1

`analyze_question` nhận bảng ở tham số `data`, kiểm tra đây là DataFrame rồi đếm cột `neighbourhood`. `value_counts()` tạo Series mà chỉ mục là khu vực. `reset_index()` đưa chỉ mục đó thành cột, và phép gán `counts.columns` đặt đúng hai tên cột yêu cầu.

Từ điển trả về tách ba vai trò. Trường `question` nói bảng trả lời câu hỏi gì, `table` chứa số liệu có thể tính tiếp, và `unit` ghi đơn vị. Nhánh bảng rỗng tạo DataFrame có hai tên cột nhưng không có dòng. Không thêm một dòng toàn giá trị thiếu để giả làm bảng rỗng.

#### Kết quả cách 1

| neighbourhood | count |
| --- | --- |
| Centro | 2 |
| Norte | 2 |
| Sur | 2 |

`unit` bằng `"chỗ ở"`. Nếu truyền `ds.iloc[:0]`, kết quả `table.shape` là `(0, 2)` với hai cột `neighbourhood`, `count`.

#### Cách 2: Nhóm dữ liệu với groupby và tạo bản sao bảo vệ dữ liệu gốc

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

# Bắt đầu lời giải


def analyze_question(data: pd.DataFrame) -> dict:
    """Phân tích tổng hợp số chỗ ở theo quận kèm kiểm soát tính toàn vẹn dữ liệu.

    Bảo đảm không sửa đổi đối số truyền vào và duy trì cấu trúc cột nhất quán.
    """
    cols = ["neighbourhood", "count"]
    if not isinstance(data, pd.DataFrame):
        raise TypeError("Đối số data phải là pandas DataFrame.")
    if data.empty:
        return {
            "question": "Số lượng chỗ ở phân bổ theo từng khu vực địa lý là bao nhiêu?",
            "table": pd.DataFrame(columns=cols),
            "unit": "chỗ ở",
        }
    # Sử dụng bản sao để không làm biến đổi dữ liệu truyền vào
    working_df = data.copy(deep=False)
    summary = (
        working_df.groupby("neighbourhood", as_index=False)
        .size()
        .rename(columns={"size": "count"})
        .sort_values(by="count", ascending=False)
        .reset_index(drop=True)
    )
    return {
        "question": "Số lượng chỗ ở phân bổ theo từng khu vực địa lý là bao nhiêu?",
        "table": summary[cols],
        "unit": "chỗ ở",
    }


ket_qua_nang_cao = analyze_question(ds)
print(ket_qua_nang_cao["table"].head(3))

# Kết thúc lời giải
```

#### Giải thích cách 2

`groupby("neighbourhood", as_index=False).size()` đếm số dòng trong mỗi nhóm và giữ tên nhóm ở một cột thông thường. `rename(columns={"size": "count"})` đổi tên cột đếm. `sort_values(..., ascending=False)` xếp nhóm đông hơn trước, rồi `reset_index(drop=True)` tạo chỉ mục dòng liên tiếp và bỏ chỉ mục cũ.

Các phép tổng hợp này tạo bảng kết quả thay vì gán lại cột của đầu vào. `copy(deep=False)` tạo một đối tượng DataFrame khác nhưng không mặc nhiên sao chép mọi vùng dữ liệu. Vì thế lý do dữ liệu gốc được giữ nguyên trong hàm này là không có thao tác sửa nó. Hàm trả đúng ba trường và chọn lại `summary[cols]` để khóa thứ tự cột.

#### Kết quả cách 2

| neighbourhood | count |
| --- | --- |
| Centro | 2 |
| Norte | 2 |
| Sur | 2 |

Ba khu vực đều có hai dòng. Vì hòa điểm, bảng này chưa cho một khu vực đứng đầu duy nhất.

#### So sánh hai cách

Cách 1 diễn đạt trực tiếp thao tác đếm một cột. Cách 2 đưa cùng phép đếm vào quy trình nhóm dữ liệu, thuận tiện nếu sau này cần thêm tổng hay trung vị. Bảng có sáu dòng vẫn cho ba nhóm bằng nhau, nên không nên diễn giải rằng một khu vực có nguồn cung lớn nhất riêng biệt.

:::

---

<span id="data-lab-01-07"></span>
### Bài 7: Phân tích suy luận: Tỷ lệ niêm yết so với lượt đặt phòng và giới hạn dữ liệu giả lập

::: exercise
Thực hiện phân tích bản chất kinh tế và suy luận thống kê từ dữ liệu. Hãy giải thích rõ hai nội dung:
1. Vì sao tỷ lệ chỗ ở niêm yết (listings) trên nền tảng không đồng nhất với tỷ lệ lượt đặt phòng thành công thực tế (bookings)?
2. Vì sao tuyệt đối không được sử dụng các con số tính toán từ tập dữ liệu giả lập 6 dòng để kết luận về thị trường du lịch Santiago?

Yêu cầu kỹ thuật:
- Đầu vào: Số liệu quan sát từ bảng chỗ ở và các cột liên quan đến hoạt động như `number_of_reviews` và `last_review`.
- Thao tác: Xây dựng khung so sánh định tính và định lượng giữa chỉ số nguồn cung tĩnh (stock) và chỉ số dòng giao dịch động (flow).
- Đầu ra: Ma trận phân tích đối chiếu rõ ràng các yếu tố tác động và mã nguồn kiểm tra tính hoạt động của các phòng.
- Ranh giới kiểm chứng: Phân biệt rõ dữ liệu mẫu kiểm thử phục vụ xác thực kỹ thuật với dữ liệu khảo sát thực địa diện rộng.
:::

::: solution
#### Cách 1: Phân tích định tính cấu trúc thị trường và bản chất biến số

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

# Bắt đầu lời giải

# Ma trận phân tích sự khác biệt giữa nguồn cung niêm yết và giao dịch thực tế
bang_so_sanh = [
    {
        "Tieu_chi": "Bản chất khái niệm",
        "Niem_yet_Listings": "Nguồn cung tiềm năng (Stock)",
        "Dat_phong_Bookings": "Giao dịch phát sinh thực tế (Flow)",
    },
    {
        "Tieu_chi": "Mức độ hoạt động",
        "Niem_yet_Listings": "Bao gồm cả bài đăng cũ hoặc không nhận khách",
        "Dat_phong_Bookings": "Có khách lưu trú và thanh toán thành công",
    },
    {
        "Tieu_chi": "Chỉ số thay thế",
        "Niem_yet_Listings": "Tổng số dòng trong listings.csv",
        "Dat_phong_Bookings": "Số đánh giá mới hoặc lịch kín phòng",
    },
]
df_so_sanh = pd.DataFrame(bang_so_sanh)
print(df_so_sanh)

# Kết thúc lời giải
```

#### Giải thích cách 1

Danh sách `bang_so_sanh` gồm ba từ điển, mỗi từ điển là một dòng mô tả. `pd.DataFrame(bang_so_sanh)` ghép các khóa thành tên cột và các giá trị thành ô. Bảng đặt hai đại lượng cạnh nhau để thấy đơn vị đếm khác nhau: Niêm yết đếm bài đăng chỗ ở, còn đặt phòng đếm giao dịch trong một khoảng thời gian.

Đây là bảng khái niệm, không phải phép đo số giao dịch. Một niêm yết có thể nhận nhiều lượt đặt hoặc chưa nhận lượt nào. Ngày bị chặn trên lịch và số đánh giá cũng không đồng nhất với số lượt đặt phòng. Muốn ước lượng giao dịch từ các chỉ số gián tiếp phải nêu thêm giả định và kiểm chứng chúng.

#### Kết quả cách 1

| Tieu_chi | Niem_yet_Listings | Dat_phong_Bookings |
| --- | --- | --- |
| Bản chất khái niệm | Nguồn cung tiềm năng (Stock) | Giao dịch phát sinh thực tế (Flow) |
| Mức độ hoạt động | Bao gồm cả bài đăng cũ hoặc không nhận khách | Có khách lưu trú và thanh toán thành công |
| Chỉ số thay thế | Tổng số dòng trong listings.csv | Số đánh giá mới hoặc lịch kín phòng |

#### Cách 2: Lập trình kiểm tra chỉ số thay thế về mức độ hoạt động thực tế

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

from io import StringIO
import pandas as pd

ds = pd.read_csv(StringIO(DEMO_CSV))

# Bắt đầu lời giải


def kiem_tra_hoat_dong(df: pd.DataFrame) -> dict:
    """Đánh giá sơ bộ tỷ lệ phòng có dấu hiệu hoạt động dựa trên chỉ số đánh giá.

    Tham số df: Bảng dữ liệu chỗ ở chứa các cột đánh giá.
    """
    tong_so = len(df)
    if tong_so == 0:
        return {"tong_phong": 0, "ty_le_chua_danh_gia": 0.0}
    # Lọc các dòng có 0 review
    chua_danh_gia = df[df["number_of_reviews"].astype(str) == "0"]
    ty_le_trong = len(chua_danh_gia) / tong_so * 100.0
    return {
        "tong_phong": tong_so,
        "so_phong_chua_danh_gia": len(chua_danh_gia),
        "ty_le_chua_danh_gia": round(ty_le_trong, 1),
    }


bao_cao_hoat_dong = kiem_tra_hoat_dong(ds)
print(f"Báo cáo sơ bộ hoạt động: {bao_cao_hoat_dong}")

# Kết thúc lời giải
```

#### Giải thích cách 2

`kiem_tra_hoat_dong` nhận bảng và dùng `len(df)` làm mẫu số. `astype(str)` chuyển cột số đánh giá sang chuỗi để so sánh với `"0"` trong ví dụ. Mặt nạ chọn hai dòng có mã `1` và `3`, nên số dòng chưa có đánh giá là `2` trên tổng `6`. `round(..., 1)` hiển thị phần trăm thành `33.3`.

Tên báo cáo không làm thay đổi giới hạn của dữ liệu. Không có đánh giá không chứng minh không có khách, và có đánh giá cũng không cho biết đầy đủ giao dịch. Tập sáu dòng được dựng để thử chương trình, không được dùng ước lượng thị trường Santiago. Khi bảng rỗng, hàm quy ước tỷ lệ bằng `0.0`, tức là giá trị xử lý kỹ thuật chứ không phải tỷ lệ thị trường đã đo.

#### Kết quả cách 2

| Trường | Giá trị |
| --- | --- |
| tong_phong | 6 |
| so_phong_chua_danh_gia | 2 |
| ty_le_chua_danh_gia | 33.3 |

#### So sánh hai cách

Cách 1 làm rõ câu hỏi có thể trả lời bằng từng loại dữ liệu. Cách 2 tính một chỉ số quan sát được là tỷ lệ dòng chưa có đánh giá. Hai phần bổ trợ nhau, nhưng không phải hai thuật toán thay thế để suy ra lượt đặt phòng. Không có phương pháp nào ở đây chứng minh quy mô giao dịch thực tế.

:::

---

## Tài liệu tham khảo

1. McKinney, W. (2022). *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter* (3rd ed.). O'Reilly Media.
2. Inside Airbnb. (2026). *Santiago Data Assumptions and Data Dictionary*. Inside Airbnb Open Data.
3. Kluyver, T., et al. (2016). *Jupyter Notebooks: A Publishing Format for Reproducible Computational Workflows*. Positioning and Power in Academic Publishing: Players, Agents and Agendas, pp. 87–90.
