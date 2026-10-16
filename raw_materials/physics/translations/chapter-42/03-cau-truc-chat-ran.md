## 42.3. Cấu trúc chất rắn

Thuật ngữ **vật chất ngưng tụ** (condensed matter) bao gồm cả thể rắn và thể lỏng. Trong cả hai trạng thái này, tương tác giữa các nguyên tử lân cận có cường độ tương đương với các liên kết phân tử. Điểm khác biệt căn bản là: Trong chất lỏng, các phân tử có thể trượt tự do qua nhau. Còn trong chất rắn, các nguyên tử dao động với biên độ nhỏ xung quanh những vị trí cân bằng cố định trong không gian.

Dựa vào mức độ trật tự trong sự sắp xếp của các nguyên tử, chất rắn được phân thành hai nhóm lớn:
1. **Chất rắn tinh thể (Crystalline solids)**: Các nguyên tử, ion hoặc phân tử được sắp xếp theo một trật tự không gian ba chiều có tính tuần hoàn lặp lại trên quy mô lớn, gọi là **trật tự xa** (long-range order). Đa số các kim loại, muối khoáng và chất bán dẫn đều thuộc loại này.
2. **Chất rắn vô định hình (Amorphous solids)**: Các nguyên tử chỉ có sự sắp xếp trật tự với các nguyên tử lân cận gần nhất, gọi là **trật tự gần** (short-range order), nhưng không có tính tuần hoàn đều đặn trên toàn khối vật liệu. Thủy tinh, nhựa đường và nhiều loại polyme vô định hình là những ví dụ điển hình.

Ngoài hai trạng thái quen thuộc trên, một số chất hữu cơ có thể tồn tại ở trạng thái trung gian kỳ thú gọi là **tinh thể lỏng** (liquid crystals). Trong tinh thể lỏng, các phân tử có dạng hình que dài có xu hướng định hướng song song với nhau nhưng lại có thể chuyển động trượt tự do giống như chất lỏng. Tính chất quang học của tinh thể lỏng có thể thay đổi nhanh chóng dưới tác dụng của điện trường ngoài, tạo nên nguyên lý hoạt động của các màn hình tinh thể lỏng (LCD) phổ biến trong đời sống.

Cấu trúc tinh thể được khảo sát bằng các phương pháp thực nghiệm nhiễu xạ: Nhiễu xạ tia X, nhiễu xạ chùm electron hoặc nhiễu xạ chùm neutron. Khi bước sóng của bức xạ có độ lớn tương đương với khoảng cách giữa các mặt phẳng nguyên tử trong tinh thể ($\sim 0{,}1\,\mathrm{nm}$), hiện tượng giao thoa tăng cường xuất hiện theo định luật Bragg với bậc nhiễu xạ $m = 1, 2, 3, \dots$:

$$
2d\sin\theta = m\lambda
$$

### Mạng tinh thể và cơ sở

Để mô tả toán học một tinh thể, ta phân biệt hai khái niệm riêng biệt: **Mạng tinh thể** (crystal lattice) và **cơ sở** (basis).
- **Mạng tinh thể**: Là một lưới hình học gồm vô hạn các điểm (nút mạng) phân bố tuần hoàn trong không gian ba chiều. Môi trường xung quanh bất kỳ nút mạng nào cũng hoàn toàn giống hệt môi trường xung quanh mọi nút mạng khác.
- **Cơ sở**: Là một nhóm gồm một hoặc nhiều nguyên tử có cấu hình không gian xác định, được gắn giống hệt nhau vào từng nút mạng của mạng tinh thể.

Nói một cách ngắn gọn: Cấu trúc tinh thể là sự kết hợp giữa mạng tinh thể và cơ sở.

Trong không gian ba chiều, các nhà tinh thể học chứng minh được rằng chỉ có đúng 14 kiểu mạng tuần hoàn thỏa mãn tính đối xứng tịnh tiến, gọi là **14 mạng Bravais**, được phân thành 7 hệ tinh thể.

![Hình 42.11: Một số kiểu mạng tinh thể phổ biến trong tự nhiên. (a) Lập phương đơn giản (sc). (b) Lập phương tâm diện (fcc). (c) Lập phương tâm khối (bcc). (d) Lục giác xếp chặt (hcp). (e) Hình chiếu bằng của cấu trúc lục giác xếp chặt.](../img/young-42/hinh-42-11.png)

::: warning Cảnh báo: Mạng tinh thể lý tưởng là vô hạn
Một mạng tinh thể thực tế chứa hàng tỷ tỷ nguyên tử và trên lý thuyết là vô hạn. Hình 42.11 chỉ hiển thị một phần nhỏ thể tích đủ để minh họa tính chất đối xứng và hình học tuần hoàn của mạng. Khối thể tích nhỏ nhất có tính lặp lại đó được gọi là **ô mạng cơ sở** (unit cell).
:::

Ba kiểu mạng lập phương thường gặp nhất bao gồm:
1. **Lập phương đơn giản (Simple cubic - sc)**: Các nút mạng chỉ nằm ở 8 đỉnh của một hình lập phương cạnh $a$. Mỗi nguyên tử ở đỉnh được chia sẻ chung bởi 8 ô mạng kề nhau, do đó một ô mạng cơ sở chỉ chứa $8 \times (1/8) = 1$ nguyên tử.

Mỗi nguyên tử có 6 nguyên tử lân cận gần nhất cách một khoảng $a$, nên **số phối vị** (coordination number) bằng 6. Cấu trúc này có mật độ xếp chặt rất thấp (hệ số xếp chặt chỉ đạt $52\%$), nên rất hiếm gặp trong tự nhiên (chỉ có nguyên tố polonium ở dạng $\alpha$-Po kết tinh theo dạng này).

2. **Lập phương tâm khối (Body-centered cubic - bcc)**: Ngoài 8 nguyên tử ở 8 đỉnh, có thêm một nguyên tử nằm chính giữa khối lập phương (Hình 42.12a). Số nguyên tử thuộc về một ô mạng là $8 \times (1/8) + 1 = 2$ nguyên tử.

Nguyên tử ở tâm tiếp xúc với 8 nguyên tử ở các đỉnh, do đó số phối vị bằng 8. Khoảng cách giữa các nguyên tử lân cận gần nhất bằng nửa đường chéo chính: $\frac{1}{2}a\sqrt{3}$. Nhiều kim loại như sắt ($\alpha$-Fe), natri, kali, wolfram kết tinh theo mạng bcc.

3. **Lập phương tâm diện (Face-centered cubic - fcc)**: Ngoài 8 nguyên tử ở 8 đỉnh, có thêm 6 nguyên tử nằm ở tâm của 6 mặt ngoài hình lập phương (Hình 42.12b). Mỗi nguyên tử ở tâm mặt được chia sẻ bởi 2 ô mạng kề nhau, do đó số nguyên tử trong một ô mạng là $8 \times (1/8) + 6 \times (1/2) = 4$ nguyên tử.

Số phối vị của mạng fcc bằng 12, và khoảng cách giữa các nguyên tử lân cận gần nhất bằng nửa đường chéo mặt: $\frac{1}{2}a\sqrt{2}$. Nhiều kim loại quan trọng như đồng, nhôm, bạc, vàng, chì kết tinh theo mạng fcc.

![Hình 42.12: So sánh cấu trúc ô mạng cơ sở của (a) mạng lập phương tâm khối (bcc) với một nguyên tử ở tâm khối tiếp xúc với 8 nguyên tử ở đỉnh, và (b) mạng lập phương tâm diện (fcc) với các nguyên tử nằm ở tâm của 6 mặt ngoài khối lập phương.](../img/young-42/hinh-42-12.png)

4. **Lục giác xếp chặt (Hexagonal close-packed - hcp)**: Cùng với mạng fcc, cấu trúc hcp đại diện cho cách xếp chặt nhất các quả cầu cứng có cùng kích thước trong không gian ba chiều, với hệ số lấp đầy thể tích cực đại đạt $74\%$ và số phối vị bằng 12. Sự khác biệt giữa fcc và hcp nằm ở thứ tự xếp chồng các lớp nguyên tử: Nếu các lớp nguyên tử xếp chồng theo chu kỳ hai lớp lặp lại $ABABAB\dots$ thì ta thu được cấu trúc hcp (như magie, titan, kẽm). Còn nếu xếp chồng theo chu kỳ ba lớp $ABCABC\dots$ thì ta thu được cấu trúc fcc.

### Cấu trúc tinh thể của các hợp chất

Khi tinh thể được cấu thành từ nhiều nguyên tố hóa học khác nhau, cấu trúc tinh thể được mô tả bằng một mạng Bravais kết hợp với một cơ sở gồm hai hay nhiều ion hoặc nguyên tử.

![Hình 42.13: Cấu trúc tinh thể muối ăn ($\mathrm{NaCl}$). Mạng tinh thể gồm hai mạng lập phương tâm diện (fcc) lồng vào nhau, dịch chuyển tương đối một đoạn bằng nửa cạnh ô mạng ($a/2$) dọc theo trục tọa độ. Mỗi ion natri $\mathrm{Na}^+$ được bao quanh bởi 6 ion clorua $\mathrm{Cl}^-$, và ngược lại.](../img/young-42/hinh-42-13.png)

Trong tinh thể muối ăn $\mathrm{NaCl}$ (Hình 42.13), các ion $\mathrm{Na}^+$ và $\mathrm{Cl}^-$ phân bố xen kẽ đều đặn. Cấu trúc này có thể xem là một mạng fcc của các ion $\mathrm{Cl}^-$, với cơ sở gắn vào mỗi nút mạng gồm một ion $\mathrm{Cl}^-$ tại tọa độ $(0, 0, 0)$ và một ion $\mathrm{Na}^+$ tại tọa độ $(a/2, 0, 0)$. Mỗi ion trong tinh thể $\mathrm{NaCl}$ có 6 ion trái dấu là các lân cận gần nhất nằm ở khoảng cách $a/2$, do đó số phối vị của cả hai ion đều bằng 6.

![Hình 42.14: Cấu trúc tinh thể kim cương. Mạng tinh thể là mạng lập phương tâm diện với cơ sở gồm hai nguyên tử carbon giống hệt nhau dịch chuyển tương đối một đoạn bằng một phần tư đường chéo chính khối lập phương $(a/4, a/4, a/4)$. Mỗi nguyên tử carbon liên kết cộng hóa trị với 4 nguyên tử lân cận ở các đỉnh của một hình tứ diện đều.](../img/young-42/hinh-42-14.png)

Cấu trúc tinh thể kim cương (Hình 42.14) cũng dựa trên mạng fcc, nhưng cơ sở gồm hai nguyên tử carbon dịch chuyển tương đối một đoạn bằng một phần tư đường chéo chính:

$$
\left(\frac{a}{4}, \frac{a}{4}, \frac{a}{4}\right)
$$

Trong cấu trúc này, mỗi nguyên tử carbon liên kết cộng hóa trị định hướng mạnh với 4 nguyên tử lân cận gần nhất tạo thành một góc tứ diện $109{,}5^\circ$, mang lại độ cứng kỷ lục cho kim cương. Hai vật liệu bán dẫn then chốt là silic ($\mathrm{Si}$) và germani ($\mathrm{Ge}$) cũng kết tinh theo đúng cấu trúc kim cương này. Khi hai vị trí nguyên tử trong cơ sở được thay thế bằng hai nguyên tố hóa học khác nhau (chẳng hạn kẽm $\mathrm{Zn}$ và lưu huỳnh $\mathrm{S}$, hoặc gali $\mathrm{Ga}$ và asen $\mathrm{As}$), ta thu được cấu trúc **sphalerite** (hay kẽm sulfide $\mathrm{ZnS}$), vốn là cấu trúc nền tảng của nhiều chất bán dẫn hợp chất hiện đại.

### Các loại liên kết trong chất rắn

Tương tự như trong phân tử, liên kết giữ các nguyên tử lại với nhau trong chất rắn được phân thành bốn loại chính:
1. **Chất rắn ion**: Được hình thành bởi lực hút tĩnh điện giữa các ion dương và ion âm (như $\mathrm{NaCl}$, $\mathrm{KCl}$, $\mathrm{LiF}$). Các tinh thể ion có đặc tính: Độ cứng cơ học cao, giòn, nhiệt độ nóng chảy cao, và cách điện rất tốt ở nhiệt độ phòng do không có hạt tải điện tự do (nhưng trở thành chất dẫn điện tốt khi bị nóng chảy thành thể lỏng).
2. **Chất rắn cộng hóa trị**: Các nguyên tử liên kết với nhau bằng các cặp electron dùng chung định hướng mạnh trong không gian (như kim cương, silic, thạch anh $\mathrm{SiO}_2$). Chúng có độ bền liên kết rất lớn, nhiệt độ nóng chảy rất cao, độ cứng cao và độ dẫn điện kém ở nhiệt độ thấp.
3. **Chất rắn kim loại**: Trong kim loại, các electron hóa trị ngoài cùng liên kết rất lỏng lẻo với hạt nhân. Khi các nguyên tử tập hợp lại thành tinh thể, các electron này tách khỏi nguyên tử mẹ và chuyển động tự do trong toàn bộ thể tích khối chất rắn, tạo thành một "biển electron tự do" (hay khí electron) bao bọc mạng lưới các ion dương cố định (Hình 42.15).

![Hình 42.15: Trong tinh thể kim loại, các electron hóa trị bị bứt khỏi nguyên tử mẹ và chuyển động tự do trong toàn bộ mạng tinh thể, tạo thành một biển electron tự do bao quanh mạng lưới các ion dương cố định. Sự hiện diện của các electron tự do giải thích độ dẫn điện và dẫn nhiệt cao của kim loại.](../img/young-42/hinh-42-15.png)

Biển electron tự do này giữ các ion dương lại với nhau mà không có tính định hướng không gian chặt chẽ như liên kết cộng hóa trị. Điều này mang lại cho kim loại những tính chất cơ học và vật lý độc nhất vô nhị: Khả năng dẫn điện và dẫn nhiệt cao, ánh kim rực rỡ, tính dẻo và tính dễ dát mỏng, uốn nắn thành hình dáng mong muốn.

4. **Chất rắn phân tử**: Được cấu tạo từ các phân tử trung hòa liên kết với nhau bằng lực van der Waals yếu hoặc liên kết hydro (như băng đá $\mathrm{H}_2\mathrm{O}$, băng khô $\mathrm{CO}_2$, tinh thể iot $\mathrm{I}_2$). Do lực liên kết yếu, các chất rắn phân tử thường mềm, có nhiệt độ nóng chảy thấp và rất dễ thăng hoa.

### Ví dụ 42.4: Thế năng tương tác tĩnh điện của chuỗi tinh thể ion một chiều

Xét một chuỗi tinh thể ion lý thuyết một chiều gồm một số lượng rất lớn các ion dương và âm xen kẽ mang điện tích $+e$ và $-e$, phân bố cách đều nhau một khoảng $a$ dọc theo một đường thẳng. Chứng minh rằng tổng thế năng tương tác tĩnh điện là một số âm (thiết lập tính liên kết về mặt năng lượng so với các ion riêng biệt ở xa vô cùng).

**Nhận diện và thiết lập**: Ta xem mỗi ion như một điện tích điểm. Thế năng tương tác điện giữa hai điện tích điểm $q$ và $q_0$ cách nhau khoảng cách $r$ là $U = q q_0 / (4\pi\varepsilon_0 r)$. Ta chọn một ion được đánh dấu (tagged ion) nằm ở giữa chuỗi để tính tổng thế năng tương tác của nó với tất cả các ion khác. Sau đó, ta xác định tổng thế năng tương tác của toàn bộ mạng tinh thể tính theo từng cặp ion (không đếm lặp lại).

**Thực hiện**: Chọn một ion làm gốc tọa độ và tính tổng thế năng tương tác của nó với tất cả các ion nằm về một phía của nó (phía bên phải).
- Ion thứ nhất ở khoảng cách $a$ mang điện tích trái dấu, thế năng tương tác là:

$$
U_1 = -\frac{1}{4\pi\varepsilon_0}\frac{e^2}{a}
$$

- Ion thứ hai ở khoảng cách $2a$ mang điện tích cùng dấu, thế năng tương tác là:

$$
U_2 = +\frac{1}{4\pi\varepsilon_0}\frac{e^2}{2a}
$$

- Ion thứ ba ở khoảng cách $3a$ mang điện tích trái dấu, thế năng tương tác là:

$$
U_3 = -\frac{1}{4\pi\varepsilon_0}\frac{e^2}{3a}
$$

Gọi $U_+$ là tổng tương tác với các ion ở một phía, được đánh số $j=1,2,\dots$ theo khoảng cách $ja$. Ta cộng lần lượt $U_1,U_2,U_3,\dots$:

$$
U_+=\sum_{j=1}^{\infty}U_j.
$$

Thay các số hạng đã tính, ta được chuỗi đan dấu:

$$
\begin{aligned}
&U_+ = -\frac{e^2}{4\pi\varepsilon_0 a}\,S, \\
&S = 1 - \frac{1}{2} + \frac{1}{3} - \frac{1}{4} + \dots
\end{aligned}
$$

Chuỗi số trong dấu ngoặc đơn chính là khai triển chuỗi Taylor của logarit tự nhiên $\ln(1 + x)$ tại điểm $x = 1$, với chuỗi số tổng quát $\ln(1 + x) = \sum_{n=1}^\infty (-1)^{n-1} x^n / n$. Khi thay $x = 1$, chuỗi số hội tụ về giá trị $\ln(1 + 1)=\ln 2$, xấp xỉ $0{,}69315$. Do đó:

$$
U_+ = -\frac{e^2}{4\pi\varepsilon_0 a}\ln 2
$$

Vì $\ln 2 > 0$, đại lượng này chắc chắn là một số âm. Các ion nằm ở phía đối diện của chuỗi đóng góp một lượng thế năng hoàn toàn tương đương, do đó tổng thế năng tương tác của ion được đánh dấu với toàn bộ chuỗi hai phía là:

$$
\begin{aligned}
U_{\mathrm{tagged}} &= 2U_+ \\
&= -\frac{2\ln 2}{4\pi\varepsilon_0}\frac{e^2}{a} \\
&\approx -1{,}386\,\frac{1}{4\pi\varepsilon_0}\frac{e^2}{a}
\end{aligned}
$$

Xét một chuỗi tinh thể gồm $N$ ion. Nếu ta nhân $N$ với $U_{\mathrm{tagged}}$, mỗi cặp tương tác $(i, j)$ giữa hai ion sẽ bị đếm lặp hai lần. Do đó, để tránh đếm hai lần (no double-counting), tổng thế năng tương tác toàn phần của hệ $N$ ion tính theo từng cặp là:

$$
\begin{aligned}
U_{\mathrm{total}} &= \frac{1}{2}\sum_{i=1}^N U_i \\
&= -\frac{N\ln 2}{4\pi\varepsilon_0}\frac{e^2}{a} \\
&\approx -0{,}693 N\,\frac{1}{4\pi\varepsilon_0}\frac{e^2}{a}
\end{aligned}
$$

Năng lượng thế năng tĩnh điện tính trên mỗi ion của tinh thể là:

$$
\frac{U_{\mathrm{total}}}{N} = -\frac{\ln 2}{4\pi\varepsilon_0}\frac{e^2}{a}
$$

**Đánh giá**: Vì tổng thế năng tương tác tĩnh điện mang giá trị âm ($U_{\mathrm{total}} < 0$), hệ tinh thể có năng lượng thấp hơn so với trạng thái các ion phân ly ở xa vô cùng ($U = 0$). Kết quả này chứng minh tính liên kết về mặt năng lượng (energetic binding) của mạng tinh thể ion.

Tuy nhiên, cần phân biệt rõ ràng giữa tính liên kết về mặt năng lượng và trạng thái cân bằng cơ học bền vững (mechanical equilibrium). Nếu chỉ tồn tại lực hút tĩnh điện Coulomb ($U \propto -1/a$), lực tương tác luôn mang tính chất hút ở mọi khoảng cách và có xu hướng kéo các ion co cụm vô hạn về $a \to 0$ để thế năng giảm sâu về $-\infty$. Mạng tinh thể chỉ đạt được trạng thái cân bằng cơ học bền vững tại một khoảng cách mạng xác định $a_0$ khi có sự xuất hiện của lực đẩy lượng tử tầm ngắn do nguyên lý loại trừ Pauli sinh ra khi các lớp vỏ electron xen phủ nhau ($U_{\mathrm{rep}} \propto 1/a^n$). Vị trí cân bằng cơ học là nghiệm của phương trình triệt tiêu lực tổng hợp:

$$
\left.\frac{dU_{\mathrm{net}}}{da}\right|_{a=a_0} = 0
$$

Trong tinh thể ba chiều thực tế, tổng thế năng tĩnh điện của một ion trong mạng được viết dưới dạng tương tự thông qua **hằng số Madelung** $\alpha$:

$$
U_{\mathrm{net}} = -\alpha\,\frac{1}{4\pi\varepsilon_0}\frac{e^2}{r}
$$

Đối với mạng $\mathrm{NaCl}$ ba chiều, hằng số Madelung có giá trị $\alpha \approx 1{,}7476$, phản ánh sự đóng góp tổng hợp của các tầng ion lân cận trong không gian ba chiều.

::: tip Khái niệm cốt lõi: Tính liên kết của tinh thể ion
Một tinh thể ion có tính liên kết về mặt năng lượng vì tổng thế năng tĩnh điện Coulomb của các cặp ion trong mạng âm hơn so với khi tách rời các ion ra xa vô cùng. Trạng thái cân bằng cơ học bền vững của tinh thể được xác lập nhờ sự triệt tiêu lẫn nhau giữa lực hút tĩnh điện Coulomb tầm xa và lực đẩy lượng tử tầm ngắn do nguyên lý loại trừ Pauli.
:::

### Sai hỏng mạng tinh thể

Mọi tinh thể trong thế giới thực đều không hoàn hảo tuyệt đối mà luôn chứa các khuyết tật mạng (defects). Các sai hỏng mạng được phân loại theo số chiều không gian:
- **Khuyết tật điểm (Point defects)**: Gồm nút khuyết (vacancy, vị trí nút mạng bị bỏ trống), nguyên tử xen kẽ (interstitial, nguyên tử chui vào khoảng trống giữa các nút mạng), và nguyên tử tạp chất (thay thế hoặc xen kẽ). Các khuyết tật điểm có vai trò trong việc tạo ra tính dẫn điện của chất bán dẫn pha tạp và tạo nên màu sắc rực rỡ của đá quý.
- **Khuyết tật đường (Line defects - Dislocations)**: Gồm lệch mạng biên (edge dislocation) và lệch mạng xoắn (screw dislocation). Lệch mạng biên xuất hiện khi có một nửa mặt phẳng nguyên tử bị chèn thêm vào mạng tinh thể (Hình 42.16).

![Hình 42.16: Lệch mạng biên trong mạng tinh thể hai chiều, hình thành do sự chèn thêm một nửa mặt phẳng nguyên tử vào trong khối tinh thể. Bạn có thể nhận thấy sự bất thường rõ nhất bằng cách quan sát hình vẽ từ các hướng khác nhau ở góc nghiêng hẹp so với mặt trang giấy.](../img/young-42/hinh-42-16.png)

Sự hiện diện của các lệch mạng làm giảm ứng suất cắt lý thuyết cần thiết để làm biến dạng tinh thể đi hàng nghìn lần. Thay vì phải bẻ gãy đồng thời toàn bộ các liên kết nguyên tử trên cả một mặt phẳng, tinh thể chỉ cần dịch chuyển từng hàng nguyên tử tại vị trí lệch mạng. Điều này giải thích tại sao các kim loại có thể dễ dàng bị dát mỏng, rèn nguội hoặc uốn cong trong cơ khí chế tạo.

![Ứng dụng: Các tinh thể insulin, một protein gồm 51 axit amin. Những phân tử trong cùng một tinh thể có định hướng giống nhau. Phân tích nhiễu xạ tia X hoặc neutron cho phép suy ra hình dạng và kích thước phân tử. Các nghiên cứu như vậy đã xác định cấu trúc của hơn 100.000 loại protein.](../img/young-42/ung-dung-a-3.png)

### Câu tự kiểm tra 42.3

Nếu $a$ là khoảng cách trong tinh thể $\mathrm{NaCl}$ từ một ion $\mathrm{Na}^+$ đến một trong các ion lân cận gần nhất $\mathrm{Cl}^-$, thì khoảng cách từ ion $\mathrm{Na}^+$ đó đến một trong các ion $\mathrm{Cl}^-$ lân cận thứ hai là bao nhiêu?

(i) $a\sqrt{2}$;
(ii) $a\sqrt{3}$;
(iii) $2a$;
(iv) Không có đáp án nào trong số này.

::: details Giải thích và đáp án
**Đáp án lựa chọn**: (ii) $a\sqrt{3}$.

**Lời giải chi tiết**: Quan sát cấu trúc ô mạng cơ sở của tinh thể $\mathrm{NaCl}$ ở Hình 42.13. Gọi $a$ là khoảng cách giữa hai ion kề nhau nằm dọc theo cạnh của khối lập phương (tức khoảng cách từ một ion $\mathrm{Na}^+$ đến 6 ion $\mathrm{Cl}^-$ lân cận gần nhất).

Các ion $\mathrm{Cl}^-$ lân cận tiếp theo (lân cận thứ hai) của ion $\mathrm{Na}^+$ này nằm ở đỉnh đối diện qua đường chéo của khối lập phương nhỏ có kích thước cạnh bằng $a$. Khoảng cách không gian giữa hai đỉnh đối diện của một hình lập phương cạnh $a$ được tính theo định lý Pythagoras ba chiều:

$$
\begin{aligned}
d &= \sqrt{a^2 + a^2 + a^2} \\
&= a\sqrt{3}
\end{aligned}
$$

Do đó, khoảng cách từ ion natri đến ion clorua lân cận thứ hai bằng $a\sqrt{3}$.
:::
