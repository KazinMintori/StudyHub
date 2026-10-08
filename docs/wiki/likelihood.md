---
title: "Likelihood"
wikiTerm: likelihood
prev: false
next: false
---

# Likelihood

Likelihood lấy dữ liệu đã quan sát làm cố định và xem mật độ hoặc xác suất của dữ liệu như một hàm theo tham số. Cực đại likelihood chọn tham số làm dữ liệu quan sát có giá trị mật độ hoặc xác suất lớn nhất trong mô hình.

<WikiUsage />

## Giải thích kỹ thuật

**Dữ liệu cố định, tham số thay đổi.** Với mô hình xác suất $p(y\mid\theta)$ và dữ liệu đã thấy $y$, likelihood là $L(\theta;y)=p(y\mid\theta)$ nhìn như một hàm của $\theta$. Nó không phải một phân phối xác suất theo $\theta$ nếu chưa đưa thêm prior và chuẩn hóa.

Dùng log-likelihood biến tích xác suất thành tổng. Vì log tăng nghiêm ngặt, cực đại likelihood tương đương cực đại log-likelihood; thường ta cực tiểu negative log-likelihood. Cần ghi rõ giả định độc lập, phân phối nhiễu và tham số nào được xem là cố định. Nguồn: Convex Optimization, §7.1.

## Ví dụ

Tung đồng xu 10 lần được 7 mặt ngửa cho likelihood theo p tỉ lệ với p⁷(1−p)³.

## Khi nào cần dùng?

Nối giả định xác suất với hàm mất mát và ước lượng tham số.

## Tự kiểm tra

Trong likelihood, dữ liệu hay tham số là đối tượng được thay đổi để tối ưu?

<details><summary>Xem đáp án</summary>

Tham số được thay đổi; dữ liệu đã quan sát được giữ cố định.

</details>

## Thuật ngữ liên quan

- [Phân phối Gauss](./phan-phoi-gauss.md)
- [Bình phương tối thiểu](./binh-phuong-toi-thieu.md)
- [Xác suất có điều kiện](./xac-suat-co-dieu-kien.md)
