---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: quy-hoach-toan-phuong
section: topic
title: "Quy hoạch toàn phương và QCQP"
description: "Quy hoạch toàn phương với mục tiêu toàn phương lồi trên đa diện, hình học của nghiệm khi đường mức là ellipse, QCQP và quan hệ LP ⊂ QP ⊂ QCQP, các ví dụ của sách: Bình phương tối thiểu có ràng buộc, khoảng cách giữa hai đa diện, phương sai lớn nhất, LP có chi phí ngẫu nhiên và danh mục đầu tư Markowitz."
---

Quy hoạch tuyến tính dùng hàm mục tiêu phẳng như một mặt dốc. Rất nhiều bài toán thực tế lại có hàm mục tiêu cong: Bình phương sai số, phương sai của rủi ro, bình phương khoảng cách. Khi hàm mục tiêu là một hàm toàn phương lồi và các ràng buộc vẫn affine, ta có một **quy hoạch toàn phương** (quadratic program, QP). Sự thay đổi tưởng nhỏ ấy làm hình học của nghiệm khác hẳn: Nghiệm không còn bị buộc phải nằm ở đỉnh của đa diện.

Trang này trình bày QP, mở rộng của nó là QCQP, và năm ví dụ của sách cho thấy QP xuất hiện từ những nguồn rất khác nhau: Thống kê, hình học, xác suất và tài chính.

## 1. Bài toán

Một QP có dạng

$$
\begin{aligned}
\text{minimize}\quad & \tfrac12 x^TPx + q^Tx + r\\
\text{subject to}\quad & Gx \preceq h,\quad Ax = b,
\end{aligned}
$$

với $P \in \mathbb{S}^n_+$, tức $P$ đối xứng và [nửa xác định dương](../bai-01-nhap-mon-toi-uu/non-psd.md). Điều kiện $P \succeq 0$ là điều làm hàm mục tiêu lồi, nên QP là bài toán lồi. Thiếu điều kiện này, ta vẫn có một bài toán cực tiểu hàm toàn phương trên đa diện, nhưng nó không còn lồi và nói chung rất khó, như Câu 2 sẽ cho thấy. Với $P = 0$, QP trở thành LP.

Về hình học, các tập mức của hàm mục tiêu là những ellipse đồng tâm khi $P \succ 0$. Nghiệm là điểm đầu tiên của đa diện mà các ellipse chạm vào khi chúng nở ra từ tâm. Có ba khả năng. Nếu tâm, tức nghiệm của bài toán không ràng buộc, nằm trong đa diện, thì đó là nghiệm và không ràng buộc nào chặt. Nếu không, ellipse có thể chạm đa diện tại một điểm giữa một cạnh, hoặc tại một đỉnh. Khác với LP, trường hợp thứ nhất và thứ hai là bình thường, không phải ngoại lệ. Khi $P \succ 0$, hàm mục tiêu lồi chặt, nên nghiệm, nếu có, là duy nhất.

## 2. QCQP

Nếu cả các ràng buộc bất đẳng thức cũng là hàm toàn phương lồi,

$$
\begin{aligned}
\text{minimize}\quad & \tfrac12 x^TP_0x + q_0^Tx + r_0\\
\text{subject to}\quad & \tfrac12 x^TP_ix + q_i^Tx + r_i \le 0, \quad i = 1, \ldots, m,\\
& Ax = b,
\end{aligned}
$$

với $P_i \succeq 0$, ta có một **quy hoạch toàn phương với ràng buộc toàn phương** (QCQP). Khi $P_i \succ 0$, mỗi ràng buộc mô tả một [ellipsoid](../bai-01-nhap-mon-toi-uu/qua-cau-va-ellipsoid.md), và ta cực tiểu một hàm toàn phương lồi trên giao của các ellipsoid. Các lớp bài toán lồng vào nhau: LP là QP với $P = 0$, và QP là QCQP với mọi $P_i = 0$. Một ràng buộc như $x_1^2 + x_2^2 \ge 1$ không thuộc QCQP, vì viết thành $1 - x_1^2 - x_2^2 \le 0$ thì vế trái lõm, và miền khả thi là phần bên ngoài một hình tròn, không lồi.

## 3. Bình phương tối thiểu có ràng buộc

Bài toán cực tiểu $\|Ax - b\|_2^2 = x^TA^TAx - 2b^TAx + b^Tb$ là một QP không ràng buộc với $P = 2A^TA \succeq 0$, và nó có công thức nghiệm quen thuộc qua phương trình chuẩn. Khi thêm ràng buộc tuyến tính, chẳng hạn cận dưới và cận trên cho từng biến, $l_i \le x_i \le u_i$, ta được **bình phương tối thiểu có ràng buộc**. Bài toán vẫn là QP, nhưng không còn công thức nghiệm đơn giản.

Ví dụ tự đặt: Khớp $y \approx w_1u + w_2$ với dữ liệu $u = (1, 2, 3, 4)$, $y = (2, 3.5, 5.5, 7)$, nhưng hệ số góc là một đại lượng vật lý chỉ được nằm trong $[0, 1]$. Không có ràng buộc, nghiệm là $w = (1.7,\ 0.25)$ với tổng bình phương sai số 0.05. Hệ số góc 1.7 vi phạm ràng buộc. Dùng [tối ưu theo từng nhóm biến](./khu-rang-buoc-va-toi-uu-tung-phan.md): Với $w_1$ cố định, hệ số chặn tốt nhất là $\bar y - w_1\bar u$, và tổng bình phương sai số còn lại là một parabol theo $w_1$ có đỉnh tại 1.7. Trên đoạn $[0, 1]$, parabol này giảm, nên $w_1^\star = 1$, rồi $w_2^\star = 4.5 - 2.5 = 2$, với tổng bình phương sai số 2.5. Cái giá của ràng buộc vật lý là sai số khớp tăng từ 0.05 lên 2.5.

Có một cám dỗ cần tránh: Giải bài toán không ràng buộc rồi kẹp từng thành phần vào hộp. Khi các biến tương quan với nhau, cách làm ấy có thể cho kết quả tệ, như Câu 3 sẽ cho thấy.

## 4. Khoảng cách giữa hai đa diện

Khoảng cách Euclid giữa hai đa diện $\mathcal{P}_1 = \{x : A_1x \preceq b_1\}$ và $\mathcal{P}_2 = \{x : A_2x \preceq b_2\}$ là giá trị tối ưu của QP

$$
\text{minimize}\quad \|x_1 - x_2\|_2^2 \qquad \text{subject to}\quad A_1x_1 \preceq b_1,\quad A_2x_2 \preceq b_2,
$$

với biến $(x_1, x_2)$. Bài toán bất khả thi khi và chỉ khi một trong hai đa diện rỗng. Giá trị tối ưu bằng 0 khi và chỉ khi hai đa diện giao nhau. Trong trường hợp còn lại, nghiệm là cặp điểm gần nhau nhất của hai đa diện, và như mô phỏng cho thấy, đường trung trực của đoạn nối chúng là một siêu phẳng tách hai đa diện. Lecture 01 đã dùng đúng cặp điểm gần nhất này để chứng minh [định lý siêu phẳng phân tách](../bai-01-nhap-mon-toi-uu/sieu-phang-phan-tach-va-tua.md). Giờ lời chứng minh ấy đã thành một thuật toán: Giải một QP rồi lấy đường trung trực.

<PolyDistanceLab />

## 5. Phương sai lớn nhất và chi phí ngẫu nhiên

**Phương sai lớn nhất.** Trở lại tình huống ở [chủ đề trước](./mo-hinh-lp.md): Một biến ngẫu nhiên nhận các giá trị đã biết, với phân phối $p$ chưa biết, chỉ thỏa vài ràng buộc tuyến tính. Phương sai của $f(x)$ là

$$
\sum_i f_i^2p_i - \Big(\sum_i f_ip_i\Big)^2,
$$

một hàm **lõm** bậc hai của $p$, vì nó là một hàm tuyến tính trừ đi bình phương của một hàm tuyến tính. Cực đại một hàm lõm trên đa diện là một bài toán lồi, và ở đây nó là một QP. Với biến nhận giá trị trong $\{0, 1, 2, 3, 4\}$ và trung bình nằm trong $[1, 2]$, phương sai lớn nhất có thể là 4, đạt khi dồn một nửa khối lượng vào 0 và nửa kia vào 4. Kết quả khớp với trực giác: Muốn phương sai lớn, hãy đẩy khối lượng ra hai đầu.

**LP có chi phí ngẫu nhiên.** Xét một LP mà vector chi phí $c$ là ngẫu nhiên, với trung bình $\bar c$ và ma trận hiệp phương sai $\Sigma$. Với một quyết định $x$, chi phí $c^Tx$ có trung bình $\bar c^Tx$ và phương sai $x^T\Sigma x$. Thường có một sự đánh đổi giữa chi phí trung bình nhỏ và rủi ro nhỏ. Cực tiểu **chi phí có tính đến rủi ro** $\bar c^Tx + \gamma\,x^T\Sigma x$, với $\gamma \ge 0$ là mức ngại rủi ro, trên cùng miền khả thi là một QP, vì $\Sigma \succeq 0$.

## 6. Danh mục đầu tư Markowitz

Bài toán danh mục đầu tư kinh điển của Markowitz là một QP. Có $n$ tài sản, $x_i$ là tỉ lệ vốn đặt vào tài sản $i$, với $\mathbf{1}^Tx = 1$ và $x \succeq 0$ nếu không cho phép bán khống. Lợi suất của các tài sản là một vector ngẫu nhiên với trung bình $\bar p$ và hiệp phương sai $\Sigma$, nên lợi suất của danh mục có trung bình $\bar p^Tx$ và phương sai $x^T\Sigma x$. Bài toán là

$$
\text{minimize}\quad x^T\Sigma x \qquad \text{subject to}\quad \bar p^Tx \ge r_{\min},\quad \mathbf{1}^Tx = 1,\quad x \succeq 0,
$$

tức tìm danh mục ít rủi ro nhất trong những danh mục đạt lợi suất trung bình tối thiểu $r_{\min}$.

Ví dụ tự đặt với hai tài sản: Tài sản A có lợi suất trung bình 10% và độ lệch chuẩn 15%, tài sản B có 4% và 5%, hệ số tương quan $-0.2$. Danh mục ít rủi ro nhất, không cần đạt lợi suất nào, đặt $\tfrac17 \approx 14.3\%$ vốn vào A. Nó có lợi suất khoảng 4.86% và độ lệch chuẩn khoảng 4.39%, **thấp hơn cả** tài sản an toàn hơn trong hai tài sản. Đây là sức mạnh của đa dạng hóa: Khi hai tài sản tương quan âm, biến động của chúng triệt tiêu một phần. Nếu đòi lợi suất ít nhất 7%, ràng buộc lợi suất chặt, buộc đặt một nửa vốn vào mỗi tài sản, và độ lệch chuẩn tăng lên khoảng 7.42%. Chủ đề [tối ưu vector](./toi-uu-vector-va-danh-doi.md) sẽ xem toàn bộ đường đánh đổi giữa lợi suất và rủi ro.

## 7. Những câu hỏi để đào sâu

**Câu 1.** Trong LP, nghiệm (nếu có) luôn có thể chọn ở một đỉnh của đa diện có đỉnh. Vì sao điều này sai với QP?

<details><summary>Xem lời giải thích</summary>

Vì đường mức của hàm toàn phương cong. Trong LP, đường mức là siêu phẳng, nên khi đẩy nó tới biên đa diện, chỗ chạm đầu tiên luôn chứa một đỉnh. Với QP, đường mức là ellipse, và một ellipse đang nở có thể chạm một cạnh tại điểm giữa cạnh, nơi cạnh là tiếp tuyến của ellipse. Nó còn có thể không chạm biên chút nào, nếu tâm ellipse đã nằm trong đa diện. Hệ quả thuật toán là phương pháp đơn hình, vốn chỉ đi qua các đỉnh, không dùng trực tiếp được cho QP. Các thuật toán cho QP như phương pháp tập chặt hay phương pháp điểm trong phải tính đến nghiệm nằm giữa cạnh hoặc bên trong.

</details>

**Câu 2.** Nếu $P$ không nửa xác định dương, chẳng hạn cực tiểu $-\|x\|_2^2$ trên hình hộp $[-1, 1]^n$, bài toán còn dễ không?

<details><summary>Xem lời giải thích</summary>

Bài toán này tương đương cực đại $\|x\|_2^2$ trên hình hộp. Mọi đỉnh $(\pm1, \ldots, \pm1)$ đều là nghiệm với giá trị $n$, nên ở ví dụ này ta biết nghiệm. Nhưng thay $\|x\|^2$ bằng một dạng toàn phương không xác định tổng quát, bài toán cực đại một hàm lồi trên đa diện nói chung chỉ giải được bằng cách so sánh rất nhiều đỉnh, và hình hộp $n$ chiều có $2^n$ đỉnh. Bài toán QP không lồi thuộc lớp NP-khó, nên không có thuật toán nào được biết là giải nó nhanh trong mọi trường hợp. Điều kiện $P \succeq 0$ không phải chi tiết kỹ thuật, mà là ranh giới giữa dễ và khó.

</details>

**Câu 3.** Với ma trận $A$ có các hàng $(1, 0.9)$, $(0.9, 1)$, $(1, 1.1)$ và $b = (2.5,\ 0.2,\ 2.6)$, nghiệm bình phương tối thiểu không ràng buộc là khoảng $(7.17,\ -5.13)$. Kẹp nó vào hình hộp $[0, 1]^2$ được $(1, 0)$. Đó có phải nghiệm của bài toán có ràng buộc hộp không?

<details><summary>Xem lời giải thích</summary>

Không. Điểm kẹp $(1, 0)$ cho tổng bình phương sai số khoảng $5.30$, trong khi nghiệm đúng của QP có ràng buộc hộp là khoảng $(1,\ 0.798)$ với giá trị khoảng $3.38$. Phép kẹp chỉ đúng khi hàm mục tiêu tách được theo từng biến, tức $A^TA$ chéo. Ở đây hai cột của $A$ gần cùng hướng, nên hai biến bù trừ cho nhau mạnh: Nghiệm không ràng buộc dùng một biến rất dương và một biến rất âm để triệt tiêu lẫn nhau. Khi một biến bị chặn, biến kia phải điều chỉnh lại theo, và phép kẹp từng thành phần bỏ qua sự điều chỉnh ấy. Muốn đúng, phải giải QP, hoặc ít nhất dùng phương pháp gradient có chiếu.

</details>

**Câu 4.** Trong mô phỏng, khoảng cách giữa hai đa giác thay đổi khi kéo $P_2$. Vì sao khoảng cách, xem như hàm của vector tịnh tiến $c$ của $P_2$, là một hàm lồi?

<details><summary>Xem lời giải thích</summary>

Khoảng cách giữa $\mathcal{P}_1$ và $\mathcal{P}_2 + c$ là $\inf\{\|x_1 - x_2 - c\|_2 : x_1 \in \mathcal{P}_1,\ x_2 \in \mathcal{P}_2\}$. Hàm $(x_1, x_2, c) \mapsto \|x_1 - x_2 - c\|_2$ lồi đồng thời theo cả ba biến, và tập các $(x_1, x_2)$ khả thi lồi. Cực tiểu hóa theo một phần biến giữ tính lồi, nên kết quả là hàm lồi theo $c$. Một cách nhìn khác: Khoảng cách ấy chính là khoảng cách từ $c$ tới tập lồi $\mathcal{P}_1 - \mathcal{P}_2$, và khoảng cách tới một tập lồi là hàm lồi.

</details>

**Câu 5.** Vì sao cực đại phương sai là bài toán lồi, còn cực tiểu phương sai trên cùng tập phân phối thì sao?

<details><summary>Xem lời giải thích</summary>

Phương sai là hàm lõm theo $p$, nên cực đại nó là cực tiểu một hàm lồi, một bài toán lồi. Cực tiểu phương sai theo $p$ là cực tiểu một hàm lõm, nói chung không lồi, và nghiệm nằm ở các đỉnh của đa diện phân phối. Điều này ngược với bài toán Markowitz, nơi phương sai $x^T\Sigma x$ là hàm lồi theo **tỉ lệ đầu tư** $x$, nên cực tiểu nó là bài toán lồi. Cùng một chữ "phương sai", nhưng là hàm của những biến khác nhau, nên có tính lồi ngược nhau.

</details>

## 8. Bài tập tự luyện

::: exercise 1. QP trên hình vuông
Cực tiểu $(x_1 - 3)^2 + (x_2 + 1)^2$ trên hình vuông $[0, 2]^2$. Nghiệm nằm ở đỉnh, giữa cạnh hay bên trong? Ràng buộc nào chặt?
:::

::: solution
Bài toán tìm điểm của hình vuông gần $(3, -1)$ nhất, tức phép chiếu của $(3, -1)$ lên hình vuông. Vì hàm mục tiêu tách được theo hai tọa độ, ta kẹp từng tọa độ: $x_1 = \min\{3, 2\} = 2$ và $x_2 = \max\{-1, 0\} = 0$. Nghiệm là đỉnh $(2, 0)$ với giá trị $1 + 1 = 2$. Hai ràng buộc $x_1 \le 2$ và $x_2 \ge 0$ chặt. Ở đây phép kẹp hợp lệ, khác với Câu 3, vì $P$ chéo.
:::

::: exercise 2. Khoảng cách giữa hai hình hộp
Tính khoảng cách giữa hình vuông $[0, 1]^2$ và hình chữ nhật $[3, 4] \times [2, 5]$, và chỉ ra cặp điểm gần nhau nhất.
:::

::: solution
Theo trục $x_1$, khoảng cách giữa hai đoạn $[0, 1]$ và $[3, 4]$ là 2, đạt khi $x_1$ bằng 1 và 3. Theo trục $x_2$, khoảng cách giữa $[0, 1]$ và $[2, 5]$ là 1, đạt khi $x_2$ bằng 1 và 2. Vì cả hai tập là tích của các đoạn, bài toán tách theo từng trục, và khoảng cách là $\sqrt{2^2 + 1^2} = \sqrt5 \approx 2.236$, giữa hai điểm $(1, 1)$ và $(3, 2)$.
:::

::: exercise 3. Danh mục hai tài sản
Với hai tài sản A, B như ở mục 6, chứng minh danh mục ít rủi ro nhất đặt $\tfrac17$ vốn vào A. Gợi ý: Viết phương sai như hàm một biến $x_1$, với $x_2 = 1 - x_1$.
:::

::: solution
Ma trận hiệp phương sai có các phần tử $\sigma_A^2 = 0.0225$, $\sigma_B^2 = 0.0025$ và hiệp phương sai $\rho\sigma_A\sigma_B = -0.0015$. Phương sai của danh mục là

$$
v(x_1) = 0.0225x_1^2 - 0.003x_1(1 - x_1) + 0.0025(1 - x_1)^2 .
$$

Lấy đạo hàm và gom các số hạng, ta được $v'(x_1) = 0.056x_1 - 0.008$, triệt tiêu tại $x_1 = \tfrac{0.008}{0.056} = \tfrac17$. Điểm này nằm trong $[0, 1]$, nên ràng buộc không âm không chặt, và đó là nghiệm.
:::

## Tóm tắt

Quy hoạch toàn phương cực tiểu một hàm toàn phương lồi, với $P \succeq 0$, trên một đa diện. Đường mức là ellipse, nên nghiệm có thể nằm bên trong, giữa một cạnh hoặc tại một đỉnh, và là duy nhất khi $P \succ 0$. QCQP cho phép cả ràng buộc toàn phương lồi, và các lớp lồng nhau: LP nằm trong QP, QP nằm trong QCQP. Không có điều kiện $P \succeq 0$, bài toán trở nên khó.

QP xuất hiện từ nhiều nguồn. Trong thống kê, đó là bình phương tối thiểu có ràng buộc, còn trong hình học, đó là khoảng cách giữa hai đa diện, kèm theo siêu phẳng tách của chúng. Xác suất cho bài toán phương sai lớn nhất trên một tập phân phối và LP có chi phí ngẫu nhiên. Tài chính cho danh mục Markowitz, nơi đa dạng hóa có thể làm rủi ro thấp hơn cả tài sản an toàn nhất.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §4.4 (tr. 152–153) về QP, QCQP và Hình 4.5. §4.4.1 (tr. 153–156) về bình phương tối thiểu có ràng buộc, khoảng cách giữa hai đa diện, phương sai lớn nhất, LP có chi phí ngẫu nhiên và danh mục Markowitz.
- Ví dụ khớp dữ liệu có ràng buộc hệ số góc, phản ví dụ về phép kẹp, mô phỏng, ví dụ phương sai lớn nhất, ví dụ hai tài sản, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
