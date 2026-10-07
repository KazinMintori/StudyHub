# B. Phép co tensor — lượt sửa sau review

**Dịch:** “Phép co tensor lấy tổng theo một cặp chỉ số được ghép tương ứng đã chỉ định.”

Một tensor có các thành phần được xác định bằng chỉ số. Trong phép co, ta cho hai chỉ số đã chọn nhận cùng giá trị rồi cộng các thành phần tương ứng theo giá trị đó. Các chỉ số còn lại, nếu có, xác định các thành phần của kết quả. Đoạn trích chưa nêu cụ thể cặp chỉ số hay phạm vi lấy tổng.

**Ví dụ thêm:** Xét tensor loại \((1,1)\), nghĩa là các thành phần \(A^i{}_j\) có một chỉ số trên \(i\) và một chỉ số dưới \(j\). Trong ví dụ này, ta ghép chỉ số trên với chỉ số dưới để lấy tổng, theo quy ước nêu trong [ghi chép Differential Geometry, mục 2.6](https://math.berkeley.edu/~ltomczak/notes/Mich2022/DG_Notes.pdf#page=14).

Giả sử trong một cơ sở hai chiều, các thành phần của tensor được xếp thành ma trận, với \(i\) chỉ hàng và \(j\) chỉ cột:

\[
(A^i{}_j)_{i,j=1}^{2}=\begin{pmatrix}1&2\\3&4\end{pmatrix}.
\]

Co theo cặp chỉ số trên–dưới này cho

\[
\sum_{i=1}^{2}A^i{}_i=A^1{}_1+A^2{}_2=1+4=5.
\]

Hai chỉ số được ghép cùng nhận giá trị \(i\), nên ta cộng các phần tử trên đường chéo; không cộng cả bốn phần tử. “Co” ở đây nói về phép lấy tổng theo chỉ số, không khẳng định khoảng cách giữa các điểm giảm.
