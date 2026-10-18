---
course: xu-ly-du-lieu
lecture: bai-12-truc-quan-hoa-co-ban
section: lecture
title: "Trực quan hóa dữ liệu và đọc biểu đồ"
prerequisites: ["dataframe", "thong-ke-mo-ta"]
lessonStatus: ready
hasChapterExercises: true
description: "Kiến trúc hướng đối tượng của Matplotlib, trực quan hóa thống kê với pandas và Seaborn, phản biện biểu đồ sai lệch, nguyên tắc trung thực thị giác, bản đồ phân vùng choropleth và tương tác."
---


<div class="lecture-notes-content">

Một bảng dữ liệu chứa hàng chục nghìn con số có thể ẩn giấu những tri thức vô giá, nhưng bộ não con người không được tiến hóa để đọc hiểu các ma trận số học khô khốc một cách trực quan. Trực quan hóa dữ liệu không đơn thuần là việc vẽ những bức tranh minh họa bắt mắt. Về bản chất khoa học, đây là quá trình **mã hóa thị giác thông tin định lượng (Visual Encoding of Quantitative Information)**, biến các giá trị toán học trừu tượng thành các thuộc tính không gian và hình học mà mắt người có thể tiếp nhận và phân tích tức thì.

Các nghiên cứu kinh điển về nhận thức thị giác (tiêu biểu là công trình của William Cleveland và Robert McGill năm 1984) đã chứng minh rằng: Mắt người phán đoán vị trí trên cùng một thang đo và so sánh chiều dài thanh với độ chính xác cao nhất. Trái lại, việc ước lượng diện tích, góc nghiêng hay độ đậm nhạt của màu sắc thường có sai số nhận thức lớn hơn rất nhiều. Do đó, việc lựa chọn dạng biểu đồ nào hoàn toàn không phụ thuộc vào cảm tính thẩm mỹ cá nhân, mà được quyết định bởi bản chất cấu trúc của dữ liệu và thông điệp phân tích bạn muốn truyền tải.

Bài học này cung cấp nền tảng bài bản về trực quan hóa dữ liệu trong Python bằng kiến trúc hướng đối tượng của Matplotlib. Người học sẽ thực hành vẽ các biểu đồ thống kê với pandas và Seaborn, tìm hiểu cơ chế ước lượng mật độ, và rèn luyện kỹ năng phản biện biểu đồ nhằm bảo đảm tính trung thực của các ấn phẩm phân tích.

---

## 1. Sơ lược về giao diện API của Matplotlib

Thư viện Matplotlib là nền móng của toàn bộ hệ sinh thái trực quan hóa dữ liệu trong Python. Mặc dù Matplotlib cung cấp giao diện toàn cục theo phong cách MATLAB (`plt.plot`), trong môi trường kỹ nghệ dữ liệu chuyên nghiệp và các đường ống tự động hóa, chuẩn mực bắt buộc là sử dụng **giao diện hướng đối tượng (Object-Oriented API)** tường minh.

### 1.1. Kiến trúc Figure và Subplots

Kiến trúc hướng đối tượng phân tách rạch ròi hai thực thể nền tảng:
- **`Figure`**: Đại diện cho toàn bộ khung tranh vật lý, bao gồm kích thước khung hình (tính bằng inch `figsize`), độ phân giải xuất bản (`dpi`), màu nền và toàn bộ các biểu đồ con bên trong.
- **`Axes`**: Đại diện cho một hệ tọa độ cụ thể nằm trên Figure. Một đối tượng Axes sở hữu trục hoành ($X$), trục tung ($Y$), lưới tọa độ, vạch chia (*ticks*), nhãn và toàn bộ các đối tượng hình học (đường nét, cột, điểm phân tán). Một Figure có thể chứa một hoặc nhiều Axes.

Hàm `plt.subplots()` là điểm khởi đầu chuẩn mực để khởi tạo đồng thời cả Figure và lưới các Axes:

```python
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Khởi tạo Figure và lưới 2x2 gồm 4 Axes
fig, axes = plt.subplots(2, 2, figsize=(8, 6), sharex=False, sharey=False)

# Vẽ dữ liệu lên từng hệ tọa độ độc lập
axes[0, 0].hist(np.random.standard_normal(200), bins=20, color="#1E93AB", alpha=0.6)
axes[0, 0].set_title("Histogram biến chuẩn")

axes[0, 1].scatter(np.arange(30), np.arange(30) + 3 * np.random.standard_normal(30), color="#D65A31")
axes[0, 1].set_title("Biểu đồ phân tán")

axes[1, 0].plot(np.random.standard_normal(50).cumsum(), color="#393E46", linestyle="--")
axes[1, 0].set_title("Đường ngẫu nhiên")

axes[1, 1].bar(["Nhóm A", "Nhóm B", "Nhóm C"], [15, 28, 19], color="#2E7D32")
axes[1, 1].set_title("So sánh độ lớn")

fig.tight_layout()
plt.close(fig)
```

### 1.2. Căn chỉnh khoảng cách với `subplots_adjust` và `tight_layout`

Mặc định, Matplotlib để lại các khoảng trống nhất định xung quanh các biểu đồ con. Phương thức `fig.tight_layout()` tự động căn chỉnh lề để các nhãn trục không bị đè lên nhau. Khi cần tinh chỉnh thủ công khoảng cách giữa các khung vẽ, ta sử dụng:
```python
fig.subplots_adjust(left=0.1, right=0.95, bottom=0.1, top=0.9, wspace=0.3, hspace=0.3)
```
Trong đó, `wspace` và `hspace` kiểm soát tỷ lệ khoảng cách theo chiều ngang và chiều dọc giữa các Axes.

### 1.3. Màu sắc, điểm đánh dấu và kiểu đường nét

Khi vẽ biểu đồ đường hoặc đồ thị điểm, các tham số định dạng thẩm mỹ bao gồm:
- `color`: Tên màu chuẩn (`"red"`, `"teal"`), chữ cái viết tắt (`"k"` cho màu đen, `"b"` cho màu xanh dương), hoặc mã màu Hex (`"#1E93AB"`).
- `linestyle`: Kiểu nét vẽ (`"-"` nét liền, `"--"` nét đứt, `":"` nét chấm, `"-."` nét gạch chấm).
- `marker`: Ký hiệu điểm đánh dấu (`"o"` hình tròn, `"s"` hình vuông, `"^"` hình tam giác, `"x"` dấu nhân).
- `alpha`: Độ trong suốt từ $0{,}0$ (trong suốt hoàn toàn) đến $1{,}0$ (đặc hoàn toàn), vũ khí chủ lực để xử lý hiện tượng chồng lấn điểm (*Overplotting*).

### 1.4. Vạch chia, nhãn và chú giải (Ticks, Labels, and Legends)

Để một biểu đồ có thể tự đứng được mà không cần người thuyết minh, mọi trục tọa độ đều phải được ghi nhãn rõ ràng kèm đơn vị đo lường:
- `ax.set_xticks()` và `ax.set_xticklabels()`: Định vị các mốc vạch chia và gán nhãn văn bản (hỗ trợ tham số `rotation=30` khi nhãn quá dài).
- `ax.set_xlabel()`, `ax.set_ylabel()`: Tên đại lượng và đơn vị đo lường.
- `ax.set_title()`: Tiêu đề nêu bật thông điệp phân tích của biểu đồ.
- `ax.legend(loc="best")`: Thêm hộp chú giải giải thích ý nghĩa của từng đường vẽ dựa trên tham số `label` đã gán.

### 1.5. Chú thích và vẽ hình học trên Subplot

Bên cạnh các đường vẽ chính, việc dẫn dắt ánh nhìn của người đọc đến các sự kiện đặc biệt (như mốc khủng hoảng kinh tế hoặc điểm bão hòa) được thực hiện bằng chú thích:
- `ax.text(x, y, chuoi)`: Vẽ chuỗi văn bản tại tọa độ $(x, y)$.
- `ax.annotate()`: Vẽ đoạn văn bản kèm theo mũi tên chỉ trực tiếp vào điểm dữ liệu quan trọng:

```python
fig, ax = plt.subplots(figsize=(6, 3.5))
ax.plot([1, 2, 3, 4, 5], [10, 14, 25, 18, 12], marker="o", color="#1E93AB")

# Chỉ mũi tên vào đỉnh cực đại:
ax.annotate(
    "Đỉnh doanh thu",
    xy=(3, 25),
    xytext=(3.5, 23),
    arrowprops=dict(facecolor="black", shrink=0.08, width=1.5, headwidth=6)
)
ax.set_ylim(bottom=0)
plt.close(fig)
```

Ngoài ra, ta có thể bổ sung các hình học trực quan như đường thẳng tham chiếu ngang/dọc (`ax.axhline()`, `ax.axvline()`) hoặc các mảng hình học từ `matplotlib.patches` (như `Rectangle`, `Circle`) thông qua phương thức `ax.add_patch()`.

### 1.6. Xuất bản biểu đồ ra tệp với `savefig`

Phương thức `fig.savefig()` cho phép lưu biểu đồ xuống đĩa cứng với hai họ định dạng chính:
- **Định dạng điểm ảnh (Raster Image - PNG, JPEG)**: Biểu diễn hình ảnh bằng lưới các pixel. Thích hợp cho các biểu đồ chứa hàng triệu điểm dữ liệu phân tán. Cần thiết lập `dpi=300` để bảo đảm độ sắc nét khi in ấn.
- **Định dạng vector (Vector Image - SVG, PDF)**: Biểu diễn hình ảnh bằng các phương trình toán học về đường cong và nét vẽ. Cho phép phóng to thu nhỏ tùy ý mà không bao giờ bị vỡ hạt, lý tưởng cho các bài báo khoa học và tài liệu web.
- Tham số `bbox_inches="tight"`: Tự động cắt bỏ các khoảng trắng thừa ở viền ngoài bức tranh.

### 1.7. Cấu hình giao diện toàn cục với `rcParams`

Để toàn bộ các biểu đồ trong dự án tuân theo một ngôn ngữ thiết kế đồng nhất, Matplotlib cho phép cấu hình các tham số hệ thống thông qua `plt.rcParams.update()`:

```python
plt.rcParams.update({
    "font.size": 10,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.3,
    "figure.autolayout": True
})
```

---

## 2. Vẽ biểu đồ với pandas và Seaborn

Trong khi Matplotlib đóng vai trò là động cơ vẽ cấp thấp, pandas và Seaborn cung cấp các giao diện cấp cao được thiết kế riêng để tương tác trực tiếp với cấu trúc DataFrame.

### 2.1. Vẽ nhanh với pandas `.plot`

Các đối tượng Series và DataFrame tích hợp sẵn thuộc tính `.plot`:
- Biểu đồ đường: Dùng `df.plot(kind="line")` hoặc `df.plot()`.
- Biểu đồ cột: Dùng `s.plot.bar()` (cột đứng) hoặc `s.plot.barh()` (thanh ngang). Tham số `stacked=True` cho phép vẽ biểu đồ cột chồng tích lũy.

```python
df_doanh_so = pd.DataFrame({
    "Chi_nhanh_A": [120, 150, 180],
    "Chi_nhanh_B": [90, 140, 160]
}, index=["Quý 1", "Quý 2", "Quý 3"])

ax = df_doanh_so.plot.bar(figsize=(6, 4), color=["#1E93AB", "#D65A31"])
ax.set_ylabel("Doanh thu (triệu đồng)")
plt.close(ax.get_figure())
```

### 2.2. Biểu đồ tần suất và ước lượng mật độ nhân (KDE)

- **Histogram**: Dùng `s.plot.hist(bins=20)` chia dữ liệu thành các khoảng và đếm tần số xuất hiện.
- **Biểu đồ mật độ (Density Plot / KDE)**: Dùng `s.plot.kde()` hoặc `sns.kdeplot()` làm mịn phân phối dữ liệu rời rạc thành một đường cong liên tục bằng phương pháp Ước lượng Mật độ Nhân (*Kernel Density Estimation*). Mỗi quan sát thực tế được mô hình hóa bằng một hàm nhân chuẩn hóa thu nhỏ (thường là phân phối Gauss), và đường cong mật độ tổng thể là tổng tích lũy của toàn bộ các hàm nhân này.

Tham số độ rộng băng thông (*bandwidth*, điều khiển bằng `bw_adjust` trong Seaborn) quyết định mức độ làm mịn của đường cong. Băng thông quá hẹp sẽ khiến đường cong gồ ghề và bắt chước nhiễu ngẫu nhiên, trong khi băng thông quá rộng sẽ làm lu mờ các đỉnh phân phối quan trọng:

```python
import seaborn as sns

du_lieu_mau = np.array([1.2, 1.5, 1.8, 3.8, 4.0, 4.2, 4.5, 4.8])
fig, ax = plt.subplots(figsize=(6, 3.5))

# So sánh băng thông chuẩn và băng thông nhạy dao động
sns.kdeplot(du_lieu_mau, bw_adjust=1.0, label="Băng thông chuẩn (bw_adjust=1.0)", color="#1E93AB", ax=ax)
sns.kdeplot(du_lieu_mau, bw_adjust=0.5, label="Băng thông hẹp (bw_adjust=0.5)", color="#D65A31", linestyle="--", ax=ax)
ax.set_title("Ước lượng mật độ nhân với các mức băng thông khác nhau")
ax.legend()
plt.close(fig)
```

### 2.3. Biểu đồ phân tán, đồ thị hồi quy và ma trận tương quan

- `sns.scatterplot(x="bien_x", y="bien_y", hue="nhom", data=df)`: Thể hiện mối quan hệ giữa hai biến số thực, hỗ trợ phân biệt các nhóm đối tượng bằng kênh màu sắc `hue`.
- `sns.regplot()`: Tự động ước lượng và vẽ đường hồi quy tuyến tính đi kèm dải tin cậy $95\%$ (*Confidence Interval Band*), giúp đánh giá trực quan hướng vận động và độ chặt chẽ của mối liên hệ giữa hai biến số.
- `sns.boxplot()`: Biểu diễn phân phối định lượng qua các tứ phân vị và nhận diện giá trị ngoại lai, kết hợp tham số `hue` để phân rã thêm một chiều phân loại phụ.

```python
df_tips = pd.DataFrame({
    "ngay": ["Thứ 5", "Thứ 5", "Thứ 6", "Thứ 6", "Thứ 7", "Thứ 7", "CN", "CN"],
    "tong_hoa_don": [18.5, 25.0, 22.0, 30.5, 35.0, 42.0, 38.0, 48.5],
    "thoi_gian": ["Trưa", "Tối", "Trưa", "Tối", "Tối", "Tối", "Trưa", "Tối"]
})

fig, ax = plt.subplots(figsize=(6, 4))
sns.boxplot(data=df_tips, x="ngay", y="tong_hoa_don", hue="thoi_gian", palette="Set2", ax=ax)
ax.set_title("Phân bố hóa đơn theo ngày và thời gian với kênh màu sắc hue")
ax.set_ylabel("Tổng hóa đơn (USD)")
plt.close(fig)
```

- `sns.heatmap()`: Trực quan hóa ma trận số học hoặc ma trận hệ số tương quan bằng bản đồ nhiệt màu, hiển thị trực tiếp giá trị số trên từng ô qua tham số `annot=True`:

```python
df_tuong_quan = pd.DataFrame({
    "Doanh_thu": [100, 150, 200, 250, 300],
    "Chi_phi_QC": [10, 18, 25, 32, 40],
    "So_don_hang": [50, 70, 95, 110, 130]
})
ma_tran_corr = df_tuong_quan.corr()

fig, ax = plt.subplots(figsize=(5, 4))
sns.heatmap(ma_tran_corr, annot=True, cmap="Blues", fmt=".2f", vmin=-1, vmax=1, ax=ax)
ax.set_title("Ma trận tương quan với Seaborn Heatmap")
plt.close(fig)
```

### 2.4. Lưới biểu đồ khía cạnh với `FacetGrid` và `catplot`

Khi tập dữ liệu chứa nhiều chiều phân loại, việc nhồi nhét tất cả vào một biểu đồ duy nhất sẽ gây quá tải thị giác (*Visual Clutter*). Seaborn giải quyết bài toán này bằng kỹ thuật lưới biểu đồ khía cạnh:
- `sns.catplot(x=..., y=..., hue=..., data=..., kind="box"|"violin"|"bar")`: Trực quan hóa dữ liệu phân loại với các kiểu hiển thị đa dạng như biểu đồ hộp (*Boxplot*) hay biểu đồ vĩ cầm (*Violin plot*).
- `sns.FacetGrid`: Tạo một ma trận gồm nhiều biểu đồ nhỏ (*Small Multiples*), trong đó mỗi biểu đồ con khảo sát cùng một mối quan hệ nhưng trên một phân khúc dữ liệu riêng biệt:

```python
df_khao_sat = pd.DataFrame({
    "chi_phi": [15, 22, 40, 18, 35, 50, 12, 28],
    "tien_tip": [2.5, 3.0, 6.0, 2.8, 5.0, 8.5, 1.8, 4.2],
    "buoi": ["Trưa", "Tối", "Tối", "Trưa", "Tối", "Tối", "Trưa", "Tối"],
    "gioi_tinh": ["Nam", "Nữ", "Nam", "Nữ", "Nam", "Nữ", "Nam", "Nữ"]
})

g = sns.FacetGrid(df_khao_sat, col="buoi", row="gioi_tinh", margin_titles=True)
g.map(sns.scatterplot, "chi_phi", "tien_tip", color="#1E93AB")
plt.close(g.fig)
```

---

## 3. Phản biện biểu đồ và nguyên tắc trung thực thị giác

Trực quan hóa dữ liệu có vai trò định hướng nhận thức quan trọng. Một biểu đồ được thiết kế sai lệch có thể phóng đại những chênh lệch nhỏ, hoặc ngược lại che giấu đi những biến động đáng lưu tâm trong dữ liệu.

### 3.1. Phản biện ba cạm bẫy trực quan hóa kinh điển

#### Cạm bẫy 1: Cắt cụt trục tung của biểu đồ cột (Truncated Y-axis)
- **Cơ chế**: Khi nhìn vào biểu đồ cột hoặc thanh ngang, mắt người tự động mã hóa độ lớn dựa trên **chiều dài hình học của thanh** so với đường cơ sở (*baseline*).
- **Hệ quả**: Nếu tỷ lệ của hai đơn vị là $94\%$ và $98\%$, nhưng người vẽ cắt cụt trục tung bắt đầu từ mốc $90\%$: Thanh thứ hai sẽ có chiều dài hiển thị là $98 - 90 = 8$ đơn vị, gấp đôi thanh thứ nhất ($94 - 90 = 4$ đơn vị). Người đọc dễ lầm tưởng rằng đơn vị thứ hai vượt trội gấp đôi, trong khi khoảng cách thực tế chỉ là $4$ điểm phần trăm.
- **Nguyên tắc trực quan**: Đối với biểu đồ cột và thanh ngang, trục đo chiều dài bắt buộc phải xuất phát từ mốc $0$ để bảo toàn tỷ lệ trực quan:

```python
df_so_sanh = pd.DataFrame({
    "don_vi": ["Đơn vị A", "Đơn vị B"],
    "ty_le": [94.0, 98.0]
})

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 3.5))

# Biểu đồ sai lệch: Trục tung bị cắt cụt từ 90 làm méo mó trực quan
ax1.bar(df_so_sanh["don_vi"], df_so_sanh["ty_le"], color=["#1E93AB", "#D65A31"])
ax1.set_ylim(bottom=90, top=100)
ax1.set_title("Trục tung cắt cụt (Phóng đại chênh lệch)")
ax1.set_ylabel("Tỷ lệ (%)")

# Biểu đồ chuẩn mực: Trục tung bắt đầu từ 0 bảo toàn tỷ lệ chiều dài
ax2.bar(df_so_sanh["don_vi"], df_so_sanh["ty_le"], color=["#1E93AB", "#D65A31"])
ax2.set_ylim(bottom=0, top=100)
ax2.set_title("Trục tung từ 0 (Trung thực)")
ax2.set_ylabel("Tỷ lệ (%)")

fig.tight_layout()
plt.close(fig)
```

#### Cạm bẫy 2: Cạm bẫy trục tung kép (Dual Y-axis)
- **Cơ chế**: Đặt hai biến số có thang đo và đơn vị hoàn toàn khác nhau lên cùng một biểu đồ đường với hai trục tung bên trái và bên phải.
- **Hệ quả**: Người vẽ có thể tùy tiện co giãn khoảng giá trị của hai trục tung để ép hai đường cong chạy song song hoặc cắt nhau tại bất kỳ điểm nào, ngụy tạo mối tương quan hình thức giữa hai biến số vốn không liên quan.
- **Giải pháp**: Thay vì dùng trục kép, hãy vẽ hai biểu đồ con nằm xếp chồng theo chiều dọc (*Stacked Subplots*) có chung trục hoành thời gian, hoặc chuyển đổi các đại lượng về dạng chỉ số tăng trưởng tương đối (phần trăm thay đổi so với mốc cơ sở).

#### Cạm bẫy 3: Biểu đồ tròn quá nhiều lát và đồ thị 3D giả lập
- **Cơ chế**: Biểu đồ tròn mã hóa dữ liệu bằng góc ở tâm và diện tích hình quạt. Khi biểu đồ tròn có nhiều lát cắt hoặc các lát có kích thước gần tương đồng, mắt người rất khó so sánh chính xác góc và diện tích hình quạt. Đặc biệt, việc lạm dụng hiệu ứng 3D làm biến dạng góc nghiêng: Các lát cắt nằm ở phía trước góc nhìn phối cảnh sẽ bị phóng đại nhân tạo, trong khi các lát cắt ở phía sau bị thu nhỏ lại.
- **Giải pháp**: Luôn thay thế biểu đồ tròn phức tạp bằng một biểu đồ thanh ngang được sắp xếp thứ tự giảm dần.

### 3.2. Tỷ lệ dữ liệu trên mực in

Trong tác phẩm *The Visual Display of Quantitative Information*, Edward Tufte giới thiệu khái niệm **Tỷ lệ dữ liệu trên mực in (Data-to-Ink Ratio)**. Khái niệm này biểu thị tỷ lệ giữa lượng mực dùng để truyền tải thông tin dữ liệu cốt lõi so với tổng lượng mực tạo nên toàn bộ biểu đồ. Một biểu đồ được thiết kế hiệu quả cần tối ưu hóa tỷ lệ này bằng cách:
- Loại bỏ các chi tiết trang trí rườm rà không mang thông tin (*Chartjunk*), chẳng hạn như bóng đổ 3D, họa tiết hoa văn không cần thiết, và đường viền khung tranh dày đặc.
- Tiết chế độ đậm của các đường lưới tọa độ (*Gridlines*): Đường lưới chỉ đóng vai trò hỗ trợ đọc số liệu, không được phép lấn át các đường biểu diễn dữ liệu chính.

### 3.3. Bản đồ phân vùng địa lý (Choropleth Maps) và cạm bẫy diện tích

Bản đồ Choropleth tô màu các vùng địa lý (như tỉnh thành, quốc gia) theo một chỉ số định lượng (chẳng hạn thu nhập bình quân, tỷ lệ thất nghiệp hoặc mật độ dân số). Quy trình kỹ thuật kết hợp cấu trúc hình học không gian (GeoJSON hoặc Shapefile) với bảng dữ liệu thống kê thông qua phương thức ghép nối dữ liệu.

Tuy nhiên, bản đồ Choropleth cần được đọc cẩn trọng trước **Cạm bẫy diện tích địa lý (Geographic Area Trap)**:
- Trên bản đồ, những khu vực có diện tích đất đai rộng lớn (như vùng rừng núi hoặc hoang mạc) sẽ chiếm trọn thị giác của người xem nhờ diện tích mảng màu rất lớn.
- Ngược lại, các trung tâm đô thị đông dân cư và có đóng góp kinh tế trọng yếu lại chỉ là những chấm nhỏ li ti khó nhìn thấy.
- **Nguyên tắc nhận thức**: Diện tích đất đai không đồng nghĩa với tầm quan trọng của dữ liệu. Cần cân nhắc sử dụng bản đồ bong bóng (*Bubble Map*) hoặc bản đồ biến dạng diện tích (*Cartogram*) khi nghiên cứu các chỉ số gắn liền với dân số.

### 3.4. Trực quan hóa tương tác với Plotly Express

Biểu đồ tĩnh tạo bởi Matplotlib và Seaborn phù hợp cho các báo cáo dạng in ấn và tài liệu học thuật. Trong khi đó, các thư viện trực quan hóa tương tác như Plotly Express cung cấp trải nghiệm khám phá linh hoạt trên môi trường web:
- **Khám phá chi tiết (Hover tooltips)**: Người dùng có thể rê chuột lên từng điểm dữ liệu để đọc chính xác tọa độ, nhãn định danh và các thuộc tính phụ trợ mà không làm rối mắt bức tranh tổng thể.
- **Thao tác động (Zoom & Pan)**: Cho phép phóng to vào các cụm dữ liệu dày đặc và di chuyển qua lại giữa các khoảng thời gian.
- **Lựa chọn công cụ**: Sử dụng biểu đồ tĩnh khi cần cố định bố cục trang in và xuất bản định dạng vector, còn sử dụng biểu đồ tương tác trong các bảng điều khiển nghiệp vụ (*Dashboards*) để người dùng có thể lọc và phóng to theo nhu cầu.

---

## 4. Tổng kết

1. **Tuân thủ kiến trúc hướng đối tượng**: Khởi tạo `fig, ax = plt.subplots()` tường minh để phân định ranh giới giữa khung tranh `Figure` và hệ tọa độ `Axes`, giúp kiểm soát chặt chẽ bố cục nhiều thành phần.
2. **Khai thác Seaborn cho đồ họa thống kê**: Sử dụng `catplot` và `FacetGrid` để phân rã dữ liệu nhiều chiều thành các biểu đồ con trực quan, tránh nhồi nhét quá tải thị giác.
3. **Bảo đảm tính chuẩn mực của biểu đồ cột**: Không cắt cụt trục tung của biểu đồ cột và thanh ngang, trục đo chiều dài cần xuất phát từ mốc $0$ để bảo toàn tỷ lệ trực quan.
4. **Cảnh giác trước cạm bẫy trực quan**: Tránh sử dụng trục tung kép gây ngụy tạo tương quan, đồng thời hạn chế biểu đồ tròn quá nhiều lát và các hiệu ứng 3D làm sai lệch nhận thức hình học.
5. **Tối ưu hóa tỷ lệ dữ liệu trên mực in**: Giảm bớt các chi tiết trang trí rườm rà (*Chartjunk*) và tiết chế độ đậm của đường lưới nhằm làm nổi bật tín hiệu phân tích cốt lõi.
6. **Nhận thức ranh giới của bản đồ Choropleth**: Phân biệt rạch ròi giữa diện tích lãnh thổ địa lý với mật độ dân số hoặc quy mô kinh tế của vùng dữ liệu.

---

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 9: Plotting and Visualization](https://wesmckinney.com/book/plotting-and-visualization).
- Tài liệu chính thức Matplotlib: [Quick start guide & Artist tutorial](https://matplotlib.org/stable/users/explain/quick_start.html).
- Tài liệu chính thức Seaborn: [Statistical data visualization](https://seaborn.pydata.org/tutorial.html).
- Edward R. Tufte, *The Visual Display of Quantitative Information*, Graphics Press, 2001.
- William S. Cleveland & Robert McGill, *Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods*, Journal of the American Statistical Association, 1984.
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">



<!--@include: ../../../raw_materials/xu-ly-du-lieu/practice/visual-reading.md-->


<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-12">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-12.md-->

</section>

<section class="data-lab-set" data-lab="lab-13">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-13.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 9: Plotting and Visualization](https://wesmckinney.com/book/plotting-and-visualization).
- Tài liệu chính thức Matplotlib: [Quick start guide & Artist tutorial](https://matplotlib.org/stable/users/explain/quick_start.html).
- Tài liệu chính thức Seaborn: [Statistical data visualization](https://seaborn.pydata.org/tutorial.html).
- Edward R. Tufte, *The Visual Display of Quantitative Information*, Graphics Press, 2001.
- William S. Cleveland & Robert McGill, *Graphical Perception: Theory, Experimentation, and Application to the Development of Graphical Methods*, Journal of the American Statistical Association, 1984.
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
