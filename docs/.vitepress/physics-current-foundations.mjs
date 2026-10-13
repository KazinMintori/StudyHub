const reference='\n\nTài liệu tham khảo: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 25, trang 812–835.'
export const currentConcepts={
 'dan-nhiet':{name:'Dẫn nhiệt',aliases:['dẫn nhiệt','độ dẫn nhiệt'],definition:'Dẫn nhiệt là truyền năng lượng từ vùng nhiệt độ cao sang vùng nhiệt độ thấp trong một vật hoặc giữa các vật tiếp xúc. Năng lượng truyền đi mà không cần khối vật chất chuyển từ vùng này sang vùng kia.',example:'Thanh đồng và gỗ cùng ở 20°C có thể cho cảm giác khác nhau. Đồng dẫn nhiệt từ tay đi nhanh hơn nên cho cảm giác lạnh hơn, dù hai vật có cùng nhiệt độ.',use:'Hiểu liên hệ giữa chuyển động electron, tính dẫn nhiệt và tính dẫn điện của kim loại.',question:'Vật dẫn nhiệt tốt có nhất thiết nóng hơn vật dẫn nhiệt kém không?',answer:'Không. Độ dẫn nhiệt mô tả tốc độ truyền năng lượng trong một chênh lệch nhiệt độ, không tự xác định nhiệt độ của vật.'},
 'dong-dien':{name:'Dòng điện',aliases:['dòng điện','cường độ dòng điện'],definition:'Dòng điện là tốc độ điện lượng đi qua một tiết diện, $I=dQ/dt$. Đơn vị ampere bằng coulomb trên giây. Dòng điện là vô hướng, còn chiều quy ước theo chuyển động của điện tích dương.',example:'Trong một vòng mạch ổn định không có nhánh, dòng đi ra bóng đèn bằng dòng đi vào. Bóng chuyển hóa năng lượng mà không tiêu thụ điện tích.',use:'Liên hệ điện lượng, thời gian, chuyển động hạt tải và các đại lượng trong mạch.',question:'Electron phải đi từ công tắc đến bóng trước khi bóng bắt đầu sáng không?',answer:'Không. Điện trường được thiết lập dọc mạch và làm electron ở nhiều vị trí bắt đầu trôi. Thời gian truyền tác động ấy khác thời gian một electron đi hết chiều dài dây.'},
 'mat-do-dong-dien':{name:'Mật độ dòng điện',aliases:['mật độ dòng điện'],definition:'Mật độ dòng điện là vector mô tả dòng điện cục bộ. Với một loại hạt tải, $\\vec J=nq\\vec v_d$. Nếu dòng phân bố đều qua tiết diện vuông góc hướng trôi, độ lớn $J=I/A$. Đơn vị là $\\mathrm{A/m^2}$.',example:'Dòng 1,67 A trong dây có tiết diện $8.17\\times10^{-7}\\,\\mathrm{m^2}$ cho mật độ dòng khoảng $2.04\\times10^6\\,\\mathrm{A/m^2}$.',use:'Nối dòng đo trên toàn tiết diện với vận tốc trôi, trường và tính chất vật liệu tại từng điểm.',question:'Hai dây nối tiếp có cùng dòng có luôn cùng mật độ dòng không?',answer:'Không. Nếu tiết diện khác nhau, J = I/A khác nhau. Với cùng vật liệu và mật độ hạt tải, dây nhỏ hơn có tốc độ trôi lớn hơn.'},
 'dien-tro-suat':{name:'Điện trở suất',aliases:['điện trở suất'],definition:'Điện trở suất ρ là tỉ số độ lớn điện trường và mật độ dòng điện, $\\rho=E/J$. Đơn vị là ohm mét. Nó thuộc vật liệu trong điều kiện khảo sát, khác điện trở của một mẫu có hình học xác định.',example:'Đồng ở 20°C có điện trở suất đại diện $1.72\\times10^{-8}\\,\\Omega\\,\\mathrm m$. Dây dài hơn cùng tiết diện có điện trở lớn hơn dù điện trở suất không đổi.',use:'Tính điện trở từ hình học, liên hệ điện trường với mật độ dòng và xét ảnh hưởng nhiệt độ.',question:'Định nghĩa ρ = E/J có tự bảo đảm định luật Ohm không?',answer:'Không. Vật liệu chỉ tuân theo Ohm trong miền ρ không phụ thuộc độ lớn trường, với nhiệt độ và các điều kiện liên quan được giữ phù hợp.'},
 'do-dan-dien':{name:'Độ dẫn điện',aliases:['độ dẫn điện'],definition:'Độ dẫn điện σ của vật liệu là nghịch đảo điện trở suất, $\\sigma=1/\\rho$. Đơn vị SI là siemens trên mét. Vật liệu có độ dẫn điện lớn có điện trở suất nhỏ trong cùng điều kiện.',example:'Với điện trở suất đồng $1.72\\times10^{-8}\\,\\Omega\\,\\mathrm m$, độ dẫn điện khoảng $5.81\\times10^7\\,\\mathrm{S/m}$.',use:'Mô tả đáp ứng dòng điện của vật liệu theo điện trường và đổi giữa hai cách biểu diễn tính dẫn điện.',question:'σ ở đây có phải mật độ điện tích mặt không?',answer:'Không. Ký hiệu σ còn được dùng cho mật độ điện tích mặt trong tĩnh điện. Phải nhận diện đại lượng từ định nghĩa và đơn vị của bài đang xét.'},
 'dien-tro':{name:'Điện trở',aliases:['điện trở'],definition:'Điện trở R của một mẫu là tỉ số hiệu điện thế qua mẫu và dòng qua nó, $R=V/I$ với I khác không. Đơn vị SI là ohm. Mẫu trụ đồng nhất, tiết diện đều có $R=\\rho L/A$.',example:'Đoạn dây đồng dài 50,0 m, tiết diện $8.17\\times10^{-7}\\,\\mathrm{m^2}$ và điện trở suất $1.72\\times10^{-8}\\,\\Omega\\,\\mathrm m$ có điện trở khoảng 1,05 Ω.',use:'Tính dòng, sụt áp và công suất, phân biệt ảnh hưởng vật liệu với hình học mẫu.',question:'V = IR có nghĩa R luôn không đổi theo nhiệt độ hoặc điện áp không?',answer:'Không. Muốn gọi quan hệ là định luật Ohm phải có R không đổi trong các điều kiện khảo sát. Dây nóng lên hoặc linh kiện phi tuyến có thể có R thay đổi.'},
 'suat-dien-dong':{name:'Suất điện động',aliases:['suất điện động','emf'],definition:'Suất điện động ℰ là công của tác động không tĩnh điện trên mỗi đơn vị điện tích được đưa qua nguồn từ cực thế thấp lên cực thế cao. Nó có đơn vị volt, không phải đơn vị lực.',example:'Nguồn có suất điện động 12 V và điện trở trong 2 Ω cấp dòng 2 A cho tải 4 Ω. Điện áp hai cực nguồn là 8 V, nhỏ hơn suất điện động.',use:'Phân tích nguồn thực, điện áp hai cực, chiều truyền năng lượng và trạng thái nạp hoặc phóng pin.',question:'Điện áp đo giữa hai cực có luôn bằng suất điện động không?',answer:'Không. Trong mô hình nguồn thực đang phát dòng, điện áp hai cực bằng ℰ − Ir. Ở mạch hở lý tưởng, I = 0 nên hai đại lượng bằng nhau.'},
 'dien-tro-trong':{name:'Điện trở trong',aliases:['điện trở trong'],definition:'Điện trở trong r mô tả phần sụt áp và phát nhiệt bên trong một nguồn thực trong mô hình tuyến tính. Khi nguồn phát dòng I, điện áp hai cực là $V_{ab}=\\mathcal E-Ir$. Tổn hao trong là $I^2r$.',example:'Nguồn 12 V có điện trở trong 2 Ω bị ngắn mạch lý tưởng cho dòng 6 A, điện áp hai cực bằng không và công suất tỏa nhiệt trong nguồn là 72 W.',use:'Tính điện áp tải, dòng ngắn mạch và cân bằng công suất của nguồn.',question:'Có coi r là một linh kiện bên ngoài tách khỏi nguồn không?',answer:'Trong sơ đồ tương đương, r được vẽ như điện trở nối tiếp với suất điện động. Nó đại diện cho tổn hao nằm trong nguồn thực, không phải một điện trở ngoài có thể tháo riêng.'}
}
export const currentWikiDetails={
 'dan-nhiet':String.raw`Trong cơ chế dẫn nhiệt, các nguyên tử ở vùng nóng truyền một phần năng lượng cho các nguyên tử lân cận. Trong kim loại, electron tự do còn mang năng lượng từ vùng nóng đến vùng lạnh. Cơ chế electron giúp giải thích vì sao nhiều kim loại vừa dẫn nhiệt tốt vừa dẫn điện tốt.

Với thanh đồng nhất dài L, tiết diện A, hai đầu giữ ở nhiệt độ T_H và T_C với T_H > T_C, và mặt bên được cách nhiệt:

$$
\begin{aligned}
&H = \frac{dQ}{dt},\\
&H = \frac{kA(T_H-T_C)}{L}.
\end{aligned}
$$

H là tốc độ truyền nhiệt, đo bằng watt. k là độ dẫn nhiệt của vật liệu, có đơn vị W/(m·K). Q ở đây là nhiệt lượng, khác điện tích Q trong các bài điện học.

Nếu nhiệt độ biến thiên không đều theo tọa độ x dọc thanh:

$$
H=-kA\frac{dT}{dx}.
$$

Dấu âm cho hướng truyền nhiệt về phía nhiệt độ giảm. Dẫn nhiệt khác đối lưu, vốn có sự chuyển động của khối vật chất, và khác bức xạ, vốn truyền năng lượng bằng sóng điện từ mà không cần môi trường vật chất.`+'\n\nTài liệu tham khảo: Young & Freedman, ấn bản 15, mục 17.7, trang 561–562.',
 'dong-dien':String.raw`I đo lượng điện tích thuần đi qua tiết diện trong một đơn vị thời gian. Nếu I không đổi, điện lượng trong khoảng Δt bằng IΔt. Nếu dòng đổi theo thời gian, cộng các điện lượng vi phân:

$$
\Delta Q=\int_{t_1}^{t_2}I(t)\,dt.
$$

Chiều dòng quy ước theo điện tích dương. Electron trong kim loại đi ngược chiều ấy. Điện tích dương và âm chuyển ngược nhau trong dung dịch vẫn có thể đóng góp dòng cùng chiều.

Ở dòng ổn định, điện tích không tích tụ liên tục tại một phần mạch. Dòng đi vào và ra một phần tử nối tiếp bằng nhau. Điện trở và bóng đèn chuyển hóa năng lượng, không làm điện tích biến mất.

Các electron có chuyển động ngẫu nhiên rất nhanh và một vận tốc trôi nhỏ. Vận tốc trôi không phải tốc độ truyền tín hiệu hoặc tốc độ thiết lập điện trường dọc dây.`+reference,
 'mat-do-dong-dien':String.raw`Với một loại hạt tải, mật độ số n là số hạt trên một đơn vị thể tích. Điện tích mỗi hạt q có dấu, còn vector vận tốc trôi là vận tốc trung bình có hướng. Mật độ dòng là:

$$
\vec J=nq\vec v_d.
$$

Với q âm, vector vận tốc trôi ngược trường, nhưng tích nq với vector vận tốc làm J cùng chiều trường trong vật liệu dẫn đang xét. Công thức độ lớn dùng giá trị tuyệt đối của q:

$$
\begin{aligned}
&J = n|q|v_d,\\
&I = JA.
\end{aligned}
$$

Công thức I = JA cần dòng đều trên tiết diện và vector J vuông góc tiết diện. Dòng I là vô hướng, còn J là vector và có thể đổi hướng theo đường dây.

Với hai loại hạt tải, tính riêng J₁ và J₂ rồi cộng vector. Tổng quát cho N loại:

$$
\begin{aligned}
&\vec J = \vec J_1+\vec J_2+\cdots+\vec J_N,\\
&\vec J = \sum_{i=1}^{N}\vec J_i.
\end{aligned}
$$

Chỉ số i chạy qua các loại hạt. Không cộng độ lớn nếu các dòng thành phần khác hướng.`+reference,
 'dien-tro-suat':String.raw`Trong vật liệu đẳng hướng, quan hệ cục bộ giữa trường và mật độ dòng là:

$$
\vec E=\rho\vec J.
$$

Điện trở suất có thể thay đổi theo nhiệt độ, thành phần vật liệu hoặc điểm hoạt động. Định luật Ohm nói ρ không phụ thuộc độ lớn điện trường trong miền khảo sát. Định nghĩa tỉ số E/J tự nó không bảo đảm điều kiện ấy.

Với kim loại trong một khoảng nhiệt độ không quá rộng, dùng gần đúng:

$$
\rho(T)\approx\rho_0[1+\alpha(T-T_0)].
$$

ρ₀ là điện trở suất ở T₀. α thường dương ở kim loại, âm với một số vật liệu như carbon trong khoảng được xét. Bán dẫn tinh khiết có thể dẫn mạnh hơn khi nóng lên vì mật độ hạt tải tăng.

Khi chỉ thay chiều dài hoặc tiết diện mẫu mà giữ vật liệu và nhiệt độ, điện trở suất không đổi. Điện trở mẫu vẫn đổi theo R = ρL/A.`+reference,
 'do-dan-dien':String.raw`Độ dẫn điện và điện trở suất là hai cách biểu diễn cùng khả năng đáp ứng dòng của vật liệu:

$$
\begin{aligned}
&\sigma = 1/\rho,\\
&\vec J = \sigma\vec E.
\end{aligned}
$$

Quan hệ vector với một hệ số vô hướng cần vật liệu đẳng hướng. Nếu vật liệu tuân theo Ohm, σ không phụ thuộc độ lớn trường trong miền khảo sát. Đơn vị S/m khác siemens, vốn là đơn vị độ dẫn của một mẫu hoặc linh kiện.

Với mẫu trụ đồng nhất dài L, tiết diện A, điện trở là R = L/(σA). Cùng vật liệu nhưng mẫu dài hoặc mảnh hơn có điện trở lớn hơn. Khi nhiệt độ làm ρ tăng thì σ giảm, và ngược lại.

σ cũng là ký hiệu mật độ điện tích mặt trong bài tĩnh điện. Đại lượng đang nói ở đây có đơn vị S/m, còn mật độ điện tích mặt có đơn vị C/m².`+reference,
 'dien-tro':String.raw`Đối với dây đồng nhất, tiết diện đều và mật độ dòng đều:

$$
\begin{aligned}
&V = EL,\\
&I = JA,\\
&\frac VI = \rho\frac LA,\\
&R = \frac{\rho L}{A}.
\end{aligned}
$$

Giữ ρ và A, tăng chiều dài làm R tăng. Giữ ρ và L, tăng diện tích làm R giảm. Tiết diện tròn tăng theo bình phương đường kính, nên không lấy tỉ số đường kính làm tỉ số diện tích.

Định nghĩa R = V/I dùng ở một điểm hoạt động có dòng khác không. Linh kiện Ohm có R không đổi theo điện áp hoặc dòng trong điều kiện phù hợp. Điôt có quan hệ dòng và điện áp phi tuyến, nên không mô tả bằng một điện trở cố định cho mọi điểm.

Khi bỏ giãn nở hình học, điện trở biến thiên nhiệt gần như điện trở suất:

$$
R(T)\approx R_0[1+\alpha(T-T_0)].
$$

Ở nguồn giữ điện áp, R tăng làm dòng và công suất giảm. Ở nguồn giữ dòng, R tăng lại làm công suất I²R tăng. Vì vậy phải nêu điều kiện nguồn khi so hai trạng thái.`+reference,
 'suat-dien-dong':String.raw`Lực điện tĩnh đưa điện tích dương về phía điện thế thấp. Muốn duy trì một vòng dòng ổn định có điện trở, nguồn phải dùng tác động không tĩnh điện để đưa điện tích trở lại thế cao. Tác động ấy có thể bắt nguồn từ quá trình hóa học, cơ học hoặc cơ chế khác.

Với điện tích q được đưa qua nguồn:

$$
W_n=q\mathcal E.
$$

Với nguồn lý tưởng, điện áp hai cực bằng ℰ. Với nguồn có điện trở trong r đang phát dòng ra cực dương:

$$
\begin{aligned}
&V_{ab} = \mathcal E-Ir,\\
&I = \frac{\mathcal E}{R+r}.
\end{aligned}
$$

Công thức dòng cuối dùng một tải ngoài R và dây nối không có điện trở. Mạch hở có I = 0 nên V_ab = ℰ. Khi nguồn khác nạp pin và dòng đi vào cực dương, điện áp cần có là ℰ + Ir.

Tên suất điện động không có nghĩa đại lượng này là lực cơ học. Một volt bằng một joule trên coulomb, còn lực có đơn vị newton.`+reference,
 'dien-tro-trong':String.raw`Sơ đồ tương đương của nguồn thực gồm nguồn suất điện động ℰ và điện trở trong r mắc nối tiếp. Khi nguồn phát dòng, sụt áp trong là Ir. Điện áp tới tải giảm so với suất điện động.

Các công suất tương ứng là:

$$
\begin{aligned}
&P_{\mathcal E} = \mathcal EI,\\
&P_r = I^2r,\\
&P_{\mathrm{ra}} = \mathcal EI-I^2r.
\end{aligned}
$$

Khi nạp, điện trở trong vẫn tỏa nhiệt. Công suất điện vào nguồn là ℰI + I²r, trong đó ℰI chuyển thành dạng năng lượng có thể tích trữ.

Ngắn mạch lý tưởng có I = ℰ/r và điện áp hai cực bằng không. Nguồn vẫn chuyển hóa năng lượng nhưng phần ấy tỏa bên trong nguồn. Khi dòng lớn làm nguồn nóng hoặc thay đổi trạng thái, mô hình ℰ và r không đổi chỉ là gần đúng.

Hai nguồn cùng suất điện động có thể cấp dòng rất khác nhau nếu điện trở trong khác nhau. Vì vậy chỉ so điện áp ghi trên pin chưa đủ để so khả năng cấp công suất.`+reference
}
export const currentWikiConnections={
 'dan-nhiet':['nhiet-do-tuyet-doi','noi-nang','cong-nang-luong','dien-tro-suat'],
 'dong-dien':['dien-tich','mat-do-dong-dien','dien-the','suat-dien-dong'],
 'mat-do-dong-dien':['dong-dien','dien-truong','dien-tro-suat','do-dan-dien'],
 'dien-tro-suat':['dien-tro','do-dan-dien','mat-do-dong-dien','nhiet-do-tuyet-doi'],
 'do-dan-dien':['dien-tro-suat','mat-do-dong-dien','dien-truong'],
 'dien-tro':['dien-tro-suat','dong-dien','dien-the','cong-nang-luong'],
 'suat-dien-dong':['dien-the','dong-dien','dien-tro-trong','cong-nang-luong'],
 'dien-tro-trong':['suat-dien-dong','dien-tro','dong-dien','cong-nang-luong']
}
