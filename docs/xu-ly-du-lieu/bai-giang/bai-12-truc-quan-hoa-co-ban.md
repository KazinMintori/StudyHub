---
course: xu-ly-du-lieu
lecture: bai-12-truc-quan-hoa-co-ban
section: lecture
title: "Trực quan hóa cơ bản"
prerequisites: ["gia-tri-thieu", "thong-ke-mo-ta"]
lessonStatus: ready
description: "Trực quan hóa khoa học với Matplotlib: Kiến trúc Figure và Axes, bốn dạng biểu đồ nền tảng, cơ chế chia khoảng histogram và nguyên tắc trung thực thị giác."
---

Một bảng dữ liệu chứa hàng chục nghìn con số có thể ẩn giấu những tri thức vô giá, nhưng bộ não con người không được tiến hóa để đọc hiểu các ma trận số học khô khốc một cách trực quan. Trực quan hóa dữ liệu không đơn thuần là việc vẽ những bức tranh minh họa bắt mắt. Về bản chất khoa học, đây là quá trình **mã hóa thị giác thông tin định lượng (Visual Encoding of Quantitative Information)**, biến các giá trị toán học trừu tượng thành các thuộc tính không gian và hình học mà mắt người có thể tiếp nhận và phân tích tức thì.

Các nghiên cứu kinh điển về nhận thức thị giác (tiêu biểu là công trình của Cleveland và McGill năm 1984) đã chứng minh rằng: Mắt người phán đoán vị trí trên cùng một thang đo và so sánh chiều dài thanh với độ chính xác cao nhất. Ngược lại, việc ước lượng diện tích, góc nghiêng hay độ đậm nhạt của màu sắc thường có sai số nhận thức lớn hơn rất nhiều. Do đó, việc lựa chọn dạng biểu đồ nào hoàn toàn không phụ thuộc vào cảm tính thẩm mỹ cá nhân, mà được quyết định bởi bản chất cấu trúc của dữ liệu và thông điệp phân tích bạn muốn truyền tải.

Bài học này xây dựng nền tảng vững chắc về trực quan hóa dữ liệu với thư viện Matplotlib trong Python: Làm chủ kiến trúc hướng đối tượng của Figure và Axes, phân định rạch ròi bốn dạng biểu đồ cơ bản, giải mã cơ chế toán học của phép chia khoảng trong histogram, và thiết lập kỷ luật kiểm thử cấu trúc biểu đồ bằng mã lệnh để bảo đảm tính trung thực tuyệt đối của các ấn phẩm báo cáo.

---

## 1. Bản chất câu hỏi quyết định hình thức biểu đồ

Trước khi đặt bút viết bất kỳ dòng mã vẽ đồ thị nào, người làm dữ liệu phải trả lời câu hỏi cốt lõi: *"Tôi muốn người đọc nhìn ra quy luật gì từ hình vẽ này?"*. Mỗi dạng biểu đồ được thiết kế để phục vụ một cấu trúc so sánh chuyên biệt:

| Câu hỏi phân tích | Dạng biểu đồ chuẩn mực | Kênh thị giác mã hóa | Kiểm tra dữ liệu trước khi vẽ |
| :--- | :--- | :--- | :--- |
| **So sánh độ lớn giữa các nhóm rời rạc** | Biểu đồ cột đứng hoặc thanh ngang (Bar chart) | Chiều dài của thanh phản ánh giá trị đại lượng | Danh mục các nhóm có bị trùng lặp không? Trục đo có bắt đầu từ 0 không? |
| **Theo dõi biến thiên tuần tự theo thời gian** | Biểu đồ đường (Line plot) | Vị trí điểm nối liền thể hiện xu hướng và nhịp điệu | Chuỗi thời gian đã được sắp xếp tăng dần chưa? Có bị thiếu khoảng thời gian nào không? |
| **Khám phá hình dạng phân phối của biến liên tục** | Biểu đồ tần suất (Histogram) | Diện tích và chiều cao của cột trong từng khoảng giá trị | Số lượng khoảng chia (bins), các giá trị biên và sự hiện diện của phân phối nhiều đỉnh |
| **Khảo sát mối quan hệ hiệp biến giữa hai biến số** | Biểu đồ phân tán (Scatter plot) | Tọa độ không gian hai chiều $(x, y)$ của từng quan sát | Đơn vị hai trục, hiện tượng các điểm bị đè khít lên nhau (overplotting) |

### Phân biệt rạch ròi giữa Biểu đồ cột (Bar chart) và Histogram

Đây là hai dạng đồ thị mà người mới học thường xuyên nhầm lẫn vì thoạt nhìn cả hai đều bao gồm những chiếc cột hình chữ nhật. Tuy nhiên, cấu trúc toán học của chúng hoàn toàn khác nhau:

- **Biểu đồ cột (Bar chart)**: Trục hoành là tập hợp các **danh mục rời rạc (categorical variables)**, ví dụ như tên các quận huyện hay nhóm sản phẩm. Giữa các nhóm này không có khoảng cách toán học liên tục. Bạn hoàn toàn có thể hoán đổi vị trí của các quận mà không làm thay đổi bản chất dữ liệu. Các cột luôn được vẽ tách rời nhau bằng một khoảng cách hình học để nhấn mạnh tính phân nhóm độc lập. Độ rộng của thanh hoàn toàn tùy ý và chỉ có chiều dài là mang thông tin định lượng.
- **Biểu đồ tần suất (Histogram)**: Trục hoành là một **trục số thực liên tục (continuous numeric axis)**. Mỗi cột đại diện cho một khoảng giá trị số học (gọi là bin). Vị trí và thứ tự của các khoảng bị khóa cứng theo thứ tự từ bé đến lớn của trục số. Các cột nằm san sát, dính liền kề nhau. Độ rộng của cột đại diện cho khoảng biến thiên số học $\Delta x$, và diện tích của cột phản ánh số lượng hoặc tỷ lệ quan sát rơi vào khoảng đó.

---

## 2. Kiến trúc hướng đối tượng của Matplotlib: Figure và Axes

Trong Matplotlib, ta có thể gọi các hàm vẽ toàn cục theo phong cách MATLAB (`plt.plot`, `plt.bar`). Tuy nhiên, trong môi trường kỹ nghệ dữ liệu chuyên nghiệp và các đường ống tự động hóa, chuẩn mực bắt buộc là sử dụng **giao diện hướng đối tượng (Object-Oriented API)** tường minh.

Kiến trúc này phân tách rõ hai thực thể nền tảng:
- **`Figure`**: Đại diện cho toàn bộ khung tranh vật lý, bao gồm kích thước khung hình (tính bằng inch), độ phân giải xuất bản (DPI), màu nền và tất cả các đồ thị con nằm bên trong.
- **`Axes`**: Đại diện cho một hệ tọa độ cụ thể nằm trên Figure. Một đối tượng Axes sở hữu trục hoành (X axis), trục tung (Y axis), lưới tọa độ, vạch chia (ticks), nhãn và toàn bộ các đối tượng hình học (đường nét, hình chữ nhật). Một Figure có thể chứa một hoặc nhiều Axes.

Hàm `plt.subplots` là điểm khởi đầu chuẩn mực để khởi tạo đồng thời cả Figure và Axes:

```python
import matplotlib.pyplot as plt
import pandas as pd

# Thiết lập phong cách tối giản học thuật
plt.rcParams.update({
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.25,
    "font.size": 11
})

thong_ke = pd.Series([12, 8, 5], index=["Sách", "Vở", "Bút"])

# Khởi tạo Figure và Axes tường minh
fig, ax = plt.subplots(figsize=(6, 3.8), dpi=150)

# Vẽ dữ liệu lên Axes
thanh = ax.bar(thong_ke.index, thong_ke.values, color="#1E93AB", width=0.55)

# BẮT BUỘC: Khóa trục tung bắt đầu từ 0
ax.set_ylim(bottom=0)

# Ghi nhãn và tiêu đề nêu thông điệp
ax.set_title("Số lượng văn phòng phẩm bán ra trong ngày", pad=12, fontweight="bold")
ax.set_ylabel("Số sản phẩm (chiếc)")
ax.bar_label(thanh, padding=3)

fig.tight_layout()
fig.savefig("van_phong_pham.png", dpi=150, bbox_inches="tight")
plt.close(fig)
```

---

## 3. Nguyên tắc trung thực thị giác: Trục tung bắt đầu từ 0 và cạm bẫy cắt cụt trục

Khi nhìn vào một biểu đồ cột (hoặc thanh ngang), não bộ con người tự động mã hóa thông tin dựa trên **chiều dài hình học của thanh** so với đường cơ sở (*baseline*).

Giả sử tỷ lệ hài lòng của ba dịch vụ là $93.5\%$, $94.8\%$ và $97.2\%$.
Nếu một người vô tình hay hữu ý cắt cụt trục tung (Truncated Axis), ép trục Y chỉ chạy từ $92\%$ đến $98\%$:
- Phần hiển thị của cột $93.5\%$ chỉ có chiều cao là $93.5 - 92 = 1.5$ đơn vị.
- Phần hiển thị của cột $97.2\%$ có chiều cao là $97.2 - 92 = 5.2$ đơn vị.

Mắt người nhìn vào sẽ thấy cột thứ ba cao gấp hơn $3.4$ lần cột thứ nhất, tạo ra cảm giác về một sự vượt trội thần kỳ. Trong khi thực tế, khoảng cách chênh lệch chỉ vỏn vẹn $3.7$ điểm phần trăm.

<DataDiagram name="truncated-axis" />

**Nguyên tắc đạo đức nghề nghiệp**: Đối với biểu đồ cột và thanh ngang, trục đo độ dài bắt buộc phải bắt đầu từ mốc 0 tuyệt đối. Cắt cụt trục tung của biểu đồ cột là hành vi ngụy tạo thị giác thiếu trung thực.
*Ngoại lệ*: Với biểu đồ đường (Line plot) theo dõi biến thiên theo thời gian của các chỉ số sinh học hay kinh tế vĩ mô (như thân nhiệt bệnh nhân hay chỉ số chứng khoán), việc thu hẹp trục tung là hợp lệ vì mắt người theo dõi vị trí và độ dốc của đường, nhưng biểu đồ bắt buộc phải ghi chú rõ ràng về thang đo.

---

## 4. Cơ chế chia khoảng của Histogram và hiện tượng phân phối hai đỉnh

Khi dựng biểu đồ histogram, các mốc biên khoảng dữ liệu được chia theo quy tắc toán học nửa mở:
- Các khoảng từ đầu đến áp chót là nửa mở $[a, b)$: Nhận giá trị tại biên trái $a$, loại trừ giá trị tại biên phải $b$.
- Khoảng cuối cùng là khoảng đóng $[c, d]$: Nhận cả hai đầu mút biên $c$ và $d$.

### Cạm bẫy giá trị trung bình trước phân phối hai đỉnh (Bimodal Distribution)

Trong phân tích số ngày mở lịch đón khách trong năm (`availability_365`) của các chỗ ở trên nền tảng Airbnb, một hiện tượng kinh điển thường xuất hiện:
- Có hàng trăm chỗ ở có `availability_365 == 0` (chủ nhà khóa lịch hoàn toàn, phòng ngừng hoạt động hoặc đã kín chỗ).
- Có hàng nghìn chỗ ở có `availability_365 >= 360` (chủ nhà mở lịch quanh năm như một cơ sở kinh doanh chuyên nghiệp).
- Rất ít chỗ ở nằm ở khoảng giữa (mở lịch vài chục hoặc vài trăm ngày).

Khi đó, phân phối dữ liệu có **hai đỉnh nhọn ở hai đầu cực trị** (Bimodal Distribution):

$$
\begin{aligned}
\text{Nhóm khóa lịch hoàn toàn: } & X = 0 \\
\text{Nhóm kinh doanh quanh năm: } & X \approx 365
\end{aligned}
$$

Nếu người phân tích ngây thơ tính giá trị trung bình cộng:
$$
\bar{X} \approx \frac{0 \times N_1 + 365 \times N_2}{N_1 + N_2} \approx 180 \text{ ngày}
$$
Con số trung bình 180 ngày là một **con số ảo tưởng hoàn toàn vô nghĩa**. Trong thực tế, hầu như không có chủ nhà nào mở lịch nửa năm rồi đóng nửa năm. Việc chỉ báo cáo một con số trung bình đơn độc sẽ che giấu hoàn toàn bản chất phân hóa sâu sắc của hai nhóm hành vi kinh doanh. Một histogram với số khoảng đủ chi tiết là công cụ duy nhất phơi bày sự thật này.

---

## 5. Hệ thống bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 12) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 6. Tổng kết và Đọc thêm

| Dạng biểu đồ | Cấu trúc toán học | Quy tắc bắt buộc & Cạm bẫy |
| :--- | :--- | :--- |
| **Biểu đồ cột (`bar`, `barh`)** | Danh mục rời rạc; chiều dài mã hóa độ lớn | Trục đo chiều dài bắt buộc phải bắt đầu từ 0; sắp xếp thứ tự hợp lý trước khi vẽ. |
| **Biểu đồ đường (`plot`)** | Chuỗi thứ tự liên tục; vị trí và độ dốc | Không nối qua khoảng thời gian bị khuyết thiếu; ghi rõ nhãn thời gian và đơn vị. |
| **Histogram (`hist`)** | Biến số thực liên tục; diện tích mã hóa tần suất | Hiểu quy ước nửa mở $[a, b)$; nhận diện phân phối hai đỉnh để tránh bẫy giá trị trung bình ảo. |
| **Kiểm thử tự động** | Thuộc tính của `Axes` (`lines`, `patches`, `ylim`) | Dùng `assert` kiểm tra tiêu đề thông điệp, nhãn trục và gốc 0 ngay trong đường ống CI/CD. |

### Tài liệu tham khảo học thuật

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 9: Plotting and Visualization](https://wesmckinney.com/book/plotting-and-visualization).
- Tài liệu chính thức Matplotlib: [Object-Oriented API Guide](https://matplotlib.org/stable/users/explain/quick_start.html).
- Edward R. Tufte, *The Visual Display of Quantitative Information*, Graphics Press, 2001.
- William S. Cleveland & Robert McGill, *Graphical Perception: Theory, Experimentation, and Application*, JASA, 1984.
- Hệ thống bài giảng thực hành: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
