# Sổ đối chiếu nguồn Chương 28, mục 28.5–28.8

## Phạm vi và nguồn

Đối chiếu trực quan bản *University Physics with Modern Physics*, ấn bản 15, PDF `raw_materials/physics/source/young-freedman-15.pdf`. Phạm vi chính là trang in 927–941 (trang PDF 947–961), gồm trọn các mục 28.5–28.8. Ngoài ra, phạm vi bao gồm toàn bộ phần tóm tắt chương trên trang in 942–943 (PDF 962–963), từ hàng 28.1 đến 28.8, toàn bộ bảng phân bố từ trường và hình đường trễ vật liệu từ. Phần Guided Practice bắt đầu ở nửa dưới trang 943 và không thuộc phạm vi.

Trang in 927 mở đầu bằng phần cuối mục 28.4. Đoạn này nhắc rằng sau lần sửa định nghĩa SI năm 2018, giá trị của \(\mu_0\) không còn được định nghĩa chính xác bằng \(4\pi\times10^{-7}\,\mathrm{T\,m/A}\), dù giá trị làm tròn vẫn đủ chính xác cho các phép tính thông thường; sai số tương đối cỡ \(2\times10^{-10}\). Đoạn kế tiếp giới thiệu hiệu ứng thắt dòng (pinch) trong chất lỏng dẫn điện/plasma và ứng dụng trong một kiểu phản ứng nhiệt hạch. Đây là phần chuyển tiếp của 28.4, không tính là nội dung cần biên soạn của 28.5. Hình nam châm điện nâng sắt vụn (28.11) thuộc phần mở đầu 28.5.

Ví dụ 28.5 và câu tự kiểm tra cuối 28.4 cũng xuất hiện trên trang 927 nhưng nằm ngoài phạm vi. Không đưa chúng vào danh mục bài tập của các mục 28.5–28.8. Tương tự, các bài Guided Practice VP28.2.x và VP28.5.x ở cuối trang 943 không nằm trong phần tóm tắt chương.

## Danh mục nội dung theo mục

### 28.5 — Từ trường trên trục của vòng dây có dòng điện

- Các trang in 927–930 (PDF 947–950). Hình 28.11–28.15; công thức (28.12)–(28.18); Ví dụ 28.6; ứng dụng MRI và phần tự kiểm tra cuối mục.
- Định luật Biot–Savart cho phần tử dòng điện: \(d\vec B\) tỉ lệ với \(I\,d\vec l\times\hat r/r^2\). Với vòng tròn bán kính \(a\), điểm khảo sát \(P\) nằm trên trục cách tâm \(x\), phần tử \(d\vec l\) vuông góc với \(\vec r\). Các thành phần vi phân được phân tích theo trục và phương ngang. Cặp phần tử đối diện triệt tiêu thành phần ngang, còn các thành phần dọc trục cùng chiều.
- Tích phân quanh vòng dùng \(\int dl=2\pi a\), cho trường trên trục:

  $$
  B_x=\frac{\mu_0 I a^2}{2(x^2+a^2)^{3/2}}.
  $$

  Chiều xác định bằng quy tắc bàn tay phải. Với \(N\) vòng gần như đồng phẳng, nhân độ lớn với \(N\). Tại tâm, \(B=\mu_0NI/(2a)\), là cực đại trên trục; khi \(|x|\gg a\), độ lớn giảm theo xấp xỉ \(1/|x|^3\).
- Mômen lưỡng cực của vòng là \(\vec\mu=IA\hat n\), với \(A=\pi a^2\); với \(N\) vòng, \(\mu=NIA\). Thay vào biểu thức trên được dạng theo mômen lưỡng cực. Công thức trường vòng này chỉ áp dụng trên trục, không phải công thức trường tại mọi điểm quanh vòng.
- Ứng dụng MRI: nam châm tạo trường cỡ 1,5 T; bệnh nhân nằm trong lòng cuộn dây. Dòng điện lớn gây tỏa nhiệt, nên hệ dùng helium lỏng ở 4,2 K để làm mát cuộn dây.
- Ví dụ 28.6 cho cuộn \(N=100\), \(a=0{,}60\,\mathrm m\), \(I=5{,}0\,\mathrm A\), tại \(x=0{,}80\,\mathrm m\): trường xấp xỉ \(1{,}1\times10^{-4}\,\mathrm T\). Điểm có trường bằng một phần tám trường tại tâm nằm ở \(x=\pm\sqrt3a\), tức khoảng \(\pm1{,}04\,\mathrm m\). Mômen từ của cuộn xấp xỉ \(5{,}7\times10^2\,\mathrm{A\,m^2}\); trường tại điểm xa này tương đương cỡ trường Trái Đất, minh họa vì sao khó tạo trường mạnh ở xa.
- Tự kiểm tra 28.5 yêu cầu xét dấu các thành phần trường của một phần tử dòng điện ở phía \(y<0\) và phía \(z<0\). Phải lấy dấu từ tích có hướng \(d\vec l\times\vec r\), không đọc ký hiệu mũi tên tách khỏi hình học.

### 28.6 — Định luật Ampere

- Các trang in 930–933 (PDF 950–953). Hình 28.16–28.19; công thức (28.19)–(28.20); Chiến lược 28.2; phần tự kiểm tra cuối mục.
- Định luật Ampere phát biểu tích phân đường kín của trường từ bằng \(\mu_0\) nhân dòng điện đại số được bao bởi đường kín. Hướng đi quanh đường tích phân cùng quy tắc bàn tay phải xác định dấu dòng điện.
- Với dây thẳng dài, đối xứng trụ cho \(B=\mu_0I/(2\pi r)\). Trên đường tròn đồng tâm, \(\vec B\) tiếp tuyến và có độ lớn không đổi, nên tích phân bằng \(\pm\mu_0I\), tùy chiều đi quanh vòng. Nếu đường kín không bao dây, tích phân bằng không dù trường từ tại nhiều điểm trên đường vẫn khác không: các cung và đoạn thẳng đóng góp triệt tiêu.
- Dạng tổng quát của lập luận dùng \(\vec B\cdot d\vec l=B\,dl\cos\phi\), với \(dl\cos\phi=r\,d\theta\). Tổng biến thiên góc là \(2\pi\) nếu đường bao dây và bằng không nếu không bao dây. Nhiều dây được xử lý bằng tổng dòng điện đại số nằm trong đường kín. Dòng điện ngoài đường kín vẫn có thể góp phần vào \(\vec B\) tại đường đi nhưng không góp vào giá trị tích phân tổng.
- Điều kiện vật lý nêu trong mục là dòng điện không đổi theo thời gian và không có điện trường biến thiên theo thời gian. Tích phân Ampere không phải công cơ học và không hàm ý lực từ là lực thế.
- Chiến lược 28.2: Chọn đường tích phân đi qua điểm cần tìm và tận dụng đối xứng để \(B\) không đổi hoặc \(\vec B\perp d\vec l\) trên các đoạn. Đường chọn phải đủ đơn giản để tính tích phân, nhưng vẫn phải bao đủ dòng điện cần tính theo dấu. Định luật áp dụng tổng quát, song chỉ hữu ích trực tiếp khi có đối xứng cao.
- Tự kiểm tra 28.6 về đường sức quanh nam châm vĩnh cửu cần nhận ra dòng điện liên kết với vật liệu nam châm; chiều dòng điện được xác định theo quy tắc bàn tay phải.

### 28.7 — Ứng dụng định luật Ampere

- Các trang in 934–936 (PDF 954–956). Hình 28.20–28.25; công thức (28.21)–(28.24); Ví dụ 28.7–28.10; tự kiểm tra về cáp đồng trục.
- Ví dụ 28.7 áp dụng đường tròn Ampere cho dây dẫn thẳng dài, nhắc lại kết quả \(B=\mu_0I/(2\pi r)\) và suy ra chiều bằng quy tắc bàn tay phải.
- Ví dụ 28.8 xét dây trụ đặc bán kính \(R\) có dòng \(I\) phân bố đều. Mật độ dòng là \(J=I/(\pi R^2)\). Bên trong, dòng điện được bao tỉ lệ với diện tích \(\pi r^2\), nên \(I_{\rm enc}=Ir^2/R^2\) và:

  $$
  B(r)=\begin{cases}
  \dfrac{\mu_0Ir}{2\pi R^2},&r<R,\\[4pt]
  \dfrac{\mu_0I}{2\pi r},&r>R.
  \end{cases}
  $$

  Hai nhánh khớp liên tục tại \(r=R\). Bên ngoài, trường không phụ thuộc bán kính dây hay cách dòng phân bố theo bán kính nếu đối xứng trụ vẫn đúng. Đồ thị tăng tuyến tính bên trong, đạt cực đại tại bề mặt rồi giảm như \(1/r\).
- Tự kiểm tra cáp đồng trục: Dòng ở lõi và dòng ngược chiều có cùng độ lớn ở vỏ trụ khiến dòng tổng được bao bên ngoài bằng không, nên trường ngoài bằng không trong mô hình đối xứng lý tưởng.
- Ví dụ 28.9 xét ống dây dài, quấn sít. Ở gần trung điểm, trường bên trong gần đều, còn bên ngoài gần bằng không. Hình chữ nhật Ampere có cạnh dài \(L\) song song trường, các cạnh ngắn vuông góc trường và nhánh ngoài nằm nơi trường gần bằng không. Dòng được bao là \(nLI\), do đó \(B=\mu_0nI\), với \(n=N/\ell\) là số vòng trên một đơn vị chiều dài. Độ đều theo tiết diện được suy ra từ việc vị trí cạnh bên trong không nhất thiết phải nằm trên trục. Gần đầu ống dây rất dài, trường xấp xỉ một nửa trường giữa ống.
- Ví dụ 28.10 xét hình xuyến quấn sít lý tưởng. Đường tròn 1 trong lỗ không bao dòng, đường 3 ngoài xuyến có các lượt dây xuyên qua theo hai chiều nên dòng đại số tổng bằng không, còn đường 2 trong lõi bao \(NI\). Vì vậy trong lõi \(B=\mu_0NI/(2\pi r)\), theo chiều xác định từ hướng tích phân. Trường thay đổi theo bán kính; nếu lõi mỏng có thể lấy gần đúng \(B\approx\mu_0nI\). Hình xuyến quấn thực có đường dây xoắn ốc nên trường ngoài không triệt tiêu chính xác; ước lượng một vòng dòng điện cho trường ngoài nhỏ hơn trường trong một hệ số cỡ \(N/\pi\).
- Các kết quả trong phần này giả sử chân không hoặc môi trường không từ tính đáng kể. Lõi từ làm thay đổi trường và được xử lý tiếp ở mục 28.8.

### 28.8 — Từ tính trong vật chất

- Các trang in 937–941 (PDF 957–961). Hình 28.26–28.29; Bảng 28.1; công thức (28.25)–(28.32); Ví dụ 28.11–28.12; ứng dụng hạt nano hướng đích; tự kiểm tra cuối mục.
- Phần mở đầu nêu các ứng dụng của lõi sắt, nam châm vĩnh cửu và lưu trữ từ trên đĩa, rồi phân biệt vật liệu nghịch từ, thuận từ và sắt từ.
- Mô hình quỹ đạo electron là hình ảnh cổ điển sơ lược: electron chuyển động quanh hạt nhân tương đương một vòng dòng điện có độ lớn \(e/T=ev/(2\pi r)\). Mômen từ có độ lớn \(\mu=evr/2\), còn mômen động lượng quỹ đạo \(L=mvr\). Với electron, vectơ mômen từ ngược chiều vectơ mômen động lượng; quan hệ độ lớn là \(\mu=eL/(2m)\). Không được hiểu mô hình quỹ đạo cổ điển là mô tả đầy đủ chuyển động lượng tử.
- Các thành phần mômen động lượng lượng tử hóa theo đơn vị \(h/(2\pi)\); do bất định, không xác định đồng thời phương vectơ mômen một cách cổ điển. Từ đó định nghĩa magneton Bohr \(\mu_B=eh/(4\pi m)=9{,}274\times10^{-24}\,\mathrm{A\,m^2}=\mathrm{J/T}\). Mômen spin nội tại của electron là tính chất riêng, không phải quả cầu điện tích quay; độ lớn mômen spin xấp xỉ \(1{,}001\mu_B\).
- Ở vật liệu thuận từ, nhiều mômen vi mô triệt tiêu từng cặp, nhưng một số mômen tổng còn lại cỡ \(\mu_B\). Từ trường gây mômen lực định hướng chúng, làm tăng trường tổng. Độ từ hóa \(M=\mu_{\rm total}/V\), đóng góp trường \(\mu_0M\), nên trong mô hình tuyến tính \(B=B_0+\mu_0M\). Hệ số từ thẩm tương đối \(K_m>1\), độ từ thẩm \(\mu=K_m\mu_0\), độ cảm từ \(\chi_m=K_m-1\); cả hai hệ số tương đối đều không thứ nguyên. Ở nhiệt độ phòng, các giá trị thuận từ nêu trong sách thường chỉ nhỉnh hơn 1 một lượng nhỏ.
- Bảng 28.1 cho độ cảm từ tại 20 °C theo đơn vị \(10^{-5}\). Thuận từ: phèn sắt amoni 66, urani 40, platin 26, nhôm 2,2, natri 0,72, khí oxy 0,19. Nghịch từ: bitmut −16,6, thủy ngân −2,9, bạc −2,6, carbon dạng kim cương −2,1, chì −1,8, natri clorua −1,4, đồng −1,0.
- Chuyển động nhiệt làm nhiễu sự định hướng thuận từ. Độ cảm từ giảm khi nhiệt độ tăng; định luật Curie được trình bày dưới dạng \(M=CB/T\), với \(C\) là hằng số Curie. Thuận từ bị hút yếu về phía trường mạnh và hiệu ứng tăng khi làm lạnh.
- Ví dụ 28.11: Nitric oxide thuận từ, mômen chiếu cực đại cỡ \(\mu_B\), trường 1,5 T, nhiệt độ 300 K. Năng lượng tương tác cực đại xấp xỉ \(1{,}4\times10^{-23}\,\mathrm J=8{,}7\times10^{-5}\,\mathrm{eV}\), trong khi động năng tịnh tiến trung bình \(3kT/2\approx6{,}2\times10^{-21}\,\mathrm J=0{,}039\,\mathrm{eV}\). Tỉ số cỡ 0,2% giải thích sự định hướng chỉ nhẹ ở nhiệt độ phòng.
- Vật liệu nghịch từ không có mômen từ tổng cố hữu; từ trường gây dòng điện cảm ứng hoặc mômen cảm ứng ngược chiều trường ngoài theo định luật Lenz. Vì vậy \(\chi_m<0\) và \(K_m\) nhỏ hơn nhưng rất gần 1. Độ cảm từ nghịch từ gần như không phụ thuộc nhiệt độ trong mô tả này.
- Vật liệu sắt từ như sắt, niken, coban và hợp kim có mômen lân cận tự sắp xếp thành miền ngay cả khi chưa có trường ngoài. Khi chưa từ hóa, các miền phân bố hướng gần ngẫu nhiên. Trường ngoài làm dịch chuyển vách miền và xoay các miền, tạo độ từ hóa lớn; \(K_m\) có thể đạt 10³–10⁵. Khi gần bão hòa, tăng trường thêm không làm \(M\) tăng đáng kể.
- Đường trễ biểu diễn \(M\) theo trường ngoài \(B_0\) trên các chu trình tăng/giảm và đảo chiều. Sau bão hòa, giảm trường về không vẫn còn từ hóa dư. Cần trường ngược chiều để đưa từ hóa về không; tăng trường ngược thêm sẽ từ hóa vật liệu theo chiều ngược lại. Vật liệu từ cứng có vòng trễ rộng, phù hợp nam châm vĩnh cửu và lưu trữ; sắt mềm có vòng hẹp, độ từ thẩm cao và tổn hao chu trình nhỏ hơn, phù hợp lõi động cơ/máy biến áp. Nam châm vĩnh cửu điển hình có trường dư khoảng 1 T, tương ứng \(M\) cỡ \(8\times10^5\,\mathrm{A/m}\).
- Ứng dụng sinh học đề cập hạt nano sắt từ có thể được nhắm đến tế bào ung thư và điều hướng bằng nam châm ngoài; hình dùng thước tỷ lệ 100 μm.
- Ví dụ 28.12: Khối lập phương có \(M=8\times10^5\,\mathrm{A/m}\) và cạnh 2 cm có mômen tổng \(\mu=MV=6\,\mathrm{A\,m^2}\). Ở điểm trên trục cách tâm 10 cm, xấp xỉ khối bằng vòng dòng điện/lưỡng cực vì khoảng cách lớn hơn nhiều kích thước khối; bỏ các hiệu chỉnh bậc \(a^2/x^2\), trường xấp xỉ \(10^{-3}\,\mathrm T=10\,\mathrm G\). Trường ngoài vật liệu dùng \(\mu_0\), không thay bằng độ từ thẩm của lõi.
- Tự kiểm tra 28.8: Natri và urani là thuận từ nên bị hút yếu; bitmut và chì là nghịch từ nên bị đẩy yếu.

## Toàn bộ phần tóm tắt Chương 28

Trang in 942 trình bày sáu hàng đầu, còn trang in 943 tiếp tục bằng bảng phân bố từ trường và hàng tóm tắt vật liệu từ. Hàng 28.1–28.8 được đối chiếu như sau:

- 28.1, từ trường do điện tích chuyển động: \(\vec B=(\mu_0/4\pi)\,q\vec v\times\hat r/r^2\); trường vuông góc với vận tốc và phương từ nguồn đến điểm đo. Hình nhắc nguyên lý chồng chất bằng tổng vectơ trường của các điện tích chuyển động.
- 28.2, từ trường do phần tử dòng điện: dạng Biot–Savart \(d\vec B=(\mu_0/4\pi)I\,d\vec l\times\hat r/r^2\); trường vuông góc với \(d\vec l\) và \(\hat r\). Trường do dây hữu hạn là tích phân của các phần tử trường dọc dây.
- 28.3, dây thẳng dài: \(B=\mu_0I/(2\pi r)\), đường sức là các đường tròn đồng tâm và chiều theo quy tắc bàn tay phải.
- 28.4, lực giữa hai dây dẫn song song dài: \(F/L=\mu_0II'/(2\pi r)\); dòng cùng chiều hút nhau, dòng ngược chiều đẩy nhau. Định nghĩa ampe gắn với lực trên một đơn vị chiều dài này.
- 28.5, vòng dòng điện: trường trên trục \(B_x=\mu_0Ia^2/[2(x^2+a^2)^{3/2}]\), còn tâm của \(N\) vòng có \(B_x=\mu_0NI/(2a)\). Sơ đồ phân tích thành phần cho thấy các thành phần ngang triệt tiêu theo cặp.
- 28.6, định luật Ampere: \(\oint\vec B\cdot d\vec l=\mu_0I_{\rm encl}\); dấu dòng điện dương theo quy tắc bàn tay phải.
- 28.7, bảng phân bố từ trường tổng kết các đối xứng lý tưởng và vị trí khảo sát:
  - Dây thẳng dài, tại điểm cách dây \(r\): \(B=\mu_0I/(2\pi r)\).
  - Vòng tròn bán kính \(a\), trên trục: \(B=\mu_0Ia^2/[2(x^2+a^2)^{3/2}]\); tại tâm, với \(N\) vòng: \(B=\mu_0NI/(2a)\). Nếu có \(N\) vòng, nhân kết quả trường của một vòng với \(N\).
  - Dây trụ dài bán kính \(R\), dòng phân bố đều: bên trong \(B=(\mu_0I/2\pi)(r/R^2)\) khi \(r<R\); bên ngoài \(B=\mu_0I/(2\pi r)\) khi \(r>R\).
  - Ống dây dài, quấn sít, có \(n\) vòng trên một đơn vị chiều dài, gần trung điểm: bên trong gần tâm \(B=\mu_0nI\), ngoài ống dây \(B\approx0\).
  - Hình xuyến quấn sít có \(N\) vòng: trong vùng được cuộn dây bao quanh, ở khoảng cách \(r\) tới trục đối xứng, \(B=\mu_0NI/(2\pi r)\); bên ngoài vùng đó \(B\approx0\).
- 28.8, vật liệu từ: độ từ hóa bổ sung vào trường; với vật liệu thuận từ/nghịch từ thay \(\mu_0\) bằng \(\mu=K_m\mu_0\), và \(\chi_m=K_m-1\). Độ cảm từ thuận từ nhỏ dương, nghịch từ nhỏ âm; vật liệu sắt từ có \(K_m\) lớn và không hằng, một số nam châm giữ từ hóa sau khi trường ngoài được bỏ đi. Đồ thị bên phải minh họa độ từ hóa \(M\) theo trường ngoài \(B_0\) trên vòng trễ.

Đây là phần tóm tắt nên bảng không có số thứ tự phương trình mới; các biểu thức lặp lại giữ nguyên số phương trình gốc khi được chỉ rõ, còn bảng dùng như tập hợp kết quả không gắn nhãn số riêng.

## Hình và tài sản ảnh đã chuẩn bị

Script `scripts/prepare-physics28-theory-b-assets.py` khai báo 31 vùng ở 2,5× từ trang PDF theo số trang in. Các ảnh đầu ra do phạm vi này sở hữu:

- 28.11–28.15: `hinh-28-11.png` đến `hinh-28-15.png`; ảnh nam châm điện, hình học phần tử dòng điện và vòng dây, quy tắc bàn tay phải, đồ thị trường trên trục, đường sức vòng dây.
- Ứng dụng MRI: `ung-dung-mri-28.png`.
- 28.16–28.19: các hình về đường tích phân quanh dây, những đường kín tùy ý và định luật Ampere.
- 28.20–28.25: dây trụ có dòng đều, đồ thị trường bên trong/ngoài dây, đường sức ống dây, đường Ampere hình chữ nhật, trường ống dây theo trục, đường tích phân của hình xuyến.
- Cáp đồng trục: `ung-dung-cap-dong-truc.png`.
- 28.26–28.29 và Bảng 28.1: mô hình mômen electron, bảng độ cảm từ, miền thuận từ, đường trễ và phân loại vật liệu từ cứng/mềm.
- Ứng dụng hạt nano: `ung-dung-nano-sat-ung-thu.png`.
- Tóm tắt 28.1–28.6 trên trang in 942: sáu hình `tom-tat-28-01-dien-tich-chuyen-dong.png` đến `tom-tat-28-06-ampere.png`.
- Tóm tắt trang in 943: toàn bộ bảng `tom-tat-28-bang-phan-bo-dong.png` và hình đường trễ `tom-tat-28-tu-tinh.png`.

Các ảnh được giới hạn trong hình và chữ nhúng trong hình; caption hoặc văn xuôi lân cận không được đưa vào. Danh mục đầu ra trong thư mục chung có thêm ảnh của hai phần khác do tác nhân khác tạo, không thuộc phạm vi báo cáo này.

Module chú giải là `docs/.vitepress/physics28-theory-b-image-annotations.mjs`. Chú giải tiếng Việt đi cùng đúng chuỗi tiếng Anh một lần cho các hình có nhãn/câu tiếng Anh nhúng. Các hình chỉ có ký hiệu/toán học hoặc không có chữ tiếng Anh có mảng chú giải rỗng. Không thêm module này vào registry toàn cục theo phạm vi đã giao.

## Kiểm tra phạm vi

- Đã kiểm tra trực quan các trang nguồn in 927–943; phần ảnh tóm tắt giới hạn ở sáu hàng trên trang 942, bảng trường và hàng vật liệu từ trên trang 943.
- Danh mục công thức trong phạm vi: (28.12)–(28.18), (28.19)–(28.20), (28.21)–(28.24), (28.25)–(28.32).
- Ví dụ trong phạm vi: 28.6–28.12; tự kiểm tra thuộc 28.5, 28.6, 28.7, 28.8; Chiến lược 28.2; Bảng 28.1; các ứng dụng MRI, cáp đồng trục, hạt nano.
- Không trích ảnh/chữ từ phần Guided Practice phía dưới trang 943 hoặc từ các trang trước 927, ngoài việc ghi chú rõ nội dung chuyển tiếp ở đầu trang 927.
