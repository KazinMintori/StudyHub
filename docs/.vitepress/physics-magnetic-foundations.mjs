const reference='\n\nTài liệu tham khảo: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 27, trang 878–907.'
export const magneticConcepts={
 'tu-truong':{name:'Từ trường',aliases:['từ trường'],definition:'Từ trường là trường vector mô tả tương tác từ. Điện tích chuyển động hoặc dòng điện tạo từ trường. Hạt mang điện q, chuyển động với vận tốc v trong trường B, chịu lực từ $\\vec F=q\\vec v\\times\\vec B$. Đơn vị SI là tesla.',example:'Proton có tốc độ 300 km/s tạo góc 30° với từ trường 2,0 T chịu lực có độ lớn 4,8×10⁻¹⁴ N. Với cùng vận tốc và từ trường, electron chịu lực cùng độ lớn nhưng ngược chiều.',use:'Tính lực lên hạt tải, dây dẫn và vòng dây, phân tích quỹ đạo và hoạt động của thiết bị từ.',question:'Có từ trường tại một điểm thì một hạt mang điện ở đó có luôn chịu lực từ không?',answer:'Không. Lực bằng không nếu hạt đứng yên hoặc vận tốc song song hay ngược song song với trường. Hướng và độ lớn lực phụ thuộc cả điện tích lẫn vận tốc.'},
 'luc-tu-tren-dien-tich':{name:'Lực từ lên điện tích',aliases:['lực từ lên điện tích','lực từ'],definition:'Lực từ lên hạt điện tích chuyển động được cho bởi tích có hướng của vận tốc và từ trường, nhân điện tích có dấu. Lực vuông góc với vận tốc tức thời nên công suất của riêng lực từ bằng không.',example:'Trong từ trường đều hướng vào mặt giấy, một hạt dương bay sang phải chịu lực hướng lên. Hạt âm cùng vận tốc chịu lực hướng xuống.',use:'Xác định dấu điện tích từ hướng cong và phân biệt lực đổi hướng chuyển động với lực làm đổi động năng.',question:'Lực từ có thể làm hạt tăng tốc độ dù không thay đổi hướng không?',answer:'Không, nếu chỉ có lực từ. Lực vuông góc vận tốc nên không sinh công. Tốc độ có thể đổi khi có lực khác, chẳng hạn lực điện.'},
 'duong-suc-tu':{name:'Đường sức từ',aliases:['đường sức từ'],definition:'Đường sức từ có tiếp tuyến tại mỗi điểm cùng hướng vector từ trường. Trong cùng một bản đồ, các đường dày hơn biểu thị trường mạnh hơn. Đường sức không chỉ hướng lực từ lên hạt và không có điểm đầu hoặc điểm cuối.',example:'Bên ngoài nam châm thanh, đường sức đi từ cực bắc đến cực nam rồi tiếp tục trong nam châm. Dấu chấm biểu diễn trường hướng ra mặt giấy, dấu chéo biểu diễn trường hướng vào.',use:'Đọc hướng và độ mạnh tương đối của trường, lựa chọn pháp tuyến và giải thích tác dụng của la bàn.',question:'Hai đường sức có thể cắt nhau tại một điểm có từ trường khác không không?',answer:'Không. Hai tiếp tuyến khác nhau sẽ gán hai hướng khác nhau cho cùng một vector từ trường tại điểm ấy.'},
 'tu-thong':{name:'Từ thông',aliases:['từ thông'],definition:'Từ thông là tích phân mặt của thành phần từ trường theo pháp tuyến đã chọn, $\\Phi_B=\\int\\vec B\\cdot d\\vec A$. Nó là đại lượng vô hướng có dấu, đơn vị weber. Qua mọi mặt kín, từ thông tổng bằng không.',example:'Mặt diện tích $3{,}0\\,\\mathrm{cm^2}$ trong trường 6,0 T, với pháp tuyến tạo góc 60° cùng trường, có từ thông +0,90 mWb. Đảo pháp tuyến cho −0,90 mWb.',use:'Liên hệ trường với hình học mặt và dấu pháp tuyến, chuẩn bị cho cảm ứng điện từ.',question:'Từ thông mặt kín bằng không có buộc trường bằng không trong hoặc trên mặt không?',answer:'Không. Các đóng góp đi vào và đi ra có thể triệt tiêu dù từ trường tại mỗi điểm khác không.'},
 'chuyen-dong-hat-trong-tu-truong':{name:'Chuyển động hạt trong từ trường',aliases:['chuyển động trong từ trường','quỹ đạo xoắn ốc'],definition:'Trong từ trường đều và chỉ có lực từ, thành phần vận tốc song song trường không đổi. Thành phần vuông góc quay đều trong mô hình không tương đối tính. Kết hợp hai chuyển động cho đường xoắn ốc, hoặc đường tròn nếu thành phần song song bằng không.',example:'Electron chuyển động tròn trong từ trường có tần số không phụ thuộc tốc độ ở mô hình không tương đối tính. Tăng tốc độ làm bán kính lớn hơn, nhưng chu kỳ giữ nguyên nếu trường và khối lượng không đổi.',use:'Tính bán kính, chu kỳ, bước xoắn và nhận ra điều kiện áp dụng mô hình khối lượng không đổi.',question:'Hai hạt cùng khối lượng và độ lớn điện tích nhưng khác tốc độ vuông góc có cùng bán kính không?',answer:'Không. Bán kính tỉ lệ tốc độ vuông góc. Tuy nhiên, chu kỳ bằng nhau trong cùng trường đều và mô hình không tương đối tính.'},
 'bo-chon-van-toc':{name:'Bộ chọn vận tốc',aliases:['bộ chọn vận tốc'],definition:'Bộ chọn vận tốc bố trí điện trường và từ trường chéo nhau để lực điện và lực từ triệt tiêu đối với hạt có vận tốc phù hợp. Khi vận tốc vuông góc cả hai trường và hai lực đối nhau, tốc độ được chọn là $v=E/B$.',example:'Các hạt có cùng tốc độ được chọn dù khác khối lượng. Nếu hạt lệch tốc độ ấy, lực tổng không còn bằng không và quỹ đạo bị lệch.',use:'Lọc chùm hạt theo vận tốc trước khi đo tỉ số khối lượng và điện tích.',question:'Chỉ có độ lớn v = E/B thì mọi hướng chuyển động đều đi thẳng không?',answer:'Không. Còn cần hướng sao cho tích v×B đối với điện trường. Công thức độ lớn tự nó không xác định hướng.'},
 'khoi-pho':{name:'Khối phổ',aliases:['khối phổ','máy khối phổ'],definition:'Khối phổ phân biệt hạt theo tỉ số khối lượng và độ lớn điện tích nhờ chuyển động trong điện trường hoặc từ trường. Trong cấu hình gồm bộ chọn vận tốc rồi trường phân tích vuông góc, bán kính quỹ đạo tỉ lệ m/|q| khi tốc độ và trường giữ nguyên.',example:'Hai đồng vị có cùng điện tích và được chọn cùng tốc độ đi theo các bán kính khác nhau trong cùng trường phân tích. Đồng vị nặng hơn có bán kính lớn hơn.',use:'Giải thích phép phân biệt đồng vị và suy khối lượng từ vị trí chùm hạt trên bộ thu.',question:'Bán kính lớn hơn có luôn chứng tỏ hạt nặng hơn không?',answer:'Chỉ khi độ lớn điện tích, tốc độ và từ trường phân tích được giữ như nhau. Nếu một trong các đại lượng ấy đổi, bán kính còn phụ thuộc sự thay đổi đó.'},
 'momen-tu':{name:'Mômen từ',aliases:['mômen từ','mômen lưỡng cực từ'],definition:'Mômen từ của vòng dây phẳng là $\\vec\\mu=I\\vec A$, với vector diện tích hướng theo quy tắc bàn tay phải của dòng. Nó đặc trưng cách vòng tương tác với từ trường, có đơn vị $\\mathrm{A\\cdot m^2}$. Mômen từ khác mômen lực.',example:'Cuộn 30 vòng, bán kính 5,00 cm, dòng 5,00 A có mômen từ khoảng 1,18 $\\mathrm{A\\cdot m^2}$. Hướng của nó vuông góc mặt cuộn theo chiều dòng.',use:'Tính mômen lực và thế năng của vòng dây, mô tả nam châm như lưỡng cực từ.',question:'Mômen từ lớn có đồng nghĩa mômen lực luôn lớn không?',answer:'Không. Mômen lực còn phụ thuộc trường và góc giữa mômen từ với trường. Khi hai vector song song hoặc ngược song song, mômen lực bằng không.'},
 'luong-cuc-tu':{name:'Lưỡng cực từ',aliases:['lưỡng cực từ'],definition:'Lưỡng cực từ là hệ có mômen từ, chẳng hạn vòng dây mang dòng. Trong trường đều, mômen lực bằng tích có hướng của mômen từ và trường, còn thế năng có thể viết $U=-\\vec\\mu\\cdot\\vec B$ với mốc thích hợp.',example:'Cuộn có mômen từ 1,18 $\\mathrm{A\\cdot m^2}$ quay từ hướng vuông góc sang cùng hướng với trường 1,20 T làm thế năng giảm khoảng 1,41 J.',use:'Phân tích cân bằng bền và không bền, công của mômen từ, lực trong trường không đều và tương tác nam châm.',question:'Vòng dây không chịu tổng lực trong trường đều có nhất thiết không quay không?',answer:'Không. Hai lực ngược chiều đặt trên các đường tác dụng khác nhau có thể tạo mômen tổng dù tổng lực bằng không.'},
 'suat-phan-dien-dong':{name:'Suất phản điện động',aliases:['suất phản điện động'],definition:'Suất phản điện động là suất điện động cảm ứng trong động cơ đang quay có chiều chống lại dòng được nguồn ngoài duy trì. Trong mô hình động cơ nối tiếp, điện áp hai cực bằng suất phản điện động cộng sụt áp trên điện trở trong.',example:'Động cơ có điện áp 120 V, dòng 4,00 A và điện trở trong 2,00 Ω có suất phản điện động 112 V. Trong mô hình bỏ qua tổn hao khác, công suất cơ phát triển là 448 W.',use:'Liên hệ tốc độ rôto, dòng, công suất, hiệu suất và dòng lớn khi khởi động hoặc rôto bị kẹt.',question:'Rôto dừng có làm dòng giảm về không trong mô hình nguồn cố định không?',answer:'Không. Suất phản điện động mất đi nên dòng trở thành V/r, thường lớn hơn dòng khi động cơ đang quay trong cùng mô hình.'},
 'hieu-ung-hall':{name:'Hiệu ứng Hall',aliases:['hiệu ứng Hall','điện áp Hall'],definition:'Hiệu ứng Hall tạo điện áp ngang vật dẫn mang dòng khi đặt trong từ trường. Lực từ làm hạt tải tích tụ ở một mép đến khi điện trường ngang cân bằng lực từ. Cực tính phụ thuộc dấu hạt tải.',example:'Dải đồng mang dòng 75 A trong trường 0,40 T tạo điện áp Hall chỉ 0,81 µV trong phép đo đang xét. Mô hình một loại hạt tải suy mật độ khoảng $1{,}16\\times10^{29}\\,\\mathrm{m^{-3}}$.',use:'Suy dấu và mật độ hạt tải trong mô hình phù hợp, đo từ trường hoặc phát hiện chuyển động bằng cảm biến.',question:'Điện áp Hall lớn hơn có luôn nghĩa từ trường mạnh hơn không?',answer:'Không. Nó còn phụ thuộc dòng, mật độ và điện tích hạt tải, bề dày mẫu và mô hình dẫn điện của vật liệu.'}
}
export const magneticWikiDetails={
 'tu-truong':String.raw`Từ trường được tạo bởi điện tích chuyển động và dòng điện. Ở đây ta xét phản ứng của hạt khi đã biết trường. Quy luật nguồn của trường được xét ở các chương tiếp theo.

$$
\begin{aligned}
\vec F_B&=q\vec v\times\vec B,\\
F_B&=|q|vB\sin\phi.
\end{aligned}
$$

φ là góc giữa hai vector. Điện tích dương chịu lực theo tích có hướng, điện tích âm chịu lực ngược hướng. Không suy lực chỉ từ hướng B. Nếu có cả điện trường, tổng lực điện từ là:

$$
\vec F=q\vec E+q\vec v\times\vec B.
$$

Đơn vị tesla bằng N/(A·m). Một gauss bằng 10⁻⁴ tesla. Đường sức biểu diễn hướng và độ mạnh tương đối của trường, còn từ thông đo thành phần xuyên qua một mặt theo pháp tuyến.`+reference,
 'luc-tu-tren-dien-tich':String.raw`Tích có hướng cho lực vuông góc với cả vận tốc và từ trường. Đổi dấu điện tích đảo lực. Đảo riêng vận tốc hoặc từ trường cũng đảo lực.

Vì vuông góc vận tốc, công suất tức thời của riêng lực từ bằng không:

$$
\begin{aligned}
P_B&=\vec F_B\cdot\vec v=0,\\
dW_B&=\vec F_B\cdot d\vec r=0.
\end{aligned}
$$

Từ trường có thể đổi hướng động lượng mà không đổi động năng của hạt khi không có lực khác sinh công. Khi lực điện cùng tác dụng, tốc độ có thể thay đổi do lực điện. Phân biệt nhận xét về một hạt với năng lượng của cả nguồn, dây và trường trong một hệ thiết bị.`+reference,
 'duong-suc-tu':String.raw`Đường sức là cách biểu diễn một trường vector. Tại điểm có trường khác không, tiếp tuyến có hướng B. Dấu chấm biểu diễn vector ra khỏi mặt giấy, dấu chéo biểu diễn vector đi vào.

Kim la bàn định hướng theo trường tại chỗ. Lực từ lên một điện tích đang chuyển động lại vuông góc trường. Vì vậy, đường sức từ không phải đường chỉ hướng lực ấy.

Trong các bản đồ nam châm, đường sức đi qua bên ngoài và tiếp tục trong nam châm. Đường sức không có nguồn hay điểm tận cùng. Định luật Gauss cho từ trường nói tổng từ thông mặt kín bằng không. Phát biểu này không buộc mọi đường sức tổng quát phải khép trong một miền hữu hạn, chẳng hạn trường đều lý tưởng có các đường kéo dài đến vô cực.`+reference,
 'tu-thong':String.raw`Vector diện tích của phần tử mặt có độ lớn dA và hướng pháp tuyến. Gọi φ là góc giữa trường và pháp tuyến:

$$
\begin{aligned}
d\Phi_B&=\vec B\cdot d\vec A\\
&=B\cos\phi\,dA,\\
\Phi_B&=\int\vec B\cdot d\vec A.
\end{aligned}
$$

Mặt phẳng trong trường đều cho Φ_B = BA cosφ. Mặt hở có hai lựa chọn pháp tuyến, nên cần nêu lựa chọn. Mặt kín dùng pháp tuyến ngoài:

$$
\oint\vec B\cdot d\vec A=0.
$$

Thông lượng vào có dấu âm, thông lượng ra có dấu dương. Chúng triệt tiêu tổng dù trường tại từng điểm không bằng không. Weber bằng tesla mét vuông. Từ thông và từ trường là hai đại lượng khác nhau, đơn vị cũng khác nhau.`+reference,
 'chuyen-dong-hat-trong-tu-truong':String.raw`Tách vận tốc thành các thành phần song song và vuông góc từ trường đều. Lực từ không có thành phần dọc trường, nên v_∥ không đổi. Phần vuông góc chịu lực hướng tâm:

$$
\begin{aligned}
|q|v_\perp B&=mv_\perp^2/R,\\
R&=\frac{mv_\perp}{|q|B},\\
\omega&=|q|B/m,\\
T&=\frac{2\pi m}{|q|B},\\
p&=v_\parallel T.
\end{aligned}
$$

Các biểu thức dùng mô hình không tương đối tính. Dấu điện tích đảo chiều quay, nhưng không đổi bán kính khi các độ lớn khác giống nhau. Thành phần song song bằng không cho đường tròn, thành phần vuông góc bằng không cho chuyển động thẳng dọc trường.`+reference,
 'bo-chon-van-toc':String.raw`Cân bằng hai lực cần một phương trình vector:

$$
\vec E+\vec v\times\vec B=0.
$$

Trong bố trí vận tốc vuông góc cả hai trường, cân bằng độ lớn cho v = E/B. Còn phải chọn chiều để lực điện và lực từ đối nhau. Điện tích có dấu q triệt tiêu khỏi điều kiện cân bằng khi q khác không.

Các hạt nhanh hơn hoặc chậm hơn có lực tổng khác không và bị lệch. Bộ chọn vận tốc không tự chọn khối lượng. Muốn phân biệt khối lượng cần vùng phân tích hoặc phép đo bổ sung.`+reference,
 'khoi-pho':String.raw`Một cấu hình khối phổ dùng bộ chọn vận tốc với trường E, B rồi trường phân tích B′ vuông góc chùm hạt. Với hạt không tương đối tính:

$$
\begin{aligned}
v&=E/B,\\
R&=\frac{mv}{|q|B'},\\
\frac m{|q|}&=\frac{BB'R}{E}.
\end{aligned}
$$

Độ lệch trên bộ thu cho bán kính, từ đó suy m/|q|. Nếu điện tích đã biết, suy được khối lượng. Khi hạt đi qua nửa vòng tròn, khoảng cách giữa điểm vào và điểm tới bộ thu liên hệ với đường kính 2R. Không đồng nhất khoảng cách bộ thu với bán kính nếu hình học khác.`+reference,
 'momen-tu':String.raw`Vòng dây phẳng diện tích A và dòng I có mômen từ:

$$
\vec\mu=I\vec A.
$$

Khum ngón tay phải theo chiều dòng, ngón cái chỉ hướng vector diện tích và mômen từ. Với N vòng giống nhau cùng hướng, cộng các vector đóng góp. Viết tường minh trước dạng gọn:

$$
\begin{aligned}
\vec\mu&=\vec\mu_1+\vec\mu_2+\cdots\\
&\quad+\vec\mu_N,\\
\vec\mu&=\sum_{j=1}^{N}\vec\mu_j,\\
\vec\mu_j&=I\vec A,\\
\vec\mu&=NI\vec A.
\end{aligned}
$$

j chạy từ 1 đến N qua các vòng. Nếu hướng hoặc diện tích các vòng khác nhau, cần cộng vector thực thay vì nhân N. Mômen từ có đơn vị $\\mathrm{A\\cdot m^2}$, mômen lực có đơn vị N·m.`+reference,
 'luong-cuc-tu':String.raw`Trong từ trường đều, lưỡng cực chịu mômen:

$$
\begin{aligned}
\vec\tau&=\vec\mu\times\vec B,\\
\tau&=\mu B\sin\phi.
\end{aligned}
$$

Chọn mốc thế năng bằng không khi hai vector vuông góc:

$$
U=-\vec\mu\cdot\vec B.
$$

Cùng chiều cho thế năng nhỏ nhất và cân bằng bền, ngược chiều cho thế năng lớn nhất và cân bằng không bền. Trong trường đều, vòng dây kín có tổng lực bằng không. Trong trường không đều, tổng lực có thể khác không, vì lực trên các phần của vòng không triệt tiêu.

Mô hình lưỡng cực giúp giải thích nam châm định hướng, lực hút sắt bị cảm ứng từ và tương tác giữa hai nam châm. Mômen từ vi mô của electron cần mô tả lượng tử, không coi electron là quả cầu quay cổ điển.`+reference,
 'suat-phan-dien-dong':String.raw`Suất phản điện động trong mô hình động cơ nối tiếp thỏa mãn:

$$
\begin{aligned}
V_{ab}&=\mathcal E+Ir,\\
V_{ab}I&=\mathcal EI+I^2r.
\end{aligned}
$$

ℰI là công suất cơ phát triển trong mô hình bỏ qua tổn hao khác, I²r là công suất nhiệt. Khi từ trường và cấu hình không đổi, suất phản điện động tỉ lệ tốc độ. Rôto dừng cho ℰ = 0 và I = V_ab/r.

Mômen động cơ còn phụ thuộc cách tạo từ trường. Với nam châm vĩnh cửu giữ trường, đảo dòng rôto đảo mômen. Với cuộn kích từ và rôto nối cùng nguồn, đảo đồng thời dòng và trường có thể giữ nguyên chiều mômen. Cần phân biệt các cấu hình ấy.`+reference,
 'hieu-ung-hall':String.raw`Lực từ đẩy hạt tải về mép và tạo điện trường ngang. Ở trạng thái ổn định, tổng lực ngang bằng không. Với dòng theo x và trường theo y:

$$
\begin{aligned}
qE_z+qv_xB_y&=0,\\
E_z&=-v_xB_y,\\
J_x&=nqv_x,\\
nq&=-\frac{J_xB_y}{E_z}.
\end{aligned}
$$

v_x và q đều có dấu. Electron tạo dòng dương có v_x âm. Điện áp Hall cho dấu hạt tải và, khi biết độ lớn điện tích, cho mật độ trong mô hình một loại hạt tải phù hợp.

Với dải có bề dày t theo từ trường:

$$
|V_H|=\frac{IB}{n|q|t}.
$$

Quan hệ này có giới hạn khi vật liệu có nhiều loại hạt tải hoặc hiệu ứng lượng tử đáng kể. Không dùng độ lớn điện áp Hall một mình để suy từ trường khi dòng, kích thước hoặc mật độ hạt tải chưa biết.`+reference
}
export const magneticWikiConnections={
 'tu-truong':['luc-tu-tren-dien-tich','duong-suc-tu','tu-thong','tich-co-huong','dong-dien'],
 'luc-tu-tren-dien-tich':['tu-truong','dien-tich','tich-co-huong','cong-nang-luong'],
 'duong-suc-tu':['tu-truong','tu-thong','luong-cuc-tu'],
 'tu-thong':['tu-truong','dien-thong','tich-phan'],
 'chuyen-dong-hat-trong-tu-truong':['tu-truong','luc-tu-tren-dien-tich','cong-nang-luong'],
 'bo-chon-van-toc':['dien-truong','tu-truong','khoi-pho'],
 'khoi-pho':['bo-chon-van-toc','chuyen-dong-hat-trong-tu-truong','dien-tich'],
 'momen-tu':['momen-luc','tich-co-huong','luong-cuc-tu','dong-dien'],
 'luong-cuc-tu':['momen-tu','tu-truong','cong-nang-luong','luong-cuc-dien'],
 'suat-phan-dien-dong':['suat-dien-dong','momen-tu','dien-tro','cong-nang-luong'],
 'hieu-ung-hall':['tu-truong','mat-do-dong-dien','bo-chon-van-toc','dien-the']
}
