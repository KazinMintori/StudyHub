---
title: "Nón lồi"
wikiTerm: non-loi
prev: false
next: false
---

# Nón lồi

Tập C là nón nếu $\theta x \in C$ với mọi $x \in C$ và mọi $\theta \ge 0$. Nón lồi là nón đồng thời là tập lồi, tương đương với việc chứa mọi tổng $\theta_1 x_1 + \theta_2 x_2$ với $\theta_1, \theta_2 \ge 0$. Tổng với hệ số không âm như vậy gọi là tổ hợp nón.

<WikiUsage />

## Giải thích kỹ thuật

**Bốn loại tổ hợp.** Tổ hợp tuyến tính không ràng buộc hệ số, tổ hợp affine đòi tổng hệ số bằng 1, tổ hợp nón đòi hệ số không âm, tổ hợp lồi đòi cả hai điều kiện. Tương ứng với chúng là không gian con, tập affine, nón lồi và tập lồi.

**Các ví dụ quan trọng.** Nón không âm $\mathbb R^n_+$, nón bậc hai $\{(x, t) : \|x\|_2 \le t\}$ và nón ma trận nửa xác định dương $\mathbb S^n_+$. Kiểm tra $b$ có thuộc nón sinh bởi các cột của $A$ hay không là một bài toán khả thi tuyến tính: Tìm $\lambda \succeq 0$ với $A\lambda = b$. Nguồn: Convex Optimization, §2.1.5 và §2.2.3–2.2.5.

## Ví dụ

Góc phần tư thứ nhất $\mathbb R^2_+$ là nón lồi. Hợp của hai tia dương trên hai trục tọa độ là nón nhưng không lồi.

## Khi nào cần dùng?

Mô tả ràng buộc không âm, nón bậc hai, nón ma trận nửa xác định dương và các bất đẳng thức tổng quát.

## Câu hỏi ôn lại

Một nón khác rỗng có luôn chứa gốc tọa độ không?

<details><summary>Xem đáp án</summary>

Có, vì lấy $\theta = 0$ được $0 \cdot x = 0$ thuộc nón.

</details>

## Thuật ngữ liên quan

- [Tập lồi](./tap-loi.md)
- [Ma trận nửa xác định dương](./ma-tran-psd.md)
- [Nón đối ngẫu](./non-doi-ngau.md)
