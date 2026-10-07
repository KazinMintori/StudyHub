*Lượt sửa dựa trên phản hồi mô phỏng; không phải kết quả quan sát từ người học thật.*

Tôi đã thêm thuật ngữ “affine” và ví dụ hai biến vào bản trước, khiến bạn phải học thêm để theo được lời giảng. Ta quay về một biến để hiểu điều đoạn nguồn muốn nói, rồi đọc lại ký hiệu tổng quát.

Với một biến, công thức đầu tiên trở thành

\[
f(y)\geq f(x)+f'(x)(y-x).
\]

Trong đó, \(x\) là điểm ta chọn để xét đạo hàm, còn \(y\) là điểm bất kỳ muốn so sánh. Đạo hàm \(f'(x)\) cho độ dốc của tiếp tuyến tại \(x\). Từ giá trị \(f(x)\), đi ngang một lượng \(y-x\) trên đường tiếp tuyến thì giá trị thay đổi \(f'(x)(y-x)\). Vì vậy, vế phải là độ cao của đường tiếp tuyến tại vị trí \(y\).

Hàm lồi có đồ thị nằm không cao hơn đoạn thẳng nối hai điểm bất kỳ trên đồ thị. Với hàm lồi có đạo hàm, đoạn nguồn khẳng định thêm: **tiếp tuyến nằm dưới hoặc chạm đồ thị ở mọi vị trí**. Đó là ý nghĩa của dấu \(\geq\). Chỉ có đạo hàm thì chưa đủ để bảo đảm quan hệ này trên toàn trục số.

**Ví dụ bổ sung:** Xét hàm lồi khả vi \(f(u)=u^2\), có \(f'(u)=2u\). Tại \(x=1\), tiếp tuyến cho giá trị

\[
f(1)+f'(1)(y-1)=1+2(y-1)=2y-1.
\]

Tại \(y=3\), đường tiếp tuyến cho \(5\), còn hàm cho \(9\). Với mọi \(y\), ta kiểm tra được

\[
y^2-(2y-1)=(y-1)^2\geq0.
\]

Như vậy, hàm luôn có giá trị ít nhất bằng giá trị trên tiếp tuyến.

Bây giờ chọn một điểm \(x^\star\) có đạo hàm bằng \(0\); dấu sao chỉ dùng để đặt tên điểm này. Thế vào công thức:

\[
f(y)\geq f(x^\star)+0\,(y-x^\star)=f(x^\star)
\qquad\text{với mọi }y.
\]

Không có điểm nào cho giá trị nhỏ hơn \(f(x^\star)\): đó là **cực tiểu toàn cục**. Với \(f(u)=u^2\), điểm ấy là \(0\), vì \(f'(0)=0\) và mọi \(y\) đều thỏa \(y^2\geq0=f(0)\).

Trở lại nguồn: \(\mathbb R^n\) là tập các bộ gồm \(n\) số thực; \(f:\mathbb R^n\to\mathbb R\) nhận một bộ như vậy và trả về một số. Gradient \(\nabla f(x)\) gom các đạo hàm theo từng biến tại \(x\). Biểu thức \(\nabla f(x)^T(y-x)\) có nghĩa là nhân từng đạo hàm với độ thay đổi của biến tương ứng, rồi cộng lại; dấu \(T\) là ký hiệu chuyển vị dùng trong cách viết phép tính này. Khi gradient bằng \(0\), mọi đạo hàm trong bộ đều bằng \(0\), nên tổng đó bằng \(0\). Vì thế, lập luận vẫn cho \(f(y)\geq f(x^\star)\) với mọi \(y\in\mathbb R^n\).

Ta cần giữ cả hai điều kiện **khả vi và lồi**. Ví dụ bổ sung \(g(u)=-u^2\) có \(g'(0)=0\), nhưng \(g(1)=-1<g(0)=0\); riêng đạo hàm bằng \(0\) chưa đủ.

Note đã chỉnh để đọc độc lập: [06-revised-study-note.md](/C:/Users/Ai/Documents/StudyHub/Research/evaluation/notes-forward/06-revised-study-note.md).
