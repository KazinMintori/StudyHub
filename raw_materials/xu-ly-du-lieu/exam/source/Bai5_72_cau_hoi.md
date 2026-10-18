# BÀI 5 — SERIES & DATAFRAME CHUYÊN SÂU

Ngân hàng 72 câu: 60 trọng tâm và 12 tự học, chia sáu đợt.

## Nguồn đã đọc và thứ tự sử dụng

- **BG:** [bai-05-series-dataframe-chuyen-sau.md](<D:/LTXLDL_GK/Bài 5/bai-05-series-dataframe-chuyen-sau.md>), toàn văn gồm ghi chú giảng viên, code, bài tập và phần đọc thêm.
- **NB:** [lecture_05.ipynb](<D:/LTXLDL_GK/Bài 5/lecture_05.ipynb>), đủ 162 ô, gồm code và tự học. Chỉ số ô tham chiếu tính từ 0 trong JSON notebook.
- **LAB:** [lab_05.ipynb](<D:/LTXLDL_GK/Bài 5/lab_05.ipynb>), đủ 27 ô gồm TODO, assert và hai bài tự làm; không tuyên bố notebook chứa TODO đã chạy trọn vẹn.
- **PDF Bài 5:** [bản PDF 28 trang](<D:/LTXLDL_GK/Bài 5/bai-05-series-dataframe-chuyen-sau.pdf>), đã đọc và đối chiếu với BG; các phần trùng không được tính thành mục tiêu mới.
- **GK:** [Giữa kỳ luyện tập](<D:/LTXLDL_GK/Bài_kiểm_tra/2627I_UET.DSE2049 - Kiểm tra giữa kỳ (luyện tập) (1).pdf>), ưu tiên câu 10–13 và 23: ghép đúng đối tượng, thiếu dữ liệu, số cặp sau merge, qcut và sửa mask cấp nhóm. Đã đọc toàn bộ đề trong cùng cuộc làm việc và đọc lại trực tiếp các câu dùng hiệu chỉnh Bài 5.
- **AI5, DS1, DS2:** [LTXLDL_AI_5.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_5.pdf>), [LTXLDL_DS_1.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_1.pdf>), [LTXLDL_DS_2.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_2.pdf>) đã đọc toàn bộ trong cùng cuộc làm việc: tham khảo cách đặt tình huống, nhiễu có cơ chế và câu trả lời ngắn của Nguyễn Tuấn Phong. Không chuyển nội dung NumPy tuần 3 thành trọng tâm Bài 5.
- **AI1, AI2:** [LTXLDL_AI_1.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_1.pdf>), [LTXLDL_AI_2.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_2.pdf>) đã đọc toàn bộ trong cùng cuộc làm việc, chỉ bổ trợ diễn đạt/suy luận. Hai tệp ghi Đào Việt Anh, không gán nhầm tác giả.

Không thiếu nguồn được yêu cầu. Không tải snapshot Santiago hay chạy benchmark thật: câu dùng bảng giả lập độc lập, tính tay được. Không tuyên bố đọc toàn bộ sách/website liên kết ngoài các tệp nguồn. Không mở rộng sang SQL, API, regex, thời gian, pipe hoặc MultiIndex nâng cao.

**Ranh giới trọng tâm/tự học:** pivot_table có ở NB tự học nhưng LAB bước 5 là thực hành chính, nên được đánh giá trong câu trọng tâm. reindex, chỉ mục lặp và duplicated, apply axis=0, map với Series, reset_index giữ nhãn tự học theo NB/BG; tìm top theo transform max và cơ cấu quận thuộc LAB tự làm nên đặt ở phần bổ sung. Phép kiểm is_unique cơ bản vẫn là trọng tâm vì xuất hiện ở BG §1. stack chỉ được nhắc như tên thao tác ngược trong ghi chú BG, không có bài thực hành hay mục tiêu riêng; ngân hàng không thêm bài API stack ngoài nội dung minh hoạ.


## Giả định và quy ước

- Giả định pandas **3.0.x**, ưu tiên ngữ nghĩa 3.0.3 theo NB. Môi trường thực thi: **pandas 3.0.1, NumPy 2.3.5, Python 3.12.14**. Không tuyên bố đã kiểm riêng trên 3.0.3.
- Mỗi câu khởi tạo dữ liệu riêng; đã có `import pandas as pd` và `import numpy as np`. Thực hiện đúng thứ tự, chỉ chạy lại những dòng đề nói rõ. Giá và số liệu đều giả lập.
- Một listing là một chỗ ở; host là chủ nhà; review là một đánh giá; listing–snapshot là một chỗ ở ở một đợt. Mỗi câu nêu đơn vị quan sát, phạm vi nhóm và đơn vị giá nếu liên quan. Khóa nhóm/merge không thiếu, trừ câu ghi khác; các chỉ mục dùng alignment là duy nhất, trừ phần tự học ghi rõ lặp.
- NaN là thiếu số, không tự coi là 0; số thực có `np.nan` dùng float64. Không yêu cầu dạng in dtype chuỗi, khoảng trắng hoặc thứ tự chưa quy định. Nếu cần thứ tự, dùng danh sách nhãn, sort hoặc truy cập theo nhãn trong đề.
- cut luôn chỉ rõ bins, labels, right. qcut dùng các dữ liệu không trùng mốc gây lỗi ngoài mục tiêu; so giữa kỳ trên cùng tập listing không làm tròn, trừ câu cố ý thay thành phần.
- Khi có categorical, ghi observed rõ nếu ảnh hưởng nhóm; không đưa bẫy khóa thiếu của SQL vào pandas. Với top, giữ mọi đồng hạng nếu đề yêu cầu.
- Nhận đáp án số thực sai số tuyệt đối `1e-12`, trừ câu ghi mức khác. Với thiếu, kiểm bằng isna/notna; không kiểm `NaN == NaN`.
- Mỗi TN đúng duy nhất một lựa chọn, có thể chấm 1 điểm; TL có thang riêng 2 hoặc 3 điểm. Nhận lời giải tương đương đúng giá trị, nhãn, đơn vị và ý nghĩa; không trừ vì có cách khác gọn hơn.

## Ma trận và kế hoạch sáu đợt

Đây là tham số thiết kế, không phải tần suất chính thức hay độ khó đã đo thực nghiệm. Mỗi câu có một nhóm chính và tối đa hai mục tiêu phụ.

| Nhóm chính | Tổng | TN | TL | Nền tảng | Vận dụng | Phân loại |
| --- | --- | --- | --- | --- | --- | --- |
| Khớp nhãn, phép tính và phép gán Series | 10 | 7 | 3 | 6 | 1 | 3 |
| map, apply, phép toán cột, cut/qcut | 12 | 9 | 3 | 2 | 10 | 0 |
| groupby, agg, transform, filter và bảng tổng hợp | 16 | 10 | 6 | 2 | 11 | 3 |
| concat, merge và kiểm chứng phép ghép | 14 | 9 | 5 | 4 | 5 | 5 |
| assign và phân tích có thể chạy lại | 8 | 5 | 3 | 1 | 6 | 1 |

| Đợt | Trọng tâm | TN/TL | Nền tảng/Vận dụng/Phân loại | Tự học | TN/TL |
| --- | --- | --- | --- | --- | --- |
| 1 | B5-001–B5-010 | 7/3 | 3/5/2 | MR01–MR02 | 2/0 |
| 2 | B5-011–B5-020 | 7/3 | 3/5/2 | MR03–MR04 | 1/1 |
| 3 | B5-021–B5-030 | 7/3 | 3/5/2 | MR05–MR06 | 2/0 |
| 4 | B5-031–B5-040 | 7/3 | 2/6/2 | MR07–MR08 | 1/1 |
| 5 | B5-041–B5-050 | 6/4 | 2/6/2 | MR09–MR10 | 1/1 |
| 6 | B5-051–B5-060 | 6/4 | 2/6/2 | MR11–MR12 | 1/1 |

## Danh mục mục tiêu K và mã câu dự kiến

Lập trước khi biên soạn; các mã trong cột câu bỏ tiền tố B5-. Chỉ tính bao phủ nếu phải dùng để giải câu, không chỉ xuất hiện trong lời giải.

| Mã | Mục tiêu | Ưu tiên | Câu dự kiến | Nguồn đọc lại |
| --- | --- | --- | --- | --- |
| K01 | Phép toán Series ghép đúng mã dù đảo thứ tự | Trọng tâm | 001,021 | BG §1; NB ô 6–10; LAB W2 |
| K02 | Hợp nhãn trong phép toán; thiếu toán hạng khác giá bằng 0 | Trọng tâm | 006,030 | BG §1; NB ô 11–13 |
| K03 | to_numpy bỏ nhãn; cùng độ dài vẫn có thể ghép sai đối tượng | Trọng tâm | 011,018 | BG §1; NB ô 6–10; GK câu 10 |
| K04 | set_index không bảo đảm mã duy nhất; kiểm index.is_unique | Trọng tâm | 031 | BG §1; NB ô 14–16 |
| K05 | Gán Series căn theo index bảng; giữ hàng bảng, thêm NaN nhưng không thêm nhãn mới | Trọng tâm | 041,030 | BG §1; NB ô 17–20 |
| K06 | Tên index khác giá trị nhãn dùng để khớp | Trọng tâm | 051 | BG §1 ghi chú gán cột |
| K07 | Gán list/ndarray theo vị trí; RHS Series dài hơn có thể khớp nhưng ndarray lỗi độ dài | Trọng tâm | 050,011 | BG §1; suy ra từ alignment; GK câu 10 |
| K08 | map dict tra theo giá trị khác gán Series căn theo index | Trọng tâm | 002,022 | BG §2; NB ô 23–27 |
| K09 | Thiếu bảng phí là chưa biết; sum/count/len sau map dùng tập giá trị khác nhau | Trọng tâm | 007,022 | BG §2; NB ô 26–27; GK câu 11 |
| K10 | map hàm phân loại: xử lý NaN trước if/elif/else và đúng biên | Trọng tâm | 012,038 | LAB bước 1, ô 8–9 |
| K11 | apply axis=1 nhận hàng Series; scalar tạo Series giữ index | Trọng tâm | 016 | BG §2; NB ô 28–35 |
| K12 | Phép toán trực tiếp trên cột và apply: tính đúng trước hiệu năng; không tự vector hoá hàm Python | Trọng tâm | 052,047 | BG §2; NB ô 33–41 |
| K13 | Tiền nhiều đêm, phí một lần, miễn phí từ đúng 7 đêm; lan truyền thiếu theo nghiệp vụ | Trọng tâm | 047,022 | BG §2 bài tập 2; NB ô 42–45 |
| K14 | cut ngưỡng đặt trước, right=False, nhóm giá hợp lệ khác NaN | Trọng tâm | 026,057 | BG §2; NB ô 46–52; LAB bước 1 |
| K15 | qcut dùng phân vị tập hiện tại; gần cân bằng số lượng khác đều độ rộng giá | Trọng tâm | 032 | BG §2; NB ô 46–52 |
| K16 | Cùng tập đối tượng biến đổi affine dương: nhóm qcut giữ, mốc đổi; giới hạn khi đổi thành phần | Trọng tâm | 042,057 | BG §2; NB ô 50–52; GK câu 13 |
| K17 | Thống nhất đơn vị tiền và quy ước ngưỡng khi so mốc chụp | Trọng tâm | 057,010 | BG §2,5; LAB bước 1 |
| K18 | Split–apply–combine; hàng cùng nhóm không cần liên tiếp; mean/median bỏ giá thiếu | Trọng tâm | 003,013 | BG §3; NB ô 53–61 |
| K19 | size đếm hàng, count đếm giá biết, nunique đếm đối tượng khác nhau | Trọng tâm | 013,015 | BG §3; LAB bước 2; GK câu 23 |
| K20 | agg trên Series và named aggregation nhiều cột; một hàng mỗi nhóm | Trọng tâm | 027,013 | BG §3; NB ô 60,90; LAB bước 2 |
| K21 | Nhiều khóa, dạng dài/rộng, unstack; tổ hợp không có dữ liệu khác số 0 | Trọng tâm | 043 | BG §3; NB ô 69–75 |
| K22 | Gộp mean phải dùng count đúng trọng số; không gộp median bằng công thức mean | Trọng tâm | 008,033 | BG §3 bài tập 3; NB ô 67–68 |
| K23 | transform trả từng hàng, giữ index sau lọc; hàng thiếu giá vẫn nhận thống kê nhóm | Trọng tâm | 023,029 | BG §3; NB ô 76–88 |
| K24 | Thống kê/mask cấp nhóm khác cấp hàng; căn nhãn sai tạo NaN hoặc mask lỗi IndexingError | Trọng tâm | 019,049 | BG §3; GK câu 23 |
| K25 | Review/snapshot khác listing; nunique khác size; chọn đúng khóa khi tính độ lệch | Trọng tâm | 015,019,029 | BG §3 ghi chú đơn vị; GK câu 23 |
| K26 | GroupBy.filter nhận cả nhóm, trả bool và giữ các hàng gốc của nhóm đạt điều kiện | Trọng tâm | 036,049 | BG §3; NB ô 82–85 |
| K27 | Lọc trước thống kê khác thống kê toàn nhóm rồi lọc; transform size chỉ biết phạm vi bảng hiện tại | Trọng tâm | 039,020 | BG §3,5; NB ô 94,137–144 |
| K28 | Tỷ lệ listing thuộc host chuyên nghiệp khác tỷ lệ host; trọng số listing khác host ngang nhau | Trọng tâm | 046 | BG §3; NB ô 89–92; LAB bước 3 |
| K29 | Dựng lại cột đếm nhà cung cấp; lệch phạm vi chưa chứng minh nguồn sai | Trọng tâm | 053,039 | BG §3; NB ô 93–95 |
| K30 | pivot_table: index/columns/values/aggfunc; mean mặc định khác size/count/sum | Trọng tâm | 058 | LAB bước 5, ô 18–20; NB ô 156–157 |
| K31 | Review là proxy, bảng chéo và chênh lệch chưa chứng minh nhân quả/đắt vô lý | Trọng tâm | 058,029 | LAB bước 2–5; BG §3 |
| K32 | concat thêm quan sát, khớp tên cột; ignore_index không khử mã trùng | Trọng tâm | 004,024 | BG §4; NB ô 97–100 |
| K33 | Mỗi hàng listing–snapshot; lặp id giữa hai đợt có thể hợp lệ | Trọng tâm | 009,024 | BG §4; NB ô 98–100 |
| K34 | merge theo giá trị khóa, không theo thứ tự hay index; khác concat | Trọng tâm | 014 | BG §4; NB ô 101–106 |
| K35 | Mặc định inner; giữ cặp khớp khác left giữ hàng chưa khớp | Trọng tâm | 017,028 | BG §4; NB ô 113–115 |
| K36 | Khóa lặp hai phía tạo các cặp; left có thể tăng hàng; đếm bằng bội số từng khóa | Trọng tâm | 034,028,040 | BG §4; NB ô 116–126; GK câu 12 |
| K37 | validate m:1 kiểm khóa phải duy nhất, cho phép khóa trái lặp; không sửa hay chọn dòng hộ | Trọng tâm | 037,048 | BG §4; NB ô 119–124; LAB bước 6 |
| K38 | indicator both/left_only; NaN bên phải có thể đã khớp nhưng thiếu thông tin | Trọng tâm | 044,059 | BG §4; NB ô 107–112 |
| K39 | validate và len bằng nhau không bảo đảm mọi khóa khớp hay thông tin đủ/đúng | Trọng tâm | 056,059 | BG §4 ghi chú validate/indicator; LAB bước 6 |
| K40 | Ghép host về listing theo nhiều–một; nhân hàng làm lệch tổng, tỷ lệ, trọng số | Trọng tâm | 054,040 | BG §4; NB ô 122–124 |
| K41 | Không tự drop_duplicates ép số hàng khi chưa biết bản ghi đúng; kiểm số hàng/khóa/độ khớp | Trọng tâm | 048,059 | BG §4 ghi chú khóa lặp; LAB bước 6 |
| K42 | assign trả bảng mới; đầu vào giữ nguyên trong cách dùng đúng | Trọng tâm | 005 | BG §5; NB ô 132–135 |
| K43 | Chạy lại cập nhật đơn vị trên kết quả cũ tiếp tục chia; assign không tự chống lỗi này | Trọng tâm | 010,020 | BG §5; NB ô 128–135 |
| K44 | Callable assign nhận bảng hiện tại; truyền hàm khác gọi hàm thiếu đối số; dùng cột vừa thêm | Trọng tâm | 025,035 | BG §5; NB ô 136–141 |
| K45 | Cột phụ thuộc phải tính lại từ nguồn đúng sau khi cột nguồn đổi | Trọng tâm | 045 | BG §5; NB ô 142–144 |
| K46 | Chuỗi lọc → assign → groupby → agg từ đầu vào cố định; observed=True chỉ giữ nhóm phân loại xuất hiện | Trọng tâm | 055 | BG §5; NB ô 142–144 |
| K47 | Hàm trong chuỗi phải không sửa lén đầu vào hoặc trạng thái ngoài; kiểm chạy hai lần và bảng gốc | Trọng tâm | 060 | BG §5; NB ô 136–144 |
| K48 | Kiểm logic mệnh đề assert; assert qua chưa chứng minh toàn bộ yêu cầu | Trọng tâm | 060 | LAB ô 4; BG kiểm chứng AI |
| K49 | reindex theo danh sách nhãn, thêm nhãn mới nhận thiếu | Tự học/đọc thêm | MR01,MR09 | NB ô 146–147 |
| K50 | Chỉ mục lặp: loc một nhãn trả nhiều phần tử; is_unique | Tự học/đọc thêm | MR02 | NB ô 148–149 |
| K51 | index.duplicated giữ lần đầu mặc định; set_index không khử mã lặp | Tự học/đọc thêm | MR06 | NB ô 150–151 |
| K52 | apply axis=0 nhận cột; tên/nhãn đầu ra là cột, khác axis=1 | Tự học/đọc thêm | MR03,MR11 | NB ô 152–153 |
| K53 | map bằng Series thống kê nhóm đưa giá trị về từng hàng; khác gán trực tiếp Series nhóm | Tự học/đọc thêm | MR04,MR12 | NB ô 154–155 |
| K54 | reset_index tạo bảng mới, đưa khóa nhóm thành cột và giữ khóa khi xuất index=False | Tự học/đọc thêm | MR05,MR10 | BG §3 tự học; NB ô 62–63 |
| K55 | transform max chọn top mỗi quận, đồng hạng có thể nhiều listing | Tự học/đọc thêm | MR07 | LAB tự làm 1, ô 24 |
| K56 | value_counts normalize theo từng quận; mẫu số và thiếu; khác tỷ lệ toàn thành phố | Tự học/đọc thêm | MR08 | LAB tự làm 2, ô 24 |

## Đợt 1

### Câu trọng tâm

#### B5-001

Mỗi nhãn là mã một listing; giá giả lập USD/đêm:
```python
cu = pd.Series([30., 70., 50.], index=['L1','L2','L3'])
moi = pd.Series([55., 40., 60.], index=['L3','L1','L2'])
r = moi - cu
print(r.loc[['L1','L2','L3']].tolist())
```
Dòng cuối cho các giá trị nào?

A. `[10,-10,5]`

B. `[25,-30,10]`

C. `[5,10,-10]`

D. `[-10,10,-5]`

#### B5-002

Mỗi hàng là một listing:
```python
d = pd.DataFrame({'loai':['can','phong','khac','can']},
                 index=['phong','can','x','y'])
d['phi'] = d['loai'].map({'can':12., 'phong':5.})
```
Phí của hàng mang nhãn `phong` là gì?

A. `5`

B. `12`

C. ValueError vì bảng tra có 2 khóa nhưng d có 4 hàng.

D. KeyError ở loại khac nên không tạo được cột phi.

#### B5-003

Mỗi hàng là một listing, USD/đêm:
```python
d = pd.DataFrame({'khu':['A','B','A','B'],
                  'gia':[20.,40.,np.nan,80.]})
t = d.groupby('khu', sort=True)['gia'].mean()
```
Nhận định nào đúng?

A. A=10, B=60; mỗi khu chia cho số hàng.

B. A=20, B=60; t vẫn có 4 phần tử, mỗi listing một giá trị.

C. Báo lỗi vì các hàng A không đứng liền nhau.

D. `t['A']=20`, `t['B']=60`; t có 2 phần tử, mỗi phần tử cho một khu.

#### B5-004

Mỗi hàng là một listing trong một đợt thu thập:
```python
a = pd.DataFrame({'id':['P','Q'], 'gia':[10.,20.], 'dot':[1,1]})
b = pd.DataFrame({'dot':[2,2], 'gia':[30.,40.], 'id':['P','R']})
c = pd.concat([a,b], ignore_index=True)
```
Nhận định nào đúng về c?

A. Có 3 hàng vì ignore_index xoá id P lặp.

B. Có 4 hàng nhưng P đợt 2 nhận gia bằng 2.

C. Có 2 hàng vì concat ghép hai bảng theo id.

D. Có 4 hàng, index 0–3; P xuất hiện hai lần và giá đợt 2 của P là 30.

#### B5-005

Mỗi hàng là một listing, price tính bằng CLP/đêm:
```python
goc = pd.DataFrame({'price':[40000.,80000.]})
moi = goc.assign(gia_nghin=goc['price']/1000)
print(goc.shape, moi.shape, moi['gia_nghin'].tolist())
```
Dòng cuối có kết quả nào?

A. `(2,1), (2,2), [40,80]`

B. `(2,2), (2,2), [40,80]`

C. `(2,1), (2,1), [40,80]`

D. `(2,1), (2,2), [40000,80000]`

#### B5-006

Nhãn là mã listing, giá USD/đêm:
```python
cu = pd.Series([10.,20.,30.], index=['A','B','C'])
moi = pd.Series([25.,50.,12.], index=['B','D','A'])
r = moi - cu
```
Những nhãn nào của r nhận NaN và vì sao?

A. Chỉ D, vì giữ các nhãn của moi.

B. Không nhãn nào; C=−30 và D=50.

C. C và D; phép trừ lấy hợp A,B,C,D, nhưng thiếu một toán hạng tại C,D.

D. C và D không xuất hiện vì chỉ lấy giao nhãn.

#### B5-007

Mỗi hàng là một listing; phí một lần, USD:
```python
loai = pd.Series(['can','mien','la','can'])
phi = loai.map({'can':15., 'mien':0.})
print(phi.sum(), phi.count(), len(phi))
```
Ba giá trị được in ra là gì?

A. `30,2,4`

B. `30,3,4`

C. `NaN,3,4`

D. `30,4,4`

#### B5-008

Mỗi hàng của bảng tổng hợp là một khu; các mean/count dưới đây chính xác. Giá USD/đêm:

| Khu | mean giá đã biết | count giá đã biết | size tất cả listing |
| --- | --- | --- | --- |
| A | 40 | 2 | 5 |
| B | 100 | 4 | 4 |

Tính mean của toàn bộ giá đã biết. Vì sao dùng trọng số size hoặc lấy mean hai số 40,100 sai? Nếu thay cột mean bằng median, công thức gộp tương tự có luôn đúng không?

#### B5-009

Mỗi hàng dưới là một listing–snapshot, không phải một listing duy nhất:
```python
a = pd.DataFrame({'id':['P','Q'], 'dot':[1,1], 'gia':[10.,20.]})
b = pd.DataFrame({'id':['P','R'], 'dot':[2,2], 'gia':[30.,40.]})
d = pd.concat([a,b], ignore_index=True)
m = d.merge(d[['id']], on='id', how='left')
```
Không cần viết toàn bộ m: có bao nhiêu hàng và m['gia'].sum() bằng bao nhiêu? Đếm cặp khớp theo id. Một bạn nói ignore_index đã làm id duy nhất nên phép ghép không thể tăng hàng: sai ở đâu?

#### B5-010

Mỗi hàng là một listing, price nguồn tính bằng CLP/đêm:
```python
d = pd.DataFrame({'price':[40000.,80000.]})
d = d.assign(price=d['price']/1000)
```
Sau đó chỉ chạy lại đúng dòng assign một lần nữa, không khởi tạo lại d.
(a) Giá hai hàng sau lần chạy lại là gì và còn được gọi là CLP/đêm không?
(b) Viết cách tạo cột giá nghìn CLP từ bảng nguồn goc cố định mà giữ price gốc.
(c) Nêu cách kiểm chạy lại và vì sao đổi tên biến kết quả thôi chưa đủ nếu vẫn dùng đầu vào đã chia.

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR01

Giá theo mã listing:
```python
s = pd.Series([20.,50.], index=['A','B'])
r = s.reindex(['B','C','A'])
```
Giá trị r theo thứ tự nhãn đã yêu cầu là gì?

A. `[20,50,NaN]`

B. `[50,NaN,20]`

C. `[50,0,20]`

D. Báo KeyError vì C không có trong s.

#### B5-MR02

Mỗi hàng là một snapshot giá, nên mã listing có thể lặp:
```python
s = pd.Series([10.,30.,50.], index=['A','B','A'])
r = s.loc['A']
```
r và s.index.is_unique là gì?

A. r là scalar 10, is_unique=True.

B. r là scalar 60, is_unique=False.

C. r là Series hai giá `[10,50]`, is_unique=False.

D. Lệnh tạo s báo lỗi nên không có r.

### Độ bao phủ sau đợt 1

Đã dùng 17/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K03, K05, K06, K07, K10, K11, K12, K13, K14, K15, K16, K20, K21, K23, K24, K25, K26, K27, K28, K29, K30, K31, K34, K35, K37, K38, K39, K41, K44, K45, K46, K47, K48, K51, K52, K53, K54, K55, K56. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 2

### Câu trọng tâm

#### B5-011

Mỗi hàng là một listing; phí USD đã gắn với mã trong s:
```python
d = pd.DataFrame({'gia':[70.,30.]}, index=['B','A'])
s = pd.Series([5.,10.], index=['A','B'])
d['phi'] = s.to_numpy()
print(d.loc[['A','B'],'phi'].tolist())
```
Kết quả và nhận xét nào đúng?

A. `[5,10]`; to_numpy vẫn giữ nhãn để căn chỉnh.

B. Báo ValueError vì index d khác thứ tự s.

C. `[10,5]`; không lỗi độ dài nhưng gán sai mã vì ndarray dùng vị trí.

D. `[NaN,NaN]`; mảng không có index nên không gán được.

#### B5-012

Mỗi giá là của một listing, cùng đơn vị USD/đêm:
```python
def nhom(x):
    if x < 30: return 're'
    elif x < 100: return 'trung'
    else: return 'cao'
s = pd.Series([20.,30.,100.,np.nan])
r = s.map(nhom)
```
Nhận định nào đúng?

A. r là `[re,trung,cao,NaN]` vì map tự bỏ qua mọi NaN.

B. r là `[re,re,trung,cao]`.

C. Dừng ở NaN vì if luôn gây ngoại lệ khi x thiếu.

D. r là `[re,trung,cao,cao]`; giá thiếu bị gán cao mà không báo lỗi.

#### B5-013

Mỗi hàng là một listing, USD/đêm:
```python
d = pd.DataFrame({'khu':['A','B','A','B','A'],
                  'gia':[10.,np.nan,30.,60.,np.nan]})
t = d.groupby('khu')['gia'].agg(tb='mean', n='size', co_gia='count')
```
Bộ ba `(tb,n,co_gia)` của khu A là gì?

A. `(20,3,2)`

B. `(40/3,3,3)`

C. `(20,2,3)`

D. `(20,2,2)`

#### B5-014

Mỗi hàng d là một listing; bảng tra có một phí cho mỗi khu, USD:
```python
d = pd.DataFrame({'id':['P','Q','R'], 'khu':['B','A','C']}, index=[9,2,7])
phi = pd.DataFrame({'khu':['C','B','A'], 'phi':[30.,20.,10.]})
m = d.merge(phi, on='khu', how='left', sort=False)
print(m['phi'].tolist())
```
Dòng cuối cho gì?

A. `[30,20,10]`

B. `[20,10,30]`

C. `[NaN,NaN,NaN]`

D. `[10,20,30]`

#### B5-015

Mỗi hàng là một review; một listing có thể có nhiều review:
```python
d = pd.DataFrame({'khu':['A','A','A','B','B','B'],
                  'id':['P','P','Q','R','R','R']})
n = d.groupby('khu')['id'].nunique()
```
Nếu chỉ giữ các khu có từ 2 listing khác nhau trở lên, khu nào đạt và vì sao?

A. n[A]=3, n[B]=3; cả A,B đạt.

B. n[A]=1, n[B]=0; không khu nào đạt.

C. n[A]=2, n[B]=1; cả A,B đạt.

D. n[A]=2, n[B]=1; chỉ A đạt.

#### B5-016

Mỗi hàng là một lượt ở; gia USD/đêm, phi thu một lần USD:
```python
d = pd.DataFrame({'gia':[20.,30.,40.], 'phi':[5.,np.nan,0.]},
                 index=['R3','R1','R2'])
def tien(hang): return 2*hang['gia'] + hang['phi']
r = d.apply(tien, axis=1)
```
Mô tả nào đúng?

A. Hàm nhận từng cột; r có index gia,phi.

B. Hàm nhận một số duy nhất; r là DataFrame ba hàng hai cột.

C. r là `[50,60,80]`, vì phí được thu mỗi đêm và NaN coi là 0.

D. Hàm nhận từng hàng Series; r là Series index R3,R1,R2 với giá trị `[45,NaN,80]`.

#### B5-017

Mỗi hàng là một listing; vùng có khóa duy nhất:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'khu':['A','B','C','A']})
v = pd.DataFrame({'khu':['A','B'], 'vung':['Bac','Nam']})
m = d.merge(v, on='khu')
```
m có bao nhiêu hàng, listing nào mất?

A. 4 hàng; R được giữ với NaN vì mặc định left.

B. 3 hàng; R mất vì merge mặc định inner và C không khớp.

C. 2 hàng; mỗi khu phải chỉ xuất hiện một lần.

D. 8 hàng; mỗi listing ghép mọi vùng.

#### B5-018

Mỗi nhãn là một listing, giá USD/đêm:
```python
d = pd.DataFrame({'gia':[30.,10.,60.]}, index=['C','A','B'])
moi = pd.Series([90.,40.,20.], index=['B','C','A'])
d['lech'] = (moi-d['gia']).to_numpy()
```
(a) Code có lỗi độ dài không? Cho lech theo thứ tự A,B,C hiện tại.
(b) Sửa dòng gán để tăng giá của mỗi mã ghép đúng mã đó.
(c) Cho kết quả đúng và cách thử bằng đảo thứ tự hàng.

#### B5-019

Mỗi hàng là một listing–snapshot, giá USD/đêm. Cần giữ snapshot thuộc khu có ít nhất 2 listing khác nhau, rồi so giá với mean của chính listing qua các snapshot được giữ:
```python
d = pd.DataFrame({'id':['P','P','Q','R','R','R'],
 'khu':['A','A','A','B','B','B'], 'gia':[20.,40.,80.,30.,50.,70.]},
 index=[10,20,30,40,50,60])
du = d.loc[d.groupby('khu')['id'].nunique() >= 2]
```
(a) Vì sao dòng cuối lỗi? (b) Sửa thao tác lọc. (c) Thêm cột lech đúng yêu cầu và cho kết quả theo index được giữ.

#### B5-020

Mỗi hàng nguồn goc là một listing; giá USD/đêm:
```python
goc = pd.DataFrame({'id':['P','Q','R','S'], 'host':['H','H','H','K'],
                    'gia':[10.,np.nan,30.,20.]})
co = goc.loc[goc['gia'].notna()].assign(
    n_host=lambda d: d.groupby('host')['id'].transform('size'))
```
Cho n_host theo P,R,S. Chạy lại cả lệnh tạo co từ goc cố định có ổn định không? Một bạn cho rằng ổn định chứng minh H chỉ có 2 listing trong toàn bộ goc: đúng không? Muốn đếm trên toàn goc rồi mới bỏ giá thiếu thì đổi thứ tự thế nào?

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR03

Mỗi hàng là một listing:
```python
d = pd.DataFrame({'gia':[10.,20.,30.], 'phi':[0.,np.nan,5.]})
def mota(cot): return cot.count()
r = d.apply(mota, axis=0)
```
Nhãn và giá trị của r là gì?

A. Index 0,1,2; giá trị `[2,1,2]`.

B. Index gia,phi; giá trị `[3,3]`.

C. Index 0,1; giá trị `[3,2]`.

D. Index gia,phi; giá trị `[3,2]`.

#### B5-MR04

Mỗi hàng là một listing, giá USD/đêm:
```python
d = pd.DataFrame({'khu':['B','A','B','A'], 'gia':[10.,20.,50.,np.nan]},
                 index=[7,2,9,5])
tb = d.groupby('khu')['gia'].mean()
```
Viết một lệnh dùng map với tb để tạo cột tb_khu theo từng hàng. Cho giá trị và index kết quả; vì sao gán thẳng `d['tb_khu']=tb` không tương đương? Hàng index 5 thiếu giá có nhận được tb_khu không?

### Độ bao phủ sau đợt 2

Đã dùng 30/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K05, K06, K12, K13, K14, K15, K16, K21, K26, K28, K29, K30, K31, K37, K38, K39, K41, K44, K45, K46, K47, K48, K51, K54, K55, K56. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 3

### Câu trọng tâm

#### B5-021

Mỗi nhãn ban đầu là đúng mã listing, USD/đêm:
```python
cu = pd.Series([40.,80.], index=['A','B'])
moi = pd.Series([100.,30.], index=['B','A'])
moi.index = cu.index
r = moi-cu
```
Đổi nhãn như trên có sửa được lỗi thứ tự không?

A. Có; r tự khôi phục A=−10,B=20 từ nhãn ban đầu.

B. Không; r là A=60,B=−50 nhưng đã ghép sai listing.

C. Có; chỉ cần hai Series có cùng số phần tử.

D. Không; pandas báo lỗi ngay khi thay index bằng một index cùng độ dài.

#### B5-022

Mỗi hàng là một lượt ở hai đêm; gia USD/đêm, phí thu một lần USD:
```python
d = pd.DataFrame({'loai':['can','phong','la'], 'gia':[20.,50.,30.]})
d['phi'] = d['loai'].map({'can':0., 'phong':5.})
d['tong'] = 2*d['gia'] + d['phi']
```
Nhận định nào đúng?

A. tong là `[40,105,60]` vì map tự điền 0 cho mọi loại lạ.

B. tong là `[40,105,NaN]`; chưa thể khẳng định lượt loại la chỉ tốn 60.

C. tong là `[40,110,NaN]`.

D. tong là `[NaN,105,NaN]` vì phí 0 được coi là thiếu.

#### B5-023

Mỗi hàng là một listing sau lọc, giá USD/đêm:
```python
d = pd.DataFrame({'khu':['A','A','B','A'], 'gia':[10.,np.nan,80.,50.]},
                 index=[8,2,10,5])
t = d.groupby('khu')['gia'].transform('mean')
```
Giá trị t tại nhãn 2 và index của t là gì?

A. 30; index `[8,2,10,5]`.

B. NaN; index `[8,2,10,5]`.

C. 30; index `[0,1,2,3]`.

D. 30; index `[A,B]`.

#### B5-024

Mỗi hàng là một listing–snapshot; gia USD/đêm, phi USD:
```python
a = pd.DataFrame({'id':['P','Q'], 'dot':[1,1], 'gia':[10.,30.]})
b = pd.DataFrame({'id':['P','R'], 'dot':[2,2], 'phi':[5.,8.]})
c = pd.concat([a,b], ignore_index=True)
```
c có shape nào và `c['gia'].mean()` bằng bao nhiêu?

A. `(3,4)` và 20.

B. `(4,4)` và 20.

C. `(4,4)` và 10.

D. `(4,3)` và 13.25.

#### B5-025

Mỗi hàng là một listing; giá USD/đêm:
```python
d = pd.DataFrame({'gia':[10.,20.]})
r = d.assign(hai=lambda t: 2*t['gia'],
             tong=lambda t: t['hai']+5)
```
tong là gì, hàm phía sau có thấy cột hai không?

A. Báo KeyError vì assign gọi mọi hàm trên bảng ban đầu chưa có hai.

B. `[15,25]`; tong luôn dùng gia gốc thay hai.

C. `[25,45]`; có, callable sau nhận bảng đang có cột hai vừa thêm.

D. `[25,45]`; d cũng được thêm cả hai và tong.

#### B5-026

Mỗi giá USD/đêm thuộc một listing:
```python
s = pd.Series([0.,30.,99.,100.,np.nan])
r = pd.cut(s, bins=[0,30,100,np.inf], labels=['re','trung','cao'],
           right=False)
```
Giá 0,30,100 và giá thiếu lần lượt thuộc nhóm nào?

A. re, trung, cao, thiếu.

B. re, trung, trung, thiếu.

C. re, re, cao, thiếu.

D. re, trung, cao, re.

#### B5-027

Mỗi hàng là một listing; gia USD/đêm, review là số đánh giá trong năm:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'host':['H','H','K','K'],
 'gia':[10.,np.nan,20.,40.], 'review':[0.,4.,np.nan,6.]})
t = d.groupby('host').agg(n=('id','size'), tv=('gia','median'),
                         rv=('review','mean'))
```
Bộ ba `(n,tv,rv)` tại host H là gì và một hàng t đại diện cho gì?

A. `(1,10,2)`; một host.

B. `(2,5,2)`; một host.

C. `(2,10,2)`; một host.

D. `(2,10,4)`; một host.

#### B5-028

Mỗi hàng d là một listing; bảng phi có thể có nhiều bản ghi cho một khu:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'khu':['A','B','A','C']})
phi = pd.DataFrame({'khu':['A','A','B'], 'phi':[1.,np.nan,2.]})
m = d.merge(phi, on='khu', indicator=True)
```
Cần giữ mọi listing kể cả chưa tìm được khu.
(a) m hiện tại có mấy hàng và mất listing nào? (b) Sửa phép ghép theo yêu cầu, dự đoán số hàng mới. (c) Trong kết quả sửa, có bao nhiêu phi thiếu, bao nhiêu left_only? Giải thích chênh lệch bằng cặp khớp.

#### B5-029

Mỗi hàng là một listing, gia USD/đêm. Chỉ xét nguyên căn (can), mỗi listing cần so với mean các nguyên căn trong chính khu:
```python
d = pd.DataFrame({'host':['H','H','K','K'], 'khu':['A','B','A','B'],
 'loai':['can','can','can','phong'], 'gia':[20.,100.,40.,500.]})
x = d.loc[d['loai']=='can'].copy()
x['lech'] = x['gia']-x.groupby('host')['gia'].transform('mean')
```
Cho lech hiện tại theo index 0,1,2; sửa dòng cuối đúng yêu cầu và cho kết quả đúng. Có thể kết luận listing lệch dương là “đắt không hợp lý” không?

#### B5-030

Mỗi hàng d là một listing; giá và phí USD:
```python
d = pd.DataFrame({'gia':[10.,20.,30.]}, index=['A','B','C'])
phi = pd.Series([1.,2.,3.], index=['B','D','E'])
r = d['gia']+phi
d['tong'] = r
```
r có bao nhiêu nhãn và bao nhiêu giá thiếu? Sau gán, d có thêm hàng D,E không; tong theo A,B,C là gì? Một bạn thay mọi toán hạng thiếu bằng 0 rồi báo tổng A,C là 10,30: kết luận đó đã có đủ dữ liệu chưa?

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR05

Mỗi hàng d là một listing; gia USD/đêm:
```python
d = pd.DataFrame({'khu':['B','A','A'], 'gia':[60.,10.,30.]})
t = d.groupby('khu')['gia'].agg(tb='mean')
u = t.reset_index()
```
Nhận định nào đúng?

A. t và u đều mất tên khu vì reset_index xoá mọi nhãn cũ.

B. u có cột khu và tb, index 0,1; t vẫn dùng A,B làm index.

C. u có 3 hàng vì reset_index khôi phục bảng listing ban đầu.

D. t bị sửa tại chỗ, nên không còn index A,B.

#### B5-MR06

Mỗi hàng là một listing–snapshot:
```python
d = pd.DataFrame({'id':['A','A','B','A'], 'gia':[10.,20.,30.,40.]})
t = d.set_index('id')
m = t.index.duplicated()
```
m là gì và t có còn đủ bốn hàng không? Dùng mặc định giữ lần xuất hiện đầu của duplicated.

A. `[True,True,False,True]`; vẫn 4 hàng.

B. `[False,True,False,True]`; chỉ còn 2 hàng.

C. `[False,True,False,True]`; vẫn 4 hàng.

D. `[False,False,False,False]`; set_index tự làm id duy nhất.

### Độ bao phủ sau đợt 3

Đã dùng 38/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K12, K15, K16, K21, K26, K28, K29, K30, K37, K39, K41, K45, K46, K47, K48, K55, K56. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 4

### Câu trọng tâm

#### B5-031

Mỗi hàng là một bản ghi được dự định dùng mã listing làm khóa duy nhất:
```python
d = pd.DataFrame({'id':['A','B','A','C'], 'gia':[10.,20.,30.,40.]})
t = d.set_index('id')
```
Nhận định nào đúng?

A. set_index tự báo lỗi ngay vì A lặp.

B. t chỉ có 3 hàng vì A được gộp và lấy giá cuối 30.

C. set_index chạy, t có 4 hàng; t.index.is_unique=False nên mã chưa đạt yêu cầu khóa duy nhất.

D. t có 4 hàng và is_unique=True vì nhãn hàng nào cũng là chuỗi.

#### B5-032

Bảy giá hợp lệ USD/đêm, mỗi giá là một listing:
```python
s = pd.Series([1.,2.,3.,4.,5.,6.,100.])
q = pd.qcut(s, 3, labels=['thap','giua','cao'])
n = q.value_counts().loc[['thap','giua','cao']]
```
Nhận định nào đúng?

A. n là `[3,2,2]`; qcut chia theo phân vị, không bắt buộc số phần tử mỗi nhóm bằng nhau tuyệt đối hay khoảng giá rộng bằng nhau.

B. n phải bằng `[7/3,7/3,7/3]` vì qcut chia đều số hàng tuyệt đối.

C. Nhóm cao chứa chỉ 100 vì qcut chia khoảng min–max thành ba đoạn rộng bằng nhau.

D. Báo lỗi chỉ vì 7 không chia hết cho 3.

#### B5-033

Mỗi hàng bảng dưới là một khu; các mean/count chính xác, USD/đêm:

| Khu | mean | count giá đã biết | size listing |
| --- | --- | --- | --- |
| A | 50 | 1 | 4 |
| B | 100 | 3 | 3 |

Mean của toàn bộ giá đã biết là bao nhiêu?

A. `75`

B. `87.5`

C. `500/7`

D. `50`

#### B5-034

Mỗi hàng d là một listing, mỗi hàng v là một bản ghi vùng:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'khu':['A','A','B','C']})
v = pd.DataFrame({'khu':['A','A','A','B'], 'vung':['X','Y','Z','W']})
```
Cặp số hàng của `d.merge(v,on='khu',how='left')` và `d.merge(v,on='khu',how='inner')` là gì?

A. `(4,3)`

B. `(8,7)`

C. `(7,7)`

D. `(16,16)`

#### B5-035

Mỗi hàng là một listing, price CLP/đêm. Muốn gia_nghin dùng price mới đã cộng 1000:
```python
d = pd.DataFrame({'price':[10000.,20000.]})
def nghin(t): return t['price']/1000
r = d.assign(price=lambda t: t['price']+1000,
             gia_nghin=____)
```
Điền gì để gia_nghin là `[11,21]`?

A. `nghin()`

B. `nghin(d)`

C. `"nghin"`

D. `nghin`

#### B5-036

Mỗi hàng là một listing:
```python
d = pd.DataFrame({'id':['P','Q','R','S','T','U'],
                  'khu':['A','B','A','C','B','A']})
r = d.groupby('khu').filter(lambda nhom: len(nhom) >= 2)
```
Nhận định nào đúng?

A. r có 2 hàng, mỗi hàng là một khu đạt.

B. r giữ mọi hàng vì lambda nhận từng hàng, mỗi hàng có 2 cột.

C. r giữ 5 hàng gốc với index `[0,1,2,4,5]`; hàm nhận cả nhóm DataFrame và trả bool.

D. r giữ 5 hàng nhưng reset index thành `[0,1,2,3,4]`.

#### B5-037

Mỗi hàng d là một listing; v có một hàng cho mỗi khu:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'khu':['A','A','B','B']})
v = pd.DataFrame({'khu':['A','B'], 'phi':[10.,20.]})
m = d.merge(v, on='khu', how='left', validate='m:1')
```
Lệnh merge có chạy không?

A. MergeError vì A và B lặp phía trái.

B. Có, nhưng m chỉ 2 hàng vì validate gộp mỗi khu thành một hàng.

C. Có, m có 4 hàng; nhiều listing trái cùng khu hợp lệ, khóa khu bên phải duy nhất.

D. Có, vì validate tự chọn hàng đầu nếu bảng phải bị lặp.

#### B5-038

Mỗi giá là một listing, USD/đêm; yêu cầu re <50, trung từ 50 đến dưới 100, cao từ 100; thiếu phải giữ là thiếu:
```python
def nhom(x):
    if x < 50: return 're'
    elif x < 100: return 'trung'
    else: return 'cao'
s = pd.Series([49.,50.,100.,np.nan])
r = s.map(nhom)
```
(a) Kết quả hiện tại sai ở đâu? (b) Sửa hàm, vẫn dùng map. (c) Nêu ca kiểm biên/thiếu; có thể dùng một lệnh cut tương đương cho dữ liệu không âm không?

#### B5-039

Mỗi hàng goc là một listing. n_nguon do nhà cung cấp đếm trên toàn bộ goc; host có từ 3 listing trở lên được gọi chuyên nghiệp:
```python
goc = pd.DataFrame({'id':['P','Q','R','S','T'], 'host':['H','H','H','K','K'],
 'loai':['can','phong','can','can','can'], 'n_nguon':[3,3,3,2,2]})
x = goc.loc[goc['loai']=='can'].copy()
x['n_host'] = x.groupby('host')['id'].transform('size')
```
(a) n_host theo P,R,S,T là gì; lệch n_nguon có chứng minh nguồn sai không?
(b) Sửa để n_host đếm toàn bộ goc trước khi chỉ chọn nguyên căn.
(c) Trong các nguyên căn được giữ, tỷ lệ listing thuộc host chuyên nghiệp theo phạm vi goc là bao nhiêu; code cũ sẽ cho tỷ lệ nào?

#### B5-040

Mỗi hàng d là một listing, gia USD/đêm. Tệp h được gọi là “bảng host”, nhưng H xuất hiện hai lần:
```python
d = pd.DataFrame({'id':['P','Q','R'], 'host':['H','H','K'], 'gia':[10.,30.,100.]})
h = pd.DataFrame({'host':['H','H','K'], 'chuyen':[True,True,False]})
m = d.merge(h, on='host', how='left')
```
Tính số hàng m, tổng gia và tỷ lệ chuyen sau ghép. So với phép ghép một hàng đúng cho mỗi host, những listing nào bị tăng trọng số? Thêm ràng buộc nào để phát hiện sai quan hệ, và nó có tự sửa bảng h không?

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR07

Mỗi hàng là một listing, gia USD/đêm. Giữ tất cả đồng hạng đắt nhất trong từng khu:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'khu':['A','A','B','B'],
                  'gia':[20.,20.,10.,30.]})
r = d.loc[d['gia'] == d.groupby('khu')['gia'].transform('max')]
```
Những listing nào được giữ?

A. P,S.

B. Q,S.

C. Chỉ S.

D. P,Q,S.

#### B5-MR08

Mỗi hàng là một listing; giá thiếu nên phan có thể thiếu:
```python
d = pd.DataFrame({'khu':['A','A','A','B','B','B'],
                  'phan':['cao','re',None,'cao','cao','re']})
r = d.groupby('khu')['phan'].value_counts(normalize=True)
```
Tỷ lệ cao ở A và B trong r là bao nhiêu, mẫu số là gì? Nếu cần tỷ lệ listing đã được gắn nhãn cao trên tất cả listing của chính khu, kể cả hàng chưa có phân khúc, sửa lệnh thế nào? So với tỷ lệ cao toàn bảng có giống không?

### Độ bao phủ sau đợt 4

Đã dùng 46/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K12, K16, K21, K30, K39, K41, K46, K47, K48. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 5

### Câu trọng tâm

#### B5-041

Mỗi hàng là một listing, giá và phí USD:
```python
d = pd.DataFrame({'gia':[30.,10.,20.]}, index=['C','A','B'])
s = pd.Series([5.,9.], index=['A','D'])
d['phi'] = s
```
Nhận định nào đúng?

A. d có 4 hàng, thêm D với phi=9.

B. d có 3 hàng; phi là `[5,9,NaN]`.

C. d vẫn có 3 hàng C,A,B; phi theo thứ tự đó là `[NaN,5,NaN]`.

D. Báo lỗi vì s có 2 phần tử còn d có 3 hàng.

#### B5-042

Cùng bốn listing qua hai kỳ, không mất hàng, không giá thiếu và không làm tròn:
```python
cu = pd.Series([10.,20.,30.,40.], index=['P','Q','R','S'])
moi = 2*cu+5
q1, b1 = pd.qcut(cu, 2, labels=['thap','cao'], retbins=True)
q2, b2 = pd.qcut(moi, 2, labels=['thap','cao'], retbins=True)
```
Nhận định nào đúng về mốc giữa và thành viên nhóm?

A. Mốc giữa vẫn 25 vì số nhóm và các listing không đổi.

B. Mốc giữa đổi 55, nên một số listing nhất thiết đổi nhóm.

C. Thành viên nhóm luôn giữ nguyên kể cả thêm listing giá mới vào kỳ sau.

D. Mốc giữa đổi từ 25 lên 55; từng listing giữ nhóm cũ.

#### B5-043

Mỗi hàng là một listing, gia USD/đêm; giá 0 là hợp lệ:
```python
d = pd.DataFrame({'khu':['A','A','A','B','B'],
 'loai':['can','can','phong','can','can'], 'gia':[10.,30.,0.,50.,70.]})
long = d.groupby(['khu','loai'])['gia'].mean()
wide = long.unstack('loai')
```
Shape wide và cặp `(wide.loc['A','phong'], wide.loc['B','phong'])` là gì?

A. `(2,2)` và `(0,NaN)`.

B. `(3,1)` và `(0,NaN)`.

C. `(2,2)` và `(0,0)`.

D. `(2,2)` và `(NaN,NaN)`.

#### B5-044

Mỗi hàng d là một listing; phi là thông tin một lần theo khu, USD:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'khu':['A','B','C','D']})
v = pd.DataFrame({'khu':['A','B','C'], 'phi':[5.,np.nan,8.]})
m = d.merge(v, on='khu', how='left', indicator=True)
```
Những listing nào có phi thiếu và trạng thái _merge tương ứng?

A. Q và S đều left_only.

B. Chỉ S có phi thiếu.

C. Q: both; S: left_only.

D. Q: left_only; S: both.

#### B5-045

Mỗi hàng là một lượt ở hai đêm; gia USD/đêm:
```python
d = pd.DataFrame({'gia':[10.,20.]})
d['tong'] = 2*d['gia']
r = d.assign(gia=d['gia']+5)
```
Nhận định nào đúng nếu tong của r phải dùng giá mới?

A. tong tự đổi thành `[30,50]` vì đã được định nghĩa bằng công thức ở d.

B. r sai vì assign không cho ghi đè gia.

C. Chỉ cần đổi tên r thành moi, tong sẽ cập nhật.

D. tong của r vẫn `[20,40]`; cần tính lại từ gia mới, ví dụ thêm `tong=lambda t:2*t["gia"]` trong assign sau gia.

#### B5-046

Bảng tổng hợp có một hàng mỗi host; không listing nào lặp, giá mean theo USD/đêm chính xác. Host chuyên nghiệp có ít nhất 2 listing:

| host | số listing | mean giá listing của host |
| --- | --- | --- |
| H | 5 | 20 |
| K | 2 | 80 |
| J | 1 | 140 |

Bộ bốn: (tỷ lệ listing thuộc host chuyên nghiệp; tỷ lệ host chuyên nghiệp; mean của ba mean host với host ngang trọng số; mean của tám listing) là gì?

A. `(7/8, 2/3, 80, 50)`

B. `(2/3, 7/8, 80, 50)`

C. `(7/8, 2/3, 80, 80)`

D. `(7/8, 7/8, 50, 50)`

#### B5-047

Mỗi hàng là một lượt ở; giá USD/đêm, phi dọn dẹp USD thu một lần. Từ 7 đêm được miễn phí kể cả khi phí niêm yết chưa biết:
```python
d = pd.DataFrame({'gia':[10.,20.,np.nan,30.], 'so_dem':[6,7,8,2],
                  'phi':[5.,np.nan,7.,np.nan]}, index=['A','B','C','D'])
```
Viết vài dòng dùng phép toán cột hoặc apply để tính tong. Cho kết quả theo A,B,C,D và giải thích hai giá thiếu. Nêu hai ca kiểm để bắt lỗi phí bị nhân theo đêm hoặc bỏ sót biên 7.

#### B5-048

Mỗi hàng d là một listing, id duy nhất. Cần tra đúng một mức phí USD cho mỗi host, nhưng h chưa thống nhất phí của H:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'host':['H','H','K','J']})
h = pd.DataFrame({'host':['H','H','K','J'], 'phi':[2.,5.,3.,4.]})
m = d.merge(h, on='host', how='left')
assert m['id'].nunique() == len(d)
```
(a) Assert có qua không, m có mấy hàng; nó đã đủ kiểm yêu cầu chưa?
(b) Thêm validate để phát hiện đúng vi phạm. Nó sẽ làm gì?
(c) Có nên tự drop_duplicates('host') rồi coi xong không? Nêu các kiểm tra cần làm sau khi nguồn phí đã được làm rõ.

#### B5-049

Mỗi hàng là một listing, gia USD/đêm:
```python
d = pd.DataFrame({'khu':['A','B','A','B'], 'gia':[10.,30.,50.,70.]},
                 index=[4,7,9,12])
tb = d.groupby('khu')['gia'].mean()
r = d['gia']-tb
```
Cho số nhãn và số NaN của r; sửa để mỗi hàng trừ đúng mean khu. Sau đó viết một lệnh groupby.filter giữ các hàng gốc thuộc khu có mean giá từ 40 trở lên; những index nào còn lại?

#### B5-050

Mỗi hàng là một listing, phí USD; s đã gắn đúng mã:
```python
d = pd.DataFrame({'gia':[20.,30.,10.]}, index=['B','C','A'])
s = pd.Series([9.,5.,7.,3.], index=['D','A','C','B'])
d['phi'] = s.to_numpy()
```
(a) Vì sao dòng cuối lỗi? Một bạn cắt còn ba phần tử `s.to_numpy()[:3]`: khi đó chạy được nhưng gán gì theo B,C,A?
(b) Sửa đúng mà không thêm hàng D.
(c) Cho kết quả đúng và cách kiểm không chỉ dựa vào độ dài.

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR09

Mỗi hàng là một listing; phí USD theo mã:
```python
d = pd.DataFrame({'gia':[20.,10.,30.]}, index=['B','A','C'])
s = pd.Series([5.,8.], index=['A','B'])
d['phi'] = s.reindex(d.index).to_numpy()
```
Nhận định nào đúng?

A. phi theo B,A,C là `[8,5,NaN]`, ghép đúng vì đã reindex theo hàng d trước khi bỏ nhãn.

B. phi là `[5,8,NaN]` vì to_numpy huỷ cả kết quả sắp nhãn đã làm.

C. phi là `[8,5,0]` vì reindex tự điền 0.

D. Báo KeyError ở C vì C không có trong s.

#### B5-MR10

Mỗi hàng d là một listing, gia USD/đêm. Cần CSV mỗi host một hàng, gồm mã host và mean giá:
```python
d = pd.DataFrame({'host':['H','K','H'], 'gia':[20.,80.,40.]})
t = d.groupby('host')['gia'].agg(tb='mean')
u = t.reset_index()
t.to_csv('host.csv', index=False)
```
CSV có giữ mã host không? Sửa đúng dòng xuất mà không sửa t; nêu bảng hai cột mong đợi và vì sao chỉ gọi reset_index nhưng xuất t chưa đạt yêu cầu.

### Độ bao phủ sau đợt 5

Đã dùng 51/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K30, K46, K47, K48. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 6

### Câu trọng tâm

#### B5-051

Mỗi hàng là một listing; phí USD:
```python
d = pd.DataFrame({'gia':[10.,20.]}, index=['A','B'])
d.index.name = 'listing_id'
s = pd.Series([8.,5.], index=['B','A'])
s.index.name = 'ma_khac'
d['phi'] = s
```
Hai phí theo A,B là gì?

A. `[5,8]`; khác tên index không cản ghép theo giá trị nhãn A,B.

B. `[NaN,NaN]`; tên index phải trùng mới khớp.

C. `[8,5]`; tên khác khiến pandas chuyển sang ghép vị trí.

D. Phát sinh ValueError chỉ vì index.name khác nhau.

#### B5-052

Mỗi hàng là một lượt ở; cần cùng công thức gia*so_dem+phi. Một cách dùng apply(axis=1), cách kia viết trực tiếp trên các cột. Nhận định nào đúng để chọn và kiểm chứng cách tính?

A. Khi công thức phù hợp, phép toán cột diễn đạt trực tiếp và tránh gọi hàm Python từng hàng; cần kiểm cả giá trị, nhãn, NaN và biên nghiệp vụ trước khi so tốc độ.

B. apply luôn sai về kết quả nên phải loại dù đã đúng mọi quy tắc tính tiền.

C. apply tự biên dịch hàm Python nên chắc chắn bằng tốc độ phép toán cột.

D. Chỉ cần hai Series kết quả cùng độ dài; không cần so nhãn hay vị trí NaN khi đo.

#### B5-053

Mỗi hàng là một listing trong bảng thành phố hiện tại. Nhà cung cấp có thể đếm host ở phạm vi rộng hơn:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'host':['H','H','H','K'],
                  'n_nguon':[5,5,5,1]})
n = d.groupby('host')['id'].transform('size')
print((n == d['n_nguon']).sum(), len(d))
```
Kết quả và diễn giải nào đúng?

A. `3,4`; có ba hàng H khớp.

B. `4,4`; transform tự đọc và dùng n_nguon.

C. `1,4`; H được đếm 3 trong bảng này so với 5 của nguồn; cần kiểm phạm vi, chưa kết luận nguồn sai.

D. `1,4`; điều đó chắc chắn chứng minh ba bản ghi H của nhà cung cấp sai.

#### B5-054

Mỗi hàng d là một listing, không id nào lặp:
```python
d = pd.DataFrame({'id':['P','Q','R','S','T','U'],
                  'host':['H','K','H','J','H','K']})
h = d.groupby('host').agg(n=('id','size'))
m = d.merge(h, on='host', how='left', validate='m:1')
```
m có bao nhiêu hàng và listing P nhận n bằng bao nhiêu?

A. 3 hàng; P nhận n=3.

B. 6 hàng; P nhận n=3.

C. 9 hàng; P nhận n=3.

D. 6 hàng; P nhận n=1.

#### B5-055

Mỗi hàng là một listing, gia USD/đêm:
```python
goc = pd.DataFrame({'id':['P','Q','R','S'], 'gia':[20.,80.,np.nan,40.]})
def run(src):
    return (src.loc[src['gia'].notna()]
      .assign(phan=lambda t: pd.cut(t['gia'], [0,50,100,np.inf],
                                   labels=['re','trung','cao'], right=False))
      .groupby('phan', observed=True).agg(n=('id','size'), tb=('gia','mean')))
a = run(goc)
b = run(goc)
```
Nhận định nào đúng?

A. a có 3 hàng, cao luôn có một hàng n=0 vì labels khai báo ba nhóm.

B. a có 2 hàng; re có n=1,tb=20 vì chỉ dùng listing đầu nhóm.

C. b khác a vì gọi assign lần hai chia tiếp gia của goc.

D. a,b bằng nhau; có 2 hàng re,trung với n=2,1 và tb=30,80; goc không có cột phan.

#### B5-056

Mỗi hàng d là một listing, bảng v có một hàng mỗi khu:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'khu':['A','B','C','A']})
v = pd.DataFrame({'khu':['A','B'], 'phi':[5.,np.nan]})
m = d.merge(v, on='khu', how='left', validate='m:1', indicator=True)
assert len(m) == len(d)
```
Assert qua và validate không lỗi. Kết luận nào đúng?

A. Mọi listing chắc chắn đã có đúng mức phí vì cả hai kiểm tra đều qua.

B. Q,R đều left_only vì phi cùng thiếu.

C. validate=m:1 đã loại R để giữ số hàng bằng d.

D. Chưa bảo đảm mọi khóa khớp hay phí đủ; R là left_only, Q là both nhưng phi thiếu.

#### B5-057

Cùng bốn listing, giá CLP/đêm, không làm tròn:
```python
cu = pd.Series([20000.,40000.,60000.,80000.], index=['P','Q','R','S'])
moi = 2*cu+10000
bins = [0,50000,100000,np.inf]
labels = ['re','trung','cao']
```
Với cut dùng bins, labels trên và right=False, cho nhóm trước/sau theo P,Q,R,S. Với qcut chia 2 nhóm thấp/cao, thành viên có đổi không, mốc giữa đổi thế nào? Nếu đổi moi sang nghìn CLP nhưng giữ bins cũ, sai ở đâu và sửa bins thế nào? Có được bảo đảm nhóm qcut giữ nguyên nếu đổi tập listing, tình trạng thiếu hoặc quy tắc chia nhóm không?

#### B5-058

Mỗi hàng là một listing; review là số đánh giá trong một năm, không phải số booking:
```python
d = pd.DataFrame({'phan':['re','re','re','cao','cao','cao'],
 'chuyen':[False,False,True,False,True,True],
 'review':[0.,4.,8.,2.,np.nan,6.]})
```
Viết pivot_table cho mean review theo phân khúc (hàng) × kiểu host chuyên nghiệp (cột). Cho bốn ô và mẫu số của ô (cao,True); nếu bỏ aggfunc thì có thay mean thành số listing không? Mỗi hàng kết quả là gì và bảng này có đủ chứng minh host chuyên nghiệp tạo thêm booking nhờ tính chuyên nghiệp không?

#### B5-059

Mỗi hàng d là một listing, host là mã chủ, khu là mã quận. Bảng v tra phí USD theo KHU, không theo host; hai hệ mã tình cờ đều có A,B:
```python
d = pd.DataFrame({'id':['P','Q','R','S'], 'host':['A','B','A','B'],
                  'khu':['B','A','A','B']})
v = pd.DataFrame({'khu':['A','B'], 'phi':[10.,20.]})
m = (d.assign(khu=d['host'])
       .merge(v, on='khu', how='left', validate='m:1', indicator=True))
assert len(m) == len(d)
assert (m['_merge']=='both').all()
```
(a) Các kiểm tra có qua không, những listing nào bị gán sai phí?
(b) Sửa thao tác đầu để ghép đúng khu gốc.
(c) Cho phí đúng theo P,Q,R,S và phép kiểm phát hiện sai ngữ nghĩa mà len/validate/both đều bỏ sót.

#### B5-060

Mỗi hàng goc là một listing, price nguồn CLP/đêm. Cần thêm gia_nghin và giữ đầu vào nguyên vẹn:
```python
goc = pd.DataFrame({'price':[40000.,80000.]})
def nghin(d):
    goc['price'] = goc['price']/1000
    return goc['price']
moi = goc.assign(gia_nghin=nghin)
assert goc['price'].tolist()==[40000.,80000.] or True
```
(a) Sau lần đầu, goc['price'] là gì; vì sao assert qua? Nếu chỉ chạy lại hai dòng cuối, không khởi tạo lại goc, gia_nghin nhận gì?
(b) Sửa hàm; giả sử đã khôi phục goc từ nguồn đúng.
(c) Nêu kiểm tra hai lần tạo kết quả và bảng gốc; vì sao chỉ dùng assign chưa đủ trong code cũ?

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR11

Mỗi hàng là một listing; k1,k2 là giá USD/đêm hai kỳ:
```python
d = pd.DataFrame({'k1':[10.,20.,30.,40.], 'k2':[2.,np.nan,6.,0.]},
                 index=['A','B','C','D'])
r = d.apply(lambda cot: cot.mean())
```
Nhãn và giá trị r là gì?

A. Index k1,k2; giá trị `[25,8/3]`.

B. Index A,B,C,D; giá trị `[6,20,18,20]`.

C. r là DataFrame giống hệt d vì apply áp một hàm lên từng số.

D. Index k1,k2; giá trị `[25,2]`.

#### B5-MR12

Mỗi nhãn hàng d là mã LISTING; khu cũng dùng A,B nhưng là mã KHU khác ý nghĩa, giá USD/đêm:
```python
d = pd.DataFrame({'khu':['A','B','A','B'], 'gia':[10.,50.,30.,70.]},
                 index=['B','A','C','D'])
tb = d.groupby('khu')['gia'].mean()
d['tb_khu'] = tb
u = tb.reset_index()
```
Cho tb_khu sai theo thứ tự B,A,C,D; giải thích các nhãn tình cờ khớp. Sửa bằng map với tb và cho kết quả đúng. Chỉ tạo u bằng reset_index đã tự sửa cột sai của d chưa; u gồm những cột nào?

### Độ bao phủ sau đợt 6

Đã dùng 56/56 mục tiêu trong yêu cầu trả lời. Không còn mục tiêu thiếu trong phạm vi đã xác định.

## Đối chiếu cuối bộ

- Đủ B5-001–B5-060: **60 câu trọng tâm = 40 TN + 20 TL**; nhóm chính **10/12/16/14/8**.
- Đủ B5-MR01–B5-MR12: **12 bổ sung = 8 TN + 4 TL**; tách riêng ở từng đợt.
- Trọng tâm có **15 nền tảng + 33 vận dụng + 12 phân loại**. Không coi đây là dự đoán chắc chắn đề thi thật.
- **56/56 mục tiêu** được dùng để trả lời ít nhất một câu. pivot_table ở trọng tâm; các phần tự học giữ nhãn ưu tiên theo nguồn. Các câu sửa lỗi ba ý (a)–(b)–(c) gồm 010,018,019,028,038,039,048,050,059,060.
- Đã rà câu trùng ý và phương án nhiễu; có cặp đối chiếu chủ đích để phân biệt đọc nhãn/vị trí, lọc trước/sau, cùng số hàng/đúng khóa. Không chỉ đổi số hoặc tên từ đề gốc: các tình huống thay tập quan sát, điều kiện, yêu cầu sửa và cách kiểm chứng.
- Độ bao phủ nguồn Bài 5 khác mức ưu tiên từ đề mẫu. Không bao phủ toàn bộ sách/website liên kết và không thêm SQL, API, regex, thời gian, pipe hay kỹ thuật pandas ngoài bài.

Đã chạy kiểm chứng **71/72 câu** bằng pandas 3.0.1; **1 câu** được kiểm bằng suy luận, chưa chạy vì chỉ hỏi cơ chế/thiết kế. Không đo tỷ lệ hiệu năng. Các kiểm tra gồm đảo thứ tự alignment, đối chiếu nhóm/tập giá, đếm cặp merge, chạy hai lần từ nguồn cố định và kiểm bảng gốc.
