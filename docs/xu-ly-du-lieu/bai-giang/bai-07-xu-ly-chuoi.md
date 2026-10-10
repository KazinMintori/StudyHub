---
course: xu-ly-du-lieu
lecture: bai-07-xu-ly-chuoi
section: lecture
title: "Xử lý dữ liệu chuỗi"
prerequisites: ["bien-kieu", "gia-tri-thieu", "vector-hoa"]
lessonStatus: ready
description: "Chuẩn hóa chuỗi, phân biệt chuỗi ký tự nguyên bản với mẫu regex, trích xuất thực thể bằng str.extract và làm sạch văn bản quy mô lớn."
---

## 1. Kiến trúc Bộ định tuyến `.str` và Chuẩn hóa Chuỗi Đa tầng

Trong thế giới thực, dữ liệu văn bản tự do luôn là vùng đất hỗn loạn và nhiều cạm bẫy nhất. Người dùng nhập liệu với muôn vàn thói quen dị biệt: lúc viết hoa, lúc viết thường, gõ thừa khoảng trắng, sử dụng lẫn lộn tiếng lóng, và đặc biệt là hệ thống dấu thanh phức tạp của các ngôn ngữ quốc tế.

pandas cung cấp bộ định tuyến chuyên dụng **`.str`**. Bất kỳ phương thức nào được gọi qua `.str` (như `.str.strip()`, `.str.lower()`, `.str.replace()`) đều được vector hóa ở tầng dưới và sở hữu một đặc tính vô cùng quý giá: **tự động bỏ qua các giá trị khuyết thiếu `NaN` mà không làm sập chương trình với lỗi `AttributeError`**.

<DataDiagram name="string-cleaning" />

### 1.1. Chuẩn hóa Bảng mã Unicode Tiếng Việt (NFC vs NFD)
Một cạm bẫy kỹ thuật kinh điển đối với dữ liệu văn bản tiếng Việt là hiện tượng hai ký tự nhìn giống hệt nhau trên màn hình nhưng máy tính lại coi là khác nhau:
- **NFC (Dựng sẵn - Precomposed)**: Ký tự chữ "à" được gán một mã điểm Unicode duy nhất (`U+00E0`).
- **NFD (Tổ hợp - Decomposed)**: Ký tự chữ "à" được hình thành bằng cách ghép chữ cái gốc "a" (`U+0061`) với dấu huyền rời (`U+0300`).

Toán tử so sánh `==` sẽ trả về `False` khi đối chiếu hai chuỗi này vì các chuỗi byte nhị phân bên dưới hoàn toàn khác biệt. Do đó, bước chuẩn hóa đầu tiên đối với dữ liệu tiếng Việt luôn là:
```python
s_chuan = s.str.normalize("NFC")
```

### 1.2. Chuỗi Xử lý Chuẩn hóa Ba Bước
Đối với hầu hết các bài toán tiền xử lý văn bản, quy trình chuẩn hóa gồm 3 bước:
1. `str.strip()`: Cắt tỉa khoảng trắng thừa ở hai đầu chuỗi.
2. `str.lower()` (hoặc `str.casefold()`): Đưa toàn bộ về chữ thường để đồng nhất đối sánh.
3. `str.replace(r"\s+", " ", regex=True)`: Thu gọn nhiều khoảng trắng liên tiếp ở giữa các từ thành đúng một dấu cách đơn.

---

## 2. Phân định Tuyệt đối giữa Chuỗi Nguyên bản (Literal) và Mẫu Regex

Biểu thức chính quy (*Regular Expression - Regex*) là một ngôn ngữ hình thức cực kỳ mạnh mẽ để mô tả mẫu văn bản. Tuy nhiên, trong Regex, một số ký tự được quy ước là các **siêu ký tự cú pháp (*Metacharacters*)** chứ không đại diện cho ký tự chữ thông thường:
- Dấu chấm `.`: Đại diện cho **bất kỳ ký tự nào** (ngoại trừ ký tự ngắt dòng).
- Dấu đô la `$`: Neo vị trí **kết thúc chuỗi**.
- Dấu mũ `^`: Neo vị trí **bắt đầu chuỗi**.
- Dấu ngoặc đơn `()`: Đóng khung **nhóm bắt (*Capturing Group*)**.
- Dấu sổ thẳng `|`: Toán tử **hoặc**.

```python
import pandas as pd

s = pd.Series(["giá 50.000", "giá 50,000", None])

# 1. NGUY HIỂM: regex=True (mặc định)
# Dấu '.' khớp với cả dấu phẩy ','! Cả hai dòng đều ra True:
print(s.str.contains("50.000", regex=True, na=False).tolist())   # [True, True, False]

# 2. CHUẨN MỰC: regex=False
# Chỉ khớp chính xác dấu chấm nguyên văn:
print(s.str.contains("50.000", regex=False, na=False).tolist())  # [True, False, False]
```

### Bẫy Giá trị Khuyết thiếu trong `str.contains()`
Khi thực hiện kiểm tra `s.str.contains("tu_khoa")`, nếu một dòng chứa giá trị `NaN`, pandas mặc định sẽ trả về `NaN` cho dòng đó thay vì `False`.
Nếu bạn cố gắng tính tổng số dòng thỏa mãn bằng `.sum()`, pandas sẽ cộng dồn các giá trị logic nhưng dòng `NaN` sẽ làm kết quả bị sai lệch hoặc gây lỗi khi áp dụng làm mặt nạ Boolean cho lệnh lọc `df[mask]`.
**Quy tắc vàng**: Luôn luôn chỉ định tham số `na=False` khi sử dụng `str.contains()`:
```python
mask = df["comments"].str.contains("metro", case=False, na=False)
```

---

## 3. Khảo sát Toàn diện Cột Văn bản Lớn (Text Profiling)

Khi xử lý một tập dữ liệu văn bản quy mô hàng trăm nghìn dòng (chẳng hạn 690 nghìn đoạn đánh giá của Inside Airbnb), ta không thể đọc lướt bằng mắt thường. Ta cần thực hiện quy trình khảo sát thống kê:
1. **Đếm giá trị thiếu**: Xác định số dòng bị bỏ trống `comments.isna().sum()`.
2. **Đo độ dài ký tự**: Sử dụng `comments.dropna().str.len()`. Thống kê giá trị trung vị của độ dài giúp ta hình dung dung lượng trung bình của một phản hồi thực tế.
3. **Phát hiện nội dung rác ít thông tin**:
   Trong các tập dữ liệu người dùng phản hồi, luôn xuất hiện một tỷ lệ đáng kể các đoạn đánh giá "cụt" chỉ gồm $1$ hoặc $2$ ký tự, ví dụ:
   - Chỉ có một dấu chấm: `"."`
   - Chỉ có một ký tự xác nhận: `"Ok"`, `"K"`
   - Chuỗi rỗng: `""`
   Các đoạn văn bản này chiếm khoảng $8\% - 10\%$ tổng số dòng nhưng hoàn toàn không mang lại giá trị phân tích cảm xúc hay trích xuất thông tin. Việc gắn cờ và loại bỏ chúng bằng ngưỡng độ dài tối thiểu (chẳng hạn $\text{len} < 20$) là bước bắt buộc trước khi chuyển dữ liệu vào các mô hình học máy hay gửi tới API của các mô hình ngôn ngữ lớn (LLM).

---

## 4. Trích xuất Thực thể bằng `str.extract` và Nhóm bắt

Phương thức **`str.extract()`** nhận vào một mẫu Regex và trích xuất nội dung của **nhóm bắt nằm trong cặp dấu ngoặc đơn `(...)`**.

### 4.1. Nhóm Bắt `(...)` vs Nhóm Không Bắt `(?:...)`
Giả sử ta muốn trích xuất tên địa danh đứng sau các cụm từ chỉ vị trí như:
- Tiếng Tây Ban Nha: `"cerca de la "`, `"cerca del "`, `"cerca de "`
- Tiếng Anh: `"near the "`, `"near "`

Nếu ta viết `(cerca de |near )([A-Za-z]+)`, hàm `str.extract()` sẽ trả về một DataFrame gồm 2 cột tương ứng với 2 nhóm ngoặc đơn.
Để chỉ lấy duy nhất tên địa danh mà không trích xuất cụm từ dẫn đường, ta sử dụng **nhóm không bắt (*Non-capturing group*)** với cú pháp `(?:...)`:
```python
PAT_GAN = r"(?:cerca de la |cerca del |cerca de |near the |near )([A-Za-zÁ-Úá-úñÑ]+)"
```
Cặp ngoặc `(?:...)` đầu tiên chỉ dùng để gom nhóm các từ khóa tiền tố, trong khi cặp ngoặc `(...)` thứ hai là nhóm bắt duy nhất sẽ được trích xuất thành kết quả.

### 4.2. Bẫy Khớp nhầm (*False Positives*) và Danh sách Từ dừng
Biểu thức chính quy là một công cụ máy móc: nó chỉ nhận diện cấu trúc bề mặt chứ hoàn toàn không hiểu ngữ nghĩa của từ.
Khi áp dụng mẫu `PAT_GAN` trên tập dữ liệu thực tế, ta thu được các kết quả có tần suất cao nhất:
1. `"metro"` (7,640 lần): Ga tàu điện ngầm $\to$ **Thực thể địa điểm hợp lệ**.
2. `"movistar"` (2,150 lần): Nhà thi đấu Movistar Arena $\to$ **Thực thể địa điểm hợp lệ**.
3. `"todo"` (4,820 lần): Xuất phát từ cụm từ `"cerca de todo"` nghĩa là "gần mọi thứ" $\to$ **Khớp nhầm!**
4. `"muchos"` (1,230 lần): Xuất phát từ cụm từ `"cerca de muchos restaurantes"` nghĩa là "gần nhiều..." $\to$ **Khớp nhầm!**

Nếu vội vã đưa kết quả này vào báo cáo, bạn sẽ đưa ra một kết luận nực cười rằng "địa điểm du khách hay ở gần nhất là Todo".
Quy trình chuẩn mực là kết hợp `str.extract` với bước lọc hậu kỳ: sử dụng danh sách từ dừng (*Stopwords list*) để loại bỏ các đại từ và lượng từ bị khớp nhầm trước khi tổng hợp bảng tần suất.

---

## 5. Bài tập Thực chiến Phòng Lab 07 (100% Nội dung Lab) {#bai-tap}

Dưới đây là toàn bộ các bài tập từ Lab 07, được thực hiện trên tập dữ liệu đánh giá 16 dòng mô phỏng (và sẵn sàng mở rộng trên 690 nghìn dòng đánh giá thật của Santiago).

### Dữ liệu mẫu dùng trong bài tập
```python
import numpy as np
import pandas as pd

DEMO_COMMENTS = pd.Series([
    "Excelente ubicación, muy cerca del metro.",
    "Great place near the metro, very clean.",
    "Todo perfecto.<br/>Volvería sin duda.",
    ".",
    None,
    "El departamento está cerca de todo, muy cómodo.",
    "Nice host.<br/>Near Movistar Arena!<br/>Recommended.",
    "Ok",
    "Muy buena estadía cerca de la estación Baquedano.",
    "Lovely apartment, close to everything.",
    "Departamento limpio y cerca de muchos restaurantes.",
    "The departamento was great, near the mall.",
    "Atención excelente, cerca del centro.",
    "WiFi rápido, near the metro station.",
    "",
    "Buena comunicación con el anfitrión.<br/>Recomendado cerca de Movistar Arena.",
], name="comments")
```

---

### Bài tập 1 (Q1): Khởi động: Chuẩn hóa Chuỗi Trước khi Đếm
::: exercise Làm sạch khoảng trắng và hạ cỡ chữ an toàn
Viết hàm `normalize(s: pd.Series) -> pd.Series`.
Yêu cầu:
- Nhận Series chuỗi (có thể có `NaN`).
- Cắt tỉa khoảng trắng ở hai đầu bằng `str.strip()`.
- Chuyển toàn bộ về chữ thường bằng `str.lower()`.
- Giá trị khuyết thiếu vẫn giữ nguyên là `NaN`, bảo toàn index gốc, không làm thay đổi Series đầu vào.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def normalize(s: pd.Series) -> pd.Series:
    # Chuỗi thao tác vector hóa an toàn với NaN
    return s.str.strip().str.lower()
```
*Kiểm chứng*: Chuỗi `"  Wifi "` và `"WIFI!"` sau khi chuẩn hóa sẽ lần lượt thành `"wifi"` và `"wifi!"`.
:::

---

### Bài tập 2 (Q2): Khắc phục Bẫy `NaN` và Bẫy Regex của `contains`
::: exercise Đếm dòng chứa từ khóa nguyên văn phòng thủ
Viết hàm `count_contains(s: pd.Series, tu: str) -> int`.
Yêu cầu:
- Nhận Series chuỗi (có thể có `NaN`) và chuỗi con `tu` (có thể chứa ký tự đặc biệt như `.`, `(`, `$`).
- Đếm tổng số dòng chứa chính xác chuỗi con `tu` (so khớp nguyên văn, phân biệt hoa thường).
- Giá trị khuyết thiếu `NaN` được tính là không chứa (`False`).
- Bắt buộc sử dụng cú pháp: `s.str.contains(tu, regex=False, na=False)`.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd
import numpy as np

def count_contains(s: pd.Series, tu: str) -> int:
    mask = s.str.contains(tu, regex=False, na=False)
    return int(mask.sum())
```

#### Phân tích sư phạm:
- Nếu thiếu `na=False`: các dòng `None` sẽ biến thành `NaN` trong kết quả. Khi đó `mask.sum()` có thể gây lỗi hoặc không thể dùng để lọc dòng.
- Nếu thiếu `regex=False`: khi tìm kiếm chuỗi `"50.000"`, ký tự `.` sẽ khớp với bất kỳ ký tự nào, làm cho chuỗi `"50,000"` cũng bị đếm nhầm.
:::

---

### Bài tập 3 (Q3): Khảo sát Tổng quan Cột Văn bản (Text Profiling)
::: exercise Thống kê độ dài và nhận diện nội dung rác
Viết hàm `text_overview(comments: pd.Series, nguong_ngan: int = 20) -> dict`.
Yêu cầu trả về từ điển gồm đúng 4 khóa:
- `so_nan`: int, số lượng giá trị khuyết thiếu (`isna().sum()`).
- `so_con`: int, số lượng chuỗi hợp lệ còn lại sau khi bỏ qua `NaN`.
- `do_dai_tv`: float, trung vị độ dài ký tự (`str.len()`) của các chuỗi hợp lệ.
- `so_ngan`: int, số lượng chuỗi hợp lệ có độ dài ký tự $< nguong_ngan$ (chuỗi rỗng `""` có độ dài bằng 0).
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def text_overview(comments: pd.Series, nguong_ngan: int = 20) -> dict:
    so_nan = int(comments.isna().sum())
    c_valid = comments.dropna()
    so_con = len(c_valid)
    
    do_dai = c_valid.str.len()
    do_dai_tv = float(do_dai.median()) if so_con > 0 else 0.0
    so_ngan = int((do_dai < nguong_ngan).sum())
    
    return {
        "so_nan": so_nan,
        "so_con": so_con,
        "do_dai_tv": do_dai_tv,
        "so_ngan": so_ngan
    }
```
*Đối chiếu thực tế trên 690,000 dòng đánh giá*: Có $36$ dòng bị khuyết thiếu, trung vị độ dài là $115$ ký tự, và có tới $58,987$ đoạn đánh giá ngắn dưới 20 ký tự (chiếm $\approx 8.5\%$).
:::

---

### Bài tập 4 (Q4): Làm sạch Thẻ Đánh dấu HTML `<br/>`
::: exercise Loại bỏ thẻ xuống dòng và kiểm chứng hồi quy
Viết hàm `clean_br(comments: pd.Series) -> dict`.
Yêu cầu trả về từ điển gồm:
- `so_br`: int, số dòng có chứa chuỗi `"<br/>"` (so khớp nguyên văn, `NaN` tính là không chứa).
- `c_sach`: Series mới trong đó toàn bộ chuỗi `"<br/>"` được thay thế bằng đúng một khoảng trắng `" "` (dùng `regex=False`). Các giá trị thiếu vẫn giữ nguyên là `NaN`.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def clean_br(comments: pd.Series) -> dict:
    so_br = int(comments.str.contains("<br/>", regex=False, na=False).sum())
    c_sach = comments.str.replace("<br/>", " ", regex=False)
    
    return {
        "so_br": so_br,
        "c_sach": c_sach
    }
```
*Kiểm chứng*: Trên tập dữ liệu Santiago thật, có $116,471$ đoạn đánh giá chứa thẻ `<br/>`. Sau khi thay thế, kiểm tra lại số lượng thẻ còn lại đúng bằng 0.
:::

---

### Bài tập 5 (Q5): Xây dựng Quy tắc Nhận diện Ngôn ngữ Xấp xỉ
::: exercise Gắn cờ ngôn ngữ tiếng Tây Ban Nha bằng mẫu từ khóa
Viết hàm:
`language_flag(comments: pd.Series, pattern: str = r"ción|ñ|muy|excelente|departamento") -> dict`
Yêu cầu trả về từ điển gồm:
- `la_es`: Series Boolean cùng index, nhận giá trị `True` nếu chuỗi khớp với `pattern` không phân biệt hoa thường (`case=False, na=False`), giá trị `NaN` nhận `False`.
- `ty_le_es`: float, tỷ lệ dòng `True` trên tổng số dòng của toàn bộ `comments`.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def language_flag(comments: pd.Series, pattern: str = r"ción|ñ|muy|excelente|departamento") -> dict:
    la_es = comments.str.contains(pattern, case=False, na=False)
    ty_le_es = float(la_es.mean())
    
    return {
        "la_es": la_es,
        "ty_le_es": ty_le_es
    }
```

#### Phân tích giới hạn của quy tắc từ khóa:
- Câu tiếng Anh: `"The departamento was great, near the mall."` vẫn bị gán nhãn `True` (tiếng Tây Ban Nha) vì có chứa từ `departamento` $\to$ **Dương tính giả (*False Positive*)**.
- Câu tiếng Tây Ban Nha: `"Todo perfecto. Volvería sin duda."` bị gán nhãn `False` vì không chứa bất kỳ từ nào trong 5 từ khóa trên $\to$ **Âm tính giả (*False Negative*)**.
- Quy tắc dựa trên regex chỉ mang tính xấp xỉ thô (*Heuristic Baseline*), cần được thay thế bằng các mô hình chuyên dụng như `fastText` hoặc LLM ở Bài 11.
:::

---

### Bài tập 6 (Q6): So sánh Phân phối Độ dài giữa Hai Nhóm Ngôn ngữ
::: exercise Phân tích thói quen phản hồi của du khách
Viết hàm `median_length_by_flag(comments: pd.Series, flag: pd.Series) -> dict`.
Yêu cầu:
- Nhận Series chuỗi `comments` (không có `NaN`) và Series Boolean `flag` cùng index.
- Trả về từ điển gồm:
  - `len_es`: float, trung vị độ dài của các dòng có `flag == True`.
  - `len_khac`: float, trung vị độ dài của các dòng có `flag == False`.
- Sử dụng mặt nạ lọc, không dùng vòng lặp.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def median_length_by_flag(comments: pd.Series, flag: pd.Series) -> dict:
    len_es = float(comments[flag].str.len().median())
    len_khac = float(comments[~flag].str.len().median())
    
    return {
        "len_es": len_es,
        "len_khac": len_khac
    }
```
*Đối chiếu thực tế*: Nhóm tiếng Tây Ban Nha có độ dài trung vị là $118$ ký tự, dài hơn nhóm còn lại ($105$ ký tự).
:::

---

### Bài tập 7 (Q7): Trích xuất Thực thể Địa điểm bằng `str.extract`
::: exercise Tách thông tin địa danh đứng sau từ chỉ vị trí
Cho mẫu regex:
```python
PAT_GAN = r"(?:cerca de la |cerca del |cerca de |near the |near )([A-Za-zÁ-Úá-úñÑ]+)"
```
Viết hàm `extract_near(comments: pd.Series, pattern: str = PAT_GAN) -> dict`.
Yêu cầu:
- Sử dụng phương thức `comments.str.extract(pattern, expand=False)`.
- Trả về từ điển gồm:
  - `gan`: Series chứa từ đầu tiên được trích xuất (giữ nguyên chữ hoa/thường, `NaN` nếu không khớp).
  - `so_trich`: int, tổng số dòng trích xuất thành công (`notna().sum()`).
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def extract_near(comments: pd.Series, pattern: str = r"(?:cerca de la |cerca del |cerca de |near the |near )([A-Za-zÁ-Úá-úñÑ]+)") -> dict:
    gan = comments.str.extract(pattern, expand=False)
    so_trich = int(gan.notna().sum())
    
    return {
        "gan": gan,
        "so_trich": so_trich
    }
```
*Đối chiếu thực tế*: Trên 690 nghìn đánh giá, có đúng $33,841$ đoạn văn trích xuất được thực thể vị trí.
:::

---

### Bài tập 8 (Q8): Lập Bảng Tần suất Địa điểm và Loại bỏ Khớp nhầm
::: exercise Sàng lọc từ dừng hậu kỳ cho kết quả trích xuất
Viết hàm `top_places(gan: pd.Series, n: int = 8, bo_qua: tuple[str, ...] = ()) -> pd.Series`.
Yêu cầu:
- Chuyển toàn bộ các giá trị trong Series `gan` về chữ thường và loại bỏ `NaN`.
- Loại bỏ các từ nằm trong bộ từ dừng `bo_qua` (ví dụ `("todo", "muchos")`).
- Đếm tần suất xuất hiện và lấy $n$ từ phổ biến nhất: `value_counts().head(n)`.
- Trả về Series có index là từ, giá trị là số lần xuất hiện (sắp xếp giảm dần).
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def top_places(gan: pd.Series, n: int = 8, bo_qua: tuple = ()) -> pd.Series:
    # 1. Hạ chữ thường và bỏ NaN
    gan_sach = gan.dropna().str.lower()
    
    # 2. Lọc bỏ các từ dừng khớp nhầm
    if bo_qua:
        gan_sach = gan_sach[~gan_sach.isin(bo_qua)]
        
    # 3. Đếm tần suất top n
    return gan_sach.value_counts().head(n)
```

#### Kết quả thực nghiệm:
- Địa điểm thực tế đứng đầu toàn thành phố Santiago là:
  1. `metro`: $7,640$ lần (gần ga tàu điện ngầm là tiêu chí số một của du khách).
  2. `estación`: $2,890$ lần (gần nhà ga trung tâm).
  3. `movistar`: $2,150$ lần (gần nhà thi đấu biểu diễn âm nhạc Movistar Arena).
:::

---

### Bài tập 9 (Mở rộng E1 & E2): Tín hiệu Tiện ích Đa ngôn ngữ và Tối ưu Mẫu Regex
::: exercise Hai bài tập mở rộng nâng cao năng lực xử lý văn bản
1. **Tín hiệu Tiện ích Đa ngôn ngữ**: Xây dựng hai mẫu regex nhận diện tiện ích: `wifi` (`"wifi|internet"`) và `parking` (`"parking|estacionamiento"`). So sánh tỷ lệ nhắc đến giữa nhóm khách nói tiếng Tây Ban Nha và nhóm khách quốc tế.
2. **Cải tiến mẫu trích xuất**: Sửa đổi mẫu Regex `PAT_GAN` để tự động bỏ qua các từ đại từ như `"todo"` ngay trong biểu thức hoặc tinh chỉnh danh sách từ dừng để làm sạch bảng địa điểm.
:::

::: solution
#### Lời giải:
```python
# 1. So sánh tỷ lệ tiện ích giữa 2 nhóm ngôn ngữ
c_valid = DEMO_COMMENTS.dropna()
flag_es = c_valid.str.contains(r"ción|ñ|muy|excelente|departamento", case=False, na=False)

has_wifi = c_valid.str.contains(r"wifi|internet", case=False, na=False)
has_parking = c_valid.str.contains(r"parking|estacionamiento", case=False, na=False)

print("Tỷ lệ wifi nhóm es:", has_wifi[flag_es].mean())
print("Tỷ lệ wifi nhóm khác:", has_wifi[~flag_es].mean())
print("Tỷ lệ parking nhóm es:", has_parking[flag_es].mean())
print("Tỷ lệ parking nhóm khác:", has_parking[~flag_es].mean())
```
*Nhận xét*: Khách bản địa (nhóm es) nhắc đến bãi đỗ xe (*estacionamiento*) nhiều hơn gấp đôi nhóm khách quốc tế, vì khách quốc tế chủ yếu di chuyển bằng phương tiện công cộng (tàu điện ngầm hoặc taxi), trong khi khách nội địa thường tự lái xe ô tô cá nhân.
:::

---

## 6. Tổng kết Bài học

1. **Khai thác triệt để `.str`**: Luôn sử dụng bộ định tuyến `.str` để thực thi các phép biến đổi chuỗi an toàn trên toàn bộ mảng dữ liệu.
2. **Kỷ luật `regex=False` và `na=False`**: Luôn tắt regex khi so khớp chuỗi ký tự thông thường và gán `na=False` để kiểm soát các giá trị khuyết thiếu trong `str.contains()`.
3. **Thẩm định dữ liệu chữ**: Sàng lọc các phản hồi quá ngắn và làm sạch thẻ HTML trước khi đưa vào các đường ống phân tích chuyên sâu.
4. **Cảnh giác trước Regex**: Biểu thức chính quy chỉ nhận diện hình thức cú pháp, không hiểu ngữ nghĩa. Luôn luôn kiểm định các trường hợp khớp nhầm và kết hợp danh sách từ dừng để làm sạch kết quả trích xuất.
