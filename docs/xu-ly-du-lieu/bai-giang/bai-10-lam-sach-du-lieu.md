---
course: xu-ly-du-lieu
lecture: bai-10-lam-sach-du-lieu
section: lecture
title: "Làm sạch dữ liệu có cấu trúc"
prerequisites: ["gia-tri-thieu", "dictionary"]
lessonStatus: ready
description: "Làm sạch dữ liệu chuyên nghiệp: Toàn vẹn khóa ngoại, xung đột khóa tự nhiên, đối soát cột dẫn xuất, xử lý ngoại lai Tukey và đóng gói báo cáo QA chéo bảng."
---

Một ngạn ngữ kinh điển trong khoa học máy tính đúc kết: *"Rác vào thì rác ra"* (Garbage In, Garbage Out). Bất kể thuật toán học máy hay mô hình kinh tế lượng của bạn có tinh vi và phức tạp đến đâu, nếu nạp vào một nguồn dữ liệu bẩn chứa đầy lỗi nhập liệu, giá trị âm phi lý, dữ liệu mồ côi và các bản ghi mâu thuẫn, thì kết quả đầu ra chỉ là những con số ảo tưởng được bọc trong vỏ bọc toán học hào nhoáng.

Tuy nhiên, làm sạch dữ liệu không đồng nghĩa với việc xóa bỏ tùy tiện mọi dòng dữ liệu mà ta cảm thấy "bất thường". Người làm khoa học dữ liệu chuyên nghiệp tiếp cận việc làm sạch như một **quy trình kiểm toán có trách nhiệm**: Thiết lập bộ quy tắc kiểm định minh bạch, phân loại rạch ròi bản chất của từng loại lỗi, đối soát tính nhất quán chéo giữa các bảng liên kết, và bảo tồn đầy đủ dấu vết kiểm toán của các bản ghi bị loại trừ để bất kỳ ai cũng có thể thẩm định lại.

Bài học này xây dựng khung làm sạch dữ liệu chuẩn mực: Từ việc hiểu đúng bản chất toán học của dữ liệu khuyết thiếu, nhận diện ngoại lai bằng hàng rào Tukey, đến kỹ thuật kiểm tra toàn vẹn tham chiếu khóa ngoại, chứng minh sự vắng mặt của khóa tự nhiên, đối chiếu các cột dẫn xuất với dữ liệu sự kiện gốc, và đóng gói báo cáo chất lượng dữ liệu (`qa_report`).

---

## 1. Bản chất toán học của dữ liệu khuyết thiếu và rủi ro méo mó phân phối

Trong pandas, giá trị khuyết thiếu thường được biểu diễn bằng `np.nan` (đối với số thực), `pd.NA` (đối với kiểu dữ liệu có thể chứa giá trị rỗng của pandas), hoặc `pd.NaT` (đối với dữ liệu thời gian). 

Trước khi quyết định loại bỏ (`dropna()`) hay điền thế (`fillna()`), nhà phân tích cần nắm vững ba cơ chế phát sinh dữ liệu thiếu trong lý thuyết thống kê của Donald Rubin:

1. **Khuyết thiếu hoàn toàn ngẫu nhiên (Missing Completely at Random - MCAR)**: Xác suất một ô bị trống hoàn toàn độc lập với cả giá trị của chính nó lẫn mọi biến số khác trong bảng (ví dụ: Một tờ phiếu khảo sát vô tình bị gió thổi bay mất). Khi dữ liệu là MCAR, việc xóa dòng chỉ làm giảm kích thước mẫu chứ không làm lệch ước lượng trung bình.
2. **Khuyết thiếu ngẫu nhiên phụ thuộc biến quan sát (Missing at Random - MAR)**: Xác suất bị trống phụ thuộc vào một biến số khác đã được quan sát nhưng không phụ thuộc vào chính giá trị bị thiếu (ví dụ: Nam giới ít khi khai báo thu nhập hơn nữ giới, nhưng trong cùng nhóm nam giới thì mức thu nhập cao hay thấp không ảnh hưởng đến xác suất bỏ trống).
3. **Khuyết thiếu không ngẫu nhiên (Missing Not at Random - MNAR)**: Xác suất bị trống phụ thuộc trực tiếp vào chính giá trị tiềm ẩn của ô đó (ví dụ: Những người có thu nhập cực cao hoặc cực thấp thường cố tình từ chối khai báo mức lương). Đây là tình huống nguy hiểm nhất, vì mọi phép lọc bỏ đơn giản đều làm biến dạng nghiêm trọng phân phối thực tế của xã hội.

```python
import numpy as np
import pandas as pd

# Minh họa tác động toán học của việc điền khuyết
du_lieu = pd.Series([10.0, 12.0, 14.0, 16.0, 18.0, np.nan])

print("Trung bình gốc (bỏ qua NaN):", du_lieu.mean())               # 14.0
print("Phương sai gốc:", du_lieu.var())                              # 10.0

# 1. Điền bằng 0
dien_khong = du_lieu.fillna(0)
print("Trung bình khi điền 0:", dien_khong.mean())                   # 11.667 (kéo tụt tâm phân phối)

# 2. Điền bằng trung bình
dien_tb = du_lieu.fillna(du_lieu.mean())
print("Trung bình khi điền mean:", dien_tb.mean())                   # 14.0 (bảo toàn tâm)
print("Phương sai khi điền mean:", dien_tb.var())                    # 8.0 (phương sai bị sụt giảm nhân tạo!)
```

### Phân tích hệ quả toán học
Khi điền giá trị trung bình $\bar{x} = 14.0$ vào vị trí khuyết thiếu:
- Khoảng cách sai lệch của điểm mới này so với giá trị trung bình bằng đúng 0: $(14.0 - 14.0)^2 = 0$.
- Tổng bình phương độ lệch không đổi, nhưng kích thước mẫu $N$ lại tăng từ 5 lên 6.
- Kết quả là phương sai mẫu bị kéo tụt từ $10.0$ xuống $8.0$. Dữ liệu trông có vẻ "ổn định" và "ít phân tán" hơn thực tế, dẫn đến việc các khoảng tin cậy bị thu hẹp giả tạo và làm sai lệch kết quả kiểm định giả thuyết thống kê.

---

## 2. Phân định rạch ròi giữa bản sao hoàn toàn và xung đột khóa

Khi làm việc với các bảng dữ liệu nghiệp vụ, hai hiện tượng trùng lặp cần được phân biệt rõ ràng:

1. **Bản sao hoàn toàn (Exact Duplicate Rows)**: Toàn bộ các trường dữ liệu trên hai dòng đều giống hệt nhau từng ký tự. Đây là hệ quả của việc gửi trùng yêu cầu qua mạng hoặc nối trùng tệp dữ liệu. Thao tác gọi `df.drop_duplicates()` trên toàn bộ các cột là an toàn và cần thiết.
2. **Xung đột khóa (Key Conflict)**: Hai dòng có cùng mã định danh khóa chính `id`, nhưng các trường thuộc tính khác (như giá bán, số điện thoại, địa chỉ) lại mang giá trị khác nhau. 

```python
bang_giao_dich = pd.DataFrame({
    "ma_don": ["D01", "D01", "D02", "D02"],
    "khach_hang": ["An", "An", "Bình", "Bình"],
    "so_tien": [100, 100, 200, 250] # D02 có cùng mã nhưng số tiền mâu thuẫn!
})

# 1. Quét bản sao hoàn toàn trên mọi cột
trung_toan_bo = bang_giao_dich.duplicated(keep="first")
print("Số dòng trùng hoàn toàn:", int(trung_toan_bo.sum())) # 1 dòng (D01)

# 2. Phát hiện xung đột khóa
bang_loai_trung_thuc = bang_giao_dich.loc[~trung_toan_bo]
xung_dot = bang_loai_trung_thuc.duplicated(subset=["ma_don"], keep=False)
print("Các dòng xung đột khóa cần điều tra:")
print(bang_loai_trung_thuc[xung_dot])
```

Tuyệt đối không được nhắm mắt gọi `drop_duplicates(subset=["ma_don"])` để xóa bừa dòng thứ hai của đơn `D02`. Hành vi đó biến mất mát dữ liệu thành một lỗi ngầm không thể cứu vãn. Quy trình chuẩn mực là gắn cờ xung đột, tách các bản ghi này ra một bảng riêng để thẩm định nguồn gốc.

---

## 3. Nhận diện ngoại lai bằng Hàng rào Tukey (IQR Fences)

Giá trị ngoại lai (Outlier) là các điểm dữ liệu nằm cách biệt bất thường so với phân phối chung. Phương pháp hàng rào Tukey dựa trên **Khoảng tứ phân vị (Interquartile Range - IQR)** là công cụ phi tham số mạnh mẽ vì không phụ thuộc vào giả định phân phối chuẩn:

$$
IQR = Q_3 - Q_1
$$
$$
\text{Hàng rào dưới: } lo = Q_1 - 1.5 \times IQR
$$
$$
\text{Hàng rào trên: } hi = Q_3 + 1.5 \times IQR
$$

```python
gia_phong = pd.Series([500, 550, 600, 650, 700, 750, 800, 850, 900, 5000]) # 5000 là căn biệt thự siêu sang

q1, q3 = gia_phong.quantile([0.25, 0.75])
iqr = q3 - q1
lo = q1 - 1.5 * iqr
hi = q3 + 1.5 * iqr

ngoai_lai = (gia_phong < lo) | (gia_phong > hi)
print(f"Q1 = {q1}, Q3 = {q3}, IQR = {iqr}")
print(f"Dải an toàn: [{lo}, {hi}]")
print("Giá trị ngoại lai phát hiện:", gia_phong[ngoai_lai].tolist())
```

**Nguyên tắc sư phạm**: Ngoại lai không đồng nghĩa với dữ liệu sai. Căn biệt thự giá 5.000 là một thực thể kinh doanh có thật. Ta chỉ gắn cờ `la_ngoai_lai` để phục vụ các phân tích phân khúc riêng, tuyệt đối không được tự ý xóa bỏ các dòng ngoại lai hợp lệ khỏi tổng thể kinh tế.

---

## 4. Đảm bảo chất lượng dữ liệu chéo bảng (Cross-Table QA)

Khi làm việc với các hệ thống dữ liệu quan hệ gồm nhiều bảng (chẳng hạn bảng danh sách chỗ ở `listings` và bảng lịch sử đánh giá `reviews`), chất lượng dữ liệu không chỉ nằm ở từng cột đơn lẻ mà nằm ở **tính nhất quán chéo giữa các bảng**:

### 1. Tính toàn vẹn tham chiếu khóa ngoại (Foreign Key Referential Integrity)
Mọi bản ghi sự kiện ở bảng con (ví dụ cột `listing_id` trong `reviews`) bắt buộc phải tham chiếu đến một bản ghi thực sự tồn tại ở bảng cha (cột `id` trong `listings`). Các bản ghi không tìm thấy cha được gọi là **bản ghi mồ côi (Orphan Records)**, phản ánh sự đứt gãy trong quá trình đồng bộ hoặc xóa dữ liệu ở tầng cơ sở dữ liệu.

### 2. Sự ngộ nhận về khóa tự nhiên (Natural Key Pitfall)
Nhiều lập trình viên ngây thơ giả định rằng một cặp cột mô tả nghiệp vụ (như `listing_id` và `date`) có thể làm khóa duy nhất để phân biệt các dòng đánh giá. Tuy nhiên, trong thực tế, một căn hộ trong cùng một ngày có thể đón nhiều khách khác nhau trả phòng và viết đánh giá, hoặc nhiều thành viên trong cùng một đoàn khách cùng gửi nhận xét. Việc áp dụng `drop_duplicates(subset=["listing_id", "date"])` một cách máy móc sẽ xóa oan hàng nghìn nhận xét chân thực của khách hàng.

### 3. Đối soát cột dẫn xuất (Derived Columns Reconciliation)
Bảng cha thường lưu trữ sẵn các cột thống kê tổng hợp (như `number_of_reviews` hoặc `number_of_reviews_ltm` - số đánh giá trong 12 tháng gần nhất). Những cột này là các **cột dẫn xuất** do hệ thống backend tự tính toán sẵn. Người làm phân tích dữ liệu cần đối soát độc lập các cột này bằng cách tự tính lại từ bảng chi tiết để kiểm tra tính khớp nối và tìm ra các điểm lệch quy chuẩn định nghĩa thời gian.

---

## 5. Hệ thống bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 10) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 6. Tổng kết và Đọc thêm

| Trụ cột làm sạch | Công cụ pandas | Điểm nhấn kỹ thuật & Sư phạm |
| :--- | :--- | :--- |
| **Dữ liệu khuyết thiếu** | `isna()`, `fillna()`, `dropna()` | Nhận diện cơ chế thiếu (MCAR/MAR/MNAR); cẩn trọng với việc điền trung bình làm sụt giảm phương sai. |
| **Xung đột khóa** | `duplicated()`, `is_unique` | Phân biệt bản sao hoàn toàn với xung đột thuộc tính; không dùng `drop_duplicates` để xóa xung đột. |
| **Khoảng tứ phân vị (IQR)** | `quantile()`, Tukey Fences | Ngoại lai không đồng nghĩa với lỗi; chỉ gắn cờ cảnh báo để tách nhánh phân tích, không xóa dữ liệu thật. |
| **Kiểm định chéo bảng** | `isin()`, `reindex()`, `groupby()` | Kiểm tra toàn vẹn khóa ngoại; phân biệt khóa tự nhiên; đối soát định nghĩa các cột dẫn xuất. |
| **Đóng gói báo cáo** | `to_csv()`, `keep_default_na=False` | Lập biên bản kiểm toán minh bạch ghi nhận toàn bộ các vi phạm và quyết định xử lý. |

### Tài liệu tham khảo học thuật

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 7: Data Cleaning and Preparation](https://wesmckinney.com/book/data-cleaning).
- Tài liệu chính thức pandas: [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html).
- Donald B. Rubin, *Inference and Missing Data*, Biometrika, 1976.
- John W. Tukey, *Exploratory Data Analysis*, Addison-Wesley, 1977.
- Hệ thống bài giảng thực hành: [Khóa học Lập trình xử lý dữ liệu (UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/).
