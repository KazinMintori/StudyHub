const term = (name, aliases, definition, example, use, question, answer) => ({ name, aliases: [name, ...aliases], definition, example, use, question, answer })
const ref = '\n\nTài liệu tham khảo: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 28, trang 918–943.'

export const sourcesConcepts = {
  'momen-dong-luong': term('Mômen động lượng', ['mômen động lượng', 'động lượng góc'], String.raw`Mômen động lượng của một hạt đối với gốc đã chọn là $\vec L=\vec r\times\vec p$. Vector vị trí $\vec r$ tính từ gốc đến hạt, còn $\vec p$ là động lượng. Đại lượng này phụ thuộc gốc chọn và có đơn vị $\mathrm{kg\,m^2/s}$.`, String.raw`Nếu $\vec r=(2,0,0)\,\mathrm m$ và $\vec p=(0,3,0)\,\mathrm{kg\,m/s}$, thì $\vec L=(0,0,6)\,\mathrm{kg\,m^2/s}$.`, 'Phân tích chuyển động quay, tương tác mômen từ với từ trường và tiến động.', 'Hạt có động lượng khác không có luôn có mômen động lượng khác không đối với mọi gốc không?', 'Không. Nếu vector vị trí cùng phương với động lượng, tích có hướng bằng không.'),

  'dinh-luat-biot-savart': term(String.raw`Định luật Biot–Savart`, [String.raw`Biot–Savart`, String.raw`định luật Biot-Savart`], String.raw`Định luật Biot–Savart cho biết phần tử dòng điện $I\,d\vec l$ tạo tại điểm cách nó vector vị trí tương đối $\vec r$ một đóng góp từ trường $d\vec B=\frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}$. Cần cộng vector các đóng góp trên toàn dòng điện.`, String.raw`Một đoạn dây ngắn 1,0 mm mang dòng 2,0 A tạo trường khoảng 20 nT tại điểm cách 10 cm theo phương vuông góc. Đây là gần đúng phần tử dòng, vì chiều dài đoạn nhỏ so với khoảng cách.`, String.raw`Tính trường do dây dẫn có hình dạng xác định.`, String.raw`Tích có hướng khiến $d\vec B$ song song với $d\vec l$ không?`, String.raw`Không. Nó vuông góc với cả $d\vec l$ và $\hat r$.`),
  'dinh-luat-ampere': term(String.raw`Định luật Ampere`, [String.raw`định luật Ampe`, String.raw`định luật vòng Ampere`], String.raw`Trong từ tĩnh, tích phân đường kín của thành phần tiếp tuyến từ trường bằng $\mu_0$ nhân tổng đại số dòng điện xuyên qua mặt được đường kín bao: $\oint\vec B\cdot d\vec l=\mu_0 I_{\mathrm{encl}}$.`, String.raw`Hai dòng 3,0 A và 1,0 A xuyên qua mặt theo hai chiều ngược nhau. Chọn chiều 3,0 A là dương, dòng bao bằng 2,0 A. Nếu hai dòng bằng nhau, tích phân bằng không dù trường tại từng điểm có thể khác không.`, String.raw`Tính trường khi phân bố dòng có đối xứng thích hợp.`, String.raw`Tích phân Ampere bằng không có buộc từ trường bằng không từng điểm không?`, String.raw`Không. Nó chỉ khẳng định tổng tích phân đường bằng không.`),
  'do-tu-hoa': term(String.raw`Độ từ hóa`, [String.raw`từ hóa`, String.raw`độ từ hóa`], String.raw`Độ từ hóa $\vec M$ là mômen từ tổng cộng trên một đơn vị thể tích. Trong mô hình môi trường đang xét, đóng góp của từ hóa vào trường là $\mu_0\vec M$, nên $\vec B=\vec B_0+\mu_0\vec M$.`, String.raw`Mẫu có mômen từ tổng $0{,}20\,\mathrm{A\,m^2}$ trong thể tích $0{,}010\,\mathrm{m^3}$ có độ từ hóa $20\,\mathrm{A/m}$ theo hướng mômen tổng. Trong mô hình đang xét, đóng góp $\mu_0M$ khoảng $25{,}1\,\mu\mathrm T$.`, String.raw`Mô tả phản ứng vĩ mô của vật liệu từ.`, String.raw`Đơn vị SI của độ từ hóa là gì?`, String.raw`$\mathrm{A/m}$.`) ,
  'do-tu-tham': term(String.raw`Độ từ thẩm`, [String.raw`độ từ thẩm vật liệu`, String.raw`độ từ thẩm tương đối`], String.raw`Trong vật liệu tuyến tính đẳng hướng, độ từ thẩm $\mu$ liên hệ với độ từ thẩm tương đối $K_m$ bởi $\mu=K_m\mu_0$. Khi các giả thiết tuyến tính phù hợp, có thể thay $\mu_0$ bằng $\mu$ trong biểu thức trường.`, String.raw`Vật liệu thuận từ có $K_m>1$ còn vật liệu nghịch từ có $K_m<1$, cả hai thường gần 1.`, String.raw`Liên hệ trường với dòng điện trong môi trường từ tuyến tính.`, String.raw`Có thể xem độ từ thẩm của sắt từ là hằng số độc lập với trường không?`, String.raw`Không nói chung. Vật liệu sắt từ có thể bão hòa và có từ trễ.`),
  'do-cam-tu': term(String.raw`Độ cảm từ`, [String.raw`độ cảm từ`], String.raw`Độ cảm từ $\chi_m$ đo độ lệch của độ từ thẩm tương đối khỏi giá trị 1: $\chi_m=K_m-1$. Trong mô hình tuyến tính đẳng hướng, nó không có thứ nguyên.`, String.raw`Thuận từ có $\chi_m>0$, nghịch từ có $\chi_m<0$.`, String.raw`Phân loại định lượng đáp ứng từ yếu của vật liệu.`, String.raw`Dấu của $\chi_m$ cho biết gì?`, String.raw`Dấu dương chỉ đáp ứng thuận từ, dấu âm chỉ đáp ứng nghịch từ.`),
  'thuan-tu': term(String.raw`Thuận từ`, [String.raw`vật liệu thuận từ`, String.raw`paramagnetism`], String.raw`Vật liệu thuận từ có mômen từ vi mô định hướng một phần theo trường ngoài. Độ cảm từ dương, nên vật liệu bị hút yếu về vùng có trường mạnh.`, String.raw`Oxy khí và nhôm là ví dụ thuận từ được nêu trong chương.`, String.raw`So sánh phản ứng yếu của vật liệu với sắt từ.`, String.raw`Thuận từ có nhất thiết giữ từ hóa mạnh sau khi bỏ trường không?`, String.raw`Không. Mô tả thuận từ cơ bản cho đáp ứng yếu theo trường ngoài.`),
  'nghich-tu': term(String.raw`Nghịch từ`, [String.raw`vật liệu nghịch từ`, String.raw`diamagnetism`], String.raw`Vật liệu nghịch từ tạo mômen từ cảm ứng chống lại trường ngoài. Độ cảm từ âm và gần như không phụ thuộc nhiệt độ đối với nhiều chất rắn và lỏng.`, String.raw`Bitmut có độ cảm từ âm, nên bị đẩy yếu khỏi vùng trường mạnh.`, String.raw`Giải thích đáp ứng cảm ứng ngược chiều trường ngoài.`, String.raw`Dấu của độ cảm từ nghịch từ là gì?`, String.raw`Âm.`),
  'sat-tu': term(String.raw`Sắt từ`, [String.raw`vật liệu sắt từ`, String.raw`ferromagnetism`], String.raw`Trong vật liệu sắt từ, tương tác giữa mômen từ tạo các miền có từ hóa tự phát cùng hướng. Trường ngoài làm các miền đổi hướng hoặc kích thước, tạo đáp ứng mạnh, có thể bão hòa và phụ thuộc lịch sử từ hóa.`, String.raw`Sắt, niken và coban là các vật liệu sắt từ được nêu trong chương.`, String.raw`Phân tích lõi điện từ, nam châm vĩnh cửu và lưu trữ từ.`, String.raw`Quan hệ tuyến tính với một $K_m$ cố định có mô tả đầy đủ sắt từ không?`, String.raw`Không. Cần xét bão hòa và từ trễ.`),
  'bao-hoa-tu': term(String.raw`Bão hòa từ hóa`, [String.raw`bão hòa từ`, String.raw`từ hóa bão hòa`], String.raw`Bão hòa từ hóa là trạng thái độ từ hóa gần đạt cực đại vì gần như mọi mômen vi mô đã định hướng theo trường ngoài. Tăng trường thêm chỉ làm độ từ hóa tăng rất ít.`, String.raw`Trên đường cong từ hóa, bão hòa xuất hiện khi đường cong tiến đến vùng gần nằm ngang.`, String.raw`Nhận biết giới hạn của mô hình đáp ứng tuyến tính.`, String.raw`Khi vật liệu đã bão hòa, độ từ hóa còn tăng tỉ lệ thuận với trường không?`, String.raw`Không còn tăng tuyến tính đáng kể.`),
  'tu-tre': term(String.raw`Từ trễ`, [String.raw`vòng từ trễ`, String.raw`hysteresis`], String.raw`Từ trễ là sự phụ thuộc của độ từ hóa vào lịch sử biến thiên trường ngoài. Khi giảm trường về không, độ từ hóa dư có thể còn lại; cần trường ngược để khử từ.`, String.raw`Vật liệu từ cứng có vòng trễ rộng, còn vật liệu từ mềm có vòng hẹp hơn.`, String.raw`Chọn vật liệu lõi và nam châm theo chu kỳ từ hóa.`, String.raw`Sau khi bỏ trường ngoài, độ từ hóa có luôn bằng không không?`, String.raw`Không. Từ hóa dư có thể tồn tại.`),
  'tu-hoa-du': term(String.raw`Từ hóa dư`, [String.raw`từ dư`, String.raw`remanence`], String.raw`Từ hóa dư là độ từ hóa còn lại sau khi trường ngoài được giảm về không từ trạng thái đã từ hóa. Giá trị này thuộc nhánh từ hóa cụ thể và là một phần của vòng trễ.`, String.raw`Nam châm vĩnh cửu giữ từ hóa dư đáng kể sau khi ngắt trường kích từ.`, String.raw`Mô tả khả năng giữ từ của vật liệu.`, String.raw`Muốn khử từ dư cần làm gì?`, String.raw`Đặt trường ngược đủ lớn để đưa độ từ hóa về không.`),
  'luc-khu-tu': term(String.raw`Trường kháng từ`, [String.raw`trường khử từ`, String.raw`lực kháng từ`, String.raw`coercivity`], String.raw`Trường kháng từ là độ lớn trường ngược cần đặt để đưa độ từ hóa về không sau khi mẫu đã được từ hóa. Nó được đọc trên vòng trễ.`, String.raw`Vật liệu từ cứng có trường kháng từ lớn hơn vật liệu từ mềm trong so sánh vòng trễ.`, String.raw`Đánh giá khả năng chống mất từ của nam châm.`, String.raw`Vật liệu có trường kháng từ lớn có dễ bị khử từ hơn không?`, String.raw`Không. Cần trường ngược lớn hơn.`),
  'hien-tuong-curie': term(String.raw`Định luật Curie`, [String.raw`định luật Curie`, String.raw`định luật Curi`], String.raw`Trong miền áp dụng cho vật liệu thuận từ, độ từ hóa tuân theo $M=CB/T$, với $C$ là hằng số Curie và $T$ là nhiệt độ tuyệt đối. Ở cùng trường, tăng nhiệt độ làm giảm độ từ hóa.`, String.raw`Khi nhiệt độ tăng gấp đôi và trường giữ nguyên, mô hình Curie dự đoán độ từ hóa giảm còn một nửa.`, String.raw`Mô tả ảnh hưởng nhiệt độ lên đáp ứng thuận từ trong miền phù hợp.`, String.raw`Nhiệt độ trong định luật Curie phải là nhiệt độ Celsius hay tuyệt đối?`, String.raw`Nhiệt độ tuyệt đối, tính bằng kelvin.`),
  'ong-day-dien': term(String.raw`Ống dây`, [String.raw`ống dây dài`, String.raw`solenoid`], String.raw`Ống dây là dây dẫn quấn nhiều vòng quanh một hình trụ. Với ống dây đủ dài, trường gần vùng giữa gần đều và có độ lớn $B\approx\mu_0 nI$ trong chân không hoặc môi trường gần đúng không từ tính.`, String.raw`Ống dây dài có $1000\,\mathrm{vòng/m}$, mang dòng $0{,}50\,\mathrm A$, tạo trường khoảng $0{,}628\,\mathrm{mT}$ gần tâm trong không khí.`, String.raw`Tạo trường gần đều trong cuộn cảm và nam châm điện.`, String.raw`Công thức ống dây dài có mô tả chính xác vùng đầu không?`, String.raw`Không. Hiệu ứng đầu làm trường giảm và không còn gần đều.`),
  'ong-day-hinh-xuyen': term(String.raw`Ống dây hình xuyến`, [String.raw`xuyến từ`, String.raw`toroid`], String.raw`Ống dây hình xuyến quấn quanh lõi dạng vòng. Trong mô hình lý tưởng có $N$ vòng, dòng $I$ và đường tròn Ampere bán kính $r$ trong lõi, trường có độ lớn $B(r)=\frac{\mu_0NI}{2\pi r}$.`, String.raw`Xuyến không có lõi từ với 500 vòng, dòng $0{,}20\,\mathrm A$, cho trường $0{,}400\,\mathrm{mT}$ tại bán kính $5{,}0\,\mathrm{cm}$. Ở bán kính gấp đôi trong cùng miền lõi, trường còn một nửa.`, String.raw`Tập trung từ thông trong lõi vòng kín.`, String.raw`Trường trong lõi xuyến có đều theo bán kính không?`, String.raw`Không. Độ lớn tỉ lệ nghịch với bán kính $r$.`),
}


export const sourcesWikiDetails = {
  'momen-dong-luong': String.raw`Trước hết xét một hạt. Mômen động lượng đối với gốc cố định trong hệ quán tính là:

$$
\vec L=\vec r\times\vec p.
$$

Độ lớn bằng khoảng cách vuông góc từ gốc đến đường chuyển động nhân độ lớn động lượng. Vì vậy một hạt có thể có động lượng khác không nhưng mômen động lượng bằng không đối với một gốc cụ thể.

Với hai hạt, mômen tổng là tổng hai vector mômen. Với hệ gồm n hạt, phép cộng được mở rộng theo cùng gốc:

$$
\begin{aligned}
&\vec L_{\mathrm{tổng}} = \vec L_1+\vec L_2+\cdots+\vec L_n,\\
&\vec L_i = \vec r_i\times\vec p_i.
\end{aligned}
$$

Chỉ số i chạy từ 1 đến n. Mômen lực ngoài quyết định tốc độ thay đổi mômen động lượng tổng khi các mômen lực nội triệt tiêu trong hệ đang xét:

$$
\vec\tau_{\mathrm{ngoài}}=\frac{d\vec L_{\mathrm{tổng}}}{dt}.
$$

Với vật rắn quay quanh một trục đối xứng cố định, mômen động lượng dọc trục có độ lớn $I\omega$. Không áp dụng quan hệ vector vô hướng này cho một trục quay bất kỳ mà chưa xét phân bố khối lượng.`+ref,

  'dinh-luat-biot-savart': String.raw`Phần tử dòng điện tạo từ trường tại điểm quan sát theo hướng vuông góc với cả hướng dòng và hướng nối từ phần tử đến điểm đó:

$$
\begin{aligned}
d\vec B&=\frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}.
\end{aligned}
$$

Để tìm trường của cả dây, cộng vector đóng góp trên toàn chiều dài. Định luật phù hợp với phân bố dòng ổn định trong mô hình từ tĩnh.`+ref,
  'dinh-luat-ampere': String.raw`Định luật Ampere trong từ tĩnh liên hệ tích phân đường với dòng điện đại số xuyên qua mặt giới hạn bởi đường ấy:

$$
\oint\vec B\cdot d\vec l=\mu_0 I_{\mathrm{encl}}.
$$

Chiều đường đi và dấu dòng bao liên hệ bằng quy tắc bàn tay phải. Định luật dạng này áp dụng khi dòng không đổi theo thời gian và điện trường không biến thiên theo thời gian. Khi điện trường biến thiên, phương trình Ampere–Maxwell có thêm số hạng dòng điện dịch. Tích phân bằng không không có nghĩa trường bằng không từng điểm.`+ref,
  'do-tu-hoa': String.raw`Độ từ hóa là mật độ mômen từ:

$$
\vec M=\frac{\vec\mu_{\mathrm{total}}}{V}.
$$

Đơn vị SI là ampere trên mét. Trong mô tả vật liệu tuyến tính cơ bản, trường tổng là $\vec B=\vec B_0+\mu_0\vec M$, với $\vec B_0$ do các dòng ngoài vật liệu tạo nên.`+ref,
  'do-tu-tham': String.raw`Độ từ thẩm tuyệt đối $\mu$ có đơn vị $\mathrm{T\,m/A}$. Độ từ thẩm tương đối $K_m=\mu/\mu_0$ không thứ nguyên. Với vật liệu tuyến tính đẳng hướng, quan hệ $\mu=K_m\mu_0$ cho phép biểu diễn đáp ứng của môi trường trong các công thức thích hợp.

Vật liệu sắt từ nói chung không có một độ từ thẩm hằng số áp dụng cho mọi trường. Bão hòa và từ trễ làm quan hệ giữa trường ngoài và từ hóa phụ thuộc trạng thái vật liệu.`+ref,
  'do-cam-tu': String.raw`Độ cảm từ là đại lượng không thứ nguyên $\chi_m=K_m-1$. Giá trị dương đặc trưng cho thuận từ, còn giá trị âm đặc trưng cho nghịch từ. Quan hệ này đi cùng mô tả tuyến tính và không loại bỏ các hiệu ứng bão hòa, từ trễ của sắt từ.`+ref,
  'thuan-tu': String.raw`Mômen từ vi mô của chất thuận từ có thể định hướng một phần theo trường ngoài. Sự định hướng nhiệt bị nhiễu bởi chuyển động nhiệt, nên đáp ứng thường yếu. Trong miền Curie, $M=CB/T$.`+ref,
  'nghich-tu': String.raw`Trường ngoài làm thay đổi chuyển động electron, tạo mômen cảm ứng ngược chiều trường. Bởi vậy $\chi_m<0$ và vật liệu bị đẩy yếu khỏi vùng trường mạnh. Với nhiều chất rắn, lỏng, độ cảm từ nghịch từ gần như không phụ thuộc nhiệt độ.`+ref,
  'sat-tu': String.raw`Tương tác giữa mômen nguyên tử tạo các miền từ có định hướng tự phát. Khi chưa từ hóa, các miền khác hướng có thể làm tổng mômen mẫu nhỏ. Trường ngoài làm miền thuận hướng lớn lên, tạo đáp ứng mạnh.

Khi các mômen gần như đã thẳng hàng, vật liệu bão hòa. Quan hệ trường và từ hóa khi ấy không còn tuyến tính với một hệ số cố định. Nhiều vật liệu sắt từ còn có từ trễ.`+ref,
  'bao-hoa-tu': String.raw`Khi gần như mọi mômen vi mô đã định hướng theo trường, độ từ hóa tiến gần giá trị cực đại. Trên đường cong $M$ theo trường ngoài, độ dốc giảm mạnh ở vùng bão hòa. Mô hình tuyến tính với $M$ tỉ lệ trường không còn phù hợp ở vùng này.`+ref,
  'tu-tre': String.raw`Đường từ trễ ghi lại trạng thái từ hóa khi trường ngoài tăng rồi giảm qua một chu kỳ. Sau khi trường trở về không, mẫu có thể giữ từ hóa dư. Trường ngược cần để đưa từ hóa về không xác định trường kháng từ.

Diện tích vòng trễ biểu thị năng lượng tiêu tán trên một đơn vị thể tích trong một chu kỳ từ hóa. Vật liệu từ mềm có vòng hẹp để giảm tổn hao trong lõi chịu trường đổi chiều.`+ref,
  'tu-hoa-du': String.raw`Từ hóa dư là giá trị từ hóa tại trường ngoài bằng không trên nhánh giảm của vòng trễ. Nó cho biết vật liệu còn giữ trạng thái từ sau khi bỏ trường kích thích. Nam châm vĩnh cửu cần từ hóa dư đáng kể.`+ref,
  'luc-khu-tu': String.raw`Trường kháng từ là độ lớn trường ngược tại đó từ hóa trở về không sau một trạng thái đã từ hóa. Trường kháng từ lớn giúp nam châm chống lại các trường ngược và nhiễu làm mất từ.`+ref,
  'hien-tuong-curie': String.raw`Định luật Curie mô tả nhiều chất thuận từ trong miền đáp ứng thích hợp:

$$
M=\frac{CB}{T}.
$$

$C$ phụ thuộc vật liệu, còn $T$ là nhiệt độ tuyệt đối. Định luật này không phải mô hình tổng quát cho vật liệu sắt từ hoặc mọi cường độ trường.`+ref,
  'ong-day-dien': String.raw`Ống dây đủ dài có $n$ vòng trên một đơn vị chiều dài. Gần trung điểm, trường bên trong xấp xỉ đều:

$$
B\approx\mu_0 nI.
$$

Kết quả giả thiết ống dây dài hơn nhiều đường kính và bỏ qua hiệu ứng đầu. Trường ngoài gần trung điểm nhỏ.`+ref,
  'ong-day-hinh-xuyen': String.raw`Với xuyến lý tưởng có $N$ vòng, dòng $I$ và đường tròn Ampere bán kính $r$ trong lõi, định luật Ampere cho:

$$
B(r)=\frac{\mu_0NI}{2\pi r}.
$$

Trường phụ thuộc $r$, nên không đều trên tiết diện lõi. Trong mô hình lý tưởng, trường bằng không trong lỗ và phía ngoài, nhưng xuyến thực có thể rò trường.`+ref,
}

export const sourcesWikiConnections = {
  'momen-dong-luong': ['momen-luc','momen-quan-tinh','dong-luong-vat-ly','momen-tu','tich-co-huong'],
  'dinh-luat-biot-savart': ['dinh-luat-ampere', 'dong-dien'],
  'dinh-luat-ampere': ['dinh-luat-biot-savart', 'dong-dien', 'tu-truong'],
  'do-tu-hoa': ['do-tu-tham', 'do-cam-tu', 'sat-tu'],
  'do-tu-tham': ['do-tu-hoa', 'do-cam-tu', 'sat-tu'],
  'do-cam-tu': ['do-tu-tham', 'thuan-tu', 'nghich-tu'],
  'thuan-tu': ['do-cam-tu', 'hien-tuong-curie'],
  'nghich-tu': ['do-cam-tu'],
  'sat-tu': ['bao-hoa-tu', 'tu-tre', 'tu-hoa-du', 'luc-khu-tu'],
  'bao-hoa-tu': ['sat-tu', 'tu-tre'],
  'tu-tre': ['sat-tu', 'tu-hoa-du', 'luc-khu-tu'],
  'tu-hoa-du': ['tu-tre', 'luc-khu-tu', 'sat-tu'],
  'luc-khu-tu': ['tu-tre', 'tu-hoa-du', 'sat-tu'],
  'hien-tuong-curie': ['thuan-tu', 'do-cam-tu'],
  'ong-day-dien': ['dinh-luat-ampere', 'do-tu-tham'],
  'ong-day-hinh-xuyen': ['dinh-luat-ampere', 'do-tu-tham', 'ong-day-dien'],
}
