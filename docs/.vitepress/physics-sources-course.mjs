const note = '08-nguon-tu-truong'
const display = (s) => `$$\n${s}\n$$`

export const sourcesTopics = [
  { title: 'Từ trường do dòng điện tạo ra', topics: [
    { slug: 'dien-tich-chuyen-dong-tu-truong', title: 'Từ trường do điện tích chuyển động', question: 'Một điện tích chuyển động tạo từ trường phụ thuộc vận tốc và vị trí ra sao?', source: '28.1' },
    { slug: 'tu-truong-biot-savart', title: 'Định luật Biot–Savart', question: 'Mỗi phần tử dòng điện đóng góp vào từ trường tại điểm khảo sát như thế nào?', source: '28.2' },
    { slug: 'tu-truong-day-thang', title: 'Từ trường của dây dẫn thẳng', question: 'Đối xứng trụ cho biết độ lớn và chiều trường quanh dây ra sao?', source: '28.3' },
    { slug: 'luc-tu-hai-day', title: 'Lực giữa hai dây dẫn song song', question: 'Vì sao hai dòng cùng chiều hút nhau còn hai dòng ngược chiều đẩy nhau?', source: '28.4' },
    { slug: 'tu-truong-vong-day', title: 'Từ trường trên trục vòng dây', question: 'Các phần tử đối xứng của vòng dây tổng hợp trường trên trục thế nào?', source: '28.5' },
    { slug: 'dinh-luat-ampere', title: 'Định luật Ampere', question: 'Tích phân đường kín liên hệ với dòng điện bao quanh như thế nào?', source: '28.6' },
    { slug: 'ung-dung-ampere', title: 'Ứng dụng định luật Ampere', question: 'Đối xứng nào cho phép tìm trường trong dây trụ, ống dây và xuyến?', source: '28.7' },
    { slug: 'vat-lieu-tu', title: 'Vật liệu từ', question: 'Từ hóa, độ cảm từ và từ trễ mô tả phản ứng của vật liệu ra sao?', source: '28.8' },
  ] },
]

export const sourcesSlides = [
  { note, title: 'Điện tích chuyển động tạo từ trường', bullets: ['Từ trường tại điểm khảo sát phụ thuộc vị trí tương đối đến điện tích.', 'Biểu thức dùng điện tích chuyển động đều với tốc độ nhỏ so với tốc độ ánh sáng.', 'Chiều vuông góc với vận tốc và phương nối đến điểm.'], formula: display(String.raw`\vec B=\frac{\mu_0}{4\pi}\frac{q\vec v\times\hat r}{r^2}`) },
  { note, title: 'Biot–Savart cộng trường của các phần tử dòng', bullets: ['Mỗi phần tử dòng đóng góp một vector từ trường tại điểm khảo sát.', 'Độ lớn giảm theo bình phương khoảng cách và phụ thuộc góc giữa phần tử dòng với phương nối đến điểm.', 'Chiều xác định bằng tích có hướng theo quy tắc bàn tay phải.'], formula: display(String.raw`d\vec B=\frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}`) },
  { note, title: 'Dây thẳng dài có trường giảm theo khoảng cách', bullets: ['Đối xứng trụ làm đường sức là các đường tròn đồng tâm.', 'Chiều trường xác định bởi chiều dòng điện.', 'Kết quả áp dụng cho dây thẳng đủ dài so với khoảng cách đang xét.'], formula: display(String.raw`B=\frac{\mu_0 I}{2\pi r}`) },
  { note, title: 'Hai dây song song hút hoặc đẩy tùy chiều dòng', bullets: ['Mỗi dây nằm trong trường do dây kia tạo ra.', 'Dòng cùng chiều gây lực hút, dòng ngược chiều gây lực đẩy.', 'Lực trên một đơn vị chiều dài tỉ lệ tích hai dòng và nghịch với khoảng cách.'], formula: display(String.raw`\frac{F}{L}=\frac{\mu_0 I_1 I_2}{2\pi d}`) },
  { note, title: 'Trường trên trục vòng dây có hai thành phần đối xứng', bullets: ['Các thành phần ngang triệt tiêu từng cặp.', 'Các thành phần dọc trục cùng chiều và cộng lại.', 'Tại tâm một vòng bán kính a, biểu thức rút gọn tương ứng.'], formula: display(String.raw`B_x=\frac{\mu_0 I a^2}{2(a^2+x^2)^{3/2}}`) },
  { note, title: 'Đoạn dây hữu hạn cho trường theo hai góc đầu mút', bullets: ['Biot–Savart tích phân dọc đoạn dây thẳng hữu hạn.', 'Các góc được đo từ phương vuông góc với dây qua điểm quan sát.', 'Giới hạn dây rất dài khôi phục biểu thức dây thẳng vô hạn.'], formula: display(String.raw`B=\frac{\mu_0 I}{4\pi a}(\sin\theta_1+\sin\theta_2)`) },
  { note, title: 'Định luật Ampere tính tích phân theo dòng bao', bullets: ['Dòng xuyên qua mặt được giới hạn bởi đường kín được cộng đại số.', 'Chiều dương gắn với chiều đi trên đường bằng quy tắc bàn tay phải.', 'Định luật dạng này dùng cho từ tĩnh, không bao gồm số hạng điện trường biến thiên.'], formula: display(String.raw`\oint\vec B\cdot d\vec l=\mu_0 I_{\mathrm{encl}}`) },
  { note, title: 'Dây trụ có dòng đều cho trường tuyến tính bên trong', bullets: ['Bên trong, dòng bao tỉ lệ diện tích tiết diện được bao.', 'Bên ngoài, đường tích phân bao toàn bộ dòng.', 'Độ lớn trường liên tục tại mặt trụ trong mô hình phân bố đều.'], formula: display(String.raw`\begin{aligned}&B(r) = \frac{\mu_0 I r}{2\pi R^2},\quad r<R\\&B(r) = \frac{\mu_0 I}{2\pi r},\quad r\ge R.\end{aligned}`) },
  { note, title: 'Ống dây dài và xuyến tập trung trường nhờ đối xứng', bullets: ['Ở vùng giữa ống dây dài, trường gần đều và bên ngoài nhỏ.', 'Trong lõi xuyến, trường phụ thuộc bán kính tính từ trục xuyến.', 'Các kết quả là gần đúng hình học và giả thiết môi trường không từ tính.'], formula: display(String.raw`\begin{aligned}&B_{\text{ống dây}} \approx \mu_0 nI\\&B_{\text{xuyến}}(r) = \frac{\mu_0 NI}{2\pi r}.\end{aligned}`) },
  { note, title: 'Độ từ hóa bổ sung vào trường do dòng ngoài', bullets: ['Độ từ hóa là mômen từ trên một đơn vị thể tích.', 'Trong vật liệu tuyến tính đẳng hướng, độ từ thẩm tương đối liên hệ với độ cảm từ.', 'Không dùng quan hệ tuyến tính như hằng số vật liệu sắt từ khi vật liệu bão hòa hoặc có từ trễ.'], formula: display(String.raw`\begin{aligned}&\vec B = \vec B_0+\mu_0\vec M\\&\mu = K_m\mu_0\\&\chi_m = K_m-1.\end{aligned}`) },
  { note, title: 'Vật liệu sắt từ có bão hòa và từ trễ', bullets: ['Các miền từ có thể đổi kích thước và hướng khi tăng trường ngoài.', 'Sau khi bỏ trường, từ hóa dư có thể còn lại.', 'Vòng trễ phụ thuộc lịch sử từ hóa nên không mô tả bằng một độ từ thẩm cố định.'], formula: '' },
]

export const sourcesCheatsheet = {
  summary: 'Định nghĩa, tính chất và công thức về trường do dòng điện, định luật Ampere và vật liệu từ.',
  sections: [
    { id: 'moving-charge', title: 'Điện tích chuyển động', items: [
      { name: 'Điện tích điểm chuyển động chậm', formula: display(String.raw`\vec B=\frac{\mu_0}{4\pi}\frac{q\vec v\times\hat r}{r^2}`), description: String.raw`Biểu thức không tương đối tính. $\hat r$ hướng từ điện tích đến điểm khảo sát.` },
      { name: 'Độ lớn và góc', formula: display(String.raw`B=\frac{\mu_0|q|v}{4\pi r^2}\sin\phi`), description: 'φ là góc giữa vận tốc và hướng từ điện tích đến điểm đo. Trường bằng không khi hai hướng song song hoặc ngược song song.' },
    ] },
    { id: 'biot-savart', title: 'Biot–Savart', items: [
      { name: 'Định luật Biot–Savart', formula: display(String.raw`\begin{aligned}&d\vec B = \frac{\mu_0}{4\pi}\\&\quad\cdot\frac{I\,d\vec l\times\hat r}{r^2}.\end{aligned}`), description: 'Dùng cho dòng điện ổn định. Cộng vector các phần tử trên toàn dây.' },
      { name: 'Trường của cả dây dẫn', formula: display(String.raw`\begin{aligned}&\vec B = \frac{\mu_0}{4\pi}\\&\quad\times\int\frac{I\,d\vec l\times\hat r}{r^2}.\end{aligned}`), description: 'Tích phân dọc dây dẫn. Hướng từ phần tử nguồn đến điểm trường và khoảng cách được tính riêng tại mỗi phần tử.' },
      { name: 'Đoạn dây hữu hạn', formula: display(String.raw`B=\frac{\mu_0 I}{4\pi a}(\sin\theta_1+\sin\theta_2)`), description: 'a là khoảng cách vuông góc đến dây. Với hình chiếu điểm nằm giữa hai đầu, hai góc không âm đo từ phương vuông góc. Nếu hình chiếu ở ngoài đoạn, phải dùng góc có dấu nhất quán.' },
      { name: 'Điểm trên trung trực đoạn dài 2a', formula: display(String.raw`B=\frac{\mu_0I}{2\pi}\frac{a}{x\sqrt{x^2+a^2}}`), description: 'Trong công thức này, a là nửa chiều dài đoạn dây và x là khoảng cách vuông góc từ điểm đo đến dây.' },
      { name: 'Hằng số từ chân không', formula: display(String.raw`\mu_0\approx4\pi\times10^{-7}\,\mathrm{T\,m/A}`), description: 'Giá trị gần đúng dùng trong các phép tính. Từ khi định nghĩa ampere thay đổi, độ từ thẩm chân không được xác định bằng thực nghiệm và không còn có giá trị định nghĩa chính xác như trước.' },
      { name: 'Liên hệ các hằng số điện từ', formula: display(String.raw`c=\frac1{\sqrt{\varepsilon_0\mu_0}}`), description: 'c là tốc độ ánh sáng trong chân không, ε₀ là hằng số điện và μ₀ là hằng số từ.' },
    ] },
    { id: 'wires', title: 'Dây thẳng và lực giữa hai dây', items: [
      { name: 'Dây dẫn thẳng dài', formula: display(String.raw`B=\frac{\mu_0 I}{2\pi r}`), description: 'Dây đủ dài, môi trường chân không hoặc gần đúng không khí.' },
      { name: 'Hai dây song song', formula: display(String.raw`\frac{F}{L}=\frac{\mu_0 I_1I_2}{2\pi d}`), description: 'Độ lớn lực trên đơn vị chiều dài. Dòng cùng chiều hút nhau, ngược chiều đẩy nhau.' },
    ] },
    { id: 'loops', title: 'Vòng dây', items: [
      { name: 'Vòng dây trên trục', formula: display(String.raw`B_x=\frac{\mu_0 I a^2}{2(a^2+x^2)^{3/2}}`), description: 'Vòng bán kính a mang dòng I, điểm khảo sát cách tâm x trên trục.' },
      { name: 'Tâm cuộn N vòng', formula: display(String.raw`B=\frac{\mu_0 NI}{2a}`), description: 'N vòng đồng tâm cùng bán kính a và cùng chiều dòng.' },
    ] },
    { id: 'ampere', title: 'Định luật Ampere', items: [
      { name: 'Định luật Ampere từ tĩnh', formula: display(String.raw`\oint\vec B\cdot d\vec l=\mu_0 I_{\mathrm{encl}}`), description: String.raw`$I_{\mathrm{encl}}$ là tổng đại số dòng xuyên qua mặt do đường kín bao. Dạng này không gồm dòng điện dịch.` },
    ] },
    { id: 'ampere-applications', title: 'Ứng dụng Ampere', items: [
      { name: 'Dây trụ có dòng đều', formula: display(String.raw`\begin{aligned}&B(r) = \frac{\mu_0 I r}{2\pi R^2},\quad r<R\\&B(r) = \frac{\mu_0 I}{2\pi r},\quad r\ge R.\end{aligned}`), description: 'Dây dài bán kính R, dòng I phân bố đều trên tiết diện.' },
      { name: 'Ống dây dài và xuyến', formula: display(String.raw`\begin{aligned}&B_{\text{ống dây}} \approx \mu_0 nI\\&B_{\text{xuyến}}(r) = \frac{\mu_0 NI}{2\pi r}.\end{aligned}`), description: 'Ống dây dài: vùng giữa. Xuyến lý tưởng: trường trong lõi.' },
    ] },
    { id: 'magnetic-response', title: 'Từ hóa và vật liệu tuyến tính', items: [
      { name: 'Từ hóa và trường tổng', formula: display(String.raw`\begin{aligned}&\vec M = \frac{\vec\mu_{\mathrm{total}}}{V}\\&\vec B = \vec B_0+\mu_0\vec M.\end{aligned}`), description: '$M$ là mômen từ trên đơn vị thể tích. $B_0$ do các dòng ngoài vật liệu tạo ra.' },
      { name: 'Độ từ thẩm và độ cảm từ', formula: display(String.raw`\begin{aligned}&\mu = K_m\mu_0,\\&\chi_m = K_m-1.\end{aligned}`), description: 'Quan hệ cho vật liệu tuyến tính đẳng hướng. Sắt từ có thể phi tuyến và có từ trễ.' },
      { name: 'Định luật Curie', formula: display(String.raw`M=\frac{CB}{T}`), description: 'Vật liệu thuận từ trong miền áp dụng, với T là nhiệt độ tuyệt đối.' },
    ] },
    { id: 'atomic-magnetism', title: 'Mômen từ nguyên tử', items: [
      { name: 'Mômen từ quỹ đạo electron', formula: display(String.raw`\mu=\frac{eL}{2m}`), description: 'Liên hệ độ lớn mômen từ quỹ đạo với mômen động lượng. Hai vector ngược hướng với electron.' },
      { name: 'Magneton Bohr', formula: display(String.raw`\mu_B=\frac{eh}{4\pi m_e}`), description: String.raw`Thang mômen từ nguyên tử, xấp xỉ $9{,}274\times10^{-24}\,\mathrm{A\,m^2}$.` },
      { name: 'Năng lượng nhiệt và từ', formula: display(String.raw`\begin{aligned}&U = -\vec\mu\cdot\vec B,\\&K_{\mathrm{tr}} = \frac32 kT.\end{aligned}`), description: 'K_tr là động năng tịnh tiến trung bình của phân tử khí lý tưởng.' },
    ] },
    { id: 'ferromagnetic-behavior', title: 'Bão hòa và từ trễ', items: [
      { name: 'Bão hòa từ hóa', formula: '', description: 'Khi gần như mọi mômen đã định hướng, độ từ hóa tiến gần cực đại và không còn tăng tuyến tính đáng kể.' },
      { name: 'Vòng từ trễ', formula: '', description: 'Từ hóa phụ thuộc lịch sử. Từ hóa dư còn lại khi trường ngoài bằng không. Trường ngược đưa từ hóa về không đặc trưng lực khử từ.' },
    ] },
  ],
}
