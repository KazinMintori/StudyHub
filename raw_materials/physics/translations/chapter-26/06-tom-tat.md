<!-- Source: Chapter26 Summary, printed867/PDF887. -->

## Tóm tắt

### Điện trở nối tiếp và song song

![Tóm tắt: Hai cách mắc điện trở giữa cùng hai đầu mạch](img/young-26/tom-tat-noi-tiep-song-song.png)

Nối tiếp giữ cùng dòng, song song giữ cùng hiệu điện thế.

Các điện trở nối tiếp có cùng dòng điện. Điện trở tương đương bằng tổng các điện trở thành phần. Với ba điện trở:

$$
R_s=R_1+R_2+R_3.
$$

Với n điện trở, tổng ấy viết là $\sum_{i=1}^{n}R_i$, trong đó i chạy từ 1 đến n. Các điện trở song song nối vào cùng hai nút, nên có cùng hiệu điện thế. Với ba điện trở:

$$
\frac1{R_p}=\frac1{R_1}+\frac1{R_2}+\frac1{R_3}.
$$

Tổng quát, 1/R_p bằng tổng các nghịch đảo 1/Rᵢ, từ i = 1 đến i = n. Xem Ví dụ 26.1–26.2.

### Quy tắc Kirchhoff

![Tóm tắt: Quy ước dòng điện tại nút và chiều duyệt vòng](img/young-26/tom-tat-kirchhoff.png)

Quy tắc nút và quy tắc vòng dùng cùng hệ quy ước dấu đã chọn.

Quy tắc nút dựa vào bảo toàn điện tích. Tổng đại số các dòng tại nút bằng không nếu dòng vào và ra được gán dấu trái nhau. Chẳng hạn I₁,I₂ vào nút và I₃ đi ra:

$$
I_1+I_2-I_3=0.
$$

Quy tắc vòng dựa vào bảo toàn năng lượng và tính chất thế của trường tĩnh điện. Tổng đại số các biến thiên điện thế quanh một vòng kín bằng không. Chẳng hạn một nguồn lý tưởng và hai điện trở nối tiếp cho:

$$
\mathcal E-IR_1-IR_2=0.
$$

Viết dưới dạng tổng, với m nhánh tại nút và k phần tử trên vòng:

$$
\begin{aligned}
\sum_{i=1}^{m}I_i &= 0, \\
\sum_{j=1}^{k}\Delta V_j &= 0.
\end{aligned}
$$

Iᵢ là dòng đã gán dấu theo quy ước nút. ΔVⱼ là tăng hoặc giảm điện thế theo chiều đi vòng đã chọn. Cần dùng nhất quán cùng quy ước khi lập và giải phương trình. Xem Ví dụ 26.3–26.7.

### Dụng cụ đo điện

![Tóm tắt: Điện trở phụ và cuộn dây điện kế](img/young-26/tom-tat-dung-cu-do.png)

Cách mắc điện trở phụ quyết định dụng cụ đo dòng hay hiệu điện thế.

Trong điện kế khung quay d’Arsonval, góc lệch tỉ lệ với dòng qua cuộn dây. Để đo dòng lớn hơn dòng toàn thang của cuộn, mắc thêm điện trở shunt song song để một phần dòng đi vòng qua cuộn. Dụng cụ được hiệu chuẩn thành ampe kế.

Nếu cuộn và điện trở nối tiếp bổ sung tuân theo Ohm, có thể hiệu chuẩn dòng qua cuộn theo hiệu điện thế, tạo thành vôn kế. Ampe kế tốt có điện trở rất nhỏ để ít làm thay đổi dòng đo. Vôn kế tốt có điện trở rất lớn để ít lấy dòng khỏi phần mạch được đo. Xem Ví dụ 26.8–26.11.

### Mạch điện trở và tụ điện

![Tóm tắt: Điện tích và dòng trong quá trình nạp tụ](img/young-26/tom-tat-mach-rc.png)

Điện tích tăng về giá trị cuối trong khi dòng giảm về không.

Khi nạp một tụ ban đầu chưa có điện tích qua điện trở R từ nguồn suất điện động ℰ không đổi, điện tích tiến dần đến giá trị cuối và dòng tiến dần về không:

$$
\begin{aligned}
q(t) &= C\mathcal E(1-e^{-t/(RC)}), \\
&= Q_f(1-e^{-t/(RC)}), \\
i(t) &= \frac{\mathcal E}{R}e^{-t/(RC)}.
\end{aligned}
$$

Q_f = Cℰ là điện tích cuối. Hằng số thời gian, còn gọi là thời gian hồi phục, bằng τ = RC. Sau một τ, phần điện tích còn thiếu so với Q_f bằng 1/e của độ thiếu ban đầu, còn dòng bằng 1/e dòng đầu.

Khi tụ có điện tích đầu Q₀ được ngắt nguồn rồi phóng qua R:

$$
\begin{aligned}
q(t) &= Q_0e^{-t/(RC)}, \\
i(t) &= \frac{dq}{dt} \\
&= -\frac{Q_0}{RC}e^{-t/(RC)}.
\end{aligned}
$$

Dấu âm của i dùng quy ước dòng nạp là chiều dương. Dòng phóng thực có chiều ngược lại. Hai quá trình có cùng hằng số thời gian khi dùng cùng R và C. Xem Ví dụ 26.12–26.13.

### Hệ thống dây điện gia đình

![Tóm tắt: Mạch nhánh nối các thiết bị song song](img/young-26/tom-tat-phan-phoi-dien.png)

Các mạch nhánh nhận cùng điện áp cấp trong mô hình đang xét.

Trong hệ thống được xét, các thiết bị nối song song vào đường cấp điện gồm dây pha và dây trung tính. Dây nối đất bổ sung tạo đường bảo vệ khi vỏ kim loại thiết bị có sự cố. Dòng lớn nhất cho phép phụ thuộc kích thước dây và nhiệt độ mà dây chịu được.

Cầu chì hoặc thiết bị ngắt mạch bảo vệ trước dòng quá mức và nguy cơ phát nhiệt gây cháy. Định mức của thiết bị ngắt phải phù hợp với mạch được bảo vệ, không chỉ với công suất của các thiết bị đang cắm. Xem Ví dụ 26.14.
