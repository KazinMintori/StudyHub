---
course: toan-cho-ai
lecture: bai-00-on-tap-nen-tang
section: lecture
title: "Ôn tập nền tảng toán học cho AI"
prerequisites: ["ham-so", "dao-ham", "tap-hop"]
lessonStatus: ready
description: "Tính dự đoán bằng ma trận, gradient và độ cong; nối nhiễu Gauss với bình phương tối thiểu."
---

Khi một mô hình dự đoán chưa chính xác, ta cần biết tham số nào nên thay đổi và thay đổi theo chiều nào. Bài này ôn lại ba mảnh kiến thức sẽ được dùng xuyên suốt môn học. Phép nhân ma trận giúp viết đồng thời nhiều dự đoán; đạo hàm mô tả sự thay đổi của hàm mục tiêu; mô hình xác suất giải thích vì sao ta chọn một tiêu chuẩn sai số cụ thể. Các phép tính được thực hiện trên một bộ dữ liệu nhỏ tự đặt để bạn có thể theo dõi từng bước.

Sau khi học xong, bạn sẽ xác định được kích thước của các đại lượng trong phép nhân ma trận, tự tính gradient của hàm mất mát tổng bình phương, và suy ra tiêu chuẩn bình phương tối thiểu từ giả thiết rằng sai số quan sát tuân theo phân phối Gauss.

Ở lần đọc đầu, bạn nên học mục 1–2 để làm quen với ký hiệu ma trận và phần dư, rồi chuyển sang gradient và Hessian ở mục 3–4. Mục 5–6 giải thích mối liên hệ giữa mô hình nhiễu và bài toán bình phương tối thiểu; có thể để lại cho lượt đọc thứ hai nếu phần xác suất còn mới. Nếu hàm số hoặc đạo hàm một biến chưa vững, hãy mở tab Kiến thức nền trước khi bắt đầu. Thuật ngữ có gạch chấm mở một ghi chú ngắn ngay trên trang.

## 1. Viết nhiều dự đoán bằng một phép nhân ma trận

Giả sử ta thử mô hình một tham số $\widehat b_i=a_iw$. Dữ liệu minh họa là:

| Quan sát $i$ | Đầu vào $a_i$ | Đầu ra $b_i$ |
| --- | ---: | ---: |
| 1 | 1 | 1 |
| 2 | 2 | 2 |
| 3 | 3 | 2 |

$a_i,b_i$ là dữ liệu cố định. $w$ là số ta được chọn. Với $w=1$, ba dự đoán là $1,2,3$; dự đoán cuối vượt đầu ra quan sát một đơn vị.

Gom ba đầu vào thành ma trận một cột và ba đầu ra thành vector:

$$
A=\begin{bmatrix}1\\2\\3\end{bmatrix},\quad
b=\begin{bmatrix}1\\2\\2\end{bmatrix},\quad
\widehat b=Aw,\quad r=Aw-b.
$$

**Vector** là danh sách có thứ tự; ở đây mỗi thành phần tương ứng một quan sát. **Ma trận** là bảng số; $A$ có ba hàng và một cột. Vector $r$ là phần dư. Ta thống nhất dấu phần dư là dự đoán trừ quan sát; nếu đổi dấu, phải đổi nhất quán khi tính gradient.

Với $m$ quan sát và $n$ đặc trưng, $A\in\mathbb R^{m\times n}$, $w\in\mathbb R^n$, $b,r\in\mathbb R^m$. Ký hiệu $\mathbb R^n$ chỉ các vector gồm $n$ số thực. Một hàng của $A$ dùng các đặc trưng của một quan sát để tính một dự đoán.

<details><summary>Thử trả lời: Nếu A có 5 hàng và 2 cột thì w và Aw có bao nhiêu thành phần?</summary>

$w$ có 2 thành phần để khớp 2 cột. $Aw$ có 5 thành phần, mỗi thành phần đến từ một hàng.

</details>

## 2. Tích vô hướng, chuẩn và độ lớn của phần dư

Với hai vector cùng số chiều,

$$u^Tv=\sum_{j=1}^n u_jv_j,\qquad
\|u\|_2=\sqrt{u^Tu}.
$$

$T$ là chuyển vị: vector cột thành vector hàng. Ký hiệu $\sum$ yêu cầu cộng các số hạng theo chỉ số. Tích vô hướng $u^Tv$ cho một số, còn $uv^T$ cho một ma trận. Không được hoán đổi hai biểu thức này.

Ta dùng **hàm mất mát** (loss function)

$$f(w)=\frac12\|Aw-b\|_2^2=\frac12\sum_{i=1}^m r_i^2.$$

Bình phương làm cho phần dư âm và phần dư dương đều đóng góp một lượng không âm vào hàm mất mát. Hệ số $1/2$ chỉ làm công thức đạo hàm gọn hơn; nó không làm thay đổi điểm cực tiểu.

::: example So sánh hai giá trị của tham số
Với $w=1$, $r=(0,0,1)^T$, nên $f(1)=1/2$.

Với $w=1/2$, $r=(-1/2,-1,-1/2)^T$, nên $f(1/2)=3/4$. Theo hàm mất mát đã chọn, $w=1$ cho giá trị nhỏ hơn $w=1/2$. Phép so sánh này mới xét hai giá trị của $w$, nên chưa chứng minh $w=1$ là lựa chọn tốt nhất trong mọi trường hợp.
:::

Hai chuẩn khác cũng gặp trong môn:

$$\|u\|_1=\sum_j|u_j|,\qquad \|u\|_\infty=\max_j|u_j|.$$

Với $u=(3,-4)$, ba chuẩn lần lượt là $7,5,4$. Mỗi chuẩn đo độ lớn theo một quy tắc khác nhau. Khi đọc $\|r\|$, cần biết đang dùng chuẩn nào.

## 3. Gradient của hàm mất mát tổng bình phương

Đạo hàm một biến $f'(w)$ cho độ thay đổi bậc nhất: với độ dời nhỏ $d$, $f(w+d)\approx f(w)+f'(w)d$. Với nhiều biến, ta gom các đạo hàm riêng thành gradient:

$$\nabla f(w)=\begin{bmatrix}\partial f/\partial w_1\\\vdots\\\partial f/\partial w_n\end{bmatrix}.$$

Khi lấy đạo hàm riêng theo $w_j$, các biến còn lại được giữ cố định. Do $r_i=\sum_j A_{ij}w_j-b_i$, ta có $\partial r_i/\partial w_j=A_{ij}$. Dùng quy tắc chuỗi:

$$
\frac{\partial f}{\partial w_j}
=\sum_i r_i\frac{\partial r_i}{\partial w_j}
=\sum_i A_{ij}r_i.
$$

Đây là thành phần thứ $j$ của $A^Tr$, nên

$$\boxed{\nabla f(w)=A^T(Aw-b).}$$

Đối chiếu kích thước cho thấy $A^T$ có $n$ hàng và $m$ cột; nhân với phần dư $m$ chiều sẽ cho gradient $n$ chiều. Kết quả này phù hợp với yêu cầu rằng gradient phải có cùng số thành phần với vector tham số.

::: example Giải mô hình một tham số
Với dữ liệu đang dùng,

$$f(w)=\frac12[(w-1)^2+(2w-2)^2+(3w-2)^2],$$

$$f'(w)=14w-11.$$

Đặt $f'(w)=0$ cho $w^*=11/14$. Dự đoán là $(11/14,11/7,33/14)$; phần dư là $(-3/14,-3/7,5/14)$. Ta được $f(w^*)=5/28$, nhỏ hơn $1/2$.

Vì sao điểm dừng này là điểm cực tiểu? Mục kế tiếp sẽ xét độ cong; chỉ giải phương trình đạo hàm bằng 0 chưa đủ để kết luận đối với một hàm bất kỳ.
:::

<details><summary>Thử trả lời: Tại w=1, đạo hàm dương hay âm? Muốn làm hàm mất mát giảm trong một lân cận nhỏ thì nên tăng hay giảm w?</summary>

$f'(1)=3>0$. Chọn độ dời âm đủ nhỏ làm $f'(1)d<0$, nên giảm $w$ là hướng giảm cục bộ.

</details>

## 4. Hessian và độ cong theo một hướng

**Hessian** $H=\nabla^2 f(w)$ là ma trận đạo hàm bậc hai. Nếu $f$ có đạo hàm bậc hai liên tục, $H$ đối xứng. Xấp xỉ bậc hai là

$$f(w+d)\approx f(w)+\nabla f(w)^Td+\frac12d^THd.$$

$d^THd$ mô tả độ cong theo hướng $d$. Với hàm mất mát tổng bình phương,

$$H=A^TA,\qquad d^THd=(Ad)^T(Ad)=\|Ad\|_2^2\ge0.$$

Ta gọi ma trận đối xứng có dạng toàn phương không âm với mọi $d$ là **nửa xác định dương**, viết $H\succeq0$. Nếu dạng toàn phương dương với mọi $d\ne0$, ma trận **dương xác định**, viết $H\succ0$.

Trong ví dụ, $H=14>0$. Khai triển quanh $w^*=11/14$ cho

$$f(w)=\frac5{28}+7\left(w-\frac{11}{14}\right)^2.$$

Số hạng cuối không âm và chỉ bằng 0 tại $w^*$; vì vậy nghiệm duy nhất đã được chứng minh.

Dấu của từng phần tử không đủ để xác định một ma trận có PSD hay không. Ma trận $\begin{bmatrix}1&2\\2&1\end{bmatrix}$ có toàn phần tử dương nhưng với $d=(1,-1)$, ta được $d^THd=-2$. Ngược lại, $\begin{bmatrix}1&-1\\-1&1\end{bmatrix}$ có phần tử âm nhưng $d^THd=(d_1-d_2)^2\ge0$.

Trước khi đọc tiếp, hãy thử giải thích vì sao $A^TA$ luôn PSD và vì sao PSD chưa bảo đảm PD. Gợi ý: nếu $Ad=0$ với một $d\ne0$, độ cong theo hướng đó bằng 0.

## 5. Mật độ xác suất của biến Gauss

Với biến ngẫu nhiên liên tục $Z$ có mật độ $p(z)$, xác suất trên một khoảng là tích phân của mật độ:

$$P(a\le Z\le b)=\int_a^b p(z)\,dz.$$

$p(z)$ không phải xác suất tại đúng điểm $z$; với phân phối liên tục, xác suất của một điểm bằng 0. **Kỳ vọng** là trung bình theo phân phối, $\mathbb E[Z]=\int z p(z)dz$ khi tích phân tồn tại. **Phương sai** là $\mathbb E[(Z-\mathbb E[Z])^2]$.

Phân phối Gauss một biến, với $\sigma^2>0$, có mật độ

$$p(z)=\frac1{\sqrt{2\pi\sigma^2}}\exp\left[-\frac{(z-\mu)^2}{2\sigma^2}\right].$$

$\mu$ là kỳ vọng, $\sigma$ là độ lệch chuẩn. Nếu ba nhiễu độc lập, mật độ chung bằng tích ba mật độ. Độc lập là giả định thêm; không suy ra độc lập chỉ từ việc có nhiều biến.

Với vector Gauss $Z\in\mathbb R^m$, kỳ vọng $\mu$ và ma trận hiệp phương sai $\Sigma\succ0$,

$$p(z)=\frac{\exp[-\tfrac12(z-\mu)^T\Sigma^{-1}(z-\mu)]}{(2\pi)^{m/2}\sqrt{\det\Sigma}}.$$

Phần tử $\Sigma_{ij}$ đo hiệp phương sai giữa hai thành phần. $\Sigma^{-1}$ là ma trận nghịch đảo, thỏa $\Sigma\Sigma^{-1}=I$; $I$ có đường chéo bằng 1 và các phần tử còn lại bằng 0. $\det\Sigma$ là định thức: với ma trận hai chiều $\begin{bmatrix}a&c\\c&b\end{bmatrix}$, nó bằng $ab-c^2$ và dương khi ma trận PD. Trong công thức, định thức điều chỉnh hệ số để tổng mật độ bằng 1.

Với $\Sigma=\sigma^2I$, công thức tách thành các mật độ Gauss độc lập cùng phương sai. Công thức mật độ này không áp dụng trực tiếp nếu $\Sigma$ suy biến. Trong lần đọc đầu, bạn chỉ cần hiểu trường hợp $\sigma^2I$ để theo được mục 6; ma trận hiệp phương sai tổng quát phục vụ đọc thêm về nhiễu tương quan.

## 6. Suy ra bài toán bình phương tối thiểu từ mô hình nhiễu Gauss

Giả sử mô hình

$$b_i=a_i^Tw+\varepsilon_i,\qquad \varepsilon_i\overset{\text{độc lập}}\sim\mathcal N(0,\sigma^2),$$

trong đó $a_i^T$ là hàng thứ $i$ của $A$, và $\sigma^2$ được xem là đã biết. Trong phép ước lượng bằng **likelihood**, dữ liệu đã quan sát được giữ cố định, còn biểu thức mật độ được xem như một hàm của tham số $w$. Ta chọn $w$ sao cho dữ liệu đã quan sát có mật độ lớn nhất theo mô hình.

Lấy âm log tích mật độ:

$$-\log p(b\mid w)=\frac m2\log(2\pi\sigma^2)+\frac1{2\sigma^2}\|Aw-b\|_2^2.$$

Số hạng đầu không phụ thuộc $w$, còn hệ số $1/(2\sigma^2)$ luôn dương. Do đó, giá trị $w$ làm likelihood lớn nhất cũng chính là giá trị làm tổng bình phương phần dư nhỏ nhất. Kết luận này phụ thuộc vào mô hình nhiễu Gauss độc lập và cùng phương sai; nếu thay mô hình nhiễu, hàm mất mát thích hợp cũng có thể thay đổi.

Với nhiễu có ma trận hiệp phương sai cố định $\Sigma\succ0$, ta thu được hàm mất mát có trọng số $\tfrac12r^T\Sigma^{-1}r$. Khi các sai số được mô hình hóa với phương sai khác nhau, không thể tự động thay biểu thức này bằng tổng bình phương không trọng số.

## Bài tập tự luyện

Các bài dưới đây được tự biên soạn từ những thao tác vừa học.

::: exercise 1. Đọc phép nhân
$A=\begin{bmatrix}1&2\\0&1\end{bmatrix}$, $w=(2,-1)^T$, $b=(0,2)^T$. Tính dự đoán, phần dư và giá trị hàm mất mát $\tfrac12\|r\|_2^2$.
:::
::: solution
$Aw=(0,-1)^T$, $r=(0,-3)^T$, nên giá trị hàm mất mát bằng $9/2$. Phần dư có hai thành phần vì có hai quan sát.
:::

::: exercise 2. Theo một gradient
Với $A,w,b$ ở bài 1, tính $A^Tr$. Vì sao kết quả có hai thành phần?
:::
::: solution
$A^T=\begin{bmatrix}1&0\\2&1\end{bmatrix}$, nên $A^Tr=(0,-3)^T$. Hai thành phần tương ứng hai tham số. Nếu đổi dấu phần dư mà giữ công thức $A^Tr$, ta sẽ chọn sai hướng.
:::

::: exercise 3. Một hệ thiếu hạng
Mô hình chỉ dự đoán tổng $w_1+w_2$ cho đầu ra 1. Hàm mất mát là $\tfrac12(w_1+w_2-1)^2$. Bài toán có nghiệm duy nhất không?
:::
::: solution
Không. Mọi cặp $w_1+w_2=1$ đều cho giá trị hàm mất mát bằng 0. Hessian $\begin{bmatrix}1&1\\1&1\end{bmatrix}$ PSD nhưng không PD: dịch chuyển theo hướng $(1,-1)$ không làm dự đoán thay đổi. Ví dụ này chuẩn bị cho việc phân biệt lồi và lồi nghiêm ở Bài 01.
:::

## Tóm tắt

Ta đã viết các dự đoán dưới dạng $Aw$, đo độ lớn của phần dư bằng chuẩn và suy ra từng bước công thức $\nabla f=A^T(Aw-b)$. Hessian $A^TA$ mô tả độ cong của hàm mục tiêu. Dưới giả định nhiễu Gauss độc lập và cùng phương sai, cực đại likelihood dẫn đến bài toán cực tiểu tổng bình phương phần dư; giả định này không bắt buộc cho mọi bộ dữ liệu.

## Nguồn và đọc thêm

- Nguồn chính: Boyd & Vandenberghe, *Convex Optimization*, bản local `toan-cho-ai/docs/Convex_Optimization_Boyd.pdf`: §A.1 (tr. 633–636), §A.4–A.5 (tr. 640–651), §1.2.1 và §7.1 về ước lượng từ phân phối Gauss. Số trang là trang in trong sách; số trang PDF bằng trang in cộng 14.
- Koller & Friedman, *Probabilistic Graphical Models*, bản local cùng thư mục, là tài liệu tham khảo về phân phối chung và độc lập; không dùng phần scan không đọc chắc để suy ra công thức.
- Bộ dữ liệu, các phép tính và bài tập ở đây do người biên soạn đặt và đã được đối chiếu lại bằng chương trình.

Tiếp theo: [Bài 01 — Giới thiệu tối ưu, tập lồi và hàm lồi](./bai-01-nhap-mon-toi-uu.md).
