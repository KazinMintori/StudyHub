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

### 1.2. Kiểm soát giá trị khuyết thiếu và bẫy quy ước quốc tế

Mỗi nguồn dữ liệu lại sở hữu một quy ước riêng để đánh dấu ô trống, chẳng hạn `"N/A"`, `"NaN"`, `"NULL"` hoặc `"-999"`. Hàm `read_csv` có sẵn một danh sách các chuỗi mặc định được tự động nhận diện là giá trị khuyết thiếu (`np.nan`).

Tuy nhiên, cơ chế tự động này tiềm ẩn cạm bẫy kỹ thuật nghiêm trọng. Xét bài toán xử lý mã quốc gia theo tiêu chuẩn quốc tế ISO alpha-2: Quốc gia Namibia có mã chính thức là `"NA"`. Nếu nạp dữ liệu một cách mặc định, pandas sẽ tự ý chuyển mã quốc gia `"NA"` của Namibia thành giá trị khuyết thiếu `NaN`.

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

### 1.4. Ghi dữ liệu ra định dạng văn bản

Phương thức `to_csv` cho phép lưu cấu trúc DataFrame xuống đĩa hoặc luồng văn bản. Các tham số kỹ thuật cần kiểm soát:
- `sep`: Ký tự phân cách giữa các cột (mặc định là dấu phẩy `,`).
- `na_rep`: Chuỗi ký tự đại diện cho các ô khuyết thiếu khi ghi ra tệp (ví dụ `na_rep="NULL"`).
- `index=False`: Bỏ qua cột chỉ mục hàng nếu chỉ mục chỉ là dãy số tự tăng vô nghĩa, tránh tạo thêm cột thừa khi nạp lại.
- `header=False`: Loại bỏ dòng tiêu đề cột khi cần nối tiếp dữ liệu vào tệp đã có.

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
