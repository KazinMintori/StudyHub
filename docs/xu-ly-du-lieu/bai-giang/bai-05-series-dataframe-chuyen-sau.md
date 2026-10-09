---
course: xu-ly-du-lieu
lecture: bai-05-series-dataframe-chuyen-sau
section: lecture
title: "Series & DataFrame chuyên sâu"
prerequisites: ["chi-muc","gia-tri-thieu","ky-vong","phuong-sai"]
lessonStatus: ready
description: "Phân biệt nhãn và vị trí, căn chỉnh Series, tổng hợp nhóm, nối bảng và chuyển dạng dữ liệu."
---

Khi đã nắm vững các thao tác tạo lập bảng căn bản, người lập trình dữ liệu bắt đầu bước vào những bài toán phức tạp hơn: làm sao để tổng hợp số liệu theo từng phân khúc khách hàng, làm sao để hợp nhất nhiều bảng từ cơ sở dữ liệu quan hệ mà không làm nhân bản dữ liệu, và làm sao để chuyển đổi linh hoạt giữa bảng dạng rộng cho con người đọc và bảng dạng dài cho máy tính xử lý?

Những thao tác này tưởng chừng chỉ là việc gọi hàm, nhưng bên dưới nắp ca-pô là cả một hệ thống quy tắc toán học khắt khe về đại số quan hệ và căn chỉnh chỉ mục. Nếu không thấu suốt các quy tắc này, bạn sẽ rất dễ tạo ra những lỗi ngầm tai hại: doanh thu bị đội lên gấp đôi sau khi nối bảng, hoặc phép trừ giữa hai cột cho ra toàn giá trị rỗng chỉ vì thứ tự nhãn bị lệch nhau.

## 1. Bản chất của Index: Nhãn ngữ nghĩa khác với Vị trí bộ nhớ

Tính năng độc đáo nhất và cũng là nguồn cơn gây nhiều bối rối nhất của pandas chính là **Cơ chế căn chỉnh tự động theo nhãn** (Automatic Label Alignment).

Trong danh sách Python hay mảng NumPy, hai phần tử được cộng với nhau vì chúng đứng ở cùng một vị trí chỉ số $0, 1, 2$. Nhưng trong pandas, hai phần tử được ghép nối với nhau vì chúng **có cùng nhãn định danh**, bất kể chúng đang nằm ở dòng thứ mấy trong bảng.

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=[2, 0, 1])
print(s.loc[2], s.iloc[2])       # 10 30
a = pd.Series([10, 20], index=["A", "B"])
b = pd.Series([1, 2], index=["B", "C"])
print((a + b).to_dict())         # A: nan, B: 21.0, C: nan
print(a.add(b, fill_value=0).to_dict())  # A: 10.0, B: 21.0, C: 2.0
```

Hãy giải phẫu hai hiện tượng sâu sắc trong đoạn mã trên:

1. **Sự phân kỳ giữa `.loc` và `.iloc`**: 
   Khi Index của Series là các số nguyên bị xáo trộn `[2, 0, 1]`:
   - `s.loc[2]` đi tìm phần tử có **nhãn mang tên 2**, nằm ngay ở vị trí đầu tiên và trả về giá trị `10`.
   - `s.iloc[2]` đếm theo **vị trí vật lý** (0, 1, 2), lấy phần tử thứ ba và trả về giá trị `30`.
   Nếu bạn viết `s[2]`, các phiên bản pandas cũ sẽ cố gắng đoán xem bạn muốn tìm nhãn hay tìm vị trí. Để viết mã nguồn an toàn tuyệt đối trong sản xuất, luôn luôn sử dụng tường minh `.loc` khi muốn tìm theo nhãn và `.iloc` khi muốn tìm theo vị trí.
2. **Căn chỉnh nhãn khi làm toán**:
   Trong phép cộng `a + b`, pandas nhận thấy chỉ có nhãn `"B"` xuất hiện ở cả hai Series, nên nó lấy $20 + 1 = 21.0$. Nhãn `"A"` chỉ có ở `a`, nhãn `"C"` chỉ có ở `b`, do thiếu đối tác để ghép cặp nên kết quả ở cả hai nhãn này đều trở thành `NaN`.
   Phương thức `a.add(b, fill_value=0)` thể hiện một quy ước nghiệp vụ: nếu một bên bị khuyết thiếu nhãn thì tạm thời coi giá trị của bên đó là $0$ để tiếp tục phép cộng. Chỉ sử dụng quy ước này khi bạn chắc chắn rằng sự thiếu vắng dữ liệu đồng nghĩa với lượng giao dịch bằng 0.

Lưu ý rằng Index trong pandas không tự động bảo đảm tính duy nhất. Khi một cột cần đóng vai trò là khóa chính duy nhất của bảng, hãy chủ động kiểm tra bằng `df["id"].is_unique` hoặc thiết lập chỉ mục với cơ chế bảo vệ toàn vẹn: `df.set_index("id", verify_integrity=True)`.

## 2. Biến đổi cột an toàn và kỷ nguyên Copy-on-Write

Khi tạo mới hoặc cập nhật dữ liệu của một cột, pandas cung cấp nhiều công cụ khác nhau tùy thuộc vào mức độ phức tạp của bài toán.

```python
df = pd.DataFrame({
    "id": ["001", "002", "003"],
    "nhom": ["A", "A", "B"],
    "gia": [20, 40, 90],
})
df["gia_moi"] = df["gia"] * 1.1
df["ten_nhom"] = df["nhom"].map({"A": "Sach", "B": "Vo"})
df.loc[df["nhom"] == "A", "gia_moi"] = 25
print(df["gia_moi"].tolist())    # [25.0, 25.0, 99.00000000000001]
```

Ba bài học quan trọng về hiệu năng và an toàn dữ liệu:

1. **Ưu tiên phép toán vector hóa trực tiếp**: Phép tính `df["gia"] * 1.1` chạy hoàn toàn bằng mã C ở tầng dưới. Khi cần ánh xạ giá trị rời rạc, hãy dùng phương thức **`.map()`** truyền vào một cuốn từ điển. Hạn chế lạm dụng phương thức `.apply(..., axis=1)` vì nó sẽ duyệt từng dòng một thông qua vòng lặp Python thuần, làm tốc độ xử lý sụt giảm nghiêm trọng trên các tập dữ liệu lớn.
2. **Bản chất của số thực dấu phẩy động**: Giá trị $90 \times 1.1$ in ra là `99.00000000000001`. Đây không phải lỗi của pandas hay Python, mà là giới hạn tự nhiên của chuẩn biểu diễn số thực nhị phân IEEE 754 trên phần cứng máy tính (con số $1.1$ không thể biểu diễn hữu hạn dưới dạng nhị phân, tương tự như $1/3$ trong hệ thập phân). Khi làm việc với tiền tệ hay số liệu kế toán, ta cần làm tròn hiển thị hoặc sử dụng kiểu dữ liệu số nguyên cho đơn vị nhỏ nhất (ví dụ tính bằng xu thay vì đồng).
3. **Chấm dứt cạm bẫy Chained Assignment**: Trong các phiên bản pandas trước đây, người học rất hay viết: `df[df["nhom"] == "A"]["gia_moi"] = 25`. Cách viết chọn chuỗi này sẽ kích hoạt cảnh báo nguy hiểm `SettingWithCopyWarning`, vì pandas không thể xác định bạn đang gán giá trị vào bảng gốc hay vào một bản sao tạm thời. Từ pandas 3.0 với cơ chế **Copy-on-Write (CoW)**, việc gán giá trị có điều kiện bắt buộc phải viết trực tiếp qua `.loc`:
   ```python
   df.loc[df["nhom"] == "A", "gia_moi"] = 25
   ```

## 3. Triết lý Split-Apply-Combine: Phân định rạch ròi giữa `agg` và `transform`

Xử lý dữ liệu theo nhóm là trái tim của mọi phân tích kinh doanh. pandas hiện thực hóa mô hình kinh điển **Split - Apply - Combine** (Chia tách -> Áp dụng -> Kết hợp) của nhà khoa học thống kê Hadley Wickham thông qua phương thức `groupby()`.

Tuy nhiên, có một ranh giới then chốt giữa hai phương thức áp dụng mà nhiều người thường nhầm lẫn:

```python
bang_nhom = df.groupby("nhom").agg(
    so_dong=("id", "size"),
    so_gia=("gia", "count"),
    gia_tb=("gia", "mean"),
)
print(bang_nhom)
df["gia_tb_nhom"] = df.groupby("nhom")["gia"].transform("mean")
print(df["gia_tb_nhom"].tolist())  # [30.0, 30.0, 90.0]
```

Hãy nhìn vào sự khác biệt về hình dạng không gian của kết quả:

- **Phương thức `.agg()` (Aggregation - Thu gọn)**: Rút gọn số lượng dòng. Bảng gốc có 3 dòng thuộc 2 nhóm, bảng kết quả sau khi `agg` chỉ còn đúng 2 dòng đại diện cho 2 nhóm `"A"` và `"B"`. Cú pháp truyền tham số đặt tên như `so_dong=("id", "size")` cho phép ta vừa chỉ định cột tính toán, vừa chọn hàm thống kê và vừa đặt tên cột kết quả một cách mạch lạc. Lưu ý: `size` đếm toàn bộ số dòng kể cả ô trống, còn `count` chỉ đếm các ô có dữ liệu hợp lệ.
- **Phương thức `.transform()` (Biến đổi bảo toàn cấu trúc)**: Tính toán số liệu thống kê của từng nhóm, nhưng **phát ngược kết quả trở lại từng dòng ban đầu**, giữ nguyên vẹn kích thước và chỉ mục của bảng gốc!
  Ở nhóm `"A"`, hai mặt hàng có giá 20 và 40 nên giá trung bình nhóm là 30. Phương thức `transform` điền số 30 vào cả hai dòng thuộc nhóm `"A"`. Nhóm `"B"` nhận giá trị 90.

Nhờ việc bảo toàn số dòng, ta có thể dễ dàng so sánh từng cá thể với mức bình quân của phân khúc mà nó thuộc về:

```python
chenh_lech = df["gia"] - df["gia_tb_nhom"]
# Kết quả: [-10.0, 10.0, 0.0] -> Mặt hàng 1 rẻ hơn trung bình nhóm 10 nghìn, mặt hàng 2 đắt hơn 10 nghìn
```

Nếu không dùng `transform`, bạn sẽ phải tự viết một phép tính nhóm bằng `agg`, sau đó thực hiện lệnh ghép bảng phức tạp để nối ngược số liệu về bảng cũ.

## 4. Đại số quan hệ và cạm bẫy bùng nổ tổ hợp Cartesian khi ghép bảng

Khi làm việc với các hệ thống dữ liệu doanh nghiệp, thông tin thường bị phân mảnh ở nhiều bảng khác nhau. Để có một bức tranh toàn cảnh, ta sử dụng hàm **`pd.merge()`** để thực hiện các phép nối quan hệ (JOIN).

```python
danh_muc = pd.DataFrame({"nhom": ["A", "B"], "mo_ta": ["Sach", "Vo"]})
ket_qua = df.merge(
    danh_muc, on="nhom", how="left", validate="many_to_one", indicator=True
)
print(len(df), len(ket_qua))     # 3 3
print(ket_qua["_merge"].value_counts().to_dict())
```

Bốn kiểu nối dữ liệu kinh điển:
- **`how="left"`**: Giữ lại toàn bộ các dòng của bảng bên trái. Nếu bảng bên phải không có khóa khớp, các cột mới sẽ nhận giá trị `NaN`.
- **`how="inner"`**: Chỉ giữ lại các dòng mà khóa xuất hiện ở cả hai bảng.
- **`how="outer"`**: Giữ lại toàn bộ khóa của cả hai bên (hợp của hai tập hợp).
- **`how="right"`**: Giữ lại toàn bộ các dòng của bảng bên phải.

Một cạm bẫy nguy hiểm bậc nhất trong thực tế là **Hiện tượng nhân bản dòng ngoài ý muốn (Cartesian Explosion)**. Giả sử bảng danh mục hàng hóa bên phải bị lỗi hệ thống và vô tình chứa 2 dòng trùng lặp cho mã nhóm `"A"`. Khi bạn thực hiện phép nối, 2 dòng nhóm `"A"` của bảng bên trái khi gặp 2 dòng nhóm `"A"` của bảng bên phải sẽ tạo ra $2 \times 2 = 4$ dòng kết quả! Bảng dữ liệu bán hàng của bạn bỗng dưng bị nhân đôi doanh thu một cách bí ẩn.

Để bảo vệ hệ thống trước thảm họa này, các chuyên gia luôn bổ sung tham số **`validate="many_to_one"`** khi nối với bảng danh mục. Tham số này ra lệnh cho pandas kiểm tra nghiêm ngặt: khóa ở bảng bên phải bắt buộc phải là duy nhất. Nếu bảng bên phải có dòng trùng khóa, chương trình sẽ lập tức ném ra ngoại lệ `pd.errors.MergeError` và dừng lại để ta xử lý, thay vì âm thầm nhân bản dữ liệu.

Tham số **`indicator=True`** sinh thêm một cột đặc biệt mang tên `_merge`, ghi nhận rõ dòng dữ liệu này đến từ cả hai bảng (`both`), chỉ đến từ bên trái (`left_only`) hay chỉ đến từ bên phải (`right_only`). Đây là công cụ đắc lực để kiểm toán xem có bao nhiêu khách hàng chưa từng phát sinh đơn hàng nào.

## 5. Tái cấu trúc không gian bảng: Bảng rộng (Wide) và Bảng dài (Long)

Dữ liệu thường tồn tại dưới hai hình thái cấu trúc:
- **Dạng rộng (Wide format)**: Mỗi biến hoặc mỗi thời điểm chiếm một cột riêng biệt. Dạng này rất thân thiện với mắt người đọc báo cáo trên bảng tính Excel.
- **Dạng dài (Long / Tidy format)**: Mỗi hàng là một quan sát đơn lẻ, các biến được gom chung vào một cột định danh và một cột giá trị. Dạng này là chuẩn mực bắt buộc cho máy tính xử lý, vẽ biểu đồ nâng cao và đưa vào thuật toán phân tích.

```python
rong = pd.DataFrame({"quay": ["Q1", "Q2"], "sach": [2, 4], "vo": [3, 5]})
dai = rong.melt(id_vars="quay", var_name="mat_hang", value_name="so_luong")
print(dai)
lai = dai.pivot(index="quay", columns="mat_hang", values="so_luong")
assert lai.loc["Q1", "sach"] == 2
```

Hai thao tác chuyển đổi qua lại:
- **`df.melt(...)`**: "Làm tan chảy" bảng rộng thành bảng dài. Tham số `id_vars` chỉ định các cột định danh cần giữ nguyên vị trí, còn toàn bộ các cột còn lại được duỗi thẳng thành các cặp thuộc tính - giá trị.
- **`df.pivot(...)`**: "Cuộn" bảng dài trở lại thành bảng rộng. Phương thức `pivot()` đòi hỏi mỗi cặp chỉ số hàng và cột phải xác định duy nhất một giá trị. Nếu dữ liệu có sự trùng lặp (ví dụ quầy Q1 bán sách nhiều lần trong ngày), ta phải sử dụng hàm **`df.pivot_table()`** đi kèm một hàm tổng hợp như `aggfunc="sum"`.

## 6. Bài tập tự luyện

::: exercise Thẩm định cơ chế căn chỉnh nhãn
Cho hai Series:
```python
a = pd.Series([10, 20], index=["A", "B"])
b = pd.Series([1, 2], index=["B", "C"])
```
Hãy giải thích vì sao phép tính `(a + b)["B"]` cho kết quả là `21.0` thay vì `12.0` (tổng của hai phần tử đầu tiên).
:::

::: solution
Vì pandas hoạt động theo nguyên tắc căn chỉnh tự động theo nhãn (label alignment), hoàn toàn không phụ thuộc vào vị trí vật lý của phần tử trong mảng.

Khi thực hiện phép cộng `a + b`, pandas tìm phần tử có nhãn `"B"` trong `a` (giá trị là 20) và phần tử có nhãn `"B"` trong `b` (giá trị là 1) rồi cộng lại: $20 + 1 = 21.0$. Phép tính này không lấy phần tử đầu tiên của `a` (giá trị 10) cộng với phần tử đầu tiên của `b` (giá trị 1).
:::

::: exercise Kiểm soát sự bùng nổ dòng khi ghép bảng
Bảng `left` có 3 dòng đều mang khóa `"A"`. Bảng `right` có 2 dòng đều mang khóa `"A"`. 
1. Sau khi thực hiện `left.merge(right, on="k")`, bảng kết quả có bao nhiêu dòng?
2. Nếu bảng `right` đáng lẽ là bảng danh mục thông tin định danh của nhóm, ta cần truyền tham số gì vào `merge()` để phát hiện lỗi trùng khóa này?
:::

::: solution
1. Số dòng kết quả là $3 \times 2 = 6$ dòng. Mỗi dòng mang khóa `"A"` bên trái sẽ kết hợp với cả hai dòng mang khóa `"A"` bên phải theo quy tắc tích Descartes (Cartesian product).
2. Để ngăn chặn việc nhân bản dòng ngoài ý muốn, ta truyền tham số `validate="many_to_one"`. Khi phát hiện bảng bên phải có nhiều hơn một dòng cho cùng một khóa `"A"`, pandas sẽ lập tức ném ra ngoại lệ `MergeError` để cảnh báo lập trình viên kiểm tra lại tính duy nhất của dữ liệu nguồn.
:::

::: exercise Phân biệt trường hợp sử dụng agg và transform
Một kỹ sư muốn tạo thêm một cột mới trong bảng dữ liệu bán hàng để lưu trữ chênh lệch giữa giá bán của từng sản phẩm so với giá bán trung bình của phân khúc tương ứng. Hãy cho biết kỹ sư đó nên dùng `groupby().agg()` hay `groupby().transform()`, và viết câu lệnh thực hiện.
:::

::: solution
Kỹ sư đó bắt buộc phải sử dụng **`groupby().transform()`**.

Lý do: Phép tính so sánh cá thể đòi hỏi giữ nguyên toàn bộ số dòng của bảng ban đầu. Phương thức `agg()` sẽ thu gọn bảng thành số dòng bằng số nhóm, khiến ta không thể trừ trực tiếp với cột giá gốc.

Câu lệnh chuẩn xác là:
```python
df["chenh_lech"] = df["gia"] - df.groupby("nhom")["gia"].transform("mean")
```
:::

::: exercise Tổng hợp đa chỉ số với Named Aggregation và kiểm toán quan hệ bảng
Cho hai bảng dữ liệu giao dịch thương mại điện tử:
```python
import pandas as pd

don_hang = pd.DataFrame({
    "ma_don": ["DH1", "DH2", "DH3", "DH4", "DH5"],
    "ma_khach": ["K1", "K2", "K1", "K3", "K1"],
    "khu_vuc": ["MienBac", "MienNam", "MienBac", "MienTrung", "MienBac"],
    "thanh_toan": ["COD", "The", "The", "COD", "The"],
    "gia_tri": [150.0, 320.0, 210.0, 90.0, 450.0]
})

khach_hang = pd.DataFrame({
    "ma_khach": ["K1", "K2", "K3", "K4"],
    "ten_khach": ["An", "Bình", "Cường", "Dũng"]
})
```
Yêu cầu:
1. Tính đồng thời 3 chỉ số theo từng `khu_vuc`: tổng giá trị (`tong_tien`), số đơn hàng (`so_don`), và giá trị đơn trung bình (`gia_trung_binh`). Kết quả trả về phải có tên cột phẳng, không mang cấu trúc phân cấp đa tầng (*MultiIndex*).
2. Tạo bảng chéo tổng hợp tổng doanh thu theo `khu_vuc` (hàng) và phương thức `thanh_toan` (cột). Những ô không phát sinh giao dịch phải được điền bằng `0.0`.
3. Ghép hai bảng để tìm ra khách hàng nào trong hệ thống chưa từng phát sinh bất kỳ đơn hàng nào.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Tính toán phân mảnh và Merge thông thường)
Người mới thường gọi `.agg(['sum', 'count', 'mean'])` rồi tự đổi tên cột, sau đó dùng `merge` để kiểm tra thủ công:

```python
# 1. Aggregation cơ bản sinh ra MultiIndex ở cột
nhom_c1 = don_hang.groupby("khu_vuc")["gia_tri"].agg(["sum", "count", "mean"])
# Phải gán lại tên cột thủ công
nhom_c1.columns = ["tong_tien", "so_don", "gia_trung_binh"]

# 2. Pivot table cơ bản
pivot_c1 = don_hang.pivot_table(index="khu_vuc", columns="thanh_toan", values="gia_tri", aggfunc="sum").fillna(0)

# 3. Tìm khách chưa mua: Left join rồi lọc dòng có ma_don bị NaN
hop_nhat_c1 = pd.merge(khach_hang, don_hang, on="ma_khach", how="left")
khach_chua_mua_c1 = hop_nhat_c1.loc[hop_nhat_c1["ma_don"].isna(), "ten_khach"].tolist()
print("Khách chưa mua hàng (cơ bản):", khach_chua_mua_c1)
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Named Aggregation và Merge Indicator chuyên nghiệp)
Một cách người ta hay dùng trong các pipeline dữ liệu quy chuẩn là dùng cú pháp Named Aggregation chỉ định rõ tên cột ngay từ đầu, kết hợp tham số `indicator=True`:

```python
# 1. Named Aggregation: sạch sẽ, một bước, không tạo MultiIndex
bao_cao_khu_vuc = don_hang.groupby("khu_vuc").agg(
    tong_tien=("gia_tri", "sum"),
    so_don=("gia_tri", "count"),
    gia_trung_binh=("gia_tri", "mean")
).reset_index()

# 2. Pivot Table tối ưu với tham số fill_value trực tiếp
bang_cheo = don_hang.pivot_table(
    index="khu_vuc",
    columns="thanh_toan",
    values="gia_tri",
    aggfunc="sum",
    fill_value=0.0
)

# 3. Kiểm toán ghép nối với indicator=True
kiem_toan_khach = pd.merge(
    khach_hang,
    don_hang,
    on="ma_khach",
    how="left",
    indicator=True
)
khach_mo_coi = kiem_toan_khach.loc[kiem_toan_khach["_merge"] == "left_only", ["ma_khach", "ten_khach"]]

print("Báo cáo khu vực:\n", bao_cao_khu_vuc)
print("\nBảng chéo doanh thu:\n", bang_cheo)
print("\nKhách hàng mồ côi (chưa có đơn hàng):\n", khach_mo_coi)
```

#### Phân tích bản chất & Bình luận sư phạm
- **Ưu thế của Named Aggregation**: Cho phép áp dụng các hàm khác nhau lên cùng một cột hoặc nhiều cột khác nhau và định danh tên cột kết quả ngay tại thời điểm tính toán (ví dụ: `tong_tien=('gia_tri', 'sum')`). Nhờ đó, bảng kết quả luôn có cấu trúc cột đơn phẳng (*Flat Columns*), sẵn sàng xuất ra định dạng CSV/Parquet mà không gặp lỗi phân cấp chỉ mục.
- **Giá trị của `indicator=True`**: Cột `_merge` nhận 3 giá trị chuẩn tắc: `'left_only'`, `'right_only'`, và `'both'`. Trong bài toán đối soát tài chính, việc lọc `_merge == 'left_only'` là chuẩn mực vàng để phát hiện tức thì các tài khoản rác, khách hàng thụ động hoặc bản ghi mồ côi mà không sợ bị nhầm lẫn với các dòng dữ liệu bị thiếu do bản thân cột nghiệp vụ mang giá trị `NaN`.
:::

## 7. Nguồn và đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 5, mục 5.2: Essential Functionality](https://wesmckinney.com/book/pandas-basics), [Chương 8: Data Wrangling: Join, Combine, and Reshape](https://wesmckinney.com/book/data-wrangling), và [Chương 10: Data Aggregation and Group Operations](https://wesmckinney.com/book/data-aggregation).
- Hướng dẫn chính thức: [pandas User Guide — Merge, join, concatenate and compare](https://pandas.pydata.org/docs/user_guide/merging.html).
- [Bài giảng tham khảo môn Xử lý dữ liệu (iaidev)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-05-series-dataframe-chuyen-sau.html).
