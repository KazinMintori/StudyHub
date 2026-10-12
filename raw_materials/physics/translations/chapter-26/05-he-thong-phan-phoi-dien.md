<!-- Source: Section 26.5, printed pages 863–866, PDF pages 883–886. Figures 26.24–26.26 and Example 26.14 are included. The Chapter 26 summary begins on printed page 867 and is outside this section. -->

## 26.5. Hệ thống phân phối điện

Điện năng phải được đưa từ nguồn đến nhiều bóng đèn, động cơ và thiết bị mà mỗi thiết bị vẫn hoạt động độc lập. Trong ô tô, nguồn một chiều lấy từ ắc quy và máy phát điện. Nhà ở, cửa hàng và nhà máy thường dùng dòng xoay chiều vì máy biến áp có thể tăng hoặc hạ điện áp thuận tiện. Những nguyên tắc mạch điện cơ bản trong mục này áp dụng cho cả hai dạng nguồn. Mạch xoay chiều sẽ được xét kỹ hơn ở Chương 31.

Các thiết bị trong một căn nhà hoặc ô tô được mắc song song với đường dây cấp điện. Nhờ vậy, tắt một thiết bị không làm các thiết bị khác mất điện. Trong mô hình đường dây gia dụng được xét ở đây, một dây là **dây pha** (hot), dây còn lại là **dây trung tính** (neutral). Tại bảng đầu vào, dây trung tính được nối với đất theo sơ đồ hệ thống đang mô tả. Điểm nối đất có thể là điện cực cắm vào đất hoặc, trong một số hệ thống, đường ống nước gia dụng. Hệ thống hiện đại trong mô hình này còn có dây bảo vệ nối đất, nhưng hình dưới lược bỏ dây ấy.

![Hình 26.24: Sơ đồ hệ thống điện gia dụng gồm công tơ, cầu chì chính và hai mạch nhánh mắc song song](../img/young-26/hinh-26-24.png)

**Hình 26.24:** Sơ đồ minh họa hai mạch nhánh sau công tơ và cầu chì chính. Mỗi nhánh có các ổ cắm, cầu chì, công tắc và đèn. Hệ thống thực tế có thể có từ bốn đến ba mươi mạch nhánh. Dây bảo vệ nối đất không được vẽ và bình thường không mang dòng.

Trong các ví dụ hệ thống dân dụng ở Bắc Mỹ, điện áp danh định là $120\,\mathrm V$. Nhiều hệ thống ở châu Âu được trình bày với điện áp $240\,\mathrm V$. Đây là các mô hình điện áp cụ thể, không phải một mức dùng chung cho mọi nơi. Với dòng xoay chiều hình sin, các trị số này là điện áp hiệu dụng, bằng điện áp cực đại chia cho $\sqrt{2}$.

Công suất điện đầu vào của thiết bị thỏa mãn quan hệ $P=VI$ (Phương trình 25.17), nên dòng điện được tính bằng

$$
I=\frac{P}{V}.
$$

Một bóng đèn $100\,\mathrm W$ nối vào nguồn $120\,\mathrm V$ lấy dòng khoảng $0{,}83\,\mathrm A$. Nếu xem bóng đèn ở nhiệt độ hoạt động như một điện trở, từ $P=VI=I^2R=V^2/R$ (Phương trình 25.18), điện trở của nó là

$$
R=\frac{V}{I}=\frac{V^2}{P}=144\,\Omega.
$$

Một bàn nướng bánh công suất $1500\,\mathrm W$ lấy dòng $12{,}5\,\mathrm A$ ở $120\,\mathrm V$. Điện trở của nó ở nhiệt độ hoạt động là $9{,}6\,\Omega$. Điện trở suất kim loại tăng theo nhiệt độ, vì thế điện trở của dây tóc và dây nung khi còn lạnh nhỏ hơn nhiều so với lúc đang hoạt động. Một bóng đèn $100\,\mathrm W$ có điện trở hoạt động khoảng $144\,\Omega$, nhưng phép đo bằng ôm kế với dòng nhỏ có thể cho khoảng $10\,\Omega$. Khi bật đèn, điện trở nhỏ lúc nguội tạo ra dòng khởi động lớn. Một bóng đèn sắp hỏng vì thế có thể đứt dây tóc ngay khi vừa bật.

### Quá tải và ngắn mạch

Khi dòng chạy qua dây, một phần công suất biến thành nhiệt theo $P=I^2R$. Dây nóng lên quá mức có thể làm hỏng lớp cách điện, nóng chảy dây hoặc gây cháy. Trong mô hình hệ thống được mô tả ở mục này, các mạch chiếu sáng và ổ cắm thường dùng dây đồng cỡ 12 gauge, đường kính $2{,}05\,\mathrm{mm}$, với dòng tối đa an toàn được nêu là $20\,\mathrm A$. Dây gauge có số nhỏ hơn thì đường kính lớn hơn.

| Vị trí trong mô hình nguồn | Cỡ dây được nêu | Đường kính |
| --- | ---: | ---: |
| Chiếu sáng và ổ cắm | 12 gauge | $2{,}05\,\mathrm{mm}$ |
| Thiết bị cần dòng lớn, như máy sấy quần áo | 8 hoặc 6 gauge | $3{,}26$ hoặc $4{,}11\,\mathrm{mm}$ |
| Đường cấp điện chính vào nhà | 2 gauge hoặc lớn hơn | Từ $6{,}54\,\mathrm{mm}$ trở lên |

Các cỡ dây và dòng điện trong bảng là dữ kiện của mô hình ví dụ ở đây. Kích thước cần thiết trong một công trình còn phụ thuộc điều kiện lắp đặt và quy định tại nơi sử dụng, nên bảng không phải hướng dẫn chọn dây cho công trình thực tế.

Cầu chì và bộ ngắt mạch bảo vệ dây khi dòng vượt mức quy định. Cầu chì có một đoạn hợp kim chì–thiếc nóng chảy ở nhiệt độ thấp. Khi dòng quá lớn, đoạn kim loại đứt và làm hở mạch. Bộ ngắt mạch dùng cơ cấu điện từ hoặc thanh lưỡng kim để ngắt mạch khi dòng vượt ngưỡng. Bộ ngắt có thể được đóng lại sau khi đã ngắt, còn cầu chì nóng chảy cần được thay.

![Hình 26.25: Cầu chì nóng chảy khi quá dòng và bộ ngắt mạch ngắt đường điện](../img/young-26/hinh-26-25.png)

**Hình 26.25:** (a) Dây hợp kim chì–thiếc bên trong cầu chì nóng chảy khi dòng vượt định mức. (b) Bộ ngắt mạch chuyển sang trạng thái ngắt khi dòng vượt giới hạn cho phép.

::: warning Quá dòng và cầu chì
Thay cầu chì hoặc bộ ngắt bằng loại có định mức cao hơn có thể khiến dây dẫn nóng quá mức trước khi mạch ngắt, làm tăng nguy cơ cháy. Ví dụ này cho thấy thiết bị bảo vệ phải tương thích với dây dẫn và tải của mạch.
:::

**Ngắn mạch** xảy ra khi dây pha tiếp xúc với dây trung tính, tạo đường dẫn có điện trở rất nhỏ. Dòng lớn có thể làm nóng chảy dây và đốt cháy lớp cách điện nếu cầu chì hoặc bộ ngắt không ngắt mạch. Một dây bị đứt tạo thành **mạch hở** cũng có thể nguy hiểm nếu tiếp điểm chập chờn gây tia lửa.

Trong sơ đồ hệ thống được xét, cầu chì hoặc bộ ngắt đặt trên dây pha. Nếu thiết bị ngắt chỉ đặt ở dây trung tính rồi ngắt do sự cố, dây pha vẫn có thể còn điện thế cao so với đất. Khi ấy, chạm đồng thời vào phần dẫn điện và một vật nối đất có thể gây điện giật. Công tắc đèn trong cùng mô hình cũng được đặt ở dây pha vì cùng lý do.

Dây bảo vệ nối đất là dây dẫn thứ ba, thường nối với vỏ kim loại của thiết bị và với điểm nối đất của hệ thống. Dây này đi tới chân tròn hoặc chân chữ U của phích ba chấu. Ở trạng thái hoạt động bình thường, dây không mang dòng. Nếu dây pha chạm vào vỏ kim loại, dây bảo vệ tạo đường cho dòng sự cố đi qua, giúp cầu chì hoặc bộ ngắt ngắt mạch. Không có đường bảo vệ ấy, vỏ kim loại có thể bị nâng lên điện thế nguy hiểm, khoảng $120\,\mathrm V$ so với đất trong mô hình này.

![Hình 26.26: Đường dòng sự cố khi dụng cụ điện dùng phích hai chấu và ba chấu](../img/young-26/hinh-26-26.png)

**Hình 26.26:** (a) Khi dụng cụ có lỗi cách điện dùng phích hai chấu, vỏ kim loại có thể trở nên nguy hiểm và người chạm vào có thể thành đường dẫn dòng. (b) Với dây bảo vệ của phích ba chấu, dòng sự cố có đường trở về đất qua dây bảo vệ, nhờ đó giảm nguy cơ dòng đi qua cơ thể. Nếu dòng sự cố đủ lớn, cầu chì hoặc bộ ngắt sẽ ngắt mạch.

Ở nơi có nguy cơ tiếp xúc với nước, mô hình nguồn nêu thêm **bộ ngắt mạch khi rò điện** (GFI hoặc GFCI). Thiết bị này so sánh dòng trên dây pha và dây trung tính. Trong hoạt động bình thường, hai dòng bằng nhau. Nếu độ lệch vượt một ngưỡng nhỏ, thường khoảng $5\,\mathrm{mA}$ trong ví dụ, thiết bị ngắt mạch. Cơ chế này bổ sung cho đường dây bảo vệ nối đất.

### Hệ thống điện gia dụng và ô tô

Trong mô hình ba dây được mô tả, công ty điện lực cung cấp một dây trung tính và hai dây pha. Mỗi dây pha có điện áp hiệu dụng $120\,\mathrm V$ so với dây trung tính, nhưng hai dây pha ngược pha nhau. Vì vậy, điện áp giữa hai dây pha là $240\,\mathrm V$. Thiết bị dùng $120\,\mathrm V$ được mắc giữa dây trung tính và một dây pha. Thiết bị công suất lớn cần $240\,\mathrm V$, chẳng hạn bếp điện và máy sấy quần áo trong ví dụ, được nối giữa hai dây pha.

Ô tô dùng hệ thống một chiều có điện áp khoảng $13\,\mathrm V$. Ắc quy cấp điện khi động cơ chưa chạy, còn máy phát nạp lại ắc quy khi động cơ hoạt động. Thân và khung xe làm đường hồi dòng chung của mạch, nên mô hình này không cần một dây bảo vệ riêng như mạch dân dụng. Cầu chì hoặc bộ ngắt vẫn có vai trò bảo vệ quá dòng. Ở cùng công suất, điện áp thấp đòi hỏi dòng lớn hơn. Chẳng hạn, một đèn pha $100\,\mathrm W$ ở $13\,\mathrm V$ lấy dòng khoảng $8\,\mathrm A$.

Điện lực được mua dưới dạng năng lượng, dù thiết bị thường được ghi công suất. Năng lượng tiêu thụ bằng công suất trung bình nhân với thời gian. Đơn vị kilowatt-giờ được đổi sang joule như sau:

$$
\begin{aligned}
1\,\mathrm{kW\cdot h}
&=(10^3\,\mathrm W)(3600\,\mathrm s)\\
&=3{,}6\times10^6\,\mathrm J.
\end{aligned}
$$

Một bàn nướng bánh $1500\,\mathrm W$ hoạt động liên tục một giờ tiêu thụ $1{,}5\,\mathrm{kW\cdot h}$. Nếu lấy đơn giá minh họa $0{,}10$ đô la cho mỗi kilowatt-giờ, chi phí là $0{,}15$ đô la. Khoảng giá $0{,}08$ đến $0{,}27$ đô la cho mỗi kilowatt-giờ được nêu như dữ kiện theo bối cảnh ấn bản, không phải giá hiện hành. Một số thiết bị nấu ăn tự đóng ngắt để giữ nhiệt độ, nên công suất trung bình trong thời gian sử dụng có thể thấp hơn công suất ghi trên nhãn.

## Ví dụ 26.14. Các thiết bị trong cùng một mạch bếp

Một máy nướng bánh mì $1800\,\mathrm W$, một chảo điện $1{,}3\,\mathrm{kW}$ và một đèn $100\,\mathrm W$ được cắm vào cùng mạch $120\,\mathrm V$ có bộ ngắt định mức $20\,\mathrm A$. (a) Mỗi thiết bị lấy dòng bao nhiêu và có điện trở bao nhiêu ở điều kiện hoạt động? (b) Tổ hợp này có làm bộ ngắt mạch tác động không?

**Nhận diện:** Các thiết bị mắc song song nên mỗi thiết bị đều có hiệu điện thế $120\,\mathrm V$. Dùng $I=P/V$ để tìm dòng và $R=V^2/P$ để tìm điện trở.

**Thực hiện:** Gọi chỉ số 1, 2 và 3 lần lượt ứng với máy nướng, chảo điện và đèn.

$$
\begin{aligned}
I_1&=\frac{1800\,\mathrm W}{120\,\mathrm V}=15\,\mathrm A,\\
R_1&=\frac{(120\,\mathrm V)^2}{1800\,\mathrm W}=8\,\Omega,\\
I_2&=\frac{1300\,\mathrm W}{120\,\mathrm V}\approx11\,\mathrm A,\\
R_2&=\frac{(120\,\mathrm V)^2}{1300\,\mathrm W}\approx11\,\Omega,\\
I_3&=\frac{100\,\mathrm W}{120\,\mathrm V}\approx0{,}83\,\mathrm A,\\
R_3&=\frac{(120\,\mathrm V)^2}{100\,\mathrm W}=144\,\Omega.
\end{aligned}
$$

Tổng dòng qua dây cấp là tổng dòng của ba nhánh:

$$
\begin{aligned}
I_{\mathrm{tổng}}
&=I_1+I_2+I_3\\
&=15+10{,}83+0{,}83\\
&\approx26{,}7\,\mathrm A.
\end{aligned}
$$

Vì tổng dòng vượt mức $20\,\mathrm A$ của mạch, bộ ngắt sẽ tác động. Có thể kiểm tra bằng công suất tổng: $P_{\mathrm{tổng}}=1800+1300+100=3200\,\mathrm W$, do đó $I_{\mathrm{tổng}}=P_{\mathrm{tổng}}/120\,\mathrm V\approx26{,}7\,\mathrm A$. Một phép kiểm tra khác dùng điện trở tương đương của ba tải mắc song song:

$$
\begin{aligned}
\frac{1}{R_{\mathrm{tđ}}}
&=\frac{1}{8\,\Omega}+\frac{1}{11\,\Omega}+\frac{1}{144\,\Omega},\\
I_{\mathrm{tổng}}&=\frac{120\,\mathrm V}{R_{\mathrm{tđ}}}\approx26{,}7\,\mathrm A.
\end{aligned}
$$

Với cùng điện áp, nhánh có điện trở nhỏ nhất lấy dòng lớn nhất và nhận công suất lớn hơn.

::: exercise Kiểm tra hiểu mục 26.5
Để bộ ngắt mạch của Ví dụ 26.14 không tác động, một người thay nó bằng bộ ngắt định mức $40\,\mathrm A$. Đây có phải cách xử lý hợp lý không? Giải thích dựa trên công suất tỏa nhiệt trong dây dẫn.
:::

::: solution Lời giải
Không. Mạch và dây được mô tả có giới hạn $20\,\mathrm A$. Cho dòng đến $40\,\mathrm A$ chạy qua dây có thể làm dây nóng quá mức. Nếu tạm xem điện trở dây không đổi, công suất nhiệt ở $40\,\mathrm A$ gấp

$$
\left(\frac{40}{20}\right)^2=4
$$

lần công suất ở $20\,\mathrm A$. Khi dây nóng lên, điện trở còn tăng và mức phát nhiệt có thể lớn hơn ước tính này. Bộ ngắt định mức cao hơn vì thế làm mất tác dụng bảo vệ mà dây cần.
:::
