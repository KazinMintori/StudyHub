---
course: xu-ly-du-lieu
lecture: phu-luc-b-ipython
section: lecture
title: "Phụ lục B: Làm việc hiệu quả với IPython"
prerequisites: ["ham-lap-trinh"]
lessonStatus: ready
hasChapterExercises: true
description: "Lệnh ma thuật, lịch sử In/Out, tương tác hệ vỏ, gỡ lỗi pdb, đo hiệu năng time/prun, tự động nạp lại autoreload và cấu hình hệ thống IPython."
---


<div class="lecture-notes-content">

## 1. Phím tắt dòng lệnh tương tác trong IPython

Sau khi một hàm xử lý dữ liệu báo lỗi, bạn muốn xem biến ở bước sai và thử lại một phần của chương trình. IPython hỗ trợ gỡ lỗi sau ngoại lệ, xem lịch sử, chạy tệp và đo thời gian ngay trong phiên tương tác. Các công cụ này giúp thử một giả thuyết cụ thể về lỗi hoặc hiệu năng mà không phải viết lại chương trình kiểm tra từ đầu.

Phím tắt phụ thuộc terminal, chế độ sửa dòng và cấu hình. IPython hiện dùng `prompt_toolkit` với nhiều tổ hợp kiểu Readline. Các tổ hợp dưới đây là điểm bắt đầu để tra cứu, không phải hành vi cố định trên mọi môi trường.

### 1.1. Điều hướng con trỏ
- `Ctrl + A`: Di chuyển con trỏ về ngay đầu dòng lệnh.
- `Ctrl + E`: Di chuyển con trỏ tới cuối dòng lệnh.
- `Ctrl + B`: Di chuyển con trỏ lùi lại một ký tự (tương đương phím mũi tên trái).
- `Ctrl + F`: Di chuyển con trỏ tiến lên một ký tự (tương đương phím mũi tên phải).

### 1.2. Xóa và chỉnh sửa văn bản
- `Ctrl + K`: Xóa toàn bộ văn bản từ vị trí con trỏ hiện tại tới cuối dòng.
- `Ctrl + U`: Xóa toàn bộ văn bản từ đầu dòng tới vị trí con trỏ hiện tại.
- `Ctrl + W`: Xóa một từ nằm ngay trước con trỏ.
- `Ctrl + Y`: Dán lại (*yank*) đoạn văn bản vừa bị xóa bằng các lệnh trên.

### 1.3. Điều khiển và tìm kiếm lịch sử
- `Ctrl + R`: Kích hoạt chế độ tìm kiếm tăng dần trong lịch sử lệnh. Nhập từ khóa để tự động khớp lại các câu lệnh phức tạp đã từng thực thi trước đó.
- `Ctrl + L`: Xóa sạch màn hình dòng lệnh và vẽ lại dấu nhắc hiện tại ở dòng đầu tiên.
- `Ctrl + C`: Ngắt tiến trình Python đang chạy, gửi tín hiệu ngắt `KeyboardInterrupt`.

---

## 2. Hệ thống lệnh ma thuật

Lệnh ma thuật là các lệnh đặc biệt bắt đầu bằng ký tự phần trăm `%`, cung cấp các tiện ích điều khiển hệ thống mà cú pháp Python tiêu chuẩn không hỗ trợ. IPython phân biệt hai loại lệnh ma thuật:
- **Ma thuật dòng (*Line Magics*)**: Bắt đầu bằng một ký tự `%`, chỉ nhận đối số nằm trên cùng một dòng lệnh.
- **Ma thuật ô (*Cell Magics*)**: Bắt đầu bằng hai ký tự `%%`, áp dụng lên toàn bộ khối mã của một ô trong Jupyter Notebook.

### 2.1. Lệnh %run thực thi tệp kịch bản
Lệnh `%run <ten_tep.py>` thực thi trực tiếp tệp mã nguồn Python bên trong phiên làm việc của IPython:
```ipython
%run thong_ke_doanh_thu.py
```
Khác với việc chạy `python thong_ke_doanh_thu.py` từ terminal ngoài, lệnh `%run` bảo lưu toàn bộ các biến, hàm và đối tượng vừa được định nghĩa trong tệp vào không gian tên hiện tại của IPython. Nhờ đó, sau khi chạy kịch bản, bạn có thể kiểm tra ngay giá trị của các biến trong RAM hoặc gọi tiếp các hàm mà không cần nạp lại dữ liệu.

<!-- worked-example phu-luc-b-ipython-worked-1 -->

::: example Thực thi tệp kịch bản và lưu giữ biến trong không gian tên với %run

Ví dụ sau mô phỏng một phiên IPython riêng để có thể chạy lại bằng Python. Khi đang dùng IPython hoặc Jupyter, bạn có thể thực hiện các lệnh tương ứng trực tiếp trong ô mã. Phiên mô phỏng lưu lịch sử trong bộ nhớ và không đọc lịch sử làm việc của bạn.

```python
import io
import os
import tempfile
from contextlib import redirect_stdout
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

# Khởi tạo phiên làm việc IPython độc lập
from traitlets.config import Config
config = Config()
config.HistoryManager.hist_file = ":memory:"
shell = InteractiveShell(config=config, user_ns={})

# Tạo tệp kịch bản tạm tính toán giá trị đơn hàng
with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
    f.write("gia_tri = [120, 250, 310]\ntong_cong = sum(gia_tri)\n")
    tep_tam = f.name

try:
    # Thực thi tệp kịch bản bằng lệnh ma thuật run
    with redirect_stdout(io.StringIO()):
        shell.run_line_magic("run", tep_tam)
    bang_kq = pd.DataFrame([{
        "bien": "tong_cong",
        "gia_tri": shell.user_ns["tong_cong"],
        "so_phan_tu": len(shell.user_ns["gia_tri"]),
    }])
    print(bang_kq)
finally:
    if os.path.exists(tep_tam):
        os.remove(tep_tam)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| bien | gia&#95;tri | so&#95;phan&#95;tu |
| --- | --- | --- |
| tong&#95;cong | 680 | 3 |

</div>

Trong IPython, `%run ten_tep.py` chạy tệp như một chương trình rồi đưa các biến đã tạo về phiên tương tác. Ví dụ tạo một tệp tạm chứa danh sách `[120, 250, 310]` và phép tính tổng. `run_line_magic("run", tep_tam)` là cách gọi cùng lệnh đó từ chương trình Python.

Mặc định `%run` thực thi tệp trong một không gian tên riêng trước khi cập nhật các tên vào phiên IPython. Nó không mặc nhiên đọc mọi biến bạn đang có trong phiên. Nếu cần dùng không gian tên hiện tại để chạy tệp, `%run -i` là một lựa chọn khác. Những tên trùng được đưa về sau khi chạy có thể thay giá trị trong phiên.

Sau khi chạy, `shell.user_ns` có `gia_tri` gồm 3 phần tử và `tong_cong` bằng 680. Đây là trạng thái của phiên mô phỏng. Tệp tạm được đóng trước khi chạy và được xóa ở cuối, còn notebook thực tế cần giữ các tệp nguồn mà phân tích phụ thuộc.

:::

<!-- /worked-example -->

### 2.2. Dán mã nguồn với %paste và %cpaste
Khi sao chép mã nguồn từ các trang web hoặc tài liệu có nhiều cấp thụt lề phức tạp, việc dán trực tiếp vào terminal thông thường có thể khiến trình thông dịch hiểu nhầm dấu cách và báo lỗi cú pháp.
- `%paste`: Tự động lấy văn bản từ clipboard của hệ điều hành, chuẩn hóa lại thụt lề và thực thi an toàn.
- `%cpaste`: Mở ra một vùng nhập liệu đặc biệt, cho phép dán nhiều đoạn mã liên tiếp, kiểm tra kỹ lưỡng trước khi gõ `--` để thực thi.

### 2.3. Tra cứu nhanh với %magic và %quickref
- `%magic`: Hiển thị toàn bộ tài liệu hướng dẫn chi tiết về mọi lệnh ma thuật có sẵn trong IPython.
- `%quickref`: Bảng tra cứu tóm tắt các cú pháp dòng lệnh, phím tắt và tiện ích thường dùng nhất.

---

<!-- worked-example phu-luc-b-ipython-worked-2 -->

::: example Kiểm tra các lệnh ma thuật đã có trong phiên

Ví dụ sau mô phỏng một phiên IPython riêng để có thể chạy lại bằng Python. Khi đang dùng IPython hoặc Jupyter, bạn có thể thực hiện các lệnh tương ứng trực tiếp trong ô mã. Phiên mô phỏng lưu lịch sử trong bộ nhớ và không đọc lịch sử làm việc của bạn.

```python
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

from traitlets.config import Config
config = Config()
config.HistoryManager.hist_file = ":memory:"
shell = InteractiveShell(config=config, user_ns={})
line_magics = shell.magics_manager.magics["line"]

# Kiểm tra các lệnh ma thuật thường dùng trong phân tích dữ liệu
cac_lenh = ["run", "timeit", "prun", "pwd", "cd"]
bang_kq = pd.DataFrame([{
    "lenh": f"%{m}",
    "loai": "line",
    "san_sang": m in line_magics,
} for m in cac_lenh])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| lenh | loai | san&#95;sang |
| --- | --- | --- |
| %run | line | `True` |
| %timeit | line | `True` |
| %prun | line | `True` |
| %pwd | line | `True` |
| %cd | line | `True` |

</div>

IPython có lệnh dòng bắt đầu bằng `%` và lệnh ô bắt đầu bằng `%%`. Ví dụ, `%timeit` đo một biểu thức, còn `%%timeit` đo phần thân của cả ô. Đây là cú pháp IPython, không phải câu lệnh Python thông thường trong tệp `.py`.

Ví dụ đọc danh mục lệnh dòng mà phiên mô phỏng đã đăng ký. Các lệnh `run`, `timeit`, `prun`, `pwd` và `cd` đều được tìm theo tên không có dấu `%`. Cột `san_sang` cho biết tên có nằm trong danh mục, không thực thi những lệnh này.

Khi dùng trực tiếp, `%lsmagic` liệt kê lệnh đang có, còn `%quickref` mở bảng tra cứu ngắn. Có thể gõ `%timeit?` để xem trợ giúp của riêng lệnh đó. Những phần mở rộng như `line_profiler` chỉ cung cấp thêm lệnh sau khi đã được cài và nạp.

:::

<!-- /worked-example -->

## 3. Quản lý lịch sử lệnh và biến đầu vào đầu ra

IPython duy trì một cơ chế ghi nhận nhật ký toàn diện cho toàn bộ các biểu thức được thực thi trong một phiên làm việc.

### 3.1. Các biến đặc biệt _ và __
- Ký tự gạch dưới đơn `_`: Lưu trữ giá trị của kết quả đầu ra gần đây nhất.
- Ký tự gạch dưới kép `__`: Lưu trữ giá trị của kết quả đầu ra trước đó hai bước.
```text
In [1]: 150000 * 4
Out[1]: 600000

In [2]: _ + 50000
Out[2]: 650000
```

<!-- worked-example phu-luc-b-ipython-worked-3 -->

::: example Tái sử dụng kết quả tính toán gần nhất với biến gạch dưới _ và __

Ví dụ sau mô phỏng một phiên IPython riêng để có thể chạy lại bằng Python. Khi đang dùng IPython hoặc Jupyter, bạn có thể thực hiện các lệnh tương ứng trực tiếp trong ô mã. Phiên mô phỏng lưu lịch sử trong bộ nhớ và không đọc lịch sử làm việc của bạn.

```python
import io
from contextlib import redirect_stdout
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

from traitlets.config import Config
config = Config()
config.HistoryManager.hist_file = ":memory:"
shell = InteractiveShell(config=config, user_ns={})

# Thực thi hai biểu thức tính toán liên tiếp
with redirect_stdout(io.StringIO()):
    shell.run_cell("150000 * 4", store_history=True)
    shell.run_cell("_ + 50000", store_history=True)

bang_kq = pd.DataFrame([{
    "buoc": "Ket_qua_vua_tinh (_)",
    "gia_tri": shell.user_ns["_"],
}, {
    "buoc": "Ket_qua_truoc_do (__)",
    "gia_tri": shell.user_ns["__"],
}])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| buoc | gia&#95;tri |
| --- | --- |
| Ket&#95;qua&#95;vua&#95;tinh (&#95;) | 650000 |
| Ket&#95;qua&#95;truoc&#95;do (&#95;&#95;) | 600000 |

</div>

Trong phiên tương tác, biểu thức `150000 * 4` hiển thị 600000. Biến `_` giữ kết quả được hiển thị gần nhất, nên `_ + 50000` cho 650000 ở lượt sau. Khi đó, `_` là 650000 và `__` là 600000.

Lịch sử đầu ra chỉ đổi khi một biểu thức thật sự được hiển thị. Lệnh gán như `x = 10` và lời gọi `print(x)` không tạo đầu ra đối tượng mới để thay `_` theo cách này. Dấu chấm phẩy cuối biểu thức cũng có thể tắt việc hiển thị và lưu kết quả.

Cách gọi `run_cell` trong ví dụ tạo đúng hai lượt tương tác trong một phiên mới. Khi viết một quy trình cần chạy lại ổn định, nên gán tên rõ ràng cho các kết quả quan trọng. `_` và `__` phụ thuộc các lượt vừa chạy nên phù hợp hơn cho bước kiểm tra nhanh.

:::

<!-- /worked-example -->

### 3.2. Danh sách In và từ điển Out
Mỗi lượt tương tác được đánh số thứ tự $n$:
- `_i<n>` hoặc `In[n]`: Lưu chuỗi mã nguồn đầu vào của lượt thực thi thứ $n$.
- `_o<n>` hoặc `Out[n]`: Lưu trữ đối tượng kết quả trả về của biểu thức ở lượt thực thi thứ $n$.

Lưu ý: Chỉ những biểu thức có sinh ra giá trị đầu ra (như phép tính, lời gọi hàm trả về dữ liệu) mới được lưu vào `Out`. Các câu lệnh không trả về giá trị (như `x = 10` hoặc lệnh `print()`) sẽ không có mục tương ứng trong `Out`.

<!-- worked-example phu-luc-b-ipython-worked-4 -->

::: example Truy xuất lịch sử câu lệnh và kết quả đầu ra qua In và Out

Ví dụ sau mô phỏng một phiên IPython riêng để có thể chạy lại bằng Python. Khi đang dùng IPython hoặc Jupyter, bạn có thể thực hiện các lệnh tương ứng trực tiếp trong ô mã. Phiên mô phỏng lưu lịch sử trong bộ nhớ và không đọc lịch sử làm việc của bạn.

```python
import io
from contextlib import redirect_stdout
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

from traitlets.config import Config
config = Config()
config.HistoryManager.hist_file = ":memory:"
shell = InteractiveShell(config=config, user_ns={})

# Lượt 1: Câu lệnh gán biến (không tạo mục trong Out)
# Lượt 2: Biểu thức có giá trị trả về
with redirect_stdout(io.StringIO()):
    shell.run_cell("x = 25", store_history=True)
    shell.run_cell("x * 4", store_history=True)

in_list = shell.user_ns["In"]
out_dict = shell.user_ns["Out"]

bang_kq = pd.DataFrame([
    {"luot": 1, "ma_lenh": in_list[1], "co_out": 1 in out_dict, "gia_tri": out_dict.get(1, "Khong_co")},
    {"luot": 2, "ma_lenh": in_list[2], "co_out": 2 in out_dict, "gia_tri": str(out_dict.get(2, "Khong_co"))},
])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| luot | ma&#95;lenh | co&#95;out | gia&#95;tri |
| --- | --- | --- | --- |
| 1 | x = 25 | `False` | Khong&#95;co |
| 2 | x &#42; 4 | `True` | 100 |

</div>

Danh sách `In` lưu chuỗi mã đã chạy theo số lượt, còn từ điển `Out` lưu những kết quả đã hiển thị. Trong ví dụ, lượt 1 chạy `x = 25`, lượt 2 chạy `x * 4`. Cả hai có trong `In`, nhưng chỉ lượt 2 cho mục đầu ra 100.

`Out[2]` lấy lại đối tượng kết quả của lượt 2 mà không tính lại biểu thức. Nó giữ tham chiếu tới đối tượng, không phải bản sao lịch sử bất biến. Nếu kết quả là một danh sách rồi bạn sửa danh sách đó, nội dung nhìn qua `Out` có thể đổi theo.

Giữ tham chiếu trong `Out` cũng có thể giữ một mảng lớn trong bộ nhớ. Xóa biến đã đặt tên chưa chắc giải phóng mảng nếu còn tham chiếu trong lịch sử đầu ra. Khi cần dọn bộ nhớ, nên xét cả biến đang dùng và các mục lịch sử liên quan.

:::

<!-- /worked-example -->

### 3.3. Xem lịch sử với %history
Lệnh `%history` cho phép xem lại các câu lệnh đã chạy:
```ipython
%history -n 1-5  # In lại các câu lệnh từ lượt 1 đến lượt 5 kèm số thứ tự
```

---

<!-- worked-example phu-luc-b-ipython-worked-5 -->

::: example Trích xuất và kiểm tra chuỗi câu lệnh đã thực thi với danh sách lịch sử

Ví dụ sau mô phỏng một phiên IPython riêng để có thể chạy lại bằng Python. Khi đang dùng IPython hoặc Jupyter, bạn có thể thực hiện các lệnh tương ứng trực tiếp trong ô mã. Phiên mô phỏng lưu lịch sử trong bộ nhớ và không đọc lịch sử làm việc của bạn.

```python
import io
from contextlib import redirect_stdout
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

from traitlets.config import Config
config = Config()
config.HistoryManager.hist_file = ":memory:"
shell = InteractiveShell(config=config, user_ns={})

# Thực thi chuỗi 3 câu lệnh tính toán mẫu
with redirect_stdout(io.StringIO()):
    shell.run_cell("a = 10", store_history=True)
    shell.run_cell("b = 20", store_history=True)
    shell.run_cell("c = a + b", store_history=True)

bang_kq = pd.DataFrame([{
    "so_thu_tu": i,
    "cau_lenh": shell.user_ns["In"][i],
} for i in range(1, 4)])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| so&#95;thu&#95;tu | cau&#95;lenh |
| --- | --- |
| 1 | a = 10 |
| 2 | b = 20 |
| 3 | c = a + b |

</div>

Ba lượt trong ví dụ lần lượt gán `a`, gán `b` và tính `c = a + b`. Đọc các mục 1 đến 3 trong `In` cho đúng thứ tự thực thi, khác với thứ tự các ô có thể đã được kéo lại trên màn hình notebook.

Trong phiên thật, `%history -n 1-3` hiển thị cùng dải lượt kèm số thứ tự. Tùy chọn `-f ten_tep.py` ghi lịch sử được chọn vào tệp. Trước khi chạy lại tệp đó, cần đọc và bỏ các lệnh thử chưa đúng hoặc những lệnh phụ thuộc trạng thái cũ.

Lịch sử ghi mọi lệnh đã thực hiện trong phạm vi được lưu, không tự chọn ra một quy trình đúng. Muốn tạo mã chạy lại được, cần giữ các bước chuẩn bị dữ liệu, khai báo biến và kiểm tra kết quả. Sau đó thử từ một phiên mới thay vì dựa vào việc biến còn tồn tại.

:::

<!-- /worked-example -->

## 4. Tương tác trực tiếp với hệ điều hành

IPython cho phép điều phối các công cụ của hệ điều hành ngay trong luồng làm việc phân tích dữ liệu mà không cần chuyển đổi cửa sổ terminal.

### 4.1. Thực thi lệnh hệ vỏ với tiền tố !
Đặt dấu chấm than `!` ở đầu dòng để gọi bất kỳ tiện ích hệ vỏ nào:
```ipython
# Xem danh sách tệp tin trong thư mục
!dir  # Trên Windows
!ls -la  # Trên Linux/macOS

# Kiểm tra trạng thái Git
!git status
```

IPython cho phép **bắt đầu ra của lệnh hệ vỏ vào một biến Python**:
```ipython
danh_sach_tep = !dir /b
print(f"Số lượng tệp: {len(danh_sach_tep)}")
```
Biến `danh_sach_tep` là một đối tượng danh sách đặc biệt của IPython, cho phép bạn lặp và lọc các tệp bằng cú pháp Python.

### 4.2. Điều hướng thư mục với %pwd, %cd và %dhist
- `%pwd`: In ra đường dẫn của thư mục làm việc hiện hành (*print working directory*).
- `%cd <duong_dan>`: Chuyển đổi thư mục làm việc hiện tại.
- `%dhist`: In ra toàn bộ lịch sử các thư mục mà phiên làm việc đã từng điều hướng qua.

<!-- worked-example phu-luc-b-ipython-worked-6 -->

::: example Quản lý thư mục làm việc và theo dõi lịch sử điều hướng với %pwd và %dhist

Ví dụ sau mô phỏng một phiên IPython riêng để có thể chạy lại bằng Python. Khi đang dùng IPython hoặc Jupyter, bạn có thể thực hiện các lệnh tương ứng trực tiếp trong ô mã. Phiên mô phỏng lưu lịch sử trong bộ nhớ và không đọc lịch sử làm việc của bạn.

```python
import io
import os
import tempfile
from contextlib import redirect_stdout
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

from traitlets.config import Config
config = Config()
config.HistoryManager.hist_file = ":memory:"
shell = InteractiveShell(config=config, user_ns={})

# Tạo một thư mục tạm có tên xác định
tam = tempfile.TemporaryDirectory(prefix="studyhub-")
thu_muc_tam = tam.name

with redirect_stdout(io.StringIO()):
    pwd_goc = shell.run_line_magic("pwd", "")

try:
    # Chuyển tới thư mục tạm rồi quay về thư mục gốc
    with redirect_stdout(io.StringIO()):
        shell.run_line_magic("cd", thu_muc_tam)
        shell.run_line_magic("cd", pwd_goc)
    lich_su = list(shell.user_ns["_dh"])
    bang_kq = pd.DataFrame([{
        "buoc": idx + 1,
        "thu_muc": "Thư mục tạm" if duong_dan == thu_muc_tam else "Thư mục ban đầu",
    } for idx, duong_dan in enumerate(lich_su[-2:])])
    print(bang_kq)
finally:
    with redirect_stdout(io.StringIO()):
        shell.run_line_magic("cd", pwd_goc)
    tam.cleanup()
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| buoc | thu&#95;muc |
| --- | --- |
| 1 | Thư mục ban đầu |
| 2 | Thư mục ban đầu |

</div>

`%pwd` trả thư mục làm việc hiện tại. Đường dẫn tương đối trong lệnh đọc tệp được tính từ thư mục này, nên `data.csv` có thể chỉ tới một tệp khác nếu trước đó bạn đã đổi thư mục bằng `%cd`.

Phiên mô phỏng tạo một thư mục tạm riêng, chuyển vào đó rồi quay về vị trí ban đầu. `_dh` là lịch sử các thư mục đã chuyển qua. Trong IPython, `%dhist` hiển thị lịch sử này mà không cần truy cập biến nội bộ.

Bảng chỉ dùng hai nhãn “Thư mục tạm” và “Thư mục ban đầu” để không phụ thuộc tên thư mục trên từng máy. Khối `finally` quay lại vị trí cũ trước khi dọn thư mục tạm. Khi làm notebook thật, cần xác nhận thư mục hiện tại trước các thao tác đọc và ghi.

:::

<!-- /worked-example -->

### 4.3. Hệ thống đánh dấu thư mục với %bookmark
Khi thường xuyên phải làm việc với các đường dẫn thư mục sâu trong ổ đĩa, bạn có thể tạo các điểm đánh dấu ghi nhớ:
```ipython
# Tạo điểm đánh dấu mang tên 'duan'
%bookmark duan C:\Users\Ai\Projects\DataProcessing

# Chuyển nhanh tới thư mục đã đánh dấu từ bất kỳ đâu
%cd duan
```

---

## 5. Công cụ gỡ lỗi và đo lường hiệu năng

### 5.1. Trình gỡ lỗi tương tác sau sự cố
Khi một câu lệnh hoặc kịch bản chạy bị sập do phát sinh ngoại lệ đột ngột, việc gõ lệnh `%debug` ngay sau đó sẽ kích hoạt trình gỡ lỗi tương tác:
```ipython
%debug
```
IPython sẽ tự động đưa con trỏ gỡ lỗi tới đúng dòng mã phát sinh ngoại lệ, hiển thị khung ngăn xếp (*stack frame*) và mở dấu nhắc `ipdb>`.

Các lệnh điều khiển cơ bản trong `ipdb`:
- `p <ten_bien>`: In giá trị hiện tại của biến tại thời điểm gặp lỗi.
- `u` (*up*): Di chuyển lên một cấp khung ngăn xếp gọi hàm bên ngoài.
- `d` (*down*): Di chuyển xuống một cấp khung ngăn xếp bên trong.
- `n` (*next*): Thực thi dòng lệnh kế tiếp.
- `s` (*step*): Nhảy vào bên trong hàm đang được gọi.
- `c` (*continue*): Tiếp tục thực thi chương trình cho tới điểm dừng tiếp theo.
- `q` (*quit*): Thoát khỏi trình gỡ lỗi.

Ngoài ra, bạn có thể đặt điểm dừng chủ động trong mã nguồn bằng hàm tích hợp sẵn của Python: `breakpoint()`.

### 5.2. Đo lường thời gian thực thi với %time và %timeit
- **`%time`**: Đo thời gian thực thi một lần duy nhất của câu lệnh. Báo cáo cung cấp hai thông số:
  - `CPU times`: Thời gian vi xử lý thực sự dành để tính toán mã lệnh.
  - `Wall time`: Thời gian thực tế trôi qua theo đồng hồ treo tường (bao gồm cả thời gian chờ đọc đĩa, mạng và chuyển ngữ cảnh của hệ điều hành).
- **`%timeit`**: Công cụ đo lường hiệu năng chuyên nghiệp. `%timeit` tự động thực thi câu lệnh lặp đi lặp lại hàng trăm đến hàng triệu lần, tính toán thời gian trung bình và độ lệch chuẩn của phép đo. Nó tự động vô hiệu hóa cơ chế dọn rác tạm thời để hạn chế tối đa nhiễu đo lường:
```ipython
%timeit [x**2 for x in range(1000)]
# 52.3 µs ± 1.1 µs per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
```

<!-- worked-example phu-luc-b-ipython-worked-7 -->

::: example Đo lường thời gian thực thi thuật toán với lệnh ma thuật %timeit

Ví dụ sau mô phỏng một phiên IPython riêng để có thể chạy lại bằng Python. Khi đang dùng IPython hoặc Jupyter, bạn có thể thực hiện các lệnh tương ứng trực tiếp trong ô mã. Phiên mô phỏng lưu lịch sử trong bộ nhớ và không đọc lịch sử làm việc của bạn.

```python
import io
from contextlib import redirect_stdout
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

from traitlets.config import Config
config = Config()
config.HistoryManager.hist_file = ":memory:"
shell = InteractiveShell(config=config, user_ns={})

# Thực hiện đo lường với số vòng lặp và số lần lặp lại được kiểm soát
with redirect_stdout(io.StringIO()):
    kq_do = shell.run_line_magic("timeit", "-n 50 -r 3 -o sum(range(1000))")

bang_kq = pd.DataFrame([{
    "phep_tinh": "sum(range(1000))",
    "so_vong_lap": kq_do.loops,
    "so_lan_lap_lai": kq_do.repeat,
    "da_hoan_thanh": len(kq_do.all_runs) == 3,
}])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| phep&#95;tinh | so&#95;vong&#95;lap | so&#95;lan&#95;lap&#95;lai | da&#95;hoan&#95;thanh |
| --- | --- | --- | --- |
| sum(range(1000)) | 50 | 3 | `True` |

</div>

Trong IPython, `%timeit -n 50 -r 3 -o sum(range(1000))` thực hiện ba lượt đo, mỗi lượt lặp biểu thức 50 lần. `-o` trả đối tượng kết quả thay vì chỉ hiển thị một dòng báo thời gian.

`loops` xác nhận số lần lặp trong mỗi lượt, còn `repeat` và `all_runs` cho biết số lượt đo. Bảng chỉ hiển thị các tham số này vì thời gian cụ thể thay đổi theo máy và tác vụ đang chạy. Lặp nhiều lần giúp quan sát độ biến thiên, không loại bỏ mọi ảnh hưởng của môi trường.

Khi so hai cách xử lý, cần dùng cùng đầu vào và xác định có tính cả chi phí chuẩn bị dữ liệu hay không. Một phép đo tại một kích thước không chứng minh độ phức tạp tính toán tổng quát. Đặc biệt, biểu thức có tác dụng phụ sẽ được chạy nhiều lần, nên cần chuẩn bị lại trạng thái nếu phép tính thay đổi dữ liệu.

:::

<!-- /worked-example -->

### 5.3. Đo đạc hiệu năng hàm với %prun
Khi một chương trình chạy chậm, việc đoán mò nguyên nhân thường dẫn đến tối ưu hóa sai chỗ. Lệnh ma thuật `%prun` sử dụng mô-đun `cProfile` để đo đạc chính xác thời gian tiêu tốn trong từng hàm:
```ipython
%prun ham_xu_ly_du_lieu(bang)
```
Bảng kết quả thống kê các cột:
- `ncalls`: Số lần hàm được gọi.
- `tottime`: Tổng thời gian thực thi bên trong bản thân hàm đó (không tính thời gian gọi các hàm con).
- `percall`: Thời gian trung bình cho mỗi lần gọi hàm (`tottime / ncalls`).
- `cumtime`: Thời gian tích lũy tiêu tốn trong hàm đó và toàn bộ các hàm con mà nó gọi.

<!-- worked-example phu-luc-b-ipython-worked-8 -->

::: example Đo đạc số lần gọi hàm và cấu trúc thực thi bằng lệnh ma thuật %prun

Ví dụ sau mô phỏng một phiên IPython riêng để có thể chạy lại bằng Python. Khi đang dùng IPython hoặc Jupyter, bạn có thể thực hiện các lệnh tương ứng trực tiếp trong ô mã. Phiên mô phỏng lưu lịch sử trong bộ nhớ và không đọc lịch sử làm việc của bạn.

```python
import io
from contextlib import redirect_stdout
import pandas as pd
from IPython.core.interactiveshell import InteractiveShell

from traitlets.config import Config
config = Config()
config.HistoryManager.hist_file = ":memory:"
shell = InteractiveShell(config=config, user_ns={})

# Định nghĩa hàm tính toán có quan hệ gọi hàm con
def ham_con(n):
    return sum(i for i in range(n))

def ham_chinh():
    return [ham_con(100) for _ in range(50)]

shell.user_ns["ham_chinh"] = ham_chinh

with redirect_stdout(io.StringIO()):
    stats = shell.run_line_magic("prun", "-r -q ham_chinh()")

k_chinh = [k for k in stats.stats if k[2] == "ham_chinh"][0]
k_con = [k for k in stats.stats if k[2] == "ham_con"][0]

bang_kq = pd.DataFrame([
    {"ham": "ham_chinh", "so_lan_goi": stats.stats[k_chinh][1]},
    {"ham": "ham_con", "so_lan_goi": stats.stats[k_con][1]},
])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| ham | so&#95;lan&#95;goi |
| --- | --- |
| ham&#95;chinh | 1 |
| ham&#95;con | 50 |

</div>

`%prun` dùng bộ đo cProfile để ghi số lần gọi và thời gian của từng hàm. Trong ví dụ, `ham_chinh` gọi `ham_con(100)` 50 lần. Cờ `-r` trả đối tượng thống kê, còn `-q` không in bảng báo cáo mặc định.

Khóa trong `stats.stats` có tên tệp, dòng và tên hàm. Ví dụ tìm hai hàm mình vừa định nghĩa rồi đọc số lần gọi từ thống kê. Kết quả là `ham_chinh` được gọi 1 lần và `ham_con` được gọi 50 lần.

Số lần gọi giúp nhận ra một thao tác đang bị lặp, nhưng chưa cho biết đó có phải điểm tốn thời gian nhất hay không. Muốn chọn phần cần cải tiến, cần xem thêm thời gian riêng của hàm và thời gian tính cả các hàm con. Bản thân việc đo cũng tạo chi phí, nên cần đánh giá lại sau khi sửa.

:::

<!-- /worked-example -->

### 5.4. Đo đạc hiệu năng từng dòng lệnh với %lprun
Để biết chính xác dòng lệnh nào trong một hàm chiếm nhiều thời gian nhất, ta sử dụng thư viện `line_profiler` qua lệnh ma thuật `%lprun`:
```ipython
# Nạp tiện ích mở rộng line_profiler
%load_ext line_profiler

# Đo đạc chi tiết từng dòng của hàm xu_ly
%lprun -f xu_ly xu_ly(du_lieu)
```
Bảng báo cáo sẽ in ra tỷ lệ phần trăm thời gian `% Time` trên từng dòng mã, giúp người kỹ sư phát hiện ngay các phép toán tạo bản sao ngầm hoặc các vòng lặp thừa thãi.

---

## 6. Bí quyết lập trình hiệu quả với IPython

### 6.1. Tự động nạp lại mô-đun phụ thuộc với %autoreload
Một vấn đề nan giải khi phát triển mã nguồn: Bạn vừa viết sổ tay vừa chỉnh sửa các hàm trong tệp thư viện `.py` bên cạnh. Khi bạn sửa tệp `.py` và gõ lại `import my_module`, Python sẽ bỏ qua vì mô-đun đã nằm trong bộ nhớ đệm `sys.modules`.

Tiện ích mở rộng `autoreload` giải quyết triệt để vấn đề này:
```ipython
%load_ext autoreload
%autoreload 2
```
Với thiết lập `%autoreload 2`, mỗi khi bạn thực thi một câu lệnh mới trong IPython, hệ thống sẽ tự động quét và nạp lại toàn bộ các mô-đun `.py` đã bị sửa đổi trên đĩa trước khi chạy lệnh. Bạn không bao giờ phải khởi động lại kernel chỉ để cập nhật một dòng sửa đổi trong thư viện.

### 6.2. Nguyên tắc thiết kế mã nguồn tương tác
1. **Duy trì các đối tượng dữ liệu lớn thường trực trong RAM**: Khi làm việc với tập dữ liệu hàng triệu bản ghi, việc đọc tệp từ đĩa có thể mất vài phút. Hãy thiết kế quy trình nạp dữ liệu ở một ô riêng biệt. Toàn bộ các phép thử nghiệm thuật toán và vẽ biểu đồ được thực hiện trên các ô bên dưới, tái sử dụng trực tiếp đối tượng bảng trong RAM.
2. **Ưu tiên cấu trúc hàm phẳng (*Flat is better than nested*)**: Tránh lồng các hàm quá sâu bên trong nhau. Tách các bước biến đổi thành các hàm độc lập cấp mô-đun giúp bạn dễ dàng gọi trực tiếp từng hàm con từ cửa sổ IPython để truyền dữ liệu mẫu và kiểm tra biên.
3. **Không e ngại các tệp mã nguồn dài hơn**: Trong giai đoạn phát triển, gom nhóm các hàm liên quan chặt chẽ vào cùng một tệp giúp tìm kiếm và quản lý phụ thuộc trực quan hơn. Việc chia nhỏ thành quá nhiều tệp ngắn thường làm tăng độ phức tạp khi điều hướng mã nguồn.

---

## 7. Cấu hình nâng cao và hồ sơ IPython

Mọi hành vi mặc định của IPython có thể được tùy biến thông qua hệ thống hồ sơ cấu hình:

### 7.1. Khởi tạo hồ sơ mặc định
Chạy lệnh từ terminal để sinh tệp cấu hình chuẩn:
```bash
ipython profile create
```
Lệnh này tạo ra thư mục cấu hình tại `~/.ipython/profile_default/`, chứa tệp cấu hình chính `ipython_config.py`.

### 7.2. Tự động thực thi kịch bản khi khởi động
Thư mục `~/.ipython/profile_default/startup/` chứa các kịch bản Python sẽ được tự động thực thi theo thứ tự tên tệp mỗi khi một phiên IPython khởi động.

Bạn có thể tạo tệp `00-first.py` trong thư mục trên với nội dung:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình chỉ chạy khi đang ở trong IPython.
from IPython import get_ipython
shell = get_ipython()
if shell is not None:
    shell.run_line_magic("load_ext", "autoreload")
    shell.run_line_magic("autoreload", "2")
```
Mỗi khi bạn mở IPython hoặc Jupyter Notebook, các thư viện `np`, `pd`, `plt` và tiện ích `autoreload` đều đã sẵn sàng mà không cần gõ lại các lệnh nhập thủ công.

---

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Phụ lục B: More on the IPython System.
- Fernando Pérez, Brian E. Granger. *IPython: A System for Interactive Scientific Computing*. Computing in Science & Engineering, 2007.
- IPython Development Team. *IPython Interactive Computing Documentation*. https://ipython.readthedocs.io/

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 8. Bài tập thực hành

::: exercise Bài tập 1: Đo lường và so sánh hiệu năng giữa thuật toán thuần và thư viện bằng %timeit
Một bài toán yêu cầu tính tổng bình phương của $100\,000$ số nguyên từ $0$ đến $99\,999$:
$$
S = \sum_{i=0}^{99\,999} i^2
$$
1. Hãy viết biểu thức tính toán bằng Python thuần sử dụng hàm `sum()` kết hợp với biểu thức sinh (*generator expression*).
2. Hãy viết biểu thức tính toán sử dụng mảng NumPy và hàm `np.sum()`.
3. Với $n=100\,000$, kiểm chứng hai cách tính bằng công thức tổng bình phương:
   $$
   S = \frac{(n-1)n(2n-1)}{6}.
   $$
4. Dùng lệnh ma thuật `%timeit` để đo thời gian thực thi của cả hai phương pháp và nhận xét về sự chênh lệch hiệu năng.
:::

::: solution Lời giải
```python
import numpy as np

n = 100_000
arr = np.arange(n, dtype=np.int64)

# 1. Python thuần với generator
tong_py = sum(x**2 for x in range(n))

# 2. NumPy vector hóa
tong_np = np.sum(arr**2)

# 3. Kiểm chứng bằng công thức toán học giải tích
tong_giai_tich = (n - 1) * n * (2 * n - 1) // 6

assert tong_py == tong_np == tong_giai_tich
print(f"Tổng bình phương tính toán: {tong_np:,}")

# 4. Đo đạc thời gian bằng %timeit trong IPython
# %timeit sum(x**2 for x in range(n))
# %timeit np.sum(arr**2)
```

Kết quả đo lường thực tế trên máy tính:
- Python thuần: Tiêu tốn khoảng $6{,}5\text{ ms}$ cho mỗi lượt tính do phải duyệt qua $100\,000$ số nguyên và thực hiện phép nhân mũ trong máy ảo.
- NumPy vector hóa: Tiêu tốn khoảng $45\text{ µs}$ ($0{,}045\text{ ms}$).
- Nhận xét: Phiên bản vector hóa của NumPy nhanh hơn khoảng $140$ lần so với Python thuần, chứng minh sự vượt trội của việc xử lý dữ liệu số học trong vùng nhớ liên tục được tối ưu hóa phần cứng.
:::

::: exercise Bài tập 2: Tự động hóa trích xuất kết quả từ lịch sử In và Out
Trong một phiên làm việc khám phá dữ liệu, người phân tích đã chạy các câu lệnh tính toán sau:
- Lượt 1: Khởi tạo biến dữ liệu doanh thu.
- Lượt 2: Tính doanh thu trung bình.
- Lượt 3: Tính độ lệch chuẩn.

1. Hãy giải thích cơ chế lưu trữ của danh sách `In` và từ điển `Out` trong IPython.
2. Giả sử tại lượt thứ 4, người phân tích muốn tính hệ số biến thiên (*Coefficient of Variation - CV*), định nghĩa bằng tỉ số giữa độ lệch chuẩn (tính ở lượt 3) và trung bình (tính ở lượt 2):
   $$
   CV = \frac{\text{Out}[3]}{\text{Out}[2]}
   $$
   Hãy viết biểu thức trích xuất giá trị từ `Out` để tính toán chỉ số trên mà không cần thực thi lại mã nguồn của lượt 2 và lượt 3.
3. Khi nào một câu lệnh trong `In` không có giá trị tương ứng trong `Out`? Cho ví dụ cụ thể.
:::

::: solution Lời giải
1. Cơ chế lưu trữ của `In` và `Out`:
   - `In` là một danh sách các chuỗi văn bản (`list` of `str`). Mỗi phần tử `In[n]` lưu trữ nguyên vẹn đoạn mã nguồn mà người dùng đã nhập ở lượt thứ $n$.
   - `Out` là một từ điển (`dict`). Mỗi mục `Out[n]` lưu trữ đối tượng Python thực tế là kết quả của biểu thức được đánh giá ở lượt thứ $n$.
2. Tính toán hệ số biến thiên sử dụng từ điển `Out`:
```python
# Mô phỏng trạng thái lịch sử
In = ["", "du_lieu = [10, 20, 30, 40, 50]", "np.mean(du_lieu)", "np.std(du_lieu)"]
Out = {2: 30.0, 3: 14.142135623730951}

# Tính hệ số biến thiên CV từ lịch sử Out
cv = Out[3] / Out[2]
print(f"Hệ số biến thiên CV: {cv:.4f}")  # 0.4714
```
   Biểu thức này lấy trực tiếp hai con số đã tính toán trong RAM mà không cần duyệt lại tập dữ liệu `du_lieu`.
3. Câu lệnh không có kết quả trong `Out`:
   - Mọi câu lệnh gán biến (như `x = 100`), câu lệnh điều khiển (như `for`, `if`), định nghĩa hàm (`def`), hoặc hàm trả về `None` (chẳng hạn `print("Xin chào")`) đều không sinh ra giá trị đầu ra. Do đó, các lượt chạy này chỉ được ghi nhận trong danh sách `In` mà hoàn toàn vắng mặt trong từ điển `Out`.
:::

::: exercise Bài tập 3: Mô phỏng phân tích hiệu năng từng dòng để xác định điểm nghẽn
Cho hàm làm sạch dữ liệu chuỗi thô sau:
```python
import re

def lam_sach_du_lieu(danh_sach_ban_ghi):
    ket_qua = []
    for ban_ghi in danh_sach_ban_ghi:
        s = ban_ghi.strip()
        if s != "N/A":
            so_thuc = float(s)
            ket_qua.append(so_thuc)
    return ket_qua
```
1. Phân tích chức năng của từng dòng mã trong hàm trên.
2. Dữ liệu thử nghiệm gồm các bản ghi: `[" 100.5 ", " 200.75 ", " N/A ", " 300.0 "]`. Hãy chạy hàm và tính tổng các số thu được.
3. Trong các dòng mã bên trong vòng lặp, dòng lệnh nào có khả năng tiêu tốn nhiều thời gian nhất khi xử lý hàng triệu bản ghi? Đề xuất phương án tối ưu hóa hiệu năng nếu dữ liệu có thể chuyển đổi thành mảng pandas hoặc NumPy.
:::

::: solution Lời giải
1. Phân tích chức năng:
   - `s = ban_ghi.strip()`: Loại bỏ các khoảng trắng thừa ở hai đầu chuỗi ký tự.
   - `if s != "N/A"`: Kiểm tra giá trị chuỗi có phải là chuỗi đánh dấu khuyết thiếu hay không.
   - `so_thuc = float(s)`: Ép kiểu chuỗi ký tự sang số thực dấu phẩy động.
   - `ket_qua.append(so_thuc)`: Thêm số thực hợp lệ vào danh sách kết quả.
2. Chạy thử nghiệm và kiểm chứng:
```python
ban_ghi_mau = [" 100.5 ", " 200.75 ", " N/A ", " 300.0 "]
du_lieu_sach = lam_sach_du_lieu(ban_ghi_mau)

assert du_lieu_sach == [100.5, 200.75, 300.0]
tong_gia_tri = sum(du_lieu_sach)
print(f"Tổng giá trị hợp lệ: {tong_gia_tri}")  # 601.25
```
3. Đánh giá hiệu năng và tối ưu hóa:
   - Khi xử lý hàng triệu bản ghi, thao tác `float(s)` và `ban_ghi.strip()` trên từng đối tượng chuỗi Python thông dịch chiếm phần lớn thời gian (thường chiếm trên $70\%$ tổng thời gian hàm theo báo cáo `%lprun`).
   - Phương án tối ưu hóa: Chuyển toàn bộ danh sách chuỗi thô thành một đối tượng `Series` của pandas và sử dụng hàm vector hóa chuyên dụng `pd.to_numeric(s.str.strip(), errors="coerce")`. Cách làm này đẩy toàn bộ vòng lặp phân tích chuỗi xuống tầng C, tự động chuyển đổi các giá trị `"N/A"` thành `NaN` và tăng tốc độ xử lý lên từ 10 đến 50 lần.
:::

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Phụ lục B: More on the IPython System.
- Fernando Pérez, Brian E. Granger. *IPython: A System for Interactive Scientific Computing*. Computing in Science & Engineering, 2007.
- IPython Development Team. *IPython Interactive Computing Documentation*. https://ipython.readthedocs.io/

</div>
