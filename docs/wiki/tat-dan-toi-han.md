---
title: "Tắt dần tới hạn"
wikiTerm: tat-dan-toi-han
prev: false
next: false
---

# Tắt dần tới hạn

Tắt dần tới hạn là ngưỡng giữa dao động và đáp ứng không dao động. Với hệ lò xo có lực cản tuyến tính, $b_c=2\sqrt{km}$. Với mạch RLC nối tiếp, $R_c=2\sqrt{L/C}$.

<WikiUsage />

## Giải thích kỹ thuật

### Hệ lò xo có lực cản tuyến tính

$$
b_c=2\sqrt{km}
$$

Dưới tới hạn, $0<b<b_c$, bao biên giảm nhưng vật còn dao động. Tại và quá tới hạn, vật bị lệch rồi thả từ nghỉ không dao động qua lại.

Với vận tốc đầu tùy ý, cần đọc đầy đủ nghiệm để xác định vật có cắt qua cân bằng một lần hay không. Căn âm trong biểu thức tần số báo không còn tần số dao động thực, không phải một dao động vật lý có “tần số ảo”.

Ở ngưỡng tới hạn, nghiệm cơ học có dạng:

$$
x(t)=(C_1+C_2t)e^{-\beta t}
$$

$$
\beta=\frac{b_c}{2m}
$$

Với vị trí đầu $x_0$ và vận tốc đầu $v_0$, các hằng số thỏa:

$$
C_1=x_0,\qquad C_2=v_0+\beta x_0
$$

### Mạch RLC nối tiếp

Ngưỡng tới hạn RLC được xác định bởi nghiệm kép của phương trình đặc trưng. Với $R^2=4L/C$, tốc độ suy giảm là $\alpha=R/(2L)$ và

$$
q(t)=(a+bt)e^{-\alpha t}.
$$

Điện tích đầu $q_0$ cho $a=q_0$. Dòng đầu $i_0$ cho $b=i_0+\alpha q_0$. Với $i_0=0$ và $q_0$ dương, điện tích giữ dấu dương rồi tiến về không. Với dòng đầu khác không, $a+bt$ có thể bằng không một lần.

Hệ không có các lần đổi dấu lặp lại như dao động. Kết luận không dao động phải được phân biệt với kết luận không bao giờ đổi dấu dưới mọi điều kiện đầu.

## Ví dụ

Với điện tích đầu dương và dòng đầu bằng không, nghiệm tới hạn trở về không mà không dao động lặp lại. Một vật gắn lò xo bị lệch rồi thả từ nghỉ cũng trở về mà không dao động qua lại ở ngưỡng tới hạn.

## Khi nào cần dùng?

Phân loại đáp ứng sau một kích thích và phân biệt ngưỡng tắt dần với ngưỡng mất đỉnh cộng hưởng.

## Câu hỏi ôn lại

Ngưỡng tới hạn của dao động tự do có bằng ngưỡng mất đỉnh biên độ cưỡng bức không?

<details><summary>Xem đáp án</summary>

Không. Ngưỡng tự do là $2\sqrt{km}$, còn đỉnh biên độ li độ ở tần số dương mất khi $b\ge\sqrt{2km}$.

</details>

## Thuật ngữ liên quan

- [Dao động tắt dần](./dao-dong-tat-dan.md)
- [Lực cản tuyến tính](./luc-can-tuyen-tinh.md)
- [Cộng hưởng cơ học](./cong-huong-co-hoc.md)
- [Mạch RLC nối tiếp](./mach-rlc.md)
- [Quá tắt dần](./qua-tat-dan.md)

## Tài liệu tham khảo

Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, mục 14.7–14.8 và chương 30, tr. 988–1009.
