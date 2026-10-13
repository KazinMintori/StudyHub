<!-- Source: Section27.3, printed884–887/PDF904–907. Figures27.11–27.16, Example27.2, equations27.5–27.9. -->

## 27.3. Đường sức từ và từ thông

Làm thế nào mô tả một từ trường có hướng và độ lớn thay đổi từ điểm này sang điểm khác? Ta dùng **đường sức từ**, tương tự cách dùng đường sức điện. Tại mỗi điểm, tiếp tuyến của đường sức có hướng của vector từ trường $\vec B$.

![Hình 27.11: Đường sức từ của một nam châm vĩnh cửu](../img/young-27/hinh-27-11.png)

Các đường đi qua cả bên ngoài lẫn bên trong nam châm. Kim la bàn định hướng theo tiếp tuyến của đường sức tại vị trí đặt kim.

Ta chỉ vẽ một số đường đại diện. Nếu vẽ tất cả, chúng sẽ phủ kín không gian. Trong cùng một cách biểu diễn, nơi các đường kề nhau dày hơn có từ trường mạnh hơn. Nơi chúng thưa hơn có từ trường yếu hơn. Các đường sức không cắt nhau vì hướng của $\vec B$ tại một điểm được xác định duy nhất.

::: warning Đường sức từ không chỉ hướng lực từ lên điện tích
Lực từ lên hạt chuyển động vuông góc với từ trường. Hướng lực còn phụ thuộc vận tốc và dấu điện tích. Vì vậy, chỉ nhìn đường sức chưa đủ để xác định lực lên một hạt bất kỳ. Kim la bàn cho biết hướng từ trường, không phải hướng lực tịnh tiến lên hạt mang điện.
:::

![Hình 27.12: Phân biệt hướng từ trường và hướng lực từ](../img/young-27/hinh-27-12.png)

Lực được xác định bởi $\vec F=q\vec v\times\vec B$. Nó không nằm dọc đường sức đi qua vị trí hạt.

### Nhận biết từ trường qua bản đồ đường sức

![Hình 27.13: Từ trường của nam châm chữ C, dây thẳng, vòng dây và ống dây mang dòng](../img/young-27/hinh-27-13.png)

Trong khe giữa hai mặt cực phẳng, song song, các đường gần thẳng, song song và cách đều. Điều này biểu thị từ trường gần đều trong miền ấy, tức độ lớn và hướng gần như không đổi. Từ trường của vòng dây và đặc biệt của ống dây có hình dạng giống từ trường của một nam châm thẳng.

Vì từ trường có cấu trúc ba chiều, hình vẽ cần biểu diễn cả hướng vào và ra khỏi mặt giấy. Dấu chấm biểu thị vector hướng ra phía người nhìn. Dấu chéo biểu thị vector hướng vào trong. Có thể hình dung chấm là đầu mũi tên đang bay tới, còn chéo là đuôi mũi tên đang bay đi.

![Hình 27.14: Mạt sắt định hướng theo đường sức và bản vẽ đường sức tương ứng](../img/young-27/hinh-27-14.png)

Mạt sắt nhỏ có xu hướng xếp theo hướng của từ trường, giống những kim la bàn nhỏ. Nhờ đó, mạt sắt giúp quan sát dạng đường sức.

### Từ thông qua một mặt

Để đo mức xuyên qua của từ trường đối với một mặt, chia mặt ấy thành những phần tử diện tích nhỏ $dA$. Mỗi phần tử có vector diện tích $d\vec A$ vuông góc với mặt tại vị trí đó. Gọi $\phi$ là góc giữa $\vec B$ và pháp tuyến đã chọn, còn $B_\perp=B\cos\phi$ là thành phần có dấu theo pháp tuyến.

![Hình 27.15: Từ trường và vector diện tích tại một phần tử mặt](../img/young-27/hinh-27-15.png)

Góc dùng trong công thức là góc với pháp tuyến, không phải góc với mặt. Thành phần song song với mặt không đóng góp từ thông.

**Từ thông** vi phân qua phần tử là:

$$
\begin{aligned}
&d\Phi_B = B_\perp\,dA\\
&\quad =B\cos\phi\,dA\\
&\quad =\vec B\cdot d\vec A.
\end{aligned}
\tag{27.5}
$$

Khi thành phần vuông góc biến thiên trên mặt, cộng đóng góp của tất cả phần tử bằng tích phân mặt:

$$
\begin{aligned}
&\Phi_B = \int B_\perp\,dA\\
&\quad =\int B\cos\phi\,dA\\
&\quad =\int\vec B\cdot d\vec A.
\end{aligned}
\tag{27.6}
$$

Từ thông là đại lượng vô hướng. Với mặt phẳng diện tích $A$ trong từ trường đều, $B_\perp$ và $\phi$ không đổi trên mặt, nên:

$$
\begin{aligned}
&\Phi_B = B_\perp A\\
&\quad =BA\cos\phi.
\end{aligned}
\tag{27.7}
$$

Nếu từ trường vuông góc mặt và cùng chiều vector diện tích, $\phi=0$ và $\Phi_B=BA$. Khái niệm này sẽ được dùng khi xét cảm ứng điện từ ở Chương 29.

Đơn vị SI của từ thông là **weber**, ký hiệu Wb, đặt theo tên nhà vật lý Wilhelm Weber (1804–1891). Từ đơn vị của từ trường và diện tích:

$$
\begin{aligned}
&1\,\mathrm{Wb} = 1\,\mathrm{T\cdot m^2},\\
&1\,\mathrm T = 1\,\mathrm{N/(A\cdot m)},\\
&1\,\mathrm{Wb} = 1\,\mathrm{N\cdot m/A}.
\end{aligned}
$$

### Định luật Gauss đối với từ trường

Đối với điện trường, thông lượng qua mặt kín tỉ lệ với điện tích tổng bên trong. Chẳng hạn, một mặt kín bao cả lưỡng cực điện có điện thông tổng bằng không vì điện tích tổng bằng không. Nếu tồn tại một đơn cực từ, ta có thể hình dung một quan hệ tương tự với tổng từ tích.

Trong mô tả từ học đang xét, không có đơn cực từ đóng vai trò nguồn hay điểm tận cùng của đường sức. **Định luật Gauss đối với từ trường** phát biểu rằng từ thông tổng qua mọi mặt kín bằng không:

$$
\oint\vec B\cdot d\vec A=0.
\tag{27.8}
$$

Ở đây $d\vec A$ luôn hướng ra ngoài mặt kín. Mỗi phần đường sức đi vào một mặt kín cũng phải đi ra. Các đóng góp vào và ra có dấu trái nhau, nên tổng từ thông triệt tiêu. Có thể kiểm tra điều này bằng cách vẽ một mặt kín bất kỳ trên các bản đồ ở Hình 27.11 và 27.13.

::: warning Đường sức từ không có điểm đầu hoặc điểm cuối
Không được kết thúc đường sức ở mặt cực nam châm. Bên ngoài nam châm, đường sức đi từ cực bắc đến cực nam, nhưng nó còn tiếp tục trong nam châm. Các đường trong những bản đồ nam châm và vòng dây trên tạo thành vòng kín. Định luật Gauss loại trừ nguồn hay điểm hút đường sức, không đòi hỏi một đường kéo dài đến vô cực phải khép lại trong miền hữu hạn đang vẽ.
:::

Một mặt hở có hai cách chọn pháp tuyến. Ta phải chọn một phía là phía dương và dùng nhất quán trong toàn bộ phép tính. Đổi phía dương sẽ đổi dấu từ thông, dù từ trường vật lý không đổi.

Nếu phần tử diện tích $dA_\perp$ vuông góc đường sức, thành phần vuông góc có độ lớn bằng $B$, nên:

$$
B=\frac{d\Phi_B}{dA_\perp}.
\tag{27.9}
$$

Vì vậy, độ lớn từ trường có thể được hiểu là từ thông trên một đơn vị diện tích vuông góc với trường. Trong cách diễn đạt này, $\vec B$ còn được gọi là mật độ từ thông.

### Ví dụ 27.2: Xác định từ trường từ từ thông

Một mặt phẳng có diện tích $3{,}0\,\mathrm{cm^2}$ nằm trong từ trường đều. Từ thông qua mặt là $+0{,}90\,\mathrm{mWb}$. Trong Hình 27.16a, từ trường tạo góc $30^\circ$ với mặt. Hãy tìm độ lớn từ trường và hướng vector diện tích.

![Hình 27.16: Mặt phẳng đặt nghiêng trong từ trường đều và hai cách chọn pháp tuyến](../img/young-27/hinh-27-16.png)

Vector diện tích vuông góc mặt. Hướng được chọn ở hình (b) tạo góc $60^\circ$ với từ trường. Hướng ngược lại tạo góc $120^\circ$.

#### Nhận diện và bố trí

Vì từ trường đều và mặt phẳng, dùng $\Phi_B=BA\cos\phi$. Từ thông đã được cho có dấu dương, còn $B$ và $A$ là độ lớn dương. Do đó $\cos\phi$ phải dương.

#### Thực hiện

Hai pháp tuyến có thể cho $\phi=60^\circ$ hoặc $120^\circ$. Trường hợp thứ hai có cosine âm, nên không phù hợp dấu từ thông đã cho. Ta chọn pháp tuyến tạo góc $60^\circ$ rồi tính:

$$
\begin{aligned}
&A = 3{,}0\times10^{-4}\,\mathrm{m^2},\\
&B = \frac{\Phi_B}{A\cos\phi}\\
&\quad =\frac{0{,}90\times10^{-3}}{(3{,}0\times10^{-4})\cos60^\circ}\\
&\quad =6{,}0\,\mathrm T.
\end{aligned}
$$

#### Đánh giá và ý chính

Đây là phép suy từ từ thông về độ lớn trường và hướng pháp tuyến. Nếu chọn pháp tuyến ngược lại, cùng mặt và cùng trường sẽ cho từ thông âm. Với trường đều, từ thông bằng diện tích nhân thành phần trường vuông góc có dấu. Qua mặt kín, từ thông tổng luôn bằng không.

::: exercise Kiểm tra hiểu biết 27.3
Hãy tưởng tượng chuyển động dọc trục của vòng dây mang dòng ở Hình 27.13c, từ một điểm xa bên trái đến một điểm xa bên phải. (a) Độ lớn từ trường biến thiên thế nào? (i) Không đổi trên toàn đường đi. (ii) Tăng rồi giảm. (iii) Giảm rồi tăng. (b) Hướng từ trường có thay đổi trên đường đi ấy không?
:::

::: solution Lời giải
(a) Chọn (ii). Các đường sức dày dần khi tiến đến mặt phẳng vòng dây, rồi thưa dần khi đi ra xa về bên phải. Vì vậy, độ lớn trường tăng đến cực đại ở mặt phẳng vòng dây rồi giảm.

(b) Hướng không đổi. Với chiều dòng trong hình, từ trường dọc trục hướng sang phải ở mọi vị trí trên đường đi. Vector trường luôn tiếp tuyến với đường sức tại điểm đang xét.
:::
