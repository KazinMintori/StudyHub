const term=(name,aliases,definition,example,use,question,answer)=>({name,aliases:[name,...aliases],definition,example,use,question,answer})
const ref='\n\nTài liệu tham khảo: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 29, trang 953–977.'
export const inductionConcepts={
 'dien-truong-bao-toan':term('Điện trường bảo toàn',['điện trường bảo toàn','điện trường tĩnh bảo toàn'],String.raw`Điện trường bảo toàn có công trên một điện tích chỉ phụ thuộc hai điểm đầu cuối. Tích phân đường kín bằng không, nên có thể mô tả bằng thế điện: $\vec E=-\nabla V$.`,String.raw`Điện trường của điện tích đứng yên có công tổng bằng không khi điện tích thử trở lại điểm xuất phát theo đường kín.`, 'Phân biệt điện thế giữa hai điểm với suất điện động quanh mạch.', 'Có thể dùng hiệu điện thế giữa hai điểm trùng nhau để mô tả công khác không quanh một đường kín không?', 'Không. Đó là dấu hiệu trường đang xét không bảo toàn.'),
 'cam-ung-dien-tu':term('Cảm ứng điện từ',['cảm ứng điện từ'],String.raw`Cảm ứng điện từ là sự xuất hiện suất điện động do từ thông qua mạch biến thiên. Sự thay đổi có thể đến từ trường biến thiên, chuyển động của mạch hoặc biến dạng mạch. Mạch kín có thể có dòng cảm ứng, còn mạch hở vẫn có thể có suất điện động.`,String.raw`Đưa nam châm lại gần cuộn dây nối điện kế làm kim lệch trong thời gian từ thông biến đổi. Giữ nam châm đứng yên không duy trì dòng ấy.`, 'Phân tích máy phát, cuộn thu, lực hãm từ và tín hiệu điện do trường biến thiên.', 'Có bắt buộc nam châm hoặc mạch phải chuyển động mới có cảm ứng không?', 'Không. Hai cuộn đứng yên vẫn có thể cảm ứng khi dòng nguồn biến thiên.'),
 'dinh-luat-faraday':term('Định luật Faraday',['định luật Faraday','định luật cảm ứng Faraday'],String.raw`Suất điện động quanh một vòng kín theo chiều đã chọn bằng số đối của tốc độ biến thiên từ thông: $\mathcal E=-d\Phi_B/dt$. Với N vòng nối tiếp có cùng từ thông, suất điện động tổng gấp N lần.`,String.raw`Vòng diện tích $0{,}012\,\mathrm{m^2}$ trong trường vuông góc tăng $0{,}020\,\mathrm{T/s}$ có suất điện động độ lớn $0{,}24\,\mathrm{mV}$.`, 'Tìm suất điện động khi trường, diện tích hoặc hướng mạch thay đổi.', 'Từ thông lớn nhưng không đổi có tạo suất điện động cảm ứng không?', 'Không. Đạo hàm từ thông bằng không.'),
 'dinh-luat-lenz':term('Định luật Lenz',['định luật Lenz','quy tắc Lenz'],String.raw`Chiều của hiệu ứng cảm ứng chống lại sự thay đổi đã gây ra nó. Dòng cảm ứng chống biến thiên từ thông, không nhất thiết chống từ trường ngoài.`,String.raw`Trường hướng lên đang giảm làm vòng kín có dòng tạo trường hướng lên. Nhìn từ trên, dòng ấy ngược chiều kim đồng hồ.`, 'Tìm chiều dòng, cực tính và lực cản do cảm ứng.', 'Trường cảm ứng có luôn ngược chiều trường ngoài không?', 'Không. Khi từ thông ngoài giảm, trường cảm ứng có thể cùng chiều để duy trì từ thông.'),
 'suat-dien-dong-chuyen-dong':term('Suất điện động do chuyển động',['suất điện động chuyển động','suất điện động do chuyển động'],String.raw`Suất điện động do chuyển động xuất hiện vì lực từ trên điện tích trong vật dẫn chuyển động. Đóng góp của phần tử dây là $d\mathcal E=(\vec v\times\vec B)\cdot d\vec\ell$.`,String.raw`Thanh dài $0{,}10\,\mathrm m$, chuyển động $2{,}5\,\mathrm{m/s}$ trong trường $0{,}60\,\mathrm T$, với ba phương vuông góc, có suất điện động $0{,}15\,\mathrm V$.`, 'Tính hiệu điện thế thanh chuyển động, máy phát thanh trượt và đĩa Faraday.', 'Có dùng toàn bộ tốc độ trong vBL khi vận tốc không vuông góc trường không?', 'Không. Phải lấy tích có hướng rồi chiếu dọc vật dẫn.'),
 'dien-truong-cam-ung':term('Điện trường cảm ứng',['điện trường cảm ứng','điện trường không tĩnh điện'],String.raw`Điện trường cảm ứng do từ trường biến thiên có tuần hoàn quanh đường kín cố định bằng $-d\Phi_B/dt$. Trường này không bảo toàn và tồn tại cả khi không có dây dẫn.`,String.raw`Dòng tăng trong ống dây tạo điện trường tiếp tuyến quanh trục, kể cả ngoài vùng có từ trường gần đúng bằng không.`, 'Giải thích lực làm điện tích chạy trong vòng đứng yên và tính điện trường quanh ống dây.', 'Điện trường cảm ứng có nhất thiết chỉ tồn tại bên trong vật dẫn không?', 'Không. Vật dẫn là phương tiện phát hiện trường, không phải điều kiện trường tồn tại.'),
 'dong-dien-foucault':term('Dòng điện Fu-cô',['dòng Fu-cô','dòng điện Fu-cô','dòng Foucault','dòng điện xoáy','eddy current'],String.raw`Dòng Fu-cô là các dòng cảm ứng khép kín trong thể tích một vật dẫn khi từ thông biến thiên. Chúng gây lực từ, tỏa nhiệt và tạo trường thứ cấp.`,String.raw`Đĩa kim loại quay qua một vùng từ trường cục bộ xuất hiện dòng Fu-cô làm lực từ hãm quay.`, 'Giải thích hãm từ, lò cảm ứng, máy dò kim loại và tổn hao lõi biến áp.', 'Đổi chiều từ trường có làm lực hãm tự biến thành lực đẩy chuyển động không?', 'Không. Chiều dòng cũng đổi để lực vẫn chống chuyển động gây cảm ứng.'),
 'dong-dien-dich':term('Dòng điện dịch',['dòng điện dịch','dòng dịch','displacement current'],String.raw`Dòng điện dịch qua một mặt là đại lượng $i_D=\varepsilon\,d\Phi_E/dt$ trong môi trường tuyến tính có điện thẩm không đổi. Nó biểu diễn tác dụng tạo từ trường của điện trường biến thiên.`,String.raw`Tụ lý tưởng đang nạp có dòng dịch tổng trong khe bằng dòng dẫn trong dây nạp, dù không có dòng dẫn xuyên điện môi.`, 'Dùng Ampere–Maxwell cho tụ đang nạp và vùng có điện trường biến thiên.', 'Dòng dịch có phải luôn là dòng điện tích tự do đi qua chất cách điện không?', 'Không. Nó được xác định từ thông lượng điện biến thiên.'),
 'phuong-trinh-maxwell':term('Các phương trình Maxwell',['phương trình Maxwell','các phương trình Maxwell','hệ Maxwell'],String.raw`Bốn phương trình Maxwell gồm Gauss cho điện trường, Gauss cho từ trường, Faraday và Ampere có dòng điện dịch. Chúng liên hệ trường điện từ với điện tích, dòng dẫn và biến thiên của trường.`,String.raw`Trong chân không không có dòng dẫn, điện trường biến thiên vẫn có thể tạo từ trường. Sự liên hệ hai chiều dẫn đến sóng điện từ.`, 'Chọn quan hệ trường và nguồn đúng cho bài toán điện từ tổng quát.', 'Chỉ dùng Ampere dạng từ tĩnh có đủ cho tụ đang nạp không?', 'Không. Phải kể dòng điện dịch.'),
 'sieu-dan':term('Siêu dẫn',['siêu dẫn','trạng thái siêu dẫn','superconductivity'],String.raw`Siêu dẫn là trạng thái vật liệu có điện trở bằng không và các tính chất từ đặc biệt dưới điều kiện nhiệt độ, từ trường và dòng phù hợp. Hiệu ứng Meissner phân biệt trạng thái này với việc chỉ có điện trở bằng không.`,String.raw`Một mẫu siêu dẫn ở trạng thái Meissner đẩy từ thông khỏi phần khối và có thể tạo lực đẩy lên nam châm.`, 'Phân tích nam châm siêu dẫn, ngưỡng chuyển pha và lực nâng từ.', 'Chỉ nói điện trở bằng không đã mô tả đầy đủ siêu dẫn chưa?', 'Chưa. Cần xét tính chất từ và điều kiện tồn tại pha.'),
 'nhiet-do-toi-han-sieu-dan':term('Nhiệt độ tới hạn siêu dẫn',['nhiệt độ tới hạn siêu dẫn','nhiệt độ chuyển pha siêu dẫn'],String.raw`Nhiệt độ tới hạn siêu dẫn $T_c$ là ngưỡng chuyển giữa pha thường và pha siêu dẫn trong điều kiện trường đã xác định. Trường ngoài có thể làm ngưỡng này giảm.`,String.raw`Thủy ngân chuyển sang siêu dẫn ở nhiệt độ thấp hơn khi đặt trong trường ngoài mạnh hơn, trong miền đường tới hạn cho phép.`, 'Đọc giản đồ pha và xác định điều kiện làm lạnh.', 'Một nhiệt độ thấp hơn ngưỡng khi không có trường có luôn bảo đảm siêu dẫn trong trường mạnh không?', 'Không. Trường có thể làm mất pha siêu dẫn.'),
 'tu-truong-toi-han-sieu-dan':term('Từ trường tới hạn siêu dẫn',['từ trường tới hạn siêu dẫn','trường tới hạn siêu dẫn'],String.raw`Trường tới hạn $B_c$ là độ lớn trường nhỏ nhất làm mất trạng thái siêu dẫn loại I ở một nhiệt độ đang xét. Giá trị phụ thuộc nhiệt độ và vật liệu.`,String.raw`Vanadi gần độ không tuyệt đối có trường tới hạn khoảng $0{,}142\,\mathrm T$. Trường ngoài $0{,}260\,\mathrm T$ làm mẫu ở pha thường trong mô hình bài toán.`, 'So sánh trường ngoài với đường chuyển pha.', 'B_c có phải cùng một hằng số cho mọi nhiệt độ không?', 'Không. Phải đọc tại nhiệt độ đang xét.'),
 'hieu-ung-meissner':term('Hiệu ứng Meissner',['hiệu ứng Meissner','sự đẩy từ thông'],String.raw`Hiệu ứng Meissner là sự đẩy từ thông khỏi phần khối khi vật liệu chuyển vào trạng thái siêu dẫn phù hợp. Trường trong khối bằng không, ngoại trừ tầng bề mặt rất mỏng.`,String.raw`Một quả cầu được làm lạnh qua chuyển pha trong trường ngoài đủ nhỏ làm các đường sức bị đẩy ra ngoài và từ thông qua khối giảm về không.`, 'Giải thích tính nghịch từ của trạng thái siêu dẫn và lực nâng nam châm.', 'Mọi trạng thái của chất siêu dẫn loại II đều có trường bằng không trong toàn khối không?', 'Không. Miền hỗn hợp cho từ thông đi vào theo các sợi hoặc xoáy từ.'),
 'sieu-dan-loai-i':term('Siêu dẫn loại I',['siêu dẫn loại I','chất siêu dẫn loại I'],String.raw`Siêu dẫn loại I có một đường trường tới hạn B_c(T) trong mô tả của chương. Dưới ngưỡng phù hợp, trạng thái Meissner đẩy từ thông khỏi khối. Trên ngưỡng, vật liệu ở pha thường.`, 'Thủy ngân và mô hình trụ vanadi minh họa giản đồ một trường tới hạn.', 'Phân biệt giản đồ pha và đáp ứng từ của các loại siêu dẫn.', 'Loại I có miền hỗn hợp rộng giữa Bc1 và Bc2 như loại II không?', 'Không trong phân loại và mô hình đang xét.'),
 'sieu-dan-loai-ii':term('Siêu dẫn loại II',['siêu dẫn loại II','chất siêu dẫn loại II'],String.raw`Siêu dẫn loại II có hai trường tới hạn $B_{c1}$ và $B_{c2}$. Giữa hai ngưỡng, từ thông đi vào theo các sợi trong khi phần vật liệu còn lại vẫn siêu dẫn. Trên B_c2, vật liệu chuyển sang pha thường.`, 'Dây siêu dẫn loại II được dùng trong nam châm điện mạnh vì có thể duy trì phần siêu dẫn ở trường lớn.', 'Mô tả trạng thái hỗn hợp và vật liệu cho nam châm siêu dẫn.', 'Từ thông đi vào một phần vật liệu có đồng nghĩa toàn mẫu đã mất siêu dẫn không?', 'Không. Trong miền hỗn hợp vẫn còn phần siêu dẫn liên tục.'),
 'dao-dong-tat-dan':term('Dao động tắt dần',['dao động tắt dần','dao động có lực cản tuyến tính'],String.raw`Dao động tắt dần có năng lượng cơ giảm vì lực cản. Với lực cản tỉ lệ vận tốc, phương trình là $m\ddot x+b\dot x+kx=0$. Dao động còn xảy ra khi $b^2<4mk$.`,String.raw`Thanh trượt nối lò xo trong mạch kín có hệ số cản từ $b=B^2W^2/R$. Cơ năng mất đi chuyển thành nhiệt trong điện trở.`, 'Giải chuyển động của hệ lò xo có hãm điện từ và giữ đúng điều kiện ban đầu.', 'Nghiệm chỉ chứa cosin nhân hàm mũ có tự động thỏa điều kiện thả từ nghỉ không?', 'Không. Nói chung cần pha hoặc cả số hạng sin để đạo hàm ban đầu bằng không.')
}
export const inductionWikiDetails={
 'dien-truong-bao-toan':String.raw`Điện trường tĩnh của điện tích đứng yên có công không phụ thuộc đường đi. Với hai điểm a và b, công trên một đơn vị điện tích bằng V_a−V_b. Khi quay về cùng điểm, công bằng không:

$$
\oint\vec E\cdot d\vec\ell=0.
$$

Từ trường biến thiên có thể tạo điện trường với tuần hoàn khác không. Khi ấy không thể dùng một thế điện vô hướng duy nhất để mô tả toàn bộ trường. Tuy nhiên, tổng điện trường vẫn có thể gồm phần bảo toàn do điện tích và phần cảm ứng không bảo toàn.`+ref,
 'cam-ung-dien-tu':String.raw`Cần phân biệt ba đại lượng: Từ thông, suất điện động và dòng điện. Từ thông là thông lượng từ trường qua mặt có định hướng. Suất điện động là công của lực tạo nguồn trên một đơn vị điện tích quanh mạch. Dòng còn phụ thuộc đường dẫn kín và điện trở.

Một vòng có thể đứng yên mà vẫn cảm ứng khi trường biến thiên. Một vòng cũng có thể chuyển động trong trường không đổi nhưng không có suất điện động tổng nếu từ thông giữ nguyên. Trường hợp vòng chữ nhật tịnh tiến hoàn toàn trong từ trường đều minh họa sự triệt tiêu giữa các cạnh.

Nguồn năng lượng điện đến từ cơ năng của tác nhân chuyển động hoặc nguồn làm trường biến thiên. Cảm ứng không tạo năng lượng từ hư không.`+ref,
 'dinh-luat-faraday':String.raw`Trước hết xét một vòng và chọn pháp tuyến. Chiều dương đi quanh vòng được xác định bằng quy tắc bàn tay phải. Khi từ thông dương tăng, suất điện động có dấu âm.

Với hai vòng nối tiếp có cùng từ thông, cộng hai suất điện động. Với N vòng, N là số nguyên dương:

$$
\begin{aligned}
&\mathcal E_{\mathrm{tổng}}
=\mathcal E_1+\mathcal E_2+\dots+\mathcal E_N\\
&\quad=-N\frac{d\Phi_B}{dt}.
\end{aligned}
$$

Từ thông có thể đổi vì trường, diện tích, hướng mặt hoặc phối hợp các yếu tố. Khi trường không đều, cần tích phân trên diện tích trước khi lấy đạo hàm. Giá trị từ thông lớn không tự bảo đảm suất điện động lớn.`+ref,
 'dinh-luat-lenz':String.raw`Bắt đầu bằng hướng từ thông nguồn qua vòng. Sau đó xác định nó tăng hay giảm. Trường cảm ứng phải chống sự thay đổi ấy, rồi quy tắc bàn tay phải cho chiều dòng.

Nếu trường hướng lên tăng, trường cảm ứng hướng xuống. Nếu trường hướng lên giảm, trường cảm ứng hướng lên. Hai trường hợp cho thấy việc nói dòng luôn chống trường ngoài là sai.

Với thanh trượt, lực từ cản chuyển động sinh dòng. Đảo trường cũng đảo dòng, nên không thể làm lực hãm tự trở thành lực kéo tăng tốc mà không có năng lượng bên ngoài.`+ref,
 'suat-dien-dong-chuyen-dong':String.raw`Điện tích trong phần tử vật dẫn chuyển động chịu lực từ trên một đơn vị điện tích bằng tích có hướng của vận tốc vật dẫn với trường. Thành phần dọc dây tạo suất điện động.

$$
\mathcal E=\oint(\vec v\times\vec B)\cdot d\vec\ell.
$$

Vận tốc và trường có thể thay đổi theo vị trí. Công thức vBL là trường hợp đặc biệt với ba phương vuông góc và trường đều. Thanh cô lập phân bố điện tích đến khi điện trường cân bằng lực từ, nên vẫn có hiệu điện thế dù chưa có dòng vòng.

Biểu thức trên chỉ mô tả phần do chuyển động. Với dây đứng yên trong trường biến thiên, cần xét điện trường cảm ứng.`+ref,
 'dien-truong-cam-ung':String.raw`Một vòng đứng yên nằm ngoài ống dây dài vẫn có dòng khi dòng trong ống biến thiên. Từ trường ngoài được bỏ qua trong mô hình, nên lực từ không giải thích được chuyển động điện tích. Tác nhân là điện trường cảm ứng.

Với đường kín đứng yên,

$$
\oint\vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt}.
$$

Đối xứng trụ cho điện trường tiếp tuyến. Nếu trường chỉ có trong ống bán kính a thì khi đường tích phân ở ngoài, từ thông chỉ qua diện tích πa². Không dùng diện tích vòng lớn πr² để tính từ thông của ống.`+ref,
 'dong-dien-foucault':String.raw`Khối kim loại không có một đường dây định trước vẫn cho phép điện tích chạy theo các đường kín. Khi khối đi qua vùng trường hoặc trường biến thiên, các đường dòng ấy có suất điện động cảm ứng.

Trong đĩa quay qua trường cục bộ, một phần đường dòng nằm trong trường chịu lực hãm, còn phần hồi ngoài trường không chịu lực ấy. Cơ năng giảm và nhiệt tăng. Hiện tượng được dùng để hãm, nung và dò vật dẫn. Trong lõi máy biến áp, cùng hiệu ứng tạo tổn hao cần hạn chế.`+ref,
 'dong-dien-dich':String.raw`Tụ đang nạp đặt ra mâu thuẫn nếu chỉ dùng Ampere từ tĩnh: Một mặt căng cắt dây có dòng dẫn, mặt khác cùng biên đi qua khe tụ không có dòng dẫn. Thông lượng điện trong khe đang tăng cung cấp số hạng còn thiếu.

Với tụ phẳng có điện thẩm không đổi,

$$
\begin{aligned}
q&=\varepsilon\Phi_E,\\
i_C&=\frac{dq}{dt},\\
i_D&=\varepsilon\frac{d\Phi_E}{dt}.
\end{aligned}
$$

Dòng dịch tổng qua khe bằng dòng dẫn trong dây nạp. Trong điện môi lý tưởng, điều này không có nghĩa có dòng dẫn xuyên khe. Điện trường biến thiên trong vật dẫn cũng có thể tạo dòng dịch đồng thời với dòng dẫn.`+ref,
 'phuong-trinh-maxwell':String.raw`Dạng tích phân trong chân không gồm hai quan hệ mặt kín và hai quan hệ đường kín đứng yên:

$$
\oint\vec E\cdot d\vec A=\frac{Q_{\mathrm{encl}}}{\varepsilon_0}.
$$

$$
\oint\vec B\cdot d\vec A=0.
$$

$$
\oint\vec E\cdot d\vec\ell=-\frac{d\Phi_B}{dt}.
$$

$$
\begin{aligned}
&\oint\vec B\cdot d\vec\ell\\
&\quad=\mu_0(i_C)_{\mathrm{encl}}\\
&\quad+\mu_0\varepsilon_0\frac{d\Phi_E}{dt}.
\end{aligned}
$$

Dòng và thông lượng ở phương trình cuối tính trên cùng mặt căng. Các phương trình dùng điện trường tổng. Trong chân không không có nguồn, trường biến thiên vẫn liên hệ với trường kia và có thể lan truyền thành sóng điện từ.`+ref,
 'sieu-dan':String.raw`Hạ nhiệt độ qua ngưỡng phù hợp có thể làm điện trở vật liệu đột ngột biến mất. Siêu dẫn còn có đáp ứng từ đặc trưng, được mô tả qua Meissner và các trường tới hạn.

Điện trở bằng không tự nó chỉ nói không có hao phí Joule trên đường dẫn. Hiệu ứng Meissner còn đòi hỏi từ thông bị đẩy khỏi khối trong trạng thái phù hợp. Vì vậy không nên đồng nhất mọi chất dẫn hoàn hảo với toàn bộ tính chất của chất siêu dẫn.

Nam châm điện siêu dẫn tạo trường mạnh mà không có tổn hao điện trở trong cuộn. Hệ thống vẫn cần duy trì điều kiện nhiệt độ và giới hạn trường, dòng của vật liệu.`+ref,
 'nhiet-do-toi-han-sieu-dan':String.raw`Nhiệt độ tới hạn được đọc trên giản đồ pha theo điều kiện trường ngoài. Với loại I, đường B_c(T) phân chia pha thường và pha siêu dẫn. Tăng trường ngoài làm chuyển pha xảy ra ở nhiệt độ thấp hơn.

Kelvin là đơn vị dùng khi đọc nhiệt độ tuyệt đối. Việc nhiệt độ thấp hơn T_c tại trường bằng không không đủ để kết luận mẫu vẫn siêu dẫn trong một trường ngoài tùy ý.`+ref,
 'tu-truong-toi-han-sieu-dan':String.raw`Trường tới hạn phụ thuộc vật liệu và nhiệt độ. Khi xét trụ loại I dài song song trường, ở xa đầu và dưới ngưỡng, Meissner cho trường trong khối bằng không.

Quan hệ giữa trường ngoài và độ từ hóa khi đó là

$$
\vec M=-\frac{\vec B_0}{\mu_0}.
$$

Trên ngưỡng, vật chuyển pha thường và không còn áp dụng điều kiện trường trong bằng không. Không dùng một B_c duy nhất để thay hai ngưỡng của vật liệu loại II.`+ref,
 'hieu-ung-meissner':String.raw`Xét mẫu ở pha thường trong trường ngoài đủ nhỏ, rồi làm lạnh qua chuyển pha. Trường trong phần khối giảm về không và các đường sức bị đẩy ra ngoài. Một tầng bề mặt mỏng có thể mang dòng tạo đáp ứng ấy.

Trường bị dồn quanh mẫu và có thể tạo lực đẩy lên nam châm. Với chất siêu dẫn loại II trong miền hỗn hợp, từ thông có thể vào theo các sợi, nên phải xác định trạng thái trước khi kết luận trường khối bằng không.`+ref,
 'sieu-dan-loai-i':String.raw`Trong mô tả loại I, một đường B_c(T) phân chia trạng thái Meissner và pha thường. Bên dưới đường tới hạn, từ thông bị đẩy khỏi khối. Khi trường quá lớn hoặc nhiệt độ quá cao, mẫu trở về pha thường.

Tính chất này được dùng khi giải trường và độ từ hóa trong trụ vanadi. Phải tránh vùng hai đầu để giả thiết trường dọc trục và bỏ qua hiệu ứng hình học đầu trụ.`+ref,
 'sieu-dan-loai-ii':String.raw`Dưới B_c1, mẫu có thể ở trạng thái Meissner. Giữa B_c1 và B_c2, các sợi chứa từ thông xuất hiện trong phần vật liệu còn siêu dẫn. Trên B_c2, trạng thái thường chiếm toàn vật.

Một đường siêu dẫn liên tục có thể giữ điện trở giữa hai đầu bằng không trong mô hình dòng dưới ngưỡng. Sự chuyển động các xoáy từ và giới hạn dòng là những điều kiện cần xét khi mô tả tổn hao thực tế, nên không suy rằng mọi dòng ở mọi trạng thái hỗn hợp đều không hao phí.`+ref,
 'dao-dong-tat-dan':String.raw`Với lực hồi phục −kx và lực cản −bẋ, phương trình động lực học là

$$
m\ddot x+b\dot x+kx=0.
$$

Đặt α=b/(2m). Trong miền dao động còn tồn tại, tần số góc là

$$
\omega_d=\sqrt{\frac km-\alpha^2}.
$$

Nếu thả từ nghỉ tại x₀, nghiệm phải giữ cả hai điều kiện ban đầu:

$$
\begin{aligned}
&x(t)=x_0e^{-\alpha t}\cos\omega_dt\\
&\quad+x_0e^{-\alpha t}\frac\alpha{\omega_d}\sin\omega_dt.
\end{aligned}
$$

Trong thanh trượt nối lò xo, b=B²W²/R. Mất mát cơ năng bằng công suất nhiệt I²R trong mạch. Khi b²≥4mk, không dùng công thức dao động hình sin của miền tắt dần yếu.`+ref
}
export const inductionWikiConnections={
 'dien-truong-bao-toan':['dien-the','dien-truong-cam-ung','tich-phan'],
 'cam-ung-dien-tu':['tu-thong','dinh-luat-faraday','dinh-luat-lenz'],
 'dinh-luat-faraday':['tu-thong','dao-ham','dinh-luat-lenz'],
 'dinh-luat-lenz':['dinh-luat-faraday','dong-dien','tu-truong'],
 'suat-dien-dong-chuyen-dong':['suat-dien-dong','luc-tu-tren-dien-tich','tich-co-huong'],
 'dien-truong-cam-ung':['dien-truong-bao-toan','dinh-luat-faraday','ong-day-dien'],
 'dong-dien-foucault':['dinh-luat-lenz','dien-tro','cam-ung-dien-tu'],
 'dong-dien-dich':['dien-dung','do-dien-tham','phuong-trinh-maxwell'],
 'phuong-trinh-maxwell':['dinh-luat-gauss','dinh-luat-ampere','dinh-luat-faraday','dong-dien-dich'],
 'sieu-dan':['hieu-ung-meissner','sieu-dan-loai-i','sieu-dan-loai-ii'],
 'nhiet-do-toi-han-sieu-dan':['sieu-dan','tu-truong-toi-han-sieu-dan'],
 'tu-truong-toi-han-sieu-dan':['sieu-dan','do-tu-hoa','nhiet-do-toi-han-sieu-dan'],
 'hieu-ung-meissner':['nghich-tu','sieu-dan','dinh-luat-lenz'],
 'sieu-dan-loai-i':['sieu-dan','tu-truong-toi-han-sieu-dan','hieu-ung-meissner'],
 'sieu-dan-loai-ii':['sieu-dan','sieu-dan-loai-i','hieu-ung-meissner'],
 'dao-dong-tat-dan':['dao-dong-dieu-hoa','momen-quan-tinh','dong-dien-foucault']
}
