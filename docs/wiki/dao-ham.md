---
title: "Đạo hàm"
wikiTerm: dao-ham
prev: false
next: false
---

# Đạo hàm

Quãng đường đi được trong một giờ không cho biết tốc độ đúng tại một thời điểm. **Đạo hàm** giải quyết câu hỏi cục bộ đó bằng cách xét tỷ số thay đổi trên những khoảng ngày càng nhỏ.

<WikiUsage />

![Hình 1: Tiếp tuyến ghi lại độ dốc cục bộ, không thay thế toàn bộ đường cong.](./img/atlas/derivative.svg)

## Giải thích kỹ thuật

Đạo hàm của $f$ tại $a$ là giới hạn hữu hạn:

$$
f'(a)=\lim_{h\to0}\frac{f(a+h)-f(a)}h.
$$

Tỷ số trong giới hạn là độ dốc dây cung. Khi giới hạn tồn tại, đường thẳng có độ dốc $f'(a)$ đi qua $(a,f(a))$ là tiếp tuyến. Với bước $h$ nhỏ:

$$
f(a+h)\approx f(a)+f'(a)h.
$$

Khả vi tại một điểm kéo theo liên tục tại điểm đó. Chiều ngược lại không đúng: Hàm $|x|$ liên tục tại 0 nhưng có hai độ dốc một phía khác nhau, nên không có đạo hàm tại đó.

Đạo hàm bằng 0 chưa đủ để kết luận cực tiểu. Hàm $x^3$ có đạo hàm bằng 0 tại gốc nhưng vẫn tăng qua gốc. Khi tìm cực trị trên một đoạn đóng, cũng phải kiểm tra hai đầu mút.

## Ví dụ có lời giải

Với $f(x)=x^2$, tại $a=2$:

$$
\begin{aligned}
\frac{f(2+h)-f(2)}h&=4+h,\\
f'(2)&=4.
\end{aligned}
$$

Nếu tăng $x$ từ 2 lên $2{,}01$, xấp xỉ tiếp tuyến cho $f(2{,}01)\approx4{,}04$. Giá trị thật là $4{,}0401$. Sai số $0{,}0001$ chính là phần bình phương của bước $h=0{,}01$.

## Câu hỏi ôn lại

Có thể dùng dấu của $f'(a)$ để kết luận hàm tăng trên toàn trục số không?

::: details Xem lời giải
Không. Dấu tại một điểm là thông tin tại điểm đó. Để suy ra tính đơn điệu trên một khoảng, cần kiểm tra dấu đạo hàm trên khoảng thích hợp và các giả thiết của định lý tương ứng.
:::

## Đọc tiếp

- [Giới hạn](./gioi-han.md)
- [Đạo hàm riêng](./dao-ham-rieng.md)
- [Gradient](./gradient.md)
- [Quy tắc chuỗi](./quy-tac-chuoi.md)

## Tài liệu tham khảo

- [OpenStax, Calculus Volume 1, Defining the Derivative](https://openstax.org/books/calculus-volume-1/pages/3-1-defining-the-derivative).
