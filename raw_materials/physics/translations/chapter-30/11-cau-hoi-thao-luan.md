## Câu hỏi thảo luận

::: exercise Q30.1
Động cơ xe điện bánh hơi hoặc xe buýt điện lấy dòng từ dây điện phía trên qua một cần dài có đầu tiếp xúc trượt. Khi đầu tiếp xúc đi qua chỗ nối dây, tiếp xúc có thể mất trong chốc lát và xuất hiện tia lửa sáng. Giải thích hiện tượng này.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mạch động cơ đang có dòng điện bị gián đoạn ở đầu tiếp xúc. Cần giải thích tia lửa.

**Hướng đi:**

- Dùng suất điện động tự cảm vì cuộn dây động cơ chống lại sự giảm dòng.
- Xét điện trường trong khe tiếp xúc để liên hệ điện áp lớn với sự phóng điện.

Khi tiếp xúc mất, dòng điện có xu hướng giảm rất nhanh. Cuộn dây tạo suất điện động có chiều duy trì dòng đang có. Độ lớn của nó tuân theo

$$
|\mathcal E_L|=L\left|\frac{di}{dt}\right|.
$$

Điện áp giữa hai phía khe hở có thể tăng đủ để ion hóa không khí, tạo hồ quang dẫn điện. Năng lượng từ trường đã tích trữ trong cuộn dây và năng lượng nguồn tiếp tục cung cấp qua hồ quang chuyển thành nhiệt, ánh sáng. Vì vậy tia lửa liên hệ với tự cảm, không chỉ với điện trở ở chỗ tiếp xúc.
:::

::: exercise Q30.2
Từ hệ thức định nghĩa tự cảm suy ra $1\,\mathrm H=1\,\mathrm{Wb/A}$. Từ hệ thức suất điện động tự cảm suy ra $1\,\mathrm H=1\,\Omega\cdot\mathrm s$. Chứng minh hai cách viết đơn vị này tương đương.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** So sánh đơn vị henry biểu diễn qua từ thông và qua điện trở, thời gian.

**Hướng đi:**

- Dùng định luật Faraday để đổi weber thành volt nhân giây.
- Dùng định luật Ohm để đổi volt trên ampere thành ohm.

Từ suất điện động bằng tốc độ biến thiên từ thông, ta có $1\,\mathrm{Wb}=1\,\mathrm V\cdot\mathrm s$. Do đó

$$
\begin{aligned}
1\,\frac{\mathrm{Wb}}{\mathrm A} &= 1\,\frac{\mathrm V\cdot\mathrm s}{\mathrm A} \\
&= 1\,\Omega\cdot\mathrm s.
\end{aligned}
$$

Hai cách viết cùng đo một đại lượng. Cách thứ nhất thể hiện liên hệ giữa dòng và từ thông móc vòng. Cách thứ hai làm rõ vì sao $L/R$ có đơn vị thời gian.
:::

::: exercise Q30.3
Trong Hình 30.1, nếu quay cuộn 2 một góc $90^\circ$ để trục cuộn trở thành thẳng đứng thì hỗ cảm tăng hay giảm? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Giữ hai cuộn ở vị trí đang xét nhưng đổi hướng trục cuộn nhận từ thông.

**Hướng đi:**

- Dùng từ thông qua cuộn 2 để xác định mức liên kết từ giữa hai mạch.
- So sánh hướng từ trường cuộn 1 với pháp tuyến cuộn 2 trước và sau khi quay.

Hỗ cảm giảm vì từ trường do cuộn 1 tạo ra đi xuyên qua mặt các vòng của cuộn 2 ít hơn. Trong mô hình trường gần đều ở vị trí cuộn nhỏ, từ thông chứa thừa số cosin của góc giữa trường và pháp tuyến. Khi trục cuộn 2 vuông góc hướng trường, từ thông qua cuộn có thể bằng không.

Với cuộn có kích thước hữu hạn và trường không đều, không được chỉ thay một góc vào công thức trường đều để khẳng định hỗ cảm chính xác bằng không. Kết luận cần ở đây là sự liên kết từ suy giảm khi quay cuộn theo cách đã nêu.
:::

::: exercise Q30.4
Ống dây hình xuyến quấn sát là một trong số ít cấu hình có thể tính tự cảm dễ dàng. Những đặc điểm nào của cấu hình này tạo ra sự đơn giản đó?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xác định các yếu tố đối xứng và hình học giúp tính tự cảm hình xuyến.

**Hướng đi:**

- Dùng đối xứng quay để chọn đường Ampere tròn trong lõi.
- Dùng các vòng dây cùng móc từ thông để chuyển từ trường thành tự cảm.

Với mô hình quấn đều, sát và đủ nhiều vòng, trường bên trong lõi hướng theo đường tròn đồng tâm. Độ lớn trường không đổi trên từng đường Ampere tròn, nên định luật Ampere cho trực tiếp $B(r)$. Trường ở ngoài lõi được coi là không đáng kể.

Các vòng dây có cùng tiết diện lõi và cùng móc từ thông. Nếu tiết diện nhỏ so với bán kính trung bình, có thể coi trường gần đều trên tiết diện và dùng $\Phi_B\approx BA$. Nếu không, vẫn tính được từ thông bằng tích phân theo bán kính. Cấu hình khép kín cũng tránh phần đầu ống dây, nơi trường của ống dây thẳng thay đổi mạnh.
:::

::: exercise Q30.5
Hai cuộn dây tròn giống nhau, quấn sát, mỗi cuộn có tự cảm $L$, được đặt đồng trục gần như chạm nhau. Tự cảm tương đương bằng bao nhiêu khi mắc nối tiếp và khi mắc song song? Có thể nối để tự cảm tổng bằng không không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai cuộn có cùng tự cảm và liên kết từ mạnh. Phải tính cả hỗ cảm, đồng thời phân biệt hai cách nối chiều quấn.

**Hướng đi:**

- Giữ hỗ cảm $M$ trong phương trình điện áp vì hai cuộn ở gần nhau.
- Xét hai dòng tạo trường cùng chiều hoặc ngược chiều để chọn dấu của số hạng hỗ cảm.
- Chỉ lấy giới hạn $M=L$ sau khi nêu điều kiện liên kết từ hoàn toàn.

Khi mắc nối tiếp, dòng qua hai cuộn bằng nhau. Từ thông móc vòng của cả bộ cho

$$
\begin{aligned}
L_{\mathrm{nt},+} &= 2L+2M, \\
L_{\mathrm{nt},-} &= 2L-2M.
\end{aligned}
$$

Dấu cộng ứng với hai trường hỗ trợ nhau. Dấu trừ ứng với hai trường đối nhau. Khi mắc song song hai cuộn đối xứng, mỗi cuộn mang một nửa tổng dòng, nên

$$
\begin{aligned}
L_{\mathrm{ss},+} &= \frac{L+M}{2}, \\
L_{\mathrm{ss},-} &= \frac{L-M}{2}.
\end{aligned}
$$

Trong giới hạn liên kết hoàn toàn $M=L$, cách nối hỗ trợ cho $4L$ khi nối tiếp và $L$ khi song song. Cách nối đối nhau cho tự cảm bằng không trong mô hình lý tưởng vì từ trường triệt tiêu.

Hai cuộn thực chỉ gần nhau vẫn có từ thông rò, nên thường có $M<L$. Khi ấy nối đối nhau làm tự cảm nhỏ đi nhưng không triệt tiêu hoàn toàn. Cũng không được dùng công thức hai cuộn độc lập, vốn bỏ qua hỗ cảm, cho cấu hình này.
:::

::: exercise Q30.6
Hai cuộn dây tròn quấn sát có cùng số vòng, nhưng bán kính một cuộn gấp đôi cuộn kia. Tự cảm của chúng liên hệ thế nào? Giải thích lập luận.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** So sánh ảnh hưởng của bán kính khi giữ số vòng như nhau.

**Hướng đi:**

- Ước lượng trường trong cuộn tròn theo $B\propto Ni/r$.
- Kết hợp diện tích vòng tỉ lệ với $r^2$ để xét từ thông móc vòng trên một đơn vị dòng.

Trong mô hình các cuộn có hình dạng tương tự và trường được ước lượng bằng một giá trị đại diện, từ thông mỗi vòng tỉ lệ với

$$
\Phi_B\propto\frac{Ni}{r}\,r^2.
$$

Do đó $L=N\Phi_B/i$ tỉ lệ với $N^2r$. Với cùng số vòng, cuộn có bán kính gấp đôi có tự cảm xấp xỉ gấp đôi.

Đây là quan hệ theo mô hình hình học tương tự, không phải quy luật chính xác chỉ cần biết hai bán kính. Tự cảm thực còn phụ thuộc tiết diện dây, bề dày và cách phân bố các vòng. Nếu những tỉ lệ hình học này thay đổi, cần tính từ thông thực thay vì khẳng định hệ số hai tuyệt đối.
:::

::: exercise Q30.7
Muốn chế tạo một điện trở bằng dây quấn quanh lõi trụ, người ta đề nghị quấn nửa chiều dài dây theo một chiều và nửa còn lại theo chiều ngược lại để giảm tự cảm tối đa. Cách đó có đạt mục tiêu không? Vì sao?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai phần dây có chiều quấn đối nhau. Cần xét chúng có thực sự triệt tiêu trường trong cùng không gian không.

**Hướng đi:**

- Dùng năng lượng từ trường để nhận biết tự cảm còn lại, ngay cả khi trường ở xa nhỏ.
- Xét vị trí hai phần quấn. Hai trường chỉ triệt tiêu tốt khi các đoạn mang dòng ngược chiều nằm rất gần nhau.

Chỉ chia ống dây thành hai nửa quấn ngược chiều chưa bảo đảm tự cảm nhỏ nhất. Hai phần có thể làm giảm trường ở một số vùng nhưng mỗi phần vẫn tạo trường mạnh trong vùng riêng. Năng lượng của những trường đó không biến mất chỉ vì các mômen từ tổng cộng đối nhau.

Cách bố trí hiệu quả hơn là gập dây đôi rồi quấn hai nhánh kề nhau. Dòng đi và dòng về ngược chiều trên những đoạn gần như trùng vị trí, nên trường của chúng triệt tiêu tốt hơn. Khi đó phần tự cảm còn lại chủ yếu liên hệ với khoảng cách hữu hạn giữa hai dây và các đoạn nối.
:::

::: exercise Q30.8
Với cùng độ lớn cảm ứng từ $B$, mật độ năng lượng từ trường lớn hơn trong chân không hay trong vật liệu từ? Công thức mật độ năng lượng có hàm ý năng lượng trong ống dây dài mang dòng $I$ tỉ lệ với $1/\mu$ không? Có phải cùng dòng thì lõi sắt từ chứa ít năng lượng hơn lõi không khí không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Phân biệt hai phép so sánh giữ $B$ không đổi và giữ dòng điện không đổi.

**Hướng đi:**

- Dùng $u_B=B^2/(2\mu)$ trong mô hình vật liệu tuyến tính.
- Khi giữ dòng, thay cả quan hệ $B=\mu nI$ vì trường cũng thay đổi theo độ từ thẩm.

Nếu $B$ giống nhau, vật liệu có độ từ thẩm lớn hơn có mật độ năng lượng nhỏ hơn theo công thức đang xét. Vì vậy, với vật liệu thuận từ hoặc sắt từ được mô hình hóa bằng $\mu>\mu_0$, mật độ này nhỏ hơn trong chân không. Vật liệu nghịch từ có $\mu<\mu_0$ cho chiều so sánh ngược lại.

Khi giữ $I$ và hình học ống dây, phải thay độ lớn trường tương ứng:

$$
u_B = \frac{(\mu nI)^2}{2\mu} = \frac12\mu n^2I^2.
$$

Trong mô hình đó, năng lượng tăng theo $\mu$, phù hợp với $U_B=LI^2/2$ và $L\propto\mu$. Không thể giữ $B$ cố định trong một công thức rồi diễn giải kết quả như thể đã giữ $I$ cố định. Với lõi sắt từ có quan hệ từ hóa phi tuyến hoặc từ trễ, biểu thức dùng một độ từ thẩm hằng cần được thay bằng mô hình vật liệu thích hợp.
:::

::: exercise Q30.9
Một mạch RC gồm điện trở, tụ chưa tích điện, pin một chiều và công tắc hở mắc nối tiếp. Một mạch RL gồm điện trở, cuộn cảm, pin một chiều và công tắc hở mắc nối tiếp. So sánh dòng điện (a) ngay sau khi đóng công tắc và (b) rất lâu sau khi đóng. Tụ điện và cuộn cảm ảnh hưởng đến mạch khác nhau thế nào?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai mạch bắt đầu từ tụ chưa tích điện và cuộn cảm chưa mang dòng. Bỏ qua điện trở ngoài các điện trở đã nêu.

**Hướng đi:**

- Dùng tính liên tục của điện áp tụ và dòng cuộn cảm tại thời điểm chuyển mạch.
- Xét trạng thái một chiều ổn định để xác định phần tử nào còn có điện áp hoặc dòng.

Ở mạch RC, điện áp tụ ban đầu bằng không nên dòng ngay sau khi đóng là $\mathcal E/R$. Khi tụ tích điện, dòng giảm và tiến về không. Về lâu dài, điện áp tụ bằng suất điện động pin và tụ không cho dòng một chiều ổn định chạy qua.

Ở mạch RL, dòng ban đầu bằng không và chưa thể nhảy tức thời. Cuộn cảm ban đầu nhận toàn bộ điện áp nguồn, rồi dòng tăng dần. Về lâu dài, suất điện động tự cảm bằng không và dòng tiến đến $\mathcal E/R$.

Như vậy, tụ cản sự thay đổi đột ngột điện áp, còn cuộn cảm cản sự thay đổi đột ngột dòng. Hai kết luận này gắn với các điều kiện đầu đã nêu, không phải quy tắc bỏ qua mọi tụ hoặc mọi cuộn ở thời điểm ban đầu.
:::

::: exercise Q30.10. Mạch vi phân
Dòng qua cuộn cảm không có điện trở biến thiên theo đồ thị Hình Q30.10. (a) Phác dạng tín hiệu trên máy hiện sóng mắc vào hai đầu cuộn cảm. Chấm sáng quét ngang với tốc độ không đổi và độ lệch dọc tỉ lệ với hiệu điện thế hai đầu cuộn. (b) Vì sao mạch có cuộn cảm được gọi là mạch vi phân?

![Hình Q30.10: Dòng điện liên tục tăng và giảm tuyến tính theo thời gian.](img/young-30/hinh-q30-10.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dòng có dạng các đoạn thẳng tam giác. Cần suy ra điện áp, tức đại lượng được máy hiện sóng đo.

**Hướng đi:**

- Chọn điện áp dương ở đầu dòng đi vào cuộn để dùng $v_L=L\,di/dt$.
- Lấy độ dốc từng đoạn của đồ thị dòng. Độ dốc không đổi cho một mức điện áp không đổi.

Gọi độ lớn độ dốc các đoạn tăng và giảm là $k$. Trong đoạn tăng, điện áp bằng $+Lk$. Trong đoạn giảm, điện áp bằng $-Lk$. Vì thế tín hiệu điện áp là sóng vuông luân phiên hai mức, đổi mức tại mỗi đỉnh hoặc đáy của đồ thị dòng. Nếu đảo hai đầu đo thì toàn bộ tín hiệu đổi dấu.

![Lời giải Q30.10: Điện áp dương khi dòng tăng tuyến tính và âm khi dòng giảm tuyến tính, với quy ước điện áp thụ động.](img/young-30/hinh-giai-q30-10.svg)

Cuộn cảm cho điện áp tỉ lệ với đạo hàm của dòng theo thời gian, nên phép đo điện áp thực hiện thao tác vi phân tín hiệu dòng. Ở mô hình lý tưởng, dòng vẫn liên tục trong khi điện áp có thể nhảy giữa hai mức tại chỗ độ dốc đổi dấu.
:::

::: exercise Q30.11
Áp dụng định luật vòng cho mạch LC có tụ ban đầu tích điện đầy cho phương trình $-L\,di/dt-q/C=0$. Khi tụ bắt đầu phóng, dòng tăng từ không. Vì sao phương trình lại cho $L\,di/dt=-q/C<0$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Có vẻ mâu thuẫn giữa dòng tăng và đạo hàm dòng âm. Phải xét dấu của dòng theo chiều quy ước.

**Hướng đi:**

- Phân biệt dòng điện có dấu $i$ với độ lớn $|i|$.
- Giữ quy ước $i=dq/dt$, trong đó $q$ là điện tích có dấu trên bản tụ đã chọn.

Khi $q$ ban đầu dương rồi giảm, $dq/dt<0$, nên dòng theo quy ước là âm. Dòng đi từ $i=0$ sang các giá trị âm có độ lớn tăng dần. Vì vậy $di/dt<0$ hoàn toàn phù hợp với việc cường độ dòng tăng về độ lớn.

Dấu âm không phủ nhận sự phóng điện. Nó chỉ cho biết dòng thực đi ngược chiều dương đã chọn trong phép lập phương trình vòng. Nếu đổi chiều quy ước dòng thì cả quan hệ giữa $i$ và $q$ lẫn các dấu trong phương trình phải đổi nhất quán.
:::

::: exercise Q30.12
Khi suy ra phương trình dao động LC, ta dùng $i=dq/dt$. Nhưng dòng chạy khi tụ phóng làm điện tích trên tụ giảm. Vì sao quan hệ này vẫn đúng, thay vì phải dùng $i=-dq/dt$?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dấu trong quan hệ dòng, điện tích phụ thuộc bản tụ và chiều dòng được chọn.

**Hướng đi:**

- Xác định $q$ là điện tích có dấu trên một bản cụ thể, không phải tổng điện tích của cả tụ.
- Dùng bảo toàn điện tích tại bản đó để liên hệ chiều dòng dương với dấu của $dq/dt$.

Trong quy ước đang dùng, dòng dương đi vào bản có điện tích $q$. Dòng đi vào làm $q$ tăng, nên $i=dq/dt$. Khi bản ấy phóng điện, dòng thực đi ra và $i$ âm, đồng thời $dq/dt$ âm.

Nếu chọn dòng dương đi ra khỏi bản đó thì đúng là $i=-dq/dt$. Hai cách đều được phép, nhưng không được lấy phương trình vòng của một cách rồi ghép với quan hệ dòng, điện tích của cách còn lại.
:::

::: exercise Q30.13
Trong mạch RL của Hình 30.11, khi đóng công tắc $S_1$, hiệu điện thế $v_{ac}$ thay đổi đột ngột nhưng dòng điện không thay đổi đột ngột. Vì sao điện áp có thể nhảy còn dòng thì không?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Một điện áp nguồn hữu hạn được đặt vào mạch có cuộn cảm tại thời điểm đóng công tắc.

**Hướng đi:**

- Dùng quan hệ điện áp cuộn cảm với đạo hàm dòng.
- Tích phân quan hệ đó qua khoảng thời gian chuyển mạch rất ngắn để xét dòng có thể nhảy hay không.

Điện áp nguồn có thể chuyển từ không sang một giá trị hữu hạn ngay khi đóng công tắc lý tưởng. Điện áp cuộn cảm cũng có thể nhảy, nên tốc độ biến thiên dòng đổi ngay. Tuy nhiên, biến thiên dòng là

$$
\Delta i=\frac1L\int v_L\,dt.
$$

Nếu điện áp chỉ hữu hạn, tích phân trên một khoảng thời gian tiến về không cũng tiến về không. Vì vậy dòng không nhảy. Muốn tạo một bước nhảy dòng hữu hạn trong thời gian bằng không phải có xung điện áp vô hạn trong mô hình lý tưởng.
:::

::: exercise Q30.14
Trong mạch RL của Hình 30.11, dòng qua điện trở có luôn bằng dòng qua cuộn cảm không? Dựa vào đâu để biết?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xét mạch khi dòng tăng qua nguồn hoặc giảm trong vòng kín sau khi chuyển công tắc.

**Hướng đi:**

- Theo dõi nhánh nối điện trở với cuộn cảm.
- Áp dụng định luật nút để kiểm tra có nhánh nào lấy bớt dòng giữa hai phần tử không.

Trong hai cấu hình hoạt động được xét ở Hình 30.11, điện trở và cuộn cảm nằm nối tiếp trên cùng đường dòng. Không có chỗ phân nhánh giữa chúng, nên bảo toàn điện tích buộc dòng qua hai phần tử bằng nhau tại cùng một thời điểm.

Kết luận vẫn đúng khi dòng thay đổi. Quy tắc “cùng dòng” đến từ cách mắc nối tiếp, không đến từ trạng thái ổn định. Nó không còn được áp dụng nguyên dạng nếu mắc thêm một nhánh dẫn điện tại nút giữa hai phần tử.
:::

::: exercise Q30.15
Một cuộn cảm đang mang dòng không đổi. Nếu mở công tắc thật nhanh để cố đưa dòng về không ngay lập tức, có thể xuất hiện hồ quang giữa các tiếp điểm. Vì sao? Có thể dừng dòng tức thời về mặt vật lý không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Cuộn đang chứa năng lượng từ trường, trong khi thao tác ngắt mạch cố làm dòng giảm rất nhanh.

**Hướng đi:**

- Dùng suất điện động tự cảm để xác định tác dụng của cuộn khi dòng giảm.
- Xét tính liên tục của dòng và nơi nhận năng lượng từ trường đã tích trữ.

Cuộn tạo suất điện động duy trì chiều dòng cũ. Khi thời gian ngắt rất ngắn, độ lớn điện áp tự cảm có thể rất lớn và đánh thủng không khí ở khe tiếp điểm, tạo hồ quang. Dòng tiếp tục chạy một thời gian qua đường phóng điện này.

Không thể đưa dòng của cuộn có $L>0$ về không trong thời gian bằng không bằng một điện áp hữu hạn. Trong mạch thực, dòng giảm trong một thời gian hữu hạn qua hồ quang, điện dung ký sinh hoặc mạch bảo vệ. Năng lượng từ trường chuyển thành nhiệt, bức xạ hoặc năng lượng điện trường, chứ không biến mất khi mở công tắc.
:::

::: exercise Q30.16
Trong mạch RLC nối tiếp, có thể dùng tiêu chí nào để biết hệ quá tắt dần hay vẫn dao động tắt dần? Chẳng hạn, có thể so sánh năng lượng cực đại được tích trữ trong một chu kỳ với năng lượng tiêu tán trong một chu kỳ không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Cần một tiêu chí phân loại nghiệm RLC, đồng thời đánh giá cách so sánh năng lượng theo chu kỳ.

**Hướng đi:**

- Xét nghiệm đặc trưng của phương trình $Lq''+Rq'+q/C=0$.
- Dùng dấu của biểu thức dưới căn để phân biệt nghiệm có phần dao động và nghiệm chỉ suy giảm.

Tiêu chí chính xác là

$$
\begin{aligned}
&R^2 <\frac{4L}{C}:\quad\omega_d>0, \\
R^2 &= \frac{4L}{C}, \\
&R^2 >\frac{4L}{C}.
\end{aligned}
$$

Dòng thứ nhất ứng với dao động tắt dần. Dòng thứ hai là tắt dần tới hạn. Dòng cuối là quá tắt dần, với hai nghiệm mũ thực suy giảm.

Quan sát các lần đổi dấu lặp lại của điện tích hoặc dòng có thể xác nhận dao động tắt dần. Tuy nhiên, chỉ một lần đi qua không chưa đủ để kết luận hệ dao động, vì điều kiện đầu của nghiệm quá tắt dần cũng có thể tạo một lần đổi dấu.

So sánh năng lượng “trong một chu kỳ” không phải tiêu chí chung độc lập. Hệ quá tắt dần không có chu kỳ dao động, còn chu kỳ của hệ dưới tắt dần thay đổi theo điện trở. Phải xác định bản chất nghiệm trước khi dùng chu kỳ để mô tả lượng năng lượng tiêu tán.
:::
