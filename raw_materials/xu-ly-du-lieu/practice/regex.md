## Thực hành biểu thức chính quy

Mỗi bài nhận đầu vào là `str` hoặc `None`. Các chữ số trong mẫu phải thuộc ASCII, trừ phần ký tự trắng được nêu riêng. Không tự xóa khoảng trắng hay đổi hoa thường trước khi kiểm tra. Hãy giữ đúng kiểu kết quả và thử lời giải trên các trường hợp biên.

Các bài sử dụng miền đầu vào giản lược của từng đề. Không dùng lookaround hoặc tham chiếu ngược. Với HTML, email hay URL ngoài miền đó, cần dùng bộ phân tích phù hợp.

### Regex 1. Trích dãy chữ số đầu tiên

::: exercise Regex 1
Một cột mô tả có thể chứa mã số ở bất kỳ vị trí nào. Viết hàm `solve(text)` trả về dãy chữ số ASCII liên tiếp đầu tiên, giữ kiểu chuỗi và các số 0 ở đầu. Nếu đầu vào là `None` hoặc không có chữ số ASCII, trả `None`. Không chuyển kết quả sang số nguyên..
:::

::: solution
```python
import re
PATTERN = r"[0-9]+"

def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=0)
    return m.group(0) if m is not None else None
```

[0-9] chỉ nhận chữ số ASCII, còn dấu + lấy trọn dãy liên tiếp. re.search dừng ở lần khớp đầu tiên. Giữ kết quả dạng chuỗi để mã 007 không mất hai số 0 ở đầu.
:::

### Regex 2. Dấu chấm thường và ký tự đại diện

::: exercise Regex 2
Viết hàm kiểm tra toàn chuỗi gồm đúng ba ký tự bất kỳ, tiếp theo là một dấu chấm thường. Ba ký tự đầu có thể là chữ, số, khoảng trắng hoặc dấu câu, nhưng không có ký tự xuống dòng `\n`. Phân biệt hoa thường, không dùng cờ DOTALL. Đầu vào `None` trả `False`..
:::

::: solution
```python
import re
PATTERN = r"...\."

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

Ba dấu chấm đầu là ký tự đại diện, mỗi dấu nhận một ký tự khác xuống dòng. Dấu chấm cuối được escape để chỉ nhận đúng ký tự chấm. re.fullmatch buộc cả độ dài lẫn ký tự cuối đều thỏa yêu cầu.
:::

### Regex 3. Chọn ký tự trong một tập

::: exercise Regex 3
Viết hàm kiểm tra toàn chuỗi gồm một ký tự thuộc tập `c`, `m`, `f`, tiếp theo là `an`. Phân biệt hoa thường. Khoảng trắng đầu hoặc cuối làm chuỗi không hợp lệ. `None` trả `False`. Dùng lớp ký tự trong regex.
:::

::: solution
```python
import re
PATTERN = r"[cmf]an"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

Nhóm [cmf] chọn đúng một trong ba chữ c, m, f. Hai chữ an ở sau phải xuất hiện nguyên vẹn. Một dấu chấm đại diện sẽ nhận cả những chữ đầu ngoài tập được phép.
:::

### Regex 4. Kết hợp các khoảng ký tự

::: exercise Regex 4
Mã hợp lệ có đúng ba ký tự: Ký tự đầu là chữ hoa từ `A` đến `C`, ký tự thứ hai là chữ thường từ `n` đến `p`, ký tự cuối là chữ thường từ `a` đến `c`. Viết hàm kiểm tra toàn chuỗi bằng các khoảng ký tự, phân biệt hoa thường. `None` trả `False`..
:::

::: solution
```python
import re
PATTERN = r"[A-C][n-p][a-c]"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

Mỗi cặp ngoặc vuông quy định một vị trí và bao gồm cả hai đầu khoảng. Chẳng hạn Cpc hợp lệ vì C, p và c đều ở cận trên tương ứng. Không có phép lặp nên chuỗi phải có đúng ba ký tự.
:::

### Regex 5. Giới hạn số lần lặp

::: exercise Regex 5
Chuỗi hợp lệ bắt đầu bằng `wa`, có từ ba đến năm ký tự `z`, rồi kết thúc bằng `up`. Viết hàm kiểm tra toàn chuỗi, phân biệt hoa thường. `None` trả `False`..
:::

::: solution
```python
import re
PATTERN = r"waz{3,5}up"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

Ký hiệu {3,5} chỉ tác động lên chữ z đứng ngay trước nó. Vì vậy phải có ít nhất ba và nhiều nhất năm chữ z giữa wa và up. re.fullmatch loại chuỗi có thêm ký tự ở hai đầu.
:::

### Regex 6. Phân biệt không lần và ít nhất một lần

::: exercise Regex 6
Chuỗi hợp lệ có ít nhất hai chữ `a`, sau đó có thể có bất kỳ số chữ `b` nào kể cả không có, cuối cùng có ít nhất một chữ `c`. Không đặt cận trên cho các nhóm này. Viết hàm kiểm tra toàn chuỗi, phân biệt hoa thường. `None` trả `False`..
:::

::: solution
```python
import re
PATTERN = r"a{2,}b*c+"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

a{2,} đặt cận dưới là hai mà không đặt cận trên. b* cho phép cả trường hợp không có b, còn c+ bắt buộc ít nhất một c. Ba nhóm phải xuất hiện theo đúng thứ tự trong mẫu.
:::

### Regex 7. Ký tự tùy chọn và dấu hỏi thường

::: exercise Regex 7
Thông báo hợp lệ gồm số nguyên dương ASCII không có số 0 đầu, một dấu cách, từ `file` hoặc `files`, một dấu cách, rồi đúng chuỗi `found?`. Hai dạng từ file/files đều được chấp nhận với mọi số nguyên dương trong bài này. Viết hàm kiểm tra toàn chuỗi, phân biệt hoa thường. `None` trả `False`..
:::

::: solution
```python
import re
PATTERN = r"[1-9][0-9]* files? found\?"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

Chữ số đầu thuộc [1-9] nên không nhận 0 hay số có 0 đứng đầu. Dấu hỏi sau s làm riêng chữ s thành tùy chọn. Dấu hỏi cuối được escape vì nó là dấu câu phải có trong thông báo.
:::

### Regex 8. Yêu cầu có ký tự trắng phân cách

::: exercise Regex 8
Mục danh sách hợp lệ gồm một hoặc nhiều chữ số ASCII, dấu chấm thường, ít nhất một ký tự trắng, rồi đúng từ `abc`. Ký tự trắng được hiểu theo `\s` của Python, bao gồm dấu cách, tab, xuống dòng, carriage return và khoảng trắng Unicode. Viết hàm kiểm tra toàn chuỗi, phân biệt hoa thường. `None` trả `False`..
:::

::: solution
```python
import re
PATTERN = r"[0-9]+\.\s+abc"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

Dấu chấm được escape, còn \s+ yêu cầu ít nhất một ký tự trắng. Thay dấu + bằng * sẽ nhận cả chuỗi 1.abc, trái với yêu cầu có phân cách. Ở bài này, ký tự trắng tuân theo nghĩa Unicode của Python.
:::

### Regex 9. Trích tên tệp PDF bằng nhóm bắt

::: exercise Regex 9
Chỉ xử lý tên tệp, không có đường dẫn. Tệp hợp lệ có phần tên bắt đầu bằng `file`, tiếp theo ít nhất một ký tự ASCII thuộc chữ, số hoặc `_`, rồi phần mở rộng đúng `.pdf` chữ thường. Viết hàm trả phần tên trước `.pdf`. Đầu vào thiếu hoặc tên không hợp lệ trả `None`..
:::

::: solution
```python
import re
PATTERN = r"(file[A-Za-z0-9_]+)\.pdf"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) if m is not None else None
```

Nhóm bắt chỉ bao lấy phần tên để group(1) trả tên mà không kèm .pdf. Dấu + yêu cầu còn ít nhất một ký tự sau file. Kiểm tra toàn chuỗi loại cả đường dẫn lẫn hậu tố tạm như .pdf.tmp.
:::

### Regex 10. Trích số phòng với phép hoặc và ranh giới từ

::: exercise Regex 10
Tên chỗ ở có thể ghi số phòng bằng `BR`, `bedroom` hoặc `bedrooms`, không phân biệt hoa thường. Trong dữ liệu bài này, số lượng chỉ là số nguyên ASCII không dấu. Không có số âm hoặc thập phân. Trích số ở cụm hợp lệ đầu tiên, cho phép không có khoảng trắng giữa số và từ chỉ phòng, và phải có ranh giới từ ở hai đầu cụm. `None` hoặc không khớp trả `None`. Kết quả vẫn là chuỗi..
:::

::: solution
```python
import re
PATTERN = r"\b([0-9]+)\s*(?:BR|bedrooms?)\b"

def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=re.I)
    return m.group(1) if m is not None else None
```

Nhóm bắt giữ số phòng, còn nhóm không bắt liệt kê hai cách viết đơn vị. Cờ re.I cho phép khác biệt hoa thường. Ranh giới từ ở cuối loại 12bravo và 2BR2BA vì từ chỉ phòng vẫn dính với phần chữ hoặc số phía sau.
:::

### Regex 11. Kiểm tra số nguyên và số thập phân đơn giản

::: exercise Regex 11
Cột số ở dạng chuỗi chỉ chấp nhận số nguyên hoặc thập phân dùng dấu chấm, có thể có dấu trừ ở đầu. Phần nguyên bắt buộc có ít nhất một chữ số ASCII. Nếu có dấu chấm thì phải có chữ số sau dấu chấm. Cho phép số 0 đầu. Không nhận dấu cộng, phân cách hàng nghìn, số mũ hay khoảng trắng. Viết hàm kiểm tra toàn chuỗi. `None` trả `False`..
:::

::: solution
```python
import re
PATTERN = r"-?[0-9]+(?:\.[0-9]+)?"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

Phần nguyên luôn phải có chữ số. Toàn bộ phần dấu chấm và chữ số sau nó được đặt trong một nhóm tùy chọn, vì vậy 12. bị loại. re.fullmatch cũng loại hậu tố và ký tự xuống dòng ở cuối.
:::

### Regex 12. Kiểm tra số có phân cách hàng nghìn và số mũ

::: exercise Regex 12
Viết hàm kiểm tra toàn chuỗi số theo quy tắc: Dấu `+`/`-` đầu chuỗi tùy chọn. Phần nguyên là các chữ số ASCII không có dấu phẩy, hoặc một nhóm 1–3 chữ số rồi ít nhất một nhóm `,` và đúng ba chữ số. Phần thập phân tùy chọn dùng dấu chấm và ít nhất một chữ số. Số mũ tùy chọn gồm `e`/`E`, dấu tùy chọn và ít nhất một chữ số. Cho phép số 0 đầu, không có khoảng trắng. `None` trả `False`..
:::

::: solution
```python
import re
PATTERN = r"[+-]?(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None
```

Phần nguyên chọn giữa dạng có phân nhóm hàng nghìn và dạng chỉ gồm chữ số. Ở dạng có dấu phẩy, mỗi nhóm sau dấu phẩy phải có đúng ba chữ số nên 12,34.00 không hợp lệ. Phần thập phân và số mũ được kiểm tra riêng, mỗi phần đều phải có chữ số nếu dấu mở đầu của nó xuất hiện.
:::

### Regex 13. Trích mã vùng điện thoại

::: exercise Regex 13
Số điện thoại của bài dùng dạng Bắc Mỹ: Mã quốc gia `1` tùy chọn, mã vùng đúng ba chữ số ASCII, cụm ba chữ số và cụm bốn chữ số. Mã vùng có thể được bọc trong một cặp ngoặc tròn đầy đủ. Giữa các phần cho phép vắng dấu phân cách hoặc có đúng một dấu cách hay dấu gạch ngang. Không có khoảng trắng ngoài chuỗi. Trả mã vùng dưới dạng chuỗi nếu toàn số hợp lệ. Ngược lại trả `None`..
:::

::: solution
```python
import re
PATTERN = r"(?:1[ -]?)?(?:\(([0-9]{3})\)|([0-9]{3}))[ -]?[0-9]{3}[ -]?[0-9]{4}"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) or m.group(2) if m is not None else None
```

Hai nhánh của mã vùng lần lượt nhận dạng có đủ cặp ngoặc hoặc không có ngoặc. Không đặt từng dấu ngoặc thành tùy chọn độc lập, vì cách đó sẽ nhận cả ngoặc đơn lẻ. Kết quả nằm ở một trong hai nhóm bắt nên lấy nhóm không rỗng.
:::

### Regex 14. Trích tên tài khoản email trước bộ lọc

::: exercise Regex 14
Email trong bài có tên gốc gồm các nhóm chữ/số/`_` ASCII ngăn bằng dấu chấm. Mỗi nhóm có ít nhất một ký tự. Sau tên gốc có thể có một bộ lọc `+` và ít nhất một chữ/số/`_`. Miền gồm ít nhất hai nhãn phân cách bằng dấu chấm. Nhãn trước nhãn cuối gồm nhóm chữ/số ngăn bằng dấu `-`, nhãn cuối chỉ có ít nhất hai chữ cái ASCII. Chỉ trả tên tài khoản gốc. Bỏ phần bộ lọc từ dấu `+` và phần miền từ dấu `@` khỏi kết quả. Email sai hoặc `None` trả `None`..
:::

::: solution
```python
import re
PATTERN = r"([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*)(?:\+[A-Za-z0-9_]+)?@(?:[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\.)+[A-Za-z]{2,}"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) if m is not None else None
```

Tên gốc gồm các nhóm không rỗng, giữa hai nhóm là một dấu chấm nên không nhận dấu chấm liên tiếp. Phần +bộ_lọc không thuộc nhóm bắt đầu tiên. Mẫu chỉ xác nhận miền email giản lược của đề, không xác minh hộp thư có tồn tại.
:::

### Regex 15. Trích tên thẻ mở đầu tiên

::: exercise Regex 15
Đoạn HTML của bài đã được bảo đảm là dữ liệu đơn giản trên một dòng: Tên thẻ mở bắt đầu bằng chữ ASCII, phần sau gồm chữ/số/`-`. Phần thuộc tính nếu có được ngăn với tên thẻ bằng ký tự trắng và không chứa `<` hay `>`. Chú thích có đủ dấu `<!--`/`-->`, không lồng nhau và có thể chứa chuỗi giống thẻ HTML. Trích tên thẻ mở đầu tiên nằm ngoài chú thích, giữ nguyên hoa thường. Thẻ tự đóng như `<br/>` cũng được tính. Bỏ qua thẻ đóng và toàn bộ nội dung chú thích. Chuỗi không có thẻ mở hoặc `None` trả `None`.. Không cần kiểm tính hợp lệ của tài liệu HTML hay thuộc tính.
:::

::: solution
```python
import re
PATTERN = r"<([A-Za-z][A-Za-z0-9-]*)(?:\s+[^<>]*?)?\s*/?>"

def solve(text):
    if text is None:
        return None
    for i, part in enumerate(text.split("<!--")):
        if i:
            _, closed, part = part.partition("-->")
            if not closed: return None
        m = re.search(PATTERN, part, flags=0)
        if m is not None: return m.group(1)
    return None
```

Trước khi tìm thẻ, hàm bỏ qua từng đoạn chú thích đã có đủ dấu đóng. Mẫu sau đó chỉ nhận dấu mở theo sau bởi tên bắt đầu bằng chữ, nên không nhận thẻ đóng. Cách làm này dựa vào miền HTML giản lược của đề, không thay cho bộ phân tích HTML tổng quát.
:::

### Regex 16. Chọn tệp ảnh và trích phần mở rộng

::: exercise Regex 16
Tên tệp ảnh hợp lệ có phần tên gồm các nhóm chữ/số/`_` ASCII, ngăn bằng một dấu `.` hoặc `-`. Mỗi nhóm có ít nhất một ký tự. Phần mở rộng là đúng `jpg`, `png` hoặc `gif` chữ thường. Không có đường dẫn, dấu cách hoặc dấu chấm đầu tên. Trả bộ đôi `(tên, phần_mở_rộng)`. Tên sai hoặc `None` trả `None`..
:::

::: solution
```python
import re
PATTERN = r"([A-Za-z0-9_]+(?:[.-][A-Za-z0-9_]+)*)\.(jpg|png|gif)"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.groups() if m is not None else None
```

Nhóm đầu bắt tên với từng đoạn không rỗng, còn nhóm sau chỉ nhận một trong ba phần mở rộng. Vì dùng re.fullmatch, phần mở rộng phải ở cuối chuỗi. Mẫu giữ nguyên hoa thường của tên và chỉ nhận phần mở rộng viết thường như đề yêu cầu.
:::

### Regex 17. Sửa mẫu cắt khoảng trắng bị tham lam

::: exercise Regex 17
Một đoạn mã dùng `r"^\s*(.*)\s*$"` để bắt nội dung sau khi bỏ khoảng trắng hai đầu, nhưng nhóm `(.*)` có thể giữ cả dấu cách cuối. Hãy sửa regex và viết `solve(text)` chỉ bỏ dấu cách/tab ở hai đầu, giữ nguyên khoảng trắng bên trong. Đầu vào không chứa `\n`/`\r`. Dấu cách không ngắt dòng `\u00a0`, tab dọc `\v` và ký tự chuyển trang `\f`, nếu có, phải được giữ nguyên. Chuỗi chỉ có dấu cách/tab trả `""`, `None` vẫn trả `None`..
:::

::: solution
```python
import re
PATTERN = r"[ \t]*(.*?)[ \t]*"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return (m.group(1) or "") if m is not None else None
```

Hai đầu chỉ dùng dấu cách và tab thay vì \s để giữ lại những ký tự trắng khác mà đề yêu cầu. Nhóm giữa dùng phép lặp không tham lam để nhường dấu cách hoặc tab cuối cho nhóm ngoài. Nếu toàn chuỗi chỉ có hai loại ký tự bị cắt, nội dung còn lại là chuỗi rỗng.
:::

### Regex 18. Trích dữ liệu từ dòng ngăn xếp lỗi

::: exercise Regex 18
Một dòng log có thể chứa cụm `at package.Class.method(File.java:line)`. Tên gói/lớp/phương thức bắt đầu bằng chữ ASCII hoặc `_`, tiếp theo là chữ/số/`_`. Trước phương thức có ít nhất một thành phần và dấu chấm. Tên tệp có phần tên gồm ít nhất một chữ/số/`_`, phần mở rộng đúng `.java`. Số dòng là số nguyên ASCII không dấu. Trích cụm hợp lệ đầu tiên và trả `(phương_thức, tên_tệp, số_dòng)` với số dòng kiểu int. Không có cụm hợp lệ hoặc `None` trả `None`..
:::

::: solution
```python
import re
PATTERN = r"\bat\s+(?:[A-Za-z_][A-Za-z0-9_]*\.)+([A-Za-z_][A-Za-z0-9_]*)\(([A-Za-z0-9_]+\.java):([0-9]+)\)"

def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=0)
    return (m.group(1), m.group(2), int(m.group(3))) if m is not None else None
```

Phần trước phương thức là một hay nhiều thành phần có dấu chấm, được đặt trong nhóm không bắt. Ba nhóm bắt giữ riêng phương thức, tên tệp và số dòng. Các dấu ngoặc của dòng log phải escape để khớp ký tự thật, rồi số dòng được đổi sang int sau khi đã kiểm tra chỉ gồm chữ số ASCII.
:::

### Regex 19. Trích giao thức, máy chủ và cổng URL

::: exercise Regex 19
URL giản lược gồm giao thức bắt đầu bằng chữ ASCII rồi chữ/số/`+`/`.`/`-`. Tiếp theo là `://`. Máy chủ gồm các nhóm chữ/số/`_`/`-` ngăn bằng dấu chấm. Cổng tùy chọn gồm `:` và ít nhất một chữ số ASCII, giữ kiểu chuỗi, không kiểm miền giá trị cổng. Phần sau tùy chọn phải bắt đầu bằng `/` và không có ký tự trắng. Không xử lý tài khoản đăng nhập hay IPv6. Trả `(giao_thức, máy_chủ, cổng)`. Không ghi cổng thì trường này là `None`. URL sai hoặc `None` trả `None`..
:::

::: solution
```python
import re
PATTERN = r"([A-Za-z][A-Za-z0-9+.-]*)://([A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*)(?::([0-9]+))?(?:/[^\s]*)?"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.groups() if m is not None else None
```

Ba nhóm bắt tương ứng với giao thức, máy chủ và cổng. Dấu hai chấm nằm ngoài nhóm bắt cổng nhưng trong nhóm tùy chọn, nên cổng vắng cho kết quả None. Phần sau máy chủ phải bắt đầu bằng dấu gạch chéo và không được chứa ký tự trắng.
:::

### Regex 20. Trích đường dẫn URL, loại truy vấn và đoạn neo

::: exercise Regex 20
URL giản lược của bài chỉ có giao thức `http` hoặc `https` chữ thường. Máy chủ là các nhóm chữ/số/`_`/`-` ASCII ngăn bằng dấu chấm. Cổng nếu có là chữ số ASCII. Phần đường dẫn bắt đầu bằng `/`, kết thúc trước dấu `?` hoặc `#`, không có ký tự trắng. Sau đó có thể có truy vấn `?` và đoạn neo `#`. Trả nguyên văn đường dẫn, giữ mã hóa `%20`. Nếu không ghi đường dẫn thì trả `/`. URL sai hoặc `None` trả `None`. Không xử lý tài khoản hay IPv6..
:::

::: solution
```python
import re
PATTERN = r"https?://[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*(?::[0-9]+)?(/[^?#\s]*)?(?:\?[^#\s]*)?(?:#[^\s]*)?"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) or "/" if m is not None else None
```

Nhóm đường dẫn dừng trước dấu hỏi hoặc dấu thăng, nhờ đó không lấy lẫn truy vấn và đoạn neo. Hai phần này được kiểm tra trong các nhóm không bắt riêng. Nếu nhóm đường dẫn vắng, hàm trả / theo quy ước của đề và giữ nguyên các ký tự mã hóa trong đường dẫn đã có.
:::
