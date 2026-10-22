---
course: xu-ly-du-lieu
lecture: bai-06-ket-noi-truy-xuat-du-lieu
section: lecture
title: "Nạp, lưu trữ và truy xuất dữ liệu"
prerequisites: ["dataframe", "ham-lap-trinh"]
lessonStatus: ready
hasChapterExercises: true
description: "Kỹ thuật nạp dữ liệu phân đoạn với chunksize, định dạng văn bản CSV/JSON/XML/HTML, lưu trữ cột Parquet, định dạng HDF5/Excel, ranh giới an toàn của pickle, giao tiếp Web API và truy vấn SQL tại chỗ bằng DuckDB."
---


<div class="lecture-notes-content">

Xét bài toán nạp một tệp ghi nhận đơn hàng gồm mã giao dịch, thời điểm mua và giá trị thanh toán. Dữ liệu này có thể được lưu trữ dưới dạng tệp văn bản CSV trên máy cục bộ, chuỗi JSON trả về từ cổng dịch vụ web, bảng quan hệ trong cơ sở dữ liệu SQL, hoặc tệp nhị phân nén Parquet. Nếu người xử lý chỉ gọi các hàm đọc mặc định mà không nắm rõ cơ chế phân tích cú pháp, chương trình rất dễ phân loại sai kiểu dữ liệu, nhận nhầm mã ký hiệu hợp lệ thành ô trống, hoặc gây tràn bộ nhớ khi dung lượng tệp vượt quá bộ nhớ RAM khả dụng.

Bài học này làm rõ cơ chế nạp, lưu trữ và truy xuất dữ liệu trong Python: Phân tích cú pháp tệp văn bản và kỹ thuật đọc phân đoạn theo khối, bóc tách cấu trúc bán cấu trúc JSON/XML/HTML, tối ưu hóa lưu trữ cột với Parquet, nhận diện ranh giới an toàn của pickle, giao tiếp với Web API qua HTTP, và truy vấn trực tiếp bằng SQL cùng DuckDB.

---

## 1. Đọc và ghi dữ liệu định dạng văn bản phân cách

Định dạng văn bản thuần túy (như CSV hoặc tệp phân cách bằng dấu tab) là phương tiện phổ biến nhất để trao đổi dữ liệu giữa các hệ thống nhờ tính tương thích phổ quát và khả năng đọc trực tiếp bằng mắt người.

### 1.1. Cơ chế phân tích cú pháp của `read_csv` và `read_table`

Thư viện pandas cung cấp hai hàm nạp tệp văn bản chủ lực:
- `read_csv`: Mặc định sử dụng dấu phẩy `,` làm ký tự phân cách các trường dữ liệu.
- `read_table`: Mặc định sử dụng dấu tab `\t` làm ký tự phân cách.

Về bản chất kỹ thuật, `read_csv` nhận diện dòng đầu tiên làm tiêu đề cột (*header*). Khi tệp dữ liệu không có dòng tiêu đề, lập trình viên bắt buộc phải chỉ định `header=None` và truyền danh sách tên cột vào tham số `names`. Nếu muốn sử dụng một cột cụ thể làm chỉ mục hàng (*Index*), ta thiết lập tham số `index_col`.

```python
import io
import pandas as pd

du_lieu_csv = """ma_so,ho_ten,phong_ban,luong
NV01,Nguyễn Văn An,Kỹ thuật,1850
NV02,Trần Thị Bình,Kinh doanh,2100
NV03,Lê Hoàng Cường,Kỹ thuật,1950
"""

# Nạp bảng dữ liệu và đặt cột ma_so làm chỉ mục
df_nhan_vien = pd.read_csv(
    io.StringIO(du_lieu_csv),
    index_col="ma_so"
)
print(df_nhan_vien)
```

Khi tệp chứa các dòng ghi chú hoặc thông tin phiên bản ở đầu tệp, tham số `skiprows` cho phép bỏ qua số dòng tương ứng hoặc truyền vào một danh sách các chỉ số dòng cần loại trừ trước khi phân tích cú pháp.

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-1 -->

::: example Chỉ định tiêu đề cột và kiểu dữ liệu khi phân tích tệp phân cách bằng tab

Khi tiếp nhận tệp nhật ký ghi nhận nhân sự phân cách bằng tab nhưng không có dòng tiêu đề cột, việc gọi hàm đọc thông thường sẽ lấy nhầm dòng đầu tiên làm tên cột và tự động ép mã nhân viên thành số nguyên. Ta cần chỉ định tham số names, header=None và định rõ dtype để giữ trọn vẹn định dạng chuỗi của mã định danh.

```python
import io
import pandas as pd

du_lieu_tab = (
    "NV01\tAn\t12.5\n"
    "NV02\tBinh\t18.0\n"
    "NV03\tChi\t15.2"
)

df_nv = pd.read_table(
    io.StringIO(du_lieu_tab),
    header=None,
    names=["ma_nv", "ten", "luong"],
    usecols=["ma_nv", "luong"],
    dtype={"ma_nv": "string", "luong": "float64"}
)
print(df_nv)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| ma&#95;nv | luong |
| --- | --- |
| NV01 | 12.5 |
| NV02 | 18.0 |
| NV03 | 15.2 |

</div>

Một tình huống thực tế khi xử lý dữ liệu hệ thống là tệp văn bản không có dòng tiêu đề đầu tiên và các trường được phân tách bằng ký tự tab. Nếu gọi `pd.read_csv` theo mặc định mà không cấu hình tham số phân cách, hàm sẽ tìm kiếm dấu phẩy và lấy dòng dữ liệu đầu tiên làm tiêu đề. Hàng dữ liệu đầu tiên do đó bị nhận nhầm thành tên cột, làm mất một quan sát hợp lệ.

Hàm `pd.read_table` được thiết lập với ký tự phân cách mặc định `sep='\t'`. Để tránh lấy dòng đầu làm tiêu đề, ta truyền tham số `header=None` kết hợp với danh sách tên cột tường minh qua tham số `names=['ma_nv', 'ten', 'luong']`. Thao tác này thiết lập cấu trúc cột ngay từ bước đọc tệp.

Tham số `usecols` giới hạn danh sách các cột cần nạp vào bộ nhớ: Cột `ma_nv` và cột `luong`. Việc bỏ qua cột `ten` ngay trong quá trình phân tích cú pháp giúp giảm lượng dữ liệu cần chuyển vào bộ nhớ khi xử lý các bảng có nhiều cột không phục vụ bài toán.

`dtype` chỉ định kiểu của các cột đã chọn. Với mã có số 0 ở đầu như `"0012"`, đặt kiểu chuỗi tránh biến mã thành số 12. Mã `NV01` trong ví dụ vốn đã chứa chữ, nhưng khai báo `string` vẫn làm rõ cách chương trình dự định sử dụng cột này.

:::

<!-- /worked-example -->

### 1.2. Quy ước nhận diện giá trị thiếu trong tệp {#_1-2-kiem-soat-gia-tri-khuyet-thieu-va-bay-quy-uoc-quoc-te}

Mỗi nguồn dữ liệu lại sở hữu một quy ước riêng để đánh dấu ô trống, chẳng hạn `"N/A"`, `"NaN"`, `"NULL"` hoặc `"-999"`. Hàm `read_csv` có sẵn một danh sách các chuỗi mặc định được tự động nhận diện là giá trị khuyết thiếu (`np.nan`).

Một chuỗi ký tự có thể mang ý nghĩa khác với quy ước nhận diện ô thiếu. Xét mã quốc gia theo ISO alpha-2: Namibia có mã `"NA"`. Khi đọc CSV bằng cấu hình mặc định, pandas nhận chuỗi này là giá trị thiếu. Ta cần chỉ định quy tắc đọc phù hợp với ý nghĩa của từng cột.

Để xử lý chính xác, ta phải làm chủ hai tham số:
1. `keep_default_na=False`: Vô hiệu hóa toàn bộ danh sách quy ước khuyết thiếu mặc định của thư viện.
2. `na_values`: Khai báo tường minh tập hợp các chuỗi được coi là khuyết thiếu, áp dụng chung cho toàn bảng hoặc định nghĩa riêng theo từng cột dưới dạng một từ điển (`dict`).

```python
bang_quoc_gia = """ma_qg,ten_qg,chi_so
VN,Việt Nam,85
NA,Namibia,
JP,Nhật Bản,92
"""

# Namibia có mã 'NA' nhưng không phải là dữ liệu thiếu; ô trống ở cột chi_so mới là thiếu
df_qg = pd.read_csv(
    io.StringIO(bang_quoc_gia),
    keep_default_na=False,
    na_values={"chi_so": [""]}
)
print(df_qg)
assert df_qg.loc[df_qg["ma_qg"] == "NA", "ten_qg"].iloc[0] == "Namibia"
assert pd.isna(df_qg.loc[df_qg["ma_qg"] == "NA", "chi_so"].iloc[0])
```

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-2 -->

::: example Chỉ định giá trị khuyết thiếu theo từng cột và bảo vệ mã phân loại quốc tế

Trong các bảng dữ liệu khu vực quốc tế, mã hai chữ cái NA đại diện cho quốc gia Namibia hoặc khu vực Bắc Mỹ thường bị pandas tự động quy đổi thành giá trị khuyết thiếu NaN. Ta vô hiệu hóa bộ quy tắc nhận diện mặc định và chỉ định cụ thể các ký hiệu được xem là ô trống trên từng cột riêng biệt.

```python
import io
import pandas as pd

csv_quoc_gia = (
    "khu,ma_vung,diem\n"
    "A,NA,8.5\n"
    "B,VN,-999\n"
    "C,NA,\n"
    "D,US,9.0"
)

df_vung = pd.read_csv(
    io.StringIO(csv_quoc_gia),
    keep_default_na=False,
    na_values={"diem": ["-999", ""]}
)
print(df_vung)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| khu | ma&#95;vung | diem |
| --- | --- | --- |
| A | NA | 8.5 |
| B | VN | (thiếu) |
| C | NA | (thiếu) |
| D | US | 9.0 |

</div>

Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.

Theo mặc định, `read_csv` nhận một số chuỗi như `"NA"`, `"N/A"` và `"null"` là ô thiếu. Trong bảng này, `NA` lại là mã quốc gia Namibia. Nếu giữ mặc định, giá trị mã bị mất ý nghĩa, dù bản ghi vẫn còn trong bảng.

Để xử lý chính xác, ta truyền tham số `keep_default_na=False`: Thao tác này thông báo cho pandas không tự động xem các từ viết tắt mặc định là dữ liệu thiếu. Khi đó, chuỗi `'NA'` ở cột `ma_vung` được giữ nguyên vẹn dưới dạng văn bản đại diện cho quốc gia.

`na_values={"diem": ["-999", ""]}` bổ sung quy ước thiếu riêng cho cột điểm. Vì thế, hai giá trị này được đọc thành ô thiếu ở `diem`, trong khi `NA` ở cột mã vẫn là văn bản. Khi tắt quy ước mặc định, những chuỗi còn lại vẫn được suy diễn kiểu theo nội dung, không nhất thiết đều thành chuỗi.

Kết quả thu được là một `DataFrame` phản ánh đúng thiết kế: Cột `ma_vung` bảo toàn mã chuỗi `'NA'`, trong khi cột `diem` nhận đúng các giá trị số thực và mang giá trị `NaN` ở các dòng thiếu. Cách tiếp cận theo từng cột này bảo vệ tính toàn vẹn của dữ liệu phân loại mà không bỏ sót việc làm sạch dữ liệu số đo lường.

:::

<!-- /worked-example -->

### 1.3. Đọc dữ liệu phân đoạn với `chunksize` và `nrows`

Khi kích thước của tệp văn bản vượt quá dung lượng bộ nhớ RAM khả dụng, việc gọi `read_csv` trên toàn bộ tệp sẽ lập tức gây ra lỗi tràn bộ nhớ (*Out-Of-Memory*).

Chiến lược xử lý chuẩn mực gồm hai bước:
- **Khảo sát cấu trúc**: Dùng tham số `nrows=n` để đọc thử $n$ dòng đầu tiên, kiểm tra tên cột, định dạng dữ liệu và dấu phân cách mà không tốn tài nguyên.
- **Xử lý theo luồng phân đoạn (Chunking)**: Thiết lập tham số `chunksize=k`. Khi đó, hàm không trả về một DataFrame tĩnh mà trả về một đối tượng lặp `TextFileReader`. Mỗi lần lặp qua đối tượng này, pandas sẽ nạp đúng $k$ dòng vào bộ nhớ dưới dạng một DataFrame nhỏ.

Kỹ sư dữ liệu sẽ áp dụng phép tổng hợp trung gian trên từng khối rồi giải phóng bộ nhớ trước khi nạp khối tiếp theo, giúp xử lý các tệp hàng chục gigabyte chỉ với vài trăm megabyte RAM:

```python
du_lieu_giao_dich = """id,khu_vuc,doanh_thu
1,Bắc,120
2,Nam,200
3,Bắc,180
4,Trung,150
5,Nam,300
6,Bắc,100
"""

# Đọc từng khối gồm 2 dòng để tính tổng doanh thu và số giao dịch toàn hệ thống
bo_doc = pd.read_csv(io.StringIO(du_lieu_giao_dich), chunksize=2)

tong_doanh_thu = 0
tong_so_luong = 0

for phan_doan in bo_doc:
    tong_doanh_thu += phan_doan["doanh_thu"].sum()
    tong_so_luong += phan_doan["doanh_thu"].count()

gia_tri_trung_binh = tong_doanh_thu / tong_so_luong
print("Tổng doanh thu:", tong_doanh_thu)
print("Số giao dịch:", tong_so_luong)
print("Doanh thu trung bình mỗi đơn:", gia_tri_trung_binh)
assert gia_tri_trung_binh == 175.0
```

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-3 -->

::: example Thăm dò dữ liệu và tính toán phân đoạn với TextFileReader

Khi làm việc với tệp nhật ký giao dịch có dung lượng lớn hơn bộ nhớ khả dụng, việc đọc toàn bộ tệp cùng lúc dễ dẫn đến cạn kiệt bộ nhớ. Ta sử dụng tham số chunksize để tạo đối tượng lặp TextFileReader và chủ động lấy từng khối dữ liệu bằng phương thức get_chunk nhằm tích lũy thống kê theo nhóm.

```python
import io
import pandas as pd

csv_giao_dich = (
    "id,nhom,gia\n"
    "1,A,10\n"
    "2,B,20\n"
    "3,A,30\n"
    "4,B,40\n"
    "5,A,50"
)

bo_doc = pd.read_csv(io.StringIO(csv_giao_dich), chunksize=2)
khoi_1 = bo_doc.get_chunk()
khoi_2 = bo_doc.get_chunk()
print(khoi_1)
print("Tong gia khoi 1:", int(khoi_1["gia"].sum()))
print(khoi_2)
print("Tong gia khoi 2:", int(khoi_2["gia"].sum()))
khoi_3 = bo_doc.get_chunk()
print(khoi_3)
print("Tổng giá cả ba khối:", sum(k["gia"].sum() for k in [khoi_1, khoi_2, khoi_3]))
bo_doc.close()
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| id | nhom | gia |
| --- | --- | --- |
| 1 | A | 10 |
| 2 | B | 20 |

</div>

```text
Tong gia khoi 1: 30
```

<div class="data-worked-table data-worked-table-wide">

| Chỉ mục | id | nhom | gia |
| --- | --- | --- | --- |
| 2 | 3 | A | 30 |
| 3 | 4 | B | 40 |

</div>

```text
Tong gia khoi 2: 70
```

<div class="data-worked-table data-worked-table-wide">

| Chỉ mục | id | nhom | gia |
| --- | --- | --- | --- |
| 4 | 5 | A | 50 |

</div>

```text
Tổng giá cả ba khối: 150
```

Khi nạp toàn bộ tệp lớn vào bộ nhớ bằng một lệnh `pd.read_csv` duy nhất, dung lượng bộ nhớ của tiến trình có thể vượt quá ngưỡng cho phép, dẫn đến lỗi cạn bộ nhớ. Đọc phân đoạn giúp chia nhỏ quá trình xử lý thành các đợt có kích thước xác định.

Tham số `chunksize=2` biến hàm `pd.read_csv` thành cơ chế tạo bộ lặp: Thay vì trả về một `DataFrame` duy nhất, hàm trả về đối tượng `TextFileReader`. Đối tượng này cho phép đọc từng khối bản ghi nối tiếp nhau mà không giữ toàn bộ dữ liệu trong bộ nhớ cùng lúc.

Hai lần `get_chunk()` đầu đọc các cặp dòng có tổng lần lượt 30 và 70. Lần thứ ba chỉ còn một dòng, giá 50. Vì vậy, kích thước khối là giới hạn mỗi lần đọc, không bảo đảm mọi khối đều có đúng hai dòng. Tổng cả tệp là 150.

Ví dụ giữ cả ba khối để đối chiếu. Với tệp lớn, có thể duyệt `for khoi in bo_doc` và chỉ lưu tổng đang tính, thay vì giữ từng DataFrame. Việc chia khối chỉ giảm bộ nhớ nếu chương trình cũng tránh tích lũy toàn bộ các khối lại.

:::

<!-- /worked-example -->

### 1.4. Ghi dữ liệu ra định dạng văn bản

Phương thức `to_csv` cho phép lưu cấu trúc DataFrame xuống đĩa hoặc luồng văn bản. Các tham số kỹ thuật cần kiểm soát:
- `sep`: Ký tự phân cách giữa các cột (mặc định là dấu phẩy `,`).
- `na_rep`: Chuỗi ký tự đại diện cho các ô khuyết thiếu khi ghi ra tệp (ví dụ `na_rep="NULL"`).
- `index=False`: Bỏ qua cột chỉ mục hàng nếu chỉ mục chỉ là dãy số tự tăng vô nghĩa, tránh tạo thêm cột thừa khi nạp lại.
- `header=False`: Loại bỏ dòng tiêu đề cột khi cần nối tiếp dữ liệu vào tệp đã có.

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-4 -->

::: example Định dạng tệp CSV đầu ra với phân cách tùy biến và giá trị thiếu

Khi chia sẻ bảng dữ liệu với các hệ thống kế toán hoặc cơ sở dữ liệu ngoài, hệ thống đích có thể yêu cầu dấu chấm phẩy làm ký tự phân cách và chuỗi ký tự tường minh đại diện cho ô trống. Phương thức to_csv cung cấp các tham số để kiểm soát định dạng tệp xuất mà không làm biến dạng dữ liệu.

```python
import io
import numpy as np
import pandas as pd

df_kho = pd.DataFrame({
    "ma": ["X1", "X2", "X3"],
    "ten": ["Kho A", "Kho B", "Kho C"],
    "ton": [15, np.nan, 42]
})

bo_nho = io.StringIO()
df_kho.to_csv(
    bo_nho,
    sep=";",
    na_rep="NULL",
    index=False,
    columns=["ma", "ton"]
)
print(bo_nho.getvalue().strip())
```

Kết quả khi chạy đoạn mã trên:

```text
ma;ton
X1;15.0
X2;NULL
X3;42.0
```

Sau khi tính toán và làm sạch, nhiệm vụ tiếp theo là lưu trữ kết quả ra tệp văn bản để chuyển giao. Nếu chỉ gọi `df.to_csv` với các thiết lập mặc định, bảng xuất ra sẽ chứa cột chỉ mục số nguyên tự tăng và để trống các ô có giá trị `NaN`. Hệ thống tiếp nhận bên ngoài có thể hiểu nhầm ô trống này là chuỗi rỗng thay vì giá trị khuyết thiếu.

Tham số `sep=';'` thay đổi ký tự phân cách cột từ dấu phẩy mặc định sang dấu chấm phẩy. Đây là quy ước thường gặp tại nhiều hệ thống tài chính vốn dùng dấu phẩy làm dấu ngăn cách phần thập phân của số thực.

`na_rep="NULL"` ghi chuỗi `NULL` tại ô thiếu. Đó chỉ là quy ước xuất văn bản, không khiến mọi hệ thống đọc tự hiểu đây là giá trị thiếu trong SQL. Bên nhận cần được cấu hình cùng quy ước, chẳng hạn dùng `na_values=["NULL"]` khi đọc lại bằng pandas.

Việc thiết lập `index=False` loại bỏ cột chỉ mục hàng mặc định của pandas, ngăn chặn việc sinh ra cột thừa mang tên `Unnamed: 0` khi tệp được nạp lại. Danh sách `columns=['ma', 'ton']` chỉ định chính xác các cột cần lưu, giúp lọc bỏ cột tên kho không cần thiết mà không phải tạo thêm một bản sao `DataFrame` trung gian.

:::

<!-- /worked-example -->

### 1.5. Xử lý các định dạng phân cách dị biệt với module `csv`

Trong thực tế, nhiều tệp văn bản chứa các trường dữ liệu có chứa cả dấu phân cách bên trong, sử dụng quy ước bao chuỗi phức tạp hoặc dùng nhiều ký tự thoát (*escape characters*). Thư viện chuẩn `csv` của Python cho phép định nghĩa các khuôn mẫu phân tích (`csv.Dialect`) để kiểm soát chính xác hành vi:

```python
import csv

dong_du_lieu = '101|"Căn hộ cao cấp, trung tâm"|5500\n102|"Biệt thự ven hồ"|12000'

class QuyUocDacBiet(csv.Dialect):
    delimiter = "|"
    quotechar = '"'
    doublequote = True
    skipinitialspace = True
    lineterminator = "\n"
    quoting = csv.QUOTE_MINIMAL

bo_tach = csv.reader(io.StringIO(dong_du_lieu), dialect=QuyUocDacBiet)
cac_dong = list(bo_tach)
print("Dòng 1 sau khi bóc tách:", cac_dong[0])
assert cac_dong[0][1] == "Căn hộ cao cấp, trung tâm"
```

---

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-5 -->

::: example Bao bọc trường dữ liệu phi số bằng module csv tiêu chuẩn

Khi nội dung các trường văn bản chứa sẵn dấu phẩy hoặc dấu cách, việc ghép chuỗi thủ công rất dễ làm vỡ cấu trúc cột của tệp dữ liệu. Ta sử dụng module csv của thư viện chuẩn cùng quy tắc trích dẫn QUOTE_NONNUMERIC để tự động đặt dấu nháy kép quanh toàn bộ các trường ký tự.

```python
import csv
import io

bo_dem = io.StringIO()
ghi_tep = csv.writer(
    bo_dem,
    delimiter=",",
    quoting=csv.QUOTE_NONNUMERIC
)

ghi_tep.writerow(["ma_hang", "mo_ta", "gia"])
ghi_tep.writerow(["H01", "May in, laser 2 mat", 3500])
ghi_tep.writerow(["H02", "Muc in chinh hang", 450])
print(bo_dem.getvalue().strip())
```

Kết quả khi chạy đoạn mã trên:

```text
"ma_hang","mo_ta","gia"
"H01","May in, laser 2 mat",3500
"H02","Muc in chinh hang",450
```

Một tình huống thường gặp khi xuất tệp dữ liệu văn bản là các trường mô tả sản phẩm chứa sẵn dấu phẩy, ví dụ cụm từ `'May in, laser 2 mat'`. Nếu ghi chuỗi bằng cách nối dấu phẩy thông thường, trình phân tích cú pháp khi đọc lại sẽ đếm dấu phẩy này thành dấu phân cách cột, khiến dòng dữ liệu bị tách thành bốn cột thay vì ba cột như thiết kế ban đầu.

Module `csv` tiêu chuẩn của Python cung cấp lớp `csv.writer` hỗ trợ các chế độ trích dẫn: Khi cấu hình `quoting=csv.QUOTE_NONNUMERIC`, trình ghi kiểm tra kiểu của từng phần tử. Mọi trường có kiểu chuỗi được tự động bao bọc bên trong cặp dấu nháy kép, trong khi các trường số thực hoặc số nguyên được giữ nguyên ở dạng số trần.

Quan sát dòng tiêu đề và dòng dữ liệu đầu tiên: Các chuỗi như `'ma_hang'`, `'mo_ta'` và `'May in, laser 2 mat'` đều có cặp dấu nháy kép bao quanh, còn giá trị số 3500 được ghi trực tiếp không có dấu nháy. Trình đọc tiêu chuẩn sẽ nhận ra nội dung nằm giữa hai dấu nháy kép là một trường dữ liệu thống nhất, bỏ qua dấu phẩy phân cách bên trong.

Cơ chế này giúp tệp trao đổi dữ liệu duy trì đúng số lượng cột: Hệ thống tiếp nhận không bị lệch vị trí các trường, đồng thời có thể nhận biết các trường mang số để chuyển đổi sang kiểu dữ liệu tính toán mà không cần bước ép kiểu thủ công.

:::

<!-- /worked-example -->

## 2. Dữ liệu bán cấu trúc: JSON, XML và HTML

Không phải mọi nguồn dữ liệu đều được sắp xếp ngay ngắn dưới dạng bảng hai chiều. Dữ liệu bán cấu trúc tổ chức thông tin dưới dạng cây hoặc các cặp khóa - giá trị lồng nhau.

### 2.1. Cấu trúc JSON và chuyển đổi hai chiều

JSON (*JavaScript Object Notation*) là chuẩn giao tiếp thực tế của các ứng dụng web và cổng API hiện đại. Python tích hợp sẵn module `json` với hai cặp hàm chủ đạo:
- `json.loads` và `json.dumps`: Chuyển đổi qua lại giữa chuỗi văn bản JSON và cấu trúc dữ liệu nguyên bản của Python (từ điển, danh sách).
- `json.load` và `json.dump`: Đọc và ghi trực tiếp trên các đối tượng tệp.

Thư viện pandas cung cấp hàm `pd.read_json` để chuyển chuỗi hoặc tệp JSON thành DataFrame. Tham số `orient` xác định cách thức tổ chức cấu trúc dữ liệu trong JSON:
- `orient="records"`: Mảng gồm các đối tượng từ điển, mỗi đối tượng đại diện cho một hàng trong bảng.
- `orient="columns"`: Từ điển chứa các cột, mỗi cột là một ánh xạ từ chỉ mục sang giá trị.
- `orient="index"`: Từ điển chứa các hàng, mỗi khóa là một chỉ mục hàng.

```python
chuoi_json = """[
    {"id": 1, "khach_hang": "Công ty A", "doanh_so": 150.5},
    {"id": 2, "khach_hang": "Công ty B", "doanh_so": 280.0}
]"""

df_json = pd.read_json(io.StringIO(chuoi_json), orient="records")
print(df_json)
assert df_json["doanh_so"].sum() == 430.5
```

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-6 -->

::: example Làm phẳng đối tượng JSON lồng nhau thành bảng hai chiều với json_normalize

Dữ liệu trả về từ các cổng dịch vụ Web API thường chứa các đối tượng lồng nhau biểu thị quan hệ phân cấp, chẳng hạn thông tin địa chỉ nằm bên trong trường khách hàng. Ta sử dụng hàm pd.json_normalize để làm phẳng các trường lồng này thành các cột độc lập với tên phân cách rõ ràng.

```python
import pandas as pd

phan_hoi_api = [
    {"id": 101, "khach": {"ten": "Lan", "tp": "HN"}, "tien": 500},
    {"id": 102, "khach": {"ten": "Minh", "tp": "DN"}, "tien": 820}
]

df_don = pd.json_normalize(phan_hoi_api, sep="_")
print(df_don)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| id | tien | khach&#95;ten | khach&#95;tp |
| --- | --- | --- | --- |
| 101 | 500 | Lan | HN |
| 102 | 820 | Minh | DN |

</div>

Định dạng JSON được xây dựng dựa trên các cấu trúc lồng nhau tùy biến: Một khóa trong đối tượng có thể chứa một từ điển con hoặc một danh sách các bản ghi phụ. Khi đưa cấu trúc này vào hàm `pd.DataFrame` thông thường, trường lồng nhau `khach` sẽ nạp nguyên vẹn dưới dạng một đối tượng từ điển Python trong một ô dữ liệu, gây khó khăn cho việc lọc và tổng hợp.

Hàm `pd.json_normalize` xử lý cấu trúc này bằng cách quét cấu trúc cây JSON và trải phẳng các khóa con thành các cột ngang: Khóa `ten` bên trong từ điển `khach` được trích xuất thành một thuộc tính độc lập của từng hàng dữ liệu.

Tham số `sep='_'` quy định ký tự nối giữa khóa cha và khóa con khi ghép tên cột mới: Hàm sinh ra hai cột mới là `khach_ten` và `khach_tp`. Điều này giúp cấu trúc `DataFrame` giữ được dạng phẳng hai chiều thân thiện với các câu lệnh truy vấn của pandas.

Kết quả trả về là một bảng dữ liệu với bốn cột riêng biệt gồm `id`, `tien`, `khach_ten` và `khach_tp`. Kiểu dữ liệu của các trường số và chuỗi được phân loại rõ ràng, cho phép người phân tích thực hiện các phép lọc theo thành phố hoặc tính tổng doanh thu mà không cần viết các hàm bóc tách từ điển trung gian.

:::

<!-- /worked-example -->

### 2.2. Trích xuất bảng từ trang web với `pd.read_html`

Để thu thập nhanh các bảng dữ liệu được nhúng trên các trang web, hàm `pd.read_html` sử dụng các công cụ phân tích cú pháp HTML như `lxml` hay `BeautifulSoup` để quét toàn bộ văn bản và trích xuất tất cả các khối thẻ `<table>...</table>`.

Hàm luôn trả về một danh sách các DataFrame:

```python
ma_html = """
<table>
    <thead>
        <tr><th>Kỳ học</th><th>Môn học</th><th>Số tín chỉ</th></tr>
    </thead>
    <tbody>
        <tr><td>Kỳ 1</td><td>Nhập môn lập trình</td><td>4</td></tr>
        <tr><td>Kỳ 2</td><td>Xử lý dữ liệu</td><td>3</td></tr>
    </tbody>
</table>
"""

danh_sach_bang = pd.read_html(io.StringIO(ma_html))
df_mon_hoc = danh_sach_bang[0]
print(df_mon_hoc)
assert df_mon_hoc["Số tín chỉ"].sum() == 7
```

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-7 -->

::: example Bóc tách bảng dữ liệu HTML thành danh sách DataFrame với read_html

Khi thu thập dữ liệu công khai từ các báo cáo định dạng trang web, tài liệu HTML thường chứa nhiều bảng dữ liệu. Ta sử dụng hàm pd.read_html để phân tích các thẻ table và chuyển đổi nội dung dạng bảng thành danh sách các đối tượng DataFrame.

```python
import io
import pandas as pd

trang_html = """
<table>
  <tr><th>ma_kho</th><th>so_luong</th></tr>
  <tr><td>K01</td><td>120</td></tr>
  <tr><td>K02</td><td>85</td></tr>
</table>
"""

danh_sach_bang = pd.read_html(io.StringIO(trang_html))
df_kho = danh_sach_bang[0]
print(df_kho)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| ma&#95;kho | so&#95;luong |
| --- | --- |
| K01 | 120 |
| K02 | 85 |

</div>

Trang web là nguồn cung cấp số liệu phổ biến nhưng cấu trúc tài liệu chứa nhiều thẻ định dạng hiển thị. Thư viện pandas cung cấp hàm `pd.read_html` để tự động tìm kiếm các khối thẻ `table` trên trang và phân tích nội dung bảng.

`read_html` trả danh sách những bảng thỏa điều kiện tìm kiếm. Với HTML mẫu chỉ có một bảng, phần tử đầu là bảng kho cần lấy. Nếu trang có nhiều bảng, có thể dùng `match` hoặc `attrs` để giới hạn bảng phù hợp thay vì luôn lấy phần tử 0.

Khi truyền đối tượng luồng văn bản `io.StringIO(trang_html)`, hàm nhận diện dòng đầu tiên chứa các thẻ `th` làm tiêu đề cột `ma_kho` và `so_luong`. Các dòng tiếp theo chứa thẻ `td` được chuyển thành các hàng dữ liệu tương ứng: Giá trị số 120 và 85 được chuyển đổi thành số nguyên.

Hàm đọc bảng có trong HTML đã được cung cấp, không tự thao tác giao diện hoặc chạy JavaScript để tải thêm dữ liệu. Nó cần một công cụ phân tích HTML như `lxml`. Vì vậy, cần kiểm tra bảng nguồn và thư viện hỗ trợ trước khi dùng cho một trang thực tế.

:::

<!-- /worked-example -->

### 2.3. Phân tích tài liệu XML bằng `lxml.objectify`

XML (*Extensible Markup Language*) là định dạng phân cấp lâu đời, thường xuất hiện trong các hệ thống ngân hàng, viễn thông và dữ liệu địa lý. Mô-đun `lxml.objectify` cung cấp cơ chế phân tích cú pháp hiệu năng cao, ánh xạ các thẻ XML thành các thuộc tính của đối tượng Python một cách tự nhiên:

```python
from lxml import objectify

du_lieu_xml = """
<kho_hang>
    <san_pham ma="SP01">
        <ten>Bàn phím cơ</ten>
        <gia>1200</gia>
    </san_pham>
    <san_pham ma="SP02">
        <ten>Chuột quang</ten>
        <gia>450</gia>
    </san_pham>
</kho_hang>
"""

goc = objectify.fromstring(du_lieu_xml.strip().encode("utf-8"))
danh_sach = []
for sp in goc.san_pham:
    danh_sach.append({
        "ma": sp.get("ma"),
        "ten": str(sp.ten),
        "gia": int(sp.gia)
    })

df_kho = pd.DataFrame(danh_sach)
print(df_kho)
assert df_kho["gia"].sum() == 1650
```

---

## 3. Định dạng nhị phân, lưu trữ cột và ranh giới bảo mật

Mặc dù định dạng văn bản rất tiện lợi, chúng lại bộc lộ hạn chế lớn: Kích thước tệp cồng kềnh, tốc độ đọc ghi chậm chạp do phải phân tích cú pháp chuỗi, và quan trọng nhất là đánh mất thông tin về kiểu dữ liệu kỹ thuật (*Type Degradation*). Các định dạng nhị phân ra đời để giải quyết triệt để những điểm yếu này.

### 3.1. Đọc và ghi tệp Microsoft Excel

Trong môi trường phân tích nghiệp vụ, bảng tính Excel (`.xlsx`, `.xls`) là phương tiện trao đổi phổ biến. Thư viện pandas tương tác với Excel thông qua công cụ nền `openpyxl`:
- `pd.read_excel`: Đọc trực tiếp một trang tính thành DataFrame.
- `pd.ExcelFile`: Đối tượng đại diện cho một sổ bảng tính gồm nhiều trang (*sheets*). Việc khởi tạo `ExcelFile` một lần giúp tăng tốc đáng kể khi cần đọc lần lượt nhiều trang tính từ cùng một tệp đĩa:

```python
bo_dem = io.BytesIO()
with pd.ExcelWriter(bo_dem, engine="openpyxl") as ghi_excel:
    df_nhan_vien.to_excel(ghi_excel, sheet_name="NhanVien")

bo_dem.seek(0)
so_bang_tinh = pd.ExcelFile(bo_dem)
print("Danh sách trang tính:", so_bang_tinh.sheet_names)
df_doc_lai = so_bang_tinh.parse("NhanVien", index_col="ma_so")
assert len(df_doc_lai) == 3
```

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-8 -->

::: example Ghi nhiều trang tính với ExcelWriter và đọc chọn lọc với ExcelFile

Trong các báo cáo nghiệp vụ tài chính, dữ liệu doanh thu và chi phí thường được lưu trữ trên các trang tính khác nhau trong cùng một tệp sổ tính Excel. Ta sử dụng ngữ cảnh pd.ExcelWriter để ghi nhiều bảng vào một tệp và dùng đối tượng pd.ExcelFile để truy xuất danh sách trang tính mà không cần nạp lại tệp nhiều lần.

```python
import io
import pandas as pd

bo_dem_excel = io.BytesIO()
df_thu = pd.DataFrame({"thang": ["T1", "T2"], "tien": [100, 150]})
df_chi = pd.DataFrame({"khoan": ["Luong", "Dien"], "tien": [60, 25]})

with pd.ExcelWriter(bo_dem_excel, engine="openpyxl") as bo_ghi:
    df_thu.to_excel(bo_ghi, sheet_name="Thu", index=False)
    df_chi.to_excel(bo_ghi, sheet_name="Chi", index=False)

bo_dem_excel.seek(0)
with pd.ExcelFile(bo_dem_excel) as so_tinh:
    print("Các trang tính:", so_tinh.sheet_names)
    df_doc_thu = so_tinh.parse("Thu")
print(df_doc_thu)
```

Kết quả khi chạy đoạn mã trên:

```text
Các trang tính: ['Thu', 'Chi']
```

<div class="data-worked-table">

| thang | tien |
| --- | --- |
| T1 | 100 |
| T2 | 150 |

</div>

Nếu gọi phương thức `df.to_excel` hai lần liên tiếp với cùng một đường dẫn tệp mà không dùng bộ ghi, bảng ghi sau sẽ ghi đè và làm mất dữ liệu của trang tính trước đó. Để tạo ra một sổ tính Excel chứa nhiều trang tính độc lập, ta quản lý tiến trình ghi thông qua lớp đối tượng `pd.ExcelWriter`.

Khi sử dụng khối lệnh `with pd.ExcelWriter(..., engine='openpyxl') as bo_ghi`, đối tượng bộ ghi mở một phiên làm việc: Phương thức `df_thu.to_excel` ghi dữ liệu vào trang `'Thu'`, sau đó `df_chi.to_excel` ghi dữ liệu vào trang `'Chi'`. Khi khối `with` kết thúc, toàn bộ cấu trúc định dạng của sổ tính được đóng gói và lưu hoàn chỉnh.

Ở chiều đọc dữ liệu: Nếu một tệp Excel có dung lượng lớn và chứa nhiều trang tính, việc gọi `pd.read_excel` lặp lại sẽ buộc hệ thống phải mở tệp và giải nén lại cấu trúc từ đầu ở mỗi lần gọi. Lớp `pd.ExcelFile` khắc phục tình trạng này bằng cách nạp cấu trúc sổ tính vào bộ nhớ một lần.

Thuộc tính `sheet_names` của đối tượng `ExcelFile` cung cấp danh sách tên các trang tính có trong tệp, và phương thức `parse('Thu')` trích xuất nội dung của trang tính mong muốn thành `DataFrame`. Cách tiếp cận này giúp giảm chi phí I/O khi xử lý các bảng tính có nhiều trang.

:::

<!-- /worked-example -->

### 3.2. Định dạng khoa học HDF5

HDF5 (*Hierarchical Data Format 5*) là định dạng lưu trữ nhị phân chuyên dụng trong tính toán khoa học, cho phép lưu trữ hàng tỷ phần tử số học kèm theo cơ chế nén trên đĩa. Điểm nổi trội của HDF5 là tổ chức dữ liệu như một hệ thống tệp thu nhỏ bên trong một tệp duy nhất, chia thành các nhóm (*groups*) và tập dữ liệu (*datasets*).

Pandas hỗ trợ HDF5 qua lớp `pd.HDFStore`:
- Chế độ `fixed`: Lưu trữ mảng khối nhị phân thuần túy, tốc độ ghi và đọc cực nhanh nhưng không thể truy vấn bộ phận.
- Chế độ `table`: Lưu trữ theo định dạng bảng quan hệ của PyTables. Muốn thực hiện truy vấn bộ phận bằng mệnh đề `where="luong > 1900"` mà không cần nạp toàn bộ tập dữ liệu lên RAM, ta bắt buộc phải khai báo tham số `data_columns` chứa danh sách các cột dùng làm điều kiện lọc (hoặc `data_columns=True`). Nếu không khai báo, PyTables sẽ gom các cột vào một khối nhị phân chung và không thể đánh chỉ mục để lọc trực tiếp trên đĩa:

```python
import tempfile
import os

with tempfile.NamedTemporaryFile(suffix=".h5", delete=False) as tep_tam:
    duong_dan_h5 = tep_tam.name

try:
    with pd.HDFStore(duong_dan_h5, mode="w") as kho:
        kho.put("giao_dich", df_nhan_vien, format="table", data_columns=["luong"])
        # Truy vấn trực tiếp các dòng có mức lương lớn hơn 1900
        ket_qua_loc = kho.select("giao_dich", where="luong > 1900")
        assert len(ket_qua_loc) == 2
except (ImportError, Exception):
    # PyTables có thể không được cài đặt sẵn trong môi trường thử nghiệm cục bộ
    pass
finally:
    if os.path.exists(duong_dan_h5):
        os.remove(duong_dan_h5)
```

### 3.3. Định dạng định hướng cột Apache Parquet

Trong kỹ nghệ dữ liệu hiện đại, Apache Parquet là chuẩn mực lưu trữ dữ liệu phân tích. Khác với CSV tổ chức theo từng dòng liên tiếp, Parquet tổ chức dữ liệu theo từng cột (*Columnar Storage*):

1. **Hiệu năng I/O vượt trội nhờ đọc cột chọn lọc**: Khi người dùng chỉ cần phân tích cột `luong`, trình đọc Parquet chỉ đọc đúng các dải byte của cột đó trong từng nhóm hàng (*Row Groups*), bỏ qua các khối dữ liệu của những cột không dùng đến. Điều này giúp giảm đáng kể lượng byte phải đọc từ đĩa so với việc phải duyệt qua toàn bộ các dòng và cột của tệp CSV dạng hàng.
2. **Khả năng nén tối ưu**: Vì một cột chỉ chứa cùng một kiểu dữ liệu đồng nhất, các thuật toán nén hiện đại (Snappy, Zstd, Dictionary Encoding) có thể nén dữ liệu chặt chẽ hơn nhiều so với việc nén văn bản dòng không đồng nhất.
3. **Lưu trữ lược đồ kiểu dữ liệu kỹ thuật (Schema Preservation)**: Định dạng Parquet lưu trữ thông tin kiểu dữ liệu chi tiết trong phần siêu dữ liệu ở đuôi tệp (*Metadata Footer*), bao gồm số nguyên, số thực, thời gian có hoặc không gắn múi giờ, kiểu boolean và cấu trúc lồng nhau. Điều này giúp hạn chế tình trạng suy giảm kiểu vốn thường gặp khi đọc lại CSV, mặc dù các kiểu đối tượng Python tùy biến hoặc kiểu mở rộng đặc thù của pandas vẫn cần khai báo lược đồ chuyển đổi tương ứng khi ghi đọc.

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-9 -->

::: example Lưu trữ định hướng cột và đọc lọc trực tiếp trên đĩa với Parquet

Định dạng Apache Parquet tổ chức dữ liệu theo cột và lưu trữ siêu dữ liệu thống kê ở phần chân tệp, cho phép đọc lọc một tập con các cột và bỏ qua các bản ghi không thỏa mãn điều kiện ngay từ bước đọc đĩa. Ta thực hiện lưu trữ bảng sang tệp Parquet và nạp lại với tham số columns và filters để giảm lượng dữ liệu đọc.

```python
import os
import tempfile
import pandas as pd

df_hang = pd.DataFrame({
    "ma": ["P1", "P2", "P3"],
    "vung": ["Bac", "Nam", "Bac"],
    "so": [10, 25, 40]
})

with tempfile.NamedTemporaryFile(suffix=".parquet", delete=False) as tf:
    duong_dan = tf.name

try:
    df_hang.to_parquet(duong_dan, engine="pyarrow", index=False)
    df_doc = pd.read_parquet(
        duong_dan,
        columns=["ma", "so"],
        filters=[("so", ">=", 20)]
    )
    print(df_doc)
finally:
    if os.path.exists(duong_dan):
        os.remove(duong_dan)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| ma | so |
| --- | --- |
| P2 | 25 |
| P3 | 40 |

</div>

CSV ghi các trường của một hàng nối tiếp nhau trong văn bản. Khi chỉ cần vài cột, bộ đọc vẫn phải xử lý ranh giới trường. Parquet tổ chức các khối theo cột trong từng nhóm hàng, cho phép công cụ đọc chọn các khối cột cần dùng.

Phương thức `df.to_parquet` sử dụng công cụ `pyarrow` để nén và tuần tự hóa bảng dữ liệu xuống đĩa. Cột `vung` mang kiểu chuỗi và cột `so` mang kiểu số nguyên được mã hóa thành các khối nhị phân độc lập kèm theo phần siêu dữ liệu thống kê ghi lại giá trị nhỏ nhất và lớn nhất của từng khối.

`columns=["ma", "so"]` chọn hai cột đầu ra. `filters=[("so", ">=", 20)]` yêu cầu giữ những hàng đạt điều kiện. Công cụ `pyarrow` có thể bỏ qua các nhóm hàng dựa vào thống kê hoặc thông tin phân vùng. Với tệp nhỏ này, toàn bộ nhóm có thể vẫn phải đọc trước khi lọc.

Kết quả gồm P2 và P3 với số lượng 25 và 40. Ví dụ cần thư viện `pyarrow` để ghi và đọc Parquet. Bộ ba trong `filters` là tên cột, toán tử và giá trị so sánh, còn `index=False` tránh lưu chỉ mục pandas như một cột dữ liệu bổ sung.

:::

<!-- /worked-example -->

### 3.4. Ranh giới an toàn của Pickle

Module `pickle` là công cụ tuần tự hóa nhị phân mặc định của Python. Phương thức `df.to_pickle()` và hàm `pd.read_pickle()` cho phép đóng gói mọi đối tượng Python xuống đĩa và tái tạo lại chính xác.

Tuy nhiên, `pickle` tiềm ẩn một nguy cơ an ninh nghiêm trọng: **Lỗ hổng thực thi mã tùy ý (Arbitrary Code Execution)**.

Về mặt cơ chế: Khi một đối tượng được tuần tự hóa (*pickling*), Python có thể gọi phương thức `__reduce__` của đối tượng để sinh ra một hàm khởi tạo (*callable*) và danh sách đối số. Khi giải tuần tự hóa (*unpickling*), máy ảo của pickle sẽ tự động triệu gọi trực tiếp bất kỳ callable nào được ghi nhận trong luồng byte đó mà không cần gọi lại phương thức `__reduce__`. Kẻ tấn công có thể cấu tạo một luồng byte pickle chứa lời gọi tới các hàm thực thi lệnh hệ thống nguy hiểm (như hàm chạy tiến trình hệ điều hành). Khi người dùng gọi `pd.read_pickle()`, mã độc sẽ được kích hoạt ngay lập tức dưới quyền của tiến trình Python đang chạy.

> [!WARNING] Yêu cầu nguồn dữ liệu đáng tin cậy
> Chỉ sử dụng `pickle` để lưu tạm các đối tượng Python nội bộ giữa các bước xử lý trong một môi trường hoàn toàn kiểm soát được. Tuyệt đối không nạp tệp `pickle` nhận từ mạng Internet, tải về từ bên ngoài hoặc từ các nguồn chưa được xác thực độ tin cậy. Khi trao đổi dữ liệu giữa các hệ thống, hãy ưu tiên các định dạng dữ liệu có cấu trúc không mang mã thực thi nhúng như Parquet, Arrow, JSON hoặc CSV với bộ phân tích an toàn, đồng thời kiểm tra kích thước và giới hạn tài nguyên của tệp đầu vào.

---

## 4. Giao tiếp với Web API và cơ sở dữ liệu

Dữ liệu thực tế thường xuyên được truy xuất từ các giao diện lập trình ứng dụng qua web (*Web API*) hoặc các hệ quản trị cơ sở dữ liệu doanh nghiệp.

### 4.1. Tiêu thụ Web API và nguyên tắc lưu trữ phản hồi thô

Các dịch vụ web cung cấp dữ liệu qua giao thức HTTP/HTTPS. Thư viện `requests` là công cụ chuẩn mực trong Python để gửi các yêu cầu mạng. Khi xây dựng hàm thu thập dữ liệu từ Web API, một thiết kế tốt cần bảo đảm:
- Cho phép truyền vào `session` (hỗ trợ tái sử dụng kết nối TCP hoặc truyền session giả lập trong kiểm thử tự động).
- Thiết lập `timeout` rõ ràng để tránh treo tiến trình khi mạng gặp sự cố.
- Gọi `response.raise_for_status()` để phát hiện và ném lỗi tức thì khi máy chủ trả về mã lỗi HTTP ($4xx, 5xx$).
- **Lưu trực tiếp `response.content` (chuỗi byte nhị phân thô)** xuống tệp trước khi xử lý: Việc chuyển đổi JSON thành từ điển rồi dùng `json.dumps()` ghi lại không bảo toàn được luồng byte HTTP nguyên gốc (có thể làm thay đổi thứ tự khóa, khoảng trắng, định dạng số thực hoặc làm mất tính toàn vẹn của mã băm kiểm tra checksum).

```python
import io
import json
import os
import tempfile
import pandas as pd
import requests

def lay_va_luu_du_lieu_api(url, duong_dan_luu, session=None, timeout=10):
    """
    Gửi yêu cầu HTTP GET, kiểm tra lỗi, lưu luồng byte thô xuống đĩa
    và trích xuất dữ liệu JSON thành DataFrame.
    """
    s = session or requests.Session()
    phan_hoi = s.get(url, timeout=timeout)
    phan_hoi.raise_for_status()

    # Lưu chính xác luồng byte nhị phân nguyên bản từ HTTP, không tái tuần tự hóa dict
    with open(duong_dan_luu, "wb") as f:
        f.write(phan_hoi.content)

    du_lieu = phan_hoi.json()
    df = pd.DataFrame(du_lieu["quan_sat"])
    df["tram_do"] = du_lieu["tram_do"]
    return df

# Lớp giả lập phản hồi HTTP phục vụ kiểm thử offline không phụ thuộc mạng ngoài
class FakeResponse:
    def __init__(self, content_bytes, status_code=200):
        self.content = content_bytes
        self.status_code = status_code

    def raise_for_status(self):
        if self.status_code >= 400:
            raise requests.HTTPError(f"Lỗi HTTP {self.status_code}")

    def json(self):
        return json.loads(self.content.decode("utf-8"))

class FakeSession:
    def __init__(self, fake_response):
        self._fake_response = fake_response

    def get(self, url, timeout=10):
        return self._fake_response

du_lieu_http_goc = (
    b'{"tram_do": "HN_01", "quan_sat": ['
    b'{"gio": "08:00", "nhiet_do": 26.5, "do_am": 78}, '
    b'{"gio": "12:00", "nhiet_do": 32.0, "do_am": 65}, '
    b'{"gio": "16:00", "nhiet_do": 29.5, "do_am": 72}'
    b']}'
)

fake_session = FakeSession(FakeResponse(du_lieu_http_goc, status_code=200))

with tempfile.TemporaryDirectory() as thu_muc_tam:
    tep_tho = os.path.join(thu_muc_tam, "thoi_tiet_raw.json")
    df_thoi_tiet = lay_va_luu_du_lieu_api(
        "https://api.example.com/weather/hn01",
        tep_tho,
        session=fake_session,
        timeout=5
    )
    # Kiểm tra luồng byte lưu trên đĩa trùng khớp 100% dữ liệu gốc
    with open(tep_tho, "rb") as f:
        noi_dung_luu = f.read()
    assert noi_dung_luu == du_lieu_http_goc
    assert df_thoi_tiet["nhiet_do"].max() == 32.0

print("DataFrame trích xuất từ dữ liệu API:")
print(df_thoi_tiet)
```

Hai lợi ích thực tiễn của nguyên tắc **Lưu trữ Phản hồi Thô (Raw Response Persistence)**:
1. **Tính tái lập (Reproducibility)**: Khi logic nghiệp vụ thay đổi hoặc cần bóc tách thêm trường dữ liệu mới (chẳng hạn tọa độ trạm đo), ta có thể chạy lại mã nguồn từ tệp thô đã lưu mà không phụ thuộc vào trạng thái của máy chủ bên ngoài.
2. **Bảo toàn hạn ngạch (Rate Limit)**: Tránh nguy cơ bị khóa tài khoản hoặc gián đoạn thử nghiệm do chạm ngưỡng giới hạn số lần gọi API trong ngày của nhà cung cấp.

### 4.2. Tương tác với cơ sở dữ liệu quan hệ (SQL)

Thư viện pandas kết hợp với `sqlite3` hoặc `SQLAlchemy` cho phép tương tác trực tiếp với các hệ quản trị cơ sở dữ liệu quan hệ (PostgreSQL, MySQL, SQLite):
- `to_sql`: Xuất cấu trúc DataFrame thành bảng trong cơ sở dữ liệu (`if_exists="replace"`, `"append"`).
- `read_sql` hoặc `read_sql_query`: Nạp dữ liệu từ câu truy vấn SQL trực tiếp thành DataFrame.

Nguyên tắc tối ưu hóa hàng đầu của kỹ sư dữ liệu là: **Lọc tại nguồn (Filter at Source)**. Luôn đẩy các phép lọc hàng (`WHERE`), phép chọn cột và tổng hợp nhóm (`GROUP BY`) xuống động cơ cơ sở dữ liệu thực thi, chỉ kéo về máy khách phần kết quả tinh gọn nhất:

```python
import sqlite3

ket_noi = sqlite3.connect(":memory:")

# Ghi dữ liệu mẫu vào cơ sở dữ liệu SQLite trong bộ nhớ
df_nhan_vien.to_sql("nhan_vien", ket_noi, if_exists="replace", index=True)

# Thực thi truy vấn lọc trực tiếp tại cơ sở dữ liệu
cau_lenh_sql = """
SELECT ma_so, ho_ten, luong
FROM nhan_vien
WHERE luong >= 1950
ORDER BY luong DESC
"""

df_loc_sql = pd.read_sql_query(cau_lenh_sql, ket_noi, index_col="ma_so")
print("Kết quả lọc từ SQL:")
print(df_loc_sql)
assert len(df_loc_sql) == 2
ket_noi.close()
```

<!-- worked-example bai-06-ket-noi-truy-xuat-du-lieu-worked-10 -->

::: example Ghi bảng và thực thi truy vấn tham số hóa với SQLite

Khi làm việc với các hệ cơ sở dữ liệu quan hệ, việc lọc dữ liệu trực tiếp trong câu lệnh SQL giúp giảm lượng bản ghi truyền tải về ứng dụng. Ta sử dụng to_sql để nạp bảng và dùng read_sql_query với cơ chế truyền tham số params an toàn nhằm lọc dữ liệu ngay tại nguồn.

```python
import sqlite3
import pandas as pd

ket_noi = sqlite3.connect(":memory:")

df_hang = pd.DataFrame({
    "id": [1, 2, 3],
    "ten": ["Ao", "Quan", "Mu"],
    "gia": [150, 220, 80]
})

df_hang.to_sql("san_pham", ket_noi, index=False)

df_loc = pd.read_sql_query(
    "SELECT ten, gia FROM san_pham WHERE gia >= ?",
    ket_noi,
    params=[100]
)
ket_noi.close()
print(df_loc)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| ten | gia |
| --- | --- |
| Ao | 150 |
| Quan | 220 |

</div>

Trong các hệ thống xử lý dữ liệu, cơ sở dữ liệu quan hệ là nơi lưu trữ tập trung có khả năng đánh chỉ mục và thực hiện các phép lọc dữ liệu hiệu quả. Thay vì nạp toàn bộ một bảng lớn vào bộ nhớ máy tính rồi mới dùng lệnh lọc của pandas, việc đẩy phép toán lọc xuống cơ sở dữ liệu giúp chỉ kéo về những bản ghi thực sự cần thiết.

Phương thức `df.to_sql('san_pham', ket_noi, index=False)` tự động tạo bảng tương ứng trong SQLite dựa trên lược đồ cột của `DataFrame`. Việc thiết lập `index=False` bảo đảm cột chỉ mục số nguyên của pandas không bị ghi thừa vào lược đồ cơ sở dữ liệu.

Khi thực hiện truy vấn với `pd.read_sql_query`, việc tự ý nối chuỗi biến số trực tiếp vào câu lệnh SQL dễ tạo ra lỗ hổng bảo mật. Ta sử dụng ký tự giữ chỗ `?` trong câu lệnh `WHERE gia >= ?` và truyền giá trị cụ thể qua danh sách tham số `params=[100]`.

Động cơ SQLite sẽ phân tích cấu trúc câu truy vấn trước, sau đó mới gắn giá trị tham số vào để thực thi: Hai bản ghi sản phẩm có giá từ 100 trở lên gồm Ao và Quan được trích xuất thành một `DataFrame` mới. Cách làm này bảo đảm an toàn truy vấn và giảm thiểu lượng dữ liệu trung gian.

:::

<!-- /worked-example -->

### 4.3. Truy vấn dữ liệu phân tích tại chỗ với DuckDB

Đối với bài toán phân tích các tệp dữ liệu cục bộ lớn, việc cài đặt các hệ quản trị cơ sở dữ liệu truyền thống gây tốn kém thời gian cấu hình và quản trị. Dự án **DuckDB** ra đời như một hệ cơ sở dữ liệu phân tích nhúng chạy trực tiếp bên trong tiến trình của ứng dụng:
- **Định hướng cột (Columnar Engine)**: Tối ưu hóa cho các phép toán tổng hợp phân tích (*OLAP*).
- **Truy vấn trực tiếp không cần bước nạp trước**: DuckDB có khả năng quét và thực thi các câu truy vấn SQL trực tiếp trên các tệp CSV (thông qua trình phân tích cú pháp theo khối) hoặc đọc trực tiếp các khối cột Parquet trên đĩa cứng mà không cần nạp toàn bộ vào bảng cơ sở dữ liệu nội bộ trước. Cần lưu ý rằng việc quét CSV trực tiếp đòi hỏi giải mã chuỗi văn bản thành các kiểu dữ liệu trong bộ nhớ chứ không phải là thao tác sao chép không bộ nhớ (*zero-copy*).
- **Tích hợp sâu với pandas**: Kết quả truy vấn SQL của DuckDB có thể chuyển đổi thành DataFrame thông qua phương thức `.df()`.

---

## 6. Tổng kết

1. **Kiểm soát ký tự khuyết thiếu**: Luôn thận trọng với các quy ước mặc định của `read_csv`. Thiết lập `keep_default_na=False` và chỉ định `na_values` chính xác để không làm sai lệch các mã định danh hợp lệ như `"NA"`.
2. **Khai thác kỹ thuật đọc phân đoạn**: Sử dụng `chunksize` để xử lý các tệp dữ liệu vượt quá kích thước RAM khả dụng, tích lũy thống kê qua từng khối để bảo vệ tài nguyên hệ thống.
3. **Khai thác định dạng cột Parquet**: Thay thế các tệp CSV trung gian bằng Apache Parquet để tiết kiệm dung lượng lưu trữ, tăng tốc độ truy xuất cột và lưu giữ lược đồ kiểu dữ liệu kỹ thuật.
4. **Nhận thức ranh giới an toàn của Pickle**: Chỉ sử dụng pickle trong môi trường nội bộ đáng tin cậy. Tuyệt đối không nạp tệp pickle từ nguồn lạ nhằm loại trừ nguy cơ máy ảo pickle tự động kích hoạt các hàm thực thi mã độc tùy ý.
5. **Kỷ luật lưu trữ phản hồi thô**: Luôn lưu trực tiếp chuỗi byte HTTP thô (`response.content`) nhận từ Web API xuống đĩa trước khi trích xuất bảng biểu nhằm bảo đảm tính tái lập và bảo vệ dữ liệu nguyên gốc.
6. **Đẩy tác vụ xuống tầng cơ sở dữ liệu**: Sử dụng các câu truy vấn SQL hoặc tận dụng sức mạnh tính toán tại chỗ của DuckDB để lọc và tổng hợp dữ liệu ngay tại nguồn trước khi kéo về bộ nhớ.

---

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 6: Data Loading, Storage, and File Formats](https://wesmckinney.com/book/accessing-data).
- Tài liệu chính thức pandas: [IO tools (Text, CSV, HDF5, Parquet, SQL)](https://pandas.pydata.org/docs/user_guide/io.html).
- Tài liệu chính thức DuckDB: [DuckDB Python API & SQL on Parquet/CSV](https://duckdb.org/docs/api/python/overview).
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 5. Bài tập rèn luyện

<span id="iai-06-bai-1"></span>

::: exercise Bài tập 1: Đọc bảng giá có mã khu đặc biệt
Một tệp dữ liệu giả lập `gia_theo_khu.csv` lưu trữ thông tin giá phòng như sau:

```text
khu,gia
NA,100
TB,80
NA,
TB,0
```

Trong đó: Ký hiệu `NA` là mã khu vực hợp lệ (không phải giá trị thiếu), ô trống là trường hợp chưa ghi nhận được giá, và giá trị `0` là mức giá đã được ghi nhận thực tế. Hãy viết mã nguồn nạp tệp dữ liệu này và tính giá trung bình theo từng khu vực sao cho kết quả hoàn toàn chuẩn xác.
:::

::: solution Lời giải
Trọng tâm kỹ thuật của bài toán là vô hiệu hóa danh sách giá trị thiếu mặc định để bảo toàn mã khu `NA`, đồng thời chỉ định ô trống ở cột `gia` là giá trị khuyết thiếu:

```python
csv_gia = """khu,gia
NA,100
TB,80
NA,
TB,0
"""

df_gia = pd.read_csv(
    io.StringIO(csv_gia),
    keep_default_na=False,
    na_values={"gia": [""]}
)

# Tính giá trung bình theo từng khu vực
ket_qua = df_gia.groupby("khu")["gia"].mean()
print(ket_qua)

# Kiểm tra tính đúng đắn của phép tính
assert ket_qua["NA"] == 100.0
assert ket_qua["TB"] == 40.0
```

Khu `NA` có hai quan sát gồm giá trị 100 và ô trống. Vì ô trống bị bỏ qua nên giá trung bình của khu này là 100. Khu `TB` có hai quan sát là 80 và 0, do đó giá trung bình là $(80 + 0) / 2 = 40{,}0$.
:::

<span id="iai-06-bai-2"></span>

::: exercise Bài tập 2: Lọc ngày nóng từ dữ liệu API thời tiết
Dữ liệu dự báo thời tiết trả về từ cổng dịch vụ có cấu trúc JSON như sau:

```python
phan_hoi_api = {
    "timezone": "America/Phoenix",
    "daily_units": {"temperature_2m_max": "°F"},
    "daily": {
        "time": ["2026-10-01", "2026-10-02", "2026-10-03"],
        "temperature_2m_max": [95, 100, 88]
    }
}
```

Nhiệt độ tối đa hàng ngày đang được tính theo thang độ Fahrenheit (°F). Công thức chuyển đổi sang thang độ Celsius (°C) là:
$$
T_{(^\circ\text{C})} = \frac{T_{(^\circ\text{F})} - 32}{1{,}8}
$$
Hãy tạo một DataFrame từ dữ liệu trên, bổ sung cột nhiệt độ tính theo độ C, và lọc ra danh sách các ngày có nhiệt độ tối đa từ $35^\circ\text{C}$ trở lên.
:::

::: solution Lời giải
Ta trích xuất từ điển con `daily` để tạo DataFrame, sau đó áp dụng phép toán vector hóa trên cột để đổi đơn vị:

```python
import numpy as np

phan_hoi_api = {
    "timezone": "America/Phoenix",
    "daily_units": {"temperature_2m_max": "°F"},
    "daily": {
        "time": ["2026-10-01", "2026-10-02", "2026-10-03"],
        "temperature_2m_max": [95, 100, 88]
    }
}

df_thoi_tiet = pd.DataFrame(phan_hoi_api["daily"])
df_thoi_tiet["nhiet_do_c"] = (df_thoi_tiet["temperature_2m_max"] - 32) / 1.8

ngay_nong = df_thoi_tiet[df_thoi_tiet["nhiet_do_c"] >= 35]
print("Các ngày có nhiệt độ tối đa từ 35 độ C trở lên:")
print(ngay_nong[["time", "nhiet_do_c"]])

assert ngay_nong["time"].tolist() == ["2026-10-01", "2026-10-02"]
np.testing.assert_allclose(df_thoi_tiet["nhiet_do_c"], [35.0, 37.777778, 31.111111], rtol=1e-5)
```

Nhiệt độ sau khi chuyển đổi lần lượt là $35{,}0^\circ\text{C}$, $37{,}8^\circ\text{C}$ và $31{,}1^\circ\text{C}$. Hai ngày thỏa mãn điều kiện là `2026-10-01` và `2026-10-02`.
:::

<span id="iai-06-bai-3"></span>

::: exercise Bài tập 3: Đếm số chỗ ở thiếu giá theo từng khu bằng SQL
Cho bảng dữ liệu `cho_o` được lưu trữ trong cơ sở dữ liệu với các bản ghi như sau:

| id | khu | gia |
| :--- | :--- | :--- |
| 001 | A | 100 |
| 002 | B | 80 |
| 003 | A | 200 |
| 004 | B | 120 |
| 005 | A | NULL |

Hãy viết một câu truy vấn SQL đếm số chỗ ở chưa có thông tin giá của từng khu vực. Yêu cầu: Kết quả phải hiển thị đầy đủ mọi khu vực, kể cả khu vực không có chỗ ở nào bị thiếu giá.
:::

::: solution Lời giải
Nếu sử dụng mệnh đề `WHERE gia IS NULL` kết hợp với `GROUP BY khu`, khu `B` sẽ bị loại bỏ hoàn toàn khỏi bảng kết quả vì không có dòng nào thỏa mãn điều kiện lọc.

Giải pháp chuẩn mực là lấy tổng số bản ghi trừ đi số bản ghi có giá trị ở cột `gia` (hàm `COUNT(gia)` tự động bỏ qua các giá trị `NULL`):

```python
ket_noi = sqlite3.connect(":memory:")

df_bai_tap = pd.DataFrame({
    "id": ["001", "002", "003", "004", "005"],
    "khu": ["A", "B", "A", "B", "A"],
    "gia": [100.0, 80.0, 200.0, 120.0, None]
})
df_bai_tap.to_sql("cho_o", ket_noi, if_exists="replace", index=False)

cau_truy_van = """
SELECT khu, COUNT(*) - COUNT(gia) AS so_thieu
FROM cho_o
GROUP BY khu
ORDER BY khu ASC
"""

df_dem_thieu = pd.read_sql_query(cau_truy_van, ket_noi)
print(df_dem_thieu)

assert df_dem_thieu.to_dict("records") == [
    {"khu": "A", "so_thieu": 1},
    {"khu": "B", "so_thieu": 0}
]
ket_noi.close()
```

Khu `A` có 3 bản ghi nhưng chỉ có 2 bản ghi có giá, số lượng thiếu là $3 - 2 = 1$. Khu `B` có 2 bản ghi và cả 2 đều có giá, số lượng thiếu là $2 - 2 = 0$.
:::

---




<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-06">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-06.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 6: Data Loading, Storage, and File Formats](https://wesmckinney.com/book/accessing-data).
- Tài liệu chính thức pandas: [IO tools (Text, CSV, HDF5, Parquet, SQL)](https://pandas.pydata.org/docs/user_guide/io.html).
- Tài liệu chính thức DuckDB: [DuckDB Python API & SQL on Parquet/CSV](https://duckdb.org/docs/api/python/overview).
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
