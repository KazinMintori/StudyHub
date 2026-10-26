const note='10-tu-cam'
const display=s=>`$$\n${s}\n$$`
export const inductanceTopics=[{title:'Điện cảm, năng lượng và quá trình chuyển tiếp',topics:[
 {slug:'ho-cam',title:'Hỗ cảm',question:'Dòng ở một cuộn tạo suất điện động trong cuộn khác như thế nào?',source:'30.1'},
 {slug:'tu-cam-cuon-cam',title:'Tự cảm và cuộn cảm',question:'Vì sao điện áp cuộn phụ thuộc tốc độ biến thiên dòng?',source:'30.2'},
 {slug:'nang-luong-tu-truong',title:'Năng lượng từ trường',question:'Công để thiết lập dòng được tích trữ ở đâu?',source:'30.3'},
 {slug:'mach-rl',title:'Mạch RL',question:'Dòng tăng và giảm theo quy luật nào khi chuyển công tắc?',source:'30.4'},
 {slug:'mach-lc',title:'Mạch LC',question:'Vì sao tụ và cuộn tạo dao động điện?',source:'30.5'},
 {slug:'mach-rlc',title:'Mạch RLC nối tiếp',question:'Điện trở quyết định dao động hay suy giảm không dao động ra sao?',source:'30.6'}
]}]
const slide=(title,bullets,formula='')=>({note,title,bullets,formula})
export const inductanceSlides=[
 slide('Hỗ cảm liên hệ hai mạch qua từ thông',[
  'Dòng biến thiên ở cuộn nguồn làm từ thông qua cuộn nhận thay đổi.',
  'Từ thông trong định nghĩa là trung bình một vòng, còn từ thông móc vòng có tính số vòng.',
  'Hỗ cảm không đổi cần hình học cố định và môi trường từ tuyến tính.'
 ],display(String.raw`\begin{aligned}&N_2\Phi_{B2}=Mi_1\\&\mathcal E_2=-M\frac{di_1}{dt}.\end{aligned}`)),
 slide('Đổi vai hai cuộn vẫn cho cùng hỗ cảm',[
  'Trong mô hình môi trường từ tuyến tính thuận nghịch, M12 bằng M21.',
  'Từ thông một vòng ở hai cuộn không nhất thiết bằng nhau.',
  'Dòng không đổi không tạo suất điện động hỗ cảm trong cấu hình cố định.'
 ],display(String.raw`\begin{aligned}&M=\frac{N_2\Phi_{B2}}{i_1}\\&\quad=\frac{N_1\Phi_{B1}}{i_2}.\end{aligned}`)),
 slide('Tự cảm chống sự thay đổi dòng',[
  'Mạch mang dòng biến thiên tạo suất điện động qua biến thiên từ thông của chính nó.',
  'Dấu Lenz chống biến thiên dòng, không nhất thiết chống chiều dòng.',
  'Hệ số L là hằng trong mô hình cuộn tuyến tính, hình học cố định.'
 ],display(String.raw`\begin{aligned}&L=\frac{N\Phi_B}{i}\\&\mathcal E_L=-L\frac{di}{dt}.\end{aligned}`)),
 slide('Dấu điện áp cuộn phải đi với chiều dòng',[
  'Điện áp thụ động là điện thế đầu dòng đi vào trừ điện thế đầu dòng đi ra.',
  'Dòng dương tăng làm cuộn nhận năng lượng, còn dòng dương giảm làm cuộn nhả năng lượng.',
  'Với điện áp hữu hạn và L khác không, dòng cuộn liên tục khi chuyển mạch.'
 ],display(String.raw`v_L=L\frac{di}{dt}`)),
 slide('Năng lượng cuộn nằm trong từ trường',[
  'Tích phân công suất nạp cuộn cho năng lượng tỷ lệ bình phương dòng.',
  'Công thức mật độ trong vật liệu cần độ từ thẩm không đổi.',
  'Dòng đổi dấu nhưng giữ độ lớn không làm năng lượng từ trường đổi.'
 ],display(String.raw`\begin{aligned}&U_B=\frac12Li^2\\&u_B=\frac{B^2}{2\mu}.\end{aligned}`)),
 slide('Dòng RL tăng về giá trị do điện trở quyết định',[
  'Cuộn ban đầu không dòng nhận toàn bộ điện áp nguồn ngay sau đóng.',
  'Hằng số thời gian quyết định tốc độ tăng, còn dòng cuối không phụ thuộc L.',
  'Sau một hằng số thời gian, dòng đạt khoảng 63,2% giá trị cuối.'
 ],display(String.raw`\begin{aligned}&\tau=\frac LR\\&I_\infty=\frac{\mathcal E}{R}\\&i=I_\infty(1-e^{-t/\tau}).\end{aligned}`)),
 slide('Tách nguồn làm dòng giảm liên tục',[
  'Dòng ngay sau chuyển bằng dòng ngay trước chuyển.',
  'Cuộn cấp năng lượng từ trường cho điện trở trong vòng kín.',
  'Năng lượng giảm với hệ số mũ gấp đôi hệ số của dòng.'
 ],display(String.raw`\begin{aligned}&i=I_0e^{-t/\tau}\\&U_B=U_0e^{-2t/\tau}.\end{aligned}`)),
 slide('LC trao đổi năng lượng giữa tụ và cuộn',[
  'Dòng không dừng khi tụ vừa hết điện tích, nên tụ tiếp tục được nạp với cực tính ngược.',
  'Trong mạch lý tưởng, tổng năng lượng không đổi.',
  'Quy ước i bằng đạo hàm q đòi hỏi dòng dương đi vào bản có điện tích q.'
 ],display(String.raw`\begin{aligned}&Lq''+\frac qC=0\\&\omega_0=\frac1{\sqrt{LC}}.\end{aligned}`)),
 slide('Dòng và điện tích LC lệch pha một phần tư chu kỳ',[
  'Biên độ và pha được xác định bởi điện tích và dòng ban đầu.',
  'Tại cực đại điện tích, dòng bằng không. Khi điện tích bằng không, độ lớn dòng cực đại.',
  'Điện tích âm cho biết bản tụ đã chọn có cực tính ngược với ban đầu.'
 ],display(String.raw`\begin{aligned}&q=Q\cos(\omega_0t+\phi)\\&i=-\omega_0Q\sin(\omega_0t+\phi).\end{aligned}`)),
 slide('RLC cần đồng thời xét pha và suy giảm biên độ',[
  'Điện trở tiêu tán năng lượng và làm tần số dưới tắt dần giảm.',
  'Dòng đầu bằng không không cho phép tự đặt pha cosin bằng không khi R khác không.',
  'Hệ số suy giảm biên độ là R trên 2L.'
 ],display(String.raw`\begin{aligned}&\alpha=\frac{R}{2L}\\&\omega_d=\sqrt{\frac1{LC}-\alpha^2}\\&q=Ae^{-\alpha t}\cos(\omega_dt+\phi).\end{aligned}`)),
 slide('Ngưỡng điện trở phân biệt ba chế độ',[
  'Dưới ngưỡng tới hạn, hệ có dao động tắt dần.',
  'Tại ngưỡng, nghiệm tới hạn không còn phần dao động hình sin.',
  'Trên ngưỡng, nghiệm là tổng hai hàm mũ thực suy giảm.'
 ],display(String.raw`\begin{aligned}&R_{\mathrm{th}}=2\sqrt{\frac LC}\\&R<R_{\mathrm{th}}\\&R=R_{\mathrm{th}}\\&R>R_{\mathrm{th}}.\end{aligned}`))
]
export const inductanceCheatsheet={title:'Cheatsheet: Điện cảm',lead:'Định nghĩa, tính chất, công thức và điều kiện của hỗ cảm, tự cảm, năng lượng từ trường và các mạch RL, LC, RLC.',sections:[
 {id:'mutual',title:'Hỗ cảm',items:[
  {name:'Từ thông móc vòng và hỗ cảm',formula:display(String.raw`\begin{aligned}&N_2\Phi_{B2}=Mi_1\\&N_1\Phi_{B1}=Mi_2.\end{aligned}`),description:'Hai mạch có hình học cố định, môi trường tuyến tính thuận nghịch. Từ thông là trung bình mỗi vòng, chiều dương được chọn nhất quán.',variables:[String.raw`$M$: Hỗ cảm ($\mathrm H$).`,String.raw`$N_1,N_2$: Số vòng (không thứ nguyên).`,String.raw`$i_1,i_2$: Dòng điện ($\mathrm A$).`,String.raw`$\Phi_B$: Từ thông mỗi vòng ($\mathrm{Wb}$).`]},
  {name:'Suất điện động hỗ cảm',formula:display(String.raw`\begin{aligned}&\mathcal E_2=-M\frac{di_1}{dt}\\&\mathcal E_1=-M\frac{di_2}{dt}.\end{aligned}`),description:'M không đổi. Dấu suất điện động phụ thuộc chiều quấn và các chiều dương đã chọn.',variables:[String.raw`$\mathcal E$: Suất điện động có dấu ($\mathrm V$).`,String.raw`$t$: Thời gian ($\mathrm s$).`]},
  {name:'Ống dây dài và cuộn ngoài',formula:display(String.raw`M=\frac{\mu N_1N_2A}{\ell}`),description:'Cuộn ngoài bao phần giữa ống dây dài. Trường ngoài ống được bỏ qua và A là tiết diện ống trong.',variables:[String.raw`$\mu$: Độ từ thẩm không đổi ($\mathrm{H/m}$).`,String.raw`$A$: Diện tích tiết diện ($\mathrm{m^2}$).`,String.raw`$\ell$: Chiều dài ($\mathrm m$).`]}
 ]},
 {id:'self',title:'Tự cảm và điện áp cuộn',items:[
  {name:'Định nghĩa và suất điện động',formula:display(String.raw`\begin{aligned}&L=\frac{N\Phi_B}{i}\\&\mathcal E_L=-L\frac{di}{dt}.\end{aligned}`),description:'Cuộn tuyến tính, hình học cố định. Suất điện động chống biến thiên dòng. Tỉ số định nghĩa được lấy ở dòng khác không hoặc qua giới hạn tuyến tính.',variables:[String.raw`$L$: Tự cảm ($\mathrm H$).`]},
  {name:'Quy ước điện áp thụ động',formula:display(String.raw`\begin{aligned}&v_{ab}=V_a-V_b\\&\quad=L\frac{di}{dt}.\end{aligned}`),description:'Cuộn lý tưởng, dòng dương từ a đến b. Với điện áp hữu hạn và L khác không, dòng cuộn liên tục khi chuyển mạch.',variables:[String.raw`$v_{ab}$: Điện áp có dấu ($\mathrm V$).`]},
  {name:'Ống dây thẳng và hình xuyến',formula:display(String.raw`\begin{aligned}&L_{\mathrm{ống}}=\frac{\mu N^2A}{\ell}\\&L_{\mathrm{xuyến}}=\frac{\mu N^2A}{2\pi r}.\end{aligned}`),description:'Ống thẳng dài với trường gần đều. Hình xuyến dùng bán kính trung bình r và tiết diện nhỏ so với r.',variables:[String.raw`$r$: Bán kính trung bình ($\mathrm m$).`]},
  {name:'Hai cuộn nối tiếp có hỗ cảm',formula:display(String.raw`\begin{aligned}&L_+=L_1+L_2+2M\\&L_-=L_1+L_2-2M.\end{aligned}`),description:'Dấu cộng khi hai trường hỗ trợ, dấu trừ khi đối nhau. M biểu diễn độ lớn liên kết từ theo cách chọn chiều tương ứng.'},
  {name:'Các đơn vị tương đương',formula:display(String.raw`\begin{aligned}&1\,\mathrm H=1\,\mathrm{Wb/A}\\&\quad=1\,\mathrm{V\,s/A}\\&\quad=1\,\Omega\cdot\mathrm s\\&\quad=1\,\mathrm{J/A^2}.\end{aligned}`),description:'Henry là đơn vị SI của tự cảm và hỗ cảm.'}
 ]},
 {id:'energy',title:'Năng lượng từ trường',items:[
  {name:'Năng lượng và công suất cuộn',formula:display(String.raw`\begin{aligned}&U_B=\frac12Li^2\\&\frac{dU_B}{dt}=Li\frac{di}{dt}.\end{aligned}`),description:'L không đổi. Năng lượng không phụ thuộc dấu dòng.',variables:[String.raw`$U_B$: Năng lượng từ trường ($\mathrm J$).`,String.raw`$dU_B/dt$: Công suất nhận vào cuộn ($\mathrm W$).`]},
  {name:'Mật độ năng lượng',formula:display(String.raw`\begin{aligned}&u_B=\frac{B^2}{2\mu_0}\\&u_B=\frac{B^2}{2\mu}.\end{aligned}`),description:'Dòng đầu dùng chân không. Dòng sau dùng vật liệu tuyến tính có độ từ thẩm không đổi.',variables:[String.raw`$u_B$: Mật độ năng lượng ($\mathrm{J/m^3}$).`,String.raw`$B$: Cảm ứng từ ($\mathrm T$).`,String.raw`$\mu_0$: Độ từ thẩm chân không ($\mathrm{H/m}$).`]}
 ]},
 {id:'rl',title:'Mạch RL',items:[
  {name:'Dòng tăng từ không',formula:display(String.raw`\begin{aligned}&L\frac{di}{dt}+Ri=\mathcal E\\&\tau=\frac LR\\&I_\infty=\frac{\mathcal E}{R}\\&i(t)=I_\infty(1-e^{-t/\tau}).\end{aligned}`),description:'Nguồn không đổi, R và L không đổi, i(0)=0. R là tổng điện trở trong vòng.',variables:[String.raw`$R$: Điện trở ($\Omega$).`,String.raw`$\tau$: Hằng số thời gian ($\mathrm s$).`]},
  {name:'Dòng giảm khi tách nguồn',formula:display(String.raw`\begin{aligned}&i(t)=I_0e^{-t/\tau}\\&\frac{di}{dt}=-\frac{i}{\tau}\\&U_B(t)=U_0e^{-2t/\tau}\\&t_{1/2}=\tau\ln2.\end{aligned}`),description:'Vòng RL kín không nguồn. I0 là dòng ngay trước và sau chuyển mạch.',variables:[String.raw`$I_0$: Dòng ban đầu ($\mathrm A$).`,String.raw`$U_0$: Năng lượng ban đầu ($\mathrm J$).`]},
  {name:'Cân bằng công suất',formula:display(String.raw`\begin{aligned}&\mathcal Ei=i^2R+\frac{dU_B}{dt}\\&0=i^2R+\frac{dU_B}{dt}.\end{aligned}`),description:'Dòng đầu khi nguồn còn trong vòng. Dòng sau khi vòng RL không có nguồn.'}
 ]},
 {id:'lc',title:'Mạch LC lý tưởng',items:[
  {name:'Phương trình và tần số',formula:display(String.raw`\begin{aligned}&Lq''+\frac qC=0\\&\omega_0=\frac1{\sqrt{LC}}\\&f=\frac{\omega_0}{2\pi}\\&T=2\pi\sqrt{LC}.\end{aligned}`),description:'Bỏ qua điện trở và bức xạ trong mô hình mạch tập trung. i=dq/dt đi vào bản có điện tích q.',variables:[String.raw`$C$: Điện dung ($\mathrm F$).`,String.raw`$q$: Điện tích có dấu ($\mathrm C$).`,String.raw`$\omega_0$: Tần số góc ($\mathrm{rad/s}$).`,String.raw`$f$: Tần số ($\mathrm{Hz}$).`,String.raw`$T$: Chu kỳ ($\mathrm s$).`]},
  {name:'Điện tích và dòng',formula:display(String.raw`\begin{aligned}&q=Q\cos(\omega_0t+\phi)\\&i=-\omega_0Q\sin(\omega_0t+\phi)\\&I_{\max}=\omega_0Q.\end{aligned}`),description:'Q và pha φ được xác định từ điện tích và dòng ban đầu.',variables:[String.raw`$Q$: Biên độ điện tích ($\mathrm C$).`,String.raw`$\phi$: Pha ban đầu ($\mathrm{rad}$).`]},
  {name:'Bảo toàn năng lượng',formula:display(String.raw`\begin{aligned}&U=\frac12Li^2+\frac{q^2}{2C}\\&\quad=\frac{Q^2}{2C}\\&\quad=\frac12LI_{\max}^2.\end{aligned}`),description:'Tổng năng lượng không đổi, trao đổi giữa tụ và cuộn. Hai phần năng lượng luôn không âm.'}
 ]},
 {id:'rlc',title:'Mạch RLC và ba chế độ',items:[
  {name:'Phương trình tự do',formula:display(String.raw`\begin{aligned}&Lq''+Rq'+\frac qC=0\\&\alpha=\frac{R}{2L}\\&\omega_d=\sqrt{\frac1{LC}-\alpha^2}.\end{aligned}`),description:'Nguồn đã tách, R,L,C không đổi. Tần số góc thực dùng trong miền dưới tắt dần.',variables:[String.raw`$\alpha$: Hệ số suy giảm biên độ ($\mathrm{s^{-1}}$).`,String.raw`$\omega_d$: Tần số góc tắt dần ($\mathrm{rad/s}$).`]},
  {name:'Nghiệm dưới tắt dần',formula:"$$\n\\begin{aligned}\n&q=Ae^{-\\alpha t}\\cos(\\omega_dt+\\phi),\\\\\n&q(0)=A\\cos\\phi,\\\\\n&i(0)=-\\alpha q(0)-\\omega_dA\\sin\\phi.\n\\end{aligned}\n$$",description:'R²<4L/C. Cả điện tích lẫn dòng ban đầu quyết định A và φ.',variables:[String.raw`$A$: Hệ số biên độ ($\mathrm C$).`]},
  {name:'Điện trở tới hạn',formula:display(String.raw`R_{\mathrm{th}}=2\sqrt{\frac LC}`),description:'R nhỏ hơn ngưỡng cho dao động tắt dần. R bằng ngưỡng cho tắt dần tới hạn. R lớn hơn ngưỡng cho quá tắt dần.'},
  {name:'Các nghiệm không dao động',formula:display(String.raw`\begin{aligned}&q_{\mathrm{th}}=(a+bt)e^{-\alpha t}\\&q_{\mathrm{quá}}=ae^{-\alpha_1t}+be^{-\alpha_2t}.\end{aligned}`),description:'Nghiệm tới hạn dùng R²=4L/C. Nghiệm quá tắt dần dùng R²>4L/C với hai tốc độ suy giảm dương. Các hệ số phụ thuộc điều kiện đầu.'},
  {name:'Năng lượng tiêu tán',formula:display(String.raw`\begin{aligned}&U=\frac{q^2}{2C}+\frac12Li^2\\&\frac{dU}{dt}=-Ri^2.\end{aligned}`),description:String.raw`Tổng năng lượng giảm trong mạch RLC tự do. Bao biên độ giảm theo $e^{-\alpha t}$ trong miền dưới tắt dần.`}
 ]}
]}
