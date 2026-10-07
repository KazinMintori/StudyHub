# D. Ràng buộc chặt và điều kiện dừng

Xét bài toán

\[
\min_{x\in\mathbb R}x^2\qquad\text{với }-x\le0.
\]

Ràng buộc \(-x\le0\) tương đương \(x\ge0\): nhân hai vế với \(-1\) thì phải đổi chiều bất đẳng thức. Những số thực không âm là các điểm khả thi của bài toán.

Nguồn nói ràng buộc là *active* tại \(x=0\). Ta gọi đó là **ràng buộc chặt tại \(x=0\)**: khi thế điểm này vào, bất đẳng thức trở thành đẳng thức \(-0=0\). Chẳng hạn, tại \(x=1\), ta có \(-1<0\), nên ràng buộc vẫn được thỏa nhưng không chặt. Trường hợp \(x=1\) là ví dụ bổ sung để phân biệt hai trạng thái.

Nguồn cho **phương trình của điều kiện dừng**

\[
2x-\lambda=0,\qquad\lambda\ge0.
\]

Ký hiệu \(\lambda\) là nhân tử gắn với ràng buộc \(-x\le0\); theo quy ước của đoạn nguồn, nhân tử này phải không âm. Để giải thích dấu trừ trong phương trình, ta ghép hàm mục tiêu với ràng buộc qua nhân tử đó thành hàm Lagrange:

\[
L(x,\lambda)=x^2+\lambda(-x)=x^2-\lambda x.
\]

Lấy đạo hàm theo \(x\), coi \(\lambda\) là hằng số, cho \(\frac{\partial L}{\partial x}=2x-\lambda\). Điều kiện dừng đặt đạo hàm này bằng 0. Đây là phần giải thích bổ sung cho phương trình trong nguồn.

Tại \(x=0\), phương trình trở thành \(-\lambda=0\), nên **\(\lambda=0\)**. Giá trị này thỏa \(\lambda\ge0\). Như vậy, ràng buộc chặt tại một điểm không buộc nhân tử của nó phải dương: trong chính ví dụ này, ràng buộc chặt nhưng nhân tử bằng 0.

Có thể kiểm tra tối ưu trực tiếp mà không chỉ dựa vào điều kiện dừng: với mọi điểm khả thi \(x\ge0\), ta có \(x^2\ge0\), còn tại \(x=0\) giá trị mục tiêu bằng 0. Vì không có điểm khả thi nào cho giá trị nhỏ hơn, \(x=0\) là nghiệm tối ưu toàn cục. Đây là kết luận kiểm tra thêm từ bài toán đã cho.
