---
course: xu-ly-du-lieu
lecture: bai-02-python-co-ban
section: lecture
title: "Python cơ bản cho xử lý dữ liệu"
prerequisites: ["bien-kieu", "list", "dictionary", "vong-lap", "ham-lap-trinh"]
lessonStatus: ready
description: "Chọn cấu trúc dữ liệu, cơ chế tham chiếu bộ nhớ, phân biệt biến đổi với sàng lọc và đọc tệp chuẩn mực bằng Python thuần."
---

## 1. Cấu trúc Dữ liệu Quyết định Cơ chế Tra cứu và Hiệu năng Bộ nhớ

Trước khi vận hành các thư viện chuyên dụng như NumPy hay pandas, người kỹ sư dữ liệu bắt buộc phải làm chủ các cấu trúc dữ liệu bản địa của Python. Bản thân Python cung cấp một ngăn xếp cấu trúc dữ liệu rất linh hoạt, tuy nhiên mỗi cấu trúc lại mang một thiết kế bộ nhớ và chi phí tính toán hoàn toàn khác biệt. Nếu chọn sai cấu trúc cho một thao tác lặp lại thường xuyên trong đường ống xử lý hàng triệu bản ghi, thời gian thực thi có thể tăng từ vài giây lên tới nhiều giờ đồng hồ.

<DataDiagram name="python-collections" />

### 1.1. Bản chất bên dưới của Danh sách (`list`) và Dãy bất biến (`tuple`)
Trong ngôn ngữ C thực thi CPython, `list` thực chất là một mảng động chứa các con trỏ trỏ tới các đối tượng Python phân tán trong bộ nhớ heap.
- Khi truy cập phần tử theo chỉ số vị trí `ds[i]`, hệ thống chỉ cần một phép tính số học địa chỉ bộ nhớ: `địa_chỉ_gốc + i * kích_thước_con_trỏ`, do đó thao tác này luôn đạt độ phức tạp tức thì $O(1)$.
- Ngược lại, khi bạn thực hiện kiểm tra `if x in ds:`, CPython buộc phải duyệt tuần tự từ đầu đến cuối danh sách và so sánh từng con trỏ đối tượng. Nếu danh sách có $n$ bản ghi, thao tác này tiêu tốn thời gian $O(n)$. Nếu đặt phép kiểm tra này bên trong một vòng lặp duyệt $n$ phần tử khác, thuật toán sẽ bùng nổ độ phức tạp lên bậc hai $O(n^2)$.
- `tuple` có cơ chế bộ nhớ tương tự `list` nhưng sở hữu tính bất biến (*immutable*). Khi đã được khởi tạo, danh sách con trỏ bên trong `tuple` không thể thêm bớt hay tráo đổi. Đặc tính bất biến này cho phép CPython tối ưu hóa cấp phát bộ nhớ và cho phép `tuple` sinh mã băm (*hashable*), biến nó thành cấu trúc lý tưởng để làm khóa phức hợp nhiều trường (*composite key*) trong các bài toán gom nhóm dữ liệu.

### 1.2. Bảng băm (`dict` và `set`): Vũ khí gia tốc tra cứu
`dict` và `set` được cài đặt dựa trên cấu trúc bảng băm (*hash table*) được tối ưu hóa cao độ của CPython.
- Để một đối tượng có thể đưa vào `set` hoặc làm khóa của `dict`, đối tượng đó bắt buộc phải bất biến (như chuỗi, số thực, số nguyên, hoặc tuple chứa các phần tử bất biến) để giá trị băm `hash(obj)` không đổi theo thời gian.
- Khi kiểm tra `if khoa in tu_dien:` hoặc `if phan_tu in tap_hop:`, Python tính toán mã băm của đối tượng, ánh xạ trực tiếp tới vị trí ô nhớ trong bảng băm. Độ phức tạp trung bình của phép tra cứu này là $O(1)$, hoàn toàn độc lập với kích thước dữ liệu.
- Phép toán đại số tập hợp giữa hai `set`:
  ```python
  thang_3 = {"HN01", "HN02", "HN03", "HN04"}
  thang_6 = {"HN02", "HN04", "HN05"}
  
  # Tìm các mã phòng biến mất và các mã phòng mới xuất hiện
  bien_mat = thang_3 - thang_6  # {'HN01', 'HN03'}
  moi_them = thang_6 - thang_3  # {'HN05'}
  ```
  Phép trừ tập hợp đạt độ phức tạp $O(\text{len}(thang\_3))$, nhanh hơn vượt trội so với việc viết vòng lặp lồng nhau duyệt qua danh sách thông thường.

### 1.3. Mã định danh không phải là con số
Một sai lầm kinh điển của người mới bước vào ngành dữ liệu là tự động ép kiểu mọi chuỗi ký tự chứa các chữ số sang dạng số nguyên `int()`.
Xét mã bưu chính, mã căn cước công dân hoặc mã sản phẩm: `"00123"`. Nếu bạn ép kiểu thành `int("00123")`, giá trị sẽ biến thành `123` và toàn bộ các số $0$ ở đầu (*leading zeros*) sẽ bị triệt tiêu vĩnh viễn. Trong kỹ thuật dữ liệu, nguyên tắc vàng được phát biểu như sau:
> **Nguyên tắc định danh**: Chỉ chuyển đổi sang kiểu số đối với những trường dữ liệu mà ta có nhu cầu thực hiện các phép toán số học (cộng, trừ, nhân, chia, tính trung bình). Mọi mã số định danh, số điện thoại, mã giao dịch hay số phòng đều phải được bảo toàn nghiêm ngặt dưới dạng chuỗi (`str`).

---

## 2. Cơ chế Tham chiếu Vùng nhớ và Đột biến Dữ liệu Ngầm

Python vận hành theo mô hình quản lý bộ nhớ hướng đối tượng thông qua cơ chế gắn nhãn tham chiếu (*name-binding*). Việc không thấu suốt mô hình này là nguyên nhân hàng đầu dẫn tới các lỗi sai logic rất khó phát hiện.

### 2.1. Phép gán chưa bao giờ tạo ra bản sao
Khi bạn viết `b = a`, Python không hề sao chép các phần tử trong danh sách `a` sang một vùng nhớ mới. Lệnh này chỉ đơn thuần tạo thêm một cái tên mới `b` cùng trỏ vào đúng đối tượng mà `a` đang trỏ tới:

```python
a = [100, 200, 300]
b = a
b.append(400)

print(a)  # [100, 200, 300, 400] -> a bị biến đổi ngoài tầm kiểm soát!
```

### 2.2. Phân biệt Sao chép nông (*Shallow Copy*) và Sao chép sâu (*Deep Copy*)
Khi cần độc lập dữ liệu, ta thường dùng phương thức `.copy()` hoặc lát cắt `a[:]`. Tuy nhiên, đây mới chỉ là **sao chép nông**:

```python
import copy

# Danh sách chứa các từ điển bản ghi
du_lieu_goc = [{"id": "P01", "gia": 100}, {"id": "P02", "gia": 200}]

# 1. Sao chép nông
ban_sao_nong = du_lieu_goc.copy()
ban_sao_nong[0]["gia"] = 999
print(du_lieu_goc[0]["gia"])  # 999 -> Dữ liệu gốc vẫn bị sửa đổi ngầm!

# 2. Sao chép sâu độc lập hoàn toàn
du_lieu_chuan = copy.deepcopy(du_lieu_goc)
du_lieu_chuan[0]["gia"] = 500
print(du_lieu_goc[0]["gia"])  # 999 -> Dữ liệu gốc được bảo vệ an toàn
```

Bản sao nông chỉ tạo ra một danh sách mới chứa cùng các con trỏ trỏ tới các từ điển con bên trong. Để bảo đảm tính độc lập dữ liệu tuyệt đối khi thao tác với các cấu trúc lồng nhau (như danh sách các từ điển đọc từ CSV hay JSON), ta bắt buộc phải sử dụng `copy.deepcopy()` hoặc tạo mới từ điển con bằng phép tái cấu trúc `{**ban_ghi}`.

---

## 3. Phân định Rạch ròi giữa Biến đổi và Sàng lọc

Trong đường ống xử lý dữ liệu chuẩn mực, hai thao tác toán học sau đây không bao giờ được nhập nhằng:
1. **Biến đổi (Transformation / Mapping)**: Nhận một giá trị thô và chuyển hóa sang một biểu diễn chuẩn hóa tương ứng ($f: X \to Y$). Số lượng phần tử đầu vào và đầu ra là tương đương $1:1$.
2. **Sàng lọc (Filtering)**: Nhận một tập hợp các giá trị và giữ lại một tập con thỏa mãn điều kiện vị từ ($P: Y \to \{\text{True}, \text{False}\}$).

### 3.1. Bẫy chân trị (*Truthy vs Falsy*) với giá trị số 0
Trong ngôn ngữ Python, các giá trị sau đây khi đưa vào cấu trúc điều kiện `if` sẽ tự động bị đánh giá là sai (`False`):
- `None`
- `0`, `0.0`
- Chuỗi rỗng `""`
- Danh sách rỗng `[]`, từ điển rỗng `{}`

Hãy quan sát một đoạn mã nghiệp dư thường gặp:
```python
# CÁCH LÀM SAI LẦM NGUY HIỂM:
gia_hop_le = [g for g in danh_sach_gia if g]
```
Nếu trong dữ liệu có một phòng trọ được quảng bá với giá khuyến mãi bằng $0$ đồng (`0` hoặc `0.0`), đoạn mã trên sẽ coi `0` là `False` và loại bỏ nó không thương tiếc! Khi đó:
- Số lượng phòng hợp lệ bị đếm thiếu.
- Giá trị trung bình của thị trường bị thổi phồng một cách giả tạo.
- Phòng $0$ đồng bị đánh đồng với phòng bị mất thông tin giá (`None`).

Một cách người ta hay dùng để kiểm soát chính xác là sử dụng toán tử kiểm tra danh tính đối tượng:
```python
# CÁCH LÀM CHUẨN MỰC KỸ THUẬT:
gia_hop_le = [g for g in danh_sach_gia if g is not None]
```

### 3.2. Ép kiểu an toàn bằng khối `try / except` phòng thủ
Khi đọc dữ liệu văn bản từ tệp, ta không thể lường trước người dùng nhập vào những chuỗi ký tự quái dị nào (`"N/A"`, `"chưa_rõ"`, chuỗi rỗng `""`, hoặc các giá trị hỏng hóc). Ta đóng gói logic chuyển đổi vào một hàm phòng thủ:

```python
def to_float(value: any) -> float | None:
    """Chuyển đổi an toàn giá trị sang số thực float.
    
    Bảo toàn số 0.0; trả về None đối với chuỗi rỗng, None hoặc chuỗi không đọc được số.
    Bắt đích danh ngoại lệ (ValueError, TypeError), không che giấu lỗi hệ thống.
    """
    if value is None:
        return None
    try:
        return float(value)
    except (ValueError, TypeError):
        return None
```

Hàm trên tuân thủ nghiêm ngặt nguyên tắc xử lý ngoại lệ: Chỉ bắt đích danh `(ValueError, TypeError)`. Tuyệt đối không bao giờ dùng `except: pass` cộc lốc vì cú pháp đó sẽ nuốt chửng cả những lỗi lập trình nghiêm trọng như gọi sai tên biến (`NameError`) hay tràn bộ nhớ (`MemoryError`).

---

## 4. Kỹ thuật Đọc & Ghi Tệp CSV, JSON Chuẩn mực

### 4.1. Đọc tệp CSV dạng từ điển với `csv.DictReader`
Mô-đun `csv` của thư viện chuẩn cung cấp lớp `csv.DictReader`. Thay vì trả về một danh sách các phần tử theo chỉ mục số nguyên dễ gây nhầm lẫn, `DictReader` tự động lấy dòng đầu tiên làm tiêu đề cột và ánh xạ mỗi dòng dữ liệu tiếp theo thành một từ điển có khóa là tên cột:

```python
import csv

def doc_danh_sach(duong_dan: str) -> list[dict]:
    with open(duong_dan, mode="r", encoding="utf-8", newline="") as tep:
        doc = csv.DictReader(tep)
        return list(doc)
```

Hai chi tiết kỹ thuật cốt lõi cần ghi nhớ:
- **Luôn chỉ định `encoding="utf-8"`**: Trên hệ điều hành Windows, mã hóa mặc định có thể là `cp1252` hoặc `cp930`, dẫn đến việc lỗi sập chương trình khi gặp ký tự tiếng Việt hoặc các ngôn ngữ có dấu.
- **Sử dụng `newline=""`**: Ngăn chặn Python tự ý diễn dịch sai các ký tự ngắt dòng (`\r\n` vs `\n`) lồng bên trong các trường văn bản CSV.

### 4.2. Xuất báo cáo JSON bảo toàn ký tự quốc tế
Khi tuần tự hóa (*serialize*) dữ liệu ra tệp JSON, mặc định `json.dump()` sẽ chuyển toàn bộ các ký tự Unicode không phải mã ASCII thành các chuỗi thoát hiểm dạng `\u00f1`. Để tệp JSON dễ đọc và bảo toàn nguyên vẹn tiếng Việt cùng các ký tự quốc tế, ta luôn thiết lập `ensure_ascii=False`:

```python
import json

def luu_bao_cao(du_lieu: dict, duong_dan: str) -> None:
    with open(duong_dan, mode="w", encoding="utf-8") as tep:
        json.dump(du_lieu, tep, ensure_ascii=False, indent=2)
```

---

## 5. Thống kê Mô tả: Trung bình Cộng vs Trung vị

Xét một mẫu số liệu giá gồm $n$ quan sát: $x_1, x_2, \dots, x_n$.
- **Giá trị trung bình cộng (*Mean*)**:
  $$\bar{x} = \frac{1}{n}\sum_{i=1}^n x_i$$
- **Giá trị trung vị (*Median*)**: Là giá trị nằm ở vị trí chính giữa khi mẫu số liệu đã được sắp xếp tăng dần:
  $$\operatorname{Median} = \begin{cases} 
  x_{((n+1)/2)} & \text{khi } n \text{ lẻ} \\
  \frac{x_{(n/2)} + x_{(n/2 + 1)}}{2} & \text{khi } n \text{ chẵn}
  \end{cases}$$

### Bản chất sư phạm: Sức đề kháng trước ngoại lai (*Robustness*)
Trong kinh tế học và phân tích dữ liệu thị trường thực tế (như giá bất động sản, tiền lương, lưu lượng truy cập), phân phối dữ liệu hầu như không bao giờ có dạng chuẩn đối xứng mà luôn **lệch phải (*right-skewed*)** với chiếc đuôi rất dài gồm một số ít căn hộ siêu sang có giá hàng triệu USD.
- Trung bình cộng rất nhạy cảm với ngoại lai: Chỉ cần xuất hiện một căn biệt thự giá 10 tỷ đồng, mức giá trung bình của toàn khu phố sẽ bị kéo vọt lên, tạo cảm giác sai lệch về mức sống thực tế của cư dân.
- Trung vị là một thống kê có **sức chịu tải vững (*robust statistic*)**: Mức giá căn biệt thự dù có tăng từ 10 tỷ lên 100 tỷ thì giá trị đứng giữa danh sách sắp xếp vẫn không hề thay đổi. Do đó, trong các báo cáo thị trường chuyên nghiệp, trung vị luôn là thước đo trung tâm được ưu tiên hàng đầu.

---

## 6. Bài tập Thực chiến Phòng Lab 02 (100% Nội dung Lab) {#bai-tap}

Toàn bộ hệ thống bài tập thực hành chuyên sâu và phòng Lab thực chiến của bài học này đã được tích hợp đầy đủ tại tab **Bài tập** ở đầu trang. Sau khi đọc xong phần lý thuyết, bạn hãy bấm chuyển sang tab [**Bài tập**](#bai-tap) để bắt đầu thực hành trên dữ liệu thực tế.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để mở phòng Lab tương tác với 2 hướng tiếp cận (Cơ bản & Nâng cao), phân tích giả thuyết và bộ kiểm chứng tự động `assert`.
:::

## 7. Tổng kết và Bài học Kinh nghiệm

1. **Cấu trúc dữ liệu định hình thuật toán**: Sử dụng `list` khi cần bảo toàn thứ tự, dùng `set` khi cần trừ tập hợp và kiểm tra thành viên $O(1)$, dùng `dict` để quản lý các trường bản ghi, và dùng `tuple` khi cần khóa phức hợp bất biến.
2. **Cảnh giác trước phép gán**: Phép gán trong Python chỉ liên kết tên biến với vùng nhớ có sẵn. Luôn dùng `copy.deepcopy()` hoặc tái cấu trúc bản ghi khi cần chỉnh sửa dữ liệu mà không làm biến dạng tập dữ liệu thô ban đầu.
3. **Kỷ luật với giá trị 0**: Tuyệt đối không kiểm tra hợp lệ bằng `if price:`. Luôn sử dụng `if price is not None:` để bảo vệ các giá trị số $0$ hợp lệ.
4. **Vững chãi trước ngoại lai**: Trong các phân phối dữ liệu kinh tế lệch phải, giá trị trung vị (*Median*) là chỉ số trung tâm đáng tin cậy hơn nhiều so với trung bình cộng (*Mean*).
5. **Giữ gìn dấu vết kiểm toán**: Không tự ý xóa bỏ các dòng dữ liệu xung đột logic mà hãy đưa chúng vào báo cáo kiểm định chất lượng (QA) để truy xuất nguồn gốc lỗi của hệ thống.
