---
course: xu-ly-du-lieu
lecture: bai-10-lam-sach-du-lieu
section: lecture
title: "Làm sạch dữ liệu có cấu trúc"
prerequisites: ["gia-tri-thieu","dictionary","ky-vong"]
lessonStatus: ready
description: "Làm sạch dữ liệu chuyên nghiệp: toàn vẹn khóa ngoại, xung đột khóa tự nhiên, đối soát cột dẫn xuất, xử lý ngoại lai Tukey và đóng gói báo cáo QA chéo bảng."
---

Một ngạn ngữ kinh điển trong khoa học máy tính đúc kết: *"Rác vào thì rác ra"* (Garbage In, Garbage Out). Bất kể thuật toán học máy hay mô hình kinh tế lượng của bạn có tinh vi và phức tạp đến đâu, nếu nạp vào một nguồn dữ liệu bẩn chứa đầy lỗi nhập liệu, giá trị âm phi lý, dữ liệu mồ côi và các bản ghi mâu thuẫn, thì kết quả đầu ra chỉ là những con số ảo tưởng được bọc trong vỏ bọc toán học hào nhoáng.

Tuy nhiên, làm sạch dữ liệu không đồng nghĩa với việc xóa bỏ tùy tiện mọi dòng dữ liệu mà ta cảm thấy "bất thường". Người làm khoa học dữ liệu chuyên nghiệp tiếp cận việc làm sạch như một **quy trình kiểm toán có trách nhiệm**: thiết lập bộ quy tắc kiểm định minh bạch, phân loại rạch ròi bản chất của từng loại lỗi, đối soát tính nhất quán chéo giữa các bảng liên kết, và bảo tồn đầy đủ dấu vết kiểm toán của các bản ghi bị loại trừ để bất kỳ ai cũng có thể thẩm định lại.

Bài học này xây dựng khung làm sạch dữ liệu chuẩn mực: từ việc hiểu đúng bản chất toán học của dữ liệu khuyết thiếu, nhận diện ngoại lai bằng hàng rào Tukey, đến kỹ thuật kiểm tra toàn vẹn tham chiếu khóa ngoại, chứng minh sự vắng mặt của khóa tự nhiên, đối chiếu các cột dẫn xuất với dữ liệu sự kiện gốc, và đóng gói báo cáo chất lượng dữ liệu (`qa_report`).

---

## 1. Bản chất toán học của dữ liệu khuyết thiếu và rủi ro méo mó phân phối

Trong pandas, giá trị khuyết thiếu thường được biểu diễn bằng `np.nan` (đối với số thực), `pd.NA` (đối với kiểu dữ liệu có thể chứa giá trị rỗng của pandas), hoặc `pd.NaT` (đối với dữ liệu thời gian). 

Trước khi quyết định loại bỏ (`dropna()`) hay điền thế (`fillna()`), nhà phân tích cần nắm vững ba cơ chế phát sinh dữ liệu thiếu trong lý thuyết thống kê của Donald Rubin:

1. **Khuyết thiếu hoàn toàn ngẫu nhiên (Missing Completely at Random - MCAR)**: Xác suất một ô bị trống hoàn toàn độc lập với cả giá trị của chính nó lẫn mọi biến số khác trong bảng (ví dụ: một tờ phiếu khảo sát vô tình bị gió thổi bay mất). Khi dữ liệu là MCAR, việc xóa dòng chỉ làm giảm kích thước mẫu chứ không làm lệch ước lượng trung bình.
2. **Khuyết thiếu ngẫu nhiên phụ thuộc biến quan sát (Missing at Random - MAR)**: Xác suất bị trống phụ thuộc vào một biến số khác đã được quan sát nhưng không phụ thuộc vào chính giá trị bị thiếu (ví dụ: nam giới ít khi khai báo thu nhập hơn nữ giới, nhưng trong cùng nhóm nam giới thì mức thu nhập cao hay thấp không ảnh hưởng đến xác suất bỏ trống).
3. **Khuyết thiếu không ngẫu nhiên (Missing Not at Random - MNAR)**: Xác suất bị trống phụ thuộc trực tiếp vào chính giá trị tiềm ẩn của ô đó (ví dụ: những người có thu nhập cực cao hoặc cực thấp thường cố tình từ chối khai báo mức lương). Đây là tình huống nguy hiểm nhất, vì mọi phép lọc bỏ đơn giản đều làm biến dạng nghiêm trọng phân phối thực tế của xã hội.

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

## 5. Hệ thống bài tập thực hành chuyên sâu (Hệ thống bài tập Lab 10)

Hệ thống bài tập dưới đây mô phỏng bài toán đảm bảo chất lượng dữ liệu chéo bảng giữa hai bảng `listings` (thông tin chỗ ở) và `reviews` (nhật ký đánh giá) của nền tảng Inside Airbnb tại Santiago. Để bảo đảm tính độc lập và khả năng tự kiểm thử, ta xây dựng bộ dữ liệu mô phỏng chứa đầy đủ các hiện tượng thực tế: bản ghi sau mốc chụp, dòng lặp cặp cột nghiệp vụ, và độ lệch định nghĩa cửa sổ thời gian 12 tháng gần nhất (LTM).

### Dữ liệu thực hành giả lập

```python
import numpy as np
import pandas as pd

if pd.__version__.startswith("2."):
    pd.set_option("mode.copy_on_write", True)

MOC = "2026-06-29"
LTM_BAT_DAU = "2025-06-30"

# Bảng đánh giá mẫu (18 dòng)
DEMO_RV = pd.DataFrame({
    "listing_id": [11, 11, 11, 11, 11, 11, 11, 12, 12, 12, 12, 13, 13, 13, 13, 14, 14, 16],
    "date": pd.to_datetime([
        "2019-03-01", "2024-12-01", "2025-06-30", "2025-08-10", "2025-08-10", "2026-06-29", "2026-06-30",
        "2010-11-13", "2025-06-30", "2026-01-05", "2026-07-01",
        "2023-04-04", "2023-04-04", "2023-04-04", "2025-07-01",
        "2025-12-24", "2026-06-30", "2021-02-02"
    ]),
})

# Bảng chỗ ở mẫu (6 chỗ ở)
DEMO_DS = pd.DataFrame({
    "id": [11, 12, 13, 14, 15, 16],
    "name": ["Depto Lastarria", "Pieza Bellavista", "Loft Providencia", "Casa Ñuñoa", "Studio nuevo", "Hab Centro"],
    "number_of_reviews": [7, 4, 4, 2, 0, 1],
    "number_of_reviews_ltm": [4, 2, 1, 2, 0, 0],
    "last_review": pd.to_datetime(["2026-06-30", "2026-07-01", "2025-07-01", "2026-06-30", None, "2021-02-02"]),
})
```

---

### Bài 1: Kiểm tra miền thời gian của bảng đánh giá

::: exercise Yêu cầu nghiệp vụ
Tên gói dữ liệu ghi nhận mốc chụp công bố là `2026-06-29`. Tuy nhiên trong bảng đánh giá có thể xuất hiện các dòng có ngày tháng vượt quá mốc đó do sự chênh lệch múi giờ hoặc ghi nhận muộn.
Hãy viết hàm `time_domain(rv: pd.DataFrame, moc: str) -> dict` nhận vào bảng đánh giá `rv` (cột `date` kiểu `datetime64`) và chuỗi `moc` dạng `"YYYY-MM-DD"`.

Hàm trả về từ điển gồm ba khóa:
- `"ngay_dau"`: Đối tượng `Timestamp` sớm nhất của cột `date`.
- `"ngay_cuoi"`: Đối tượng `Timestamp` muộn nhất của cột `date`.
- `"so_sau_moc"`: Số nguyên là số dòng có `date > moc`.
Tuyệt đối không làm thay đổi bảng dữ liệu đầu vào.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def time_domain_co_ban(rv: pd.DataFrame, moc: str) -> dict:
    ngay_dau = rv["date"].min()
    ngay_cuoi = rv["date"].max()
    
    moc_ts = pd.Timestamp(moc)
    so_sau_moc = int((rv["date"] > moc_ts).sum())
    
    return {
        "ngay_dau": ngay_dau,
        "ngay_cuoi": ngay_cuoi,
        "so_sau_moc": so_sau_moc
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu

```python
def time_domain(rv: pd.DataFrame, moc: str) -> dict:
    c_date = rv["date"]
    return {
        "ngay_dau": c_date.min(),
        "ngay_cuoi": c_date.max(),
        "so_sau_moc": int((c_date > pd.Timestamp(moc)).sum())
    }
```

#### Phân tích sư phạm chuyên sâu: Chính sách mốc chụp
- **Các dòng sau mốc rơi vào những ngày nào?**
  Các dòng sau mốc chụp thường rơi vào ngày tiếp theo hoặc ngày kế tiếp (trong ví dụ là `2026-06-30` và `2026-07-01`).
- **Có nên đổi mốc công bố thành ngày muộn nhất trong tệp không?**
  Tuyệt đối không. Mốc công bố `2026-06-29` là thời điểm hệ thống bắt đầu quy trình trích xuất cơ sở dữ liệu (`snapshot`). Một số tiến trình ngầm có thể mất vài tiếng hoặc sang ngày hôm sau mới kết thúc ghi nhận nhật ký. Nếu ta tự ý đẩy mốc công bố tiến lên, ta sẽ làm sai lệch định nghĩa chu kỳ 12 tháng gần nhất và phá vỡ tính nhất quán khi đối soát với các bảng khác (như bảng lịch phòng `calendar`). Quy trình chuẩn là ghi nhận số dòng vượt mốc vào báo cáo QA và áp dụng chính sách lọc bỏ đồng bộ các dòng sau mốc công bố.
:::

---

### Bài 2: Kiểm tra toàn vẹn khóa ngoại (Phát hiện đánh giá mồ côi)

::: exercise Yêu cầu nghiệp vụ
Mọi `listing_id` trong bảng đánh giá `rv` bắt buộc phải tồn tại trong cột `id` của bảng danh sách chỗ ở `ds`. Nếu một đánh giá mang mã căn hộ không hề có trong danh mục chỗ ở, đó là một **bản ghi mồ côi**.
Hãy viết hàm `orphan_reviews(rv: pd.DataFrame, ds: pd.DataFrame) -> int` trả về số lượng dòng đánh giá có `listing_id` không nằm trong `ds["id"]`. Mỗi dòng mồ côi đều phải được đếm đầy đủ.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Dùng `isin` và phủ định `~`)

```python
def orphan_reviews_co_ban(rv: pd.DataFrame, ds: pd.DataFrame) -> int:
    tap_hop_hop_le = ds["id"]
    mat_na_co_cha = rv["listing_id"].isin(tap_hop_hop_le)
    so_mo_coi = int((~mat_na_co_cha).sum())
    return so_mo_coi
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Tận dụng cấu trúc `set` tra cứu $\mathcal{O}(1)$)

```python
def orphan_reviews(rv: pd.DataFrame, ds: pd.DataFrame) -> int:
    # Chuyển cột ID thành set băm để tăng tốc độ kiểm tra khi bảng lớn
    id_set = set(ds["id"])
    return int((~rv["listing_id"].isin(id_set)).sum())
```

#### Phân tích sư phạm chuyên sâu: Ý nghĩa của con số 0 vi phạm
- **Vì sao phép kiểm cho kết quả 0 vẫn bắt buộc phải ghi trong báo cáo QA?**
  Trong kiểm toán dữ liệu, con số 0 vi phạm không phải là một thông tin thừa thãi mà là một **chứng chỉ chất lượng (Proof of Integrity)**. Nó chứng minh cho các bên liên quan và khách hàng thấy rằng hệ thống đã thực sự chạy quy trình kiểm định toàn vẹn tham chiếu và cơ sở dữ liệu hoàn toàn sạch sẽ, thay vì việc bỏ qua không kiểm tra.
:::

---

### Bài 3: Kiểm tra khóa tự nhiên và bài học về tính duy nhất

::: exercise Yêu cầu nghiệp vụ
Nhiều người lầm tưởng rằng cặp `(listing_id, date)` có thể làm khóa duy nhất để định danh mỗi lượt đánh giá.
Hãy viết hàm `duplicate_pairs(rv: pd.DataFrame, cot: list = ["listing_id", "date"]) -> int` nhận vào bảng `rv` và danh sách cột ứng viên làm khóa.
Hàm trả về số dòng bị lặp lại theo các cột đó (`duplicated(subset=cot)`, lần xuất hiện đầu tiên không tính là trùng). Hàm chỉ đếm số lượng, tuyệt đối không xóa dòng và không sửa bảng đầu vào.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def duplicate_pairs_co_ban(rv: pd.DataFrame, cot: list = ["listing_id", "date"]) -> int:
    mat_na_lap = rv.duplicated(subset=cot, keep="first")
    return int(mat_na_lap.sum())
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu

```python
def duplicate_pairs(rv: pd.DataFrame, cot: list = ["listing_id", "date"]) -> int:
    return int(rv.duplicated(subset=cot).sum())
```

#### Phân tích sư phạm chuyên sâu: Khóa tự nhiên và rủi ro xóa dữ liệu
- **Các dòng trùng lặp cặp `(listing_id, date)` có phải là lỗi không?**
  Hoàn toàn không phải lỗi. Một chỗ ở có thể đón tiếp nhiều khách hàng độc lập trong cùng một ngày, hoặc một nhóm bạn cùng đi du lịch và mỗi người đều để lại một lời nhận xét trên nền tảng. Vì tệp `reviews` dạng rút gọn này không lưu trữ trường mã người đánh giá (`reviewer_id`), việc xuất hiện nhiều dòng có cùng `listing_id` và cùng `date` là một hiện tượng tự nhiên của đời sống.
- **Hậu quả nếu lập trình viên gọi `drop_duplicates(subset=["listing_id", "date"])`**:
  Trên dữ liệu thực tế tại Santiago, thao tác này sẽ xóa sổ oan uổng **3.548 đánh giá có thật** của khách hàng, làm sai lệch tổng số lượt đánh giá của các căn hộ và phá vỡ tính khớp nối với bảng `listings`.
:::

---

### Bài 4: Đối chiếu cột dẫn xuất tổng số đánh giá với số tự đếm

::: exercise Yêu cầu nghiệp vụ
Bảng `listings` có sẵn cột `number_of_reviews`. Hãy viết hàm `review_count_check(rv: pd.DataFrame, ds: pd.DataFrame) -> dict` nhận vào hai bảng để đối soát tính nhất quán.
Hàm trả về từ điển gồm hai khóa:
- `"dem_that"`: Series số nguyên có **cùng chỉ mục với `ds`**, thể hiện số lượng dòng đánh giá của từng chỗ ở được đếm trực tiếp từ bảng `rv` (`groupby("listing_id").size()`, sau đó khớp theo `ds["id"]`), chỗ ở nào không có đánh giá nào phải mang giá trị là $0$.
- `"so_lech_tong"`: Số nguyên là số lượng chỗ ở có giá trị `number_of_reviews` khác với `"dem_that"`.
Tuyệt đối không thêm cột vào DataFrame `ds` gốc.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan (Dùng `map` và `fillna`)

```python
def review_count_check_co_ban(rv: pd.DataFrame, ds: pd.DataFrame) -> dict:
    # 1. Đếm số dòng theo từng chỗ ở
    so_dem = rv.groupby("listing_id").size()
    
    # 2. Ánh xạ vào từng dòng của ds theo cột id
    dem_that = ds["id"].map(so_dem).fillna(0).astype(int)
    dem_that.index = ds.index
    
    # 3. So sánh với cột có sẵn
    lech = dem_that != ds["number_of_reviews"]
    so_lech = int(lech.sum())
    
    return {
        "dem_that": dem_that,
        "so_lech_tong": so_lech
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Tận dụng `reindex` trên Series)

```python
def review_count_check(rv: pd.DataFrame, ds: pd.DataFrame) -> dict:
    # Đếm và reindex trực tiếp theo mảng id của ds
    so_dem = rv.groupby("listing_id").size()
    dem_that = so_dem.reindex(ds["id"], fill_value=0).set_axis(ds.index)
    
    so_lech = int((dem_that != ds["number_of_reviews"]).sum())
    return {
        "dem_that": dem_that,
        "so_lech_tong": so_lech
    }
```

#### Phân tích sư phạm chuyên sâu: Diễn giải kết quả khớp
- **Khớp toàn bộ nghĩa là gì?**
  Nếu `so_lech_tong == 0`, điều đó chứng minh rằng con số `number_of_reviews` trong bảng `listings` được sinh ra từ chính tập dữ liệu đầy đủ của `reviews`, bao gồm cả những dòng có ngày sau mốc công bố `2026-06-29`. Nếu quy trình của bạn áp dụng chính sách cắt bỏ các dòng sau mốc, cột dẫn xuất `number_of_reviews` sẽ không còn khớp hoàn toàn và cần được tính toán lại trong pha làm sạch dữ liệu.
:::

---

### Bài 5: Đối soát cột LTM và phân tích độ lệch định nghĩa cửa sổ

::: exercise Yêu cầu nghiệp vụ
Cột `number_of_reviews_ltm` đại diện cho số đánh giá trong 12 tháng gần nhất (Last Twelve Months - LTM). Ta tự đếm từ bảng `rv` với ngày bắt đầu cửa sổ `bat_dau` (ví dụ `"2025-06-30"`) và ngày kết thúc tùy chọn `ket_thuc` (nếu bằng `None` tức là không chặn trên).
Hãy viết hàm `ltm_mismatch(rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str | None = None) -> dict`.

Hàm trả về từ điển gồm ba khóa:
- `"ltm_that"`: Series số nguyên cùng chỉ mục với `ds`, đếm số đánh giá thỏa mãn `bat_dau <= date` (và `date <= ket_thuc` nếu có tham số), chỗ ở không có thì điền $0$.
- `"do_lech"`: Series số nguyên bằng `ds["number_of_reviews_ltm"] - ltm_that`.
- `"so_lech_ltm"`: Số nguyên là số lượng chỗ ở có `do_lech != 0`.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def ltm_mismatch_co_ban(rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str | None = None) -> dict:
    ts_bat_dau = pd.Timestamp(bat_dau)
    mat_na = rv["date"] >= ts_bat_dau
    if ket_thuc is not None:
        mat_na = mat_na & (rv["date"] <= pd.Timestamp(ket_thuc))
        
    rv_cua_so = rv.loc[mat_na]
    dem_cua_so = rv_cua_so.groupby("listing_id").size()
    
    ltm_that = ds["id"].map(dem_cua_so).fillna(0).astype(int)
    ltm_that.index = ds.index
    
    do_lech = ds["number_of_reviews_ltm"] - ltm_that
    so_lech_ltm = int((do_lech != 0).sum())
    
    return {
        "ltm_that": ltm_that,
        "do_lech": do_lech,
        "so_lech_ltm": so_lech_ltm
    }
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu

```python
def ltm_mismatch(rv: pd.DataFrame, ds: pd.DataFrame, bat_dau: str, ket_thuc: str | None = None) -> dict:
    c_date = rv["date"]
    cond = c_date >= pd.Timestamp(bat_dau)
    if ket_thuc is not None:
        cond &= (c_date <= pd.Timestamp(ket_thuc))
        
    counts = rv.loc[cond].groupby("listing_id").size()
    ltm_that = counts.reindex(ds["id"], fill_value=0).set_axis(ds.index)
    do_lech = ds["number_of_reviews_ltm"] - ltm_that
    
    return {
        "ltm_that": ltm_that,
        "do_lech": do_lech,
        "so_lech_ltm": int((do_lech != 0).sum())
    }
```

#### Phân tích sư phạm chuyên sâu: Phân bố độ lệch LTM
- Trên dữ liệu thực tế tại Santiago với `bat_dau="2025-06-30"` và không chặn trên, có 665 chỗ ở bị lệch và phần lớn các chỗ ở bị lệch đúng **$-1$**.
- **Điều này gợi ý điều gì?**
  Độ lệch tập trung gần như tuyệt đối ở mức $-1$ gợi ý rằng Inside Airbnb đã áp dụng một quy ước cửa sổ hơi khác một ngày so với giả thuyết của ta (chẳng hạn bắt đầu từ ngày `2025-07-01` thay vì `2025-06-30`, hoặc áp dụng quy ước khoảng nửa mở `>` thay vì `>=`). Việc khảo sát phân bố độ lệch thay vì chỉ nhìn vào số lượng bản ghi lệch giúp nhà phân tích hiểu rõ bản chất toán học của sự khác biệt.
:::

---

### Bài 6: Đóng gói báo cáo kiểm toán chất lượng dữ liệu (`qa_report`)

::: exercise Yêu cầu nghiệp vụ
Hãy viết hàm `qa_report(so_dong: dict, ghi_chu: dict, path) -> pd.DataFrame` nhận vào:
- `so_dong`: Từ điển `{tên_quy_tắc: số_dòng_vi_phạm}` (bảo toàn thứ tự các khóa).
- `ghi_chu`: Từ điển `{tên_quy_tắc: nội_dung_ghi_chú}`.
- `path`: Đường dẫn tệp CSV cần ghi (thư mục cha đã tồn tại).

Hàm tạo DataFrame gồm đúng ba cột `quy_tac`, `so_dong`, `ghi_chu`, mỗi quy tắc trong `so_dong` là một dòng theo đúng thứ tự (kể cả quy tắc có $0$ dòng vi phạm; nếu quy tắc không có trong `ghi_chu` thì điền chuỗi rỗng `""`).
Ghi tệp bằng `to_csv(path, index=False)` với mã hóa UTF-8, sau đó đọc lại bằng `pd.read_csv(path, keep_default_na=False)` và trả về DataFrame đọc lại.
:::

::: solution
#### Cách 1: Tiếp cận Căn bản & Trực quan

```python
def qa_report_co_ban(so_dong: dict, ghi_chu: dict, path) -> pd.DataFrame:
    danh_sach_dong = []
    for quy_tac, so in so_dong.items():
        chu_thich = ghi_chu.get(quy_tac, "")
        danh_sach_dong.append({
            "quy_tac": quy_tac,
            "so_dong": int(so),
            "ghi_chu": chu_thich
        })
        
    df_report = pd.DataFrame(danh_sach_dong)
    df_report.to_csv(path, index=False, encoding="utf-8")
    
    return pd.read_csv(path, keep_default_na=False)
```

#### Cách 2: Tiếp cận Nâng cao & Tối ưu (Cấu trúc bảng từ mảng ánh xạ)

```python
def qa_report(so_dong: dict, ghi_chu: dict, path) -> pd.DataFrame:
    df_report = pd.DataFrame({
        "quy_tac": list(so_dong.keys()),
        "so_dong": list(so_dong.values()),
        "ghi_chu": [ghi_chu.get(k, "") for k in so_dong.keys()]
    })
    
    df_report.to_csv(path, index=False, encoding="utf-8")
    return pd.read_csv(path, keep_default_na=False)
```

#### Phân tích so sánh & Trực giác bản chất
- Tham số `keep_default_na=False` khi đọc lại tệp CSV là cực kỳ quan trọng. Nếu không thiết lập tham số này, các chuỗi rỗng `""` trong cột `ghi_chu` sẽ bị pandas tự động chuyển đổi thành `NaN`, làm sai lệch cấu trúc văn bản ban đầu của báo cáo kiểm toán.
:::

---

### Bài tự làm mở rộng: Thiết kế bộ quy tắc QA 4 thành phần cho dự án thực tế

::: exercise Đề bài mở rộng
Hãy thiết lập một bộ quy tắc QA hoàn chỉnh gồm 4 thành phần bắt buộc cho một dự án xử lý dữ liệu thực tế:
1. **Tên quy tắc (Rule Name)**
2. **Điều kiện kiểm tra (Assertion Condition)**
3. **Lý do nghiệp vụ (Business Rationale)**
4. **Hành động xử lý (Action Policy)**

Thực thi bộ quy tắc trên một bảng dữ liệu giả lập và xuất ra bảng tổng hợp kiểm toán.
:::

::: solution
#### Mã nguồn thực thi bộ quy tắc 4 thành phần

```python
# Bộ dữ liệu thử nghiệm nghiệp vụ
du_lieu_demo = pd.DataFrame({
    "ma_phong": [101, 102, 103, 104, 105],
    "gia_dem": [500, 700, -50, 1200, 80000], # có giá âm và ngoại lai
    "so_khach_toi_da": [2, 4, 0, 6, 2],       # có số khách bằng 0
    "trang_thai": ["hoat_dong", "hoat_dong", "dong_cua", "hoat_dong", "hoat_dong"]
})

# Khung định nghĩa quy tắc 4 thành phần
QUY_TAC_QA = [
    {
        "ten": "GIA_DUONG",
        "dieu_kien": lambda df: df["gia_dem"] > 0,
        "ly_do": "Giá thuê mỗi đêm bắt buộc phải là số dương",
        "hanh_dong": "Loại bỏ bản ghi và đưa vào sổ theo dõi dữ liệu lỗi"
    },
    {
        "ten": "SO_KHACH_HOP_LE",
        "dieu_kien": lambda df: df["so_khach_toi_da"] >= 1,
        "ly_do": "Phòng cho thuê phải chứa được ít nhất 1 khách",
        "hanh_dong": "Gán cờ cảnh báo thông tin phòng chưa hoàn thiện"
    },
    {
        "ten": "GIA_KHONG_VUOT_TRAN",
        "dieu_kien": lambda df: df["gia_dem"] <= 50000,
        "ly_do": "Giá đêm vượt 50 triệu/đêm là ngoại lai cần thẩm định",
        "hanh_dong": "Gắn cờ kiểm duyệt thủ công bởi chuyên viên"
    }
]

ket_qua_kiem_toan = []
for qt in QUY_TAC_QA:
    hop_le = qt["dieu_kien"](du_lieu_demo)
    so_vi_pham = int((~hop_le).sum())
    ket_qua_kiem_toan.append({
        "quy_tac": qt["ten"],
        "so_vi_pham": so_vi_pham,
        "ly_do": qt["ly_do"],
        "hanh_dong": qt["hanh_dong"]
    })

df_kiem_toan = pd.DataFrame(ket_qua_kiem_toan)
print("BÁO CÁO KIỂM TOÁN CHẤT LƯỢNG DỮ LIỆU:")
print(df_kiem_toan.to_string(index=False))
```

#### Bình luận chuyên môn
Khung quy tắc 4 thành phần (Tên – Điều kiện – Lý do – Hành động) là tiêu chuẩn vàng của kỹ nghệ dữ liệu hiện đại (Data Engineering). Nó biến các đoạn mã kiểm tra vụn vặt thành một quy trình nghiệp vụ rõ ràng, giúp đội ngũ kỹ thuật và các chuyên viên kinh doanh có chung một tiếng nói khi đánh giá độ tin cậy của kho dữ liệu.
:::

---

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
