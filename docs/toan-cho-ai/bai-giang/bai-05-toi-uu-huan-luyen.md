---
course: toan-cho-ai
lecture: bai-05-toi-uu-huan-luyen
section: lecture
title: "Các phương pháp tối ưu trong huấn luyện mô hình học sâu"
prerequisites: ["gradient", "quy-tac-chuoi", "ky-vong", "phuong-sai"]
lessonStatus: ready
description: "Phân biệt hàm mục tiêu trên tập huấn luyện với đại lượng đánh giá; theo dõi SGD, momentum, Nesterov và khởi tạo Glorot."
---

Ở Bài 04, ta giả sử mỗi bước đều tính được gradient chính xác của toàn bộ hàm mục tiêu. Trong học máy, hàm mục tiêu thường là trung bình của hàm mất mát trên rất nhiều quan sát, nên tính toàn bộ gradient ở mỗi bước có thể quá tốn kém. Một lô dữ liệu nhỏ cho phép ước lượng gradient với chi phí thấp hơn, đổi lại từng bước cập nhật sẽ dao động theo các mẫu được chọn. Vì vậy, quá trình huấn luyện phải được mô tả cùng với quy tắc lấy lô và cách đánh giá trên dữ liệu không dùng để cập nhật tham số.

Sau khi học xong, bạn sẽ viết được gradient của một lô dữ liệu, giải thích được tính không chệch dưới đúng giả thiết lấy mẫu, tính được hai bước đầu của momentum và Nesterov, và xác định được thang khởi tạo Glorot từ số đầu vào và đầu ra của một tầng.

Mục 1–3 tạo thành phần chính của bài: hàm mục tiêu, gradient lô nhỏ và SGD. Sau khi tự tính được ví dụ một tham số ở mục 2, hãy đọc mục 4–5 để thấy momentum và Nesterov lưu thêm trạng thái như thế nào. Mục 6 về khởi tạo trọng số có thể học riêng. Những kiến thức xác suất cần dùng được nhắc lại tại chỗ và có liên kết sang Wiki.

## 1. Hàm mục tiêu dùng trong huấn luyện

Với tập huấn luyện $D=\{(x_i,y_i)\}_{i=1}^N$, tham số $\theta$ và hàm mất mát trên mẫu thứ $i$ là $\ell_i(\theta)$, hàm mục tiêu thực nghiệm được viết

$$J(\theta)=\frac1N\sum_{i=1}^N\ell_i(\theta).$$

Nếu có điều chuẩn, ta cộng thêm $\rho R(\theta)$ và phải ghi rõ hệ số $\rho$. Đầu ra $\widehat y_i=f_\theta(x_i)$ của mô hình được đưa vào hàm mất mát; gradient theo $\theta$ được tính bằng quy tắc chuỗi. Lan truyền ngược chỉ tổ chức các phép tính đạo hàm trên đồ thị tính toán, chứ không tạo ra một loại đạo hàm mới.

Hàm mất mát trên tập huấn luyện được tính từ dữ liệu đã dùng để cập nhật tham số. Hàm mất mát trên **tập xác thực** (validation set) được tính trên một tập dữ liệu giữ riêng và dùng để chọn mô hình hoặc siêu tham số. **Tập kiểm thử** (test set) được giữ lại cho lần đánh giá cuối theo quy trình đã định. Giảm hàm mất mát trên tập huấn luyện chưa chứng minh rằng mô hình sẽ dự đoán tốt hơn trên dữ liệu mới.

Ta phải phân biệt hai bài toán. **Tối ưu** tìm tham số làm $J$ nhỏ trên dữ liệu huấn luyện; **khái quát hóa** xét chất lượng của mô hình trên phân phối dữ liệu sẽ gặp khi sử dụng. Việc thuật toán đã hội tụ trên tập huấn luyện không có nghĩa bài toán khái quát hóa cũng đã được giải quyết.

## 2. Gradient ước lượng từ một lô dữ liệu

Đạo hàm tổng hữu hạn bằng tổng đạo hàm:

$$\nabla J(\theta)=\frac1N\sum_i\nabla\ell_i(\theta).$$

Lấy $B$ chỉ số độc lập, đều trên $\{1,\ldots,N\}$, có hoàn lại. Với $\theta$ đang cố định, đặt

$$g_B(\theta)=\frac1B\sum_{j=1}^B\nabla\ell_{I_j}(\theta).$$

Mỗi gradient mẫu có kỳ vọng bằng gradient toàn bộ dữ liệu, nên $\mathbb E[g_B\mid\theta]=\nabla J(\theta)$. Đây là **ước lượng không chệch**, không có nghĩa từng lô đều đúng bằng gradient thật.

Với một tọa độ gradient có phương sai $\sigma_g^2$ và các mẫu độc lập, trung bình $B$ mẫu có phương sai $\sigma_g^2/B$. Lấy mẫu không hoàn lại vẫn cho trung bình không chệch nhưng phương sai có hệ số hiệu chỉnh khác. Xáo trộn rồi đi hết một epoch là quy trình khác lấy mẫu độc lập; không bê nguyên giả thiết độc lập sang mọi bước.

::: example Nhìn thấy nhiễu dù mô hình chỉ có một tham số
Dữ liệu tự đặt gồm hai đầu ra $b_1=0$, $b_2=2$. Mô hình dùng cùng một dự đoán $\theta$ cho cả hai quan sát; hàm mất mát trên mẫu thứ $i$ là $\ell_i=\tfrac12(\theta-b_i)^2$.

$$J(\theta)=\frac14[\theta^2+(\theta-2)^2]
=\frac12(\theta-1)^2+\frac12.$$

Tại $\theta=0$, hai gradient mẫu là 0 và $-2$, còn gradient đầy đủ là $-1$. Với $\eta=0.1$, một bước toàn bộ đến $0.1$; lấy riêng mẫu 1 thì đứng yên; lấy riêng mẫu 2 thì đến $0.2$. Trung bình hai cập nhật là $0.1$.

Tại nghiệm của hàm mục tiêu trên toàn bộ tập huấn luyện, $\theta=1$, gradient toàn bộ bằng 0 nhưng hai gradient mẫu vẫn lần lượt là $1$ và $-1$. Vì vậy một bước SGD với tốc độ học cố định vẫn có thể rời khỏi điểm này.
:::

<details><summary>Thử trả lời: Ở θ=1, nếu lấy mẫu b=0 và η=0.1 thì hàm mục tiêu trên toàn bộ dữ liệu thay đổi thế nào?</summary>

Điểm mới là $0.9$. Ta có $J(1)=0.5$ và $J(0.9)=0.505$, nên hàm mục tiêu tăng. Tính không chệch của gradient là một phát biểu về kỳ vọng; nó không bảo đảm hàm mục tiêu giảm sau từng lần lấy mẫu.

</details>

## 3. Stochastic gradient descent (SGD)

**Stochastic gradient descent (SGD)** cập nhật

$$\theta_{t+1}=\theta_t-\eta_tg_{B_t}(\theta_t).$$

Để mô tả đầy đủ thuật toán, cần nêu mô hình, hàm mất mát, dữ liệu, điểm khởi đầu, quy tắc lấy lô, lịch tốc độ học và tiêu chí dừng. Trạng thái tối thiểu gồm $\theta_t$ và vị trí hiện tại trong quy trình duyệt dữ liệu. Một **epoch** là một lượt đi qua toàn bộ tập huấn luyện khi dữ liệu được chia thành các lô không hoàn lại; số bước trong mỗi epoch phụ thuộc vào kích thước lô.

Không nên dừng chỉ vì gradient của một lô tình cờ nhỏ. Ta có thể theo dõi trung bình hàm mất mát trên tập huấn luyện, hàm mất mát trên tập xác thực theo một lịch cố định, và những phần dư phù hợp với bài toán. Trong mô hình không lồi, gradient nhỏ cũng không phải là chứng nhận tối ưu toàn cục.

```python
def sgd_scalar(theta, targets, rate, draws):
    history = [theta]
    for i in draws:  # chỉ số lấy mẫu được cung cấp để tái lập
        gradient = theta-targets[i]
        theta -= rate*gradient
        history.append(theta)
    return history

print(sgd_scalar(0.0, [0.0, 2.0], 0.1, [0, 1, 0, 1]))
# [0.0, 0.0, 0.2, 0.18, 0.362]
```

Ví dụ cố định chỉ số để nhìn cơ chế; nó không dùng kỳ vọng không chệch như bảo đảm cho một lịch lặp tất định. Khi thí nghiệm ngẫu nhiên, lưu seed và quy tắc lấy mẫu.

## 4. Momentum và trạng thái vận tốc

Chọn quy ước vận tốc là độ dời, khởi tạo $v_0=0$, $0\le\mu<1$:

$$v_{t+1}=\mu v_t-\eta g_t,\qquad \theta_{t+1}=\theta_t+v_{t+1}.$$

Hệ số $\mu$ giữ một phần vận tốc trước. Nếu gradient nhiều bước cùng hướng, đóng góp tích lũy; nếu đổi hướng, vận tốc cũ có thể làm ta đi quá điểm mong muốn. $\mu$ lớn không phải luôn tốt.

::: example Hai bước với cùng quy ước dấu
Dùng $J(\theta)=\tfrac12(\theta-1)^2+\tfrac12$, gradient đầy đủ $\theta-1$, $\theta_0=0$, $\eta=0.1$, $\mu=0.9$.

Bước 1: $g_0=-1$, $v_1=0.1$, $\theta_1=0.1$.

Bước 2: $g_1=-0.9$, $v_2=0.9(0.1)-0.1(-0.9)=0.18$, $\theta_2=0.28$.

Gradient descent thuần đến $0.19$ sau hai bước. So hai điểm cho thấy cơ chế vận tốc, chưa xếp hạng các thuật toán trên mọi bài toán.
:::

## 5. Nesterov và điểm nhìn trước

Giữ cùng quy ước $v$, nhưng tính gradient tại $\widetilde\theta_t=\theta_t+\mu v_t$:

$$g_t=\nabla J(\widetilde\theta_t),\quad
v_{t+1}=\mu v_t-\eta g_t,\quad
\theta_{t+1}=\theta_t+v_{t+1}.$$

Với lô nhỏ, thay $\nabla J$ bằng gradient lô tại điểm nhìn trước. Sự khác biệt ở **địa chỉ tính gradient**, không ở việc đổi tên vận tốc.

Trong ví dụ mục 4, bước 1 vẫn đến $0.1$. Trước bước 2, điểm nhìn trước là $0.1+0.9(0.1)=0.19$, gradient $-0.81$. Vì vậy $v_2=0.171$, $\theta_2=0.271$. Phép tính này giúp kiểm tra phần cài đặt có thực sự lấy gradient tại điểm nhìn trước hay không.

<MathLab type="optimizer" initial-method="momentum">

```js
const lookahead = point.map((x,i) => x+mu*velocity[i]);
const g = gradient(lookahead);
velocity = velocity.map((v,i) => mu*v-rate*g[i]);
point = point.map((x,i) => x+velocity[i]);
```

</MathLab>

Mô phỏng dùng gradient đầy đủ trên hàm toàn phương hai chiều để tách tác động của momentum khỏi nhiễu lấy mẫu. Chọn Momentum và Nesterov, giữ cùng $\eta,\kappa$, rồi xem từng bước. Không suy ra tốc độ hội tụ cho mạng sâu từ mô phỏng lồi này.

## 6. Khởi tạo trọng số

Nếu hai neuron có cùng kiểu kết nối, cùng trọng số và cùng các điều kiện khác, chúng tạo đầu ra giống nhau. Trong tính toán tất định với cùng dữ liệu, gradient giống nhau có thể giữ chúng giống nhau qua nhiều lần cập nhật. Muốn các neuron học những đặc trưng khác nhau, cần phá vỡ đối xứng này. Khởi tạo toàn bộ trọng số của tầng ẩn bằng 0 thường không đạt mục đích đó; việc hệ số chặn (bias) được đặt bằng 0 không có nghĩa mọi trọng số cũng phải bằng 0.

Để xét thang, dùng mô hình tuyến tính hóa $z=\sum_{i=1}^{n_{\mathrm{in}}}W_ix_i$, các trọng số trung bình 0, độc lập với các đầu vào, và các đóng góp được giả định độc lập. Khi phương sai đầu vào giống nhau,

$$\operatorname{Var}(z)=n_{\mathrm{in}}\operatorname{Var}(W)\operatorname{Var}(x).$$

Nếu hệ số nhân lớn hơn 1 qua nhiều tầng, thang tín hiệu có thể tăng; nhỏ hơn 1 có thể giảm. Truyền gradient ngược còn liên quan $n_{\mathrm{out}}$. **Glorot** chọn một cân bằng:

$$\operatorname{Var}(W)=\frac2{n_{\mathrm{in}}+n_{\mathrm{out}}}.$$

Bản uniform tương ứng $W\sim U[-a,a]$, $a=\sqrt{6/(n_{\mathrm{in}}+n_{\mathrm{out}})}$, vì uniform đối xứng có phương sai $a^2/3$. Với fan-in 4, fan-out 2, $a=1$, phương sai $1/3$.

Đây là lựa chọn được suy ra dưới các giả định phân tích và loại hàm kích hoạt đang xét, không phải định luật cho mọi kiến trúc. Hàm kích hoạt phi tuyến và sự phụ thuộc giữa các đại lượng có thể làm phép tính phương sai thay đổi. Khi thử mô hình, vẫn phải theo dõi độ lớn của giá trị kích hoạt và gradient.

## Bài tập tự luyện

::: exercise 1. Tính một lô
Tại $\theta=0.5$ trong dữ liệu $(0,2)$, tính hai gradient mẫu và gradient của lô chứa cả hai.
:::
::: solution
Hai gradient là $0.5,-1.5$. Trung bình $-0.5$, bằng $J'(0.5)$. Cộng mà không chia cỡ lô sẽ cho $-1$ và đổi thang bước cập nhật.
:::

::: exercise 2. Tính tiếp một bước momentum
Ở cuối bước 2 mục 4, tính bước 3 với gradient đầy đủ.
:::
::: solution
$\theta_2=0.28$, $v_2=0.18$, $g_2=-0.72$. $v_3=0.9(0.18)+0.072=0.234$, $\theta_3=0.514$. Phải dùng vận tốc cũ trước khi ghi đè.
:::

::: exercise 3. Thang khởi tạo
Tầng có fan-in 8, fan-out 4. Tính phương sai Glorot và cận uniform.
:::
::: solution
Phương sai $2/12=1/6$, cận $a=\sqrt{6/12}=1/\sqrt2$. Không dùng số neuron của toàn mạng thay fan của tầng đang xét.
:::

## Tóm tắt

SGD thay gradient toàn bộ bằng ước lượng có cách lấy mẫu cụ thể. Momentum giữ vận tốc; Nesterov đổi điểm tính gradient. Khởi tạo quyết định đối xứng và thang tín hiệu trước khi cập nhật. Để biết huấn luyện có ích hay không, vẫn phải theo dõi dữ liệu đánh giá tách riêng.

## Nguồn và đọc thêm

- Nguồn chính cho gradient xác định: *Convex Optimization*, §9.3. Các bảo đảm lồi ở đó không tự chuyển sang mạng sâu.
- Nguồn chính thức bổ sung: Goodfellow, Bengio & Courville, [*Deep Learning*, chương 8](https://www.deeplearningbook.org/contents/optimization.html), §8.1, §8.3.1–8.3.3 và §8.4.
- Glorot & Bengio (2010), [Understanding the difficulty of training deep feedforward neural networks](https://proceedings.mlr.press/v9/glorot10a.html), phần khởi tạo chuẩn hóa; công thức và giả định được đối chiếu với bài báo.
- Ví dụ scalar, đường đi toàn phương và bài tập tự đặt, không phải số liệu thực nghiệm của các tác giả.

[Bài 04](./bai-04-gradient-newton.md) · [Bài 06 — Các phương pháp thích nghi](./bai-06-phuong-phap-thich-nghi.md).
