# Rà chéo độc lập: Bài tập chương 27.61–27.85

## Phạm vi và nguồn

Đã đọc trực tiếp trang in 913–917 (PDF 933–937), các hình bài 27.64–27.73 trên trang nguồn, và trang đáp án A-17 (PDF 1562). Đã rà lại đủ 25 đề và tiểu mục trong hai tệp bài tập 15/16, cùng các kết quả độc lập bằng Python. Không sửa hai tệp này hoặc checker cũ.

Checker cũ không được dùng làm căn cứ kết luận: một số phép kiểm của nó kế thừa cùng hướng vectơ sai trong bản nháp. Verifier độc lập mới tự dựng các vectơ từ dòng điện, hình học và trường nêu trong đề, rồi mới so sánh đáp số.

## Phát hiện P1

### 27.71 — Trường trên vòng vuông bị áp dụng sai ngoài mặt phẳng vòng

Nguồn cho B_y = B_0 z/L và B_z = B_0 y/L, trong khi vòng nằm trong mặt phẳng xy nên z = 0 tại mọi điểm của dây. Vì vậy B_y = 0 dọc cả vòng. Dùng chiều dòng kim đồng hồ nhìn từ +z:

- Cạnh trái: dòng +y, lực tổng +I B_0 L/2 theo +x.
- Cạnh phải: dòng −y, lực tổng −I B_0 L/2 theo −x.
- Cạnh trên: dòng +x, B_z = B_0, lực −I B_0 L theo −y.
- Cạnh dưới: y = 0 và z = 0, nên lực bằng không.

Hai lực ngang triệt tiêu. Lực tổng là −I B_0 L theo −y. Bản nháp hiện có dùng B_y khác không trên cạnh nằm ở z = 0, cộng thành phần lực sai và cho lực tổng sai chiều. Nguồn đáp án A-17 xác nhận các lực trái/phải đối nhau, lực cạnh trên hướng −y, cạnh dưới bằng không, và lực tổng −I B_0 L theo −y.

### 27.72 — Lực căng dây sai số học

Với dòng hướng về bản lề P và trường hướng vào trang, mômen từ cùng chiều với mômen trọng lực. Các độ lớn là:

$$
\begin{aligned}
    &\tau_B = \frac{IBL^2}{2} = 0{,}023328\ \mathrm{N\,m}\\
    &\tau_g = mg\frac{L}{2}\cos 53^\circ = 0{,}04451\ \mathrm{N\,m}
\end{aligned}
$$

Dây ngang ở đầu thanh có cánh tay đòn L sin 53°. Vì thế lực căng là

$$
T = \frac{\tau_g+\tau_B}{L\sin 53^\circ}
  = 0{,}472\ \mathrm{N}.
$$

Bản nháp ghi 0,515 N, không khớp với chính các mômen và điều kiện cân bằng đang trình bày.

### 27.75 — Điều kiện độ lớn trường và thành phần B_z không đúng

Với vòng trong mặt phẳng xy, dòng nhìn từ +z theo chiều kim đồng hồ cho μ = −IA k. Từ τ = μ × B = D(4i − 3j):

- B_y = 4D/(IA).
- B_x = 3D/(IA).

Nguồn cho |B| = 13D/(IA), nên |B_z| = 12D/(IA). Điều kiện U = −μ·B < 0 chọn B_z = −12D/(IA). Vectơ đúng là

$$
\vec B = \frac{D}{IA}(3\hat i + 4\hat j - 12\hat k).
$$

Bản nháp trước khi root sửa điều kiện trường dùng √34D/(IA) rồi suy ra B_z = −3D/(IA). Cả độ lớn trường lẫn thành phần z khi ấy sai. Cần kiểm lại bài đã sửa hiện tại vì đề đã được sửa sang hệ số 13 nhưng phần lời giải còn khả năng dùng kết quả cũ.

### 27.77 — Thang đo đồ thị bị mất hệ số 10^8

Trục tung của Hình P27.77 ghi E² theo đơn vị 10^8 V²/m². Tại V = 400 V, điểm y = 800 nghĩa là E² = 800×10^8 = 8,0×10^10 V²/m², không phải 8,0×10^8. Hệ số góc đúng là 2,0×10^8 (V²/m²)/V, khớp với khối lượng muon 1,85×10^−28 kg và tốc độ 8,32×10^5 m/s. Phần tóm tắt trong bản nháp đang ghi điểm đồ thị nhỏ hơn 100 lần trong khi dùng hệ số góc đúng ở bước sau.

### 27.79 — Thành phần từ trường theo trục j bị đổi thành trục k

Đề nguồn cho B = B(sin α i + cos α j). Với vỏ cầu quay Ω = ωk, mômen từ là μ = (QωR²/3)k. Do đó

$$
\vec\tau =
\frac{Q\omega R^2B}{3}
\left(\sin\alpha\,\hat j-\cos\alpha\,\hat i\right).
$$

Bản nháp đổi thành phần cos α j sang cos α k và vì vậy bỏ mất thành phần mômen theo −x. Cần giữ nguyên vectơ trường của đề.

### 27.80 — Phân tích ban đầu của người rà sai góc vận tốc

Tôi đã kết luận sai ở lượt rà đầu rằng vận tốc vuông góc với trường và lấy v_perp = v. Kiểm tra lại đúng hình học tại vĩ độ 80° Bắc cho thấy vận tốc hướng về trục Trái Đất, song song mặt phẳng xích đạo; trường lại hướng tâm Trái Đất. Chọn x hướng ra ngoài theo bán kính xích đạo, z song song trục Trái Đất, y theo hướng đông, ta có r_hat = (cos 80°, 0, sin 80°), B = −B r_hat và v = (−v, 0, 0). Góc giữa v và B là 80°, không phải 90°.

Do đó, thành phần song song hướng về tâm là v_parallel = v cos 80° = 69,5 km/s, còn thành phần gây chuyển động tròn là v_perp = v sin 80° = 393,9 km/s. Bán kính quỹ đạo là

$$
r = \frac{m_e v_\perp}{eB}
  = 0{,}1495\ \mathrm{m}.
$$

Vì vậy bán kính 1,52×10^5 m trong bản nháp sai đơn vị sáu bậc độ lớn, còn con số 0,152 m tôi báo ban đầu cũng hơi cao vì đã dùng sai toàn bộ tốc độ làm thành phần vuông góc. Thành phần song song không bị lực từ đổi nên electron tiếp tục tiến về phía Trái Đất với tốc độ xuyên tâm 69,5 km/s; tổng tốc độ ngay sau khi vào vùng có từ trường vẫn là 400 km/s. Nhìn từ không gian theo hướng vào Trái Đất, electron quay theo chiều kim đồng hồ vì q < 0. Tần số cyclotron khoảng 4,19×10^5 Hz. Công của điện trường lên electron khi nó dịch chuyển về phía nam là dương, tốc độ cuối xấp xỉ 2,65×10^7 m/s và K_f/K_i khoảng 4,39×10^3.

## Phát hiện P2 và nội dung cần làm rõ

- **27.65, mômen trọng lực:** Đáp số 0,0241 T khớp nguồn, nhưng dòng hiện tại gọi mg(0,08/2)tan30° là mômen trọng lực. Mômen trọng lực thực là mg(0,08/2)sin30°. Mômen từ quanh bản lề là IA B cos30°. Tỉ số hai mômen mới cho công thức chứa tan30°. Nên trình bày hai mômen riêng để không dạy sai cơ học quay.
- **27.74, ký pháp đạo hàm:** Dòng (b) viết d²v_y/dt² = −ω,dv_x/dt = −ω²v_y. Dấu phẩy giữa ω và dv_x/dt nên được thay bằng phép nhân hoặc ngoặc: −ω(dv_x/dt). Phương trình còn lại và kết quả y_max = 0,510 mm phù hợp đề.
- **27.62, hướng “trục rotor”:** Nguồn nói từ trường stator song song trục mỗi rotor, còn lời giải dùng τ = μB, tương đương giả thiết μ vuông góc B. Nếu “trục rotor” chỉ trục mômen từ của cuộn thì hai điều kiện mâu thuẫn. Cần làm rõ trục hình học nào đang được gọi là trục rotor hoặc nêu rõ góc giữa μ và B khi dùng công thức mômen.
- **27.63, đại lượng trả lời câu (d):** Nguồn hỏi extra weight và đáp án A-17 cho 0,83 N. Bản dịch đổi thành “khối lượng thêm” và cho 0,0846 kg. Hai số tương đương vật lý, nhưng nên nêu 0,829 N theo đại lượng nguồn, có thể kèm khối lượng tương đương.

## Các mục đã đối chiếu

- 27.61: Dùng lực tổng trong trường đều bằng I Δr × B, cho 1,13 N hướng về gốc trong trường +z và 0,800 N hướng +z trong trường +x.
- 27.62: Phép ước lượng hình học cho đường kính rotor khoảng 1,31 cm, mômen từ khoảng 0,117 A·m² và khoảng 1,38×10^4 vòng, với lựa chọn đường kính hub đã nêu.
- 27.63: Dòng nâng thanh bằng thành phần ngang trường Trái Đất khoảng 4,84×10^4 A; trường ngang tối thiểu ở 900 A khoảng 1,9 mT; tải thêm khoảng 0,83 N.
- 27.64–27.70: Kiểm dấu dòng và tích có hướng theo hình P27.64–P27.70. Các mômen cần giữ ở 27.64 là 0,0299 N·m theo +y và 0,0173 N·m theo −y; bài 27.65 cho +y; 27.67 cho mômen quanh PR 3,60 N·m hướng +x; 27.68 có mômen quanh PR bằng không; lực cuộn loa 27.69 hướng −y; dòng cân bằng 27.70 khoảng 2,26 A từ a đến b.
- 27.73: Công thức đã được root sửa, khớp kiểm tra độc lập với nguồn: μ = 2NIWR, s = 2NIWB/(Mg), h_top = R(1+π/2), hai nhánh mômen và thế năng liên tục tại h = R. Điều kiện quay quá nửa vòng là s < (1+π/2)/2.
- 27.76–27.78: Hồi quy SI cho 27.76 cho slope 4,0213×10^−6 m²/V, q/m = 7,958×10^6 C/kg, v(20 kV) = 5,642×10^5 m/s; tỷ lệ bán kính ion đôi là 1/√2. Dữ liệu cyclotron 27.78 khớp slope khoảng 7,67×10^6 Hz/T, từ đó ra khối lượng alpha và các tần số nêu trong bản nháp.
- 27.81–27.85: Quỹ đạo hạt ở 27.81 cho R = 5,14 m, t = 1,72 μs, lệch tại mép 6,08 mm và lệch tại tường 3,05 cm. Lập luận năng lượng và độ cong của cycloid 27.82 đúng. Các đáp án MRI 27.83–27.84 và lực cực đại lên dây thần kinh 27.85 lần lượt là (c), phosphorus-31 và khoảng 5,9×10^−7 N.

## Kiểm tra độc lập

Verifier mới tự tính từ các thông số của đề và vectơ trên hình, không dùng lại checker cũ. Nó kiểm tra các mục có hướng, P71–P75, hồi quy DATA 27.76–27.78, 27.79–27.82 và 27.85. Lệnh chạy:

& 'C:/Users/Ai/miniconda3/python.exe' -X utf8 raw_materials/physics/rawphysicsverify_chapter27_advanced_cross.py

Kết quả chạy: Selected independent checks for Problems 27.61–27.85 passed. Đây là các kiểm tra được chọn để xác minh công thức và hướng, không phải tuyên bố mọi phép tính trong 25 lời giải đã được tự động chứng nhận.
