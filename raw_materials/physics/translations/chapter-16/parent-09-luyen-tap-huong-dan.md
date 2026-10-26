## Bài luyện tập hướng dẫn

Nhóm VP16.9.1–VP16.9.4 dùng phương pháp của Ví dụ 16.5–16.9 ở Mục 16.3 về cường độ và mức cường độ âm. Nhóm VP16.12.1–VP16.12.4 nối với Ví dụ 16.11–16.12 ở Mục 16.4–16.5 về sóng dừng trong cột khí. Nhóm VP16.18.1–VP16.18.4 dùng cách xác định nguồn, người nghe và vận tốc đối với không khí ở Ví dụ 16.14–16.18 trong Mục 16.8.

Ký hiệu $p_m$ là biên độ áp suất, $\rho$ là khối lượng riêng môi trường và $v$ là tốc độ âm. Khi tính mức cường độ âm $\beta$, dùng mốc

$$
I_0=10^{-12}\,\mathrm{W/m^2}.
$$

### VP16.9.1: Biên độ áp suất khi đổi tần số

Một sóng âm tần số $256\,\mathrm{Hz}$ truyền trong không khí có khối lượng riêng $1{,}20\,\mathrm{kg/m^3}$ và tốc độ âm $344\,\mathrm{m/s}$. Cường độ âm là $5{,}50\times10^{-8}\,\mathrm{W/m^2}$.

(a) Biên độ áp suất của sóng bằng bao nhiêu?

(b) Nếu cường độ giữ nguyên nhưng tần số tăng gấp đôi thành $512\,\mathrm{Hz}$, biên độ áp suất thay đổi thế nào?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cường độ và môi trường đã biết. Cần tìm biên độ áp suất, không phải biên độ chuyển vị của các phần tử khí.

**Hướng đi:**

- Dùng quan hệ cường độ với bình phương biên độ áp suất. Quan hệ này chứa trở kháng âm $\rho v$ nhưng không chứa tần số.
- Giữ riêng điều kiện cường độ không đổi ở phần (b). Tăng tần số không đồng nghĩa tăng áp suất nếu cường độ được giữ như cũ.

**Lời giải:** (a) Với sóng âm chạy hình sin,

$$
I=\frac{p_m^2}{2\rho v}.
$$

Do đó

$$
p_m=\sqrt{2\rho vI}.
$$

Thay số được

$$
p_m\approx6{,}74\times10^{-3}\,\mathrm{Pa}.
$$

(b) Cường độ, khối lượng riêng và tốc độ âm đều giữ nguyên, nên biên độ áp suất cũng giữ nguyên. Biên độ chuyển vị lại giảm một nửa, vì cùng áp suất tại tần số cao hơn đòi chuyển vị nhỏ hơn.

</details>

### VP16.9.2: Đổi mức âm thành cường độ

Ở một khoảng cách nhất định tới chuông báo cháy, mức cường độ âm là $85{,}0\,\mathrm{dB}$.

(a) Cường độ âm bằng bao nhiêu?

(b) Cường độ ấy lớn gấp bao nhiêu lần cường độ của âm có mức $67{,}0\,\mathrm{dB}$?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Phần (a) hỏi cường độ tuyệt đối theo mốc chuẩn, còn phần (b) hỏi tỷ số hai cường độ.

**Hướng đi:**

- Đảo định nghĩa logarit của mức âm để tìm cường độ.
- Khi lấy hiệu hai mức âm, mốc chuẩn triệt tiêu. Vì vậy dùng hiệu $18{,}0\,\mathrm{dB}$ để tìm tỷ số, không chia hai số đo dB cho nhau.

**Lời giải:** (a) Định nghĩa mức âm là

$$
\beta=10\log_{10}\frac I{I_0}.
$$

Suy ra

$$
I=I_0\,10^{\beta/10}.
$$

Với mức âm đã cho,

$$
I\approx3{,}16\times10^{-4}\,\mathrm{W/m^2}.
$$

(b) Gọi hai cường độ là $I_1$ và $I_2$. Khi đó

$$
\frac{I_1}{I_2}=10^{(85{,}0-67{,}0)/10}.
$$

Tỷ số xấp xỉ $63{,}1$. Mức âm chỉ chênh $18{,}0\,\mathrm{dB}$ nhưng cường độ lớn hơn nhiều lần, vì thang dB là thang logarit.

</details>

### VP16.9.3: Mức âm của tiếng sư tử gầm

Một con sư tử có thể gầm với mức cường độ âm $114\,\mathrm{dB}$ ở khoảng cách $1{,}00\,\mathrm m$. Tìm mức cường độ âm ở khoảng cách (a) $4{,}00\,\mathrm m$ và (b) $15{,}8\,\mathrm m$. Giả sử cường độ tuân theo định luật nghịch đảo bình phương.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Biết mức âm tại một khoảng cách chuẩn. Sự suy giảm được xét ở cường độ, rồi chuyển sang mức dB.

**Hướng đi:**

- Dùng tỷ số cường độ bằng bình phương tỷ số khoảng cách đảo.
- Lấy logarit tỷ số ấy để tìm độ giảm mức âm. Không áp trực tiếp định luật nghịch đảo bình phương cho số đo dB.

**Lời giải:** Nếu mức âm tại $r_0$ là $\beta_0$, thì

$$
\frac I{I(r_0)}=\left(\frac{r_0}{r}\right)^2.
$$

Suy ra

$$
\beta=\beta_0-20\log_{10}\frac r{r_0}.
$$

(a) Tại $4{,}00\,\mathrm m$,

$$
\beta\approx102\,\mathrm{dB}.
$$

(b) Tại $15{,}8\,\mathrm m$,

$$
\beta\approx90{,}0\,\mathrm{dB}.
$$

Khoảng cách tăng làm cường độ giảm do cùng công suất phân bố trên diện tích lớn hơn. Giả thiết ở đây bỏ qua hấp thụ và vật cản.

</details>

### VP16.9.4: Biên độ áp suất trong khoang máy bay

Mức cường độ âm trong một máy bay chở khách hiện đại đang bay là $66{,}0\,\mathrm{dB}$. Không khí trong khoang có khối lượng riêng $0{,}920\,\mathrm{kg/m^3}$ và tốc độ âm $344\,\mathrm{m/s}$.

(a) Biên độ áp suất của âm bằng bao nhiêu?

(b) Nếu biên độ áp suất tăng $10{,}0$ lần, mức cường độ âm mới bằng bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dùng khối lượng riêng của không khí trong khoang, thấp hơn giá trị thường dùng ở gần mực nước biển.

**Hướng đi:**

- Đổi mức dB thành cường độ rồi suy biên độ áp suất từ trở kháng âm.
- Vì cường độ tỷ lệ bình phương biên độ áp suất, áp suất tăng mười lần làm cường độ tăng một trăm lần.

**Lời giải:** (a) Cường độ tương ứng là

$$
I=I_0\,10^{66{,}0/10}.
$$

Dùng $p_m=\sqrt{2\rho vI}$ cho

$$
p_m\approx5{,}02\times10^{-2}\,\mathrm{Pa}.
$$

(b) Tỷ số cường độ bằng

$$
\frac{I'}I=10{,}0^2=100.
$$

Mức âm tăng

$$
\Delta\beta=20{,}0\,\mathrm{dB}.
$$

Vì vậy mức mới là $86{,}0\,\mathrm{dB}$. Không tăng số đo dB theo cùng hệ số với biên độ áp suất.

</details>

### VP16.12.1: Hai ống cùng tạo một tần số

Một ống đàn organ hở hai đầu có tần số cơ bản $220\,\mathrm{Hz}$, ứng với nốt La dưới Đô giữa (A3), khi tốc độ âm là $344\,\mathrm{m/s}$.

(a) Ống dài bao nhiêu?

(b) Họa âm thứ ba của ống này có cùng tần số với âm cơ bản của một ống bịt kín một đầu. Ống bịt kín một đầu dài bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai đầu hở là bụng chuyển vị và nút áp suất. Đầu bịt kín là nút chuyển vị và bụng áp suất. Bỏ qua hiệu chỉnh đầu ống.

**Hướng đi:**

- Ống hở hai đầu chứa nửa bước sóng ở dạng cơ bản, nên dùng $f_1=v/(2L_o)$.
- Ống bịt kín một đầu chứa một phần tư bước sóng ở dạng cơ bản. Tần số ghép ở phần (b) là $3f_1$, không phải $f_1$.

**Lời giải:** (a) Gọi chiều dài ống hở là $L_o$.

$$
L_o=\frac v{2f_1}\approx0{,}782\,\mathrm m.
$$

(b) Tần số họa âm thứ ba là

$$
f_3=3f_1=660\,\mathrm{Hz}.
$$

Gọi chiều dài ống bịt kín một đầu là $L_s$.

$$
L_s=\frac v{4f_3}\approx0{,}130\,\mathrm m.
$$

Hai ống có thể phát cùng tần số dù chiều dài khác nhau vì điều kiện biên và số họa âm đang xét khác nhau.

</details>

### VP16.12.2: Họa âm được phép trong ống bịt kín một đầu

Có hai ống đàn organ, một ống hở hai đầu và một ống bịt kín một đầu. Họa âm nào, nếu có, của ống bịt kín có cùng tần số với họa âm thứ ba của ống hở khi chiều dài ống bịt kín bằng (a) $1/6$, (b) $1/2$ hoặc (c) $1/3$ chiều dài ống hở?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Hai ống chứa cùng môi trường. Gọi chiều dài ống hở là $L_o$, chiều dài ống bịt kín là $L_s$ và đặt $\alpha=L_s/L_o$.

**Hướng đi:**

- Viết tần số mục tiêu của ống hở và tần số họa âm của ống bịt kín.
- Sau khi giải chỉ số $n$, phải kiểm tra $n$ là số nguyên dương lẻ. Có nghiệm đại số chưa đủ để có một họa âm được phép.

**Lời giải:** Điều kiện cùng tần số là

$$
\frac{nv}{4L_s}=\frac{3v}{2L_o}.
$$

Suy ra

$$
n=6\frac{L_s}{L_o}=6\alpha.
$$

(a) Với $\alpha=1/6$, ta có $n=1$. Đó là tần số cơ bản của ống bịt kín.

(b) Với $\alpha=1/2$, ta có $n=3$. Đó là họa âm thứ ba.

(c) Với $\alpha=1/3$, phương trình đòi $n=2$. Ống bịt kín một đầu lý tưởng chỉ có các họa âm $n=1,3,5,\dots$, nên không có họa âm phù hợp.

Sự loại bỏ ở phần (c) xuất phát từ điều kiện một đầu là nút chuyển vị, đầu kia là bụng chuyển vị.

</details>

### VP16.12.3: Dây contrabass kích thích một cột khí

Một dây contrabass dài $0{,}680\,\mathrm m$ có tần số cơ bản $165\,\mathrm{Hz}$.

(a) Tốc độ sóng trên dây bằng bao nhiêu?

(b) Khi dây dao động ở tần số cơ bản, nó làm không khí trong một ống đàn organ bịt kín một đầu gần đó dao động ở tần số cơ bản của ống. Tốc độ âm trong ống là $344\,\mathrm{m/s}$. Ống dài bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tần số kích thích được giữ khi dây truyền dao động sang không khí. Tốc độ sóng trên dây và tốc độ âm trong ống là hai đại lượng khác nhau.

**Hướng đi:**

- Dây cố định hai đầu có bước sóng cơ bản bằng hai lần chiều dài.
- Ống bịt kín một đầu có bước sóng cơ bản bằng bốn lần chiều dài. Dùng tốc độ của không khí ở phần (b).

**Lời giải:** (a) Trên dây,

$$
v_d=2L_df_1\approx224\,\mathrm{m/s}.
$$

(b) Tần số cơ bản của ống bằng $165\,\mathrm{Hz}$. Do đó

$$
L_s=\frac{344\,\mathrm{m/s}}{4(165\,\mathrm{Hz})}.
$$

Kết quả là

$$
L_s\approx0{,}521\,\mathrm m.
$$

Tần số bằng nhau cho phép kích thích cộng hưởng, nhưng bước sóng trong dây và trong không khí không bằng nhau.

</details>

### VP16.12.4: Cộng hưởng giữa khí heli và không khí

Một ống bịt kín một đầu dài $1{,}00\,\mathrm m$ chứa heli ở $20\,{}^\circ\mathrm C$, với tốc độ âm $999\,\mathrm{m/s}$. Khi heli dao động ở họa âm thứ ba, nó làm không khí ở $20\,{}^\circ\mathrm C$ trong một ống hở hai đầu gần đó dao động ở họa âm thứ năm. Tốc độ âm trong không khí là $344\,\mathrm{m/s}$.

Tìm tần số và bước sóng (a) trong heli của ống bịt kín, (b) trong không khí của ống hở. (c) Ống hở dài bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Một tần số chung kích thích hai dạng dao động riêng khác nhau. Giữ phân biệt tốc độ của hai khí và điều kiện biên của hai ống.

**Hướng đi:**

- Ống bịt kín có $f_3=3v_h/(4L_s)$ vì chỉ có các họa âm lẻ.
- Tần số truyền sang không khí giữ nguyên, còn bước sóng đổi theo tốc độ.
- Ống hở ở họa âm thứ năm chứa năm nửa bước sóng, nên dùng $L_o=5\lambda_a/2$.

**Lời giải:** (a) Trong heli,

$$
f=\frac{3v_h}{4L_s}=749{,}25\,\mathrm{Hz}.
$$

Vì vậy

$$
f\approx749\,\mathrm{Hz},
$$

$$
\lambda_h=\frac{v_h}f\approx1{,}33\,\mathrm m.
$$

(b) Trong không khí, tần số vẫn xấp xỉ $749\,\mathrm{Hz}$. Dùng giá trị tần số chưa làm tròn,

$$
\lambda_a=\frac{344\,\mathrm{m/s}}f\approx0{,}459\,\mathrm m.
$$

(c) Chiều dài ống hở là

$$
L_o=\frac52\lambda_a\approx1{,}15\,\mathrm m.
$$

Họa âm thứ ba ở ống bịt kín là dạng được phép thứ hai. Không thay chỉ số họa âm $3$ bằng số thứ tự dạng dao động $2$ trong công thức tần số.

</details>

### VP16.18.1: Âm còi ở phía trước và phía sau xe cứu thương

Còi xe cứu thương phát âm có tần số $2{,}80\times10^3\,\mathrm{Hz}$. Xe chạy với tốc độ $26{,}0\,\mathrm{m/s}$, tương đương $93{,}6\,\mathrm{km/h}$ hay $58{,}2$ dặm mỗi giờ. Không khí đứng yên và tốc độ âm là $340\,\mathrm{m/s}$. Người đứng yên nghe tần số và nhận bước sóng nào nếu ở (a) phía trước hoặc (b) phía sau xe?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Nguồn chuyển động đối với không khí, người nghe đứng yên. Gọi tốc độ xe là $u$ và tần số phát là $f_S$.

**Hướng đi:**

- Nguồn tiến thêm một đoạn trong mỗi chu kỳ phát, nên khoảng cách mặt sóng phía trước giảm còn $(v-u)/f_S$.
- Phía sau, khoảng cách ấy tăng thành $(v+u)/f_S$. Người nghe đứng yên gặp các mặt sóng với tốc độ $v$, nên dùng $f_L=v/\lambda$.

**Lời giải:** (a) Ở phía trước,

$$
\lambda_t=\frac{v-u}{f_S}\approx0{,}112\,\mathrm m,
$$

$$
f_t=\frac v{v-u}f_S.
$$

Suy ra

$$
f_t\approx3{,}03\times10^3\,\mathrm{Hz}.
$$

(b) Ở phía sau,

$$
\lambda_s=\frac{v+u}{f_S}\approx0{,}131\,\mathrm m,
$$

$$
f_s=\frac v{v+u}f_S.
$$

Suy ra

$$
f_s\approx2{,}60\times10^3\,\mathrm{Hz}.
$$

Âm phía trước cao hơn, âm phía sau thấp hơn tần số phát. Tốc độ truyền trong không khí vẫn là $340\,\mathrm{m/s}$ ở cả hai phía.

</details>

### VP16.18.2: Người đi xe đạp nghe kèn túi

Một người đứng yên chơi kèn túi Highland. Một lưỡi gà phát liên tục âm có tần số $440\,\mathrm{Hz}$. Không khí đứng yên và tốc độ âm là $340\,\mathrm{m/s}$.

(a) Bước sóng do kèn tạo ra bằng bao nhiêu?

Tần số và bước sóng mà người đi xe đạp nhận được bằng bao nhiêu khi cô ấy (b) tiến về người chơi kèn với tốc độ $10{,}0\,\mathrm{m/s}$ hoặc (c) đi ra xa với cùng tốc độ ấy?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Nguồn đứng yên đối với không khí. Chỉ người nghe chuyển động, nên khoảng cách giữa các mặt sóng trong không khí không đổi.

**Hướng đi:**

- Tính bước sóng từ tần số nguồn và tốc độ âm trong môi trường.
- Khi người nghe tiến lại, tốc độ gặp mặt sóng là $v+u$. Khi ra xa, tốc độ gặp là $v-u$. Không dùng riêng $v$ chia cho tần số đã dịch để tìm bước sóng trong không khí.

**Lời giải:** (a)

$$
\lambda=\frac v{f_S}\approx0{,}773\,\mathrm m.
$$

(b) Người nghe tiến về nguồn nên

$$
f_+=\frac{v+u}{v}f_S\approx453\,\mathrm{Hz}.
$$

(c) Người nghe đi ra xa nên

$$
f_-=\frac{v-u}{v}f_S\approx427\,\mathrm{Hz}.
$$

Trong cả (b) và (c), bước sóng trong không khí vẫn bằng $0{,}773\,\mathrm m$. Người nghe thay đổi nhịp gặp các mặt sóng, không thay đổi khoảng cách giữa chúng.

</details>

### VP16.18.3: Xe cảnh sát đuổi xe thể thao

Xe cảnh sát chạy về phía đông với tốc độ $40{,}0\,\mathrm{m/s}$, đuổi theo xe thể thao chạy về phía đông với tốc độ $35{,}0\,\mathrm{m/s}$. Còi cảnh sát phát tần số $1{,}20\times10^3\,\mathrm{Hz}$. Không khí đứng yên, tốc độ âm $340\,\mathrm{m/s}$.

(a) Người lái xe thể thao nghe tần số bao nhiêu?

(b) Nếu xe thể thao quay đầu, chạy về phía tây với tốc độ $35{,}0\,\mathrm{m/s}$ về phía xe cảnh sát đang tiến tới, người lái nghe tần số bao nhiêu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cả nguồn và người nghe chuyển động đối với không khí. Âm tới xe thể thao truyền về phía đông trong cả hai tình huống đang xét.

**Hướng đi:**

- Nguồn chuyển động về phía đông làm bước sóng phía trước bằng $(v-u_S)/f_S$, với $u_S=40{,}0\,\mathrm{m/s}$.
- Ở (a), người nghe đi cùng chiều sóng nên tốc độ gặp là $v-u_L$. Ở (b), người nghe đi ngược chiều sóng nên tốc độ gặp là $v+u_L$, với $u_L=35{,}0\,\mathrm{m/s}$.
- Giữ riêng hai vận tốc so với môi trường. Không thay chúng bằng tốc độ khép khoảng cách giữa hai xe.

**Lời giải:** (a)

$$
f_a=\frac{v-u_L}{v-u_S}f_S.
$$

Thay số được

$$
f_a=1{,}22\times10^3\,\mathrm{Hz}.
$$

(b)

$$
f_b=\frac{v+u_L}{v-u_S}f_S.
$$

Thay số được

$$
f_b=1{,}50\times10^3\,\mathrm{Hz}.
$$

Ở phần (b), cả nguồn lẫn người nghe đều làm tăng nhịp gặp các mặt sóng, nên độ tăng tần số lớn hơn phần (a).

</details>

### VP16.18.4: Âm còi phản xạ từ tường

Trong một cảnh phim hành động, ô tô chạy thẳng về một bức tường với tốc độ $25{,}0\,\mathrm{m/s}$. Còi xe phát liên tục âm có tần số $415\,\mathrm{Hz}$.

(a) Nếu tốc độ âm là $340\,\mathrm{m/s}$ và không khí đứng yên, người lái nghe âm phản xạ từ tường có tần số bao nhiêu?

(b) Xe phải chạy với tốc độ nào để tần số âm phản xạ người lái nghe được là $495\,\mathrm{Hz}$?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Tường đứng yên. Xe mang cả nguồn phát và người nhận âm phản xạ. Xét vận tốc xe nhỏ hơn tốc độ âm.

**Hướng đi:**

- Ở lượt tới, tường là người nhận đứng yên, còn còi là nguồn đang tiến lại.
- Tường phản xạ với tần số mà nó nhận. Ở lượt về, tường là nguồn đứng yên, người lái tiến về nguồn ấy.
- Nhân hai hệ số Doppler rồi giải ngược ở phần (b). Một lần Doppler không mô tả đủ đường đi và về.

**Lời giải:** (a) Gọi tốc độ xe là $u$. Tần số tường nhận được là

$$
f_W=\frac v{v-u}f_S.
$$

Người lái nhận âm phản xạ với tần số

$$
\begin{aligned}
f_E&=\frac{v+u}{v}f_W\\
&=\frac{v+u}{v-u}f_S.
\end{aligned}
$$

Với $u=25{,}0\,\mathrm{m/s}$,

$$
f_E\approx481\,\mathrm{Hz}.
$$

(b) Đặt $R=f_E/f_S$. Giải quan hệ

$$
R=\frac{v+u}{v-u}
$$

cho

$$
u=v\frac{R-1}{R+1}.
$$

Dùng $R=495/415$ thu được

$$
u\approx29{,}9\,\mathrm{m/s}.
$$

Tốc độ lớn hơn phần (a) cho tần số phản xạ cao hơn, phù hợp cả hai lượt đều tăng tần số.

</details>
