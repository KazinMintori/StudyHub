<!-- Source: Section27.8, printed902–904/PDF922–924. Figures27.39–27.40, Example27.11, equation27.29. -->

## 27.8. Động cơ điện một chiều

Làm thế nào biến điện năng thành chuyển động quay liên tục? Trong động cơ điện, từ trường tác dụng mômen lên dây dẫn mang dòng và điện năng được chuyển thành cơ năng. Ta xét động cơ một chiều đơn giản ở Hình 27.39.

![Hình 27.39: Ba vị trí liên tiếp của vòng dây trong động cơ một chiều](../img/young-27/hinh-27-39.png)

Hai phần của vòng dây được tô đỏ và xanh để theo dõi chuyển động. Hai phiến cổ góp cách điện với nhau, nối với hai đầu vòng dây và tiếp xúc với các chổi điện.

### Vì sao cổ góp làm động cơ tiếp tục quay?

Phần chuyển động gọi là **rôto**, ở đây là một vòng dây có hai đầu hở và có thể quay quanh trục. Hai đầu dây gắn với hai phiến dẫn hình cung tạo thành **cổ góp**. Các **chổi điện** nối cổ góp với mạch ngoài có nguồn điện.

Ở Hình 27.39a, dòng đi vào phía đỏ của vòng và đi ra phía xanh. Vòng dây có mômen từ $\vec\mu$ và nằm giữa hai cực của nam châm. Từ trường tác dụng mômen:

$$
\vec\tau=\vec\mu\times\vec B.
$$

Với vị trí đang vẽ, mômen làm rôto quay ngược chiều kim đồng hồ, theo chiều đưa mômen từ về cùng hướng với từ trường.

Sau khi quay $90^\circ$, rôto ở Hình 27.39b. Nếu dòng trong vòng giữ nguyên chiều, đây sẽ là vị trí cân bằng và vòng chỉ dao động quanh vị trí ấy. Cổ góp làm thay đổi tình huống. Trong mô hình đang vẽ, mỗi chổi cùng tiếp xúc hai phiến nên dòng đi vòng qua rôto. Hiệu điện thế giữa hai phiến bằng không, dòng rôto bằng không và mômen từ bằng không tại thời điểm đó.

Nhờ quán tính, rôto vẫn tiếp tục quay. Khi tiếp xúc được thiết lập như Hình 27.39c, dòng đi vào phía xanh và đi ra phía đỏ. Chiều dòng so với vòng dây đã đảo, đồng thời vòng cũng đã quay $180^\circ$. Vì vậy, hướng mômen từ so với từ trường lại giống vị trí ban đầu, và mômen tiếp tục đẩy rôto quay theo cùng chiều.

Cổ góp đảo chiều dòng qua vòng sau mỗi nửa vòng quay. Khi động cơ đạt tốc độ ổn định, mômen từ trung bình cân bằng mômen cản do không khí, ma sát ổ trục và ma sát giữa chổi điện với cổ góp.

Động cơ thực có nhiều vòng dây để tăng mômen từ và kéo tải lớn hơn. Tăng từ trường cũng tăng mômen, nên nhiều thiết kế dùng nam châm điện. Với một vòng đơn, mômen tăng giảm theo góc quay. Dùng nhiều cuộn độc lập đặt ở các góc khác nhau giúp mômen đều hơn.

![Hình 27.40: Động cơ có nhiều cuộn dây để tạo mômen gần như không đổi](../img/young-27/hinh-27-40.png)

Trong thiết kế này, các cuộn dây tương tác với nam châm vĩnh cửu trên rôto. Vị trí phần đứng yên và phần quay đảo lại so với mô hình vòng dây quay ở Hình 27.39. Những động cơ nhiều cuộn như vậy được dùng trong thiết bị bay, ô tô điện và nhiều hệ thống khác.

### Công suất và suất phản điện động

Động cơ cần điện năng đầu vào để thực hiện công cơ học. Với hiệu điện thế hai cực $V_{ab}$ và dòng $I$, công suất vào là $P_{\mathrm{in}}=V_{ab}I$. Ngay cả khi điện trở cuộn dây rất nhỏ, động cơ đang chuyển hóa công suất vẫn phải có hiệu điện thế giữa hai đầu.

Khi dây rôto chuyển động trong từ trường, lực từ gây ra suất điện động cảm ứng. Suất điện động này chống lại chiều dòng được nguồn ngoài duy trì, nên gọi là **suất phản điện động**. Cơ chế cảm ứng do chuyển động sẽ được xét kỹ ở Chương 29.

Trong động cơ kích từ nối tiếp, cuộn rôto nối tiếp với nam châm điện tạo từ trường. Trong động cơ kích từ song song, hai phần mắc song song. Xét mô hình nối tiếp có điện trở trong tổng $r$. Điện áp đặt vào phải cung cấp cả suất phản điện động $\mathcal E$ lẫn sụt áp trên điện trở:

$$
V_{ab}=\mathcal E+Ir.
\tag{27.29}
$$

Suất phản điện động phụ thuộc tốc độ quay. Với từ trường và cấu hình không đổi, nó tỉ lệ tốc độ rôto. Nhân phương trình điện áp với dòng cho cân bằng công suất:

$$
\begin{aligned}
V_{ab}I &= \mathcal EI+I^2r, \\
P_{\mathrm{in}} &= P_{\mathrm{mech}}+P_r.
\end{aligned}
$$

Trong mô hình bỏ qua các tổn hao khác, $\mathcal EI$ là công suất cơ phát triển, còn $I^2r$ là công suất nhiệt bên trong động cơ.

### Ví dụ 27.11: Động cơ một chiều kích từ nối tiếp

Cuộn rôto và cuộn kích từ mắc nối tiếp có điện trở tổng $2{,}00\,\Omega$. Khi chạy đầy tải trên nguồn $120\,\mathrm V$, động cơ lấy dòng $4{,}00\,\mathrm A$. Tìm (a) suất phản điện động, (b) công suất cấp vào, (c) công suất nhiệt, (d) công suất cơ phát triển, (e) hiệu suất. (f) Điều gì xảy ra nếu máy bị kẹt và rôto dừng đột ngột?

#### Nhận diện và bố trí

Dùng phương trình điện áp động cơ để tìm $\mathcal E$. Công suất vào bằng $V_{ab}I$, nhiệt bằng $I^2r$. Hiệu giữa hai công suất là công suất cơ nếu bỏ qua tổn hao khác. Hiệu suất là tỉ số công suất cơ và công suất điện vào.

#### Thực hiện

(a) Suất phản điện động:

$$
\mathcal E = V_{ab}-Ir = 120-(4{,}00)(2{,}00) = 112\,\mathrm V.
$$

(b) Công suất cấp vào:

$$
P_{\mathrm{in}} = V_{ab}I = (120)(4{,}00) = 480\,\mathrm W.
$$

(c) Công suất nhiệt:

$$
P_r = I^2r = (4{,}00)^2(2{,}00) = 32\,\mathrm W.
$$

(d) Bỏ qua các tổn hao khác:

$$
P_{\mathrm{mech}} = 480-32 = 448\,\mathrm W.
$$

(e) Hiệu suất:

$$
\begin{aligned}
\eta &= \frac{P_{\mathrm{mech}}}{P_{\mathrm{in}}} \\
&= 448/480 \\
&\approx 0{,}93=93\%.
\end{aligned}
$$

(f) Khi rôto dừng, suất phản điện động bằng không trong mô hình. Dòng và công suất nhiệt trở thành:

$$
\begin{aligned}
I_{\mathrm{stall}} &= V_{ab}/r \\
&= 120/2{,}00 \\
&= 60\,\mathrm A, \\
P_{r,\mathrm{stall}} &= I_{\mathrm{stall}}^2r \\
&= (60)^2(2{,}00) \\
&= 7200\,\mathrm W.
\end{aligned}
$$

#### Đánh giá và ý chính

Nếu cầu chì hoặc bộ ngắt không ngắt dòng quá tải này, cuộn dây sẽ nhanh chóng bị hỏng do nhiệt. Lúc mới khởi động cũng có một đợt dòng lớn trước khi rôto tăng tốc và thiết lập suất phản điện động. Dòng tăng làm sụt áp trên dây cấp lớn hơn, giải thích việc đèn có thể tối đi thoáng chốc khi động cơ điều hòa hoặc máy rửa bát khởi động.

Động cơ đang hoạt động tạo suất phản điện động lớn trong cuộn rôto. Trong mô hình đã dùng, nhân suất điện động ấy với dòng cho công suất cơ phát triển.

::: exercise Kiểm tra hiểu biết 27.8
Mắc thêm công tắc nối tiếp với nguồn trong Hình 27.39. Khi đóng công tắc, rôto có bắt đầu quay với mọi vị trí ban đầu hay không?
:::

::: solution Lời giải
Không. Nếu ban đầu rôto ở vị trí Hình 27.39b, dòng không đi qua vòng nên không có mômen từ khởi động. Dùng nhiều cuộn đặt ở các góc khác nhau giúp luôn có mômen khởi động, bất kể vị trí rôto.
:::
