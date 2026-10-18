# BÀI 7 — ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM

Đi cùng [file câu hỏi](<D:/LTXLDL_GK/output/bai7/Bai7_80_cau_hoi.md>).

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

## Cách đọc

Đáp án giải thích đủ bốn lựa chọn, phần TL có tiêu chí điểm. Kxx tra ở danh mục câu hỏi. Mục tự học trong A vẫn ghi rõ nguồn/ưu tiên ở đây; không hiểu mọi API ở bảng tra có cùng ưu tiên với bài tập chính.

## Đợt 1 — phần A

### B7-001

**Đáp án: A.**

- A đúng: strip chỉ hai đầu; lower không gộp hai dấu cách giữa; thao tác trả kết quả mới.
- B sai: nhầm strip với xóa khoảng trắng ở mọi vị trí.
- C sai: Series không có strip trực tiếp như str Python.
- D sai: .str giữ nhãn và trả kết quả mới.

**Đối chiếu:** nhóm 1; K01, K02; mức Nền tảng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Chuỗi Python có strip; Series dùng accessor .str, không có strip trực tiếp; strip chỉ hai đầu; lower trả kết quả mới giữ index và bản gốc; không xóa khoảng trắng giữa. **Nguồn đọc lại:** NB ô 4–13; LAB ô 6.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-002

**Đáp án: B.**

- A sai: tưởng hai tầng xử lý escape cho cùng kết quả.
- B đúng: chuỗi thô chuyển backslash-b tới regex làm ranh giới; chuỗi thường đã biến mỗi backslash-b thành backspace.
- C sai: đảo vai trò raw và chuỗi thường.
- D sai: cho rằng raw làm ranh giới thành văn bản hai ký tự cần có trong text.

**Đối chiếu:** nhóm 3; K21, K25; mức Nền tảng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Hai tầng escape Python/regex; r"\b" khác backspace "\b"; raw giữ backslash; \b là ranh giới ký tự từ, không là dấu cách; số và _ cũng là ký tự từ. **Nguồn đọc lại:** NB ô 45–51.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-003

**Đáp án: A.**

- A đúng: replace mặc định regex=False tìm nguyên văn [$,], không bỏ $ hay phẩy; ba chuỗi có dữ liệu đều không chuyển được.
- B sai: ngầm coi [$,] là lớp regex dù thiếu regex=True.
- C sai: đếm cả None từ nguồn là lỗi chuyển đổi.
- D sai: tưởng coerce sửa mọi văn bản thành giá hợp lệ.

**Đối chiếu:** nhóm 2; K14, K16; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** pandas 3 str.replace mặc định regex=False; [$,] cần regex=True; to_numeric coerce; lỗi raw.notna & parsed.isna khác thiếu từ nguồn, kể cả chuỗi rỗng có dữ liệu. **Nguồn đọc lại:** BG §1; LAB ô 9–10.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-004

**Đáp án: A.**

- A đúng: JSON có hai mục; dấu phẩy trong chuỗi tên không tách mục.
- B sai: cắt JSON theo mọi phẩy, làm vỡ Stove, gas.
- C sai: bỏ việc giải mã thành list.
- D sai: đảo thứ tự mục nguồn.

**Đối chiếu:** nhóm 4; K37; mức Nền tảng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** JSON string → json.loads → list; tên có dấu phẩy vẫn một mục, không split JSON theo phẩy. **Nguồn đọc lại:** NB ô 68–75; LAB ô 31–32.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-005

**Đáp án: D.**

- A sai: coi nhóm đơn vị không bắt hoặc expand=False luôn cho Series.
- B sai: nhầm cả đoạn khớp với các nhóm trả về.
- C sai: tưởng extract tự bỏ hàng Studio không khớp.
- D đúng: cả số và đơn vị đều có nhóm bắt; expand=False không ép nhiều nhóm thành Series.

**Đối chiếu:** nhóm 3; K24, K28; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Nhóm bắt và không bắt; nhóm thừa đổi phần dữ liệu/shape được trả; expand=False một nhóm → Series; nhiều nhóm → DataFrame; extract không nhóm bắt gây lỗi. **Nguồn đọc lại:** NB ô 45,63.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-006

**Đáp án: B.**

- A sai: tự nhập wifi!/wi-fi vào wifi ngoài quy tắc.
- B đúng: hai nhãn đầu thành wifi; wifi!,wi-fi,café,cafe vẫn khác nhau.
- C sai: tự xóa dấu để nhập café với cafe.
- D sai: không tính hai nhãn đầu đã gộp.

**Đối chiếu:** nhóm 1; K02, K03; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** strip chỉ hai đầu; lower trả kết quả mới giữ index và bản gốc; không xóa khoảng trắng giữa; Không tự gộp khác dấu, dấu câu, chính tả; wifi/wifi!/wi-fi cần quy tắc riêng. **Nguồn đọc lại:** NB ô 7–13; LAB ô 6–7.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-007

**Đáp án: A.**

- A đúng: ranh giới có thể giảm khớp nhầm đồng thời tăng bỏ sót.
- B sai: đồng nhất số khớp với độ chính xác.
- C sai: sửa một lỗi không chứng minh hết lỗi khác.
- D sai: 2BR2BA có thể là cách viết thật bị ranh giới loại.

**Đối chiếu:** nhóm 5; K48, K32; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Số khớp không là độ chính xác; kiểm dương/âm/gần đúng và nguyên văn, test hữu hạn không là chứng minh mọi đầu vào; BR/bedroom(s), re.I, \s*, ranh giới: giảm bravo nhưng bỏ 2BR2BA; không khớp không suy không phòng. **Nguồn đọc lại:** NB ô 64–65,98–100.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu đánh giá cơ chế/thiết kế hoặc diễn giải dữ kiện cho sẵn).

### B7-008

```python
clean = raw.str.strip().str.replace(r'[$,]', '', regex=True)
parsed = pd.to_numeric(clean, errors='coerce')
loi = raw.notna() & parsed.isna()
```
A=2000,B/C/D=thiếu,E=0; lỗi C,D, thiếu nguồn chỉ B. Giữ index A–E và raw để truy nguyên. fillna(0) làm B,C,D lẫn E dù E là giá 0 hợp lệ; chưa có quy tắc coi chưa biết/lỗi là miễn phí. Chuyển đổi này chưa kiểm mọi cách viết phân cách nghìn.

**Hướng dẫn chấm:** 3 điểm: pipeline/giữ raw 1; loi phân biệt nguồn/lỗi 1; kết quả, E=0 và không điền 0 1. Nhận hai replace nguyên văn tương đương.

**Đối chiếu:** nhóm 2; K15, K16, K17; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Bỏ ký hiệu tiền/phân cách theo quy ước nguồn; dấu phẩy nghìn khác dấu phẩy thập phân; to_numeric coerce; lỗi raw.notna & parsed.isna khác thiếu từ nguồn, kể cả chuỗi rỗng có dữ liệu; Giữ giá gốc; chưa biết khác 0, không fillna(0) tùy ý. **Nguồn đọc lại:** NB ô 21–24,32–39; LAB ô 9–10; GK câu 18.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-009

20→'3',50→'5', đều chuỗi trong Series x cùng năm nhãn. Nhãn 10: sau BR là _ cũng là ký tự từ; 30: sau BR là số 2; 40: trước 4 là chữ x. Các vị trí đó không có ranh giới từ. Không khớp chỉ nói quy tắc chưa lấy được số, không chứng minh 0 phòng.

**Hướng dẫn chấm:** 2 điểm: nhãn/giá trị/kiểu/index 0,75; ba lý do 0,75; không suy 0 0,5.

**Đối chiếu:** nhóm 3; K25, K27, K32; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** \b là ranh giới ký tự từ, không là dấu cách; số và _ cũng là ký tự từ; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0; BR/bedroom(s), re.I, \s*, ranh giới: giảm bravo nhưng bỏ 2BR2BA; không khớp không suy không phòng. **Nguồn đọc lại:** NB ô 47–54,98–100.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-010

```python
ds = raw.dropna().map(json.loads)
co = ds.map(lambda xs: any(x.strip().lower()=='wifi' for x in xs))
ty_le = co.mean()
```
A,E có wifi: 2/4=0.5; B rỗng vẫn trong mẫu số, C chưa biết bị loại theo quy ước. Sau dropna có 4 mục thật, 3 là wifi do A lặp: 3/4 khác tỷ lệ listing. Trước dropna, [] tạo placeholder cho B: 5 hàng; eq('wifi') trên object cho placeholder False nên mean=3/5. Không lấy số mục thay số listing.

**Hướng dẫn chấm:** 3 điểm: JSON/None theo mẫu số 1; một bool mỗi listing, chuẩn hoá/không đếm lặp 1; 2/4,3/4,3/5 và ý nghĩa 1. Nhận explode+nunique rồi chia len(ds).

**Đối chiếu:** nhóm 4; K42, K43, K44; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Tỷ lệ listing có tiện nghi khác tỷ lệ mục tiện nghi; một bool mỗi listing và mẫu số đúng; Danh sách biết rỗng vẫn thuộc mẫu số listing; không dùng số hàng exploded thay thế; None chưa biết; phải nêu mẫu số toàn bộ hay nhóm đã biết, không trộn [] với None. **Nguồn đọc lại:** NB ô 82–88; LAB ô 33–36; GK câu 25.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### Độ bao phủ sau đợt 1

Đã dùng 18/72 mục tiêu. Còn: K04, K05, K06, K07, K08, K09, K10, K11, K12, K13, K18, K19, K20, K22, K23, K26, K29, K30, K31, K33, K34, K35, K36, K38, K39, K40, K41, K45, K46, K47, K49, K50, K51, K52, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 2 — phần A

### B7-011

**Đáp án: B.**

- A sai: nhầm dropna với lọc mọi chuỗi không có ký tự.
- B đúng: strip biến B thành rỗng; dropna chỉ loại C thiếu. Độ dài hai ký tự là số đo khảo sát, không tự chứng minh nội dung vô ích.
- C sai: bỏ qua strip đã xóa ba dấu cách của B.
- D sai: coi None tự thành chuỗi rỗng và không bị dropna loại.

**Đối chiếu:** nhóm 1; K04, K11; mức Nền tảng. **Ưu tiên:** Trọng tâm; Trọng tâm (len trong LAB); slice tự học bảng tra.

**Kiến thức/bẫy:** Chuỗi rỗng, toàn khoảng trắng, thiếu khác nhau; dropna không loại chuỗi rỗng; str.len/str.slice giữ nhãn; độ dài ngắn không tự là vô ích. **Nguồn đọc lại:** NB ô 79–81; LAB ô 15–18.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-012

**Đáp án: D.**

- A sai: cho rằng to_numeric tự chấp nhận phân cách nghìn bằng phẩy.
- B sai: dùng p.isna mà quên loại thiếu nguồn.
- C sai: coi giá 0 chuyển thành số là lỗi hoặc là thiếu.
- D đúng: chưa bỏ phẩy nên 1,500 thất bại; negotiable thất bại; None không là lỗi, 0 hợp lệ.

**Đối chiếu:** nhóm 2; K15, K16, K14; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Bỏ ký hiệu tiền/phân cách theo quy ước nguồn; dấu phẩy nghìn khác dấu phẩy thập phân; to_numeric coerce; lỗi raw.notna & parsed.isna khác thiếu từ nguồn, kể cả chuỗi rỗng có dữ liệu; pandas 3 str.replace mặc định regex=False; [$,] cần regex=True. **Nguồn đọc lại:** NB ô 23,34–37; GK câu 18 (biến thể truy nguyên).

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-013

**Đáp án: D.**

- A sai: coi match cũng bắt buộc hết chuỗi.
- B sai: coi contains chỉ tìm từ đầu.
- C sai: coi match tìm giữa chuỗi và fullmatch chỉ cần tiền tố.
- D đúng: contains tìm bất kỳ đâu, match từ đầu nhưng chưa hết, fullmatch yêu cầu cả chuỗi.

**Đối chiếu:** nhóm 3; K26; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** contains bất kỳ đâu, match từ đầu, fullmatch cả chuỗi; không nhầm kiểm một đoạn với cả định dạng. **Nguồn đọc lại:** NB ô 55–58,94.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-014

**Đáp án: B.**

- A sai: gán thêm quy tắc không có trong code.
- B đúng: None không phải JSON text; không được tự hiểu chưa biết là danh sách biết rỗng.
- C sai: map không tự dropna trước khi gọi hàm.
- D sai: loads giải mã JSON text, không phải hàm giữ nguyên chuỗi.

**Đối chiếu:** nhóm 4; K38, K37; mức Nền tảng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** json.loads(None) lỗi nếu không xử lý; None chưa biết không tự đổi []; JSON string → json.loads → list; tên có dấu phẩy vẫn một mục, không split JSON theo phẩy. **Nguồn đọc lại:** LAB ô 33–36.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-015

**Đáp án: D.**

- A sai: nhầm extract với mọi lần khớp và tự chuyển kiểu.
- B sai: lấy lần khớp cuối thay đầu.
- C sai: tự thay tên không khớp Studio bằng số phòng 0.
- D đúng: extract lấy lần đầu và trả chuỗi; mã hình thức 01 chưa tự thành int; 0 chỉ có khi trích được rõ.

**Đối chiếu:** nhóm 3; K27, K32; mức Nền tảng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0; BR/bedroom(s), re.I, \s*, ranh giới: giảm bravo nhưng bỏ 2BR2BA; không khớp không suy không phòng. **Nguồn đọc lại:** NB ô 47–54,63.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-016

**Đáp án: A.**

- A đúng: A hai mục, B một placeholder, C một thiếu, D một mục; dropna loại B,C nhưng giữ index A lặp.
- B sai: cho rằng explode tự bỏ [] và None trước khi đếm.
- C sai: coi placeholder của [] không phải thiếu nên được dropna giữ.
- D sai: cho rằng explode/dropna tự đặt lại index liên tục.

**Đối chiếu:** nhóm 4; K39, K40; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** explode mỗi phần tử thành hàng, giữ index lặp; [] tạo placeholder thiếu; dropna sau explode bỏ placeholder/thiếu, không bỏ chuỗi rỗng; phân biệt trước/sau bỏ thiếu. **Nguồn đọc lại:** NB ô 76–81; LAB ô 31–36.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-017

**Đáp án: D.**

- A sai: đồng nhất nhắc từ với cảm xúc tích cực.
- B sai: contains chỉ tìm mẫu ký tự, không tự hiểu phủ định/cảm xúc.
- C sai: đổi đơn vị review thành listing khác nhau và thêm kết luận chất lượng không được xác minh.
- D đúng: từ khóa không phân tích phủ định, cảm xúc hoặc xác minh dịch vụ.

**Đối chiếu:** nhóm 5; K47; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Nhắc metro/wifi không xác minh khoảng cách, hài lòng hay tiện nghi hoạt động tốt; tên cột đúng phép đo. **Nguồn đọc lại:** NB ô 66–67; LAB tự làm 1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-018

m theo index 8,2,9,5 là True,False,True,False; mean=2/4=0.5, gồm hàng thiếu tên.
```python
ty_le_ten_biet = m[s.notna()].mean()
```
Được 2/3. 'metros' cũng chứa đoạn metro; câu nhắc metro có thể phủ định và không cho khoảng cách. None bị mask đặt False chỉ để không chọn hàng, không xác minh listing không gần metro. Có thể đặt cột nhac_metro.

**Hướng dẫn chấm:** 3 điểm: mask/tỷ lệ/mẫu số toàn bộ 1; lọc đúng tên biết và 2/3 1; giới hạn substring/thiếu/ý nghĩa 1.

**Đối chiếu:** nhóm 1; K05, K06, K08; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** contains tìm đoạn con, không xác nhận từ độc lập hay ý nghĩa; case=False và regex=False tìm nguyên văn bỏ hoa thường; na=False không chọn thiếu; na=False có thể vẫn đưa tên thiếu vào mẫu số mean; không chứng minh đối tượng không có thuộc tính. **Nguồn đọc lại:** NB ô 18–20,66–67.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-019

```python
p = r'\b([0-9]+)\s*(?:WC|bathrooms?|baths?)\b'
x = s.str.extract(p, flags=re.I, expand=False)
```
A→'2',B→'3',C/D/E thiếu. Trước 4 ở C là chữ a nên không có ranh giới; D sau bath là _ nên không có ranh giới. E không có số. Nhóm đơn vị không bắt, x là Series cùng index, kết quả số còn là chuỗi.

**Hướng dẫn chấm:** 2 điểm: mẫu/flags/nhóm số 1; năm giá trị 0,5; giải thích C,D và không suy 0 0,5. Nhận cách viết các nhánh tương đương.

**Đối chiếu:** nhóm 3; K33, K25, K27; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** bath/baths/bathroom(s)/WC theo đúng các nhánh đề cho; chữ dính số và ranh giới; \b là ranh giới ký tự từ, không là dấu cách; số và _ cũng là ký tự từ; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0. **Nguồn đọc lại:** GK câu 17; NB ô 45–54.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-020

```python
ds = raw.map(json.loads)
muc = ds.explode().dropna().str.strip().str.lower()
bang = muc.to_frame('nhan').reset_index(names='id')
dem = bang.groupby('nhan')['id'].nunique()
ty_le = dem.get('wifi',0)/len(ds)
```
stove, gas:1; wifi:2; tv:1. Wifi xuất hiện ba lần nhưng chỉ ở A,B. split phẩy làm vỡ tên Stove, gas; value_counts đếm ba mục wifi thay hai listing. Tỷ lệ=2/4=0.5; C rỗng vẫn là listing đã biết và trong mẫu số. get mặc định 0 ở đây là số listing khớp một nhãn không xuất hiện, không biến dữ liệu chưa biết thành biết rỗng.

**Hướng dẫn chấm:** 3 điểm: JSON/chuẩn hoá/nunique 1; hai cơ chế sai 1; kết quả bảng và 2/4 gồm C 1. Nhận membership một bool/listing cho tỷ lệ.

**Đối chiếu:** nhóm 4; K37, K41, K42; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** JSON string → json.loads → list; tên có dấu phẩy vẫn một mục, không split JSON theo phẩy; Chuẩn hoá từng mục rồi nunique id; mục lặp cùng listing không thành nhiều listing; Tỷ lệ listing có tiện nghi khác tỷ lệ mục tiện nghi; một bool mỗi listing và mẫu số đúng. **Nguồn đọc lại:** NB ô 73–88; LAB ô 31–36; GK câu 25.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### Độ bao phủ sau đợt 2

Đã dùng 30/72 mục tiêu. Còn: K07, K09, K10, K12, K13, K18, K19, K20, K22, K23, K29, K30, K31, K34, K35, K36, K45, K46, K49, K50, K51, K52, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 3 — phần A

### B7-021

**Đáp án: B.**

- A sai: tưởng contains mặc định tìm nguyên văn giống replace trong pandas 3.
- B đúng: contains mặc định regex: . cần một ký tự bất kỳ; regex=False chỉ dấu chấm thật.
- C sai: cho rằng . có thể khớp không ký tự nên nhận chuỗi rỗng.
- D sai: bỏ qua na=False, coi thiếu được chọn.

**Đối chiếu:** nhóm 1; K06, K07; mức Nền tảng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** case=False và regex=False tìm nguyên văn bỏ hoa thường; na=False không chọn thiếu; contains mặc định regex; . wildcard, \. chấm thật; raw string không tắt regex. **Nguồn đọc lại:** NB ô 42–44; LAB ô 8.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-022

**Đáp án: C.**

- A sai: áp phần tiền tố của nhánh trái sang nhánh phải dù không có nhóm bao.
- B sai: nhóm bắt đầu tiên chỉ là phần [0-9]+.
- C đúng: thiếu ngoặc giới hạn phạm vi |; có khớp nhưng nhóm 1 không tham gia nhánh đó.
- D sai: nhóm không tham gia là None, không tự sinh số lượng.

**Đối chiếu:** nhóm 3; K23, K29; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Ngoặc giới hạn |; các nhánh thiếu tiền tố có thể khớp sai; re.search: group(0) cả đoạn, group(1) nhóm đầu, groups tuple; thiếu nhóm nhánh là None. **Nguồn đọc lại:** NB ô 45; RX quy ước chung.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-023

**Đáp án: D.**

- A sai: khái quát quy ước Santiago sang nguồn khác.
- B sai: coi hợp kiểu là đúng đơn vị/giá trị.
- C sai: không có quy tắc đổi khác định dạng thành miễn phí.
- D đúng: chuyển được số không chứng minh quy tắc bỏ dấu đúng.

**Đối chiếu:** nhóm 2; K15; mức Nền tảng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Bỏ ký hiệu tiền/phân cách theo quy ước nguồn; dấu phẩy nghìn khác dấu phẩy thập phân. **Nguồn đọc lại:** NB ô 22–24; LAB ô 9–12.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-024

**Đáp án: A.**

- A đúng: cả đoạn khác nhóm số; groups trả tuple các nhóm bắt, vẫn là chuỗi.
- B sai: đánh số nhóm từ 0 như chỉ mục mảng thay group0 cả đoạn.
- C sai: tự ép kiểu số và mất 0 đầu chưa có lệnh chuyển.
- D sai: nhầm chuỗi nguồn với đoạn khớp.

**Đối chiếu:** nhóm 3; K29, K24; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** re.search: group(0) cả đoạn, group(1) nhóm đầu, groups tuple; thiếu nhóm nhánh là None; Nhóm bắt và không bắt; nhóm thừa đổi phần dữ liệu/shape được trả. **Nguồn đọc lại:** NB ô 94; RX quy ước chung.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-025

**Đáp án: B.**

- A sai: dùng substring JSON thô thay membership đúng nhãn.
- B đúng: chỉ listing thứ hai có đúng nhãn wifi; Pocket wifi và wifi! không tự được gộp.
- C sai: tính đúng một listing có wifi nhưng bỏ listing [] khỏi mẫu số.
- D sai: chỉ lấy các mục đúng wifi rồi lấy mean trên bảng đã lọc, làm mất tập listing gốc.

**Đối chiếu:** nhóm 4; K45, K42; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Wifi đúng nhãn khác Pocket wifi/wifi!; tìm substring JSON thô khác membership sau chuẩn hoá; Tỷ lệ listing có tiện nghi khác tỷ lệ mục tiện nghi; một bool mỗi listing và mẫu số đúng. **Nguồn đọc lại:** BG §3; LAB ô 29–36.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-026

**Đáp án: A.**

- A đúng: hàng 0 sai nhóm nghìn, hàng 3 chỉ một chữ số thập phân; 0 được phép.
- B sai: bỏ ký hiệu rồi chuyển được số không kiểm định dạng gốc.
- C sai: cho phép nhóm nghìn có hai chữ số.
- D sai: tự cấm giá 0 dù quy tắc cho phép.

**Đối chiếu:** nhóm 2; K18, K19; mức Vận dụng. **Ưu tiên:** Trọng tâm; Trọng tâm LAB; mẫu ở phần tự học NB.

**Kiến thức/bẫy:** Trích/chuyển được số không chứng minh cả chuỗi đúng định dạng hay phân cách nghìn hợp lệ; fullmatch giá: dấu $, không âm, 0 hợp lệ, nhóm nghìn đúng, thập phân hai chữ số, strip khi được phép. **Nguồn đọc lại:** NB ô 103–104; LAB ô 11–12.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-027

**Đáp án: B.**

- A sai: tưởng raw làm . thành chấm thật.
- B đúng: raw giữ backslash nhưng không vô hiệu .; . cần một ký tự và mặc định không ăn newline.
- C sai: tưởng . cho phép vắng ký tự.
- D sai: ngầm dùng DOTALL dù flags=0.

**Đối chiếu:** nhóm 3; K21, K07, K52; mức Nền tảng. **Ưu tiên:** Trọng tâm; Tự học — ký hiệu mở rộng/quy ước.

**Kiến thức/bẫy:** Hai tầng escape Python/regex; r"\b" khác backspace "\b"; raw giữ backslash; contains mặc định regex; . wildcard, \. chấm thật; raw string không tắt regex; ^/$ và fullmatch khác khi có newline cuối; . mặc định không ăn newline; phải nêu flags/quy ước. **Nguồn đọc lại:** NB ô 44–45,94; RX câu 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-028

```python
m = ds.explode().dropna().str.strip().str.lower()
t = m.to_frame('nhan').reset_index(names='id')
n = t.groupby('nhan')['id'].nunique()
ty_le_tv = n['tv']/len(ds)
```
tv:2 (A,C), wifi:2 (C,D), tỷ lệ TV=2/4. Sau dropna chỉ còn mã A,C,D nên cách sai chia 3 được 2/3; B rỗng là listing đã biết, không được biến mất khỏi mẫu số. A có hai mục tv nhưng chỉ một listing.

**Hướng dẫn chấm:** 3 điểm: chuẩn hoá/nunique gắn id 1; bảng và 2/4 1; sai 2/3, vai trò B/bản gốc và mục lặp 1.

**Đối chiếu:** nhóm 4; K39, K41, K46; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** explode mỗi phần tử thành hàng, giữ index lặp; [] tạo placeholder thiếu; Chuẩn hoá từng mục rồi nunique id; mục lặp cùng listing không thành nhiều listing; Giữ bảng gốc đủ listing để không mất rỗng/thiếu sau explode-dropna; nhãn gắn đúng nguồn. **Nguồn đọc lại:** NB ô 81,87–92; GK câu 25.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-029

Chuẩn bị cùng dữ liệu, cùng cách lưu chuỗi; chuyển dtype ngoài phần đo. Cả hai cách phải chỉ làm cùng việc bỏ hai ký hiệu và tạo kết quả (hoặc cùng gồm to_numeric nếu đã định nghĩa công việc như thế). Trước đo, đối chiếu giá trị, index và vị trí thiếu, ví dụ assert_series_equal(...,check_dtype=False) nếu biểu diễn kiểu kết quả khác. Đo lặp trên môi trường được ghi rõ. Một lần đo với một backend/thao tác không chứng minh apply hoặc .str luôn nhanh hơn; .str cũng không mặc định nhanh hơn mọi hàm Python.

**Hướng dẫn chấm:** 3 điểm: công việc/phần đo tương đương 1; kiểm giá trị/index/thiếu 1; dtype ngoài đo, lặp và giới hạn kết luận 1.

**Đối chiếu:** nhóm 5; K49; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Kiểm giá trị/index/thiếu trước benchmark; đổi dtype ngoài phần đo; hiệu năng tùy backend, không .str luôn nhanh hơn. **Nguồn đọc lại:** NB ô 25–31.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu đánh giá cơ chế/thiết kế hoặc diễn giải dữ kiện cho sẵn).

### B7-030

```python
ok = raw.str.strip().str.fullmatch(p, na=False)
```
Chỉ hàng 1,3 hợp lệ. Hàng 0 có tiền tố from, hàng 2 đặt phẩy sai. contains có thể tìm được đoạn '$400' trong hàng 0, hoặc một đoạn '$4' trong hàng 2; không kiểm hết chuỗi. Bỏ phẩy hàng 2 thành số 400 che lỗi định dạng gốc. 0 không âm nên hợp lệ.

**Hướng dẫn chấm:** 2 điểm: strip+fullmatch 1; chỉ mục 1,3 và ba lý do prefix/phẩy/0 1. Nhận Python re.fullmatch qua map với xử lý thiếu phù hợp.

**Đối chiếu:** nhóm 2; K18, K19, K26; mức Vận dụng. **Ưu tiên:** Trọng tâm; Trọng tâm LAB; mẫu ở phần tự học NB.

**Kiến thức/bẫy:** Trích/chuyển được số không chứng minh cả chuỗi đúng định dạng hay phân cách nghìn hợp lệ; fullmatch giá: dấu $, không âm, 0 hợp lệ, nhóm nghìn đúng, thập phân hai chữ số, strip khi được phép; contains bất kỳ đâu, match từ đầu, fullmatch cả chuỗi; không nhầm kiểm một đoạn với cả định dạng. **Nguồn đọc lại:** NB ô 103–104; LAB ô 11–12.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### Độ bao phủ sau đợt 3

Đã dùng 39/72 mục tiêu. Còn: K09, K10, K12, K13, K20, K22, K30, K31, K34, K35, K36, K50, K51, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 4 — phần A

### B7-031

**Đáp án: D.**

- A sai: tự strip trước khi slice dù không có lệnh.
- B sai: coi chuỗi rỗng cũng tự thành giá trị thiếu.
- C sai: bỏ qua slice, chỉ chạy upper.
- D đúng: slice lấy hai ký tự đầu trước khi upper; dấu cách đầu vẫn có, index không đổi.

**Đối chiếu:** nhóm 1; K11, K02, K13; mức Nền tảng. **Ưu tiên:** Trọng tâm; Trọng tâm (len trong LAB); slice tự học bảng tra; Tự học — upper/casefold.

**Kiến thức/bẫy:** str.len/str.slice giữ nhãn; độ dài ngắn không tự là vô ích; strip chỉ hai đầu; lower trả kết quả mới giữ index và bản gốc; không xóa khoảng trắng giữa; upper/lower/casefold không đồng nghĩa; casefold trong bảng tra, không tự xóa dấu. **Nguồn đọc lại:** NB ô 94 bảng tra; LAB ô 15–18.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-032

**Đáp án: C.**

- A sai: nhầm Int64 nullable với int64 và tự điền thiếu.
- B sai: đã thực sự chuyển số, không giữ định dạng mã chuỗi.
- C đúng: Int64 cho số nguyên có thiếu; chỉ lúc chuyển số mới bỏ 0 đầu của 02, Studio không thành 0.
- D sai: không có dropna, chuyển kiểu vẫn giữ Studio với thiếu.

**Đối chiếu:** nhóm 3; K31, K27; mức Vận dụng. **Ưu tiên:** Tự học NB ô 96–97: Int64; nền trích số thuộc bài chính.

**Kiến thức/bẫy:** extractall giữ mọi lần và index nguồn; Int64 giữ số nguyên với thiếu; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0. **Nguồn đọc lại:** NB ô 53–54,96–97.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-033

**Đáp án: A.**

- A đúng: None là một thiếu nguồn; chuỗi rỗng và ask là hai lỗi chuyển đổi theo quy ước, $0 hợp lệ.
- B sai: coi chuỗi rỗng vốn là thiếu nguồn dù raw.notna của nó True.
- C sai: coi giá 0 cũng là lỗi.
- D sai: gộp mọi parsed thiếu thành thiếu nguồn và bỏ truy nguyên raw.

**Đối chiếu:** nhóm 2; K16, K04; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** to_numeric coerce; lỗi raw.notna & parsed.isna khác thiếu từ nguồn, kể cả chuỗi rỗng có dữ liệu; Chuỗi rỗng, toàn khoảng trắng, thiếu khác nhau; dropna không loại chuỗi rỗng. **Nguồn đọc lại:** NB ô 32–37; LAB ô 9–10.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-034

**Đáp án: D.**

- A sai: giữ một hàng mỗi listing thay đơn vị mục tiện nghi.
- B sai: cho rằng explode tự reset index.
- C sai: tự khử nhãn lặp, bỏ một mục của L4.
- D đúng: mỗi mục giữ nhãn listing nguồn; L7 chỉ có placeholder nên bị dropna bỏ.

**Đối chiếu:** nhóm 4; K39, K46; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** explode mỗi phần tử thành hàng, giữ index lặp; [] tạo placeholder thiếu; Giữ bảng gốc đủ listing để không mất rỗng/thiếu sau explode-dropna; nhãn gắn đúng nguồn. **Nguồn đọc lại:** NB ô 76–81; LAB ô 32–34.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-035

**Đáp án: A.**

- A đúng: re.I nhận M2; m2x không có ranh giới cuối; chữ a trước 45 làm thiếu ranh giới đầu.
- B sai: bỏ ranh giới cuối, nhận hậu tố m2x.
- C sai: quên re.I nên bỏ M2.
- D sai: bỏ ranh giới giữa chữ a và chữ số 4.

**Đối chiếu:** nhóm 3; K34, K25; mức Vận dụng. **Ưu tiên:** Trọng tâm; Trọng tâm diện tích; mở rộng thập phân: LAB tự làm.

**Kiến thức/bẫy:** Diện tích m2/m², re.I; thập phân chấm/phẩy theo LAB; loại m2x và giữ bản gốc; \b là ranh giới ký tự từ, không là dấu cách; số và _ cũng là ký tự từ. **Nguồn đọc lại:** NB ô 59–60; LAB tự làm 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-036

**Đáp án: B.**

- A sai: đếm số lần xuất hiện thay số id khác nhau.
- B đúng: A lặp cùng mục không thành hai listing.
- C sai: đếm số loại tiện nghi thay số listing.
- D sai: dùng mọi mục kể cả wifi làm số listing có parking.

**Đối chiếu:** nhóm 4; K41; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Chuẩn hoá từng mục rồi nunique id; mục lặp cùng listing không thành nhiều listing. **Nguồn đọc lại:** NB ô 87–92.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-037

**Đáp án: C.**

- A sai: không có ngưỡng số test hữu hạn như thế.
- B sai: phủ nhận vai trò hữu ích của kiểm thử thay vì giới hạn kết luận.
- C đúng: tập test hữu hạn không tự chứng minh tính đúng trên mọi đầu vào.
- D sai: số khớp không đo chính xác ngữ nghĩa.

**Đối chiếu:** nhóm 5; K48; mức Nền tảng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Số khớp không là độ chính xác; kiểm dương/âm/gần đúng và nguyên văn, test hữu hạn không là chứng minh mọi đầu vào. **Nguồn đọc lại:** NB ô 93; LAB ô 1,25–28.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu đánh giá cơ chế/thiết kế hoặc diễn giải dữ kiện cho sẵn).

### B7-038

```python
s_chuan = s.str.strip().str.lower()
assert s_chuan.index.equals(s.index)
assert s.loc[9] == '  Wifi  '
```
wifi:2, wifi!:1, wi-fi:1, café:1, cafe:1. Có năm nhãn khác nhau. Xóa dấu câu hoặc dấu tiếng là thêm quy tắc chưa được cho; có thể nhập nhằng các nhãn mà nguồn muốn phân biệt. strip không gộp khoảng trắng bên trong mọi chuỗi.

**Hướng dẫn chấm:** 3 điểm: hai phương thức/giữ gốc 1; giải thích vượt quy tắc 1; năm nhãn, số đếm, index/bản gốc 1.

**Đối chiếu:** nhóm 1; K02, K03; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** strip chỉ hai đầu; lower trả kết quả mới giữ index và bản gốc; không xóa khoảng trắng giữa; Không tự gộp khác dấu, dấu câu, chính tả; wifi/wifi!/wi-fi cần quy tắc riêng. **Nguồn đọc lại:** NB ô 7–13; LAB ô 6–7.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-039

```python
p = r'\b([0-9]+(?:[.,][0-9]+)?)\s*m(?:2|²)\b'
x = s.str.extract(p, flags=re.I, expand=False)
area = pd.to_numeric(x.str.replace(',', '.', regex=False), errors='coerce')
```
A=46.5,B=32.5,C=80,D/E thiếu, m². Cờ re.I nhận 80 M2; D có x sau m2 nên thiếu ranh giới cuối. E có số nhưng không đơn vị. s/index giữ nguyên, không khớp không là 0 m². Mẫu được đánh giá theo miền số đã giới hạn, không nhận là parser mọi dạng số.

**Hướng dẫn chấm:** 2 điểm: mẫu số/đơn vị/ranh giới và flags 1; chuyển phẩy, kết quả/giữ nguồn và hai ca kiểm 1. Nhận pattern tương đương trong miền đã nêu.

**Đối chiếu:** nhóm 3; K34, K27; mức Vận dụng. **Ưu tiên:** LAB tự làm 2: mở rộng diện tích thập phân; không tăng yêu cầu thành regex mọi loại số.

**Kiến thức/bẫy:** Diện tích m2/m², re.I; thập phân chấm/phẩy theo LAB; loại m2x và giữ bản gốc; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0. **Nguồn đọc lại:** NB ô 59–60; LAB tự làm 2.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-040

(a) e có 5 hàng: A một, B một placeholder, C hai, D một placeholder; sau dropna còn 3 mục thật. (b) Trước dropna: 2/5; sau: 2/3. Hai phép mean đo tỷ trọng hàng exploded/mục, không một bool mỗi listing.
```python
co = ds.map(lambda xs: 'Wifi' in xs)
ty_le = co.mean()
```
(c) A,C True; B,D False nhưng vẫn đã biết: 2/4=0.5. Giữ ds gốc để có đủ mẫu số bốn listing.

**Hướng dẫn chấm:** 3 điểm: số hàng/placeholder 1; hai tỷ lệ và đơn vị 1; code một bool/listing và 2/4 1.

**Đối chiếu:** nhóm 4; K39, K40, K42; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** explode mỗi phần tử thành hàng, giữ index lặp; [] tạo placeholder thiếu; dropna sau explode bỏ placeholder/thiếu, không bỏ chuỗi rỗng; phân biệt trước/sau bỏ thiếu; Tỷ lệ listing có tiện nghi khác tỷ lệ mục tiện nghi; một bool mỗi listing và mẫu số đúng. **Nguồn đọc lại:** NB ô 76–86.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### Độ bao phủ sau đợt 4

Đã dùng 42/72 mục tiêu. Còn: K09, K10, K12, K20, K22, K30, K35, K36, K50, K51, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 5 — phần A

### B7-041

**Đáp án: C.**

- A sai: tự ép int khi chưa có lệnh chuyển.
- B sai: nhầm findall với search/extract lần đầu.
- C đúng: findall giữ dãy chữ số, chưa chuyển số; sub thay mỗi dãy ký tự trắng bằng một dấu cách.
- D sai: nhầm thay ký tự trắng bằng dấu cách với xóa hết.

**Đối chiếu:** nhóm 3; K30, K22; mức Nền tảng. **Ưu tiên:** Trọng tâm; Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học.

**Kiến thức/bẫy:** re.findall/re.sub trên chuỗi Python; không tự là pandas Series hay số; Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước. **Nguồn đọc lại:** NB ô 94–95.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-042

**Đáp án: C.**

- A sai: coi startswith như kiểm nhãn wifi bằng nhau, bỏ wifi!.
- B sai: tự nhập wi-fi vào wifi ngoài quy tắc.
- C đúng: startswith kiểm tiền tố nên nhận wifi!; endswith nhận hậu tố tv, không phải kiểm tiện nghi đúng nhãn wifi.
- D sai: coi endswith cần có ký tự đứng trước tv, bỏ chuỗi chỉ có TV.

**Đối chiếu:** nhóm 1; K10, K12; mức Vận dụng. **Ưu tiên:** split thuộc bài chính; join/startswith/endswith từ bảng tự học NB ô 94.

**Kiến thức/bẫy:** startswith/endswith kiểm tiền tố/hậu tố, không phải so nhãn bằng nhau; split đúng dấu phân cách; expand đổi dạng cột; join nối các phần tử trong ô. **Nguồn đọc lại:** NB ô 70–71,94 bảng tra.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-043

**Đáp án: C.**

- A sai: đếm hai lần Wifi trong A làm hai listing.
- B sai: bỏ B rỗng khỏi mẫu số.
- C đúng: chỉ A có đúng Wifi, lặp trong A không tăng số listing; B rỗng thuộc mẫu số.
- D sai: lấy hai mục Wifi chia năm hàng exploded kể cả placeholder của B, đổi đơn vị quan sát.

**Đối chiếu:** nhóm 4; K42, K43, K45; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Tỷ lệ listing có tiện nghi khác tỷ lệ mục tiện nghi; một bool mỗi listing và mẫu số đúng; Danh sách biết rỗng vẫn thuộc mẫu số listing; không dùng số hàng exploded thay thế; Wifi đúng nhãn khác Pocket wifi/wifi!; tìm substring JSON thô khác membership sau chuẩn hoá. **Nguồn đọc lại:** NB ô 82–86; LAB ô 33–36.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-044

**Đáp án: C.**

- A sai: cho phép âm chỉ vì to_numeric đọc được -5.
- B sai: cho phép thập phân một chữ số ngoài quy tắc.
- C đúng: 0 được phép và khoảng trắng hai đầu được bỏ; âm bị cấm, một chữ số thập phân không đủ.
- D sai: tự loại giá 0 hoặc không thực hiện strip đã được cho phép.

**Đối chiếu:** nhóm 2; K19; mức Nền tảng. **Ưu tiên:** Trọng tâm LAB; mẫu ở phần tự học NB.

**Kiến thức/bẫy:** fullmatch giá: dấu $, không âm, 0 hợp lệ, nhóm nghìn đúng, thập phân hai chữ số, strip khi được phép. **Nguồn đọc lại:** NB ô 103–104; LAB ô 11–12.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-045

**Đáp án: C.**

- A sai: bỏ yêu cầu nhóm bắt của extract.
- B sai: nhầm extract với findall và tự chuyển số.
- C đúng: extract yêu cầu ít nhất một nhóm bắt, không tự mặc định trả toàn đoạn như re.search.group(0).
- D sai: coi extract như phép chọn cột gốc.

**Đối chiếu:** nhóm 3; K28; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** expand=False một nhóm → Series; nhiều nhóm → DataFrame; extract không nhóm bắt gây lỗi. **Nguồn đọc lại:** NB ô 63; kiểm API extract.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-046

**Đáp án: A.**

- A đúng: dấu $ có thể khớp trước newline cuối; fullmatch mẫu không chứa newline không phủ hết chuỗi.
- B sai: coi $ và fullmatch tương đương tuyệt đối kể cả newline cuối.
- C sai: cho rằng $ chỉ có đúng vị trí sau newline cuối nên không nhận P7.
- D sai: đảo hành vi hai phép kiểm.

**Đối chiếu:** nhóm 3; K52, K26; mức Vận dụng. **Ưu tiên:** Tự học NB ô 94: neo; đề nêu rõ newline/flags, không cần thuộc cờ nâng cao.

**Kiến thức/bẫy:** ^/$ và fullmatch khác khi có newline cuối; . mặc định không ăn newline; phải nêu flags/quy ước; contains bất kỳ đâu, match từ đầu, fullmatch cả chuỗi; không nhầm kiểm một đoạn với cả định dạng. **Nguồn đọc lại:** NB ô 94; RX quy ước fullmatch.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-047

```python
c = raw.str.strip()
ok = c.str.fullmatch(p, na=False)
parsed = pd.to_numeric(c.where(ok).str.replace(r'[$,]', '', regex=True), errors='coerce')
loi = raw.notna() & ~ok
```
parsed=[thiếu,0,thiếu,thiếu,30]; lỗi hàng 0,2; hàng 3 thiếu từ nguồn. Đọc ra -10 không thỏa không âm, 120 không chứng minh phẩy ban đầu đúng. Không điền 0 cho thiếu/lỗi vì sẽ lẫn với hàng 1 có giá 0 hợp lệ. Giữ raw để truy nguyên.

**Hướng dẫn chấm:** 2 điểm: fullmatch trước chuyển và chỉ chuyển ok 1; kết quả/lỗi/thiếu nguồn 0,5; giá 0 và không điền 0 0,5. Nhận gán vào Series số thiếu khởi tạo rồi chỉ điền hàng ok.

**Đối chiếu:** nhóm 2; K18, K19, K17; mức Vận dụng. **Ưu tiên:** Trọng tâm; Trọng tâm LAB; mẫu ở phần tự học NB.

**Kiến thức/bẫy:** Trích/chuyển được số không chứng minh cả chuỗi đúng định dạng hay phân cách nghìn hợp lệ; fullmatch giá: dấu $, không âm, 0 hợp lệ, nhóm nghìn đúng, thập phân hai chữ số, strip khi được phép; Giữ giá gốc; chưa biết khác 0, không fillna(0) tùy ý. **Nguồn đọc lại:** NB ô 103–104; LAB ô 11–12.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-048

```python
known = ds.dropna()
co = known.map(lambda xs: 'Wifi' in xs)
ty_le_biet = co.mean()
ty_le_quan_sat = co.sum()/len(ds)
```
(a) 2/4=0.5 gồm A,B,D,E; A chỉ đếm một, B rỗng vẫn trong mẫu số. (b) 2/5=0.4 là tỷ lệ quan sát liệt kê trên năm listing, chưa biết trạng thái C nên không xác nhận tỷ lệ thật sự có Wifi toàn bộ. (c) Kiểm co có bốn nhãn, A/E True, B/D False; tổng 2. Nếu bỏ B hoặc đếm hai mục A, các con số này sai. Không biến None thành [] để suy C chắc không có Wifi.

**Hướng dẫn chấm:** 3 điểm: nhóm đã biết/code 1; 2/4 và 2/5 đúng ý nghĩa 1; kiểm A/B/C và không đếm lặp 1.

**Đối chiếu:** nhóm 4; K44, K43, K46; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** None chưa biết; phải nêu mẫu số toàn bộ hay nhóm đã biết, không trộn [] với None; Danh sách biết rỗng vẫn thuộc mẫu số listing; không dùng số hàng exploded thay thế; Giữ bảng gốc đủ listing để không mất rỗng/thiếu sau explode-dropna; nhãn gắn đúng nguồn. **Nguồn đọc lại:** LAB ô 35–36; GK câu 25 (biến thể mẫu số).

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-049

x=['Central','todo','Museo',thiếu]. Mẫu chỉ lấy một từ: không lấy đủ Central Park/Museo Norte; todo nghĩa gần mọi thứ, không phải tên riêng. Nên gọi tu_sau_gan và đọc nguyên văn cả ca khớp/không khớp, bổ sung nhãn kiểm nếu cần xác định địa điểm. Nhắc metro không đo khoảng cách; nhắc wifi/internet không xác minh hài lòng (ví dụ 'internet was slow'). Không chỉ tăng số khớp rồi tuyên bố chính xác hơn.

**Hướng dẫn chấm:** 3 điểm: bốn kết quả 1; từ đầu/không địa danh, tên cột 1; phản ví dụ cảm xúc/khoảng cách và kiểm nguyên văn 1.

**Đối chiếu:** nhóm 5; K36, K47, K48; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** near/cerca de lấy một từ đầu theo mẫu, không chắc địa danh hay cả tên địa điểm; Nhắc metro/wifi không xác minh khoảng cách, hài lòng hay tiện nghi hoạt động tốt; tên cột đúng phép đo; Số khớp không là độ chính xác; kiểm dương/âm/gần đúng và nguyên văn, test hữu hạn không là chứng minh mọi đầu vào. **Nguồn đọc lại:** LAB ô 21–28, tự làm 1.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-050

a là Series: A='1',B thiếu,C='3', giữ ba nhãn. b là DataFrame (3,1), các cặp (A,0)→'1',(A,1)→'2',(C,0)→'3'. B không có lần khớp nên không xuất hiện trong b. len(b)=3 đếm cụm khớp, chỉ hai listing A,C được quy tắc trích được số; không là số listing thật sự có phòng trong nguồn. Giá trị trích còn là chuỗi.

**Hướng dẫn chấm:** 2 điểm: a đúng 0,5; shape/cặp index và chuỗi của b 1; đơn vị lần khớp và không suy số phòng thật 0,5.

**Đối chiếu:** nhóm 3; K31, K27; mức Vận dụng. **Ưu tiên:** Tự học NB ô 96–97: extractall; không mở rộng MultiIndex ngoài đọc nhãn lần khớp.

**Kiến thức/bẫy:** extractall giữ mọi lần và index nguồn; Int64 giữ số nguyên với thiếu; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0. **Nguồn đọc lại:** NB ô 96–97.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### Độ bao phủ sau đợt 5

Đã dùng 47/72 mục tiêu. Còn: K09, K20, K35, K50, K51, K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 6 — phần A

### B7-051

**Đáp án: D.**

- A sai: bỏ dấu phủ định ^ trong lớp.
- B sai: bỏ vai trò + gộp ký tự liên tiếp.
- C sai: coi ^ trong lớp là neo đầu chuỗi, không là phủ định lớp.
- D đúng: lớp phủ định lấy các dãy không phải chữ số ASCII; + gộp a,b liên tiếp, _ cũng không là chữ số.

**Đối chiếu:** nhóm 3; K22, K30; mức Nền tảng. **Ưu tiên:** Trọng tâm; Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học.

**Kiến thức/bẫy:** Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước; re.findall/re.sub trên chuỗi Python; không tự là pandas Series hay số. **Nguồn đọc lại:** NB ô 94; RX lớp ký tự.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-052

**Đáp án: B.**

- A sai: coi chuỗi rỗng cũng là giá trị thiếu.
- B đúng: dropna bỏ placeholder A và thiếu C, không bỏ chuỗi rỗng của B.
- C sai: coi [] explode thành chuỗi rỗng thay placeholder thiếu.
- D sai: tự đổi None thành danh sách rỗng và giữ nó như mục sau explode.

**Đối chiếu:** nhóm 4; K04, K40; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Chuỗi rỗng, toàn khoảng trắng, thiếu khác nhau; dropna không loại chuỗi rỗng; dropna sau explode bỏ placeholder/thiếu, không bỏ chuỗi rỗng; phân biệt trước/sau bỏ thiếu. **Nguồn đọc lại:** NB ô 78–81.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-053

**Đáp án: C.**

- A sai: bỏ khác biệt dtype và tham số na=False.
- B sai: a không False, và mask không xác minh trạng thái tiện nghi.
- C đúng: string nullable giữ NA; str pandas 3 và tham số na=False xử lý mask thiếu khác.
- D sai: None không là văn bản wifi; bỏ quy tắc thiếu của str/na=False.

**Đối chiếu:** nhóm 1; K09, K08; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** dtype string/str/object có thể khác kết quả thiếu; chỉ hỏi với dtype/config rõ; na=False có thể vẫn đưa tên thiếu vào mẫu số mean; không chứng minh đối tượng không có thuộc tính. **Nguồn đọc lại:** NB ô 19–20.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-054

**Đáp án: B.**

- A sai: coi expand=True như mặc định expand=False.
- B đúng: expand=True đưa các phần ra cột, chuỗi bắt đầu ; cho phần đầu rỗng; không tự bỏ hàng D.
- C sai: tự bỏ chuỗi rỗng D dù không có lệnh lọc.
- D sai: tự bỏ phần rỗng trước dấu tách, làm lệch vị trí.

**Đối chiếu:** nhóm 4; K12; mức Nền tảng. **Ưu tiên:** Trọng tâm: split; đọc thêm: join/bảng tra.

**Kiến thức/bẫy:** split đúng dấu phân cách; expand đổi dạng cột; join nối các phần tử trong ô. **Nguồn đọc lại:** BG §3; NB ô 70–71.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-055

**Đáp án: C.**

- A sai: áp miền ASCII cho mọi lớp của Python re mặc định.
- B sai: coi [0-9] mở rộng thành mọi chữ số Unicode như \d.
- C đúng: Python \d nhận chữ số Unicode; [0-9] chỉ ASCII; \w nhận chữ Unicode, _ và số.
- D sai: coi \w chỉ chữ cái ASCII hoặc loại _/chữ số.

**Đối chiếu:** nhóm 3; K50; mức Vận dụng. **Ưu tiên:** Tự học — Unicode Python re; không khái quát sang Arrow.

**Kiến thức/bẫy:** Python re mặc định Unicode: \w/\d không chỉ ASCII; [0-9] rõ miền chữ số ASCII. **Nguồn đọc lại:** NB ô 101–102; RX quy ước ASCII.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-056

**Đáp án: D.**

- A sai: đồng nhất API trên cột với đảm bảo tốc độ cho mọi backend.
- B sai: bỏ kết quả backend X và phạm vi phép đo.
- C sai: trộn thêm chi phí riêng cho một cách, trái công việc tương đương.
- D đúng: cùng API có thể dùng engine/cách duyệt khác; số đo cho một công việc không là định luật mọi phép chuỗi.

**Đối chiếu:** nhóm 5; K49; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Kiểm giá trị/index/thiếu trước benchmark; đổi dtype ngoài phần đo; hiệu năng tùy backend, không .str luôn nhanh hơn. **Nguồn đọc lại:** NB ô 25–31.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa thực thi (câu đánh giá cơ chế/thiết kế hoặc diễn giải dữ kiện cho sẵn).

### B7-057

```python
lo = s.str.lower()
fold = s.str.casefold()
```
lo=['straße','strasse','café','cafe']: 4 nhãn; fold=['strasse','strasse','café','cafe']: 3 nhãn. Cả hai giữ index [3,8,2,6], s vẫn có Straße. casefold phục vụ so chữ không phân biệt cách viết hoa/thường mạnh hơn lower trong ví dụ này, không tự là quy tắc xóa dấu hay sửa chính tả; café và cafe vẫn khác.

**Hướng dẫn chấm:** 2 điểm: hai code/kết quả 1; số nhãn/index/giữ s 0,5; không suy xóa dấu 0,5.

**Đối chiếu:** nhóm 1; K13, K03, K02; mức Vận dụng. **Ưu tiên:** Tự học — casefold trong bảng tra NB ô 94; không yêu cầu thuộc Unicode, kết quả cần dùng đã cho.

**Kiến thức/bẫy:** upper/lower/casefold không đồng nghĩa; casefold trong bảng tra, không tự xóa dấu; Không tự gộp khác dấu, dấu câu, chính tả; wifi/wifi!/wi-fi cần quy tắc riêng; strip chỉ hai đầu; lower trả kết quả mới giữ index và bản gốc; không xóa khoảng trắng giữa. **Nguồn đọc lại:** NB ô 94 bảng tra.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-058

```python
t = d.assign(loai_chuan=d['loai'].str.strip().str.lower(),
    gia=pd.to_numeric(d['raw'].str.replace(r'[$,]','',regex=True),errors='coerce'))
kq = t.groupby('loai_chuan')['gia'].median()
```
home có hai giá biết 100,300→median 200; room có 20,1000,40→median 40, không phải mean 1060/3. Điền thiếu home bằng 0 làm median 100, thay tập giá gốc. Kiểm một raw thiếu, không lỗi chuyển đổi: (t['raw'].notna() & t['gia'].isna()).sum()==0; d/raw không bị ghi đè. Đây là median trên giá biết, không coi giá chưa biết bằng 0.

**Hướng dẫn chấm:** 3 điểm: chuẩn hoá/parse giữ raw 1; groupby median/kết quả 1; tập giá, hai cách sai và kiểm nguồn 1.

**Đối chiếu:** nhóm 2; K20, K15, K17; mức Phân loại. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Chuẩn hoá loại phòng rồi median trên đúng tập giá biết; không đổi sang mean hoặc điền thiếu 0; Bỏ ký hiệu tiền/phân cách theo quy ước nguồn; dấu phẩy nghìn khác dấu phẩy thập phân; Giữ giá gốc; chưa biết khác 0, không fillna(0) tùy ý. **Nguồn đọc lại:** NB ô 38–39; LAB ô 9–12.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-059

```python
t = s.str.replace('<br/>', ' ', regex=False)
n_review = s.str.contains('<br/>',regex=False,na=False).sum()
```
t=['A B C','<br> X','<BR/>Y','<b>Z</b>'], giữ index/bản gốc. Một review bị tác động nhưng hai lần thay; mỗi lần 5 ký tự thành 1 nên tổng giảm 8. Có thể dùng re.sub(`r'<br/>'`,' ',text) tương đương trên mỗi chuỗi. Bỏ qua hoa thường sẽ thay thêm <BR/> trái quy tắc; các thẻ khác vẫn còn nên không phải bộ làm sạch mọi HTML.

**Hướng dẫn chấm:** 2 điểm: thay/đếm đúng 0,75; bốn chuỗi, một review/hai lần/giảm 8 0,75; giới hạn quy tắc và giữ nguồn 0,5.

**Đối chiếu:** nhóm 3; K35, K30; mức Vận dụng. **Ưu tiên:** Trọng tâm.

**Kiến thức/bẫy:** Chỉ thay đúng <br/> bằng một dấu cách; đếm dòng khác số lần thay; không là làm sạch mọi HTML; re.findall/re.sub trên chuỗi Python; không tự là pandas Series hay số. **Nguồn đọc lại:** LAB ô 19–20; NB ô 94–95.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-060

(a) Các phương thức/backend có thể dùng engine khác. Ở cấu hình này, contains không flags trên Arrow dùng quy ước từ ASCII; ² không là ký tự từ nên không có ranh giới từ ngay sau nó ở cuối chuỗi. extract dùng Python re; Python coi ² là ký tự từ nên lấy được 30m². Storage python dùng Python re cho contains. Đếm Ñuñoa cũng phản ánh khác quy ước ký tự từ.
(b) Không khái quát Arrow thành quy tắc Python re hoặc mọi backend. (c) Ghi phiên bản, dtype/storage, flags và phương thức; thử đúng ca ASCII/ngoài ASCII, thiếu và gần đúng, đối chiếu re.search/extract trước áp dụng. Output đã cho và ca thực thi chỉ hỗ trợ cấu hình đó, không cam kết mọi phiên bản.

**Hướng dẫn chấm:** 3 điểm: engine/ranh giới và giải thích a,b,c 1,5; bác hai khái quát 0,75; cấu hình/ca kiểm phù hợp 0,75. Không yêu cầu thuộc bảng Unicode/chi tiết nội bộ Arrow.

**Đối chiếu:** nhóm 3; K51, K50, K25; mức Phân loại. **Ưu tiên:** Đọc thêm, không yêu cầu trên lớp: Unicode/backend; ghim đúng cấu hình thực tế và cho output trong đề.

**Kiến thức/bẫy:** Arrow/Python có thể khác ranh giới/từ; ghim dtype, storage, phiên bản và kiểm thực tế, không khái quát engine; Python re mặc định Unicode: \w/\d không chỉ ASCII; [0-9] rõ miền chữ số ASCII; \b là ranh giới ký tự từ, không là dấu cách; số và _ cũng là ký tự từ. **Nguồn đọc lại:** NB ô 101–102.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### Độ bao phủ sau đợt 6

Đã dùng 52/72 mục tiêu. Còn: K53, K54, K55, K56, K57, K58, K59, K60, K61, K62, K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 7 — luyện regex bổ sung

### B7-R01

**Đáp án: C.**

- A sai: mất số 0 đầu và sai kiểu str.
- B sai: pattern không có nhóm bắt số 1 nên gây IndexError khi khớp.
- C đúng: search lấy lần đầu; group0 là chuỗi khớp, không đổi int hoặc danh sách.
- D sai: trả list mọi dãy; không khớp cho [] khác None.

**Đối chiếu:** nhóm 3; K53, K27, K50; mức Cơ bản. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm; Tự học — Unicode.

**Kiến thức/bẫy:** Dãy chữ số ASCII đầu tiên; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0; Python re mặc định Unicode: \w/\d không chỉ ASCII; [0-9] rõ miền chữ số ASCII. **Nguồn đọc lại:** RX câu 1, ô 2–6.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R02

**Đáp án: D.**

- A sai: nhận abcX dù ký tự cuối không phải dấu chấm.
- B sai: bỏ các ký tự hợp lệ như dấu cách/dấu câu ở ba vị trí đầu.
- C sai: cho dấu chấm cuối tùy chọn, nhận sai chuỗi chỉ ba ký tự abc.
- D đúng: ba wildcard rồi chấm có escape; không có DOTALL nên loại newline trong ba ký tự đầu.

**Đối chiếu:** nhóm 3; K54, K52, K07; mức Cơ bản. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm; Tự học — ký hiệu mở rộng/quy ước.

**Kiến thức/bẫy:** Dấu chấm thường/wildcard; ^/$ và fullmatch khác khi có newline cuối; . mặc định không ăn newline; phải nêu flags/quy ước; contains mặc định regex; . wildcard, \. chấm thật; raw string không tắt regex. **Nguồn đọc lại:** RX câu 2, ô 7–11.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R03

**Đáp án: A.**

- A đúng: đúng quy tắc nhưng mẫu chỉ có nhánh c, m hoặc fan nên fullmatch can thất bại.
- B sai: đúng quy tắc và đúng nhánh fan; chưa bộc lộ lỗi.
- C sai: sai quy tắc và mẫu cũng loại; chưa bộc lộ lỗi.
- D sai: sai quy tắc và mẫu cũng loại; chưa bộc lộ lỗi.

**Đối chiếu:** nhóm 3; K55, K23; mức Cơ bản. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Tập ký tự; Ngoặc giới hạn |; các nhánh thiếu tiền tố có thể khớp sai. **Nguồn đọc lại:** RX câu 3, ô 12–16.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R04

```python
def hop_le(text):
    if text is None: return False
    return re.fullmatch(r'[A-C][n-p][a-c]', text) is not None
```
False,True,False,False,False. ' Apa' có dấu cách ngoài chuỗi nên sai; strip sẽ biến nó thành Apa và nhận sai. AnaX chỉ có đoạn Ana hợp lệ nhưng cả chuỗi dài hơn ba. D vượt cận A–C. Không tự đổi hoa/thường.

**Hướng dẫn chấm:** 2 điểm: None/bool và fullmatch không preprocess 1; năm kết quả 0,5; hai phản ví dụ strip/search 0,5.

**Đối chiếu:** nhóm 3; K56, K26; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Khoảng ký tự; contains bất kỳ đâu, match từ đầu, fullmatch cả chuỗi; không nhầm kiểm một đoạn với cả định dạng. **Nguồn đọc lại:** RX câu 4, ô 17–21.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R05

**Đáp án: A.**

- A đúng: {3,5} giới hạn số z ở cả hai cận; các chuỗi có 2,3,5,6 z.
- B sai: bỏ giới hạn hai cận, coi z+ như đủ.
- C sai: coi cận dưới 3 là số lần chính xác.
- D sai: coi cận trên 5 là tối thiểu, không có giới hạn trên.

**Đối chiếu:** nhóm 3; K57, K22; mức Cơ bản. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học.

**Kiến thức/bẫy:** Giới hạn số lần lặp; Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước. **Nguồn đọc lại:** RX câu 5, ô 22–26.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R06

```python
def hop_le(text):
    return False if text is None else re.fullmatch(r'a{2,}b*c+',text) is not None
```
Cũ bỏ 'aac' vì bắt buộc b; cũ nhận 'ab' dù thiếu a thứ hai và không có c. Mới a{2,}: ít nhất hai a; b*: có thể vắng; c+: ít nhất một c. Cả chuỗi được kiểm, không chỉ đoạn đầu.

**Hướng dẫn chấm:** 2 điểm: pattern ba ràng buộc/fullmatch/None 1; hai phản ví dụ và giải thích lượng từ 1.

**Đối chiếu:** nhóm 3; K58, K22; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học.

**Kiến thức/bẫy:** Không lần/ít nhất một/tối thiểu; Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước. **Nguồn đọc lại:** RX câu 6, ô 27–31.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R07

**Đáp án: C.**

- A sai: tự áp số ít/số nhiều: bỏ 2 file và 1 files dù đề cho phép.
- B sai: cho số 0 đầu dù phần số dương đã quy định.
- C đúng: s? cho phép file/files; \? bắt buộc dấu hỏi thật; không áp thêm quy tắc ngữ pháp số ít/số nhiều.
- D sai: coi dấu hỏi cuối cũng là tùy chọn thay literal bắt buộc.

**Đối chiếu:** nhóm 3; K59, K22; mức Cơ bản. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học.

**Kiến thức/bẫy:** Tùy chọn và dấu hỏi thường; Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước. **Nguồn đọc lại:** RX câu 7, ô 32–36.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R08

```python
def hop_le(text):
    if text is None: return False
    return re.fullmatch(r'[0-9]+\.\s+abc',text) is not None
```
False,True,True,False,False. Đổi * thành + ở phần phân cách: cần ít nhất một ký tự trắng. Newline nằm trong s nên được phép ở vị trí này, dù . wildcard mặc định không ăn newline; ở đây \. là dấu chấm literal. Khoảng trắng cuối ngoài abc không được phép.

**Hướng dẫn chấm:** 2 điểm: sửa +/fullmatch/None 1; năm kết quả và lý do separator/newline/cuối chuỗi 1.

**Đối chiếu:** nhóm 3; K60, K22; mức Cơ bản. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học.

**Kiến thức/bẫy:** Ký tự trắng phân cách; Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước. **Nguồn đọc lại:** RX câu 8, ô 37–41.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R09

**Đáp án: B.**

- A sai: trả cả .pdf chưa loại phần mở rộng.
- B đúng: nhóm1 bao cả tiền tố file và phần sau; nhóm2 chỉ là B_08.
- C sai: mất tiền tố file.
- D sai: trả tuple hai nhóm, sai kiểu một chuỗi tên.

**Đối chiếu:** nhóm 3; K61, K24, K29; mức Cơ bản. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Tên PDF và nhóm bắt; Nhóm bắt và không bắt; nhóm thừa đổi phần dữ liệu/shape được trả; re.search: group(0) cả đoạn, group(1) nhóm đầu, groups tuple; thiếu nhóm nhánh là None. **Nguồn đọc lại:** RX câu 9, ô 42–46.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R10

```python
p = r'\b([0-9]+)\s*(?:BR|bedrooms?)\b'
def lay_so(text):
    if text is None: return None
    m = re.search(p,text,flags=re.I)
    return m.group(1) if m is not None else None
```
None,'0',None,'2'. Ngoặc không bắt buộc phần số áp cho mọi nhánh. 2BR2BA vẫn không khớp vì sau BR là số, không có ranh giới; tuân quy tắc này không chứng minh đã bao phủ mọi cách viết thật. Không chuyển không khớp thành 0; '0' ở A là số ghi rõ.

**Hướng dẫn chấm:** 2 điểm: mẫu/hàm một nhóm, None và re.I 1; bốn kết quả, phạm vi | và giới hạn ranh giới 1.

**Đối chiếu:** nhóm 3; K62, K23, K25; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Số phòng/hoặc/ranh giới; Ngoặc giới hạn |; các nhánh thiếu tiền tố có thể khớp sai; \b là ranh giới ký tự từ, không là dấu cách; số và _ cũng là ký tự từ. **Nguồn đọc lại:** RX câu 10, ô 47–51.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### Độ bao phủ sau đợt 7

Đã dùng 62/72 mục tiêu. Còn: K63, K64, K65, K66, K67, K68, K69, K70, K71, K72, đã bố trí ở các đợt sau.

## Đợt 8 — luyện regex bổ sung

### B7-R11

**Đáp án: C.**

- A sai: cho phần sau chấm rỗng như dùng [0-9]*.
- B sai: thêm dấu cộng ngoài quy tắc.
- C đúng: âm và 0 đầu được phép; ba mục kia lần lượt thiếu phần sau chấm, có cộng, thiếu phần nguyên.
- D sai: cho phần nguyên vắng mặt ngoài quy tắc.

**Đối chiếu:** nhóm 3; K63, K26; mức Cơ bản. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Số nguyên/thập phân đơn giản; contains bất kỳ đâu, match từ đầu, fullmatch cả chuỗi; không nhầm kiểm một đoạn với cả định dạng. **Nguồn đọc lại:** RX câu 11, ô 52–56.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R12

```python
I = r'(?:[0-9]{1,3}(?:,[0-9]{3})+|[0-9]+)'
E = r'(?:[eE][+-]?[0-9]+)?'
p = r'[+-]?'+I+r'(?:\.[0-9]+)?'+E
def hop_le(text):
    return False if text is None else re.fullmatch(p,text) is not None
```
True,False,False,True,False. Phẩy không được tùy ý xuất hiện; nhóm sau phẩy cần đúng ba số. Có e/E thì bắt buộc số mũ, nên 1E+ sai. Đây chỉ kiểm định dạng, chưa chuyển giá trị số.

**Hướng dẫn chấm:** 2 điểm: I đúng nhóm nghìn 0,75; E đầy đủ số mũ 0,5; fullmatch/None và năm kết quả 0,75.

**Đối chiếu:** nhóm 3; K64, K22, K19; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm LAB; mẫu ở phần tự học NB; Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học.

**Kiến thức/bẫy:** Nhóm nghìn và số mũ; Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước; fullmatch giá: dấu $, không âm, 0 hợp lệ, nhóm nghìn đúng, thập phân hai chữ số, strip khi được phép. **Nguồn đọc lại:** RX câu 12, ô 57–61.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R13

**Đáp án: D.**

- A sai: hai ngoặc tùy chọn độc lập nhận sai (3055551234 hoặc 305)5551234.
- B sai: bắt buộc ngoặc, bỏ số hợp lệ 305-555-1234.
- C sai: chỉ nhận không ngoặc, bỏ (305)5551234 hợp lệ.
- D đúng: hai nhánh tách biệt ngoặc đủ cặp và không ngoặc; trả nhóm1 hoặc nhóm2 có tham gia.

**Đối chiếu:** nhóm 3; K65, K24; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Mã vùng điện thoại/ngoặc đủ cặp; Nhóm bắt và không bắt; nhóm thừa đổi phần dữ liệu/shape được trả. **Nguồn đọc lại:** RX câu 13, ô 62–66.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R14

```python
p = '('+BASE+')'+FILTER+'@'+DOMAIN
def ten_goc(text):
    if text is None: return None
    m = re.fullmatch(p,text)
    return m.group(1) if m is not None else None
```
'Lan.01',None,None,None. Đặt filter ngoài nhóm trả kết quả, nhưng vẫn trong mẫu kiểm toàn email. Không lower nên giữ Lan. Chấm liên tiếp tạo nhóm rỗng; + trống sai. Chỉ kiểm hình thức trong miền giản lược, không kiểm hộp thư tồn tại/nhận thư được.

**Hướng dẫn chấm:** 2 điểm: nhóm BASE đúng, FILTER/DOMAIN vẫn được kiểm 1; hàm/None/bốn kết quả 0,5; giới hạn xác minh 0,5.

**Đối chiếu:** nhóm 3; K66, K24, K27; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Tài khoản email trước +filter; Nhóm bắt và không bắt; nhóm thừa đổi phần dữ liệu/shape được trả; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0. **Nguồn đọc lại:** RX câu 14, ô 67–71.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R15

**Đáp án: A.**

- A đúng: bỏ H1 trong chú thích và thẻ đóng p; thẻ tự đóng my-card là thẻ mở trước div.
- B sai: search trước khi bỏ chú thích, lấy thẻ nằm trong nội dung chú thích.
- C sai: coi thẻ đóng là thẻ mở.
- D sai: tự bỏ thẻ tự đóng dù quy tắc cho phép.

**Đối chiếu:** nhóm 3; K67, K35; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Thẻ mở ngoài chú thích giản lược; Chỉ thay đúng <br/> bằng một dấu cách; đếm dòng khác số lần thay; không là làm sạch mọi HTML. **Nguồn đọc lại:** RX câu 15, ô 72–76.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R16

```python
p = r'([A-Za-z0-9_]+(?:[.-][A-Za-z0-9_]+)*)\.(jpg|png|gif)'
def lay_anh(text):
    if text is None: return None
    m = re.fullmatch(p,text)
    return m.groups() if m is not None else None
```
('scene.02-night','png'),None,None,None. Nhóm giữa đổi sang không bắt để chỉ còn hai trường; fullmatch loại đuôi tạm .jpg.tmp vì toàn tên không kết thúc bằng mở rộng cho phép. Không tự lower để nhận JPG.

**Hướng dẫn chấm:** 2 điểm: ?: đúng nhóm lặp, giữ hai nhóm cần trả 0,75; hàm/None/kết quả 0,75; fullmatch, hoa thường và tệp tạm 0,5.

**Đối chiếu:** nhóm 3; K68, K24, K28; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Tên ảnh/phần mở rộng; Nhóm bắt và không bắt; nhóm thừa đổi phần dữ liệu/shape được trả; expand=False một nhóm → Series; nhiều nhóm → DataFrame; extract không nhóm bắt gây lỗi. **Nguồn đọc lại:** RX câu 16, ô 77–81.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R17

```python
def cat_dau_cuoi(text):
    if text is None: return None
    return re.fullmatch(r'[ \t]*(.*?)[ \t]*',text).group(1)
# khi gom: if result is not None:
```
Kết quả 'A  B','','',None,'\u00a0X\u00a0' (NBSP nguyên văn). .*? không tham lam để phần cuối nhận dấu cách/tab; [ \t] không ăn NBSP/\v/\f như \s. if result bỏ cả hai kết quả rỗng hợp lệ; is not None chỉ bỏ trường hợp thiếu. Không gộp khoảng trắng giữa A,B.

**Hướng dẫn chấm:** 3 điểm: mẫu chỉ space/tab, nội dung không tham lam, None 1; năm kết quả/giữ NBSP 1; truthiness và sửa giữ rỗng 1.

**Đối chiếu:** nhóm 3; K69, K04, K52; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm; Tự học — ký hiệu mở rộng/quy ước.

**Kiến thức/bẫy:** Cắt dấu cách-tab và tham lam; Chuỗi rỗng, toàn khoảng trắng, thiếu khác nhau; dropna không loại chuỗi rỗng; ^/$ và fullmatch khác khi có newline cuối; . mặc định không ăn newline; phải nêu flags/quy ước. **Nguồn đọc lại:** RX câu 17, ô 82–86.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R18

**Đáp án: B.**

- A sai: bỏ lệnh int, sai kiểu trường dòng.
- B đúng: search lần đầu, chỉ phương thức ở nhóm1, số dòng được int theo quy tắc.
- C sai: lấy cụm cuối thay lần đầu.
- D sai: trả cả đường dẫn gói/lớp thay nhóm phương thức.

**Đối chiếu:** nhóm 3; K70, K29, K27; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** Log: phương thức/tệp/dòng; re.search: group(0) cả đoạn, group(1) nhóm đầu, groups tuple; thiếu nhóm nhánh là None; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0. **Nguồn đọc lại:** RX câu 18, ô 87–91.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R19

**Đáp án: D.**

- A sai: tự lower giao thức ngoài quy tắc.
- B sai: tự chuyển cổng int, mất 0 đầu và sai kiểu.
- C sai: nhập đường dẫn vào máy chủ dù nhóm host kết thúc trước cổng/path.
- D đúng: giữ hoa thường, 0 đầu cổng; path ngoài ba nhóm; chỉ kiểm hình thức không kiểm truy cập được.

**Đối chiếu:** nhóm 3; K71, K24, K27; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm.

**Kiến thức/bẫy:** URL: giao thức/máy chủ/cổng; Nhóm bắt và không bắt; nhóm thừa đổi phần dữ liệu/shape được trả; extract lấy nhóm ở lần đầu, giữ index; kết quả số vẫn là chuỗi, không khớp không là 0. **Nguồn đọc lại:** RX câu 19, ô 92–96.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### B7-R20

**Đáp án: B.**

- A sai: tự giải mã %20 ngoài quy tắc.
- B đúng: giữ mã hóa, bỏ query/fragment khỏi path; URL không path hợp lệ nhận /, sai giao thức nhận None.
- C sai: để phần path ăn cả query/fragment như dùng .*.
- D sai: trả rỗng khi thiếu path, bỏ quy tắc mặc định /.

**Đối chiếu:** nhóm 3; K72, K22; mức Vận dụng. **Ưu tiên:** Luyện regex bổ sung; Trọng tâm ký hiệu đang dùng; bảng mở rộng tự học.

**Kiến thức/bẫy:** Đường dẫn URL, loại query/fragment; Lớp/tập/khoảng, lớp phủ định; +,* ,?,{m,n} tác động phần ngay trước. **Nguồn đọc lại:** RX câu 20, ô 97–101.

**Kiểm chứng:** Đã thực thi ca kiểm chứng cục bộ, các assert đạt.

### Độ bao phủ sau đợt 8

Đã dùng 72/72 mục tiêu. Không còn mục tiêu thiếu trong phạm vi đã xác định.

## Kiểm kê cuối bộ

- Đủ B7-001–B7-060: **60=40 TN+20 TL**, nhóm **10/10/20/14/6**, mức thiết kế **15/33/12**.
- Đủ B7-R01–B7-R20: **20=12 TN+8 TL**, tám đợt mỗi đợt mười câu.
- **72/72 mục tiêu** dùng để trả lời; đủ **20/20 dạng RX**. Câu tự luận ba phần gần cấu trúc GK câu 25 gồm 008,010,020,048 (và các biến thể khác).
- Đã rà câu trùng, giữ cặp đối chiếu có thay cơ chế/đơn vị hoặc quy tắc. Không dùng số khớp làm độ chính xác hay test hữu hạn làm chứng minh mọi đầu vào.
- **76/80 câu** đã thực thi ca kiểm chứng; **4 câu** đánh giá cơ chế/diễn giải kiểm bằng suy luận, ghi rõ từng câu. Không chạy toàn notebook TODO, không đo lại benchmark máy giảng viên, không tải dữ liệu thật.
- Phân biệt bài chính, tự học trong NB/LAB và luyện bổ sung RX. Độ bao phủ tài liệu không là tần suất thi hay dự báo chắc chắn đề thật.

## Đối chiếu 20 dạng luyện regex

| Dạng RX | Câu mới | Hình thức |
| --- | --- | --- |
| 1. Dãy chữ số ASCII đầu tiên | B7-R01 | TN |
| 2. Dấu chấm thường/wildcard | B7-R02 | TN |
| 3. Tập ký tự | B7-R03 | TN |
| 4. Khoảng ký tự | B7-R04 | TL |
| 5. Giới hạn số lần lặp | B7-R05 | TN |
| 6. Không lần/ít nhất một/tối thiểu | B7-R06 | TL |
| 7. Tùy chọn và dấu hỏi thường | B7-R07 | TN |
| 8. Ký tự trắng phân cách | B7-R08 | TL |
| 9. Tên PDF và nhóm bắt | B7-R09 | TN |
| 10. Số phòng/hoặc/ranh giới | B7-R10 | TL |
| 11. Số nguyên/thập phân đơn giản | B7-R11 | TN |
| 12. Nhóm nghìn và số mũ | B7-R12 | TL |
| 13. Mã vùng điện thoại/ngoặc đủ cặp | B7-R13 | TN |
| 14. Tài khoản email trước +filter | B7-R14 | TL |
| 15. Thẻ mở ngoài chú thích giản lược | B7-R15 | TN |
| 16. Tên ảnh/phần mở rộng | B7-R16 | TL |
| 17. Cắt dấu cách-tab và tham lam | B7-R17 | TL |
| 18. Log: phương thức/tệp/dòng | B7-R18 | TN |
| 19. URL: giao thức/máy chủ/cổng | B7-R19 | TN |
| 20. Đường dẫn URL, loại query/fragment | B7-R20 | TN |

## Biến thể bẫy và cặp đối chiếu

| Cơ chế/bẫy | Câu |
| --- | --- |
| Raw/escape/chấm | 002,021,027,R02 |
| contains/match/fullmatch/định dạng giá | 013,026,030,044,046,047 |
| replace mặc định/coerce/lỗi nguồn | 003,008,012,033,058 |
| Ngoặc \|/nhóm bắt/shape | 005,022,024,045,R10,R16 |
| Ranh giới và không khớp ≠ 0 | 009,015,019,032,035,R10 |
| Chuẩn hoá ngoài quy tắc | 006,038,042,057 |
| JSON/split/dấu phẩy/None | 004,014,020,048 |
| Explode/placeholder/đơn vị/mẫu số | 010,016,028,034,040,043,048,052 |
| Lặp mục/listing khác nhau | 010,020,028,036 |
| Từ khóa/địa điểm/cảm xúc/độ chính xác | 007,017,037,049 |
| Hiệu năng/backend/Unicode | 029,053,055,056,060 |
| Chuỗi rỗng hợp lệ/truthiness | 011,052,R17,R20 |

Các cặp đối chiếu chỉ đánh dấu ở đáp án: 003/012 (regex mặc định/bỏ chưa hết ký hiệu); 005/045 (thừa nhóm/không nhóm); 016/052 (placeholder/chuỗi rỗng thật); 010/048 (mẫu số đã biết/toàn bộ theo quy ước); R02/R17 (newline và loại ký tự trắng); 027/046 (dấu chấm/neo cuối).

## Dấu vết mục tiêu

| Mục tiêu | Câu thực sự sử dụng |
| --- | --- |
| K01 | B7-001 |
| K02 | B7-001, B7-006, B7-031, B7-038, B7-057 |
| K03 | B7-006, B7-038, B7-057 |
| K04 | B7-011, B7-033, B7-052, B7-R17 |
| K05 | B7-018 |
| K06 | B7-018, B7-021 |
| K07 | B7-021, B7-027, B7-R02 |
| K08 | B7-018, B7-053 |
| K09 | B7-053 |
| K10 | B7-042 |
| K11 | B7-011, B7-031 |
| K12 | B7-042, B7-054 |
| K13 | B7-031, B7-057 |
| K14 | B7-003, B7-012 |
| K15 | B7-008, B7-012, B7-023, B7-058 |
| K16 | B7-003, B7-008, B7-012, B7-033 |
| K17 | B7-008, B7-047, B7-058 |
| K18 | B7-026, B7-030, B7-047 |
| K19 | B7-026, B7-030, B7-044, B7-047, B7-R12 |
| K20 | B7-058 |
| K21 | B7-002, B7-027 |
| K22 | B7-041, B7-051, B7-R05, B7-R06, B7-R07, B7-R08, B7-R12, B7-R20 |
| K23 | B7-022, B7-R03, B7-R10 |
| K24 | B7-005, B7-024, B7-R09, B7-R13, B7-R14, B7-R16, B7-R19 |
| K25 | B7-002, B7-009, B7-019, B7-035, B7-060, B7-R10 |
| K26 | B7-013, B7-030, B7-046, B7-R04, B7-R11 |
| K27 | B7-009, B7-015, B7-019, B7-032, B7-039, B7-050, B7-R01, B7-R14, B7-R18, B7-R19 |
| K28 | B7-005, B7-045, B7-R16 |
| K29 | B7-022, B7-024, B7-R09, B7-R18 |
| K30 | B7-041, B7-051, B7-059 |
| K31 | B7-032, B7-050 |
| K32 | B7-007, B7-009, B7-015 |
| K33 | B7-019 |
| K34 | B7-035, B7-039 |
| K35 | B7-059, B7-R15 |
| K36 | B7-049 |
| K37 | B7-004, B7-014, B7-020 |
| K38 | B7-014 |
| K39 | B7-016, B7-028, B7-034, B7-040 |
| K40 | B7-016, B7-040, B7-052 |
| K41 | B7-020, B7-028, B7-036 |
| K42 | B7-010, B7-020, B7-025, B7-040, B7-043 |
| K43 | B7-010, B7-043, B7-048 |
| K44 | B7-010, B7-048 |
| K45 | B7-025, B7-043 |
| K46 | B7-028, B7-034, B7-048 |
| K47 | B7-017, B7-049 |
| K48 | B7-007, B7-037, B7-049 |
| K49 | B7-029, B7-056 |
| K50 | B7-055, B7-060, B7-R01 |
| K51 | B7-060 |
| K52 | B7-027, B7-046, B7-R02, B7-R17 |
| K53 | B7-R01 |
| K54 | B7-R02 |
| K55 | B7-R03 |
| K56 | B7-R04 |
| K57 | B7-R05 |
| K58 | B7-R06 |
| K59 | B7-R07 |
| K60 | B7-R08 |
| K61 | B7-R09 |
| K62 | B7-R10 |
| K63 | B7-R11 |
| K64 | B7-R12 |
| K65 | B7-R13 |
| K66 | B7-R14 |
| K67 | B7-R15 |
| K68 | B7-R16 |
| K69 | B7-R17 |
| K70 | B7-R18 |
| K71 | B7-R19 |
| K72 | B7-R20 |


Phân bố đáp án A: {'A': 10, 'B': 10, 'C': 10, 'D': 10}; phần B: {'A': 3, 'B': 3, 'C': 3, 'D': 3}.
