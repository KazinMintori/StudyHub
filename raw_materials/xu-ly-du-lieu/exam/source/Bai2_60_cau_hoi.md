# Bài 2 — Python cơ bản cho xử lý dữ liệu

Ngân hàng 60 câu: 40 trắc nghiệm A/B/C/D, 20 tự luận ngắn, chia 6 đợt. Mỗi trắc nghiệm chỉ có một đáp án đúng.

Mỗi câu độc lập, chạy bằng Python 3 với dữ liệu khởi tạo riêng. File trong đề là UTF-8 và mở/ghi được theo mô tả; không cần tải Internet. Không tự thêm lỗi quyền, thiếu thư mục hoặc dữ liệu ngoài đề. Thư mục ban đầu của câu pathlib được nêu riêng. Nếu không hỏi chính xác kiểu dấu nháy/khoảng trắng trong repr list/dict, các cách trình bày tương đương có cùng kiểu và giá trị được hiểu như nhau.

Giá 0/âm và giá thiếu tuân theo quy tắc riêng của từng câu, không suy quy tắc từ câu trước. Tự luận trả lời ngắn hoặc vài dòng Python thuần. Ký hiệu a/b/c trong câu tích hợp là các yêu cầu phải làm, không phải các lựa chọn trắc nghiệm.

## Đợt 1 — B2-001 đến B2-010

7 câu đầu trắc nghiệm; 3 câu cuối tự luận.

### B2-001

Cột số lượng được nhập dưới dạng chuỗi. Dòng cuối in gì?
```python
a = "12"
b = "3"
print(a + b, int(a) + float(b))
```

A. `15 15.0`  
B. `123 15.0`  
C. `123 123`  
D. `15 123`

### B2-002

Trong dữ liệu cảm biến, chỉ xét cơ chế truthiness của Python. Dòng cuối in danh sách nào?
```python
xs = [None, 0, 0.0, "", "0", -2]
print([bool(x) for x in xs])
```

A. `[False, False, False, False, True, True]`  
B. `[False, False, False, False, False, True]`  
C. `[False, False, False, False, True, False]`  
D. `[False, True, True, False, True, True]`

### B2-003

Mỗi số là khối lượng một kiện, đơn vị gam: None chưa đo, số âm hỏng, 0 hợp lệ. Vòng lặp sau vừa lọc vừa đổi sang kg:
```python
gam = [1200, None, -10, 0, 2400]
kq = []
for g in gam:
    if g is not None and g >= 0:
        kq.append(g / 1000)
```
Comprehension nào cho đúng cùng danh sách?

A. `[g for g in gam if g is not None and g >= 0]`  
B. `[g / 1000 for g in gam if g is not None and g > 0]`  
C. `[g / 1000 for g in gam if g is not None and g >= 0]`  
D. `[g / 1000 for g in gam if g]`

### B2-004

Ba kho theo thứ tự K2, K1, K3 có số kiện 4,9,2. Đoạn code in gì?
```python
ten = ["K2", "K1", "K3"]
so_kien = [4, 9, 2]
bang = dict(zip(sorted(ten), so_kien))
print(bang["K1"], bang["K2"])
```

A. `4 9`  
B. `9 4`  
C. `2 9`  
D. `2 4`

### B2-005

Giá âm không hợp lệ cho báo cáo; 0 được phép là miễn phí. Hàm dưới chỉ chuyển định dạng. Dòng cuối in gì?
```python
def clean_price(s):
    try:
        return float(s.replace("$", "").replace(",", ""))
    except (ValueError, AttributeError):
        return None
raw = ["$2,050.00", "-5", "", "$0"]
print([clean_price(s) for s in raw])
```

A. `[2050.0, None, None, 0.0]`  
B. `[2050.0, -5.0, None, 0.0]`  
C. `[2050.0, -5.0, 0.0, 0.0]`  
D. `[2050.0, None, None, None]`

### B2-006

Tệp note.txt có đúng nội dung `Dữ liệu`, mã hóa UTF-8 và mở được. Thuộc tính f.closed cho biết file đã đóng hay chưa. Sau đoạn code, dòng cuối in gì?
```python
with open("note.txt", encoding="utf-8") as f:
    text = f.read()
print(f.closed, text)
```

A. `False Dữ liệu`  
B. `True None`  
C. `False None`  
D. `True Dữ liệu`

### B2-007

Tệp rev.csv dưới đây, mỗi dòng là một phòng và luot là số review; tệp UTF-8 mở được.
```csv
ma,luot
R1,0
R2,2
R3,0
R4,11
```
```python
import csv
with open("rev.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
print(sum(r["luot"] == 0 for r in rows),
      sum(r["luot"] == "0" for r in rows))
```
Dòng cuối in gì?

A. `2 2`  
B. `0 2`  
C. `2 0`  
D. `0 0`

### B2-008

Ba dict sau lần lượt biểu diễn phí chưa rõ, phí miễn và chưa có khóa phí:
```python
a = {"phi": None}
b = {"phi": 0}
c = {}
print([r.get("phi", 5) for r in [a, b, c]])
```
Nêu output, sau đó cho biết `c["phi"]` có cho cùng kết quả với `c.get("phi",5)` không và vì sao; 1–2 câu.

### B2-009

Báo cáo chỉ chấp nhận giá >0; dữ liệu hỏng cần thành None. Hàm và đoạn áp dụng hiện tại:
```python
def to_float(s):
    try:
        return float(s)
    except ValueError:
        return None
raw = ["8", "0", "-2", "bad", None]
v = [to_float(s) for s in raw]
```
(a) Vì sao chưa tạo xong v? (b) Sửa mệnh đề except đúng phạm vi lỗi của float, rồi viết một comprehension lấy giá >0 an toàn từ v. (c) Nêu hai ca biên cho thấy đổi kiểu và lọc giá là hai việc khác nhau.

### B2-010

Mỗi phần tử là giá một phòng, đơn vị USD/đêm; 0 miễn phí hợp lệ, None chưa biết. Code hiện tại:
```python
gia = [0, None, 60, 60]
co_gia = [g for g in gia if g is not None]
print(sum(co_gia) / len(gia))
```
(a) In gì, vì sao sai yêu cầu “trung bình các phòng đã khai giá”? (b) Sửa mẫu số và nêu kết quả đúng. (c) Nếu mọi giá đều None, cần xử lý thế nào? Trả lời ngắn, có thể dùng một dòng điều kiện.

## Đợt 2 — B2-011 đến B2-020

7 câu đầu trắc nghiệm; 3 câu cuối tự luận.

### B2-011

Số lượt thuê từ thứ Hai đến Chủ nhật theo thứ tự:
```python
luot = [4, 7, 5, 8, 6, 9, 3]
```
Biểu thức nào tính đúng tổng từ thứ Ba đến hết thứ Năm?

A. `sum(luot[1:4])`  
B. `sum(luot[1:3])`  
C. `sum(luot[2:5])`  
D. `sum(luot[:4])`

### B2-012

Dict dem cho số phòng ở từng khu, không có đồng hạng. Dòng cuối in gì?
```python
dem = {"B": 4, "A": 8, "D": 2, "C": 6}
top = sorted(dem.items(), key=lambda kv: kv[1], reverse=True)[:2]
print(top)
```

A. `[("A",8),("B",4)]`  
B. `[("D",2),("B",4)]`  
C. `[("A",8),("C",6)]`  
D. `[8,6]`

### B2-013

Không có try/except trong hai biểu thức đang xét. Cặp loại lỗi đúng lần lượt của `float(None)` và `None.replace("$", "")` là gì?

A. ValueError; AttributeError.  
B. TypeError; AttributeError.  
C. TypeError; ValueError.  
D. AttributeError; TypeError.

### B2-014

Đọc hàm sau; quy tắc nghiệp vụ của báo cáo riêng yêu cầu số đêm >0.
```python
def clean_nights(s) -> int | None:
    """Đổi được sang int thì trả số; dữ liệu không đổi được trả None."""
    try:
        return int(s)
    except (ValueError, TypeError):
        return None
print(clean_nights("-2"), clean_nights(None))
```
Nhận định nào đúng?

A. In `None None`; type hint int tự loại giá trị âm.  
B. In `-2 0`; đầu vào None được đổi thành số nguyên 0.  
C. In `-2 None`; hàm chưa tự áp quy tắc >0.  
D. Dừng ở ValueError; int không chấp nhận chuỗi có dấu trừ.

### B2-015

Tệp dem.csv UTF-8 mở được, mỗi dòng là một lượt thuê:
```csv
ma,dem
A,3
B,20
C,100
D,8
```
```python
import csv
with open("dem.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
kq = sorted(rows, key=lambda r: r["dem"])[:2]
print([r["ma"] for r in kq])
```
Dòng cuối in gì?

A. `["A","D"]`  
B. `["D","A"]`  
C. `["C","B"]`  
D. `["A","B"]`

### B2-016

JSON dưới là chuỗi, không phải dict Python viết sẵn. Dòng cuối in gì?
```python
import json
s = '{"n":4,"ok":true,"x":null,"tags":["null",false]}'
d = json.loads(s)
print(d["n"] + 1, d["x"], d["ok"], repr(d["tags"][0]), d["tags"][1])
```

A. `5 'null' True 'null' False`  
B. `5 None true 'null' false`  
C. `5 None True 'null' False`  
D. Báo TypeError tại phép cộng với1.

### B2-017

Ban đầu chỉ có tệp `out/keep.txt`, nội dung là `giu`; chưa có thư mục out/2026 và thang10. Các đường dẫn đều mở/tạo được.
```python
from pathlib import Path
p = Path("out") / "2026" / "thang10"
p.mkdir(parents=True, exist_ok=True)
p.mkdir(parents=True, exist_ok=True)
```
Trạng thái nào đúng sau cả hai lần mkdir?

A. Có cây `out/2026/thang10`; `out/keep.txt` bị xóa để tạo lại cây sạch.  
B. Có cây `out/2026/thang10`; `out/keep.txt` vẫn có nội dung giu.  
C. Lần thứ hai báo FileExistsError; keep.txt còn nguyên.  
D. Lần đầu báo FileNotFoundError vì thư mục `out/2026` chưa tồn tại.

### B2-018

Một cặp chứa tên khu và số phòng. Viết chính xác dòng output, dùng dấu | để thể hiện ranh giới cột; nêu giá trị n sau khi in.
```python
ten, n = ("An", 1200)
print(f"|{ten:<5}|{n:>6,}|")
```
Trả lời trong một khối code ngắn và một câu.

### B2-019

Mỗi dict là một phòng; mọi giá đều đã biết, 0 hợp lệ. Chỉ có các khóa phẳng như dưới đây:
```python
a = [{"id":1,"gia":20}, {"id":2,"gia":40},
     {"id":3,"gia":60}, {"id":4,"gia":80}]
b = a.copy()
b[0]["gia"] = 0
b.append({"id":5,"gia":100})
print(len(a), a[0]["gia"], len(b))
```
(a) In gì? (b) Vì sao sửa giá và append tác động khác nhau tới a? (c) Nếu cần sửa giá thử nghiệm mà giữ nguyên a, thay dòng tạo b thế nào? Không dùng deepcopy.

### B2-020

Mỗi dòng là một phòng, giá USD/đêm đã là số; chỉ giá >0 hợp lệ cho xếp hạng. Nhóm cần các khu có ít nhất 2 giá hợp lệ.
```python
rows = [{"khu":"A","gia":0}, {"khu":"A","gia":None},
        {"khu":"A","gia":90}, {"khu":"B","gia":40},
        {"khu":"B","gia":80}, {"khu":"B","gia":None}]
dem = {}
for r in rows:
    k = r["khu"]
    dem[k] = dem.get(k, 0) + 1
print(sorted(k for k in dem if dem[k] >= 2))
```
(a) Code chọn khu nào, sai ở tập đếm nào? (b) Viết hàm gia_khu(ten) trả list giá hợp lệ của khu và một dòng chọn khu đúng. (c) Nêu list giá B và lý do không dùng tổng số phòng để thay số có giá.

## Đợt 3 — B2-021 đến B2-030

7 câu đầu trắc nghiệm; 3 câu cuối tự luận.

### B2-021

Số đo được lưu ở biến gia, chỉ cần đổi cách hiển thị. Dòng cuối in gì?
```python
gia = 12340.75
s = f"{gia:,.0f}"
print(s, gia)
```

A. `12,341 12341.0`  
B. `12341 12340.75`  
C. `12,341 12340.75`  
D. `12,340.75 12340.75`

### B2-022

Bốn bản ghi phòng chỉ có mã và loại. Dòng cuối in gì?
```python
rows = [{"id":1,"loai":"B"}, {"id":2,"loai":"A"},
        {"id":3,"loai":"B"}, {"id":4,"loai":"C"}]
loai = {r["loai"] for r in rows}
print(sorted(loai), "D" in loai)
```

A. `["A","B","C"] False`  
B. `["B","A","B","C"] False`  
C. `["A","B","B","C"] False`  
D. `["A","B","C"] True`

### B2-023

Mỗi dict là một phòng, giá USD/đêm dương và khác nhau. Dòng cuối in gì?
```python
rows = [{"id":"P1","gia":40}, {"id":"P2","gia":15},
        {"id":"P3","gia":90}, {"id":"P4","gia":60}]
p = max(rows, key=lambda r: r["gia"])
print(p["id"], p["gia"])
```

A. `P4 60`  
B. `P2 15`  
C. `P3 90`  
D. Báo TypeError vì p chỉ là số 90.

### B2-024

Hàm sau đã định nghĩa; raw chứa các chuỗi giá:
```python
def clean_price(s):
    return float(s.replace("$", ""))
raw = ["$2", "$0", "$5", "$8"]
```
Biểu thức nào tạo list `[2.0,0.0,5.0,8.0]` bằng map?

A. `list(map(clean_price(), raw))`  
B. `list(map(clean_price, raw))`  
C. `list(map(clean_price(raw), raw))`  
D. `[clean_price for s in raw]`

### B2-025

Tệp ghi_chu.txt ban đầu chứa đúng `cũ`, là UTF-8 và mở được. Dòng cuối in gì?
```python
with open("ghi_chu.txt", encoding="utf-8") as f:
    truoc = f.read()
with open("ghi_chu.txt", "w", encoding="utf-8") as f:
    f.write("mới")
with open("ghi_chu.txt", encoding="utf-8") as f:
    sau = f.read()
print(truoc, sau)
```

A. `mới mới`  
B. `cũ mới`  
C. `cũ cũmới`  
D. `cũ cũ`

### B2-026

Tệp mới gia.csv mở được. Code ghi bằng thư viện csv:
```python
import csv
with open("gia.csv", "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["id", "gia"])
    w.writeheader()
    w.writerow({"id":"P1", "gia":"$1,200"})
```
Bỏ qua khác biệt ký tự xuống dòng giữa hệ điều hành, hai dòng văn bản nào đúng?

A. `id,gia` rồi `P1,$1,200`.  
B. `P1,"$1,200"` rồi không còn dòng nào.  
C. `id,gia` rồi `P1,"$1,200"`.  
D. `id,gia` rồi `P1,1200.0`.

### B2-027

Giá bốn phòng tính bằng USD/đêm; chưa có bằng chứng phòng giá 140 sai. Hàm trung vị nhận list không rỗng:
```python
def trung_vi(xs):
    xs = sorted(xs)
    n = len(xs)
    if n % 2 == 1:
        return xs[n // 2]
    return (xs[n // 2 - 1] + xs[n // 2]) / 2
gia = [140, 10, 30, 20]
print(trung_vi([9, 1, 5]), sum(gia)/len(gia), trung_vi(gia), gia[0])
```
Nhận định nào đúng?

A. In `5 50.0 25.0 140`; giá lớn kéo trung bình lên nhưng chưa đủ để xóa.  
B. In `5 50.0 25.0 10`; sorted đã đổi list gốc nên phần tử đầu là 10.  
C. In `5 25.0 50.0 140`; trung bình và trung vị cho hai mức giá đó.  
D. In `5 20.0 20.0 140`; hàm tự bỏ 140 vì đó là ngoại lai.

### B2-028

Hai tập mã cảm biến hoạt động:
```python
cu = {11, 12, 13, 14}
moi = {13, 14, 15, 16}
bien_mat = moi - cu
print(sorted(bien_mat))
```
Code hiện in gì và có đúng tên bien_mat không? Sửa phép trừ để tìm mã biến mất, rồi tính `sorted((cu | moi) - (cu & moi))` và giải thích tập đó trong 1–3 câu.

### B2-029

Quy tắc giá USD/đêm: 0 miễn phí hợp lệ, âm không hợp lệ, None thiếu. Hàm chuyển giá như sau:
```python
def clean_price(s):
    try:
        return float(s.replace("$", ""))
    except (ValueError, AttributeError):
        return None
v = [clean_price(s) for s in ["$30", "$0", "$-3", "N/A", None]]
giu = [x for x in v if x]
print(giu, sum(giu)/len(giu))
```
(a) Code in gì, sai quy tắc nào? (b) Thay điều kiện lọc để tính đúng, nêu trung bình đúng. (c) Hai đầu vào biên nào cần giữ trong bộ thử để bắt lỗi này?

### B2-030

Cùng thư mục chạy có module cleaning.py mở/import được, nội dung:
```python
def clean_price(s):
    return float(s.replace("$", ""))
```
File chạy chính chỉ có:
```python
from cleaning import clean_price
print(cleaning.clean_price("$80"))
```
(a) File chính gặp lỗi gì? (b) Nêu một cách sửa lời gọi hoặc import. (c) Vì sao gom hàm này vào module giúp tái sử dụng; phương thức replace thuộc về đối tượng nào? Trả lời ngắn.

## Đợt 4 — B2-031 đến B2-040

7 câu đầu trắc nghiệm; 3 câu cuối tự luận.

### B2-031

Một tỷ lệ được lưu dưới dạng 0–1. Dòng cuối in gì?
```python
p = 0.04
print(f"{p:.1%}", f"{p:.1f}%")
```

A. `4.0% 4.0%`  
B. `0.0% 0.0%`  
C. `400.0% 4.0%`  
D. `4.0% 0.0%`

### B2-032

Bốn mã phòng và giá USD/đêm ban đầu khớp theo vị trí. Cần hai cặp có giá thấp nhất, vẫn đúng mã-giá, giá không đồng hạng.
```python
ma = ["P4", "P1", "P3", "P2"]
gia = [50, 40, 10, 20]
```
Biểu thức nào đáp ứng?

A. `sorted(zip(ma, gia), key=lambda x: x[1])[:2]`  
B. `list(zip(ma, sorted(gia)))[:2]`  
C. `list(zip(sorted(ma), gia))[:2]`  
D. `sorted(zip(ma, gia))[:2]`

### B2-033

Danh sách số lượng kiểm kê được sửa qua hai tên khác nhau. Dòng cuối in gì?
```python
a = [7, 3, 5, 1]
b = a
c = a.copy()
b[1] = 9
c.append(2)
print(a, c)
```

A. `[7,3,5,1] [7,3,5,1,2]`  
B. `[7,9,5,1,2] [7,9,5,1,2]`  
C. `[7,9,5,1] [7,9,5,1,2]`  
D. `[7,9,5,1] [7,3,5,1,2]`

### B2-034

Quy ước của bước chuyển giá: trả số hoặc None và không sửa dữ liệu ngoài. Đọc code sau:
```python
nhat_ky = []
def to_float(s) -> float | None:
    """Đổi chuỗi số; chuỗi hỏng trả None."""
    nhat_ky.append(s)
    try:
        return float(s)
    except (ValueError, TypeError):
        return None
print(to_float("10"), nhat_ky)
```
Nhận định nào đúng với quy ước đã nêu?

A. Trả 10.0 và không sửa ngoài; type hint đã bảo đảm điều đó.  
B. Trả None vì type hint float không nhận chuỗi đầu vào.  
C. Trả 10.0 nên đã đáp ứng toàn bộ quy ước, dù nhat_ky đổi.  
D. Trả 10.0 nhưng sửa nhat_ky; cần tách việc ghi nhật ký khỏi hàm chuyển.

### B2-035

Tệp mới bao_cao.json mở được. Đoạn ghi và đọc lại:
```python
import json
obj = {"khu": "Đồi", "n": 2}
with open("bao_cao.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)
with open("bao_cao.json", encoding="utf-8") as f:
    doc = json.load(f)
print(doc["khu"], doc["n"] + 1)
```
Nhận định nào đúng?

A. In `Đồi 3`; ensure_ascii và indent tác động biểu diễn, không biến n thành chuỗi.  
B. In `Đồi 21`; ensure_ascii=False chuyển cả số 2 thành chuỗi.  
C. Báo TypeError vì mọi giá trị đọc từ file đều là chuỗi.  
D. In `Đồi 3`; indent=2 làm mọi số trong báo cáo có hai chữ số thập phân.

### B2-036

Dict dem là số phòng, tv là giá trung vị USD/đêm; không có đồng hạng. Cần chọn khu giá cao nhất trong hai khu đông phòng nhất.
```python
dem = {"A": 5, "B": 2, "C": 3, "D": 1}
tv = {"A": 20, "B": 90, "C": 50, "D": 40}
top = sorted(dem, key=lambda k: dem[k], reverse=True)[:2]
chon = max(top, key=lambda k: tv[k])
print(chon)
```
Dòng cuối in gì?

A. `B`  
B. `C`  
C. `A`  
D. `D`

### B2-037

Cây ban đầu có đúng ba tệp dưới đây, cùng các thư mục cha của chúng, không có mục nào khác:
```text
data/raw/bang.csv
data/raw/HaNoi/a.csv
data/raw/Hue/b.csv
```
```python
from pathlib import Path
DATA = Path("data") / "raw" / "HaNoi"
print(sorted(p.name for p in DATA.parent.glob("*.csv")))
```
Dòng cuối in gì? p.name trả tên tệp ở cuối đường dẫn; không cần xét cách repr của Path theo hệ điều hành.

A. `["a.csv"]`  
B. `["a.csv","b.csv","bang.csv"]`  
C. `["HaNoi","Hue"]`  
D. `["bang.csv"]`

### B2-038

Thiết kế dữ liệu cho một báo cáo: (i) doanh thu từng ngày cần giữ thứ tự để cắt khoảng; (ii) tra giá theo mã phòng; (iii) so tập mã giữa hai snapshot, không cần giữ trùng; (iv) lưu một cặp tọa độ không thay đổi. Chọn list/dict/set/tuple cho từng việc và minh họa cách giải nén cặp (10,106), trong 1–3 câu hoặc một dòng lệnh.

### B2-039

Giá hợp lệ đều dương; chuỗi hỏng hoặc rỗng là chưa biết, không phải giá 0. Code hiện tại:
```python
def clean_price(s):
    try:
        return float(s.replace("$", ""))
    except (ValueError, AttributeError):
        return 0
raw = ["$30", "N/A", "$90", ""]
v = [clean_price(s) for s in raw]
print(sum(v)/len(v))
```
(a) Output và trung bình đúng của các giá đã biết là bao nhiêu? (b) Sửa quy ước trả về và bước lọc. (c) Nếu chỉ có dữ liệu hỏng, quy định đầu ra trung bình thế nào để không che sự thiếu dữ liệu?

### B2-040

Tệp p.csv UTF-8 mở được; giá USD/đêm, ô trống chưa biết, 0 miễn phí hợp lệ:
```csv
id,gia
P1,9
P2,100
P3,
P4,20
```
```python
import csv
with open("p.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
gia = [r["gia"] for r in rows if r["gia"]]
print(max(gia))
```
(a) Code in gì và vì sao không phải giá lớn nhất? (b) Sửa dòng tạo gia để được số, bỏ đúng ô trống; nêu max đúng. (c) Nếu thêm dòng giá "0", dòng đó có cần bị loại không? Nêu thêm điều kiện trước max khi mọi ô đều trống.

## Đợt 5 — B2-041 đến B2-050

6 câu đầu trắc nghiệm; 4 câu cuối tự luận.

### B2-041

Dãy lượt thuê được lưu đúng thứ tự thời gian. Dòng cuối in gì?
```python
luot = [4, 7, 5, 8, 6, 9, 3]
print(luot[0], luot[-1], luot[-2])
```

A. `4 9 6`  
B. `4 3 9`  
C. `7 3 9`  
D. `4 3 7`

### B2-042

Các chuỗi đều chuyển được sang int. Dòng cuối in gì?
```python
v = ["40", "8", "120", "3"]
print(sorted(v, key=int)[:2], sorted(v)[:2])
```

A. `["3","8"] ["120","3"]`  
B. `[3,8] ["120","3"]`  
C. `["120","3"] ["3","8"]`  
D. `["3","8"] ["3","8"]`

### B2-043

Bộ thử chỉ có hai ca ở dưới và đều qua. Nhận định nào đúng?
```python
def clean(s):
    try:
        return float(s.replcae("$", ""))
    except Exception:
        return None
assert clean("") is None
assert clean(None) is None
print(clean("$10"))
```

A. In None; chỉ đổi except thành AttributeError là hàm đã chuyển giá đúng.  
B. In None; hai assert đã đủ chứng minh hàm đổi đúng mọi giá bình thường.  
C. Dừng ở AttributeError vì except Exception chỉ bắt lỗi dữ liệu số.  
D. In None; sai tên phương thức bị che, cần sửa và thử cả giá bình thường.

### B2-044

Một tệp bc.json UTF-8 mở được chứa `{"n":4}`; biến s cũng là chuỗi `'{"n":4}'`. Với file đang mở ở tên f, cặp lời gọi nào đọc đúng cả hai nguồn theo thứ tự file rồi chuỗi?

A. `json.loads(f)` và `json.load(s)`.  
B. `json.dump(f)` và `json.loads(s)`.  
C. `json.load(f)` và `json.loads(s)`.  
D. `json.load(f)` và `json.dump(s)`.

### B2-045

Mỗi tuple là (id phòng, giá USD/đêm, số đêm tối thiểu). Quy tắc: giá phải >0, số đêm không quá 30. Chỉ gắn cờ để kiểm, chưa xóa dòng.
```python
rows = [(1,0,2), (2,40,3), (3,-2,40),
        (4,0,60), (5,80,10), (6,50,31)]
sai_gia = {i for i, g, n in rows if g <= 0}
sai_dem = {i for i, g, n in rows if n > 30}
print(len(sai_gia | sai_dem), len(rows))
```
Dòng cuối in gì?

A. `4 6`  
B. `6 6`  
C. `4 2`  
D. `2 6`

### B2-046

Mỗi dòng là một phòng, number_of_reviews là chuỗi. Quy ước nhất quán mong muốn: số review 0 thì last_review trống; số review dương thì có ngày. Code chỉ kiểm như sau:
```python
rows = [{"id":"A","number_of_reviews":"0","last_review":""},
        {"id":"B","number_of_reviews":"1","last_review":""},
        {"id":"C","number_of_reviews":"2","last_review":"2026-01-02"},
        {"id":"D","number_of_reviews":"0","last_review":""}]
chua = [r for r in rows if r["number_of_reviews"] == "0"]
assert all(r["last_review"] == "" for r in chua)
```
Nhận định nào đúng?

A. Assert qua, vậy cả hai chiều của quan hệ đều được xác nhận.  
B. Assert lỗi ở B vì all tự quét mọi dòng của rows.  
C. Assert lỗi ở A, D vì chuỗi "0" là truthy nên phải có ngày.  
D. Assert qua; phòng B sai chiều còn lại nhưng chưa nằm trong tập được kiểm.

### B2-047

Mỗi phần tử là nhiệt độ °C, số âm và 0 đều hợp lệ; chỉ None là chưa đo.
```python
nhiet = [-4, 0, None, 8]
giu = [x for x in nhiet if x]
print(giu, sum(giu)/len(giu))
```
Nêu output và sửa điều kiện theo yêu cầu, kèm trung bình đúng. Vì sao không thay bằng điều kiện x>0? Trả lời 1–3 câu.

### B2-048

Bốn phòng đã có giá số USD/đêm; 0 hợp lệ, âm hỏng, None thiếu:
```python
rows = [{"id":"P1","gia":None}, {"id":"P2","gia":0},
        {"id":"P3","gia":-2}, {"id":"P4","gia":50}]
```
Viết (i) một comprehension lấy id các phòng có giá hợp lệ theo thứ tự gốc; (ii) một dict comprehension ánh xạ id→giá của đúng các phòng ấy. Nêu hai kết quả.

### B2-049

Chỉ giá >0 hợp lệ; chuỗi hỏng chuyển None. Hàm đã đúng cho việc chuyển kiểu:
```python
def to_float(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None
v = list(map(to_float, ["10", "bad", "0", "-5", None]))
pos = [x for x in v if x > 0]
print(sum(pos)/len(pos))
```
(a) Dừng ở đâu, lỗi gì? (b) Sửa dòng lọc, nêu pos và trung bình sau sửa. (c) Viết một dòng tính trung bình trả None khi không còn giá, để ca toàn dữ liệu hỏng không chia rỗng.

### B2-050

Tệp bc.json mới mở được. Báo cáo quy định so_phong phải là số nguyên, không phải chuỗi.
```python
import json
obj = {"khu":"Đồi", "so_phong":"4", "gia":[0,30,None], "dat":True}
with open("bc.json", "w", encoding="utf-8") as f:
    json.dump(obj, f, ensure_ascii=False, indent=2)
with open("bc.json", encoding="utf-8") as f:
    doc = json.load(f)
print(doc == obj)
```
(a) In gì; so_phong đã đúng kiểu yêu cầu chưa? (b) Sửa trước khi ghi. (c) Nêu phép kiểm bổ sung để equality không bị dùng như bằng chứng dữ liệu nguồn đã đúng.

## Đợt 6 — B2-051 đến B2-060

6 câu đầu trắc nghiệm; 4 câu cuối tự luận.

### B2-051

Một trường đọc từ CSV là chuỗi `"3.5"`. Biểu thức nào cho số thực 3.5 để cộng với các số đo khác, giữ phần thập phân?

A. `int("3.5")`  
B. `str("3.5")`  
C. `bool("3.5")`  
D. `float("3.5")`

### B2-052

Dict ghi số kiện tại bốn kho; không có đồng hạng. Dòng cuối in gì?
```python
ton = {"B":2, "A":9, "C":5, "D":1}
theo_ma = sorted(ton.items())[:2]
theo_so = sorted(ton.items(), key=lambda kv: kv[1], reverse=True)[:2]
print(theo_ma, theo_so)
```

A. `[("D",1),("B",2)] [("A",9),("C",5)]`  
B. `[("A",9),("B",2)] [("D",1),("B",2)]`  
C. `[("A",9),("C",5)] [("A",9),("B",2)]`  
D. `[("A",9),("B",2)] [("A",9),("C",5)]`

### B2-053

Hàm chỉ chuyển kiểu số đêm, chưa lọc nghiệp vụ >0. Dòng cuối in gì?
```python
def clean_nights(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None
raw = ["3", "3.0", "-2", "0"]
print([clean_nights(s) for s in raw])
```

A. `[3,3,-2,0]`  
B. `[3,None,-2,0]`  
C. `[3,None,None,None]`  
D. `[3,3,None,None]`

### B2-054

Tệp gia.csv UTF-8 mở được, mỗi dòng là một phòng; ô trống chưa biết, 0 miễn phí hợp lệ.
```csv
id,gia
P1,0
P2,15
P3,
P4,30
```
```python
import csv
with open("gia.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))
v = [float(r["gia"]) for r in rows if r["gia"] != ""]
print(len(v), sum(v)/len(v))
```
Dòng cuối in gì?

A. `2 22.5`  
B. `3 11.25`  
C. `3 15.0`  
D. Báo ValueError do ô trống.

### B2-055

Mỗi chuỗi là ngày của một review riêng. Nguồn đầy đủ cho 2025 và chỉ đến 30/06/2026; mọi ngày đúng YYYY-MM-DD.
```python
dates = ["2025-01-03", "2025-04-10", "2026-01-05",
         "2025-09-02", "2026-05-20", "2025-12-15"]
dem = {}
for date in dates:
    nam = date[:4]
    dem[nam] = dem.get(nam, 0) + 1
print(sorted(dem.items()))
```
Nhận định nào đúng?

A. Đếm 2025: 4,2026: 2; đủ kết luận cả năm 2026 chắc chắn giảm một nửa.  
B. Đếm 2025: 4,2026: 2; phép đếm đã xác định nguyên nhân giảm là giá thuê tăng.  
C. Đếm 2025: 1,2026: 1; dict chỉ giữ một lần xuất hiện cho mỗi năm.  
D. Đếm 2025: 4,2026: 2; chưa thể kết luận xu hướng cả năm hoặc nguyên nhân từ hai số này.

### B2-056

Ba hàm đã có giao ước: load_csv(path) trả list các dict từ CSV; summarize(rows) nhận list đó và trả dict báo cáo; save_json(obj, path) nhận dict rồi ghi file. Tệp in.csv UTF-8 mở được, chứa:
```csv
id,gia
P1,10
P2,20
P3,30
P4,40
```
Biểu thức nào ghép đúng thứ tự và đúng kiểu đầu vào/đầu ra để ghi out.json?

A. `save_json(summarize(load_csv("in.csv")), "out.json")`  
B. `summarize(save_json(load_csv("in.csv"), "out.json"))`  
C. `save_json(load_csv(summarize("in.csv")), "out.json")`  
D. `save_json(summarize("in.csv"), "out.json")`

### B2-057

Mỗi tuple là (mã phòng, giá USD/đêm); giá đều dương, khác nhau:
```python
phong = [("P1",40), ("P2",10), ("P3",90), ("P4",20)]
dat = max(phong, key=lambda p: p[1])
print(dat)
```
Nêu output và kiểu kết quả. Viết một biểu thức lấy mã hai phòng rẻ nhất theo giá tăng dần; sau khi dùng sorted, phần tử đầu phong có còn là ("P1", 40) không?

### B2-058

Báo cáo chỉ nhận giá dương; giá 0 và giá âm không hợp lệ. Hàm sau được thử chuỗi bình thường, rỗng và N/A; chưa thử None:
```python
def clean_price(s):
    try:
        return float(s.replace("$", ""))
    except (ValueError, TypeError):
        return None
raw = ["$10", None, "$0", "$-2"]
v = list(map(clean_price, raw))
```
(a) Lỗi thực tế ở đâu, loại gì? (b) Sửa except đúng với thao tác; nêu v sau sửa và một comprehension lấy giá hợp lệ. (c) Ca 0/âm còn cần dù hàm đã bắt lỗi không, vì sao?

### B2-059

Tệp phong.csv UTF-8 hiện có nội dung cũ, được phép ghi đè và mở được. Cần ghi đúng một bản ghi dưới đây, có header; nhan chứa dấu phẩy trong một trường:
```python
row = {"ma":"S1", "nhan":"Nam, Bắc", "gia":"0"}
```
Viết đoạn ghi bằng csv.DictWriter, thứ tự cột ma, nhan, gia; chỉ rõ encoding và newline. Khi đọc lại bằng DictReader, nhan và gia là gì? Nêu vai trò newline=""; không phải xử lý mọi biến thể CSV.

### B2-060

Cần đếm từng review theo năm. Nguồn có đủ 2025 nhưng chỉ đến 30/06/2026. Một nhóm lại dùng bảng phòng (mỗi dòng một phòng) thay vì bảng reviews (mỗi dòng một review):
```python
phong = [{"id":1,"last_review":"2026-02-01"},
         {"id":2,"last_review":"2025-12-02"},
         {"id":3,"last_review":""},
         {"id":4,"last_review":"2026-03-02"}]
reviews = [{"date":"2025-01-02"}, {"date":"2025-05-03"},
           {"date":"2025-09-01"}, {"date":"2025-12-02"},
           {"date":"2026-02-01"}, {"date":"2026-03-02"}]
dem = {}
for p in phong:
    if p["last_review"]:
        nam = p["last_review"][:4]
        dem[nam] = dem.get(nam, 0) + 1
print(sorted(dem.items()))
```
(a) Output đang đếm gì? (b) Thay vòng lặp bằng đoạn ngắn để đếm đúng review; nêu kết quả. (c) Hai số theo năm có đủ kết luận thị trường 2026 suy giảm hoặc xác định nguyên nhân không?
