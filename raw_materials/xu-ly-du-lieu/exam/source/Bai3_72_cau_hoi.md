# BÀI 3 — NUMPY, MẢNG VÀ TƯ DUY VECTOR HOÁ

Ngân hàng 72 câu: 60 trọng tâm + 12 tự học.

## Nguồn và phạm vi

Đã đọc toàn văn bản Markdown gồm ghi chú giảng viên; toàn bộ ô Markdown, code, bài tập, assert và output lưu sẵn của hai notebook sau:

- **BG**: [bai-03-numpy.md](<D:/LTXLDL_GK/Bài 3/bai-03-numpy.md>).
- **NB**: [lecture_03.ipynb](<D:/LTXLDL_GK/Bài 3/lecture_03.ipynb>). Số ô dẫn lại là chỉ số cell tính từ 0 trong tệp JSON.
- **LAB**: [lab_03.ipynb](<D:/LTXLDL_GK/Bài 3/lab_03.ipynb>). Đọc cả TODO chưa hoàn thành, lời trả lời đã điền và assert; không coi notebook lab hiện tại là đã chạy trọn vẹn.

Đã đọc đủ sáu đề PDF:

- **GK**: [Giữa kỳ luyện tập](<D:/LTXLDL_GK/Bài_kiểm_tra/2627I_UET.DSE2049 - Kiểm tra giữa kỳ (luyện tập) (1).pdf>), ưu tiên câu 5–7 (trang 2) và 21 (trang 4): chuẩn suy luận phổ biến, câu ngắn, nhiễu theo lỗi cơ chế, tự luận giải thích–sửa–diễn giải.
- **AI5**: [LTXLDL_AI_5.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_5.pdf>), **DS1**: [LTXLDL_DS_1.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_1.pdf>), **DS2**: [LTXLDL_DS_2.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_DS_2.pdf>): phong cách Nguyễn Tuấn Phong; dùng một số cơ chế tuần 3 cho câu phân loại.
- **AI1**: [LTXLDL_AI_1.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_1.pdf>), **AI2**: [LTXLDL_AI_2.pdf](<D:/LTXLDL_GK/Bài_kiểm_tra/LTXLDL_AI_2.pdf>): biến thể chỉ mục, bộ nhớ, reshape. Hai tệp này ghi người ra đề Đào Việt Anh; không gán nhầm tác giả.

Không thiếu tệp nguồn được yêu cầu. Phạm vi lấy từ ba nguồn Bài 3, không mở rộng toàn chương sách liên kết. Không tuyên bố đã đọc toàn bộ sách hay nội dung website/ảnh liên kết ngoài tệp; mô tả hình trong Markdown và nội dung notebook đủ để đối chiếu các cơ chế được hỏi. Những điều kiện phức hợp trong đề tuần 3 được dùng để kết hợp cơ chế đã học, không thêm API bộ nhớ lạ.

**Ranh giới ưu tiên:** NB ô 84 ghi “Đọc thêm: gán trực tiếp và lát cắt ngược”. Gán trực tiếp đã có trong bài giảng chính nên vẫn là trọng tâm; các bài stride âm đặt riêng ở MR09–MR10. Transpose 1D là hệ quả của cơ chế shape/transpose trong bài, có đưa vào theo yêu cầu. `ddof=1` được ghi trong BG là lựa chọn bổ sung “để notebook”, nhưng NB không có bài code riêng về nó: MR08 cung cấp toàn bộ công thức, không giả vờ đây là bài tập đã có sẵn trong notebook. Tự học với chương 4 là lựa chọn một ví dụ, không phải yêu cầu học hết chương.

## Quy ước làm bài

- Giả định NumPy 2.x, `import numpy as np` đã có trong mỗi câu. Tài liệu ghi NumPy 2.5.2; code của ngân hàng được thực thi với **NumPy 2.3.5, Python 3.12.14**. Không thay phiên bản môi trường. Các ca dùng ở đây đã được đối chiếu trên phiên bản thực tế này; không kiểm riêng trên 2.5.2.
- Mỗi câu khởi tạo dữ liệu độc lập; chạy đúng thứ tự. Chỉ số bắt đầu từ 0. Các mảng tạo bằng `np.array` số học trong câu lưu theo hàng; `reshape` đều ghi `order='C'`. Một mảng `(n,)` không tự được gọi là hàng hoặc cột.
- Strides và offset tính bằng byte. Offset được hỏi tính từ đầu dữ liệu của mảng được nêu, không phải địa chỉ tuyệt đối. Khoảng byte bao trùm gồm các khoảng bỏ qua giữa hai đầu và toàn bộ byte của ô cuối.
- `nbytes` đếm byte của các ô mảng nhìn thấy, chưa gồm metadata; không phải số byte mới cấp phát hay RAM cả tiến trình. “Không cấp phát dữ liệu mới” vẫn có thể tạo metadata view mới.
- Mảng có số thập phân dùng float64 trừ khi chỉ định khác. Khi báo số thực, chấp nhận dạng phân số đúng hoặc sai số tuyệt đối `1e-12`, trừ câu ghi mức khác. Không chấm khác biệt khoảng trắng hay dạng in scalar.
- Trắc nghiệm có đúng một đáp án. Tự luận nhận các biểu thức tương đương đúng về giá trị, shape và ý nghĩa; không trừ điểm vì có cách viết khác ngắn hơn.
- Mỗi TN có thể chấm 1 điểm; mỗi TL có thang riêng 2 hoặc 3 điểm trong file đáp án. Đây là ngân hàng luyện tập, không phải một đề thi 60 phút hay dự báo chắc chắn đề thật.

## Kế hoạch sáu đợt

Mỗi câu chỉ tính vào một nhóm chính, có tối đa hai mục tiêu phụ. Các mức độ là tham số thiết kế, không phải kết quả đo thực nghiệm. Bản hoàn chỉnh có 60 trọng tâm và 12 bổ sung, phân bổ như sau.

| Nhóm chính | Số câu trọng tâm | TN | TL | Nền tảng | Vận dụng | Phân loại |
| --- | --- | --- | --- | --- | --- | --- |
| Cấu trúc mảng, dtype, dung lượng, sai số | 8 | 8 | 0 | 5 | 3 | 0 |
| Vector hoá, ufunc, hiệu năng | 6 | 6 | 0 | 2 | 4 | 0 |
| Slicing, strides, transpose, reshape | 12 | 6 | 6 | 2 | 4 | 6 |
| Mask, advanced indexing, view/copy, phép gán | 12 | 6 | 6 | 0 | 9 | 3 |
| Broadcasting, axis, keepdims | 12 | 6 | 6 | 1 | 8 | 3 |
| Thống kê và lấy mẫu | 10 | 8 | 2 | 5 | 5 | 0 |

| Đợt | Trọng tâm | TN/TL | Nền tảng / Vận dụng / Phân loại | Bổ sung | TN/TL |
| --- | --- | --- | --- | --- | --- |
| 1 | B3-001–B3-010 | 7/3 | 3/5/2 | MR01–MR02 | 2/0 |
| 2 | B3-011–B3-020 | 7/3 | 3/5/2 | MR03–MR04 | 1/1 |
| 3 | B3-021–B3-030 | 7/3 | 3/5/2 | MR05–MR06 | 2/0 |
| 4 | B3-031–B3-040 | 7/3 | 2/6/2 | MR07–MR08 | 1/1 |
| 5 | B3-041–B3-050 | 6/4 | 2/6/2 | MR09–MR10 | 1/1 |
| 6 | B3-051–B3-060 | 6/4 | 2/6/2 | MR11–MR12 | 1/1 |

## Danh mục mục tiêu và mã câu dự kiến

Đã lập trước khi soạn câu; mã chỉ ghi phần sau `B3-`. Nội dung “đọc thêm” không có cùng ưu tiên thi với phần trọng tâm.

| Mục tiêu | Nội dung phải dùng để trả lời | Ưu tiên | Câu dự kiến | Nguồn đọc lại |
| --- | --- | --- | --- | --- |
| K01 | ndarray: shape, ndim, size, dtype, itemsize, nbytes | Trọng tâm | 001 | BG §1; NB ô 2–7; LAB bài 1 |
| K02 | Metadata, C-order; list CPython lưu tham chiếu; mảng số và dtype=object | Trọng tâm | 011 | BG §1, ghi chú cách lưu; NB ô 4–9 |
| K03 | Đổi shape giữ số ô; đổi dtype đổi itemsize, nbytes, strides; nbytes không gồm metadata | Trọng tâm | 006 | BG §1; LAB bài 1 |
| K04 | Giới hạn int8, khác int Python; astype trước/sau tràn | Trọng tâm | 016,031 | BG §1 bài tập 1; NB ô 10–17 |
| K05 | float32/64: bộ nhớ, gần đúng, chữ số in không tăng độ chính xác | Trọng tâm | 021,041 | BG §1; NB ô 12–13 |
| K06 | So sánh số thực với isclose/allclose và tolerance cho trước | Trọng tâm | 051 | NB ô 18–19; LAB bài 6,8 |
| K07 | Ufunc từng phần tử; x*2 tương đương multiply; vector hoá phép biến đổi | Trọng tâm | 002,012 | BG §2; NB ô 21–25,36–39 |
| K08 | Vòng lặp thư viện biên dịch sẵn, dtype chọn cách đọc/tính; for Python vẫn còn chi phí | Trọng tâm | 022 | BG §2; NB ô 23,26–29; LAB bài 7 |
| K09 | Truy cập liên tiếp và cache; không suy ra tốc độ từ một yếu tố | Trọng tâm | 032 | BG §2; NB ô 30 |
| K10 | SIMD khác nhiều luồng; ufunc và nhân ma trận qua BLAS; không cam kết mọi phép đều nhanh | Trọng tâm | 042 | BG §2; NB ô 31–32; LAB bài 7 |
| K11 | Benchmark tương đương kết quả, chuẩn bị ngoài đo, lặp đo và giới hạn kết luận | Trọng tâm | 052 | NB ô 33–35; LAB bài 7 |
| K12 | Chỉ mục hàng/cột, chỉ mục âm; chỉ mục nguyên bỏ chiều, slicing giữ chiều | Trọng tâm | 003,045 | BG §3; NB ô 42–43,95–96 |
| K13 | start:stop:step, stop loại trừ, shape và strides byte của view | Trọng tâm | 013 | BG §3; NB ô 47–57; LAB bài 2 |
| K14 | Offset từ đầu view khác đầu gốc; ánh xạ phép gán qua view | Trọng tâm | 008 | BG §3 bài tập 4; LAB bài 2 |
| K15 | Transpose đổi shape/strides; T[i,j] ánh xạ A[j,i] | Trọng tâm | 023 | BG §3; NB ô 58–59 |
| K16 | Reshape C-order giữ thứ tự đọc và số phần tử; khác transpose | Trọng tâm | 033 | BG §3; NB ô 60–61 |
| K17 | Reshape mảng không liên tục có thể view hoặc copy; kiểm shares_memory và ô bị sửa | Trọng tâm | 018,048 | BG §3; NB ô 58–61; DS1 câu 14; AI2 câu 2 |
| K18 | Transpose rồi reshape C-order có thể copy; view của copy không nối về gốc | Trọng tâm | 038 | NB ô 58–59; AI2 câu 14 |
| K19 | nbytes của view khác khoảng byte bao trùm và lượng dữ liệu mới cấp phát | Trọng tâm | 028 | BG §1,3; LAB bài 2; AI5 câu 11 |
| K20 | Điều kiện bước byte cố định để bố trí yêu cầu có thể là view | Trọng tâm | 058 | BG §3 strides; AI1 câu 14 |
| K21 | Shape (n,), (1,n), (n,1); transpose 1D không tạo cột | Trọng tâm | 043 | BG §4; NB ô 91–96; suy ra từ transpose |
| K22 | Reshape sai số phần tử gây ngoại lệ; khác cảnh báo và không tự cắt/đệm | Trọng tâm | 053 | BG §3 reshape |
| K23 | Mask bool cùng shape chọn ô theo hàng; mask 1D chọn hàng | Trọng tâm | 004,014 | BG §3; NB ô 66–67; LAB bài 4 |
| K24 | Điều kiện biên, &, \|, ngoặc; and/or đòi truth value đơn | Trọng tâm | 024 | BG §3; NB ô 72–73; DS2 câu 7 |
| K25 | Đọc A[mask] là copy; gán A[mask]=... sửa đích | Trọng tâm | 034 | BG §3; NB ô 68–71 |
| K26 | Hai mảng chỉ mục ghép từng cặp; ix_ chọn tích hàng × cột | Trọng tâm | 044 | BG §3; NB ô 74–79; LAB bài 4 |
| K27 | Chỉ mục đọc lặp/đổi thứ tự; số lần tham gia tổng | Trọng tâm | 054 | BG §3; NB ô 76–77; AI1 câu 1 |
| K28 | Chọn nâng cao trước rồi gán bước sau chỉ sửa bản sao tạm | Trọng tâm | 019 | BG §3 ghi chú ix_; DS2 câu 12 |
| K29 | View sau advanced indexing chỉ dùng chung với bản sao; ánh xạ ô | Trọng tâm | 009 | BG §3; DS1 câu 15 |
| K30 | ix_ chỉ tạo chỉ mục; đọc tạo copy, gán trực tiếp và broadcasting RHS | Trọng tâm | 029 | BG §3; NB ô 80–83; AI5 câu 3 |
| K31 | Mask đã tính không tự tính lại khi mảng số bị sửa | Trọng tâm | 039,059 | BG §3 cơ chế mask; AI2 câu 12 |
| K32 | B=A, copy, basic view, advanced copy; giá trị bằng nhau khác shares_memory | Trọng tâm | 049,059 | BG §3; LAB bài 3 |
| K33 | Broadcast từ phải sang trái; chiều thiếu như 1 không đổi shape gốc | Trọng tâm | 005,015 | BG §4; NB ô 93–94 |
| K34 | Hệ số riêng theo cột, theo hàng, kết hợp cả hai | Trọng tâm | 025,035 | BG §4 bài tập 5; LAB bài 5 |
| K35 | Thêm chiều bằng None/newaxis/reshape; A[:,0] khác A[:,0:1] | Trọng tâm | 045 | BG §4; NB ô 91–96 |
| K36 | Axis là chiều gộp; tập phần tử, mẫu số; shape sum/mean có/không keepdims | Trọng tâm | 020,055 | BG §5; NB ô 106–109 |
| K37 | Trừ trung bình chính hàng; ma trận chữ nhật báo lỗi, ma trận vuông che lỗi | Trọng tâm | 010,040 | BG §5 bài tập 6; LAB bài 6 |
| K38 | Chia cho tổng hàng/cột: shape, mẫu số và ý nghĩa khác nhau | Trọng tâm | 030,050 | BG §4–5; GK câu 21 |
| K39 | Kiểm chứng ý nghĩa bằng ô tính tay và bất biến; assert chỉ là kiểm một số yêu cầu | Trọng tâm | 060 | BG mục kiểm chứng AI; LAB ô 1, bài 6 |
| K40 | Mean, median, min/max, sum; giá cực lớn và mức giá điển hình | Trọng tâm | 007,017 | BG §5; LAB bài 8 |
| K41 | Var/std ddof=0, đơn vị; cùng mean khác phân tán | Trọng tâm | 026,036 | BG §5; NB ô 104–105 |
| K42 | Mean mask bool là tỷ lệ True với đúng tập đối tượng và mẫu số | Trọng tâm | 027 | LAB bài 8 |
| K43 | default_rng, choice, size; lấy mẫu chỉ mục giữ các cột cùng bản ghi | Trọng tâm | 037 | BG §5; NB ô 114–115; LAB bài 8 |
| K44 | replace=False không trùng vị trí nhưng giá trị có thể trùng; giới hạn size | Trọng tâm | 046 | BG §5; LAB bài 8 |
| K45 | Seed tái lập theo môi trường/thứ tự gọi; gọi tiếp khác khởi tạo lại; không bảo đảm đại diện/khác mẫu | Trọng tâm | 047,056 | BG §5; NB ô 114–117,128–129 |
| K46 | Thống kê toàn bộ dữ liệu hợp lệ khi có thể; mẫu để đọc kiểm tra, tránh chọn seed thuận ý | Trọng tâm | 057 | BG §5; LAB bài 8; AI2 câu 3 |
| K47 | .base có thể bỏ qua mảng trung gian; dùng shares_memory | Tự học/đọc thêm | MR01 | NB ô 64–65 |
| K48 | Một biểu thức có thể tạo nhiều mảng tạm và nhiều lượt đọc/ghi | Tự học/đọc thêm | MR02 | NB ô 40 |
| K49 | float32 với số lớn có thể làm mất phần tăng nhỏ | Tự học/đọc thêm | MR03 | NB ô 118 |
| K50 | broadcast_to: stride 0, chia sẻ, chỉ đọc; broadcasting không sao toán hạng nhưng phép cộng tạo kết quả | Tự học/đọc thêm | MR04,MR12 | NB ô 119–120 |
| K51 | Percentile 0–100, quantile 0–1; phương pháp linear và nội suy | Tự học/đọc thêm | MR05 | NB ô 125–127 |
| K52 | integers cận trên loại trừ; random thuộc [0,1) | Tự học/đọc thêm | MR06 | NB ô 128–131 |
| K53 | normal: tham số phân phối khác thống kê chính xác của mẫu nhỏ | Tự học/đọc thêm | MR07 | NB ô 130–131 |
| K54 | ddof=1 với công thức và quy ước được cung cấp | Tự học/đọc thêm | MR08 | BG §5 ghi chú để notebook; bổ sung theo yêu cầu |
| K55 | float32: dấu, số mũ bias 127, 23 bit phần trị và số chuẩn hoá | Tự học/đọc thêm | MR11 | NB ô 123–124: đọc thêm, không yêu cầu trên lớp |
| K56 | Bước cắt âm, thứ tự duyệt, stride âm, offset từ gốc không phải địa chỉ âm | Tự học/đọc thêm | MR09,MR10 | NB ô 84–85: đọc thêm; AI1 câu 2; AI2 câu 10,12 |

## Đợt 1

### A. Câu trọng tâm

#### B3-001

Cho đoạn code:
```python
A = np.array([[3, 6, 9], [2, 4, 8]], dtype=np.int32)
print(A.ndim, A.size, A.itemsize, A.nbytes)
```
Bốn giá trị được in lần lượt là gì?

A. `2, 6, 24, 4`

B. `2, 6, 4, 24`

C. `2, 2, 4, 8`

D. `6, 2, 4, 24`

#### B3-002

```python
x = np.array([2, -3, 5, 0], dtype=np.int32)
y = x * 2
```
Nhận định nào đúng về `y` và phép tính?

A. `y` lặp lại dãy x hai lần, shape `(8,)`.

B. `y` là một số bằng tổng x nhân 2.

C. `y=[4,-6,10,0]`, dtype int64 vì số 2 là int Python.

D. `y=[4,-6,10,0]`, dtype int32; tương đương `np.multiply(x,2)`.

#### B3-003

```python
A = np.array([[1, 4, 7], [2, 5, 8]], dtype=np.int64)
p = A[-1, :]
q = A[-1:, :]
```
Shape của p và q lần lượt là gì?

A. `(3,)` và `(1,3)`

B. `(1,3)` và `(1,3)`

C. `(3,)` và `(3,1)`

D. `(2,3)` và `(1,3)`

#### B3-004

```python
A = np.array([[2, 7, 4], [9, 6, 1]], dtype=np.int64)
m = A % 2 == 0
B = A[m]
```
Giá trị, shape và quan hệ bộ nhớ của B với A là gì?

A. `[[2,4],[6,1]]`, `(2,2)`, dùng chung.

B. `[2,6,4]`, `(3,)`, không dùng chung.

C. `[2,4,6]`, `(3,)`, không dùng chung.

D. `[2,4,6]`, `(3,)`, dùng chung.

#### B3-005

```python
A = np.zeros((2, 3), dtype=np.int32)
b = np.array([1, 4, 6], dtype=np.int32)
C = A + b
```
Sau phép cộng, cặp `(b.shape, C.shape)` là gì?

A. `((1,3),(2,3))`

B. `((3,),(2,3))`

C. `((3,),(3,2))`

D. Phép cộng báo ValueError vì số chiều khác nhau.

#### B3-006

```python
A = np.arange(8, dtype=np.int16).reshape(2, 4, order='C')
R = A.reshape(4, 2, order='C')
F = A.astype(np.float64)
```
Chọn cặp đúng gồm `(A.nbytes, R.nbytes, F.nbytes)` và `F.strides` tính bằng byte.

A. `(16,8,64)` và `(32,8)`

B. `(2,2,8)` và `(32,8)`

C. `(16,16,16)` và `(8,2)`

D. `(16,16,64)` và `(32,8)`

#### B3-007

Năm giá giả lập, cùng đơn vị USD/đêm, đều đã xác nhận hợp lệ:
```python
gia = np.array([20, 30, 40, 50, 260], dtype=np.float64)
```
Nhận định nào phù hợp nhất khi mô tả mức giá điển hình ít bị một giá rất cao kéo lệch?

A. Mean 80, median 40; có thể dùng median 40 và vẫn giữ giá 260 hợp lệ.

B. Mean 40, median 80; chọn mean vì ít nhạy với giá cực lớn.

C. Mean 80, median 40; bắt buộc xoá 260 vì nó lớn nhất.

D. Mean 80, median 260; median là số cuối theo thứ tự thu thập.

#### B3-008

A được tạo liên tục theo hàng (C-order):
```python
A = np.arange(16, dtype=np.int32).reshape(4, 4, order='C')
V = A[1::2, 1::2]
V[1, 0] = 90
```
Nêu shape, strides của V; offset ô đầu V tính từ byte đầu dữ liệu A. Ô nào của A bị sửa? Tính offset của ô đó từ đầu A và giải thích vì sao chỉ dùng `1*V.strides[0]` là thiếu.

#### B3-009

```python
A = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]], dtype=np.int32)
C = A[[2, 0], 1:]
W = C.T
W[1, 0] = 77
```
Ô nào của C bị sửa, C và A sau cùng là gì? Trong ba cặp `(A,C)`, `(C,W)`, `(A,W)`, cặp nào dùng chung dữ liệu? Giải thích ngắn.

#### B3-010

Mỗi hàng là giá một chỗ ở qua ba kỳ, đơn vị USD/đêm (giả lập). Cần trừ trung bình của chính hàng:
```python
P = np.array([[12., 18., 24.], [30., 36., 42.]])
tb = P.mean(axis=1)
lech = P - tb
```
(a) Vì sao dòng cuối lỗi? (b) Viết một biểu thức sửa đúng, không dùng for. (c) Nêu shape, kết quả và một cách kiểm chứng đúng ý nghĩa.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR01

```python
goc = np.arange(8, dtype=np.int32)
a = goc.reshape(2, 4, order='C')
b = a[:, 1:]
```
Trên môi trường của bài, `b.base is a` là False. Kết luận nào đúng?

A. b chắc chắn không dùng chung dữ liệu với a.

B. b có giá trị bằng một phần a nên chắc chắn là bản sao.

C. `.base` có thể trỏ qua a tới goc; `np.shares_memory(a,b)` là True.

D. Vì a là view nên mọi slicing trên a buộc phải sao chép.

#### B3-MR02

Với ndarray thông thường, không dùng tối ưu gộp biểu thức ngoài NumPy:
```python
A = np.array([2., 4., 6., 8.])
R = A * 3 + 5
```
Mô tả nào đúng ở mức các phép toán mảng?

A. Phép nhân tạo kết quả tạm; phép cộng đọc kết quả tạm và tạo R.

B. Vì viết một dòng nên chỉ có một lượt đọc A và không có kết quả tạm.

C. NumPy tự biến biểu thức thành một vòng for Python.

D. Phép cộng 5 sửa trực tiếp A nên không cần R mới.

### Cập nhật độ bao phủ sau đợt 1

Đã dùng 16/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K02, K04, K05, K06, K08, K09, K10, K11, K15, K16, K17, K18, K19, K20, K21, K22, K24, K25, K26, K27, K28, K30, K31, K34, K35, K38, K41, K42, K43, K44, K45, K46, K49, K50, K51, K52, K53, K54, K55, K56. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 2

### A. Câu trọng tâm

#### B3-011

Xét list CPython, ndarray dtype số và ndarray dtype=object. Nhận định nào mô tả đúng cách lưu?

A. Mảng số hai chiều là một list chứa các list; shape chỉ đếm các list con.

B. List lưu trực tiếp mọi giá trị số trong ô kích thước bằng nhau như int32.

C. List lưu tham chiếu; ndarray dtype số lưu giá trị cùng kiểu; dtype=object lưu tham chiếu. Shape/dtype là metadata, không phải các giá trị trong vùng dữ liệu.

D. Một mảng số C-order lưu hết cột 0 trước rồi mới tới cột 1; metadata được tính vào nbytes.

#### B3-012

Hai mảng cùng vị trí mô tả cùng một cảm biến:
```python
x = np.array([3, 5, 8, 10], dtype=np.int32)
y = np.array([5, 4, 8, 13], dtype=np.int32)
```
Biểu thức nào trả về bình phương chênh lệch từng cặp, shape `(4,)`, mà không dùng vòng lặp Python?

A. `(y-x)**2`

B. `(y-x).sum()**2`

C. `[int(v-u)**2 for u,v in zip(x,y)]`

D. `y**2-x**2`

#### B3-013

```python
A = np.arange(16, dtype=np.int32).reshape(4, 4, order='C')
V = A[1:4:2, :3:2]
```
Shape và strides của V lần lượt là gì? A ban đầu liên tục theo hàng.

A. `(2,2)` và `(16,8)`

B. `(2,3)` và `(32,8)`

C. `(2,2)` và `(8,2)`

D. `(2,2)` và `(32,8)`

#### B3-014

```python
A = np.array([[2, 9], [7, 1], [8, 6]], dtype=np.int32)
r = A[A[:, 0] >= 7]
s = A[A >= 7]
```
Shape của r và s lần lượt là gì?

A. `(3,)` và `(2,2)`

B. `(2,2)` và `(3,)`

C. `(2,)` và `(3,2)`

D. `(2,2)` và `(2,2)`

#### B3-015

```python
A = np.array([[2, 4, 6], [3, 5, 7]], dtype=np.int32)
d = np.array([10, 20], dtype=np.int32)
```
Cần cộng số 10 vào hàng 0 và số 20 vào hàng 1. Nhận định nào đúng?

A. `A+d` đúng vì len(d) bằng số hàng.

B. `A+d.reshape(1,2,order="C")` đúng vì có đủ hai chiều.

C. `A+d` lỗi do 3 khác 2 ở chiều cuối; `A+d[:,None]` thực hiện đúng yêu cầu.

D. `A.T+d` cho ngay kết quả đúng shape `(2,3)` nên không cần đổi lại.

#### B3-016

```python
x = np.array([70, 100], dtype=np.int8)
a = (x * 2).astype(np.int16)
b = x.astype(np.int16) * 2
```
Cặp giá trị `(a,b)` là gì?

A. `([-116,-56], [140,200])`

B. `([140,200], [140,200])`

C. `([-116,-56], [-116,-56])`

D. `([140,200], [-116,-56])`

#### B3-017

```python
x = np.array([8, 2, 10, 4], dtype=np.int32)
print(x.sum(), x.min(), x.max(), x.mean(), np.median(x))
```
Các giá trị được in lần lượt là gì?

A. `24,2,10,6,5`

B. `24,2,10,6,10`

C. `24,2,10,24,6`

D. `24,2,10,6,6`

#### B3-018

A liên tục theo hàng:
```python
A = np.arange(12, dtype=np.int32).reshape(3, 4, order='C')
P = A[:, ::2].reshape(6, order='C')
Q = A[:, 1:3].reshape(6, order='C')
```
Cho giá trị P, Q và cặp `(np.shares_memory(A,P), np.shares_memory(A,Q))`. Giải thích bằng khoảng cách byte giữa các ô liên tiếp khi đọc phẳng. Có thể kết luận “không C-contiguous thì reshape luôn copy” không?

#### B3-019

Cần đặt hai ô A[0,1] và A[2,1] thành 0, giữ các ô khác:
```python
A = np.array([[2, 4, 6], [8, 10, 12], [14, 16, 18]], dtype=np.int32)
T = A.T
T[[1], :][:, [0, 2]] = 0
```
(a) A có thay đổi không, vì sao? (b) Thay dòng cuối bằng một phép gán qua T đúng yêu cầu. (c) Nêu các ô thực sự đổi và một cách kiểm chứng.

#### B3-020

Mỗi hàng là một cửa hàng, mỗi cột là một ngày:
```python
D = np.array([[2., 4., 6.], [8., 10., 12.]])
u = D.mean(axis=0)
v = D.sum(axis=1, keepdims=True)
t = D.mean()
```
Nêu giá trị và shape của u, v, t. Những ô nào tham gia u[1], mẫu số của nó là bao nhiêu? Diễn giải u và v theo bảng.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR03

```python
a = np.float32(100_000_000)
b = a + np.float32(1)
c = np.float64(100_000_000) + np.float64(1)
```
Nhận định nào đúng?

A. b tăng chính xác 1 vì số 1 là nhỏ và dễ lưu.

B. b có cùng giá trị a; c bằng 100000001; phần tăng nhỏ có thể mất trong float32 ở độ lớn này.

C. In b với .12f làm b tăng thành 100000001.

D. b không đổi chứng minh phép cộng đã không được thực hiện.

#### B3-MR04

```python
b = np.array([2, 5, 8], dtype=np.int32)
V = np.broadcast_to(b, (4, 3))
```
Cho strides, nbytes của V, quan hệ bộ nhớ V với b và offset V[3,1] tính từ byte đầu b. V có cấp phát 48 byte dữ liệu mới không? Lệnh `V[0,0]=9` thành công, chỉ cảnh báo hay gây ngoại lệ?

### Cập nhật độ bao phủ sau đợt 2

Đã dùng 27/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K08, K09, K10, K11, K16, K18, K20, K21, K22, K24, K25, K26, K27, K31, K35, K38, K41, K42, K43, K44, K45, K46, K51, K52, K53, K54, K55, K56. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 3

### A. Câu trọng tâm

#### B3-021

Một số gần đúng đã được tính và lưu trong float32. Người viết chỉ đổi định dạng từ `.6f` sang `.12f`, không tính lại. Nhận định nào đúng?

A. Dtype tự đổi thành float64 vì cần 12 chữ số.

B. Số byte và giá trị được lưu không đổi; số chữ số hiển thị tăng, không làm số gần đúng chính xác hơn.

C. Giá trị float32 trở thành giá trị thực chính xác vì in thêm chữ số.

D. float64 luôn biểu diễn chính xác mọi số thực nên chuyển kiểu sau đó sẽ khôi phục giá trị thật.

#### B3-022

Nhóm đổi `ds` là list các số sang `x=np.array(ds,dtype=np.int64)` nhưng vẫn tính `[v*2 for v in x]`. Một bạn nói: “Giờ vòng for đã được NumPy biên dịch nên chắc chắn có tốc độ như x*2”. Giải thích nào đúng?

A. Đúng vì đổi vùng chứa tự động biên dịch toàn bộ code Python phía sau.

B. Đúng vì int64 và float64 đều 8 byte nên dùng cùng cách diễn giải số và mã tính.

C. Sai: for vẫn chạy trong Python; x*2 gọi vòng lặp thư viện biên dịch sẵn, chọn cách đọc/tính theo dtype.

D. Sai chỉ vì NumPy không thể nhân số nguyên, phải đổi sang float64.

#### B3-023

```python
A = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
T = A.T
```
A liên tục theo hàng. Shape, strides của T và giá trị T[2,1] là gì?

A. `(3,2)`, `(4,12)`, `6`

B. `(3,2)`, `(8,4)`, `6`

C. `(2,3)`, `(12,4)`, `6`

D. `(3,2)`, `(4,12)`, `5`

#### B3-024

```python
dem = np.array([0, 1, 7, 8, 30], dtype=np.int32)
```
Cần giữ số đêm lớn hơn 0 và không quá 8. Cách nào đúng?

A. `dem[(dem>0) and (dem<=8)]`

B. `dem[(dem>=0) & (dem<8)]`

C. `dem[(dem>0) | (dem<=8)]`

D. `dem[(dem>0) & (dem<=8)]`

#### B3-025

```python
A = np.array([[3, 6, 9], [4, 8, 12]], dtype=np.int32)
c = np.array([10, 20, 30], dtype=np.int32)
R = A + c
```
R bằng gì?

A. `[[13,16,19],[24,28,32]]`

B. `[[13,26,39],[14,28,42]]`

C. `[[30,120,270],[40,160,360]]`

D. Báo lỗi vì A có 2 hàng còn c có 3 phần tử.

#### B3-026

Bốn giá giả lập USD/đêm:
```python
x = np.array([10., 10., 30., 30.])
```
`np.var(x)` và `np.std(x)` mặc định biểu diễn gì?

A. `100 USD²` và `10 USD`, vì ddof=0 chia tổng bình phương độ lệch cho 4.

B. `10 USD` và `100 USD²`, vì var và std cùng cách tính.

C. `400 USD²` và `20 USD`, vì không cần chia số quan sát.

D. `400/3 USD²` và `sqrt(400/3) USD`, vì NumPy mặc định ddof=1.

#### B3-027

Sáu giá giả lập đều hợp lệ, USD/đêm:
```python
gia = np.array([0., 20., 20., 40., 60., 100.])
ty_le = (gia <= 40).mean()
```
ty_le có giá trị và ý nghĩa nào?

A. `3/6`: tỷ lệ trong sáu chỗ ở có giá không quá 40.

B. `4/4`: tỷ lệ trong chính các giá được chọn, nên luôn bằng 1.

C. `4/6`: tỷ lệ trong sáu chỗ ở có giá không quá 40, gồm cả giá 0 hợp lệ.

D. `80/6`: tổng các giá được chọn chia tổng số chỗ ở.

#### B3-028

A liên tục theo hàng, V không rỗng:
```python
A = np.arange(12, dtype=np.int32).reshape(3, 4, order='C')
V = A[::2, 1::2].T
```
Tính (i) V.shape, V.strides và V.nbytes; (ii) đoạn byte liên tục ngắn nhất chứa trọn các ô V tính cả khoảng bỏ qua và toàn ô cuối, nêu hai offset đầu/cuối từ đầu A; (iii) V cấp phát bao nhiêu byte dữ liệu phần tử mới?

#### B3-029

```python
A = np.arange(12, dtype=np.int32).reshape(3, 4, order='C')
idx = np.ix_([2, 0], [1, 3])
B = A[idx]
B[:] = -1
A[idx] = np.array([50, 60], dtype=np.int32)
```
Nêu shape các mảng chỉ mục trong idx, B sau cùng, A sau cùng. Vì sao sửa B và gán trực tiếp A[idx] có tác động khác? Vế phải được ghép theo hàng hay cột của vùng chọn? Nếu riêng dòng cuối thay RHS bằng `[50,60,70]`, phép gán có hợp lệ không?

#### B3-030

Mỗi hàng là một kho, mỗi cột là một tuần; cần tỷ trọng từng tuần trong tổng của chính kho đó:
```python
D = np.array([[2., 6.], [3., 9.]])
P = D / D.sum(axis=1)
```
(a) Code có lỗi chạy không? Nêu P hiện tại và nó chia mỗi cột cho số nào. (b) Sửa một dòng NumPy. (c) Nêu kết quả đúng, ý nghĩa và cách kiểm chứng theo hàng.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR05

```python
x = np.array([0., 10., 20., 30.])
p = np.percentile(x, 25, method='linear')
q = np.quantile(x, 0.25, method='linear')
```
Với phương pháp linear, vị trí là `(n-1)*t`, nội suy tuyến tính giữa hai vị trí kề nhau (t là tỷ lệ 0–1). Cặp `(p,q)` bằng gì?

A. `(10,10)`, vì phân vị phải là một ô có sẵn.

B. `(0.075,7.5)`, vì percentile cũng nhận tỷ lệ 0–1.

C. `(7.5,0.075)`, vì quantile nhận phần trăm.

D. `(7.5,7.5)`, phân vị có thể nằm giữa hai giá trị dữ liệu.

#### B3-MR06

```python
rng = np.random.default_rng(19)
a = rng.integers(2, 5, size=4)
b = rng.random(size=4)
```
Không cần nhớ mẫu sinh được. Nhận định nào đúng về miền giá trị?

A. Mỗi a[i] thuộc {2,3,4}; mỗi b[i] thoả 0<=b[i]<1.

B. a có thể chứa 5; b có thể bằng đúng 1.

C. Mỗi a[i] thuộc {3,4,5}; b luôn lớn hơn 0 và không quá 1.

D. Seed 19 khiến mọi giá trị a và b nhỏ hơn 19 và không lặp.

### Cập nhật độ bao phủ sau đợt 3

Đã dùng 35/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K09, K10, K11, K16, K18, K20, K21, K22, K25, K27, K31, K35, K43, K44, K45, K46, K53, K54, K55, K56. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 4

### A. Câu trọng tâm

#### B3-031

```python
x = np.array([126, 127], dtype=np.int8)
a = x + 1
b = (x + 1).astype(np.int16)
c = np.array([int(v) + 1 for v in x], dtype=np.int16)
```
So sánh nào đúng?

A. a, b, c đều `[127,128]`; NumPy tự tăng số byte như int Python.

B. a tràn nhưng b và c đều `[127,128]`, vì cứ đổi sang int16 là khôi phục được.

C. a và b đều `[127,-128]`; c cũng vậy vì int(v) giữ int8.

D. a và b có giá trị `[127,-128]`; c là `[127,128]` vì đã đổi từng scalar sang int Python trước phép cộng.

#### B3-032

Khi duyệt liên tiếp một mảng số theo cách bố trí trong bộ nhớ, vì sao cache thường có lợi?

A. Cache nén mảng để loại bớt các phép nhân cần thực hiện.

B. Một khối được nạp có thể chứa các số sắp đọc; nếu còn trong cache, truy cập tiếp giảm chờ RAM.

C. Cache chỉ tồn tại khi chạy nhiều lõi, một luồng không hưởng lợi.

D. Các tham chiếu trong list CPython luôn rải rác nên bảng tham chiếu của list không thể được cache.

#### B3-033

```python
A = np.array([[2, 5, 8], [3, 6, 9]], dtype=np.int32)
R = A.reshape(3, 2, order='C')
T = A.T
```
Hàng thứ hai (chỉ mục 1) của R và T lần lượt là gì?

A. `[5,6]` và `[8,3]`

B. `[8,3]` và `[8,3]`

C. `[8,3]` và `[5,6]`

D. `[3,8]` và `[6,5]`

#### B3-034

```python
x = np.array([3, 8, 5, 10], dtype=np.int32)
m = x >= 8
y = x[m]
y[:] = 0
x[m] = 1
print(x.sum(), y.sum())
```
Hai tổng được in ra là gì?

A. `10,0`

B. `26,0`

C. `10,2`

D. `8,0`

#### B3-035

```python
A = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
r = np.array([10, 20], dtype=np.int32)
c = np.array([2, 4, 6], dtype=np.int32)
B = A + r[:, None] + c
```
Giá trị B[1,2] và shape của B là gì?

A. `28` và `(2,3)`

B. `12` và `(2,3)`

C. `32` và `(2,1)`

D. `32` và `(2,3)`

#### B3-036

Hai nhóm giá giả lập USD/đêm:
```python
X = np.array([40., 40., 40., 40.])
Y = np.array([20., 20., 60., 60.])
```
Nhận định nào đúng khi dùng std mặc định của NumPy?

A. Cùng mean 40 nên std cũng bằng nhau.

B. Mean đều 40; std của X là 0 và Y là 20; chỉ báo mean sẽ bỏ mất khác biệt phân tán.

C. Std của Y là 400 USD vì bình phương độ lệch là 400.

D. Y có std 20 chứng minh hai nhóm có cùng phân phối.

#### B3-037

Mỗi hàng là một bản ghi `[mã, giá]`, dữ liệu giả lập:
```python
A = np.array([[101, 40], [102, 70], [103, 40], [104, 90]], dtype=np.int32)
rng = np.random.default_rng(25)
idx = rng.choice(len(A), size=2, replace=False)
```
Không yêu cầu nhớ output rng. Nếu lần chạy này idx là `[2,0]`, cách nào lấy đúng hai bản ghi theo thứ tự đó và giữ mã đi cùng giá?

A. `A[[0,2], :]`

B. `A[idx, idx]`

C. `A[idx, :]`

D. `A[:, idx]`

#### B3-038

A ban đầu C-order:
```python
A = np.array([[1, 4, 7], [2, 5, 8]], dtype=np.int32)
T = A.T
R = T.reshape(2, 3, order='C')
W = R[:, 1:]
W[0, 0] = 99
```
Nêu R và A sau cùng. W[0,0] sửa ô nào của R? Nêu quan hệ dùng chung của `(A,T)`, `(A,R)`, `(R,W)`, `(A,W)` và giải thích bước làm tách dữ liệu.

#### B3-039

```python
x = np.array([4, 9, 6, 12], dtype=np.int32)
v = x[1:]
m = v >= 9
v[:] = [1, 20, 2]
v[m] = v[m] + 5
```
Nêu m, v và x sau cùng. Những ô nào thực sự được cộng 5? Vì sao giá trị 20 có/không được cộng? Phân biệt bản sao ở vế phải với mảng bị gán ở vế trái.

#### B3-040

Cần trừ trung bình của chính hàng; ma trận giá giả lập USD/đêm:
```python
P = np.array([[2., 4.], [10., 14.]])
tb = P.mean(axis=1)
lech = P - tb
```
(a) Vì sao code vẫn chạy, lech hiện tại là gì? (b) Sửa một biểu thức. (c) Nêu kết quả đúng và kiểm chứng theo hàng.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR07

```python
rng = np.random.default_rng(9)
x = rng.normal(loc=50, scale=5, size=4)
```
Nhận định nào đúng, không cần biết bốn số cụ thể?

A. `x.mean()` bắt buộc bằng 50 và `x.std()` bắt buộc bằng 5.

B. Mọi x[i] bắt buộc nằm trong [45,55].

C. 50 và 5 là trung bình/độ lệch chuẩn của phân phối sinh mẫu; một mẫu bốn số không buộc có đúng hai thống kê đó.

D. Vì size=4, mỗi giá trị 45,50,55 xuất hiện đúng số lần để giữ mean 50.

#### B3-MR08

Quy ước trong câu: với n>1, `var(ddof=d)=sum((x-mean(x))**2)/(n-d)` và std là căn bậc hai của var. ddof=0 mô tả dãy đã cho; ddof=1 thường dùng khi ước lượng phương sai tổng thể từ mẫu theo giả định phù hợp.
```python
x = np.array([2., 4., 6.])  # đơn vị USD
```
Tính var/std với ddof=0 và ddof=1, ghi đơn vị; vì sao không thể nói hai lời gọi NumPy tính mâu thuẫn? Chấp nhận căn hoặc làm tròn 6 chữ số sau dấu chấm.

### Cập nhật độ bao phủ sau đợt 4

Đã dùng 44/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K10, K11, K20, K21, K22, K27, K35, K45, K46, K55, K56. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 5

### A. Câu trọng tâm

#### B3-041

Cần lưu 6 số gần đúng, so sánh hai lựa chọn float32 và float64. Phát biểu nào đúng?

A. Phần dữ liệu lần lượt 24 và 48 byte; float64 thường lưu gần đúng chính xác hơn nhưng không biểu diễn chính xác mọi số thực.

B. Cả hai đều 48 byte vì số chữ số in ra được đặt giống nhau.

C. float32 dùng 24 byte và luôn đúng 7 chữ số sau dấu chấm bất kể độ lớn.

D. float64 dùng 48 byte và luôn lưu chính xác 1/3.

#### B3-042

Một lần quan sát thấy `x*2` trên mảng số lớn dùng một lõi; `A@B` trên ma trận float64 lớn dùng nhiều lõi. Cả hai nhanh hơn vòng Python tương ứng. Giải thích nào đúng?

A. SIMD nghĩa là phân chia mảng cho nhiều lõi nên x*2 không thể dùng SIMD.

B. Tất cả phép NumPy phải dùng nhiều luồng; quan sát một lõi luôn là lỗi đo.

C. A@B và x*2 luôn dùng cùng một thư viện BLAS và cùng số luồng.

D. Ufunc có thể chạy một luồng với mã biên dịch sẵn và có thể dùng SIMD; nhân ma trận có thể dùng BLAS nhiều luồng tuỳ cấu hình.

#### B3-043

```python
x = np.array([2, 4, 6, 8], dtype=np.int32)
a = x.T
b = x.reshape(1, 4, order='C')
c = x[:, None]
```
Shape của a, b, c lần lượt là gì?

A. `(4,1)`, `(1,4)`, `(4,1)`

B. `(4,)`, `(1,4)`, `(4,1)`

C. `(1,4)`, `(4,1)`, `(4,)`

D. `(4,)`, `(4,)`, `(4,)`

#### B3-044

```python
A = np.array([[1, 3, 5], [7, 9, 11], [13, 15, 17]], dtype=np.int32)
p = A[[0, 2], [1, 2]]
q = A[np.ix_([0, 2], [1, 2])]
```
Bộ ba `(p.shape, q.shape, q[1,0])` là gì?

A. `((2,),(2,),15)`

B. `((2,),(2,2),17)`

C. `((2,),(2,2),15)`

D. `((2,2),(2,2),15)`

#### B3-045

```python
A = np.array([[2, 4, 6], [10, 20, 30]], dtype=np.int32)
```
Cần cộng giá trị đầu của chính hàng vào mọi phần tử hàng đó, giữ shape `(2,3)`. Biểu thức nào đúng?

A. `A + A[:,0:1]`

B. `A + A[:,0]`

C. `A + A[0,:]`

D. `A + A[:,0].reshape(1,2,order="C")`

#### B3-046

```python
gia = np.array([40, 40, 70, 90], dtype=np.int32)
rng = np.random.default_rng(6)
idx = rng.choice(gia.size, size=3, replace=False)
```
Nhận định nào đúng, không cần nhớ idx cụ thể?

A. Mẫu chắc chắn có ba giá trị số khác nhau vì replace=False.

B. Có thể chọn lại cùng một vị trí nhiều lần nhưng không được trùng giá trị.

C. Có thể tăng size lên 5 mà vẫn replace=False vì có thể đọc lại các vị trí.

D. Ba vị trí không trùng; các giá trị được lấy vẫn có thể trùng, chẳng hạn 40 ở hai vị trí khác nhau.

#### B3-047

```python
rng = np.random.default_rng(28)
a = rng.choice(8, size=3, replace=False)
b = rng.choice(8, size=3, replace=False)
rng2 = np.random.default_rng(28)
c = rng2.choice(8, size=3, replace=False)
```
Không tính các chỉ mục cụ thể. Trong cùng môi trường và thứ tự gọi, c tái lập a hay b? Hai lời gọi trên cùng rng có phải khởi tạo lại không? Có bắt buộc b khác a, hoặc mẫu có mean bằng toàn bộ dữ liệu không?

#### B3-048

A liên tục C-order:
```python
A = np.arange(12, dtype=np.int32).reshape(3, 4, order='C')
V = A[:, ::2]
R = V.reshape(2, 3, order='C')
S = A[:, 1:3].reshape(2, 3, order='C')
R[1, 1] = 50
S[0, 0] = 90
```
Nêu hàng cuối A sau cùng; giá trị R[1,1] ban đầu ánh xạ ô nào của A? R, S dùng chung với A như thế nào? Giải thích vì sao hai reshape có kết quả bộ nhớ khác nhau.

#### B3-049

```python
A = np.array([2, 4, 6, 8], dtype=np.int32)
B = A
C = A.copy()
V = C[1:3]
B[0] = 20
V[0] = 40
```
Cho A, C sau cùng và giải thích ba quan hệ `(A,B)`, `(A,C)`, `(C,V)`. Ngay sau dòng tạo C, A và C có cùng giá trị không; điều đó có đủ chứng minh dùng chung không?

#### B3-050

Hàng là cửa hàng, cột là tuần. Cần thị phần của từng cửa hàng trong tổng lượt toàn hệ thống ở chính tuần đó:
```python
D = np.array([[2., 6.], [6., 6.]])
P = D / D.sum(axis=1, keepdims=True)
assert np.isclose(P.sum(), 2, rtol=0, atol=1e-12)
```
(a) Code và assert có chạy qua không; P đang có ý nghĩa gì? (b) Sửa một dòng tính P. (c) Cho kết quả đúng và một kiểm tra phù hợp hơn với mục tiêu; vì sao chỉ kiểm tổng toàn mảng bằng 2 chưa đủ?

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR09

```python
x = np.array([2, 4, 6, 8, 10, 12], dtype=np.int32)
```
Cần đọc các vị trí gốc 5,3,1 theo đúng thứ tự và sửa kết quả phải sửa các ô tương ứng của x. Biểu thức nào đáp ứng cả hai yêu cầu?

A. `x[[5,3,1]]`

B. `x[5:1:-2]`

C. `x[5:-1:-2]`

D. `x[5:0:-2]`

#### B3-MR10

A ban đầu C-order:
```python
A = np.arange(12, dtype=np.int32).reshape(3, 4, order='C')
V = A[1:, ::-2].T
W = V[::-1, :]
W[0, 1] = 99
```
Tính shape/strides W, offset ô đầu W từ đầu A; chỉ ra ô A bị sửa và offset của ô đó từ đầu A. Tại sao stride âm không có nghĩa địa chỉ vật lý âm?

### Cập nhật độ bao phủ sau đợt 5

Đã dùng 49/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K11, K20, K22, K27, K46, K55. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 6

### A. Câu trọng tâm

#### B3-051

```python
x = np.array([1.0, 1.0], dtype=np.float64)
y = np.array([1.0 + 1e-9, 1.0 + 1e-7], dtype=np.float64)
m = np.isclose(x, y, rtol=0, atol=1e-8)
t = np.allclose(x, y, rtol=0, atol=1e-8)
```
m và t lần lượt là gì? Sai số ở đây được chấp nhận khi chênh lệch tuyệt đối không quá 1e-8.

A. `[True,True]` và True

B. `[True,False]` và False

C. `[False,False]` và False

D. `[True,False]` và True

#### B3-052

Nhóm muốn so vòng for Python với phép toán mảng cho cùng phép nhân 2. Phương án đo nào hỗ trợ kết luận đáng tin cậy nhất?

A. Chuẩn bị hai đầu vào tương đương ngoài phần đo, kiểm kết quả bằng nhau, đo lặp ở vài kích thước; báo môi trường và giới hạn kết luận.

B. Đo một lần cho NumPy gồm cả tạo mảng, còn for dùng list có sẵn; không cần kiểm kết quả vì nhanh là đủ.

C. Đổi sang ndarray nhưng vẫn for rồi kết luận mọi phép NumPy dùng nhiều lõi nếu thời gian giảm.

D. Dùng tỷ lệ nhanh hơn của máy giảng viên làm kết quả cho máy mình; không cần chạy lại vì dtype giống nhau.

#### B3-053

```python
x = np.arange(6, dtype=np.int32)
R = x.reshape(2, 4, order='C')
print(x.sum())
```
Điều gì xảy ra nếu không bắt ngoại lệ?

A. R tự thêm hai số 0, rồi in 15.

B. R chỉ cần metadata mới nên reshape luôn thành công, rồi in 15.

C. reshape gây ValueError vì cần 8 ô nhưng x chỉ có 6; dòng print không được thực hiện.

D. reshape chỉ phát cảnh báo và trả view shape (2,4), rồi in 15.

#### B3-054

```python
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], dtype=np.int32)
p = A[[2, 0, 2], [1, 2, 1]]
```
Giá trị và shape của p là gì?

A. `[8,3]`, `(2,)`

B. `[[8,9,8],[2,3,2],[8,9,8]]`, `(3,3)`

C. `[3,8,8]`, `(3,)`

D. `[8,3,8]`, `(3,)`

#### B3-055

```python
A = np.array([[1, 3, 5], [2, 4, 6]], dtype=np.int32)
s = A.sum(axis=0, keepdims=True)
```
Giá trị và shape của s là gì?

A. `[3,7,11]`, `(3,)`

B. `[[3,7,11]]`, `(1,3)`

C. `[[9],[12]]`, `(2,1)`

D. `21`, `()`

#### B3-056

Hai nhóm cùng lấy mẫu hai dòng không hoàn lại từ bảng hợp lệ. Nhóm thứ nhất khởi tạo lại cùng seed trước mỗi lần chạy; nhóm thứ hai đổi seed. Nhận định nào đúng?

A. Cùng seed buộc mean mẫu bằng mean bảng, bất kể dữ liệu.

B. Seed quyết định không trùng vị trí; replace=False chỉ giúp kết quả chạy lại giống nhau.

C. Cùng seed, môi trường và thứ tự gọi hỗ trợ tái lập; hai seed khác nhau vẫn có thể tình cờ lấy cùng mẫu hữu hạn.

D. Đổi seed luôn tạo hai mẫu khác nhau và ít nhất một mẫu chắc chắn đại diện.

#### B3-057

Bốn giá USD/đêm giả lập đều đã xác nhận hợp lệ. Máy có thể tính trên cả bốn giá:
```python
gia = np.array([10., 20., 30., 140.])
idx = np.array([0, 1], dtype=np.int64)  # chỉ mục mẫu đã sinh
```
Một bạn định thử nhiều seed, giữ mẫu có mean thấp nhất và ghi đó là giá trung bình toàn bộ. Tính mean toàn bộ và mean mẫu hiện tại; viết lệnh cho kết quả cần báo cáo. Giải thích ngắn vai trò hữu ích của đọc mẫu và vì sao không được tự xoá 140.

#### B3-058

A C-order có các giá trị đôi một khác nhau:
```python
A = np.arange(12, dtype=np.int32).reshape(3, 4, order='C')
```
Cần B hai chiều cùng dtype, shape `(3,2)`, đọc đúng thứ tự:
```
B = [[A[0,0], A[0,2]],
     [A[1,0], A[1,2]],
     [A[2,1], A[2,3]]]
```
B có thể là view không di chuyển dữ liệu không? Dùng bước byte của các ô đầu hàng để giải thích. Sau đó viết một biểu thức NumPy tạo B đúng giá trị bằng bản sao, không dùng for hay API bộ nhớ khác.

#### B3-059

```python
x = np.array([3, 8, 5, 10], dtype=np.int32)
m = x >= 8
y = x[1:4:2]
y[:] = 0
x[m] = 1
```
Cho x, y sau cùng và hai tổng x.sum(), y.sum(). Nêu quan hệ bộ nhớ và ánh xạ các ô y; mask m có được tính lại sau khi sửa y không?

#### B3-060

Hàng là chỗ ở, cột là hai kỳ thu thập theo thứ tự thời gian. Cần chênh lệch so với mean chính hàng, đồng thời giữ nguyên ý nghĩa và thứ tự cột:
```python
P = np.array([[2., 6.], [10., 14.]])
Z = P - P.mean(axis=1, keepdims=True)
Z = Z[:, [1, 0]]
assert np.allclose(Z.mean(axis=1), 0, rtol=0, atol=1e-12)
```
(a) Assert có qua không; code đã đúng toàn bộ yêu cầu chưa? (b) Viết một biểu thức tạo Z đúng. (c) Nêu kết quả đúng và một kiểm tra có thể phát hiện việc đảo cột mà kiểm mean hàng không phát hiện.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR11

**Đọc thêm, không yêu cầu trên lớp.** Câu cung cấp quy ước: float32 có 1 bit dấu, 8 bit số mũ lưu E=e+127, 23 bit phần trị sau dấu chấm; số chuẩn hoá hiểu ngầm bit 1 trước dấu chấm. Cho `−13 = −1.101₂ × 2³`. Bộ ba `(bit dấu, E thập phân, các bit đầu phần trị)` nào đúng? Không yêu cầu nhớ struct hay giải mã giá trị đặc biệt.

A. `(0,130,101...)`

B. `(1,130,101...)`

C. `(1,3,101...)`

D. `(1,130,1101...)`

#### B3-MR12

```python
A = np.ones((2, 3), dtype=np.int32)
b = np.array([1, 2, 3], dtype=np.int32)
V = np.broadcast_to(b, A.shape)
R = A + b
```
Nêu giá trị, shape, dtype và nbytes của R; kiểm các cặp `(b,V)`, `(b,R)`, `(A,R)` có dùng chung dữ liệu không. Giải thích câu “broadcasting không nhân bản toàn bộ b” có mâu thuẫn với việc R cần vùng dữ liệu mới không. So sánh V.nbytes với số byte dữ liệu của b và nêu một cách kiểm chứng.

### Cập nhật độ bao phủ sau đợt 6

Đã dùng 56/56 mục tiêu trong yêu cầu trả lời. Không còn mục tiêu thiếu trong phạm vi đã xác định.

## Đối chiếu cuối bộ

- Đủ B3-001–B3-060: **60 câu**, **40 TN + 20 TL**; nhóm chính lần lượt **8/6/12/12/12/10**.
- Đủ B3-MR01–B3-MR12: **12 câu**, **8 TN + 4 TL**, đặt riêng ở từng đợt.
- Độ khó thiết kế phần trọng tâm: **15 nền tảng + 33 vận dụng + 12 phân loại**. Không coi đây là xác suất câu thật hoặc độ khó đo từ dữ liệu thi.
- Cả **56/56 mục tiêu** được dùng trong đề bài/lựa chọn cần đánh giá, không tính mục chỉ tình cờ nhắc trong lời giải. Các câu sửa code (a)–(b)–(c): **B3-010, B3-019, B3-030, B3-040, B3-050, B3-060**.
- Phạm vi tài liệu: đầy đủ mục bắt buộc trong ba nguồn Bài 3, gồm bài lab, kiểm chứng AI và mục tự học xác định. Phạm vi sách/website liên kết không được tuyên bố bao phủ toàn bộ. Mức ưu tiên lấy GK làm chuẩn; một số cơ chế tuần 3 dùng cho phân loại. `.base`, mảng tạm, stride âm, stride 0, phân vị, sinh số và bit float32 giữ ở phần bổ sung như nguồn.
- Rà trùng ý: có cặp đối chiếu có chủ đích để phân biệt cơ chế; câu khác dùng thay đổi về thao tác, hình dạng, đối tượng tổng hợp hoặc yêu cầu kiểm chứng, không chỉ đổi số/tên biến từ đề gốc. Không đặt cặp hoặc nhãn bẫy cạnh câu hỏi.

Đã thực thi 66/72 câu có ca code kiểm chứng trên NumPy 2.3.5. 6 câu thuần cơ chế/thiết kế đo được kiểm bằng suy luận; không tuyên bố đo benchmark hoặc kiểm mọi cấu hình SIMD/BLAS. Với bộ nhớ dùng `np.shares_memory` trực tiếp; số nguyên dùng `assert_array_equal`, số thực dùng `assert_allclose` hoặc assert chính xác khi số biểu diễn được.
