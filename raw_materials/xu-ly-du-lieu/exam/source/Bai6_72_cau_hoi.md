# BÀI 6 — KẾT NỐI VÀ TRUY XUẤT DỮ LIỆU NGOÀI

72 câu: 60 trọng tâm và 12 tự học, chia sáu đợt.

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

## Ma trận và kế hoạch sáu đợt

Độ khó là tham số thiết kế, không phải kết quả đo thực nghiệm hay tỷ trọng chính thức của đề thi. Mỗi câu tính vào một nhóm chính, có tối đa hai mục tiêu phụ.

| Nhóm chính | Tổng | TN | TL | Nền tảng | Vận dụng | Phân loại |
| --- | --- | --- | --- | --- | --- | --- |
| CSV, kiểu dữ liệu và quy ước giá trị thiếu | 14 | 9 | 5 | 7 | 5 | 2 |
| Parquet, đọc chọn cột và kiểm chứng đọc/ghi | 8 | 6 | 2 | 1 | 7 | 0 |
| API, HTTP, JSON, đơn vị và lưu phản hồi | 14 | 9 | 5 | 1 | 10 | 3 |
| SQL lọc, nhóm, tổng hợp và NULL | 16 | 10 | 6 | 5 | 6 | 5 |
| JOIN, DuckDB và kết hợp/đối chiếu nguồn | 8 | 6 | 2 | 1 | 5 | 2 |

| Đợt | Trọng tâm | TN/TL | Nền tảng/Vận dụng/Phân loại | Bổ sung | TN/TL |
| --- | --- | --- | --- | --- | --- |
| 1 | B6-001–B6-010 | 7/3 | 3/5/2 | MR01–MR02 | 2/0 |
| 2 | B6-011–B6-020 | 7/3 | 3/5/2 | MR03–MR04 | 1/1 |
| 3 | B6-021–B6-030 | 7/3 | 3/5/2 | MR05–MR06 | 2/0 |
| 4 | B6-031–B6-040 | 7/3 | 2/6/2 | MR07–MR08 | 1/1 |
| 5 | B6-041–B6-050 | 6/4 | 2/6/2 | MR09–MR10 | 1/1 |
| 6 | B6-051–B6-060 | 6/4 | 2/6/2 | MR11–MR12 | 1/1 |

## Mục tiêu nhỏ và mã câu dự kiến

Danh mục lập trước khi soạn câu. Mã câu trong bảng bỏ tiền tố B6-. Chỉ tính bao phủ nếu nội dung được dùng để trả lời câu; không tính mục chỉ nhắc tình cờ trong lời giải.

| Mã | Mục tiêu | Ưu tiên | Câu dự kiến | Nguồn đọc lại |
| --- | --- | --- | --- | --- |
| K01 | CSV là văn bản; suy luận kiểu có thể mất số 0 đầu; mã khác đại lượng | Trọng tâm | 001,011 | BG §1; NB ô 4–11; LAB W1 |
| K02 | dtype theo cột không tự tắt nhận diện NA mặc định; dtype chuỗi vẫn có thiếu | Trọng tâm | 006,016 | NB ô 9–11; BG §1; GK câu 14 |
| K03 | na_values theo cột khác danh sách chung; không làm mất mã hợp lệ ở cột khác | Trọng tâm | 009,020 | BG §1; NB ô 9–14; LAB W1 |
| K04 | keep_default_na=False tắt NA/N/A/null/ô trống mặc định; phải khai báo lại dấu hiệu thiếu | Trọng tâm | 009,031 | BG §1; NB ô 9–14 |
| K05 | Ép float64 khi còn chuỗi không hợp lệ có thể gây ValueError | Trọng tâm | 016,009 | BG §1; NB ô 9–10 |
| K06 | Thiếu giá khác giá 0; tập giá biết và mẫu số sau đọc | Trọng tâm | 009,026 | BG §1 bài tập 1; LAB W1 |
| K07 | astype(str) sau đọc sai không khôi phục mã gốc; đọc lại từ raw đúng schema | Trọng tâm | 001,011 | NB ô 6–11,15; BG §1 |
| K08 | usecols giảm cột trong DataFrame; CSV vẫn quét văn bản, nén còn giải nén; thời gian không tỷ lệ số cột | Trọng tâm | 021,041 | NB ô 15,18–20; LAB bước 1 |
| K09 | pandas nhận diện .csv.gz từ tên file; nén không thay schema dữ liệu | Trọng tâm | 051 | NB ô 68–69; LAB phần 1, ô 7–11 |
| K10 | parse_dates trong cách dùng lab; kiểm dtype/ngày sau đọc, không chỉ tin đã truyền tham số | Trọng tâm | 047,057 | NB ô 69; LAB W2, bước 1 |
| K11 | Bản rút gọn và đầy đủ có thể khác schema, cùng price nhưng số hoặc chuỗi tiền tệ | Trọng tâm | 038 | NB ô 18–21; LAB ô 10–14 |
| K12 | Ghi CSV không giữ schema; đọc lại cần dtype, NA và ngày phù hợp | Trọng tâm | 057 | NB ô 15; LAB bước 2 |
| K13 | Kiểm shape, dtype logic, mã và số thiếu sau đọc; không kiểm riêng số hàng | Trọng tâm | 006,057 | NB ô 11,21; LAB W1,W2 |
| K14 | Parquet nhị phân dạng bảng, lưu kiểu và theo cột; có thể bỏ cột không dùng | Trọng tâm | 002,032 | NB ô 15–17; BG §1 |
| K15 | to_parquet/read_parquet và columns chọn cột; kiểm shape, mã, giá trị đọc lại | Trọng tâm | 012,032 | NB ô 16–17; LAB bước 2 |
| K16 | Parquet không sửa dữ liệu/kiểu đã sai; chuỗi tiền tệ không tự thành số | Trọng tâm | 010,022 | BG §1; LAB ô 11–14 |
| K17 | Giữ schema logic khác bảo đảm mọi backend/dtype biểu diễn y hệt ở mọi môi trường | Trọng tâm | 012,029 | NB ô 17; LAB ô 13; giới hạn theo yêu cầu |
| K18 | raw giữ đầu vào gốc, processed bảng xử lý; snapshot đã tải khác tải lại cùng URL | Trọng tâm | 042,029 | NB ô 18–20; BG §1 |
| K19 | CSV/Parquet phục vụ nhu cầu khác nhau; kích thước và tốc độ không có cam kết tuyệt đối | Trọng tâm | 002,042 | NB ô 15,70–71; LAB bước 2 |
| K20 | API, endpoint, params ghép URL và r.url để đối chiếu yêu cầu thực gửi | Trọng tâm | 003,013 | BG §2; NB ô 22–26 |
| K21 | Phân biệt dự báo và lịch sử; chọn vị trí, đại lượng, khoảng ngày, múi giờ theo bảng tham số được cho | Trọng tâm | 033,058 | NB ô 23; LAB bước 3 |
| K22 | JSON lỗi vẫn đọc được; HTTP 4xx/5xx và raise_for_status trước xử lý dữ liệu; 400 không phải timeout | Trọng tâm | 007,018 | NB ô 27–28; GK câu 16 |
| K23 | 200/raise_for_status chỉ kiểm HTTP, không bảo đảm đúng đơn vị, cấu trúc hay đủ dữ liệu | Trọng tâm | 018,048 | NB ô 27–35; LAB bước 3–4 |
| K24 | Requests timeout giới hạn chờ kết nối/đọc, không phải deadline tổng thời gian | Trọng tâm | 040 | NB ô 23–24 |
| K25 | JSON object→dict, array→list; chọn daily; các danh sách tương ứng vị trí và độ dài | Trọng tâm | 023,043 | NB ô 27–35; LAB bước 4 |
| K26 | daily_units, đổi °F sang °C theo công thức, biên từ 35°C; kiểm đơn vị trước lọc | Trọng tâm | 027,048 | NB ô 42–44; LAB bước 4 |
| K27 | timezone diễn giải khóa ngày; không gộp nhầm ngày của hai nguồn khác quy ước | Trọng tâm | 050,058 | NB ô 30–35; LAB bước 3–6 |
| K28 | r.content là bytes; lưu phản hồi thô cả đơn vị/metadata, URL/tham số và thời điểm tải | Trọng tâm | 050,053 | NB ô 36–41; LAB bước 3 |
| K29 | Đọc snapshot khác gọi API lại; khoảng quá khứ cố định không thay việc giữ phản hồi đã dùng | Trọng tâm | 053,058 | NB ô 36–41; LAB bước 3, tự làm 1 |
| K30 | Tên có timestamp không chứng minh nội dung đúng; độ phân giải giây không bảo đảm tên duy nhất | Trọng tâm | 050 | NB ô 36–39; giới hạn theo yêu cầu |
| K31 | Từ dữ liệu review theo ngày ghép thời tiết: phạm vi, khóa ngày, tính duy nhất và ngày không có dòng | Trọng tâm | 060 | LAB bước 5–6 |
| K32 | DuckDB chạy cùng chương trình; SQL mô tả kết quả; tên biến DataFrame, truy vấn file, .df trả DataFrame | Trọng tâm | 005,052 | NB ô 45–51,61–65; LAB phần 3 |
| K33 | SELECT/FROM/WHERE/AS/ORDER BY/DESC: lọc và sắp kết quả, NULL không đạt so sánh ngưỡng | Trọng tâm | 004,014 | NB ô 47–50 |
| K34 | Pandas thiếu số vào DuckDB thành NULL trong các ví dụ; =NULL không giữ hàng, dùng IS NULL/IS NOT NULL | Trọng tâm | 017,037 | NB ô 49–57; BG §3 |
| K35 | COUNT(*) khác COUNT(cột); AVG/MEDIAN bỏ NULL, giữ giá 0 đã biết | Trọng tâm | 017,044 | NB ô 49–51,62; LAB bước 8 |
| K36 | Nhóm toàn giá thiếu: COUNT(*)>0, COUNT(gia)=0, AVG(gia) NULL | Trọng tâm | 037,028 | BG §3; suy luận từ phép tổng hợp đã học |
| K37 | WHERE lọc hàng trước, HAVING lọc nhóm sau; đổi tập giá tính mean và nhóm còn lại | Trọng tâm | 008,024,049 | NB ô 52–55; GK câu 24 |
| K38 | Đếm thiếu mọi nhóm bằng COUNT(*)−COUNT(gia); WHERE IS NULL làm mất nhóm thiếu 0 | Trọng tâm | 028 | NB ô 56–57; BG §3 bài tập 3 |
| K39 | Ít nhất N hàng/giá biết/giá đạt ngưỡng là ba yêu cầu; đổi WHERE phải rà SELECT/COUNT/HAVING | Trọng tâm | 008,039 | NB ô 49–55; GK câu 24 |
| K40 | year(date): review theo năm rồi nhóm; HAVING đếm trong phạm vi năm, không lẫn mọi năm | Trọng tâm | 019,034,056 | LAB bước 7,10 |
| K41 | SQL trên Parquet chọn cột/tổng hợp tại file; công cụ theo nguồn, bộ nhớ và thao tác, không luôn nhanh hơn | Trọng tâm | 052 | NB ô 61–65 |
| K42 | LEFT JOIN/ON tạo các cặp khóa; khóa phải lặp có thể tăng hàng trái | Trọng tâm | 015,035 | NB ô 58–60; GK câu 15 |
| K43 | WHERE cột phải loại hàng đệm NULL; ON giới hạn đối ứng mà vẫn giữ trái | Trọng tâm | 025,030 | BG §3 JOIN; GK câu 15 |
| K44 | Thêm OR phải IS NULL không luôn chữa được yêu cầu giữ mọi trái; khác đưa điều kiện vào ON | Trọng tâm | 030 | Suy luận JOIN/WHERE từ BG §3; biến thể đề GK |
| K45 | COUNT(*) sau LEFT JOIN khác số đối ứng; đếm khóa phải không NULL khác đếm cột thông tin có thể thiếu | Trọng tâm | 045,059 | NB ô 49–50,58–60; LAB bước 9 |
| K46 | Khóa id/listing_id cùng kiểu và ý nghĩa; không khẳng định khác kiểu luôn lỗi hoặc luôn đổi đúng | Trọng tâm | 060,MR12 | LAB W2, bước 9, tự làm 2 |
| K47 | Tỷ lệ review theo loại khác tỷ lệ listing; review không tự bằng booking | Trọng tâm | 055 | LAB bước 9, ô 29–31 |
| K48 | Tương quan tuyến tính yếu từ hệ số cho sẵn không chứng minh nhân quả hoặc không có mọi dạng quan hệ | Trọng tâm | 055 | LAB bước 6, ô 23–24; tự làm 1 |
| K49 | Đối chiếu cùng snapshot, lọc, đơn vị, thiếu và nhóm khóa thiếu; giống kết quả chưa chắc đúng yêu cầu | Trọng tâm | 049,060 | NB ô 51,63,66; LAB bước 7,10 |
| K50 | Kiểm độ khớp qua khóa thật và metadata, không chỉ số hàng/NaN hay assert đơn lẻ | Trọng tâm | 059,060 | LAB bước 3–6,9; NB kiểm chứng AI |
| K51 | chunksize trả trình đọc từng khối; không giữ toàn bảng nếu không gom lại | Tự học/đọc thêm | MR01 | NB ô 72–73 |
| K52 | Cộng dồn sum/count rồi chia; không mean các mean khối; lọc đúng tập từng khối | Tự học/đọc thêm | MR02,MR04,MR10 | NB ô 72–73 |
| K53 | Benchmark cùng bảng/cột/schema, đọc tương đương; file, DataFrame RAM, thời gian là ba phép đo; cache/môi trường | Tự học/đọc thêm | MR03,MR08 | NB ô 70–71; LAB bước 1–2 |
| K54 | EXPLAIN trả kế hoạch, không phải kết quả hay phép đo tốc độ truy vấn | Tự học/đọc thêm | MR05 | NB ô 74–75 |
| K55 | Nhận diện Projections trong PARQUET_SCAN: những cột cần đọc, không học thuộc toàn plan | Tự học/đọc thêm | MR09 | NB ô 74–75 |
| K56 | API key từ biến môi trường/Colab Secrets, không ghi khóa thật vào notebook hoặc prompt | Tự học/đọc thêm | MR06,MR11 | NB ô 76 |
| K57 | 429 và giới hạn truy cập: làm theo hướng dẫn dịch vụ, không có thời gian nghỉ chuẩn cho mọi API | Tự học/đọc thêm | MR07,MR11 | NB ô 76 |
| K58 | Top-k review đúng năm: ORDER BY/LIMIT và đồng hạng; thống nhất mã với bảng tên | Tự học/đọc thêm | MR12 | LAB tự làm 2, ô 34 |

## Đợt 1

### Câu trọng tâm

#### B6-001

File ma.csv có một hàng mỗi listing, id là mã ba ký tự:
```csv
id,gia
001,10
010,20
101,30
003,40
```
```python
d = pd.read_csv('ma.csv')
print(d['id'].astype(str).tolist())
```
Dòng cuối cho gì?

A. `['001','010','101','003']`

B. `['1','10','101','3']`

C. `[1,10,101,3]`

D. ValueError vì mã có số 0 đầu.

#### B6-002

Một bảng đã được xử lý đúng cần lưu để nhiều lần sau chỉ đọc vài cột. Nhận định nào giải thích đúng vai trò Parquet?

A. Parquet lưu bảng dạng nhị phân cùng thông tin kiểu và tổ chức theo cột; bộ đọc có thể bỏ cột không dùng.

B. Parquet chỉ là CSV đổi phần mở rộng, nên không có thông tin kiểu.

C. Parquet tự sửa giá tiền dạng chuỗi thành số và mọi mã đã mất 0 đầu.

D. Parquet luôn nhỏ hơn và đọc nhanh hơn CSV đúng bằng tỷ lệ số cột bỏ đi.

#### B6-003

Theo bảng mô tả của dịch vụ trong đề: daily chọn đại lượng ngày, forecast_days chọn số ngày, timezone chọn múi giờ. Một yêu cầu được gửi bằng:
```python
p = {'daily':'temperature_2m_max', 'forecast_days':3, 'timezone':'America/Santiago'}
r = requests.get(endpoint, params=p, timeout=20)
```
Nhận định nào đúng để đối chiếu yêu cầu thực tế? Không cần gọi API.

A. params chỉ là ghi chú cục bộ, không được gửi tới dịch vụ.

B. r.json() luôn trả nguyên p nên không cần xem URL.

C. Requests ghép params vào URL; xem r.url và đối chiếu bảng tham số, không chỉ xem mã HTTP.

D. Chỉ cần status_code=200 là đã chứng minh mọi tham số, khoảng ngày và đơn vị đúng mục tiêu.

#### B6-004

Mỗi hàng d là một listing; id chuỗi, gia float USD/đêm, np.nan là chưa có giá:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'gia':[80.,100.,np.nan,0.]})
```
```sql
SELECT id, gia FROM d
WHERE gia >= 80
ORDER BY gia DESC
```
Các id theo thứ tự kết quả là gì?

A. `['P','Q']`

B. `['Q','P']`

C. `['Q','P','R']`

D. `['Q']`

#### B6-005

Mỗi hàng d là một listing:
```python
d = pd.DataFrame({'id':['P','Q','R','S']})
r = duckdb.sql('SELECT COUNT(*) AS n FROM d').df()
print(type(r).__name__, len(r), r.loc[0,'n'])
```
Nhận định nào đúng?

A. In DataFrame,4,1; mỗi listing vẫn một hàng.

B. In list,1,4 vì SQL chỉ trả danh sách.

C. In DataFrame,1,4; DuckDB truy vấn biến d, bảng trả về có một hàng tổng hợp.

D. Báo lỗi vì d chưa được đưa lên một máy chủ cơ sở dữ liệu.

#### B6-006

File khu.csv có một hàng mỗi listing, các mã khu đều hợp lệ:
```csv
id,khu
001,NA
002,N/A
003,TB
004,null
```
```python
d = pd.read_csv('khu.csv', dtype={'id':'str','khu':'str'})
```
Có bao nhiêu ô khu thiếu và mã id đầu có còn là 001 không?

A. 0 ô thiếu; id đầu là 001.

B. 3 ô thiếu; id đầu thành số 1.

C. 3 ô thiếu; id đầu vẫn là chuỗi 001.

D. 1 ô thiếu; chỉ null mới được nhận diện.

#### B6-007

Cho sẵn r là phản hồi HTTP 400, nội dung JSON hợp lệ `{"error":true,"reason":"tham số không hợp lệ"}`. Không có lỗi mạng:
```python
x = r.json()
print(type(x).__name__)
r.raise_for_status()
print('xong')
```
Điều gì xảy ra?

A. r.json gây HTTPError ngay nên không in dict.

B. In dict và xong vì JSON hợp lệ chứng minh thành công.

C. Dừng với Timeout vì mọi mã 400 là hết thời gian chờ.

D. In dict rồi raise_for_status gây HTTPError; không in xong.

#### B6-008

Mỗi hàng d là một listing, gia float USD/đêm; np.nan vào DuckDB thành NULL:
```python
d = pd.DataFrame({'khu':['A','A','A','B','B','C','C'],
                  'gia':[40.,80.,np.nan,60.,100.,np.nan,np.nan]})
```
(a) Viết truy vấn mỗi khu có ít nhất 2 listing giá từ 60 trở lên: khu, số listing đạt ngưỡng n, mean của chúng tb; sắp theo khu.
(b) Đổi yêu cầu: bỏ ngưỡng 60, chỉ giữ khu có ít nhất 2 giá đã biết; n phải là số giá đã biết.
(c) Sửa những chỗ COUNT/WHERE/HAVING nào, cho kết quả hai truy vấn và giải thích mẫu số.

#### B6-009

File gia.csv có một hàng mỗi listing, id là mã ba ký tự; khu NA và dấu - là mã khu hợp lệ. Ở cột gia, ?, - và ô trống đều là chưa biết; giá 0 hợp lệ, USD/đêm:
```csv
id,khu,gia
001,NA,10
002,-,?
003,NA,
004,TB,0
005,TB,30
006,-,-
```
Viết read_csv giữ đúng mã, đọc gia float64 và đúng thiếu. Mean theo các khu NA,TB,- là gì? Vì sao không nên dùng một danh sách na_values chung cho cả bảng?

#### B6-010

File gia.csv có bốn listing; các giá price là chuỗi tiền tệ:
```csv
id,price
001,$12.00
002,$20.00
003,$30.00
004,$40.00
```
```python
d = pd.read_csv('gia.csv')
d.to_parquet('bang.parquet', index=False)
r = pd.read_parquet('bang.parquet')
```
id đầu và price đầu của r là gì? Parquet có sửa hai vấn đề mã/kiểu giá không? Nêu bước cần làm để giữ mã đúng, nhưng không cần viết hàm xử lý chuỗi tiền tệ.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR01

File gia.csv có 7 listing, một dòng tiêu đề; không có dòng trống bị bỏ. Xét:
```python
doc = pd.read_csv('gia.csv', usecols=['gia'], chunksize=3)
```
Nếu duyệt doc lần lượt, số hàng của các khối là gì?

A. 3,3,3 vì khối cuối tự đệm hai hàng.

B. 7 vì usecols chỉ chọn một cột.

C. 3,3,1; doc là trình đọc từng khối, không phải một DataFrame 7 hàng đã nạp xong.

D. 2,3,2 vì dòng tiêu đề được tính vào khối đầu.

#### B6-MR02

Đọc cùng một file theo hai khối. Khối 1 có một giá biết 10 và hai giá thiếu; khối 2 có ba giá biết 30,40,50. Mỗi hàng là một listing, USD/đêm. Mean của toàn bộ giá đã biết là bao nhiêu?

A. 25

B. 130/6

C. 32.5

D. 65

### Độ bao phủ sau đợt 1

Đã dùng 21/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K05, K08, K09, K10, K11, K12, K17, K18, K21, K23, K24, K25, K26, K27, K28, K29, K30, K31, K36, K38, K40, K41, K42, K43, K44, K45, K46, K47, K48, K49, K50, K53, K54, K55, K56, K57, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 2

### Câu trọng tâm

#### B6-011

Hai listing có mã ba ký tự 007 và 070. CSV được đọc mặc định thành các số 7,70. Bảng tra vẫn dùng mã chuỗi '007','070'. Cần làm gì để dùng đúng mã gốc, không giả định độ dài mã cho những file khác?

A. Chỉ astype(str) trên cột đã đọc, vì sẽ lấy lại đúng 007 và 070.

B. Lưu cột số hiện tại thành Parquet rồi đọc lại.

C. Đổi mã ở bảng tra sang số luôn an toàn với mọi mã định danh.

D. Đọc lại CSV gốc và khai báo dtype chuỗi cho cột mã ngay khi đọc.

#### B6-012

Mỗi hàng d là một listing:
```python
d = pd.DataFrame({'id':pd.Series(['001','002','003','004'],dtype='str'),
                  'gia':[10.,np.nan,0.,40.]})
d.to_parquet('d.parquet', index=False)
r = pd.read_parquet('d.parquet', columns=['id','gia'])
```
Nhận định nào đúng khi kiểm đọc lại trong môi trường đề bài?

A. r có shape (4,2), giữ mã 001, giá 0 và một giá thiếu; cần kiểm cả kiểu logic và giá trị.

B. r có shape (3,2) vì ghi Parquet tự bỏ hàng giá thiếu.

C. id đầu tự thành số 1 vì mọi định dạng đều suy luận mã như CSV.

D. Chỉ cần shape bằng nhau là đủ chứng minh mã, kiểu và giá đều đúng.

#### B6-013

Bảng mô tả trong đề: start_date/end_date giới hạn khoảng ngày lịch sử; daily chọn đại lượng. Người phân tích muốn 01–03/02/2025, nhưng r.url ghi:
```text
https://example.test/archive?start_date=2025-01-01&end_date=2025-01-03&daily=temperature_2m_max
```
HTTP 200; phản hồi daily có ba ngày tháng 1. Kết luận nào đúng?

A. Đúng yêu cầu vì HTTP 200 và đủ ba hàng.

B. Chỉ cần đổi nhãn ba ngày thành tháng 2, giữ các nhiệt độ.

C. Tăng timeout sẽ tự đổi start_date và end_date sang tháng 2.

D. Yêu cầu gửi đi dùng sai tháng; phải sửa params và kiểm ngày phản hồi, không lấy ba hàng làm bằng chứng đúng khoảng.

#### B6-014

Mỗi hàng d là một listing; gia float USD/đêm:
```python
d = pd.DataFrame({'id':['A','B','C','D'], 'gia':[0.,np.nan,20.,np.nan]})
```
```sql
SELECT id FROM d WHERE gia IS NOT NULL ORDER BY id;
```
Kết quả chứa id nào?

A. `['A','C']`

B. `['C']`

C. `['B','D']`

D. `['A','B','C','D']`

#### B6-015

Bảng l mỗi hàng là một listing; bảng t mỗi hàng là một mức phí theo mã khu (mã khu có thể lặp). Các khóa đều chuỗi, không thiếu:
```python
l = pd.DataFrame({'id':['P','Q','R','S'], 'khu':['A','A','B','C']})
t = pd.DataFrame({'khu':['A','A','B'], 'phi':[5.,8.,3.]})
```
```sql
SELECT l.id,t.phi FROM l LEFT JOIN t ON l.khu=t.khu;
```
Kết quả có bao nhiêu hàng?

A. 4

B. 5

C. 6

D. 3

#### B6-016

File có một hàng mỗi listing:
```csv
id,gia
001,10
002,?
003,0
004,20
```
```python
d = pd.read_csv('gia.csv', dtype={'id':'str','gia':'float64'})
```
Vì ? không thuộc tập dấu hiệu thiếu mặc định đang dùng, điều gì xảy ra?

A. Đọc xong và tự thay ? bằng 0.

B. Đọc có thể dừng với ValueError khi ép ? sang float64; cần khai báo na_values cho gia.

C. Đọc xong với gia là float64, ? tự thành NaN chỉ vì đã chỉ định float64.

D. id được giữ chuỗi nên tự tắt toàn bộ nhận diện NA ở mọi cột.

#### B6-017

Mỗi hàng d là một listing, gia float USD/đêm:
```python
d = pd.DataFrame({'gia':[0.,10.,np.nan,20.]})
```
```sql
SELECT COUNT(*) AS n, COUNT(gia) AS k, AVG(gia) AS tb FROM d;
```
Một hàng kết quả có (n,k,tb) nào?

A. (4,4,7.5)

B. (4,2,15)

C. (3,3,10)

D. (4,3,10)

#### B6-018

Mỗi hàng mong muốn là một ngày. Phản hồi giả lập có HTTP 503 và JSON:
```json
{"error": true, "reason": "dịch vụ tạm lỗi"}
```
Code hiện tại là x=r.json(); d=pd.DataFrame(x['daily']).
(a) Vì sao JSON đọc được vẫn không tạo được bảng ngày đúng?
(b) Viết thứ tự kiểm HTTP, lấy daily và tạo bảng.
(c) Với một phản hồi HTTP 200 khác, đã tạo được ba hàng, hai kiểm tra ý nghĩa nào còn cần làm trước khi lọc ngày nóng?

#### B6-019

Mỗi hàng rv là một review; listing_id chuỗi, date datetime, diem float có thể thiếu:
```python
rv = pd.DataFrame({'listing_id':['A','A','A','B','B','C'],
 'date':pd.to_datetime(['2024-12-30','2025-01-01','2025-02-01',
                        '2025-01-02','2025-02-02','2025-03-01']),
 'diem':[5.,4.,np.nan,3.,5.,np.nan]})
```
(a) Lấy listing có ít nhất hai review trong năm 2025, trả listing_id,n; sắp theo mã.
(b) Đổi thành ít nhất hai review năm 2025 có diem đã biết; n phải đếm đúng chúng.
(c) Sửa COUNT/WHERE/HAVING nào? Cho kết quả và giải thích vì sao không dùng số review mọi năm.

#### B6-020

CSV có bốn listing. Dấu ? ở khu là mã khu hợp lệ; dấu ? ở gia là chưa biết. NA cũng là mã khu hợp lệ.
```csv
id,khu,gia
101,?,10
102,NA,?
103,TB,20
104,?,0
```
Người học dùng keep_default_na=False, na_values=['?'] và dtype id/khu chuỗi, gia float64. Những ô ngoài gia bị mất thông tin nào? Viết cách đọc sửa và nêu hai kiểm tra nội dung sau đọc.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR03

Hai bản CSV và Parquet biểu diễn cùng bảng đúng schema. Để so thời gian đọc hai cột id,gia, thiết kế nào hợp lý nhất?

A. CSV đọc toàn bộ 90 cột, Parquet đọc hai cột rồi kết luận riêng định dạng quyết định mọi chênh lệch.

B. Chỉ so số MB trên đĩa, bản nhỏ hơn chắc chắn đọc nhanh hơn đúng cùng tỷ lệ.

C. Đo đúng một lần và bỏ qua cache vì cache không tác động đọc file.

D. Đọc cùng hai cột, kiểm kết quả tương đương, đo lặp và nêu môi trường/cache; đo riêng file trên đĩa và RAM của bảng.

#### B6-MR04

File gồm bảy listing, cột gia đã là số hoặc ô trống được đọc thành thiếu: [10,NaN,NaN,20,40,60,NaN]. Viết cách đọc từng khối 3 hàng để tính mean của mọi giá biết, không gom toàn bảng. Cho kết quả; nếu cả file không có giá biết thì không chia cho 0.

### Độ bao phủ sau đợt 2

Đã dùng 28/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K08, K09, K10, K11, K12, K18, K21, K24, K26, K27, K28, K29, K30, K31, K36, K38, K41, K43, K44, K45, K46, K47, K48, K49, K50, K54, K55, K56, K57, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 3

### Câu trọng tâm

#### B6-021

File CSV có 6 listing và 5 cột id,khu,gia,host_id,loai. Lệnh:
```python
d = pd.read_csv('l.csv', usecols=['id','gia'], dtype={'id':'str'})
```
Nhận định nào đúng?

A. d có 2 hàng và 5 cột vì usecols chọn hai quan sát.

B. d có 6 hàng và 2 cột, chắc chắn chỉ đọc vật lý đúng 2/5 byte file CSV.

C. d có 6 hàng và 2 cột; CSV vẫn cần quét/phân tích văn bản, không bảo đảm thời gian còn đúng 2/5.

D. d có 6 hàng và 5 cột, ba cột không chọn được thay bằng NaN.

#### B6-022

Một CSV có id 001 và 01 là hai mã khác nhau. Đọc mặc định làm cả hai thành số 1; sau đó ghi Parquet. Kiểm tra r['id'].dtype là kiểu số và len(r)==2 đều đạt khi đọc lại. Kết luận nào đúng?

A. Parquet sẽ tách lại 1 thành 001 và 01 theo vị trí hai hàng.

B. Hai kiểm tra chưa phát hiện hai mã đã bị nhập nhằng; phải đối chiếu mã raw và đọc lại đúng schema.

C. Có hai hàng nên chắc chắn vẫn có hai mã phân biệt.

D. Kiểu số chứng minh id đã được làm sạch đúng để ghép theo mã gốc.

#### B6-023

Cho phản hồi JSON dưới đây; HTTP 200:
```json
{"timezone":"America/Santiago", "daily_units":{"temperature_2m_max":"°C"},
 "daily":{"time":["2025-01-01","2025-01-02","2025-01-03"],
          "temperature_2m_max":[30,32,35]}}
```
Sau x=r.json(), cách hiểu nào đúng để mỗi hàng bảng là một ngày?

A. x là list ba ngày nên pd.DataFrame(x) mặc định luôn đúng bảng ngày.

B. x["daily"] là chuỗi JSON, phải tách từng ký tự thành hàng.

C. x là dict; x["daily"]["time"] là list; pd.DataFrame(x["daily"]) tạo bảng 3 hàng,2 cột.

D. pd.DataFrame(x["daily_units"]) là bảng nhiệt độ ba ngày.

#### B6-024

Mỗi hàng d là một listing; gia float USD/đêm:
```python
d = pd.DataFrame({'khu':['A','A','B','B'], 'gia':[20.,100.,70.,90.]})
```
```sql
-- Q1
SELECT khu,AVG(gia) AS tb FROM d WHERE gia>=60 GROUP BY khu ORDER BY khu;
-- Q2
SELECT khu,AVG(gia) AS tb FROM d GROUP BY khu HAVING AVG(gia)>=60 ORDER BY khu;
```
Hai bảng kết quả là gì?

A. Cả hai A:100,B:80.

B. Cả hai A:60,B:80.

C. Q1 A:100,B:80; Q2 chỉ B:80.

D. Q1 A:100,B:80; Q2 A:60,B:80.

#### B6-025

l có một hàng mỗi listing, t có tối đa một hàng mỗi id; khóa chuỗi, không thiếu:
```python
l = pd.DataFrame({'id':['A','B','C','D']})
t = pd.DataFrame({'id':['A','B','D'], 'phi':[5.,20.,np.nan]})
```
```sql
SELECT l.id FROM l LEFT JOIN t ON l.id=t.id
WHERE t.phi<=10 ORDER BY l.id;
```
Những listing nào còn lại?

A. Chỉ A.

B. A và C.

C. A,C,D.

D. A và D.

#### B6-026

Một CSV gồm bốn listing có gia lần lượt là văn bản 0,?,20,40. Quy tắc đọc đã đúng: ? thành NaN, còn 0 là số 0. Mean của các giá đã biết và số giá đã biết lần lượt là gì?

A. 15 và 4

B. 20 và 3

C. 30 và 2

D. NaN và 0

#### B6-027

HTTP 200, nhánh daily có bốn ngày; daily_units ghi temperature_2m_max là °F:
```text
ngày:   01/01,02/01,03/01,04/01 năm 2025
giá trị: 95,   86,  104,   68
```
Đề cho °C=(°F-32)*5/9. Muốn lấy ngày nhiệt độ từ 35°C trở lên, chọn ngày nào?

A. Cả bốn ngày.

B. 01/01 và 03/01.

C. Chỉ 03/01.

D. 02/01 và 04/01.

#### B6-028

Mỗi hàng d là một listing, gia float USD/đêm:
```python
d = pd.DataFrame({'khu':['A','A','B','B','C','C'],
                  'gia':[10.,20.,np.nan,30.,np.nan,np.nan]})
```
(a) Viết SQL báo cáo mọi khu: n_hang,n_biet,n_thieu,tb. Khu không thiếu cũng phải có mặt.
(b) Chỉ giữ khu có ít nhất một giá thiếu: thêm điều kiện ở đâu?
(c) Vì sao WHERE gia IS NULL trước GROUP BY không dùng được cho báo cáo (a)? Cho kết quả (a), kể cả nhóm toàn thiếu.

#### B6-029

Một file raw/gia.csv chứa bốn listing với mã 001,002,003,004 và gia 10,20,0,ô trống. Mã phải giữ ba ký tự; ô trống là thiếu số, giá 0 hợp lệ. Viết cách đọc đúng rồi lưu processed/gia.parquet, đọc lại và kiểm kết quả. Tại sao giữ file raw? Có thể từ kiểm thử này kết luận mọi backend luôn có biểu diễn dtype chuỗi y hệt không?

#### B6-030

l mỗi hàng một listing; t mỗi hàng là một phí theo listing; các id đều chuỗi, không thiếu:
```python
l = pd.DataFrame({'id':['A','B','C','D']})
t = pd.DataFrame({'id':['A','C','D'], 'phi':[20.,5.,8.]})
```
Yêu cầu giữ mọi listing; chỉ bổ sung các đối ứng có phi<10.
```sql
SELECT l.id,t.phi FROM l LEFT JOIN t ON l.id=t.id
WHERE t.phi<10 OR t.phi IS NULL ORDER BY l.id;
```
(a) Listing nào bị mất và vì sao OR IS NULL chưa sửa được?
(b) Sửa truy vấn.
(c) Cho kết quả và giải thích hàng A khác hàng C ra sao.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR05

Mỗi hàng d là một listing có gia số. Người học chạy:
```python
p = duckdb.sql('EXPLAIN SELECT AVG(gia) AS tb FROM d').df()
```
Nhận định nào đúng? Không cần nhớ toàn bộ định dạng bảng p.

A. p chắc chắn chứa đúng một ô số mean, giống hệt bỏ EXPLAIN.

B. p là số giây chạy chính xác của SELECT trong mọi lần sau.

C. p là toàn bộ bảng nguồn được sắp theo gia.

D. p biểu diễn kế hoạch truy vấn; muốn lấy mean phải chạy truy vấn SELECT không có EXPLAIN.

#### B6-MR06

Một dịch vụ trong bài tự học yêu cầu API key. Notebook sẽ được chia sẻ. Cách quản lý nào phù hợp hướng dẫn?

A. Ghi key thật vào ô Markdown để người đọc tái lập dễ hơn.

B. Lấy key từ biến môi trường hoặc Colab Secrets; không chèn key thật vào notebook, prompt hay nội dung chia sẻ.

C. Đặt tên biến API_KEY rồi ghi trực tiếp giá trị thật vào mã là đã giữ bí mật.

D. Dán key vào prompt nhờ công cụ kiểm, rồi xóa tên biến trong notebook.

### Độ bao phủ sau đợt 3

Đã dùng 38/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K09, K10, K11, K12, K21, K24, K27, K28, K29, K30, K31, K41, K45, K46, K47, K48, K49, K55, K57, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 4

### Câu trọng tâm

#### B6-031

CSV có một hàng mỗi listing:
```csv
id,khu,gia
001,NA,10
002,TB,
003,NA,0
004,TB,20
```
```python
d = pd.read_csv('d.csv', keep_default_na=False,
                dtype={'id':'str','khu':'str','gia':'str'})
print(d.loc[1,'gia'] == '', d['gia'].isna().sum())
```
Hai giá trị in ra là gì?

A. False và 1

B. True và 1

C. False và 0

D. True và 0

#### B6-032

File p.parquet lưu đúng bảng bốn listing, các cột id (chuỗi '001'..'004'), gia (float64), khu (chuỗi), host_id (chuỗi). Xét:
```python
d = pd.read_parquet('p.parquet', columns=['id','gia'])
```
Nhận định nào đúng?

A. d có shape (2,4), vì columns chọn hai hàng.

B. d có shape (4,2), giữ id đầu 001; tổ chức theo cột cho phép bộ đọc bỏ khu và host_id.

C. d có shape (4,4); hai cột bị bỏ được điền NULL.

D. d có shape (4,2) nhưng id đầu bắt buộc thành số 1 như đọc CSV mặc định.

#### B6-033

Đề cung cấp bảng mô tả dịch vụ: /forecast trả dự báo tính từ thời điểm gọi; /archive nhận start_date,end_date để lấy dữ liệu lịch sử. Hai endpoint nhận latitude,longitude,daily,timezone. Cần nhiệt độ cực đại ngày tại vị trí (vĩ độ -33.45,kinh độ -70.67), 01–03/01/2025, theo ngày địa phương America/Santiago. Lựa chọn nào đúng mục tiêu?

A. Dùng /archive, đúng hai tọa độ, start_date=2025-01-01,end_date=2025-01-03,daily=temperature_2m_max,timezone=America/Santiago.

B. Dùng /forecast với forecast_days=3; ba ngày luôn tương đương ba ngày quá khứ đã yêu cầu.

C. Dùng /archive đúng ngày nhưng đổi daily thành precipitation_sum mà vẫn gọi kết quả là nhiệt độ.

D. Dùng /archive đúng ngày và đại lượng nhưng bỏ timezone, vì ngày theo mọi múi giờ luôn giống nhau.

#### B6-034

Mỗi hàng rv là một review, date datetime:
```python
rv = pd.DataFrame({'listing_id':['P','P','P','Q','Q','R'],
 'date':pd.to_datetime(['2024-12-31','2025-01-01','2025-01-02',
                        '2024-01-01','2025-02-01','2025-03-01'])})
```
```sql
SELECT listing_id,COUNT(*) AS n FROM rv WHERE year(date)=2025
GROUP BY listing_id HAVING COUNT(*)>=2 ORDER BY listing_id;
```
Kết quả nào đúng?

A. P:3,Q:2

B. P:2,Q:1,R:1

C. P:2

D. P:3

#### B6-035

Mỗi hàng l là một listing. Bảng h có một hàng mỗi bản ghi host nhưng host_id H1 bị lặp; các khóa chuỗi không thiếu:
```python
l = pd.DataFrame({'id':['A','B','C','D'], 'host_id':['H1','H1','H2','H3']})
h = pd.DataFrame({'host_id':['H1','H1','H2'], 'nhom':['nho','lon','nho']})
```
Sau LEFT JOIN theo host_id, người học đếm COUNT(*)=6 rồi báo “có 6 listing”. Nhận định nào đúng?

A. Có 6 listing khác nhau vì COUNT(*) luôn đếm đối tượng gốc không trùng.

B. Có 6 hàng ghép nhưng chỉ 4 listing nguồn; H1 tạo hai đối ứng cho mỗi A,B nên phép đếm bị nhân.

C. Có 5 listing vì phải bỏ hàng D không khớp trước mọi báo cáo.

D. DuckDB phải báo lỗi khóa phải lặp nên không thể có kết quả 6 hàng.

#### B6-036

Phản hồi HTTP 200 đã giải mã thành x:
```python
x = {'daily_units':{'temperature_2m_max':'°C'},
     'daily':{'time':['2025-01-01','2025-01-02','2025-01-03'],
              'temperature_2m_max':[30,32]}}
d = pd.DataFrame(x['daily'])
```
Điều gì xảy ra?

A. Tạo ba hàng, nhiệt độ ngày 03 tự là NaN.

B. Tạo hai hàng và tự bỏ ngày cuối.

C. ValueError vì hai danh sách trong daily khác độ dài; 200 không bảo đảm nhánh dữ liệu tạo bảng được.

D. HTTPError dù mã 200, vì Requests tự kiểm mọi danh sách trong JSON.

#### B6-037

Mỗi hàng d là một listing, gia float:
```python
d = pd.DataFrame({'khu':['A','A','B','B'], 'gia':[np.nan,np.nan,0.,20.]})
```
```sql
SELECT khu,COUNT(*) AS n,COUNT(gia) AS k,AVG(gia) AS tb
FROM d GROUP BY khu ORDER BY khu;
```
Hàng của khu A là gì?

A. A,2,2,0

B. A,0,0,NULL

C. A,2,0,NULL

D. Không có hàng khu A.

#### B6-038

Cùng bốn listing, hai phiên bản nguồn:
```csv
# ban_rut_gon.csv
id,price
001,12
002,20
003,0
004,30
```
```csv
# ban_day_du.csv.gz (nội dung sau giải nén, ngoài ra còn nhiều cột khác)
id,price
001,$12.00
002,$20.00
003,$0.00
004,$30.00
```
Các dòng chú thích # chỉ để mô tả, không nằm trong file. Người học đọc bản đầy đủ với usecols=['id','price'] rồi cho rằng price chắc chắn là số như bản rút gọn.
(a) Sai ở giả định nào? usecols có sửa được không?
(b) Viết đọc bản đầy đủ giữ mã, không ép price sai thành float; kiểm shape, mã và price đầu.
(c) Trước khi so mean hai bản còn phải thống nhất gì? Không yêu cầu viết hàm làm sạch tiền tệ.

#### B6-039

File l.parquet lưu sáu listing, mỗi id duy nhất; cột loai chuỗi, first_review datetime (NaT là chưa có ngày review):
```python
l = pd.DataFrame({'id':['A','B','C','D','E','F'],
 'loai':['nguyen_can','nguyen_can','nguyen_can','phong','phong','phong'],
 'first_review':pd.to_datetime(['2025-01-01',None,None,'2024-01-01','2025-02-01',None])})
```
(a) SQL đọc trực tiếp file, lấy loại có ít nhất 2 listing có first_review đã biết, xuất loai,n, sắp loai.
(b) Đổi yêu cầu: ít nhất 2 listing bất kể có review chưa, n phải đếm mọi listing.
(c) Sửa COUNT/HAVING hay WHERE nào? Cho hai kết quả; giải thích vì sao “có first_review” không là tổng số review.

#### B6-040

Một yêu cầu Requests dùng timeout=20. Máy đã nhận phản hồi HTTP 400 với JSON {"reason":"tham số ngày không hợp lệ"}. Người học nói: “400 chứng minh quá 20 giây; tăng timeout sẽ sửa ngày. Với timeout=20 mọi yêu cầu chắc chắn kết thúc trong tổng cộng 20 giây”. Hãy sửa hai kết luận, rồi viết hai dòng kiểm HTTP và giải mã JSON theo thứ tự đúng. Không cần gọi mạng.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR07

Một API trả HTTP 429 kèm hướng dẫn giới hạn truy cập trong phản hồi và tài liệu. Lựa chọn nào phù hợp?

A. Kiểm hạn mức/hướng dẫn dịch vụ, dừng gửi dồn và chờ/thử lại theo hướng dẫn; không có thời gian nghỉ chung cho mọi API.

B. Mọi API đều chỉ cần nghỉ đúng 1 giây rồi gọi vô hạn.

C. Bỏ raise_for_status và coi JSON 429 là dữ liệu quan sát bình thường.

D. Tăng timeout sẽ nâng hạn mức tài khoản.

#### B6-MR08

Một báo cáo cho: CSV 12 MB trên đĩa, đọc đủ 20 cột mất 0.8 s, DataFrame chiếm 40 MB; Parquet 5 MB, đọc 2 cột mất 0.2 s, DataFrame chiếm 6 MB. Hai bảng gốc có cùng dữ liệu, số đo là dữ kiện cho sẵn. Có được kết luận “chỉ đổi định dạng khiến mọi lần đọc nhanh gấp 4 và RAM bằng kích thước file” không? Sửa thiết kế so sánh trong tối đa bốn ý.

### Độ bao phủ sau đợt 4

Đã dùng 44/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K09, K10, K12, K27, K28, K29, K30, K31, K46, K47, K48, K49, K55, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 5

### Câu trọng tâm

#### B6-041

File listings.csv.gz có 8 listing, 20 cột. Chỉ cần id,khu,price. Nhận định nào đúng về đọc với usecols=['id','khu','price']?

A. Bảng nhận có 8 hàng,3 cột; pandas có thể nhận nén từ đuôi .gz, vẫn có chi phí giải nén và phân tích CSV.

B. Đọc chỉ 3/20 số listing vì usecols làm giảm số hàng.

C. File gốc tự thu nhỏ còn 3/20 sau read_csv.

D. Không còn chi phí giải nén vì usecols khiến CSV nén thành định dạng cột.

#### B6-042

Một nhóm cần dùng lại đúng bảng nguồn đã tải hôm nay, có thể sửa quy tắc xử lý sau này và thường chỉ đọc vài cột đã làm sạch. Thiết kế nào phù hợp nhất?

A. Ghi đè raw bằng bảng đã xử lý, vì Parquet luôn khôi phục được mọi giá trị gốc.

B. Mỗi lần phân tích tải lại cùng URL, bỏ snapshot, vì URL giống nhau chứng minh nội dung giống nhau.

C. Giữ snapshot raw gốc, ghi bảng đúng schema vào processed Parquet và kiểm đọc lại; chọn cột khi đọc theo nhu cầu.

D. Chỉ đổi phần mở rộng raw từ .csv sang .parquet là có schema và chọn cột nhị phân.

#### B6-043

daily trong phản hồi HTTP 200 có cùng thứ tự theo vị trí:
```python
daily = {'time':['2025-01-03','2025-01-01','2025-01-02'],
         'temperature_2m_max':[40,20,30]}
```
Người học chỉ sắp riêng danh sách time thành tăng dần rồi mới pd.DataFrame(daily), không đổi danh sách nhiệt độ. Nhận định nào đúng?

A. Bảng vẫn có 3 hàng nhưng gán sai ngày: 01/01 nhận 40 thay vì 20; phải tạo bảng trước rồi sắp cả hàng.

B. Không sai vì pandas tự biết 40 thuộc ngày 03/01 và căn lại.

C. Sẽ ValueError vì danh sách ngày đã sắp còn nhiệt độ chưa sắp.

D. Chỉ cần sắp riêng nhiệt độ tăng dần luôn đúng với mọi dữ liệu ngày.

#### B6-044

Mỗi hàng d là một listing, gia float USD/đêm:
```python
d = pd.DataFrame({'gia':[0.,10.,np.nan,100.]})
```
```sql
SELECT MEDIAN(gia) AS trung_vi,AVG(gia) AS tb,COUNT(gia) AS n FROM d;
```
Một hàng kết quả có các giá trị nào?

A. (10,110/3,3)

B. (5,27.5,4)

C. (55,55,2)

D. (10,27.5,3)

#### B6-045

l mỗi hàng một listing. t mỗi hàng một ghi nhận phí; rid là khóa chuỗi không NULL của ghi nhận, phi có thể thiếu. Các id ghép là chuỗi:
```python
l = pd.DataFrame({'id':['A','B','C','D']})
t = pd.DataFrame({'id':['A','A','B'], 'rid':['r1','r2','r3'], 'phi':[5.,np.nan,7.]})
```
```sql
SELECT COUNT(*) AS a,COUNT(t.rid) AS b,COUNT(t.phi) AS c
FROM l LEFT JOIN t ON l.id=t.id;
```
(a,b,c) là gì?

A. (5,3,2)

B. (4,3,2)

C. (5,5,2)

D. (5,2,2)

#### B6-046

Mỗi hàng d là một listing. Dữ liệu khu A có gia [20,100,NaN]; khu B có [70,90]; gia float USD/đêm. Cần “khu có ít nhất hai listing với giá từ 60, cùng mean của chính các giá đạt ngưỡng”. Cách nào đúng?

A. Không WHERE; HAVING AVG(gia)>=60 AND COUNT(*)>=2.

B. Không WHERE; HAVING COUNT(gia)>=2, vì mọi giá biết đều đạt 60.

C. WHERE gia>=60 rồi GROUP BY khu, không HAVING.

D. WHERE gia>=60 rồi GROUP BY khu, HAVING COUNT(*)>=2 và AVG(gia).

#### B6-047

File reviews.csv.gz có bốn review, listing_id là mã ba ký tự; date là ngày review:
```csv
listing_id,date,diem
001,2025-01-01,4
001,2025-01-02,?
002,2025-01-03,5
003,2025-01-04,3
```
Viết read_csv chọn ba cột, giữ mã, đọc date thành datetime và diem float64 với ? là thiếu. Nêu kiểm dtype ngày, ngày đầu, số hàng, mã và số điểm thiếu. Đọc được có tự chứng minh mọi yêu cầu ấy đúng không?

#### B6-048

HTTP 200; x=r.json() là:
```python
{'daily_units':{'temperature_2m_max':'°F'},
 'daily':{'time':['2025-02-01','2025-02-02','2025-02-03'],
          'temperature_2m_max':[95,86,104]}}
```
```python
r.raise_for_status()
d = pd.DataFrame(x['daily'])
hot = d[d['temperature_2m_max'] >= 35]
assert len(d)==3
```
(a) Vì sao assert qua và HTTP đúng vẫn lọc sai “từ 35°C trở lên”?
(b) Sửa cách tạo cột °C rồi lọc; đề cho °C=(°F-32)*5/9.
(c) Nêu kết quả và một kiểm chứng có thể phát hiện lỗi đơn vị.

#### B6-049

Cùng snapshot gồm bốn listing, khu có thể thiếu và gia float USD/đêm:
```python
d = pd.DataFrame({'khu':['A',None,'A','B'], 'gia':[10.,20.,np.nan,30.]})
```
SQL không lọc hàng: SELECT khu,COUNT(*) n,AVG(gia) tb FROM d GROUP BY khu.
Pandas: d.groupby('khu').agg(n=('gia','size'),tb=('gia','mean')).
Không yêu cầu thứ tự nhóm. Hai bảng có số nhóm nào, lệch do đâu? Sửa pandas để đối chiếu cùng phạm vi và cho n,tb của mỗi nhóm. Nếu hai công cụ cùng trả kết quả, đã đủ chứng minh đúng câu hỏi nghiên cứu chưa?

#### B6-050

Phản hồi r đã kiểm HTTP; x=r.json() chứa daily ba ngày, daily_units và timezone='America/Santiago'. Cần lưu đúng đầu vào để phân tích lại. Hướng dẫn có sẵn Path(...).write_bytes(...) và json.dumps(...).
(a) Nên chỉ lưu bảng daily hay lưu cả r.content? Vì sao cần giữ timezone khi ghép review theo ngày địa phương?
(b) Cho đoạn lưu phản hồi thô và metadata gồm r.url, downloaded_at (chuỗi thời điểm tải đã có).
(c) Hai lần tải trong cùng một giây cùng dùng tên raw/weather_20251018_120000.json: tên có timestamp có đảm bảo không đè và nội dung đúng không? Nêu cách kiểm/khắc phục ngắn.

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR09

File l.parquet có id,khu,gia,host_id. Với SELECT AVG(gia) FROM 'l.parquet', đoạn EXPLAIN được cung cấp cho thấy PARQUET_SCAN và Projections: gia. Điều đó cho biết gì ở mức đang học?

A. Phần quét Parquet cần cột gia cho phép tổng hợp; không cần đọc các cột id,khu,host_id để tính biểu thức này.

B. Kết quả mean chính là chuỗi gia.

C. Chỉ một hàng tên gia được đọc nên mean là giá đầu.

D. Plan chứng minh mọi lần truy vấn nhanh hơn pandas đúng bốn lần.

#### B6-MR10

File có bảy listing với gia [10,NaN,30,50,NaN,70,110], USD/đêm. Cần mean của giá từ 30 trở lên. Viết đọc từng khối 3 hàng, lọc rồi cộng dồn; không gom toàn bảng. Cho kết quả và giải thích vì sao không chia cho bảy hay lấy mean các mean khối.

### Độ bao phủ sau đợt 5

Đã dùng 51/58 mục tiêu trong yêu cầu trả lời. Còn thiếu: K12, K29, K31, K46, K47, K48, K58. Các mục đã được bố trí ở những đợt sau theo danh mục.

## Đợt 6

### Câu trọng tâm

#### B6-051

reviews.csv.gz là CSV nén gzip, có bốn review và listing_id dạng mã 001,001,002,003. Xét:
```python
d = pd.read_csv('reviews.csv.gz', dtype={'listing_id':'str'})
```
Nhận định nào đúng?

A. Phải đổi đuôi thành .parquet thì pandas mới có thể đọc file nén.

B. pandas nhận nén từ tên .gz; cột listing_id giữ 001,001,002,003 và vẫn là mã, không phải số review.

C. Có bốn review nên listing_id tự thành 1,2,3,4.

D. Đuôi .gz tự bảo đảm mọi mã có số 0 đầu kể cả bỏ dtype.

#### B6-052

File l.parquet lưu tám listing với id,khu,gia và nhiều cột khác; gia là số. Cần một bảng nhỏ median gia mỗi khu. Nhận định nào đúng về công cụ và việc đọc?

A. Có thể DuckDB SELECT khu,MEDIAN(gia) FROM file GROUP BY khu rồi .df(); không bắt buộc nạp cả bảng vào pandas trước.

B. Bắt buộc pd.read_parquet đọc mọi cột trước, vì DuckDB không truy vấn file được.

C. SQL luôn nhanh hơn pandas bất kể số hàng hay thao tác.

D. pandas không thể đọc chọn cột, cũng không bao giờ đọc từng khối ở bất kỳ nguồn nào.

#### B6-053

Hôm trước đã lưu raw/w.json bằng r.content, gồm daily, daily_units và timezone. Hôm nay cần chạy lại phân tích với đúng phản hồi ấy; endpoint lịch sử và tham số vẫn như cũ. Cách nào đáp ứng trực tiếp?

A. Gọi lại endpoint với cùng params chắc chắn cho cùng nội dung cũ từng byte.

B. Chỉ dùng tên file có chữ raw, bỏ nội dung đơn vị vì tên đã chứng minh dữ liệu đúng.

C. Lấy dự báo ba ngày hiện tại thay ba ngày lịch sử vì số hàng bằng nhau.

D. Đọc JSON từ raw/w.json và dùng metadata đã lưu để kiểm, không thay đầu vào bằng lần gọi mới.

#### B6-054

Mỗi hàng d là một listing, gia float [10,NaN,0,NaN]. Muốn lấy đúng các listing chưa biết giá, điều kiện SQL nào đúng?

A. WHERE gia = NULL

B. WHERE gia = 0

C. WHERE gia IS NOT NULL

D. WHERE gia IS NULL

#### B6-055

Snapshot l có một hàng mỗi listing: A,B,C là nguyên căn, D là phòng. Trong cùng phạm vi, bảng review có sáu hàng: listing_id A,B,D,D,D,D. Không có mã lạ. Một phân tích khác đã cho hệ số tương quan giữa nhiệt độ ngày và số review/ngày r=0.08. Nhận định nào đúng?

A. Phòng chiếm 4/6 listing vì đã có bốn review của D.

B. Phòng chiếm 4/6 review nhưng 1/4 listing; r=0.08 gợi ý liên hệ tuyến tính yếu trong dữ liệu xét, chưa chứng minh nhân quả.

C. Phòng chiếm 1/4 review vì chỉ có một listing phòng.

D. Phòng chiếm 4/6 review và r=0.08 chứng minh nhiệt độ không thể có bất kỳ quan hệ nào với review hay booking.

#### B6-056

Mỗi hàng rv là một review, date datetime. Các số review đã cho:

| Listing | Năm 2024 | Năm 2025 |
| --- | --- | --- |
| A | 3 | 1 |
| B | 0 | 2 |
| C | 1 | 0 |

Cần listing có ít nhất hai review năm 2025, n là số review chính năm đó. Cách nào đúng?

A. Nhóm mọi năm rồi HAVING COUNT(*)>=2; được A:4,B:2 nên đúng.

B. WHERE year(date)=2025 rồi bỏ HAVING; được A:1,B:2 nên đúng.

C. Giữ A vì tổng năm 2024 đủ ba; hiển thị n=1 của năm 2025.

D. WHERE year(date)=2025 trước GROUP BY listing_id, HAVING COUNT(*)>=2; được B:2.

#### B6-057

Một bảng đúng schema có bốn review:
```python
d = pd.DataFrame({'listing_id':pd.Series(['001','001','002','003'],dtype='str'),
 'khu':pd.Series(['NA','TB','NA','TB'],dtype='str'),
 'date':pd.to_datetime(['2025-01-01','2025-01-02','2025-01-03','2025-01-04']),
 'diem':[4.,np.nan,0.,5.]})
d.to_csv('review.csv', index=False)
```
Đọc lại mặc định có nguy cơ mất gì? Viết cách đọc giữ mã/khu NA hợp lệ, ngày datetime, ô trống diem là thiếu số, và nêu kiểm chứng đọc lại. Các thư viện như quy ước đầu bộ.

#### B6-058

Đề cung cấp mô tả: endpoint archive nhận latitude,longitude,start_date,end_date,daily,timezone; ngày đầu/cuối được lấy. Cần nhiệt độ cực đại ngày cho cùng địa điểm (-33.45,-70.67), 01–03/07/2025, theo ngày America/Santiago để ghép review đã đếm theo chính quy ước ngày ấy.
Viết dict params. Sau HTTP 200, nêu ba kiểm tra phản hồi gồm phạm vi ngày/đại lượng/đơn vị và cách phân tích lại đúng bản đã dùng. Không cần gọi API thật hoặc học thuộc tên tham số ngoài bảng đã cho.

#### B6-059

l có bốn listing A,B,C,D. rv có một hàng mỗi review; rid là mã review không NULL, listing_id chuỗi, date datetime, diem float có thể thiếu:
```python
l = pd.DataFrame({'id':['A','B','C','D']})
rv = pd.DataFrame({'rid':['r1','r2','r3','r4'], 'listing_id':['A','A','B','B'],
 'date':pd.to_datetime(['2024-12-01','2025-01-01','2025-02-01','2025-02-02']),
 'diem':[5.,np.nan,4.,5.]})
```
(a) Viết SQL giữ mọi listing, đếm n_review trong năm 2025 và mean diem biết của các review năm đó; mỗi listing một hàng, sắp id.
(b) Vì sao COUNT(*) hoặc COUNT(rv.diem) không thay được số review yêu cầu?
(c) Cho kết quả. Chỉ assert len(kq)==4 có đủ kiểm số review/phạm vi năm đúng chưa?

#### B6-060

rv có bốn review; listing_id là mã chuỗi ba ký tự; date datetime ghi ngày địa phương America/Santiago:
```python
rv = pd.DataFrame({'listing_id':['001','001','002','003'],
 'date':pd.to_datetime(['2025-01-01','2025-01-01','2025-01-02','2025-01-02'])})
```
Bảng thời tiết w có khóa chuỗi ISO cùng múi giờ; mỗi hàng dự kiến là một ngày:
```python
w = pd.DataFrame({'time':['2025-01-01','2025-01-01','2025-01-02','2025-01-03'],
                  't_c':[30.,31.,32.,33.]})
```
(a) Cần đếm review theo ngày rồi ghép vào thời tiết để mỗi ngày thời tiết một hàng. Phải kiểm/sửa vấn đề gì trước ghép? Không có thông tin chọn hộ một trong hai giá 30,31.
(b) Giả sử sau đối chiếu nguồn đã xác nhận w_ok gồm 01/01:30,02/01:32,03/01:33. Viết vài dòng đếm/ghép đúng khóa; quy ước ngày không có dòng review được ghi n_review thiếu, chưa tự coi là 0.
(c) Nêu ý nghĩa mỗi hàng, kiểm kết quả và điều kiện so với SQL. Nếu cần ghép thêm bảng listing có id đang là số 1,2,3, astype(str) có đủ khớp mã gốc không?

### Tự học bổ sung — ưu tiên thấp hơn

#### B6-MR11

API key lấy từ Secrets. Muốn thử lại biểu đồ trên đúng dữ liệu vừa tải, người học gọi API trong mỗi lần vẽ và gặp 429. Hành động nào phù hợp?

A. Dán key thật vào notebook chia sẻ để tăng hạn mức.

B. Tách bước tải và phân tích: dùng snapshot đã lưu để thử biểu đồ; giữ key ngoài mã chia sẻ, xử lý 429 theo hướng dẫn dịch vụ khi thực sự cần tải mới.

C. Bỏ kiểm HTTP để mỗi JSON 429 thành một ngày dữ liệu mới.

D. Cứ gọi lại cùng URL thì không bao giờ bị tính quota hoặc thay dữ liệu.

#### B6-MR12

rv có một hàng mỗi review, date datetime, listing_id chuỗi. l có một hàng mỗi listing với id đang là số nguyên, name chuỗi. Dịch vụ quy định mã là chữ số không đệm 0, nên số 1 và chuỗi '1' là cùng mã; l.id duy nhất.
```python
rv = pd.DataFrame({'listing_id':['1','1','1','2','2','3'],
 'date':pd.to_datetime(['2024-01-01','2025-01-01','2025-01-02',
                        '2025-01-03','2025-01-04','2025-01-05'])})
l = pd.DataFrame({'id':[1,2,3,4], 'name':['An','Binh','Chi','Dung']})
```
Chuẩn hóa khóa ở pandas theo quy ước trên; viết SQL lấy top 2 listing theo số review năm 2025 kèm tên. Nếu đồng hạng, ưu tiên listing_id chuỗi tăng dần. Cho kết quả; không giả định việc ghép hai kiểu khóa luôn tự đúng.

### Độ bao phủ sau đợt 6

Đã dùng 58/58 mục tiêu trong yêu cầu trả lời. Không còn mục tiêu thiếu trong phạm vi đã xác định.

## Đối chiếu cuối bộ

- Đủ **B6-001–B6-060: 60 câu = 40 TN + 20 TL**, nhóm chính **14/8/14/16/8**.
- Đủ **B6-MR01–B6-MR12: 12 câu = 8 TN + 4 TL**, đặt riêng từng đợt.
- Mức độ thiết kế: **15 nền tảng + 33 vận dụng + 12 phân loại**, không phải tần suất thi chính thức hay dự báo chắc chắn.
- **58/58 mục tiêu** thực sự được dùng để trả lời. Các câu SQL ba phần gần cấu trúc GK câu 24 gồm **008,019,028,039**; giữ/đổi phạm vi, COUNT/WHERE/HAVING và ý nghĩa được kiểm trực tiếp.
- Đọc nén, ngày, API lịch sử, year(date) ở phần chính theo LAB; chunksize/benchmark/EXPLAIN/key/quota và top-k tự làm giữ nhãn bổ sung. Không đếm các tên API chỉ tình cờ nhắc trong đáp án là mục tiêu đã phủ.
- Đã rà trùng ý, các cặp đối chiếu có chủ đích thay đổi cơ chế/tập hàng hoặc yêu cầu kiểm chứng, không chỉ đổi số/tên từ đề gốc. Độ bao phủ bài học khác mức ưu tiên từ đề mẫu; không mở rộng toàn sách/website liên kết.

Đã thực thi **66/72 câu** bằng các thư viện nêu ở đầu; **6 câu** cơ chế/thiết kế được kiểm bằng suy luận, chưa thực thi. API chỉ mô phỏng/đầu vào cố định; không chứng minh tham số thật hợp lệ với dịch vụ và không dùng forecast thật làm đáp án. Không đo benchmark thật; các số liệu benchmark nếu có được đề cung cấp để diễn giải.
