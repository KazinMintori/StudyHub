---
title: "Hệ thống bài tập Cơ sở toán học cho Trí tuệ Nhân tạo"
description: "Bộ bài tập nhận diện bản chất, tính toán giải tích và suy luận thuật toán của toàn bộ 8 bài giảng kèm lời giải phân tích chi tiết."
---

# Hệ thống bài tập Cơ sở toán học cho Trí tuệ Nhân tạo

Bộ bài tập được biên soạn nhằm rèn luyện cho người học hai năng lực cốt lõi:
1. **Năng lực trực giác và nhận diện**: Phân biệt chuẩn xác cấu trúc bài toán, kiểm tra tính lồi, tính khả thi và điều kiện cực trị.
2. **Năng lực giải tích số chuẩn xác**: Thực hiện các bước tính đạo hàm ma trận, xập xỉ Taylor, dò bước cập nhật tham số và kiểm tra các điều kiện tối ưu KKT.

Mỗi bài giảng đều đi kèm 3 bài tập tự luyện có lời giải chi tiết theo từng bước suy luận. Bạn hãy luôn chủ động giải quyết bài toán trên giấy trước khi mở rộng phần phân tích lời giải của giảng viên.

---

## 1. Mục lục bài tập theo bài giảng

| Bài giảng | Kỹ năng giải tích & Suy luận trọng tâm | Liên kết mở bài tập |
| :---: | :--- | :--- |
| **00** | Phân tích chiều ma trận, vi phân đạo hàm, sai số dự đoán và xấp xỉ Gauss MLE | [Bài tập nền tảng](./bai-giang/bai-00-on-tap-nen-tang.md#bai-tap-tu-luyen) |
| **01** | Chứng minh tập lồi, hàm lồi qua định nghĩa đoạn thẳng và điều kiện vi phân | [Bài tập tính lồi](./bai-giang/bai-01-nhap-mon-toi-uu.md#bai-tap-tu-luyen) |
| **02** | Nhận diện phả hệ bài toán lồi (LP, QP, SOCP, SDP), biến đổi Schur và nới lỏng | [Bài tập mô hình hóa](./bai-giang/bai-02-tap-loi.md#bai-tap-tu-luyen) |
| **03** | Thiết lập hàm đối ngẫu Lagrange, kiểm tra điều kiện Slater và giải hệ KKT | [Bài tập đối ngẫu](./bai-giang/bai-03-doi-ngau-lagrange.md#bai-tap-tu-luyen) |
| **04** | Dò bước Armijo backtracking, tính hướng Newton decrement và giải hệ Newton-KKT | [Bài tập thuật toán](./bai-giang/bai-04-gradient-newton.md#bai-tap-tu-luyen) |
| **05** | Ước lượng gradient mini-batch, phân tích động lượng Momentum và Nesterov | [Bài tập huấn luyện học máy](./bai-giang/bai-05-toi-uu-huan-luyen.md#bai-tap-tu-luyen) |
| **06** | Tính toán cập nhật thích nghi Adam/RMSProp, phương pháp Gradient liên hợp (CG) | [Bài tập optimizer thích nghi](./bai-giang/bai-06-phuong-phap-thich-nghi.md#bai-tap-tu-luyen) |
| **07** | Xác định nghiệm cơ sở khả thi (BFS) trong LP, quy nạp ngược Bellman trên DAG | [Bài tập LP và Bellman DP](./bai-giang/bai-07-quy-hoach-tuyen-tinh-va-dong.md#bai-tap-tu-luyen) |

---

## 2. Bài toán tích hợp: Cầu nối toàn diện các bài giảng

Dưới đây là một bài toán mẫu tích hợp toàn bộ kiến thức từ hình học tập lồi, vi phân, bài toán tối ưu có ràng buộc đến điều kiện KKT và đối ngẫu Lagrange:

::: exercise Hồi quy bình phương tối thiểu có giới hạn tham số
Cho tập dữ liệu một chiều đơn giản gồm vector đầu vào $A = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}$ và vector nhãn mục tiêu $b = \begin{bmatrix} 1 \\ 2 \\ 2 \end{bmatrix}$.

Ta cần tìm trọng số $w \in \mathbb{R}$ giải bài toán hồi quy với ràng buộc biên:
$$
\min_{w \in \mathbb{R}} f(w) = \frac{1}{2} \|Aw - b\|_2^2 \qquad \text{sao cho} \quad w \le \frac{1}{2}.
$$

1. Khai triển hàm mục tiêu $f(w)$, khảo sát đạo hàm bậc một và bậc hai. Chứng minh bài toán là một bài toán tối ưu lồi.
2. Tìm nghiệm tối ưu không ràng buộc $w_{\mathrm{uncon}}$. Nghiệm này có khả thi cho bài toán gốc không?
3. Thiết lập hệ điều kiện Karush-Kuhn-Tucker (KKT). Tìm nghiệm tối ưu có ràng buộc $w^*$ và nhân tử Lagrange $\lambda^*$.
4. Giải thích tại sao trong bài toán có ràng buộc, tiêu chí dừng "gradient bằng 0" ($\nabla f(w) = 0$) không còn áp dụng được.
:::

::: solution
### 1. Khảo sát tính lồi của bài toán
Ta khai triển hàm mục tiêu:
$$
\begin{aligned}
f(w) &= \frac{1}{2} \left[ (1w - 1)^2 + (2w - 2)^2 + (3w - 2)^2 \right] \\
&= \frac{1}{2} \left[ (w^2 - 2w + 1) + (4w^2 - 8w + 4) + (9w^2 - 12w + 4) \right] \\
&= \frac{1}{2} \left( 14w^2 - 22w + 9 \right) = 7w^2 - 11w + \frac{9}{2}.
\end{aligned}
$$

- Đạo hàm bậc nhất: Biểu thức $f'(w) = 14w - 11$.
- Đạo hàm bậc hai (Hessian): Giá trị $f''(w) = 14 > 0$ với mọi $w \in \mathbb{R}$.

Vì đạo hàm bậc hai luôn dương nên hàm mục tiêu $f(w)$ là hàm lồi ngặt (strictly convex). Miền khả thi $\mathcal{C} = \{w \in \mathbb{R} \mid w \le 1/2\}$ là một nửa đường thẳng (nửa không gian đóng một chiều), do đó là một tập lồi. Bài toán là một bài toán tối ưu lồi ngặt, bảo đảm rằng nếu nghiệm tối ưu tồn tại thì nó là duy nhất trên toàn cục.

### 2. Nghiệm tối ưu không ràng buộc
Nếu không có ràng buộc $w \le 1/2$, nghiệm cực tiểu đạt được khi triệt tiêu đạo hàm:
$$
f'(w) = 0 \iff 14w - 11 = 0 \implies w_{\mathrm{uncon}} = \frac{11}{14} \approx 0.7857.
$$
Giá trị mất mát không ràng buộc tương ứng là $f(11/14) = \frac{5}{28} \approx 0.1786$.

Tuy nhiên, giá trị $w_{\mathrm{uncon}} = \frac{11}{14} > \frac{1}{2}$, nghĩa là nghiệm không ràng buộc nằm **hoàn toàn bên ngoài miền khả thi**! Do đó, nghiệm này không được chấp nhận.

### 3. Thiết lập hệ điều kiện KKT và tìm nghiệm tối ưu
Viết lại ràng buộc dưới dạng chuẩn: $g(w) = w - \frac{1}{2} \le 0$.
Hàm Lagrange:
$$
\mathcal{L}(w, \lambda) = f(w) + \lambda \left( w - \frac{1}{2} \right) = 7w^2 - 11w + \frac{9}{2} + \lambda \left( w - \frac{1}{2} \right).
$$

Hệ 4 điều kiện KKT:
1. **Khả thi nguyên thủy (Primal Feasibility)**: $w \le \frac{1}{2}$.
2. **Khả thi đối ngẫu (Dual Feasibility)**: $\lambda \ge 0$.
3. **Độ bù bổ sung (Complementary Slackness)**: $\lambda \left( w - \frac{1}{2} \right) = 0$.
4. **Điểm dừng Lagrange (Stationarity)**: 
   $$
   \nabla_w \mathcal{L}(w, \lambda) = 14w - 11 + \lambda = 0 \iff \lambda = 11 - 14w.
   $$

Xét hai trường hợp của độ bù bổ sung:
- **Trường hợp $\lambda = 0$** (ràng buộc không hoạt động): Ta suy ra $w = 11/14$, mâu thuẫn với điều kiện $w \le 1/2$.
- **Trường hợp $w = \frac{1}{2}$** (ràng buộc hoạt động/chạm biên):
  Thay $w = 1/2$ vào phương trình điểm dừng:
  $$
  \lambda^* = 11 - 14 \left(\frac{1}{2}\right) = 11 - 7 = 4 > 0.
  $$
  Nhân tử $\lambda^* = 4 \ge 0$ thỏa mãn hoàn hảo điều kiện khả thi đối ngẫu!

Nghiệm tối ưu duy nhất của bài toán là $w^* = \frac{1}{2}$ với nhân tử đối ngẫu $\lambda^* = 4$.
Giá trị hàm mục tiêu tối ưu có ràng buộc là:
$$
f\left(\frac{1}{2}\right) = 7\left(\frac{1}{2}\right)^2 - 11\left(\frac{1}{2}\right) + \frac{9}{2} = \frac{7}{4} - \frac{22}{4} + \frac{18}{4} = \frac{3}{4} = 0.75.
$$

### 4. Bản chất của tiêu chí dừng trong tối ưu có ràng buộc
Tại nghiệm tối ưu $w^* = 1/2$, đạo hàm của hàm mục tiêu gốc là:
$$
f'\left(\frac{1}{2}\right) = 14\left(\frac{1}{2}\right) - 11 = -4 \ne 0.
$$

Gradient của hàm mục tiêu không hề triệt tiêu! Điều này mang ý nghĩa hình học rất trực quan: 
- Vì đạo hàm $f'(1/2) = -4 < 0$, đồ thị hàm mục tiêu đang dốc xuống về phía bên phải. Nếu được phép đi tiếp sang phải ($w > 1/2$), ta hoàn toàn có thể làm hàm mất mát giảm thêm.
- Tuy nhiên, "bức tường" ràng buộc $w \le 1/2$ đã chặn đứng chuyển động này lại. Lực cản của bức tường chính là nhân tử Lagrange $\lambda^* = 4$, triệt tiêu hoàn toàn lực kéo dốc dốc của gradient mục tiêu:
  $$
  f'(w^*) + \lambda^* = -4 + 4 = 0.
  $$

Đây là bài học sư phạm kinh điển: Trong tối ưu hóa có ràng buộc, nghiệm tối ưu thường nằm tại biên, nơi gradient của hàm mục tiêu bị triệt tiêu bởi tổ hợp các vector pháp tuyến của mặt ràng buộc, chứ không phải tự thân bằng 0!
:::
