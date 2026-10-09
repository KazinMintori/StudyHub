---
course: xu-ly-du-lieu
lecture: bai-12-truc-quan-hoa-co-ban
section: lecture
title: "Trực quan hóa cơ bản"
prerequisites: ["gia-tri-thieu","ky-vong"]
lessonStatus: ready
description: "Trực quan hóa khoa học với Matplotlib: kiến trúc Figure và Axes, bốn dạng biểu đồ nền tảng, cơ chế chia khoảng histogram và nguyên tắc trung thực thị giác."
---

Một bảng dữ liệu chứa hàng chục nghìn con số có thể ẩn giấu những tri thức vô giá, nhưng bộ não con người không được tiến hóa để đọc hiểu các ma trận số học khô khốc một cách trực quan. Trực quan hóa dữ liệu không đơn thuần là việc vẽ những bức tranh minh họa bắt mắt. Về bản chất khoa học, đây là quá trình **mã hóa thị giác thông tin định lượng (Visual Encoding of Quantitative Information)**, biến các giá trị toán học trừu tượng thành các thuộc tính không gian và hình học mà mắt người có thể tiếp nhận và phân tích tức thì.

Các nghiên cứu kinh điển về nhận thức thị giác (tiêu biểu là công trình của Cleveland và McGill năm 1984) đã chứng minh rằng: mắt người phán đoán vị trí trên cùng một thang đo và so sánh chiều dài thanh với độ chính xác cao nhất. Ngược lại, việc ước lượng diện tích, góc nghiêng hay độ đậm nhạt của màu sắc thường có sai số nhận thức lớn hơn rất nhiều. Do đó, việc lựa chọn dạng biểu đồ nào hoàn toàn không phụ thuộc vào cảm tính thẩm mỹ cá nhân, mà được quyết định bởi bản chất cấu trúc của dữ liệu và thông điệp phân tích bạn muốn truyền tải.

Bài học này xây dựng nền tảng vững chắc về trực quan hóa dữ liệu với thư viện Matplotlib trong Python: làm chủ kiến trúc hướng đối tượng của Figure và Axes, phân định rạch ròi bốn dạng biểu đồ cơ bản, giải mã cơ chế toán học của phép chia khoảng trong histogram, và thiết lập kỷ luật kiểm thử cấu trúc biểu đồ bằng mã lệnh để bảo đảm tính trung thực tuyệt đối của các ấn phẩm báo cáo.

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

```
Biểu đồ cắt cụt trục (92% - 98%)        Biểu đồ trung thực (0% - 100%)
[Trông cao gấp 3.5 lần!]                 [Chênh lệch thực tế rất khiêm tốn]
    ┌─┐                                      ┌─┐ ┌─┐ ┌─┐
    │ │                                      │ │ │ │ │ │
┌─┐ │ │                                      │ │ │ │ │ │
│ │ │ │                                      │ │ │ │ │ │
┴─┴─┴─┴ (Gốc = 92%)                          ┴─┴─┴─┴─┴─┴ (Gốc = 0%)
```

**Nguyên tắc đạo đức nghề nghiệp**: Đối với biểu đồ cột và thanh ngang, trục đo độ dài bắt buộc phải bắt đầu từ mốc 0 tuyệt đối. Cắt cụt trục tung của biểu đồ cột là hành vi ngụy tạo thị giác thiếu trung thực.
*Ngoại lệ*: Với biểu đồ đường (Line plot) theo dõi biến thiên theo thời gian của các chỉ số sinh học hay kinh tế vĩ mô (như thân nhiệt bệnh nhân hay chỉ số chứng khoán), việc thu hẹp trục tung là hợp lệ vì mắt người theo dõi vị trí và độ dốc của đường, nhưng biểu đồ bắt buộc phải ghi chú rõ ràng về thang đo.

---

## 4. Cơ chế chia khoảng của Histogram và hiện tượng phân phối hai đỉnh

Khi dựng biểu đồ histogram, các mốc biên khoảng dữ liệu được chia theo quy tắc toán học nửa mở:
- Các khoảng từ đầu đến áp chót là nửa mở $[a, b)$: nhận giá trị tại biên trái $a$, loại trừ giá trị tại biên phải $b$.
- Khoảng cuối cùng là khoảng đóng $[c, d]$: nhận cả hai đầu mút biên $c$ và $d$.

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

## 5. Hệ thống bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 12)

Hệ thống bài tập dưới đây mô phỏng bài toán trực quan hóa dữ liệu phục vụ báo cáo quản trị của Inside Airbnb tại Santiago. Để bảo đảm tính độc lập và khả năng tự kiểm thử, ta tạo bộ dữ liệu giả lập mô phỏng đầy đủ chuỗi thời gian, tỷ lệ nguyên căn giữa các quận và phân phối mở lịch hai đỉnh.

### Dữ liệu thực hành giả lập

```python
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Thiết lập thư mục lưu hình ảnh của pipeline
Path("figures").mkdir(exist_ok=True)

# Khởi tạo dữ liệu giả lập có kiểm soát
_QUAN = (["Santiago"] * 20 + ["Providencia"] * 12 + ["Las Condes"] * 10
         + ["Ñuñoa"] * 8 + ["Lo Barnechea"] * 6 + ["Vitacura"] * 4)
_CHU_KY_PHONG_RIENG = {"Santiago": 3, "Providencia": 4, "Las Condes": 5, "Ñuñoa": 2, "Lo Barnechea": 0, "Vitacura": 4}

DEMO_DS = pd.DataFrame({
    "id": range(101, 161),
    "neighbourhood": _QUAN,
    "room_type": ["Private room" if _CHU_KY_PHONG_RIENG[q] and k % _CHU_KY_PHONG_RIENG[q] == 1 else "Entire home/apt"
                  for k, q in enumerate(_QUAN)],
    "availability_365": [0 if k % 9 == 0 else 365 if k % 4 == 0 else (k * 37) % 300 + 20 for k in range(60)],
})

_dong = []
for k, lid in enumerate(DEMO_DS["id"]):
    for ngay in pd.date_range("2024-01-10", "2026-07-01", freq=f"{20 + k % 25}D"):
        _dong.append((lid, ngay))
DEMO_RV = pd.DataFrame(_dong, columns=["listing_id", "date"])

NGUON_DANH_GIA = "Nguồn: Dữ liệu mô phỏng chuẩn hóa Lab 12"
```

---

### Bài 1: Tổng hợp chuỗi số lượng đánh giá theo tháng của một quận

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `monthly_reviews(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series` nhận vào bảng đánh giá `rv` (`listing_id`, `date`), bảng chỗ ở `ds` (`id`, `neighbourhood`) và tên quận `quan`.

Quy trình xử lý:
1. Xác định tập các mã `id` thuộc quận `quan`.
2. Lọc các đánh giá trong `rv` có `listing_id` thuộc tập hợp đó.
3. Đưa cột `date` làm chỉ mục và lấy mẫu lại theo tháng kết thúc bằng `resample("ME").size()`.
4. **Bỏ tháng cuối cùng** (vì đây là kỳ chưa trọn vẹn của snapshot).
5. Trả về Series có chỉ mục là `DatetimeIndex` đại diện ngày cuối tháng và giá trị là số lượng đánh giá. Tuyệt đối không làm thay đổi bảng dữ liệu đầu vào.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def monthly_reviews_co_ban(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series:
    # 1. Lấy danh sách ID thuộc quận
    id_quan = ds.loc[ds["neighbourhood"] == quan, "id"]
    
    # 2. Lọc các đánh giá tương ứng
    rv_quan = rv.loc[rv["listing_id"].isin(id_quan)].copy()
    
    # 3. Tổng hợp theo tháng và loại bỏ tháng cụt cuối cùng
    thang = rv_quan.set_index("date").resample("ME").size()
    thang_tron = thang.iloc[:-1]
    
    return thang_tron
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu

```python
def monthly_reviews(rv: pd.DataFrame, ds: pd.DataFrame, quan: str) -> pd.Series:
    id_set = set(ds.loc[ds["neighbourhood"] == quan, "id"])
    return (
        rv.loc[rv["listing_id"].isin(id_set)]
        .set_index("date")
        .resample("ME")
        .size()
        .iloc[:-1]
    )
```

#### Phân tích so sánh & Trực giác bản chất
- Thao tác `.iloc[:-1]` loại bỏ tháng cuối cùng là bước bắt buộc để bảo đảm tính trung thực của chuỗi thời gian, ngăn chặn việc vẽ một điểm sụt giảm giả tạo ở cuối biểu đồ do mốc trích xuất dữ liệu diễn ra giữa chừng.
:::

---

### Bài 2: Dựng biểu đồ đường hoàn chỉnh và lưu tệp ấn phẩm

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `plot_line(thang: pd.Series, path) -> plt.Axes` nhận vào Series chuỗi thời gian theo tháng và đường dẫn tệp ảnh PNG `path`.

Yêu cầu định dạng biểu đồ:
- Khởi tạo hình mới bằng `fig, ax = plt.subplots(figsize=(9, 3.5))`.
- Vẽ đường biểu diễn bằng `ax.plot(thang.index, thang.values)`.
- Tiêu đề biểu đồ bắt buộc phải **nêu một thông điệp phân tích** (độ dài tối thiểu 15 ký tự, không đặt tên chung chung như "Biểu đồ đường").
- Trục tung phải có nhãn kèm đơn vị rõ ràng (`ax.set_ylabel(...)`).
- Chú thích nguồn dữ liệu bằng `fig.text(...)` ở góc dưới hình.
- Lưu ảnh bằng `fig.savefig(path, dpi=150, bbox_inches="tight")` và trả về đối tượng `ax`.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def plot_line(thang: pd.Series, path) -> plt.Axes:
    fig, ax = plt.subplots(figsize=(9, 3.5))
    
    # Vẽ đường số liệu chính
    ax.plot(thang.index, thang.values, color="#1E93AB", linewidth=2)
    
    # Thiết lập tiêu đề nêu thông điệp phân tích
    ax.set_title("Lượng đánh giá theo tháng tại Providencia tăng trưởng ổn định", pad=12, fontweight="bold")
    ax.set_ylabel("Số lượng đánh giá (lượt)")
    
    # Thêm chú thích nguồn ở góc dưới khung hình
    fig.text(0.99, 0.01, NGUON_DANH_GIA, ha="right", va="bottom", fontsize=9, color="#666666")
    
    # Lưu tệp đồ họa ấn phẩm
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax
```

#### Phân tích sư phạm chuyên sâu
- **Tiêu đề nêu thông điệp (Action Title)**: Thay vì đặt tiêu đề thụ động *"Biểu đồ đánh giá theo tháng"*, một tiêu đề chuyên nghiệp phải truyền tải ngay kết luận chính: *"Lượng đánh giá theo tháng tại Providencia tăng trưởng ổn định"*. Điều này giúp người đọc nắm bắt ngay thông điệp phân tích trước khi xem chi tiết các con số.
:::

---

### Bài 3: Tổng hợp bảng tỷ lệ căn hộ nguyên căn theo quận

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `share_entire(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame` nhận vào bảng chỗ ở `ds` (`id`, `neighbourhood`, `room_type`).

Yêu cầu nghiệp vụ:
- Gom nhóm theo quận `neighbourhood`.
- Tạo cột `n`: tổng số chỗ ở của quận (`size`).
- Tạo cột `pct`: tỷ lệ số chỗ ở có `room_type == "Entire home/apt"` (thang đo từ 0 đến 1, tính bằng trung bình cộng của biểu thức boolean).
- Chỉ giữ lại các quận có quy mô `n >= min_n`.
- Sắp xếp bảng theo thứ tự **`pct` tăng dần** (để khi vẽ thanh ngang, thanh dài nhất sẽ nằm ở trên cùng).
- Trả về DataFrame có chỉ mục là tên quận và đúng hai cột `n`, `pct`. Không thêm cột vào `ds` gốc.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def share_entire_co_ban(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    # 1. Tạo biến boolean tạm thời
    la_nguyen_can = ds["room_type"] == "Entire home/apt"
    
    # 2. Gom nhóm tính quy mô và tỷ lệ
    nhom = ds.groupby("neighbourhood")
    n = nhom.size()
    pct = la_nguyen_can.groupby(ds["neighbourhood"]).mean()
    
    bang = pd.DataFrame({"n": n, "pct": pct})
    
    # 3. Lọc quy mô và sắp xếp tăng dần
    bang_loc = bang.loc[bang["n"] >= min_n].sort_values("pct", ascending=True)
    return bang_loc
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Named Aggregation tinh gọn)

```python
def share_entire(ds: pd.DataFrame, min_n: int = 300) -> pd.DataFrame:
    bang = (
        ds.assign(la_nguyen_can=ds["room_type"] == "Entire home/apt")
        .groupby("neighbourhood")
        .agg(n=("id", "size"), pct=("la_nguyen_can", "mean"))
    )
    return bang.loc[bang["n"].ge(min_n)].sort_values("pct", ascending=True)
```

#### Phân tích so sánh & Trực giác bản chất
- Tận dụng tính chất số học của biến boolean trong Python: `True` tương đương 1 và `False` tương đương 0. Do đó, trung bình cộng của một cột boolean chính là tỷ lệ phần trăm các dòng thỏa mãn điều kiện.
:::

---

### Bài 4: Dựng biểu đồ thanh ngang có nhãn giá trị và trục gốc 0

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `plot_share_barh(tk: pd.DataFrame, path) -> plt.Axes` nhận vào bảng thống kê của Bài 3 (chỉ mục là tên quận, cột `pct`) và đường dẫn tệp PNG.

Yêu cầu định dạng:
- Khởi tạo khung hình mới và vẽ biểu đồ thanh ngang bằng `ax.barh`.
- Độ dài mỗi thanh là giá trị phần trăm `pct * 100` theo đúng thứ tự dòng của `tk`.
- Ghi nhãn số liệu trực tiếp trên từng thanh bằng `ax.bar_label(fmt="%.0f%%")`.
- Trục hoành bắt buộc phải **bắt đầu từ 0** (không được cắt cụt trục).
- Tiêu đề nêu thông điệp (ít nhất 15 ký tự), trục x có nhãn đơn vị `%`.
- Lưu ảnh bằng `fig.savefig(path, dpi=150, bbox_inches="tight")` và trả về `ax`.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def plot_share_barh(tk: pd.DataFrame, path) -> plt.Axes:
    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Tính độ dài thanh thang phần trăm
    gia_tri_pct = tk["pct"] * 100.0
    thanh = ax.barh(tk.index, gia_tri_pct, color="#1E93AB", height=0.6)
    
    # Hiển thị nhãn giá trị trên mỗi thanh
    ax.bar_label(thanh, fmt="%.0f%%", padding=4, fontweight="semibold")
    
    # BẮT BUỘC: Khóa trục x bắt đầu từ 0
    ax.set_xlim(left=0, right=max(gia_tri_pct.max() * 1.15, 100.0))
    
    # Định dạng tiêu đề và nhãn
    ax.set_title("Tỷ lệ chỗ ở nguyên căn chiếm ưu thế tuyệt đối ở các quận trung tâm", pad=12, fontweight="bold")
    ax.set_xlabel("Tỷ lệ căn hộ nguyên căn (%)")
    
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax
```

#### Phân tích sư phạm chuyên sâu
- Vì bảng `tk` đã được sắp xếp `pct` tăng dần ở Bài 3, khi vẽ bằng `barh`, quận có tỷ lệ cao nhất sẽ tự nhiên xuất hiện ở vị trí trên cùng của đồ thị. Mắt người đọc theo quy tắc từ trên xuống dưới sẽ tiếp cận ngay danh mục dẫn đầu.
:::

---

### Bài 5: Dựng Histogram phân tích phân phối hai đỉnh

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `plot_availability(avail: pd.Series, path, bins: int = 40) -> dict` nhận vào:
- `avail`: Series số ngày mở lịch trong năm (`availability_365`).
- `path`: Đường dẫn lưu tệp PNG.
- `bins`: Số lượng khoảng chia (mặc định bằng 40).

Yêu cầu thực thi:
- Lọc bỏ các giá trị khuyết thiếu và vẽ histogram bằng `ax.hist(avail.dropna(), bins=bins)`.
- Tiêu đề phản ánh đúng hiện tượng phân phối quan sát được (ít nhất 15 ký tự).
- Lưu ảnh bằng `fig.savefig(path, dpi=150, bbox_inches="tight")`.
- Trả về từ điển gồm ba khóa:
  - `"ax"`: Đối tượng Axes đã vẽ.
  - `"so_khoa"`: Số nguyên là số chỗ ở có đúng 0 ngày mở lịch (`avail == 0`).
  - `"so_mo_quanh_nam"`: Số nguyên là số chỗ ở có từ 360 ngày mở lịch trở lên (`avail >= 360`).
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def plot_availability(avail: pd.Series, path, bins: int = 40) -> dict:
    fig, ax = plt.subplots(figsize=(8, 4))
    
    du_lieu_hop_le = avail.dropna()
    ax.hist(du_lieu_hop_le, bins=bins, color="#1E93AB", edgecolor="white")
    
    ax.set_title("Phân phối số ngày mở lịch có hai đỉnh phân hóa sâu sắc", pad=12, fontweight="bold")
    ax.set_xlabel("Số ngày mở lịch trong năm (ngày)")
    ax.set_ylabel("Số lượng chỗ ở (căn)")
    
    # Đếm hai nhóm hành vi đối lập
    so_khoa = int((du_lieu_hop_le == 0).sum())
    so_mo_quanh_nam = int((du_lieu_hop_le >= 360).sum())
    
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return {
        "ax": ax,
        "so_khoa": so_khoa,
        "so_mo_quanh_nam": so_mo_quanh_nam
    }
```

#### Phân tích sư phạm chuyên sâu: Diễn giải phân phối hai đỉnh
- **Vì sao giá trị trung bình hay trung vị không đại diện tốt cho phân phối này?**
  Khi dữ liệu tập trung ở hai cực đối lập ($0$ ngày và $365$ ngày), giá trị trung bình rơi vào khoảng $\approx 180$ ngày. Đây là một điểm trũng hoàn toàn không có dữ liệu thực tế. Báo cáo một con số trung bình 180 ngày sẽ đánh lừa các nhà hoạch định chính sách rằng các chỗ ở hoạt động cầm chừng nửa năm.
- **Khuyến nghị phương pháp luận báo cáo**:
  Bắt buộc phải phân tách và báo cáo thành hai nhóm riêng biệt: nhóm đóng cửa hoàn toàn ($X=0$) và nhóm vận hành chuyên nghiệp quanh năm ($X \ge 360$), đồng thời trình bày tỷ trọng của từng nhóm trong tổng thể.
:::

---

### Bài 6: Phục hồi tính trung thực cho biểu đồ bị cắt cụt trục

::: exercise Yêu cầu nghiệp vụ
Một đồng nghiệp gửi cho bạn một biểu đồ so sánh tỷ lệ căn hộ nguyên căn giữa các quận, trong đó trục tung bị ép bắt đầu từ giá trị nhỏ nhất trừ đi 5 (`ax.set_ylim(pct.min() - 5, ...)`), khiến mức chênh lệch trông như gấp 4 lần.
Hãy viết hàm `plot_honest_bars(pct: pd.Series, path) -> plt.Axes` nhận vào Series tỷ lệ phần trăm (chỉ mục tên quận) và đường dẫn tệp PNG.

Yêu cầu sửa chữa:
- Vẽ biểu đồ cột đứng `ax.bar` theo đúng thứ tự của `pct`.
- **Khóa trục tung bắt đầu từ 0** (`ax.set_ylim(bottom=0)`).
- Tiêu đề phản ánh trung thực mức chênh lệch thực tế (ít nhất 15 ký tự).
- Lưu ảnh bằng `fig.savefig(path, dpi=150, bbox_inches="tight")` và trả về đối tượng `ax`.
:::

::: solution
#### Mã nguồn cài đặt chuẩn

```python
def plot_honest_bars(pct: pd.Series, path) -> plt.Axes:
    fig, ax = plt.subplots(figsize=(7, 4))
    
    thanh = ax.bar(pct.index, pct.values, color="#1E93AB", width=0.55)
    
    # KHẮC PHỤC LỖI THỊ GIÁC: Khóa trục tung bắt đầu từ 0
    ax.set_ylim(bottom=0, top=105)
    
    ax.bar_label(thanh, fmt="%.1f%%", padding=3)
    ax.set_title("So sánh trung thực: Tỷ lệ nguyên căn giữa các quận chênh lệch vừa phải", pad=12, fontweight="bold")
    ax.set_ylabel("Tỷ lệ nguyên căn (%)")
    
    fig.savefig(path, dpi=150, bbox_inches="tight")
    return ax
```

#### Phân tích sư phạm chuyên sâu: Đạo đức trong truyền thông dữ liệu
Khi trục tung được đưa về mốc 0, người đọc nhìn thấy rõ ràng rằng tất cả các quận đều có tỷ lệ nguyên căn cao (đều trên $60\%$), và khoảng cách giữa quận thấp nhất và quận cao nhất chỉ là sự nhỉnh hơn khiêm tốn. Sự trung thực thị giác bảo vệ uy tín khoa học của nhà phân tích và ngăn ngừa các quyết định kinh doanh sai lầm dựa trên ảo giác đồ họa.
:::

---

### Bài tự làm mở rộng: Xây dựng bộ kiểm thử tự động cấu trúc hình ảnh bằng `assert`

::: exercise Đề bài mở rộng
Trong các đường ống xử lý dữ liệu tự động tích hợp CI/CD, làm thế nào để đảm bảo hàng trăm biểu đồ được sinh ra đều tuân thủ các quy chuẩn thiết kế mà không cần con người phải mở từng tệp ảnh ra xem bằng mắt?
Hãy viết một hàm kiểm thử tự động sử dụng mệnh đề `assert` để thẩm định một đối tượng `Axes`.
:::

::: solution
#### Mã nguồn hàm kiểm thử cấu trúc đồ họa

```python
def kiem_thu_cau_truc_bieu_do(ax: plt.Axes, duong_dan_file: str, loai_bieu_do: str = "bar"):
    path = Path(duong_dan_file)
    
    # 1. Kiểm tra việc xuất bản tệp
    assert path.exists(), f"LỖI: Tệp ảnh {duong_dan_file} chưa được ghi ra đĩa!"
    assert path.stat().st_size > 0, "LỖI: Tệp ảnh bị rỗng (0 bytes)!"
    
    # 2. Kiểm tra tiêu đề nêu thông điệp
    tieu_de = ax.get_title().strip()
    assert len(tieu_de) >= 15, f"LỖI: Tiêu đề '{tieu_de}' quá ngắn, chưa nêu rõ thông điệp phân tích!"
    
    # 3. Kiểm tra nhãn trục tung và trục hoành
    if loai_bieu_do == "bar":
        assert ax.get_ylabel().strip() != "", "LỖI: Thiếu nhãn trục tung (Y-axis label)!"
        # Kiểm tra quy tắc đạo đức gốc 0 cho biểu đồ cột
        assert ax.get_ylim()[0] == 0, "LỖI ĐẠO ĐỨC: Trục tung của biểu đồ cột bắt buộc phải bắt đầu từ 0!"
    elif loai_bieu_do == "barh":
        assert ax.get_xlabel().strip() != "", "LỖI: Thiếu nhãn trục hoành (X-axis label)!"
        assert ax.get_xlim()[0] == 0, "LỖI ĐẠO ĐỨC: Trục hoành của biểu đồ thanh ngang bắt buộc phải bắt đầu từ 0!"
        
    # 4. Kiểm tra sự hiện diện của phần tử đồ họa
    assert len(ax.patches) > 0 or len(ax.lines) > 0, "LỖI: Biểu đồ hoàn toàn không chứa phần tử dữ liệu nào!"
    print(f"XÁC MINH HOÀN TẤT: Biểu đồ '{path.name}' đạt chuẩn cấu trúc kỹ thuật 100%.")

# Chạy thử nghiệm hàm kiểm thử
fig_test, ax_test = plt.subplots()
ax_test.bar(["A", "B"], [10, 20])
ax_test.set_ylim(bottom=0)
ax_test.set_title("Doanh thu quý tăng trưởng vượt bậc", pad=10)
ax_test.set_ylabel("Triệu đồng")
fig_test.savefig("figures/test_kiem_thu.png")

kiem_thu_cau_truc_bieu_do(ax_test, "figures/test_kiem_thu.png", loai_bieu_do="bar")
plt.close(fig_test)
```

#### Bình luận chuyên môn
Việc biến các quy tắc trực quan hóa thành các câu lệnh `assert` kiểm tra tự động là một bước tiến vượt bậc về tư duy kỹ nghệ phần mềm trong khoa học dữ liệu. Nó giải phóng chuyên gia khỏi việc rà soát thủ công tẻ nhạt và bảo đảm toàn bộ báo cáo xuất bản ra công chúng đều đáp ứng các tiêu chuẩn đạo đức và kỹ thuật cao nhất.
:::

---

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
