const reference='\n\nTài liệu tham khảo: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 26, trang 844–867.'
export const dcConcepts={
 'dien-tro-tuong-duong':{name:'Điện trở tương đương',aliases:['điện trở tương đương'],definition:'Điện trở tương đương của một tổ hợp điện trở giữ nguyên quan hệ giữa dòng vào tổ hợp và hiệu điện thế hai đầu. Hai điện trở nối tiếp có $R_s=R_1+R_2$. Hai điện trở song song có $1/R_p=1/R_1+1/R_2$.',example:'Hai điện trở 2 Ω và 3 Ω cho 5 Ω khi nối tiếp, nhưng chỉ 1,2 Ω khi song song. Đây là hai cách nối khác nhau của cùng các phần tử.',use:'Thay một tổ hợp bằng một điện trở khi xét quan hệ dòng và điện áp ở hai đầu, rồi suy dòng và điện áp từng phần tử.',question:'Hai điện trở cùng nối vào một nút có nhất thiết mắc song song không?',answer:'Không. Mắc song song cần cả hai đầu của mỗi điện trở nối vào cùng hai nút. Chung một nút chưa đủ.'},
 'quy-tac-kirchhoff':{name:'Quy tắc Kirchhoff',aliases:['quy tắc Kirchhoff','quy tắc nút','quy tắc vòng'],definition:'Quy tắc nút nói tổng dòng đi vào bằng tổng dòng đi ra khi điện tích không tích tụ tại nút. Quy tắc vòng nói tổng đại số các biến thiên điện thế khi đi hết một vòng kín bằng không trong mô hình mạch đang xét.',example:'Hai dòng 2 A và 3 A đi vào nút, một dòng đi ra phải bằng 5 A. Một nguồn 12 V nối tiếp các điện trở 2 Ω và 4 Ω cho dòng 2 A và sụt áp 4 V, 8 V.',use:'Lập phương trình cho mạch có nhiều nguồn và nhánh, giữ nhất quán chiều dòng, chiều đi vòng và cực tính.',question:'Dòng tính ra âm có chứng tỏ phương trình sai không?',answer:'Không. Nếu phương trình được lập nhất quán, dấu âm cho biết dòng thực chạy ngược chiều giả định.'},
 'dien-ke':{name:'Điện kế',aliases:['điện kế','điện kế d’Arsonval','điện kế khung quay'],definition:'Điện kế d’Arsonval dùng cuộn dây có thể quay trong từ trường và lò xo hồi phục. Trong miền hiệu chuẩn, góc lệch kim tỉ lệ với dòng qua cuộn. Dòng toàn thang là dòng làm kim đạt vị trí giới hạn của thang đo.',example:'Điện kế có điện trở cuộn 20 Ω và dòng toàn thang 1 mA cần điện áp 20 mV để kim đạt toàn thang.',use:'Hiểu nguyên lý ampe kế, vôn kế, ôm kế và việc dùng điện kế phát hiện trạng thái cân bằng.',question:'Điện kế tự đo được mọi dòng lớn mà không đổi mạch không?',answer:'Không. Dòng qua cuộn phải nằm trong thang của nó. Để đo dòng lớn hơn cần nhánh rẽ thích hợp, còn đo điện áp lớn hơn cần điện trở nối tiếp.'},
 'ampe-ke':{name:'Ampe kế',aliases:['ampe kế'],definition:'Ampe kế đo dòng điện và được mắc nối tiếp với nhánh cần đo. Ampe kế lý tưởng có điện trở bằng không. Điện trở thực cần nhỏ so với điện trở của phần mạch đang đo để tác động lên dòng nhỏ.',example:'Điện kế 20 Ω, dòng toàn thang 1 mA, ghép điện trở rẽ khoảng 0,408 Ω thành ampe kế thang 50 mA. Điện trở tương đương dụng cụ là 0,400 Ω.',use:'Chọn vị trí đo dòng, tính điện trở rẽ và đánh giá ảnh hưởng của dụng cụ lên mạch.',question:'Mắc ampe kế lý tưởng trực tiếp song song với một điện trở có đo được dòng của điện trở ấy không?',answer:'Không. Ampe kế tạo đường nối có điện trở bằng không giữa hai đầu điện trở và làm thay đổi mạch. Dòng qua ampe kế lúc đó không phải dòng ban đầu qua điện trở.'},
 'von-ke':{name:'Vôn kế',aliases:['vôn kế'],definition:'Vôn kế đo hiệu điện thế giữa hai điểm và được mắc song song giữa chúng. Vôn kế lý tưởng có điện trở vô hạn nên không lấy dòng. Vôn kế thực có điện trở hữu hạn và có thể làm thay đổi điện áp cần đo.',example:'Điện kế 20 Ω, dòng toàn thang 1 mA, cần điện trở phụ nối tiếp 9980 Ω để thành vôn kế thang 10 V. Tổng điện trở dụng cụ là 10 000 Ω.',use:'Đo điện áp, tính điện trở phụ và xét sai lệch do tải của vôn kế.',question:'Điện trở vôn kế càng lớn thì ảnh hưởng lên mạch đang đo thế nào?',answer:'Với cùng điện áp, dòng vôn kế lấy nhỏ hơn. Vì vậy, tác động lên phần mạch đang đo thường nhỏ hơn, khi các điều kiện khác giữ nguyên.'},
 'chiet-ap-can-bang':{name:'Chiết áp cân bằng',aliases:['chiết áp cân bằng','phương pháp chiết áp'],definition:'Chiết áp cân bằng so sánh suất điện động cần đo với sụt áp trên một đoạn dây có dòng ổn định. Tại điểm cân bằng, điện kế chỉ không và nguồn cần đo không cấp dòng vào nhánh đo.',example:'Dây đồng nhất có sụt áp 2,0 V trên 1,0 m. Nguồn cân bằng tại chiều dài 0,60 m có suất điện động 1,2 V, nếu dòng dây và điện trở trên một đơn vị dài không đổi.',use:'Đo suất điện động của nguồn thực mà không gây sụt áp do dòng đo chạy qua điện trở trong tại cân bằng.',question:'Điện kế chỉ không có nghĩa toàn bộ hệ chiết áp không có dòng không?',answer:'Không. Dòng vẫn chạy trong dây chiết áp nhờ nguồn cấp riêng. Chỉ nhánh chứa nguồn cần đo và điện kế có dòng bằng không ở cân bằng.'},
 'mach-rc':{name:'Mạch R-C',aliases:['mạch R-C','mạch RC','mạch điện trở và tụ điện'],definition:'Mạch R-C gồm điện trở và tụ điện. Trong mạch nạp hoặc phóng đơn giản, dòng và điện tích thay đổi theo thời gian do điện áp tụ phụ thuộc điện tích. Thời gian đặc trưng là $\\tau=RC$.',example:'Tụ 5,0 µF nạp qua điện trở 2,0 MΩ từ nguồn 10 V có hằng số thời gian 10 s, điện tích cuối 50 µC và dòng đầu 5,0 µA.',use:'Phân tích nạp, phóng, tính điện tích, dòng, điện áp và năng lượng theo thời gian.',question:'Dòng qua mạch nạp có bằng ℰ/R ở mọi thời điểm không?',answer:'Không. Giá trị ấy chỉ là dòng đầu khi tụ chưa tích điện. Điện áp trên tụ tăng làm điện áp trên điện trở và dòng giảm dần.'},
 'hang-so-thoi-gian':{name:'Hằng số thời gian',aliases:['hằng số thời gian','thời gian hồi phục'],definition:'Hằng số thời gian τ đặc trưng tốc độ giảm theo hàm mũ. Nếu một đại lượng giảm theo $e^{-t/\\tau}$, sau thời gian τ nó còn $e^{-1}$ lần giá trị đầu. Với điện tích và dòng trong mạch R-C đơn giản, $\\tau=RC$.',example:'Sau một τ, dòng nạp hoặc độ lớn dòng phóng còn khoảng 36,8% ban đầu. Điện tích tụ đang nạp từ không đạt khoảng 63,2% giá trị cuối.',use:'So sánh thời gian nạp, phóng và nhận ra đại lượng nào có cùng hoặc khác thời gian đặc trưng.',question:'Năng lượng tụ phóng có cùng hằng số thời gian với điện tích không?',answer:'Không. Năng lượng tỉ lệ bình phương điện tích nên giảm theo e^(−2t/τ). Hằng số thời gian của năng lượng là τ/2.'}
}
export const dcWikiDetails={
 'dien-tro-tuong-duong':String.raw`Hai điện trở nối tiếp có cùng dòng I vì không có nhánh rẽ giữa chúng. Cộng các hiệu điện thế cho V = IR₁ + IR₂, nên R_s = R₁ + R₂. Hai điện trở song song có cùng V vì nối cùng hai nút. Cộng các dòng cho I = V/R₁ + V/R₂.

Với n điện trở dương, khai triển trước khi dùng ký hiệu tổng:

$$
\begin{aligned}
&R_s = R_1+R_2+\cdots+R_n,\\
&R_s = \sum_{j=1}^{n}R_j,\\
&\frac1{R_p} = \frac1{R_1}+\frac1{R_2}+\cdots+\frac1{R_n},\\
&\frac1{R_p} = \sum_{j=1}^{n}\frac1{R_j}.
\end{aligned}
$$

Chỉ số j chạy từ 1 đến n qua các điện trở của tổ hợp. R_s lớn hơn từng điện trở thành phần khi có ít nhất hai điện trở dương. R_p nhỏ hơn từng điện trở thành phần. Thay tổ hợp bằng điện trở tương đương giữ quan hệ ở hai đầu, nhưng vẫn cần quay lại mạch ban đầu để tìm dòng mỗi nhánh.`+reference,
 'quy-tac-kirchhoff':String.raw`Chọn chiều dương của từng dòng trước khi lập phương trình. Với hai dòng I₁, I₂ đi vào nút và I₃ đi ra, bảo toàn điện tích cho I₁ + I₂ − I₃ = 0. Tổng quát, với m dòng có dấu:

$$
\begin{aligned}
&\widetilde I_1+\widetilde I_2+\cdots+\widetilde I_m = 0,\\
&\sum_{j=1}^{m}\widetilde I_j = 0.
\end{aligned}
$$

Chỉ số j chạy qua m nhánh tại nút. Dấu của mỗi dòng biểu thị chiều vào hoặc ra theo quy ước chung.

Khi đi quanh vòng, mỗi đoạn có một biến thiên điện thế. Với ba đoạn, ΔV₁ + ΔV₂ + ΔV₃ = 0. Tổng quát cho k đoạn:

$$
\sum_{j=1}^{k}\Delta V_j=0.
$$

Qua điện trở theo chiều dòng cho −IR, đi ngược chiều dòng cho +IR. Qua nguồn từ cực âm đến cực dương cho +ℰ, chiều ngược lại cho −ℰ. Trong mạch nhiều nhánh, không được tự coi mọi điện trở trên một vòng có cùng dòng.

Quy tắc vòng dùng tính chất thế của điện trường trong mô hình tĩnh điện. Nếu có từ thông biến thiên, cần tính suất điện động cảm ứng trong phương trình mạch tương ứng.`+reference,
 'dien-ke':String.raw`Cuộn dây mang dòng đặt trong từ trường chịu mômen làm quay cuộn và kim gắn với nó. Lò xo tạo mômen hồi phục. Khi hai mômen cân bằng trong miền hiệu chuẩn, góc lệch tỉ lệ dòng qua cuộn.

Gọi R_G là điện trở cuộn và I_G là dòng toàn thang. Điện áp toàn thang của cuộn là:

$$
V_G=I_GR_G.
$$

Điện kế có thể phát hiện cả chiều dòng bằng chiều lệch kim. Ghép nhánh rẽ để tạo ampe kế hoặc thêm điện trở nối tiếp để tạo vôn kế. Trong phương pháp cân bằng, kim chỉ không báo nhánh đo không có dòng, dù những nhánh khác vẫn có dòng.`+reference,
 'ampe-ke':String.raw`Ampe kế được mắc nối tiếp để dòng của nhánh cần đo đi qua dụng cụ. Điện trở ampe kế thực làm tăng điện trở nhánh và có thể làm dòng giảm. Giới hạn lý tưởng là R_A = 0.

Để đo dòng toàn thang I lớn hơn I_G, ghép điện trở rẽ R_sh song song với cuộn điện kế R_G. Dòng qua nhánh rẽ là I − I_G. Hai nhánh có cùng điện áp:

$$
\begin{aligned}
&I_GR_G = (I-I_G)R_{\mathrm{sh}},\\
&R_{\mathrm{sh}} = \frac{I_GR_G}{I-I_G}.
\end{aligned}
$$

Điện trở tương đương của cả dụng cụ nhỏ hơn R_G. Công thức dùng các điện trở Ohm và I > I_G. Dòng qua cuộn không bằng dòng tổng của ampe kế khi có nhánh rẽ.`+reference,
 'von-ke':String.raw`Vôn kế nối giữa hai điểm cần so sánh điện thế. Dòng qua vôn kế thực là một nhánh bổ sung của mạch. Nếu điện trở của nó không đủ lớn so với phần mạch liên quan, điện áp sau khi mắc dụng cụ có thể khác điện áp trước đó.

Để điện kế có dòng toàn thang I_G ở điện áp thang V, tổng điện trở cần bằng V/I_G. Điện trở phụ nối tiếp cuộn là:

$$
\begin{aligned}
&R_G+R_s = V/I_G,\\
&R_s = \frac V{I_G}-R_G.
\end{aligned}
$$

Vôn kế lý tưởng có điện trở vô hạn. Nó đo điện áp nhưng không lấy dòng. Trong hai cách mắc ampe kế và vôn kế để đo điện trở, cần tính rõ điện trở dụng cụ nào nằm trong giá trị suy ra từ V/I.`+reference,
 'chiet-ap-can-bang':String.raw`Một nguồn cấp riêng duy trì dòng I qua dây chiết áp đồng nhất. Điện thế giảm đều theo chiều dài dây nếu tiết diện A và điện trở suất ρ không đổi. Với đoạn dài L:

$$
\begin{aligned}
&R_L = \rho L/A,\\
&V_L = IR_L.
\end{aligned}
$$

Điều chỉnh điểm tiếp xúc để điện kế trong nhánh chứa nguồn cần đo chỉ không. Khi đó suất điện động cần đo bằng sụt áp trên đoạn dây:

$$
\mathcal E_x=I\rho L/A.
$$

Nguồn cần đo không cấp dòng ở cân bằng, nên không có sụt áp do dòng đo qua điện trở trong. Nếu I hoặc nhiệt độ dây thay đổi, quan hệ điện áp trên một đơn vị chiều dài cũng thay đổi và cần hiệu chuẩn lại.`+reference,
 'mach-rc':String.raw`Khi nạp tụ chưa tích điện từ nguồn lý tưởng có suất điện động ℰ không đổi qua R, quy tắc vòng cho ℰ − iR − q/C = 0. Vì i = dq/dt, đây là phương trình vi phân của điện tích:

$$
\begin{aligned}
&\frac{dq}{dt} = \frac{\mathcal E}{R}-\frac q{RC},\\
&q(t) = C\mathcal E(1-e^{-t/(RC)}),\\
&i(t) = \frac{\mathcal E}{R}e^{-t/(RC)}.
\end{aligned}
$$

Điện tích không nhảy đột ngột trong mạch có dòng hữu hạn. Lúc đầu q = 0, sau thời gian đủ dài q tiến đến Cℰ và dòng tiến đến không.

Ngắt nguồn rồi cho tụ có điện tích Q₀ phóng qua R:

$$
\begin{aligned}
&q(t) = Q_0e^{-t/(RC)},\\
&i(t) = -\frac{Q_0}{RC}e^{-t/(RC)}.
\end{aligned}
$$

Dấu âm dùng chiều nạp làm chiều dương. Năng lượng ban đầu Q₀²/(2C) cuối cùng chuyển thành nhiệt trên điện trở. Các công thức cần R và C không đổi, tụ lý tưởng và đúng cấu hình nạp hoặc phóng đã nêu.`+reference,
 'hang-so-thoi-gian':String.raw`Một đại lượng x giảm theo x(t) = x₀e^(−t/τ) còn x₀/e sau một τ. Đây là thời gian để giảm theo một hệ số xác định, không phải thời gian đại lượng đột ngột trở thành không.

Trong mạch R-C đơn giản, điện tích phóng, điện áp tụ và độ lớn dòng có τ = RC. Với tụ đang nạp từ không, đại lượng giảm theo cùng τ là phần điện tích còn thiếu so với Q_f = Cℰ.

Nếu muốn đại lượng giảm còn một phần f, với 0 < f < 1:

$$
\begin{aligned}
&f = e^{-t/\tau},\\
&t = -\tau\ln f.
\end{aligned}
$$

Năng lượng của tụ tỉ lệ q², nên khi phóng nó giảm theo e^(−2t/τ). Thời gian đặc trưng của năng lượng là τ/2. Do đó, cùng một giá trị f đòi hỏi thời gian khác nhau khi xét điện tích và năng lượng.`+reference
}
export const dcWikiConnections={
 'dien-tro-tuong-duong':['dien-tro','dong-dien','dien-the','quy-tac-kirchhoff'],
 'quy-tac-kirchhoff':['dien-tich','dong-dien','dien-the','suat-dien-dong'],
 'dien-ke':['dong-dien','ampe-ke','von-ke'],
 'ampe-ke':['dien-ke','dien-tro-tuong-duong','dong-dien'],
 'von-ke':['dien-ke','dien-the','dien-tro'],
 'chiet-ap-can-bang':['suat-dien-dong','dien-tro-trong','dien-ke','dien-tro-suat'],
 'mach-rc':['dien-dung','dien-tro','quy-tac-kirchhoff','hang-so-thoi-gian','dao-ham'],
 'hang-so-thoi-gian':['mach-rc','dien-dung','dien-tro','tich-phan']
}
