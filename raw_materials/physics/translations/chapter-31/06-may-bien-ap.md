## 31.6. Máy biến áp

Truyền một công suất lớn bằng dòng nhỏ giúp giảm nhiệt tỏa trên đường dây. Tuy nhiên, cùng công suất với dòng nhỏ đòi hỏi điện áp cao. Làm thế nào nâng điện áp khi truyền đi rồi hạ điện áp gần nơi sử dụng?

Máy biến áp thực hiện sự chuyển đổi đó với điện xoay chiều. Điện áp truyền tải có thể đạt cỡ 500 kV trong các hệ thống đang xét. Điện áp ở nơi phát và nơi tiêu dùng cần phù hợp với thiết bị, cách điện và điều kiện sử dụng.

Các mức điện áp gia dụng minh họa là 120 V ở Bắc và Trung Mỹ, cùng 220–240 V ở nhiều hệ thống khác. Đây đều là giá trị hiệu dụng. Máy biến áp tạo các mức điện áp khác nhau trong quá trình phân phối.

### Cấu tạo và nguyên lý

Máy gồm hai cuộn dây cách điện với nhau, cùng quấn trên một lõi có độ từ thẩm lớn, thường là lõi sắt. Lõi giữ phần lớn đường sức bên trong nó, giúp từ thông do một cuộn tạo ra đi qua cuộn còn lại và làm hỗ cảm lớn.

Cuộn nhận năng lượng từ nguồn gọi là **cuộn sơ cấp**. Cuộn cấp năng lượng cho tải gọi là **cuộn thứ cấp**.

![Ký hiệu: Máy biến áp có lõi sắt trên sơ đồ mạch.](../img/young-31/ky-hieu-may-bien-ap.png)

![Hình 31.21: Máy biến áp tăng áp lý tưởng với sơ cấp nối nguồn xoay chiều và thứ cấp nối tải điện trở.](../img/young-31/hinh-31-21.png)

Dòng xoay chiều sơ cấp tạo từ thông biến thiên trong lõi. Theo Faraday, từ thông biến thiên gây suất điện động ở cả hai cuộn. Suất điện động thứ cấp tạo dòng qua tải và truyền năng lượng cho tải.

Các dòng và suất điện động có cùng tần số với nguồn. Máy biến áp đổi mức điện áp, không đổi tần số trong mô hình này.

### Tỉ số điện áp và số vòng

Xét máy lý tưởng với điện trở cuộn bằng không và không có từ thông rò. Gọi $\Phi_B$ là từ thông qua mỗi vòng, giống nhau ở cả sơ cấp và thứ cấp. Số vòng tương ứng là $N_1$ và $N_2$.

Hai suất điện động, với chiều quấn và quy ước dấu thống nhất:

$$
\begin{aligned}
\mathcal E_1&=-N_1\frac{d\Phi_B}{dt},\\
\mathcal E_2&=-N_2\frac{d\Phi_B}{dt}.\tag{31.33}
\end{aligned}
$$

Suất điện động trên mỗi vòng bằng nhau. Tại những thời điểm $\mathcal E_1\ne0$:

$$
\frac{\mathcal E_2}{\mathcal E_1}=\frac{N_2}{N_1}.\tag{31.34}
$$

Quan hệ tương ứng giữa hai suất điện động vẫn đúng khi cả hai cùng bằng không. Vì hai dạng sóng chỉ khác hệ số số vòng, tỉ số biên độ và tỉ số hiệu dụng đều bằng tỉ số số vòng.

Khi bỏ qua sụt áp điện trở cuộn, độ lớn điện áp đầu cuộn có quan hệ

$$
\frac{V_2}{V_1}=\frac{N_2}{N_1}.\tag{31.35}
$$

$V_1$, $V_2$ phải cùng là biên độ hoặc cùng là giá trị hiệu dụng. Dấu của điện áp tức thời giữa các đầu còn phụ thuộc chiều quấn và cách chọn đầu đo.

Nếu $N_2>N_1$, thứ cấp có điện áp lớn hơn sơ cấp, gọi là máy tăng áp. Nếu $N_2<N_1$, máy hạ áp.

Tại nơi phát, máy tăng áp đưa điện năng vào đường dây truyền tải. Gần người tiêu dùng, máy hạ áp đưa điện áp về mức phù hợp.

![Hình 31.22: Máy hạ áp trên cột điện đưa điện áp đường dây về mức phân phối cho các nhà và cơ sở xung quanh.](../img/young-31/hinh-31-22.png)

Thiết bị điện tử còn có thể cần điện áp thấp hơn mức ổ cắm. Một bộ đổi nguồn kiểu máy biến áp hạ điện áp xuống khoảng 3–12 V rồi dùng diode chỉnh lưu để cung cấp dòng một chiều.

![Hình 31.23: Bộ đổi nguồn dùng máy biến áp hạ điện áp và mạch chỉnh lưu để tạo nguồn một chiều điện áp thấp.](../img/young-31/hinh-31-23.png)

::: info Ứng dụng: Điện áp xoay chiều và tác động lên cơ thể
Điện áp cao có thể gây dòng nguy hiểm qua cơ thể, dù là xoay chiều hay một chiều. Dòng xoay chiều ở tần số lưới có thể gây co cơ không tự chủ và làm người bị điện giật khó buông vật đang tiếp xúc.

Dòng một chiều cũng có thể gây co cơ và tổn thương. Không thể coi việc phản xạ cơ có thể làm cơ thể rời nguồn là một cơ chế bảo vệ. Hạ điện áp bằng máy biến áp làm giảm mức điện áp tiếp xúc, nhưng mức độ nguy hiểm còn phụ thuộc dòng qua cơ thể, đường đi và thời gian tiếp xúc.

![Ứng dụng 31.6: Biển cảnh báo điện áp cao tại khu vực thiết bị điện.](../img/young-31/ung-dung-31-dien-ap-cao.png)

Tác động co cơ do điện được trình bày trong [tài liệu an toàn điện của NIOSH](https://stacks.cdc.gov/view/cdc/158172/cdc_158172_DS1.pdf).
:::

### Năng lượng và dòng điện

Với tải thuần trở $R$, dòng thứ cấp là $I_2=V_2/R$. Trong máy lý tưởng, không có năng lượng hao hụt. Bỏ qua dòng từ hóa không tải, công suất nhận ở sơ cấp bằng công suất cấp cho thứ cấp:

$$
V_1I_1=V_2I_2.\tag{31.36}
$$

Nếu dùng hiệu dụng, hai vế là công suất trung bình của mô hình tải thuần trở. Nếu dùng biên độ, mỗi công suất trung bình có thêm hệ số $1/2$, và hai hệ số triệt tiêu khi lập phương trình.

Kết hợp với tỉ số điện áp:

$$
\frac{I_2}{I_1}=\frac{N_1}{N_2}.
$$

Tăng áp đi kèm giảm dòng, còn hạ áp đi kèm tăng dòng. Máy biến áp không tạo thêm năng lượng.

### Điện trở tải nhìn từ sơ cấp

Đặt $n=N_2/N_1$ để viết ngắn các bước. Khi đó $V_2=nV_1$ và $I_1=nI_2$. Vì $I_2=V_2/R$:

$$
\begin{aligned}
I_1&=n\frac{nV_1}{R}\\
&=\frac{n^2V_1}{R}.
\end{aligned}
$$

Suy ra

$$
\begin{aligned}
\frac{V_1}{I_1}&=\frac R{n^2},\\
n&=\frac{N_2}{N_1}.\tag{31.37}
\end{aligned}
$$

Nguồn sơ cấp đáp ứng như đang nối trực tiếp với điện trở tải chia cho bình phương tỉ số số vòng. Vì vậy máy biến áp còn chuyển đổi điện trở, hay tổng quát hơn là trở kháng mà nguồn nhìn thấy.

Điều này được dùng để phối hợp trở kháng giữa nguồn và tải, chẳng hạn giữa bộ khuếch đại âm thanh với loa. Với nguồn có điện trở trong cố định và tải thuần trở thay đổi, công suất tải lớn nhất khi điện trở tải nhìn từ nguồn bằng điện trở trong.

Kết luận cực đại trên nói về công suất truyền cho tải. Nó không có nghĩa điều kiện ấy đồng thời cho hiệu suất truyền năng lượng lớn nhất.

### Tổn hao của máy thực

Máy thực có điện trở cuộn dây, gây nhiệt theo $i^2R$. Lõi còn có tổn hao từ trễ. Dùng sắt từ mềm với vòng từ trễ hẹp giúp giảm phần tổn hao này.

Từ thông biến thiên cũng gây dòng Fu-cô trong lõi dẫn điện. Nhìn một tiết diện vuông góc từ thông, có thể hình dung những vòng dẫn lồng nhau. Suất điện động cảm ứng làm dòng chạy trong các vòng đó, gây nhiệt và tạo từ thông chống lại sự biến thiên.

![Hình 31.24: Dòng Fu-cô lớn trong lõi đặc và các đường dòng nhỏ hơn khi lõi được ghép từ những lá cách điện với nhau.](../img/young-31/hinh-31-24.png)

Lõi ghép lá gồm nhiều tấm mỏng. Lớp oxide hoặc sơn cách điện trên mặt lá hạn chế dòng qua các lá, nên dòng Fu-cô chủ yếu chạy trong từng lá. Đường vòng nhỏ hơn có suất điện động cảm ứng nhỏ hơn, giúp giảm dòng và nhiệt.

Từ trường xoay chiều tác dụng lực lên các lá mang dòng, làm chúng rung. Sự rung này góp phần tạo tiếng ù của máy biến áp đang hoạt động, tương tự tiếng ù ở chấn lưu từ của đèn huỳnh quang.

Lõi sắt từ mềm và cấu trúc ghép lá giúp máy có hiệu suất cao. Các mức hiệu suất được xét trong mô hình ứng dụng ở đây thường trên 90%, còn thiết bị công suất lớn có thể đạt khoảng 99%.

### Ứng dụng: Khi truyền tải một chiều có lợi

![Ứng dụng truyền tải: Nguồn điện mặt trời ở vùng sa mạc là một ví dụ để xét việc truyền điện đi xa bằng đường dây điện áp cao.](../img/young-31/ung-dung-31-truyen-tai-mot-chieu.png)

Trong dây truyền dòng xoay chiều, từ trường biến thiên gây sự phân bố dòng thiên về gần bề mặt. Hiệu ứng bề mặt làm giảm tiết diện dẫn hữu hiệu và tăng điện trở hiệu dụng, khiến tổn hao tăng.

Vì lý do này cùng những đặc điểm khác của hệ thống, truyền tải một chiều điện áp cao có thể có lợi hơn xoay chiều ở những tuyến dài. Một tình huống để xét là đưa điện mặt trời từ Bắc Phi đến châu Âu qua cáp dưới Địa Trung Hải.

Lợi thế đổi điện áp bằng máy biến áp không có nghĩa xoay chiều luôn tối ưu cho mọi tuyến truyền tải. Cần xét cả đường dây và các thiết bị chuyển đổi của toàn hệ thống.

::: example Ví dụ 31.9: Máy pha cà phê và máy biến áp
Một máy pha cà phê công suất 960 W được thiết kế cho đường điện 240 V. Muốn dùng nó trên đường điện 120 V, tìm (a) loại máy biến áp và tỉ số vòng cần thiết, (b) dòng lấy từ đường 120 V, (c) điện trở máy pha. Các điện áp đều là hiệu dụng.

**Nhận dạng và chuẩn bị:** Máy pha cần giữ đúng 240 V. Xem tải thuần trở và máy biến áp lý tưởng, nên công suất lấy từ sơ cấp bằng công suất cấp cho máy pha.

**Lời giải:**

(a) Cần máy tăng áp:

$$
\begin{aligned}
\frac{N_2}{N_1}&=\frac{V_2}{V_1}\\
&=\frac{240}{120}=2.
\end{aligned}
$$

Thứ cấp nối máy pha cần số vòng gấp đôi sơ cấp nối đường 120 V.

(b) Dòng sơ cấp:

$$
\begin{aligned}
I_1&=\frac{P_{\mathrm{av}}}{V_1}\\
&=\frac{960\,\mathrm W}{120\,\mathrm V}\\
&=8{,}0\,\mathrm A.
\end{aligned}
$$

Dòng thứ cấp:

$$
I_2=\frac{960\,\mathrm W}{240\,\mathrm V}=4{,}0\,\mathrm A.
$$

(c) Điện trở nhìn từ sơ cấp:

$$
\frac{V_1}{I_1}=\frac{120\,\mathrm V}{8{,}0\,\mathrm A}=15\,\Omega.
$$

Từ quan hệ chuyển đổi điện trở:

$$
\begin{aligned}
R&=\left(\frac{N_2}{N_1}\right)^2\frac{V_1}{I_1}\\
&=2^2(15\,\Omega)\\
&=60\,\Omega.
\end{aligned}
$$

**Đánh giá:** Ở thứ cấp, $240\,\mathrm V/(60\,\Omega)=4{,}0\,\mathrm A$, phù hợp dòng đã tìm. Công suất tải cũng bằng bình phương điện áp thứ cấp chia điện trở.

Tăng điện áp gấp đôi đã giảm dòng xuống một nửa. Công suất vẫn là 960 W vì máy lý tưởng không có tổn hao.
:::

### Câu hỏi tự kiểm 31.6

Bốn máy đều có 1000 vòng sơ cấp. Xếp theo số vòng thứ cấp từ lớn đến nhỏ:

(i) Đổi 120 V xoay chiều thành 6,0 V. (ii) Đổi 120 V thành 240 V. (iii) Đổi 240 V thành 6,0 V. (iv) Đổi 240 V thành 120 V.

<details><summary>Xem đáp án và giải thích</summary>

Dùng $N_2=N_1V_2/V_1$. Số vòng tương ứng là

$$
\begin{aligned}
N_{2,\mathrm{(i)}}&=50,\\
N_{2,\mathrm{(ii)}}&=2000,\\
N_{2,\mathrm{(iii)}}&=25,\\
N_{2,\mathrm{(iv)}}&=500.
\end{aligned}
$$

Thứ tự là (ii), (iv), (i), (iii). Chỉ (ii) là tăng áp với số vòng thứ cấp lớn hơn sơ cấp. Ba trường hợp còn lại đều là hạ áp.

</details>
