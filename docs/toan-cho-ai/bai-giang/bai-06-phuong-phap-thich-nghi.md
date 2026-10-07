---
course: toan-cho-ai
lecture: bai-06-phuong-phap-thich-nghi
section: lecture
title: "Các phương pháp tối ưu trong học sâu"
prerequisites: ["gradient", "hessian", "ky-vong", "phuong-sai"]
lessonStatus: ready
description: "Tính trạng thái AdaGrad, RMSProp và Adam; đối chiếu Newton, gradient liên hợp và BFGS; thiết kế phép so sánh."
---

Gradient của một tọa độ có thể liên tục lớn hơn tọa độ khác. Một tốc độ học chung không phản ánh sự khác biệt đó. Các phương pháp thích nghi giữ thống kê của gradient để đổi thang cập nhật; các phương pháp dùng độ cong giải quyết câu hỏi này theo cách khác.

Sau bài, bạn có thể tự tính các trạng thái của Adam ở hai bước đầu, phân biệt tổng tích lũy với trung bình mũ, và giải thích điều một mô phỏng nhỏ có thể hoặc không thể chứng minh.

**Cách học:** mục 1–3 là tuyến tính toán bậc nhất; mục 4–5 là tuyến độ cong; mục 6 là cách đánh giá. Mỗi phép bình phương, căn và chia giữa vector ở mục 1–3 đều thực hiện theo từng tọa độ, không phải phép nhân ma trận.

## 1. AdaGrad: giữ tổng bình phương từ bước đầu

Với gradient $g_t$ ở bước $t$, trạng thái $s_0=0$, AdaGrad dùng

$$s_t=s_{t-1}+g_t\odot g_t,\qquad
\theta_{t+1}=\theta_t-\eta\frac{g_t}{\sqrt{s_t}+\varepsilon}.$$

$\odot$ là nhân theo tọa độ; $\varepsilon>0$ tránh mẫu số bằng 0. Công thức này dùng biến thể epsilon ngoài căn, cũng là quy ước trong code minh họa. Khi so thư viện, phải kiểm vị trí epsilon trước khi so từng số.

Một tọa độ nhận gradient lớn nhiều lần sẽ có $s_t$ lớn, nên hệ số hiệu dụng $\eta/(\sqrt{s_t}+\varepsilon)$ giảm. $s_t$ không quên các bước cũ. Điều này có thể làm bước quá nhỏ về sau nếu bình phương gradient tiếp tục tích lũy; không phải bảo đảm thuật toán kém trên mọi bài toán.

::: example Chỉ xét một tọa độ
Cho chuỗi gradient thử $g_1=2$, $g_2=2$, $\eta=0.1$. Bỏ epsilon chỉ trong phép tính tay vì mẫu số ở đây khác 0:

$s_1=4$, độ dời thứ nhất $-0.1$.

$s_2=8$, độ dời thứ hai $-0.1/\sqrt2\approx-0.07071$.

Chuỗi gradient này được cung cấp để kiểm công thức, không được mô tả là gradient của một thí nghiệm train thật.
:::

## 2. RMSProp: giảm trọng số của quá khứ xa

Thay tổng tích lũy bằng **trung bình mũ**:

$$v_t=\beta v_{t-1}+(1-\beta)g_t\odot g_t,\qquad
\theta_{t+1}=\theta_t-\eta\frac{g_t}{\sqrt{v_t}+\varepsilon},\quad0\le\beta<1.$$

Gradient bình phương cách $k$ bước có hệ số $(1-\beta)\beta^k$. Vì vậy ảnh hưởng giảm dần theo tuổi. $v_t$ không phải phương sai có trừ trung bình; nó theo dõi bình phương gradient, còn gọi moment bậc hai không tâm.

Với $v_0=0$, $g_1=2$, $\beta=0.9$, $v_1=0.4$. Nếu $\eta=0.1$, độ dời xấp xỉ $-0.31623$ khi epsilon rất nhỏ. Giá trị đầu có thể lớn hơn AdaGrad vì trạng thái còn nhỏ. Công thức RMSProp ở đây không có hiệu chỉnh bias như Adam ở mục tiếp theo.

<details><summary>Tự kiểm: gradient bằng 0 ở bước sau thì v có trở về 0 ngay không?</summary>

Không khi $0<\beta<1$ và $v$ cũ khác 0. Nó trở thành $\beta v$ cũ. Với $\beta=0$, chỉ gradient hiện tại quyết định trạng thái.

</details>

## 3. Adam: hai moment và hiệu chỉnh trạng thái khởi đầu

Khởi tạo $m_0=v_0=0$, đếm bước $t=1,2,\ldots$:

$$\begin{aligned}
m_t&=\beta_1m_{t-1}+(1-\beta_1)g_t,\\
v_t&=\beta_2v_{t-1}+(1-\beta_2)g_t\odot g_t,\\
\widehat m_t&=m_t/(1-\beta_1^t),\\
\widehat v_t&=v_t/(1-\beta_2^t),\\
\theta_{t+1}&=\theta_t-\eta\widehat m_t/(\sqrt{\widehat v_t}+\varepsilon).
\end{aligned}$$

$0\le\beta_1,\beta_2<1$, $\varepsilon>0$. $m$ theo dõi gradient có dấu, $v$ theo dõi bình phương không âm. Không đổi $v_t$ thành $m_t^2$; trung bình bình phương khác bình phương trung bình.

### 3.1 Vì sao có 1−βᵗ?

Nếu gradient giả sử giữ bằng một số cố định $g$, trung bình mũ khởi tạo 0 cho $m_t=(1-\beta_1^t)g$. Chia cho tổng trọng số $1-\beta_1^t$ đưa kết quả về $g$. Với gradient biến thiên, đây là trung bình có trọng số được chuẩn hóa; không khẳng định nó là một ước lượng không chệch của gradient tại tham số hiện tại, vì tham số và phân phối gradient cũng đổi.

### 3.2 Tính hai bước đầu bằng tay

Cho chuỗi thử $g_1=2$, $g_2=1$, $\beta_1=0.9$, $\beta_2=0.999$:

| Trạng thái | Bước 1 | Bước 2 |
| --- | ---: | ---: |
| $m_t$ | 0.2 | 0.28 |
| $v_t$ | 0.004 | 0.004996 |
| $\widehat m_t$ | 2 | $28/19\approx1.47368$ |
| $\widehat v_t$ | 4 | $4996/1999\approx2.49925$ |

Với $\eta=0.1$ và epsilon rất nhỏ, độ dời thứ nhất gần $-0.1$, thứ hai gần $-0.09322$. Thứ tự phải là: tính gradient → cập nhật moment → hiệu chỉnh theo đúng số bước → cập nhật tham số. Reset moment mà giữ bộ đếm cũ sẽ đổi thuật toán.

<MathLab type="optimizer" initial-method="adam">

```js
m = beta1*m + (1-beta1)*g;
v = beta2*v + (1-beta2)*g*g;
const mHat = m/(1-beta1**t), vHat = v/(1-beta2**t);
theta -= rate*mHat/(Math.sqrt(vHat)+epsilon);
```

</MathLab>

Mô phỏng dùng cùng điểm đầu và hàm toàn phương để đối chiếu các phép cập nhật. Mở “Trạng thái thuật toán” để xem các moment thực sự được tính. Tốc độ học, $\kappa$ và phương pháp đổi thì trạng thái được đặt lại. Không có gradient ngẫu nhiên trong mô phỏng này.

Adam không tự cho chứng nhận KKT, không bảo đảm tốt nhất trên mọi dữ liệu và không biến loss mạng sâu thành lồi. Các định lý cần đúng giả thiết của chúng; không dùng tên thuật toán làm bảo đảm.

## 4. Newton và gradient liên hợp: dùng độ cong theo cách khác

Ở Bài 04, Newton giải $Hd=-g$. Lập và lưu Hessian dày $n\times n$ tốn bậc $n^2$ phần tử. Một lựa chọn là dùng phép nhân $Hv$ mà không lưu toàn ma trận, rồi giải hệ bằng thuật toán lặp.

**Gradient liên hợp tuyến tính (CG)** giải $Hz=b$ với $H$ đối xứng dương xác định. Đây là bài giải hệ; để dùng nó cho Newton phải đặt $b=-g$. Khởi tạo $z_0$, phần dư $r_0=b-Hz_0$, hướng $p_0=r_0$:

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

## 5. BFGS: học một xấp xỉ độ cong

Gọi $s_k=\theta_{k+1}-\theta_k$, $y_k=g_{k+1}-g_k$. $s$ là độ dời; $y$ là đổi gradient. Với một hàm toàn phương có Hessian $H$, ta có $y_k=Hs_k$, nên $H^{-1}y_k=s_k$ nếu $H$ khả nghịch. BFGS giữ quan hệ ấy trên cặp vừa quan sát: một xấp xỉ Hessian nghịch đảo $M$ được cập nhật để thỏa **điều kiện secant** $M_{k+1}y_k=s_k$.

Với $y_k^Ts_k>0$, đặt $\rho_k=1/(y_k^Ts_k)$. Công thức BFGS nghịch đảo là

$$M_{k+1}=(I-\rho_ks_ky_k^T)M_k(I-\rho_ky_ks_k^T)+\rho_ks_ks_k^T.$$

Nếu $M_k\succ0$ và điều kiện độ cong dương đúng, cập nhật giữ tính dương xác định. Khi $y^Ts$ bằng 0 hoặc âm, không chia tiếp như thể đã đủ giả thiết; implementation phải có cách bỏ hoặc sửa cập nhật. Hướng là $d=-M_kg_k$, rồi tìm kiếm độ dài bước.

Ví dụ tự đặt $M_0=I$, $s=(1,0)$, $y=(2,0)$ cho $\rho=1/2$, $M_1=\operatorname{diag}(1/2,1)$. Ta kiểm $M_1y=s$. Toàn ma trận dày cần bộ nhớ bậc $n^2$; L-BFGS giữ một số cặp $(s,y)$ để tính hướng mà không lưu ma trận đầy đủ. Việc dùng gradient lô nhỏ còn phải xét nhiễu khi đo $y$.

## 6. Tổ chức phép so sánh trước khi kết luận

Một phép so sánh hữu ích giữ cùng mô hình, dữ liệu, khởi tạo, seed và ngân sách; mỗi phương pháp được chọn siêu tham số theo cùng quy tắc validation. Báo riêng số bước, số lượt qua dữ liệu và thời gian, vì một bước Newton khác chi phí một bước SGD.

Lưu tối thiểu loss train, loss validation, tốc độ học, cỡ lô và tiêu chí dừng. Khi tiếp tục một optimizer có trạng thái, lưu cả moment/vận tốc và bộ đếm. Chỉ lưu tham số mô hình rồi gọi là “tiếp tục đúng bước trước” sẽ bỏ mất trạng thái thuật toán.

Mô phỏng ở mục 3 giúp đọc công thức và phát hiện sai dấu hoặc sai bộ đếm. Nó chưa cho biết phương pháp nào tốt nhất trên một mạng sâu hoặc một phân phối dữ liệu thật. Muốn trả lời câu hỏi ấy cần thí nghiệm đúng điều kiện vừa nêu.

## Bài tập tự luyện

::: exercise 1. Bình phương trung bình khác gì trung bình bình phương?
Hai gradient là $2,-2$. Tính trung bình gradient và trung bình bình phương. Điều gì xảy ra nếu dùng bình phương trung bình thay cho v?
:::
::: solution
Trung bình bằng 0; trung bình bình phương bằng 4. Bình phương trung bình cho 0 và bỏ mất độ lớn dao động. Đây là lý do moment bậc hai không được thay bằng bình phương moment bậc nhất.
:::

::: exercise 2. Hiệu chỉnh bước đầu
Với gradient đầu $g_1=-3$, $\beta_1=0.9$, $\beta_2=0.999$, tính các moment và dấu cập nhật Adam.
:::
::: solution
$m_1=-0.3$, $v_1=0.009$, $\widehat m_1=-3$, $\widehat v_1=9$. Với tốc độ học dương, độ dời $-\eta(-3)/(3+\varepsilon)>0$. Dấu hướng được giữ ở moment thứ nhất; moment thứ hai không giữ dấu.
:::

::: exercise 3. Đừng đặt Newton bằng một phép chia tọa độ
Với $H=\begin{bmatrix}2&1\\1&2\end{bmatrix}$, $g=(1,0)$, giải $Hd=-g$ và so với việc chỉ chia theo đường chéo.
:::
::: solution
Giải $2d_1+d_2=-1$, $d_1+2d_2=0$ cho $d=(-2/3,1/3)$. Chia đường chéo cho $(-1/2,0)$ không thỏa hệ. Adam/RMSProp đổi thang theo tọa độ, không tương đương dùng Hessian nghịch đảo đầy đủ.
:::

## Tóm tắt

AdaGrad tích lũy lịch sử, RMSProp dùng trung bình mũ, Adam kết hợp hai moment được hiệu chỉnh. Newton, CG và BFGS dùng thông tin độ cong theo cơ chế khác. Theo dõi trạng thái và điều kiện dùng giúp đọc đúng thuật toán; một đường loss đẹp của mô hình nhỏ chưa đủ chọn optimizer cho mạng sâu.

## Nguồn và đọc thêm

- *Convex Optimization*, §9.5 (Newton), phụ lục C về giải hệ tuyến tính. Phụ lục này không dùng làm nguồn của công thức CG.
- Jonathan Shewchuk, [An Introduction to the Conjugate Gradient Method Without the Agonizing Pain](https://www.cs.cmu.edu/~quake-papers/painless-conjugate-gradient.pdf), §8 và thuật toán B2: nguồn chính thức bổ sung cho CG tuyến tính, cùng giả thiết SPD và kiểm phần dư.
- Duchi, Hazan & Singer (2011), [Adaptive Subgradient Methods](https://jmlr.org/papers/v12/duchi11a.html): nguồn gốc phương pháp tích lũy thang theo tọa độ.
- Goodfellow, Bengio & Courville, [*Deep Learning*, §8.5–8.6](https://www.deeplearningbook.org/contents/optimization.html): RMSProp, Adam và phương pháp độ cong. Công thức BFGS được trình bày đầy đủ để người học kiểm điều kiện secant; ví dụ ma trận tự đặt.
- Công thức BFGS và điều kiện giữ PD đối chiếu với Madeleine Udell, [Quasi-Newton Methods, ORIE 6326](https://web.stanford.edu/~udell/orie6326/lectures/quasinewton.pdf), phần BFGS inverse update và positive definiteness.
- Kingma & Ba, [Adam: A Method for Stochastic Optimization](https://arxiv.org/abs/1412.6980), Algorithm 1: các moment và hiệu chỉnh bias. Bản minh họa dùng epsilon ngoài căn theo công thức này.
- Các chuỗi gradient, hệ hai chiều và bài tập là dữ liệu tự đặt, có kiểm toán bằng chương trình.

[Bài 05](./bai-05-toi-uu-huan-luyen.md) · [Bài 07 — LP và quy hoạch động](./bai-07-quy-hoach-tuyen-tinh-va-dong.md).
