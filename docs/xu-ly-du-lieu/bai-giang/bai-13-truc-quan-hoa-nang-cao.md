---
course: xu-ly-du-lieu
lecture: bai-13-truc-quan-hoa-nang-cao
section: lecture
title: "Trực quan hóa nâng cao & đọc biểu đồ"
prerequisites: ["thong-ke-mo-ta", "gia-tri-thieu"]
lessonStatus: ready
description: "Trực quan hóa nâng cao với seaborn và bản đồ địa lý; giải phẫu boxplot đa chiều trên thang log, bóc trần bẫy chọn mốc so sánh và lập hồ sơ phản biện biểu đồ."
---

Một biểu đồ được lập trình hoàn hảo về mặt kỹ thuật, không có bất kỳ lỗi cú pháp nào và truy xuất số liệu chính xác từ cơ sở dữ liệu, vẫn có thể dẫn dắt người xem đến những kết luận hoàn toàn sai lệch. Trực quan hóa dữ liệu không dừng lại ở kỹ năng sử dụng công cụ đồ họa. Phẩm chất quan trọng hơn của một nhà khoa học dữ liệu là **năng lực đọc và thẩm định biểu đồ có tư duy phản biện (Critical Chart Literacy)**: Nhìn thấu qua lớp vỏ đồ họa hào nhoáng để nhận diện các thủ pháp phóng đại thị giác, các thang đo bị thao túng và các cách chọn mốc so sánh có lợi (cherry-picking).

Khi sản lượng hai quý là 98 và 100, mức tăng trưởng thực tế chỉ là 2%. Tuy nhiên, chỉ bằng một thao tác cắt gọt trục tung, người ta có thể làm cho cột thứ hai trông cao gấp ba lần cột thứ nhất. Tương tự, nếu một báo cáo so sánh lượng khách du lịch năm 2025 với đáy đại dịch năm 2020 rồi giật tít *"tăng trưởng bùng nổ 8 lần"*, người phân tích đã cố tình đánh tráo sự hồi phục tự nhiên sau biến cố phong tỏa thành một kỳ tích kinh doanh.

Bài học này trang bị kỹ năng trực quan hóa nâng cao với thư viện seaborn và dữ liệu không gian GeoPandas: Từ việc phân tích phân phối đa chiều bằng boxplot trên thang đo logarit, kỹ thuật dựng cặp bản đồ giá và nguồn cung để tránh bẫy diện tích địa lý, đến phương pháp bóc trần hệ số dối trá (Lie Factor) và quy trình lập hồ sơ lỗi phản biện các ấn phẩm số liệu.

---

## 1. Phân tích phân phối đa biến với Seaborn và Thang đo Logarit

Biểu đồ hộp (Boxplot) do John Tukey đề xuất là công cụ mạnh mẽ để khảo sát đồng thời vị trí trung tâm và độ phân tán của dữ liệu qua bộ 5 số: Cực tiểu trong hàng rào, tứ phân vị dưới ($Q_1$), trung vị ($Q_2$), tứ phân vị trên ($Q_3$) và cực đại trong hàng rào.

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

Trong các bài toán kinh tế như giá thuê phòng hay thu nhập, phân phối dữ liệu thường bị **lệch phải nghiêm trọng (Heavy Right-Skewed)**: Đại đa số các căn hộ có giá bình dân từ 20 đến 80 USD, nhưng có một số ít biệt thự và penthouse có giá lên tới hàng nghìn hoặc chục nghìn USD.

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

Khi nhìn vào cặp bản đồ, người đọc sẽ nhận ra ngay: Quận ngoại ô tuy có giá cao nhưng chỉ có vỏn vẹn vài căn hộ, trong khi quận trung tâm nhỏ bé mới là trái tim của thị trường với hàng nghìn cơ sở lưu trú.

Một bài học kỹ thuật quan trọng khi ghép nối bảng ranh giới địa lý (`geo`) với bảng dữ liệu thống kê (`ds`):
Một quận có thể có ranh giới hành chính trên bản đồ nhưng **hoàn toàn không có chỗ ở nào được đăng ký**. Sau phép ghép nối `geo.merge(ds_counts, how="left")`, cột số lượng `n` của quận đó sẽ mang giá trị `NaN`.
Trong ngữ cảnh này, giá trị `NaN` không phải là "chưa biết" hay "khuyết thiếu", mà là một sự thật khẳng định: **Tại quận đó có đúng 0 chỗ ở**. Lập trình viên bắt buộc phải điền giá trị 0 bằng `fillna(0)` để bản đồ tô màu trắng hoặc màu nhạt nhất cho quận này, tránh làm phát sinh lỗi render đồ họa.

---

## 3. Bóc trần thủ thuật chọn mốc so sánh có lợi (Cherry-Picking Baseline)

Một đồ thị có thể sử dụng các số liệu hoàn toàn chính xác nhưng vẫn là một tác phẩm ngụy tạo nếu người vẽ cố tình chọn mốc thời gian cơ sở (Baseline) có lợi để phục vụ cho một kết luận thiên kiến.

Hãy xem xét diễn biến số lượng đánh giá của một thị trường qua các năm:
- Năm 2016: 120 lượt
- Năm 2019: 420 lượt (đỉnh cao trước đại dịch)
- Năm 2020: 90 lượt (đáy sâu phong tỏa do đại dịch COVID-19)
- Năm 2025: 700 lượt

Nếu người vẽ biểu đồ muốn tạo cảm giác về một sự bùng nổ đột biến, họ sẽ cắt gọt trục thời gian chỉ lấy từ năm 2020 đến 2025:
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

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 6. Tổng kết và Đọc thêm

| Kỹ thuật trực quan hóa | Bản chất toán học & Kỹ nghệ | Trực giác phản biện |
| :--- | :--- | :--- |
| **Boxplot đa chiều trên thang Log** | Tóm tắt 5 số; râu dừng ở quan sát thực tế; thang log kéo dãn đuôi lệch | Tránh bị nén hộp; so sánh công bằng giữa các nhóm có quy mô giá cách biệt. |
| **Cặp bản đồ Choropleth** | Ghép nối ranh giới GeoPandas; điền `n.fillna(0)` cho vùng trắng | Chống bẫy diện tích địa lý; đặt bản đồ giá cạnh bản đồ nguồn cung để thấy được cái nhìn toàn diện. |
| **Phản biện mốc so sánh** | Đổi mốc cơ sở $\{Y_t / Y_{t_0}\}$; bóc trần Lie Factor | Cảnh giác với việc so sánh với đáy khủng hoảng; luôn kéo dài chuỗi qua cả thời kỳ bình thường. |
| **Năm câu hỏi phản biện** | Kiểm tra trục, cỡ mẫu $N$, thanh sai số, mốc so sánh và tính nhân quả | Bảo vệ uy tín khoa học; từ chối các kết luận giật gân xây dựng trên ngụy tạo thị giác. |

### Tài liệu tham khảo học thuật

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 9: Plotting and Visualization](https://wesmckinney.com/book/plotting-and-visualization).
- Edward R. Tufte, *The Visual Display of Quantitative Information*, Graphics Press, 2001 (Chương 2: *Graphical Integrity* và *Lie Factor*).
- Thư viện Seaborn: [Official Tutorial: Categorical Plots](https://seaborn.pydata.org/tutorial/categorical.html).
- Thư viện GeoPandas: [GeoPandas Official Documentation: Mapping and Plotting Tools](https://geopandas.org/en/stable/docs/user_guide/mapping.html).
- Hệ thống bài giảng thực hành: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
