---
course: xu-ly-du-lieu
lecture: bai-02-python-co-ban
section: lecture
title: "Python cơ bản cho xử lý dữ liệu"
prerequisites: ["bien-kieu", "list", "dictionary", "vong-lap", "ham-lap-trinh"]
lessonStatus: ready
description: "Chọn cấu trúc dữ liệu, cơ chế tham chiếu bộ nhớ, phân biệt biến đổi với sàng lọc và đọc tệp chuẩn mực bằng Python thuần."
---

## 1. Cấu trúc Dữ liệu Quyết định Cơ chế Tra cứu và Hiệu năng Bộ nhớ

Trước khi vận hành các thư viện chuyên dụng như NumPy hay pandas, người kỹ sư dữ liệu bắt buộc phải làm chủ các cấu trúc dữ liệu bản địa của Python. Bản thân Python cung cấp một ngăn xếp cấu trúc dữ liệu rất linh hoạt, tuy nhiên mỗi cấu trúc lại mang một thiết kế bộ nhớ và chi phí tính toán hoàn toàn khác biệt. Nếu chọn sai cấu trúc cho một thao tác lặp lại thường xuyên trong đường ống xử lý hàng triệu bản ghi, thời gian thực thi có thể tăng từ vài giây lên tới nhiều giờ đồng hồ.

```
+----------------+-------------------------------+----------------------+------------------------+
| Cấu trúc       | Bản chất vùng nhớ             | Tra cứu theo khóa/vị trí | Kiểm tra tồn tại (in) |
+----------------+-------------------------------+----------------------+------------------------+
| list           | Mảng động chứa con trỏ        | O(1) theo chỉ số nguyên | O(n) quét tuần tự      |
| tuple          | Mảng con trỏ cố định bất biến | O(1) theo chỉ số nguyên | O(n) quét tuần tự      |
| dict           | Bảng băm (Hash Table)         | O(1) trung bình theo khóa | O(1) tra cứu khóa      |
| set            | Bảng băm chỉ chứa khóa        | Không hỗ trợ chỉ số  | O(1) tra cứu phần tử   |
+----------------+-------------------------------+----------------------+------------------------+
```

### 1.1. Bản chất bên dưới của Danh sách (`list`) và Dãy bất biến (`tuple`)
Trong ngôn ngữ C thực thi CPython, `list` thực chất là một mảng động chứa các con trỏ trỏ tới các đối tượng Python phân tán trong bộ nhớ heap.
- Khi truy cập phần tử theo chỉ số vị trí `ds[i]`, hệ thống chỉ cần một phép tính số học địa chỉ bộ nhớ: `địa_chỉ_gốc + i * kích_thước_con_trỏ`, do đó thao tác này luôn đạt độ phức tạp tức thì $O(1)$.
- Ngược lại, khi bạn thực hiện kiểm tra `if x in ds:`, CPython buộc phải duyệt tuần tự từ đầu đến cuối danh sách và so sánh từng con trỏ đối tượng. Nếu danh sách có $n$ bản ghi, thao tác này tiêu tốn thời gian $O(n)$. Nếu đặt phép kiểm tra này bên trong một vòng lặp duyệt $n$ phần tử khác, thuật toán sẽ bùng nổ độ phức tạp lên bậc hai $O(n^2)$.
- `tuple` có cơ chế bộ nhớ tương tự `list` nhưng sở hữu tính bất biến (*immutable*). Khi đã được khởi tạo, danh sách con trỏ bên trong `tuple` không thể thêm bớt hay tráo đổi. Đặc tính bất biến này cho phép CPython tối ưu hóa cấp phát bộ nhớ và cho phép `tuple` sinh mã băm (*hashable*), biến nó thành cấu trúc lý tưởng để làm khóa phức hợp nhiều trường (*composite key*) trong các bài toán gom nhóm dữ liệu.

### 1.2. Bảng băm (`dict` và `set`) — Vũ khí gia tốc tra cứu
`dict` và `set` được cài đặt dựa trên cấu trúc bảng băm (*hash table*) cực kỳ tinh vi của CPython.
- Để một đối tượng có thể đưa vào `set` hoặc làm khóa của `dict`, đối tượng đó bắt buộc phải bất biến (như chuỗi, số thực, số nguyên, hoặc tuple chứa các phần tử bất biến) để giá trị băm `hash(obj)` không đổi theo thời gian.
- Khi kiểm tra `if khoa in tu_dien:` hoặc `if phan_tu in tap_hop:`, Python tính toán mã băm của đối tượng, ánh xạ trực tiếp tới vị trí ô nhớ trong bảng băm. Độ phức tạp trung bình của phép tra cứu này là $O(1)$, hoàn toàn độc lập với kích thước dữ liệu.
- Phép toán đại số tập hợp giữa hai `set`:
  ```python
  thang_3 = {"HN01", "HN02", "HN03", "HN04"}
  thang_6 = {"HN02", "HN04", "HN05"}
  
  # Tìm các mã phòng biến mất và các mã phòng mới xuất hiện
  bien_mat = thang_3 - thang_6  # {'HN01', 'HN03'}
  moi_them = thang_6 - thang_3  # {'HN05'}
  ```
  Phép trừ tập hợp đạt độ phức tạp $O(\text{len}(thang\_3))$, nhanh hơn vượt trội so với việc viết vòng lặp lồng nhau duyệt qua danh sách thông thường.

### 1.3. Mã định danh không phải là con số
Một sai lầm kinh điển của người mới bước vào ngành dữ liệu là tự động ép kiểu mọi chuỗi ký tự chứa các chữ số sang dạng số nguyên `int()`.
Xét mã bưu chính, mã căn cước công dân hoặc mã sản phẩm: `"00123"`. Nếu bạn ép kiểu thành `int("00123")`, giá trị sẽ biến thành `123` và toàn bộ các số $0$ ở đầu (*leading zeros*) sẽ bị triệt tiêu vĩnh viễn. Trong kỹ thuật dữ liệu, nguyên tắc vàng được phát biểu như sau:
> **Nguyên tắc định danh**: Chỉ chuyển đổi sang kiểu số đối với những trường dữ liệu mà ta có nhu cầu thực hiện các phép toán số học (cộng, trừ, nhân, chia, tính trung bình). Mọi mã số định danh, số điện thoại, mã hợp đồng hay số phòng đều phải được bảo toàn nghiêm ngặt dưới dạng chuỗi (`str`).

---

## 2. Cơ chế Tham chiếu Vùng nhớ và Đột biến Dữ liệu Ngầm

Python vận hành theo mô hình quản lý bộ nhớ hướng đối tượng thông qua cơ chế gắn nhãn tham chiếu (*name-binding*). Việc không thấu suốt mô hình này là nguyên nhân hàng đầu dẫn tới các lỗi sai logic cực kỳ khó phát hiện.

### 2.1. Phép gán chưa bao giờ tạo ra bản sao
Khi bạn viết `b = a`, Python không hề sao chép các phần tử trong danh sách `a` sang một vùng nhớ mới. Lệnh này chỉ đơn thuần tạo thêm một cái tên mới `b` cùng trỏ vào đúng đối tượng mà `a` đang trỏ tới:

```python
a = [100, 200, 300]
b = a
b.append(400)

print(a)  # [100, 200, 300, 400] -> a bị biến đổi ngoài tầm kiểm soát!
```

### 2.2. Phân biệt Sao chép nông (*Shallow Copy*) và Sao chép sâu (*Deep Copy*)
Khi cần độc lập dữ liệu, ta thường dùng phương thức `.copy()` hoặc lát cắt `a[:]`. Tuy nhiên, đây mới chỉ là **sao chép nông**:

```python
import copy

# Danh sách chứa các từ điển bản ghi
du_lieu_goc = [{"id": "P01", "gia": 100}, {"id": "P02", "gia": 200}]

# 1. Sao chép nông
ban_sao_nong = du_lieu_goc.copy()
ban_sao_nong[0]["gia"] = 999
print(du_lieu_goc[0]["gia"])  # 999 -> Dữ liệu gốc vẫn bị sửa đổi ngầm!

# 2. Sao chép sâu độc lập hoàn toàn
du_lieu_chuan = copy.deepcopy(du_lieu_goc)
du_lieu_chuan[0]["gia"] = 500
print(du_lieu_goc[0]["gia"])  # 999 -> Dữ liệu gốc được bảo vệ an toàn
```

Bản sao nông chỉ tạo ra một danh sách mới chứa cùng các con trỏ trỏ tới các từ điển con bên trong. Để bảo đảm tính độc lập dữ liệu tuyệt đối khi thao tác với các cấu trúc lồng nhau (như danh sách các từ điển đọc từ CSV hay JSON), ta bắt buộc phải sử dụng `copy.deepcopy()` hoặc tạo mới từ điển con bằng phép tái cấu trúc `{**ban_ghi}`.

---

## 3. Phân định Rạch ròi giữa Biến đổi và Sàng lọc

Trong đường ống xử lý dữ liệu chuẩn mực, hai thao tác toán học sau đây không bao giờ được nhập nhằng:
1. **Biến đổi (Transformation / Mapping)**: Nhận một giá trị thô và chuyển hóa sang một biểu diễn chuẩn hóa tương ứng ($f: X \to Y$). Số lượng phần tử đầu vào và đầu ra là tương đương $1:1$.
2. **Sàng lọc (Filtering)**: Nhận một tập hợp các giá trị và giữ lại một tập con thỏa mãn điều kiện vị từ ($P: Y \to \{\text{True}, \text{False}\}$).

### 3.1. Bẫy chân trị (*Truthy vs Falsy*) với giá trị số 0
Trong ngôn ngữ Python, các giá trị sau đây khi đưa vào cấu trúc điều kiện `if` sẽ tự động bị đánh giá là sai (`False`):
- `None`
- `0`, `0.0`
- Chuỗi rỗng `""`
- Danh sách rỗng `[]`, từ điển rỗng `{}`

Hãy quan sát một đoạn mã nghiệp dư thường gặp:
```python
# CÁCH LÀM SAI LẦM NGUY HIỂM:
gia_hop_le = [g for g in danh_sach_gia if g]
```
Nếu trong dữ liệu có một phòng trọ được quảng bá với giá khuyến mãi bằng $0$ đồng (`0` hoặc `0.0`), đoạn mã trên sẽ coi `0` là `False` và loại bỏ nó không thương tiếc! Khi đó:
- Số lượng phòng hợp lệ bị đếm thiếu.
- Giá trị trung bình của thị trường bị thổi phồng một cách giả tạo.
- Phòng $0$ đồng bị đánh đồng với phòng bị mất thông tin giá (`None`).

Một cách người ta hay dùng để kiểm soát chính xác là sử dụng toán tử kiểm tra danh tính đối tượng:
```python
# CÁCH LÀM CHUẨN MỰC KỸ THUẬT:
gia_hop_le = [g for g in danh_sach_gia if g is not None]
```

### 3.2. Ép kiểu an toàn bằng khối `try / except` phòng thủ
Khi đọc dữ liệu văn bản từ tệp, ta không thể lường trước người dùng nhập vào những chuỗi ký tự quái dị nào (`"N/A"`, `"chưa_rõ"`, chuỗi rỗng `""`, hoặc các giá trị hỏng hóc). Ta đóng gói logic chuyển đổi vào một hàm phòng thủ:

```python
def to_float(value: any) -> float | None:
    """Chuyển đổi an toàn giá trị sang số thực float.
    
    Bảo toàn số 0.0; trả về None đối với chuỗi rỗng, None hoặc chuỗi không đọc được số.
    Bắt đích danh ngoại lệ (ValueError, TypeError), không che giấu lỗi hệ thống.
    """
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
```

Hàm trên tuân thủ nghiêm ngặt nguyên tắc xử lý ngoại lệ: chỉ bắt đích danh `(ValueError, TypeError)`. Tuyệt đối không bao giờ dùng `except: pass` cộc lốc vì cú pháp đó sẽ nuốt chửng cả những lỗi lập trình nghiêm trọng như gọi sai tên biến (`NameError`) hay tràn bộ nhớ (`MemoryError`).

---

## 4. Kỹ thuật Đọc & Ghi Tệp CSV, JSON Chuẩn mực

### 4.1. Đọc tệp CSV dạng từ điển với `csv.DictReader`
Mô-đun `csv` của thư viện chuẩn cung cấp lớp `csv.DictReader`. Thay vì trả về một danh sách các phần tử theo chỉ mục số nguyên dễ gây nhầm lẫn, `DictReader` tự động lấy dòng đầu tiên làm tiêu đề cột và ánh xạ mỗi dòng dữ liệu tiếp theo thành một từ điển có khóa là tên cột:

```python
import csv

def doc_danh_sach(duong_dan: str) -> list[dict]:
    with open(duong_dan, mode="r", encoding="utf-8", newline="") as tep:
        doc = csv.DictReader(tep)
        return list(doc)
```

Hai chi tiết kỹ thuật cốt lõi cần ghi nhớ:
- **Luôn chỉ định `encoding="utf-8"`**: Trên hệ điều hành Windows, mã hóa mặc định có thể là `cp1252` hoặc `cp930`, dẫn đến việc lỗi sập chương trình khi gặp ký tự tiếng Việt hoặc các ngôn ngữ có dấu.
- **Sử dụng `newline=""`**: Ngăn chặn Python tự ý diễn dịch sai các ký tự ngắt dòng (`\r\n` vs `\n`) lồng bên trong các trường văn bản CSV.

### 4.2. Xuất báo cáo JSON bảo toàn ký tự quốc tế
Khi tuần tự hóa (*serialize*) dữ liệu ra tệp JSON, mặc định `json.dump()` sẽ chuyển toàn bộ các ký tự Unicode không phải mã ASCII thành các chuỗi thoát hiểm dạng `\u00f1`. Để tệp JSON dễ đọc và bảo toàn nguyên vẹn tiếng Việt cùng các ký tự quốc tế, ta luôn thiết lập `ensure_ascii=False`:

```python
import json

def luu_bao_cao(du_lieu: dict, duong_dan: str) -> None:
    with open(duong_dan, mode="w", encoding="utf-8") as tep:
        json.dump(du_lieu, tep, ensure_ascii=False, indent=2)
```

---

## 5. Thống kê Mô tả: Trung bình Cộng vs Trung vị

Xét một mẫu số liệu giá gồm $n$ quan sát: $x_1, x_2, \dots, x_n$.
- **Giá trị trung bình cộng (*Mean*)**:
  $$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$$
- **Giá trị trung vị (*Median*)**: Là giá trị nằm ở vị trí chính giữa khi mẫu số liệu đã được sắp xếp tăng dần:
  $$\operatorname{Median} = \begin{cases} 
  x_{((n+1)/2)} & \text{khi } n \text{ lẻ} \\
  \frac{x_{(n/2)} + x_{(n/2 + 1)}}{2} & \text{khi } n \text{ chẵn}
  \end{cases}$$

### Bản chất sư phạm: Sức đề kháng trước ngoại lai (*Robustness*)
Trong kinh tế học và phân tích dữ liệu thị trường thực tế (như giá bất động sản, tiền lương, lưu lượng truy cập), phân phối dữ liệu hầu như không bao giờ có dạng chuẩn đối xứng mà luôn **lệch phải (*right-skewed*)** với chiếc đuôi rất dài gồm một số ít căn hộ siêu sang có giá hàng triệu USD.
- Trung bình cộng rất nhạy cảm với ngoại lai: chỉ cần xuất hiện một căn biệt thự giá 10 tỷ đồng, mức giá trung bình của toàn khu phố sẽ bị kéo vọt lên, tạo cảm giác sai lệch về mức sống thực tế của cư dân.
- Trung vị là một thống kê có **sức chịu tải vững (*robust statistic*)**: mức giá căn biệt thự dù có tăng từ 10 tỷ lên 100 tỷ thì giá trị đứng giữa danh sách sắp xếp vẫn không hề thay đổi. Do đó, trong các báo cáo thị trường chuyên nghiệp, trung vị luôn là thước đo trung tâm được ưu tiên hàng đầu.

---

## 6. Bài tập Thực chiến Phòng Lab 02 (100% Nội dung Lab)

Dưới đây là toàn bộ bài tập thực hành từ Lab 02, được thiết kế lại độc lập và sư phạm với đầy đủ hai tầng lời giải: **Cách 1: Căn bản & Trực quan** và **Cách 2: Nâng cao & Tối ưu**.

### Bài tập 1 (Khởi động & Dự đoán): Định dạng số, Lọc giá và Phép toán tập hợp
::: exercise Dự đoán kết quả thực thi chuỗi lệnh Python thuần
Cho đoạn mã khởi động sau:
```python
gia_tb, ty_le = 118199.6, 0.178
print(f"Giá TB: {gia_tb:,.0f} CLP | Tỷ lệ: {ty_le:.1%}")

gia_mau = [52000, None, 78000, 0]
gia_co = [g for g in gia_mau if g is not None]
print("Giá hợp lệ:", gia_co, "Trung bình:", sum(gia_co) / len(gia_co))

thang_3, thang_6 = {101, 102, 103, 104}, {102, 104, 105}
print("Biến mất:", thang_3 - thang_6, "Mới thêm:", thang_6 - thang_3)
```
1. Dự đoán kết quả in ra màn hình của từng dòng lệnh.
2. Nếu dòng lọc giá được viết thành `[g for g in gia_mau if g]`, kết quả danh sách `gia_co` và giá trị trung bình sẽ thay đổi như thế nào?
:::

::: solution
#### Lời giải & Phân tích chi tiết:
1. **Kết quả thực thi**:
   - Dòng 1: `f"{gia_tb:,.0f} CLP"` định dạng số thực thành số không có chữ số thập phân (`.0f`), có dấu phẩy ngăn phần nghìn (làm tròn số học thành `118,200 CLP`). `f"{ty_le:.1%}"` nhân số thực với $100$ và thêm ký hiệu phần trăm với 1 chữ số sau dấu phẩy (`17.8%`).
     $\to$ In ra: `Giá TB: 118,200 CLP | Tỷ lệ: 17.8%`.
   - Dòng 2: Danh sách `gia_co` chỉ loại trừ giá trị `None`, giữ lại số `0`. Do đó `gia_co = [52000, 78000, 0]`. Tổng là $130,000$, số phần tử là $3$.
     $\to$ In ra: `Giá hợp lệ: [52000, 78000, 0] Trung bình: 43333.333333333336`.
   - Dòng 3: Phép trừ tập hợp `thang_3 - thang_6` tìm các phần tử thuộc tháng 3 nhưng không thuộc tháng 6: `{101, 103}`. Ngược lại `thang_6 - thang_3` tìm các phần tử mới: `{105}`.
     $\to$ In ra: `Biến mất: {101, 103} Mới thêm: {105}`.

2. **Hậu quả khi viết `[g for g in gia_mau if g]`**:
   - Biểu thức `if g` đánh giá số `0` là `False`, dẫn đến việc số `0` bị loại bỏ cùng với `None`.
   - Khi đó danh sách chỉ còn `[52000, 78000]`. Số phần tử hợp lệ giảm xuống còn $2$ và trung bình bị thổi phồng thành $\frac{130,000}{2} = 65,000$, sai lệch hoàn toàn so với thực tế!
:::

---

### Bài tập 2 (Q1): Đọc tệp CSV danh sách phòng trọ bằng `csv.DictReader`
::: exercise Hiện thực hàm đọc tệp dữ liệu CSV chuẩn mực
Viết hàm `read_listings(path: str | Path) -> list[dict]`.
Yêu cầu:
- Sử dụng `csv.DictReader` và mã hóa UTF-8.
- Đóng tệp an toàn bằng ngữ cảnh `with`.
- Giữ nguyên toàn bộ giá trị dưới dạng chuỗi và bảo toàn thứ tự dòng.
- Nếu tệp rỗng hoặc chỉ có dòng tiêu đề, trả về danh sách rỗng `[]`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Duyệt tuần tự và thêm vào danh sách)
```python
import csv
from pathlib import Path

def read_listings(path):
    danh_sach = []
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for dong in reader:
            danh_sach.append(dict(dong))
    return danh_sach
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Ép kiểu trực tiếp iterator tầng C)
```python
import csv
from pathlib import Path

def read_listings(path: str | Path) -> list[dict]:
    with open(path, mode="r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))
```

#### Phân tích bản chất:
- `csv.DictReader` là một đối tượng generator lặp qua từng dòng của tệp. Lệnh `list(...)` sẽ kích hoạt vòng lặp tối ưu hóa ở tầng C để tiêu thụ toàn bộ các bản ghi vào bộ nhớ mà không cần viết vòng lặp `for` thủ công trong Python.
:::

---

### Bài tập 3 (Q2): Ép kiểu giá sang số thực phòng thủ
::: exercise Chuyển đổi dữ liệu giá phòng sang số thực
Viết hàm `to_float(value: any) -> float | None`.
Quy tắc xử lý:
- Giá trị chuỗi biểu diễn số hợp lệ hoặc số hữu hạn $\to$ trả về `float`.
- Chuỗi rỗng `""`, `None`, hoặc chuỗi không chuyển được (như `"N/A"`, `"chua_co"`) $\to$ trả về `None`.
- Bảo toàn nguyên vẹn giá trị bằng $0$ (`0` hoặc `"0"` chuyển thành `0.0`).
- Bắt đích danh `(ValueError, TypeError)`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan
```python
def to_float(value):
    if value is None:
        return None
    if isinstance(value, str) and value.strip() == "":
        return None
    try:
        ket_qua = float(value)
        return ket_qua
    except ValueError:
        return None
    except TypeError:
        return None
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu
```python
def to_float(value: any) -> float | None:
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
```

#### Phân tích bản chất:
- Trong Python, `float("")` tự động ném ra `ValueError`. Do đó việc bắt cặp ngoại lệ `(ValueError, TypeError)` sẽ xử lý trọn vẹn cả chuỗi rỗng lẫn các ký tự rác mà không cần thêm phép kiểm tra chuỗi rỗng thủ công, giúp mã nguồn cô đọng và chạy nhanh hơn.
:::

---

### Bài tập 4 (Q3): Tóm tắt thống kê cột giá đã làm sạch
::: exercise Xây dựng hàm thống kê mô tả trung tâm
Viết hàm `summarize_prices(prices: list[float | None]) -> dict`.
Hàm nhận vào danh sách giá (đã được làm sạch thành số thực hoặc `None`), trả về từ điển chứa chính xác 4 khóa:
- `n_valid`: Số lượng bản ghi hợp lệ (khác `None`, giữ lại $0$).
- `n_missing`: Số lượng bản ghi bị thiếu (`None`).
- `mean`: Giá trị trung bình cộng của các bản ghi hợp lệ.
- `median`: Giá trị trung vị của các bản ghi hợp lệ.

Nếu danh sách không có bất kỳ giá trị hợp lệ nào (`n_valid == 0`), thiết lập `mean = None` và `median = None`. Không làm tròn số bên trong hàm.
:::

::: solution
#### Hàm phụ trợ tính trung vị chuẩn xác:
```python
def trung_vi(xs: list[float]) -> float | None:
    n = len(xs)
    if n == 0:
        return None
    da_sap_xep = sorted(xs)
    vi_tri_giua = n // 2
    if n % 2 == 1:
        return da_sap_xep[vi_tri_giua]
    return (da_sap_xep[vi_tri_giua - 1] + da_sap_xep[vi_tri_giua]) / 2.0
```

#### Cách 1: Tiếp cận Căn bản & Trực quan (Duyệt vòng lặp đếm)
```python
def summarize_prices(prices):
    hop_le = []
    so_thieu = 0
    for p in prices:
        if p is None:
            so_thieu += 1
        else:
            hop_le.append(p)
            
    so_hop_le = len(hop_le)
    if so_hop_le == 0:
        return {"n_valid": 0, "n_missing": so_thieu, "mean": None, "median": None}
        
    gia_tb = sum(hop_le) / so_hop_le
    gia_tv = trung_vi(hop_le)
    return {"n_valid": so_hop_le, "n_missing": so_thieu, "mean": gia_tb, "median": gia_tv}
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Dùng List Comprehension)
```python
def summarize_prices(prices: list[float | None]) -> dict:
    valid = [p for p in prices if p is not None]
    n_valid = len(valid)
    n_missing = len(prices) - n_valid
    
    if n_valid == 0:
        return {"n_valid": 0, "n_missing": n_missing, "mean": None, "median": None}
        
    return {
        "n_valid": n_valid,
        "n_missing": n_missing,
        "mean": sum(valid) / n_valid,
        "median": trung_vi(valid)
    }
```
:::

---

### Bài tập 5 (Q4): Tìm phòng có giá đắt nhất
::: exercise Trích xuất định danh bản ghi đạt giá trị cực đại
Viết hàm `most_expensive(records: list[dict]) -> str | None`.
Đầu vào là danh sách các bản ghi chứa trường `id` (dạng chuỗi) và trường `price` (đã là số thực hoặc `None`).
Yêu cầu:
- Sử dụng hàm `max(..., key=...)` của Python.
- Loại bỏ các bản ghi có giá `None`, bảo toàn bản ghi có giá $0$.
- Nếu có nhiều phòng đồng giá đắt nhất, lấy bản ghi xuất hiện đầu tiên trong danh sách.
- Nếu không có bất kỳ phòng nào có giá hợp lệ, trả về `None`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan
```python
def most_expensive(records):
    id_max = None
    gia_max = -1.0
    
    for r in records:
        gia = r.get("price")
        if gia is not None:
            if gia > gia_max:
                gia_max = gia
                id_max = r["id"]
                
    return id_max
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Sử dụng `max` với hàm khóa chuẩn vị từ)
```python
def most_expensive(records: list[dict]) -> str | None:
    valid_records = [r for r in records if r.get("price") is not None]
    if not valid_records:
        return None
    # Trong Python, max() bảo toàn phần tử đầu tiên khi có sự hòa điểm (tie-break)
    best = max(valid_records, key=lambda r: r["price"])
    return best["id"]
```

#### Phân tích bản chất:
- Hàm `max()` trong Python được cài đặt ổn định (*stable*): khi hai phần tử có giá trị khóa bằng nhau, `max()` luôn giữ lại phần tử gặp đầu tiên trong chuỗi lặp.
:::

---

### Bài tập 6 (Q5): Thống kê số lượng phòng theo khu vực
::: exercise Đếm tần suất xuất hiện theo nhóm danh mục
Viết hàm `count_by_area(records: list[dict]) -> dict[str, int]`.
Đầu vào là danh sách các bản ghi chứa trường `neighbourhood` (chuỗi không rỗng).
Trả về từ điển dạng `{tên_khu: số_lượng_phòng}`. Đếm mọi bản ghi bất kể giá, nếu danh sách rỗng trả về `{}`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Duyệt từ điển thông thường)
```python
def count_by_area(records):
    ket_qua = {}
    for r in records:
        khu = r["neighbourhood"]
        if khu in ket_qua:
            ket_qua[khu] += 1
        else:
            ket_qua[khu] = 1
    return ket_qua
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Sử dụng `collections.Counter`)
```python
from collections import Counter

def count_by_area(records: list[dict]) -> dict[str, int]:
    return dict(Counter(r["neighbourhood"] for r in records))
```

#### Phân tích bản chất:
- `Counter` là một lớp con của `dict` được tối ưu hóa ở tầng C cho bài toán đếm tần suất. Việc truyền một generator expression `(r["neighbourhood"] for r in records)` vào `Counter` giúp tiết kiệm bộ nhớ tối đa vì không cần tạo danh sách trung gian.
:::

---

### Bài tập 7 (Q6): Tính trung vị giá theo từng khu vực
::: exercise Phân nhóm dữ liệu và tổng hợp trung vị
Viết hàm `median_by_area(records: list[dict]) -> dict[str, float | None]`.
Đầu vào là danh sách các bản ghi có `neighbourhood` không rỗng và `price` đã là số thực hoặc `None`.
Yêu cầu:
- Trả về từ điển ánh xạ từ mọi khu vực xuất hiện sang giá trị trung vị của khu vực đó.
- Nếu một khu vực chỉ có các phòng bị thiếu giá (`None`), giá trị trung vị tương ứng là `None`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Gom nhóm bằng từ điển thường)
```python
def median_by_area(records):
    nhom_gia = {}
    for r in records:
        khu = r["neighbourhood"]
        if khu not in nhom_gia:
            nhom_gia[khu] = []
        if r.get("price") is not None:
            nhom_gia[khu].append(r["price"])
            
    ket_qua = {}
    for khu, ds_gia in nhom_gia.items():
        ket_qua[khu] = trung_vi(ds_gia)
    return ket_qua
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Sử dụng `collections.defaultdict`)
```python
from collections import defaultdict

def median_by_area(records: list[dict]) -> dict[str, float | None]:
    gia_theo_khu = defaultdict(list)
    for r in records:
        gia = r.get("price")
        if gia is not None:
            gia_theo_khu[r["neighbourhood"]].append(gia)
        else:
            # Bảo đảm khu vực vẫn có mặt trong khóa dù không có giá hợp lệ
            _ = gia_theo_khu[r["neighbourhood"]]
            
    return {khu: trung_vi(ds) for khu, ds in gia_theo_khu.items()}
```
:::

---

### Bài tập 8 (Q7): Kiểm định chéo chất lượng dữ liệu đánh giá (Cross-Column QA)
::: exercise Thẩm định logic toàn vẹn giữa số lượng đánh giá và ngày đánh giá
Trong tập dữ liệu thực tế, mỗi bản ghi phòng trọ có hai cột:
- `number_of_reviews`: Chuỗi biểu diễn số nguyên không âm (ví dụ: `"0"`, `"5"`).
- `last_review`: Chuỗi biểu diễn ngày đánh giá gần nhất (ví dụ: `"2026-05-10"` hoặc chuỗi rỗng `""` nếu chưa có đánh giá nào).

Viết hàm `review_qa(records: list[dict]) -> dict[str, int]` trả về từ điển có đúng hai khóa:
- `n_zero`: Tổng số dòng có `number_of_reviews == "0"`.
- `n_inconsistent`: Trong số các dòng có 0 lượt đánh giá đó, có bao nhiêu dòng lại có trường `last_review` khác rỗng (`last_review != ""`).
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan
```python
def review_qa(records):
    n_zero = 0
    n_inconsistent = 0
    
    for r in records:
        if r.get("number_of_reviews") == "0":
            n_zero += 1
            if r.get("last_review") != "":
                n_inconsistent += 1
                
    return {"n_zero": n_zero, "n_inconsistent": n_inconsistent}
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Đếm tích lũy generator)
```python
def review_qa(records: list[dict]) -> dict[str, int]:
    zero_records = [r for r in records if r.get("number_of_reviews") == "0"]
    n_inconsistent = sum(1 for r in zero_records if r.get("last_review", "") != "")
    return {
        "n_zero": len(zero_records),
        "n_inconsistent": n_inconsistent
    }
```
:::

---

### Bài tập 9 (Q8): Tuần tự hóa Báo cáo ra tệp JSON và Thẩm định Round-Trip
::: exercise Lưu trữ và đọc lại báo cáo phân tích
Viết hàm `save_report(report: dict, path: str | Path) -> dict`.
Yêu cầu:
- Ghi từ điển `report` vào đường dẫn `path` dưới dạng tệp JSON, sử dụng `encoding="utf-8"` và `ensure_ascii=False`.
- Đọc lại tệp vừa ghi bằng `json.load()` và trả về chính từ điển được đọc lại từ đĩa để xác thực tính toàn vẹn (*Round-trip serialization validation*).
:::

::: solution
#### Lời giải chuẩn mực:
```python
import json
from pathlib import Path

def save_report(report: dict, path: str | Path) -> dict:
    duong_dan = Path(path)
    
    # 1. Ghi tệp JSON chuẩn hóa UTF-8
    with open(duong_dan, mode="w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
        
    # 2. Đọc lại để kiểm chứng tính toàn vẹn
    with open(duong_dan, mode="r", encoding="utf-8") as f:
        du_lieu_doc_lai = json.load(f)
        
    return du_lieu_doc_lai
```
:::

---

### Bài tập 10 (Diễn giải & Phỏng đoán): Đào sâu Bản chất Xử lý Dữ liệu
::: exercise Ba câu hỏi bản chất trong phân tích dữ liệu thực tế
1. **Mean vs Median**: Dẫn chứng số liệu và giải thích vì sao trong tập dữ liệu phòng trọ, giá trị trung bình cộng thường cao hơn đáng kể so với trung vị?
2. **Hiểm họa của bẫy chân trị**: Vì sao tuyệt đối không được dùng câu lệnh điều kiện `if price:` để lọc dữ liệu giá hợp lệ?
3. **Kỷ luật kiểm định chất lượng (QA)**: Khi phát hiện một bản ghi có 0 lượt đánh giá nhưng ngày đánh giá lại không rỗng, vì sao người kỹ sư dữ liệu không được tự ý xóa dòng đó đi mà phải gắn cờ báo cáo QA?
:::

::: solution
#### Phân tích & Trả lời từ Giảng viên:

1. **Về sự chênh lệch giữa Mean và Median**:
   - Trong dữ liệu thực tế (chẳng hạn tại thủ đô Santiago hoặc Hà Nội), đa số các phòng trọ bình dân có mức giá dao động tập trung trong khoảng từ $300,000$ đến $800,000$ VNĐ/đêm. Tuy nhiên, thị trường luôn tồn tại một số ít các biệt thự, penthouse nghỉ dưỡng cao cấp có giá lên tới $20,000,000$ hoặc $50,000,000$ VNĐ/đêm.
   - Các căn hộ siêu đắt này đóng vai trò là các **ngoại lai cực trị ở phía đuôi dài (*extreme outliers*)**. Khi tính trung bình cộng, tử số $\sum x_i$ bị kéo vọt lên, khiến giá trung bình bị thổi phồng lên mức $1,500,000$ VNĐ/đêm — một con số không đại diện cho số đông.
   - Trong khi đó, trung vị chỉ quan tâm đến thứ tự sắp xếp: dù căn penthouse có tăng giá gấp mười lần thì điểm chính giữa phân phối vẫn đứng yên quanh mức $500,000$ VNĐ/đêm. Vì vậy, trung vị phản ánh chính xác nhất mức giá thông thường mà một du khách phổ thông phải chi trả.

2. **Về hiểm họa của điều kiện `if price:`**:
   - Trong Python, giá trị số thực `0.0` được đánh giá là `False`.
   - Trong kinh doanh khách sạn và dịch vụ lưu trú, mức giá $0$ đồng là một trạng thái nghiệp vụ hoàn toàn hợp lệ: đây có thể là các đêm phòng miễn phí tích lũy theo chương trình khách hàng thân thiết, phòng tài trợ sự kiện, hoặc các voucher khuyến mãi đặc biệt.
   - Nếu viết `if price:`, chương trình sẽ vô tình loại bỏ các phòng $0$ đồng này cùng với các phòng bị mất dữ liệu (`None`), làm suy giảm cỡ mẫu hợp lệ và khiến giá bình quân bị tính sai lệch. Nguyên tắc đúng đắn bắt buộc phải là `if price is not None:`.

3. **Về lý do không tự ý xóa dữ liệu mâu thuẫn**:
   - Việc có 0 review nhưng ngày review không rỗng là một biểu hiện của **xung đột toàn vẹn dữ liệu (*Data Inconsistency*)**. Hiện tượng này có thể bắt nguồn từ:
     - Lỗi đồng bộ cơ sở dữ liệu (*replication lag*) giữa bảng `listings` và bảng `reviews`.
     - Lập trình viên hệ thống backend đã xóa các bình luận tiêu cực của người dùng (khiến số review về $0$) nhưng quên không xóa trường ngày bình luận cuối cùng.
     - Dữ liệu bị ghi đè không trọn vẹn trong quá trình giải nén hoặc chuyển đổi dữ liệu.
   - Nếu kỹ sư dữ liệu tự ý xóa dòng này, ta đã **tiêu hủy bằng chứng về lỗi hệ thống (*destructive action*)**, che giấu một lỗi tiềm ẩn trong đường ống dữ liệu gốc và làm sai lệch tổng số lượng phòng đang hoạt động trên thị trường. Việc chuẩn mực là giữ nguyên bản ghi, gắn cờ báo cáo vào tệp kiểm định chất lượng (`review_qa`) để bộ phận kỹ thuật điều tra tận gốc.
:::

---

### Bài tập 11 (Mở rộng E1): Xếp hạng Khu vực theo Trung vị có Lọc Ngưỡng Cỡ mẫu
::: exercise Xây dựng bảng xếp hạng thị trường đa tiêu chí
Viết hàm `rank_areas(records: list[dict], min_valid: int = 100) -> list[dict]`.
Yêu cầu:
- Mỗi bản ghi đầu vào chứa `neighbourhood` (chuỗi) và `price` (đã là số thực hoặc `None`).
- Chỉ giữ lại các khu vực có số lượng phòng có giá hợp lệ $\ge min\_valid$.
- Trả về danh sách các từ điển có đúng ba trường: `neighbourhood` (str), `n_valid` (int), `median_price` (float).
- Sắp xếp kết quả theo hai tiêu chí: `median_price` giảm dần; nếu có hai khu bằng nhau về trung vị thì sắp xếp tên khu tăng dần theo thứ tự từ điển alphabet.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan
```python
from collections import defaultdict

def rank_areas(records, min_valid=100):
    gia_nhom = defaultdict(list)
    for r in records:
        p = r.get("price")
        if p is not None:
            gia_nhom[r["neighbourhood"]].append(p)
            
    ket_qua = []
    for khu, ds in gia_nhom.items():
        if len(ds) >= min_valid:
            ket_qua.append({
                "neighbourhood": khu,
                "n_valid": len(ds),
                "median_price": float(trung_vi(ds))
            })
            
    # Sắp xếp 2 tiêu chí: median giảm dần (-x), tên tăng dần
    ket_qua.sort(key=lambda item: (-item["median_price"], item["neighbourhood"]))
    return ket_qua
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Độc lập dữ liệu tuyệt đối và đóng gói bộ lọc)
```python
from collections import defaultdict

def rank_areas(records: list[dict], min_valid: int = 100) -> list[dict]:
    if min_valid <= 0:
        min_valid = 1
        
    gom_gia = defaultdict(list)
    for r in records:
        gia = r.get("price")
        if gia is not None:
            gom_gia[r["neighbourhood"]].append(gia)
            
    danh_sach_dat_chuan = [
        {
            "neighbourhood": khu,
            "n_valid": len(ds_gia),
            "median_price": float(trung_vi(ds_gia))
        }
        for khu, ds_gia in gom_gia.items()
        if len(ds_gia) >= min_valid
    ]
    
    return sorted(danh_sach_dat_chuan, key=lambda x: (-x["median_price"], x["neighbourhood"]))
```
:::

---

### Bài tập 12 (Mở rộng E2): Phân tích Xu hướng Đánh giá theo Năm và Bẫy Dữ liệu Dang dở
::: exercise Thống kê chuỗi thời gian lượt đánh giá qua các năm
Viết hàm `review_counts_by_year(records: list[dict]) -> dict[str, int]`.
Mỗi bản ghi chứa trường `date` có định dạng `"YYYY-MM-DD"` hoặc chuỗi rỗng `""`.
Yêu cầu:
- Bỏ qua các dòng có `date == ""`. Với mỗi dòng hợp lệ, trích xuất 4 ký tự đầu tiên làm năm (`date[:4]`).
- Đếm tổng số đánh giá theo từng năm, không tự ý loại trừ dòng trùng.
- Trả về từ điển `{năm: số_đánh_giá}` với các khóa năm được sắp xếp tăng dần theo thời gian.
- **Thảo luận**: Nếu dữ liệu snapshot được trích xuất vào ngày 29/06/2026, ta có thể so sánh trực tiếp số lượng đánh giá của năm 2026 với cả năm 2025 để kết luận thị trường du lịch đang suy thoái hay không? Vì sao?
:::

::: solution
#### Lời giải Thuần Python:
```python
from collections import Counter

def review_counts_by_year(records: list[dict]) -> dict[str, int]:
    dem_nam = Counter(
        r["date"][:4]
        for r in records
        if r.get("date")
    )
    # Sắp xếp các khóa năm theo thứ tự thời gian tăng dần
    return {nam: dem_nam[nam] for nam in sorted(dem_nam.keys())}
```

#### Phân tích sư phạm về bẫy so sánh dữ liệu dang dở:
- **Tuyệt đối không được kết luận thị trường suy thoái!**
- Tệp dữ liệu có mốc snapshot là ngày 29/06/2026, tức là năm 2026 mới chỉ đi qua chưa đầy 6 tháng đầu năm. Việc lấy số lượng đánh giá của một nửa năm 2026 đi so sánh trực tiếp với tổng lượng đánh giá của trọn vẹn 12 tháng năm 2025 là một sai lầm nghiêm trọng về phương pháp luận thống kê.
- Hơn nữa, ngành du lịch có tính chu kỳ mùa vụ (*seasonality*) rất mạnh: các tháng mùa hè và dịp nghỉ lễ cuối năm thường chiếm tới $60\% - 70\%$ tổng lượng khách của cả năm. Để so sánh chuẩn xác, người phân tích bắt buộc phải so sánh cùng kỳ năm trước (*Year-over-Year - YoY*), tức là đối chiếu giai đoạn 6 tháng đầu năm 2026 với 6 tháng đầu năm 2025.
:::

---

## 7. Tổng kết và Bài học Kinh nghiệm

1. **Cấu trúc dữ liệu định hình thuật toán**: Sử dụng `list` khi cần bảo toàn thứ tự, dùng `set` khi cần trừ tập hợp và kiểm tra thành viên $O(1)$, dùng `dict` để quản lý các trường bản ghi, và dùng `tuple` khi cần khóa phức hợp bất biến.
2. **Cảnh giác trước phép gán**: Phép gán trong Python chỉ liên kết tên biến với vùng nhớ có sẵn. Luôn dùng `copy.deepcopy()` hoặc tái cấu trúc bản ghi khi cần chỉnh sửa dữ liệu mà không làm biến dạng tập dữ liệu thô ban đầu.
3. **Kỷ luật với giá trị 0**: Tuyệt đối không kiểm tra hợp lệ bằng `if price:`. Luôn sử dụng `if price is not None:` để bảo vệ các giá trị số $0$ hợp lệ.
4. **Vững chãi trước ngoại lai**: Trong các phân phối dữ liệu kinh tế lệch phải, giá trị trung vị (*Median*) là chỉ số trung tâm đáng tin cậy hơn nhiều so với trung bình cộng (*Mean*).
5. **Giữ gìn dấu vết kiểm toán**: Không tự ý xóa bỏ các dòng dữ liệu xung đột logic mà hãy đưa chúng vào báo cáo kiểm định chất lượng (QA) để truy xuất nguồn gốc lỗi của hệ thống.
