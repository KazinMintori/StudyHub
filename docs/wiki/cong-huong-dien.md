---
title: "Cộng hưởng điện"
wikiTerm: "cong-huong-dien"
prev: false
next: false
---

# Cộng hưởng điện

RLC nối tiếp cộng hưởng dòng khi cảm kháng bằng dung kháng. Với biên độ nguồn cố định và R dương, dòng lớn nhất tại $\omega_0=1/\sqrt{LC}$, trở kháng nhỏ nhất bằng R.

<WikiUsage />

## Giải thích kỹ thuật

Giữ biên độ nguồn và thay tần số. RLC nối tiếp với $R,L,C$ dương có biên độ dòng $V/Z$. Trở kháng nhỏ nhất khi hai điện kháng bằng nhau:

$$
\omega_0L=\frac1{\omega_0C}\\ \omega_0=\frac1{\sqrt{LC}}\\ Z_{\min}=R.
$$

Nguồn cùng pha dòng tại cộng hưởng. Điện áp cuộn và tụ cùng biên độ, ngược pha nên tổng tức thời bằng không. Từng điện áp có thể lớn hơn điện áp nguồn.

Giảm điện trở làm đỉnh cao và hẹp hơn, nhưng vị trí đỉnh dòng vẫn do L,C quyết định. Một mạch lọc quá hẹp có thể loại các thành phần mang thông tin của tín hiệu cần thu.

Cần nêu đại lượng đang cực đại. Tần số làm dòng cực đại không nhất thiết làm điện áp cuộn hoặc tụ cực đại. Tần số dao động tự do tắt dần cũng không thay được tần số cộng hưởng dòng.

## Ví dụ

$L=0{,}40\,\mathrm{mH}$ và $C=100\,\mathrm{pF}$ cho tần số góc cộng hưởng $5{,}0\times10^6\,\mathrm{rad/s}$, tương ứng khoảng 800 kHz.

## Khi nào cần dùng?

Phân tích mạch dò đài và đường đáp ứng.

## Câu hỏi ôn lại

Điện áp từng cuộn và tụ có bằng không tại cộng hưởng không?

<details><summary>Xem đáp án</summary>

Không. Hai điện áp có cùng biên độ, ngược pha và tổng tức thời bằng không.

</details>

## Thuật ngữ liên quan

- [Mạch LC](./mach-lc.md)
- [Mạch RLC nối tiếp](./mach-rlc.md)
- [Cảm kháng](./cam-khang.md)
- [Dung kháng](./dung-khang.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 31, trang 1018–1040.
