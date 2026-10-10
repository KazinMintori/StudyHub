---
course: xu-ly-du-lieu
lecture: bai-06-ket-noi-truy-xuat-du-lieu
section: lecture
title: "Đọc, lưu trữ & truy xuất dữ liệu"
prerequisites: ["dictionary", "ham-lap-trinh", "gia-tri-thieu"]
lessonStatus: ready
description: "Đọc chọn lọc tệp lớn với usecols, làm sạch giá chuỗi, định dạng Parquet định hướng cột, tiêu thụ API và truy vấn SQL tại chỗ bằng DuckDB."
---

## 1. Kỹ thuật Nạp Tệp CSV An toàn Chống lỗi và Xác thực Cấu trúc Dữ liệu

Trong môi trường phân tích dữ liệu thực tế, các tệp dữ liệu thường có dung lượng rất lớn với hàng chục, thậm chí hàng trăm cột thông tin. Chẳng hạn, tệp `listings_full.csv.gz` của Inside Airbnb chứa tới $90$ cột thuộc tính khác nhau.

Nếu bạn thực thi lệnh `pd.read_csv("listings_full.csv.gz")` một cách ngây thơ, máy tính sẽ phải giải nén và nạp toàn bộ $90$ cột vào bộ nhớ RAM. Điều này không chỉ gây lãng phí bộ nhớ nghiêm trọng mà còn khiến thời gian nạp tệp kéo dài hàng chục giây.

<DataDiagram name="csv-loading" />

### 1.1. Nạp Chọn lọc với `usecols` và `parse_dates`
Kỹ thuật chuẩn mực của một kỹ sư dữ liệu là chỉ nạp đúng những cột phục vụ trực tiếp cho bài toán thông qua tham số `usecols`, đồng thời ép kiểu thời gian ngay tại tầng đọc tệp bằng `parse_dates`:

```python
import pandas as pd

cot_can_doc = ["id", "room_type", "price", "first_review", "number_of_reviews"]
cot_ngay = ["first_review"]

df = pd.read_csv(
    "listings_full.csv.gz",
    usecols=cot_can_doc,
    parse_dates=cot_ngay
)
```

Hai lợi ích kỹ thuật cốt lõi:
1. **Tiết kiệm tài nguyên**: Giảm thiểu tới $80\% - 90\%$ lượng bộ nhớ RAM cần thiết, ngăn ngừa hoàn toàn nguy cơ sập hệ thống do tràn bộ nhớ (*Out-Of-Memory*).
2. **Ép kiểu chuẩn xác**: Cột ngày tháng được chuyển đổi ngay thành định dạng `datetime64[ns]`, các ô trống tự động biến thành `NaT` (*Not a Time*), sẵn sàng cho các phép toán thời gian tiếp theo mà không cần gọi thêm lệnh chuyển đổi phụ.

### 1.2. Khóa Kiểu Cột Định danh và Kiểm soát Dấu hiệu Khuyết thiếu
- **Khóa kiểu chuỗi cho mã số**: Luôn chỉ định `dtype={"id": "string"}` nếu mã định danh có chứa các số 0 ở đầu, tránh việc pandas tự ý ép kiểu về số nguyên và làm mất mát thông tin.
- **Dấu hiệu khuyết thiếu `na_values`**: Mỗi nguồn dữ liệu lại có một quy ước ghi nhận ô trống dị biệt (`"N/A"`, `"chua_ro"`, `"-999"`). Hãy dùng `na_values` để chuẩn hóa chúng về `NaN`.
- *Cảnh báo về bẫy Namibia*: Quốc gia Namibia có mã tiêu chuẩn quốc tế ISO alpha-2 là `"NA"`. Nếu nạp tệp quốc gia mà không thiết lập `keep_default_na=False`, pandas sẽ tự động biến tên nước Namibia thành giá trị khuyết thiếu một cách oan uổng.

---

## 2. Kỹ thuật Làm sạch Chuỗi Tiền tệ và Bẫy Ký tự Neo Regex

Trong các tệp trích xuất từ hệ thống tài chính hoặc nền tảng thương mại, dữ liệu giá thường được lưu trữ dưới dạng chuỗi văn bản kèm ký hiệu tiền tệ và dấu phân cách hàng nghìn, chẳng hạn: `"$45,647.00"`.

Để chuyển chuỗi này về dạng số thực `float64` có thể tính toán được, ta cần loại bỏ ký tự `$` và dấu phẩy `,`.

### Bẫy Ký tự Neo trong Biểu thức Chính quy (Regex)
Trong cú pháp của biểu thức chính quy (*Regular Expression*), ký tự `$` là một **ký tự siêu đặc biệt (Meta-character)**, đóng vai trò là ký tự neo đại diện cho **vị trí cuối cùng của chuỗi văn bản**.
Nếu bạn viết:
```python
# CÁCH LÀM SAI LẦM:
s.str.replace("$", "", regex=True)
```
pandas sẽ tìm vị trí cuối chuỗi và thay thế nó bằng chuỗi rỗng! Ký tự `$` thực tế ở đầu chuỗi hoàn toàn không bị xóa, và lệnh ép kiểu `astype(float)` sau đó sẽ sập ngay lập tức với lỗi `ValueError`.

**Giải pháp chuẩn mực**: Luôn chỉ định tường minh tham số `regex=False` khi muốn thay thế các ký tự văn bản thông thường:
```python
# CÁCH LÀM CHUẨN MỰC:
gia_sach = prices.str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)
```

---

## 3. Định dạng Lưu trữ: CSV vs Apache Parquet

Trong quá trình xây dựng các đường ống dữ liệu, việc lựa chọn định dạng lưu trữ trung gian giữa các bước xử lý đóng vai trò quyết định đến hiệu năng tổng thể của toàn bộ hệ thống.

<DataDiagram name="csv-parquet" />

### 3.1. Bản chất Định hướng Cột của Parquet
- Trong tệp CSV, dữ liệu được ghi lần lượt từng dòng từ trái sang phải. Nếu bạn chỉ cần đọc đúng một cột giá tiền trong bảng 90 cột, hệ điều hành vẫn buộc phải nạp toàn bộ $100\%$ dung lượng tệp từ đĩa cứng vào bộ nhớ rồi mới bóc tách được cột đó.
- Ngược lại, Apache Parquet tổ chức dữ liệu theo từng cột riêng biệt. Khi bạn chỉ truy vấn cột `price`, trình điều khiển chỉ cần nhảy cóc đến đúng các dải byte của cột đó và nạp vào bộ nhớ.

### 3.2. Tính Bảo toàn Siêu dữ liệu Kiểu (*Type Preservation*)
Khi bạn xuất một DataFrame có cột ngày `first_review` (kiểu `datetime64[ns]`) ra tệp CSV bằng `df.to_csv("data.csv")`, tệp CSV chỉ lưu chuỗi văn bản `"2023-03-15"`. Khi đọc lại bằng `pd.read_csv("data.csv")`, cột này sẽ bị giáng cấp thành kiểu chuỗi `object`, và bạn lại phải mất công ép kiểu lần thứ hai.
Nếu xuất ra Parquet bằng `df.to_parquet("data.parquet")`, toàn bộ cấu trúc kiểu dữ liệu kỹ thuật (`int64`, `float64`, `datetime64`) đều được lưu trữ nguyên vẹn trong phần siêu dữ liệu của tệp nhị phân. Khi đọc lại, dữ liệu lập tức sẵn sàng sử dụng với kiểu gốc ban đầu.

---

## 4. Nguyên tắc Tiêu thụ Web API và Lưu trữ Phản hồi Thô

Khi thu thập dữ liệu từ các dịch vụ web bên ngoài (chẳng hạn như dữ liệu thời tiết lịch sử từ Open-Meteo API), một nguyên tắc bất biến của các kỹ sư dữ liệu là: **Lưu trữ Phản hồi Thô (*Raw Response Persistence*)**.

<DataDiagram name="api-provenance" />

### Vì sao phải lưu tệp JSON thô trước khi chuyển thành bảng?
1. **Tính tái lập (*Reproducibility*)**: Nếu sau này bạn phát hiện mã nguồn chuyển đổi bảng bị sai logic hoặc cần trích xuất thêm một trường thông tin mới (như độ ẩm hay tốc độ gió), bạn chỉ cần đọc lại tệp JSON đã lưu trên đĩa mà không cần gọi lại API.
2. **Bảo vệ giới hạn tần suất (*Rate Limit*)**: Hầu hết các dịch vụ API đều giới hạn số lượng cuộc gọi trong ngày. Việc lưu trữ cục bộ giúp bạn có thể chạy thử nghiệm mã nguồn hàng trăm lần mà không sợ bị nhà cung cấp khóa tài khoản.
3. **Phòng vệ trước sự cố mạng**: Trong các bài kiểm thử tự động (*CI/CD*) hoặc môi trường chấm bài ngắt kết nối mạng, đường ống dữ liệu vẫn vận hành trơn tru nhờ tệp dữ liệu thô đã được lưu trữ sẵn.

---

## 5. Truy vấn SQL Tại chỗ Hiệu năng cao với DuckDB

Trong nhiều thập kỷ, khi muốn sử dụng ngôn ngữ truy vấn SQL, lập trình viên buộc phải cài đặt các hệ quản trị cơ sở dữ liệu cồng kềnh như PostgreSQL hay MySQL.
Năm 2019, dự án **DuckDB** ra đời và nhanh chóng trở thành một hiện tượng công nghệ, được mệnh danh là "SQLite của ngành phân tích dữ liệu".

### 5.1. Sức mạnh của DuckDB
- **Không cần máy chủ (Serverless)**: DuckDB chạy nhúng trực tiếp bên trong tiến trình Python của bạn dưới dạng một thư viện C++ siêu nhẹ.
- **Thực thi trực tiếp trên tệp đĩa**: DuckDB có thể chạy các câu truy vấn SQL phức tạp (gồm `GROUP BY`, `JOIN`, hàm cửa sổ) trực tiếp trên các tệp `CSV`, `Parquet` hoặc `JSON` mà không cần bước nạp dữ liệu (*Ingestion*) vào cơ sở dữ liệu trước:
  ```python
  import duckdb

  # Chạy SQL trực tiếp trên tệp CSV và trả về pandas DataFrame:
  ket_qua = duckdb.query("""
      SELECT year(date) AS nam, count(*) AS n
      FROM 'reviews.csv'
      GROUP BY nam
      ORDER BY nam ASC
  """).df()
  ```
- **Xử lý tệp vượt RAM mượt mà**: Nhờ kỹ thuật thực thi luồng (*Streaming Execution*) và định dạng vector hóa, DuckDB có thể xử lý tệp CSV hàng chục triệu dòng với dung lượng RAM chỉ vài trăm Megabyte.

---

## 6. Bài tập Thực chiến Phòng Lab 06 (100% Nội dung Lab) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 7. Tổng kết Bài học

1. **Nạp dữ liệu có chọn lọc**: Sử dụng `usecols` và `parse_dates` để giảm thiểu tối đa tài nguyên I/O và RAM khi làm việc với các bảng dữ liệu khổng lồ.
2. **Kỷ luật với chuỗi tiền tệ**: Luôn thiết lập `regex=False` khi sử dụng `.str.replace()` để xử lý các ký hiệu tiền tệ `$`.
3. **Ưu tiên định dạng Parquet**: Sử dụng Parquet cho dữ liệu trung gian để tiết kiệm dung lượng đĩa và bảo toàn nguyên vẹn kiểu dữ liệu kỹ thuật.
4. **Lưu trữ phản hồi thô**: Luôn ghi tệp JSON thô từ Web API xuống đĩa trước khi trích xuất bảng biểu.
5. **Khai thác sức mạnh DuckDB**: Tận dụng DuckDB để truy vấn SQL tức thì trên các tệp đĩa mà không cần cài đặt máy chủ cơ sở dữ liệu cồng kềnh.
