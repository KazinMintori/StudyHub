---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: bai-toan-dang-non-va-sdp
section: topic
title: "Bài toán dạng nón và quy hoạch nửa xác định"
description: "Bài toán lồi với bất đẳng thức suy rộng, bài toán dạng nón như một mở rộng của LP, quy hoạch nửa xác định với bất đẳng thức ma trận tuyến tính, dạng chuẩn và dạng bất đẳng thức của SDP, ghép nhiều LMI thành một khối chéo, hình học của miền khả thi qua ví dụ ma trận tương quan, và quan hệ LP ⊂ SOCP ⊂ SDP."
---

Quy hoạch tuyến tính dùng thứ tự của từng thành phần: Điều kiện $Gx \preceq h$ nghĩa là mọi thành phần của $h - Gx$ không âm. [Lecture 01](../bai-01-nhap-mon-toi-uu/bat-dang-thuc-tong-quat.md) đã cho thấy thứ tự này chỉ là một trường hợp của bất đẳng thức suy rộng, sinh bởi nón không âm. Thay nón không âm bằng một nón chính quy khác, ta được những họ bài toán mới có cùng cấu trúc với LP. Quan trọng nhất trong số đó là **quy hoạch nửa xác định** (semidefinite program, SDP), dùng nón các ma trận nửa xác định dương.

Trang này định nghĩa bài toán dạng nón và SDP, rồi nhìn miền khả thi của SDP qua một câu hỏi rất cụ thể của thống kê: Ba biến ngẫu nhiên có thể có những bộ hệ số tương quan nào?

## 1. Ràng buộc bất đẳng thức suy rộng

Ta mở rộng bài toán lồi dạng chuẩn bằng cách cho phép hàm ràng buộc nhận giá trị vector và dùng bất đẳng thức suy rộng:

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)\\
\text{subject to}\quad & f_i(x) \preceq_{K_i} 0, \quad i = 1, \ldots, m,\\
& Ax = b,
\end{aligned}
$$

với $K_i$ là các nón chính quy và mỗi $f_i$ lồi theo nón $K_i$. Bài toán lồi thông thường là trường hợp $K_i = \mathbb{R}_+$. Những tính chất quan trọng nhất vẫn giữ nguyên: Miền khả thi, các tập mức dưới và tập nghiệm đều lồi, mọi cực tiểu cục bộ là toàn cục, và [điều kiện tối ưu bậc nhất](../bai-01-nhap-mon-toi-uu/dieu-kien-toi-uu.md) vẫn đúng mà không cần sửa gì.

## 2. Bài toán dạng nón

Bài toán đơn giản nhất thuộc loại này có hàm mục tiêu tuyến tính và một ràng buộc affine theo nón:

$$
\text{minimize}\quad c^Tx \qquad \text{subject to}\quad Fx + g \preceq_K 0,\quad Ax = b .
$$

Đây là **bài toán dạng nón**. Khi $K$ là nón không âm, nó chính là LP, nên có thể xem bài toán dạng nón như một LP mà thứ tự từng thành phần được thay bằng một thứ tự tổng quát hơn. Tương tự như với LP, ta gọi bài toán cực tiểu $c^Tx$ với $x \succeq_K 0$, $Ax = b$ là dạng chuẩn, và bài toán không có ràng buộc đẳng thức là dạng bất đẳng thức. [Chủ đề trước](./quy-hoach-non-bac-hai.md) đã gặp một trường hợp riêng: SOCP là bài toán dạng nón với $K$ là tích của các nón bậc hai.

## 3. Quy hoạch nửa xác định

Khi $K = \mathbb{S}^k_+$, [nón các ma trận nửa xác định dương](../bai-01-nhap-mon-toi-uu/non-psd.md) cỡ $k \times k$, bài toán dạng nón được gọi là **quy hoạch nửa xác định**:

$$
\begin{aligned}
\text{minimize}\quad & c^Tx\\
\text{subject to}\quad & x_1F_1 + \cdots + x_nF_n + G \preceq 0,\\
& Ax = b,
\end{aligned}
$$

với $G, F_1, \ldots, F_n \in \mathbb{S}^k$. Ràng buộc thứ nhất là một **bất đẳng thức ma trận tuyến tính** (linear matrix inequality, LMI). Nó nói rằng ma trận $-(x_1F_1 + \cdots + x_nF_n + G)$, phụ thuộc affine vào $x$, phải nửa xác định dương. Đó không phải điều kiện về từng phần tử, mà về mọi dạng toàn phương: Biểu thức $v^T(\cdots)v \le 0$ phải thỏa mãn với mọi vector $v$. Vì vậy một LMI tương đương với vô hạn bất đẳng thức tuyến tính theo $x$, mỗi bất đẳng thức ứng với một $v$, và miền khả thi là giao của vô hạn nửa không gian.

Nếu mọi ma trận $G, F_1, \ldots, F_n$ đều chéo, LMI tách thành $k$ bất đẳng thức tuyến tính, một cho mỗi phần tử đường chéo, và SDP trở thành LP. Dạng chuẩn của SDP, tương tự dạng chuẩn của LP, dùng biến ma trận $X \in \mathbb{S}^n$:

$$
\text{minimize}\quad \operatorname{tr}(CX) \qquad \text{subject to}\quad \operatorname{tr}(A_iX) = b_i,\ i = 1, \ldots, p,\qquad X \succeq 0 .
$$

Ở đây tích trong Frobenius $\operatorname{tr}(CX) = \sum_{i=1}^n \sum_{j=1}^n C_{ij}X_{ij}$ là dạng tổng quát của một hàm tuyến tính trên không gian các ma trận đối xứng. So với LP dạng chuẩn, vector không âm $x \succeq 0$ được thay bằng ma trận nửa xác định dương $X \succeq 0$, và tích vô hướng $c^Tx$ được thay bằng $\operatorname{tr}(CX)$.

Một bài toán có nhiều LMI và cả bất đẳng thức tuyến tính vẫn được gọi là SDP, vì có thể gộp chúng lại. Một ma trận khối chéo nửa xác định dương khi và chỉ khi từng khối nửa xác định dương, nên các ràng buộc $F^{(1)}(x) \preceq 0, \ldots, F^{(K)}(x) \preceq 0$ và $Gx \preceq h$ tương đương với một LMI duy nhất:

$$
\operatorname{diag}\big(Gx - h,\ F^{(1)}(x),\ \ldots,\ F^{(K)}(x)\big) \preceq 0 .
$$

## 4. Ví dụ: Ba hệ số tương quan

Cho ba biến ngẫu nhiên, ma trận tương quan của chúng là

$$
R = \begin{bmatrix} 1 & \rho_{12} & \rho_{13} \\ \rho_{12} & 1 & \rho_{23} \\ \rho_{13} & \rho_{23} & 1 \end{bmatrix}.
$$

Mỗi hệ số tương quan nằm trong $[-1, 1]$, nhưng điều kiện ấy chưa đủ. Một ma trận như trên là ma trận tương quan của ba biến ngẫu nhiên nào đó khi và chỉ khi nó nửa xác định dương, vì $v^TRv$ là phương sai của tổ hợp tuyến tính $\sum_i v_iX_i/\sigma_i$. Điều kiện $R \succeq 0$ là một LMI theo ba biến $(\rho_{12}, \rho_{13}, \rho_{23})$.

Hãy hỏi một câu cụ thể: Nếu biến 1 tương quan 0.8 với biến 2, và biến 2 tương quan 0.8 với biến 3, thì biến 1 và biến 3 có thể tương quan bao nhiêu? Đó là hai SDP, cực tiểu và cực đại $\rho_{13}$ với ràng buộc $R \succeq 0$ khi $\rho_{12} = \rho_{23} = 0.8$. Với ma trận $3 \times 3$ có các phần tử đường chéo bằng 1, điều kiện nửa xác định dương ở đây quy về định thức không âm, tức

$$
-\rho_{13}^2 + 1.28\,\rho_{13} - 0.28 \ge 0,
$$

nên $\rho_{13} \in [0.28, 1]$. Tương quan không có tính bắc cầu tùy ý: Biến 1 và biến 3 bắt buộc phải tương quan dương ít nhất 0.28. Tổng quát hơn, với $\rho_{12}$ và $\rho_{23}$ cho trước,

$$
\rho_{13} \in \left[\rho_{12}\rho_{23} - \sqrt{(1 - \rho_{12}^2)(1 - \rho_{23}^2)},\ \ \rho_{12}\rho_{23} + \sqrt{(1 - \rho_{12}^2)(1 - \rho_{23}^2)}\right].
$$

Giữ $\rho_{23} = c$ cố định, miền các cặp $(\rho_{12}, \rho_{13})$ hợp lệ là ellipse $\rho_{12}^2 + \rho_{13}^2 - 2c\,\rho_{12}\rho_{13} \le 1 - c^2$, nằm gọn trong hình vuông $[-1, 1]^2$. Diện tích của nó là $\pi\sqrt{1 - c^2}$: Khoảng 78.5% hình vuông khi $c = 0$, nhưng chỉ còn khoảng 47% khi $c = 0.8$. Miền khả thi của một LMI là một tập lồi có thể có biên cong, và người ta gọi nó là một **spectrahedron**. Trong không gian ba chiều, tập các ma trận tương quan $3 \times 3$ có hình dạng giống một chiếc gối phồng, với bốn đỉnh nhọn ứng với những ma trận chỉ gồm các phần tử $\pm 1$.

<CorrelationLab />

Đây cũng là bài toán thực tế. Trong tài chính hay trong thống kê nhiều chiều, các hệ số tương quan thường được ước lượng riêng lẻ từ những nguồn dữ liệu khác nhau. Ghép chúng lại có thể cho một ma trận không nửa xác định dương, và mọi phép tính dựa trên nó, chẳng hạn phương sai của một danh mục, có thể cho kết quả âm vô nghĩa. Tìm ma trận tương quan hợp lệ gần nhất là một SDP.

## 5. LP, SOCP và SDP lồng vào nhau

Ta đã có LP $\subset$ QP $\subset$ QCQP $\subset$ SOCP. SDP còn tổng quát hơn nữa: Một ràng buộc nón bậc hai $\|u\|_2 \le t$ tương đương với LMI

$$
\begin{bmatrix} tI & u \\ u^T & t \end{bmatrix} \succeq 0,
$$

một hệ quả của phần bù Schur mà [chủ đề tiếp theo](./phan-bu-schur-va-bai-toan-tri-rieng.md) sẽ chứng minh. Vì vậy mọi SOCP đều là một SDP. Cái giá của sự tổng quát là chi phí tính toán: Một LMI cỡ $k \times k$ nặng hơn nhiều so với $k$ bất đẳng thức tuyến tính, nên trong thực hành người ta luôn dùng dạng bài toán hẹp nhất đủ để mô tả bài toán.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Ràng buộc $X \succeq 0$ có tương đương với "mọi phần tử của $X$ không âm" không?

<details><summary>Xem lời giải thích</summary>

Không, theo cả hai chiều. Ma trận $\begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$ có mọi phần tử dương nhưng định thức $-3 < 0$, nên có một trị riêng âm, không nửa xác định dương. Ngược lại, $\begin{bmatrix} 1 & -1 \\ -1 & 1 \end{bmatrix}$ có phần tử âm nhưng nửa xác định dương, vì dạng toàn phương là $(v_1 - v_2)^2 \ge 0$. Đây là lý do LMI được viết bằng ký hiệu $\succeq$ riêng: Nó là thứ tự theo nón PSD, khác hẳn thứ tự từng phần tử.

</details>

**Câu 2.** Với $\rho_{23} = 0.5$, điểm $(\rho_{12}, \rho_{13}) = (0.9, -0.9)$ có cả hai hệ số trong $[-1, 1]$. Ma trận tương quan tương ứng có hợp lệ không? Hãy giải thích bằng trực giác.

<details><summary>Xem lời giải thích</summary>

Không. Ma trận có trị riêng nhỏ nhất khoảng $-0.547$. Trực giác: Biến 1 gần như cùng chiều với biến 2 và gần như ngược chiều với biến 3, nên biến 2 và biến 3 phải gần như ngược chiều nhau, tức $\rho_{23}$ phải gần $-1$. Thế mà $\rho_{23} = 0.5$ lại nói chúng cùng chiều vừa phải. Ba thông tin mâu thuẫn, và LMI $R \succeq 0$ chính là cách diễn đạt chính xác sự nhất quán mà trực giác ấy cảm nhận được.

</details>

**Câu 3.** Miền khả thi của một LMI có thể có biên cong, thậm chí có những góc nhọn. Điều gì bảo đảm nó vẫn luôn là một tập lồi?

<details><summary>Xem lời giải thích</summary>

Có hai cách nhìn. Cách thứ nhất: Nón $\mathbb{S}^k_+$ lồi, và miền khả thi là ảnh ngược của nón ấy qua một ánh xạ affine $x \mapsto -(x_1F_1 + \cdots + x_nF_n + G)$, nên lồi. Cách thứ hai: LMI tương đương với họ vô hạn bất đẳng thức $v^T(x_1F_1 + \cdots + G)v \le 0$, mỗi bất đẳng thức tuyến tính theo $x$ với $v$ cố định. Giao của vô hạn nửa không gian là tập lồi. Biên cong vì các nửa không gian có pháp tuyến thay đổi liên tục theo $v$. Góc xuất hiện ở những điểm mà ma trận có trị riêng 0 bội cao, như các ma trận tương quan chỉ gồm $\pm1$.

</details>

**Câu 4.** Trong ví dụ, khoảng của $\rho_{13}$ được tính bằng tay qua định thức. Vì sao với ma trận lớn hơn, ta không thể chỉ đòi định thức không âm?

<details><summary>Xem lời giải thích</summary>

Vì định thức không âm không đủ để ma trận nửa xác định dương. Ma trận $\operatorname{diag}(-1, -1, 1)$ có định thức dương nhưng hai trị riêng âm. Ở ví dụ $3 \times 3$ với đường chéo bằng 1, các định thức con $2 \times 2$ là $1 - \rho^2 \ge 0$ đã được bảo đảm sẵn, và vì vậy chỉ còn phải kiểm định thức toàn phần, theo tiêu chuẩn mọi định thức con chính không âm. Với ma trận tổng quát, phải kiểm mọi định thức con chính, một số lượng tăng theo hàm mũ. Các bộ giải SDP không làm như vậy, mà làm việc trực tiếp với trị riêng và cấu trúc nón.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Từ LMI chéo về LP
Viết LMI $\operatorname{diag}(1 - x_1,\ 2 - x_2,\ x_1 + x_2) \succeq 0$ thành các bất đẳng thức tuyến tính và vẽ miền khả thi.
:::

::: solution
Một ma trận chéo nửa xác định dương khi và chỉ khi mọi phần tử đường chéo không âm, nên LMI tương đương $x_1 \le 1$, $x_2 \le 2$ và $x_1 + x_2 \ge 0$. Miền khả thi là phần mặt phẳng nằm bên trái đường $x_1 = 1$, dưới đường $x_2 = 2$ và phía trên đường $x_1 + x_2 = 0$. Ba đường thẳng cắt nhau từng đôi tại $(1, -1)$, $(1, 2)$ và $(-2, 2)$, và cả ba điểm đều thỏa ràng buộc còn lại, nên miền khả thi là tam giác với ba đỉnh ấy. Nó bị chặn, vì $x_1 \ge -x_2 \ge -2$ và $x_2 \ge -x_1 \ge -1$.
:::

::: exercise 2. Hệ số tương quan
Biến 1 tương quan $0.6$ với biến 2, biến 2 tương quan $-0.6$ với biến 3. Hệ số tương quan giữa biến 1 và biến 3 có thể nằm trong khoảng nào?
:::

::: solution
Theo công thức ở mục 4, $\rho_{12}\rho_{23} = -0.36$ và $\sqrt{(1 - 0.36)(1 - 0.36)} = 0.64$, nên $\rho_{13} \in [-1, 0.28]$. Biến 1 và biến 3 có thể ngược chiều hoàn toàn, nhưng không thể cùng chiều quá 0.28.
:::

::: exercise 3. Một LMI hai biến
Với những $(x, y)$ nào thì $\begin{bmatrix} 1 & x \\ x & y \end{bmatrix} \succeq 0$? Điểm $(1, 2)$ và $(2, 3)$ có thỏa không?
:::

::: solution
Ma trận $2 \times 2$ đối xứng nửa xác định dương khi và chỉ khi hai phần tử đường chéo không âm và định thức không âm. Phần tử đầu là 1, nên điều kiện còn $y \ge 0$ và $y - x^2 \ge 0$, gộp lại là $y \ge x^2$: Miền phía trên parabol, một tập lồi. Điểm $(1, 2)$ thỏa vì $2 \ge 1$, với hai trị riêng khoảng $0.382$ và $2.618$. Điểm $(2, 3)$ không thỏa vì $3 < 4$, và ma trận có một trị riêng khoảng $-0.236$. LMI này chính là epigraph của hàm $x^2$ viết dưới dạng ma trận.
:::

## Tóm tắt

Thay thứ tự từng thành phần bằng thứ tự theo một nón chính quy, ta được bài toán với bất đẳng thức suy rộng, vẫn giữ mọi tính chất quan trọng của bài toán lồi. Bài toán dạng nón cực tiểu một hàm tuyến tính với một ràng buộc affine theo nón, và là LP khi nón là nón không âm. Quy hoạch nửa xác định dùng nón các ma trận nửa xác định dương, với ràng buộc là bất đẳng thức ma trận tuyến tính. LMI chéo cho LP, nhiều LMI gộp được thành một khối chéo, và mọi SOCP đều là SDP.

Miền khả thi của một LMI là một tập lồi có thể có biên cong và góc. Ví dụ ma trận tương quan cho thấy nó mang ý nghĩa rất cụ thể: Không phải bộ hệ số tương quan nào trong $[-1, 1]$ cũng hợp lệ, và khoảng giá trị của một hệ số khi biết các hệ số còn lại là nghiệm của hai SDP.

## Tài liệu tham khảo

- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.
