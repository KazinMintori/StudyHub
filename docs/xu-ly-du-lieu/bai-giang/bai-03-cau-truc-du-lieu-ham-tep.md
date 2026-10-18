---
course: xu-ly-du-lieu
lecture: bai-03-cau-truc-du-lieu-ham-tep
section: lecture
title: "Cấu trúc dữ liệu, hàm và tệp"
prerequisites: ["bien-kieu", "vong-lap"]
lessonStatus: ready
hasChapterExercises: true
description: "Cấu trúc dữ liệu Python bản địa, hàm bậc cao, hàm sinh generator, xử lý ngoại lệ và thao tác tệp an toàn trong đường ống dữ liệu."
---


<div class="lecture-notes-content">

## 1. Cấu trúc dữ liệu và dãy trong Python

Bạn nhận một tệp nhật ký bán hàng gồm nhiều dòng dạng `ma_san_pham,so_tien`. Một số dòng ghi thiếu số tiền, một số dòng chứa ký tự lạ. Bạn cần đọc từng dòng, làm sạch khoảng trắng, phân nhóm theo sản phẩm và tính tổng tiền mà không để một dòng lỗi làm dừng toàn bộ chương trình.

Trước khi vận hành các thư viện phân tích bảng như pandas, người kỹ sư dữ liệu cần làm chủ các cấu trúc dữ liệu bản địa của Python. Việc chọn đúng cấu trúc cho từng thao tác giúp đường ống dữ liệu vận hành ổn định và tiết kiệm tài nguyên.

### 1.1. Bộ bất biến (Tuple)
`tuple` là một dãy cố định các phần tử có thứ tự và mang tính **bất biến** (*immutable*). Khi đã được khởi tạo, chuỗi tham chiếu bên trong `tuple` không thể thêm bớt hay thay thế.

Tuy nhiên, nếu một phần tử bên trong `tuple` là một đối tượng khả biến (chẳng hạn một danh sách `list`), nội dung của danh sách con đó vẫn có thể bị thay đổi tại chỗ:
```python
tup_long = (1, 2, [3, 4])
tup_long[2].append(5)
print(tup_long)  # (1, 2, [3, 4, 5])
```
Bản thân tuple vẫn lưu giữ các tham chiếu ban đầu, nhưng trạng thái bên trong của đối tượng danh sách con đã biến đổi.

```python
tup = (4, 5, 6)
tup_chuoi = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
```

#### Phép giải nén Tuple (Unpacking)
Python cho phép gán đồng thời các phần tử của tuple vào các biến độc lập:
```python
a, b, c = tup  # a=4, b=5, c=6

# Tráo đổi giá trị hai biến mà không cần biến trung gian
a, b = b, a
```

Kỹ thuật bắt phần tử thừa với toán tử dấu sao `*rest` cho phép tách phần tử đầu và giữ lại phần còn lại dưới dạng danh sách:
```python
day_so = (1, 2, 3, 4, 5, 6)
dau, *giua, cuoi = day_so
print(dau)   # 1
print(giua)  # [2, 3, 4, 5]
print(cuoi)  # 6
```

Phương thức chính của tuple gồm `tup.count(gia_tri)` (đếm số lần xuất hiện) và `tup.index(gia_tri)` (tìm vị trí đầu tiên).

### 1.2. Danh sách (List)
Khác với tuple, `list` là cấu trúc mảng động có kích thước biến thiên và nội dung **khả biến** (*mutable*).

#### Thao tác thêm, bớt và chi phí thời gian
- `ds.append(x)`: Thêm phần tử vào cuối danh sách. Thao tác này đạt độ phức tạp khấu hao $O(1)$.
- `ds.insert(vi_tri, x)`: Chèn phần tử vào một vị trí chỉ định. Nếu chèn ở đầu danh sách (`vi_tri = 0`), CPython buộc phải dịch chuyển toàn bộ $n$ phần tử về phía sau, tiêu tốn thời gian $O(n)$.
- `ds.pop(vi_tri)`: Lấy ra và xóa phần tử. `ds.pop()` ở cuối danh sách đạt $O(1)$, nhưng `ds.pop(0)` ở đầu danh sách tốn $O(n)$.
- `ds.remove(gia_tri)`: Tìm và xóa phần tử đầu tiên khớp giá trị, tốn $O(n)$.
- Kiểm tra thành viên `if x in ds:` duyệt tuần tự qua danh sách, đạt độ phức tạp $O(n)$.

#### Nối danh sách: Toán tử `+` so với phương thức `.extend()`
Khi cần kết hợp hai danh sách:
- Toán tử `ds1 + ds2` cấp phát một danh sách mới trong RAM và sao chép các tham chiếu phần tử của cả hai danh sách vào đó (sao chép nông tham chiếu, không sao chép sâu các đối tượng).
- Phương thức `ds1.extend(ds2)` thay đổi trực tiếp danh sách `ds1` tại chỗ bằng cách gắn thêm các tham chiếu phần tử từ `ds2`. Thao tác này tránh việc cấp phát danh sách vỏ ngoài mới khi muốn tích lũy dữ liệu vào một danh sách sẵn có.

#### Sắp xếp danh sách
- `ds.sort()`: Sắp xếp danh sách tại chỗ (*in-place*), làm biến đổi danh sách gốc và trả về `None`.
- `sorted(ds)`: Giữ nguyên danh sách gốc và trả về một danh sách mới đã được sắp xếp.
- Tham số `key`: Tiếp nhận một hàm chỉ định tiêu chí sắp xếp:
  ```python
  danh_sach_tu = ["trung_binh", "gia", "du_lieu_lon", "bang"]
  danh_sach_tu.sort(key=len)  # Sắp xếp tăng dần theo độ dài từ
  print(danh_sach_tu)  # ['gia', 'bang', 'trung_binh', 'du_lieu_lon']
  ```

#### Cắt lát danh sách (Slicing)
Cú pháp lát cắt `ds[start:stop:step]` cho phép trích xuất một đoạn danh sách. `stop` không được bao gồm trong kết quả. Bước nhảy `step` có thể mang giá trị âm để đảo ngược danh sách: `ds[::-1]`. Gán giá trị vào lát cắt `ds[1:3] = [88, 99]` sẽ thay thế trực tiếp đoạn phần tử đó.

### 1.3. Từ điển (Dictionary)
`dict` là cấu trúc bảng băm (*hash table*) lưu trữ các cặp khóa - giá trị (*key - value*).

#### Tạo từ điển từ hai chuỗi song song
Hàm `zip` kết hợp hai tập hợp thành các cặp, sau đó truyền vào hàm khởi tạo `dict`:
```python
cot = ["ma", "gia", "so_luong"]
du_lieu = ["P01", 150000, 4]
ban_ghi = dict(zip(cot, du_lieu))
# {'ma': 'P01', 'gia': 150000, 'so_luong': 4}
```

#### Quản lý giá trị mặc định
Khi truy cập một khóa không tồn tại bằng cú pháp `d[khoa]`, Python sẽ ném ngoại lệ `KeyError`. Để xử lý an toàn:
- `d.get(khoa, mac_dinh)`: Trả về giá trị mặc định nếu khóa không tồn tại mà không ném lỗi.
- `d.setdefault(khoa, mac_dinh)`: Nếu khóa chưa có, tự động gán giá trị mặc định vào từ điển và trả về giá trị đó.
- Lớp `collections.defaultdict`: Tự động khởi tạo giá trị khi truy cập một khóa mới:
  ```python
  from collections import defaultdict

  # Gom nhóm mã phòng theo khu vực
  phong_theo_khu = defaultdict(list)
  phong_theo_khu["Bắc"].append("HN01")
  phong_theo_khu["Bắc"].append("HN02")
  print(phong_theo_khu["Bắc"])  # ['HN01', 'HN02']
  ```

#### Ràng buộc về kiểu khóa trong từ điển (Hashability)
Khóa của từ điển bắt buộc phải là đối tượng **có thể sinh mã băm** (*hashable*). Điều này đồng nghĩa với việc khóa phải là đối tượng bất biến (như chuỗi, số thực, số nguyên, hoặc tuple chứa toàn các phần tử bất biến).

Hàm `hash(obj)` tính toán mã băm nguyên của đối tượng. Một danh sách `[1, 2]` không thể dùng làm khóa vì nó có thể bị đột biến nội dung, làm thay đổi vị trí ô nhớ trong bảng băm:
```python
hash("HN01")  # Hợp lệ
hash((1, 2))  # Hợp lệ
```
```pycon
>>> hash([1, 2])
TypeError: unhashable type: 'list'
```

### 1.4. Tập hợp (Set)
`set` là tập hợp các phần tử không có thứ tự và không chứa phần tử trùng lặp. Mỗi phần tử trong tập hợp phải có tính chất sinh mã băm. Phép kiểm tra thành viên `if x in s:` trên tập hợp đạt độ phức tạp trung bình $O(1)$.

Các phép toán đại số tập hợp giữa hai tập `A` và `B`:
- **Phép hợp (Union)**: Biểu thức `A | B` hoặc `A.union(B)` lấy tất cả các phần tử thuộc ít nhất một trong hai tập hợp.
- **Phép giao (Intersection)**: Biểu thức `A & B` hoặc `A.intersection(B)` lấy các phần tử xuất hiện ở cả hai tập hợp.
- **Phép hiệu (Difference)**: Biểu thức `A - B` hoặc `A.difference(B)` lấy các phần tử thuộc `A` nhưng không thuộc `B`.
- **Phép hiệu đối xứng (Symmetric Difference)**: Biểu thức `A ^ B` lấy các phần tử thuộc `A` hoặc `B` nhưng không thuộc phần giao.

### 1.5. Các hàm tuần tự tích hợp (Built-In Sequence Functions)
- `enumerate(iterable, start=0)`: Trả về từng cặp `(chi_so, gia_tri)`, giúp tránh việc phải khởi tạo và tăng biến đếm thủ công:
  ```python
  for i, ten in enumerate(["Hà Nội", "Đà Nẵng", "TP.HCM"]):
      print(f"{i}: {ten}")
  ```
- `sorted(iterable, key=..., reverse=...)`: Trả về danh sách mới được sắp xếp từ bất kỳ tập hợp khả lặp nào.
- `zip(*iterables)`: Ghép đôi các phần tử có cùng vị trí từ nhiều tập hợp. Chiều dài kết quả bằng chiều dài của tập hợp ngắn nhất.
- `reversed(sequence)`: Trả về một iterator duyệt ngược các phần tử của một dãy mà không cần nhân bản danh sách.

### 1.6. Cú pháp Comprehension
Comprehension cho phép biến đổi và lọc dữ liệu ngắn gọn, diễn đạt rõ ý đồ lập trình:
- **List comprehension**: `[f(x) for x in tap_hop if dieu_kien]`
- **Dict comprehension**: `{khoa(x): gia_tri(x) for x in tap_hop if dieu_kien}`
- **Set comprehension**: `{f(x) for x in tap_hop if dieu_kien}`

```python
# Lọc và viết hoa tên các tỉnh thành có độ dài lớn hơn 6 ký tự
tinh_thanh = ["Hà Nội", "Huế", "Quảng Ninh", "Hải Phòng"]
ket_qua = [t.upper() for t in tinh_thanh if len(t) > 6]
# ['QUẢNG NINH', 'HẢI PHÒNG']
```

Comprehension lồng nhau (*nested comprehensions*) cho phép làm phẳng danh sách hai chiều:
```python
ma_tran = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lam_phang = [x for hang in ma_tran for x in hang if x % 2 == 0]
# [2, 4, 6, 8]
```

---

## 2. Hàm trong Python

Trong kỹ thuật dữ liệu, hàm là đơn vị cơ sở để đóng gói từng bước biến đổi độc lập trong đường ống xử lý.

### 2.1. Không gian tên và quy tắc tìm kiếm LEGB
Khi một biến được gọi trong hàm, Python tìm kiếm tên biến theo quy tắc thứ tự **LEGB**:
1. **L (Local)**: Không gian tên cục bộ bên trong hàm hiện tại.
2. **E (Enclosing)**: Không gian tên của các hàm bao bọc bên ngoài (trong trường hợp hàm lồng nhau).
3. **G (Global)**: Không gian tên toàn cục của tệp mô-đun hiện tại.
4. **B (Built-in)**: Không gian tên chứa các hàm và hằng số tích hợp sẵn của Python (như `len`, `sum`, `range`).

Mọi biến được gán giá trị bên trong hàm mặc định thuộc về phạm vi cục bộ `Local`. Muốn thay đổi giá trị của một biến toàn cục, lập trình viên phải sử dụng từ khóa `global` (tuy nhiên việc lạm dụng biến toàn cục làm mất tính độc lập của hàm và khó kiểm thử).

### 2.2. Trả về nhiều giá trị
Một hàm trong Python có thể trả về nhiều giá trị bằng cách ngăn cách chúng bằng dấu phẩy. Về mặt bản chất, Python đóng gói các giá trị đó thành một `tuple` duy nhất:
```python
def thong_ke_co_ban(ds):
    return min(ds), sum(ds) / len(ds), max(ds)

nho_nhat, trung_binh, lon_nhat = thong_ke_co_ban([10, 20, 30])
```

### 2.3. Hàm là đối tượng hạng nhất (First-Class Functions)
Trong Python, hàm là đối tượng hạng nhất: Hàm có thể được gán cho một biến, được lưu trong danh sách hoặc từ điển, và được truyền vào như đối số của một hàm khác.

Tính chất này cho phép xây dựng đường ống làm sạch dữ liệu linh hoạt:
```python
import re

def xoa_khoang_trang(s):
    return s.strip()

def loai_dau_cau(s):
    return re.sub(r"[!?.]", "", s)

def viet_hoa_dau_tu(s):
    return s.title()

duong_ong_lam_sach = [xoa_khoang_trang, loai_dau_cau, viet_hoa_dau_tu]

def ap_dung_duong_ong(van_ban, cac_ham):
    for f in cac_ham:
        van_ban = f(van_ban)
    return van_ban

chuoi_tho = "  hà NỘI! "
chuoi_sach = ap_dung_duong_ong(chuoi_tho, duong_ong_lam_sach)
print(chuoi_sach)  # 'Hà Nội'
```

### 2.4. Hàm ẩn danh (Lambda Functions)
Hàm lambda là hàm không tên, được định nghĩa bằng một dòng biểu thức duy nhất:
```python
tinh_tong = lambda x, y: x + y
```
Hàm lambda thường được dùng khi cần truyền nhanh một hàm ngắn làm đối số cho các hàm như `sort` hoặc các phương thức ánh xạ của pandas. Tuy nhiên, nếu logic xử lý vượt quá một biểu thức đơn giản, hãy định nghĩa một hàm rõ ràng bằng từ khóa `def` để bảo đảm tính dễ đọc của mã nguồn.

### 2.5. Hàm sinh (Generators) và Thư viện `itertools`
Khi xử lý tệp dữ liệu dung lượng lớn (chẳng hạn vài chục gigabyte), việc nạp toàn bộ dữ liệu vào một danh sách sẽ làm cạn kiệt bộ nhớ RAM. Hàm sinh (*generator*) giải quyết triệt để vấn đề này bằng cơ chế **đánh giá lười biếng** (*lazy evaluation*): Phần tử chỉ được tính toán và sinh ra khi có yêu cầu.

#### Hàm sinh với từ khóa `yield`
Khi một hàm chứa từ khóa `yield`, nó trở thành một hàm sinh. Mỗi khi gặp `yield`, hàm tạm dừng thực thi, trả về giá trị hiện tại cho môi trường gọi và bảo lưu toàn bộ trạng thái cục bộ để sẵn sàng chạy tiếp ở lượt yêu cầu tiếp theo:
```python
def tao_day_binh_phuong(n):
    for i in range(n):
        yield i ** 2

gen = tao_day_binh_phuong(5)
for v in gen:
    print(v, end=" ")
# 0 1 4 9 16
```

#### Biểu thức sinh (Generator Expression)
Cú pháp tương tự list comprehension nhưng đặt trong cặp ngoặc đơn `()`:
```python
tong_binh_phuong = sum(x ** 2 for x in range(1000000))
```
Biểu thức trên không tạo ra một danh sách một triệu phần tử trong RAM mà truyền từng số một vào hàm `sum()`.

#### Thư viện `itertools`
Mô-đun `itertools` cung cấp nhiều công cụ lặp hiệu năng cao:
- `itertools.chain(*iterables)`: Nối liên tiếp nhiều tập hợp mà không nhân bản dữ liệu.
- `itertools.groupby(iterable, key)`: Gom nhóm các phần tử liên tiếp có cùng giá trị khóa (yêu cầu dữ liệu phải được sắp xếp theo khóa trước khi gom nhóm).

### 2.6. Bắt và Xử lý Ngoại lệ (Exception Handling)
Trong phân tích dữ liệu, việc gặp phải các ô dữ liệu rác, chuỗi ký tự sai định dạng là điều tất yếu. Nếu không bắt ngoại lệ, chương trình sẽ lập tức sập và làm gián đoạn toàn bộ đường ống:

```python
def chuyen_sang_so_thuc(gia_tri):
    try:
        return float(gia_tri)
    except (ValueError, TypeError):
        return None
```

Cấu trúc hoàn chỉnh của khối xử lý ngoại lệ:
- `try`: Chứa đoạn mã có nguy cơ phát sinh lỗi.
- `except`: Bắt và xử lý lỗi cụ thể (tránh dùng `except:` trần trụi mà không bắt loại ngoại lệ xác định).
- `else`: Khối mã chỉ được thực thi nếu khối `try` diễn ra suôn sẻ và không có ngoại lệ nào phát sinh.
- `finally`: Khối mã **luôn luôn được thực thi**, kể cả khi có lỗi hay không, thường dùng để đóng tệp hoặc giải phóng tài nguyên mạng.

---

## 3. Thao tác với tệp tin và hệ thống tệp

### 3.1. Mở và đóng tệp an toàn với ngữ cảnh `with`
Khối `with open(...)` giúp đóng tệp khi kết thúc việc đọc. Ví dụ dưới tạo một tệp trong thư mục tạm rồi đọc từng dòng:
```python
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as thu_muc:
    tep = Path(thu_muc) / "du_lieu.txt"
    tep.write_text("Hà Nội\nĐà Nẵng\n", encoding="utf-8")
    cac_dong = []
    with open(tep, mode="r", encoding="utf-8") as f:
        for dong in f:
            cac_dong.append(dong.strip())
    assert cac_dong == ["Hà Nội", "Đà Nẵng"]
```
Khối lệnh `with` bảo đảm rằng tệp tin luôn được đóng an toàn ngay sau khi thoát khỏi khối mã, kể cả khi quá trình đọc tệp phát sinh ngoại lệ đột ngột.

### 3.2. Các phương thức đọc tệp
- `f.read()`: Đọc toàn bộ nội dung tệp thành một chuỗi duy nhất. Chỉ nên dùng khi kích thước tệp nhỏ và vừa vặn với RAM.
- `f.readlines()`: Đọc toàn bộ tệp và trả về danh sách các dòng văn bản.
- `for dong in f:`: Duyệt từng dòng mà không tự nạp cả tệp thành một danh sách. Bộ nhớ sử dụng còn phụ thuộc bộ đệm, độ dài dòng và việc chương trình có giữ lại kết quả của các dòng trước hay không.

### 3.3. Chế độ mở và mã hóa ký tự
- Chế độ mở tệp: Đọc văn bản (`'r'`), ghi đè (`'w'`), ghi tiếp vào cuối (`'a'`), đọc nhị phân (`'rb'`), ghi nhị phân (`'wb'`).
- Mã hóa ký tự: Nếu tệp dùng UTF-8, hãy ghi rõ `encoding="utf-8"`. Với nguồn dùng mã hóa khác, cần chọn đúng mã hóa của nguồn. Giá trị mặc định còn phụ thuộc phiên bản Python và cấu hình, nên không nên dựa vào đó để diễn giải dữ liệu.

---

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 3: Built-In Data Structures, Functions, and Files.
- Python Software Foundation. *Data Structures & itertools: Functions creating iterators for efficient looping*. https://docs.python.org/3/library/itertools.html
- David Beazley. *Python Cookbook*, tái bản lần 3. O'Reilly Media, 2013.

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 4. Bài tập thực hành

::: exercise Bài tập 1: Pipeline làm sạch chuỗi bằng danh sách hàm bậc cao
Một tập dữ liệu văn bản thô chứa tên các địa danh bị lỗi khoảng trắng và dấu câu như sau:
```python
dia_danh_tho = ["  hà NỘI! ", " ĐÀ Nẵng? ", "TP. Hồ Chí Minh  "]
```
Hãy xây dựng một hệ thống làm sạch dữ liệu tuân thủ các yêu cầu sau:
1. Viết ba hàm nhỏ độc lập:
   - `loai_khoang_trang(s)`: Loại bỏ các khoảng trắng thừa ở đầu và cuối chuỗi.
   - `xoa_dau_cau(s)`: Loại bỏ các ký tự dấu câu `!`, `?`, và dấu chấm `.`.
   - `chuan_hoa_chu_hoa(s)`: Chuyển đổi chuỗi về định dạng viết hoa chữ cái đầu mỗi từ (`title`).
2. Gom ba hàm trên vào một danh sách `pipeline = [loai_khoang_trang, xoa_dau_cau, chuan_hoa_chu_hoa]`.
3. Sử dụng List Comprehension kết hợp duyệt qua danh sách hàm trong `pipeline` để biến đổi danh sách `dia_danh_tho` thành danh sách sạch.
:::

::: solution Lời giải
```python
import re

dia_danh_tho = ["  hà NỘI! ", " ĐÀ Nẵng? ", "TP. Hồ Chí Minh  "]

def loai_khoang_trang(s):
    return s.strip()

def xoa_dau_cau(s):
    return re.sub(r"[!?.]", "", s)

def chuan_hoa_chu_hoa(s):
    return s.title()

pipeline = [loai_khoang_trang, xoa_dau_cau, chuan_hoa_chu_hoa]

def lam_sach_chuoi(van_ban):
    for f in pipeline:
        van_ban = f(van_ban)
    return van_ban

dia_danh_sach = [lam_sach_chuoi(s) for s in dia_danh_tho]
print("Kết quả làm sạch:", dia_danh_sach)
```

Kết quả in ra:
- `['Hà Nội', 'Đà Nẵng', 'Tp Hồ Chí Minh']`.
- Mỗi hàm trong pipeline thực hiện đúng một nhiệm vụ duy nhất, giúp mã nguồn dễ dàng mở rộng khi cần thêm các bước chuẩn hóa mới.
:::

::: exercise Bài tập 2: Xử lý tệp log dạng dòng với Generator và Exception Handling
Giả sử bạn cần đọc một luồng dữ liệu giao dịch từ nhật ký hệ thống. Dữ liệu gồm các dòng văn bản ngăn cách bởi dấu phẩy chứa `ma_giao_dich,so_tien`. Một số dòng bị lỗi dữ liệu chuỗi hoặc thiếu giá trị:
```python
du_lieu_log = [
    "101,250",
    "102,invalid",
    "103,400",
    "104,"
]
```
1. Hãy viết một hàm sinh `phan_tich_log(cac_dong)` sử dụng từ khóa `yield` để duyệt qua từng dòng.
2. Với mỗi dòng, tách trường dữ liệu bằng dấu phẩy. Sử dụng cấu trúc `try/except ValueError` để chuyển đổi trường số tiền sang số nguyên `int`. Nếu dòng dữ liệu hợp lệ, trả về một tuple `(ma_gd, so_tien)`.
3. Nếu dòng dữ liệu bị lỗi chuyển đổi kiểu hoặc thiếu trường, hàm sẽ bỏ qua dòng đó một cách an toàn mà không làm sập chương trình.
4. Chuyển toàn bộ đầu ra của hàm sinh thành danh sách và tính tổng số tiền của các giao dịch hợp lệ.
:::

::: solution Lời giải
```python
du_lieu_log = [
    "101,250",
    "102,invalid",
    "103,400",
    "104,"
]

def phan_tich_log(cac_dong):
    for dong in cac_dong:
        thanh_phan = dong.strip().split(",")
        if len(thanh_phan) == 2:
            try:
                ma_gd = int(thanh_phan[0])
                so_tien = int(thanh_phan[1])
                yield ma_gd, so_tien
            except ValueError:
                continue

# Khởi tạo hàm sinh và trích xuất kết quả
ds_hop_le = list(phan_tich_log(du_lieu_log))
tong_tien = sum(tien for ma, tien in ds_hop_le)

print("Các giao dịch hợp lệ:", ds_hop_le)
print("Tổng số tiền hợp lệ:", tong_tien)
```

Kết quả:
- Dòng `"102,invalid"` và dòng `"104,"` phát sinh lỗi `ValueError` khi ép kiểu số nguyên và được bỏ qua an toàn.
- `ds_hop_le`: `[(101, 250), (103, 400)]`.
- Tổng số tiền hợp lệ: $250 + 400 = 650$.
:::

::: exercise Bài tập 3: Gom nhóm dữ liệu và đếm tần suất với defaultdict
Cho danh sách các bản ghi doanh thu theo khu vực thị trường:
```python
giao_dich = [
    ("Bắc", 100),
    ("Nam", 200),
    ("Bắc", 150),
    ("Trung", 80),
    ("Nam", 50)
]
```
1. Sử dụng lớp `defaultdict` từ thư viện `collections` để tính tổng doanh thu theo từng khu vực.
2. Sử dụng `defaultdict(list)` để gom toàn bộ các giao dịch riêng lẻ của từng khu vực vào danh sách tương ứng.
3. Chuyển kết quả về từ điển chuẩn và in ra màn hình.
:::

::: solution Lời giải
```python
from collections import defaultdict

giao_dich = [
    ("Bắc", 100),
    ("Nam", 200),
    ("Bắc", 150),
    ("Trung", 80),
    ("Nam", 50)
]

# 1. Tính tổng doanh thu theo khu vực
tong_doanh_thu = defaultdict(int)
for khu, tien in giao_dich:
    tong_doanh_thu[khu] += tien

# 2. Gom danh sách giao dịch theo khu vực
ds_giao_dich = defaultdict(list)
for khu, tien in giao_dich:
    ds_giao_dich[khu].append(tien)

print("Tổng doanh thu từng khu:", dict(tong_doanh_thu))
print("Chi tiết các giao dịch:", dict(ds_giao_dich))
```

Kết quả:
- Tổng doanh thu: `{'Bắc': 250, 'Nam': 250, 'Trung': 80}`.
- Chi tiết giao dịch: `{'Bắc': [100, 150], 'Nam': [200, 50], 'Trung': [80]}`.
- Cơ chế `defaultdict` giúp loại bỏ hoàn toàn các câu lệnh kiểm tra điều kiện tồn tại của khóa trước khi cập nhật dữ liệu.
:::

<!--@include: ../../../raw_materials/xu-ly-du-lieu/practice/iai-a-chapter-3.md-->

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 3: Built-In Data Structures, Functions, and Files.
- Python Software Foundation. *Data Structures & itertools: Functions creating iterators for efficient looping*. https://docs.python.org/3/library/itertools.html
- David Beazley. *Python Cookbook*, tái bản lần 3. O'Reilly Media, 2013.

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>
