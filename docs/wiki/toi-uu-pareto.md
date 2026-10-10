---
title: "Tối ưu vector và điểm Pareto"
wikiTerm: toi-uu-pareto
prev: false
next: false
---

# Tối ưu vector và điểm Pareto

Khi hàm mục tiêu nhận giá trị vector, hai phương án có thể không so sánh được. Một phương án khả thi là tối ưu Pareto nếu không có phương án khả thi nào tốt bằng ở mọi mục tiêu và tốt hơn ở ít nhất một mục tiêu. Cực tiểu một tổng có trọng số dương của các mục tiêu luôn cho một điểm Pareto, và với bài toán lồi, thay đổi trọng số quét được gần như toàn bộ đường đánh đổi.

<WikiUsage />

## Giải thích kỹ thuật

**Vô hướng hóa và siêu phẳng tựa.** Nghiệm của bài toán cực tiểu $\lambda^Tf_0(x)$ với $\lambda \succ_{K^*} 0$ là Pareto, và siêu phẳng $\{u : \lambda^Tu = \lambda^Tf_0(x)\}$ là siêu phẳng tựa của tập giá trị đạt được. Với bài toán lồi, mọi điểm Pareto là nghiệm của bài toán vô hướng hóa với một $\lambda \succeq_{K^*} 0$ khác 0, nhưng khi $\lambda$ có thành phần bằng 0, không phải mọi nghiệm đều Pareto.

**Đánh đổi.** Tỉ số $\lambda_i/\lambda_j$ là tỉ giá giữa hai mục tiêu, và tại chỗ đường đánh đổi trơn, $\lambda$ là pháp tuyến của nó. Ước lượng bình phương tối thiểu là tối ưu theo nón PSD trong số các ước lượng tuyến tính không chệch, một trường hợp hiếm có điểm tối ưu thật sự. Nguồn: Convex Optimization, §4.7.

## Ví dụ

Cực tiểu $\|Ax - b\|_2^2 + \mu\|x\|_2^2$ với mỗi $\mu > 0$ cho một điểm Pareto giữa sai số khớp và độ lớn tham số.

## Khi nào cần dùng?

Điều chuẩn trong học máy, cân lợi suất và rủi ro trong đầu tư, thiết kế theo nhiều tiêu chí.

## Câu hỏi ôn lại

Vô hướng hóa với trọng số có thành phần bằng 0 có luôn cho điểm Pareto không?

<details><summary>Xem đáp án</summary>

Không. Khi đó có thể có nhiều nghiệm, và chỉ một số trong đó là Pareto, nên phải kiểm tra thêm.

</details>

## Thuật ngữ liên quan

- [Nón đối ngẫu](./non-doi-ngau.md)
- [Siêu phẳng phân tách và siêu phẳng tựa](./sieu-phang-phan-tach.md)
- [Điều chuẩn: Ridge và lasso](./dieu-chuan.md)
