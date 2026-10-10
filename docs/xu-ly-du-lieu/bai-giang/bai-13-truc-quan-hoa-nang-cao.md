---
course: xu-ly-du-lieu
lecture: bai-13-truc-quan-hoa-nang-cao
section: lecture
title: "Trực quan hóa nâng cao & đọc biểu đồ"
prerequisites: ["ky-vong","phuong-sai","gia-tri-thieu"]
lessonStatus: ready
description: "Trực quan hóa nâng cao với seaborn và bản đồ địa lý; giải phẫu boxplot đa chiều trên thang log, bóc trần bẫy chọn mốc so sánh và lập hồ sơ phản biện biểu đồ."
---

Một biểu đồ được lập trình hoàn hảo về mặt kỹ thuật, không có bất kỳ lỗi cú pháp nào và truy xuất số liệu chính xác từ cơ sở dữ liệu, vẫn có thể dẫn dắt người xem đến những kết luận hoàn toàn sai lệch. Trực quan hóa dữ liệu không dừng lại ở kỹ năng sử dụng công cụ đồ họa. Phẩm chất quan trọng hơn của một nhà khoa học dữ liệu là **năng lực đọc và thẩm định biểu đồ có tư duy phản biện (Critical Chart Literacy)**: nhìn thấu qua lớp vỏ đồ họa hào nhoáng để nhận diện các thủ pháp phóng đại thị giác, các thang đo bị thao túng và các cách chọn mốc so sánh có lợi (cherry-picking).

Khi sản lượng hai quý là 98 và 100, mức tăng trưởng thực tế chỉ là 2%. Tuy nhiên, chỉ bằng một thao tác cắt gọt trục tung, người ta có thể làm cho cột thứ hai trông cao gấp ba lần cột thứ nhất. Tương tự, nếu một báo cáo so sánh lượng khách du lịch năm 2025 với đáy đại dịch năm 2020 rồi giật tít *"tăng trưởng bùng nổ 8 lần"*, người phân tích đã cố tình đánh tráo sự hồi phục tự nhiên sau biến cố phong tỏa thành một kỳ tích kinh doanh.

Bài học này trang bị kỹ năng trực quan hóa nâng cao với thư viện seaborn và dữ liệu không gian GeoPandas: từ việc phân tích phân phối đa chiều bằng boxplot trên thang đo logarit, kỹ thuật dựng cặp bản đồ giá và nguồn cung để tránh bẫy diện tích địa lý, đến phương pháp bóc trần hệ số dối trá (Lie Factor) và quy trình lập hồ sơ lỗi phản biện các ấn phẩm số liệu.

---

## 1. Phân tích phân phối đa biến với Seaborn và Thang đo Logarit

Biểu đồ hộp (Boxplot) do John Tukey đề xuất là công cụ mạnh mẽ để khảo sát đồng thời vị trí trung tâm và độ phân tán của dữ liệu qua bộ 5 số: cực tiểu trong hàng rào, tứ phân vị dưới ($Q_1$), trung vị ($Q_2$), tứ phân vị trên ($Q_3$) và cực đại trong hàng rào.

### Cơ chế hoạt động của râu hộp (Whiskers) và ranh giới Tukey

Nhiều người lầm tưởng rằng hai đầu râu của boxplot luôn kéo dài tới đúng vị trí của hàng rào lý thuyết:
$$
\text{Hàng rào dưới: } Q_1 - 1.5 \times IQR \quad \text{và} \quad \text{Hàng rào trên: } Q_3 + 1.5 \times IQR
$$
với $IQR = Q_3 - Q_1$ là khoảng tứ phân vị.

Thực tế hoàn toàn không phải như vậy:
- Đầu râu trên chỉ vươn tới **quan sát thực tế lớn nhất vẫn còn nằm bên trong hàng rào trên**. Nếu hàng rào trên là 22 nhưng giá trị thực tế lớn nhất nhỏ hơn 22 là 16, râu trên sẽ dừng lại chính xác tại 16.
- Đầu râu dưới chỉ vươn tới **quan sát thực tế nhỏ nhất vẫn còn nằm bên trong hàng rào dưới**.
- Mọi quan sát vượt ra ngoài hai hàng rào này được coi là điểm ngoại lai và được vẽ thành các dấu chấm riêng biệt.

### Nhu cầu tất yếu của Thang đo Logarit (Log Scale) trước dữ liệu lệch phải

Trong các bài toán kinh tế như giá thuê phòng hay thu nhập, phân phối dữ liệu thường bị **lệch phải nghiêm trọng (Heavy Right-Skewed)**: đại đa số các căn hộ có giá bình dân từ 20 đến 80 USD, nhưng có một số ít biệt thự và penthouse có giá lên tới hàng nghìn hoặc chục nghìn USD.

Nếu vẽ boxplot trên thang đo tuyến tính thông thường:
- Toàn bộ các hộp của các phân khúc sẽ bị nén chặt thành một dải mỏng dính sát cạnh đáy đồ thị.
- Các điểm ngoại lai kéo dài tít tắp lên phía trên, chiếm tới 90% diện tích khung tranh.
- Người xem hoàn toàn không thể so sánh được sự khác biệt giữa trung vị và khoảng tứ phân vị của các nhóm.

Việc chuyển trục giá sang thang đo logarit (`ax.set_xscale("log")`) biến đổi phép nhân thành phép cộng, kéo các khoảng cách cấp số nhân về các khoảng cách đều đặn trên thị giác:
$$
\log_{10}(10) = 1, \quad \log_{10}(100) = 2, \quad \log_{10}(1000) = 3
$$
Nhờ đó, hình dạng phân phối của từng nhóm phòng được mở rộng rõ ràng, cho phép ta so sánh trực quan cả về độ lệch tâm lẫn độ trải giữa của các nhóm chủ nhà khác nhau.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Tạo dữ liệu giả lập giá phòng lệch phải
np.random.seed(42)
df_gia = pd.DataFrame({
    "room_type": ["Entire home/apt"] * 100 + ["Private room"] * 100,
    "kieu_host": (["cá nhân"] * 50 + ["chuyên nghiệp"] * 50) * 2,
    "price": np.concatenate([
        np.random.lognormal(mean=4.5, sigma=0.6, size=50), # Căn hộ cá nhân
        np.random.lognormal(mean=5.2, sigma=0.7, size=50), # Căn hộ chuyên nghiệp (giá cao hơn)
        np.random.lognormal(mean=3.8, sigma=0.5, size=50), # Phòng riêng cá nhân
        np.random.lognormal(mean=4.1, sigma=0.6, size=50), # Phòng riêng chuyên nghiệp
    ])
})

fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df_gia, x="price", y="room_type", hue="kieu_host", ax=ax, palette="Blues")
ax.set_xscale("log")
ax.set_title("Phân phối giá theo loại phòng và nhóm chủ nhà trên thang log", pad=12, fontweight="bold")
ax.set_xlabel("Giá thuê mỗi đêm (USD, thang đo log)")
ax.set_ylabel("Loại chỗ ở")
plt.tight_layout()
plt.show()
```

---

## 2. Trực quan hóa dữ liệu không gian và Cặp bản đồ tránh bẫy diện tích

Khi làm việc với dữ liệu đô thị và du lịch, bản đồ phân bố màu sắc theo ranh giới hành chính (**Choropleth Map**) là công cụ trực quan hóa địa lý phổ biến nhất. Tuy nhiên, bản đồ Choropleth ẩn chứa một cạm bẫy nhận thức thị giác rất lớn: **Bẫy diện tích địa lý (Geographical Area Bias)**.

Trong các đô thị lớn:
- Các quận nội thành trung tâm thường có diện tích địa lý rất nhỏ nhưng mật độ dân cư và số lượng phòng cho thuê lại dày đặc (chiếm tới 70-80% nguồn cung).
- Trái lại, các quận ngoại thành hoặc vùng đệm miền núi có diện tích bao la rộng lớn nhưng chỉ có lưa thưa vài căn hộ.

Nếu bạn chỉ vẽ một bản đồ duy nhất thể hiện giá trung vị:
- Các quận ngoại ô rộng lớn với diện tích khổng lồ sẽ đập ngay vào mắt người xem, tạo cảm giác rằng đây là thị trường chủ đạo của thành phố.
- Người xem bị diện tích đánh lừa và ngộ nhận về quy mô kinh tế thực tế.

### Giải pháp: Cặp bản đồ song hành (Giá và Nguồn cung) và Xử lý vùng trắng

Để khắc phục điểm mù này, chuyên gia phân tích dữ liệu luôn dựng **cặp bản đồ song hành**:
1. Một bản đồ thể hiện **Giá trung vị** (chất lượng phân khúc).
2. Một bản đồ đặt ngay bên cạnh thể hiện **Số lượng chỗ ở** (quy mô nguồn cung thực tế).

Khi nhìn vào cặp bản đồ, người đọc sẽ nhận ra ngay: quận ngoại ô tuy có giá cao nhưng chỉ có vỏn vẹn vài căn hộ, trong khi quận trung tâm nhỏ bé mới là trái tim của thị trường với hàng nghìn cơ sở lưu trú.

Một bài học kỹ thuật quan trọng khi ghép nối bảng ranh giới địa lý (`geo`) với bảng dữ liệu thống kê (`ds`):
Một quận có thể có ranh giới hành chính trên bản đồ nhưng **hoàn toàn không có chỗ ở nào được đăng ký**. Sau phép ghép nối `geo.merge(ds_counts, how="left")`, cột số lượng `n` của quận đó sẽ mang giá trị `NaN`.
Trong ngữ cảnh này, giá trị `NaN` không phải là "chưa biết" hay "khuyết thiếu", mà là một sự thật khẳng định: **tại quận đó có đúng 0 chỗ ở**. Lập trình viên bắt buộc phải điền giá trị 0 bằng `fillna(0)` để bản đồ tô màu trắng hoặc màu nhạt nhất cho quận này, tránh làm phát sinh lỗi render đồ họa.

---

## 3. Bóc trần thủ thuật chọn mốc so sánh có lợi (Cherry-Picking Baseline)

Một đồ thị có thể sử dụng các số liệu hoàn toàn chính xác nhưng vẫn là một tác phẩm ngụy tạo nếu người vẽ cố tình chọn mốc thời gian cơ sở (Baseline) có lợi để phục vụ cho một kết luận thiên kiến.

Hãy xem xét diễn biến số lượng đánh giá của một thị trường qua các năm:
- Năm 2016: 120 lượt
- Năm 2019: 420 lượt (đỉnh cao trước đại dịch)
- Năm 2020: 90 lượt (đáy sâu phong tỏa do đại dịch COVID-19)
- Năm 2025: 700 lượt

Nếu người vẽ biểu đồ muốn tạo cảm giác về một sự bùng nổ kỳ diệu, họ sẽ cắt gọt trục thời gian chỉ lấy từ năm 2020 đến 2025:
$$
\text{Tốc độ tăng trưởng hiển thị} = \frac{700}{90} \approx 7.78 \text{ lần (tăng gần 800\%)}
$$
và giật tít: *"Thị trường bùng nổ gấp 8 lần!"*.

### Phản biện khoa học và Bản sửa trung thực

Sự "bùng nổ" này là một ảo giác toán học. Năm 2020 là một năm dị biệt khi toàn bộ các chuyến bay bị đình chỉ và các thành phố bị phong tỏa. Bất kỳ ngành dịch vụ nào khi mở cửa trở lại sau phong tỏa cũng sẽ có tốc độ tăng trưởng tính từ đáy sâu trông như một bước nhảy vọt.

Nếu so sánh năm 2025 với mốc bình thường trước dịch là năm 2019:
$$
\text{Tốc độ tăng trưởng thực chất} = \frac{700}{420} \approx 1.67 \text{ lần (tăng 67\% sau 6 năm)}
$$
Mức tăng 67% sau 6 năm (tương đương bình quân $\approx 8.9\%$ mỗi năm) là một tốc độ tăng trưởng lành mạnh, hoàn toàn không phải là "bùng nổ thần kỳ gấp 8 lần".

**Quy tắc biên tập trung thực**:
1. Khi vẽ chuỗi thời gian dài hạn, phải kéo dài chuỗi qua cả giai đoạn trước khủng hoảng (từ 2016 đến 2025).
2. Đánh dấu rõ ràng giai đoạn khủng hoảng (năm 2020–2021) bằng vùng tô màu xám nhạt (`ax.axvspan`) hoặc ghi chú văn bản giải thích.
3. Tiêu đề biểu đồ phải phản ánh đúng bản chất hồi phục và tăng trưởng ổn định dài hạn, từ chối các từ ngữ giật gân, phóng đại.

---

## 4. Hệ số dối trá (Lie Factor) và Năm câu hỏi phản biện biểu đồ

Nhà lý thuyết đồ họa Edward Tufte đã lượng hóa mức độ bóp méo thông tin của một biểu đồ thông qua chỉ số **Hệ số dối trá (Lie Factor)**:

$$
\text{Lie Factor} = \frac{\text{Tỷ lệ biến thiên đo được trên hình vẽ}}{\text{Tỷ lệ biến thiên thực tế trong dữ liệu}}
$$

- $\text{Lie Factor} = 1.0$: Biểu đồ phản ánh trung thực tuyệt đối dữ liệu.
- $\text{Lie Factor} > 1.05$: Biểu đồ đang phóng đại mức độ biến động của dữ liệu.
- $\text{Lie Factor} < 0.95$: Biểu đồ đang giảm thiểu, làm mờ nhạt mức độ biến động thực tế.

Khi đọc bất kỳ biểu đồ số liệu nào trong báo cáo kinh doanh hay bài báo khoa học, hãy luôn tự vấn qua **Năm câu hỏi phản biện**:
1. **Trục tọa độ và Điểm gốc**: Trục đo có bị cắt cụt không? Có điểm mốc 0 đối với biểu đồ cột không? Thang đo là tuyến tính hay logarit?
2. **Cỡ mẫu $N$**: Biểu đồ có chú thích quy mô mẫu của từng nhóm không? Sự khác biệt có bị chi phối bởi một nhóm có cỡ mẫu quá nhỏ không?
3. **Thanh sai số (Error Bars)**: Các vạch sai số đại diện cho độ lệch chuẩn ($SD$), sai số chuẩn ($SE$), hay khoảng tin cậy $95\%$ ($CI$)?
4. **Mốc thời gian so sánh**: Mốc xuất phát có bị chọn lọc có chủ đích (chọn đáy hoặc chọn đỉnh) để tạo ra tỷ số phóng đại không?
5. **Mối quan hệ nhân quả**: Biểu đồ có đang gán ghép một mối tương quan thuần túy thành một kết luận nhân quả chưa được chứng minh không?

---

## 5. Hệ thống bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 13) {#bai-tap}

Hệ thống bài tập dưới đây mô phỏng bài toán trực quan hóa nâng cao trên dữ liệu lưu trú tại Santiago: từ việc so sánh phân phối giá bằng boxplot seaborn trên thang log, ghép nối ranh giới địa lý tạo bản đồ số chỗ ở, đến việc bóc trần và sửa chữa một biểu đồ chọn mốc thời gian thiên lệch.

### Dữ liệu thực hành giả lập

```python
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

Path("figures").mkdir(exist_ok=True)

# Khởi tạo bảng danh sách chỗ ở (48 căn hộ thuộc 5 quận)
_QUAN = ["Santiago"] * 18 + ["Providencia"] * 12 + ["Las Condes"] * 8 + ["Ñuñoa"] * 6 + ["Lo Barnechea"] * 4
DEMO_DS = pd.DataFrame({
    "id": range(201, 249),
    "neighbourhood": _QUAN,
    "room_type": ["Private room" if k % 4 == 1 else "Entire home/apt" for k in range(48)],
    "price": [None if k % 11 == 5 else float(18000 + (k * 7919) % 90000 + (15000 if k % 3 == 0 else 0))
              for k in range(48)],
    "calculated_host_listings_count": [1 + (k * 5) % 9 for k in range(48)],
})

# Danh sách 6 quận trên bản đồ ranh giới hành chính (quận Pirque không có chỗ ở nào)
DEMO_QUAN_BAN_DO = ["Santiago", "Providencia", "Las Condes", "Ñuñoa", "Lo Barnechea", "Pirque"]

# Số lượng đánh giá lịch sử từ năm 2014 đến 2026
_SO_THEO_NAM = {2014: 40, 2015: 70, 2016: 120, 2017: 210, 2018: 330, 2019: 420, 2020: 90,
                2021: 150, 2022: 380, 2023: 520, 2024: 610, 2025: 700, 2026: 260}
DEMO_RV = pd.DataFrame({
    "date": [pd.Timestamp(f"{nam}-01-01") + pd.Timedelta(days=(k * 97) % (181 if nam == 2026 else 365))
             for nam, so in _SO_THEO_NAM.items() for k in range(so)]
})

# Phân loại nhóm chủ nhà: từ 5 căn trở lên là chuyên nghiệp
DEMO_DS["kieu_host"] = (DEMO_DS["calculated_host_listings_count"] >= 5).map(
    {True: "chuyên nghiệp", False: "cá nhân"}
)
co_gia = DEMO_DS.dropna(subset=["price"]).copy()
```

---

### Bài 1: Dựng Boxplot Seaborn với `hue` trên Thang đo Logarit

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `plot_price_box(co_gia: pd.DataFrame) -> plt.Axes` nhận vào DataFrame `co_gia` chứa cột `price` (số dương, không khuyết thiếu), `room_type` và `kieu_host`.

Yêu cầu định dạng biểu đồ:
- Khởi tạo hình mới `fig, ax = plt.subplots(figsize=(8.5, 4))`.
- Vẽ biểu đồ hộp bằng seaborn: `sns.boxplot(data=co_gia, x="price", y="room_type", hue="kieu_host", ax=ax)`.
- **Khóa trục x theo thang logarit**: `ax.set_xscale("log")`.
- Tiêu đề biểu đồ nêu rõ thông điệp phân tích (ít nhất 15 ký tự).
- Trục x có nhãn kèm đơn vị rõ ràng. Chú giải (`legend`) liệt kê đầy đủ hai nhãn `"chuyên nghiệp"` và `"cá nhân"`.
- Trả về đối tượng `ax`.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def plot_price_box(co_gia: pd.DataFrame) -> plt.Axes:
    fig, ax = plt.subplots(figsize=(8.5, 4))
    
    # Vẽ boxplot đa chiều bằng seaborn
    sns.boxplot(
        data=co_gia,
        x="price",
        y="room_type",
        hue="kieu_host",
        ax=ax,
        palette="Set2"
    )
    
    # Thiết lập thang log cho trục giá
    ax.set_xscale("log")
    
    ax.set_title("Chủ nhà chuyên nghiệp có mức giá trung vị cao hơn ở cả hai loại phòng", pad=12, fontweight="bold")
    ax.set_xlabel("Giá thuê mỗi đêm (CLP, thang đo log)")
    ax.set_ylabel("Loại phòng")
    
    return ax
```

#### Phân tích sư phạm chuyên sâu: Đọc biểu đồ Boxplot
- **Hộp của nhóm chuyên nghiệp nằm lệch về phía nào?**
  Ở cả hai loại phòng (nguyên căn và phòng riêng), hộp của nhóm chủ nhà chuyên nghiệp đều nằm lệch về bên phải so với nhóm chủ nhà cá nhân. Điều này chứng minh rằng các đơn vị vận hành chuyên nghiệp thường sở hữu các căn hộ ở phân khúc cao cấp hơn và định giá cao hơn.
- **Vì sao bắt buộc phải dùng thang log?**
  Phân phối giá thuê có đuôi kéo dài về bên phải rất nặng. Nếu giữ nguyên thang đo tuyến tính, các hộp sẽ bị co cụm lại sát biên trái và ta hoàn toàn không thể nhận ra khoảng cách chênh lệch giữa hai nhóm chủ nhà.
:::

---

### Bài 2: Ghép nối ranh giới địa lý và Xử lý vùng trắng bản đồ

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `count_by_area(ds: pd.DataFrame, geo: pd.DataFrame) -> dict` nhận vào bảng chỗ ở `ds` (`neighbourhood`) và bảng ranh giới quận `geo` (`neighbourhood` không trùng lặp).

Quy trình thực thi:
1. Đếm số chỗ ở theo từng quận từ bảng `ds` thành bảng có hai cột `neighbourhood` và `n`.
2. Ghép nối với bảng ranh giới bằng phép nối trái: `geo.merge(..., on="neighbourhood", how="left")`.
3. Đếm số lượng quận trên bản đồ hoàn toàn **không có chỗ ở nào** (giá trị `NaN` ngay sau phép ghép nối).
4. Điền giá trị 0 cho các ô `NaN` của cột `n` và chuyển về kiểu số nguyên `int`.
5. Trả về từ điển gồm hai khóa:
   - `"so_quan_nan"`: Số nguyên là số quận không có chỗ ở nào trong bảng dữ liệu.
   - `"ban_do"`: Bảng sau ghép nối, giữ nguyên số dòng và thứ tự dòng của `geo`, cột `n` là kiểu số nguyên không còn `NaN`. Tuyệt đối không làm thay đổi bảng `geo` gốc.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def count_by_area_co_ban(ds: pd.DataFrame, geo: pd.DataFrame) -> dict:
    # 1. Đếm số chỗ ở mỗi quận
    dem = ds.groupby("neighbourhood").size().reset_index(name="n")
    
    # 2. Ghép nối trái vào bảng ranh giới
    ban_do_tho = geo.merge(dem, on="neighbourhood", how="left")
    
    # 3. Đếm số quận bị khuyết thiếu dữ liệu
    so_quan_nan = int(ban_do_tho["n"].isna().sum())
    
    # 4. Điền 0 và ép kiểu số nguyên
    ban_do_tho["n"] = ban_do_tho["n"].fillna(0).astype(int)
    
    return {
        "ban_do": ban_do_tho,
        "so_quan_nan": so_quan_nan
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Chuỗi xử lý hàm tinh gọn)

```python
def count_by_area(ds: pd.DataFrame, geo: pd.DataFrame) -> dict:
    dem = ds.groupby("neighbourhood").size().rename("n")
    ban_do = geo.merge(dem, on="neighbourhood", how="left")
    
    so_nan = int(ban_do["n"].isna().sum())
    ban_do["n"] = ban_do["n"].fillna(0).astype(int)
    
    return {
        "ban_do": ban_do,
        "so_quan_nan": so_nan
    }
```

#### Phân tích sư phạm chuyên sâu: Diễn giải ý nghĩa phép thế NaN = 0
- Trong các bài toán ghép nối bảng, `NaN` thường thể hiện sự thiếu thông tin. Nhưng trong bài toán thống kê không gian địa lý, nếu một quận nằm trong phạm vi hành chính của thành phố mà không xuất hiện bất kỳ căn hộ nào trong danh sách khảo sát, điều đó đồng nghĩa với việc số lượng nguồn cung tại quận đó chính xác bằng $0$.
- Việc chủ động thay thế `NaN` bằng $0$ cho phép thư viện bản đồ tô màu trắng hoặc màu nhạt nhất cho quận này, cung cấp cho nhà quản lý bức tranh trung thực về những "vùng trắng du lịch" của thành phố.
:::

---

### Bài 3: Tổng hợp số lượng đánh giá theo năm trong một khoảng

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `yearly_counts(rv: pd.DataFrame, bat_dau: str, ket_thuc: str) -> pd.Series` nhận vào bảng đánh giá `rv` (cột `date`) và hai mốc năm dạng chuỗi `bat_dau`, `ket_thuc` (ví dụ `"2016"`, `"2025"`).

Hàm thực hiện:
- Đưa `date` làm chỉ mục và lấy mẫu lại theo năm kết thúc bằng `resample("YE").size()`.
- Cắt lát chuỗi từ `bat_dau` đến `ket_thuc`.
- Trả về Series có chỉ mục là `DatetimeIndex` đại diện ngày cuối năm, những năm không có đánh giá mang giá trị là 0.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def yearly_counts(rv: pd.DataFrame, bat_dau: str, ket_thuc: str) -> pd.Series:
    return (
        rv.set_index("date")
        .resample("YE")
        .size()
        .loc[bat_dau:ket_thuc]
    )
```

#### Phân tích so sánh & Trực giác bản chất
- Tần số `"YE"` (Year End) là chuẩn mực mới của pandas thay thế cho ký hiệu cũ `"Y"`. Nó gán nhãn mỗi năm bằng ngày cuối cùng của năm đó (ví dụ `2020-12-31`), bảo đảm sự thống nhất toán học trên dòng thời gian.
:::

---

### Bài 4: So sánh tốc độ tăng trưởng với các mốc cơ sở khác nhau

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `compare_baselines(nam: pd.Series, nam_cuoi: int, cac_moc: list) -> dict` nhận vào:
- `nam`: Series số đếm theo năm (chỉ mục `DatetimeIndex`).
- `nam_cuoi`: Số nguyên là năm kết thúc cần đánh giá (ví dụ `2025`).
- `cac_moc`: Danh sách các năm làm mốc so sánh cơ sở (ví dụ `[2020, 2019, 2016]`).

Hàm tính toán và trả về từ điển:
$$
\{\text{moc}: \text{số\_lượng}(nam\_cuoi) / \text{số\_lượng}(\text{moc})\}
$$
cho từng năm trong `cac_moc` theo đúng thứ tự ban đầu. Giá trị là số thực `float` không làm tròn.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def compare_baselines(nam: pd.Series, nam_cuoi: int, cac_moc: list) -> dict:
    # Lấy giá trị của năm đích
    gia_tri_dich = nam[nam.index.year == nam_cuoi].iloc[0]
    
    ket_qua = {}
    for moc in cac_moc:
        gia_tri_moc = nam[nam.index.year == moc].iloc[0]
        ket_qua[moc] = float(gia_tri_dich / gia_tri_moc)
        
    return ket_qua
```

#### Phân tích sư phạm chuyên sâu: Sự thật đằng sau các con số
Khi chạy hàm trên dữ liệu mẫu với năm đích 2025:
- So với mốc 2020: Tỷ số là **$7.78$ lần** ($700 / 90$).
- So với mốc 2019: Tỷ số là **$1.67$ lần** ($700 / 420$).
- So với mốc 2016: Tỷ số là **$5.83$ lần** ($700 / 120$).

Nếu chỉ báo cáo duy nhất con số $7.78$ lần so với năm 2020, bạn đang chọn một mốc cơ sở bất thường để phóng đại thành tích. Một báo cáo khoa học khách quan bắt buộc phải đặt năm 2025 cạnh mốc 2019 trước đại dịch.
:::

---

### Bài 5: Phục hồi tính trung thực cho biểu đồ xu hướng thời gian

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `plot_fixed_trend(nam: pd.Series, path, covid: tuple = (2020, 2021)) -> plt.Axes` nhận vào:
- `nam`: Series số lượng đánh giá của chuỗi năm đầy đủ (ví dụ 2016–2025).
- `path`: Đường dẫn lưu tệp PNG.
- `covid`: Cặp năm đánh dấu giai đoạn đại dịch (mặc định `(2020, 2021)`).

Yêu cầu sửa chữa:
- Khởi tạo hình mới và vẽ một đường biểu diễn toàn bộ các năm của `nam` (`nam.index.year`).
- **Đánh dấu giai đoạn đại dịch** bằng vùng tô màu xám nhạt xuyên suốt trục x (`ax.axvspan(covid[0] - 0.5, covid[1] + 0.5, color="#e2e8f0", alpha=0.5)`) kèm chú thích văn bản.
- Tiêu đề phản ánh đúng xu hướng hồi phục và tăng trưởng dài hạn (ít nhất 15 ký tự, không dùng từ ngữ giật gân).
- Nhãn trục y ghi rõ đơn vị. Lưu ảnh vào `path` và trả về đối tượng `ax`.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def plot_fixed_trend(nam: pd.Series, path, covid: tuple = (2020, 2021)) -> plt.Axes:
    fig, ax = plt.subplots(figsize=(8, 3.8))
    
    nam_x = nam.index.year
    ax.plot(nam_x, nam.values, marker="o", color="#1E93AB", linewidth=2.2, label="Số lượt đánh giá")
    
    # Đánh dấu vùng ảnh hưởng của dịch bệnh
    ax.axvspan(covid[0] - 0.5, covid[1] + 0.5, color="#f1f5f9", alpha=0.8, zorder=0)
    ax.text(
        (covid[0] + covid[1]) / 2, ax.get_ylim()[1] * 0.7,
        "Giai đoạn đại dịch\n(2020–2021)",
        ha="center", va="center", color="#64748b", fontsize=9, fontweight="semibold"
    )
    
    ax.set_title("Thị trường phục hồi vững chắc và vượt đỉnh trước đại dịch", pad=12, fontweight="bold")
    ax.set_xlabel("Năm")
    ax.set_ylabel("Số lượng đánh giá (lượt)")
    ax.set_xticks(nam_x)
    
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax
```

#### Hồ sơ lỗi (Critique Dossier) của biểu đồ gốc
1. **Lỗi 1 (Mốc so sánh có lợi - Cherry-picked Baseline)**: Biểu đồ gốc cố tình cắt bỏ toàn bộ giai đoạn 2014–2019, chỉ bắt đầu chuỗi từ năm 2020 (đáy khủng hoảng), khiến mức tăng trưởng trông như một sự bùng nổ kỳ diệu.
2. **Lỗi 2 (Ngôn từ phóng đại giật gân)**: Tiêu đề gốc dùng cụm từ *"BÙNG NỔ x8 lần"* để mô tả một hiện tượng hồi phục tự nhiên sau khi dỡ bỏ phong tỏa.
3. **Bản sửa khác hình gốc ở điểm nào?**: Bản sửa kéo dài chuỗi dữ liệu về năm 2016 để người đọc thấy rõ bối cảnh trước dịch, đồng thời đánh dấu vùng xám cho hai năm dịch bệnh, giúp người xem hiểu rằng năm 2020 là một dị biệt ngoại cảnh chứ không phải phong độ kinh doanh thực tế.
:::

---

### Bài tự làm mở rộng: Trực quan hóa tương tác với Plotly Express

::: exercise Đề bài mở rộng
Hãy viết mã sử dụng thư viện `plotly.express` để vẽ biểu đồ phân tán tương tác kinh độ và vĩ độ của các chỗ ở:
1. Thể hiện mức giá qua màu sắc hoặc kích thước điểm.
2. Cung cấp thông tin chi tiết (tên chỗ ở, quận, giá) khi người dùng rê chuột qua (*Hover tooltip*).
3. Phân tích sự đánh đổi giữa biểu đồ tương tác trên web và biểu đồ tĩnh trong các báo cáo xuất bản PDF.
:::

::: solution
#### Mã nguồn biểu đồ tương tác

```python
import plotly.express as px

# Tạo dữ liệu tọa độ mô phỏng
np.random.seed(42)
df_map_points = pd.DataFrame({
    "name": [f"Chỗ ở tiện nghi {i}" for i in range(1, 101)],
    "neighbourhood": np.random.choice(["Santiago", "Providencia", "Las Condes"], 100),
    "latitude": -33.45 + np.random.normal(0, 0.02, 100),
    "longitude": -70.65 + np.random.normal(0, 0.02, 100),
    "price": np.random.exponential(scale=50, size=100) + 20
})

# Dựng biểu đồ phân tán tương tác
fig_interactive = px.scatter(
    df_map_points,
    x="longitude",
    y="latitude",
    color="price",
    hover_name="name",
    hover_data=["neighbourhood", "price"],
    color_continuous_scale="Viridis",
    title="Phân bố không gian các chỗ ở tại Santiago (Thử nghiệm Tương tác)"
)

# Xuất ra tệp HTML độc lập
fig_interactive.write_html("figures/ban_do_tuong_tac.html")
print("Đã tạo tệp bản đồ tương tác HTML độc lập tại figures/ban_do_tuong_tac.html")
```

#### Phân tích chuyên môn: Đánh đổi giữa Biểu đồ tương tác và Biểu đồ tĩnh
- **Ưu điểm của biểu đồ tương tác**: Cung cấp khả năng đào sâu dữ liệu (Drill-down). Khi phát hiện một điểm ngoại lai có giá 5.000 USD nằm đơn độc, người phân tích chỉ cần rê chuột qua là biết ngay tên căn hộ và địa chỉ cụ thể mà không cần phải viết thêm truy vấn SQL.
- **Vì sao báo cáo chính thức vẫn bắt buộc phải có biểu đồ tĩnh?**:
  Báo cáo điều hành, hồ sơ kiểm toán và ấn phẩm khoa học thường được lưu trữ và in ấn dưới dạng tệp PDF cố định. Biểu đồ tương tác sẽ hoàn toàn bị vô hiệu hóa khi in ra giấy. Một biểu đồ tĩnh xuất sắc phải tự thân truyền tải đầy đủ thông điệp, nhãn trục, cỡ mẫu và bối cảnh mà không cần dựa dẫm vào hành vi rê chuột của người đọc.
:::

---

## 6. Tổng kết và Đọc thêm

| Kỹ thuật trực quan hóa | Bản chất toán học & Kỹ nghệ | Trực giác phản biện |
| :--- | :--- | :--- |
| **Boxplot đa chiều trên thang Log** | Tóm tắt 5 số; râu dừng ở quan sát thực tế; thang log kéo dãn đuôi lệch | Tránh bị nén hộp; so sánh công bằng giữa các nhóm có quy mô giá cách biệt. |
| **Cặp bản đồ Choropleth** | Ghép nối ranh giới GeoPandas; điền `n.fillna(0)` cho vùng trắng | Chống bẫy diện tích địa lý; đặt bản đồ giá cạnh bản đồ nguồn cung để thấy bức tranh toàn cảnh. |
| **Phản biện mốc so sánh** | Đổi mốc cơ sở $\{Y_t / Y_{t_0}\}$; bóc trần Lie Factor | Cảnh giác với việc so sánh với đáy khủng hoảng; luôn kéo dài chuỗi qua cả thời kỳ bình thường. |
| **Năm câu hỏi phản biện** | Kiểm tra trục, cỡ mẫu $N$, thanh sai số, mốc so sánh và tính nhân quả | Bảo vệ uy tín khoa học; từ chối các kết luận giật gân xây dựng trên ngụy tạo thị giác. |

### Tài liệu tham khảo học thuật

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 9: Plotting and Visualization](https://wesmckinney.com/book/plotting-and-visualization).
- Edward R. Tufte, *The Visual Display of Quantitative Information*, Graphics Press, 2001 (Chương 2: *Graphical Integrity* và *Lie Factor*).
- Thư viện Seaborn: [Official Tutorial: Categorical Plots](https://seaborn.pydata.org/tutorial/categorical.html).
- Thư viện GeoPandas: [GeoPandas Official Documentation: Mapping and Plotting Tools](https://geopandas.org/en/stable/docs/user_guide/mapping.html).
- Hệ thống bài giảng thực hành: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
