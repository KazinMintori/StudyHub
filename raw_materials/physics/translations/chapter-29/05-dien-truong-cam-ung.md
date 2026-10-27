## 29.5 Điện trường cảm ứng

Khi dây dẫn chuyển động trong từ trường, lực từ lên các điện tích trong dây giải thích được suất điện động cảm ứng. Nhưng nếu dây đứng yên mà từ thông qua nó thay đổi, điều gì đẩy điện tích chạy quanh mạch?

Xét một ống dây dài, mảnh có tiết diện $A$ và mật độ vòng dây $n$, được một vòng dây dẫn tròn bao quanh ở giữa. Dòng điện $I$ trong ống dây tạo từ trường dọc trục, có độ lớn $B=\mu_0nI$. Ta bỏ qua từ trường nhỏ bên ngoài ống dây và chọn vectơ diện tích của vòng dây cùng chiều với từ trường. Từ thông qua vòng là $\Phi_B=BA=\mu_0nIA$. Khi dòng điện thay đổi, từ thông cũng thay đổi, nên định luật Faraday cho:

$$
\begin{aligned}
\mathcal{E} &= -\frac{d\Phi_B}{dt} \\
&= -\mu_0nA\frac{dI}{dt}.
\end{aligned} \tag{29.8}
$$

Nếu điện trở toàn vòng là $R$, dòng cảm ứng tức thời có độ lớn và dấu theo quy ước của suất điện động: $I'=\mathcal{E}/R$. Vòng dây nằm ngoài vùng có từ trường, vì vậy lực từ không thể làm điện tích chạy quanh vòng. Ta phải kết luận rằng từ thông biến thiên tạo ra một điện trường cảm ứng trong dây.

Khi điện tích $q$ đi một vòng quanh mạch, điện trường thực hiện công $q\mathcal{E}$. Do đó công trên một đơn vị điện tích, tức tích phân đường của điện trường quanh vòng kín, bằng suất điện động:

$$
\oint \vec E\cdot d\vec\ell=\mathcal{E}.
\tag{29.9}
$$

Tích phân quanh đường kín khác không, nên điện trường cảm ứng không bảo toàn. Không thể gắn cho nó một thế điện vô hướng như với điện trường tĩnh. Với đường tích phân đứng yên, Faraday viết thành:

$$
\oint \vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt}.
\tag{29.10}
$$

Dạng $\mathcal{E}=-d\Phi_B/dt$ dùng được cả khi mạch chuyển động. Dạng tích phân điện trường trong (29.10) được dùng cho đường tích phân đứng yên.

Với đường tròn bán kính $r$ đồng trục ống dây, điện trường cảm ứng có thành phần tiếp tuyến cùng độ lớn tại mọi điểm nhờ đối xứng trụ. Thành phần xuyên tâm, nếu xét thêm, không góp vào tích phân đường trên vòng tròn. Trong mô hình không có điện tích bên trong và trường không kỳ dị trên trục, cũng có thể dùng định luật Gauss với một mặt trụ kín đồng trục để loại thành phần xuyên tâm đối xứng. Ký hiệu độ lớn thành phần tiếp tuyến là $E$. Khi đó tuần hoàn điện trường có độ lớn $2\pi rE$, nên:

$$
E=\frac{1}{2\pi r}\left|\frac{d\Phi_B}{dt}\right|.
\tag{29.11}
$$

Một điện trường cảm ứng vẫn tác dụng lực $\vec F=q\vec E$ lên điện tích, nhưng khác điện trường tĩnh ở chỗ nó không bảo toàn và không có thế. Điện trường cảm ứng tồn tại ngay cả khi không có dây dẫn. Từ trường biến thiên là nguồn của điện trường loại này. Ở mục sau, ta sẽ thấy điện trường biến thiên cũng là nguồn của từ trường. Sự liên hệ giữa hai trường là nền tảng của sóng điện từ.

### Ví dụ 29.11: Điện trường cảm ứng quanh ống dây

Một ống dây dài có $500$ vòng trên mét và tiết diện $4{,}0\,\mathrm{cm^2}$. Dòng điện trong ống dây tăng với tốc độ $100\,\mathrm{A/s}$. (a) Tìm độ lớn suất điện động trong vòng dây bao quanh ống dây. (b) Tìm độ lớn điện trường cảm ứng nếu bán kính vòng là $2{,}0\,\mathrm{cm}$.

Vòng dây và ống dây đồng trục. Đối xứng khiến điện trường tiếp tuyến và có cùng độ lớn trên toàn chu vi, nên dùng (29.8) cho suất điện động rồi dùng (29.9) cho điện trường.

Đổi tiết diện và bán kính sang đơn vị SI:

$$
\begin{aligned}
A &= 4{,}0\,\mathrm{cm^2} \\
&= 4{,}0\times10^{-4}\,\mathrm{m^2}, \\
r &= 2{,}0\,\mathrm{cm} \\
&= 2{,}0\times10^{-2}\,\mathrm{m}.
\end{aligned}
$$

Với $\mu_0=4\pi\times10^{-7}\,\mathrm{Wb/(A\,m)}$, tích $n(dI/dt)=500\times100$ cho:

$$
\begin{aligned}
\frac{dB}{dt}&=\mu_0n\frac{dI}{dt}\\
&=(4\pi)(5)\times10^{-3}\,\mathrm{T/s}\\
&\approx6{,}283\times10^{-2}\,\mathrm{T/s}.
\end{aligned}
$$

Từ đó:

$$
\begin{aligned}
\mathcal{E} &= -\mu_0nA\frac{dI}{dt} \\
&=-A\frac{dB}{dt}\\
&=-(4{,}0)(6{,}283)\times10^{-6}\,\mathrm V\\
&= -2{,}513\times10^{-5}\,\mathrm V \\
&\approx -25\,\mu\mathrm V.
\end{aligned}
$$

Độ lớn suất điện động là $25\,\mu\mathrm V$. Vì $|\oint\vec E\cdot d\vec\ell|=2\pi rE=|\mathcal E|$, điện trường có độ lớn:

$$
\begin{aligned}
E &= \frac{|\mathcal E|}{2\pi r} \\
&= \frac{25\times10^{-6}}{2\pi(2{,}0\times10^{-2})}\,\mathrm{V/m} \\
&= 2{,}0\times10^{-4}\,\mathrm{V/m}.
\end{aligned}
$$

Trong hình, từ thông hướng vào mặt trang đang tăng. Theo quy ước chiều dương của hình, suất điện động âm nên dòng cảm ứng chạy ngược chiều kim đồng hồ. Có thể suy ra cùng chiều bằng định luật Lenz: Dòng cảm ứng tạo từ trường chống lại phần từ thông đang tăng.

![Hình 29.18: Ống dây có dòng điện tăng tạo từ thông biến thiên qua vòng dây đồng trục, gây điện trường cảm ứng và dòng điện đo bằng điện kế](../img/young-29/hinh-29-18.png)

Điện trường cảm ứng có nhiều ứng dụng. Khi xe điện giảm tốc, bánh xe vẫn quay động cơ theo chiều máy phát, tạo dòng nạp lại pin. Trục khuỷu của động cơ piston trên máy bay quay nam châm, làm xuất hiện suất điện động trong cuộn dây bên cạnh và tạo tia lửa đốt nhiên liệu. Cơ chế này giúp động cơ tiếp tục chạy khi các hệ thống điện khác của máy bay hỏng.

Bộ thu tín hiệu của guitar điện cảm ứng dòng trong cuộn dây đứng yên khi dây đàn sắt từ rung. Máy phát điện xoay chiều trên ô tô cũng dùng nam châm quay để tạo dòng trong các cuộn dây đứng yên.

![Hình 29.19: Xe điện nạp pin khi giảm tốc và cuộn đánh lửa trong máy bay động cơ piston](../img/young-29/hinh-29-19.png)

### Tự kiểm 29.5

Nếu lắc một nam châm qua lại bằng tay, ta có tạo ra điện trường không? Nếu có, điện trường ấy có bảo toàn không?

::: details Lời giải
Có. Tại mỗi vị trí cố định, từ trường thay đổi khi nam châm chuyển động. Từ thông biến thiên tạo điện trường cảm ứng, và điện trường đó không bảo toàn.
:::
