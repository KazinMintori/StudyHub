---
title: "Hằng số thời gian RL"
wikiTerm: hang-so-thoi-gian-rl
prev: false
next: false
---

# Hằng số thời gian RL

Hằng số thời gian RL là $\tau=L/R$, với R là tổng điện trở trong vòng. Sau một $\tau$, dòng tăng từ không đạt khoảng 63,2% giá trị cuối, còn dòng suy giảm còn khoảng 36,8% giá trị đầu.

<WikiUsage />

## Giải thích kỹ thuật

Từ nghiệm mũ, thời gian đặc trưng RL là $\tau=L/R$. Đơn vị henry bằng ohm nhân giây, nên $\tau$ đo bằng giây.

Sau $\tau$, dòng suy giảm còn $e^{-1}$ giá trị đầu. Dòng tăng từ không còn thiếu $e^{-1}$ phần giá trị cuối. Thời gian còn một tỉ phần f của dòng đầu là

$$
t=-\tau\ln f,
$$

với 0<f<1. Nếu hỏi năng lượng còn tỉ phần f, thời gian là $-(\tau/2)\ln f$ vì năng lượng phụ thuộc bình phương dòng.

Một hằng số thời gian không có nghĩa hệ đã hoàn toàn ổn định. Mức gần trạng thái cuối phải gắn với sai số yêu cầu.

## Ví dụ

Cuộn $L=0{,}20\,\mathrm H$ trong vòng $R=10\,\Omega$ có $\tau=20\,\mathrm{ms}$.

## Khi nào cần dùng?

Ước lượng và tính thời gian chuyển tiếp của RL.

## Câu hỏi ôn lại

Thời gian giảm nửa dòng có bằng một hằng số thời gian không?

<details><summary>Xem đáp án</summary>

Không. Nó bằng $\tau\ln2$.

</details>

## Thuật ngữ liên quan

- [Mạch RL](./mach-rl.md)
- [Mạch R-C](./mach-rc.md)
- [Năng lượng từ trường](./nang-luong-tu-truong.md)

## Tài liệu tham khảo

Young & Freedman, ấn bản 15, chương 30, trang 988–1009.
