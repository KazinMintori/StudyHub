---
course: xu-ly-du-lieu
lecture: bai-01-tong-quan-cong-cu-chinh-sach-ai
section: lecture
title: "Công việc xử lý dữ liệu và môi trường Python"
prerequisites: []
lessonStatus: ready
hasChapterExercises: true
description: "Công việc xử lý dữ liệu, ngăn xếp Scientific Python, kiến trúc IPython Kernel, quản lý môi trường ảo và quy ước làm việc."
---


<div class="lecture-notes-content">

## 1. Công việc xử lý dữ liệu trong thực tế

### 1.1. Thực tế dữ liệu và các dạng dữ liệu phổ biến
Bạn nhận hai tệp: Danh sách đơn hàng và bảng thanh toán. Cả hai cùng ghi doanh thu, nhưng tổng tiền không khớp. Trước khi cộng cột, ta cần xác định một hàng đại diện cho điều gì và hai bảng liên kết bằng khóa nào.

Trong các bài tập mẫu, người học thường tiếp cận dữ liệu dưới dạng các bảng số liệu sạch sẽ, ngay ngắn và đồng nhất. Tuy nhiên, trong môi trường sản xuất thực tế, dữ liệu thô hiếm khi ở trạng thái sẵn sàng cho mô hình hóa. Dữ liệu thực tế thường đối mặt với ba vấn đề:
- **Phân mảnh và đa dạng nguồn**: Một phần dữ liệu nằm trong nhật ký máy chủ bán cấu trúc, một phần nằm trong cơ sở dữ liệu quan hệ SQL và một phần được truyền qua API dưới dạng JSON lồng nhau. Sự đa dạng này đòi hỏi nhiều kỹ thuật kết nối khác nhau.
- **Nhiễu loạn và suy hao**: Các trường số học bị lẫn ký tự tiền tệ hoặc đơn vị đo lường, ngày tháng bị xung đột giữa các quy ước quốc tế, và nhiều bản ghi bị trùng lặp do lỗi kết nối mạng khi người dùng gửi yêu cầu nhiều lần.
- **Xung đột định nghĩa nghiệp vụ**: Cùng một chỉ số kinh doanh, hai phòng ban có thể áp dụng hai công thức tính toán khác nhau, dẫn tới những con số vênh nhau nếu không được chuẩn hóa ngay từ tầng dữ liệu thô.

Dữ liệu trong phân tích hiện đại thường phân bố ở bốn nhóm cấu trúc chính:
1. **Dữ liệu dạng bảng (Tabular data)**: Cấu trúc phổ biến gồm các hàng biểu diễn cho từng quan sát và các cột mang tên nhãn cụ thể, trong đó mỗi cột có thể chứa một kiểu dữ liệu riêng biệt.
2. **Dữ liệu chuỗi thời gian (Time series)**: Tập hợp các điểm dữ liệu được gắn nhãn thời gian cố định hoặc biến đổi, đòi hỏi các phép toán trượt cửa sổ, dịch chuyển thời gian và đổi tần suất lấy mẫu.
3. **Mảng nhiều chiều và ma trận số học**: Cấu trúc số học đồng nhất nhiều chiều dùng trong xử lý hình ảnh, tín hiệu số, hoặc làm đầu vào cho các thuật toán học máy.
4. **Các bảng liên kết (Relational tables)**: Nhiều bảng dữ liệu độc lập nhưng liên kết với nhau thông qua các trường khóa chung, cần các phép ghép nối (*join*, *merge*) để tạo thành tập dữ liệu phân tích hoàn chỉnh.

<!-- worked-example bai-01-tong-quan-cong-cu-chinh-sach-ai-worked-1 -->

::: example Đối chiếu bản ghi giữa danh mục đơn hàng và nhật ký thanh toán

Một cửa hàng lưu đơn hàng và giao dịch thanh toán ở hai danh sách. Ta cần tìm mã đơn chưa có bản ghi thanh toán tương ứng và tính tổng tiền đã được ghi nhận. Trong ví dụ này, mỗi bản ghi thanh toán được coi là một giao dịch thành công và không lặp lại.

```python
don_hang = [
    {"ma": "DH01", "tien": 120000},
    {"ma": "DH02", "tien": 250000},
    {"ma": "DH03", "tien": 180000},
]
thanh_toan = [
    {"ma_don": "DH01", "tien": 120000},
    {"ma_don": "DH03", "tien": 180000},
]

ma_tt = {item["ma_don"] for item in thanh_toan}
lech = [item for item in don_hang if item["ma"] not in ma_tt]
tong_tt = sum(item["tien"] for item in thanh_toan)

print("Đơn chưa có bản ghi thanh toán:", [x["ma"] for x in lech])
print("Tổng tiền đơn chưa đối soát:   ", sum(x["tien"] for x in lech))
print("Tổng tiền thanh toán nhận được:", tong_tt)
```

Kết quả khi chạy đoạn mã trên:

```text
Đơn chưa có bản ghi thanh toán: ['DH02']
Tổng tiền đơn chưa đối soát:    250000
Tổng tiền thanh toán nhận được: 300000
```

Đoạn mã tiếp nhận hai danh sách từ điển đại diện cho danh mục đơn hàng và nhật ký thanh toán. Mỗi phần tử trong danh sách chứa khóa định danh mã đơn cùng số tiền tương ứng. Mục tiêu của thao tác là đối chiếu sự hiện diện của mã đơn giữa hai bảng dữ liệu độc lập.

Tập hợp `ma_tt` chứa các mã đơn đã xuất hiện trong nhật ký thanh toán. Biểu thức `item["ma"] not in ma_tt` chọn các đơn chưa có mã tương ứng. Sau đó, `sum` cộng các trường `tien`. Đây mới là đối chiếu mã, chưa phải kiểm tra xem số tiền của từng đơn có khớp giữa hai danh sách hay không.

Việc mã đơn `DH02` chưa xuất hiện trong bảng thanh toán chỉ cho thấy hệ thống thanh toán đang thiếu bản ghi của đơn này. Kết quả này không tự chứng minh khách hàng đang nợ tiền, và cũng không chứng minh giao dịch thanh toán bị thất bại.

Nếu một đơn có nhiều lần thanh toán hoặc hoàn tiền, sự hiện diện của mã đơn chưa cho biết đã thu đủ tiền. Khi cần đối chiếu tiền, hãy gom các khoản theo mã đơn, thống nhất cách ghi hoàn tiền rồi mới so sánh tổng với giá trị đơn hàng.

:::

<!-- /worked-example -->

### 1.2. Chu trình xử lý dữ liệu từ dữ liệu thô đến quyết định
Quá trình phân tích dữ liệu là một chuỗi biến đổi khép kín gồm các bước: Thu thập, làm sạch, chuyển dạng, tổng hợp, trực quan hóa và kiểm tra kết luận.

Trước khi mô hình hóa, ta cần kiểm tra dữ liệu có phù hợp với câu hỏi hay không. Một phép tính có thể chạy đúng nhưng trả lời sai câu hỏi nếu bảng bị lặp hàng, dùng nhầm đơn vị hoặc chọn khác tập quan sát. Vì vậy, làm sạch và kiểm chứng phải gắn với ý nghĩa của từng cột.

Mục tiêu của môn học là trang bị năng lực biến những tập dữ liệu thô hỗn loạn thành dữ liệu sạch, đáng tin cậy và có thể kiểm chứng được bằng mã nguồn minh bạch.

---

<!-- worked-example bai-01-tong-quan-cong-cu-chinh-sach-ai-worked-2 -->

::: example Tách ký tự đơn vị và chuyển chuỗi số theo quy ước phân cách hàng nghìn

Biểu mẫu sau ghi số tiền nguyên không âm. Dấu chấm trong nguồn này phân cách hàng nghìn, các chữ số thuộc bộ ASCII, còn đơn vị là `đ` hoặc `VND`. Ta chuyển những chuỗi theo quy ước đó thành số nguyên và giữ giá trị chưa xác định bằng `None`.

```python
du_lieu_tho = [
    " 150000 đ ", "200.500 VND", " 180000 ", "Chưa thanh toán"
]

def lam_sach_so_tien(gia_tri):
    if not isinstance(gia_tri, str):
        return None
    chuoi = gia_tri.strip()
    for ky_tu in ["đ", "VND", " "]:
        chuoi = chuoi.replace(ky_tu, "")
    chuoi = chuoi.replace(".", "")
    if chuoi.isascii() and chuoi.isdigit():
        return int(chuoi)
    return None

for muc in du_lieu_tho:
    kq = lam_sach_so_tien(muc)
    print(f"{muc!r:>20} -> {kq}")
```

Kết quả khi chạy đoạn mã trên:

```text
        ' 150000 đ ' -> 150000
       '200.500 VND' -> 200500
          ' 180000 ' -> 180000
   'Chưa thanh toán' -> None
```

Hàm `lam_sach_so_tien` tiếp nhận đối số `gia_tri` dưới dạng chuỗi văn bản hoặc kiểu dữ liệu bất kỳ. Nếu đầu vào không phải kiểu chuỗi `str`, hàm trả về `None` để biểu thị dữ liệu không đúng khuôn mẫu. Đầu ra của hàm là một số nguyên `int` hoặc giá trị `None`.

Phương thức `strip()` loại bỏ khoảng trắng thừa ở hai đầu chuỗi, sau đó phương thức `replace()` lần lượt xóa các ký hiệu tiền tệ phổ biến và dấu cách. Lệnh `chuoi.replace('.', '')` loại bỏ dấu chấm dựa trên giả thiết rõ ràng rằng dấu chấm đóng vai trò phân cách hàng nghìn trong nguồn dữ liệu này, chứ không phải một bộ phân tích tiền tệ vạn năng.

`isascii()` giới hạn chuỗi vào bộ ký tự ASCII, còn `isdigit()` kiểm tra các ký tự còn lại có phải chữ số hay không. Hai điều kiện này giúp `int()` nhận chuỗi số nguyên như `"200500"`. Nếu chỉ dùng `isdigit()`, một số ký tự như `"²"` vẫn được nhận là chữ số nhưng không chuyển được bằng `int()`.

Hàm cho kết quả 150000, 200500, 180000 và `None`. Nó chuẩn hóa dữ liệu theo quy ước đã nêu, chưa kiểm tra mọi cách đặt dấu phân cách. Chẳng hạn, nếu dấu chấm là dấu thập phân thì xóa dấu trong `"12.5"` sẽ biến 12,5 thành 125. Vì vậy, cần xác định định dạng nguồn trước khi chọn quy tắc chuyển đổi.

:::

<!-- /worked-example -->

## 2. Vì sao chọn Python cho phân tích dữ liệu?

### 2.1. Python trong vai trò ngôn ngữ điều phối và kết nối
Python là một ngôn ngữ thông dịch (*interpreted language*). Tốc độ duyệt vòng lặp thuần túy của Python chậm hơn đáng kể so với các ngôn ngữ biên dịch như C hay C++. Dù vậy, Python được ứng dụng rộng rãi trong kỹ thuật dữ liệu nhờ khả năng đóng vai trò ngôn ngữ điều phối và kết nối các thành phần tính toán.

Ngăn xếp tính toán khoa học kết hợp hai ưu thế:
1. **Tầng tương tác bậc cao**: Python cung cấp cú pháp gần gũi với tư duy toán học và ngôn ngữ tự nhiên, giúp người phân tích diễn đạt ý tưởng nhanh chóng mà không cần bận tâm về việc quản lý con trỏ hay cấp phát bộ nhớ thủ công.
2. **Tầng tính toán biên dịch**: Bên dưới giao diện lập trình, các thư viện như NumPy và SciPy ủy thác các phép toán ma trận nặng cho các thư viện biên dịch sẵn bằng C, Fortran hoặc C++ (như BLAS, LAPACK khi có sẵn).

Khi thực hiện phép tính trên một mảng dữ liệu, Python đóng vai trò điều phối gửi chỉ thị xuống khối mã C đã được biên dịch tối ưu cho phần cứng CPU. Nhờ đó, chương trình vừa giữ được sự linh hoạt trong phát triển mã nguồn, vừa đạt tốc độ tính toán của mã nhị phân tối ưu.

<!-- worked-example bai-01-tong-quan-cong-cu-chinh-sach-ai-worked-3 -->

::: example Phối hợp danh sách Python và bộ đệm số học NumPy

Khi xử lý mảng số lớn, việc duyệt từng phần tử bằng vòng lặp Python thuần tạo ra chi phí quản lý đối tượng lớn. Ngược lại, việc chuyển danh sách thành mảng số học giúp Python ủy thác toàn bộ phép tính cho khối mã C được biên dịch sẵn của NumPy. Ta đối chiếu cách viết lặp truyền thống và hàm cộng dồn mảng để thấy rõ vai trò điều phối của Python.

```python
import numpy as np

gia_tri = [12.5, 18.0, 24.5, 30.0, 15.0]

tong_thuan = 0.0
for x in gia_tri:
    tong_thuan += x

mang = np.array(gia_tri, dtype=np.float64)
tong_numpy = float(np.sum(mang))

print(f"Tổng lặp:  {tong_thuan:.1f}")
print(f"Tổng mảng: {tong_numpy:.1f}")
print(f"Khớp nhau: {tong_thuan == tong_numpy}")
```

Kết quả khi chạy đoạn mã trên:

```text
Tổng lặp:  100.0
Tổng mảng: 100.0
Khớp nhau: True
```

Đoạn mã tiếp nhận một danh sách Python chứa các số thực và thực hiện tính tổng theo hai cơ chế khác nhau. Cơ chế thứ nhất dùng vòng lặp `for` truyền thống để cộng dồn từng phần tử vào biến `tong_thuan`. Cơ chế thứ hai chuyển danh sách thành đối tượng `ndarray` với kiểu dữ liệu `np.float64` và gọi hàm `np.sum`.

Trong vòng lặp thuần, mỗi lần cộng dồn, trình thông dịch Python phải kiểm tra kiểu của đối tượng `x`, mở hộp giá trị số thực và cấp phát đối tượng mới cho kết quả. Quá trình này tiêu tốn nhiều chu kỳ xử lý của CPU do chi phí thông dịch động.

Khi chuyển sang mảng NumPy, toàn bộ các số thực được xếp liên tục trong một khối bộ nhớ liền kề. Hàm `np.sum` ủy thác vòng lặp tính toán trực tiếp cho khối mã nhị phân C bên dưới, bỏ qua chi phí đóng gói đối tượng của Python.

Với các số trong ví dụ, cả hai cách đều cho tổng 100.0. Đoạn mã chưa đo thời gian chạy nên chưa kết luận cách nào nhanh hơn ở đây. Với số thực khác, thứ tự cộng cũng có thể tạo ra sai khác làm tròn. Khi so sánh gần đúng, cần chọn dung sai phù hợp với đại lượng đang tính.

:::

<!-- /worked-example -->

### 2.2. Giải quyết bài toán hai ngôn ngữ (Two-Language Problem)
Trước khi Python phổ biến trong khoa học dữ liệu, các tổ chức nghiên cứu thường đối mặt với bài toán hai ngôn ngữ:
- Giai đoạn nghiên cứu mẫu thử (prototype) được thực hiện trên một ngôn ngữ chuyên sâu về thống kê hoặc toán học (như R, MATLAB, SAS).
- Khi đưa vào vận hành, một số dự án phải chuyển một phần hoặc cả chương trình sang công cụ khác để đáp ứng yêu cầu về hiệu năng hay tích hợp.

Quy trình hai bước này gây lãng phí nguồn lực kỹ thuật, dễ phát sinh lỗi chuyển đổi công thức và làm chậm tiến độ triển khai sản phẩm. Python thống nhất cả hai giai đoạn: Một nhà phân tích có thể xây dựng mô hình thử nghiệm trong sổ tay tương tác, và chính đoạn mã đó có thể được đóng gói trực tiếp vào dịch vụ vận hành thực tế.

### 2.3. Ranh giới và giới hạn của Python
Bên cạnh các ưu thế rõ rệt, người làm kỹ thuật dữ liệu cần nhận thức rõ những giới hạn của Python:
- **Khóa thông dịch toàn cục (Global Interpreter Lock, GIL)**: Trong bản dựng CPython có bật GIL, tại một thời điểm chỉ một luồng được thực thi mã Python trong cùng trình thông dịch. Điều này không buộc luồng luôn nằm trên một lõi CPU. Một số thư viện có thể nhả GIL khi tính toán, còn bản dựng free-threaded có cơ chế khác. Vì vậy phải xác định môi trường và loại công việc trước khi chọn luồng hay tiến trình.
- **Chi phí vòng lặp thông dịch**: Việc viết vòng lặp `for` duyệt qua từng phần tử trên tập dữ liệu lớn bằng Python thuần sẽ gây suy giảm hiệu năng đáng kể. Nhiều phép biến đổi quy mô lớn cần được chuyển thành phép toán vector hóa của NumPy, pandas, hoặc xử lý theo khối đệm.
- **Giới hạn bộ nhớ RAM**: Khi nạp cả bảng vào pandas, dữ liệu và các kết quả trung gian cần bộ nhớ. Nếu không đủ RAM, chương trình có thể chậm do phân trang hoặc không cấp phát được dữ liệu. Đọc theo khối, chọn cột, đổi kiểu phù hợp hay truy vấn tại nơi lưu dữ liệu là những cách cần cân nhắc trước khi mở rộng công cụ.

---

## 3. Ngăn xếp tính toán khoa học Python (Scientific Python Stack)

Hệ sinh thái xử lý dữ liệu hiện đại được xây dựng dựa trên ngăn xếp các thư viện chuyên biệt:

1. **NumPy (*Numerical Python*)**: Là nền móng của hệ sinh thái tính toán số học. NumPy cung cấp đối tượng mảng đa chiều đồng nhất `ndarray`, các hàm toán học vector hóa (*ufuncs*), cùng các công cụ đại số tuyến tính và sinh số ngẫu nhiên.
2. **pandas**: Thư viện xử lý dữ liệu dạng bảng. pandas cung cấp hai cấu trúc dữ liệu chính là `Series` (mảng một chiều có nhãn) và `DataFrame` (bảng hai chiều có nhãn hàng và cột). pandas sở hữu bộ công cụ phong phú để nạp tệp, làm sạch dữ liệu khuyết thiếu, nối bảng, chuyển đổi hình dạng và tổng hợp theo nhóm. Ngoài vùng đệm NumPy truyền thống, pandas hiện đại còn hỗ trợ các định dạng lưu trữ như PyArrow.
3. **Matplotlib & Seaborn**: Bộ đôi trực quan hóa dữ liệu. Matplotlib kiểm soát chi tiết từng thành phần của trục tọa độ và hình vẽ, trong khi Seaborn cung cấp giao diện bậc cao để tạo các đồ thị thống kê trực quan.
4. **IPython & Jupyter**: Cung cấp môi trường thực thi tương tác dòng lệnh và giao diện sổ tay nghiên cứu, hỗ trợ quy trình khám phá dữ liệu lặp đi lặp lại.
5. **SciPy**: Mở rộng các thuật toán khoa học chuyên sâu dựa trên NumPy, bao gồm tối ưu hóa hàm số, tích phân số trị, xử lý tín hiệu và các phân phối xác suất thống kê.
6. **scikit-learn & statsmodels**: Scikit-learn là bộ công cụ học máy phổ biến (phân loại, hồi quy, gom cụm), còn statsmodels tập trung vào các mô hình thống kê suy diễn cổ điển, kinh lượng học và kiểm định giả thuyết.

---

<!-- worked-example bai-01-tong-quan-cong-cu-chinh-sach-ai-worked-4 -->

::: example Kiểm tra phiên bản các thư viện cốt lõi bằng importlib.metadata

Một notebook chạy được trên máy này có thể gặp lỗi trên máy khác khi phiên bản thư viện khác nhau. Ta dùng `importlib.metadata` để xem phiên bản NumPy và pandas trong chính môi trường đang chạy, đồng thời xử lý trường hợp gói chưa được cài.

```python
import importlib.metadata

cac_goi = ["numpy", "pandas"]
for ten in cac_goi:
    try:
        ver = importlib.metadata.version(ten)
        major = int(ver.split(".")[0])
        print(f"Gói {ten:<8}: phiên bản {ver}, thế hệ chính {major}")
    except importlib.metadata.PackageNotFoundError:
        print(f"Gói {ten:<8}: chưa được cài đặt")
```

Kết quả khi chạy đoạn mã trên:

```text
Gói numpy   : phiên bản 2.5.2, thế hệ chính 2
Gói pandas  : phiên bản 3.0.5, thế hệ chính 3
```

Đoạn mã nhận vào danh sách chuỗi tên các thư viện cần kiểm tra môi trường. Vòng lặp duyệt qua từng tên gói và gọi hàm `importlib.metadata.version` để tra cứu siêu dữ liệu đã được cài đặt trong môi trường hiện hành.

`version(ten)` trả chuỗi phiên bản của gói đã cài. Trong ví dụ, `split(".")[0]` lấy phần đầu rồi chuyển sang số nguyên, chẳng hạn lấy 3 từ `"3.0.5"`. Chuỗi đầy đủ vẫn được in ra vì chỉ số phiên bản chính không đủ để tái lập môi trường.

Nếu một gói chưa từng được cài đặt trong môi trường, hàm sẽ làm phát sinh ngoại lệ `PackageNotFoundError`. Việc bọc khối tra cứu trong cấu trúc `try...except` giúp chương trình không bị gián đoạn, đồng thời thông báo trạng thái gói một cách rõ ràng.

Kết quả in ra cung cấp thông tin kiểm tra nhanh về các thành phần cốt lõi của Scientific Python Stack. Trong thực tế, kỹ thuật này thường được đặt ở đầu các kịch bản kiểm thử nhằm bảo đảm các gói phụ thuộc đã sẵn sàng trước khi xử lý dữ liệu.

:::

<!-- /worked-example -->

## 4. Kiến trúc Môi trường Tính toán: Kịch bản Python và Sổ tay Jupyter

### 4.1. Phân biệt tệp mã nguồn `.py` và sổ tay `.ipynb`
Người lập trình có thể thực thi cùng một biểu thức tính toán trong tệp kịch bản `.py` hoặc trong một ô của Jupyter Notebook. Điểm khác biệt cốt lõi nằm ở định dạng tệp và cách thức lưu trữ:

- **Tệp mã nguồn `.py`**: Là tệp văn bản thuần (*plain text*). Khi thực thi bằng lệnh `python chuong_trinh.py`, trình thông dịch đọc tuần tự các câu lệnh từ đầu đến cuối tệp. Đầu ra in ra màn hình hoặc tệp nhật ký, hoàn toàn không được ghi ngược vào tệp mã nguồn. Tệp `.py` là định dạng chuẩn để xây dựng các mô-đun, thư viện và đường ống xử lý tự động chạy ngầm.
- **Sổ tay tính toán `.ipynb`**: Thực chất là một tệp văn bản chứa dữ liệu có cấu trúc theo định dạng JSON (*JavaScript Object Notation*). Cấu trúc tệp bao gồm:
  - Trường `cells`: Danh sách các ô tính toán. Mỗi ô mã chứa nội dung mã (`source`), số thứ tự thực thi (`execution_count`), và toàn bộ kết quả đầu ra tương ứng (`outputs`). Đầu ra có thể là văn bản, bảng HTML, hoặc ảnh biểu đồ mã hóa Base64.
  - Trường `metadata`: Thông tin về môi trường kernel, phiên bản ngôn ngữ và cấu hình hiển thị.

Nhờ lưu trữ đồng thời cả mã lệnh lẫn kết quả đầu ra, tệp `.ipynb` cho phép người đọc xem trực tiếp biểu đồ và bảng kết quả mà không cần chạy lại toàn bộ mã nguồn.

<!-- worked-example bai-01-tong-quan-cong-cu-chinh-sach-ai-worked-5 -->

::: example Đọc và phân tách cấu trúc ô tính toán trong tệp sổ tay JSON

Tệp sổ tay Jupyter có phần mở rộng `.ipynb` thực chất là một tài liệu JSON chứa mã nguồn kèm các khối kết quả đã được lưu. Khi cần tự động hóa việc kiểm tra mã hoặc trích xuất nội dung, ta có thể phân tích trực tiếp cấu trúc của tệp này bằng thư viện `json`. Đoạn mã sau mô phỏng việc tạo một sổ tay tối giản trong thư mục tạm và đọc lại các trường quan trọng.

```python
import json
import tempfile
from pathlib import Path

noi_dung_so_tay = {
    "cells": [
        {
            "cell_type": "code",
            "metadata": {},
            "id": "cell-demo1",
            "execution_count": 1,
            "source": ["a = 5\n", "print(a * 2)"],
            "outputs": [{"output_type": "stream", "name": "stdout", "text": ["10\n"]}],
        }
    ],
    "metadata": {"language_info": {"name": "python"}},
    "nbformat": 4,
    "nbformat_minor": 5,
}

with tempfile.NamedTemporaryFile(
    mode="w", suffix=".ipynb", delete=False, encoding="utf-8"
) as f:
    json.dump(noi_dung_so_tay, f)
    duong_dan = Path(f.name)

try:
    du_lieu = json.loads(duong_dan.read_text(encoding="utf-8"))
    o_dau = du_lieu["cells"][0]
    print(f"Loại ô tính:      {o_dau['cell_type']}")
    print(f"Thứ tự thực thi:  {o_dau['execution_count']}")
    print(f"Số dòng mã nguồn: {len(o_dau['source'])}")
    print(f"Đầu ra đã lưu:    {o_dau['outputs'][0]['text'][0].strip()}")
finally:
    duong_dan.unlink(missing_ok=True)
```

Kết quả khi chạy đoạn mã trên:

```text
Loại ô tính:      code
Thứ tự thực thi:  1
Số dòng mã nguồn: 2
Đầu ra đã lưu:    10
```

Đoạn mã khởi tạo một từ điển Python mô phỏng cấu trúc của một tệp sổ tay Jupyter phiên bản `nbformat` 4. Cấu trúc này chứa danh sách `cells` đại diện cho các ô tính toán, kèm thông tin siêu dữ liệu `metadata` của ngôn ngữ.

`NamedTemporaryFile` tạo tệp tạm, còn `json.dump` ghi từ điển thành JSON. Cờ `delete=False` giữ tệp sau khi đóng để `Path.read_text` có thể mở lại. Việc đóng trước khi đọc giúp ví dụ hoạt động cả trên Windows, nơi một tệp đang mở có thể bị khóa.

Sau `json.loads`, `cells[0]` là ô đầu tiên. `execution_count` là số thứ tự lần chạy đã lưu, còn `outputs` chứa đầu ra cũ. Đọc được chuỗi `10` trong tệp không có nghĩa mã vừa được thực thi lại. Muốn kiểm tra kết quả hiện tại, cần chạy ô mã trong một kernel.

Khối `finally` bảo đảm gọi phương thức `unlink()` của `Path` để xóa tệp tạm ngay cả khi xảy ra sự cố trong quá trình đọc. Việc hiểu rõ định dạng JSON của sổ tay giúp lập trình viên tự tin xây dựng các công cụ trích xuất nội dung hoặc chuyển đổi sổ tay thành báo cáo.

:::

<!-- /worked-example -->

### 4.2. Kiến trúc tương tác ba tầng của Jupyter
Khi bạn thao tác trong Jupyter Notebook trên trình duyệt web, mã lệnh không được thực thi trực tiếp trên trang web đó. Kiến trúc vận hành của Jupyter gồm ba thành phần tách biệt:

1. **Giao diện trình duyệt (Client)**: Tiếp nhận thao tác gõ mã của người dùng và hiển thị kết quả đầu ra.
2. **Máy chủ Jupyter (Jupyter Server)**: Ứng dụng web đóng vai trò trung gian, quản lý các tệp sổ tay trên đĩa và điều phối các phiên làm việc.
3. **Hạt nhân tính toán (IPython Kernel)**: Một tiến trình Python độc lập chạy ngầm trên hệ điều hành, chịu trách nhiệm thực thi các khối mã và duy trì trạng thái các biến trong bộ nhớ RAM.

Khi người dùng nhấn tổ hợp phím `Shift + Enter`, trình duyệt gửi mã qua giao thức WebSocket tới Jupyter Server, sau đó máy chủ chuyển tiếp mã tới IPython Kernel qua thư viện ZeroMQ. Kernel thực thi xong sẽ gửi trả kết quả về trình duyệt để vẽ giao diện.

### 4.3. Thứ tự thực thi `In [ ]` và trạng thái trong bộ nhớ {#_4-3-thu-tu-thuc-thi-in-trang-thai-ram-va-bay-bien-ma}
Cần phân biệt rạch ròi giữa **tệp notebook lưu trên đĩa** và **trạng thái tính toán trong RAM**:

- Nhãn `In [ ]`: Ô chưa từng được thực thi kể từ khi khởi động kernel.
- Nhãn `In [*]`: Ô đang trong trạng thái xử lý tính toán.
- Nhãn `In [n]`: Số nguyên `n` phản ánh thứ tự thực thi của ô đó theo thời gian thực. Nhãn này không phản ánh vị trí hình học từ trên xuống dưới trên trang màn hình.

Mọi ô mã trong cùng một sổ tay chia sẻ chung một không gian tên toàn cục (*global namespace*) trong RAM. Nếu bạn chạy một ô mã gán `x = 10`, sau đó chạy một ô mã khác tăng `x = x + 5` ba lần liên tiếp, giá trị của `x` trong RAM sẽ là $25$, bất kể các ô mã đó nằm ở vị trí nào trên trang.

#### Biến còn trong bộ nhớ sau khi xóa ô mã {#cam-bay-bien-ma-ghost-variable-trap}
Giả sử bạn tạo một ô mã khai báo biến tạm:
```python
du_lieu_tam = [10, 20, 30]
```
Sau khi chạy ô mã này, biến `du_lieu_tam` đã nằm trong RAM của kernel. Bạn viết tiếp các ô mã bên dưới sử dụng biến này. Sau đó, bạn xóa ô khai báo `du_lieu_tam` khỏi giao diện notebook. Vì tiến trình kernel vẫn đang chạy, các ô bên dưới vẫn hoạt động bình thường trong phiên làm việc hiện tại của bạn.

Tuy nhiên, khi gửi tệp `.ipynb` cho đồng nghiệp hoặc chạy trên hệ thống kiểm tra tự động, kernel mới được tạo ra từ đầu. Khi chạy tuần tự, chương trình sẽ lập tức sập với lỗi:
```text
NameError: name 'du_lieu_tam' is not defined
```

> [!IMPORTANT] Kỷ luật vàng khi làm việc với Notebook
> Trước khi chia sẻ notebook, hãy thử khởi động lại kernel và chạy các ô từ trên xuống. Việc này giúp phát hiện phụ thuộc vào trạng thái cũ trong phiên. Muốn chạy lại cả phân tích, còn cần cùng dữ liệu, cấu hình, thư viện và các điều kiện ngẫu nhiên đã được ghi nhận.

---

## 5. Quản trị môi trường làm việc với venv và pip

### 5.1. Cơ chế cách ly gói thư viện và phòng tránh xung đột
Mỗi bản cài Python có các vị trí tìm kiếm gói thư viện, trong đó thường có thư mục `site-packages`. Nếu nhiều dự án cùng dùng một môi trường, việc nâng cấp gói cho dự án này có thể thay đổi phiên bản mà dự án kia sử dụng. Một máy có thể có nhiều bản Python, môi trường ảo và thư mục gói của người dùng.

Thiết kế dùng chung thư mục bộc lộ hai rủi ro:
1. **Xung đột phụ thuộc giữa các dự án (Dependency Collision)**: Dự án cũ của bạn cần `pandas 1.5.3`, trong khi dự án mới yêu cầu `pandas 2.2.0`. Việc cài đè phiên bản mới sẽ làm gãy mã nguồn của dự án cũ do nhiều hàm đã bị thay đổi cú pháp hoặc loại bỏ.
2. **Nguy cơ làm hỏng Python hệ thống**: Trên các hệ điều hành như Linux (Ubuntu, Debian) và macOS, nhiều tiến trình quản trị hệ thống phụ thuộc trực tiếp vào phiên bản Python của hệ thống. Cài đặt bừa bãi với quyền quản trị viên (`sudo pip install`) có thể phá vỡ các công cụ quản lý mạng và gói phần mềm của hệ điều hành.

Môi trường ảo (*virtual environment* hay `venv`) giải quyết vấn đề này bằng cách tạo ra một thư mục biệt lập cho từng dự án, chứa:
- Bản sao hoặc liên kết biểu tượng (*symlink*) trỏ tới tệp thực thi `python`.
- Thư mục `site-packages` riêng biệt, hoàn toàn cách ly với hệ điều hành và các dự án khác.
- Các kịch bản kích hoạt (*activation scripts*) để tạm thời điều chỉnh biến môi trường hệ thống `PATH`.

### 5.2. Quy trình làm việc với `venv`, `requirements.txt` và `.python-version`
Quy trình thiết lập môi trường cho một dự án dữ liệu gồm bốn bước:

```bash
# Bước 1: Điều hướng vào thư mục dự án và khởi tạo môi trường ảo mang tên .venv
python -m venv .venv

# Bước 2: Kích hoạt môi trường ảo
# Trên hệ điều hành Windows PowerShell:
.venv\Scripts\Activate.ps1
# Trên hệ điều hành macOS / Linux:
source .venv/bin/activate
```

Kích hoạt môi trường thường thêm tiền tố `(.venv)` và ưu tiên đường dẫn chương trình của môi trường trong PATH. Hãy kiểm tra `python -c "import sys; print(sys.executable)"` và `python -m pip --version` để biết đúng trình thực thi đang dùng.

```bash
# Bước 3: Cài đặt các gói thư viện cần thiết
pip install numpy pandas matplotlib

# Bước 4: Khóa danh sách phụ thuộc ra tệp cấu hình
pip freeze > requirements.txt
```

Tệp `requirements.txt` lưu trữ danh sách tên gói và phiên bản chính xác, ví dụ:
```text
numpy==1.26.4
pandas==2.2.2
matplotlib==3.8.4
```

Một số công cụ như pyenv hoặc uv đọc `.python-version` để chọn phiên bản Python. Tệp này không tự điều khiển Python hay venv và không mặc nhiên có nghĩa là phiên bản tối thiểu. Khi nhận dự án, cần chọn trình thực thi phù hợp, tạo môi trường rồi cài các gói đã ghi nhận:
```bash
pip install -r requirements.txt
```

> [!TIP] Quy tắc quản lý phiên bản với Git
> Thư mục `.venv` chứa nhiều tệp nhị phân và mã nguồn thư viện với dung lượng lớn. Không đưa thư mục `.venv` lên kho lưu trữ Git. Hãy thêm dòng `.venv/` vào tệp `.gitignore`. Kho lưu trữ chỉ cần lưu mã nguồn của bạn và tệp `requirements.txt`.

---

### 5.3. Môi trường Conda

Conda là một lựa chọn khác để quản lý trình thực thi và các gói. Sau khi cài Miniconda hoặc một bản phân phối Conda phù hợp hệ điều hành, mở terminal được cấu hình cho Conda rồi tạo môi trường riêng:

```bash
conda create -n study-data python numpy pandas matplotlib jupyterlab
conda activate study-data
python -c "import sys; print(sys.executable)"
conda env export --from-history > environment.yml
```

Trên Windows có thể dùng terminal đi kèm bản phân phối. Trên macOS và Linux, cần terminal đã được khởi tạo cho Conda. Hãy theo hướng dẫn cài đặt hiện hành của bản phân phối thay vì dùng một tên bộ cài cố định.

`venv` và Conda là hai cách tổ chức môi trường, không cần lồng chúng cho bài học này. Tệp môi trường ghi các yêu cầu đã chọn. Khi cần lặp lại chính xác một phân tích, còn phải ghi phiên bản và kiểm tra khả năng cài lại trên hệ thống đích.

## 6. Quy ước nhập thư viện và tổ chức mã nguồn

Cộng đồng phân tích dữ liệu đã thống nhất các quy ước viết tắt khi nhập các thư viện cốt lõi. Việc tuân thủ các bí danh chuẩn giúp mã nguồn dễ đọc, dễ bảo trì và tương thích với tài liệu kỹ thuật:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

Các quy tắc thực hành tốt cần duy trì:
- Gom toàn bộ các câu lệnh nhập thư viện (`import`) lên đầu tệp mã nguồn hoặc ô đầu tiên của sổ tay tính toán.
- Tránh sử dụng cú pháp `from module import *` vì cách viết này làm ô nhiễm không gian tên, gây xung đột hàm và khiến người đọc không thể truy vết nguồn gốc của các phương thức.
- Khi viết mã trong sổ tay tương tác, chia nhỏ logic thành các ô độc lập, mỗi ô giải quyết một bước biến đổi cụ thể và có chú thích rõ ràng.

---

<!-- worked-example bai-01-tong-quan-cong-cu-chinh-sach-ai-worked-6 -->

::: example Bảo vệ biến cục bộ và kiểm soát không gian tên với bí danh import as

Chương trình đang có biến `sqrt` chứa một dòng mô tả. Ta vẫn muốn gọi hàm căn bậc hai trong thư viện `math` mà giữ nguyên biến đó. Bí danh `toan` giúp phân biệt hàm của thư viện với tên đang dùng trong chương trình.

```python
import math as toan

sqrt = "Căn bậc hai của mẫu đo"
gia_tri_tinh = toan.sqrt(25.0)

print(f"Biến sqrt sẵn có: {sqrt}")
print(f"Hàm toan.sqrt:    {gia_tri_tinh}")
print(f"Định danh sqrt không bị ghi đè: {isinstance(sqrt, str)}")
```

Kết quả khi chạy đoạn mã trên:

```text
Biến sqrt sẵn có: Căn bậc hai của mẫu đo
Hàm toan.sqrt:    5.0
Định danh sqrt không bị ghi đè: True
```

`sqrt` trong chương trình và `sqrt` trong mô-đun `math` là hai tên thuộc hai không gian tên khác nhau. Phép gán ban đầu gắn tên `sqrt` của chương trình với một chuỗi. `toan.sqrt` truy cập thuộc tính `sqrt` của mô-đun.

Nếu viết `from math import sqrt` sau phép gán chuỗi, tên `sqrt` trong chương trình sẽ được gắn lại với hàm nhập vào. Lệnh nhập không xóa các tham chiếu khác tới chuỗi, nhưng tên `sqrt` không còn dùng để lấy chuỗi đó nữa.

Bằng cách sử dụng `import math as toan`, định danh duy nhất được đưa vào không gian tên hiện hành là bí danh `toan`. Phép tính căn bậc hai được gọi tường minh qua thuộc tính `toan.sqrt(25.0)`, giữ nguyên vẹn biến `sqrt` ban đầu dưới dạng chuỗi.

Kết quả cho thấy `sqrt` vẫn là chuỗi và `toan.sqrt(25.0)` cho 5.0. Cách viết qua tên mô-đun giúp nhìn ra hàm đến từ đâu. Bản thân bí danh cũng là một tên, nên cần chọn `toan` sao cho không đè lên một biến đang dùng.

:::

<!-- /worked-example -->

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 1: Preliminaries.
- Project Jupyter Documentation. *Jupyter and the Future of Interactive Computing*. https://docs.jupyter.org/
- Python Software Foundation. *PEP 668 – Marking Python base environments as "externally managed"*. https://peps.python.org/pep-0668/

</div>

<div class="lecture-exercises-content" aria-label="Bài tập của chương">

## 7. Bài tập thực hành

::: exercise Bài tập 1: Theo dõi trạng thái kernel và thứ tự thực thi ô mã
Một kỹ sư dữ liệu khởi động một phiên làm việc với IPython Kernel hoàn toàn mới và nhập ba ô mã sau vào notebook:

- Ô 1:
  ```python
  x = 10
  ```
- Ô 2:
  ```python
  x = x - 3
  ```
- Ô 3:
  ```python
  x = x * 2 + 5
  ```

Kỹ sư này thực hiện chạy các ô mã theo trình tự sau: Chạy Ô 1 một lần, sau đó chạy Ô 3 hai lần liên tiếp, và cuối cùng chạy Ô 2 một lần.
1. Xác định giá trị cuối cùng của biến `x` trong RAM sau khi kết thúc chuỗi thao tác trên.
2. Giả sử sau đó kỹ sư xóa hoàn toàn Ô 1 khỏi giao diện notebook và chạy lại Ô 2 thêm một lần nữa. Lệnh này có báo lỗi không, và giá trị mới của `x` là bao nhiêu?
3. Nếu khởi động lại kernel hoàn toàn (Restart Kernel) và chỉ chạy duy nhất Ô 2, điều gì sẽ xảy ra?
:::

::: solution Lời giải
1. Lần theo từng bước thực thi trong không gian tên toàn cục:
   - Bước 1 (Ô 1): Khởi tạo biến `x = 10`.
   - Bước 2 (Ô 3 lần thứ nhất): Tính `x = 10 * 2 + 5 = 25`. Giá trị của `x` trong RAM cập nhật thành $25$.
   - Bước 3 (Ô 3 lần thứ hai): Tính `x = 25 * 2 + 5 = 55`. Giá trị của `x` cập nhật thành $55$.
   - Bước 4 (Ô 2): Tính `x = 55 - 3 = 52`. Kết quả cuối cùng trong RAM là $52$.
2. Xóa Ô 1 trên giao diện chỉ làm thay đổi văn bản của tệp tài liệu, hoàn toàn không xóa biến `x` đang thường trực trong tiến trình kernel. Khi chạy lại Ô 2, chương trình không báo lỗi và tiếp tục lấy giá trị hiện tại để tính toán: `x = 52 - 3 = 49`.
3. Khi khởi động lại kernel, toàn bộ trạng thái trong RAM bị xóa sạch. Nếu chỉ bấm chạy Ô 2 mà chưa chạy Ô 1, biểu thức `x - 3` cố gắng truy xuất biến `x` chưa từng tồn tại trong không gian tên mới, dẫn đến lỗi:
   ```text
   NameError: name 'x' is not defined
   ```
   Hiện tượng này minh họa cạm bẫy biến ma khi các ô mã phụ thuộc vào trạng thái ẩn của các phiên chạy trước.
:::

::: exercise Bài tập 2: Kiểm tra tính nhất quán của môi trường qua tập tin requirements.txt
Cho nội dung tệp kê khai phụ thuộc `requirements.txt` như sau:
```text
pandas==2.2.0
numpy>=1.26.0
matplotlib==3.8.2
scipy
```
Hãy viết một hàm Python `phan_tich_yeu_cau(dong_cau_hinh)` nhận vào một chuỗi cấu hình và trả về một tuple gồm `(ten_goi, toan_tu, phien_ban)`. Nếu gói không chỉ định phiên bản, toán tử và phiên bản nhận giá trị `None`. Áp dụng hàm trên cho từng dòng và in ra danh sách các gói có yêu cầu phiên bản cố định chính xác (`==`).
:::

::: solution Lời giải
```python
def phan_tich_yeu_cau(dong):
    dong = dong.strip()
    if not dong or dong.startswith("#"):
        return None
    for toan_tu in ["==", ">=", "<=", ">", "<"]:
        if toan_tu in dong:
            ten, phien_ban = dong.split(toan_tu, 1)
            return ten.strip(), toan_tu, phien_ban.strip()
    return dong.strip(), None, None

du_lieu_req = [
    "pandas==2.2.0",
    "numpy>=1.26.0",
    "matplotlib==3.8.2",
    "scipy"
]

ket_qua = [phan_tich_yeu_cau(dong) for dong in du_lieu_req]
cac_goi_co_dinh = [ten for ten, op, ver in ket_qua if op == "=="]

print("Kết quả phân tích:", ket_qua)
print("Các gói cố định phiên bản:", cac_goi_co_dinh)
```

Kết quả in ra:
- `ket_qua`: `[('pandas', '==', '2.2.0'), ('numpy', '>=', '1.26.0'), ('matplotlib', '==', '3.8.2'), ('scipy', None, None)]`.
- `cac_goi_co_dinh`: `['pandas', 'matplotlib']`.
:::

::: exercise Bài tập 3: Đo lường tỷ lệ dữ liệu khuyết thiếu và doanh thu hợp lệ
Một hệ thống thu thập thông tin đơn hàng trả về danh sách các giao dịch thô như sau:
```python
giao_dich = [
    {"id": "GD01", "so_tien": 150000},
    {"id": "GD02", "so_tien": None},
    {"id": "GD03", "so_tien": 200000},
    {"id": "GD04", "so_tien": 0}
]
```
1. Xác định số lượng giao dịch bị thiếu thông tin số tiền (`None`). Tính tỷ lệ phần trăm dữ liệu khuyết thiếu trên tổng số giao dịch.
2. Tính tổng số tiền thu được và giá trị giao dịch trung bình trên các giao dịch hợp lệ (có số tiền xác định). Lưu ý: Giao dịch có `so_tien = 0` là một giao dịch hợp lệ có phát sinh giá trị bằng không, không phải giá trị thiếu.
:::

::: solution Lời giải
```python
giao_dich = [
    {"id": "GD01", "so_tien": 150000},
    {"id": "GD02", "so_tien": None},
    {"id": "GD03", "so_tien": 200000},
    {"id": "GD04", "so_tien": 0}
]

tong_so = len(giao_dich)
giao_dich_thieu = [g for g in giao_dich if g["so_tien"] is None]
so_thieu = len(giao_dich_thieu)
ty_le_thieu = (so_thieu / tong_so) * 100

gia_tri_hop_le = [g["so_tien"] for g in giao_dich if g["so_tien"] is not None]
tong_doanh_thu = sum(gia_tri_hop_le)
trung_binh = tong_doanh_thu / len(gia_tri_hop_le)

print(f"Số lượng giao dịch thiếu: {so_thieu} ({ty_le_thieu:.1f}%)")
print(f"Tổng doanh thu hợp lệ: {tong_doanh_thu:,} đ")
print(f"Giá trị giao dịch trung bình: {trung_binh:,.2f} đ")
```

Kết quả:
- Số lượng giao dịch thiếu: 1 giao dịch trên tổng số 4 bản ghi, chiếm tỷ lệ $25{,}0\%$.
- Các giao dịch hợp lệ gồm `150000`, `200000` và `0`, tổng cộng có đúng 3 giao dịch hợp lệ.
- Tổng doanh thu hợp lệ bằng $150\,000 + 200\,000 + 0 = 350\,000$ đồng.
- Giá trị trung bình trên 3 giao dịch hợp lệ đạt $\frac{350\,000}{3} \approx 116\,666{,}67$ đồng.
:::




<!-- data-labs:start -->
<section class="data-lab-set" data-lab="lab-01">

<!--@include: ../../../raw_materials/xu-ly-du-lieu/labs/lab-01.md-->

</section>

<!-- data-labs:end -->

## Tài liệu tham khảo

- Wes McKinney. *Python for Data Analysis: Data Wrangling with pandas, NumPy, and Jupyter*, tái bản lần 3. O'Reilly Media, 2022. Chương 1: Preliminaries.
- Project Jupyter Documentation. *Jupyter and the Future of Interactive Computing*. https://docs.jupyter.org/
- Python Software Foundation. *PEP 668 – Marking Python base environments as "externally managed"*. https://peps.python.org/pep-0668/

- IAI. [Notebook thực hành](https://github.com/uet-iai-notebook-labs-2026/notebook-labs-template) và [học liệu thực hành 2627-1](https://courses.iaidev.com/programming-for-data-processing/2627-1/). Các yêu cầu kỹ thuật được đối chiếu, biên tập và bổ sung lời giải cùng dữ liệu minh họa. Phần thích nghi từ học liệu IAI áp dụng giấy phép [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

</div>
