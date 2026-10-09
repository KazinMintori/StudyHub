---
course: xu-ly-du-lieu
lecture: bai-04-lam-quen-pandas
section: lecture
title: "Làm quen với pandas"
prerequisites: ["chi-muc", "dictionary", "gia-tri-thieu"]
lessonStatus: ready
description: "Dựng Series và DataFrame, thói quen 5 bước khám phá dữ liệu, lọc chọn chuẩn mực bằng .loc, bẫy gán hai lần ngoặc và lập hồ sơ phân tích thị trường."
---

::: info Mục tiêu bài học
- Thấu suốt hai cấu trúc nền tảng của pandas: `Series` và `DataFrame`, phân biệt rạch ròi giữa trích xuất cột một chiều `df["col"]` và trích xuất bảng con hai chiều `df[["col"]]`.
- Thành thạo "Thói quen 5 bước" khám phá dữ liệu ban đầu (`shape`, `sample`, `info`, `describe`, `value_counts`), rèn luyện phản xạ đọc và diễn giải các số liệu thực tế thay vì chỉ thực thi lệnh máy móc.
- Làm chủ kỹ thuật lọc chọn dữ liệu bằng mặt nạ Boolean nhiều điều kiện (`&`, `|`, `~`), tra cứu cực trị bằng `nsmallest` và phân biệt rạch ròi giữa `df[mask]` với `df.loc[mask, "col"]`.
- Nhận diện bản chất cơ chế Copy-on-Write (CoW) trong pandas 3, loại bỏ hoàn toàn bẫy gán hai lần ngoặc (*Chained Indexing*) và nắm vững nguyên lý: cột trong DataFrame lưu trữ giá trị đã tính, không tự động cập nhật như công thức bảng tính Excel.
- Phân tích tác động của giá trị khuyết thiếu `NaN` lên mẫu số khi tính tỷ lệ, hoàn thành trọn vẹn 100% bài tập thực hành Lab 4 lập hồ sơ phân tích thị trường một quận.
:::

---

## 1. Bản chất Cấu trúc: Series, DataFrame và Hệ thống Nhãn (Index)

Khi làm việc với các bài toán thực tế, dữ liệu hiếm khi chỉ tồn tại dưới dạng những con số vô danh. Dữ liệu thực luôn đi kèm ngữ nghĩa phong phú: cột nào là định danh khách hàng, cột nào là giá niêm yết, hàng nào thuộc về quận nào, và làm sao để xử lý những quan sát bị bỏ trống mà không làm gãy vỡ cấu trúc tính toán?

Năm 2008, Wes McKinney đã phát triển **pandas** nhằm mang lại cho Python một cấu trúc dữ liệu dạng bảng có nhãn (*Labeled Tabular Data*) sánh ngang với ngôn ngữ R hay cơ sở dữ liệu quan hệ SQL.

```
                     +---------------------------------------+
                     |           DATAFRAME (2D)              |
                     |  Tập hợp các cột Series chung Index   |
                     +---------------------------------------+
                     |  name              price    room_type |  <- Cột (Columns)
        +------------+---------------------------------------+
Index   | 0 (id 101) | Depto Plaza Ñuñoa  45000.0  Entire    |
(Nhãn   | 1 (id 102) | Pieza cerca metro  18000.0  Private   |
hàng)   | 2 (id 103) | Loft Irarrázaval   72000.0  Entire    |
        +------------+---------------------------------------+
                             |
                             v Trích xuất 1 cột: df["price"]
                     +-------------------+
                     |    SERIES (1D)    |
                     +-------------------+
        Index (Nhãn) | 0 -> 45000.0      |  (Mảng dữ liệu 1D
                     | 1 -> 18000.0      |   gắn liền mảng nhãn)
                     | 2 -> 72000.0      |
                     +-------------------+
```

### 1.1. Series vs DataFrame: Cú pháp Một Ngoặc vs Hai Ngoặc
Hai cấu trúc cốt lõi của pandas:
- **`Series`**: Mảng 1 chiều có nhãn, là khối xây dựng cơ bản của từng cột dữ liệu.
- **`DataFrame`**: Bảng 2 chiều hình chữ nhật gồm nhiều Series ghép lại, có chung trục chỉ mục hàng (`index`) và danh sách tên cột (`columns`).

Hãy quan sát sự khác biệt tinh tế giữa hai cú pháp trích xuất cột:
```python
import pandas as pd

# 1. Một cặp ngoặc vuông: Trả về Series 1 chiều
cot_gia = df["price"]
print(type(cot_gia))  # <class 'pandas.core.series.Series'>

# 2. Hai cặp ngoặc vuông (truyền vào một list tên cột): Trả về DataFrame 2 chiều
bang_con = df[["price"]]
print(type(bang_con))  # <class 'pandas.core.frame.DataFrame'>
```
Việc nhầm lẫn giữa Series và DataFrame 1 cột là nguồn gốc của rất nhiều lỗi cú pháp khi gọi các hàm xử lý tiếp theo. Khi cần thao tác trên vector giá trị (như tính toán trung bình, kiểm tra điều kiện logic), ta dùng Series. Khi cần trích xuất một tập con các trường dữ liệu để ghép bảng hoặc xuất tệp, ta dùng DataFrame với danh sách cột.

---

## 2. Thói quen 5 Bước Khám phá Dữ liệu (The 5-Step Exploration Habit)

Khi tiếp nhận một tệp dữ liệu mới (chẳng hạn tệp `listings.csv` từ Inside Airbnb), người kỹ sư dữ liệu không bao giờ vội vã đưa dữ liệu vào huấn luyện mô hình hay vẽ biểu đồ ngay lập tức. Ta bắt buộc phải thực hiện quy trình "khám sức khỏe sơ bộ" gồm 5 bước kỷ luật:

### Bước 1: Kiểm tra Kích thước Không gian với `df.shape`
Lệnh `df.shape` trả về tuple `(số_hàng, số_cột)`. Cho ta biết quy mô tổng thể của mẫu dữ liệu mà không tốn tài nguyên in toàn bộ bảng ra màn hình.

### Bước 2: Quan sát Bản ghi Thực tế với `df.sample(n, random_state=...)`
Thay vì dùng `df.head()` (vốn chỉ hiển thị các dòng đầu tiên thường được nhập chỉn chu trong giai đoạn thử nghiệm), hãy dùng `df.sample(3)` để bốc ngẫu nhiên một vài dòng ở giữa và cuối bảng. Điều này giúp phát hiện sớm các hiện tượng bất thường như chuỗi ký tự bị lỗi font, giá trị số bị lẫn đơn vị tiền tệ, hoặc các giá trị rỗng xuất hiện bất chợt.

### Bước 3: Kiểm định Toàn diện Cấu trúc và Bộ nhớ với `df.info()`
Lệnh `df.info()` cung cấp cái nhìn toàn cảnh:
- Tên chính xác của từng cột và thứ tự của chúng.
- Số lượng bản ghi không bị khuyết thiếu (*Non-Null Count*). Lấy tổng số dòng trừ đi số non-null sẽ cho ta biết chính xác số lượng giá trị bị khuyết (`NaN`).
- Kiểu dữ liệu kỹ thuật (`Dtype`) của từng cột: kiểm tra xem cột giá tiền có thực sự là kiểu số (`float64`) hay đang bị đọc nhầm thành chuỗi ký tự (`object`).
- Tổng dung lượng bộ nhớ RAM mà bảng đang chiếm dụng.

### Bước 4: Tóm tắt Phân phối Số học với `df["price"].describe()`
Lệnh `.describe()` tóm tắt các thông số thống kê cốt lõi: số lượng quan sát hợp lệ (`count`), trung bình (`mean`), độ lệch chuẩn (`std`), giá trị nhỏ nhất (`min`), tứ phân vị ($25\%$, $50\%$ - trung vị, $75\%$) và giá trị lớn nhất (`max`).
- Nếu giá trị nhỏ nhất bằng $0$ hoặc âm: cần kiểm tra xem nghiệp vụ có cho phép giá bằng 0 hay không.
- Nếu giá trị lớn nhất vọt lên gấp hàng trăm lần giá trị trung vị: dấu hiệu rõ ràng của các ngoại lai cực trị (*Extreme Outliers*).

### Bước 5: Thẩm định Cơ cấu Danh mục với `df["room_type"].value_counts()`
Đếm số lượng bản ghi của từng phân loại. Khi bổ sung tham số `normalize=True`, hàm tự động chuyển đổi sang tỷ lệ phần trăm ($0.0 - 1.0$), giúp nhận diện ngay lập tức loại phòng nào đang chiếm lĩnh thị phần áp đảo.

---

## 3. Lọc và Chọn Dữ liệu Chuẩn mực: `df[mask]` vs `df.loc[mask, col]`

### 3.1. Phân biệt `df[mask]` và `df.loc[mask, col]`
- **`df[mask]`**: Sử dụng khi mục tiêu là **lọc các hàng** thỏa mãn điều kiện và giữ lại **toàn bộ các cột** của bảng.
- **`df.loc[mask, "price"]`**: Sử dụng khi mục tiêu là truy cập chính xác vào **một hoặc một nhóm cột cụ thể** trên những hàng thỏa mãn điều kiện.

```python
mask = df["room_type"] == "Entire home/apt"

# Lấy toàn bộ các cột của các căn nguyên căn
bang_nguyen_can = df[mask]

# Chỉ trích xuất cột giá của các căn nguyên căn
gia_nguyen_can = df.loc[mask, "price"]
```

### 3.2. Lọc Logic Kết hợp Nhiều Điều kiện
Trong pandas, các biểu thức logic trên Series được thực hiện theo cơ chế vector hóa từng phần tử. Vì độ ưu tiên của các toán tử bit trong Python (`&`, `|`, `~`) cao hơn toán tử so sánh (`<=`, `==`), ta **bắt buộc phải bọc ngoặc đơn quanh từng biểu thức điều kiện**:

```python
# CÚ PHÁP ĐÚNG CHUẨN:
mask = (df["room_type"] == "Entire home/apt") & (df["price"] <= 60000)

# CÚ PHÁP SAI LỖI:
# mask = df["room_type"] == "Entire home/apt" and df["price"] <= 60000  -> Lỗi ValueError!
# mask = (df["room_type"] == "Entire home/apt") & df["price"] <= 60000  -> Lỗi toán tử!
```
Tuyệt đối không dùng các từ khóa `and`, `or`, `not` của Python thuần vì chúng chỉ đánh giá tính chân trị của một giá trị đơn lẻ, không thể áp dụng cho toàn bộ mảng Boolean.

### 3.3. Tra cứu Cực trị Hiệu năng cao với `nsmallest`
Khi cần tìm $n$ căn phòng có giá thấp nhất, thay vì sắp xếp toàn bộ bảng bằng `.sort_values()` với độ phức tạp $O(N \log N)$, ta nên sử dụng phương thức `nsmallest(n, "price")`. Phương thức này sử dụng thuật toán hàng đợi ưu tiên (*Priority Queue / Heap*) với chi phí chỉ $O(N \log n)$, cực kỳ tối ưu khi tập dữ liệu có hàng triệu dòng:
```python
top_re = df.nsmallest(5, "price")[["name", "price"]]
```

---

## 4. Cơ chế Sửa Bảng, Bẫy Gán Hai Lần Ngoặc và Copy-on-Write (CoW)

### 4.1. Bẫy Gán Hai Lần Ngoặc (*Chained Indexing*)
Xét một đoạn mã thường thấy của người mới học khi muốn giảm $10\%$ giá phòng nguyên căn:
```python
# CÁCH LÀM SAI LẦM NGUY HIỂM:
df["price"][df["room_type"] == "Entire home/apt"] *= 0.9
```
Đoạn mã trên thực hiện qua hai bước liên tiếp:
1. `df["price"]`: Trả về một đối tượng Series trung gian (có thể là View hoặc Copy tùy thuộc vào bộ quản lý bộ nhớ bên dưới).
2. `[mask] *= 0.9`: Tiến hành gán giá trị mới lên đối tượng trung gian đó.

Hậu quả:
- Trong các phiên bản pandas cũ, lệnh này sẽ phát sinh cảnh báo danh bất hư truyền: `SettingWithCopyWarning`, và phép gán có thể không được cập nhật ngược trở lại bảng gốc `df`.
- Trong **pandas 2.0+ và pandas 3.0** với cơ chế **Copy-on-Write (CoW)** được kích hoạt mặc định, bước 1 sẽ tạo ra một bản sao phòng thủ. Phép gán ở bước 2 chỉ sửa đổi trên bản sao tạm thời rồi biến mất, **bảng gốc `df` hoàn toàn không đổi**!

**Quy tắc vàng bất biến**: Khi muốn sửa đổi giá trị trong DataFrame, luôn sử dụng cú pháp một bước duy nhất với `.loc`:
```python
# CÁCH LÀM CHUẨN MỰC KỸ THUẬT:
mask = df["room_type"] == "Entire home/apt"
df.loc[mask, "price"] = df.loc[mask, "price"] * 0.9
```

### 4.2. Cột Lưu Giá trị Đã tính, KHÔNG Lưu Công thức
Trong các phần mềm bảng tính như Microsoft Excel, nếu cột $C$ được cài đặt công thức `= A * B`, khi giá trị của cột $A$ thay đổi thì cột $C$ sẽ tự động cập nhật.
Tuy nhiên, trong DataFrame của pandas: **các cột chỉ lưu trữ các giá trị tĩnh tại thời điểm tính toán**.
Nếu bạn đã tạo cột `tien_3_dem = df["price"] * 3`, sau đó bạn giảm giá cột `price` đi $10\%$, thì giá trị trong cột `tien_3_dem` **vẫn giữ nguyên con số cũ**!
Do đó, sau bất kỳ thao tác chỉnh sửa dữ liệu gốc nào, ta bắt buộc phải **chủ động tính toán lại toàn bộ các cột phụ thuộc liên quan**:
```python
# Sau khi sửa đổi giá:
df.loc[mask, "price"] = df.loc[mask, "price"] * 0.9

# BẮT BUỘC TÍNH TOÁN LẠI CỘT PHỤ THUỘC:
df["tien_3_dem"] = df["price"] * 3
```

---

## 5. Tác động của `NaN` lên Phép tính Tỷ lệ và Mẫu số

Trong toán học và thống kê, phép so sánh logic giữa một số thực với giá trị thiếu `NaN` luôn trả về `False`:
```python
np.nan < 50000  # Trả về False!
```
Giả sử ta muốn tính tỷ lệ các chỗ ở có giá thấp hơn mức trung vị toàn thành phố ($50,000$ CLP). Có hai cách tính toán dẫn đến hai con số hoàn toàn khác nhau:

### Cách 1: Tỷ lệ thô (*Gross Share*)
```python
ty_le_tho = (df["price"] < 50000).mean()
```
- Phép toán `(df["price"] < 50000)` biến các dòng có giá trị `NaN` thành `False`.
- Hàm `.mean()` trên mảng Boolean sẽ tính tổng số phần tử `True` chia cho **tổng số dòng của toàn bộ bảng (bao gồm cả các dòng bị thiếu giá)**.
- Mẫu số ở đây là: $\text{Mẫu số} = N_{\text{toàn bộ}}$.

### Cách 2: Tỷ lệ sạch (*Net Share*)
```python
gia_hop_le = df["price"].dropna()
ty_le_sach = (gia_hop_le < 50000).mean()
```
- Mẫu số ở đây chỉ bao gồm các dòng thực sự có dữ liệu giá hợp lệ: $\text{Mẫu số} = N_{\text{hợp lệ}}$.

### Bài học phương pháp luận:
Vì $N_{\text{toàn bộ}} \ge N_{\text{hợp lệ}}$, tỷ lệ thô luôn nhỏ hơn hoặc bằng tỷ lệ sạch ($\text{ty\_le\_tho} \le \text{ty\_le\_sach}$). Khi trình bày báo cáo cho các nhà đầu tư, người phân tích dữ liệu trung thực bắt buộc phải **nêu rõ mẫu số được sử dụng**, và đồng thời báo cáo số lượng các dòng bị thiếu dữ liệu (`n_missing`) để người ra quyết định đánh giá được mức độ rủi ro thông tin.

---

## 6. Bài tập Thực chiến Phòng Lab 04 (100% Nội dung Lab)

Dưới đây là trọn vẹn các bài tập từ Lab 04, giải quyết bài toán thực tế: Lập hồ sơ phân tích thị trường cho quận **Ñuñoa** (thủ đô Santiago) và đối sánh với toàn thành phố.

### Bảng dữ liệu mẫu dùng trong bài tập
Bảng giả lập 12 dòng `DEMO` phản ánh đầy đủ các tình huống thực tế (giá thiếu `NaN`, nhiều loại phòng):
```python
import numpy as np
import pandas as pd

DEMO = pd.DataFrame({
    "id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112],
    "name": ["Depto Plaza Ñuñoa", "Pieza cerca metro", "Loft Irarrázaval", "Depto sin precio",
             "Dormitorio simple", "Casa familiar", "Studio Providencia", "Pieza Providencia",
             "Depto Centro", "Hostal Centro", "Pieza Centro", "Hotel boutique"],
    "neighbourhood": ["Ñuñoa"] * 6 + ["Providencia"] * 2 + ["Santiago"] * 4,
    "room_type": ["Entire home/apt", "Private room", "Entire home/apt", "Entire home/apt",
                  "Private room", "Entire home/apt", "Entire home/apt", "Private room",
                  "Entire home/apt", "Shared room", "Private room", "Hotel room"],
    "price": [45000.0, 18000.0, 72000.0, np.nan, 2500.0, 60000.0,
              80000.0, 30000.0, 40000.0, 12000.0, np.nan, 95000.0],
    "number_of_reviews": [12, 3, 0, 1, 25, 7, 4, 0, 30, 2, 5, 9],
})
```

---

### Bài tập 1 (Q1): Khởi động: Chọn Cột, Chọn Hàng và Tính Tỷ lệ
::: exercise Phân biệt Series, DataFrame và lọc hàng theo điều kiện
Viết hàm `select_basics(df: pd.DataFrame) -> dict`.
Yêu cầu trả về từ điển chứa chính xác 5 khóa:
- `cot_gia`: Series cột `price` (dùng 1 cặp ngoặc vuông).
- `bang_con`: DataFrame gồm đúng 2 cột `name`, `price` theo thứ tự (dùng danh sách 2 cặp ngoặc).
- `ty_le_private`: float, tỷ lệ dòng có `room_type == "Private room"` trên tổng số dòng (dùng `mean()` trên mask Boolean).
- `nguyen_can`: DataFrame gồm các dòng có `room_type == "Entire home/apt"`, giữ đủ mọi cột (dùng `df[mask]`).
- `gia_nguyen_can`: Series `price` của đúng các dòng nguyên căn đó (dùng `df.loc[mask, "price"]`).
- Giữ nguyên index và thứ tự dòng, không sửa DataFrame đầu vào.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def select_basics(df: pd.DataFrame) -> dict:
    # 1. Trích xuất Series và DataFrame con
    cot_gia = df["price"]
    bang_con = df[["name", "price"]]
    
    # 2. Tỷ lệ dòng phòng riêng trên tổng số dòng
    mask_private = df["room_type"] == "Private room"
    ty_le_private = float(mask_private.mean())
    
    # 3. Lọc dòng nguyên căn bằng df[mask] và trích xuất cột giá bằng .loc
    mask_entire = df["room_type"] == "Entire home/apt"
    nguyen_can = df[mask_entire]
    gia_nguyen_can = df.loc[mask_entire, "price"]
    
    return {
        "cot_gia": cot_gia,
        "bang_con": bang_con,
        "ty_le_private": ty_le_private,
        "nguyen_can": nguyen_can,
        "gia_nguyen_can": gia_nguyen_can
    }
```
:::

---

### Bài tập 2 (Thói quen 5 bước): Khám phá Dữ liệu Thị trường
::: exercise Thực hành 5 lệnh khám phá và đọc chỉ số thực tế
Chạy 5 câu lệnh sau trên tập dữ liệu và ghi nhận số liệu:
```python
# 1. Kiểm tra kích thước
print("1. Shape:", df.shape)

# 2. Bốc ngẫu nhiên 3 dòng
print("2. Sample:\n", df.sample(3, random_state=1)[["name", "neighbourhood", "room_type", "price"]])

# 3. Kiểm định thông tin cột và kiểu
print("3. Info:")
df.info()

# 4. Tóm tắt thống kê cột giá
print("4. Describe:\n", df["price"].describe().round(0))

# 5. Cơ cấu phân loại phòng
print("5. Value counts:\n", df["room_type"].value_counts())
```
Hãy giải thích ý nghĩa của từng chỉ số đối với một nhà đầu tư đang cân nhắc mở cơ sở lưu trú.
:::

::: solution
#### Phân tích sư phạm:
1. **`df.shape`**: Cho biết dung lượng toàn thị trường (trên bảng snapshot Santiago thật là $18,534$ chỗ ở, $19$ cột thông tin).
2. **`df.sample()`**: Giúp nhà đầu tư quan sát cách đặt tên phòng thực tế của các đối thủ cạnh tranh trên nền tảng Airbnb.
3. **`df.info()`**: Cột `price` có $17,688$ giá trị non-null, suy ra có đúng $18,534 - 17,688 = 846$ chỗ ở đang bị ẩn giá hoặc chưa công khai giá.
4. **`df["price"].describe()`**: Trung vị giá ($50\%$) toàn thành phố là $59,000$ CLP, trong khi giá trung bình là $118,200$ CLP. Sự chênh lệch gấp đôi này khẳng định thị trường có nhiều căn hộ siêu sang kéo lệch phân phối.
5. **`df["room_type"].value_counts()`**: Toàn thị trường gồm 4 loại phòng, trong đó căn hộ nguyên căn (*Entire home/apt*) chiếm ưu thế tuyệt đối ($> 80\%$).
:::

---

### Bài tập 3 (Q2): Phân lập Dữ liệu một Quận và Tính Tỷ trọng Quy mô
::: exercise Lọc dữ liệu theo ranh giới hành chính
Viết hàm `filter_district(df: pd.DataFrame, ten_quan: str) -> dict`.
Yêu cầu trả về từ điển chứa:
- `bang`: DataFrame gồm tất cả các dòng có `neighbourhood == ten_quan`, giữ đủ các cột, giữ nguyên index gốc.
- `ty_trong`: float, tỷ lệ số dòng của quận chia cho tổng số dòng của toàn bảng `df`.
- Nếu quận không có trong bảng, trả về `bang` rỗng (vẫn đầy đủ các cột) và `ty_trong = 0.0`.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def filter_district(df: pd.DataFrame, ten_quan: str) -> dict:
    mask = df["neighbourhood"] == ten_quan
    bang_quan = df[mask]
    
    tong_so_dong = len(df)
    ty_trong = float(len(bang_quan) / tong_so_dong) if tong_so_dong > 0 else 0.0
    
    return {
        "bang": bang_quan,
        "ty_trong": ty_trong
    }
```
*Đối chiếu thực tế*: Quận Ñuñoa trên dữ liệu Santiago có $1,813$ chỗ ở, chiếm xấp xỉ $9.8\%$ quy mô thị trường toàn thành phố.
:::

---

### Bài tập 4 (Q3): Lọc Phân khúc Kết hợp Nhiều Điều kiện
::: exercise Đếm số lượng căn phòng theo phân khúc ngân sách
Viết hàm `count_segment(listings: pd.DataFrame, room_type: str = "Entire home/apt", gia_toi_da: float = 60000) -> int`.
Yêu cầu:
- Nhận bảng dữ liệu một quận.
- Đếm tổng số dòng thỏa mãn đồng thời: `room_type` bằng tham số và `price <= gia_toi_da`.
- Các dòng bị thiếu giá (`price` là `NaN`) không được tính vào kết quả.
- Sử dụng mặt nạ Boolean với toán tử `&`, không dùng vòng lặp `for`.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def count_segment(listings: pd.DataFrame, room_type: str = "Entire home/apt", gia_toi_da: float = 60000) -> int:
    # Phép so sánh price <= gia_toi_da tự động trả về False cho các ô NaN
    mask = (listings["room_type"] == room_type) & (listings["price"] <= gia_toi_da)
    return int(mask.sum())
```
*Đối chiếu thực tế*: Tại quận Ñuñoa, có đúng $539$ căn hộ nguyên căn có mức giá từ $60,000$ CLP trở xuống.
:::

---

### Bài tập 5 (Q4): Tìm kiếm Chỗ ở Giá Thấp Nhất và Thẩm định Ngoại lai Sàn
::: exercise Trích xuất các vị trí có giá thấp nhất bằng `nsmallest`
Viết hàm `cheapest(listings: pd.DataFrame, n: int = 5) -> pd.DataFrame`.
Yêu cầu:
- Trả về DataFrame gồm đúng $n$ dòng có giá thấp nhất, chỉ gồm hai cột `["name", "price"]` theo thứ tự đó.
- Sắp xếp giá tăng dần, giữ nguyên index gốc. Các dòng bị thiếu giá không được đưa vào danh sách.
- Không sửa DataFrame đầu vào.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def cheapest(listings: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    # nsmallest tự động bỏ qua các giá trị NaN và giữ tính ổn định thứ tự khi đồng giá
    return listings.nsmallest(n, "price")[["name", "price"]]
```

#### Nhận xét sư phạm về ngoại lai sàn:
- Trên dữ liệu snapshot Santiago thật, căn phòng rẻ nhất tại Ñuñoa được ghi nhận với mức giá chỉ $2,228$ CLP/đêm (tương đương khoảng $60,000$ VNĐ).
- Mức giá này là một ngoại lai bất thường cần gắn cờ kiểm tra: có thể chủ nhà đã nhập nhầm giá phòng theo giờ thành giá theo đêm, hoặc đây là mức phí đặt cọc giữ chỗ chứ không phải giá thuê trọn gói.
:::

---

### Bài tập 6 (Q5): Sửa Bảng Bằng `.loc` và Cập nhật Cột Phụ thuộc
::: exercise Mô phỏng chính sách giảm giá và bảo toàn tính toàn vẹn
Viết hàm `discount_quote(listings: pd.DataFrame, room_type: str = "Entire home/apt", giam: float = 0.10) -> pd.DataFrame`.
Yêu cầu:
- Tạo một bảng mới độc lập từ `listings.copy()`.
- Giảm giá các phòng có `room_type` tương ứng đi một tỷ lệ `giam` bằng cú pháp chuẩn mực `.loc[mask, "price"]`. Các loại phòng khác giữ nguyên giá.
- Thêm cột `tien_3_dem` tính bằng $3 \times \text{price}$ **tính từ mức giá sau khi đã giảm**. Các ô có giá `NaN` vẫn giữ nguyên là `NaN`.
- Bảng kết quả gồm đúng 4 cột: `["id", "room_type", "price", "tien_3_dem"]`, giữ nguyên index gốc.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def discount_quote(listings: pd.DataFrame, room_type: str = "Entire home/apt", giam: float = 0.10) -> pd.DataFrame:
    # 1. Tạo bản sao độc lập
    df_quote = listings[["id", "room_type", "price"]].copy()
    
    # 2. Cập nhật giá bằng .loc an toàn
    mask = df_quote["room_type"] == room_type
    df_quote.loc[mask, "price"] = df_quote.loc[mask, "price"] * (1.0 - giam)
    
    # 3. Tính toán lại cột phụ thuộc sau khi cập nhật giá
    df_quote["tien_3_dem"] = df_quote["price"] * 3
    
    return df_quote
```
:::

---

### Bài tập 7 (Q6): Đối sánh với Toàn Thành phố và Phân tích Độ chệch Mẫu số
::: exercise Đo lường sức cạnh tranh và kiểm soát giá trị khuyết thiếu
Viết hàm `share_below(prices: pd.Series, nguong: float) -> dict`.
Yêu cầu nhận Series giá và một ngưỡng giá, trả về từ điển chứa:
- `ty_le_tho`: float, tỷ lệ dòng có giá $<$ ngưỡng tính trên toàn bộ mọi dòng (kể cả dòng thiếu giá).
- `ty_le_sach`: float, tỷ lệ dòng có giá $<$ ngưỡng tính riêng trên các dòng thực sự có giá (`notna()`).
- `so_thieu`: int, tổng số dòng bị thiếu giá (`isna().sum()`).
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def share_below(prices: pd.Series, nguong: float) -> dict:
    so_thieu = int(prices.isna().sum())
    
    # 1. Tỷ lệ thô: Mẫu số là toàn bộ dòng
    ty_le_tho = float((prices < nguong).mean())
    
    # 2. Tỷ lệ sạch: Mẫu số chỉ gồm các dòng hợp lệ
    prices_valid = prices.dropna()
    ty_le_sach = float((prices_valid < nguong).mean()) if len(prices_valid) > 0 else 0.0
    
    return {
        "ty_le_tho": ty_le_tho,
        "ty_le_sach": ty_le_sach,
        "so_thieu": so_thieu
    }
```
*Đối chiếu thực tế*: Tại quận Ñuñoa so với trung vị thành phố ($59,000$ CLP), tỷ lệ thô là $0.444$ trong khi tỷ lệ sạch là $0.467$. Hai con số chênh lệch nhau đúng bằng lượng dữ liệu bị thiếu ($4.96\%$).
:::

---

### Bài tập 8 (Q7): Phân tích Cơ cấu Loại phòng và Mức Thiếu Dữ liệu
::: exercise Lập báo cáo cơ cấu danh mục
Viết hàm `room_mix(listings: pd.DataFrame) -> dict`.
Yêu cầu trả về từ điển gồm:
- `co_cau`: Series chứa tỷ lệ phần trăm ($0.0 - 1.0$) của từng loại phòng, sử dụng `.value_counts(normalize=True)`.
- `thieu_pct`: float, phần trăm các dòng bị thiếu giá (thang đo $0 - 100$), làm tròn đúng 2 chữ số thập phân.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def room_mix(listings: pd.DataFrame) -> dict:
    # 1. Cơ cấu loại phòng chuẩn hóa tổng bằng 1.0
    co_cau = listings["room_type"].value_counts(normalize=True)
    
    # 2. Phần trăm dòng thiếu giá
    thieu_pct = round(float(listings["price"].isna().mean() * 100), 2)
    
    return {
        "co_cau": co_cau,
        "thieu_pct": thieu_pct
    }
```
:::

---

### Bài tập 9 (Q8): Đóng gói Hồ sơ Quận ra Tệp CSV và Kiểm định Bất biến
::: exercise Tuần tự hóa bảng tóm tắt và kiểm tra tính toàn vẹn
Viết hàm `export_profile(listings: pd.DataFrame, ten_quan: str, path: str) -> pd.DataFrame`.
Yêu cầu:
1. Tạo một DataFrame gồm đúng 1 dòng tóm tắt hồ sơ quận với 5 cột theo thứ tự:
   - `quan`: Tên quận (`ten_quan`).
   - `so_cho_o`: Tổng số dòng của quận.
   - `gia_trung_vi`: Giá trị trung vị cột `price` (bỏ qua `NaN`).
   - `ty_le_nguyen_can`: Tỷ lệ phòng nguyên căn (`Entire home/apt`), làm tròn 3 chữ số thập phân.
   - `ty_le_thieu_gia_pct`: Phần trăm dòng thiếu giá, làm tròn 2 chữ số thập phân.
2. Xuất bảng ra tệp CSV tại đường dẫn `path`, sử dụng `to_csv(path, index=False, encoding="utf-8")`.
3. Đọc lại tệp CSV vừa xuất bằng `pd.read_csv(path)` và trả về DataFrame đọc lại để kiểm định tính toàn vẹn.
:::

::: solution
#### Lời giải chi tiết:
```python
import pandas as pd

def export_profile(listings: pd.DataFrame, ten_quan: str, path: str) -> pd.DataFrame:
    so_cho_o = len(listings)
    gia_trung_vi = float(listings["price"].median())
    ty_le_nguyen_can = round(float((listings["room_type"] == "Entire home/apt").mean()), 3)
    ty_le_thieu_gia_pct = round(float(listings["price"].isna().mean() * 100), 2)
    
    ho_so = pd.DataFrame([{
        "quan": ten_quan,
        "so_cho_o": so_cho_o,
        "gia_trung_vi": gia_trung_vi,
        "ty_le_nguyen_can": ty_le_nguyen_can,
        "ty_le_thieu_gia_pct": ty_le_thieu_gia_pct
    }])
    
    # Xuất ra file không lưu index phụ
    ho_so.to_csv(path, index=False, encoding="utf-8")
    
    # Đọc lại và trả về
    return pd.read_csv(path)
```
:::

---

### Bài tập 10 (Mở rộng & Nâng cao): Khám phá Quận Tối ưu và Phản biện Mã nguồn AI
::: exercise Ba bài tập mở rộng nâng cao năng lực thực chiến
1. **Lập hồ sơ quận đối chứng**: Đổi biến cấu hình `TEN_QUAN = "Providencia"` hoặc `"Santiago"`. Viết 3 nhận xét so sánh giữa quận mới và quận Ñuñoa.
2. **Tìm quận "Ngon - Bổ - Rẻ"**: Viết lệnh tìm quận có ít nhất $300$ chỗ ở và có mức giá trung vị thấp nhất toàn thành phố.
3. **Phản biện mã nguồn AI**: Một trợ lý AI gợi ý cách giảm giá như sau:
   ```python
   bao_gia = nu[["id", "room_type", "price"]].copy()
   bao_gia["price"][bao_gia["room_type"] == "Entire home/apt"] *= 0.9
   ```
   Hãy giải thích tại sao trong pandas 3 (Copy-on-Write), đoạn mã trên chạy không báo lỗi cú pháp nhưng cột `price` lại không hề giảm một đồng nào!
:::

::: solution
#### Lời giải & Phân tích chuyên sâu:

1. **So sánh Ñuñoa và Providencia**:
   - Quận Providencia có quy mô lớn hơn đáng kể (hơn $3,800$ chỗ ở, chiếm $> 20\%$ thị trường).
   - Mức giá trung vị tại Providencia ($72,000$ CLP) cao hơn Ñuñoa ($60,981$ CLP) khoảng $18\%$, phản ánh đây là khu trung tâm thương mại và tài chính sầm uất.
   - Cơ cấu phòng của cả hai quận đều có tỷ lệ nguyên căn cao ($> 80\%$), cho thấy đặc thù phục vụ khách du lịch gia đình và chuyên gia lưu trú ngắn hạn.

2. **Tìm quận quy mô lớn có giá trung vị thấp nhất**:
   ```python
   thong_ke_khu = df.groupby("neighbourhood")["price"].agg(
       trung_vi="median",
       quy_mo="size"
   )
   khu_dat_chuan = thong_ke_khu[thong_ke_khu["quy_mo"] >= 300]
   quan_re_nhat = khu_dat_chuan.sort_values("trung_vi").head(1)
   print(quan_re_nhat)
   ```
   *Kết quả*: Quận **Santiago (Centro)** hoặc **Estación Central** là quận có quy mô lớn ($\ge 300$ phòng) và giá trung vị thấp nhất (khoảng $35,000 - 40,000$ CLP/đêm).

3. **Mổ xẻ cơ chế Copy-on-Write đối với mã AI**:
   - Biểu thức `bao_gia["price"]` trả về một khung nhìn tạm thời của cột giá.
   - Trong cơ chế Copy-on-Write (CoW) của pandas 2.0+ và 3.0, khi bạn cố gắng sửa đổi khung nhìn tạm thời đó bằng `[mask] *= 0.9`, pandas nhận diện đây là hành vi sửa đổi qua hai lần ngoặc (*chained assignment*).
   - Để bảo vệ an toàn cho bảng gốc `bao_gia`, pandas tự động tạo ra một bản sao tách rời (*copy*) của Series `price`, áp dụng phép nhân $0.9$ trên bản sao đó rồi hủy bỏ nó ngay khi kết thúc dòng lệnh.
   - Do đó, cột `price` trong bảng gốc `bao_gia` vẫn giữ nguyên giá trị ban đầu!
   - Đoạn mã sửa lại đúng chuẩn mực bắt buộc phải là:
     ```python
     mask = bao_gia["room_type"] == "Entire home/apt"
     bao_gia.loc[mask, "price"] = bao_gia.loc[mask, "price"] * 0.9
     ```
:::

---

## 7. Tổng kết Bài học

1. **Thói quen 5 bước**: Luôn luôn bắt đầu dự án bằng `shape`, `sample`, `info`, `describe`, và `value_counts`.
2. **Kỷ luật với `.loc`**: Nói không với phép gán hai lần ngoặc `df["col"][mask] = ...`. Luôn dùng `df.loc[mask, "col"] = ...` để bảo đảm mã nguồn hoạt động chính xác trên mọi phiên bản pandas.
3. **Cập nhật cột phụ thuộc**: Cột trong DataFrame lưu giá trị, không lưu công thức. Phải chủ động tính toán lại sau khi sửa đổi dữ liệu gốc.
4. **Minh bạch mẫu số**: Luôn phân định rạch ròi giữa tỷ lệ thô và tỷ lệ sạch khi dữ liệu xuất hiện giá trị thiếu `NaN`.
