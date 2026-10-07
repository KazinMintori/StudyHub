# Hàm lồi: vì sao đạo hàm bằng 0 cho cực tiểu toàn cục?

Nguồn là đoạn tự viết: “Cho f:R^n->R khả vi và lồi. Với mọi x,y, f(y)>=f(x)+grad f(x)^T(y-x). Nếu grad f(x*)=0 thì x* là cực tiểu toàn cục.” Phần diễn giải và các ví dụ dưới đây được bổ sung để giải thích nguồn.

Note được điều chỉnh theo phản hồi mô phỏng rằng thuật ngữ affine, ký hiệu norm và ví dụ hai biến gây quá tải. Đây không phải bằng chứng về kết quả học của người học thật.

## Phát biểu và cách đọc ký hiệu

Giả sử \(f:\mathbb R^n\to\mathbb R\) khả vi và lồi. Với mọi \(x,y\in\mathbb R^n\),

\[
f(y)\geq f(x)+\nabla f(x)^T(y-x).
\tag{1}
\]

Nếu \(\nabla f(x^\star)=0\), thì \(x^\star\) là điểm cực tiểu toàn cục.

\(\mathbb R\) là tập số thực; \(\mathbb R^n\) gồm các bộ có \(n\) số thực. Hàm \(f\) nhận một bộ số và trả về một số. Các chữ \(x,y\) gọi hai bộ số đầu vào; \(x^\star\) là tên một điểm đang xét, không phải phép nhân với dấu sao.

Khả vi cho phép mô tả sự thay đổi của hàm bằng đạo hàm. Gradient \(\nabla f(x)\) là bộ các đạo hàm theo từng biến tại \(x\). Để đọc số hạng \(\nabla f(x)^T(y-x)\), lấy mỗi đạo hàm nhân với độ thay đổi của biến tương ứng, rồi cộng các tích. Dấu \(T\) chỉ chuyển vị, được dùng để viết phép nhân đó. Nếu gradient bằng \(0\), mọi thành phần của nó bằng \(0\), nên số hạng này bằng \(0\).

## Hiểu bất đẳng thức qua một biến

Khi \(n=1\), gradient trở thành đạo hàm thông thường và (1) là

\[
f(y)\geq f(x)+f'(x)(y-x).
\tag{2}
\]

Đạo hàm \(f'(x)\) là độ dốc tiếp tuyến tại \(x\). Đường tiếp tuyến đi qua điểm có độ cao \(f(x)\). Tại vị trí \(y\), độ cao của đường này là \(f(x)+f'(x)(y-x)\): độ dời ngang là \(y-x\), nhân với độ dốc cho độ thay đổi theo chiều đứng.

Với một biến, tính lồi có nghĩa là đồ thị nằm không cao hơn đoạn thẳng nối hai điểm bất kỳ trên đồ thị. Bất đẳng thức (2) là hệ quả mà nguồn nêu cho hàm lồi khả vi: đường tiếp tuyến nằm dưới hoặc chạm đồ thị ở **mọi** vị trí \(y\). Quan hệ này so sánh được cả những điểm ở xa \(x\); chỉ biết hàm có đạo hàm chưa đủ để kết luận như vậy.

**Ví dụ bổ sung.** Hàm \(f(u)=u^2\) lồi và khả vi, với \(f'(u)=2u\). Chọn \(x=1\), giá trị tiếp tuyến tại \(y\) là

\[
1+2(y-1)=2y-1.
\]

Tại \(y=3\), giá trị hàm là \(9\), còn tiếp tuyến cho \(5\). Để kiểm tra quan hệ với mọi \(y\), tính hiệu:

\[
f(y)-(2y-1)=y^2-2y+1=(y-1)^2\geq0.
\]

Bình phương luôn không âm, nên \(f(y)\geq2y-1\) với mọi số thực \(y\). Ví dụ này minh họa (2); nó không thay cho chứng minh (1) với mọi hàm lồi khả vi.

## Bước suy ra cực tiểu toàn cục

Điểm \(x^\star\) là cực tiểu toàn cục khi không có đầu vào nào cho giá trị hàm nhỏ hơn \(f(x^\star)\). Để chứng minh điều đó, dùng (1) tại \(x=x^\star\):

\[
f(y)\geq f(x^\star)+\nabla f(x^\star)^T(y-x^\star).
\]

Vì \(\nabla f(x^\star)=0\), tổng các tích ở vế phải bằng \(0\). Do đó,

\[
f(y)\geq f(x^\star)\qquad\text{với mọi }y\in\mathbb R^n.
\]

Đây chính là điều cần chứng minh. Tính lồi và khả vi cho phép dùng (1); gradient bằng \(0\) làm vế phải còn \(f(x^\star)\). Chữ “toàn cục” đến từ lượng từ “với mọi \(y\)”.

Trong ví dụ \(f(u)=u^2\), chọn \(x^\star=0\): \(f'(0)=0\) và (2) trở thành \(y^2\geq0=f(0)\) với mọi \(y\). Vì thế \(0\) là điểm cực tiểu toàn cục.

Điều kiện lồi phải được giữ. Ví dụ bổ sung \(g(u)=-u^2\) có đạo hàm bằng \(0\) tại \(0\), nhưng \(g(1)=-1<g(0)=0\), nên \(0\) không phải cực tiểu. Phát biểu nguồn cũng chỉ nói **nếu** có một điểm với gradient bằng \(0\); nó không khẳng định điểm ấy luôn tồn tại hoặc cực tiểu là duy nhất.
