---
course: xu-ly-du-lieu
lecture: bai-05-series-dataframe-chuyen-sau
section: lecture
title: "Series & DataFrame chuyên sâu"
prerequisites: ["chi-muc", "gia-tri-thieu", "vector-hoa"]
lessonStatus: ready
description: "Cơ chế căn chỉnh Index, Split-Apply-Combine với groupby/agg/transform, bảng chéo pivot_table và ghép bảng an toàn với merge validate."
---

## 1. Cơ chế Căn chỉnh Index và Phân kỳ giữa `.loc` và `.iloc`

### 1.1. Bản chất của Index: Nhãn Ngữ nghĩa khác với Vị trí Bộ nhớ
Điểm độc đáo nhất và cũng là nguồn gốc gây ra nhiều bất ngờ nhất cho người mới học pandas chính là: **Pandas luôn tự động căn chỉnh dữ liệu theo nhãn chỉ mục (Index Alignment)**, hoàn toàn không phụ thuộc vào vị trí dòng trong bộ nhớ.

<DataDiagram name="index-alignment" />

Trong phép trừ `B - A`, pandas không lấy dòng 1 trừ dòng 1 như NumPy! Nó đi tìm phần tử có cùng nhãn `"A"` ở cả hai bên ($90 - 100 = -10$), và phần tử có cùng nhãn `"B"` ($220 - 200 = 20$). Các nhãn chỉ xuất hiện ở một phía (nhãn `"C"` chỉ có ở $A$, nhãn `"D"` chỉ có ở $B$) do thiếu toán hạng đối ứng nên kết quả tự động trở thành `NaN`.
Index của Series kết quả là **hợp của hai tập nhãn (*Union of indexes*)**: `{"A", "B", "C", "D"}`.

### 1.2. Phân định Tuyệt đối giữa `.loc` và `.iloc`
Khi một bảng dữ liệu có Index là các số nguyên không liên tục (ví dụ sau khi xáo trộn hoặc lọc dòng): `index = [2, 0, 5]`:
- **`s.loc[nhan]`**: Tra cứu theo **nhãn định danh**. `s.loc[2]` tìm phần tử có nhãn bằng số `2` (đứng ở dòng đầu tiên).
- **`s.iloc[vi_tri]`**: Tra cứu theo **vị trí số nguyên vật lý** trong mảng ($0, 1, \dots, n-1$ hoặc $-1$ từ cuối). `s.iloc[2]` lấy phần tử ở dòng thứ ba (mang nhãn `5`).

Trong môi trường sản xuất, ta không bao giờ dùng cú pháp nhập nhằng `s[2]`. Luôn luôn chỉ định tường minh `.loc` khi làm việc với nhãn nghiệp vụ và `.iloc` khi đếm vị trí tương đối.

---

## 2. Mô hình Chia để trị: `groupby`, `agg` và `transform`

Trong phân tích dữ liệu, hầu hết các câu hỏi nghiệp vụ đều tuân theo mô hình **Split-Apply-Combine (Tách nhóm - Áp dụng - Gộp kết quả)** do Hadley Wickham hệ thống hóa:
1. **Split**: Chia dữ liệu thành các nhóm độc lập dựa trên một hoặc nhiều biến phân loại (ví dụ: Chia theo quận hoặc theo phân khúc giá).
2. **Apply**: Áp dụng một hàm tính toán lên từng nhóm.
3. **Combine**: Gộp kết quả của các nhóm thành một cấu trúc dữ liệu mới.

<DataDiagram name="groupby" />

### 2.1. Cú pháp Đặt tên Cột Tổng hợp (Named Aggregation)
Thay vì dùng cú pháp cũ trả về MultiIndex phức tạp, pandas hỗ trợ cú pháp đặt tên cột trực tiếp cực kỳ tường minh:
```python
thong_ke = df.groupby("phan_khuc").agg(
    so_phong=("id", "size"),
    gia_trung_vi=("price", "median"),
    review_nam_tb=("number_of_reviews_ltm", "mean")
)
```
Mỗi tham số là một tuple gồm `("tên_cột_nguồn", "hàm_tổng_hợp")`. Bảng kết quả trả về các cột phẳng, đúng tên nghiệp vụ mong muốn và sẵn sàng xuất bản.

### 2.2. Điểm Khác biệt Sống còn giữa `agg` và `transform`
- **`agg` (Aggregate)**: Làm **suy giảm số chiều dữ liệu**. Nếu có 10 nhóm, kết quả trả về đúng 10 dòng đại diện.
- **`transform`**: **Bảo tồn nguyên vẹn số dòng của bảng ban đầu**. Hàm tính toán chỉ số cho từng nhóm rồi phát tán (*broadcast*) ngược lại cho từng bản ghi thuộc nhóm đó.

Ví dụ: Bạn muốn biết mỗi phòng trọ nằm trong một quận có quy mô bao nhiêu phòng, để từ đó lọc bỏ các phòng thuộc các quận quá nhỏ ($< 300$ phòng):
```python
# Gắn quy mô quận vào từng dòng (Series cùng độ dài với bảng gốc):
n_quan = df.groupby("neighbourhood")["id"].transform("size")

# Lọc các dòng thuộc quận lớn mà không làm biến dạng cấu trúc bảng:
df_quan_lon = df[n_quan >= 300]
```
Nếu dùng `agg("size")`, bạn chỉ nhận được một bảng danh sách quận và số đếm, không thể lọc trực tiếp trên các dòng của bảng gốc.

---

## 3. Bảng chéo Hai chiều (`pivot_table`) và Phát hiện Biến ẩn

Khi cần khảo sát mối quan hệ giữa hai biến phân loại độc lập lên một biến đo lường liên tục, công cụ chuẩn mực là `pivot_table`:
- **`index`**: Biến phân nhóm theo chiều dọc (các hàng).
- **`columns`**: Biến phân nhóm theo chiều ngang (các cột).
- **`values`**: Cột dữ liệu cần tổng hợp.
- **`aggfunc`**: Phép toán thống kê (mặc định là `"mean"`).

```python
pv = df.pivot_table(
    index="phan_khuc",
    columns="chuyen",
    values="number_of_reviews_ltm",
    aggfunc="mean"
)
```

### Ý nghĩa kinh tế lượng: Kiểm soát Biến ẩn Ngoại sinh (*Confounder*)
Xét câu hỏi: *"Các chủ nhà chuyên nghiệp (sở hữu $\ge 5$ phòng) có hoạt động hiệu quả hơn chủ nhà cá nhân không?"*
- Nếu chỉ so sánh một chiều đơn giản qua `groupby("chuyen")`, ta thấy chủ nhà chuyên nghiệp có số lượt đánh giá trung bình cao hơn ($15.2$ so với $12.7$).
- Tuy nhiên, khi tách ma trận hai chiều bằng `pivot_table` theo từng phân khúc giá: Ta phát hiện ở cùng phân khúc cao cấp, số review của chủ nhà chuyên nghiệp và cá nhân là tương đương nhau.
- Sở dĩ số liệu chung của nhóm chuyên nghiệp cao hơn là vì họ tập trung tới $80\%$ cơ sở tại các quận trung tâm du lịch sầm uất (nơi có lưu lượng khách tự nhiên rất lớn). Địa điểm quận chính là một **biến ẩn ngoại sinh (*Confounding Variable*)**. `pivot_table` giúp bóc tách và phân lập các hiệu ứng này một cách minh bạch.

---

## 4. Hợp nhất Bảng Dữ liệu (`merge`) và Kỷ luật `validate`

### 4.1. Bốn Kiểu Ghép Nối Đại số Quan hệ
Khi kết hợp bảng `df_trai` với bảng `df_phai` theo khóa liên kết `on="khoa"`:
- `how="left"`: Giữ trọn vẹn mọi dòng của bảng trái. Bảng phải không khớp sẽ điền `NaN`.
- `how="right"`: Giữ trọn vẹn mọi dòng của bảng phải.
- `how="inner"`: Chỉ giữ lại các dòng mà khóa xuất hiện ở cả hai bảng (phép giao).
- `how="outer"`: Giữ lại toàn bộ các dòng của cả hai bảng (phép hợp).

### 4.2. Vũ khí Phòng thủ Toàn vẹn Dữ liệu: `validate="m:1"`
Trong các đường ống xử lý dữ liệu doanh nghiệp, một trong những thảm họa kinh hoàng nhất là lỗi **Nhân bản số dòng ngoài tầm kiểm soát (*Row Explosion / Cartesian Bug*)**.
Giả sử bạn có bảng giao dịch gồm $18,534$ dòng, và bạn muốn ghép thêm bảng biểu phí dịch vụ theo phân khúc gồm 3 dòng (`re: 10%`, `trung: 13%`, `cao: 15%`).
Nếu vô tình bảng biểu phí bị lỗi hệ thống và xuất hiện hai dòng cùng mang nhãn `"trung"`, một phép ghép `how="left"` thông thường sẽ nhân đôi mỗi giao dịch ở phân khúc trung! Bảng kết quả sẽ phình to lên thành $30,000$ dòng và toàn bộ báo cáo doanh thu tài chính bị đội lên gấp bội mà không hề có bất kỳ thông báo lỗi nào!

Để ngăn chặn thảm họa này, pandas cung cấp tham số kiểm định **`validate`**:
- `validate="1:1"`: Kiểm tra khóa ở cả hai bảng đều phải là duy nhất.
- `validate="1:m"`: Khóa ở bảng trái là duy nhất, bảng phải có thể lặp lại.
- **`validate="m:1"`**: Khóa ở bảng trái có thể lặp lại nhiều lần, nhưng **khóa ở bảng tra cứu bên phải BẮT BUỘC phải là duy nhất**.

```python
# Nếu bảng phi có khóa phân khúc bị trùng lặp,
# pandas sẽ lập tức dừng chương trình và ném lỗi pd.errors.MergeError!
m = pd.merge(df, phi, on="phan_khuc", how="left", validate="m:1")
```

---

## 5. Bài tập Thực chiến Phòng Lab 05 (100% Nội dung Lab) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 6. Tổng kết Bài học

1. **Hiểu rõ Index Alignment**: Phép toán giữa hai Series luôn tự động so khớp theo nhãn chỉ mục. Khi nhãn bị lệch, kết quả sẽ sinh ra `NaN`.
2. **Phân biệt `agg` và `transform`**: `agg` dùng để thu gọn và tóm tắt theo nhóm; `transform` dùng để tính toán và phát tán ngược lại từng dòng mà không làm thay đổi kích thước bảng ban đầu.
3. **Phân tích đa chiều với `pivot_table`**: Luôn kiểm tra các tương tác chéo để tránh cào bằng số liệu và nhận diện các biến ẩn ngoại sinh.
4. **Kỷ luật `validate="m:1"` khi nối bảng**: Luôn kiểm định quan hệ khóa ngoại khi thực hiện `pd.merge()` để bảo vệ đường ống dữ liệu khỏi lỗi nhân bản số dòng.
