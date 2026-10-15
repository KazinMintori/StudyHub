## Bài tập nâng cao 38.38–38.40

::: exercise 38.38

Dùng mạch ở Hình P38.38 để khảo sát công thoát. Ampe kế đo dòng quang điện $i$, còn $V_{AC}$ là điện thế anode so với cathode.

![Hình P38.38: Mạch khảo sát quang điện có hai nguồn 15,0 V mắc ngược cực tính, điện trở 1,00 kΩ và biến trở R. Cần đọc cực tính nguồn cùng nhãn vị trí công tắc.](img/young-38/hinh-p38-38.png)

(a) Công tắc ở vị trí a, bước sóng chiếu $140\,\mathrm{nm}$ và $R=3{,}20\,\mathrm{k\Omega}$, không có dòng quang điện. Tìm $V_{AC}$. (b) Giảm dần $R$, dòng bắt đầu xuất hiện tại $R=334\,\Omega$. Tìm $V_{AC}$. (c) Tìm công thoát cathode.

(d) Chuyển công tắc sang b, ampe kế chỉ $i=3{,}71\,\mathrm{mA}$. Dòng $I$ qua $R$ theo mũi tên hình bằng bao nhiêu? (e) Tìm $V_{AC}$ lúc ấy. (f) Trở lại a, giảm bước sóng xuống $65{,}0\,\mathrm{nm}$. Tìm $R$ nhỏ nhất để dòng quang điện vừa ngừng.

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Hai nhánh nguồn có cực tính ngược nhau. Cần kiểm tra rằng vị trí được dùng để hãm electron thật sự đặt anode ở điện thế thấp hơn cathode. Điện trở cố định $R_0=1000\,\Omega$.

**Hướng đi:**

- Khi dòng quang điện bằng không, dùng mạch chia điện áp giữa $R_0$ và $R$.
- Tại ngưỡng dòng, độ lớn điện thế hãm bằng động năng cực đại chia $e$.
- Khi có dòng quang điện, phải dùng định luật nút, không tiếp tục dùng công thức chia áp của mạch không tải.
- Đối chiếu dấu điện áp với cực tính trong hình trước khi dùng dữ kiện phát electron.

Với đúng nhãn và cực tính đang vẽ, vị trí a nối nguồn làm anode dương hơn cathode. Khi không có dòng quang điện,

$$
V_{AC}=\frac{15{,}0R}{R+R_0}>0.
$$

Ở $R=3{,}20\,\mathrm{k\Omega}$, điện áp là $+11{,}43\,\mathrm V$. Giảm $R$ vẫn giữ điện áp dương. Vì vậy, chuỗi “không có dòng rồi dòng vừa xuất hiện do giảm thế hãm” không phù hợp với vị trí a được ghi trên chính hình này trong mô hình quang điện chuẩn.

Muốn thực hiện phép đo hãm được mô tả ở (a)–(c), phải dùng nhánh làm anode âm, tức vị trí b theo cực tính hình. Các kết quả có điều kiện dưới đây giữ nguyên số liệu và thực hiện đúng chức năng điện của hai nhánh, tương đương hoán đổi tên a và b trong phần mô tả thao tác.

(a) Với nhánh hãm, điện áp là $V_{AC}\approx-11{,}43\,\mathrm V$.

(b) Tại $R=334\,\Omega$,

$$
\begin{aligned}
V_{AC}&=-\frac{15{,}0(334)}{334+1000}\\
&\approx-3{,}756\,\mathrm V.
\end{aligned}
$$

(c) Photon $140\,\mathrm{nm}$ có năng lượng khoảng $8{,}857\,\mathrm{eV}$. Động năng cực đại là $e|V_{AC}|$, nên công thoát suy ra xấp xỉ $5{,}10\,\mathrm{eV}$.

(d), (e) Đổi sang nhánh tăng tốc, vẫn giữ $R=334\,\Omega$. Chọn anode làm mốc điện thế không, và gọi điện thế cathode là $U$. Đầu bên kia của $R_0$ có điện thế $-15{,}0\,\mathrm V$. Dòng quang điện theo mũi tên đi vào cathode, nên định luật nút là

$$
\frac{U+15{,}0}{R_0}+\frac UR=i.
$$

Suy ra

$$
U=\frac{i-15{,}0/R_0}{1/R_0+1/R}.
$$

Với $i=3{,}71\,\mathrm{mA}$, ta có $U\approx-2{,}827\,\mathrm V$. Do đó,

$$
\begin{aligned}
I&=U/R\approx-8{,}46\,\mathrm{mA},\\
V_{AC}&=-U\approx+2{,}83\,\mathrm V.
\end{aligned}
$$

Dòng qua biến trở thực sự đi ngược mũi tên $I$ đã chọn trong hình.

(f) Với photon $65{,}0\,\mathrm{nm}$ và cùng công thoát, độ lớn thế hãm cần khoảng $V_s=13{,}98\,\mathrm V$. Trong nhánh hãm,

$$
V_s=\frac{15{,}0R}{R+R_0}.
$$

Giải theo $R$:

$$
R=\frac{R_0V_s}{15{,}0-V_s}\approx13{,}6\,\mathrm{k\Omega}.
$$

Ở điện trở lớn hơn, thế ngược có độ lớn lớn hơn nên vẫn chặn dòng. Những giá trị (a)–(f) này chỉ áp dụng với chức năng hai nhánh được nêu rõ. Không thể đồng thời giữ nguyên tên thao tác ban đầu, đúng cực tính đang vẽ và mọi dữ kiện dòng điện mà bỏ qua sự không nhất quán ấy.

:::

::: exercise 38.39

Photon bước sóng $\lambda$ tới một hạt đứng yên có khối lượng $M$. Photon bị hấp thụ, đồng thời tạo electron–positron. Hạt bia chuyển động theo hướng photon tới với tốc độ $V_M$. Electron và positron có cùng tốc độ $v$, đi đối xứng ở góc $\phi$ với hướng ban đầu.

![Hình P38.39: Hạt bia nhận giật lùi khi một photon tạo cặp electron–positron. Hai hạt mới có động lượng ngang đối nhau.](img/young-38/hinh-p38-39.png)

Đặt $\gamma=1/\sqrt{1-v^2/c^2}$ và $\gamma_M=1/\sqrt{1-V_M^2/c^2}$.

(a) Viết bảo toàn năng lượng với khối lượng nghỉ electron $m$. (b) Viết bảo toàn động lượng. (c) Khử $h/\lambda$ để liên hệ $v/c,V_M/c,\phi$ và $m/M$. (d) Dùng khai triển ở $V_M/c$ nhỏ để suy tốc độ giật lùi gần đúng. (e) Có lựa chọn hữu hạn nào của $v,\phi$ cho $V_M=0$ không?

(f) Nếu bia là proton và hai hạt mới đứng yên, proton đi nhanh bao nhiêu theo $\mathrm{km/s}$? (g) Nếu mỗi hạt mới có năng lượng toàn phần $5{,}00\,\mathrm{MeV}$ và $\phi=60^\circ$, proton đi nhanh bao nhiêu? (h) Năng lượng photon tới trong trường hợp (g) bằng bao nhiêu?

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Hạt bia giữ nguyên khối lượng nghỉ $M$. Hai hạt mới có khối lượng nghỉ $m$ và động lượng ngang triệt tiêu. Đặt $r=m/M$, $\beta=v/c$, $B=V_M/c$ và $G=\gamma_M$.

**Hướng đi:**

- Giữ cả năng lượng nghỉ ban đầu của bia trong phương trình năng lượng.
- Chiếu động lượng theo hướng photon tới, vì các thành phần vuông góc của cặp triệt tiêu.
- Chuẩn hóa hai phương trình bằng $Mc^2$ để khử năng lượng photon, rồi dùng định nghĩa $G$.
- Ở tốc độ bia nhỏ, khai triển theo $B$ và giữ rõ bậc gần đúng.

(a) Gọi năng lượng photon là $E_\gamma=hc/\lambda$, năng lượng toàn phần của hạt bia sau tương tác là $E_M=GMc^2$ và của cặp mới là $E_{\rm pair}=2\gamma mc^2$. Bảo toàn năng lượng là

$$
E_\gamma+Mc^2=E_M+E_{\rm pair}.
$$

(b) Bảo toàn động lượng dọc:

$$
\frac h\lambda=GMV_M+2\gamma mv\cos\phi.
$$

(c) Chia phương trình năng lượng cho $Mc^2$ và phương trình động lượng cho $Mc$, rồi khử photon. Đặt $F=2r\gamma$ và $C=\beta\cos\phi$, ta thu được

$$
(G-1)+F=GB+FC.
$$

Để viết gọn mà vẫn giữ mọi phụ thuộc, đặt

$$
D=2r\gamma(1-\beta\cos\phi).
$$

Quan hệ cần tìm là

$$
G(1-B)=1-D.
$$

Vì $G(1-B)=\sqrt{(1-B)/(1+B)}$, đặt $A=1-D$ cho nghiệm chính xác

$$
B=\frac{1-A^2}{1+A^2}.
$$

Trong cấu hình bia chuyển động về phía trước, cần $0<A\le1$ để nghiệm thuộc miền vật lý đã chọn.

(d) Khi $B$ nhỏ, khai triển nhị thức cho

$$
G\approx1+\frac12B^2.
$$

Giữ đến hiệu chỉnh bậc hai trong quan hệ đã khử photon cho

$$
B-\frac12B^2\approx D.
$$

Nghiệm nhỏ là $B\approx1-\sqrt{1-2D}$. Nếu chỉ giữ bậc nhất, ta có $B\approx D$, hay

$$
V_M\approx2r\gamma c(1-\beta\cos\phi).
$$

(e) Không có nghiệm $V_M=0$ với hai hạt mới có năng lượng hữu hạn trong cấu hình này. Vì $\beta<1$ và $\cos\phi\le1$, ta có $D>0$. Bia phải nhận giật lùi để bảo toàn cả năng lượng lẫn động lượng của một photon tới.

(f) Với $v=0$, $\gamma=1$ và $D=2m/M$. Dùng khối lượng proton $M=1{,}673\times10^{-27}\,\mathrm{kg}$ cho tốc độ khoảng $327\,\mathrm{km/s}$. Nghiệm chính xác và gần đúng nhỏ đều phù hợp ở độ chính xác này.

(g) Mỗi hạt mới có năng lượng $5{,}00\,\mathrm{MeV}$ nên $\gamma\approx9{,}78$ và $\beta\approx0{,}9948$. Thay $\phi=60^\circ$ vào $D$ rồi tính nghiệm nhỏ, ta được $V_M\approx1{,}61\times10^3\,\mathrm{km/s}$.

(h) Gọi động năng giật lùi của bia là $K_M=(G-1)Mc^2$. Photon tới phải cung cấp tổng năng lượng toàn phần $10{,}00\,\mathrm{MeV}$ của cặp và động năng giật lùi của proton. Bảo toàn năng lượng cho

$$
E_\gamma=E_{\rm pair}+K_M.
$$

Giá trị trước làm tròn xấp xỉ $10{,}0135\,\mathrm{MeV}$. Năng lượng photon hơi lớn hơn tổng năng lượng của riêng cặp vì bia cũng chuyển động sau tương tác.

:::

::: exercise 38.40

Photon bước sóng $\lambda$ bay theo $+x$, va chạm trực diện với electron bay theo $-x$. Electron có năng lượng toàn phần $E$, gồm năng lượng nghỉ $mc^2$. Sau va chạm, photon bị tán xạ ngược theo $-x$, và electron cũng chuyển động theo $-x$.

(a) Suy biểu thức bước sóng photon cuối $\lambda'$. Chứng minh giới hạn $E\gg mc^2$ cho dạng gần đúng có số hạng $hc/E$ và hiệu chỉnh phụ thuộc bước sóng tới. (b) Với laser CO₂ có $\lambda=10{,}6\,\mu\mathrm m$ và electron có năng lượng toàn phần $10{,}0\,\mathrm{GeV}$, tính $\lambda'$ ở góc tán xạ $180^\circ$. (c) Photon cuối thuộc vùng phổ nào và hiệu ứng có thể dùng làm gì?

:::

::: solution Lời giải chi tiết

**Tóm tắt đề bài:** Đặt năng lượng nghỉ $E_0=mc^2$, năng lượng photon tới $\varepsilon=hc/\lambda$ và photon cuối $\varepsilon'=hc/\lambda'$. Gọi $q=\sqrt{E^2-E_0^2}$ là độ lớn động lượng electron ban đầu nhân $c$.

**Hướng đi:**

- Viết bảo toàn năng lượng và động lượng một chiều với dấu của photon cuối là âm.
- Dùng hệ thức năng lượng–động lượng cho electron sau tương tác để khử trạng thái cuối của nó.
- Chỉ sau khi có biểu thức chính xác mới dùng $q\approx E$ trong miền siêu tương đối tính.

(a) Năng lượng electron cuối là $E_f=E+\varepsilon-\varepsilon'$. Thành phần động lượng electron cuối nhân $c$ là

$$
p_fc=\varepsilon-q+\varepsilon'.
$$

Hệ thức electron $E_f^2-(p_fc)^2=E_0^2$, cùng $E^2-q^2=E_0^2$, rút gọn thành

$$
\varepsilon(E+q)=\varepsilon'(E-q+2\varepsilon).
$$

Do đó,

$$
\varepsilon'=\frac{\varepsilon(E+q)}{E-q+2\varepsilon}.
$$

Đặt $S=E+q$. Vì $(E-q)S=E_0^2$, bước sóng cuối có thể viết bằng hai số hạng

$$
L_1=\frac{2hc}{S},
$$

$$
L_2=\frac{E_0^2\lambda}{S^2},
$$

$$
\lambda'=L_1+L_2.
$$

Khi $E\gg E_0$, ta có $S\approx2E$. Đặt $a=E_0^2\lambda/(4hcE)$, biểu thức gần đúng là

$$
\lambda'\approx\frac{hc}{E}(1+a).
$$

Thay định nghĩa $a$ và $E_0=mc^2$ vào, đây chính là tổng $hc/E$ và hiệu chỉnh $m^2c^4\lambda/(4E^2)$. Mỗi số hạng đều có đơn vị chiều dài.

(b) Đổi $10{,}0\,\mathrm{GeV}$ thành năng lượng toàn phần trong đơn vị SI, rồi thay vào biểu thức chính xác cho

$$
\lambda'\approx7{,}05\times10^{-15}\,\mathrm m.
$$

Điều kiện electron cuối vẫn theo $-x$ được thỏa mãn vì $p_fc<0$ với các dữ kiện này.

(c) Năng lượng photon cuối xấp xỉ $176\,\mathrm{MeV}$, thuộc vùng gamma. Electron nhanh đã truyền năng lượng cho photon, nên đây là Compton ngược. Cơ chế có thể dùng tạo chùm photon năng lượng cao từ nguồn laser và chùm electron, với năng lượng và hình học tương tác được điều khiển.

:::
