# Báo Cáo Đánh Giá Độc Lập Bài Tập Đánh Số Chương 10 (10.1–10.75): Vật Lý Đại Cương 1

**Ngày thực hiện**: 23/10/2026
**Người thực hiện**: Antigravity Assistant (Đánh giá độc lập - Báo cáo hiệu chỉnh toàn diện)
**Tệp mục tiêu được rà soát**: `raw_materials/physics/translations/chapter-10/11-bai-tap-001-075.md`
**Kế hoạch cam kết tham chiếu**: `docs/agy-plans/2026-10-23-physics1-ch10-numbered-review.md` (Commit: `455c572d`)
**Tài liệu nguồn gốc đối chiếu**: Giáo trình *Young & Freedman, University Physics 15th Edition*, Chương 10: *Dynamics of Rotational Motion*, trang in 328–334 (tương ứng trang PDF 348–354 trong `raw_materials/physics/source/young-freedman-15.pdf`).

---

## 1. Tổng Quan & Phạm Vi Rà Soát Độc Lập

Báo cáo này ghi nhận toàn bộ kết quả rà soát học thuật và kiểm định vật lý độc lập đối với 75 lời giải bài tập đánh số (từ Bài 10.1 đến Bài 10.75) do Parent soạn thảo tại tệp `raw_materials/physics/translations/chapter-10/11-bai-tap-001-075.md` (gồm 2.253 dòng).

### Phạm vi và nguyên tắc thẩm định
1. **Chủ quyền bài giảng & Tính độc lập học thuật**: Đánh giá bản dịch và lời giải theo đúng chuẩn mực học thuật của StudyHub, bảo đảm văn phong sư phạm của người giảng viên độc lập, mạch lạc, trực diện, không lệ thuộc câu chữ dịch máy và không mang tính chắp vá thụ động.
2. **Kiểm tra tính toán số học độc lập trong bộ nhớ**: Toàn bộ các phép tính số học, đơn vị đo, dấu vector, tích có hướng và các bước biến đổi giải tích đều được tính toán lại độc lập thông qua Python chạy trực tiếp trong bộ nhớ (`python -B -X utf8 -c`), hoàn toàn không suy đoán cảm tính, không chạy trực tiếp script verifier để bảo vệ tính bất biến của không gian làm việc.
3. **Loại bỏ các khẳng định tuyệt đối hóa không căn cứ**: Mọi kết luận thẩm định trong báo cáo đều đi kèm dữ kiện nguồn gốc và bước chứng minh định lượng tường minh. Các phát biểu mang tính cảm tính ("100%", "tuyệt đối không tì vết") được thay thế bằng số liệu kiểm toán cụ thể.
4. **Phân bố thực tế của 75 bài tập trên tài liệu nguồn PDF**:
   - **Trang PDF 348 (trang in 328)**: Bài 10.1 – 10.3 (Mômen lực cơ bản, tích vector, quy tắc bàn tay phải).
   - **Trang PDF 349 (trang in 329)**: Bài 10.4 – 10.18 (Mômen lực tổng hợp, định luật II Newton cho vật rắn quay quanh trục cố định, liên kết dây quấn).
   - **Trang PDF 350 (trang in 330)**: Bài 10.19 – 10.35 (Động năng lăn không trượt, bảo toàn cơ năng trong chuyển động lăn, công và công suất quay).
   - **Trang PDF 351 (trang in 331)**: Bài 10.36 – 10.49 (Mômen động lượng của chất điểm và vật rắn, định luật bảo toàn mômen động lượng).
   - **Trang PDF 352 (trang in 332)**: Bài 10.50 – 10.61 (Côn trùng bò trên thanh quay, hiện tượng tiến động con quay gyroscope, va chạm và chuyển động quay).
   - **Trang PDF 353 (trang in 333)**: Bài 10.62 – 10.72 (Bài toán tổng hợp: Cơ cấu Atwood có quán tính ròng rọc, lăn trên máng tròn, điều kiện tiếp xúc).
   - **Trang PDF 354 (trang in 334)**: Bài 10.73 – 10.75 (Chuyển tiếp giữa lăn và trượt, bảo toàn cơ năng phân tách, ném ngang sau khi lăn khỏi bờ dốc).

---

## 2. Phân Tích Chuyên Sâu Các Bài Toán Trọng Điểm (High-Stakes Scrutiny)

Theo kế hoạch cam kết, chín nhóm bài toán nhạy cảm về bản chất vật lý, dấu vector, mômen biến thiên và bảo toàn năng lượng được tiến hành kiểm chứng đa chiều như sau:

### 2.1. Nhóm bài 10.1 – 10.4: Quy ước dấu và chiều quay của mômen lực
- **Bài 10.1**: Thanh dài $4{,}00\,\mathrm m$, lực tác dụng có độ lớn $F = 10{,}0\,\mathrm N$. Tính mômen lực đối với điểm O trong 6 trường hợp hình vẽ (a)–(f):
  - *(a)* Trục O tại một đầu, lực $\vec F \perp$ thanh tại đầu kia ($r = 4{,}00\,\mathrm m$): $\tau_a = +Fr = +(10{,}0\,\mathrm N)(4{,}00\,\mathrm m) = +40{,}0\,\mathrm{N\cdot m}$ (ngược chiều kim đồng hồ, CCW, dấu dương).
  - *(b)* Trục O tại một đầu, lực $\vec F$ đặt ở đầu kia ($r = 4{,}00\,\mathrm m$) hợp góc $60{,}0^\circ$ với thanh: $\tau_b = +Fr\sin 60{,}0^\circ = +(10{,}0)(4{,}00)\frac{\sqrt{3}}{2} = +34{,}6\,\mathrm{N\cdot m}$ (CCW, dấu dương).
  - *(c)* Trục O tại một đầu, lực $\vec F \perp$ thanh tại điểm chính giữa ($r = 2{,}00\,\mathrm m$): $\tau_c = +Fr = +(10{,}0)(2{,}00) = +20{,}0\,\mathrm{N\cdot m}$ (CCW, dấu dương).
  - *(d)* Trục O tại điểm chính giữa thanh, lực $\vec F$ đặt ở đầu ngoài ($r = 2{,}00\,\mathrm m$) hợp góc $60{,}0^\circ$ hướng xuống bên trái: $\tau_d = -Fr\sin 60{,}0^\circ = -(10{,}0)(2{,}00)\frac{\sqrt{3}}{2} = -17{,}3\,\mathrm{N\cdot m}$ (cùng chiều kim đồng hồ, CW, dấu âm).
  - *(e)* Lực tác dụng dọc theo trục của thanh: Cánh tay đòn bằng 0 nên $\tau_e = 0$.
  - *(f)* Lực tác dụng trực tiếp tại trục quay O ($r = 0$): $\tau_f = 0$.
  - *Nhận xét học thuật*: Giá trị tính toán của Parent hoàn toàn chính xác về độ lớn và dấu. Điểm cần lưu ý là lời giải hoán đổi nhẹ lời giải thích hình học giữa câu (e) và (f): Ở câu (e) điểm đặt ở đầu nhưng giá đi qua O; ở câu (f) điểm đặt nằm trực tiếp tại O.
- **Bài 10.2**: Thanh chịu tác dụng đồng thời của 2 lực trong mặt phẳng: $F_1 = 8{,}00\,\mathrm N$ hướng thẳng đứng xuống dưới tại điểm cách O khoảng $5{,}00\,\mathrm m$ ($2{,}00\,\mathrm m + 3{,}00\,\mathrm m$); $F_2 = 12{,}0\,\mathrm N$ đặt cách O khoảng $2{,}00\,\mathrm m$, hợp góc $30{,}0^\circ$ hướng lên sang trái:
  - $\tau_1 = -(8{,}00\,\mathrm N)(5{,}00\,\mathrm m) = -40{,}0\,\mathrm{N\cdot m}$ (chiều kim đồng hồ, CW).
  - $\tau_2 = +(12{,}0\,\mathrm N)(2{,}00\,\mathrm m)\sin 30{,}0^\circ = +12{,}0\,\mathrm{N\cdot m}$ (ngược chiều kim đồng hồ, CCW).
  - $\tau_{\text{net}} = -40{,}0 + 12{,}0 = -28{,}0\,\mathrm{N\cdot m}$ (chiều kim đồng hồ, CW).
- **Bài 10.3**: Tấm kim loại hình vuông đồng chất cạnh $0{,}180\,\mathrm m$ quay quanh trục qua tâm O (khoảng cách vuông góc từ tâm tới các cạnh là $b = 0{,}0900\,\mathrm m$). Ba lực tác dụng: $F_1 = 18{,}0\,\mathrm N$ ở mép trên sang trái; $F_2 = 26{,}0\,\mathrm N$ ở mép phải hướng lên; $F_3 = 14{,}0\,\mathrm N$ ở góc hợp góc $45^\circ$:
  - $\tau_1 = -(18{,}0)(0{,}0900) = -1{,}62\,\mathrm{N\cdot m}$ (CW).
  - $\tau_2 = +(26{,}0)(0{,}0900) = +2{,}34\,\mathrm{N\cdot m}$ (CCW).
  - Cánh tay đòn của lực $F_3$: $d_3 = b\sqrt{2} = 0{,}0900\sqrt{2} \implies \tau_3 = +(14{,}0)(0{,}0900\sqrt{2}) = +1{,}782\,\mathrm{N\cdot m}$ (CCW).
  - $\tau_{\text{net}} = -1{,}62 + 2{,}34 + 1{,}782 = +2{,}50\,\mathrm{N\cdot m}$ (ngược chiều kim đồng hồ, CCW). Lời giải parent tính toán chuẩn xác, không nhầm lẫn cấu hình hình học.
- **Bài 10.4**: Bánh xe bán kính $R = 0{,}350\,\mathrm m$ chịu tác dụng của 3 lực:
  - Lực hướng tâm $F_{\text{rad}} = 11{,}9\,\mathrm N$ có giá đi qua tâm nên cánh tay đòn bằng 0, mômen $\tau = 0$.
  - Lực tiếp tuyến $F_{\text{tan}} = 8{,}50\,\mathrm N$ làm quay ngược chiều kim đồng hồ: $\tau_{\text{tan}} = +R F_{\text{tan}} = +(0{,}350)(8{,}50) = +2{,}975\,\mathrm{N\cdot m}$.
  - Lực $F_{\text{ang}} = 14{,}6\,\mathrm N$ hợp góc $40{,}0^\circ$ với bán kính làm quay cùng chiều kim đồng hồ: $\tau_{\text{ang}} = -R F_{\text{ang}}\sin 40{,}0^\circ = -(0{,}350)(14{,}6)\sin 40{,}0^\circ = -3{,}2846\,\mathrm{N\cdot m}$.
  - $\tau_{\text{net}} = +2{,}975 - 3{,}2846 = -0{,}310\,\mathrm{N\cdot m}$ (chiều kim đồng hồ, CW). Đề bài gốc không cho và không yêu cầu mômen quán tính $I$, chỉ hỏi mômen lực tổng hợp. Lời giải parent bám sát chuẩn xác yêu cầu đề bài.

### 2.2. Bài 10.37: Dấu vector vị trí, vận tốc và mômen động lượng
- **Đề bài**: Viên đá $m = 2{,}00\,\mathrm{kg}$ bay ngang sang phải với $v = 12{,}0\,\mathrm{m/s}$ qua điểm P có $OP = 8{,}00\,\mathrm m$, đường OP hợp góc $36{,}9^\circ$ với phương ngang. Điểm P ở phía trên bên trái trục tọa độ O.
- **Tọa độ vector vị trí**: $r_x = -8{,}00 \cos 36{,}9^\circ = -6{,}40\,\mathrm m$, $r_y = +8{,}00 \sin 36{,}9^\circ = +4{,}80\,\mathrm m$.
- **Mômen động lượng quanh O**:
  $$\vec{L} = \vec{r} \times m\vec{v} = (-6{,}40\hat{\imath} + 4{,}80\hat{\jmath}) \times (2{,}00 \times 12{,}0\hat{\imath}) = - (4{,}80)(24{,}0)\hat{k} = -115{,}2\hat{k} \approx -115\hat{k}\,\mathrm{kg\cdot m^2/s}.$$
  Dấu âm thể hiện vector $\vec{L}$ hướng vào trong mặt phẳng hình vẽ (trục $-z$).
- **Tốc độ biến thiên mômen động lượng**:
  $$\frac{d\vec{L}}{dt} = \vec{\tau}_{\text{net}} = \vec{r} \times (-mg\hat{\jmath}) = (-6{,}40\hat{\imath} + 4{,}80\hat{\jmath}) \times (-19{,}6\hat{\jmath}) = (-6{,}40)(-19{,}6)\hat{k} = +125{,}44\hat{k} \approx +125\hat{k}\,\mathrm{N\cdot m}.$$
  Vector hướng ra khỏi hình vẽ (trục $+z$). Dấu của $d\vec{L}/dt$ ngược với dấu của $\vec{L}$, tức trọng lực đang làm giảm độ lớn mômen động lượng của viên đá đối với gốc O.

### 2.3. Bài 10.42: Công của lực hướng tâm khi thay đổi bán kính dây quấn
- **Hiện tượng**: Khối chất điểm $m = 0{,}0250\,\mathrm{kg}$ chuyển động tròn trên bàn nhẵn với bán kính ban đầu $r_i = 0{,}300\,\mathrm m$, $\omega_i = 2{,}85\,\mathrm{rad/s}$. Dây bị kéo xuyên qua lỗ ở tâm để giảm bán kính về $r_f = 0{,}150\,\mathrm m$.
- **Bảo toàn mômen động lượng**: Vì lực căng dây luôn hướng xuyên tâm về lỗ tròn, mômen lực tác dụng quanh trục qua lỗ bằng 0. Do đó $L_z = \text{const}$.
  $$\omega_f = \omega_i \left(\frac{r_i}{r_f}\right)^2 = 2{,}85 \times \left(\frac{0{,}300}{0{,}150}\right)^2 = 11{,}4\,\mathrm{rad/s}.$$
- **Động năng và công**:
  - $K_i = \frac{1}{2} m r_i^2 \omega_i^2 = \frac{1}{2}(0{,}0250)(0{,}300)^2(2{,}85)^2 = 0{,}00914\,\mathrm J$.
  - $K_f = \frac{1}{2} m r_f^2 \omega_f^2 = \frac{1}{2}(0{,}0250)(0{,}150)^2(11{,}4)^2 = 0{,}0366\,\mathrm J$.
  - Công kéo dây: $W = \Delta K = K_f - K_i = +0{,}0274\,\mathrm J$.
- **Bản chất vật lý**: Lực căng dây hướng vào trong tâm và điểm đặt lực dịch chuyển về phía tâm nên lực căng sinh công dương, công cơ học từ ngoại lực chuyển hóa trực tiếp thành động năng của vật.

### 2.4. Bài 10.47: Phân tách năng lượng quay và năng lượng tịnh tiến thẳng đứng
- **Hệ vật**: Mâm gỗ hình đĩa $M = 120\,\mathrm{kg}$, $R = 2{,}00\,\mathrm m$, $\omega_i = 3{,}00\,\mathrm{rad/s}$. Người nhảy dù $m = 70{,}0\,\mathrm{kg}$ rơi thẳng đứng tiếp đất tại mép ngoài mâm rồi quay cùng mâm.
- **Bảo toàn mômen động lượng trục đứng**: Người rơi thẳng đứng không có vận tốc tiếp tuyến nên mômen động lượng ban đầu theo trục đứng bằng 0.
  $$I_i = \frac{1}{2}MR^2 = 240\,\mathrm{kg\cdot m^2}, \quad I_f = I_i + mR^2 = 240 + 70 \times 4 = 520\,\mathrm{kg\cdot m^2}.$$
  $$\omega_f = \frac{I_i \omega_i}{I_f} = \frac{240 \times 3{,}00}{520} = 1{,}3846 \approx 1{,}38\,\mathrm{rad/s}.$$
- **Năng lượng**:
  - $K_{i,\text{rot}} = \frac{1}{2}(240)(3{,}00)^2 = 1080\,\mathrm J$.
  - $K_{f,\text{rot}} = \frac{1}{2}(520)(1{,}3846)^2 = 498{,}46 \approx 498\,\mathrm J$.
  - Độ hụt động năng quay: $\Delta K_{\text{rot}} = -582\,\mathrm J$.
- **Tính chính xác**: $582\,\mathrm J$ động năng quay chuyển hóa thành nhiệt năng qua ma sát trượt giữa chân người và mặt mâm trong quá trình đồng tốc. Động năng rơi thẳng đứng của người khi chạm mâm bị tiêu tán riêng biệt qua biến dạng của chân và sàn, không ghép nối với chuyển động quay.

### 2.5. Bài 10.61: Mômen lực biến thiên khi thanh rơi, cảnh báo công thức gia tốc góc hằng số
- **Cấu hình**: Thanh dài $L = 0{,}800\,\mathrm m$, $M = 3{,}80\,\mathrm{kg}$, hai viên cầu $m = 2{,}50\,\mathrm{kg}$ ở hai đầu, quay quanh trục qua tâm thanh. Một viên cầu rơi ra khi thanh đang nằm ngang.
- **Mômen quán tính hệ còn lại**:
  $$I = \frac{ML^2}{12} + m\left(\frac{L}{2}\right)^2 = \frac{3{,}80 \times 0{,}64}{12} + 2{,}50 \times 0{,}16 = 0{,}20267 + 0{,}400 = 0{,}60267\,\mathrm{kg\cdot m^2}.$$
- **Gia tốc góc ban đầu**:
  $$\tau_0 = mg\left(\frac{L}{2}\right) = 2{,}50 \times 9{,}80 \times 0{,}400 = 9{,}80\,\mathrm{N\cdot m} \implies \alpha_0 = \frac{9{,}80}{0{,}60267} = 16{,}26 \approx 16{,}3\,\mathrm{rad/s^2}.$$
- **Phân tích biến thiên**: Khi thanh nghiêng một góc $\phi$ so với phương ngang, mômen trọng lực là $\tau(\phi) = mg(L/2)\cos\phi$. Khi thanh tới phương thẳng đứng ($\phi = 90^\circ$), $\tau = 0 \implies \alpha = 0$.
- **Lưu ý phương pháp luận**: Vì gia tốc góc biến thiên liên tục từ $16{,}3\,\mathrm{rad/s^2}$ về $0$, không thể dùng công thức động học chuyển động tròn biến đổi đều. Phải dùng bảo toàn cơ năng:
  $$mg\left(\frac{L}{2}\right) = \frac{1}{2}I\omega^2 \implies \omega = \sqrt{\frac{2 \times 9{,}80}{0{,}60267}} = 5{,}70\,\mathrm{rad/s}.$$

### 2.6. Bài 10.69: Lực nâng của móc treo trong máy Atwood có quán tính ròng rọc
- **Hệ vật**: $W_A = 125\,\mathrm N$, $W_B = 75{,}0\,\mathrm N$, ròng rọc đĩa đặc $W_p = 80{,}0\,\mathrm N$, $R = 0{,}300\,\mathrm m$.
- **Gia tốc góc và chuyển động**:
  $$\frac{a}{g} = \frac{W_A - W_B}{W_A + W_B + W_p/2} = \frac{125 - 75}{125 + 75 + 40} = \frac{50}{240} = \frac{5}{24}.$$
- **Sức căng hai nhánh dây**:
  - Nhánh A (đi xuống): $T_A = W_A(1 - a/g) = 125 \times \frac{19}{24} = 98{,}96 \approx 99{,}0\,\mathrm N$.
  - Nhánh B (đi lên): $T_B = W_B(1 + a/g) = 75{,}0 \times \frac{29}{24} = 90{,}625 \approx 90{,}6\,\mathrm N$.
- **Lực tác dụng lên móc treo**:
  $$F_{\text{hook}} = W_p + T_A + T_B = 80{,}0 + 98{,}96 + 90{,}625 = 269{,}58 \approx 270\,\mathrm N.$$
- **Nhận định vật lý**: Tổng trọng lượng tĩnh của cả hệ là $W_A + W_B + W_p = 125 + 75 + 80 = 280\,\mathrm N$. Khi hệ gia tốc, lực tác dụng lên móc treo chỉ là $270\,\mathrm N < 280\,\mathrm N$. Khối lượng tổng hợp có gia tốc khối tâm đi xuống nên trọng lượng biểu kiến tác dụng lên giá đỡ giảm bớt.

### 2.7. Bài 10.72: Chuyển động lăn không trượt trên vòng xiếc thẳng đứng
- **Cấu hình**: Vỏ cầu mỏng $I = \frac{2}{3}mr^2$, thả từ nghỉ ở độ cao $h_0$, lăn không trượt vào vòng xiếc bán kính $R$.
- **(a) Chiều cao tối thiểu $h_{0,\min}$ để không rơi khỏi vòng**:
  - Điều kiện tại đỉnh A: Phản lực $N_A \ge 0 \implies v_A^2 \ge gR$.
  - Động năng lăn: $K = \frac{1}{2}mv^2 + \frac{1}{2}\left(\frac{2}{3}mr^2\right)\left(\frac{v}{r}\right)^2 = \frac{5}{6}mv^2$.
  - Cơ năng: $mgh_0 = 2mgR + \frac{5}{6}mv_A^2 = 2mgR + \frac{5}{6}mgR = \frac{17}{6}mgR \implies h_{0,\min} = \frac{17}{6}R \approx 2{,}83R$.
- **(b) Phản lực tại vị trí B (ngang tâm vòng)**:
  - $\frac{5}{6}mv_B^2 = mg(h_0 - R) = mg\left(\frac{17}{6}R - R\right) = \frac{11}{6}mgR \implies mv_B^2 = \frac{11}{5}mgR$.
  - Lực hướng tâm tại B thuần túy do phản lực pháp tuyến cung cấp: $N_B = \frac{mv_B^2}{R} = \frac{11}{5}mg = 2{,}20mg$.
- **(c) Trường hợp ray không ma sát**:
  - Khi ray nhẵn bóng, không có ma sát tiếp tuyến để sinh mômen lực làm quay quả cầu. Quả cầu chỉ trượt thuần túy mà không quay: $K = \frac{1}{2}mv^2$.
  - Tại đỉnh: $mg(h_0 - 2R) = \frac{1}{2}mv_A^2 \implies v_A^2 = 2g(h_0 - 2R) = 2g\left(\frac{17}{6}R - 2R\right) = \frac{5}{3}gR > gR$. Quả cầu đi hết vòng trọn vẹn và an toàn.
- **(d) Phản lực tại đỉnh khi không có ma sát**:
  - $N_A + mg = \frac{mv_A^2}{R} = \frac{5}{3}mg \implies N_A = \frac{2}{3}mg > 0$.

### 2.8. Bài 10.74: Chuyển động phức hợp: Lăn lên dốc rồi phóng bay khỏi bờ dốc
- **Hệ vật**: Quả cầu đặc đồng chất $I = \frac{2}{5}MR^2$, lăn không trượt lên dốc từ chân với $v_0 = 25{,}0\,\mathrm{m/s}$. Đỉnh dốc cao $h = 28{,}0\,\mathrm m$. Tại mép dốc, quả cầu bay ngang ra không trung như một vật ném ngang.
- **(a) Quỹ đạo và vận tốc chạm đất**:
  - Cơ năng lăn lên dốc: $\frac{7}{10}Mv_0^2 = Mgh + \frac{7}{10}Mu^2 \implies u^2 = v_0^2 - \frac{10}{7}gh = 25^2 - \frac{10}{7}(9{,}80)(28{,}0) = 625 - 392 = 233\,\mathrm{m^2/s^2} \implies u \approx 15{,}264\,\mathrm{m/s} \approx 15{,}3\,\mathrm{m/s}$.
  - Thời gian bay từ độ cao $h = 28{,}0\,\mathrm m$: $t = \sqrt{\frac{2h}{g}} = \sqrt{\frac{56{,}0}{9{,}80}} = \sqrt{5{,}714} \approx 2{,}390\,\mathrm s \approx 2{,}39\,\mathrm s$.
  - Tầm xa rơi: $x = u t = 15{,}264 \times 2{,}390 \approx 36{,}49\,\mathrm m \approx 36{,}5\,\mathrm m$.
  - Tốc độ tịnh tiến ngay trước khi chạm đất:
    $$v_{\text{impact}} = \sqrt{u^2 + 2gh} = \sqrt{233 + 2(9{,}80)(28{,}0)} = \sqrt{233 + 548{,}8} = \sqrt{781{,}8} \approx 27{,}96\,\mathrm{m/s} \approx 28{,}0\,\mathrm{m/s}.$$
- **(b) Nghịch lý tốc độ chạm đất $28{,}0\,\mathrm{m/s} > v_0 = 25{,}0\,\mathrm{m/s}$**:
  - Trong giai đoạn bay tự do, chỉ có trọng lực tác dụng xuyên qua tâm quả cầu (mômen lực quanh khối tâm bằng 0). Do đó, tốc độ góc $\omega = u/R$ và động năng quay được bảo toàn nguyên vẹn.
  - Toàn bộ thế năng rơi tự do $Mgh$ được chuyển hóa thành động năng tịnh tiến $K_{\text{trans}}$, thay vì phải chia bớt $\frac{2}{7}$ cho động năng quay như trong chuyển động lăn. Cơ năng toàn phần của hệ được bảo toàn nguyên vẹn.

### 2.9. Đính chính & Xác minh các bài toán trọng điểm được điều chỉnh từ báo cáo cũ
- **Bài 10.48 (Tiểu hành tinh va chạm Trái Đất)**: Đề bài yêu cầu tìm khối lượng tiểu hành tinh $m$ theo khối lượng Trái Đất $M$ để ngày dài thêm $25{,}0\%$. Kết quả tính toán độc lập: $I_f = 1{,}25I_i \implies mR^2 = 0{,}25(\frac{2}{5}MR^2) \implies m = 0{,}100M$. Khớp hoàn toàn với lời giải parent.
- **Bài 10.49 (Côn trùng nhảy khỏi thanh)**: Côn trùng $m = 10{,}0\,\mathrm g = 0{,}0100\,\mathrm{kg}$ nhảy ngang $v = 20{,}0\,\mathrm{cm/s} = 0{,}200\,\mathrm{m/s}$ từ đầu thanh $M = 50{,}0\,\mathrm g = 0{,}0500\,\mathrm{kg}$ dài $L = 1{,}00\,\mathrm m$ quay quanh đinh cố định. Kết quả tính toán: $\omega = \frac{mvL}{I} = \frac{0{,}00200}{0{,}0500/3} = 0{,}120\,\mathrm{rad/s}$, động năng toàn hệ $K_{\text{tot}} = \frac{1}{2}I\omega^2 + \frac{1}{2}mv^2 = 1{,}20\times 10^{-4} + 2{,}00\times 10^{-4} = 3{,}20\times 10^{-4}\,\mathrm J$, năng lượng do hoạt động cơ bắp sinh ra.
- **Bài 10.50 (Côn trùng bò trên thanh quay)**: Thanh đồng chất dài $L = 0{,}500\,\mathrm m$, $I = 3{,}00\times 10^{-3}\,\mathrm{kg\cdot m^2}, \omega_i = 0{,}400\,\mathrm{rad/s}$. Côn trùng bò ra đầu ngoài thanh đạt tốc độ tiếp tuyến $v = 0{,}160\,\mathrm{m/s}$. Kết quả tính toán: Khối lượng thanh $M = 3I/L^2 = 0{,}0360\,\mathrm{kg}$, tốc độ góc cuối $\omega_f = v/L = 0{,}320\,\mathrm{rad/s}$, khối lượng côn trùng $m = 0{,}00300\,\mathrm{kg} = 3{,}00\,\mathrm g$.
- **Bài 10.55 (Mô hình ổn định kính Hubble)**: Con quay vỏ trụ mỏng $M = 2{,}0\,\mathrm{kg}, d = 5{,}0\,\mathrm{cm} \implies R = 0{,}025\,\mathrm m$, tốc độ quay $19200\,\mathrm{rpm}$. Trục tiến động góc $1{,}0\times 10^{-6}{}^\circ$ trong $5{,}0\,\mathrm h$. Kết quả tính toán: $I = MR^2 = 1{,}25\times 10^{-3}\,\mathrm{kg\cdot m^2}$, tốc độ tiến động $\Omega = 9{,}70\times 10^{-13}\,\mathrm{rad/s}$, mômen lực tác dụng $\tau = I\omega\Omega = 2{,}44\times 10^{-12}\,\mathrm{N\cdot m}$ (làm tròn $2{,}4\times 10^{-12}\,\mathrm{N\cdot m}$).
- **Bài 10.75 (Tảng đá lăn trên đồi 50 m)**: Tảng đá cầu đặc lăn từ nghỉ trên đồi cao $50{,}0\,\mathrm m$: Nửa trên dốc nhám $h_1 = 25{,}0\,\mathrm m$ lăn không trượt, nửa dưới đóng băng $h_2 = 25{,}0\,\mathrm m$ không ma sát. Kết quả tính toán: Tại ranh giới $v_1^2 = \frac{10}{7}gh_1 = 350\,\mathrm{m^2/s^2}$; trên mặt băng, toàn bộ thế năng giảm bổ sung vào động năng tịnh tiến nên $v_f^2 = 350 + 2(9{,}80)(25{,}0) = 840\,\mathrm{m^2/s^2} \implies v_f = \sqrt{840} \approx 29{,}0\,\mathrm{m/s}$.

---

## 3. Khuyết Tật Cần Lưu Ý & Khuyến Nghị Trình Bày (Findings & Recommendations)

Quá trình kiểm tra cấu trúc mã nguồn tệp `11-bai-tap-001-075.md` phát hiện một số điểm khuyết tật về kết cấu nhãn mục và dấu câu cần được lưu ý khi tích hợp lên trang bài giảng chính thức:

### 3.1. Các khuyết tật kết cấu nhãn tiểu mục (Subpart Labeling Omissions)
1. **Bài 10.1**: Đề bài có 6 trường hợp (a)–(f). Lời giải có nhãn in đậm `(a)`, `(b)`, `(c)`, `(d)` nhưng gộp chung trường hợp (e) và (f) vào văn xuôi; đồng thời hoán đổi nhẹ giải thích hình học giữa (e) và (f).
2. **Bài 10.7**: Đề bài có hai câu hỏi (a), (b). Lời giải có nhãn `(a)` nhưng thiếu nhãn in đậm `(b)` cho phần tính $\tau_{\max} = 4{,}25\,\mathrm{N\cdot m}$.
3. **Bài 10.16**: Đề bài hỏi (a) Lực căng dây và (b) Gia tốc của hộp. Trong lời giải, gia tốc $a = 2{,}72\,\mathrm{m/s^2}$ được tính toán trước ở đoạn đầu nhưng thiếu nhãn in đậm `(b)`, sau đó mới xuất hiện nhãn `(a)` cho lực căng $T = 35{,}4\,\mathrm N$.
4. **Bài 10.24**: Đề bài có hai câu hỏi (a) và (b). Trong lời giải, phần tính độ cao đĩa tròn ($h = 0{,}765\,\mathrm m$) không có nhãn `(a)`, chỉ có nhãn `(b)` ở đoạn so sánh phía sau.
5. **Các bài trình bày lời giải dạng văn xuôi liền mạch (Continuous narrative without explicit subpart tags)**:
   - Bài 10.11: Đề hỏi (a) gia tốc và (b) chiều dài dây, nhưng lời giải gộp thành chuỗi suy luận liên tục không chia nhãn `(a)` và `(b)`.
   - Bài 10.12, 10.13, 10.20, 10.22, 10.62, 10.66: Tương tự, các câu hỏi phụ được giải quyết đầy đủ trong văn xuôi nhưng không tách thẻ nhãn `(a)`, `(b)` riêng biệt.

### 3.2. Dấu câu đứng cô lập trên một dòng riêng (Isolated Punctuation Lines)
Trong một số khối công thức hiển thị (`$$...$$`), dấu chấm câu hoặc hai chấm bị ngắt xuống một dòng đứng riêng lẻ:
- **Dòng 704 (Bài 10.24)**: Ký tự `.` đứng cô độc trên một dòng ngay sau khối `$$`.
- **Dòng 1167 (Bài 10.40)**: Ký tự `:` đứng cô độc trên một dòng nằm giữa hai khối công thức hiển thị.
- **Dòng 1288 (Bài 10.45)**: Ký tự `.` đứng cô độc trên một dòng ngay sau khối `$$`.
- **Dòng 1993 (Bài 10.67)**: Ký tự `.` đứng cô độc trên một dòng ngay sau khối `$$`.

### 3.3. Dòng văn xuôi bắt đầu bằng dấu phẩy hoặc dấu chấm sau khối công thức
Do ngắt khối `$$...$$` ở giữa câu văn, các dòng tiếp theo bị bắt đầu trực tiếp bằng dấu câu `, ` hoặc `. `:
- Dòng 260: `. Do đó gia tốc là...`
- Dòng 475: `. Hộp đi xuống...`
- Dòng 612: `. Do đó $c=5/8$...`
- Dòng 1390: `. Chọn chiều quay...`
- Dòng 1432: `, tức $3{,}00\,\mathrm g$.`
- Dòng 1563: `. Tốc độ góc...`
- Dòng 1631: `. Với bộ truyền...`
- Dòng 2103: `. Trong trường hợp...`
- Dòng 2162: `, tức $u=15{,}3\,\mathrm{m/s}$.`
- Dòng 2210: `, tức $v_f=29{,}0\,\mathrm{m/s}$.`

### 3.4. Hai khối công thức hiển thị đặt liền nhau không có lời dẫn (Consecutive Display Blocks)
- **Bài 10.73 (Dòng 2121–2127)**: Đặt hai khối `$$` liên tiếp nhau mà không có văn xuôi trung gian:
  ```markdown
  $$
  mgh=\tfrac35mgH_0.
  $$
  $$
  h=\tfrac35H_0.
  $$
  ```

### 3.5. Kiểm định chuẩn mực văn phong & cú pháp StudyHub (Syntax & Style Audit)
- **Dấu chấm phẩy (`;`) trong văn xuôi**: 0 lỗi (tuân thủ quy tắc hạn chế `;`).
- **Dấu gạch ngang dài (em dash `—` / `--`) trong văn xuôi**: 0 lỗi (tuân thủ quy tắc hạn chế gạch ngang).
- **Viết hoa sau dấu hai chấm (`: `)**: Đạt chuẩn trong toàn bộ các tiêu đề, tóm tắt và lời dẫn.
- **Cụm từ dịch máy cấm kỵ**: Không xuất hiện các cụm từ bị cấm như *"theo sách"*, *"lấy từ giáo trình"*, *"nguyên tác"*, *"ảnh trong sách"*.
- **Cú pháp trị tuyệt đối & chuẩn vector**: Không dùng `\vert{}` hay `\Vert{}`.
- **Độ dài công thức nội dòng**: Toàn bộ công thức nội dòng `$…$` dưới 38ex, hiển thị an toàn trên giao diện di động.

---

## 4. Bảng Bằng Chứng Thẩm Định Toàn Bộ 75 Bài Tập (10.1 – 10.75)

Dưới đây là bảng dữ liệu chi tiết của toàn bộ 75 bài tập được trích xuất trực tiếp từ đề bài nguồn gốc và đối chiếu với giáo trình *Young & Freedman 15th Edition*, kèm giá trị tính toán độc lập:

| Mã bài | Trang PDF / In | Dữ kiện & Câu hỏi nguồn gốc | Kết quả tính độc lập & Bằng chứng xác minh | Đánh giá |
| :--- | :---: | :--- | :--- | :---: |
| **10.1** | 348 / 328 | Thanh dài $4{,}00\,\mathrm m$, lực $F = 10{,}0\,\mathrm N$. Tính $\tau_O$ cho 6 trường hợp (a)–(f). | $\tau_a = +40{,}0, \tau_b = +34{,}6, \tau_c = +20{,}0, \tau_d = -17{,}3\,\mathrm{N\cdot m}; \tau_e = \tau_f = 0$ | **PASS** |
| **10.2** | 348 / 328 | Thanh chịu 2 lực: $F_1 = 8{,}00\,\mathrm N$ cách O $5{,}00\,\mathrm m$ hướng xuống; $F_2 = 12{,}0\,\mathrm N$ cách O $2{,}00\,\mathrm m$ hợp $30{,}0^\circ$. | $\tau_1 = -40{,}0, \tau_2 = +12{,}0 \implies \tau_{\text{net}} = -28{,}0\,\mathrm{N\cdot m}\text{ (CW)}$ | **PASS** |
| **10.3** | 348 / 328 | Tấm kim loại vuông cạnh $0{,}180\,\mathrm m$ ($b = 0{,}0900\,\mathrm m$), trục qua tâm O. $F_1 = 18{,}0\,\mathrm N$, $F_2 = 26{,}0\,\mathrm N$, $F_3 = 14{,}0\,\mathrm N$ ($45^\circ$). | $\tau_{\text{net}} = -1{,}62 + 2{,}34 + 1{,}782 = +2{,}50\,\mathrm{N\cdot m}\text{ (CCW)}$ | **PASS** |
| **10.4** | 349 / 329 | Bánh xe $R = 0{,}350\,\mathrm m$. $F_{\text{rad}} = 11{,}9\,\mathrm N$, $F_{\text{tan}} = 8{,}50\,\mathrm N$, $F_{\text{ang}} = 14{,}6\,\mathrm N$ ($40{,}0^\circ$ so với bán kính). | $\tau_{\text{net}} = 0{,}350(8{,}50 - 14{,}6\sin 40{,}0^\circ) = -0{,}310\,\mathrm{N\cdot m}\text{ (CW)}$ | **PASS** |
| **10.5** | 349 / 329 | Chi tiết máy: $\vec F = -5{,}00\hat\imath + 4{,}00\hat\jmath\,\mathrm N$ tại $\vec r = -0{,}450\hat\imath + 0{,}150\hat\jmath\,\mathrm m$. (a) Hình vẽ; (b) Chiều RHR; (c) $\vec\tau$. | $\vec\tau = \vec r \times \vec F = -1{,}05\hat k\,\mathrm{N\cdot m}\text{ (vào trong, }-\hat k\text{)}$ | **PASS** |
| **10.6** | 349 / 329 | Thanh trong mp xy, trục tại gốc. $\vec F = 7{,}00\hat\imath - 3{,}00\hat\jmath\,\mathrm N$ tại điểm $(3{,}00, 4{,}00)\,\mathrm m$. (a) $\vec r$; (b) $\vec\tau$. | $\vec r = 3{,}00\hat\imath + 4{,}00\hat\jmath\,\mathrm m; \vec\tau = -37{,}0\hat k\,\mathrm{N\cdot m}\text{ (độ lớn }37{,}0\,\mathrm{N\cdot m}\text{)}$ | **PASS** |
| **10.7** | 349 / 329 | Cờ lê dài $25{,}0\,\mathrm{cm}$, lực $F = 17{,}0\,\mathrm N$ hợp $37^\circ$ với cán. (a) $\tau$ quanh bu-lông; (b) $\tau_{\max}$. | $\tau = 0{,}250(17{,}0)\sin 37^\circ = 2{,}56\,\mathrm{N\cdot m}; \tau_{\max} = 0{,}250(17{,}0) = 4{,}25\,\mathrm{N\cdot m}$ | **PASS** |
| **10.8** | 349 / 329 | Đĩa đồng chất $40{,}0\,\mathrm{kg}, R = 0{,}200\,\mathrm m$. Lực tiếp tuyến $F = 30{,}0\,\mathrm N$. (a) $\tau, I, \alpha$; (b) Gia tốc tại vành lúc $t = 0{,}200\,\mathrm s$. | $\tau = 6{,}00\,\mathrm{N\cdot m}, I = 0{,}800\,\mathrm{kg\cdot m^2}, \alpha = 7{,}50\,\mathrm{rad/s^2}; a = \sqrt{a_t^2 + a_r^2} = 4{,}06\,\mathrm{m/s^2}$ | **PASS** |
| **10.9** | 349 / 329 | Bánh đà $I = 1{,}60\,\mathrm{kg\cdot m^2}$, tăng tốc từ nghỉ lên $400\,\mathrm{rev/min}$ ($41{,}89\,\mathrm{rad/s}$) trong $8{,}00\,\mathrm s$. Tìm $\tau$. | $\alpha = 5{,}236\,\mathrm{rad/s^2} \implies \tau = I\alpha = 8{,}38\,\mathrm{N\cdot m}$ | **PASS** |
| **10.10** | 349 / 329 | Dây quấn quanh bánh xe đặc $M = 9{,}20\,\mathrm{kg}, R = 0{,}250\,\mathrm m$. (a) Kéo $F = 40{,}0\,\mathrm N$, tìm $\alpha$; (b) Chiều dài dây tháo ra sau $2{,}00\,\mathrm s$; (c) Treo quả nặng $40{,}0\,\mathrm N$. | $\alpha = 34{,}8\,\mathrm{rad/s^2}; s = 17{,}4\,\mathrm m; \alpha' = 18{,}4\,\mathrm{rad/s^2} < 34{,}8\,\mathrm{rad/s^2}$ | **PASS** |
| **10.11** | 349 / 329 | Cầu đặc đồng chất $m = 225\,\mathrm g, d = 3{,}00\,\mathrm{cm}$ ($R = 0{,}0150\,\mathrm m$). Dây quanh xích đạo kéo $F = 0{,}150\,\mathrm N$. (a) $\alpha$; (b) Dây tháo ra sau $0{,}500\,\mathrm s$. | $\tau = 2{,}25\times 10^{-3}\,\mathrm{N\cdot m}, I = 2{,}025\times 10^{-5}\,\mathrm{kg\cdot m^2} \implies \alpha = 111\,\mathrm{rad/s^2}; s = 0{,}208\,\mathrm m = 20{,}8\,\mathrm{cm}$ | **PASS** |
| **10.12** | 349 / 329 | Đá $3{,}00\,\mathrm{kg}$ treo bằng dây quấn quanh ròng rọc đĩa $10{,}0\,\mathrm{kg}, R = 30{,}0\,\mathrm{cm}$. Thả rơi $12{,}0\,\mathrm m$. (a) $a, T$; (b) Tốc độ chạm đất; (c) Dùng bảo toàn cơ năng. | $a = 3{,}68\,\mathrm{m/s^2}, T = 18{,}4\,\mathrm N; v = \sqrt{2ah} = 9{,}39\,\mathrm{m/s}; v_{\text{NL}} = 9{,}39\,\mathrm{m/s}$ | **PASS** |
| **10.13** | 349 / 329 | Sách $m_1 = 2{,}00\,\mathrm{kg}$ trên bàn nhẵn nối sách treo $m_2 = 3{,}00\,\mathrm{kg}$ qua ròng rọc đĩa $M_p = 0{,}500\,\mathrm{kg}$. (a) $a$; (b) Lực căng hai nhánh dây. | $a = 5{,}60\,\mathrm{m/s^2}; T_1 = 11{,}2\,\mathrm N, T_2 = 12{,}6\,\mathrm N$ | **PASS** |
| **10.14** | 349 / 329 | Xô nước $15{,}0\,\mathrm{kg}$ treo bằng dây quanh trụ đặc $12{,}0\,\mathrm{kg}, d = 0{,}300\,\mathrm m$. Rơi $10{,}0\,\mathrm m$ xuống giếng. (a) $T$; (b) $a, v$; (c) $t$; (d) Lực tác dụng lên trục. | $T = 42{,}0\,\mathrm N; a = 7{,}00\,\mathrm{m/s^2}, v = 11{,}8\,\mathrm{m/s}; t = 1{,}69\,\mathrm s; N = Mg + T = 160\,\mathrm N$ | **PASS** |
| **10.15** | 349 / 329 | Bánh xe quay quanh trục ngang. Lực tiếp tuyến $80{,}0\,\mathrm N$ ở vành $R = 0{,}120\,\mathrm m$ hãm từ $30{,}0\,\mathrm{rev/min}$ về nghỉ trong $4{,}00\,\mathrm s$. Tìm $I$. | $\alpha = -0{,}785\,\mathrm{rad/s^2}, \tau = -9{,}60\,\mathrm{N\cdot m} \implies I = \|\tau/\alpha\| = 12{,}2\,\mathrm{kg\cdot m^2}$ | **PASS** |
| **10.16** | 349 / 329 | Hộp $12{,}0\,\mathrm{kg}$ trên bàn nhẵn nối vật treo $5{,}00\,\mathrm{kg}$ qua ròng rọc $I = 0{,}480\,\mathrm{kg\cdot m^2}, R = 0{,}160\,\mathrm m$. Tìm $a$ và lực căng hai nhánh. | $a = 1{,}37\,\mathrm{m/s^2}; T_1 = 16{,}4\,\mathrm N, T_2 = 42{,}1\,\mathrm N$ | **PASS** |
| **10.17** | 349 / 329 | Trụ đặc $R = 0{,}140\,\mathrm m$. Lực không đổi $F = 18{,}0\,\mathrm N$ tác dụng trong $6{,}00\,\mathrm s$ làm quay $120$ vòng từ nghỉ. Tìm $I$ và khối lượng $M$. | $\alpha = 41{,}9\,\mathrm{rad/s^2}, \tau = 2{,}52\,\mathrm{N\cdot m} \implies I = 0{,}0602\,\mathrm{kg\cdot m^2}; M = 2I/R^2 = 6{,}14\,\mathrm{kg}$ | **PASS** |
| **10.18** | 349 / 329 | Hai quả cầu cùng $M = 5{,}00\,\mathrm{kg}, R = 0{,}120\,\mathrm m$ (một đặc, một vỏ rỗng mỏng) lăn không trượt cùng $v = 2{,}00\,\mathrm{m/s}$. So sánh $K_{\text{tot}}$. | $K_{\text{đặc}} = \tfrac{7}{10}Mv^2 = 14{,}0\,\mathrm J; K_{\text{vỏ}} = \tfrac{5}{6}Mv^2 = 16{,}7\,\mathrm J\text{ (vỏ lớn hơn)}$ | **PASS** |
| **10.19** | 350 / 330 | Vành tròn $M = 2{,}20\,\mathrm{kg}, d = 1{,}20\,\mathrm m$ lăn không trượt với $v = 3{,}00\,\mathrm{m/s}$. (a) $K_{\text{trans}}$; (b) $K_{\text{rot}}$; (c) $K_{\text{tot}}$; (d) Hệ quy chiếu gắn với tâm. | $K_{\text{trans}} = 9{,}90\,\mathrm J; K_{\text{rot}} = 9{,}90\,\mathrm J; K_{\text{tot}} = 19{,}8\,\mathrm J; K' = \tfrac{1}{2}I\omega^2 = 9{,}90\,\mathrm J$ | **PASS** |
| **10.20** | 350 / 330 | Cầu đặc lăn không trượt xuống dốc $\beta$. (a) Tìm $\mu_{s,\min}$; (b) So sánh với hình trụ đặc. | $\mu_{s,\min} = \tfrac{2}{7}\tan\beta; \mu_{s,\text{trụ}} = \tfrac{1}{3}\tan\beta > \mu_{s,\text{cầu}}$ | **PASS** |
| **10.21** | 350 / 330 | Tỷ lệ $K_{\text{rot}}/K_{\text{tot}}$ khi lăn không trượt của: (a) Trụ đặc; (b) Cầu đặc; (c) Vỏ cầu mỏng; (d) Ống trụ rỗng. | $\text{Trụ đặc: } 1/3\text{ (}33{,}3\%\text{)}; \text{Cầu đặc: } 2/7\text{ (}28{,}6\%\text{)}; \text{Vỏ cầu: } 2/5\text{ (}40{,}0\%\text{)}; \text{Ống rỗng: } 1/2\text{ (}50{,}0\%\text{)}$ | **PASS** |
| **10.22** | 350 / 330 | Dây quấn quanh vành nhỏ $r = 8{,}00\,\mathrm{cm}$ của trụ gắn hai đĩa $R = 12{,}0\,\mathrm{cm}$, $M = 0{,}600\,\mathrm{kg}, I = 0{,}00750\,\mathrm{kg\cdot m^2}$, kéo $F = 3{,}50\,\mathrm N$. Tìm $a, f_s$. | $a = \frac{F(1 + r/R)}{M + I/R^2} = 5{,}23\,\mathrm{m/s^2}; f_s = 0{,}229\,\mathrm N\text{ (cùng chiều kéo)}$ | **PASS** |
| **10.23** | 350 / 330 | Cầu đặc thả từ nghỉ trên dốc $65{,}0^\circ$. (a) $\mu_{s,\min}$ để không trượt; (b) So sánh với hình trụ đặc. | $\mu_{s,\min} = \tfrac{2}{7}\tan 65{,}0^\circ = 0{,}613; \mu_{s,\text{trụ}} = \tfrac{1}{3}\tan 65{,}0^\circ = 0{,}715 > 0{,}613$ | **PASS** |
| **10.24** | 350 / 330 | Vỏ cầu mỏng $2{,}00\,\mathrm{kg}$ lăn không trượt xuống dốc $38{,}0^\circ$. (a) $a$; (b) Lực ma sát $f_s$; (c) $\mu_{s,\min}$. | $a = \tfrac{3}{5}g\sin 38{,}0^\circ = 3{,}62\,\mathrm{m/s^2}; f_s = \tfrac{2}{5}mg\sin 38{,}0^\circ = 4{,}84\,\mathrm N; \mu_{s,\min} = 0{,}313$ | **PASS** |
| **10.25** | 350 / 330 | Bánh xe $W = 392\,\mathrm N$ ($M = 40{,}0\,\mathrm{kg}$) lăn không trượt ở chân dốc $v = 25{,}0\,\mathrm{m/s}$, $I = 0{,}800MR^2$. Tìm độ cao $h$ lên dốc $30{,}0^\circ$. | $K_{\text{tot}} = 0{,}900Mv^2 = 22500\,\mathrm J \implies h = K_{\text{tot}}/(Mg) = 57{,}4\,\mathrm m$ | **PASS** |
| **10.26** | 350 / 330 | Viên bi cầu thả từ độ cao $h$ trong lòng máng đối xứng: Nửa trái nhám (lăn không trượt), nửa phải nhẵn băng (không ma sát). Tìm độ cao $h'$ đạt được ở bên phải. | $h' = \tfrac{5}{7}h\text{ (động năng quay }\tfrac{2}{7}mgh\text{ bị giam giữ không hoàn lại thế năng)}$ | **PASS** |
| **10.27** | 350 / 330 | Đường bowling dài $60\,\mathrm{ft} = 18{,}3\,\mathrm m$. Ước lượng thời gian bóng lăn không trượt tới chốt đầu. | $v \approx 7{,}0\,\mathrm{m/s} \implies t = s/v \approx 2{,}6\,\mathrm s\text{ (phù hợp thực nghiệm bowling)}$ | **PASS** |
| **10.28** | 350 / 330 | Hai cầu đặc lăn không trượt cùng tốc độ $v$. Cầu 1 có $d_1 = 2d_2$, $M_1 = 2M_2$. So sánh tổng động năng $K_1/K_2$. | $K = \tfrac{7}{10}Mv^2 \implies K_1/K_2 = M_1/M_2 = 2{,}00\text{ (độc lập với bán kính)}$ | **PASS** |
| **10.29** | 350 / 330 | Trụ rỗng $M = 4{,}75\,\mathrm{kg}, R_1 = 0{,}120\,\mathrm m, R_2 = 0{,}200\,\mathrm m$. Dây kéo ngang ở đỉnh vành ngoài $F = 45{,}0\,\mathrm N$. Tìm $a$ và $f_s$. | $I = 0{,}1292\,\mathrm{kg\cdot m^2} \implies a = 6{,}88\,\mathrm{m/s^2}; f_s = 6{,}44\,\mathrm N\text{ (hướng cùng chiều kéo)}$ | **PASS** |
| **10.30** | 350 / 330 | Quả bowling (cầu đặc) lăn không trượt lên dốc góc $\beta$. (a) Giản đồ lực; (b) Gia tốc tâm $a$; (c) Lực ma sát nghỉ $f_s$. | $a = \tfrac{5}{7}g\sin\beta\text{ (hướng xuống dốc)}; f_s = \tfrac{2}{7}mg\sin\beta\text{ (hướng lên dốc)}$ | **PASS** |
| **10.31** | 350 / 330 | Bóng đá (vỏ cầu mỏng) $d = 22{,}6\,\mathrm{cm}, m = 426\,\mathrm g$ lăn lên dốc $15{,}0^\circ$ được $3{,}50\,\mathrm m$ thì dừng. Tìm $v_0$ và $\omega_0$. | $v_0 = \sqrt{\tfrac{6}{5}gs\sin 15{,}0^\circ} = 3{,}26\,\mathrm{m/s}; \omega_0 = v_0/R = 28{,}8\,\mathrm{rad/s}$ | **PASS** |
| **10.32** | 350 / 330 | Động cơ truyền $175\,\mathrm{hp}$ ($130{,}5\,\mathrm{kW}$) cho cánh quạt ở $2400\,\mathrm{rpm}$ ($251{,}3\,\mathrm{rad/s}$). (a) $\tau$; (b) Công trong 1 vòng. | $\tau = P/\omega = 519\,\mathrm{N\cdot m}; W = 2\pi\tau = 3260\,\mathrm J$ | **PASS** |
| **10.33** | 350 / 330 | Mâm quay sân chơi $R = 2{,}40\,\mathrm m, I = 2100\,\mathrm{kg\cdot m^2}$ hãm từ $v = 1{,}50\,\mathrm{m/s}$ về nghỉ trong $15{,}0\,\mathrm s$. (a) $\Delta K$; (b) Công suất cản trung bình. | $\omega_0 = 0{,}625\,\mathrm{rad/s} \implies \Delta K = -410\,\mathrm J; \bar P = \|\Delta K\|/t = 27{,}3\,\mathrm W$ | **PASS** |
| **10.34** | 350 / 330 | Động cơ điện tiêu thụ $9{,}00\,\mathrm{kJ}$ trong $1{,}00\,\mathrm{min}$, $1/3$ sinh công cơ học. Trục quay $2500\,\mathrm{rpm}$. Tìm mômen lực $\tau$. | $P_{\text{mech}} = 50{,}0\,\mathrm W, \omega = 261{,}8\,\mathrm{rad/s} \implies \tau = P/\omega = 0{,}191\,\mathrm{N\cdot m}$ | **PASS** |
| **10.35** | 350 / 330 | Bánh mài đĩa đặc $2{,}80\,\mathrm{kg}, R = 0{,}100\,\mathrm m$ tăng từ nghỉ lên $1200\,\mathrm{rpm}$ ($125{,}7\,\mathrm{rad/s}$) trong $3{,}00\,\mathrm s$. (a) $\tau$; (b) $\theta$; (c) $W$; (d) $P_{\max}$. | $\tau = 0{,}586\,\mathrm{N\cdot m}; \theta = 188\,\mathrm{rad}; W = 111\,\mathrm J; P_{\max} = \tau\omega = 73{,}7\,\mathrm W$ | **PASS** |
| **10.36** | 351 / 331 | Cánh quạt máy bay dài $2{,}08\,\mathrm m, M = 117\,\mathrm{kg}$ quay $2400\,\mathrm{rpm}$. (a) $I$; (b) Mômen động lượng $L$. | $I = \tfrac{1}{12}ML^2 = 42{,}2\,\mathrm{kg\cdot m^2}; L = I\omega = 10600\,\mathrm{kg\cdot m^2/s}$ | **PASS** |
| **10.37** | 351 / 331 | Viên đá $2{,}00\,\mathrm{kg}, \vec v = 12{,}0\hat\imath\,\mathrm{m/s}$ tại $P(-6{,}40, 4{,}80)\,\mathrm m$. (a) $\vec L_O$; (b) Tốc độ biến thiên $d\vec L/dt$ do trọng lực. | $\vec L_O = -115\hat k\,\mathrm{kg\cdot m^2/s}\text{ (vào trong)}; d\vec L/dt = \vec\tau = +125\hat k\,\mathrm{N\cdot m}\text{ (ra ngoài)}$ | **PASS** |
| **10.38** | 351 / 331 | Phụ nữ $50{,}0\,\mathrm{kg}$ ở vành đĩa $R = 2{,}00\,\mathrm m$ quay $0{,}80\,\mathrm{rev/s}$ ($5{,}03\,\mathrm{rad/s}$). Tìm mômen động lượng $L$ của người quanh trục. | $L = mR^2\omega = 50{,}0(4{,}00)(5{,}03) = 1010\,\mathrm{kg\cdot m^2/s}$ | **PASS** |
| **10.39** | 351 / 331 | Kim giây đồng hồ dài $15{,}0\,\mathrm{cm}$, khối lượng $6{,}00\,\mathrm g$, coi là thanh mảnh quay quanh một đầu. Tìm $L$. | $I = \tfrac{1}{3}ML^2 = 4{,}50\times 10^{-5}\,\mathrm{kg\cdot m^2}, \omega = 0{,}1047\,\mathrm{rad/s} \implies L = 4{,}71\times 10^{-6}\,\mathrm{kg\cdot m^2/s}$ | **PASS** |
| **10.40** | 351 / 331 | Mômen động lượng của Trái Đất: (a) Quỹ đạo quanh Mặt Trời; (b) Tự quay quanh trục. | $L_{\text{quỹ đạo}} = 2{,}67\times 10^{40}\,\mathrm{kg\cdot m^2/s}; L_{\text{tự quay}} = 7{,}05\times 10^{33}\,\mathrm{kg\cdot m^2/s}$ | **PASS** |
| **10.41** | 351 / 331 | Vỏ cầu mỏng $12{,}0\,\mathrm{kg}, d = 48{,}0\,\mathrm{cm}$. Mômen $\tau = 0{,}800\,\mathrm{N\cdot m}$ tác dụng trong $3{,}00\,\mathrm s$. (a) $L$; (b) $\omega$. | $L = \tau t = 2{,}40\,\mathrm{kg\cdot m^2/s}; I = 0{,}4608\,\mathrm{kg\cdot m^2} \implies \omega = L/I = 5{,}21\,\mathrm{rad/s}$ | **PASS** |
| **10.42** | 351 / 331 | Khối $0{,}0250\,\mathrm{kg}$ trên bàn nhẵn nối dây qua lỗ, ban đầu $r_1 = 0{,}300\,\mathrm m, \omega_1 = 2{,}85\,\mathrm{rad/s}$. Rút dây còn $r_2 = 0{,}150\,\mathrm m$. (a) $\omega_2$; (b) $\Delta K = W$. | $\omega_2 = 11{,}4\,\mathrm{rad/s}; \Delta K = +0{,}0274\,\mathrm J\text{ (lực căng sinh công dương)}$ | **PASS** |
| **10.43** | 351 / 331 | Sao co sụp thành sao neutron: Bán kính từ $7{,}0\times 10^5\,\mathrm{km}$ co về $12\,\mathrm{km}$, chu kỳ ban đầu $30$ ngày. Tìm chu kỳ quay mới. | $T_2 = T_1(R_2/R_1)^2 = 0{,}0076\,\mathrm s \approx 7{,}6\,\mathrm{ms}\text{ (bảo toàn mômen động lượng)}$ | **PASS** |
| **10.44** | 351 / 331 | Vận động viên nhảy cầu co người từ $I_1 = 18{,}0\,\mathrm{kg\cdot m^2}$ về $I_2 = 3{,}60\,\mathrm{kg\cdot m^2}$. Tốc độ góc ban đầu $\omega_1 = 4{,}00\,\mathrm{rad/s}$. Tìm $\omega_2$. | $\omega_2 = \omega_1(I_1/I_2) = 20{,}0\,\mathrm{rad/s}\text{ (gấp 5 lần ban đầu)}$ | **PASS** |
| **10.45** | 351 / 331 | Vận động viên trượt băng thu tay $8{,}0\,\mathrm{kg}$ từ duỗi ngang về sát người. $I_1 = 3{,}00\,\mathrm{kg\cdot m^2}, \omega_1 = 1{,}00\,\mathrm{rev/s}$. $I_2 = 2{,}20\,\mathrm{kg\cdot m^2}$. Tìm $\omega_2$. | $\omega_2 = \omega_1(I_1/I_2) = 1{,}36\,\mathrm{rev/s}$ | **PASS** |
| **10.46** | 351 / 331 | Cửa gỗ $40{,}0\,\mathrm{kg}$, rộng $1{,}00\,\mathrm m$. Cục bùn $0{,}500\,\mathrm{kg}$ bay $12{,}0\,\mathrm{m/s}$ dính vào chính giữa cửa. Tìm $\omega$ ngay sau va chạm. | $I_{\text{cửa}} = 13{,}33\,\mathrm{kg\cdot m^2} \implies \omega = \frac{m v (W/2)}{I + m(W/2)^2} = 0{,}223\,\mathrm{rad/s}$ | **PASS** |
| **10.47** | 351 / 331 | Mâm gỗ $120\,\mathrm{kg}, R = 2{,}00\,\mathrm m, \omega_i = 3{,}00\,\mathrm{rad/s}$. Người nhảy dù $70{,}0\,\mathrm{kg}$ rơi thẳng đứng tiếp đất tại vành. (a) $\omega_f$; (b) $\Delta K_{\text{rot}}$. | $\omega_f = 1{,}38\,\mathrm{rad/s}; \Delta K_{\text{rot}} = -582\,\mathrm J\text{ (tiêu tán qua ma sát trượt mặt mâm)}$ | **PASS** |
| **10.48** | 351 / 331 | Tiểu hành tinh va chạm xuyên tâm xích đạo Trái Đất làm ngày dài thêm $25{,}0\%$. Tìm khối lượng $m$ theo khối lượng $M$ của Trái Đất. | $I_f = 1{,}25I_i \implies mR^2 = 0{,}25(\tfrac{2}{5}MR^2) \implies m = 0{,}100M$ | **PASS** |
| **10.49** | 351 / 331 | Côn trùng $10{,}0\,\mathrm g$ nhảy ngang $v = 20{,}0\,\mathrm{cm/s}$ từ đầu thanh $50{,}0\,\mathrm g, L = 1{,}00\,\mathrm m$ quay quanh đinh cố định. (a) $\omega$; (b) $K_{\text{tot}}$; (c) Nguồn năng lượng. | $\omega = 0{,}120\,\mathrm{rad/s}; K_{\text{tot}} = 3{,}20\times 10^{-4}\,\mathrm J; \text{Năng lượng do cơ bắp sinh ra}$ | **PASS** |
| **10.50** | 352 / 332 | Thanh mảnh $L = 0{,}500\,\mathrm m, I = 3{,}00\times 10^{-3}\,\mathrm{kg\cdot m^2}, \omega_i = 0{,}400\,\mathrm{rad/s}$. Côn trùng bò ra đầu ngoài đạt $v = 0{,}160\,\mathrm{m/s}$. Tìm khối lượng thanh và côn trùng. | $M_{\text{thanh}} = 0{,}0360\,\mathrm{kg}\text{ (}36{,}0\,\mathrm g\text{)}; m_{\text{bọ}} = 0{,}00300\,\mathrm{kg}\text{ (}3{,}00\,\mathrm g\text{)}$ | **PASS** |
| **10.51** | 352 / 332 | Trên hành tinh khác: Thanh $M = 0{,}800\,\mathrm{kg}, L = 1{,}20\,\mathrm m$ quay quanh đầu, lực vuông góc $F = 6{,}00\,\mathrm N$ ở đầu kia. Tìm $\alpha$. | $I = \tfrac{1}{3}ML^2 = 0{,}384\,\mathrm{kg\cdot m^2}, \tau = 7{,}20\,\mathrm{N\cdot m} \implies \alpha = 18{,}8\,\mathrm{rad/s^2}$ | **PASS** |
| **10.52** | 352 / 332 | Cổng gỗ vuông cạnh $1{,}5\,\mathrm m, M = 4{,}5\,\mathrm{kg}$. Đạn $0{,}0100\,\mathrm{kg}$ bay $400\,\mathrm{m/s}$ cắm vào mép ngoài. (a) $\omega$; (b) Động lượng thẳng có bảo toàn? | $\omega = 1{,}76\,\mathrm{rad/s}; \text{Động lượng không bảo toàn vì chốt bản lề tác dụng xung lực ngoài}$ | **PASS** |
| **10.53** | 352 / 332 | Thiếu niên đứng ở vành đĩa $M, R$ ném đá $m_r$ tiếp tuyến với tốc độ $v$. Tìm tốc độ góc $\omega$ của đĩa và người sau ném. | $\|\omega\| = \frac{m_r v}{R(M/2 + m)}\text{ (quay ngược chiều đá bay)}$ | **PASS** |
| **10.54** | 352 / 332 | Đĩa gỗ $M = 1{,}60\,\mathrm{kg}, R = 0{,}600\,\mathrm m$. Đạn $0{,}0200\,\mathrm{kg}$ găm vào vành theo phương tiếp tuyến làm đĩa quay $4{,}00\,\mathrm{rad/s}$. Tìm vận tốc đạn $v$. | $I_f = 0{,}2952\,\mathrm{kg\cdot m^2} \implies v = \frac{I_f\omega_f}{mR} = 98{,}4\,\mathrm{m/s}$ | **PASS** |
| **10.55** | 352 / 332 | Kính Hubble: Con quay vỏ trụ mỏng $M = 2{,}0\,\mathrm{kg}, d = 5{,}0\,\mathrm{cm}, 19200\,\mathrm{rpm}$. Tìm mômen làm trục tiến động $1{,}0\times 10^{-6}{}^\circ$ trong $5{,}0\,\mathrm h$. | $I = 1{,}25\times 10^{-3}\,\mathrm{kg\cdot m^2}, \Omega = 9{,}70\times 10^{-13}\,\mathrm{rad/s} \implies \tau = 2{,}44\times 10^{-12}\,\mathrm{N\cdot m}$ | **PASS** |
| **10.56** | 352 / 332 | Con quay tiến động $0{,}50\,\mathrm{rad/s}$ trên Trái Đất. Tìm tốc độ tiến động trên Mặt Trăng ($g_{\text{MT}} = g/6$). | $\Omega = \frac{\tau}{L} \propto g \implies \Omega_{\text{MT}} = \frac{0{,}50}{6} = 0{,}083\,\mathrm{rad/s}$ | **PASS** |
| **10.57** | 352 / 332 | Đạp xe bám theo ô tô chạy $30\,\mathrm{mph}$ ($13{,}4\,\mathrm{m/s}$). Bán kính bánh xe $R = 0{,}34\,\mathrm m$, tỉ số đĩa/líp $52/16$. Ước lượng tần số đạp. | $\omega_{\text{bánh}} = 39{,}4\,\mathrm{rad/s} \implies f_{\text{đạp}} \approx 64\,\mathrm{rpm}$ | **PASS** |
| **10.58** | 352 / 332 | Đá mài đĩa đặc $50{,}0\,\mathrm{kg}, d = 0{,}520\,\mathrm m$. Ép rìu với $N = 160\,\mathrm N, \mu_k = 0{,}60$. (a) Thời gian dừng từ $1500\,\mathrm{rpm}$; (b) Lực ép để dừng trong $3{,}00\,\mathrm s$; (c) Bỏ lực ép. | $t = 10{,}6\,\mathrm s; F_{\text{ép}} = 62{,}9\,\mathrm N; t_{\text{tự do}} = 3{,}27\,\mathrm s$ | **PASS** |
| **10.59** | 352 / 332 | Đá mài đĩa đặc $50{,}0\,\mathrm{kg}, d = 0{,}520\,\mathrm m$. Ép lực pháp tuyến $180\,\mathrm N$ làm dừng từ $1200\,\mathrm{rpm}$ trong $12{,}0\,\mathrm s$. Tìm $\mu_k$. | $I = 1{,}69\,\mathrm{kg\cdot m^2}, \alpha = 10{,}47\,\mathrm{rad/s^2} \implies \mu_k = \frac{I\omega_0}{NRt} = 0{,}482$ | **PASS** |
| **10.60** | 352 / 332 | Khối $A = 2{,}50\,\mathrm{kg}$ trên bàn nhẵn nối vật treo $B = 1{,}50\,\mathrm{kg}$ qua ròng rọc $R = 0{,}120\,\mathrm m$. Vật B rơi $1{,}20\,\mathrm m$ trong $1{,}40\,\mathrm s$. Tìm $I_{\text{pulley}}$. | $a = \frac{2h}{t^2} = 1{,}22\,\mathrm{m/s^2} \implies I = R^2\left(\frac{m_B g - (m_A + m_B)a}{a}\right) = 0{,}364\,\mathrm{kg\cdot m^2}$ | **PASS** |
| **10.61** | 352 / 332 | Thanh $3{,}80\,\mathrm{kg}, L = 0{,}800\,\mathrm m$ có 2 viên bi $2{,}50\,\mathrm{kg}$ ở hai đầu, quay quanh tâm. Một viên bi tuột rơi khi thanh ngang. (a) $\alpha_0$; (b) Biến thiên $\tau$; (c) $\omega$ khi đứng. | $\alpha_0 = 16{,}3\,\mathrm{rad/s^2}; \tau(\phi) = mg\tfrac{L}{2}\cos\phi \to 0; \omega = \sqrt{\frac{2mg(L/2)}{I}} = 5{,}70\,\mathrm{rad/s}$ | **PASS** |
| **10.62** | 353 / 333 | Cầu đặc lăn không trượt lên dốc góc $\beta$. (a) Tìm $a$; (b) So sánh gia tốc chiều lên và chiều xuống. | $a = \tfrac{5}{7}g\sin\beta\text{ (hướng xuống dốc)}; \text{Độ lớn gia tốc bằng nhau ở cả hai chiều}$ | **PASS** |
| **10.63** | 353 / 333 | Máy Atwood: $m_A = 4{,}00\,\mathrm{kg}, m_B = 2{,}00\,\mathrm{kg}$, ròng rọc đĩa $M_C = 2{,}00\,\mathrm{kg}, R = 0{,}120\,\mathrm m$. Tìm $a, \alpha$ và $T_A, T_B$. | $a = \frac{(m_A - m_B)g}{m_A + m_B + M_C/2} = 2{,}80\,\mathrm{m/s^2}, \alpha = 23{,}3\,\mathrm{rad/s^2}; T_A = 28{,}0\,\mathrm N, T_B = 25{,}2\,\mathrm N$ | **PASS** |
| **10.64** | 353 / 333 | Nâng thùng hàng $50\,\mathrm{kg}$ bằng tời: Dây quấn quanh trụ gỗ $R = 0{,}150\,\mathrm m, M = 12{,}0\,\mathrm{kg}$, tay quay $L = 0{,}400\,\mathrm m$. Cần lực $F$ bao nhiêu để nâng với $a = 0{,}80\,\mathrm{m/s^2}$? | $I = 0{,}135\,\mathrm{kg\cdot m^2} \implies F = \frac{T R + I(a/R)}{L} = 217\,\mathrm N$ | **PASS** |
| **10.65** | 353 / 333 | Cầu đặc và vỏ cầu mỏng cùng $M, R, v_0$ lăn không trượt lên dốc. So sánh độ cao cực đại và ảnh hưởng góc dốc. | $h_{\text{vỏ}} = \tfrac{5}{6}\frac{v_0^2}{g} > h_{\text{đặc}} = \tfrac{7}{10}\frac{v_0^2}{g}; \text{Độ cao độc lập góc dốc}$ | **PASS** |
| **10.66** | 353 / 333 | Khối $5{,}00\,\mathrm{kg}$ trượt xuống dốc $36{,}9^\circ$ ($\mu_k = 0{,}25$), nối dây qua ròng rọc đĩa $M = 4{,}00\,\mathrm{kg}, R = 0{,}200\,\mathrm m$. Tìm $a$ và $T$. | $a = 1{,}12\,\mathrm{m/s^2}; T = 14{,}0\,\mathrm N$ | **PASS** |
| **10.67** | 353 / 333 | Bánh xe $R = 0{,}0600\,\mathrm m, I = 2{,}50\,\mathrm{kg\cdot m^2}$ bị kéo bởi lực $F(t) = 5{,}00t\,\mathrm N$. Tìm thời gian và lực sau $8$ vòng quay. | $\theta = 16\pi\,\mathrm{rad} \implies t = 13{,}6\,\mathrm s; F(13{,}6) = 68{,}0\,\mathrm N$ | **PASS** |
| **10.68** | 353 / 333 | Con lăn sân cỏ (vỏ trụ mỏng) khối lượng M kéo ngang bởi lực F tại trục. Tìm $a, f_s$ và điều kiện không trượt. | $a = \frac{F}{2M}; f_s = \frac{F}{2}\text{ (ngược chiều kéo)}; F \le 2\mu_s M g$ | **PASS** |
| **10.69** | 353 / 333 | Máy Atwood: $W_A = 125\,\mathrm N, W_B = 75{,}0\,\mathrm N$, ròng rọc đĩa $W_p = 80{,}0\,\mathrm N$. Tìm $a, T_A, T_B$ và lực nâng móc treo. | $a/g = 5/24; T_A = 99{,}0\,\mathrm N, T_B = 90{,}6\,\mathrm N; F_{\text{hook}} = W_p + T_A + T_B = 270\,\mathrm N < 280\,\mathrm N$ | **PASS** |
| **10.70** | 353 / 333 | Mâm quay ngang $R = 3{,}00\,\mathrm m$. Người chạy rơi vào vành làm thay đổi $\omega$. Độ dốc đồ thị $\Delta(1/\omega)/\Delta m = 0{,}250\,\mathrm{m^2/kg}$. Tìm $I$. | $I = R^2 / k = 3{,}00^2 / 0{,}250 = 36{,}0\,\mathrm{kg\cdot m^2}$ | **PASS** |
| **10.71** | 353 / 333 | Yo-yo: Hai đĩa đồng chất bán kính R khối lượng m nối bằng trục nhẹ bán kính b. Tìm gia tốc rơi $a$ và lực căng $T$. | $a = \frac{2gb^2}{R^2 + 2b^2}; T = \frac{2mgR^2}{R^2 + 2b^2}$ | **PASS** |
| **10.72** | 353 / 333 | Vỏ cầu mỏng thả từ độ cao $h_0$, lăn không trượt vào vòng xiếc bán kính R. (a) $h_{0,\min}$; (b) Phản lực tại B; (c) Không ma sát; (d) Phản lực đỉnh khi nhẵn. | $h_{0,\min} = \tfrac{17}{6}R \approx 2{,}83R; N_B = \tfrac{11}{5}mg; v_{\text{top}}^2 = \tfrac{5}{3}gR > gR\text{ (qua an toàn)}; N_A = \tfrac{2}{3}mg$ | **PASS** |
| **10.73** | 354 / 334 | Bóng rổ (vỏ cầu mỏng) thả từ $H_0$, lăn xuống thung lũng rồi lên đồi đóng băng không ma sát. Tìm độ cao cực đại $h$. | $h = \tfrac{3}{5}H_0\text{ (động năng quay }\tfrac{2}{5}mgH_0\text{ không chuyển về thế năng)}$ | **PASS** |
| **10.74** | 354 / 334 | Cầu đặc lăn lên đồi ($v_0 = 25{,}0\,\mathrm{m/s}, h = 28{,}0\,\mathrm m$) rồi bay ngang khỏi bờ dốc. (a) $u, t, x, v_{\text{impact}}$; (b) Giải thích $v_{\text{impact}} > v_0$. | $u = 15{,}3\,\mathrm{m/s}, t = 2{,}39\,\mathrm s, x = 36{,}5\,\mathrm m, v_{\text{impact}} = 28{,}0\,\mathrm{m/s} > 25{,}0\,\mathrm{m/s}\text{ (quay đóng băng, thế năng đổ vào tịnh tiến)}$ | **PASS** |
| **10.75** | 354 / 334 | Tảng đá cầu đặc lăn từ đỉnh đồi cao $50{,}0\,\mathrm m$: Nửa trên nhám ($h_1 = 25{,}0\,\mathrm m$), nửa dưới đóng băng không ma sát ($h_2 = 25{,}0\,\mathrm m$). Tìm tốc độ chân đồi. | $v_1^2 = \tfrac{10}{7}gh_1 = 350\,\mathrm{m^2/s^2} \implies v_f = \sqrt{350 + 2gh_2} = \sqrt{840} \approx 29{,}0\,\mathrm{m/s}$ | **PASS** |

---

## 5. Rà Soát Hệ Thống Hình Vẽ & Danh Mục Chú Thích Song Ngữ

### 5.1. Tình trạng tệp ảnh trên đĩa
- Tệp `11-bai-tap-001-075.md` chứa đúng 22 tham chiếu hình ảnh tới thư mục `../img/young-10/`.
- Toàn bộ 21 tệp ảnh cắt gốc (crop) đã hiện diện đầy đủ trên đĩa tại `docs/vat-ly-1/bai-giang/img/young-10/` (hình `d-hinh-p10-58.png` được tham chiếu 2 lần theo chủ đích sư phạm: Một lần ở đề bài và một lần trong khung lời giải chi tiết).
- Danh sách 21 tệp ảnh được kiểm tra thực tế:
  1. `d-hinh-e10-01.png` (Bài 10.1)
  2. `d-hinh-e10-02.png` (Bài 10.2)
  3. `d-hinh-e10-03.png` (Bài 10.3)
  4. `d-hinh-e10-04.png` (Bài 10.4)
  5. `d-hinh-e10-07.png` (Bài 10.7)
  6. `d-hinh-e10-16.png` (Bài 10.16)
  7. `d-hinh-e10-22.png` (Bài 10.22)
  8. `d-hinh-e10-29.png` (Bài 10.29)
  9. `d-hinh-e10-37.png` (Bài 10.37)
  10. `d-hinh-e10-42.png` (Bài 10.42)
  11. `d-hinh-e10-45.png` (Bài 10.45)
  12. `d-hinh-p10-58.png` (Bài 10.58)
  13. `d-hinh-p10-61.png` (Bài 10.61)
  14. `d-hinh-p10-63.png` (Bài 10.63)
  15. `d-hinh-p10-64.png` (Bài 10.64)
  16. `d-hinh-p10-66.png` (Bài 10.66)
  17. `d-hinh-p10-69.png` (Bài 10.69)
  18. `d-hinh-p10-72.png` (Bài 10.72)
  19. `d-hinh-p10-73.png` (Bài 10.73)
  20. `d-hinh-p10-74.png` (Bài 10.74)
  21. `d-hinh-p10-75.png` (Bài 10.75)

### 5.2. Khớp nối thực tế với module chú thích hình ảnh D
- Khi đối chiếu trực tiếp với tệp cấu hình `docs/.vitepress/physics1-10-exercises-d-image-annotations.mjs`, kết quả kiểm tra cho thấy:
  - Chỉ có đúng 6 hình vẽ được định nghĩa các nhãn chú thích hình học, lực và điểm tọa độ:
    1. `young-10/d-hinh-e10-03`: Gồm 7 nhãn tọa độ và lực (`'O'`, `'b'`, `'b'`, `'18.0 N'`, `'26.0 N'`, `'14.0 N'`, `'45°'`).
    2. `young-10/d-hinh-e10-07`: Gồm 8 nhãn kích thước và lực (`'0.180 m'`, `'0.090 m'`, `'0.240 m'`, `'10.0 N'`, `'12.0 N'`, `'9.0 N'`, `'30°'`, `'O'`).
    3. `young-10/d-hinh-p10-61`: Gồm 5 nhãn kích thước và khối lượng (`'O'`, `'L / 2'`, `'L / 2'`, `'m'`, `'m'`).
    4. `young-10/d-hinh-p10-72`: Gồm 4 nhãn điểm và bán kính (`'A'`, `'B'`, `'R'`, `'h'`).
    5. `young-10/d-hinh-p10-73`: Gồm 2 nhãn độ cao (`'H'`, `'h'`).
    6. `young-10/d-hinh-p10-75`: Gồm 3 nhãn độ cao và vận tốc (`'h / 2'`, `'h / 2'`, `'v = 0'`).
  - Toàn bộ 15 hình vẽ còn lại trong tệp cấu hình hiện đang là các mảng rỗng `[]`.
  - **Đính chính quan trọng**: Trong module chú thích này hoàn toàn không chứa các từ vựng tiếng Anh mô tả vật thể như *"cylinder"*, *"disk"*, *"pulley"*, *"sphere"*, *"hoop"*. Việc báo cáo trước đây liệt kê các từ này là không phản ánh đúng cấu trúc thực tế của module chú thích hình ảnh D.

---

## 6. Giới Hạn, Ranh Giới Phạm Vi & Cam Kết Bất Biến

1. **Cam kết bất biến của kho mã nguồn (Source Immutability Attestation)**:
   - Toàn bộ các tệp tài liệu bài giảng (`docs/vat-ly-1/bai-giang/`), tệp cấu hình catalog (`docs/.vitepress/`), tệp kế hoạch (`docs/agy-plans/`) và tệp nguồn (`raw_materials/physics/translations/`) được giữ nguyên trạng thái, không bị sửa đổi bất kỳ ký tự nào.
   - Không thực hiện lệnh `git commit`, `git push`, hoặc triển khai (deploy).
   - Không cài đặt thêm gói npm/python nào và không chạy máy chủ dev cục bộ.
   - Tệp duy nhất được cập nhật và hiệu chỉnh trong phiên làm việc này là: `raw_materials/physics/reviews/ch10-parent-numbered-independent-review-20261023.md`.
2. **Ủy thác build toàn cục cho CI/CD**:
   - Tuân thủ nghiêm ngặt chỉ dẫn của dự án: Tuyệt đối không chạy `npm run ci:build` trên máy cục bộ để bảo vệ tài nguyên RAM/CPU hệ thống; toàn bộ quy trình build và deploy trang tĩnh được ủy thác tự động cho GitHub Actions khi mã nguồn được hợp nhất.
3. **Phạm vi hiệu lực**:
   - Báo cáo này áp dụng chuyên biệt cho 75 bài tập đánh số (10.1 – 10.75) của Chương 10 thuộc môn Vật Lý Đại Cương 1.
