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

<!-- worked-example bai-02-python-co-ban-worked-1 -->

::: example Tra cứu chữ ký hàm và tham số mặc định bằng inspect.signature

Khi xây dựng đường ống xử lý dữ liệu động, chương trình thường nhận các hàm tùy biến từ bên ngoài mà không biết trước số lượng tham số cần thiết. Để gọi hàm an toàn, ta cần kiểm tra xem đối tượng có thể gọi được hay không và trích xuất danh sách các tham số của nó. Thư viện chuẩn `inspect` cung cấp công cụ tra cứu cấu trúc hàm tương tự cơ chế của IPython.

```python
import inspect

def tinh_chiet_khau(don_gia, ty_le=0.1, ma_giam="SUMMER"):
    """Tính số tiền được giảm dựa trên đơn giá và tỷ lệ."""
    return don_gia * ty_le

sig = inspect.signature(tinh_chiet_khau)
print(f"Hàm có thể gọi: {callable(tinh_chiet_khau)}")
print(f"Chữ ký đầy đủ: {sig}")
for ten, p in sig.parameters.items():
    md = "không có" if p.default is inspect.Parameter.empty else p.default
    print(f"Tham số {ten:<10}: mặc định = {md}")
```

Kết quả khi chạy đoạn mã trên:

```text
Hàm có thể gọi: True
Chữ ký đầy đủ: (don_gia, ty_le=0.1, ma_giam='SUMMER')
Tham số don_gia   : mặc định = không có
Tham số ty_le     : mặc định = 0.1
Tham số ma_giam   : mặc định = SUMMER
```

`inspect.signature` đọc chữ ký của hàm mà không gọi hàm đó. Đối tượng `Signature` mô tả các tham số, giá trị mặc định và chú thích trả về nếu có. Tên của hàm không nằm trong chuỗi chữ ký được in ở đây.

Thuộc tính `parameters` của đối tượng `Signature` trả về một từ điển có thứ tự ánh xạ từ tên tham số sang đối tượng `Parameter` tương ứng. Mỗi tham số cho phép kiểm tra giá trị mặc định thông qua thuộc tính `default`.

Trong ví dụ này, tham số `don_gia` không có giá trị mặc định, nên thuộc tính `default` của nó mang giá trị đặc biệt `inspect.Parameter.empty`. Đoạn mã nhận biết điều này và chuyển thành nhãn không có, trong khi `ty_le` nhận `0.1` và `ma_giam` nhận chuỗi `'SUMMER'`.

`callable` cho biết đối tượng có thể được gọi theo cú pháp `doi_tuong(...)`. Kết quả `True` chưa bảo đảm một lời gọi cụ thể có đủ đối số hoặc đúng kiểu dữ liệu. Trong ví dụ, chữ ký cho biết phải cung cấp `don_gia`, còn hai tham số sau đã có mặc định. `ma_giam` xuất hiện trong chữ ký nhưng thân hàm chưa dùng nó để đổi kết quả.

:::

<!-- /worked-example -->

## 3. Ngữ nghĩa cốt lõi của ngôn ngữ Python

### 3.1. Thụt lề định hình khối mã, không dùng ngoặc nhọn
Khác với C, C++ hay Java dùng cặp ngoặc nhọn `{}` để giới hạn khối lệnh, Python sử dụng **khoảng trắng thụt lề** (*indentation*) để phân định phạm vi cấu trúc logic. Chuẩn mực quy ước (PEP 8) quy định sử dụng đúng 4 khoảng trắng cho mỗi cấp thụt lề. Dấu hai chấm `:` ở cuối dòng mở đầu cho một khối mã thụt lề mới.

### 3.2. Mọi thứ đều là đối tượng (Everything is an Object)
Số, chuỗi, danh sách, hàm và mô-đun đều là đối tượng Python. Mỗi đối tượng có định danh, kiểu và giá trị. `id(obj)` cho một định danh ổn định trong thời gian đối tượng còn tồn tại, còn `type(obj)` cho biết kiểu. Không nên coi định danh là một địa chỉ bộ nhớ có ý nghĩa chung cho mọi cách triển khai Python.

<!-- worked-example bai-02-python-co-ban-worked-2 -->

::: example Kiểm tra kích thước bộ nhớ nông của các đối tượng với sys.getsizeof

Trong các bài toán xử lý lượng lớn quan sát, việc lựa chọn cấu trúc dữ liệu phù hợp ảnh hưởng trực tiếp đến dung lượng bộ nhớ RAM mà chương trình tiêu thụ. Mỗi đối tượng trong Python đều mang theo chi phí bộ nhớ để lưu trữ bảng thông tin kiểu và số lượng tham chiếu. Ta đo lường kích thước bộ đệm nông của các kiểu dữ liệu khác nhau bằng thư viện `sys`.

```python
import sys

cac_doi_tuong = [
    ("số nguyên 100", 100),
    ("số thực 100.5", 100.5),
    ("chuỗi 'UET'", "UET"),
    ("danh sách rỗng", []),
    ("từ điển rỗng", {}),
]

for ten, obj in cac_doi_tuong:
    kich_thuoc = sys.getsizeof(obj)
    print(f"{ten:<18}: kiểu {type(obj).__name__:<5}, chiếm {kich_thuoc} byte")
```

Kết quả khi chạy đoạn mã trên:

```text
số nguyên 100     : kiểu int  , chiếm 28 byte
số thực 100.5     : kiểu float, chiếm 24 byte
chuỗi 'UET'       : kiểu str  , chiếm 44 byte
danh sách rỗng    : kiểu list , chiếm 56 byte
từ điển rỗng      : kiểu dict , chiếm 64 byte
```

Hàm `sys.getsizeof` tiếp nhận một đối tượng Python bất kỳ và trả về số lượng byte mà đối tượng đó trực tiếp chiếm dụng trong bộ nhớ heap. Giá trị này bao gồm phần dữ liệu thực tế cùng phần tiêu đề của đối tượng trên bản dựng CPython hiện hành.

Kích thước bộ nhớ trả về phản ánh chi phí bộ nhớ nông (shallow size) trên kiến trúc máy tính và bản dựng Python cụ thể. Các con số này có thể khác biệt giữa phiên bản 32-bit và 64-bit, hoặc giữa các bản phân phối Python khác nhau, do đó không nên coi các giá trị byte này là bất biến trên mọi môi trường.

Phương thức `sys.getsizeof` chỉ đo lường vùng nhớ trực tiếp của đối tượng vỏ bọc ngoài cùng. Nếu một danh sách chứa các chuỗi hoặc từ điển con bên trong, hàm chỉ tính kích thước của các con trỏ tham chiếu chứ không tự động đệ quy để tính tổng dung lượng của toàn bộ các phần tử con.

Hiểu rõ chi phí bộ nhớ của từng đối tượng giúp giải thích vì sao khi xử lý hàng triệu bản ghi, ta cần chuyển sang các cấu trúc mảng liên tục của NumPy hoặc Series của pandas để tránh chi phí quản lý đối tượng riêng lẻ của Python.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-02-python-co-ban-worked-3 -->

::: example Phân biệt sao chép nông và sao chép sâu khi sao chép danh sách lồng nhau

Khi sao chép một bảng dữ liệu hoặc cấu trúc danh sách lồng nhau, việc chỉ sao chép nông qua phương thức `copy` có thể khiến các danh sách con bên trong vẫn bị gắn chung vùng nhớ với bản gốc. Khi một nhánh thay đổi phần tử con, nhánh còn lại cũng bị biến đổi theo ngoài ý muốn. Thư viện `copy` cung cấp hai cấp độ sao chép để lập trình viên lựa chọn chính xác theo nhu cầu.

```python
import copy

goc = [10, [20, 30]]
sao_nong = copy.copy(goc)
sao_sau = copy.deepcopy(goc)

goc[1].append(99)

print(f"Danh sách gốc: {goc}")
print(f"Bản sao nông:  {sao_nong}")
print(f"Bản sao sâu:   {sao_sau}")
print(f"Sở hữu chung phần tử con (nông): {sao_nong[1] is goc[1]}")
print(f"Sở hữu chung phần tử con (sâu):  {sao_sau[1] is goc[1]}")
```

Kết quả khi chạy đoạn mã trên:

```text
Danh sách gốc: [10, [20, 30, 99]]
Bản sao nông:  [10, [20, 30, 99]]
Bản sao sâu:   [10, [20, 30]]
Sở hữu chung phần tử con (nông): True
Sở hữu chung phần tử con (sâu):  False
```

Đoạn mã khởi tạo một danh sách `goc` chứa một số nguyên 10 và một danh sách con `[20, 30]`. Danh sách `sao_nong` được tạo thông qua hàm `copy.copy`, trong khi `sao_sau` được tạo qua hàm `copy.deepcopy`.

Hàm `copy.copy` chỉ tạo ra một đối tượng danh sách vỏ bọc mới, nhưng sao chép nguyên vẹn các tham chiếu của các phần tử bên trong. Do đó, phần tử `goc[1]` và `sao_nong[1]` cùng trỏ tới một vùng nhớ duy nhất, thể hiện qua phép so sánh danh tính `sao_nong[1] is goc[1]` cho kết quả `True`.

Khi gọi lệnh `append` trên `goc[1]`, danh sách con bị thay đổi và kéo theo sự thay đổi đồng thời trên `sao_nong`. Ngược lại, `copy.deepcopy` thực hiện duyệt đệ quy toàn bộ cấu trúc để nhân bản các đối tượng con thành các vùng nhớ biệt lập, giúp `sao_sau` giữ nguyên trạng thái `[10, [20, 30]]`.

Trong ví dụ này, `deepcopy` tạo một danh sách con mới nên việc thêm 99 vào bản gốc không đổi bản sao sâu. Với cấu trúc chỉ chứa các giá trị bất biến, một bản sao nông thường đã đủ. Các đối tượng khác có thể tự quy định cách sao chép hoặc không hỗ trợ sao chép, nên cần xét cấu trúc thực tế.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-02-python-co-ban-worked-4 -->

::: example Kiểm tra khả năng lặp và lọc dữ liệu số theo Duck Typing

Trong thực tế, một hàm phân tích thường nhận đầu vào là nhiều cấu trúc khác nhau như danh sách, bộ tuple hoặc dãy số range. Thay vì kiểm tra cứng nhắc kiểu dữ liệu cụ thể, triết lý Duck Typing khuyến khích kiểm tra hành vi có thể lặp được của đối tượng. Cách tiếp cận này giúp hàm linh hoạt và tái sử dụng được trên nhiều nguồn dữ liệu.

```python
def tinh_tong_so(tap_hop):
    try:
        bo_lap = iter(tap_hop)
    except TypeError:
        return None
    tong = 0.0
    for x in bo_lap:
        if isinstance(x, (int, float)) and not isinstance(x, bool):
            tong += x
    return tong

dau_vao = [
    ("danh sách", [10, 20.5, 30]),
    ("bộ tuple", (5, 15.0, 25)),
    ("dãy range", range(1, 4)),
    ("có chứa bool", [10, True, 20]),
    ("số đơn", 100),
]

for ten, gia_tri in dau_vao:
    kq = tinh_tong_so(gia_tri)
    print(f"{ten:<14}: tổng = {kq}")
```

Kết quả khi chạy đoạn mã trên:

```text
danh sách     : tổng = 60.5
bộ tuple      : tổng = 45.0
dãy range     : tổng = 6.0
có chứa bool  : tổng = 30.0
số đơn        : tổng = None
```

Hàm `tinh_tong_so` áp dụng kiểm tra Duck Typing bằng cách truyền tham số `tap_hop` vào hàm tích hợp `iter`. Nếu đối tượng hỗ trợ giao thức lặp, hàm `iter` sẽ trả về một bộ lặp hợp lệ để vòng lặp `for` tiến hành duyệt phần tử.

Nếu đối tượng không thể lặp, ví dụ như số nguyên 100, hàm `iter` sẽ phát sinh ngoại lệ `TypeError`. Khối `except` bắt ngoại lệ này và trả về `None` thay vì để chương trình gặp sự cố.

Trong quá trình duyệt các phần tử, điều kiện `isinstance(x, (int, float)) and not isinstance(x, bool)` sàng lọc các giá trị số học. Trong Python, kiểu `bool` là một lớp con của `int` (`issubclass(bool, int)` bằng `True`), do đó giá trị `True` sẽ bị coi là số nguyên 1 trừ khi ta loại trừ kiểu boolean một cách tường minh.

Kết quả in ra cho thấy danh sách, bộ tuple và dãy range đều được tính tổng chính xác. Riêng danh sách chứa cờ `True` chỉ cộng hai số 10 và 20 thành 30.0 nhờ loại trừ boolean, còn số đơn lẻ trả về `None` một cách an toàn.

:::

<!-- /worked-example -->

### 3.6. Phân biệt đối tượng khả biến (Mutable) và bất biến (Immutable)
Tính khả biến là ranh giới kỹ thuật quan trọng trong xử lý dữ liệu:
- **Đối tượng khả biến (*Mutable*)**: Nội dung bên trong có thể được thêm bớt, sửa đổi mà không làm thay đổi định danh `id` của đối tượng. Bao gồm: `list`, `dict`, `set`, và mảng `ndarray` của NumPy.
- **Đối tượng bất biến (*Immutable*)**: Không thể sửa trực tiếp giá trị hay thay các phần tử của chính đối tượng đó. Ví dụ gồm `int`, `float`, `bool`, `str`, `tuple`, `bytes`, `frozenset`. Một thao tác có thể trả đối tượng mới hoặc dùng lại đối tượng có sẵn, nên không suy quan hệ định danh chỉ từ tính bất biến.

Tuple không cho thay các phần tử của nó, nhưng một phần tử là list vẫn có thể đổi nội dung. Khả năng làm khóa từ điển là tính chất hashable: Mã băm phải ổn định và các đối tượng bằng nhau phải có cùng mã băm. Chẳng hạn tuple chứa list không hashable, còn một số đối tượng tùy biến khả biến vẫn dùng định danh để băm. Không nên đồng nhất hashable với bất biến hoặc an toàn khi chia sẻ giữa các luồng.

---

<!-- worked-example bai-02-python-co-ban-worked-5 -->

::: example Kiểm tra tính băm được của đối tượng để làm khóa từ điển

Từ điển và tập hợp trong Python dựa vào bảng băm để tìm kiếm phần tử với tốc độ tức thì. Một đối tượng chỉ có thể dùng làm khóa nếu nó có tính bất biến và hỗ trợ hàm băm `hash`. Ta xây dựng hàm kiểm tra an toàn tính băm được của các kiểu dữ liệu trước khi quyết định đưa chúng vào cấu trúc chỉ mục.

```python
cac_mau = [
    ("số nguyên 42", 42),
    ("chuỗi ký tự 'HN'", "HN"),
    ("bộ số thuần (1, 2)", (1, 2)),
    ("bộ chứa danh sách (1, [2, 3])", (1, [2, 3])),
    ("danh sách [1, 2]", [1, 2]),
]

for ten, gia_tri in cac_mau:
    try:
        hash(gia_tri)
        co_the_bam = True
    except TypeError:
        co_the_bam = False
    print(f"{ten:<32}: băm được = {co_the_bam}")
```

Kết quả khi chạy đoạn mã trên:

```text
số nguyên 42                    : băm được = True
chuỗi ký tự 'HN'                : băm được = True
bộ số thuần (1, 2)              : băm được = True
bộ chứa danh sách (1, [2, 3])   : băm được = False
danh sách [1, 2]                : băm được = False
```

Đối tượng băm được cần có mã băm ổn định trong suốt thời gian được dùng làm khóa. Các đối tượng so sánh bằng nhau phải có cùng mã băm. Phép gọi `hash` dưới đây kiểm tra các kiểu dựng sẵn trong ví dụ, chưa kiểm định mọi cách tự viết `__hash__` của một lớp riêng.

Đoạn mã kiểm tra tính băm được bằng cách đặt lệnh gọi `hash(gia_tri)` bên trong cấu trúc `try...except TypeError` và ghi nhận kết quả `True` hoặc `False`. Phép thử này không dựa vào việc mã băm khác không, bởi vì một giá trị hợp lệ trong Python hoàn toàn có thể có mã băm bằng không.

Các kiểu dữ liệu bất biến như `int`, `str` và bộ tuple chứa các phần tử bất biến đều cho kết quả `True`. Chúng đáp ứng đầy đủ điều kiện để sử dụng làm khóa trong từ điển hoặc phần tử trong tập hợp.

`list` không hỗ trợ băm, nên cả danh sách `[1, 2]` lẫn tuple `(1, [2, 3])` đều không dùng được làm khóa. Với tuple, điều kiện là từng phần tử cũng phải băm được. Tính băm được không đồng nhất với tính bất biến trong mọi lớp tự định nghĩa.

:::

<!-- /worked-example -->

## 4. Các kiểu dữ liệu vô hướng (Scalar Types)

### 4.1. Kiểu số học: Số nguyên, số thực và số phức
- **Số nguyên (`int`)**: Trong Python 3, số nguyên có độ chính xác tùy ý (*arbitrary precision*). Số nguyên có thể tăng kích thước không giới hạn cho tới khi cạn kiệt bộ nhớ hệ thống, loại bỏ hoàn toàn nguy cơ tràn số nguyên kinh điển thường gặp trong C/C++.
- **Số thực (`float`)**: Biểu diễn số dấu phẩy động độ chính xác kép 64-bit theo chuẩn IEEE 754. Do cách biểu diễn nhị phân, các số thập phân hữu hạn như $0{,}1$ không thể biểu diễn chính xác tuyệt đối trong bộ nhớ:
  ```python
  0.1 + 0.2 == 0.3  # Trả về False vì 0.1 + 0.2 = 0.30000000000000004
  ```
  Khi so sánh hai số thực trong tính toán, luôn sử dụng hàm so sai số nhỏ như `math.isclose(a, b)` hoặc `np.isclose(a, b)`.
- **Số phức (`complex`)**: Biểu diễn dạng phần thực và phần ảo với hậu tố `j`, ví dụ `z = 3 + 4j`.

<!-- worked-example bai-02-python-co-ban-worked-6 -->

::: example So sánh số thực với khoảng dung sai math.isclose

Do sai số làm tròn của chuẩn số dấu phẩy động IEEE 754, phép so sánh bằng trực tiếp giữa các số thực thường cho kết quả sai lệch ngoài ý muốn. Trong tính toán khoa học và kỹ thuật, việc áp dụng khoảng dung sai cho phép là phương pháp tiêu chuẩn để kiểm tra hai số thực có tương đương hay không. Hàm `math.isclose` cung cấp cơ chế so sánh với dung sai tương đối và tuyệt đối.

```python
import math

tong_tinh = 0.1 + 0.2
tong_ky_vong = 0.3

so_sanh_bang = (tong_tinh == tong_ky_vong)
so_sanh_isclose = math.isclose(tong_tinh, tong_ky_vong, rel_tol=1e-9)

print(f"Tổng thực tế 0.1 + 0.2: {tong_tinh:.17f}")
print(f"Giá trị kỳ vọng 0.3:    {tong_ky_vong:.17f}")
print(f"So sánh bằng (==):      {so_sanh_bang}")
print(f"So sánh math.isclose:   {so_sanh_isclose}")
```

Kết quả khi chạy đoạn mã trên:

```text
Tổng thực tế 0.1 + 0.2: 0.30000000000000004
Giá trị kỳ vọng 0.3:    0.29999999999999999
So sánh bằng (==):      False
So sánh math.isclose:   True
```

Đoạn mã thực hiện phép cộng hai số thực `0.1` và `0.2`, sau đó so sánh kết quả thu được với giá trị kỳ vọng `0.3`. Do số `0.1` và `0.2` không có biểu diễn hữu hạn trong hệ nhị phân, giá trị thực tế lưu trữ trong bộ nhớ xấp xỉ `0.30000000000000004`.

Phép so sánh toán tử `==` trả về kết quả `False`, phản ánh đặc tính tự nhiên của số dấu phẩy động IEEE 754. Nếu sử dụng phép so sánh bằng tuyệt đối trong các điều kiện logic, chương trình có thể phân nhánh sai lệch.

Hàm `math.isclose` giải quyết vấn đề bằng cách kiểm tra xem độ lệch giữa hai số có nằm trong ngưỡng dung sai cho phép hay không. Tham số `rel_tol` quy định dung sai tương đối dựa trên độ lớn của số, còn `abs_tol` quy định dung sai tuyệt đối cho các giá trị gần bằng không.

Người phân tích cần phân biệt rõ phạm vi áp dụng: Hàm `math.isclose` phục vụ tính toán số học và mô phỏng khoa học, chứ không thay thế cho các kiểu số nguyên đếm xu hoặc `Decimal` trong kế toán tài chính. Trong hạch toán tiền tệ, quy định nghiệp vụ đòi hỏi số tiền phải được làm tròn chính xác từng xu thay vì chấp nhận một khoảng dung sai tương đối.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-02-python-co-ban-worked-7 -->

::: example Căn chỉnh độ rộng cột và phân cách hàng nghìn bằng f-string

Khi xuất dữ liệu thống kê ra màn hình dòng lệnh hoặc tệp văn bản báo cáo, các cột số cần được căn lề thẳng hàng và phân cách hàng nghìn rõ ràng để người đọc dễ theo dõi. Chuỗi định dạng f-string cung cấp các cú pháp định dạng trực tiếp bên trong biểu thức mà không cần thư viện ngoài. Ta định dạng bảng tóm tắt gồm tên hàng hóa, số lượng và tổng doanh thu.

```python
mat_hang = [
    {"ten": "Gạo ST25", "sl": 120, "gia": 35000},
    {"ten": "Cà phê", "sl": 45, "gia": 115000},
    {"ten": "Trà xanh", "sl": 8, "gia": 450000},
]

print(f"{'Tên hàng':<12} {'Số lượng':>8} {'Đơn giá':>12} {'Thành tiền':>14}")
print("-" * 50)
for h in mat_hang:
    thanh_tien = h["sl"] * h["gia"]
    print(f"{h['ten']:<12} {h['sl']:>8d} {h['gia']:>12,d} {thanh_tien:>14,d}")
```

Kết quả khi chạy đoạn mã trên:

```text
Tên hàng     Số lượng      Đơn giá     Thành tiền
--------------------------------------------------
Gạo ST25          120       35,000      4,200,000
Cà phê             45      115,000      5,175,000
Trà xanh            8      450,000      3,600,000
```

Đoạn mã duyệt qua danh sách các mặt hàng và áp dụng các đặc tả định dạng của f-string để chuẩn hóa độ rộng của từng trường thông tin. Cú pháp bắt đầu bằng dấu hai chấm sau tên biến bên trong cặp ngoặc nhọn.

Đặc tả `:<12` căn trái trong độ rộng tối thiểu 12 ký tự, thêm khoảng trắng bên phải nếu tên ngắn hơn. Nếu tên dài hơn 12 ký tự, Python vẫn in toàn bộ tên và cột có thể rộng ra. `:>8d` căn phải số nguyên trong độ rộng tối thiểu 8 vị trí.

Đặc tả `:>14,d` là sự kết hợp giữa căn lề phải độ rộng 14 ký tự và chèn dấu phẩy phân cách hàng nghìn cho số nguyên. Nhờ đó, số tiền lớn như `4,200,000` hay `5,175,000` được xếp thẳng hàng với các chữ số hàng đơn vị.

Bảng văn bản này được đọc bằng phông đơn cách trên màn hình dòng lệnh. Độ rộng trong f-string không phải số điểm ảnh. Ký tự ghép dấu hoặc ký tự có bề rộng hiển thị khác nhau có thể cần cách căn riêng. Khi làm trang web, hãy dùng bảng HTML để hàng và cột được trình bày theo cấu trúc bảng.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-02-python-co-ban-worked-8 -->

::: example Loại bỏ tiền tố Byte Order Mark bằng chuẩn giải mã utf-8-sig

Các tệp văn bản xuất từ phần mềm trên Windows thường được tự động chèn thêm ba byte đánh dấu thứ tự byte (Byte Order Mark - BOM) ở đầu tệp. Nếu giải mã bằng chuẩn utf-8 thông thường, ký tự vô hình này sẽ bị dính vào đầu từ đầu tiên và làm sai lệch các phép so khớp khóa. Ta sử dụng chuẩn mã hóa utf-8-sig để tự động loại bỏ tiền tố này một cách an toàn.

```python
chuoi_goc = "Hà Nội"
du_lieu_bom = b"\xef\xbb\xbf" + chuoi_goc.encode("utf-8")

giai_ma_thuong = du_lieu_bom.decode("utf-8")
giai_ma_sig = du_lieu_bom.decode("utf-8-sig")

print(f"Độ dài byte có BOM:          {len(du_lieu_bom)}")
print(f"Giải mã với 'utf-8':         {giai_ma_thuong!r}")
print(f"Khớp với chuỗi gốc:          {giai_ma_thuong == chuoi_goc}")
print(f"Mã Unicode ký tự đầu:        {ord(giai_ma_thuong[0])}")
print(f"Giải mã với 'utf-8-sig':     {giai_ma_sig!r}")
print(f"Khớp hoàn toàn khi dùng sig: {giai_ma_sig == chuoi_goc}")
```

Kết quả khi chạy đoạn mã trên:

```text
Độ dài byte có BOM:          12
Giải mã với 'utf-8':         '\ufeffHà Nội'
Khớp với chuỗi gốc:          False
Mã Unicode ký tự đầu:        65279
Giải mã với 'utf-8-sig':     'Hà Nội'
Khớp hoàn toàn khi dùng sig: True
```

Đoạn mã mô phỏng tình huống nhận dữ liệu nhị phân chứa chuỗi ký tự tiếng Việt kèm theo ba byte tiền tố `\xef\xbb\xbf` đặc trưng của chuẩn UTF-8 BOM. Biến `chuoi_goc` có 6 ký tự nhưng chuỗi byte gốc chiếm 9 byte do các chữ cái có dấu chiếm nhiều byte trong bảng mã UTF-8.

Khi giải mã bằng `du_lieu_bom.decode('utf-8')`, trình thông dịch giải mã cả ba byte BOM thành ký tự mã điểm Unicode 65279 (Zero Width No-Break Space). Ký tự này không nhìn thấy được trên màn hình, khiến biểu thức so sánh `giai_ma_thuong == chuoi_goc` trả về `False`.

Ngược lại, khi giải mã bằng chuẩn `utf-8-sig`, trình giải mã nhận biết sự hiện diện của BOM ở đầu chuỗi và tự động loại bỏ nó khỏi dữ liệu. Kết quả thu được hoàn toàn trùng khớp với chuỗi gốc ban đầu.

Kết quả in ra cho thấy số hiệu mã điểm của ký tự đầu tiên trong cách giải mã thông thường là 65279 thay vì ký tự `'H'` (mã điểm 72). Việc nắm vững chuẩn `utf-8-sig` giúp xử lý các lỗi so khớp khóa khi nạp dữ liệu từ các tệp CSV xuất từ hệ điều hành Windows.

:::

<!-- /worked-example -->

### 4.4. Giá trị `None` trong câu lệnh điều kiện {#_4-4-gia-tri-none-va-bay-chan-tri}
`None` là đối tượng đơn nhất (*singleton*) thuộc kiểu `NoneType`, dùng để biểu thị sự vắng mặt của giá trị.
- Kiểm tra một biến có mang giá trị `None` hay không phải luôn dùng toán tử danh tính `is` hoặc `is not`, tuyệt đối không dùng `==`:
  ```python
  ket_qua = None
  if ket_qua is None:
      print("Dữ liệu bị thiếu!")
  ```
- Khi đặt trong câu lệnh điều kiện `if`, Python đánh giá `None`, số `0`, số `0.0`, chuỗi rỗng `""`, danh sách rỗng `[]` và từ điển rỗng `{}` là sai (`False`). Vì vậy, `if gia_tri` không phân biệt được một phép đo bằng không với một ô chưa có dữ liệu. Khi cần giữ số không, hãy kiểm tra riêng bằng `gia_tri is None`.
  Cần hết sức cẩn trọng: Số $0$ mang giá trị số học hợp lệ nhưng vẫn bị coi là `False`. Đoạn mã sau sẽ mắc lỗi nghiêm trọng khi lọc số liệu:
  ```python
  ds_gia = [0.0, 100.0, None]
  gia_hop_le = []
  for g in ds_gia:
      if g is not None:
          gia_hop_le.append(g)
  assert gia_hop_le == [0.0, 100.0]
  ```

<!-- worked-example bai-02-python-co-ban-worked-9 -->

::: example Phân biệt giá trị số không và dữ liệu khuyết thiếu None

Trong các tệp dữ liệu cảm biến hoặc giao dịch, giá trị số không (0 hoặc 0.0) đại diện cho một phép đo hợp lệ có kết quả bằng không, hoàn toàn khác với giá trị None đại diện cho việc mất tín hiệu đo. Nếu kiểm tra điều kiện lọc dữ liệu bằng câu lệnh if thô, cả 0 và None đều bị coi là sai và bị loại bỏ cùng lúc. Ta phân tách rõ hai trạng thái này bằng toán tử is not.

```python
nhiet_do_do = [25.5, 0.0, None, 18.2, None, -2.0]

hop_le = [x for x in nhiet_do_do if x is not None]
thieu = sum(1 for x in nhiet_do_do if x is None)
trung_binh = sum(hop_le) / len(hop_le)

print(f"Dữ liệu gốc:        {nhiet_do_do}")
print(f"Các giá trị hợp lệ: {hop_le}")
print(f"Số mẫu bị khuyết:   {thieu}")
print(f"Trung bình cộng:    {trung_binh:.2f}")
```

Kết quả khi chạy đoạn mã trên:

```text
Dữ liệu gốc:        [25.5, 0.0, None, 18.2, None, -2.0]
Các giá trị hợp lệ: [25.5, 0.0, 18.2, -2.0]
Số mẫu bị khuyết:   2
Trung bình cộng:    10.43
```

Danh sách `nhiet_do_do` chứa các giá trị nhiệt độ thô gồm số thực dương, số thực âm, số `0.0` và giá trị thiếu `None`. Biểu thức comprehension sử dụng phép so sánh danh tính `x is not None` để sàng lọc các giá trị đo đạc hợp lệ.

Nếu người lập trình viết câu lệnh điều kiện `if x:` thay vì so sánh danh tính tường minh, giá trị `0.0` sẽ bị đánh giá là `False` và bị loại bỏ nhầm. Hậu quả là giá trị `0.0` độ C hợp lệ bị mất khỏi mẫu, làm sai lệch giá trị trung bình chung của toàn bộ chuỗi quan sát.

Bằng cách kiểm tra tường minh với toán tử `is not None`, danh sách `hop_le` giữ lại đầy đủ 4 giá trị số thực gồm 25.5, 0.0, 18.2 và -2.0. Số lượng phần tử thiếu được ghi nhận chính xác là 2 thông qua phép đếm `x is None`.

Giá trị trung bình cộng tính trên 4 mẫu hợp lệ đạt 10.43 độ C. Đây là nguyên tắc quan trọng trong tiền xử lý: Không sử dụng kiểm tra chân trị ngầm định để lọc dữ liệu số học nhằm bảo toàn các giá trị bằng không có nghĩa. Nếu mọi phần tử đều là `None`, danh sách `hop_le` sẽ rỗng và phép chia cho `len(hop_le)` không hợp lệ. Khi dùng lại cách tính này cho dữ liệu khác, cần kiểm tra có ít nhất một giá trị trước khi tính trung bình.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-02-python-co-ban-worked-10 -->

::: example Chuyển đổi chuỗi thời gian và tính toán khoảng cách với datetime

Dữ liệu nhật ký máy chủ thường ghi lại thời điểm bắt đầu và kết thúc của các phiên xử lý dữ liệu dưới dạng chuỗi văn bản. Để đánh giá thời gian phản hồi của hệ thống, ta cần chuyển các chuỗi này thành đối tượng thời gian chuẩn, tính toán hiệu số thời gian và định dạng kết quả ra chuỗi hiển thị thân thiện. Thư viện `datetime` cung cấp đầy đủ các công cụ phục vụ quy trình này.

```python
from datetime import datetime, timedelta

nhat_ky = [
    {"id": "L01", "bat_dau": "2026-03-01 08:30:00", "giay": 125},
    {"id": "L02", "bat_dau": "2026-03-01 09:15:20", "giay": 3600},
]

for item in nhat_ky:
    t_bd = datetime.strptime(item["bat_dau"], "%Y-%m-%d %H:%M:%S")
    t_kt = t_bd + timedelta(seconds=item["giay"])
    khoang_cach_phut = (t_kt - t_bd).total_seconds() / 60
    print(f"Phiên {item['id']}: từ {t_bd.strftime('%H:%M:%S')} "
          f"đến {t_kt.strftime('%H:%M:%S')} ({khoang_cach_phut:.1f} phút)")
```

Kết quả khi chạy đoạn mã trên:

```text
Phiên L01: từ 08:30:00 đến 08:32:05 (2.1 phút)
Phiên L02: từ 09:15:20 đến 10:15:20 (60.0 phút)
```

Phương thức `datetime.strptime` phân tích chuỗi văn bản ngày tháng dựa trên chuỗi định dạng `%Y-%m-%d %H:%M:%S`. Kết quả trả về là một đối tượng `datetime` chứa thông tin chi tiết về năm, tháng, ngày, giờ, phút và giây.

Lớp `timedelta` đại diện cho một khoảng thời gian biến thiên. Bằng cách cộng đối tượng `datetime` với `timedelta(seconds=item['giay'])`, Python tự động tính toán thời điểm kết thúc `t_kt`, xử lý chính xác việc chuyển tiếp sang giờ tiếp theo.

Phương thức `strftime` chuyển đổi ngược đối tượng thời gian thành chuỗi hiển thị `%H:%M:%S`. Phép trừ giữa hai đối tượng `datetime` trả về một đối tượng `timedelta`, và phương thức `total_seconds()` cho phép đổi toàn bộ khoảng cách thời gian ra giây để tính số phút.

Kết quả in ra ghi nhận rõ ràng mốc bắt đầu, mốc kết thúc và thời lượng thực thi tính theo phút cho từng phiên ghi nhật ký. Việc chuyển chuỗi sang đối tượng `datetime` giúp ngăn ngừa các lỗi tính toán thời gian khi dữ liệu bước qua ranh giới ngày hoặc tháng.

:::

<!-- /worked-example -->

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
