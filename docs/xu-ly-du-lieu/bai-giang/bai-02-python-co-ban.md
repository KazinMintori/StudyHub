---
course: xu-ly-du-lieu
lecture: bai-02-python-co-ban
section: lecture
title: "Python, IPython và Jupyter Notebook"
prerequisites: []
lessonStatus: ready
hasChapterExercises: true
description: "Trình thông dịch Python, môi trường IPython và Jupyter, ngữ nghĩa hướng đối tượng, kiểu vô hướng, chuỗi byte, thời gian và điều khiển luồng."
---


<div class="lecture-notes-content">

## 1. Trình thông dịch Python và môi trường dòng lệnh

Bạn nhận một bản ghi nhiệt độ thời tiết lưu dưới dạng chuỗi: `'Hà Nội: 28.5°C'`. Làm thế nào để trích xuất phần số, chuyển sang số thực để so sánh ngưỡng, và định dạng lại ngày đo mà không làm hỏng dữ liệu ký tự? Việc nắm vững kiểu dữ liệu và cách Python quản lý vùng nhớ là bước đầu tiên để viết mã xử lý dữ liệu chính xác.

Ta có thể chạy một tệp Python hoặc thử từng lệnh trong phiên tương tác. Khi giải thích bytecode dưới đây, ta xét cách triển khai CPython:
- **Chế độ kịch bản (Script mode)**: Toàn bộ mã nguồn được lưu trữ trong một tệp văn bản có phần mở rộng `.py` và được thực thi bằng lệnh `python chuong_trinh.py`. Trong CPython, khi thực thi tệp trực tiếp, mã nguồn được biên dịch thành mã byte (*bytecode*) trong bộ nhớ và thực thi trên máy ảo mà không mặc nhiên ghi tệp `.pyc` vào thư mục `__pycache__`. Thư mục `__pycache__` chủ yếu dùng để lưu trữ bytecode đã biên dịch của các mô-đun được nạp bằng `import` nhằm tăng tốc độ nạp ở các lần chạy sau.
- **Chế độ tương tác (Interactive mode)**: Khởi chạy bằng lệnh `python` trên cửa sổ dòng lệnh (terminal). Môi trường mở ra vòng lặp đọc, đánh giá và in kết quả (*Read-Eval-Print Loop - REPL*). Người dùng nhập từng câu lệnh và nhận phản hồi tức thì.

Python có sẵn các công cụ tra cứu như `help` và `dir`. IPython bổ sung cú pháp tra cứu, lịch sử và nhiều lệnh phục vụ thử nghiệm, gỡ lỗi, đo thời gian trong cùng phiên làm việc.

---

## 2. Nền tảng tính toán tương tác với IPython và Jupyter Notebook

IPython ra đời nhằm tối ưu hóa trải nghiệm lập trình khám phá dữ liệu. IPython vừa đóng vai trò như một hệ vỏ tương tác nâng cao trên dòng lệnh, vừa là hạt nhân tính toán (*kernel*) chạy ngầm bên dưới Jupyter Notebook.

### 2.1. Khởi chạy IPython và Jupyter
Để mở giao diện dòng lệnh tương tác IPython, bạn gõ lệnh trên terminal:
```bash
ipython
```
Giao diện dòng lệnh hiển thị dấu nhắc `In [1]:`, sẵn sàng tiếp nhận các câu lệnh Python kèm theo các cú pháp mở rộng đặc thù.

Để khởi chạy giao diện sổ tay tính toán trên trình duyệt web, bạn sử dụng lệnh:
```bash
jupyter notebook
```
Lệnh này khởi tạo máy chủ cục bộ và mở giao diện quản lý tệp trên trình duyệt, cho phép tạo các tệp sổ tay `.ipynb`.

### 2.2. Tự động hoàn thành với phím Tab (Tab Completion)
Một trong những tính năng gia tốc công việc quan trọng nhất của IPython là phím `Tab`. Khi gõ một phần của định danh và nhấn `Tab`, hệ thống sẽ tự động quét không gian tên hiện tại để gợi ý:
- **Tên biến và hàm**: Nhập các ký tự đầu và bấm `Tab` để hoàn thiện tên biến dài.
- **Thuộc tính và phương thức của đối tượng**: Sau dấu chấm `obj.`, bấm `Tab` để xem các gợi ý có thể tra cứu trong môi trường đang dùng.
- **Đường dẫn tệp tin**: Khi viết chuỗi đường dẫn tệp trong dấu ngoặc kép, bấm `Tab` sẽ duyệt các tệp và thư mục trong hệ thống tệp cục bộ.
- **Tham số hàm**: Nhập dấu mở ngoặc đơn `ten_ham(` rồi bấm `Shift + Tab` (trong Jupyter) để mở nhanh bảng kê khai các tham số và giá trị mặc định.

### 2.3. Tra cứu thông tin đối tượng (Introspection)
IPython cho phép khám phá cấu trúc nội tại của các đối tượng Python bằng ký tự hỏi chấm `?`:

1. **Xem tài liệu và kiểu đối tượng (`?`)**:
   Đặt dấu `?` trước hoặc sau tên một biến, hàm hoặc mô-đun để hiển thị bảng tóm tắt gồm kiểu dữ liệu, chuỗi tài liệu (*docstring*) và chữ ký hàm:
   ```ipython
   import numpy as np
   np.array?
   ```
2. **Xem mã nguồn gốc (`??`)**:
   Khi mã nguồn của đối tượng có thể truy cập được (chẳng hạn hàm được viết bằng Python thuần trong tệp hoặc phiên làm việc), đặt hai dấu hỏi chấm `??` sẽ hiển thị toàn bộ khối mã nguồn cài đặt:
   ```python
   def tinh_trung_binh(ds):
       """Tính trung bình cộng của danh sách số thực."""
       return sum(ds) / len(ds) if ds else 0.0
   ```
   ```ipython
   tinh_trung_binh??
   ```
   Nếu đối tượng là hàm tích hợp sẵn của CPython hoặc được biên dịch bằng C mà không có mã nguồn Python kèm theo, `??` sẽ chỉ hiển thị chuỗi tài liệu tương tự `?`.
3. **Tìm kiếm bằng ký tự đại diện (`*`)**:
   Kết hợp dấu `?` với ký tự đại diện `*` để tra cứu nhanh các hàm có tên chứa một mẫu từ khóa nhất định trong thư viện:
   ```ipython
   np.*load*?
   ```
   Lệnh trên sẽ liệt kê tất cả các hàm trong NumPy có chứa từ khóa `load`, chẳng hạn `np.load`, `np.loadtxt`.

---

## 3. Ngữ nghĩa cốt lõi của ngôn ngữ Python

### 3.1. Thụt lề định hình khối mã, không dùng ngoặc nhọn
Khác với C, C++ hay Java dùng cặp ngoặc nhọn `{}` để giới hạn khối lệnh, Python sử dụng **khoảng trắng thụt lề** (*indentation*) để phân định phạm vi cấu trúc logic. Chuẩn mực quy ước (PEP 8) quy định sử dụng đúng 4 khoảng trắng cho mỗi cấp thụt lề. Dấu hai chấm `:` ở cuối dòng mở đầu cho một khối mã thụt lề mới.

### 3.2. Mọi thứ đều là đối tượng (Everything is an Object)
Số, chuỗi, danh sách, hàm và mô-đun đều là đối tượng Python. Mỗi đối tượng có định danh, kiểu và giá trị. `id(obj)` cho một định danh ổn định trong thời gian đối tượng còn tồn tại, còn `type(obj)` cho biết kiểu. Không nên coi định danh là một địa chỉ bộ nhớ có ý nghĩa chung cho mọi cách triển khai Python.

### 3.3. Biến và cơ chế gắn tham số với đối tượng
Trong Python, biến không phải là một ô nhớ cố định chứa trực tiếp dữ liệu. Biến thực chất chỉ là một **chiếc nhãn dán tham chiếu** trỏ tới đối tượng nằm trên bộ nhớ heap.

Khi thực hiện phép gán:
```python
a = [10, 20, 30]
b = a
```
Python không hề nhân đôi danh sách `[10, 20, 30]`. Phép gán chỉ gắn thêm nhãn `b` vào cùng một đối tượng danh sách mà `a` đang trỏ tới. Vì vậy:
```python
b.append(40)
print(a)  # [10, 20, 30, 40]
```
Mọi thay đổi nội dung qua nhãn `b` đều phản ánh ngay lập tức qua nhãn `a`.

Khi truyền đối số vào hàm, Python áp dụng cơ chế **gắn tên tham số với đối tượng** (*call by object reference* hay *call by sharing*). Cần phân biệt rõ:
- Nếu trong thân hàm ta gọi phương thức làm biến đổi một đối tượng khả biến (chẳng hạn `param.append(...)`), đối tượng gốc ở môi trường gọi sẽ thay đổi vì cả hai cùng tham chiếu tới một vùng nhớ.
- Nếu trong thân hàm ta thực hiện phép gán lại biến tham số (chẳng hạn `param = [1, 2, 3]`), phép gán này chỉ thay đổi đối tượng mà biến cục bộ bên trong hàm trỏ tới, hoàn toàn không làm thay đổi biến ở môi trường gọi. Cơ chế này khác với truyền biến bằng tham chiếu (*call by reference*).

### 3.4. Tham chiếu động và kiểm tra kiểu mạnh (Dynamic References, Strong Types)
Python là ngôn ngữ có **hệ thống kiểu động** (*dynamically typed*): Người lập trình không cần khai báo kiểu của biến trước khi dùng. Một biến có thể trỏ tới số nguyên, sau đó trỏ sang chuỗi ký tự mà không gặp lỗi biên dịch:
```python
x = 100      # x trỏ tới số nguyên
x = "Python" # x trỏ sang chuỗi ký tự
```
Đồng thời, Python là ngôn ngữ có **kiểu mạnh** (*strongly typed*): Trình thông dịch không tự ý ép kiểu ngầm giữa các kiểu dữ liệu không tương thích. Biểu thức sau sẽ ném lỗi:
```pycon
>>> ket_qua = "Điểm số: " + 10
TypeError: can only concatenate str (not "int") to str
```
Có thể dùng `str(10)` để chuyển số thành chuỗi trước khi nối, hoặc dùng f-string để định dạng kết quả.

### 3.5. Thuộc tính, phương thức và cơ chế Duck Typing
Các đối tượng trong Python chứa cả dữ liệu (thuộc tính - *attributes*) và các hàm xử lý gắn liền (phương thức - *methods*). Ta có thể kiểm tra sự tồn tại của thuộc tính và trích xuất chúng bằng các hàm tích hợp: `hasattr(obj, 'ten')`, `getattr(obj, 'ten')`.

Python áp dụng triết lý thiết kế **Duck Typing**: Thay vì kiểm tra đối tượng có thuộc đúng một lớp cụ thể hay không (`isinstance(x, list)`), ta kiểm tra đối tượng đó có hỗ trợ các hành vi cần thiết hay không. Ví dụ: Để biết một đối tượng có thể duyệt được bằng vòng lặp `for` hay không, ta chỉ cần kiểm tra xem đối tượng đó có thể chuyển qua hàm `iter(obj)` hay không, thay vì bắt buộc nó phải là kiểu danh sách.

### 3.6. Phân biệt đối tượng khả biến (Mutable) và bất biến (Immutable)
Tính khả biến là ranh giới kỹ thuật quan trọng trong xử lý dữ liệu:
- **Đối tượng khả biến (*Mutable*)**: Nội dung bên trong có thể được thêm bớt, sửa đổi mà không làm thay đổi định danh `id` của đối tượng. Bao gồm: `list`, `dict`, `set`, và mảng `ndarray` của NumPy.
- **Đối tượng bất biến (*Immutable*)**: Không thể sửa trực tiếp giá trị hay thay các phần tử của chính đối tượng đó. Ví dụ gồm `int`, `float`, `bool`, `str`, `tuple`, `bytes`, `frozenset`. Một thao tác có thể trả đối tượng mới hoặc dùng lại đối tượng có sẵn, nên không suy quan hệ định danh chỉ từ tính bất biến.

Tuple không cho thay các phần tử của nó, nhưng một phần tử là list vẫn có thể đổi nội dung. Khả năng làm khóa từ điển là tính chất hashable: Mã băm phải ổn định và các đối tượng bằng nhau phải có cùng mã băm. Chẳng hạn tuple chứa list không hashable, còn một số đối tượng tùy biến khả biến vẫn dùng định danh để băm. Không nên đồng nhất hashable với bất biến hoặc an toàn khi chia sẻ giữa các luồng.

---

## 4. Các kiểu dữ liệu vô hướng (Scalar Types)

### 4.1. Kiểu số học: Số nguyên, số thực và số phức
- **Số nguyên (`int`)**: Trong Python 3, số nguyên có độ chính xác tùy ý (*arbitrary precision*). Số nguyên có thể tăng kích thước không giới hạn cho tới khi cạn kiệt bộ nhớ hệ thống, loại bỏ hoàn toàn nguy cơ tràn số nguyên kinh điển thường gặp trong C/C++.
- **Số thực (`float`)**: Biểu diễn số dấu phẩy động độ chính xác kép 64-bit theo chuẩn IEEE 754. Do cách biểu diễn nhị phân, các số thập phân hữu hạn như $0{,}1$ không thể biểu diễn chính xác tuyệt đối trong bộ nhớ:
  ```python
  0.1 + 0.2 == 0.3  # Trả về False vì 0.1 + 0.2 = 0.30000000000000004
  ```
  Khi so sánh hai số thực trong tính toán, luôn sử dụng hàm so sai số nhỏ như `math.isclose(a, b)` hoặc `np.isclose(a, b)`.
- **Số phức (`complex`)**: Biểu diễn dạng phần thực và phần ảo với hậu tố `j`, ví dụ `z = 3 + 4j`.

### 4.2. Kiểu chuỗi (`str`) và định dạng f-string
Chuỗi trong Python là một dãy bất biến chứa các ký tự Unicode.
- **Chuỗi thô (*Raw strings*)**: Đặt tiền tố `r` trước chuỗi để vô hiệu hóa các ký tự thoát đặc biệt, rất hữu ích khi viết biểu thức chính quy (Regex) hoặc đường dẫn tệp trên Windows: `r"C:\Users\TenThucMuc"`.
- **Định dạng chuỗi với f-string**: Cú pháp chuẩn mực và tối ưu tốc độ nhất trong Python hiện đại:
  ```python
  gia = 1850000.5
  ty_le = 0.1275
  print(f"Giá phòng: {gia:,.0f} đ | Tỷ lệ lấp đầy: {ty_le:.1%}")
  # Giá phòng: 1,850,001 đ | Tỷ lệ lấp đầy: 12.8%
  ```

### 4.3. Kiểu Byte và Chuỗi Ký tự Unicode
Trong xử lý dữ liệu, phân biệt rạch ròi giữa văn bản người đọc (`str`) và dữ liệu nhị phân (`bytes`) là yêu cầu bắt buộc:
- **`str`**: Dãy các ký tự trừu tượng Unicode. Mỗi ký tự đại diện cho một mã điểm (*code point*).
- **`bytes`**: Dãy các số nguyên 8-bit không dấu có giá trị từ $0$ đến $255$, phản ánh chính xác chuỗi byte lưu trên đĩa hoặc truyền qua cáp mạng.

Chuyển đổi qua lại giữa hai dạng này thông qua quá trình mã hóa (*encoding*) và giải mã (*decoding*), với chuẩn mã hóa toàn cầu là `UTF-8`:
```python
van_ban = "Hà Nội"
# Mã hóa chuỗi ký tự thành dãy byte
du_lieu_byte = van_ban.encode("utf-8")
print(du_lieu_byte)  # b'H\xc3\xa0 N\xe1\xbb\x99i'
print(len(van_ban))  # 6 ký tự
print(len(du_lieu_byte))  # 9 byte vì các ký tự 'à', 'ộ' chiếm nhiều byte

# Giải mã byte trở lại chuỗi ký tự
chuoi_goc = du_lieu_byte.decode("utf-8")
assert chuoi_goc == van_ban
```

### 4.4. Giá trị `None` và bẫy chân trị
`None` là đối tượng đơn nhất (*singleton*) thuộc kiểu `NoneType`, dùng để biểu thị sự vắng mặt của giá trị.
- Kiểm tra một biến có mang giá trị `None` hay không phải luôn dùng toán tử danh tính `is` hoặc `is not`, tuyệt đối không dùng `==`:
  ```python
  ket_qua = None
  if ket_qua is None:
      print("Dữ liệu bị thiếu!")
  ```
- **Bẫy chân trị (*Truthiness vs Falsiness*)**: Khi đặt trong câu lệnh điều kiện `if`, Python đánh giá các giá trị sau là sai (`False`): `None`, số `0`, số `0.0`, chuỗi rỗng `""`, danh sách rỗng `[]`, từ điển rỗng `{}`.
  Cần hết sức cẩn trọng: Số $0$ mang giá trị số học hợp lệ nhưng vẫn bị coi là `False`. Đoạn mã sau sẽ mắc lỗi nghiêm trọng khi lọc số liệu:
  ```python
  ds_gia = [0.0, 100.0, None]
  gia_hop_le = []
  for g in ds_gia:
      if g is not None:
          gia_hop_le.append(g)
  assert gia_hop_le == [0.0, 100.0]
  ```

### 4.5. Ngày tháng và Thời gian (`datetime`)
Mô-đun `datetime` cung cấp các kiểu dữ liệu để biểu diễn thời gian:
- `datetime.datetime`: Lưu trữ đầy đủ cả ngày, tháng, năm, giờ, phút, giây và micro giây.
- `datetime.date`: Chỉ lưu ngày, tháng, năm.
- `datetime.time`: Chỉ lưu thông tin thời gian trong ngày.
- `datetime.timedelta`: Biểu diễn khoảng cách chênh lệch giữa hai mốc thời gian.

```python
from datetime import datetime, timedelta

# Chuyển chuỗi thành đối tượng thời gian (strptime: string parse time)
chuoi_ngay = "2026-03-01 14:30:00"
moc_tg = datetime.strptime(chuoi_ngay, "%Y-%m-%d %H:%M:%S")

# Cộng thêm một khoảng thời gian
tg_tuong_lai = moc_tg + timedelta(days=2, hours=3)

# Định dạng đối tượng thời gian thành chuỗi (strftime: string format time)
chuoi_xuat = tg_tuong_lai.strftime("%d/%m/%Y lúc %H:%M")
print(chuoi_xuat)  # 03/03/2026 lúc 17:30
```

---

## 5. Cấu trúc điều khiển luồng (Control Flow)

### 5.1. Cấu trúc rẽ nhánh `if`, `elif`, và `else`
Python kiểm tra tuần tự các biểu thức điều kiện từ trên xuống dưới. Ngay khi một nhánh thỏa mãn chân trị, khối mã bên trong sẽ được thực thi và toàn bộ các nhánh còn lại bị bỏ qua:
```python
diem = 7.5
if diem >= 8.5:
    xep_loai = "Giỏi"
elif diem >= 7.0:
    xep_loai = "Khá"
elif diem >= 5.0:
    xep_loai = "Trung bình"
else:
    xep_loai = "Yếu"
```

Python hỗ trợ cú pháp so sánh chuỗi gọn gàng: `0 <= diem <= 10`.

Biểu thức ba ngôi (*ternary expression*) cho phép viết phép gán có điều kiện ngắn gọn trên một dòng:
```python
trang_thai = "Đạt" if diem >= 5.0 else "Trượt"
```

### 5.2. Vòng lặp `for` và dãy số `range`
Vòng lặp `for` trong Python dùng để duyệt qua các phần tử của một tập hợp dữ liệu khả lặp:
```python
doanh_thu = [120, 150, 180, 200]
tong = 0
for dt in doanh_thu:
    tong += dt
```

- Lệnh `continue`: Bỏ qua các câu lệnh còn lại trong lượt lặp hiện tại để chuyển ngay sang lượt tiếp theo.
- Lệnh `break`: Lập tức thoát hoàn toàn khỏi vòng lặp `for`.

Hàm `range(start, stop, step)` tạo đối tượng mô tả một dãy số nguyên. Nó không cấp phát danh sách chứa toàn bộ dãy mà cung cấp giá trị khi được duyệt:
```python
# Duyệt các số chẵn từ 0 đến 8
for i in range(0, 10, 2):
    print(i, end=" ")
# 0 2 4 6 8
```

### 5.3. Vòng lặp `while` và câu lệnh `pass`
Vòng lặp `while` tiếp tục thực thi chừng nào biểu thức điều kiện vẫn giữ chân trị `True`. Cần bảo đảm có cơ chế cập nhật biến điều kiện để tránh rơi vào vòng lặp vô tận.

Câu lệnh `pass` là một câu lệnh rỗng (*no-op*), đóng vai trò giữ chỗ khi cú pháp của Python đòi hỏi phải có một khối mã nhưng bạn chưa muốn thực hiện hành động nào:
```python
for gia_tri in [None, 10]:
    if gia_tri is None:
        pass
    else:
        print(gia_tri)
```

---

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 2: Python Language Basics, IPython, and Jupyter Notebooks.
- Python Software Foundation. *The Python Standard Library: Built-in Types & datetime*. https://docs.python.org/3/library/
- Fernando Pérez, Brian E. Granger. *IPython: A System for Interactive Scientific Computing*. Computing in Science & Engineering, 2007.

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 6. Bài tập thực hành

::: exercise Bài tập 1: Tham chiếu đối tượng, tính đột biến và sao chép nông
Cho đoạn mã Python sau:
```python
a = [1, 2, [3, 4]]
b = a
c = a.copy()

b.append(5)
c[2].append(6)
```
1. Xác định giá trị của danh sách `a`, `b`, và `c` sau khi hoàn thành đoạn mã trên.
2. Giải thích vì sao thao tác `c[2].append(6)` trên danh sách `c` lại làm thay đổi phần tử bên trong danh sách `a`.
3. Cần sử dụng công cụ gì trong Python để tạo ra một bản sao hoàn toàn độc lập, sao cho thao tác trên các phần tử con không ảnh hưởng tới dữ liệu gốc?
:::

::: solution Lời giải
1. Giá trị sau khi thực thi:
   - `a`: `[1, 2, [3, 4, 6], 5]`
   - `b`: `[1, 2, [3, 4, 6], 5]`
   - `c`: `[1, 2, [3, 4, 6]]`
2. Giải thích cơ chế bộ nhớ:
   - Phép gán `b = a` không tạo đối tượng mới, vì `a` và `b` cùng tham chiếu tới một danh sách. Do đó, `b.append(5)` làm `a` nhận thêm phần tử $5$.
   - Phương thức `.copy()` của danh sách là phép **sao chép nông** (*shallow copy*). Nó tạo một danh sách vỏ ngoài mới `c`, nhưng các phần tử con bên trong (như danh sách `[3, 4]`) vẫn chỉ là các con trỏ trỏ tới cùng một đối tượng danh sách con trong RAM. Khi gọi `c[2].append(6)`, đối tượng danh sách con chung đó bị biến đổi, dẫn đến `a[2]` cũng hiển thị `[3, 4, 6]`.
3. Để tạo bản sao độc lập hoàn toàn ở mọi tầng lồng nhau, ta sử dụng hàm `copy.deepcopy()` từ mô-đun thư viện chuẩn `copy`:
   ```python
   import copy
   c = copy.deepcopy(a)
   ```
:::

::: exercise Bài tập 2: Xử lý chuỗi byte và Unicode khi làm sạch dữ liệu
Một chuỗi văn bản ghi nhận nhiệt độ thời tiết tại Việt Nam có nội dung:
```python
s = "Hà Nội - 25°C"
```
1. Chuỗi `s` chứa bao nhiêu ký tự Unicode (`len(s)`)?
2. Hãy mã hóa chuỗi `s` thành dãy byte sử dụng chuẩn mã hóa `UTF-8`. Dãy byte thu được có độ dài bao nhiêu byte? Giải thích vì sao số lượng byte lại lớn hơn số lượng ký tự.
3. Giải mã dãy byte đó trở lại chuỗi ký tự ban đầu và viết câu lệnh kiểm tra sự tương đương.
:::

::: solution Lời giải
```python
s = "Hà Nội - 25°C"

# 1. Số ký tự Unicode
so_ky_tu = len(s)
print(f"Số ký tự Unicode: {so_ky_tu}")

# 2. Mã hóa sang byte UTF-8
b_utf8 = s.encode("utf-8")
so_byte = len(b_utf8)
print(f"Dãy byte: {b_utf8}")
print(f"Độ dài theo byte: {so_byte} bytes")

# 3. Giải mã trở lại chuỗi
s_khoi_phuc = b_utf8.decode("utf-8")
assert s_khoi_phuc == s
print("Khôi phục thành công!")
```

Kết quả phân tích:
- `so_ky_tu`: 13 ký tự (gồm cả các dấu cách, dấu gạch nối và ký hiệu độ).
- `b_utf8`: `b'H\xc3\xa0 N\xe1\xbb\x99i - 25\xc2\xb0C'`.
- `so_byte`: 17 byte.
- Giải thích: Trong chuẩn mã hóa `UTF-8`, các ký tự mã ASCII cơ bản (như `H`, `N`, `i`, dấu cách, số `2`, `5`, chữ `C`) chiếm đúng 1 byte mỗi ký tự. Tuy nhiên, các ký tự có dấu tiếng Việt và ký hiệu đặc biệt chiếm nhiều hơn 1 byte: Ký tự `'à'` chiếm 2 byte (`\xc3\xa0`), ký tự `'ộ'` chiếm 3 byte (`\xe1\xbb\x99`), và ký hiệu độ `'°'` chiếm 2 byte (`\xc2\xb0`). Do đó tổng dung lượng lưu trữ tăng thêm 4 byte so với số lượng ký tự ban đầu.
:::

::: exercise Bài tập 3: Tính toán khoảng thời gian và lọc dữ liệu với datetime
Cho danh sách các mốc thời gian phát sinh giao dịch ở định dạng chuỗi:
```python
giao_dich_str = [
    "2026-03-01 08:30:00",
    "2026-03-01 10:15:00",
    "2026-03-02 14:00:00",
    "2026-03-05 09:00:00"
]
```
1. Hãy chuyển đổi danh sách chuỗi trên thành danh sách các đối tượng `datetime.datetime`.
2. Lấy mốc thời gian đầu tiên làm điểm xuất phát $T_0$. Tính khoảng cách thời gian (dưới dạng đối tượng `timedelta`) từ $T_0$ đến giao dịch thứ ba trong danh sách.
3. Sử dụng cấu trúc điều khiển luồng để lọc ra tất cả các giao dịch diễn ra trong vòng không quá 48 giờ kể từ mốc thời gian $T_0$.
:::

::: solution Lời giải
```python
from datetime import datetime, timedelta

giao_dich_str = [
    "2026-03-01 08:30:00",
    "2026-03-01 10:15:00",
    "2026-03-02 14:00:00",
    "2026-03-05 09:00:00"
]

# 1. Chuyển đổi sang datetime
dinh_dang = "%Y-%m-%d %H:%M:%S"
ds_tg = [datetime.strptime(t, dinh_dang) for t in giao_dich_str]

# 2. Tính khoảng cách thời gian từ T0 đến giao dịch thứ ba (chỉ số 2)
t0 = ds_tg[0]
khoang_cach = ds_tg[2] - t0
print(f"Khoảng cách thời gian: {khoang_cach}")

# 3. Lọc các giao dịch trong vòng không quá 48 giờ
gioi_han_48h = timedelta(hours=48)
trong_48h = [t.strftime(dinh_dang) for t in ds_tg if (t - t0) <= gioi_han_48h]

print(f"Các giao dịch trong vòng 48 giờ: {trong_48h}")
```

Kết quả:
- Khoảng cách thời gian từ giao dịch 1 (`08:30:00` ngày 01/03) đến giao dịch 3 (`14:00:00` ngày 02/03) là 1 ngày, 5 giờ và 30 phút (`timedelta(days=1, seconds=19800)`).
- Giao dịch thứ tư diễn ra vào ngày 05/03 (sau 96 giờ 30 phút), vượt quá ngưỡng 48 giờ.
- Danh sách giao dịch hợp lệ thỏa mãn điều kiện gồm 3 giao dịch đầu tiên: `"2026-03-01 08:30:00"`, `"2026-03-01 10:15:00"`, và `"2026-03-02 14:00:00"`.
:::

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 2: Python Language Basics, IPython, and Jupyter Notebooks.
- Python Software Foundation. *The Python Standard Library: Built-in Types & datetime*. https://docs.python.org/3/library/
- Fernando Pérez, Brian E. Granger. *IPython: A System for Interactive Scientific Computing*. Computing in Science & Engineering, 2007.

</div>
