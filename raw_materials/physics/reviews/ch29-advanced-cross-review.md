# Rà soát chéo chương 29, bài 29.43–29.74

## Phạm vi và phương pháp

Đối chiếu bản dịch và lời giải trong `raw_materials/physics/translations/chapter-29/13-bai-tap-31-60.md`, `14-bai-tong-hop-61-66.md`, `15-nang-cao-mcat.md`, cùng đáp số trong `16-dap-so.md` với PDF *Young & Freedman, University Physics*, ấn bản 15, các trang in 983–987 (PDF một-based 1003–1007). Đã đọc trực quan toàn bộ năm trang nguồn, gồm hình mạch, trục, mũi tên, bảng số liệu và đồ thị. Rà nội dung từng bài 29.43–29.74 và từng tiểu mục; tự lập phép tính Python độc lập cho các kết quả số bên dưới, không gọi verifier của repo.

## Lỗi cần sửa trước khi dùng

1. **29.58: Chép sai dấu của thành phần từ trường và kết luận ngược cực tính.** Bản thảo dòng 1049 ghi $B_z=+0{,}0900\,\mathrm T$, nhưng hình/văn bản nguồn ở trang in 985 (PDF 1005) ghi $B_z=-0{,}0900\,\mathrm T$. Với $\vec v=(6{,}80,0,0)\,\mathrm{m/s}$, thành phần $y$ của $\vec v\times\vec B$ là $-v_xB_z=+0{,}612\,\mathrm{V/m}$. Do đó $V_b-V_a=(\vec v\times\vec B)\cdot\vec L=+0{,}0919\,\mathrm V$: đầu **b** (phía trên phải) cao thế hơn **a**. Bản thảo dòng 1071–1082 cho dấu âm, dòng 1088 kết luận a cao thế hơn. Chú thích và hình lời giải tại dòng 1090 cùng SVG `docs/vat-ly-2/bai-giang/img/young-29/hinh-giai29-58.svg` cũng đang ghi a cao thế hơn, cần sửa đồng bộ. Độ lớn suất điện động $0{,}0919\,\mathrm V$ vẫn đúng.

2. **Đoạn dẫn MCAT: Đảo nghĩa một mệnh đề phủ định của nguồn.** Dòng 315 trong `15-nang-cao-mcat.md` nói các nhà nghiên cứu “hiện có thể kích thích thần kinh ở vị trí xác định trên người đang tỉnh”. Nguồn trang in 987 (PDF 1007) nói họ *cannot stimulate* thần kinh tại vị trí xác định ở người tỉnh, kể cả không xâm lấn. Bản dịch bỏ “không thể”, làm sai bối cảnh dẫn nhập cho kỹ thuật TMS. Sửa thành “chưa thể…” theo nguyên ý nguồn.

## Kết quả các phép tính độc lập

Các giá trị sau khớp bản thảo trong sai số làm tròn: 29.43(a) $2{,}52\times10^5\,\mathrm C$, 29.43(c) $0{,}106\,\mathrm T$; 29.44(a–c) $4{,}136\,\mathrm{m/s^2}$, $0{,}0669\,\mathrm{m/s}$, $7{,}50\,\mathrm{m/s^2}$; 29.45(a–b) $3{,}679\,\mathrm A$ và $1{,}347\,\mathrm{mA}$; 29.46 $1{,}831\,\mathrm{mA}$; 29.47 $16{,}19\,\mu\mathrm V$; 29.51 $17{,}92\,\mathrm{mV}$; 29.52 $1{,}591\,\mathrm s$; 29.54 $13{,}89\,\mathrm{m/s}$ giới hạn; 29.57(a,c) $0{,}1647\,\mathrm V$ và $0{,}04118\,\mathrm V$; 29.60 $R_1=125{,}66\,\Omega$, $R_2=0{,}2513\,\Omega$, $\tau=1{,}257\,\mathrm{ms}$, $I_2(1{,}26\,\mathrm{ms})=0{,}3650\,\mathrm A$; 29.62 $f=1{,}378\,\mathrm{Hz}$, biên độ tại 5 s $5{,}135\,\mathrm{cm}$, dòng lần qua cân bằng đầu $0{,}6762\,\mathrm A$; 29.63 $5{,}00\,\mathrm s$.

Tích phân diện tích đồ thị 29.64 cho $B(2\,\mathrm s)=0{,}933\,\mathrm T$, $B(5\,\mathrm s)=3{,}73\,\mathrm T$, $B(6\,\mathrm s)=4{,}20\,\mathrm T$. Khớp bình phương tối thiểu toàn bộ sáu điểm của 29.65 cho độ dốc $0{,}30714\,\mathrm{s^{-1}}$, hệ số chặn $2{,}14\times10^{-4}\,\mathrm{m/s^2}$, suy ra $B=3{,}69\,\mathrm T$ và thời gian giảm tốc $2{,}26\,\mathrm s$. Khớp toàn bộ năm điểm 29.66 cho độ dốc $5{,}20\,\mathrm{N,s/m}$, hệ số chặn $-0{,}0020\,\mathrm N$, suy ra $B=1{,}80\,\mathrm T$ và công suất tại $5{,}00\,\mathrm{cm/s}$ là $1{,}30\times10^{-2}\,\mathrm W$.

## Đối chiếu lý luận, chiều và đáp số

- 29.43(b) là ước lượng vì đề không ấn định số đèn/gạt mưa. Bản thảo nêu rõ giả thiết hai đèn, hai gạt mưa (60 A), và trường hợp thêm gạt mưa sau (65 A), nên đáp số diễn giải hợp lý.
- 29.45–46: Mạch lớn có $\tau=R_0C=200\,\mu\mathrm s$; điện trở cuộn nhỏ 15,0 Ω. Hình trang 983 xác nhận chiều dây gần vòng nhỏ là xuống khi tụ phóng, lên khi mạch được cấp nguồn để nạp tụ. Hai chiều cảm ứng mô tả trong bản thảo nhất quán với Lenz.
- 29.48: Hình trang 984 xác nhận pháp tuyến ban đầu song song $\vec B\parallel x$. Quay quanh $x$ cho suất điện động không, quay quanh $y$ hoặc cạnh song song $z$ cho cực đại $\omega BA=0{,}672\,\mathrm V$.
- 29.49, 29.51, 29.53, 29.55, 29.57, 29.59, 29.61, 29.63, 29.65, 29.69, 29.71 và 29.73: Công thức/chiều hoặc đáp số trong bản thảo phù hợp với suy luận độc lập và đáp số cuối chương. Các ngoại lệ khi so bản in A-18 được nêu riêng bên dưới.
- 29.61: Từ trường hướng vào trang và tăng, điện trường cảm ứng ngược chiều kim đồng hồ; tại điểm phía trên lực hướng trái, phía phải hướng lên, tâm bằng không.
- 29.62: Hình nguồn trang 985 xác nhận thanh chạy dọc ray và $W=0{,}400\,\mathrm m$ là khoảng cách hai ray. Công thức cản $b=B^2W^2/R$ đúng; nghiệm thả từ nghỉ dùng cả thành phần sin là cần thiết. Độ lớn dòng/chiều tại lần qua cân bằng đầu khớp.
- 29.64: Đồ thị nguồn trang 985 có tam giác tăng đến 3,00 mA tại 2,00 s, đoạn bằng 3,00 mA đến 5,00 s, rồi giảm về 0 tại 6,00 s. Bản thảo mô tả đúng và tích phân đúng; dòng về 0 tại 6 s chỉ có nghĩa trường thôi tăng.
- 29.65–66: Dữ liệu được chuyển đúng từ bảng ở trang 986. Đã kiểm khớp tất cả điểm, không chỉ hai điểm đầu/cuối; các hệ số góc, trường và công suất khớp.
- 29.67: Hình trang 986 cho tốc độ quay 2 Hz và trường hướng xuống. Tích phân $\vec v\times\vec B$ dọc cung cho $|\mathcal E|=0{,}0471\,\mathrm V$, dòng $4{,}71\,\mathrm{mA}$; chiều trong thanh thẳng đứng hướng lên như bản thảo.
- 29.68–70: Kiểm tra đối xứng và công thức: $i_D=2\pi\varepsilon_0\eta tr^2$, $B=\mu_0\varepsilon_0\eta tr$, $|\Phi|=\frac12\mu_0\varepsilon_0\eta tba^2$; 29.69 dùng thành phần trường vuông góc mặt ray $B\cos\phi$ và cân bằng công suất ở tốc độ giới hạn; 29.70 có $J_x=5mL^2/12$, mômen trọng lực theo $-x$ và mômen cảm ứng theo $+x$ khi quay xuống. Lời giải thống nhất với mô hình và dấu đã chọn.
- MCAT 29.71–74: Hình trang 987 cho chiều 1 là chiều tạo trường ngược trường cuộn khi dòng cuộn tăng, chiều 2 là chiều duy trì trường khi dòng cuộn giảm; đáp án (c) ở 29.71 đúng. Suất điện động vòng tăng theo $r^2$ nên 29.72 chọn (b). Độ dốc cực đại lớn hơn ở đường A nên 29.73 chọn (a). Đạo hàm có xung dương hẹp lúc trường tăng nhanh rồi phần âm nhỏ, dài lúc trường giảm chậm; đồ thị C và đáp án (c) ở 29.74 phù hợp.

## Đối chiếu riêng với đáp số in ở A-18

- 29.47: Ảnh A-18 in rõ $16{,}2\,\mu\mathrm V$, không phải mV. Bản thảo dùng đúng đơn vị.
- 29.67: Đáp số A-18 in $4{,}73\,\mathrm A$, nhưng đề cho suất điện động khoảng $0{,}0471\,\mathrm V$ trên điện trở $10{,}0\,\Omega$, nên dòng phải là $4{,}71\,\mathrm{mA}$. Bản thảo ghi $4{,}71\,\mathrm{mA}$ và đúng theo tính toán; đáp số sách có vẻ sai đơn vị và lệch nhẹ số làm tròn.
- 29.45: A-18 ghi $1{,}33\,\mathrm{mA}$. Tính lại từ các số liệu in (dòng mạch lớn $100e^{-1}/10=3{,}679\,\mathrm A$, $\tau=200\,\mu\mathrm s$, điện trở cuộn nhỏ 15,0 Ω) cho $1{,}347\,\mathrm{mA}$, tức $1{,}35\,\mathrm{mA}$ ở ba chữ số có nghĩa như bản thảo. Chênh lệch khoảng 1,3%, nhỏ nhưng không giải thích được bằng làm tròn chuẩn của dữ liệu đã cho.
- 29.43: A-18 trong ảnh đọc như $11\,\mathrm T$ hoặc thiếu dấu thập phân. Tính từ $\mathcal E_{av}=2N\omega BA/\pi$ cho $0{,}106\,\mathrm T$, phù hợp bản thảo $0{,}11\,\mathrm T$; không dùng giá trị 11 T.

Ngoài các điểm này, các đáp số lẻ có mặt trong A-18 đã đối chiếu khớp bản thảo trong độ chính xác phù hợp. Hai lỗi nội dung cần sửa trước khi dùng vẫn là dấu/cực tính ở 29.58 và câu dẫn MCAT bị đảo nghĩa.
