const d=tex=>'$$\n'+tex+'\n$$'
// Wrap each authored formula at its call site so build-time math extraction sees it.
const row=(label,formula)=>({label,formula})
const item=(name,description,rows=[])=>({name,description,formulaRows:rows.map(([a,b])=>row(a,b)),variables:[]})
const section=(id,title,badge,items)=>({id,title,badge,items})
const topic=(slug,title,question,source)=>({slug,title,question,source})
const slide=(note,title,bullets,tex='')=>({note,title,bullets,formula:tex?d(tex):''})
const definitions={
 9:{slug:'09-dong-hoc-vat-ran',prerequisites:['dao-ham','tich-phan','vector','cong-nang-luong'],supportingConcepts:['toa-do-goc','van-toc-goc','gia-toc-goc','momen-quan-tinh','dinh-ly-truc-song-song','ban-kinh-quan-tinh'],topics:[
  topic('van-toc-va-gia-toc-goc','Vận tốc góc và gia tốc góc','Làm thế nào mô tả vị trí và chiều quay của toàn bộ vật rắn?','9.1'),
  topic('quay-gia-toc-goc-khong-doi','Quay với gia tốc góc không đổi','Khi nào dùng được các phương trình quay tương tự chuyển động thẳng?','9.2'),
  topic('lien-he-dai-luong-dai-va-goc','Liên hệ đại lượng dài và đại lượng góc','Vì sao các điểm trên cùng vật có cùng vận tốc góc nhưng khác tốc độ dài?','9.3'),
  topic('dong-nang-va-momen-quan-tinh','Động năng quay và mômen quán tính','Sự phân bố khối lượng quanh trục quyết định động năng quay thế nào?','9.4'),
  topic('dinh-ly-truc-song-song','Định lý trục song song','Đổi trục quay song song làm mômen quán tính thay đổi ra sao?','9.5'),
  topic('tinh-momen-quan-tinh','Tính mômen quán tính bằng tích phân','Chọn phần tử khối lượng nào để tính mômen quán tính của một vật liên tục?','9.6')
 ],sections:[
  section('angular','Đại lượng động học góc','9.1–9.2',[
   item('Tọa độ góc và độ dời góc','Góc tính bằng radian. Độ dời góc là đại lượng có dấu, còn quãng đường trên cung tròn không âm.',[[ 'Độ dời góc',d(String.raw`\Delta\theta=\theta_2-\theta_1`)],['Góc và cung có hướng',d(String.raw`s=r\theta`)],['Một vòng quay',d(String.raw`1\,\mathrm{rev}=2\pi\,\mathrm{rad}`)]]),
   item('Vận tốc góc','Chọn chiều dương quanh trục trước khi xác định dấu. Tốc độ góc là độ lớn vận tốc góc.',[['Trung bình',d(String.raw`\omega_{\mathrm{av},z}=\Delta\theta/\Delta t`)],['Tức thời',d(String.raw`\omega_z=d\theta/dt`)]]),
   item('Gia tốc góc','Gia tốc góc biểu diễn sự thay đổi vận tốc góc. Đơn vị là rad/s².',[['Đạo hàm theo thời gian',d(String.raw`\alpha_z=d\omega_z/dt`)]]),
   item('Gia tốc góc không đổi','Các hệ thức sau áp dụng trong cùng một khoảng có gia tốc góc không đổi. Thời điểm đầu lấy bằng không.',[['Vận tốc góc',d(String.raw`\omega_z=\omega_{0z}+\alpha_zt`)],['Độ dời góc',d(String.raw`\Delta\theta=\omega_{0z}t+\tfrac12\alpha_zt^2`)],['Khử thời gian',d(String.raw`\omega_z^2-\omega_{0z}^2=2\alpha_z\Delta\theta`)],['Vận tốc góc trung bình',d(String.raw`\Delta\theta=\tfrac12(\omega_{0z}+\omega_z)t`)]])
  ]),
  section('linear','Chuyển động của một điểm trên vật','9.3',[
   item('Vận tốc và gia tốc','Khoảng r là khoảng cách vuông góc từ điểm đến trục cố định. Hai thành phần gia tốc tiếp tuyến và hướng tâm vuông góc nhau.',[['Tốc độ dài',d(String.raw`v=r|\omega_z|`)],['Thành phần tiếp tuyến có dấu',d(String.raw`a_t=r\alpha_z`)],['Độ lớn hướng tâm',d(String.raw`a_r=r\omega_z^2`)],['Độ lớn gia tốc',d(String.raw`a=\sqrt{a_t^2+a_r^2}`)]])
  ]),
  section('inertia','Mômen quán tính và động năng','9.4–9.6',[
   item('Mômen quán tính','Mômen quán tính phụ thuộc vật và trục. Các rᵢ là khoảng cách đến trục, không nhất thiết là khoảng cách đến gốc.',[['Ba chất điểm',d(String.raw`I=m_1r_1^2+m_2r_2^2+m_3r_3^2`)],['Hệ n chất điểm',d(String.raw`I=\sum_{i=1}^{n}m_ir_i^2`)],['Phân bố liên tục',d(String.raw`I=\int r^2\,dm`)]]),
   item('Động năng quay','Vật rắn quay quanh trục cố định, với mọi điểm có cùng vận tốc góc.',[['Động năng',d(String.raw`K=\tfrac12I\omega_z^2`)],['Bán kính quán tính',d(String.raw`k=\sqrt{I/M}`)]]),
   item('Định lý trục song song','Một trục phải đi qua khối tâm. Trục thứ hai song song và cách nó một khoảng d.',[['Mômen quán tính trục dời',d(String.raw`I=I_{\mathrm{cm}}+Md^2`)]]),
   item('Thanh mảnh đồng chất','Trục vuông góc chiều dài L. M là khối lượng thanh.',[['Trục qua giữa thanh',d(String.raw`I_{\mathrm{cm}}=ML^2/12`)],['Trục qua đầu thanh',d(String.raw`I_{\mathrm{end}}=ML^2/3`)]]),
   item('Các vật tròn đối xứng','Trục qua tâm và là trục đối xứng tương ứng. Các vật đồng chất.',[['Vành tròn mảnh',d(String.raw`I=MR^2`)],['Đĩa hoặc trụ đặc',d(String.raw`I=\tfrac12MR^2`)],['Trụ rỗng thành dày',d(String.raw`I=\tfrac12M(R_1^2+R_2^2)`)],['Cầu đặc',d(String.raw`I=\tfrac25MR^2`)],['Vỏ cầu mỏng',d(String.raw`I=\tfrac23MR^2`)]]),
   item('Tấm chữ nhật đồng chất','Trục qua tâm, vuông góc mặt tấm cạnh a và b.',[['Mômen quán tính',d(String.raw`I=M(a^2+b^2)/12`)]])
  ])]},
 10:{slug:'10-dong-luc-hoc-quay',prerequisites:['vector','luc','momen-quan-tinh','cong-nang-luong','dong-luong-vat-ly'],supportingConcepts:['momen-luc','momen-dong-luong','lan-khong-truot','con-quay-tien-dong'],topics:[
  topic('momen-luc','Mômen lực','Lực tác dụng ở đâu và theo hướng nào tạo ra tác dụng quay?','10.1'),
  topic('momen-luc-va-gia-toc-goc','Mômen lực và gia tốc góc','Tổng mômen lực quyết định gia tốc quay quanh trục cố định thế nào?','10.2'),
  topic('quay-quanh-truc-chuyen-dong','Vật rắn quay quanh trục chuyển động','Kết hợp chuyển động khối tâm và chuyển động quay trong bài toán lăn ra sao?','10.3'),
  topic('cong-va-cong-suat-quay','Công và công suất trong chuyển động quay','Lực làm vật quay truyền năng lượng với tốc độ nào?','10.4'),
  topic('momen-dong-luong','Mômen động lượng','Mômen động lượng phụ thuộc gốc và phân bố vận tốc như thế nào?','10.5'),
  topic('bao-toan-momen-dong-luong','Bảo toàn mômen động lượng','Khi nào thay đổi cấu hình làm vận tốc quay thay đổi mà mômen động lượng vẫn giữ nguyên?','10.6'),
  topic('con-quay-va-tien-dong','Con quay và tiến động','Vì sao mômen trọng lực có thể đổi hướng trục quay thay vì làm con quay đổ ngay?','10.7')
 ],sections:[
  section('torque','Mômen lực và phương trình chuyển động','10.1–10.2',[
   item('Mômen lực','Vector vị trí tính từ gốc đã chọn đến điểm đặt lực. Cánh tay đòn là khoảng cách từ gốc đến giá lực.',[['Dạng vector',d(String.raw`\vec\tau=\vec r\times\vec F`)],['Độ lớn',d(String.raw`\tau=rF\sin\phi=F\ell`)]]),
   item('Vật rắn quay quanh trục cố định','Dùng thành phần mômen ngoại lực và mômen quán tính đối với cùng trục cố định trong hệ quán tính.',[['Phương trình theo trục',d(String.raw`\sum\tau_z=I_z\alpha_z`)]])
  ]),
  section('rolling','Tịnh tiến, quay và lăn','10.3–10.4',[
   item('Động năng vật rắn','Tách động năng chuyển động của khối tâm và động năng quay quanh trục qua khối tâm.',[['Tổng động năng',d(String.raw`K=\tfrac12Mv_{\mathrm{cm}}^2+\tfrac12I_{\mathrm{cm}}\omega^2`)]]),
   item('Lăn không trượt','Quan hệ độ lớn này áp dụng tại tiếp xúc với mặt phẳng đứng yên. Dấu các thành phần phụ thuộc quy ước trục.',[['Tốc độ khối tâm',d(String.raw`v_{\mathrm{cm}}=R\omega`)],['Gia tốc tiếp tuyến',d(String.raw`a_{\mathrm{cm}}=R\alpha`)]]),
   item('Lăn xuống mặt nghiêng','Vật tròn lăn không trượt dưới trọng lực, không có lực hay mômen ngoài bổ sung. Ma sát phải đủ giữ điều kiện lăn.',[['Gia tốc khối tâm',d(String.raw`a_{\mathrm{cm}}=\frac{g\sin\beta}{1+I_{\mathrm{cm}}/(MR^2)}`)]]),
   item('Công và công suất quay','Trục cố định. Công phụ thuộc góc và mômen lực tác dụng trong suốt quá trình.',[['Công của mômen lực',d(String.raw`W=\int_{\theta_1}^{\theta_2}\tau_z\,d\theta`)],['Định lý công–động năng',d(String.raw`W_{\mathrm{net}}=K_2-K_1`)],['Công suất tức thời',d(String.raw`P=\tau_z\omega_z`)]])
  ]),
  section('angular-momentum','Mômen động lượng và con quay','10.5–10.7',[
   item('Mômen động lượng','Gốc tính mômen phải được xác định. Với gốc cố định trong hệ quán tính, tổng mômen ngoại lực bằng tốc độ đổi mômen động lượng.',[['Một chất điểm',d(String.raw`\vec L=\vec r\times\vec p`)],['Định luật biến thiên',d(String.raw`d\vec L/dt=\vec\tau_{\mathrm{ext}}`)],['Thành phần theo trục quay',d(String.raw`L_z=I_z\omega_z`)]]),
   item('Bảo toàn mômen động lượng','Tổng mômen ngoại lực đối với gốc xét bằng không. Bảo toàn mômen động lượng không kéo theo bảo toàn động năng.',[['Dạng vector',d(String.raw`\vec L_i=\vec L_f`)],['Cùng một trục với mô hình thích hợp',d(String.raw`I_i\omega_i=I_f\omega_f`)]]),
   item('Tiến động đều chậm','Con quay đối xứng quay nhanh, trục nghiêng và đầu tựa cố định. Hệ thức là gần đúng khi mômen động lượng chủ yếu do quay quanh trục đối xứng.',[['Tốc độ góc tiến động',d(String.raw`\Omega=Mgr/(I\omega)`)]])
  ])]},
 11:{slug:'11-can-bang-dan-hoi',prerequisites:['luc','momen-luc','don-vi'],supportingConcepts:['can-bang-co-hoc','trong-tam-vat-ran','ung-suat','bien-dang-tuong-doi','modun-young','modun-khoi','modun-truot','gioi-han-dan-hoi'],topics:[
  topic('dieu-kien-can-bang','Điều kiện cân bằng','Vì sao cân bằng lực chưa đủ để giữ vật rắn đứng yên?','11.1'),
  topic('trong-tam','Trọng tâm','Khi nào có thể thay trọng lực phân bố bằng một lực đặt tại trọng tâm?','11.2'),
  topic('giai-bai-toan-can-bang-vat-ran','Giải bài toán cân bằng vật rắn','Chọn vật, điểm tính mômen và lực liên kết như thế nào?','11.3'),
  topic('ung-suat-bien-dang-modun','Ứng suất, biến dạng và môđun đàn hồi','Lực phân bố trên diện tích và sự biến dạng liên hệ ra sao?','11.4'),
  topic('dan-hoi-va-deo','Đàn hồi và dẻo','Giới hạn tỉ lệ khác giới hạn đàn hồi thế nào?','11.5')
 ],sections:[
  section('equilibrium','Cân bằng và trọng tâm','11.1–11.3',[
   item('Điều kiện cân bằng tĩnh','Vật ban đầu đứng yên trong hệ quán tính. Hợp lực và tổng mômen ngoại lực cùng bằng không.',[['Cân bằng lực',d(String.raw`\sum\vec F=\vec0`)],['Cân bằng mômen lực',d(String.raw`\sum\vec\tau=\vec0`)]]),
   item('Trọng tâm trong trường đều','Khi gia tốc trọng trường cùng hướng và cùng độ lớn trong toàn vật, trọng tâm trùng khối tâm.',[['Tọa độ khối tâm',d(String.raw`x_{\mathrm{cm}}=\frac{\sum_{i=1}^{n}m_ix_i}{M}`)]]),
   item('Ma sát nghỉ','Lực ma sát tự điều chỉnh trong giới hạn. Chỉ đạt dấu bằng ở ngưỡng trượt.',[['Giới hạn độ lớn',d(String.raw`f_s\le\mu_sN`)]])
  ]),
  section('elastic','Đại lượng đàn hồi tuyến tính','11.4–11.5',[
   item('Kéo và nén','F⊥ là độ lớn lực pháp tuyến trên tiết diện A. Công thức môđun áp dụng trong miền tỉ lệ tuyến tính.',[['Ứng suất pháp',d(String.raw`\sigma=F_\perp/A`)],['Biến dạng dài',d(String.raw`\varepsilon=\Delta L/L_0`)],['Môđun Young',d(String.raw`Y=\sigma/\varepsilon`)],['Độ dãn',d(String.raw`\Delta L=F_\perp L_0/(YA)`)]]),
   item('Nén thể tích','Áp suất tăng làm thể tích giảm đối với vật liệu ổn định thông thường. Dấu trừ làm môđun khối dương.',[['Môđun khối',d(String.raw`B=-\Delta p/(\Delta V/V_0)`)],['Độ nén',d(String.raw`\kappa=1/B`)]]),
   item('Trượt','Lực tiếp tuyến phân bố trên diện tích A làm hai mặt lệch nhau. x/h là biến dạng trượt góc nhỏ.',[['Môđun trượt',d(String.raw`S=\frac{F_\parallel/A}{x/h}`)]]),
   item('Giới hạn vật liệu','Giới hạn tỉ lệ là ranh giới gần đúng của quan hệ ứng suất–biến dạng tuyến tính. Giới hạn đàn hồi là ranh giới phục hồi hoàn toàn sau bỏ lực. Vượt giới hạn đàn hồi có thể để lại biến dạng dư.')
  ])]},
 17:{slug:'17-nhiet-do-nhiet-luong',prerequisites:['don-vi','cong-nang-luong','luc'],supportingConcepts:['can-bang-nhiet','nguyen-ly-khong-nhiet-dong','nhiet-do-tuyet-doi','su-no-vi-nhiet','nhiet-luong','nhiet-dung-rieng','nhiet-an-chuyen-pha','dan-nhiet','nhiet-tro','doi-luu-nhiet','buc-xa-nhiet'],topics:[
  topic('nhiet-do-va-can-bang-nhiet','Nhiệt độ và cân bằng nhiệt','Nhiệt kế đo đại lượng nào khi đạt cân bằng với vật?','17.1'),
  topic('nhiet-ke-va-thang-nhiet-do','Nhiệt kế và các thang nhiệt độ','Các tính chất vật lý được dùng để xây dựng thang nhiệt độ thế nào?','17.2'),
  topic('nhiet-ke-khi-va-thang-kelvin','Nhiệt kế khí và thang Kelvin','Giới hạn khí loãng dẫn tới thang nhiệt độ tuyệt đối ra sao?','17.3'),
  topic('su-no-vi-nhiet','Sự nở vì nhiệt','Vì sao thay đổi nhiệt độ làm thay đổi kích thước và tạo ứng suất?','17.4'),
  topic('nhiet-luong','Nhiệt lượng và nhiệt dung','Nhiệt lượng khác nhiệt độ và năng lượng chứa trong vật như thế nào?','17.5'),
  topic('nhiet-luong-ke-va-chuyen-pha','Nhiệt lượng kế và chuyển pha','Cân bằng năng lượng thế nào khi các vật đổi nhiệt độ hoặc đổi pha?','17.6'),
  topic('cac-co-che-truyen-nhiet','Các cơ chế truyền nhiệt','Dẫn nhiệt, đối lưu và bức xạ truyền năng lượng bằng cơ chế nào?','17.7')
 ],sections:[
  section('temperature','Nhiệt độ và thang nhiệt độ','17.1–17.3',[
   item('Nguyên lý không','Nếu hai hệ cùng cân bằng nhiệt với một hệ thứ ba thì chúng cân bằng nhiệt với nhau. Nhiệt độ là đại lượng xác định điều kiện cân bằng nhiệt.'),
   item('Đổi thang nhiệt độ','Trong các công thức sau, tF và tC là các số đo theo độ Fahrenheit và độ Celsius. T là số đo theo kelvin.',[['Fahrenheit và Celsius',d(String.raw`t_F=\tfrac95t_C+32`)],['Kelvin và Celsius',d(String.raw`T=t_C+273.15`)],['Khoảng nhiệt độ',d(String.raw`\Delta T=\Delta t_C`)]]),
   item('Thang Kelvin','Kelvin là đơn vị nhiệt độ nhiệt động lực học. Nhiệt kế khí thể tích không đổi trong giới hạn khí loãng cho quan hệ áp suất tỉ lệ nhiệt độ tuyệt đối.',[['Cùng thể tích và lượng khí lý tưởng',d(String.raw`T_2/T_1=p_2/p_1`)]])
  ]),
  section('expansion','Nở vì nhiệt','17.4',[
   item('Nở dài và nở thể tích','Biến thiên nhiệt độ đủ nhỏ để hệ số nở có thể coi không đổi. Vật nở tự do, không chịu cản trở cơ học.',[['Nở dài',d(String.raw`\Delta L=\alpha L_0\Delta T`)],['Nở thể tích',d(String.raw`\Delta V=\beta V_0\Delta T`)],['Vật đẳng hướng, nở nhỏ',d(String.raw`\beta\approx3\alpha`)]]),
   item('Ứng suất nhiệt','Thanh bị giữ không đổi chiều dài trong miền đàn hồi tuyến tính. Dấu ứng suất theo quy ước kéo dương.',[['Ứng suất khi bị giữ',d(String.raw`\sigma=-Y\alpha\Delta T`)]])
  ]),
  section('heat','Nhiệt lượng và chuyển pha','17.5–17.6',[
   item('Nhiệt lượng khi đổi nhiệt độ','Không chuyển pha. c hoặc C có thể coi không đổi trong khoảng khảo sát. Nhiệt lượng dương khi hệ nhận năng lượng bằng truyền nhiệt.',[['Theo khối lượng',d(String.raw`Q=mc\Delta T`)],['Theo số mol',d(String.raw`Q=nC\Delta T`)],['Hai loại nhiệt dung',d(String.raw`C=Mc`)]]),
   item('Ẩn nhiệt','Chuyển pha ở điều kiện xác định. L là ẩn nhiệt trên một đơn vị khối lượng. Dấu Q phụ thuộc chiều chuyển pha.',[['Nhiệt lượng chuyển pha',d(String.raw`|Q|=mL`)]]),
   item('Nhiệt lượng kế cách nhiệt','Chọn toàn bộ các vật trao đổi nhiệt làm hệ. Không có công ngoài đáng kể và không thất thoát nhiệt ra môi trường.',[['Cân bằng trao đổi nhiệt',d(String.raw`Q_1+Q_2+\cdots+Q_n=0`)]])
  ]),
  section('transfer','Cơ chế truyền nhiệt','17.7',[
   item('Dẫn nhiệt ổn định qua bản phẳng','Vật đồng nhất, tiết diện A, chiều dài dẫn L. Hai đầu giữ ở nhiệt độ Th lớn hơn Tc. H là độ lớn dòng nhiệt.',[['Dòng nhiệt',d(String.raw`H=kA(T_h-T_c)/L`)],['Nhiệt trở dẫn',d(String.raw`R_{\mathrm{th}}=L/(kA)`)],['Dòng theo nhiệt trở',d(String.raw`H=(T_h-T_c)/R_{\mathrm{th}}`)]]),
   item('Các lớp nối tiếp','Dòng nhiệt ổn định đi qua lần lượt các lớp, không có nguồn nhiệt ở nút nối và không thất thoát ngang.',[['Tổng nhiệt trở',d(String.raw`R=R_1+R_2+\cdots+R_n`)]]),
   item('Đối lưu','Truyền nhiệt kèm chuyển động vĩ mô của chất lưu. Đối lưu có thể do chênh lệch khối lượng riêng hoặc do quạt và bơm gây ra.'),
   item('Bức xạ nhiệt','Nhiệt độ tính bằng kelvin. e là hệ số phát xạ. Hệ thức trao đổi ròng xét vật nhỏ trong môi trường bao quanh lớn ở nhiệt độ Ts.',[['Công suất phát xạ',d(String.raw`P=e\sigma AT^4`)],['Công suất phát ròng',d(String.raw`P_{\mathrm{net}}=e\sigma A(T^4-T_s^4)`)]])
  ])]},
 18:{slug:'18-thuyet-dong-hoc-chat-khi',prerequisites:['nhiet-do-tuyet-doi','cong-nang-luong','dong-luong-vat-ly'],supportingConcepts:['khi-ly-tuong','phuong-trinh-van-der-waals','phan-bo-maxwell','nguyen-ly-phan-bo-deu-nang-luong','quang-duong-tu-do-trung-binh','diem-ba','diem-toi-han-chat'],topics:[
  topic('phuong-trinh-trang-thai','Phương trình trạng thái','Áp suất, thể tích và nhiệt độ của chất khí được ràng buộc ra sao?','18.1'),
  topic('tinh-chat-phan-tu-vat-chat','Tính chất phân tử của vật chất','Kích thước, tương tác và lượng chất liên hệ với đại lượng vĩ mô thế nào?','18.2'),
  topic('mo-hinh-dong-hoc-khi-ly-tuong','Mô hình động học phân tử của khí lý tưởng','Va chạm phân tử tạo áp suất và nối nhiệt độ với động năng ra sao?','18.3'),
  topic('nhiet-dung','Nhiệt dung và các bậc tự do','Vì sao nhiệt dung khí phụ thuộc cấu trúc phân tử và nhiệt độ?','18.4'),
  topic('toc-do-phan-tu','Tốc độ phân tử','Tốc độ trung bình, hiệu dụng và có xác suất lớn nhất khác nhau thế nào?','18.5'),
  topic('cac-pha-cua-vat-chat','Các pha của vật chất','Giản đồ pha cho biết gì về điểm ba và điểm tới hạn?','18.6')
 ],sections:[
  section('state','Lượng chất và phương trình trạng thái','18.1–18.2',[
   item('Khí lý tưởng','Các phân tử có thể coi là chất điểm, tương tác giữa các va chạm được bỏ qua. n là số mol, N là số phân tử.',[['Dạng mol',d(String.raw`pV=nRT`)],['Dạng phân tử',d(String.raw`pV=Nk_BT`)],['Liên hệ lượng chất',d(String.raw`N=nN_A`)]]),
   item('Khí thực theo van der Waals','a và b là các hằng số đặc trưng cho chất khí trong mô hình hiệu dụng. p* là áp suất đã hiệu chỉnh lực hút, V* là thể tích đã hiệu chỉnh kích thước phân tử.',[['Áp suất hiệu chỉnh',d(String.raw`p_*=p+an^2/V^2`)],['Thể tích hiệu chỉnh',d(String.raw`V_*=V-nb`)],['Phương trình trạng thái',d(String.raw`p_*V_*=nRT`)]])
  ]),
  section('kinetic','Áp suất, chuyển động và nhiệt dung','18.3–18.4',[
   item('Động năng tịnh tiến','Cân bằng nhiệt, khí cổ điển lý tưởng và chuyển động đẳng hướng. m là khối lượng một phân tử.',[['Động năng tịnh tiến trung bình',d(String.raw`\langle K_{\mathrm{tr}}\rangle=\tfrac32k_BT`)],['Tốc độ hiệu dụng',d(String.raw`v_{\mathrm{rms}}=\sqrt{3k_BT/m}`)],['Dạng khối lượng mol',d(String.raw`v_{\mathrm{rms}}=\sqrt{3RT/M}`)],['Áp suất động học',d(String.raw`pV=\tfrac13Nm\langle v^2\rangle`)]]),
   item('Phân bố đều năng lượng','Mỗi số hạng bậc hai độc lập đang hoạt động trong giới hạn cổ điển đóng góp năng lượng trung bình bằng một nửa kBT trên mỗi phân tử.',[['Nhiệt dung mol đẳng tích',d(String.raw`C_V=fR/2`)]]),
   item('Quãng đường tự do trung bình','Mô hình các phân tử cầu cứng đường kính d, khí loãng có mật độ số nN.',[['Mật độ số',d(String.raw`n_N=N/V`)],['Quãng đường tự do',d(String.raw`\ell=1/(\sqrt2\pi d^2n_N)`)]])
  ]),
  section('distribution','Phân bố tốc độ và pha vật chất','18.5–18.6',[
   item('Các tốc độ đặc trưng','Khí lý tưởng có phân bố Maxwell ở cân bằng nhiệt. Khối lượng m là của một phân tử.',[['Tốc độ có xác suất lớn nhất',d(String.raw`v_{\mathrm{mp}}=\sqrt{2k_BT/m}`)],['Tốc độ trung bình',d(String.raw`\bar v=\sqrt{8k_BT/(\pi m)}`)],['Thứ tự',d(String.raw`v_{\mathrm{mp}}<\bar v<v_{\mathrm{rms}}`)]]),
   item('Phân bố Maxwell','f(v)dv là phần phân tử có tốc độ trong khoảng từ v đến v+dv, với v không âm. Các ký hiệu C và b được định nghĩa trong các dòng dưới.',[['Hệ số chuẩn hóa',d(String.raw`C=4\pi[m/(2\pi k_BT)]^{3/2}`)],['Hệ số trong hàm mũ',d(String.raw`b=m/(2k_BT)`)],['Mật độ tốc độ',d(String.raw`f(v)=Cv^2e^{-bv^2}`)]]),
   item('Điểm ba và điểm tới hạn','Điểm ba là điều kiện nhiệt độ và áp suất tại đó ba pha cân bằng. Điểm tới hạn kết thúc đường cân bằng lỏng–hơi, nơi ranh giới giữa hai pha này mất đi.')
  ])]},
 19:{slug:'19-nguyen-ly-thu-nhat',prerequisites:['khi-ly-tuong','tich-phan','nhiet-do-tuyet-doi','cong-nang-luong'],supportingConcepts:['he-nhiet-dong','noi-nang','cong-nhiet-dong','qua-trinh-dang-nhiet','qua-trinh-doan-nhiet','nhiet-dung-dang-tich-dang-ap'],topics:[
  topic('he-nhiet-dong','Hệ nhiệt động','Chọn hệ và quy ước dấu cho năng lượng trao đổi thế nào?','19.1'),
  topic('cong-khi-the-tich-thay-doi','Công khi thể tích thay đổi','Diện tích dưới đường quá trình trên đồ thị p–V biểu diễn đại lượng gì?','19.2'),
  topic('duong-di-giua-cac-trang-thai','Đường đi giữa các trạng thái','Vì sao cùng hai trạng thái đầu cuối có thể cho công và nhiệt lượng khác nhau?','19.3'),
  topic('noi-nang-va-nguyen-ly-thu-nhat','Nội năng và nguyên lý thứ nhất','Bảo toàn năng lượng được viết thế nào theo nội năng, nhiệt lượng và công?','19.4'),
  topic('cac-qua-trinh-nhiet-dong','Các quá trình nhiệt động','Đẳng tích, đẳng áp, đẳng nhiệt và đoạn nhiệt khác nhau ở điều kiện nào?','19.5'),
  topic('noi-nang-khi-ly-tuong','Nội năng của khí lý tưởng','Vì sao nội năng khí lý tưởng chỉ phụ thuộc nhiệt độ?','19.6'),
  topic('nhiet-dung-khi-ly-tuong','Nhiệt dung của khí lý tưởng','Vì sao đun đẳng áp cần nhiều nhiệt lượng hơn đun đẳng tích?','19.7'),
  topic('qua-trinh-doan-nhiet-khi-ly-tuong','Quá trình đoạn nhiệt của khí lý tưởng','Trong điều kiện nào áp suất và thể tích tuân theo định luật lũy thừa?','19.8')
 ],sections:[
  section('first-law','Hệ, công và bảo toàn năng lượng','19.1–19.4',[
   item('Quy ước dấu','Q dương khi hệ nhận nhiệt. W dương khi hệ thực hiện công lên môi trường.',[['Nguyên lý thứ nhất',d(String.raw`\Delta U=Q-W`)]]),
   item('Công biến đổi thể tích','Quá trình đủ chậm để dùng áp suất cân bằng p của hệ cho công biên. Khi giãn nở không cân bằng, phải xét áp suất ngoài phù hợp.',[['Công do hệ thực hiện',d(String.raw`W=\int_{V_1}^{V_2}p\,dV`)],['Đẳng áp',d(String.raw`W=p(V_2-V_1)`)]]),
   item('Đại lượng trạng thái và đường đi','Nội năng phụ thuộc trạng thái. Q và W phụ thuộc cả đường quá trình giữa hai trạng thái.')
  ]),
  section('process','Các quá trình và khí lý tưởng','19.5–19.7',[
   item('Điều kiện quá trình','Đẳng tích giữ V không đổi. Đẳng áp giữ p không đổi. Đẳng nhiệt giữ T không đổi. Đoạn nhiệt không trao đổi nhiệt.',[['Đẳng tích',d(String.raw`W=0`)],['Đoạn nhiệt',d(String.raw`Q=0`)],['Một chu trình',d(String.raw`\Delta U=0`)]]),
   item('Nội năng khí lý tưởng','Lượng khí và thành phần không đổi. CV có thể coi không đổi trên khoảng nhiệt độ đang xét.',[['Độ biến thiên nội năng',d(String.raw`\Delta U=nC_V\Delta T`)],['Khí đơn nguyên tử cổ điển',d(String.raw`U=\tfrac32nRT`)]]),
   item('Nhiệt dung mol','Khí lý tưởng có cùng thành phần, trong cùng miền nhiệt độ xét.',[['Đẳng áp và đẳng tích',d(String.raw`C_p-C_V=R`)],['Tỉ số nhiệt dung',d(String.raw`\gamma=C_p/C_V`)]]),
   item('Giãn nở đẳng nhiệt khí lý tưởng','Quá trình thuận nghịch hoặc gần tĩnh, T không đổi và lượng khí không đổi.',[['Công đẳng nhiệt',d(String.raw`W=nRT\ln(V_2/V_1)`)],['Biến thiên nội năng',d(String.raw`\Delta U=0`)]])
  ]),
  section('adiabatic','Đoạn nhiệt thuận nghịch','19.8',[
   item('Định luật đoạn nhiệt','Chỉ áp dụng cho khí lý tưởng, quá trình đoạn nhiệt thuận nghịch hoặc gần tĩnh phù hợp, với nhiệt dung và gamma coi không đổi.',[['Áp suất–thể tích',d(String.raw`pV^\gamma=\mathrm{const}`)],['Nhiệt độ–thể tích',d(String.raw`TV^{\gamma-1}=\mathrm{const}`)],['Công do khí thực hiện',d(String.raw`W=\frac{p_1V_1-p_2V_2}{\gamma-1}`)]])
  ])]},
 20:{slug:'20-nguyen-ly-thu-hai-entropy',prerequisites:['noi-nang','khi-ly-tuong','nhiet-do-tuyet-doi','tich-phan'],supportingConcepts:['dong-co-nhiet','hieu-suat-nhiet','he-so-lam-lanh','chu-trinh-carnot','entropy-nhiet-dong','qua-trinh-thuan-nghich','so-trang-thai-vi-mo'],topics:[
  topic('chieu-cua-qua-trinh-nhiet-dong','Chiều của quá trình nhiệt động','Vì sao bảo toàn năng lượng chưa xác định được chiều diễn biến?','20.1'),
  topic('dong-co-nhiet','Động cơ nhiệt','Động cơ nhận nhiệt, sinh công và thải nhiệt trong một chu trình ra sao?','20.2'),
  topic('dong-co-dot-trong','Động cơ đốt trong','Mô hình Otto và Diesel liên hệ các quá trình nhiệt động như thế nào?','20.3'),
  topic('may-lanh','Máy lạnh và bơm nhiệt','Công cấp vào giúp chuyển nhiệt từ nguồn lạnh lên nguồn nóng thế nào?','20.4'),
  topic('nguyen-ly-thu-hai','Nguyên lý thứ hai','Các phát biểu Kelvin–Planck và Clausius tương đương về giới hạn nào?','20.5'),
  topic('chu-trinh-carnot','Chu trình Carnot','Vì sao nhiệt độ hai nguồn đặt giới hạn cho hiệu suất?','20.6'),
  topic('entropy','Entropy','Làm thế nào tính độ biến thiên entropy của một quá trình không thuận nghịch?','20.7'),
  topic('giai-thich-vi-mo-entropy','Giải thích vi mô của entropy','Số trạng thái vi mô liên hệ với entropy và chiều diễn biến thế nào?','20.8')
 ],sections:[
  section('engine','Động cơ nhiệt và máy lạnh','20.1–20.5',[
   item('Cân bằng một chu trình động cơ','Qh là nhiệt nhận từ nguồn nóng, Qc là độ lớn nhiệt thải cho nguồn lạnh. W là công có ích trong một chu trình.',[['Công một chu trình',d(String.raw`W=Q_h-Q_c`)],['Hiệu suất nhiệt',d(String.raw`e=W/Q_h=1-Q_c/Q_h`)]]),
   item('Máy lạnh','Qc là nhiệt lấy từ nguồn lạnh, W là công cấp vào, Qh là nhiệt tỏa cho nguồn nóng.',[['Cân bằng năng lượng',d(String.raw`Q_h=Q_c+W`)],['Hệ số làm lạnh',d(String.raw`K=Q_c/W`)],['Hệ số bơm nhiệt',d(String.raw`K_h=Q_h/W`)]]),
   item('Chu trình Otto lý tưởng','Khí lý tưởng với gamma không đổi. r là tỉ số thể tích lớn nhất trên thể tích nhỏ nhất.',[['Hiệu suất Otto',d(String.raw`e=1-r^{1-\gamma}`)]]),
   item('Nguyên lý thứ hai','Không có động cơ tuần hoàn chỉ nhận nhiệt từ một nguồn rồi biến toàn bộ thành công. Không có quá trình mà kết quả duy nhất là chuyển nhiệt từ vật lạnh sang vật nóng.')
  ]),
  section('carnot','Giới hạn Carnot','20.6',[
   item('Động cơ thuận nghịch hai nguồn','Th lớn hơn Tc và cả hai là nhiệt độ tuyệt đối. Nguồn có nhiệt độ không đổi.',[['Tỉ số nhiệt trao đổi',d(String.raw`Q_c/Q_h=T_c/T_h`)],['Hiệu suất Carnot',d(String.raw`e_C=1-T_c/T_h`)],['Giới hạn mọi động cơ hai nguồn',d(String.raw`e\le e_C`)]]),
   item('Máy lạnh Carnot','Máy lạnh thuận nghịch làm việc giữa đúng hai nguồn ở nhiệt độ tuyệt đối Th và Tc.',[['Hệ số làm lạnh',d(String.raw`K_C=T_c/(T_h-T_c)`)]])
  ]),
  section('entropy','Entropy vĩ mô và vi mô','20.7–20.8',[
   item('Độ biến thiên entropy','Tính theo một đường thuận nghịch nối cùng hai trạng thái cân bằng. Không thay nhiệt thực của một đường không thuận nghịch vào công thức này.',[['Định nghĩa theo đường thuận nghịch',d(String.raw`\Delta S=\int_i^f\frac{\delta Q_{\mathrm{rev}}}{T}`)],['Truyền nhiệt thuận nghịch đẳng nhiệt',d(String.raw`\Delta S=Q_{\mathrm{rev}}/T`)]]),
   item('Hệ cô lập và toàn thể','Tổng entropy của hệ cô lập không giảm. Dấu bằng ứng với quá trình thuận nghịch trong mô hình xét.',[['Nguyên lý tăng entropy',d(String.raw`\Delta S_{\mathrm{tot}}\ge0`)]]),
   item('Khí lý tưởng','Lượng khí không đổi, CV có thể coi không đổi. Hai dòng đóng góp cộng lại thành độ biến thiên entropy.',[['Phần do thay đổi nhiệt độ',d(String.raw`\Delta S_T=nC_V\ln(T_2/T_1)`)],['Phần do thay đổi thể tích',d(String.raw`\Delta S_V=nR\ln(V_2/V_1)`)],['Tổng',d(String.raw`\Delta S=\Delta S_T+\Delta S_V`)]]),
   item('Diễn giải thống kê','Omega là số trạng thái vi mô tương thích với trạng thái vĩ mô trong mô hình các trạng thái vi mô đồng xác suất.',[['Hệ thức Boltzmann',d(String.raw`S=k_B\ln\Omega`)]])
  ])]}
}

export const physics1PriorityCourseData=Object.fromEntries(Object.entries(definitions).map(([chapter,data])=>{
 const number=Number(chapter)
 const extra={
  'Tấm chữ nhật đồng chất':'Nếu đổi vị trí hoặc hướng của trục, phải tính lại mômen quán tính theo trục mới.',
  'Vật rắn quay quanh trục cố định':'Dấu của gia tốc góc theo trục được quyết định bởi tổng mômen lực có dấu theo chính trục đó.',
  'Động năng vật rắn':'Vận tốc khối tâm và vận tốc góc mô tả hai phần của cùng chuyển động vật rắn.',
  'Trọng tâm trong trường đều':'Trong trường không đều, cần phân biệt khối tâm với điểm đặt tương đương của trọng lực.',
  'Trượt':'Biến dạng trượt mô tả thay đổi hình dạng, còn nén đều từ mọi phía mô tả biến đổi thể tích.',
  'Các lớp nối tiếp':'Chênh lệch nhiệt độ của từng lớp tỉ lệ nhiệt trở của lớp khi các lớp truyền cùng dòng nhiệt.',
  'Phân bố đều năng lượng':'Lượng tử hóa có thể làm một số bậc tự do quay hoặc dao động chưa đóng góp theo giá trị cổ điển.',
  'Chu trình Otto lý tưởng':'Tỉ số nén là một tham số của mô hình chu trình, còn gamma phụ thuộc mô hình nhiệt dung của môi chất.',
  'Máy lạnh Carnot':'Chênh lệch nhiệt độ hai nguồn càng nhỏ thì hệ số làm lạnh thuận nghịch càng lớn.',
  'Diễn giải thống kê':'Entropy cộng được khi số trạng thái vi mô của hai hệ độc lập nhân với nhau.'
 }
 const topicGroups=[{title:number<17?'Chuyển động quay và vật rắn':'Nhiệt học và nhiệt động lực học',topics:data.topics}]
 const slides=data.sections.flatMap(group=>group.items.filter(i=>i.formulaRows.length||i.name==='Nguyên lý không'||i.name==='Nguyên lý thứ hai').map(i=>{
  const bullets=i.description.split(/(?<=\.)\s+(?=[A-ZÀ-Ỹ])/u)
  if(bullets.length===1&&i.formulaRows.length>1){
   const relation=i.formulaRows.at(-1)
   bullets.push(relation.label+':\n\n'+relation.formula)
  }
  if(bullets.length===1&&extra[i.name])bullets.push(extra[i.name])
  return slide(data.slug,i.name,bullets,i.formulaRows[0]?.formula.replace(/^\$\$\n|\n\$\$$/g,'')||'')
 }))
 return [number,{...data,topicGroups,slides,cheatsheet:{summary:'Định nghĩa, tính chất, công thức và điều kiện áp dụng của '+(number<17?'chuyển động quay và vật rắn.':'nhiệt học.'),sections:data.sections}}]
}))
