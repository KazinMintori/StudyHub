---
course: xu-ly-du-lieu
lecture: bai-04-lam-quen-pandas
section: lecture
title: "Làm quen với pandas"
prerequisites: ["chi-muc", "dictionary", "gia-tri-thieu"]
lessonStatus: ready
description: "Dựng Series và DataFrame, thói quen 5 bước khám phá dữ liệu, lọc chọn chuẩn mực bằng .loc, bẫy gán hai lần ngoặc và lập hồ sơ phân tích thị trường."
---

## 1. Bản chất Cấu trúc: Series, DataFrame và Hệ thống Nhãn (Index)

Khi làm việc với các bài toán thực tế, dữ liệu hiếm khi chỉ tồn tại dưới dạng những con số vô danh. Dữ liệu thực luôn đi kèm ngữ nghĩa phong phú: Cột nào là định danh khách hàng, cột nào là giá niêm yết, hàng nào thuộc về quận nào, và làm sao để xử lý những quan sát bị bỏ trống mà không làm gãy vỡ cấu trúc tính toán?

Năm 2008, Wes McKinney đã phát triển **pandas** nhằm mang lại cho Python một cấu trúc dữ liệu dạng bảng có nhãn (*Labeled Tabular Data*) sánh ngang với ngôn ngữ R hay cơ sở dữ liệu quan hệ SQL.

<DataDiagram name="dataframe-series" />

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
- Kiểu dữ liệu kỹ thuật (`Dtype`) của từng cột: Kiểm tra xem cột giá tiền có thực sự là kiểu số (`float64`) hay đang bị đọc nhầm thành chuỗi ký tự (`object`).
- Tổng dung lượng bộ nhớ RAM mà bảng đang chiếm dụng.

### Bước 4: Tóm tắt Phân phối Số học với `df["price"].describe()`
Lệnh `.describe()` tóm tắt các thông số thống kê cốt lõi: Số lượng quan sát hợp lệ (`count`), trung bình (`mean`), độ lệch chuẩn (`std`), giá trị nhỏ nhất (`min`), tứ phân vị ($25\%$, $50\%$ - trung vị, $75\%$) và giá trị lớn nhất (`max`).
- Nếu giá trị nhỏ nhất bằng $0$ hoặc âm: Cần kiểm tra xem nghiệp vụ có cho phép giá bằng 0 hay không.
- Nếu giá trị lớn nhất vọt lên gấp hàng trăm lần giá trị trung vị: Dấu hiệu rõ ràng của các ngoại lai cực trị (*Extreme Outliers*).

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
Tuy nhiên, trong DataFrame của pandas: **Các cột chỉ lưu trữ các giá trị tĩnh tại thời điểm tính toán**.
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

## 6. Bài tập Thực chiến Phòng Lab 04 (100% Nội dung Lab) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 7. Tổng kết Bài học

1. **Thói quen 5 bước**: Luôn luôn bắt đầu dự án bằng `shape`, `sample`, `info`, `describe`, và `value_counts`.
2. **Kỷ luật với `.loc`**: Nói không với phép gán hai lần ngoặc `df["col"][mask] = ...`. Luôn dùng `df.loc[mask, "col"] = ...` để bảo đảm mã nguồn hoạt động chính xác trên mọi phiên bản pandas.
3. **Cập nhật cột phụ thuộc**: Cột trong DataFrame lưu giá trị, không lưu công thức. Phải chủ động tính toán lại sau khi sửa đổi dữ liệu gốc.
4. **Minh bạch mẫu số**: Luôn phân định rạch ròi giữa tỷ lệ thô và tỷ lệ sạch khi dữ liệu xuất hiện giá trị thiếu `NaN`.
