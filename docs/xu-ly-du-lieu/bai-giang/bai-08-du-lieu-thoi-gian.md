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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-1 -->

::: example Xử lý mốc thời gian không tồn tại khi chuyển sang giờ mùa hè với nonexistent

Nhật ký sau được ghi bằng giờ địa phương New York, chưa gắn múi giờ. Ngày 08/03/2026, đồng hồ chuyển từ 01:59:59 sang 03:00:00 nên nhãn 02:30 không có thời điểm tương ứng. Ta chọn một cách xử lý nhãn đó rồi đổi các thời điểm hợp lệ sang UTC.

```python
import pandas as pd

# Giờ New York nhảy qua 02:00 sáng ngày 08/03/2026 khi đổi sang giờ mùa hè
chuoi_thoi_gian = pd.Series([
    "2026-03-08 01:30:00",
    "2026-03-08 02:30:00",
    "2026-03-08 03:30:00",
])
dt_chua_mui = pd.to_datetime(chuoi_thoi_gian)

# nonexistent="shift_forward" đưa mốc không tồn tại sang mốc hợp lệ kế tiếp
dt_da_gan = dt_chua_mui.dt.tz_localize(
    "America/New_York", nonexistent="shift_forward"
)
dt_utc = dt_da_gan.dt.tz_convert("UTC")

ket_qua = pd.DataFrame({
    "goc": chuoi_thoi_gian,
    "ny_tz": dt_da_gan.dt.strftime("%Y-%m-%d %H:%M %Z"),
    "utc": dt_utc.dt.strftime("%Y-%m-%d %H:%M %Z"),
})
print(ket_qua)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| goc | ny&#95;tz | utc |
| --- | --- | --- |
| 2026-03-08 01:30:00 | 2026-03-08 01:30 EST | 2026-03-08 06:30 UTC |
| 2026-03-08 02:30:00 | 2026-03-08 03:00 EDT | 2026-03-08 07:00 UTC |
| 2026-03-08 03:30:00 | 2026-03-08 03:30 EDT | 2026-03-08 07:30 UTC |

</div>

`pd.to_datetime` đọc các chuỗi thành thời gian chưa gắn múi giờ. `tz_localize("America/New_York")` gắn quy tắc của New York vào nhãn giờ. Nếu giữ mặc định, nhãn 02:30 không tồn tại trong ngày chuyển giờ sẽ gây lỗi. Tham số `nonexistent="shift_forward"` đưa nó tới mốc hợp lệ đầu tiên là 03:00 EDT, không phải cộng một giờ để thành 03:30.

`tz_convert("UTC")` đổi cách biểu diễn nhưng giữ cùng thời điểm. Kết quả lần lượt là 06:30, 07:00 và 07:30 UTC. Hai nhãn đầu và cuối được giữ nguyên giờ địa phương khi gắn múi giờ, còn nhãn giữa đã được điều chỉnh theo lựa chọn `nonexistent`.

Dùng ngay `pd.to_datetime(..., utc=True)` trên các chuỗi chưa có múi giờ sẽ coi chúng vốn là giờ UTC. Với dữ liệu địa phương này, cách đó đọc sai thời điểm. Nếu không có căn cứ để dịch nhãn 02:30, có thể chọn `nonexistent="NaT"` để giữ lại tình trạng chưa xác định thay vì tạo một thời điểm thay thế.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-2 -->

::: example Lọc khung giờ cố định trong ngày bằng between_time và at_time

Trong các hệ thống phân tích phiên giao dịch chứng khoán hoặc lưu lượng mạng viễn thông, người phân tích cần trích xuất các bản ghi diễn ra trong đúng khung giờ hành chính mỗi ngày, ví dụ từ 09:00 đến 11:00. Thay vì phải tách trường giờ và trường phút ra các cột phụ rồi ghép điều kiện lọc, DatetimeIndex cung cấp phương thức between_time để lọc trực tiếp trên toàn bộ các ngày quan sát.

```python
import pandas as pd

# Giả lập chuỗi ghi nhận giao dịch mỗi 30 phút trong hai ngày làm việc
idx = pd.date_range("2026-03-02 08:30", "2026-03-03 12:30", freq="30min")
ts = pd.Series(range(100, 100 + len(idx)), index=idx, name="lenh")

# Lọc các giao dịch trong khung giờ khớp lệnh liên tục từ 09:00 đến 11:00
khung_sang = ts.between_time("09:00", "11:00", inclusive="both")
bang_kq = pd.DataFrame({
    "thoi_diem": khung_sang.index.strftime("%Y-%m-%d %H:%M"),
    "so_lenh": khung_sang.values,
})
print(bang_kq)
print("Chỉ các mốc đúng 11 giờ:")
print(ts.at_time("11:00"))
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| thoi&#95;diem | so&#95;lenh |
| --- | --- |
| 2026-03-02 09:00 | 101 |
| 2026-03-02 09:30 | 102 |
| 2026-03-02 10:00 | 103 |
| 2026-03-02 10:30 | 104 |
| 2026-03-02 11:00 | 105 |
| 2026-03-03 09:00 | 149 |
| 2026-03-03 09:30 | 150 |
| 2026-03-03 10:00 | 151 |
| 2026-03-03 10:30 | 152 |
| 2026-03-03 11:00 | 153 |

</div>

```text
Chỉ các mốc đúng 11 giờ:
```

<div class="data-worked-table">

| Chỉ mục | lenh |
| --- | --- |
| 2026-03-02 11:00:00 | 105 |
| 2026-03-03 11:00:00 | 153 |

</div>

`between_time("09:00", "11:00", inclusive="both")` lọc phần giờ trong `DatetimeIndex` cho mọi ngày. Hai biên đều được giữ. Vì vậy, kết quả có các mốc 09:00, 09:30, 10:00, 10:30 và 11:00 ở cả hai ngày. Đây khác với lát cắt có ghi ngày cụ thể, vốn chỉ lấy khoảng của ngày đó.

`at_time("11:00")` chỉ lấy những bản ghi đúng 11 giờ, gồm một bản ghi mỗi ngày trong dữ liệu mẫu. Nó không chọn giá trị gần 11 giờ nhất. Cả hai phương thức cần chỉ mục thời gian, nên cần chuyển cột thời gian và đặt làm chỉ mục trước nếu bảng vẫn dùng chỉ mục số.

Nếu giờ bắt đầu lớn hơn giờ kết thúc, như 22:00 đến 04:00, `between_time` chọn các giờ nằm ngoài khoảng ban ngày. Kết quả vẫn giữ nhãn ngày gốc của từng bản ghi, không tự gán ngày 04:00 về cùng một ca với 22:00 hôm trước. Muốn thống kê theo ca cần thêm quy tắc xác định ca.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-3 -->

::: example Phát hiện và hợp nhất các mốc thời gian trùng lặp theo phương pháp chọn lọc

Trong các hệ thống nhật ký cảm biến hoặc máy chủ phân tán, nhiều bản ghi có thể phát sinh tại cùng một mốc giây do đo đạc song song. Chỉ mục chứa khóa trùng lặp khiến các thao tác truy vấn trả về cấu trúc không đồng nhất và làm sai lệch các phép lấy mẫu lại. Ta cần kiểm tra tính đơn nhất và gom nhóm chỉ mục để thu gọn dữ liệu về trạng thái sạch.

```python
import pandas as pd

idx = pd.to_datetime([
    "2026-03-01 10:00:00",
    "2026-03-01 10:00:00",
    "2026-03-01 10:00:01",
    "2026-03-01 10:00:02",
])
s = pd.Series([25.4, 25.6, 26.0, 25.9], index=idx, name="nhiet_do")

# Hợp nhất bằng cách lấy giá trị trung bình tại mốc trùng lặp
s_tb = s.groupby(level=0).mean()
s_dem = s.groupby(level=0).count()

bang_kq = pd.DataFrame({
    "thoi_diem": s_tb.index.strftime("%H:%M:%S"),
    "so_mau": s_dem.values,
    "nhiet_do": s_tb.round(2).values,
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| thoi&#95;diem | so&#95;mau | nhiet&#95;do |
| --- | --- | --- |
| 10:00:00 | 2 | 25.5 |
| 10:00:01 | 1 | 26.0 |
| 10:00:02 | 1 | 25.9 |

</div>

Khi làm việc với chuỗi thời gian trong pandas, giả định thuận lợi nhất là mỗi mốc thời gian chỉ xuất hiện đúng một lần, tức thuộc tính s.index.is_unique trả về True. Tuy nhiên, khi gộp dữ liệu từ nhiều nguồn đo độc lập, tình trạng trùng lặp chỉ mục có thể xảy ra. Nếu chỉ mục bị trùng, thao tác truy vấn s.loc['2026-03-01 10:00:00'] sẽ không trả về một giá trị vô hướng đơn lẻ mà trả về một Series gồm nhiều phần tử, làm gián đoạn các phép tính tiếp theo vốn kỳ vọng một số đơn.

`s.groupby(level=0)` gom các quan sát có cùng nhãn thời gian. `.mean()` tính nhiệt độ trung bình, còn `.count()` đếm các giá trị không thiếu. Nếu muốn đếm cả bản ghi có giá trị thiếu, dùng `.size()`. Chọn tổng, trung bình hay một quan sát đại diện tùy ý nghĩa đại lượng, không chỉ để chỉ mục hết trùng.

Hai nhiệt độ 25.4 và 25.6 lúc 10:00:00 cho trung bình 25.5 với số mẫu bằng 2. Hai mốc sau có một mẫu mỗi mốc. Chỉ mục đầu ra có đúng một nhãn mỗi nhóm. Thao tác này thay đổi đơn vị quan sát từ từng mẫu đo sang từng thời điểm.

Một hướng tiếp cận dễ nhầm lẫn là gọi phương thức drop_duplicates() trên Series mà không kiểm tra chỉ mục. Phương thức drop_duplicates() theo mặc định chỉ kiểm tra sự trùng lặp trên các giá trị dữ liệu chứ không kiểm tra sự trùng lặp trên nhãn chỉ mục thời gian. Nếu hai thời điểm khác nhau tình cờ ghi nhận cùng một nhiệt độ, drop_duplicates() sẽ loại bỏ một mốc thời gian hợp lệ mà không giải quyết được sự cố trùng khóa thời gian ban đầu.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-4 -->

::: example Chuẩn hóa thời điểm về đầu ngày với tham số normalize

Một mốc bắt đầu mang theo giờ 14:25. Ta cần tạo ba ngày liên tiếp để ghép với một bảng thống kê theo ngày ở lúc 00:00. Tham số `normalize` cho thấy phần giờ được giữ lại hoặc đưa về đầu ngày như thế nào.

```python
import pandas as pd

# Mốc bắt đầu phát sinh lúc 14:25 chiều
bat_dau = pd.Timestamp("2026-03-01 14:25:00")

# Sinh dải ngày giữ nguyên giờ lẻ so với sinh dải ngày đã chuẩn hóa
dr_le = pd.date_range(bat_dau, periods=3, freq="D")
dr_chuan = pd.date_range(bat_dau, periods=3, freq="D", normalize=True)

bang_kq = pd.DataFrame({
    "giu_gio": dr_le.strftime("%Y-%m-%d %H:%M"),
    "chuan_hoa": dr_chuan.strftime("%Y-%m-%d %H:%M"),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| giu&#95;gio | chuan&#95;hoa |
| --- | --- |
| 2026-03-01 14:25 | 2026-03-01 00:00 |
| 2026-03-02 14:25 | 2026-03-02 00:00 |
| 2026-03-03 14:25 | 2026-03-03 00:00 |

</div>

Hàm pd.date_range là công cụ tạo trục thời gian phổ biến trong pandas, nhận mốc bắt đầu, mốc kết thúc, tần số hoặc số lượng chu kỳ. Một trường hợp thường gặp trong thực tế là mốc bắt đầu được lấy trực tiếp từ thời gian hiện tại của hệ thống hoặc từ một dòng nhật ký cụ thể, mang theo thành phần giờ và phút lẻ như 14:25:00. Khi truyền mốc này vào pd.date_range với tần số freq='D', dải thời gian sinh ra sẽ giữ nguyên thành phần giờ lẻ 14:25:00 qua tất cả các ngày tiếp theo.

Cần lưu ý rằng tần số freq='D' thể hiện bước nhảy một ngày theo lịch, và không phải lúc nào cũng tương đương đúng 24 giờ trôi qua trên thang đo thời gian thực: Khi đi qua ngày chuyển đổi giờ mùa hè (Daylight Saving Time), một ngày theo lịch có thể chỉ kéo dài 23 giờ vào mùa xuân hoặc kéo dài 25 giờ vào mùa thu. Do đó, việc hiểu bước nhảy lịch là rất quan trọng khi phân tích dữ liệu đa múi giờ.

Nếu giữ lại giờ lẻ, khi thực hiện phép nối bảng dữ liệu theo chỉ mục với một bảng khác vốn có chỉ mục ngày được sinh từ mốc nửa đêm '2026-03-01 00:00:00', các dòng mang nhãn 14:25:00 sẽ không khớp được với nhãn 00:00:00. Phép nối sẽ không thể ghép cặp các dòng này và tạo ra giá trị NaN ở những vị trí lệch nhãn, dù các dòng khác nếu trùng khớp thì vẫn được kết nối bình thường.

Tham số normalize=True trong pd.date_range giải quyết sự lệch nhãn này bằng cách đưa phần giờ, phút, giây về đúng 00:00:00 trước khi áp dụng quy tắc tần số. Bảng kết quả so sánh làm rõ sự khác biệt: Dãy thứ nhất duy trì mốc 14:25, trong khi dãy thứ hai được chuẩn hóa thành chuỗi ngày bắt đầu từ nửa đêm. Tuy nhiên, cần nhớ rằng normalize chỉ làm sạch thành phần giờ trong ngày, chứ không thể tự động xử lý hay triệt tiêu sự bất đồng về múi giờ nếu hai bảng dữ liệu thuộc hai múi giờ khác nhau.

:::

<!-- /worked-example -->

### Dịch chuỗi khi dữ liệu thiếu tháng {#dich-chuoi-va-cam-bay-thieu-thang}

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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-5 -->

::: example Phân biệt dịch chuyển giá trị và dịch chuyển chỉ mục thời gian với freq

Trong phân tích chuỗi thời gian kinh tế, người phân tích cần tính tỷ lệ tăng trưởng so với kỳ trước hoặc căn chỉnh các chuỗi dữ liệu có độ trễ. Phương thức shift mặc định dịch chuyển giá trị dữ liệu theo số hàng và để lại giá trị khuyết thiếu ở đầu chuỗi. Ngược lại, khi truyền thêm tham số freq, phương thức này giữ nguyên toàn bộ mảng giá trị và chỉ tịnh tiến các mốc thời gian trên trục chỉ mục.

```python
import pandas as pd

idx = pd.date_range("2026-01-31", periods=3, freq="ME")
ts = pd.Series([120, 150, 180], index=idx, name="goc")

# Dịch chuyển giá trị: giữ nguyên nhãn ngày, đưa giá trị hàng trước xuống hàng kế tiếp
s_val = ts.shift(1)

# Dịch chuyển chỉ mục: giữ nguyên giá trị, đẩy nhãn ngày tiến 1 tháng
s_freq = ts.shift(1, freq="ME")

# Kết hợp thành bảng theo dõi để quan sát sự khác biệt
bang_kq = pd.DataFrame({
    "ngay_goc": ts.index.strftime("%Y-%m-%d"),
    "gia_tri": ts.values,
    "shift_val": s_val.values,
    "ngay_moi": s_freq.index.strftime("%Y-%m-%d"),
    "shift_freq": s_freq.values,
})
bang_kq = bang_kq.astype(object).where(pd.notna(bang_kq), None)
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| ngay&#95;goc | gia&#95;tri | shift&#95;val | ngay&#95;moi | shift&#95;freq |
| --- | --- | --- | --- | --- |
| 2026-01-31 | 120 | (thiếu) | 2026-02-28 | 120 |
| 2026-02-28 | 150 | 120.0 | 2026-03-31 | 150 |
| 2026-03-31 | 180 | 150.0 | 2026-04-30 | 180 |

</div>

Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.

Phương thức Series.shift là công cụ tạo biến trễ cơ bản khi làm việc với chuỗi thời gian. Khi gọi ts.shift(1) không kèm tham số tần số, pandas giữ cố định toàn bộ chỉ mục thời gian ban đầu và dịch chuyển các giá trị dọc theo hàng: Mỗi quan sát nhận giá trị của hàng liền trước đó trong bảng dữ liệu. Dòng đầu tiên tại mốc 2026-01-31 nhận giá trị khuyết thiếu NaN vì không có hàng nào đứng trước nó, trong khi giá trị 120 của tháng 1 được chuyển xuống dòng ngày 2026-02-28.

Trái lại, khi truyền thêm tham số tần số như ts.shift(1, freq='ME'), cơ chế thực thi thay đổi: Toàn bộ mảng giá trị [120, 150, 180] được giữ nguyên vẹn và không xuất hiện giá trị khuyết thiếu. Thay vào đó, toàn bộ các mốc thời gian trên trục chỉ mục bị tịnh tiến thêm một chu kỳ tần số cuối tháng, biến tập chỉ mục ban đầu thành [28/02, 31/03, 30/04].

Sự phân biệt giữa hai hình thức dịch chuyển này gắn liền với mục tiêu phân tích: Dịch chuyển giá trị dùng để tính toán mức chênh lệch giữa hai thời điểm trên cùng một bảng dữ liệu cố định (ví dụ ts - ts.shift(1)), còn dịch chuyển chỉ mục dùng để dời toàn bộ chuỗi quan sát về tương lai nhằm đóng vai trò biến dự báo cho mốc thời gian tiếp theo.

Cần lưu ý rằng việc gọi ts.shift(1) không kèm freq dịch chuyển thuần túy theo vị trí hàng quan sát: Nếu dữ liệu bị ngắt quãng hoặc thiếu tháng, hàng liền trước có thể cách xa hai hoặc ba tháng trước đó. Trong nhiều bài toán tài chính, việc dịch chuyển theo hàng giao dịch thực tế là hành vi được mong muốn có chủ đích. Tuy nhiên, nếu mục tiêu là so sánh đúng độ dài thời gian theo lịch, việc căn chỉnh chuỗi về lưới lịch đều đặn bằng asfreq hoặc resample là một lựa chọn thiết kế cần được cân nhắc kỹ lưỡng.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-6 -->

::: example Biến đổi cột ngày sang chu kỳ kinh doanh với dt.to_period và tổng hợp theo tháng

Trong các báo cáo quản trị doanh nghiệp, các giao dịch phát sinh rải rác vào các ngày giờ ngẫu nhiên trong tháng cần được phân loại về chu kỳ kế toán tương ứng, chẳng hạn tháng 1 hoặc tháng 2 năm 2026. Nếu sử dụng chuỗi ký tự cắt lát để gom nhóm, dữ liệu sẽ mất đi trật tự thời gian và khả năng tính toán số học trên chu kỳ. Ta sử dụng thuộc tính dt.to_period để quy đổi các mốc thời gian sang đối tượng Period.

```python
import pandas as pd

df_don = pd.DataFrame({
    "ma": ["DH01", "DH02", "DH03", "DH04"],
    "ngay": pd.to_datetime([
        "2026-01-12 09:30",
        "2026-01-28 14:15",
        "2026-02-05 11:00",
        "2026-02-20 16:45",
    ]),
    "doanh_thu": [250, 180, 310, 420],
})

# Chuyển đổi Timestamp sang Period chu kỳ tháng
df_don["ky_thang"] = df_don["ngay"].dt.to_period("M")

# Tổng hợp doanh thu theo từng chu kỳ tháng
tong_hop = df_don.groupby("ky_thang")["doanh_thu"].agg(
    tong="sum", so_don="count"
).reset_index()

# Chuyển đổi kỳ sang chuỗi hiển thị gọn gàng
bang_kq = pd.DataFrame({
    "ky": tong_hop["ky_thang"].astype(str),
    "tong": tong_hop["tong"],
    "so_don": tong_hop["so_don"],
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| ky | tong | so&#95;don |
| --- | --- | --- |
| 2026-01 | 430 | 2 |
| 2026-02 | 730 | 2 |

</div>

Cột `ngay` ghi từng thời điểm giao dịch. Khi báo cáo theo tháng, ta cần nhận biết các ngày thuộc cùng kỳ mà vẫn giữ một kiểu có thể tính toán theo lịch. `dt.to_period("M")` chuyển mỗi thời điểm sang kỳ tháng như `2026-01` hoặc `2026-02`.

Một `Period` mang cả giá trị kỳ và tần số. Cộng 1 vào kỳ tháng sẽ sang tháng kế tiếp, dù các tháng có số ngày khác nhau. Nếu thời gian ban đầu có múi giờ, cần xác định tháng đang xét theo múi giờ nào trước khi chuyển, vì kỳ không giữ thông tin múi giờ đó.

Sau khi có cột chu kỳ Period, phép gom nhóm df.groupby('ky_thang') cho phép tính toán các chỉ số tổng hợp như tổng doanh thu và số lượng đơn hàng cho từng tháng. Khi cần chuyển đổi ngược lại thành các mốc thời gian để vẽ đồ thị hoặc lưu trữ vào cơ sở dữ liệu quan hệ, phương thức to_timestamp(how='start') hoặc to_timestamp(how='end') sẽ tự động xác định ngày đầu tiên hoặc ngày cuối cùng của chu kỳ đó.

Hai ngày của tháng 1 cho tổng doanh thu 430, còn hai ngày của tháng 2 cho 730. `count` ở đây đếm giá trị doanh thu không thiếu. Nếu mục tiêu là đếm mọi đơn dù chưa có doanh thu, hãy dùng `size` cho số bản ghi hoặc đếm một mã đơn bắt buộc có giá trị.

:::

<!-- /worked-example -->

## 6. Lấy mẫu lại (Resampling): Tần số, Biên khoảng và kỳ chưa đủ dữ liệu {#_6-lay-mau-lai-resampling-tan-so-bien-đong-mo-va-bay-ky-dang-do}

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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-7 -->

::: example Xác lập ranh giới đóng mở khoảng thời gian khi gom nhóm với closed và label

Khi gom nhóm chuỗi thời gian tần số cao về các khung cửa sổ định kỳ (chẳng hạn mỗi 10 phút), các giao dịch phát sinh đúng tại mốc ranh giới như 10:10:00 sẽ được tính vào khung giờ trước hay khung giờ sau? Sự khác biệt giữa tham số closed và tham số label quyết định việc phân chia dữ liệu và nhãn hiển thị thời gian. Ta so sánh hai cấu hình biên để nắm rõ quy luật gán nhãn của pandas.

```python
import pandas as pd

# Giả lập 4 giao dịch tại các mốc phút liền kề
idx = pd.to_datetime([
    "2026-03-01 10:00:00",
    "2026-03-01 10:05:00",
    "2026-03-01 10:10:00",
    "2026-03-01 10:15:00",
])
s = pd.Series([10, 20, 30, 40], index=idx)

# So sánh hai cấu hình biên phổ biến trong resample 10 phút
rs_left = s.resample("10min", closed="left", label="left").sum()
rs_right = s.resample("10min", closed="right", label="right").sum()

df_cmp = pd.concat([
    rs_left.rename("left_sum"),
    rs_right.rename("right_sum"),
], axis=1)
df_cmp["thoi_diem"] = df_cmp.index.strftime("%H:%M")
bang_kq = df_cmp[["thoi_diem", "left_sum", "right_sum"]].reset_index(drop=True)
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| thoi&#95;diem | left&#95;sum | right&#95;sum |
| --- | --- | --- |
| 10:00 | 30.0 | 10 |
| 10:10 | 70.0 | 50 |
| 10:20 | (thiếu) | 40 |

</div>

Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.

Phương thức Series.resample là phiên bản chuyên biệt của groupby trên trục thời gian, thực hiện phân chia chuỗi dữ liệu liên tục thành các khối khoảng thời gian đều đặn. Khi chia khoảng, một câu hỏi kỹ thuật cơ bản phát sinh: Một giá trị nằm đúng tại mốc ranh giới (ví dụ 10:10:00) sẽ thuộc về khoảng nào? Tham số closed='left' quy định khoảng thời gian có dạng nửa mở nửa đóng [10:00, 10:10), nghĩa là nhận mốc 10:00 nhưng loại trừ mốc 10:10 để đưa sang khoảng kế tiếp. Ngược lại, closed='right' quy định khoảng có dạng (10:00, 10:10], nghĩa là nhận mốc 10:10 vào khoảng hiện tại.

Đi kèm với việc phân định ranh giới là việc chọn nhãn đại diện thông qua tham số label. Khi gom nhóm các sự kiện xảy ra trong 10 phút, người lập trình có thể dùng thời điểm bắt đầu của khoảng làm nhãn (label='left') hoặc dùng thời điểm kết thúc làm nhãn (label='right'). Trong thực tế, quy ước phổ biến là closed='left', label='left' cho các khung thời gian trong ngày (như phút hoặc giờ), trong khi các tần số theo tháng hoặc quý (như 'ME', 'QE') lại mặc định dùng closed='right', label='right'.

Với biên trái và nhãn trái, khoảng `[10:00, 10:10)` chứa 10 và 20 nên tổng tại nhãn 10:00 là 30. Khoảng `[10:10, 10:20)` chứa 30 và 40 nên cho 70. Với biên phải và nhãn phải, khoảng `(09:50, 10:00]` cho 10, còn `(10:00, 10:10]` cho 50.

Cấu hình phải còn một khoảng kết thúc lúc 10:20, chứa giá trị 40. Cấu hình trái không có nhãn 10:20 trong kết quả nên khi `concat` căn hai Series, ô bên trái tại đó là thiếu. Giữ ô thiếu giúp phân biệt một khoảng chưa có trong kết quả với một tổng thật sự bằng 0. Tham số `label` chỉ chọn nhãn, còn `closed` mới quyết định một điểm biên thuộc khoảng nào.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-8 -->

::: example Nội suy theo trọng số khoảng cách thời gian khi dữ liệu ngắt quãng không đều

Khi chuỗi thời gian có khoảng cách quan sát ngắt quãng không đều đặn, phương pháp nội suy tuyến tính thông thường sẽ coi khoảng cách giữa các hàng là đồng đều. Phương thức interpolate với method='time' tính toán tỷ lệ nội suy dựa trên khoảng cách thời gian thực tế giữa các mốc DatetimeIndex.

```python
import pandas as pd

# Ba mốc quan sát ngắt quãng không đều: 01/03, 02/03 và 10/03
idx = pd.to_datetime(["2026-03-01", "2026-03-02", "2026-03-10"])
s = pd.Series([10.0, None, 100.0], index=idx)

# So sánh nội suy tuyến tính theo hàng và nội suy theo khoảng cách thời gian
s_linear = s.interpolate(method="linear")
s_time = s.interpolate(method="time")

bang_kq = pd.DataFrame({
    "ngay": idx.strftime("%Y-%m-%d"),
    "goc": s.values,
    "linear": s_linear.values,
    "time": s_time.values,
})
bang_kq = bang_kq.astype(object).where(pd.notna(bang_kq), None)
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| ngay | goc | linear | time |
| --- | --- | --- | --- |
| 2026-03-01 | 10.0 | 10.0 | 10.0 |
| 2026-03-02 | (thiếu) | 55.0 | 20.0 |
| 2026-03-10 | 100.0 | 100.0 | 100.0 |

</div>

Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.

Trong xử lý chuỗi thời gian, việc xuất hiện các giá trị khuyết thiếu do ngắt quãng đo đạc là tình huống thường gặp. Để lấp đầy các khoảng trống này, pandas cung cấp phương thức interpolate() với nhiều cơ chế xấp xỉ toán học khác nhau. Hai phương thức phổ biến là method='linear' (mặc định) và method='time'.

Khi các mốc quan sát nằm trên một lưới thời gian đều đặn (chẳng hạn mỗi ngày một mốc), cả hai phương thức linear và time đều cho kết quả hoàn toàn giống nhau vì khoảng cách hàng trùng khớp với khoảng cách thời gian. Sự khác biệt chỉ thực sự xuất hiện khi chuỗi thời gian có khoảng cách đo không đều đặn. Phương thức linear coi các dòng dữ liệu có khoảng cách số nguyên đồng đều (vị trí 0, 1, 2) bất chấp giá trị của chỉ mục thời gian, do đó giá trị tại dòng ở giữa được tính bằng trung bình cộng đơn giản của hai đầu mút: (10.0 + 100.0) / 2 = 55.0.

Từ 01/03 đến 10/03 có 9 ngày, hai giá trị đầu cuối lệch 90. Nếu nội suy tuyến tính theo thời gian, mỗi ngày tăng 10 đơn vị nên 02/03 nhận `10 + 90 × 1/9 = 20`. Đây là giá trị ước lượng dưới giả định tuyến tính, không phải phép đo được khôi phục chắc chắn.

Nội suy dùng cả hai đầu mút đã biết. Với dự báo tại 02/03, dữ liệu ngày 10/03 chưa có ở thời điểm đó nên không được dùng để tiền xử lý tập đánh giá tương lai. Với phân tích hồi cứu, có thể sử dụng khi giả định biến thiên tuyến tính phù hợp và ghi nhận rõ giá trị nào đã được ước lượng.

:::

<!-- /worked-example -->

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

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-9 -->

::: example Xử lý chuỗi thời gian không đều đặn với cửa sổ khoảng thời gian và min_periods

Khi chuỗi thời gian có khoảng cách quan sát không đều đặn (như các giao dịch phát sinh vào ngày làm việc và ngắt quãng vào cuối tuần), cửa sổ trượt theo số lượng hàng cố định sẽ gom các quan sát thuộc các khoảng thời gian xa nhau. Pandas cho phép truyền chuỗi khoảng thời gian như '2D' vào phương thức rolling để tính toán trên đúng độ dài thời gian thực tế.

```python
import pandas as pd

# 4 giao dịch không đều ngày: 01/03, 02/03, 05/03 và 06/03
idx = pd.to_datetime(["2026-03-01", "2026-03-02", "2026-03-05", "2026-03-06"])
s = pd.Series([10.0, 20.0, 30.0, 40.0], index=idx)

# Cửa sổ 2 hàng cố định so với cửa sổ 2 ngày thời gian thực
tb_hang = s.rolling(2).mean()
tb_thoi_gian = s.rolling("2D").mean()

bang_kq = pd.DataFrame({
    "ngay": s.index.strftime("%Y-%m-%d"),
    "gia_tri": s.values,
    "tb_2_hang": tb_hang.values,
    "tb_2_ngay": tb_thoi_gian.values,
})
bang_kq = bang_kq.astype(object).where(pd.notna(bang_kq), None)
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| ngay | gia&#95;tri | tb&#95;2&#95;hang | tb&#95;2&#95;ngay |
| --- | --- | --- | --- |
| 2026-03-01 | 10.0 | (thiếu) | 10.0 |
| 2026-03-02 | 20.0 | 15.0 | 15.0 |
| 2026-03-05 | 30.0 | 25.0 | 30.0 |
| 2026-03-06 | 40.0 | 35.0 | 35.0 |

</div>

Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.

Kỹ thuật cửa sổ trượt (Rolling Windows) giúp làm mượt các dao động ngắn hạn để làm lộ rõ xu hướng vận động chính của chuỗi thời gian. Cú pháp cơ bản s.rolling(2).mean() xác lập một cửa sổ gồm 2 hàng quan sát liên tiếp. Phép tính trượt theo số lượng hàng này hoàn toàn có ý nghĩa khi mục tiêu là làm mượt qua 2 sự kiện giao dịch gần nhất, bất kể hai sự kiện đó diễn ra cách nhau bao lâu.

Tuy nhiên, nếu mục tiêu là đánh giá mức biến động trong một khoảng thời gian cố định theo lịch, việc trượt theo số hàng có thể dẫn đến việc gom các quan sát thuộc các tuần lễ khác nhau. Quan sát ngày 2026-03-05: Hàng liền trước nó là ngày 2026-03-02, cách xa 3 ngày. Phép tính s.rolling(2) gom giá trị 20.0 của ngày 02/03 với 30.0 của ngày 05/03 để tính trung bình ra 25.0.

Trái lại, khi truyền tham số chuỗi thời gian s.rolling('2D'), pandas xác định cửa sổ trượt tại mỗi dòng là khoảng thời gian kéo dài đúng 2 ngày kết thúc tại mốc quan sát hiện tại. Với mốc 05/03 lúc 00:00:00, khoảng cửa sổ 2 ngày mặc định là nửa mở nửa đóng (03/03 00:00, 05/03 00:00]. Vì ngày 02/03 nằm ngoài khoảng thời gian này, cửa sổ '2D' tại ngày 05/03 chỉ chứa duy nhất điểm dữ liệu của chính nó và trả về giá trị trung bình là 30.0. Đến ngày 06/03, khoảng 2 ngày (04/03 00:00, 06/03 00:00] chứa cả 05/03 và 06/03 nên trung bình trả về là (30 + 40) / 2 = 35.0.

Cửa sổ số nguyên 2 mặc định cần đủ 2 giá trị không thiếu, còn cửa sổ thời gian `"2D"` mặc định chỉ cần 1. Do đó, hàng đầu của hai phép tính khác nhau. Có thể đặt `min_periods` tường minh để yêu cầu một số mẫu tối thiểu. Đây là số quan sát hợp lệ, không phải độ dài thời gian.

:::

<!-- /worked-example -->

### Làm mượt theo hàm mũ (Exponentially Weighted Moving)

Phương pháp cửa sổ trượt gán trọng số đồng đều cho mọi ngày trong cửa sổ. Trái lại, phương pháp **làm mượt hàm mũ (EWM)** gán trọng số giảm dần theo cấp số nhân khi càng lùi xa về quá khứ:

```python
s_gia = pd.Series([10.0, 12.0, 15.0, 14.0, 16.0])

# Tính trung bình trượt hàm mũ với span = 3
ewm_tb = s_gia.ewm(span=3).mean()
print("EWM làm mượt:")
print(pd.DataFrame({"Goc": s_gia, "EWM": ewm_tb}))
```

<!-- worked-example bai-08-du-lieu-thoi-gian-worked-10 -->

::: example Điều khiển tốc độ suy giảm trọng số lịch sử qua tham số halflife trong ewm

Khi làm mượt dữ liệu bằng trung bình trượt hàm mũ, tham số halflife quy định độ dài thời gian mà sau đó mức độ ảnh hưởng của một quan sát trong quá khứ bị suy giảm đi một nửa. Ta so sánh phản ứng của đường xu hướng trước một biến động đột ngột với hai mức halflife khác nhau.

```python
import pandas as pd

# Giả lập một biến động nhảy vọt từ 10 lên 50 tại thời điểm t=1
idx = pd.date_range("2026-03-01", periods=5, freq="D")
s = pd.Series([10.0, 50.0, 10.0, 10.0, 10.0], index=idx)

# So sánh làm mượt với halflife ngắn (1 ngày) và halflife dài (3 ngày)
ewm_nhanh = s.ewm(halflife="1D", times=idx).mean()
ewm_cham = s.ewm(halflife="3D", times=idx).mean()

bang_kq = pd.DataFrame({
    "ngay": idx.strftime("%Y-%m-%d"),
    "tin_hieu": s.values,
    "ewm_hl1": ewm_nhanh.round(2).values,
    "ewm_hl3": ewm_cham.round(2).values,
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| ngay | tin&#95;hieu | ewm&#95;hl1 | ewm&#95;hl3 |
| --- | --- | --- | --- |
| 2026-03-01 | 10.0 | 10.0 | 10.0 |
| 2026-03-02 | 50.0 | 36.67 | 32.3 |
| 2026-03-03 | 10.0 | 21.43 | 23.1 |
| 2026-03-04 | 10.0 | 15.33 | 18.62 |
| 2026-03-05 | 10.0 | 12.58 | 16.02 |

</div>

Khác với phương pháp cửa sổ trượt thông thường vốn phân bổ trọng số bằng nhau cho mọi quan sát trong cửa sổ rồi đột ngột bỏ qua các quan sát bên ngoài, phương pháp làm mượt hàm mũ (Exponentially Weighted Moving - EWM) gán trọng số suy giảm liên tục theo quy luật hàm mũ khi lùi dần về quá khứ. Điều này giúp đường làm mượt phản ứng nhanh nhạy trước các biến động mới nhất trong khi vẫn duy trì ảnh hưởng giảm dần của lịch sử.

Mặc định `adjust=True`, kết quả là tổng có trọng số chia cho tổng trọng số. Ở ngày thứ hai với chu kỳ bán rã 1 ngày, quan sát cũ có trọng số 0.5 và quan sát mới có trọng số 1. Giá trị là `(10 × 0.5 + 50) / 1.5`, xấp xỉ 36.67.

Trong các cách đặc tả hệ số suy giảm của pandas, tham số halflife kết hợp với times=idx mang lại ý nghĩa trực quan khi xử lý chuỗi thời gian: Với halflife='1D', cứ sau mỗi ngày trôi qua, trọng số ảnh hưởng của một quan sát trong quá khứ lại giảm đi một nửa. Với halflife='3D', phải sau 3 ngày thì trọng số của biến động mới giảm 50%, đồng nghĩa đường cong có độ trễ lớn hơn và duy trì ảnh hưởng quá khứ lâu hơn.

Chu kỳ bán rã 1 ngày cho 36.67 ở đỉnh rồi về 12.58 vào ngày cuối. Chu kỳ 3 ngày cho đỉnh 32.30 và giá trị cuối 16.02. Kết quả thể hiện mức độ phản ứng với chuỗi mẫu này. Cần chọn độ làm mượt theo khoảng thời gian và mục tiêu phân tích, không chỉ chọn đường nhìn ít dao động hơn.

:::

<!-- /worked-example -->

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
