# BÀI 3 — ĐÁP ÁN, GIẢI THÍCH VÀ HƯỚNG DẪN CHẤM

Đọc cùng [file câu hỏi](<D:/LTXLDL_GK/output/bai3/Bai3_72_cau_hoi.md>).

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

## Cách đọc đáp án

TN: đáp án kèm lý do của đủ bốn lựa chọn, mỗi nhiễu gắn một lỗi suy luận. TL: lời giải mẫu và điểm thành phần, nhận cách đúng tương đương. Kiến thức/bẫy/mức độ chỉ xuất hiện ở đây. Kxx tra ở danh mục trong file câu hỏi. Tỷ lệ đáp án không theo quy luật cần đoán.

## Đợt 1

### A. Câu trọng tâm

#### B3-001

**Đáp án: B.**

- A sai: đảo byte mỗi ô với byte toàn mảng.
- B đúng: 2 chiều, 6 ô, mỗi int32 là 4 byte, tổng 24 byte.
- C sai: lấy số hàng làm size.
- D sai: đảo ndim và size.

**Đối chiếu:** nhóm 1; K01; mức Nền tảng. **Kiến thức và bẫy:** ndarray: shape, ndim, size, dtype, itemsize, nbytes. **Đọc lại:** BG §1; NB ô 2–7; LAB bài 1.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-002

**Đáp án: D.**

- A sai: áp quy tắc list * 2 cho ndarray.
- B sai: nhầm phép toán từng phần tử với tổng hợp.
- C sai: với số 2 biểu diễn được, phép nhân này trong NumPy 2.x giữ int32.
- D đúng: mỗi y[i]=x[i]*2; shape (4,), dtype int32.

**Đối chiếu:** nhóm 2; K07; mức Nền tảng. **Kiến thức và bẫy:** Ufunc từng phần tử; x*2 tương đương multiply; vector hoá phép biến đổi. **Đọc lại:** BG §2 ufunc; NB ô 24–25.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-003

**Đáp án: A.**

- A đúng: -1 chọn hàng cuối bằng chỉ mục nguyên nên bỏ chiều; -1: giữ chiều hàng.
- B sai: tưởng chỉ mục nguyên giữ chiều.
- C sai: tưởng giữ chiều tức tạo cột.
- D sai: tưởng -1 là một lát cắt lấy cả hai hàng.

**Đối chiếu:** nhóm 3; K12; mức Vận dụng. **Kiến thức và bẫy:** Chỉ mục hàng/cột, chỉ mục âm; chỉ mục nguyên bỏ chiều, slicing giữ chiều. **Đọc lại:** BG §3; NB ô 42–43,95–96.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-004

**Đáp án: C.**

- A sai: mask cùng shape chọn từng ô True, không giữ hình chữ nhật và không lấy số 1.
- B sai: duyệt theo cột thay vì theo hàng.
- C đúng: lấy A[0,0], A[0,2], A[1,1]; đọc mask tạo bản sao.
- D sai: nhầm boolean indexing với basic slicing.

**Đối chiếu:** nhóm 4; K23; mức Vận dụng. **Kiến thức và bẫy:** Mask bool cùng shape chọn ô theo hàng; mask 1D chọn hàng. **Đọc lại:** BG §3; NB ô 66–67.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-005

**Đáp án: B.**

- A sai: chiều 1 dùng để đối chiếu không được tự thêm vào metadata của b.
- B đúng: (2,3)+(3,)→(2,3); C[i,j]=A[i,j]+b[j], b vẫn (3,).
- C sai: đảo shape kết quả theo thứ tự toán hạng.
- D sai: broadcasting cho phép chiều thiếu xem như 1.

**Đối chiếu:** nhóm 5; K33; mức Vận dụng. **Kiến thức và bẫy:** Broadcast từ phải sang trái; chiều thiếu như 1 không đổi shape gốc. **Đọc lại:** BG §4 quy tắc broadcasting.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-006

**Đáp án: D.**

- A sai: đổi shape không giảm số ô.
- B sai: trả itemsize thay vì nbytes.
- C sai: giữ dung lượng và strides cũ dù astype đổi itemsize từ 2 lên 8.
- D đúng: 8 ô × 2 byte; R vẫn 8 ô int16; F có 8 ô float64, 4 ô mỗi hàng nên strides (4*8,8)=(32,8). Các nbytes chưa gồm metadata.

**Đối chiếu:** nhóm 1; K03; mức Vận dụng. **Kiến thức và bẫy:** Đổi shape giữ số ô; đổi dtype đổi itemsize, nbytes, strides; nbytes không gồm metadata. **Đọc lại:** BG §1 dung lượng; LAB bài 1.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-007

**Đáp án: A.**

- A đúng: tổng 400/5=80; số giữa sau sắp xếp là 40. Median phù hợp mục tiêu đã nêu.
- B sai: đảo mean và median, đồng thời đảo tính nhạy với cực trị.
- C sai: độ lớn chưa phải bằng chứng giá sai, và đề xác nhận hợp lệ.
- D sai: median không phải phần tử cuối của dãy.

**Đối chiếu:** nhóm 6; K40; mức Nền tảng. **Kiến thức và bẫy:** Mean, median, min/max, sum; giá cực lớn và mức giá điển hình. **Đọc lại:** BG §5 mô tả mức giá; LAB bài 8.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-008

V có shape `(2,2)`, strides `(32,8)` byte, ô đầu là A[1,1], offset `16+4=20` byte. V[1,0] là A[3,1], được đổi từ 13 thành 90, offset `20+1*32+0*8=52` byte. Số 32 chỉ là độ lệch từ đầu V, còn đầu V đã lệch 20 byte so với đầu A. V dùng chung dữ liệu với A; mỗi ô V[i,j] ánh xạ A[1+2*i,1+2*j].

**Hướng dẫn chấm:** 2 điểm: shape và strides 0,5; offset đầu 0,5; ô/offset bị sửa 0,5; giải thích cộng offset và dùng chung 0,5.

**Đối chiếu:** nhóm 3; K14, K13; mức Phân loại. **Kiến thức và bẫy:** Offset từ đầu view khác đầu gốc; ánh xạ phép gán qua view; start:stop:step, stop loại trừ, shape và strides byte của view. **Đọc lại:** BG §3 bài tập 4; LAB bài 2.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-009

W[1,0] chính là C[0,1], nên C=`[[16,77],[4,6]]`; A vẫn `[[2,4,6],[8,10,12],[14,16,18]]`. Chỉ `(C,W)` dùng chung. C được đọc bằng chỉ mục nâng cao nên đã là bản sao; transpose W dùng chung với C, không nối về A. Ban đầu C[0,1] lấy giá trị A[2,2], nhưng sau khi sao chép đó là hai ô dữ liệu độc lập.

**Hướng dẫn chấm:** 2 điểm: ánh xạ và C 0,75; A 0,5; ba quan hệ dùng chung và nguyên nhân 0,75.

**Đối chiếu:** nhóm 4; K29, K32; mức Phân loại. **Kiến thức và bẫy:** View sau advanced indexing chỉ dùng chung với bản sao; ánh xạ ô; B=A, copy, basic view, advanced copy; giá trị bằng nhau khác shares_memory. **Đọc lại:** BG §3 view/copy; DS1 câu 15 (biến thể cơ chế).

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-010

(a) P `(2,3)` còn tb `(2,)`; so chiều cuối 3 với 2 không ghép được, gây ValueError. (b) `lech = P - P.mean(axis=1, keepdims=True)`. Cũng nhận `P - tb[:,None]` hoặc `P - tb.reshape(-1,1,order='C')`. (c) Trung bình `(2,1)` là `[[18],[36]]`; đầu ra `(2,3)`, float64, `[[−6,0,6],[−6,0,6]]`. Mỗi `lech[i,j]=P[i,j]−mean(P[i,:])`, đơn vị USD/đêm. Kiểm hàng đầu tính tay và `np.allclose(lech.mean(axis=1),0,rtol=0,atol=1e-12)`.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm gồm hai shape và lỗi chiều cuối; (b) 1 điểm biểu thức đúng; (c) 1 điểm gồm kết quả/ý nghĩa 0,5 và kiểm chứng 0,5.

**Đối chiếu:** nhóm 5; K37, K36, K39; mức Vận dụng. **Kiến thức và bẫy:** Trừ trung bình chính hàng; ma trận chữ nhật báo lỗi, ma trận vuông che lỗi; Axis là chiều gộp; tập phần tử, mẫu số; shape sum/mean có/không keepdims; Kiểm chứng ý nghĩa bằng ô tính tay và bất biến; assert chỉ là kiểm một số yêu cầu. **Đọc lại:** BG §5; LAB bài 6; GK câu 21 về cấu trúc giải thích/sửa/diễn giải.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR01

**Đáp án: C.**

- A sai: kiểm tra đồng nhất .base không phải phép kiểm tổng quát về dùng chung.
- B sai: giá trị bằng nhau không quyết định copy/view.
- C đúng: b dùng chung các ô của a dù .base bỏ qua mảng trung gian.
- D sai: view của view vẫn có thể dùng chung. b[i,j] ánh xạ a[i,j+1].

**Đối chiếu:** nhóm 3; K47; mức Bổ sung. **Kiến thức và bẫy:** .base có thể bỏ qua mảng trung gian; dùng shares_memory. **Đọc lại:** NB ô 64–65: Đọc thêm .base.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-MR02

**Đáp án: A.**

- A đúng: có thể tách t=A*3; R=t+5, tương ứng hai phép tính và các vùng kết quả riêng.
- B sai: một dòng mã không đồng nghĩa một phép toán hợp nhất.
- C sai: các phép tính chạy trong thư viện, không sinh for Python cho người dùng.
- D sai: toán tử * và + thông thường ở đây tạo mảng mới, không phải phép gán tại chỗ.

**Đối chiếu:** nhóm 2; K48; mức Bổ sung. **Kiến thức và bẫy:** Một biểu thức có thể tạo nhiều mảng tạm và nhiều lượt đọc/ghi. **Đọc lại:** NB ô 40: Đọc thêm mảng trung gian.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### Cập nhật độ bao phủ sau đợt 1

Đã dùng 16/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K02, K04, K05, K06, K08, K09, K10, K11, K15, K16, K17, K18, K19, K20, K21, K22, K24, K25, K26, K27, K28, K30, K31, K34, K35, K38, K41, K42, K43, K44, K45, K46, K49, K50, K51, K52, K53, K54, K55, K56. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 2

### A. Câu trọng tâm

#### B3-011

**Đáp án: C.**

- A sai: ndarray số 2D không phải cấu trúc list lồng nhau.
- B sai: dãy ô liên tiếp của list là các tham chiếu tới đối tượng, không phải các số int32 lưu trực tiếp.
- C đúng: phân biệt nội dung ô và metadata; không áp mô hình mảng số cho object.
- D sai: C-order đi theo hàng; nbytes không tính metadata.

**Đối chiếu:** nhóm 1; K02; mức Nền tảng. **Kiến thức và bẫy:** Metadata, C-order; list CPython lưu tham chiếu; mảng số và dtype=object. **Đọc lại:** BG §1 cách lưu list/ndarray, ghi chú dtype=object; NB ô 4–9.

**Kiểm chứng:** Đã kiểm bằng suy luận; không có code cần thực thi. Không đo hiệu năng thực tế.

#### B3-012

**Đáp án: A.**

- A đúng: ghép y[i] với x[i], kết quả [4,1,0,9], dtype int32.
- B sai: gộp các chênh lệch rồi bình phương, cho scalar 16.
- C sai: giá trị đúng nhưng vẫn dùng vòng lặp Python và trả list, không đáp ứng yêu cầu. Không phủ nhận nó đúng nếu đề cho phép vòng lặp/list.
- D sai: hiệu hai bình phương khác bình phương của hiệu.

**Đối chiếu:** nhóm 2; K07; mức Vận dụng. **Kiến thức và bẫy:** Ufunc từng phần tử; x*2 tương đương multiply; vector hoá phép biến đổi. **Đọc lại:** BG §2 bài tập 2; LAB bài 7.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-013

**Đáp án: D.**

- A sai: quên nhân stride hàng với bước 2.
- B sai: đếm cả stop=3 như một cột được lấy; cột chỉ có 0 và 2.
- C sai: dùng đơn vị phần tử thay cho byte.
- D đúng: hàng 1,3 và cột 0,2; A.strides=(16,4), nhân bước từng chiều ra (32,8).

**Đối chiếu:** nhóm 3; K13; mức Vận dụng. **Kiến thức và bẫy:** start:stop:step, stop loại trừ, shape và strides byte của view. **Đọc lại:** BG §3 strides; LAB bài 2; GK câu 6.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-014

**Đáp án: B.**

- A sai: hoán đổi mask chọn hàng với mask chọn ô.
- B đúng: mask hàng (3,) chọn hàng 1,2 giữ hai cột; mask ô (3,2) chọn 9,7,8 theo hàng.
- C sai: tưởng mask hàng chỉ trả phần tử cột 0, còn mask ô giữ nguyên toàn bảng.
- D sai: tưởng mask cùng shape luôn cho hình chữ nhật. Cả r và s đều là bản sao của dữ liệu được chọn.

**Đối chiếu:** nhóm 4; K23; mức Vận dụng. **Kiến thức và bẫy:** Mask bool cùng shape chọn ô theo hàng; mask 1D chọn hàng. **Đọc lại:** BG §3; NB ô 66–67; LAB bài 4.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-015

**Đáp án: C.**

- A sai: broadcasting so chiều cuối trước, không đoán ý nghĩa số hàng.
- B sai: (2,3)+(1,2) vẫn không khớp chiều cuối.
- C đúng: (2,3)+(2,1)→(2,3); kết quả[i,j]=A[i,j]+d[i].
- D sai: A.T+d có shape (3,2), không phải shape yêu cầu; transpose lại mới có thể là cách tương đương đúng.

**Đối chiếu:** nhóm 5; K33, K34; mức Vận dụng. **Kiến thức và bẫy:** Broadcast từ phải sang trái; chiều thiếu như 1 không đổi shape gốc; Hệ số riêng theo cột, theo hàng, kết hợp cả hai. **Đọc lại:** BG §4 Vì sao A+d bị lỗi.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-016

**Đáp án: A.**

- A đúng: nhân trong int8 tràn trước; đổi trước sang int16 giữ kết quả toán học. a và b đều int16 nhưng khác giá trị.
- B sai: cho rằng astype sau phép nhân có thể khôi phục giá trị.
- C sai: cho rằng đổi trước vẫn buộc tính trong int8.
- D sai: đảo thời điểm tác dụng của chuyển kiểu.

**Đối chiếu:** nhóm 1; K04; mức Nền tảng. **Kiến thức và bẫy:** Giới hạn int8, khác int Python; astype trước/sau tràn. **Đọc lại:** BG §1 bài tập 1; NB ô 10–17.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-017

**Đáp án: D.**

- A sai: lấy trung bình hai phần tử đầu theo thứ tự thu thập (8+2)/2=5, chưa sắp xếp.
- B sai: median không phải phần tử lớn nhất.
- C sai: mean phải chia tổng cho 4.
- D đúng: sắp xếp [2,4,8,10], median=(4+8)/2=6; tổng 24, min 2, max 10.

**Đối chiếu:** nhóm 6; K40; mức Nền tảng. **Kiến thức và bẫy:** Mean, median, min/max, sum; giá cực lớn và mức giá điển hình. **Đọc lại:** BG §5; NB ô 102–105.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-018

P=`[0,2,4,6,8,10]`, Q=`[1,2,5,6,9,10]`; cặp `(True,False)`. Các ô P cách đều 8 byte nên một chiều stride 8 đọc được dù lát cắt không C-contiguous. Với Q, các bước là 4,12,4,12,4 byte; không thể là view 1D có một stride cố định theo thứ tự C đó nên reshape tạo dữ liệu riêng so với A. Cả hai dtype int32, shape (6,), nbytes 24. Không thể kết luận chỉ từ việc không C-contiguous.

**Hướng dẫn chấm:** 2 điểm: hai giá trị 0,5; quan hệ dùng chung 0,5; phân tích bước byte 0,75; bác bỏ khẳng định quá mức 0,25.

**Đối chiếu:** nhóm 3; K17; mức Phân loại. **Kiến thức và bẫy:** Reshape mảng không liên tục có thể view hoặc copy; kiểm shares_memory và ô bị sửa. **Đọc lại:** BG §3 reshape; DS1 câu 14; AI2 câu 2.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-019

(a) A không đổi: đọc `T[[1],:]` tạo bản sao do chỉ mục nâng cao, phép gán sau ghi vào bản sao tạm. T vẫn là view của A nhưng không làm bước chọn đầu thành view. (b) `T[np.ix_([1],[0,2])] = 0`; cũng nhận `T[1,[0,2]]=0`. (c) T[1,0]↔A[0,1] và T[1,2]↔A[2,1]; A=`[[2,0,6],[8,10,12],[14,0,18]]`. Kiểm toàn A với mảng kỳ vọng và `np.shares_memory(A,T)` là True. Đích ix_ shape (1,2), scalar 0 shape () được dùng cho hai ô.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm xác định copy tạm; (b) 1 điểm gán đúng; (c) 1 điểm ánh xạ/kết quả 0,5 và kiểm chứng 0,5.

**Đối chiếu:** nhóm 4; K28, K15, K30; mức Phân loại. **Kiến thức và bẫy:** Chọn nâng cao trước rồi gán bước sau chỉ sửa bản sao tạm; Transpose đổi shape/strides; T[i,j] ánh xạ A[j,i]; ix_ chỉ tạo chỉ mục; đọc tạo copy, gán trực tiếp và broadcasting RHS. **Đọc lại:** BG §3 ghi chú ix_; DS2 câu 12.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-020

u=`[5,7,9]`, shape (3,): trung bình hai cửa hàng theo từng ngày. u[1]=(D[0,1]+D[1,1])/2=(4+10)/2=7. v=`[[12],[30]]`, shape (2,1): tổng ba ngày của từng cửa hàng, giữ chiều cột bằng 1. t=7, shape (): trung bình tất cả 6 ô, tổng 42/6. Cả ba kết quả có dtype float64. Axis 0 gộp hàng; axis 1 gộp cột.

**Hướng dẫn chấm:** 2 điểm: giá trị/shape ba kết quả 1 điểm; tập ô và mẫu số u[1] 0,5; diễn giải theo hàng/cột 0,5.

**Đối chiếu:** nhóm 5; K36; mức Vận dụng. **Kiến thức và bẫy:** Axis là chiều gộp; tập phần tử, mẫu số; shape sum/mean có/không keepdims. **Đọc lại:** BG §5 axis/keepdims; NB ô 106–109.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR03

**Đáp án: B.**

- A sai: khả năng giữ phần tăng phụ thuộc độ lớn và số bit có nghĩa, không chỉ giá trị của số cộng.
- B đúng: phép cộng được làm rồi làm tròn về giá trị float32 biểu diễn được; float64 giữ được 1 ở ví dụ này.
- C sai: định dạng in không sửa giá trị đã lưu.
- D sai: bằng nhau sau làm tròn không có nghĩa không tính phép cộng.

**Đối chiếu:** nhóm 1; K49, K05; mức Bổ sung. **Kiến thức và bẫy:** float32 với số lớn có thể làm mất phần tăng nhỏ; float32/64: bộ nhớ, gần đúng, chữ số in không tăng độ chính xác. **Đọc lại:** NB ô 118: Tự học sai số theo độ lớn.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-MR04

Strides `(0,4)` byte; V.nbytes=4*3*4=48, nhưng chỉ dùng lại ba ô b.nbytes=12, không cấp phát 48 byte dữ liệu phần tử mới. Metadata view vẫn được tạo. `np.shares_memory(b,V)` True; mọi V[i,j] đọc b[j]. V[3,1] offset `3*0+1*4=4` byte, giá trị 5. V là view chỉ đọc; phép gán gây ValueError và không sửa b, không phải chỉ cảnh báo. Khoảng byte bao trùm các ô thực đọc là 12 byte.

**Hướng dẫn chấm:** 2 điểm: strides/nbytes 0,5; dùng chung/cấp phát 0,5; offset/ánh xạ 0,5; chỉ đọc và ValueError 0,5.

**Đối chiếu:** nhóm 5; K50, K19; mức Bổ sung. **Kiến thức và bẫy:** broadcast_to: stride 0, chia sẻ, chỉ đọc; broadcasting không sao toán hạng nhưng phép cộng tạo kết quả; nbytes của view khác khoảng byte bao trùm và lượng dữ liệu mới cấp phát. **Đọc lại:** NB ô 119–120: Đọc thêm stride 0.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### Cập nhật độ bao phủ sau đợt 2

Đã dùng 27/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K08, K09, K10, K11, K16, K18, K20, K21, K22, K24, K25, K26, K27, K31, K35, K38, K41, K42, K43, K44, K45, K46, K51, K52, K53, K54, K55, K56. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 3

### A. Câu trọng tâm

#### B3-021

**Đáp án: B.**

- A sai: định dạng in không đổi dtype.
- B đúng: đây là thay đổi cách trình bày, không đổi các bit dữ liệu.
- C sai: hiển thị thêm không bổ sung thông tin chính xác đã mất.
- D sai: float64 cũng hữu hạn; chuyển từ float32 không khôi phục thông tin đã làm tròn.

**Đối chiếu:** nhóm 1; K05; mức Nền tảng. **Kiến thức và bẫy:** float32/64: bộ nhớ, gần đúng, chữ số in không tăng độ chính xác. **Đọc lại:** BG §1 độ chính xác; NB ô 12–13; AI5 câu 1, DS1 câu 6.

**Kiểm chứng:** Đã kiểm bằng suy luận; không có code cần thực thi. Không đo hiệu năng thực tế.

#### B3-022

**Đáp án: C.**

- A sai: NumPy không tự JIT vòng for của người dùng khi tạo ndarray.
- B sai: cùng itemsize không đồng nghĩa cùng kiểu số hay cùng mã tính.
- C đúng: vẫn phải tính từng số, nhưng nơi xử lý vòng lặp và chi phí đối tượng khác nhau.
- D sai: NumPy có phép nhân int64; không cần chuyển sang float để vector hoá.

**Đối chiếu:** nhóm 2; K08, K07; mức Vận dụng. **Kiến thức và bẫy:** Vòng lặp thư viện biên dịch sẵn, dtype chọn cách đọc/tính; for Python vẫn còn chi phí; Ufunc từng phần tử; x*2 tương đương multiply; vector hoá phép biến đổi. **Đọc lại:** BG §2; NB ô 23–29; GK câu 7.

**Kiểm chứng:** Đã kiểm bằng suy luận; không có code cần thực thi. Không đo hiệu năng thực tế.

#### B3-023

**Đáp án: A.**

- A đúng: hoán thứ tự shape/strides; T[2,1]=A[1,2]=6. T dùng chung với A.
- B sai: cho rằng transpose sắp lại dữ liệu thành C-order liên tục mới.
- C sai: tưởng transpose không đổi metadata.
- D sai: truy về A[1,1], bỏ qua chỉ mục cột 2.

**Đối chiếu:** nhóm 3; K15; mức Nền tảng. **Kiến thức và bẫy:** Transpose đổi shape/strides; T[i,j] ánh xạ A[j,i]. **Đọc lại:** BG §3 chuyển vị; NB ô 58–59.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-024

**Đáp án: D.**

- A sai: and cần truth value đơn, mảng nhiều phần tử gây ValueError; đây không phải vấn đề tốc độ.
- B sai: lấy thêm 0 và bỏ 8 do sai cả hai biên.
- C sai: hợp hai điều kiện chọn mọi ô ở ví dụ này.
- D đúng: hai mask có ngoặc, giao điều kiện, kết quả [1,7,8].

**Đối chiếu:** nhóm 4; K24; mức Vận dụng. **Kiến thức và bẫy:** Điều kiện biên, &, |, ngoặc; and/or đòi truth value đơn. **Đọc lại:** BG §3 nhiều điều kiện; DS2 câu 7.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-025

**Đáp án: B.**

- A sai: lấy c[0] cho hàng 0, c[1] cho hàng 1 và bỏ c[2], không theo quy tắc ghép từ phải.
- B đúng: (2,3)+(3,)→(2,3), R[i,j]=A[i,j]+c[j].
- C sai: làm phép nhân thay phép cộng.
- D sai: c khớp số cột, chiều hàng thiếu được xem như 1.

**Đối chiếu:** nhóm 5; K34, K33; mức Vận dụng. **Kiến thức và bẫy:** Hệ số riêng theo cột, theo hàng, kết hợp cả hai; Broadcast từ phải sang trái; chiều thiếu như 1 không đổi shape gốc. **Đọc lại:** BG §4 cộng theo cột; LAB bài 5.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-026

**Đáp án: A.**

- A đúng: mean=20, độ lệch ±10; tổng bình phương 400, chia 4 được 100 rồi căn 10.
- B sai: đảo var/std và đơn vị.
- C sai: quên bước lấy trung bình bình phương.
- D sai: dùng ddof=1 thay mặc định 0; công thức đó không phải lời gọi đã cho.

**Đối chiếu:** nhóm 6; K41; mức Nền tảng. **Kiến thức và bẫy:** Var/std ddof=0, đơn vị; cùng mean khác phân tán. **Đọc lại:** BG §5 độ phân tán; NB ô 104–105.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-027

**Đáp án: C.**

- A sai: đếm với <40 được ba ô, nhưng đề dùng <=40 nên phải lấy thêm giá 40.
- B sai: mẫu số phải là toàn bộ 6 phần tử mask, không phải riêng số True.
- C đúng: mask [True,True,True,True,False,False], True tính như 1 khi lấy mean.
- D sai: mean mask lấy số True chia số quan sát, không cộng giá.

**Đối chiếu:** nhóm 6; K42, K24; mức Vận dụng. **Kiến thức và bẫy:** Mean mask bool là tỷ lệ True với đúng tập đối tượng và mẫu số; Điều kiện biên, &, |, ngoặc; and/or đòi truth value đơn. **Đọc lại:** LAB bài 8 tỷ lệ; BG §3 điều kiện biên.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-028

Trước T, các ô có offset từ đầu A là 4,12,36,44 byte. Sau T, V=`[[1,9],[3,11]]`, shape (2,2), strides (8,32). V.nbytes=4*4=16 byte. Ô có offset nhỏ nhất 4, ô cuối bắt đầu ở 44 và chiếm [44,48), nên đoạn bao trùm [4,48) dài `44−4+4=44` byte. V dùng chung A, không cấp phát dữ liệu phần tử mới (0 byte); metadata view vẫn mới. Ba con số 16,44,0 trả lời ba câu hỏi khác nhau.

**Hướng dẫn chấm:** 2 điểm: shape/strides/nbytes 0,75; hai đầu và chiều dài bao trùm 0,75; cấp phát/dùng chung 0,5.

**Đối chiếu:** nhóm 3; K19, K15; mức Phân loại. **Kiến thức và bẫy:** nbytes của view khác khoảng byte bao trùm và lượng dữ liệu mới cấp phát; Transpose đổi shape/strides; T[i,j] ánh xạ A[j,i]. **Đọc lại:** BG §1 nbytes, §3 strides; AI5 câu 11.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-029

idx gồm mảng hàng shape (2,1) và cột shape (1,2); ix_ chỉ tạo bộ chỉ mục. Đọc A[idx] mới tạo B shape (2,2) độc lập với A, ban đầu `[[9,11],[1,3]]`, sau sửa thành toàn −1 và không đổi nữa. Gán trực tiếp sửa A[2,1]=50, A[2,3]=60, A[0,1]=50, A[0,3]=60. A=`[[0,50,2,60],[4,5,6,7],[8,50,10,60]]`. RHS (2,) được so như (1,2), lặp qua hàng của vùng chọn (2,2): ô vùng chọn [i,j] nhận RHS[j]. Không phải mỗi hàng nhận một số. RHS [50,60,70] có shape (3,), không ghép được chiều cuối 2 của vùng chọn, gây ValueError.

**Hướng dẫn chấm:** 2 điểm: shape chỉ mục/B và copy 0,5; B sau cùng 0,25; A/ánh xạ 0,75; broadcasting RHS đúng và trường hợp lỗi 0,5.

**Đối chiếu:** nhóm 4; K30, K26; mức Vận dụng. **Kiến thức và bẫy:** ix_ chỉ tạo chỉ mục; đọc tạo copy, gán trực tiếp và broadcasting RHS; Hai mảng chỉ mục ghép từng cặp; ix_ chọn tích hàng × cột. **Đọc lại:** BG §3 ix_ đọc/gán; NB ô 78–83.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-030

(a) Không lỗi: D (2,2), tổng hàng (2,) là [8,12]; broadcasting chia cột j cho tổng hàng j, dù đó không phải kho chứa phần tử. P=`[[1/4,1/2],[3/8,3/4]]`. (b) `P=D/D.sum(axis=1,keepdims=True)`. (c) Mẫu số (2,1) là [[8],[12]], P đúng=`[[1/4,3/4],[1/4,3/4]]`, float64, shape (2,2). P[i,j]=D[i,j]/sum(D[i,:]); mỗi hàng biểu diễn phân bố lượt của chính kho qua các tuần. Kiểm tay 6/8=3/4 và `np.allclose(P.sum(axis=1),1,rtol=0,atol=1e-12)`.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm shape/kết quả/ghép sai; (b) 1 điểm sửa; (c) 1 điểm gồm ý nghĩa/kết quả 0,5 và kiểm chứng 0,5.

**Đối chiếu:** nhóm 5; K38, K39; mức Phân loại. **Kiến thức và bẫy:** Chia cho tổng hàng/cột: shape, mẫu số và ý nghĩa khác nhau; Kiểm chứng ý nghĩa bằng ô tính tay và bất biến; assert chỉ là kiểm một số yêu cầu. **Đọc lại:** BG §4–5; GK câu 21 (biến thể vuông và kiểm chứng).

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR05

**Đáp án: D.**

- A sai: bỏ qua nội suy được đề cung cấp.
- B sai: nhầm thang đo đối số của percentile; 25 là 25%, không phải 0.25%.
- C sai: nhầm thang đo quantile; 0.25 là 25%, không phải 0.25%.
- D đúng: vị trí 3*0.25=0.75, nội suy 0+0.75*(10−0)=7.5. Hai hàm dùng cùng mức phân vị.

**Đối chiếu:** nhóm 6; K51; mức Bổ sung. **Kiến thức và bẫy:** Percentile 0–100, quantile 0–1; phương pháp linear và nội suy. **Đọc lại:** NB ô 125–127: phân vị tự học.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-MR06

**Đáp án: A.**

- A đúng: integers loại cận trên; random lấy trong [0,1); cả hai có shape (4,).
- B sai: đóng cả hai cận trên vốn bị loại trừ.
- C sai: mở cận dưới, đóng cận trên trái quy ước.
- D sai: seed không đặt giới hạn giá trị hay ngăn lặp; miền do hàm/tham số quy định.

**Đối chiếu:** nhóm 6; K52; mức Bổ sung. **Kiến thức và bẫy:** integers cận trên loại trừ; random thuộc [0,1). **Đọc lại:** NB ô 128–131: tra cứu thêm tự học.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### Cập nhật độ bao phủ sau đợt 3

Đã dùng 35/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K09, K10, K11, K16, K18, K20, K21, K22, K25, K27, K31, K35, K43, K44, K45, K46, K53, K54, K55, K56. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 4

### A. Câu trọng tâm

#### B3-031

**Đáp án: D.**

- A sai: int8 cố định 1 byte, không tự mở rộng như int Python.
- B sai: b đổi sau khi tràn nên giữ giá trị −128 đã sai.
- C sai: int(v) chuyển sang int Python, phép cộng sau đó không chạy trong int8.
- D đúng: a dtype int8, b/c dtype int16; c đúng giá trị nhưng vẫn dùng vòng lặp Python.

**Đối chiếu:** nhóm 1; K04; mức Vận dụng. **Kiến thức và bẫy:** Giới hạn int8, khác int Python; astype trước/sau tràn. **Đọc lại:** BG §1 int8; NB ô 10–17.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-032

**Đáp án: B.**

- A sai: cache không thay đổi số phần tử hay số phép toán về mặt bài toán.
- B đúng: tận dụng tính gần nhau của dữ liệu; còn phụ thuộc cách duyệt, kích thước và phép tính.
- C sai: một luồng cũng sử dụng cache.
- D sai: bảng tham chiếu list cũng liên tiếp; còn có bước truy cập đối tượng được tham chiếu. Không suy ra NumPy luôn nhanh hơn ở mọi kích thước.

**Đối chiếu:** nhóm 2; K09; mức Nền tảng. **Kiến thức và bẫy:** Truy cập liên tiếp và cache; không suy ra tốc độ từ một yếu tố. **Đọc lại:** BG §2 cache; NB ô 30.

**Kiểm chứng:** Đã kiểm bằng suy luận; không có code cần thực thi. Không đo hiệu năng thực tế.

#### B3-033

**Đáp án: C.**

- A sai: hoán đổi kết quả reshape với transpose.
- B sai: đồng nhất transpose với đọc lại dãy C-order.
- C đúng: dãy C là [2,5,8,3,6,9], chia thành cặp; T[1] lấy cột 1 của A.
- D sai: đảo thứ tự trong mỗi cặp dù không có thao tác đảo chiều.

**Đối chiếu:** nhóm 3; K16, K15; mức Vận dụng. **Kiến thức và bẫy:** Reshape C-order giữ thứ tự đọc và số phần tử; khác transpose; Transpose đổi shape/strides; T[i,j] ánh xạ A[j,i]. **Đọc lại:** BG §3 transpose/reshape; NB ô 58–61.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-034

**Đáp án: A.**

- A đúng: x thành [3,1,5,1], y độc lập thành [0,0].
- B sai: tưởng advanced indexing tạo copy nên gán trực tiếp x[m] cũng không sửa được x.
- C sai: tưởng y vẫn đồng bộ với các ô đã chọn trong x sau phép gán.
- D sai: tưởng sửa y làm x thành [3,0,5,0] và bỏ qua gán trực tiếp sau đó.

**Đối chiếu:** nhóm 4; K25; mức Vận dụng. **Kiến thức và bẫy:** Đọc A[mask] là copy; gán A[mask]=... sửa đích. **Đọc lại:** BG §3 mask đọc/gán; NB ô 68–71.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-035

**Đáp án: D.**

- A sai: chỉ cộng hệ số c[0]=2 thay c[2]=6.
- B sai: quên số cộng theo hàng r[1]=20.
- C sai: cho rằng shape cuối bị r[:,None] ép còn một cột.
- D đúng: (2,3)+(2,1)+(3,)→(2,3); B[i,j]=A[i,j]+r[i]+c[j], nên 6+20+6=32.

**Đối chiếu:** nhóm 5; K34, K33; mức Vận dụng. **Kiến thức và bẫy:** Hệ số riêng theo cột, theo hàng, kết hợp cả hai; Broadcast từ phải sang trái; chiều thiếu như 1 không đổi shape gốc. **Đọc lại:** BG §4 bài tập 5; LAB bài 5.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-036

**Đáp án: B.**

- A sai: cùng vị trí trung tâm không quyết định độ phân tán.
- B đúng: Y lệch ±20, phương sai 400 USD² và std 20 USD; X không lệch.
- C sai: nhầm phương sai với độ lệch chuẩn và đơn vị.
- D sai: vài thống kê không xác định phân phối, và hai dãy ở đây khác nhau rõ ràng.

**Đối chiếu:** nhóm 6; K41; mức Nền tảng. **Kiến thức và bẫy:** Var/std ddof=0, đơn vị; cùng mean khác phân tán. **Đọc lại:** BG §5 độ phân tán; NB ô 104–105.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-037

**Đáp án: C.**

- A sai: trả các bản ghi đúng cặp nhưng sai thứ tự yêu cầu: mã 101 trước 103 thay vì 103 trước 101; giá tình cờ bằng nhau không xoá được khác biệt chỉ mục.
- B sai: ghép cặp chỉ mục hàng/cột; cột 2 còn vượt phạm vi.
- C đúng: [[103,40],[101,40]], shape (2,2); chọn cùng chỉ mục cho toàn bộ trường của mỗi dòng.
- D sai: idx là chỉ mục dòng, dùng cho cột sẽ chọn sai chiều và cột 2 vượt phạm vi.

**Đối chiếu:** nhóm 6; K43, K44; mức Vận dụng. **Kiến thức và bẫy:** default_rng, choice, size; lấy mẫu chỉ mục giữ các cột cùng bản ghi; replace=False không trùng vị trí nhưng giá trị có thể trùng; giới hạn size. **Đọc lại:** BG §5 lấy mẫu; LAB bài 8.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-038

T được đọc C-order theo dãy [1,2,4,5,7,8]. R trước sửa là [[1,2,4],[5,7,8]], sau sửa [[1,99,4],[5,7,8]]. W[0,0]↔R[0,1]. A vẫn [[1,4,7],[2,5,8]]. Các cặp lần lượt True, False, True, False. T là view của A; reshape theo C ở cách bố trí này phải copy so với A. W chỉ là view của vùng dữ liệu R, không nối trở lại A. Không suy luận copy chỉ từ giá trị hay `.base`.

**Hướng dẫn chấm:** 2 điểm: dãy đọc/R 0,75; A và ánh xạ W 0,5; bốn quan hệ và bước copy 0,75.

**Đối chiếu:** nhóm 3; K18, K15; mức Phân loại. **Kiến thức và bẫy:** Transpose rồi reshape C-order có thể copy; view của copy không nối về gốc; Transpose đổi shape/strides; T[i,j] ánh xạ A[j,i]. **Đọc lại:** BG §3; NB ô 58–59; AI2 câu 14.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-039

m được tính một lần là [True,False,True], không tự cập nhật. Sau gán v[:] thì v=[1,20,2]; lệnh cuối đọc bản sao v[m]=[1,2], cộng 5 được [6,7], rồi gán trực tiếp vào v[0],v[2]. v cuối [6,20,7], x cuối [4,6,20,7]. Ô x[1] và x[3] được cộng, x[2]=20 không được cộng vì m[1] đã là False. v dùng chung x, còn các kết quả đọc nâng cao không dùng chung dữ liệu v; gán trực tiếp vẫn ghi vào v và qua đó sửa x.

**Hướng dẫn chấm:** 2 điểm: mask giữ nguyên 0,5; v/x 0,75; ô sửa và 20 0,5; phân biệt đọc/gán 0,25.

**Đối chiếu:** nhóm 4; K31, K25, K32; mức Phân loại. **Kiến thức và bẫy:** Mask đã tính không tự tính lại khi mảng số bị sửa; Đọc A[mask] là copy; gán A[mask]=... sửa đích; B=A, copy, basic view, advanced copy; giá trị bằng nhau khác shares_memory. **Đọc lại:** BG §3 mask đọc/gán; AI2 câu 12 (biến thể không bước âm).

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-040

(a) P (2,2), tb (2,)=[3,12]; chiều cuối khớp nên phép trừ dùng tb[j] cho cột j. lech sai=[[-1,−8],[7,2]]. (b) `lech=P-P.mean(axis=1,keepdims=True)`, hoặc `P-tb[:,None]`. (c) tb đúng để dùng lại có shape (2,1); lech=[[-1,1],[−2,2]], shape (2,2), float64. Ô [i,j] trừ mean của hàng i; mỗi hàng có mean gần 0. Chấp nhận kiểm `np.allclose(lech.mean(axis=1),0,rtol=0,atol=1e-12)` và ví dụ 4−3=1.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm nêu shape, hướng ghép và lech; (b) 1 điểm sửa; (c) 1 điểm kết quả/ý nghĩa và kiểm chứng.

**Đối chiếu:** nhóm 5; K37, K39; mức Vận dụng. **Kiến thức và bẫy:** Trừ trung bình chính hàng; ma trận chữ nhật báo lỗi, ma trận vuông che lỗi; Kiểm chứng ý nghĩa bằng ô tính tay và bất biến; assert chỉ là kiểm một số yêu cầu. **Đọc lại:** BG §5 bài tập 6; LAB bài 6.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR07

**Đáp án: C.**

- A sai: nhầm tham số phân phối với thống kê chính xác của mẫu nhỏ.
- B sai: scale=5 không phải giới hạn cứng một độ lệch chuẩn quanh loc.
- C đúng: kích thước đầu ra (4,), thống kê mẫu có dao động; seed chỉ giúp tái lập trong điều kiện đã nêu.
- D sai: normal không phân phối các giá trị cố định theo hạn ngạch.

**Đối chiếu:** nhóm 6; K53; mức Bổ sung. **Kiến thức và bẫy:** normal: tham số phân phối khác thống kê chính xác của mẫu nhỏ. **Đọc lại:** NB ô 130–131: normal tự học.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-MR08

Mean=4, tổng bình phương độ lệch=4+0+4=8. ddof=0: var=8/3 USD², std=sqrt(8/3)≈1.632993 USD. ddof=1: var=8/2=4 USD², std=2 USD. Hai cách dùng mẫu số/quy ước khác nhau chứ không mâu thuẫn; lời gọi mặc định NumPy dùng ddof=0. Không yêu cầu chứng minh tính không chệch hay thuộc quy ước ngoài phần đã cho.

**Hướng dẫn chấm:** 2 điểm: tổng bình phương và mẫu số 0,5; bốn kết quả 1 điểm; đơn vị và giải thích 0,5. Với giá trị làm tròn nhận sai số tuyệt đối 5e-7.

**Đối chiếu:** nhóm 6; K54, K41; mức Bổ sung. **Kiến thức và bẫy:** ddof=1 với công thức và quy ước được cung cấp; Var/std ddof=0, đơn vị; cùng mean khác phân tán. **Đọc lại:** BG §5 ghi chú ddof=1; bổ sung theo yêu cầu, cung cấp công thức.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### Cập nhật độ bao phủ sau đợt 4

Đã dùng 44/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K10, K11, K20, K21, K22, K27, K35, K45, K46, K55, K56. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 5

### A. Câu trọng tâm

#### B3-041

**Đáp án: A.**

- A đúng: 6*4 và 6*8 byte; độ chính xác hữu hạn của cả hai kiểu.
- B sai: định dạng in không quyết định số byte phần tử.
- C sai: không có bảo đảm cố định 7 vị trí sau dấu chấm cho mọi độ lớn.
- D sai: 1/3 là ví dụ cả hai kiểu chỉ lưu gần đúng.

**Đối chiếu:** nhóm 1; K05; mức Nền tảng. **Kiến thức và bẫy:** float32/64: bộ nhớ, gần đúng, chữ số in không tăng độ chính xác. **Đọc lại:** BG §1 float32/64; NB ô 12–13.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-042

**Đáp án: D.**

- A sai: SIMD xử lý nhiều dữ liệu trên lệnh máy, một luồng/một lõi vẫn dùng được.
- B sai: không có cam kết mọi phép NumPy dùng nhiều luồng.
- C sai: phép nhân từng phần tử thông thường không đồng nhất với gọi BLAS nhân ma trận.
- D đúng: phân biệt ba cơ chế; không khẳng định mọi dtype, layout, độ dài đều dùng SIMD hoặc luôn nhanh hơn.

**Đối chiếu:** nhóm 2; K10, K08; mức Vận dụng. **Kiến thức và bẫy:** SIMD khác nhiều luồng; ufunc và nhân ma trận qua BLAS; không cam kết mọi phép đều nhanh; Vòng lặp thư viện biên dịch sẵn, dtype chọn cách đọc/tính; for Python vẫn còn chi phí. **Đọc lại:** BG §2 SIMD/luồng; NB ô 31–32; DS2 câu 8.

**Kiểm chứng:** Đã kiểm bằng suy luận; không có code cần thực thi. Không đo hiệu năng thực tế.

#### B3-043

**Đáp án: B.**

- A sai: transpose 1D không tự tạo chiều mới.
- B đúng: a vẫn một chiều; b là một hàng 2D; c thêm chiều cột dài 1.
- C sai: đảo chiều thêm vào và coi T tạo hàng.
- D sai: bỏ qua metadata mới do reshape và None. Cả ba ở ví dụ này dùng chung dữ liệu với x.

**Đối chiếu:** nhóm 3; K21, K15; mức Vận dụng. **Kiến thức và bẫy:** Shape (n,), (1,n), (n,1); transpose 1D không tạo cột; Transpose đổi shape/strides; T[i,j] ánh xạ A[j,i]. **Đọc lại:** BG §4; NB ô 91–96; cơ chế transpose §3.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-044

**Đáp án: C.**

- A sai: tưởng ix_ cũng ghép cặp để q còn một chiều; khi đó q[1,0] không hợp lệ.
- B sai: xác định shape đúng nhưng nhầm q[1,0] với ô A[2,2] thay A[2,1].
- C đúng: p=[3,17], q=[[3,5],[15,17]]; q[1,0] là A[2,1]=15.
- D sai: tưởng hai danh sách chỉ mục tự lấy mọi giao điểm cho p. Cả hai khi đọc đều không dùng chung dữ liệu A.

**Đối chiếu:** nhóm 4; K26; mức Vận dụng. **Kiến thức và bẫy:** Hai mảng chỉ mục ghép từng cặp; ix_ chọn tích hàng × cột. **Đọc lại:** BG §3; LAB bài 4; AI5 câu 14.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-045

**Đáp án: A.**

- A đúng: (2,3)+(2,1)→(2,3), R[i,j]=A[i,j]+A[i,0]. Có thể dùng A[:,0][:,None] hay np.newaxis.
- B sai: A[:,0] shape (2,), chiều cuối không khớp 3.
- C sai: (3,) cộng theo cột các số của hàng đầu; chạy được nhưng không đúng ý nghĩa.
- D sai: thêm chiều thành (1,2) vẫn không khớp chiều cuối.

**Đối chiếu:** nhóm 5; K35, K12, K34; mức Vận dụng. **Kiến thức và bẫy:** Thêm chiều bằng None/newaxis/reshape; A[:,0] khác A[:,0:1]; Chỉ mục hàng/cột, chỉ mục âm; chỉ mục nguyên bỏ chiều, slicing giữ chiều; Hệ số riêng theo cột, theo hàng, kết hợp cả hai. **Đọc lại:** BG §4 giữ cột; NB ô 95–96.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-046

**Đáp án: D.**

- A sai: không hoàn lại là quy tắc theo vị trí, không khử trùng giá trị.
- B sai: đảo quy tắc vị trí/giá trị.
- C sai: không thể chọn 5 vị trí khác nhau từ 4, lời gọi sẽ gây ValueError.
- D đúng: ví dụ chỉ mục [0,1,2] cho [40,40,70] mà vẫn không lặp vị trí.

**Đối chiếu:** nhóm 6; K44, K43; mức Nền tảng. **Kiến thức và bẫy:** replace=False không trùng vị trí nhưng giá trị có thể trùng; giới hạn size; default_rng, choice, size; lấy mẫu chỉ mục giữ các cột cùng bản ghi. **Đọc lại:** BG §5 lấy mẫu; LAB bài 8.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-047

c tái lập a vì cùng seed và cùng lời gọi đầu tiên trên bộ sinh mới. Lời gọi tạo b dùng trạng thái tiếp theo của rng, không tự khởi tạo lại seed. Không thể cam kết hai mẫu hữu hạn bắt buộc khác nhau: chúng có thể tình cờ giống. Mỗi mảng có shape (3,), chỉ mục trong 0..7 và không lặp trong chính lần gọi; hai lần gọi vẫn có thể chung vị trí. Seed không bảo đảm tính đại diện hay mean mẫu bằng mean toàn bộ.

**Hướng dẫn chấm:** 2 điểm: c=a và lý do 0,75; trạng thái tiếp theo 0,5; không cam kết khác/đại diện/mean 0,5; không lặp trong mỗi lần gọi khác không lặp giữa hai lần 0,25.

**Đối chiếu:** nhóm 6; K45; mức Vận dụng. **Kiến thức và bẫy:** Seed tái lập theo môi trường/thứ tự gọi; gọi tiếp khác khởi tạo lại; không bảo đảm đại diện/khác mẫu. **Đọc lại:** BG §5 seed; NB ô 128–129; LAB bài 8.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-048

V đọc [0,2,4,6,8,10] với bước đều 8 byte; R dùng chung A và R[1,1]↔A[2,0], ban đầu là 8, nay 50. A[2] cuối [50,9,10,11]. S đọc [1,2,5,6,9,10] theo C-order, bước 4 rồi 12 byte xen kẽ nên reshape này copy so với A; S[0,0]=90 không sửa A[0,1] (vẫn 1). Quan hệ shares_memory(A,R)=True, shares_memory(A,S)=False. Cả V và lát cắt A[:,1:3] đều không C-contiguous, nhưng điều đó một mình không quyết định có copy.

**Hướng dẫn chấm:** 2 điểm: hàng A và ánh xạ 0,75; hai quan hệ và tác động S 0,5; giải thích bước đều/không đều, không suy quá mức 0,75.

**Đối chiếu:** nhóm 3; K17, K32; mức Phân loại. **Kiến thức và bẫy:** Reshape mảng không liên tục có thể view hoặc copy; kiểm shares_memory và ô bị sửa; B=A, copy, basic view, advanced copy; giá trị bằng nhau khác shares_memory. **Đọc lại:** BG §3 reshape; DS1 câu 14; AI2 câu 2.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-049

A=[20,4,6,8]; C=[2,40,6,8]. B chính là cùng đối tượng ndarray A, dùng chung toàn bộ dữ liệu nên B[0] sửa A[0]. C là copy độc lập với A, dù ngay sau khi tạo có giá trị bằng A. V là view của C; V[0]↔C[1], không sửa A[1]. Shares_memory lần lượt True,False,True. Giá trị bằng nhau chỉ kiểm nội dung, không quyết định dùng chung; có thể đối chiếu bằng array_equal và shares_memory riêng.

**Hướng dẫn chấm:** 2 điểm: A/C 0,75; alias/copy/view và ánh xạ 0,75; bằng giá trị không suy ra dùng chung 0,5.

**Đối chiếu:** nhóm 4; K32; mức Vận dụng. **Kiến thức và bẫy:** B=A, copy, basic view, advanced copy; giá trị bằng nhau khác shares_memory. **Đọc lại:** BG §3; LAB bài 3.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-050

(a) Đều chạy qua. Mẫu số (2,1)=[[8],[12]], P=[[1/4,3/4],[1/2,1/2]] là tỷ trọng các tuần bên trong từng cửa hàng; mỗi hàng tổng 1 nên toàn mảng tổng 2. (b) `P=D/D.sum(axis=0,keepdims=True)`; cũng nhận `D/D.sum(axis=0)`. (c) Tổng theo tuần (1,2)=[[8,12]], P=[[1/4,1/2],[3/4,1/2]], shape (2,2), float64. P[i,j]=D[i,j]/sum(D[:,j]), so các cửa hàng trong tuần j. Kiểm `np.allclose(P.sum(axis=0),1,rtol=0,atol=1e-12)` và tính tay 6/(2+6)=3/4. Cả hai cách đều có tổng toàn mảng 2 nên assert đó không phân biệt đúng ý nghĩa.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm trạng thái/ý nghĩa; (b) 1 điểm sửa đúng theo tuần; (c) 1 điểm kết quả/kiểm cột và giới hạn assert.

**Đối chiếu:** nhóm 5; K38, K39, K36; mức Phân loại. **Kiến thức và bẫy:** Chia cho tổng hàng/cột: shape, mẫu số và ý nghĩa khác nhau; Kiểm chứng ý nghĩa bằng ô tính tay và bất biến; assert chỉ là kiểm một số yêu cầu; Axis là chiều gộp; tập phần tử, mẫu số; shape sum/mean có/không keepdims. **Đọc lại:** BG §4–5; GK câu 21 (biến thể đổi tập đối tượng).

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR09

**Đáp án: D.**

- A sai: giá trị/thứ tự đúng nhưng đọc advanced indexing tạo copy.
- B sai: stop=1 không được lấy, chỉ chọn 5,3.
- C sai: -1 được chuẩn hoá là chỉ mục 5, nên start và stop trùng nhau với bước âm, kết quả rỗng.
- D đúng: chọn 5,3,1, view stride −8 byte; ô đầu ở x[5], không phải địa chỉ âm.

**Đối chiếu:** nhóm 3; K56, K32; mức Bổ sung. **Kiến thức và bẫy:** Bước cắt âm, thứ tự duyệt, stride âm, offset từ gốc không phải địa chỉ âm; B=A, copy, basic view, advanced copy; giá trị bằng nhau khác shares_memory. **Đọc lại:** NB ô 84–85: lát cắt ngược đọc thêm; AI5 câu 5.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-MR10

Lát cắt A[1:,::-2] chọn hàng 1,2 và cột 3,1: [[7,5],[11,9]], strides (16,−8). Tạo V=[[7,11],[5,9]], strides (−8,16); đảo hàng V tạo W=[[5,9],[7,11]], shape (2,2), strides (8,16), ô đầu A[1,1] offset 20. W[0,1]↔A[2,1], offset 20+0*8+1*16=36, đổi 9 thành 99. Tất cả V,W dùng chung A. Stride âm là bước dịch so với ô đầu view nằm ở vị trí phù hợp trong dữ liệu A; không phải một địa chỉ tuyệt đối âm. Đảo tiếp chiều âm có thể tạo stride dương như W.

**Hướng dẫn chấm:** 2 điểm: shape/strides/offset đầu 0,75; ô và offset bị sửa 0,75; dùng chung và giải thích dấu stride 0,5.

**Đối chiếu:** nhóm 3; K56, K14, K15; mức Bổ sung. **Kiến thức và bẫy:** Bước cắt âm, thứ tự duyệt, stride âm, offset từ gốc không phải địa chỉ âm; Offset từ đầu view khác đầu gốc; ánh xạ phép gán qua view; Transpose đổi shape/strides; T[i,j] ánh xạ A[j,i]. **Đọc lại:** NB ô 84–85 đọc thêm; AI1 câu 2; DS2 câu 10.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### Cập nhật độ bao phủ sau đợt 5

Đã dùng 49/56 mục tiêu trong yêu cầu trả lời. Còn thiếu: K06, K11, K20, K22, K27, K46, K55. Các mục này được bố trí ở đợt tiếp theo theo danh mục.

## Đợt 6

### A. Câu trọng tâm

#### B3-051

**Đáp án: B.**

- A sai: bỏ qua tolerance đã chỉ định, có thể đã áp rtol mặc định thay rtol=0.
- B đúng: sai lệch thứ nhất khoảng 1e-9 trong ngưỡng, thứ hai khoảng 1e-7 ngoài ngưỡng; allclose cần mọi cặp gần nhau.
- C sai: dùng so sánh bằng tuyệt đối thay so gần đúng.
- D sai: hiểu allclose như chỉ cần ít nhất một cặp gần nhau.

**Đối chiếu:** nhóm 1; K06; mức Vận dụng. **Kiến thức và bẫy:** So sánh số thực với isclose/allclose và tolerance cho trước. **Đọc lại:** NB ô 18–19; LAB bài 6 assert_allclose.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-052

**Đáp án: A.**

- A đúng: tách chuẩn bị dữ liệu, kiểm tính tương đương, giảm nhiễu và tránh kết luận vượt phạm vi đo.
- B sai: hai phần đo chứa công việc khác nhau; tốc độ không chứng minh đúng kết quả.
- C sai: vòng for vẫn chạy trong Python; thời gian không tự chứng minh số luồng hay SIMD.
- D sai: hiệu năng phụ thuộc môi trường, kích thước, cấu hình và chi phí gọi; không có tỷ lệ cần học thuộc.

**Đối chiếu:** nhóm 2; K11, K08; mức Vận dụng. **Kiến thức và bẫy:** Benchmark tương đương kết quả, chuẩn bị ngoài đo, lặp đo và giới hạn kết luận; Vòng lặp thư viện biên dịch sẵn, dtype chọn cách đọc/tính; for Python vẫn còn chi phí. **Đọc lại:** NB ô 33–35; LAB bài 7; BG kiểm chứng AI.

**Kiểm chứng:** Đã kiểm bằng suy luận; không có code cần thực thi. Không đo hiệu năng thực tế.

#### B3-053

**Đáp án: C.**

- A sai: reshape không tự đệm dữ liệu.
- B sai: thay metadata vẫn phải giữ số phần tử.
- C đúng: 2*4≠6, ngoại lệ dừng trước dòng print; x không bị sửa.
- D sai: đây là ngoại lệ, không phải cảnh báo có thể chạy tiếp bình thường.

**Đối chiếu:** nhóm 3; K22, K16; mức Nền tảng. **Kiến thức và bẫy:** Reshape sai số phần tử gây ngoại lệ; khác cảnh báo và không tự cắt/đệm; Reshape C-order giữ thứ tự đọc và số phần tử; khác transpose. **Đọc lại:** BG §3 reshape giữ số phần tử.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-054

**Đáp án: D.**

- A sai: tự khử chỉ mục trùng, làm mất một lần đọc A[2,1].
- B sai: lấy tích hàng × cột như ix_ thay ghép từng cặp.
- C sai: tự sắp xếp giá trị trong khi chỉ mục phải giữ thứ tự đã cho.
- D đúng: cặp (2,1),(0,2),(2,1), nên số 8 tham gia hai lần; p.sum()=19. Đọc nâng cao tạo copy.

**Đối chiếu:** nhóm 4; K27, K26; mức Vận dụng. **Kiến thức và bẫy:** Chỉ mục đọc lặp/đổi thứ tự; số lần tham gia tổng; Hai mảng chỉ mục ghép từng cặp; ix_ chọn tích hàng × cột. **Đọc lại:** BG §3 lặp chỉ mục; NB ô 76–77; AI1 câu 1.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-055

**Đáp án: B.**

- A sai: bỏ qua keepdims=True.
- B đúng: gộp hai hàng ở từng cột; s[0,j]=A[0,j]+A[1,j], giữ chiều hàng bằng 1.
- C sai: gộp cột theo axis=1 thay vì axis=0.
- D sai: tổng toàn mảng thay tổng theo cột. Dtype của phép sum không được hỏi vì có thể phụ thuộc kiểu tích luỹ mặc định của môi trường.

**Đối chiếu:** nhóm 5; K36; mức Nền tảng. **Kiến thức và bẫy:** Axis là chiều gộp; tập phần tử, mẫu số; shape sum/mean có/không keepdims. **Đọc lại:** BG §5 axis/keepdims; NB ô 106–109.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-056

**Đáp án: C.**

- A sai: tái lập không bảo đảm mean hay tính đại diện.
- B sai: đảo vai trò seed và replace=False.
- C đúng: tái lập có điều kiện; không có ràng buộc ánh xạ một-một từ seed tới mọi mẫu hữu hạn.
- D sai: cả tính khác nhau lẫn đại diện đều không được bảo đảm. Ví dụ chọn hết hai vị trí rồi xét tập vị trí thì mọi seed đều cho cùng tập.

**Đối chiếu:** nhóm 6; K45, K44; mức Vận dụng. **Kiến thức và bẫy:** Seed tái lập theo môi trường/thứ tự gọi; gọi tiếp khác khởi tạo lại; không bảo đảm đại diện/khác mẫu; replace=False không trùng vị trí nhưng giá trị có thể trùng; giới hạn size. **Đọc lại:** BG §5 seed; NB ô 114–117; AI1 câu 6.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-057

Mean toàn bộ=(10+20+30+140)/4=50 USD/đêm; mẫu hiện tại [10,20] có mean=15. Báo cáo trung bình của toàn bộ bằng `gia.mean()` (50), không thay bằng mẫu thuận ý; thử seed đến khi có kết quả thấp làm lựa chọn thiên lệch. Mẫu hữu ích để đọc/kiểm tra từng bản ghi khi bảng lớn, không cần thiết để thay phép tính chính xác đã làm được trên cả dữ liệu hợp lệ. Giá 140 đã được xác nhận hợp lệ; cao hơn các giá khác không tự chứng minh sai để xoá. Nếu muốn mô tả mức điển hình bằng median thì phải nói rõ đó là đại lượng khác, không đổi tên thành mean.

**Hướng dẫn chấm:** 2 điểm: hai mean 0,5; lệnh và tập dữ liệu/mẫu số đúng 0,5; phê bình chọn seed 0,5; vai trò mẫu và giữ giá hợp lệ 0,5.

**Đối chiếu:** nhóm 6; K46, K40, K45; mức Vận dụng. **Kiến thức và bẫy:** Thống kê toàn bộ dữ liệu hợp lệ khi có thể; mẫu để đọc kiểm tra, tránh chọn seed thuận ý; Mean, median, min/max, sum; giá cực lớn và mức giá điển hình; Seed tái lập theo môi trường/thứ tự gọi; gọi tiếp khác khởi tạo lại; không bảo đảm đại diện/khác mẫu. **Đọc lại:** BG §5 diễn giải mẫu; LAB bài 8; AI2 câu 3.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-058

Không thể là view ndarray thông thường như yêu cầu. Các ô đầu hàng bắt đầu ở offset 0,16,36 byte từ đầu A; hai bước hàng 16 và 20 khác nhau, trong khi một stride hàng phải cố định. Dù trong mỗi hàng hai ô cách 8 byte, điều đó chưa đủ. Một biểu thức đúng: `B=A.reshape(-1,order='C')[[0,2,4,6,9,11]].reshape(3,2,order='C')`. Kết quả [[0,2],[4,6],[9,11]], int32, không dùng chung A vì bước đọc bằng list chỉ mục tạo copy; reshape sau chỉ tổ chức bản sao đó. Không dùng as_strided để ép một bố trí không phù hợp.

**Hướng dẫn chấm:** 2 điểm: offset/bước và kết luận không view 1 điểm; biểu thức đúng 0,75; giải thích copy/shape 0,25. Nhận các biểu thức chỉ mục nâng cao tương đương, hoặc ghép các lát cắt bằng API đã học nếu tạo đúng bản sao.

**Đối chiếu:** nhóm 3; K20, K16, K32; mức Phân loại. **Kiến thức và bẫy:** Điều kiện bước byte cố định để bố trí yêu cầu có thể là view; Reshape C-order giữ thứ tự đọc và số phần tử; khác transpose; B=A, copy, basic view, advanced copy; giá trị bằng nhau khác shares_memory. **Đọc lại:** BG §3 strides; AI1 câu 14 (biến thể bố trí và tạo bản sao).

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-059

y là basic view, y[0]↔x[1], y[1]↔x[3], stride 8 byte; shares_memory True. Sửa y thành 0 làm x=[3,0,5,0]. m vẫn [False,True,False,True], không tính lại; gán x[m]=1 làm x=[3,1,5,1] và y nhìn thấy [1,1]. Hai tổng 10 và 2. Dù giá trị x ở các vị trí đó đã dưới 8, mask cũ vẫn chọn chúng.

**Hướng dẫn chấm:** 2 điểm: x/y và hai tổng 0,75; view/ánh xạ/strides 0,75; mask không tính lại và tác động gán 0,5.

**Đối chiếu:** nhóm 4; K32, K25, K31; mức Vận dụng. **Kiến thức và bẫy:** B=A, copy, basic view, advanced copy; giá trị bằng nhau khác shares_memory; Đọc A[mask] là copy; gán A[mask]=... sửa đích; Mask đã tính không tự tính lại khi mảng số bị sửa. **Đọc lại:** BG §3 view/copy, mask đọc/gán.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-060

(a) Assert qua: đảo cột vẫn giữ mean từng hàng bằng 0. Nhưng Z hiện tại [[2,−2],[2,−2]] đã gán chênh lệch kỳ 2 sang vị trí kỳ 1, sai yêu cầu thứ tự. (b) `Z=P-P.mean(axis=1,keepdims=True)`, bỏ bước chọn [1,0]. Shape (2,2) trừ (2,1) cho (2,2), float64; Z[i,j]=P[i,j]−mean(P[i,:]), giữ j. (c) Đúng là [[−2,2],[−2,2]]. Kiểm ô đầu 2−4=−2, hoặc `np.allclose(Z, np.array([[-2.,2.],[-2.,2.]]),rtol=0,atol=1e-12)`. Bất biến mean hàng là điều kiện cần trong ví dụ, không đủ chứng minh đúng ánh xạ cột. Bước advanced indexing đọc tạo dữ liệu mới và đổi thứ tự; copy không tự bảo đảm đúng ý nghĩa.

**Hướng dẫn chấm:** 3 điểm: (a) 1 điểm nhận assert qua nhưng sai thứ tự; (b) 1 điểm sửa đúng; (c) 1 điểm gồm giá trị/ánh xạ và kiểm tra phân biệt được đảo cột. Không trừ điểm cách kiểm tương đương.

**Đối chiếu:** nhóm 5; K39, K37, K27; mức Phân loại. **Kiến thức và bẫy:** Kiểm chứng ý nghĩa bằng ô tính tay và bất biến; assert chỉ là kiểm một số yêu cầu; Trừ trung bình chính hàng; ma trận chữ nhật báo lỗi, ma trận vuông che lỗi; Chỉ mục đọc lặp/đổi thứ tự; số lần tham gia tổng. **Đọc lại:** BG kiểm chứng AI; LAB bài 6; BG §3 đổi thứ tự chỉ mục.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### B. Tự học bổ sung — mức ưu tiên thấp hơn

#### B3-MR11

**Đáp án: B.**

- A sai: bỏ dấu âm, dùng bit dấu cho số dương.
- B đúng: âm nên dấu 1, E=3+127=130, bỏ bit 1 ngầm và lưu 101 rồi 20 bit 0. Tổng trường bit 1+8+23=32.
- C sai: lưu số mũ thật thay số mũ đã cộng bias.
- D sai: lưu cả bit 1 trước dấu chấm vào phần trị 23 bit. Không yêu cầu trường hợp NaN, vô cực hay số dưới chuẩn.

**Đối chiếu:** nhóm 1; K55; mức Bổ sung. **Kiến thức và bẫy:** float32: dấu, số mũ bias 127, 23 bit phần trị và số chuẩn hoá. **Đọc lại:** NB ô 123–124: Đọc thêm, không yêu cầu trên lớp.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

#### B3-MR12

R=[[2,3,4],[2,3,4]], shape (2,3), dtype int32, nbytes=24. Các cặp shares_memory lần lượt True,False,False. V có strides (0,4), nbytes=24 nhưng dùng lại b.nbytes=12, không có bản sao vật lý cho từng hàng. Ngược lại R do phép cộng thông thường tạo ra cần vùng dữ liệu riêng 24 byte cho 6 giá trị; hai phát biểu nói về toán hạng và đầu ra nên không mâu thuẫn. R[i,j]=A[i,j]+b[j], không cần gọi broadcast_to trước A+b. Kiểm bằng assert_array_equal cho R và shares_memory cho từng cặp; sửa b sau đó đổi V nhưng không tự tính lại R. Không lấy nbytes của V làm số byte cấp phát mới.

**Hướng dẫn chấm:** 2 điểm: R/thuộc tính 0,5; ba quan hệ 0,5; phân biệt toán hạng/kết quả và byte 0,75; kiểm chứng phù hợp 0,25.

**Đối chiếu:** nhóm 5; K50, K48, K19; mức Bổ sung. **Kiến thức và bẫy:** broadcast_to: stride 0, chia sẻ, chỉ đọc; broadcasting không sao toán hạng nhưng phép cộng tạo kết quả; Một biểu thức có thể tạo nhiều mảng tạm và nhiều lượt đọc/ghi; nbytes của view khác khoảng byte bao trùm và lượng dữ liệu mới cấp phát. **Đọc lại:** NB ô 40,119–120: mảng tạm, stride 0 đọc thêm.

**Kiểm chứng:** Đã thực thi kiểm chứng bằng NumPy 2.3.5; các assert liên quan đều đạt.

### Cập nhật độ bao phủ sau đợt 6

Đã dùng 56/56 mục tiêu trong yêu cầu trả lời. Không còn mục tiêu thiếu trong phạm vi đã xác định.

## Cặp đối chiếu và bảng kiểm bẫy

- **B3-034/B3-059:** cùng dữ liệu và phần tử dự định sửa, chỉ khác mask/list chỉ mục và slicing khi đọc: copy khác view.
- **B3-010/B3-040:** hình chữ nhật làm lộ lỗi shape; ma trận vuông vẫn chạy nhưng sai phép trừ.
- **B3-018/B3-048:** hai cách cắt không liên tục nhưng một cách reshape giữ view, cách còn lại phải copy.
- **B3-029/B3-019:** gán trực tiếp qua ix_ khác chọn nâng cao trước rồi gán qua mảng tạm.

| Bẫy bắt buộc | Các biến thể đánh giá |
| --- | --- |
| itemsize / nbytes | 001,006,028 |
| nbytes / khoảng bao trùm / cấp phát | 028,MR04,MR12 |
| Đổi dtype sau khi tràn | 016,031 |
| Chữ số in / độ chính xác | 021,041,MR03 |
| Bỏ vòng lặp / luôn nhiều lõi | 002,022,042,052 |
| Kết hợp view/copy | 009,018,019,038,048,049,059 |
| Advanced copy / gán trực tiếp | 019,029,034 |
| Ghép cặp / tích hàng × cột | 029,044,054 |
| Quên offset / dấu stride | 008,028,MR09,MR10 |
| Reshape luôn view / luôn copy | 018,038,048 |
| Broadcast hàng / cột | 015,025,035,045 |
| Axis / giữ chiều | 010,020,030,040,055 |
| Ma trận vuông che sai nghĩa | 030,040,050,060 |
| Mask cũ tự tính lại | 039,059 |
| Seed / đại diện; vị trí / giá trị trùng | 037,046,047,056,057 |
## Đối chiếu cuối bộ

- Đủ B3-001–B3-060: **60 câu**, **40 TN + 20 TL**; nhóm chính lần lượt **8/6/12/12/12/10**.
- Đủ B3-MR01–B3-MR12: **12 câu**, **8 TN + 4 TL**, đặt riêng ở từng đợt.
- Độ khó thiết kế phần trọng tâm: **15 nền tảng + 33 vận dụng + 12 phân loại**. Không coi đây là xác suất câu thật hoặc độ khó đo từ dữ liệu thi.
- Cả **56/56 mục tiêu** được dùng trong đề bài/lựa chọn cần đánh giá, không tính mục chỉ tình cờ nhắc trong lời giải. Các câu sửa code (a)–(b)–(c): **B3-010, B3-019, B3-030, B3-040, B3-050, B3-060**.
- Phạm vi tài liệu: đầy đủ mục bắt buộc trong ba nguồn Bài 3, gồm bài lab, kiểm chứng AI và mục tự học xác định. Phạm vi sách/website liên kết không được tuyên bố bao phủ toàn bộ. Mức ưu tiên lấy GK làm chuẩn; một số cơ chế tuần 3 dùng cho phân loại. `.base`, mảng tạm, stride âm, stride 0, phân vị, sinh số và bit float32 giữ ở phần bổ sung như nguồn.
- Rà trùng ý: có cặp đối chiếu có chủ đích để phân biệt cơ chế; câu khác dùng thay đổi về thao tác, hình dạng, đối tượng tổng hợp hoặc yêu cầu kiểm chứng, không chỉ đổi số/tên biến từ đề gốc. Không đặt cặp hoặc nhãn bẫy cạnh câu hỏi.

Phân bố đáp án trọng tâm: {'A': 10, 'B': 10, 'C': 10, 'D': 10}; bổ sung: {'A': 2, 'B': 2, 'C': 2, 'D': 2}.

Đã thực thi 66/72 câu có ca code kiểm chứng trên NumPy 2.3.5. 6 câu thuần cơ chế/thiết kế đo được kiểm bằng suy luận; không tuyên bố đo benchmark hoặc kiểm mọi cấu hình SIMD/BLAS. Với bộ nhớ dùng `np.shares_memory` trực tiếp; số nguyên dùng `assert_array_equal`, số thực dùng `assert_allclose` hoặc assert chính xác khi số biểu diễn được.

## Dấu vết độ bao phủ cuối

| Mục tiêu | Câu thực sự dùng |
| --- | --- |
| K01 | B3-001 |
| K02 | B3-011 |
| K03 | B3-006 |
| K04 | B3-016, B3-031 |
| K05 | B3-MR03, B3-021, B3-041 |
| K06 | B3-051 |
| K07 | B3-002, B3-012, B3-022 |
| K08 | B3-022, B3-042, B3-052 |
| K09 | B3-032 |
| K10 | B3-042 |
| K11 | B3-052 |
| K12 | B3-003, B3-045 |
| K13 | B3-008, B3-013 |
| K14 | B3-008, B3-MR10 |
| K15 | B3-019, B3-023, B3-028, B3-033, B3-038, B3-043, B3-MR10 |
| K16 | B3-033, B3-053, B3-058 |
| K17 | B3-018, B3-048 |
| K18 | B3-038 |
| K19 | B3-MR04, B3-028, B3-MR12 |
| K20 | B3-058 |
| K21 | B3-043 |
| K22 | B3-053 |
| K23 | B3-004, B3-014 |
| K24 | B3-024, B3-027 |
| K25 | B3-034, B3-039, B3-059 |
| K26 | B3-029, B3-044, B3-054 |
| K27 | B3-054, B3-060 |
| K28 | B3-019 |
| K29 | B3-009 |
| K30 | B3-019, B3-029 |
| K31 | B3-039, B3-059 |
| K32 | B3-009, B3-039, B3-048, B3-049, B3-MR09, B3-058, B3-059 |
| K33 | B3-005, B3-015, B3-025, B3-035 |
| K34 | B3-015, B3-025, B3-035, B3-045 |
| K35 | B3-045 |
| K36 | B3-010, B3-020, B3-050, B3-055 |
| K37 | B3-010, B3-040, B3-060 |
| K38 | B3-030, B3-050 |
| K39 | B3-010, B3-030, B3-040, B3-050, B3-060 |
| K40 | B3-007, B3-017, B3-057 |
| K41 | B3-026, B3-036, B3-MR08 |
| K42 | B3-027 |
| K43 | B3-037, B3-046 |
| K44 | B3-037, B3-046, B3-056 |
| K45 | B3-047, B3-056, B3-057 |
| K46 | B3-057 |
| K47 | B3-MR01 |
| K48 | B3-MR02, B3-MR12 |
| K49 | B3-MR03 |
| K50 | B3-MR04, B3-MR12 |
| K51 | B3-MR05 |
| K52 | B3-MR06 |
| K53 | B3-MR07 |
| K54 | B3-MR08 |
| K55 | B3-MR11 |
| K56 | B3-MR09, B3-MR10 |
