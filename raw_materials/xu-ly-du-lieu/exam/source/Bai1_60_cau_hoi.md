# Bài 1 — Tổng quan môn học, công cụ và chính sách AI

## Ngân hàng 60 câu hỏi

- Đây là ngân hàng ôn theo Bài 1, gồm 40 câu trắc nghiệm và 20 tự luận ngắn, chia 6 đợt; không phải tỷ trọng hay dự báo của một đề thi thật.
- Mỗi câu độc lập. “Phiên sạch” nghĩa là chưa chạy code của câu đó. Lịch chạy cell và trạng thái ban đầu được nêu trong từng câu; không suy thứ tự thực thi từ vị trí cell.
- Với Run all/Restart & Run all, giả định thực thi từ trên xuống và dừng khi gặp lỗi đầu tiên. Lịch chạy cell riêng vẫn được thực hiện đúng thứ tự đề chỉ định, kể cả nếu lần trước báo lỗi.
- Câu môi trường nêu OS/shell và Python được gọi. Không tự thêm lỗi mạng, quyền hoặc tương thích ngoài đề. Các tình huống freeze giả định venv thông thường, không kế thừa gói hệ thống; không cần đoán số/tên các gói phụ thuộc.
- Mỗi trắc nghiệm có đúng một phương án A/B/C/D. Tự luận thường trả lời 1–3 câu hoặc vài dòng lệnh; không yêu cầu viết luận hay pipeline hoàn chỉnh.

## Đợt 1 — B1-001 đến B1-010

7 câu đầu trắc nghiệm; 3 câu cuối tự luận.

### B1-001

Nhóm lấy thêm file giá từ một dịch vụ, xóa các bản ghi trùng rồi nối bảng giá với bảng chỗ ở theo mã. Ba công việc lần lượt thuộc giai đoạn nào?

A. Thu thập → biến đổi → làm sạch.  
B. Thu thập → làm sạch → biến đổi.  
C. Làm sạch → thu thập → biến đổi.  
D. Biến đổi → làm sạch → trực quan.

### B1-002

Bạn mở notebook gốc chỉ có quyền xem và muốn sửa bản của mình. Một cell code có:

```python
print("Chao")
2 + 5
```
Trong Colab mặc định, lựa chọn nào đúng về cách bắt đầu và output khi chạy cell bằng Shift+Enter?

A. Save a copy in Drive; cell chỉ hiển thị 7, không hiện Chao.  
B. Sửa trực tiếp bản gốc chỉ xem; cell in Chao rồi hiển thị 7.  
C. Save a copy in Drive; cell in Chao rồi hiển thị 7.  
D. Save a copy in Drive; cell chỉ in Chao vì 2+5 không có print.

### B1-003

Linux/Bash: máy có Python 3.11.9 và 3.12.3, không có trình quản lý phiên bản. Khi python đang là 3.11.9, nhóm tạo .venv và cài gói; sau đó mới ghi .python-version là 3.12.3 và freeze requirements.txt. Họ chỉ kích hoạt lại venv cũ, không tạo mới. Nhận định nào đúng?

A. Kích hoạt lại đọc .python-version và tự thay Python nền thành 3.12.3.  
B. freeze đã ghi cả Python 3.12.3 vừa nêu trong tệp nên môi trường đã khớp.  
C. Vẫn dùng 3.11.9; ghi tệp rồi kích hoạt lại không đổi Python nền đã dùng để tạo venv.  
D. Chỉ cần cài lại requirements, pip sẽ nâng Python trong venv cũ lên 3.12.3.

### B1-004

Bài về nhà có nhãn mở. Linh dùng AI viết bản nháp hàm, tự phát hiện lỗi, viết lại gần hết và giữ lại ý tưởng từ bản nháp. Khi nộp, cách nào phù hợp?

A. Vẫn khai công cụ, việc đã dùng và cách kiểm chứng dù code được viết lại nhiều.  
B. Ghi Không dùng AI vì không còn nguyên hàm do AI tạo.  
C. Chỉ khai báo nếu giữ nguyên hơn nửa số dòng trong bản nháp.  
D. Chỉ nêu tên công cụ; không cần nêu công việc hay cách kiểm chứng.

### B1-005

Hai dự án trên máy cần hai phiên bản khác nhau của cùng một thư viện. Nhóm muốn làm bài tập lớn trong VS Code mà hạn chế xung đột. Cách nào phù hợp nhất với công cụ được giới thiệu?

A. Đổi tên hai thư mục dự án rồi cài cả hai phiên bản vào một môi trường chung.  
B. Tạo hai requirements.txt nhưng tiếp tục cài mọi thứ vào một môi trường duy nhất.  
C. Dùng hai file notebook trong cùng môi trường; mỗi file tự giữ phiên bản thư viện riêng.  
D. Tạo venv riêng cho từng dự án, cài và ghi phiên bản trong môi trường tương ứng.

### B1-006

Trong lúc làm bài tập lớn tại nhà được mở, nhóm đã dùng AI và khai báo đầy đủ. Tới buổi vấn đáp đóng, một thành viên xin hỏi chatbot một gợi ý về hàm mình đang trình bày. Cách xử lý nào đúng?

A. Được hỏi nếu chỉ xem gợi ý, không chép nguyên câu trả lời.  
B. Được hỏi vì hàm này vốn do AI viết và đã có trong AI_USAGE.md.  
C. Không dùng chatbot trong vấn đáp; đã khai báo vẫn phải tự giải thích.  
D. Được hỏi nếu sau buổi vấn đáp bổ sung prompt vào bản khai báo.

### B1-007

Bài lab mở yêu cầu tính cơ cấu loại phòng. Mai đã tự ước lượng nhóm A khoảng 3/4, hỏi AI bằng tên bảng và cột cụ thể, rồi nhận code có một hàm chưa hiểu. Chuỗi hành động tiếp theo nào đúng quy trình?

A. Chạy code, thấy không lỗi thì khai báo; đọc hàm lạ khi được hỏi vấn đáp.  
B. Hỏi lại AI xem có chắc đúng không, nhận xác nhận rồi coi đã kiểm chứng độc lập.  
C. Khai báo ngay, dùng output làm giá trị dự đoán và không cần kiểm thêm.  
D. Đọc từng dòng, đối chiếu hàm lạ với tài liệu; thử kết quả với ước lượng/cách độc lập; khai báo.

### B1-008

Trong phiên cũ, từng chạy `gia = 40` ở một cell nay không còn trong file. File hiện chỉ có:

Cell A:
```python
tong = gia * 2
```
Cell B:
```python
print(tong)
```
a) Run all trong phiên cũ in gì? b) Restart & Run all lỗi ở đâu? c) Nêu cách sửa để chạy từ phiên sạch và một phép kiểm để biết phép tính đúng yêu cầu “tiền hai đêm, giá 40/đêm”. Trả lời tối đa ba câu hoặc vài dòng.

### B1-009

Một bài mở: nhóm đã khai báo AI, tự viết lại phần lớn code, nhưng chưa hiểu một hàm và chưa đối chiếu số liệu; kết quả báo cáo sau đó bị phát hiện sai. a) Điều gì nhóm đã làm đúng? b) Điều gì vẫn thiếu? c) Nêu trách nhiệm về bản nộp, không suy thêm hình thức kỷ luật. Trả lời tối đa ba câu.

### B1-010

Nhóm đã có một bản code cuối đúng nhưng định gửi duy nhất tệp nén, không tạo repo GitHub private và không giữ các commit trong quá trình làm. Theo Bài 1, còn thiếu điều gì liên quan Git/GitHub? Phân biệt vai trò hai công cụ trong 1–2 câu.

## Đợt 2 — B1-011 đến B1-020

7 câu đầu trắc nghiệm; 3 câu cuối tự luận.

### B1-011

Một bảng thô có giá "$2,400", một ô chưa khai giá và một giá "$1". Trước khi kết luận mức giá của khu vực, nhận định nào phù hợp?

A. Bỏ dấu tiền là đủ; ô thiếu có thể tính như giá 0 để giữ số hàng.  
B. Xóa giá 1 vì nhỏ hơn các giá còn lại là đủ để dữ liệu sạch.  
C. Dùng biểu đồ trước; nếu biểu đồ đọc được thì không cần xem định dạng và thiếu.  
D. Cần làm rõ dạng chuỗi, ô thiếu và kiểm chứng giá lạ trước khi thống kê, diễn giải.

### B1-012

Phiên mới chưa có biến x. Các cell trong file theo thứ tự:

Cell A:
```python
x = 2
```
Cell B:
```python
print(x)
```
Bạn chạy B, rồi A, rồi B, không restart giữa các lần. Hai lần chạy B có kết quả gì?

A. Cả hai lần đều in 2 vì A nằm phía trên.  
B. Lần đầu in 0; lần sau in 2.  
C. Cả hai lần đều NameError vì mỗi cell có bộ biến riêng.  
D. Lần đầu NameError; lần sau in 2.

### B1-013

Linux/Bash: venv A vẫn đang kích hoạt và cwd là B. Bạn đã kiểm tra đường dẫn /du_an_B/.venv/bin/python chính là Python của venv B. Lệnh sau thành công:

```bash
/du_an_B/.venv/bin/python -m pip install pandas
```
Gói được cài vào đâu?

A. Vào A vì môi trường đang kích hoạt luôn thắng đường dẫn Python trong lệnh.  
B. Vào cả A và B vì một nơi được kích hoạt còn một nơi được ghi trong lệnh.  
C. Vào B vì lệnh gọi đích danh Python của B, dù shell vẫn kích hoạt A.  
D. Vào Python hệ thống vì dùng đường dẫn tuyệt đối sẽ bỏ qua venv.

### B1-014

Đang làm quiz có nhãn đóng, Huy định hỏi AI đúng một gợi ý để nhớ khái niệm, rồi tự viết đáp án. Theo chính sách môn, lựa chọn nào đúng?

A. Không dùng AI ở quiz này; lượng trợ giúp nhỏ không thay đổi chế độ đóng.  
B. Được hỏi nếu không chép nguyên câu trả lời của AI.  
C. Được hỏi nếu ghi công cụ vào cuối bài ngay sau quiz.  
D. Được hỏi nếu chỉ yêu cầu khái niệm thay vì giải câu cụ thể.

### B1-015

Venv thông thường không kế thừa gói hệ thống. Sau khi cài pandas và matplotlib, nhóm chạy `python -m pip freeze > requirements.txt`, thấy nhiều dòng hơn hai gói đã gõ tên. Giải thích nào đúng?

A. freeze tự thêm các gói phổ biến chưa được cài để dự án dễ chạy hơn.  
B. Các dòng thêm là mọi phiên bản cũ từng được cài của hai gói.  
C. Các dòng thêm phải đến từ Python hệ thống ngoài venv.  
D. Danh sách có thể gồm các gói phụ thuộc được cài kèm đang hiện diện trong venv.

### B1-016

Một bài nhỏ làm tại nhà không có nhãn mở/đóng. Trước khi làm, Vy định dùng AI viết nháp rồi tự kiểm tra; bạn cùng nhóm nói bài ít điểm nên khỏi hỏi. Cách nào phù hợp?

A. Hỏi giảng viên xác nhận chế độ trước khi dùng AI cho bài này.  
B. Dùng rồi khai báo đầy đủ vì tự kiểm tra sẽ bảo đảm được phép.  
C. Dùng vì bài ở nhà và ít điểm, chỉ hỏi nếu đề ghi đóng.  
D. Nhờ AI viết nháp nhưng không nộp nguyên văn nên không cần xác nhận chế độ.

### B1-017

Nhóm sắp xếp việc học theo cơ cấu điểm và chế độ trong Bài 1. Bản ghi nào đúng?

A. Lab 10%; kiểm tra lớp 20%; giữa kỳ 10%; BTL và vấn đáp 60%; vấn đáp đóng.  
B. Lab 10%; kiểm tra lớp 10%; giữa kỳ 20%; BTL và vấn đáp 60%; vấn đáp mở vì thuộc BTL.  
C. Lab 10% mở; kiểm tra lớp 10% đóng; giữa kỳ 20% đóng; BTL/vấn đáp 60%, mở ở nhà và đóng khi vấn đáp.  
D. Lab 20%; kiểm tra lớp 10%; giữa kỳ 20%; BTL và vấn đáp 50%; vấn đáp đóng.

### B1-018

Bài mở cần nhận xét giá của năm chỗ ở: 40,80, chưa biết,chưa biết,120. AI dùng mean bỏ ô thiếu và báo80. a) 80 tính trên mấy giá, có phải biết được trung bình thực của cả năm không? b) Đề xuất một phép kiểm nhỏ độc lập kèm kết quả mong đợi. Trả lời 1–3 câu; không cần code pandas.

### B1-019

Linux/Bash: đã kích hoạt venv A, python vẫn trỏ A; venv B ở thư mục B/.venv đã có đúng thư viện của dự án B. Bạn chuyển cwd sang B và chạy freeze ghi requirements.txt tại B, rồi gọi đó là bản ghi môi trường B. a) Tệp đang mô tả môi trường nào? b) Sửa thao tác để ghi đúng B. Trả lời 1–3 câu hoặc vài lệnh ngắn.

### B1-020

Trong vấn đáp đóng, An không dùng AI nhưng không giải thích được một phần code mà nhóm đã khai báo trung thực là có AI hỗ trợ khi làm ở nhà. Theo nguồn, hậu quả trực tiếp của phần không giải thích được áp dụng thế nào? Có tự suy ra cả nhóm nhận 0 điểm không? Trả lời 1–2 câu.

## Đợt 3 — B1-021 đến B1-030

7 câu đầu trắc nghiệm; 3 câu cuối tự luận.

### B1-021

Một nhóm đã có bảng giá sạch. Họ tính số chỗ ở theo khu, làm biểu đồ so sánh rồi viết khuyến nghị có nêu giới hạn dữ liệu. Chuỗi công việc sau bảng sạch phù hợp với hướng đi nào?

A. Làm sạch → trực quan → kể chuyện, vì tính số theo khu là sửa dữ liệu.  
B. Biến đổi để tạo thông tin → trực quan hóa → kể chuyện hỗ trợ quyết định.  
C. Biến đổi → kể chuyện → trực quan, vì biểu đồ chỉ có vai trò sau khuyến nghị.  
D. Trực quan → biến đổi → kể chuyện, vì bảng tổng hợp đã là biểu đồ.

### B1-022

Trong Colab, bạn muốn viết hướng dẫn bằng chữ rồi thực thi `!python --version`. Cách hiểu nào đúng về loại cell và dấu !?

A. Dùng Markdown cho cả hướng dẫn và lệnh !; dấu ! chỉ biến dòng thành ghi chú.  
B. Dùng Markdown cho chữ, code cho !; lệnh đổi Python theo .python-version của repo.  
C. Dùng Markdown cho chữ, code cho !; lệnh báo phiên bản Python của máy cá nhân.  
D. Markdown viết hướng dẫn; cell code dùng ! chạy lệnh hệ điều hành, ở đây xem phiên bản Python của Colab.

### B1-023

Repo có requirements.txt tạo từ venv đã kiểm thử, nhưng không ghi phiên bản Python. Máy mới chưa chọn trình thông dịch. Muốn dựng sát môi trường đã kiểm thử, điều kiện nào còn thiếu?

A. Không thiếu gì; các dòng gói==phiên_bản đồng thời cố định Python chạy chúng.  
B. Chỉ chạy pip freeze ở máy mới; lệnh đó sẽ khôi phục môi trường cũ.  
C. Biết và chọn đúng phiên bản Python đã kiểm thử trước khi tạo venv, rồi cài requirements.  
D. Chỉ ghi tên Python trong README; không cần biết phiên bản nào đã dùng để kiểm thử.

### B1-024

Bài mở: nhóm hiểu code AI, khai báo đúng và không giấu sử dụng, nhưng một phép tính nhầm cột làm báo cáo sai. Nhận định nào phù hợp?

A. Không mất điểm nội dung vì đã khai báo công cụ gây ra lỗi.  
B. Chỉ cần sửa AI_USAGE.md để số liệu sai được chấp nhận.  
C. Nhóm vẫn chịu điểm sai của bài; khai báo đúng không bảo đảm số liệu đúng.  
D. Kết quả sai tự chứng minh nhóm đã gian lận ở chế độ đóng.

### B1-025

Linux/Bash, đang ở gốc dự án. Venv `.venv` đã tạo thành công; shell chưa kích hoạt môi trường nào. Lệnh nào kích hoạt venv theo hướng dẫn Bài 1?

A. `source .venv/bin/activate`  
B. `cd .venv`  
C. `python -m pip freeze > requirements.txt`  
D. `python -m venv .venv`

### B1-026

Mẫu nhỏ có 10 bản ghi: loại A có 6, B có 3, C có 1. AI báo A30%, B60%, C10%; tổng 100%. Bạn cần làm gì trước khi chấp nhận?

A. Đối chiếu từng nhóm với phép đếm tay: phải là A60%, B30%, C10%.  
B. Chấp nhận vì tổng 100% là điều kiện đủ cho từng nhóm đúng.  
C. Đổi cách làm tròn để A và B tự trở về số đúng.  
D. Chỉ hỏi lại AI một lần; nếu cùng output thì coi là đối chiếu độc lập.

### B1-027

Một nhóm BTL được phân công thành phố X. Họ định nộp chỉ vài biểu đồ của thành phố Y và bỏ phần review vì cho rằng môn chỉ chấm ảnh cuối. Nhận định nào đúng theo giới thiệu BTL?

A. Có thể đổi thành phố tùy ý; chỉ cần ảnh đẹp là đã thay được pipeline và báo cáo.  
B. Cần làm thành phố được phân công và sản phẩm chạy một lệnh qua QA, KPI, biểu đồ, báo cáo, kèm LLM trên review.  
C. Giữ thành phố X nhưng chỉ nộp ảnh; QA và review được thay bằng output notebook cũ.  
D. Làm đầy đủ pipeline thành phố Y là đủ; phân công trên Canvas chỉ là ví dụ gợi ý.

### B1-028

Phiên mới có cell A `muc = 3` và cell B `print(muc)`. Chạy A một lần, xóa A khỏi file, rồi chạy B; sau đó Restart & Run all trên file chỉ còn B. a) Hai lần chạy B ra sao? b) Xóa cell đã làm gì và chưa làm gì? c) Nêu sửa tối thiểu để file chạy từ phiên sạch. Trả lời tối đa ba câu.

### B1-029

Báo cáo BTL có nhãn mở. Nhóm dùng AI dịch phần thảo luận do nhóm tự viết nhưng khai “Không dùng AI”; một thành viên còn lấy code nhóm khác nhờ AI viết lại để nộp. Nêu vấn đề của từng việc và cách sửa phù hợp trong tối đa ba câu, không tự đặt mức phạt.

### B1-030

Nhóm thực hiện lần lượt: lấy dữ liệu qua API; xử lý ô thiếu và bản ghi trùng theo quy ước; nối bảng rồi tổng hợp; vẽ biểu đồ; viết kết luận có khuyến nghị. Gắn năm giai đoạn tương ứng và nêu vì sao không nên bỏ bước chuẩn bị. Trả lời 1–2 câu.

## Đợt 4 — B1-031 đến B1-040

7 câu đầu trắc nghiệm; 3 câu cuối tự luận.

### B1-031

Sau khi thấy AI viết code nhanh, một sinh viên cho rằng mục tiêu môn là nhớ tên công cụ, không cần hiểu các dòng mình nộp. Nhận định nào phù hợp mục tiêu Bài 1?

A. Dùng hệ sinh thái Python từ thử nghiệm đến pipeline, đồng thời hiểu, chỉ đạo và kiểm chứng công cụ.  
B. Chỉ cần tự gõ mọi dòng; việc chỉ đạo công cụ và kiểm chứng không thuộc mục tiêu môn.  
C. Chỉ cần AI tạo code chạy được; phần hiểu từng dòng chỉ dành cho môn Python trước đó.  
D. Chỉ cần nắm thư viện rời; xây quy trình hoàn chỉnh nằm ngoài phạm vi môn.

### B1-032

Phiên sạch có A, B như sau.

Cell A:
```python
dem = 0
```
Cell B:
```python
dem = dem + 1
print(dem)
```
Chạy A,B,B,A,B theo đúng lịch này, không restart. Ba lần chạy B in gì theo thứ tự?

A. `1; 1; 1`  
B. `1; 2; 1`  
C. `1; 2; 3`  
D. `0; 1; 0`

### B1-033

Lan tải .ipynb đã có output từ Colab. Trên máy cá nhân, phiên Python mới trong VS Code chưa cài pandas. Chạy cell import pandas báo thiếu thư viện, dù output cũ vẫn nhìn thấy. Nhận định nào đúng?

A. File tải lỗi vì .ipynb đúng phải tự chứa bản pandas đã dùng trên Colab.  
B. Chỉ cần nhìn output cũ; nó chứng minh pandas đã sẵn trong phiên local mới.  
C. Chạy lại cell cuối là đủ để lấy lại tất cả biến và import của Colab.  
D. Output cũ không cài thư viện hay tạo phiên sống; dựng/chọn môi trường local rồi chạy lại.

### B1-034

Một bài có nhãn mở. Đâu là tình huống đáp ứng đủ ba trách nhiệm của việc dùng AI?

A. Khai công cụ và prompt nhưng chưa đọc code vì mô hình trả lời rất tự tin.  
B. Tự đọc hiểu code, đối chiếu bằng mẫu tính tay, khai công cụ/công việc/prompt và cách kiểm chứng.  
C. Hiểu và thử mẫu đúng nhưng ghi Không dùng AI vì chỉ nhận gợi ý.  
D. Đọc code và hỏi lại cùng chatbot hai lần, không ghi nội dung đã dùng vào bài.

### B1-035

Linux/Bash: venv dự án đã kích hoạt; python trỏ đúng venv. Có requirements.txt cần cài. Lệnh nào dùng danh sách đó để cài thư viện?

A. `python -m pip freeze > requirements.txt`  
B. `python -m pip install -r requirements.txt`  
C. `python -m pip install pandas`  
D. `python --version`

### B1-036

AI giải thích một hàm lạ và trả cùng kết quả ở hai lần hỏi. Nhóm muốn nói “đã kiểm chứng độc lập”. Bước nào bổ sung bằng chứng phù hợp nhất?

A. Đối chiếu tài liệu chính thức và chạy mẫu nhỏ có đáp án tự tính, hoặc so với cách tính độc lập.  
B. Hỏi lần thứ ba cùng nội dung; ba phản hồi giống nhau là đủ thay ca thử.  
C. Chụp hai phản hồi để thay kiểm thử vì đã có bằng chứng AI nhất quán.  
D. Chỉ đổi tên biến rồi chạy không lỗi; như vậy đã có cách tính khác.

### B1-037

Nhóm có notebook đầy đủ output và khai báo AI, nhưng người chấm chưa thể chạy repo từ đầu trên máy khác. Theo cách chấm BTL được giới thiệu, cách chuẩn bị nào đúng?

A. Giữ output cũ thay việc chạy test vì notebook đã là bản ghi kết quả.  
B. Chỉ cho một thành viên hiểu hết; vấn đáp người đó đại diện toàn nhóm là đủ.  
C. Hoàn thiện repo để chạy test chung và chuẩn bị từng người tự giải thích.  
D. Chỉ bổ sung AI_USAGE.md; khai báo đầy đủ thay được cả test và vấn đáp.

### B1-038

Bạn cùng nhóm chép nguyên thư mục .venv sang máy mới nhưng không chạy được. Repo còn requirements.txt, .python-version và README; các phiên bản ghi trong đó có sẵn để cài/chọn, không có lỗi mạng hay quyền. Nêu quy trình thay thế đáng tin và nội dung README cần có, trong 1–3 câu.

### B1-039

Phân biệt ba trường hợp: (I) dùng một gợi ý AI trong quiz đóng rồi khai báo; (II) dùng AI ở bài mở nhưng giấu; (III) bài mở đã khai báo trung thực nhưng tính sai số liệu. Gọi đúng loại vấn đề của từng trường hợp và nêu vì sao một điều làm đúng không chữa được điều còn sai. Trả lời tối đa ba câu, không tự đặt mức kỷ luật.

### B1-040

Bài lab mở: bạn dùng ChatGPT viết code tính phần trăm theo room_type của ds; prompt đã dùng là “Tính phần trăm số hàng theo room_type của ds, kết quả ở thang 0–100”; phát hiện AI trả tỷ lệ 0–1 thay vì0–100, đã sửa; đối chiếu bằng đếm tay mẫu nhỏ và kiểm tổng gần 100. Viết khai báo AI ngắn theo nội dung mẫu trong nguồn. Không bịa model nếu chưa biết; 2–3 câu là đủ.

## Đợt 5 — B1-041 đến B1-050

6 câu đầu trắc nghiệm; 4 câu cuối tự luận.

### B1-041

Một nhóm có biểu đồ rất rõ nhưng đã tự đổi các giá chưa biết thành 0 và xóa mọi giá nhỏ mà không tra nguồn. Họ kết luận “vì biểu đồ đẹp nên thị trường chắc chắn rẻ”. Cần xem lại điều gì trước hết?

A. Chỉ đổi màu biểu đồ để kết luận phản ánh tốt hơn các mức giá đã sửa.  
B. Quy ước chuẩn bị dữ liệu và bằng chứng cho việc sửa/xóa; biểu đồ rõ không chữa đầu vào sai.  
C. Chỉ chạy lại code vẽ; nếu không báo lỗi thì quy ước thiếu và xóa giá đã được xác nhận.  
D. Chỉ bổ sung câu AI đã xử lý dữ liệu để người đọc tự chịu trách nhiệm.

### B1-042

Bạn được cung cấp output của một bảng giả lập:

```text
shape: (12, 5)
Số dòng theo loại:
Nguyên căn     7
Phòng riêng    3
Phòng chung    2
```
Nhận định nào đúng ở mức đọc kết quả Bài 1?

A. Bảng có 5 hàng,12 cột; Nguyên căn có nhiều dòng nhất.  
B. Bảng có 12 hàng,5 cột; giá Nguyên căn trung bình là 7.  
C. Bảng có 12 hàng,5 cột; Phòng chung nhiều nhất vì nằm cuối bảng đếm.  
D. Bảng có 12 hàng,5 cột; Nguyên căn có nhiều dòng nhất.

### B1-043

Windows/Command Prompt có hai cửa sổ độc lập cùng đứng ở thư mục B. Cửa sổ1 đã kích hoạt venv A, python trỏ A; cửa sổ2 đã kích hoạt venv B, python trỏ B. Cửa sổ1 cài một gói bằng python -m pip install; cửa sổ2 chạy python -m pip freeze. Giả sử không có lỗi cài đặt. Nhận định nào đúng?

A. Cài ở cửa sổ1 vào B; freeze ở cửa sổ2 đọc B vì cả hai cwd đều là B.  
B. Cài ở cửa sổ1 vào cả A và B; freeze B thấy gói vì hai shell cùng máy.  
C. Cài ở cửa sổ1 vào A; freeze ở cửa sổ2 ghi nhận các gói của B mà nó thu được.  
D. Cài ở cửa sổ1 vào A; freeze ở cửa sổ2 tự chuyển sang A để theo lần cài gần nhất.

### B1-044

Bài về nhà có nhãn mở và yêu cầu khai báo theo mẫu. Trong quá trình làm, Phúc thực sự không dùng công cụ AI nào. Điền mục khai báo thế nào?

A. Để trống vì chỉ người có dùng AI mới được ghi mục khai báo.  
B. Ghi rõ Không dùng AI theo mẫu, không cần bịa công cụ hay prompt.  
C. Ghi một chatbot quen thuộc để mục khai báo đủ hình thức.  
D. Ghi Không dùng AI và xin miễn kiểm chứng vì bài hoàn toàn tự viết.

### B1-045

Nhóm dựng lại đúng Python và thư viện như bản đã kiểm thử. Lần chạy mới dùng file đầu vào đã cập nhật số hàng, nên KPI khác trước. Chưa có bằng chứng lỗi code. Kết luận nào hợp lý?

A. Chưa đủ kết luận lỗi; đối chiếu đầu vào và phép tính dù môi trường đã khớp.  
B. KPI khác tự chứng minh requirements.txt đã không có hiệu lực.  
C. Môi trường khớp tự chứng minh KPI mới đúng, không cần xem dữ liệu.  
D. Chỉ cần sửa KPI thành số cũ để giữ tính chạy lại, bỏ qua file đầu vào mới.

### B1-046

Ghi chú Bài 1 nêu lộ trình theo số bài và hai bài kiểm tra giấy 15 phút; các đề tuần 3 được cung cấp lại ghi 20 phút, đề giữa kỳ luyện tập ghi 60 phút. Bản ôn nào đọc đúng nguồn và lộ trình?

A. Nền tảng 1–5; dữ liệu thật 6–8,10; hiện đại 11–14; tuần 9 giữa kỳ,tuần 15 vấn đáp; số bài chính là tuần.  
B. Nền tảng 1–5; dữ liệu thật 6–8,10; hiện đại 11–14; bài 9 giữa kỳ,15 vấn đáp; ghi riêng khác biệt thời lượng mẫu.  
C. Nền tảng 1–3; dữ liệu thật 4–10; hiện đại 11–14; bài 9 giữa kỳ,15 vấn đáp; giữ khác biệt thời lượng.  
D. Nền tảng 1–5; dữ liệu thật 6–8,10; hiện đại 11–14; tự đổi kiểm tra môn thành 20 phút, giữa kỳ thật 60 phút.

### B1-047

Trên Colab, bạn đã lưu bản sao notebook trong Drive, lưu một tệp kết quả vào Drive và chạy cell `ten = "An"`. Chỉ Restart session, không xóa notebook hay tệp, rồi chạy một cell mới `print(ten)`. a) Điều gì xảy ra với lệnh print? b) Mã notebook, output đã lưu và tệp Drive có bị xóa chỉ bởi thao tác restart này không? Trả lời 1–3 câu.

### B1-048

Lab ghi “nên tự gõ, không dùng AI” cho phần khởi động; bài tự làm được gắn nhãn mở. Một bạn từ câu khuyến nghị đó suy ra mọi phần lab đều đóng, nhưng lại xin dùng AI trong quiz đóng vì “chỉ hỏi chút”. Chỉ ra hai suy luận sai và cách xác định quyền dùng trong tối đa ba câu.

### B1-049

Mẫu 20 hàng có A16, B3, C1. Output AI là A80%,B5%,C15%. Hai assert chỉ kiểm A trong khoảng 79–82 và tổng trong99,5–100,5; đều qua. a) Đã kiểm được gì, còn sai gì? b) Viết ba tỷ lệ đúng ở dạng 0–1 và dạng%, rồi nêu kiểm tra bổ sung có kết quả mong đợi. Không viết pandas nâng cao; 1–3 câu là đủ.

### B1-050

Một demo biểu đồ nói “mỗi chấm là một con chim, màu phân biệt loài”; code có groupby("species"). Notebook còn giới thiệu Secrets để dùng API key ở bài sau. a) Nêu ý nghĩa chấm/màu và mức ý nghĩa của việc gộp theo species. b) Có nên dán khóa thật vào code notebook hoặc commit không; hướng được giới thiệu là gì? Không viết mã biểu đồ/groupby/API; tối đa ba câu.

## Đợt 6 — B1-051 đến B1-060

6 câu đầu trắc nghiệm; 4 câu cuối tự luận.

### B1-051

Một sinh viên đã học Tư duy tính toán muốn dùng môn này làm nền cho Học máy/Khoa học dữ liệu. Lựa chọn nào phù hợp vị trí và mục tiêu Bài 1?

A. Dùng môn này để học mô hình dự đoán ngay; dữ liệu sạch được giả định có sẵn.  
B. Dùng Python cơ bản đã có để xây kỹ năng xử lý dữ liệu với hệ sinh thái công cụ, phục vụ các môn sau.  
C. Tập trung dùng thư viện trên bảng mẫu; xử lý dữ liệu thô chỉ cần ở môn Học máy.  
D. Tập trung thao tác Colab; kiến thức Python của môn tiên quyết chưa cần áp dụng.

### B1-052

Phiên sạch: chạy A rồi B. Sau đó sửa nội dung A nhưng chưa chạy lại A, chạy B một lần; cuối cùng chạy A mới rồi B.

Cell A ban đầu:
```python
a = 2
```
Cell B:
```python
print(a * 3)
```
A sau khi sửa:
```python
a = 50
```
Hai lần chạy B sau thời điểm sửa A in gì?

A. `150; 150`  
B. `6; 6`  
C. `6; 150`  
D. `NameError; 150`

### B1-053

Linux/Bash chưa kích hoạt venv; `python3.12` được xác nhận là Python 3.12.3 có sẵn. Repo có .python-version ghi 3.11.9, không có trình quản lý phiên bản. Chạy:

```bash
python3.12 -m venv .venv
```
Venv mới dùng bản Python nào, và điều gì còn cần kiểm?

A. Dùng 3.11.9 vì .python-version luôn được ưu tiên hơn tên executable.  
B. Dùng bản Python mới nhất trên máy vì venv bỏ qua python 3.12.  
C. Chưa có Python cho đến khi pip install -r hoàn tất.  
D. Dùng 3.12.3; phải làm rõ việc khác bản ghi 3.11.9, tệp không tự đổi Python.

### B1-054

Trong bài kiểm tra trên lớp đóng, một bạn không mở chatbot nhưng bật trợ lý AI gợi code và chỉ chấp nhận vài từ gợi ý. Bạn dự định khai báo ở cuối bài. Nhận định nào đúng?

A. Vẫn dùng AI ở chế độ đóng; gợi ý ít hoặc khai báo không cấp quyền.  
B. Được phép vì chỉ chatbot mới tính là AI trong môn.  
C. Được phép vì nhận vài từ chưa đủ thành một đoạn code hoàn chỉnh.  
D. Được phép nếu bản khai cuối bài ghi đúng công cụ đã dùng.

### B1-055

Ở bài mở, AI đề xuất một hàm bạn chưa biết cho bảng ds để đếm loại phòng, nhưng tài liệu thư viện theo phiên bản đang dùng chưa được kiểm tra. Cách nào phù hợp bước đọc hiểu/kiểm chứng?

A. Dùng luôn vì tên hàm nghe đúng, chỉ cần xem AI nói chắc đến mức nào.  
B. Chỉ hỏi AI viết tên hàm khác; có hai tên là đã kiểm được tài liệu.  
C. Chỉ chạy trên toàn dữ liệu, bỏ dự đoán mẫu để tránh thiên lệch người kiểm.  
D. Tra tài liệu chính thức đúng phiên bản, hiểu cách dùng rồi thử mẫu nhỏ với số đếm dự đoán trước.

### B1-056

Một bài làm tại nhà chưa có nhãn. Bạn chỉ muốn AI viết nháp phần mô tả kết quả, không viết code và hứa sẽ tự sửa lời văn. Trước khi dùng, cách nào đúng?

A. Hỏi giảng viên xác nhận chế độ; hỗ trợ viết cũng phải xét quyền dùng và khai báo.  
B. Dùng vì không sinh code nên không thuộc chính sách AI của bài.  
C. Dùng vì làm ở nhà; chỉ xin xác nhận nếu định nộp nguyên bản nháp.  
D. Dùng rồi ghi Không dùng AI nếu tự viết lại các câu trong bản nộp.

### B1-057

Phiên đang có `dem=4` từ một cell đã bị xóa. File hiện chỉ còn hai cell sau.

Cell A:
```python
dem = dem + 1
```
Cell B:
```python
print(dem)
```
Chạy Run all đúng một lần trong phiên hiện tại, rồi Restart & Run all. Nêu kết quả của từng lượt và bước sửa tối thiểu để file chạy được từ đầu, trong 1–3 câu.

### B1-058

Linux/Bash, chưa kích hoạt venv. Repo ghi Python 3.12.3 và đủ requirements/README; `python` hiện là 3.11.9, còn `python3.12` đã xác nhận là 3.12.3. Không có trình quản lý phiên bản. Bạn tạo venv bằng python 3.11, cài đúng requirements và thấy code chạy. a) Phần nào đã làm đúng, điều gì chưa khớp? b) Nêu cách dựng lại khớp bản kiểm thử, trong vài lệnh hoặc tối đa ba câu.

### B1-059

Mục tiêu là trung bình các giá đã biết của bốn chỗ ở:20, chưa biết,40, chưa biết. AI âm thầm thay hai ô thiếu bằng 0 rồi báo15. Code chạy không lỗi và qua một ca thử khác không có ô thiếu. a) Kết quả có đáp ứng câu hỏi không? b) Nêu một kiểm tra nhỏ với kết quả mong đợi và giới hạn của ca thử đã qua. Trả lời 1–3 câu.

### B1-060

Một bạn mới vào lớp hỏi: “Mỗi tuần học/làm lab ở đâu, nộp và xem thông báo bằng gì; trước Bài 2 chuẩn bị gì? Cài local có phải bắt buộc ngay không?” Trả lời tối đa ba câu, gồm việc tìm nhóm và phân biệt mốc khuyến nghị cài môi trường giữa các nguồn.
