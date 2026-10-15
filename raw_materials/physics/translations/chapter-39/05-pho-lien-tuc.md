## 39.5. Phổ liên tục và bức xạ vật đen

Nguyên tử trong khí loãng gần như hoạt động độc lập và phát những vạch phổ riêng. Nhưng một vật rắn hoặc chất lỏng nóng thường phát bức xạ trải trên một dải bước sóng liên tục. Vì sao cùng là vật chất mà hai dạng phổ lại khác nhau?

Một âm thoa riêng lẻ phát âm gần một tần số xác định. Nếu nhét nhiều âm thoa sát nhau trong một chiếc va li rồi lắc, tương tác giữa chúng làm âm thanh trở thành tiếng ồn có dải tần rộng. Tương tự, các nguyên tử ở gần nhau trong vật rắn hoặc chất lỏng không còn ứng xử như những nguyên tử cô lập.

Để khảo sát định lượng, ta xét một mô hình lý tưởng của vật nóng, đặc. Mức năng lượng và photon, vốn giải thích phổ vạch, cũng cần thiết để giải thích phổ liên tục.

### Vật đen và ba đặc điểm thực nghiệm

Một bề mặt phát bức xạ lý tưởng cũng hấp thụ hoàn toàn bức xạ tới ở mọi bước sóng. Bề mặt ấy gọi là **vật đen**. Nếu chỉ chiếu sáng mà không xét sự tự phát sáng do nhiệt, nó không phản xạ ánh sáng nên trông đen.

Vật đen hoàn hảo là một lý tưởng hóa, giống dây không khối lượng hoặc mặt phẳng không ma sát. Một hộp rỗng có lỗ nhỏ gần đúng khá tốt mô hình này. Ánh sáng đi qua lỗ phản xạ nhiều lần bên trong và cuối cùng bị hấp thụ. Khi nung nóng hộp, bức xạ đi ra từ lỗ gần phổ vật đen.

![Hình 39.30: Hộp rỗng có lỗ nhỏ gần đúng một vật đen. Ánh sáng đi vào bị hấp thụ sau nhiều lần phản xạ, còn bức xạ thoát ra khi hộp nóng có phổ gần phổ vật đen.](../img/young-39/hinh-39-30.png)

Đến khoảng năm 1900, ba đặc điểm của bức xạ này đã được xác lập.

Thứ nhất, tổng công suất phát trên một đơn vị diện tích, ký hiệu $I$, tỉ lệ với lũy thừa bậc bốn của nhiệt độ tuyệt đối. Đó là **định luật Stefan–Boltzmann**:

$$
I=\sigma T^4.
\tag{39.19}
$$

Đơn vị của $I$ là $\mathrm{W/m^2}$. Khi biểu diễn bằng đơn vị $\mathrm{W/(m^2\,K^4)}$, hằng số Stefan–Boltzmann có giá trị số $5{,}67037442\times10^{-8}$.

Quan hệ này cũng xuất hiện trong bài toán truyền nhiệt bằng bức xạ.

![Hình 39.31: Vết đen trên bề mặt Mặt Trời có nhiệt độ khoảng 4000 K, thấp hơn vùng xung quanh khoảng 5800 K. Nó vẫn phát sáng, nhưng phát ít năng lượng hơn trên cùng diện tích nên trông tối hơn.](../img/young-39/hinh-39-31.png)

Theo mô hình vật đen, tỉ số cường độ toàn phần của hai vùng là

$$
\left(\frac{4000}{5800}\right)^4\approx0{,}23.
$$

Thứ hai, năng lượng không phân bố đều theo bước sóng. **Suất phát xạ phổ** $I(\lambda)$ cho công suất trên một đơn vị diện tích và trên một đơn vị khoảng bước sóng. Phần cường độ thuộc khoảng rất nhỏ từ $\lambda$ đến $\lambda+d\lambda$ bằng $I(\lambda)\,d\lambda$.

Tổng cường độ bằng diện tích dưới đường phân bố:

$$
I=\int_0^\infty I(\lambda)\,d\lambda.
\tag{39.20}
$$

::: warning Phân biệt suất phát xạ phổ và cường độ toàn phần

$I$ có đơn vị $\mathrm{W/m^2}$, còn $I(\lambda)$ có đơn vị $\mathrm{W/m^3}$ khi bước sóng đo bằng mét. Phải nhân với độ rộng bước sóng hoặc lấy tích phân mới thu được công suất trên một đơn vị diện tích.

:::

![Hình 39.32: Suất phát xạ phổ của vật đen ở 1250 K, 1750 K và 2000 K. Nhiệt độ tăng làm đỉnh cao hơn và dịch về bước sóng ngắn hơn.](../img/young-39/hinh-39-32.png)

Mỗi đường cong có một bước sóng cực đại $\lambda_m$. Thực nghiệm cho

$$
\lambda_mT=2{,}90\times10^{-3}\,\mathrm{m\,K}.
\tag{39.21}
$$

Đây là **định luật dịch chuyển Wien**. Khi nhiệt độ tăng, đỉnh dịch về bước sóng ngắn hơn. Một vật phát sáng vàng thường nóng hơn và sáng hơn một vật cùng kích thước phát sáng đỏ.

Thứ ba, các đường phân bố ở những nhiệt độ khác nhau có cùng dạng sau khi đổi thang thích hợp cho hai trục. Một lý thuyết đúng phải giải thích được đồng thời cả ba đặc điểm.

### Rayleigh và tai biến tử ngoại

Trong các nỗ lực cuối thế kỷ XIX, Lord Rayleigh xét sóng điện từ trong hộp chữ nhật. Hộp có những mode dao động chuẩn, tương tự các sóng điện từ dừng đã khảo sát trước đó.

Ông dùng nguyên lý phân bố đều năng lượng: Tính cả năng lượng điện trường lẫn từ trường, mỗi mode có năng lượng trung bình $kT$. Sau khi đếm số mode theo khoảng bước sóng và tính bức xạ thoát qua lỗ, kết quả là

$$
I(\lambda)=\frac{2\pi ckT}{\lambda^4}.
\tag{39.22}
$$

Ở bước sóng dài, công thức phù hợp khá tốt với thực nghiệm. Nhưng khi $\lambda$ tiến về không, nó tăng không giới hạn như $1/\lambda^4$, trong khi đường thực nghiệm giảm về không.

Tệ hơn, tích phân trên mọi bước sóng phân kỳ. Lý thuyết dự đoán tổng công suất phát trên một đơn vị diện tích là vô hạn. Sự thất bại này được gọi là **tai biến tử ngoại**.

### Giả thuyết lượng tử của Planck

Năm 1900, Max Planck tìm được hàm phân bố phù hợp với thực nghiệm. Điểm mới là giả thuyết rằng các dao động điện từ trong thành hộp, có tần số $f$, chỉ nhận năng lượng

$$
E_n=nhf.
$$

Ở đây $n=0,1,2,3,\ldots$. Các mức đầu là $0,hf,2hf,3hf,\ldots$. Khi trao đổi năng lượng với sóng điện từ trong hộp, dao động chỉ phát hoặc hấp thụ những lượng bội của $hf$. Điều này khác với giả thiết cổ điển cho phép một mode nhận năng lượng liên tục tùy ý.

Ban đầu Planck xem lượng tử hóa như một thủ thuật tính toán hơn là nguyên lý nền tảng. Trong thư gửi một người bạn, ông gọi đó là “một hành động tuyệt vọng”, vì phải tìm ra lời giải thích lý thuyết bằng bất cứ giá nào.

Năm năm sau, Einstein nhận ra lượng chênh lệch $hf$ chính là năng lượng một photon. Những bằng chứng tiếp theo khiến đến khoảng năm 1915, mô tả lượng tử và sự tồn tại của photon đã được thừa nhận rộng rãi.

Về lịch sử, lượng tử hóa của Planck xuất hiện trước mô hình mức năng lượng nguyên tử được trình bày ở các mục trước. Công lao khởi đầu thuộc về Planck. Ông nhận giải Nobel Vật lý năm 1918.

![Hình 39.33: Hai dãy mức năng lượng của dao động tử. Dao động tử tần số thấp có khoảng cách mức hf nhỏ hơn dao động tử tần số cao.](../img/young-39/hinh-39-33.png)

Hình 39.33 giải thích vì sao giả thuyết lượng tử làm giảm bức xạ ở tần số cao. Khoảng cách giữa hai mức kề nhau là $hf$. Khi $hf$ nhỏ so với năng lượng nhiệt, nhiều dao động tử có thể được kích thích. Khi $hf$ lớn, rất ít dao động tử đạt mức đủ cao để phát photon.

Gọi $N_n$ là số dao động tử ở mức $nhf$. Phân bố Boltzmann cho $N_n=Ae^{-nhf/(kT)}$, trong đó $A$ là hệ số chung. Tỉ số số dao động tử ở mức kích thích thứ nhất so với mức cơ bản là

$$
\begin{aligned}
\frac{N_1}{N_0}&=\frac{Ae^{-hf/(kT)}}{Ae^0}\\
&=e^{-hf/(kT)}.
\end{aligned}
\tag{39.23}
$$

Ở $T=2000\,\mathrm K$, năng lượng nhiệt khoảng $kT=0{,}172\,\mathrm{eV}$.

- Photon có $\lambda=3{,}00\,\mu\mathrm m$ mang năng lượng khoảng $0{,}413\,\mathrm{eV}$. Tỉ số $N_1/N_0$ gần $0{,}0909$, tức cỡ một dao động tử ở mức thứ nhất trên mười một dao động tử ở mức cơ bản.
- Photon có $\lambda=0{,}500\,\mu\mathrm m$ mang năng lượng khoảng $2{,}48\,\mathrm{eV}$. Tỉ số chỉ cỡ $5{,}6\times10^{-7}$, gần một trên hai triệu.

Hai con số là tỉ số so với mức cơ bản, không phải tỉ lệ trên tổng số dao động tử ở mọi mức. Dao động tử ở mức cơ bản không thể phát photon bằng cách hạ thêm một mức. Vì vậy, sự phát photon bước sóng ngắn bị giảm mạnh so với dự đoán của Rayleigh.

### Mắt và màu sắc của sao

Phần bên trong mắt người, mèo hoặc cá thường trông đen dù mô bên trong không có màu đen. Ánh sáng vào mắt bị hấp thụ sau các lần phản xạ bên trong, gần với cơ chế của hộp có lỗ nhỏ.

![Ứng dụng: Bên trong mắt người, mèo và cá có thể gần đúng một hốc hấp thụ ánh sáng. Ở nhiệt độ khoảng 300 K, bức xạ nhiệt chủ yếu thuộc vùng hồng ngoại không nhìn thấy.](../img/young-39/ung-dung-doi-mat.png)

Mắt cũng phát bức xạ nhiệt. Ở nhiệt độ cỡ $300\,\mathrm K$, bước sóng đỉnh gần $9{,}7\,\mu\mathrm m$, thuộc hồng ngoại.

### Định luật bức xạ Planck

Kết quả của Planck cho suất phát xạ phổ là

$$
I(\lambda)=\frac{2\pi hc^2}{\lambda^5(e^x-1)},
\tag{39.24}
$$

trong đó $x=hc/(\lambda kT)$. Như vậy, biểu thức chứa đầy đủ hằng số Planck, tốc độ ánh sáng, hằng số Boltzmann, nhiệt độ tuyệt đối và bước sóng.

Để suy định luật Wien, lấy đạo hàm theo $\lambda$ rồi đặt bằng không. Nghiệm cực đại khác không cho

$$
\lambda_m=\frac{hc}{4{,}965kT}.
\tag{39.25}
$$

Hằng số $4{,}965$ là nghiệm dương khác không của phương trình

$$
5-x=5e^{-x}.
\tag{39.26}
$$

Có thể tìm nghiệm bằng thử dần hoặc một phương pháp số. Từ các hằng số cơ bản, giá trị $hc/(4{,}965k)$ gần $2{,}90\times10^{-3}\,\mathrm{m\,K}$, đúng với hệ số Wien.

Lấy tích phân định luật Planck trên mọi bước sóng cho

$$
\begin{aligned}
I&=\int_0^\infty I(\lambda)\,d\lambda\\
&=\frac{2\pi^5k^4}{15c^2h^3}T^4\\
&=\sigma T^4.
\end{aligned}
\tag{39.27}
$$

Do đó,

$$
\sigma=\frac{2\pi^5k^4}{15c^2h^3}.
\tag{39.28}
$$

Thay các giá trị hằng số cơ bản nhất quán vào cho $\sigma\approx5{,}6704\times10^{-8}\,\mathrm{W/(m^2\,K^4)}$. Định luật Planck vừa mô tả hình dạng phổ, vừa chứa hai định luật thực nghiệm như những hệ quả.

Ở bước sóng dài, $x=hc/(\lambda kT)$ rất nhỏ. Dùng $e^x\approx1+x$ trong mẫu số, công thức Planck trở về công thức Rayleigh (39.22). Biểu thức giới hạn không còn $h$, phù hợp với việc hiệu ứng lượng tử giảm vai trò khi năng lượng photon rất nhỏ.

Các sao có nhiệt độ bề mặt từ dưới $2500\,\mathrm K$ đến trên $30\,000\,\mathrm K$. Một sao ở $12\,000\,\mathrm K$ có đỉnh phổ trong tử ngoại, phát nhiều ánh sáng lam hơn đỏ nên thường trông xanh. Sao ở $3000\,\mathrm K$ có đỉnh trong hồng ngoại và thường trông đỏ.

![Ứng dụng: Màu sao và các đường phân bố Planck. Sao nóng phát tương đối nhiều ánh sáng lam, sao lạnh phát tương đối nhiều ánh sáng đỏ, còn sao nhiệt độ trung gian phát nhiều bước sóng nhìn thấy cùng lúc.](../img/young-39/ung-dung-mau-sao.png)

Với Mặt Trời ở khoảng $5800\,\mathrm K$, đỉnh nằm trong vùng nhìn thấy. Màu tổng hợp của sao gần trắng, không chỉ là màu của riêng bước sóng tại đỉnh.

### Ví dụ 39.7: Ánh sáng từ Mặt Trời

Coi bề mặt Mặt Trời gần đúng vật đen ở $5800\,\mathrm K$, bỏ qua các vạch hấp thụ do khí quyển Mặt Trời. (a) Bước sóng nào được phát mạnh nhất? (b) Tổng công suất phát trên một đơn vị diện tích bằng bao nhiêu?

**Nhận dạng:** Cần tìm bước sóng đỉnh và công suất trên diện tích, nên dùng định luật Wien và Stefan–Boltzmann.

**Chuẩn bị:** Dùng $T=5800\,\mathrm K$ và $\sigma\approx5{,}67\times10^{-8}\,\mathrm{W/(m^2\,K^4)}$.

**Thực hiện:**

(a) Bước sóng đỉnh là

$$
\begin{aligned}
\lambda_m&=\frac{2{,}90\times10^{-3}}{5800}\,\mathrm m\\
&=5{,}00\times10^{-7}\,\mathrm m\\
&=500\,\mathrm{nm}.
\end{aligned}
$$

(b) Cường độ toàn phần tại bề mặt là

$$
\begin{aligned}
I&=\sigma T^4\\
&\approx6{,}42\times10^7\,\mathrm{W/m^2}\\
&=64{,}2\,\mathrm{MW/m^2}.
\end{aligned}
$$

**Đánh giá:** Bước sóng $500\,\mathrm{nm}$ gần giữa miền nhìn thấy. Mắt người thích nghi với nguồn sáng tự nhiên có phổ mạnh trong miền này.

Giá trị $64{,}2\,\mathrm{MW/m^2}$ là tại bề mặt Mặt Trời. Với bán kính Mặt Trời $R=6{,}96\times10^8\,\mathrm m$ và khoảng cách Trái Đất $r=1{,}50\times10^{11}\,\mathrm m$, năng lượng phân bố trên mặt cầu lớn hơn. Cường độ giảm theo hệ số $(R/r)^2\approx2{,}15\times10^{-5}$, còn khoảng $1{,}4\,\mathrm{kW/m^2}$.

**Khái niệm cần nhớ:** Nhiệt độ cao hơn cho bước sóng đỉnh ngắn hơn, còn tổng công suất phát trên diện tích tăng theo $T^4$.

### Ví dụ 39.8: Một khoảng hẹp trong phổ Mặt Trời

Tính công suất phát trên một đơn vị diện tích bề mặt Mặt Trời trong khoảng từ $600{,}0$ đến $605{,}0\,\mathrm{nm}$.

**Nhận dạng:** Đây là phần diện tích dưới đường suất phát xạ phổ trên một khoảng hẹp, không phải tổng công suất ở mọi bước sóng.

**Chuẩn bị:** Dùng $T=5800\,\mathrm K$. Lấy giá trị tại trung điểm $\lambda=602{,}5\,\mathrm{nm}$ nhân với độ rộng $\Delta\lambda=5{,}0\,\mathrm{nm}$ để xấp xỉ tích phân.

**Thực hiện:** Với $h=6{,}626\times10^{-34}\,\mathrm{J\,s}$, $c=2{,}998\times10^8\,\mathrm{m/s}$ và $k=1{,}381\times10^{-23}\,\mathrm{J/K}$,

$$
x=\frac{hc}{\lambda kT}\approx4{,}116.
$$

Thay vào định luật Planck:

$$
I(\lambda)\approx7{,}81\times10^{13}\,\mathrm{W/m^3}.
$$

Gọi $I_{\rm band}$ là phần cường độ trong khoảng đang xét. Khi ấy,

$$
\begin{aligned}
I_{\rm band}&\approx I(\lambda)\Delta\lambda\\
&\approx3{,}9\times10^5\,\mathrm{W/m^2}\\
&=0{,}39\,\mathrm{MW/m^2}.
\end{aligned}
$$

**Đánh giá:** So với tổng $64{,}2\,\mathrm{MW/m^2}$, khoảng hẹp này chứa cỡ $0{,}6\%$ công suất phát trên diện tích.

**Khái niệm cần nhớ:** Định luật Planck cho suất phát xạ trên mỗi khoảng bước sóng. Muốn tìm phần công suất trong một dải, phải lấy tích phân theo bước sóng trên dải ấy.

### Câu hỏi tự kiểm tra 39.5

Một vật đen ở $2000\,\mathrm K$ có phát (a) tia X và (b) sóng vô tuyến không?

<details><summary>Xem đáp án và giải thích</summary>

Cả (a) và (b) đều có. Với mọi bước sóng hữu hạn, dương và nhiệt độ dương, định luật Planck cho suất phát xạ phổ dương. Nó tiến về không khi bước sóng tiến về không hoặc tiến tới vô hạn.

Tuy nhiên, ở $2000\,\mathrm K$, bức xạ rất yếu ở bước sóng ngắn hơn nhiều so với $1\,\mu\mathrm m$, trong đó có tia X. Nó cũng yếu ở bước sóng dài hơn nhiều so với vài micromét, trong đó có sóng vô tuyến. Có phát về mặt mô hình không có nghĩa là phát mạnh hoặc dễ phát hiện.

</details>
