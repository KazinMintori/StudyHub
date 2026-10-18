"""IAI regex public tests, adapted under CC BY-NC-SA 4.0.
Source: https://github.com/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/lab-07-regex.ipynb
Only solution patterns and neutral explanations were added.
"""
import re
from contextlib import redirect_stdout
from io import StringIO
TOTAL = 0

# Exercise 1: Câu 1. Trích dãy chữ số đầu tiên
import re
PATTERN = r"[0-9]+"

def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=0)
    return m.group(0) if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('abc123xyz', '123'),
        ('define "123"', '123'),
        ('var g = 123;', '123'),
        ('P007 / P12', '007'),
        ('không có mã', None),
        (None, None),
        ('', None),
        ('42', '42'),
        ('mã 0', '0'),
        ('１２３', None),
        ('A8B9', '8'),
        ('١٢٣', None),
        ('A١٢B34', '34'),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Trong báo cáo nhập dữ liệu, trợ giảng ghi lại các mô tả có mã số mà nhóm đã gặp '
        'trong nhiều tệp khác nhau. Bản ghi đầu tiên là «abc123xyz»; người tiếp theo đưa vào '
        '«define "123"»; ở phần rà soát có «var g = 123;»; sau đó nhóm ghi thêm «P007 / '
        'P12»; một mục khác được lưu là «không có mã». Một ô khác bị thiếu dữ liệu và được '
        'lưu là None. Mục tiêu là nhận dãy số xuất hiện đầu tiên trong từng mô tả, giữ '
        'nguyên hình thức ban đầu để còn đối chiếu với mã gốc.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('abc123xyz', '123'),
        ('define "123"', '123'),
        ('var g = 123;', '123'),
        ('P007 / P12', '007'),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 13 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 14

# Exercise 2: Câu 2. Dấu chấm thường và ký tự đại diện
import re
PATTERN = r"...\."

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('cat.', True),
        ('896.', True),
        ('?=+.', True),
        ('abc1', False),
        ('ab.', False),
        ('abcd.', False),
        ('   .', True),
        ('...', False),
        ('....', True),
        ('ab\n.', False),
        ('cat.\n', False),
        (None, False),
        ('ab\r.', True),
        ('A🦊B.', True),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Một nhóm đang rà soát các nhãn ngắn được gửi từ biểu mẫu và cần nhận đúng kiểu nhãn '
        'có dấu chấm cuối. Bản ghi đầu tiên là «cat.»; người tiếp theo đưa vào «896.»; ở '
        'phần rà soát có «?=+.»; sau đó nhóm ghi thêm «abc1»; một mục khác được lưu là '
        '«ab.»; và mục cuối trong lượt này là «abcd.». Những nhãn nhìn gần giống nhau cũng '
        'được giữ trong bản ghi, để nhóm kiểm chứng rằng ký tự cuối và độ dài đều được xét.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('cat.', True),
        ('896.', True),
        ('?=+.', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 14 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 15

# Exercise 3: Câu 3. Chọn ký tự trong một tập
import re
PATTERN = r"[cmf]an"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('can', True),
        ('man', True),
        ('fan', True),
        ('dan', False),
        ('ran', False),
        ('pan', False),
        ('Can', False),
        (' can', False),
        ('cann', False),
        ('xcan', False),
        ('', False),
        (None, False),
        ('can\n', False),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Trong một trò chơi nhận diện từ, người quản lý gom các mục từ nhiều phiếu trả lời '
        'vào cùng một ghi chú. Bản ghi đầu tiên là «can»; người tiếp theo đưa vào «man»; ở '
        'phần rà soát có «fan»; sau đó nhóm ghi thêm «dan»; một mục khác được lưu là «ran»; '
        'và mục cuối trong lượt này là «pan». Hệ thống chỉ chọn mục đúng cấu trúc đã nêu, dù '
        'nhiều mục gây nhiễu có cùng phần kết thúc.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('can', True),
        ('man', True),
        ('fan', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 13 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 14

# Exercise 4: Câu 4. Kết hợp các khoảng ký tự
import re
PATTERN = r"[A-C][n-p][a-c]"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('Ana', True),
        ('Bob', True),
        ('Cpc', True),
        ('aax', False),
        ('bby', False),
        ('ccz', False),
        ('Apa', True),
        ('Cnc', True),
        ('Dna', False),
        ('Amc', False),
        ('Bpd', False),
        (None, False),
        ('Ana\n', False),
        ('Boc', True),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Bộ phận dữ liệu nhận một danh sách mã ba ký tự do nhiều người nhập và muốn kiểm tra '
        'từng vị trí của mã. Bản ghi đầu tiên là «Ana»; người tiếp theo đưa vào «Bob»; ở '
        'phần rà soát có «Cpc»; sau đó nhóm ghi thêm «aax»; một mục khác được lưu là «bby»; '
        'và mục cuối trong lượt này là «ccz». Người rà soát cần phân biệt chữ hoa với chữ '
        'thường và giữ lại cả các mã sai để xác nhận mẫu không chọn quá rộng.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('Ana', True),
        ('Bob', True),
        ('Cpc', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 14 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 15

# Exercise 5: Câu 5. Giới hạn số lần lặp
import re
PATTERN = r"waz{3,5}up"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('wazzzup', True),
        ('wazzzzup', True),
        ('wazzzzzup', True),
        ('wazup', False),
        ('wazzup', False),
        ('wazzzzzzup', False),
        ('wazzzup!', False),
        ('Wazzzup', False),
        ('waup', False),
        ('', False),
        (None, False),
        ('wazzzup\n', False),
        ('wazzzzzzzup', False),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Một ứng dụng thử nghiệm lưu các cách người dùng kéo dài âm trong tin nhắn để nhóm '
        'kiểm tra quy tắc số lần lặp. Bản ghi đầu tiên là «wazzzup»; người tiếp theo đưa vào '
        '«wazzzzup»; ở phần rà soát có «wazzzzzup»; sau đó nhóm ghi thêm «wazup»; một mục '
        'khác được lưu là «wazzup»; và mục cuối trong lượt này là «wazzzzzzup». Nhóm cần '
        'chọn cách viết nằm đúng trong giới hạn, thay vì nhận tất cả chuỗi có chữ z.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('wazzzup', True),
        ('wazzzzup', True),
        ('wazzzzzup', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 13 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 14

# Exercise 6: Câu 6. Phân biệt không lần và ít nhất một lần
import re
PATTERN = r"a{2,}b*c+"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('aaaabcc', True),
        ('aabbbbc', True),
        ('aacc', True),
        ('a', False),
        ('abc', False),
        ('aabb', False),
        ('aac', True),
        ('aaaaaabbbbbccccc', True),
        ('aabca', False),
        ('aa', False),
        ('', False),
        (None, False),
        ('aaaaaacccc', True),
        ('aaacbb', False),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Phòng thực hành đang thử bộ sinh chuỗi với các nhóm ký tự a, b và c, rồi ghi mọi '
        'kết quả vào một đoạn nhật ký. Bản ghi đầu tiên là «aaaabcc»; người tiếp theo đưa '
        'vào «aabbbbc»; ở phần rà soát có «aacc»; sau đó nhóm ghi thêm «a»; một mục khác '
        'được lưu là «abc»; và mục cuối trong lượt này là «aabb». Người kiểm tra chọn chuỗi '
        'có đủ các phần bắt buộc và đúng thứ tự, kể cả khi nhóm b hoàn toàn vắng mặt.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('aaaabcc', True),
        ('aabbbbc', True),
        ('aacc', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 14 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 15

# Exercise 7: Câu 7. Ký tự tùy chọn và dấu hỏi thường
import re
PATTERN = r"[1-9][0-9]* files? found\?"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('1 file found?', True),
        ('2 files found?', True),
        ('24 files found?', True),
        ('No files found.', False),
        ('0 files found?', False),
        ('2 files found.', False),
        ('2 file found?', True),
        ('01 file found?', False),
        ('1 file found', False),
        ('1  file found?', False),
        ('1 File found?', False),
        (None, False),
        ('1 files found?', True),
        ('1 file found?\n', False),
        ('１２ files found?', False),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Sau một đợt tìm kiếm tệp, nhân viên hỗ trợ chép các thông báo từ màn hình vào báo '
        'cáo bàn giao. Bản ghi đầu tiên là «1 file found?»; người tiếp theo đưa vào «2 files '
        'found?»; ở phần rà soát có «24 files found?»; sau đó nhóm ghi thêm «No files '
        'found.»; một mục khác được lưu là «0 files found?»; và mục cuối trong lượt này là '
        '«2 files found.». Các thông báo có hình thức gần nhau được giữ cạnh nhau, để phân '
        'biệt dấu hỏi thực sự với ký hiệu tùy chọn của mẫu.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('1 file found?', True),
        ('2 files found?', True),
        ('24 files found?', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 15 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 16

# Exercise 8: Câu 8. Yêu cầu có ký tự trắng phân cách
import re
PATTERN = r"[0-9]+\.\s+abc"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('1.   abc', True),
        ('2.\tabc', True),
        ('3.           abc', True),
        ('4.abc', False),
        ('12. abc', True),
        ('1x abc', False),
        ('1.\nabc', True),
        ('1.\rabc', True),
        ('1. ABC', False),
        ('1. abc ', False),
        ('', False),
        (None, False),
        ('1.\xa0abc', True),
        ('1.\x0babc', True),
        ('1.\u2003abc', True),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Người biên tập nhận các mục đánh số được sao chép từ nhiều ứng dụng, có mục dùng '
        'dấu cách và có mục dùng tab. Bản ghi đầu tiên là «1.   abc»; người tiếp theo đưa '
        'vào «2.\tabc»; ở phần rà soát có «3.           abc»; sau đó nhóm ghi thêm «4.abc»; '
        'một mục khác được lưu là «12. abc»; và mục cuối trong lượt này là «1x abc». Bản ghi '
        'giữ nguyên ký tự phân cách để kiểm tra xem mẫu có nhận đủ loại ký tự trắng và loại '
        'mục viết dính hay không.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('1.   abc', True),
        ('2.\tabc', True),
        ('3.           abc', True),
        ('12. abc', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 15 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 16

# Exercise 9: Câu 9. Trích tên tệp PDF bằng nhóm bắt
import re
PATTERN = r"(file[A-Za-z0-9_]+)\.pdf"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('file_record_transcript.pdf', 'file_record_transcript'),
        ('file_07241999.pdf', 'file_07241999'),
        ('fileA1.pdf', 'fileA1'),
        ('testfile_fake.pdf.tmp', None),
        ('fileA.pdf.tmp', None),
        ('fileA.txt', None),
        ('file.pdf', None),
        ('fileA.PDF', None),
        ('folder/fileA.pdf', None),
        ('file-A.pdf', None),
        ('', None),
        (None, None),
        ('file_.pdf', 'file_'),
        ('fileA.pdf\n', None),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Một nhóm quản lý hồ sơ đang chọn tệp PDF từ danh sách tên được chuyển sang dạng văn '
        'bản. Bản ghi đầu tiên là «file_record_transcript.pdf»; người tiếp theo đưa vào '
        '«file_07241999.pdf»; ở phần rà soát có «fileA1.pdf»; sau đó nhóm ghi thêm '
        '«testfile_fake.pdf.tmp»; một mục khác được lưu là «fileA.pdf.tmp»; và mục cuối '
        'trong lượt này là «fileA.txt». Bản ghi cũng giữ các tệp có phần mở rộng khác và các '
        'bản tạm, để người xử lý chỉ lấy đúng phần tên cần thiết.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('file_record_transcript.pdf', 'file_record_transcript'),
        ('file_07241999.pdf', 'file_07241999'),
        ('fileA1.pdf', 'fileA1'),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 14 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 15

# Exercise 10: Câu 10. Trích số phòng với phép hoặc và ranh giới từ
import re
PATTERN = r"\b([0-9]+)\s*(?:BR|bedrooms?)\b"

def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=re.I)
    return m.group(1) if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('Modern 1BR Oasis', '1'),
        ('Casa 3 bedrooms', '3'),
        ('Studio 2 br centro', '2'),
        ('12bravo centro', None),
        ('Modern 2BR2BA', None),
        ('Torre 2024', None),
        ('2 bedroom', '2'),
        ('2 BEDROOMS', '2'),
        ('Room 2 bedrooms and 1BR', '2'),
        ('x2BR', None),
        ('2 bedroomss', None),
        (None, None),
        ('A 0BR', '0'),
        ('2BR_apt', None),
        ('1 bedroom; 3BR', '1'),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Người phân tích đang đọc các tên chỗ ở do chủ nhà tự nhập và muốn tìm thông tin số '
        'phòng được ghi trong tên. Bản ghi đầu tiên là «Modern 1BR Oasis»; người tiếp theo '
        'đưa vào «Casa 3 bedrooms»; ở phần rà soát có «Studio 2 br centro»; sau đó nhóm ghi '
        'thêm «12bravo centro»; một mục khác được lưu là «Modern 2BR2BA»; và mục cuối trong '
        'lượt này là «Torre 2024». Các tên có chữ hoặc con số dễ gây nhầm đều được đưa vào '
        'bản ghi để kiểm tra ranh giới của cụm cần lấy.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('Modern 1BR Oasis', '1'),
        ('Casa 3 bedrooms', '3'),
        ('Studio 2 br centro', '2'),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 15 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 16

# Exercise 11: Câu 11. Kiểm tra số nguyên và số thập phân đơn giản
import re
PATTERN = r"-?[0-9]+(?:\.[0-9]+)?"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('3.14529', True),
        ('-255.34', True),
        ('128', True),
        ('720p', False),
        ('.5', False),
        ('5.', False),
        ('-0', True),
        ('001.50', True),
        ('+12', False),
        ('1,000', False),
        ('1e3', False),
        (' 12', False),
        ('12\n', False),
        (None, False),
        ('0.0', True),
        ('-', False),
        ('１２', False),
        ('12x5', False),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Trong quá trình nhập số đo từ một biểu mẫu, nhóm hỗ trợ giữ nguyên các ô dạng chuỗi '
        'để rà soát định dạng. Bản ghi đầu tiên là «3.14529»; người tiếp theo đưa vào '
        '«-255.34»; ở phần rà soát có «128»; sau đó nhóm ghi thêm «720p»; một mục khác được '
        'lưu là «.5»; và mục cuối trong lượt này là «5.». Người xử lý cần chọn đúng số theo '
        'miền đã cho trước khi chuyển kiểu, thay vì chỉ nhận một đoạn số nằm trong ô sai.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('3.14529', True),
        ('-255.34', True),
        ('128', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 18 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 19

# Exercise 12: Câu 12. Kiểm tra số có phân cách hàng nghìn và số mũ
import re
PATTERN = r"[+-]?(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?"

def solve(text):
    if text is None:
        return False
    m = re.fullmatch(PATTERN, text, flags=0)
    return m is not None

with redirect_stdout(StringIO()):
    CASES = [
        ('1.9e10', True),
        ('123,340.00', True),
        ('+1E-3', True),
        ('12,34.00', False),
        ('1,000e+2', True),
        ('720p', False),
        ('128', True),
        ('-255.34', True),
        ('1,234,567.89', True),
        ('1234,567', False),
        ('1,,000', False),
        ('1e', False),
        ('1e+', False),
        ('1.2.3', False),
        ('.5', False),
        ('12\n', False),
        (None, False),
        ('128e2', True),
        ('1,000,000', True),
        ('1,00e2', False),
        ('1.0e-2', True),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Một báo cáo kỹ thuật gom số liệu từ các phần mềm có thể ghi số theo dạng thường, '
        'nhóm hàng nghìn hoặc dạng số mũ. Bản ghi đầu tiên là «1.9e10»; người tiếp theo đưa '
        'vào «123,340.00»; ở phần rà soát có «+1E-3»; sau đó nhóm ghi thêm «12,34.00»; một '
        'mục khác được lưu là «1,000e+2»; và mục cuối trong lượt này là «720p». Nhóm cần '
        'chọn mục hợp lệ theo cùng một bộ quy tắc, đặc biệt kiểm tra các dấu phẩy và các '
        'thành phần bị thiếu.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('1.9e10', True),
        ('123,340.00', True),
        ('+1E-3', True),
        ('1,000e+2', True),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 21 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 22

# Exercise 13: Câu 13. Trích mã vùng điện thoại
import re
PATTERN = r"(?:1[ -]?)?(?:\(([0-9]{3})\)|([0-9]{3}))[ -]?[0-9]{3}[ -]?[0-9]{4}"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) or m.group(2) if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('415-555-1234', '415'),
        ('(416)555-3456', '416'),
        ('202 555 4567', '202'),
        ('4035555678', '403'),
        ('1 416 555 9292', '416'),
        ('(416555-3456', None),
        ('650-555-2345', '650'),
        ('1-416-555-9292', '416'),
        ('14165559292', '416'),
        ('416)5553456', None),
        ('+1 416 555 9292', None),
        ('416.555.3456', None),
        ('416-555-345', None),
        (' 4165553456', None),
        (None, None),
        ('(416)-555-3456', '416'),
        ('1 (416) 555 3456', '416'),
        ('416--555-3456', None),
        ('416\t5553456', None),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Bộ phận liên hệ khách hàng sao chép các số điện thoại từ nhiều biểu mẫu vào ghi chú '
        'chung. Bản ghi đầu tiên là «415-555-1234»; người tiếp theo đưa vào «(416)555-3456»; '
        'ở phần rà soát có «202 555 4567»; sau đó nhóm ghi thêm «4035555678»; một mục khác '
        'được lưu là «1 416 555 9292»; và mục cuối trong lượt này là «(416555-3456». Người '
        'xử lý phải kiểm cả số trước khi lấy mã vùng, vì một số dòng có hình thức gần đúng '
        'nhưng thiếu dấu ngoặc hoặc thiếu chữ số.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('415-555-1234', '415'),
        ('(416)555-3456', '416'),
        ('202 555 4567', '202'),
        ('4035555678', '403'),
        ('1 416 555 9292', '416'),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 19 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 20

# Exercise 14: Câu 14. Trích tên tài khoản email trước bộ lọc
import re
PATTERN = r"([A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*)(?:\+[A-Za-z0-9_]+)?@(?:[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\.)+[A-Za-z]{2,}"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('tom@hogwarts.com', 'tom'),
        ('tom.riddle@hogwarts.com', 'tom.riddle'),
        ('tom.riddle+regexone@hogwarts.com', 'tom.riddle'),
        ('tom@hogwarts.eu.com', 'tom'),
        ('hermione+regexone@hogwarts.com', 'hermione'),
        ('tom..riddle@hogwarts.com', None),
        ('an_01+lab@data-lab.edu.vn', 'an_01'),
        ('tom+@hogwarts.com', None),
        ('@hogwarts.com', None),
        ('tom@localhost', None),
        ('tom@-host.com', None),
        ('tom@host-.com', None),
        ('tom@@host.com', None),
        (' tom@host.com', None),
        (None, None),
        ('Tom.Riddle+LAB@EXAMPLE.COM', 'Tom.Riddle'),
        ('.tom@host.com', None),
        ('tom.@host.com', None),
        ('tom@host.c', None),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Nhóm hỗ trợ khóa học đang gom các địa chỉ email được dùng để nhận tài liệu, trong '
        'đó có địa chỉ gắn bộ lọc. Bản ghi đầu tiên là «tom@hogwarts.com»; người tiếp theo '
        'đưa vào «tom.riddle@hogwarts.com»; ở phần rà soát có '
        '«tom.riddle+regexone@hogwarts.com»; sau đó nhóm ghi thêm «tom@hogwarts.eu.com»; một '
        'mục khác được lưu là «hermione+regexone@hogwarts.com»; và mục cuối trong lượt này '
        'là «tom..riddle@hogwarts.com». Người xử lý chỉ trả tên tài khoản gốc sau khi địa '
        'chỉ đáp ứng miền quy tắc, còn các mục viết sai vẫn được giữ để thử mẫu.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('tom@hogwarts.com', 'tom'),
        ('tom.riddle@hogwarts.com', 'tom.riddle'),
        ('tom.riddle+regexone@hogwarts.com', 'tom.riddle'),
        ('tom@hogwarts.eu.com', 'tom'),
        ('hermione+regexone@hogwarts.com', 'hermione'),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 19 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 20

# Exercise 15: Câu 15. Trích tên thẻ mở đầu tiên
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

with redirect_stdout(StringIO()):
    CASES = [
        ('<a>Liên kết</a>', 'a'),
        ("<a href='https://regexone.com'>Mở</a>", 'a'),
        ("<div class='test_style'>Nội dung</div>", 'div'),
        ('<div>Chào <span>lớp</span></div>', 'div'),
        ('</div>', None),
        ('văn bản thuần', None),
        ('<h2>Tiêu đề</h2>', 'h2'),
        ('<my-card>Thẻ</my-card>', 'my-card'),
        ('<DIV>ABC</DIV>', 'DIV'),
        ('<123>abc</123>', None),
        ('<!-- ghi chú -->', None),
        ('<a', None),
        (None, None),
        ('<!-- <div>ẩn</div> -->', None),
        ('<!-- <div>ẩn</div> --><p>Hiện</p>', 'p'),
        ('<!-- <a>ẩn</a> --><!-- <b>ẩn</b> --><section>Hiện</section>', 'section'),
        ('<a>Hiện</a><!-- <div>ẩn</div> -->', 'a'),
        ('<br/>', 'br'),
        ("<img src='x'/>", 'img'),
        ('<my-card/>', 'my-card'),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Trong lúc rà soát các đoạn HTML nhỏ đã được xác nhận từ một nguồn kiểm soát được, '
        'người biên tập ghi lại một số đoạn và cả văn bản thuần. Bản ghi đầu tiên là '
        "«<a>Liên kết</a>»; người tiếp theo đưa vào «<a href='https://regexone.com'>Mở</a>»; "
        "ở phần rà soát có «<div class='test_style'>Nội dung</div>»; sau đó nhóm ghi thêm "
        '«<div>Chào <span>lớp</span></div>»; một mục khác được lưu là «</div>»; và mục cuối '
        'trong lượt này là «văn bản thuần». Nhóm chỉ cần nhận tên thẻ mở đầu tiên để phân '
        'loại nhanh từng đoạn, kể cả đoạn có thẻ con ở bên trong.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('<a>Liên kết</a>', 'a'),
        ("<a href='https://regexone.com'>Mở</a>", 'a'),
        ("<div class='test_style'>Nội dung</div>", 'div'),
        ('<div>Chào <span>lớp</span></div>', 'div'),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 20 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 21

# Exercise 16: Câu 16. Chọn tệp ảnh và trích phần mở rộng
import re
PATTERN = r"([A-Za-z0-9_]+(?:[.-][A-Za-z0-9_]+)*)\.(jpg|png|gif)"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.groups() if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('img0912.jpg', ('img0912', 'jpg')),
        ('updated_img0912.png', ('updated_img0912', 'png')),
        ('favicon.gif', ('favicon', 'gif')),
        ('.bash_profile', None),
        ('workspace.doc', None),
        ('img0912.jpg.tmp', None),
        ('anh-phong.01.png', ('anh-phong.01', 'png')),
        ('a.jpg.jpg', ('a.jpg', 'jpg')),
        ('.jpg', None),
        ('a..jpg', None),
        ('a.JPG', None),
        ('folder/a.jpg', None),
        ('a b.png', None),
        (None, None),
        ('a.pngx', None),
        ('photo-01.jpg', ('photo-01', 'jpg')),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Nhân viên quản lý tài nguyên chép tên các tệp nhận được trong ngày vào một đoạn báo '
        'cáo để chọn ảnh. Bản ghi đầu tiên là «img0912.jpg»; người tiếp theo đưa vào '
        '«updated_img0912.png»; ở phần rà soát có «favicon.gif»; sau đó nhóm ghi thêm '
        '«.bash_profile»; một mục khác được lưu là «workspace.doc»; và mục cuối trong lượt '
        'này là «img0912.jpg.tmp». Các tệp tài liệu, tệp ẩn và tệp tạm được giữ trong danh '
        'sách làm đối chứng, giúp kiểm tra đúng phần mở rộng ở cuối toàn tên.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('img0912.jpg', ('img0912', 'jpg')),
        ('updated_img0912.png', ('updated_img0912', 'png')),
        ('favicon.gif', ('favicon', 'gif')),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 16 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 17

# Exercise 17: Câu 17. Sửa mẫu cắt khoảng trắng bị tham lam
import re
PATTERN = r"[ \t]*(.*?)[ \t]*"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return (m.group(1) or "") if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('  Chào lớp  ', 'Chào lớp'),
        ('\tPhân tích dữ liệu\t', 'Phân tích dữ liệu'),
        ('  A  B  ', 'A  B'),
        ('   ', ''),
        ('', ''),
        (None, None),
        ('A', 'A'),
        (' A ', 'A'),
        ('\t \t', ''),
        ('  0  ', '0'),
        ('A\t B', 'A\t B'),
        ('Ñuñoa  ', 'Ñuñoa'),
        ('\xa0A\xa0', '\xa0A\xa0'),
        (' \xa0A\xa0\t', '\xa0A\xa0'),
        ('\x0bA\x0c', '\x0bA\x0c'),
        ('\xa0', '\xa0'),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Trong báo cáo nhập văn bản, nhóm gặp các mục có dấu cách hoặc tab thừa ở hai đầu và '
        'muốn chuẩn hóa chúng. Bản ghi đầu tiên là «  Chào lớp  »; người tiếp theo đưa vào '
        '«\tPhân tích dữ liệu\t»; ở phần rà soát có «  A  B  »; sau đó nhóm ghi thêm «   »; '
        'một mục khác được lưu là «». Một ô khác bị thiếu dữ liệu và được lưu là None. Bản '
        'ghi vẫn giữ cả mục toàn khoảng trắng, mục rỗng và dữ liệu thiếu, để người xử lý '
        'thấy rõ các trường hợp này khác nhau.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('  Chào lớp  ', 'Chào lớp'),
        ('\tPhân tích dữ liệu\t', 'Phân tích dữ liệu'),
        ('  A  B  ', 'A  B'),
        ('   ', ''),
        ('', ''),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 16 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 17

# Exercise 18: Câu 18. Trích dữ liệu từ dòng ngăn xếp lỗi
import re
PATTERN = r"\bat\s+(?:[A-Za-z_][A-Za-z0-9_]*\.)+([A-Za-z_][A-Za-z0-9_]*)\(([A-Za-z0-9_]+\.java):([0-9]+)\)"

def solve(text):
    if text is None:
        return None
    m = re.search(PATTERN, text, flags=0)
    return (m.group(1), m.group(2), int(m.group(3))) if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('E/( 1553): at widget.List.makeView(ListView.java:1727)', ('makeView', 'ListView.java', 1727)),
        ('E/( 1553): at widget.List.fillDown(ListView.java:652)', ('fillDown', 'ListView.java', 652)),
        ('E/( 1553): at widget.List.fillFrom(ListView.java:709)', ('fillFrom', 'ListView.java', 709)),
        ('W/dalvikvm: uncaught exception', None),
        ('E/: FATAL EXCEPTION: main', None),
        ('at widget.List.run(ListView.java:abc)', None),
        ('at app.Main.run(Main.java:0)', ('run', 'Main.java', 0)),
        ('at app.Main.run(Main.java:-1)', None),
        ('at app.Main.run(Unknown Source)', None),
        ('at app.Main.run(Main.java:12', None),
        ('at app.Main.run(Main.txt:12)', None),
        ('method(Main.java:12)', None),
        (None, None),
        ('sat app.Main.run(Main.java:2)', None),
        ('at app.Main.run(Main.java:007)', ('run', 'Main.java', 7)),
        ('E/: at pkg.sub.Main.run(Main.java:5)', ('run', 'Main.java', 5)),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Một nhân viên hỗ trợ ứng dụng gom các dòng thông báo và dòng ngăn xếp lỗi vào cùng '
        'một đoạn nhật ký bàn giao. Bản ghi đầu tiên là «E/( 1553): at '
        'widget.List.makeView(ListView.java:1727)»; người tiếp theo đưa vào «E/( 1553): at '
        'widget.List.fillDown(ListView.java:652)»; ở phần rà soát có «E/( 1553): at '
        'widget.List.fillFrom(ListView.java:709)»; sau đó nhóm ghi thêm «W/dalvikvm: '
        'uncaught exception»; một mục khác được lưu là «E/: FATAL EXCEPTION: main»; và mục '
        'cuối trong lượt này là «at widget.List.run(ListView.java:abc)». Nhóm phân tích cần '
        'chọn những dòng có đủ cụm phương thức, tệp nguồn và số dòng, sau đó chuyển số dòng '
        'sang kiểu số nguyên.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('E/( 1553): at widget.List.makeView(ListView.java:1727)',
         ('makeView', 'ListView.java', 1727)),
        ('E/( 1553): at widget.List.fillDown(ListView.java:652)',
         ('fillDown', 'ListView.java', 652)),
        ('E/( 1553): at widget.List.fillFrom(ListView.java:709)',
         ('fillFrom', 'ListView.java', 709)),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 16 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 17

# Exercise 19: Câu 19. Trích giao thức, máy chủ và cổng URL
import re
PATTERN = r"([A-Za-z][A-Za-z0-9+.-]*)://([A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*)(?::([0-9]+))?(?:/[^\s]*)?"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.groups() if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('ftp://file_server.com:21/top_secret/a.pdf', ('ftp', 'file_server.com', '21')),
        ('https://regexone.com/lesson/introduction#section', ('https', 'regexone.com', None)),
        ('file://localhost:4040/zip_file', ('file', 'localhost', '4040')),
        ('https://s3cur3-server.com:9999/', ('https', 's3cur3-server.com', '9999')),
        ('market://search/angry%20birds', ('market', 'search', None)),
        ('https://host:abc/a', None),
        ('http://localhost', ('http', 'localhost', None)),
        ('git+ssh://git.example.com:0022/x', ('git+ssh', 'git.example.com', '0022')),
        ('1http://host/a', None),
        ('https://host:/a', None),
        ('https:///a', None),
        ('https://a..com/x', None),
        ('https://host/a b', None),
        ('https://host:80x/a', None),
        (None, None),
        ('HTTPS://host/', ('HTTPS', 'host', None)),
        ('https://host:', None),
        ('https://host:999999/', ('https', 'host', '999999')),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Nhóm hạ tầng đang rà soát địa chỉ tài nguyên do nhiều dịch vụ gửi tới, với giao '
        'thức, máy chủ và cổng có thể khác nhau. Bản ghi đầu tiên là '
        '«ftp://file_server.com:21/top_secret/a.pdf»; người tiếp theo đưa vào '
        '«https://regexone.com/lesson/introduction#section»; ở phần rà soát có '
        '«file://localhost:4040/zip_file»; sau đó nhóm ghi thêm '
        '«https://s3cur3-server.com:9999/»; một mục khác được lưu là '
        '«market://search/angry%20birds»; và mục cuối trong lượt này là '
        '«https://host:abc/a». Người xử lý cần giữ nguyên ba trường có thật trong địa chỉ, '
        'đồng thời loại mục có cổng sai thay vì chỉ lấy một tiền tố hợp lệ.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('ftp://file_server.com:21/top_secret/a.pdf', ('ftp', 'file_server.com', '21')),
        ('https://regexone.com/lesson/introduction#section', ('https', 'regexone.com', None)),
        ('file://localhost:4040/zip_file', ('file', 'localhost', '4040')),
        ('https://s3cur3-server.com:9999/', ('https', 's3cur3-server.com', '9999')),
        ('market://search/angry%20birds', ('market', 'search', None)),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 18 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 19

# Exercise 20: Câu 20. Trích đường dẫn URL, loại truy vấn và đoạn neo
import re
PATTERN = r"https?://[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*(?::[0-9]+)?(/[^?#\s]*)?(?:\?[^#\s]*)?(?:#[^\s]*)?"

def solve(text):
    if text is None:
        return None
    m = re.fullmatch(PATTERN, text, flags=0)
    return m.group(1) or "/" if m is not None else None

with redirect_stdout(StringIO()):
    CASES = [
        ('https://example.com/data.csv?year=2026#top', '/data.csv'),
        ('http://localhost:8080/a/b', '/a/b'),
        ('https://example.com', '/'),
        ('https://example.com/?q=x', '/'),
        ('https://example.com/angry%20birds#info', '/angry%20birds'),
        ('ftp://example.com/a', None),
        ('https://example.com?q=x', '/'),
        ('https://example.com#top', '/'),
        ('https://example.com/a?x=1?y=2#z', '/a'),
        ('https://example.com/a#x?y=1', '/a'),
        ('https://example.com:abc/a', None),
        ('https://example.com/a b', None),
        ('https:///a', None),
        ('HTTP://example.com/a', None),
        (None, None),
        ('https://host:0', '/'),
        ('https://host/?#', '/'),
        ('https://host/a%2Fb?q=x', '/a%2Fb'),
    ]
    for text, expected in CASES:
        actual = solve(text)
        assert actual == expected, (text, expected, actual)
        assert type(actual) is type(expected), (text, type(expected), type(actual))

    # Đoạn văn đầu vào giống phần đề; ký tự trắng được giữ nguyên.
    PASSAGE = (
        'Trong một báo cáo truy cập, nhân viên ghi các địa chỉ trang có đường dẫn, tham số '
        'truy vấn hoặc đoạn neo để nhóm xử lý. Bản ghi đầu tiên là '
        '«https://example.com/data.csv?year=2026#top»; người tiếp theo đưa vào '
        '«http://localhost:8080/a/b»; ở phần rà soát có «https://example.com»; sau đó nhóm '
        'ghi thêm «https://example.com/?q=x»; một mục khác được lưu là '
        '«https://example.com/angry%20birds#info»; và mục cuối trong lượt này là '
        '«ftp://example.com/a». Mục tiêu là lấy riêng đường dẫn của các URL đúng miền đã '
        'nêu, giữ nguyên phần mã hóa và trả đường dẫn gốc khi địa chỉ không ghi đường dẫn.'
    )
    selected = []
    for item in re.findall(r"«([^»]*)»", PASSAGE):
        result = solve(item)
        if result is not None and result is not False:
            selected.append((item, result))
    assert selected == [
        ('https://example.com/data.csv?year=2026#top', '/data.csv'),
        ('http://localhost:8080/a/b', '/a/b'),
        ('https://example.com', '/'),
        ('https://example.com/?q=x', '/'),
        ('https://example.com/angry%20birds#info', '/angry%20birds'),
    ], selected
    print("Các mục được chọn:", selected)
    print("Đạt 18 test riêng và 1 test chọn trong đoạn văn")
TOTAL += 19

print(f"Regex: 20 exercises, {TOTAL} original public tests passed")
