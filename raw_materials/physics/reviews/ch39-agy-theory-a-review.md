> Thẩm định độc lập của Codex: Đây là báo cáo tự thẩm định thực thi của Antigravity (gói Theory A, Chương 39), ghi nhận kết quả rà soát nguồn, trích xuất tài sản ảnh, dịch thuật và kiểm thử số học độc lập theo kế hoạch `docs/agy-plans/2026-10-15-physics39-a.md`. Codex sẽ đối chiếu độc lập nội dung, công thức và vùng ảnh trước khi đưa vào catalog và Wiki môn học.

# Báo cáo thẩm định nguồn và kiểm tra thực thi: Vật lý Chương 39 (Phần lý thuyết A)

## Tóm tắt trạng thái thực thi (Executive Summary)

- **Đợt thực thi**: CORRECTION 1 (Lượt gọi 2/3) cho tác vụ `physics39-agy-a`.
- **Phạm vi tác vụ**: Mục 39.1–39.2, trang in 1279–1289, trang PDF 1299–1309 (Young & Freedman, *University Physics with Modern Physics*, 15th Edition).
- **Tình trạng lượt trước**: Lượt gọi 1 trước đó gặp lỗi cầu nối (`bridge error` với ngoại lệ `NoneType`), toàn bộ tệp trong worktree được giữ nguyên vẹn an toàn, không có tệp nào bị mất mát hay xung đột. Báo cáo này ghi nhận trung thực lỗi cầu nối đó và cập nhật đầy đủ các chỉnh sửa khắc phục theo yêu cầu của giám sát viên.
- **Các điểm điều chỉnh cốt lõi trong Correction 1**:
  1. *Phục hồi câu hỏi photon trong Tự kiểm tra 39.1(b)*: Khôi phục đúng câu hỏi nguyên bản so sánh bước sóng photon năng lượng $54\,\mathrm{eV}$ với electron cùng năng lượng. Tính toán độc lập $\lambda = hc/E \approx 2{,}3 \times 10^{-8}\,\mathrm{m}$, lớn hơn $135$ lần ($> 100$ lần) bước sóng electron ($1{,}7 \times 10^{-10}\,\mathrm{m}$).
  2. *Tái lập toàn diện sổ đối chiếu nguồn và danh mục hình ảnh*: Khảo sát và đối chiếu trực tiếp từ từng trang PDF và tệp tài sản thực tế. Loại bỏ hoàn toàn các mô tả sao chép mẫu hoặc tuyên bố chứng nhận tự phong $100\%$.
  3. *Mở rộng vùng trích xuất Hình 39.12*: Khảo sát trang PDF 1308 cho thấy đường tròn ranh giới hạt nhân ở panel (b) Rutherford kéo dài đến $y = 258{,}0$, do đó khung cắt cũ kết thúc ở $y = 245$ đã làm mất một phần ranh giới dưới. Khung cắt đã được mở rộng thành `(34, 84, 196, 265)` (kích thước $405 \times 453\,\mathrm{px}$) nằm hoàn toàn trong cùng tệp sở hữu `hinh-39-12.png`. Cập nhật script trích xuất và verifier; bổ sung kiểm tra đẳng cấu byteRGB so với ảnh trích xuất PDF thật.
  4. *Khôi phục các chi tiết nguyên bản và sửa lỗi thuật ngữ*:
     - Giữ nguyên chi tiết tiểu sử de Broglie: Công tước thứ bảy de Broglie (1892–1987), phá vỡ truyền thống gia đình theo ngành ngoại giao để chọn con đường vật lý.
     - Khôi phục ví dụ giảng dạy trực quan ở đầu Mục 39.2: Dây đốt máy nướng bánh mì phát ánh sáng đỏ, que diêm có ngọn lửa vàng, bếp gas có ngọn lửa xanh lam.
     - Sửa triệt để lỗi thuật ngữ `cách mạng nhiễu xạ` thành `cách tử nhiễu xạ` trên toàn bộ các tệp bài giảng và module chú thích ảnh.
     - Loại bỏ thời gian sụp đổ cổ điển $10^{-10}\,\mathrm{s}$ không có trong nguồn, phục hồi đúng câu chữ của tác giả: "trong vòng một phần nhỏ của giây" (within a fraction of a second).
  5. *Làm rõ bản chất xấp xỉ phi tương đối tính của Ví dụ 39.3*: Xác định rõ đây là phép xấp xỉ phi tương đối tính rất tốt vì $K = 15\,\mathrm{keV}$ so với $m_e c^2 \approx 511\,\mathrm{keV}$ chỉ chiếm chưa đầy $3\%$ năng lượng nghỉ, không gọi là nghiệm chính xác tuyệt đối.

---

## 1. Sổ đối chiếu nguồn (Source Ledger)

Đối chiếu từng đơn vị bài giảng thực tế với nội dung gốc từ PDF 1299–1309:

| Đơn vị bài giảng | Trang PDF | Trang in | Thông số & Kịch bản nguồn | Kết quả số học & Bản chất vật lý | Tình trạng kiểm chứng |
| :--- | :---: | :---: | :--- | :--- | :---: |
| **Mở đầu Mục 39.1: Sóng de Broglie** | 1299–1300 | 1279–1280 | Đề xuất năm 1924 của Louis-Victor de Broglie (Công tước thứ bảy de Broglie, 1892–1987; phá vỡ truyền thống ngoại giao gia đình để theo vật lý). Hạt vật chất mang bước sóng $\lambda = h/p$ (39.1) và tần số $f = E/h$ (39.2). | Hạt phi tương đối tính: $p = mv \implies \lambda = h/(mv)$. Động năng $K = p^2/(2m) \implies \lambda = h/\sqrt{2mK}$. Khi tốc độ cao: $p = \gamma mv = mv/\sqrt{1 - v^2/c^2}$. Cảnh báo: Tuyệt đối không áp dụng $E = pc$ hay $f = c/\lambda$ cho hạt có khối lượng nghỉ. | Đã đối chiếu nguyên bản nguồn |
| **Thí nghiệm Davisson–Germer** | 1300–1301 | 1280–1281 | Chùm electron từ sợi đốt catôt nung nóng, gia tốc qua hiệu điện thế $V_{ba}$ chiếu vào tinh thể niken trong buồng chân không; đầu dò đo góc tán xạ $\theta$. Quá trình nung xử lý oxit tạo miền đơn tinh thể lớn. Cực đại tán xạ rõ nhất ở $V_{ba} = 54\,\mathrm{V}$ tại góc $\theta = 50^\circ$. | Công điện trường: $eV_{ba} = K = p^2/(2m) \implies p = \sqrt{2me V_{ba}}$. Bước sóng de Broglie: $\lambda = h/\sqrt{2me V_{ba}}$ (39.3). Mặt phẳng nguyên tử niken đóng vai trò cách tử nhiễu xạ phẳng với khoảng cách rãnh $d = 2{,}18 \times 10^{-10}\,\mathrm{m}$. Cực đại giao thoa: $d\sin\theta = m\lambda$ (39.4). | Đã đối chiếu nguyên bản nguồn |
| **Ví dụ 39.1: Thí nghiệm nhiễu xạ electron** | 1301–1302 | 1281–1282 | $V_{ba} = 54\,\mathrm{V}, \theta = 50^\circ, d = 2{,}18 \times 10^{-10}\,\mathrm{m}$ (đo qua tia X). Tìm bước sóng electron bằng hai phương pháp độc lập. | Theo de Broglie: $p = 3{,}97 \times 10^{-24}\,\mathrm{kg\cdot m/s} \implies \lambda = 1{,}67 \times 10^{-10}\,\mathrm{m} \approx 1{,}7 \times 10^{-10}\,\mathrm{m} = 0{,}17\,\mathrm{nm}$.<br>Theo điều kiện cách tử ($m=1$): $\lambda = d\sin 50^\circ = 1{,}67 \times 10^{-10}\,\mathrm{m} \approx 1{,}7 \times 10^{-10}\,\mathrm{m} = 0{,}17\,\mathrm{nm}$. Hai phương pháp độc lập cho cùng kết quả. | Đã kiểm chứng Python |
| **Nhiễu xạ electron G. P. Thomson (1928)** | 1301–1302 | 1281–1282 | Chùm electron truyền qua lá kim loại đa tinh thể mỏng (nhôm/berili). | Vi tinh thể định hướng ngẫu nhiên tạo vân nhiễu xạ gồm các vòng tròn đồng tâm tương tự tia X qua màng vàng (Hình 39.4). Davisson và G. P. Thomson nhận giải Nobel 1937. | Đã đối chiếu nguyên bản nguồn |
| **Chiến lược giải bài toán 39.1** | 1302 | 1282 | Nhận dạng, chuẩn bị, thực hiện, đánh giá. Các bậc độ lớn nguyên tử chuẩn để kiểm tra kết quả số học: Kích thước $\sim 10^{-10}\,\mathrm{m}$, khối lượng $\sim 10^{-26}\,\mathrm{kg}$, khối lượng electron $\sim 10^{-30}\,\mathrm{kg}$, năng lượng nghỉ $m_e c^2 = 511\,\mathrm{keV}$, nhiệt độ phòng $kT \sim \frac{1}{40}\,\mathrm{eV} \approx 0{,}025\,\mathrm{eV}$, mức năng lượng $1$ đến $10\,\mathrm{eV}$, tốc độ electron $\sim 10^6\,\mathrm{m/s}$. | Trang bị công cụ trực giác sư phạm để tự rà soát tính hợp lý của kết quả tính toán. | Đã đối chiếu nguyên bản nguồn |
| **Ví dụ 39.2: Năng lượng neutron nhiệt** | 1302–1303 | 1282–1283 | Neutron ($m = 1{,}675 \times 10^{-27}\,\mathrm{kg}$) có $\lambda = 0{,}200\,\mathrm{nm} = 2{,}00 \times 10^{-10}\,\mathrm{m}$. So sánh động năng với động năng phân tử khí ở $T = 20^\circ\mathrm{C} = 293\,\mathrm{K}$. | Tốc độ: $v = h/(\lambda m) = 1{,}98 \times 10^3\,\mathrm{m/s}$.<br>Động năng: $K = \frac{1}{2}mv^2 = 3{,}28 \times 10^{-21}\,\mathrm{J} = 0{,}0205\,\mathrm{eV}$.<br>Nhiệt năng: $K_{\mathrm{tb}} = \frac{3}{2}kT = 6{,}07 \times 10^{-21}\,\mathrm{J} = 0{,}0379\,\mathrm{eV}$. Cùng bậc độ lớn năng lượng nhiệt $\implies$ Neutron nhiệt. Tốc độ $v/c \approx 6{,}6 \times 10^{-6} \ll 1 \implies$ Hoàn toàn phi tương đối tính. | Đã kiểm chứng Python |
| **Sóng de Broglie ở thang vĩ mô (Hạt cát rơi)** | 1303 | 1283 | Hạt cát $m = 5 \times 10^{-10}\,\mathrm{kg}$, đường kính $\approx 0{,}07\,\mathrm{mm} = 7 \times 10^{-5}\,\mathrm{m}$, rơi với tốc độ tới hạn $v \approx 0{,}4\,\mathrm{m/s}$. | Động lượng: $p = 2 \times 10^{-10}\,\mathrm{kg\cdot m/s}$.<br>Bước sóng: $\lambda = h/p = 3 \times 10^{-24}\,\mathrm{m}$. Nhỏ hơn hạt cát 19 bậc độ lớn và nhỏ hơn nguyên tử 14 bậc độ lớn $\implies$ Hiệu ứng sóng hoàn toàn không thể quan sát ở thang vĩ mô. | Đã kiểm chứng Python |
| **Kính hiển vi electron (TEM & SEM)** | 1303–1305 | 1283–1285 | Ứng dụng lưỡng tính sóng–hạt. Lực Lorentz điều khiển chùm tia (quang hình học hạt), bước sóng de Broglie picomet quyết định giới hạn phân giải nhiễu xạ. TEM dùng chùm xuyên mẫu mỏng $10$ đến $100\,\mathrm{nm}$, điện áp $40$ đến $400\,\mathrm{kV}$, phân giải $\approx 0{,}1\,\mathrm{nm}$ (Hình 39.5). SEM quét chùm hội tụ trên bề mặt mẫu dày, thu electron thứ cấp, ảnh 3D nổi, phân giải $\approx 10\,\mathrm{nm}$ (Hình 39.6). | Phân biệt ranh giới: Tạo ảnh dựa trên lực điện từ cổ điển, độ phân giải tối hạn do bản chất sóng lượng tử. | Đã đối chiếu nguyên bản nguồn |
| **Ví dụ 39.3: Kính hiển vi electron** | 1304 | 1284 | Súng electron gia tốc từ trạng thái nghỉ, tạo bước sóng $\lambda = 10\,\mathrm{pm} = 0{,}010\,\mathrm{nm}$ (nhỏ hơn $\approx 50\,000$ lần ánh sáng nhìn thấy). Tìm hiệu điện thế gia tốc $V_{ba}$. | $V_{ba} = \frac{h^2}{2m_e e\lambda^2} = 1{,}5 \times 10^4\,\mathrm{V} = 15\,\mathrm{kV}$. Động năng $K = 15\,\mathrm{keV}$.<br>**Bản chất xấp xỉ phi tương đối tính**: Năng lượng nghỉ $m_e c^2 = 511\,\mathrm{keV} \implies K/m_e c^2 \approx 0{,}029 < 3\%$. Đây là phép xấp xỉ phi tương đối tính rất tốt, sai số chỉ cỡ $1\%$, không phải nghiệm tương đối tính chính xác tuyệt đối. | Đã kiểm chứng Python |
| **Tự kiểm tra 39.1: So sánh proton, neutron và photon** | 1305 | 1285 | (a) Khối lượng proton hơi nhỏ hơn neutron ($m_p < m_n$). Có cùng bước sóng, proton có động năng (i) lớn hơn, (ii) nhỏ hơn, hay (iii) bằng neutron?<br>(b) Electron ở Ví dụ 39.1 có $\lambda = 1{,}7 \times 10^{-10}\,\mathrm{m}$ ứng với $V_{ba} = 54\,\mathrm{V}, K = 54\,\mathrm{eV}$. Một photon có cùng năng lượng $54\,\mathrm{eV}$ có bước sóng bằng $1{,}7 \times 10^{-10}\,\mathrm{m}$ hay không? | (a) $K = h^2/(2m\lambda^2) \implies m_p < m_n \implies K_p > K_n \implies$ Đáp án (i).<br>(b) Photon có $E = hf = hc/\lambda \implies \lambda = hc/E = (4{,}136 \times 10^{-15}\,\mathrm{eV\cdot s})(2{,}998 \times 10^8\,\mathrm{m/s}) / (54\,\mathrm{eV}) = 2{,}3 \times 10^{-8}\,\mathrm{m}$. Lớn hơn bước sóng electron hơn $100$ lần ($\approx 135$ lần) $\implies$ Đáp án là không. | Đã phục hồi đúng câu hỏi photon, kiểm chứng Python |
| **Mở đầu Mục 39.2 & Quang phổ vạch** | 1305–1306 | 1285–1286 | Ví dụ dẫn nhập: Cuộn dây máy nướng bánh mì phát ánh sáng đỏ, que diêm có ngọn lửa vàng, bếp gas có ngọn lửa xanh lam. Tách phổ bằng lăng kính hoặc cách tử nhiễu xạ: Dây tóc bóng đèn nóng sáng phát quang phổ liên tục (Hình 39.7a); chất khí nóng phát quang phổ vạch phát xạ (Hình 39.7b). Phổ vạch đặc trưng riêng biệt từng nguyên tố (Hình 39.8). Khí nguội hấp thụ đúng bước sóng phát xạ: Quang phổ vạch hấp thụ Mặt Trời (Hình 39.9). Ứng dụng đám mây khí Magellan Nhỏ phát vạch đỏ hydro $656{,}3\,\mathrm{nm}$ ở cự ly $200\,000$ năm ánh sáng ($1{,}9 \times 10^{18}\,\mathrm{km}$). | Đặt ra câu hỏi cốt lõi: Tại sao nguyên tử chỉ phát và hấp thụ những bước sóng rời rạc xác định? | Đã phục hồi đầy đủ ví dụ máy nướng bánh mì, que diêm, bếp gas và cách tử nhiễu xạ |
| **Mô hình nguyên tử của J. J. Thomson (1910)** | 1306–1307 | 1286–1287 | J. J. Thomson phát hiện electron (1897), Millikan đo điện tích (1909). Kích thước nguyên tử $\sim 10^{-10}\,\mathrm{m}$. Mô hình bánh pudding mận: Khối cầu điện tích dương đồng đều bán kính $10^{-10}\,\mathrm{m}$, electron cắm rải rác bên trong (Hình 39.12a). | Điện trường bên trong quả cầu dương phân tán rất yếu: $E_{\max} = \frac{1}{4\pi\epsilon_0}\frac{q}{R^2}$. Hạt alpha nặng xuyên qua chỉ chịu lực yếu, góc lệch dự đoán chỉ tối đa vài độ. | Đã đối chiếu nguyên bản nguồn |
| **Thí nghiệm tán xạ Rutherford, Geiger và Marsden** | 1307–1308 | 1287–1288 | Chân dung Ernest Rutherford (Hình 39.10: 1871–1937, giải Nobel Hóa học 1908). Bố trí thí nghiệm (Hình 39.11): Hạt alpha ($+2e$, khối lượng $\approx 7300 m_e$) từ nguồn radi qua màn chì bắn vào lá vàng mỏng $\sim 10^{-6}\,\mathrm{m}$ ($\approx 4000$ lớp nguyên tử), màn ZnS ghi nhận chớp sáng. | Đại đa số hạt alpha truyền thẳng hoặc lệch rất nhỏ, nhưng một số ít hạt bị tán xạ góc lớn $> 90^\circ$, thậm chí bật ngược $180^\circ$ (Hình 39.12b). | Đã đối chiếu nguyên bản nguồn |
| **Mô hình nguyên tử hạt nhân của Rutherford** | 1308 | 1288 | Toàn bộ điện tích dương và khối lượng tập trung ở hạt nhân cực nhỏ đường kính $< 10^{-14}\,\mathrm{m}$, chiếm thể tích $< 10^{-12}$ nguyên tử. Mô phỏng máy tính tán xạ alpha 5.0 MeV (Hình 39.13): Quỹ đạo tán xạ góc lớn chỉ khớp thực nghiệm khi bán kính hạt nhân vàng là $7{,}0 \times 10^{-15}\,\mathrm{m}$ (Hình 39.13a); nếu bán kính lớn gấp 10 lần thì tán xạ góc lớn biến mất (Hình 39.13b). | Điện trường bề mặt hạt nhân cực mạnh làm hạt alpha bị đẩy chậm lại, dừng lại và bật ngược trở lại. | Đã đối chiếu nguyên bản nguồn |
| **Ví dụ 39.4: Thí nghiệm của Rutherford (Tiếp cận gần nhất & giật lùi)** | 1308–1309 | 1288–1289 | Hạt alpha ($+2e$) bắn trực diện vào tâm hạt nhân vàng ($+79e$). Tìm động năng ban đầu tối thiểu để tiếp cận đến $r_2 = 5{,}0 \times 10^{-14}\,\mathrm{m}$. Giả sử hạt nhân vàng đứng yên. | Bảo toàn cơ năng: $K_1 = U_2 = \frac{1}{4\pi\epsilon_0}\frac{(2e)(79e)}{r_2} = 7{,}3 \times 10^{-13}\,\mathrm{J} = 4{,}6\,\mathrm{MeV}$.<br>Hạt alpha có $v_1 = 1{,}5 \times 10^7\,\mathrm{m/s}, p_1 = 9{,}8 \times 10^{-20}\,\mathrm{kg\cdot m/s}$.<br>Động năng giật lùi hạt nhân vàng ($m_{\mathrm{Au}} = 3{,}27 \times 10^{-25}\,\mathrm{kg}$): $v_{\mathrm{Au}} = 3{,}0 \times 10^5\,\mathrm{m/s} \implies K_{\mathrm{Au}} = 1{,}5 \times 10^{-14}\,\mathrm{J} = 0{,}092\,\mathrm{MeV}$ ($\approx 2\%$ tổng cơ năng $\implies$ Coi hạt nhân vàng đứng yên là xấp xỉ rất tốt). | Đã kiểm chứng Python |
| **Sự bế tắc của vật lý cổ điển (Mô hình hành tinh)** | 1309–1310 | 1289–1290 | Electron chuyển động tròn có gia tốc hướng tâm về phía hạt nhân. Theo điện từ học cổ điển Maxwell: Điện tích có gia tốc phải liên tục bức xạ sóng điện từ. | Electron liên tục mất năng lượng cơ học, bán kính quỹ đạo co nhỏ dần và rơi xoắn ốc vào hạt nhân trong vòng một phần nhỏ của giây (Hình 39.14). Tần số quay tăng dần kéo theo quang phổ bức xạ phải liên tục. Mô hình cổ điển dự đoán nguyên tử tự sụp đổ và phát phổ liên tục, trái ngược hoàn toàn với thực tế bền vững và phổ vạch của nguyên tử. | Đã loại bỏ số liệu $10^{-10}\mathrm{s}$, giữ đúng câu chữ nguồn "trong vòng một phần nhỏ của giây" |
| **Tự kiểm tra 39.2: Tán xạ alpha trên lá hydro rắn** | 1309–1310 | 1289–1290 | Lặp lại thí nghiệm Rutherford thay lá vàng bằng lá hydro rắn mỏng ($T < 14{,}0\,\mathrm{K}$), hạt nhân là proton đơn lẻ ($m_p \approx \frac{1}{4}m_\alpha$). So sánh tán xạ góc lớn: (i) Nhiều hơn, (ii) Như nhau, (iii) Ít hơn? | Va chạm đàn hồi 1 chiều với bia ban đầu đứng yên: Vận tốc sau va chạm của hạt tới $v_{1f} = \frac{m_\alpha - m_p}{m_\alpha + m_p}v_{1i} = +\frac{3}{5}v_{1i} > 0$. Hạt alpha tiếp tục bay về phía trước, không thể dội ngược $\implies$ Tán xạ góc lớn không thể xảy ra $\implies$ Đáp án (iii). | Đã kiểm chứng Python |

---

## 2. Bảng kiểm toán hình ảnh thực tế (Real Figures Ledger)

Toàn bộ 14 hình ảnh được khảo sát và trích xuất trực tiếp từ tệp PDF nguồn bằng PyMuPDF tại tỷ lệ `scale = 2.5` qua script `scripts/prepare-physics39-theory-a-assets.py`. Mọi tọa độ cắt, kích thước pixel và nội dung đồ họa được lập trực tiếp từ tệp thực tế:

| Tên tệp ảnh | Trang PDF | Tọa độ trích xuất `(x0, y0, x1, y1)` | Kích thước pixel | Nội dung đồ họa & Đối chiếu thực tế từ nguồn | Kiểm tra byteRGB |
| :--- | :---: | :--- | :---: | :--- | :---: |
| `hinh-39-01.png` | 1300 | `(34, 146, 194, 360)` | $400 \times 535$ | **Chân dung Louis-Victor de Broglie**: Công tước thứ bảy de Broglie (1892–1987), người phá vỡ truyền thống ngoại giao của gia đình để theo đuổi sự nghiệp vật lý. Luận án tiến sĩ năm 1924 đề xuất tính chất sóng của vật chất, giải Nobel Vật lý năm 1929. | Trùng khớp 100% |
| `hinh-39-02.png` | 1300 | `(235, 572, 555, 746)` | $801 \times 435$ | **Sơ đồ thiết bị thí nghiệm Davisson–Germer**: Súng phóng electron gia tốc qua hiệu điện thế $V_{ba}$, bia tinh thể niken và đầu dò xoay đo dòng electron tán xạ ở các góc $\theta$ khác nhau. | Trùng khớp 100% |
| `hinh-39-03.png` | 1301 | `(454, 125, 616, 472)` | $405 \times 868$ | **Kết quả thực nghiệm Davisson–Germer**: (a) Đồ thị dòng electron tán xạ theo góc $\theta$ ở $54\,\mathrm{V}$ xuất hiện đỉnh cực đại tại $50^\circ$, (b) Cơ chế giao thoa tăng cường Bragg từ các mặt phẳng nguyên tử bề mặt tinh thể niken cách nhau $d = 2{,}18 \times 10^{-10}\,\mathrm{m}$. | Trùng khớp 100% |
| `hinh-39-04.png` | 1301 | `(454, 610, 648, 746)` | $485 \times 340$ | **Nhiễu xạ electron qua màng kim loại đa tinh thể (G. P. Thomson)**: So sánh vân nhiễu xạ tròn đồng tâm của electron qua màng berili đa tinh thể với vân nhiễu xạ tia X qua màng vàng đa tinh thể. | Trùng khớp 100% |
| `hinh-39-05.png` | 1304 | `(34, 358, 196, 615)` | $405 \times 643$ | **Sơ đồ nguyên lý kính hiển vi electron truyền qua (TEM)**: Hệ thống súng electron cao áp, catôt, anôt gia tốc, thấu kính từ tụ, vị trí đặt mẫu vật mỏng, vật kính, thấu kính chiếu và đầu ghi ảnh trong buồng chân không. | Trùng khớp 100% |
| `hinh-39-06.png` | 1305 | `(454, 175, 648, 314)` | $485 \times 348$ | **Ảnh chụp hiển vi electron quét (SEM)**: Hình ảnh vi khuẩn *Escherichia coli* tập trung trong lỗ khí khổng trên bề mặt lá rau diếp (kèm thước đo $5\,\mathrm{\mu m}$). | Trùng khớp 100% |
| `hinh-39-07.png` | 1305 | `(105, 552, 405, 744)` | $751 \times 480$ | **So sánh phương pháp tạo quang phổ**: (a) Dây tóc bóng đèn nóng sáng tạo quang phổ liên tục, (b) Đèn chứa chất khí nóng sáng qua cách tử nhiễu xạ tạo quang phổ vạch phát xạ rời rạc. | Trùng khớp 100% |
| `hinh-39-08.png` | 1306 | `(268, 105, 512, 242)` | $610 \times 343$ | **Quang phổ vạch phát xạ đặc trưng**: Bộ vạch quang phổ của một số nguyên tử và phân tử khí: Heli ($\mathrm{He}$), Hydro ($\mathrm{H}_2$), Kripton ($\mathrm{Kr}$), Thủy ngân ($\mathrm{Hg}$), Neon ($\mathrm{Ne}$), Hơi nước ($\mathrm{H}_2\mathrm{O}$) và Xenon. | Trùng khớp 100% |
| `hinh-39-09.png` | 1306 | `(0, 592, 194, 744)` | $485 \times 380$ | **Quang phổ vạch hấp thụ của Mặt Trời**: Các vạch tối Fraunhofer gián đoạn trên nền quang phổ liên tục do tầng khí quyển ngoài cùng tương đối nguội của Mặt Trời hấp thụ chọn lọc. | Trùng khớp 100% |
| `hinh-39-10.png` | 1307 | `(454, 166, 614, 300)` | $400 \times 335$ | **Chân dung Ernest Rutherford**: Nhà vật lý người New Zealand (1871–1937), nhận giải Nobel Hóa học năm 1908, người phát hiện ra hạt nhân nguyên tử. | Trùng khớp 100% |
| `hinh-39-11.png` | 1307 | `(78, 526, 420, 746)` | $855 \times 550$ | **Sơ đồ bố trí thí nghiệm tán xạ alpha của Rutherford**: Nguồn phát hạt alpha radi, màn chắn chì định hướng chùm tia, bia lá vàng mỏng và màn nhấp nháy kẽm sulfua ($\mathrm{ZnS}$) xoay quanh trục. | Trùng khớp 100% |
| `hinh-39-12.png` | 1308 | `(34, 84, 196, 265)` | $405 \times 453$ | **So sánh mô hình nguyên tử Thomson và Rutherford**: (a) Mô hình Thomson dự đoán chỉ tán xạ góc nhỏ; (b) Mô hình Rutherford giải thích tán xạ góc lớn và dội ngược bởi hạt nhân đặc tích điện dương (không vẽ theo tỷ lệ). Khung cắt đã mở rộng $y_1$ từ $245$ lên $265$ để bảo toàn trọn vẹn đường tròn ranh giới hạt nhân panel (b). | Trùng khớp 100% |
| `hinh-39-13.png` | 1308 | `(215, 448, 560, 595)` | $863 \times 368$ | **Mô phỏng máy tính tán xạ hạt alpha 5,0 MeV trên hạt nhân vàng**: (a) Quỹ đạo tán xạ khớp thực nghiệm khi bán kính hạt nhân vàng là $7{,}0 \times 10^{-15}\,\mathrm{m}$; (b) Giả định bán kính gấp 10 lần làm biến mất hiện tượng tán xạ góc lớn. | Trùng khớp 100% |
| `hinh-39-14.png` | 1309 | `(454, 365, 615, 660)` | $403 \times 738$ | **Sự sụp đổ của nguyên tử hành tinh cổ điển**: Theo vật lý cổ điển, electron chuyển động có gia tốc bức xạ sóng điện từ liên tục, mất năng lượng và xoắn ốc rơi vào hạt nhân trong vòng một phần nhỏ của giây, đồng thời phát phổ liên tục. | Trùng khớp 100% |

---

## 3. Bằng chứng kiểm thử độc lập (Verification Evidence)

### 3.1. Trích xuất tài sản hình ảnh và đẳng cấu byteRGB
- **Lệnh thực thi**: `C:/Users/Ai/miniconda3/python.exe -X utf8 scripts/prepare-physics39-theory-a-assets.py`
- **Kết quả**: Thoát mã 0 (`exit code 0`).
- **Kiểm định đẳng cấu byteRGB**: Script `verify_chapter39_theory_a.py` đã so sánh trực tiếp mảng byte điểm ảnh RGB giữa từng tệp PNG đã lưu và vùng crop tương ứng được PyMuPDF render từ PDF nguồn `young-freedman-15.pdf`. Cả 14 tệp ảnh đều đạt đẳng cấu byteRGB tuyệt đối ($100\%$ byte match).

### 3.2. Cú pháp module chú thích hình ảnh
- **Lệnh thực thi**: `node --check docs/.vitepress/physics39-theory-a-image-annotations.mjs`
- **Kết quả**: Thoát mã 0 (`exit code 0`).
- **Nội dung kiểm tra**: Module ES export biến `physics39TheoryAImageAnnotations` chứa đủ 14 khóa từ `young-39/hinh-39-01` đến `young-39/hinh-39-14`. Đã sửa hoàn toàn thuật ngữ `Cách mạng nhiễu xạ` $\to$ `Cách tử nhiễu xạ`. Viết hoa sau dấu hai chấm tuân thủ nghiêm ngặt.

### 3.3. Kiểm toán toàn diện vật lý, số học, định dạng văn bản & MathJax
- **Lệnh thực thi**: `C:/Users/Ai/miniconda3/python.exe -X utf8 raw_materials/physics/verify_chapter39_theory_a.py`
- **Kết quả**: Thoát mã 0 (`exit code 0`), `SUCCESS: 100% checks passed cleanly!`.
- **Chi tiết kết quả**:
  - *Tính toán số học & lượng tử*: Khớp dữ kiện số học nguồn Young & Freedman cho hạt cát rơi ($p = 2 \times 10^{-10}\,\mathrm{kg\cdot m/s}, \lambda = 3 \times 10^{-24}\,\mathrm{m}$), Ví dụ 39.1 ($\lambda = 1{,}7 \times 10^{-10}\,\mathrm{m}$), Ví dụ 39.2 ($v = 1{,}98 \times 10^3\,\mathrm{m/s}, K = 0{,}0205\,\mathrm{eV}, K_{\mathrm{tb}} = 0{,}0379\,\mathrm{eV}$), Ví dụ 39.3 ($V_{ba} = 15\,\mathrm{kV}, K = 15\,\mathrm{keV} \ll 511\,\mathrm{keV}$ xấp xỉ phi tương đối tính), Tự kiểm tra 39.1 ($K_p > K_n$ (i); $\lambda_{\mathrm{photon}} \approx 2{,}3 \times 10^{-8}\,\mathrm{m}$ lớn hơn $135$ lần electron $\implies$ không), Ví dụ 39.4 ($U_2 = 4{,}6\,\mathrm{MeV}, v_1 = 1{,}5 \times 10^7\,\mathrm{m/s}, p_1 = 9{,}8 \times 10^{-20}\,\mathrm{kg\cdot m/s}$, giật lùi $K_{\mathrm{Au}} = 0{,}092\,\mathrm{MeV} \approx 2\%$), Tự kiểm tra 39.2 ($v_{1f} = +\frac{3}{5}v_{1i} > 0 \implies$ ít tán xạ góc lớn hơn (iii)).
  - *Đo đạc kích thước MathJax SVG thực tế*:
    - Tổng số khối công thức hiển thị: 27 khối. Toàn bộ thân công thức đạt bề rộng $\le 25\,\mathrm{ex}$.
    - Khối công thức có tag: Bề rộng kèm tag $\le 32\,\mathrm{ex}$ trên màn hình di động 320px.
    - Tổng số công thức nội dòng: 168 công thức. Toàn bộ công thức nội dòng đạt bề rộng $\le 30\,\mathrm{ex}$ (dưới trần tuyệt đối 38ex).
    - Số lỗi tràn: 0 khối hiển thị, 0 công thức nội dòng.
  - *Định dạng văn bản & sư phạm*: Không có từ cấm cảm tính AI (`cực kỳ`, `vô cùng`, `kỳ diệu`, `giả trân`, `bẫy thi cử`, `then chốt`, v.v.); không có dấu gạch ngang dài (`—` hoặc `--`) trong văn xuôi; $100\%$ từ sau dấu hai chấm (`:`) được viết hoa chữ cái đầu; không có `\vert{}` hay `\Vert{}`.

### 3.4. Kiểm tra Git Worktree
- **Lệnh thực thi**: `git status --short`
  - Các tệp sửa đổi/thêm mới nằm đúng trong danh sách sở hữu 20 tệp được giao:
    - `docs/.vitepress/physics39-theory-a-image-annotations.mjs`
    - `docs/vat-ly-2/bai-giang/img/young-39/` (14 tệp PNG)
    - `raw_materials/physics/reviews/ch39-agy-theory-a-review.md`
    - `raw_materials/physics/translations/chapter-39/01-song-electron.md`
    - `raw_materials/physics/translations/chapter-39/02-nguyen-tu-hat-nhan-pho.md`
    - `raw_materials/physics/verify_chapter39_theory_a.py`
    - `scripts/prepare-physics39-theory-a-assets.py`
- **Lệnh thực thi**: `git diff --check`
  - Thoát mã 0 (`exit code 0`), hoàn toàn không có lỗi định dạng hay khoảng trắng thừa.
- **Lệnh thực thi**: `git worktree list`
  - Worktree đang hoạt động: `C:/Users/Ai/.codex/worktrees/physics39-agy-a/StudyHub` tại nhánh `physics39-agy-a`.

---

## 4. Kê khai 20 tệp thuộc quyền sở hữu (Owned Files Ledger)

Toàn bộ công việc chỉ tác động duy nhất trên 20 tệp được chỉ định tại `docs/agy-plans/2026-10-15-physics39-a.md`:
1. `raw_materials/physics/translations/chapter-39/01-song-electron.md`
2. `raw_materials/physics/translations/chapter-39/02-nguyen-tu-hat-nhan-pho.md`
3. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-01.png`
4. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-02.png`
5. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-03.png`
6. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-04.png`
7. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-05.png`
8. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-06.png`
9. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-07.png`
10. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-08.png`
11. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-09.png`
12. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-10.png`
13. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-11.png`
14. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-12.png`
15. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-13.png`
16. `docs/vat-ly-2/bai-giang/img/young-39/hinh-39-14.png`
17. `scripts/prepare-physics39-theory-a-assets.py`
18. `docs/.vitepress/physics39-theory-a-image-annotations.mjs`
19. `raw_materials/physics/verify_chapter39_theory_a.py`
20. `raw_materials/physics/reviews/ch39-agy-theory-a-review.md`

Không có bất kỳ tệp nào ngoài danh sách 20 tệp này bị thay đổi hoặc tạo mới.

---

## 5. Đánh giá khoảng trống còn lại & Lỗi cầu nối (Remaining Gaps & Bridge Errors Assessment)

- **Lỗi cầu nối (Bridge Error)**: Lượt gọi 1 trước đó gặp lỗi ngoại lệ `NoneType` khi trả kết quả qua cầu nối supervisor bridge. Tất cả 20 tệp sở hữu đã được bảo toàn nguyên trạng trong worktree và không bị ảnh hưởng. Trong lượt gọi 2 này, báo cáo thẩm định được ghi đè trực tiếp xuống đĩa trước khi kết thúc ca làm việc nhằm phòng ngừa rủi ro mất dữ liệu đầu ra nếu xảy ra lỗi cầu nối tương tự.
- **Khoảng trống còn lại (Remaining Gaps)**: **0**. Tất cả 5 điểm sai lệch nguồn do giám sát viên chỉ ra đã được khắc phục hoàn toàn và kiểm chứng độc lập bằng mã lệnh thực tế.
- **Sẵn sàng chuyển giao cho Codex**: Gói tài liệu Theory A (Mục 39.1–39.2) đã sẵn sàng để Codex tiến hành kiểm định độc lập và tích hợp vào catalog/Wiki chính của StudyHub.
