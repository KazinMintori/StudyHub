---
title: "Hình học tập lồi — đọc thêm sau Lecture 01"
description: "Tập affine, ellipsoid, nón, phối cảnh, phân tách và thứ tự Pareto từ chương 2 Convex Optimization."
---

# Hình học tập lồi

Trang này giữ các công cụ của chương 2 cần cho mô hình nón và đối ngẫu nhưng chưa cần đọc liền trong lần học đầu. Chọn một mục khi gặp nó trong Notes. Không cần học cả trang trước Lecture 02. Nguồn nội dung là *Convex Optimization*, chương 2. Các số và ví dụ ở đây tự đặt.

## 1. Bao affine, bao lồi và nội tương đối

Trước hết, chọn $k$ điểm $x_1,\ldots,x_k$ trong $C$ và gắn cho mỗi điểm một trọng số $\theta_i$. Tổng có trọng số được viết đầy đủ là

$$
z=\theta_1x_1+\theta_2x_2+\cdots+\theta_kx_k.
$$

Điều kiện “các trọng số cộng thành 1” nghĩa là

$$
\theta_1+\theta_2+\cdots+\theta_k=1.
$$

Viết gọn hai dòng này bằng ký hiệu tổng:

$$
z=\sum_{i=1}^{k}\theta_i x_i,
\qquad \sum_{i=1}^{k}\theta_i=1.
$$

Chỉ số $i$ chạy qua các số nguyên từ 1 đến $k$. $\theta_i x_i$ là số hạng ứng với điểm thứ $i$. Sau khi đã xác định phạm vi đó, có thể viết tắt $\sum_i$. Tổng trọng số bằng 1 không có nghĩa từng trọng số đều bằng 1.

**Bao affine** của $C$ gồm mọi tổ hợp hữu hạn như trên, cho phép trọng số âm. **Bao lồi** thêm điều kiện $\theta_i\ge0$ với mọi $i$. Mỗi bao là tập nhỏ nhất cùng loại chứa $C$.

Với ba điểm $x_1=(0,0)$, $x_2=(1,0)$, $x_3=(0,1)$ và trọng số $\theta_1=\frac12$, $\theta_2=\frac13$, $\theta_3=\frac16$, ta có $\theta_1+\theta_2+\theta_3=1$ và $z=(\frac13,\frac16)$. Bao lồi của ba điểm là tam giác đặc, còn bao affine là cả mặt phẳng. **Simplex xác suất** $\{p\in\mathbb R^k:p_i\ge0,\sum_{i=1}^k p_i=1\}$ là bao lồi của các vector đơn vị. Mỗi $p_i$ là một trọng số. Với ba thành phần, điều kiện chuẩn hóa là $p_1+p_2+p_3=1$.

Không gian affine nhỏ nhất chứa tập xác định **chiều affine**. Đoạn nằm trên một đường trong $\mathbb R^2$ có chiều affine 1. Nội tương đối bỏ hai đầu mút khi nhìn trong đường đó. Nội hai chiều của đoạn rỗng. Đây là khái niệm dùng trong Slater ở Lecture 03.

## 2. Ellipsoid và các chuẩn

Với $P\succ0$, ellipsoid tâm $c$ là

$$E=\{x:(x-c)^TP^{-1}(x-c)\le1\}.$$

Nếu $P=AA^T$ với $A$ vuông khả nghịch, cũng có thể viết $E=\{c+Au:\|u\|_2\le1\}$. Hai ma trận $A$ và $P$ có vai trò khác nhau. Trị riêng của $P$ cho bình phương độ dài bán trục. Vector riêng cho hướng trục.

Ví dụ $P=\operatorname{diag}(4,1)$ cho $\frac{x_1^2}{4}+x_2^2\le1$ với bán trục 2 và 1. Dùng $A=\operatorname{diag}(2,1)$ mới cho cùng miền. Dùng $A=P$ sẽ làm bán trục đầu thành 4.

Trong hai chiều, quả cầu chuẩn 1 là $|x_1|+|x_2|\le1$, chuẩn 2 là $x_1^2+x_2^2\le1$, chuẩn vô cùng là $\max(|x_1|,|x_2|)\le1$. Đọc hình học từ bất đẳng thức. Các miền này đều lồi, nhưng biên của chúng nói chung không lồi.

## 3. Nón lồi, nón chính quy và PSD

Một tập là **nón** nếu nhân một điểm của nó với mọi hệ số không âm vẫn ở trong tập. Nón **lồi** giữ $\alpha x+\beta y$ với $\alpha,\beta\ge0$, không cần tổng bằng 1. Không nhầm phép nhân thay đổi quy mô này với pha xác suất.

Nón $\mathbb R^n_+$ gồm vector không âm. Nón chuẩn là $\{(x,t):\|x\|\le t\}$. Nón bậc hai dùng chuẩn Euclid. Nón PSD sống trong không gian ma trận đối xứng: nếu $X,Y\succeq0$, thì với mọi $v$,

$$v^T(\alpha X+\beta Y)v=\alpha v^TXv+\beta v^TYv\ge0.$$

Vì vậy nó là nón lồi. Khi đọc PSD, điểm trong miền là một ma trận, không phải vector các phần tử bị ép không âm.

Nón **chính quy** là nón lồi, đóng, có nội khác rỗng và nhọn: $K\cap(-K)=\{0\}$. Bốn thuộc tính này không được rút thành “có dạng nón đẹp”. Chúng giúp tạo thứ tự và một nón đối ngẫu phù hợp.

## 4. Phối cảnh và phân tuyến tính

Phép phối cảnh $P(z,t)=z/t$ có miền $t>0$. Nó giữ tính lồi của ảnh và ảnh ngược các tập lồi trên miền ấy nhưng không giữ nguyên trọng số của đoạn.

Với $u=(z_1,t_1)$, $v=(z_2,t_2)$, $t_1,t_2>0$,

$$P(\theta u+(1-\theta)v)
=\gamma P(u)+(1-\gamma)P(v),\quad
\gamma=\frac{\theta t_1}{\theta t_1+(1-\theta)t_2}\in[0,1].$$

Đây là bước chứng minh: trọng số mới vẫn không âm và cộng thành 1. Ví dụ $u=(0,1)$, $v=(4,2)$: phối cảnh của trung điểm là $\frac{4}{3}$, trong khi trung điểm hai ảnh là 1. Chúng khác nhau nhưng cùng ở đoạn ảnh $[0,2]$.

Ánh xạ phân tuyến tính $F(x)=(Ax+b)/(c^Tx+d)$ là affine rồi phối cảnh, trên miền $c^Tx+d>0$. Không bỏ điều kiện dấu mẫu. Chia qua một mẫu chưa biết dấu sẽ làm sai bất đẳng thức và chứng minh.

## 5. Siêu phẳng phân tách và siêu phẳng tựa

Siêu phẳng $a^Tx=b$, $a\ne0$, chia không gian thành hai nửa. Hai tập lồi khác rỗng, không giao nhau có một siêu phẳng phân tách yếu: $a^Tx\le b$ trên một tập và $a^Ty\ge b$ trên tập kia. “Yếu” cho phép có dấu bằng. Không tự suy ra khoảng cách dương giữa các tập.

Một điều kiện đủ đơn giản cho phân tách chặt là hai tập lồi đóng, không giao nhau, và một tập compact. Khi ấy có thể đặt một khoảng dương giữa hai mức chiếu. Thiếu điều kiện này, các tập có thể tiến sát nhau mà không giao.

Tại điểm biên $x_0$ của tập lồi, một **siêu phẳng tựa** đi qua $x_0$ và giữ toàn tập về một phía. Ví dụ hình tròn đặc đơn vị có siêu phẳng tựa $x_1=1$ tại $(1,0)$. Đây là hình học phía sau điều kiện bậc nhất tại biên, không chỉ là tiếp tuyến của đồ thị hàm.

## 6. Nón đối ngẫu và thứ tự Pareto

Với nón $K$, nón đối ngẫu

$$K^*=\{y:y^Tx\ge0\ \forall x\in K\}.$$

Nó gồm những hướng chấm điểm không âm trên mọi hướng của $K$. Với không gian ma trận đối xứng, thay tích vô hướng bằng $\operatorname{tr}(XY)$, trong đó trace là tổng phần tử đường chéo.

$\mathbb R^n_+$ tự đối ngẫu. Nón bậc hai và nón PSD cũng tự đối ngẫu với tích vô hướng tương ứng. Ký hiệu $x\preceq_Ky$ nghĩa là $y-x\in K$. Với PSD, nó so ma trận theo dạng toàn phương.

Với $K=\mathbb R^n_+$ và mục tiêu giảm nhiều tọa độ, một điểm **nhỏ nhất** không lớn hơn mọi điểm khác theo từng tọa độ. Một điểm **tối thiểu/Pareto** chỉ đòi không có điểm khác nhỏ hơn hoặc bằng ở mọi tọa độ và nhỏ hơn thật ở ít nhất một tọa độ. Các điểm tối thiểu có thể không so sánh được.

::: example Hai chi phí đã chuẩn hóa
Các phương án tự đặt $A=(1,6)$, $B=(2,4)$, $C=(4,2)$ không phương án nào trội hơn phương án khác theo cả hai chi phí. $D=(3,6)$ bị $A$ trội hơn.

Với trọng số $(3,1)$, chi phí $A,B,C$ là $9,10,14$, chọn A. Với $(3,2)$ là $15,14,16$, chọn B. Với $(1,3)$ là $19,14,10$, chọn C. Phải chuẩn hóa đơn vị trước khi diễn giải trọng số giữa các chi phí khác đơn vị.
:::

Với trọng số dương ở mọi tọa độ, cực tiểu tổng có trọng số cho điểm Pareto: nếu một điểm khác trội hơn, tổng sẽ nhỏ hơn thật, mâu thuẫn. Tổng trọng số dương không tạo ra điểm nhỏ nhất của mọi tiêu chí.

Trong trường hợp nón chính quy tổng quát, dùng $\lambda\in\operatorname{int}K^*$ cho chiều đủ tương tự. Một số kết quả ngược trên tập lồi chỉ cho $\lambda\in K^*\setminus\{0\}$, có thể trên biên. Không tự nâng nó thành trọng số trong nội. “Minimal” ở đây thuộc thứ tự, khác “local minimum” của giải tích.

## Tự kiểm

1. Vì sao nón PSD không thể kiểm bằng dấu từng phần tử?
2. Vì sao phép phối cảnh không giữ trung điểm?
3. Một trọng số bằng 0 có bỏ qua một tiêu chí không?

<details><summary>Đáp án</summary>

1. PSD kiểm mọi dạng $v^TXv$. Ma trận $\begin{bmatrix}1&2\\2&1\end{bmatrix}$ vi phạm ở $v=(1,-1)$ dù mọi phần tử dương.
2. Nó đổi trọng số từ $\theta$ thành $\gamma$ tùy hai mẫu số. Ví dụ mục 4 tính ra $\frac{4}{3}\ne1$.
3. Có. Khi tiêu chí bị bỏ qua, một điểm đạt tối ưu tổng có thể bị trội hơn chỉ ở tiêu chí ấy, nên không đủ kết luận Pareto.

</details>

## Nguồn và đường đọc

*Convex Optimization*, §2.1 (affine, lồi, nội tương đối), §2.2 (chuẩn, ellipsoid, PSD), §2.3.3 (phối cảnh), §2.4 (thứ tự), §2.5 (phân tách, tựa), §2.6 (đối ngẫu nón). Các ví dụ số tự biên soạn. Không có ảnh sao chép từ sách.

[Quay lại Lecture 01](../bai-giang/bai-01-nhap-mon-toi-uu.md).
