---
title: "Bất đẳng thức Jensen"
wikiTerm: bat-dang-thuc-jensen
prev: false
next: false
---

# Bất đẳng thức Jensen

Với f lồi và biến ngẫu nhiên X nhận giá trị trong miền xác định của f, ta có $f(\mathbf E X) \le \mathbf E f(X)$. Với tổ hợp lồi hữu hạn, đó là $f(\sum_i \theta_i x_i) \le \sum_i \theta_i f(x_i)$. Với hàm lõm, chiều bất đẳng thức đảo lại.

<WikiUsage />

## Giải thích kỹ thuật

**Đặc trưng cho tính lồi.** Bất đẳng thức đúng với mọi phân phối khi và chỉ khi $f$ lồi, vì phân phối hai điểm với xác suất $\theta$ và $1 - \theta$ cho đúng bất đẳng thức dây cung.

**Khoảng cách Jensen.** Hiệu $\mathbf E f(X) - f(\mathbf E X)$ đo độ cong của $f$ trên vùng mà $X$ phân tán. Với $f(x) = x^2$, nó bằng phương sai. Khi $X$ ít phân tán, nó xấp xỉ $\tfrac12 f''(\mathbf E X)\operatorname{Var}(X)$.

**ELBO.** Với hàm lõm $\log$, ta có $\log \mathbf E_q[p(x, z)/q(z)] \ge \mathbf E_q[\log(p(x, z)/q(z))]$. Vế phải là cận dưới được tối ưu trong suy luận biến phân, và cận chặt khi $q$ đúng bằng phân phối hậu nghiệm. Nguồn: Convex Optimization, §3.1.8–3.1.9.

## Ví dụ

Với $f(x) = x^2$ và biến ngẫu nhiên $X$ phân phối đều trên $\{1, 2, 3, 4\}$, giá trị kỳ vọng $\mathbf E X^2 = 7.5$ lớn hơn $(\mathbf E X)^2 = 6.25$, và hiệu $1.25$ chính là phương sai.

## Khi nào cần dùng?

Chứng minh AM–GM, Hölder, cận dưới ELBO và giải thích tác động của nhiễu lên một hàm lồi.

## Câu hỏi ôn lại

Áp dụng Jensen cho hàm lõm $\log$ cho bất đẳng thức gì?

<details><summary>Xem đáp án</summary>

$\frac1n \sum_i \log x_i \le \log\big(\frac1n \sum_i x_i\big)$. Lấy mũ hai vế được trung bình nhân không vượt trung bình cộng.

</details>

## Thuật ngữ liên quan

- [Hàm lồi](./ham-loi.md)
- [Kỳ vọng](./ky-vong.md)
- [Phương sai](./phuong-sai.md)
