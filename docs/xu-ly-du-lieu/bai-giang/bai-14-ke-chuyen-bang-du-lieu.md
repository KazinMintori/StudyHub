---
course: xu-ly-du-lieu
lecture: bai-14-ke-chuyen-bang-du-lieu
section: lecture
title: "Các bài toán phân tích dữ liệu và kiểm tra kết luận"
prerequisites: ["dataframe", "groupby"]
lessonStatus: ready
hasChapterExercises: true
description: "Vận dụng tổng hợp kỹ thuật xử lý dữ liệu qua 5 bài toán thực tế: Nhật ký múi giờ, điểm phim và mức độ bất đồng, xu hướng đặt tên, dữ liệu dinh dưỡng phân cấp, quyên góp tài chính và quy trình thẩm định kết luận."
---


<div class="lecture-notes-content">

Bài học này vận dụng các kỹ thuật xử lý dữ liệu vào 5 bài toán phân tích thực tế: Phân tích nhật ký truy cập web, đo lường mức độ bất đồng trong đánh giá phim, chuỗi thời gian tên khai sinh, dữ liệu dinh dưỡng phân cấp và hồ sơ tài chính quyên góp.

Song song với các bước làm sạch và biến đổi dữ liệu, bài học tập trung vào phương pháp kiểm chứng kết luận phân tích: Nhận diện nghịch lý Simpson khi tổng hợp dữ liệu gộp, kiểm soát mẫu số và tỷ trọng nhóm, phân biệt tương quan với nhân quả, và áp dụng quy trình thẩm định 4 bước để đánh giá độ tin cậy của các phát biểu định lượng.

---

## 1. Bài toán 1: Nhật ký truy cập và phân loại tác tử theo múi giờ

Dữ liệu nhật ký máy chủ (server logs) thường được ghi nhận dưới dạng chuỗi JSON thô (như nhật ký dịch vụ rút gọn liên kết 1.usa.gov). Mỗi dòng nhật ký ghi lại một sự kiện yêu cầu HTTP được gửi đến hệ thống, không tự động đại diện cho một người dùng duy nhất nếu chưa qua bước khử trùng lặp theo định danh hoặc phiên làm việc.

### Đọc, chuẩn hóa và xử lý giá trị khuyết thiếu

Một bản ghi nhật ký điển hình chứa trường múi giờ (`tz`) và thông tin chuỗi tác tử (`a`, user-agent string). Hai thách thức lớn nhất khi làm sạch cột múi giờ là sự phân biệt giữa giá trị khuyết hoàn toàn (`None` hoặc `NaN`) với chuỗi rỗng (`""`):

```python
import numpy as np
import pandas as pd

# Tập dữ liệu nhật ký mô phỏng nhỏ
ban_ghi = [
    {"tz": "Asia/Ho_Chi_Minh", "a": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
    {"tz": "Asia/Ho_Chi_Minh", "a": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"},
    {"tz": "America/New_York", "a": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"},
    {"tz": "", "a": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)"},
    {"a": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"} # Không có trường tz
]

df_nhat_ky = pd.DataFrame(ban_ghi)

# Chuẩn hóa giá trị thiếu: Phân biệt thiếu từ nguồn với chuỗi rỗng
tz_sach = df_nhat_ky["tz"].fillna("Missing").replace({"": "Unknown"})

print("Tần suất phân bố múi giờ:")
print(tz_sach.value_counts())
```

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-1 -->

::: example Tách thông tin tác tử và chuẩn hóa chuỗi khuyết thiếu bằng str.extract

Chuỗi User-Agent thường chứa thông tin ứng dụng và phiên bản ghép nối. Phương thức Series.str.extract với biểu thức chính quy hỗ trợ phân tách chuỗi thành các cột độc lập, kết hợp xử lý chuỗi rỗng và giá trị khuyết thiếu một cách tường minh.

```python
import pandas as pd

s_agent = pd.Series([
    "Mozilla/5.0 (Windows NT 10.0)",
    "curl/7.68.0",
    "",
    None,
], name="agent")

# Trích xuất tên ứng dụng chính trước dấu gạch chéo
df_ext = s_agent.fillna("Missing").replace({"": "Unknown"}).to_frame()
df_ext[["app", "ver"]] = df_ext["agent"].str.extract(r"^([^/]+)/?(\S+)?")

bang_kq = pd.DataFrame({
    "goc": df_ext["agent"],
    "app": df_ext["app"].fillna("None"),
    "ver": df_ext["ver"].fillna("None"),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| goc | app | ver |
| --- | --- | --- |
| Mozilla/5.0 (Windows NT 10.0) | Mozilla | 5.0 |
| curl/7.68.0 | curl | 7.68.0 |
| Unknown | Unknown | None |
| Missing | Missing | None |

</div>

Chuỗi tác tử người dùng (User-Agent) trong tiêu đề HTTP là chuỗi văn bản do phía máy khách gửi lên máy chủ web. Trong lịch sử phát triển web, tiền tố `Mozilla/5.0` là tiền tố tương thích kế thừa xuất hiện trên hầu hết các chuỗi User-Agent của các trình duyệt hiện đại, chứ không đại diện riêng cho danh tính của một trình duyệt đơn lẻ. Đối với các công cụ tự động như `curl/7.68.0`, định dạng thường thể hiện trực tiếp tên công cụ cùng số hiệu phiên bản.

Mẫu `^([^/]+)/?(\S+)?` lấy phần đầu trước dấu `/` và dãy ký tự không phải khoảng trắng tiếp theo. Với `curl/7.68.0`, hai cột là `curl` và `7.68.0`. Với chuỗi Mozilla, nó chỉ lấy tiền tố tương thích và phiên bản tiền tố. Đây chưa phải một bộ phân tích đầy đủ để nhận diện trình duyệt.

Các bản ghi có thể bị khuyết thiếu dưới dạng giá trị `None` hoặc chuỗi rỗng `""`. Việc gán nhãn `Missing` cho `None` và `Unknown` cho chuỗi rỗng giúp mã nguồn xử lý đồng bộ các trường hợp đặc biệt này. Tuy nhiên, chỉ dựa vào sự khác biệt giữa chuỗi rỗng và giá trị khuyết trong dữ liệu lưu vết thì chưa đủ căn cứ kỹ thuật để kết luận chính xác nguyên nhân gốc rễ phát sinh từ mạng truyền dẫn hay từ ứng dụng.

:::

<!-- /worked-example -->

### Phân loại heuristic hệ điều hành từ chuỗi tác tử

Chuỗi tác tử người dùng (User-Agent string) phản ánh thông tin trình duyệt và môi trường do trình khách khai báo. Việc kiểm tra chuỗi con `"Windows"` bằng `str.contains("Windows")` là một bộ phân loại phỏng đoán (heuristic classifier) phục vụ việc phân nhóm sơ bộ các yêu cầu HTTP, không phải là cơ chế xác thực danh tính hệ điều hành thực tế của người dùng (chuỗi User-Agent có thể bị chỉnh sửa hoặc chứa nhiều thông tin phụ):

```python
# Phân loại sơ bộ yêu cầu từ môi trường Windows theo quy tắc heuristic
df_nhat_ky["he_dieu_hanh"] = np.where(
    df_nhat_ky["a"].fillna("").str.contains("Windows"),
    "Windows",
    "Khac"
)

# Tổng hợp số lượng yêu cầu theo múi giờ và hệ điều hành suy đoán
bang_he_dieu_hanh = df_nhat_ky.groupby(
    [tz_sach, "he_dieu_hanh"]
).size().unstack(fill_value=0)

print("Phân bố số lượng yêu cầu theo múi giờ và hệ điều hành:")
print(bang_he_dieu_hanh)
```

---

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-2 -->

::: example Phân loại điều kiện hệ điều hành bằng np.select

Khi phân loại hệ điều hành từ chuỗi User-Agent theo các quy tắc gần đúng, việc dùng nhiều lệnh rẽ nhánh lồng nhau gây khó khăn cho việc bảo trì. Hàm np.select hỗ trợ quản lý danh sách điều kiện và nhãn lựa chọn theo cấu trúc mảng tuần tự.

```python
import numpy as np
import pandas as pd

s_agent = pd.Series([
    "Mozilla/5.0 (Windows NT 10.0; Win64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X)",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64)",
    "Googlebot/2.1",
])

# Thiết lập các điều kiện phân loại heuristic
dieu_kien = [
    s_agent.str.contains("Windows"),
    s_agent.str.contains("Macintosh"),
    s_agent.str.contains("Linux"),
]
lua_chon = ["Windows", "MacOS", "Linux"]

s_os = np.select(dieu_kien, lua_chon, default="Other")
bang_kq = pd.DataFrame({
    "os": s_os,
    "so_luong": [1] * len(s_os),
})
bang_dem = bang_kq.groupby("os").count().reset_index()
print(bang_dem)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| os | so&#95;luong |
| --- | --- |
| Linux | 1 |
| MacOS | 1 |
| Other | 1 |
| Windows | 1 |

</div>

Nhận diện hệ điều hành từ chuỗi User-Agent là bài toán phân loại theo quy tắc phỏng đoán (heuristic), bởi chuỗi tác tử có thể chứa nhiều từ khóa đồng thời hoặc bị thay đổi bởi phía người dùng. Thay vì viết nhiều câu lệnh lồng ghép phức tạp, hàm `np.select` của NumPy cung cấp cấu trúc biểu diễn trực quan dựa trên danh sách điều kiện và danh sách giá trị tương ứng.

Cơ chế vận hành của `np.select` bao gồm một danh sách các mảng boolean `dieu_kien` và danh sách nhãn `lua_chon`. Cần lưu ý rằng các biểu thức điều kiện như `s_agent.str.contains(...)` được tính toán toàn bộ trước khi đưa vào hàm, chứ không thực thi song song trên phần cứng hay ngắt sớm (short-circuit) như cấu trúc rẽ nhánh trong ngôn ngữ lập trình thuần túy. Hàm sẽ quét lần lượt qua từng mảng điều kiện theo thứ tự danh sách và chọn nhãn thỏa mãn đầu tiên cho mỗi phần tử.

Nếu một bản ghi không thỏa mãn bất kỳ điều kiện nào trong danh sách, ví dụ chuỗi bot tìm kiếm `Googlebot/2.1`, hàm sẽ gán giá trị mặc định được chỉ định tại `default="Other"`. Bảng kết quả sau khi gom nhóm thể hiện số lượng bản ghi tương ứng cho từng nhóm hệ điều hành, giúp cấu trúc phân loại dễ dàng bổ sung thêm các điều kiện mới khi mở rộng hệ thống.

:::

<!-- /worked-example -->

## 2. Bài toán 2: Đánh giá phim và đo lường mức độ bất đồng quan điểm

Trong hệ thống gợi ý và phân tích thị hiếu người tiêu dùng, dữ liệu thường được phân tán trên nhiều bảng quan hệ: Bảng người dùng (Users), bảng nội dung (Movies) và bảng nhật ký đánh giá (Ratings).

### Hợp nhất dữ liệu và lập bảng xoay chiều

Quy trình phân tích bắt đầu bằng việc ghép nối các bảng theo khóa ngoại bằng `pd.merge()`:

```python
ratings = pd.DataFrame({
    "user_id": [1, 2, 3, 4, 1, 2, 3, 4],
    "movie_id": [10, 10, 10, 10, 20, 20, 20, 20],
    "rating": [5, 2, 4, 1, 4, 4, 3, 4]
})
users = pd.DataFrame({
    "user_id": [1, 2, 3, 4],
    "gender": ["F", "M", "F", "M"]
})
movies = pd.DataFrame({
    "movie_id": [10, 20],
    "title": ["Phim Hanh Dong A", "Phim Tam Ly B"]
})

# Hợp nhất ba bảng dữ liệu
du_lieu_phim = ratings.merge(users, on="user_id").merge(movies, on="movie_id")

# Lập bảng xoay chiều tính điểm trung bình theo giới tính
bang_diem = du_lieu_phim.pivot_table(
    index="title",
    columns="gender",
    values="rating",
    aggfunc="mean"
)
print("Điểm đánh giá trung bình theo giới tính:")
print(bang_diem)
```

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-3 -->

::: example Lọc số lượng đánh giá tối thiểu bằng GroupBy.filter trước khi lập bảng xoay chiều

Trong dữ liệu đánh giá sản phẩm, các mục chỉ có một vài lượt đánh giá ngẫu nhiên có thể tạo ra điểm số bình quân không mang tính đại diện. Phương thức GroupBy.filter cho phép loại bỏ các nhóm có cỡ mẫu quá nhỏ trước khi tổng hợp bằng pivot_table.

```python
import pandas as pd

df_danh_gia = pd.DataFrame({
    "phim": ["Phim A", "Phim A", "Phim A", "Phim B", "Phim C", "Phim C"],
    "gioi_tinh": ["F", "M", "F", "M", "F", "M"],
    "diem": [5, 4, 5, 5, 2, 3],
})

# Lọc chỉ giữ lại các phim có tối thiểu 3 lượt đánh giá
df_loc = df_danh_gia.groupby("phim").filter(lambda x: len(x) >= 3)

bang_piv = df_loc.pivot_table(
    index="phim",
    columns="gioi_tinh",
    values="diem",
    aggfunc="mean",
).reset_index()
print(bang_piv)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| phim | F | M |
| --- | --- | --- |
| Phim A | 5.0 | 4.0 |

</div>

Khi phân tích dữ liệu xếp hạng sản phẩm hoặc nội dung, những mục chỉ có rất ít lượt đánh giá có thể đạt điểm số trung bình tối đa nhưng mang độ bất định cao do cỡ mẫu hạn chế. Chẳng hạn một bộ phim chỉ nhận được một lượt chấm 5 sao sẽ có điểm trung bình bằng 5.0, nhưng con số này khó so sánh trực tiếp với những bộ phim có hàng trăm lượt đánh giá với điểm số 4.5.

Phương thức `GroupBy.filter` hỗ trợ chọn lọc các nhóm thỏa mãn một điều kiện kích thước cụ thể. Điều kiện `lambda x: len(x) >= 3` yêu cầu mỗi nhóm phim phải có tối thiểu 3 lượt đánh giá mới được giữ lại trong dữ liệu phân tích. Khác với các hàm tổng hợp dữ liệu, phương thức này trả về tập con của bảng ban đầu gồm toàn bộ các dòng thuộc các nhóm đủ điều kiện.

Dù vậy, việc đặt ngưỡng tối thiểu 3 lượt đánh giá chỉ là một bước lọc sơ bộ chứ không loại bỏ hoàn toàn thiên lệch chọn mẫu, đồng thời không bảo đảm rằng số lượng mẫu trong từng nhóm con nhân khẩu học đã đủ lớn để suy diễn tin cậy. Trong bảng kết quả, `Phim A` vượt qua điều kiện lọc với 3 đánh giá, và bảng xoay chiều `pivot_table` hiển thị điểm trung bình của khán giả nữ là 5.0 dựa trên 2 lượt chấm và khán giả nam là 4.0 dựa trên 1 lượt chấm duy nhất.

:::

<!-- /worked-example -->

### Đo lường mức độ bất đồng quan điểm

Làm thế nào để phát hiện các tác phẩm gây tranh cãi trong cộng đồng? Ta sử dụng hai thước đo định lượng:
1. **Chênh lệch thị hiếu giữa các nhóm**: Tính hiệu số điểm giữa khán giả nữ và nam (`diff = piv["F"] - piv["M"]`).
2. **Độ phân tán của toàn bộ khán giả**: Tính độ lệch chuẩn (`std`) của điểm số cho từng bộ phim. Phim có độ lệch chuẩn cao là phim mà người xem chia rẽ sâu sắc (người chấm 1 sao, người chấm 5 sao), trong khi phim có độ lệch chuẩn thấp nhận được sự đồng thuận cao.

```python
# 1. Đo lường chênh lệch giới tính
bang_diem["chenh_lech"] = bang_diem["F"] - bang_diem["M"]

# 2. Đo lường độ phân tán bằng độ lệch chuẩn
do_phan_tan = du_lieu_phim.groupby("title")["rating"].std()
bang_diem["do_lech_chuan"] = do_phan_tan

print("Bảng đo lường bất đồng quan điểm:")
print(bang_diem[["chenh_lech", "do_lech_chuan"]])
```

---

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-4 -->

::: example Đo lường độ phân tán đánh giá bằng độ lệch chuẩn và khoảng tứ phân vị IQR

Điểm trung bình không phản ánh được mức độ phân cực ý kiến của người đánh giá. Kết hợp độ lệch chuẩn std và khoảng tứ phân vị IQR cung cấp góc nhìn đa chiều về mức độ đồng thuận của các tập dữ liệu điểm số.

```python
import pandas as pd

df = pd.DataFrame({
    "phim": ["A", "A", "A", "A", "B", "B", "B", "B"],
    "diem": [1, 5, 1, 5, 3, 3, 4, 3],
})

def tinh_iqr(s):
    return s.quantile(0.75) - s.quantile(0.25)

tong_hop = df.groupby("phim")["diem"].agg(
    tb="mean",
    std="std",
    iqr=tinh_iqr,
).reset_index()

bang_kq = pd.DataFrame({
    "phim": tong_hop["phim"],
    "tb": tong_hop["tb"].round(2),
    "std": tong_hop["std"].round(2),
    "iqr": tong_hop["iqr"].round(2),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| phim | tb | std | iqr |
| --- | --- | --- | --- |
| A | 3.0 | 2.31 | 4.0 |
| B | 3.25 | 0.5 | 0.25 |

</div>

Điểm trung bình là thước đo xu hướng tập trung cơ bản nhưng không thể hiện được sự phân tán của dữ liệu. Hai tập dữ liệu điểm số có thể cùng mang điểm trung bình là 3.0, nhưng một tập gồm toàn điểm 3 thể hiện sự đồng thuận cao, trong khi tập còn lại gồm nửa điểm 1 và nửa điểm 5 lại phản ánh sự chia rẽ ý kiến rõ rệt giữa hai thái cực.

Để định lượng độ biến thiên, độ lệch chuẩn mẫu `std` đo lường căn bậc hai của phương sai mẫu với bậc tự do hiệu chỉnh `ddof=1`. Với tập điểm `[1, 5, 1, 5]` của phim A, độ lệch chuẩn đạt giá trị xấp xỉ 2.31, trong khi tập điểm của phim B có độ lệch chuẩn là 0.50, cho thấy mức độ phân tán của phim A cao hơn đáng kể so với phim B.

IQR bằng phân vị 75% trừ phân vị 25%. Với điểm `[1, 5, 1, 5]`, hai phân vị là 5 và 1 nên IQR bằng 4. Phim B có IQR 0.25 theo cách nội suy phân vị mặc định. Hai chỉ tiêu cho thấy mức phân tán khác nhau trong mẫu, không tự suy ra nguyên nhân người xem chấm điểm.

:::

<!-- /worked-example -->

## 3. Bài toán 3: Phân tích xu hướng đặt tên, tính đa dạng và sự dịch chuyển âm cuối

Tập dữ liệu đặt tên của cơ quan quản lý an sinh xã hội ghi nhận số lượng trẻ em sinh ra theo tên, giới tính và năm, kéo dài từ cuối thế kỷ 19 đến nay. Đây là ví dụ điển hình cho việc phân tích dữ liệu lịch sử dài hạn.

### Chuẩn hóa tỷ trọng và phân tích xu hướng

Tổng số trẻ sinh ra thay đổi mạnh qua từng thập kỷ do bùng nổ dân số. Do đó, so sánh số lượng tuyệt đối sẽ làm sai lệch nhận định. Thao tác cần thiết là tính **tỷ trọng phần trăm** của từng tên trong từng năm và từng giới tính:

```python
du_lieu_ten = pd.DataFrame({
    "nam": [1880, 1880, 1950, 1950, 2010, 2010],
    "ten": ["John", "Mary", "John", "Mary", "John", "Mary"],
    "gioi_tinh": ["M", "F", "M", "F", "M", "F"],
    "so_tre": [9655, 7065, 79428, 65482, 11498, 4073]
})

# Tính tỷ trọng trong từng nhóm năm và giới tính
du_lieu_ten["ty_trong"] = du_lieu_ten.groupby(
    ["nam", "gioi_tinh"]
)["so_tre"].transform(lambda x: x / x.sum())

print("Bảng tỷ trọng đặt tên:")
print(du_lieu_ten)
```

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-5 -->

::: example Xếp hạng mức độ phổ biến theo từng nhóm năm bằng rank

Khi phân tích xu hướng tên khai sinh theo thời gian, số lượng tuyệt đối bị chi phối bởi quy mô dân số. Phương thức rank với tham số ascending=False hỗ trợ tính toán thứ hạng tương đối của các tên trong từng năm quan sát.

```python
import pandas as pd

df_ten = pd.DataFrame({
    "nam": [2010, 2010, 2010, 2020, 2020, 2020],
    "ten": ["Liam", "Noah", "William", "Liam", "Noah", "William"],
    "so_tre": [15000, 14000, 16000, 19000, 18000, 12000],
})

# Tính thứ hạng giảm dần theo số lượng trẻ trong từng năm
df_ten["thu_hang"] = df_ten.groupby("nam")["so_tre"].rank(
    ascending=False, method="min"
).astype(int)

bang_kq = df_ten.sort_values(["nam", "thu_hang"]).reset_index(drop=True)
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| nam | ten | so&#95;tre | thu&#95;hang |
| --- | --- | --- | --- |
| 2010 | William | 16000 | 1 |
| 2010 | Liam | 15000 | 2 |
| 2010 | Noah | 14000 | 3 |
| 2020 | Liam | 19000 | 1 |
| 2020 | Noah | 18000 | 2 |
| 2020 | William | 12000 | 3 |

</div>

Khi theo dõi tần suất xuất hiện của các tên gọi qua các giai đoạn, sự gia tăng về số lượng tuyệt đối có thể phản ánh sự thay đổi quy mô dân số chung thay vì phản ánh sự thay đổi mức độ phổ biến tương đối. Do đó, việc chuyển đổi số lượng quan sát sang chỉ số thứ hạng (rank) theo từng năm giúp người phân tích theo dõi sự dịch chuyển vị thế giữa các thực thể trong tập dữ liệu.

Phương thức `GroupBy.rank` kết hợp tham số `ascending=False` thực hiện sắp xếp thứ bậc giảm dần trong từng nhóm năm: Tên có số lượng trẻ lớn nhất nhận thứ hạng 1, các tên kế tiếp nhận thứ hạng lớn hơn. Tùy chọn `method="min"` quy định rằng các phần tử có cùng số lượng sẽ nhận chung thứ hạng nhỏ nhất trong nhóm đồng hạng.

Thứ hạng tính toán chỉ áp dụng cho danh sách các tên có mặt trong bảng dữ liệu khảo sát cụ thể. Bảng kết quả cho thấy vào năm 2010, thứ tự sắp xếp lần lượt là `William` (hạng 1), `Liam` (hạng 2) và `Noah` (hạng 3). Đến năm 2020, thứ tự ghi nhận là `Liam` (hạng 1), `Noah` (hạng 2) và `William` (hạng 3), phản ánh sự thay đổi thứ bậc số lượng giữa ba tên gọi này trong mẫu dữ liệu được cung cấp.

:::

<!-- /worked-example -->

### Đo lường tính đa dạng đặt tên

Một câu hỏi xã hội học đáng quan tâm: Thị hiếu đặt tên của cha mẹ ngày càng phong phú hay ngày càng thu hẹp?
Ta có thể đo lường tính đa dạng bằng cách tính **số lượng tên phổ biến nhất cần thiết để chiếm đủ 50% tổng số trẻ sinh ra trong năm**. Ở thế kỷ 19, chỉ cần vài chục tên đứng đầu đã chiếm tới một nửa số trẻ em. Đến thế kỷ 21, số lượng tên cần thiết đã tăng lên hàng trăm, phản ánh sự mở rộng về tính đa dạng khi lựa chọn tên gọi.

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-6 -->

::: example Xác định số lượng tên chiếm 50% tổng số trẻ bằng cumsum và searchsorted

Để đánh giá mức độ tập trung của các tên gọi phổ biến, ta đo lường số lượng tên cần thiết để chiếm một nửa tổng số lượng quan sát. Quy trình kết hợp sắp xếp giảm dần, tính tổng tích lũy bằng cumsum và xác định vị trí ngưỡng bằng np.searchsorted.

```python
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "ten": ["NameA", "NameB", "NameC", "NameD", "NameE"],
    "so_tre": [400, 300, 150, 100, 50],
})

# Sắp xếp giảm dần và tính tổng dồn tích lũy
df_sap = df.sort_values("so_tre", ascending=False).copy()
df_sap["tong_don"] = df_sap["so_tre"].cumsum()
tong_so = df_sap["so_tre"].sum()
nguong_50 = tong_so * 0.5

# Tìm số lượng tên chạm hoặc vượt ngưỡng 50%
so_luong_ten = int(df_sap["tong_don"].values.searchsorted(nguong_50)) + 1

bang_kq = pd.DataFrame([{
    "tong_tre": int(tong_so),
    "nguong_50": float(nguong_50),
    "so_ten_top50": so_luong_ten,
}])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| tong&#95;tre | nguong&#95;50 | so&#95;ten&#95;top50 |
| --- | --- | --- |
| 1000.0 | 500.0 | 2.0 |

</div>

Đo lường mức độ tập trung giúp người phân tích hiểu được tỷ trọng đóng góp của các thực thể hàng đầu vào quy mô chung. Nếu chỉ cần một số lượng nhỏ các phần tử đứng đầu đã chiếm tới một nửa tổng số quan sát, phân phối dữ liệu mang tính tập trung cao. Ngược lại, nếu cần nhiều phần tử hơn để đạt ngưỡng đó, phân phối có xu hướng phân tán và đa dạng hơn.

Phương pháp tính toán bắt đầu bằng việc sắp xếp bảng dữ liệu theo số lượng giảm dần qua `sort_values`. Tiếp theo, phương thức `Series.cumsum()` tính tổng dồn tích lũy qua từng hàng. Phép tính này đòi hỏi các giá trị số lượng phải không âm và tổng số lượng toàn bảng phải lớn hơn 0 để ngưỡng phân vị mang ý nghĩa toán học hợp lệ. Với tổng số trẻ là 1,000, ngưỡng 50% tương ứng với mốc 500 trẻ.

Hàm `np.searchsorted()` thực hiện tìm kiếm vị trí của phần tử đầu tiên đạt hoặc vượt ngưỡng 500 trên mảng tổng dồn đã sắp xếp tăng dần. Giá trị 700 tại chỉ số 1 vượt qua mốc 500, cộng thêm 1 do quy ước chỉ mục bắt đầu từ 0 của Python, ta xác định được kết quả là 2 tên. Hai tên đầu tiên trong danh sách đã tích lũy được 700 lượt, đạt và vượt ngưỡng 50% của tập dữ liệu mẫu.

:::

<!-- /worked-example -->

### Sự dịch chuyển của chữ cái kết thúc

Bằng cách trích xuất ký tự cuối cùng của chuỗi tên gọi bằng `str[-1]`, ta quan sát thấy sự thay đổi rõ rệt trong phân bố chữ cái kết thúc của tên con trai. Tỷ trọng các tên kết thúc bằng chữ cái `"n"` (như John, Ryan, Ethan) đã tăng từ khoảng 14% ở thế kỷ 19 lên hơn 35% trong những năm gần đây.

```python
du_lieu_ten["chu_cai_cuoi"] = du_lieu_ten["ten"].str[-1]
bang_chu_cai = du_lieu_ten.pivot_table(
    index="chu_cai_cuoi",
    columns=["nam", "gioi_tinh"],
    values="so_tre",
    aggfunc="sum",
    fill_value=0
)
print("Phân bố chữ cái kết thúc:")
print(bang_chu_cai)
```

---

## 4. Bài toán 4: Khai phá dữ liệu dinh dưỡng lồng nhau dạng JSON

Cơ sở dữ liệu dinh dưỡng (như dữ liệu thành phần thực phẩm) thường được phân phối dưới dạng các cấu trúc JSON phân cấp sâu: Mỗi món ăn là một đối tượng chứa các trường định danh cơ bản, kèm theo một mảng con lồng nhau gồm hàng chục chỉ số vi chất dinh dưỡng.

### Phẳng hóa dữ liệu phân cấp

Để phân tích bằng các công cụ bảng, ta cần tách dữ liệu thành hai bảng liên kết:
1. **Bảng món ăn**: Chứa thông tin chung (`id`, `ten_mon`, `nhom_thuc_pham`).
2. **Bảng thành phần dinh dưỡng**: Chứa các dòng chi tiết liên kết qua khóa `id`.

```python
thuc_pham_raw = [
    {
        "id": 1001,
        "ten": "Bo lat",
        "nhom": "Sua",
        "dinh_duong": [
            {"chat": "protein", "luong": 0.85},
            {"chat": "chat_beo", "luong": 81.11},
            {"chat": "canxi", "luong": 24.0}
        ]
    },
    {
        "id": 1002,
        "ten": "Trung ga",
        "nhom": "Trung",
        "dinh_duong": [
            {"chat": "protein", "luong": 12.56},
            {"chat": "chat_beo", "luong": 9.51},
            {"chat": "canxi", "luong": 56.0}
        ]
    }
]

# Tách bảng thông tin món ăn
df_thuc_pham = pd.DataFrame([
    {"id": d["id"], "ten": d["ten"], "nhom": d["nhom"]}
    for d in thuc_pham_raw
])

# Phẳng hóa mảng lồng nhau thành bảng dinh dưỡng chi tiết
danh_sach_chat = []
for d in thuc_pham_raw:
    for n in d["dinh_duong"]:
        danh_sach_chat.append({
            "id": d["id"],
            "chat": n["chat"],
            "luong": n["luong"]
        })
df_dinh_duong = pd.DataFrame(danh_sach_chat)

# Hợp nhất hai bảng để phục vụ phân tích
bang_tong_hop = df_dinh_duong.merge(df_thuc_pham, on="id")
print("Bảng dinh dưỡng phẳng hóa hoàn chỉnh:")
print(bang_tong_hop)
```

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-7 -->

::: example Phẳng hóa cấu trúc JSON lồng nhau nhiều cấp bằng pd.json_normalize

Dữ liệu phân cấp dạng JSON thường chứa các mảng con lồng trong bản ghi cha. Hàm pd.json_normalize nhận tham số record_path và meta để phân rã mảng con và liên kết trường định danh cha thành bảng hai chiều hoàn chỉnh.

```python
import pandas as pd

du_lieu = [
    {
        "id": 101,
        "ten": "Bo lat",
        "nhom": "Sua",
        "chat": [
            {"ten_chat": "protein", "luong": 0.85},
            {"ten_chat": "fat", "luong": 81.11},
        ],
    },
    {
        "id": 102,
        "ten": "Trung ga",
        "nhom": "Trung",
        "chat": [
            {"ten_chat": "protein", "luong": 12.56},
            {"ten_chat": "fat", "luong": 9.51},
        ],
    },
]

df_phang = pd.json_normalize(
    du_lieu,
    record_path="chat",
    meta=["id", "ten", "nhom"],
)

bang_kq = df_phang[["id", "ten", "ten_chat", "luong"]]
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| id | ten | ten&#95;chat | luong |
| --- | --- | --- | --- |
| 101 | Bo lat | protein | 0.85 |
| 101 | Bo lat | fat | 81.11 |
| 102 | Trung ga | protein | 12.56 |
| 102 | Trung ga | fat | 9.51 |

</div>

Dữ liệu trao đổi qua các giao diện lập trình ứng dụng (API) thường có cấu trúc JSON phân cấp bán cấu trúc. Mỗi đối tượng ở tầng gốc có thể đính kèm một mảng các đối tượng con ở tầng dưới, chẳng hạn thông tin về một món ăn chứa mảng danh sách các thành phần dinh dưỡng. Việc xử lý thủ công các cấu trúc lồng nhau này bằng các vòng lặp Python thường tốn công sức và dễ phát sinh lỗi khi định dạng dữ liệu phức tạp.

Hàm `pd.json_normalize` cung cấp giải pháp chuyển đổi cấu trúc cây phân cấp thành bảng hai chiều có cấu trúc. Tham số `record_path="chat"` hướng dẫn hàm tách từng phần tử trong mảng con thành một dòng dữ liệu độc lập. Mỗi chất dinh dưỡng trong mảng được chuyển hóa thành một bản ghi riêng biệt trong bảng kết quả.

Đi kèm với việc tách dòng con, tham số `meta=["id", "ten", "nhom"]` sao chép các thuộc tính ở cấp độ cha và gắn kèm vào từng dòng con tương ứng. Cơ chế này tương tự như một phép nối bảng quan hệ, bảo đảm mỗi dòng thành phần dinh dưỡng đều mang đầy đủ thông tin định danh và tên món ăn nguồn, tạo thuận lợi cho các bước phân tích tiếp theo.

:::

<!-- /worked-example -->

### Truy vấn thực phẩm giàu vi chất theo nhóm

Nhờ cấu trúc bảng phẳng, việc tìm kiếm thực phẩm có hàm lượng vi chất cao nhất theo từng nhóm trở nên trực diện thông qua `groupby` và `idxmax`:

```python
# Tìm món ăn giàu protein nhất trong từng nhóm
protein_df = bang_tong_hop[bang_tong_hop["chat"] == "protein"]
top_protein = protein_df.sort_values("luong", ascending=False)
print("Thực phẩm giàu protein nhất:")
print(top_protein[["ten", "nhom", "luong"]])
```

---

## 5. Bài toán 5: Phân tích đóng góp tài chính và phân khoảng giá trị

Hồ sơ quyên góp tài chính chính trị và xã hội thường có phân phối số tiền lệch phải rõ rệt: Đa số các khoản quyên góp có quy mô nhỏ (vài chục đến vài trăm nghìn đồng), trong khi tổng giá trị đóng góp chịu ảnh hưởng lớn từ các khoản tài trợ quy mô lớn của các nhà tài trợ.

### Chuẩn hóa trường nghề nghiệp và cơ quan

Dữ liệu tự khai báo thường chứa hàng trăm biến thể chính tả của cùng một nghề nghiệp (ví dụ: `"KS"`, `"Kỹ sư"`, `"ENGINEER"`). Kỹ thuật chuẩn hóa là xây dựng từ điển ánh xạ (`mapping dictionary`):

```python
df_quyen_gop = pd.DataFrame({
    "nguoi_ung_ho": ["An", "Binh", "Chi", "Dung", "Em"],
    "nghe_nghiep": ["Kỹ sư", "KS", "Bác sĩ", "GIAO VIEN", "Giáo viên"],
    "ung_vien": ["UngVien_A", "UngVien_A", "UngVien_B", "UngVien_B", "UngVien_A"],
    "so_tien": [50, 250, 1500, 75, 12000]
})

anh_xa_nghe = {
    "Kỹ sư": "Kỹ thuật",
    "KS": "Kỹ thuật",
    "Bác sĩ": "Y tế",
    "GIAO VIEN": "Giáo dục",
    "Giáo viên": "Giáo dục"
}
df_quyen_gop["nghe_chuan"] = df_quyen_gop["nghe_nghiep"].map(anh_xa_nghe)
```

### Phân khoảng số tiền đóng góp với `pd.cut`

Để quan sát cơ cấu nhà tài trợ, ta phân chia số tiền quyên góp thành các khoảng giá trị (buckets / bins) tăng theo cấp số nhân:

```python
cac_nguong = [0, 100, 1000, 10000, 100000]
df_quyen_gop["khoang_tien"] = pd.cut(
    df_quyen_gop["so_tien"],
    bins=cac_nguong,
    right=True
)

# Tổng hợp dòng tiền theo ứng viên và khoảng tiền đóng góp
dong_tien_nhom = df_quyen_gop.groupby(
    ["ung_vien", "khoang_tien"],
    observed=False
)["so_tien"].sum().unstack(fill_value=0)

print("Phân bố dòng tiền quyên góp theo quy mô:")
print(dong_tien_nhom)
```

Bảng tổng hợp này cho thấy ngay ứng viên nào nhận được sự ủng hộ rộng rãi từ các cử tri bình dân (chi phối ở khoảng dưới 100) và ứng viên nào phụ thuộc vào các khoản tài trợ quy mô lớn (chi phối ở khoảng trên 1.000).

---

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-8 -->

::: example So sánh phân khoảng theo mốc cố định pd.cut và phân khoảng theo phân vị pd.qcut

Rời rạc hóa biến liên tục phục vụ việc gom nhóm đối tượng phân tích. Hàm pd.cut phân khoảng theo các mốc số học định trước, trong khi pd.qcut chia dữ liệu theo các phân vị nhằm tạo ra các nhóm có số lượng phần tử xấp xỉ bằng nhau.

```python
import pandas as pd

s_tien = pd.Series([10, 25, 50, 100, 200, 500, 1000, 5000])

# 1. pd.cut theo các ngưỡng giá trị định trước
khoang_cut = pd.cut(s_tien, bins=[0, 100, 1000, 10000])

# 2. pd.qcut chia đều thành 4 tứ phân vị có cỡ mẫu bằng nhau
khoang_qcut = pd.qcut(s_tien, q=4)

bang_kq = pd.DataFrame({
    "tien": s_tien,
    "cut_bin": khoang_cut.astype(str),
    "qcut_bin": khoang_qcut.astype(str),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| tien | cut&#95;bin | qcut&#95;bin |
| --- | --- | --- |
| 10 | (0, 100&#93; | (9.999, 43.75&#93; |
| 25 | (0, 100&#93; | (9.999, 43.75&#93; |
| 50 | (0, 100&#93; | (43.75, 150.0&#93; |
| 100 | (0, 100&#93; | (43.75, 150.0&#93; |
| 200 | (100, 1000&#93; | (150.0, 625.0&#93; |
| 500 | (100, 1000&#93; | (150.0, 625.0&#93; |
| 1000 | (100, 1000&#93; | (625.0, 5000.0&#93; |
| 5000 | (1000, 10000&#93; | (625.0, 5000.0&#93; |

</div>

Phân khoảng dữ liệu (Binning) là kỹ thuật chuyển đổi một biến số liên tục thành các nhóm rời rạc để phục vụ việc thống kê hoặc lập báo cáo. Trong pandas, hai hàm `pd.cut` và `pd.qcut` đáp ứng hai nhu cầu phân nhóm khác nhau tùy thuộc vào yêu cầu nghiệp vụ và đặc điểm phân phối của dữ liệu.

Hàm `pd.cut` nhận danh sách các ngưỡng ranh giới cố định thông qua tham số `bins`. Phương thức này gán mỗi giá trị vào khoảng chứa tương ứng bất kể số lượng mẫu trong mỗi khoảng nhiều hay ít. Cách tiếp cận này phù hợp với các tiêu chuẩn phân loại định sẵn theo quy định hành chính hoặc biểu phí kế toán, dù có thể dẫn đến việc các khoảng giá trị lớn có rất ít quan sát.

Ngược lại, hàm `pd.qcut` phân khoảng dựa trên các mốc phân vị thực nghiệm với tham số `q=4` để chia dữ liệu thành 4 nhóm. Mục tiêu của `pd.qcut` là tạo ra các khoảng có số lượng quan sát gần như bằng nhau. Cần chú ý rằng sự đồng đều về số lượng chỉ mang tính xấp xỉ và không được bảo đảm nếu dữ liệu xuất hiện nhiều giá trị trùng nhau tại các điểm phân vị biên. Bảng kết quả minh họa rõ sự khác biệt giữa hai cột phân khoảng trên cùng một tập số liệu.

:::

<!-- /worked-example -->

## 6. Thiên lệch tổng hợp, nghịch lý Simpson và thẩm định kết luận

Một báo cáo phân tích dữ liệu thất bại thường không phải do mã nguồn tính sai số học, mà do **người phân tích chọn sai thước đo và diễn giải sai bản chất của kết quả**.

### Nghịch lý Simpson: Sự đảo chiều toán học khi gộp nhóm

Một hiện tượng đáng chú ý trong phân tích dữ liệu là **nghịch lý Simpson (Simpson's Paradox)**: Xu hướng tăng trưởng hay suy giảm xuất hiện đồng nhất trong từng nhóm thành phần riêng lẻ có thể bị **đảo ngược hoàn toàn** khi dữ liệu được gộp chung lại ở cấp độ toàn bộ thị trường.

#### Cơ cấu trọng số tác động như thế nào đến giá trị bình quân gộp?

Với k nhóm, gọi $m_i$ là trung bình nhóm i và $w_i$ là tỷ trọng số quan sát của nhóm đó. Trung bình gộp M được khai triển thành:

$$
M = w_1m_1+w_2m_2+\cdots+w_km_k.
$$

Viết gọn, $M=\sum_{i=1}^k w_im_i$. Nếu $n_i$ là số quan sát của nhóm i thì tổng số quan sát là:
$$
N = n_1+n_2+\cdots+n_k.
$$
Với N dương và các nhóm tách biệt bao phủ toàn bộ tập quan sát, trọng số là:
$$
w_i = \frac{n_i}{N} \ge 0.
$$

$$
w_1+w_2+\cdots+w_k = 1.
$$

Ký hiệu tổng cho điều kiện cuối là $\sum_{i=1}^k w_i=1$.

Xét bảng minh họa với trung bình và số quan sát của từng nhóm:

| Phân khúc chỗ ở | Giá trung bình kỳ 1 | Giá trung bình kỳ 2 | Biến động từng nhóm |
| :--- | :---: | :---: | :---: |
| **Căn hộ nguyên căn** | 60 nghìn | 66 nghìn | **Tăng +10%** |
| **Phòng riêng** | 30 nghìn | 33 nghìn | **Tăng +10%** |
| Các quan sát gộp chung | 55 nghìn | 38,5 nghìn | Giảm 30% |

Mỗi trung bình nhóm tăng 10%, nhưng trung bình gộp của tập quan sát giảm 30%. Không được thay các trung bình nhóm trong công thức bằng trung vị nhóm, vì trung vị gộp không được tính bằng phép bình quân có trọng số này.

Nguyên nhân nằm ở **sự thay đổi cơ cấu mẫu giữa hai kỳ khảo sát**: Ở Kỳ 1, căn hộ nguyên căn đắt tiền chiếm đa số (10 căn hộ so với 2 phòng riêng). Sang Kỳ 2, số lượng phòng riêng giá rẻ tăng vọt (10 phòng riêng so với chỉ 2 căn hộ). Vì phòng riêng có mức giá nền thấp hơn nhiều so với căn hộ, sự gia tăng áp đảo về số lượng của chúng đã kéo tụt con số bình quân gộp chung của toàn thành phố.

**Bài học cốt lõi**: Khi phân tích biến động qua thời gian, bắt buộc phải kiểm tra cơ cấu tỷ trọng của các nhóm thành phần trước khi vội vã diễn giải một con số gộp chung.

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-9 -->

::: example Phân rã biến động bình quân gộp và minh chứng nghịch lý Simpson bằng code

Bảng minh họa sau ghi giá trung bình, tính bằng nghìn đồng, và số quan sát ở hai loại chỗ ở qua hai kỳ. Giá của cả hai loại đều tăng 10%. Ta cần xem giá bình quân gộp có tăng theo hay không khi tỷ trọng hai loại thay đổi.

```python
import pandas as pd

df = pd.DataFrame({
    "ky": [1, 1, 2, 2],
    "loai": ["CanHo", "PhongRieng", "CanHo", "PhongRieng"],
    "so_luong": [10, 2, 2, 10],
    "gia_tb": [60.0, 30.0, 66.0, 33.0],
})

# Tính tỷ trọng số lượng và trung bình gộp cho từng kỳ
df["tong_ky"] = df.groupby("ky")["so_luong"].transform("sum")
df["ty_trong"] = df["so_luong"] / df["tong_ky"]
df["dong_gop"] = df["ty_trong"] * df["gia_tb"]

gop = df.groupby("ky")["dong_gop"].sum().reset_index()
bang_kq = pd.DataFrame({
    "ky": gop["ky"],
    "gia_tb_gop": gop["dong_gop"].round(1),
})
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| ky | gia&#95;tb&#95;gop |
| --- | --- |
| 1.0 | 55.0 |
| 2.0 | 38.5 |

</div>

Nghịch lý Simpson là một hiện tượng thống kê trong đó mối quan hệ hoặc xu hướng xuất hiện đồng nhất ở từng nhóm nhỏ có thể bị đảo chiều khi các nhóm được gộp chung lại. Trong bài toán giá thuê phòng được khảo sát, phân khúc căn hộ nguyên căn tăng giá từ 60.0 lên 66.0 nghìn đồng (tăng 10%), và phân khúc phòng riêng cũng tăng giá từ 30.0 lên 33.0 nghìn đồng (tăng 10%).

Kỳ 1 có bình quân gộp `(10 × 60 + 2 × 30) / 12 = 55`. Kỳ 2 có bình quân `(2 × 66 + 10 × 33) / 12 = 38.5`. Phép nhân lấy phần đóng góp của từng nhóm theo số quan sát, rồi phép chia đưa về bình quân trên một quan sát. Hai nhóm đều tăng giá nhưng bình quân gộp lại giảm.

Hiện tượng này được giải thích bởi sự dịch chuyển cơ cấu tỷ trọng của các nhóm thành phần qua hai kỳ. Ở Kỳ 1, phân khúc căn hộ có giá cao chiếm tỷ trọng lớn là 10 trên 12 giao dịch, kéo giá trung bình gộp lên cao. Sang Kỳ 2, phân khúc phòng riêng có giá thấp hơn lại chiếm áp đảo với 10 trên 12 giao dịch, khiến trọng số bình quân bị kéo dồn về phân khúc giá thấp. Phân tích này cho thấy tầm quan trọng của việc kiểm tra cơ cấu trọng số thay vì chỉ dựa vào một chỉ số trung bình gộp duy nhất.

:::

<!-- /worked-example -->

### Chọn kỳ gốc và giới hạn của suy luận nhân quả {#bay-chon-ky-goc-co-loi-va-nguy-bien-nhan-qua}

- **Chọn kỳ gốc**: Nếu chọn một mốc thấp bất thường, tỷ lệ tăng đến kỳ cuối có thể lớn hơn nhiều so với khi chọn mốc khác. Cần nêu kỳ gốc và đối chiếu cả lịch sử, thay vì chỉ giữ đoạn có lợi cho lời kể.
- **Tương quan và nhân quả**: Giá niêm yết của các căn hộ gần ga thấp hơn chưa chứng minh ga làm giảm giá. Hai nhóm có thể khác vị trí, diện tích hoặc chất lượng. Cần dữ liệu và thiết kế phân tích phù hợp để kiểm tra các cách giải thích đó.

### Phân biệt phần trăm (%) và điểm phần trăm (pp)

Giả sử tỷ lệ hủy phòng giảm từ $5\%$ ở quý 1 xuống còn $4\%$ ở quý 2:
- **Chênh lệch tuyệt đối (Điểm phần trăm, percentage points, pp)**:
  $$
  4\%-5\% = -1\%.
  $$
  Đây là mức giảm một điểm phần trăm.
- **Biến động tương đối (Phần trăm, percentage, %)**:
  $$
  \begin{aligned}
  g &= \frac{0{,}04-0{,}05}{0{,}05}, \\
  &= -0{,}20 = -20\%.
  \end{aligned}
  $$

Nếu diễn đạt rằng "tỷ lệ hủy phòng giảm 1%", người đọc trong giới kiểm toán và tài chính có thể hiểu là giảm $1\%$ của mức $5\%$ ban đầu (còn $4{,}95\%$). Hãy luôn ghi rõ cụm từ **điểm phần trăm** khi trừ hai giá trị tỷ lệ cho nhau.

---

<!-- worked-example bai-14-ke-chuyen-bang-du-lieu-worked-10 -->

::: example Tính toán chênh lệch điểm phần trăm và tỷ lệ thay đổi phần trăm

Khi phân tích biến động giữa hai tỷ lệ phần trăm, việc nhầm lẫn giữa mức chênh lệch tuyệt đối và tốc độ thay đổi tương đối dễ gây hiểu lầm số liệu. Đoạn mã tính toán song song điểm phần trăm và phần trăm biến động nhằm phân định rõ ràng hai khái niệm này.

```python
import pandas as pd

df_ty_le = pd.DataFrame({
    "quy": ["Q1", "Q2"],
    "ty_le_huy": [0.05, 0.04],  # 5% và 4%
})

# 1. Chênh lệch tuyệt đối: Điểm phần trăm (percentage points - pp)
pp_diff = (df_ty_le["ty_le_huy"].iloc[1] - df_ty_le["ty_le_huy"].iloc[0]) * 100

# 2. Biến động tương đối: Phần trăm thay đổi (%)
pct_change = (
    (df_ty_le["ty_le_huy"].iloc[1] - df_ty_le["ty_le_huy"].iloc[0])
    / df_ty_le["ty_le_huy"].iloc[0]
) * 100

bang_kq = pd.DataFrame([{
    "q1_pct": df_ty_le["ty_le_huy"].iloc[0] * 100,
    "q2_pct": df_ty_le["ty_le_huy"].iloc[1] * 100,
    "chenh_lech_pp": round(pp_diff, 1),
    "bien_dong_pct": round(pct_change, 1),
}])
print(bang_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| q1&#95;pct | q2&#95;pct | chenh&#95;lech&#95;pp | bien&#95;dong&#95;pct |
| --- | --- | --- | --- |
| 5.0 | 4.0 | -1.0 | -20.0 |

</div>

Phân biệt giữa điểm phần trăm (percentage points - pp) và tỷ lệ phần trăm (percentage - %) là yêu cầu quan trọng trong trình bày số liệu định lượng. Khi một chỉ số vốn đã mang bản chất tỷ lệ (như tỷ lệ hủy đặt phòng hay lãi suất), phép trừ trực tiếp giữa hai mốc thời gian mang đơn vị đo lường là điểm phần trăm chứ không phải là phần trăm thay đổi tương đối.

Từ 5% xuống 4%, tỷ lệ giảm 1 điểm phần trăm. So với mức ban đầu, mức thay đổi tương đối là `(0.04 - 0.05) / 0.05 = -0.2`, tức giảm 20% của chính tỷ lệ đó. Số lượt hủy chưa chắc giảm 20% nếu tổng số đơn của hai quý khác nhau.

Bảng kết quả cung cấp cả hai chỉ số `-1.0 pp` và `-20.0%` để phản ánh đầy đủ hai khía cạnh đo lường khác nhau của cùng một chuỗi quan sát. Trình bày tách bạch cả chênh lệch tuyệt đối theo điểm phần trăm lẫn biến động tương đối theo phần trăm giúp báo cáo phân tích duy trì tính khách quan và chuẩn mực học thuật.

:::

<!-- /worked-example -->

## 7. Khung quy trình thẩm định dữ liệu 4 bước (Data audit framework)

Khi nhận được một bản báo cáo phân tích hoặc khi sử dụng trí tuệ nhân tạo để soạn thảo kết luận, người làm dữ liệu phải thực hiện quy trình thẩm định 4 bước:

1. **Bước 1: Truy số (Number Tracing)**: Viết mã nguồn Python chạy lại từ bảng dữ liệu gốc để xác minh từng con số được nêu. Nếu con số là bịa đặt do ảo giác của mô hình, bác bỏ ngay lập tức.
2. **Bước 2: Kiểm tra phương pháp (Methodological Audit)**: Đánh giá xem thước đo được chọn có phù hợp với phân phối của dữ liệu hay không. Phân phối có bị lệch do ngoại lai không? Kỳ thời gian khảo sát đã khép lại trọn vẹn chưa?
3. **Bước 3: Kiểm tra diễn giải (Interpretive Scrutiny)**: Kiểm tra xem lời kết luận có vượt quá phạm vi bằng chứng không. Có đang nhầm lẫn giữa tương quan với nhân quả hay không?
4. **Bước 4: Phán quyết chuyên gia (Expert Verdict)**: Đưa ra phán quyết chính thức cho từng kết luận độc lập (Giữ nguyên, Sửa đổi, hoặc Chưa thể kiểm chứng).

### Bảng tổng hợp phán quyết thẩm định mẫu

| Kết luận cần thẩm định | Truy số | Kiểm phương pháp | Kiểm diễn giải | Phán quyết chuyên gia |
| :--- | :---: | :---: | :---: | :--- |
| **Giá thuê trung bình 118 nghìn** | Đạt | Không đạt (Ngoại lai làm lệch) | Không đạt | **Sửa đổi**: Bắt buộc dùng giá trung vị để đại diện. |
| **Tháng 6 sụt giảm 28%, thị trường hạ nhiệt** | Đạt | Không đạt (Mốc chụp tháng chưa trọn) | Không đạt | **Chưa thể kiểm chứng**: Chờ mốc chụp đầy đủ. |
| **Phòng gần tàu điện rẻ hơn, ga làm giảm giá** | Đạt | Cần lưu ý (Đo gián tiếp qua từ khóa) | Không đạt (Ngụy biện nhân quả) | **Sửa đổi**: Chỉ khẳng định hai yếu tố đi kèm. |

Bài học quan trọng nhất: **Trong cả ba trường hợp có tì vết, các con số tính toán đều hoàn toàn chính xác, trong khi lỗi sai thực sự nằm ở phương pháp chọn thước đo và cách diễn giải bằng lời**.

---

## 9. Tổng kết

| Chủ đề phân tích | Công cụ kỹ thuật chủ yếu | Bài học phương pháp luận cốt lõi |
| :--- | :--- | :--- |
| **Nhật ký máy chủ** | `fillna()`, `replace()`, `str.contains()` | Luôn phân biệt ô khuyết thiếu từ nguồn với chuỗi rỗng do hệ thống ghi nhận. |
| **Đánh giá & Thị hiếu** | `pivot_table()`, `std()` | Độ lệch chuẩn phản ánh mức độ bất đồng quan điểm giữa các nhóm người dùng. |
| **Xu hướng đặt tên** | `transform()`, `str[-1]` | Chuẩn hóa tỷ trọng trước khi so sánh chuỗi thời gian, đồng thời phân tích âm cuối để phát hiện quy luật. |
| **Dữ liệu phân cấp** | `pd.json_normalize()`, tách bảng | Phẳng hóa dữ liệu JSON thành các bảng quan hệ liên kết bằng khóa duy nhất. |
| **Dòng tiền & Đóng góp** | `pd.cut()`, `map()` | Phân khoảng số tiền tăng dần theo cấp số nhân để xử lý dữ liệu lệch phải. |
| **Thẩm định kết luận** | Bốn bước: Truy số, Phương pháp, Diễn giải, Phán quyết | Luôn cảnh giác với nghịch lý Simpson. Số đúng chưa đủ, phương pháp và lập luận phải chuẩn xác. |

## Tài liệu tham khảo

1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Chapter 13: Data Analysis Examples. URL: [https://wesmckinney.com/book/data-analysis-examples](https://wesmckinney.com/book/data-analysis-examples).
2. Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN: *Giáo trình Lập trình xử lý dữ liệu (Bài 14: Kể chuyện bằng dữ liệu và thẩm định phân tích AI)*. Nội dung thẩm định và nghịch lý tổng hợp được chuyển thể theo giấy phép [CC BY-NC-SA 4.0](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).
3. Edward H. Simpson, *The Interpretation of Interaction in Contingency Tables*, Journal of the Royal Statistical Society, 1951.
4. Darrell Huff, *How to Lie with Statistics*, W. W. Norton & Company.

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 8. Bài tập thực hành

::: exercise Bài tập 1: Đo lường mức độ bất đồng quan điểm trong đánh giá dịch vụ
Một chuỗi nhà hàng thu thập dữ liệu đánh giá của khách hàng về các chi nhánh, được lưu trong bảng sau:

```python
df_danh_gia = pd.DataFrame({
    "chi_nhanh": ["A", "A", "A", "A", "B", "B", "B", "B"],
    "khach_hang": ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"],
    "nhom_khach": ["Tre", "TrungNien", "Tre", "TrungNien", "Tre", "TrungNien", "Tre", "TrungNien"],
    "diem": [5, 1, 5, 2, 4, 3, 4, 3]
})
```

1. Tính điểm đánh giá trung bình của từng chi nhánh theo nhóm khách hàng bằng `pivot_table`.
2. Tính độ lệch chuẩn của điểm số tại mỗi chi nhánh. Chi nhánh nào có sự phân hóa quan điểm mạnh mẽ hơn?
:::

::: solution Lời giải chi tiết
Mã nguồn thực hiện:

```python
# 1. Bảng xoay chiều điểm trung bình theo nhóm khách
bang_pivot = df_danh_gia.pivot_table(
    index="chi_nhanh",
    columns="nhom_khach",
    values="diem",
    aggfunc="mean"
)
print("Điểm trung bình theo nhóm khách:")
print(bang_pivot)

# 2. Độ lệch chuẩn đo lường bất đồng quan điểm
do_lech_chuan = df_danh_gia.groupby("chi_nhanh")["diem"].std()
print("Độ lệch chuẩn điểm số của từng chi nhánh:")
print(do_lech_chuan)
```

Kết quả phân tích:
- Tại chi nhánh A: Điểm trung bình của nhóm Khách Trẻ là 5,0 trong khi nhóm Trung Niên là 1,5. Độ lệch chuẩn đạt xấp xỉ 2,06. Chi nhánh A có sự bất đồng quan điểm sâu sắc giữa các thế hệ khách hàng.
- Tại chi nhánh B: Điểm trung bình của hai nhóm lần lượt là 4,0 và 3,0, độ lệch chuẩn chỉ là xấp xỉ 0,58. Khách hàng tại chi nhánh B có mức độ đồng thuận cao về chất lượng dịch vụ.
:::

::: exercise Bài tập 2: Thẩm định biến động doanh thu và nhận diện nghịch lý Simpson
Một công ty thương mại điện tử công bố bảng số liệu sau về giá trị đơn hàng trung bình giữa hai năm:

```python
# Năm 1: 100 đơn hàng điện tử (trung bình 200$), 20 đơn hàng sách (trung bình 20$)
# Năm 2: 20 đơn hàng điện tử (trung bình 220$), 100 đơn hàng sách (trung bình 22$)
```

1. Tính giá trị đơn hàng trung bình của từng ngành hàng giữa hai năm. Mỗi ngành hàng tăng trưởng bao nhiêu phần trăm?
2. Tính giá trị đơn hàng trung bình gộp của toàn bộ công ty trong từng năm. Chỉ ra hiện tượng nghịch lý Simpson và giải thích nguyên nhân bằng cơ cấu trọng số.
:::

::: solution Lời giải chi tiết
Mã nguồn tính toán:

```python
# Năm 1
tb_dt_nam1 = 200
tb_sach_nam1 = 20
tong_don_nam1 = 100 + 20
tb_gop_nam1 = (100 * tb_dt_nam1 + 20 * tb_sach_nam1) / tong_don_nam1

# Năm 2
tb_dt_nam2 = 220
tb_sach_nam2 = 22
tong_don_nam2 = 20 + 100
tb_gop_nam2 = (20 * tb_dt_nam2 + 100 * tb_sach_nam2) / tong_don_nam2

print(f"Năm 1: Điện tử {tb_dt_nam1}$, Sách {tb_sach_nam1}$, Bình quân gộp: {tb_gop_nam1:.2f}$")
print(f"Năm 2: Điện tử {tb_dt_nam2}$, Sách {tb_sach_nam2}$, Bình quân gộp: {tb_gop_nam2:.2f}$")

tang_dt = (tb_dt_nam2 / tb_dt_nam1 - 1) * 100
tang_sach = (tb_sach_nam2 / tb_sach_nam1 - 1) * 100
tang_gop = (tb_gop_nam2 / tb_gop_nam1 - 1) * 100

print(f"Tăng trưởng Điện tử: +{tang_dt:.1f}%")
print(f"Tăng trưởng Sách: +{tang_sach:.1f}%")
print(f"Tăng trưởng Bình quân gộp toàn công ty: {tang_gop:.1f}%")
```

Kết quả:
- Ngành hàng Điện tử tăng trưởng: $+10{,}0\%$.
- Ngành hàng Sách tăng trưởng: $+10{,}0\%$.
- Bình quân gộp toàn công ty giảm từ $170{,}00$ USD xuống $55{,}00$ USD, tương đương giảm khoảng $67{,}6\%$.
- Giải thích: Nghịch lý Simpson xuất hiện do cơ cấu đơn hàng đảo chiều mạnh mẽ. Năm 1, ngành điện tử giá trị cao chiếm $83{,}3\%$ tổng số đơn. Sang năm 2, ngành sách giá trị thấp chiếm tới $83{,}3\%$ tổng số đơn. Sự thay đổi trọng số phân bổ này đã kéo sụt con số trung bình gộp dù từng ngành hàng đều tăng giá.
:::

---



<!--@include: ../../../raw_materials/xu-ly-du-lieu/practice/aggregation-figure.md-->

<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-14">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-14.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Chapter 13: Data Analysis Examples. URL: [https://wesmckinney.com/book/data-analysis-examples](https://wesmckinney.com/book/data-analysis-examples).
2. Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN: *Giáo trình Lập trình xử lý dữ liệu (Bài 14: Kể chuyện bằng dữ liệu và thẩm định phân tích AI)*. Nội dung thẩm định và nghịch lý tổng hợp được chuyển thể theo giấy phép [CC BY-NC-SA 4.0](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).
3. Edward H. Simpson, *The Interpretation of Interaction in Contingency Tables*, Journal of the Royal Statistical Society, 1951.
4. Darrell Huff, *How to Lie with Statistics*, W. W. Norton & Company.

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
