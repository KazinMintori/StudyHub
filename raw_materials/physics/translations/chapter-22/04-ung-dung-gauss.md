<!-- Source: Section22.4, printed729–733, PDF749–753. -->

## 22.4. Áp dụng định luật Gauss

Định luật Gauss đúng với mọi phân bố điện tích và mọi mặt kín. Nhưng để dùng nó tìm điện trường dễ dàng, phân bố phải có đủ đối xứng để tính điện thông. Ngược lại, khi biết trường trên mặt, định luật có thể cho điện tích được bao hoặc điện tích trên mặt vật dẫn.

Trước mỗi bài toán, hãy xác định **đối xứng nào của toàn hệ buộc trường phải có hướng và độ lớn như thế nào**. Việc chọn một mặt đẹp không tự tạo ra đối xứng cho một nguồn vốn không đối xứng.

### Điện tích dư nằm ở đâu trên vật dẫn đặc?

Trong cân bằng tĩnh điện, trường trong vật liệu dẫn bằng không. Nếu trường khác không, những điện tích tự do sẽ chuyển động và trạng thái chưa thể là cân bằng.

![Hình 22.17: Mặt Gauss nằm hoàn toàn trong vật dẫn đặc](../img/young-22/hinh-22-17.png)

Vẽ một mặt Gauss nằm hoàn toàn trong vật liệu. Trường trên mặt bằng không, nên điện tích tổng được bao bằng không. Có thể thu nhỏ hoặc đặt mặt đó quanh một vùng tùy ý trong phần vật liệu. Vì vậy không có điện tích dư trong khối vật liệu của vật dẫn đặc. **Điện tích dư nằm hoàn toàn trên bề mặt.**

Điện tích dư là phần điện tích vượt khỏi lượng ion dương và electron vốn cân bằng trong vật trung hòa. Kết luận không nói rằng vật dẫn không chứa các hạt mang điện. Trường hợp vật dẫn có hốc bên trong sẽ được xét ở mục 22.5.

### Quy trình chọn và dùng mặt Gauss

1. Ghi đại lượng đã biết, đại lượng chưa biết và đại lượng cần tìm. Xác định đối xứng cầu, trụ hay phẳng của phân bố.
2. Với đối xứng cầu, chọn mặt cầu đồng tâm. Với đối xứng trụ, chọn hình trụ đồng trục có hai đáy vuông góc trục. Với đối xứng phẳng, chọn hình trụ có hai đáy song song mặt tích điện.
3. Muốn tìm trường tại một điểm, chọn mặt Gauss đi qua điểm đó. Trong bài có vật dẫn, có thể đặt một đáy bên trong vật liệu, nơi trường bằng không. Với mặt phẳng tích điện, có thể đặt hai đáy đối xứng qua mặt.
4. Chia mặt kín thành những phần dễ xét, chẳng hạn mặt bên và hai đáy. Điện thông tổng bằng tổng điện thông qua từng phần.
5. Trên phần mặt mà trường vuông góc, hướng ra và **có độ lớn không đổi**, điện thông bằng EA. Nếu trường hướng vào, kết quả là −EA. Nếu trường tiếp tuyến mặt hoặc bằng không, điện thông qua phần đó bằng không.
6. Tính điện tích được bao với dấu đầy đủ, rồi giải phương trình Gauss cho đại lượng cần tìm. Cuối cùng kiểm tra sự phụ thuộc theo vị trí, đơn vị và các giới hạn có ý nghĩa.

Đừng suy ra trường bằng không chỉ vì mặt không bao điện tích. Điều được bảo đảm khi ấy là **điện thông tổng** bằng không. Đường sức đi vào và đi ra giúp dự đoán dấu, nhưng số đường vẽ chỉ biểu diễn tỷ lệ với điện thông.

### Ví dụ 22.5: Quả cầu dẫn mang điện

Quả cầu dẫn đặc bán kính R mang điện tích tổng dương q. Tìm trường ở mọi điểm trong và ngoài cầu.

![Hình 22.18: Điện trường của quả cầu dẫn và đồ thị độ lớn theo bán kính](../img/young-22/hinh-22-18.png)

::: solution Chi tiết
**Xác định và thiết lập.** Điện tích dư nằm trên mặt cầu. Khi không có nguồn ngoài phá đối xứng, mọi vị trí trên mặt là tương đương, nên điện tích phân bố đều. Chọn mặt Gauss cầu bán kính r đồng tâm.

Đối xứng loại bỏ mọi thành phần trường tiếp tuyến mặt cầu, vì không có hướng tiếp tuyến được ưu tiên. Độ lớn trường chỉ phụ thuộc khoảng cách r, nên không đổi trên mặt Gauss.

**Thực hiện.** Với $r>R$, mặt bao toàn bộ q. Trường hướng ra và điện thông bằng diện tích cầu nhân E:

$$
\begin{aligned}
E(4\pi r^2) &= \frac{q}{\varepsilon_0}, \\
E &= \frac{kq}{r^2}.
\end{aligned}
$$

Ngay sát mặt ngoài, $E(R^+)=\frac{kq}{R^2}$. Với $r<R$, mặt không bao điện tích dư. Kết hợp đối xứng với Gauss cho $E(4\pi r^2)=0$, nên E = 0. Tại tâm, trường cũng bằng không.

**Đánh giá.** Ngoài cầu, trường giống hệt trường của nguồn điểm q đặt tại tâm. Nếu q âm, trường hướng vào, còn công thức độ lớn dùng |q|. Đồ thị bằng không trong cầu, nhảy tại bề mặt rồi giảm theo $1/r^2$ bên ngoài.

Khi cho R tiến về không, quả cầu trở thành nguồn điểm. Ta đã suy ra trường Coulomb từ Gauss. Trước đó đã suy ra Gauss từ Coulomb, cho thấy sự tương đương giữa hai định luật trong tĩnh điện.

Với vỏ cầu dẫn có hốc cầu đồng tâm không chứa nguồn, cũng chọn mặt cầu trong hốc. Đối xứng buộc trường xuyên tâm và không đổi độ lớn trên mặt, còn điện tích được bao bằng không. Do đó trường trong hốc bằng không.
:::

::: exercise Câu hỏi ngay sau Ví dụ 22.5
Có thể dùng cách chọn mặt tương tự để tìm điện trường giữa một quả cầu tích điện và một vỏ cầu dẫn đồng tâm bao quanh nó hay không?
:::

### Ví dụ 22.6: Dây dài vô hạn tích điện đều

Dây mảnh dài vô hạn có mật độ điện tích dài dương λ. Dùng Gauss để tìm trường.

![Hình 22.19: Mặt Gauss hình trụ đồng trục với dây dài vô hạn](../img/young-22/hinh-22-19.png)

::: solution Chi tiết
**Xác định và thiết lập.** Đối xứng quay quanh dây và đối xứng tịnh tiến dọc dây buộc trường hướng vuông góc dây, với độ lớn chỉ phụ thuộc khoảng cách r. Chọn hình trụ đồng trục bán kính r, chiều dài ℓ tùy ý.

**Thực hiện.** Trường song song hai đáy nên điện thông qua đáy bằng không. Trên mặt bên, trường vuông góc hướng ra và độ lớn không đổi. Diện tích mặt bên là $2\pi r\ell$, điện tích được bao là $\lambda\ell$:

$$
\begin{aligned}
E(2\pi r\ell) &= \frac{\lambda\ell}{\varepsilon_0}, \\
E &= \frac{\lambda}{2\pi\varepsilon_0r}.
\end{aligned}
$$

Nếu λ âm, trường hướng về dây và công thức độ lớn dùng |λ|.

**Đánh giá.** Kết quả trùng tích phân ở Ví dụ 21.10. Dù chỉ điện tích nằm trong hình trụ xuất hiện ở vế phải, **toàn bộ dây** góp tạo trường. Chính toàn dây vô hạn làm hệ có đối xứng cần thiết để tính điện thông dễ dàng.

Với dây hữu hạn, độ lớn trường nhìn chung không đều trên mặt trụ và có thể có thành phần dọc trục. Gauss vẫn đúng, nhưng không cho phép thay điện thông bằng E nhân diện tích mặt bên như trên. Khi ấy cần tích phân Coulomb. Cách chọn mặt trụ còn dùng được cho trụ dài tích điện đều và khoảng giữa hai trụ dẫn đồng trục, như trong các bài cuối chương.
:::

### Ví dụ 22.7: Mặt phẳng vô hạn tích điện đều

Mặt phẳng mỏng vô hạn có mật độ điện tích mặt dương σ. Tìm trường bằng Gauss.

![Hình 22.20: Mặt Gauss hình trụ xuyên qua mặt phẳng tích điện](../img/young-22/hinh-22-20.png)

::: solution Chi tiết
**Xác định và thiết lập.** Trường vuông góc mặt và hai phía có cùng độ lớn. Chọn hình trụ xuyên qua mặt, trục vuông góc mặt và hai đáy cùng diện tích A, đặt đối xứng hai phía.

**Thực hiện.** Trường tiếp tuyến mặt bên nên điện thông qua đó bằng không. Trên **mỗi** đáy, trường hướng ra khỏi thể tích và có điện thông +EA. Điện tích được bao là σA:

$$
\begin{aligned}
2EA &= \frac{\sigma A}{\varepsilon_0}, \\
E &= \frac{\sigma}{2\varepsilon_0}.
\end{aligned}
$$

Nếu σ âm, trường hướng về mặt, điện thông tổng âm và công thức độ lớn dùng |σ|.

**Đánh giá.** Kết quả trùng giới hạn mặt phẳng vô hạn của Ví dụ 21.11, nhưng không cần tích phân theo các vòng. Trường có độ lớn độc lập khoảng cách đến mặt. Mặt Gauss phù hợp biến toàn bộ tích phân thành điện thông qua hai đáy, nhờ đối xứng phẳng.
:::

### Ví dụ 22.8: Hai bản dẫn song song trái dấu

Hai bản dẫn phẳng lớn song song mang điện tích trái dấu và cùng độ lớn. Mật độ trên hai mặt đối diện là +σ và −σ. Tìm điện trường giữa hai bản.

![Hình 22.21: Trường thực có hiệu ứng mép và mô hình lý tưởng của hai bản dẫn](../img/young-22/hinh-22-21.png)

::: solution Chi tiết
**Xác định và thiết lập.** Điện tích trái dấu hút nhau nên phần lớn tập trung trên hai mặt quay vào nhau. Một lượng nhỏ có thể nằm ở mặt ngoài và trường bị loe ở mép. Nếu kích thước bản lớn hơn nhiều khoảng cách giữa chúng, có thể bỏ điện tích mặt ngoài và hiệu ứng mép trong vùng xét xa mép. Trường giữa bản gần đều, điện tích trên hai mặt đối diện gần đều.

Chọn mặt trụ S₁ có một đáy nằm trong vật liệu bản dương và đáy kia ở khoảng giữa. Hai đáy cùng diện tích A.

**Thực hiện.** Đáy trong vật dẫn không có điện thông vì E = 0. Mặt bên song song trường nên không có điện thông. Đáy ở giữa bản có điện thông +EA và mặt trụ bao điện tích +σA:

$$
\begin{aligned}
EA &= \frac{\sigma A}{\varepsilon_0}, \\
E &= \frac{\sigma}{\varepsilon_0}.
\end{aligned}
$$

Trường hướng từ bản dương sang bản âm. Mặt S₄ cho cùng kết quả. Dùng S₂ và S₃ có một đáy trong vật liệu, đáy kia ở ngoài hệ, điện tích được bao bằng không nên trường ngoài bằng không trong mô hình lý tưởng.

**Đánh giá.** Cũng có thể cộng trường của hai mặt mang điện. Mỗi mặt tạo độ lớn $\frac{\sigma}{2\varepsilon_0}$. Ngoài hai bản, hai trường đối nhau và triệt tiêu. Giữa hai bản, chúng cùng chiều và cộng thành $\frac{\sigma}{\varepsilon_0}$. Trường trong vật liệu bản dẫn bằng không. Kết quả trùng Ví dụ 21.12, đồng thời làm rõ điện tích nằm trên những mặt nào của bản dẫn.
:::

### Ví dụ 22.9: Quả cầu cách điện tích điện đều theo thể tích

Điện tích dương Q phân bố đều khắp thể tích quả cầu cách điện bán kính R. Tìm độ lớn trường tại điểm P cách tâm r.

![Hình 22.22: Mặt Gauss trong quả cầu cách điện và đồ thị trường trong, ngoài cầu](../img/young-22/hinh-22-22.png)

::: solution Chi tiết
**Xác định và thiết lập.** Phân bố có đối xứng cầu. Chọn mặt Gauss cầu đồng tâm bán kính r. Trường xuyên tâm và cùng độ lớn trên toàn mặt, nên điện thông bằng $4\pi r^2E$.

**Thực hiện trong cầu.** Với $r<R$, chỉ phần điện tích trong bán kính r được bao. Mật độ thể tích và điện tích được bao là:

$$
\begin{aligned}
\rho &= \frac{Q}{\frac{4}{3}\pi R^3}, \\
Q_{\mathrm{trong}} &= \rho\frac{4\pi r^3}{3} \\
&= Q\frac{r^3}{R^3}.
\end{aligned}
$$

Do đó:

$$
\begin{aligned}
4\pi r^2E &= \frac Q{\varepsilon_0}\frac{r^3}{R^3}, \\
E &= k\frac{Qr}{R^3}.
\end{aligned}
$$

Trường tăng tuyến tính từ không tại tâm đến $\frac{kQ}{R^2}$ ở mặt.

**Thực hiện ngoài cầu.** Với $r>R$, mặt bao toàn bộ Q:

$$
\begin{aligned}
4\pi r^2E &= \frac{Q}{\varepsilon_0}, \\
E &= \frac{kQ}{r^2}.
\end{aligned}
$$

Trường ngoài giống nguồn điểm Q đặt tại tâm. Với Q âm, hướng trường đảo vào tâm và công thức độ lớn dùng |Q|.

**Đánh giá.** Tại r = R, hai biểu thức cho cùng giá trị, nên trường liên tục. Điều này khác cầu dẫn, nơi điện tích tập trung thành một mặt và trường nhảy từ không bên trong sang giá trị khác không bên ngoài. Nói chung, một mặt mang điện có thể làm điện trường gián đoạn về độ lớn, hướng hoặc cả hai.

Cách làm còn áp dụng cho mật độ chỉ phụ thuộc bán kính dù không đều. Với mọi phân bố đối xứng cầu, trường tại r tương đương trường của toàn bộ điện tích nằm trong r dồn về tâm. Những phần điện tích ở bán kính lớn hơn r không tạo trường tổng tại đó. Các mô hình điện tích trong nguyên tử và hạt nhân cũng sử dụng kết quả này.
:::

### Ví dụ 22.10: Suy ra điện tích trên vỏ cầu

Vỏ cầu mỏng bán kính 0,250 m có điện tích chưa biết phân bố đều trên mặt. Ở cách tâm 0,300 m, trường hướng xuyên tâm vào trong và có độ lớn $1.80\times10^2$ N/C. Tìm điện tích trên vỏ.

::: solution Chi tiết
**Xác định và thiết lập.** Phân bố đối xứng cầu, nên chọn mặt Gauss đồng tâm bán kính 0,300 m bao toàn bộ điện tích q. Trường hướng vào khiến thành phần theo pháp tuyến ra ngoài âm.

**Thực hiện.** Điện thông là $-E(4\pi r^2)$, do đó:

$$
\begin{aligned}
q &= -4\pi\varepsilon_0r^2E \\
&= -1.80\times10^{-9}\,\mathrm C \\
&= -1.80\,\mathrm{nC}.
\end{aligned}
$$

**Đánh giá.** Nhờ đối xứng, biết trường tại một điểm trên mặt cầu cũng cho biết trường ở tất cả các điểm khác để tính điện thông. Nếu phân bố không đều và không có đối xứng, một giá trị trường đơn lẻ như vậy nhìn chung không đủ suy ra điện tích bằng Gauss.
:::

::: exercise Câu hỏi ôn lại mục 22.4
Biết điện tích tổng Q, kích thước và hình dạng của vật dẫn không đều như Hình 22.17, có thể chỉ dùng Gauss để tính trường ở một vị trí bất kỳ bên ngoài hay không?
:::

::: solution Giải thích
Không thể làm theo cách rút E ra ngoài tích phân. Một mặt Gauss có hình giống vật dẫn và lớn hơn nó vẫn có điện thông Q/$\varepsilon_0$, nhưng trường không nhất thiết vuông góc mặt và cũng không nhất thiết có cùng độ lớn ở mọi điểm. Biết điện thông chưa xác định được trường tại điểm cần tìm. Tính thuận tiện của Gauss đòi hỏi đối xứng của **phân bố điện tích**, không chỉ hình dạng được chọn cho mặt Gauss.
:::
