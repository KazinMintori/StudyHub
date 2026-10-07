---
title: Bài tập ôn luyện - Xử lý dữ liệu thông minh
description: Tuyển tập bài tập tiền xử lý dữ liệu, chuẩn hóa số liệu, thuật toán MapReduce/Spark, TF-IDF và mô hình OLAP.
---

# Bài tập ôn luyện: Xử lý dữ liệu thông minh

Tài liệu tuyển tập bài tập cho môn Xử lý dữ liệu thông minh, tập trung vào kỹ thuật tiền xử lý dữ liệu định lượng, tính toán phân tán với mô hình MapReduce/Spark và khai phá đặc trưng văn bản.

---

## Phần 1. Tiền xử lý dữ liệu & Chuẩn hóa (Data Preprocessing)

### Bài 1.1: Chuẩn hóa dữ liệu Min-Max và Z-Score
Cho tập mẫu quan sát về thu nhập hàng tháng (đơn vị: triệu đồng) của 8 nhân viên:
$$X = \{10, 12, 14, 15, 18, 20, 25, 46\}$$

1. Tính giá trị trung bình mẫu $\bar{x}$, độ lệch chuẩn mẫu $s$ (dùng mẫu hiệu chỉnh $N-1$), và khoảng tứ phân vị $IQR = Q_3 - Q_1$.
2. Áp dụng chuẩn hóa Min-Max về đoạn $[0, 1]$ cho giá trị $x = 25$. Công thức:
   $$x_{\text{norm}} = \frac{x - \min(X)}{\max(X) - \min(X)}$$
3. Áp dụng chuẩn hóa Z-Score cho giá trị $x = 46$. Công thức:
   $$z = \frac{x - \bar{x}}{s}$$
4. Nhận xét về giá trị $46$: giá trị này có phải là một ngoại lai (outlier) theo quy tắc hàng rào Tukey $1.5 \times IQR$ không?

#### Lời giải gợi ý
1. Thống kê mô tả:
   - Số phần tử $N = 8$. Tổng $\sum x_i = 10 + 12 + 14 + 15 + 18 + 20 + 25 + 46 = 160$.
   - Trung bình mẫu: $\bar{x} = \frac{160}{8} = 20.0$.
   - Phương sai mẫu:
     $$\sum (x_i - \bar{x})^2 = (-10)^2 + (-8)^2 + (-6)^2 + (-5)^2 + (-2)^2 + 0^2 + 5^2 + 26^2 = 100 + 64 + 36 + 25 + 4 + 0 + 25 + 676 = 930$$
     $$s^2 = \frac{930}{8 - 1} = \frac{930}{7} \approx 132.86 \implies s = \sqrt{132.86} \approx 11.53$$
   - Tứ phân vị:
     Nửa dưới $\{10, 12, 14, 15\} \implies Q_1 = \frac{12 + 14}{2} = 13.0$.
     Nửa trên $\{18, 20, 25, 46\} \implies Q_3 = \frac{20 + 25}{2} = 22.5$.
     $IQR = Q_3 - Q_1 = 22.5 - 13.0 = 9.5$.

2. Chuẩn hóa Min-Max với $x = 25$:
   $$\min(X) = 10, \quad \max(X) = 46$$
   $$x_{\text{norm}} = \frac{25 - 10}{46 - 10} = \frac{15}{36} = \frac{5}{12} \approx 0.4167$$

3. Chuẩn hóa Z-Score với $x = 46$:
   $$z = \frac{46 - 20.0}{11.53} = \frac{26}{11.53} \approx 2.255$$

4. Kiểm tra ngoại lai theo quy tắc Tukey:
   - Ngưỡng trên (Upper Fence): $Q_3 + 1.5 \times IQR = 22.5 + 1.5 \times 9.5 = 22.5 + 14.25 = 36.75$.
   - Vì $46 > 36.75$, nên giá trị $46$ là một ngoại lai (mild outlier) theo tiêu chuẩn Tukey.

---

## Phần 2. Mô hình tính toán phân tán (MapReduce & Spark)

### Bài 2.1: Thiết kế giải thuật MapReduce tính điểm trung bình sinh viên
Cho một file nhật ký điểm số lớn chứa các dòng bản ghi có cấu trúc:
`(SinhVienID, MonHoc, SoTinChi, DiemSo)`
Ví dụ:
`("SV01", "Toan", 3, 8.5)`
`("SV01", "Ly", 4, 7.0)`
`("SV02", "Toan", 3, 9.0)`

Mục tiêu: Tính điểm trung bình tích lũy có trọng số (GPA theo tín chỉ) của từng sinh viên:
$$\text{GPA} = \frac{\sum (\text{SoTinChi} \times \text{DiemSo})}{\sum \text{SoTinChi}}$$

1. Hãy viết mã giả cho hàm `Map(key, value)`. Chỉ rõ đầu vào và các cặp `(key_out, value_out)` phát ra.
2. Trình bày cơ chế `Shuffle & Sort` của framework giữa pha Map và pha Reduce.
3. Hãy viết mã giả cho hàm `Reduce(key_in, list_values)`.

#### Lời giải gợi ý
1. Hàm Map:
   - Đầu vào: `key = offset dòng`, `value = chuỗi "SinhVienID, MonHoc, SoTinChi, DiemSo"`.
   - Phân tích chuỗi: tách thành các trường $sv\_id$, $mon$, $tin\_chi$, $diem$.
   - Tính tích điểm và tín chỉ: $tong\_diem = tin\_chi \times diem$.
   - Phát ra cặp khóa-giá trị:
     $$\text{EmitIntermediate}(sv\_id, (tin\_chi, tong\_diem))$$

2. Giai đoạn Shuffle & Sort:
   Hệ thống tự động gom nhóm tất cả các giá trị phát ra từ các worker Map có cùng khóa $sv\_id$ lại với nhau và chuyển tới cùng một Reduce worker, tạo thành danh sách `list_values = [(tc_1, td_1), (tc_2, td_2), ...]`.

3. Hàm Reduce:
   ```python
   def reduce(student_id, list_tuples):
       total_credits = 0
       total_weighted_score = 0.0
       for credits, weighted_score in list_tuples:
           total_credits += credits
           total_weighted_score += weighted_score
       if total_credits > 0:
           gpa = total_weighted_score / total_credits
           emit(student_id, gpa)
   ```

---

## Phần 3. Trích xuất đặc trưng văn bản & TF-IDF

### Bài 3.1: Tính toán trọng số TF-IDF và Cosine Similarity
Cho tập ngữ liệu gồm 3 văn bản ngắn sau:
- $D_1$: "học máy dữ liệu"
- $D_2$: "khoa học dữ liệu thuật toán"
- $D_3$: "thuật toán học máy"

Xét từ khóa $t_1 = \text{"máy"}$ và $t_2 = \text{"thuật toán"}$.

1. Tính tần suất xuất hiện của từ (Term Frequency - $TF$) chuẩn hóa theo độ dài văn bản cho từng từ trong mỗi văn bản:
   $$TF(t, D) = \frac{f(t, D)}{|D|}$$
2. Tính tần số nghịch đảo văn bản (Inverse Document Frequency - $IDF$) với công thức:
   $$IDF(t) = \ln\left(\frac{N}{DF(t)}\right)$$
   (với $N = 3$ là tổng số văn bản, $DF(t)$ là số văn bản chứa từ $t$).
3. Tính trọng số $TF\text{-}IDF(t, D_1)$ cho cả hai từ.
4. Lập vector biểu diễn không gian $TF\text{-}IDF$ và tính độ tương đồng Cosine giữa văn bản $D_1$ và $D_3$.

#### Lời giải gợi ý
1. Độ dài các văn bản: $|D_1| = 3$, $|D_2| = 4$, $|D_3| = 3$.
   - Tần suất $TF(\text{"máy"}, D_1) = 1/3 \approx 0.333$.
   - Tần suất $TF(\text{"thuật toán"}, D_1) = 0$.
   - Tần suất $TF(\text{"máy"}, D_3) = 1/3 \approx 0.333$.
   - Tần suất $TF(\text{"thuật toán"}, D_3) = 1/3 \approx 0.333$.

2. Tính $IDF$:
   - Từ "máy" xuất hiện trong $D_1$ và $D_3 \implies DF = 2 \implies IDF(\text{"máy"}) = \ln(3/2) \approx 0.4055$.
   - Từ "thuật toán" xuất hiện trong $D_2$ và $D_3 \implies DF = 2 \implies IDF(\text{"thuật toán"}) = \ln(3/2) \approx 0.4055$.

3. Trọng số $TF\text{-}IDF$:
   $$TF\text{-}IDF(\text{"máy"}, D_1) = \frac{1}{3} \times 0.4055 \approx 0.1352$$
   $$TF\text{-}IDF(\text{"thuật toán"}, D_1) = 0$$

4. Độ tương đồng Cosine:
   $$\text{Cosine}(u, v) = \frac{u \cdot v}{\|u\|_2 \|v\|_2}$$
   Tính tích vô hướng và chuẩn của hai vector đặc trưng để tìm mức độ tương đồng giữa hai tài liệu.
