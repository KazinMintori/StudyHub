<!-- Source: Section22.3, printed725–729, PDF745–749. -->

## 22.3. Định luật Gauss

Định luật Gauss diễn đạt quan hệ giữa điện tích và điện trường theo một cách khác với định luật Coulomb. Trong tĩnh điện, hai cách diễn đạt tương đương nhau. Carl Friedrich Gauss (1777–1855) đã xây dựng định luật này.

![Hình 22.10: Carl Friedrich Gauss](../img/young-22/hinh-22-10.png)

**Hình 22.10:** Gauss có đóng góp vào hình học vi phân, giải tích thực, lý thuyết số và phân bố dạng chuông trong thống kê. Ông còn nghiên cứu từ trường Trái Đất và tính quỹ đạo của tiểu hành tinh đầu tiên được phát hiện.

### Nguồn điểm ở tâm mặt cầu

Đặt điện tích điểm dương q tại tâm một mặt cầu tưởng tượng bán kính R. Trường hướng xuyên tâm ra ngoài và có cùng độ lớn tại mọi điểm trên mặt:

$$
E=\frac{q}{4\pi\varepsilon_0R^2}.
$$

Mọi vector diện tích đều hướng ra ngoài và cùng chiều trường. Vì thế:

$$
\begin{aligned}
&\Phi_E = EA\\
&\quad =\frac{q}{4\pi\varepsilon_0R^2}\\
&\quad\times(4\pi R^2)\\
&\quad =\frac q{\varepsilon_0}.
\end{aligned}
\tag{22.6}
$$

Điện thông không phụ thuộc bán kính cầu, mà chỉ phụ thuộc điện tích được bao. Mỗi đường sức xuyên qua mặt cầu nhỏ cũng xuyên qua mặt cầu lớn đồng tâm.

![Hình 22.11: Chiếu một phần mặt cầu bán kính R lên mặt cầu bán kính 2R](../img/young-22/hinh-22-11.png)

**Hình 22.11:** Phần diện tích dA trên cầu nhỏ được chiếu theo các tia từ nguồn thành 4dA trên cầu lớn. Trường ở cầu lớn còn một phần tư. Do đó điện thông qua hai phần tương ứng bằng nhau. Lập luận đúng với từng phần mặt, không chỉ với cả mặt cầu.

### Nguồn điểm bên trong mặt kín không phải mặt cầu

Bao mặt cầu bằng một mặt kín có hình dạng không đều. Xét một phần nhỏ dA của mặt không đều và chiếu nó lên mặt cầu có cùng khoảng cách đến nguồn.

![Hình 22.12: Diện tích hình chiếu và thành phần trường vuông góc mặt không đều](../img/young-22/hinh-22-12.png)

**Hình 22.12:** Pháp tuyến của dA hợp góc φ với phương xuyên tâm. Khi chiếu lên mặt vuông góc tia, một cặp cạnh bị thu ngắn theo cosφ, còn cặp kia không đổi. Diện tích hình chiếu là dA cosφ.

Trường xuyên tâm có độ lớn E tại vị trí đang xét. Điện thông qua phần mặt không đều bằng E dA cosφ, đúng bằng điện thông qua phần hình chiếu. Chia toàn mặt thành những phần nhỏ, chiếu từng phần và cộng bằng tích phân, ta nhận được cùng điện thông như qua mặt cầu:

$$
\begin{aligned}
&\Phi_E = \oint\vec E\cdot d\vec A\\
&\quad =\frac{q}{\varepsilon_0}.
\end{aligned}
\tag{22.7}
$$

Vòng tròn trên dấu tích phân nhắc rằng phép tích phân đi trên **toàn một mặt kín**. Các vector diện tích luôn hướng ra ngoài. Nơi trường hướng ra, tích vô hướng dương. Nơi trường hướng vào, tích vô hướng âm.

Nếu q âm, trường hướng vào nguồn, nên điện thông âm. Vế phải cũng âm và (22.7) vẫn đúng. Điện thông không phụ thuộc hình dạng hoặc kích thước của mặt kín bao nguồn.

### Điện tích bên ngoài mặt kín

![Hình 22.13: Đường sức từ nguồn ngoài đi vào rồi đi ra một mặt kín](../img/young-22/hinh-22-13.png)

Nếu không có điện tích bên trong, đường sức do nguồn bên ngoài đi vào mặt phải đi ra ở một nơi khác. Phần đóng góp điện thông âm và dương bù nhau:

$$
\oint\vec E\cdot d\vec A=0.
$$

Đường sức chỉ có thể bắt đầu hoặc kết thúc trong vùng khi vùng ấy có điện tích. Kết quả này mở rộng nhận xét về hộp trong trường đều sang mặt kín bất kỳ.

### Phát biểu tổng quát

Xét trước hai điện tích được bao. Trường tổng là $\vec E_1+\vec E_2$, và tính tuyến tính của tích phân cho điện thông bằng $\frac{q_1+q_2}{\varepsilon_0}$. Với n điện tích, tổng đại số được bao là:

$$
\begin{aligned}
&Q_{\mathrm{trong}} = q_1+q_2+\cdots+q_n\\
&\quad =\sum_{i=1}^{n}q_i.
\end{aligned}
$$

Chỉ số i chạy qua từng điện tích nằm bên trong mặt, từ 1 đến n. Điện tích dương và âm được cộng với dấu của chúng. Nguyên lý chồng chất cho phép cộng các hệ thức điện thông của từng nguồn, dẫn đến:

> **Định luật Gauss:** Điện thông tổng qua một mặt kín bằng tổng đại số điện tích nằm bên trong mặt đó chia cho hằng số điện $\varepsilon_0$.

$$
\begin{aligned}
&\Phi_E = \oint\vec E\cdot d\vec A\\
&\quad =\frac{Q_{\mathrm{trong}}}{\varepsilon_0}.
\end{aligned}
\tag{22.8}
$$

Các cách viết tương đương là:

$$
\begin{aligned}
&\Phi_E = \oint E\cos\varphi\,dA\\
&\quad =\oint E_\perp\,dA\\
&\quad =\oint\vec E\cdot d\vec A\\
&\quad =\frac{Q_{\mathrm{trong}}}{\varepsilon_0}.
\end{aligned}
\tag{22.9}
$$

Mặt kín được dùng trong định luật gọi là **mặt Gauss**. Đây là mặt tưởng tượng, không cần trùng với bất kỳ vật thể hay bề mặt vật liệu nào.

### Dấu của trường và điện thông

![Hình 22.14: Mặt Gauss cầu bao điện tích dương và điện tích âm](../img/young-22/hinh-22-14.png)

Với nguồn $+q$, thành phần trường theo pháp tuyến ra ngoài là $E_\perp=+\frac{kq}{r^2}$. Tích phân trên mặt cầu cho $+\frac{q}{\varepsilon_0}$. Với nguồn $-q$, trong đó q là độ lớn dương, thành phần ấy là $E_\perp=-\frac{kq}{r^2}$, nên tích phân cho $-\frac{q}{\varepsilon_0}$. Không được thay thành phần có dấu bằng độ lớn E ở cả hai trường hợp.

Trong (22.8) và (22.9), $\vec E$ là **trường tổng tại điểm trên mặt**, do cả điện tích trong lẫn điện tích ngoài tạo ra. Chỉ vế phải sử dụng riêng điện tích được bao. Nguồn ngoài có thể làm trường trên mặt thay đổi mạnh, nhưng điện thông tổng của riêng phần trường ấy luôn bằng không.

Vì vậy, khi $Q_{\mathrm{trong}}=0$, điện thông tổng phải bằng không, còn trường có thể khác không. Một số phần mặt có điện thông dương và những phần khác có điện thông âm.

Định luật đã trả lời câu hỏi đi từ trường trên mặt đến điện tích bên trong. Theo chiều ngược lại, nếu biết phân bố điện tích, ta có thể tìm trường hay không? Điều đó còn phụ thuộc việc có tính được tích phân hay không. Các cấu hình đối xứng sẽ làm bước này đặc biệt đơn giản.

### Ví dụ 22.4: Điện thông và điện tích được bao

Hình 22.15 biểu diễn trường của lưỡng cực gồm $+q$ và $-q$. Tìm điện thông qua các mặt kín A, B, C và D.

![Hình 22.15: Bốn mặt kín bao những phần khác nhau của một lưỡng cực](../img/young-22/hinh-22-15.png)

::: solution Chi tiết
Mặt A bao điện tích dương, B bao điện tích âm, C bao cả hai, còn D không bao nguồn nào. Áp dụng định luật Gauss trực tiếp:

$$
\begin{aligned}
&\Phi_{EA} = +\frac{q}{\varepsilon_0},\\
&\Phi_{EB} = -\frac{q}{\varepsilon_0},\\
&\Phi_{EC} = \frac{q-q}{\varepsilon_0}=0,\\
&\Phi_{ED} = 0.
\end{aligned}
$$

Không cần thực hiện tích phân. Kết quả chỉ phụ thuộc điện tích được bao, không phụ thuộc hình dạng chi tiết của mặt. Với A, các đường sức đi ra cho điện thông dương. Với B, các đường đi vào cho điện thông âm. Với C và D, phần đi vào và đi ra cân bằng nhau. Các bài biến thể nằm trong phần luyện tập cuối chương.
:::

::: exercise Câu hỏi ôn lại mục 22.3
Sáu điện tích cùng nằm trong một mặt phẳng. Hình 22.16 cho giao tuyến của năm mặt Gauss với mặt phẳng ấy. Hãy xếp các mặt theo điện thông từ dương nhất đến âm nhất.

![Hình 22.16: Năm mặt Gauss và sáu điện tích điểm](../img/young-22/hinh-22-16.png)
:::

::: solution Giải thích
Các điện tích được bao, tính bằng µC, là:

$$
\begin{aligned}
&Q_1 = 0,\\
&Q_2 = 9+5-7=7,\\
&Q_3 = 9+1-10=0,\\
&Q_4 = 8-7=1,\\
&Q_5 = 8-7-10+1+9+5=6.
\end{aligned}
$$

Điện thông có cùng thứ tự với điện tích được bao, nên **S₂, S₅, S₄, rồi S₁ và S₃ bằng nhau**.
:::
