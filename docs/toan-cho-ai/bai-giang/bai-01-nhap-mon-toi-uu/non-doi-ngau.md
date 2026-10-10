---
course: toan-cho-ai
lecture: bai-01-nhap-mon-toi-uu
topic: non-doi-ngau
section: topic
title: "Nón đối ngẫu và lựa chọn Pareto"
description: "Định nghĩa và hình học của nón đối ngẫu, các nón tự đối ngẫu, đối ngẫu của nón chuẩn và chuẩn đối ngẫu, các tính chất K** = K, bất đẳng thức đối ngẫu, và cách tìm phần tử tối thiểu bằng cực tiểu một tổng có trọng số."
---

Ở chủ đề trước, ta thấy một tập lồi đóng được mô tả hoàn toàn bởi các nửa không gian chứa nó. Với một **nón**, câu chuyện còn gọn hơn: Một nón lồi đóng được mô tả bởi các nửa không gian **có biên đi qua gốc** chứa nó. Mỗi nửa không gian như vậy có dạng $\{x : y^T x \ge 0\}$ và được xác định bởi một vector $y$. Tập tất cả những vector $y$ "nhìn" toàn bộ nón từ cùng một phía là một nón mới, gọi là **nón đối ngẫu**.

Nón đối ngẫu là cầu nối giữa hình học không gian tập lồi và lý thuyết đối ngẫu Lagrange. Nó cũng giải quyết một bài toán thực tế sâu sắc trong tối ưu hóa đa mục tiêu: Khi không tồn tại phương án duy nhất nào tối ưu trên mọi tiêu chí, làm thế nào để tìm được toàn bộ các phương án không bị chi phối (Pareto optimal)? Phương pháp tự nhiên là tổ hợp các tiêu chí với những trọng số dương, và cấu trúc nón đối ngẫu sẽ giải thích chính xác điều kiện bảo đảm tính đúng đắn của phương pháp này.

## 1. Định nghĩa và hình học

> **Định nghĩa.** Cho $K$ là một nón trong $\mathbb{R}^n$. Tập hợp
> $$K^* = \{y : x^T y \ge 0 \ \text{ với mọi } x \in K\}$$
> được gọi là **nón đối ngẫu** (dual cone) của $K$.

Mỗi vector $y \in K^*$ tạo với mọi vector thuộc $K$ một góc không vượt quá $90^\circ$. Đúng như tên gọi, $K^*$ là một nón, và nó **luôn luôn lồi và đóng, kể cả khi nón gốc $K$ không lồi**. Bản chất là vì: Với mỗi điểm $x \in K$ cố định, tập hợp $\{y : x^T y \ge 0\}$ là một nửa không gian đóng theo biến $y$, và $K^*$ chính là giao của vô số nửa không gian đóng xuất phát từ gốc tọa độ đó.

Ý nghĩa hình học trực quan của nón đối ngẫu được làm sáng tỏ như sau: Điểm $y \in K^*$ khi và chỉ khi nửa không gian $\{x : y^T x \ge 0\}$, với pháp tuyến hướng vào trong là $y$, chứa trọn vẹn nón $K$. Nói cách khác, $-y$ là vector pháp tuyến của một siêu phẳng tựa của nón $K$ tại gốc tọa độ. Trong mô phỏng dưới đây, vùng nhạt là nửa mặt phẳng $\{x : y^T x \ge 0\}$. Khi di chuyển vector $y$ quanh gốc tọa độ: Điểm $y$ thuộc vùng xanh $K^*$ chính xác khi nửa mặt phẳng nhạt bao trọn vẹn nón tím $K$.

<ConeLab type="dual" />

Một cách người ta hay dùng trong thực tế để tìm nón đối ngẫu của nón đa diện là kiểm tra trực tiếp trên các vector sinh. Nếu $K = \operatorname{cone}\{v_1, \ldots, v_k\}$ thì $y \in K^*$ khi và chỉ khi $y^T v_i \ge 0$ với mọi chỉ số $i = 1, \dots, k$, bởi vì mọi phần tử của $K$ đều là tổ hợp hình nón (tổ hợp tuyến tính với hệ số không âm) của các $v_i$. Chẳng hạn với $K = \operatorname{cone}\{(2, 1), (1, 3)\}$, ta xác định được:

$$
K^* = \{y : 2y_1 + y_2 \ge 0,\ y_1 + 3y_2 \ge 0\} = \operatorname{cone}\{(-1, 2),\ (3, -1)\}.
$$

Hai vector sinh của $K^*$ trực giao với hai vector sinh biên của $K$: Vector $(-1, 2)$ vuông góc với $(2, 1)$, còn vector $(3, -1)$ vuông góc với $(1, 3)$. Đây là quy tắc hình học mẫu mực trong mặt phẳng: Mỗi tia biên của $K^*$ vuông góc với một tia biên tương ứng của $K$, và hướng vào phía bên trong của $K$.

Từ đó dẫn tới một tính chất cốt lõi: **Nón càng mở rộng thì nón đối ngẫu càng thu hẹp**. Tổng quát hơn, nếu $K_1 \subseteq K_2$ thì $K_2^* \subseteq K_1^*$, bởi vì điều kiện tích vô hướng không âm trên toàn bộ $K_2$ chặt chẽ hơn nhiều so với trên tập con $K_1$. Tại hai trường hợp suy biến cực đoan: Nón chỉ gồm gốc tọa độ $\{0\}$ có đối ngẫu là toàn bộ không gian $\mathbb{R}^n$, còn toàn bộ không gian $\mathbb{R}^n$ có đối ngẫu chính là $\{0\}$.

## 2. Những nón tự đối ngẫu và cặp nón đối ngẫu quan trọng

- **Không gian con tuyến tính**: Đối ngẫu của một không gian con $V \subseteq \mathbb{R}^n$ chính là phần bù trực giao $V^\perp = \{y : v^T y = 0 \text{ với mọi } v \in V\}$. Thật vậy, nếu $y^T v \ge 0$ đúng với mọi $v \in V$, thì áp dụng cho cả vector đối $-v \in V$ ta suy ra $y^T (-v) \ge 0 \iff y^T v \le 0$, buộc $y^T v = 0$.
- **Góc phần tư không âm**: Ta có đẳng thức $(\mathbb{R}^n_+)^* = \mathbb{R}^n_+$. Một nón thỏa mãn $K^* = K$ được gọi là **nón tự đối ngẫu** (self-dual cone). Nếu $y \succeq 0$ thì rõ ràng $x^T y = \sum_{i=1}^n x_i y_i \ge 0$ với mọi $x \succeq 0$. Ngược lại, nếu $y \in (\mathbb{R}^n_+)^*$, lần lượt chọn $x = e_i$ (các vector cơ sở chính tắc) ta suy ra $y_i \ge 0$ với mọi $i$.
- **Nón ma trận nửa xác định dương (PSD)**: Trong không gian các ma trận đối xứng $\mathbb{S}^n$ trang bị tích vô hướng chuẩn Frobenius $\langle X, Y\rangle = \operatorname{tr}(XY) = \sum_{i,j} X_{ij} Y_{ij}$, nón $\mathbb{S}^n_+$ cũng là nón tự đối ngẫu: Điều kiện $\operatorname{tr}(XY) \ge 0$ với mọi $X \succeq 0$ tương đương với $Y \succeq 0$. Lập luận gồm hai chiều tường minh:
  - Chiều thuận: Giả sử $Y \not\succeq 0$, tức tồn tại vector $q \ne 0$ sao cho $q^T Y q < 0$. Chọn ma trận hạng một $X = qq^T \succeq 0$, ta tính được $\operatorname{tr}(XY) = \operatorname{tr}(q q^T Y) = q^T Y q < 0$, dẫn tới mâu thuẫn $Y \notin (\mathbb{S}^n_+)^*$. Các ma trận hạng một $qq^T$ đóng vai trò như những phép thử đầy uy lực.
  - Chiều nghịch: Nếu cả $X, Y \succeq 0$, ta khai triển phổ $X = \sum_{i=1}^n \lambda_i q_i q_i^T$ với các giá trị riêng $\lambda_i \ge 0$. Khi đó $\operatorname{tr}(XY) = \sum_{i=1}^n \lambda_i q_i^T Y q_i \ge 0$ vì từng số hạng đều không âm.
- **Nón chuẩn và chuẩn đối ngẫu**: Với một chuẩn tổng quát $\|\cdot\|$ trên $\mathbb{R}^n$, **chuẩn đối ngẫu** tương ứng được định nghĩa là $\|u\|_* = \sup\{u^T x : \|x\| \le 1\}$, đo độ dốc cực đại của dạng tuyến tính $u^T x$ trên hình cầu đơn vị. Ta chứng minh được rằng đối ngẫu của nón chuẩn $K = \{(x, t) : \|x\| \le t\}$ chính là nón sinh bởi chuẩn đối ngẫu:

  $$
  K^* = \{(u, v) : \|u\|_* \le v\}.
  $$

  Chuẩn Euclid $\|\cdot\|_2$ tự đối ngẫu với chính nó ($\|\cdot\|_{2, *} = \|\cdot\|_2$), do đó nón bậc hai (nón Lorentz) là nón tự đối ngẫu. Chuẩn $\|\cdot\|_1$ có đối ngẫu là $\|\cdot\|_\infty$ và ngược lại, vì $\sup\{u^T x : \|x\|_1 \le 1\} = \max_i |u_i|$, đạt được tại các đỉnh cực biên $\pm e_i$ của hình cầu $\ell_1$. Vì vậy nón chuẩn $\ell_1$ và nón chuẩn $\ell_\infty$ là cặp đối ngẫu của nhau, dù không nón nào tự đối ngẫu. Cặp đối ngẫu này giải thích trực quan cấu trúc hình học: Hình cầu $\ell_1$ có ít đỉnh nhưng nhiều diện (mặt), trong khi hình cầu $\ell_\infty$ có nhiều đỉnh nhưng ít diện, đỉnh của hình cầu này tương ứng với mặt của hình cầu kia.

## 3. Các tính chất đại số và giải tích của nón đối ngẫu

Hệ thống tính chất nền tảng của nón đối ngẫu bao gồm:

- $K^*$ luôn luôn đóng và lồi.
- Quan hệ bao hàm đảo chiều: Nếu $K_1 \subseteq K_2$ thì $K_2^* \subseteq K_1^*$.
- Nếu $K$ đặc ($\operatorname{int} K \ne \emptyset$) thì $K^*$ nhọn.
- Nếu bao đóng $\operatorname{cl} K$ nhọn thì $K^*$ đặc ($\operatorname{int} K^* \ne \emptyset$).
- Phép đối ngẫu cấp hai: Tập hợp $K^{**}$ là bao đóng của bao lồi của $K$, tức $K^{**} = \operatorname{cl}(\operatorname{conv} K)$. Đặc biệt, nếu $K$ lồi và đóng thì $K^{**} = K$.

Đẳng thức $K^{**} = K$ là phiên bản hình nón của định lý tách tập lồi: Một nón lồi đóng được xác định hoàn toàn bởi tập hợp các nửa không gian đóng qua gốc chứa nó. Kết hợp các tính chất trên: **Nếu $K$ là một nón chính quy thì nón đối ngẫu $K^*$ cũng là một nón chính quy, và $K^{**} = K$**. Tính đặc và tính nhọn hoán đổi vai trò cho nhau qua phép đối ngẫu. Khi kéo các vector sinh của $K$ mở rộng thành nửa mặt phẳng (mất tính nhọn), nón đối ngẫu $K^*$ co lại thành một tia (mất tính đặc).

## 4. Bất đẳng thức đối ngẫu: Chuyển đổi so sánh vector sang so sánh số thực

Khi $K$ là nón chính quy, nón đối ngẫu $K^*$ cũng sinh ra một quan hệ thứ tự bộ phận $\preceq_{K^*}$. Hai quan hệ thứ tự này gắn kết mật thiết qua các mệnh đề tương đương sau:

$$
x \preceq_K y \iff \lambda^T x \le \lambda^T y \quad \text{với mọi } \lambda \succeq_{K^*} 0,
$$

$$
x \prec_K y \iff \lambda^T x < \lambda^T y \quad \text{với mọi } \lambda \succeq_{K^*} 0,\ \lambda \ne 0.
$$

Ý nghĩa bản chất: Một bất đẳng thức giữa hai **vector** trong không gian nhiều chiều tương đương với vô số bất đẳng thức giữa các **số thực**, trong đó mỗi số thực ứng với một phép chiếu có trọng số $\lambda$ thuộc nón đối ngẫu. Với $K = \mathbb{R}^n_+$, điều này khẳng định $x \preceq y$ theo từng tọa độ khi và chỉ khi mọi tổ hợp tuyến tính với trọng số không âm của $x$ không vượt quá giá trị tương ứng của $y$. Với thứ tự ma trận, $X \preceq Y$ khi và chỉ khi $\operatorname{tr}(ZX) \le \operatorname{tr}(ZY)$ với mọi ma trận kiểm tra $Z \succeq 0$. Đây là công cụ toán học chủ đạo: Chuyển một điều kiện phức tạp trên vector hoặc ma trận thành một họ điều kiện đại số trên số thực.

Định lý về giải pháp thay thế (theorems of alternatives) cũng được mở rộng tự nhiên cho bất đẳng thức tổng quát: Hệ $Ax \prec_K b$ vô nghiệm khi và chỉ khi tồn tại vector $\lambda \ne 0$ thỏa mãn $\lambda \succeq_{K^*} 0$, $A^T \lambda = 0$ và $\lambda^T b \le 0$. Vai trò của các trọng số không âm giờ đây được đảm nhận bởi các phần tử của nón đối ngẫu.

## 5. Tìm phần tử tối thiểu bằng phương pháp vô hướng hóa

Trong các bài toán tối ưu nhiều mục tiêu, một tập hợp thường có vô số phần tử tối thiểu mà không có phần tử nhỏ nhất. Phương pháp toán học tiêu chuẩn để định vị các phần tử tối thiểu là: Lựa chọn một vector trọng số $\lambda$, rồi giải bài toán tối ưu đơn mục tiêu tìm cực tiểu của đại lượng vô hướng $\lambda^T z$ trên tập hợp $S$. Kỹ thuật này được gọi là **vô hướng hóa** (scalarization).

> **Mệnh đề (Điều kiện đủ của nghiệm tối thiểu).** Nếu $\lambda \succ_{K^*} 0$ và điểm $x \in S$ làm cực tiểu hóa hàm mục tiêu $\lambda^T z$ trên tập $S$, thì $x$ là một phần tử tối thiểu của $S$.

Chứng minh: Giả sử phản chứng $x$ không phải phần tử tối thiểu, tức tồn tại $z \in S$, $z \ne x$, thỏa mãn $z \preceq_K x$. Khi đó hiệu $x - z \in K \setminus \{0\}$. Vì $\lambda \in \operatorname{int} K^*$ (nằm trong phần trong của nón đối ngẫu), ta có tích vô hướng $\lambda^T(x - z) > 0$, dẫn tới $\lambda^T z < \lambda^T x$. Điều này mâu thuẫn trực tiếp với giả thiết $x$ là điểm cực tiểu của $\lambda^T z$ trên $S$. Lưu ý rằng kết quả này **không đòi hỏi tập hợp $S$ phải lồi**.

Với nón không âm $K = \mathbb{R}^n_+$, điều kiện $\lambda \succ_{K^*} 0$ tương đương với việc toàn bộ các trọng số $\lambda_i$ đều **dương ngặt**. Một cách giải thích rất trực quan trong kinh tế học và lý thuyết quyết định: Mỗi phương án sản xuất tiêu tốn một vector tài nguyên $x$ (lao động, năng lượng, nguyên liệu), $\lambda_i > 0$ là đơn giá thị trường của tài nguyên thứ $i$, và $\lambda^T x$ biểu diễn tổng chi phí sản xuất. Phương án đạt chi phí tối thiểu theo bất kỳ bảng giá dương ngặt nào chắc chắn là phương án **tối ưu Pareto**: Không thể giảm mức tiêu hao của một loại tài nguyên mà không làm tăng mức tiêu hao của ít nhất một loại tài nguyên khác.

<OrderLab type="pareto" />

Chiều ngược lại đòi hỏi lập luận giải tích cẩn trọng hơn, và có hai điểm mấu chốt cần lưu tâm:

- **Không phải mọi phần tử tối thiểu đều tìm được bằng trọng số dương ngặt**: Trong tập hợp hữu hạn (không lồi), một điểm có thể là tối thiểu nhưng lại nằm ở vùng "lõm vào" so với các điểm tối thiểu lân cận. Chẳng hạn xét tập ba điểm gồm $(2, 7)$, $(6, 3)$ và $(4, 5.4)$. Điểm $(4, 5.4)$ không bị điểm nào chi phối, nhưng nó lại bằng trung điểm của hai điểm kia cộng thêm độ lệch $(0, 0.4)$. Do đó với mọi vector trọng số dương $\lambda \succ 0$, giá trị $\lambda^T(4, 5.4)$ luôn lớn hơn trung bình cộng giá trị tại hai điểm còn lại, nghĩa là không bao giờ đạt giá trị nhỏ nhất. Không tồn tại bộ trọng số dương nào có thể phát hiện ra điểm này.
- **Khi $S$ lồi, chiều ngược được bảo đảm với trọng số không âm**: Nếu $S$ là tập lồi và $x$ là phần tử tối thiểu, thì luôn tồn tại vector $\lambda \succeq_{K^*} 0$, $\lambda \ne 0$, sao cho $x$ làm cực tiểu hóa $\lambda^T z$ trên $S$. Chứng minh sử dụng định lý siêu phẳng phân tách cho hai tập lồi không giao nhau là $(x - K) \setminus \{x\}$ và $S$. Tuy nhiên, vector trọng số tìm được có thể nằm trên **biên** của $K^*$ (tức có thành phần bằng 0), và không thể bảo đảm luôn dương ngặt. Ngược lại, một điểm cực tiểu hóa $\lambda^T z$ với $\lambda$ nằm trên biên của $K^*$ chưa chắc đã là phần tử tối thiểu.

Đối với **phần tử nhỏ nhất**, ta có một đặc trưng đại số thanh lịch: Điểm $x$ là phần tử nhỏ nhất của $S$ khi và chỉ khi với **mọi** vector trọng số $\lambda \succ_{K^*} 0$, $x$ là điểm cực tiểu **duy nhất** của $\lambda^T z$ trên $S$. Một phần tử nhỏ nhất luôn chiến thắng tuyệt đối dưới mọi thước đo giá dương.

Trong học máy hiện đại, vô hướng hóa là nền tảng của các bài toán tối ưu đa mục tiêu và điều chuẩn (regularization). Chẳng hạn, hàm mất mát huấn luyện thường được thiết lập dưới dạng tổng có trọng số giữa hàm mất mát dữ liệu và hàm phạt độ phức tạp mô hình: $\mathcal{L}(w) + \rho \mathcal{R}(w)$. Mỗi tham số điều chuẩn $\rho > 0$ ứng với một nghiệm trên biên Pareto giữa độ khớp dữ liệu và năng lực tổng quát hóa. Khi bài toán tối ưu là lồi (như trong Ridge Regression hay Support Vector Machines), việc quét tham số $\rho \ge 0$ cho phép tìm ra toàn bộ biên Pareto. Trái lại, trong các bài toán không lồi như huấn luyện mạng nơ-ron sâu, tồn tại những nghiệm Pareto mà phương pháp trọng số tuyến tính không thể tiếp cận được.

## 6. Những câu hỏi để đào sâu

**Câu 1.** Nón đối ngẫu của nửa mặt phẳng $\{x \in \mathbb{R}^2 : a^T x \ge 0\}$ là gì? Của một tia $\{t v : t \ge 0\}$ là gì?

<details><summary>Xem lời giải thích</summary>

Với nửa mặt phẳng $\{a^T x \ge 0\}$, chỉ các vector $y$ cùng phương dương với $a$ mới bảo đảm $y^T x \ge 0$ với mọi $x$ thuộc nửa mặt phẳng, do đó nón đối ngẫu là tia $\{t a : t \ge 0\}$. Với tia $\{t v : t \ge 0\}$, điều kiện đối ngẫu quy về $y^T v \ge 0$, do đó nón đối ngẫu là nửa mặt phẳng $\{y : v^T y \ge 0\}$. Hai ví dụ minh chứng hoàn hảo tính đối ngẫu hai lần $K^{**} = K$. Nửa mặt phẳng đặc nhưng không nhọn, đối ngẫu của nó là tia, nhọn nhưng không đặc.

</details>

**Câu 2.** Để kiểm tra một vector $y$ có thuộc $K^*$ hay không, việc thử nghiệm điều kiện $y^T x \ge 0$ trên một vài vector $x \in K$ có đủ không? Khi nào thì điều này trở nên chính xác?

<details><summary>Xem lời giải thích</summary>

Định nghĩa nón đối ngẫu đòi hỏi $y^T x \ge 0$ phải thỏa mãn với **mọi** $x \in K$, do đó thử nghiệm một số hữu hạn vector nói chung là không đủ. Tuy nhiên, nếu $K$ là một nón đa diện sinh bởi tập hữu hạn các vector $v_1, \ldots, v_k$, thì ta chỉ cần kiểm tra trên đúng các vector sinh đó, bởi vì $y^T(\sum_i \alpha_i v_i) = \sum_i \alpha_i y^T v_i \ge 0$ khi mọi $\alpha_i \ge 0$. Đối với nón ma trận nửa xác định dương $\mathbb{S}^n_+$, các phần tử sinh cực biên là vô số ma trận hạng một $qq^T$, vì vậy việc chứng minh đòi hỏi phân tích cấu trúc giải tích thay vì kiểm tra cơ học.

</details>

**Câu 3.** Trong mô hình bài toán kinh tế, nếu một loại tài nguyên được cung cấp miễn phí (đơn giá bằng 0), phương án đạt chi phí thấp nhất có chắc chắn là tối ưu Pareto hay không?

<details><summary>Xem lời giải thích</summary>

Không chắc chắn. Với vector giá có thành phần bằng 0, chẳng hạn $\lambda = (1, 0)$, mọi phương án sử dụng cùng lượng tài nguyên thứ nhất sẽ có tổng chi phí bằng nhau, bất kể mức tiêu hao tài nguyên thứ hai lãng phí đến mức nào. Chẳng hạn hai phương án $(2, 1)$ và $(2, 5)$ cùng cho chi phí bằng 2, nhưng phương án $(2, 5)$ bị phương án $(2, 1)$ chi phối hoàn toàn. Nếu thuật toán tối ưu chọn phương án $(2, 5)$ thì đó là một nghiệm không hiệu quả. Đây chính là lý do định lý vô hướng hóa bắt buộc vector trọng số phải nằm trong **phần trong** $\operatorname{int} K^*$, tức là mọi đơn giá đều phải dương ngặt.

</details>

## 7. Bài tập tự luyện

::: exercise 1. Tính một nón đối ngẫu
Tìm nón đối ngẫu của nón $K = \operatorname{cone}\{(1, 0), (1, 2)\}$ trong $\mathbb{R}^2$. Vector $y = (1, -0.4)$ có thuộc $K^*$ không?
:::

::: solution
Vector $y \in K^*$ khi và chỉ khi $y^T(1, 0) = y_1 \ge 0$ và $y^T(1, 2) = y_1 + 2y_2 \ge 0$. Từ đó ta xác định:

$$
K^* = \{y \in \mathbb{R}^2 : y_1 \ge 0,\ y_1 + 2y_2 \ge 0\} = \operatorname{cone}\{(0, 1), (2, -1)\}.
$$

Với vector $y = (1, -0.4)$: Ta có $y_1 = 1 \ge 0$ và $y_1 + 2y_2 = 1 - 0.8 = 0.2 \ge 0$, do đó $y \in K^*$.
:::

::: exercise 2. Chuẩn đối ngẫu
Cho vector $u = (3, -1, 2)$. Hãy tính $\|u\|_*$ khi chuẩn gốc là chuẩn $\ell_1$, và khi chuẩn gốc là chuẩn $\ell_\infty$. Xác định điểm cực biên $x$ đạt giá trị lớn nhất của $u^T x$ trong từng trường hợp.
:::

::: solution
Khi chuẩn gốc là $\|\cdot\|_1$, chuẩn đối ngẫu là $\|u\|_\infty = \max\{|3|, |-1|, |2|\} = 3$, đạt được tại đỉnh $x = e_1 = (1, 0, 0)^T$ của hình cầu $\ell_1$.

Khi chuẩn gốc là $\|\cdot\|_\infty$, chuẩn đối ngẫu là $\|u\|_1 = |3| + |-1| + |2| = 6$, đạt được tại đỉnh $x = (1, -1, 1)^T$ của hình lập phương đơn vị, với các tọa độ được chọn theo dấu $x_i = \operatorname{sign}(u_i)$.

Trong cả hai trường hợp, nghiệm tối ưu luôn đạt tại các đỉnh cực biên của hình cầu đơn vị tương ứng.
:::

::: exercise 3. Vô hướng hóa trên một tập hữu hạn
Cho tập hợp gồm các phương án $(2, 9)$, $(3, 6.5)$, $(5.5, 4)$, $(8, 3)$, $(6, 7)$, $(9, 8)$, với hai mục tiêu đều cần tối thiểu hóa. Hãy tìm toàn bộ phần tử tối thiểu. Với các vector trọng số $\lambda = (1, 0.2)$, $(1, 1)$ và $(0.3, 1)$, điểm nào làm cực tiểu hóa $\lambda^T z$? Kết quả với $\lambda = (1, 1)$ phản ánh hiện tượng gì?
:::

::: solution
Điểm $(6, 7)$ bị điểm $(5.5, 4)$ chi phối, điểm $(9, 8)$ bị chi phối bởi nhiều điểm khác trong tập. Do đó tập các phần tử tối thiểu Pareto gồm bốn điểm: $(2, 9)$, $(3, 6.5)$, $(5.5, 4)$, $(8, 3)$.

- Với $\lambda = (1, 0.2)$, giá trị $\lambda^T z$ tại các điểm lần lượt là $3.8,\ 4.3,\ 6.3,\ 8.6,\ 7.4,\ 10.6$, do đó điểm $(2, 9)$ được chọn.
- Với $\lambda = (1, 1)$, hai điểm $(3, 6.5)$ và $(5.5, 4)$ cùng đạt giá trị cực tiểu là $9.5$: Đường mức $z_1 + z_2 = 9.5$ tiếp xúc với toàn bộ đoạn thẳng nối hai điểm này, cho thấy bài toán vô hướng hóa có thể có đa nghiệm tối ưu cùng lúc.
- Với $\lambda = (0.3, 1)$, các giá trị tương ứng là $9.6,\ 7.4,\ 5.65,\ 5.4,\ 8.8,\ 10.7$, do đó điểm $(8, 3)$ được chọn.

Mọi nghiệm tìm được qua bài toán vô hướng hóa với vector trọng số dương ngặt đều là các phần tử tối thiểu Pareto hợp thức.
:::

## Tóm tắt

Nón đối ngẫu $K^*$ bao gồm toàn bộ các vector tạo góc không vượt quá $90^\circ$ với mọi vector thuộc $K$, tương ứng với các vector pháp tuyến của các nửa không gian đóng qua gốc chứa $K$. Nón đối ngẫu luôn luôn lồi và đóng. Quan hệ bao hàm bị đảo chiều: Nón càng rộng thì nón đối ngẫu càng hẹp. Khi $K$ là nón chính quy thì $K^*$ cũng là nón chính quy và thỏa mãn tính đối ngẫu hai lần $K^{**} = K$. Góc phần tư không âm, nón nửa xác định dương với tích vô hướng vết, và nón Lorentz là các nón tự đối ngẫu.

Quan hệ bất đẳng thức tổng quát giữa các vector tương đương với một họ vô hạn các bất đẳng thức số thực $\lambda^T x \le \lambda^T y$ với mọi $\lambda \in K^*$. Việc cực tiểu hóa tổng có trọng số $\lambda^T z$ với vector trọng số dương ngặt luôn sinh ra một phần tử tối thiểu Pareto. Khi tập hợp là lồi, mọi phần tử tối thiểu đều có thể biểu diễn qua một bài toán vô hướng hóa với vector trọng số không âm khác không.

## Tài liệu tham khảo
- Stephen Boyd, Lieven Vandenberghe, *Convex Optimization*, Cambridge University Press.

