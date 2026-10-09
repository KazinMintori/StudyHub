---
course: xu-ly-du-lieu
lecture: bai-08-du-lieu-thoi-gian
section: lecture
title: "Xử lý dữ liệu thời gian"
prerequisites: ["chi-muc","gia-tri-thieu","ky-vong"]
lessonStatus: ready
description: "Làm chủ chuỗi thời gian trong pandas: DatetimeIndex, cắt lát chuỗi, lấy mẫu lại resample, cửa sổ trượt rolling và so sánh cùng kỳ YoY vs MoM."
---

Thời gian không phải là một chuỗi văn bản thông thường, và càng không phải là một con số vô hướng đơn thuần. Trong tự nhiên cũng như trong phân tích dữ liệu, thời gian sở hữu một đặc tính cốt lõi: **mũi tên một chiều (Arrow of Time)**. Mọi sự kiện diễn ra trong quá khứ định hình trạng thái hiện tại, trong khi tương lai là miền bất định và tuyệt đối không bao giờ được phép rò rỉ ngược về quá khứ trong các quy trình huấn luyện mô hình dự báo.

Hơn thế nữa, dữ liệu thời gian mang bản chất bất đối xứng của các quy ước xã hội và thiên văn học: năm nhuận có 366 ngày, số ngày giữa các tháng chênh lệch nhau, các hệ thống phân tán đặt tại nhiều múi giờ khác nhau, và quy ước đổi giờ mùa hè (Daylight Saving Time) có thể làm dòng thời gian nhảy cóc một tiếng hoặc lặp lại một tiếng. Nếu xử lý cẩu thả bằng cách ghép chuỗi hay chia số nguyên đơn thuần, toàn bộ các chỉ số thống kê và báo cáo tài chính sẽ bị méo mó nghiêm trọng.

Bài giảng này trình bày bài bản cách làm chủ dữ liệu chuỗi thời gian (Time Series) trong Python và pandas: từ việc phân biệt ba phạm trù thời gian, kỹ thuật quản trị múi giờ chuẩn mực, các phép cắt lát chuỗi trực quan trên `DatetimeIndex`, đến kỹ thuật lấy mẫu lại (`resample`), làm mượt dao động bằng cửa sổ trượt (`rolling`), và phương pháp tính toán so sánh cùng kỳ khoa học.

---

## 1. Ba phạm trù cốt lõi: Điểm thời gian, Khoảng biến thiên và Kỳ hạn

Để tư duy mạch lạc và tránh những lỗi ngớ ngẩn khi lập trình, ta cần phân biệt rạch ròi ba khái niệm thời gian hoàn toàn khác nhau trong toán học và đời sống thực tế:

1. **Điểm thời gian (Timestamp)**: Đại diện cho một khoảnh khắc cố định duy nhất trên trục thời gian liên tục, chẳng hạn đúng 09:15:30 ngày 15 tháng 3 năm 2026. Trong pandas, đối tượng đại diện là `pd.Timestamp` (tương đương với `datetime.datetime` của Python chuẩn nhưng có độ phân giải nano giây).
2. **Khoảng biến thiên (Timedelta)**: Đại diện cho độ dài của một khoảng cách thời gian giữa hai biến cố, không gắn với bất kỳ ngày tháng cụ thể nào, chẳng hạn như khoảng thời gian kéo dài 48 giờ hoặc 3 ngày 5 tiếng. Đối tượng tương ứng là `pd.Timedelta`.
3. **Kỳ hạn (Period)**: Đại diện cho một khoảng thời gian hữu hạn gắn liền với một nhịp lịch thiên văn hay lịch tài chính, ví dụ trọn vẹn tháng 3 năm 2026 hoặc Quý 2 năm 2026. Một thời điểm nằm trong tháng 3 không đồng nghĩa với toàn bộ khoảng thời gian của tháng 3. Đối tượng đại diện là `pd.Period`.

```python
import numpy as np
import pandas as pd

# 1. Điểm thời gian (Timestamp)
t1 = pd.Timestamp("2026-03-15 09:15:30")
t2 = pd.Timestamp("2026-03-18 15:30:00")

# 2. Khoảng biến thiên (Timedelta) sinh ra từ hiệu của hai Timestamp
khoang_cach = t2 - t1
print("Khoảng cách:", khoang_cach)          # 3 days 06:14:30
print("Số ngày thực tế:", khoang_cach.days) # 3
print("Tổng số giây:", khoang_cach.total_seconds())

# 3. Kỳ hạn (Period)
ky_thang = pd.Period("2026-03", freq="M")
print("Kỳ hạn tháng 3:", ky_thang)
print("Bắt đầu:", ky_thang.start_time, "-> Kết thúc:", ky_thang.end_time)
```

Khi chuyển đổi văn bản sang ngày tháng, hai cạm bẫy lớn nhất là định dạng ngày tháng mập mờ và dữ liệu rác:

- **Khóa chặt định dạng bằng tham số `format`**: Chuỗi `"02/03/2026"` đối với người Việt Nam hay người Anh là ngày 2 tháng 3, nhưng đối với người Mỹ lại là ngày 3 tháng 2. Nếu ta không chỉ định tường minh `format="%d/%m/%Y"`, pandas sẽ phải tự phỏng đoán dựa trên dữ liệu mẫu và rất dễ hoán đổi ngày thành tháng khi ngày nhỏ hơn hoặc bằng 12.
- **Xử lý chuỗi phi lý bằng `errors="coerce"`**: Tháng 2 không bao giờ có ngày 30 hay 31. Khi gặp chuỗi sai trái như `"31/02/2026"`, nếu để mặc định chương trình sẽ ném ngoại lệ làm sập toàn bộ đường ống xử lý. Tham số `errors="coerce"` sẽ biến các ô lỗi này thành giá trị **`NaT`** (*Not a Time* - hằng số khuyết thiếu chuẩn dành riêng cho dữ liệu thời gian trong pandas).

```python
chuoi_ngay = pd.Series(["01/02/2026", "15/02/2026", "31/02/2026", "chua_xac_dinh"])
ngay_chuan = pd.to_datetime(chuoi_ngay, format="%d/%m/%Y", errors="coerce")

print("Kết quả chuẩn hóa:")
print(ngay_chuan)
print("Mảng nhận diện khuyết thiếu:", ngay_chuan.isna().tolist())
```

---

## 2. Quản trị múi giờ: Bản chất của Localize và Convert

Một sai lầm kinh điển trong các hệ thống thông tin là việc lưu trữ thời gian dưới dạng chuỗi hoặc số nguyên ngây thơ mà không gắn kèm thông tin múi giờ. Khi hệ thống mở rộng đa quốc gia, thời điểm 08:00 sáng tại Tokyo (UTC+9) bị nhầm lẫn ngang bằng với 08:00 sáng tại Hà Nội (UTC+7) hay London (UTC+0), dẫn đến việc đối soát giao dịch và phân tích hành vi khách hàng bị sai lệch hoàn toàn.

Trong pandas, ta phân biệt hai trạng thái dữ liệu:
- **Thời gian ngây thơ (Timezone-naive)**: Dữ liệu chỉ ghi nhận giờ số học đơn thuần, hoàn toàn không chứa thông tin về độ lệch múi giờ so với giờ phối hợp quốc tế (UTC).
- **Thời gian có nhận thức (Timezone-aware)**: Dữ liệu gắn liền với một múi giờ cụ thể theo chuẩn cơ sở dữ liệu quốc tế IANA (ví dụ: `Asia/Ho_Chi_Minh`, `Europe/London`, `America/Santiago`).

Hai phép toán quản trị múi giờ mang ý nghĩa bản chất hoàn toàn khác nhau:

```python
# Tạo điểm thời gian ngây thơ (chưa biết múi giờ)
t_ngay_tho = pd.Timestamp("2026-03-15 08:00:00")

# 1. tz_localize: Gán nhãn nhận thức múi giờ cho dữ liệu ngây thơ
# Không thay đổi số giờ hiển thị, chỉ gắn thêm thông tin ngữ cảnh địa phương
t_ha_noi = t_ngay_tho.tz_localize("Asia/Ho_Chi_Minh")
print("Giờ Hà Nội:", t_ha_noi)  # 2026-03-15 08:00:00+07:00

# 2. tz_convert: Chuyển đổi tọa độ thời gian từ múi giờ này sang múi giờ khác
# Mốc thời gian vật lý giữ nguyên, nhưng số giờ hiển thị được tính lại theo kinh độ mới
t_utc = t_ha_noi.tz_convert("UTC")
t_london = t_ha_noi.tz_convert("Europe/London")

print("Giờ UTC:", t_utc)        # 2026-03-15 01:00:00+00:00 (lùi 7 tiếng)
print("Giờ London:", t_london)  # 2026-03-15 01:00:00+00:00
```

Một lưu ý đặc biệt quan trọng: Nếu dữ liệu nguồn thu thập tại Hà Nội nhưng bạn lại vội vã gọi `pd.to_datetime(..., utc=True)`, pandas sẽ ngây thơ coi con số `08:00` đó vốn dĩ là 8 giờ sáng theo giờ UTC, sau đó gắn đuôi `+00:00`. Kết quả là thời điểm phát sinh sự kiện bị chạy nhanh hơn thực tế đúng 7 tiếng đồng hồ. Quy trình chuẩn mực luôn là: **`tz_localize` trước để xác định vị trí thực địa, rồi mới `tz_convert` về UTC để lưu trữ đồng bộ**.

---

## 3. Chỉ mục thời gian `DatetimeIndex` và kỹ thuật cắt lát chuỗi ký tự

Khi đưa một cột ngày tháng đã chuẩn hóa thành chỉ mục (index) của DataFrame bằng `set_index("date")` và sắp xếp tăng dần bằng `sort_index()`, bảng dữ liệu trở thành một **chuỗi thời gian thực thụ**. 

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

Cơ chế này hoạt động cực kỳ hiệu quả nhờ thuật toán tìm kiếm nhị phân trên chỉ mục đơn điệu tăng dần (`is_monotonic_increasing`). Nếu chỉ mục chưa được sắp xếp, thao tác cắt lát chuỗi có thể trả về kết quả sai hoặc ném ra cảnh báo nghiêm trọng.

---

## 4. Lấy mẫu lại (Resampling): Tần số, Biên đóng mở và Bẫy kỳ dang dở

Trong thực tế, các sự kiện trong đời sống diễn ra ở các nhịp độ ngẫu nhiên: có ngày có hàng trăm lượt đánh giá của khách hàng, có ngày không có lượt nào. Để phát hiện quy luật kinh doanh, ta cần tổng hợp dữ liệu về các thang đo định kỳ đều đặn (theo ngày, tuần, tháng, quý hoặc năm). Quá trình này được gọi là **lấy mẫu lại (Resampling)**.

### Bảng quy chuẩn mã tần số (Frequency Aliases) trong pandas hiện đại

Từ các phiên bản pandas gần đây, các ký hiệu tần số kết thúc kỳ đã được chuẩn hóa rõ ràng để tránh hiểu nhầm với các ký hiệu bắt đầu kỳ:

| Mã tần số mới | Mã cũ (đã cảnh báo) | Ý nghĩa chu kỳ |
| :--- | :--- | :--- |
| **`"D"`** | `"D"` | Theo ngày theo lịch (Calendar day) |
| **`"B"`** | `"B"` | Theo ngày làm việc (Business day, thứ Hai đến thứ Sáu) |
| **`"W"`** hoặc `"W-MON"` | `"W"` | Theo tuần (mặc định Chủ nhật hoặc neo vào thứ Hai) |
| **`"ME"`** | `"M"` | Cuối tháng (Month End) |
| **`"MS"`** | `"MS"` | Đầu tháng (Month Start) |
| **`"QE"`** | `"Q"` | Cuối quý (Quarter End) |
| **`"QS"`** | `"QS"` | Đầu quý (Quarter Start) |
| **`"YE"`** | `"Y"` hoặc `"A"` | Cuối năm (Year End) |

### Lấy mẫu giảm tần số (Downsampling) và quy tắc biên `closed`, `label`

Downsampling là việc gộp dữ liệu từ tần số cao xuống tần số thấp hơn (ví dụ từ giờ sang ngày, từ ngày sang tháng). Khi gộp các khoảng thời gian, hai tham số quyết định ranh giới tính toán:
- `closed`: Xác định biên nào của khoảng thời gian được tính vào kỳ. Mặc định đối với các tần số cuối kỳ như `"ME"`, `"QE"` là `closed="right"` (nhận cận phải).
- `label`: Xác định nhãn hiển thị của kỳ gộp. Mặc định là `label="right"` (lấy mốc thời gian của cận phải làm đại diện).

```python
# Ví dụ: Gộp số lượng giao dịch theo tháng
# Tạo dữ liệu giao dịch phát sinh rải rác
ngay_gd = pd.to_datetime(["2026-01-05", "2026-01-20", "2026-02-14", "2026-03-01", "2026-03-25"])
df_gd = pd.DataFrame({"tien": [100, 200, 150, 300, 250]}, index=ngay_gd)

# Lấy mẫu theo tháng kết thúc (Month End)
thang_gd = df_gd.resample("ME").agg(tong_tien=("tien", "sum"), so_gd=("tien", "count"))
print(thang_gd)
```

### Cạm bẫy sống còn: Kỳ dang dở (Incomplete Period Trap)

Giả sử bạn trích xuất dữ liệu của một hệ thống vào ngày **29 tháng 6 năm 2026**.
Khi gọi `resample("QE").sum()`, pandas sẽ gom toàn bộ các ngày từ tháng 4 đến hết ngày 29/6 vào Quý 2 năm 2026 và gán nhãn là ngày kết thúc quý: `2026-06-30`.

Tuy nhiên, Quý 2 thực tế có 91 ngày, trong khi dữ liệu của bạn mới chỉ ghi nhận đến ngày 29 (thiếu ngày 30). Khi đem so sánh tổng doanh thu hoặc số lượng đánh giá của Quý 2 với Quý 1 (vốn đã trọn vẹn 90 ngày), con số của Quý 2 trông như bị sụt giảm. Nếu người phân tích ngây thơ đưa con số này vào biểu đồ báo cáo, các nhà quản lý sẽ hoang mang vì ngỡ rằng hoạt động kinh doanh đang lao dốc.

**Quy tắc thẩm định**: Khi mốc chụp dữ liệu (*snapshot*) nằm trước ngày kết thúc của kỳ tổng hợp, kỳ đó là **kỳ chưa trọn vẹn**. Bắt buộc phải loại bỏ kỳ này khỏi các phân tích so sánh tổng sản lượng, hoặc phải chuẩn hóa thành chỉ số trung bình theo ngày.

---

## 5. Dịch chuỗi, So cùng kỳ (YoY vs MoM) và Cửa sổ trượt (Rolling Windows)

### So kỳ liền trước (MoM/QoQ) so với So cùng kỳ năm trước (YoY)

Để đánh giá tình hình tăng trưởng, người làm dữ liệu thường sử dụng hai thước đo:
1. **So kỳ liền trước (Period-over-Period, ví dụ Month-over-Month - MoM)**: Đo lường xung lực ngắn hạn giữa tháng này và tháng ngay trước đó.
2. **So cùng kỳ năm trước (Year-over-Year - YoY)**: So sánh tháng này với chính tháng này của năm trước.

Công thức tính tỷ lệ tăng trưởng phần trăm:
$$
g = \left( \frac{Y_t}{Y_{t-k}} - 1 \right) \times 100\%
$$

Trong kinh doanh có tính mùa vụ (Seasonality), ví dụ như ngành du lịch, dịch vụ nhà hàng hay bán lẻ thời trang:
- Tháng 1 và tháng 2 (dịp Tết hoặc mùa du lịch hè) luôn có lượng khách tăng đột biến so với tháng 11 hay tháng 12 năm trước. So sánh MoM giữa tháng 1 với tháng 12 sẽ tạo ra ảo tưởng về sự tăng trưởng thần tốc.
- Trái lại, so sánh YoY giữa tháng 1 năm nay với tháng 1 năm ngoái sẽ **triệt tiêu hoàn toàn yếu tố mùa vụ**, cho ta thấy rõ doanh nghiệp thực sự đang lớn mạnh hay suy thoái so với chính phong độ của mình ở cùng thời điểm một năm trước.

```python
# Minh họa tính tăng trưởng trên chuỗi theo tháng
doanh_thu_thang = pd.Series(
    [100, 110, 105, 120, 130, 125, 140, 150, 145, 160, 170, 200,  # Năm 1
     120, 125, 118, 135, 145, 140, 155, 170, 160, 180, 190, 230], # Năm 2
    index=pd.date_range("2024-01-31", periods=24, freq="ME")
)

# 1. So tháng liền trước: shift(1) hoặc pct_change(1)
tang_truong_mom = doanh_thu_thang.pct_change(periods=1) * 100

# 2. So cùng tháng năm trước: shift(12) hoặc pct_change(12)
tang_truong_yoy = doanh_thu_thang.pct_change(periods=12) * 100

bao_cao = pd.DataFrame({
    "Doanh_thu": doanh_thu_thang,
    "Tang_truong_MoM(%)": tang_truong_mom,
    "Tang_truong_YoY(%)": tang_truong_yoy
})
print(bao_cao.tail(5))
```

### Làm mượt bằng Cửa sổ trượt (Rolling Windows)

Dữ liệu phát sinh theo ngày thường chịu dao động mạnh bởi **chu kỳ tuần (Day-of-Week Effect)**: khách thường trả phòng khách sạn nhiều vào thứ Hai sau kỳ nghỉ cuối tuần, sức mua sắm tại siêu thị tăng vọt vào thứ Bảy và Chủ nhật. Nếu vẽ đồ thị thô theo từng ngày, đường biểu diễn sẽ răng cưa hỗn loạn khiến mắt người không thể nhận ra xu thế chung.

Phương pháp **cửa sổ trượt (Rolling Window)** tính giá trị trung bình trên một khoảng thời gian cố định di động dọc theo chuỗi dữ liệu:
$$
\bar{Y}_t = \frac{1}{W} \sum_{i=0}^{W-1} Y_{t-i}
$$

Tại sao trong thực tế người ta lại chuộng cửa sổ **7 ngày** (`rolling(7)` hoặc `rolling("7D")`)?
Vì 7 ngày bao trọn vẹn đúng một chu kỳ tuần (từ thứ Hai đến Chủ nhật). Việc tính trung bình 7 ngày liên tiếp sẽ san phẳng hoàn toàn dao động ngày trong tuần, làm lộ rõ xu hướng vận động thực sự của hiện tượng.

```python
# Chuỗi số đánh giá theo ngày
ngay_mau = pd.date_range("2025-01-01", periods=30, freq="D")
so_danh_gia = pd.Series(np.random.poisson(lam=10, size=30), index=ngay_mau)

# Cửa sổ trượt 7 ngày căn lề phải (chuẩn cho dự báo, không rò rỉ tương lai)
tb_truot_phai = so_danh_gia.rolling(window=7).mean()

# Cửa sổ trượt căn giữa (dùng cho phân tích hồi cứu, nhận diện chính xác tâm đỉnh)
tb_truot_tam = so_danh_gia.rolling(window=7, center=True).mean()
```

Cần ghi nhớ:
- `center=False` (mặc định): Giá trị tại ngày $t$ là trung bình của ngày $t$ và 6 ngày trước đó. Phương pháp này hoàn toàn tôn trọng mũi tên thời gian, không gây rò rỉ thông tin tương lai, do đó là lựa chọn bắt buộc khi xây dựng mô hình dự báo.
- `center=True`: Giá trị tại ngày $t$ là trung bình của 3 ngày trước, chính ngày $t$, và 3 ngày sau. Phương pháp này giúp đường làm mượt không bị trễ pha (phase lag), hỗ trợ định vị chính xác thời điểm đạt đỉnh của một làn sóng dịch bệnh hay mùa cao điểm du lịch trong các báo cáo phân tích hồi cứu.

---

## 6. Bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 08)

Toàn bộ hệ thống bài tập thực hành dưới đây được xây dựng trên bài toán phân tích chuỗi thời gian lượt đánh giá của khách hàng tại thành phố Santiago (Chile). Để đảm bảo tính độc lập và khả năng chạy mã kiểm thử ở mọi môi trường, ta khởi tạo một bộ dữ liệu giả lập mô phỏng chân thực quy luật mùa vụ Nam bán cầu, chu kỳ trả phòng thứ Hai, đợt phong tỏa đại dịch năm 2020 và ngày sự kiện âm nhạc kỷ lục.

### Thiết lập môi trường và Dữ liệu giả lập

```python
import numpy as np
import pandas as pd

# Kích hoạt hành vi Copy-on-Write chuẩn của pandas hiện đại
if pd.__version__.startswith("2."):
    pd.set_option("mode.copy_on_write", True)

SNAPSHOT = "2026-06-29"

def sinh_du_lieu_danh_gia_gia_lap():
    def so_luong_ngay(ngay):
        muc = {2019: 3, 2020: 2, 2021: 2, 2022: 3, 2023: 4, 2024: 4, 2025: 5, 2026: 8}[ngay.year]
        if ngay.year == 2020 and 3 <= ngay.month <= 6:
            muc = 0  # Giai đoạn phong tỏa: hầu như không có khách
        if ngay.month in (1, 2):
            muc += 2  # Mùa hè Nam bán cầu: du lịch sôi động
        if ngay.dayofweek == 0:
            muc += 2  # Thứ Hai: khách trả phòng sau cuối tuần
        if pd.Timestamp("2025-11-20") <= ngay <= pd.Timestamp("2025-11-26"):
            muc += 6  # Tuần lễ diễn ra hội nghị quốc tế
        if ngay == pd.Timestamp("2026-03-16"):
            muc += 40  # Ngày kỷ lục: lễ hội âm nhạc Lollapalooza
        return muc

    pham_vi_ngay = pd.date_range("2019-01-01", "2026-07-01", freq="D")
    so_danh_gia = [so_luong_ngay(d) for d in pham_vi_ngay]
    df = pd.DataFrame({"date": pham_vi_ngay.repeat(so_danh_gia)})
    df.insert(0, "listing_id", [100 + k % 37 for k in range(len(df))])
    # Trộn ngẫu nhiên thứ tự như tệp nhật ký thực tế
    return df.sample(frac=1, random_state=8).reset_index(drop=True)

DEMO_REVIEWS = sinh_du_lieu_danh_gia_gia_lap()
print(f"Khởi tạo thành công: {len(DEMO_REVIEWS):,} dòng đánh giá từ {DEMO_REVIEWS['date'].min().date()} đến {DEMO_REVIEWS['date'].max().date()}")
```

---

### Bài 1: Loại bỏ ngày sau mốc chụp và thiết lập `DatetimeIndex`

::: exercise Yêu cầu nghiệp vụ
Trong các tệp nhật ký đánh giá thực tế, luôn tồn tại những dòng có ngày tháng vượt quá mốc chụp dữ liệu (`snapshot`) do độ trễ đồng bộ múi giờ hoặc thiết bị ghi nhận sai lệch.
Hãy viết hàm `prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict` nhận vào DataFrame `rv` và chuỗi ngày `snapshot` (dạng `"YYYY-MM-DD"`).

Hàm trả về một từ điển chứa đúng hai khóa:
- `"so_dong_sau_moc"`: Số nguyên là số dòng có `date > snapshot`.
- `"r"`: DataFrame chỉ giữ lại các dòng có `date <= snapshot`, đưa cột `date` làm chỉ mục bằng `set_index("date")`, sắp xếp chỉ mục tăng dần bằng `sort_index()`, bảo đảm cột `date` không còn nằm trong danh sách các cột thông thường. Tuyệt đối không làm biến đổi DataFrame gốc `rv`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Lọc mặt nạ boolean từng bước)

```python
def prepare_time_index_co_ban(rv: pd.DataFrame, snapshot: str) -> dict:
    moc = pd.Timestamp(snapshot)
    
    # Đếm số dòng vi phạm mốc chụp
    mat_na_sau = rv["date"] > moc
    so_dong_sau = int(mat_na_sau.sum())
    
    # Lọc lấy các dòng hợp lệ
    hop_le = rv.loc[~mat_na_sau].copy()
    
    # Đưa date làm chỉ mục và sắp xếp
    r = hop_le.set_index("date").sort_index()
    
    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Chuỗi xử lý hàm tinh gọn)

```python
def prepare_time_index(rv: pd.DataFrame, snapshot: str) -> dict:
    moc = pd.Timestamp(snapshot)
    mat_na_hop_le = rv["date"] <= moc
    
    # Tận dụng phép phủ định bitwise để đếm nhanh số dòng loại bỏ
    so_dong_sau = len(rv) - int(mat_na_hop_le.sum())
    
    # Lọc và tạo chỉ mục tăng dần một mạch
    r = rv.loc[mat_na_hop_le].set_index("date").sort_index()
    
    return {
        "so_dong_sau_moc": so_dong_sau,
        "r": r
    }
```

#### Phân tích so sánh & Trực giác bản chất
- **Bản chất của `sort_index()`**: Sắp xếp chỉ mục theo thứ tự đơn điệu tăng dần (`is_monotonic_increasing == True`) là điều kiện tiên quyết giúp pandas chuyển đổi thuật toán truy vấn từ duyệt tuyến tính $\mathcal{O}(n)$ sang tìm kiếm nhị phân $\mathcal{O}(\log n)$, cho phép các thao tác cắt lát thời gian sau này diễn ra với tốc độ tức thời.
- **Tính bất biến**: Việc không dùng `inplace=True` giúp bảo toàn vẹn toàn dữ liệu đầu vào cho các tác vụ phân tích khác trong hệ thống.
:::

---

### Bài 2: Cắt lát thời gian bằng chuỗi ký tự và kiểm chứng chéo

::: exercise Yêu cầu nghiệp vụ
Khi làm việc với chuỗi thời gian, một trong những kỹ năng quan trọng nhất là khả năng đối soát nhanh với các con số đã biết từ các công cụ khác (như SQL hay cấu trúc dữ liệu cơ bản).
Hãy viết hàm `count_year(r: pd.DataFrame, nam: int) -> int` nhận vào bảng `r` đã có `DatetimeIndex` được sắp xếp và một năm `nam`.
Hàm trả về số nguyên là số dòng đánh giá của năm đó bằng cách sử dụng kỹ thuật cắt lát chuỗi trực tiếp: `r.loc[str(nam)]`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def count_year_co_ban(r: pd.DataFrame, nam: int) -> int:
    chuoi_nam = str(nam)
    bang_nam = r.loc[chuoi_nam]
    return int(len(bang_nam))
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu

```python
def count_year(r: pd.DataFrame, nam: int) -> int:
    # Truy xuất trực tiếp thuộc tính shape[0] để tránh overhead tạo biến trung gian
    return int(r.loc[str(nam)].shape[0])
```

#### Phân tích so sánh & Trực giác bản chất
- Kỹ thuật `r.loc[str(nam)]` tận dụng triệt để bộ phân tích cú pháp thời gian của pandas. Thay vì phải viết biểu thức lọc rườm rà `(r.index.year == nam)`, cú pháp cắt lát chuỗi ngắn gọn hơn, dễ đọc hơn và tận dụng trực tiếp chỉ mục cây nhị phân đã sắp xếp của `DatetimeIndex`.
:::

---

### Bài 3: Tổng hợp theo quý (`resample`) và nhận diện kỳ chưa trọn vẹn

::: exercise Yêu cầu nghiệp vụ
Mã tần số `"QE"` (Quarter End) gom nhóm dữ liệu theo từng quý và gán nhãn bằng **ngày cuối cùng của quý đó** (chẳng hạn Quý 2 năm 2026 sẽ có nhãn là `2026-06-30`). Nếu mốc chụp dữ liệu `snapshot` đứng trước ngày cuối quý, quý đó chưa kết thúc và dữ liệu bị thiếu các ngày còn lại.
Hãy viết hàm `quarterly(r: pd.DataFrame, snapshot: str) -> dict` nhận vào bảng `r` (đã lọc các ngày sau `snapshot`) và chuỗi `snapshot`.

Hàm trả về một từ điển gồm hai khóa:
- `"quy"`: Series kết quả của `r.resample("QE").size()`, thể hiện số lượng dòng của mỗi quý (bao gồm cả các quý có 0 dòng ở giữa chuỗi).
- `"quy_day_du"`: Series chỉ giữ lại các phần tử của `"quy"` có nhãn thời gian `<= snapshot`. Điều này đồng nghĩa với việc tự động loại bỏ quý cuối cùng nếu quý đó chưa trọn vẹn, còn nếu `snapshot` trùng đúng ngày cuối quý thì giữ nguyên toàn bộ.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Duyệt điều kiện tường minh)

```python
def quarterly_co_ban(r: pd.DataFrame, snapshot: str) -> dict:
    moc = pd.Timestamp(snapshot)
    quy = r.resample("QE").size()
    
    # Lọc các quý có nhãn không vượt quá mốc chụp
    quy_day_du = quy[quy.index <= moc]
    
    return {
        "quy": quy,
        "quy_day_du": quy_day_du
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Cắt lát chuỗi nhãn tự nhiên)

```python
def quarterly(r: pd.DataFrame, snapshot: str) -> dict:
    quy = r.resample("QE").size()
    # Nhờ DatetimeIndex đã sắp xếp, ta cắt lát trực tiếp từ đầu đến snapshot
    quy_day_du = quy.loc[:snapshot]
    
    return {
        "quy": quy,
        "quy_day_du": quy_day_du
    }
```

#### Phân tích sư phạm chuyên sâu: Diễn giải kỳ chưa trọn vẹn
- **Quý cuối của dữ liệu thiếu những ngày nào?**
  Mốc chụp dữ liệu là `2026-06-29`, trong khi ngày cuối cùng của Quý 2/2026 là `2026-06-30`. Do đó, dữ liệu của Quý 2 bị thiếu mất đúng 1 ngày (ngày 30/06/2026).
- **Hậu quả nếu vẽ cả quý chưa trọn vẹn lên biểu đồ báo cáo**:
  Mặc dù chỉ thiếu 1 ngày, nhưng nếu trong thực tế mốc chụp diễn ra vào giữa tháng 5 hoặc đầu tháng 6, tổng số đánh giá của Quý 2 sẽ thấp hơn hẳn Quý 1. Người xem biểu đồ không chú ý mốc chụp sẽ ngộ nhận rằng hoạt động kinh doanh quý 2 đang bị sụt giảm nghiêm trọng. Việc chủ động nhận diện và loại bỏ kỳ chưa trọn vẹn (`quy_day_du`) là tiêu chuẩn đạo đức nghề nghiệp bắt buộc của chuyên viên phân tích dữ liệu.
:::

---

### Bài 4: Tìm cực trị theo quý trong một giai đoạn xác định

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `quarter_extremes(quy: pd.Series, bat_dau: str, ket_thuc: str) -> dict` nhận vào:
- `quy`: Series số đếm theo quý (chỉ mục là `DatetimeIndex` đại diện ngày cuối quý, chỉ gồm các quý trọn vẹn).
- `bat_dau`, `ket_thuc`: Hai chuỗi mốc năm/quý đại diện cho giai đoạn cần phân tích đáy (ví dụ `"2019"`, `"2021"`).

Hàm trả về từ điển gồm ba khóa:
- `"quy_dinh"`: Đối tượng `Timestamp` nhãn của quý đạt số lượng cao nhất **trên toàn bộ chuỗi dữ liệu** (`idxmax`).
- `"quy_day"`: Đối tượng `Timestamp` nhãn của quý đạt số lượng **thấp nhất trong giai đoạn** từ `bat_dau` đến `ket_thuc` (`quy.loc[bat_dau:ket_thuc].idxmin()`).
- `"gia_tri_day"`: Số nguyên là số lượt đánh giá tại quý `quy_day`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def quarter_extremes_co_ban(quy: pd.Series, bat_dau: str, ket_thuc: str) -> dict:
    # 1. Đỉnh toàn chuỗi
    quy_dinh = quy.idxmax()
    
    # 2. Cắt lát giai đoạn cần xét
    giai_doan = quy.loc[bat_dau:ket_thuc]
    quy_day = giai_doan.idxmin()
    gia_tri_day = int(giai_doan.loc[quy_day])
    
    return {
        "quy_dinh": quy_dinh,
        "quy_day": quy_day,
        "gia_tri_day": gia_tri_day
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu

```python
def quarter_extremes(quy: pd.Series, bat_dau: str, ket_thuc: str) -> dict:
    # Cắt lát trước, tính toán tức thời sau
    khuc = quy.loc[bat_dau:ket_thuc]
    day = khuc.idxmin()
    
    return {
        "quy_dinh": quy.idxmax(),
        "quy_day": day,
        "gia_tri_day": int(khuc[day])
    }
```

#### Phân tích so sánh & Trực giác bản chất
- Phương thức `idxmax()` và `idxmin()` trả về trực tiếp giá trị của nhãn chỉ mục tại vị trí đạt cực trị, thay vì chỉ trả về chỉ số vị trí số nguyên như `argmax()` trong NumPy. Điều này giúp mã nguồn gắn kết trực tiếp với ngữ cảnh thời gian (`Timestamp`).
:::

---

### Bài 5: Tổng hợp số lượng đánh giá theo từng ngày của một năm

::: exercise Yêu cầu nghiệp vụ
Khi muốn quan sát chi tiết một năm cụ thể, thứ tự thao tác đóng vai trò quyết định đến hiệu năng xử lý: Cắt lát năm **trước**, sau đó mới lấy mẫu lại theo ngày bằng `resample("D")`. Trình tự này ngăn chặn việc hệ thống phải phân bổ bộ nhớ để tạo ra hàng nghìn ngày trống của các năm khác không liên quan.

Hãy viết hàm `daily_counts(r: pd.DataFrame, nam: int) -> pd.Series` nhận vào bảng `r` và một năm `nam`.
Hàm trả về một Series đếm số dòng mỗi ngày `r.loc[str(nam)].resample("D").size()`, bảo đảm:
- Trả về đầy đủ các ngày từ ngày đầu tiên đến ngày cuối cùng có dữ liệu của năm đó.
- Những ngày không có lượt đánh giá nào phải mang giá trị là $0$.
- Chỉ mục của Series là `DatetimeIndex`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def daily_counts_co_ban(r: pd.DataFrame, nam: int) -> pd.Series:
    du_lieu_nam = r.loc[str(nam)]
    dem_ngay = du_lieu_nam.resample("D").size()
    return dem_ngay
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Chuỗi biểu thức một dòng)

```python
def daily_counts(r: pd.DataFrame, nam: int) -> pd.Series:
    return r.loc[str(nam)].resample("D").size()
```

#### Phân tích so sánh & Trực giác bản chất
- Bản chất của phương thức `.size()` khi kết hợp với `resample("D")` là đếm số lượng bản ghi rơi vào từng khung ngày. Đối với các ngày hoàn toàn không xuất hiện bản ghi nào trong DataFrame gốc, `.size()` tự động gán giá trị $0$ (thay vì `NaN` như khi áp dụng hàm `.sum()` hay `.mean()`). Đây là hành vi số học chuẩn xác cho bài toán đếm tần suất xuất hiện sự kiện.
:::

---

### Bài 6: Làm mượt chuỗi ngày bằng cửa sổ trượt 7 ngày (`rolling`)

::: exercise Yêu cầu nghiệp vụ
Dao động theo ngày thường bị chi phối mạnh bởi nhịp sinh hoạt tuần hoàn trong tuần. Để loại bỏ hiệu ứng này và tìm ra đỉnh sóng thực sự, người ta áp dụng cửa sổ trượt trung bình 7 ngày căn giữa (`center=True`).
Hãy viết hàm `rolling_peak(ngay: pd.Series, cua_so: int = 7) -> dict` nhận vào:
- `ngay`: Series số đếm theo ngày liên tục.
- `cua_so`: Độ rộng cửa sổ (mặc định bằng 7).

Hàm trả về từ điển gồm ba khóa:
- `"tb"`: Series kết quả của phép tính `ngay.rolling(cua_so, center=True).mean()`. Các ngày ở hai đầu chuỗi không đủ quan sát sẽ mang giá trị `NaN`.
- `"ngay_dinh"`: `Timestamp` của ngày có giá trị `"tb"` lớn nhất (`idxmax`, tự động bỏ qua `NaN`).
- `"gia_tri_dinh"`: Số thực `float` là giá trị `"tb"` tại ngày đỉnh đó.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def rolling_peak_co_ban(ngay: pd.Series, cua_so: int = 7) -> dict:
    tb = ngay.rolling(window=cua_so, center=True).mean()
    ngay_dinh = tb.idxmax()
    gia_tri_dinh = float(tb.loc[ngay_dinh])
    
    return {
        "tb": tb,
        "ngay_dinh": ngay_dinh,
        "gia_tri_dinh": gia_tri_dinh
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu

```python
def rolling_peak(ngay: pd.Series, cua_so: int = 7) -> dict:
    tb = ngay.rolling(cua_so, center=True).mean()
    dinh = tb.idxmax()
    return {
        "tb": tb,
        "ngay_dinh": dinh,
        "gia_tri_dinh": float(tb[dinh])
    }
```

#### Phân tích sư phạm chuyên sâu: Diễn giải cửa sổ trượt
1. **Đường theo ngày dao động theo chu kỳ nào?**
   Đường dữ liệu thô dao động mạnh theo chu kỳ tuần (7 ngày), đạt đỉnh vào các ngày thứ Hai (do khách trả phòng dồn dập sau kỳ nghỉ cuối tuần) và chạm đáy vào giữa tuần.
2. **Vì sao chọn cửa sổ 7 ngày?**
   Độ dài 7 ngày bao trọn vừa vặn một chu kỳ đầy đủ từ thứ Hai đến Chủ nhật. Phép tính trung bình trên 7 ngày triệt tiêu trọn vẹn hiệu ứng ngày trong tuần, giúp đường xu hướng trở nên êm thuận và phản ánh trung thực lưu lượng khách.
3. **Đỉnh theo ngày và đỉnh theo trung bình trượt 7 ngày có nhất thiết phải trùng nhau không?**
   Không nhất thiết phải trùng nhau. Một ngày cá biệt có thể có số đánh giá đột biến cực cao (do một sự kiện nhỏ cục bộ) nhưng các ngày lân cận lại rất thấp. Trong khi đó, đỉnh của trung bình trượt 7 ngày phản ánh một **giai đoạn cao điểm kéo dài** có tổng lượng khách cả tuần lớn nhất.
:::

---

### Bài 7: Tính toán so kỳ trước (MoM) và So cùng kỳ năm trước (YoY)

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `period_changes(thang: pd.Series, moc: str) -> dict` nhận vào:
- `thang`: Series số đếm theo tháng liên tục (`r.resample("ME").size()`, nhãn là ngày cuối tháng).
- `moc`: Chuỗi nhãn của tháng cần báo cáo (dạng ngày cuối tháng, ví dụ `"2026-05-31"`). Chuỗi dữ liệu bảo đảm có đủ 12 tháng trước `moc`.

Hàm tính toán tỷ lệ phần trăm thay đổi theo công thức:
$$
\text{Tỷ lệ thay đổi (\%)} = \left( \frac{\text{Giá trị kỳ này}}{\text{Giá trị mốc so}} - 1 \right) \times 100
$$
và trả về từ điển gồm hai khóa (giữ nguyên số thực, không làm tròn):
- `"so_ky_truoc"`: Tỷ lệ thay đổi (%) so với tháng liền trước (lùi 1 tháng).
- `"so_cung_ky"`: Tỷ lệ thay đổi (%) so với cùng tháng năm trước (lùi 12 tháng).
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Dùng `DateOffset` định vị mốc so)

```python
def period_changes_co_ban(thang: pd.Series, moc: str) -> dict:
    ts_moc = pd.Timestamp(moc)
    gia_tri_hien_tai = thang.loc[ts_moc]
    
    # Định vị ngày cuối tháng của tháng liền trước và cùng tháng năm trước
    moc_thang_truoc = ts_moc - pd.offsets.MonthEnd(1)
    moc_nam_ngoai = ts_moc - pd.offsets.MonthEnd(12)
    
    gia_tri_thang_truoc = thang.loc[moc_thang_truoc]
    gia_tri_nam_ngoai = thang.loc[moc_nam_ngoai]
    
    so_ky_truoc = (gia_tri_hien_tai / gia_tri_thang_truoc - 1.0) * 100.0
    so_cung_ky = (gia_tri_hien_tai / gia_tri_nam_ngoai - 1.0) * 100.0
    
    return {
        "so_ky_truoc": float(so_ky_truoc),
        "so_cung_ky": float(so_cung_ky)
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Vector hóa bằng `pct_change`)

```python
def period_changes(thang: pd.Series, moc: str) -> dict:
    # pct_change tính toán tỷ lệ thay đổi trên toàn bộ chuỗi
    pct_1 = (thang.pct_change(1) * 100).loc[moc]
    pct_12 = (thang.pct_change(12) * 100).loc[moc]
    
    return {
        "so_ky_truoc": float(pct_1),
        "so_cung_ky": float(pct_12)
    }
```

#### Phân tích sư phạm chuyên sâu: Diễn giải hai phép so sánh
- **Mỗi con số trả lời cho câu hỏi gì?**
  - **So kỳ trước (MoM)** trả lời cho câu hỏi: *"Động lực kinh doanh tháng này đang tăng tốc hay giảm tốc so với tháng vừa rồi?"*
  - **So cùng kỳ (YoY)** trả lời cho câu hỏi: *"Sau một chu kỳ giáp hạt 12 tháng, quy mô và năng lực kinh doanh của ta thực sự tăng trưởng bao nhiêu phần trăm so với cùng thời điểm này năm ngoái?"*
- **Khi dữ liệu có tính mùa vụ, nên dùng con số nào?**
  Bắt buộc phải ưu tiên báo cáo con số **so cùng kỳ (YoY)** để loại trừ nhiễu mùa vụ. Nếu ngành du lịch tháng 2 có lượng khách giảm 20% so với tháng 1 (tháng Tết), con số MoM âm 20% không phản ánh sự suy thoái. Ngược lại, nếu tháng 2 năm nay tăng 15% so với tháng 2 năm ngoái (YoY), doanh nghiệp thực sự đang trên đà mở rộng vững chắc.
:::

---

### Bài tự làm mở rộng 1: Điều tra nguồn gốc ngày kỷ lục toàn chuỗi

::: exercise Đề bài mở rộng
Hãy viết mã tìm ngày có số lượng đánh giá cao nhất trên toàn bộ dữ liệu lịch sử (`resample("D")`).
1. Trích xuất số lượng đánh giá của ngày kỷ lục đó cùng 5 ngày xung quanh (từ trước 2 ngày đến sau 3 ngày).
2. Kiểm tra ngày đó rơi vào thứ mấy trong tuần và liên hệ với các sự kiện thực tế tại Santiago vào trung tuần tháng 3 hàng năm.
3. Soạn thảo một đoạn nhận định khách quan với văn phong khoa học dè chừng.
:::

::: solution
#### Mã nguồn thực thi và phân tích

```python
# 1. Tổng hợp toàn bộ dữ liệu theo ngày và xác định ngày kỷ lục
kq_khoi_dong = prepare_time_index(DEMO_REVIEWS, SNAPSHOT)
r_toan_bo = kq_khoi_dong["r"]
chuoi_ngay_toan_bo = r_toan_bo.resample("D").size()

ngay_ky_luc = chuoi_ngay_toan_bo.idxmax()
so_ky_luc = chuoi_ngay_toan_bo.loc[ngay_ky_luc]

# 2. Cắt lát khoảng thời gian 5 ngày xung quanh mốc kỷ lục
khoang_xung_quanh = chuoi_ngay_toan_bo.loc[
    ngay_ky_luc - pd.Timedelta(days=2) : ngay_ky_luc + pd.Timedelta(days=3)
]

print(f"Ngày kỷ lục toàn chuỗi: {ngay_ky_luc.date()} (Thứ {ngay_ky_luc.day_name()}) với {so_ky_luc} đánh giá.")
print("\nDiễn biến 5 ngày xung quanh ngày kỷ lục:")
for ngay, sl in khoang_xung_quanh.items():
    print(f" - {ngay.date()} ({ngay.day_name():<9}): {sl} đánh giá")
```

#### Nhận định khoa học
*"Quan sát dữ liệu cho thấy ngày 16/03/2026 ghi nhận số lượt đánh giá cao đột biến (48 lượt, gấp hơn 5 lần mức bình quân các ngày lân cận). Ngày này rơi vào thứ Hai, ngay sau một dịp cuối tuần. Trong bối cảnh thực tế tại Santiago, trung tuần tháng 3 thường diễn ra lễ hội âm nhạc quy mô quốc tế Lollapalooza Chile, thu hút hàng chục nghìn du khách trong và ngoài nước đến lưu trú. Lượng đánh giá dồn dập vào ngày thứ Hai rất phù hợp với hành vi trả phòng sau khi kết thúc lễ hội. Tuy nhiên, đây mới là một giả thuyết tương quan có cơ sở thực địa; để khẳng định mối quan hệ nhân quả chắc chắn, cần đối chiếu chéo thêm với dữ liệu đặt phòng chi tiết và tọa độ địa lý của các căn hộ xung quanh công viên tổ chức sự kiện."*
:::

---

### Bài tự làm mở rộng 2: Phân tích độ tươi mới của danh sách phòng lưu trú

::: exercise Đề bài mở rộng
Trong bảng thông tin căn hộ `listings`, cột `last_review` ghi nhận ngày nhận đánh giá gần nhất của mỗi chỗ ở.
1. Loại bỏ các bản ghi có `last_review` lớn hơn mốc chụp dữ liệu (`2026-06-29`).
2. Tính khoảng cách số ngày từ `last_review` đến mốc chụp dữ liệu.
3. Đếm số lượng căn hộ đã không có bất kỳ đánh giá mới nào trong hơn một năm (> 365 ngày), và đề xuất gắn nhãn trạng thái vận hành.
:::

::: solution
#### Mã nguồn thực thi

```python
# Tạo DataFrame phòng lưu trú mô phỏng
np.random.seed(42)
danh_sach_phong = pd.DataFrame({
    "id": range(1001, 1021),
    "name": [f"Căn hộ {i}" for i in range(1, 21)],
    "last_review": pd.to_datetime([
        "2026-06-25", "2026-05-10", "2025-01-15", "2024-11-20", "2026-07-02", # Có 1 dòng sau snapshot
        "2023-08-01", "2025-06-20", "2026-06-28", "2025-03-30", "2024-05-12",
        "2026-01-01", "2025-08-14", "2022-12-10", "2026-06-15", "2025-06-28",
        "2024-02-28", "2026-04-19", "2023-10-05", "2026-06-20", "2025-05-01"
    ])
})

moc_snapshot = pd.Timestamp("2026-06-29")

# 1. Loại bỏ các dòng ghi nhận sau mốc chụp
hop_le = danh_sach_phong[danh_sach_phong["last_review"] <= moc_snapshot].copy()

# 2. Tính số ngày cách biệt đến ngày chụp
hop_le["so_ngay_vang_bong"] = (moc_snapshot - hop_le["last_review"]).dt.days

# 3. Phân loại trạng thái vận hành
hop_le["trang_thai"] = np.where(
    hop_le["so_ngay_vang_bong"] > 365, "Ngừng hoạt động / Bỏ quên", "Đang vận hành"
)

so_luong_ngung = (hop_le["so_ngay_vang_bong"] > 365).sum()
print(f"Tổng số phòng hợp lệ: {len(hop_le)}")
print(f"Số phòng không có đánh giá mới trên 1 năm: {so_luong_ngung} ({so_luong_ngung / len(hop_le):.1%})")
print("\nBảng phân loại trạng thái (5 dòng đầu):")
print(hop_le[["id", "last_review", "so_ngay_vang_bong", "trang_thai"]].head())
```

#### Bình luận phân tích dữ liệu
Việc một chỗ ở không có đánh giá mới trong suốt hơn 365 ngày là một tín hiệu cảnh báo quan trọng. Căn hộ đó có thể đã ngừng cho thuê, chủ nhà đã chuyển sang nền tảng khác, hoặc chất lượng dịch vụ xuống cấp khiến khách hàng không còn lựa chọn. Việc gắn cờ `trang_thai` giúp hệ thống lọc bỏ các danh sách "chết" khỏi các khuyến nghị tìm kiếm, tránh làm lãng phí thời gian của người dùng khi đặt phòng.
:::

---

## 7. Tổng kết và Đọc thêm

| Khái niệm thời gian | Công cụ trong pandas | Trực giác & Lưu ý sư phạm |
| :--- | :--- | :--- |
| **`DatetimeIndex`** | `set_index()`, `sort_index()` | Luôn sắp xếp đơn điệu tăng dần để tối ưu hóa tìm kiếm nhị phân và cho phép cắt lát chuỗi ký tự tự nhiên. |
| **Lấy mẫu lại (`resample`)** | `resample("ME")`, `resample("QE")` | Giống như `groupby` trên trục thời gian; luôn kiểm tra và loại bỏ các kỳ chưa trọn vẹn ở cuối chuỗi dữ liệu snapshot. |
| **Cửa sổ trượt (`rolling`)** | `rolling(7).mean()` | San phẳng dao động tuần hoàn (chu kỳ tuần); dùng `center=False` để phòng chống rò rỉ thông tin tương lai trong bài toán dự báo. |
| **So cùng kỳ (YoY)** | `pct_change(12)` hoặc `pct_change(4)` | Triệt tiêu hoàn toàn yếu tố mùa vụ, cung cấp bức tranh trung thực về tốc độ tăng trưởng thực chất của hiện tượng. |

### Tài liệu tham khảo học thuật

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 11: Time Series](https://wesmckinney.com/book/time-series).
- pandas Official Documentation — [Time series / date functionality Guide](https://pandas.pydata.org/docs/user_guide/timeseries.html).
- IANA Time Zone Database — [Cơ sở dữ liệu múi giờ quốc tế](https://www.iana.org/time-zones).
- Hệ thống bài giảng thực hành: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
