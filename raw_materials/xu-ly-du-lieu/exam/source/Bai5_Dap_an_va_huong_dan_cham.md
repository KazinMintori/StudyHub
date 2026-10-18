# BÀI 5 — ĐÁP ÁN VÀ HƯỚNG DẪN CHẤM

Dùng cùng [file câu hỏi](<D:/LTXLDL_GK/output/bai5/Bai5_72_cau_hoi.md>).

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


## Ghi chú kiểm logic nguồn

LAB ô 4 có `assert ... or True`, luôn qua; B5-060 kiểm trực tiếp giới hạn của kiểm tra này. Nội dung ngân hàng không suy ra “mọi khóa đều khớp” từ riêng validate/len; không diễn giải “nhóm qcut giữ nguyên” thành “ngưỡng giữ nguyên” hoặc số phần tử mỗi nhóm luôn bằng nhau tuyệt đối. Những phát biểu giản lược trong slide được đọc cùng ghi chú, điều kiện dữ liệu và kiểm chứng. Các ghi chú giải đáp này chỉ đặt trong file đáp án.

## Giả định và quy ước

- Giả định pandas **3.0.x**, ưu tiên ngữ nghĩa 3.0.3 theo NB. Môi trường thực thi: **pandas 3.0.1, NumPy 2.3.5, Python 3.12.14**. Không tuyên bố đã kiểm riêng trên 3.0.3.
- Mỗi câu khởi tạo dữ liệu riêng; đã có `import pandas as pd` và `import numpy as np`. Thực hiện đúng thứ tự, chỉ chạy lại những dòng đề nói rõ. Giá và số liệu đều giả lập.
- Một listing là một chỗ ở; host là chủ nhà; review là một đánh giá; listing–snapshot là một chỗ ở ở một đợt. Mỗi câu nêu đơn vị quan sát, phạm vi nhóm và đơn vị giá nếu liên quan. Khóa nhóm/merge không thiếu, trừ câu ghi khác; các chỉ mục dùng alignment là duy nhất, trừ phần tự học ghi rõ lặp.
- NaN là thiếu số, không tự coi là 0; số thực có `np.nan` dùng float64. Không yêu cầu dạng in dtype chuỗi, khoảng trắng hoặc thứ tự chưa quy định. Nếu cần thứ tự, dùng danh sách nhãn, sort hoặc truy cập theo nhãn trong đề.
- cut luôn chỉ rõ bins, labels, right. qcut dùng các dữ liệu không trùng mốc gây lỗi ngoài mục tiêu; so giữa kỳ trên cùng tập listing không làm tròn, trừ câu cố ý thay thành phần.
- Khi có categorical, ghi observed rõ nếu ảnh hưởng nhóm; không đưa bẫy khóa thiếu của SQL vào pandas. Với top, giữ mọi đồng hạng nếu đề yêu cầu.
- Nhận đáp án số thực sai số tuyệt đối `1e-12`, trừ câu ghi mức khác. Với thiếu, kiểm bằng isna/notna; không kiểm `NaN == NaN`.
- Mỗi TN đúng duy nhất một lựa chọn, có thể chấm 1 điểm; TL có thang riêng 2 hoặc 3 điểm. Nhận lời giải tương đương đúng giá trị, nhãn, đơn vị và ý nghĩa; không trừ vì có cách khác gọn hơn.

## Cách dùng

Đáp án tách khỏi toàn bộ câu hỏi. TN giải thích đủ bốn lựa chọn; TL có điểm thành phần. Kxx tra tại danh mục trong file câu hỏi; nhóm, kiến thức/bẫy và độ khó chỉ đặt trong file đáp án. Mỗi câu được tự giải và kiểm tập hàng, nhãn, mẫu số, khóa ghép hoặc trạng thái chạy lại phù hợp.

## Đợt 1

### Câu trọng tâm

#### B5-001

**Đáp án: A.**

- A đúng: L1 ghép 40−30, L2 ghép 60−70, L3 ghép 55−50; không dùng vị trí hiển thị.
- B sai: ghép theo vị trí: 55−30,40−70,60−50, bỏ nhãn.
- C sai: giữ kết quả theo thứ tự moi mà quên .loc yêu cầu L1,L2,L3.
- D sai: đảo chiều phép trừ thành cu−moi.

**Đối chiếu:** nhóm 1; K01; mức Nền tảng. **Kiến thức và bẫy:** Phép toán Series ghép đúng mã dù đảo thứ tự. **Đọc lại:** BG §1; NB ô 6–10.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-002

**Đáp án: B.**

- A sai: tra tên index phong thay vì giá trị cột loai.
- B đúng: map tra giá trị loai của hàng đó là can, không tra nhãn index phong.
- C sai: map tra lại một khóa nhiều lần được; không áp quy tắc gán list cùng độ dài.
- D sai: map bằng dict trả giá trị thiếu cho loại chưa có, không dừng bằng KeyError.

**Đối chiếu:** nhóm 2; K08; mức Nền tảng. **Kiến thức và bẫy:** map dict tra theo giá trị khác gán Series căn theo index. **Đọc lại:** BG §2; NB ô 23–27.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-003

**Đáp án: D.**

- A sai: đưa giá thiếu vào mẫu số mean của A.
- B sai: nhầm aggregate với transform.
- C sai: nhầm groupby với việc chỉ gộp các đoạn liền nhau.
- D đúng: A chỉ có một giá biết 20; B dùng (40+80)/2. Hàng A không cần đứng cạnh nhau.

**Đối chiếu:** nhóm 3; K18; mức Vận dụng. **Kiến thức và bẫy:** Split–apply–combine; hàng cùng nhóm không cần liên tiếp; mean/median bỏ giá thiếu. **Đọc lại:** BG §3; NB ô 53–61.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-004

**Đáp án: D.**

- A sai: nhầm đặt nhãn index với khử bản ghi trùng mã.
- B sai: ghép cột theo vị trí thay theo tên.
- C sai: nhầm nối thêm quan sát với merge bổ sung theo khóa.
- D đúng: concat khớp tên cột dù thứ tự cột b khác; ignore_index chỉ đặt lại index.

**Đối chiếu:** nhóm 4; K32, K33; mức Vận dụng. **Kiến thức và bẫy:** concat thêm quan sát, khớp tên cột; ignore_index không khử mã trùng; Mỗi hàng listing–snapshot; lặp id giữa hai đợt có thể hợp lệ. **Đọc lại:** BG §4; NB ô 97–100.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-005

**Đáp án: A.**

- A đúng: assign tạo bảng mới hai cột, giữ price gốc; goc không có gia_nghin.
- B sai: tưởng assign thêm cột vào cả bảng đầu vào.
- C sai: tưởng thêm cột mới là đổi tên/thay cột price.
- D sai: bỏ qua phép chia đơn vị.

**Đối chiếu:** nhóm 5; K42; mức Nền tảng. **Kiến thức và bẫy:** assign trả bảng mới; đầu vào giữ nguyên trong cách dùng đúng. **Đọc lại:** BG §5; NB ô 132–135.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-006

**Đáp án: C.**

- A sai: bỏ C như thể phép toán chỉ giữ index bên trái.
- B sai: tự điền toán hạng thiếu bằng 0.
- C đúng: A=2, B=5; C thiếu giá mới, D thiếu giá cũ. Không tự coi giá chưa có là 0.
- D sai: nhầm phép toán Series với inner join.

**Đối chiếu:** nhóm 1; K02; mức Vận dụng. **Kiến thức và bẫy:** Hợp nhãn trong phép toán; thiếu toán hạng khác giá bằng 0. **Đọc lại:** BG §1; NB ô 11–13.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-007

**Đáp án: B.**

- A sai: loại giá trị 0 hợp lệ khỏi count.
- B đúng: hai phí 15 và một phí 0 đã biết được count; loại la cho NaN, sum bỏ qua nhưng len vẫn đếm hàng.
- C sai: cho rằng sum mặc định lan NaN thay bỏ qua các giá thiếu.
- D sai: coi phí chưa biết là 0 đã xác nhận.

**Đối chiếu:** nhóm 2; K09; mức Vận dụng. **Kiến thức và bẫy:** Thiếu bảng phí là chưa biết; sum/count/len sau map dùng tập giá trị khác nhau. **Đọc lại:** BG §2; GK câu 11 (biến thể có loại miễn phí đã biết).

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-008

Mean chung = `(40*2+100*4)/(2+4)=80` USD/đêm, mỗi giá đã biết có trọng số bằng nhau. Mean A dùng 2 giá, không phải 5 listing; ba giá thiếu không tham gia tử hay mẫu số. Dùng size ra 600/9≈66.666667; lấy mean của mean ra 70, đều sai mục tiêu. Không gộp median bằng công thức mean: median và count không chứa đủ phân bố các giá gốc để luôn khôi phục median chung.

**Hướng dẫn chấm:** 2 điểm: kết quả/công thức 0,75; mẫu số và hai trọng số sai 0,75; giới hạn với median 0,5. Chấp nhận sai số 1e-6 cho số thập phân.

**Đối chiếu:** nhóm 3; K22, K19; mức Phân loại. **Kiến thức và bẫy:** Gộp mean phải dùng count đúng trọng số; không gộp median bằng công thức mean; size đếm hàng, count đếm giá biết, nunique đếm đối tượng khác nhau. **Đọc lại:** BG §3 bài tập 3; NB ô 67–68.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-009

P có 2 hàng trái × 2 hàng phải =4 cặp; Q và R mỗi mã 1 cặp, tổng 6 hàng. Giá 10 và 30 của P được lặp hai lần; tổng =2*10+20+2*30+40=140, khác tổng d là 100. ignore_index chỉ đặt nhãn hàng 0–3, không làm id duy nhất. d có đơn vị listing–snapshot; ghép theo id đơn lẻ tạo các cặp chéo giữa các đợt của P. Nếu muốn bổ sung thông tin theo snapshot phải xác định khóa phù hợp, không ép bỏ một đợt hợp lệ.

**Hướng dẫn chấm:** 2 điểm: 6 hàng và cặp khớp 0,75; tổng 140 và ảnh hưởng trọng số 0,75; đơn vị/ignore_index 0,5.

**Đối chiếu:** nhóm 4; K33, K36, K40; mức Phân loại. **Kiến thức và bẫy:** Mỗi hàng listing–snapshot; lặp id giữa hai đợt có thể hợp lệ; Khóa lặp hai phía tạo các cặp; left có thể tăng hàng; đếm bằng bội số từng khóa; Ghép host về listing theo nhiều–một; nhân hàng làm lệch tổng, tỷ lệ, trọng số. **Đọc lại:** BG §4 concat/merge và kiểm số hàng.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-010

(a) Sau lần đầu [40,80], sau chạy lại [0.04,0.08]; chia lặp làm sai quy ước đơn vị, không còn giữ price CLP như nguồn. (b) Với goc nguyên vẹn: `moi=goc.assign(gia_nghin=goc['price']/1000)`. (c) Chạy lại biểu thức này hai lần từ cùng goc rồi so bảng bằng nhau và goc vẫn [40000,80000]. Tên moi không sửa được một d đã bị chia trước đó; phải lấy lại nguồn đúng. Nếu dùng cut với ngưỡng CLP, dùng price gốc hoặc đổi cả giá và ngưỡng sang cùng đơn vị.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm kết quả và đơn vị; (b) 1 điểm nguồn cố định/cột mới; (c) 1 điểm kiểm hai lần và không dựa vào tên biến.

**Đối chiếu:** nhóm 5; K43, K17, K42; mức Vận dụng. **Kiến thức và bẫy:** Chạy lại cập nhật đơn vị trên kết quả cũ tiếp tục chia; assign không tự chống lỗi này; Thống nhất đơn vị tiền và quy ước ngưỡng khi so mốc chụp; assign trả bảng mới; đầu vào giữ nguyên trong cách dùng đúng. **Đọc lại:** BG §5; NB ô 128–135.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR01

**Đáp án: B.**

- A sai: giữ vị trí dữ liệu rồi đổi nhãn, không reindex theo giá trị nhãn.
- B đúng: reindex tra B rồi nhãn mới C nhận thiếu, sau đó A; s không bị sửa.
- C sai: tự điền 0 cho nhãn mới.
- D sai: nhầm reindex cho phép nhãn mới với chọn danh sách bằng loc.

**Đối chiếu:** nhóm 1; K49; mức Bổ sung. **Kiến thức và bẫy:** reindex theo danh sách nhãn, thêm nhãn mới nhận thiếu. **Đọc lại:** NB ô 146–147: tự học reindex.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-MR02

**Đáp án: C.**

- A sai: tưởng index luôn duy nhất và lấy lần xuất hiện đầu.
- B sai: tưởng loc tự cộng các hàng trùng nhãn.
- C đúng: một nhãn có thể chọn nhiều hàng; pandas không tự gộp giá hay xóa snapshot.
- D sai: nhầm yêu cầu khóa nghiệp vụ duy nhất với khả năng index lặp của pandas.

**Đối chiếu:** nhóm 1; K50, K04; mức Bổ sung. **Kiến thức và bẫy:** Chỉ mục lặp: loc một nhãn trả nhiều phần tử; is_unique; set_index không bảo đảm mã duy nhất; kiểm index.is_unique. **Đọc lại:** NB ô 148–151: chỉ mục lặp.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Độ bao phủ sau đợt 1

Đã dùng 17/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K03, K05, K06, K07, K10, K11, K12, K13, K14, K15, K16, K20, K21, K23, K24, K25, K26, K27, K28, K29, K30, K31, K34, K35, K37, K38, K39, K41, K44, K45, K46, K47, K48, K51, K52, K53, K54, K55, K56. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 2

### Câu trọng tâm

#### B5-011

**Đáp án: C.**

- A sai: ndarray không mang index của s.
- B sai: độ dài bằng nhau nên phép gán ndarray vẫn chạy, không kiểm mã.
- C đúng: B ở vị trí 0 nhận 5, A ở vị trí 1 nhận 10; đúng nghiệp vụ phải A=5,B=10.
- D sai: pandas gán mảng cùng độ dài theo vị trí, không mặc định thêm NaN.

**Đối chiếu:** nhóm 1; K03, K07; mức Nền tảng. **Kiến thức và bẫy:** to_numpy bỏ nhãn; cùng độ dài vẫn có thể ghép sai đối tượng; Gán list/ndarray theo vị trí; RHS Series dài hơn có thể khớp nhưng ndarray lỗi độ dài. **Đọc lại:** BG §1; NB ô 6–10.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-012

**Đáp án: D.**

- A sai: lời gọi map này vẫn đưa NaN vào hàm; không có quy tắc tự giữ thiếu cho mọi hàm.
- B sai: coi các biên 30,100 thuộc khoảng bên trái dù đề dùng <.
- C sai: so sánh float NaN với ngưỡng trả False, không tự gây lỗi ở đây.
- D đúng: hai so sánh với NaN đều False nên rơi vào else; phải kiểm pd.isna trước để giữ thiếu.

**Đối chiếu:** nhóm 2; K10; mức Vận dụng. **Kiến thức và bẫy:** map hàm phân loại: xử lý NaN trước if/elif/else và đúng biên. **Đọc lại:** LAB bước 1, ô 8–9.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-013

**Đáp án: A.**

- A đúng: A có ba listing nhưng chỉ 10,30 được dùng trong mean: (10+30)/2=20.
- B sai: coi NaN là 0 và là một giá đã biết.
- C sai: đảo size với count.
- D sai: đếm size chỉ trên hàng có giá như count.

**Đối chiếu:** nhóm 3; K18, K19, K20; mức Nền tảng. **Kiến thức và bẫy:** Split–apply–combine; hàng cùng nhóm không cần liên tiếp; mean/median bỏ giá thiếu; size đếm hàng, count đếm giá biết, nunique đếm đối tượng khác nhau; agg trên Series và named aggregation nhiều cột; một hàng mỗi nhóm. **Đọc lại:** BG §3; NB ô 59–61.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-014

**Đáp án: B.**

- A sai: ghép phí theo vị trí hàng phải.
- B đúng: B ghép B nhận 20; A nhận 10; C nhận 30, theo khóa khu chứ không theo thứ tự/index.
- C sai: căn theo index 9,2,7 với index bảng phải thay vì on=khu.
- D sai: tự sắp xếp khu A,B,C dù sort=False giữ thứ tự trái trong ca này.

**Đối chiếu:** nhóm 4; K34; mức Vận dụng. **Kiến thức và bẫy:** merge theo giá trị khóa, không theo thứ tự hay index; khác concat. **Đọc lại:** BG §4; NB ô 101–106.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-015

**Đáp án: D.**

- A sai: dùng size/count review thay cho số listing khác nhau.
- B sai: hiểu nunique là chỉ đếm các id xuất hiện đúng một lần, thay vì các giá trị khác nhau.
- C sai: đếm đúng nhưng áp tiêu chí có ít nhất 1 listing thay vì ít nhất 2.
- D đúng: nunique xác định số listing khác nhau: P,Q so với chỉ R, không phải số review.

**Đối chiếu:** nhóm 3; K19, K25; mức Vận dụng. **Kiến thức và bẫy:** size đếm hàng, count đếm giá biết, nunique đếm đối tượng khác nhau; Review/snapshot khác listing; nunique khác size; chọn đúng khóa khi tính độ lệch. **Đọc lại:** BG §3 đơn vị quan sát; GK câu 23.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-016

**Đáp án: D.**

- A sai: đó là axis=0, không phải axis=1.
- B sai: nhầm DataFrame.apply axis=1 với Series.map từng phần tử.
- C sai: sai quy tắc phí một lần và tự điền phí chưa biết.
- D đúng: mỗi scalar trả về cho một lượt ở; hàng R1 thiếu phí nên chưa tính được tổng.

**Đối chiếu:** nhóm 2; K11; mức Vận dụng. **Kiến thức và bẫy:** apply axis=1 nhận hàng Series; scalar tạo Series giữ index. **Đọc lại:** BG §2; NB ô 28–35.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-017

**Đáp án: B.**

- A sai: nhầm how mặc định.
- B đúng: P,S khớp A, Q khớp B; R không tạo cặp.
- C sai: tự gộp P,S thành một hàng khu A.
- D sai: bỏ điều kiện khóa, suy thành tích Descartes.

**Đối chiếu:** nhóm 4; K35; mức Nền tảng. **Kiến thức và bẫy:** Mặc định inner; giữ cặp khớp khác left giữ hàng chưa khớp. **Đọc lại:** BG §4; NB ô 113–115.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-018

(a) Không lỗi: hiệu Series có đủ ba nhãn A,B,C, nhưng ndarray bỏ nhãn. Thứ tự dữ liệu hiệu là A=10,B=30,C=10; khi gán vào thứ tự C,A,B thì lech theo A,B,C thành [30,10,10]. (b) `d['lech']=moi-d['gia']`. (c) Đúng A=20−10=10, B=90−60=30, C=40−30=10. Đảo thứ tự d và moi độc lập, tính lại rồi so theo cùng danh sách A,B,C; giá trị theo mã phải không đổi.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm không lỗi và kết quả sai; (b) 1 điểm giữ nhãn; (c) 1 điểm kết quả và thử đảo thứ tự.

**Đối chiếu:** nhóm 1; K03, K01, K07; mức Phân loại. **Kiến thức và bẫy:** to_numpy bỏ nhãn; cùng độ dài vẫn có thể ghép sai đối tượng; Phép toán Series ghép đúng mã dù đảo thứ tự; Gán list/ndarray theo vị trí; RHS Series dài hơn có thể khớp nhưng ndarray lỗi độ dài. **Đọc lại:** BG §1; GK câu 10 (biến thể cùng độ dài nhưng sai âm thầm).

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-019

(a) Mask có nhãn khu A,B, không khớp nhãn hàng 10…60, gây IndexingError. (b) `du=d.loc[d.groupby('khu')['id'].transform('nunique')>=2].copy()`. Cũng nhận groupby.filter theo id.nunique. A đạt với P,Q; B chỉ R. (c) `du['lech']=du['gia']-du.groupby('id')['gia'].transform('mean')`. Giữ index [10,20,30], mean của P là 30 và Q là 80; lech=[−10,10,0]. Đếm size snapshot sẽ sai tiêu chí listing khác nhau; nhóm khu để trừ sẽ sai đối tượng so sánh.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm cấp mask/nhãn và lỗi; (b) 1 điểm lọc đúng hai listing; (c) 1 điểm đúng khóa id, index và ba giá trị.

**Đối chiếu:** nhóm 3; K24, K25, K23; mức Phân loại. **Kiến thức và bẫy:** Thống kê/mask cấp nhóm khác cấp hàng; căn nhãn sai tạo NaN hoặc mask lỗi IndexingError; Review/snapshot khác listing; nunique khác size; chọn đúng khóa khi tính độ lệch; transform trả từng hàng, giữ index sau lọc; hàng thiếu giá vẫn nhận thống kê nhóm. **Đọc lại:** BG §3; GK câu 23 (đổi đơn vị thành listing–snapshot).

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-020

n_host=[2,2,1]: H còn P,R sau lọc giá, K còn S. Chạy lại từ goc cố định cho cùng kết quả và không sửa goc, nhưng ổn định không chứng minh đúng phạm vi diễn giải: H có 3 listing trong goc, gồm Q thiếu giá. Cách đếm toàn bộ trước: `day_du=goc.assign(n_host=lambda d:d.groupby('host')['id'].transform('size'))`; `co=day_du.loc[day_du['gia'].notna()]`. Khi đó n_host theo P,R,S=[3,3,1].

**Hướng dẫn chấm:** 2 điểm: hai bộ đếm và tập hàng 1 điểm; chạy lại/không suy đúng phạm vi 0,5; sửa thứ tự 0,5.

**Đối chiếu:** nhóm 5; K27, K43; mức Vận dụng. **Kiến thức và bẫy:** Lọc trước thống kê khác thống kê toàn nhóm rồi lọc; transform size chỉ biết phạm vi bảng hiện tại; Chạy lại cập nhật đơn vị trên kết quả cũ tiếp tục chia; assign không tự chống lỗi này. **Đọc lại:** BG §5; NB ô 137–144.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR03

**Đáp án: D.**

- A sai: đó là đếm giá biết theo từng hàng, tức axis=1.
- B sai: dùng len thay count nên tính cả NaN.
- C sai: bỏ nhãn cột khi mô tả Series trả về từ apply.
- D đúng: hàm nhận mỗi cột Series; count tính cả phí 0 và bỏ ô thiếu.

**Đối chiếu:** nhóm 2; K52; mức Bổ sung. **Kiến thức và bẫy:** apply axis=0 nhận cột; tên/nhãn đầu ra là cột, khác axis=1. **Đọc lại:** NB ô 152–153: tự học apply theo cột.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-MR04

`d['tb_khu']=d['khu'].map(tb)`. tb có A=20, B=30; kết quả theo index [7,2,9,5] là [30,20,30,20]. map tra giá trị khu A/B và giữ index từng hàng. Gán tb trực tiếp sẽ căn nhãn A,B vào index số 7,2,9,5, tất cả không khớp nên NaN. Hàng 5 vẫn nhận mean khu A từ giá biết 20; riêng chênh lệch giá của hàng 5 vẫn thiếu. Tương đương groupby('khu')['gia'].transform('mean').

**Hướng dẫn chấm:** 2 điểm: lệnh map 0,75; giá trị/index 0,5; phân biệt căn nhãn và hàng thiếu 0,75.

**Đối chiếu:** nhóm 3; K53, K23; mức Bổ sung. **Kiến thức và bẫy:** map bằng Series thống kê nhóm đưa giá trị về từng hàng; khác gán trực tiếp Series nhóm; transform trả từng hàng, giữ index sau lọc; hàng thiếu giá vẫn nhận thống kê nhóm. **Đọc lại:** NB ô 154–155: map bằng Series thống kê nhóm.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Độ bao phủ sau đợt 2

Đã dùng 30/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K05, K06, K12, K13, K14, K15, K16, K21, K26, K28, K29, K30, K31, K37, K38, K39, K41, K44, K45, K46, K47, K48, K51, K54, K55, K56. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 3

### Câu trọng tâm

#### B5-021

**Đáp án: B.**

- A sai: pandas chỉ dùng nhãn hiện tại, không nhớ ý nghĩa mã đã bị người dùng thay.
- B đúng: đặt lại nhãn không sắp lại giá trị; giá 100 của B bị gắn nhãn A, giá 30 của A bị gắn nhãn B.
- C sai: độ dài không xác nhận giá trị đi đúng đối tượng.
- D sai: thao tác thay nhãn có thể chạy; vấn đề là ý nghĩa sai âm thầm.

**Đối chiếu:** nhóm 1; K01, K03; mức Nền tảng. **Kiến thức và bẫy:** Phép toán Series ghép đúng mã dù đảo thứ tự; to_numpy bỏ nhãn; cùng độ dài vẫn có thể ghép sai đối tượng. **Đọc lại:** BG §1; NB ô 6–10.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-022

**Đáp án: B.**

- A sai: tự biến chưa biết phí thành miễn phí.
- B đúng: phí can được xác nhận bằng 0; phí la chưa biết và lan truyền thiếu qua công thức.
- C sai: nhân cả phí phong theo số đêm dù phí một lần.
- D sai: nhầm số 0 hợp lệ với NaN.

**Đối chiếu:** nhóm 2; K08, K09, K13; mức Vận dụng. **Kiến thức và bẫy:** map dict tra theo giá trị khác gán Series căn theo index; Thiếu bảng phí là chưa biết; sum/count/len sau map dùng tập giá trị khác nhau; Tiền nhiều đêm, phí một lần, miễn phí từ đúng 7 đêm; lan truyền thiếu theo nghiệp vụ. **Đọc lại:** BG §2; LAB bước 6 về phí chưa biết.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-023

**Đáp án: A.**

- A đúng: hàng 2 thiếu giá nhưng vẫn nhận mean A=(10+50)/2=30; transform giữ index bảng đầu vào.
- B sai: tưởng giá trị đầu vào thiếu buộc thống kê nhóm gắn về hàng cũng thiếu.
- C sai: tưởng transform tự reset index sau lọc.
- D sai: nhầm transform với aggregate mean cấp nhóm.

**Đối chiếu:** nhóm 3; K23; mức Nền tảng. **Kiến thức và bẫy:** transform trả từng hàng, giữ index sau lọc; hàng thiếu giá vẫn nhận thống kê nhóm. **Đọc lại:** BG §3; NB ô 79–88.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-024

**Đáp án: B.**

- A sai: tưởng ignore_index khử id P trùng giữa các đợt.
- B đúng: hợp tên cột id,dot,gia,phi; hai snapshot đợt 2 thiếu gia nên mean dùng 10,30, mẫu số 2.
- C sai: chia tổng 40 cho cả 4 hàng thay vì 2 giá biết.
- D sai: ghép phi vào vị trí cột gia rồi tính (10+30+5+8)/4.

**Đối chiếu:** nhóm 4; K32, K33; mức Vận dụng. **Kiến thức và bẫy:** concat thêm quan sát, khớp tên cột; ignore_index không khử mã trùng; Mỗi hàng listing–snapshot; lặp id giữa hai đợt có thể hợp lệ. **Đọc lại:** BG §4; NB ô 97–100.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-025

**Đáp án: C.**

- A sai: các callable được đánh giá theo thứ tự cột được thêm trong lời gọi này.
- B sai: bỏ qua cột mà biểu thức chỉ rõ.
- C đúng: hai=[20,40], cộng phí một lần 5; d vẫn chỉ có gia.
- D sai: giá trị r đúng nhưng nhầm assign sửa bảng đầu vào.

**Đối chiếu:** nhóm 5; K44, K42; mức Vận dụng. **Kiến thức và bẫy:** Callable assign nhận bảng hiện tại; truyền hàm khác gọi hàm thiếu đối số; dùng cột vừa thêm; assign trả bảng mới; đầu vào giữ nguyên trong cách dùng đúng. **Đọc lại:** BG §5 ghi chú callable; NB ô 138–141.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-026

**Đáp án: A.**

- A đúng: các khoảng [0,30),[30,100),[100,∞); NaN không phải một nhóm giá hợp lệ.
- B sai: xếp riêng biên 100 vào khoảng trung dù khoảng này loại cận 100.
- C sai: xếp riêng biên 30 vào khoảng re dù khoảng này loại cận 30.
- D sai: tự điền giá thiếu bằng 0 trước khi chia nhóm.

**Đối chiếu:** nhóm 2; K14, K10; mức Nền tảng. **Kiến thức và bẫy:** cut ngưỡng đặt trước, right=False, nhóm giá hợp lệ khác NaN; map hàm phân loại: xử lý NaN trước if/elif/else và đúng biên. **Đọc lại:** BG §2; LAB bước 1.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-027

**Đáp án: C.**

- A sai: dùng count trên gia thay size trên id cho cột n; giá thiếu không làm listing biến mất.
- B sai: coi giá NaN của Q là 0 khi lấy median.
- C đúng: H có P,Q; median dùng một giá 10; mean review dùng cả 0 và 4, mẫu số 2. Review không tự bằng booking.
- D sai: dùng sum review thay mean hoặc loại 0 khỏi mẫu số.

**Đối chiếu:** nhóm 3; K20, K18, K31; mức Vận dụng. **Kiến thức và bẫy:** agg trên Series và named aggregation nhiều cột; một hàng mỗi nhóm; Split–apply–combine; hàng cùng nhóm không cần liên tiếp; mean/median bỏ giá thiếu; Review là proxy, bảng chéo và chênh lệch chưa chứng minh nhân quả/đắt vô lý. **Đọc lại:** BG §3; LAB bước 2.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-028

(a) Mặc định inner: P và R mỗi listing khớp hai hàng A, Q khớp một B; 5 hàng, mất S. (b) `m=d.merge(phi,on='khu',how='left',indicator=True)`; thêm S chưa khớp thành 6 hàng. (c) Phi thiếu 3: P và R mỗi mã có một cặp A đã khớp nhưng phi gốc thiếu, trạng thái both; S thêm một NaN do C không đối ứng, left_only. Vậy both=5, left_only=1; đếm NaN không đồng nghĩa đếm khóa chưa khớp.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm cặp và hàng mất; (b) 1 điểm left/6 hàng; (c) 1 điểm ba NaN, một left_only và nguyên nhân.

**Đối chiếu:** nhóm 4; K35, K36, K38; mức Phân loại. **Kiến thức và bẫy:** Mặc định inner; giữ cặp khớp khác left giữ hàng chưa khớp; Khóa lặp hai phía tạo các cặp; left có thể tăng hàng; đếm bằng bội số từng khóa; indicator both/left_only; NaN bên phải có thể đã khớp nhưng thiếu thông tin. **Đọc lại:** BG §4; GK câu 12 (biến thể default inner và phí thiếu đã khớp).

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-029

Hiện tại nhóm host: H mean (20+100)/2=60, K mean 40 nên lech=[−40,40,0], sai tập so sánh. Sửa `x['lech']=x['gia']-x.groupby('khu')['gia'].transform('mean')`. Trong tập nguyên căn, A gồm 20,40 mean30; B chỉ 100 mean100, không gồm phòng riêng 500. Kết quả đúng [−10,0,10], giữ index [0,1,2]. Lệch dương chỉ cho biết cao hơn mean khu của tập đang xét; chưa có bằng chứng về diện tích/chất lượng để kết luận không hợp lý hay nhân quả.

**Hướng dẫn chấm:** 2 điểm: kết quả hiện tại/khóa host sai 0,5; sửa và đúng tập nguyên căn 0,75; kết quả đúng 0,5; giới hạn diễn giải 0,25.

**Đối chiếu:** nhóm 3; K23, K25, K31; mức Vận dụng. **Kiến thức và bẫy:** transform trả từng hàng, giữ index sau lọc; hàng thiếu giá vẫn nhận thống kê nhóm; Review/snapshot khác listing; nunique khác size; chọn đúng khóa khi tính độ lệch; Review là proxy, bảng chéo và chênh lệch chưa chứng minh nhân quả/đắt vô lý. **Đọc lại:** BG §3 so giá nguyên căn; NB ô 64–66,86–88.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-030

r lấy hợp A,B,C,D,E: 5 nhãn, chỉ B có hai toán hạng nên r[B]=21; bốn nhãn khác thiếu. Gán Series trở lại d giữ ba hàng A,B,C, không thêm D,E; tong=[NaN,21,NaN], chỉ hai giá thiếu còn trong bảng d. Không đủ dữ liệu để khẳng định A,C không có phí: chưa biết phí khác với phí 0. D,E có phí nhưng không có giá trong d nên cũng chưa tính được tổng. Phép toán tạo hợp nhãn khác phép gán căn vào hàng sẵn có.

**Hướng dẫn chấm:** 2 điểm: r và nhãn/tập thiếu 0,75; d/tong/hàng không thêm 0,75; diễn giải chưa biết không bằng 0 0,5.

**Đối chiếu:** nhóm 1; K02, K05, K09; mức Phân loại. **Kiến thức và bẫy:** Hợp nhãn trong phép toán; thiếu toán hạng khác giá bằng 0; Gán Series căn theo index bảng; giữ hàng bảng, thêm NaN nhưng không thêm nhãn mới; Thiếu bảng phí là chưa biết; sum/count/len sau map dùng tập giá trị khác nhau. **Đọc lại:** BG §1 và §2 phí chưa biết.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR05

**Đáp án: B.**

- A sai: mặc định đưa nhãn cũ thành cột, không dùng drop=True.
- B đúng: reset_index tạo kết quả mới, đưa khóa nhóm về cột, không tự sửa t.
- C sai: thao tác chỉ đổi cách lưu nhãn, không đảo ngược phép tổng hợp.
- D sai: không có inplace=True; t không thay đổi.

**Đối chiếu:** nhóm 3; K54; mức Bổ sung. **Kiến thức và bẫy:** reset_index tạo bảng mới, đưa khóa nhóm thành cột và giữ khóa khi xuất index=False. **Đọc lại:** BG §3 tự học; NB ô 62–63.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-MR06

**Đáp án: C.**

- A sai: đánh dấu cả lần đầu như keep=False, trái mặc định đã nêu.
- B sai: tưởng tạo mask duplicated đồng thời xoá hàng.
- C đúng: duplicated đánh dấu lần lặp sau lần đầu, không xóa dữ liệu; set_index cho phép lặp.
- D sai: không có bước khử trùng hay kiểm tính duy nhất tự động.

**Đối chiếu:** nhóm 1; K51, K50; mức Bổ sung. **Kiến thức và bẫy:** index.duplicated giữ lần đầu mặc định; set_index không khử mã lặp; Chỉ mục lặp: loc một nhãn trả nhiều phần tử; is_unique. **Đọc lại:** NB ô 150–151: tự học duplicated.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Độ bao phủ sau đợt 3

Đã dùng 38/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K12, K15, K16, K21, K26, K28, K29, K30, K37, K39, K41, K45, K46, K47, K48, K55, K56. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 4

### Câu trọng tâm

#### B5-031

**Đáp án: C.**

- A sai: nhầm việc đặt index với kiểm khóa duy nhất.
- B sai: set_index không tự tổng hợp hay chọn bản ghi cuối.
- C đúng: đưa mã vào index không tự kiểm hoặc khử mã lặp.
- D sai: tính duy nhất phụ thuộc giá trị nhãn lặp, không phải kiểu chuỗi.

**Đối chiếu:** nhóm 1; K04; mức Nền tảng. **Kiến thức và bẫy:** set_index không bảo đảm mã duy nhất; kiểm index.is_unique. **Đọc lại:** BG §1; NB ô 14–16.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-032

**Đáp án: A.**

- A đúng: 7 không chia đều thành 3 nhóm; khoảng 6 đến 100 rất lớn nhưng thứ hạng vẫn quyết định phân vị.
- B sai: số hàng phải nguyên, không thể có một phần ba listing.
- C sai: đó là ý tưởng khoảng giá đều, không phải phân vị.
- D sai: qcut không yêu cầu số hàng chia hết số nhóm; dữ liệu này có mốc hợp lệ.

**Đối chiếu:** nhóm 2; K15; mức Vận dụng. **Kiến thức và bẫy:** qcut dùng phân vị tập hiện tại; gần cân bằng số lượng khác đều độ rộng giá. **Đọc lại:** BG §2; NB ô 46–52.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-033

**Đáp án: B.**

- A sai: lấy (50+100)/2, coi hai khu có trọng số bằng nhau.
- B đúng: tổng giá 50*1+100*3=350, chia 1+3=4 giá biết.
- C sai: dùng size làm trọng số: (50*4+100*3)/(4+3), gán giá trung bình cho cả ba listing thiếu của A.
- D sai: giữ tử 350 từ các giá biết nhưng chia cho 7 hàng bao gồm ba giá thiếu.

**Đối chiếu:** nhóm 3; K22, K19; mức Vận dụng. **Kiến thức và bẫy:** Gộp mean phải dùng count đúng trọng số; không gộp median bằng công thức mean; size đếm hàng, count đếm giá biết, nunique đếm đối tượng khác nhau. **Đọc lại:** BG §3 bài tập 3; biến thể có thiếu và trọng số hàng.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-034

**Đáp án: B.**

- A sai: tưởng mỗi hàng trái chỉ ghép một hàng phải dù A lặp.
- B đúng: A có 2*3=6 cặp, B có 1*1=1; left thêm một hàng C chưa khớp, inner không thêm.
- C sai: quên giữ hàng C chưa khớp trong left.
- D sai: ghép tất cả 4*4 hàng không xét điều kiện khu.

**Đối chiếu:** nhóm 4; K36, K35; mức Vận dụng. **Kiến thức và bẫy:** Khóa lặp hai phía tạo các cặp; left có thể tăng hàng; đếm bằng bội số từng khóa; Mặc định inner; giữ cặp khớp khác left giữ hàng chưa khớp. **Đọc lại:** BG §4; GK câu 12 (biến thể đếm cả inner và left).

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-035

**Đáp án: D.**

- A sai: gọi ngay nhưng thiếu đối số t, gây TypeError.
- B sai: hàm chạy trước assign trên price cũ, trả [10,20], hợp cú pháp nhưng sai nguồn tính.
- C sai: chuỗi chỉ là giá trị được gán lặp, không phải tham chiếu đến hàm.
- D đúng: truyền callable, assign gọi với bảng hiện tại đã có price mới.

**Đối chiếu:** nhóm 5; K44, K45; mức Vận dụng. **Kiến thức và bẫy:** Callable assign nhận bảng hiện tại; truyền hàm khác gọi hàm thiếu đối số; dùng cột vừa thêm; Cột phụ thuộc phải tính lại từ nguồn đúng sau khi cột nguồn đổi. **Đọc lại:** BG §5; NB ô 136–141.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-036

**Đáp án: C.**

- A sai: nhầm filter giữ hàng nguồn với bảng tổng hợp cấp nhóm.
- B sai: nhầm GroupBy.filter nhận nhóm với apply nhận hàng.
- C đúng: A có ba listing, B hai, C một; filter giữ mọi hàng của A,B.
- D sai: filter trong ví dụ giữ index hàng gốc, không tự đặt lại.

**Đối chiếu:** nhóm 3; K26, K18; mức Vận dụng. **Kiến thức và bẫy:** GroupBy.filter nhận cả nhóm, trả bool và giữ các hàng gốc của nhóm đạt điều kiện; Split–apply–combine; hàng cùng nhóm không cần liên tiếp; mean/median bỏ giá thiếu. **Đọc lại:** BG §3; NB ô 82–85.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-037

**Đáp án: C.**

- A sai: áp yêu cầu one_to_one thay many_to_one.
- B sai: validate chỉ kiểm quan hệ, không tổng hợp hay loại bản ghi.
- C đúng: m:1 yêu cầu phía phải duy nhất, không bắt phía trái duy nhất.
- D sai: không có khóa phải lặp trong dữ liệu này; validate cũng không tự chọn/sửa nếu có lặp.

**Đối chiếu:** nhóm 4; K37; mức Nền tảng. **Kiến thức và bẫy:** validate m:1 kiểm khóa phải duy nhất, cho phép khóa trái lặp; không sửa hay chọn dòng hộ. **Đọc lại:** BG §4; NB ô 119–124.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-038

(a) r=[re,trung,cao,cao]; NaN rơi vào else vì hai so sánh đều False. (b) Thêm ngay đầu hàm `if pd.isna(x): return None`, giữ các nhánh ngưỡng sau. (c) Kiểm 50→trung,100→cao và `pd.isna(r.iloc[3])`; không chỉ đếm ba nhóm đã biết. Với giá không âm: `r=pd.cut(s,[0,50,100,np.inf],labels=['re','trung','cao'],right=False)`. Nhận hàm trả np.nan thay None; khác dtype phân loại không làm lời giải sai.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm nguyên nhân NaN; (b) 1 điểm xử lý thiếu trước phân nhánh; (c) 1 điểm kiểm biên/thiếu và cut đúng.

**Đối chiếu:** nhóm 2; K10, K14; mức Vận dụng. **Kiến thức và bẫy:** map hàm phân loại: xử lý NaN trước if/elif/else và đúng biên; cut ngưỡng đặt trước, right=False, nhóm giá hợp lệ khác NaN. **Đọc lại:** LAB bước 1, ô 8–9; BG §2 cut.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-039

(a) [2,2,2,2]; H bị mất Q phòng riêng khi lọc nên lệch 3 của nguồn, không chứng minh nguồn sai. (b) `day_du=goc.assign(n_host=lambda d:d.groupby('host')['id'].transform('size'))`; `x=day_du.loc[day_du['loai']=='can'].copy()`. (c) Khi đó n_host=[3,3,2,2], P,R thuộc H chuyên nghiệp: tỷ lệ listing 2/4=0.5. Code cũ cho 0/4=0 vì đếm sau lọc. Đây không phải tỷ lệ host chuyên nghiệp; thống kê chỉ có nghĩa trong phạm vi đã nêu.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm đếm và phạm vi; (b) 1 điểm đổi thứ tự; (c) 1 điểm hai tỷ lệ, đúng đơn vị listing.

**Đối chiếu:** nhóm 3; K27, K29, K28; mức Phân loại. **Kiến thức và bẫy:** Lọc trước thống kê khác thống kê toàn nhóm rồi lọc; transform size chỉ biết phạm vi bảng hiện tại; Dựng lại cột đếm nhà cung cấp; lệch phạm vi chưa chứng minh nguồn sai; Tỷ lệ listing thuộc host chuyên nghiệp khác tỷ lệ host; trọng số listing khác host ngang nhau. **Đọc lại:** BG §3 dựng cột nhà cung cấp; NB ô 93–95; BG §5 chuỗi.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-040

H tạo 2*2=4 cặp (P hai lần, Q hai lần); K một cặp, tổng 5 hàng. Tổng gia=2*10+2*30+100=180; tỷ lệ chuyen=4/5=0.8. Nếu mỗi host một hàng đúng: tổng listing=3, tổng gia=140, tỷ lệ 2/3. Các listing H bị tăng trọng số, không phải xuất hiện thêm listing thật. Dùng `d.merge(h,on='host',how='left',validate='m:1')` để gây MergeError vì khóa phải lặp; validate không tự chọn hay sửa h.

**Hướng dẫn chấm:** 2 điểm: cặp/số hàng 0,5; tổng và hai tỷ lệ 0,75; tăng trọng số 0,25; validate và không tự sửa 0,5.

**Đối chiếu:** nhóm 4; K36, K40, K37; mức Phân loại. **Kiến thức và bẫy:** Khóa lặp hai phía tạo các cặp; left có thể tăng hàng; đếm bằng bội số từng khóa; Ghép host về listing theo nhiều–một; nhân hàng làm lệch tổng, tỷ lệ, trọng số; validate m:1 kiểm khóa phải duy nhất, cho phép khóa trái lặp; không sửa hay chọn dòng hộ. **Đọc lại:** BG §4 ghép host về listing; NB ô 122–124.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR07

**Đáp án: D.**

- A sai: tự loại Q dù yêu cầu giữ mọi đồng hạng.
- B sai: tự chọn lần xuất hiện cuối của đồng hạng A.
- C sai: lấy max toàn thị trường 30 thay max từng khu.
- D đúng: A có hai listing đồng hạng 20; B chỉ S đạt max30. transform trả max về từng hàng rồi so.

**Đối chiếu:** nhóm 3; K55; mức Bổ sung. **Kiến thức và bẫy:** transform max chọn top mỗi quận, đồng hạng có thể nhiều listing. **Đọc lại:** LAB tự làm 1, ô 24.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-MR08

Mặc định bỏ phân khúc thiếu: A cao=1/2, B cao=2/3; mẫu số là số listing có nhãn phân khúc trong từng khu (2 và 3). Muốn mẫu số toàn listing của khu: `r=d.groupby('khu')['phan'].value_counts(normalize=True,dropna=False)`; cao A=1/3, B=2/3, cùng mẫu số 3. Dữ liệu thiếu là nhóm chưa biết, không được diễn giải là chắc chắn không cao. Tỷ lệ nhãn cao toàn bảng là 3/6 nếu giữ thiếu trong mẫu số, hoặc 3/5 nếu chỉ biết nhãn; cả hai không thay cho cơ cấu từng khu.

**Hướng dẫn chấm:** 2 điểm: tỷ lệ/mẫu số mặc định 0,75; lệnh và tỷ lệ giữ thiếu 0,75; không nhầm toàn bảng và giải thích thiếu 0,5.

**Đối chiếu:** nhóm 3; K56; mức Bổ sung. **Kiến thức và bẫy:** value_counts normalize theo từng quận; mẫu số và thiếu; khác tỷ lệ toàn thành phố. **Đọc lại:** LAB tự làm 2, ô 24; LAB bước 1 value_counts dropna=False.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Độ bao phủ sau đợt 4

Đã dùng 46/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K12, K16, K21, K30, K39, K41, K46, K47, K48. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 5

### Câu trọng tâm

#### B5-041

**Đáp án: C.**

- A sai: nhầm gán Series với phép toán lấy hợp nhãn.
- B sai: gán Series theo vị trí thay nhãn.
- C đúng: chỉ A có nhãn khớp; D trong s không tự thêm hàng vào DataFrame.
- D sai: đó không phải quy tắc độ dài của gán Series có index; pandas căn nhãn.

**Đối chiếu:** nhóm 1; K05; mức Nền tảng. **Kiến thức và bẫy:** Gán Series căn theo index bảng; giữ hàng bảng, thêm NaN nhưng không thêm nhãn mới. **Đọc lại:** BG §1; NB ô 17–19.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-042

**Đáp án: D.**

- A sai: nhầm thành viên/thứ hạng giữ với ngưỡng giá giữ.
- B sai: bỏ qua việc các giá cũng tăng theo cùng phép biến đổi.
- C sai: khái quát quá điều kiện cùng tập đối tượng và cùng quy tắc phân vị.
- D đúng: biến đổi affine dương giữ thứ tự và biến đổi các mốc cùng công thức; b2=2*b1+5.

**Đối chiếu:** nhóm 2; K16, K15; mức Vận dụng. **Kiến thức và bẫy:** Cùng tập đối tượng biến đổi affine dương: nhóm qcut giữ, mốc đổi; giới hạn khi đổi thành phần; qcut dùng phân vị tập hiện tại; gần cân bằng số lượng khác đều độ rộng giá. **Đọc lại:** BG §2; NB ô 50–52; GK câu 13.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-043

**Đáp án: A.**

- A đúng: mỗi khu một hàng, mỗi loại một cột; A có giá đo 0, B không có tổ hợp phòng riêng nên ô trống.
- B sai: giữ số tổ hợp của dạng dài thay shape sau unstack.
- C sai: tự thay tổ hợp không quan sát bằng giá đo 0.
- D sai: coi giá 0 hợp lệ là thiếu dữ liệu.

**Đối chiếu:** nhóm 3; K21, K18; mức Vận dụng. **Kiến thức và bẫy:** Nhiều khóa, dạng dài/rộng, unstack; tổ hợp không có dữ liệu khác số 0; Split–apply–combine; hàng cùng nhóm không cần liên tiếp; mean/median bỏ giá thiếu. **Đọc lại:** BG §3; NB ô 69–75.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-044

**Đáp án: C.**

- A sai: coi NaN bên phải luôn là không khớp khóa.
- B sai: cho rằng đã both thì mọi cột thông tin đều đầy đủ.
- C đúng: B có khóa khớp nhưng phí gốc thiếu; D không có đối ứng.
- D sai: đảo nguyên nhân thiếu giá trị đã khớp với thiếu khóa đối ứng.

**Đối chiếu:** nhóm 4; K38; mức Nền tảng. **Kiến thức và bẫy:** indicator both/left_only; NaN bên phải có thể đã khớp nhưng thiếu thông tin. **Đọc lại:** BG §4; NB ô 107–112.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-045

**Đáp án: D.**

- A sai: pandas lưu kết quả cột, không lưu công thức tự tính lại như vậy.
- B sai: assign cho phép thay cột trong bảng mới.
- C sai: tên biến không thay nguồn tính hay giá trị dẫn xuất.
- D đúng: cột phụ thuộc không tự cập nhật khi nguồn thay; đúng phải [30,50].

**Đối chiếu:** nhóm 5; K45, K44; mức Vận dụng. **Kiến thức và bẫy:** Cột phụ thuộc phải tính lại từ nguồn đúng sau khi cột nguồn đổi; Callable assign nhận bảng hiện tại; truyền hàm khác gọi hàm thiếu đối số; dùng cột vừa thêm. **Đọc lại:** BG §5; NB ô 142–144.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-046

**Đáp án: A.**

- A đúng: H,K chuyên nghiệp nắm 7/8 listing nhưng chỉ 2/3 host; mean host=(20+80+140)/3=80, mean listing=(5*20+2*80+140)/8=50.
- B sai: đảo đơn vị/mẫu số của hai tỷ lệ.
- C sai: dùng mean các mean host không trọng số làm mean listing.
- D sai: dùng trọng số listing cho cả thống kê cần mỗi host ngang nhau.

**Đối chiếu:** nhóm 3; K28, K22; mức Vận dụng. **Kiến thức và bẫy:** Tỷ lệ listing thuộc host chuyên nghiệp khác tỷ lệ host; trọng số listing khác host ngang nhau; Gộp mean phải dùng count đúng trọng số; không gộp median bằng công thức mean. **Đọc lại:** BG §3 đơn vị host; NB ô 89–92; LAB bước 3.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-047

Một cách theo cột:
```python
phi_tinh = d['phi'].copy()
phi_tinh.loc[d['so_dem']>=7] = 0
tong = d['gia']*d['so_dem'] + phi_tinh
```
Kết quả [65,140,NaN,NaN], giữ nhãn A,B,C,D. C vẫn thiếu vì chưa biết giá, dù phí đã được miễn; D chưa biết phí và không đủ đêm miễn. Kiểm A=6*10+5=65 (không nhân phí), B đúng 7 đêm vẫn trả 7*20=140. Nhận apply đúng quy tắc; không coi apply luôn sai hoặc ép dùng một API cụ thể.

**Hướng dẫn chấm:** 2 điểm: công thức/phí một lần 0,75; >=7 gồm phí thiếu được miễn 0,5; kết quả và lan truyền thiếu 0,5; kiểm hai ca 0,25.

**Đối chiếu:** nhóm 2; K13, K12; mức Vận dụng. **Kiến thức và bẫy:** Tiền nhiều đêm, phí một lần, miễn phí từ đúng 7 đêm; lan truyền thiếu theo nghiệp vụ; Phép toán trực tiếp trên cột và apply: tính đúng trước hiệu năng; không tự vector hoá hàm Python. **Đọc lại:** BG §2 bài tập 2; NB ô 42–45.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-048

(a) Assert qua vì vẫn đủ 4 id khác nhau, nhưng H tạo 2*2=4 cặp và J,K mỗi mã một cặp: m có 6 hàng. nunique không kiểm mỗi listing chỉ có một hàng. (b) Dùng `validate='m:1'` trong merge: gây MergeError vì H lặp bên phải, không tự sửa phí. (c) Chưa biết phí 2 hay 5 đúng nên không chọn dòng đầu tuỳ ý. Sau khi có bảng phí đúng: kiểm khóa phải duy nhất; merge left với validate và indicator; kiểm len, id duy nhất, left_only và cột phí thiếu riêng. Các kiểm này vẫn cần đối chiếu ý nghĩa/mức phí nguồn, không tự chứng minh nghiệp vụ đúng.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm assert/6 hàng; (b) 1 điểm ràng buộc và MergeError; (c) 1 điểm không chọn tuỳ ý và kiểm sau sửa.

**Đối chiếu:** nhóm 4; K37, K41, K39; mức Phân loại. **Kiến thức và bẫy:** validate m:1 kiểm khóa phải duy nhất, cho phép khóa trái lặp; không sửa hay chọn dòng hộ; Không tự drop_duplicates ép số hàng khi chưa biết bản ghi đúng; kiểm số hàng/khóa/độ khớp; validate và len bằng nhau không bảo đảm mọi khóa khớp hay thông tin đủ/đúng. **Đọc lại:** BG §4 validate, khóa lặp; LAB bước 6 kiểm sau ghép.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-049

tb có A=30,B=50, còn giá có index 4,7,9,12: phép trừ lấy hợp 6 nhãn, không có nhãn chung nên r có 6 NaN. Sửa `r=d['gia']-d.groupby('khu')['gia'].transform('mean')`, giữ bốn index, giá trị [−20,−20,20,20]. Lọc `du=d.groupby('khu').filter(lambda nhom:nhom['gia'].mean()>=40)`: giữ khu B, index [7,12]. Filter nhận cả nhóm và trả bool; không dùng trực tiếp Series bool A,B làm mask hàng số.

**Hướng dẫn chấm:** 2 điểm: hợp nhãn/NaN 0,5; transform và bốn giá trị 0,75; filter và index giữ 0,75.

**Đối chiếu:** nhóm 3; K24, K26, K23; mức Vận dụng. **Kiến thức và bẫy:** Thống kê/mask cấp nhóm khác cấp hàng; căn nhãn sai tạo NaN hoặc mask lỗi IndexingError; GroupBy.filter nhận cả nhóm, trả bool và giữ các hàng gốc của nhóm đạt điều kiện; transform trả từng hàng, giữ index sau lọc; hàng thiếu giá vẫn nhận thống kê nhóm. **Đọc lại:** BG §3; NB ô 76–85.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-050

(a) ndarray dài 4 không khớp 3 hàng, gây ValueError. Cắt còn ba cho [9,5,7] theo B,C,A, nhưng đã lấy phí D=9 gán B và làm sai cả A,C. (b) `d['phi']=s`; Series dài hơn được căn theo nhãn có sẵn. (c) Đúng B=3,C=7,A=5; D bị bỏ qua, d vẫn ba hàng. Kiểm giá theo từng mã, đảo thứ tự d/s rồi tính lại; không dùng độ dài bằng nhau làm chứng cứ ghép đúng. Cách reindex theo d.index trước khi lấy mảng cũng hợp lệ nếu giữ đúng nhãn.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm lỗi độ dài và ba giá gán sai; (b) 1 điểm Series căn nhãn; (c) 1 điểm kết quả/không thêm D và kiểm mã.

**Đối chiếu:** nhóm 1; K07, K05, K03; mức Phân loại. **Kiến thức và bẫy:** Gán list/ndarray theo vị trí; RHS Series dài hơn có thể khớp nhưng ndarray lỗi độ dài; Gán Series căn theo index bảng; giữ hàng bảng, thêm NaN nhưng không thêm nhãn mới; to_numpy bỏ nhãn; cùng độ dài vẫn có thể ghép sai đối tượng. **Đọc lại:** BG §1; GK câu 10 (biến thể Series dài hơn và sửa bằng cắt độ dài).

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR09

**Đáp án: A.**

- A đúng: không kết luận mọi cách dùng to_numpy đều sai; ở đây sự căn chỉnh đã được thực hiện rõ trước đó.
- B sai: bỏ nhãn không đảo lại thứ tự giá trị sau reindex.
- C sai: nhãn mới C nhận thiếu chứ không mặc định 0.
- D sai: nhầm reindex với chọn loc bắt buộc nhãn tồn tại.

**Đối chiếu:** nhóm 1; K49, K03; mức Bổ sung. **Kiến thức và bẫy:** reindex theo danh sách nhãn, thêm nhãn mới nhận thiếu; to_numpy bỏ nhãn; cùng độ dài vẫn có thể ghép sai đối tượng. **Đọc lại:** NB ô 146–147: biến thể tự học reindex rồi chuyển mảng.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-MR10

CSV ở dòng cuối chỉ có cột tb, không có mã host vì mã vẫn ở index của t và index=False bỏ nó. Sửa `u.to_csv('host.csv',index=False)` hoặc `t.reset_index().to_csv('host.csv',index=False)`. Bảng mong đợi: host H,tb30; host K,tb80. u là bảng mới, reset_index không sửa t; không thể suy thao tác trước đã ảnh hưởng đối tượng dùng ở dòng sau. Xuất t với index=True và đặt đúng tên cột host cũng là cách hợp lệ giữ mã, dù khác cách yêu cầu “hai cột” qua u.

**Hướng dẫn chấm:** 2 điểm: xác định mất khóa 0,5; dòng xuất đúng 0,75; hai hàng/mã 0,5; reset không sửa t 0,25.

**Đối chiếu:** nhóm 3; K54, K20; mức Bổ sung. **Kiến thức và bẫy:** reset_index tạo bảng mới, đưa khóa nhóm thành cột và giữ khóa khi xuất index=False; agg trên Series và named aggregation nhiều cột; một hàng mỗi nhóm. **Đọc lại:** BG §3 tự học reset_index; NB ô 62–63.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Độ bao phủ sau đợt 5

Đã dùng 51/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K30, K46, K47, K48. Đã bố trí ở các đợt sau theo danh mục.

## Đợt 6

### Câu trọng tâm

#### B5-051

**Đáp án: A.**

- A đúng: tên listing_id/ma_khac là tên của chỉ mục, không phải các nhãn dùng đối chiếu.
- B sai: nhầm tên của index với giá trị nhãn.
- C sai: không có quy tắc tự bỏ alignment vì tên khác.
- D sai: gán Series ở ví dụ này vẫn căn nhãn bình thường.

**Đối chiếu:** nhóm 1; K06, K05; mức Nền tảng. **Kiến thức và bẫy:** Tên index khác giá trị nhãn dùng để khớp; Gán Series căn theo index bảng; giữ hàng bảng, thêm NaN nhưng không thêm nhãn mới. **Đọc lại:** BG §1 ghi chú tên index; NB ô 17–19.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-052

**Đáp án: A.**

- A đúng: apply không tự vector hoá hàm Python; vẫn có thể là lời giải đúng/rõ cho logic phức tạp, không có tỷ lệ nhanh hơn cần học thuộc.
- B sai: hiệu năng và đúng đắn là hai tiêu chí khác nhau.
- C sai: không có cơ chế tự chuyển mọi hàm Python thành phép toán vector hoá như phát biểu.
- D sai: cùng độ dài không bảo đảm cùng đối tượng, giá trị hay cách xử lý thiếu.

**Đối chiếu:** nhóm 2; K12, K11; mức Vận dụng. **Kiến thức và bẫy:** Phép toán trực tiếp trên cột và apply: tính đúng trước hiệu năng; không tự vector hoá hàm Python; apply axis=1 nhận hàng Series; scalar tạo Series giữ index. **Đọc lại:** BG §2 hiệu năng; NB ô 33–41; BG kiểm chứng AI.

**Kiểm chứng:** Đã kiểm bằng suy luận, chưa chạy (câu cơ chế/thiết kế kiểm chứng, không có output code cần đo).

#### B5-053

**Đáp án: C.**

- A sai: đếm các hàng không khớp thay vì điều kiện ==.
- B sai: transform size chỉ nhóm các hàng đang có, không tự lấy cột đếm sẵn.
- C đúng: chỉ S thuộc K khớp 1; transform size đếm số hàng của bảng đầu vào hiện tại.
- D sai: đếm đúng nhưng kết luận vượt dữ liệu, bỏ khả năng phạm vi khác.

**Đối chiếu:** nhóm 3; K29, K27; mức Vận dụng. **Kiến thức và bẫy:** Dựng lại cột đếm nhà cung cấp; lệch phạm vi chưa chứng minh nguồn sai; Lọc trước thống kê khác thống kê toàn nhóm rồi lọc; transform size chỉ biết phạm vi bảng hiện tại. **Đọc lại:** BG §3; NB ô 93–95.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-054

**Đáp án: B.**

- A sai: nhầm bảng merge cấp listing với bảng h cấp host.
- B đúng: h có một hàng mỗi host; H có P,R,T nên mỗi listing H khớp đúng một hàng host mang n=3.
- C sai: cộng số hàng hai bảng như concat thay vì tạo cặp theo khóa host.
- D sai: đếm mỗi listing riêng thay vì quy mô host được tổng hợp trong h.

**Đối chiếu:** nhóm 4; K40, K37; mức Nền tảng. **Kiến thức và bẫy:** Ghép host về listing theo nhiều–một; nhân hàng làm lệch tổng, tỷ lệ, trọng số; validate m:1 kiểm khóa phải duy nhất, cho phép khóa trái lặp; không sửa hay chọn dòng hộ. **Đọc lại:** BG §3–4; NB ô 90,122–124.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-055

**Đáp án: D.**

- A sai: bỏ qua observed=True chỉ giữ nhóm categorical thực sự xuất hiện.
- B sai: groupby dùng cả P=20 và S=40 trong nhóm re, không chỉ phần tử đầu.
- C sai: code này không chia/ghi đè gia và không sửa goc; không thể gán lỗi chạy lại cho mọi assign.
- D đúng: lọc giá thiếu rồi tính lại từ goc; observed=True bỏ nhóm cao không có listing.

**Đối chiếu:** nhóm 5; K46, K42; mức Vận dụng. **Kiến thức và bẫy:** Chuỗi lọc → assign → groupby → agg từ đầu vào cố định; observed=True chỉ giữ nhóm phân loại xuất hiện; assign trả bảng mới; đầu vào giữ nguyên trong cách dùng đúng. **Đọc lại:** BG §5; NB ô 142–144.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-056

**Đáp án: D.**

- A sai: đồng nhất quan hệ khóa và số hàng với độ khớp/độ đầy đủ nghiệp vụ.
- B sai: không phân biệt thiếu thông tin với thiếu khóa đối ứng.
- C sai: left không loại R; số hàng bằng là nhờ mỗi hàng có tối đa một đối ứng hoặc hàng đệm chưa khớp.
- D đúng: left m:1 có thể giữ C chưa khớp mà vẫn giữ số hàng; khóa B khớp nhưng thông tin bên phải thiếu.

**Đối chiếu:** nhóm 4; K39, K38; mức Vận dụng. **Kiến thức và bẫy:** validate và len bằng nhau không bảo đảm mọi khóa khớp hay thông tin đủ/đúng; indicator both/left_only; NaN bên phải có thể đã khớp nhưng thiếu thông tin. **Đọc lại:** BG §4 validate/indicator; LAB bước 6.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-057

cut cũ=[re,re,trung,trung]; cut mới=[trung,trung,cao,cao], phản ánh vượt ngưỡng tuyệt đối. qcut 2 nhóm giữ P,Q thấp và R,S cao; mốc giữa từ 50000 lên 110000 CLP, không giữ mốc giá cũ. Sau đổi moi/1000, phải dùng bins=[0,50,100,np.inf] nghìn CLP; giữ bins CLP khiến toàn bộ bị xếp re sai đơn vị. Bảo đảm giữ thành viên chỉ trong điều kiện cùng tập đối tượng, không đổi thiếu/quy tắc và biến đổi affine dương đã nêu; thay các điều kiện đó có thể đổi phân vị và thành viên, không khái quát từ ví dụ này.

**Hướng dẫn chấm:** 2 điểm: hai bộ cut 0,5; qcut/mốc đổi 0,5; đơn vị và bins mới 0,5; giới hạn điều kiện 0,5.

**Đối chiếu:** nhóm 2; K14, K16, K17; mức Vận dụng. **Kiến thức và bẫy:** cut ngưỡng đặt trước, right=False, nhóm giá hợp lệ khác NaN; Cùng tập đối tượng biến đổi affine dương: nhóm qcut giữ, mốc đổi; giới hạn khi đổi thành phần; Thống nhất đơn vị tiền và quy ước ngưỡng khi so mốc chụp. **Đọc lại:** BG §2 cut/qcut; NB ô 46–52; GK câu 13.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-058

`pv=d.pivot_table(index='phan',columns='chuyen',values='review',aggfunc='mean')`. Bốn ô: re/False=2 từ (0+4)/2; re/True=8; cao/False=2; cao/True=6 từ một giá biết 6, không chia 2 vì một NaN. pv.shape=(2,2); mỗi hàng là một phân khúc, mỗi ô tổng hợp các listing thuộc cặp phân khúc–kiểu host. Bỏ aggfunc vẫn là mean mặc định, không phải size/count hay sum. Review là proxy; bảng cho chênh lệch mô tả, chưa chứng minh số booking thật hoặc quan hệ nhân quả. Các host có nhiều listing có thể đóng góp nhiều hàng, không phải mỗi host một trọng số ngang nhau.

**Hướng dẫn chấm:** 2 điểm: lệnh/các chiều 0,5; bốn ô và mẫu số 0,75; mặc định/đơn vị hàng 0,5; giới hạn proxy/nhân quả 0,25.

**Đối chiếu:** nhóm 3; K30, K31, K18; mức Vận dụng. **Kiến thức và bẫy:** pivot_table: index/columns/values/aggfunc; mean mặc định khác size/count/sum; Review là proxy, bảng chéo và chênh lệch chưa chứng minh nhân quả/đắt vô lý; Split–apply–combine; hàng cùng nhóm không cần liên tiếp; mean/median bỏ giá thiếu. **Đọc lại:** LAB bước 5, ô 18–20; NB ô 156–157.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-059

(a) Đều qua: bảng phải duy nhất, mọi mã đã bị đổi thành A/B đều khớp, mỗi listing ra một hàng. Nhưng assign thay khu bằng host nên P nhận10 thay20, Q nhận20 thay10; R,S tình cờ đúng. (b) Bỏ bước assign: `m=d.merge(v,on='khu',how='left',validate='m:1',indicator=True)`. (c) Phí đúng [20,10,10,20], ghép theo d.khu gốc. Kiểm từng mã listing với khu nguồn và bảng phí; ví dụ P ở khu B phải nhận20. Điều kiện cấu trúc không chứng minh đã dùng đúng hệ mã; giữ bảng gốc để đối chiếu. Không sửa nhãn khóa cho khớp chỉ để assert qua.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm kiểm qua và P,Q sai; (b) 1 điểm bỏ ghi đè sai hệ mã; (c) 1 điểm giá đúng và kiểm với nguồn nghiệp vụ.

**Đối chiếu:** nhóm 4; K39, K34, K41; mức Phân loại. **Kiến thức và bẫy:** validate và len bằng nhau không bảo đảm mọi khóa khớp hay thông tin đủ/đúng; merge theo giá trị khóa, không theo thứ tự hay index; khác concat; Không tự drop_duplicates ép số hàng khi chưa biết bản ghi đúng; kiểm số hàng/khóa/độ khớp. **Đọc lại:** BG §4 kiểm khóa/ý nghĩa; BG kiểm chứng AI.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-060

(a) Hàm sửa trực tiếp biến ngoài goc thành [40,80]; `... or True` luôn True nên không phát hiện. Chạy lại hai dòng cuối tiếp tục chia, gia_nghin=[0.04,0.08]. (b) Hàm đúng: `def nghin(d): return d['price']/1000`; sau khôi phục, dùng `moi=goc.assign(gia_nghin=nghin)`. (c) Lưu bản goc_truoc, tạo a,b bằng biểu thức đúng từ cùng goc rồi kiểm a bằng b và goc bằng goc_truoc, đồng thời gia_nghin=[40,80]. Bỏ or True và kiểm giá/đơn vị. assign trả bảng mới nhưng không ngăn hàm người dùng sửa trạng thái ngoài; hàm phải thuần theo hợp đồng nhận bảng, trả cột, không sửa nguồn.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm thay đổi, assert vô hiệu và lần hai; (b) 1 điểm hàm dùng tham số không ghi nguồn; (c) 1 điểm kiểm hai kết quả/bảng gốc và ý nghĩa assign.

**Đối chiếu:** nhóm 5; K47, K48, K43; mức Phân loại. **Kiến thức và bẫy:** Hàm trong chuỗi phải không sửa lén đầu vào hoặc trạng thái ngoài; kiểm chạy hai lần và bảng gốc; Kiểm logic mệnh đề assert; assert qua chưa chứng minh toàn bộ yêu cầu; Chạy lại cập nhật đơn vị trên kết quả cũ tiếp tục chia; assign không tự chống lỗi này. **Đọc lại:** BG §5 hàm không sửa bảng; NB ô 136–144; LAB ô 4 assert or True.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Tự học bổ sung — ưu tiên thấp hơn

#### B5-MR11

**Đáp án: A.**

- A đúng: apply mặc định axis=0, nhận từng cột Series; mean k2 dùng 2,6,0, mẫu số 3.
- B sai: tính mean theo hàng như axis=1, không phải mặc định.
- C sai: hàm ở đây nhận cả cột và trả scalar, không phải giữ bảng từng ô.
- D sai: chia tổng k2 bằng 8 cho cả 4 hàng thay vì 3 giá biết.

**Đối chiếu:** nhóm 2; K52; mức Bổ sung. **Kiến thức và bẫy:** apply axis=0 nhận cột; tên/nhãn đầu ra là cột, khác axis=1. **Đọc lại:** NB ô 152–153: tự học apply theo cột, biến thể mean.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

#### B5-MR12

tb có khu A=20,B=60. Gán trực tiếp căn theo mã listing: listing B nhận60, listing A nhận20, C,D thiếu, nên [60,20,NaN,NaN]. Đó là khớp chuỗi nhãn tình cờ, không phải cùng đối tượng khu. Sửa `d['tb_khu']=d['khu'].map(tb)`, kết quả theo B,A,C,D=[20,60,20,60]. map tra giá trị cột khu rồi giữ nhãn listing; cũng tương đương transform mean. u có hai cột khu,gia (Series tb vẫn có tên gia); reset_index tạo kết quả mới, không tự chạy lại phép gán sai vào d.

**Hướng dẫn chấm:** 2 điểm: bốn giá sai/nguyên nhân 0,75; map và bốn giá đúng 0,75; cột u và không tự sửa d 0,5.

**Đối chiếu:** nhóm 3; K53, K54, K23; mức Bổ sung. **Kiến thức và bẫy:** map bằng Series thống kê nhóm đưa giá trị về từng hàng; khác gán trực tiếp Series nhóm; reset_index tạo bảng mới, đưa khóa nhóm thành cột và giữ khóa khi xuất index=False; transform trả từng hàng, giữ index sau lọc; hàng thiếu giá vẫn nhận thống kê nhóm. **Đọc lại:** NB ô 154–155 và 62–63: kết hợp map Series/reset_index.

**Kiểm chứng:** Đã chạy code kiểm chứng với pandas 3.0.1, NumPy 2.3.5; các assert liên quan đạt.

### Độ bao phủ sau đợt 6

Đã dùng 56/56 mục tiêu trong yêu cầu trả lời. Không còn mục tiêu thiếu trong phạm vi đã xác định.

## Cặp đối chiếu và bẫy

| Bẫy | Câu đánh giá |
| --- | --- |
| Cùng độ dài sai đối tượng; nhãn / vị trí | 001,011,018,021,050 |
| Hợp nhãn phép tính / hàng có sẵn khi gán | 006,030,041 |
| map giá trị / gán theo index; thiếu phí / miễn phí | 002,007,022,MR04,MR12 |
| NaN rơi vào else; xử lý biên | 012,026,038,047 |
| size / count / nunique; review / listing | 013,015,019,027 |
| Gộp mean sai trọng số; host / listing | 008,033,046,058 |
| Mask nhóm / hàng; khóa tính độ lệch | 019,023,029,049 |
| Left nhân hàng; validate không kiểm đủ khóa | 009,028,034,037,040,048,056,059 |
| NaN bên phải / không khớp | 044,056,059 |
| ignore_index không xóa mã trùng | 004,009,024 |
| qcut giữ thành viên / đổi mốc; đơn vị | 032,042,057 |
| assign không chống chia lặp; cột phụ thuộc cũ | 005,010,020,045,055,060 |
| Lọc trước transform đổi phạm vi | 020,039,053 |
| Một assert qua chưa chứng minh đúng toàn bộ | 048,056,059,060 |

Cặp đối chiếu: **001/011** (nhãn/vị trí); **003/023** (aggregate/transform); **007/022** (thiếu phí và công thức); **028/040** (cặp ghép và tổng bị tăng trọng số); **005/010** (trả bảng mới và cập nhật lặp). Nhãn cặp chỉ xuất hiện ở đáp án.

## Đối chiếu cuối bộ

- Đủ B5-001–B5-060: **60 câu trọng tâm = 40 TN + 20 TL**; nhóm chính **10/12/16/14/8**.
- Đủ B5-MR01–B5-MR12: **12 bổ sung = 8 TN + 4 TL**; tách riêng ở từng đợt.
- Trọng tâm có **15 nền tảng + 33 vận dụng + 12 phân loại**. Không coi đây là dự đoán chắc chắn đề thi thật.
- **56/56 mục tiêu** được dùng để trả lời ít nhất một câu. pivot_table ở trọng tâm; các phần tự học giữ nhãn ưu tiên theo nguồn. Các câu sửa lỗi ba ý (a)–(b)–(c) gồm 010,018,019,028,038,039,048,050,059,060.
- Đã rà câu trùng ý và phương án nhiễu; có cặp đối chiếu chủ đích để phân biệt đọc nhãn/vị trí, lọc trước/sau, cùng số hàng/đúng khóa. Không chỉ đổi số hoặc tên từ đề gốc: các tình huống thay tập quan sát, điều kiện, yêu cầu sửa và cách kiểm chứng.
- Độ bao phủ nguồn Bài 5 khác mức ưu tiên từ đề mẫu. Không bao phủ toàn bộ sách/website liên kết và không thêm SQL, API, regex, thời gian, pipe hay kỹ thuật pandas ngoài bài.

Đã chạy kiểm chứng **71/72 câu** bằng pandas 3.0.1; **1 câu** được kiểm bằng suy luận, chưa chạy vì chỉ hỏi cơ chế/thiết kế. Không đo tỷ lệ hiệu năng. Các kiểm tra gồm đảo thứ tự alignment, đối chiếu nhóm/tập giá, đếm cặp merge, chạy hai lần từ nguồn cố định và kiểm bảng gốc.

Phân bố đáp án trọng tâm: {'A': 10, 'B': 10, 'C': 10, 'D': 10}; bổ sung: {'A': 2, 'B': 2, 'C': 2, 'D': 2}.

## Dấu vết bao phủ thực tế

| Mục tiêu | Câu dùng để trả lời |
| --- | --- |
| K01 | B5-001, B5-018, B5-021 |
| K02 | B5-006, B5-030 |
| K03 | B5-011, B5-018, B5-021, B5-050, B5-MR09 |
| K04 | B5-MR02, B5-031 |
| K05 | B5-030, B5-041, B5-050, B5-051 |
| K06 | B5-051 |
| K07 | B5-011, B5-018, B5-050 |
| K08 | B5-002, B5-022 |
| K09 | B5-007, B5-022, B5-030 |
| K10 | B5-012, B5-026, B5-038 |
| K11 | B5-016, B5-052 |
| K12 | B5-047, B5-052 |
| K13 | B5-022, B5-047 |
| K14 | B5-026, B5-038, B5-057 |
| K15 | B5-032, B5-042 |
| K16 | B5-042, B5-057 |
| K17 | B5-010, B5-057 |
| K18 | B5-003, B5-013, B5-027, B5-036, B5-043, B5-058 |
| K19 | B5-008, B5-013, B5-015, B5-033 |
| K20 | B5-013, B5-027, B5-MR10 |
| K21 | B5-043 |
| K22 | B5-008, B5-033, B5-046 |
| K23 | B5-019, B5-MR04, B5-023, B5-029, B5-049, B5-MR12 |
| K24 | B5-019, B5-049 |
| K25 | B5-015, B5-019, B5-029 |
| K26 | B5-036, B5-049 |
| K27 | B5-020, B5-039, B5-053 |
| K28 | B5-039, B5-046 |
| K29 | B5-039, B5-053 |
| K30 | B5-058 |
| K31 | B5-027, B5-029, B5-058 |
| K32 | B5-004, B5-024 |
| K33 | B5-004, B5-009, B5-024 |
| K34 | B5-014, B5-059 |
| K35 | B5-017, B5-028, B5-034 |
| K36 | B5-009, B5-028, B5-034, B5-040 |
| K37 | B5-037, B5-040, B5-048, B5-054 |
| K38 | B5-028, B5-044, B5-056 |
| K39 | B5-048, B5-056, B5-059 |
| K40 | B5-009, B5-040, B5-054 |
| K41 | B5-048, B5-059 |
| K42 | B5-005, B5-010, B5-025, B5-055 |
| K43 | B5-010, B5-020, B5-060 |
| K44 | B5-025, B5-035, B5-045 |
| K45 | B5-035, B5-045 |
| K46 | B5-055 |
| K47 | B5-060 |
| K48 | B5-060 |
| K49 | B5-MR01, B5-MR09 |
| K50 | B5-MR02, B5-MR06 |
| K51 | B5-MR06 |
| K52 | B5-MR03, B5-MR11 |
| K53 | B5-MR04, B5-MR12 |
| K54 | B5-MR05, B5-MR10, B5-MR12 |
| K55 | B5-MR07 |
| K56 | B5-MR08 |
