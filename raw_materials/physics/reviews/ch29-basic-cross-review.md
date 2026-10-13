# Rà soát độc lập bài tập chương 29: Bài 29.31–29.42

## Phạm vi và căn cứ

Đối chiếu toàn bộ phần Bài 29.31–29.42 trong `translations/chapter-29/13-bai-tap-31-60.md` với *University Physics with Modern Physics*, 15e, bản PDF tại `source/young-freedman-15.pdf`. Đọc văn bản trích xuất theo trang và kiểm tra trực tiếp hình E29.31–E29.33 trên trang in 982 (PDF trang 1002). Các câu 29.34–29.42 nằm trên trang in 982–984 (PDF trang 1002–1004). Tính lại mọi kết quả số của phần này bằng Python độc lập.

Phần được rà gồm đủ các ý: 29.31 (một câu), 29.32 (a–c), 29.33 (a–d), 29.34 (a–b), 29.35, 29.36 (a–b), 29.37, 29.38 (a–d), 29.39 (a–c), 29.40 (a–c), 29.41 (a–b), 29.42 (hai trường hợp a–b). Không phát hiện thiếu câu hay tiểu mục trong phạm vi này.

## Kết quả

Không phát hiện sai số học hoặc sai đáp án vật lý cần chặn trong các bài 29.31–29.42. Kết quả tính lại khớp với bản thảo sau khi làm tròn theo chữ số có nghĩa của đề:

| Bài | Kết quả kiểm tra độc lập |
| --- | --- |
| 29.31 | $v=IR/(BL)=35{,}0\,\mathrm{m/s}$; chiều sang phải để từ thông hướng vào trang tăng. |
| 29.32 | $B=1{,}333\ldots\,\mathrm T$ (làm tròn $1{,}3\,\mathrm T$); biểu thức lưu lượng $\mathcal R=\pi\mathcal E d/(4B)$ đúng với mô hình vận tốc trung bình đều được nêu. |
| 29.33 | $I_0=Bhv/R=0{,}225\,\mathrm A$; chiều kim đồng hồ lúc vào, bằng không khi ở trọn trong trường, ngược chiều kim đồng hồ lúc ra. Với $t=0$ khi cạnh trước vào, các mốc $\ell/v$, $D/v$, $(D+\ell)/v$ nhất quán. |
| 29.34 | $E=(r/2)|dB/dt|=2{,}8125\times10^{-3}\,\mathrm{V/m}$; nhìn từ cực nam, dòng ngược chiều kim đồng hồ. |
| 29.35–29.37 | $di/dt=9{,}2073\,\mathrm{A/s}$; hai điện trường cảm ứng lần lượt $1{,}0179\times10^{-4}$ và $2{,}0358\times10^{-4}\,\mathrm{V/m}$; suất điện động trung bình $9{,}5002\times10^{-4}\,\mathrm V$. |
| 29.38 | $j_D=103{,}45\,\mathrm{A/m^2}$; $dE/dt=1{,}1684\times10^{13}\,\mathrm{V/(m\,s)}$; $B(2{,}00\,\mathrm{cm})=1{,}30\,\mu\mathrm T$ và $B(1{,}00\,\mathrm{cm})=0{,}650\,\mu\mathrm T$. |
| 29.39 | $q=5{,}9925\times10^{-10}\,\mathrm C$; $dq/dt=i_C=6{,}00\,\mathrm{mA}$; dòng dịch tổng cũng bằng $6{,}00\,\mathrm{mA}$. |
| 29.40 | Tại $0{,}500\,\mu\mathrm s$: $q=9{,}00\times10^{-10}\,\mathrm C$, $E=2{,}0329\times10^5\,\mathrm{V/m}$, $V=406{,}6\,\mathrm V$; $dE/dt=4{,}066\times10^{11}\,\mathrm{V/(m\,s)}$, $j_D=3{,}60\,\mathrm{A/m^2}$, $i_D=1{,}80\,\mathrm{mA}$. |
| 29.41 | $i_D(1{,}5\,\mathrm s)=2{,}2412\times10^{-9}\,\mathrm A$; thời điểm trước đó để dòng bằng $1/6$ là $0{,}9584\,\mathrm s$. |
| 29.42 | Với $B_0=0{,}130\,\mathrm T<B_c$, $M=-B_0/\mu_0=-1{,}0345\times10^5\,\mathrm{A/m}$ và $B=0$ trong khối siêu dẫn. Với $B_0=0{,}260\,\mathrm T>B_c$, vật ở pha thường, $M\approx0$ và $B\approx B_0$ trong và ngoài trụ dài. |

## Hình và các điểm đối chiếu đặc biệt

Hình E29.31, E29.32 và E29.33 được đưa vào phần đề. Đã so trực tiếp với hình nguồn trên PDF trang 1002: hướng trường, vị trí thanh/điện trở, hướng chuyển động, kích thước và cấu hình đều khớp. Hình 29.23 được câu 29.38 dẫn chiếu nhưng không lặp lại trong phần bài tập; hình này đã có ở phần lý thuyết, `07-dong-dien-dich-maxwell.md` (dòng 83), nên người đọc toàn chương có thể tra được.

Hai chi tiết được kiểm riêng theo yêu cầu rà soát: Bài 29.40 dùng đúng thời điểm $0{,}500\,\mu\mathrm s$ như đề in, không phải một giá trị khác; Bài 29.41 giữ đúng yêu cầu “bằng một phần sáu” trên PDF trang 1004 (trang in 984). Lời giải dùng $i_D\propto t^4$, do đó $t=1{,}5/6^{1/4}=0{,}958\,\mathrm s$. Nếu đáp số appendix của bản PDF ghi $1/16$, đó là khác biệt với chính đề in; không nên đổi lời giải thành $1/16$ khi chưa có bản đính chính chính thức.

## Ghi chú biên tập nhẹ

- Ở `13-bai-tap-31-60.md:60`, câu dẫn của (c) Bài 29.32 có thể đổi thành “Trong mô hình này, $v$ là tốc độ trung bình của máu trên tiết diện” để nêu điều kiện dùng trong phép suy ra lưu lượng ngay trước công thức.
- Ở `13-bai-tap-31-60.md:410–431`, Bài 29.42 đã nêu kết quả, nhưng có thể gọi rõ “trường tới hạn $B_c$” ngay trong tóm tắt và giải thích rằng trụ rất dài giúp bỏ qua trường khử từ ở đầu trụ. Đây là tăng độ rõ, không phải sửa lỗi đáp án.

## Kiểm tra hình thức

Các đề và lời giải 29.31–29.42 có khối đề và lời giải tương ứng, không có tiểu mục nào bị bỏ. Đã rà các công thức hiển thị và đơn vị; phép tính nhiều bước dùng `aligned`. Đã mở trực tiếp trang PDF 1002 để xác nhận hình theo hướng/chiều chứ không dựa riêng vào OCR. Không chạy checker của repo làm bằng chứng cho phần rà này.

## Rà soát bổ sung: Luyện tập, câu hỏi và Bài 29.1–29.30

Đã đối chiếu trực tiếp PDF cho toàn bộ Guided Practice (VP29.8.1–.8.4, VP29.9.1–.9.4, VP29.11.1–.11.4 và bài toán cầu nối), Câu hỏi Q29.1–Q29.21, cùng Bài 29.1–29.30. Các câu hỏi thảo luận nằm ở trang in 979–980 (PDF trang 999–1000); hình các Bài 29.16–29.20 và E29.21 được xem trực tiếp trên trang in 981 (PDF trang 1001). Bài 29.1–29.30 nằm ở trang in 980–982 (PDF trang 1000–1002). Đã so các hình E29.7, E29.8, E29.12, E29.14–E29.22, E29.24–E29.29 với hình PDF khi đề dẫn hình; các chiều trường, vị trí vòng/thanh, khoảng cách và hướng chuyển động khớp. Hình E29.20 cho thấy hai cuộn quấn ngược chiều, giống hình đã đưa vào bài.

Mọi phần con của đề trong phạm vi này đều có mặt: Guided Practice gồm 4+4+4 bài kèm cầu nối; Q29.1–Q29.21 đủ 21 câu; Bài 29.1–29.30 đủ 30 bài và mọi mục con được giữ. Không phát hiện lỗi số học hoặc đáp án vật lý cần chặn trong phần bổ sung. Các kết quả số được tính lại bằng Python độc lập; những nhóm chính như sau:

| Bài hoặc cụm | Kết quả tính lại |
| --- | --- |
| VP29.8.1–.8.4 | $\Phi(0)=2{,}53\times10^{-4}\,\mathrm{Wb}$, $\Phi(2\,\mathrm s)=-1{,}99\times10^{-4}\,\mathrm{Wb}$, $|\mathcal E|=2{,}26\times10^{-4}\,\mathrm V$; cuộn 455 vòng có $|\mathcal E|=1{,}01\times10^{-2}\,\mathrm V$, $I=6{,}95\times10^{-4}\,\mathrm A$; VP29.8.3 cho $0{,}163\,\mathrm V$; VP29.8.4 cho $-\omega NAB_0\cos\omega t$. |
| VP29.9.1–.9.4 | Lần lượt $0{,}187\,\mathrm V$ và $2{,}34\,\mathrm{V/m}$; $0{,}900\,\mathrm A$; $2{,}40\times10^{-2}\,\mathrm V$; $4{,}12\,\mathrm{m/s}$. |
| VP29.11.1–.11.4 | Lần lượt $1{,}81\times10^3\,\mathrm{m^{-1}}$ và $7{,}70\times10^{-5}\,\mathrm{V/m}$; $2{,}70\times10^{-5}\,\mathrm{V/m}$; $dI/dt=-7{,}77$ và $+11{,}7\,\mathrm{A/s}$; $5{,}52\times10^{-6}\,\mathrm A$. Tốc độ giới hạn của bài cầu nối là $16\rho_m\rho_Rg/B^2$. |
| 29.1–29.6 | $0{,}0171\,\mathrm V$ và $0{,}0285\,\mathrm A$; $7{,}2\times10^{-8}\,\mathrm{Wb}$ mỗi vòng và $3{,}60\times10^{-4}\,\mathrm V$; 29.3 cho $-1{,}20\,\mathrm V$ ở $0{,}250\,\mathrm s$; 29.4 cho $Q=4{,}50\times10^{-4}\,\mathrm C$; $33{,}9\,\mathrm V$; 29.6 cho $1{,}13\times10^{-4}\,\mathrm A$ tại $5{,}00\,\mathrm s$. |
| 29.7–29.13 | 29.7 cho $|\mathcal E|=5{,}0624\times10^{-7}\,\mathrm V=0{,}506\,\mu\mathrm V$; 29.8 cho $0{,}122\,\mathrm V$ lúc đầu và $40{,}4\,\mathrm s$; 29.9 cho $5{,}44\,\mathrm{mV}$; 29.10 cho $90{,}3\,\mathrm V$; 29.11 cho $12{,}6\,\mathrm{mA}$ và $626\,\mu\mathrm A$; 29.13 cho $10{,}4\,\mathrm{rad/s}$. |
| 29.14, 29.22–29.30 | 29.14 cho $4{,}92\,\mathrm{mV}$ và $1{,}51\times10^{-4}\,\mathrm W$; 29.22 cho $1{,}323\times10^{-2}\,\mathrm A$; 29.23 cho $0{,}72\,\mathrm V$ và $0$; 29.24 cho $6{,}48\times10^{-3}\,\mathrm N$; 29.25 cho $0{,}675\,\mathrm V$ và $2{,}25\,\mathrm{V/m}$; 29.26 cho $0{,}0100\,\mathrm V$ khi cắt biên; 29.27 cho $3{,}00\,\mathrm V$, $2{,}00\,\mathrm A$, $0{,}800\,\mathrm N$, $6{,}00\,\mathrm W$; 29.28 cho $2{,}4375\,\mathrm V$ và $0{,}0975\,\mathrm A$; 29.29 cho $42{,}36\,\mathrm{mW}$; 29.30 cho $26{,}27\,\mathrm{m/s}$. |

Đối chiếu đặc biệt:

- Bài 29.7: Hình E29.7 đặt vòng bên phải dây có dòng hướng lên. Trường hướng vào trang như lời giải chọn. Từ thông và dấu suất điện động nhất quán, độ lớn tính lại là $0{,}506\,\mu\mathrm V$, khớp đáp số ở `16-dap-so.md`.
- Bài 29.16: Hình nguồn trang in 981 cho A ở trên dây đi lên, B dưới dây đi xuống, C phía trên chuyển động song song sang phải, D dưới dây đi lên. Dòng cảm ứng và lực ghi trong bản thảo khớp khi xét đúng cạnh gần dây: Với A, cạnh gần cùng chiều dây nên bị hút xuống; cạnh xa bị đẩy lên yếu hơn. B cũng bị hút về dây, C không có dòng, D bị đẩy ra xa.
- Bài 29.20: Hình nguồn và hình StudyHub đều cho cuộn B quấn ngược cuộn A. Nếu lấy từ trường do dòng A từ $a$ đến $b$ hướng sang phải, ba trường hợp cho dòng qua $R$: (a) phải sang trái; (b) phải sang trái; (c) trái sang phải. Cả ba hướng trong lời giải đúng với Lenz và cách nối hai đầu B trên hình.

Các bài tập còn lại và cả 21 câu hỏi thảo luận đã được rà về chiều từ trường, định luật Lenz, tích có hướng, giả thiết mạch hở/kín và nội dung từng mệnh đề. Không có mục nào bị thiếu hoặc lệch so với câu chữ trên PDF trong phạm vi đã đọc. Không đề xuất sửa nội dung cho các phần bổ sung này.
