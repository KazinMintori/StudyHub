---
course: toan-cho-ai
lecture: bai-06-phuong-phap-thich-nghi
section: lecture
title: "Các phương pháp tối ưu trong học sâu"
prerequisites: ["gradient", "hessian", "ky-vong", "phuong-sai"]
lessonStatus: ready
description: "Tính trạng thái AdaGrad, RMSProp và Adam; đối chiếu Newton, gradient liên hợp và BFGS; thiết kế phép so sánh."
---

Các tọa độ của gradient có thể khác nhau rất nhiều về độ lớn. Nếu dùng cùng một tốc độ học cho mọi tọa độ, bước cập nhật có thể quá lớn theo một hướng nhưng lại quá nhỏ theo hướng khác. AdaGrad, RMSProp và Adam lưu các thống kê của gradient để điều chỉnh thang cập nhật theo từng tọa độ. Newton, conjugate gradient và BFGS khai thác thông tin về độ cong theo những cách khác.

Sau khi học xong, bạn sẽ tính được trạng thái của Adam trong hai bước đầu, phân biệt được tổng tích lũy với trung bình mũ, và nêu được giới hạn của một mô phỏng nhỏ khi so sánh các thuật toán tối ưu.

Lần đọc đầu nên tập trung vào mục 1–3 và tự tính lại bảng hai bước Adam. Mục 4–5 dành cho các phương pháp dùng độ cong và có thể học sau. Mục 6 giải thích cách tổ chức một phép so sánh có ý nghĩa. Trong mục 1–3, mọi phép bình phương, căn và chia giữa các vector đều được thực hiện theo từng tọa độ, không phải phép nhân ma trận.

## 1. AdaGrad và tổng bình phương gradient

Với gradient $g_t$ ở bước $t$, trạng thái $s_0=0$, AdaGrad dùng

$$s_t=s_{t-1}+g_t\odot g_t,\qquad
\theta_{t+1}=\theta_t-\eta\frac{g_t}{\sqrt{s_t}+\varepsilon}.$$

$\odot$ là phép nhân theo từng tọa độ; $\varepsilon>0$ ngăn mẫu số bằng 0. Công thức ở đây đặt epsilon bên ngoài dấu căn, đúng với đoạn mã minh họa. Khi đối chiếu với một thư viện, cần xem epsilon nằm trong hay ngoài căn trước khi so từng con số.

Một tọa độ nhận gradient lớn nhiều lần sẽ có $s_t$ lớn, nên hệ số hiệu dụng $\eta/(\sqrt{s_t}+\varepsilon)$ giảm. $s_t$ không quên các bước cũ. Điều này có thể làm bước quá nhỏ về sau nếu bình phương gradient tiếp tục tích lũy; không phải bảo đảm thuật toán kém trên mọi bài toán.

::: example Chỉ xét một tọa độ
Cho chuỗi gradient thử $g_1=2$, $g_2=2$, $\eta=0.1$. Bỏ epsilon chỉ trong phép tính tay vì mẫu số ở đây khác 0:

$s_1=4$, độ dời thứ nhất $-0.1$.

$s_2=8$, độ dời thứ hai $-0.1/\sqrt2\approx-0.07071$.

Chuỗi gradient này chỉ dùng để đối chiếu công thức; nó không phải kết quả của một quá trình huấn luyện thực.
:::

## 2. RMSProp và trung bình mũ của bình phương gradient

Thay tổng tích lũy bằng **trung bình mũ**:

$$v_t=\beta v_{t-1}+(1-\beta)g_t\odot g_t,\qquad
\theta_{t+1}=\theta_t-\eta\frac{g_t}{\sqrt{v_t}+\varepsilon},\quad0\le\beta<1.$$

Một gradient bình phương xuất hiện cách hiện tại $k$ bước có trọng số $(1-\beta)\beta^k$, nên ảnh hưởng của dữ liệu cũ giảm dần theo thời gian. $v_t$ không phải phương sai vì biểu thức không trừ giá trị trung bình; trong tài liệu tiếng Anh, đại lượng này được gọi là *uncentered second moment*.

Với $v_0=0$, $g_1=2$, $\beta=0.9$, ta được $v_1=0.4$. Nếu $\eta=0.1$ và epsilon rất nhỏ, độ dời xấp xỉ $-0.31623$. Bước đầu có thể lớn hơn bước của AdaGrad vì trạng thái $v_1$ vẫn còn nhỏ. Công thức RMSProp dùng trong bài không hiệu chỉnh ảnh hưởng của việc khởi tạo trạng thái bằng 0; Adam ở mục tiếp theo có bước hiệu chỉnh này.

<details><summary>Thử trả lời: Nếu gradient ở bước sau bằng 0 thì v có trở về 0 ngay không?</summary>

Không khi $0<\beta<1$ và $v$ cũ khác 0. Nó trở thành $\beta v$ cũ. Với $\beta=0$, chỉ gradient hiện tại quyết định trạng thái.

</details>

## 3. Adam và hai trung bình mũ

Khởi tạo $m_0=v_0=0$, đếm bước $t=1,2,\ldots$:

$$\begin{aligned}
m_t&=\beta_1m_{t-1}+(1-\beta_1)g_t,\\
v_t&=\beta_2v_{t-1}+(1-\beta_2)g_t\odot g_t,\\
\widehat m_t&=m_t/(1-\beta_1^t),\\
\widehat v_t&=v_t/(1-\beta_2^t),\\
\theta_{t+1}&=\theta_t-\eta\widehat m_t/(\sqrt{\widehat v_t}+\varepsilon).
\end{aligned}$$

$0\le\beta_1,\beta_2<1$, $\varepsilon>0$. $m$ theo dõi gradient có dấu, $v$ theo dõi bình phương không âm. Không đổi $v_t$ thành $m_t^2$; trung bình bình phương khác bình phương trung bình.

### 3.1 Lý do phải hiệu chỉnh trạng thái ban đầu

Nếu gradient giả sử giữ bằng một số cố định $g$, trung bình mũ khởi tạo 0 cho $m_t=(1-\beta_1^t)g$. Chia cho tổng trọng số $1-\beta_1^t$ đưa kết quả về $g$. Với gradient biến thiên, đây là trung bình có trọng số được chuẩn hóa; không khẳng định nó là một ước lượng không chệch của gradient tại tham số hiện tại, vì tham số và phân phối gradient cũng đổi.

### 3.2 Tính hai bước đầu bằng tay

Cho chuỗi thử $g_1=2$, $g_2=1$, $\beta_1=0.9$, $\beta_2=0.999$:

| Trạng thái | Bước 1 | Bước 2 |
| --- | ---: | ---: |
| $m_t$ | 0.2 | 0.28 |
| $v_t$ | 0.004 | 0.004996 |
| $\widehat m_t$ | 2 | $28/19\approx1.47368$ |
| $\widehat v_t$ | 4 | $4996/1999\approx2.49925$ |

Với $\eta=0.1$ và epsilon rất nhỏ, độ dời thứ nhất gần $-0.1$, còn độ dời thứ hai gần $-0.09322$. Thứ tự tính là: lấy gradient, cập nhật hai trung bình mũ, hiệu chỉnh theo đúng số bước, rồi mới cập nhật tham số. Nếu đặt lại hai trạng thái nhưng vẫn giữ bộ đếm cũ, bước tiếp theo sẽ không còn tuân theo công thức Adam ở trên.

<MathLab type="optimizer" initial-method="adam">

```js
m = beta1*m + (1-beta1)*g;
v = beta2*v + (1-beta2)*g*g;
const mHat = m/(1-beta1**t), vHat = v/(1-beta2**t);
theta -= rate*mHat/(Math.sqrt(vHat)+epsilon);
```

</MathLab>

Mô phỏng dùng cùng một điểm đầu và cùng một hàm toàn phương để đối chiếu các phép cập nhật. Mở “Trạng thái thuật toán” để xem hai trung bình mũ được tính ở từng bước. Khi tốc độ học, $\kappa$ hoặc phương pháp thay đổi, mô phỏng sẽ đặt lại trạng thái. Mô phỏng này dùng gradient chính xác, không có nhiễu do lấy mẫu.

Adam không tạo ra chứng nhận KKT, không bảo đảm tốt nhất trên mọi bộ dữ liệu, và không làm cho hàm mất mát của mạng sâu trở thành hàm lồi. Mọi định lý hội tụ chỉ áp dụng khi các giả thiết tương ứng được thỏa mãn; tên của thuật toán tự nó không phải một bảo đảm.

## 4. Giải hệ Newton bằng conjugate gradient

Ở Bài 04, Newton giải $Hd=-g$. Lập và lưu Hessian dày $n\times n$ tốn bậc $n^2$ phần tử. Một lựa chọn là dùng phép nhân $Hv$ mà không lưu toàn ma trận, rồi giải hệ bằng thuật toán lặp.

**Gradient liên hợp tuyến tính (conjugate gradient, CG)** giải $Hz=b$ với $H$ đối xứng dương xác định. Đây là bài giải hệ; để dùng nó cho Newton phải đặt $b=-g$. Khởi tạo $z_0$, phần dư $r_0=b-Hz_0$, hướng $p_0=r_0$:

$$\begin{aligned}
\alpha_k&=\frac{r_k^Tr_k}{p_k^THp_k},&z_{k+1}&=z_k+\alpha_kp_k,\\
r_{k+1}&=r_k-\alpha_kHp_k,&\gamma_k&=\frac{r_{k+1}^Tr_{k+1}}{r_k^Tr_k},\\
p_{k+1}&=r_{k+1}+\gamma_kp_k.
\end{aligned}$$

Nếu phần dư đã 0 thì dừng trước phép chia. SPD đảm bảo mẫu $p_k^THp_k>0$ với hướng khác 0. Trong số học chính xác, CG giải hệ SPD $n$ chiều trong nhiều nhất $n$ bước; với số học máy, phần dư và làm tròn cần được theo dõi.

::: example Hai bước cho hệ hai chiều
Cho $H=\operatorname{diag}(1,2)$, $b=(1,1)$, $z_0=0$. Khi đó $r_0=p_0=(1,1)$.

$\alpha_0=2/3$, $z_1=(2/3,2/3)$, $r_1=(1/3,-1/3)$.

$\gamma_0=1/9$, $p_1=(4/9,-2/9)$, $\alpha_1=3/4$. Điểm mới $z_2=(1,1/2)$, thỏa $Hz_2=b$. Các hướng khác nhau nhưng $p_0^THp_1=0$, nên được gọi là liên hợp theo $H$.
:::

Không đồng nhất CG tuyến tính trên với CG phi tuyến dùng tìm kiếm đường cho mục tiêu tổng quát. Với Hessian bất định của mạng sâu, giả thiết SPD của phép giải hệ này phải được xử lý trước.

## 5. BFGS và điều kiện secant

Gọi $s_k=\theta_{k+1}-\theta_k$, $y_k=g_{k+1}-g_k$. $s$ là độ dời; $y$ là đổi gradient. Với một hàm toàn phương có Hessian $H$, ta có $y_k=Hs_k$, nên $H^{-1}y_k=s_k$ nếu $H$ khả nghịch. BFGS giữ quan hệ ấy trên cặp vừa quan sát: một xấp xỉ Hessian nghịch đảo $M$ được cập nhật để thỏa **điều kiện secant** $M_{k+1}y_k=s_k$.

Với $y_k^Ts_k>0$, đặt $\rho_k=1/(y_k^Ts_k)$. Công thức BFGS nghịch đảo là

$$M_{k+1}=(I-\rho_ks_ky_k^T)M_k(I-\rho_ky_ks_k^T)+\rho_ks_ks_k^T.$$

Nếu $M_k\succ0$ và điều kiện độ cong dương đúng, cập nhật giữ tính dương xác định. Khi $y^Ts$ bằng 0 hoặc âm, không chia tiếp như thể đã đủ giả thiết; phần cài đặt phải bỏ hoặc sửa cập nhật. Hướng là $d=-M_kg_k$, rồi mới tìm độ dài bước.

Trong ví dụ tự đặt $M_0=I$, $s=(1,0)$, $y=(2,0)$, ta có $\rho=1/2$ và $M_1=\operatorname{diag}(1/2,1)$. Nhân trực tiếp cho $M_1y=s$, đúng với điều kiện secant. Lưu một ma trận dày cần bộ nhớ bậc $n^2$; L-BFGS chỉ giữ một số cặp $(s,y)$ gần đây để tính hướng mà không lưu toàn bộ ma trận. Nếu gradient được ước lượng từ lô nhỏ, nhiễu trong hiệu $y$ cũng phải được xét.

## 6. So sánh các phương pháp tối ưu

Một phép so sánh có ý nghĩa phải giữ nguyên mô hình, dữ liệu, điểm khởi tạo, hạt giống ngẫu nhiên và ngân sách tính toán. Siêu tham số của mỗi phương pháp cần được chọn theo cùng một quy tắc trên tập xác thực. Số bước, số lượt đi qua dữ liệu và thời gian phải được báo riêng, vì chi phí của một bước Newton khác nhiều so với một bước SGD.

Tối thiểu cần lưu hàm mất mát trên tập huấn luyện, hàm mất mát trên tập xác thực, tốc độ học, kích thước lô và tiêu chí dừng. Khi tiếp tục một bộ tối ưu có trạng thái, phải lưu cả các trung bình mũ hoặc vận tốc cùng bộ đếm bước. Nếu chỉ lưu tham số mô hình, lần chạy sau sẽ không tiếp nối đúng trạng thái của thuật toán.

Mô phỏng ở mục 3 giúp đọc công thức và phát hiện sai dấu hoặc sai bộ đếm. Nó chưa cho biết phương pháp nào tốt nhất trên một mạng sâu hoặc một phân phối dữ liệu thật. Muốn trả lời câu hỏi ấy cần thí nghiệm đúng điều kiện vừa nêu.

## Bài tập tự luyện

::: exercise 1. Bình phương trung bình khác gì trung bình bình phương?
Hai gradient là $2,-2$. Tính trung bình gradient và trung bình bình phương. Điều gì xảy ra nếu dùng bình phương trung bình thay cho v?
:::
::: solution
Trung bình gradient bằng 0, còn trung bình bình phương gradient bằng 4. Nếu bình phương giá trị trung bình, ta nhận 0 và làm mất hoàn toàn thông tin về độ lớn dao động. Vì vậy không thể thay trung bình của bình phương bằng bình phương của trung bình.
:::

::: exercise 2. Hiệu chỉnh bước đầu
Với gradient đầu $g_1=-3$, $\beta_1=0.9$, $\beta_2=0.999$, hãy tính hai trạng thái của Adam và xác định dấu của bước cập nhật.
:::
::: solution
$m_1=-0.3$, $v_1=0.009$, $\widehat m_1=-3$, $\widehat v_1=9$. Với tốc độ học dương, độ dời $-\eta(-3)/(3+\varepsilon)>0$. Dấu của gradient được giữ trong $m_1$, còn $v_1$ chỉ lưu bình phương nên không giữ dấu.
:::

::: exercise 3. Đừng đặt Newton bằng một phép chia tọa độ
Với $H=\begin{bmatrix}2&1\\1&2\end{bmatrix}$, $g=(1,0)$, giải $Hd=-g$ và so với việc chỉ chia theo đường chéo.
:::
::: solution
Giải $2d_1+d_2=-1$, $d_1+2d_2=0$ cho $d=(-2/3,1/3)$. Chia đường chéo cho $(-1/2,0)$ không thỏa hệ. Adam/RMSProp đổi thang theo tọa độ, không tương đương dùng Hessian nghịch đảo đầy đủ.
:::

## Tóm tắt

AdaGrad cộng dồn toàn bộ bình phương gradient; RMSProp thay tổng đó bằng một trung bình mũ; Adam dùng cả trung bình mũ của gradient và của bình phương gradient, kèm hiệu chỉnh lúc khởi đầu. Newton, conjugate gradient và BFGS khai thác độ cong theo những cơ chế khác. Muốn đọc đúng một thuật toán, phải theo dõi trạng thái và các điều kiện áp dụng. Một đường biểu diễn hàm mất mát đẹp trên mô hình nhỏ chưa đủ để chọn bộ tối ưu cho một mạng sâu.

## Nguồn và đọc thêm

- *Convex Optimization*, §9.5 (Newton), phụ lục C về giải hệ tuyến tính. Phụ lục này không dùng làm nguồn của công thức CG.
- Jonathan Shewchuk, [An Introduction to the Conjugate Gradient Method Without the Agonizing Pain](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf), §8 và thuật toán B2: nguồn bổ sung cho CG tuyến tính, cùng giả thiết SPD và cách theo dõi phần dư.
- Duchi, Hazan & Singer (2011), [Adaptive Subgradient Methods](https://jmlr.org/papers/v12/duchi11a.html): nguồn gốc phương pháp tích lũy thang theo tọa độ.
- Goodfellow, Bengio & Courville, [*Deep Learning*, §8.5–8.6](https://www.deeplearningbook.org/contents/optimization.html): RMSProp, Adam và các phương pháp dùng độ cong. Công thức BFGS được trình bày đầy đủ để người học xác minh điều kiện secant; ví dụ ma trận do người biên soạn tự đặt.
- Công thức BFGS và điều kiện giữ PD đối chiếu với Madeleine Udell, [Quasi-Newton Methods, ORIE 6326](https://web.stanford.edu/~udell/orie6326/lectures/quasinewton.pdf), phần BFGS inverse update và positive definiteness.
- Kingma & Ba, [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980), Algorithm 1: các moment và hiệu chỉnh bias. Bản minh họa dùng epsilon ngoài căn theo công thức này.
- Các chuỗi gradient, hệ hai chiều và bài tập là dữ liệu tự đặt, đã được kiểm tra lại bằng chương trình.

[Bài 05](./bai-05-toi-uu-huan-luyen.md) · [Bài 07 — LP và quy hoạch động](./bai-07-quy-hoach-tuyen-tinh-va-dong.md).
