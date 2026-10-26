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
&I_G = 0.
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
\end{aligned}`),variables:[
   String.raw`$R_s$: Điện trở tương đương của hai điện trở mắc nối tiếp ($\Omega$)`,
   String.raw`$R_1, R_2$: Điện trở của từng phần tử thành phần ($\Omega$)`,
   String.raw`$I$: Cường độ dòng điện chung qua mạch nối tiếp ($I_1 = I_2 = I$) ($\mathrm{A}$)`,
   String.raw`$V$: Hiệu điện thế tổng trên toàn đoạn mạch nối tiếp ($\mathrm{V}$)`
  ],description:'Không có nhánh rẽ giữa hai điện trở. Điện trở tương đương cho cùng dòng ở cùng điện áp hai đầu.'},
  {name:'Hai điện trở song song',formula:d(String.raw`\begin{aligned}
&V_1 = V_2=V,\\
&I = I_1+I_2,\\
&\frac1{R_p} = \frac1{R_1}+\frac1{R_2},\\
&R_p = \frac{R_1R_2}{R_1+R_2}.
\end{aligned}`),variables:[
   String.raw`$R_p$: Điện trở tương đương của hai điện trở mắc song song ($\Omega$)`,
   String.raw`$V$: Hiệu điện thế chung giữa hai đầu các nhánh song song ($V_1 = V_2 = V$) ($\mathrm{V}$)`,
   String.raw`$I$: Dòng điện tổng đi vào nút phân nhánh ($I = I_1 + I_2$) ($\mathrm{A}$)`
  ],description:'Hai điện trở nối cùng hai nút. Với các điện trở dương, R_p nhỏ hơn từng điện trở thành phần.'},
  {name:'n điện trở dương',formula:"$$\n\\begin{aligned}\n&R_s=R_1+R_2+\\cdots+R_n,\\\\\n&R_s=\\sum_{j=1}^{n}R_j,\\\\\n&\\frac1{R_p}=\\frac1{R_1}+\\frac1{R_2}+\\cdots+\\frac1{R_n},\\\\\n&\\frac1{R_p}=\\sum_{j=1}^{n}\\frac1{R_j}.\n\\end{aligned}\n$$",variables:[
   String.raw`$R_s$: Điện trở tương đương của $n$ điện trở nối tiếp ($\Omega$)`,
   String.raw`$R_p$: Điện trở tương đương của $n$ điện trở song song ($\Omega$)`,
   String.raw`$R_j$: Điện trở của phần tử thứ $j$ trong tổ hợp ($\Omega$)`
  ],description:'Chỉ số j chạy từ 1 đến n qua các điện trở của tổ hợp. Nối tiếp có cùng dòng, song song có cùng điện áp.'},
  {name:'Phân chia điện áp và dòng với hai điện trở',formula:d(String.raw`\begin{aligned}
&V_1 = V\frac{R_1}{R_1+R_2},\\
&I_1 = I\frac{R_2}{R_1+R_2}.
\end{aligned}`),variables:[
   String.raw`$V_1$: Điện áp rơi trên điện trở $R_1$ trong mạch phân áp nối tiếp ($\mathrm{V}$)`,
   String.raw`$I_1$: Dòng điện chạy qua nhánh $R_1$ trong mạch phân dòng song song ($\mathrm{A}$)`,
   String.raw`$V$: Điện áp tổng đặt vào toàn bộ tổ hợp nối tiếp ($\mathrm{V}$)`,
   String.raw`$I$: Cường độ dòng điện tổng đi vào tổ hợp song song ($\mathrm{A}$)`
  ],description:'Công thức V₁ dùng mạch nối tiếp. Công thức I₁ dùng mạch song song, với V là điện áp toàn tổ hợp và I là dòng tổng.'}]},
 {id:'kirchhoff',title:'Quy tắc Kirchhoff',items:[
  {name:'Quy tắc nút',formula:d(String.raw`\begin{aligned}
&\widetilde I_1+\widetilde I_2+\cdots+\widetilde I_m = 0,\\
&\sum_{j=1}^{m}\widetilde I_j = 0.
\end{aligned}`),variables:[
   String.raw`$\widetilde I_j$: Cường độ dòng điện có dấu tại nhánh thứ $j$ nối vào nút ($\mathrm{A}$)`,
   String.raw`$m$: Số lượng các nhánh rẽ quy tụ tại nút khảo sát (Không có đơn vị)`
  ],description:'Dòng vào mang dấu dương, dòng ra mang dấu âm (hoặc ngược lại). Tổng đại số các dòng điện tại một nút bằng không.'},
  {name:'Quy tắc vòng',formula:"$$\n\\begin{aligned}\n&\\Delta V_1+\\Delta V_2+\\cdots+\\Delta V_k=0,\\\\\n&\\sum_{j=1}^{k}\\Delta V_j=0.\n\\end{aligned}\n$$",variables:[
   String.raw`$\Delta V_j$: Độ biến thiên điện thế dọc theo đoạn mạch thứ $j$ trong vòng kín ($\mathrm{V}$)`,
   String.raw`$k$: Số phần tử mạch trên vòng kín khảo sát (Không có đơn vị)`
  ],description:'Đi theo một vòng kín theo chiều tùy chọn. Tổng đại số các biến thiên điện thế bằng không.'},
  {name:'Dấu biến thiên điện thế',formulaRows:[
   {label:'Qua điện trở cùng chiều dòng',formula:d(String.raw`\Delta V=-IR`)},
   {label:'Qua điện trở ngược chiều dòng',formula:d(String.raw`\Delta V=+IR`)},
   {label:'Qua nguồn từ cực âm sang cực dương',formula:d(String.raw`\Delta V=+\mathcal E`)},
   {label:'Qua nguồn từ cực dương sang cực âm',formula:d(String.raw`\Delta V=-\mathcal E`)}
  ],variables:[
   String.raw`$\Delta V$: Biến thiên điện thế khi đi qua phần tử mạch theo chiều duyệt vòng ($\mathrm{V}$)`,
   String.raw`$I$: Cường độ dòng điện giả định trong nhánh qua điện trở $R$ ($\mathrm{A}$)`,
   String.raw`$R$: Điện trở của đoạn mạch khảo sát ($\Omega$)`,
   String.raw`$\mathcal E$: Suất điện động của nguồn điện trong nhánh ($\mathrm{V}$)`
  ],description:'Quy tắc dấu độc lập với chiều thực của dòng. Nếu giải ra dòng âm, dòng thực ngược chiều giả định.'}]},
 {id:'meters',title:'Dụng cụ đo điện',items:[
  {name:'Điện kế, ampe kế và vôn kế',formulaRows:[
   {label:'Điện áp toàn thang của cuộn dây',formula:d(String.raw`V_{\mathrm{fs}}=I_{\mathrm{fs}}R_c`)},
   {label:'Điện trở shunt cho ampe kế',formula:d(String.raw`R_{\mathrm{sh}}=\frac{I_{\mathrm{fs}}R_c}{I_{\mathrm{max}}-I_{\mathrm{fs}}}`)},
   {label:'Điện trở phụ cho vôn kế',formula:d(String.raw`R_s=\frac{V_{\mathrm{max}}}{I_{\mathrm{fs}}}-R_c`)}
  ],variables:[
   String.raw`$I_{\mathrm{fs}}$: Dòng điện lệch toàn thang của cơ cấu đo điện kế ($\mathrm{A}$)`,
   String.raw`$R_c$: Điện trở trong của cuộn dây điện kế ($\Omega$)`,
   String.raw`$V_{\mathrm{fs}}$: Điện áp rơi trên cuộn dây khi kim lệch toàn thang ($\mathrm{V}$)`,
   String.raw`$R_{\mathrm{sh}}$: Điện trở shunt mắc song song để làm ampe kế ($\Omega$)`,
   String.raw`$I_{\mathrm{max}}$: Giới hạn đo dòng điện cực đại mong muốn ($\mathrm{A}$)`,
   String.raw`$R_s$: Điện trở phụ mắc nối tiếp để làm vôn kế ($\Omega$)`,
   String.raw`$V_{\mathrm{max}}$: Giới hạn đo điện áp cực đại mong muốn ($\mathrm{V}$)`
  ],description:'Rc là điện trở cuộn dây, Ifs là dòng toàn thang. Rsh mắc song song để làm ampe kế, Rs mắc nối tiếp để làm vôn kế.'},
  {name:'Dụng cụ lý tưởng và chiết áp cân bằng',formula:d(String.raw`\begin{aligned}
&R_A \to 0,\quad R_V\to\infty,\\
&\mathcal E_x = \mathcal E_s\frac{L_x}{L_s}.
\end{aligned}`),variables:[
   String.raw`$R_A$: Điện trở của ampe kế lý tưởng ($R_A = 0$) ($\Omega$)`,
   String.raw`$R_V$: Điện trở của vôn kế lý tưởng ($R_V = \infty$) ($\Omega$)`,
   String.raw`$\mathcal E_x$: Suất điện động chưa biết cần đo bằng chiết áp cân bằng ($\mathrm{V}$)`,
   String.raw`$\mathcal E_s$: Suất điện động của pin chuẩn đã biết chính xác ($\mathrm{V}$)`,
   String.raw`$L_x, L_s$: Chiều dài đoạn dây con chạy tương ứng ở vị trí cân bằng ($\mathrm{m}$)`
  ],description:'Ampe kế lý tưởng không làm rơi áp. Vôn kế lý tưởng không lấy dòng. Chiết áp đo suất điện động không lấy dòng ở điểm cân bằng.'}]},
 {id:'rc-charging',title:'Nạp tụ trong mạch R-C',items:[
  {name:'Điện tích, dòng và điện áp',formula:d(String.raw`\begin{aligned}
&q(t) = C\mathcal E(1-e^{-t/\tau}),\\
&i(t) = \frac{\mathcal E}{R}e^{-t/\tau}=I_0e^{-t/\tau},\\
&v_C(t) = \mathcal E(1-e^{-t/\tau}).
\end{aligned}`),variables:[
   String.raw`$q(t)$: Điện tích tức thời trên tụ điện tại thời điểm $t$ ($\mathrm{C}$)`,
   String.raw`$i(t)$: Dòng điện nạp tức thời trong mạch tại thời điểm $t$ ($\mathrm{A}$)`,
   String.raw`$v_C(t)$: Hiệu điện thế tức thời trên hai bản tụ điện ($\mathrm{V}$)`,
   String.raw`$\tau$: Hằng số thời gian của mạch R-C ($\tau = RC$) ($\mathrm{s}$)`,
   String.raw`$I_0$: Dòng nạp cực đại ngay tại thời điểm đóng mạch $t = 0$ ($I_0 = \mathcal E/R$) ($\mathrm{A}$)`
  ],description:'q(0) = 0, tụ ban đầu chưa tích điện. i(0) = ℰ/R, vC(0) = 0. Sau thời gian dài: q → Cℰ, i → 0, vC → ℰ.'},
  {name:'Điều kiện đầu, cuối và hằng số thời gian',formula:d(String.raw`\begin{aligned}
&\tau = RC,\\
&q(\tau) = (1-e^{-1})Q_{\mathrm{max}}\\
&\quad\approx 0.632\,Q_{\mathrm{max}},\\
&i(\tau) = e^{-1}I_0\\
&\quad\approx 0.368\,I_0.
\end{aligned}`),variables:[
   String.raw`$\tau$: Hằng số thời gian đặc trưng cho tốc độ nạp tụ ($\mathrm{s}$)`,
   String.raw`$R$: Điện trở mạch nạp ($\Omega$)`,
   String.raw`$C$: Điện dung của tụ điện ($\mathrm{F}$)`,
   String.raw`$Q_{\mathrm{max}}$: Điện tích cực đại tụ đạt được khi nạp đầy ($C\mathcal E$) ($\mathrm{C}$)`
  ],description:'τ = RC có đơn vị giây. Sau một hằng số thời gian, tụ nạp được khoảng 63.2% điện tích cực đại.'},
  {name:'Cân bằng năng lượng từ tụ chưa tích điện',formula:d(String.raw`\begin{aligned}
&W_{\mathrm{nguon}} = C\mathcal E^2,\\
&U_C = \tfrac12 C\mathcal E^2,\\
&U_R = \tfrac12 C\mathcal E^2.
\end{aligned}`),variables:[
   String.raw`$W_{\mathrm{nguon}}$: Tổng công do nguồn điện cung cấp trong suốt quá trình nạp đầy ($\mathrm{J}$)`,
   String.raw`$U_C$: Năng lượng tĩnh điện tích lũy trong tụ khi nạp đầy ($\mathrm{J}$)`,
   String.raw`$U_R$: Năng lượng điện bị tiêu tán thành nhiệt trên điện trở trong quá trình nạp ($\mathrm{J}$)`
  ],description:'Một nửa năng lượng nguồn cung cấp tích trữ trong tụ, nửa còn lại tỏa nhiệt trên điện trở, độc lập với giá trị R.'}]},
 {id:'rc-discharging',title:'Phóng tụ trong mạch R-C',items:[
  {name:'Điện tích, dòng và năng lượng',formula:d(String.raw`\begin{aligned}
&q(t) = Q_0e^{-t/\tau},\\
&i(t) = -\frac{Q_0}{\tau}e^{-t/\tau}=I_0e^{-t/\tau},\\
&U(t) = \frac{Q_0^2}{2C}e^{-2t/\tau}.
\end{aligned}`),variables:[
   String.raw`$q(t)$: Điện tích tức thời còn lại trên tụ tại thời điểm $t$ ($\mathrm{C}$)`,
   String.raw`$Q_0$: Điện tích ban đầu của tụ điện trước khi bắt đầu phóng ($t = 0$) ($\mathrm{C}$)`,
   String.raw`$i(t)$: Dòng điện phóng tức thời qua điện trở tại thời điểm $t$ ($\mathrm{A}$)`,
   String.raw`$U(t)$: Năng lượng điện trường còn lại trong tụ tại thời điểm $t$ ($\mathrm{J}$)`
  ],description:'Q₀ là điện tích ban đầu. Dấu âm của dòng chỉ chiều phóng ngược chiều nạp. Năng lượng giảm theo thời gian đặc trưng τ/2 = RC/2.'},
  {name:'Thời gian đạt một phần f của giá trị đầu',formula:d(String.raw`t_f=\tau\ln(1/f)`),variables:[
   String.raw`$t_f$: Thời gian để điện tích tụ giảm còn một phần $f$ so với ban đầu ($\mathrm{s}$)`,
   String.raw`$f$: Tỉ số điện tích còn lại ($f = q(t)/Q_0$, với $0 < f < 1$) (Không có đơn vị)`,
   String.raw`$\tau$: Hằng số thời gian của mạch R-C ($\tau = RC$) ($\mathrm{s}$)`
  ],description:'Ví dụ: còn 50% sau t = τ ln 2 ≈ 0.693 τ; còn 10% sau t = τ ln 10 ≈ 2.303 τ.'}]},
 {id:'distribution',title:'Phân phối điện và đơn vị năng lượng',items:[
  {name:'Tải song song nhận cùng điện áp',formula:d(String.raw`\begin{aligned}
&I_{\mathrm{tong}} = I_1+I_2+\cdots+I_n,\\
&P_{\mathrm{tong}} = P_1+P_2+\cdots+P_n.
\end{aligned}`),variables:[
   String.raw`$I_{\mathrm{tong}}$: Tổng cường độ dòng điện cấp từ nguồn chính ($\mathrm{A}$)`,
   String.raw`$I_j$: Cường độ dòng điện qua nhánh tải thứ $j$ ($\mathrm{A}$)`,
   String.raw`$P_{\mathrm{tong}}$: Tổng công suất điện tiêu thụ của toàn bộ hệ thống ($\mathrm{W}$)`
  ],description:'Các thiết bị trong mạng điện gia đình mắc song song để hoạt động độc lập ở cùng điện áp định mức.'},
  {name:'Công suất nhiệt và đơn vị kilowatt-giờ',formula:d(String.raw`\begin{aligned}
&P = VI = I^2R = \frac{V^2}{R},\\
&1\,\mathrm{kW\cdot h} = 3.60\times 10^6\,\mathrm J\\
&\quad= 3.60\,\mathrm{MJ}.
\end{aligned}`),variables:[
   String.raw`$P$: Công suất tiêu thụ của thiết bị điện ($\mathrm{W}$ hoặc $\mathrm{kW}$)`,
   String.raw`$V$: Điện áp làm việc của mạng điện ($\mathrm{V}$)`,
   String.raw`$1\,\mathrm{kW\cdot h}$: Đơn vị năng lượng điện thương dụng kilowatt-giờ ($\approx 3{,}60\times10^6\,\mathrm{J}$)`
  ],description:'Kilowatt-giờ là đơn vị năng lượng, không phải công suất. 1 kW·h bằng năng lượng tiêu thụ với công suất 1 kW trong 1 giờ.'}]}
]}
