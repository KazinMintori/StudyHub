# BÀI 6 — ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM

Dùng cùng [file câu hỏi](<D:/LTXLDL_GK/output/bai6/Bai6_72_cau_hoi.md>).

## Nguồn đã đọc và phạm vi

- **BG:** [bai-06-ket-noi-truy-xuat-du-lieu.md](<D:/LTXLDL_GK/Bài 6/bai-06-ket-noi-truy-xuat-du-lieu.md>), toàn văn. Chính tệp ghi đây là ghi chú tóm lược bằng lời riêng, không phải bản chép nguyên văn; vì vậy ngân hàng dùng cùng notebook, không coi tệp này là toàn bộ bài giảng gốc.
- **NB:** [lecture_06.ipynb](<D:/LTXLDL_GK/Bài 6/lecture_06.ipynb>), đủ 78 ô, gồm hướng dẫn, code, assert, bài tập, tự học. Số ô tham chiếu tính từ 0 trong JSON notebook.
- **LAB:** [lab_06.ipynb](<D:/LTXLDL_GK/Bài 6/lab_06.ipynb>), đủ 37 ô, gồm TODO, assert và hai bài tự làm. Không tuyên bố notebook còn TODO đã được chạy trọn vẹn.
- **GK:** [Kiểm tra giữa kỳ luyện tập](<D:/LTXLDL_GK/Bài_kiểm_tra/2627I_UET.DSE2049 - Kiểm tra giữa kỳ (luyện tập) (1).pdf>), đã đọc đủ trong cùng cuộc làm việc; đọc lại trực tiếp câu 14–16 và 24 để hiệu chỉnh mã/NA, LEFT JOIN/WHERE, HTTP và COUNT/WHERE/HAVING. Đây là chuẩn suy luận phổ biến, không phải dự báo chắc chắn đề thật.
- **AI5, DS1, DS2:** [LTXLDL_AI_5.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_5.pdf>), [LTXLDL_DS_1.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_1.pdf>), [LTXLDL_DS_2.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_2.pdf>), đã đọc đầy đủ trong cùng cuộc làm việc, dùng cách hỏi tình huống và nhiễu có cơ chế của Nguyễn Tuấn Phong.
- **AI1, AI2:** [LTXLDL_AI_1.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_1.pdf>), [LTXLDL_AI_2.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_2.pdf>), đã đọc đủ trong cùng cuộc làm việc; chỉ tham khảo bổ trợ cách diễn đạt/suy luận. Hai tệp ghi tác giả Đào Việt Anh, không gán nhầm tác giả.

Không thiếu nguồn được yêu cầu. Không tải dữ liệu Santiago, không gọi API thật để giải hoặc chốt đáp án, không tuyên bố đọc toàn bộ sách/website được liên kết. Bảng nhỏ, file nhỏ, phản hồi và mô tả tham số cần dùng đều có trong câu. Không thêm window function, SQL nâng cao, quản trị CSDL, OAuth hoặc thiết kế API.

**Ranh giới ưu tiên:** đọc file nén, parse_dates, API lịch sử và year(date) nằm trong phần chính vì LAB dùng trực tiếp. Chunksize, tổng hợp qua khối, benchmark, EXPLAIN, API key/giới hạn truy cập nằm ở phần bổ sung. Top-k kèm tên listing là LAB tự làm 2 nên đặt ở MR12, có quy ước khóa và xử lý đồng hạng rõ. Tình huống tháng khác vẫn dùng cùng cơ chế API lịch sử/lưu snapshot đã hỏi trong phần chính, không đòi nhớ số đo tháng thật.

## Giả định và quy ước kỹ thuật

- Notebook chỉ định pandas 3.0.3, DuckDB 1.5.5, PyArrow 25.0.1. Môi trường chạy thực tế: **pandas 3.0.1, DuckDB 1.5.5, PyArrow 25.0.1, Requests 2.34.2, NumPy 2.3.5, Python 3.12.14**. Không tuyên bố đã chạy pandas 3.0.3.
- Mỗi câu độc lập, đã có `import pandas as pd`, `import numpy as np`, `import duckdb`, `import requests`, `import json` và `from io import StringIO` khi cần. File CSV/Parquet/JSON trong câu có đúng nội dung/bảng được cung cấp; kiểm chứng dùng StringIO hoặc file nhỏ riêng.
- Mỗi hàng được nói rõ là listing, review, ngày hoặc nhóm. Mã chuỗi khác số đo; giá trị thiếu số trong DataFrame dùng np.nan và float64. Trong các ví dụ đăng ký DataFrame với DuckDB, thiếu trở thành NULL; không mở rộng kết luận đó sang mọi NaN tạo trực tiếp trong SQL.
- Dùng ngữ nghĩa DuckDB. Trừ câu có khóa nhóm thiếu ghi rõ, các khóa nhóm/ghép không thiếu. Khi so pandas/SQL có khóa nhóm thiếu, phải giữ cùng dropna. Nếu hỏi thứ tự, đề có ORDER BY hoặc danh sách nhãn; không chấm nguyên văn thông báo lỗi hay toàn query plan.
- Khi hỏi kiểu chuỗi, nhận dtype chuỗi logic phù hợp; không bắt mọi backend lưu chuỗi giống hệt. Datetime chỉ dùng đọc ngày, lấy năm và khóa ngày như LAB, không mở rộng rolling/resample hay chuyển múi giờ chuyên sâu.
- Tham số API được cho bảng/mô tả trong câu hoặc trích từ nguồn, không cần học thuộc tên dài. Các mã HTTP/nội dung đề cho là dữ kiện cố định; không suy mọi tham số lạ đều có cùng mã lỗi. Mô phỏng chỉ kiểm luồng xử lý cục bộ.
- Chấp nhận kết quả số thực sai số tuyệt đối 1e-12 hoặc dạng phân số đúng, trừ câu ghi mức khác. NaN/NULL được kiểm bằng isna/IS NULL; không so bằng NaN.
- TN đúng duy nhất một đáp án, có thể chấm 1 điểm. TL có thang 2 hoặc 3 điểm riêng; chấp nhận truy vấn/cách đọc tương đương đáp ứng đúng schema, tập hàng, mẫu số và ý nghĩa.

## Cách dùng đáp án

TN giải thích đủ bốn lựa chọn; mỗi nhiễu ứng với lỗi suy luận cụ thể. TL có đáp án ngắn, code/SQL và điểm thành phần. Kxx tra ở danh mục trong file câu hỏi. Nhãn nhóm, bẫy và độ khó chỉ đặt trong file đáp án; code kiểm chứng là ca riêng cho từng câu, không dùng API trực tiếp hay snapshot thật thay đổi.

## Đợt 1

### Câu trọng tâm

#### B6-001

**Đáp án: B.**

- A sai: tưởng astype(str) khôi phục văn bản mã ban đầu.
- B đúng: pandas suy luận id thành số khi đọc; đổi sang chuỗi sau đó chỉ đổi các số đã mất số 0 đầu.
- C sai: bỏ qua phép astype(str), trả số thay chuỗi.
- D sai: chuỗi chữ số trong CSV có thể được suy luận thành số, không gây lỗi chỉ vì có 0 đầu.

**Đối chiếu:** nhóm 1; K01, K07; mức Nền tảng. **Kiến thức và bẫy:** CSV là văn bản; suy luận kiểu có thể mất số 0 đầu; mã khác đại lượng; astype(str) sau đọc sai không khôi phục mã gốc; đọc lại từ raw đúng schema. **Đọc lại:** BG §1; NB ô 4–11.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-002

**Đáp án: A.**

- A đúng: phù hợp bảng trung gian; kích thước/tốc độ còn phụ thuộc dữ liệu và cấu hình.
- B sai: nhầm hai định dạng lưu trữ.
- C sai: lưu định dạng mới không sửa sai dữ liệu có trước.
- D sai: không có cam kết tuyệt đối về kích thước hay tỷ lệ thời gian.

**Đối chiếu:** nhóm 2; K14, K19; mức Nền tảng. **Kiến thức và bẫy:** Parquet nhị phân dạng bảng, lưu kiểu và theo cột; có thể bỏ cột không dùng; CSV/Parquet phục vụ nhu cầu khác nhau; kích thước và tốc độ không có cam kết tuyệt đối. **Đọc lại:** BG §1; NB ô 15–17.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu cơ chế hoặc thiết kế, không có output cần chạy).

#### B6-003

**Đáp án: C.**

- A sai: bỏ vai trò tham số truy vấn.
- B sai: JSON là nội dung phản hồi, không mặc định là bản sao tham số yêu cầu.
- C đúng: r.url cho địa chỉ đã gửi kèm tham số; mô phỏng không chứng minh dịch vụ thật chấp nhận một tên mới.
- D sai: HTTP thành công khác yêu cầu phân tích đúng.

**Đối chiếu:** nhóm 3; K20; mức Vận dụng. **Kiến thức và bẫy:** API, endpoint, params ghép URL và r.url để đối chiếu yêu cầu thực gửi. **Đọc lại:** BG §2; NB ô 23–26.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-004

**Đáp án: B.**

- A sai: giữ đúng hàng nhưng bỏ ORDER BY DESC.
- B đúng: giữ 100 và 80, loại NULL vì so sánh không TRUE, rồi sắp giảm dần.
- C sai: cho rằng NULL tự đạt ngưỡng hoặc luôn được giữ.
- D sai: dùng >80 thay >=80, bỏ biên P.

**Đối chiếu:** nhóm 4; K33, K34; mức Vận dụng. **Kiến thức và bẫy:** SELECT/FROM/WHERE/AS/ORDER BY/DESC: lọc và sắp kết quả, NULL không đạt so sánh ngưỡng; Pandas thiếu số vào DuckDB thành NULL trong các ví dụ; =NULL không giữ hàng, dùng IS NULL/IS NOT NULL. **Đọc lại:** NB ô 47–50.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-005

**Đáp án: C.**

- A sai: nhầm số hàng nguồn với số hàng kết quả COUNT tổng hợp.
- B sai: .df() đã yêu cầu chuyển kết quả thành DataFrame.
- C đúng: DuckDB chạy cùng chương trình trong ví dụ, không cần dựng máy chủ riêng; .df() trả DataFrame.
- D sai: DuckDB có thể truy vấn DataFrame Python theo tên biến trong cách dùng bài học.

**Đối chiếu:** nhóm 5; K32; mức Nền tảng. **Kiến thức và bẫy:** DuckDB chạy cùng chương trình; SQL mô tả kết quả; tên biến DataFrame, truy vấn file, .df trả DataFrame. **Đọc lại:** BG §3; NB ô 45–51.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-006

**Đáp án: C.**

- A sai: tưởng dtype str đồng thời tắt nhận diện giá trị thiếu.
- B sai: bỏ qua dtype id đã được khai báo.
- C đúng: dtype chuỗi bảo vệ mã id nhưng không tắt danh sách nhận diện NA,N/A,null mặc định.
- D sai: quên NA,N/A cũng thuộc các dấu hiệu thiếu mặc định trong câu.

**Đối chiếu:** nhóm 1; K02, K13; mức Vận dụng. **Kiến thức và bẫy:** dtype theo cột không tự tắt nhận diện NA mặc định; dtype chuỗi vẫn có thiếu; Kiểm shape, dtype logic, mã và số thiếu sau đọc; không kiểm riêng số hàng. **Đọc lại:** BG §1; NB ô 9–11; GK câu 14.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-007

**Đáp án: D.**

- A sai: json() giải mã nội dung, không thay raise_for_status.
- B sai: nhầm đúng cú pháp JSON với trạng thái HTTP thành công.
- C sai: 400 là mã phản hồi lỗi đã cho, không phải bằng chứng timeout.
- D đúng: JSON lỗi vẫn giải mã được; mã 400 vẫn là lỗi HTTP. Nên kiểm HTTP trước xử lý dữ liệu.

**Đối chiếu:** nhóm 3; K22; mức Vận dụng. **Kiến thức và bẫy:** JSON lỗi vẫn đọc được; HTTP 4xx/5xx và raise_for_status trước xử lý dữ liệu; 400 không phải timeout. **Đọc lại:** NB ô 27–28; GK câu 16 (đổi thứ tự lệnh để theo dõi điểm dừng).

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-008

(a)
```sql
SELECT khu, COUNT(*) AS n, AVG(gia) AS tb FROM d
WHERE gia>=60 GROUP BY khu
HAVING COUNT(*)>=2 ORDER BY khu;
```
Chỉ B: n=2,tb=80 từ 60,100. (b) Bỏ WHERE, thay COUNT(*) bằng COUNT(gia) ở SELECT và HAVING. Được A:(2,60), B:(2,80). (c) A tính 40,80, không chia cho ba hàng; C có hai hàng nhưng không giá biết nên bị loại ở (b). Chỉ xoá WHERE mà giữ COUNT(*) sẽ đếm cả giá thiếu, sai n và có thể giữ C với AVG NULL.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm WHERE và HAVING đúng; (b) 1 điểm thay cả hai COUNT; (c) 1 điểm kết quả/tập giá/mẫu số. Nhận COUNT(gia) ở (a) vì sau WHERE mọi gia đều biết.

**Đối chiếu:** nhóm 4; K37, K39, K35; mức Phân loại. **Kiến thức và bẫy:** WHERE lọc hàng trước, HAVING lọc nhóm sau; đổi tập giá tính mean và nhóm còn lại; Ít nhất N hàng/giá biết/giá đạt ngưỡng là ba yêu cầu; đổi WHERE phải rà SELECT/COUNT/HAVING; COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết. **Đọc lại:** NB ô 49–55; GK câu 24 (biến thể nhóm toàn thiếu).

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-009

Một cách đọc:
```python
d = pd.read_csv('gia.csv', dtype={'id':'str','khu':'str','gia':'float64'},
    keep_default_na=False, na_values={'gia':['?','-','']})
tb = d.groupby('khu')['gia'].mean()
```
Mean NA=10 (một giá biết), TB=15 từ (0+30)/2, khu -=NaN vì không có giá biết nhưng mã khu vẫn được giữ. Có ba gia thiếu. na_values chung chứa '-' sẽ làm mất mã khu '-' hợp lệ; để mặc định còn có thể mất mã NA. Giữ id đầu 001; không coi 0 là thiếu.

**Hướng dẫn chấm:** 2 điểm: schema/mã 0,5; keep_default_na và na_values theo cột đủ ba dấu hiệu 0,75; ba mean và phân biệt 0 0,5; lý do không dùng chung 0,25.

**Đối chiếu:** nhóm 1; K03, K04, K06; mức Phân loại. **Kiến thức và bẫy:** na_values theo cột khác danh sách chung; không làm mất mã hợp lệ ở cột khác; keep_default_na=False tắt NA/N/A/null/ô trống mặc định; phải khai báo lại dấu hiệu thiếu; Thiếu giá khác giá 0; tập giá biết và mẫu số sau đọc. **Đọc lại:** BG §1 bài tập 1; NB ô 9–14; LAB W1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-010

id đầu của r vẫn là số 1, price đầu vẫn là chuỗi '$12.00'. Parquet giữ kiểu/giá trị của bảng đầu vào đã đọc, không khôi phục 001 hoặc tự làm sạch tiền tệ thành số. Cần đọc lại CSV raw với dtype={'id':'str'} để giữ mã; xác định schema và xử lý price theo quy tắc phù hợp trước khi cần tính toán số, rồi mới lưu bảng processed. Kiểm mã, dtype logic, shape và giá trị sau đọc lại, không chỉ nhìn phần mở rộng Parquet.

**Hướng dẫn chấm:** 2 điểm: hai giá trị/kiểu 0,75; không tự sửa 0,5; đọc lại raw đúng dtype và kiểm kết quả 0,75.

**Đối chiếu:** nhóm 2; K16, K15, K07; mức Vận dụng. **Kiến thức và bẫy:** Parquet không sửa dữ liệu/kiểu đã sai; chuỗi tiền tệ không tự thành số; to_parquet/read_parquet và columns chọn cột; kiểm shape, mã, giá trị đọc lại; astype(str) sau đọc sai không khôi phục mã gốc; đọc lại từ raw đúng schema. **Đọc lại:** BG §1; NB ô 15–17; LAB bước 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR01

**Đáp án: C.**

- A sai: không có quy tắc tự thêm quan sát cho đủ khối.
- B sai: chọn cột không vô hiệu hoá chunksize.
- C đúng: chunksize giới hạn số hàng mỗi khối, khối cuối có thể ngắn hơn; không gom các khối thì không cần giữ toàn bảng.
- D sai: header được dùng làm tên cột, không là quan sát.

**Đối chiếu:** nhóm 1; K51; mức Bổ sung. **Kiến thức và bẫy:** chunksize trả trình đọc từng khối; không giữ toàn bảng nếu không gom lại. **Đọc lại:** NB ô 72–73: tự học từng khối.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-MR02

**Đáp án: C.**

- A sai: lấy trung bình hai mean khối (10+40)/2, cho khối ít giá ngang trọng số.
- B sai: dùng tổng số hàng gồm hai giá thiếu làm mẫu số.
- C đúng: cộng sum 10+120=130 và count 1+3=4 rồi chia; không chia theo số khối hay tổng sáu hàng.
- D sai: lấy tổng giá 130 chia số khối 2 thay số giá biết.

**Đối chiếu:** nhóm 1; K52; mức Bổ sung. **Kiến thức và bẫy:** Cộng dồn sum/count rồi chia; không mean các mean khối; lọc đúng tập từng khối. **Đọc lại:** NB ô 72–73: tự học tổng hợp qua khối.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

### Độ bao phủ sau đợt 1

Đã dùng 21/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K05, K08, K09, K10, K11, K12, K17, K18, K21, K23, K24, K25, K26, K27, K28, K29, K30, K31, K36, K38, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50, K53, K54, K55, K56, K57, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 2

### Câu trọng tâm

#### B6-011

**Đáp án: D.**

- A sai: kết quả là chuỗi 7 và 70, không khôi phục số 0 đầu.
- B sai: định dạng lưu mới giữ các giá trị 7,70 đã sai mã.
- C sai: có thể nhập nhằng các mã phân biệt bằng số 0 đầu; thay quy ước khóa không có căn cứ.
- D đúng: giữ văn bản nguồn thay vì đoán cách đệm lại thông tin đã mất.

**Đối chiếu:** nhóm 1; K01, K07; mức Nền tảng. **Kiến thức và bẫy:** CSV là văn bản; suy luận kiểu có thể mất số 0 đầu; mã khác đại lượng; astype(str) sau đọc sai không khôi phục mã gốc; đọc lại từ raw đúng schema. **Đọc lại:** NB ô 6–11; BG §1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-012

**Đáp án: A.**

- A đúng: Parquet lưu schema của d; kiểm round-trip trên môi trường đang dùng, không suy mọi backend phải có cùng biểu diễn chuỗi.
- B sai: ghi/đọc thông thường không có yêu cầu lọc hàng thiếu.
- C sai: bỏ thông tin kiểu đã lưu trong Parquet.
- D sai: shape không kiểm nội dung, nhãn mã hay kiểu dữ liệu.

**Đối chiếu:** nhóm 2; K15, K17; mức Vận dụng. **Kiến thức và bẫy:** to_parquet/read_parquet và columns chọn cột; kiểm shape, mã, giá trị đọc lại; Giữ schema logic khác bảo đảm mọi backend/dtype biểu diễn y hệt ở mọi môi trường. **Đọc lại:** NB ô 16–17; LAB bước 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-013

**Đáp án: D.**

- A sai: trạng thái và số hàng không chứng minh đúng phạm vi ngày.
- B sai: đổi nhãn không biến số đo tháng 1 thành tháng 2.
- C sai: timeout không sửa tham số sai.
- D đúng: URL và nhánh daily cùng cho thấy tháng 1, khác mục tiêu tháng 2 dù số ngày bằng nhau.

**Đối chiếu:** nhóm 3; K20, K23; mức Vận dụng. **Kiến thức và bẫy:** API, endpoint, params ghép URL và r.url để đối chiếu yêu cầu thực gửi; 200/raise_for_status chỉ kiểm HTTP, không bảo đảm đúng đơn vị, cấu trúc hay đủ dữ liệu. **Đọc lại:** NB ô 23–28; LAB bước 3.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-014

**Đáp án: A.**

- A đúng: 0 là giá đã biết; IS NOT NULL loại B,D.
- B sai: nhầm giá 0 với thiếu.
- C sai: đảo IS NOT NULL thành IS NULL.
- D sai: coi IS NOT NULL không lọc những giá thiếu từ DataFrame.

**Đối chiếu:** nhóm 4; K33, K34; mức Nền tảng. **Kiến thức và bẫy:** SELECT/FROM/WHERE/AS/ORDER BY/DESC: lọc và sắp kết quả, NULL không đạt so sánh ngưỡng; Pandas thiếu số vào DuckDB thành NULL trong các ví dụ; =NULL không giữ hàng, dùng IS NULL/IS NOT NULL. **Đọc lại:** NB ô 49–57.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-015

**Đáp án: C.**

- A sai: cho rằng LEFT JOIN luôn giữ nguyên số hàng trái dù khóa phải lặp.
- B sai: đếm đúng năm cặp khớp nhưng bỏ hàng S không khớp.
- C đúng: P và Q mỗi listing ghép hai hàng A: 4 cặp; R ghép một B; S không khớp được giữ một hàng phi NULL: tổng 6.
- D sai: đếm số mã khu khác nhau thay hàng kết quả ghép.

**Đối chiếu:** nhóm 5; K42; mức Vận dụng. **Kiến thức và bẫy:** LEFT JOIN/ON tạo các cặp khóa; khóa phải lặp có thể tăng hàng trái. **Đọc lại:** NB ô 58–60; GK câu 15.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-016

**Đáp án: B.**

- A sai: không có quy tắc coi chưa biết là miễn phí.
- B đúng: dtype yêu cầu kiểu, không định nghĩa dấu hiệu thiếu mới; dtype id chuỗi chỉ giữ mã.
- C sai: ép kiểu không tự tạo quy tắc NA cho mọi chuỗi không hợp lệ.
- D sai: dtype chuỗi không thay keep_default_na hay na_values.

**Đối chiếu:** nhóm 1; K02, K05; mức Vận dụng. **Kiến thức và bẫy:** dtype theo cột không tự tắt nhận diện NA mặc định; dtype chuỗi vẫn có thiếu; Ép float64 khi còn chuỗi không hợp lệ có thể gây ValueError. **Đọc lại:** BG §1; NB ô 9–14.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-017

**Đáp án: D.**

- A sai: coi NULL là 0 và chia cho bốn hàng.
- B sai: loại giá 0 cùng giá thiếu khỏi COUNT(gia) và AVG.
- C sai: nhầm COUNT(*) cũng bỏ hàng có gia NULL.
- D đúng: COUNT(*) lấy bốn hàng; COUNT(gia) và mẫu số AVG dùng ba giá biết 0,10,20.

**Đối chiếu:** nhóm 4; K34, K35; mức Nền tảng. **Kiến thức và bẫy:** Pandas thiếu số vào DuckDB thành NULL trong các ví dụ; =NULL không giữ hàng, dùng IS NULL/IS NOT NULL; COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết. **Đọc lại:** NB ô 49–51; BG §3.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-018

(a) JSON hợp lệ chỉ bảo đảm giải mã được dict. HTTP 503 là lỗi; x không có nhánh daily nên truy cập ấy gây KeyError, không phải dữ liệu ngày.
```python
r.raise_for_status()
x = r.json()
d = pd.DataFrame(x['daily'])
```
(b) Với 503, dòng đầu gây HTTPError và không chạy bước sau. (c) Kiểm đơn vị trong daily_units; kiểm ngày/địa điểm và timezone đúng yêu cầu (cũng kiểm độ dài các danh sách tương ứng). 200 và ba hàng chưa đủ chứng minh các điều này.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm phân biệt JSON/HTTP và nhánh; (b) 1 điểm thứ tự đúng; (c) 1 điểm hai kiểm tra ý nghĩa cụ thể. Nhận kiểm ngày và đơn vị hoặc kiểm địa điểm, đơn vị phù hợp mục tiêu.

**Đối chiếu:** nhóm 3; K22, K23, K25; mức Phân loại. **Kiến thức và bẫy:** JSON lỗi vẫn đọc được; HTTP 4xx/5xx và raise_for_status trước xử lý dữ liệu; 400 không phải timeout; 200/raise_for_status chỉ kiểm HTTP, không bảo đảm đúng đơn vị, cấu trúc hay đủ dữ liệu; JSON object→dict, array→list; chọn daily; các danh sách tương ứng vị trí và độ dài. **Đọc lại:** NB ô 27–35; GK câu 16.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-019

(a)
```sql
SELECT listing_id, COUNT(*) AS n FROM rv
WHERE year(date)=2025 GROUP BY listing_id
HAVING COUNT(*)>=2 ORDER BY listing_id;
```
Kết quả A:2,B:2. (b) Giữ WHERE năm, đổi cả hai COUNT(*) thành COUNT(diem): chỉ B:2. (c) Review A năm 2024 không thuộc tập xét; A năm 2025 chỉ có một diem biết, C không có diem biết. Có thể thêm AND diem IS NOT NULL vào WHERE rồi dùng COUNT(*) cho (b), vì yêu cầu đếm review có điểm, không báo mọi review.

**Hướng dẫn chấm:** 3 điểm: (a) lọc năm trước nhóm và HAVING 1; (b) sửa số đếm nhất quán 1; (c) hai kết quả và ý nghĩa phạm vi/mẫu số 1. Không bắt buộc cùng cách viết.

**Đối chiếu:** nhóm 4; K40, K35, K39; mức Phân loại. **Kiến thức và bẫy:** year(date): review theo năm rồi nhóm; HAVING đếm trong phạm vi năm, không lẫn mọi năm; COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết; Ít nhất N hàng/giá biết/giá đạt ngưỡng là ba yêu cầu; đổi WHERE phải rà SELECT/COUNT/HAVING. **Đọc lại:** LAB bước 7,10; GK câu 24 (biến thể review).

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-020

Danh sách NA chung làm khu của 101 và 104 thành thiếu. Dtype chuỗi không ngăn việc nhận diện NA.
```python
d = pd.read_csv('d.csv', keep_default_na=False,
    na_values={'gia':['?']},
    dtype={'id':'str','khu':'str','gia':'float64'})
assert d['khu'].tolist() == ['?','NA','TB','?']
assert d['gia'].isna().sum() == 1 and d.loc[3,'gia'] == 0
```
Kiểm giữ mã khu và thiếu giá/giá 0, không chỉ shape (4,3).

**Hướng dẫn chấm:** 2 điểm: xác định hai ô 0,5; sửa na_values theo cột và giữ mặc định đã tắt 0,75; hai kiểm tra cụ thể 0,75.

**Đối chiếu:** nhóm 1; K03, K02, K13; mức Vận dụng. **Kiến thức và bẫy:** na_values theo cột khác danh sách chung; không làm mất mã hợp lệ ở cột khác; dtype theo cột không tự tắt nhận diện NA mặc định; dtype chuỗi vẫn có thiếu; Kiểm shape, dtype logic, mã và số thiếu sau đọc; không kiểm riêng số hàng. **Đọc lại:** BG §1 bài tập 1; NB ô 9–14.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR03

**Đáp án: D.**

- A sai: khác công việc cần làm, không tách tác động chọn cột.
- B sai: kích thước file không là thời gian đọc hay RAM DataFrame.
- C sai: kết quả đọc chịu ảnh hưởng cache và môi trường, cần diễn giải thận trọng.
- D đúng: giữ cùng công việc và tách ba đại lượng, không suy tỷ lệ từ một lần đo.

**Đối chiếu:** nhóm 2; K53; mức Bổ sung. **Kiến thức và bẫy:** Benchmark cùng bảng/cột/schema, đọc tương đương; file, DataFrame RAM, thời gian là ba phép đo; cache/môi trường. **Đọc lại:** NB ô 70–71: tự học benchmark.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu cơ chế hoặc thiết kế, không có output cần chạy).

#### B6-MR04

```python
s = 0.0; n = 0
for c in pd.read_csv('gia.csv', usecols=['gia'], chunksize=3):
    s += c['gia'].sum()
    n += c['gia'].count()
tb = s/n if n else np.nan
```
s=130,n=4,tb=32.5 USD/đêm. Các count khối là 1,3,0; không lấy mean của các mean khối và không chia cho bảy listing.

**Hướng dẫn chấm:** 2 điểm: đọc từng khối/không gom 0,5; sum/count cộng dồn 0,75; kết quả và xử lý n=0 0,75. Nhận đọc dtype float64 phù hợp.

**Đối chiếu:** nhóm 1; K52, K51; mức Bổ sung. **Kiến thức và bẫy:** Cộng dồn sum/count rồi chia; không mean các mean khối; lọc đúng tập từng khối; chunksize trả trình đọc từng khối; không giữ toàn bảng nếu không gom lại. **Đọc lại:** NB ô 72–73: tự học từng khối.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

### Độ bao phủ sau đợt 2

Đã dùng 28/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K08, K09, K10, K11, K12, K18, K21, K24, K26, K27, K28, K29, K30, K31, K36, K38, K41, K43, K44, K45, K46, K47, K48, K49, K50, K54, K55, K56, K57, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 3

### Câu trọng tâm

#### B6-021

**Đáp án: C.**

- A sai: nhầm cột với hàng.
- B sai: CSV không có tổ chức cột nhị phân như Parquet để suy ra tỷ lệ byte đó.
- C đúng: usecols chọn cột đưa vào DataFrame, không lọc hàng hay cam kết tỷ lệ thời gian.
- D sai: usecols loại cột khỏi bảng kết quả, không tạo cột đệm.

**Đối chiếu:** nhóm 1; K08; mức Nền tảng. **Kiến thức và bẫy:** usecols giảm cột trong DataFrame; CSV vẫn quét văn bản, nén còn giải nén; thời gian không tỷ lệ số cột. **Đọc lại:** NB ô 15,18–20; LAB bước 1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-022

**Đáp án: B.**

- A sai: không có thông tin độ dài mã gốc trong cột số đã ghi.
- B đúng: Parquet giữ hai giá trị số 1; kiểm số hàng/kiểu số không chứng minh giữ đúng khóa định danh.
- C sai: số hàng khác số khóa phân biệt.
- D sai: mã là định danh, kiểu số có thể làm mất phân biệt có ý nghĩa.

**Đối chiếu:** nhóm 2; K16, K07; mức Vận dụng. **Kiến thức và bẫy:** Parquet không sửa dữ liệu/kiểu đã sai; chuỗi tiền tệ không tự thành số; astype(str) sau đọc sai không khôi phục mã gốc; đọc lại từ raw đúng schema. **Đọc lại:** NB ô 15–17; LAB bước 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-023

**Đáp án: C.**

- A sai: lớp ngoài còn metadata và là object, không phải danh sách quan sát.
- B sai: json() đã giải mã object lồng nhau thành dict.
- C đúng: object thành dict, array thành list; nhánh daily chứa các dãy quan sát theo ngày.
- D sai: daily_units mô tả đơn vị, không chứa các quan sát ngày.

**Đối chiếu:** nhóm 3; K25; mức Nền tảng. **Kiến thức và bẫy:** JSON object→dict, array→list; chọn daily; các danh sách tương ứng vị trí và độ dài. **Đọc lại:** NB ô 27–35.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-024

**Đáp án: D.**

- A sai: coi HAVING lọc từng giá trước khi tính mean.
- B sai: coi WHERE không làm đổi tập giá tham gia mean.
- C sai: dùng >60 thay >=60 ở HAVING nên loại nhầm A.
- D đúng: Q1 bỏ giá 20 trước mean; Q2 tính mean A=(20+100)/2 rồi giữ A ở biên 60.

**Đối chiếu:** nhóm 4; K37, K35; mức Vận dụng. **Kiến thức và bẫy:** WHERE lọc hàng trước, HAVING lọc nhóm sau; đổi tập giá tính mean và nhóm còn lại; COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết. **Đọc lại:** NB ô 52–55; GK câu 24.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-025

**Đáp án: A.**

- A đúng: A có phí 5; B không đạt ngưỡng, C không khớp và D khớp nhưng phi NULL đều không cho điều kiện TRUE.
- B sai: cho rằng LEFT JOIN vẫn bắt buộc giữ C sau mọi điều kiện WHERE bên phải.
- C sai: coi NULL tự thỏa phi<=10 hoặc dùng OR IS NULL chưa có trong truy vấn.
- D sai: phân biệt C không khớp nhưng vẫn cho phi thiếu của D đạt ngưỡng số.

**Đối chiếu:** nhóm 5; K43, K50; mức Vận dụng. **Kiến thức và bẫy:** WHERE cột phải loại hàng đệm NULL; ON giới hạn đối ứng mà vẫn giữ trái; Kiểm độ khớp qua khóa thật và metadata, không chỉ số hàng/NaN hay assert đơn lẻ. **Đọc lại:** BG §3 JOIN; NB ô 58–60; GK câu 15.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-026

**Đáp án: B.**

- A sai: chia tổng 60 cho cả bốn hàng, ngầm coi thiếu là 0.
- B đúng: (0+20+40)/3; thiếu ? không tham gia mẫu số nhưng 0 có.
- C sai: loại cả giá 0 như một dấu hiệu thiếu.
- D sai: coi chỉ một giá thiếu làm mọi giá đều không biết, bỏ quy tắc mean trên tập biết.

**Đối chiếu:** nhóm 1; K06; mức Nền tảng. **Kiến thức và bẫy:** Thiếu giá khác giá 0; tập giá biết và mẫu số sau đọc. **Đọc lại:** BG §1; LAB W1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-027

**Đáp án: B.**

- A sai: so trực tiếp các số °F với ngưỡng 35°C.
- B đúng: sau đổi đơn vị được 35,30,40,20°C; giữ cả biên 35.
- C sai: đổi đúng đơn vị nhưng dùng >35 thay từ 35 trở lên.
- D sai: đổi đúng đơn vị nhưng đảo điều kiện thành dưới 35°C, lấy phần bù của tập cần tìm.

**Đối chiếu:** nhóm 3; K26, K23; mức Vận dụng. **Kiến thức và bẫy:** daily_units, đổi °F sang °C theo công thức, biên từ 35°C; kiểm đơn vị trước lọc; 200/raise_for_status chỉ kiểm HTTP, không bảo đảm đúng đơn vị, cấu trúc hay đủ dữ liệu. **Đọc lại:** NB ô 42–44; LAB bước 4.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-028

```sql
SELECT khu, COUNT(*) AS n_hang, COUNT(gia) AS n_biet,
       COUNT(*)-COUNT(gia) AS n_thieu, AVG(gia) AS tb
FROM d GROUP BY khu ORDER BY khu;
```
(a) A:(2,2,0,15), B:(2,1,1,30), C:(2,0,2,NULL); mỗi hàng là một khu, mean chia số giá biết. (b) Thêm HAVING COUNT(*)-COUNT(gia)>=1 trước ORDER BY; giữ B,C. (c) WHERE chỉ giữ hàng thiếu nên A biến mất, n_hang của B còn 1 và mọi mean còn lại NULL; không thể hiện số thiếu 0 cho mọi khu như yêu cầu.

**Hướng dẫn chấm:** 3 điểm: (a) đủ bốn phép tổng hợp và giữ A 1; (b) HAVING đúng 0,75; (c) kết quả/tập giá/mẫu số và lý do mất A 1,25. Nhận SUM biểu thức tương đương đã giải thích nếu chạy đúng DuckDB.

**Đối chiếu:** nhóm 4; K38, K36, K37; mức Phân loại. **Kiến thức và bẫy:** Đếm thiếu mọi nhóm bằng COUNT(*)−COUNT(gia); WHERE IS NULL làm mất nhóm thiếu 0; Nhóm toàn giá thiếu: COUNT(*)>0, COUNT(gia)=0, AVG(gia) NULL; WHERE lọc hàng trước, HAVING lọc nhóm sau; đổi tập giá tính mean và nhóm còn lại. **Đọc lại:** NB ô 56–57; BG §3 bài tập 3; GK câu 24.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-029

```python
d = pd.read_csv('raw/gia.csv', dtype={'id':'str','gia':'float64'})
d.to_parquet('processed/gia.parquet', index=False)
r = pd.read_parquet('processed/gia.parquet')
pd.testing.assert_frame_equal(d, r)
assert r.loc[0,'id']=='001' and r['gia'].isna().sum()==1
```
Giả sử các thư mục đã tồn tại. Không ghi đè raw: có thể đọc lại đúng đầu vào để sửa quy tắc xử lý. Kiểm round-trip này xác nhận môi trường đang chạy; schema logic không có nghĩa mọi backend/phiên bản có biểu diễn dtype giống hệt. Kiểm thêm shape (4,2) và giá 0 nếu dùng kiểm rời thay assert_frame_equal.

**Hướng dẫn chấm:** 2 điểm: đọc mã/thiếu đúng 0,5; ghi đọc và kiểm nội dung 0,75; giữ raw và giới hạn backend 0,75. Nhận các kiểm tương đương có shape, mã, kiểu logic, giá và thiếu.

**Đối chiếu:** nhóm 2; K18, K17, K15; mức Vận dụng. **Kiến thức và bẫy:** raw giữ đầu vào gốc, processed bảng xử lý; snapshot đã tải khác tải lại cùng URL; Giữ schema logic khác bảo đảm mọi backend/dtype biểu diễn y hệt ở mọi môi trường; to_parquet/read_parquet và columns chọn cột; kiểm shape, mã, giá trị đọc lại. **Đọc lại:** NB ô 16–20; LAB bước 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-030

(a) Mất A: đã khớp với phí 20 nên không có hàng đệm NULL cho A; cả hai vế WHERE đều không TRUE. B không khớp nên được giữ bởi OR.
```sql
SELECT l.id,t.phi FROM l
LEFT JOIN t ON l.id=t.id AND t.phi<10
ORDER BY l.id;
```
(c) A:NULL,B:NULL,C:5,D:8. Điều kiện ON giới hạn đối ứng; A không có đối ứng đạt điều kiện nên được giữ với NULL, còn C có đối ứng hợp lệ 5. Chưa có đối ứng đạt điều kiện khác chưa từng có mã trong t.

**Hướng dẫn chấm:** 3 điểm: (a) A và cơ chế không có hàng đệm bổ sung 1; (b) điều kiện trong ON, bỏ WHERE sai 1; (c) bốn hàng và ý nghĩa A/C 1.

**Đối chiếu:** nhóm 5; K43, K44, K42; mức Phân loại. **Kiến thức và bẫy:** WHERE cột phải loại hàng đệm NULL; ON giới hạn đối ứng mà vẫn giữ trái; Thêm OR phải IS NULL không luôn chữa được yêu cầu giữ mọi trái; khác đưa điều kiện vào ON; LEFT JOIN/ON tạo các cặp khóa; khóa phải lặp có thể tăng hàng trái. **Đọc lại:** BG §3 JOIN; GK câu 15 (biến thể ON).

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR05

**Đáp án: D.**

- A sai: nhầm kế hoạch với dữ liệu kết quả.
- B sai: EXPLAIN không bảo đảm thời gian thực nghiệm hay bỏ ảnh hưởng môi trường.
- C sai: query plan không là danh sách các quan sát nguồn.
- D đúng: EXPLAIN cho biết cách thực hiện dự kiến, không phải bảng thống kê kết quả và không tự là phép đo tốc độ.

**Đối chiếu:** nhóm 5; K54; mức Bổ sung. **Kiến thức và bẫy:** EXPLAIN trả kế hoạch, không phải kết quả hay phép đo tốc độ truy vấn. **Đọc lại:** NB ô 74–75: tự học EXPLAIN.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-MR06

**Đáp án: B.**

- A sai: chia sẻ notebook cũng làm lộ key.
- B đúng: tách bí mật khỏi mã và chỉ gửi theo cách tài liệu dịch vụ yêu cầu.
- C sai: tên biến không che giá trị literal có trong file.
- D sai: vẫn đưa bí mật vào nơi không cần chia sẻ; xóa tên biến không thu hồi thông tin đã lộ.

**Đối chiếu:** nhóm 3; K56; mức Bổ sung. **Kiến thức và bẫy:** API key từ biến môi trường/Colab Secrets, không ghi khóa thật vào notebook hoặc prompt. **Đọc lại:** NB ô 76: tự học xác thực API.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu cơ chế hoặc thiết kế, không có output cần chạy).

### Độ bao phủ sau đợt 3

Đã dùng 38/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K09, K10, K11, K12, K21, K24, K27, K28, K29, K30, K31, K41, K45, K46, K47, K48, K49, K55, K57, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 4

### Câu trọng tâm

#### B6-031

**Đáp án: D.**

- A sai: cho rằng ô trống luôn là NaN ngay cả khi đã tắt mặc định.
- B sai: biết chuỗi rỗng được giữ nhưng vẫn tính nó là giá trị thiếu theo isna.
- C sai: cho rằng dtype chuỗi tự thay ô trống bằng chuỗi số 0, dù không có quy tắc thay giá trị.
- D đúng: tắt danh sách thiếu mặc định mà không khai báo lại ô trống nên gia hàng 1 là chuỗi rỗng; mã NA cũng được giữ.

**Đối chiếu:** nhóm 1; K04, K05; mức Nền tảng. **Kiến thức và bẫy:** keep_default_na=False tắt NA/N/A/null/ô trống mặc định; phải khai báo lại dấu hiệu thiếu; Ép float64 khi còn chuỗi không hợp lệ có thể gây ValueError. **Đọc lại:** NB ô 9–14; BG §1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-032

**Đáp án: B.**

- A sai: đảo chiều hàng/cột.
- B đúng: columns chọn cột; không phải yêu cầu chỉ giữ hàng có giá biết.
- C sai: đọc chọn cột không tạo lại cột không chọn.
- D sai: Parquet giữ thông tin kiểu của bảng đã lưu đúng.

**Đối chiếu:** nhóm 2; K14, K15; mức Vận dụng. **Kiến thức và bẫy:** Parquet nhị phân dạng bảng, lưu kiểu và theo cột; có thể bỏ cột không dùng; to_parquet/read_parquet và columns chọn cột; kiểm shape, mã, giá trị đọc lại. **Đọc lại:** NB ô 15–17; LAB bước 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-033

**Đáp án: A.**

- A đúng: chọn nguồn lịch sử và phạm vi/đại lượng/múi giờ theo bảng đã cho, sau đó vẫn kiểm phản hồi.
- B sai: số ngày bằng nhau không làm dự báo thành dữ liệu lịch sử.
- C sai: khác đại lượng cần phân tích.
- D sai: ngày trong phản hồi cần được diễn giải theo quy ước múi giờ phù hợp.

**Đối chiếu:** nhóm 3; K21, K20; mức Vận dụng. **Kiến thức và bẫy:** Phân biệt dự báo và lịch sử; chọn vị trí, đại lượng, khoảng ngày, múi giờ theo bảng tham số được cho; API, endpoint, params ghép URL và r.url để đối chiếu yêu cầu thực gửi. **Đọc lại:** LAB bước 3; NB ô 23–26.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-034

**Đáp án: C.**

- A sai: đếm mọi năm trước khi áp điều kiện số review.
- B sai: lọc năm đúng nhưng bỏ HAVING.
- C đúng: chỉ hai review P năm 2025 tham gia; Q và R mỗi listing một review năm đó nên không đạt HAVING.
- D sai: giữ đúng listing có đủ review năm 2025 nhưng hiển thị n từ mọi năm.

**Đối chiếu:** nhóm 4; K40, K35; mức Vận dụng. **Kiến thức và bẫy:** year(date): review theo năm rồi nhóm; HAVING đếm trong phạm vi năm, không lẫn mọi năm; COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết. **Đọc lại:** LAB bước 7,10.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-035

**Đáp án: B.**

- A sai: COUNT(*) đếm hàng hiện tại, không tự khử lặp id.
- B đúng: hai cặp cho A, hai cho B, một cho C và một hàng không khớp cho D; cần kiểm khóa host trước diễn giải.
- C sai: vừa bỏ sai phạm vi listing vừa giữ các bản sao do ghép H1.
- D sai: JOIN mặc định tạo các cặp khớp, không tự áp ràng buộc duy nhất.

**Đối chiếu:** nhóm 5; K42, K45; mức Vận dụng. **Kiến thức và bẫy:** LEFT JOIN/ON tạo các cặp khóa; khóa phải lặp có thể tăng hàng trái; COUNT(*) sau LEFT JOIN khác số đối ứng; đếm khóa phải không NULL khác đếm cột thông tin có thể thiếu. **Đọc lại:** NB ô 58–60; LAB bước 9.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-036

**Đáp án: C.**

- A sai: nhầm list khác độ dài với Series có nhãn có thể căn chỉnh.
- B sai: không có quy tắc tự cắt danh sách dài cho vừa.
- C đúng: DataFrame từ dict các list yêu cầu số phần tử tương ứng; không tự quyết ngày nào thiếu.
- D sai: raise_for_status kiểm mã HTTP, không kiểm cấu trúc nghiệp vụ.

**Đối chiếu:** nhóm 3; K25, K23; mức Vận dụng. **Kiến thức và bẫy:** JSON object→dict, array→list; chọn daily; các danh sách tương ứng vị trí và độ dài; 200/raise_for_status chỉ kiểm HTTP, không bảo đảm đúng đơn vị, cấu trúc hay đủ dữ liệu. **Đọc lại:** NB ô 30–35; LAB bước 4.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-037

**Đáp án: C.**

- A sai: coi hai NULL là giá 0 đã biết.
- B sai: nhầm không giá biết với không có hàng.
- C đúng: nhóm có hai hàng, không giá biết, mean là NULL; nhóm không tự biến mất.
- D sai: coi GROUP BY mặc định loại mọi nhóm toàn giá thiếu, dù khóa A không thiếu.

**Đối chiếu:** nhóm 4; K36, K34; mức Nền tảng. **Kiến thức và bẫy:** Nhóm toàn giá thiếu: COUNT(*)>0, COUNT(gia)=0, AVG(gia) NULL; Pandas thiếu số vào DuckDB thành NULL trong các ví dụ; =NULL không giữ hàng, dùng IS NULL/IS NOT NULL. **Đọc lại:** NB ô 49–57; BG §3.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-038

(a) Hai file cùng nguồn/cùng tên cột vẫn có thể khác schema. usecols chỉ chọn cột; không chuyển '$12.00' thành số.
```python
d = pd.read_csv('ban_day_du.csv.gz', usecols=['id','price'],
                dtype={'id':'str','price':'str'})
assert d.shape == (4,2)
assert d.loc[0,'id']=='001' and d.loc[0,'price']=='$12.00'
```
(c) Xác định đơn vị tiền và quy tắc thiếu, xử lý chuỗi tiền tệ thành số đúng rồi kiểm cùng id/snapshot/phạm vi trước so mean. Không suy schema từ bản rút gọn hay chỉ từ bốn hàng đọc thành công.

**Hướng dẫn chấm:** 3 điểm: (a) khác schema/usecols 1; (b) đọc và kiểm đủ 1; (c) chuẩn hóa giá/đơn vị/thiếu và cùng đối tượng 1. Không bắt cú pháp xử lý chuỗi ngoài Bài 6.

**Đối chiếu:** nhóm 1; K11, K08, K13; mức Phân loại. **Kiến thức và bẫy:** Bản rút gọn và đầy đủ có thể khác schema, cùng price nhưng số hoặc chuỗi tiền tệ; usecols giảm cột trong DataFrame; CSV vẫn quét văn bản, nén còn giải nén; thời gian không tỷ lệ số cột; Kiểm shape, dtype logic, mã và số thiếu sau đọc; không kiểm riêng số hàng. **Đọc lại:** NB ô 18–21; LAB ô 7–14.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-039

(a)
```sql
SELECT loai,COUNT(first_review) AS n FROM 'l.parquet'
GROUP BY loai HAVING COUNT(first_review)>=2 ORDER BY loai;
```
Chỉ phong:2. (b) Đổi cả COUNT(first_review) thành COUNT(*): nguyen_can:3,phong:3. (c) Không thêm WHERE first_review IS NOT NULL ở (b); nếu (a) dùng WHERE ấy cùng COUNT(*) thì phải bỏ WHERE khi đổi. Mỗi hàng nguồn là listing; biết ngày đầu không cho biết listing có bao nhiêu review.

**Hướng dẫn chấm:** 3 điểm: (a) đọc file và số đếm 1; (b) đổi SELECT/HAVING đúng 1; (c) hai kết quả, bỏ lọc sai nếu có, đơn vị quan sát 1.

**Đối chiếu:** nhóm 4; K39, K35, K41; mức Phân loại. **Kiến thức và bẫy:** Ít nhất N hàng/giá biết/giá đạt ngưỡng là ba yêu cầu; đổi WHERE phải rà SELECT/COUNT/HAVING; COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết; SQL trên Parquet chọn cột/tổng hợp tại file; công cụ theo nguồn, bộ nhớ và thao tác, không luôn nhanh hơn. **Đọc lại:** LAB bước 8; NB ô 49–55; GK câu 24.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-040

400 là mã phản hồi lỗi đã nhận; lý do đề cho là tham số ngày, không phải bằng chứng Timeout. Cần đối chiếu tham số/tài liệu và nội dung lỗi, không kỳ vọng timeout tự sửa ngày.
timeout=20 giới hạn chờ kết nối/nhận dữ liệu theo Requests, không là deadline cứng cho toàn bộ thời gian yêu cầu.
```python
r.raise_for_status()
x = r.json()
```
Với 400, dòng đầu gây HTTPError, không chạy dòng thứ hai. Có thể đọc body để chẩn đoán lỗi trong xử lý ngoại lệ, nhưng không dùng nó như dữ liệu quan sát thành công.

**Hướng dẫn chấm:** 2 điểm: giải thích 400 và sửa tham số 0,75; timeout không deadline tổng 0,75; thứ tự và điểm dừng 0,5. Không chấm theo thời gian mạng thực tế.

**Đối chiếu:** nhóm 3; K24, K22; mức Vận dụng. **Kiến thức và bẫy:** Requests timeout giới hạn chờ kết nối/đọc, không phải deadline tổng thời gian; JSON lỗi vẫn đọc được; HTTP 4xx/5xx và raise_for_status trước xử lý dữ liệu; 400 không phải timeout. **Đọc lại:** NB ô 23–28.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR07

**Đáp án: A.**

- A đúng: 429 liên quan giới hạn truy cập; cách xử lý phụ thuộc dịch vụ và thông tin được cung cấp.
- B sai: bịa quy tắc chờ cố định và bỏ hạn mức dịch vụ.
- C sai: giải mã JSON không làm yêu cầu bị giới hạn thành thành công.
- D sai: timeout điều chỉnh chờ kết nối/đọc, không cấp thêm quota.

**Đối chiếu:** nhóm 3; K57; mức Bổ sung. **Kiến thức và bẫy:** 429 và giới hạn truy cập: làm theo hướng dẫn dịch vụ, không có thời gian nghỉ chuẩn cho mọi API. **Đọc lại:** NB ô 76: tự học giới hạn truy cập.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-MR08

Không. 0.8/0.2=4 chỉ mô tả hai lần đọc khác số cột; chưa tách hiệu ứng chọn cột khỏi định dạng, và RAM khác số byte file.
1. Đọc cùng bảng, cùng cột (CSV usecols; Parquet columns), cùng schema/NA cần thiết.
2. Kiểm shape, mã và giá trị tương đương trước so thời gian.
3. Đo lặp, nêu cache/môi trường và tách chi phí chuẩn bị/ghi khỏi phần đo đọc.
4. Báo riêng kích thước file, RAM DataFrame và thời gian; không suy cam kết mọi lần chạy.
Không cần tạo benchmark thật để trả lời.

**Hướng dẫn chấm:** 2 điểm: bác hai kết luận đúng lý do 0,75; công việc tương đương/kiểm kết quả 0,75; đo lặp/cache và tách đại lượng 0,5.

**Đối chiếu:** nhóm 2; K53; mức Bổ sung. **Kiến thức và bẫy:** Benchmark cùng bảng/cột/schema, đọc tương đương; file, DataFrame RAM, thời gian là ba phép đo; cache/môi trường. **Đọc lại:** NB ô 70–71: tự học benchmark.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu cơ chế hoặc thiết kế, không có output cần chạy).

### Độ bao phủ sau đợt 4

Đã dùng 44/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K09, K10, K12, K27, K28, K29, K30, K31, K46, K47, K48, K49, K55, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 5

### Câu trọng tâm

#### B6-041

**Đáp án: A.**

- A đúng: ít cột có thể giảm RAM bảng nhưng không chứng minh thời gian hoặc kích thước file giảm còn 3/20.
- B sai: nhầm lựa chọn cột với lấy mẫu hàng.
- C sai: đọc có chọn lọc không ghi đè hay rút gọn file trên đĩa.
- D sai: usecols không thay cấu trúc file hay bỏ việc giải nén.

**Đối chiếu:** nhóm 1; K08, K09; mức Nền tảng. **Kiến thức và bẫy:** usecols giảm cột trong DataFrame; CSV vẫn quét văn bản, nén còn giải nén; thời gian không tỷ lệ số cột; pandas nhận diện .csv.gz từ tên file; nén không thay schema dữ liệu. **Đọc lại:** NB ô 18–20,68–69; LAB bước 1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-042

**Đáp án: C.**

- A sai: xử lý có thể mất thông tin; Parquet không là phép đảo mọi biến đổi.
- B sai: nguồn có thể cập nhật, không bảo đảm đúng đầu vào cũ.
- C đúng: raw giữ bằng chứng đầu vào, processed phục vụ phân tích; lợi ích cột không là cam kết mọi file nhỏ/nhanh hơn.
- D sai: đổi tên không chuyển định dạng hay xử lý kiểu.

**Đối chiếu:** nhóm 2; K18, K19; mức Vận dụng. **Kiến thức và bẫy:** raw giữ đầu vào gốc, processed bảng xử lý; snapshot đã tải khác tải lại cùng URL; CSV/Parquet phục vụ nhu cầu khác nhau; kích thước và tốc độ không có cam kết tuyệt đối. **Đọc lại:** NB ô 15–20; LAB bước 2.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu cơ chế hoặc thiết kế, không có output cần chạy).

#### B6-043

**Đáp án: A.**

- A đúng: các list ghép theo vị trí, không tự khớp nhiệt độ theo giá trị ngày.
- B sai: list không có nhãn quan sát để tự căn chỉnh.
- C sai: độ dài vẫn bằng nhau nên có thể sai âm thầm, không nhất thiết báo lỗi.
- D sai: thứ tự nhiệt độ không quyết định thứ tự ngày, cách này chỉ có thể tình cờ đúng.

**Đối chiếu:** nhóm 3; K25; mức Vận dụng. **Kiến thức và bẫy:** JSON object→dict, array→list; chọn daily; các danh sách tương ứng vị trí và độ dài. **Đọc lại:** NB ô 30–35; LAB bước 4–6.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-044

**Đáp án: A.**

- A đúng: ba giá biết là 0,10,100; trung vị 10, mean 110/3, không bỏ giá 0.
- B sai: thay NULL bằng 0 rồi tính trên 0,0,10,100.
- C sai: bỏ cả giá 0 và NULL, còn 10,100.
- D sai: trung vị/count bỏ NULL nhưng mẫu số mean vẫn dùng cả bốn hàng.

**Đối chiếu:** nhóm 4; K35; mức Nền tảng. **Kiến thức và bẫy:** COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết. **Đọc lại:** NB ô 49–51,62; LAB bước 8.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-045

**Đáp án: A.**

- A đúng: A hai hàng, B một, C và D mỗi bên một hàng đệm; ba rid đã khớp nhưng chỉ hai phí biết.
- B sai: cho rằng mỗi listing luôn một hàng sau ghép dù A có hai đối ứng.
- C sai: coi COUNT(rid) đếm cả hai hàng đệm NULL như COUNT(*).
- D sai: coi ghi nhận A có phí thiếu là không khớp khóa nên bỏ cả rid r2.

**Đối chiếu:** nhóm 5; K45, K50; mức Vận dụng. **Kiến thức và bẫy:** COUNT(*) sau LEFT JOIN khác số đối ứng; đếm khóa phải không NULL khác đếm cột thông tin có thể thiếu; Kiểm độ khớp qua khóa thật và metadata, không chỉ số hàng/NaN hay assert đơn lẻ. **Đọc lại:** NB ô 49–50,58–60; LAB bước 9.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-046

**Đáp án: D.**

- A sai: đổi câu hỏi sang mean nhóm và tổng hàng, giữ cả A dù chỉ một giá đạt ngưỡng.
- B sai: giá biết không đồng nghĩa giá đạt ngưỡng; A có 20 biết nhưng không đạt.
- C sai: chưa kiểm ít nhất hai listing, sẽ giữ nhầm A.
- D đúng: lọc giá trước đếm/tính mean; A còn một hàng nên bị loại, B hai hàng mean 80.

**Đối chiếu:** nhóm 4; K37, K39; mức Vận dụng. **Kiến thức và bẫy:** WHERE lọc hàng trước, HAVING lọc nhóm sau; đổi tập giá tính mean và nhóm còn lại; Ít nhất N hàng/giá biết/giá đạt ngưỡng là ba yêu cầu; đổi WHERE phải rà SELECT/COUNT/HAVING. **Đọc lại:** NB ô 52–55; GK câu 24.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-047

```python
d = pd.read_csv('reviews.csv.gz', usecols=['listing_id','date','diem'],
    dtype={'listing_id':'str','diem':'float64'},
    na_values={'diem':['?']}, parse_dates=['date'])
assert pd.api.types.is_datetime64_any_dtype(d['date'])
assert len(d)==4 and d.loc[0,'listing_id']=='001'
assert d.loc[0,'date']==pd.Timestamp('2025-01-01') and d['diem'].isna().sum()==1
```
Không; truyền parse_dates vẫn cần kiểm kiểu và nội dung sau đọc. Đuôi .gz cho pandas nhận nén, không thay quy tắc mã/thiếu. Một listing có thể có nhiều review; bốn hàng không là bốn listing khác nhau.

**Hướng dẫn chấm:** 2 điểm: đọc nén/chọn cột/schema/NA 0,75; parse_dates và kiểm dtype/ngày 0,75; kiểm mã/hàng/thiếu và diễn giải review 0,5.

**Đối chiếu:** nhóm 1; K10, K09, K13; mức Vận dụng. **Kiến thức và bẫy:** parse_dates trong cách dùng lab; kiểm dtype/ngày sau đọc, không chỉ tin đã truyền tham số; pandas nhận diện .csv.gz từ tên file; nén không thay schema dữ liệu; Kiểm shape, dtype logic, mã và số thiếu sau đọc; không kiểm riêng số hàng. **Đọc lại:** NB ô 68–69; LAB W2, bước 1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-048

(a) So số đang ở °F với ngưỡng °C; raise_for_status không kiểm đơn vị, assert chỉ đếm hàng.
```python
assert x['daily_units']['temperature_2m_max'] == '°F'
d = pd.DataFrame(x['daily'])
d['t_c'] = (d['temperature_2m_max']-32)*5/9
hot = d.loc[d['t_c']>=35]
```
(c) 01/02 và 03/02; cột t_c là 35,30,40. Kiểm tay 95°F=35°C và giữ đúng biên, đối chiếu daily_units trước chuyển. Nếu dịch vụ đã trả °C thì không đổi thêm lần nữa.

**Hướng dẫn chấm:** 3 điểm: (a) HTTP/shape không kiểm đơn vị 1; (b) đổi đúng và >=35 1; (c) hai ngày và kiểm tay/metadata 1. Nhận lọc bằng biểu thức không tạo cột nếu tương đương.

**Đối chiếu:** nhóm 3; K23, K26, K25; mức Phân loại. **Kiến thức và bẫy:** 200/raise_for_status chỉ kiểm HTTP, không bảo đảm đúng đơn vị, cấu trúc hay đủ dữ liệu; daily_units, đổi °F sang °C theo công thức, biên từ 35°C; kiểm đơn vị trước lọc; JSON object→dict, array→list; chọn daily; các danh sách tương ứng vị trí và độ dài. **Đọc lại:** NB ô 30–35,42–44; LAB bước 4.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-049

SQL có 3 nhóm: A:(2,10), B:(1,30), khu NULL:(1,20). Pandas mặc định dropna=True có 2 nhóm A,B nên đã bỏ listing thiếu khu.
```python
p = d.groupby('khu', dropna=False).agg(
    n=('gia','size'), tb=('gia','mean'))
```
Giữ nhóm khóa thiếu để cùng phạm vi SQL. Mean A chỉ dùng giá 10 (mẫu số 1), n A vẫn 2 hàng. Hai công cụ giống nhau chỉ hỗ trợ kiểm triển khai; vẫn phải kiểm tập đối tượng, đơn vị và yêu cầu nghiên cứu, vì cả hai có thể cùng tính sai mục tiêu.

**Hướng dẫn chấm:** 2 điểm: số nhóm và nguyên nhân 0,5; dropna=False 0,5; ba n/mean và mẫu số A 0,5; giới hạn kết quả trùng 0,5.

**Đối chiếu:** nhóm 4; K49, K35, K37; mức Vận dụng. **Kiến thức và bẫy:** Đối chiếu cùng snapshot, lọc, đơn vị, thiếu và nhóm khóa thiếu; giống kết quả chưa chắc đúng yêu cầu; COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết; WHERE lọc hàng trước, HAVING lọc nhóm sau; đổi tập giá tính mean và nhóm còn lại. **Đọc lại:** NB ô 51,63,66; LAB bước 7 (đối chiếu quy tắc thiếu).

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-050

(a) Lưu cả bytes phản hồi để giữ daily, đơn vị và timezone. Khóa ngày review phải cùng quy ước ngày địa phương; cùng chuỗi ngày nhưng khác cách xác định ngày có thể ghép sai.
```python
Path(raw_path).write_bytes(r.content)
meta = {'url':r.url, 'downloaded_at':downloaded_at}
Path(meta_path).write_text(json.dumps(meta), encoding='utf-8')
```
Giả sử raw_path/meta_path đã chọn riêng và thư mục tồn tại. (c) Timestamp theo giây có thể trùng tên và ghi đè; dùng tên/đường dẫn không trùng hoặc kiểm tồn tại trước ghi. Đọc lại kiểm khoảng ngày, đơn vị, địa điểm/metadata; tên file không chứng minh nội dung đúng. Không cần thuộc cách định dạng thời điểm.

**Hướng dẫn chấm:** 3 điểm: giữ bytes/cả metadata và ý nghĩa timezone 1; hai file/thông tin URL+thời điểm 1; nguy cơ trùng/ghi đè và kiểm nội dung 1. Nhận lưu params riêng kèm endpoint thay URL đầy đủ.

**Đối chiếu:** nhóm 3; K28, K30, K27; mức Phân loại. **Kiến thức và bẫy:** r.content là bytes; lưu phản hồi thô cả đơn vị/metadata, URL/tham số và thời điểm tải; Tên có timestamp không chứng minh nội dung đúng; độ phân giải giây không bảo đảm tên duy nhất; timezone diễn giải khóa ngày; không gộp nhầm ngày của hai nguồn khác quy ước. **Đọc lại:** NB ô 36–41; LAB bước 3–6.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR09

**Đáp án: A.**

- A đúng: nhận diện lựa chọn cột, không suy toàn bộ định dạng plan hay cam kết thời gian.
- B sai: Projections mô tả cột được dùng, không là giá trị tổng hợp.
- C sai: projection chọn cột, không có nghĩa LIMIT 1.
- D sai: plan không là phép benchmark hay bảo đảm tỷ lệ tốc độ.

**Đối chiếu:** nhóm 2; K55, K54; mức Bổ sung. **Kiến thức và bẫy:** Nhận diện Projections trong PARQUET_SCAN: những cột cần đọc, không học thuộc toàn plan; EXPLAIN trả kế hoạch, không phải kết quả hay phép đo tốc độ truy vấn. **Đọc lại:** NB ô 74–75: tự học query plan.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-MR10

```python
s = 0.0; n = 0
for c in pd.read_csv('gia.csv', usecols=['gia'], chunksize=3):
    v = c.loc[c['gia']>=30, 'gia']
    s += v.sum(); n += v.count()
tb = s/n if n else np.nan
```
Tập đúng 30,50,70,110: sum=260,count=4,mean=65. Mean khối sau lọc là 30,60,110; trung bình không trọng số của chúng là 200/3, khác 65 vì count khối là 1,2,1. Chia bảy tính cả hàng ngoài ngưỡng và thiếu. Cần thuật toán sum/count, kể cả khi vài khối rỗng sau lọc.

**Hướng dẫn chấm:** 2 điểm: lọc đúng >= trước tổng hợp 0,5; sum/count từng khối không gom 0,75; kết quả và giải thích mẫu số/trọng số 0,75.

**Đối chiếu:** nhóm 1; K52; mức Bổ sung. **Kiến thức và bẫy:** Cộng dồn sum/count rồi chia; không mean các mean khối; lọc đúng tập từng khối. **Đọc lại:** NB ô 72–73: tự học tổng hợp khối có lọc.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

### Độ bao phủ sau đợt 5

Đã dùng 51/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K12, K29, K31, K46, K47, K48, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 6

### Câu trọng tâm

#### B6-051

**Đáp án: B.**

- A sai: read_csv hỗ trợ nhận gzip theo đuôi file trong cách dùng bài.
- B đúng: nén thay cách lưu byte trên đĩa, không làm nội dung CSV tự có schema; dtype giữ mã lúc đọc.
- C sai: cột mã không phải bộ đếm dòng.
- D sai: CSV nén vẫn được suy luận kiểu như văn bản khi đọc; nén không lưu schema mã.

**Đối chiếu:** nhóm 1; K09, K01; mức Nền tảng. **Kiến thức và bẫy:** pandas nhận diện .csv.gz từ tên file; nén không thay schema dữ liệu; CSV là văn bản; suy luận kiểu có thể mất số 0 đầu; mã khác đại lượng. **Đọc lại:** NB ô 68–69; LAB W2, bước 1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-052

**Đáp án: A.**

- A đúng: SQL truy vấn trực tiếp Parquet và trả kết quả tổng hợp; pandas cũng có thể đọc chọn cột, chọn công cụ theo nhu cầu/bộ nhớ.
- B sai: bỏ cách truy vấn Parquet trực tiếp đã học.
- C sai: không có bảo đảm tốc độ tuyệt đối.
- D sai: read_parquet có columns, read_csv có usecols/chunksize trong phạm vi tự học.

**Đối chiếu:** nhóm 2; K41, K32, K15; mức Vận dụng. **Kiến thức và bẫy:** SQL trên Parquet chọn cột/tổng hợp tại file; công cụ theo nguồn, bộ nhớ và thao tác, không luôn nhanh hơn; DuckDB chạy cùng chương trình; SQL mô tả kết quả; tên biến DataFrame, truy vấn file, .df trả DataFrame; to_parquet/read_parquet và columns chọn cột; kiểm shape, mã, giá trị đọc lại. **Đọc lại:** NB ô 61–65; LAB bước 8.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-053

**Đáp án: D.**

- A sai: URL và tham số không là cam kết bất biến của nguồn.
- B sai: tên file không thay kiểm metadata/nội dung.
- C sai: khác thời điểm/nguồn dữ liệu và không tái lập snapshot.
- D đúng: snapshot giữ đúng bytes phản hồi cũ; cùng URL/khoảng quá khứ vẫn có thể được dịch vụ cập nhật.

**Đối chiếu:** nhóm 3; K28, K29; mức Vận dụng. **Kiến thức và bẫy:** r.content là bytes; lưu phản hồi thô cả đơn vị/metadata, URL/tham số và thời điểm tải; Đọc snapshot khác gọi API lại; khoảng quá khứ cố định không thay việc giữ phản hồi đã dùng. **Đọc lại:** NB ô 36–41; LAB bước 3.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-054

**Đáp án: D.**

- A sai: so sánh bằng NULL không cho TRUE để WHERE giữ hàng.
- B sai: giá 0 là giá đã biết, không là dấu hiệu thiếu.
- C sai: lấy phần bù: các giá đã biết 10 và 0.
- D đúng: kiểm thiếu bằng IS NULL; ở ví dụ DataFrame này hai np.nan được tiếp nhận thành NULL.

**Đối chiếu:** nhóm 4; K34; mức Nền tảng. **Kiến thức và bẫy:** Pandas thiếu số vào DuckDB thành NULL trong các ví dụ; =NULL không giữ hàng, dùng IS NULL/IS NOT NULL. **Đọc lại:** NB ô 56–57; BG §3.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-055

**Đáp án: B.**

- A sai: lặp review của một listing không tạo bốn listing khác nhau.
- B đúng: hai tỷ lệ có đơn vị quan sát/mẫu số khác nhau; review không tự bằng booking và tương quan yếu không loại mọi dạng quan hệ.
- C sai: dùng cơ cấu listing làm cơ cấu review.
- D sai: khái quát từ tương quan tuyến tính yếu sang mọi quan hệ và cả booking chưa quan sát.

**Đối chiếu:** nhóm 5; K47, K48; mức Vận dụng. **Kiến thức và bẫy:** Tỷ lệ review theo loại khác tỷ lệ listing; review không tự bằng booking; Tương quan tuyến tính yếu từ hệ số cho sẵn không chứng minh nhân quả hoặc không có mọi dạng quan hệ. **Đọc lại:** LAB bước 6,9; ô 23–24,29–31.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-056

**Đáp án: D.**

- A sai: đã trả lời số review mọi năm, giữ nhầm A.
- B sai: chưa áp điều kiện ít nhất hai review.
- C sai: dùng tập hàng khác cho điều kiện giữ nhóm và số đếm được yêu cầu.
- D đúng: lọc phạm vi năm trước tính n; A không đủ dù có nhiều review cũ.

**Đối chiếu:** nhóm 4; K40, K37; mức Vận dụng. **Kiến thức và bẫy:** year(date): review theo năm rồi nhóm; HAVING đếm trong phạm vi năm, không lẫn mọi năm; WHERE lọc hàng trước, HAVING lọc nhóm sau; đổi tập giá tính mean và nhóm còn lại. **Đọc lại:** LAB bước 7,10.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-057

Mã có thể mất số 0 đầu, khu NA có thể thành thiếu, ngày không tự chắc chắn là datetime. CSV không giữ schema.
```python
r = pd.read_csv('review.csv', keep_default_na=False,
    dtype={'listing_id':'str','khu':'str','diem':'float64'},
    na_values={'diem':['']}, parse_dates=['date'])
pd.testing.assert_frame_equal(d, r)
```
Nhận kiểm tương đương: shape (4,4), mã 001 và khu NA giữ nguyên, kiểu ngày cùng bốn ngày, diem float có một thiếu và giá 0 không mất. Nếu so ở backend khác, đối chiếu kiểu logic/nội dung phù hợp thay vì bắt biểu diễn chuỗi phải giống mọi môi trường.

**Hướng dẫn chấm:** 2 điểm: ba nguy cơ 0,5; schema/keep_default_na/NA/ngày 1; kiểm nội dung và kiểu 0,5.

**Đối chiếu:** nhóm 1; K12, K10, K13; mức Vận dụng. **Kiến thức và bẫy:** Ghi CSV không giữ schema; đọc lại cần dtype, NA và ngày phù hợp; parse_dates trong cách dùng lab; kiểm dtype/ngày sau đọc, không chỉ tin đã truyền tham số; Kiểm shape, dtype logic, mã và số thiếu sau đọc; không kiểm riêng số hàng. **Đọc lại:** NB ô 15; LAB W1,W2, bước 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-058

```python
params = dict(latitude=-33.45, longitude=-70.67,
    start_date='2025-07-01', end_date='2025-07-03',
    daily='temperature_2m_max', timezone='America/Santiago')
```
Đối chiếu daily.time đúng ba ngày 01–03/07; nhánh đại lượng và các dãy có độ dài tương ứng; daily_units và timezone đúng (cần °C hoặc chuyển đúng đơn vị). Kiểm địa điểm/URL thực gửi khi đối chiếu metadata; giữ cùng quy ước ngày với review. Lưu phản hồi thô và URL/thời điểm tải; các lần phân tích sau đọc snapshot đó, không coi gọi lại archive cùng khoảng ngày là giữ nguyên nội dung.

**Hướng dẫn chấm:** 2 điểm: params đúng phạm vi/vị trí/đại lượng/múi giờ 0,75; ba kiểm tra ý nghĩa 0,75; snapshot phân biệt gọi lại 0,5.

**Đối chiếu:** nhóm 3; K21, K27, K29; mức Vận dụng. **Kiến thức và bẫy:** Phân biệt dự báo và lịch sử; chọn vị trí, đại lượng, khoảng ngày, múi giờ theo bảng tham số được cho; timezone diễn giải khóa ngày; không gộp nhầm ngày của hai nguồn khác quy ước; Đọc snapshot khác gọi API lại; khoảng quá khứ cố định không thay việc giữ phản hồi đã dùng. **Đọc lại:** LAB bước 3–6, tự làm 1; NB ô 36–41.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt. Dùng phản hồi/đầu vào cố định hoặc mô phỏng Requests; không gọi API thật và không chứng minh dịch vụ thật chấp nhận tham số mới.

#### B6-059

```sql
SELECT l.id, COUNT(rv.rid) AS n_review, AVG(rv.diem) AS tb
FROM l LEFT JOIN rv ON l.id=rv.listing_id AND year(rv.date)=2025
GROUP BY l.id ORDER BY l.id;
```
(b) COUNT(*) đếm hàng đệm của C,D thành 1; COUNT(diem) bỏ review r2 của A dù review có thật nhưng chưa biết điểm. Đặt năm trong ON để không loại listing không có đối ứng năm đó.
(c) A:(1,NULL), B:(2,4.5), C:(0,NULL), D:(0,NULL). Mean B chia hai điểm 4,5; A có review nhưng không điểm biết. len=4 chỉ kiểm số hàng tổng hợp, không kiểm n_review, điểm hay năm; cần đối chiếu r2,r3,r4 và số đếm từng id.

**Hướng dẫn chấm:** 3 điểm: JOIN/năm trong ON và GROUP BY 1; COUNT khóa review/AVG và lý do 1; bốn kết quả, mẫu số và kiểm vượt len 1. Nhận lọc rv theo năm trước LEFT JOIN bằng cách hợp lệ đã nêu rõ.

**Đối chiếu:** nhóm 4; K45, K43, K50; mức Phân loại. **Kiến thức và bẫy:** COUNT(*) sau LEFT JOIN khác số đối ứng; đếm khóa phải không NULL khác đếm cột thông tin có thể thiếu; WHERE cột phải loại hàng đệm NULL; ON giới hạn đối ứng mà vẫn giữ trái; Kiểm độ khớp qua khóa thật và metadata, không chỉ số hàng/NaN hay assert đơn lẻ. **Đọc lại:** NB ô 49–50,58–60; LAB bước 9–10; GK câu 15,24.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

#### B6-060

(a) w trùng ngày 01/01 với hai số đo; phải kiểm phạm vi/múi giờ/nguồn rồi xác định bản đúng, không tùy tiện drop_duplicates để ép số hàng. Kiểm time duy nhất và hai bên cùng định dạng, cùng quy ước ngày.
```python
n = rv.assign(time=rv['date'].dt.strftime('%Y-%m-%d')).groupby('time').size().rename('n_review')
assert w_ok['time'].is_unique
kq = w_ok.merge(n.reset_index(), on='time', how='left', validate='one_to_one')
```
(b,c) Ba hàng là ba ngày thời tiết: (01/01,30,2),(02/01,32,2),(03/01,33,NaN). Ngày cuối không có dòng review trong bảng xét; chưa chứng minh không review ngoài phạm vi thu thập. So SQL phải cùng snapshot, phạm vi ngày, đơn vị, quy tắc khóa/thiếu và loại JOIN; kết quả trùng chưa chứng minh đúng mục tiêu. Mã số 1→chuỗi '1' không khớp '001': cần lấy lại mã nguồn đúng schema hoặc quy tắc mã đã được xác nhận, không mặc định chuyển kiểu là đủ.

**Hướng dẫn chấm:** 3 điểm: trùng ngày/không chọn tùy tiện, cùng quy ước 1; đếm và ghép tạo đúng ba hàng 1; đơn vị hàng/số đếm/thiếu, đối chiếu cùng đầu vào và mã 001 1. Nhận các cách groupby/SQL tương đương. Không bắt thuộc strftime: có thể tạo khóa ngày ISO bằng cách tương đương đã giải thích.

**Đối chiếu:** nhóm 5; K31, K46, K49; mức Phân loại. **Kiến thức và bẫy:** Từ dữ liệu review theo ngày ghép thời tiết: phạm vi, khóa ngày, tính duy nhất và ngày không có dòng; Khóa id/listing_id cùng kiểu và ý nghĩa; không khẳng định khác kiểu luôn lỗi hoặc luôn đổi đúng; Đối chiếu cùng snapshot, lọc, đơn vị, thiếu và nhóm khóa thiếu; giống kết quả chưa chắc đúng yêu cầu. **Đọc lại:** LAB W2, bước 5–7,9; NB ô 66.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR11

**Đáp án: B.**

- A sai: công khai key không nâng quota và làm lộ bí mật.
- B đúng: tránh gọi lại không cần thiết, giữ đầu vào ổn định và không lộ bí mật; vẫn tôn trọng quota.
- C sai: JSON lỗi không là quan sát để thêm vào bảng.
- D sai: cùng URL không miễn hạn mức và không bảo đảm nội dung bất biến.

**Đối chiếu:** nhóm 3; K56, K57, K29; mức Bổ sung. **Kiến thức và bẫy:** API key từ biến môi trường/Colab Secrets, không ghi khóa thật vào notebook hoặc prompt; 429 và giới hạn truy cập: làm theo hướng dẫn dịch vụ, không có thời gian nghỉ chuẩn cho mọi API; Đọc snapshot khác gọi API lại; khoảng quá khứ cố định không thay việc giữ phản hồi đã dùng. **Đọc lại:** NB ô 76: tự học key/quota; NB ô 36–41.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu cơ chế hoặc thiết kế, không có output cần chạy).

#### B6-MR12

```python
l = l.assign(id=l['id'].astype('str'))
```
```sql
SELECT rv.listing_id,l.name,COUNT(*) AS n FROM rv
LEFT JOIN l ON rv.listing_id=l.id WHERE year(rv.date)=2025
GROUP BY rv.listing_id,l.name
ORDER BY n DESC,rv.listing_id ASC LIMIT 2;
```
Kết quả ('1','An',2),('2','Binh',2); '3' có một review. Điều kiện năm loại review 2024 của '1'; khóa phải duy nhất nên mỗi review không bị nhân. LIMIT và khóa phụ xác định rõ cách xử lý đồng hạng. Chỉ đổi sang str đủ ở câu này vì quy ước không đệm 0 đã được cho, không khái quát sang mã '001'.

**Hướng dẫn chấm:** 2 điểm: chuẩn hóa theo quy ước và đúng JOIN 0,5; năm/nhóm/COUNT 0,75; ORDER BY hai khóa/LIMIT và kết quả 0,75. Nhận nhóm review trước rồi ghép tên nếu giữ đúng một hàng mỗi listing.

**Đối chiếu:** nhóm 5; K58, K46, K40; mức Bổ sung. **Kiến thức và bẫy:** Top-k review đúng năm: ORDER BY/LIMIT và đồng hạng; thống nhất mã với bảng tên; Khóa id/listing_id cùng kiểu và ý nghĩa; không khẳng định khác kiểu luôn lỗi hoặc luôn đổi đúng; year(date): review theo năm rồi nhóm; HAVING đếm trong phạm vi năm, không lẫn mọi năm. **Đọc lại:** LAB tự làm 2, ô 34.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ; các assert đạt.

### Độ bao phủ sau đợt 6

Đã dùng 58/58 mục tiêu trong yêu cầu trả lời. Không còn mục tiêu thiếu trong phạm vi đã xác định.

## Đối chiếu các bẫy bắt buộc

| Bẫy | Câu đánh giá |
| --- | --- |
| Mã thành số, astype không khôi phục | 001,011,057 |
| dtype chuỗi / NA mặc định; tắt NA quên ô trống | 006,009,016,031 |
| na_values chung làm mất mã hợp lệ | 009,020 |
| Parquet không sửa đầu vào sai | 010,022,029 |
| usecols / quét CSV / thời gian | 021,041,MR03,MR08 |
| JSON đọc được / HTTP; 400 / timeout | 007,018,040 |
| raise_for_status / đơn vị và dữ liệu | 018,027,048 |
| Ngưỡng °C trên °F | 027,048 |
| Gọi API lại / snapshot | 050,053,058 |
| COUNT hàng / COUNT giá biết / thiếu | 008,017,028,037,039,044 |
| WHERE / HAVING; mất nhóm thiếu 0 | 008,024,028,039 |
| LEFT JOIN / WHERE phải; ON và OR NULL | 015,025,030,035 |
| Đếm review / listing / booking | 019,034,055,056,MR12 |
| Đối chiếu khác đầu vào hoặc thiếu | 049,057,060 |
| Mean các mean khối / sum-count | MR02,MR04,MR10 |

Cặp đối chiếu chỉ đánh dấu ở đây: **006/031** (NA mặc định/bỏ mặc định); **007/018** (điểm dừng và cách kiểm trước xử lý); **008/024** (lọc hàng/lọc nhóm); **025/030** (WHERE/ON, giới hạn OR IS NULL); **010/012** (lưu đầu vào sai/đúng); **MR02/MR04/MR10** (tính tay, viết vòng tổng hợp, đổi tập hàng).

## Đối chiếu cuối bộ

- Đủ **B6-001–B6-060: 60 câu = 40 TN + 20 TL**, nhóm chính **14/8/14/16/8**.
- Đủ **B6-MR01–B6-MR12: 12 câu = 8 TN + 4 TL**, đặt riêng từng đợt.
- Mức độ thiết kế: **15 nền tảng + 33 vận dụng + 12 phân loại**, không phải tần suất thi chính thức hay dự báo chắc chắn.
- **58/58 mục tiêu** thực sự được dùng để trả lời. Các câu SQL ba phần gần cấu trúc GK câu 24 gồm **008,019,028,039**; giữ/đổi phạm vi, COUNT/WHERE/HAVING và ý nghĩa được kiểm trực tiếp.
- Đọc nén, ngày, API lịch sử, year(date) ở phần chính theo LAB; chunksize/benchmark/EXPLAIN/key/quota và top-k tự làm giữ nhãn bổ sung. Không đếm các tên API chỉ tình cờ nhắc trong đáp án là mục tiêu đã phủ.
- Đã rà trùng ý, các cặp đối chiếu có chủ đích thay đổi cơ chế/tập hàng hoặc yêu cầu kiểm chứng, không chỉ đổi số/tên từ đề gốc. Độ bao phủ bài học khác mức ưu tiên từ đề mẫu; không mở rộng toàn sách/website liên kết.

Đã thực thi **66/72 câu** bằng các thư viện nêu ở đầu; **6 câu** cơ chế/thiết kế được kiểm bằng suy luận, chưa thực thi. API chỉ mô phỏng/đầu vào cố định; không chứng minh tham số thật hợp lệ với dịch vụ và không dùng forecast thật làm đáp án. Không đo benchmark thật; các số liệu benchmark nếu có được đề cung cấp để diễn giải.

Phân bố đáp án trọng tâm: {'A': 10, 'B': 10, 'C': 10, 'D': 10}; bổ sung: {'A': 2, 'B': 2, 'C': 2, 'D': 2}.

## Dấu vết độ bao phủ

| Mục tiêu | Câu dùng để trả lời |
| --- | --- |
| K01 | B6-001, B6-011, B6-051 |
| K02 | B6-006, B6-016, B6-020 |
| K03 | B6-009, B6-020 |
| K04 | B6-009, B6-031 |
| K05 | B6-016, B6-031 |
| K06 | B6-009, B6-026 |
| K07 | B6-001, B6-010, B6-011, B6-022 |
| K08 | B6-021, B6-038, B6-041 |
| K09 | B6-041, B6-047, B6-051 |
| K10 | B6-047, B6-057 |
| K11 | B6-038 |
| K12 | B6-057 |
| K13 | B6-006, B6-020, B6-038, B6-047, B6-057 |
| K14 | B6-002, B6-032 |
| K15 | B6-010, B6-012, B6-029, B6-032, B6-052 |
| K16 | B6-010, B6-022 |
| K17 | B6-012, B6-029 |
| K18 | B6-029, B6-042 |
| K19 | B6-002, B6-042 |
| K20 | B6-003, B6-013, B6-033 |
| K21 | B6-033, B6-058 |
| K22 | B6-007, B6-018, B6-040 |
| K23 | B6-013, B6-018, B6-027, B6-036, B6-048 |
| K24 | B6-040 |
| K25 | B6-018, B6-023, B6-036, B6-043, B6-048 |
| K26 | B6-027, B6-048 |
| K27 | B6-050, B6-058 |
| K28 | B6-050, B6-053 |
| K29 | B6-053, B6-058, B6-MR11 |
| K30 | B6-050 |
| K31 | B6-060 |
| K32 | B6-005, B6-052 |
| K33 | B6-004, B6-014 |
| K34 | B6-004, B6-014, B6-017, B6-037, B6-054 |
| K35 | B6-008, B6-017, B6-019, B6-024, B6-034, B6-039, B6-044, B6-049 |
| K36 | B6-028, B6-037 |
| K37 | B6-008, B6-024, B6-028, B6-046, B6-049, B6-056 |
| K38 | B6-028 |
| K39 | B6-008, B6-019, B6-039, B6-046 |
| K40 | B6-019, B6-034, B6-056, B6-MR12 |
| K41 | B6-039, B6-052 |
| K42 | B6-015, B6-030, B6-035 |
| K43 | B6-025, B6-030, B6-059 |
| K44 | B6-030 |
| K45 | B6-035, B6-045, B6-059 |
| K46 | B6-060, B6-MR12 |
| K47 | B6-055 |
| K48 | B6-055 |
| K49 | B6-049, B6-060 |
| K50 | B6-025, B6-045, B6-059 |
| K51 | B6-MR01, B6-MR04 |
| K52 | B6-MR02, B6-MR04, B6-MR10 |
| K53 | B6-MR03, B6-MR08 |
| K54 | B6-MR05, B6-MR09 |
| K55 | B6-MR09 |
| K56 | B6-MR06, B6-MR11 |
| K57 | B6-MR07, B6-MR11 |
| K58 | B6-MR12 |
