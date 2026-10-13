const note='06-mach-dien-mot-chieu'
const d=tex=>'$$\n'+tex+'\n$$'
export const dcTopics=[
 {title:'Tổ hợp điện trở và mạch nhiều nhánh',topics:[
  {slug:'noi-tiep-song-song',title:'Điện trở nối tiếp và song song',question:'Dòng và điện áp được phân chia thế nào trong từng kiểu mắc?',source:'26.1'},
  {slug:'kirchhoff',title:'Quy tắc Kirchhoff',question:'Lập phương trình cho mạch không thu gọn được bằng nối tiếp và song song ra sao?',source:'26.2'}]},
 {title:'Đo điện, quá trình chuyển tiếp và phân phối điện',topics:[
  {slug:'dung-cu-do',title:'Dụng cụ đo điện',question:'Dụng cụ đo ảnh hưởng đến mạch như thế nào?',source:'26.3'},
  {slug:'mach-rc',title:'Mạch điện trở và tụ điện',question:'Vì sao điện tích và dòng thay đổi theo hàm mũ khi nạp hoặc phóng tụ?',source:'26.4'},
  {slug:'phan-phoi-dien',title:'Hệ thống phân phối điện',question:'Mạch nhánh, bảo vệ quá dòng và dây bảo vệ thực hiện những chức năng gì?',source:'26.5'}]}
]
export const dcSlides=[
 {note,title:'Nối tiếp giữ dòng, song song giữ điện áp',bullets:['Nối tiếp không có nhánh rẽ giữa các điện trở nên các dòng bằng nhau.','Song song nối vào cùng hai nút nên các hiệu điện thế bằng nhau.','Điện trở tương đương giữ nguyên quan hệ dòng và điện áp nhìn từ hai đầu tổ hợp.'],formula:d(String.raw`\begin{aligned}
&R_s = R_1+R_2,\\
&\frac1{R_p} = \frac1{R_1}+\frac1{R_2},\\
&R_p = \frac{R_1R_2}{R_1+R_2}.
\end{aligned}`),example:''},
 {note,title:'Quy tắc nút biểu diễn bảo toàn điện tích',bullets:['Ở trạng thái ổn định, điện tích không tích tụ liên tục tại nút.','Dòng vào và dòng ra được gán dấu trái nhau trong phương trình nút.','Kết quả dòng âm chỉ ra chiều thực ngược với chiều giả định.'],formula:d(String.raw`\begin{aligned}
&I_1+I_2-I_3 = 0,\\
&I_1+I_2 = I_3.
\end{aligned}`),example:''},
 {note,title:'Quy tắc vòng giữ nhất quán các biến thiên điện thế',bullets:['Đi dọc chiều dòng qua điện trở cho biến thiên −IR. Đi ngược chiều cho +IR.','Qua nguồn từ cực âm đến cực dương cho +ℰ, ngược lại cho −ℰ.','Chiều duyệt vòng do người giải chọn và không buộc trùng chiều dòng.'],formula:d(String.raw`\begin{aligned}
&\Delta V_1+\Delta V_2+\Delta V_3 = 0,\\
&\mathcal E-IR_1-IR_2 = 0.
\end{aligned}`),example:''},
 {note,title:'Dòng toàn thang quyết định điện trở bổ sung của dụng cụ',bullets:['Điện kế d’Arsonval có góc lệch tỉ lệ dòng trong miền hiệu chuẩn.','Điện trở rẽ song song cho phép đo dòng lớn hơn dòng toàn thang của cuộn.','Điện trở nối tiếp cho phép đo điện áp lớn hơn điện áp toàn thang của cuộn.'],formula:d(String.raw`\begin{aligned}
&R_{\mathrm{sh}} = \frac{I_GR_G}{I-I_G},\\
&R_s = \frac{V}{I_G}-R_G.
\end{aligned}`),example:''},
 {note,title:'Dụng cụ thực làm thay đổi đại lượng đang đo',bullets:['Ampe kế mắc nối tiếp và có điện trở nhỏ.','Vôn kế mắc song song và có điện trở lớn.','Chiết áp cân bằng đo suất điện động mà không lấy dòng từ nguồn cần đo ở điểm cân bằng.'],formula:d(String.raw`\begin{aligned}
&R_A \to0,\\
&R_V \to\infty,\\
&I_G = 0\quad\text{(cân bằng)}.
\end{aligned}`),example:''},
 {note,title:'Nạp tụ qua điện trở là quá trình tiến dần đến cân bằng',bullets:['Tụ ban đầu chưa tích điện, nguồn và điện trở không đổi.','Điện tích liên tục nên tụ chưa có điện áp ngay khi đóng công tắc.','Khi thời gian đủ dài, dòng bằng không và điện áp tụ bằng suất điện động nguồn.'],formula:d(String.raw`\begin{aligned}
&\tau = RC,\\
&q(t) = C\mathcal E(1-e^{-t/\tau}),\\
&i(t) = \frac{\mathcal E}{R}e^{-t/\tau}.
\end{aligned}`),example:''},
 {note,title:'Phóng tụ chuyển năng lượng điện trường thành nhiệt',bullets:['Nguồn được ngắt, tụ có điện tích đầu Q₀ và phóng qua điện trở R.','Dấu âm của dòng dùng chiều nạp làm chiều dương.','Năng lượng giảm với thời gian đặc trưng RC/2, khác thời gian giảm điện tích RC.'],formula:d(String.raw`\begin{aligned}
&q(t) = Q_0e^{-t/\tau},\\
&i(t) = -\frac{Q_0}{\tau}e^{-t/\tau},\\
&U(t) = \frac{Q_0^2}{2C}e^{-2t/\tau}.
\end{aligned}`),example:''},
 {note,title:'Mạch nhánh dùng chung điện áp và cộng dòng ở nguồn',bullets:['Các thiết bị được mắc song song để nhận cùng điện áp cấp trong mô hình.','Cầu chì và bộ ngắt bảo vệ mạch trước dòng quá mức.','Dây bảo vệ và thiết bị ngắt do chênh dòng có chức năng khác bảo vệ quá dòng.'],formula:d(String.raw`\begin{aligned}
&I = I_1+I_2\\
&\quad+\cdots+I_n,\\
&P = VI,\\
&1\,\mathrm{kW\cdot h} = 3.60\,\mathrm{MJ},\\
&1\,\mathrm{MJ} = 10^6\,\mathrm J.
\end{aligned}`),example:''}
]
export const dcCheatsheet={summary:'Định nghĩa, tính chất và công thức của tổ hợp điện trở, quy tắc Kirchhoff, dụng cụ đo và mạch R-C.',sections:[
 {id:'resistor-networks',title:'Điện trở tương đương',items:[
  {name:'Hai điện trở nối tiếp',formula:d(String.raw`\begin{aligned}
&I_1 = I_2=I,\\
&V = V_1+V_2,\\
&R_s = R_1+R_2.
\end{aligned}`),description:'Không có nhánh rẽ giữa hai điện trở. Điện trở tương đương cho cùng dòng ở cùng điện áp hai đầu.'},
  {name:'Hai điện trở song song',formula:d(String.raw`\begin{aligned}
&V_1 = V_2=V,\\
&I = I_1+I_2,\\
&\frac1{R_p} = \frac1{R_1}+\frac1{R_2},\\
&R_p = \frac{R_1R_2}{R_1+R_2}.
\end{aligned}`),description:'Hai điện trở nối cùng hai nút. Với các điện trở dương, R_p nhỏ hơn từng điện trở thành phần.'},
  {name:'n điện trở dương',formula:d(String.raw`\begin{aligned}
&R_s = R_1+R_2+\cdots+R_n,\\
&R_s = \sum_{j=1}^{n}R_j,\\
&\frac1{R_p} = \frac1{R_1}+\frac1{R_2}\\
&\quad+\cdots+\frac1{R_n},\\
&\frac1{R_p} = \sum_{j=1}^{n}\frac1{R_j}.
\end{aligned}`),description:'Chỉ số j chạy từ 1 đến n qua các điện trở của tổ hợp. Nối tiếp có cùng dòng, song song có cùng điện áp.'},
  {name:'Phân chia điện áp và dòng với hai điện trở',formula:d(String.raw`\begin{aligned}
&V_1 = V\frac{R_1}{R_1+R_2},\\
&I_1 = I\frac{R_2}{R_1+R_2}.
\end{aligned}`),description:'Công thức V₁ dùng mạch nối tiếp. Công thức I₁ dùng mạch song song, với V là điện áp toàn tổ hợp và I là dòng tổng.'}]},
 {id:'kirchhoff',title:'Quy tắc Kirchhoff',items:[
  {name:'Quy tắc nút',formula:d(String.raw`\begin{aligned}
&\widetilde I_1+\widetilde I_2+\cdots+\widetilde I_m = 0,\\
&\sum_{j=1}^{m}\widetilde I_j = 0.
\end{aligned}`),description:'m là số nhánh nối tại nút. Dòng có dấu được quy ước dương khi đi vào, âm khi đi ra, hoặc chọn toàn bộ ngược lại. Áp dụng khi nút không tích tụ điện tích.'},
  {name:'Quy tắc vòng',formula:d(String.raw`\begin{aligned}
&\Delta V_1+\Delta V_2+\cdots\\
&\quad+\Delta V_k=0,\\
&\sum_{j=1}^{k}\Delta V_j = 0.
\end{aligned}`),description:'k là số đoạn hoặc phần tử trên vòng kín. Mỗi ΔV là biến thiên điện thế theo cùng chiều duyệt vòng. Dùng trường tĩnh điện hoặc mô hình mạch tập trung không có suất điện động cảm ứng chưa được tính.'},
  {name:'Dấu biến thiên điện thế',formulaRows:[
   {label:'Qua điện trở theo chiều dòng',formula:d(String.raw`\Delta V=-IR`)},
   {label:'Qua điện trở ngược chiều dòng',formula:d(String.raw`\Delta V=+IR`)},
   {label:'Qua nguồn từ cực âm đến cực dương',formula:d(String.raw`\Delta V=+\mathcal E`)},
   {label:'Qua nguồn từ cực dương đến cực âm',formula:d(String.raw`\Delta V=-\mathcal E`)}
  ],description:'I là dòng đã xác định trong nhánh. Điện trở trong nguồn được tính riêng như một điện trở của nhánh.'}]},
 {id:'meters',title:'Dụng cụ đo điện',items:[
  {name:'Điện kế, ampe kế và vôn kế',formulaRows:[
   {label:'Điện áp toàn thang cuộn dây',formula:d(String.raw`V_G=I_GR_G`)},
   {label:'Điện trở rẽ của thang dòng I > I_G',formula:d(String.raw`R_{\mathrm{sh}}=\frac{I_GR_G}{I-I_G}`)},
   {label:'Điện trở nối tiếp của thang áp V',formula:d(String.raw`R_s=\frac V{I_G}-R_G`)}
  ],description:'R_G là điện trở cuộn điện kế và I_G là dòng toàn thang. Điện trở rẽ mắc song song, điện trở phụ vôn kế mắc nối tiếp. Các công thức dùng phần tử Ohm và cùng dòng toàn thang.'},
  {name:'Dụng cụ lý tưởng và chiết áp cân bằng',formula:d(String.raw`\begin{aligned}
&R_A = 0,\\
&R_V \to\infty,\\
&\mathcal E_x = I\rho\frac{L}{A}.
\end{aligned}`),description:'Ampe kế mắc nối tiếp, vôn kế mắc song song. Công thức chiết áp dùng dây đồng nhất tiết diện A, điện trở suất ρ, dòng I và chiều dài cân bằng L. Ở cân bằng, nguồn cần đo không cấp dòng qua điện kế.'}]},
 {id:'rc-charging',title:'Nạp tụ trong mạch R-C',items:[
  {name:'Điện tích, dòng và điện áp',formula:d(String.raw`\begin{aligned}
&\tau = RC,\\
&Q_f = C\mathcal E,\\
&q(t) = Q_f(1-e^{-t/\tau}),\\
&i(t) = \frac{\mathcal E}{R}e^{-t/\tau},\\
&V_C(t) = \mathcal E(1-e^{-t/\tau}).
\end{aligned}`),description:'Tụ ban đầu chưa tích điện. Nguồn lý tưởng có ℰ không đổi. R là tổng điện trở nối tiếp và C không đổi, t được tính từ lúc đóng mạch.'},
  {name:'Điều kiện đầu, cuối và hằng số thời gian',formula:d(String.raw`\begin{aligned}
&q(0) = 0,\\
&i(0) = \mathcal E/R,\\
&q(\infty) = C\mathcal E,\\
&i(\infty) = 0,\\
&q(\tau)/Q_f = 1-e^{-1},\\
&i(\tau)/i(0) = e^{-1}.
\end{aligned}`),description:'τ có đơn vị giây. Sau một τ, điện tích bằng khoảng 63,2% giá trị cuối, dòng còn khoảng 36,8% ban đầu.'},
  {name:'Cân bằng năng lượng từ tụ chưa tích điện',formula:d(String.raw`\begin{aligned}
&W_{\mathcal E} = C\mathcal E^2,\\
&U_f = \frac12C\mathcal E^2,\\
&W_R = \frac12C\mathcal E^2.
\end{aligned}`),description:'Dùng quá trình nạp đến trạng thái cuối qua một điện trở dương. W_ℰ là năng lượng nguồn cấp, U_f là năng lượng tụ, W_R là nhiệt tỏa ở toàn bộ điện trở nối tiếp.'}]},
 {id:'rc-discharging',title:'Phóng tụ trong mạch R-C',items:[
  {name:'Điện tích, dòng và năng lượng',formula:d(String.raw`\begin{aligned}
&q(t) = Q_0e^{-t/\tau},\\
&i(t) = -\frac{Q_0}{\tau}e^{-t/\tau},\\
&V_C(t) = \frac{Q_0}{C}e^{-t/\tau},\\
&U(t) = \frac{Q_0^2}{2C}e^{-2t/\tau}.
\end{aligned}`),description:'Nguồn đã ngắt, tụ có điện tích đầu Q₀ và phóng qua R. τ = RC. Chiều nạp được chọn dương nên dòng phóng có dấu âm. Hằng số thời gian của năng lượng bằng τ/2.'},
  {name:'Thời gian đạt một phần f của giá trị đầu',formula:d(String.raw`\begin{aligned}
&t_q = -\tau\ln f,\\
&t_U = -\frac\tau2\ln f.
\end{aligned}`),description:'0 < f < 1. t_q áp dụng cho điện tích, điện áp và độ lớn dòng. t_U áp dụng cho năng lượng còn lại.'}]},
 {id:'distribution',title:'Phân phối điện và đơn vị năng lượng',items:[
  {name:'Tải song song nhận cùng điện áp',formula:d(String.raw`\begin{aligned}
&I = I_1+I_2+\cdots+I_n,\\
&I = \sum_{j=1}^{n}I_j,\\
&P = VI.
\end{aligned}`),description:'j chạy từ 1 đến n qua các tải song song. Công thức P = VI dùng mạch một chiều. Với tải thuần trở xoay chiều, P là công suất trung bình, còn V và I là điện áp và dòng hiệu dụng.'},
  {name:'Công suất nhiệt và đơn vị kilowatt-giờ',formula:d(String.raw`\begin{aligned}
&P_R = I^2R,\\
&1\,\mathrm{kW\cdot h} = 3.60\times10^6\,\mathrm J.
\end{aligned}`),description:'Cầu chì và bộ ngắt quá dòng bảo vệ trước dòng vượt định mức. Dây bảo vệ dẫn dòng sự cố ở vỏ kim loại. Thiết bị ngắt do chênh dòng so sánh dòng đi và về, khác thiết bị bảo vệ quá dòng.'}]}
]}
