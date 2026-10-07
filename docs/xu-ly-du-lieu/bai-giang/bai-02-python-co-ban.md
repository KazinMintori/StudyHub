---
course: xu-ly-du-lieu
lecture: bai-02-python-co-ban
section: lecture
title: "Python cơ bản cho xử lý dữ liệu"
prerequisites: ["bien-kieu","list","dictionary","vong-lap","ham-lap-trinh"]
lessonStatus: ready
---


::: tip  Sau bài này bạn phải trả lời được
1. Cho một bài toán dữ liệu cụ thể, chọn đúng cấu trúc trong 4 loại `list / dict / set / tuple` — và giải thích **vì sao** cấu trúc khác lại không phù hợp.
2. Viết lại một vòng lặp `for` thành *comprehension*, và giải thích comprehension là "bước đệm tư duy" sang NumPy như thế nào.
3. Chỉ ra lỗi trong đoạn code dùng `except Exception: pass`, và trong đoạn code gán `b = a` rồi sửa `b` khiến `a` đổi theo.
:::

## 0. Nhập môn bằng một ẩn dụ: cái kho hàng

Nếu dữ liệu là hàng hoá, thì mỗi **cấu trúc dữ liệu** trong Python là một loại kệ chứa khác nhau trong kho — chọn sai loại kệ thì tìm đồ vừa chậm vừa dễ lẫn:

| Loại kệ trong kho | Cấu trúc Python | Đặc điểm |
|---|---|---|
| Kệ hàng đánh số thứ tự, lấy theo vị trí | `list` | Có thứ tự, truy cập bằng chỉ số, cắt lát được |
| Tủ có ngăn kéo dán nhãn | `dict` | Tra cứu theo **tên/khoá**, không quan tâm thứ tự lưu |
| Bao tải đổ chung, không đếm trùng | `set` | Tự động khử trùng lặp, so sánh thành viên rất nhanh |
| Hộp niêm phong không mở lại | `tuple` | Không đổi được sau khi tạo — dùng cho dữ liệu "cố định" |

Việc đầu tiên khi viết code xử lý dữ liệu không phải là "viết vòng lặp nào" mà là **"chọn đúng cái kệ"** — 80% code xử lý dữ liệu ngắn gọn tự nhiên đến từ việc chọn đúng cấu trúc ngay từ đầu.

## 1. Kiểu dữ liệu trong xử lý dữ liệu

### 1.1 Số và chuỗi: định dạng cho người đọc

Máy tính không quan tâm `1834567.891` có dễ đọc hay không, nhưng người đọc báo cáo thì có. F-string với đuôi định dạng là công cụ chuẩn:

```python
gia_tb = 1834567.891
ty_le_trong = 0.0734

# :,.0f  → phân cách hàng nghìn bằng dấu phẩy, 0 chữ số thập phân
# :.1%   → nhân 100, thêm dấu %, 1 chữ số thập phân
bao_cao = f"Giá TB: {gia_tb:,.0f} đ — tỷ lệ phòng trống: {ty_le_trong:.1%}"
print(bao_cao)
```
```text
Giá TB: 1,834,568 đ — tỷ lệ phòng trống: 7.3%
```

::: tip Hai đuôi định dạng phải nhớ nằm lòng
`:,.0f` (số nguyên có phân cách nghìn) và `:.1%` (phần trăm 1 chữ số thập phân) — xuất hiện lại liên tục từ bài 4 trở đi khi in kết quả `groupby`, KPI, báo cáo.
:::

### 1.2 `None` là một giá trị — không phải "không có gì"

**Trước → Sau: tính trung bình khi có dữ liệu thiếu**

| Bước | Trạng thái | Diễn giải |
|---|---|---|
| Trước | `gia = [1200000, None, 950000]` | Phòng thứ 2 không khai giá |
| Code | `sum(x for x in gia if x is not None) / 2` | Lọc bỏ `None` **trước** khi tính tổng, chia cho **số phần tử hợp lệ** (2), không phải độ dài gốc (3) |
| Sau | `1075000.0` | = (1.200.000 + 950.000) ÷ 2 |

::: danger Phân biệt bắt buộc: `None` ≠ `0` ≠ `""`
`None` nghĩa là **"không biết/chưa có giá trị"**; `0` là một số thực; `""` là một chuỗi rỗng — cả ba đều là giá trị hợp lệ nhưng mang ý nghĩa hoàn toàn khác nhau. Nếu bạn code `gia = gia or 0` để "xử lý dữ liệu thiếu", bạn đã **âm thầm biến "không biết" thành "miễn phí"**. Toàn bộ Bài 10 (xử lý giá trị thiếu) sẽ xây dựng trên đúng tính chất này.
:::

### 1.3 `list`: dãy có thứ tự — slicing (cắt lát)

```python
doanh_thu = [5, 8, 6, 9, 12, 11, 7]   # doanh thu 7 ngày liên tiếp (triệu đồng)

doanh_thu[0], doanh_thu[-1]           # phần tử đầu, phần tử cuối (chỉ số âm = đếm từ cuối)
```
```text
(5, 7)
```

```python
doanh_thu[1:4]     # slicing [bắt_đầu:kết_thúc) — lấy chỉ số 1, 2, 3 (KHÔNG lấy chỉ số 4)
```
```text
[8, 6, 9]
```

::: tip Vì sao học slicing kỹ ngay từ bây giờ?
Cú pháp `[bắt_đầu:kết_thúc:bước]` **giữ nguyên gần như 100%** khi sang NumPy array (Bài 3) và pandas `.iloc[]` (Bài 4–5). Hiểu chắc quy tắc "kết thúc không bao gồm" ở đây sẽ giúp không bị nhầm off-by-one (lệch 1) sau này.
:::

### 1.4 `dict`: một "dòng dữ liệu"

```python
phong = {"id": 52811, "gia": 1200000, "loai": "Entire home"}

phong["gia"]                      # tra theo khoá — lỗi KeyError nếu khoá không tồn tại
```
```text
1200000
```

```python
phong.get("diem", "chưa có")      # .get() có "phương án B" khi khoá không tồn tại — không bao giờ crash
```
```text
'chưa có'
```

::: info Bảng dữ liệu trong Python thuần
Một bảng có thể biểu diễn bằng **list các dict** — mỗi dict là một dòng. Đây là cách hình dung "tự nhiên" của một `DataFrame` trước khi học pandas ở Bài 4; nhìn theo hướng này giúp việc học `DataFrame` sau này bớt trừu tượng hơn.
:::

### 1.5 `set`: khử trùng lặp và so khớp cực nhanh

Bài toán: có hai snapshot ID phòng chụp ở hai thời điểm, phòng nào đã biến mất?

```python
thang_9  = {52811, 78230, 99182, 10021}
thang_12 = {52811, 99182, 33307}

thang_9 - thang_12       # phép trừ tập hợp: có ở T9 nhưng KHÔNG có ở T12
```
```text
{10021, 78230}
```

| Phép toán | Ký hiệu Python | Ý nghĩa dữ liệu |
|---|---|---|
| Hiệu | `a - b` | Có ở `a`, mất ở `b` (phòng "biến mất") |
| Giao | `a & b` | Có ở cả hai (phòng "còn tồn tại") |
| Hợp | `a \| b` | Toàn bộ ID xuất hiện ở ít nhất một trong hai |

### 1.6 Bảng quyết định: chọn cấu trúc nào?

| Bạn cần… | Dùng | Ví dụ trong môn |
|---|---|---|
| Dãy có thứ tự, cắt lát được | **list** | giá 7 ngày liên tiếp |
| Tra cứu theo tên/khoá | **dict** | một dòng dữ liệu, cấu hình pipeline |
| Khử trùng lặp, so thành viên | **set** | so ID phòng giữa hai snapshot |
| Bộ giá trị cố định, không đổi | **tuple** | toạ độ `(lat, lon)` |

## 2. Vòng lặp & Comprehension — bước đệm sang tư duy vector hoá

### 2.1 Cách viết "thủ công": `for` + `if`

```python
gia_tho = [1200000, -5, 950000, 0, 2400000]

gia_sach = []
for g in gia_tho:
    if g > 0:                 # quy tắc QA (quality assurance) đầu tiên: giá phải dương
        gia_sach.append(g)

print(gia_sach)
```
```text
[1200000, 950000, 2400000]
```

**Dry Run — chạy từng bước vòng lặp trên để thấy rõ trạng thái thay đổi:**

| Vòng lặp | `g` | Điều kiện `g > 0` | `gia_sach` sau bước này |
|---|---|---|---|
| khởi tạo | — | — | `[]` |
| 1 | `1200000` | True | `[1200000]` |
| 2 | `-5` | **False** | `[1200000]` (không đổi) |
| 3 | `950000` | True | `[1200000, 950000]` |
| 4 | `0` | **False** | `[1200000, 950000]` (không đổi) |
| 5 | `2400000` | True | `[1200000, 950000, 2400000]` |

### 2.2 Cách viết "cả dãy": Comprehension

```python
gia_sach = [g for g in gia_tho if g > 0]      # lọc

gia_trieu = [g / 1e6 for g in gia_sach]       # biến đổi CẢ DÃY cùng lúc, không lặp thủ công
print(gia_trieu)
```
```text
[1.2, 0.95, 2.4]
```

Cách đọc thành tiếng: *"lấy `g`, cho mỗi `g` trong dãy, với điều kiện…"*. Cùng kết quả với vòng lặp `for`, nhưng ngắn hơn, ít chỗ để gõ nhầm hơn (không quên `.append()`, không quên khởi tạo list rỗng).

::: tip  Trực giác quan trọng nhất của Bài 2
Comprehension **chưa phải** vectorization thật sự (bên dưới Python vẫn lặp từng phần tử) — nhưng nó tập cho bạn **thói quen tư duy đúng**: nghĩ về việc "biến đổi cả dãy" thay vì "xử lý từng phần tử". Bài 3 (NumPy) sẽ thay bước lặp ngầm này bằng phép toán mảng thật sự, nhanh hơn hàng chục lần vì được tính bằng code C đã biên dịch sẵn, không phải bytecode Python.
:::

**So sánh trực tiếp — vì sao đây là bước đệm quan trọng:**

| | `for` truyền thống | List comprehension | NumPy vector hoá (Bài 3) |
|---|---|---|---|
| Số dòng code | 3–4 dòng | 1 dòng | 1 dòng |
| Tốc độ trên 1 triệu phần tử | Chậm nhất | Nhanh hơn `for` một chút | **Nhanh hơn hàng chục lần** |
| Nguyên lý | Lặp + gọi `.append()` mỗi bước | Lặp ngầm, tối ưu hơn ở tầng interpreter | Không lặp ở tầng Python — thực thi bằng mảng C liên tục trong bộ nhớ |

### 2.3 `dict` comprehension & `zip`

```python
ten = ["Adelie", "Gentoo", "Chinstrap"]
so_luong = [152, 124, 68]

{t: n for t, n in zip(ten, so_luong)}   # zip ghép 2 dãy song song thành từng cặp (tên, số lượng)
```
```text
{'Adelie': 152, 'Gentoo': 124, 'Chinstrap': 68}
```

`zip` là công cụ thường dùng khi cần **ghép hai cột dữ liệu song song** — ý tưởng này lặp lại khi nối (`merge`) hai bảng ở Bài 5.

### 2.4 Cạm bẫy kinh điển: gán không phải là sao chép

```python
goc = [1, 2, 3]
ban_sao = goc          #  KHÔNG copy — chỉ tạo thêm một cái TÊN trỏ vào CÙNG một list
ban_sao.append(99)

print(goc)              # goc cũng bị đổi theo, dù ta chỉ động vào ban_sao!
```
```text
[1, 2, 3, 99]
```

::: danger Vì sao lỗi này nguy hiểm hơn vẻ ngoài của nó
`list`, `dict`, `set` trong Python là kiểu **mutable** (thay đổi được tại chỗ) và biến chỉ là một "tên" trỏ tới vùng nhớ, không phải bản thân dữ liệu. Muốn có bản sao thật sự độc lập, dùng `ban_sao = goc.copy()`. Đây **chính là gốc rễ** của lỗi "SettingWithCopyWarning" khét tiếng trong pandas (vấn đề *view vs copy*) mà bạn sẽ gặp lại ở Bài 4–5 — hiểu đúng ở đây sẽ tiết kiệm rất nhiều thời gian debug sau này.
:::

### 2.5 Khi nào dừng viết `for`?

::: warning Tín hiệu cần dừng lại và tự hỏi
Trong môn học này, cứ thấy mình viết `for` chạy qua **từng dòng dữ liệu số, hàng nghìn dòng trở lên**, hãy dừng lại và hỏi: *"Có công cụ thao tác cả-dãy nào (NumPy/pandas) làm được việc này không?"* Đề thi hay cho một đoạn code dùng `for` để cộng dồn một cột số hàng chục nghìn dòng và hỏi "cách nào tối ưu hơn" — câu trả lời luôn là vector hoá, không phải tối ưu vòng lặp.
:::

## 3. Hàm — đơn vị nhỏ nhất của một pipeline

### 3.1 Đóng gói một bước làm sạch thành hàm

Nhớ lại cột `price = "$45,647.00"` từ Bài 1 — đây là cách biến chuỗi đó thành số:

```python
def clean_price(s):
    """Đổi chuỗi giá kiểu '$45,647.00' thành float; đầu vào hỏng thì trả None."""
    try:
        # Bỏ ký tự '$' và dấu phân cách ',' rồi mới ép kiểu sang số thực
        return float(s.replace("$", "").replace(",", ""))
    except (ValueError, AttributeError):
        # ValueError: chuỗi còn lại không phải số hợp lệ (vd: "N/A")
        # AttributeError: đầu vào không phải chuỗi, ví dụ đã là None
        return None

clean_price("$45,647.00"), clean_price(None)
```
```text
(45647.0, None)
```

**Trước → Sau khi áp dụng `clean_price` lên cả một danh sách:**

| Trước (`str` hoặc `None`) | Sau (`float` hoặc `None`) |
|---|---|
| `"$1,200.00"` | `1200.0` |
| `"N/A"` | `None` |
| `"$950.00"` | `950.0` |

```python
gia_tho = ["$1,200.00", "N/A", "$950.00"]

list(map(clean_price, gia_tho))    # map: áp dụng MỘT hàm lên TỪNG phần tử của dãy
```
```text
[1200.0, None, 950.0]
```

### 3.2 Ba tiêu chuẩn của một hàm tốt trong pipeline dữ liệu

1. **Chỉ làm một việc** — thể hiện ngay trong tên hàm (`clean_price`, không đặt tên mơ hồ như `xu_ly`).
2. **Đoán được (predictable)** — cùng đầu vào luôn cho cùng đầu ra; không âm thầm sửa biến ở ngoài phạm vi hàm.
3. **Chịu được dữ liệu bẩn** — phải nói rõ đầu vào không hợp lệ sẽ trả về gì: `None`, hay chủ động phát sinh lỗi (`raise`).

Một docstring một dòng cộng với gợi ý kiểu dữ liệu nhẹ nhàng (`def clean_price(s) -> float | None:`) thường là đủ cho quy mô bài tập môn này.

### 3.3 `try/except`: bắt đúng loại lỗi, không bắt "tất cả"

```python
float("N/A")
```
```text
ValueError: could not convert string to float: 'N/A'
```

::: danger Bẫy nghiêm trọng nhất trong toàn bộ Bài 2 — cũng là bẫy AI hay mắc nhất
```python
#  SAI — che giấu MỌI loại lỗi, kể cả lỗi lập trình (gõ sai tên biến, sai kiểu tham số…)
try:
    ket_qua = clean_price(gia)
except Exception:
    pass    # pipeline "chạy được" nhưng âm thầm bỏ qua cả lỗi logic nghiêm trọng
```
Viết `except Exception: pass` khiến chương trình **không bao giờ báo lỗi** — kể cả khi bug nằm ở chính logic của bạn chứ không phải ở dữ liệu đầu vào. Hậu quả: pipeline "chạy xong, không lỗi" nhưng trả về kết quả sai mà không ai phát hiện ra cho đến khi quá muộn. Luôn bắt **đúng loại lỗi cụ thể** (`except ValueError`, `except (ValueError, AttributeError)`).
:::

### 3.4 Hàm là một giá trị — truyền được như mọi dữ liệu khác

```python
sorted(phong, key=lambda p: p["gia"], reverse=True)[0]   # lambda: hàm ẩn danh, dùng 1 lần
```

`lambda` chỉ nên gói gọn trong **một dòng**; logic dài hơn nên viết hàm có tên bằng `def` để dễ đọc, dễ kiểm thử. Mẫu "truyền hàm vào hàm khác" (`map(clean_price, ...)`) sẽ xuất hiện lại nguyên vẹn ở Bài 5 dưới dạng `df["price"].map(clean_price)`.

::: info Vì sao code xử lý dữ liệu có nhiều dấu chấm `.`?
Mọi giá trị trong Python là một **đối tượng**, luôn mang theo sẵn các phương thức của nó (`"abc".upper()`, `[1,2].append(3)`). Hãy tập đọc `df.groupby("city").mean()` như một **chuỗi lời gọi phương thức nối tiếp nhau**, mỗi dấu chấm là một bước biến đổi — chứ không phải một cú pháp "kỳ lạ" cần học thuộc lòng riêng lẻ.
:::

## 4. Đọc & ghi file

### 4.1 `with open`: đọc/ghi văn bản an toàn

```python
with open("ghi_chu.txt", encoding="utf-8") as f:
    noi_dung = f.read()
```

`with` tự động đóng file kể cả khi có lỗi phát sinh giữa chừng khi đang đọc/ghi. Tham số `encoding="utf-8"` phải **luôn được ghi rõ tường minh** — phần lớn lỗi "tiếng Việt vỡ chữ" (mojibake, ví dụ `Tiáº¿ng Viá»‡t`) đến từ việc quên tham số này và để hệ điều hành tự đoán bảng mã.

### 4.2 CSV thủ công — vì sao pandas ra đời

```python
import csv

with open("phong.csv", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

rows[0]
```
```text
{'id': '52811', 'gia': '$1,200.00', 'loai': 'Entire home'}
```

::: warning Quan sát quan trọng
**Mọi giá trị đọc từ CSV đều là chuỗi (`str`)** — kể cả `id` (một con số) cũng thành `'52811'`. Định dạng CSV **không lưu kiểu dữ liệu**; chương trình đọc phải tự chuyển kiểu bằng tay. Từ Bài 4, `pandas.read_csv()` sẽ tự động *suy luận* kiểu dữ liệu cho bạn — tiện lợi hơn hẳn, nhưng cũng chính vì suy luận tự động nên đôi khi sẽ **suy luận sai** (ví dụ đọc nhầm mã bưu điện `"07012"` thành số nguyên `7012`, mất số 0 đứng đầu).
:::

### 4.3 JSON: định dạng trao đổi giữa các chương trình

```python
import json

ket_qua = {"thanh_pho": "Santiago", "gia_tb": 45647.0}

with open("kq.json", "w", encoding="utf-8") as f:
    # ensure_ascii=False  → giữ nguyên tiếng Việt có dấu thay vì mã hoá \uXXXX
    # indent=2            → định dạng đẹp, dễ đọc bằng mắt thường
    json.dump(ket_qua, f, ensure_ascii=False, indent=2)

json.loads('{"gia_tb": 45647.0}')["gia_tb"]
```
```text
45647.0
```

Cấu trúc JSON tương ứng gần như trực tiếp với `dict`/`list` trong Python. Đây là định dạng phổ biến khi gọi API (Bài 6) và khi lưu tạm dữ liệu do LLM sinh ra (Bài 11).

### 4.4 `pathlib`: đường dẫn không phụ thuộc hệ điều hành

```python
from pathlib import Path

DATA = Path("data") / "raw" / "santiago"     # nối đường dẫn bằng '/' — hoạt động cả Windows lẫn macOS/Linux
DATA.mkdir(parents=True, exist_ok=True)      # parents=True: tự tạo cả thư mục cha nếu chưa có
                                              # exist_ok=True: không báo lỗi nếu thư mục đã tồn tại
sorted(DATA.parent.glob("*"))
```
```text
[PosixPath('data/raw/santiago')]
```

Cấu trúc thư mục kiểu `data/raw/<thanh_pho>/` — quy ước này sẽ được dùng lại xuyên suốt bài tập lớn Inside Airbnb.

##  Cheat Sheet — 7 điều phải nhớ của Bài 2

| # | Cú pháp / khái niệm | Ghi nhớ nhanh |
|---|---|---|
| 1 | `f"{x:,.0f}"` / `f"{x:.1%}"` | Định dạng số nghìn / phần trăm cho báo cáo |
| 2 | `lst[a:b]` | Cắt lát, lấy chỉ số `a` đến `b-1` (không bao gồm `b`) |
| 3 | `d.get(key, default)` | Tra `dict` an toàn, không lo `KeyError` |
| 4 | `a - b`, `a & b`, `a \| b` | Hiệu / giao / hợp giữa hai `set` |
| 5 | `[expr for x in seq if cond]` | Comprehension = lọc + biến đổi cả dãy trong 1 dòng |
| 6 | `x.copy()` | Bắt buộc khi cần bản sao độc lập của list/dict (tránh alias) |
| 7 | `except ValueError:` (không dùng `except Exception: pass`) | Chỉ bắt đúng loại lỗi đã lường trước |

## Tổng kết

- `None` là dữ liệu **thiếu**, khác `0` và `""`; `list`/`dict`/`set`/`tuple` — mỗi cấu trúc phục vụ một mục đích riêng biệt, chọn đúng ngay từ đầu giúp code ngắn và ít lỗi.
- Comprehension = tư duy "biến đổi cả dãy" — chưa nhanh bằng NumPy nhưng là bước đệm tư duy bắt buộc trước khi học vector hoá thật sự ở Bài 3.
- Một pipeline dữ liệu tốt = chuỗi các **hàm nhỏ, chịu được dữ liệu bẩn**, dùng `try/except` bắt đúng loại lỗi thay vì nuốt mọi lỗi.
- Đọc/ghi file: luôn `with` + `encoding="utf-8"`; CSV **không** mang theo kiểu dữ liệu (mọi thứ đều là chuỗi), JSON thì tương ứng gần như trực tiếp với `dict`/`list`.

##  Mẹo thi & bẫy thường gặp

::: warning Câu hỏi hay xuất hiện trong đề
- **"`b = a.copy()` và `b = a` cho kết quả giống nhau nếu sau đó không sửa gì"** → Đúng về mặt giá trị ban đầu, nhưng **SAI về bản chất**: `b = a` khiến `a` và `b` cùng trỏ một vùng nhớ; chỉ cần sửa `b` ở bất kỳ đâu sau đó, `a` cũng đổi theo. Đề thi hay cho code sửa `b` rồi hỏi giá trị của `a`.
- **"CSV lưu số thì đọc ra sẽ là số"** → SAI, `csv.DictReader` luôn trả về **chuỗi** cho mọi cột, kể cả cột toàn số.
- **"`except Exception: pass` là cách an toàn để code không bao giờ crash"** → SAI, đây là bẫy nguy hiểm nhất bài — nó che giấu cả lỗi logic, khiến pipeline âm thầm sai mà không báo động.
- **Dry-run vòng lặp `for` với điều kiện lồng nhau**: đề hay cho một vòng `for` + `if` + `append` và yêu cầu viết ra list kết quả cuối — cách chắc ăn nhất là kẻ bảng dry-run như mục 2.1 ở trên, đừng tính nhẩm.
:::

##  Đọc thêm & tài nguyên

- McKinney, *Python for Data Analysis*, 3rd ed. — chương 2–3 (ôn Python built-ins, miễn phí tại [wesmckinney.com/book](https://wesmckinney.com/book/)).
- [Python Official Tutorial — Data Structures](https://docs.python.org/3/tutorial/datastructures.html) — list/dict/set/tuple, comprehension.
- [Python Official Tutorial — Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html) — cách bắt đúng loại lỗi.
- [Real Python — Python's `with` Statement](https://realpython.com/python-with-statement/) — hiểu sâu vì sao `with` an toàn hơn `open()`/`close()` thủ công.
-  Tự học OOP (chưa cần gấp): *Official Python Tutorial*, mục [Classes](https://docs.python.org/3/tutorial/classes.html) — cần khi đọc code nguồn thư viện, chưa cần để dùng pandas ở mức cơ bản.

::: info  Làm việc với AI thì sao?
**AI làm tốt:** tạo nhanh các hàm tiện ích cho thao tác chuẩn (như `clean_price`).
**AI hay sai:** có xu hướng dùng `except Exception: pass` để code "chạy được bằng mọi giá"; hay quên `encoding="utf-8"`; code đúng với đúng ví dụ bạn đưa ra nhưng sai với các ca biên (giá âm, chuỗi rỗng, `None`).
**Kiểm chứng bằng cách nào:** đưa hàm AI viết qua một **bộ ca thử tự nghĩ ra**: giá trị bình thường, rỗng, `None`, âm, sai định dạng — rồi yêu cầu chính AI liệt kê thêm các đầu vào có thể làm hàm sai, và tự tay kiểm tra từng trường hợp đó.
:::
