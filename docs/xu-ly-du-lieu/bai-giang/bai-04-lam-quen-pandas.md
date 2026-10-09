---
course: xu-ly-du-lieu
lecture: bai-04-lam-quen-pandas
section: lecture
title: "Làm quen với pandas"
prerequisites: ["chi-muc","dictionary","gia-tri-thieu"]
lessonStatus: ready
description: "Dựng Series và DataFrame, kiểm tra bảng, chọn hàng cột và tính thống kê với mẫu số rõ ràng."
---

Nếu NumPy cung cấp sức mạnh tính toán thần tốc trên các mảng thuần số, thì trong đời thực, dữ liệu hiếm khi chỉ toàn những con số vô danh. Dữ liệu thực tế gắn liền với ngữ nghĩa: cột nào là tên khách hàng, cột nào là mã sản phẩm, hàng nào tương ứng với thời điểm nào, và làm sao để xử lý những ô dữ liệu bị bỏ trống mà không làm gãy toàn bộ cấu trúc bảng?

Năm 2008, khi làm việc tại quỹ đầu tư AQR Capital Management, Wes McKinney nhận thấy Python lúc bấy giờ thiếu vắng một công cụ đủ mạnh để thao tác với dữ liệu dạng bảng có nhãn như ngôn ngữ R hay cơ sở dữ liệu SQL. Ông đã khai sinh ra **pandas** (viết tắt từ *Python Data Analysis Library* và lấy cảm hứng từ thuật ngữ kinh tế lượng *Panel Data*). pandas nhanh chóng trở thành tiêu chuẩn vàng của ngành khoa học dữ liệu, biến Python thành một ngôn ngữ xử lý bảng số liệu linh hoạt bậc nhất thế giới.

## 1. Hai trụ cột cấu trúc: Series và DataFrame

pandas kế thừa toàn bộ tốc độ của mảng NumPy bên dưới, nhưng bổ sung thêm một lớp trừu tượng cực kỳ quan trọng: **Hệ thống nhãn (Index)**.

- **`Series`**: Cấu trúc dữ liệu 1 chiều gồm một mảng dữ liệu đi kèm một mảng nhãn định danh tương ứng. Bạn có thể hình dung Series như một danh sách Python có chỉ số thông minh, hoặc một cuốn từ điển có thứ tự được vector hóa.
- **`DataFrame`**: Cấu trúc dữ liệu 2 chiều dạng bảng hình chữ nhật. Một DataFrame bao gồm tập hợp các Series xếp cạnh nhau có chung một trục nhãn hàng (Index). Điểm đặc sắc là mỗi cột có thể mang một kiểu dữ liệu khác nhau (cột chuỗi, cột số thực, cột ngày tháng) mà vẫn giữ được sự đồng nhất hoàn hảo trong bảng.

```python
import pandas as pd

df = pd.DataFrame({
    "id": ["001", "002", "003", "004"],
    "nhom": ["sach", "vo", "sach", "vo"],
    "gia": [20, 30, None, 50],
    "so_luong": [2, 1, 3, 2],
})
print(df.shape)                 # (4, 4)
print(type(df["gia"]).__name__)  # Series
print(type(df[["gia"]]).__name__)  # DataFrame
```

Hãy quan sát sự khác biệt tinh tế giữa hai cú pháp truy cập cột:
- **`df["gia"]`** (một cặp ngoặc vuông): Trích xuất cột dưới dạng một đối tượng **`Series`** 1 chiều.
- **`df[["gia"]]`** (hai cặp ngoặc vuông, truyền vào một danh sách tên cột): Trích xuất một **`DataFrame`** con chỉ gồm 1 cột duy nhất, bảo tồn đầy đủ cấu trúc bảng 2 chiều.

Hiểu rõ sự khác biệt giữa Series và DataFrame một cột là kỹ năng căn bản giúp ta tránh được hàng loạt lỗi không tương thích kiểu đối tượng khi truyền dữ liệu vào các hàm biến đổi tiếp theo.

## 2. Thăm dò và thẩm định dữ liệu ban đầu

Khi tiếp nhận một tập dữ liệu mới, việc đầu tiên của một nhà khoa học dữ liệu không phải là lao vào vẽ biểu đồ hay xây dựng mô hình, mà là tiến hành "khám sức khỏe" sơ bộ cho bảng dữ liệu.

```python
print(df.head())
print(df.dtypes)
df.info()
print(df.describe())
print(df["nhom"].value_counts(dropna=False))
print(df.isna().sum())
```

Quy trình khám xét dữ liệu gồm năm bước kỷ luật:

1. **`head(n)`**: Xem nhanh $n$ dòng đầu tiên để cảm nhận hình thái dữ liệu. Đây là bước kiểm tra trực quan, nhưng tuyệt đối không được chủ quan coi $n$ dòng đầu đại diện cho toàn bộ tệp dữ liệu.
2. **`info()`**: Báo cáo tổng thể về số lượng dòng, số cột, kiểu dữ liệu thực tế của từng cột và lượng bộ nhớ RAM mà bảng đang chiếm dụng.
3. **`describe()`**: Tóm tắt thống kê mô tả cho các cột số: số lượng quan sát hợp lệ, trung bình, độ lệch chuẩn, giá trị nhỏ nhất, lớn nhất và các mốc phân vị (25%, 50%, 75%).
4. **`value_counts(dropna=False)`**: Đếm tần suất xuất hiện của từng giá trị trong cột phân loại. Luôn đặt `dropna=False` để phát hiện xem có bao nhiêu ô dữ liệu đang bị khuyết thiếu trong cột này.
5. **`isna().sum()`**: Kiểm đếm số lượng giá trị rỗng trên từng cột.

Hãy nhìn sâu vào mối quan hệ số học giữa số dòng và số quan sát hợp lệ:

```python
print(len(df), df["gia"].count(), df["gia"].isna().sum())  # 4 3 1
print(df["gia"].mean())         # 33.333333333333336
```

Bảng có 4 dòng (`len(df) = 4`), nhưng giá trị `df["gia"].count()` chỉ trả về 3. Trong pandas, hàm `count()` chỉ đếm các giá trị **không khuyết thiếu**. Khi tính giá trị trung bình `df["gia"].mean()`, pandas tự động bỏ qua ô khuyết thiếu và chia tổng giá trị ($20 + 30 + 50 = 100$) cho 3 mẫu số hợp lệ, cho ra kết quả $33.33$ nghìn đồng.

## 3. Lựa chọn dữ liệu có điều kiện: loc, iloc và logic bitwise

pandas cung cấp hai bộ định tuyến truy xuất dữ liệu độc lập:

- **`.loc[...]` (Label-based)**: Truy xuất hoàn toàn dựa trên **nhãn** của hàng và tên của cột. Quy ước lát cắt của `.loc` bao gồm **cả hai đầu mút** $[start, stop]$.
- **`.iloc[...]` (Integer-based)**: Truy xuất hoàn toàn dựa trên **vị trí số nguyên** tương đối từ $0$ đến $n-1$. Quy ước lát cắt của `.iloc` tuân theo chuẩn Python thông thường, bao gồm đầu mút trái nhưng loại trừ đầu mút phải $[start, stop)$.

```python
print(df.loc[1, "gia"])         # 30.0: nhãn hàng 1
print(df.iloc[1, 2])            # 30.0: vị trí hàng 1, cột 2
mask = (df["nhom"] == "vo") & (df["gia"] >= 30)
print(df.loc[mask, ["id", "gia"]])
```

Khi lọc dữ liệu theo nhiều tiêu chí, có hai nguyên tắc sống còn:

1. **Sử dụng toán tử bitwise (`&`, `|`, `~`) thay vì từ khóa logic (`and`, `or`, `not`)**: Trong Python thuần, `and` và `or` đánh giá giá trị chân lý của toàn bộ đối tượng. Khi áp dụng lên một Series gồm nhiều phần tử, Python sẽ bối rối không biết Series này là đúng hay sai và ném ra lỗi nổi tiếng `ValueError: The truth value of a Series is ambiguous`. Ta bắt buộc phải dùng các toán tử bitwise `&` (và), `|` (hoặc), `~` (phủ định) để ép việc so sánh diễn ra trên từng phần tử tương ứng của mảng.
2. **Luôn bao bọc mỗi mệnh đề điều kiện trong dấu ngoặc đơn**: Trong bảng thứ tự ưu tiên toán tử của Python, các toán tử bitwise `&`, `|` có độ ưu tiên cao hơn các toán tử so sánh `==`, `>=`. Nếu bạn viết `df["nhom"] == "vo" & df["gia"] >= 30` mà không có ngoặc, Python sẽ thực hiện phép toán `"vo" & df["gia"]` trước tiên, dẫn đến lỗi sập chương trình `TypeError`. Viết `(df["nhom"] == "vo") & (df["gia"] >= 30)` là chuẩn mực bắt buộc.

## 4. Tạo lập cột mới và triết lý dữ liệu khuyết thiếu

Việc tính toán thêm các chỉ số phái sinh là thao tác diễn ra liên tục trong phân tích. Phép nhân hai Series được thực hiện tự động trên từng dòng tương ứng theo cơ chế vector hóa:

```python
df["doanh_thu"] = df["gia"] * df["so_luong"]
print(df["doanh_thu"].tolist())  # [40.0, 30.0, nan, 100.0]
print(df["doanh_thu"].sum(min_count=1))  # 170.0
print(df.sort_values("gia", na_position="last")["id"].tolist())
```

Tại dòng mang mã `003`, do giá bán là `None` (biểu diễn dưới dạng `NaN` trong mảng số thực), phép nhân $\text{NaN} \times 3$ lập tức sinh ra $\text{NaN}$. Đây là hành vi toán học hoàn toàn chính xác theo chuẩn IEEE 754: bất kỳ phép tính nào có sự tham gia của một đại lượng không xác định đều phải cho ra một kết quả không xác định.

Tuy nhiên, khi tính tổng doanh thu bằng `df["doanh_thu"].sum()`, theo mặc định pandas sẽ bỏ qua các giá trị `NaN` và cộng các phần tử còn lại: $40 + 30 + 100 = 170$ nghìn đồng.

Ở đây xuất hiện một cạm bẫy học thuật rất lớn: Giả sử một cột dữ liệu bị hỏng hoàn toàn và chứa toàn bộ giá trị `NaN`. Hàm `.sum()` mặc định của pandas sẽ trả về kết quả là `0.0`! Điều này vô tình đánh đồng việc "một cửa hàng không có bất kỳ dữ liệu nào" với việc "cửa hàng có doanh thu bằng 0".

Để giải quyết triệt để vấn đề này, các kỹ sư thường truyền thêm tham số **`min_count=1`**:

```python
s = pd.Series([None, None], dtype="float64")
print(s.sum())              # 0.0 (dễ gây ngộ nhận)
print(s.sum(min_count=1))   # NaN (chính xác về mặt ngữ nghĩa)
```

Tham số `min_count=1` đòi hỏi cột phải có **ít nhất một giá trị hợp lệ** thì mới được phép trả về tổng số; nếu toàn bộ đều là dữ liệu khuyết thiếu, kết quả sẽ là `NaN`. Đây là cách làm bảo đảm tính trung thực tuyệt đối của báo cáo tài chính.

## 5. Nạp dữ liệu từ tệp CSV an toàn

CSV (Comma-Separated Values) là định dạng trao đổi dữ liệu phổ biến nhất, nhưng cũng là định dạng lỏng lẻo nhất vì bản thân tệp CSV thuần túy không chứa bất kỳ siêu dữ liệu (metadata) nào về kiểu của các cột.

```python
from io import StringIO

text = "id,nhom,gia\n001,sach,20\n002,vo,30\n003,sach,\n"
doc = pd.read_csv(StringIO(text), dtype={"id": "string"})
print(doc["id"].tolist())        # ['001', '002', '003']
print(doc["gia"].isna().sum())   # 1
csv_moi = doc.to_csv(index=False)
assert "001" in csv_moi
```

Khi đọc dữ liệu bằng `pd.read_csv()`, hãy ghi nhớ ba nguyên tắc:

1. **Khóa định dạng chuỗi bằng `dtype`**: Nếu không chỉ định `dtype={"id": "string"}`, pandas sẽ tự động suy đoán cột `id` là số nguyên và biến `"001"` thành số `1`. Luôn chủ động khai báo kiểu chuỗi cho mọi cột mã định danh, số điện thoại hoặc mã bưu cục.
2. **Loại bỏ chỉ số phụ khi xuất tệp**: Khi gọi `doc.to_csv()`, luôn truyền tham số **`index=False`**. Nếu quên tham số này, pandas sẽ ghi cả cột số thứ tự mặc định `0, 1, 2...` vào tệp CSV mới dưới dạng một cột không tên. Sau vài lần đọc đi ghi lại, tệp dữ liệu của bạn sẽ bị rác hóa bởi hàng loạt cột `Unnamed: 0`, `Unnamed: 1`.
3. **Kiểm tra tham số phân tách**: Nếu tệp dữ liệu sử dụng dấu chấm phẩy `;` thay cho dấu phẩy (rất phổ biến ở châu Âu) hoặc dấu tab `\t`, hãy cấu hình tường minh tham số `sep=";"` hoặc `sep="\t"`.

## 6. Bài tập tự luyện

::: exercise Thẩm định kích thước và độ rỗng
Xem lại bảng `df` ở mục 1. Hãy viết biểu thức pandas để tính:
1. Tổng số dòng của bảng.
2. Số lượng mặt hàng thực sự đã có giá.
3. Số lượng phân loại hàng hóa duy nhất trong cột `nhom`.
:::

::: solution
1. Tổng số dòng: `len(df)` cho kết quả là `4`.
2. Số mặt hàng đã có giá: `df["gia"].count()` cho kết quả là `3`.
3. Số phân loại duy nhất: `df["nhom"].nunique()` cho kết quả là `2` (gồm nhóm `"sach"` và `"vo"`).

Ba câu hỏi này ứng với ba hàm khác nhau và trả lời ba khía cạnh độc lập của chất lượng dữ liệu.
:::

::: exercise Trích xuất bảng con đúng cấu trúc
Hãy viết câu lệnh sử dụng `.loc` để lọc ra các mặt hàng thuộc nhóm `"sach"`, chỉ lấy hai cột `id` và `gia`. Kết quả trả về phải là một đối tượng DataFrame hai chiều.
:::

::: solution
Câu lệnh chuẩn xác là:
```python
df.loc[df["nhom"] == "sach", ["id", "gia"]]
```
Biểu thức điều kiện `df["nhom"] == "sach"` đóng vai trò mặt nạ chọn các dòng `001` và `003`. Danh sách cột `["id", "gia"]` bảo đảm kết quả trả về duy trì cấu trúc DataFrame 2 chiều.
:::

::: exercise Bản chất của tổng khuyết thiếu
Cho một Series rỗng: `s = pd.Series([None, None], dtype="float64")`. So sánh giá trị trả về của `s.sum()` và `s.sum(min_count=1)`. Trong tình huống nào việc sử dụng `s.sum()` mặc định sẽ dẫn đến kết luận kinh doanh sai lầm?
:::

::: solution
- `s.sum()` trả về `0.0`.
- `s.sum(min_count=1)` trả về `NaN`.

Nếu ta đang tính tổng doanh thu của một chi nhánh mới mở chưa kịp gửi báo cáo dữ liệu về trụ sở, hàm `s.sum()` mặc định sẽ thông báo doanh thu của chi nhánh bằng $0$ đồng. Điều này khiến ban giám đốc hiểu lầm rằng chi nhánh kinh doanh ế ẩm và không bán được gì, trong khi sự thật là số liệu kinh doanh chưa từng được ghi nhận. Sử dụng `min_count=1` giúp bảo vệ hệ thống trước sự nhầm lẫn tai hại này.
:::

::: exercise Lọc đa điều kiện và gán nhãn phân khúc phòng tránh SettingWithCopyWarning
Cho bảng dữ liệu khách hàng lưu trong một DataFrame:
```python
import pandas as pd
import numpy as np

data = {
    "ma_khach": ["KH01", "KH02", "KH03", "KH04", "KH05"],
    "chi_tieu": [" $1,200.50 ", " 450.00 ", "Chua_co", " $780.00 ", " -100.00 "],
    "so_don": [8, 3, 1, 6, 2],
    "phan_khuc": ["Thuong", "Thuong", "Thuong", "Thuong", "Thuong"]
}
df = pd.DataFrame(data)
```
Yêu cầu:
1. Chuyển đổi cột `chi_tieu` thành số thực hợp lệ. Các chuỗi không đọc được hoặc giá âm phải được coi là khuyết thiếu (`NaN`).
2. Xác định các khách hàng thỏa mãn tiêu chuẩn VIP: `chi_tieu >= 500` và `so_don >= 5`.
3. Cập nhật nhãn `"VIP"` vào cột `phan_khuc` của các khách hàng này trên chính bảng gốc `df` mà tuyệt đối không để phát sinh cảnh báo `SettingWithCopyWarning`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Chained Assignment - Tiềm ẩn cạm bẫy)
Người mới học thường thực hiện việc lọc trước để tạo bảng con rồi gán nhãn:

```python
# Làm sạch cột chi tiêu
df["chi_tieu_so"] = df["chi_tieu"].astype(str).str.replace("$", "", regex=False).str.replace(",", "", regex=False).str.strip()
df["chi_tieu_so"] = pd.to_numeric(df["chi_tieu_so"], errors="coerce")
df.loc[df["chi_tieu_so"] < 0, "chi_tieu_so"] = np.nan

# Cạm bẫy thường gặp: Chained Indexing
# Lọc bảng con rồi gán nhãn trực tiếp -> pandas ném cảnh báo SettingWithCopyWarning
bang_vip = df[(df["chi_tieu_so"] >= 500) & (df["so_don"] >= 5)]
# bang_vip["phan_khuc"] = "VIP"  <-- NGUY HIỂM: Sửa trên bản sao ngầm, không tác động bảng gốc df!
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Vector hóa Regex một bước và gán trực tiếp qua `.loc`)
Một cách người ta hay dùng trong thực tế sản xuất là chuẩn hóa số học bằng Regex gọn gàng và gán thẳng vào vị trí nhãn thông qua `.loc`:

```python
# 1. Làm sạch siêu tốc một bước bằng Regex loại bỏ mọi ký tự không phải số hoặc dấu chấm
df["chi_tieu_so"] = pd.to_numeric(
    df["chi_tieu"].astype(str).str.replace(r"[^0-9.]", "", regex=True),
    errors="coerce"
)

# 2. Xây dựng mặt nạ boolean kết hợp điều kiện có đóng mở ngoặc đơn tường minh
mask_vip = (df["chi_tieu_so"] >= 500.0) & (df["so_don"] >= 5)

# 3. Gán nhãn trực tiếp một bước duy nhất qua .loc trên bảng gốc
df.loc[mask_vip, "phan_khuc"] = "VIP"

print(df[["ma_khach", "chi_tieu_so", "so_don", "phan_khuc"]])
```

#### Phân tích bản chất & Bình luận sư phạm
- **Nguồn gốc cảnh báo `SettingWithCopyWarning`**: Khi ta viết `df[dieu_kien]['cot'] = gia_tri`, pandas phải thực hiện 2 thao tác riêng biệt: `__getitem__` (lọc) rồi `__setitem__` (gán). pandas không thể biết kết quả của bước lọc là một khung nhìn (*View*) hay một bản sao (*Copy*). Do đó, phép gán có thể bị nuốt chửng trên một đối tượng tạm thời mà không hề làm thay đổi bảng gốc `df`.
- **Nguyên tắc bất di bất dịch của `.loc`**: Cú pháp `df.loc[hang, cot] = gia_tri` thực hiện phép gán trong **một bước duy nhất**, chỉ thị trực tiếp vị trí ô nhớ cần biến đổi trên DataFrame cha, bảo đảm tính xác định $100\%$ và an toàn tuyệt đối dưới cơ chế Copy-on-Write (CoW).
:::

## 7. Nguồn và đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 5: Getting Started with pandas](https://wesmckinney.com/book/pandas-basics) và [Chương 6: Data Loading, Storage, and File Formats](https://wesmckinney.com/book/accessing-data).
- Tài liệu chính thức về kiến trúc hiện đại: [pandas User Guide — Copy-on-Write (CoW)](https://pandas.pydata.org/docs/user_guide/copy_on_write.html).
- [Bài giảng tham khảo môn Xử lý dữ liệu (iaidev)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-04-lam-quen-pandas.html).
