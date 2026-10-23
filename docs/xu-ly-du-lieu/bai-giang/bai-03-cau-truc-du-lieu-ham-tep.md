---
course: xu-ly-du-lieu
lecture: bai-03-cau-truc-du-lieu-ham-tep
section: lecture
title: "Cấu trúc dữ liệu, hàm và tệp"
prerequisites: ["bien-kieu", "vong-lap"]
lessonStatus: ready
hasChapterExercises: true
description: "Cấu trúc dữ liệu Python bản địa, hàm bậc cao, hàm sinh generator, xử lý ngoại lệ và thao tác tệp an toàn trong đường ống dữ liệu."
---


<div class="lecture-notes-content">

## 1. Cấu trúc dữ liệu và dãy trong Python

Bạn nhận một tệp nhật ký bán hàng gồm nhiều dòng dạng `ma_san_pham,so_tien`. Một số dòng ghi thiếu số tiền, một số dòng chứa ký tự lạ. Bạn cần đọc từng dòng, làm sạch khoảng trắng, phân nhóm theo sản phẩm và tính tổng tiền mà không để một dòng lỗi làm dừng toàn bộ chương trình.

Trước khi vận hành các thư viện phân tích bảng như pandas, người kỹ sư dữ liệu cần làm chủ các cấu trúc dữ liệu bản địa của Python. Việc chọn đúng cấu trúc cho từng thao tác giúp đường ống dữ liệu vận hành ổn định và tiết kiệm tài nguyên.

### 1.1. Bộ bất biến (Tuple)
`tuple` là một dãy cố định các phần tử có thứ tự và mang tính **bất biến** (*immutable*). Khi đã được khởi tạo, chuỗi tham chiếu bên trong `tuple` không thể thêm bớt hay thay thế.

Tuy nhiên, nếu một phần tử bên trong `tuple` là một đối tượng khả biến (chẳng hạn một danh sách `list`), nội dung của danh sách con đó vẫn có thể bị thay đổi tại chỗ:
```python
tup_long = (1, 2, [3, 4])
tup_long[2].append(5)
print(tup_long)  # (1, 2, [3, 4, 5])
```
Bản thân tuple vẫn lưu giữ các tham chiếu ban đầu, nhưng trạng thái bên trong của đối tượng danh sách con đã biến đổi.

```python
tup = (4, 5, 6)
tup_chuoi = tuple("Python")  # ('P', 'y', 't', 'h', 'o', 'n')
```

#### Phép giải nén Tuple (Unpacking)
Python cho phép gán đồng thời các phần tử của tuple vào các biến độc lập:
```python
a, b, c = tup  # a=4, b=5, c=6

# Tráo đổi giá trị hai biến mà không cần biến trung gian
a, b = b, a
```

Kỹ thuật bắt phần tử thừa với toán tử dấu sao `*rest` cho phép tách phần tử đầu và giữ lại phần còn lại dưới dạng danh sách:
```python
day_so = (1, 2, 3, 4, 5, 6)
dau, *giua, cuoi = day_so
print(dau)   # 1
print(giua)  # [2, 3, 4, 5]
print(cuoi)  # 6
```

Phương thức chính của tuple gồm `tup.count(gia_tri)` (đếm số lần xuất hiện) và `tup.index(gia_tri)` (tìm vị trí đầu tiên).

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-1 -->

::: example Giải nén phần tử đầu cuối với toán tử sao

Các bản ghi giao dịch xuất từ tệp nhật ký thường chứa trường định danh ở đầu, một chuỗi các chỉ số phụ ở giữa và mã trạng thái ở cuối dòng. Độ dài của các chỉ số ở giữa có thể thay đổi tùy thuộc vào số lượng mặt hàng trong đơn. Ta sử dụng cú pháp giải nén với toán tử dấu sao để bóc tách các trường này mà không cần đo kích thước thủ công.

```python
ban_ghi = [
    ("DH01", 120, 150, "HOAN_THANH"),
    ("DH02", 90, 110, 85, 200, "HOAN_THANH"),
    ("DH03", "HUY"),
]

for muc in ban_ghi:
    ma, *chi_so, trang_thai = muc
    tong_tien = sum(chi_so)
    print(f"Mã: {ma:<5} | Số món: {len(chi_so)} | "
          f"Tổng: {tong_tien:>4} | Trạng thái: {trang_thai}")
```

Kết quả khi chạy đoạn mã trên:

```text
Mã: DH01  | Số món: 2 | Tổng:  270 | Trạng thái: HOAN_THANH
Mã: DH02  | Số món: 4 | Tổng:  485 | Trạng thái: HOAN_THANH
Mã: DH03  | Số món: 0 | Tổng:    0 | Trạng thái: HUY
```

Cú pháp giải nén tuple mở rộng `ma, *chi_so, trang_thai = muc` phân bổ phần tử đầu tiên cho biến `ma` và phần tử cuối cùng cho biến `trang_thai`. Toàn bộ các phần tử nằm ở giữa được Python tự động thu gom vào biến `chi_so` dưới dạng một danh sách mới.

Trong bản ghi `DH01`, biến `chi_so` nhận danh sách gồm hai giá trị `[120, 150]`. Ở bản ghi `DH02`, danh sách nhận bốn giá trị `[90, 110, 85, 200]`. Nếu bản ghi có đúng hai phần tử, biến `chi_so` sẽ nhận danh sách rỗng `[]`.

Mẫu `ma, *chi_so, trang_thai` cần ít nhất hai phần tử. Cả ba bản ghi đều thỏa điều kiện đó, kể cả `DH03` chỉ có mã và trạng thái. Nếu nhận dữ liệu từ nguồn chưa kiểm soát, cần kiểm tra số phần tử trước khi giải nén.

`sum([])` cho 0 nên đơn `DH03` có số món và tổng tiền đều bằng 0. Dấu sao thu phần giữa thành một danh sách, dù phần giữa có không, hai hay bốn phần tử. Nhờ đó, cùng một vòng lặp xử lý được các bản ghi có số món khác nhau.

:::

<!-- /worked-example -->

### 1.2. Danh sách (List)
Khác với tuple, `list` là cấu trúc mảng động có kích thước biến thiên và nội dung **khả biến** (*mutable*).

#### Thao tác thêm, bớt và chi phí thời gian
- `ds.append(x)`: Thêm phần tử vào cuối danh sách. Thao tác này đạt độ phức tạp khấu hao $O(1)$.
- `ds.insert(vi_tri, x)`: Chèn phần tử vào một vị trí chỉ định. Nếu chèn ở đầu danh sách (`vi_tri = 0`), CPython buộc phải dịch chuyển toàn bộ $n$ phần tử về phía sau, tiêu tốn thời gian $O(n)$.
- `ds.pop(vi_tri)`: Lấy ra và xóa phần tử. `ds.pop()` ở cuối danh sách đạt $O(1)$, nhưng `ds.pop(0)` ở đầu danh sách tốn $O(n)$.
- `ds.remove(gia_tri)`: Tìm và xóa phần tử đầu tiên khớp giá trị, tốn $O(n)$.
- Kiểm tra thành viên `if x in ds:` duyệt tuần tự qua danh sách, đạt độ phức tạp $O(n)$.

#### Nối danh sách: Toán tử `+` so với phương thức `.extend()`
Khi cần kết hợp hai danh sách:
- Toán tử `ds1 + ds2` cấp phát một danh sách mới trong RAM và sao chép các tham chiếu phần tử của cả hai danh sách vào đó (sao chép nông tham chiếu, không sao chép sâu các đối tượng).
- Phương thức `ds1.extend(ds2)` thay đổi trực tiếp danh sách `ds1` tại chỗ bằng cách gắn thêm các tham chiếu phần tử từ `ds2`. Thao tác này tránh việc cấp phát danh sách vỏ ngoài mới khi muốn tích lũy dữ liệu vào một danh sách sẵn có.

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-2 -->

::: example Phân biệt tạo danh sách mới bằng toán tử cộng và biến đổi tại chỗ bằng extend

Trong các vòng lặp thu thập dữ liệu theo lô, việc lựa chọn cách nối danh sách quyết định tốc độ thực thi và lượng RAM bị chiếm dụng. Toán tử cộng tạo ra một đối tượng danh sách mới trong khi phương thức extend nối trực tiếp vào danh sách hiện tại. Ta kiểm tra định danh đối tượng và quan sát biến bí danh để hiểu rõ sự khác biệt giữa hai cách viết.

```python
ds_cong = [10, 20]
id_cong_truoc = id(ds_cong)
ds_cong = ds_cong + [30, 40]
id_cong_sau = id(ds_cong)

ds_ext = [10, 20]
id_ext_truoc = id(ds_ext)
bi_danh_ext = ds_ext
ds_ext.extend([30, 40])
id_ext_sau = id(ds_ext)

print(f"Toán tử + tạo đối tượng mới:             {id_cong_truoc != id_cong_sau}")
print(f"Phương thức extend giữ nguyên đối tượng: {id_ext_truoc == id_ext_sau}")
print(f"Biến bí danh cùng phản ánh dữ liệu mới:  {bi_danh_ext == [10, 20, 30, 40]}")
```

Kết quả khi chạy đoạn mã trên:

```text
Toán tử + tạo đối tượng mới:             True
Phương thức extend giữ nguyên đối tượng: True
Biến bí danh cùng phản ánh dữ liệu mới:  True
```

Đoạn mã khởi tạo hai danh sách có nội dung ban đầu giống nhau `[10, 20]` và lưu lại định danh `id` trước khi thực hiện thao tác nối. Hàm `id` trả về định danh duy nhất của đối tượng thùng chứa danh sách trong phiên làm việc hiện tại.

Khi thực hiện phép toán `ds_cong + [30, 40]`, trình thông dịch cấp phát một đối tượng danh sách hoàn toàn mới trên bộ nhớ heap và sao chép các con trỏ phần tử sang đó. Định danh sau khi gán lại `id_cong_sau` khác biệt với `id_cong_truoc`, xác nhận một đối tượng mới đã được tạo ra.

Ngược lại, phương thức `extend` thay đổi trực tiếp danh sách hiện tại tại chỗ. Định danh `id_ext_sau` hoàn toàn trùng khớp với `id_ext_truoc`, và biến bí danh `bi_danh_ext` cùng trỏ tới danh sách này cũng nhìn thấy ngay các phần tử mới được thêm vào.

Cần hiểu rõ rằng `id()` chỉ phản ánh định danh của đối tượng thùng chứa danh sách, chứ không chứng minh sự ổn định của vùng đệm con trỏ bên trong. Khi vượt quá dung lượng đệm dự phòng của danh sách, phương thức `extend` vẫn có thể phải cấp phát lại vùng đệm C bên dưới để chứa thêm các phần tử mới.

:::

<!-- /worked-example -->

#### Sắp xếp danh sách
- `ds.sort()`: Sắp xếp danh sách tại chỗ (*in-place*), làm biến đổi danh sách gốc và trả về `None`.
- `sorted(ds)`: Giữ nguyên danh sách gốc và trả về một danh sách mới đã được sắp xếp.
- Tham số `key`: Tiếp nhận một hàm chỉ định tiêu chí sắp xếp:
  ```python
  danh_sach_tu = ["trung_binh", "gia", "du_lieu_lon", "bang"]
  danh_sach_tu.sort(key=len)  # Sắp xếp tăng dần theo độ dài từ
  print(danh_sach_tu)  # ['gia', 'bang', 'trung_binh', 'du_lieu_lon']
  ```

#### Cắt lát danh sách (Slicing)
Cú pháp lát cắt `ds[start:stop:step]` cho phép trích xuất một đoạn danh sách. `stop` không được bao gồm trong kết quả. Bước nhảy `step` có thể mang giá trị âm để đảo ngược danh sách: `ds[::-1]`. Gán giá trị vào lát cắt `ds[1:3] = [88, 99]` sẽ thay thế trực tiếp đoạn phần tử đó.

### 1.3. Từ điển (Dictionary)
`dict` là cấu trúc bảng băm (*hash table*) lưu trữ các cặp khóa - giá trị (*key - value*).

#### Tạo từ điển từ hai chuỗi song song
Hàm `zip` kết hợp hai tập hợp thành các cặp, sau đó truyền vào hàm khởi tạo `dict`:
```python
cot = ["ma", "gia", "so_luong"]
du_lieu = ["P01", 150000, 4]
ban_ghi = dict(zip(cot, du_lieu))
# {'ma': 'P01', 'gia': 150000, 'so_luong': 4}
```

#### Quản lý giá trị mặc định
Khi truy cập một khóa không tồn tại bằng cú pháp `d[khoa]`, Python sẽ ném ngoại lệ `KeyError`. Để xử lý an toàn:
- `d.get(khoa, mac_dinh)`: Trả về giá trị mặc định nếu khóa không tồn tại mà không ném lỗi.
- `d.setdefault(khoa, mac_dinh)`: Nếu khóa chưa có, tự động gán giá trị mặc định vào từ điển và trả về giá trị đó.
- Lớp `collections.defaultdict`: Tự động khởi tạo giá trị khi truy cập một khóa mới:
  ```python
  from collections import defaultdict

  # Gom nhóm mã phòng theo khu vực
  phong_theo_khu = defaultdict(list)
  phong_theo_khu["Bắc"].append("HN01")
  phong_theo_khu["Bắc"].append("HN02")
  print(phong_theo_khu["Bắc"])  # ['HN01', 'HN02']
  ```

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-3 -->

::: example Gom nhóm dữ liệu với collections.defaultdict và dict.setdefault

Khi tổng hợp các đơn hàng theo từng khách hàng, việc truy xuất một mã khách hàng chưa từng xuất hiện sẽ dẫn tới lỗi KeyError nếu dùng từ điển thông thường. Cả hai công cụ `collections.defaultdict` và `dict.setdefault` đều cho phép tự động khởi tạo danh sách gom nhóm. Ta triển khai cả hai cách để so sánh cú pháp và đánh giá cơ chế khởi tạo giá trị mặc định.

```python
from collections import defaultdict

giao_dich = [
    ("KH01", "Áo thun", 150000),
    ("KH02", "Quần jean", 350000),
    ("KH01", "Mũ len", 80000),
    ("KH02", "Giày vải", 420000),
]

gom_defaultdict = defaultdict(list)
for ma_kh, san_pham, gia in giao_dich:
    gom_defaultdict[ma_kh].append({"sp": san_pham, "gia": gia})

gom_setdefault = {}
for ma_kh, san_pham, gia in giao_dich:
    gom_setdefault.setdefault(ma_kh, []).append({"sp": san_pham, "gia": gia})

print(f"Hai cách gom nhóm cho kết quả khớp nhau: {dict(gom_defaultdict) == gom_setdefault}")
for ma_kh, ds in sorted(gom_defaultdict.items()):
    tong = sum(item["gia"] for item in ds)
    print(f"Khách hàng {ma_kh}: {len(ds)} món, tổng tiền = {tong:,d} đ")
```

Kết quả khi chạy đoạn mã trên:

```text
Hai cách gom nhóm cho kết quả khớp nhau: True
Khách hàng KH01: 2 món, tổng tiền = 230,000 đ
Khách hàng KH02: 2 món, tổng tiền = 770,000 đ
```

Đối tượng `defaultdict(list)` nhận tham số là hàm tạo kiểu `list`. Khi truy cập vào một khóa chưa từng tồn tại trong từ điển, thay vì ném ngoại lệ `KeyError`, nó gọi hàm `list()` để tạo một danh sách rỗng gán vào khóa đó rồi trả về tham chiếu.

Phương thức `setdefault(ma_kh, [])` của từ điển chuẩn cũng thực hiện nhiệm vụ tương tự: Nếu khóa đã tồn tại thì trả về giá trị hiện có, còn nếu khóa chưa có thì gán giá trị mặc định vào từ điển rồi trả về giá trị đó.

Điểm khác biệt quan trọng nằm ở thời điểm khởi tạo: Biểu thức `[]` trong `setdefault(ma_kh, [])` luôn được lượng giá sớm ngay khi gọi hàm, tức là một danh sách rỗng mới luôn được tạo trong bộ nhớ ở mọi lượt lặp kể cả khi khóa đã tồn tại từ trước. Ngược lại, `defaultdict(list)` chỉ gọi hàm tạo `list()` một cách lười biếng khi gặp khóa bị thiếu.

Phép so sánh `dict(gom_defaultdict) == gom_setdefault` xác nhận hai phương pháp cho ra cấu trúc từ điển hoàn toàn đồng nhất. Việc lựa chọn tùy thuộc vào nhu cầu: Dùng `defaultdict` khi gom nhóm dữ liệu lớn để tránh tạo danh sách thừa, hoặc dùng `setdefault` khi muốn giữ mã nguồn trên cấu trúc từ điển Python chuẩn.

:::

<!-- /worked-example -->

#### Ràng buộc về kiểu khóa trong từ điển (Hashability)
Khóa của từ điển bắt buộc phải là đối tượng **có thể sinh mã băm** (*hashable*). Điều này đồng nghĩa với việc khóa phải là đối tượng bất biến (như chuỗi, số thực, số nguyên, hoặc tuple chứa toàn các phần tử bất biến).

Hàm `hash(obj)` tính toán mã băm nguyên của đối tượng. Một danh sách `[1, 2]` không thể dùng làm khóa vì nó có thể bị đột biến nội dung, làm thay đổi vị trí ô nhớ trong bảng băm:
```python
hash("HN01")  # Hợp lệ
hash((1, 2))  # Hợp lệ
```
```pycon
>>> hash([1, 2])
TypeError: unhashable type: 'list'
```

### 1.4. Tập hợp (Set)
`set` là tập hợp các phần tử không có thứ tự và không chứa phần tử trùng lặp. Mỗi phần tử trong tập hợp phải có tính chất sinh mã băm. Phép kiểm tra thành viên `if x in s:` trên tập hợp đạt độ phức tạp trung bình $O(1)$.

Các phép toán đại số tập hợp giữa hai tập `A` và `B`:
- **Phép hợp (Union)**: Biểu thức `A | B` hoặc `A.union(B)` lấy tất cả các phần tử thuộc ít nhất một trong hai tập hợp.
- **Phép giao (Intersection)**: Biểu thức `A & B` hoặc `A.intersection(B)` lấy các phần tử xuất hiện ở cả hai tập hợp.
- **Phép hiệu (Difference)**: Biểu thức `A - B` hoặc `A.difference(B)` lấy các phần tử thuộc `A` nhưng không thuộc `B`.
- **Phép hiệu đối xứng (Symmetric Difference)**: Biểu thức `A ^ B` lấy các phần tử thuộc `A` hoặc `B` nhưng không thuộc phần giao.

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-4 -->

::: example Đối soát người dùng hoạt động giữa hai kỳ bằng đại số tập hợp

Trong phân tích hành vi khách hàng, các bộ phận dữ liệu cần xác định nhóm người dùng mới xuất hiện, nhóm duy trì sử dụng liên tục và nhóm đã rời bỏ dịch vụ giữa hai kỳ báo cáo. Việc duyệt qua danh sách bằng vòng lặp thủ công sẽ chậm khi quy mô người dùng lớn. Các toán tử đại số tập hợp cung cấp giải pháp tra cứu với độ phức tạp trung bình hằng số.

```python
thang_1 = {"U01", "U02", "U03", "U04"}
thang_2 = {"U03", "U04", "U05", "U06"}

duy_tri = sorted(thang_1 & thang_2)
roi_bo = sorted(thang_1 - thang_2)
moi_den = sorted(thang_2 - thang_1)
thay_doi = sorted(thang_1 ^ thang_2)

print(f"Người dùng duy trì (&): {duy_tri}")
print(f"Người dùng rời bỏ (-):  {roi_bo}")
print(f"Người dùng mới đến (-): {moi_den}")
print(f"Nhóm có biến động (^):  {thay_doi}")
```

Kết quả khi chạy đoạn mã trên:

```text
Người dùng duy trì (&): ['U03', 'U04']
Người dùng rời bỏ (-):  ['U01', 'U02']
Người dùng mới đến (-): ['U05', 'U06']
Nhóm có biến động (^):  ['U01', 'U02', 'U05', 'U06']
```

Đoạn mã tiếp nhận hai tập hợp chứa mã người dùng hoạt động trong tháng một và tháng hai. Cấu trúc `set` tự động loại bỏ các phần tử trùng lặp và xây dựng bảng băm cho các chuỗi định danh.

Toán tử giao `&` trích xuất những mã người dùng xuất hiện đồng thời trong cả hai tháng, thể hiện nhóm khách hàng duy trì gồm `U03` và `U04`. Toán tử hiệu `-` giữa `thang_1` và `thang_2` bóc tách những khách hàng có ở tháng trước nhưng không còn ở tháng sau gồm `U01` và `U02`.

`thang_2 - thang_1` cho các mã chỉ hoạt động ở tháng hai, gồm `U05` và `U06`. Chúng chưa chắc là tài khoản mới đăng ký, vì có thể đã tồn tại nhưng không hoạt động trong tháng một. Hiệu đối xứng `^` gom các mã chỉ xuất hiện ở một trong hai tháng.

Tất cả các phép toán tập hợp trên đều đạt độ phức tạp thời gian trung bình tỷ lệ thuận với số phần tử. Sau khi tính toán, hàm `sorted()` chuyển đổi tập hợp thành danh sách có thứ tự để kết quả xuất ra ổn định và thuận tiện cho việc trình bày.

:::

<!-- /worked-example -->

### 1.5. Các hàm tuần tự tích hợp (Built-In Sequence Functions)
- `enumerate(iterable, start=0)`: Trả về từng cặp `(chi_so, gia_tri)`, giúp tránh việc phải khởi tạo và tăng biến đếm thủ công:
  ```python
  for i, ten in enumerate(["Hà Nội", "Đà Nẵng", "TP.HCM"]):
      print(f"{i}: {ten}")
  ```
- `sorted(iterable, key=..., reverse=...)`: Trả về danh sách mới được sắp xếp từ bất kỳ tập hợp khả lặp nào.
- `zip(*iterables)`: Ghép đôi các phần tử có cùng vị trí từ nhiều tập hợp. Chiều dài kết quả bằng chiều dài của tập hợp ngắn nhất.
- `reversed(sequence)`: Trả về một iterator duyệt ngược các phần tử của một dãy mà không cần nhân bản danh sách.

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-5 -->

::: example Ghép cặp danh sách song song và đánh số thứ tự với zip và enumerate

Khi tiếp nhận các cột dữ liệu rời rạc từ các tệp cảm biến khác nhau, ta cần ghép từng dòng tương ứng lại thành một bản ghi hoàn chỉnh và gắn số thứ tự dòng để ghi nhật ký. Việc quản lý chỉ số bằng một biến đếm thủ công ngoài vòng lặp rất dễ gây lỗi quên tăng bước nhảy. Sự kết hợp giữa `zip` và `enumerate` mang lại giải pháp duyệt song song an toàn và ngắn gọn.

```python
thoi_gian = ["08:00", "08:15", "08:30"]
nhiet_do = [24.5, 25.0, 24.8]
do_am = [65, 62, 60]

for stt, (tg, nd, da) in enumerate(zip(thoi_gian, nhiet_do, do_am), start=1):
    print(f"Dòng {stt}: lúc {tg}, nhiệt độ {nd}°C, độ ẩm {da}%")
```

Kết quả khi chạy đoạn mã trên:

```text
Dòng 1: lúc 08:00, nhiệt độ 24.5°C, độ ẩm 65%
Dòng 2: lúc 08:15, nhiệt độ 25.0°C, độ ẩm 62%
Dòng 3: lúc 08:30, nhiệt độ 24.8°C, độ ẩm 60%
```

Hàm `zip` tiếp nhận ba tập hợp khả lặp `thoi_gian`, `nhiet_do` và `do_am`, sau đó ghép các phần tử có cùng vị trí chỉ số thành từng bộ tuple gồm ba giá trị `(tg, nd, da)`. Quá trình ghép dừng lại ngay khi tập hợp ngắn nhất duyệt đến phần tử cuối cùng.

Hàm `enumerate` bọc lấy bộ lặp của `zip` và bổ sung thêm chỉ số thứ tự `stt` cho mỗi lượt lặp. Tham số `start=1` chỉ định biến đếm bắt đầu từ số một thay vì số không mặc định, phù hợp với quy ước đánh số dòng của các báo cáo.

Bên trong vòng lặp `for`, cú pháp giải nén tuple `stt, (tg, nd, da)` bóc tách đồng thời số thứ tự và các giá trị cảm biến một cách trực tiếp, loại bỏ nhu cầu truy cập bằng chỉ số mảng như `thoi_gian[i]`.

Kết quả in ra cho thấy dữ liệu được ghép cặp chuẩn xác giữa các mốc thời gian và chỉ số tương ứng. Đây là mẫu hình thuận tiện để chuyển đổi nhiều danh sách cột riêng lẻ thành dạng bản ghi theo dòng mà không cần tạo cấu trúc trung gian phức tạp.

:::

<!-- /worked-example -->

### 1.6. Cú pháp Comprehension
Comprehension cho phép biến đổi và lọc dữ liệu ngắn gọn, diễn đạt rõ ý đồ lập trình:
- **List comprehension**: `[f(x) for x in tap_hop if dieu_kien]`
- **Dict comprehension**: `{khoa(x): gia_tri(x) for x in tap_hop if dieu_kien}`
- **Set comprehension**: `{f(x) for x in tap_hop if dieu_kien}`

```python
# Lọc và viết hoa tên các tỉnh thành có độ dài lớn hơn 6 ký tự
tinh_thanh = ["Hà Nội", "Huế", "Quảng Ninh", "Hải Phòng"]
ket_qua = [t.upper() for t in tinh_thanh if len(t) > 6]
# ['QUẢNG NINH', 'HẢI PHÒNG']
```

Comprehension lồng nhau (*nested comprehensions*) cho phép làm phẳng danh sách hai chiều:
```python
ma_tran = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lam_phang = [x for hang in ma_tran for x in hang if x % 2 == 0]
# [2, 4, 6, 8]
```

---

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-6 -->

::: example Làm phẳng và lọc dữ liệu mảng hai chiều bằng list comprehension

Dữ liệu nhật ký máy chủ thường được nhóm theo từng đợt dưới dạng danh sách chứa nhiều danh sách con. Để phục vụ việc thống kê toàn cục, ta cần làm phẳng cấu trúc hai chiều này thành một mảng duy nhất, đồng thời loại bỏ các giao dịch có giá trị không hợp lệ. Cú pháp comprehension lồng nhau cho phép thực hiện đồng thời hai thao tác này trong một biểu thức duy nhất.

```python
cac_lo = [
    [{"id": "G01", "tien": 100}, {"id": "G02", "tien": -5}],
    [{"id": "G03", "tien": 250}, {"id": "G04", "tien": 0}],
    [{"id": "G05", "tien": 180}],
]

hop_le = [
    {"ma": item["id"], "so_tien": item["tien"]}
    for lo in cac_lo
    for item in lo
    if item["tien"] > 0
]

for g in hop_le:
    print(f"Giao dịch {g['ma']}: số tiền = {g['so_tien']}")
```

Kết quả khi chạy đoạn mã trên:

```text
Giao dịch G01: số tiền = 100
Giao dịch G03: số tiền = 250
Giao dịch G05: số tiền = 180
```

Biểu thức list comprehension lồng nhau chứa hai mệnh đề `for` liên tiếp: Mệnh đề `for lo in cac_lo` duyệt qua từng lô danh sách lớn, và mệnh đề `for item in lo` tiếp tục duyệt qua từng bản ghi bên trong lô đó.

Mệnh đề điều kiện `if item['tien'] > 0` được đặt ở cuối biểu thức đóng vai trò bộ lọc, chỉ giữ lại các giao dịch phát sinh giá trị dương và loại bỏ các bản ghi mang số tiền âm hoặc bằng không.

Thứ tự các mệnh đề `for` giống thứ tự của vòng lặp lồng nhau. Phải có `lo` trước khi duyệt `item` trong nó. Nếu đảo hai mệnh đề, `lo` chưa được tạo trong ví dụ độc lập này. Trong notebook còn giữ biến `lo` cũ, mã thậm chí có thể chạy nhưng đọc nhầm dữ liệu.

Kết quả in ra trả về ba bản ghi hợp lệ `G01`, `G03` và `G05` đã được làm phẳng hoàn toàn. So với cách viết hai vòng lặp `for` lồng nhau và gọi `append()` thủ công, comprehension vừa ngắn gọn vừa thể hiện rõ ràng luồng biến đổi dữ liệu.

:::

<!-- /worked-example -->

## 2. Hàm trong Python

Trong kỹ thuật dữ liệu, hàm là đơn vị cơ sở để đóng gói từng bước biến đổi độc lập trong đường ống xử lý.

### 2.1. Không gian tên và quy tắc tìm kiếm LEGB
Khi một biến được gọi trong hàm, Python tìm kiếm tên biến theo quy tắc thứ tự **LEGB**:
1. **L (Local)**: Không gian tên cục bộ bên trong hàm hiện tại.
2. **E (Enclosing)**: Không gian tên của các hàm bao bọc bên ngoài (trong trường hợp hàm lồng nhau).
3. **G (Global)**: Không gian tên toàn cục của tệp mô-đun hiện tại.
4. **B (Built-in)**: Không gian tên chứa các hàm và hằng số tích hợp sẵn của Python (như `len`, `sum`, `range`).

Mọi biến được gán giá trị bên trong hàm mặc định thuộc về phạm vi cục bộ `Local`. Muốn thay đổi giá trị của một biến toàn cục, lập trình viên phải sử dụng từ khóa `global` (tuy nhiên việc lạm dụng biến toàn cục làm mất tính độc lập của hàm và khó kiểm thử).

### 2.2. Trả về nhiều giá trị
Một hàm trong Python có thể trả về nhiều giá trị bằng cách ngăn cách chúng bằng dấu phẩy. Về mặt bản chất, Python đóng gói các giá trị đó thành một `tuple` duy nhất:
```python
def thong_ke_co_ban(ds):
    return min(ds), sum(ds) / len(ds), max(ds)

nho_nhat, trung_binh, lon_nhat = thong_ke_co_ban([10, 20, 30])
```

### 2.3. Hàm là đối tượng hạng nhất (First-Class Functions)
Trong Python, hàm là đối tượng hạng nhất: Hàm có thể được gán cho một biến, được lưu trong danh sách hoặc từ điển, và được truyền vào như đối số của một hàm khác.

Tính chất này cho phép xây dựng đường ống làm sạch dữ liệu linh hoạt:
```python
import re

def xoa_khoang_trang(s):
    return s.strip()

def loai_dau_cau(s):
    return re.sub(r"[!?.]", "", s)

def viet_hoa_dau_tu(s):
    return s.title()

duong_ong_lam_sach = [xoa_khoang_trang, loai_dau_cau, viet_hoa_dau_tu]

def ap_dung_duong_ong(van_ban, cac_ham):
    for f in cac_ham:
        van_ban = f(van_ban)
    return van_ban

chuoi_tho = "  hà NỘI! "
chuoi_sach = ap_dung_duong_ong(chuoi_tho, duong_ong_lam_sach)
print(chuoi_sach)  # 'Hà Nội'
```

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-7 -->

::: example Áp dụng chuỗi hàm chuẩn hóa văn bản tuần tự

Trong các hệ thống tiền xử lý văn bản, mỗi chuỗi dữ liệu thô phải trải qua nhiều bước chuẩn hóa như cắt khoảng trắng thừa, chuyển về chữ thường và thay thế từ viết tắt. Nếu viết lồng các phép gọi hàm vào nhau, mã nguồn sẽ trở nên rối rắm và khó bổ sung bước mới. Việc lưu trữ các hàm trong một danh sách cho phép ta áp dụng tuần tự từng bước xử lý một cách linh hoạt.

```python
def xoa_khoang_trang(chuoi):
    return chuoi.strip()

def viet_thuong(chuoi):
    return chuoi.lower()

def chuan_hoa_thanh_pho(chuoi):
    tu_dien = {"hn": "Hà Nội", "hcm": "TP.HCM", "dn": "Đà Nẵng"}
    return tu_dien.get(chuoi, chuoi)

duong_ong = [xoa_khoang_trang, viet_thuong, chuan_hoa_thanh_pho]

def thuc_thi_duong_ong(gia_tri_tho, cac_buoc):
    kq = gia_tri_tho
    for buoc in cac_buoc:
        kq = buoc(kq)
    return kq

du_lieu_vao = ["  HN ", " HCM  ", " dn", "hai phong"]
for item in du_lieu_vao:
    ket_qua = thuc_thi_duong_ong(item, duong_ong)
    print(f"{item!r:<14} -> {ket_qua!r}")
```

Kết quả khi chạy đoạn mã trên:

```text
'  HN '        -> 'Hà Nội'
' HCM  '       -> 'TP.HCM'
' dn'          -> 'Đà Nẵng'
'hai phong'    -> 'hai phong'
```

Trong Python, hàm là đối tượng hạng nhất nên ta có thể đưa tên các hàm `xoa_khoang_trang`, `viet_thuong`, `chuan_hoa_thanh_pho` vào danh sách `duong_ong` như những đối tượng thông thường mà không cần đặt cặp ngoặc tròn gọi hàm.

Hàm `thuc_thi_duong_ong` tiếp nhận giá trị văn bản ban đầu và danh sách các bước xử lý. Vòng lặp `for` duyệt qua từng hàm `buoc` và thực thi nó với cú pháp `buoc(kq)`, chuyển kết quả đầu ra của bước trước thành đầu vào của bước kế tiếp.

Thiết kế này tách rời logic của từng bước biến đổi với cơ chế điều phối đường ống. Khi cần bổ sung thêm bước lọc ký tự đặc biệt, lập trình viên chỉ cần viết một hàm độc lập và thêm vào danh sách mà không phải sửa đổi cấu trúc vòng lặp chính.

Kết quả in ra cho thấy các chuỗi thô chứa khoảng trắng và chữ viết tắt đều được chuẩn hóa về tên thành phố mong muốn. Đây là nguyên lý nền tảng để xây dựng các đường ống biến đổi dữ liệu có khả năng mở rộng cao.

:::

<!-- /worked-example -->

### 2.4. Hàm ẩn danh (Lambda Functions)
Hàm lambda là hàm không tên, được định nghĩa bằng một dòng biểu thức duy nhất:
```python
tinh_tong = lambda x, y: x + y
```
Hàm lambda thường được dùng khi cần truyền nhanh một hàm ngắn làm đối số cho các hàm như `sort` hoặc các phương thức ánh xạ của pandas. Tuy nhiên, nếu logic xử lý vượt quá một biểu thức đơn giản, hãy định nghĩa một hàm rõ ràng bằng từ khóa `def` để bảo đảm tính dễ đọc của mã nguồn.

### 2.5. Hàm sinh (Generators) và Thư viện `itertools`
Khi xử lý tệp dữ liệu dung lượng lớn (chẳng hạn vài chục gigabyte), việc nạp toàn bộ dữ liệu vào một danh sách sẽ làm cạn kiệt bộ nhớ RAM. Hàm sinh (*generator*) giải quyết triệt để vấn đề này bằng cơ chế **đánh giá lười biếng** (*lazy evaluation*): Phần tử chỉ được tính toán và sinh ra khi có yêu cầu.

#### Hàm sinh với từ khóa `yield`
Khi một hàm chứa từ khóa `yield`, nó trở thành một hàm sinh. Mỗi khi gặp `yield`, hàm tạm dừng thực thi, trả về giá trị hiện tại cho môi trường gọi và bảo lưu toàn bộ trạng thái cục bộ để sẵn sàng chạy tiếp ở lượt yêu cầu tiếp theo:
```python
def tao_day_binh_phuong(n):
    for i in range(n):
        yield i ** 2

gen = tao_day_binh_phuong(5)
for v in gen:
    print(v, end=" ")
# 0 1 4 9 16
```

#### Biểu thức sinh (Generator Expression)
Cú pháp tương tự list comprehension nhưng đặt trong cặp ngoặc đơn `()`:
```python
tong_binh_phuong = sum(x ** 2 for x in range(1000000))
```
Biểu thức trên không tạo ra một danh sách một triệu phần tử trong RAM mà truyền từng số một vào hàm `sum()`.

#### Thư viện `itertools`
Mô-đun `itertools` cung cấp nhiều công cụ lặp hiệu năng cao:
- `itertools.chain(*iterables)`: Nối liên tiếp nhiều tập hợp mà không nhân bản dữ liệu.
- `itertools.groupby(iterable, key)`: Gom nhóm các phần tử liên tiếp có cùng giá trị khóa (yêu cầu dữ liệu phải được sắp xếp theo khóa trước khi gom nhóm).

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-8 -->

::: example Gom nhóm và tính tổng dữ liệu đã sắp xếp với itertools.groupby

Hàm `itertools.groupby` cho phép phân nhóm các bản ghi liên tiếp có cùng giá trị khóa mà không cần cấp phát thêm bộ nhớ từ điển phụ. Tuy nhiên, nếu dữ liệu chưa được sắp xếp trước theo khóa phân nhóm, `groupby` sẽ tách một nhóm thành nhiều nhóm nhỏ rời rạc mỗi khi khóa thay đổi. Ta kết hợp `sorted` và `groupby` để thực hiện phép tổng hợp doanh thu theo từng kho hàng.

```python
import itertools
import operator

don_hang = [
    {"kho": "K01", "tien": 150},
    {"kho": "K02", "tien": 200},
    {"kho": "K01", "tien": 350},
    {"kho": "K02", "tien": 100},
    {"kho": "K01", "tien": 120},
]

lay_kho = operator.itemgetter("kho")
don_da_sap = sorted(don_hang, key=lay_kho)

for ma_kho, nhom in itertools.groupby(don_da_sap, key=lay_kho):
    danh_sach_don = list(nhom)
    tong_tien = sum(item["tien"] for item in danh_sach_don)
    print(f"Kho {ma_kho}: {len(danh_sach_don)} đơn, tổng tiền = {tong_tien}")
```

Kết quả khi chạy đoạn mã trên:

```text
Kho K01: 3 đơn, tổng tiền = 620
Kho K02: 2 đơn, tổng tiền = 300
```

`operator.itemgetter("kho")` tạo hàm lấy trường `kho` của mỗi từ điển. `itertools.groupby` chỉ gom các khóa bằng nhau đang nằm liên tiếp. Để có đúng một nhóm cho mỗi kho, ta sắp danh sách theo chính hàm lấy khóa này trước khi gom.

Hàm `itertools.groupby` duyệt qua danh sách đã sắp xếp và sinh ra từng cặp `(ma_kho, nhom)`. Biến `nhom` là một bộ lặp, chỉ cung cấp các bản ghi thuộc nhóm hiện tại cho đến khi gặp một giá trị khóa mới trong chuỗi tuần tự.

Vì `nhom` là một bộ lặp chỉ duyệt được một lần, ta chuyển nó thành `list(nhom)` để vừa tính được số lượng đơn bằng `len()`, vừa tính được tổng tiền bằng `sum()`. Nếu không lưu thành danh sách, việc gọi `sum()` trước sẽ làm cạn bộ lặp và khiến các phép tính sau không còn dữ liệu.

Kho `K01` có 3 đơn, tổng 620, còn `K02` có 2 đơn, tổng 300. Nếu dữ liệu đã được sắp hoặc đã gom liền theo khóa thì không cần sắp lại. Nếu muốn giữ các đoạn liên tiếp như từng lượt vận hành, có thể chủ ý dùng `groupby` mà không sắp.

:::

<!-- /worked-example -->

### 2.6. Bắt và Xử lý Ngoại lệ (Exception Handling)
Trong phân tích dữ liệu, việc gặp phải các ô dữ liệu rác, chuỗi ký tự sai định dạng là điều tất yếu. Nếu không bắt ngoại lệ, chương trình sẽ lập tức sập và làm gián đoạn toàn bộ đường ống:

```python
def chuyen_sang_so_thuc(gia_tri):
    try:
        return float(gia_tri)
    except (ValueError, TypeError):
        return None
```

Cấu trúc hoàn chỉnh của khối xử lý ngoại lệ:
- `try`: Chứa đoạn mã có nguy cơ phát sinh lỗi.
- `except`: Bắt và xử lý lỗi cụ thể (tránh dùng `except:` trần trụi mà không bắt loại ngoại lệ xác định).
- `else`: Khối mã chỉ được thực thi nếu khối `try` diễn ra suôn sẻ và không có ngoại lệ nào phát sinh.
- `finally`: Khối mã **luôn luôn được thực thi**, kể cả khi có lỗi hay không, thường dùng để đóng tệp hoặc giải phóng tài nguyên mạng.

---

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-9 -->

::: example Bóc tách dòng dữ liệu và xử lý ngoại lệ với try, except và else

Trong một tệp nhật ký nhiều dòng, chắc chắn sẽ xuất hiện những dòng bị cắt cụt, thiếu trường hoặc sai định dạng số học. Nếu để ngoại lệ làm dừng tiến trình, công sức xử lý các dòng trước đó sẽ bị lãng phí. Cấu trúc gồm `try`, `except` và `else` cho phép chương trình bỏ qua dòng hỏng, ghi nhận lỗi và duy trì tiến trình an toàn.

```python
dong_nhat_ky = [
    "D01,150.5",
    "D02,chu_khong_phai_so",
    "D03,200.0",
    "D04_thieu_dau_phay",
]

hop_le = []
dong_loi = []

for idx, dong in enumerate(dong_nhat_ky, start=1):
    try:
        ma, chuoi_tien = dong.split(",")
        so_tien = float(chuoi_tien)
    except (ValueError, AttributeError):
        dong_loi.append((idx, dong))
    else:
        hop_le.append((ma, so_tien))

print(f"Số dòng hợp lệ: {len(hop_le)}")
for ma, tien in hop_le:
    print(f"  Hợp lệ: mã {ma}, tiền = {tien}")
print(f"Số dòng lỗi:    {len(dong_loi)}")
for idx, dong in dong_loi:
    print(f"  Lỗi tại dòng {idx}: {dong!r}")
```

Kết quả khi chạy đoạn mã trên:

```text
Số dòng hợp lệ: 2
  Hợp lệ: mã D01, tiền = 150.5
  Hợp lệ: mã D03, tiền = 200.0
Số dòng lỗi:    2
  Lỗi tại dòng 2: 'D02,chu_khong_phai_so'
  Lỗi tại dòng 4: 'D04_thieu_dau_phay'
```

Mỗi dòng được tách bằng `split(",")` rồi giải nén vào hai biến. `split` vẫn trả về danh sách khi không có dấu phẩy. Chính phép giải nén sẽ phát sinh `ValueError` nếu số phần khác hai. `float` cũng có thể gây `ValueError` khi phần tiền không đọc được thành số.

Khối `except (ValueError, AttributeError)` bắt chính xác các lớp ngoại lệ dự kiến mà không sử dụng câu lệnh `except` trần trụi. Những dòng gặp lỗi được ghi lại vào danh sách `dong_loi` kèm theo số thứ tự dòng để tiện theo dõi và kiểm tra lại.

Khối `else` chỉ thực thi khi khối `try` hoàn thành suôn sẻ mà không gặp bất kỳ ngoại lệ nào. Việc đặt thao tác thêm bản ghi vào danh sách `hop_le` bên trong `else` giúp tách bạch rõ ràng logic xử lý dữ liệu chuẩn với logic xử lý lỗi.

Kết quả in ra xác nhận có 2 dòng hợp lệ và 2 dòng lỗi được phân loại rành mạch. Cấu trúc `try...except...else` này giúp đường ống xử lý dữ liệu tiếp tục vận hành liên tục mà không bị gián đoạn bởi các bản ghi cá biệt bị hỏng.

:::

<!-- /worked-example -->

## 3. Thao tác với tệp tin và hệ thống tệp

### 3.1. Mở và đóng tệp an toàn với ngữ cảnh `with`
Khối `with open(...)` giúp đóng tệp khi kết thúc việc đọc. Ví dụ dưới tạo một tệp trong thư mục tạm rồi đọc từng dòng:
```python
from pathlib import Path
from tempfile import TemporaryDirectory
with TemporaryDirectory() as thu_muc:
    tep = Path(thu_muc) / "du_lieu.txt"
    tep.write_text("Hà Nội\nĐà Nẵng\n", encoding="utf-8")
    cac_dong = []
    with open(tep, mode="r", encoding="utf-8") as f:
        for dong in f:
            cac_dong.append(dong.strip())
    assert cac_dong == ["Hà Nội", "Đà Nẵng"]
```
Khối lệnh `with` bảo đảm rằng tệp tin luôn được đóng an toàn ngay sau khi thoát khỏi khối mã, kể cả khi quá trình đọc tệp phát sinh ngoại lệ đột ngột.

### 3.2. Các phương thức đọc tệp
- `f.read()`: Đọc toàn bộ nội dung tệp thành một chuỗi duy nhất. Chỉ nên dùng khi kích thước tệp nhỏ và vừa vặn với RAM.
- `f.readlines()`: Đọc toàn bộ tệp và trả về danh sách các dòng văn bản.
- `for dong in f:`: Duyệt từng dòng mà không tự nạp cả tệp thành một danh sách. Bộ nhớ sử dụng còn phụ thuộc bộ đệm, độ dài dòng và việc chương trình có giữ lại kết quả của các dòng trước hay không.

<!-- worked-example bai-03-cau-truc-du-lieu-ham-tep-worked-10 -->

::: example Đọc và phân tách dòng văn bản với read_text và splitlines

Khi xử lý các tệp cấu hình hoặc dữ liệu bảng kích thước nhỏ, việc đọc toàn bộ tệp thành chuỗi văn bản thông qua `pathlib.Path` giúp đơn giản hóa mã nguồn. Phương thức `splitlines` xử lý tự động các ký tự xuống dòng khác nhau giữa các hệ điều hành. Ta đọc tệp tạm và trích xuất dữ liệu thành các trường có cấu trúc.

```python
import tempfile
from pathlib import Path

du_lieu_csv = """ma_kho,ten_kho,suc_chua
K01,Kho Bac Ninh,15000
K02,Kho Da Nang,8000
K03,Kho Binh Duong,22000"""

with tempfile.NamedTemporaryFile(
    mode="w", suffix=".csv", delete=False, encoding="utf-8"
) as f:
    f.write(du_lieu_csv)
    duong_dan = Path(f.name)

try:
    noi_dung = duong_dan.read_text(encoding="utf-8")
    cac_dong = [d.strip() for d in noi_dung.splitlines() if d.strip()]
    tieu_de = cac_dong[0].split(",")
    for dong in cac_dong[1:]:
        gia_tri = dong.split(",")
        print(f"Kho {gia_tri[0]}: {gia_tri[1]} (sức chứa {int(gia_tri[2]):,d})")
finally:
    duong_dan.unlink(missing_ok=True)
```

Kết quả khi chạy đoạn mã trên:

```text
Kho K01: Kho Bac Ninh (sức chứa 15,000)
Kho K02: Kho Da Nang (sức chứa 8,000)
Kho K03: Kho Binh Duong (sức chứa 22,000)
```

Đoạn mã sử dụng `NamedTemporaryFile` để tạo một tệp dữ liệu tạm thời với mã hóa UTF-8. Lớp `Path` từ thư viện `pathlib` quản lý đường dẫn tệp một cách hướng đối tượng và tương thích trên nhiều hệ điều hành.

Phương thức `duong_dan.read_text(encoding='utf-8')` mở tệp, đọc toàn bộ nội dung thành chuỗi `str` và tự động đóng tệp. Phương thức `splitlines()` phân tách chuỗi thành danh sách các dòng, xử lý đồng nhất cả ký tự xuống dòng `\n` của Unix lẫn `\r\n` của Windows.

Thao tác tách chuỗi bằng `split(',')` trong ví dụ này chỉ phù hợp với các tệp dữ liệu đơn giản, trong đó các trường không chứa dấu phẩy nằm trong ngoặc kép hoặc ký tự xuống dòng bên trong nội dung. Đối với dữ liệu CSV tổng quát trong thực tế, việc dùng `split(',')` sẽ bị sai lệch cấu trúc cột, và ta bắt buộc phải sử dụng thư viện chuyên dụng như `csv.reader` hoặc `pandas.read_csv`.

Khối `finally` gọi phương thức `unlink()` để xóa tệp tạm khỏi ổ đĩa, bảo đảm không để lại tài nguyên rác sau phiên làm việc. Kết quả in ra xác nhận các thông tin kho hàng và sức chứa đã được bóc tách chính xác từ tệp văn bản.

:::

<!-- /worked-example -->

### 3.3. Chế độ mở và mã hóa ký tự
- Chế độ mở tệp: Đọc văn bản (`'r'`), ghi đè (`'w'`), ghi tiếp vào cuối (`'a'`), đọc nhị phân (`'rb'`), ghi nhị phân (`'wb'`).
- Mã hóa ký tự: Nếu tệp dùng UTF-8, hãy ghi rõ `encoding="utf-8"`. Với nguồn dùng mã hóa khác, cần chọn đúng mã hóa của nguồn. Giá trị mặc định còn phụ thuộc phiên bản Python và cấu hình, nên không nên dựa vào đó để diễn giải dữ liệu.

---

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 3: Built-In Data Structures, Functions, and Files.
- Python Software Foundation. *Data Structures & itertools: Functions creating iterators for efficient looping*. https://docs.python.org/3/library/itertools.html
- David Beazley. *Python Cookbook*, tái bản lần 3. O'Reilly Media, 2013.

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 4. Bài tập thực hành

::: exercise Bài tập 1: Pipeline làm sạch chuỗi bằng danh sách hàm bậc cao
Một tập dữ liệu văn bản thô chứa tên các địa danh bị lỗi khoảng trắng và dấu câu như sau:
```python
dia_danh_tho = ["  hà NỘI! ", " ĐÀ Nẵng? ", "TP. Hồ Chí Minh  "]
```
Hãy xây dựng một hệ thống làm sạch dữ liệu tuân thủ các yêu cầu sau:
1. Viết ba hàm nhỏ độc lập:
   - `loai_khoang_trang(s)`: Loại bỏ các khoảng trắng thừa ở đầu và cuối chuỗi.
   - `xoa_dau_cau(s)`: Loại bỏ các ký tự dấu câu `!`, `?`, và dấu chấm `.`.
   - `chuan_hoa_chu_hoa(s)`: Chuyển đổi chuỗi về định dạng viết hoa chữ cái đầu mỗi từ (`title`).
2. Gom ba hàm trên vào một danh sách `pipeline = [loai_khoang_trang, xoa_dau_cau, chuan_hoa_chu_hoa]`.
3. Sử dụng List Comprehension kết hợp duyệt qua danh sách hàm trong `pipeline` để biến đổi danh sách `dia_danh_tho` thành danh sách sạch.
:::

::: solution Lời giải
```python
import re

dia_danh_tho = ["  hà NỘI! ", " ĐÀ Nẵng? ", "TP. Hồ Chí Minh  "]

def loai_khoang_trang(s):
    return s.strip()

def xoa_dau_cau(s):
    return re.sub(r"[!?.]", "", s)

def chuan_hoa_chu_hoa(s):
    return s.title()

pipeline = [loai_khoang_trang, xoa_dau_cau, chuan_hoa_chu_hoa]

def lam_sach_chuoi(van_ban):
    for f in pipeline:
        van_ban = f(van_ban)
    return van_ban

dia_danh_sach = [lam_sach_chuoi(s) for s in dia_danh_tho]
print("Kết quả làm sạch:", dia_danh_sach)
```

Kết quả in ra:
- `['Hà Nội', 'Đà Nẵng', 'Tp Hồ Chí Minh']`.
- Mỗi hàm trong pipeline thực hiện đúng một nhiệm vụ duy nhất, giúp mã nguồn dễ dàng mở rộng khi cần thêm các bước chuẩn hóa mới.
:::

::: exercise Bài tập 2: Xử lý tệp log dạng dòng với Generator và Exception Handling
Giả sử bạn cần đọc một luồng dữ liệu giao dịch từ nhật ký hệ thống. Dữ liệu gồm các dòng văn bản ngăn cách bởi dấu phẩy chứa `ma_giao_dich,so_tien`. Một số dòng bị lỗi dữ liệu chuỗi hoặc thiếu giá trị:
```python
du_lieu_log = [
    "101,250",
    "102,invalid",
    "103,400",
    "104,"
]
```
1. Hãy viết một hàm sinh `phan_tich_log(cac_dong)` sử dụng từ khóa `yield` để duyệt qua từng dòng.
2. Với mỗi dòng, tách trường dữ liệu bằng dấu phẩy. Sử dụng cấu trúc `try/except ValueError` để chuyển đổi trường số tiền sang số nguyên `int`. Nếu dòng dữ liệu hợp lệ, trả về một tuple `(ma_gd, so_tien)`.
3. Nếu dòng dữ liệu bị lỗi chuyển đổi kiểu hoặc thiếu trường, hàm sẽ bỏ qua dòng đó một cách an toàn mà không làm sập chương trình.
4. Chuyển toàn bộ đầu ra của hàm sinh thành danh sách và tính tổng số tiền của các giao dịch hợp lệ.
:::

::: solution Lời giải
```python
du_lieu_log = [
    "101,250",
    "102,invalid",
    "103,400",
    "104,"
]

def phan_tich_log(cac_dong):
    for dong in cac_dong:
        thanh_phan = dong.strip().split(",")
        if len(thanh_phan) == 2:
            try:
                ma_gd = int(thanh_phan[0])
                so_tien = int(thanh_phan[1])
                yield ma_gd, so_tien
            except ValueError:
                continue

# Khởi tạo hàm sinh và trích xuất kết quả
ds_hop_le = list(phan_tich_log(du_lieu_log))
tong_tien = sum(tien for ma, tien in ds_hop_le)

print("Các giao dịch hợp lệ:", ds_hop_le)
print("Tổng số tiền hợp lệ:", tong_tien)
```

Kết quả:
- Dòng `"102,invalid"` và dòng `"104,"` phát sinh lỗi `ValueError` khi ép kiểu số nguyên và được bỏ qua an toàn.
- `ds_hop_le`: `[(101, 250), (103, 400)]`.
- Tổng số tiền hợp lệ: $250 + 400 = 650$.
:::

::: exercise Bài tập 3: Gom nhóm dữ liệu và đếm tần suất với defaultdict
Cho danh sách các bản ghi doanh thu theo khu vực thị trường:
```python
giao_dich = [
    ("Bắc", 100),
    ("Nam", 200),
    ("Bắc", 150),
    ("Trung", 80),
    ("Nam", 50)
]
```
1. Sử dụng lớp `defaultdict` từ thư viện `collections` để tính tổng doanh thu theo từng khu vực.
2. Sử dụng `defaultdict(list)` để gom toàn bộ các giao dịch riêng lẻ của từng khu vực vào danh sách tương ứng.
3. Chuyển kết quả về từ điển chuẩn và in ra màn hình.
:::

::: solution Lời giải
```python
from collections import defaultdict

giao_dich = [
    ("Bắc", 100),
    ("Nam", 200),
    ("Bắc", 150),
    ("Trung", 80),
    ("Nam", 50)
]

# 1. Tính tổng doanh thu theo khu vực
tong_doanh_thu = defaultdict(int)
for khu, tien in giao_dich:
    tong_doanh_thu[khu] += tien

# 2. Gom danh sách giao dịch theo khu vực
ds_giao_dich = defaultdict(list)
for khu, tien in giao_dich:
    ds_giao_dich[khu].append(tien)

print("Tổng doanh thu từng khu:", dict(tong_doanh_thu))
print("Chi tiết các giao dịch:", dict(ds_giao_dich))
```

Kết quả:
- Tổng doanh thu: `{'Bắc': 250, 'Nam': 250, 'Trung': 80}`.
- Chi tiết giao dịch: `{'Bắc': [100, 150], 'Nam': [200, 50], 'Trung': [80]}`.
- Cơ chế `defaultdict` giúp loại bỏ hoàn toàn các câu lệnh kiểm tra điều kiện tồn tại của khóa trước khi cập nhật dữ liệu.
:::





<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-02">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-02.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 3: Built-In Data Structures, Functions, and Files.
- Python Software Foundation. *Data Structures & itertools: Functions creating iterators for efficient looping*. https://docs.python.org/3/library/itertools.html
- David Beazley. *Python Cookbook*, tái bản lần 3. O'Reilly Media, 2013.

- IAI, [Lập trình xử lý dữ liệu, học liệu và notebook](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các đề thực hành đã được biên tập cách diễn đạt và bổ sung lời giải, giữ [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/). [Giấy phép học liệu](https://github.com/uet-iai-course/programming-for-data-processing/blob/main/LICENSE).

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
