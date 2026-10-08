---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: phan-bu-schur-va-bai-toan-tri-rieng
section: topic
title: "Phần bù Schur và các bài toán về trị riêng"
description: "Phần bù Schur của một ma trận khối, cách hiểu qua bài toán cực tiểu một dạng toàn phương, tiêu chuẩn nửa xác định dương của ma trận khối, cách dùng phần bù Schur để viết ràng buộc nón bậc hai, tỉ số bậc hai trên tuyến tính và chuẩn phổ thành LMI, bài toán cực tiểu trị riêng lớn nhất và vì sao nó không trơn."
---

[Chủ đề trước](./bai-toan-dang-non-va-sdp.md) định nghĩa SDP nhưng để lại một câu hỏi thực tế: những ràng buộc nào viết được thành bất đẳng thức ma trận tuyến tính? Một ràng buộc như $\|A(x)\|_2 \le t$, chuẩn phổ của một ma trận phụ thuộc vào $x$, trông hoàn toàn phi tuyến. Công cụ biến những ràng buộc như vậy thành LMI là **phần bù Schur**, một kết quả nhỏ của đại số tuyến tính nhưng được dùng ở khắp nơi trong tối ưu lồi.

Trang này trình bày phần bù Schur theo cách của phụ lục A.5.5 trong sách, tức như nghiệm của một bài toán cực tiểu, rồi dùng nó cho ba loại ràng buộc và cho bài toán cực tiểu trị riêng lớn nhất.

## 1. Phần bù Schur

Xét một ma trận đối xứng chia khối

$$
X = \begin{bmatrix} A & B \\ B^T & C \end{bmatrix}, \qquad A \in \mathbb{S}^k .
$$

Nếu $A$ khả nghịch, ma trận

$$
S = C - B^TA^{-1}B
$$

được gọi là **phần bù Schur** của $A$ trong $X$. Nó xuất hiện trong nhiều công thức, chẳng hạn $\det X = \det A \cdot \det S$, và nó là nghịch đảo của khối dưới phải trong $X^{-1}$.

Cách hiểu hữu ích nhất cho tối ưu là qua một bài toán cực tiểu. Giả sử $A \succ 0$ và xét dạng toàn phương của $X$ tại vector $(u, v)$, cực tiểu theo $u$ với $v$ cố định:

$$
\inf_u \begin{bmatrix} u \\ v \end{bmatrix}^T\begin{bmatrix} A & B \\ B^T & C \end{bmatrix}\begin{bmatrix} u \\ v \end{bmatrix} = \inf_u\ \big(u^TAu + 2v^TB^Tu + v^TCv\big) .
$$

Đạo hàm theo $u$ bằng 0 khi $u = -A^{-1}Bv$, và thay vào cho giá trị nhỏ nhất $v^TSv$. Phần bù Schur chính là "phần còn lại" của dạng toàn phương sau khi đã tối ưu hết theo khối biến thứ nhất. Đây đúng là phép [cực tiểu theo từng nhóm biến](./khu-rang-buoc-va-toi-uu-tung-phan.md) đã gặp ở đầu chương, ở đó với ví dụ $3x_1^2 + 2x_1x_2 + 2x_2^2$.

Từ cách hiểu này suy ra ngay tiêu chuẩn nửa xác định dương của ma trận khối:

- $X \succ 0$ khi và chỉ khi $A \succ 0$ và $S \succ 0$.
- Nếu $A \succ 0$, thì $X \succeq 0$ khi và chỉ khi $S \succeq 0$.

Lý do cho ý thứ hai: $X \succeq 0$ nghĩa là dạng toàn phương không âm tại mọi $(u, v)$, tức là giá trị nhỏ nhất theo $u$, chính là $v^TSv$, không âm với mọi $v$. Ví dụ nhỏ: với $X = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$, ta có $S = 1 - \tfrac12 = \tfrac12 > 0$, nên $X \succ 0$, khớp với hai trị riêng khoảng $0.382$ và $2.618$. Một ví dụ khối: ma trận $3 \times 3$ với khối $A = 2I_2$, cột $B = (1, 1)$ và góc $C = c$ có phần bù Schur $S = c - \tfrac{1 + 1}{2} = c - 1$, nên nó nửa xác định dương đúng khi $c \ge 1$. Tại $c = 1$, trị riêng nhỏ nhất của nó đúng bằng 0.

## 2. Biến ràng buộc phi tuyến thành LMI

Đọc tiêu chuẩn trên theo chiều ngược lại: một ràng buộc phi tuyến dạng "$C - B^TA^{-1}B \succeq 0$", với $A \succ 0$, tương đương với một ma trận khối nửa xác định dương. Nếu $A$, $B$, $C$ phụ thuộc affine vào biến, ma trận khối ấy là một LMI. Ba ví dụ quan trọng:

**Tỉ số bậc hai trên tuyến tính.** Với $y > 0$, ràng buộc $\dfrac{x^Tx}{y} \le t$ tương đương với

$$
\begin{bmatrix} yI & x \\ x^T & t \end{bmatrix} \succeq 0,
$$

vì phần bù Schur của khối $yI$ là $t - x^Tx/y$.

**Nón bậc hai.** Với $t > 0$, ràng buộc $\|u\|_2 \le t$ tương đương $t - u^Tu/t \ge 0$, tức

$$
\begin{bmatrix} tI & u \\ u^T & t \end{bmatrix} \succeq 0 .
$$

Trường hợp $t = 0$ cũng khớp: ma trận khi đó chỉ nửa xác định dương khi $u = 0$. Vì vậy mọi ràng buộc nón bậc hai đều là một LMI, và mọi SOCP đều là SDP, như chủ đề trước đã báo trước. Chẳng hạn với $u = (3, 4)$, ma trận trên nửa xác định dương đúng khi $t \ge 5 = \|u\|_2$.

**Chuẩn phổ.** Chuẩn phổ $\|A\|_2$, giá trị kỳ dị lớn nhất của $A \in \mathbb{R}^{p \times q}$, thỏa $\|A\|_2 \le t$ khi và chỉ khi $A^TA \preceq t^2I$ và $t \ge 0$. Áp dụng phần bù Schur, điều kiện này tương đương với

$$
\begin{bmatrix} tI_p & A \\ A^T & tI_q \end{bmatrix} \succeq 0 .
$$

Nếu $A(x) = A_0 + x_1A_1 + \cdots + x_nA_n$ phụ thuộc affine vào $x$, ma trận khối là một LMI theo $(x, t)$, và bài toán cực tiểu chuẩn phổ $\|A(x)\|_2$ là SDP: cực tiểu $t$ với ràng buộc trên.

## 3. Cực tiểu trị riêng lớn nhất

Với một ma trận đối xứng $A(x)$ phụ thuộc affine vào $x$, trị riêng lớn nhất là

$$
\lambda_{\max}(A(x)) = \sup_{\|u\|_2 = 1} u^TA(x)u .
$$

Với mỗi $u$ cố định, $u^TA(x)u$ là hàm affine của $x$, nên $\lambda_{\max}$ là supremum của một họ hàm affine, do đó lồi. Ràng buộc $\lambda_{\max}(A(x)) \le t$ tương đương $tI - A(x) \succeq 0$, một LMI, nên bài toán cực tiểu trị riêng lớn nhất là SDP:

$$
\text{minimize}\quad t \qquad \text{subject to}\quad tI - A(x) \succeq 0 .
$$

Bài toán này có một đặc điểm quan trọng: nó thường **không trơn** tại nghiệm. Ví dụ tự đặt $A(x) = \begin{bmatrix} x & \varepsilon \\ \varepsilon & 1 - x \end{bmatrix}$ có hai trị riêng $\tfrac12 \pm \sqrt{(x - \tfrac12)^2 + \varepsilon^2}$. Trị riêng lớn nhất nhỏ nhất bằng $\tfrac12 + \varepsilon$ tại $x = \tfrac12$. Với $\varepsilon > 0$, hai trị riêng không bao giờ bằng nhau và $\lambda_{\max}$ khả vi. Khi $\varepsilon = 0$, ma trận chéo, $\lambda_{\max} = \max\{x, 1 - x\}$ có một góc nhọn đúng tại nghiệm $x = \tfrac12$, nơi hai trị riêng bằng nhau. Hiện tượng này không phải ngẫu nhiên. Cực tiểu trị riêng lớn nhất có xu hướng đẩy nhiều trị riêng lên cùng một mức, và tại những điểm trị riêng lớn nhất có bội lớn hơn 1, hàm không khả vi. Vì vậy các phương pháp gradient thông thường xử lý bài toán này kém, còn cách viết SDP thì không gặp vấn đề gì.

<EigenLab />

Sách đưa thêm một số ứng dụng của cùng ý tưởng. Tốc độ trộn của một chuỗi Markov đối xứng là chuẩn phổ của ma trận chuyển trạng thái trừ đi ma trận chiếu lên phân phối đều, nên chọn xác suất chuyển trên một đồ thị cho trước để chuỗi trộn nhanh nhất là một SDP. Rủi ro lớn nhất của một danh mục đầu tư khi ma trận hiệp phương sai chỉ được biết một phần, chẳng hạn chỉ biết cận trên và cận dưới của từng phần tử, cũng là một SDP với biến là chính ma trận hiệp phương sai.

## 4. Những câu hỏi để đào sâu

**Câu 1.** Tiêu chuẩn "$X \succeq 0$ khi và chỉ khi $S \succeq 0$" cần giả thiết $A \succ 0$. Hãy tìm một ma trận $X$ với $A = 0$ để thấy giả thiết ấy không thể bỏ.

<details><summary>Xem lời giải thích</summary>

Lấy $X = \begin{bmatrix} 0 & 1 \\ 1 & 1 \end{bmatrix}$, với $A = 0$ không khả nghịch, nên phần bù Schur không định nghĩa được. Ma trận này có định thức $-1 < 0$, nên không nửa xác định dương, dù khối $C = 1 > 0$. Về mặt cực tiểu, với $A = 0$ dạng toàn phương là $2uv + v^2$, tuyến tính theo $u$, nên giá trị nhỏ nhất theo $u$ là $-\infty$ khi $v \ne 0$. Sách có một phiên bản tổng quát cho $A$ suy biến dùng giả nghịch đảo, với thêm điều kiện cột của $B$ nằm trong không gian ảnh của $A$.

</details>

**Câu 2.** Trị riêng lớn nhất là hàm lồi của ma trận. Còn trị riêng nhỏ nhất thì sao, và bài toán cực đại trị riêng nhỏ nhất có lồi không?

<details><summary>Xem lời giải thích</summary>

$\lambda_{\min}(A) = \inf_{\|u\|_2 = 1} u^TAu$ là infimum của một họ hàm tuyến tính theo $A$, nên lõm. Cực đại một hàm lõm là bài toán lồi, nên cực đại $\lambda_{\min}(A(x))$ cũng là SDP: cực đại $t$ với $A(x) - tI \succeq 0$. Hai bài toán "dễ" là cực tiểu $\lambda_{\max}$ và cực đại $\lambda_{\min}$. Hai bài toán ngược lại, cực đại $\lambda_{\max}$ và cực tiểu $\lambda_{\min}$, nói chung không lồi. Trong mô phỏng, đường $\lambda_{\min}$ ở dưới có dạng một cái mái úp, đúng hình dạng của hàm lõm.

</details>

**Câu 3.** Bài toán cực tiểu $\lambda_{\max}$ thường đưa nhiều trị riêng lên cùng một mức tại nghiệm. Hãy giải thích bằng trực giác, rồi cho biết điều đó ảnh hưởng thế nào tới các phương pháp dùng gradient.

<details><summary>Xem lời giải thích</summary>

Nếu tại một điểm chỉ có một trị riêng đạt giá trị lớn nhất, ta thường có thể di chuyển $x$ để kéo nó xuống mà các trị riêng khác chưa kịp vượt lên. Quá trình cực tiểu vì thế dừng lại ở chỗ mà việc kéo một trị riêng xuống buộc một trị riêng khác đi lên, thường là chỗ hai hay nhiều trị riêng lớn nhất bằng nhau. Tại đó $\lambda_{\max}$ không khả vi, như góc nhọn khi $\varepsilon = 0$ trong mô phỏng. Phương pháp gradient sẽ dao động qua lại hai bên góc nhọn, vì gradient đổi hướng đột ngột, và không hội tụ tốt. Đây là lý do người ta giải bài toán trị riêng bằng SDP, hoặc bằng các phương pháp dành riêng cho hàm không trơn.

</details>

**Câu 4.** Dùng phần bù Schur, hãy viết ràng buộc $\|Ax - b\|_2 \le t$ thành một LMI theo $(x, t)$.

<details><summary>Xem lời giải thích</summary>

Đây là ràng buộc nón bậc hai với $u = Ax - b$, phụ thuộc affine vào $x$. Theo mục 2, nó tương đương với

$$
\begin{bmatrix} tI & Ax - b \\ (Ax - b)^T & t \end{bmatrix} \succeq 0,
$$

một ma trận phụ thuộc affine vào $(x, t)$. Cách viết này hữu ích khi ràng buộc phải được ghép chung với những LMI khác thành một SDP. Khi bài toán chỉ có ràng buộc nón bậc hai, giải trực tiếp như một SOCP rẻ hơn nhiều so với chuyển sang SDP.

</details>

## 5. Bài tập tự luyện

::: exercise 1. Tiêu chuẩn Schur
Với những $t$ nào thì ma trận $4 \times 4$ có khối trên trái $2I_3$, cột cuối $(1, 1, 1, t)$ và hàng cuối đối xứng tương ứng, nửa xác định dương?
:::

::: solution
Khối $A = 2I_3 \succ 0$, cột $B = (1, 1, 1)$ và $C = t$. Phần bù Schur là $S = t - B^TA^{-1}B = t - \tfrac{3}{2}$. Vậy ma trận nửa xác định dương khi và chỉ khi $t \ge 1.5$. Tại $t = 1.5$ trị riêng nhỏ nhất bằng 0, và kiểm bằng số cho thấy tại $t = 1.4$ trị riêng nhỏ nhất âm, khoảng $-0.058$.
:::

::: exercise 2. Cực tiểu trị riêng lớn nhất
Tìm $x$ cực tiểu $\lambda_{\max}\!\left(\begin{bmatrix} x & 1 \\ 1 & -x \end{bmatrix}\right)$ và giá trị nhỏ nhất. Viết SDP tương ứng.
:::

::: solution
Ma trận có vết bằng 0 và định thức $-x^2 - 1$, nên hai trị riêng là $\pm\sqrt{x^2 + 1}$. Vậy $\lambda_{\max} = \sqrt{x^2 + 1}$, nhỏ nhất bằng 1 tại $x = 0$. SDP: cực tiểu $t$ với $\begin{bmatrix} t - x & -1 \\ -1 & t + x \end{bmatrix} \succeq 0$. Với $x = 0$, ma trận là $\begin{bmatrix} t & -1 \\ -1 & t \end{bmatrix}$, nửa xác định dương khi $t \ge 1$, khớp với kết quả trên.
:::

::: exercise 3. Từ chuẩn tới LMI
Viết bài toán cực tiểu $\|A_0 + x_1A_1 + x_2A_2\|_2$ thành một SDP, với $A_0, A_1, A_2 \in \mathbb{R}^{3 \times 2}$. LMI có cỡ bao nhiêu?
:::

::: solution
Cực tiểu $t$ với $\begin{bmatrix} tI_3 & A(x) \\ A(x)^T & tI_2 \end{bmatrix} \succeq 0$, trong đó $A(x) = A_0 + x_1A_1 + x_2A_2$. Ma trận khối có cỡ $(3 + 2) \times (3 + 2) = 5 \times 5$, phụ thuộc affine vào ba biến $(x_1, x_2, t)$.
:::

## Tóm tắt

Phần bù Schur $S = C - B^TA^{-1}B$ của khối $A$ trong một ma trận đối xứng chia khối là giá trị nhỏ nhất của dạng toàn phương theo khối biến thứ nhất. Từ đó, khi $A \succ 0$, ma trận khối nửa xác định dương khi và chỉ khi $S \succeq 0$. Đọc ngược tiêu chuẩn này, nhiều ràng buộc phi tuyến trở thành LMI: tỉ số bậc hai trên tuyến tính, ràng buộc nón bậc hai và ràng buộc chuẩn phổ.

Trị riêng lớn nhất của một ma trận đối xứng phụ thuộc affine vào $x$ là hàm lồi, trị riêng nhỏ nhất là hàm lõm, và cực tiểu trị riêng lớn nhất là một SDP. Tại nghiệm, các trị riêng lớn nhất thường bằng nhau và hàm không khả vi, nên cách viết SDP đáng tin cậy hơn các phương pháp gradient thông thường.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §A.5.5 (tr. 650–651) về phần bù Schur, bài toán (A.13)–(A.14) và tiêu chuẩn nửa xác định dương. §4.6.3 (tr. 169–174) về SOCP như một bài toán dạng nón, cực tiểu chuẩn ma trận, rủi ro danh mục với hiệp phương sai không đầy đủ và chuỗi Markov trộn nhanh nhất.
- Ví dụ khối, mô phỏng trị riêng với phần tử ngoài đường chéo, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
