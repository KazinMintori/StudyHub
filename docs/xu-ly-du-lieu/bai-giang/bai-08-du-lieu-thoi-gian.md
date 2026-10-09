---
course: xu-ly-du-lieu
lecture: bai-08-du-lieu-thoi-gian
section: lecture
title: "Xử lý dữ liệu thời gian"
prerequisites: ["chi-muc","gia-tri-thieu","ky-vong"]
lessonStatus: ready
description: "Đọc ngày giờ với định dạng và múi giờ rõ ràng; lấy mẫu lại, dịch chuỗi và tính cửa sổ trượt."
---

Thời gian không phải là một chuỗi văn bản thông thường, cũng không phải là một đại lượng vô hướng đơn giản. Trong vật lý và trong khoa học dữ liệu, thời gian có một thuộc tính đặc biệt: **mũi tên một chiều (Arrow of Time)**. Mọi biến cố trong quá khứ định hình trạng thái hiện tại, còn tương lai là điều chưa xảy ra và tuyệt đối không bao giờ được phép rò rỉ ngược về quá khứ trong các mô hình dự báo.

Hơn thế nữa, dữ liệu thời gian mang trong mình đầy rẫy sự bất đối xứng: năm nhuận có 366 ngày, các tháng có số ngày chênh lệch nhau, các hệ thống trên thế giới hoạt động ở các múi giờ khác nhau, và nhiều quốc gia còn áp dụng quy ước giờ mùa hè (Daylight Saving Time) làm thời gian bị nhảy cóc hoặc lặp lại.

Bài học này làm rõ cách tiếp cận khoa học để làm chủ dữ liệu chuỗi thời gian (Time Series) trong pandas: phân biệt ba phạm trù thời gian, kỹ thuật quản trị múi giờ chuẩn xác, quy tắc lấy mẫu lại không làm méo mó bản chất, và kỹ thuật cửa sổ trượt phòng chống rò rỉ dữ liệu tương lai.

## 1. Ba phạm trù cốt lõi: Điểm thời gian, Khoảng biến thiên và Kỳ hạn

Để làm việc mạch lạc, ta phải phân biệt rõ ba khái niệm thời gian hoàn toàn khác nhau trong toán học và đời sống:

1. **Điểm thời gian (Timestamp)**: Đại diện cho một khoảnh khắc cố định duy nhất trên dòng thời gian (ví dụ: đúng 09:00:00 ngày 01 tháng 02 năm 2026). Trong pandas, kiểu tương ứng là `pd.Timestamp`.
2. **Khoảng biến thiên (Timedelta)**: Đại diện cho độ dài của một khoảng cách thời gian giữa hai biến cố (ví dụ: khoảng cách 48 giờ hoặc 2 ngày). Kiểu tương ứng là `pd.Timedelta`.
3. **Kỳ hạn (Period)**: Đại diện cho một khoảng thời gian hữu hạn gắn liền với lịch thiên văn hay lịch kinh doanh (ví dụ: trọn vẹn tháng 02 năm 2026, hoặc Quý 1 năm 2026). Một thời điểm thuộc tháng 2 không đồng nghĩa với toàn bộ tháng 2.

```python
import pandas as pd

raw = pd.Series(["01/02/2026", "03/02/2026", "31/02/2026"])
dates = pd.to_datetime(raw, format="%d/%m/%Y", errors="coerce")
print(dates.dt.strftime("%Y-%m-%d").tolist())
print(dates.isna().tolist())     # [False, False, True]
print((dates.iloc[1] - dates.iloc[0]).days)  # 2
```

Ba bài học kỹ thuật quan trọng từ ví dụ trên:

- **Khóa định dạng bằng `format`**: Chuỗi `"01/02/2026"` đối với người Việt Nam là ngày 1 tháng 2, nhưng đối với người Mỹ lại là ngày 2 tháng 1. Nếu không khai báo tham số `format="%d/%m/%Y"`, pandas sẽ phải tự đoán mò và rất dễ hoán đổi ngày thành tháng khi ngày nhỏ hơn 12.
- **Nhận diện ngày phi lý với `errors="coerce"`**: Tháng 2 không bao giờ có ngày 31. Khi gặp chuỗi phi lý `"31/02/2026"`, tham số `errors="coerce"` giúp chuyển đổi giá trị lỗi này thành **`NaT`** (viết tắt của *Not a Time* - dấu hiệu khuyết thiếu chuyên biệt cho dữ liệu thời gian) mà không làm sập toàn bộ quy trình nạp dữ liệu.
- **Số học thời gian tự nhiên**: Lấy thời điểm ngày 03/02 trừ đi ngày 01/02 sinh ra một đối tượng `Timedelta`, từ đó ta truy xuất thuộc tính `.days` để nhận giá trị số nguyên 2 ngày một cách chính xác.

## 2. Quản trị múi giờ: Bản chất của Localize và Convert

Một trong những thảm họa phổ biến nhất của các hệ thống đa quốc gia là dữ liệu từ chi nhánh Tokyo, chi nhánh Hà Nội và chi nhánh London bị lưu chung mà không ghi rõ múi giờ.

Trong pandas, ta cần phân biệt rạch ròi giữa hai trạng thái:
- **Thời gian ngây thơ (Timezone-naive)**: Dữ liệu chỉ ghi giờ số học đơn thuần, không mang bất kỳ thông tin nào về múi giờ.
- **Thời gian có nhận thức (Timezone-aware)**: Dữ liệu gắn liền với một múi giờ cụ thể theo cơ sở dữ liệu quốc tế IANA.

```python
local = pd.DatetimeIndex(["2026-02-01 07:00"]).tz_localize("Asia/Ho_Chi_Minh")
utc = local.tz_convert("UTC")
print(utc[0].isoformat())        # 2026-02-01T00:00:00+00:00
```

Hai thao tác mang ý nghĩa hoàn toàn khác biệt:

1. **`tz_localize("Asia/Ho_Chi_Minh")`**: Phép gán nhãn nhận thức. Ta khẳng định rằng con số `07:00` trong tệp dữ liệu gốc được quan sát tại múi giờ Việt Nam (UTC+7). Phép toán này **không thay đổi con số hiển thị**, mà chỉ bổ sung thêm ngữ cảnh độ lệch giờ.
2. **`tz_convert("UTC")`**: Phép chuyển đổi tọa độ. Sau khi đã biết chắc đó là 7 giờ sáng ở Việt Nam, ta chuyển đổi sang giờ phối hợp quốc tế UTC. Lúc này, con số hiển thị được lùi về đúng `00:00:00` cùng ngày.

Nếu nguồn dữ liệu là giờ địa phương Việt Nam nhưng bạn lại gọi ngay `pd.to_datetime(..., utc=True)`, pandas sẽ ngây thơ coi 7 giờ sáng ở Việt Nam chính là 7 giờ sáng giờ UTC, làm sai lệch đồng hồ của toàn bộ hệ thống đi 7 tiếng!

Đối với các quốc gia áp dụng quy ước giờ mùa hè (DST), có những thời điểm đồng hồ bị vặn tiến 1 tiếng (khiến một giờ bị biến mất khỏi dòng thời gian) hoặc vặn lùi 1 tiếng (khiến một giờ xuất hiện hai lần). Khi gặp dữ liệu này, tham số `ambiguous` và `nonexistent` của hàm `tz_localize` cho phép ta cấu hình cách xử lý minh bạch thay vì để hệ thống tự suy diễn.

## 3. Lấy mẫu lại (Resampling) và khoảng trống dữ liệu

Trong thực tế, các sự kiện phát sinh không đều đặn: có giờ bán được 10 đơn, có giờ không bán được đơn nào. Để phân tích xu hướng, ta cần đưa dữ liệu về các khoảng thời gian đều đặn (hàng ngày, hàng tuần, hàng tháng).

```python
s = pd.Series(
    [10.0, 30.0, 20.0],
    index=pd.to_datetime(["2026-02-01 09:00", "2026-02-01 15:00", "2026-02-03 09:00"]),
).sort_index()
print(s.loc["2026-02-01"].sum())  # 40.0
daily = s.resample("D", closed="left", label="left").sum(min_count=1)
print(daily.tolist())            # [40.0, nan, 20.0]
```

Phương thức **`resample("D")`** hoạt động như một phép `groupby` chuyên dụng trên trục thời gian. Hai tham số cần lưu tâm:
- **`closed="left"`**: Quy ước khoảng thời gian nửa mở $[00:00, 24:00)$, nhận biên bên trái và loại trừ mốc biên bên phải.
- **`label="left"`**: Đặt nhãn của ngày là mốc bắt đầu của khoảng thời gian đó.

Hãy nhìn vào kết quả mảng `daily`:
- Ngày 01/02: Có hai giao dịch lúc 9h và 15h, tổng doanh thu là $10 + 30 = 40.0$.
- Ngày 02/02: Hoàn toàn không có giao dịch nào xuất hiện.
- Ngày 03/02: Có một giao dịch lúc 9h, tổng doanh thu là $20.0$.

Tại ngày 02/02, việc sử dụng tham số **`min_count=1`** đã giữ nguyên giá trị là `NaN` (khuyết thiếu) thay vì tự động điền số $0$. Đây là một quyết định học thuật quan trọng:
- Nếu ta biết chắc chắn rằng cửa hàng mở cửa cả ngày và thiết bị ghi nhận hoạt động hoàn hảo, việc không có giao dịch thực sự đồng nghĩa với doanh thu bằng 0.
- Nhưng nếu ngày hôm đó cửa hàng bị mất điện, hỏng máy quét thẻ, hoặc đường truyền mạng bị ngắt, việc tự ý điền số 0 sẽ làm méo mó nghiêm trọng phân tích hiệu quả kinh doanh. Giữ nguyên `NaN` nhắc nhở nhà phân tích phải điều tra nguyên nhân của khoảng trống dữ liệu trước khi kết luận.

## 4. Dịch chuyển chuỗi và Cửa sổ trượt phòng chống rò rỉ dữ liệu

Hai phép toán động học phổ biến nhất trên chuỗi thời gian là tính tốc độ thay đổi và làm mượt dao động:

```python
day = pd.Series([10.0, 20.0, 30.0], index=pd.date_range("2026-02-01", periods=3))
previous = day.shift(1)
delta = day - previous
moving = day.rolling(window=2, min_periods=2).mean()
print(delta.tolist())            # [nan, 10.0, 10.0]
print(moving.tolist())           # [nan, 15.0, 25.0]
print(day.to_period("M").index[0])  # 2026-02
```

1. **Dịch chuyển chuỗi với `shift(1)`**: Đẩy toàn bộ các giá trị tiến về phía trước một bước thời gian. Tại ngày 02/02 (giá trị 20), biến `previous` giữ giá trị của ngày hôm trước (giá trị 10). Mức tăng trưởng $\Delta = 20 - 10 = 10.0$. Tại ngày đầu tiên, do không có dữ liệu của quá khứ, kết quả đương nhiên là `NaN`.
2. **Cửa sổ trượt với `rolling(window=2, min_periods=2)`**: Tính toán thống kê trên một khoảng quan sát di động. Tại bước thứ hai, cửa sổ bao gồm 2 ngày [10, 20], trung bình là 15.0. Tại bước thứ ba, cửa sổ trượt sang [20, 30], trung bình là 25.0.

Cạm bẫy sống còn trong chuỗi thời gian: **Rò rỉ dữ liệu tương lai (Data Leakage)**.
Khi xây dựng các mô hình dự báo học máy hoặc chỉ số giao dịch tài chính, bạn chỉ được phép sử dụng những dữ liệu đã xuất hiện **trước hoặc tại thời điểm dự báo**. Nếu bạn sử dụng phép dịch chuyển ngược `shift(-1)` hoặc cửa sổ trượt căn giữa (`rolling(..., center=True)`), bạn đang vô tình lấy dữ liệu của ngày mai để tính toán cho ngày hôm nay. Mô hình của bạn trên tập kiểm thử sẽ đạt độ chính xác ảo tưởng 99%, nhưng khi đưa vào thực tế sẽ thất bại thảm hại vì không ai biết trước tương lai.

## 5. Bài tập tự luyện

::: exercise Phân biệt quy trình bản địa hóa và chuyển đổi múi giờ
Một máy chủ đặt tại Hà Nội ghi nhận dòng nhật ký giao dịch vào lúc `"2026-02-01 07:00"`. Hãy trình bày chuỗi câu lệnh pandas để chuyển đổi mốc thời gian này về giờ chuẩn UTC, và giải thích vì sao không được dùng `utc=True` trực tiếp.
:::

::: solution
Chuỗi câu lệnh chuẩn xác là:
```python
ts = pd.to_datetime("2026-02-01 07:00")
ts_vn = ts.tz_localize("Asia/Ho_Chi_Minh")
ts_utc = ts_vn.tz_convert("UTC")
```
Kết quả thu được là `2026-02-01 00:00:00+00:00`.

Nếu truyền `utc=True` trực tiếp vào hàm `pd.to_datetime("2026-02-01 07:00", utc=True)`, pandas sẽ hiểu lầm rằng chuỗi văn bản gốc vốn dĩ là giờ UTC. Khi đó mốc thời gian được hiểu là 7 giờ sáng giờ UTC (tương đương 14 giờ chiều tại Việt Nam), làm sai lệch toàn bộ thời điểm phát sinh sự kiện đi 7 tiếng đồng hồ.
:::

::: exercise Phân tích bản chất ngày khuyết thiếu khi Resample
Trong ví dụ ở mục 3, tại sao ngày 02/02 lại nhận giá trị `NaN` thay vì số 0? Trong tình huống thực tế nào việc điền số 0 vào ngày này sẽ dẫn đến kết luận phân tích sai lệch?
:::

::: solution
Ngày 02/02 nhận giá trị `NaN` vì trong ngày đó không có bất kỳ dòng dữ liệu nào phát sinh, và tham số `min_count=1` đòi hỏi phải có ít nhất một giá trị hợp lệ mới thực hiện phép tính tổng.

Nếu ngày 02/02 là ngày hệ thống ghi nhận dữ liệu bị sập máy chủ hoặc mất điện, việc tự động điền số 0 sẽ khiến báo cáo ghi nhận rằng ngày hôm đó doanh số bằng 0. Khi tính doanh thu trung bình hàng ngày trong tháng, việc chèn thêm các ngày 0 đồng giả tạo này sẽ kéo tụt hiệu suất bán hàng bình quân của cửa hàng xuống một cách sai lầm.
:::

::: exercise Tính toán cửa sổ trượt trên dữ liệu thực tế
Cho chuỗi doanh thu 3 ngày liên tiếp: `[10.0, 20.0, 30.0]`. Hãy tính giá trị trung bình trượt với cửa sổ `window=2, min_periods=2` tại từng ngày và giải thích tại sao ngày đầu tiên lại là `NaN`.
:::

::: solution
- Ngày 1: Cửa sổ trượt chỉ mới có 1 quan sát `[10.0]`. Do tham số `min_periods=2` yêu cầu phải có tối thiểu 2 quan sát hợp lệ, kết quả tại ngày này là `NaN`.
- Ngày 2: Cửa sổ chứa 2 quan sát `[10.0, 20.0]`, trung bình bằng $(10 + 20) / 2 = 15.0$.
- Ngày 3: Cửa sổ trượt chứa 2 quan sát `[20.0, 30.0]`, trung bình bằng $(20 + 30) / 2 = 25.0$.
Kết quả chuỗi là `[NaN, 15.0, 25.0]`.
:::

## 6. Nguồn và đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 11: Time Series](https://wesmckinney.com/book/time-series).
- Hướng dẫn chính thức: [pandas User Guide — Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html).
- Cơ sở dữ liệu múi giờ quốc tế: [IANA Time Zone Database](https://www.iana.org/time-zones).
- [Bài giảng tham khảo môn Xử lý dữ liệu (iaidev)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-08-du-lieu-thoi-gian.html).
