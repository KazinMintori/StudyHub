---
course: xu-ly-du-lieu
lecture: bai-08-du-lieu-thoi-gian
section: lecture
title: "Chuỗi thời gian"
prerequisites: ["dataframe", "chi-muc"]
lessonStatus: ready
hasChapterExercises: true
description: "Làm chủ chuỗi thời gian trong pandas: DatetimeIndex, quản trị múi giờ, lấy mẫu lại resample, chu kỳ Period, cửa sổ trượt rolling và so sánh cùng kỳ YoY vs MoM."
---


<div class="lecture-notes-content">

Giả sử một tệp nhật ký ghi nhận cùng mốc thời gian 08:00 tại hai máy chủ đặt ở hai thành phố khác nhau: Hà Nội và Tokyo. Liệu đó có phải là cùng một thời điểm vật lý, và tệp nhật ký đang thiếu thông tin gì để có thể đối chiếu chính xác? Nếu thiếu thông tin múi giờ, hai chuỗi thời gian trông giống nhau về mặt số học nhưng thực chất lại lệch nhau hai tiếng đồng hồ trong thế giới thực.

Bên cạnh múi giờ, dữ liệu thời gian trong thực tế còn gắn với các quy ước lịch: Năm nhuận có 366 ngày, số ngày giữa các tháng không đều nhau, và quy ước đổi giờ mùa hè có thể làm đồng hồ dịch chuyển. Nếu xử lý bằng cách ghép chuỗi hoặc chia số nguyên đơn thuần, các phép tính thống kê chuỗi thời gian sẽ không phản ánh đúng thực tế.

Bài giảng này trình bày phương pháp xử lý dữ liệu chuỗi thời gian trong Python và pandas: Phân biệt ba phạm trù thời gian, kỹ thuật quản trị múi giờ, các phép cắt lát chuỗi trên `DatetimeIndex`, cấu trúc kỳ `Period`, kỹ thuật lấy mẫu lại (`resample`), làm mượt dao động bằng cửa sổ trượt (`rolling` và `ewm`), cùng phương pháp so sánh cùng kỳ.

---

## 1. Ba phạm trù: Điểm thời gian, Khoảng thời gian và Kỳ

Để tư duy mạch lạc và tránh những lỗi sai khi lập trình, ta cần phân biệt ba khái niệm thời gian khác nhau trong phân tích dữ liệu:

1. **Điểm thời gian (Timestamp)**: Đại diện cho một khoảnh khắc cố định duy nhất trên trục thời gian liên tục, chẳng hạn đúng 09:15:30 ngày 15 tháng 3 năm 2026. Trong pandas, đối tượng đại diện là `pd.Timestamp` (tương đương với `datetime.datetime` của Python chuẩn nhưng hỗ trợ độ phân giải micro giây hoặc nano giây).
2. **Khoảng thời gian (Timedelta)**: Đại diện cho độ dài của một khoảng cách thời gian giữa hai biến cố, không gắn với bất kỳ ngày tháng cụ thể nào, chẳng hạn khoảng thời gian kéo dài 48 giờ hoặc 3 ngày 5 tiếng. Đối tượng tương ứng là `pd.Timedelta`.
3. **Kỳ (Period)**: Đại diện cho một khoảng thời gian hữu hạn gắn liền với một nhịp lịch thiên văn hay lịch tài chính, ví dụ trọn vẹn tháng 3 năm 2026 hoặc Quý 2 năm 2026. Một thời điểm nằm trong tháng 3 không đồng nghĩa với toàn bộ khoảng thời gian của tháng 3. Đối tượng đại diện là `pd.Period`.

```python
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

# 1. Điểm thời gian (Timestamp)
t1 = pd.Timestamp("2026-03-15 09:15:30")
t2 = pd.Timestamp("2026-03-18 15:30:00")

# 2. Khoảng thời gian (Timedelta) sinh ra từ hiệu của hai Timestamp
khoang_thoi_gian = t2 - t1
khoang_cach = khoang_thoi_gian
print("Khoảng thời gian:", khoang_thoi_gian)      # 3 days 06:14:30
print("Số ngày thực tế:", khoang_thoi_gian.days)  # 3
print("Tổng số giây:", khoang_thoi_gian.total_seconds())

# 3. Kỳ (Period)
ky_thang = pd.Period("2026-03", freq="M")
print("Kỳ tháng 3:", ky_thang)
print("Bắt đầu:", ky_thang.start_time, "-> Kết thúc:", ky_thang.end_time)
```

Khi chuyển đổi văn bản sang ngày tháng, hai điểm quan trọng cần lưu ý là định dạng ngày tháng và việc xử lý dữ liệu không hợp lệ:

- **Chỉ định tường minh định dạng bằng tham số `format`**: Chuỗi `"02/03/2026"` đối với người Việt Nam hay người Anh là ngày 2 tháng 3, nhưng đối với người Mỹ lại là ngày 3 tháng 2. Nếu không chỉ định tường minh `format="%d/%m/%Y"`, pandas sẽ phải tự phỏng đoán dựa trên dữ liệu mẫu và có thể hoán đổi ngày thành tháng khi ngày nhỏ hơn hoặc bằng 12.
- **Xử lý chuỗi không hợp lệ bằng `errors="coerce"`**: Tháng 2 không có ngày 30 hay 31. Khi gặp chuỗi không hợp lệ như `"31/02/2026"`, nếu để mặc định chương trình sẽ ném ngoại lệ dừng thực thi. Tham số `errors="coerce"` sẽ chuyển các giá trị lỗi này thành giá trị **`NaT`** (*Not a Time*, hằng số khuyết thiếu chuẩn dành riêng cho dữ liệu thời gian trong pandas).

```python
chuoi_ngay = pd.Series(["01/02/2026", "15/02/2026", "31/02/2026", "chua_xac_dinh"])
ngay_chuan = pd.to_datetime(chuoi_ngay, format="%d/%m/%Y", errors="coerce")

print("Kết quả chuẩn hóa:")
print(ngay_chuan)
print("Mảng nhận diện khuyết thiếu:", ngay_chuan.isna().tolist())
```

---

## 2. Quản trị múi giờ: Phân biệt localize và convert

Một vấn đề phổ biến trong các hệ thống lưu trữ dữ liệu là việc ghi nhận thời gian dưới dạng chuỗi hoặc số nguyên mà không kèm thông tin múi giờ. Khi hệ thống mở rộng đa quốc gia, thời điểm 08:00 sáng tại Tokyo (UTC+9) dễ bị nhầm lẫn với 08:00 sáng tại Hà Nội (UTC+7) hoặc London (UTC+0), dẫn đến việc đối chiếu giao dịch bị sai lệch thời điểm vật lý.

Trong pandas, dữ liệu thời gian được phân loại thành hai trạng thái:
- **Thời gian chưa gắn múi giờ (Timezone-naive)**: Dữ liệu chỉ ghi nhận giờ số học đơn thuần, không chứa thông tin về độ lệch múi giờ so với giờ phối hợp quốc tế (UTC).
- **Thời gian đã gắn múi giờ (Timezone-aware)**: Dữ liệu gắn liền với một múi giờ cụ thể theo chuẩn cơ sở dữ liệu quốc tế IANA (ví dụ: `Asia/Ho_Chi_Minh`, `Europe/London`, `America/New_York`).

Hai phép toán quản trị múi giờ mang ý nghĩa hoàn toàn khác nhau:

```python
# Tạo điểm thời gian chưa gắn múi giờ (tz-naive)
t_chua_mui_gio = pd.Timestamp("2026-03-15 08:00:00")

# 1. tz_localize: Gán thông tin múi giờ thực địa cho dữ liệu chưa gắn múi giờ
# Giữ nguyên số giờ hiển thị, chỉ gắn thêm ngữ cảnh múi giờ địa phương
t_ha_noi = t_chua_mui_gio.tz_localize("Asia/Ho_Chi_Minh")
print("Giờ Hà Nội:", t_ha_noi)  # 2026-03-15 08:00:00+07:00

# 2. tz_convert: Chuyển đổi một Timestamp đã gắn múi giờ sang múi giờ khác
# Mốc thời gian vật lý giữ nguyên, số giờ hiển thị được tính lại theo múi giờ đích
t_utc = t_ha_noi.tz_convert("UTC")
t_london = t_ha_noi.tz_convert("Europe/London")

print("Giờ UTC:", t_utc)        # 2026-03-15 01:00:00+00:00 (lùi 7 tiếng)
print("Giờ London:", t_london)  # 2026-03-15 01:00:00+00:00
```

Lưu ý về điều kiện nguồn và phân biệt hai phương thức:
- Phương thức `tz_localize` chỉ áp dụng cho dữ liệu chưa gắn múi giờ. Nếu gọi `tz_localize` trên một Timestamp đã gắn múi giờ, pandas sẽ ném ngoại lệ `TypeError`.
- Phương thức `tz_convert` chỉ hoạt động trên dữ liệu đã gắn múi giờ. Nếu gọi trên dữ liệu chưa gắn múi giờ, pandas sẽ báo lỗi do không có mốc tham chiếu ban đầu.
- Khi chuyển đổi chuỗi bằng `pd.to_datetime(..., utc=True)`: Nếu chuỗi nguồn là giờ địa phương chưa có thông tin múi giờ (ví dụ `"2026-03-15 08:00:00"`), pandas sẽ coi con số `08:00` đó vốn là giờ UTC rồi gắn nhãn `+00:00`. Nếu sự kiện thực tế phát sinh tại Hà Nội (UTC+7), cách làm này khiến mốc thời gian bị lệch 7 tiếng. Quy trình chính xác là: **Gọi `tz_localize` với múi giờ thực địa trước, sau đó nếu cần lưu trữ thống nhất theo chuẩn quốc tế mới gọi `tz_convert("UTC")`**.

Khi thực hiện phép tính giữa hai Series có múi giờ khác nhau, pandas sẽ tự động quy đổi cả hai về chuẩn UTC trước khi thực hiện phép toán, bảo đảm kết quả thời gian tuyệt đối luôn chính xác.

---

## 3. Chỉ mục thời gian `DatetimeIndex` và kỹ thuật cắt lát chuỗi ký tự

Khi đưa một cột ngày tháng đã chuẩn hóa thành chỉ mục của DataFrame bằng `set_index("date")` và sắp xếp tăng dần bằng `sort_index()`, bảng dữ liệu trở thành một **chuỗi thời gian thực thụ**.

Lợi ích lớn nhất của `DatetimeIndex` là khả năng **cắt lát thông minh bằng chuỗi văn bản (String Slicing)** mà không cần viết các biểu thức logic phức tạp:

```python
# Thiết lập chuỗi thời gian mẫu gồm 1000 ngày
chi_muc = pd.date_range("2024-01-01", periods=1000, freq="D")
gia_tri = np.random.normal(loc=100, scale=15, size=len(chi_muc))
ts = pd.Series(gia_tri, index=chi_muc)

# 1. Cắt lát theo cả năm: Tự động lọc toàn bộ các ngày thuộc năm 2025
nam_2025 = ts.loc["2025"]
print("Số ngày trong năm 2025:", len(nam_2025))

# 2. Cắt lát theo tháng cụ thể
thang_05_2025 = ts.loc["2025-05"]
print("Số ngày trong tháng 5/2025:", len(thang_05_2025))

# 3. Cắt lát theo khoảng thời gian tùy ý (kết quả bao gồm cả hai đầu mút)
khoang_thoi_gian = ts.loc["2025-06-15":"2025-07-15"]
print("Khoảng từ 15/06 đến 15/07:", len(khoang_thoi_gian))
```

Cơ chế này hoạt động đạt hiệu năng cao nhờ thuật toán tìm kiếm nhị phân trên chỉ mục đơn điệu tăng dần (`is_monotonic_increasing`). Nếu chỉ mục chưa được sắp xếp, thao tác cắt lát chuỗi có thể trả về kết quả sai hoặc ném ra cảnh báo nghiêm trọng.

### Xử lý chuỗi thời gian có chỉ mục trùng lặp

Trong nhiều hệ thống (như nhật ký giao dịch ngân hàng hoặc cảm biến IoT), nhiều bản ghi có thể phát sinh tại cùng một thời điểm:

```python
dup_idx = pd.to_datetime(["2026-03-01", "2026-03-01", "2026-03-02"])
dup_ts = pd.Series([10, 20, 30], index=dup_idx)

print("Chỉ mục có đơn nhất không?", dup_ts.index.is_unique) # False
print("Truy vấn ngày 2026-03-01:")
print(dup_ts.loc["2026-03-01"]) # Trả về một Series gồm 2 phần tử

# Gom nhóm theo chỉ mục để hợp nhất các bản ghi trùng lặp
hop_nhat = dup_ts.groupby(level=0).sum()
print("Sau khi gộp theo mốc thời gian:")
print(hop_nhat)
```

---

## 4. Dải ngày, Tần số và Phép dịch chuyển dữ liệu

### Sinh dải ngày bằng `pd.date_range` và mã tần số hiện đại

Hàm `pd.date_range` nhận mốc bắt đầu, mốc kết thúc, số lượng chu kỳ (`periods`) và mã tần số (`freq`). Trong pandas hiện đại, các mã tần số đã được quy chuẩn hóa rõ ràng:

| Mã tần số mới | Ý nghĩa chu kỳ |
| :--- | :--- |
| **`"D"`** | Theo ngày theo lịch (Calendar day) |
| **`"B"`** | Theo ngày làm việc (Business day, thứ Hai đến thứ Sáu) |
| **`"W"`** hoặc `"W-MON"` | Theo tuần (mặc định Chủ nhật hoặc neo vào thứ Hai) |
| **`"ME"`** | Cuối tháng (Month End) |
| **`"MS"`** | Đầu tháng (Month Start) |
| **`"QE"`** | Cuối quý (Quarter End) |
| **`"QS"`** | Đầu quý (Quarter Start) |
| **`"YE"`** | Cuối năm (Year End) |

Bên cạnh các tần số cơ bản, pandas cung cấp các lớp **Date Offsets** linh hoạt trong module `pandas.tseries.offsets`:

```python
from pandas.tseries.offsets import Day, MonthEnd, WeekOfMonth

moc = pd.Timestamp("2026-03-15")

# Dịch chuyển đến ngày cuối cùng của tháng hiện tại
cuoi_thang = moc + MonthEnd()
print("Cuối tháng 3:", cuoi_thang) # 2026-03-31

# Tần số tuần trong tháng (Week of Month), ví dụ: Ngày thứ Sáu tuần thứ 3 mỗi tháng
thu_sau_tuan_3 = pd.date_range("2026-01-01", periods=3, freq="WOM-3FRI")
print("Thứ Sáu tuần thứ 3 các tháng đầu năm 2026:")
for d in thu_sau_tuan_3:
    print(d.strftime("%Y-%m-%d"))
```

### Dịch chuỗi và Cạm bẫy thiếu tháng

Phương thức `shift()` cho phép dịch chuyển dữ liệu tiến hoặc lùi dọc theo chuỗi:
- `shift(1)`: Dịch dữ liệu lùi 1 vị trí (dòng hiện tại nhận giá trị của dòng trước đó).
- `shift(-1)`: Dịch dữ liệu tiến 1 vị trí (dòng hiện tại nhận giá trị của tương lai).

Một sai lầm rất nguy hiểm là việc ngộ nhận rằng `shift(1)` luôn lấy đúng giá trị của tháng trước:

```python
# Giả sử tập dữ liệu bị khuyết toàn bộ tháng 2 năm 2026
chuoi_thieu = pd.Series([100, 150, 180], index=pd.to_datetime(["2026-01-31", "2026-03-31", "2026-04-30"]))

# Dịch chuyển theo số hàng thuần túy
dich_hang = chuoi_thieu.shift(1)
print("Dịch theo hàng:")
print(pd.DataFrame({"Gia_tri": chuoi_thieu, "Shift_1": dich_hang}))
```

Tại dòng tháng 3 (`2026-03-31`), cột `Shift_1` nhận 100 của tháng 1 vì `shift(1)` lùi một hàng trong bảng đang có. Nếu muốn so với tháng liền trước theo lịch, có thể đưa chuỗi về lịch tháng đầy đủ bằng `asfreq("ME")` rồi dịch một hàng:

```python
chuoi_chuan_lich = chuoi_thieu.asfreq("ME")
print("Sau khi chèn mốc lịch chuẩn xác:")
print(pd.DataFrame({
    "Gia_tri": chuoi_chuan_lich,
    "Shift_lich": chuoi_chuan_lich.shift(1)
}))
```

Giờ đây, tháng 3 nhận giá trị `NaN` vì tháng 2 liền trước thực sự không có số liệu, bảo đảm tính trung thực của các phân tích tăng trưởng.

Ngoài ra, ta có thể dịch chuyển chính trục thời gian (giữ nguyên giá trị) bằng cách truyền thêm tham số `freq`:
`ts.shift(2, freq="ME")` sẽ tịnh tiến toàn bộ các nhãn thời gian thêm 2 tháng.

---

## 5. Kỳ (Period) và số học trên kỳ

Đối tượng `pd.Period` đại diện cho một khoảng thời gian hữu hạn (kỳ lịch) thay vì một thời điểm đơn lẻ.

### Chuyển đổi tần số kỳ

Một kỳ năm có thể được phân rã thành các kỳ nhỏ hơn (tháng hoặc ngày làm việc), với tùy chọn neo vào đầu kỳ (`how="start"`) hoặc cuối kỳ (`how="end"`):

```python
p_nam = pd.Period("2026", freq="Y")

# Chuyển đổi sang ngày làm việc đầu tiên và cuối cùng của năm
p_ngay_dau = p_nam.asfreq("B", how="start")
p_ngay_cuoi = p_nam.asfreq("B", how="end")

print("Ngày làm việc đầu năm 2026:", p_ngay_dau)   # 2026-01-01
print("Ngày làm việc cuối năm 2026:", p_ngay_cuoi) # 2026-12-31
```

### Kỳ quý tài chính

Trong kế toán doanh nghiệp, năm tài chính thường không trùng với năm dương lịch (ví dụ kết thúc vào tháng 11: `Q-NOV`):

```python
p_quy = pd.Period("2026Q1", freq="Q-NOV")
print("Quý 1 tài chính bắt đầu từ:", p_quy.start_time, "đến:", p_quy.end_time)
```

### Chuyển đổi giữa Timestamp và Period

Chuyển từ mốc thời gian sang kỳ bằng `to_period()`, và chuyển ngược lại điểm thời gian bằng `to_timestamp()`:

```python
ngay_ts = pd.date_range("2026-01-15", periods=3, freq="MS")
chu_ky = ngay_ts.to_period("M")
print("Chuyển sang Period:", chu_ky)

ve_timestamp = chu_ky.to_timestamp(how="end")
print("Chuyển ngược về Timestamp cuối kỳ:", ve_timestamp)
```

Ta cũng có thể tạo trực tiếp một `PeriodIndex` từ hai mảng số nguyên biểu diễn năm và quý:

```python
nam = [2025, 2025, 2026, 2026]
quy = [3, 4, 1, 2]
p_idx = pd.PeriodIndex.from_fields(year=nam, quarter=quy, freq="Q")
print("PeriodIndex từ mảng năm và quý:", p_idx)
```

---

## 6. Lấy mẫu lại (Resampling): Tần số, Biên đóng mở và Bẫy kỳ dang dở

Lấy mẫu lại (`resample`) là quá trình chuyển đổi tần số của một chuỗi thời gian, đóng vai trò như phép toán `groupby` chuyên biệt trên trục thời gian.

### Lấy mẫu giảm tần số (Downsampling) và quy tắc biên `closed`, `label`

Downsampling là việc gộp dữ liệu từ tần số cao xuống tần số thấp hơn (ví dụ từ phút sang giờ, từ ngày sang tháng). Khi gộp các khoảng thời gian, hai tham số quyết định ranh giới tính toán:
- `closed`: Xác định biên nào của khoảng thời gian được tính vào kỳ. Mặc định đối với các tần số cuối kỳ như `"ME"`, `"QE"` là `closed="right"` (nhận cận phải).
- `label`: Xác định nhãn hiển thị của kỳ gộp. Mặc định là `label="right"` (lấy mốc thời gian của cận phải làm đại diện).

```python
ngay_gd = pd.to_datetime(["2026-01-05", "2026-01-20", "2026-02-14", "2026-03-01", "2026-03-25"])
df_gd = pd.DataFrame({"tien": [100, 200, 150, 300, 250]}, index=ngay_gd)

# Lấy mẫu theo tháng kết thúc (Month End)
thang_gd = df_gd.resample("ME").agg(tong_tien=("tien", "sum"), so_gd=("tien", "count"))
print(thang_gd)
```

### Lấy mẫu OHLC trong phân tích tài chính

Trong giao dịch tài chính và cảm biến kỹ thuật, người ta thường quan tâm đến 4 giá trị đặc trưng trong từng khung thời gian: Giá mở cửa (Open), giá cao nhất (High), giá thấp nhất (Low), và giá đóng cửa (Close):

```python
rng_phut = pd.date_range("2026-01-01", periods=10, freq="1min")
ts_gia = pd.Series([10, 12, 9, 15, 14, 13, 18, 11, 16, 20], index=rng_phut)

bang_ohlc = ts_gia.resample("5min").ohlc()
print("Bảng tóm tắt OHLC 5 phút:")
print(bang_ohlc)
```

### Lấy mẫu tăng tần số (Upsampling) và các phương pháp nội suy

Upsampling là việc chuyển từ tần số thấp lên tần số cao hơn (ví dụ từ tháng sang ngày). Thao tác này làm phát sinh các mốc thời gian chưa có giá trị quan sát:

```python
chuoi_thap = pd.Series([10.0, 20.0], index=pd.to_datetime(["2026-01-01", "2026-01-03"]))

# 1. Để trống bằng asfreq
up_trong = chuoi_thap.resample("D").asfreq()

# 2. Điền tiến (Forward Fill)
up_ffill = up_trong.ffill()

# 3. Nội suy tuyến tính (Linear Interpolation)
up_interp = up_trong.interpolate(method="linear")

print(pd.DataFrame({
    "Goc": up_trong,
    "Forward_Fill": up_ffill,
    "Noi_suy": up_interp
}))
```

### Lấy mẫu thời gian theo nhóm (Grouped Time Resampling)

Khi bảng dữ liệu có nhiều thực thể (ví dụ nhiều cửa hàng hoặc chi nhánh), ta kết hợp `groupby` với `pd.Grouper`:

```python
df_ban_hang = pd.DataFrame({
    "ngay": pd.to_datetime(["2026-01-05", "2026-01-20", "2026-02-10", "2026-01-15", "2026-02-25"]),
    "chi_nhanh": ["HN", "HN", "HN", "SG", "SG"],
    "doanh_thu": [100, 150, 200, 300, 400]
})

doanh_thu_thang_nhom = df_ban_hang.groupby(
    ["chi_nhanh", pd.Grouper(key="ngay", freq="ME")]
)["doanh_thu"].sum()
print("Doanh thu theo chi nhánh và tháng:")
print(doanh_thu_thang_nhom)
```

### Lưu ý khi xử lý kỳ chưa trọn vẹn (Incomplete Period)

Giả sử bạn trích xuất dữ liệu của một hệ thống vào ngày **29 tháng 6 năm 2026**.
Khi gọi `resample("QE").sum()`, pandas sẽ gom toàn bộ các ngày từ tháng 4 đến hết ngày 29/6 vào Quý 2 năm 2026 và gán nhãn là ngày kết thúc quý: `2026-06-30`.

Tuy nhiên, Quý 2 thực tế có 91 ngày, trong khi dữ liệu mới chỉ ghi nhận đến ngày 29 (thiếu ngày 30). Khi đem so sánh tổng doanh thu hoặc số lượng đánh giá của Quý 2 với Quý 1 (vốn đã trọn vẹn 90 ngày), con số của Quý 2 trông như bị sụt giảm. Nếu người phân tích đưa con số này vào biểu đồ so sánh tổng mà không chú thích, người đọc sẽ nhận định sai lầm rằng hoạt động kinh doanh suy thoái.

**Quy tắc thẩm định**: Khi mốc chụp dữ liệu nằm trước ngày kết thúc của kỳ tổng hợp, kỳ đó là **kỳ chưa trọn vẹn**. Ta cần loại bỏ kỳ này khỏi các phân tích so sánh tổng sản lượng, hoặc phải chuẩn hóa thành chỉ số trung bình theo ngày.

---

## 7. Cửa sổ trượt, Làm mượt hàm mũ và So sánh cùng kỳ

### Cửa sổ trượt (Rolling Windows)

Phương pháp cửa sổ trượt tính giá trị trung bình trên một khoảng thời gian di động dọc theo chuỗi dữ liệu:
$$
\bar{Y}_t = \frac{1}{W} \sum_{i=0}^{W-1} Y_{t-i}
$$

Trong thực tế, cửa sổ 7 ngày (`rolling(7)` hoặc `rolling("7D")`) thường được ưu tiên vì nó bao trọn một chu kỳ tuần (từ thứ Hai đến Chủ nhật), triệt tiêu dao động ngày trong tuần.

- `center=False` (mặc định): Giá trị tại thời điểm $t$ chỉ dùng dữ liệu của $t$ và quá khứ. Đây là lựa chọn bắt buộc cho bài toán dự báo nhằm tránh rò rỉ thông tin tương lai.
- `center=True`: Giá trị tại $t$ là trung bình của quá khứ, hiện tại và tương lai. Phương pháp này loại bỏ độ trễ pha (phase lag), hỗ trợ định vị chính xác thời điểm đạt đỉnh trong các báo cáo hồi cứu.

### Làm mượt theo hàm mũ (Exponentially Weighted Moving)

Phương pháp cửa sổ trượt gán trọng số đồng đều cho mọi ngày trong cửa sổ. Trái lại, phương pháp **làm mượt hàm mũ (EWM)** gán trọng số giảm dần theo cấp số nhân khi càng lùi xa về quá khứ:

```python
s_gia = pd.Series([10.0, 12.0, 15.0, 14.0, 16.0])

# Tính trung bình trượt hàm mũ với span = 3
ewm_tb = s_gia.ewm(span=3).mean()
print("EWM làm mượt:")
print(pd.DataFrame({"Goc": s_gia, "EWM": ewm_tb}))
```

### Cửa sổ trượt trên hai chuỗi (Binary Moving Windows)

Thuật ngữ "binary" ở đây chỉ phép toán hai ngôi thực hiện trên hai chuỗi dữ liệu (two series), hoàn toàn không mang nghĩa dữ liệu nhận giá trị nhị phân 0 hoặc 1.

Các phương thức như `s1.rolling(w).corr(s2)` hoặc `s1.rolling(w).cov(s2)` yêu cầu hai chuỗi `s1` và `s2` có cùng chỉ mục thời gian, tính toán hệ số tương quan hoặc hiệp phương sai trượt trên từng khung cửa sổ kích thước $w$:

```python
ngay_gd = pd.date_range("2026-01-01", periods=10, freq="D")
s1 = pd.Series([10, 12, 11, 14, 16, 15, 18, 19, 21, 22], index=ngay_gd)
s2 = pd.Series([100, 105, 102, 110, 115, 112, 120, 122, 130, 132], index=ngay_gd)

# Tính tương quan trượt trên cửa sổ 5 ngày
tuong_quan_truot = s1.rolling(5).corr(s2)
print("Tương quan trượt 5 ngày:")
print(tuong_quan_truot.dropna())
```

### So kỳ liền trước (MoM) so với So cùng kỳ năm trước (YoY)

Công thức tính tỷ lệ tăng trưởng phần trăm:
$$
g = \left( \frac{Y_t}{Y_{t-k}} - 1 \right) \times 100\%
$$

- **MoM (Month-over-Month)**: Dùng `pct_change(1)` để đo xung lực biến động ngắn hạn giữa hai tháng liền kề.
- **YoY (Year-over-Year)**: Dùng `pct_change(12)` để đối chiếu các vị trí mùa tương ứng giữa hai năm liên tiếp (ví dụ so tháng 3 năm nay với tháng 3 năm trước). Phép so sánh này giúp loại bỏ ảnh hưởng của mô hình mùa cố định hàng năm, nhưng không tự bảo đảm triệt tiêu toàn bộ yếu tố mùa vụ nếu biên độ mùa vụ thay đổi theo chu kỳ kinh tế hoặc có sự chênh lệch về số ngày làm việc trong tháng.

```python
doanh_thu_thang = pd.Series(
    [100, 110, 105, 120, 130, 125, 140, 150, 145, 160, 170, 200,
     120, 125, 118, 135, 145, 140, 155, 170, 160, 180, 190, 230],
    index=pd.date_range("2024-01-31", periods=24, freq="ME")
)

tang_truong_mom = doanh_thu_thang.pct_change(periods=1) * 100
tang_truong_yoy = doanh_thu_thang.pct_change(periods=12) * 100

bao_cao = pd.DataFrame({
    "Doanh_thu": doanh_thu_thang,
    "Tang_truong_MoM(%)": tang_truong_mom,
    "Tang_truong_YoY(%)": tang_truong_yoy
})
print(bao_cao.tail(5))
```

---

## 9. Tổng kết

| Khái niệm kỹ thuật | Công cụ trong pandas | Lưu ý thực hành và Ranh giới |
| :--- | :--- | :--- |
| **`DatetimeIndex`** | `set_index()`, `sort_index()` | Sắp xếp tăng dần để tối ưu tìm kiếm nhị phân và cho phép cắt lát chuỗi ký tự tự nhiên. |
| **Múi giờ** | `tz_localize()`, `tz_convert()` | `tz_localize` gán ngữ cảnh cho dữ liệu chưa gắn múi giờ, còn `tz_convert` đổi tọa độ giờ cho dữ liệu đã gắn múi giờ. |
| **Dịch chuỗi** | `shift(1)`, `asfreq("ME")` | Dịch theo hàng không đồng nghĩa với dịch theo lịch, do đó cần đưa về lưới thời gian đều trước khi dịch. |
| **Kỳ `Period`** | `pd.Period`, `PeriodIndex` | Đại diện cho khoảng thời gian hữu hạn, chuyển đổi qua lại với `Timestamp` bằng `to_period()` và `to_timestamp()`. |
| **Lấy mẫu lại** | `resample("ME")`, `ohlc()` | Lấy mẫu giảm tần số cần chú ý kỳ chưa trọn vẹn, còn lấy mẫu tăng tần số cần chọn phép nội suy thích hợp. |
| **Cửa sổ trượt** | `rolling()`, `ewm()` | Dùng `center=False` để phòng chống rò rỉ tương lai, và dùng `ewm` khi muốn ưu tiên quan sát gần nhất. Cửa sổ trên hai chuỗi áp dụng cho cặp chuỗi cùng chỉ mục. |
| **So cùng kỳ (YoY)** | `pct_change(12)` | Đối chiếu các vị trí mùa tương ứng giữa hai năm, hỗ trợ nhận định tốc độ tăng trưởng dài hạn. |

## Tài liệu tham khảo

1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Chapter 11: Time Series. URL: [https://wesmckinney.com/book/time-series](https://wesmckinney.com/book/time-series).
2. Tài liệu chính thức pandas: *Time Series / Date Functionality*. URL: [https://pandas.pydata.org/docs/user_guide/timeseries.html](https://pandas.pydata.org/docs/user_guide/timeseries.html).
3. Cơ sở dữ liệu múi giờ quốc tế IANA: *Time Zone Database*. URL: [https://www.iana.org/time-zones](https://www.iana.org/time-zones).
4. Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN: *Giáo trình Lập trình xử lý dữ liệu (Bài 8: Xử lý dữ liệu thời gian)*. Các bài tập thực hành được chuyển thể theo giấy phép [CC BY-NC-SA 4.0](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 8. Bài tập thực hành

<span id="iai-08-bai-1"></span>

::: exercise Bài tập 1: Tính số đêm lưu trú và bẫy định dạng
Mỗi hàng trong bảng sau là một lượt đặt chỗ lưu trú, với ngày đến và ngày đi được ghi dưới dạng chuỗi theo quy ước `DD/MM/YYYY`:

```python
dat = pd.DataFrame({
    "vao": ["03/07/2026", "10/07/2026"],
    "ra": ["06/07/2026", "12/07/2026"],
})
```

Hãy viết đoạn mã tính số đêm lưu trú thực tế của từng lượt khách. Giải thích điều gì xảy ra nếu lập trình viên không cung cấp tham số `format` tường minh cho `pd.to_datetime`.
:::

::: solution Lời giải chi tiết
Nếu không truyền `format="%d/%m/%Y"`, pandas mặc định phỏng đoán theo chuẩn quốc tế hoặc quy ước Mỹ (`MM/DD/YYYY`). Chuỗi `"03/07/2026"` sẽ bị hiểu thành ngày 7 tháng 3 năm 2026 thay vì ngày 3 tháng 7. Do đó, khoảng thời gian sẽ bị kéo dài thành 92 đêm và 61 đêm một cách phi lý.

Mã nguồn chuẩn xác:

```python
vao = pd.to_datetime(dat["vao"], format="%d/%m/%Y")
ra = pd.to_datetime(dat["ra"], format="%d/%m/%Y")
so_dem = (ra - vao).dt.days

print("Số đêm thực tế:", so_dem.tolist())
# Kết quả chính xác: [3, 2]
```
:::

<span id="iai-08-bai-2"></span>

::: exercise Bài tập 2: Tính trung bình số đánh giá mỗi ngày trong tuần
Hệ thống thu thập dữ liệu ghi nhận số lượt đánh giá trong tuần từ ngày 01/06/2026 đến ngày 07/06/2026. Tuy nhiên, bảng dữ liệu chỉ ghi nhận những ngày thực tế có khách viết đánh giá:

```python
df_danh_gia = pd.DataFrame({
    "ngay": pd.to_datetime(["2026-06-01", "2026-06-03", "2026-06-07"]),
    "so_luong": [2, 1, 4]
}).set_index("ngay")
```

Giả thiết rằng trong tuần này hệ thống hoạt động liên tục và việc thu thập dữ liệu diễn ra đầy đủ, các ngày không xuất hiện trong bảng là những ngày thực tế không phát sinh lượt đánh giá nào (số lượng bằng 0). Hãy tính số lượt đánh giá trung bình mỗi ngày trong toàn bộ tuần khảo sát gồm 7 ngày này.
:::

::: solution Lời giải chi tiết
Nếu gọi trực tiếp `df_danh_gia["so_luong"].mean()`, kết quả sẽ là $(2 + 1 + 4) / 3 = 7 / 3 \approx 2{,}33$ đánh giá/ngày. Con số này chỉ tính bình quân trên các ngày có phát sinh đánh giá, bỏ qua 4 ngày không có lượt đánh giá nào.

Khi giả thiết thu thập dữ liệu đầy đủ được bảo đảm từ nguồn, ta khôi phục lại đủ 7 ngày của tuần bằng `resample("D")`, điền giá trị 0 cho các ngày không có giao dịch, rồi mới tính trung bình:

```python
chuoi_ngay_du = df_danh_gia.resample("D").sum().fillna(0)
tb_moi_ngay = chuoi_ngay_du["so_luong"].mean()

print("Số đánh giá trung bình mỗi ngày:", tb_moi_ngay)
# Kết quả: 7 / 7 = 1.0 đánh giá/ngày
```
:::

<span id="iai-08-bai-3"></span>

::: exercise Bài tập 3: Nhận diện tháng tăng trưởng đột biến
Cho chuỗi số lượt đánh giá theo từng tháng trong năm 2025:

```python
thang_dem = pd.Series(
    [90, 120, 90, 150, 120, 240],
    index=pd.date_range("2025-01-31", periods=6, freq="ME")
)
```

Hãy viết mã nguồn tìm tất cả các tháng có số đánh giá cao hơn ít nhất 50% so với trung bình của 3 tháng liền trước đó. Lưu ý: Chỉ xét các tháng đã có đủ 3 tháng liền trước để làm mốc đối chiếu.
:::

::: solution Lời giải chi tiết
Để so sánh tháng hiện tại với trung bình 3 tháng trước, ta cần:
1. Tính trung bình trượt 3 tháng bằng `rolling(3, min_periods=3).mean()`.
2. Dịch chuyển mốc tính toán lùi 1 vị trí bằng `shift(1)` để giá trị tại hàng hiện tại là trung bình của 3 tháng trước đó, không bao gồm chính tháng hiện tại.
3. Lọc các tháng thỏa mãn điều kiện $Y_t \ge 1{,}5 \times \text{tb\_3\_truoc}$.

```python
tb_3_truoc = thang_dem.rolling(3, min_periods=3).mean().shift(1)
thang_tang_manh = thang_dem[thang_dem >= 1.5 * tb_3_truoc]

print("Các tháng tăng mạnh (>= 50% so với 3 tháng trước):")
for idx, val in thang_tang_manh.items():
    print(f"Tháng {idx.month}: {val} đánh giá (mốc so sánh: {tb_3_truoc.loc[idx]:.1f})")

# Tháng 4: 150 >= 1.5 * (90 + 120 + 90)/3 = 1.5 * 100 = 150 (Đạt)
# Tháng 5: 120 < 1.5 * (120 + 90 + 150)/3 = 1.5 * 120 = 180 (Không đạt)
# Tháng 6: 240 >= 1.5 * (90 + 150 + 120)/3 = 1.5 * 120 = 180 (Đạt)
# Kết quả lọc: Tháng 4 và Tháng 6
```
:::

---





<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-08">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-08.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Chapter 11: Time Series. URL: [https://wesmckinney.com/book/time-series](https://wesmckinney.com/book/time-series).
2. Tài liệu chính thức pandas: *Time Series / Date Functionality*. URL: [https://pandas.pydata.org/docs/user_guide/timeseries.html](https://pandas.pydata.org/docs/user_guide/timeseries.html).
3. Cơ sở dữ liệu múi giờ quốc tế IANA: *Time Zone Database*. URL: [https://www.iana.org/time-zones](https://www.iana.org/time-zones).
4. Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN: *Giáo trình Lập trình xử lý dữ liệu (Bài 8: Xử lý dữ liệu thời gian)*. Các bài tập thực hành được chuyển thể theo giấy phép [CC BY-NC-SA 4.0](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
