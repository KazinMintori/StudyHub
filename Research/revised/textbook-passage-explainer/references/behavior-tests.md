# Tình huống kiểm tra hành vi

Đây là yêu cầu và bất biến để chạy thử, không phải tuyên bố đã thử trên sinh viên. Lưu output thực, nguồn, phiên bản và lỗi. Với mỗi tình huống, đánh giá nghĩa, bước nối và giọng trong ngữ cảnh; không đối chiếu từng chữ với một đáp án cố định.

## B01 — Điểm dừng và tính lồi

Nguồn tự viết: “Cho f: R^n -> R khả vi và lồi. Với mọi x,y, f(y) >= f(x) + grad f(x)^T(y-x). Nếu grad f(x*) = 0, x* là cực tiểu toàn cục.”

Yêu cầu: giảng trong chat cho người biết đạo hàm nhưng chưa học tối ưu lồi. Giữ miền và tính khả vi; chỉ đúng bất đẳng thức dùng tính lồi và bước dùng gradient bằng 0. Nếu thêm -x^2, tính đạo hàm và chỉ kết luận đúng phạm vi phản ví dụ. Không thay lập luận bằng “tính lồi đảm bảo”.

## B02 — Chuyển thành note

Dùng cùng nguồn B01, yêu cầu note Markdown tự học. Note phải có nghĩa ký hiệu, lập luận đầy đủ và đọc được độc lập; không dùng “ở chỗ này” với đối tượng không tồn tại. So slide/note nếu có cặp, không nhét một kiểu giọng vào cả hai.

## B03 — Thuật toán và quy ước dấu

Nguồn tự viết: “Gradient descent dùng x_(k+1)=x_k-alpha_k grad f(x_k), alpha_k>0. Với ràng buộc đẳng thức h(x)=0, L(x,nu)=f(x)+nu h(x), nu không bị giới hạn dấu.”

Yêu cầu: giải thích hai đoạn, không tự nối thành thuật toán tối ưu có ràng buộc. Nếu dùng f(x)=(x-3)^2, x_0=0, alpha=1/4, bước đầu phải ra x_1=1.5. Phân biệt gradient, hướng -gradient và độ dời. Không hứa giảm/hội tụ với mọi alpha>0; không coi gradient của L bằng 0 là đủ tối ưu nếu thiếu điều kiện.

## B04 — Phản hồi có bằng chứng

Người học viết: “10 trong 40 người thuộc nhóm B cũng thuộc A, nên P(A|B)=10/100.” Phản hồi phải tìm sai mẫu số và giải thích điều kiện chọn nhóm. Không kết luận họ không biết chia; không gọi họ thành thạo chỉ vì sau đó nói “hiểu rồi”. Nếu họ muốn lời giải trực tiếp, không bắt trả lời thêm mới cho đáp án.

## B05 — Diễn giải văn bản

Nguồn tự viết: “Nhân vật khép cửa rồi đặt lá thư chưa mở dưới ngọn đèn. Đoạn văn không cho biết nội dung thư.” Yêu cầu giảng ý nghĩa chi tiết. Phải dùng chứng cứ và nêu mức chắc chắn; không bịa nội dung thư hoặc ý tác giả. Không ép định lý, công thức và phản ví dụ lên văn học.

## B06 — Nguồn thiếu / mơ hồ

Nguồn: “Chia hai vế cho x để suy ra …”, không cho dấu của x. Yêu cầu giải thích phép chia bất đẳng thức. Phải nói điều kiện thiếu, xét dấu khi cần; không đoán x>0. Trong OCR “P(B) ? 0”, không mặc định ký tự ? là > rồi ghi như nguồn chắc chắn.

## B07 — Biên tập giọng có bảo toàn nghĩa

Yêu cầu sửa câu “Bài 04 áp dụng thao tác lập mô hình và giải điều kiện dừng để tạo bước đi; phần đẳng thức dùng nu hoặc eta tự do dấu.” Nguồn không xác định bước cập nhật. Sửa giọng phải tách nhiệm vụ và giữ quy ước dấu; không khẳng định giải điều kiện dừng tự tạo hướng cập nhật. Nêu chỗ cần ngữ cảnh thay vì sửa câu gượng thành một câu tự nhiên nhưng sai.

Đạt khi không còn lỗi nghĩa/nguồn hoặc bước nối thiết yếu, giọng đúng đầu ra và phần chưa kiểm chứng được ghi đúng. Kết quả thử bằng model chưa chứng minh người học thật hiểu.

## B08 — Thuật ngữ phụ và sửa sau phản hồi

Người học chỉ biết đạo hàm. Bản giải thích thêm “hàm affine”, ký hiệu chuẩn và chứng minh ví dụ nhiều biến khiến họ phải học thêm để hiểu kết luận. Khi họ phản hồi điều đó, giảm phần phụ, dùng ví dụ một biến và nối rõ về ký hiệu tổng quát. Giữ miền R^n và lượng từ mọi y; không biến việc giảm tải thành xóa nội dung nguồn. Đây là tình huống hồi quy từ một output soạn thử, chưa phải dữ liệu lớp học.

## B09–B14 — Nghĩa chuyên ngành và bản dịch

- **B09:** nguồn EN cho T:X->X và d(Tx,Ty)≤q d(x,y) với 0≤q<1. Dùng “ánh xạ co” theo môn, giữ cùng q/mọi cặp điểm; không đổi q<1 thành q≤1. Nếu tuyên bố tồn tại điểm bất động, kiểm tra thêm các giả thiết.
- **B10:** nguồn tensor contraction có chỉ số ghép. Dùng “phép co tensor”, không thêm tính chất giảm khoảng cách. Từ contraction đứng riêng không có lĩnh vực thì giữ các nghĩa có điều kiện hoặc hỏi đúng thông tin thiếu.
- **B10b:** ví dụ trace phải nêu cặp chỉ số hợp lệ, chẳng hạn tổng A^i_i của tensor (1,1), hoặc metric/cấu trúc tương ứng. Không gọi tổng A_ii của tensor covariant tùy ý là bất biến mà chưa có điều kiện. Đây là hồi quy từ output soạn thử.
- **B11:** nguồn feasible point. Giữ “điểm khả thi”, miền và mọi ràng buộc; không đổi thành tối ưu hoặc loại từ “khả thi” để viết đời thường.
- **B12:** equality multiplier unrestricted in sign. Bản Việt phải giữ khả năng bằng 0, không áp điều kiện của nhân tử bất đẳng thức hoặc gọi giá trị được phép là nghiệm đã tìm được.
- **B13:** active constraint tại một điểm với g_i(x)=0. Không suy multiplier phải dương/khác 0; tên gọi ưu tiên glossary của môn. Hợp đồng trong câu về thỏa thuận không bị sửa thành ánh xạ co.
- **B14:** ∇f(x)^T d<0 và “sufficiently small positive steps”. Giữ “đủ nhỏ”, không giảng thành mọi bước dương. Sau khi sửa lời văn phải rà lại dấu, lượng từ và miền.

Tập ví dụ JSONL phục vụ prompting không phải đáp án vàng cho các bài kiểm tra. Đổi ký hiệu, ví dụ và cấu trúc câu khi đánh giá; không truy xuất bản Việt của chính câu kiểm tra.
