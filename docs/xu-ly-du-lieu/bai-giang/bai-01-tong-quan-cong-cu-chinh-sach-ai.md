---
course: xu-ly-du-lieu
lecture: bai-01-tong-quan-cong-cu-chinh-sach-ai
section: lecture
title: "Tổng quan xử lý dữ liệu & công cụ"
prerequisites: ["bien-kieu", "list", "dictionary"]
lessonStatus: ready
description: "Vị trí của xử lý dữ liệu trong chuỗi giá trị, ngăn xếp Scientific Python, kiến trúc IPython Kernel và kỷ luật làm việc với AI."
---

## 1. Vị thế của Môn học trong Chuỗi giá trị Dữ liệu

### 1.1. Hiện thực dữ liệu trong môi trường sản xuất
Trong các bài giảng lý thuyết nhập môn hoặc trên các diễn đàn công nghệ, người ta thường ca ngợi sức mạnh của các thuật toán Học máy (*Machine Learning*), Trí tuệ Nhân tạo (*AI*) hay những mô hình dự báo phức tạp. Tuy nhiên, một ngộ nhận kinh điển của người mới bắt đầu là tưởng tượng rằng dữ liệu luôn có sẵn dưới dạng các bảng tính tinh tươm, các cột số học ngay ngắn và các nhãn phân loại chuẩn mực.

Thực tế ngành công nghiệp dữ liệu khắc nghiệt hơn rất nhiều. Dữ liệu thô (*raw data*) trong thế giới thực luôn mang trong mình những đặc tính:
- **Phân mảnh và bất đồng bộ**: Một phần nằm trong tệp nhật ký máy chủ (server logs), một phần nằm ở cơ sở dữ liệu quan hệ SQL của bộ phận vận hành, một phần khác lại được gửi về dưới dạng chuỗi JSON lồng nhau từ các cổng thanh toán của đối tác.
- **Nhiễu loạn và suy hao**: Các trường tiền tệ bị lẫn ký tự đơn vị đo lường (như `$`, `VNĐ`, dấu phẩy ngăn phần nghìn), các trường ngày tháng bị đảo lộn giữa định dạng Anh (`DD/MM/YYYY`) và định dạng Mỹ (`MM/DD/YYYY`), các bản ghi bị nhân đôi do mạng chập chờn khi người dùng bấm gửi nhiều lần.
- **Xung đột ngữ nghĩa**: Cùng một trạng thái khách hàng rời bỏ dịch vụ, phòng kinh doanh định nghĩa là "sau 30 ngày không phát sinh đơn hàng", nhưng phòng tài chính lại quy ước là "đã gửi yêu cầu đóng tài khoản".

### 1.2. Quy tắc $80/20$ của ngành Khoa học Dữ liệu
Các cuộc khảo sát thực tế trên toàn cầu đối với các kỹ sư dữ liệu và nhà khoa học dữ liệu đều chỉ ra một tỷ lệ thực tế:

```
+-------------------------------------------------------------+---------+
| Thu thập, Khám phá, Làm sạch, Biến đổi & Thẩm định Dữ liệu  | Mô hình |
|                         (~80% thời gian)                     | (~20%)  |
+-------------------------------------------------------------+---------+
```

Khoảng $80\%$ tổng thời lượng và công sức của một dự án được dành cho việc chuyển hóa dữ liệu từ dạng hỗn loạn ban đầu thành một cấu trúc đáng tin cậy. Chỉ có khoảng $20\%$ thời gian còn lại được dùng để áp dụng thuật toán mô hình hóa hoặc vẽ biểu đồ báo cáo. Nếu tầng xử lý dữ liệu nền tảng làm sai lệch giá trị, toàn bộ các mô hình học máy tinh vi nhất đặt ở tầng trên đều trở thành vô nghĩa theo nguyên lý bất biến: **Rác vào thì Rác ra (*Garbage In, Garbage Out*)**.

Môn học **Lập trình xử lý dữ liệu** được thiết kế nhằm xây dựng cho sinh viên năng lực thực chiến cốt lõi này: biến những luồng dữ liệu bẩn, phân tán thành những tài sản thông tin sạch sẽ, chuẩn mực và có thể kiểm chứng được bằng mã nguồn.

---

## 2. Ngăn xếp Tính toán Khoa học Python (Scientific Python Stack)

### 2.1. Python — Ngôn ngữ "keo dán" của Khoa học Máy tính
Tại sao Python, một ngôn ngữ thông dịch (*interpreted language*) với tốc độ thực thi các vòng lặp thuần túy chậm hơn hàng chục lần so với C hay C++, lại trở thành ngôn ngữ thống trị tuyệt đối trong lĩnh vực dữ liệu và AI?

Câu trả lời nằm ở vai trò **ngôn ngữ keo (*glue language*)**. Các nhà thiết kế hệ thống tính toán đã khéo léo kết hợp hai thế giới:
1. **Tầng người dùng (Cú pháp bậc cao)**: Python cung cấp cú pháp sáng rõ, gần gũi với ngôn ngữ tự nhiên, cho phép nhà nghiên cứu và kỹ sư thử nghiệm ý tưởng nhanh chóng mà không phải bận tâm về việc quản lý con trỏ, cấp phát bộ nhớ thủ công hay biên dịch mã nguồn phức tạp.
2. **Tầng tính toán hạt nhân (Hiệu năng C/Fortran/Rust)**: Bên dưới mui xe (*under the hood*), toàn bộ các thao tác tính toán nặng nề trên ma trận số học đều được giao phó cho các thư viện gốc viết bằng C, C++ hoặc Fortran (như BLAS, LAPACK, OpenBLAS).

Khi ta thực hiện một phép nhân hai mảng trong Python, trình thông dịch Python chỉ đóng vai trò người điều phối gửi chỉ thị xuống khối mã C đã được biên dịch tối ưu cho phần cứng CPU. Nhờ đó, lập trình viên tận hưởng trọn vẹn cả hai ưu điểm: sự linh hoạt trong phát triển mã nguồn và tốc độ tính toán xấp xỉ mã C gốc.

### 2.2. Các trụ cột của Hệ sinh thái Dữ liệu Python

Hệ sinh thái xử lý dữ liệu hiện đại được xây dựng dựa trên ngăn xếp phân tầng chặt chẽ:

```
+-----------------------------------------------------------------------+
|  Ứng dụng Chuyên sâu: Học máy (Scikit-learn), Deep Learning (PyTorch)  |
+-----------------------------------------------------------------------+
|  Trực quan hóa Dữ liệu: Matplotlib, Seaborn                            |
+-----------------------------------------------------------------------+
|  Xử lý Dữ liệu Bảng (Tabular Data): Pandas                             |
+-----------------------------------------------------------------------+
|  Mảng Đa chiều & Đại số Tuyến tính: NumPy                              |
+-----------------------------------------------------------------------+
|  Ngôn ngữ Nền tảng: Python Core & CPython Runtime                      |
+-----------------------------------------------------------------------+
```

- **NumPy (*Numerical Python*)**: Cung cấp cấu trúc mảng nhiều chiều đồng nhất `ndarray` và các hàm toán học vector hóa (*ufuncs*), là nền móng bộ nhớ của mọi thư viện khoa học trong Python.
- **Pandas**: Xây dựng dựa trên NumPy, bổ sung cấu trúc dữ liệu bảng có nhãn hai chiều `DataFrame` và một chiều `Series`, cung cấp các công cụ đọc tệp, ghép bảng, xử lý giá trị khuyết thiếu và tổng hợp dữ liệu nâng cao.
- **Matplotlib & Seaborn**: Cung cấp công cụ trực quan hóa trực giao, từ việc kiểm soát từng thành phần đồ họa theo hướng đối tượng đến các biểu đồ phân tích thống kê đa chiều.

---

## 3. Kiến trúc Môi trường Tính toán & IPython Kernel

### 3.1. Phân định rõ Client và Kernel trong Jupyter Notebook
Nhiều sinh viên thường nhầm lẫn giao diện trang web của Jupyter Notebook hay Google Colab với chính tiến trình đang chạy Python. Trên thực tế, đây là hai thành phần hoàn toàn độc lập giao tiếp với nhau qua kiến trúc Client-Server:

```
[Giao diện Trình duyệt (Client)]
        │   ▲
  JSON  │   │  ZeroMQ Messages
  gửi đi│   │  trả về kết quả
        ▼   │
[Máy chủ Notebook (Server)] ─── IPC ───► [IPython Kernel (Tiến trình Python trong RAM)]
```

1. **Giao diện người dùng (Front-end Client)**: Là trang web hiển thị các ô nhập mã nguồn (cell), văn bản giải thích Markdown và kết quả đồ họa. Nó đóng gói toàn bộ nội dung của phiên làm việc thành một tệp văn bản có định dạng JSON mang phần mở rộng `.ipynb`.
2. **Hạt nhân tính toán (IPython Kernel)**: Là một tiến trình Python độc lập chạy nền trên hệ điều hành. Khi bạn nhấn tổ hợp phím `Shift + Enter` tại một ô mã, nội dung mã nguồn được gửi qua giao thức tin nhắn ZeroMQ tới Kernel. Kernel thực thi đoạn mã trong bộ nhớ RAM và gửi kết quả trả ngược về để trình duyệt hiển thị.

### 3.2. Bẫy Không gian tên Toàn cục (Global Namespace Trap)
Điều quan trọng cần ghi nhớ: **Hạt nhân IPython duy trì một không gian tên toàn cục duy nhất xuyên suốt phiên làm việc**. 

Trạng thái của các biến số trong RAM được quyết định bởi **trật tự bấm chạy thực tế của bạn**, hoàn toàn không phụ thuộc vào vị trí hiển thị từ trên xuống dưới của các ô cell trên màn hình:
- Nếu bạn khai báo `x = 10` ở ô cell số 1, sau đó chạy ô cell số 3 có lệnh `x = x + 5` hai lần liên tiếp, giá trị của `x` trong bộ nhớ RAM lúc này là $20$.
- Nếu một người đồng nghiệp mở cuốn notebook đó ra và bấm chạy tuần tự từ trên xuống dưới, họ sẽ nhận được kết quả `x = 15`. Đây chính là nguyên nhân hàng đầu gây ra hiện tượng **mã chạy được trên máy tôi nhưng lỗi trên máy bạn**.

> [!IMPORTANT] Quy tắc vàng về Tính tái lập (Reproducibility)
> Trước khi nộp bài hoặc bàn giao sản phẩm phân tích dữ liệu, bạn bắt buộc phải thực hiện thao tác: **Restart Kernel and Run All Cells** (Khởi động lại Hạt nhân và Chạy toàn bộ các ô từ đầu đến cuối). Nếu cuốn notebook không thể chạy trơn tru từ dòng 1 đến dòng cuối cùng trên một hạt nhân sạch, mã nguồn đó được coi là chưa hoàn thiện.

---

## 4. Quản trị Dự án Chuẩn mực: Venv, Phụ thuộc & Git

Một kỹ sư dữ liệu chuyên nghiệp không bao giờ cài đặt tất cả các thư viện vào môi trường Python gốc của hệ điều hành. Mỗi dự án phải là một thực thể độc lập và tự khép kín.

### 4.1. Môi trường ảo (`venv`)
Môi trường ảo tạo ra một thư mục biệt lập chứa bản sao nhị phân của Python và khu vực cài đặt các gói thư viện (`site-packages`) riêng biệt cho từng dự án. Điều này giúp ngăn chặn triệt để xung đột phiên bản:

```bash
# Khởi tạo môi trường ảo có tên .venv trong thư mục dự án
python -m venv .venv

# Kích hoạt môi trường ảo
# Trên macOS / Linux:
source .venv/bin/activate
# Trên Windows PowerShell:
.venv\Scripts\Activate.ps1
```

### 4.2. Khóa phiên bản thư viện (`requirements.txt`)
Để bảo đảm bất kỳ ai tải dự án về cũng tái lập được chính xác môi trường làm việc, danh sách các thư viện cùng phiên bản cụ thể cần được xuất ra tệp cấu hình:

```bash
# Xuất danh sách thư viện hiện hành
pip freeze > requirements.txt

# Cài đặt chính xác các thư viện trên một máy mới
pip install -r requirements.txt
```

Bên cạnh đó, tệp `.python-version` ghi rõ phiên bản Python chuẩn (ví dụ `3.12.8`) để các công cụ quản lý như `pyenv` hay `uv` tự động đồng bộ môi trường giữa các thành viên trong nhóm nghiên cứu.

---

## 5. Phương pháp luận Làm việc với Trí tuệ Nhân tạo (AI)

Trong kỷ nguyên của các mô hình ngôn ngữ lớn (LLM), việc cấm đoán sử dụng AI là điều phi thực tế và đi ngược lại xu thế công nghệ. Tuy nhiên, ranh giới giữa một **kỹ sư làm chủ công cụ** và một **người phụ thuộc thụ động** nằm ở nhận thức về các quy ước ngầm.

### 5.1. Nhận diện các lựa chọn quy ước ngầm của AI
Khi bạn đưa cho AI một yêu cầu giản đơn: *"Hãy tính giá phòng trung bình của tập dữ liệu này"*, mô hình ngôn ngữ sẽ lập tức sinh ra một dòng mã như:
```python
avg_price = df["price"].mean()
```
Dòng mã này trông có vẻ hoàn hảo, nhưng thực chất AI vừa âm thầm chọn thay bạn hàng loạt quy ước nghiệp vụ quan trọng mà bạn không hề hay biết:
1. **Xử lý giá trị khuyết thiếu**: Hàm `.mean()` của pandas mặc định bỏ qua các giá trị `NaN` (`skipna=True`). Nếu cột có tới $40\%$ dữ liệu bị thiếu và các ô bị thiếu đó đều thuộc về các căn hộ giá rẻ, kết quả trung bình thu được sẽ bị kéo lệch lên cao một cách sai lầm.
2. **Hiện diện của ngoại lai**: Giá trị trung bình cộng (*Mean*) cực kỳ nhạy cảm với các điểm ngoại lai. Nếu có một căn biệt thự giá 500 triệu đồng/đêm, con số trung bình không còn đại diện cho mức giá phổ biến của thị trường (vốn phải dùng Trung vị - *Median*).
3. **Mẫu số bằng không**: Nếu tập dữ liệu lọc ra bị rỗng, phép tính sẽ trả về `NaN` và có thể làm sập các khối tính toán tài chính phía sau.

### 5.2. Nguyên tắc "Tự phác thảo trước khi hỏi" (Think First, Prompt Later)
Quy trình làm việc chuẩn mực của một nhà phân tích khi cộng tác với trợ lý AI bao gồm 3 bước:
1. **Tự phác thảo logic nghiệp vụ**: Xác định rõ ràng miền giá trị hợp lệ, cách ứng xử với giá trị rỗng, cấu trúc dữ liệu đầu vào và định dạng đầu ra kỳ vọng.
2. **Chỉ định ngữ cảnh và ràng buộc cho AI**: Yêu cầu AI viết mã kèm theo các điều kiện biên tường minh.
3. **Thẩm định và giải thích từng dòng**: Tuyệt đối không bao giờ tích hợp một đoạn mã vào hệ thống nếu bản thân bạn chưa thể giải thích cặn kẽ từng câu lệnh và các tác dụng phụ (*side effects*) của nó.

---

## 6. Hệ thống Bài tập Thực chiến Lab 1

Hệ thống bài tập dưới đây chuyển hóa toàn bộ nội dung thực hành từ `lab-01.ipynb` sang chuẩn mực phân tích dữ liệu độc lập. Mỗi bài tập đều đi kèm tình huống thực tế, các câu hỏi phỏng đoán kiểm chứng cơ chế hạt nhân, và lời giải hai tầng (căn bản và nâng cao).

::: exercise Bài 1.1: Quản lý biến trạng thái và Bẫy thực thi ngoài trật tự (Notebook State)
Trong một cuốn sổ tay phân tích, một sinh viên tạo 3 ô mã liên tiếp như sau:

```python
# Ô mã A:
x = 10

# Ô mã B:
x = x + 5

# Ô mã C:
print(f"Giá trị hiện tại của x là: {x}")
```

**Nhiệm vụ phỏng đoán và giải thích:**
1. **Kịch bản 1**: Giả sử sinh viên bấm chạy ô A một lần, sau đó bấm chạy ô B hai lần liên tiếp, rồi mới bấm chạy ô C. Dự đoán giá trị được in ra ở màn hình console và giải thích cơ chế bộ nhớ bên dưới của IPython Kernel.
2. **Kịch bản 2**: Sinh viên khởi động lại hạt nhân (Restart Kernel) và ngay lập tức bấm chạy ô C trước tiên. Điều gì sẽ xảy ra? Trình thông dịch Python báo lỗi gì?
3. **Đề xuất giải pháp**: Viết lại logic tăng giá trị trên dưới dạng một hàm thuần khiết (*pure function*) để loại bỏ hoàn toàn sự phụ thuộc vào biến trạng thái toàn cục.
:::

::: solution
#### 1. Phân tích Dự đoán & Cơ chế Hạt nhân
- **Kết quả Kịch bản 1**: Giá trị in ra là **`20`**.
  * **Giải thích**: Khi chạy ô A, biến `x` được tạo trong không gian tên toàn cục với giá trị 10. Khi chạy ô B lần thứ nhất, `x` nhận giá trị $10 + 5 = 15$. Khi chạy ô B lần thứ hai, giá trị hiện thời trong RAM là 15 được cộng thêm 5 thành 20. Ô C chỉ đơn thuần đọc giá trị đang lưu trong RAM tại thời điểm nó được kích hoạt.
- **Kết quả Kịch bản 2**: Trình thông dịch sẽ ném ra ngoại lệ:
  `NameError: name 'x' is not defined`
  * **Giải thích**: Khi khởi động lại Kernel, toàn bộ không gian tên bộ nhớ RAM bị xóa sạch. Biến `x` chưa từng được cấp phát và gán giá trị, do đó lệnh truy xuất `x` ở ô C sẽ lập tức thất bại.

#### 2. Lời giải Kỹ thuật Hai tầng

##### Cách 1: Tiếp cận Căn bản & Trực quan (Biến cục bộ tuần tự)
Một cách người ta hay dùng để tránh nhầm lẫn là đặt tên biến phản ánh rõ từng bước biến đổi, không ghi đè biến cũ:

```python
x_goc = 10
x_buoc_1 = x_goc + 5
x_buoc_2 = x_buoc_1 + 5
print(f"Giá trị sau hai bước tăng: {x_buoc_2}")  # 20
```

##### Cách 2: Tiếp cận Nâng cao & Tối ưu (Đóng gói Hàm thuần khiết - Pure Function)
Kỹ sư chuyên nghiệp sẽ đóng gói logic thành hàm độc lập, không làm biến đổi bất kỳ trạng thái toàn cục nào bên ngoài:

```python
def tang_gia_tri(gia_tri_ban_dau: int, so_buoc: int = 1, buoc_nhay: int = 5) -> int:
    """Tính toán giá trị sau một số bước tăng nhất định.
    
    Hàm thuần khiết (Pure function): Cùng đầu vào luôn cho cùng đầu ra,
    hoàn toàn không làm biến đổi bộ nhớ toàn cục.
    """
    assert so_buoc >= 0, "Số bước lặp không được âm!"
    return gia_tri_ban_dau + so_buoc * buoc_nhay

# Chạy thử nghiệm có kiểm chứng
ket_qua = tang_gia_tri(10, so_buoc=2, buoc_nhay=5)
assert ket_qua == 20
print(f"Giá trị tính toán an toàn: {ket_qua}")
```

#### Phân tích bản chất & Bình luận sư phạm
- Việc dùng biến toàn cục lỏng lẻo trong Notebook giống như việc xây nhà trên cát. Chỉ cần vô tình bấm chạy lại một ô cell ở giữa trang, toàn bộ số liệu của các ô bên dưới sẽ bị sai lệch mà không hề phát sinh thông báo lỗi (*Silent Data Corruption*).
- Đóng gói logic vào hàm thuần khiết giúp mã nguồn có thể kiểm thử đơn vị (*Unit Test*), tái sử dụng trong các pipeline lớn và hoàn toàn miễn nhiễm với trật tự bấm phím của người dùng.
:::

---

::: exercise Bài 1.2: Đọc bảng dữ liệu thực tế và Thẩm định cấu trúc (Shape & Dtypes)
Cho một bảng dữ liệu khảo sát thị trường lưu trú được lưu dưới định dạng bảng. Bạn cần tải dữ liệu và thực hiện các bước thẩm định cấu trúc ban đầu:
1. Đọc dữ liệu thành DataFrame.
2. Kiểm tra kích thước hình học của bảng: có bao nhiêu dòng quan sát và bao nhiêu cột đặc trưng?
3. Trích xuất danh sách tên các cột và phân loại kiểu dữ liệu (`dtypes`).
4. Viết các câu lệnh kiểm tra tự động (`assert`) để đảm bảo bảng không bị rỗng và chứa đúng các cột bắt buộc phục vụ phân tích.
:::

::: solution
#### Lời giải Kỹ thuật Hai tầng

```python
import pandas as pd
import numpy as np
from io import StringIO

# Giả lập dữ liệu chỗ ở thực tế
csv_data = """id,ten_cho_o,quan,loai_phong,gia_dem,so_danh_gia
101,Homestay Phố Cổ,Hoàn Kiếm,Entire home/apt,850000,45
102,Phòng Riêng View Hồ,Tây Hồ,Private room,450000,12
103,Studio Cầu Giấy,Cầu Giấy,Entire home/apt,600000,28
104,Căn hộ Vinhomes,Nam Từ Liêm,Entire home/apt,1200000,60
105,Nhà tập thể xưa,Đống Đa,Private room,350000,5
"""
```

##### Cách 1: Tiếp cận Căn bản & Trực quan (Truy xuất thuộc tính cơ bản)

```python
df_cho_o = pd.read_csv(StringIO(csv_data))

# 1. Kiểm tra kích thước
so_dong = len(df_cho_o)
so_cot = len(df_cho_o.columns)
print(f"Bảng có {so_dong} dòng và {so_cot} cột.")

# 2. Xem tên cột và kiểu dữ liệu
print("Danh sách cột:", list(df_cho_o.columns))
print("Kiểu dữ liệu từng cột:\n", df_cho_o.dtypes)
```

##### Cách 2: Tiếp cận Nâng cao & Tối ưu (Đóng gói Hàm Thẩm định Cấu trúc với Assertions)

```python
def tham_dinh_cau_truc_bang(df: pd.DataFrame, cot_bat_buoc: list[str]) -> dict:
    """Thẩm định cấu trúc và tính toàn vẹn ban đầu của bảng dữ liệu."""
    # 1. Chốt chặn an toàn: Bảng không được phép rỗng
    assert not df.empty, "LỖI DỮ LIỆU: Bảng nạp vào bị rỗng hoàn toàn!"
    
    # 2. Chốt chặn an toàn: Phải chứa đầy đủ các cột bắt buộc
    tap_cot_thieu = set(cot_bat_buoc) - set(df.columns)
    assert len(tap_cot_thieu) == 0, f"LỖI CẤU TRÚC: Thiếu các cột bắt buộc: {tap_cot_thieu}"
    
    # 3. Tổng hợp báo cáo kiểm định
    n_rows, n_cols = df.shape
    phan_loai_kieu = df.dtypes.value_counts().to_dict()
    
    return {
        "so_dong": n_rows,
        "so_cot": n_cols,
        "danh_sach_cot": df.columns.tolist(),
        "phan_bo_kieu_du_lieu": {str(k): v for k, v in phan_loai_kieu.items()},
        "kich_thuoc_bo_nho_kb": round(df.memory_usage(deep=True).sum() / 1024, 2)
    }

cot_can_kiem_tra = ["id", "loai_phong", "gia_dem"]
bao_cao = tham_dinh_cau_truc_bang(df_cho_o, cot_can_kiem_tra)
print("Báo cáo thẩm định cấu trúc:\n", pd.Series(bao_cao))
```

#### Phân tích bản chất & Bình luận sư phạm
- Thuộc tính `.shape` trả về một tuple `(n_rows, n_cols)` được tính toán trực tiếp từ cấu trúc khối nhớ bên dưới của mảng hai chiều, nhanh hơn nhiều so với việc gọi `len(df)` kết hợp `len(df.columns)`.
- Việc kiểm tra kích thước bộ nhớ với `memory_usage(deep=True)` là phản xạ cần thiết khi chuyển sang xử lý tệp dữ liệu lớn, giúp nhận biết các cột kiểu chuỗi (`object`) đang tiêu tốn bộ nhớ RAM gấp nhiều lần so với các kiểu số học.
:::

---

::: exercise Bài 1.3: Tính tỷ lệ phân bố có kiểm chứng và Bẫy mẫu số rỗng
Từ bảng dữ liệu chỗ ở trên, ban quản lý muốn xác định tỷ trọng chỗ ở thuộc loại "Căn hộ nguyên căn" (`Entire home/apt`) trên toàn thị trường để đánh giá mức độ chuyên nghiệp hóa của các chủ nhà:

$$
\text{Tỷ lệ} = \frac{\text{Số chỗ ở loại Entire home/apt}}{\text{Tổng số chỗ ở hợp lệ}}
$$

**Yêu cầu kỹ thuật:**
1. Tính toán tỷ lệ trên bằng code Python.
2. Xử lý an toàn trường hợp tập dữ liệu bị rỗng (mẫu số bằng 0) để hàm không ném ra ngoại lệ `ZeroDivisionError` mà trả về kết quả hợp lý.
3. Diễn giải ý nghĩa kinh tế/nghiệp vụ của con số thu được.
:::

::: solution
#### Lời giải Kỹ thuật Hai tầng

##### Cách 1: Tiếp cận Căn bản & Trực quan (Đếm tuần tự với vòng lặp Python)

```python
danh_sach_phong = df_cho_o["loai_phong"].tolist()
so_luong_nguyen_can = 0
tong_so = len(danh_sach_phong)

for lp in danh_sach_phong:
    if lp == "Entire home/apt":
        so_luong_nguyen_can += 1

if tong_so > 0:
    ty_le_cb = so_luong_nguyen_can / tong_so
else:
    ty_le_cb = 0.0

print(f"Số lượng nguyên căn: {so_luong_nguyen_can}/{tong_so}")
print(f"Tỷ lệ (Căn bản): {ty_le_cb:.1%}")
```

##### Cách 2: Tiếp cận Nâng cao & Tối ưu (Vector hóa với Pandas và Kiểm soát Mẫu số)

```python
def tinh_ty_le_loai_phong(df: pd.DataFrame, loai_phong_muc_tieu: str = "Entire home/apt") -> float:
    """Tính tỷ lệ chỗ ở thuộc loại chỉ định với cơ chế bảo vệ mẫu số rỗng."""
    if df.empty or "loai_phong" not in df.columns:
        return 0.0
    
    # 1. Tạo mặt nạ Boolean ở tầng C (nhanh gấp hàng chục lần vòng for)
    mat_na_dung = (df["loai_phong"] == loai_phong_muc_tieu)
    
    # 2. Lấy trung bình của mảng Boolean chính là tỷ lệ phần trăm (True = 1, False = 0)
    # Pandas .mean() tự động xử lý mẫu số an toàn
    ty_le = mat_na_dung.mean()
    
    return float(ty_le)

ty_le_nc = tinh_ty_le_loai_phong(df_cho_o, "Entire home/apt")
print(f"Tỷ lệ nguyên căn (Nâng cao): {ty_le_nc:.2%}")
assert np.isclose(ty_le_nc, 3 / 5)
```

#### Diễn giải Ý nghĩa Nghiệp vụ & Bình luận sư phạm
- **Mẹo toán học vector hóa**: Trong khoa học dữ liệu, một cách người ta hay dùng để tính tỷ lệ của một điều kiện là **lấy trung bình cộng của mặt nạ Boolean** (`mask.mean()`). Vì kiểu Boolean quy ước `True == 1` và `False == 0`, trung bình cộng của dãy số 0 và 1 chính là tổng số lần xuất hiện chia cho kích thước mẫu. Phép tính này thực thi hoàn toàn trong hạt nhân C của NumPy mà không tốn chi phí duyệt từng phần tử.
- **Ý nghĩa thị trường**: Tỷ lệ $60\%$ chỗ ở là căn hộ nguyên căn cho thấy thị trường lưu trú này mang tính chuyên nghiệp và thương mại hóa cao (các nhà đầu tư sở hữu trọn vẹn bất động sản để cho thuê), thay vì mô hình chia sẻ phòng ở truyền thống mang tính gia đình (`Private room` chỉ chiếm $40\%$).
:::

---

::: exercise Bài 1.4: Đóng gói Báo cáo Thị trường Độc lập (Tự làm mở — E1)
Hãy thiết kế một hàm độc lập mang tên `dong_goi_bao_cao_thi_truong(data: pd.DataFrame) -> dict` nhận vào một DataFrame chỗ ở bất kỳ và trả về một từ điển tổng hợp các chỉ số quan trọng phục vụ ban giám đốc:
- `tong_so_cho_o`: Số lượng chỗ ở hợp lệ.
- `gia_trung_binh`: Giá thuê trung bình mỗi đêm (làm tròn đến hàng đơn vị).
- `gia_trung_vi`: Mức giá trung vị (đại diện cho phân khúc phổ thông).
- `ty_le_nguyen_can`: Tỷ lệ phần trăm chỗ ở loại nguyên căn.
- `thong_diep_chinh`: Chuỗi nhận định ngắn gọn về đặc điểm thị trường dựa trên mức chênh lệch giữa giá trung bình và giá trung vị.
:::

::: solution
#### Lời giải Kỹ thuật Chuẩn mực

```python
def dong_goi_bao_cao_thi_truong(data: pd.DataFrame) -> dict:
    """Đóng gói báo cáo phân tích thị trường chỗ ở tự động và toàn diện."""
    if data.empty:
        return {
            "trang_thai": "DU_LIEU_RONG",
            "tong_so_cho_o": 0,
            "gia_trung_binh": 0.0,
            "gia_trung_vi": 0.0,
            "ty_le_nguyen_can": 0.0,
            "thong_diep_chinh": "Không có dữ liệu để phân tích."
        }
    
    n_total = len(data)
    
    # 1. Tính toán các chỉ số thống kê tiền tệ
    gia_mean = data["gia_dem"].mean()
    gia_median = data["gia_dem"].median()
    
    # 2. Tính tỷ lệ loại phòng
    ty_le_nc = (data["loai_phong"] == "Entire home/apt").mean()
    
    # 3. Phân tích độ lệch phân phối (Skewness Insight)
    # Nếu giá trung bình cao hơn trung vị đáng kể (> 15%), thị trường có phân khúc siêu sang kéo lệch
    do_lech_gia = (gia_mean - gia_median) / gia_median if gia_median > 0 else 0
    if do_lech_gia > 0.15:
        thong_diep = (
            f"Giá trung bình ({gia_mean:,.0f} đ) cao hơn trung vị ({gia_median:,.0f} đ) "
            f"{do_lech_gia:.1%}, cho thấy sự hiện diện của phân khúc căn hộ cao cấp kéo lệch thị trường."
        )
    else:
        thong_diep = (
            f"Giá trung bình ({gia_mean:,.0f} đ) bám sát trung vị ({gia_median:,.0f} đ), "
            "thị trường có phân bố giá tương đối đồng đều."
        )
        
    return {
        "tong_so_cho_o": n_total,
        "gia_trung_binh": round(gia_mean, 0),
        "gia_trung_vi": round(gia_median, 0),
        "ty_le_nguyen_can": round(ty_le_nc * 100, 2),
        "thong_diep_chinh": thong_diep
    }

# Chạy thử nghiệm và hiển thị kết quả
bao_cao_kinh_doanh = dong_goi_bao_cao_thi_truong(df_cho_o)
print("BÁO CÁO PHÂN TÍCH THỊ TRƯỜNG TỰ ĐỘNG:")
for k, v in bao_cao_kinh_doanh.items():
    print(f"- {k}: {v}")
```

#### Phân tích bản chất & Bình luận sư phạm
- Báo cáo này áp dụng nguyên tắc **phản biện thống kê giữa Trung bình cộng và Trung vị**. Trong phân tích kinh doanh, không bao giờ báo cáo đơn độc giá trung bình mà phải đặt cạnh trung vị. Việc nhận diện giá trung bình ($690,000$ đ) cao hơn trung vị ($600,000$ đ) tới $15\%$ giúp ban lãnh đạo lập tức nhận ra tác động của căn hộ cao cấp 1.2 triệu đồng ở Nam Từ Liêm kéo lệch chỉ số chung.
:::

---

## 7. Nguồn Tham khảo & Đọc thêm

- Wes McKinney, *Python for Data Analysis*, 3rd Edition — [Chương 1: Preliminaries](https://wesmckinney.com/book/preliminaries) và [Chương 2: Python Language Basics, IPython, and Jupyter Notebooks](https://wesmckinney.com/book/python-basics).
- Tài liệu chính thức về Hạt nhân tương tác: [IPython Architecture and Messaging Protocol](https://ipython.readthedocs.io/en/stable/development/messaging.html).
- Hướng dẫn chuẩn hóa môi trường: [Python Virtual Environments — Real Python](https://realpython.com/python-virtual-environments-a-primer/).
- [Bài giảng tham khảo môn Xử lý dữ liệu (IAI UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-01-tong-quan-va-chinh-sach-ai.html).
