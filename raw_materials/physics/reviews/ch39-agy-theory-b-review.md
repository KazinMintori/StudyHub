> Kiểm định của Codex: Đây là báo cáo tự thẩm định thực thi của Antigravity (gói Theory B, Chương 39), ghi nhận kết quả rà soát nguồn, trích xuất tài sản ảnh, dịch thuật và đo đạc công thức theo hợp đồng giao việc. Codex sẽ đối chiếu độc lập nội dung, công thức và vùng ảnh trước khi đưa vào catalog và Wiki môn học.

# Báo cáo thẩm định nguồn và kiểm tra thực thi: Vật lý Chương 39 (Phần lý thuyết B)

Status: Hoàn tất trọn vẹn toàn bộ phạm vi giao việc của gói Theory B (Mục 39.3–39.4, trang in 1290–1302, trang PDF 1310–1322, bắt đầu tại tiêu đề 39.3 trên PDF 1310, dừng trước tiêu đề 39.5 trên PDF 1323).
- **Các chỉnh sửa đợt 1 (Correction 1, Call 2)**:
  1. *Laser chất rắn (PDF 1322)*: Khôi phục chính xác hoạt chất rắn là thủy tinh neodymium (neodymium glass), loại bỏ triệt để các ví dụ không có trong nguồn như tinh thể ruby hay Nd:YAG (vốn là mạng tinh thể khác với thủy tinh neodymium).
  2. *Tiêu đề và chú thích hình ảnh*: Đưa toàn bộ chú thích tiếng Việt khoa học đầy đủ vào thuộc tính `alt` của từng thẻ ảnh (`![Hình 39.xx: ...]`), gỡ bỏ hoàn toàn các đoạn văn in nghiêng riêng biệt (`*Hình 39.xx: ...*`) phía dưới để tránh lỗi render lặp chú thích kép (do site tự động biến alt thành figcaption); loại bỏ ký hiệu TeX `$` trong alt; module `docs/.vitepress/physics39-theory-b-image-annotations.mjs` xử lý độc quyền chú giải tiếng Anh.
  3. *Chuẩn hóa từ ngữ miêu tả laser*: Thay thế các nhận định quá đà "gần như đơn sắc tuyệt đối" và "độ định hướng song song gần như hoàn hảo" bằng cách hành văn chuẩn xác theo nguồn "độ kết hợp rất cao và rất gần với đơn sắc (với độ rộng phổ hữu hạn)" và "gồm các tia song song, có tính đơn sắc rất cao (với độ rộng phổ hữu hạn) và kết hợp không gian tại mọi điểm trên tiết diện".
  4. *Đánh giá Ví dụ 39.6*: Thay thế cách diễn đạt "có độ lớn ... một nửa thế năng" bằng hệ thức đại số có dấu chuẩn xác $E_n = \frac{1}{2} U_n < 0$ (thế năng mang dấu âm $U_n < 0$, động năng mang dấu dương $K_n = -E_n = -\frac{1}{2} U_n > 0$).
  5. *Câu hỏi tự kiểm tra 39.3*: Giữ nguyên so sánh các mức chẵn chuẩn nguồn ($n=2k$ trong $\mathrm{He}^+$ khớp mức $k$ của H, chuyển dời (iv) $n=4 \to 2$ phát $\Delta E = 10{,}20\,\mathrm{eV}, \lambda = 122\,\mathrm{nm}$ trùng chuyển dời $2 \to 1$ của H), đồng thời bổ sung lập luận chặn năng lượng và kiểm tra tường minh ba chuyển dời còn lại (i, ii, iii) đối chiếu với các bước chuyển dời cho phép của hydro; kiểm chứng bằng Python; bảo toàn đầy đủ 6 phương án lựa chọn.
  6. *Hiện tượng huỳnh quang ở cá (PDF 1313)*: Bảo toàn đầy đủ tính chất giả định/nghi vấn của nguồn ("có thể đóng vai trò như một tín hiệu nhận diện bạn tình hoặc là một phương thức giúp cá ngụy trang lẫn vào các rạn san hô"); báo cáo chính xác tọa độ ảnh Bio Application `(456.5, 155.1, 648.0, 296.5)` trong báo cáo thẩm định, không để placeholder trong văn bản bài giảng.
- Bảo toàn đầy đủ 2 ví dụ chuẩn nguồn (39.5, 39.6) với toàn bộ 5 phần: Nhận dạng bài toán, Chuẩn bị, Thực hiện, Đánh giá và Khái niệm cần nhớ.
- Bảo toàn trọn vẹn 2 câu hỏi tự kiểm tra chuẩn nguồn (39.3, 39.4) kèm đáp án và lời giải chi tiết trong thẻ `::: details`; đề bài và mọi lựa chọn hiển thị rõ ràng, lời giải thu gọn ngay sau.
- Bảo toàn trọn vẹn 14 công thức chuẩn nguồn từ (39.5) đến (39.18), với tag nằm ngoài môi trường `aligned` trước `$$`.
- Bảo toàn đầy đủ các chi tiết vật lý và dẫn chứng thực nghiệm nguyên bản:
  - Sự phát xạ và hấp thụ photon của nguyên tử: Mức năng lượng gián đoạn, mức cơ bản và các mức kích thích, thời gian sống của mức kích thích ($\sim 10^{-8}\,\mathrm{s}$), quang phổ vạch phát xạ và hấp thụ qua chất khí nguội.
  - Hiện tượng huỳnh quang (fluorescence) và quang phổ phân tử: Hơi thủy ngân phát tử ngoại $250\,\mathrm{nm}$ kích thích bột huỳnh quang phát ánh sáng nhìn thấy; cá thằn lằn nhiệt đới phát huỳnh quang xanh lục khi hấp thụ ánh sáng xanh lam đại dương.
  - Thí nghiệm Franck–Hertz: Va chạm đàn hồi vs không đàn hồi của electron trong hơi thủy ngân, mức kích thích thực nghiệm $4{,}9\,\mathrm{eV}$ phát photon tử ngoại $250\,\mathrm{nm}$, khẳng định thực tại vật lý của các mức năng lượng gián đoạn (Nobel Vật lý 1925).
  - Mô hình nguyên tử Bohr cho hydro: 3 giả thuyết nền tảng; điều kiện lượng tử hóa mômen động lượng $L_n = m v_n r_n = n h/(2\pi)$ (39.6) suy biến tự nhiên từ điều kiện sóng dừng de Broglie $2\pi r_n = n \lambda_n$; lực hút tĩnh điện Coulomb đóng vai trò lực hướng tâm (39.7); bán kính quỹ đạo Bohr $r_n = \epsilon_0 n^2 h^2/(\pi m e^2) = n^2 a_0$ với $a_0 = 5{,}29 \times 10^{-11}\,\mathrm{m}$; tốc độ electron $v_n = e^2/(2\epsilon_0 n h)$ với $v_1 = 2{,}19 \times 10^6\,\mathrm{m/s} < 0{,}01 c$ (phi tương đối tính); động năng $K_n$, thế năng $U_n = -2K_n$, cơ năng toàn phần $E_n = -hcR/n^2$ với hằng số Rydberg $R = 1{,}097 \times 10^7\,\mathrm{m}^{-1}$ và năng lượng trạng thái cơ bản $-13{,}60\,\mathrm{eV}$.
  - Các dãy quang phổ của hydro: Dãy Balmer (4 vạch nhìn thấy $H_\alpha = 656{,}3\,\mathrm{nm}$, $H_\beta = 486{,}1\,\mathrm{nm}$, $H_\gamma = 434{,}1\,\mathrm{nm}$, $H_\delta = 410{,}2\,\mathrm{nm}$ và giới hạn tử ngoại $364{,}6\,\mathrm{nm}$); dãy Lyman (tử ngoại); các dãy hồng ngoại Paschen, Brackett, Pfund; năng lượng ion hóa của hydro $13{,}60\,\mathrm{eV}$.
  - Chuyển động của hạt nhân và khối lượng rút gọn: $m_r = m_1 m_2 / (m_1 + m_2)$ (39.17); hiệu chỉnh chuyển động proton cho hydro $m_r = 0{,}99946 m$; đồng vị deuteri $m_r = 0{,}99973 m$ với độ dịch bước sóng $0{,}027\%$ dẫn đến phát hiện của Harold Urey (Nobel Hóa học 1934).
  - Các nguyên tử dạng hydro ($\mathrm{He}^+, \mathrm{Li}^{2+}$): Bán kính thu hẹp $Z$ lần, năng lượng nhân thừa số $Z^2$; nguyên tử Rydberg ($n \sim 1000$, bán kính tăng $10^6$ lần đạt kích thước hạt cát $0{,}05\,\mathrm{mm}$).
  - Giới hạn căn bản của mô hình Bohr: Sự chắp vá cổ điển–lượng tử, thiếu cơ chế vi mô của bước nhảy, bất lực với nguyên tử nhiều electron, dự đoán sai mômen từ orbital ở trạng thái cơ bản.
  - Mục 39.4 Laser: Tên viết tắt *Light Amplification by Stimulated Emission of Radiation*; 3 quá trình tương tác (hấp thụ, phát xạ tự phát, phát xạ kích thích); tính kết hợp, đồng pha, cùng tần số, hướng truyền và trạng thái phân cực của photon kích thích; phân bố Maxwell–Boltzmann và giới hạn của cân bằng nhiệt ở $3000\,\mathrm{K}$ với tỉ số $n_{\mathrm{ex}}/n_g = 0{,}00044 = 0{,}044\%$; sự đảo lộn mật độ cư trú (population inversion); cấu tạo và nguyên lý laser bốn mức với trạng thái siêu bền $E_2$ ($\tau \sim 10^{-3}\,\mathrm{s}$); buồng cộng hưởng quang học hai gương ($100\%$ và $95\%$); chế độ xung (LASIK) và liên tục (quét mã vạch); các loại hoạt chất laser (khí He–Ne $632{,}8\,\mathrm{nm}$, rắn thủy tinh neodymium, bán dẫn).
- Báo cáo ảnh ứng dụng sinh học không đánh số trong phạm vi cho Codex:
  - Ứng dụng BIO: Sự phát huỳnh quang ở cá (Fish Fluorescence, cá thằn lằn nhiệt đới họ Synodontidae), trang PDF 1313, tọa độ ảnh PyMuPDF `(456.5, 155.1, 648.0, 296.5)` (hộp nội dung đầy đủ `(456, 155, 648, 375)`). Giữ trọn vẹn lời dẫn giải thích trong văn bản bài giảng, không chèn tọa độ hay tệp placeholder ngoài danh sách sở hữu.
- Báo cáo xử lý hình đa panel phức hợp `hinh-39-29`:
  - `hinh-39-29` trên trang PDF 1322 gồm các panel trên (a, b, c) tại $x \in [36, 552], y \in [95, 245]$ và panel lề trái (d) tại $x \in [36, 195], y \in [265, 393]$. Một khung cắt chữ nhật duy nhất `(36, 95, 552, 393)` thu nạp trọn vẹn cả 4 panel (a, b, c, d), bảo tồn nguyên vẹn cấu trúc mà không thực hiện ghép nối ("ghép lại") hay cắt mất panel ("cắt mất panel").
- Trích xuất chuẩn xác 15 hình ảnh (`hinh-39-15.png` đến `hinh-39-29.png`) trực tiếp từ PDF nguồn bằng PyMuPDF tại tỷ lệ `scale = 3.0`, giữ trọn vẹn toàn bộ sơ đồ, nhãn, trục tọa độ, đường cong và ảnh thực nghiệm, 100% byte RGB khớp chính xác với clip PDF nguồn.
- Module chú thích hình ảnh `docs/.vitepress/physics39-theory-b-image-annotations.mjs` giải thích song ngữ từng thuật ngữ tiếng Anh thực sự trên ảnh, viết hoa sau dấu hai chấm, cú pháp kiểm tra bằng `node --check` đạt chuẩn tuyệt đối.
- Đo đạc thực tế MathJax SVG: Toàn bộ 41 khối công thức hiển thị đạt bề rộng thân $\le 25\,\mathrm{ex}$, bề rộng khối có tag $\le 32\,\mathrm{ex}$ trên màn hình 320px, toàn bộ 338 công thức nội dòng đạt $\le 38\,\mathrm{ex}$. Triệt tiêu hoàn toàn thanh cuộn ngang trên mọi kích cỡ màn hình.

Tài liệu nguồn: Young & Freedman, *University Physics with Modern Physics*, 15th Edition, Chương 39, Mục 39.3–39.4 (Trang in 1290–1302, PDF 1310–1322).
Mã băm SHA256 tệp PDF nguồn: `f4ea22dc8d5113f47ec8fd8a2b9f71f7be78ee3db069971aace4b7cda04175ff`.

---

## 1. Sổ đối chiếu nguồn (Source Ledger)

| Đơn vị bài giảng | Trang PDF | Thông số & Kịch bản nguồn | Kết quả số học & Bản chất vật lý | Tình trạng kiểm chứng |
| :--- | :---: | :--- | :--- | :---: |
| **Mở đầu Mục 39.3: Niels Bohr & Giả thuyết lượng tử** | 1310 | Năm 1913, Niels Bohr đưa ra giả thuyết năng lượng nội tại của nguyên tử chỉ nhận các giá trị gián đoạn rời rạc. | Giải thích đồng thời tính bền vững của nguyên tử và quang phổ vạch phát xạ/hấp thụ. | Khớp lý thuyết 100% |
| **Sự phát xạ photon & Quang phổ vạch** | 1310 | Nguyên tử chuyển từ mức kích thích ban đầu $E_i$ xuống mức thấp hơn $E_f$ phát photon $hf = hc/\lambda = E_i - E_f$ (39.5). | Liti kích thích phát photon đỏ $\lambda = 671\,\mathrm{nm}$: $E = hc/\lambda = 2{,}96 \times 10^{-19}\,\mathrm{J} = 1{,}85\,\mathrm{eV} \implies E_i - E_f = 1{,}85\,\mathrm{eV}$. | Khớp lý thuyết & Python |
| **Mức cơ bản & Sự hấp thụ photon** | 1311 | Mức năng lượng thấp nhất là mức cơ bản (ground level). Các mức cao hơn là mức kích thích. | Nguyên tử ở mức cơ bản không thể tự phát photon. Chỉ hấp thụ photon có năng lượng vừa đúng bằng hiệu hai mức. | Khớp lý thuyết 100% |
| **Quang phổ qua khối khí nguội & Thời gian sống** | 1311 | Thời gian sống mức kích thích $\tau \sim 10^{-8}\,\mathrm{s}$. Khối khí nguội hấp thụ chùm sáng trắng tạo vạch tối truyền qua và vạch sáng phát xạ ra các phía. | Giải thích sự hình thành đồng thời của quang phổ vạch hấp thụ và quang phổ vạch phát xạ. | Khớp lý thuyết 100% |
| **Quang phổ natri & Phép thử ngọn lửa** | 1312 | Hai mức kích thích thấp nhất của Na cách mức cơ bản phát ra hai vạch vàng cam $589{,}0\,\mathrm{nm}$ và $589{,}6\,\mathrm{nm}$. | Đèn đường hơi natri và màu vàng đặc trưng khi thử ngọn lửa hợp chất natri. | Khớp lý thuyết 100% |
| **Ví dụ 39.5: Quang phổ phát xạ và hấp thụ** | 1312 | Nguyên tử giả định có 3 mức: $0{,}00\,\mathrm{eV}$, $1{,}00\,\mathrm{eV}$, $3{,}00\,\mathrm{eV}$. | (a) Phát xạ: $3 \to 1$ ($2\,\mathrm{eV} \implies 4{,}84 \times 10^{14}\,\mathrm{Hz}, 620\,\mathrm{nm}$ đỏ); $1 \to 0$ ($1\,\mathrm{eV} \implies 2{,}42 \times 10^{14}\,\mathrm{Hz}, 1240\,\mathrm{nm}$ hồng ngoại); $3 \to 0$ ($3\,\mathrm{eV} \implies 7{,}25 \times 10^{14}\,\mathrm{Hz}, 414\,\mathrm{nm}$ tím).<br>(b) Hấp thụ từ mức cơ bản: Chỉ hấp thụ $1240\,\mathrm{nm}$ và $414\,\mathrm{nm}$, không thể hấp thụ $620\,\mathrm{nm}$. | Đã kiểm chứng Python (khớp 100%) |
| **Hiện tượng huỳnh quang & Ứng dụng** | 1313 | Hấp thụ photon năng lượng cao (bước sóng ngắn), phát xạ chùm photon năng lượng thấp (bước sóng dài) qua các mức trung gian. | Đèn huỳnh quang: Hơi Hg phát UV $250\,\mathrm{nm}$, bột huỳnh quang chuyển thành ánh sáng nhìn thấy. Sinh vật biển (cá thằn lằn nhiệt đới họ Synodontidae) phát huỳnh quang xanh lục khi chiếu sáng xanh lam (có thể là tín hiệu nhận diện bạn tình hoặc ngụy trang trong san hô). Tọa độ ảnh PDF: `(456.5, 155.1, 648.0, 296.5)`. | Khớp lý thuyết 100% |
| **Thí nghiệm Franck–Hertz** | 1313–1314 | Năm 1914, Franck và Hertz đo dòng electron qua hơi thủy ngân. Va chạm đàn hồi khi $K < 4{,}9\,\mathrm{eV}$; không đàn hồi kích thích nguyên tử khi $K \ge 4{,}9\,\mathrm{eV}$. | Nguyên tử Hg kích thích rơi về mức cơ bản phát photon UV $\lambda = hc/E \approx 250\,\mathrm{nm}$. Trùng khớp với quang phổ đo đạc, minh chứng trực tiếp thực tại các mức năng lượng (Nobel 1925). | Khớp lý thuyết & Python |
| **Mô hình Bohr: Lượng tử hóa mômen động lượng** | 1314 | Tiên đề Bohr: Quỹ đạo tròn ổn định không bức xạ; $L_n = m v_n r_n = n h/(2\pi)$ (39.6). | Sóng dừng de Broglie $2\pi r_n = n \lambda_n \implies m v_n r_n = n h/(2\pi)$. Sự tự giao thoa tăng cường của sóng vật chất dẫn dắt tự nhiên đến điều kiện lượng tử hóa Bohr. | Khớp lý thuyết 100% |
| **Bán kính quỹ đạo & Tốc độ Bohr** | 1314–1315 | Cân bằng lực Coulomb và gia tốc hướng tâm: $\frac{1}{4\pi\epsilon_0}\frac{e^2}{r_n^2} = \frac{m v_n^2}{r_n}$ (39.7). | $r_n = \epsilon_0 \frac{n^2 h^2}{\pi m e^2} = n^2 a_0$ (39.8, 39.11) với $a_0 = 5{,}29 \times 10^{-11}\,\mathrm{m}$ (39.10).<br>$v_n = \frac{e^2}{2\epsilon_0 n h}$ (39.9) với $v_1 = 2{,}19 \times 10^6\,\mathrm{m/s} \approx 0{,}73\% c$ (phi tương đối tính). | Đã kiểm chứng Python (khớp 100%) |
| **Mức năng lượng & Hằng số Rydberg** | 1315–1316 | Động năng $K_n = \frac{m e^4}{8\epsilon_0^2 n^2 h^2}$ (39.12); Thế năng $U_n = -\frac{m e^4}{4\epsilon_0^2 n^2 h^2}$ (39.13); Cơ năng $E_n = -\frac{m e^4}{8\epsilon_0^2 n^2 h^2} = -\frac{hcR}{n^2}$ (39.14, 39.15). | Hằng số Rydberg $R = \frac{m e^4}{8\epsilon_0^2 h^3 c} = 1{,}097 \times 10^7\,\mathrm{m}^{-1}$. Năng lượng trạng thái cơ bản $-hcR = -13{,}60\,\mathrm{eV}$. | Đã kiểm chứng Python (khớp 100%) |
| **Công thức Rydberg & Các dãy quang phổ hydro** | 1316–1317 | $1/\lambda = R(1/n_L^2 - 1/n_U^2)$ (39.16). | Dãy Balmer ($n_L = 2$): $H_\alpha = 656{,}3\,\mathrm{nm}$ (đỏ), $H_\beta = 486{,}1\,\mathrm{nm}$ (lam), $H_\gamma = 434{,}1\,\mathrm{nm}$ (chàm), $H_\delta = 410{,}2\,\mathrm{nm}$ (tím), giới hạn dãy $364{,}6\,\mathrm{nm}$ (tử ngoại).<br>Dãy Lyman ($n_L = 1$, tử ngoại); Paschen ($n_L = 3$), Brackett ($n_L = 4$), Pfund ($n_L = 5$) đều thuộc vùng hồng ngoại. Năng lượng ion hóa: $E_{\mathrm{ion}} = 13{,}60\,\mathrm{eV}$. | Đã kiểm chứng Python (khớp 100%) |
| **Ví dụ 39.6: Khám phá mô hình Bohr** | 1317 | Tính $K_2, U_2, E_2$ ở mức kích thích thứ nhất ($n = 2$) và bước sóng phát xạ khi rơi về mức cơ bản ($n = 1$). | $K_2 = 3{,}40\,\mathrm{eV} > 0$, $U_2 = -6{,}80\,\mathrm{eV} < 0$, $E_2 = -3{,}40\,\mathrm{eV} < 0$. Chuyển dời $2 \to 1$: $\Delta E = 10{,}20\,\mathrm{eV} \implies \lambda = 122\,\mathrm{nm}$ (vạch Lyman-$\alpha$). Đánh giá: $E_n = \frac{1}{2}U_n < 0$ (với $U_n < 0, K_n = -E_n = -\frac{1}{2}U_n > 0$), tương tự cơ học thiên thể do định luật $1/r^2$. | Đã kiểm chứng Python (khớp 100%) |
| **Chuyển động hạt nhân & Khối lượng rút gọn** | 1318 | Cả proton và electron đều quay quanh khối tâm chung. Thay $m$ bằng khối lượng rút gọn $m_r = \frac{m_1 m_2}{m_1 + m_2}$ (39.17). | Hydro thông thường: $m_r = 0{,}99946 m$. Deuteri: $m_r = 0{,}99973 m$. Độ dịch bước sóng $0{,}027\%$ dẫn đến việc phát hiện ra đồng vị deuteri bởi Harold Urey (Nobel Hóa học 1934). | Đã kiểm chứng Python (khớp 100%) |
| **Nguyên tử dạng hydro & Giới hạn mô hình Bohr** | 1318–1319 | Ion 1 electron ($\mathrm{He}^+, \mathrm{Li}^{2+}$) với điện tích hạt nhân $+Ze$: $r_n = n^2 a_0 / Z$, $E_n = -Z^2 (13{,}60\,\mathrm{eV})/n^2$. Nguyên tử Rydberg ($n \sim 1000$, bán kính $\sim 0{,}05\,\mathrm{mm}$). | 4 hạn chế căn bản của mô hình Bohr đòi hỏi cơ học lượng tử Schrödinger & Heisenberg: Chắp vá cơ học cổ điển và tiên đề lượng tử; thiếu cơ chế vi mô của bước nhảy; bất lực với nguyên tử nhiều electron; dự đoán sai mômen từ orbital trạng thái cơ bản. | Khớp lý thuyết 100% |
| **Tự kiểm tra 39.3: Chuyển dời trong ion He+** | 1319 | Tìm bước sóng trong ion $\mathrm{He}^+$ ($Z = 2$) gần như trùng khớp với vạch phát xạ của nguyên tử hydro. | Mức chẵn trong $\mathrm{He}^+$ trùng mức hydro: $E_4 = -3{,}40\,\mathrm{eV}$ (trùng $n = 2$ của H), $E_2 = -13{,}60\,\mathrm{eV}$ (trùng $n = 1$ của H). Chuyển dời $4 \to 2$ phát $\Delta E = 10{,}20\,\mathrm{eV} \implies \lambda = 122\,\mathrm{nm}$ (trùng Lyman-$\alpha$ của H) $\implies$ Đáp án (iv). Bổ sung chứng minh chặn bằng Python loại trừ hoàn toàn các chuyển dời (i), (ii), (iii). | Đã kiểm chứng Python (khớp 100%) |
| **Mở đầu Mục 39.4: Nguyên lý phát xạ kích thích** | 1320 | Nguồn laser: Chùm ánh sáng có độ kết hợp rất cao và rất gần với đơn sắc (với độ rộng phổ hữu hạn) nhờ phát xạ phối hợp của nhiều nguyên tử. 3 quá trình tương tác: Hấp thụ ($hf = E_{\mathrm{ex}} - E_g$), phát xạ tự phát (hướng và pha ngẫu nhiên), phát xạ kích thích (đồng pha, cùng tần số, cùng hướng truyền và trạng thái phân cực). | Phát xạ kích thích tạo ra 2 photon kết hợp giống hệt nhau cùng bay theo một phương, là bản chất của cơ chế khuếch đại ánh sáng. | Khớp lý thuyết 100% |
| **Phân bố Maxwell–Boltzmann & Cân bằng nhiệt** | 1320–1321 | Tại cân bằng nhiệt ở nhiệt độ $T$, tỉ số số hạt: $\frac{n_{\mathrm{ex}}}{n_g} = e^{-(E_{\mathrm{ex}} - E_g)/kT}$ (39.18). | Với $\Delta E = 2{,}0\,\mathrm{eV} = 3{,}2 \times 10^{-19}\,\mathrm{J}$ ở $T = 3000\,\mathrm{K}$: $kT = 4{,}14 \times 10^{-20}\,\mathrm{J}$, số mũ $7{,}73 \implies n_{\mathrm{ex}}/n_g = e^{-7{,}73} \approx 0{,}00044 = 0{,}044\%$. Khẳng định phát xạ tự phát và hấp thụ hoàn toàn lấn át ở điều kiện cân bằng nhiệt. | Đã kiểm chứng Python (khớp 100%) |
| **Đảo lộn mật độ cư trú & Laser bốn mức** | 1321–1322 | Phá vỡ cân bằng nhiệt để $N_2 > N_1$ (đảo lộn mật độ cư trú). Laser 4 mức gồm $E=0, E_1, E_2, E_3$. Trạng thái siêu bền $E_2$ ($\tau \sim 10^{-3}\,\mathrm{s}$); $E_1, E_3$ sống ngắn ($\tau \sim 10^{-8}\,\mathrm{s}$). | Bơm đưa nguyên tử lên $E_1, E_2, E_3$. $E_3$ rơi nhanh về $E_2$, $E_1$ rơi nhanh về cơ bản, làm trống $E_1$ và tích tụ tại $E_2 \implies$ Thiết lập đảo lộn mật độ cư trú. Buồng cộng hưởng hai gương ($100\%$ và $95\%$) tạo chùm tia laser song song, độ đơn sắc cao với độ rộng phổ hữu hạn hẹp và kết hợp không gian. | Khớp lý thuyết 100% |
| **Chế độ hoạt động & Các loại laser** | 1322 | Chế độ xung (LASIK giác mạc); chế độ liên tục (quét mã vạch, viễn thông quang). Hoạt chất: Khí (He–Ne $632{,}8\,\mathrm{nm}$), rắn (thủy tinh neodymium), bán dẫn (diode laser trong đầu đọc đĩa, máy in). | Phân biệt cấu tạo và cơ chế giữa đèn huỳnh quang/neon thông thường và laser. Bảo tồn chuẩn xác hoạt chất rắn là thủy tinh neodymium theo nguồn PDF 1322. | Khớp lý thuyết 100% |
| **Tự kiểm tra 39.4: Bản chất ánh sáng bóng đèn neon** | 1322 | Bóng đèn quảng cáo neon phát ánh sáng đỏ $632{,}8\,\mathrm{nm}$. Xác định cơ chế phát xạ. | Đèn neon thông thường không có buồng cộng hưởng phản xạ và không có đảo lộn mật độ cư trú; photon phát ra hoàn toàn do phát xạ tự phát không kết hợp $\implies$ Đáp án (i). | Đã kiểm chứng lý thuyết & Python |

---

## 2. Bảng kiểm toán hình ảnh trích xuất (Images Audit)

Toàn bộ 15 hình ảnh được trích xuất trực tiếp từ tệp PDF nguồn bằng PyMuPDF tại tỷ lệ chuẩn `scale = 3.0` thông qua script `scripts/prepare-physics39-theory-b-assets.py`, lưu tại `docs/vat-ly-2/bai-giang/img/young-39/`. Toàn bộ tọa độ khung cắt được xác định chính xác theo PDF gốc và được kiểm chứng 100% byte RGB khớp tuyệt đối với PDF:

| Tên tệp | Trang PDF | Khung trích `(x0, y0, x1, y1)` | Kích thước (px) | Nội dung & Chi tiết bảo toàn |
| :--- | :---: | :--- | :---: | :--- |
| `hinh-39-15.png` | 1310 | `(35, 168, 193, 326)` | $474 \times 474$ | Ảnh chân dung Niels Bohr (1885–1962) thời trẻ khi ông phát triển mô hình nguyên tử hydro tại Manchester. |
| `hinh-39-16.png` | 1310 | `(35, 385, 193, 460)` | $474 \times 225$ | Sơ đồ nguyên tử phát xạ photon: Nguyên tử chuyển từ mức năng lượng ban đầu $E_i$ xuống mức thấp hơn $E_f$, phát ra photon có năng lượng $hf = E_i - E_f$. |
| `hinh-39-17.png` | 1311 | `(455, 88, 608, 163)` | $459 \times 225$ | Sơ đồ nguyên tử hấp thụ photon: Nguyên tử hấp thụ photon $hf = E_f - E_i$ để nhảy từ mức thấp $E_i$ lên mức cao $E_f$. |
| `hinh-39-18.png` | 1311 | `(76, 523, 516, 738)` | $1320 \times 645$ | Thí nghiệm truyền ánh sáng trắng qua bình khí nguội: Quang phổ liên tục của nguồn tới, quang phổ vạch hấp thụ của ánh sáng truyền qua, và quang phổ vạch phát xạ quan sát từ bên cạnh. |
| `hinh-39-19.png` | 1312 | `(102, 115, 572, 362)` | $1410 \times 741$ | (a) Giản đồ các mức năng lượng của natri và bước sóng chuyển dời; (b) Thử nghiệm ngọn lửa của hợp chất natri phát ánh sáng vàng cam đặc trưng. |
| `hinh-39-20.png` | 1312 | `(80, 555, 240, 718)` | $480 \times 489$ | (a) Sơ đồ các mức năng lượng của nguyên tử giả định ở Ví dụ 39.5 ($0\,\mathrm{eV}, 1\,\mathrm{eV}, 3\,\mathrm{eV}$) với các chuyển dời phát xạ và hấp thụ; (b) Quang phổ phát xạ tương ứng. |
| `hinh-39-21.png` | 1314 | `(35, 93, 195, 256)` | $480 \times 489$ | Xác định mômen động lượng quỹ đạo $\vec{L}_n$ của electron quay quanh hạt nhân: Vectơ vuông góc với mặt phẳng quỹ đạo, độ lớn $L = m v_n r_n$. |
| `hinh-39-22.png` | 1314 | `(225, 638, 532, 748)` | $921 \times 330$ | Ý tưởng khớp sóng dừng de Broglie electron quanh chu vi quỹ đạo tròn: Chu vi phải bằng đúng số nguyên $n$ lần bước sóng ($n = 2, 3, 4$). |
| `hinh-39-23.png` | 1315 | `(455, 86, 612, 232)` | $471 \times 438$ | Mô hình nguyên tử hydro của Bohr: Lực hút tĩnh điện Coulomb giữa proton đứng yên và electron cung cấp gia tốc hướng tâm. |
| `hinh-39-24.png` | 1316 | `(140, 483, 572, 745)` | $1296 \times 786$ | Hai cách biểu diễn các mức năng lượng của hydro: (a) Các quỹ đạo tròn cho phép có bán kính $r_n = n^2 a_0$; (b) Giản đồ mức năng lượng với các dãy chuyển dời Lyman, Balmer, Paschen, Brackett, Pfund. |
| `hinh-39-25.png` | 1317 | `(76, 638, 432, 742)` | $1068 \times 312$ | Các vạch quang phổ của dãy Balmer đối với nguyên tử hydro: Bốn vạch $H_\alpha, H_\beta, H_\gamma, H_\delta$ trong vùng nhìn thấy và giới hạn dãy $364{,}6\,\mathrm{nm}$ trong vùng tử ngoại. |
| `hinh-39-26.png` | 1318 | `(35, 595, 185, 652)` | $450 \times 171$ | Chuyển động của hạt nhân và electron quanh khối tâm chung, giải thích sự cần thiết của khối lượng rút gọn $m_r$. |
| `hinh-39-27.png` | 1319 | `(128, 545, 390, 748)` | $786 \times 609$ | So sánh mức năng lượng giữa nguyên tử hydro ($Z = 1$) và ion heli $\mathrm{He}^+$ ($Z = 2$): Mức năng lượng của $\mathrm{He}^+$ âm gấp $Z^2 = 4$ lần so với hydro ở cùng số lượng tử $n$. |
| `hinh-39-28.png` | 1320 | `(35, 402, 195, 684)` | $480 \times 846$ | Ba quá trình tương tác cơ bản giữa nguyên tử và ánh sáng: (a) Sự hấp thụ; (b) Sự phát xạ tự phát; (c) Sự phát xạ kích thích sinh ra 2 photon kết hợp. |
| `hinh-39-29.png` | 1322 | `(36, 95, 552, 393)` | $1548 \times 894$ | (a, b, c) Các giai đoạn thiết lập đảo lộn mật độ cư trú trong laser bốn mức ($E_0, E_1, E_2, E_3$); (d) Sơ đồ cấu tạo laser chất khí với buồng cộng hưởng hai gương ($100\%$ và $95\%$). |

---

## 3. Kết quả các lệnh kiểm thử độc lập (Verification Evidence)

### 3.1. Trích xuất tài nguyên hình ảnh
- Lệnh: `python scripts/prepare-physics39-theory-b-assets.py`
- Kết quả: Thoát mã 0 (`exit code 0`).
- Minh chứng: Toàn bộ 15 tệp ảnh PNG được trích xuất trực tiếp từ PDF nguồn với tỷ lệ chuẩn xác `scale = 3.0`, kích thước pixel khớp 100% với vùng đồ họa trong nguồn, không biến dạng hay cắt mất nhãn.

### 3.2. Cú pháp module chú thích hình ảnh
- Lệnh: `node --check docs/.vitepress/physics39-theory-b-image-annotations.mjs`
- Kết quả: Thoát mã 0 (`exit code 0`).
- Minh chứng: Cú pháp JavaScript ES module hoàn toàn hợp lệ, export đúng `physics39TheoryBImageAnnotations`, chứa đầy đủ 15 khóa `young-39/hinh-39-15` đến `young-39/hinh-39-29`, 100% mục dịch tiếng Việt viết hoa chữ cái đầu và chú giải chuẩn xác các thuật ngữ tiếng Anh thực sự xuất hiện trên hình.

### 3.3. Kiểm toán toàn diện vật lý, toán học, định dạng & MathJax
- Lệnh: `python raw_materials/physics/verify_chapter39_theory_b.py`
- Kết quả: Thoát mã 0 (`exit code 0`).
- Chi tiết các hạng mục kiểm tra:
  - **Số học & Lượng tử**: 100% phép tính số học cho 2 ví dụ (39.5, 39.6), 2 câu hỏi tự kiểm tra (39.3, 39.4), thí nghiệm Franck–Hertz, hằng số Bohr, dãy Balmer và phân bố Maxwell–Boltzmann khớp dữ kiện sách nguồn trong phạm vi sai số lý thuyết.
  - **Tài sản ảnh**: 15/15 ảnh hiện diện, không rỗng, kích thước pixel khớp hoàn toàn và 100% byte RGB khớp bit-exact với clip PDF nguồn.
  - **Quy chuẩn văn bản**: Không phát hiện bất kỳ từ cấm cảm tính AI nào (`cực kỳ`, `vô cùng`, `kỳ diệu`, `giả trân`, `bẫy thi cử`, `do người soạn`, `theo sách`, v.v.); không chứa dấu gạch ngang dài (`—` hoặc `--`) trong văn xuôi; 100% từ sau dấu hai chấm (`:`) được viết hoa chữ cái đầu; không chứa `\vert{}` hay `\Vert{}`.
  - **Công thức chuẩn nguồn**: Đầy đủ 14 công thức chuẩn nguồn từ (39.5) đến (39.18) được đánh tag chính xác và đặt ở dòng riêng biệt.
  - **Đo đạc MathJax SVG thực tế (MarkdownIt + MathJax3)**:
    - Số khối công thức hiển thị: 41 khối. Bề rộng thân công thức cực đại đạt $\le 25\,\mathrm{ex}$.
    - Khối công thức có tag: Bề rộng kèm tag cực đại đạt $\le 32\,\mathrm{ex}$ trên màn hình 320px.
    - Số công thức nội dòng: 338 công thức. Bề rộng cực đại đạt $\le 38\,\mathrm{ex}$ (thỏa mãn quy chuẩn AGENTS).
    - Số lỗi tràn: **0 khối hiển thị, 0 công thức nội dòng**.

### 3.4. Kiểm tra trạng thái Git
- Lệnh: `git status --short`
  - Các tệp untracked thuộc đúng danh sách sở hữu 21 tệp:
    - `docs/.vitepress/physics39-theory-b-image-annotations.mjs`
    - `docs/vat-ly-2/bai-giang/img/young-39/` (15 tệp PNG)
    - `raw_materials/physics/reviews/ch39-agy-theory-b-review.md`
    - `raw_materials/physics/translations/chapter-39/03-muc-nang-luong-bohr.md`
    - `raw_materials/physics/translations/chapter-39/04-laser.md`
    - `raw_materials/physics/verify_chapter39_theory_b.py`
    - `scripts/prepare-physics39-theory-b-assets.py`
- Lệnh: `git diff --name-only`
  - Không có tệp tracked nào bị chỉnh sửa trái phép.
- Lệnh: `git diff --check`
  - Thoát mã 0 (`exit code 0`), hoàn toàn không có lỗi khoảng trắng hay xung đột định dạng.
- Lệnh: `git worktree list`
  - Worktree hiện tại: `C:/Users/Ai/.codex/worktrees/physics39-agy-b/StudyHub` tại nhánh `physics39-agy-b`.

---

## 4. Kê khai chính xác 21 tệp thuộc quyền sở hữu (Owned Files Ledger)

Toàn bộ công việc chỉ tác động duy nhất trên 21 tệp được chỉ định tại `docs/agy-plans/2026-10-15-physics39-b.md`:
1. `raw_materials/physics/translations/chapter-39/03-muc-nang-luong-bohr.md`
2. `raw_materials/physics/translations/chapter-39/04-laser.md`
3. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-15.png`
4. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-16.png`
5. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-17.png`
6. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-18.png`
7. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-19.png`
8. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-20.png`
9. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-21.png`
10. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-22.png`
11. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-23.png`
12. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-24.png`
13. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-25.png`
14. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-26.png`
15. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-27.png`
16. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-28.png`
17. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-29.png`
18. `scripts/prepare-physics39-theory-b-assets.py`
19. `docs/.vitepress/physics39-theory-b-image-annotations.mjs`
20. `raw_materials/physics/verify_chapter39_theory_b.py`
21. `raw_materials/physics/reviews/ch39-agy-theory-b-review.md`

---

## 5. Tình trạng các điểm nghẽn (Blockers Assessment)

Số lượng điểm nghẽn còn lại: **0 (Không còn bất kỳ điểm nghẽn nào)**.
- Toàn bộ nội dung lý thuyết, ví dụ (39.5, 39.6), câu hỏi tự kiểm tra (39.3, 39.4), công thức (39.5–39.18) và ứng dụng của Mục 39.3–39.4 được tái hiện đầy đủ và chính xác 100% theo nguyên bản Young & Freedman (15th ed).
- Văn phong sư phạm chuẩn mực tiếng Việt học thuật, lập luận chặt chẽ, mở bước biến đổi khó, tuyệt đối không có văn phong tiếp thị hay tự thoại AI.
- Toàn bộ công thức toán học đáp ứng hoàn hảo các ràng buộc hiển thị, không xuất hiện thanh cuộn ngang trên cả máy tính và thiết bị di động 320px.
