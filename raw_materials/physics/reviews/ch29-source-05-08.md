# Inventory nguồn Chương 29, mục 29.5–29.8 và Summary

## Phạm vi và trạng thái đối chiếu

- Đã đọc trực tiếp PDF `raw_materials/physics/source/young-freedman-15.pdf` bằng PyMuPDF. Bản văn bản trích xuất của nguồn nằm ở `qa/physics/full-source/pdf-NNNN.txt` trong thư mục gốc của workspace.
- Số trang PDF trong brief là số trang một-based: trang in 953 tương ứng trang PDF 973. PyMuPDF dùng chỉ số zero-based, nên index trang bằng `trang in + 19`; trang in 967 là PDF index 986, tức trang PDF một-based 987. Dải trang PDF 973–1007 bao trùm trang in 953–987, bao gồm mục 29.5–Summary trên trang in 967–977. Đã đọc đủ các trang in 967–976 chứa mục 29.5–29.8, trang in 977 chứa Summary, và trang in 978 để xác nhận ranh giới kế tiếp.
- Trang in 967 còn có đáp án tự kiểm 29.4 và phần cuối Ví dụ 29.10; chúng được ghi dưới đây như ngữ cảnh liền trang, không xem là nội dung mới của mục 29.5.
- Không đọc các trang ngoài phạm vi nêu trên, không kiểm tra toàn chương hay các câu bài tập cuối chương. Không dựng lại hình thành ảnh riêng. Mô tả hình và nhãn dưới đây lấy từ chú thích, nhãn trong trang và nội dung văn bản đọc được.

## Mục 29.5 — Điện trường cảm ứng (trang in 967–968)

### Mạch lập luận và điều kiện

Mục mở từ câu hỏi: Trong một vòng dây đứng yên có từ thông biến thiên, lực nào làm điện tích chạy quanh mạch khi dây không chuyển động trong từ trường? Tác giả xét ống dây dài, mảnh có tiết diện `A`, mật độ vòng dây `n`, mang dòng `I`, được một vòng dẫn tròn bao quanh ở giữa. Bỏ qua từ trường nhỏ bên ngoài ống dây; lấy vectơ diện tích cùng chiều với từ trường dọc trục. Dùng kết quả ống dây dài `B = μ₀nI`, suy ra từ thông `ΦB = BA = μ₀nIA`, rồi dùng định luật Faraday:

- **(29.8)** `ℰ = −dΦB/dt = −μ₀nA dI/dt`.
- Với điện trở tổng `R` của vòng dây, dòng cảm ứng tức thời là `I′ = ℰ/R`.
- Vì vòng dây ở ngoài vùng có từ trường, lực từ không thể giải thích chuyển động điện tích. Suy ra có điện trường cảm ứng do từ thông biến thiên.
- **(29.9)** Công trên một đơn vị điện tích khi đi một vòng là suất điện động: `∮ E⃗ · dℓ⃗ = ℰ`. Tích phân đường kín khác không, do đó điện trường cảm ứng không bảo toàn và không có thế điện vô hướng gắn với nó.
- **(29.10)** Với đường tích phân đứng yên, `∮ E⃗ · dℓ⃗ = −dΦB/dt`. Tác giả nhấn mạnh dạng `ℰ = −dΦB/dt` luôn đúng, còn dạng tích phân trường theo đường kín nêu ở (29.10) chỉ được khẳng định cho đường tích phân đứng yên.
- Với vòng tròn bán kính `r`, đối xứng trụ cho `E⃗` tiếp tuyến, cùng độ lớn trên vòng. Khi đó độ lớn tích phân là `2πrE`, và **(29.11)** `E = (1/(2πr)) |dΦB/dt|`. Khả năng trường hướng xuyên tâm bị loại bằng định luật Gauss vì khi ấy phải có điện tích thuần bên trong, trong khi không có.
- Lập luận được đối chiếu với điện trường tĩnh: trường tĩnh bảo toàn, có thế; điện trường cảm ứng không bảo toàn, có thể sinh công trên đường kín. Tuy vậy cả hai đều tác dụng lực `F⃗ = qE⃗` lên điện tích. Điện trường cảm ứng tồn tại ngay cả khi không có vật dẫn.
- Mục nối tính chất này với đối xứng sẽ gặp ở 29.7: điện trường biến thiên cũng có thể là nguồn của từ trường; các trường biến thiên liên hệ với sóng điện từ ở Chương 32.

### Ví dụ, ứng dụng và hình

- **Hình 29.18:** Ống dây dài mang dòng `I` đang tăng, từ thông qua vòng dây tăng và gây suất điện động, dòng `I′` được galvanometer `G` đo. (a) Hình 3D có ống dây, vòng dây, galvanometer, vùng hình trụ màu xanh biểu thị `B`; (b) mặt cắt ngang ghi `I`, `dI/dt`, bán kính `r`, diện tích `A`.
- **Ví dụ 29.11:** Dữ kiện `n = 500 vòng/m`, `A = 4.0 cm² = 4.0×10⁻⁴ m²`, `dI/dt = 100 A/s`, bán kính vòng `r = 2.0 cm = 2.0×10⁻² m`. Câu hỏi lần lượt tìm độ lớn suất điện động và điện trường cảm ứng trên vòng.
  - Dùng (29.8): `ℰ = −μ₀nA(dI/dt) = −25×10⁻⁶ V = −25 μV` (trang in thể hiện tương đương `−25×10⁻⁶ Wb/s = −25×10⁻⁶ V`). Độ lớn là `25 μV`.
  - Dùng `|∮E⃗·dℓ⃗| = 2πrE = |ℰ|`: `E = 25×10⁻⁶/[2π(2.0×10⁻²)] = 2.0×10⁻⁴ V/m`.
  - Từ thông hướng vào mặt trang đang tăng. Theo chiều dấu trong Faraday và quy ước hình, suất điện động dương sẽ theo chiều kim đồng hồ, nhưng dấu âm cho biết chiều thực là ngược kim đồng hồ. Lời đánh giá yêu cầu có thể tự kiểm tra cùng kết luận bằng định luật Lenz.
- **Hình 29.19, ứng dụng điện trường cảm ứng:** (a) Xe điện khi dừng, bánh xe vẫn quay động cơ ngược chiều tác dụng như máy phát, dòng nạp lại pin; (b) trục khuỷu máy bay động cơ piston quay nam châm, gây suất điện động ở cuộn dây kề bên và tạo tia lửa đốt nhiên liệu, giúp động cơ tiếp tục chạy nếu hệ điện khác hỏng. Văn bản còn nêu pickup guitar điện cảm ứng dòng trong cuộn đứng yên do dây sắt từ rung và alternator ô tô dùng nam châm quay để cảm ứng dòng trong cuộn đứng yên.

### Tự kiểm và lời đáp

- **Tự kiểm 29.5:** Lắc qua lại một nam châm bằng tay có tạo điện trường không? Nếu có, điện trường ấy có bảo toàn không?
- **Đáp án nguồn:** Có. Tại một vị trí cố định, từ trường thay đổi khi nam châm chuyển động, nên điện trường cảm ứng xuất hiện. Trường ấy không bảo toàn.

## Mục 29.6 — Dòng điện Fu-cô (trang in 969–970)

### Giải thích, giả thiết và suy luận

Dòng cảm ứng trước đó thường đi theo mạch xác định. Trong khối kim loại chuyển động trong từ trường hoặc nằm trong từ trường biến thiên, dòng có thể tuần hoàn qua thể tích vật liệu; các đường dòng xoáy gợi hình ảnh xoáy nước nên được gọi là dòng điện Fu-cô (eddy currents).

- **Hình 29.20:** Đĩa kim loại quay trong vùng từ trường vuông góc mặt đĩa, vùng trường chỉ phủ một phần. Miền `Ob` cắt qua từ trường và có suất điện động; các miền `Oa` và `Oc` ngoài trường tạo đường hồi cho điện tích. Dòng xoáy ở vùng `Ob` tương tác với trường và sinh lực hãm. Khi `B⃗` hướng vào mặt trang, chiều dòng và vectơ đoạn dây `L⃗` có thành phần hướng xuống để `F⃗ = I L⃗ × B⃗` hướng sang phải, ngược chiều quay tại vùng tác dụng. Dòng hồi ở ngoài trường không chịu lực từ. Không có công thức đánh số riêng trong phần giải thích này.
- Ứng dụng hãm: Dòng Fu-cô dừng nhanh lưỡi cưa tròn sau khi ngắt điện. Trên một số tàu điện đô thị nhanh, nam châm điện trên toa gây dòng Fu-cô trong đường ray; từ trường của dòng đó tạo lực hãm lên nam châm và toa.
- Ứng dụng gia nhiệt: Lò cảm ứng dùng dòng Fu-cô nung vật liệu trong bình kín hoàn toàn, khi cần tránh nhiễm bẩn.
- Ứng dụng dò kim loại: Cổng dò sân bay phát hiện dòng Fu-cô trong vật kim loại. Máy dò cầm tay hoạt động cùng nguyên lý, có thể dò các vật nhỏ bị chôn như nắp chai hoặc đồng xu.
- Tác dụng không mong muốn: Dòng biến thiên hình sin trong cuộn biến áp tạo dòng Fu-cô trong lõi sắt. Dòng này gây tổn hao nhiệt `I²R` và suất điện động đối kháng không mong muốn trong cuộn. Để giảm, làm đường dòng Fu-cô hẹp; cấu tạo lõi biến áp được dành lại cho mục 31.6.
- **Hình 29.21:** (a) Cuộn phát tạo từ trường xoay chiều `B⃗₀`, gây dòng Fu-cô trong vật dẫn; trường do chúng tạo ra `B⃗′` cảm ứng dòng ở cuộn thu. Nhãn gồm xung dòng, `I₀`, `I′`, cuộn phát, cuộn thu. (b) Máy dò kim loại cầm tay cùng nguyên lý.
- **Ứng dụng “Eddy Currents Help Power Io’s Volcanoes”:** Io, vệ tinh Sao Mộc, lớn hơn Mặt Trăng một chút và chuyển động trên 60.000 km/h trong từ trường mạnh khoảng mười lần từ trường Trái Đất. Dòng Fu-cô trong Io tiêu tán năng lượng khoảng `10¹² W`, làm nóng phần trong và góp phần gây núi lửa trên bề mặt. Tác giả nêu hiệu ứng hấp dẫn từ Sao Mộc còn gây mức nung nóng lớn hơn.

### Tự kiểm và lời đáp

- **Tự kiểm 29.6:** Đảo `B⃗` trong Hình 29.20 ra khỏi mặt trang và cho đĩa quay ngược chiều kim đồng hồ. So với Hình 29.20b, lực `F⃗` và dòng Fu-cô đổi chiều thế nào? Bốn lựa chọn phân biệt việc lực/dòng cùng chiều hoặc trái chiều so với hình gốc.
- **Đáp án nguồn:** (iii), lực đổi chiều còn dòng Fu-cô giữ chiều như cũ. Lenz yêu cầu lực chống chuyển động; vật liệu đĩa tại vùng từ trường chuyển động sang phải nên lực hướng trái. Với `B⃗` hướng ra khỏi trang, dòng hướng xuống vẫn tạo lực trái theo `I L⃗ × B⃗`.

## Mục 29.7 — Dòng điện dịch và phương trình Maxwell (trang in 970–974)

### Vì sao cần sửa định luật Ampère

Mở đầu nêu tính đối xứng vật lý: từ trường biến thiên sinh điện trường, và điện trường biến thiên sinh từ trường. Quan hệ thứ hai giúp giải thích sóng radio, tia gamma, ánh sáng nhìn thấy và các sóng điện từ khác.

- Dạng định luật Ampère ở Chương 28 là `∮B⃗·dℓ⃗ = μ₀ I_encl`. Xét tụ điện phẳng đang nạp (Hình 29.22), dòng dẫn `iC` chạy vào một bản và ra bản kia, điện tích `Q` tăng, điện trường giữa hai bản tăng. Ký hiệu `iC` phân biệt dòng dẫn với dòng dịch `iD`; chữ thường `i`, `v` chỉ giá trị tức thời có thể đổi theo thời gian.
- Chọn đường Ampère kín chung cho hai mặt: mặt phẳng cắt dây dẫn nên dòng bao là `iC`; mặt cong phình qua khe tụ không cắt dòng dẫn nên cho số hạng dòng bao bằng 0. Dạng Ampère cũ khi ấy cho cùng tích phân đường bằng `μ₀iC` và bằng 0, một mâu thuẫn phụ thuộc mặt căng.
- Với điện môi có hằng số điện môi `P` (ký hiệu của sách; trong chân không thay bằng `P₀`), bỏ qua hiệu ứng bờ và giả sử điện trường đều trong khe. Dùng `q = Cv`, `C = PA/d`, `v = Ed`, `ΦE = EA`, được **(29.12)** `q = Cv = (PA/d)(Ed) = PEA = PΦE`.
- Lấy đạo hàm theo thời gian và dùng `iC = dq/dt`, được **(29.13)** `iC = dq/dt = P dΦE/dt`.
- Định nghĩa dòng dịch qua diện tích là **(29.14)** `iD = P dΦE/dt`. Đây là cách mở rộng khái niệm dòng để từ thông điện biến thiên trong khe tụ đóng vai trò trong định luật Ampère như dòng dẫn qua mặt cong.
- **(29.15), Ampère tổng quát:** `∮B⃗·dℓ⃗ = μ₀(iC+iD)_encl`. Với mặt phẳng, `iD=0`; với mặt cong, `iC=0`; dòng dẫn mặt thứ nhất bằng dòng dịch mặt thứ hai, nên cùng kết quả cho hai mặt. Trong vật liệu từ, dạng này còn đúng nếu độ từ hóa tỉ lệ với trường ngoài và thay `μ₀` bằng `μ`.
- **(29.16), mật độ dòng dịch:** `jD = iD/A = P dE/dt` trong trường hợp trường đều qua diện tích. Văn bản giải thích phép chia (29.14) cho `A` và `ΦE=EA`.
- Dòng dịch cũng khôi phục cách phát biểu quy tắc nút Kirchhoff: tại một bản tụ có dòng dẫn đi vào nhưng không có dòng dẫn đi ra; nếu tính dòng dịch đi ra bằng nó thì dòng tổng quát vào và ra cân bằng, cho phép nói dòng đi qua tụ.

### Kiểm chứng dòng dịch bằng từ trường đo được

- Câu hỏi được nêu trực tiếp: Dòng dịch có ý nghĩa vật lý thật hay chỉ là mẹo cứu định luật Ampère và quy tắc Kirchhoff?
- **Hình 29.23 và (29.17):** Tụ tròn có bán kính bản `R`, đang nạp; xét đường tròn bán kính `r<R` giữa hai bản. Mật độ dòng dịch bằng `iD/(πR²)`, dòng dịch bao bởi đường tròn nhỏ bằng mật độ ấy nhân `πr²`. Đối xứng cho tích phân trái bằng `2πrB`; với `iD=iC`, suy ra `2πrB=μ₀(r²/R²)iC` và **(29.17)** `B=(μ₀/(2π))(r/R²)iC`. Từ trường bằng 0 trên trục và tăng tuyến tính theo `r`. Ngoài vùng giữa hai bản (`r>R`), phép tính cho trường như dây dẫn liên tục, không có tụ.
- Sách nói phép đo thực tế xác nhận trường giữa hai bản có thật và đúng dự đoán của (29.17), từ đó khẳng định dòng dịch là đặc trưng cơ bản của tự nhiên, không chỉ là thủ thuật hình thức.

### Bốn phương trình Maxwell và phạm vi của chúng

Đặt gói phương trình ở dạng đơn giản nhất cho điện tích và dòng điện trong chân không/không gian trống; việc có điện môi hay vật liệu từ được để sang Chương 32. Ký hiệu `∮` dùng cho mặt kín hoặc đường kín tùy biểu thức; `Q_encl` là điện tích nằm trong mặt kín.

- **(29.18), Gauss cho điện trường:** `∮ E⃗·dA⃗ = Q_encl/P₀`.
- **(29.19), Gauss cho từ trường:** `∮ B⃗·dA⃗ = 0`. Hệ quả nêu trong sách là không có đơn cực từ riêng lẻ đóng vai trò nguồn từ trường.
- **(29.20), Faraday cho đường tích phân đứng yên:** `∮ E⃗·dℓ⃗ = −dΦB/dt`. Từ trường biến thiên sinh điện trường không bảo toàn.
- **(29.21), Ampère–Maxwell cho đường tích phân đứng yên:** `∮ B⃗·dℓ⃗ = μ₀(iC + P₀ dΦE/dt)_encl`. Dòng dẫn và thông lượng điện biến thiên đều là nguồn từ trường.
- Trường điện tổng quát là chồng chất `E⃗ = E⃗_c + E⃗_n`, gồm phần tĩnh do phân bố điện tích đứng yên (bảo toàn, có tích phân đường kín bằng 0) và phần cảm ứng từ không bảo toàn. Trong (29.20) dùng trường tổng vì phần tĩnh không góp vào tích phân đường kín. Trong Gauss, phần không tĩnh cảm ứng không đóng góp vào thông lượng mặt kín theo lập luận sách; do đó toàn bộ các phương trình dùng trường điện tổng, không cần tách hai loại trường.

### Đối xứng, hệ quả và giới hạn

- Trong chân không không có điện tích và dòng dẫn, hai phương trình mặt kín có cùng dạng: **(29.18)** và **(29.19)** cho thông lượng `E⃗` và `B⃗` bằng 0. Hai phương trình đường kín cũng đối xứng theo vai trò hai trường:
  - **(29.22):** `∮E⃗·dℓ⃗ = −d/dt ∫B⃗·dA⃗`.
  - **(29.23):** `∮B⃗·dℓ⃗ = μ₀P₀ d/dt ∫E⃗·dA⃗`.
- Từ quan hệ này, trường biến thiên loại này sinh trường kia ở vùng lân cận. Maxwell nhận ra chúng dự đoán nhiễu loạn điện từ tự truyền qua không gian không có vật chất trung gian. Sóng điện từ là cơ sở vật lý của ánh sáng, sóng radio và truyền hình, hồng ngoại, tử ngoại, tia X.
- Tác giả nêu có thể suy ra định luật Coulomb từ Gauss, định luật Biot–Savart từ Ampère, và các quan hệ nguồn-trường cơ bản khác từ bộ Maxwell. Khi ghép thêm lực Lorentz **(29.24)** `F⃗ = q(E⃗ + v⃗ × B⃗)`, có đủ các quan hệ cơ bản của điện từ học.
- Nếu tồn tại đơn cực từ, tính đối xứng tăng: vế phải (29.19) có điện tích từ bao bởi mặt, còn (29.20) có thêm dòng đơn cực từ. Sách ghi chưa tìm được đơn cực từ.
- Sách so sánh sức khái quát và độ cô đọng của tổng hợp Maxwell với các định luật Newton, nhiệt động lực học, thuyết tương đối và cơ học lượng tử.
- **Hình 29.24:** Sơ đồ Maxwell trong chân không, ghi thông lượng `E⃗`, `B⃗` qua mặt kín bằng 0 khi không có điện tích; đồng thời tích phân đường của mỗi trường liên hệ với tốc độ biến thiên thông lượng trường kia khi không có dòng dẫn.

### Tự kiểm và lời đáp

- **Tự kiểm 29.7:** (a) Phương trình Maxwell nào giải thích đầu đọc thẻ tín dụng? (b) Phương trình nào mô tả dây mang dòng không đổi tạo từ trường?
- **Đáp án nguồn:** (a) Định luật Faraday, vì quẹt dải từ cảm ứng dòng trong cuộn dây của đầu đọc; (b) định luật Ampère, có tính cả dòng dẫn và dòng dịch.

## Mục 29.8 — Siêu dẫn (trang in 975–976)

### Tính chất, điều kiện và hiệu ứng Meissner

- Tính chất quen thuộc: điện trở biến mất đột ngột khi làm lạnh vật liệu xuống dưới nhiệt độ tới hạn `Tc`. Mục nhấn mạnh siêu dẫn còn có các tính chất từ đặc biệt.
- Với mọi vật liệu siêu dẫn, `Tc` thay đổi khi đặt vật liệu vào từ trường ngoài `B⃗₀`. Hình 29.25 minh họa thủy ngân, nguyên tố đầu tiên ghi nhận siêu dẫn: trường ngoài lớn hơn `0.0412 T` thì không còn chuyển pha siêu dẫn. Độ lớn trường nhỏ nhất cần để triệt tiêu siêu dẫn ở nhiệt độ dưới `Tc` được gọi là trường tới hạn `Bc`. Hình biểu diễn pha thường/pha siêu dẫn, `Tc`, `Bc(T)` và các vạch số 0.01–0.05 T, 1–5 K. Với vật liệu khác, hình dạng tương tự nhưng số liệu khác.
- **Điều kiện thí nghiệm Meissner:** Cầu đồng chất siêu dẫn đặt trong trường ngoài đều `B⃗₀` khi `T>Tc`, nên lúc đầu ở pha thường. Hạ nhiệt độ xuống `T<Tc`, giả sử độ lớn trường ngoài không đủ để ngăn chuyển pha.
- Trường bên ngoài bị biến dạng; bên trong vật liệu không còn từ trường, ngoại trừ khả năng có một lớp bề mặt rất mỏng cỡ một trăm nguyên tử. Cuộn dây quấn quanh cầu cho thấy từ thông qua cuộn giảm về 0 trong chuyển pha. Sau đó tắt trường ngoài khi vật liệu vẫn ở pha siêu dẫn thì không có suất điện động cảm ứng trong cuộn và đo được trường bên ngoài bằng 0. Tác giả kết luận từ thông bị đẩy khỏi phần khối vật liệu, từ thông qua cuộn bằng 0; hiện tượng đẩy từ thông ấy là hiệu ứng Meissner. Các đường sức dồn sát hai bên cầu nên `B⃗` tại đó tăng.
- **Hình 29.26:** (a) Trên `Tc`, trường trong vật liệu xấp xỉ `B₀`; (b) hạ xuống dưới `Tc`, từ thông bị đẩy khỏi vật liệu và `B=0` bên trong (Meissner); (c) tắt trường ngoài khi vẫn dưới `Tc`, trường bằng 0 khắp nơi, không có thay đổi từ thông trong vật liệu.

### Lực từ và ứng dụng

- Tác giả giải thích bằng tính nghịch từ: vật liệu thuận từ hoặc sắt từ bị nam châm hút vì lưỡng cực từ định hướng theo trường không đều. Vật liệu nghịch từ có độ từ hóa ngược chiều và bị nam châm đẩy; theo định luật III Newton, nam châm cũng bị đẩy khỏi vật liệu.
- **Hình 29.27:** Mẫu siêu dẫn nhiệt độ cao đẩy nam châm, lực đẩy giữ nam châm lơ lửng.
- Vật liệu loại I có hành vi vừa mô tả. Với loại II, phần khối vẫn siêu dẫn trong từ trường nhưng các sợi nhỏ chạy song song trường có thể trở về pha thường. Dòng tuần hoàn quanh biên các sợi, bên trong có từ thông. Vật liệu loại II dùng trong nam châm điện vì thường có trường tới hạn lớn hơn loại I, chịu được trường mạnh hơn trước khi mất siêu dẫn. Có hai trường tới hạn: `Bc1` là lúc từ thông bắt đầu đi vào và các sợi hình thành; `Bc2` là lúc vật liệu trở thành thường.
- Nam châm điện siêu dẫn dùng trong phòng thí nghiệm và máy MRI. MRI cần trường tĩnh `1.5 T` trở lên để định hướng lưỡng cực hạt nhân nguyên tử của bệnh nhân; nam châm thường khó tạo trường đó vì cần dòng lớn và tổn hao điện trở cao. Nam châm siêu dẫn không có tổn hao điện trở và có thể đạt trường đến `10 T` theo mô tả của sách.
- SQUID (thiết bị giao thoa lượng tử siêu dẫn) đo được biến thiên từ thông nhỏ hơn `10⁻¹⁴ Wb`, ứng dụng trong y học, địa chất và lĩnh vực khác.
- Vật liệu siêu dẫn nhiệt độ cao được phát hiện năm 1987 có `Tc` cao hơn nhiệt độ nitơ lỏng, khoảng `77 K`, nên dễ đạt điều kiện làm lạnh hơn tương đối. Sách kết thúc bằng nhận định triển vọng ứng dụng thực tế đang tăng.

### Công thức, tự kiểm và hình

- Không có công thức đánh số trong mục 29.8. Các đại lượng định lượng cần giữ gồm `Tc`, `Bc`, `Bc1`, `Bc2`, `0.0412 T`, `1.5 T`, `10 T`, `<10⁻¹⁴ Wb`, `1987`, `77 K` và độ dày lớp bề mặt có thể tới cỡ 100 nguyên tử.
- Không thấy câu “Test Your Understanding” riêng cho 29.8 trong phạm vi trang đã đọc.

## Summary Chương 29 (trang in 977)

Summary gom các kết luận và công thức dưới đây. Các hình minh họa nhỏ trong trang cũng thuộc phần nội dung cần bảo toàn khi chọn nội dung cho bài giảng.

- **Định luật Faraday, (29.3):** Suất điện động cảm ứng trong mạch kín bằng âm tốc độ biến thiên từ thông qua mạch. Đúng khi biến thiên từ thông do từ trường thay đổi, mạch chuyển động hoặc cả hai. Dẫn chiếu Ví dụ 29.1–29.6. Công thức `ℰ = −dΦB/dt`. Hình nam châm chuyển động qua cuộn dây cho biết từ thông từ trường đổi theo thời gian và cảm ứng dòng.
- **Định luật Lenz:** Dòng hoặc suất điện động cảm ứng luôn có xu hướng chống lại hay triệt tiêu sự biến thiên gây ra nó; có thể suy ra từ Faraday và thường dễ áp dụng. Dẫn chiếu Ví dụ 29.7–29.8. Hình chỉ chiều `B` đang tăng, trường cảm ứng `Binduced`, dòng `I` và chiều biến thiên.
- **Suất điện động chuyển động, (29.6):** `ℰ = vBL`, với thanh dẫn dài `L` chuyển động trong từ trường đều và `L⃗`, `v⃗` vuông góc nhau, đồng thời cả hai vuông góc với `B⃗`.
- **Suất điện động chuyển động dạng tổng quát, (29.7):** `ℰ = ∮(v⃗ × B⃗)·dℓ⃗`, khi toàn bộ hoặc một phần mạch kín chuyển động trong từ trường. Dẫn chiếu Ví dụ 29.9–29.10. Hình nhãn `q`, `L`, `a`, `b`, `v⃗`, `B⃗`, `F⃗=qvB`, `F⃗=qE⃗`, và phân cực hai đầu.
- **Điện trường cảm ứng, (29.10):** Khi suất điện động do từ thông biến thiên qua vật dẫn đứng yên, có điện trường cảm ứng không tĩnh điện; trường không bảo toàn và không có thế. `∮E⃗·dℓ⃗ = −dΦB/dt`. Dẫn chiếu Ví dụ 29.11. Hình vòng, galvanometer và từ trường tăng.
- **Dòng dịch và Maxwell:** Điện trường biến thiên tạo dòng dịch `iD`, đóng vai trò nguồn từ trường như dòng dẫn; bốn phương trình Maxwell nêu quan hệ giữa điện trường, từ trường và nguồn của chúng.
  - **(29.14):** `iD = P dΦE/dt` (dòng dịch).
  - **(29.18):** `∮E⃗·dA⃗ = Q_encl/P₀` (Gauss cho điện trường).
  - **(29.19):** `∮B⃗·dA⃗ = 0` (Gauss cho từ trường).
  - **(29.20):** `∮E⃗·dℓ⃗ = −dΦB/dt` (Faraday).
  - **(29.21):** `∮B⃗·dℓ⃗ = μ₀[iC + P₀ dΦE/dt]_encl` (Ampère có dòng dịch).

## Danh mục công thức đánh số cần bảo toàn trong phạm vi

| Số công thức | Vị trí | Nội dung/điều kiện gắn với công thức |
|---|---|---|
| (29.8) | 29.5, tr. 967 | Faraday cho vòng bao quanh ống dây dài, bỏ qua trường ngoài: `ℰ=−dΦB/dt=−μ₀nA dI/dt`. |
| (29.9) | 29.5, tr. 968 | Suất điện động bằng tích phân đường kín của điện trường cảm ứng: `∮E⃗·dℓ⃗=ℰ`. |
| (29.10) | 29.5, tr. 968; Summary tr. 977 | Đường tích phân đứng yên: `∮E⃗·dℓ⃗=−dΦB/dt`. |
| (29.11) | 29.5, tr. 968 | Đối xứng trụ trên vòng tròn: `E=|dΦB/dt|/(2πr)`. |
| (29.12) | 29.7, tr. 971 | Tụ phẳng, trường đều, bỏ qua hiệu ứng bờ: `q=Cv=(PA/d)(Ed)=PEA=PΦE`. |
| (29.13) | 29.7, tr. 971 | `iC=dq/dt=P dΦE/dt`. |
| (29.14) | 29.7, tr. 971; Summary tr. 977 | Định nghĩa `iD=P dΦE/dt`. |
| (29.15) | 29.7, tr. 971 | Ampère tổng quát: `∮B⃗·dℓ⃗=μ₀(iC+iD)_encl`; trong vật liệu từ có điều kiện và thay `μ₀` bằng `μ`. |
| (29.16) | 29.7, tr. 972 | Mật độ dòng dịch trong trường đều: `jD=P dE/dt`. |
| (29.17) | 29.7, tr. 972 | Tụ tròn, điểm giữa bản với `r<R`: `B=(μ₀/2π)(r/R²)iC`. |
| (29.18) | 29.7, tr. 973; Summary tr. 977 | Gauss điện: `∮E⃗·dA⃗=Q_encl/P₀`. |
| (29.19) | 29.7, tr. 973; Summary tr. 977 | Gauss từ: `∮B⃗·dA⃗=0`. |
| (29.20) | 29.7, tr. 973; Summary tr. 977 | Faraday cho đường kín đứng yên: `∮E⃗·dℓ⃗=−dΦB/dt`. |
| (29.21) | 29.7, tr. 973; Summary tr. 977 | Ampère–Maxwell cho đường kín đứng yên: `∮B⃗·dℓ⃗=μ₀(iC+P₀dΦE/dt)_encl`. |
| (29.22) | 29.7, tr. 974 | Viết Faraday bằng tích phân mặt từ thông trong chân không: `∮E⃗·dℓ⃗=−d/dt∫B⃗·dA⃗`. |
| (29.23) | 29.7, tr. 974 | Viết Ampère–Maxwell bằng thông lượng điện trong chân không, không dòng dẫn: `∮B⃗·dℓ⃗=μ₀P₀ d/dt∫E⃗·dA⃗`. |
| (29.24) | 29.7, tr. 974 | Lực Lorentz: `F⃗=q(E⃗+v⃗×B⃗)`. |

Các biểu thức không đánh số nhưng có vai trò suy diễn/định lượng gồm `B=μ₀nI`, `ΦB=BA=μ₀nIA`, `I′=ℰ/R`, `q=Cv`, `C=P₀A/d` (hoặc `P A/d` trong điện môi), `v=Ed`, `ΦE=EA`, `iC=dq/dt`, lực dây `F⃗=I L⃗×B⃗`, và các giá trị trong Ví dụ 29.11. Phần cuối trang in 967 cũng có tích phân suất điện động cho đĩa Faraday thuộc Ví dụ 29.10, nằm ngoài nội dung 29.5 nhưng cùng trang nguồn.

## Inventory hình và nhãn

| Hình | Trang in | Nội dung và nhãn đọc được |
|---|---:|---|
| 29.17 | 967 | Đĩa dẫn bán kính `R` quay tốc độ góc `ω` trong `B⃗`; suất điện động theo bán kính, hai tiếp điểm trượt `b`, `r`, `dr`, `v=ωr`, `dℰ=vBdr=ωBrdr`. Phần cuối Ví dụ 29.10 và ngoại vi phạm vi 29.5. |
| 29.18 | 967 | Ống dây `I`, `dI/dt`, từ trường `B⃗`, diện tích `A`, vòng dây và galvanometer `G`, dòng cảm ứng `I′`; mặt cắt tròn bán kính `r`. |
| 29.19 | 968 | Xe điện nạp pin nhờ động cơ làm việc như máy phát khi xe dừng; hệ đánh lửa động cơ piston trên máy bay. |
| 29.20 | 969 | Đĩa kim loại quay trong vùng từ trường cục bộ; các vùng `O`, `a`, `b`, `c`, dòng xoáy và lực hãm `F⃗`. |
| 29.21 | 970 | Máy dò kim loại có cuộn phát/thu, dòng `I₀`, `I′`, các trường `B⃗₀`, `B⃗′` và dòng Fu-cô trong vật dò; phiên bản cầm tay. |
| Hộp ứng dụng Io | 970 | Đường sức từ Sao Mộc, Io, núi lửa phun trào; số liệu vận tốc, độ mạnh trường tương đối, công suất tiêu tán ghi trong đoạn ứng dụng. |
| 29.22 | 971 | Tụ phẳng đang nạp; bản `Q`, `−Q`, dòng `iC`, điện trường `E⃗`; cùng đường Ampère, mặt phẳng và mặt cong phình. |
| 29.23 | 972 | Tụ tròn bán kính `R`, đường kiểm tra bán kính `r<R`, dòng dẫn `iC`, dòng dịch, mật độ `jD` và điểm `a`, `b` dùng suy ra trường giữa bản. |
| 29.24 | 974 | Bốn Maxwell trong chân không, ghi thông lượng mặt kín bằng 0 khi không có nguồn và quan hệ tích phân đường của trường biến thiên. |
| 29.25 | 975 | Đồ thị pha thủy ngân, `Bc` theo nhiệt độ, `Tc`, vùng pha thường và siêu dẫn; vạch trục `T(K)` và `Bc(T)`. |
| 29.26 | 975 | Cầu siêu dẫn trong trường: (a) `T>Tc`, trường trong gần `B₀`; (b) hạ `T<Tc`, đẩy từ thông, `B=0` trong khối; (c) tắt trường ngoài khi còn siêu dẫn, trường bằng 0 khắp nơi. |
| 29.27 | 976 | Nam châm được lực đẩy của mẫu siêu dẫn nâng lơ lửng. |
| Hình tóm tắt Faraday/Lenz | 977 | Nam châm chuyển động qua cuộn, `N/S`, dòng cảm ứng; hình Lenz có `B` tăng, `Binduced`, `I`; hình suất điện động chuyển động có `q`, `L`, `a`, `b`, `v⃗`, `B⃗`, lực `qvB`, `qE`. |
| Hình tóm tắt điện trường cảm ứng/Maxwell | 977 | Vòng dây, galvanometer `G`, `B` tăng, các mũi tên `E⃗`; bảng nhỏ bốn phương trình Maxwell. |

## Tự kiểm và đáp án nằm trong phần đã đọc

| Mục | Câu hỏi | Đáp án/luận cứ nguồn |
|---|---|---|
| Cuối 29.4, tr. 967 (ngữ cảnh) | Thanh kim loại khi người đi về đông, với trường Trái Đất hướng bắc và không có thành phần thẳng đứng: hướng thanh để suất điện động cực đại, bằng 0; hướng chuyển động để suất điện động bằng 0 với mọi hướng thanh? | Cực đại: thanh thẳng đứng. Bằng 0 khi thanh nằm theo hướng đông–tây hoặc bắc–nam. Đi về bắc hoặc nam thì `v⃗×B⃗=0`. |
| 29.5, tr. 969 | Lắc nam châm có tạo điện trường không, trường có bảo toàn không? | Có; điện trường cảm ứng không bảo toàn. |
| 29.6, tr. 970 | Đảo trường ra khỏi trang và quay đĩa ngược chiều kim đồng hồ thì hướng lực/dòng so với hình? | (iii), lực ngược chiều trong hình, dòng cùng chiều trong hình; giải bằng Lenz và `I L⃗×B⃗`. |
| 29.7, tr. 974 | Maxwell nào mô tả đầu đọc thẻ tín dụng; dòng không đổi trong dây tạo từ trường? | (a) Faraday; (b) Ampère, gồm dòng dẫn và dòng dịch. |

### Điểm cần giữ khi chuyển thành Notes sau này

- Không rút mục 29.7 thành câu ghi nhớ “điện trường biến thiên sinh từ trường”: giữ mâu thuẫn chọn hai mặt căng của Ampère, giả thiết tụ phẳng/điện trường đều, phép nối `q=Cv` đến `ΦE`, định nghĩa dòng dịch, kiểm chứng đo được (29.17), bốn phương trình, miền áp dụng, đối xứng chân không và lực Lorentz.
- Không thu hẹp 29.8 thành “điện trở bằng không”: hiệu ứng Meissner là đẩy từ thông trong điều kiện chuyển pha cụ thể; giữ khác biệt loại I/II, hai ngưỡng `Bc1`, `Bc2`, lớp bề mặt, và các ứng dụng/định lượng MRI, SQUID, nitơ lỏng.
- Với ví dụ 29.11, giữ dấu âm của suất điện động bên cạnh độ lớn, chuyển đổi `cm²` sang `m²`, đối xứng để tích phân thành `2πrE`, và cách suy ra chiều dòng.
- Giữ các ứng dụng có chức năng khác nhau của dòng Fu-cô: hãm, nung kín, dò kim loại, tổn hao lõi biến áp, nung nóng Io; không bỏ phần lợi và hại.
- Phần trang 978 bắt đầu Guided Practice và Bridging Problem, không thuộc Summary trang 977; chưa inventory đề/lời giải các phần tiếp theo.
