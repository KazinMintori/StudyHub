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

<DataDiagram name="effort" />

Khoảng $80\%$ tổng thời lượng và công sức của một dự án được dành cho việc chuyển hóa dữ liệu từ dạng hỗn loạn ban đầu thành một cấu trúc đáng tin cậy. Chỉ có khoảng $20\%$ thời gian còn lại được dùng để áp dụng thuật toán mô hình hóa hoặc vẽ biểu đồ báo cáo. Nếu tầng xử lý dữ liệu nền tảng làm sai lệch giá trị, toàn bộ các mô hình học máy tinh vi nhất đặt ở tầng trên đều trở thành vô nghĩa theo nguyên lý bất biến: **Rác vào thì Rác ra (*Garbage In, Garbage Out*)**.

Môn học **Lập trình xử lý dữ liệu** được thiết kế nhằm xây dựng cho sinh viên năng lực thực chiến cốt lõi này: Biến những luồng dữ liệu bẩn, phân tán thành những tài sản thông tin sạch sẽ, chuẩn mực và có thể kiểm chứng được bằng mã nguồn.

---

## 2. Ngăn xếp Tính toán Khoa học Python (Scientific Python Stack)

### 2.1. Python: Ngôn ngữ "keo dán" của Khoa học Máy tính
Tại sao Python, một ngôn ngữ thông dịch (*interpreted language*) với tốc độ thực thi các vòng lặp thuần túy chậm hơn hàng chục lần so với C hay C++, lại trở thành ngôn ngữ thống trị tuyệt đối trong lĩnh vực dữ liệu và AI?

Câu trả lời nằm ở vai trò **ngôn ngữ keo (*glue language*)**. Các nhà thiết kế hệ thống tính toán đã khéo léo kết hợp hai thế giới:
1. **Tầng người dùng (Cú pháp bậc cao)**: Python cung cấp cú pháp sáng rõ, gần gũi với ngôn ngữ tự nhiên, cho phép nhà nghiên cứu và kỹ sư thử nghiệm ý tưởng nhanh chóng mà không phải bận tâm về việc quản lý con trỏ, cấp phát bộ nhớ thủ công hay biên dịch mã nguồn phức tạp.
2. **Tầng tính toán hạt nhân (Hiệu năng C/Fortran/Rust)**: Bên dưới mui xe (*under the hood*), toàn bộ các thao tác tính toán nặng nề trên ma trận số học đều được giao phó cho các thư viện gốc viết bằng C, C++ hoặc Fortran (như BLAS, LAPACK, OpenBLAS).

Khi ta thực hiện một phép nhân hai mảng trong Python, trình thông dịch Python chỉ đóng vai trò người điều phối gửi chỉ thị xuống khối mã C đã được biên dịch tối ưu cho phần cứng CPU. Nhờ đó, lập trình viên tận hưởng trọn vẹn cả hai ưu điểm: Sự linh hoạt trong phát triển mã nguồn và tốc độ tính toán xấp xỉ mã C gốc.

### 2.2. Các trụ cột của Hệ sinh thái Dữ liệu Python

Hệ sinh thái xử lý dữ liệu hiện đại được xây dựng dựa trên ngăn xếp phân tầng chặt chẽ:

<DataDiagram name="python-stack" />

- **NumPy (*Numerical Python*)**: Cung cấp cấu trúc mảng nhiều chiều đồng nhất `ndarray` và các hàm toán học vector hóa (*ufuncs*), là nền móng bộ nhớ của mọi thư viện khoa học trong Python.
- **Pandas**: Xây dựng dựa trên NumPy, bổ sung cấu trúc dữ liệu bảng có nhãn hai chiều `DataFrame` và một chiều `Series`, cung cấp các công cụ đọc tệp, ghép bảng, xử lý giá trị khuyết thiếu và tổng hợp dữ liệu nâng cao.
- **Matplotlib & Seaborn**: Cung cấp công cụ trực quan hóa trực giao, từ việc kiểm soát từng thành phần đồ họa theo hướng đối tượng đến các biểu đồ phân tích thống kê đa chiều.

---

## 3. Kiến trúc Môi trường Tính toán & IPython Kernel

### 3.1. Phân định bản chất: Tệp mã nguồn `.py` và Sổ tay tính toán `.ipynb`
Bạn có thể viết cùng một phép tính trong tệp `.py` hoặc trong một ô của Jupyter Notebook. Khi chạy, cả hai đều có thể in ra cùng một kết quả. Điểm khác biệt nằm ở **những gì được lưu trong tệp**.

- **Tệp `.py`** là văn bản chứa mã Python và chú thích. Khi chạy bằng lệnh `python tinh_toan.py`, các câu lệnh được thực hiện theo luồng điều khiển của chương trình. Kết quả in ra màn hình không tự được ghi ngược vào tệp mã nguồn. Định dạng này thuận tiện để tổ chức mô-đun, thư viện và các chương trình chạy tự động.
- **Tệp `.ipynb`** là tài liệu JSON chứa danh sách các ô trong trường `cells`. Ô mã có trường `source` lưu mã, `execution_count` ghi số thứ tự thực thi và `outputs` lưu đầu ra. Notebook còn có siêu dữ liệu `metadata` cùng các trường phiên bản định dạng. Nhờ đó, người đọc có thể xem mã, lời giải thích và kết quả đã lưu trong cùng một tài liệu.

<DataDiagram name="notebook-file-formats" />

Trong ví dụ này, `print()` tạo đầu ra văn bản thuộc luồng `stdout`. Với đồ thị, đầu ra có thể chứa dữ liệu ảnh hoặc các dạng hiển thị khác. Notebook có thể lớn và khó đối chiếu thay đổi trên Git khi chứa nhiều đầu ra. Kích thước đó phụ thuộc vào nội dung được lưu, không phải mọi tệp `.ipynb` đều nặng.

Hai tệp mẫu để xem cấu trúc đầy đủ: [Mã Python `tinh_toan.py`](/materials/xu-ly-du-lieu/lec01/tinh_toan.py) và [Notebook `tinh_toan.ipynb`](/materials/xu-ly-du-lieu/lec01/tinh_toan.ipynb). Mở tệp notebook bằng trình soạn thảo văn bản sẽ thấy cấu trúc JSON tương ứng với các trường trong minh họa.

### 3.2. Kiến trúc tương tác ba tầng: Trình duyệt, Máy chủ và IPython Kernel
Khi nhấn `Shift + Enter` trong Jupyter Notebook trên trình duyệt, mã không được thực thi ngay trong trang web. Yêu cầu chạy đi qua máy chủ để tới một tiến trình Python riêng, gọi là **kernel**. Ba thành phần và hai kênh trao đổi được ghép trong cùng một sơ đồ dưới đây.

<DataDiagram name="jupyter" />

Cần phân biệt **tệp notebook trên đĩa** với **trạng thái tính toán trong RAM**. Lưu notebook có thể giữ lại mã và đầu ra đang hiển thị, nhưng không tự lưu toàn bộ các đối tượng Python đang tồn tại trong kernel. Sự khác biệt này giải thích vì sao một kết quả vẫn xuất hiện trên trang dù kernel vừa được khởi động lại.

### 3.3. Minh họa cơ chế chạy Cell và Chỉ số Thực thi `In [ ]`
Nhãn bên cạnh một ô mã giúp nhận biết việc thực thi của ô đó:

- **`In [ ]`**: Ô không có số thứ tự thực thi đang hiển thị. Chỉ nhìn nhãn này không thể kết luận một tên biến có tồn tại trong kernel hay không, vì tên đó có thể đã được tạo bởi một ô khác.
- **`In [*]`**: Ô đang chờ hoặc đang được xử lý. Kernel có thể đang tính toán, đọc dữ liệu hoặc chờ phản hồi mạng.
- **`In [n]`**: Số thứ tự của lần thực thi gần nhất được ghi nhận cho ô. Nhãn này phản ánh thứ tự chạy, không phản ánh vị trí ô trên trang và cũng không bảo đảm lần chạy đã hoàn tất mà không có lỗi.

Xét một phiên làm việc bắt đầu với kernel sạch. Tài liệu có ba ô, nhưng người dùng **chạy ô 1 trước, chạy ô 3 hai lần rồi mới chạy ô 2**. Hai góc nhìn dưới đây cùng mô tả phiên làm việc đó. Màu của mỗi ô được giữ nguyên để đối chiếu giữa vị trí trong tài liệu và lịch sử thực thi.

<NotebookExecution />

Ô 2 in ra `20` vì lần chạy của nó xảy ra sau hai lần cộng thêm `5` ở ô 3. Nhãn `In [3]` cạnh ô 3 chỉ ghi lần chạy gần nhất của ô này. Lần chạy trước đó mang nhãn `In [2]` không còn hiện cạnh ô. Đầu ra của `print(x)` là dòng văn bản `20`, không mang nhãn `Out [4]`. Nhãn `Out [n]` thường đi với kết quả của một biểu thức được IPython hiển thị tự động.

Khi lưu notebook, các nhãn và đầu ra này có thể được giữ lại trong tệp. Khi mở lại tài liệu, hãy xác định kernel hiện tại đã chạy những ô nào trước khi dùng các nhãn đã lưu để suy luận về RAM.

### 3.4. Bẫy Không gian tên Toàn cục (Global Namespace Trap)
Ví dụ vừa rồi cho thấy trạng thái của `x` phụ thuộc vào lịch sử thực thi. Các ô mã trong cùng một kernel sử dụng chung không gian tên. Biến, hàm và các đối tượng được tạo ra có thể tiếp tục được dùng ở những lần chạy sau cho đến khi bị thay đổi, bị xóa hoặc kernel kết thúc.

#### 1. Cơ chế trạng thái tích lũy trong RAM
Mỗi lần chạy `x = x + 5`, Python lấy giá trị hiện tại của `x` để tính giá trị mới rồi gán lại. Vì vậy, chạy lặp một ô có thể làm kết quả thay đổi ngay cả khi nội dung ô vẫn giữ nguyên. Di chuyển ô hoặc sửa văn bản trên trang cũng không tự thực thi lại mã và không tự hoàn tác trạng thái trong RAM.

Khi gỡ lỗi, hãy lần theo thứ tự thực thi và các lệnh gán trước đó. Đọc từ trên xuống dưới chỉ phản ánh đúng quá trình tính toán khi các ô thực sự đã được chạy theo thứ tự ấy trên một trạng thái khởi đầu xác định.

#### 2. Cạm bẫy biến ma (Ghost Variable Trap)
Giả sử bạn chạy một ô tạo biến `du_lieu_tam = tai_bang()`, rồi dùng biến đó để vẽ biểu đồ. Sau đó, bạn xóa ô tạo biến khỏi tài liệu. **Xóa ô khỏi notebook không xóa biến đã được tạo trong kernel**, nên các ô còn lại vẫn có thể chạy trong phiên hiện tại.

Người nhận notebook sẽ gặp vấn đề khi chạy trên một kernel sạch. Nếu không còn câu lệnh tạo `du_lieu_tam`, lần sử dụng tên đó sẽ báo lỗi:

```text
NameError: name 'du_lieu_tam' is not defined
```

Để phát hiện sự phụ thuộc vào trạng thái cũ, trước khi nộp bài hoặc chia sẻ notebook, hãy dùng thao tác **Restart Kernel and Run All Cells** trong menu quản lý kernel. Thao tác này tạo lại trạng thái tính toán và chạy các ô theo thứ tự tài liệu. Nếu thiếu bước tạo biến, lỗi sẽ xuất hiện thay vì bị trạng thái của phiên trước che khuất. Khả năng tái lập kết quả còn phụ thuộc vào dữ liệu đầu vào, phiên bản thư viện và các nguồn ngẫu nhiên của chương trình.

---

## 4. Quản trị Dự án Chuẩn mực: Môi trường ảo `venv` và Kiểm soát Phụ thuộc

Một kỹ sư dữ liệu chuyên nghiệp không bao giờ cài đặt thư viện bừa bãi vào môi trường Python gốc của hệ điều hành. Mỗi dự án nghiên cứu hoặc sản phẩm phân tích phải là một không gian độc lập và tự khép kín.

### 4.1. Vì sao người ta nghĩ ra Môi trường ảo (`venv`)?
Để hiểu được giá trị của môi trường ảo, trước hết ta cần nắm được cách thức tổ chức mặc định của Python trên máy tính.

Khi bạn cài đặt Python lên hệ điều hành, hệ thống chỉ cung cấp một thư mục lưu trữ duy nhất dành cho các gói phần mềm bên thứ ba, thường mang tên `site-packages` nằm sâu trong thư mục cài đặt gốc. Mỗi khi bạn gõ lệnh `pip install <ten-goi>`, trình quản lý gói sẽ tải mã nguồn về và ghi thẳng vào thư mục dùng chung này. Nếu gói phần mềm đó đã tồn tại một phiên bản trước đó, lệnh cài đặt mới sẽ âm thầm ghi đè và xóa bỏ phiên bản cũ.

Cách thiết kế dùng chung một chiếc tủ đồ này nhanh chóng bộc lộ hạn chế khi một lập trình viên phải phụ trách nhiều dự án cùng lúc. Các kỹ sư nhận thấy rằng: Mỗi dự án phần mềm có chu kỳ phát triển, đối tác công nghệ và ràng buộc thư viện hoàn toàn khác nhau. Một dự án không thể bị phụ thuộc hoặc làm hỏng các dự án khác chỉ vì một bản nâng cấp thư viện.

Môi trường ảo (*virtual environment* hay `venv`) ra đời như một **chiếc hộp cách ly (sandbox)** độc lập cho từng dự án. Về mặt bản chất kỹ thuật, `venv` thực chất chỉ là một thư mục con nằm ngay bên trong dự án của bạn (thường đặt tên là `.venv`), bao gồm:
1. **Bản sao hoặc liên kết biểu tượng (*symlink*)**: Trỏ tới tệp thực thi `python` của hệ thống.
2. **Thư mục `site-packages` riêng biệt**: Chứa toàn bộ các thư viện được cài đặt riêng cho dự án đó, hoàn toàn cách ly với phần còn lại của máy tính.
3. **Các kịch bản kích hoạt (`activate`)**: Có nhiệm vụ tạm thời điều chỉnh biến môi trường hệ thống `$PATH`, ưu tiên trỏ các lệnh `python` và `pip` vào bên trong thư mục `.venv`.

Khi bạn làm việc xong hoặc muốn dọn dẹp dự án, bạn chỉ cần xóa bỏ thư mục `.venv` đó là toàn bộ thư viện liên quan biến mất sạch sẽ, không để lại bất kỳ rác thải hay ảnh hưởng tiêu cực nào lên hệ điều hành.

### 4.2. Ba tình huống thực tế hằng ngày nếu không sử dụng `venv`
Nếu không duy trì kỷ luật tạo môi trường ảo, bạn sẽ thường xuyên đối mặt với ba tình huống trớ trêu sau đây trong công việc hằng ngày:

#### 1. Bi kịch xung đột phiên bản giữa các dự án (Dependency Collision)
- **Bối cảnh**: Bạn đang duy trì một hệ thống báo cáo bán hàng cho doanh nghiệp xây dựng từ năm ngoái (Dự án A), sử dụng thư viện `pandas` phiên bản cũ `1.5.3`. Sang học kỳ này, bạn bắt đầu làm đồ án môn Xử lý dữ liệu (Dự án B) cần sử dụng các tính năng tối ưu hóa kiểu dữ liệu chuỗi mới nhất của `pandas 2.2.0`.
- **Diễn biến**: Do không dùng môi trường ảo, bạn mở terminal lên và gõ `pip install pandas==2.2.0`. Lệnh này lập tức gỡ bỏ bản 1.5.3 và chép đè bản 2.2.0 vào hệ thống máy tính.
- **Hệ quả**: Dự án B chạy rất tốt, nhưng ngày hôm sau khi công ty yêu cầu bạn xuất báo cáo định kỳ cho Dự án A, chương trình Dự án A lập tức ném ra hàng loạt lỗi màu đỏ `ImportError` và gãy đổ chức năng vì nhiều cú pháp cũ đã bị loại bỏ ở phiên bản mới. Bạn rơi vào bẫy bế tắc: Nâng cấp mã nguồn Dự án A thì mất nhiều ngày kiểm thử lại toàn bộ hệ thống, trong khi hạ cấp phiên bản về `1.5.3` thì đồ án Dự án B không thể tiếp tục thực hiện.

#### 2. Ô nhiễm và làm tê liệt Python của Hệ điều hành (Corrupting System Python)
- **Bối cảnh**: Trên các hệ điều hành phổ biến dành cho lập trình viên như Ubuntu, Debian hay macOS, rất nhiều công cụ quản trị hệ thống cốt lõi (chẳng hạn công cụ cài đặt gói `apt`, trình quản lý mạng, các dịch vụ tường lửa hay tiện ích đồ họa) được viết và vận hành bằng chính phiên bản Python mặc định của hệ điều hành.
- **Diễn biến**: Khi gặp thông báo lỗi thiếu quyền cài đặt thư viện, người mới học thường gõ thêm quyền quản trị viên tối cao: `sudo pip install <ten-goi>`.
- **Hệ quả**: Trình quản lý gói `pip` với quyền root sẽ ghi đè các thư viện nền tảng của hệ điều hành bằng các phiên bản thử nghiệm của ngành khoa học dữ liệu. Sự bất tương thích này có thể khiến các công cụ quản lý hệ thống bị tê liệt, máy tính không thể cập nhật phần mềm, thậm chí mất hoàn toàn giao diện đồ họa khi khởi động lại máy. Đây là lý do các hệ điều hành hiện đại đã áp dụng tiêu chuẩn bảo vệ nghiêm ngặt (PEP 668), từ chối lệnh `pip install` ở môi trường ngoài và yêu cầu người dùng bắt buộc phải sử dụng môi trường ảo.

#### 3. Mất khả năng đóng gói và tái lập môi trường ("Chạy trên máy tôi nhưng sập trên máy bạn")
- **Bối cảnh**: Sau một thời gian học tập, máy tính của bạn đã được cài đặt tự do hàng trăm thư viện khác nhau phục vụ từ làm web, lập trình game, trí tuệ nhân tạo đến phân tích dữ liệu. Đến hạn nộp bài tập lớn, bạn gõ lệnh xuất danh sách phụ thuộc `pip freeze > requirements.txt` để gửi cho bạn cùng nhóm.
- **Diễn biến**: Tệp văn bản sinh ra chứa một danh sách khổng lồ gồm hơn 180 thư viện với các phiên bản hỗn tạp, trong đó chứa cả những gói chỉ hoạt động trên một hệ điều hành nhất định hoặc đòi hỏi driver phần cứng đặc thù của riêng máy bạn.
- **Hệ quả**: Khi giảng viên hoặc bạn cùng nhóm tải mã nguồn về và gõ `pip install -r requirements.txt`, quá trình cài đặt liên tục báo lỗi biên dịch, làm tràn bộ nhớ ổ đĩa hoặc cài đặt hàng loạt thư viện thừa thãi không liên quan. Nguy hiểm hơn, dự án có thể thiếu mất tính năng cốt lõi do bạn quên mất tên gói thư viện thực sự cần dùng.

### 4.3. Quy trình thực hành chuẩn mực với `venv`
Một quy trình làm việc chuyên nghiệp luôn bắt đầu bằng việc thiết lập môi trường biệt lập ngay khi khởi tạo dự án:

```bash
# Bước 1: Điều hướng vào thư mục dự án và khởi tạo môi trường ảo có tên .venv
python -m venv .venv

# Bước 2: Kích hoạt môi trường ảo
# Trên macOS / Linux:
source .venv/bin/activate
# Trên Windows PowerShell:
.venv\Scripts\Activate.ps1
```

Khi kích hoạt thành công, dấu nhắc lệnh trên terminal sẽ hiển thị thêm tiền tố `(.venv)`, báo hiệu cho bạn biết mọi lệnh gọi `python` hay `pip` từ lúc này trở đi đều được gói gọn an toàn bên trong chiếc hộp cát của dự án.

```bash
# Bước 3: Cài đặt các thư viện cần thiết cho dự án
pip install pandas numpy matplotlib

# Bước 4: Khóa danh sách phụ thuộc ra tệp cấu hình
pip freeze > requirements.txt
```

Khi một thành viên khác trong nhóm nghiên cứu nhận dự án hoặc khi triển khai lên máy chủ, họ chỉ cần thực hiện hai thao tác tái lập đơn giản:
```bash
# Tạo môi trường ảo sạch trên máy mới và kích hoạt
python -m venv .venv
source .venv/bin/activate  # Hoặc .venv\Scripts\Activate.ps1 trên Windows

# Cài đặt chính xác các phiên bản thư viện đã được khóa
pip install -r requirements.txt
```

Bên cạnh đó, tệp `.python-version` ghi rõ phiên bản Python chuẩn (ví dụ `3.12.8`) để các công cụ quản lý như `pyenv` hay `uv` tự động đồng bộ môi trường giữa các thành viên trong nhóm nghiên cứu.

> [!TIP] Nguyên tắc vàng khi làm việc với Git
> Thư mục `.venv` có thể chứa hàng chục nghìn tệp tin với dung lượng hàng trăm megabyte. Tuyệt đối **không bao giờ đưa thư mục `.venv` lên kho lưu trữ Git**.
>
> Bạn chỉ cần thêm dòng chữ `.venv/` vào tệp `.gitignore`. Kho lưu trữ mã nguồn chỉ cần lưu trữ mã lệnh của bạn và tệp kê khai `requirements.txt`. Bất kỳ ai tải mã nguồn về đều có thể tự động dựng lại môi trường nguyên bản chỉ bằng một dòng lệnh.

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
2. **Hiện diện của ngoại lai**: Giá trị trung bình cộng (*Mean*) rất nhạy cảm với các điểm ngoại lai. Nếu có một căn biệt thự giá 500 triệu đồng/đêm, con số trung bình không còn đại diện cho mức giá phổ biến của thị trường (vốn phải dùng Trung vị - *Median*).
3. **Mẫu số bằng không**: Nếu tập dữ liệu lọc ra bị rỗng, phép tính sẽ trả về `NaN` và có thể làm sập các khối tính toán tài chính phía sau.

### 5.2. Nguyên tắc "Tự phác thảo trước khi hỏi" (Think First, Prompt Later)
Quy trình làm việc chuẩn mực của một nhà phân tích khi cộng tác với trợ lý AI bao gồm 3 bước:
1. **Tự phác thảo logic nghiệp vụ**: Xác định rõ ràng miền giá trị hợp lệ, cách ứng xử với giá trị rỗng, cấu trúc dữ liệu đầu vào và định dạng đầu ra kỳ vọng.
2. **Chỉ định ngữ cảnh và ràng buộc cho AI**: Yêu cầu AI viết mã kèm theo các điều kiện biên tường minh.
3. **Thẩm định và giải thích từng dòng**: Tuyệt đối không bao giờ tích hợp một đoạn mã vào hệ thống nếu bản thân bạn chưa thể giải thích cặn kẽ từng câu lệnh và các tác dụng phụ (*side effects*) của nó.

---

## 6. Hệ thống Bài tập Tự luyện {#bai-tap}

Bài tập củng cố tri thức của bài học này được tích hợp xuyên suốt từng mục lý thuyết trong Notes. Để luyện tập thêm các bài toán thực hành chuyên sâu và làm quen với các tình huống thực tế, bạn có thể tham khảo chuyên trang Bài tập của môn học hoặc chuyển sang tab [**Bài tập**](#bai-tap) ở đầu trang.

::: tip Chuyển sang Tab Bài tập
Bấm vào tab **Bài tập** trên thanh điều hướng bài giảng ở đầu trang để tra cứu nhanh chuyên trang bài tập của môn học.
:::

## 7. Nguồn Tham khảo & Đọc thêm

- [Định dạng tệp notebook và các kiểu đầu ra (Jupyter nbformat)](https://nbformat.readthedocs.io/en/latest/format_description.html).
- [WebSocket và kênh trao đổi với kernel (Jupyter Server)](https://jupyter-server.readthedocs.io/en/latest/developers/websocket-protocols.html).

- Wes McKinney, *Python for Data Analysis* (tái bản lần 3): [Chương 1: Preliminaries](https://wesmckinney.com/book/preliminaries) và [Chương 2: Python Language Basics, IPython, and Jupyter Notebooks](https://wesmckinney.com/book/python-basics).
- Tài liệu chính thức về Hạt nhân tương tác: [IPython Architecture and Messaging Protocol](https://ipython.readthedocs.io/en/stable/development/messaging.html).
- Hướng dẫn chuẩn hóa môi trường: [Python Virtual Environments (Real Python)](https://realpython.com/python-virtual-environments-a-primer/).
- [Bài giảng tham khảo môn Xử lý dữ liệu (IAI UET)](https://courses.iaidev.com/programming-for-data-processing/2627-1/lecture-01-tong-quan-va-chinh-sach-ai.html).
