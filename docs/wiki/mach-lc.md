---
title: "Mạch LC"
wikiTerm: mach-lc
prev: false
next: false
---

# Mạch LC

Mạch LC lý tưởng gồm cuộn cảm và tụ, không hao phí năng lượng. Điện tích và dòng dao động điều hòa với $\omega_0=1/\sqrt{LC}$, trao đổi năng lượng giữa điện trường tụ và từ trường cuộn.

<WikiUsage />

## Giải thích kỹ thuật

Chọn q là điện tích trên một bản tụ và i dương đi vào bản đó, nên $i=dq/dt$. Định luật vòng cho $Lq''+q/C=0$. Nghiệm điện tích có dạng

$$
\begin{aligned}
q&=Q\cos(\omega_0t+\phi),\\
i&=-\omega_0Q\sin(\omega_0t+\phi),\\
\omega_0&=\frac1{\sqrt{LC}}.
\end{aligned}
$$

Điện tích và dòng lệch pha một phần tư chu kỳ. Hai điều kiện đầu quyết định biên độ và pha. Dòng âm trong giai đoạn phóng chỉ nghĩa dòng thực ngược chiều dương đã chọn.

Tổng $q^2/(2C)+Li^2/2$ không đổi. Cơ chế giống trao đổi thế năng lò xo và động năng vật nặng, với q tương ứng li độ, i tương ứng vận tốc, L tương ứng khối lượng và 1/C tương ứng độ cứng lò xo.

## Ví dụ

Khi tụ vừa phóng hết điện tích, dòng qua cuộn có độ lớn cực đại và toàn bộ năng lượng nằm trong từ trường.

## Khi nào cần dùng?

Phân tích dao động tự do, tần số và năng lượng điện.

## Câu hỏi ôn lại

Dòng dừng ngay khi tụ hết điện tích trong mạch LC không?

<details><summary>Xem đáp án</summary>

Không. Dòng tiếp tục và nạp tụ với cực tính ngược.

</details>

## Thuật ngữ liên quan

- [Điện dung](./dien-dung.md)
- [Tự cảm](./tu-cam.md)
- [Dao động điều hòa](./dao-dong-dieu-hoa.md)

## Tài liệu tham khảo

Young & Freedman, ấn bản 15, chương 30, trang 988–1009.
