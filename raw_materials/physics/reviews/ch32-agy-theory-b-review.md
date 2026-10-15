# Chương 32 (Lý thuyết B): Báo cáo rà soát và đối chiếu nguồn

Ngày: 2026-10-15.
Trạng thái: Đã hoàn tất đối chiếu toàn diện lý thuyết các mục 32.4–32.5, năm ví dụ 32.3–32.7, các câu tự kiểm và toàn bộ tổng kết chương 32. Dừng đúng tại ranh giới phân công của tác vụ physics32-agy-b.

## Nguồn và nơi đến

Nguồn tài liệu là tập tin PDF giáo trình đại học chuẩn tại `raw_materials/physics/source/young-freedman-15.pdf` (SHA256: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`). Phạm vi thực hiện nằm trên các trang in 1061–1070, tương ứng các trang PDF 1081–1090. Văn bản trích xuất tại `qa/physics/full-source/pdf-1081.txt` đến `pdf-1090.txt` được dùng đối chiếu song song với việc đọc trực tiếp hình vẽ, công thức và nhãn từ tệp PDF gốc.

| Đơn vị nguồn | Tập tin đích | Thành phần học thuật giữ lại |
| :--- | :--- | :--- |
| **Mục 32.4** (Năng lượng và động lượng trong sóng điện từ) | `raw_materials/physics/translations/chapter-32/04-nang-luong-dong-luong.md` | Mật độ năng lượng điện từ trường, sự cân bằng năng lượng điện và từ trong sóng phẳng chạy ($u_E = u_B$), vector Poynting $\vec{S}$, tốc độ dòng năng lượng qua tiết diện, cường độ sóng hình sin $I = |\langle \vec{S} \rangle| = S_{\text{av}}$, sóng truyền qua điện môi tuyến tính đồng nhất đẳng hướng không tán sắc không tiêu tán với $u_B = B^2/(2\mu)$, ảnh ứng dụng y học phẫu thuật laser (`ung-dung-32-song-trong-chat-lieu.png`), cảnh báo phân biệt giá trị tức thời và giá trị trung bình của vector Poynting, mật độ động lượng trường, tốc độ truyền động lượng, áp suất bức xạ trường hợp hấp thụ hoàn toàn và phản xạ hoàn toàn, áp suất bức xạ trong lòng các sao lớn và tinh vân, Ví dụ 32.3, 32.4, 32.5, Câu hỏi tự kiểm 32.4. |
| **Mục 32.5** (Sóng dừng điện từ) | `raw_materials/physics/translations/chapter-32/05-song-dung-dien-tu.md` | Phản xạ tại mặt phẳng dẫn điện lý tưởng, điều kiện biên triệt tiêu điện trường tiếp tuyến ($E_\parallel = 0$), vai trò dòng điện mặt cảm ứng sinh sóng phản xạ, phương trình sóng dừng $E_y(x, t)$ và $B_z(x, t)$, vị trí các mặt phẳng nút và bụng của điện trường và từ trường, tính chất lệch pha $90^\circ$ theo thời gian, kiểm chứng hệ phương trình Maxwell và phương trình vi phân sóng bằng vi phân giải tích và số học, sóng dừng trong hộp cộng hưởng, tần số và bước sóng của các mode dao động riêng, ý nghĩa lịch sử của thí nghiệm Hertz, phản xạ tại mặt phân cách điện môi, ứng dụng sóng dừng và đĩa quay trong lò vi sóng, Ví dụ 32.6, 32.7, Câu hỏi tự kiểm 32.5. |
| **Tổng kết chương** | `raw_materials/physics/translations/chapter-32/09-tom-tat.md` | Đầy đủ 5 khối kiến thức tổng kết tại trang PDF 1089: Phương trình Maxwell và sóng điện từ; Sóng điện từ hình sin; Sóng điện từ trong vật chất; Năng lượng và động lượng trong sóng điện từ; Sóng dừng điện từ. Kèm đúng 4 hình vẽ tổng kết thực tế của giáo trình `tom-tat-32-01.png` đến `tom-tat-32-04.png` trong các nhóm tương ứng (loại bỏ dẫn chiếu trùng lặp 05 khỏi bài giảng; khối vật chất không có hình vẽ trong nguyên tác). |

## Số lượng đã đối chiếu

- **Công thức và phương trình**: Đầy đủ 17 nhãn phương trình gốc trong phạm vi lý thuyết B, xuất hiện đúng một lần duy nhất cho mỗi nhãn trong bài lý thuyết và mỗi khối toán chỉ chứa tối đa một nhãn:
  - Nhóm năng lượng và động lượng: (32.23), (32.24), (32.25), (32.26), (32.27), (32.28), (32.29), (32.30), (32.31), (32.32), (32.33).
  - Nhóm sóng dừng và hộp cộng hưởng: (32.34), (32.35), (32.36), (32.37), (32.38), (32.39).
  - Nhóm tổng kết chương: Hệ thống hóa lại các phương trình (32.4), (32.8), (32.9), (32.17), (32.18), (32.21), (32.28), (32.29), (32.31).
- **Ví dụ bài tập**: Đầy đủ 5 ví dụ:
  - Ví dụ 32.3: Năng lượng trong sóng phi sin ($E = 100\,\mathrm{V/m}$, $B = 3{,}33 \times 10^{-7}\,\mathrm{T}$, $u = 8{,}85 \times 10^{-8}\,\mathrm{J/m^3}$, $S = 26{,}5\,\mathrm{W/m^2}$).
  - Ví dụ 32.4: Năng lượng trong sóng hình sin phát vào bán cầu ($P = 50\,\mathrm{kW}$, $R = 100\,\mathrm{km}$, $A = 6{,}28 \times 10^{10}\,\mathrm{m^2}$, $I = 7{,}96 \times 10^{-7}\,\mathrm{W/m^2}$, $E_{\max} = 2{,}45 \times 10^{-2}\,\mathrm{V/m}$, $B_{\max} = 8{,}17 \times 10^{-11}\,\mathrm{T}$).
  - Ví dụ 32.5: Công suất và áp suất từ ánh sáng Mặt Trời ($I = 1{,}4\,\mathrm{kW/m^2}$, $A = 4{,}0\,\mathrm{m^2}$, $P = 5{,}6\,\mathrm{kW}$, $p_{\text{rad}} = 4{,}7 \times 10^{-6}\,\mathrm{Pa}$, $F = 1{,}9 \times 10^{-5}\,\mathrm{N}$).
  - Ví dụ 32.6: Cường độ trong sóng dừng (chứng minh $S_x(x, t) \propto \sin 2kx \sin 2\omega t$ và giá trị trung bình $I = |\langle \vec{S} \rangle| = S_{\text{av}} = 0$; phân biệt rành mạch với giá trị trung bình độ lớn $\langle |S_x| \rangle > 0$).
  - Ví dụ 32.7: Sóng dừng trong hộp cộng hưởng hai thành ($L = 1{,}50\,\mathrm{cm}$, $\lambda_1 = 3{,}00\,\mathrm{cm}$, $f_1 = 10\,\mathrm{GHz}$, xác định chính xác các tọa độ nút và bụng của $\vec{E}$ và $\vec{B}$).
  Giữ nguyên vẹn ba bước sư phạm chuẩn mực: Nhận dạng và chuẩn bị, Lời giải, Đánh giá.
- **Câu hỏi tự kiểm**: Đầy đủ 2 câu:
  - Câu hỏi tự kiểm 32.4: Khảo sát tại 4 tọa độ $x = 0, \lambda/4, \lambda/2, 3\lambda/4$ cho 4 tiêu chí cực đại, cực tiểu của mật độ năng lượng và vector Poynting tức thời.
  - Câu hỏi tự kiểm 32.5: Phân tích sự không triệt tiêu đồng thời của mật độ năng lượng theo thời gian; làm rõ năng lượng có thể bằng không tại một thời điểm tức thời xác định, nhưng không có điểm nào có năng lượng đồng nhất bằng không cho mọi thời điểm.
  Đề bài luôn hiển thị trực tiếp cho người học, phần đáp án và giải thích được gập trong thẻ `<details><summary>Xem đáp án và giải thích</summary>`.
- **Hình ảnh trích xuất**: Đầy đủ 14 hình ảnh gốc đã được trích xuất trực tiếp từ PDF bằng PyMuPDF tại `docs/vat-ly-2/bai-giang/img/young-32/`:
  - `hinh-32-17.png` (Hình 32.17: Mặt sóng tại thời điểm dt sau khi qua mặt phẳng cố định).
  - `hinh-32-18.png` (Hình 32.18: Tấm pin năng lượng mặt trời trên mái nhà).
  - `hinh-32-19.png` (Hình 32.19: Trạm phát thanh bức xạ vào bán cầu).
  - `hinh-32-20.png` (Hình 32.20: Bong bóng khí liên sao do áp suất bức xạ khoét rỗng).
  - `hinh-32-21.png` (Hình 32.21: Tấm pin năng lượng mặt trời trên vệ tinh nhân tạo).
  - `hinh-32-22.png` (Hình 32.22: Cấu trúc nút và bụng của sóng dừng điện từ tại pha thời gian bằng 3pi/4 radian).
  - `hinh-32-23.png` (Hình 32.23: Sóng dừng và đĩa xoay trong lò vi sóng).
  - `hinh-32-24.png` (Hình 32.24: Ăng-ten vòng tròn thu sóng vô tuyến trong bài toán chuyển tiếp).
  - `ung-dung-32-song-trong-chat-lieu.png` (Ảnh ứng dụng y học: Phẫu thuật não bằng laser, trích chính xác từ vùng ảnh cột phải trang PDF 1083).
  - `tom-tat-32-01.png` đến `tom-tat-32-04.png` (4 hình vẽ tổng kết thực tế của chương 32; bao gồm đầy đủ biên lề và nhãn 'Stationary plane', 'Wave front at time dt later' trong `tom-tat-32-03.png`).
  - Tệp `tom-tat-32-05.png` được bảo lưu nguyên vẹn để không vi phạm ranh giới sở hữu nhưng không được gán trùng lặp trong bài giảng.
- **Chú thích hình ảnh song ngữ (Image Annotations)**: Đã cấu hình tập tin `docs/.vitepress/physics32-theory-b-image-annotations.mjs`:
  - Chỉ chứa các cụm chữ tiếng Anh thực sự xuất hiện trong khung hình đã crop.
  - Các ảnh thực tế không chứa chữ (32.18, 32.20, 32.23, phẫu thuật laser) và hình vẽ chỉ có ký hiệu toán học (tom-tat-32-02) đều để danh sách rỗng `[]`.
  - Hình 32.19 chỉ chú thích hai nhãn danh từ tiếng Anh thực tế (`Transmitter`, `Satellite`).
  - Hình tổng kết 32.03 chứa đầy đủ hai nhãn thực tế (`Stationary plane`, `Wave front at time dt later`).

## Điểm học thuật làm rõ và kiểm chứng

1. **Sự cân bằng năng lượng điện và từ trong sóng điện từ phẳng chạy đơn hướng**: Trong chân không, hệ thức $B = E/c$ và $c = 1/\sqrt{\epsilon_0 \mu_0}$ dẫn đến $u_B = B^2/(2\mu_0) = E^2/(2\mu_0 c^2) = \frac{1}{2}\epsilon_0 E^2 = u_E$. Năng lượng của sóng phẳng chạy đơn hướng luôn được chia đều chính xác 50% cho điện trường và 50% cho từ trường tại mọi vị trí và thời điểm. Tính chất này không đúng cho sóng dừng hoặc trường chồng chập tổng quát.
2. **Hướng và tính chất không đổi chiều của vector Poynting sóng chạy**: Trong sóng hình sin phân cực thẳng chạy theo chiều dương trục $x$, dù điện trường $\vec{E}$ và từ trường $\vec{B}$ đổi chiều tuần hoàn theo thời gian, tích có hướng $\vec{E} \times \vec{B}$ luôn hướng theo chiều dương trục $x$ do $\hat{\jmath} \times \hat{k} = \hat{\imath}$ và $\cos^2(kx - \omega t) \ge 0$. Khi sóng truyền theo chiều âm trục $x$, đối số đổi thành $kx + \omega t$ đồng thời dấu tương đối giữa $\vec{E}$ và $\vec{B}$ phải đảo ngược để tích $\vec{E} \times \vec{B}$ chỉ theo chiều $-\hat{\imath}$.
3. **Mở rộng sang môi trường điện môi**: Khi sóng truyền trong môi trường điện môi tuyến tính, đồng nhất, đẳng hướng, không tán sắc và không tiêu tán, tốc độ pha của sóng là $v = 1/\sqrt{\epsilon \mu} = c/\sqrt{K K_{\mathrm{m}}}$. Mật độ năng lượng từ trường là $u_B = B^2/(2\mu)$ (tuyệt đối không viết nhầm thành $\mu B^2/2$). Với phần lớn điện môi không từ tính thông thường ($K > 1, K_{\mathrm{m}} \approx 1$), tốc độ sóng nhỏ hơn $c$; nhận định này không áp dụng vô điều kiện cho mọi môi trường dị thường hoặc có tán sắc.
4. **Bản chất áp suất bức xạ và sự khác biệt giữa hấp thụ và phản xạ**: Khi sóng điện từ bị hấp thụ hoàn toàn, nó truyền toàn bộ động lượng $p$ cho vật; khi bị phản xạ lý tưởng, chiều chuyển động của sóng đảo ngược khiến độ biến thiên động lượng của sóng là $\Delta p = -2p$, do đó động lượng truyền cho mặt phản xạ là $2p$, làm áp suất bức xạ tăng gấp đôi so với trường hợp hấp thụ hoàn toàn.
5. **Điều kiện biên và dòng mặt trên vật dẫn lý tưởng**: Điện trường tiếp tuyến bị triệt tiêu trên bề mặt kim loại dẫn điện lý tưởng nhờ dòng điện mặt dao động do sóng tới kích thích. Dòng điện mặt này không làm triệt tiêu từ trường; trái lại, nó tạo ra bụng của từ trường ngay trên bề mặt vật dẫn.
6. **Lệch pha không gian, lệch pha thời gian và cường độ bức xạ trong sóng dừng**: Trong sóng dừng, $\vec{E}$ biến thiên theo $\sin \omega t$ còn $\vec{B}$ biến thiên theo $\cos \omega t$, nên hai trường lệch pha nhau $90^\circ$ theo thời gian. Về mặt không gian, nút của trường này là bụng của trường kia. Cường độ bức xạ được định nghĩa là độ lớn của vector Poynting trung bình theo thời gian: $I = |\langle \vec{S} \rangle| = S_{\text{av}} = 0$, phản ánh thông lượng năng lượng thuần ròng bằng không. Trái lại, giá trị trung bình của độ lớn $\langle |\vec{S}| \rangle > 0$, đặc trưng cho sự trao đổi năng lượng qua lại giữa hai dạng trường trong từng bó sóng. Sóng dừng phản xạ lý tưởng không tiêu tán năng lượng thành nhiệt; tiêu tán đòi hỏi vật liệu có điện trở hoặc cơ chế hấp thụ tổn hao.
7. **Sự không triệt tiêu đồng nhất của mật độ năng lượng theo thời gian**: Tại nút điện trường $x = 0$, $u_E = 0$ ở mọi thời điểm, nhưng từ trường dao động với biên độ cực đại. Khi $\omega t = \pi/2$ ($t = T/4$), từ trường tức thời đi qua điểm không dẫn đến tổng mật độ năng lượng tức thời $u(0, T/4) = 0$. Tuy nhiên, không có điểm nào trong không gian mà năng lượng đồng nhất bằng không cho mọi thời điểm ($\min_x (\max_t u(x, t)) > 0$).

## Bằng chứng kiểm tra tự động

- Kịch bản kiểm tra số học `raw_materials/physics/verify_chapter32_theory_b.py` được lập trình kiểm tra toàn bộ 5 ví dụ, 2 câu hỏi tự kiểm, tích phân trung bình thời gian của vector Poynting, và kiểm tra phương trình sóng Maxwell:
  - Khẳng định số học Faraday trên lưới 2D $(x, t)$: Độ dư cực đại $\max |-dE_y/dx - dB_z/dt| < 5{,}7 \times 10^{-14} \implies$ Đạt (Pass).
  - Khẳng định số học Ampere trên lưới 2D $(x, t)$: Độ dư cực đại với $c = 3{,}00 \times 10^8\,\mathrm{m/s}$ đạt $< 4{,}3 \times 10^{-22} \implies$ Đạt (Pass).
  - Khẳng định phương trình sóng vi phân: Độ dư tương đối đạt $< 5{,}0 \times 10^{-16} \implies$ Đạt (Pass).
  - Khẳng định năng lượng: Xác nhận không có điểm nào có năng lượng đồng nhất triệt tiêu theo thời gian, đồng thời xác nhận năng lượng tức thời có thể bằng không tại $t = T/4$ ở nút điện trường.
  Kết quả chạy thành công 100% và lưu tại `qa/physics/chapter32/theory-b-numeric-checks.json`.
- Kiểm tra toàn bộ công thức toán hiển thị: Đều sử dụng môi trường `\begin{aligned}...\end{aligned}` với hai dấu phân cách `$$` độc lập trên dòng riêng; bẻ dòng tại các vị trí toán tử hoặc dấu bằng để đảm bảo chiều rộng không vượt quá giới hạn 27ex cho display và 38ex cho inline, triệt tiêu hoàn toàn nguy cơ xuất hiện thanh cuộn ngang (scrollbar). Đã kiểm chứng 56 khối display và 251 công thức inline, kết quả 0 vi phạm (findings: []).
- Kiểm tra số lượng nhãn phương trình: Đầy đủ 17 nhãn từ (32.23) đến (32.39), mỗi nhãn xuất hiện chính xác một lần, mỗi khối toán chỉ chứa một nhãn duy nhất.
- Kiểm tra quy tắc viết hoa sau dấu hai chấm (`:`): 100% các câu văn xuôi, nhãn hộp, đầu mục và chú thích đều tuân thủ viết hoa chữ cái đầu sau dấu hai chấm.
- Kiểm tra văn phong: Toàn bộ nội dung giữ chuẩn mực học thuật, tự nhiên, thuần Việt; loại bỏ hoàn toàn các câu tường thuật về tiến độ dịch, không bịa đặt số liệu bẫy thi cử, không dùng lối viết tự độc thoại trong lời giải.

