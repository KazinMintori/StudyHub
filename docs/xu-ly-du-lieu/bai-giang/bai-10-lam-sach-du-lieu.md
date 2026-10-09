---
course: xu-ly-du-lieu
lecture: bai-10-lam-sach-du-lieu
section: lecture
title: "Làm sạch dữ liệu có cấu trúc"
prerequisites: ["gia-tri-thieu","dictionary","ky-vong"]
lessonStatus: ready
description: "Kiểm tra khóa, kiểu và miền giá trị; phân biệt thiếu với lỗi, xử lý ngoại lai và ghi nhận dữ liệu bị loại."
---

Một ngạn ngữ kinh điển trong ngành khoa học máy tính đúc kết: *"Rác vào thì rác ra"* (Garbage In, Garbage Out). Bất kể thuật toán học máy hay mô hình kinh tế lượng của bạn có tinh vi và phức tạp đến đâu, nếu nạp vào một nguồn dữ liệu bẩn chứa đầy lỗi nhập liệu, giá trị âm phi lý và các bản ghi mâu thuẫn, thì kết quả đầu ra chỉ là những con số ảo tưởng được bọc trong vỏ bọc toán học hào nhoáng.

Tuy nhiên, làm sạch dữ liệu không đồng nghĩa với việc xóa bỏ tùy tiện mọi dòng dữ liệu mà ta cảm thấy "bất thường". Người làm khoa học dữ liệu chuyên nghiệp tiếp cận việc làm sạch như một **quy trình kiểm toán có trách nhiệm**: thiết lập bộ quy tắc kiểm định minh bạch, phân loại rạch ròi bản chất của từng loại lỗi, và bảo tồn đầy đủ dấu vết của các bản ghi bị loại bỏ để bất kỳ ai cũng có thể thẩm định lại.

Bài học này xây dựng một khung làm sạch dữ liệu chuẩn mực: phân định trùng lặp và xung đột khóa, lập biên bản kiểm toán cho dữ liệu lỗi, hiểu đúng bản chất toán học của phép điền khuyết, nhận diện ngoại lai bằng hàng rào Tukey và kiểm chứng các bất biến sau làm sạch.

## 1. Thiết lập quy tắc kiểm định và phân biệt xung đột khóa

Trước khi viết bất kỳ dòng mã làm sạch nào, ta phải định hình rõ **Bộ quy tắc tính hợp lệ của dữ liệu** (Data Validation Rules) dựa trên hiểu biết nghiệp vụ:
- Mỗi mã định danh `id` phải đại diện cho duy nhất một mặt hàng.
- Giá bán phải là một số thực hữu hạn và không âm ($0 \le gia < \infty$).
- Đơn vị đo lường thống nhất là nghìn đồng.

```python
import pandas as pd
import numpy as np

raw = pd.DataFrame({
    "id": ["01", "01", "02", "03", "04"],
    "gia": ["20", "20", None, "-3", "oops"],
})
dup = raw.duplicated(keep="first")
unique_rows = raw.loc[~dup].copy()
assert unique_rows["id"].is_unique
print(len(raw), int(dup.sum()), len(unique_rows))  # 5 1 4
```

Hai tình huống trùng lặp cần phân biệt rạch ròi:

1. **Trùng lặp hoàn toàn (Exact Duplicates)**: Hai dòng đầu tiên có cùng `id="01"` và cùng `gia="20"`. Đây là hiện tượng một giao dịch bị ghi nhận lặp lại do lỗi đường truyền mạng hoặc bấm gửi hai lần. Phương thức `duplicated(keep="first")` quét trên toàn bộ các cột và an tâm loại bỏ bản sao thứ hai.
2. **Xung đột khóa (Key Conflict)**: Giả sử hai dòng có cùng `id="01"` nhưng dòng trên ghi giá 20 còn dòng dưới ghi giá 30. Đây không phải là bản sao, mà là **sự xung đột dữ liệu**. Tuyệt đối không được gọi `drop_duplicates(subset=["id"])` để nhắm mắt giữ lấy dòng đầu tiên. Ta phải điều tra nguyên nhân: đây là hai thời điểm cập nhật giá khác nhau, hay là do hai mặt hàng khác nhau bị gán nhầm mã?

Dòng lệnh `assert unique_rows["id"].is_unique` là bước xác nhận bắt buộc: sau khi đã loại bỏ các bản sao hoàn toàn, mỗi mã định danh còn lại phải là duy nhất.

## 2. Lập biên bản kiểm toán dữ liệu bị loại trừ

Khi một bản ghi không thể sử dụng để tính giá trung bình, lý do đằng sau sự thất bại đó mang ý nghĩa học thuật rất khác nhau:

```python
work = unique_rows.copy()
work["gia_so"] = pd.to_numeric(work["gia"], errors="coerce")
missing = work["gia"].isna()
bad_parse = work["gia"].notna() & work["gia_so"].isna()
bad_domain = work["gia_so"].notna() & (
    (work["gia_so"] < 0) | ~np.isfinite(work["gia_so"])
)
work["ly_do"] = np.select(
    [missing, bad_parse, bad_domain],
    ["thieu", "khong_doc_duoc", "ngoai_mien"], default="hop_le",
)
clean = work.loc[work["ly_do"] == "hop_le"].copy()
rejected = work.loc[work["ly_do"] != "hop_le"].copy()
print(clean["id"].tolist())       # ['01']
print(rejected["ly_do"].value_counts().to_dict())
```

Hàm `np.select()` phân loại chính xác ba bản chất lỗi trong bảng `rejected`:
- **`thieu`** (Mã `02`): Ô dữ liệu bị để trống ngay từ nguồn.
- **`khong_doc_duoc`** (Mã `04`): Ô chứa chuỗi ký tự rác `"oops"` không thể chuyển đổi thành số thực. Lỗi này phản ánh vấn đề ở khâu nhập liệu của con người hoặc định dạng tệp.
- **`ngoai_mien`** (Mã `03`): Ô chứa số `-3`, đọc thành công về mặt kỹ thuật nhưng vi phạm điều kiện logic của bài toán kinh doanh (giá bán không thể âm).

Báo cáo phân tích phải giải trình minh bạch: từ 5 dòng dữ liệu ban đầu, hệ thống loại bỏ 1 dòng trùng lặp, thu được 1 dòng hợp lệ duy nhất (`id="01"`), và đưa 3 dòng không đạt chuẩn vào sổ theo dõi đi kèm nguyên nhân chi tiết.

## 3. Bản chất của dữ liệu khuyết thiếu: Điền khuyết và rủi ro méo mó phân phối

pandas cung cấp hai công cụ thao tác với dữ liệu thiếu:
- `dropna()`: Loại bỏ toàn bộ dòng hoặc cột chứa ô trống.
- `fillna()`: Điền một giá trị thay thế vào ô trống.

Mỗi quyết định điền khuyết đều tác động sâu sắc lên cấu trúc toán học của tập dữ liệu:

```python
s = pd.Series([10.0, None, 30.0])
print(s.mean())                  # 20.0 trên hai giá đã biết
print(s.fillna(0).mean())        # 13.333333333333334
print(s.fillna(s.mean()).tolist())  # [10.0, 20.0, 30.0]
```

- **Điền số 0 (`fillna(0)`)**: Kéo tụt giá trị trung bình từ 20.0 xuống 13.33. Phép điền này chỉ hợp lệ nếu bản chất ô trống đại diện cho sự không phát sinh giao dịch.
- **Điền giá trị trung bình (`fillna(s.mean())`)**: Bảo toàn được tâm phân phối (trung bình vẫn là 20.0), nhưng làm **suy giảm nhân tạo độ phân tán** (phương sai và độ lệch chuẩn bị co cụm lại quanh điểm trung tâm), làm sai lệch các ước lượng kiểm định giả thuyết sau này.

Nguyên tắc vàng trong học máy: Nếu dữ liệu được phân chia thành tập huấn luyện (Train) và tập kiểm thử (Test), mọi giá trị thống kê dùng để điền khuyết (như trung bình hay trung vị) bắt buộc phải được tính toán **chỉ trên tập huấn luyện**, sau đó áp dụng giá trị đó sang tập kiểm thử. Việc tính trung bình trên toàn bộ bảng dữ liệu trước khi chia tập là hành vi gian lận dữ liệu ngầm (Data Leakage), khiến mô hình nhìn thấy trước phân phối của tập kiểm định.

## 4. Nhận diện ngoại lai bằng Hàng rào Tukey (IQR)

**Giá trị ngoại lai (Outlier)** là những quan sát nằm cách biệt bất thường so với phần còn lại của tập dữ liệu. Ngoại lai có thể là một lỗi đo lường (nhập thừa một số 0), nhưng cũng có thể là một sự kiện đặc biệt có thật (một khách hàng VIP chi tiêu đột biến).

Quy tắc kinh điển của nhà thống kê học John Tukey sử dụng **Khoảng tứ phân vị (Interquartile Range - IQR)**:

```python
values = pd.Series([10.0, 12.0, 14.0, 16.0, 100.0])
q1, q3 = values.quantile([0.25, 0.75], interpolation="linear")
iqr = q3 - q1
lo, hi = q1 - 1.5 * iqr, q3 + 1.5 * iqr
flag = (values < lo) | (values > hi)
print(q1, q3, iqr, lo, hi)       # 12.0 16.0 4.0 6.0 22.0
print(values[flag].tolist())     # [100.0]
```

Các bước tính toán hàng rào:
1. Xác định tứ phân vị thứ nhất $Q_1 = 12.0$ (mốc 25%) và tứ phân vị thứ ba $Q_3 = 16.0$ (mốc 75%).
2. Tính độ trải giữa: $IQR = Q_3 - Q_1 = 16.0 - 12.0 = 4.0$.
3. Thiết lập hai hàng rào an toàn:
   $$\text{Hàng rào dưới: } lo = Q_1 - 1.5 \times IQR = 12.0 - 1.5 \times 4.0 = 6.0$$
   $$\text{Hàng rào trên: } hi = Q_3 + 1.5 \times IQR = 16.0 + 1.5 \times 4.0 = 22.0$$

Giá trị $100.0$ vượt xa ngưỡng $22.0$ nên bị gắn cờ cảnh báo ngoại lai. Hãy ghi nhớ: gắn cờ ngoại lai chỉ nhằm mục đích **yêu cầu điều tra**, chứ không phải giấy phép để xóa bỏ ngay lập tức. Nếu con số 100 là một hóa đơn bán hàng có thật, việc xóa bỏ nó sẽ làm sai lệch tổng doanh thu thực tế của doanh nghiệp.

## 5. Rời rạc hóa và kiểm chứng tính toàn vẹn sau làm sạch

Sau khi làm sạch, ta có thể phân nhóm biến định lượng thành các khoảng danh mục phục vụ báo cáo:

```python
nhom_gia = pd.cut(values, bins=[0, 15, 50, float("inf")], right=False)
print(nhom_gia.value_counts(sort=False).tolist())  # [3, 1, 1]
assert len(clean) + len(rejected) == len(unique_rows)
assert clean["gia_so"].ge(0).all()
assert clean["id"].is_unique
```

Phương thức **`pd.cut()`** chia dữ liệu theo các mốc biên cố định. Tham số `right=False` quy định các khoảng nửa mở dạng $[a, b)$, tức là nhận biên dưới nhưng loại trừ biên trên. Ở ví dụ trên, giá trị 15 sẽ rơi vào khoảng thứ hai $[15, 50)$, còn các giá trị từ 50 trở lên rơi vào khoảng $[50, \infty)$.

Ba bài kiểm tra bất biến (Invariant Invariants) chốt chặn ở cuối quy trình:
1. **Bảo toàn số lượng dòng**: Tổng số dòng sạch cộng số dòng bị loại phải bằng đúng số dòng duy nhất ban đầu (`len(clean) + len(rejected) == len(unique_rows)`). Không có bất kỳ bản ghi nào bị "bốc hơi" một cách bí ẩn.
2. **Bảo đảm miền giá trị**: Toàn bộ giá trị trong cột số của bảng sạch phải không âm (`clean["gia_so"].ge(0).all()`).
3. **Bảo đảm tính toàn vẹn của khóa**: Cột `id` của bảng sạch phải là duy nhất tuyệt đối.

## 6. Bài tập tự luyện

::: exercise Phân biệt bản sao và xung đột dữ liệu
Một bảng khách hàng xuất hiện hai dòng cùng mang mã định danh `"KH01"`, nhưng một dòng ghi số điện thoại kết thúc bằng `888`, dòng kia kết thúc bằng `999`. 
1. Việc gọi lệnh `df.drop_duplicates(subset=["id"])` có giải quyết triệt để vấn đề không?
2. Hãy nêu cách tiếp cận chuẩn mực để xử lý tình huống này.
:::

::: solution
1. Lệnh `drop_duplicates(subset=["id"])` chỉ giải quyết vấn đề về mặt kỹ thuật bằng cách giữ lại dòng đầu tiên và xóa dòng thứ hai. Nó không giải quyết được vấn đề về mặt dữ liệu, vì hệ thống không biết số điện thoại nào mới là số chính xác của khách hàng.
2. Cách tiếp cận chuẩn mực:
   - Đưa hai bản ghi này vào bảng cảnh báo xung đột dữ liệu.
   - Kiểm tra các trường siêu dữ liệu khác (như thời điểm cập nhật cuối cùng `updated_at`). Nếu có cột thời gian, giữ lại bản ghi có mốc cập nhật gần nhất.
   - Nếu không có thông tin thời gian, cần chuyển thông tin này cho bộ phận quản trị cơ sở dữ liệu để đối chiếu với hồ sơ gốc.
:::

::: exercise Tác động của phép điền khuyết lên phương sai
Cho danh sách số liệu: `[10.0, 10.0, 20.0, 20.0, None]`. Nếu ta thay thế giá trị `None` bằng giá trị trung bình của các phần tử đã biết (bằng 15.0), phương sai của tập dữ liệu sau khi điền sẽ tăng lên, giảm đi hay giữ nguyên so với ban đầu? Giải thích lý do toán học.
:::

::: solution
Phương sai của tập dữ liệu sau khi điền sẽ **giảm đi**.

Lý do toán học: Phương sai đo lường mức độ phân tán của các điểm dữ liệu xung quanh giá trị trung bình. Bằng cách chèn thêm một phần tử có giá trị đúng bằng giá trị trung bình ($\bar{x} = 15.0$), khoảng cách lệch của phần tử mới này so với trung bình bằng 0 ($(15.0 - 15.0)^2 = 0$). Tổng bình phương độ lệch không đổi, nhưng mẫu số kích thước mẫu $N$ lại tăng từ 4 lên 5. Do đó, phương sai bị kéo tụt xuống, làm tập dữ liệu trông có vẻ "đồng đều" hơn so với bản chất thực tế.
:::

::: exercise Quy tắc biên nửa mở trong phân nhóm
Với mảng biên phân nhóm `bins = [0, 15, 50]` và tùy chọn `right=False`:
1. Điểm dữ liệu có giá trị 15 sẽ rơi vào khoảng nào?
2. Điểm dữ liệu có giá trị đúng bằng 50 có rơi vào khoảng nào không? Làm sao để không bỏ sót điểm này?
:::

::: solution
1. Với `right=False`, các khoảng được định nghĩa là $[0, 15)$ và $[15, 50)$. Do đó, giá trị 15 thuộc về khoảng thứ hai $[15, 50)$ (nhận biên trái).
2. Giá trị 50 **không rơi vào khoảng nào cả** và sẽ bị biến thành `NaN`, vì khoảng thứ hai loại trừ biên phải 50. Để không bỏ sót điểm này, ta phải mở rộng mốc biên trên thành vô cực `[0, 15, 50, float("inf")]` hoặc sử dụng tùy chọn mặc định `right=True` với biên mở phù hợp.
:::

## 7. Nguồn và đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 7: Data Cleaning and Preparation](https://wesmckinney.com/book/data-cleaning).
- Hướng dẫn chính thức: [pandas User Guide — Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html).
- Lý thuyết thống kê về dữ liệu khuyết thiếu: Little & Rubin, *Statistical Analysis with Missing Data*, Wiley.
- [Bài giảng tham khảo môn Xử lý dữ liệu (iaidev)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-10-lam-sach-du-lieu.html).
