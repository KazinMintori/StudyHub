---
course: xu-ly-du-lieu
lecture: bai-08-du-lieu-thoi-gian
section: lecture
title: "Xử lý dữ liệu thời gian"
prerequisites: ["chi-muc", "gia-tri-thieu"]
lessonStatus: ready
description: "Làm chủ chuỗi thời gian trong pandas: DatetimeIndex, cắt lát chuỗi, lấy mẫu lại resample, cửa sổ trượt rolling và so sánh cùng kỳ YoY vs MoM."
---

Thời gian không phải là một chuỗi văn bản thông thường, và càng không phải là một con số vô hướng đơn thuần. Trong tự nhiên cũng như trong phân tích dữ liệu, thời gian sở hữu một đặc tính cốt lõi: **Mũi tên một chiều (Arrow of Time)**. Mọi sự kiện diễn ra trong quá khứ định hình trạng thái hiện tại, trong khi tương lai là miền bất định và tuyệt đối không bao giờ được phép rò rỉ ngược về quá khứ trong các quy trình huấn luyện mô hình dự báo.

Hơn thế nữa, dữ liệu thời gian mang bản chất bất đối xứng của các quy ước xã hội và thiên văn học: Năm nhuận có 366 ngày, số ngày giữa các tháng chênh lệch nhau, các hệ thống phân tán đặt tại nhiều múi giờ khác nhau, và quy ước đổi giờ mùa hè (Daylight Saving Time) có thể làm dòng thời gian nhảy cóc một tiếng hoặc lặp lại một tiếng. Nếu xử lý cẩu thả bằng cách ghép chuỗi hay chia số nguyên đơn thuần, toàn bộ các chỉ số thống kê và báo cáo tài chính sẽ bị méo mó nghiêm trọng.

Bài giảng này trình bày bài bản cách làm chủ dữ liệu chuỗi thời gian (Time Series) trong Python và pandas: Từ việc phân biệt ba phạm trù thời gian, kỹ thuật quản trị múi giờ chuẩn mực, các phép cắt lát chuỗi trực quan trên `DatetimeIndex`, đến kỹ thuật lấy mẫu lại (`resample`), làm mượt dao động bằng cửa sổ trượt (`rolling`), và phương pháp tính toán so sánh cùng kỳ khoa học.

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

Cơ chế này hoạt động đạt hiệu năng cao nhờ thuật toán tìm kiếm nhị phân trên chỉ mục đơn điệu tăng dần (`is_monotonic_increasing`). Nếu chỉ mục chưa được sắp xếp, thao tác cắt lát chuỗi có thể trả về kết quả sai hoặc ném ra cảnh báo nghiêm trọng.

---

## 4. Lấy mẫu lại (Resampling): Tần số, Biên đóng mở và Bẫy kỳ dang dở

Trong thực tế, các sự kiện trong đời sống diễn ra ở các nhịp độ ngẫu nhiên: Có ngày có hàng trăm lượt đánh giá của khách hàng, có ngày không có lượt nào. Để phát hiện quy luật kinh doanh, ta cần tổng hợp dữ liệu về các thang đo định kỳ đều đặn (theo ngày, tuần, tháng, quý hoặc năm). Quá trình này được gọi là **lấy mẫu lại (Resampling)**.

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

Dữ liệu phát sinh theo ngày thường chịu dao động mạnh bởi **chu kỳ tuần (Day-of-Week Effect)**: Khách thường trả phòng khách sạn nhiều vào thứ Hai sau kỳ nghỉ cuối tuần, sức mua sắm tại siêu thị tăng vọt vào thứ Bảy và Chủ nhật. Nếu vẽ đồ thị thô theo từng ngày, đường biểu diễn sẽ răng cưa hỗn loạn khiến mắt người không thể nhận ra xu thế chung.

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

## 6. Bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 08) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 7. Tổng kết và Đọc thêm

| Khái niệm thời gian | Công cụ trong pandas | Trực giác & Lưu ý sư phạm |
| :--- | :--- | :--- |
| **`DatetimeIndex`** | `set_index()`, `sort_index()` | Luôn sắp xếp đơn điệu tăng dần để tối ưu hóa tìm kiếm nhị phân và cho phép cắt lát chuỗi ký tự tự nhiên. |
| **Lấy mẫu lại (`resample`)** | `resample("ME")`, `resample("QE")` | Giống như `groupby` trên trục thời gian; luôn kiểm tra và loại bỏ các kỳ chưa trọn vẹn ở cuối chuỗi dữ liệu snapshot. |
| **Cửa sổ trượt (`rolling`)** | `rolling(7).mean()` | San phẳng dao động tuần hoàn (chu kỳ tuần); dùng `center=False` để phòng chống rò rỉ thông tin tương lai trong bài toán dự báo. |
| **So cùng kỳ (YoY)** | `pct_change(12)` hoặc `pct_change(4)` | Triệt tiêu hoàn toàn yếu tố mùa vụ, cung cấp bức tranh trung thực về tốc độ tăng trưởng thực chất của hiện tượng. |

### Tài liệu tham khảo học thuật

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 11: Time Series](https://wesmckinney.com/book/time-series).
- Tài liệu chính thức pandas: [Time series / date functionality Guide](https://pandas.pydata.org/docs/user_guide/timeseries.html).
- IANA Time Zone Database: [Cơ sở dữ liệu múi giờ quốc tế](https://www.iana.org/time-zones).
- Hệ thống bài giảng thực hành: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
