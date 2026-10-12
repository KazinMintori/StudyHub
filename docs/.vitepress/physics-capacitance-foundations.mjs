const reference='\n\nTài liệu tham khảo: Young & Freedman, *University Physics with Modern Physics*, ấn bản 15, chương 24, trang 781–802.'
export const capacitanceConcepts={
 'dien-dung':{
  name:'Điện dung',aliases:['điện dung','tụ điện'],
  definition:'Điện dung C của hai vật dẫn mang điện tích ±Q là tỉ số $C=Q/V_{ab}$, với $V_{ab}$ là điện thế vật dương trừ điện thế vật âm. Đơn vị SI là farad. Trong mô hình tuyến tính, C phụ thuộc hình học và điện môi, không phụ thuộc điện tích đã nạp.',
  example:'Tụ 100 nF ở điện áp 12 V có độ lớn điện tích mỗi bản 1,20 µC và năng lượng 7,20 µJ. Tổng đại số điện tích hai bản bằng không.',
  use:'Tính điện tích, điện áp, năng lượng và điện dung tương đương của các cấu hình vật dẫn.',
  question:'Hai tụ mắc nối tiếp có luôn cùng độ lớn điện tích không?',
  answer:'Quy tắc ấy cần các nút trung gian trung hòa và cô lập. Nếu nút đã có điện tích dư, phải dùng bảo toàn điện tích của từng nút.'
 },
 'dien-moi':{
  name:'Điện môi',aliases:['điện môi','hằng số điện môi'],
  definition:'Điện môi là vật liệu cách điện có thể bị phân cực trong điện trường. Khi một điện môi tuyến tính, đồng nhất lấp đầy khoảng giữa hai vật dẫn của tụ mà không đổi hình học, điện dung tăng K lần. $K=C/C_0$ là hằng số điện môi, không có đơn vị.',
  example:'Tụ 100 nF được nạp đến 12 V rồi ngắt nguồn. Điện môi K = 3 lấp đầy khe làm điện dung thành 300 nF và điện áp còn 4 V, trong khi điện tích tự do giữ nguyên.',
  use:'Phân tích điện trường, điện tích cảm ứng và năng lượng của tụ có chất cách điện.',
  question:'Đưa điện môi vào có luôn làm điện trường trong tụ giảm K lần không?',
  answer:'Cần giữ điện tích tự do và hình học. Nếu nguồn vẫn giữ điện áp, trường gần đều V/d giữ nguyên và nguồn cung cấp thêm điện tích.'
 },
 'do-dien-tham':{
  name:'Độ điện thẩm',aliases:['độ điện thẩm','điện thẩm'],
  definition:'Trong mô hình điện môi tuyến tính, đồng nhất và đẳng hướng, độ điện thẩm $\\varepsilon=K\\varepsilon_0$ diễn tả đáp ứng điện của môi trường. Đơn vị SI là F/m. K không có đơn vị, còn $\\varepsilon_0$ là độ điện thẩm chân không.',
  example:'Vật liệu có K = 3 có độ điện thẩm khoảng 26,6 pF/m. Cùng hình học tụ, điện dung gấp ba giá trị chân không.',
  use:'Viết điện dung, mật độ năng lượng và định luật Gauss theo môi trường đang xét.',
  question:'Có thể đưa ε ra ngoài tích phân mặt Gauss khi vật liệu thay đổi theo vị trí không?',
  answer:'Chỉ đưa ra ngoài khi ε không đổi trên toàn phần mặt đang tích phân. Nếu không, phải dùng giá trị tại từng điểm.'
 },
 'do-ben-dien-moi':{
  name:'Độ bền điện môi',aliases:['độ bền điện môi','đánh thủng điện môi'],
  definition:'Độ bền điện môi là cường độ điện trường lớn nhất mà vật liệu chịu được trước khi xảy ra đánh thủng. Khi đánh thủng, vật liệu cách điện trở thành đường dẫn điện. Độ bền có đơn vị V/m và khác hằng số điện môi K.',
  example:'Điện môi dày 1,0 mm có ngưỡng trường 20 MV/m tương ứng điện áp lý tưởng 20 kV trong mô hình trường đều.',
  use:'Giới hạn điện áp và năng lượng tích trữ, chọn vật liệu và chiều dày cách điện.',
  question:'Vật liệu có K lớn hơn có chắc chịu điện áp cao hơn không?',
  answer:'Không. K mô tả sự phân cực, còn độ bền liên quan tới ngưỡng mất cách điện. Cần biết cả độ bền, chiều dày và sự phân bố trường.'
 },
 'mat-do-nang-luong-dien-truong':{
  name:'Mật độ năng lượng điện trường',aliases:['mật độ năng lượng điện trường'],
  definition:'Mật độ năng lượng điện trường là năng lượng trên một đơn vị thể tích. Trong chân không, $u=\\varepsilon_0E^2/2$. Trong điện môi tuyến tính đẳng hướng, $u=\\varepsilon E^2/2$ với E là trường thực trong vật liệu. Đơn vị là $\\mathrm{J/m^3}$.',
  example:'Điện trường 100 kV/m trong chân không có mật độ năng lượng khoảng $0.0443\\,\\mathrm{J/m^3}$. Đây là mật độ, chưa phải tổng năng lượng của cả vùng trường.',
  use:'Tính năng lượng của trường đều hoặc không đều bằng tích phân theo thể tích.',
  question:'Có cộng năng lượng điện trường với $Q^2/(2C)$ để có năng lượng toàn tụ không?',
  answer:'Không. Tích phân mật độ trường và $Q^2/(2C)$ là hai cách tính cùng một năng lượng của tụ lý tưởng.'
 }
}
export const capacitanceWikiDetails={
 'dien-dung':String.raw`Muốn tìm điện dung từ hình học, giả sử hai vật dẫn mang điện tích +Q và −Q. Tìm điện trường trong khe, tính hiệu điện thế giữa hai vật rồi lấy tỉ số Q/V_ab. Đại lượng Q là điện tích một bản, không phải tổng điện tích cả tụ.

Với hai bản phẳng cách nhau d, diện tích A và điện môi đồng nhất có độ điện thẩm ε:

$$
C=\frac{\varepsilon A}{d}.
$$

Công thức cần bỏ được hiệu ứng mép. Với hai mặt cầu đồng tâm bán kính a < b trong chân không:

$$
C=4\pi\varepsilon_0\frac{ab}{b-a}.
$$

Mạng song song có các tụ nối cùng hai nút nên cùng điện áp. Ba tụ cho C_p = C₁ + C₂ + C₃. Với n tụ, tổng ấy viết là:

$$
C_p=\sum_{i=1}^{n}C_i.
$$

Chỉ số i chạy qua từng tụ. Chuỗi nối tiếp có các nút giữa ban đầu trung hòa và cô lập giữ cùng độ lớn điện tích trên các tụ. Ba tụ cho:

$$
\frac1{C_s}=\frac1{C_1}+\frac1{C_2}+\frac1{C_3}.
$$

Tổng quát, 1/C_s bằng tổng các nghịch đảo 1/Cᵢ, từ i = 1 đến i = n. Năng lượng của một tụ tuyến tính là:

$$
\begin{aligned}
U&=\frac{Q^2}{2C},\\
&=\frac12 CV^2,\\
&=\frac12 QV.
\end{aligned}
$$

Khi hình học hoặc vật liệu thay đổi, phải xác định tụ cô lập hay còn nối nguồn. Tụ cô lập giữ điện tích tự do, còn nguồn lý tưởng giữ điện áp và trao đổi điện tích với các bản.`+reference,
 'dien-moi':String.raw`Ở mức phân tử, điện trường làm dịch chuyển tương đối các điện tích liên kết hoặc định hướng các lưỡng cực thường trực. Hai mặt điện môi xuất hiện điện tích liên kết trái dấu. Trong tụ cô lập, trường do chúng tạo ra ngược trường của các bản và làm trường tổng yếu đi.

Với điện môi tuyến tính lấp đầy khe và điện tích tự do giữ nguyên:

$$
\begin{aligned}
C&=KC_0,\\
E&=E_0/K,\\
V&=V_0/K,\\
Q_i&=Q(1-1/K).
\end{aligned}
$$

Qᵢ là độ lớn điện tích liên kết trên mỗi mặt trong mô hình tụ phẳng bỏ hiệu ứng mép. Hai mặt có dấu trái nhau nên tổng điện tích liên kết của toàn tấm vẫn bằng không.

Nếu vẫn nối nguồn giữ V, điện dung tăng K lần và điện tích tự do trên mỗi bản tăng K lần. Trường E = V/d giữ nguyên. Vì vậy phải xác định điều kiện nối nguồn trước khi dùng các tỉ số điện trường hoặc năng lượng.

K phụ thuộc vật liệu và điều kiện khảo sát. Mô hình hệ số vô hướng không đổi cần vật liệu tuyến tính, đẳng hướng và điện trường còn trong miền cách điện. Điện môi chỉ lấp một phần khe thường phải chia cấu hình thành các miền mắc nối tiếp hoặc song song.`+reference,
 'do-dien-tham':String.raw`Trong chân không, ε = ε₀. Với điện môi tuyến tính và đẳng hướng:

$$
\varepsilon=K\varepsilon_0.
$$

Điện dung tụ phẳng lấp đầy một điện môi đồng nhất là:

$$
C=\frac{\varepsilon A}{d}.
$$

Độ điện thẩm còn xuất hiện trong quan hệ Gauss viết theo điện tích tự do:

$$
\oint_S\varepsilon\vec E\cdot d\vec A
=Q_{\mathrm{free}}.
$$

Điện trường trong tích phân là trường thực gồm tác dụng của cả điện tích tự do và điện tích liên kết. Vế phải chỉ đếm điện tích tự do. Nếu ε thay đổi theo vị trí, giữ nó bên trong tích phân.

Không thay ε₀ bằng ε trong mọi bài toán mà bỏ qua hình học các mặt phân cách. Phép thay đơn giản cho các công thức tụ cầu, tụ trụ cần điện môi đồng nhất lấp toàn vùng giữa các vật dẫn.`+reference,
 'do-ben-dien-moi':String.raw`Điện môi giữ cách điện khi trường chưa đủ mạnh để tạo dòng dẫn gây đánh thủng. Trong mô hình tụ phẳng với trường đều, điện áp giới hạn ước tính từ:

$$
\begin{aligned}
V_{\max}&=E_{\mathrm{bd}}d,\\
Q_{\max}&=CV_{\max},\\
U_{\max}&=\frac12 CV_{\max}^2.
\end{aligned}
$$

E_bd ký hiệu ngưỡng đánh thủng. Nếu chọn làm việc ở một phần f của ngưỡng, với 0 < f < 1, thay trường bằng fE_bd. Khi hình học không đổi, điện áp và điện tích giảm f lần, năng lượng giảm f² lần so với giá trị ở ngưỡng.

Độ bền và K là hai dữ kiện độc lập. Khi so vật liệu cho cùng hình học, điện áp giới hạn phụ thuộc độ bền. Điện tích và năng lượng còn phụ thuộc điện dung, nên vật liệu tốt nhất cho ba mục tiêu có thể khác nhau.

Điện trường có thể tập trung ở mép, khuyết tật hoặc vùng cách điện mỏng. Khi ấy không dùng điện áp trung bình chia chiều dày trung bình để bảo đảm mọi điểm đều dưới ngưỡng.`+reference,
 'mat-do-nang-luong-dien-truong':String.raw`Đối với tụ phẳng chân không, điện trường gần đều trong thể tích Ad. Từ điện dung và điện áp:

$$
\begin{aligned}
U&=\frac12 CV^2,\\
C&=\frac{\varepsilon_0 A}{d},\\
V&=Ed,\\
U&=\frac12\varepsilon_0 E^2Ad.
\end{aligned}
$$

Chia cho thể tích cho u = ε₀E²/2. Với trường không đều, chia vùng thành các thể tích nhỏ rồi cộng năng lượng của chúng:

$$
U=\int_{\mathcal V}u\,d\mathcal V.
$$

Trong điện môi tuyến tính đẳng hướng, dùng u = εE²/2. Cùng một Q trên tụ phẳng cô lập, tăng ε làm trường yếu đi và năng lượng giảm. Cùng một V do nguồn giữ cố định, trường giữ nguyên nhưng mật độ năng lượng và tổng năng lượng tăng theo ε.

Năng lượng trường là cách diễn tả thế năng điện đã dùng cho hệ điện tích. Không cộng nó thêm một lần nữa vào thế năng hoặc năng lượng tụ.`+reference
}
export const capacitanceWikiConnections={
 'dien-dung':['dien-the','dien-truong','dien-moi','mat-do-nang-luong-dien-truong','cong-nang-luong'],
 'dien-moi':['phan-cuc-dien','do-dien-tham','dien-dung','do-ben-dien-moi'],
 'do-dien-tham':['dien-moi','dien-truong','dinh-luat-gauss','dien-dung'],
 'do-ben-dien-moi':['dien-moi','dien-dung','mat-do-nang-luong-dien-truong'],
 'mat-do-nang-luong-dien-truong':['dien-truong','dien-dung','do-dien-tham','cong-nang-luong']
}
