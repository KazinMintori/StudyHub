---
course: xu-ly-du-lieu
lecture: bai-07-xu-ly-chuoi
section: lecture
title: "Xử lý dữ liệu chuỗi"
prerequisites: ["bien-kieu", "gia-tri-thieu", "vector-hoa"]
lessonStatus: ready
description: "Chuẩn hóa chuỗi, phân biệt chuỗi ký tự nguyên bản với mẫu regex, trích xuất thực thể bằng str.extract và làm sạch văn bản quy mô lớn."
---

## 1. Kiến trúc Bộ định tuyến `.str` và Chuẩn hóa Chuỗi Đa tầng

Trong thế giới thực, dữ liệu văn bản tự do luôn là vùng đất hỗn loạn và nhiều cạm bẫy nhất. Người dùng nhập liệu với muôn vàn thói quen dị biệt: Lúc viết hoa, lúc viết thường, gõ thừa khoảng trắng, sử dụng lẫn lộn tiếng lóng, và đặc biệt là hệ thống dấu thanh phức tạp của các ngôn ngữ quốc tế.

pandas cung cấp bộ định tuyến chuyên dụng **`.str`**. Bất kỳ phương thức nào được gọi qua `.str` (như `.str.strip()`, `.str.lower()`, `.str.replace()`) đều được vector hóa ở tầng dưới và sở hữu một đặc tính vô cùng quý giá: **Tự động bỏ qua các giá trị khuyết thiếu `NaN` mà không làm sập chương trình với lỗi `AttributeError`**.

<DataDiagram name="string-cleaning" />

### 1.1. Chuẩn hóa Bảng mã Unicode Tiếng Việt (NFC vs NFD)
Một cạm bẫy kỹ thuật kinh điển đối với dữ liệu văn bản tiếng Việt là hiện tượng hai ký tự nhìn giống hệt nhau trên màn hình nhưng máy tính lại coi là khác nhau:
- **NFC (Dựng sẵn - Precomposed)**: Ký tự chữ "à" được gán một mã điểm Unicode duy nhất (`U+00E0`).
- **NFD (Tổ hợp - Decomposed)**: Ký tự chữ "à" được hình thành bằng cách ghép chữ cái gốc "a" (`U+0061`) với dấu huyền rời (`U+0300`).

Toán tử so sánh `==` sẽ trả về `False` khi đối chiếu hai chuỗi này vì các chuỗi byte nhị phân bên dưới hoàn toàn khác biệt. Do đó, bước chuẩn hóa đầu tiên đối với dữ liệu tiếng Việt luôn là:
```python
s_chuan = s.str.normalize("NFC")
```

### 1.2. Chuỗi Xử lý Chuẩn hóa Ba Bước
Đối với hầu hết các bài toán tiền xử lý văn bản, quy trình chuẩn hóa gồm 3 bước:
1. `str.strip()`: Cắt tỉa khoảng trắng thừa ở hai đầu chuỗi.
2. `str.lower()` (hoặc `str.casefold()`): Đưa toàn bộ về chữ thường để đồng nhất đối sánh.
3. `str.replace(r"\s+", " ", regex=True)`: Thu gọn nhiều khoảng trắng liên tiếp ở giữa các từ thành đúng một dấu cách đơn.

---

## 2. Phân định Tuyệt đối giữa Chuỗi Nguyên bản (Literal) và Mẫu Regex

Biểu thức chính quy (*Regular Expression - Regex*) là một ngôn ngữ hình thức cực kỳ mạnh mẽ để mô tả mẫu văn bản. Tuy nhiên, trong Regex, một số ký tự được quy ước là các **siêu ký tự cú pháp (*Metacharacters*)** chứ không đại diện cho ký tự chữ thông thường:
- Dấu chấm `.`: Đại diện cho **bất kỳ ký tự nào** (ngoại trừ ký tự ngắt dòng).
- Dấu đô la `$`: Neo vị trí **kết thúc chuỗi**.
- Dấu mũ `^`: Neo vị trí **bắt đầu chuỗi**.
- Dấu ngoặc đơn `()`: Đóng khung **nhóm bắt (*Capturing Group*)**.
- Dấu sổ thẳng `|`: Toán tử **hoặc**.

```python
import pandas as pd

s = pd.Series(["giá 50.000", "giá 50,000", None])

# 1. NGUY HIỂM: regex=True (mặc định)
# Dấu '.' khớp với cả dấu phẩy ','! Cả hai dòng đều ra True:
print(s.str.contains("50.000", regex=True, na=False).tolist())   # [True, True, False]

# 2. CHUẨN MỰC: regex=False
# Chỉ khớp chính xác dấu chấm nguyên văn:
print(s.str.contains("50.000", regex=False, na=False).tolist())  # [True, False, False]
```

### Bẫy Giá trị Khuyết thiếu trong `str.contains()`
Khi thực hiện kiểm tra `s.str.contains("tu_khoa")`, nếu một dòng chứa giá trị `NaN`, pandas mặc định sẽ trả về `NaN` cho dòng đó thay vì `False`.
Nếu bạn cố gắng tính tổng số dòng thỏa mãn bằng `.sum()`, pandas sẽ cộng dồn các giá trị logic nhưng dòng `NaN` sẽ làm kết quả bị sai lệch hoặc gây lỗi khi áp dụng làm mặt nạ Boolean cho lệnh lọc `df[mask]`.
**Quy tắc vàng**: Luôn luôn chỉ định tham số `na=False` khi sử dụng `str.contains()`:
```python
mask = df["comments"].str.contains("metro", case=False, na=False)
```

---

## 3. Khảo sát Toàn diện Cột Văn bản Lớn (Text Profiling)

Khi xử lý một tập dữ liệu văn bản quy mô hàng trăm nghìn dòng (chẳng hạn 690 nghìn đoạn đánh giá của Inside Airbnb), ta không thể đọc lướt bằng mắt thường. Ta cần thực hiện quy trình khảo sát thống kê:
1. **Đếm giá trị thiếu**: Xác định số dòng bị bỏ trống `comments.isna().sum()`.
2. **Đo độ dài ký tự**: Sử dụng `comments.dropna().str.len()`. Thống kê giá trị trung vị của độ dài giúp ta hình dung dung lượng trung bình của một phản hồi thực tế.
3. **Phát hiện nội dung rác ít thông tin**:
   Trong các tập dữ liệu người dùng phản hồi, luôn xuất hiện một tỷ lệ đáng kể các đoạn đánh giá "cụt" chỉ gồm $1$ hoặc $2$ ký tự, ví dụ:
   - Chỉ có một dấu chấm: `"."`
   - Chỉ có một ký tự xác nhận: `"Ok"`, `"K"`
   - Chuỗi rỗng: `""`
   Các đoạn văn bản này chiếm khoảng $8\% - 10\%$ tổng số dòng nhưng hoàn toàn không mang lại giá trị phân tích cảm xúc hay trích xuất thông tin. Việc gắn cờ và loại bỏ chúng bằng ngưỡng độ dài tối thiểu (chẳng hạn $\text{len} < 20$) là bước bắt buộc trước khi chuyển dữ liệu vào các mô hình học máy hay gửi tới API của các mô hình ngôn ngữ lớn (LLM).

---

## 4. Trích xuất Thực thể bằng `str.extract` và Nhóm bắt

Phương thức **`str.extract()`** nhận vào một mẫu Regex và trích xuất nội dung của **nhóm bắt nằm trong cặp dấu ngoặc đơn `(...)`**.

### 4.1. Nhóm Bắt `(...)` vs Nhóm Không Bắt `(?:...)`
Giả sử ta muốn trích xuất tên địa danh đứng sau các cụm từ chỉ vị trí như:
- Tiếng Tây Ban Nha: `"cerca de la "`, `"cerca del "`, `"cerca de "`
- Tiếng Anh: `"near the "`, `"near "`

Nếu ta viết `(cerca de |near )([A-Za-z]+)`, hàm `str.extract()` sẽ trả về một DataFrame gồm 2 cột tương ứng với 2 nhóm ngoặc đơn.
Để chỉ lấy duy nhất tên địa danh mà không trích xuất cụm từ dẫn đường, ta sử dụng **nhóm không bắt (*Non-capturing group*)** với cú pháp `(?:...)`:
```python
PAT_GAN = r"(?:cerca de la |cerca del |cerca de |near the |near )([A-Za-zÁ-Úá-úñÑ]+)"
```
Cặp ngoặc `(?:...)` đầu tiên chỉ dùng để gom nhóm các từ khóa tiền tố, trong khi cặp ngoặc `(...)` thứ hai là nhóm bắt duy nhất sẽ được trích xuất thành kết quả.

### 4.2. Bẫy Khớp nhầm (*False Positives*) và Danh sách Từ dừng
Biểu thức chính quy là một công cụ máy móc: Nó chỉ nhận diện cấu trúc bề mặt chứ hoàn toàn không hiểu ngữ nghĩa của từ.
Khi áp dụng mẫu `PAT_GAN` trên tập dữ liệu thực tế, ta thu được các kết quả có tần suất cao nhất:
1. `"metro"` (7,640 lần): Ga tàu điện ngầm $\to$ **Thực thể địa điểm hợp lệ**.
2. `"movistar"` (2,150 lần): Nhà thi đấu Movistar Arena $\to$ **Thực thể địa điểm hợp lệ**.
3. `"todo"` (4,820 lần): Xuất phát từ cụm từ `"cerca de todo"` nghĩa là "gần mọi thứ" $\to$ **Khớp nhầm!**
4. `"muchos"` (1,230 lần): Xuất phát từ cụm từ `"cerca de muchos restaurantes"` nghĩa là "gần nhiều..." $\to$ **Khớp nhầm!**

Nếu vội vã đưa kết quả này vào báo cáo, bạn sẽ đưa ra một kết luận nực cười rằng "địa điểm du khách hay ở gần nhất là Todo".
Quy trình chuẩn mực là kết hợp `str.extract` với bước lọc hậu kỳ: Sử dụng danh sách từ dừng (*Stopwords list*) để loại bỏ các đại từ và lượng từ bị khớp nhầm trước khi tổng hợp bảng tần suất.

---

## 5. Bài tập Thực chiến Phòng Lab 07 (100% Nội dung Lab) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 6. Tổng kết Bài học

1. **Khai thác triệt để `.str`**: Luôn sử dụng bộ định tuyến `.str` để thực thi các phép biến đổi chuỗi an toàn trên toàn bộ mảng dữ liệu.
2. **Kỷ luật `regex=False` và `na=False`**: Luôn tắt regex khi so khớp chuỗi ký tự thông thường và gán `na=False` để kiểm soát các giá trị khuyết thiếu trong `str.contains()`.
3. **Thẩm định dữ liệu chữ**: Sàng lọc các phản hồi quá ngắn và làm sạch thẻ HTML trước khi đưa vào các đường ống phân tích chuyên sâu.
4. **Cảnh giác trước Regex**: Biểu thức chính quy chỉ nhận diện hình thức cú pháp, không hiểu ngữ nghĩa. Luôn luôn kiểm định các trường hợp khớp nhầm và kết hợp danh sách từ dừng để làm sạch kết quả trích xuất.
