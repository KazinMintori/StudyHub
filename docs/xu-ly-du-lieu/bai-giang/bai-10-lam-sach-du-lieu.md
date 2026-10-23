---
course: xu-ly-du-lieu
lecture: bai-10-lam-sach-du-lieu
section: lecture
title: "Làm sạch, chuẩn bị và xử lý chuỗi"
prerequisites: ["dataframe"]
lessonStatus: ready
hasChapterExercises: true
description: "Phương pháp luận làm sạch dữ liệu: Xử lý giá trị khuyết thiếu và biến dạng phân phối, biến đổi dữ liệu, kiểu dữ liệu mở rộng, biểu thức chính quy và hàm chuỗi vector hóa, kiểu phân loại categorical, xác thực văn bản sang bảng và hệ thống kiểm định toàn vẹn."
---


<div class="lecture-notes-content">

Xét bảng dữ liệu đặt phòng khách sạn được xuất từ nhiều chi nhánh khác nhau. Bảng này xuất hiện ô trống ở cột giá, chuỗi văn bản không đồng nhất như `' Entire home '` và `'entire HOME'`, các bản ghi trùng lặp do gửi hai lần qua mạng, hoặc các mức giá ngoại lai gấp hàng chục lần mức thông thường. Nếu đưa trực tiếp dữ liệu thô này vào các phép toán thống kê hoặc mô hình dự đoán, các kết quả tính toán sẽ bị sai lệch nghiêm trọng.

Tuy nhiên, làm sạch dữ liệu không phải là việc xóa bỏ tùy tiện mọi dòng dữ liệu có vẻ bất thường. Quá trình này đòi hỏi sự cẩn trọng: Nhận diện cơ chế phát sinh dữ liệu thiếu, phân định giữa bản ghi gửi lặp và các sự kiện hợp lệ độc lập, chuẩn hóa văn bản bằng biểu thức chính quy, áp dụng kiểu dữ liệu mở rộng và kiểu phân loại đúng chỗ, đồng thời đo lường độ chính xác của các bước trích xuất bằng các chỉ số thống kê minh bạch. Bài học này làm rõ toàn bộ hệ thống kỹ thuật chuẩn bị dữ liệu trong thư viện pandas.

---

## 1. Xử lý giá trị khuyết thiếu (Handling Missing Data)

Trong pandas, giá trị khuyết thiếu được biểu diễn chủ yếu bằng `np.nan` (đối với dữ liệu số thực), `pd.NA` (đối với kiểu dữ liệu mở rộng có hỗ trợ giá trị rỗng), hoặc `pd.NaT` (đối với dữ liệu thời gian).

### 1.1. Lọc bỏ giá trị khuyết thiếu với `dropna`

Hàm `isna()` và `notna()` là hai công cụ nền tảng trả về mặt nạ boolean để kiểm tra từng phần tử. Khi cần loại bỏ các bản ghi chứa ô trống, phương thức `dropna()` cung cấp các tham số điều khiển tinh tế:
- `axis=0` (mặc định): Loại bỏ theo hàng, trong khi `axis=1` là loại bỏ theo cột.
- `how="any"` (mặc định): Xóa nếu hàng hoặc cột chứa ít nhất một ô trống. Trái lại, `how="all"` chỉ xóa khi toàn bộ các ô trên hàng hoặc cột đó đều trống.
- `thresh=k`: Chỉ giữ lại các hàng hoặc cột có ít nhất $k$ giá trị hợp lệ (khác NA).
- `subset`: Chỉ xét sự hiện diện của ô trống trên một danh sách các cột cụ thể, ngăn ngừa việc xóa nhầm các dòng chỉ vì thiếu dữ liệu ở các cột phụ trợ.

```python
import numpy as np
import pandas as pd

du_lieu = pd.DataFrame({
    "ma_phong": ["P1", "P2", "P3", "P4"],
    "gia": [100.0, np.nan, 200.0, np.nan],
    "so_phong": [1, 2, np.nan, np.nan],
    "ghi_chu": [np.nan, "gần biển", np.nan, np.nan]
})

# Chỉ loại bỏ những hàng thiếu giá trị ở cột 'gia'
df_loc_gia = du_lieu.dropna(subset=["gia"])
print("Bảng sau khi lọc theo cột gia:")
print(df_loc_gia)
assert len(df_loc_gia) == 2
```

<!-- worked-example bai-10-lam-sach-du-lieu-worked-1 -->

::: example Lọc bỏ hàng theo ngưỡng số lượng giá trị hợp lệ với tham số thresh

Trong một bảng điểm tuyển sinh gồm nhiều môn thi, một thí sinh vắng thi một môn vẫn được giữ lại nếu có đủ điểm của hai môn còn lại. Ta sử dụng tham số thresh trong hàm dropna để giữ lại những hàng đạt tối thiểu hai giá trị hợp lệ trên tập hợp các cột môn học.

```python
import numpy as np
import pandas as pd

df_diem = pd.DataFrame({
    "ma": ["A1", "A2", "A3", "A4"],
    "toan": [8.0, np.nan, np.nan, 9.0],
    "van": [7.5, 6.0, np.nan, np.nan],
    "anh": [9.0, np.nan, np.nan, 7.0]
})

df_loc = df_diem.dropna(subset=["toan", "van", "anh"], thresh=2)
print(df_loc)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| Chỉ mục | ma | toan | van | anh |
| --- | --- | --- | --- | --- |
| 0 | A1 | 8.0 | 7.5 | 9.0 |
| 3 | A4 | 9.0 | (thiếu) | 7.0 |

</div>

Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.

Mặc định `dropna()` bỏ hàng có bất kỳ ô thiếu nào trong phạm vi đang xét. Điều kiện đó phù hợp khi mọi trường đều bắt buộc. Trong bảng này, quy tắc minh họa chỉ yêu cầu ít nhất hai trong ba điểm, nên ta cần một điều kiện khác.

Tham số `thresh` cung cấp cơ chế lọc dựa trên ngưỡng số lượng: Thay vì kiểm tra xem có ô `NaN` nào hay không, tham số này yêu cầu hàng phải có ít nhất một số lượng giá trị không khuyết nhất định. Khi ta thiết lập `thresh=2` trên danh sách các cột môn thi, pandas sẽ đếm số phần tử hợp lệ trong mỗi dòng.

Xét các dòng của bảng điểm: Thí sinh A1 có đủ 3 điểm môn thi nên được giữ lại. Thí sinh A2 chỉ có 1 điểm hợp lệ (môn Văn) nên bị loại bỏ. Thí sinh A3 khuyết cả 3 môn nên bị loại. Thí sinh A4 có 2 điểm hợp lệ (môn Toán và môn Anh) nên vẫn được giữ lại trong danh sách.

`subset` giới hạn việc đếm vào ba môn, không tính cột mã. `thresh=2` yêu cầu ít nhất hai ô không thiếu. Không truyền đồng thời `how` và `thresh`, vì pandas không cho kết hợp hai cách chỉ định điều kiện này.

:::

<!-- /worked-example -->

### 1.2. Điền giá trị khuyết thiếu với `fillna`, `ffill` và `bfill`

Thay vì xóa bỏ, ta có thể điền giá trị cho các ô trống:
- Điền giá trị cố định: Sử dụng `df.fillna(0)` hoặc truyền một từ điển ánh xạ riêng từng cột như `df.fillna({"gia": 150, "so_phong": 1})`.
- Điền theo thứ tự quan sát: Trong pandas 3, tham số `method` trong `fillna` đã bị loại bỏ hoàn toàn. Người dùng sử dụng trực tiếp hai phương thức riêng biệt là `df.ffill()` (lấy giá trị hợp lệ liền trước điền tới) hoặc `df.bfill()` (lấy giá trị hợp lệ liền sau điền lùi lại), hỗ trợ tham số `limit` để khống chế số bước điền liên tiếp tối đa.
- Điền bằng đại lượng thống kê trung tâm: Sử dụng giá trị trung bình (`mean()`) hoặc giá trị trung vị (`median()`) của cột.

<!-- worked-example bai-10-lam-sach-du-lieu-worked-2 -->

::: example Điền dữ liệu thiếu theo từng cột và kiểm soát bước truyền với ffill

Trong chuỗi dữ liệu giá theo phiên, việc thiếu giá trị đo lường có thể tạm thời được bù đắp bằng giá trị hợp lệ gần nhất phía trước. Tuy nhiên, nếu khoảng gián đoạn kéo dài, việc truyền giá liên tục sẽ tạo ra thông tin giả định không có cơ sở. Ta áp dụng ffill có giới hạn limit và điền giá trị mặc định cho cột danh mục.

```python
import numpy as np
import pandas as pd

df_gia = pd.DataFrame({
    "ngay": ["T2", "T3", "T4", "T5"],
    "gia_goc": [100.0, np.nan, np.nan, 120.0],
    "kho": ["K1", np.nan, "K2", np.nan]
})

df_gia["gia_ffill"] = df_gia["gia_goc"].ffill(limit=1)
df_gia["kho"] = df_gia["kho"].fillna("ChuaGhi")
print(df_gia)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| ngay | gia&#95;goc | kho | gia&#95;ffill |
| --- | --- | --- | --- |
| T2 | 100.0 | K1 | 100.0 |
| T3 | (thiếu) | ChuaGhi | 100.0 |
| T4 | (thiếu) | K2 | (thiếu) |
| T5 | 120.0 | ChuaGhi | 120.0 |

</div>

Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.

Phương thức `ffill` (forward fill) sao chép giá trị hợp lệ gần nhất phía trước theo chiều chỉ mục hiện hành để lấp vào vị trí trống tiếp theo. Tuy nhiên, phương thức này không tự kiểm tra xem khoảng cách thời gian thực tế có phải là 1 ngày hay không: Nó thuần túy đếm số dòng khuyết thiếu liên tiếp theo đúng thứ tự đang sắp xếp của bảng.

Thứ tự hàng cần phản ánh đúng chiều mà giá trị có thể truyền đi. Nếu muốn diễn giải `limit=1` là tối đa một ngày, còn cần bảo đảm mỗi hàng tương ứng một ngày liên tiếp. `ffill` tự nó không xác minh giả định đó và cũng không chứng minh giá cũ vẫn đúng ở ngày mới.

Tham số `limit=1` giới hạn số bước truyền liên tiếp tối đa là 1 dòng: So sánh giữa cột ban đầu `gia_goc` và cột kết quả `gia_ffill` cho thấy ngày T3 được điền giá trị 100.0 từ ngày T2. Đến ngày T4, do đã chạm ngưỡng giới hạn 1 bước, ô dữ liệu vẫn giữ nguyên là `NaN` thay vì tiếp tục kéo dài giá trị cũ.

Đối với cột biến định tính `kho`, việc truyền giá trị xuôi thường không phù hợp với quy trình nghiệp vụ. Ta sử dụng `fillna('ChuaGhi')` để gán một nhãn phân loại rõ ràng, phân biệt giữa các dòng đã có mã kho và các dòng chưa xác định kho lưu trữ.

:::

<!-- /worked-example -->

### 1.3. Nguyên nhân khuyết thiếu và ảnh hưởng của việc điền dữ liệu {#_1-3-phan-loai-nguyen-nhan-khuyet-thieu-va-cam-bay-khi-đien-gia-tri}

Trước khi quyết định loại bỏ hay điền giá trị cho các ô trống, nhà phân tích cần xem xét bản chất của dữ liệu thiếu:
1. **Thiếu ngẫu nhiên do kỹ thuật**: Quá trình đo đạc hoặc truyền tải gói tin qua mạng gặp sự cố cục bộ, không phụ thuộc vào bản thân giá trị cần đo. Trong trường hợp này, việc loại bỏ dòng chỉ làm giảm kích thước mẫu quan sát mà không làm lệch ước lượng trung tâm.
2. **Thiếu có điều kiện theo thuộc tính khác**: Xác suất thiếu gắn liền với một đặc tính đã quan sát được (chẳng hạn cơ sở lưu trú ở vùng ngoại ô ít khi cập nhật thông tin tiện nghi hơn cơ sở ở trung tâm thành phố).
3. **Thiếu gắn liền với giá trị tiềm ẩn**: Ô trống xuất hiện chính vì giá trị của nó rơi vào khoảng khó ghi nhận hoặc người cung cấp chủ động bỏ trống trường dữ liệu đó. Việc điền giá trị đơn giản trong tình huống này có thể làm biến dạng bức tranh thống kê thực tế.

Điền các ô thiếu bằng cùng một giá trị trung bình tạo thêm các quan sát ngay tại tâm của mẫu. Vì thế, độ phân tán của cột sau khi điền có thể nhỏ hơn ban đầu. Xét phép tính sau:

```python
s = pd.Series([10.0, 12.0, 14.0, 16.0, 18.0, np.nan])

print("Giá trị trung bình gốc:", s.mean())  # 14.0
print("Phương sai mẫu gốc:", s.var())        # 10.0

# Điền giá trị bằng giá trị trung bình mẫu:
s_dien_tb = s.fillna(s.mean())
print("Giá trị trung bình sau khi điền:", s_dien_tb.mean())  # 14.0
print("Phương sai mẫu sau khi điền:", s_dien_tb.var())       # 8.0
```

> [!WARNING] Phương sai thay đổi sau khi điền dữ liệu
> Khi điền giá trị trung bình $\bar{x} = 14{,}0$ vào vị trí khuyết thiếu, độ lệch của điểm dữ liệu mới này so với tâm bằng đúng $0$: $(14{,}0 - 14{,}0)^2 = 0$. Tổng bình phương độ lệch không đổi, nhưng kích thước mẫu $N$ lại tăng từ $5$ lên $6$. Hệ quả là phương sai mẫu bị kéo tụt nhân tạo từ $10{,}0$ xuống $8{,}0$. Dữ liệu trông có vẻ ít phân tán hơn thực tế, làm thu hẹp khoảng tin cậy một cách giả tạo và dễ dẫn đến kết luận kiểm định sai lệch.

---

## 2. Biến đổi dữ liệu (Data Transformation)

Biến đổi dữ liệu là bước tái cấu trúc và chuẩn hóa các giá trị trước khi đưa vào mô hình phân tích chuyên sâu.

### 2.1. Loại bỏ bản ghi trùng lặp: Đơn vị quan sát và xung đột khóa

Phương thức `duplicated()` trả về mảng boolean đánh dấu các dòng trùng lặp, và `drop_duplicates()` loại bỏ các dòng này:
- **Đơn vị quan sát và bản sao hoàn toàn**: Khi hai hàng giống hệt nhau trên mọi cột đang lưu, chỉ có thể xem đó là bản sao lỗi nếu đơn vị quan sát (*Unit of Observation*) xác nhận mỗi sự kiện kinh tế chỉ được phép xuất hiện duy nhất một lần. Nếu bảng dữ liệu ghi nhận giao dịch mua sắm nhưng không lưu mã đơn hàng hoặc mốc thời gian chi tiết từng giây, hai dòng hoàn toàn giống nhau có thể là hai giao dịch mua hợp lệ và độc lập của cùng một khách hàng. Do đó, việc gọi `drop_duplicates()` trên toàn bộ các cột chỉ an toàn khi đã xác định rõ đơn vị quan sát hoặc có xác nhận về lỗi truyền lặp bản ghi.
- **Xung đột thuộc tính trên khóa (Key Conflicts)**: Hai hàng có cùng mã định danh `id` nhưng các trường thuộc tính khác (như giá hay địa chỉ) lại mang giá trị khác nhau. Tuyệt đối không gọi `drop_duplicates(subset=["id"])` một cách vội vàng vì thao tác đó sẽ âm thầm loại bỏ một trong hai dữ liệu mâu thuẫn. Cách tiếp cận phù hợp là gắn cờ cảnh báo để đối soát nguồn gốc, hoặc sử dụng mốc thời gian để chỉ giữ lại bản ghi cập nhật sau cùng (`keep="last"`).

```python
bang_giao_dich = pd.DataFrame({
    "ma_don": ["D1", "D1", "D2", "D2"],
    "khach": ["An", "An", "Bình", "Bình"],
    "so_tien": [100, 100, 200, 250]
})

# Quét bản sao hoàn toàn trên tất cả các cột
trung_hoan_toan = bang_giao_dich.duplicated()
print("Số dòng trùng hoàn toàn:", int(trung_hoan_toan.sum())) # 1 dòng (D1)

# Phát hiện xung đột khóa trên các dòng không trùng hoàn toàn
bang_khong_trung = bang_giao_dich[~trung_hoan_toan]
xung_dot = bang_khong_trung.duplicated(subset=["ma_don"], keep=False)
print("Các dòng xung đột khóa cần thẩm định:")
print(bang_khong_trung[xung_dot])
```

<!-- worked-example bai-10-lam-sach-du-lieu-worked-3 -->

::: example Nhận diện bản ghi trùng lặp và kiểm soát vị trí lưu giữ với keep

Khi hệ thống đồng bộ dữ liệu giao dịch phát lại các gói tin cũ, bảng ghi nhận có thể xuất hiện các dòng trùng lặp cùng một mã khách hàng và lần thanh toán. Ta sử dụng phương thức duplicated với keep=False để hiển thị mặt nạ kiểm tra và dùng drop_duplicates với keep='last' để giữ lại bản ghi ở vị trí cuối.

```python
import pandas as pd

df_gd = pd.DataFrame({
    "khach": ["An", "Binh", "An", "An"],
    "lan": [1, 1, 2, 2],
    "tien": [50, 70, 60, 60]
})

mask_trung = df_gd.duplicated(subset=["khach", "lan"], keep=False)
print("Mat na cac dong trung lap:")
print(mask_trung)

df_sach = df_gd.drop_duplicates(subset=["khach", "lan"], keep="last")
print("Bang sau khi giu dong cuoi:")
print(df_sach)
```

Kết quả khi chạy đoạn mã trên:

```text
Mat na cac dong trung lap:
```

<div class="data-worked-table">

| Giá trị |
| --- |
| `False` |
| `False` |
| `True` |
| `True` |

</div>

```text
Bang sau khi giu dong cuoi:
```

<div class="data-worked-table data-worked-table-wide">

| Chỉ mục | khach | lan | tien |
| --- | --- | --- | --- |
| 0 | An | 1 | 50 |
| 1 | Binh | 1 | 70 |
| 3 | An | 2 | 60 |

</div>

Hiện tượng trùng lặp trong dữ liệu bảng thường gắn với định nghĩa đơn vị quan sát trên một tập cột khóa cụ thể, chẳng hạn cặp mã `khach` và `lan`. Các dòng trùng lặp không nhất thiết phải xung đột về giá trị số tiền: Trong ví dụ trên, hai dòng của khách An ở lần 2 đều có cùng số tiền 60.

Phương thức `df_gd.duplicated(subset=['khach', 'lan'], keep=False)` trả về một Series boolean đánh dấu `True` cho toàn bộ các dòng tham gia vào quan hệ trùng khóa. Việc in mặt nạ boolean này giúp người phân tích kiểm tra trực tiếp các vị trí bị lặp trong tập dữ liệu.

Tham số `keep='last'` trong phương thức `drop_duplicates` chỉ thị giữ lại dòng xuất hiện sau cùng theo thứ tự hàng hiện thời của bảng. Cần lưu ý rằng dòng cuối cùng trong bảng không đồng nghĩa với bản ghi mới nhất theo mốc thời gian trừ khi bảng đã được sắp xếp trước theo cột thời gian giao dịch.

Kết quả trả về là một bảng dữ liệu sạch với ba dòng đại diện cho ba lần giao dịch: Dòng số 2 bị loại bỏ và dòng số 3 được giữ lại, bảo toàn chỉ mục hàng gốc để phục vụ các bước đối chiếu tiếp theo.

:::

<!-- /worked-example -->

### 2.2. Biến đổi bằng hàm hoặc ánh xạ (`map`)

Phương thức `map()` trên Series cho phép ánh xạ từng giá trị sang một giá trị mới thông qua một hàm hoặc một từ điển tra cứu:

```python
du_lieu_mon = pd.DataFrame({
    "ten": ["thịt bò", "cá hồi", "thịt lợn", "thịt bò"],
    "khoi_luong": [4.0, 3.0, 12.0, 6.0]
})

anh_xa_nguon = {
    "thịt bò": "gia súc",
    "cá hồi": "hải sản",
    "thịt lợn": "gia súc"
}

du_lieu_mon["nguon_goc"] = du_lieu_mon["ten"].map(anh_xa_nguon)
print(du_lieu_mon)
```

<!-- worked-example bai-10-lam-sach-du-lieu-worked-4 -->

::: example Ánh xạ cột với Series.map và biến đổi bảng với DataFrame.map

Khi chuẩn hóa dữ liệu, mã vùng cần được chuyển đổi thành tên địa phương qua bảng tra cứu từ điển, đồng thời các cột số thực cần được làm tròn đồng nhất một chữ số thập phân. Ta kết hợp Series.map để ánh xạ cột và DataFrame.map để áp dụng hàm trên từng ô dữ liệu.

```python
import pandas as pd

df_sp = pd.DataFrame({
    "ma": ["HN", "SG"],
    "x": [1.234, 5.678],
    "y": [9.101, 3.141]
})

tra_cuu = {"HN": "HaNoi", "SG": "SaiGon"}
df_sp["ten_vung"] = df_sp["ma"].map(tra_cuu)

df_tron = df_sp[["x", "y"]].map(lambda v: round(v, 1))
print(df_sp)
print(df_tron)
print(df_sp[["x", "y"]].round(1))
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table data-worked-table-wide">

| ma | x | y | ten&#95;vung |
| --- | --- | --- | --- |
| HN | 1.234 | 9.101 | HaNoi |
| SG | 5.678 | 3.141 | SaiGon |

</div>

<div class="data-worked-table">

| x | y |
| --- | --- |
| 1.2 | 9.1 |
| 5.7 | 3.1 |

</div>

<div class="data-worked-table">

| x | y |
| --- | --- |
| 1.2 | 9.1 |
| 5.7 | 3.1 |

</div>

Phương thức `Series.map` nhận một từ điển hoặc một hàm để ánh xạ từng phần tử của một Series sang giá trị mới: Biểu thức `df_sp['ma'].map(tra_cuu)` đối chiếu từng mã vùng với từ điển để sinh ra cột `ten_vung`. Nếu một giá trị không xuất hiện trong từ điển, `Series.map` sẽ gán giá trị `NaN` tại vị trí đó.

Trên phạm vi toàn bảng, phương thức `DataFrame.map` áp dụng một hàm Python lên từng ô dữ liệu đơn lẻ: Đoạn mã áp dụng hàm lambda làm tròn trên tập con hai cột `['x', 'y']` để đưa các giá trị số thực về một chữ số thập phân.

Đối với thao tác làm tròn số thực đơn thuần, pandas cung cấp phương thức chuyên dụng `df[['x', 'y']].round(1)`: Phương thức này biểu đạt trực tiếp mục đích nghiệp vụ mà không cần truyền hàm lambda qua `map`.

Sự phân biệt giữa các phương thức nằm ở phạm vi áp dụng: `Series.map` hoạt động trên một cột, `DataFrame.map` duyệt qua từng ô của bảng, và các phương thức chuyên dụng như `round` xử lý trực tiếp trên mảng số liệu mà không cần tạo hàm trung gian.

:::

<!-- /worked-example -->

### 2.3. Thay thế giá trị và đổi tên chỉ mục trục

- Phương thức `replace()` cho phép thay thế các giá trị cụ thể bằng giá trị mới, hỗ trợ danh sách hoặc từ điển.
- Phương thức `rename(index=..., columns=...)` cho phép đổi tên các nhãn hàng và nhãn cột mà không cần gán lại toàn bộ thuộc tính trục:

```python
du_lieu_mon = du_lieu_mon.rename(columns={"ten": "ten_thuc_pham", "khoi_luong": "so_kg"})
print(du_lieu_mon.columns.tolist())
assert "ten_thuc_pham" in du_lieu_mon.columns
```

<!-- worked-example bai-10-lam-sach-du-lieu-worked-5 -->

::: example Thay thế nhiều giá trị bằng từ điển và chuẩn hóa tên cột với rename

Một hệ thống cũ lưu trữ trạng thái người dùng bằng các chuỗi tiếng Anh viết thường và tên cột mang tiền tố kỹ thuật. Để chuẩn hóa báo cáo theo ngôn ngữ nghiệp vụ, ta sử dụng phương thức replace với từ điển ánh xạ để thay thế nhiều giá trị đồng thời và dùng rename để cập nhật lại tiêu đề cột.

```python
import pandas as pd

df_nv = pd.DataFrame({
    "ma_nv": [1, 2, 3],
    "trang_thai": ["active", "pending", "unknown"]
})

df_nv["trang_thai"] = df_nv["trang_thai"].replace({
    "active": "HoatDong",
    "pending": "ChoXuLy",
    "unknown": "KhongRo"
})

df_nv = df_nv.rename(columns={"ma_nv": "id", "trang_thai": "status"})
print(df_nv)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| id | status |
| --- | --- |
| 1 | HoatDong |
| 2 | ChoXuLy |
| 3 | KhongRo |

</div>

Phương thức `Series.replace` khác biệt với `Series.map` ở cơ chế xử lý các giá trị không khớp: Khi dùng `map` với từ điển, bất kỳ giá trị nào không nằm trong danh sách khóa đều bị biến thành `NaN`. Ngược lại, `replace` chỉ thay thế những phần tử trùng khớp với từ điển và giữ nguyên các giá trị còn lại.

Ta truyền từ điển chuyển đổi trực tiếp vào `replace`: Chuỗi `'active'` được đổi thành `'HoatDong'`, `'pending'` thành `'ChoXuLy'`, và `'unknown'` thành `'KhongRo'`. Phép biến đổi diễn ra trên toàn bộ cột mà không cần viết các cấu trúc rẽ nhánh điều kiện lặp lại.

Phương thức `df.rename` cung cấp cơ chế cập nhật nhãn trục: Thông qua tham số `columns={'ma_nv': 'id', 'trang_thai': 'status'}`, ta đổi tên hai cột kỹ thuật thành các định danh ngắn gọn và nhất quán với quy ước của hệ thống mới.

Kết quả thu được là một `DataFrame` mới có tên cột rõ ràng và nội dung trạng thái được quy chuẩn, bảo toàn toàn bộ số lượng dòng và chỉ mục hàng ban đầu.

:::

<!-- /worked-example -->

### 2.4. Rời rạc hóa và chia khoảng (Discretization and Binning)

Để nhóm các biến số thực liên tục thành các khoảng phân loại (ví dụ phân nhóm độ tuổi hoặc mức giá), pandas cung cấp hai hàm:
- `pd.cut()`: Chia theo các điểm cắt cố định do người dùng xác định. Tham số `right=False` quy định khoảng nửa mở dạng $[a, b)$ (nhận mút trái $a$, loại mút phải $b$).
- `pd.qcut()`: Chia theo các điểm phân vị mẫu (Quantiles), bảo đảm số lượng quan sát trong mỗi khoảng là xấp xỉ bằng nhau:

```python
do_tuoi = pd.Series([20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32])
cac_khoang = [18, 25, 35, 60, 100]

nhom_tuoi = pd.cut(do_tuoi, bins=cac_khoang, right=False)
dem_nhom = nhom_tuoi.value_counts()
print("Phân bố số lượng theo khoảng độ tuổi:")
print(dem_nhom)
assert dem_nhom.loc[pd.Interval(18, 25, closed="left")] == 4
```

<!-- worked-example bai-10-lam-sach-du-lieu-worked-6 -->

::: example Rời rạc hóa giá trị theo khoảng cố định với cut và theo phân vị với qcut

Trong các nghiên cứu nhân khẩu học, biến độ tuổi liên tục thường được phân thành các nhóm mốc cố định hoặc chia theo các phân vị mẫu. Ta kết hợp hàm pd.cut để chia theo ngưỡng giá trị và pd.qcut để chia theo phân vị.

```python
import pandas as pd

tuoi = pd.Series([15, 22, 35, 48, 62], name="tuoi")
nhom_cut = pd.cut(
    tuoi,
    bins=[0, 18, 40, 100],
    labels=["Nhom_1", "Nhom_2", "Nhom_3"],
    right=False
)
nhom_qcut = pd.qcut(
    tuoi,
    q=2,
    labels=["PhanVi_Thap", "PhanVi_Cao"]
)

df_tuoi = pd.DataFrame({
    "tuoi": tuoi,
    "nhom_cut": nhom_cut,
    "nhom_qcut": nhom_qcut
})
print(df_tuoi)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| tuoi | nhom&#95;cut | nhom&#95;qcut |
| --- | --- | --- |
| 15 | Nhom&#95;1 | PhanVi&#95;Thap |
| 22 | Nhom&#95;2 | PhanVi&#95;Thap |
| 35 | Nhom&#95;2 | PhanVi&#95;Thap |
| 48 | Nhom&#95;3 | PhanVi&#95;Cao |
| 62 | Nhom&#95;3 | PhanVi&#95;Cao |

</div>

Rời rạc hóa là quá trình chuyển đổi một biến số liên tục thành các nhóm định tính rời rạc. Hàm `pd.cut` chia miền giá trị dựa trên các điểm cắt tường minh do người phân tích chỉ định thông qua danh sách `bins=[0, 18, 40, 100]` cùng các nhãn trung tính `['Nhom_1', 'Nhom_2', 'Nhom_3']`.

Quy ước toán học về mút của khoảng đóng vai trò quyết định: Khi thiết lập `right=False`, các khoảng được định nghĩa thành `[a, b)`, tức là nửa mở đóng bên trái. Với quy ước này, người 18 tuổi thuộc về nhóm `[18, 40)` thay vì nhóm trước đó.

Hàm `pd.qcut` chia dữ liệu dựa trên các phân vị mẫu với tham số `q=2`: Tập dữ liệu được chia thành hai nhóm có số lượng phần tử xấp xỉ bằng nhau dựa trên giá trị trung vị của mẫu.

Nếu nhiều giá trị bằng nhau nằm tại biên phân vị, hai nhóm có thể có số phần tử khác nhau. Khi điểm cắt bị trùng, có thể chọn `duplicates="drop"` để giảm số khoảng. Nếu còn truyền `labels`, số nhãn cũng phải khớp số khoảng thực tế sau khi bỏ điểm cắt.

:::

<!-- /worked-example -->

### 2.5. Phát hiện và xử lý giá trị ngoại lai bằng Hàng rào Tukey (IQR Fences)

Giá trị ngoại lai (*Outlier*) là các điểm dữ liệu nằm cách biệt bất thường so với phần còn lại của phân phối. Phương pháp hàng rào Tukey dựa trên Khoảng tứ phân vị ($IQR$) là phương pháp phi tham số hữu hiệu vì không phụ thuộc vào giả định phân phối chuẩn:

$$
\begin{aligned}
IQR &= Q_3 - Q_1 \\
\text{Ngưỡng dưới: } lo &= Q_1 - 1{,}5 \times IQR \\
\text{Ngưỡng trên: } hi &= Q_3 + 1{,}5 \times IQR
\end{aligned}
$$

```python
gia_phong = pd.Series([100, 110, 120, 130, 140, 150, 160, 170, 180, 1200])

q1 = gia_phong.quantile(0.25)
q3 = gia_phong.quantile(0.75)
iqr = q3 - q1
lo = q1 - 1.5 * iqr
hi = q3 + 1.5 * iqr

ngoai_lai = (gia_phong < lo) | (gia_phong > hi)
print(f"Khoảng an toàn: [{lo}, {hi}]")
print("Các giá trị ngoại lai:", gia_phong[ngoai_lai].tolist())
assert gia_phong[ngoai_lai].tolist() == [1200]
```

**Nguyên tắc sư phạm cốt lõi**: Ngoại lai không đồng nghĩa với dữ liệu sai sót. Một căn biệt thự có giá 1.200 USD/đêm là một thực thể kinh doanh hoàn toàn có thật. Nhà phân tích chỉ gắn cờ `la_ngoai_lai` để tách nhánh phân tích riêng, tuyệt đối không được tự ý xóa bỏ các dòng ngoại lai hợp lệ khỏi tổng thể kinh tế.

<!-- worked-example bai-10-lam-sach-du-lieu-worked-7 -->

::: example Xác định biên ngoại lai theo khoảng tứ phân vị và nẹp giá trị bằng clip

Thiết bị đo lường có thể ghi nhận các giá trị tăng vọt bất thường như 50.0 trong khi dải giá trị thông thường dao động từ 10.0 đến 18.0. Ta áp dụng quy tắc Hàng rào Tukey để xác định biên trên và nẹp giá trị quan sát bằng phương thức clip.

```python
import pandas as pd

s_do = pd.Series([10.0, 12.0, 14.0, 15.0, 16.0, 18.0, 50.0])
q1 = s_do.quantile(0.25)
q3 = s_do.quantile(0.75)
iqr = q3 - q1
duoi = q1 - 1.5 * iqr
tren = q3 + 1.5 * iqr

s_nep = s_do.clip(lower=duoi, upper=tren)
df_kq = pd.DataFrame({"goc": s_do, "nep": s_nep})
print(df_kq)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| goc | nep |
| --- | --- |
| 10.0 | 10.0 |
| 12.0 | 12.0 |
| 14.0 | 14.0 |
| 15.0 | 15.0 |
| 16.0 | 16.0 |
| 18.0 | 18.0 |
| 50.0 | 23.0 |

</div>

Quy tắc Hàng rào Tukey dựa trên khoảng tứ phân vị (`IQR = Q3 - Q1`) là phương pháp xác định biên ngoại lai ít nhạy cảm với các giá trị cực trị hơn so với phương pháp dựa trên giá trị trung bình và độ lệch chuẩn. Tuy nhiên, quy tắc này không miễn nhiễm hoàn toàn với các phân phối lệch nặng hoặc các tập dữ liệu có nhiều điểm bất thường cùng chiều.

Các ngưỡng biên được thiết lập theo công thức: Biên dưới là `Q1 - 1.5 * IQR` và biên trên là `Q3 + 1.5 * IQR`. Trong chuỗi quan sát mẫu, phân vị Q1 bằng 13.0 và Q3 bằng 17.0, dẫn tới IQR bằng 4.0 và ngưỡng biên trên là 23.0.

Giá trị 50.0 vượt qua ngưỡng biên 23.0. Phương thức `s_do.clip(lower=duoi, upper=tren)` điều chỉnh giá trị này về mức trần 23.0 trong khi giữ nguyên các quan sát bình thường từ 10.0 đến 18.0.

Thao tác nẹp giá trị bằng `clip` là một lựa chọn mô hình hóa có chủ đích: Việc nẹp giá trị không chứng minh rằng quan sát 50.0 bắt nguồn từ lỗi đo lường thực tế, và thao tác này cũng không tự động bảo đảm cải thiện hiệu năng của mô hình phân tích sau đó.

:::

<!-- /worked-example -->

### 2.6. Hoán vị và lấy mẫu ngẫu nhiên

Phương thức `sample()` trên DataFrame cho phép lấy mẫu ngẫu nhiên không hoàn lại (`replace=False`) hoặc có hoàn lại (`replace=True`), theo số lượng cố định `n` hoặc theo tỷ lệ `frac`.

### 2.7. Tạo biến giả / biến chỉ báo (Dummy / Indicator Variables)

Trong các mô hình thống kê và học máy, các biến phân loại dạng chuỗi cần được chuyển đổi thành các cột nhị phân $0/1$. Hàm `pd.get_dummies()` tự động thực hiện phép biến đổi này:

```python
df_loai = pd.DataFrame({"loai": ["nha_rieng", "can_ho", "nha_rieng", "phong_tro"]})
df_dummies = pd.get_dummies(df_loai["loai"], prefix="la", dtype=int)
print(df_dummies)
assert df_dummies.shape == (4, 3)
```

---

<!-- worked-example bai-10-lam-sach-du-lieu-worked-8 -->

::: example Mã hóa một nóng cho biến định tính với get_dummies

Nhiều mô hình thống kê và thuật toán học máy yêu cầu dữ liệu đầu vào ở dạng ma trận số. Ta sử dụng hàm pd.get_dummies với tiền tố prefix và kiểu số nguyên dtype=int để chuyển đổi cột phân loại thành các cột chỉ báo nhị phân.

```python
import pandas as pd

df_hang = pd.DataFrame({
    "ma": ["P1", "P2", "P3"],
    "loai": ["Ao", "Quan", "Ao"]
})

dummies = pd.get_dummies(df_hang["loai"], prefix="loai", dtype=int)
df_out = pd.concat([df_hang[["ma"]], dummies], axis=1)
print(df_out)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| ma | loai&#95;Ao | loai&#95;Quan |
| --- | --- | --- |
| P1 | 1 | 0 |
| P2 | 0 | 1 |
| P3 | 1 | 0 |

</div>

Mã hóa biến giả (Dummy variable) hoặc mã hóa một nóng (One-Hot Encoding) chuyển đổi một cột định tính có k giá trị phân loại thành k cột nhị phân chứa các giá trị 0 và 1. Cột nhận giá trị 1 biểu thị quan sát thuộc về nhóm tương ứng.

Hàm `pd.get_dummies(df_hang['loai'], prefix='loai', dtype=int)` tạo ra hai cột mới là `loai_Ao` và `loai_Quan`. Tham số `prefix='loai'` gắn tiền tố rõ ràng vào tên cột, tránh xung đột tên khi mã hóa nhiều biến phân loại trong cùng một bảng.

Thiết lập tham số `dtype=int` bảo đảm các giá trị xuất ra là số nguyên 0 và 1 thay vì kiểu boolean, phù hợp trực tiếp với các phép tính ma trận trong mô hình tuyến tính.

Trong ví dụ, mỗi hàng thuộc đúng một loại nên chỉ một cột chỉ báo nhận 1. Cách mã hóa cần phù hợp với mô hình tiếp nhận. Một số công cụ hỗ trợ biến phân loại trực tiếp, nhưng không thể suy ra rằng mọi mô hình cây đều nhận chuỗi hoặc kiểu danh mục mà không cần chuyển đổi.

:::

<!-- /worked-example -->

## 3. Kiểu dữ liệu mở rộng (Extension Data Types)

Trong các phiên bản pandas ban đầu, sự hiện diện của một giá trị khuyết thiếu trong cột số nguyên `int64` buộc pandas phải ép kiểu ngầm toàn bộ cột sang số thực `float64`, vì kiểu số nguyên nguyên thủy của NumPy không có ký hiệu biểu diễn cho `NaN`.

Để khắc phục hạn chế này, pandas phát triển hệ thống kiểu dữ liệu mở rộng (*Extension Dtypes*) hỗ trợ khả năng chứa ô trống (*Nullable Types*):
- `Int64`, `Int32`, `UInt8`: Số nguyên cho phép chứa `pd.NA` mà không bị biến đổi sang số thực.
- `boolean`: Kiểu logic ba trạng thái (`True`, `False`, `pd.NA`).
- `string` hoặc `string[pyarrow]`: Kiểu chuỗi ký tự chuyên dụng, tối ưu hóa bộ nhớ và bảo vệ dữ liệu chuỗi khỏi việc vô tình bị coi là đối tượng Python chung chung (`object`).

```python
# Cột số nguyên có chứa giá trị thiếu nhưng vẫn bảo toàn kiểu nguyên:
s_nguyen = pd.Series([1, 2, None, 4], dtype="Int64")
print(s_nguyen)
assert s_nguyen.dtype == "Int64"
assert pd.isna(s_nguyen.iloc[2])
```

---

## 4. Xử lý dữ liệu chuỗi (String Manipulation)

Phần lớn dữ liệu nghiệp vụ và dữ liệu thu thập từ web đều xuất hiện dưới dạng chuỗi văn bản tự do.

### 4.1. Phương thức chuỗi có sẵn trong Python

Các phương thức tích hợp trên đối tượng `str` của Python cung cấp khả năng xử lý nhanh từng chuỗi đơn lẻ: Gồm các hàm `strip()`, `split()`, `join()`, `find()`, `replace()`, `startswith()`, `endswith()`.

### 4.2. Biểu thức chính quy (Regular Expressions)

Mô-đun `re` của Python cung cấp sức mạnh trích xuất và so khớp mẫu nâng cao:
- `re.compile`: Biên dịch mẫu biểu thức chính quy thành đối tượng mẫu để tái sử dụng nhiều lần.
- `search` và `match`: Tìm kiếm sự xuất hiện đầu tiên của mẫu trong chuỗi.
- `findall`: Tìm toàn bộ các đoạn khớp mẫu.
- `sub`: Thay thế các đoạn khớp mẫu bằng chuỗi mới.
- Ranh giới từ `\b`: Khóa khớp tại ranh giới từ để tránh khớp nhầm chuỗi con nằm bên trong từ khác.
- Cờ `re.I` (*Ignore Case*): Khớp không phân biệt chữ hoa và chữ thường.

### 4.3. Các hàm chuỗi vector hóa trong pandas (`.str`)

Thuộc tính `.str` cho phép thực thi các phép biến đổi chuỗi trên toàn bộ một Series mà tự động bỏ qua và bảo toàn các giá trị khuyết thiếu `NaN`:
- Chuẩn hóa: `.str.strip()`, `.str.lower()`, `.str.upper()`.
- Kiểm tra điều kiện: `.str.contains()`, `.str.startswith()`.
- Trích xuất cấu trúc: `.str.extract()`, `.str.findall()`.

Cần lưu ý rằng thuộc tính `.str` là tiện ích duyệt từng phần tử chuỗi Python ở tầng thông dịch. Với các bảng dữ liệu lớn hoặc biểu thức chính quy phức tạp, việc áp dụng liên tiếp nhiều phương thức `.str` có thể tiêu tốn thời gian hơn so với việc biên dịch trước mẫu regex bằng `re.compile()` và duyệt xử lý qua hàm `map()` hoặc list comprehension.

> [!CAUTION] Dấu đô la có ý nghĩa riêng trong regex
> Trong biểu thức chính quy, ký tự neo `\$` đại diện cho vị trí kết thúc chuỗi văn bản. Nếu gọi `s.str.replace(r"\$", "", regex=True)`, pandas sẽ thay thế vị trí cuối chuỗi bằng chuỗi rỗng và giữ nguyên ký tự đô la ở đầu chuỗi! Để thay thế ký tự tiền tệ thông thường một cách an toàn, luôn chỉ định tham số `regex=False`:
> `s.str.replace("$", "", regex=False).str.replace(",", "", regex=False).astype(float)`

---

<!-- worked-example bai-10-lam-sach-du-lieu-worked-9 -->

::: example Trích xuất nhóm thông tin bằng biểu thức chính quy với str.extract

Trong các mã đơn hàng có cấu trúc dạng DH_HN_102, phần chữ hai ký tự đại diện cho mã vùng và dãy số biểu thị số thứ tự giao dịch. Ta sử dụng phương thức str.extract kèm biểu thức chính quy có neo giới hạn để bóc tách các trường thông tin thành các cột riêng biệt.

```python
import pandas as pd

s_ma = pd.Series(["DH_HN_102", "DH_SG_405", "DH_DN_801", "sai_ma", "DH_HN_102\n"])
mau_regex = r"^DH_(?P<vung>[A-Z]{2})_(?P<so>\d+)\Z"

df_tach = s_ma.str.extract(mau_regex)
print(df_tach)
print("Kieu du lieu cot so:", df_tach["so"].dtype)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| vung | so |
| --- | --- |
| HN | 102 |
| SG | 405 |
| DN | 801 |
| (thiếu) | (thiếu) |
| (thiếu) | (thiếu) |

</div>

```text
Kieu du lieu cot so: str
```

Ô ghi “(thiếu)” biểu thị giá trị chưa được cung cấp hoặc chưa xác định.

Thuộc tính `.str` của pandas cung cấp các phương thức xử lý chuỗi theo vector trên đối tượng Series: Phương thức `str.extract` áp dụng một biểu thức chính quy chứa các nhóm bắt (capturing groups) để trích xuất các thành phần con thành một DataFrame.

Cú pháp đặt tên nhóm `(?P<vung>[A-Z]{2})` và `(?P<so>\d+)` chỉ định tên hiển thị cho các cột kết quả: Hai ký tự chữ hoa được đưa vào cột `vung`, và dãy chữ số được đưa vào cột `so`.

`^` neo đầu chuỗi, còn `\Z` yêu cầu kết thúc hẳn chuỗi. Nhờ vậy, mã có phần thừa hoặc dòng mới ở cuối không được chấp nhận. Dấu `$` có thể khớp ngay trước một ký tự xuống dòng cuối chuỗi, nên không thay hoàn toàn cho việc kiểm tra kết thúc nghiêm ngặt.

Các hàng không khớp cho ô thiếu trong cả hai cột. Cột `so` chứa chuỗi chữ số, chưa phải số nguyên. Nếu cần tính toán, có thể dùng `pd.to_numeric(df_tach["so"], errors="coerce")`. `.str` giúp diễn đạt phép xử lý theo cột, không phải cam kết tốc độ trên mọi dữ liệu.

:::

<!-- /worked-example -->

## 5. Kiểu dữ liệu phân loại (Categorical Data)

Trong các bảng dữ liệu lớn, nhiều cột văn bản chỉ lặp đi lặp lại một số ít các giá trị danh mục cố định (ví dụ tên giới tính, tên thành phố, hoặc mức độ ưu tiên). Việc lưu trữ các chuỗi văn bản này dưới dạng `object` tiêu tốn bộ nhớ RAM và làm chậm các phép toán gom nhóm so sánh.

### 5.1. Bản chất và phạm vi hiệu quả của `category`

Kiểu phân loại `category` trong pandas sử dụng kỹ thuật mã hóa từ điển (*Dictionary Encoding*):
- `categories`: Mảng duy nhất chứa các chuỗi danh mục phân biệt.
- `codes`: Mảng số nguyên nhỏ (`int8` hoặc `int16`) lưu trữ vị trí trỏ tới danh mục của từng hàng.

Khi số lượng danh mục duy nhất nhỏ hơn rất nhiều so với tổng số dòng (tính phân biệt thấp), pandas chỉ lưu trữ một mảng số nguyên nhỏ gọn thay vì lặp lại các chuỗi ký tự, giúp tiết kiệm đáng kể dung lượng bộ nhớ RAM:

```python
trai_cay = pd.Series(["táo", "cam", "táo", "táo"] * 2, dtype="category")
print("Các danh mục phân loại:", trai_cay.cat.categories.tolist())
print("Mã số nguyên đại diện:", trai_cay.cat.codes.tolist())
assert trai_cay.cat.codes.tolist() == [1, 0, 1, 1, 1, 0, 1, 1]
```

Tuy nhiên, kiểu `category` không phải lúc nào cũng mang lại lợi ích về bộ nhớ và tốc độ. Khi một cột có số lượng giá trị phân biệt lớn gần bằng số hàng (chẳng hạn cột mã bưu chính, số điện thoại hoặc văn bản tự do hầu như không lặp lại), việc ép sang `category` thậm chí còn làm tốn thêm bộ nhớ để lưu mảng từ điển `categories` và làm chậm tốc độ tính toán do chi phí quản lý bảng mã. Vì vậy, chỉ nên sử dụng `category` khi tỷ lệ giá trị duy nhất trên tổng số dòng đủ nhỏ.

### 5.2. Phân loại có thứ tự và các phương thức chuyên dụng

Tham số `ordered=True` cho phép thiết lập quan hệ thứ tự logic giữa các danh mục (ví dụ: Thứ tự `kém < trung bình < khá < giỏi`), mở đường cho các phép so sánh toán học và sắp xếp chính xác:

```python
danh_gia = pd.Categorical(
    ["khá", "giỏi", "kém", "trung bình"],
    categories=["kém", "trung bình", "khá", "giỏi"],
    ordered=True
)
print("Đánh giá lớn nhất:", danh_gia.max())
assert danh_gia.min() == "kém"
assert danh_gia.max() == "giỏi"
```

---

<!-- worked-example bai-10-lam-sach-du-lieu-worked-10 -->

::: example Thiết lập phân loại có thứ tự và biến đổi thang đo định tính

Các thang đo đánh giá chất lượng có thứ bậc nội tại nhưng khi lưu dưới dạng chuỗi thông thường, chúng sẽ bị sắp xếp theo thứ tự bảng chữ cái. Ta sử dụng pd.Categorical với tham số ordered=True để thiết lập thứ tự logic và trích xuất mã số định danh qua thuộc tính cat.codes.

```python
import pandas as pd

phan_loai = pd.Categorical(
    ["TrungBinh", "Cao", "Thap", "Cao"],
    categories=["Thap", "TrungBinh", "Cao"],
    ordered=True
)

s_hang = pd.Series(phan_loai)
df_out = pd.DataFrame({
    "nhan": s_hang.astype(str),
    "ma_so": s_hang.cat.codes
})
print(df_out)
```

Kết quả khi chạy đoạn mã trên:

<div class="data-worked-table">

| nhan | ma&#95;so |
| --- | --- |
| TrungBinh | 1 |
| Cao | 2 |
| Thap | 0 |
| Cao | 2 |

</div>

Kiểu dữ liệu chuỗi thông thường không mang theo khái niệm thứ bậc: Khi sắp xếp các chuỗi `'Cao'`, `'Thap'`, `'TrungBinh'`, hệ thống căn cứ vào bảng mã ký tự và xếp `'Cao'` trước `'Thap'`. Thao tác này làm lệch thứ tự đánh giá khi mức `'Thap'` là điểm khởi đầu của thang đo.

Lớp `pd.Categorical` giải quyết vấn đề này thông qua hai tham số: Tham số `categories=['Thap', 'TrungBinh', 'Cao']` xác định danh mục các giá trị hợp lệ theo thứ bậc tăng dần, và `ordered=True` xác nhận thang đo có thứ tự so sánh được.

Thuộc tính `cat.codes` cung cấp mã số nguyên đại diện cho từng mức phân loại: Mức `'Thap'` nhận mã 0, `'TrungBinh'` nhận mã 1, và `'Cao'` nhận mã 2. Việc mã hóa số nguyên này hỗ trợ các phép sắp xếp theo đúng logic thứ bậc của danh mục.

Bảng kết quả liên kết giữa nhãn văn bản và mã số kỹ thuật tương ứng, cho phép thực hiện các phép lọc so sánh như `s_hang >= 'TrungBinh'` theo đúng thứ tự thang đo đã định nghĩa. Giá trị thiếu được mã hóa bằng -1. Mã 0, 1, 2 chỉ biểu diễn thứ tự, không khẳng định khoảng cách giữa hai mức liên tiếp bằng nhau.

:::

<!-- /worked-example -->

## 6. Xác thực văn bản sang bảng và đo lường chất lượng

Trong kỷ nguyên xử lý dữ liệu phi cấu trúc, kỹ sư dữ liệu thường xuyên phải trích xuất các thực thể từ văn bản tự do thành các trường thuộc tính có cấu trúc trong bảng.

### 6.1. Ràng buộc cấu trúc và kiểm tra định dạng

Một quy trình chuyển đổi văn bản sang bảng đáng tin cậy bắt buộc phải có tầng kiểm soát schema nghiêm ngặt:
1. **Kiểm tra sự hiện diện của trường bắt buộc**: Không chấp nhận các đối tượng thiếu khóa định danh.
2. **Kiểm tra miền giá trị và kiểu dữ liệu**: Sử dụng biểu thức chính quy hoặc logic kiểm tra để đảm bảo dữ liệu số không bị biến tướng thành chuỗi rỗng.
3. **Phân loại lỗi**: Tách riêng các trường hợp trích xuất thất bại để phân tích nguyên nhân thay vì để lỗi làm sập toàn bộ đường ống.

### 6.2. Đo lường chất lượng trên tập kiểm thử đã gán nhãn

Để đánh giá một phương pháp trích xuất dữ liệu mà không cần phụ thuộc vào bất kỳ dịch vụ hay công cụ trả phí nào, chuẩn mực khoa học là xây dựng một tập kiểm chuẩn nhỏ (khoảng 50 đến 100 mẫu) đã được con người gán nhãn chính xác tuyệt đối (*Ground Truth*).

Chất lượng trích xuất được đo lường thông qua ba chỉ số toán học:
- **Độ chính xác (Accuracy)**: Tỷ lệ số quan sát được trích xuất hoàn toàn trùng khớp trên tổng số quan sát:
$$
\text{Accuracy} = \frac{TP + TN}{TP + TN + FP + FN}
$$
- **Độ chuẩn xác (Precision)**: Trong số những trường hợp hệ thống trích xuất là dương tính, tỷ lệ phần trăm thực sự chính xác là bao nhiêu:
$$
\text{Precision} = \frac{TP}{TP + FP}
$$
- **Độ thu hồi (Recall)**: Trong số tất cả các thực thể thực sự tồn tại trong văn bản, hệ thống đã trích xuất thành công bao nhiêu phần trăm:
$$
\text{Recall} = \frac{TP}{TP + FN}
$$

```python
# Giả lập kết quả trích xuất thực thể so với nhãn chuẩn:
nhan_thuc_te = [1, 1, 1, 0, 0, 0]
nhan_du_doan = [1, 1, 0, 1, 0, 0]

tp = sum(t == 1 and p == 1 for t, p in zip(nhan_thuc_te, nhan_du_doan))
fp = sum(t == 0 and p == 1 for t, p in zip(nhan_thuc_te, nhan_du_doan))
fn = sum(t == 1 and p == 0 for t, p in zip(nhan_thuc_te, nhan_du_doan))
tn = sum(t == 0 and p == 0 for t, p in zip(nhan_thuc_te, nhan_du_doan))

do_chinh_xac = (tp + tn) / len(nhan_thuc_te)
do_chuan_xac = tp / (tp + fp)
do_thu_hoi = tp / (tp + fn)

print(f"Accuracy: {do_chinh_xac:.2f}, Precision: {do_chuan_xac:.2f}, Recall: {do_thu_hoi:.2f}")
assert np.isclose(do_chinh_xac, 4/6)
assert np.isclose(do_chuan_xac, 2/3)
assert np.isclose(do_thu_hoi, 2/3)
```

---

## 8. Tổng kết

1. **Thận trọng với cơ chế khuyết thiếu**: Phân biệt rõ các tình huống thiếu ngẫu nhiên do kỹ thuật, thiếu có điều kiện hay thiếu gắn liền với giá trị tiềm ẩn. Tránh điền giá trị trung bình một cách máy móc làm sụt giảm phương sai và thu hẹp khoảng tin cậy.
2. **Phân định rõ ranh giới trùng lặp**: Xác lập đơn vị quan sát trước khi xóa các hàng trùng hoàn toàn. Đối với xung đột thuộc tính trên cùng một khóa chính, không dùng `drop_duplicates` để che đậy các mâu thuẫn nghiệp vụ mà cần gắn cờ cảnh báo hoặc lưu bản ghi sau cùng.
3. **Khai thác hàng rào Tukey IQR**: Nhận diện ngoại lai dựa trên khoảng tứ phân vị. Chỉ gắn cờ phân loại để phân tích chuyên sâu chứ không tự ý xóa bỏ các thực thể kinh tế hợp lệ.
4. **Làm chủ biểu thức chính quy và hàm chuỗi**: Tận dụng thuộc tính `.str` để biến đổi vector hóa, đồng thời luôn chỉ định `regex=False` khi thay thế các ký tự văn bản thông thường như dấu đô la `$`.
5. **Cân nhắc phạm vi của kiểu phân loại Categorical**: Tận dụng cơ chế mã hóa từ điển của kiểu `category` cho các cột văn bản có số lượng nhãn phân biệt nhỏ so với quy mô dòng để tối ưu hóa bộ nhớ.
6. **Kiểm soát chất lượng bằng thước đo toán học**: Đánh giá các quy trình trích xuất văn bản thành bảng bằng các chỉ số khách quan như Accuracy, Precision và Recall trên tập mẫu kiểm thử đã gán nhãn chuẩn mực.

---

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 7: Data Cleaning and Preparation](https://wesmckinney.com/book/data-cleaning).
- Tài liệu chính thức pandas: [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) & [Categorical data](https://pandas.pydata.org/docs/user_guide/categorical.html).
- John W. Tukey, *Exploratory Data Analysis*, Addison-Wesley, 1977.
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).
- [RegexOne](https://regexone.com/), các chủ đề luyện biểu thức chính quy. [Bộ đề và ca thử IAI](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/lab-07-regex.ipynb).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 7. Bài tập rèn luyện

<span id="iai-07-bai-1"></span>

::: exercise Bài tập 1: Giá trung vị theo loại chỗ ở
Một bảng dữ liệu lưu trữ loại chỗ ở và giá thuê (USD/đêm) gặp tình trạng ô trống và định dạng chuỗi không thống nhất như sau:

| Loại | Giá |
| :--- | :--- |
| " Entire home " | 300 |
| "entire HOME" | thiếu |
| "PRIVATE ROOM" | 40 |
| "Private room " | 60 |
| "private room" | 200 |

Hãy viết mã nguồn tính giá trung vị theo từng loại chỗ ở, trong đó các nhãn chỉ khác nhau về chữ hoa chữ thường hoặc khoảng trắng thừa ở hai đầu phải được gộp chung vào cùng một nhóm.
:::

::: solution Lời giải
Ta sử dụng phương thức chuỗi vector hóa `.str.strip().str.lower()` để chuẩn hóa cột loại chỗ ở về dạng chữ thường không có khoảng trắng thừa, sau đó gom nhóm và tính giá trị trung vị (`median()`):

```python
bang_cho_o = pd.DataFrame({
    "loai": [" Entire home ", "entire HOME", "PRIVATE ROOM", "Private room ", "private room"],
    "gia": [300.0, np.nan, 40.0, 60.0, 200.0]
})

loai_chuan = bang_cho_o["loai"].str.strip().str.lower()
gia_trung_vi = bang_cho_o.groupby(loai_chuan)["gia"].median()

print("Giá trung vị theo loại chỗ ở sau chuẩn hóa:")
print(gia_trung_vi)

assert gia_trung_vi["entire home"] == 300.0
assert gia_trung_vi["private room"] == 60.0
```

Nhóm `entire home` chỉ có một quan sát có giá là 300 (dòng thứ hai bị thiếu giá), do đó giá trung vị là 300. Nhóm `private room` có ba quan sát với các giá trị 40, 60 và 200. Giá trị trung vị của ba số này là 60.
:::

<span id="iai-07-bai-2"></span>

::: exercise Bài tập 2: Trích xuất diện tích phòng bằng biểu thức chính quy
Cho cột tên phòng mô tả tự do của các cơ sở lưu trú như sau:

| Tên phòng | Diện tích kỳ vọng ($m^2$) |
| :--- | :--- |
| Depto 45 m2 | 45 |
| Studio 30m² | 30 |
| 80 M2 luxury | 80 |
| Torre 2024 | thiếu |
| 30m2x | thiếu |

Hãy thiết kế một biểu thức chính quy duy nhất để trích xuất chính xác diện tích phòng thành giá trị số nguyên. Yêu cầu: Không trích xuất các năm như `2024` và không khớp nhầm các từ có chứa hậu tố bất thường như `30m2x`.
:::

::: solution Lời giải
Biểu thức chính quy cần thỏa mãn:
1. Bắt đầu bằng ranh giới từ `\b`.
2. Khớp nhóm các chữ số diện tích `(\d+)`.
3. Khớp khoảng trắng tùy chọn `\s*` đi kèm đơn vị `m2` hoặc `m²`: Mẫu `m(?:2|²)`.
4. Kết thúc bằng ranh giới từ `\b` để loại trừ trường hợp `30m2x`.
5. Bổ sung cờ `re.I` để nhận diện cả chữ hoa `M2`.

```python
import re

ten_phong = pd.Series(["Depto 45 m2", "Studio 30m²", "80 M2 luxury", "Torre 2024", "30m2x"])

# Thiết kế mẫu regex và trích xuất
mau_regex = r"\b(\d+)\s*m(?:2|²)\b"
dien_tich_chuoi = ten_phong.str.extract(mau_regex, flags=re.I, expand=False)
dien_tich_so = pd.to_numeric(dien_tich_chuoi)

print("Kết quả trích xuất diện tích:")
print(dien_tich_so)

assert dien_tich_so.iloc[0] == 45.0
assert dien_tich_so.iloc[1] == 30.0
assert dien_tich_so.iloc[2] == 80.0
assert pd.isna(dien_tich_so.iloc[3])
assert pd.isna(dien_tich_so.iloc[4])
```
:::

<span id="iai-07-bai-3"></span>

::: exercise Bài tập 3: Thống kê tần số tiện nghi độc lập
Một bảng dữ liệu lưu trữ danh sách các tiện nghi của từng chỗ ở dưới dạng danh sách chuỗi:

| Mã chỗ ở | Danh sách tiện nghi |
| :--- | :--- |
| P1 | `["Wifi", " wifi ", "Kitchen"]` |
| P2 | `["WIFI", "Kitchen"]` |
| P3 | `["Kitchen", "Parking", "Parking"]` |
| P4 | `[]` |

Hãy viết mã nguồn thống kê xem mỗi tiện nghi được bao nhiêu chỗ ở độc lập liệt kê. Yêu cầu: Gộp các tiện nghi chỉ khác nhau về chữ hoa chữ thường hoặc khoảng trắng thừa ở hai đầu, và mỗi tiện nghi xuất hiện nhiều lần trong cùng một chỗ ở chỉ được tính là một lần.
:::

::: solution Lời giải
Quy trình xử lý gồm ba bước:
1. Sử dụng phương thức `explode()` để bung từng phần tử danh sách thành các hàng riêng biệt và loại bỏ các hàng rỗng.
2. Chuẩn hóa chuỗi bằng `.str.strip().str.lower()`.
3. Sử dụng `drop_duplicates(subset=["cho_o", "tien_nghi"])` để đảm bảo mỗi tiện nghi chỉ được đếm một lần cho mỗi chỗ ở, sau đó dùng `value_counts()`:

```python
df_tien_nghi = pd.DataFrame({
    "cho_o": ["P1", "P2", "P3", "P4"],
    "danh_sach": [
        ["Wifi", " wifi ", "Kitchen"],
        ["WIFI", "Kitchen"],
        ["Kitchen", "Parking", "Parking"],
        []
    ]
})

# Bung danh sách thành các hàng
df_bung = df_tien_nghi.explode("danh_sach").dropna()
df_bung["danh_sach"] = df_bung["danh_sach"].str.strip().str.lower()

# Loại trùng lặp trong cùng một cơ sở lưu trú
df_duy_nhat = df_bung.drop_duplicates(subset=["cho_o", "danh_sach"])

# Đếm số lượng cơ sở lưu trú có từng tiện nghi
thong_ke_tn = df_duy_nhat["danh_sach"].value_counts()
print(thong_ke_tn)

assert thong_ke_tn["kitchen"] == 3
assert thong_ke_tn["wifi"] == 2
assert thong_ke_tn["parking"] == 1
```

Kết quả: Tiện nghi `kitchen` có mặt tại 3 chỗ ở (P1, P2, P3), tiện nghi `wifi` có mặt tại 2 chỗ ở (P1, P2), và tiện nghi `parking` có mặt tại 1 chỗ ở (P3).
:::

<span id="iai-10-bai-1"></span>

::: exercise Bài tập 4: So sánh giá giữa hai kỳ quan sát
Bảng dữ liệu theo dõi giá thuê phòng (USD/đêm) của cùng ba chỗ ở qua hai kỳ tháng 5 (T5) và tháng 6 (T6), trong đó chỗ ở P3 bị thiếu giá ở kỳ T6:

```python
bang_gia_ky = pd.DataFrame({
    "T5": [100.0, 200.0, 300.0],
    "T6": [110.0, 220.0, np.nan]
}, index=["P1", "P2", "P3"])
```

Nếu tính trung bình gộp từng cột: Kỳ T5 có giá trung bình là 200, trong khi kỳ T6 có giá trung bình là 165 (giảm 35 USD). Hãy phân tích cạm bẫy của phép so sánh này và viết mã nguồn so sánh lại giá trung bình một cách khoa học.
:::

::: solution Lời giải
Phép tính trung bình gộp bị sai lệch nghiêm trọng do thành phần mẫu thay đổi: Kỳ T5 tính trên cả 3 chỗ ở, bao gồm căn hộ cao cấp P3 (giá 300). Sang kỳ T6, căn hộ đắt nhất bị thiếu dữ liệu, khiến mẫu chỉ còn lại hai căn hộ bình dân P1 và P2. Con số giảm từ 200 xuống 165 phản ánh việc mất mẫu của căn hộ đắt tiền chứ không phản ánh xu hướng giá thị trường.

Để so sánh công bằng (*Paired Comparison*), ta chỉ so sánh trên những chỗ ở có đầy đủ dữ liệu ở cả hai kỳ bằng cách gọi `dropna()` trước khi tính trung bình:

```python
bang_gia_ky = pd.DataFrame({
    "T5": [100.0, 200.0, 300.0],
    "T6": [110.0, 220.0, np.nan]
}, index=["P1", "P2", "P3"])

# So sánh trên tập quan sát có dữ liệu ở cả hai kỳ
bang_cap_doi = bang_gia_ky.dropna()
tb_chuan = bang_cap_doi.mean()

print("Giá trung bình cặp đôi chuẩn mực:")
print(tb_chuan)

assert tb_chuan["T5"] == 150.0
assert tb_chuan["T6"] == 165.0
```

Khi xét trên cùng hai chỗ ở P1 và P2, giá trung bình thực tế tăng từ 150 lên 165 (tăng $10\%$). Cả hai căn hộ đều tăng giá ($100 \to 110$ và $200 \to 220$), trái ngược hoàn toàn với ảo tưởng sụt giá từ phép tính gộp.
:::

<span id="iai-10-bai-2"></span>

::: exercise Bài tập 5: Phản xạ của bộ kiểm tra ngoại lai trước đợt tăng giá đồng loạt
Một hệ thống kiểm toán dữ liệu tự động định kỳ tính ngưỡng bách phân vị $99$ ($P_{99}$) của giá phòng ở mỗi kỳ khảo sát, sau đó gắn cờ cảnh báo đối với mọi giá phòng vượt quá ngưỡng $P_{99}$ của kỳ đó.

Giả sử ở kỳ tiếp theo, danh sách các cơ sở lưu trú được giữ nguyên vẹn nhưng mọi mức giá trên toàn thị trường đều tăng gấp đôi một cách đồng loạt do lạm phát. Hỏi: Dựa vào tỷ lệ bản ghi bị gắn cờ cảnh báo, bộ kiểm tra này có phát hiện ra đợt tăng giá đột biến trên toàn thị trường hay không? Giải thích bản chất toán học.
:::

::: solution Lời giải
Bộ kiểm tra này **hoàn toàn không phát hiện được** đợt tăng giá đồng loạt.

Về bản chất toán học: Phép biến đổi nhân toàn bộ tập dữ liệu với một hằng số dương $c = 2$ ($X_{\text{mới}} = 2 \times X_{\text{cũ}}$) là một phép biến đổi đơn điệu tuyến tính.
Hệ quả là ngưỡng bách phân vị $P_{99}$ của kỳ mới cũng tăng đúng 2 lần:
$$
P_{99}(X_{\text{mới}}) = 2 \times P_{99}(X_{\text{cũ}})
$$

Gọi $a_i$ là giá cũ ở hàng i và q là P99 của dãy giá cũ. Điều kiện một quan sát bị gắn cờ ở kỳ mới tương đương với:
$$
2a_i > 2q \iff a_i > q.
$$

Mặt nạ boolean gắn cờ và tỷ lệ các bản ghi bị đánh dấu ở kỳ mới hoàn toàn trùng khớp với kỳ cũ. Ngưỡng phân vị tương đối chỉ phát hiện các điểm dị biệt so với nội bộ phân phối của chính kỳ đó chứ không có khả năng phát hiện sự dịch chuyển mức độ của toàn bộ hệ thống qua các mốc thời gian.
:::

<span id="iai-10-bai-3"></span>

::: exercise Bài tập 6: Giữ giá cập nhật sau cùng theo từng khóa
Một bảng dữ liệu ghi nhận lịch sử các lần cập nhật giá của các phòng như sau:

| id | ky | cap_nhat | gia |
| :--- | :--- | :--- | :--- |
| P1 | T6 | 2026-06-29 10:00 | 120 |
| P2 | T6 | 2026-06-29 08:00 | 90 |
| P1 | T5 | 2026-05-31 07:00 | 100 |
| P1 | T6 | 2026-06-29 09:00 | 110 |

Với mỗi cặp mã chỗ ở và kỳ quan sát `(id, ky)`, hãy viết mã nguồn chọn ra mức giá được cập nhật sau cùng, bất kể các dòng dữ liệu ban đầu nằm ở thứ tự nào trong bảng.
:::

::: solution Lời giải
Ta sắp xếp bảng dữ liệu theo thứ tự thời gian tăng dần của cột `cap_nhat`, sau đó áp dụng phương thức `drop_duplicates()` trên tập khóa `["id", "ky"]` và chỉ định tham số `keep="last"` để giữ lại dòng cuối cùng:

```python
lich_cap_nhat = pd.DataFrame({
    "id": ["P1", "P2", "P1", "P1"],
    "ky": ["T6", "T6", "T5", "T6"],
    "cap_nhat": pd.to_datetime(["2026-06-29 10:00", "2026-06-29 08:00", "2026-05-31 07:00", "2026-06-29 09:00"]),
    "gia": [120, 90, 100, 110]
})

# Sắp xếp theo mốc thời gian và giữ lại bản ghi sau cùng
gia_sau_cung = (
    lich_cap_nhat
    .sort_values("cap_nhat")
    .drop_duplicates(subset=["id", "ky"], keep="last")
)
print("Các mức giá cập nhật sau cùng:")
print(gia_sau_cung)

ket_qua_kiem_tra = set(zip(gia_sau_cung["id"], gia_sau_cung["ky"], gia_sau_cung["gia"]))
assert ket_qua_kiem_tra == {("P1", "T6", 120), ("P2", "T6", 90), ("P1", "T5", 100)}
```

Với cặp `(P1, T6)`, bản ghi lúc 10:00 với mức giá 120 được giữ lại, bản ghi lúc 09:00 với mức giá 110 bị loại bỏ chính xác.
:::

---








<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-07">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-07.md-->

</section>

<section class="data-lab-set" data-lab="lab-07-regex">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-07-regex.md-->

</section>

<section class="data-lab-set" data-lab="lab-10">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-10.md-->

</section>

<section class="data-lab-set" data-lab="lab-11">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-11.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 7: Data Cleaning and Preparation](https://wesmckinney.com/book/data-cleaning).
- Tài liệu chính thức pandas: [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html) & [Categorical data](https://pandas.pydata.org/docs/user_guide/categorical.html).
- John W. Tukey, *Exploratory Data Analysis*, Addison-Wesley, 1977.
- Hệ thống bài tập được chuyển thể từ học liệu mở của: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/) theo giấy phép [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).
- [RegexOne](https://regexone.com/), các chủ đề luyện biểu thức chính quy. [Bộ đề và ca thử IAI](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/2627-1/notebooks/lab-07-regex.ipynb).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
