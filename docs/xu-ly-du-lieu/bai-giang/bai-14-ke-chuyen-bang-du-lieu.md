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

### Đo lường tính đa dạng đặt tên

Một câu hỏi xã hội học đáng quan tâm: Thị hiếu đặt tên của cha mẹ ngày càng phong phú hay ngày càng thu hẹp?
Ta có thể đo lường tính đa dạng bằng cách tính **số lượng tên phổ biến nhất cần thiết để chiếm đủ 50% tổng số trẻ sinh ra trong năm**. Ở thế kỷ 19, chỉ cần vài chục tên đứng đầu đã chiếm tới một nửa số trẻ em. Đến thế kỷ 21, số lượng tên cần thiết đã tăng lên hàng trăm, phản ánh sự mở rộng về tính đa dạng khi lựa chọn tên gọi.

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

### Bẫy chọn kỳ gốc có lợi và ngụy biện nhân quả

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

<!--@include: ../../../raw_materials/xu-ly-du-lieu/practice/iai-bc-chapter-13.md-->


<!--@include: ../../../raw_materials/xu-ly-du-lieu/practice/aggregation-figure.md-->

## Tài liệu tham khảo

1. Wes McKinney, *Python for Data Analysis*, 3rd Edition, Chapter 13: Data Analysis Examples. URL: [https://wesmckinney.com/book/data-analysis-examples](https://wesmckinney.com/book/data-analysis-examples).
2. Viện Trí tuệ Nhân tạo, Trường Đại học Công nghệ, ĐHQGHN: *Giáo trình Lập trình xử lý dữ liệu (Bài 14: Kể chuyện bằng dữ liệu và thẩm định phân tích AI)*. Nội dung thẩm định và nghịch lý tổng hợp được chuyển thể theo giấy phép [CC BY-NC-SA 4.0](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).
3. Edward H. Simpson, *The Interpretation of Interaction in Contingency Tables*, Journal of the Royal Statistical Society, 1951.
4. Darrell Huff, *How to Lie with Statistics*, W. W. Norton & Company.

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>
