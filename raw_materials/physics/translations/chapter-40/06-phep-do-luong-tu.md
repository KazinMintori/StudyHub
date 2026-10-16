## 40.6. Phép đo trong cơ học lượng tử

Biết hàm sóng cho phép tính những kết quả có thể thu được khi đo. Nhưng sau khi thu được một kết quả, trạng thái của hệ có còn như trước hay không?

Ta xét lại hạt trong hộp để phân biệt ba việc: Trạng thái trước phép đo, kết quả của một lần đo và trạng thái ngay sau phép đo. Cũng cần tách một mô hình đo lý tưởng khỏi tương tác cụ thể giữa hạt với dụng cụ.

### Quan sát một vật cổ điển cũng có tương tác

Một đĩa hockey trượt không ma sát giữa hai vách có cơ năng bằng động năng. Tại một thời điểm, nó chuyển động theo một trong hai chiều:

$$
p_x=\pm\sqrt{2mE}.
\tag{40.49}
$$

Ta có thể nhìn hướng chuyển động để xác định dấu. Tuy nhiên, muốn nhìn thấy đĩa phải có ánh sáng. Photon va chạm với đĩa và truyền động lượng, nên hành động quan sát cũng tác động lên vật được quan sát.

Với khối lượng $m=0{,}165\,\mathrm{kg}$ và tốc độ $v=1{,}00\,\mathrm{m/s}$, đĩa có động lượng

$$
p=mv=0{,}165\,\mathrm{kg\,m/s}.
$$

Một photon ánh sáng nhìn thấy, bước sóng $500\,\mathrm{nm}$, chỉ có động lượng

$$
\begin{aligned}
p_\gamma&=\frac{h}{\lambda}\\
&\approx1{,}33\times10^{-27}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

Ngay cả khi tập trung toàn bộ ánh sáng của nguồn $100\,\mathrm W$ lên đĩa trong $1{,}00\,\mathrm s$, tổng năng lượng chùm sáng là $100\,\mathrm J$. Nếu các photon cùng hướng, tổng động lượng của chùm chỉ bằng

$$
\begin{aligned}
P_\gamma&=\frac{100\,\mathrm J}{c}\\
&\approx3{,}33\times10^{-7}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

Động lượng trao đổi còn phụ thuộc sự hấp thụ hay phản xạ, nhưng với những số liệu này ảnh hưởng lên đĩa vẫn rất nhỏ. Đây là lý do nhiều phép đo cổ điển có thể được thực hiện mà không làm thay đổi đáng kể đại lượng đang đo.

### Trạng thái dừng trong hộp là một sóng đứng

Một hạt trong hộp vô hạn rộng $L$ ở mức năng lượng $E_n$ có hàm sóng

$$
\begin{aligned}
\Psi(x,t)&=\psi_n(x)e^{-iE_nt/\hbar}\\
&=\psi_n(x)e^{-i\omega_nt}.
\end{aligned}
\tag{40.50}
$$

Ở đây $\omega_n=E_n/\hbar$, còn hàm sóng không phụ thuộc thời gian là

$$
\psi_n(x)=\sqrt{\frac2L}
\sin\frac{n\pi x}{L}.
\tag{40.51}
$$

Công thức này áp dụng trong $0\le x\le L$, với $n=1,2,3,\ldots$. Hàm sóng bằng không bên ngoài hộp và tại hai vách.

Đặt

$$
k_n=\frac{n\pi}{L},
\qquad
p_n=\hbar k_n.
$$

Liên hệ năng lượng cho $p_n=\sqrt{2mE_n}$. $p_n$ là thang động lượng gắn với mức năng lượng, chưa phải phát biểu rằng hạt bị giam giữ có sẵn một giá trị động lượng xác định.

Dùng công thức Euler để khai triển hàm sin:

$$
\sin(k_nx)=\frac{e^{ik_nx}-e^{-ik_nx}}{2i}.
$$

Vì vậy,

$$
\psi_n(x)=\frac{e^{ik_nx}-e^{-ik_nx}}{i\sqrt{2L}}.
\tag{40.52}
$$

Phép khai triển cho thấy hai thành phần đối truyền trên khoảng của hộp. Để ghi rõ cả thừa số thời gian mà vẫn giữ công thức dễ đọc, đặt

$$
u_+(x,t)=\frac{e^{ik_nx}e^{-i\omega_nt}}{i\sqrt{2L}}.
$$

$$
u_-(x,t)=\frac{e^{-ik_nx}e^{-i\omega_nt}}{i\sqrt{2L}}.
$$

Khi đó, hàm sóng đầy đủ là tổng hai thành phần dưới đây. Cả $u_+$ và $u_-$ đều được đánh giá tại cùng $(x,t)$:

$$
\Psi(x,t)=u_+-u_-.
\tag{40.53}
$$

Hai thành phần có cùng năng lượng và hệ số có cùng độ lớn. Sóng đứng không phải một hạt cổ điển lúc chạy sang phải, lúc chạy sang trái theo một quỹ đạo đã xác định. Giá trị kỳ vọng của động lượng bằng không ở mọi thời điểm, còn giá trị trung bình theo thời gian của đĩa hockey mới bằng không khi xét cả hai chiều chuyển động.

::: warning Phạm vi của mô hình hai thành phần

Đẳng thức (40.52) đúng trên khoảng của hộp. Tuy nhiên, hai sóng phẳng riêng lẻ không thỏa điều kiện bằng không tại các vách. Chỉ từ đẳng thức này, không được kết luận rằng mọi cách đo động lượng của hạt trong hộp đều chỉ cho hai giá trị $\pm p_n$.

Nếu bỏ vách và đo động lượng tự do của trạng thái ban đầu, phải biến đổi Fourier toàn bộ hàm sin bị giới hạn trong hộp. Phân bố động lượng khi ấy là liên tục. Mô hình hai kết quả dưới đây cần giả thiết riêng rằng dụng cụ phân biệt hai thành phần đối truyền.

:::

### Photon tán xạ và ý nghĩa của một kết quả đo

Hình 40.30 minh họa một photon tới theo chiều âm của trục $y$, nên photon tới không có thành phần động lượng theo $x$. Các đầu dò ở hai phía ghi nhận photon tán xạ. Sự tương quan giữa tín hiệu đầu dò và trạng thái hạt cho phép rút ra thông tin về hạt.

![Hình 40.30: Sơ đồ dùng photon tán xạ để minh họa phép đo động lượng. Hai đầu dò A và B biểu diễn hai nhánh kết quả trong mô hình lý tưởng. Khi dùng bảo toàn động lượng, phải phân biệt tổng động lượng của từng sự kiện với giá trị trung bình của trạng thái chuẩn bị.](../img/young-40/hinh-40-30.png)

Trong một tương tác cô lập, tổng động lượng trước và sau được bảo toàn. Theo phương $x$, đặt

$$
P_x=p_x+p_{\gamma,x}.
$$

Khi đó $P_x$ trước va chạm bằng $P_x$ sau va chạm. Nhưng giá trị trung bình ban đầu bằng không không có nghĩa tổng động lượng của mọi lần thử đều là một giá trị xác định bằng không. Vì vậy, không thể suy ra đầy đủ các kết quả đo chỉ bằng cách gán hai động lượng sau va chạm luôn đối nhau.

Sự tác động của ánh sáng đặc biệt đáng kể ở thang vi mô. Với electron trong hộp rộng $L=1{,}00\,\mathrm{\mu m}$, thang động lượng ở trạng thái cơ bản là

$$
\begin{aligned}
p_1&=\frac{\pi\hbar}{L}\\
&\approx3{,}31\times10^{-28}\,\mathrm{kg\,m/s}.
\end{aligned}
$$

Giá trị này chỉ khoảng một phần tư động lượng photon bước sóng $500\,\mathrm{nm}$. Dùng photon bước sóng dài hơn, chẳng hạn photon vô tuyến, sẽ giảm động lượng của từng photon. Tuy nhiên, giảm xung lượng tác động không tự động bảo đảm một phép đo có thông tin lại giữ nguyên trạng thái.

### Sự thay đổi trạng thái trong phép đo lý tưởng

Xét mô hình mà dụng cụ phân biệt hai thành phần đối truyền trong (40.53) và phép đo có tính lặp lại ngay sau khi đo. Hai hệ số có cùng độ lớn nên có hai nhánh đồng xác suất.

1. Nếu thu được nhánh $+p_n$, trạng thái sau phép đo chỉ còn thành phần truyền theo chiều dương, với thừa số không gian $e^{ik_nx}$. Đo lại ngay bằng cùng mô hình lý tưởng cho cùng kết quả.
2. Nếu thu được nhánh $-p_n$, trạng thái sau phép đo chỉ còn thành phần truyền theo chiều âm, với thừa số không gian $e^{-ik_nx}$.
3. Khi lặp lại trên nhiều hệ được chuẩn bị giống nhau, xác suất mỗi nhánh là $1/2$. Điều này không có nghĩa một mẫu hữu hạn bắt buộc chia đúng một nửa, cũng không cho phép dự đoán chắc chắn kết quả của một lần riêng lẻ.

Sự chuyển từ một chồng chập sang trạng thái ứng với kết quả đã thu được được gọi là **sự suy sụp hàm sóng**, trong cách mô tả phép đo bằng phép chiếu. Việc chọn một kết quả có điều kiện không phải là bước tiến triển tự do của riêng hệ theo phương trình Schrödinger.

Một thành phần sóng phẳng riêng lẻ không đáp ứng điều kiện biên của hộp vô hạn ban đầu. Vì vậy, muốn dùng mô hình này để dự đoán chuyển động sau phép đo, phải chỉ rõ tương tác đo, điều kiện giam giữ và Hamiltonian sau tương tác. Không thể vừa giữ nguyên hộp lý tưởng, vừa coi một sóng phẳng là trạng thái dừng mới của hộp.

::: warning Không đồng nhất kết quả đo với giá trị đã có sẵn

Trong mô hình phép chiếu, một kết quả $+p_n$ không chứng minh hạt đã mang sẵn đúng giá trị ấy trước phép đo. Cũng không thể kết luận dụng cụ bị thiên lệch chỉ vì một lần thử cho dấu dương thay vì dấu âm. Mô hình dự đoán xác suất trên nhiều lần chuẩn bị và đo tương ứng.

:::

### Có phải mọi phép đo đều đổi trạng thái?

Không. Giả sử hệ đã ở trạng thái riêng năng lượng $E_n$. Một phép đo năng lượng lý tưởng, không gây tương tác phụ làm chuyển mức, cho $E_n$ với xác suất $1$ và giữ nguyên trạng thái riêng ấy, ngoài một pha chung không ảnh hưởng xác suất.

Điều quan trọng là quan hệ giữa trạng thái được chuẩn bị và đại lượng được đo. Phép đo một đại lượng mà hệ chưa có giá trị xác định có thể làm thay đổi trạng thái. Phép đo lý tưởng trên một trạng thái riêng phù hợp có thể không làm thay đổi trạng thái đó.

### Cách diễn giải về sự suy sụp

Mô tả bằng phép chiếu xem kết quả đo là điều kiện để cập nhật trạng thái. Một hướng diễn giải khác, gọi là **diễn giải nhiều thế giới**, dùng hàm sóng chung cho hệ và dụng cụ, không đặt một bước suy sụp riêng.

Trong cách diễn giải ấy, các thành phần tương ứng với những kết quả khác nhau trở thành các nhánh. Chẳng hạn, một nhánh gắn với tín hiệu đầu dò A và nhánh kia gắn với tín hiệu đầu dò B. Chúng không còn giao thoa quan sát được trong mô tả phép đo thông thường.

Đây là những cách diễn giải về phép đo. Không được biến hình ảnh phân nhánh thành một kết luận thực nghiệm rằng ta đã quan sát trực tiếp những thế giới khác. Các xác suất dự đoán và cách kiểm tra chúng vẫn phải được phát biểu bằng những phép đo cụ thể.

### Câu hỏi tự kiểm tra 40.6

Hạt trong hộp được chuẩn bị trong chồng chập của hai trạng thái dừng đầu tiên. Ký hiệu các trạng thái ấy là

$$
\Psi_1(x,t)=\psi_1(x)e^{-iE_1t/\hbar}.
$$

$$
\Psi_2(x,t)=\psi_2(x)e^{-iE_2t/\hbar}.
$$

Trạng thái được chuẩn bị bằng chồng chập sau, với mọi hàm đều được lấy tại cùng $(x,t)$:

$$
\Psi=C\Psi_1+D\Psi_2.
$$

$C$ và $D$ đều khác không. Nếu đo năng lượng, kết quả nào sau đây được bảo đảm?

1. $E_1$.
2. $E_2$.
3. Trung bình cộng $(E_1+E_2)/2$.
4. Một giá trị nằm giữa $E_1$ và $E_2$, tùy thuộc $C$ và $D$.
5. Không có phương án nào trong bốn phương án trên.

<details><summary>Xem đáp án và giải thích</summary>

Chọn **5**. Mỗi lần đo năng lượng cho $E_1$ hoặc $E_2$, nhưng không thể bảo đảm trước sẽ thu được giá trị nào khi cả hai hệ số đều khác không.

Nếu trạng thái đã chuẩn hóa, $|C|^2+|D|^2=1$. Các xác suất là

$$
\begin{aligned}
P(E_1)&=|C|^2,\\
P(E_2)&=|D|^2.
\end{aligned}
$$

Nếu chưa chuẩn hóa, phải chia các bình phương độ lớn cho tổng của chúng. Hai kết quả đồng xác suất khi $|C|=|D|$. Kết quả $E_1$ có xác suất lớn hơn khi $|C|>|D|$, còn $E_2$ có xác suất lớn hơn trong trường hợp ngược lại.

Giá trị kỳ vọng có thể nằm giữa hai mức, nhưng không phải một mức năng lượng mới được phép xuất hiện trong một lần đo.

</details>
