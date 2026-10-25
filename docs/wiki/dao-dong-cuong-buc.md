---
title: "Dao động cưỡng bức"
wikiTerm: dao-dong-cuong-buc
prev: false
next: false
---

# Dao động cưỡng bức

Chuyển động của hệ được kích thích bởi ngoại lực tuần hoàn. Trong hệ tuyến tính có cản, sau khi quá độ tắt, tần số đáp ứng ổn định bằng tần số ngoại lực.

<WikiUsage />

## Giải thích kỹ thuật

Xét lực $F(t)=F_{\max}\cos\omega_dt$, với $m>0$, $k>0$, $b>0$. Phương trình là:

$$
m\ddot x+b\dot x+kx=F(t)
$$

Đặt:

$$
\delta=k-m\omega_d^2
$$

Biên độ ổn định là:

$$
A=\frac{F_{\max}}{\sqrt{\delta^2+b^2\omega_d^2}}
$$

Phần dao động tự do có cản còn được cộng vào trong giai đoạn quá độ. Đáp ứng ngay sau lúc bắt đầu kích thích vì vậy có thể khác nghiệm ổn định.

## Ví dụ

Cùng một xích đu có thể bị buộc dao động theo những nhịp khác nhau, nhưng biên độ đáp ứng phụ thuộc nhịp kích thích.

## Khi nào cần dùng?

Phân biệt tần số riêng với tần số đáp ứng và tính cộng hưởng.

## Câu hỏi ôn lại

Đáp ứng cưỡng bức ổn định luôn có tần số riêng của dao động tự do không?

<details><summary>Xem đáp án</summary>

Không. Tần số đáp ứng ổn định bằng tần số lực cưỡng bức. Tần số riêng cùng các tham số khác quyết định miền đáp ứng mạnh.

</details>

## Thuật ngữ liên quan

- [Dao động tắt dần](./dao-dong-tat-dan.md)
- [Cộng hưởng cơ học](./cong-huong-co-hoc.md)
- [Tần số góc của dao động](./tan-so-goc-dao-dong.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục 14.8.
