# BÀI 7 — NGÂN HÀNG 80 CÂU HỎI

60 câu bài giảng/lab và 20 câu luyện regex bổ sung; tám đợt, mỗi đợt mười câu.

## Nguồn đã đọc và phạm vi

- **BG:** [bai-07-xu-ly-du-lieu-chuoi.md](<D:/LTXLDL_GK/Bài 7/bai-07-xu-ly-du-lieu-chuoi.md>), toàn văn. Tệp tự ghi là bản tóm lược bằng lời riêng, không phải chép nguyên văn bài giảng; dùng cùng notebook.
- **NB:** [lecture_07.ipynb](<D:/LTXLDL_GK/Bài 7/lecture_07.ipynb>), đủ 106 ô, gồm hướng dẫn, code, TODO, assert, tự học và ghi chú backend.
- **LAB:** [lab_07.ipynb](<D:/LTXLDL_GK/Bài 7/lab_07.ipynb>), đủ 41 ô, gồm khởi động, quy ước giá, khảo sát comments, thay đúng HTML, từ sau near/cerca de, tiện nghi và bài tự làm.
- **RX:** [bai07_regex_luyen_tap.ipynb](<D:/LTXLDL_GK/Bài 7/bai07_regex_luyen_tap.ipynb>), đủ 102 ô: quy ước chung, 20 đề, mã khởi đầu, mọi CASES/test đoạn văn và phần giải thích. Mã khởi đầu còn trống không được coi là lời giải đúng.
- **GK:** [đề giữa kỳ luyện tập](<D:/LTXLDL_GK/Bài_kiểm_tra/2627I_UET.DSE2049 - Kiểm tra giữa kỳ (luyện tập) (1).pdf>), đã đọc trong cùng cuộc làm việc; đọc lại trực tiếp câu 17–18 và 25 để hiệu chỉnh ranh giới, lỗi chuyển giá và mẫu số tiện nghi.
- **AI5/DS1/DS2:** [AI5](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_5.pdf>), [DS1](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_1.pdf>), [DS2](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_2.pdf>), đã đọc đủ trong cùng cuộc làm việc, tham khảo cách hỏi và nhiễu có cơ chế của Nguyễn Tuấn Phong.
- **AI1/AI2:** [AI1](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_1.pdf>), [AI2](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_2.pdf>), đã đọc đủ trong cùng cuộc làm việc, chỉ bổ trợ cách diễn đạt/suy luận. Hai tệp ghi Đào Việt Anh, không gán nhầm tác giả.

Không thiếu bốn nguồn Bài 7 hoặc sáu đề được yêu cầu. Không tải snapshot thật, không mở rộng toàn bộ tài liệu liên kết hay lấy kiến thức NumPy tuần 3 làm phạm vi. Số ô tham chiếu tính từ 0. Không tuyên bố đã hoàn thành/chạy trọn notebook còn TODO. Phần A gồm nội dung bài giảng/lab và một số mục tự học được ghi ưu tiên rõ trong đáp án; phần B luyện thêm không mặc định khó hơn A. Mức phổ biến theo GK khác độ bao phủ tài liệu, không phải dự báo đề thi.

## Phiên bản và quy ước

- Nguồn ghim pandas **3.0.3** và PyArrow **25.0.1**. Kiểm chứng thực tế dùng **pandas 3.0.1, Python 3.12.14, PyArrow 25.0.1, NumPy 2.3.5**; không tuyên bố đã chạy pandas 3.0.3. Các câu thông thường dùng ASCII hoặc Python re, không dựa vào khác biệt nhỏ giữa hai bản pandas. Câu backend ghi riêng cấu hình thực tế và kết quả đã chạy.
- Mỗi câu độc lập, có `import pandas as pd`, `import numpy as np`, `import re`, `import json` khi cần. Regex cốt lõi dùng Python re qua chuỗi Python/Series object hoặc cấu hình được chỉ định. Các ví dụ object chỉ chứa str/None, trừ khi nói khác. Không đoán engine từ tên dtype str.
- Mọi chuỗi giữ nguyên đầu/cuối và hoa thường nếu đề không cho strip/lower. Flags=0 trừ chỗ ghi re.I/case=False. Python re mặc định không có DOTALL/MULTILINE. Nếu newline ảnh hưởng kết quả, đề nêu rõ. Phần B chữ số ASCII, không dùng lookaround, backreference hay cờ nâng cao.
- Các mã/index gốc là duy nhất trước explode trừ khi đề nói khác. Sau explode có thể lặp. [] là danh sách đã biết rỗng; None là chưa biết, mẫu số phải theo đề. Không khớp không tự thành số 0. Nhận NaN/NA/None khi đáp án chỉ yêu cầu thiếu logic, không hỏi nguyên văn kiểu hiển thị.
- Giá tiền ghi đơn vị và quy tắc từng câu. Chấp nhận tỷ lệ dạng phân số hoặc sai số tuyệt đối 1e-12. Kiểm số thực bằng assert_allclose, thiếu bằng isna; không so NaN bằng ==.
- TN đúng một đáp án, có thể chấm 1 điểm/câu; TL có thang 2 hoặc 3 điểm, chấp nhận code/regex tương đương đáp ứng toàn quy tắc. Test hữu hạn hỗ trợ kiểm tra, không chứng minh mọi đầu vào đều đúng.

## Ma trận toàn bộ

Phần A: 60=40 TN+20 TL; mức thiết kế 15/33/12. Phần B: 20=12 TN+8 TL, một câu cho mỗi dạng RX. Đây không phải tỷ trọng chính thức hoặc kết quả đo độ khó thực nghiệm. Mỗi câu một nhóm chính, tối đa hai mục tiêu phụ.

| Nhóm chính A | Tổng | TN | TL | Nền tảng | Vận dụng | Phân loại |
| --- | --- | --- | --- | --- | --- | --- |
| Chuẩn hoá, phương thức .str và giá trị thiếu | 10 | 7 | 3 | 4 | 4 | 2 |
| Chuyển đổi giá và kiểm tra định dạng | 10 | 6 | 4 | 2 | 6 | 2 |
| Regex, phương thức khớp và trích nhóm | 20 | 14 | 6 | 5 | 14 | 1 |
| JSON, split, explode và đếm/tính tỷ lệ | 14 | 9 | 5 | 3 | 6 | 5 |
| Kiểm chứng quy tắc, diễn giải và hiệu năng | 6 | 4 | 2 | 1 | 3 | 2 |

| Đợt | Mã câu | TN/TL |
| --- | --- | --- |
| 1 | B7-001–B7-010 | 7/3 |
| 2 | B7-011–B7-020 | 7/3 |
| 3 | B7-021–B7-030 | 7/3 |
| 4 | B7-031–B7-040 | 7/3 |
| 5 | B7-041–B7-050 | 6/4 |
| 6 | B7-051–B7-060 | 6/4 |
| 7 | B7-R01–B7-R10 | 6/4 |
| 8 | B7-R11–B7-R20 | 6/4 |

## Danh mục mục tiêu lập trước khi soạn

Mã ở cột câu bỏ tiền tố B7-. Chỉ tính mục tiêu thực sự dùng để trả lời, không tính kiến thức chỉ nhắc trong đáp án.

| Mã | Mục tiêu | Ưu tiên theo nguồn | Câu dự kiến | Đọc lại |
| --- | --- | --- | --- | --- |
| K01 | Chuỗi Python có strip; Series dùng accessor .str, không có strip trực tiếp | Trọng tâm | 001,018 | BG §1; NB ô 4–8 |
| K02 | strip chỉ hai đầu; lower trả kết quả mới giữ index và bản gốc; không xóa khoảng trắng giữa | Trọng tâm | 001,006,031,038,057 | NB ô 7–13; LAB ô 6–7 |
| K03 | Không tự gộp khác dấu, dấu câu, chính tả; wifi/wifi!/wi-fi cần quy tắc riêng | Trọng tâm | 006,038,057 | NB ô 12–13; LAB ô 6–7 |
| K04 | Chuỗi rỗng, toàn khoảng trắng, thiếu khác nhau; dropna không loại chuỗi rỗng | Trọng tâm | 011,033,052 | NB ô 79–81; LAB ô 15–18 |
| K05 | contains tìm đoạn con, không xác nhận từ độc lập hay ý nghĩa | Trọng tâm | 018,021 | NB ô 14–20,66–67 |
| K06 | case=False và regex=False tìm nguyên văn bỏ hoa thường; na=False không chọn thiếu | Trọng tâm | 018,021 | NB ô 16–20; LAB ô 8 |
| K07 | contains mặc định regex; . wildcard, \\. chấm thật; raw string không tắt regex | Trọng tâm | 021,027,059 | NB ô 42–45; LAB ô 8 |
| K08 | na=False có thể vẫn đưa tên thiếu vào mẫu số mean; không chứng minh đối tượng không có thuộc tính | Trọng tâm | 018,053 | NB ô 18–20,66–67 |
| K09 | dtype string/str/object có thể khác kết quả thiếu; chỉ hỏi với dtype/config rõ | Trọng tâm | 053 | NB ô 19–20 |
| K10 | startswith/endswith kiểm tiền tố/hậu tố, không phải so nhãn bằng nhau | Tự học — bảng tra | 042 | NB ô 94 bảng tra |
| K11 | str.len/str.slice giữ nhãn; độ dài ngắn không tự là vô ích | Trọng tâm (len trong LAB); slice tự học bảng tra | 011,031 | NB ô 94; LAB ô 15–18 |
| K12 | split đúng dấu phân cách; expand đổi dạng cột; join nối các phần tử trong ô | Trọng tâm: split; đọc thêm: join/bảng tra | 042,054 | BG §3; NB ô 70–71,94 |
| K13 | upper/lower/casefold không đồng nghĩa; casefold trong bảng tra, không tự xóa dấu | Tự học — upper/casefold | 031,057 | NB ô 94 |
| K14 | pandas 3 str.replace mặc định regex=False; [$,] cần regex=True | Trọng tâm | 003,012 | BG §1; NB ô 23–31; LAB ô 10 |
| K15 | Bỏ ký hiệu tiền/phân cách theo quy ước nguồn; dấu phẩy nghìn khác dấu phẩy thập phân | Trọng tâm | 008,012,023,058 | NB ô 21–24; LAB ô 9–12 |
| K16 | to_numeric coerce; lỗi raw.notna & parsed.isna khác thiếu từ nguồn, kể cả chuỗi rỗng có dữ liệu | Trọng tâm | 003,008,012,033 | NB ô 32–37; LAB ô 9–10; GK câu 18 |
| K17 | Giữ giá gốc; chưa biết khác 0, không fillna(0) tùy ý | Trọng tâm | 008,047,058 | NB ô 37–39; LAB ô 9–10 |
| K18 | Trích/chuyển được số không chứng minh cả chuỗi đúng định dạng hay phân cách nghìn hợp lệ | Trọng tâm | 026,030,047 | NB ô 103–104; LAB ô 11–12 |
| K19 | fullmatch giá: dấu $, không âm, 0 hợp lệ, nhóm nghìn đúng, thập phân hai chữ số, strip khi được phép | Trọng tâm LAB; mẫu ở phần tự học NB | 026,030,044,047 | NB ô 103–104; LAB ô 11–12 |
| K20 | Chuẩn hoá loại phòng rồi median trên đúng tập giá biết; không đổi sang mean hoặc điền thiếu 0 | Trọng tâm | 058 | NB ô 38–39; LAB mục tiêu 1 |
| K21 | Hai tầng escape Python/regex; r"\\b" khác backspace "\\b"; raw giữ backslash | Trọng tâm | 002,027 | NB ô 45–51 |
| K22 | Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước | Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học | 041,051,R03–R08 | NB ô 45,94; RX câu 3–8 |
| K23 | Ngoặc giới hạn \|; các nhánh thiếu tiền tố có thể khớp sai | Trọng tâm | 022,R10 | NB ô 45; RX câu 10 |
| K24 | Nhóm bắt và không bắt; nhóm thừa đổi phần dữ liệu/shape được trả | Trọng tâm | 005,024 | NB ô 45,63 |
| K25 | \\b là ranh giới ký tự từ, không là dấu cách; số và _ cũng là ký tự từ | Trọng tâm | 002,009,019,035,060 | NB ô 49–51,98–102; GK câu 17 |
| K26 | contains bất kỳ đâu, match từ đầu, fullmatch cả chuỗi; không nhầm kiểm một đoạn với cả định dạng | Trọng tâm | 013,030,046 | BG §2; NB ô 55–58,94 |
| K27 | extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0 | Trọng tâm | 009,015,019,032,039,050 | NB ô 47–54,63 |
| K28 | expand=False một nhóm → Series; nhiều nhóm → DataFrame; extract không nhóm bắt gây lỗi | Trọng tâm | 005,045 | NB ô 63; kiểm API bằng ca cục bộ |
| K29 | re.search: group(0) cả đoạn, group(1) nhóm đầu, groups tuple; thiếu nhóm nhánh là None | Trọng tâm | 022,024 | RX quy ước chung; NB ô 94 |
| K30 | re.findall/re.sub trên chuỗi Python; không tự là pandas Series hay số | Trọng tâm | 041,051,059 | NB ô 94–95 |
| K31 | extractall giữ mọi lần và index nguồn; Int64 giữ số nguyên với thiếu | Tự học — extractall/Int64 | 032,050 | NB ô 96–97 |
| K32 | BR/bedroom(s), re.I, \\s*, ranh giới: giảm bravo nhưng bỏ 2BR2BA; không khớp không suy không phòng | Trọng tâm | 007,009,015,R10 | NB ô 40–54,98–100 |
| K33 | bath/baths/bathroom(s)/WC theo đúng các nhánh đề cho; chữ dính số và ranh giới | Trọng tâm | 019 | GK câu 17; cơ chế NB ô 45–54 |
| K34 | Diện tích m2/m², re.I; thập phân chấm/phẩy theo LAB; loại m2x và giữ bản gốc | Trọng tâm diện tích; mở rộng thập phân: LAB tự làm | 035,039 | NB ô 59–60; LAB tự làm 2 |
| K35 | Chỉ thay đúng <br/> bằng một dấu cách; đếm dòng khác số lần thay; không là làm sạch mọi HTML | Trọng tâm | 059 | LAB ô 19–20 |
| K36 | near/cerca de lấy một từ đầu theo mẫu, không chắc địa danh hay cả tên địa điểm | Trọng tâm | 049 | LAB ô 21–28 |
| K37 | JSON string → json.loads → list; tên có dấu phẩy vẫn một mục, không split JSON theo phẩy | Trọng tâm | 004,014,020 | NB ô 68–75; LAB ô 31–32 |
| K38 | json.loads(None) lỗi nếu không xử lý; None chưa biết không tự đổi [] | Trọng tâm | 014,048 | LAB ô 33–36 |
| K39 | explode mỗi phần tử thành hàng, giữ index lặp; [] tạo placeholder thiếu | Trọng tâm | 016,028,034,040 | NB ô 76–81; LAB ô 31–36 |
| K40 | dropna sau explode bỏ placeholder/thiếu, không bỏ chuỗi rỗng; phân biệt trước/sau bỏ thiếu | Trọng tâm | 016,040,052 | NB ô 78–81 |
| K41 | Chuẩn hoá từng mục rồi nunique id; mục lặp cùng listing không thành nhiều listing | Trọng tâm | 020,028,036 | NB ô 87–92 |
| K42 | Tỷ lệ listing có tiện nghi khác tỷ lệ mục tiện nghi; một bool mỗi listing và mẫu số đúng | Trọng tâm | 010,020,025,040,043 | NB ô 82–86; GK câu 25 |
| K43 | Danh sách biết rỗng vẫn thuộc mẫu số listing; không dùng số hàng exploded thay thế | Trọng tâm | 010,043,048 | NB ô 81–86; LAB ô 33–36 |
| K44 | None chưa biết; phải nêu mẫu số toàn bộ hay nhóm đã biết, không trộn [] với None | Trọng tâm | 010,048 | LAB ô 35–36 |
| K45 | Wifi đúng nhãn khác Pocket wifi/wifi!; tìm substring JSON thô khác membership sau chuẩn hoá | Trọng tâm | 025,043 | BG §3; NB ô 89–92; LAB ô 29 |
| K46 | Giữ bảng gốc đủ listing để không mất rỗng/thiếu sau explode-dropna; nhãn gắn đúng nguồn | Trọng tâm | 028,034,048 | NB ô 81; LAB ô 32–36 |
| K47 | Nhắc metro/wifi không xác minh khoảng cách, hài lòng hay tiện nghi hoạt động tốt; tên cột đúng phép đo | Trọng tâm | 017,049 | NB ô 66–67,93; LAB tự làm 1 |
| K48 | Số khớp không là độ chính xác; kiểm dương/âm/gần đúng và nguyên văn, test hữu hạn không là chứng minh mọi đầu vào | Trọng tâm | 007,037,049 | NB ô 64–65,93; LAB ô 1,25–28 |
| K49 | Kiểm giá trị/index/thiếu trước benchmark; đổi dtype ngoài phần đo; hiệu năng tùy backend, không .str luôn nhanh hơn | Trọng tâm | 029,056 | NB ô 25–31 |
| K50 | Python re mặc định Unicode: \\w/\\d không chỉ ASCII; [0-9] rõ miền chữ số ASCII | Tự học — Unicode | 055,060,R01 | NB ô 101–102; RX quy ước |
| K51 | Arrow/Python có thể khác ranh giới/từ; ghim dtype, storage, phiên bản và kiểm thực tế, không khái quát engine | Tự học — Unicode/backend | 060 | NB ô 101–102 |
| K52 | ^/$ và fullmatch khác khi có newline cuối; . mặc định không ăn newline; phải nêu flags/quy ước | Tự học — ký hiệu mở rộng/quy ước | 027,046,R02 | NB ô 44,94; RX câu 2 |
| K53 | Dãy chữ số ASCII đầu tiên | Luyện regex bổ sung | R01 | RX câu 1: ô 2–6 |
| K54 | Dấu chấm thường/wildcard | Luyện regex bổ sung | R02 | RX câu 2: ô 7–11 |
| K55 | Tập ký tự | Luyện regex bổ sung | R03 | RX câu 3: ô 12–16 |
| K56 | Khoảng ký tự | Luyện regex bổ sung | R04 | RX câu 4: ô 17–21 |
| K57 | Giới hạn số lần lặp | Luyện regex bổ sung | R05 | RX câu 5: ô 22–26 |
| K58 | Không lần/ít nhất một/tối thiểu | Luyện regex bổ sung | R06 | RX câu 6: ô 27–31 |
| K59 | Tùy chọn và dấu hỏi thường | Luyện regex bổ sung | R07 | RX câu 7: ô 32–36 |
| K60 | Ký tự trắng phân cách | Luyện regex bổ sung | R08 | RX câu 8: ô 37–41 |
| K61 | Tên PDF và nhóm bắt | Luyện regex bổ sung | R09 | RX câu 9: ô 42–46 |
| K62 | Số phòng/hoặc/ranh giới | Luyện regex bổ sung | R10 | RX câu 10: ô 47–51 |
| K63 | Số nguyên/thập phân đơn giản | Luyện regex bổ sung | R11 | RX câu 11: ô 52–56 |
| K64 | Nhóm nghìn và số mũ | Luyện regex bổ sung | R12 | RX câu 12: ô 57–61 |
| K65 | Mã vùng điện thoại/ngoặc đủ cặp | Luyện regex bổ sung | R13 | RX câu 13: ô 62–66 |
| K66 | Tài khoản email trước +filter | Luyện regex bổ sung | R14 | RX câu 14: ô 67–71 |
| K67 | Thẻ mở ngoài chú thích giản lược | Luyện regex bổ sung | R15 | RX câu 15: ô 72–76 |
| K68 | Tên ảnh/phần mở rộng | Luyện regex bổ sung | R16 | RX câu 16: ô 77–81 |
| K69 | Cắt dấu cách-tab và tham lam | Luyện regex bổ sung | R17 | RX câu 17: ô 82–86 |
| K70 | Log: phương thức/tệp/dòng | Luyện regex bổ sung | R18 | RX câu 18: ô 87–91 |
| K71 | URL: giao thức/máy chủ/cổng | Luyện regex bổ sung | R19 | RX câu 19: ô 92–96 |
| K72 | Đường dẫn URL, loại query/fragment | Luyện regex bổ sung | R20 | RX câu 20: ô 97–101 |

## Đợt 1 — phần A

### B7-001

```python
s = pd.Series([' A  B ', ' WIFI ', None, ''], index=[4,7,9,12], dtype=object)
t = s.str.strip().str.lower()
```
Nhận định nào đúng?

A. t giữ index [4,7,9,12], có 'a  b','wifi',thiếu,''; s vẫn giữ chuỗi gốc.

B. t có 'ab','wifi',thiếu,'' vì strip xóa mọi dấu cách.

C. Thay s.str.strip() bằng s.strip() vẫn đúng.

D. t tự đặt index thành 0,1,2,3 và sửa luôn s.

### B7-002

Python re, flags=0; chuỗi không chứa backspace:
```python
text = 'bath tub'
a = re.search(r'\bbath\b', text)
b = re.search('\bbath\b', text)
print(a is not None, b is not None)
```
Dòng cuối cho gì?

A. True,True

B. True,False

C. False,True

D. False,False

### B7-003

pandas 3; mỗi hàng một listing, phẩy ngăn nghìn:
```python
raw = pd.Series(['$800','$1,200',None,'hoi chu'], dtype=object)
p = pd.to_numeric(raw.str.replace(r'[$,]', ''), errors='coerce')
loi = raw.notna() & p.isna()
print(loi.sum())
```
In gì?

A. 3

B. 1

C. 4

D. 0

### B7-004

```python
raw = '["Stove, gas", "Wifi"]'
ds = json.loads(raw)
print(type(ds).__name__, len(ds), ds[0])
```
Kết quả nào đúng?

A. list,2,Stove, gas

B. list,3,Stove

C. str,2,Stove, gas

D. list,2,Wifi

### B7-005

```python
s = pd.Series(['2BR','3 bedrooms','Studio','1 br'], index=['A','B','C','D'], dtype=object)
p = r'([0-9]+)\s*(BR|bedrooms?)'
x = s.str.extract(p, flags=re.I, expand=False)
```
Kiểu, shape và hàng B của x là gì?

A. Series, (4,), chỉ '3'.

B. DataFrame, (4,1), '3 bedrooms'.

C. DataFrame, (3,2), hai nhóm '3' và 'bedrooms'.

D. DataFrame, (4,2), hai nhóm '3' và 'bedrooms'.

### B7-006

```python
s = pd.Series([' Wifi ','WIFI','wifi!','wi-fi','Café','Cafe'], dtype=object)
print(s.str.strip().str.lower().nunique())
```
In gì? Chỉ gộp theo hai phép đã viết.

A. 3

B. 5

C. 4

D. 6

### B7-007

Trên cùng 100 tên, mẫu rộng lấy số ở 18 tên, mẫu thêm ranh giới từ lấy ở 14 tên. Chưa có nhãn tay; đã thấy mẫu rộng lấy nhầm số trong '12bravo', mẫu chặt bỏ '2BR2BA'. Kết luận nào được hỗ trợ?

A. Chưa biết mẫu nào chính xác hơn chỉ từ số khớp; cần kiểm cả tên khớp, không khớp và mục tiêu quy tắc.

B. Mẫu rộng chính xác hơn vì 18>14.

C. Mẫu chặt hoàn hảo vì đã loại bravo.

D. Bốn tên chỉ mẫu rộng nhận chắc chắn đều sai.

### B7-008

Mỗi hàng một listing, USD/đêm; $ ở đầu, phẩy ngăn nghìn, chấm thập phân. None thiếu nguồn; chuỗi không chuyển được là lỗi:
```python
raw = pd.Series([' $2,000.00 ',None,'lien he','tu $500','$0'],
                index=['A','B','C','D','E'], dtype=object)
```
(a) Viết pipeline bỏ khoảng trắng hai đầu, ký hiệu đã biết rồi chuyển số; giữ raw, tạo loi.
(b) Vì sao fillna(0) ngay sau chuyển làm mất thông tin?
(c) Cho parsed, mã lỗi và số thiếu nguồn; nêu ca biên giá 0.

### B7-009

Chỉ có số nguyên ASCII không dấu, không âm/thập phân. Python re qua object:
```python
s = pd.Series(['2BR_apt','House 3 BR!','2BR2BA','x4BR','5 bedrooms'],
              index=[10,20,30,40,50], dtype=object)
p = r'\b([0-9]+)\s*(?:BR|bedrooms?)\b'
x = s.str.extract(p, flags=re.I, expand=False)
```
Nhãn nào có kết quả, giá trị/kiểu nào? Vì sao ba tên kia không khớp? Có thể kết luận 0 phòng không?

### B7-010

Mỗi mã một listing; [] biết rỗng, None chưa biết. Chỉ strip+lower nhãn, Pocket wifi khác wifi:
```python
raw = pd.Series(['["Wifi","Wifi"]','[]',None,'["Pocket wifi"]','[" wifi "]'],
                index=['A','B','C','D','E'], dtype=object)
```
(a) Tính tỷ lệ listing có wifi trong nhóm đã biết tiện nghi.
(b) Vì sao không lấy mean so sánh trên mục sau explode/dropna?
(c) Nêu tử/mẫu đúng; nếu chỉ explode nhóm đã biết rồi so sánh, chưa dropna, phép mean chia cho bao nhiêu?

### Độ bao phủ sau đợt 1

Đã dùng 18/72 mục tiêu. Còn: K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K18, K19, K20, K22, K23, K26, K29, K30, K31, K33, K34, K35, K36, K38, K39, K40, K41, K45, K46, K47, K49, K50, K51, K52, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 2 — phần A

### B7-011

```python
s = pd.Series(['', '   ', None, 'OK'], index=['A','B','C','D'], dtype=object)
t = s.str.strip().dropna()
print(t.index.tolist(), t.str.len().tolist())
```
Kết quả nào đúng? Có đủ căn cứ từ độ dài để kết luận 'OK' là văn bản vô ích cần loại không?

A. ['D'] và [2]

B. ['A','B','D'] và [0,0,2]; chưa đủ căn cứ loại OK chỉ vì ngắn.

C. ['A','B','D'] và [0,3,2]

D. ['A','B','C','D'] và [0,0,0,2]

### B7-012

USD/đêm, phẩy ngăn nghìn, None thiếu nguồn:
```python
raw = pd.Series(['$10','$1,500',None,'negotiable','$0'], dtype=object)
p = pd.to_numeric(raw.str.replace('$','',regex=False), errors='coerce')
print((raw.notna() & p.isna()).tolist())
```
Kết quả nào đúng?

A. [False,False,False,True,False]

B. [False,True,True,True,False]

C. [False,True,False,True,True]

D. [False,True,False,True,False]

### B7-013

Python re qua object, na=False ở cả ba phép:
```python
s = pd.Series(['Q7','Q7x','ma Q7','xQ',''], dtype=object)
p = r'Q[0-9]+'
```
Những chỉ mục True của contains(p), match(p), fullmatch(p) lần lượt là gì?

A. [0,1,2]; [0]; [0]

B. [0,1]; [0,1]; [0]

C. [0,1,2]; [0,1,2]; [0,1]

D. [0,1,2]; [0,1]; [0]

### B7-014

```python
raw = pd.Series(['["Wifi"]', None, '[]', '["Kitchen"]'], dtype=object)
ds = raw.map(json.loads)
```
Điều gì xảy ra ở mã hiện tại?

A. ds tự có None thành [] và không lỗi.

B. TypeError khi json.loads nhận None; cần quy tắc cho thiếu trước khi đọc từng ô.

C. ds tự bỏ hàng None nên còn ba listing.

D. ds giữ bốn chuỗi gốc vì json.loads không làm đổi kiểu.

### B7-015

Chỉ số nguyên ASCII không dấu; Python re qua object:
```python
s = pd.Series(['01 BR, 2BR annex','Studio','0BR','3 bedroom'], index=['L1','L2','L3','L4'], dtype=object)
x = s.str.extract(r'\b([0-9]+)\s*(?:BR|bedrooms?)\b', flags=re.I, expand=False)
```
Giá trị L1,L2,L3 lần lượt là gì?

A. [1,2],thiếu,0; x là danh sách số.

B. '2',thiếu,'0'; x là Series.

C. '01','0','0'; x là Series.

D. '01',thiếu,'0'; x là Series giữ nhãn.

### B7-016

Mỗi mã một listing; [] biết rỗng, None chưa biết:
```python
ds = pd.Series([['Wifi','TV'],[],None,['Kitchen']], index=['A','B','C','D'], dtype=object)
e = ds.explode()
print(len(e), len(e.dropna()), e.dropna().index.tolist())
```
In gì?

A. 5,3,['A','A','D']

B. 3,3,['A','A','D']

C. 5,4,['A','A','B','D']

D. 5,3,[0,1,2]

### B7-017

Ba review có comments: 'Wifi worked well', 'No internet during stay', 'wifi was slow'. Mask contains(`r'wifi|internet'`,case=False,regex=True,na=False) đều True. Kết luận nào đúng?

A. Ba review đều hài lòng về mạng vì đều khớp.

B. Chỉ review đầu được mask chọn vì contains tự loại các câu phủ định và chê mạng.

C. Có ba listing khác nhau có mạng tốt.

D. Có ba review nhắc wifi/internet; chưa suy ra ba khách hài lòng hay mạng hoạt động tốt.

### B7-018

Mỗi hàng một listing:
```python
s = pd.Series(['Metro nearby',None,'100 metros','Casa'], index=[8,2,9,5], dtype=object)
m = s.str.contains('metro',case=False,regex=False,na=False)
```
(a) Cho m và m.mean(), mẫu số nào được dùng?
(b) Tính tỷ lệ tên nhắc đoạn metro chỉ trong nhóm có tên đã biết.
(c) Vì sao cả hai số không là tỷ lệ listing thật sự gần metro?

### B7-019

Chỉ có số nguyên ASCII không dấu, không âm/thập phân. Viết một mẫu có đúng một nhóm bắt số, cho phép không hoặc nhiều ký tự trắng, theo sau là WC,bath,baths,bathroom,bathrooms không phân biệt hoa thường; hai đầu cụm phải có ranh giới từ. Trích lần đầu trên:
```python
s = pd.Series(['Flat 2bathroom!','3 WC','Villa4baths','1bath_apt','No bath count'],
              index=['A','B','C','D','E'], dtype=object)
```
Cho kết quả và giải thích C,D. Không thay không khớp bằng 0.

### B7-020

Mỗi mã một listing, không thiếu nguồn; chỉ strip+lower nhãn:
```python
raw = pd.Series(['["Stove, gas","Wifi"]','["wifi ","WIFI"]','[]','["TV"]'],
                index=['A','B','C','D'], dtype=object)
```
(a) Lập số listing khác nhau có từng nhãn tiện nghi.
(b) Vì sao split(',') và value_counts ngay sau explode đều có thể sai yêu cầu?
(c) Tỷ lệ listing có wifi là bao nhiêu? Nêu tử/mẫu và vai trò C.

### Độ bao phủ sau đợt 2

Đã dùng 30/72 mục tiêu. Còn: K07, K09, K10, K12, K13, K18, K19, K20, K22, K23, K29, K30, K31, K34, K35, K36, K45, K46, K49, K50, K51, K52, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 3 — phần A

### B7-021

pandas 3, không có newline:
```python
s = pd.Series(['a.b','axb','',None], dtype=object)
a = s.str.contains('.', na=False)
b = s.str.contains('.', regex=False, na=False)
```
a và b lần lượt là gì?

A. [True,False,False,False] và [True,False,False,False]

B. [True,True,False,False] và [True,False,False,False]

C. [True,True,True,False] và [True,False,False,False]

D. [True,True,False,True] và [True,False,False,True]

### B7-022

Python re, flags=re.I:
```python
p = r'\b([0-9]+)\s*BR|bedrooms?\b'
m = re.search(p, 'bedrooms only')
print(m.group(0), m.group(1))
```
Kết quả và cơ chế nào đúng?

A. Không khớp vì toàn pattern luôn đòi một số trước bedrooms.

B. bedrooms và bedrooms; group(1) luôn giống group(0).

C. bedrooms và None; nhánh bedrooms? không bị ràng buộc bởi phần số ở nhánh trái.

D. bedrooms và 0; nhóm không tham gia tự cho số 0.

### B7-023

Nguồn X quy định dấu phẩy là dấu thập phân, không có dấu phân cách nghìn. Với chuỗi '12,50', người học bỏ dấu phẩy rồi to_numeric được 1250. Nhận định nào đúng?

A. Đúng vì mọi dấu phẩy trong giá luôn ngăn nghìn.

B. Đúng vì to_numeric đã không báo lỗi.

C. Giá phải là 0 vì không dùng dấu chấm như nguồn khác.

D. 1250 không đúng ý nghĩa giá 12.5; phải theo quy ước thập phân của nguồn trước khi chuyển.

### B7-024

Python re:
```python
m = re.search(r'([0-9]+)\s*(m2)', 'area 007 m2 near park')
print(m.group(0), m.group(1), m.groups())
```
Nhận định nào đúng?

A. group(0)='007 m2', group(1)='007', groups()=('007','m2').

B. group(0)='007', group(1)='m2', groups()=('m2',).

C. group(0)='007 m2', group(1)=7, groups()=(7,'m2').

D. group(0) là toàn câu area...park, group(1)='007'.

### B7-025

Bốn listing có JSON amenities lần lượt: ["Pocket wifi"], ["Wifi"], [], ["wifi!"]. Chỉ strip+lower, đúng nhãn wifi mới tính có Wifi. Tìm đoạn wifi không phân biệt hoa thường trên JSON thô cho 3/4. Tỷ lệ listing đúng yêu cầu là gì?

A. 3/4

B. 1/4

C. 1/3

D. 1

### B7-026

Chỉ giá không âm bắt đầu $, số nguyên viết liền hoặc ngăn nghìn đúng ba chữ số; thập phân nếu có đúng hai chữ số. ASCII; không có khoảng trắng. Cho:
```python
s = pd.Series(['$1,20.00','$120.00','$0','$12.5'], dtype=object)
p = r'\$(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]{2})?'
```
Chỉ mục True của fullmatch(p,na=False) là gì?

A. [1,2]

B. [0,1,2,3]

C. [0,1,2]

D. [1]

### B7-027

Python re, flags=0; mẫu raw không được sửa:
```python
p = r'A.B'
text = ['A.B','AxB','AB','A\nB']
print([re.fullmatch(p,x) is not None for x in text])
```
Kết quả nào đúng?

A. [True,False,False,False]

B. [True,True,False,False]

C. [True,True,True,False]

D. [True,True,False,True]

### B7-028

Mỗi mã là một listing, không thiếu thông tin; chỉ strip+lower:
```python
ds = pd.Series([['TV','tv '],[],['TV','Wifi'],['Wifi']], index=['A','B','C','D'], dtype=object)
```
Lập số listing khác nhau có mỗi tiện nghi và tỷ lệ listing có TV. Một bạn dùng số index khác nhau của bảng exploded sau dropna làm mẫu số. Chỉ ra kết quả sai đó, và vì sao giữ ds gốc cần thiết.

### B7-029

Hai cách bỏ $ và phẩy trên cột giá: .str.replace hai lần, hoặc apply một hàm Python giữ thiếu. Cách A được đo cả astype và to_numeric; cách B chỉ đo thay chuỗi. Người học thấy B nhanh hơn rồi kết luận apply luôn nhanh hơn .str. Viết cách sửa thiết kế và nêu những gì cần đối chiếu trước đo. Không yêu cầu viết bộ benchmark hoặc nhớ số đo máy giảng viên.

### B7-030

Quy tắc giá như mẫu dưới: không âm, $ bắt buộc, ASCII, nghìn đúng ba chữ số, thập phân hai chữ số; được strip hai đầu:
```python
raw = pd.Series(['from $400',' $400.00 ','$4,00.00','$0'], dtype=object)
p = r'\$(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]{2})?'
ok = raw.str.contains(p, regex=True, na=False)
```
Sửa một dòng kiểm đúng toàn định dạng. Những hàng nào hợp lệ? Vì sao trích được 400 hoặc bỏ phẩy rồi chuyển được 400 chưa đủ?

### Độ bao phủ sau đợt 3

Đã dùng 39/72 mục tiêu. Còn: K09, K10, K12, K13, K20, K22, K30, K31, K34, K35, K36, K50, K51, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 4 — phần A

### B7-031

```python
s = pd.Series([' abcd ','Wifi','',None], index=[5,9,12,20], dtype=object)
t = s.str.slice(0,2).str.upper()
```
t ở các nhãn 5,9,12,20 lần lượt là gì? Không có bước strip.

A. 'AB','WI','',thiếu

B. ' A','WI',thiếu,thiếu

C. 'ABCD','WIFI','',thiếu

D. ' A','WI','',thiếu

### B7-032

Python re qua object, chỉ số nguyên không dấu:
```python
s = pd.Series(['02 BR','Studio','0BR','3 bedrooms'], index=['A','B','C','D'], dtype=object)
x = s.str.extract(r'\b([0-9]+)\s*(?:BR|bedrooms?)\b',flags=re.I,expand=False)
n = pd.to_numeric(x,errors='coerce').astype('Int64')
```
Nhận định nào đúng?

A. n có dtype int64 thường và mọi chỗ thiếu tự bằng 0.

B. n giữ chuỗi 02 vì astype Int64 chỉ đổi tên dtype.

C. n giữ index A–D, dtype Int64; giá trị 2,thiếu,0,3.

D. n chỉ còn ba hàng có số.

### B7-033

Mỗi hàng một listing; None thiếu nguồn, chuỗi rỗng có dữ liệu nhưng không chuyển được; USD/đêm:
```python
raw = pd.Series(['$100',None,'','ask','$0'], dtype=object)
p = pd.to_numeric(raw.str.replace('$','',regex=False), errors='coerce')
print(raw.isna().sum(), (raw.notna() & p.isna()).sum())
```
Hai số nào được in?

A. 1,2

B. 2,1

C. 1,3

D. 3,0

### B7-034

Mỗi mã một listing:
```python
ds = pd.Series([['TV','Wifi'],['TV'],[],['Wifi']], index=['L4','L1','L7','L2'], dtype=object)
m = ds.explode().dropna()
print(m.index.tolist())
```
Kết quả nào đúng?

A. ['L4','L1','L7','L2']

B. [0,1,2,3]

C. ['L4','L1','L2']

D. ['L4','L4','L1','L2']

### B7-035

Tên chỉ dùng số nguyên không âm, không có dấu thập phân; Python re:
```python
s = pd.Series(['Loft 40m²','75 M2','30m2x','Villa45m2'], dtype=object)
p = r'\b([0-9]+)\s*m(?:2|²)\b'
x = s.str.extract(p,flags=re.I,expand=False)
```
Các hàng không thiếu là gì?

A. 0→'40',1→'75'

B. 0→'40',1→'75',2→'30'

C. Chỉ 0→'40'

D. 0→'40',1→'75',3→'45'

### B7-036

Sau chuẩn hoá strip+lower và explode/dropna, bảng dài gồm:

| id listing | nhãn |
| --- | --- |
| A | parking |
| A | parking |
| B | parking |
| C | wifi |

Để báo số listing có parking, nhận định nào đúng?

A. Có 3 listing vì value_counts parking bằng 3.

B. Có 2 listing A,B; nunique id trong nhóm parking phù hợp hơn đếm ba hàng.

C. Có 1 listing vì parking là một nhãn duy nhất.

D. Có 4 listing vì bảng dài có bốn hàng.

### B7-037

Một hàm regex đạt cả 12 test công khai. Người học nói đã chứng minh hàm đúng với mọi chuỗi, không cần xem quy tắc hoặc các dòng khớp trên dữ liệu mới. Nhận định nào đúng?

A. Đúng vì đủ 12 test thì mọi regex đều được chứng minh.

B. Sai nên không được dùng bất kỳ test nào để kiểm code.

C. Test đạt hỗ trợ kiểm tra 12 ca; vẫn phải đối chiếu quy tắc, thêm phản ví dụ và xem nguyên văn khi diễn giải.

D. Chỉ cần tăng số dòng khớp trên dữ liệu mới là thay được việc xem nguyên văn.

### B7-038

```python
s = pd.Series(['  Wifi  ','WIFI!','wi-fi','wifi','Café','Cafe'],
              index=[9,4,8,1,7,3], dtype=object)
```
(a) Tạo s_chuan chỉ bỏ khoảng trắng hai đầu và lower, giữ s.
(b) Một bạn xóa mọi dấu câu/dấu để gộp nhãn, vì sao chưa đáp ứng đúng quy tắc đã cho?
(c) Cho số lần từng nhãn sau chuẩn hoá, kiểm index và bản gốc.

### B7-039

Đầu vào không có số âm hoặc chuỗi số nhiều dấu thập phân. Cần trích diện tích ở cụm đầu tiên: số nguyên/ thập phân chấm hoặc phẩy, m2/m² không phân biệt hoa thường, ranh giới hai đầu; loại m2x. Giữ tên gốc:
```python
s = pd.Series(['Loft 46.5 m2','Studio 32,5 m²','80 M2','30m2x','Torre 2024'],
              index=['A','B','C','D','E'], dtype=object)
```
Viết mẫu/cách chuyển số. Cho kết quả, một ca khớp và một ca gần đúng không khớp.

### B7-040

Mỗi mã một listing đã biết danh sách:
```python
ds = pd.Series([['Wifi'],[],['TV','Wifi'],[]], index=['A','B','C','D'], dtype=object)
e = ds.explode()
```
(a) Nêu số hàng e và e.dropna(), các mã placeholder.
(b) Với object, e.eq('Wifi').mean() chia cho bao nhiêu? Nếu dropna trước thì chia bao nhiêu?
(c) Viết tỷ lệ listing có đúng Wifi và giải thích vì sao hai mẫu số trên không thay được số listing.

### Độ bao phủ sau đợt 4

Đã dùng 42/72 mục tiêu. Còn: K09, K10, K12, K20, K22, K30, K35, K36, K50, K51, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 5 — phần A

### B7-041

Python re:
```python
a = re.findall(r'[0-9]+', 'A02 B3')
b = re.sub(r'\s+', ' ', 'A   B\tC')
```
Nhận định nào đúng?

A. a=[2,3] là list số; b='A B C'.

B. a=['02'] vì findall chỉ tìm lần đầu; b='A B C'.

C. a=['02','3'] là list các chuỗi; b='A B C' là str.

D. a=['02','3']; b='ABC'.

### B7-042

Không tự strip hoặc bỏ dấu câu:
```python
s = pd.Series(['wifi;TV','wifi!;Kitchen','wi-fi;TV','TV'], dtype=object)
t = s.str.split(';',regex=False).str.join('|').str.lower()
a = t.str.startswith('wifi',na=False)
b = t.str.endswith('tv',na=False)
```
Các chỉ mục True của a,b là gì?

A. [0] và [0,2,3]

B. [0,1,2] và [0,2,3]

C. [0,1] và [0,2,3]

D. [0,1] và [0,2]

### B7-043

Bốn listing đã biết danh sách: A=['Wifi','Wifi'], B=[], C=['Pocket wifi'], D=['TV']. Không gộp nhãn mở rộng. Code tạo một bool mỗi listing bằng 'Wifi' in xs rồi mean. Kết quả là gì?

A. 2/4

B. 1/3

C. 1/4

D. 2/5

### B7-044

Kiểm toàn giá không âm, $ bắt buộc, phần nguyên ASCII, có thể viết liền hoặc ngăn nghìn đúng ba số; phần thập phân nếu có đúng hai số. Được strip hai đầu. Các chuỗi: 0=' $0.00 ',1='$-5.00',2='$25.5',3='$25'. Chỉ mục hợp lệ là gì?

A. [0,1,3]

B. [0,2,3]

C. [0,3]

D. [3]

### B7-045

```python
s = pd.Series(['code 007','no code','12',''], dtype=object)
x = s.str.extract(r'[0-9]+', expand=False)
```
Điều gì xảy ra?

A. Trả Series 007,thiếu,12,thiếu.

B. Trả list [7,12] và bỏ các hàng không khớp.

C. ValueError vì mẫu extract không có nhóm bắt; thêm ([0-9]+) nếu cần trích dãy số.

D. Trả cả bốn chuỗi nguồn không đổi.

### B7-046

Python re, flags=0, không MULTILINE; text có đúng một newline cuối:
```python
text = 'P7\n'
a = re.search(r'^P[0-9]+$',text)
b = re.fullmatch(r'P[0-9]+',text)
print(a is not None,b is not None)
```
In gì?

A. True,False

B. True,True

C. False,False

D. False,True

### B7-047

USD/đêm; cho phép strip hai đầu, giá không âm, định dạng như p. None thiếu nguồn:
```python
raw = pd.Series(['$-10',' $0.00 ','$1,20.00',None,'$30'], dtype=object)
p = r'\$(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)(?:\.[0-9]{2})?'
```
Người học bỏ $ và phẩy rồi chuyển số, thấy -10 và 120 nên coi hai chuỗi đầu/nhóm nghìn đều hợp lệ. Sửa pipeline để chỉ chuyển các chuỗi đúng toàn định dạng; nêu kết quả, hàng lỗi khác thiếu nguồn, và vì sao không fillna(0).

### B7-048

Mỗi mã một listing, [] biết rỗng và None chưa biết; chỉ đúng nhãn Wifi, không chuẩn hoá thêm:
```python
ds = pd.Series([['Wifi','Wifi'],[],None,['TV'],['Wifi']], index=['A','B','C','D','E'], dtype=object)
```
(a) Tính tỷ lệ có Wifi trong nhóm đã biết danh sách.
(b) Nếu người báo cáo dùng mọi listing làm mẫu số và ghi “tỷ lệ listing quan sát được liệt kê Wifi”, tính bao nhiêu? Vì sao không gọi nó là tỷ lệ thật sự có Wifi của toàn bộ?
(c) Viết code và nêu một kiểm chứng phát hiện việc bỏ [] hoặc đếm lặp.

### B7-049

Python re qua object:
```python
s = pd.Series(['near the Central Park','cerca de todo','cerca del Museo Norte','No metro nearby'], dtype=object)
p = r'\b(?:cerca de(?: la|l)?|near(?: the)?)\s+(\w+)'
x = s.str.extract(p,flags=re.I,expand=False)
```
Cho x. Một người đặt tên cột dia_diem, suy mọi listing khớp đều gần đúng địa điểm đó, và mọi câu có wifi|internet đều hài lòng. Chỉ ra giới hạn; đề xuất tên cột và cách kiểm chứng phù hợp.

### B7-050

Python re qua object, số nguyên không dấu:
```python
s = pd.Series(['1BR main; 2BR annex','Studio','3 bedrooms'], index=['A','B','C'], dtype=object)
p = r'\b([0-9]+)\s*(?:BR|bedrooms?)\b'
a = s.str.extract(p,flags=re.I,expand=False)
b = s.str.extractall(p,flags=re.I)
```
Cho a, số hàng/cột và các cặp (nhãn gốc,lần khớp) của b. Không cần thuộc thao tác MultiIndex khác. Có thể dùng len(b) làm số listing có phòng không?

### Độ bao phủ sau đợt 5

Đã dùng 47/72 mục tiêu. Còn: K09, K20, K35, K50, K51, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 6 — phần A

### B7-051

Python re, ASCII trong chuỗi đã cho:
```python
x = re.findall(r'[^0-9]+','ab12_3')
print(x)
```
In gì?

A. ['12','3']

B. ['a','b','_']

C. ['ab12_3']

D. ['ab','_']

### B7-052

Mỗi mã một listing; [] biết rỗng, None chưa biết; danh sách [''] chứa một mục chuỗi rỗng thật:
```python
ds = pd.Series([[],[''],None,['Wifi']], index=['A','B','C','D'], dtype=object)
m = ds.explode().dropna()
```
Giá trị/index m là gì?

A. Chỉ D→'Wifi'

B. B→'',D→'Wifi'

C. A→'',B→'',D→'Wifi'

D. B→'',C→[],D→'Wifi'

### B7-053

pandas 3; giá trị chỉ ASCII/None:
```python
a = pd.Series(['wifi',None,'TV'],dtype='string').str.contains('wifi')
b = pd.Series(['wifi',None,'TV'],dtype='str').str.contains('wifi')
c = pd.Series(['wifi',None,'TV'],dtype=object).str.contains('wifi',na=False)
```
Nhận định nào đúng cho vị trí 1?

A. Cả ba đều thiếu vì mọi dtype chuỗi có cùng mặc định NA.

B. Cả ba False nên chứng minh listing thiếu tên không có Wifi.

C. a thiếu, b False, c False; thêm na=False là quy ước lọc, không là bằng chứng listing không có Wifi.

D. a thiếu,b thiếu,c True vì None là chuỗi chứa wifi.

### B7-054

Dấu ; là dấu tách của nguồn, không phải JSON. Không thiếu dữ liệu:
```python
s = pd.Series(['Wifi;TV','Kitchen',';TV',''], index=['A','B','C','D'], dtype=object)
t = s.str.split(';',regex=False,expand=True)
```
Kiểu, shape và hàng C của t là gì?

A. Series,(4,),['','TV'] trong một ô

B. DataFrame,(4,2),['','TV']

C. DataFrame,(3,2),['','TV']

D. DataFrame,(4,2),['TV',thiếu]

### B7-055

Python re mặc định Unicode, flags=0. Đề cho các ký tự ١٢ là chữ số Arabic-Indic; không cần thuộc bảng Unicode:
```python
a = re.fullmatch(r'\d+','١٢') is not None
b = re.fullmatch(r'[0-9]+','١٢') is not None
c = re.fullmatch(r'\w+','Ñ_2') is not None
```
(a,b,c) là gì?

A. (False,False,False)

B. (True,True,True)

C. (True,False,True)

D. (True,False,False)

### B7-056

Một phép thay chuỗi được đo sau khi đã đối chiếu kết quả. Ở backend X, .str nhanh hơn apply; ở object, apply nhanh hơn .str. Công việc và phần đo như nhau. Kết luận nào phù hợp?

A. Kết quả object chắc sai vì .str luôn vector hóa nên luôn nhanh hơn.

B. apply luôn nhanh hơn vì chỉ cần nhìn hàng object.

C. Chuyển dtype ngay trong phần đo chỉ cho .str sẽ làm so sánh công bằng hơn.

D. Hiệu năng phụ thuộc cách lưu chuỗi và thao tác; chọn trên dữ liệu/cấu hình thực tế, không suy mọi .str hay apply luôn thắng.

### B7-057

Chuỗi Python qua object; cho biết lower của Straße là straße, casefold của Straße là strasse:
```python
s = pd.Series(['Straße','STRASSE','Café','Cafe'], index=[3,8,2,6], dtype=object)
```
Viết hai Series lower và casefold; cho kết quả, số nhãn khác nhau và index. Có thể suy casefold tự xóa dấu café để gộp cafe không? Có sửa s gốc không?

### B7-058

Mỗi hàng một listing, USD/đêm; các giá không thiếu đều hợp lệ theo nguồn: $ ở đầu, phẩy nghìn, chấm thập phân. None chưa biết:
```python
d = pd.DataFrame({'loai':[' Home ','HOME','home','Room',' room ','ROOM'],
                 'raw':['$100','$300',None,'$20','$1,000','$40']})
```
(a) Giữ raw, chuẩn hoá loại bằng strip+lower, chuyển giá rồi tính median mỗi loại.
(b) Vì sao mean hoặc fillna(0) không thay được yêu cầu?
(c) Cho tập giá/mẫu số, kết quả và một kiểm chứng truy nguyên.

### B7-059

Mỗi hàng một review. Quy tắc chỉ thay đúng chuỗi <br/> bằng một dấu cách, không sửa <br>, <BR/>, thẻ khác hoặc khoảng trắng còn lại:
```python
s = pd.Series(['A<br/>B<br/>C','<br> X','<BR/>Y','<b>Z</b>'],index=[4,9,2,7],dtype=object)
```
Viết cách thay đúng và số review bị tác động. Cho kết quả, số lần thay, tổng độ dài giảm bao nhiêu. Vì sao thay bằng regex không phân biệt hoa thường hoặc gọi đây là làm sạch mọi HTML đều quá quy tắc?

### B7-060

Câu đọc thêm với cấu hình kiểm chứng pandas 3.0.1, PyArrow 25.0.1, Python re (khác pandas 3.0.3 nguồn). Đã ghim storage, không suy từ tên dtype chung:
```python
ar = pd.Series(['Studio 30m²'],dtype=pd.StringDtype('pyarrow',na_value=np.nan))
py = pd.Series(['Studio 30m²'],dtype=pd.StringDtype('python',na_value=np.nan))
a = ar.str.contains(r'[0-9]+m²\b')
b = ar.str.extract(r'([0-9]+m²)\b',expand=False)
c = py.str.contains(r'[0-9]+m²\b')
```
Ca kiểm chứng cho a=[False], b=['30m²'], c=[True]. Với Ñuñoa, str.count(`r'\w'`) cho [3] trên storage pyarrow và [5] trên storage python ở cấu hình này.
(a) Giải thích vì sao cùng mẫu gần giống nhau có thể khác kết quả.
(b) Có thể kết luận mọi Python re coi ²/Ñ không là ký tự từ, hoặc mọi pandas backend giống nhau không?
(c) Nêu cách kiểm trước khi dùng quy tắc chứa \b/\w trên nguồn ngoài ASCII.

### Độ bao phủ sau đợt 6

Đã dùng 52/72 mục tiêu. Còn: K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 7 — luyện regex bổ sung

### B7-R01

Hàm phải trả dãy chữ số ASCII đầu tiên dạng str giữ số 0 đầu; không có hoặc text=None trả None. Không strip/lower. Điền dòng return:
```python
def lay_ma(text):
    if text is None: return None
    m = re.search(r'[0-9]+',text)
    # return ...
```
Dòng nào đúng toàn quy tắc? Ví dụ 'A000 B7' phải cho '000', không là 0.

A. `return int(m.group(0)) if m is not None else None`

B. `return m.group(1) if m is not None else None`

C. `return m.group(0) if m is not None else None`

D. `return re.findall(r'[0-9]+',text)`

### B7-R02

Python re, flags=0, fullmatch. Cần đúng ba ký tự bất kỳ trừ \n rồi một dấu chấm thật; giữ khoảng trắng/hoa thường. None trả False ngoài bước regex. Mẫu nào đúng với mọi đầu vào trong miền này, gồm cả '  A.' và '?=+.'?

A. `r'.{4}'`

B. `r'[A-Za-z0-9]{3}\.'`

C. `r'.{3}\.?'`

D. `r'.{3}\.'`

### B7-R03

Chỉ các từ can,man,fan hợp lệ (một chữ trong c,m,f rồi an), phân biệt hoa thường, không strip. Người học fullmatch mẫu `r'c|m|fan'`. Đầu vào nào dưới đây chứng minh mẫu cho kết quả sai quy tắc?

A. can

B. fan

C. ran

D. pan

### B7-R04

Mã có đúng ba ký tự: A–C hoa, n–p thường, a–c thường. Không strip/lower, None→False, hàm trả bool. Pattern `r'[A-C][n-p][a-c]'` đã đúng, nhưng code dùng re.search(PATTERN,text.strip()).
Sửa hàm tối đa bốn dòng. Cho kết quả với ' Apa','Boc','Dna','AnaX',None và giải thích vì sao chỉ đổi search thành fullmatch mà vẫn strip chưa đủ.

### B7-R05

Quy tắc wa + từ ba đến năm z + up, phân biệt hoa thường, không khoảng trắng. Python re, flags=0:
```python
p = r'waz{3,5}up'
xs = ['wazzup','wazzzup','wazzzzzup','wazzzzzzup']
print([re.fullmatch(p,x) is not None for x in xs])
```
Kết quả nào đúng?

A. [False,True,True,False]

B. [True,True,True,True]

C. [False,True,False,False]

D. [False,False,True,True]

### B7-R06

Toàn chuỗi phải có ít nhất hai a, sau đó không hoặc nhiều b, cuối cùng ít nhất một c; không giới hạn trên. Không strip/lower, None→False. Mẫu hiện tại `r'a+b+c*'` sai. Sửa pattern và hàm bool ngắn; cho một ca bị bỏ sót, một ca nhận nhầm của mẫu cũ, giải thích từng lượng từ mới.

### B7-R07

Quy tắc: số nguyên dương ASCII không 0 đầu, một dấu cách, file hoặc files (đều được phép với mọi số), một dấu cách, đúng found?. Không strip/lower. Python re fullmatch:
```python
p = r'[1-9][0-9]* files? found\?'
xs = ['01 file found?','2 file found?','1 files found?','1 file found']
```
Mask hợp lệ là gì?

A. [False,False,False,False]

B. [True,True,True,False]

C. [False,True,True,False]

D. [False,True,True,True]

### B7-R08

Mục hợp lệ gồm chữ số ASCII+, chấm thật, ít nhất một ký tự trắng theo \s Python, rồi abc. Không strip/lower, None→False; cho biết \s gồm dấu cách/tab/newline. Mẫu cũ `r'[0-9]+\.\s*abc'`. Sửa đúng một ký hiệu, viết hàm bool và cho kết quả '7.abc','7.\tabc','7.\nabc','7. abc ',None.

### B7-R09

Chỉ tên file, không đường dẫn. Tên bắt đầu file, tiếp ít nhất một chữ/số/_ ASCII, kết thúc .pdf chữ thường; không strip/lower. None/không hợp lệ→None. Trong hàm đã có:
```python
if text is None: return None
m = re.fullmatch(r'(file([A-Za-z0-9_]+))\.pdf',text)
```
Để trả toàn phần tên trước .pdf, dòng return nào đúng? Với fileB_08.pdf cần fileB_08.

A. `return m.group(0) if m is not None else None`

B. `return m.group(1) if m is not None else None`

C. `return m.group(2) if m is not None else None`

D. `return m.groups() if m is not None else None`

### B7-R10

Chỉ số nguyên ASCII không dấu, không âm/thập phân. Hàm cần trả số chuỗi ở cụm đầu tiên số + khoảng trắng tùy ý + BR/bedroom/bedrooms, re.I, ranh giới hai đầu. None/không khớp→None. Một người dùng p=`r'\b([0-9]+)\s*BR|bedrooms?\b'` rồi m.group(1).
Sửa p/hàm và nêu kết quả cho 'bedrooms only','A 0BR','Modern 2BR2BA','Home 2 bedroom'. Giải thích vì sao sửa | chưa có nghĩa đã nhận được mọi cách viết số phòng ngoài thực tế.

### Độ bao phủ sau đợt 7

Đã dùng 62/72 mục tiêu. Còn: K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 8 — luyện regex bổ sung

### B7-R11

Chỉ số nguyên hoặc thập phân dấu chấm; có thể trừ đầu, cho 0 đầu. Không cộng, phẩy, số mũ hay khoảng trắng. Phần nguyên ASCII ít nhất một số; có chấm thì sau chấm phải có số. None→False. Dùng fullmatch:
```python
p = r'-?[0-9]+(?:\.[0-9]+)?'
xs = ['-00.25','12.','+8','.25']
```
Chỉ mục hợp lệ là gì?

A. [0,1]

B. [0,2]

C. [0]

D. [0,3]

### B7-R12

Số ASCII: dấu + hoặc - đầu tùy chọn; phần nguyên viết liền hoặc nhóm đầu 1–3 số rồi các nhóm phẩy đúng ba số; thập phân tùy chọn có chấm và ít nhất một số; số mũ tùy chọn e/E, dấu tùy chọn và ít nhất một số. Cho 0 đầu, không khoảng trắng; None→False.
Khung: p=`r'[+-]?'`+I+`r'(?:\.[0-9]+)?'`+E. Hai mảnh cũ I=`r'[0-9,]+'` và E=`r'(?:[eE][+-]?[0-9]*)?'` nhận quá rộng. Sửa I,E và hàm bool; nêu kết quả với '12,345e-2','12,34e2','1E+','+001.5',None.

### B7-R13

Điện thoại giản lược: quốc gia 1 tùy chọn; mã vùng ba số ASCII, cụm ba số, cụm bốn số. Giữa các phần vắng phân cách hoặc đúng một dấu cách/gạch ngang; không khoảng trắng ngoài chuỗi, không dấu cộng. Ngoặc vùng hoặc đủ cặp, hoặc không có. Fullmatch khung:
```python
p = r'(?:1[ -]?)?' + AREA + r'[ -]?[0-9]{3}[ -]?[0-9]{4}'
```
Mảnh AREA nào đúng, có nhóm để trích mã vùng?

A. `r'\(?([0-9]{3})\)?'`

B. `r'\(([0-9]{3})\)'`

C. `r'([0-9]{3})'`

D. `r'(?:\(([0-9]{3})\)|([0-9]{3}))'`

### B7-R14

Email giản lược, không strip/lower. Tên gốc gồm các nhóm chữ/số/_ ASCII ngăn bằng một chấm; filter tùy chọn + và một nhóm chữ/số/_. Miền ít nhất hai nhãn: nhãn trước cuối có các nhóm chữ/số ngăn gạch ngang, nhãn cuối từ hai chữ ASCII. Các mảnh đúng đã cho:
```python
BASE = r'[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*'
FILTER = r'(?:\+[A-Za-z0-9_]+)?'
DOMAIN = r'(?:[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*\.)+[A-Za-z]{2,}'
```
Một bạn đặt nhóm bắt bao cả BASE+FILTER nên lấy thừa filter. Viết p và hàm chỉ trả tên gốc, None/sai→None. Cho kết quả 'Lan.01+lab@data-site.edu.vn','a..b@site.vn','a+@site.vn',None. Regex có xác minh email tồn tại không?

### B7-R15

HTML giản lược một dòng: tên thẻ bắt đầu chữ ASCII, sau là chữ/số/gạch ngang; thuộc tính ngăn bằng ký tự trắng và không chứa < hoặc >. Chú thích đủ cặp, không lồng nhau. Thẻ tự đóng tính là thẻ mở; bỏ thẻ đóng. Không kiểm HTML tổng quát. Hàm đã bỏ toàn bộ chú thích rồi search:
```python
p = r'<([A-Za-z][A-Za-z0-9-]*)(?:\s+[^<>]*)?/?>'
text = '<!-- <H1>an</H1> --></p><my-card/><div>hien</div>'
```
Tên thẻ mở đầu tiên ngoài chú thích, giữ hoa thường, là gì? None nếu không có.

A. my-card

B. H1

C. p

D. div

### B7-R16

Tên ảnh: nhóm chữ/số/_ ASCII, các nhóm ngăn một chấm hoặc gạch ngang; mở rộng jpg/png/gif chữ thường, không đường dẫn/dấu cách/chấm đầu. Không strip/lower, sai/None→None. Hàm dùng fullmatch rồi m.groups() để trả (tên,mở_rộng), nhưng mẫu đang là:
```python
p = r'([A-Za-z0-9_]+([.-][A-Za-z0-9_]+)*)\.(jpg|png|gif)'
```
Sửa phần nhóm thừa, hoàn thiện hàm. Cho 'scene.02-night.png','a..jpg','a.JPG',None; giải thích vì sao .jpg.tmp không được nhận.

### B7-R17

Chỉ bỏ dấu cách ASCII/tab hai đầu, giữ mọi khoảng trắng bên trong và giữ NBSP (\u00a0), tab dọc/chuyển trang. Đầu vào không có \n/\r; None→None; toàn dấu cách/tab→chuỗi rỗng hợp lệ. Không lower. Mẫu cũ `r'\s*(.*)\s*'` vừa quá rộng vừa tham lam.
(a) Viết mẫu/hàm regex đúng với fullmatch.
(b) Cho đầu vào '  A  B\t',' \t','',None,'\u00a0X\u00a0'.
(c) Bộ gom kết quả dùng if result: sẽ mất gì? Sửa điều kiện để giữ chuỗi rỗng hợp lệ.

### B7-R18

Log giản lược: cụm at rồi các thành phần gói/lớp/phương thức ASCII (đầu chữ/_), tệp chữ/số/_ với .java, dòng số ASCII không dấu. Tìm cụm hợp lệ đầu tiên, None/không có→None. Đã có pattern:
```python
p = r'\bat\s+(?:[A-Za-z_][A-Za-z0-9_]*\.)+([A-Za-z_][A-Za-z0-9_]*)\(([A-Za-z0-9_]+\.java):([0-9]+)\)'
text = 'E: at pkg.Thing.run(Main.java:007) at pkg.Thing.stop(Main.java:8)'
m = re.search(p,text)
r = (m.group(1),m.group(2),int(m.group(3)))
```
r là gì?

A. ('run','Main.java','007')

B. ('run','Main.java',7)

C. ('stop','Main.java',8)

D. ('pkg.Thing.run','Main.java',7)

### B7-R19

URL giản lược: giao thức đầu chữ ASCII rồi chữ/số/+./-, máy chủ các nhóm chữ/số/_/- ngăn chấm; cổng tùy chọn ASCII, giữ chuỗi, không kiểm miền giá trị. Phần sau nếu có bắt đầu /, không trắng. Không userinfo/IPv6, không strip/lower; sai/None→None. Fullmatch rồi groups():
```python
p = r'([A-Za-z][A-Za-z0-9+.-]*)://([A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*)(?::([0-9]+))?(?:/[^\s]*)?'
text = 'Git+ssh://my_host.test:0022/a%20b'
```
Ba trường trả về là gì?

A. ('git+ssh','my_host.test','0022')

B. ('Git+ssh','my_host.test',22)

C. ('Git+ssh','my_host.test/a%20b','0022')

D. ('Git+ssh','my_host.test','0022')

### B7-R20

URL giản lược chỉ http/https chữ thường; host ASCII như mẫu, cổng số nếu có; không tài khoản/IPv6/trắng. Path bắt đầu /, dừng trước ? hoặc #, giữ nguyên %20; thiếu path trả '/'; sai/None→None. Hàm dùng fullmatch p rồi m.group(1) or '/' nếu có m:
```python
p = r'https?://[A-Za-z0-9_-]+(?:\.[A-Za-z0-9_-]+)*(?::[0-9]+)?(/[^?#\s]*)?(?:\?[^#\s]*)?(?:#[^\s]*)?'
xs = ['http://host/a%20b?q=1#p','https://host?x=2','ftp://host/a',None]
```
Danh sách kết quả là gì?

A. ['/a b','/',None,None]

B. ['/a%20b','/',None,None]

C. ['/a%20b?q=1#p','/',None,None]

D. ['/a%20b','',None,None]

### Độ bao phủ sau đợt 8

Đã dùng 72/72 mục tiêu. Không còn mục tiêu thiếu trong phạm vi đã xác định.

## Kiểm kê cuối bộ

- Đủ B7-001–B7-060: **60=40 TN+20 TL**, nhóm **10/10/20/14/6**, mức thiết kế **15/33/12**.
- Đủ B7-R01–B7-R20: **20=12 TN+8 TL**, tám đợt mỗi đợt mười câu.
- **72/72 mục tiêu** dùng để trả lời; đủ **20/20 dạng RX**. Câu tự luận ba phần gần cấu trúc GK câu 25 gồm 008,010,020,048 (và các biến thể khác).
- Đã rà câu trùng, giữ cặp đối chiếu có thay cơ chế/đơn vị hoặc quy tắc. Không dùng số khớp làm độ chính xác hay test hữu hạn làm chứng minh mọi đầu vào.
- **76/80 câu** đã thực thi ca kiểm chứng; **4 câu** đánh giá cơ chế/diễn giải kiểm bằng suy luận, ghi rõ từng câu. Không chạy toàn notebook TODO, không đo lại benchmark máy giảng viên, không tải dữ liệu thật.
- Phân biệt bài chính, tự học trong NB/LAB và luyện bổ sung RX. Độ bao phủ tài liệu không là tần suất thi hay dự báo chắc chắn đề thật.
