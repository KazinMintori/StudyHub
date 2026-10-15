---
title: "Mạch RLC nối tiếp"
wikiTerm: mach-rlc
prev: false
next: false
---

# Mạch RLC nối tiếp

Mạch RLC nối tiếp tự do có phương trình $Lq''+Rq'+q/C=0$. Điện trở tiêu tán năng lượng. Hệ dao động tắt dần khi $R^2<4L/C$, tới hạn khi bằng nhau và quá tắt dần khi lớn hơn.

<WikiUsage />

## Giải thích kỹ thuật

Mạch nối tiếp tự do có $Lq''+Rq'+q/C=0$, với i=q'. Tổng năng lượng thỏa $dU/dt=-Ri^2$ nên không tăng khi R dương.

Trong miền dưới tắt dần, đặt $\alpha=R/(2L)$ và $\omega_d=\sqrt{1/(LC)-\alpha^2}$. Nghiệm là cosin nhân bao mũ. Điều kiện đầu phải tính đạo hàm của cả hai thừa số:

$$
\begin{aligned}
q(0) &= A\cos\phi, \\
i(0) &= -\alpha q(0) - \omega_dA\sin\phi.
\end{aligned}
$$

Vì vậy i(0)=0 không cho phép đặt φ=0 tùy ý. Với q0 khác không, pha phải bù số hạng suy giảm biên độ.

Khi R² bằng 4L/C, nghiệm tới hạn không dao động hình sin. Khi R² lớn hơn, nghiệm là tổng hai mũ thực giảm. Chu kỳ 2π/ωd chỉ dùng khi ωd thực và khác không.

## Ví dụ

Dòng đầu bằng không trong mạch có điện trở vẫn yêu cầu chọn pha bù đạo hàm của bao hàm mũ, thay vì đặt pha bằng không.

## Khi nào cần dùng?

Phân loại đáp ứng điện và áp điều kiện đầu.

## Câu hỏi ôn lại

Nghiệm cosin nhân hàm mũ có dòng đầu bằng không khi tự đặt pha bằng không không?

<details><summary>Xem đáp án</summary>

Nói chung không, vì đạo hàm hàm mũ tạo thêm một số hạng.

</details>

## Thuật ngữ liên quan

- [Mạch LC](./mach-lc.md)
- [Dao động tắt dần](./dao-dong-tat-dan.md)
- [Tắt dần tới hạn](./tat-dan-toi-han.md)
- [Quá tắt dần](./qua-tat-dan.md)

## Tài liệu tham khảo

Young & Freedman, ấn bản 15, chương 30, trang 988–1009.
