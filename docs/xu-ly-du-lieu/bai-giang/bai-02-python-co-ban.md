---
course: xu-ly-du-lieu
lecture: bai-02-python-co-ban
section: lecture
title: "Python cơ bản cho xử lý dữ liệu"
prerequisites: ["bien-kieu","list","dictionary","vong-lap","ham-lap-trinh"]
lessonStatus: ready
description: "Chọn cấu trúc dữ liệu, viết hàm chuyển đổi và đọc tệp với cách xử lý lỗi rõ ràng."
---

Trước khi bắt tay vào các thư viện chuyên sâu như NumPy hay pandas, người kỹ sư dữ liệu cần làm chủ các công cụ sẵn có của Python. Bản thân Python cung cấp một hệ thống cấu trúc dữ liệu bản địa rất mạnh mẽ. Tuy nhiên, nếu không hiểu rõ cơ chế vận hành bên dưới của chúng trong bộ nhớ, ta rất dễ tạo ra những chương trình chạy chậm chạp, ngốn tài nguyên, hoặc nguy hiểm hơn là làm biến dạng dữ liệu một cách âm thầm.

Bài học này làm rõ những nền tảng cốt yếu nhất của Python dưới lăng kính kỹ thuật xử lý dữ liệu: cách chọn cấu trúc dữ liệu tối ưu, phân biệt rạch ròi giữa biến đổi và sàng lọc, cơ chế tham chiếu vùng nhớ và kỹ thuật đọc tệp phòng thủ.

## 1. Cấu trúc dữ liệu quyết định cơ chế tra cứu

Mỗi cấu trúc dữ liệu trong Python được thiết kế với sự đánh đổi riêng về bộ nhớ và tốc độ truy xuất. Chọn sai cấu trúc dữ liệu cho một thao tác thường xuyên có thể biến một chương trình xử lý mất 1 giây thành một chương trình chạy mất nhiều giờ đồng hồ.

| Cấu trúc | Bản chất bộ nhớ & Cơ chế tra cứu | Thao tác đặc trưng trong xử lý dữ liệu |
| :--- | :--- | :--- |
| **`list`** | Mảng động chứa các con trỏ, có thứ tự, truy cập theo chỉ số vị trí $O(1)$. Tìm kiếm giá trị bên trong đòi hỏi quét tuần tự $O(n)$. | Lưu giữ danh sách quan sát theo trình tự thời gian hoặc thứ tự dòng của tệp. |
| **`dict`** | Bảng băm (hash table) ánh xạ khóa sang giá trị. Tra cứu theo khóa có độ phức tạp trung bình $O(1)$. | Đại diện cho một bản ghi với các trường thông tin (khóa là tên cột, giá trị là ô dữ liệu). |
| **`set`** | Tập hợp các phần tử băm duy nhất, không có thứ tự và không cho phép trùng lặp. Phép kiểm tra phần tử `x in s` đạt $O(1)$. | Lọc trùng, kiểm tra mã danh mục hợp lệ và tính toán phép bù, phép giao giữa hai tập bản ghi. |
| **`tuple`** | Dãy phần tử bất biến (immutable). Khi đã khởi tạo, các con trỏ bên trong không thể thay đổi. | Đóng vai trò khóa phức hợp nhiều trường (composite key) hoặc đại diện cho tọa độ cố định. |

Hãy xem xét một ví dụ thực tế về danh sách hàng hóa:

```python
hang = [
    {"ma": "001", "gia": "24"},
    {"ma": "002", "gia": ""},
    {"ma": "003", "gia": "36"},
]
print(hang[0]["ma"])             # 001
print(hang[1:3])                 # hai dòng ở vị trí 1 và 2
print(hang[0].get("nhom", "chua_ro"))
truoc = {"001", "002", "003"}
sau = {"001", "003", "004"}
print(sorted(truoc - sau))       # ['002']
print(sorted(sau - truoc))       # ['004']
```

Đoạn mã trên minh họa ba quy tắc quan trọng:

1. **Mã số không phải là con số**: Mã hàng `"001"`, số căn cước công dân hay mã bưu chính dù chứa các chữ số nhưng bản chất ngữ nghĩa là **chuỗi định danh**. Nếu vội vã chuyển `"001"` thành số nguyên bằng `int()`, bạn sẽ nhận được số `1` và vĩnh viễn đánh mất hai số 0 ở đầu. Khi xử lý dữ liệu, nguyên tắc vàng là: *chỉ chuyển thành kiểu số những dữ liệu nào mà ta có nhu cầu thực hiện các phép toán cộng, trừ, nhân, chia trên đó*.
2. **Quy ước chỉ mục nửa mở**: Lát cắt `hang[1:3]` lấy phần tử ở chỉ số 1 và 2, nhưng dừng trước chỉ số 3. Quy ước khoảng nửa mở $[start, stop)$ này xuyên suốt toàn bộ hệ sinh thái Python, giúp việc tính độ dài lát cắt rất thuận tiện: $3 - 1 = 2$ phần tử.
3. **Tra cứu an toàn với `get()`**: Thay vì truy cập trực tiếp `hang[0]["nhom"]` vốn sẽ gây lỗi sập chương trình (`KeyError`) nếu trường `nhom` chưa tồn tại, phương thức `.get("nhom", "chua_ro")` cho phép ta định nghĩa một giá trị mặc định rõ ràng khi thiếu trường dữ liệu.

Khi cần đối chiếu hai danh sách mã sản phẩm để tìm xem mã nào đã bị xóa hoặc mã nào mới xuất hiện, việc ép kiểu danh sách sang `set` rồi sử dụng phép trừ tập hợp (`truoc - sau`) là cách làm chuẩn mực của các chuyên gia. Thao tác này vừa ngắn gọn, vừa đạt hiệu năng $O(n)$ thay vì mất $O(n^2)$ nếu dùng hai vòng lặp lồng nhau trên kiểu danh sách.

## 2. Phân định rạch ròi giữa biến đổi và sàng lọc

Khi nhận dữ liệu từ các biểu mẫu nhập liệu hoặc tệp văn bản, trường giá thường tồn tại dưới dạng chuỗi hỗn tạp: có khoảng trắng thừa, có ô để trống, có chuỗi `"N/A"`, và đôi khi có cả giá trị âm phi lý.

Một thói quen lập trình xấu là viết các đoạn mã gộp chung cả việc đọc dữ liệu, kiểm tra lỗi và tính toán thống kê vào cùng một vòng lặp. Cách tiếp cận của một kỹ sư chuyên nghiệp là tách bạch thành hai thao tác toán học riêng biệt: **Biến đổi** (Mapping/Transformation) và **Sàng lọc** (Filtering).

Ta đóng gói toàn bộ quy tắc nghiệp vụ của một trường dữ liệu vào một hàm chuyển đổi phòng thủ:

```python
def doc_gia(text):
    if text is None:
        return None
    if not isinstance(text, str):
        raise TypeError("Gia dau vao phai la chuoi hoac None")
    text = text.strip()
    if text == "":
        return None
    try:
        value = float(text)
    except ValueError:
        return None
    if not 0 <= value < float("inf"):
        return None
    return value

gia_da_doc = [doc_gia(row["gia"]) for row in hang]
gia_hop_le = [x for x in gia_da_doc if x is not None]
print(gia_da_doc)                # [24.0, None, 36.0]
print(sum(gia_hop_le) / len(gia_hop_le))  # 30.0
```

Hàm `doc_gia` trên thể hiện một triết lý xử lý ngoại lệ rất sâu sắc:

- **Phân biệt dữ liệu không hợp lệ với lỗi lập trình**: Khi dữ liệu đầu vào chứa chuỗi rỗng `""` hoặc `"N/A"`, đây là hiện tượng bình thường của dữ liệu thực tế, hàm nhẹ nhàng trả về `None` để ghi nhận sự khuyết thiếu. Ngược lại, nếu một đoạn mã khác truyền nhầm một số nguyên `18` vào hàm này, hàm lập tức ném ra ngoại lệ `TypeError`. Không bao giờ được dùng khối lệnh `except Exception: pass` một cách vô tội vạ, bởi nó sẽ nuốt chửng các lỗi sai kiểu dữ liệu và làm việc dò lỗi trở thành ác mộng.
- **Sàng lọc với `is not None`**: Trong bước lọc giá hợp lệ, ta viết tường minh `[x for x in gia_da_doc if x is not None]`. Nếu viết tắt thành `[x for x in gia_da_doc if x]`, chương trình sẽ vô tình loại bỏ cả giá trị `0.0`, bởi trong Python số 0 được đánh giá là `False`. Một món hàng có giá khuyến mãi 0 đồng là hoàn toàn hợp lệ và khác hẳn với một món hàng không rõ giá.

## 3. Hàm số, biểu thức ngắn và tính tái lập

Khi xử lý các tập dữ liệu lớn, việc trừu tượng hóa các phép tính thành hàm không chỉ giúp mã nguồn gọn gàng mà còn bảo đảm cùng một logic được áp dụng nhất quán trên mọi tệp.

```python
def gia_trung_binh(values):
    valid = [x for x in values if x is not None]
    return sum(valid) / len(valid) if valid else None

print(gia_trung_binh(gia_da_doc))
print(f"Gia trung binh: {gia_trung_binh(gia_da_doc):.1f} nghin dong")
cap = list(zip(["A", "B"], [24, 36], strict=True))
print(cap)                      # [('A', 24), ('B', 36)]
```

Hai kỹ thuật đáng lưu ý trong thực tế:

1. **Hàm `zip` với cờ `strict=True`**: Trong các phiên bản Python hiện đại (từ 3.10), hàm `zip` cung cấp tùy chọn `strict=True`. Bình thường, nếu bạn ghép hai danh sách có độ dài lệch nhau (ví dụ danh sách tên có 10 phần tử nhưng danh sách giá chỉ có 9 phần tử), `zip` mặc định sẽ âm thầm bỏ rơi phần tử cuối cùng của danh sách dài hơn. Cờ `strict=True` buộc chương trình phải dừng lại và báo lỗi `ValueError` ngay khi phát hiện độ dài hai mảng không khớp, ngăn chặn triệt để nguy cơ thất thoát dữ liệu ngầm.
2. **Khuôn mẫu định dạng chuỗi f-string**: Cú pháp `{gia_trung_binh(gia_da_doc):.1f}` cho phép ta làm tròn hiển thị số thực đến 1 chữ số thập phân một cách thanh lịch mà không làm thay đổi giá trị gốc được lưu trong bộ nhớ máy tính.

## 4. Cơ chế gắn nhãn đối tượng và cạm bẫy sao chép nông

Một trong những nguồn cơn gây ra nhiều lỗi kỳ quái nhất cho người học Python chính là sự ngộ nhận về toán tử gán `=`.

Trong Python, **biến không phải là một chiếc hộp chứa giá trị**. Biến thực chất chỉ là một **chiếc thẻ bài (name tag)** được dán lên một đối tượng đang nằm trong bộ nhớ.

```python
a = [24, 36]
b = a
b.append(60)
print(a)                        # [24, 36, 60]
c = a.copy()
c[0] = 99
print(a[0], c[0])               # 24 99
```

Khi ta thực hiện lệnh `b = a`, Python không tạo ra một bản sao danh sách nào cả. Hệ thống chỉ đơn thuần dán thêm chiếc nhãn `b` vào cùng một đối tượng danh sách mà `a` đang trỏ tới. Do đó, việc bạn thêm phần tử qua nhãn `b` sẽ hiển thị ngay lập tức khi bạn gọi nhãn `a`.

Phương thức `a.copy()` tạo ra một bản sao danh sách mới. Nhưng hãy hết sức cảnh giác: đây chỉ là **sao chép nông** (shallow copy). Phương thức này chỉ sao chép lớp danh sách bên ngoài. Các phần tử con bên trong nếu là kiểu dữ liệu khả biến (như từ điển `dict` hoặc danh sách khác) thì vẫn được trỏ chung.

Hãy quan sát tình huống sau:
```python
goc = [{"gia": 24}]
sao = goc.copy()
sao[0]["gia"] = 99
print(goc[0]["gia"])  # 99!
```

Dù `goc` và `sao` là hai danh sách khác nhau ở lớp ngoài, phần tử đầu tiên của cả hai lại cùng trỏ về một cuốn từ điển duy nhất. Khi cần sao chép độc lập toàn diện cả những cấu trúc lồng nhau phức tạp, ta phải sử dụng hàm `copy.deepcopy()` từ thư viện chuẩn `copy`.

## 5. Đọc và ghi tệp dữ liệu có cấu trúc

Khi làm việc với các tệp dữ liệu văn bản như CSV hay JSON, hai yêu cầu tối thượng là: bảo đảm tài nguyên hệ thống được giải phóng và kiểm soát chặt chẽ bảng mã ký tự.

```python
import csv
import json
from io import StringIO

csv_text = "ma,gia\n001,24\n002,\n003,36\n"
rows = list(csv.DictReader(StringIO(csv_text)))
print(rows[0]["gia"], type(rows[0]["gia"]).__name__)  # 24 str
json_text = json.dumps(rows, ensure_ascii=False)
assert json.loads(json_text) == rows
```

Khi làm việc với các tệp thật trên ổ cứng, hãy luôn tuân thủ các quy tắc sau:

1. **Quản lý ngữ cảnh với `with open()`**: Luôn mở tệp thông qua khối lệnh `with open(...) as f:`. Cấu trúc này bảo đảm tệp luôn được đóng đúng quy trình ngay khi khối lệnh kết thúc, kể cả khi xuất hiện ngoại lệ ở giữa chừng.
2. **Khai báo tường minh `encoding="utf-8"`**: Đặc biệt trên hệ điều hành Windows, nếu không chỉ định `encoding="utf-8"`, Python sẽ sử dụng bảng mã mặc định của hệ thống (như CP1252 hoặc CP1258). Điều này sẽ dẫn đến lỗi vỡ font chữ tiếng Việt hoặc ném ra ngoại lệ `UnicodeDecodeError` khi đọc các ký tự có dấu.
3. **Tham số `newline=""` cho tệp CSV**: Theo tài liệu chính thức của Python, khi làm việc với module `csv`, luôn truyền `newline=""` vào hàm `open()` để bộ đọc và bộ ghi của `csv` tự xử lý ký tự xuống dòng (`\n` hoặc `\r\n`) trên các nền tảng khác nhau một cách chuẩn xác.
4. **Tham số `ensure_ascii=False` cho JSON**: Khi xuất dữ liệu tiếng Việt sang JSON, tùy chọn này giúp các ký tự có dấu được lưu giữ tự nhiên dưới dạng văn bản đọc được thay vì bị biến thành các chuỗi thoát mã ASCII khó hiểu như `\u00e0`, `\u1ed9`.

## 6. Bài tập tự luyện

::: exercise Phân biệt lọc chân lý và lọc không rỗng
Giả sử danh sách giá chứa các phần tử `[0, None, 12]`. Hãy cho biết kết quả trả về của hai cách viết sau:
1. `[x for x in values if x]`
2. `[x for x in values if x is not None]`

Trong ngữ cảnh một chương trình bán hàng có mặt hàng tặng kèm miễn phí, cách viết nào là chính xác?
:::

::: solution
- Cách 1 (`if x`) chỉ giữ lại `[12]`, vì trong Python cả `None` lẫn số `0` đều có giá trị chân lý là `False`.
- Cách 2 (`if x is not None`) giữ lại cả `[0, 12]`.

Trong bài toán bán hàng có sản phẩm miễn phí (giá 0 đồng), cách thứ hai là cách viết chính xác. Số 0 là một giá trị định lượng có ý nghĩa thực tế, hoàn toàn khác biệt với sự thiếu thông tin (`None`).
:::

::: exercise Hệ quả của sao chép nông trên cấu trúc lồng nhau
Thực hiện đoạn mã sau:
```python
a = [{"gia": 24}]
b = a.copy()
b[0]["gia"] = 99
```
Giá trị của `a[0]["gia"]` lúc này là bao nhiêu? Giải thích cơ chế vùng nhớ bên dưới.
:::

::: solution
Giá trị `a[0]["gia"]` lúc này là **99**.

Lý do: Phương thức `a.copy()` thực hiện sao chép nông (shallow copy). Nó tạo ra một vùng nhớ danh sách mới cho `b`, nhưng các con trỏ phần tử bên trong danh sách `b` vẫn trỏ tới cùng đối tượng từ điển `{"gia": 24}` mà danh sách `a` đang trỏ. Khi ta sửa đổi trường `gia` thông qua `b[0]`, ta đang sửa trực tiếp nội dung của đối tượng từ điển dùng chung đó.
:::

::: exercise Kiểm tra phản xạ phòng thủ của hàm
Cho hàm `doc_gia` đã xây dựng ở mục 2. Hãy dự đoán kết quả trả về khi truyền lần lượt các đối số sau vào hàm:
`" 18.5 "`, `"N/A"`, `"-2"`, `"NaN"`, `None`, và số nguyên `18`.
:::

::: solution
Kết quả lần lượt là:
- `" 18.5 "` -> `18.5` (sau khi cắt khoảng trắng và ép kiểu sang float).
- `"N/A"` -> `None` (ném lỗi ValueError khi ép kiểu float và được khối except bắt lại để trả về None).
- `"-2"` -> `None` (ép kiểu thành -2.0 nhưng vi phạm điều kiện miền $0 \le value < \infty$).
- `"NaN"` -> `None` (float("NaN") không thỏa mãn điều kiện $0 \le value < \infty$ do NaN không thể so sánh thứ tự).
- `None` -> `None` (thỏa mãn điều kiện kiểm tra rỗng đầu tiên).
- Số nguyên `18` -> Ném ra ngoại lệ `TypeError: Gia dau vao phai la chuoi hoac None`. Đây là chủ đích thiết kế nhằm bắt lỗi lập trình khi truyền sai kiểu dữ liệu ngay từ đầu.
:::

::: exercise Tổng hợp doanh thu giỏ hàng bằng thư viện chuẩn Python thuần (Pure Python Aggregation)
Cho danh sách các đơn hàng thu thập từ hệ thống phân phối bán lẻ dạng bảng từ điển thô, trong đó cột giá tiền chứa các chuỗi rác ký tự tiền tệ và khoảng trắng:
```python
don_hang = [
    {"danh_muc": "VanPhong", "gia": " $1,250.00 ", "so_luong": 2},
    {"danh_muc": "GiaoDuc", "gia": "450.50", "so_luong": 5},
    {"danh_muc": "VanPhong", "gia": "Chua_co_gia", "so_luong": 1},
    {"danh_muc": "GiaoDuc", "gia": " $120.00 ", "so_luong": 10},
    {"danh_muc": "VanPhong", "gia": " -50.00 ", "so_luong": 3},
    {"danh_muc": "DienTu", "gia": " $2,500.00 ", "so_luong": 1}
]
```
Yêu cầu: Không sử dụng pandas hay bất kỳ thư viện bên thứ ba nào, hãy viết chương trình Python thuần để:
1. Làm sạch cột giá: loại bỏ ký hiệu tiền tệ `$`, dấu phẩy ngăn cách hàng nghìn `,` và khoảng trắng thừa, ép kiểu sang `float`.
2. Lọc bỏ các bản ghi không hợp lệ (giá âm hoặc không đọc được số).
3. Tính tổng doanh thu ($doanh\_thu = gia \times so\_luong$) theo từng danh mục hàng hóa.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Xử lý chuỗi tuần tự và từ điển thường)
Một cách người ta hay dùng khi mới lập trình là kết hợp các phương thức chuỗi `strip()`, `replace()` với khối `try-except` và duyệt từ điển thủ công:

```python
doanh_thu_nhom = {}

for don in don_hang:
    danh_muc = don["danh_muc"]
    raw_gia = don["gia"]
    sl = don["so_luong"]
    
    # 1. Làm sạch chuỗi thủ công
    s_sach = raw_gia.strip().replace("$", "").replace(",", "")
    
    try:
        gia = float(s_sach)
        if gia < 0:
            continue # Bỏ qua giá âm
    except ValueError:
        continue # Bỏ qua chuỗi không đọc được
        
    thanh_tien = gia * sl
    
    # 2. Gom nhóm với dict thông thường
    if danh_muc in doanh_thu_nhom:
        doanh_thu_nhom[danh_muc] += thanh_tien
    else:
        doanh_thu_nhom[danh_muc] = thanh_tien

print("Doanh thu căn bản:", doanh_thu_nhom)
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Dùng bảng dịch `str.translate` và `collections.defaultdict`)
Trong các ứng dụng hiệu năng cao xử lý hàng triệu dòng văn bản, lập trình viên chuyên nghiệp sẽ tận dụng bảng dịch ký tự ở tầng C thông qua `str.maketrans()` và cấu trúc `defaultdict(float)`:

```python
from collections import defaultdict

# Tạo bảng dịch ký tự 1 lần duy nhất ở tầng C (xóa bỏ $, , và khoảng trắng)
BANG_XOA = str.maketrans("", "", "$, ")

def tinh_doanh_thu_nhom(ds: list[dict]) -> dict[str, float]:
    ket_qua = defaultdict(float)
    
    for item in ds:
        # Làm sạch siêu tốc một bước qua translate
        chuoi_sach = item["gia"].translate(BANG_XOA)
        try:
            gia = float(chuoi_sach)
            if gia >= 0:
                ket_qua[item["danh_muc"]] += gia * item["so_luong"]
        except ValueError:
            pass # Ghi nhận lỗi hoặc bỏ qua có chủ đích
            
    return dict(ket_qua)

doanh_thu_chuan = tinh_doanh_thu_nhom(don_hang)
print("Doanh thu nâng cao:", doanh_thu_chuan)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Hiệu năng xử lý chuỗi**: Phương thức `.replace()` chuỗi lồng nhau tạo ra nhiều chuỗi trung gian trong bộ nhớ. Trong khi đó, `str.translate()` duyệt qua mảng ký tự một lượt duy nhất trong mã máy C, nhanh hơn từ 3 đến 5 lần trên các chuỗi văn bản lớn.
- **Tối ưu hóa gom nhóm**: `defaultdict(float)` tự động khởi tạo giá trị `0.0` khi gặp khóa mới, triệt tiêu hoàn toàn câu lệnh rẽ nhánh `if key in dict: ... else: ...`, giúp giảm thiểu việc tra cứu bảng băm lặp lại 2 lần trên cùng một phần tử.
:::

## 7. Nguồn và đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 2, mục 2.3: Python Language Basics](https://wesmckinney.com/book/python-basics) và [Chương 3, mục 3.1–3.3: Built-in Data Structures, Functions, and Files](https://wesmckinney.com/book/python-builtin).
- Tài liệu chính thức của Python: [The Python Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html).
- [Bài giảng tham khảo môn Xử lý dữ liệu (iaidev)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-02-python-co-ban.html).
