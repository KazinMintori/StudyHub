## 20.3 Động cơ đốt trong

Động cơ xăng, được ứng dụng rộng rãi trong ô tô và nhiều máy móc công nghiệp, là một ví dụ quen thuộc về động cơ nhiệt. Trong mục này, chúng ta sẽ khảo sát cơ chế sinh công và hiệu suất nhiệt của loại động cơ này. Hình 20.5 mô tả các kỳ hoạt động của một động cơ xăng bốn kỳ điển hình.

![Hình 20.5](../img/young-20/a-hinh-20-05.png)

*Hình 20.5: Chu trình hoạt động của động cơ đốt trong bốn kỳ.*

Hoạt động của động cơ gồm bốn hành trình liên tiếp của piston:

1. **Kỳ nạp (Intake stroke)**: Ban đầu, hỗn hợp không khí và hơi xăng đi vào xi lanh qua van nạp đang mở trong khi piston chuyển động đi xuống. Thể tích của xi lanh tăng từ giá trị cực tiểu $V$ (khi piston ở điểm chết trên) lên giá trị cực đại $rV$ (khi piston ở điểm chết dưới). Đại lượng $r$ được gọi là **tỉ số nén** (compression ratio). Đối với các động cơ ô tô hiện nay, giá trị của $r$ thường nằm trong khoảng từ 8 đến 10.
2. **Kỳ nén (Compression stroke)**: Ở cuối kỳ nạp, van nạp đóng lại và hỗn hợp khí bị nén, gần như đoạn nhiệt, từ thể tích $rV$ trở về thể tích $V$ khi piston chuyển động đi lên.
3. **Kỳ cháy và sinh công (Ignition and Power stroke)**: Hỗn hợp khí bị nén sau đó được kích nổ bởi tia lửa điện từ bugi. Khí cháy nóng giãn nở, gần như đoạn nhiệt, từ thể tích $V$ trở lại thể tích $rV$, tác dụng áp lực lớn đẩy piston đi xuống và sinh công cơ học hữu ích lên trục khuỷu.
4. **Kỳ xả (Exhaust stroke)**: Cuối cùng, van xả mở ra và các sản phẩm cháy bị piston đẩy ra ngoài ống xả khi piston chuyển động đi lên, đưa xi lanh về trạng thái sẵn sàng cho kỳ nạp tiếp theo.

### Chu trình Otto

Hình 20.6 biểu diễn đồ thị $p-V$ cho một mô hình lý tưởng hóa của các quá trình nhiệt động diễn ra trong động cơ xăng. Mô hình lý tưởng này được gọi là **chu trình Otto**.

![Hình 20.6](../img/young-20/a-hinh-20-06.png)

*Hình 20.6: Đồ thị p-V của chu trình Otto, mô hình lý tưởng hóa cho động cơ xăng.*

Các giai đoạn của chu trình Otto diễn ra như sau:
- Tại điểm $a$, hỗn hợp nhiên liệu và không khí đã nạp đầy vào xi lanh ở thể tích $rV$.
- Quá trình $a \to b$: Hỗn hợp khí bị nén đoạn nhiệt từ thể tích $rV$ về thể tích $V$.
- Quá trình $b \to c$: Nhiệt lượng $Q_H$ được cung cấp cho hệ do quá trình đốt cháy nhanh nhiên liệu ở thể tích không đổi $V$.
- Quá trình $c \to d$: Khí cháy nóng giãn nở đoạn nhiệt từ thể tích $V$ đến thể tích $rV$, đẩy piston sinh công (kỳ sinh công).
- Quá trình $d \to a$: Khí được làm mát đẳng tích ở thể tích $rV$ về nhiệt độ môi trường, nhả ra nhiệt lượng $|Q_C|$. Lượng khí này thực tế bị thải ra ngoài và không đi lại vào động cơ, nhưng vì một lượng khí mới tương đương được nạp vào ở chu kỳ sau, ta có thể mô hình hóa đây là một chu trình nhiệt động khép kín.

Ta có thể tính toán chính xác hiệu suất nhiệt của chu trình lý tưởng này. Vì hai quá trình $b \to c$ và $d \to a$ đều diễn ra ở thể tích không đổi, nhiệt lượng $Q_H$ và $Q_C$ liên hệ trực tiếp với nhiệt độ tại các điểm $a$, $b$, $c$ và $d$ thông qua nhiệt dung mol đẳng tích $C_V$:

$$
Q_H = n C_V (T_c - T_b) > 0
$$

$$
Q_C = n C_V (T_a - T_d) < 0
$$

Hiệu suất nhiệt của chu trình được cho bởi phương trình (20.4). Triệt tiêu thừa số chung $n C_V$, ta nhận được:

$$
\begin{aligned}
e &= \frac{Q_H + Q_C}{Q_H} \\
&= \frac{T_c - T_b + T_a - T_d}{T_c - T_b}
\end{aligned}
\tag{20.5}
$$

Để biến đổi biểu thức này về dạng đơn giản hơn, ta sử dụng mối liên hệ giữa nhiệt độ và thể tích trong quá trình đoạn nhiệt của khí lý tưởng: $T V^{\gamma-1} = \text{const}$, với $\gamma = C_p/C_V$ là chỉ số đoạn nhiệt. Đối với hai quá trình đoạn nhiệt $a \to b$ và $c \to d$:

$$
T_a (rV)^{\gamma-1} = T_b V^{\gamma-1}
$$

$$
T_d (rV)^{\gamma-1} = T_c V^{\gamma-1}
$$

Chia cả hai vế của mỗi phương trình cho thừa số chung $V^{\gamma-1}$, ta thu được:

$$
T_b = T_a r^{\gamma-1}
$$

$$
T_c = T_d r^{\gamma-1}
$$

Thay các biểu thức $T_b = T_a r^{\gamma-1}$ và $T_c = T_d r^{\gamma-1}$ vào phương trình (20.5), ta đặt thừa số chung $(T_d - T_a)$ ở cả tử số và mẫu số:

$$
\begin{aligned}
e &= \frac{(T_d - T_a)(r^{\gamma-1} - 1)}{(T_d - T_a)r^{\gamma-1}} \\
&= 1 - \frac{1}{r^{\gamma-1}}
\end{aligned}
\tag{20.6}
$$

Hiệu suất nhiệt xác định bởi phương trình (20.6) luôn luôn nhỏ hơn 1, ngay cả đối với mô hình hoàn toàn lý tưởng này. Với giá trị tỉ số nén điển hình $r = 8$ và chỉ số đoạn nhiệt $\gamma = 1{,}4$ (giá trị chuẩn của không khí):

$$
\begin{aligned}
e &= 1 - \frac{1}{8^{0{,}4}} \\
&\approx 1 - \frac{1}{2{,}297} \\
&\approx 0{,}56 = 56\%
\end{aligned}
$$

Theo phương trình (20.6), hiệu suất nhiệt có thể tăng lên nếu ta tăng tỉ số nén $r$. Tuy nhiên, việc tăng $r$ cũng đồng thời làm tăng nhiệt độ của hỗn hợp xăng và không khí ở cuối kỳ nén đoạn nhiệt. Nếu nhiệt độ này tăng lên quá cao, hỗn hợp sẽ tự động bốc cháy sớm trong khi piston đang nén lên, thay vì cháy êm ả sau khi bugi đánh lửa. Hiện tượng này được gọi là **hiện tượng kích nổ** (pre-ignition hoặc detonation), gây ra tiếng gõ kim loại và có thể phá hủy các chi tiết cơ khí của động cơ. Chỉ số octan của xăng chính là thước đo khả năng chống kích nổ. Tỉ số nén thực tế tối đa đối với các loại xăng cao cấp có chỉ số octan cao vào khoảng 10 đến 13.

Chu trình Otto là một mô hình lý tưởng hóa cao độ. Mô hình này giả thiết hỗn hợp khí cư xử như một khí lý tưởng, bỏ qua ma sát cơ học giữa các chi tiết, sự xoáy rối của dòng khí, sự thất thoát nhiệt qua thành xi lanh và nhiều yếu tố thực tế khác. Hiệu suất nhiệt thực tế của các động cơ xăng thương mại thường chỉ đạt khoảng 35%.

### Chu trình Diesel

Động cơ Diesel có nguyên lý hoạt động tổng thể gần giống với động cơ xăng. Điểm khác biệt quan trọng nhất là không có nhiên liệu trong xi lanh ở đầu kỳ nén. Trong suốt kỳ nén, piston chỉ nén không khí nguyên chất. Ngay trước khi bắt đầu kỳ sinh công, kim phun bắt đầu phun trực tiếp dầu diesel vào trong xi lanh với tốc độ vừa đủ để giữ cho áp suất xấp xỉ không đổi trong giai đoạn đầu của kỳ sinh công. Nhờ nhiệt độ rất cao tạo ra sau quá trình nén đoạn nhiệt không khí, các hạt dầu diesel tự bốc cháy ngay khi vừa được phun vào, do đó động cơ Diesel hoàn toàn không cần bugi đánh lửa.

![Hình 20.7](../img/young-20/a-hinh-20-07.png)

*Hình 20.7: Đồ thị p-V của chu trình Diesel lý tưởng.*

Hình 20.7 biểu diễn chu trình Diesel lý tưởng. Bắt đầu từ điểm $a$, không khí được nén đoạn nhiệt đến điểm $b$, sau đó được cấp nhiệt ở áp suất không đổi đến điểm $c$, tiếp tục giãn nở đoạn nhiệt sinh công đến điểm $d$, và cuối cùng được làm mát đẳng tích trở về điểm $a$.

Vì không có nhiên liệu trong xi lanh trong phần lớn hành trình nén, hiện tượng kích nổ sớm không thể xảy ra. Do đó, tỉ số nén $r$ của động cơ Diesel có thể thiết kế lớn hơn rất nhiều so với động cơ xăng. Điều này nâng cao rõ rệt hiệu suất nhiệt và đảm bảo nhiên liệu tự bốc cháy tin cậy khi được phun vào. Các giá trị tỉ số nén $r$ từ 15 đến 20 là rất phổ biến ở động cơ Diesel. Với các giá trị này và $\gamma = 1{,}4$, hiệu suất lý thuyết của chu trình Diesel lý tưởng đạt khoảng 0,65 đến 0,70 (tức 65% đến 70%).

Tương tự như chu trình Otto, hiệu suất thực tế của mọi động cơ Diesel đều thấp hơn đáng kể so với mức lý thuyết. Mặc dù động cơ Diesel có hiệu suất nhiệt cao và tiết kiệm nhiên liệu hơn động cơ xăng, chúng đòi hỏi quy chuẩn chế tạo cơ khí khắt khe hơn để chịu được áp suất cực cao trong xi lanh, đồng thời hệ thống kim phun nhiên liệu áp suất cao đòi hỏi quy trình bảo dưỡng rất nghiêm ngặt.

::: info Câu hỏi kiểm tra hiểu biết 20.3
Đối với một động cơ hoạt động theo chu trình Otto có kích thước xi lanh cố định và tỉ số nén cố định, những đặc điểm nào sau đây trên đồ thị $p-V$ ở Hình 20.6 sẽ thay đổi nếu ta đốt cháy gấp đôi lượng nhiên liệu trong mỗi chu trình? (Có thể có nhiều hơn một đáp án đúng).

(i) Khoảng cách thẳng đứng giữa hai điểm $b$ và $c$;
(ii) Khoảng cách thẳng đứng giữa hai điểm $a$ và $d$;
(iii) Khoảng cách nằm ngang giữa hai điểm $b$ và $a$.

<details>
<summary>Xem lời giải thích</summary>

**Đáp án đúng**: (i) và (ii).

**Giải thích chi tiết**:

Việc đốt cháy gấp đôi lượng nhiên liệu trong mỗi chu trình đồng nghĩa với nhiệt lượng cung cấp $Q_H$ tăng lên gấp đôi. Do đó, độ tăng áp suất từ trạng thái $b$ đến trạng thái $c$ trong quá trình cháy đẳng tích sẽ lớn hơn, làm tăng khoảng cách thẳng đứng giữa hai điểm $b$ và $c$ trên đồ thị $p-V$.

Vì kích thước xi lanh và tỉ số nén $r$ không đổi, hiệu suất nhiệt $e$ của chu trình không đổi theo phương trình (20.6). Do hiệu suất không đổi, nhiệt lượng thải ra môi trường $|Q_C|$ cũng phải tăng lên theo đúng tỉ lệ như $Q_H$, tức là tăng gấp đôi. Do đó, độ sụt áp suất từ trạng thái $d$ về trạng thái $a$ trong quá trình làm mát đẳng tích cũng lớn hơn, làm tăng khoảng cách thẳng đứng giữa hai điểm $a$ và $d$.

Các kích thước thể tích cực tiểu $V$ và thể tích cực đại $rV$ được cố định bởi cơ cấu cơ học của xi lanh và piston, do đó khoảng cách nằm ngang giữa hai điểm $b$ và $a$ hoàn toàn không thay đổi.
</details>
:::
