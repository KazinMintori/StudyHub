---
course: toan-cho-ai
lecture: bai-02-tap-loi
topic: bai-toan-tuong-duong
section: topic
title: "Bài toán tương đương và các phép biến đổi cơ bản"
description: "Khái niệm hai bài toán tương đương, phép co giãn, đổi biến, biến đổi đơn điệu hàm mục tiêu và ràng buộc, biến bù, dạng epigraph, ràng buộc ẩn và tường minh, những cách viết làm tính lồi hiện ra, và ranh giới giữa tương đương, nới lỏng và xấp xỉ."
---

Cùng một bài toán có thể được viết theo nhiều cách. Người này đo sai số bằng chuẩn Euclid, người kia đo bằng bình phương của nó. Người này tham số hóa độ lệch chuẩn bằng $\sigma$, người kia bằng $\log\sigma$. Trong khi đó, phần mềm giải tối ưu chỉ nhận một vài dạng nhất định, nên một phần lớn công việc của người lập mô hình là biến bài toán mình đang có thành bài toán mà công cụ giải được.

Mỗi phép biến đổi như thế đi kèm hai câu hỏi. Thứ nhất, lời giải có được bảo toàn không, nghĩa là từ nghiệm của bài toán mới có lấy lại được nghiệm của bài toán cũ không? Thứ hai, tính lồi có được bảo toàn không? Trang này cho thấy hai câu hỏi ấy độc lập với nhau: có những phép biến đổi giữ nguyên nghiệm nhưng phá hỏng tính lồi, và ngược lại, có những phép biến đổi làm tính lồi hiện ra từ một bài toán trông không lồi chút nào. Bạn cần nắm [dạng chuẩn của bài toán tối ưu](../bai-01-nhap-mon-toi-uu/bai-toan-toi-uu.md) và [bài toán lồi ở dạng chuẩn](../bai-01-nhap-mon-toi-uu/cuc-bo-va-toan-cuc.md) từ Lecture 01.

## 1. Hai bài toán tương đương

Ta tiếp cận khái niệm tương đương một cách trực quan và thực chất: Hai bài toán được gọi là **tương đương** nếu từ một nghiệm của bài toán này, ta dễ dàng tìm được một nghiệm của bài toán kia, và ngược lại. Thay vì sa đà vào các định nghĩa hình thức rườm rà, nhãn quan tương đương này giúp ta nhìn thấu bản chất biến đổi mô hình.

Ví dụ đơn giản nhất là phép co giãn. Nhân hàm mục tiêu và các hàm ràng buộc bất đẳng thức với những hằng số dương $\alpha_i > 0$, nhân các hàm ràng buộc đẳng thức với những hằng số khác không $\beta_i \ne 0$, ta được

$$
\begin{aligned}
\text{minimize}\quad & \alpha_0 f_0(x)\\
\text{subject to}\quad & \alpha_i f_i(x) \le 0, \quad i = 1, \ldots, m,\\
& \beta_i h_i(x) = 0, \quad i = 1, \ldots, p.
\end{aligned}
$$

Miền khả thi không thay đổi, vì $\alpha_i f_i(x)$ cùng dấu với $f_i(x)$, còn $\beta_i h_i(x) = 0$ khi và chỉ khi $h_i(x) = 0$. Một điểm tối ưu cho bài toán này cũng tối ưu cho bài toán kia. Thế nhưng hai bài toán không **giống nhau**: giá trị tối ưu bị nhân với $\alpha_0$, và các hàm đã là những hàm khác.

Khác biệt nhỏ ấy có hệ quả thật. Nhân hàm mục tiêu với 1000 không đổi nghiệm, nhưng làm gradient lớn lên 1000 lần, nên một thuật toán gradient với bước cố định có thể đang hội tụ bỗng phân kỳ. Sự phân biệt "tương đương nhưng không giống nhau" sẽ còn trở lại suốt trang này, vì hầu hết các phép biến đổi đều giữ nghiệm nhưng thay đổi một thứ khác: khi thì giá trị tối ưu, khi thì tính khả vi, khi thì chính tính lồi.

## 2. Đổi biến

Giả sử $\phi : \mathbb{R}^n \to \mathbb{R}^n$ là một ánh xạ một-một, và ảnh của nó phủ kín miền $\mathcal{D}$ của bài toán. Thay $x = \phi(z)$ vào mọi hàm, ta được các hàm mới $\tilde f_i(z) = f_i(\phi(z))$ và $\tilde h_i(z) = h_i(\phi(z))$, và một bài toán với biến $z$. Hai bài toán tương đương: nếu $x$ là nghiệm của bài toán gốc thì $z = \phi^{-1}(x)$ là nghiệm của bài toán mới, và nếu $z$ là nghiệm của bài toán mới thì $x = \phi(z)$ là nghiệm của bài toán gốc. Hai điều kiện đặt lên $\phi$ đều có lý do. Tính một-một bảo đảm mỗi $x$ ứng với đúng một $z$, còn điều kiện phủ miền bảo đảm không có điểm khả thi nào bị bỏ sót.

Điều đáng chú ý là phép đổi biến có thể làm tính lồi xuất hiện, hoặc làm nó biến mất. Hãy xét bài toán ước lượng độ lệch chuẩn $\sigma$ của một phân phối Gauss đã biết trung bình. Với $n$ quan sát và $S$ là tổng bình phương độ lệch của chúng so với trung bình, âm log-likelihood (bỏ đi hằng số) là

$$
f(\sigma) = n\log\sigma + \frac{S}{2\sigma^2}, \qquad \sigma > 0 .
$$

Đạo hàm cấp hai $f''(\sigma) = -\frac{n}{\sigma^2} + \frac{3S}{\sigma^4}$ âm khi $\sigma > \sqrt{3S/n}$, nên $f$ không phải hàm lồi. Với $n = 5$ và $S = 20$, hàm $f$ cong xuống trên cả khoảng $\sigma > \sqrt{12} \approx 3.46$. Bây giờ đặt $\sigma = e^s$, tức $s = \log\sigma$. Ánh xạ $s \mapsto e^s$ là một-một từ $\mathbb{R}$ lên $(0, \infty)$, đúng bằng miền của bài toán, và hàm mục tiêu mới là

$$
g(s) = f(e^s) = ns + \frac{S}{2}e^{-2s} .
$$

Lần này $g''(s) = 2Se^{-2s} > 0$ với mọi $s$, nên $g$ lồi. Phương trình $g'(s) = n - Se^{-2s} = 0$ cho $e^{2s} = S/n$, tức $\sigma^\star = \sqrt{S/n}$, đúng là ước lượng hợp lý cực đại quen thuộc của độ lệch chuẩn. Với số liệu trên, $\sigma^\star = 2$ và $s^\star = \log 2 \approx 0.693$, và hai bài toán có cùng giá trị tối ưu, khoảng 5.966, vì $f(e^s) = g(s)$ tại mọi điểm. Cách tham số hóa qua $\log\sigma$ vì thế rất tiện khi một mô hình phải học cả phương sai: ràng buộc $\sigma > 0$ biến mất, và trong ví dụ này, hàm mục tiêu còn trở nên lồi.

<EquivalenceLab />

Chiều ngược lại cũng xảy ra. Một phép đổi biến không affine có thể phá hỏng tính lồi của một bài toán vốn lồi, và Câu 2 ở cuối trang cho thấy nó còn có thể sinh ra những điểm dừng không hề có trong bài toán gốc. Vì thế khi đổi biến, ta luôn phải kiểm tra lại tính lồi trong biến mới, chứ không thừa hưởng nó từ biến cũ.

## 3. Biến đổi hàm mục tiêu và hàm ràng buộc

Thay vì đổi biến, ta có thể bọc từng hàm trong một hàm một biến. Giả sử $\psi_0$ tăng ngặt, mỗi $\psi_i$ với $i = 1, \ldots, m$ thỏa $\psi_i(u) \le 0$ khi và chỉ khi $u \le 0$, và mỗi $\psi_{m+i}$ thỏa $\psi_{m+i}(u) = 0$ khi và chỉ khi $u = 0$. Thay $f_i$ bằng $\psi_i \circ f_i$ và $h_i$ bằng $\psi_{m+i} \circ h_i$, ta được một bài toán có cùng miền khả thi và cùng tập nghiệm với bài toán gốc. Phép co giãn ở mục 1 chỉ là trường hợp riêng khi mọi $\psi_i$ tuyến tính.

Ví dụ 4.3 của sách so sánh hai bài toán: cực tiểu $\|Ax - b\|_2$ và cực tiểu $\|Ax - b\|_2^2$. Hàm $u \mapsto u^2$ tăng ngặt trên $[0, \infty)$, tập giá trị của chuẩn, nên hai bài toán có cùng nghiệm, còn giá trị tối ưu liên hệ bởi $p^\star_2 = (p^\star_1)^2$. Hai bài toán vẫn không giống nhau: hàm thứ nhất không khả vi tại những điểm có $Ax = b$, còn hàm thứ hai là một hàm toàn phương khả vi ở mọi nơi. Phép biến đổi quen thuộc nhất trong học máy cũng thuộc loại này: thay vì cực đại hóa hàm hợp lý của dữ liệu, ta cực tiểu hóa âm logarit của nó. Logarit tăng ngặt nên tập nghiệm không đổi, và tích của các mật độ biến thành một tổng, dễ lấy đạo hàm hơn nhiều.

Với ràng buộc, điều kiện đặt lên $\psi_i$ yếu hơn: nó chỉ cần giữ đúng dấu, không cần đơn điệu. Ràng buộc $x^3 \le 0$ chẳng hạn tương đương $x \le 0$, vì hàm căn bậc ba giữ dấu. Hàm $x^3$ không lồi trên $\mathbb{R}$, nên cách viết thứ nhất không phải dạng chuẩn lồi, còn cách viết thứ hai thì có. Ràng buộc $\|x\|_2 \le 1$ cũng có thể viết thành $\|x\|_2^2 \le 1$, và cách viết sau khả vi ở mọi nơi.

## 4. Biến bù

Một bất đẳng thức có thể được thay bằng một đẳng thức cộng thêm một điều kiện không âm: $f_i(x) \le 0$ khi và chỉ khi tồn tại $s_i \ge 0$ với $f_i(x) + s_i = 0$. Áp dụng cho mọi ràng buộc bất đẳng thức, ta được bài toán

$$
\begin{aligned}
\text{minimize}\quad & f_0(x)\\
\text{subject to}\quad & s_i \ge 0, \quad i = 1, \ldots, m,\\
& f_i(x) + s_i = 0, \quad i = 1, \ldots, m,\\
& h_i(x) = 0, \quad i = 1, \ldots, p,
\end{aligned}
$$

với biến $(x, s) \in \mathbb{R}^n \times \mathbb{R}^m$. Biến $s_i$ được gọi là **biến bù** (slack variable) của ràng buộc thứ $i$. Nó đo khoảng trống còn lại của ràng buộc, nên $s_i = 0$ đúng khi ràng buộc chặt. Hai bài toán tương đương theo cả hai chiều. Nếu $(x, s)$ khả thi cho bài toán mới thì $x$ khả thi cho bài toán gốc, vì $f_i(x) = -s_i \le 0$. Ngược lại, nếu $x$ khả thi cho bài toán gốc thì chọn $s_i = -f_i(x)$, ta được một điểm khả thi của bài toán mới với cùng giá trị mục tiêu.

Về tính lồi thì khác. Ràng buộc đẳng thức trong một bài toán lồi phải affine, nên phép thêm biến bù chỉ giữ tính lồi khi $f_i$ affine. Với một ràng buộc phi tuyến như $x^2 \le 1$, phép thêm biến bù cho $x^2 + s = 1$ và $s \ge 0$. Tập các cặp $(x, s)$ thỏa điều kiện này là cung parabol $s = 1 - x^2$ trên đoạn $[-1, 1]$: hai điểm $(-1, 0)$ và $(1, 0)$ thuộc tập, nhưng trung điểm $(0, 0)$ thì không, vì $0^2 + 0 \ne 1$. Bài toán mới tương đương bài toán cũ nhưng không lồi, dù hình chiếu của miền khả thi xuống trục $x$ vẫn là đoạn lồi $[-1, 1]$. Đây là lý do biến bù được dùng thoải mái trong quy hoạch tuyến tính, nơi mọi ràng buộc đều affine, nhưng hiếm khi được dùng cho ràng buộc phi tuyến.

## 5. Dạng epigraph

Bài toán gốc tương đương với bài toán

$$
\begin{aligned}
\text{minimize}\quad & t\\
\text{subject to}\quad & f_0(x) - t \le 0,\\
& f_i(x) \le 0, \quad i = 1, \ldots, m,\\
& h_i(x) = 0, \quad i = 1, \ldots, p,
\end{aligned}
$$

với biến $(x, t)$. Thật vậy, $(x, t)$ là nghiệm của bài toán này khi và chỉ khi $x$ là nghiệm của bài toán gốc và $t = f_0(x)$. Hình ảnh hình học rất gọn: ràng buộc $f_0(x) \le t$ nói rằng điểm $(x, t)$ nằm trong [epigraph](../bai-01-nhap-mon-toi-uu/epigraph-tap-muc-duoi-jensen.md) của $f_0$, và ta đang tìm **điểm thấp nhất của epigraph**, trong số những điểm có $x$ khả thi.

Nếu bài toán gốc lồi thì dạng epigraph cũng lồi: hàm mục tiêu $t$ tuyến tính, và hàm $f_0(x) - t$ lồi theo cặp $(x, t)$. Vì vậy người ta nói hàm mục tiêu tuyến tính là **phổ quát** cho tối ưu lồi: mọi bài toán lồi đều viết lại được với một hàm mục tiêu tuyến tính. Điều này đơn giản hóa cả lý thuyết lẫn thuật toán, vì một thuật toán chỉ cần xử lý mục tiêu tuyến tính và các ràng buộc lồi là đủ dùng cho mọi bài toán lồi.

Phép biến đổi này đặc biệt hữu ích khi hàm mục tiêu là một giá trị lớn nhất. Bài toán cực tiểu $\max_i f_i(x)$ tương đương cực tiểu $t$ với $f_i(x) \le t$ cho mọi $i$: điều kiện "giá trị lớn nhất không vượt quá $t$" được tách thành nhiều điều kiện đơn giản. Khi các $f_i$ affine, ta được một LP, và [bài toán khớp dữ liệu theo sai số tệ nhất](../bai-01-nhap-mon-toi-uu/hai-lop-bai-toan-kinh-dien.md) ở Lecture 01 chính là một trường hợp như vậy.

## 6. Ràng buộc ẩn và ràng buộc tường minh

Có một mẹo ký hiệu cho phép giấu mọi ràng buộc vào hàm mục tiêu. Định nghĩa $F(x) = f_0(x)$ khi $x$ khả thi và $F(x) = \infty$ trong trường hợp còn lại. Bài toán cực tiểu $F$ trông như không có ràng buộc, nhưng tất nhiên nó không dễ hơn chút nào. Thậm chí nó còn khó phân tích hơn: nếu $f_0$ khả vi với miền mở, thì $F$ thường không khả vi, vì miền của nó, tức miền khả thi, hiếm khi là tập mở.

Chiều ngược lại hữu ích hơn. Nhiều bài toán chứa những **ràng buộc ẩn** nằm trong miền xác định của hàm. Hàm $-\sum_i \log x_i$ ngầm đòi hỏi $x_i > 0$ với mọi $i$, và hàm mất mát entropy chéo ngầm đòi hỏi các xác suất dự đoán dương. Sách đưa ra một ví dụ khác: hàm bằng $x^Tx$ khi $Ax = b$ và bằng $\infty$ khi ngược lại. Bài toán cực tiểu hàm này không có ràng buộc, nhưng hàm mục tiêu không khả vi. Viết ràng buộc ra ngoài, ta được bài toán cực tiểu $x^Tx$ với $Ax = b$: có thêm một ràng buộc đẳng thức, nhưng mọi hàm đều khả vi. Nhận ra ràng buộc ẩn quan trọng cả khi chạy thuật toán: một bước lặp đi ra ngoài miền xác định sẽ cho giá trị vô nghĩa, và kỹ thuật tìm kiếm đường ở Lecture 04 phải kiểm tra điều đó trước tiên.

## 7. Viết lại để tính lồi hiện ra

Sách định nghĩa bài toán lồi một cách chặt: không chỉ cực tiểu một hàm lồi trên một tập lồi, mà miền khả thi phải được mô tả bằng các bất đẳng thức của hàm lồi và các đẳng thức affine. Chủ đề [cực tiểu cục bộ và toàn cục](../bai-01-nhap-mon-toi-uu/cuc-bo-va-toan-cuc.md) của Lecture 01 đã đưa ra ví dụ của sách, với ràng buộc $x_1/(1 + x_2^2) \le 0$ và $(x_1 + x_2)^2 = 0$: miền khả thi lồi, nhưng cách viết thì không. Các phép biến đổi ở trên chính là công cụ để sửa cách viết. Nhân ràng buộc thứ nhất với $1 + x_2^2 > 0$ cho $x_1 \le 0$, một phép co giãn bằng một hàm dương. Lấy căn bậc hai ở ràng buộc thứ hai cho $x_1 + x_2 = 0$, một phép biến đổi giữ nghiệm của phương trình.

Có hai giới hạn cần nhớ. Thứ nhất, khi chính miền khả thi không lồi, không cách viết nào giữ nguyên biến làm nó lồi được. Ràng buộc $x^2 \ge 1$ mô tả hai nửa đường thẳng rời nhau, và đó là một sự thật về tập hợp, không phải về cách viết. Thứ hai, lồi không có nghĩa là giải được: bài toán cực tiểu $-\log x$ với $x \ge 1$ là bài toán lồi ở dạng chuẩn, nhưng hàm mục tiêu giảm về $-\infty$ khi $x \to \infty$, nên bài toán không có nghiệm.

## 8. Tương đương, nới lỏng và xấp xỉ

Không phải phép biến đổi nào cũng tương đương, và hai loại phép biến đổi thường bị nhầm với tương đương là nới lỏng và xấp xỉ.

**Nới lỏng** mở rộng miền khả thi từ $C$ thành một tập lớn hơn $\widetilde C \supseteq C$, giữ nguyên hàm mục tiêu. Với bài toán cực tiểu, ta có

$$
\inf_{x \in \widetilde C} f(x) \le \inf_{x \in C} f(x),
$$

nên giá trị tối ưu của bài toán nới lỏng là một cận dưới cho bài toán gốc. Nghiệm của bài toán nới lỏng thì có thể không thỏa ràng buộc cũ. Chẳng hạn, bài toán cực tiểu $(x - 0.4)^2$ với $x \in \{0, 1\}$ có nghiệm $x = 0$ và giá trị $0.16$. Nới thành $0 \le x \le 1$, ta được nghiệm $x = 0.4$ với giá trị $0$. Cận dưới $0$ hợp lệ, nhưng $0.4$ không phải một quyết định khả thi của bài toán nhị phân. Làm tròn $0.4$ về $0$ cho một ứng viên khả thi với giá trị $0.16$, và cận dưới cùng ứng viên này kẹp giá trị tối ưu trong đoạn $[0, 0.16]$. Ở đây ứng viên tình cờ đạt đúng giá trị tối ưu, nhưng ta chỉ biết chắc điều đó khi đã liệt kê cả hai điểm.

**Xấp xỉ** thay một hàm bằng một hàm khác dễ tính hơn, chẳng hạn khai triển bậc nhất quanh một điểm. Một xấp xỉ chỉ có ích khi ta nói được hai hàm gần nhau ở đâu và sai số được đo bằng đại lượng nào. Bản thân chữ "xấp xỉ" không cho biết nó là cận trên hay cận dưới, nên không thể dùng nó để chứng nhận một nghiệm.

## 9. Những câu hỏi để đào sâu

**Câu 1.** Thay hàm mục tiêu $f_0$ bằng $\max\{f_0(x), 0\}$. Hàm $u \mapsto \max\{u, 0\}$ không giảm nhưng không tăng ngặt. Bài toán mới có còn tương đương bài toán cũ không?

<details><summary>Xem lời giải thích</summary>

Còn tùy giá trị tối ưu $p^\star$ của bài toán gốc. Nếu $p^\star > 0$ thì mọi điểm khả thi có $f_0(x) \ge p^\star > 0$, nên trên miền khả thi hai hàm mục tiêu trùng nhau và hai bài toán có cùng tập nghiệm. Nếu $p^\star < 0$ thì khác hẳn: mọi điểm khả thi có $f_0(x) \le 0$ đều cho giá trị $0$ trong bài toán mới, nên đều là nghiệm của nó. Những điểm này phần lớn không phải nghiệm của bài toán gốc. Từ một nghiệm của bài toán mới, ta không lấy lại được nghiệm của bài toán cũ, nên tương đương bị gãy ở một chiều. Điều kiện "tăng ngặt" của $\psi_0$ chính là để chặn hiện tượng các giá trị khác nhau bị dồn thành một.

</details>

**Câu 2.** Để bỏ ràng buộc $x \ge 0$ trong bài toán cực tiểu $(x - 1)^2$, một bạn đặt $x = z^2$ rồi cực tiểu $(z^2 - 1)^2$ trên toàn trục số. Cách làm này có đúng không, và nếu có vấn đề thì vấn đề nằm ở đâu?

<details><summary>Xem lời giải thích</summary>

Về nghiệm thì không sai: ánh xạ $z \mapsto z^2$ phủ kín $[0, \infty)$, hai nghiệm $z = \pm 1$ đều cho $x = 1$, đúng nghiệm của bài toán gốc. Ánh xạ không một-một, nhưng điều đó chỉ làm mỗi nghiệm có hai bản sao. Vấn đề nằm ở hình dạng của hàm mới. Hàm $h(z) = (z^2 - 1)^2$ có $h''(0) = -4 < 0$, nên không lồi, và nó có một điểm dừng tại $z = 0$, ứng với $x = 0$. Thế nhưng tại $x = 0$, bài toán gốc có đạo hàm $2(0 - 1) = -2 \ne 0$, nghĩa là $x = 0$ chẳng có gì đặc biệt. Phép đổi biến đã sinh ra một điểm dừng giả, và một thuật toán gradient xuất phát đúng tại $z = 0$ sẽ đứng yên ở đó mãi. Bài học: tương đương về nghiệm không kéo theo việc giữ được tính lồi, và phải kiểm tra lại tính lồi sau mỗi phép đổi biến không affine.

</details>

**Câu 3.** Ở mục 4, bài toán dùng biến bù cho ràng buộc $x^2 \le 1$ tương đương với bài toán gốc nhưng không lồi. Vậy "lồi" là tính chất của bài toán hay của cách viết?

<details><summary>Xem lời giải thích</summary>

Theo định nghĩa của sách, đó là tính chất của cách viết. Hai bài toán tương đương có cùng nghiệm, nhưng một cách viết có thể đáp ứng các điều kiện của dạng chuẩn lồi trong khi cách kia không. Điều này nghe như một chi tiết hình thức, nhưng nó phản ánh một sự thật thực tế. Các thuật toán và các định lý đều làm việc với một cách viết cụ thể, chẳng hạn định lý cực tiểu cục bộ là toàn cục cần hàm mục tiêu lồi theo đúng biến đang được tối ưu. Vì vậy nghệ thuật của mô hình hóa là tìm một cách viết tương đương mà tính lồi hiện rõ, chứ không chỉ tin rằng bài toán "về bản chất" là lồi.

</details>

**Câu 4.** Nhân hàm mục tiêu với 1000 làm phương pháp gradient với bước cố định hành xử khác hẳn. Phương pháp Newton thì sao?

<details><summary>Xem lời giải thích</summary>

Phương pháp Newton không bị ảnh hưởng. Bước Newton là $\Delta x = -\nabla^2 f(x)^{-1}\nabla f(x)$. Khi $f$ được nhân với $\alpha > 0$, cả gradient lẫn Hessian đều được nhân với $\alpha$, nên $\Delta x = -(\alpha \nabla^2 f)^{-1}(\alpha \nabla f)$ không đổi. Đây là một trường hợp nhỏ của tính bất biến của phương pháp Newton mà Lecture 04 sẽ khai thác: Newton không quan tâm hàm được đo bằng đơn vị nào, còn gradient thì có.

</details>

**Câu 5.** Bài toán cực tiểu $e^x$ trên $\mathbb{R}$ không đạt nghiệm. Viết nó ở dạng epigraph thì có đạt nghiệm không?

<details><summary>Xem lời giải thích</summary>

Không. Dạng epigraph là cực tiểu $t$ với $e^x \le t$. Mọi điểm khả thi có $t \ge e^x > 0$, và $t$ nhỏ tùy ý khi $x \to -\infty$, nên giá trị tối ưu là $0$ nhưng không đạt. Điều này đúng một cách tổng quát: vì mỗi nghiệm của bài toán này cho một nghiệm của bài toán kia, một phép biến đổi tương đương giữ nguyên cả việc có nghiệm hay không. Phép biến đổi chỉ đổi hình dạng của bài toán, không tạo ra nghiệm từ chỗ không có.

</details>

## 10. Bài tập tự luyện

::: exercise 1. Hai cách tham số hóa độ lệch chuẩn
Với $n = 4$ quan sát và tổng bình phương độ lệch $S = 36$, âm log-likelihood là $f(\sigma) = 4\log\sigma + 18/\sigma^2$. (a) Đặt $\sigma = e^s$, viết hàm mục tiêu theo $s$, chứng minh nó lồi và tìm nghiệm. (b) Đặt $\sigma = s^2$ với $s > 0$. Hàm mục tiêu theo $s$ có lồi không?
:::

::: hint
Ở câu (b), tính đạo hàm cấp hai rồi thử một giá trị $s$ lớn, chẳng hạn $s = 3$.
:::

::: solution
(a) $g(s) = 4s + 18e^{-2s}$, với $g''(s) = 72e^{-2s} > 0$, nên $g$ lồi. Giải $g'(s) = 4 - 36e^{-2s} = 0$ được $e^{2s} = 9$, tức $s^\star = \log 3$ và $\sigma^\star = 3$. (b) $G(s) = 8\log s + 18/s^4$, nên $G''(s) = -8/s^2 + 360/s^6$. Tại $s = 3$, ta có $G''(3) = -\tfrac{8}{9} + \tfrac{360}{729}$, khoảng $-0.395 < 0$, nên $G$ không lồi. Cả hai phép đổi biến đều bỏ được ràng buộc $\sigma > 0$ và cho cùng nghiệm $\sigma^\star = 3$, nhưng chỉ phép đổi biến qua hàm mũ làm bài toán trở nên lồi.
:::

::: exercise 2. Dạng epigraph của một giá trị lớn nhất
Viết bài toán cực tiểu $\max\{x^2,\ (x - 3)^2,\ 2 - x\}$ trên $\mathbb{R}$ ở dạng epigraph. Bài toán mới có lồi không? Tìm nghiệm và cho biết ràng buộc nào chặt.
:::

::: solution
Dạng epigraph là cực tiểu $t$ với $x^2 - t \le 0$, $(x - 3)^2 - t \le 0$ và $2 - x - t \le 0$, theo biến $(x, t)$. Ba hàm ràng buộc đều lồi theo $(x, t)$ và hàm mục tiêu tuyến tính, nên bài toán lồi. Hai parabol cắt nhau tại $x = 1.5$, nơi cả hai bằng $2.25$, còn $2 - x = 0.5$ nhỏ hơn. Bên trái $x = 1.5$, số hạng $(x - 3)^2$ lớn hơn và đang giảm, bên phải thì $x^2$ lớn hơn và đang tăng, nên nghiệm là $x^\star = 1.5$, $t^\star = 2.25$. Hai ràng buộc đầu chặt, ràng buộc thứ ba có biến bù $2.25 - 0.5 = 1.75$.
:::

::: exercise 3. Biến bù
Xét tập các điểm $x \in \mathbb{R}^2$ thỏa $x_1 + 2x_2 \le 4$ và $-x_1 + x_2 \le 1$. Dùng biến bù để mô tả tập này chỉ bằng đẳng thức và điều kiện không âm. Tính các biến bù tại $x = (1, 1)$ và tại $x = (0, 1)$, rồi cho biết ràng buộc nào chặt tại mỗi điểm.
:::

::: solution
Tập mới gồm các $(x, s)$ với $x_1 + 2x_2 + s_1 = 4$, $-x_1 + x_2 + s_2 = 1$, $s_1 \ge 0$, $s_2 \ge 0$, còn $x$ tự do. Tại $x = (1, 1)$: $s_1 = 4 - 3 = 1$ và $s_2 = 1 - 0 = 1$, không ràng buộc nào chặt. Tại $x = (0, 1)$: $s_1 = 4 - 2 = 2$ và $s_2 = 1 - 1 = 0$, nên ràng buộc thứ hai chặt. Biến bù bằng $0$ đúng khi ràng buộc tương ứng chặt.
:::

## Tóm tắt

Hai bài toán tương đương nếu nghiệm của bài toán này cho ngay nghiệm của bài toán kia và ngược lại. Các phép biến đổi cơ bản gồm co giãn, đổi biến một-một, bọc hàm mục tiêu trong một hàm tăng ngặt và bọc ràng buộc trong một hàm giữ dấu, thêm biến bù, chuyển sang dạng epigraph, và chuyển ràng buộc giữa dạng ẩn với dạng tường minh. Tất cả đều giữ nghiệm, nhưng có thể thay đổi giá trị tối ưu, tính khả vi hay tính lồi.

Tính lồi là tính chất của cách viết. Đổi biến qua hàm mũ có thể làm một bài toán không lồi trở thành lồi, còn đổi biến không affine hay thêm biến bù cho ràng buộc phi tuyến có thể làm mất tính lồi. Dạng epigraph thì luôn giữ tính lồi và cho thấy mọi bài toán lồi đều viết được với hàm mục tiêu tuyến tính. Cuối cùng, nới lỏng chỉ cho một cận, còn xấp xỉ chỉ có ích khi đo được sai số, nên cả hai đều không phải phép biến đổi tương đương.

## Nguồn và đọc thêm

- S. Boyd, L. Vandenberghe, *Convex Optimization*, §4.1.3 (tr. 130–135) về bài toán tương đương, đổi biến, biến bù, dạng epigraph và ràng buộc ẩn, Ví dụ 4.3. §4.2.1 (tr. 136–138) về bài toán lồi trừu tượng, §4.2.4 (tr. 142–144) về những phép biến đổi giữ tính lồi.
- Ví dụ đổi biến $\sigma = e^s$ cho âm log-likelihood Gauss, mô phỏng, ví dụ đổi biến $x = z^2$, ví dụ nới lỏng nhị phân, các câu hỏi và bài tập do người soạn bổ sung. Mọi con số đã được tính lại bằng chương trình.
