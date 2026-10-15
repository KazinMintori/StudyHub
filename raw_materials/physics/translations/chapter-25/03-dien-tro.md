## 25.3. Điện trở

Trong một dây dẫn, nếu mật độ dòng điện tăng gấp đôi thì điện trường cần thiết có tăng gấp đôi không? Câu trả lời phụ thuộc vào vật liệu. Với vật liệu tuân theo định luật Ohm ở nhiệt độ đang xét, điện trường tỉ lệ thuận với mật độ dòng điện. Từ quan hệ vi mô ấy, ta suy ra điện trở của một dây có tiết diện đều.

### 1. Từ mật độ dòng điện đến điện trở

Với vật liệu có điện trở suất $\rho$, mật độ dòng điện và điện trường tại mỗi điểm liên hệ bởi:

$$
\vec E=\rho\vec J.
\tag{25.7}
$$

Đẳng thức dạng vector áp dụng cho vật liệu đẳng hướng. Nếu vật liệu tuân theo định luật Ohm thì $\rho$ không phụ thuộc độ lớn điện trường đang xét. Khi ấy $\vec E$ cùng hướng và tỉ lệ với $\vec J$.

Xét dây dẫn dài $L$, tiết diện đều $A$, như Hình 25.7. Giả sử dòng điện phân bố đều trên mỗi tiết diện và điện trường dọc dây có độ lớn không đổi. Khi đó:

$$
I=JA,
\qquad
V=EL,
$$

trong đó $V$ là hiệu điện thế giữa đầu có điện thế cao và đầu có điện thế thấp, nên $V>0$. Vì $\vec E$ hướng về phía điện thế giảm, dòng điện quy ước chạy từ đầu điện thế cao đến đầu điện thế thấp. Khi điện tích đi qua dây dẫn, thế năng điện giảm và năng lượng được truyền cho các ion của vật liệu qua va chạm.

![Hình 25.7: Dây dẫn tiết diện đều có mật độ dòng điện phân bố đều và điện trường không đổi dọc chiều dài](../img/young-25/hinh-25-07.png)

**Hình 25.7:** Với dây đồng chất, tiết diện đều và điều kiện dòng phân bố đều, $J$ không đổi trên mỗi tiết diện còn điện trường dọc dây có độ lớn không đổi. Dòng điện hướng từ điện thế cao sang điện thế thấp.

Từ hai hệ thức $I=JA$ và $V=EL$, ta có $J=I/A$ và $E=V/L$. Thay vào $E=\rho J$:

$$
\begin{aligned}
\frac{V}{L} &= \rho\frac{I}{A}, \\
V &= \frac{\rho L}{A}I.
\end{aligned} \tag{25.8}
$$

Đối với một vật dẫn, tỉ số giữa hiệu điện thế hai đầu và dòng điện qua nó được gọi là **điện trở**:

$$
R=\frac{V}{I}.
\tag{25.9}
$$

So sánh với phương trình trên, đối với dây đồng chất, tiết diện đều:

$$
R=\rho\frac{L}{A}.
\tag{25.10}
$$

Điện trở tăng theo chiều dài và điện trở suất, đồng thời giảm khi tiết diện tăng. Điện trở suất là tính chất của vật liệu, còn điện trở còn phụ thuộc kích thước vật dẫn.

![Hình 25.8: Vòi cứu hỏa dài cần chênh lệch áp suất lớn để duy trì dòng nước mạnh](../img/young-25/hinh-25-08.png)

Ống dài cản dòng nước nhiều hơn ống ngắn, và ống hẹp cản nhiều hơn ống rộng. Nhồi bông hoặc cát vào ống làm tăng sức cản, tương tự tăng điện trở suất của vật liệu. Lưu lượng gần tỉ lệ chênh lệch áp suất, như dòng điện và hiệu điện thế trong mô hình Ohm.

Phép tương tự có giới hạn. Lưu lượng nước trong ống thường không tỉ lệ với tiết diện như dòng điện trong một dây đều ở cùng điện trường. Không suy rộng mọi quy luật của dòng điện sang dòng chất lỏng.

Đối với vật liệu Ohm có $R$ không đổi, ta viết:

$$
V=IR.
\tag{25.11}
$$

Phương trình $V=IR$ thường được gọi là định luật Ohm. Nội dung vật lý của định luật là tính tỉ lệ thuận trực tiếp giữa $V$ và $I$ đối với vật liệu và điều kiện cụ thể. Định nghĩa $R=V/I$ vẫn dùng được cho mọi vật dẫn, kể cả vật liệu không Ohm, nhưng nếu tỉ số thay đổi theo điện áp hoặc dòng điện thì không thể gọi quan hệ đó là định luật Ohm.

Đơn vị SI của điện trở là ôm:

$$
1\,\Omega=1\,\mathrm{V/A}.
$$

Các đơn vị thường gặp khác là kilôôm $1\,\mathrm{k\Omega}=10^3\,\Omega$ và mêgaôm $1\,\mathrm{M\Omega}=10^6\,\Omega$. Một dây đồng cỡ 12 gauge dài 100 m có điện trở khoảng $0.5\,\Omega$ ở nhiệt độ phòng. Bóng đèn sợi đốt 100 W, 120 V có điện trở khoảng $140\,\Omega$ khi hoạt động. Nếu cùng dòng điện chạy qua dây và bóng đèn, độ giảm điện thế $V=IR$ lớn hơn nhiều trên bóng đèn. Năng lượng điện thế giảm tại dây tóc được chuyển thành nhiệt và ánh sáng. Dây điện gia dụng cần điện trở nhỏ, nên thường dùng vật liệu có điện trở suất thấp và dây có tiết diện lớn.

### Điện trở linh kiện và mã màu

Điện trở có giá trị xác định được chế tạo sẵn gọi là **resistor** (điện trở linh kiện). Nhiều linh kiện có dạng trụ nhỏ với các vòng màu đánh dấu giá trị. Hai vòng đầu biểu diễn chữ số, vòng thứ ba là hệ số nhân lũy thừa của 10. Vòng thứ tư, nếu có, cho biết sai số cho phép. Ví dụ, xanh lục–tím–đỏ biểu diễn $57\times10^2\,\Omega=5.7\,\mathrm{k\Omega}$. Không có vòng dung sai nghĩa là ±20%, vòng bạc là ±10%, vòng vàng là ±5%. Điện trở linh kiện bán sẵn thường có dải giá trị từ $0.01$ đến $10^7\,\Omega$. Công suất cực đại mà linh kiện chịu được mà không hỏng cũng là thông số quan trọng.

![Hình 25.9: Điện trở linh kiện có các vòng màu biểu thị trị số và dung sai](../img/young-25/hinh-25-09.png)

**Hình 25.9:** Hai vòng gần đầu linh kiện là chữ số, vòng tiếp theo là hệ số nhân, còn vòng cuối cho biết dung sai. Mẫu minh họa có trị số 5.7 kΩ và dung sai ±10%.

**Bảng 25.3. Mã màu điện trở**

| Màu | Chữ số | Hệ số nhân |
| --- | ---: | ---: |
| Đen | 0 | $10^0$ |
| Nâu | 1 | $10^1$ |
| Đỏ | 2 | $10^2$ |
| Cam | 3 | $10^3$ |
| Vàng | 4 | $10^4$ |
| Lục | 5 | $10^5$ |
| Lam | 6 | $10^6$ |
| Tím | 7 | $10^7$ |
| Xám | 8 | $10^8$ |
| Trắng | 9 | $10^9$ |

### Nhiệt độ làm thay đổi điện trở

Điện trở suất thay đổi theo nhiệt độ, vì vậy điện trở của một vật dẫn cụ thể cũng thay đổi. Trong một khoảng nhiệt độ không quá rộng, có thể xấp xỉ:

$$
\begin{aligned}
R(T) &= R_0[1+\alpha(T-T_0)], \\
\Delta R &= R_0\alpha(T-T_0).
\end{aligned} \tag{25.12}
$$

Ở đây, $R_0$ là điện trở tại nhiệt độ mốc $T_0$, còn $\alpha$ là hệ số nhiệt điện trở. Mốc $T_0$ thường được chọn là $0^\circ\mathrm C$ hoặc $20^\circ\mathrm C$. Công thức gần đúng này giả sử kích thước dây không đổi đáng kể khi nhiệt độ thay đổi.

Khi L và A gần như giữ nguyên trong R = ρL/A, hệ số nhiệt của điện trở bằng hệ số nhiệt của điện trở suất trong Bảng 25.2. Do đó có thể dùng cùng α để tính biến thiên của R. Trong giới hạn gần đúng tuyến tính, độ thay đổi điện trở bằng R₀α(T − T₀).

### Quan hệ dòng điện và điện áp

Với một điện trở tuân theo định luật Ohm, đồ thị $I$ theo $V$ là đường thẳng qua gốc tọa độ. Độ dốc bằng $1/R$. Đảo dấu hiệu điện thế làm dòng điện đổi chiều. Khi đó điện trường và mật độ dòng điện cũng đổi chiều.

![Hình 25.10: Đồ thị dòng điện theo điện áp của điện trở Ohm và điôt bán dẫn](../img/young-25/hinh-25-10.png)

**Hình 25.10:** Đồ thị (a) của điện trở Ohm là đường thẳng có độ dốc $1/R$. Đồ thị (b) của điôt không tuyến tính và không đối xứng theo chiều dòng điện.

Một thiết bị không Ohm có thể có quan hệ $I$–$V$ phi tuyến, thậm chí khác nhau khi đảo chiều. Điôt bán dẫn là linh kiện dùng để đổi dòng xoay chiều thành dòng một chiều và thực hiện nhiều chức năng logic. Khi điện thế anôt so với catôt dương, dòng điện tăng theo hàm mũ khi điện áp tăng; khi điện thế âm, dòng điện rất nhỏ. Vì vậy điôt gần giống van một chiều trong mạch.

#### Ví dụ 25.2. Điện trường, hiệu điện thế và điện trở trong dây

Dây đồng 18 gauge có tiết diện $8.17\times10^{-7}\,\mathrm{m^2}$ và dòng điện $1.67\,\mathrm A$. Điện trở suất của đồng ở nhiệt độ đang xét là $1.72\times10^{-8}\,\Omega\,\mathrm m$. Hãy tìm (a) độ lớn điện trường trong dây, (b) hiệu điện thế giữa hai điểm cách nhau $50.0\,\mathrm m$, và (c) điện trở của đoạn dây dài $50.0\,\mathrm m$.

::: details Lời giải Ví dụ 25.2
**Tóm tắt đề bài:** $A=8.17\times10^{-7}\,\mathrm{m^2}$, $I=1.67\,\mathrm A$, $\rho=1.72\times10^{-8}\,\Omega\,\mathrm m$ và $L=50.0\,\mathrm m$.

**Hướng đi:**

- Tính $J=I/A$ vì mật độ dòng điện là dòng điện trên một đơn vị tiết diện.
- Dùng $E=\rho J$ để tìm điện trường trong vật liệu Ohm.
- Với điện trường đều dọc dây, $V=EL$. Sau đó tính điện trở từ $R=\rho L/A$ và kiểm tra bằng $R=V/I$.

(a) Mật độ dòng điện:

$$
\begin{aligned}
J &= \frac{I}{A} \\
&= \frac{1.67}{8.17\times10^{-7}} \\
&= 2.044\times10^6\,\mathrm{A/m^2}.
\end{aligned}
$$

Điện trường trong dây:

$$
\begin{aligned}
E &= \rho J \\
&= (1.72)(2.044)\times10^{-2} \\
&= 3.516\times10^{-2}\,\mathrm{V/m}.
\end{aligned}
$$

(b) Hiệu điện thế giữa hai điểm cách nhau $50.0$ m:

$$
\begin{aligned}
V &= EL \\
&= (3.516\times10^{-2})(50.0) \\
&= 1.758\,\mathrm V \\
&\approx 1.76\,\mathrm V.
\end{aligned}
$$

(c) Điện trở của đoạn dây:

$$
\begin{aligned}
R &= \rho\frac{L}{A} \\
&= \frac{(1.72\times10^{-8})(50.0)}{8.17\times10^{-7}} \\
&= 1.05263\,\Omega \\
&\approx 1.05\,\Omega.
\end{aligned}
$$

Kiểm tra bằng định nghĩa điện trở:

$$
R = \frac{V}{I} = \frac{1.758}{1.67} = 1.05269\,\Omega.
$$

Hai cách tính khớp nhau trong độ chính xác của dữ kiện. Với vật liệu không Ohm, $R=V/I$ vẫn là định nghĩa tại điểm hoạt động ấy, nhưng giá trị có thể đổi khi thay đổi $V$ hoặc $I$. Khi đó $\rho$ cũng có thể phụ thuộc điện trường.
:::

#### Ví dụ 25.3. Điện trở của dây đồng ở các nhiệt độ khác nhau

Một dây đồng có điện trở $1.05\,\Omega$ ở $20^\circ\mathrm C$. Hãy tính điện trở ở $0^\circ\mathrm C$ và $100^\circ\mathrm C$. Hệ số nhiệt điện trở của đồng là $\alpha=0.00393\,({}^\circ\mathrm C)^{-1}$ trong khoảng nhiệt độ này.

::: details Lời giải Ví dụ 25.3
**Tóm tắt đề bài:** $R_0=1.05\,\Omega$ tại $T_0=20^\circ\mathrm C$, $\alpha=0.00393\,({}^\circ\mathrm C)^{-1}$.

**Hướng đi:**

- Thay nhiệt độ cần tính vào biểu thức tuyến tính $R(T)=R_0[1+\alpha(T-T_0)]$.
- Giữ dấu của $T-T_0$: Hạ từ 20°C xuống 0°C làm điện trở giảm, còn tăng lên 100°C làm điện trở tăng.

Ở $0^\circ\mathrm C$:

$$
\begin{aligned}
R(0) &= R_0[1+\alpha(0-T_0)] \\
&= R_0(1-20\alpha) \\
&= R_0(0.9214). \\
R(0) &= 1.05(0.9214)\,\Omega \\
&= 0.9675\,\Omega \\
&\approx 0.97\,\Omega.
\end{aligned}
$$

Ở $100^\circ\mathrm C$:

$$
\begin{aligned}
R(100) &= R_0[1+\alpha(100-T_0)] \\
&= R_0(1+80\alpha) \\
&= R_0(1.3144). \\
R(100) &= 1.05(1.3144)\,\Omega \\
&= 1.3801\,\Omega \\
&\approx 1.38\,\Omega.
\end{aligned}
$$

Từ các giá trị chưa làm tròn, tỉ số giữa điện trở ở 100°C và 0°C là $1.380/0.9675\approx1.43$, tương ứng mức tăng khoảng 43%. Nếu làm tròn trước thành 1.38 Ω và 0.97 Ω như thường ghi trong bảng kết quả, tỉ số là khoảng 1.42, tức mức tăng khoảng 42%. Nếu cần giữ cùng dòng điện, $V=IR$ cho biết điện áp cần thiết cũng tăng theo điện trở. Vì thế, thiết kế mạch hoạt động trong dải nhiệt độ rộng cần xét sự thay đổi này.
:::

#### Câu hỏi kiểm tra



Nếu tăng gấp đôi điện áp trên dây đồng ở Ví dụ 25.2, dòng điện tăng theo hệ số nào khi dòng điện lớn hơn làm dây nóng lên? Chọn (i) đúng gấp đôi, (ii) lớn hơn gấp đôi, hoặc (iii) nhỏ hơn gấp đôi.

<details><summary>Đáp án và giải thích</summary>

Chọn (iii). Nếu nhiệt độ giữ nguyên thì điện trở gần như không đổi và dòng điện sẽ tăng gấp đôi. Nhưng dòng điện lớn hơn làm dây nóng hơn, khiến điện trở đồng tăng. Vì $I=V/R$, điện trở tăng làm dòng điện mới nhỏ hơn hai lần dòng ban đầu. Dây dẫn Ohm đòi hỏi $R=V/I$ không đổi trong các điều kiện so sánh. Dây nóng lên đáng kể không còn đáp ứng giả thiết đó.

</details>

### Tóm tắt

- Với dây đồng chất, tiết diện đều và dòng phân bố đều, $R=\rho L/A$. Điện trở suất mô tả vật liệu, còn điện trở phụ thuộc cả vật liệu lẫn hình học.
- Quan hệ $V=IR$ chỉ là định luật Ohm khi $R$ không đổi theo điểm hoạt động. Định nghĩa $R=V/I$ vẫn áp dụng cho vật dẫn không Ohm.
- Trong khoảng nhiệt độ hẹp, $R(T)\approx R_0[1+\alpha(T-T_0)]$. Khi nhiệt độ tăng, điện trở kim loại thường tăng, còn điện trở suất bán dẫn có xu hướng tăng khi nhiệt độ giảm.
- Đồ thị $I$–$V$ của linh kiện Ohm là đường thẳng qua gốc. Điôt là ví dụ không Ohm có tính dẫn khác nhau theo chiều.

### Tài liệu tham khảo

Young, H. D., & Freedman, R. A. *University Physics with Modern Physics* (ấn bản 15, mục 25.3, tr. 819–822). Pearson.
