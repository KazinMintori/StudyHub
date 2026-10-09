---
title: Bài tập ôn luyện - Xác suất thống kê
description: Tuyển tập bài tập giải tích xác suất, biến ngẫu nhiên, ước lượng hợp lý cực đại (MLE) và kiểm định giả thuyết thống kê.
---

# Bài tập ôn luyện: Xác suất thống kê

Tài liệu cung cấp hệ thống bài tập môn Xác suất thống kê dành cho sinh viên ngành Công nghệ thông tin và Khoa học dữ liệu, bao gồm biến ngẫu nhiên liên tục, phân phối mẫu, ước lượng tham số và kiểm định thống kê.

---

## Phần 1. Biến ngẫu nhiên & Phân phối xác suất

### Bài 1.1: Hàm mật độ xác suất và tính toán kỳ vọng, phương sai
Cho biến ngẫu nhiên liên tục $X$ có hàm mật độ xác suất (PDF) như sau:
$$f(x) = \begin{cases} c(4 - x^2) & \text{với } 0 \le x \le 2 \\ 0 & \text{với } x \text{ khác} \end{cases}$$

1. Tìm hằng số chuẩn hóa $c$ để $f(x)$ là một hàm mật độ xác suất hợp lệ.
2. Tìm hàm phân phối tích lũy $F(x) = P(X \le x)$.
3. Tính kỳ vọng $E[X]$ và kỳ vọng của bình phương $E[X^2]$.
4. Tính phương sai $\text{Var}(X)$ và độ lệch chuẩn $\sigma_X$.
5. Tính xác suất $P(1 \le X \le 2)$.

#### Lời giải gợi ý
1. Điều kiện chuẩn hóa: $\int_{-\infty}^{+\infty} f(x) \, dx = 1$:
   $$
   \begin{aligned}
   \int_0^2 c(4 - x^2) \, dx &= c \left[ 4x - \frac{x^3}{3} \right]_0^2 = c \left( 8 - \frac{8}{3} \right) \\
   &= c \cdot \frac{16}{3} = 1 \implies c = \frac{3}{16}.
   \end{aligned}
   $$

2. Hàm phân phối tích lũy với $0 \le x \le 2$:
   $$F(x) = \int_0^x \frac{3}{16}(4 - t^2) \, dt = \frac{3}{16} \left( 4x - \frac{x^3}{3} \right) = \frac{3}{4}x - \frac{x^3}{16}$$
   - Với $x < 0$: $F(x) = 0$.
   - Với $x > 2$: $F(x) = 1$.

3. Tính kỳ vọng:
   $$
   \begin{aligned}
   E[X] &= \int_0^2 x f(x) \, dx = \frac{3}{16} \int_0^2 (4x - x^3) \, dx \\
   &= \frac{3}{16} \left[ 2x^2 - \frac{x^4}{4} \right]_0^2 = \frac{3}{16} (8 - 4) = \frac{3}{4} = 0.75.
   \end{aligned}
   $$
   $$
   \begin{aligned}
   E[X^2] &= \int_0^2 x^2 f(x) \, dx = \frac{3}{16} \int_0^2 (4x^2 - x^4) \, dx \\
   &= \frac{3}{16} \left[ \frac{4x^3}{3} - \frac{x^5}{5} \right]_0^2 = \frac{3}{16} \left( \frac{32}{3} - \frac{32}{5} \right) \\
   &= \frac{3}{16} \times \frac{64}{15} = \frac{4}{5} = 0.8.
   \end{aligned}
   $$

4. Tính phương sai:
   $$
   \begin{aligned}
   \text{Var}(X) &= E[X^2] - (E[X])^2 = 0.8 - (0.75)^2 \\
   &= 0.8 - 0.5625 = 0.2375 = \frac{19}{80}.
   \end{aligned}
   $$
   $$\sigma_X = \sqrt{0.2375} \approx 0.4873$$

5. Tính xác suất:
   $$
   \begin{aligned}
   P(1 \le X \le 2) &= F(2) - F(1) = 1 - \left( \frac{3}{4}(1) - \frac{1}{16} \right) \\
   &= 1 - \frac{11}{16} = \frac{5}{16} = 0.3125.
   \end{aligned}
   $$

---

## Phần 2. Định lý giới hạn trung tâm (CLT) & Phân phối mẫu

### Bài 2.1: Ứng dụng Định lý giới hạn trung tâm (CLT)
Thời gian phản hồi của một máy chủ web là một biến ngẫu nhiên có kỳ vọng $\mu = 120$ ms và độ lệch chuẩn $\sigma = 30$ ms. Giả sử ta ghi nhận một mẫu ngẫu nhiên gồm $n = 100$ yêu cầu độc lập.

1. Gọi $\bar{X}$ là thời gian phản hồi trung bình của 100 yêu cầu trên. Xác định phân phối xấp xỉ của $\bar{X}$ theo Định lý giới hạn trung tâm.
2. Tính xác suất để thời gian phản hồi trung bình $\bar{X}$ vượt quá $125$ ms. Cho biết $\Phi(1.67) \approx 0.9525$.
3. Tính xác suất để tổng thời gian phản hồi của 100 yêu cầu $S_{100} = \sum_{i=1}^{100} X_i$ nằm trong khoảng từ $11400$ ms đến $12600$ ms. Cho biết $\Phi(2.0) \approx 0.9772$.

Ký hiệu tổng ở câu 3 nghĩa là $S_{100}=X_1+X_2+\cdots+X_{100}$. Chỉ số $i$ chọn từng yêu cầu, từ 1 đến 100.

#### Lời giải gợi ý
1. Theo Định lý giới hạn trung tâm (CLT), với kích thước mẫu lớn $n = 100 \ge 30$, biến ngẫu nhiên trung bình mẫu $\bar{X}$ xấp xỉ phân phối chuẩn:
   $$\bar{X} \sim \mathcal{N}\left(\mu, \frac{\sigma^2}{n}\right) = \mathcal{N}\left(120, \frac{30^2}{100}\right) = \mathcal{N}(120, 9)$$
   Sai số chuẩn của trung bình mẫu: $SE = \frac{\sigma}{\sqrt{n}} = \frac{30}{10} = 3$ ms.

2. Chuẩn hóa biến $\bar{X}$ về biến chuẩn tắc $Z \sim \mathcal{N}(0, 1)$:
   $$
   \begin{aligned}
   P(\bar{X} > 125) &= P\left(Z > \frac{125 - 120}{3}\right) = P\left(Z > \frac{5}{3}\right) \\
   &\approx P(Z > 1.67) = 1 - \Phi(1.67) \\
   &\approx 1 - 0.9525 = 0.0475 \quad (4.75\%).
   \end{aligned}
   $$

3. Tổng thời gian $S_{100}$ xấp xỉ phân phối chuẩn với kỳ vọng $E[S_{100}] = n\mu = 100 \times 120 = 12000$ và độ lệch chuẩn $\sigma_S = \sigma \sqrt{n} = 30 \times 10 = 300$:
   $$
   \begin{aligned}
   P(11400 \le S_{100} \le 12600) &= P\left(\frac{11400 - 12000}{300} \le Z \le \frac{12600 - 12000}{300}\right) \\
   &= P(-2 \le Z \le 2) = 2\Phi(2) - 1 \\
   &= 2(0.9772) - 1 = 0.9544 \quad (95.44\%).
   \end{aligned}
   $$

---

## Phần 3. Ước lượng tham số (MLE & Khoảng tin cậy)

### Bài 3.1: Ước lượng hợp lý cực đại (Maximum Likelihood Estimation - MLE)
Cho mẫu ngẫu nhiên độc lập cùng phân phối $X_1, X_2, \dots, X_n$ tuân theo phân phối mũ (Exponential Distribution) với tham số $\lambda > 0$, có hàm mật độ:
$$f(x; \lambda) = \lambda e^{-\lambda x}, \quad x \ge 0$$

1. Thiết lập hàm hợp lý $L(\lambda)$ và hàm log-hợp lý $\ell(\lambda) = \ln L(\lambda)$.
2. Tìm ước lượng hợp lý cực đại $\hat{\lambda}_{\text{MLE}}$ của tham số $\lambda$.
3. Kiểm tra điều kiện đạo hàm cấp 2 để chứng minh $\hat{\lambda}_{\text{MLE}}$ thực sự là điểm cực đại toàn cục.

#### Lời giải gợi ý
1. Hàm hợp lý (Likelihood Function):
   Vì các quan sát độc lập, ta nhân mật độ của từng quan sát: $L(\lambda)=f(x_1;\lambda)f(x_2;\lambda)\cdots f(x_n;\lambda)$. Ký hiệu $\prod_{i=1}^n$ viết gọn phép nhân này, với $i$ chạy qua $n$ quan sát. Còn $\sum_{i=1}^n x_i=x_1+\cdots+x_n$ cộng các giá trị quan sát.

   $$L(\lambda) = \prod_{i=1}^n f(x_i; \lambda) = \prod_{i=1}^n (\lambda e^{-\lambda x_i}) = \lambda^n e^{-\lambda \sum_{i=1}^n x_i}$$
   Hàm log-hợp lý (Log-Likelihood):
   $$\ell(\lambda) = \ln L(\lambda) = n \ln \lambda - \lambda \sum_{i=1}^n x_i$$

2. Lấy đạo hàm cấp 1 theo $\lambda$ và cho bằng $0$:
   $$\frac{d\ell}{d\lambda} = \frac{n}{\lambda} - \sum_{i=1}^n x_i = 0 \implies \frac{n}{\lambda} = \sum_{i=1}^n x_i \implies \hat{\lambda}_{\text{MLE}} = \frac{n}{\sum_{i=1}^n x_i} = \frac{1}{\bar{X}}$$
   (Nghịch đảo của giá trị trung bình mẫu).

3. Đạo hàm cấp 2:
   $$\frac{d^2\ell}{d\lambda^2} = -\frac{n}{\lambda^2} < 0 \quad \forall \lambda > 0$$
   Do đạo hàm cấp 2 luôn âm, hàm log-hợp lý là hàm lõm ngặt, điểm dừng $\hat{\lambda}_{\text{MLE}} = \frac{1}{\bar{X}}$ là điểm cực đại duy nhất.

---

## Phần 4. Kiểm định giả thuyết thống kê (Hypothesis Testing)

### Bài 4.1: Kiểm định t-Student một mẫu (One-Sample t-Test)
Một công ty công nghệ tuyên bố thuật toán tối ưu mới giúp giảm thời gian huấn luyện mô hình học sâu xuống mức $\mu_0 = 45$ phút. Một nhóm kiểm thử độc lập chạy thuật toán $n = 16$ lần trên cùng cấu hình phần cứng và thu được kết quả:
- Trung bình mẫu: $\bar{x} = 48$ phút.
- Độ lệch chuẩn mẫu: $s = 6$ phút.

Với mức ý nghĩa $\alpha = 0.05$, hãy kiểm định tuyên bố của công ty (đối thuyết là thời gian thực tế cao hơn $45$ phút).

1. Đặt giả thuyết không $H_0$ và đối thuyết $H_1$.
2. Xác định tiêu chuẩn kiểm định và tính giá trị thống kê $t_{\text{obs}}$.
3. Tra giá trị tới hạn $t_{\alpha, df}$ cho bậc tự do $df = n - 1 = 15$ tại mức ý nghĩa $\alpha = 0.05$ (cho biết $t_{0.05, 15} = 1.753$).
4. Đưa ra kết luận thống kê.

#### Lời giải gợi ý
1. Thiết lập giả thuyết:
   $$H_0: \mu = 45 \quad \text{vs} \quad H_1: \mu > 45 \quad (\text{kiểm định phía phải})$$

2. Thống kê kiểm định $t$:
   $$t_{\text{obs}} = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{48 - 45}{6 / \sqrt{16}} = \frac{3}{6 / 4} = \frac{3}{1.5} = 2.0$$

3. Miền bác bỏ:
   Bác bỏ $H_0$ nếu $t_{\text{obs}} > t_{\alpha, n-1} = t_{0.05, 15} = 1.753$.

4. Kết luận:
   Vì $t_{\text{obs}} = 2.0 > 1.753$, ta có đủ bằng chứng thống kê ở mức ý nghĩa $5\%$ để bác bỏ giả thuyết $H_0$. Có nghĩa là thời gian huấn luyện thực tế trung bình dài hơn 45 phút như tuyên bố.
