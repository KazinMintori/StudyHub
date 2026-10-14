# Sổ nguồn: Young & Freedman 15e, Chương 30 đến hết mục 30.3

## Phạm vi đã đọc

- Nguồn: `raw_materials/physics/source/young-freedman-15.pdf`.
- Bản văn QA: `qa/physics/full-source/pdf-1008.txt` đến `pdf-1017.txt`, đủ 10 trang PDF liên tiếp.
- Đối chiếu ảnh trang PDF: Trang PDF 1008–1017 tương ứng trang in 988–997. Đã xem ảnh trang liên tục ở dạng contact sheet và phóng lớn các trang có công thức, hình, ví dụ và tự kiểm.
- Ranh giới: Đọc lời mở Chương 30, mục 30.1 Mutual Inductance (trang in 988–991), 30.2 Self-Inductance and Inductors (trang 992–994, ví dụ và tự kiểm đến trang 995), và 30.3 Magnetic-Field Energy (trang 995–997). Trang in 998, nơi bắt đầu mục 30.4, không thuộc phạm vi rà soát.

## Lời mở chương và câu hỏi khởi động

- Vai trò: Đặt bối cảnh cho cảm ứng điện từ qua cuộn dây trong xe dùng động cơ xăng, đèn huỳnh quang và vòng dây dưới mặt đường điều khiển đèn giao thông. Mạch ý chính gồm cảm ứng hỗ cảm giữa hai cuộn, tự cảm trong một cuộn và năng lượng nằm trong từ trường.
- Mục tiêu chương nêu rõ: Dòng biến thiên ở cuộn này gây suất điện động ở cuộn kia; suất điện động tự cảm liên hệ với tốc độ đổi dòng; năng lượng từ trường; mạch có điện trở và cuộn cảm; dao động LC; dao động tắt dần RLC. Ba mục đầu là trọng tâm của phạm vi này.
- Kiến thức được yêu cầu ôn lại: Dao động điều hòa và tắt dần; điện dung và năng lượng điện trường; định luật Kirchhoff và mạch RC; lực giữa các dây dẫn, từ trường ống dây và độ từ thẩm; định luật Faraday, định luật Lenz, điện trường bảo toàn và không bảo toàn.
- Câu hỏi hình đèn giao thông hỏi vì sao xe làm thay đổi trạng thái phát hiện của vòng dây dưới đường. Lựa chọn đúng là xe chứa vật liệu sắt từ, không đòi hỏi vật liệu ấy đã được từ hóa sẵn. Phần 30.2 giải thích thép trong xe làm tăng độ tự cảm của cuộn dò.
- Hướng chuyển hóa sư phạm: Dùng câu hỏi đèn giao thông để dẫn đến biến thiên từ thông và thay đổi độ tự cảm. Bài học không nên làm người học hiểu nhầm rằng cảm biến nhận biết điện tích hay từ hóa dư của xe.

## Mục 30.1: Mutual Inductance, trang in 988–991

### Mạch kiến thức và điều kiện

- Hai mạch ở gần nhau. Dòng $i_1$ trong cuộn 1 tạo từ trường và từ thông qua mỗi vòng của cuộn 2. Nếu từ thông khác nhau giữa các vòng, $\Phi_{B2}$ được hiểu là giá trị trung bình trên một vòng.
- Định luật Faraday cho cuộn 2: $\mathcal E_2=-N_2\,d\Phi_{B2}/dt$ (30.1). Từ trường và từ thông tỉ lệ với dòng trong miền tuyến tính.
- Định nghĩa hệ số hỗ cảm: $N_2\Phi_{B2}=M_{21}i_1$ (30.2), từ đó $\mathcal E_2=-M_{21}\,di_1/dt$ (30.3). Chỉ rõ $\Phi_{B2}$ là từ thông qua một vòng, còn $N_2\Phi_{B2}$ là từ thông móc vòng.
- Đổi vai trò hai cuộn cho $M_{12}=M_{21}$. Ký hiệu chung là $M$, với hai suất điện động hỗ cảm $\mathcal E_2=-M\,di_1/dt$ và $\mathcal E_1=-M\,di_2/dt$ (30.4). Dấu âm thể hiện định luật Lenz.
- Định nghĩa đối xứng: $M=N_2\Phi_{B2}/i_1=N_1\Phi_{B1}/i_2$ (30.5). Không suy ra hai từ thông bằng nhau: số vòng và cấu hình hai cuộn có thể khác nhau.
- Trong chân không, hoặc vật liệu có độ từ thẩm tương đối không đổi, $M$ là hằng số do hình học quyết định: kích thước, hình dạng, số vòng, hướng và khoảng cách. Với vật liệu từ có quan hệ phi tuyến, từ thông không còn tỉ lệ tuyến tính với dòng, nên hỗ cảm có thể phụ thuộc dòng. Giả thiết tuyến tính phải được nói rõ khi dùng công thức với $M$ không đổi.
- Đơn vị henry: $1\,\mathrm H=1\,\mathrm{Wb/A}=1\,\mathrm{V\,s/A}=1\,\Omega\,\mathrm s=1\,\mathrm{J/A^2}$. Cỡ thường gặp được nêu là millihenry và microhenry.
- Điểm ranh giới: Dòng không đổi, dù lớn, không gây suất điện động hỗ cảm. Suất điện động phụ thuộc $di/dt$, không phụ thuộc riêng giá trị tức thời của dòng.
- Ứng dụng và hệ quả thiết kế: Hỗ cảm gây nhiễu giữa mạch lân cận, có thể giảm bằng cách làm $M$ nhỏ, chẳng hạn tăng khoảng cách cuộn. Máy biến áp khai thác hỗ cảm để tạo điện áp xoay chiều ở cuộn thứ cấp, biên độ phụ thuộc độ ghép hình học và tốc độ biến thiên dòng.

### Ví dụ, tự kiểm và lời hướng dẫn trong nguồn

- Ví dụ 30.1, cuộn solenoid dài: Solenoid 1 có chiều dài $l$, diện tích tiết diện $A$, $N_1$ vòng. Cuộn 2 ôm quanh vùng giữa. Giả thiết solenoid dài để trường ngoài gần bằng không, trường trong đều trên tiết diện và dùng $B_1=\mu_0N_1i_1/l$. Từ thông qua mỗi vòng ngoài là $B_1A$, nên $M=\mu_0AN_1N_2/l$.
- Bộ số Ví dụ 30.1: $l=0.50\,\mathrm m$, $A=10\,\mathrm{cm^2}=1.0\times10^{-3}\,\mathrm{m^2}$, $N_1=1000$, $N_2=10$. Kết quả trang in là $25\times10^{-6}\,\mathrm H=25\,\mu\mathrm H$.
- Ví dụ 30.2, dòng cuộn ngoài tăng đều $i_2=(2.0\times10^6\,\mathrm{A/s})t$. Với $t=3.0\,\mu\mathrm s$, $i_2=6.0\,\mathrm A$. Dùng $M=25\,\mu\mathrm H$ và $N_1=1000$, từ thông trung bình trên mỗi vòng solenoid là $1.5\times10^{-7}\,\mathrm{Wb}$. Suất điện động trong solenoid là $\mathcal E_1=-50\,\mathrm V$. Nguồn lưu ý đây là từ thông trung bình, có thể khác nhau từ giữa đến hai đầu solenoid.
- Tự kiểm 30.1: Tăng gấp đôi đồng thời $N_1$ và $l$ trong solenoid, còn các đại lượng khác giữ nguyên. Đáp án (iii), $M$ không đổi vì tỉ số $N_1/l$ không đổi.

### Hình và nhãn cần Việt hóa nếu dùng lại ý tưởng

- Hình 30.1: Hai cuộn gần nhau, các đường sức do $i_1$ tạo ra xuyên qua cuộn 2; nhãn $N_1$, $N_2$, $\Phi_{B2}$, $\vec B$, $i_1$.
- Hình 30.2: Bàn chải đánh răng sạc không tiếp xúc điện; dịch nhãn cuộn nối với pin và đế có cuộn sạc nối ổ điện.
- Hình 30.3: Solenoid dài và cuộn ngoài, có nhãn diện tích tiết diện $A$, số vòng $N_1$, $N_2$, chiều dài $l$.
- Hình phương trình 30.4–30.5: Chú giải suất điện động, tốc độ biến thiên dòng, số vòng và từ thông qua mỗi vòng. Có thể thay bằng sơ đồ mới; giữ đúng hai vế hỗ cảm và tính đối xứng của $M$.

## Mục 30.2: Self-Inductance and Inductors, trang in 992–995

### Mạch kiến thức và điều kiện

- Tự cảm xảy ra trong một mạch đơn: Dòng tạo từ trường, từ trường móc vòng với chính mạch, và biến thiên dòng tạo suất điện động tự cảm. Theo Lenz, suất điện động chống lại sự biến thiên dòng đã gây ra nó.
- Định nghĩa độ tự cảm: $L=N\Phi_B/i$ (30.6), trong đó $\Phi_B$ là từ thông trung bình qua mỗi vòng và $N$ là số vòng. Đơn vị là henry như hỗ cảm.
- Lấy đạo hàm khi $L$ không đổi và dùng Faraday: $\mathcal E=-L\,di/dt$ (30.7). Có thể đo $L$ bằng cách đổi dòng ở tốc độ đã biết, đo suất điện động tự cảm rồi lấy tỉ số độ lớn.
- Cuộn cảm là linh kiện có độ tự cảm được thiết kế; còn gọi là choke trong nguồn. Tác dụng vật lý cốt lõi là chống sự thay đổi dòng, không phải chống dòng nói chung.
- L phụ thuộc kích thước, hình dạng, số vòng và vật liệu từ. Với $N$ vòng khít, $L$ tỉ lệ $N^2$ trong mô hình tuyến tính. Lõi sắt mềm có thể làm $L$ lớn hơn lõi không khí nhiều, nhưng độ từ hóa gần bão hòa có thể phi tuyến. Các suy luận tiếp theo giả sử $L$ không đổi và hợp lý khi lõi sắt làm việc dưới vùng bão hòa.
- Quy ước điện áp cực cuộn cảm: Với dòng đi từ $a$ sang $b$, nguồn suy ra $V_{ab}=V_a-V_b=L\,di/dt$ (30.8). Đây là điện áp tĩnh điện giữa hai đầu cuộn cảm lý tưởng, dù điện trường cảm ứng trong cuộn không bảo toàn.
- Lập luận cho (30.8) cần điều kiện cuộn dây có điện trở không đáng kể. Bên trong dây, tổng điện trường bảo toàn và không bảo toàn bằng không. Dùng định luật Faraday cho điện trường cảm ứng, giới hạn tích phân ở cuộn cảm, rồi thay điện trường cảm ứng bằng đối của điện trường bảo toàn để thu được hiệu điện thế đầu cực.
- Bảng dấu Hình 30.6: Điện trở phụ thuộc dòng, còn cuộn cảm phụ thuộc $di/dt$. Với dòng $a\to b$, dòng không đổi cho $V_{ab}=0$, dòng tăng cho $V_{ab}>0$, dòng giảm cho $V_{ab}<0$. Suất điện động tự cảm luôn chống lại biến thiên dòng.

### Ứng dụng, ví dụ và tự kiểm

- Bảo vệ đường truyền khi sét đánh: Cuộn cảm lớn làm giảm đột biến dòng. Đèn huỳnh quang: Chấn lưu mắc nối tiếp giới hạn dòng trong plasma không ohmic và duy trì dòng khi điện áp xoay chiều đi qua không; nguồn nêu thêm đèn đường hơi thủy ngân/natri và đèn neon.
- Cảm biến giao thông: Cuộn dây có dòng đặt dưới mặt đường. Thép sắt từ của xe làm tăng độ tự cảm, mạch phát hiện biến thiên này. Cách giải thích này cũng trả lời câu hỏi mở chương.
- Ví dụ 30.3, solenoid hình xuyến: Tiết diện $A$, bán kính trung bình $r$, $N$ vòng khít; giả sử trường gần đều trên tiết diện và lõi không từ. Dùng $B=\mu_0Ni/(2\pi r)$, $\Phi_B=BA$ để suy ra $L=\mu_0N^2A/(2\pi r)$. Với $N=200$, $A=5.0\times10^{-4}\,\mathrm{m^2}$, $r=0.10\,\mathrm m$, kết quả là $40\,\mu\mathrm H$.
- Ví dụ 30.4: Với cuộn xuyến trên, dòng tăng từ 0 lên $6.0\,\mathrm A$ trong $3.0\,\mathrm{ms}$, nên $di/dt=2.0\times10^6\,\mathrm{A/s}$ và độ lớn suất điện động là $80\,\mathrm V$. Chiều suất điện động từ $b$ đến $a$, đối với chiều tăng dòng từ $a$ đến $b$.
- Tự kiểm 30.2: Bốn trường hợp dùng $V_{ab}=L\,di/dt$, yêu cầu xếp từ dương nhất đến âm nhất. Đáp án $(iv),(i),(iii),(ii)$ với các giá trị lần lượt $16\,\mathrm{mV}$, $4.0\,\mathrm{mV}$, $0$, $-6.0\,\mathrm{mV}$.

### Hình và nhãn cần Việt hóa nếu dùng lại ý tưởng

- Hình 30.4: Cuộn dây, dòng $i$, từ trường $\vec B$, từ thông qua cuộn và mũi tên chiều suất điện động tự cảm.
- Hình ứng dụng sét: Đường dây truyền tải và cuộn cảm bảo vệ trước xung dòng.
- Hình 30.5: Mạch nguồn biến thiên và cuộn cảm lý tưởng, nhãn đầu $a,b$, chiều dòng $i$.
- Hình 30.6: Bốn trạng thái điện trở/cuộn cảm với dòng không đổi, tăng, giảm, cực tính $V_{ab}$ và chiều suất điện động.
- Hình 30.7: Đèn huỳnh quang có cuộn cảm chấn lưu mắc nối tiếp.
- Hình 30.8: Cuộn xuyến bị cắt một phần, nhãn số vòng $N$, diện tích tiết diện $A$, bán kính $r$, chiều dòng.

## Mục 30.3: Magnetic-Field Energy, trang in 995–997

### Mạch kiến thức và điều kiện

- Nạp dòng vào cuộn cảm cần công. Nguồn giả thiết cuộn cảm lý tưởng có điện trở bằng không, dòng tăng từ 0 đến $I$. Công suất tức thời đi vào cuộn cảm là $P=V_{ab}i=Li\,di/dt$. Do đó $dU=Li\,di$ và tích phân cho $U=\int_0^I Li\,di=\tfrac12LI^2$ (30.9).
- Ở dòng ổn định, không có công suất đi vào cuộn cảm lý tưởng. Khi dòng giảm, năng lượng từ trường có thể trả về mạch. Ngắt mạch đột ngột làm dòng giảm nhanh, suất điện động lớn và có thể gây hồ quang ở tiếp điểm. Phân biệt với điện trở: Điện trở tiêu tán năng lượng thành nhiệt, cuộn cảm lý tưởng tích trữ rồi hoàn trả năng lượng.
- Năng lượng nằm trong từ trường. Với solenoid xuyến lý tưởng có trường gần đều trên tiết diện và trường giới hạn trong lõi, $V\approx2\pi rA$, $L=\mu_0N^2A/(2\pi r)$ và $B=\mu_0NI/(2\pi r)$. Từ $u=U/V$ suy ra mật độ năng lượng từ trường trong chân không $u=B^2/(2\mu_0)$ (30.10).
- Với môi trường có độ từ thẩm không đổi $\mu$, thay $\mu_0$ bằng $\mu$ để được $u=B^2/(2\mu)$ (30.11). Nguồn khẳng định biểu thức này đúng cho cấu hình từ trường bất kỳ trong vật liệu có độ từ thẩm không đổi; không mở rộng nguyên trạng cho vật liệu phi tuyến.
- Ví dụ MRI: Với $B=1.5\,\mathrm T$, nguồn tính $u=9.0\times10^5\,\mathrm{J/m^3}$.
- Ứng dụng đánh lửa động cơ xăng: Cuộn sơ cấp khoảng 250 vòng và cuộn thứ cấp khoảng 25 000 vòng. Khi ngắt dòng sơ cấp, trường suy giảm nhanh, sinh suất điện động hàng chục nghìn volt ở thứ cấp và đưa năng lượng tới bugi.
- Ứng dụng phun trào nhật hoa: Bài đọc mô tả CME với khối lượng vật chất cỡ $10^{12}\,\mathrm{kg}$, tốc độ từ $500\,\mathrm{km/s}$, xảy ra cách nhau từ vài giờ đến vài ngày. Nguồn quy năng lượng cho sự kiện vào vùng từ trường Mặt Trời mạnh và biến thiên.

### Hình và nhãn cần Việt hóa nếu dùng lại ý tưởng

- Hình 30.9: So sánh điện trở tiêu tán năng lượng với cuộn cảm tích trữ năng lượng.
- Hình 30.10: Bugi ô tô được đánh lửa bằng năng lượng từ trường tích trong cuộn đánh lửa.
- Ảnh ứng dụng CME: Chú thích hiện tượng phun trào nhật hoa và các dữ kiện khối lượng, tốc độ, khoảng thời gian nêu trong nguồn.
- Hình phương trình 30.10–30.11: Chú giải mật độ năng lượng, độ lớn từ trường, hằng số từ và độ từ thẩm môi trường.

## Danh sách phương trình cần giữ đúng

| Số | Ý nghĩa | Dạng chuẩn đã đối chiếu ảnh |
| --- | --- | --- |
| (30.1) | Faraday ở cuộn 2 | $\mathcal E_2=-N_2\,d\Phi_{B2}/dt$ |
| (30.2) | Định nghĩa hỗ cảm có chỉ số | $N_2\Phi_{B2}=M_{21}i_1$ |
| (30.3) | Suất điện động do hỗ cảm | $\mathcal E_2=-M_{21}\,di_1/dt$ |
| (30.4) | Suất điện động ở hai cuộn | $\mathcal E_2=-M\,di_1/dt$, $\mathcal E_1=-M\,di_2/dt$ |
| (30.5) | Tính đối xứng của hỗ cảm | $M=N_2\Phi_{B2}/i_1=N_1\Phi_{B1}/i_2$ |
| (30.6) | Định nghĩa tự cảm | $L=N\Phi_B/i$ |
| (30.7) | Suất điện động tự cảm | $\mathcal E=-L\,di/dt$ |
| (30.8) | Điện áp hai đầu cuộn cảm với dòng $a\to b$ | $V_{ab}=V_a-V_b=L\,di/dt$ |
| (30.9) | Năng lượng cuộn cảm lý tưởng | $U=\int_0^I Li\,di=\tfrac12LI^2$ |
| (30.10) | Mật độ năng lượng từ trường chân không | $u=B^2/(2\mu_0)$ |
| (30.11) | Mật độ năng lượng trong vật liệu tuyến tính | $u=B^2/(2\mu)$ |

## Điểm OCR phải sửa bằng ảnh trang

- Bản QA làm mất vị trí tử/mẫu trong một số công thức. Ảnh trang xác nhận các dạng (30.5), (30.10), (30.11) như bảng trên.
- Ký hiệu micro ($\mu$) thường bị nhận thành chữ `m`. Ví dụ 30.1 cho $25\,\mu\mathrm H$, Ví dụ 30.3 cho $40\,\mu\mathrm H$, Ví dụ 30.4 dùng $40\,\mu\mathrm H$; Tự kiểm 30.2 ghi các cuộn cảm $2.0$, $4.0$, $1.0$, $1.0\,\mu\mathrm H$. Không chuyển các số này thành millihenry.
- Ở ví dụ hỗ cảm, ảnh trang xác nhận $i_2=(2.0\times10^6\,\mathrm{A/s})t$, $t=3.0\,\mu\mathrm s$, $i_2=6.0\,\mathrm A$, $\Phi_{B1}=1.5\times10^{-7}\,\mathrm{Wb}$ và $\mathcal E_1=-50\,\mathrm V$.
- Công thức mật độ năng lượng bị OCR tuyến tính hóa thành tích sai dạng. Ảnh trang cho thấy mẫu số là $2\mu_0$ hoặc $2\mu$, tương ứng $u=B^2/(2\mu_0)$ và $u=B^2/(2\mu)$.
- Chỉ tiêu nhãn trong trang mở chương phân biệt vật liệu sắt từ với vật liệu sắt từ đã từ hóa. Lời giải thích ở mục 30.2 chỉ cần tính sắt từ của xe làm thay đổi độ tự cảm.

## Những đơn vị nguồn có thể bị bỏ nếu bài rút gọn

- Tên riêng Henry và các quy đổi đơn vị có thể rút về định nghĩa SI nếu nội dung cần gọn, nhưng cần giữ tính tương đương đơn vị henry.
- Chi tiết lịch sử “một trong những người phát hiện cảm ứng điện từ” không cần dùng nếu không có mục tiêu lịch sử.
- Ví dụ số học có thể thay bằng ví dụ mới sau khi tự tính lại, nhưng phải giữ điều kiện hình học, giả thiết từ trường đều hoặc xấp xỉ solenoid dài, quy ước dấu và ý nghĩa vật lý tương ứng.
- Các ứng dụng crosstalk, biến áp, đèn huỳnh quang, chống xung sét, vòng dây giao thông, đánh lửa và năng lượng từ trường Mặt Trời có thể phân vai làm mở bài hoặc đọc thêm. Nếu loại bỏ ứng dụng, cần giữ ít nhất một minh họa trực tiếp cho hỗ cảm, tự cảm và năng lượng từ trường.
