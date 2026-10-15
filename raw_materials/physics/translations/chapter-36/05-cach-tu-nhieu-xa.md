## 36.5 Cách tử nhiễu xạ

### Cách tử có những khe hoặc rãnh như thế nào?

Chúng ta vừa thấy rằng việc tăng số lượng khe trong một thí nghiệm giao thoa (trong khi vẫn giữ nguyên khoảng cách giữa các khe kề nhau) tạo ra các hình ảnh giao thoa mà ở đó các cực đại nằm ở cùng vị trí, nhưng hẹp dần một cách rõ rệt so với thí nghiệm hai khe. Vì các cực đại này quá hẹp, vị trí góc của chúng, và do đó bước sóng ánh sáng, có thể được đo lường với độ chính xác rất cao. Hiệu ứng này mang lại nhiều ứng dụng thực tiễn quan trọng.

Một dãy gồm một số lượng rất lớn các khe song song, tất cả đều có cùng bề rộng $a$ và cách đều nhau những khoảng cách $d$ giữa các tâm khe, được gọi là **cách tử nhiễu xạ** (diffraction grating). Cách tử đầu tiên được Fraunhofer chế tạo bằng cách sử dụng các sợi dây kim loại mảnh. Ngày nay, cách tử có thể được chế tạo bằng cách dùng đầu kim cương rạch nhiều rãnh cách đều nhau trên bề mặt thủy tinh hoặc kim loại, hoặc bằng phương pháp thu nhỏ qua chụp ảnh một mẫu gồm các sọc đen trắng xen kẽ trên giấy. Đối với một cách tử, những cấu trúc mà chúng ta vốn gọi là khe thường được gọi là các vạch (rulings hoặc lines).

![Hình 36.16: Một phần của cách tử nhiễu xạ truyền qua với khoảng cách giữa tâm hai khe liên tiếp là d.](../img/young-36/hinh-36-16.png)

Trên Hình 36.16, đoạn $GG'$ là mặt cắt ngang của một cách tử truyền qua (transmission grating). Các khe vuông góc với mặt phẳng trang giấy và hình ảnh giao thoa được tạo thành bởi ánh sáng truyền qua các khe. Sơ đồ chỉ biểu diễn sáu khe, trong khi một cách tử thực tế có thể chứa tới vài nghìn khe. Khoảng cách $d$ giữa tâm của hai khe liên tiếp kề nhau được gọi là chu kỳ cách tử (grating spacing). Một chùm sóng phẳng đơn sắc chiếu vuông góc vào cách tử từ phía bên trái. Chúng ta giả định điều kiện trường xa (nhiễu xạ Fraunhofer), tức là hình ảnh được hình thành trên một màn quan sát đặt đủ xa để mọi tia sáng phát ra từ cách tử truyền tới một điểm xác định trên màn đều có thể coi là song song với nhau. Một cách tử thông dụng dùng cho ánh sáng nhìn thấy ($\lambda$ từ $400\text{ nm}$ đến $700\text{ nm}$) thường có khoảng $1000\text{ khe}$ trên mỗi milimet. Giá trị của $d$ là nghịch đảo của số khe trên một đơn vị chiều dài, nên $d$ vào cỡ:

$$
\begin{aligned}
d &= \frac{1}{1000\text{ mm}^{-1}}\\
&= 10^{-3}\text{ mm}\\
&= 1000\text{ nm}
\end{aligned}
$$

Để xuất hiện góc lệch nhiễu xạ đáng kể, chu kỳ cách tử $d$ phải có cùng bậc độ lớn với bước sóng ánh sáng $\lambda$.

### Vị trí các cực đại giao thoa chính

Xét chùm tia sáng song song đơn sắc bước sóng $\lambda$ chiếu vuông góc với bề mặt cách tử. Theo nguyên lý Huygens, mỗi khe hẹp hoạt động như một nguồn phát sóng thứ cấp cùng pha. Để các sóng phát ra từ mọi khe giao thoa tăng cường tại một điểm ở rất xa (hoặc trên tiêu diện của một thấu kính hội tụ), hiệu quang trình giữa hai khe kế tiếp phải bằng một số nguyên lần bước sóng:

$$
\Delta r = d \sin\theta = m\lambda
\tag{36.13}
$$

với $m = 0, \pm 1, \pm 2, \dots$ là bậc của cực đại giao thoa (order of the maximum).

Để thấy rõ bản chất giao thoa nhiều nguồn, ta khai triển tường minh độ lệch pha giữa hai khe liên tiếp. Độ lệch pha $\phi$ giữa sóng xuất phát từ hai khe kề nhau dưới góc lệch $\theta$ được xác định bởi:

$$
\phi = \frac{2\pi}{\lambda} d \sin\theta
$$

Khi có $N$ khe hẹp, biên độ dao động tổng hợp $E$ là sự chồng chập của $N$ dao động điều hòa cùng biên độ $E_0$ với độ lệch pha không đổi $\phi$:

$$
\begin{aligned}
E &= E_1 + E_2 + \dots + E_N\\
&= \sum_{n=0}^{N-1} E_0 \cos(\omega t + n\phi)
\end{aligned}
$$

Tại các góc thỏa mãn $\phi = 2\pi m$, tất cả các vector quay đều cùng hướng, biên độ điện trường tổng hợp đạt cực đại $E_{\text{max}} = N E_0$, kéo theo cường độ sáng cực đại tỷ lệ với $N^2$:

$$
I_{\text{max}} = N^2 I_0
$$

Giữa hai cực đại chính kế tiếp có $N - 1$ cực tiểu (nơi cường độ bằng không) và $N - 2$ cực đại phụ mờ nhạt. Khi $N$ rất lớn (hàng trăm đến hàng nghìn khe), bề rộng góc của các cực đại chính trở nên rất hẹp: Cực tiểu đầu tiên liền kề cực đại chính xuất hiện khi độ lệch pha tăng thêm một lượng $\Delta\phi = 2\pi / N$, tương ứng với sự biến thiên góc rất nhỏ $\Delta\theta \approx \lambda / (N d \cos\theta)$. Do đó, các cực đại chính trở thành những vạch sáng đơn sắc mảnh, sắc nét và tách biệt nhau rõ ràng trên màn quan sát.

Các vạch ứng với $m = \pm 1$ được gọi là vạch quang phổ bậc một, $m = \pm 2$ là vạch quang phổ bậc hai. Nếu chiếu ánh sáng trắng vào cách tử, vạch trung tâm ứng với $m = 0$ vẫn là ánh sáng trắng không bị tán sắc ($\theta = 0$ với mọi bước sóng). Tuy nhiên, tại các bậc $m \neq 0$, do $\sin\theta \propto \lambda$, các bước sóng dài hơn (ánh sáng đỏ) sẽ bị lệch nhiều hơn các bước sóng ngắn (ánh sáng tím). Kết quả là ánh sáng trắng bị phân tách thành một dải quang phổ liên tục nhiều màu sắc trải dài từ tím sang đỏ.

### Cách tử phản xạ

Bên cạnh cách tử truyền qua, người ta còn chế tạo **cách tử phản xạ** (reflection grating). Bề mặt của cách tử phản xạ là một gương phẳng hoặc gương cầu có phủ các đường rãnh song song cách đều. Khi chùm sáng chiếu vào, ánh sáng phản xạ từ các gờ rãnh liên tiếp sẽ giao thoa với nhau. Điều kiện cực đại của chùm phản xạ cũng tuân theo đúng Phương trình (36.13) nếu ánh sáng tới vuông góc với mặt cách tử.

![Hình 36.17: Các hốc siêu nhỏ trên bề mặt đĩa DVD hoạt động như một cách tử phản xạ, phân tách ánh sáng trắng thành các dải màu thành phần.](../img/young-36/hinh-36-17.png)

Một ví dụ trực quan sinh động của cách tử phản xạ trong đời sống thường ngày là bề mặt của đĩa DVD (Hình 36.17). Trên bề mặt đĩa có các rãnh xoắn ốc chứa các hốc ghi dữ liệu cực nhỏ với độ sâu khoảng $0{,}12\ \mu\text{m}$ và khoảng cách hướng tâm đồng đều $d = 0{,}74\ \mu\text{m} = 740\text{ nm}$. Các rãnh này đóng vai trò như một cách tử phản xạ, tán sắc ánh sáng phòng thành các dải màu cầu vồng lấp lánh khi quan sát dưới nhiều góc độ khác nhau.

::: info Ví dụ 36.4: Bề rộng của quang phổ cách tử
Dải bước sóng của quang phổ ánh sáng nhìn thấy trải dài từ khoảng $380\text{ nm}$ (ánh sáng tím) đến $750\text{ nm}$ (ánh sáng đỏ).

a) Tìm giới hạn góc của quang phổ bậc một nhìn thấy được tạo bởi một cách tử phẳng có $600\text{ lines/mm}$ khi chiếu ánh sáng trắng vuông góc với cách tử.

b) Quang phổ bậc một và quang phổ bậc hai có chồng lấn lên nhau không? Quang phổ bậc hai và quang phổ bậc ba thì sao? Các kết luận này có phụ thuộc vào chu kỳ cách tử không?

**Nhận dạng bài toán**: Bài toán yêu cầu xác định khoảng góc nhiễu xạ ứng với các dải bước sóng nhìn thấy ở các bậc quang phổ $m = 1, 2, 3$ và kiểm tra điều kiện chồng lấn giữa các bậc liên tiếp.

**Chuẩn bị**: Chu kỳ cách tử $d$ là nghịch đảo của mật độ vạch trên một đơn vị chiều dài:

$$
\begin{aligned}
d &= \frac{1}{600\text{ lines/mm}}\\
&= \frac{10^{-3}\text{ m}}{600}\\
&\approx 1{,}67 \times 10^{-6}\text{ m}
\end{aligned}
$$

Góc nhiễu xạ ứng với mỗi bước sóng được rút ra từ Phương trình (36.13):

$$
\theta = \arcsin\left(\frac{m\lambda}{d}\right)
$$

**Thực hiện**:

a) Với quang phổ bậc một ($m = 1$), góc lệch của tia tím ($\lambda_v = 380\text{ nm}$) và tia đỏ ($\lambda_r = 750\text{ nm}$) lần lượt là:

$$
\begin{aligned}
\sin\theta_{v1} &= \frac{380 \times 10^{-9}\text{ m}}{1{,}67 \times 10^{-6}\text{ m}}\\
&= 0{,}2275\\
\theta_{v1} &= 13{,}2^{\circ}
\end{aligned}
$$

$$
\begin{aligned}
\sin\theta_{r1} &= \frac{750 \times 10^{-9}\text{ m}}{1{,}67 \times 10^{-6}\text{ m}}\\
&= 0{,}4491\\
\theta_{r1} &= 26{,}7^{\circ}
\end{aligned}
$$

Như vậy, quang phổ bậc một trải dài từ góc $\theta_{v1} = 13{,}2^{\circ}$ đến $\theta_{r1} = 26{,}7^{\circ}$.

b) Xét quang phổ bậc hai ($m = 2$) và bậc ba ($m = 3$):

Với ánh sáng tím ($\lambda_v = 380\text{ nm}$):

$$
\begin{aligned}
\sin\theta_{v2} &= \frac{760 \times 10^{-9}\text{ m}}{1{,}67 \times 10^{-6}\text{ m}}\\
&= 0{,}4551\\
\theta_{v2} &= 27{,}1^{\circ}
\end{aligned}
$$

$$
\begin{aligned}
\sin\theta_{v3} &= \frac{1{,}14 \times 10^{-6}\text{ m}}{1{,}67 \times 10^{-6}\text{ m}}\\
&= 0{,}6826\\
\theta_{v3} &= 43{,}0^{\circ}
\end{aligned}
$$

Với ánh sáng đỏ ($\lambda_r = 750\text{ nm}$):

$$
\begin{aligned}
\sin\theta_{r2} &= \frac{1{,}50 \times 10^{-6}\text{ m}}{1{,}67 \times 10^{-6}\text{ m}}\\
&= 0{,}8982\\
\theta_{r2} &= 63{,}9^{\circ}
\end{aligned}
$$

$$
\begin{aligned}
\sin\theta_{r3} &= \frac{2{,}25 \times 10^{-6}\text{ m}}{1{,}67 \times 10^{-6}\text{ m}}\\
&= 1{,}35 > 1
\end{aligned}
$$

Giá trị $\sin\theta_{r3} > 1$ cho thấy quang phổ bậc ba không thể mở rộng tới bước sóng $750\text{ nm}$. Quang phổ bậc ba bị chặn tại $\theta = 90^{\circ}$. Bạn có thể tìm bước sóng giới hạn tại hướng này không?

Với góc biên ấy, điều kiện cách tử cho:

$$
\begin{aligned}
\lambda_{\text{cut}} &= \frac{d}{3}\\
&= \frac{1{,}67 \times 10^{-6}\text{ m}}{3}\\
&\approx 557\text{ nm}
\end{aligned}
$$

So sánh các dải góc:
- Quang phổ bậc một nằm trong khoảng $[13{,}2^{\circ}, 26{,}7^{\circ}]$.
- Quang phổ bậc hai nằm trong khoảng $[27{,}1^{\circ}, 63{,}9^{\circ}]$. Vì $\theta_{r1} = 26{,}7^{\circ} < \theta_{v2} = 27{,}1^{\circ}$ nên quang phổ bậc một và quang phổ bậc hai không hề chồng lấn lên nhau.
- Quang phổ bậc ba trải từ $\theta_{v3} = 43{,}0^{\circ}$ đến $90^{\circ}$. Vì $\theta_{v3} = 43{,}0^{\circ} < \theta_{r2} = 63{,}9^{\circ}$ nên quang phổ bậc hai và quang phổ bậc ba bị chồng lấn một phần trong vùng góc từ $43{,}0^{\circ}$ đến $63{,}9^{\circ}$.

Các kết luận này không phụ thuộc vào chu kỳ cách tử $d$. Thật vậy, để quang phổ bậc một và bậc hai không chồng lấn, điều kiện cần là $\sin\theta_{r1} < \sin\theta_{v2}$, tương đương với $\lambda_r / d < 2\lambda_v / d$, hay $\lambda_r < 2\lambda_v$. Với dải nhìn thấy, vì $750\text{ nm} < 760\text{ nm}$ (trong đó $2\lambda_v = 760\text{ nm}$), bất đẳng thức này luôn đúng với mọi giá trị $d$. Tương tự, điều kiện chồng lấn giữa bậc hai và bậc ba là $3\lambda_v < 2\lambda_r$, ta có $3\lambda_v = 1140\text{ nm}$ nhỏ hơn $2\lambda_r = 1500\text{ nm}$, luôn thỏa mãn độc lập với $d$.

**Đánh giá**: Nguyên nhân bản chất khiến quang phổ bậc một và bậc hai của ánh sáng nhìn thấy không chồng lấn là mắt người chỉ nhạy với một dải bước sóng tương đối hẹp (tỷ số giữa bước sóng dài nhất và ngắn nhất xấp xỉ $750 / 380 \approx 1{,}97 < 2$). Nếu mắt người có thể cảm nhận được dải bước sóng rộng hơn, chẳng hạn từ $380\text{ nm}$ đến $900\text{ nm}$ (lan sang vùng cận hồng ngoại), thì $\sin\theta_{r1} = 900 / d$, lớn hơn giá trị $\sin\theta_{v2} = 760 / d$ (do $2 \times 380 = 760$), khi đó hai bậc đầu tiên chắc chắn sẽ chồng lấn lên nhau.

**Khái niệm cốt lõi**: Góc lệch của các cực đại chính trong cách tử nhiễu xạ được xác định đồng thời bởi chu kỳ cách tử và bước sóng ánh sáng. Công thức góc giống hệt thí nghiệm giao thoa hai khe, nhưng các vạch cực đại của cách tử hẹp và sắc nét hơn rất nhiều nhờ sự chồng chất của rất nhiều khe.
:::

### Máy quang phổ cách tử

Khả năng phân tách các bước sóng riêng biệt của cách tử được ứng dụng chủ chốt trong các **máy quang phổ cách tử** (grating spectrograph). Ánh sáng phát ra từ một nguồn được chuẩn trực thành chùm song song, chiếu qua cách tử để tán sắc thành các vạch quang phổ, sau đó hội tụ lên cảm biến quang điện tử để đo đạc chính xác bước sóng dựa vào góc lệch $\theta$. Với một cách tử có nhiều khe, các cực đại tạo ra rất sắc nét, cho phép đo góc lệch (và do đó bước sóng) với độ chính xác rất cao.

![Hình 36.18: Ảnh chụp mặt trời trong vùng ánh sáng nhìn thấy (a) và quang phổ mặt trời thu được nhờ cách tử nhiễu xạ với các vạch hấp thụ tối (b).](../img/young-36/hinh-36-18.png)

Một ứng dụng mang tính bước ngoặt của kỹ thuật này là trong thiên văn học. Khi ánh sáng phát ra từ lõi mặt trời truyền qua tầng khí quyển bao quanh mặt trời, các nguyên tử và ion ở đó sẽ hấp thụ chọn lọc những bước sóng đặc trưng, tạo nên các vạch tối trong dải quang phổ liên tục gọi là các vạch hấp thụ (Hình 36.18). Thí nghiệm trong phòng thí nghiệm cho thấy các nguyên tử và ion khác nhau hấp thụ ánh sáng ở những bước sóng khác nhau. Bằng cách đối chiếu các kết quả phòng thí nghiệm này với bước sóng của các vạch hấp thụ trong quang phổ ánh sáng mặt trời, các nhà thiên văn học có thể suy ra thành phần hóa học của khí quyển mặt trời. Kỹ thuật tương tự cũng được dùng để phân tích thành phần hóa học của các thiên hà cách xa hàng triệu năm ánh sáng.

![Hình 36.19: Sơ đồ nguyên lý của máy quang phổ cách tử dùng trong thiên văn học. Lưu ý rằng ánh sáng không chiếu vuông góc với bề mặt cách tử nên các vị trí cực đại cường độ được xác định bởi biểu thức có đôi chút khác biệt so với Phương trình (36.13).](../img/young-36/hinh-36-19.png)

Hình 36.19 minh họa một thiết kế máy quang phổ cách tử dùng trong thiên văn học. Trong sơ đồ này, người ta sử dụng một cách tử truyền qua (trong các bố trí khác, cách tử phản xạ cũng có thể được sử dụng). Cần lưu ý rằng ánh sáng không chiếu vuông góc với bề mặt cách tử (chiếu xiên), do đó các vị trí cực đại cường độ được xác định bởi một biểu thức có đôi chút khác biệt so với Phương trình (36.13). Trong các thiết kế cũ hơn, người ta sử dụng lăng kính thay cho cách tử và quang phổ được tạo thành nhờ sự tán sắc chứ không phải nhiễu xạ. Tuy nhiên, giữa bước sóng và góc lệch của lăng kính không có mối liên hệ đơn giản, lăng kính hấp thụ một phần ánh sáng truyền qua, và chúng kém hiệu quả hơn đối với nhiều bước sóng ngoài vùng nhìn thấy vốn rất quan trọng trong thiên văn học. Vì những lý do này cùng nhiều ưu điểm khác, cách tử luôn được ưu tiên lựa chọn trong các ứng dụng đo lường chính xác.

Quy trình hoạt động của thiết bị gồm sáu bước liên kết:
1. Ánh sáng từ kính thiên văn được truyền dọc theo sợi cáp quang (không vẽ trong hình) và đi ra tại đây.
2. Ánh sáng tới gương cầu lõm và phản xạ thành chùm tia song song.
3. Ánh sáng đi qua cách tử nhiễu xạ.
4. Các thấu kính hướng ánh sáng đã nhiễu xạ tới gương cầu lõm thứ hai.
5. Gương cầu lõm hội tụ ánh sáng về tiêu điểm.
6. Bộ thu điện tử (tương tự cảm biến trong máy ảnh kỹ thuật số) ghi nhận quang phổ.

### Năng suất phân giải phổ

Trong quang phổ học, việc phân biệt hai bước sóng rất gần nhau $\lambda$ và $\lambda + \Delta\lambda$ là vô cùng quan trọng. Hiệu bước sóng nhỏ nhất $\Delta\lambda$ mà một máy quang phổ có thể phân biệt được mô tả thông qua **năng suất phân giải phổ** (chromatic resolving power) $R$, được định nghĩa là:

$$
R = \frac{\lambda}{\Delta\lambda}
\tag{36.14}
$$

Chẳng hạn, khi các nguyên tử natri bị kích thích nhiệt, chúng phát xạ mạnh ở hai bước sóng màu vàng $589{,}00\text{ nm}$ và $589{,}59\text{ nm}$. Một máy quang phổ có thể vừa vặn phân biệt được hai vạch này trong quang phổ (gọi là vạch đôi natri - sodium doublet) có năng suất phân giải phổ là:

$$
\begin{aligned}
R &= \frac{\lambda}{\Delta\lambda}\\
&= \frac{589{,}00\text{ nm}}{0{,}59\text{ nm}} = 1000
\end{aligned}
$$

(Ta có thể quan sát trực tiếp các bước sóng này khi đun sôi nước có hòa tan muối ăn trên bếp gas: Nếu nước sôi trào vào ngọn lửa, natri hòa tan từ muối sẽ phát ra một luồng sáng màu vàng rực).

Để thiết lập công thức tính năng suất phân giải của cách tử dùng trong máy quang phổ, ta sử dụng tiêu chuẩn phân giải: Hai bước sóng khác nhau cho các cực đại nhiễu xạ ở các góc lệch hơi khác nhau. Như một tiêu chuẩn hợp lý (dù mang tính quy ước), ta giả định rằng có thể phân biệt hai vạch thành hai đỉnh tách rời nếu cực đại của bước sóng này trùng đúng vào cực tiểu đầu tiên liền kề của bước sóng kia.

Theo phân tích ở phần trước, cực đại bậc $m$ xuất hiện khi độ lệch pha giữa hai khe liên tiếp là $\phi = 2\pi m$. Cực tiểu đầu tiên bên cạnh cực đại này xuất hiện khi độ lệch pha là $\phi = 2\pi m + 2\pi / N$, trong đó $N$ là số lượng khe. Độ lệch pha còn được xác định bởi $\phi = (2\pi d \sin\theta) / \lambda$, do đó khoảng góc $d\theta$ tương ứng với độ tăng pha nhỏ $d\phi$ có thể nhận được từ vi phân của phương trình này:

$$
d\phi = \frac{2\pi d \cos\theta d\theta}{\lambda}
$$

Khi $d\phi = 2\pi / N$, lượng này tương ứng với khoảng góc $d\theta$ giữa cực đại và cực tiểu liền kề đầu tiên. Do đó $d\theta$ được xác định bởi:

$$
\begin{aligned}
\frac{2\pi}{N} &= \frac{2\pi d \cos\theta d\theta}{\lambda}\\
d \cos\theta d\theta &= \frac{\lambda}{N}
\end{aligned}
$$

Bây giờ ta cần tìm khoảng cách góc $d\theta$ giữa các cực đại của hai bước sóng hơi khác nhau. Vị trí của các cực đại này tuân theo $d \sin\theta = m\lambda$, và vi phân của phương trình này cho:

$$
d \cos\theta d\theta = m d\lambda
$$

Theo tiêu chuẩn phân giải của chúng ta, giới hạn phân giải đạt được khi hai khoảng cách góc này bằng nhau. Cân bằng hai biểu thức của đại lượng $(d \cos\theta d\theta)$, ta nhận được:

$$
\begin{aligned}
\frac{\lambda}{N} &= m d\lambda\\
\frac{\lambda}{d\lambda} &= Nm
\end{aligned}
$$

Nếu $\Delta\lambda$ nhỏ, ta có thể thay $d\lambda$ bằng $\Delta\lambda$, và năng suất phân giải phổ $R$ là:

$$
R = \frac{\lambda}{\Delta\lambda} = Nm
\tag{36.15}
$$

Số lượng khe $N$ càng lớn thì độ phân giải càng tốt. Ngoài ra, bậc $m$ của cực đại hình ảnh nhiễu xạ càng cao thì độ phân giải cũng càng tốt.

::: warning Cảnh báo: Phân biệt các cách dùng ký hiệu d
Cần lưu ý không nhầm lẫn giữa chu kỳ cách tử $d$ (khoảng cách giữa các khe) với ký hiệu vi phân "$d$" trong khoảng góc $d\theta$ hoặc trong độ tăng lệch pha $d\phi$!
:::

::: tip Ứng dụng sinh học: Phát hiện ADN bằng hiện tượng nhiễu xạ
![Ứng dụng: Mẫu dung dịch ADN được đưa vào phép đo hấp thụ ánh sáng.](../img/young-36/ung-dung-36-adn.png)

Cách tử nhiễu xạ được sử dụng trong một thiết bị phòng thí nghiệm phổ biến là máy quang phổ kế (spectrophotometer). Ánh sáng chiếu qua cách tử nhiễu xạ được phân tách thành các bước sóng thành phần. Một khe hẹp được dùng để chặn lại tất cả ngoại trừ một dải bước sóng rất hẹp, tạo ra chùm sáng gần như đơn sắc hoàn hảo. Thiết bị sau đó đo lượng ánh sáng bị hấp thụ bởi một dung dịch chứa các phân tử sinh học. Chẳng hạn, ống mẫu chứa dung dịch ADN vốn trong suốt với ánh sáng nhìn thấy, nhưng hấp thụ rất mạnh ánh sáng tử ngoại có bước sóng chính xác $260\text{ nm}$. Do đó, bằng cách rọi sáng mẫu bằng ánh sáng $260\text{ nm}$ và đo lượng ánh sáng bị hấp thụ, chúng ta có thể xác định nồng độ ADN trong dung dịch.
:::

### Câu hỏi tự kiểm tra 36.5

Cần số lượng khe tối thiểu là bao nhiêu trên một cách tử để có thể phân giải được vạch đôi natri ở quang phổ bậc bốn?
- (i) 250
- (ii) 400
- (iii) 1000
- (iv) 4000

::: details Trả lời
Đáp án đúng là **(i)**.

Như đã mô tả trong lý thuyết, năng suất phân giải phổ cần thiết là $R = Nm = 1000$.

Ở quang phổ bậc một ($m = 1$), chúng ta cần $N = 1000\text{ khe}$. Nhưng ở quang phổ bậc bốn ($m = 4$), chúng ta chỉ cần số lượng khe là:

$$
\begin{aligned}
N &= \frac{R}{m}\\
&= \frac{1000}{4} = 250\text{ khe}
\end{aligned}
$$

(Những con số này chỉ mang tính xấp xỉ do tính chất quy ước của tiêu chuẩn phân giải và do các cách tử trong thực tế luôn có những khiếm khuyết nhỏ về hình dạng cũng như khoảng cách giữa các khe).
:::
