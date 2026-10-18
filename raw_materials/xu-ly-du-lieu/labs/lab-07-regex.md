## Bonus regex: 20 bài tập kiểm tra và trích xuất chuỗi

Một mã sản phẩm, số điện thoại hay địa chỉ tệp đều có quy tắc về ký tự và thứ tự. Trong 20 bài dưới đây, hãy viết rõ quy tắc đó bằng biểu thức chính quy, rồi kiểm tra cả chuỗi đúng lẫn chuỗi gần đúng.

## Quy ước chung

Các bài dùng chung những quy ước sau:

- Kiểu dữ liệu đầu vào: Mỗi hàm nhận đầu vào là chuỗi `str` hoặc giá trị khuyết thiếu `None`. Không thực hiện các thao tác tiền xử lý làm biến dạng chuỗi gốc như tự ý cắt tỉa khoảng trắng (`strip`) hay hạ chữ thường (`lower`) trước khi kiểm tra định dạng.
- Miền chữ số và ký tự: Toàn bộ chữ số được quy ước trên dải ký tự ASCII chuẩn `[0-9]`. Biểu thức chính quy từ chối các ký tự số thuộc dải Unicode mở rộng (như chữ số toàn giác hoặc chữ số Ả Rập), trừ bài tập có yêu cầu xử lý khoảng trắng Unicode riêng biệt.
- Phân biệt hoa thường: Mặc định mọi bài toán đều phân biệt chữ hoa và chữ thường với cờ quy ước bằng 0. Riêng Bài 10 cho phép sử dụng cờ `re.IGNORECASE` (viết tắt là `re.I`) để nhận diện linh hoạt các biến thể viết tắt của phòng ngủ.
- Giới hạn tính năng regex: Tuyệt đối không sử dụng các kỹ thuật nhìn trước/nhìn sau (lookaround assertions) hoặc tham chiếu ngược (backreferences). Giới hạn này giúp tập trung vào ký tự, lượng từ và nhóm bắt. Nó không có nghĩa bộ máy `re` của Python luôn xử lý mẫu bằng một thuật toán không quay lui.
- Bảo toàn kiểu dữ liệu đầu ra: Phân biệt rành mạch giữa các bài toán kiểm tra tính hợp lệ (trả về giá trị boolean `True` hoặc `False`, trong đó `None` luôn trả về `False`) và bài toán trích xuất thuộc tính (trả về `str`, `tuple` hoặc `None`). Tuyệt đối không ép kiểu số nguyên đối với các mã số nhận diện nhằm tránh làm mất các chữ số 0 ở đầu.
- Hai phương pháp giải độc lập: Mỗi bài toán đều cung cấp hai giải pháp hoàn chỉnh: Cách 1 dành cho người mới bắt đầu (gọi trực tiếp hàm từ module `re`) và Cách 2 ứng dụng thực tế (biên dịch trước mẫu với `re.compile`). Mọi khối mã đều độc lập, có đủ câu lệnh nạp thư viện, hàm xử lý, dữ liệu mẫu và lời gọi kiểm thử in kết quả.

Các hàm như `re.search` và `re.fullmatch` cũng lưu đệm các mẫu dùng gần đây. Vì vậy, `re.compile` giúp quản lý và tái sử dụng mẫu, nhưng không tự bảo đảm chương trình chạy nhanh hơn. Hai cách trong mỗi bài dùng cùng mẫu và phải trả về cùng kết quả. [Tài liệu Python về `re.compile`](https://docs.python.org/3/library/re.html#re.compile).

---

## Danh mục bài tập thực hành

<span id="data-lab-07-regex-01"></span>
### Bài 1: Trích dãy chữ số đầu tiên trong chuỗi văn bản

::: exercise
Trong quá trình thu thập và làm sạch dữ liệu văn bản từ biểu mẫu nhập liệu hoặc nhật ký hệ thống, mã số định danh thường bị lẫn lộn giữa các ký tự chữ hoặc dấu câu. Bài toán đặt ra là cần lấy ra chuỗi chữ số ASCII xuất hiện đầu tiên để làm khóa tra cứu ban đầu.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng biểu thức chính quy để tìm kiếm dãy chữ số ASCII liên tiếp đầu tiên mà không làm thay đổi các ký tự gốc.
- Đầu ra: Trả về chuỗi `str` chứa các chữ số tìm thấy đầu tiên. Nếu `text` là `None` hoặc không chứa chữ số ASCII nào, trả về `None`. Tuyệt đối không chuyển đổi sang số nguyên `int` nhằm tránh làm mất các chữ số 0 ở đầu (ví dụ: Chuỗi `'007'`).
- Trường hợp biên: Giá trị `None`, chuỗi rỗng `''`, chuỗi không có số, chữ số dạng Unicode toàn giác như `'１２３'` hoặc chữ số Ả Rập như `'١٢٣'` đều phải trả về `None`.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"[0-9]+"


def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=0)
    return m.group(0) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "abc123xyz",
    'define "123"',
    "var g = 123;",
    "P007 / P12",
    "không có mã",
    None,
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"[0-9]+"`:
  - Lớp ký tự `[0-9]`: Chỉ so khớp đúng các ký tự chữ số thuộc bảng mã ASCII chuẩn từ `0` đến `9`. Lớp ký tự này từ chối các ký tự chữ số thuộc dải Unicode mở rộng như chữ số toàn giác `'１２３'` hay chữ số Ả Rập `'١٢٣'`, giữ đúng miền chữ số của đề bài.
  - Lượng từ `+`: Yêu cầu xuất hiện một hoặc nhiều lần liên tiếp, so khớp tham lam (greedy) toàn bộ dãy số liền kề.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Kiểm tra điều kiện đầu vào: Nếu `text is None`, hàm lập tức trả về `None` mà không truyền vào `re.search` nhằm tránh phát sinh ngoại lệ `TypeError`.
  - Hàm `re.search(PATTERN, text, flags=0)`: Quét từ trái sang phải trên chuỗi `text` và dừng lại ngay tại vị trí đầu tiên tìm thấy đoạn con khớp với mẫu.
  - Đối tượng `Match` và phương thức `.group(0)`: Nếu có kết quả khớp (`m is not None`), `m.group(0)` trả về toàn bộ chuỗi con vừa khớp. Nếu không tìm thấy, `m` mang giá trị `None` và hàm trả về `None`.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'abc123xyz'</code> | <code>'123'</code> | `str` |
| <code>'define "123"'</code> | <code>'123'</code> | `str` |
| <code>'var g = 123;'</code> | <code>'123'</code> | `str` |
| <code>'P007 / P12'</code> | <code>'007'</code> | `str` |
| <code>'không có mã'</code> | <code>None</code> | `NoneType` |
| <code>None</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"[0-9]+")


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.search(text)
    return m.group(0) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "abc123xyz",
    'define "123"',
    "var g = 123;",
    "P007 / P12",
    "không có mã",
    None,
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.search(text)`: Thực hiện tìm kiếm trực tiếp trên chuỗi đầu vào mà không cần lặp lại bước kiểm tra cú pháp mẫu ở mỗi lời gọi.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'abc123xyz'</code> | <code>'123'</code> | `str` |
| <code>'define "123"'</code> | <code>'123'</code> | `str` |
| <code>'var g = 123;'</code> | <code>'123'</code> | `str` |
| <code>'P007 / P12'</code> | <code>'007'</code> | `str` |
| <code>'không có mã'</code> | <code>None</code> | `NoneType` |
| <code>None</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.search`: Thuận tiện cho các tác vụ phân tích nhanh, kịch bản thử nghiệm ngắn, hoặc khi mẫu biểu thức chính quy chỉ dùng một lần duy nhất.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-02"></span>
### Bài 2: Dấu chấm thường và ký tự đại diện trong chuỗi ba ký tự

::: exercise
Trong việc xác thực mã định danh ngắn gọn từ biểu mẫu người dùng, hệ thống quy định mã hợp lệ phải gồm đúng ba ký tự bất kỳ và bắt buộc kết thúc bằng một dấu chấm thông thường. Cần kiểm tra toàn bộ chuỗi để từ chối các mã sai độ dài.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng biểu thức chính quy kiểm tra toàn chuỗi (fullmatch), phân biệt giữa ký tự đại diện chấm và ký tự dấu chấm nguyên văn.
- Đầu ra: Trả về `True` nếu toàn bộ chuỗi thỏa mãn mẫu định dạng, ngược lại trả về `False`. Đầu vào `None` bắt buộc trả về `False`.
- Trường hợp biên: Ba ký tự đầu có thể là chữ cái, chữ số, khoảng trắng hoặc dấu câu, nhưng không chứa ký tự xuống dòng `\n`. Ký tự cuối cùng bắt buộc là dấu chấm literal. Chuỗi thiếu ký tự (như `'ab.'`) hoặc thừa ký tự (như `'abcd.'`) đều bị từ chối.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"...\."


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["cat.", "896.", "?=+.", "abc1", "ab.", "abcd."]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"...\."`:
  - Ba dấu chấm đầu `...`: Mỗi dấu chấm đóng vai trò là một ký tự đại diện (wildcard), so khớp với đúng một ký tự bất kỳ ngoại trừ ký tự xuống dòng `\n` (khi không bật cờ `re.DOTALL`). Ba dấu chấm liên tiếp yêu cầu chính xác ba ký tự ở tiền tố.
  - Ký tự thoát `\.`: Ký tự gạch chéo ngược vô hiệu hóa tính năng đại diện của dấu chấm, buộc vị trí thứ tư phải là một ký tự dấu chấm nguyên văn.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Kiểm tra điều kiện đầu vào: Nếu `text is None`, hàm lập tức trả về `False` theo đúng quy ước kiểm tra logic boolean của đề bài.
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Yêu cầu toàn bộ chuỗi từ vị trí bắt đầu đến vị trí kết thúc phải khớp trọn vẹn với mẫu. Điều này ngăn chặn việc khớp một phần khi chuỗi dài hơn bốn ký tự.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'cat.'</code> | <code>True</code> | `bool` |
| <code>'896.'</code> | <code>True</code> | `bool` |
| <code>'?=+.'</code> | <code>True</code> | `bool` |
| <code>'abc1'</code> | <code>False</code> | `bool` |
| <code>'ab.'</code> | <code>False</code> | `bool` |
| <code>'abcd.'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"...\.")


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["cat.", "896.", "?=+.", "abc1", "ab.", "abcd."]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Kiểm tra độ dài và từng vị trí ký tự từ đầu đến cuối chuỗi một cách trực tiếp.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'cat.'</code> | <code>True</code> | `bool` |
| <code>'896.'</code> | <code>True</code> | `bool` |
| <code>'?=+.'</code> | <code>True</code> | `bool` |
| <code>'abc1'</code> | <code>False</code> | `bool` |
| <code>'ab.'</code> | <code>False</code> | `bool` |
| <code>'abcd.'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Rõ ràng, dễ đọc cho các đoạn mã kiểm tra tính hợp lệ nhanh trong các câu lệnh điều kiện đơn lẻ.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-03"></span>
### Bài 3: Chọn ký tự trong tập cho trước kết hợp phần đuôi cố định

::: exercise
Trong việc chuẩn hóa các từ viết tắt hoặc danh từ quy ước trong kho dữ liệu, hệ thống chỉ chấp nhận các từ có ký tự đầu thuộc tập hợp `c`, `m`, `f` và hai ký tự tiếp theo bắt buộc là `an`. Mọi từ khác ngoài danh mục này đều coi là không hợp lệ.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng lớp ký tự (character class) trong biểu thức chính quy để kiểm tra toàn bộ chuỗi theo đúng tập ký tự cho phép.
- Đầu ra: Trả về `True` nếu chuỗi khớp chính xác một trong các từ `can`, `man`, `fan`. Ngược lại trả về `False`. Đầu vào `None` trả về `False`.
- Trường hợp biên: Phân biệt hoa thường, từ chối chữ hoa như `'Can'` hay `'FAN'`. Khoảng trắng ở đầu hoặc cuối (như `' can '`) làm chuỗi không hợp lệ vì phương thức `fullmatch` kiểm tra toàn bộ chuỗi.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"[cmf]an"


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["can", "man", "fan", "dan", "ran", "pan"]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"[cmf]an"`:
  - Lớp ký tự `[cmf]`: Định nghĩa một tập hợp gồm đúng ba ký tự chữ cái viết thường. Biểu thức chỉ chấp nhận duy nhất một ký tự tại vị trí này nếu ký tự đó là `c`, `m` hoặc `f`.
  - Hai ký tự cố định `an`: Đòi hỏi hai ký tự tiếp theo phải xuất hiện nguyên vẹn theo đúng thứ tự.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Buộc chuỗi phải có đúng ba ký tự. Nếu dùng dấu chấm đại diện `.` thay cho `[cmf]`, mẫu sẽ nhận nhầm cả các từ ngoài danh mục như `dan`, `ran`, `pan`. Do đó, lớp ký tự đóng vai trò hạn định chính xác không gian ký tự hợp lệ.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'can'</code> | <code>True</code> | `bool` |
| <code>'man'</code> | <code>True</code> | `bool` |
| <code>'fan'</code> | <code>True</code> | `bool` |
| <code>'dan'</code> | <code>False</code> | `bool` |
| <code>'ran'</code> | <code>False</code> | `bool` |
| <code>'pan'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"[cmf]an")


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["can", "man", "fan", "dan", "ran", "pan"]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Kiểm tra toàn bộ chuỗi. Kết quả là `Match` nếu khớp, hoặc `None` nếu không khớp.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'can'</code> | <code>True</code> | `bool` |
| <code>'man'</code> | <code>True</code> | `bool` |
| <code>'fan'</code> | <code>True</code> | `bool` |
| <code>'dan'</code> | <code>False</code> | `bool` |
| <code>'ran'</code> | <code>False</code> | `bool` |
| <code>'pan'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Gọn nhẹ, thích hợp khi kiểm tra dữ liệu trong các hàm phụ trợ dùng một lần.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-04"></span>
### Bài 4: Kết hợp các dải khoảng ký tự rời rạc theo từng vị trí

::: exercise
Trong hệ thống mã hóa định danh kiểm kê, mỗi mã hợp lệ bắt buộc gồm đúng ba ký tự với quy chuẩn chặt chẽ theo từng vị trí: Vị trí đầu là chữ hoa từ A đến C, vị trí thứ hai là chữ thường từ n đến p, vị trí cuối cùng là chữ thường từ a đến c.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng dải ký tự (character range) với dấu gạch ngang bên trong ngoặc vuông để thiết lập điều kiện cho từng vị trí độc lập.
- Đầu ra: Trả về `True` nếu chuỗi thỏa mãn trọn vẹn cả ba khoảng ký tự, ngược lại trả về `False`. Đầu vào `None` trả về `False`.
- Trường hợp biên: Phân biệt hoa thường tuyệt đối. Bao gồm cả hai đầu mút của dải (chẳng hạn `'Cpc'` hợp lệ vì C, p, c đều nằm tại cận trên tương ứng). Chuỗi có bất kỳ ký tự nào nằm ngoài dải quy định đều bị từ chối.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"[A-C][n-p][a-c]"


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["Ana", "Bob", "Cpc", "aax", "bby", "ccz"]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"[A-C][n-p][a-c]"`:
  - Vị trí thứ nhất `[A-C]`: Đại diện cho một ký tự chữ cái viết hoa thuộc tập `{A, B, C}`.
  - Vị trí thứ hai `[n-p]`: Đại diện cho một ký tự chữ cái viết thường thuộc tập `{n, o, p}`.
  - Vị trí thứ ba `[a-c]`: Đại diện cho một ký tự chữ cái viết thường thuộc tập `{a, b, c}`.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Kiểm tra toàn diện toàn bộ chuỗi. Mẫu không chứa lượng từ lặp nào nên chuỗi hợp lệ bắt buộc phải có độ dài chính xác bằng ba ký tự. Bất kỳ sự lệch hoa thường hay vượt quá biên dải mã ASCII đều khiến hàm trả về `False`.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'Ana'</code> | <code>True</code> | `bool` |
| <code>'Bob'</code> | <code>True</code> | `bool` |
| <code>'Cpc'</code> | <code>True</code> | `bool` |
| <code>'aax'</code> | <code>False</code> | `bool` |
| <code>'bby'</code> | <code>False</code> | `bool` |
| <code>'ccz'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"[A-C][n-p][a-c]")


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["Ana", "Bob", "Cpc", "aax", "bby", "ccz"]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét và kiểm định tính hợp lệ của chuỗi một cách trực tiếp mà không cần phân tích lại chuỗi biểu thức chính quy.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'Ana'</code> | <code>True</code> | `bool` |
| <code>'Bob'</code> | <code>True</code> | `bool` |
| <code>'Cpc'</code> | <code>True</code> | `bool` |
| <code>'aax'</code> | <code>False</code> | `bool` |
| <code>'bby'</code> | <code>False</code> | `bool` |
| <code>'ccz'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Đơn giản, trực quan, phù hợp khi chỉ cần xác thực dữ liệu tại một vài vị trí mã nguồn riêng lẻ.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-05"></span>
### Bài 5: Giới hạn số lần lặp với khoảng định lượng số lần xuất hiện

::: exercise
Trong việc phân tích dữ liệu văn bản từ mạng xã hội hoặc diễn đàn trao đổi, người dùng thường kéo dài một số ký tự để nhấn mạnh cảm xúc. Hệ thống yêu cầu xác định các từ bắt đầu bằng `wa`, theo sau bởi từ 3 đến 5 ký tự `z`, và kết thúc bằng `up`.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng cú pháp định lượng khoảng `{m,n}` để kiểm soát chính xác số lần lặp tối thiểu và tối đa của ký tự mục tiêu.
- Đầu ra: Trả về `True` nếu chuỗi khớp chính xác quy tắc số lượng ký tự lặp, ngược lại trả về `False`. Đầu vào `None` trả về `False`.
- Trường hợp biên: Chuỗi chỉ có 1 hoặc 2 chữ `z` (như `'wazup'`, `'wazzup'`) hoặc có từ 6 chữ `z` trở lên (như `'wazzzzzzup'`) đều bị loại bỏ hoàn toàn.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"waz{3,5}up"


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["wazzzup", "wazzzzup", "wazzzzzup", "wazup", "wazzup", "wazzzzzzup"]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"waz{3,5}up"`:
  - Ký tự tiền tố `wa`: Bắt buộc xuất hiện chính xác hai ký tự này ở đầu chuỗi.
  - Định lượng khoảng `{3,5}`: Tác động trực tiếp lên ký tự `z` đứng ngay trước nó, quy định ký tự `z` phải xuất hiện tối thiểu 3 lần và tối đa 5 lần.
  - Ký tự hậu tố `up`: Bắt buộc xuất hiện hai ký tự này ở cuối chuỗi.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Bảo đảm chuỗi không chứa thêm bất kỳ ký tự nào khác ở cả hai đầu. Nếu chuỗi có 2 ký tự `z` thì vi phạm cận dưới, còn nếu có 6 ký tự `z` thì vi phạm cận trên, tất cả đều được phát hiện chính xác.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'wazzzup'</code> | <code>True</code> | `bool` |
| <code>'wazzzzup'</code> | <code>True</code> | `bool` |
| <code>'wazzzzzup'</code> | <code>True</code> | `bool` |
| <code>'wazup'</code> | <code>False</code> | `bool` |
| <code>'wazzup'</code> | <code>False</code> | `bool` |
| <code>'wazzzzzzup'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"waz{3,5}up")


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["wazzzup", "wazzzzup", "wazzzzzup", "wazup", "wazzup", "wazzzzzzup"]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét trọn vẹn chuỗi và trả về đối tượng `Match` nếu số lần lặp thỏa mãn phạm vi số học.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'wazzzup'</code> | <code>True</code> | `bool` |
| <code>'wazzzzup'</code> | <code>True</code> | `bool` |
| <code>'wazzzzzup'</code> | <code>True</code> | `bool` |
| <code>'wazup'</code> | <code>False</code> | `bool` |
| <code>'wazzup'</code> | <code>False</code> | `bool` |
| <code>'wazzzzzzup'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Rất phù hợp cho các bài kiểm tra logic định dạng đơn giản trong tập lệnh phân tích dữ liệu.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-06"></span>
### Bài 6: Phân biệt xuất hiện không lần và xuất hiện ít nhất một lần

::: exercise
Trong việc xác thực chuỗi ký hiệu trạng thái quy trình, chuỗi hợp lệ phải tuân theo cấu trúc tuần tự nghiêm ngặt: Có ít nhất hai ký tự `a`, theo sau là ký tự `b` xuất hiện tùy ý không lần hoặc nhiều lần, và kết thúc bằng ít nhất một ký tự `c`.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Kết hợp lượng từ mở rộng `{2,}`, dấu sao `*` và dấu cộng `+` trong một mẫu biểu thức duy nhất để kiểm tra toàn bộ chuỗi.
- Đầu ra: Trả về `True` nếu chuỗi thỏa mãn đúng cấu trúc và số lượng ký tự, ngược lại trả về `False`. Đầu vào `None` trả về `False`.
- Trường hợp biên: Chuỗi chỉ có một chữ `a` (như `'abc'`), chuỗi thiếu hoàn toàn chữ `c` (như `'aabb'`), hoặc chuỗi sai trật tự vị trí đều không hợp lệ.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"a{2,}b*c+"


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["aaaabcc", "aabbbbc", "aacc", "a", "abc", "aabb"]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"a{2,}b*c+"`:
  - Thành phần `a{2,}`: Đặt cận dưới là hai ký tự `a` mà không giới hạn cận trên, đòi hỏi tối thiểu hai chữ `a` liên tiếp ở đầu chuỗi.
  - Thành phần `b*`: Lượng từ sao cho phép ký tự `b` xuất hiện tùy ý từ không lần đến nhiều lần, do đó sự vắng mặt của `b` (như trong `'aacc'`) vẫn hoàn toàn hợp lệ.
  - Thành phần `c+`: Lượng từ cộng bắt buộc phải có ít nhất một ký tự `c` ở cuối chuỗi.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Đảm bảo toàn bộ chuỗi phải khớp trọn vẹn cả ba khối ký tự theo đúng thứ tự xuất hiện từ trái qua phải mà không có ký tự lạ chen ngang.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'aaaabcc'</code> | <code>True</code> | `bool` |
| <code>'aabbbbc'</code> | <code>True</code> | `bool` |
| <code>'aacc'</code> | <code>True</code> | `bool` |
| <code>'a'</code> | <code>False</code> | `bool` |
| <code>'abc'</code> | <code>False</code> | `bool` |
| <code>'aabb'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"a{2,}b*c+")


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["aaaabcc", "aabbbbc", "aacc", "a", "abc", "aabb"]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét tuần tự toàn chuỗi và kiểm tra điều kiện chuyển tiếp trạng thái.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'aaaabcc'</code> | <code>True</code> | `bool` |
| <code>'aabbbbc'</code> | <code>True</code> | `bool` |
| <code>'aacc'</code> | <code>True</code> | `bool` |
| <code>'a'</code> | <code>False</code> | `bool` |
| <code>'abc'</code> | <code>False</code> | `bool` |
| <code>'aabb'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Trực quan, phù hợp khi kiểm tra quy tắc cú pháp tại một vị trí cục bộ trong hàm xử lý.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-07"></span>
### Bài 7: Ký tự tùy chọn và dấu hỏi chấm thường trong thông báo

::: exercise
Trong việc kiểm tra tính chuẩn mực của các câu thông báo trạng thái tệp tin sinh ra từ hệ thống, câu thông báo hợp lệ bắt đầu bằng số lượng tệp (chữ số đầu từ 1 đến 9), theo sau bởi từ `file` hoặc `files` số nhiều, và kết thúc bằng chuỗi `found?` có dấu hỏi chấm thường.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng dấu hỏi `?` để biểu thị ký tự tùy chọn cho chữ `s` và thoát ký tự dấu hỏi nguyên văn `\?` ở cuối câu thông báo.
- Đầu ra: Trả về `True` nếu câu thông báo khớp trọn vẹn mẫu quy định, ngược lại trả về `False`. Đầu vào `None` trả về `False`.
- Trường hợp biên: Chữ số đầu tiên phải thuộc dải `[1-9]`, tức là từ chối số 0 hoặc số có số 0 đứng đầu như `'0 files found?'`. Dấu chấm câu ở cuối phải là dấu hỏi chấm literal, từ chối dấu chấm thường như `'2 files found.'`.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"[1-9][0-9]* files? found\?"


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "1 file found?",
    "2 files found?",
    "24 files found?",
    "No files found.",
    "0 files found?",
    "2 files found.",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"[1-9][0-9]* files? found\?"`:
  - Khối chữ số `[1-9][0-9]*`: Ký tự đầu tiên thuộc tập `[1-9]` ngăn chặn hoàn toàn số 0 hoặc các số có số 0 ở đầu. Các ký tự số tiếp theo `[0-9]*` cho phép số lượng tệp có giá trị từ 1 đến hàng triệu.
  - Từ số nhiều tùy chọn `files?`: Dấu hỏi `?` đứng ngay sau chữ `s` biến riêng chữ cái `s` thành tùy chọn, chấp nhận cả `'file'` (khi số lượng là 1) và `'files'` (khi số lượng từ 2 trở lên).
  - Thoát dấu hỏi kết thúc `found\?`: Ký hiệu `\?` buộc ký tự cuối cùng của thông báo phải là dấu hỏi chấm thật trong bảng mã ASCII.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Kiểm tra từ đầu đến cuối câu thông báo, loại bỏ các chuỗi thừa từ hoặc sai dấu chấm câu ở cuối.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'1 file found?'</code> | <code>True</code> | `bool` |
| <code>'2 files found?'</code> | <code>True</code> | `bool` |
| <code>'24 files found?'</code> | <code>True</code> | `bool` |
| <code>'No files found.'</code> | <code>False</code> | `bool` |
| <code>'0 files found?'</code> | <code>False</code> | `bool` |
| <code>'2 files found.'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"[1-9][0-9]* files? found\?")


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "1 file found?",
    "2 files found?",
    "24 files found?",
    "No files found.",
    "0 files found?",
    "2 files found.",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Kiểm tra toàn bộ chuỗi thông báo và trả về đối tượng khớp hoặc `None`.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'1 file found?'</code> | <code>True</code> | `bool` |
| <code>'2 files found?'</code> | <code>True</code> | `bool` |
| <code>'24 files found?'</code> | <code>True</code> | `bool` |
| <code>'No files found.'</code> | <code>False</code> | `bool` |
| <code>'0 files found?'</code> | <code>False</code> | `bool` |
| <code>'2 files found.'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Thuận tiện khi viết nhanh các kịch bản kiểm tra đơn giản trong giai đoạn phát triển thử nghiệm.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-08"></span>
### Bài 8: Ràng buộc ký tự phân cách khoảng trắng sau số thứ tự

::: exercise
Trong việc phân tích các dòng văn bản dạng danh mục có đánh số thứ tự, mỗi dòng hợp lệ phải gồm một số nguyên, theo sau là dấu chấm nguyên văn, bắt buộc có ít nhất một ký tự khoảng trắng phân cách (dấu cách hoặc ký tự tab), rồi đến chuỗi ký tự `abc`.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng lớp ký tự trắng `\s+` để ràng buộc sự xuất hiện bắt buộc của khoảng trắng phân cách sau dấu chấm.
- Đầu ra: Trả về `True` nếu chuỗi có số, dấu chấm, khoảng trắng phân cách và `abc`. Ngược lại trả về `False`. Đầu vào `None` trả về `False`.
- Trường hợp biên: Chuỗi dính liền không có khoảng trắng như `'4.abc'` bị loại hoàn toàn. Ký tự phân cách phải là dấu chấm literal `\.`, từ chối ký tự khác như `'1x abc'`.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"[0-9]+\.\s+abc"


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["1.   abc", "2.\tabc", "3.           abc", "4.abc", "12. abc", "1x abc"]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"[0-9]+\.\s+abc"`:
  - Khối số thứ tự `[0-9]+`: Khớp một hoặc nhiều chữ số ASCII liên tiếp.
  - Thoát dấu chấm `\.`: Đảm bảo dấu chấm là một ký tự literal, không phải ký tự đại diện wildcard.
  - Lớp ký tự trắng bắt buộc `\s+`: Nhận diện một hoặc nhiều ký tự trắng liên tiếp (bao gồm dấu cách và tab `\t`). Việc dùng lượng từ `+` thay vì `*` là điều kiện tiên quyết để buộc phải có khoảng trống phân cách giữa số thứ tự và nội dung.
  - Nội dung cố định `abc`: Bắt buộc kết thúc bằng đúng ba ký tự chữ cái này.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Đảm bảo toàn bộ dòng văn bản tuân thủ quy chuẩn, từ chối các dòng dính liền ký tự hoặc sai dấu chấm.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'1.   abc'</code> | <code>True</code> | `bool` |
| <code>'2.\tabc'</code> | <code>True</code> | `bool` |
| <code>'3.           abc'</code> | <code>True</code> | `bool` |
| <code>'4.abc'</code> | <code>False</code> | `bool` |
| <code>'12. abc'</code> | <code>True</code> | `bool` |
| <code>'1x abc'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"[0-9]+\.\s+abc")


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["1.   abc", "2.\tabc", "3.           abc", "4.abc", "12. abc", "1x abc"]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét và kiểm tra tính toàn vẹn của chuỗi ký tự theo quy tắc phân định ranh giới.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'1.   abc'</code> | <code>True</code> | `bool` |
| <code>'2.\tabc'</code> | <code>True</code> | `bool` |
| <code>'3.           abc'</code> | <code>True</code> | `bool` |
| <code>'4.abc'</code> | <code>False</code> | `bool` |
| <code>'12. abc'</code> | <code>True</code> | `bool` |
| <code>'1x abc'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Tiện lợi cho các tác vụ xử lý dòng dữ liệu ngắn trong các sổ tay tính toán.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-09"></span>
### Bài 9: Trích xuất tên tệp PDF bằng nhóm bắt độc lập

::: exercise
Trong việc bóc tách danh mục tài liệu lưu trữ, hệ thống cần trích xuất phần tên chính của các tệp tài liệu định dạng PDF. Tên tệp hợp lệ bắt buộc bắt đầu bằng tiền tố `file`, theo sau bởi ít nhất một ký tự chữ cái, chữ số hoặc gạch dưới, và kết thúc bằng phần mở rộng `.pdf`.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng nhóm bắt (capturing group) bao quanh phần tên tệp để lấy ra tên gốc mà không chứa phần mở rộng `.pdf`.
- Đầu ra: Trả về chuỗi `str` chứa tên tệp (bao gồm cả tiền tố `file`). Nếu chuỗi không phải tệp PDF hợp lệ hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Các tệp tạm thời có phần mở rộng kép như `'fileA.pdf.tmp'` hoặc đường dẫn thư mục đều bị từ chối. Tên tệp không được chỉ có đúng từ `'file'` mà bắt buộc phải có thêm ký tự phía sau.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"(file[A-Za-z0-9_]+)\.pdf"


def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "file_record_transcript.pdf",
    "file_07241999.pdf",
    "fileA1.pdf",
    "testfile_fake.pdf.tmp",
    "fileA.pdf.tmp",
    "fileA.txt",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"(file[A-Za-z0-9_]+)\.pdf"`:
  - Nhóm bắt `(file[A-Za-z0-9_]+)`: Cặp ngoặc đơn thiết lập nhóm bắt số 1, bao trọn tiền tố `file` và dãy ký tự tiếp theo gồm chữ cái, chữ số hoặc dấu gạch dưới. Lượng từ `+` yêu cầu có tối thiểu một ký tự sau tiền tố `file`.
  - Phần mở rộng `\.pdf`: Nằm bên ngoài nhóm bắt, yêu cầu chuỗi phải kết thúc bằng dấu chấm và chuỗi `pdf`.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Buộc toàn bộ chuỗi phải là tên tệp hoàn chỉnh, loại bỏ hoàn toàn các trường hợp tệp có thêm đuôi phụ như `.pdf.tmp`.
  - Phương thức `.group(1)`: Chỉ trích xuất chuỗi con nằm bên trong cặp ngoặc đơn đầu tiên, loại bỏ phần đuôi `.pdf` mà không cần xử lý cắt chuỗi thủ công.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'file_record_transcript.pdf'</code> | <code>'file_record_transcript'</code> | `str` |
| <code>'file_07241999.pdf'</code> | <code>'file_07241999'</code> | `str` |
| <code>'fileA1.pdf'</code> | <code>'fileA1'</code> | `str` |
| <code>'testfile_fake.pdf.tmp'</code> | <code>None</code> | `NoneType` |
| <code>'fileA.pdf.tmp'</code> | <code>None</code> | `NoneType` |
| <code>'fileA.txt'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"(file[A-Za-z0-9_]+)\.pdf")


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.fullmatch(text)
    return m.group(1) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "file_record_transcript.pdf",
    "file_07241999.pdf",
    "fileA1.pdf",
    "testfile_fake.pdf.tmp",
    "fileA.pdf.tmp",
    "fileA.txt",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Thực hiện so khớp toàn chuỗi và trả về đối tượng `Match` chứa nhóm bắt tương ứng.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'file_record_transcript.pdf'</code> | <code>'file_record_transcript'</code> | `str` |
| <code>'file_07241999.pdf'</code> | <code>'file_07241999'</code> | `str` |
| <code>'fileA1.pdf'</code> | <code>'fileA1'</code> | `str` |
| <code>'testfile_fake.pdf.tmp'</code> | <code>None</code> | `NoneType` |
| <code>'fileA.pdf.tmp'</code> | <code>None</code> | `NoneType` |
| <code>'fileA.txt'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Rõ ràng và tiện dụng khi xử lý danh sách tệp ngắn trong kịch bản lệnh dòng.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-10"></span>
### Bài 10: Trích xuất số lượng phòng ngủ với ranh giới từ và cờ không phân biệt hoa thường

::: exercise
Trong việc khai thác thông tin từ các tiêu đề tin đăng chỗ ở trực tuyến, số lượng phòng ngủ có thể được diễn đạt dưới nhiều dạng viết tắt hoặc danh từ đầy đủ như `1BR`, `3 bedrooms`, `2 br`. Cần trích xuất chính xác con số biểu thị số phòng mà không bị dính vào các mã chữ số khác.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng ranh giới từ `\b`, nhóm không bắt `(?:...)` chứa phép hoặc và bật cờ `re.IGNORECASE` (hoặc `re.I`) để tìm kiếm linh hoạt.
- Đầu ra: Trả về chuỗi `str` chứa con số chỉ số lượng phòng ngủ đầu tiên tìm thấy. Nếu không tìm thấy hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Ranh giới từ ở hai đầu loại bỏ các mã dính liền như `'12bravo'` hoặc `'2BR2BA'`. Không trích xuất các con số biểu thị năm như `'Torre 2024'` vì không đi kèm đơn vị phòng.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"\b([0-9]+)\s*(?:BR|bedrooms?)\b"


def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=re.I)
    return m.group(1) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "Modern 1BR Oasis",
    "Casa 3 bedrooms",
    "Studio 2 br centro",
    "12bravo centro",
    "Modern 2BR2BA",
    "Torre 2024",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"\b([0-9]+)\s*(?:BR|bedrooms?)\b"`:
  - Ranh giới từ `\b`: Đặt ở đầu và cuối mẫu nhằm bảo đảm cụm phòng ngủ là một từ độc lập, không bị lẫn vào các chuỗi số chữ liền kề như `12bravo` hay mã kết hợp `2BR2BA`.
  - Nhóm bắt số lượng `([0-9]+)`: Bắt riêng dãy chữ số biểu thị số lượng phòng ngủ để lấy ra bằng `.group(1)`.
  - Khoảng trắng tùy chọn `\s*`: Cho phép viết liền (như `1BR`) hoặc cách rời (như `3 bedrooms`).
  - Nhóm không bắt đơn vị `(?:BR|bedrooms?)`: Cung cấp hai nhánh lựa chọn viết tắt `BR` hoặc viết đầy đủ `bedroom`/`bedrooms` mà không tạo thêm nhóm bắt phụ trong kết quả.
  - Cờ `re.I` (`re.IGNORECASE`): Cho phép khớp cả chữ hoa và chữ thường như `br`, `Br`, `BR`, `Bedrooms`.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.search(PATTERN, text, flags=re.I)`: Tìm kiếm cụm từ phòng ngủ tại bất kỳ vị trí nào trong chuỗi tiêu đề và trích xuất đúng con số qua `m.group(1)`.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'Modern 1BR Oasis'</code> | <code>'1'</code> | `str` |
| <code>'Casa 3 bedrooms'</code> | <code>'3'</code> | `str` |
| <code>'Studio 2 br centro'</code> | <code>'2'</code> | `str` |
| <code>'12bravo centro'</code> | <code>None</code> | `NoneType` |
| <code>'Modern 2BR2BA'</code> | <code>None</code> | `NoneType` |
| <code>'Torre 2024'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"\b([0-9]+)\s*(?:BR|bedrooms?)\b", flags=re.IGNORECASE)


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.search(text)
    return m.group(1) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "Modern 1BR Oasis",
    "Casa 3 bedrooms",
    "Studio 2 br centro",
    "12bravo centro",
    "Modern 2BR2BA",
    "Torre 2024",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.search(text)`: Quét chuỗi nguồn và trích xuất nhóm bắt số 1 trực tiếp.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'Modern 1BR Oasis'</code> | <code>'1'</code> | `str` |
| <code>'Casa 3 bedrooms'</code> | <code>'3'</code> | `str` |
| <code>'Studio 2 br centro'</code> | <code>'2'</code> | `str` |
| <code>'12bravo centro'</code> | <code>None</code> | `NoneType` |
| <code>'Modern 2BR2BA'</code> | <code>None</code> | `NoneType` |
| <code>'Torre 2024'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.search`: Thuận tiện cho các phân tích khám phá nhanh trên tập mẫu dữ liệu nhỏ.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-11"></span>
### Bài 11: Xác thực số nguyên và số thập phân đơn giản

::: exercise
Trong việc xác thực các trường nhập liệu số học từ bảng dữ liệu tài chính hoặc số lượng tồn kho, giá trị số hợp lệ có thể là số nguyên hoặc số thập phân, có thể mang dấu âm ở đầu. Chuỗi không được chứa chữ cái, đơn vị đo lường hoặc định dạng dở dang.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng biểu thức chính quy kiểm tra toàn chuỗi với phần dấu âm tùy chọn và nhóm thập phân tùy chọn có điều kiện ràng buộc dấu chấm đi kèm chữ số.
- Đầu ra: Trả về `True` nếu chuỗi là số nguyên hoặc số thập phân hợp lệ, ngược lại trả về `False`. Đầu vào `None` trả về `False`.
- Trường hợp biên: Phần nguyên luôn bắt buộc phải có chữ số (từ chối chuỗi khuyết phần nguyên như `'.5'`). Nếu có dấu chấm thập phân thì bắt buộc phải có chữ số đi kèm phía sau (từ chối `'5.'`). Các hậu tố như `'720p'` đều bị loại bỏ.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"-?[0-9]+(?:\.[0-9]+)?"


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["3.14529", "-255.34", "128", "720p", ".5", "5."]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"-?[0-9]+(?:\.[0-9]+)?"`:
  - Dấu âm tùy chọn `-?`: Cho phép số mang dấu âm hoặc không có dấu, nhưng không nhận dấu cộng ở mẫu này.
  - Phần nguyên bắt buộc `[0-9]+`: Đòi hỏi ít nhất một chữ số ở phần nguyên, ngăn chặn lỗi thiếu phần nguyên như `.5`.
  - Nhóm thập phân không bắt `(?:\.[0-9]+)?`: Dấu hỏi ở cuối biến toàn bộ cụm gồm dấu chấm và phần thập phân thành tùy chọn. Nếu dấu chấm xuất hiện thì lượng từ `+` buộc phải có ít nhất một chữ số đi liền sau nó, loại bỏ hoàn toàn các trường hợp viết dở như `12.`.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Kiểm tra từ ký tự đầu tiên đến ký tự cuối cùng của chuỗi, loại trừ các chuỗi chứa ký tự chữ cái như `720p` hoặc ký tự xuống dòng dư thừa.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'3.14529'</code> | <code>True</code> | `bool` |
| <code>'-255.34'</code> | <code>True</code> | `bool` |
| <code>'128'</code> | <code>True</code> | `bool` |
| <code>'720p'</code> | <code>False</code> | `bool` |
| <code>'.5'</code> | <code>False</code> | `bool` |
| <code>'5.'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"-?[0-9]+(?:\.[0-9]+)?")


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["3.14529", "-255.34", "128", "720p", ".5", "5."]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét toàn bộ chuỗi số và xác định ngay tính hợp lệ mà không cần kiểm tra lại cú pháp mẫu.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'3.14529'</code> | <code>True</code> | `bool` |
| <code>'-255.34'</code> | <code>True</code> | `bool` |
| <code>'128'</code> | <code>True</code> | `bool` |
| <code>'720p'</code> | <code>False</code> | `bool` |
| <code>'.5'</code> | <code>False</code> | `bool` |
| <code>'5.'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Thuận tiện cho các hàm lọc đơn giản trong quá trình phân tích dữ liệu tương tác.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-12"></span>
### Bài 12: Xác thực số có phân cách hàng nghìn và ký hiệu khoa học số mũ

::: exercise
Trong việc xử lý dữ liệu tài chính kế toán và dữ liệu đo đạc khoa học kỹ thuật, các con số thường được trình bày kèm dấu phân cách hàng nghìn bằng dấu phẩy (như `123,340.00`) hoặc viết dưới dạng ký hiệu khoa học với số mũ (như `1.9e10`, `+1E-3`).

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Xây dựng biểu thức chính quy toàn diện kết hợp dấu tùy chọn, cấu trúc phân cách hàng nghìn chuẩn 3 chữ số, phần thập phân tùy chọn và phần số mũ khoa học tùy chọn.
- Đầu ra: Trả về `True` nếu chuỗi biểu diễn đúng cấu trúc số hợp lệ, ngược lại trả về `False`. Đầu vào `None` trả về `False`.
- Trường hợp biên: Nếu dùng dấu phẩy phân cách hàng nghìn, mỗi nhóm sau dấu phẩy bắt buộc phải có đúng ba chữ số (chẳng hạn `'12,34.00'` là sai quy chuẩn). Dấu cộng hoặc trừ có thể xuất hiện ở đầu số hoặc sau ký tự e/E trong số mũ.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"[+-]?(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?"


def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["1.9e10", "123,340.00", "+1E-3", "12,34.00", "1,000e+2", "720p"]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"[+-]?(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?"`:
  - Dấu tùy chọn `[+-]?`: Chấp nhận cả dấu cộng hoặc dấu trừ ở đầu số.
  - Nhánh phân tách phần nguyên `(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)`: Nhánh thứ nhất nhận dạng có phân cách hàng nghìn, bắt đầu với 1 đến 3 chữ số, theo sau bởi một hoặc nhiều nhóm gồm dấu phẩy và đúng ba chữ số `,[0-9]{3}`. Nhánh thứ hai nhận dạng viết liền thông thường gồm các chữ số liên tiếp `[0-9]+`.
  - Phần thập phân tùy chọn `(?:\.[0-9]+)?`: Bắt buộc có chữ số sau dấu chấm nếu xuất hiện dấu chấm.
  - Phần số mũ khoa học `(?:[eE][+-]?[0-9]+)?`: Cho phép viết `e` hoặc `E`, theo sau là dấu tùy chọn và các chữ số biểu thị số mũ.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Đảm bảo toàn bộ chuỗi được kiểm soát chặt chẽ, loại bỏ hoàn toàn các lỗi sai vị trí dấu phẩy hoặc định dạng số mũ thiếu chữ số.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'1.9e10'</code> | <code>True</code> | `bool` |
| <code>'123,340.00'</code> | <code>True</code> | `bool` |
| <code>'+1E-3'</code> | <code>True</code> | `bool` |
| <code>'12,34.00'</code> | <code>False</code> | `bool` |
| <code>'1,000e+2'</code> | <code>True</code> | `bool` |
| <code>'720p'</code> | <code>False</code> | `bool` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(
    r"[+-]?(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?"
)


def solve_compiled(text):
    if text is None:
        return False
    m = COMPILED_PATTERN.fullmatch(text)
    return m is not None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["1.9e10", "123,340.00", "+1E-3", "12,34.00", "1,000e+2", "720p"]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Thực thi kiểm tra cấu trúc chuỗi đầu vào theo tiêu chuẩn số học quốc tế.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'1.9e10'</code> | <code>True</code> | `bool` |
| <code>'123,340.00'</code> | <code>True</code> | `bool` |
| <code>'+1E-3'</code> | <code>True</code> | `bool` |
| <code>'12,34.00'</code> | <code>False</code> | `bool` |
| <code>'1,000e+2'</code> | <code>True</code> | `bool` |
| <code>'720p'</code> | <code>False</code> | `bool` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Thích hợp cho các trường hợp kiểm thử nhanh một vài giá trị ngoại lai trong sổ tay dữ liệu.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-13"></span>
### Bài 13: Trích xuất mã vùng điện thoại Bắc Mỹ với hai định dạng ngoặc đơn

::: exercise
Trong việc chuẩn hóa thông tin liên lạc khách hàng từ hệ thống tổng đài Bắc Mỹ, số điện thoại có thể bắt đầu bằng mã quốc gia 1 tùy chọn, theo sau là mã vùng 3 chữ số đặt trong cặp ngoặc đơn `(416)` hoặc viết liền `416`, tiếp đến là 7 chữ số liên lạc có dấu cách hoặc gạch nối.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng hai nhánh bắt riêng biệt cho mã vùng: Một nhánh cho dạng có đủ cặp ngoặc đơn và một nhánh cho dạng không có ngoặc, bảo đảm không chấp nhận ngoặc đơn lẻ.
- Đầu ra: Trả về chuỗi `str` gồm đúng 3 chữ số của mã vùng. Nếu số điện thoại sai định dạng hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Tuyệt đối không biến từng dấu ngoặc đơn thành tùy chọn độc lập (như `\(?...\)?`), vì cách làm đó sẽ nhận nhầm các chuỗi chỉ có một ngoặc đơn lẻ như `'(416555-3456'`. Chuỗi sai quy cách số điện thoại đều phải trả về `None`.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"(?:1[ -]?)?(?:\(([0-9]{3})\)|([0-9]{3}))[ -]?[0-9]{3}[ -]?[0-9]{4}"


def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) or m.group(2) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "415-555-1234",
    "(416)555-3456",
    "202 555 4567",
    "4035555678",
    "1 416 555 9292",
    "(416555-3456",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"(?:1[ -]?)?(?:\(([0-9]{3})\)|([0-9]{3}))[ -]?[0-9]{3}[ -]?[0-9]{4}"`:
  - Mã quốc gia tùy chọn `(?:1[ -]?)?`: Nhận diện số 1 ở đầu kèm dấu cách hoặc dấu gạch nối nếu có.
  - Hai nhánh mã vùng `(?:\(([0-9]{3})\)|([0-9]{3}))`: Nhánh thứ nhất `\(([0-9]{3})\)` nhận dạng có đủ hai dấu ngoặc bao quanh và bắt 3 chữ số vào nhóm 1. Nhánh thứ hai `([0-9]{3})` nhận dạng không có ngoặc và bắt 3 chữ số vào nhóm 2. Việc tách thành hai nhánh nguyên vẹn giúp triệt tiêu hoàn toàn lỗi nhận ngoặc đơn lẻ.
  - Bảy chữ số còn lại `[ -]?[0-9]{3}[ -]?[0-9]{4}`: Nhận diện 3 chữ số đầu và 4 chữ số cuối kèm dấu phân cách tùy ý.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Biểu thức `m.group(1) or m.group(2)`: Do hai nhánh loại trừ lẫn nhau, kết quả khớp sẽ nằm ở một trong hai nhóm bắt, cho phép lấy ra giá trị chuỗi không rỗng tương ứng.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'415-555-1234'</code> | <code>'415'</code> | `str` |
| <code>'(416)555-3456'</code> | <code>'416'</code> | `str` |
| <code>'202 555 4567'</code> | <code>'202'</code> | `str` |
| <code>'4035555678'</code> | <code>'403'</code> | `str` |
| <code>'1 416 555 9292'</code> | <code>'416'</code> | `str` |
| <code>'(416555-3456'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(
    r"(?:1[ -]?)?(?:\(([0-9]{3})\)|([0-9]{3}))[ -]?[0-9]{3}[ -]?[0-9]{4}"
)


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.fullmatch(text)
    return m.group(1) or m.group(2) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "415-555-1234",
    "(416)555-3456",
    "202 555 4567",
    "4035555678",
    "1 416 555 9292",
    "(416555-3456",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Đối chiếu chuỗi điện thoại nguồn và cung cấp các nhóm bắt đã trích xuất.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'415-555-1234'</code> | <code>'415'</code> | `str` |
| <code>'(416)555-3456'</code> | <code>'416'</code> | `str` |
| <code>'202 555 4567'</code> | <code>'202'</code> | `str` |
| <code>'4035555678'</code> | <code>'403'</code> | `str` |
| <code>'1 416 555 9292'</code> | <code>'416'</code> | `str` |
| <code>'(416555-3456'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Rõ ràng, dễ hiểu khi kiểm tra một vài trường dữ liệu liên hệ riêng biệt.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-14"></span>
### Bài 14: Trích xuất tên người dùng tài khoản email trước bộ lọc cộng

::: exercise
Trong việc phân tích và chuẩn hóa danh bạ thư điện tử người dùng, nhiều dịch vụ cho phép thêm phần gắn thẻ bộ lọc bằng dấu cộng sau tên người dùng (ví dụ: `tom.riddle+regexone@hogwarts.com`). Mục tiêu là trích xuất phần tên người dùng gốc (`tom.riddle`) phục vụ việc gom cụm định danh.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng nhóm bắt để thu thập phần tên tài khoản trước dấu cộng tùy chọn và kiểm tra tính hợp lệ của miền email giản lược.
- Đầu ra: Trả về chuỗi `str` chứa tên tài khoản cơ sở. Nếu địa chỉ email không hợp lệ hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Tên tài khoản không được có hai dấu chấm liên tiếp (như `'tom..riddle@hogwarts.com'`). Phần gắn thẻ `+bo_loc` không thuộc nhóm bắt. Tên miền phải có tên miền cấp cao nhất (TLD) tối thiểu hai chữ cái.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*)(?:\+[A-Za-z0-9_]+)?@(?:[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\.)+[A-Za-z]{2,}"


def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "tom@hogwarts.com",
    "tom.riddle@hogwarts.com",
    "tom.riddle+regexone@hogwarts.com",
    "tom@hogwarts.eu.com",
    "hermione+regexone@hogwarts.com",
    "tom..riddle@hogwarts.com",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*)(?:\+[A-Za-z0-9_]+)?@(?:[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\.)+[A-Za-z]{2,}"`:
  - Nhóm bắt tên cơ sở `([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*)`: Bắt chuỗi định danh gồm các đoạn chữ, số hoặc gạch dưới. Giữa các đoạn là đúng một dấu chấm nhờ cấu trúc `(?:\.[A-Za-z0-9_]+)*`, giúp loại bỏ triệt để trường hợp hai dấu chấm kề nhau như `..`.
  - Thẻ bộ lọc tùy chọn `(?:\+[A-Za-z0-9_]+)?`: Đặt trong nhóm không bắt nằm ngoài nhóm 1, bảo đảm thẻ sau dấu cộng được kiểm tra tính hợp lệ nhưng không bị gom vào tên gốc.
  - Tên miền email `@(?:[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\.)+[A-Za-z]{2,}`: Kiểm tra tên miền phân tách bằng dấu chấm, hỗ trợ tên miền con đa cấp và đuôi tên miền quốc tế từ hai chữ cái trở lên.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Phương thức `m.group(1)`: Lấy chính xác tên tài khoản trước bộ lọc, bảo đảm tính toàn vẹn cho dữ liệu định danh khách hàng.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'tom@hogwarts.com'</code> | <code>'tom'</code> | `str` |
| <code>'tom.riddle@hogwarts.com'</code> | <code>'tom.riddle'</code> | `str` |
| <code>'tom.riddle+regexone@hogwarts.com'</code> | <code>'tom.riddle'</code> | `str` |
| <code>'tom@hogwarts.eu.com'</code> | <code>'tom'</code> | `str` |
| <code>'hermione+regexone@hogwarts.com'</code> | <code>'hermione'</code> | `str` |
| <code>'tom..riddle@hogwarts.com'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(
    r"([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*)(?:\+[A-Za-z0-9_]+)?@(?:[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\.)+[A-Za-z]{2,}"
)


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.fullmatch(text)
    return m.group(1) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "tom@hogwarts.com",
    "tom.riddle@hogwarts.com",
    "tom.riddle+regexone@hogwarts.com",
    "tom@hogwarts.eu.com",
    "hermione+regexone@hogwarts.com",
    "tom..riddle@hogwarts.com",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét và trích xuất nhóm bắt số 1 an toàn trên toàn bộ chuỗi ký tự.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'tom@hogwarts.com'</code> | <code>'tom'</code> | `str` |
| <code>'tom.riddle@hogwarts.com'</code> | <code>'tom.riddle'</code> | `str` |
| <code>'tom.riddle+regexone@hogwarts.com'</code> | <code>'tom.riddle'</code> | `str` |
| <code>'tom@hogwarts.eu.com'</code> | <code>'tom'</code> | `str` |
| <code>'hermione+regexone@hogwarts.com'</code> | <code>'hermione'</code> | `str` |
| <code>'tom..riddle@hogwarts.com'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Rất phù hợp khi phân tích dữ liệu dạng ad-hoc trên các tập dữ liệu nhỏ.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-15"></span>
### Bài 15: Trích xuất tên thẻ mở HTML đầu tiên và bỏ qua đoạn chú thích

::: exercise
Trong việc bóc tách nội dung thô từ các trang web hoặc tài liệu đánh dấu bán cấu trúc, hệ thống cần trích xuất tên của thẻ mở HTML đầu tiên (như `a`, `div`, `span`). Trước khi tìm thẻ, quy trình kỹ thuật bắt buộc phải loại bỏ các đoạn chú thích `<!-- ... -->` để không nhận nhầm thẻ giả nằm trong phần ghi chú.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Phân tách và bỏ qua các đoạn chú thích HTML đã đóng, sau đó dùng biểu thức chính quy trích xuất tên thẻ mở đầu tiên bắt đầu bằng chữ cái.
- Đầu ra: Trả về chuỗi `str` chứa tên thẻ mở đầu tiên. Nếu không tìm thấy thẻ hợp lệ hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Thẻ đóng như `'</div>'` bị bỏ qua vì mẫu yêu cầu tên thẻ phải đứng ngay sau dấu `<`. Thẻ tự đóng như `'<br/>'` hoặc thẻ có thuộc tính như `"<a href='...'>"` đều được xử lý chính xác.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"<([A-Za-z][A-Za-z0-9-]*)(?:\s+[^<>]*?)?\s*/?>"


def solve(text):
    if text is None:
        return None
    for i, part in enumerate(text.split("<!--")):
        if i:
            _, closed, part = part.partition("-->")
            if not closed:
                return None
        m = re.search(PATTERN, part, flags=0)
        if m is not None:
            return m.group(1)
    return None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "<a>Liên kết</a>",
    "<a href='https://regexone.com'>Mở</a>",
    "<div class='test_style'>Nội dung</div>",
    "<div>Chào <span>lớp</span></div>",
    "</div>",
    "văn bản thuần",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"<([A-Za-z][A-Za-z0-9-]*)(?:\s+[^<>]*?)?\s*/?>"`:
  - Dấu mở và tên thẻ `<([A-Za-z][A-Za-z0-9-]*)`: Dấu mở `<` đứng liền trước tên thẻ. Tên thẻ bắt buộc bắt đầu bằng một chữ cái `[A-Za-z]` và có thể chứa chữ số hoặc gạch nối `[A-Za-z0-9-]`. Việc không cho phép dấu gạch chéo `/` ngay sau `<` giúp mẫu tự động loại bỏ các thẻ đóng `</...>` một cách tự nhiên.
  - Thuộc tính tùy chọn `(?:\s+[^<>]*?)?`: Chấp nhận các thuộc tính như `href`, `class` nằm giữa khoảng trắng và dấu đóng thẻ.
  - Dấu đóng thẻ `\s*/?>`: Chấp nhận cả thẻ mở thông thường `>` và thẻ tự đóng `/>`.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Phép phân tách chú thích `.split('<!--')` và `.partition('-->')`: Đảm bảo toàn bộ nội dung nằm trong chú thích HTML được loại bỏ hoàn toàn trước khi áp dụng biểu thức chính quy. Nếu có chú thích mở mà không đóng, hàm trả về `None` an toàn.
  - Hàm `re.search(PATTERN, part, flags=0)`: Tìm thẻ mở đầu tiên xuất hiện trong các phần văn bản thực tế ngoài chú thích.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'&lt;a&gt;Liên kết&lt;/a&gt;'</code> | <code>'a'</code> | `str` |
| <code>"&lt;a href='https://regexone.com'&gt;Mở&lt;/a&gt;"</code> | <code>'a'</code> | `str` |
| <code>"&lt;div class='test_style'&gt;Nội dung&lt;/div&gt;"</code> | <code>'div'</code> | `str` |
| <code>'&lt;div&gt;Chào &lt;span&gt;lớp&lt;/span&gt;&lt;/div&gt;'</code> | <code>'div'</code> | `str` |
| <code>'&lt;/div&gt;'</code> | <code>None</code> | `NoneType` |
| <code>'văn bản thuần'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"<([A-Za-z][A-Za-z0-9-]*)(?:\s+[^<>]*?)?\s*/?>")


def solve_compiled(text):
    if text is None:
        return None
    for i, part in enumerate(text.split("<!--")):
        if i:
            _, closed, part = part.partition("-->")
            if not closed:
                return None
        m = COMPILED_PATTERN.search(part)
        if m is not None:
            return m.group(1)
    return None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "<a>Liên kết</a>",
    "<a href='https://regexone.com'>Mở</a>",
    "<div class='test_style'>Nội dung</div>",
    "<div>Chào <span>lớp</span></div>",
    "</div>",
    "văn bản thuần",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.search(part)`: Thực hiện quét từng đoạn phân tách của văn bản một cách trực tiếp.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'&lt;a&gt;Liên kết&lt;/a&gt;'</code> | <code>'a'</code> | `str` |
| <code>"&lt;a href='https://regexone.com'&gt;Mở&lt;/a&gt;"</code> | <code>'a'</code> | `str` |
| <code>"&lt;div class='test_style'&gt;Nội dung&lt;/div&gt;"</code> | <code>'div'</code> | `str` |
| <code>'&lt;div&gt;Chào &lt;span&gt;lớp&lt;/span&gt;&lt;/div&gt;'</code> | <code>'div'</code> | `str` |
| <code>'&lt;/div&gt;'</code> | <code>None</code> | `NoneType` |
| <code>'văn bản thuần'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.search`: Dễ dàng lồng ghép trong các hàm tiện ích nhỏ xử lý văn bản tạm thời.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-16"></span>
### Bài 16: Lọc tệp hình ảnh hợp lệ và trích xuất cặp tên tệp cùng phần mở rộng

::: exercise
Trong việc quản lý kho tệp đa phương tiện của hệ thống chỗ ở, các tệp ảnh hợp lệ bắt buộc có phần mở rộng thuộc một trong ba định dạng hình ảnh chuẩn: `jpg`, `png` hoặc `gif`. Mục tiêu là tách riêng phần tên tệp cơ sở và phần mở rộng thành một cặp giá trị tuple phục vụ việc lập chỉ mục tệp.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng hai nhóm bắt độc lập: Nhóm thứ nhất bắt phần tên tệp (có thể chứa dấu chấm hoặc gạch nối ở giữa các phân đoạn) và nhóm thứ hai bắt đúng phần mở rộng ảnh cho phép.
- Đầu ra: Trả về bộ giá trị tuple dạng `(ten_tep, phan_mo_rong)` nếu chuỗi là tệp ảnh hợp lệ. Nếu không hợp lệ hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Tên tệp không được bắt đầu hoặc kết thúc bằng dấu chấm (loại bỏ tệp ẩn như `'.bash_profile'`). Các tệp văn bản khác (như `'workspace.doc'`) hoặc tệp có đuôi tạm (như `'img0912.jpg.tmp'`) đều bị từ chối.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"([A-Za-z0-9_]+(?:[.-][A-Za-z0-9_]+)*)\.(jpg|png|gif)"


def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.groups() if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "img0912.jpg",
    "updated_img0912.png",
    "favicon.gif",
    ".bash_profile",
    "workspace.doc",
    "img0912.jpg.tmp",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"([A-Za-z0-9_]+(?:[.-][A-Za-z0-9_]+)*)\.(jpg|png|gif)"`:
  - Nhóm bắt tên tệp `([A-Za-z0-9_]+(?:[.-][A-Za-z0-9_]+)*)`: Nhóm bắt số 1 nhận các đoạn ký tự chữ, số hoặc gạch dưới. Giữa các đoạn có thể chứa dấu chấm hoặc gạch nối nhờ cấu trúc `(?:[.-][A-Za-z0-9_]+)*`. Điều này cho phép các tên tệp phức hợp như `anh-phong.01` nhưng không cho phép dấu chấm ở đầu hoặc cuối tên tệp.
  - Thoát dấu chấm `\.`: Ranh giới phân cách giữa tên tệp và phần mở rộng.
  - Nhóm bắt phần mở rộng `(jpg|png|gif)`: Nhóm bắt số 2 quy định chỉ chấp nhận đúng ba định dạng ảnh được phép viết thường.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.fullmatch(PATTERN, text, flags=0)`: Đảm bảo phần mở rộng nằm ở cuối chuỗi, loại trừ tệp có thêm đuôi phụ như `.tmp`.
  - Phương thức `m.groups()`: Trả về một bộ tuple chứa đầy đủ các nhóm bắt `(nhóm_1, nhóm_2)`, khớp chính xác với kiểu dữ liệu mong đợi của đề bài.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'img0912.jpg'</code> | <code>('img0912', 'jpg')</code> | `tuple` |
| <code>'updated_img0912.png'</code> | <code>('updated_img0912', 'png')</code> | `tuple` |
| <code>'favicon.gif'</code> | <code>('favicon', 'gif')</code> | `tuple` |
| <code>'.bash_profile'</code> | <code>None</code> | `NoneType` |
| <code>'workspace.doc'</code> | <code>None</code> | `NoneType` |
| <code>'img0912.jpg.tmp'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"([A-Za-z0-9_]+(?:[.-][A-Za-z0-9_]+)*)\.(jpg|png|gif)")


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.fullmatch(text)
    return m.groups() if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "img0912.jpg",
    "updated_img0912.png",
    "favicon.gif",
    ".bash_profile",
    "workspace.doc",
    "img0912.jpg.tmp",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét trọn vẹn chuỗi và cung cấp ngay tuple `(m.group(1), m.group(2))` qua phương thức `.groups()`.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'img0912.jpg'</code> | <code>('img0912', 'jpg')</code> | `tuple` |
| <code>'updated_img0912.png'</code> | <code>('updated_img0912', 'png')</code> | `tuple` |
| <code>'favicon.gif'</code> | <code>('favicon', 'gif')</code> | `tuple` |
| <code>'.bash_profile'</code> | <code>None</code> | `NoneType` |
| <code>'workspace.doc'</code> | <code>None</code> | `NoneType` |
| <code>'img0912.jpg.tmp'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Trực quan và dễ dùng cho các hàm lọc tệp trong tập lệnh bảo trì hệ thống.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-17"></span>
### Bài 17: Khắc phục tính tham lam trong biểu thức cắt tỉa khoảng trắng hai đầu

::: exercise
Trong việc chuẩn hóa các chuỗi văn bản tự do, yêu cầu kỹ thuật là loại bỏ các ký tự dấu cách và ký tự tab ở hai đầu chuỗi, đồng thời bảo toàn nguyên vẹn các khoảng trắng nằm giữa các từ cũng như các ký tự trắng đặc biệt khác. Cần dùng biểu thức chính quy phi tham lam để nhóm trung tâm không nuốt mất khoảng trắng cần cắt ở đuôi.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng lớp ký tự `[ \t]*` ở hai đầu và nhóm bắt không tham lam `(.*?)` ở giữa để lấy nội dung bên trong.
- Đầu ra: Trả về chuỗi `str` đã được cắt tỉa khoảng trắng hai đầu. Nếu chuỗi ban đầu chỉ gồm toàn dấu cách và tab, trả về chuỗi rỗng `''`. Nếu đầu vào là `None`, trả về `None`.
- Trường hợp biên: Chỉ cắt dấu cách và ký tự tab `\t`, không dùng `\s` để tránh xóa các ký tự đặc biệt khác theo yêu cầu riêng của đề bài. Nhóm bắt phải dùng phép lặp lười (lazy) để nhường các khoảng trắng ở cuối cho lớp `[ \t]*` phía sau.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"[ \t]*(.*?)[ \t]*"


def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return (m.group(1) or "") if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["  Chào lớp  ", "\tPhân tích dữ liệu\t", "  A  B  ", "   ", "", None]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"[ \t]*(.*?)[ \t]*"`:
  - Khối cắt đầu `[ \t]*`: Nhận diện và tiêu thụ toàn bộ các ký tự dấu cách và tab xuất hiện liên tiếp ở đầu chuỗi.
  - Nhóm bắt phi tham lam `(.*?)`: Dấu hỏi sau dấu sao chuyển chế độ lặp từ tham lam (greedy) sang lười (lazy/non-greedy). Nhóm này sẽ chỉ nhận số lượng ký tự tối thiểu cần thiết để phần còn lại của chuỗi có thể khớp với khối cắt đuôi. Nếu dùng `(.*)` tham lam, nhóm giữa sẽ nuốt luôn các dấu cách ở cuối chuỗi.
  - Khối cắt đuôi `[ \t]*`: Tiêu thụ toàn bộ dấu cách và tab còn lại ở cuối chuỗi.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Biểu thức `(m.group(1) or "")`: Đảm bảo khi chuỗi ban đầu rỗng hoặc chỉ toàn khoảng trắng, kết quả trả về là chuỗi rỗng `""` thay vì giá trị `None`.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'  Chào lớp  '</code> | <code>'Chào lớp'</code> | `str` |
| <code>'\tPhân tích dữ liệu\t'</code> | <code>'Phân tích dữ liệu'</code> | `str` |
| <code>'  A  B  '</code> | <code>'A  B'</code> | `str` |
| <code>'   '</code> | <code>''</code> | `str` |
| <code>''</code> | <code>''</code> | `str` |
| <code>None</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(r"[ \t]*(.*?)[ \t]*")


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.fullmatch(text)
    return (m.group(1) or "") if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = ["  Chào lớp  ", "\tPhân tích dữ liệu\t", "  A  B  ", "   ", "", None]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét chuỗi và cung cấp nhóm trích xuất nội dung đã cắt tỉa.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'  Chào lớp  '</code> | <code>'Chào lớp'</code> | `str` |
| <code>'\tPhân tích dữ liệu\t'</code> | <code>'Phân tích dữ liệu'</code> | `str` |
| <code>'  A  B  '</code> | <code>'A  B'</code> | `str` |
| <code>'   '</code> | <code>''</code> | `str` |
| <code>''</code> | <code>''</code> | `str` |
| <code>None</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Thuận tiện cho các thao tác làm sạch dữ liệu nhanh trong sổ tay thực hành.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-18"></span>
### Bài 18: Phân tích dòng vết ngăn xếp lỗi để trích xuất hàm, tệp nguồn và số dòng

::: exercise
Trong việc giám sát vận hành và tự động hóa xử lý sự cố từ nhật ký hệ thống Android/Java, các dòng vết ngăn xếp lỗi (stack trace) chứa thông tin vị trí phát sinh lỗi dạng: `at package.Class.method(FileName.java:123)`. Mục tiêu là trích xuất phương thức gọi, tên tệp Java và chuyển số dòng thành số nguyên `int`.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng biểu thức chính quy với ranh giới từ `\b`, các nhóm không bắt cho đường dẫn gói lớp và ba nhóm bắt độc lập cho phương thức, tệp nguồn và số dòng.
- Đầu ra: Trả về bộ giá trị tuple dạng `(ten_phuong_thuc, ten_tep_java, so_dong)` trong đó `so_dong` thuộc kiểu số nguyên `int`. Nếu dòng không phải vết ngăn xếp lỗi hợp lệ hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Các dòng thông báo không chứa vị trí dòng lỗi (như thông báo ngoại lệ chung) hoặc dòng có số dòng không phải chữ số ASCII đều bị từ chối.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"\bat\s+(?:[A-Za-z_][A-Za-z0-9_]*\.)+([A-Za-z_][A-Za-z0-9_]*)\(([A-Za-z0-9_]+\.java):([0-9]+)\)"


def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=0)
    return (m.group(1), m.group(2), int(m.group(3))) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "E/( 1553): at widget.List.makeView(ListView.java:1727)",
    "E/( 1553): at widget.List.fillDown(ListView.java:652)",
    "E/( 1553): at widget.List.fillFrom(ListView.java:709)",
    "W/dalvikvm: uncaught exception",
    "E/: FATAL EXCEPTION: main",
    "at widget.List.run(ListView.java:abc)",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"\bat\s+(?:[A-Za-z_][A-Za-z0-9_]*\.)+([A-Za-z_][A-Za-z0-9_]*)\(([A-Za-z0-9_]+\.java):([0-9]+)\)"`:
  - Ranh giới từ và từ khóa `\bat\s+`: Xác định ranh giới bắt đầu dòng vết lỗi với từ khóa `at` theo sau bởi ít nhất một khoảng trắng.
  - Chuỗi gói và lớp `(?:[A-Za-z_][A-Za-z0-9_]*\.)+`: Nhóm không bắt nhận một hoặc nhiều phân đoạn tên gói hợp lệ có dấu chấm đi kèm phía sau.
  - Nhóm bắt tên phương thức `([A-Za-z_][A-Za-z0-9_]*)`: Nhóm bắt số 1 lấy tên định danh phương thức Java.
  - Nhóm bắt tệp nguồn `\(([A-Za-z0-9_]+\.java)`: Thoát dấu ngoặc mở `\(` và bắt tên tệp kết thúc bằng `.java` vào nhóm số 2.
  - Nhóm bắt số dòng `:([0-9]+)\)`: Thoát dấu hai chấm, bắt chuỗi chữ số vào nhóm số 3 và thoát dấu ngoặc đóng `\)`.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Hàm `re.search(PATTERN, text, flags=0)`: Tìm đoạn vết ngăn xếp tại bất kỳ vị trí nào trên dòng log.
  - Ép kiểu số nguyên `int(m.group(3))`: Chuyển đổi chuỗi chữ số sang số nguyên `int` theo đúng yêu cầu cấu trúc dữ liệu của bài toán.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'E/( 1553): at widget.List.makeView(ListView.java:1727)'</code> | <code>('makeView', 'ListView.java', 1727)</code> | `tuple` |
| <code>'E/( 1553): at widget.List.fillDown(ListView.java:652)'</code> | <code>('fillDown', 'ListView.java', 652)</code> | `tuple` |
| <code>'E/( 1553): at widget.List.fillFrom(ListView.java:709)'</code> | <code>('fillFrom', 'ListView.java', 709)</code> | `tuple` |
| <code>'W/dalvikvm: uncaught exception'</code> | <code>None</code> | `NoneType` |
| <code>'E/: FATAL EXCEPTION: main'</code> | <code>None</code> | `NoneType` |
| <code>'at widget.List.run(ListView.java:abc)'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(
    r"\bat\s+(?:[A-Za-z_][A-Za-z0-9_]*\.)+([A-Za-z_][A-Za-z0-9_]*)\(([A-Za-z0-9_]+\.java):([0-9]+)\)"
)


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.search(text)
    return (m.group(1), m.group(2), int(m.group(3))) if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "E/( 1553): at widget.List.makeView(ListView.java:1727)",
    "E/( 1553): at widget.List.fillDown(ListView.java:652)",
    "E/( 1553): at widget.List.fillFrom(ListView.java:709)",
    "W/dalvikvm: uncaught exception",
    "E/: FATAL EXCEPTION: main",
    "at widget.List.run(ListView.java:abc)",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.search(text)`: Quét dòng nhật ký trực tiếp và cung cấp ba nhóm bắt.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'E/( 1553): at widget.List.makeView(ListView.java:1727)'</code> | <code>('makeView', 'ListView.java', 1727)</code> | `tuple` |
| <code>'E/( 1553): at widget.List.fillDown(ListView.java:652)'</code> | <code>('fillDown', 'ListView.java', 652)</code> | `tuple` |
| <code>'E/( 1553): at widget.List.fillFrom(ListView.java:709)'</code> | <code>('fillFrom', 'ListView.java', 709)</code> | `tuple` |
| <code>'W/dalvikvm: uncaught exception'</code> | <code>None</code> | `NoneType` |
| <code>'E/: FATAL EXCEPTION: main'</code> | <code>None</code> | `NoneType` |
| <code>'at widget.List.run(ListView.java:abc)'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.search`: Thuận tiện khi viết nhanh các kịch bản đọc tệp log nhỏ phục vụ phân tích sự cố tức thời.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-19"></span>
### Bài 19: Phân tích cú pháp địa chỉ URL thành giao thức, máy chủ và cổng mạng

::: exercise
Trong việc phân tích lưu lượng mạng và nhật ký truy cập máy chủ web, mỗi địa chỉ URL hợp lệ cần được phân tách thành các thành phần cốt lõi: Giao thức mạng (scheme), tên máy chủ (host) và cổng mạng (port) nếu có chỉ định rõ ràng.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng biểu thức chính quy kiểm tra toàn chuỗi với ba nhóm bắt cho giao thức, máy chủ và cổng mạng.
- Đầu ra: Trả về bộ giá trị tuple dạng `(giao_thuc, may_chu, cong_mang)` trong đó `cong_mang` là chuỗi chữ số hoặc `None` nếu URL không ghi cổng. Nếu URL không hợp lệ hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Dấu hai chấm của cổng mạng nằm ngoài nhóm bắt số 3 nhưng nằm trong nhóm tùy chọn, bảo đảm khi không có cổng thì nhóm 3 trả về `None`. Phần đường dẫn sau máy chủ không được chứa khoảng trắng.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"([A-Za-z][A-Za-z0-9+.-]*)://([A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*)(?::([0-9]+))?(?:/[^\s]*)?"


def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.groups() if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "ftp://file_server.com:21/top_secret/a.pdf",
    "https://regexone.com/lesson/introduction#section",
    "file://localhost:4040/zip_file",
    "https://s3cur3-server.com:9999/",
    "market://search/angry%20birds",
    "https://host:abc/a",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"([A-Za-z][A-Za-z0-9+.-]*)://([A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*)(?::([0-9]+))?(?:/[^\s]*)?"`:
  - Nhóm bắt giao thức `([A-Za-z][A-Za-z0-9+.-]*)`: Nhóm bắt số 1 lấy tên giao thức mạng (như `ftp`, `https`, `file`, `git+ssh`), bắt đầu bằng chữ cái và cho phép dấu cộng, dấu chấm hoặc gạch nối.
  - Chuỗi phân cách `://`: Ranh giới cố định giữa giao thức và máy chủ.
  - Nhóm bắt máy chủ `([A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*)`: Nhóm bắt số 2 lấy tên miền hoặc địa chỉ máy chủ, hỗ trợ tên miền con đa cấp phân tách bằng dấu chấm.
  - Nhóm bắt cổng mạng tùy chọn `(?::([0-9]+))?`: Dấu hai chấm nằm ngoài nhóm bắt số 3 `([0-9]+)`. Khi URL có cổng (như `:21`), nhóm 3 nhận đúng chuỗi `'21'`. Khi URL không có cổng, nhóm 3 nhận giá trị `None`.
  - Đường dẫn tài nguyên tùy chọn `(?:/[^\s]*)?`: Cho phép có phần đường dẫn bắt đầu bằng dấu gạch chéo và không chứa khoảng trắng.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Phương thức `m.groups()`: Trả về một tuple đúng 3 phần tử tương ứng với 3 nhóm bắt `(giao_thức, máy_chủ, cổng)`.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'ftp://file_server.com:21/top_secret/a.pdf'</code> | <code>('ftp', 'file_server.com', '21')</code> | `tuple` |
| <code>'https://regexone.com/lesson/introduction#section'</code> | <code>('https', 'regexone.com', None)</code> | `tuple` |
| <code>'file://localhost:4040/zip_file'</code> | <code>('file', 'localhost', '4040')</code> | `tuple` |
| <code>'https://s3cur3-server.com:9999/'</code> | <code>('https', 's3cur3-server.com', '9999')</code> | `tuple` |
| <code>'market://search/angry%20birds'</code> | <code>('market', 'search', None)</code> | `tuple` |
| <code>'https://host:abc/a'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(
    r"([A-Za-z][A-Za-z0-9+.-]*)://([A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*)(?::([0-9]+))?(?:/[^\s]*)?"
)


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.fullmatch(text)
    return m.groups() if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "ftp://file_server.com:21/top_secret/a.pdf",
    "https://regexone.com/lesson/introduction#section",
    "file://localhost:4040/zip_file",
    "https://s3cur3-server.com:9999/",
    "market://search/angry%20birds",
    "https://host:abc/a",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét trọn vẹn chuỗi URL và trả về các thành phần đã tách nhóm.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'ftp://file_server.com:21/top_secret/a.pdf'</code> | <code>('ftp', 'file_server.com', '21')</code> | `tuple` |
| <code>'https://regexone.com/lesson/introduction#section'</code> | <code>('https', 'regexone.com', None)</code> | `tuple` |
| <code>'file://localhost:4040/zip_file'</code> | <code>('file', 'localhost', '4040')</code> | `tuple` |
| <code>'https://s3cur3-server.com:9999/'</code> | <code>('https', 's3cur3-server.com', '9999')</code> | `tuple` |
| <code>'market://search/angry%20birds'</code> | <code>('market', 'search', None)</code> | `tuple` |
| <code>'https://host:abc/a'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Phù hợp cho việc kiểm tra URL trong các hàm phân tích nhật ký độc lập.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---

<span id="data-lab-07-regex-20"></span>
### Bài 20: Trích xuất đường dẫn tài nguyên URL và loại bỏ tham số truy vấn cùng đoạn neo

::: exercise
Trong việc phân tích hành vi người dùng trên website thông qua nhật ký máy chủ web, các địa chỉ URL truy cập thường đi kèm tham số truy vấn phức tạp (sau dấu `?`) hoặc đoạn neo định vị trang (sau dấu `#`). Mục tiêu là trích xuất đúng phần đường dẫn tài nguyên nội bộ (path) và loại bỏ hoàn toàn các phần phụ phía sau.

Yêu cầu kỹ thuật:
- Đầu vào: Chuỗi văn bản `text` thuộc kiểu `str` hoặc giá trị khuyết thiếu `None`.
- Thao tác: Sử dụng biểu thức chính quy kiểm tra toàn chuỗi URL hợp lệ bắt đầu bằng `http` hoặc `https`, sử dụng nhóm bắt riêng biệt cho phần đường dẫn tài nguyên bắt đầu bằng dấu gạch chéo và dừng trước dấu hỏi hoặc dấu thăng.
- Đầu ra: Trả về chuỗi `str` chứa đường dẫn tài nguyên. Nếu URL hợp lệ nhưng không ghi đường dẫn cụ thể, mặc định trả về `'/'`. Nếu URL sai định dạng hoặc đầu vào là `None`, trả về `None`.
- Trường hợp biên: Các giao thức khác ngoài HTTP/HTTPS (như `'ftp://example.com/a'`) đều bị từ chối. Đường dẫn phải giữ nguyên các ký tự mã hóa URL (chẳng hạn `'%20'`). Chuỗi truy vấn và đoạn neo phải được phân tách bằng nhóm không bắt riêng biệt.
:::

::: solution
#### Cách 1: Người mới bắt đầu (Gọi hàm trực tiếp từ module re)

Người học gọi trực tiếp hàm xử lý từ module `re` của thư viện chuẩn Python để kiểm tra hoặc trích xuất chuỗi.

```python
import re

PATTERN = r"https?://[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*(?::[0-9]+)?(/[^?#\s]*)?(?:\?[^#\s]*)?(?:#[^\s]*)?"


def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) or "/" if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "https://example.com/data.csv?year=2026#top",
    "http://localhost:8080/a/b",
    "https://example.com",
    "https://example.com/?q=x",
    "https://example.com/angry%20birds#info",
    "ftp://example.com/a",
]
for s in mau_kiem_thu:
    print(f"solve({repr(s)}) = {repr(solve(s))}")
```

##### Giải thích chi tiết Cách 1:
- Phân tích mẫu biểu thức chính quy `r"https?://[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*(?::[0-9]+)?(/[^?#\s]*)?(?:\?[^#\s]*)?(?:#[^\s]*)?"`:
  - Giao thức `https?://`: Chỉ chấp nhận hai giao thức web tiêu chuẩn là `http` hoặc `https`.
  - Máy chủ và cổng `[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*(?::[0-9]+)?`: Kiểm tra tên máy chủ hợp lệ kèm cổng tùy chọn.
  - Nhóm bắt đường dẫn `(/[^?#\s]*)?`: Bắt đầu bằng dấu gạch chéo `/`, theo sau bởi các ký tự không phải là dấu hỏi `?`, dấu thăng `#` hay khoảng trắng. Nhờ đó, đường dẫn dừng lại chính xác trước khi bước sang phần truy vấn hoặc đoạn neo.
  - Nhóm truy vấn tùy chọn `(?:\?[^#\s]*)?`: Nhận diện chuỗi truy vấn bắt đầu bằng dấu hỏi mà không bị lẫn vào đường dẫn.
  - Nhóm đoạn neo tùy chọn `(?:#[^\s]*)?`: Nhận diện đoạn neo định vị bắt đầu bằng dấu thăng.
- Phân tích hàm và giao thức gọi lệnh regex:
  - Biểu thức `m.group(1) or "/"`: Nếu URL kết thúc ngay sau máy chủ mà không có đường dẫn (như `https://example.com`), `m.group(1)` mang giá trị `None` và toán tử `or` sẽ tự động trả về giá trị mặc định chuẩn mực là `'/'`.

##### Kết quả thực thi Cách 1:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'https://example.com/data.csv?year=2026#top'</code> | <code>'/data.csv'</code> | `str` |
| <code>'http://localhost:8080/a/b'</code> | <code>'/a/b'</code> | `str` |
| <code>'https://example.com'</code> | <code>'/'</code> | `str` |
| <code>'https://example.com/?q=x'</code> | <code>'/'</code> | `str` |
| <code>'https://example.com/angry%20birds#info'</code> | <code>'/angry%20birds'</code> | `str` |
| <code>'ftp://example.com/a'</code> | <code>None</code> | `NoneType` |

#### Cách 2: Ứng dụng thực tế (Biên dịch mẫu trước với re.compile)

Mẫu được đặt trong một đối tượng `Pattern` để dùng lại trong hàm xử lý.

```python
import re

COMPILED_PATTERN = re.compile(
    r"https?://[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*(?::[0-9]+)?(/[^?#\s]*)?(?:\?[^#\s]*)?(?:#[^\s]*)?"
)


def solve_compiled(text):
    if text is None:
        return None
    m = COMPILED_PATTERN.fullmatch(text)
    return m.group(1) or "/" if m is not None else None


# Dữ liệu kiểm thử độc lập
mau_kiem_thu = [
    "https://example.com/data.csv?year=2026#top",
    "http://localhost:8080/a/b",
    "https://example.com",
    "https://example.com/?q=x",
    "https://example.com/angry%20birds#info",
    "ftp://example.com/a",
]
for s in mau_kiem_thu:
    print(f"solve_compiled({repr(s)}) = {repr(solve_compiled(s))}")
```

##### Giải thích chi tiết Cách 2:
- `re.compile` trả về đối tượng `Pattern` chứa mẫu và các cờ đã chọn. Gọi phương thức trên đối tượng này để giữ cùng quy tắc cho mọi chuỗi.
- Phương thức `COMPILED_PATTERN.fullmatch(text)`: Quét toàn bộ chuỗi URL và bóc tách nhóm bắt số 1 một cách tin cậy.

##### Kết quả thực thi Cách 2:


| Đầu vào | Kết quả trả về | Kiểu kết quả |
| --- | --- | --- |
| <code>'https://example.com/data.csv?year=2026#top'</code> | <code>'/data.csv'</code> | `str` |
| <code>'http://localhost:8080/a/b'</code> | <code>'/a/b'</code> | `str` |
| <code>'https://example.com'</code> | <code>'/'</code> | `str` |
| <code>'https://example.com/?q=x'</code> | <code>'/'</code> | `str` |
| <code>'https://example.com/angry%20birds#info'</code> | <code>'/angry%20birds'</code> | `str` |
| <code>'ftp://example.com/a'</code> | <code>None</code> | `NoneType` |

#### So sánh hai phương pháp:
- Gọi trực tiếp `re.fullmatch`: Rất phù hợp cho các bài phân tích tương tác trên tập dữ liệu web quy mô nhỏ.
- Biên dịch mẫu với `re.compile`: Dùng khi cần đặt tên cho quy tắc và dùng chung mẫu trong nhiều lần gọi. Hãy đo trên dữ liệu thực tế nếu cần so sánh tốc độ.
:::

---