## 36.8 Kỹ thuật toàn ảnh (Holography)

### Nguyên lý cơ bản của kỹ thuật ảnh toàn ký

Kỹ thuật toàn ảnh (holography) là một phương pháp ghi nhận và tái tạo lại hình ảnh của một vật thể nhờ vận dụng các hiện tượng giao thoa. Khác với các hình ảnh hai chiều được ghi lại bởi một bức ảnh thông thường hay hệ thống truyền hình, một hình ảnh toàn ký là một hình ảnh ba chiều thực sự. Hình ảnh này có thể được quan sát từ các hướng khác nhau để thấy các mặt khác nhau và từ các khoảng cách khác nhau để thấy sự thay đổi thị sai. Nếu bạn chưa từng thấy một bức ảnh toàn ký, bạn khó có thể tin được điều đó là khả thi!

![Hình 36.28: Phần (a): Ảnh toàn ký là bản ghi trên phim của hệ vân giao thoa hình thành giữa ánh sáng từ nguồn kết hợp và ánh sáng tán xạ từ vật thể. (b) Các hình ảnh được hình thành khi ánh sáng được chiếu qua ảnh toàn ký. Người quan sát nhìn thấy ảnh ảo hình thành phía sau ảnh toàn ký.](../img/young-36/hinh-36-28.png)

Hình 36.28a minh họa quy trình cơ bản để tạo một bức ảnh toàn ký. Ta chiếu sáng vật thể cần chụp toàn ảnh bằng ánh sáng đơn sắc, và đặt một tấm phim ảnh sao cho phim vừa nhận ánh sáng tán xạ từ vật thể, vừa nhận ánh sáng trực tiếp từ nguồn sáng. Trong thực tế, nguồn sáng bắt buộc phải là laser, vì những lý do sẽ được thảo luận ở phần sau. Sự giao thoa giữa ánh sáng trực tiếp và ánh sáng tán xạ tạo thành một hệ vân giao thoa phức tạp được ghi lại trên phim.

Để tạo ra các hình ảnh, ta chỉ cần chiếu ánh sáng qua tấm phim đã tráng (Hình 36.28b). Hai hình ảnh được tạo thành: Một ảnh ảo ở phía tấm phim gần nguồn sáng hơn và một ảnh thật ở phía đối diện.

### Kỹ thuật toàn ảnh và các hệ vân giao thoa

Ta khảo sát cách một điểm sáng được ghi và tái tạo để thấy cơ chế của ảnh toàn ký. Phép phân tích này mở những bước chính, còn lý thuyết toàn diện nằm ngoài phạm vi đang xét. Xét hệ vân giao thoa được hình thành trên một tấm phim âm bản bằng sự chồng chập của một sóng phẳng tới và một sóng cầu, như trong Hình 36.29a. Sóng cầu phát ra từ một nguồn điểm $P$ ở khoảng cách $b_0$ so với tấm phim; $P$ trên thực tế có thể là một vật thể rất nhỏ tán xạ một phần sóng phẳng tới. Ta giả thiết hai sóng là đơn sắc và kết hợp, đồng thời hệ thức pha thỏa mãn điều kiện giao thoa tăng cường tại điểm $O$ trên hình vẽ. Khi đó, giao thoa tăng cường cũng sẽ xảy ra tại bất kỳ điểm $Q$ nào trên phim có khoảng cách tới $P$ lớn hơn khoảng cách từ $O$ tới $P$ một số nguyên lần bước sóng. Nghĩa là, nếu $b_m - b_0 = m\lambda$, với $m$ là một số nguyên, thì sẽ xuất hiện giao thoa tăng cường. Các điểm thỏa mãn điều kiện này tạo thành các đường tròn trên phim có tâm tại $O$, với bán kính $r_m$ được xác định bởi:

![Hình 36.29: Phần (a): Sự giao thoa tăng cường của sóng phẳng và sóng cầu xảy ra trong mặt phẳng của tấm phim tại mỗi điểm Q mà khoảng cách bm từ P lớn hơn khoảng cách b0 từ P đến O một số nguyên lần bước sóng mλ. Đối với điểm Q minh họa, m = 2. (b) Khi một sóng phẳng chiếu vào bản dương bản trong suốt của tấm phim đã tráng, sóng nhiễu xạ gồm một sóng hội tụ tại P' rồi lại phân kỳ, và một sóng phân kỳ dường như xuất phát từ P. Các sóng này lần lượt tạo thành ảnh thật và ảnh ảo.](../img/young-36/hinh-36-29.png)

$$
\begin{aligned}
b_m - b_0 &= \sqrt{b_0^2 + r_m^2} - b_0\\
&= m\lambda
\end{aligned}
\tag{36.20}
$$

với $m = 1, 2, 3, \dots$ là các số nguyên dương.

Giải phương trình này theo $r_m^2$, ta nhận được:

$$
r_m^2 = \lambda(2m b_0 + m^2\lambda)
$$

Thông thường, khoảng cách từ vật tới phim $b_0$ lớn hơn rất nhiều so với bước sóng $\lambda$, và ở vùng gần trục quang (điều kiện cận trục) ta có $m\lambda \ll b_0$, nên số hạng thứ hai $m^2\lambda$ trong ngoặc có thể bỏ qua một cách an toàn so với $2m b_0$:

$$
r_m = \sqrt{2m\lambda b_0}
\tag{36.21}
$$

với $m = 1, 2, 3, \dots$.

Hệ vân giao thoa gồm một tập hợp các vành tròn sáng đồng tâm với bán kính cho bởi Phương trình (36.21). Xen giữa các vành sáng này là các vành tối.

Bây giờ ta tráng phim và làm một bản in dương bản trong suốt, sao cho các vùng vân sáng có độ trong suốt lớn nhất trên phim. Sau đó, ta chiếu vào bản phim một sóng phẳng đơn sắc có cùng bước sóng $\lambda$ như ban đầu. Trong Hình 36.29b, xét một điểm $P'$ ở khoảng cách $b_0$ dọc theo trục từ tấm phim. Tâm của các vân sáng liên tiếp có khoảng cách tới $P'$ khác nhau một số nguyên lần bước sóng, và do đó một cực đại mạnh trong sóng nhiễu xạ sẽ xuất hiện tại $P'$. Nghĩa là ánh sáng hội tụ về $P'$ rồi sau đó phân kỳ từ điểm này sang phía đối diện. Vì vậy, $P'$ là một ảnh thật của điểm $P$.

Tuy nhiên, đây chưa phải là toàn bộ sóng nhiễu xạ. Sự giao thoa của các sóng con truyền ra từ tất cả các vùng trong suốt hình thành nên một sóng cầu thứ hai phân kỳ chứ không hội tụ. Khi dựng ngược sóng này về phía sau tấm phim trong Hình 36.29b, sóng này dường như đang lan truyền ra từ điểm $P$. Như vậy, sóng nhiễu xạ tổng cộng từ ảnh toàn ký là sự chồng chập của một sóng cầu hội tụ tạo thành ảnh thật tại $P'$ và một sóng cầu phân kỳ giống như phát ra từ điểm ảnh ảo $P$.

Nhờ nguyên lý chồng chất sóng, điều đúng đối với việc tạo ảnh của một điểm đơn lẻ cũng đúng cho việc tạo ảnh của số lượng điểm bất kỳ. Tấm phim ghi lại hệ vân giao thoa chồng chập từ vô số điểm khác nhau, và khi ánh sáng được chiếu xuyên qua phim, các điểm ảnh khác nhau được tái tạo đồng thời. Do đó, hình ảnh của một vật thể mở rộng có thể được ghi nhận và tái tạo tương tự như đối với một vật thể nguồn điểm đơn lẻ.

![Hình 36.30: Hai góc nhìn của cùng một bức ảnh toàn ký khi quan sát dưới các góc khác nhau, cho thấy sự thay đổi thị sai trong hình ảnh ba chiều này.](../img/young-36/hinh-36-30.png)

Hình 36.30 thể hiện các bức ảnh chụp cùng một ảnh toàn ký từ hai góc nhìn khác nhau, minh họa sự thay đổi thị sai trong hình ảnh ba chiều này.

### Hai khó khăn thực tế trong kỹ thuật tạo ảnh toàn ký

Khi tạo một ảnh toàn ký, chúng ta phải vượt qua hai trở ngại thực tế:

Thứ nhất, ánh sáng sử dụng bắt buộc phải có tính kết hợp trên những khoảng cách lớn so với kích thước của vật thể và khoảng cách từ vật thể đến phim. Các nguồn sáng thông thường không thỏa mãn yêu cầu này, vì những lý do chúng ta đã thảo luận trong Mục 35.1. Do đó, ánh sáng laser là điều kiện thiết yếu để tạo ảnh toàn ký. (Ánh sáng trắng thông thường có thể được sử dụng để quan sát một số loại ảnh toàn ký nhất định, chẳng hạn như những loại dùng trên thẻ tín dụng ngân hàng.)

Thứ hai, đòi hỏi độ ổn định cơ học cực cao. Nếu có bất kỳ chuyển động tương đối nào giữa nguồn phát, vật thể hoặc tấm phim xảy ra trong quá trình phơi sáng, dù chỉ bằng một phần tư bước sóng ($\lambda/4$), hệ vân giao thoa trên phim cũng sẽ bị nhòe mờ đủ để làm hỏng sự tạo ảnh.

Tuy nhiên, những trở ngại này không phải là không thể vượt qua, và kỹ thuật toàn ảnh đã trở nên quan trọng trong nghiên cứu khoa học, giải trí và rất nhiều ứng dụng công nghệ đa dạng.
