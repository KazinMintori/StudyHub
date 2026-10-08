---
title: "Phép chiếu lên tập lồi"
wikiTerm: phep-chieu
prev: false
next: false
---

# Phép chiếu lên tập lồi

Phép chiếu Euclid của z lên tập lồi đóng C là điểm của C gần z nhất, ký hiệu $\Pi_C(z)$. Điểm p là hình chiếu khi và chỉ khi $p \in C$ và $(p - z)^T (y - p) \ge 0$ với mọi $y \in C$.

<WikiUsage />

## Giải thích kỹ thuật

**Đặc trưng.** Hình chiếu tồn tại và duy nhất với mọi tập lồi đóng khác rỗng. Điều kiện $(p - z)^T (y - p) \ge 0$ chính là điều kiện tối ưu bậc nhất của bài toán cực tiểu $\tfrac12\|y - z\|_2^2$ trên $C$.

**Gradient có chiếu.** Với bài toán lồi khả vi, $x$ tối ưu khi và chỉ khi $x = \Pi_C(x - t\nabla f_0(x))$ với $t > 0$. Lặp $x^{(k+1)} = \Pi_C(x^{(k)} - t\nabla f_0(x^{(k)}))$ là phương pháp gradient có chiếu. Phép chiếu có công thức đóng cho hình hộp, quả cầu Euclid, nón không âm và siêu phẳng. Nguồn: Convex Optimization, §4.2.3 và §8.1.

## Ví dụ

Chiếu $z = (1.6, 0.5)$ lên hình vuông $[0, 1]^2$ bằng cách kẹp từng tọa độ vào đoạn $[0, 1]$ được $(1, 0.5)$.

## Khi nào cần dùng?

Phương pháp gradient có chiếu cho bài toán có ràng buộc đơn giản như hình hộp, quả cầu hay nón không âm.

## Câu hỏi ôn lại

Nếu C là một không gian con thì phép chiếu Euclid có dạng gì quen thuộc?

<details><summary>Xem đáp án</summary>

Đó là phép chiếu trực giao lên không gian con, một ánh xạ tuyến tính.

</details>

## Thuật ngữ liên quan

- [Tập lồi](./tap-loi.md)
- [Gradient](./gradient.md)
- [Chuẩn vector](./chuan.md)
