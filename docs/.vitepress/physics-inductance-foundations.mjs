const term=(name,aliases,definition,example,use,question,answer)=>({name,aliases:[name,...aliases],definition,example,use,question,answer})
const ref='\n\nTài liệu tham khảo: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 30, trang 988–1009.'
export const inductanceConcepts={
 'tu-thong-moc-vong':term('Từ thông móc vòng',['từ thông móc vòng'],String.raw`Từ thông móc vòng của một cuộn là tổng từ thông có dấu qua các vòng theo các chiều đã chọn. Nếu N vòng có từ thông trung bình $\Phi$ thì từ thông móc vòng bằng $N\Phi$.`,String.raw`Cuộn 20 vòng, mỗi vòng có từ thông trung bình $3\,\mu\mathrm{Wb}$, có từ thông móc vòng $60\,\mu\mathrm{Wb}$.`,'Định nghĩa hỗ cảm, tự cảm và suất điện động của cuộn.','Từ thông móc vòng có phải từ thông của riêng một vòng không?','Không. Nó tính đóng góp của tất cả các vòng theo chiều nhất quán.'),
 'ho-cam':term('Hỗ cảm',['hỗ cảm','hệ số hỗ cảm','mutual inductance'],String.raw`Hỗ cảm M liên hệ dòng ở một mạch với từ thông móc vòng ở mạch khác: $N_2\Phi_{B2}=Mi_1$. Trong mô hình hình học cố định, môi trường từ tuyến tính thuận nghịch, cùng M dùng khi đổi vai hai mạch.`,String.raw`Hai cuộn có $M=4\,\mathrm{mH}$. Dòng nguồn tăng $2\,\mathrm{A/s}$ gây suất điện động độ lớn $8\,\mathrm{mV}$ ở cuộn kia.`,'Phân tích hai cuộn ghép từ, máy biến áp và cảm ứng không tiếp xúc.','Hỗ cảm và tự cảm có mô tả cùng một từ thông nguồn không?','Không. Hỗ cảm liên hệ hai mạch, tự cảm liên hệ dòng và từ thông của chính một mạch.'),
 'tu-cam':term('Tự cảm',['tự cảm','độ tự cảm','điện cảm','self-inductance'],String.raw`Tự cảm L là hệ số liên hệ dòng với từ thông móc vòng do chính dòng ấy tạo ra: $N\Phi_B=Li$. Với L không đổi, suất điện động tự cảm là $\mathcal E_L=-L\,di/dt$.`,String.raw`Cuộn $L=20\,\mathrm{mH}$ có dòng tăng $3\,\mathrm{A/s}$ tạo suất điện động tự cảm độ lớn $60\,\mathrm{mV}$.`,'Tính điện áp, năng lượng và quá trình chuyển tiếp của mạch có cuộn.','Dòng lớn nhưng không đổi có suất điện động tự cảm trong cuộn tuyến tính cố định không?','Không. Suất điện động phụ thuộc tốc độ biến thiên dòng.'),
 'cuon-cam':term('Cuộn cảm',['cuộn cảm','inductor'],String.raw`Cuộn cảm là phần tử được chế tạo để có tự cảm xác định. Với cuộn lý tưởng, điện áp theo quy ước thụ động là $v_L=L\,di/dt$, điện trở dây quấn được bỏ qua.`,String.raw`Dòng dương đang giảm làm điện áp cuộn theo chiều dòng âm. Cuộn đang nhả năng lượng cho phần còn lại của mạch.`,'Đọc sơ đồ mạch và chọn dấu điện áp khi áp dụng Kirchhoff.','Dòng cuộn có thể nhảy tức thời khi điện áp đặt vào chỉ hữu hạn không?','Không nếu L khác không. Đạo hàm dòng có thể nhảy, còn dòng liên tục.'),
 'nang-luong-tu-truong':term('Năng lượng từ trường',['năng lượng từ trường','năng lượng cuộn cảm'],String.raw`Từ trường có năng lượng. Với cuộn tuyến tính tự cảm không đổi, năng lượng là $U_B=Li^2/2$. Khi dòng thay đổi, cuộn trao đổi công suất $Li\,di/dt$ với mạch.`,String.raw`Cuộn $0{,}10\,\mathrm H$ mang dòng $2\,\mathrm A$ chứa năng lượng $0{,}20\,\mathrm J$.`,'Phân tích tích trữ, phóng năng lượng và dao động điện.','Đổi chiều dòng nhưng giữ độ lớn có làm năng lượng cuộn đổi không?','Không trong mô hình L không đổi, vì năng lượng phụ thuộc bình phương dòng.'),
 'mat-do-nang-luong-tu-truong':term('Mật độ năng lượng từ trường',['mật độ năng lượng từ trường'],String.raw`Mật độ năng lượng từ trường là năng lượng trên một đơn vị thể tích. Trong chân không, $u_B=B^2/(2\mu_0)$. Trong vật liệu tuyến tính có độ từ thẩm không đổi, dùng $u_B=B^2/(2\mu)$.`,String.raw`Nếu cùng một môi trường có cảm ứng từ tăng gấp đôi, mật độ năng lượng tăng gấp bốn.`,'Tính năng lượng phân bố trong vùng có từ trường.','Giữ B cố định và giữ dòng cố định có cho cùng cách so sánh năng lượng hai lõi từ không?','Không. Với dòng cố định, B cũng thay đổi theo độ từ thẩm.'),
 'mach-rl':term('Mạch RL',['mạch RL','mạch R-L'],String.raw`Mạch RL chứa điện trở và cuộn cảm. Khi nối nguồn không đổi vào mạch ban đầu không dòng, dòng tiến về $\mathcal E/R$. Khi tách nguồn nhưng giữ vòng kín, dòng suy giảm theo hàm mũ.`,String.raw`Ngay sau đóng nguồn vào cuộn chưa có dòng, điện trở chưa có điện áp và cuộn nhận toàn bộ điện áp nguồn.`,'Phân tích đóng, ngắt nguồn và các mạch có cuộn thực.','Dòng cuối của mạch RL nối nguồn một chiều không đổi phụ thuộc L không?','Không trong mô hình đã cho. L quyết định thời gian tiến đến giá trị cuối.'),
 'hang-so-thoi-gian-rl':term('Hằng số thời gian RL',['hằng số thời gian RL','hằng số thời gian R-L'],String.raw`Hằng số thời gian RL là $\tau=L/R$, với R là tổng điện trở trong vòng. Sau một $\tau$, dòng tăng từ không đạt khoảng 63,2% giá trị cuối, còn dòng suy giảm còn khoảng 36,8% giá trị đầu.`,String.raw`Cuộn $L=0{,}20\,\mathrm H$ trong vòng $R=10\,\Omega$ có $\tau=20\,\mathrm{ms}$.`,'Ước lượng và tính thời gian chuyển tiếp của RL.','Thời gian giảm nửa dòng có bằng một hằng số thời gian không?',String.raw`Không. Nó bằng $\tau\ln2$.`),
 'mach-lc':term('Mạch LC',['mạch LC','mạch L-C','dao động LC'],String.raw`Mạch LC lý tưởng gồm cuộn cảm và tụ, không hao phí năng lượng. Điện tích và dòng dao động điều hòa với $\omega_0=1/\sqrt{LC}$, trao đổi năng lượng giữa điện trường tụ và từ trường cuộn.`,String.raw`Khi tụ vừa phóng hết điện tích, dòng qua cuộn có độ lớn cực đại và toàn bộ năng lượng nằm trong từ trường.`,'Phân tích dao động tự do, tần số và năng lượng điện.','Dòng dừng ngay khi tụ hết điện tích trong mạch LC không?','Không. Dòng tiếp tục và nạp tụ với cực tính ngược.'),
 'mach-rlc':term('Mạch RLC nối tiếp',['mạch RLC','mạch RLC nối tiếp','mạch L-R-C'],String.raw`Mạch RLC nối tiếp tự do có phương trình $Lq''+Rq'+q/C=0$. Điện trở tiêu tán năng lượng. Hệ dao động tắt dần khi $R^2<4L/C$, tới hạn khi bằng nhau và quá tắt dần khi lớn hơn.`,String.raw`Dòng đầu bằng không trong mạch có điện trở vẫn yêu cầu chọn pha bù đạo hàm của bao hàm mũ, thay vì đặt pha bằng không.`,'Phân loại đáp ứng điện và áp điều kiện đầu.','Nghiệm cosin nhân hàm mũ có dòng đầu bằng không khi tự đặt pha bằng không không?','Nói chung không, vì đạo hàm hàm mũ tạo thêm một số hạng.'),
 'tat-dan-toi-han':term('Tắt dần tới hạn',['tắt dần tới hạn','critical damping'],String.raw`Tắt dần tới hạn là ngưỡng giữa dao động tắt dần và quá tắt dần. Với RLC nối tiếp, $R=2\sqrt{L/C}$. Nghiệm điện tích có dạng $(a+bt)e^{-Rt/(2L)}$.`,String.raw`Với điện tích đầu dương và dòng đầu bằng không, nghiệm tới hạn trở về không mà không dao động lặp lại.`,'Nhận biết ngưỡng không dao động và chọn nghiệm chuyển tiếp.','Không dao động có luôn nghĩa không thể đổi dấu dù điều kiện đầu bất kỳ không?','Không. Điều kiện đầu phù hợp có thể tạo một lần đổi dấu, nhưng không dao động lặp lại.'),
 'qua-tat-dan':term('Quá tắt dần',['quá tắt dần','overdamping'],String.raw`Quá tắt dần xảy ra khi điện trở RLC thỏa $R^2>4L/C$. Phương trình đặc trưng có hai nghiệm thực âm, nên nghiệm là tổng hai hàm mũ suy giảm và không dao động lặp lại.`,String.raw`Tăng R rất lớn có thể làm một thành phần nghiệm suy giảm chậm, dù năng lượng vẫn mất trên điện trở.`,'Chọn nghiệm RLC và phân biệt dao động với suy giảm thuần túy.','Có tần số dao động thực để dùng 2π/ωd trong miền quá tắt dần không?','Không. Dạng tần số dưới tắt dần có biểu thức dưới căn âm trong miền này.')
}
export const inductanceWikiDetails={
 'tu-thong-moc-vong':String.raw`Với hai vòng, từ thông móc vòng là tổng có dấu của từ thông qua vòng thứ nhất và thứ hai. Tổng quát cho N vòng:

$$
\begin{aligned}
\Lambda&=\Phi_1+\Phi_2+\dots+\Phi_N\\
&=\sum_{k=1}^{N}\Phi_k\\
&=N\overline\Phi.
\end{aligned}
$$

Chỉ số k chạy qua tất cả các vòng. Từ thông trung bình không có nghĩa mọi vòng đều nhận từ thông như nhau. Nếu phần đầu cuộn có trường yếu hơn, vẫn dùng trung bình để biểu diễn tổng.

Với các chiều vòng được chọn nhất quán theo đường dây, Faraday cho suất điện động tổng bằng số đối đạo hàm Λ. Khi các vòng nối đối chiều, phải tính dấu trước khi cộng. Đơn vị vẫn là weber vì số vòng không thứ nguyên.`+ref,
 'ho-cam':String.raw`Chọn chiều dòng và chiều từ thông của hai cuộn trước khi dùng một hệ số hỗ cảm có dấu. Trong mô hình cố định, tuyến tính, từ thông móc vòng do cuộn 1 gây ra ở cuộn 2 là $\Lambda_2=Mi_1$. Lấy đạo hàm rồi áp dụng Faraday cho

$$
\mathcal E_2=-M\frac{di_1}{dt}.
$$

Tính đối xứng $M_{12}=M_{21}$ cần mô hình môi trường thuận nghịch phù hợp. Nó không yêu cầu số vòng hoặc kích thước hai cuộn bằng nhau. Hai từ thông trung bình mỗi vòng vẫn có thể khác nhau.

Với hai cuộn nối tiếp có trường hỗ trợ, tự cảm bộ bằng $L_1+L_2+2M$. Trường đối nhau cho $L_1+L_2-2M$, khi M là độ lớn hỗ cảm theo quy ước đó. Không được bỏ hỗ cảm khi hai cuộn có liên kết từ đáng kể. Với môi trường phi tuyến, từ thông không còn là một hàm tuyến tính của dòng và hệ số hằng phải được thay bằng mô hình thích hợp.`+ref,
 'tu-cam':String.raw`Dòng tạo từ thông qua chính mạch, nên sự thay đổi dòng gây suất điện động trong mạch ấy. Giữ hình học và môi trường tuyến tính để viết $\Lambda=Li$. Nếu L hằng, Faraday cho $\mathcal E_L=-L\,di/dt$.

Điện áp đầu cuộn theo quy ước thụ động có dấu đối với suất điện động tự cảm đi dọc chiều dòng:

$$
\begin{aligned}
v_{ab}&=V_a-V_b\\
&=L\frac{di}{dt}.
\end{aligned}
$$

Dòng dương đi từ a đến b. Khi nó tăng, đầu a cao thế hơn b. Khi nó giảm, đầu b cao thế hơn a và cuộn nhả năng lượng. Cuộn thực có thể được mô hình bằng điện trở dây quấn nối tiếp tự cảm. Khi ấy điện áp tổng còn chứa số hạng Ri.

Tự cảm không chống dòng không đổi. Nó liên hệ với năng lượng của từ trường và chống thay đổi dòng. Nếu L phụ thuộc thời gian hoặc từ hóa phi tuyến, không được lấy L ra ngoài đạo hàm mà thiếu điều kiện.`+ref,
 'cuon-cam':String.raw`Với cuộn lý tưởng, bỏ qua điện trở dây quấn, nhưng giữ tự cảm. Nguồn ngoài phải cấp công để tăng năng lượng từ trường. Với dòng dương,

$$
\begin{aligned}
p_L&=v_Li\\
&=Li\frac{di}{dt}\\
&=\frac{d}{dt}\left(\frac12Li^2\right).
\end{aligned}
$$

Công suất dương nghĩa cuộn nhận năng lượng, âm nghĩa cuộn trả năng lượng. Dấu này không được suy chỉ từ dấu dòng, mà cần cả điện áp.

Tích phân điện áp qua thời gian chuyển mạch cho $\Delta i=(1/L)\int v_Ldt$. Điện áp hữu hạn trong một khoảng tiến về không không tạo bước nhảy dòng. Một xung điện áp lý tưởng có diện tích hữu hạn có thể tạo bước nhảy trong mô hình, nhưng khác trường hợp chuyển mạch với điện áp hữu hạn.

Chấn lưu từ và các mạch hạn chế biến thiên dòng dùng tính chất này. Cần tính thêm điện trở, tổn hao vật liệu và giới hạn tuyến tính khi mô tả một cuộn thực.`+ref,
 'nang-luong-tu-truong':String.raw`Công suất nạp cuộn lý tưởng là $p=Li\,di/dt$. Tích phân từ dòng không đến i cho

$$
\begin{aligned}
U_B&=\int_0^i Lu\,du\\
&=\frac12Li^2.
\end{aligned}
$$

Biến tích phân u là giá trị dòng chạy từ 0 đến i. Công thức đòi hỏi L không đổi. Năng lượng không âm với L dương và không đổi khi đảo dấu dòng.

Trong vòng RL tách nguồn, năng lượng này cấp cho điện trở. Khi dòng giảm theo $e^{-t/\tau}$, năng lượng giảm theo $e^{-2t/\tau}$. Trong mạch LC lý tưởng, năng lượng từ trao đổi với năng lượng điện của tụ, tổng không đổi.

Với vật liệu từ phi tuyến, phải tích phân quan hệ từ thông và dòng phù hợp. Không được tự thay một tự cảm phụ thuộc dòng vào Li²/2 và coi đó là kết quả tổng quát.`+ref,
 'mat-do-nang-luong-tu-truong':String.raw`Trong chân không, năng lượng từ trường trên thể tích được mô tả bởi $u_B=B^2/(2\mu_0)$. Tổng năng lượng trong một vùng là

$$
U_B=\int_{\mathcal V}u_B\,d\mathcal V.
$$

Nếu trường đều, tích phân trở thành mật độ nhân thể tích. Trong vật liệu tuyến tính có độ từ thẩm không đổi, dùng $u_B=B^2/(2\mu)$.

Giữ $B$ cố định, tăng $\mu$ làm mật độ này nhỏ đi. Nhưng giữ dòng ở cùng một ống dây thì $B=\mu nI$ và mật độ trở thành $\mu n^2I^2/2$, tăng theo $\mu$. Hai kết luận khác nhau vì giữ các đại lượng khác nhau.

Với từ trễ hoặc độ từ thẩm thay đổi theo trường, biểu thức dùng $\mu$ hằng không mô tả đầy đủ trao đổi năng lượng vật liệu.`+ref,
 'mach-rl':String.raw`Trong mạch nối nguồn hằng, R biểu diễn tổng điện trở trong vòng. Định luật vòng cho

$$
L\frac{di}{dt}+Ri=\mathcal E.
$$

Với dòng đầu bằng không, nghiệm là $i=(\mathcal E/R)(1-e^{-tR/L})$. Dòng đầu bằng không nhưng đạo hàm đầu bằng $\mathcal E/L$. Dòng cuối bằng $\mathcal E/R$ và không phụ thuộc L.

Khi tách nguồn nhưng vẫn giữ vòng RL kín, nghiệm trở thành $i=I_0e^{-tR/L}$. Dòng đầu I0 được lấy từ ngay trước chuyển mạch vì dòng cuộn liên tục dưới điện áp hữu hạn.

Với mạch phân nhánh, R trong hằng số thời gian không tự động bằng tổng tất cả điện trở trên hình. Phải lập Kirchhoff hoặc tìm điện trở hiệu dụng mà cuộn nhìn thấy, đồng thời giữ đúng điều kiện đầu.`+ref,
 'hang-so-thoi-gian-rl':String.raw`Từ nghiệm mũ, thời gian đặc trưng RL là $\tau=L/R$. Đơn vị henry bằng ohm nhân giây, nên $\tau$ đo bằng giây.

Sau $\tau$, dòng suy giảm còn $e^{-1}$ giá trị đầu. Dòng tăng từ không còn thiếu $e^{-1}$ phần giá trị cuối. Thời gian còn một tỉ phần f của dòng đầu là

$$
t=-\tau\ln f,
$$

với 0<f<1. Nếu hỏi năng lượng còn tỉ phần f, thời gian là $-(\tau/2)\ln f$ vì năng lượng phụ thuộc bình phương dòng.

Một hằng số thời gian không có nghĩa hệ đã hoàn toàn ổn định. Mức gần trạng thái cuối phải gắn với sai số yêu cầu.`+ref,
 'mach-lc':String.raw`Chọn q là điện tích trên một bản tụ và i dương đi vào bản đó, nên $i=dq/dt$. Định luật vòng cho $Lq''+q/C=0$. Nghiệm điện tích có dạng

$$
\begin{aligned}
q&=Q\cos(\omega_0t+\phi),\\
i&=-\omega_0Q\sin(\omega_0t+\phi),\\
\omega_0&=\frac1{\sqrt{LC}}.
\end{aligned}
$$

Điện tích và dòng lệch pha một phần tư chu kỳ. Hai điều kiện đầu quyết định biên độ và pha. Dòng âm trong giai đoạn phóng chỉ nghĩa dòng thực ngược chiều dương đã chọn.

Tổng $q^2/(2C)+Li^2/2$ không đổi. Cơ chế giống trao đổi thế năng lò xo và động năng vật nặng, với q tương ứng li độ, i tương ứng vận tốc, L tương ứng khối lượng và 1/C tương ứng độ cứng lò xo.`+ref,
 'mach-rlc':String.raw`Mạch nối tiếp tự do có $Lq''+Rq'+q/C=0$, với i=q'. Tổng năng lượng thỏa $dU/dt=-Ri^2$ nên không tăng khi R dương.

Trong miền dưới tắt dần, đặt $\alpha=R/(2L)$ và $\omega_d=\sqrt{1/(LC)-\alpha^2}$. Nghiệm là cosin nhân bao mũ. Điều kiện đầu phải tính đạo hàm của cả hai thừa số:

$$
\begin{aligned}
q(0)&=A\cos\phi,\\
i(0)&=-\alpha q(0)\\
&\quad-\omega_dA\sin\phi.
\end{aligned}
$$

Vì vậy i(0)=0 không cho phép đặt φ=0 tùy ý. Với q0 khác không, pha phải bù số hạng suy giảm biên độ.

Khi R² bằng 4L/C, nghiệm tới hạn không dao động hình sin. Khi R² lớn hơn, nghiệm là tổng hai mũ thực giảm. Chu kỳ 2π/ωd chỉ dùng khi ωd thực và khác không.`+ref,
 'tat-dan-toi-han':String.raw`Ngưỡng tới hạn RLC được xác định bởi nghiệm kép của phương trình đặc trưng. Với $R^2=4L/C$, tốc độ suy giảm là $\alpha=R/(2L)$ và

$$
q(t)=(a+bt)e^{-\alpha t}.
$$

Điện tích đầu $q_0$ cho $a=q_0$. Dòng đầu $i_0$ cho $b=i_0+\alpha q_0$. Với $i_0=0$ và $q_0$ dương, điện tích giữ dấu dương rồi tiến về không. Với dòng đầu khác không, $a+bt$ có thể bằng không một lần.

Hệ không có các lần đổi dấu lặp lại như dao động. Kết luận không dao động phải được phân biệt với kết luận không bao giờ đổi dấu dưới mọi điều kiện đầu.`+ref,
 'qua-tat-dan':String.raw`Với $R^2>4L/C$, đặt các hệ số

$$
\begin{aligned}
\alpha&=\frac{R}{2L},\\
\delta&=\sqrt{\alpha^2-\frac1{LC}},\\
\alpha_1&=\alpha-\delta,\\
\alpha_2&=\alpha+\delta.
\end{aligned}
$$

Hai tốc độ suy giảm đều dương. Khi ấy

$$
q(t)=ae^{-\alpha_1t}+be^{-\alpha_2t}.
$$

Các nghiệm đặc trưng là $-\alpha_1,-\alpha_2$. Hệ không có thành phần lượng giác với tần số thực. Một trong hai tốc độ có thể nhỏ khi điện trở rất lớn, nên đuôi đáp ứng tiến về không chậm.

Hai hệ số a,b phụ thuộc điện tích và dòng đầu. Chúng có thể khác dấu, nên nghiệm có thể đổi dấu một lần. Điều đó không tạo chu kỳ dao động và không cho phép dùng công thức thời gian theo một chu kỳ LC.`+ref
}
export const inductanceWikiConnections={
 'tu-thong-moc-vong':['tu-thong','ho-cam','tu-cam'],
 'ho-cam':['tu-thong-moc-vong','dinh-luat-faraday','tu-cam'],
 'tu-cam':['cuon-cam','ho-cam','nang-luong-tu-truong'],
 'cuon-cam':['tu-cam','quy-tac-kirchhoff','mach-rl'],
 'nang-luong-tu-truong':['tu-cam','mat-do-nang-luong-tu-truong','mach-lc'],
 'mat-do-nang-luong-tu-truong':['nang-luong-tu-truong','do-tu-tham','mat-do-nang-luong-dien-truong'],
 'mach-rl':['cuon-cam','hang-so-thoi-gian-rl','quy-tac-kirchhoff'],
 'hang-so-thoi-gian-rl':['mach-rl','mach-rc','nang-luong-tu-truong'],
 'mach-lc':['dien-dung','tu-cam','dao-dong-dieu-hoa'],
 'mach-rlc':['mach-lc','dao-dong-tat-dan','tat-dan-toi-han','qua-tat-dan'],
 'tat-dan-toi-han':['mach-rlc','dao-dong-tat-dan','qua-tat-dan'],
 'qua-tat-dan':['mach-rlc','tat-dan-toi-han','dao-dong-tat-dan']
}
