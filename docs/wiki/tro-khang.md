---
title: "Trở kháng"
wikiTerm: "tro-khang"
prev: false
next: false
---

# Trở kháng

Độ lớn trở kháng Z là tỉ số biên độ điện áp với dòng ở một tần số. Với RLC nối tiếp, $Z=\sqrt{R^2+(X_L-X_C)^2}$, đo bằng ôm.

<WikiUsage />

## Giải thích kỹ thuật

Mạng tuyến tính trong trạng thái hình sin ổn định có độ lớn trở kháng:

$$
\begin{aligned}
&Z=V/I\\
&V_{\mathrm{rms}}=I_{\mathrm{rms}}Z.
\end{aligned}
$$

$V,I$ là biên độ, $Z$ đo bằng ôm. Ký hiệu $Z$ ở đây chỉ độ lớn. Trở kháng phức trong cách biểu diễn số phức còn chứa thông tin pha, nên cần phân biệt hai cách dùng ký hiệu.

Với RLC nối tiếp, điện áp điện trở cùng pha dòng. Điện áp cuộn và tụ vuông pha dòng, đồng thời ngược pha nhau. Đặt $X=X_L-X_C$:

$$
Z=\sqrt{R^2+X^2}.
$$

Không áp nguyên công thức này cho RLC song song. Mạch song song có cùng điện áp và cần cộng vector dòng.

Nối tắt vị trí tụ cho $X_C=0$, không phải $C=0$. Hai tình huống ấy mô tả cấu trúc mạch khác nhau.

## Ví dụ

Mạch nối tiếp có $R=300\,\Omega$, $X_L=600\,\Omega$ và $X_C=200\,\Omega$, cho $Z=500\,\Omega$.

## Khi nào cần dùng?

Tính dòng, điện áp và đáp ứng theo tần số.

## Câu hỏi ôn lại

Trở kháng nối tiếp có bằng tổng số học ba đại lượng R, XL, XC không?

<details><summary>Xem đáp án</summary>

Không. Điện áp lệch pha nên phải cộng vector.

</details>

## Thuật ngữ liên quan

- [Cảm kháng](./cam-khang.md)
- [Dung kháng](./dung-khang.md)
- [Góc pha mạch điện](./goc-pha-mach-dien.md)
- [Hệ số công suất](./he-so-cong-suat.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 31, trang 1018–1040.
