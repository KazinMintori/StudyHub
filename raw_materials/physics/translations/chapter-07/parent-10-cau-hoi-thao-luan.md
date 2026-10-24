## Câu hỏi thảo luận (Discussion Questions)

Mục này phân tích sâu sắc các câu hỏi định tính và bán định lượng cuối Chương 7, làm sáng tỏ bản chất của các khái niệm thế năng, lực thế, sự bảo toàn cơ năng và các đồ thị năng lượng.

---

### Q7.1 - Quả bóng ném thẳng đứng có lực cản không khí

Một quả bóng chày được ném thẳng đứng lên trên với tốc độ ban đầu $v_0$. Nếu không thể bỏ qua lực cản của không khí, khi quả bóng quay trở lại độ cao ban đầu, tốc độ của nó nhỏ hơn $v_0$. Hãy giải thích điều này bằng cách sử dụng các khái niệm năng lượng.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Quả bóng ném lên với tốc độ $v_0$, có lực cản không khí.

- Khi rơi về vị trí ban đầu, tốc độ $v < v_0$.

- Giải thích bằng định luật năng lượng.

**Hướng đi:**

- Phân tích tính chất sinh công của lực cản không khí trong suốt quá trình chuyển động.

- Áp dụng định lý biến thiên cơ năng toàn phần của hệ quả bóng và Trái Đất.

- Xét cơ năng của hệ bóng và Trái Đất vì trọng lực được gộp vào thế năng, còn lực cản là tác dụng ngoài hệ cần tính riêng bằng công.

**Lời giải:**

- Lực cản của không khí là lực không thế (lực tiêu tán) và luôn có hướng ngược với hướng của vectơ vận tốc tức thời của vật.

- Trong giai đoạn bóng đi lên, vận tốc hướng lên trên còn lực cản hướng xuống dưới, do đó lực cản sinh công âm ($W_{\mathrm{air, lên}} < 0$).

- Trong giai đoạn bóng rơi xuống, vận tốc hướng xuống dưới còn lực cản hướng lên trên, nên lực cản tiếp tục sinh công âm ($W_{\mathrm{air, xuống}} < 0$).

- Tổng công của lực cản không khí trên toàn bộ hành trình khép kín là một số âm:
$$
W_{\mathrm{other}} = W_{\mathrm{air}} < 0
$$

- Theo định lý biến thiên cơ năng:
$$
E_2 - E_1 = W_{\mathrm{other}} < 0
$$

- Khi bóng trở lại độ cao ban đầu, thế năng trọng trường bằng đúng thế năng ban đầu ($U_2 = U_1$). Do đó cơ năng giảm hoàn toàn phản ánh vào sự sụt giảm động năng:
$$
\begin{aligned}
K_2 - K_1 &= W_{\mathrm{air}} < 0 \\
\implies K_2 &< K_1.
\end{aligned}
$$

- Vì $K = \frac{1}{2}mv^2$, điều này kéo theo tốc độ khi rơi về vị trí ban đầu nhỏ hơn tốc độ lúc ném:
$$
v < v_0
$$
Năng lượng cơ học bị hao hụt đã chuyển hóa thành nội năng của quả bóng và khối không khí xung quanh, làm nhiệt độ của chúng tăng nhẹ.

</details>

---

### Q7.2 - Chuyển động ném xiên và độ cao cực đại

Một vật phóng có cùng động năng ban đầu bất kể góc bắn. Tại sao vật không đạt được cùng một độ cao cực đại trong mọi trường hợp?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Vật được bắn với cùng động năng ban đầu $K_0$.

- Giải thích tại sao độ cao cực đại khác nhau khi góc bắn thay đổi.

**Hướng đi:**

- Phân tích động học vận tốc tại đỉnh quỹ đạo trong chuyển động ném xiên.

- Vận dụng định luật bảo toàn cơ năng giữa điểm phóng và đỉnh quỹ đạo.

**Lời giải:**

- Khi bỏ qua lực cản không khí, cơ năng toàn phần của vật được bảo toàn trong suốt chuyển động:
$$
E = K_0 = K_{\mathrm{top}} + mgh_{\mathrm{max}}
$$

- Trong chuyển động ném xiên ở góc bắn $\alpha$ so với phương ngang ($0^\circ < \alpha < 90^\circ$), gia tốc trọng trường chỉ tác dụng theo phương thẳng đứng. Thành phần vận tốc theo phương ngang không đổi:
$$
v_x = v_0\cos\alpha \ne 0
$$

- Tại đỉnh cao nhất của quỹ đạo, thành phần vận tốc thẳng đứng triệt tiêu ($v_y = 0$), nhưng vật vẫn chuyển động theo phương ngang với tốc độ $v_x$. Do đó tại đỉnh quỹ đạo, động năng của vật không bằng không:
$$
\begin{aligned}
K_{\mathrm{top}} &= \frac{1}{2}mv_x^2 \\
&= \frac{1}{2}mv_0^2\cos^2\alpha \\
&= K_0\cos^2\alpha.
\end{aligned}
$$

- Thế năng cực đại đạt được là:
$$
\begin{aligned}
mgh_{\mathrm{max}} &= K_0 - K_{\mathrm{top}} \\
&= K_0(1 - \cos^2\alpha) \\
&= K_0\sin^2\alpha.
\end{aligned}
$$

- Độ cao cực đại:
$$
h_{\mathrm{max}} = \frac{K_0\sin^2\alpha}{mg}
$$

- Chỉ trong trường hợp ném thẳng đứng ($\alpha = 90^\circ$), tốc độ tại đỉnh mới hoàn toàn bằng không ($K_{\mathrm{top}} = 0$), khi đó toàn bộ động năng ban đầu mới chuyển hóa hết thành thế năng trọng trường, cho độ cao cực đại lớn nhất $h_{\mathrm{max}} = K_0 / mg$. Khi bắn xiên, một phần động năng buộc phải duy trì cho chuyển động ngang nên độ cao cực đại luôn nhỏ hơn.

</details>

---

### Q7.3 - Trượt trên máng nghiêng và sự phụ thuộc vào hình dạng

Một vật được thả từ trạng thái nghỉ tại đỉnh của một mặt dốc. Nếu mặt dốc không có ma sát, tốc độ của vật ở chân dốc có phụ thuộc vào hình dạng của mặt dốc hay chỉ phụ thuộc vào độ cao của dốc? Giải thích. Nếu mặt dốc có ma sát thì sao?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Thả vật từ đỉnh dốc độ cao $h$.

- Xét sự phụ thuộc của tốc độ ở chân dốc vào hình dạng dốc trong hai trường hợp: Không ma sát và có ma sát.

**Hướng đi:**

- Không ma sát: Xét tính chất lực thế của trọng lực và công của lực pháp tuyến.

- Có ma sát: Xét công của lực ma sát dọc theo quỹ đạo cong.

**Lời giải:**

- Trường hợp dốc không ma sát:
  - Lực tác dụng lên vật gồm trọng lực và phản lực pháp tuyến của mặt dốc. Vì mặt dốc trơn, phản lực pháp tuyến luôn vuông góc với vận tốc tức thời tại mọi điểm trên quỹ đạo, do đó công của phản lực pháp tuyến bằng không:
$$
W_N = 0
$$
  - Trọng lực là lực thế, công của trọng lực chỉ phụ thuộc vào độ chênh lệch độ cao thẳng đứng $h$ giữa điểm đầu và điểm cuối mà không phụ thuộc hình dạng đường đi:
$$
W_g = mgh
$$
  - Theo bảo toàn cơ năng, tốc độ ở chân dốc là $v = \sqrt{2gh}$, chỉ phụ thuộc độ cao chứ hoàn toàn không phụ thuộc vào hình dạng dốc.

- Trường hợp dốc có ma sát:
  - Lực ma sát trượt luôn ngược chiều tiếp tuyến của quỹ đạo, công ma sát là $W_f = -\int f_k ds$.
  - Độ lớn lực ma sát trượt phụ thuộc vào phản lực pháp tuyến: $f_k = \mu_k N$. Trên mặt dốc cong, phản lực $N$ không chỉ phụ thuộc vào góc nghiêng tức thời ($\mu_k mg\cos\theta$) mà còn phụ thuộc vào gia tốc hướng tâm nếu quỹ đạo uốn lượn cong ($N = mg\cos\theta \pm mv^2/R$).
  - Ngoài ra, tổng quãng đường trượt $s = \int ds$ dài ngắn khác nhau tùy theo hình dạng dốc. Do đó công tiêu tán do ma sát phụ thuộc chặt chẽ vào biên dạng của dốc.
  - Tốc độ ở chân dốc:
$$
v = \sqrt{2gh - \frac{2|W_f|}{m}}
$$
  sẽ phụ thuộc trực tiếp vào hình dạng hình học của mặt dốc.

</details>

---

### Q7.4 - Sự thay đổi hệ quy chiếu và năng lượng

Một quả trứng được thả từ trạng thái nghỉ từ mái một tòa nhà và rơi xuống đất. Quá trình rơi được quan sát bởi sinh viên A trên mái nhà (chọn gốc tọa độ tại mái) và sinh viên B dưới mặt đất (chọn gốc tọa độ tại mặt đất). Các giá trị mà hai sinh viên gán cho các đại lượng sau có trùng nhau không: Thế năng trọng trường ban đầu, thế năng trọng trường cuối, độ biến thiên thế năng trọng trường, và động năng của quả trứng ngay trước khi chạm đất? Giải thích.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- So sánh các đại lượng năng lượng giữa hai hệ quy chiếu có gốc tọa độ khác nhau (mái nhà và mặt đất).

**Hướng đi:**

- Định nghĩa thế năng phụ thuộc vào điểm mốc quy ước ($U = mgy$).

- Độ biến thiên thế năng $\Delta U$ và động năng $K$ liên hệ với công cơ học, vốn là đại lượng có tính bất biến đối với phép dời gốc tọa độ tĩnh.

**Lời giải:**

Gọi chiều cao tòa nhà là $h$.

- Thế năng trọng trường ban đầu ($U_i$):
  - Sinh viên A (gốc tại mái nhà $y_A = 0$): $U_{i,A} = 0$.
  - Sinh viên B (gốc tại mặt đất $y_B = 0$, mái nhà có tọa độ $y_B = h$): $U_{i,B} = mgh$.
  - Hai giá trị này không trùng nhau.

- Thế năng trọng trường cuối ($U_f$):
  - Sinh viên A (mặt đất có tọa độ $y_A = -h$): $U_{f,A} = -mgh$.
  - Sinh viên B (mặt đất có tọa độ $y_B = 0$): $U_{f,B} = 0$.
  - Hai giá trị này không trùng nhau.

- Độ biến thiên thế năng trọng trường ($\Delta U = U_f - U_i$):
  - Sinh viên A: $\Delta U_A = -mgh$.
  - Sinh viên B: $\Delta U_B = -mgh$.
  - Hai giá trị này hoàn toàn trùng khớp nhau.

- Động năng của quả trứng ngay trước khi chạm đất ($K_f$):
  - Vì thả rơi tự do từ trạng thái nghỉ ($v_0 = 0$), công của trọng lực thực hiện lên quả trứng là $W = -\Delta U = mgh$.
  - Định lý công và động năng cho $K_f = W = mgh$.
  - Cả hai sinh viên đều đo được cùng một độ biến thiên độ cao và cùng một tốc độ chạm đất, nên giá trị động năng của hai sinh viên là hoàn toàn trùng nhau.

Kết luận: Giá trị thế năng phụ thuộc cách chọn mốc thế năng. Khi chỉ đổi mốc bằng cách cộng một hằng số, độ biến thiên thế năng và kết quả tính động năng không đổi.

</details>

---

### Q7.5 - Thí nghiệm con lắc quả bóng bowling và kết cục nguy hiểm

Một giáo viên vật lý treo một quả bóng bowling nặng bằng sợi dây dài gắn vào trần giảng đường. Để chứng minh niềm tin vào định luật bảo toàn năng lượng, thầy đứng sát một bên bục giảng, kéo quả bóng sang một bên cho đến khi sợi dây căng đưa bóng chạm sát chóp mũi mình, rồi buông tay thả nhẹ không vận tốc đầu. Quả bóng vung một vòng cung lớn rồi quay trở lại dừng lại tức thời ngay trước mũi thầy mà thầy không hề chớp mắt. Tuy nhiên, sau buổi học, một học sinh bắt chước biểu diễn nhưng lại đẩy quả bóng ra xa mũi mình khi bắt đầu thả. Hãy kể tiếp câu chuyện và giải thích nguyên nhân của kết cục nguy hiểm này.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Thả bóng từ trạng thái nghỉ: Bóng quay lại vị trí cũ an toàn.

- Đẩy bóng khi thả: Phân tích cơ năng và nguy cơ chấn thương.

**Hướng đi:**

- So sánh cơ năng toàn phần của con lắc trong hai trường hợp: Thả không vận tốc đầu ($v_0 = 0$) và đẩy có vận tốc ban đầu ($v_0 > 0$).

- Sử dụng định luật bảo toàn cơ năng để xác định vị trí biên và vận tốc khi bóng quay trở lại vị trí ban đầu.

**Lời giải:**

- Trường hợp của người thầy:
  - Thầy thả bóng từ trạng thái nghỉ ($v_0 = 0$) tại độ cao ban đầu $y_0$. Cơ năng ban đầu chỉ gồm thế năng trọng trường:
$$
E = mgy_0
$$
  - Khi bóng dao động qua lại, nếu bỏ qua lực cản không khí, bóng quay lại độ cao đúng bằng $y_0$ và dừng lại tức thời ($v = 0$). Trong thực tế có lực cản không khí nhẹ tiêu tán một phần cơ năng ($W_{\mathrm{air}} < 0$), cơ năng giảm khiến độ cao quay về thực tế $y_{\mathrm{quay về}} \le y_0$, do đó bóng dừng lại cách mũi thầy một khoảng an toàn nhỏ.

- Trường hợp của học sinh:
  - Học sinh đã đẩy quả bóng về phía trước, tức là truyền cho quả bóng một vận tốc ban đầu $v_0 > 0$.
  - Cơ năng ban đầu của hệ khi đó lớn hơn thế năng tại vị trí thả:
$$
E_{\mathrm{hs}} = mgy_0 + \frac{1}{2}mv_0^2
$$
  - Khi quả bóng hoàn thành chu kỳ dao động và quay trở lại tọa độ vị trí thả ($y = y_0$), theo định luật bảo toàn cơ năng (bỏ qua phần hao phí rất nhỏ do không khí):
$$
E = mgy_0 + \frac{1}{2}mv^2 = E_{\mathrm{hs}}
$$
  - Suy ra tại vị trí ngang chóp mũi học sinh, quả bóng vẫn còn tốc độ đúng bằng tốc độ lúc đẩy:
$$
v \approx v_0 > 0
$$
  - Do vẫn còn động năng và tiếp tục lao về phía sau để đạt độ cao cực đại mới ($y_{\mathrm{max}} = y_0 + v_0^2/2g$), quả bóng có thể va vào mặt học sinh nếu người ấy đứng nguyên ở vị trí ban đầu. Việc đẩy bóng đã phá vỡ điều kiện thả từ trạng thái nghỉ vốn bảo đảm an toàn trong phép minh họa.

</details>

---

### Q7.6 - Lực ma sát và khả năng tăng cơ năng

Lực ma sát có thể làm tăng cơ năng toàn phần của một hệ không? Nếu có, hãy nêu ví dụ minh họa.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Xét dấu công của ma sát đối với hệ được chọn và cho ví dụ khi cơ năng của hệ tăng.

**Hướng đi:**

- Chọn rõ ranh giới hệ, vì ma sát giữa hai vật có thể là ngoại lực đối với một vật riêng lẻ.

- Dùng $W=\int\vec F\cdot d\vec r$ để xét dấu công, với $d\vec r$ là độ dời của điểm đặt lực trong hệ quy chiếu đang xét.

- Với vật trượt trên mặt phẳng ngang, thế năng không đổi nên công dương của ma sát làm tăng động năng.

**Lời giải:**

Có. Chẳng hạn, đặt một kiện hàng trên sàn xe tải và cho xe tăng tốc. Nếu kiện hàng không trượt so với sàn xe, ma sát nghỉ đẩy nó về phía trước. Trong hệ quy chiếu gắn với mặt đất, điểm đặt lực trên kiện hàng dịch chuyển theo chiều lực, nên công của ma sát dương và động năng kiện hàng tăng.

Một ví dụ khác là đặt kiện hàng đang đứng yên lên băng chuyền chuyển động. Khi kiện hàng còn trượt so với băng, ma sát trượt kéo nó theo chiều băng chuyền. Lực này sinh công dương lên kiện hàng và làm kiện hàng tăng tốc. Năng lượng được truyền từ động cơ băng chuyền, đồng thời một phần chuyển thành nội năng tại chỗ tiếp xúc.

Đối với hệ gồm cả hai bề mặt trượt, tổng công của cặp lực ma sát làm giảm cơ năng. Điều đó không buộc công của từng lực ma sát lên từng vật phải âm.

Khi đi bộ hoặc lăn không trượt trên mặt đất đứng yên, điểm tiếp xúc tức thời đứng yên trong mô hình lý tưởng, nên ma sát nghỉ tại đó không sinh công thực. Năng lượng làm tăng động năng trong các trường hợp ấy xuất phát từ nội năng cơ thể hoặc động cơ.

</details>

---

### Q7.7 - Nhún nhảy trên bạt nhún lò xo (Trampoline)

Một người phụ nữ nhún nhảy trên bạt lò xo (trampoline), sau mỗi lần bật lại nhảy lên cao hơn lần trước. Hãy giải thích cách cô ấy làm tăng cơ năng toàn phần của hệ.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Giải thích cơ chế gia tăng cơ năng khi nhún bạt lò xo để nhảy cao dần.

**Hướng đi:**

- Xác định các thành phần năng lượng trong hệ.

- Chỉ ra nguồn năng lượng bổ sung từ công của nội lực sinh học (cơ bắp).

**Lời giải:**

- Nếu người phụ nữ giữ cơ thể cứng như một vật không biến dạng, cô không chủ động cung cấp thêm cơ năng cho chuyển động. Hệ gồm người và bạt vẫn mất cơ năng qua lực cản không khí cùng sự tiêu tán trong vật liệu, nên độ cao mỗi lần nảy giảm dần.

- Để nhảy cao hơn sau mỗi lần chạm bạt, người phụ nữ đã chủ động gập chân và đạp mạnh duỗi thẳng cơ thể đúng vào thời điểm bạt nhún đang đạt độ võng cực đại đi lên.

- Quá trình đạp chân này thực hiện công dương lên hệ: Các cơ bắp co giãn sinh công cơ học $W_{\mathrm{cơ bắp}} > 0$.

- Nguồn gốc của công cơ học này xuất phát từ hóa năng sinh học (năng lượng dự trữ trong liên kết hóa học ATP từ thức ăn chuyển hóa) bên trong cơ thể người.

- Hóa năng chuyển hóa thành cơ năng bổ sung cho hệ qua mỗi chu kỳ:
$$
\Delta E = W_{\mathrm{cơ}} - |W_{\mathrm{tiêu tán}}| > 0
$$
Nhờ đó cơ năng toàn phần tăng lên sau mỗi lần nhún, cho phép cô ấy đạt độ cao ngày càng lớn hơn.

</details>

---

### Q7.8 - Ngôn ngữ đời sống và bản chất năng lượng (Fractured Physics)

Trong đời sống, người ta thường gọi hóa đơn tiền điện là "hóa đơn tiền công suất" (power bill), tuy nhiên đại lượng dùng để tính tiền trên hóa đơn lại được ghi bằng đơn vị kilowatt-giờ ($\mathrm{kW\cdot h}$). Thực chất người tiêu dùng đang phải trả tiền cho đại lượng vật lý nào?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Phân biệt giữa công suất (power) và năng lượng (energy) thông qua đơn vị kilowatt-giờ.

**Hướng đi:**

- Phân tích định nghĩa công suất và mối liên hệ tích phân giữa công suất, thời gian và năng lượng tiêu thụ.

**Lời giải:**

- Người tiêu dùng thực chất đang trả tiền cho điện năng tiêu thụ (năng lượng), chứ không phải công suất.

- Công suất ($P$) là tốc độ tiêu thụ hoặc truyền tải năng lượng trên một đơn vị thời gian:
$$
P = \frac{\Delta E}{\Delta t}
$$
Đơn vị đo công suất trong hệ SI là watt ($\mathrm{W}$) hoặc kilowatt ($1\,\mathrm{kW} = 10^3\,\mathrm{W}$).

- Khi nhân công suất với khoảng thời gian sử dụng ($\Delta t$), ta nhận được tổng năng lượng tiêu thụ:
$$
\Delta E = P \cdot \Delta t
$$

- Kilowatt-giờ ($\mathrm{kW\cdot h}$) là tích của đơn vị công suất ($\mathrm{kW}$) và đơn vị thời gian ($\mathrm{h}$), do đó đây là một đơn vị đo năng lượng:
$$
\begin{aligned}
1\,\mathrm{kW\cdot h} &= (1000\,\mathrm{W})(3600\,\mathrm{s}) \\
&= 3{,}60 \times 10^6\,\mathrm{J} \\
&= 3{,}60\,\mathrm{MJ}.
\end{aligned}
$$

- Do đó, việc gọi là "tiền công suất" trong ngôn ngữ thông dụng là sai lệch về mặt thuật ngữ vật lý. Đại lượng được tính tiền chính là tổng lượng điện năng tiêu thụ đo bằng kilowatt-giờ.

</details>

---

### Q7.9 - Dấu của công trọng lực và độ biến thiên thế năng

(a) Một cuốn sách được nâng thẳng đứng lên trên một đoạn $0{,}800\,\mathrm{m}$. Trong độ dời này, trọng lực tác dụng lên cuốn sách thực hiện công dương hay công âm? Thế năng trọng trường của cuốn sách tăng hay giảm?
(b) Một hộp đậu rơi tự do từ trạng thái nghỉ xuống dưới một đoạn thẳng đứng $2{,}00\,\mathrm{m}$. Trong độ dời này, trọng lực tác dụng lên hộp thực hiện công dương hay công âm? Thế năng trọng trường của hộp tăng hay giảm?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Xác định dấu của công trọng lực và xu hướng biến thiên của thế năng trọng trường khi vật đi lên và đi xuống.

**Hướng đi:**

- Công của một lực không đổi: $W = \vec{F} \cdot \Delta\vec{r} = F \Delta y \cos\phi$.

- Mối liên hệ tổng quát giữa công của lực thế và độ biến thiên thế năng:
$$
W = -\Delta U
$$

- Dùng công để liên hệ hai trạng thái vì một lực thế sinh công bằng độ giảm thế năng, không phụ thuộc việc ta chọn mức thế năng bằng không ở đâu.

**Lời giải:**

(a) Nâng cuốn sách lên cao $0{,}800\,\mathrm{m}$:

- Trọng lực hướng thẳng đứng xuống dưới, trong khi vectơ độ dời hướng thẳng đứng lên trên ($\phi = 180^\circ$).

- Công của trọng lực là công âm:
$$
W_g = -mgd < 0
$$

- Độ biến thiên thế năng trọng trường:
$$
\Delta U_g = +mgd > 0
$$

- Do đó, thế năng trọng trường của cuốn sách tăng.

(b) Hộp đậu rơi xuống dưới $2{,}00\,\mathrm{m}$:

- Trọng lực hướng thẳng đứng xuống dưới, cùng hướng với vectơ độ dời ($\phi = 0^\circ$).

- Công của trọng lực là công dương:
$$
W_g = +mgd > 0
$$

- Độ biến thiên thế năng trọng trường:
$$
\Delta U_g = -mgd < 0
$$

- Do đó, thế năng trọng trường của hộp đậu giảm.

Quy tắc tổng quát: Khi vật chuyển động theo chiều lực thế hướng đến, lực thế sinh công dương và thế năng giảm. Khi vật đi ngược chiều lực thế, lực thế sinh công âm và thế năng tăng.

</details>

---

### Q7.10 - Dấu của công lực đàn hồi và thế năng lò xo

(a) Một khối gỗ bị ấn ép vào một lò xo làm lò xo bị nén một đoạn $0{,}080\,\mathrm{m}$. Lực do lò xo tác dụng lên khối gỗ thực hiện công dương hay công âm? Thế năng tích trữ trong lò xo tăng hay giảm?
(b) Đặt một khối gỗ lên đỉnh một lò xo thẳng đứng đang bị nén $6{,}00\,\mathrm{cm}$. Thả lò xo để nó đẩy khối gỗ đi lên. Từ vị trí lò xo bị nén $6{,}00\,\mathrm{cm}$ đến vị trí chỉ còn bị nén $2{,}00\,\mathrm{cm}$ (khối gỗ đi lên $4{,}00\,\mathrm{cm}$), lực đàn hồi của lò xo thực hiện công dương hay công âm lên khối gỗ? Trong chuyển động này, thế năng tích trữ trong lò xo tăng hay giảm?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Xác định dấu của công lực đàn hồi và biến thiên thế năng đàn hồi trong hai giai đoạn nén thêm và dãn bớt của lò xo.

**Hướng đi:**

- Lực đàn hồi là lực hồi phục luôn hướng về vị trí ứng với chiều dài tự nhiên ($F_x = -kx$).

- Công của lực đàn hồi liên hệ với thế năng: $W_{\mathrm{el}} = -\Delta U_{\mathrm{el}}$.

- Dùng thế năng đàn hồi vì trong mô hình Hooke, lực đổi theo độ biến dạng. Dấu công được xác định bởi lò xo đang tiến về hay rời xa chiều dài tự nhiên.

**Lời giải:**

(a) Khối gỗ ép làm nén lò xo:

- Chiều dịch chuyển của khối gỗ là hướng vào trong để nén lò xo thêm.

- Lực đàn hồi do lò xo tác dụng lên khối gỗ hướng đẩy ngược trở lại vị trí cân bằng, ngược chiều dịch chuyển của khối gỗ.

- Do lực ngược chiều chuyển động, lực đàn hồi thực hiện công âm lên khối gỗ:
$$
W_{\mathrm{el}} < 0
$$

- Vì $W_{\mathrm{el}} = -\Delta U_{\mathrm{el}}$, ta có $\Delta U_{\mathrm{el}} = -W_{\mathrm{el}} > 0$. Thế năng đàn hồi tích trữ trong lò xo tăng lên.

(b) Lò xo đẩy khối gỗ bung lên từ độ nén $6{,}00\,\mathrm{cm}$ về $2{,}00\,\mathrm{cm}$:

- Khối gỗ chuyển động hướng lên trên. Lực đàn hồi của lò xo bị nén cũng hướng lên trên để đẩy vật về vị trí tự nhiên.

- Vì lực đàn hồi cùng chiều chuyển động, lực đàn hồi thực hiện công dương lên khối gỗ:
$$
\begin{aligned}
W_{\mathrm{el}} &= \frac{1}{2}k(x_1^2 - x_2^2) \\
&> 0.
\end{aligned}
$$

- Thế năng đàn hồi lúc đầu là $U_1 = \frac{1}{2}kx_1^2$, lúc sau là $U_2 = \frac{1}{2}kx_2^2$. Vì độ biến dạng giảm từ $6{,}00\,\mathrm{cm}$ xuống $2{,}00\,\mathrm{cm}$ nên thế năng đàn hồi tích trữ trong lò xo giảm.

</details>

---

### Q7.11 - Hai hòn đá rơi tự do có khối lượng khác nhau

Một hòn đá $1{,}0\,\mathrm{kg}$ và một hòn đá $10{,}0\,\mathrm{kg}$ được thả rơi từ trạng thái nghỉ tại cùng một độ cao so với mặt đất. Bỏ qua lực cản của không khí. Trong các phát biểu sau đây, phát biểu nào đúng? Giải thích cặn kẽ từng trường hợp.
(a) Cả hai có cùng thế năng trọng trường ban đầu.
(b) Cả hai có cùng gia tốc khi rơi.
(c) Cả hai có cùng tốc độ khi chạm đất.
(d) Cả hai có cùng động năng khi chạm đất.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- So sánh các đại lượng động học và năng lượng của hai vật rơi tự do có khối lượng chênh lệch 10 lần.

**Hướng đi:**

- Áp dụng các định nghĩa thế năng $U = mgh$, động năng $K = \frac{1}{2}mv^2$ và định luật II Newton cho rơi tự do.

**Lời giải:**

(a) "Cả hai có cùng thế năng trọng trường ban đầu": SAI.

- Biểu thức thế năng trọng trường là $U = mgh$.

- Với cùng độ cao $h$, hòn đá $10{,}0\,\mathrm{kg}$ có khối lượng gấp 10 lần hòn đá $1{,}0\,\mathrm{kg}$, do đó thế năng ban đầu của hòn đá lớn gấp 10 lần thế năng của hòn đá nhỏ:
$$
U_{10} = 10 \cdot U_{1}
$$

(b) "Cả hai có cùng gia tốc khi rơi": ĐÚNG.

- Khi rơi tự do, lực duy nhất tác dụng là trọng lực $P = mg$. Theo định luật II Newton:
$$
a = \frac{P}{m} = \frac{mg}{m} = g
$$

- Gia tốc rơi của hai vật đều bằng gia tốc trọng trường $g = 9{,}80\,\mathrm{m/s^2}$, độc lập với khối lượng.

(c) "Cả hai có cùng tốc độ khi chạm đất": ĐÚNG.

- Áp dụng định luật bảo toàn cơ năng, tốc độ khi chạm đất:
$$
v = \sqrt{2gh}
$$

- Tốc độ chạm đất chỉ phụ thuộc độ cao thả $h$ và gia tốc $g$, do đó cả hai hòn đá chạm đất với cùng tốc độ.

(d) "Cả hai có cùng động năng khi chạm đất": SAI.

- Động năng chạm đất bằng thế năng ban đầu: $K = \frac{1}{2}mv^2 = mgh$.

- Vì hai vật có cùng tốc độ $v$ nhưng khối lượng khác nhau, hòn đá $10{,}0\,\mathrm{kg}$ có động năng chạm đất gấp 10 lần hòn đá $1{,}0\,\mathrm{kg}$.

</details>

---

### Q7.12 - Phóng hai vật bằng hai lò xo nén giống nhau

Hai vật có khối lượng khác nhau được phóng thẳng đứng lên không trung bằng cách đặt chúng lên hai lò xo giống hệt nhau bị nén cùng một đoạn rồi thả nhẹ. Bỏ qua lực cản của không khí và khối lượng của các lò xo. Trong các phát biểu sau, phát biểu nào đúng? Giải thích từng câu.
(a) Cả hai vật đạt cùng độ cao cực đại.
(b) Tại độ cao cực đại, cả hai vật có cùng thế năng trọng trường nếu chọn mốc thế năng ban đầu của mỗi vật bằng không.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Hai vật khối lượng $m_1 \ne m_2$ bắn bằng hai lò xo cùng độ cứng $k$ và cùng độ nén $d$.

- Đánh giá độ cao cực đại và thế năng trọng trường tại đỉnh.

**Hướng đi:**

- Xác định năng lượng ban đầu tích trữ trong lò xo: $E = \frac{1}{2}kd^2$.

- Áp dụng định luật bảo toàn cơ năng cho toàn hệ thống.

**Lời giải:**

(a) "Cả hai vật đạt cùng độ cao cực đại": SAI.

- Cơ năng ban đầu của mỗi hệ đều bằng thế năng đàn hồi của lò xo:
$$
E = \frac{1}{2}kd^2
$$

- Tại độ cao cực đại $h$ tính từ vị trí thả, tốc độ của vật bằng không nên động năng triệt tiêu. Toàn bộ năng lượng chuyển thành thế năng trọng trường $mgh = \frac{1}{2}kd^2$:
$$
h = \frac{kd^2}{2mg}
$$

- Độ cao cực đại $h$ tỉ lệ nghịch với khối lượng $m$. Vật có khối lượng lớn hơn sẽ đạt độ cao cực đại thấp hơn vật có khối lượng nhỏ.

(b) "Tại độ cao cực đại, cả hai vật có cùng thế năng trọng trường": ĐÚNG.

- Chọn mốc thế năng trọng trường tại vị trí thả ban đầu ($U_g = 0$).

- Theo định luật bảo toàn cơ năng, không có ma sát và lực cản, cơ năng toàn phần tại vị trí cao nhất bằng cơ năng ban đầu:
$$
U_{g,\mathrm{max}} = E = \frac{1}{2}kd^2
$$

- Vì cả hai lò xo có cùng độ cứng $k$ và cùng độ nén ban đầu $d$, cơ năng ban đầu của hai hệ là như nhau. Do đó tại độ cao cực đại tương ứng của mỗi vật, thế năng trọng trường của chúng là hoàn toàn bằng nhau và đều bằng $\frac{1}{2}kd^2$.

</details>

---

### Q7.13 - Xoa tay làm ấm và nguồn gốc nhiệt năng

Khi bị lạnh, người ta thường xoa hai bàn tay vào nhau để làm ấm. Động tác này sinh ra nhiệt như thế nào? Lượng nhiệt này có nguồn gốc từ đâu?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Phân tích cơ chế sinh nhiệt và nguồn gốc năng lượng khi xoa hai bàn tay.

**Hướng đi:**

- Phân tích công của lực ma sát trượt giữa hai lòng bàn tay.

- Lần theo chuỗi chuyển hóa năng lượng từ cấp độ sinh học đến nhiệt năng.

**Lời giải:**

- Cơ chế sinh nhiệt:
  - Khi hai lòng bàn tay áp sát vào nhau và chuyển động trượt tương đối qua lại, giữa hai lớp da xuất hiện lực ma sát trượt.
  - Lực ma sát trượt này thực hiện công cơ học âm lên hệ hai bàn tay, chuyển hóa cơ năng thành nội năng (năng lượng nhiệt).
  - Nội năng gia tăng làm các phân tử tế bào ở bề mặt da dao động nhiệt mạnh hơn, biểu hiện thành sự tăng nhiệt độ cục bộ ở hai lòng bàn tay, giúp làm ấm cơ thể.

- Nguồn gốc của nhiệt lượng:
  - Để duy trì sự chuyển động qua lại của hai bàn tay thắng lực ma sát, các nhóm cơ cánh tay và bàn tay phải liên tục co duỗi để sinh công cơ học.
  - Hoạt động của cơ bắp sử dụng năng lượng sinh hóa lấy từ sự thủy phân các liên kết giàu năng lượng ATP (được tổng hợp từ quá trình chuyển hóa thức ăn hấp thụ vào cơ thể).
  - Tóm lại, chuỗi chuyển hóa năng lượng là: Hóa năng sinh học $\longrightarrow$ Công cơ học của cơ bắp $\longrightarrow$ Nội năng (nhiệt qua ma sát).

</details>

---

### Q7.14 - So sánh công của trọng lực và lực ma sát trên dốc

Một chiếc hộp trượt xuống dốc, chịu tác dụng của trọng lực và lực ma sát. Công của mỗi lực này có thể được biểu diễn thông qua độ biến thiên của một hàm thế năng không? Giải thích rõ lý do cho từng lực.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Xét khả năng biểu diễn công qua hàm thế năng đối với trọng lực và lực ma sát trượt.

**Hướng đi:**

- Điều kiện cần và đủ để một lực có thể định nghĩa hàm thế năng tương ứng là lực đó phải là lực bảo toàn (lực thế), tức là công của lực trên đường cong kín bất kỳ phải bằng không.

**Lời giải:**

- Trọng lực: Có thể biểu diễn qua hàm thế năng.
  - Lý do: Trọng lực là lực bảo toàn (lực thế). Hướng của trọng lực luôn không đổi (hướng thẳng đứng xuống dưới) và độ lớn không đổi tại gần mặt đất ($P = mg$).
  - Công của trọng lực khi vật di chuyển giữa hai điểm chỉ phụ thuộc vào độ chênh lệch độ cao thẳng đứng giữa điểm đầu và điểm cuối mà hoàn toàn không phụ thuộc vào hình dạng quỹ đạo di chuyển. Do đó ta có thể định nghĩa hàm thế năng trọng trường $U_g(y) = mgy$, sao cho:
$$
W_g = -(U_{g,2} - U_{g,1})
$$

- Lực ma sát: KHÔNG THỂ biểu diễn qua hàm thế năng.
  - Lý do: Lực ma sát trượt là lực không bảo toàn (lực tiêu tán). Lực này luôn tự động đổi hướng để ngược chiều với vectơ vận tốc tiếp tuyến tức thời của vật tại từng thời điểm.
  - Công của lực ma sát luôn là công âm trên mọi phần tử dịch chuyển dọc theo đường đi, và trên một hành trình khép kín quay về vị trí cũ, tổng công của lực ma sát là một số âm khác không:
$$
\oint \vec{f}_k \cdot d\vec{r} < 0
$$
  - Vì công phụ thuộc vào toàn bộ chiều dài quỹ đạo và không thể phục hồi lại cơ năng ban đầu, không tồn tại một hàm số tọa độ vị trí $U(\vec{r})$ nào có thể biểu diễn được công của lực ma sát. Năng lượng do ma sát sinh ra bị tiêu tán thành nội năng.

</details>

---

### Q7.15 - Bản chất vật lý của lực ma sát và việc lưu trữ năng lượng

Dưới góc độ vật lý, hãy giải thích tại sao lực ma sát lại là lực không bảo toàn. Nó có tích trữ năng lượng để sử dụng trong tương lai không?

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Giải thích bản chất không bảo toàn của ma sát và khả năng tích trữ năng lượng.

**Hướng đi:**

- Phân tích sự mất mát cơ năng và bản chất vi mô của sự tiêu tán nhiệt.

- Xét cả nội năng vì cơ năng giảm do ma sát không có nghĩa là tổng năng lượng biến mất. Chuyển động nhiệt giải thích phần năng lượng còn lại.

**Lời giải:**

- Tại sao lực ma sát là lực không bảo toàn:
  - Một lực được gọi là bảo toàn nếu công nó thực hiện làm thay đổi động năng có thể được thu hồi trọn vẹn khi vật quay trở lại vị trí ban đầu.
  - Lực ma sát trượt luôn ngược chiều với vectơ vận tốc tức thời $\vec{v}$. Khi vật đi theo chiều thuận, lực ma sát sinh công âm. Khi vật quay ngược lại đường cũ, lực ma sát đổi chiều ngược lại và tiếp tục sinh công âm. Công trên một đường khép kín luôn khác không:
$$
W_{\mathrm{khép kín}} < 0
$$
  - Ở chỗ tiếp xúc, các phân tử tương tác, những liên kết hình thành rồi đứt. Khi hai bề mặt trượt, một phần năng lượng chuyển động có trật tự chuyển thành nội năng, làm tăng chuyển động nhiệt của vật chất.

- Khả năng tích trữ năng lượng:
  - Lực ma sát KHÔNG tích trữ năng lượng dưới dạng thế năng có thể tái sử dụng cho chuyển động cơ học trong tương lai.
  - Cơ năng bị mất mát chuyển thành nội năng (nhiệt), làm nóng các vật thể tiếp xúc và phân tán vào môi trường. Theo nguyên lý nhiệt động lực học, nhiệt phân tán ngẫu nhiên này không thể tự phát chuyển hóa hoàn toàn ngược trở lại thành cơ năng có hướng để đẩy vật chuyển động.

</details>

---

### Q7.16 - Lựa chọn mốc thế năng đàn hồi của lò xo

Vì chỉ có độ biến thiên thế năng là có ý nghĩa trong các bài toán vật lý, một học sinh quyết định chọn thế năng đàn hồi của lò xo bằng không khi lò xo đang dãn một khoảng $x_1$. Do đó học sinh chọn hàm thế năng là $U = \frac{1}{2}k(x - x_1)^2$. Cách làm này có đúng không? Giải thích.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Đánh giá tính đúng đắn của việc dời gốc thế năng đàn hồi theo công thức $U = \frac{1}{2}k(x - x_1)^2$.

**Hướng đi:**

- Sử dụng mối liên hệ vi phân cơ bản giữa lực và hàm thế năng một chiều:
$$
F_x = -\frac{dU}{dx}
$$

- Xét đạo hàm vì giá trị thế năng tại một điểm không tự cho biết độ dốc của đồ thị, trong khi lực được quyết định bởi độ dốc ấy.

**Lời giải:**

- Cách làm của học sinh là HOÀN TOÀN SAI.

- Giải thích:
  - Lực đàn hồi của lò xo tuân theo định luật Hooke có biểu thức thực tế là $F_x = -kx$, trong đó $x = 0$ là vị trí lò xo không biến dạng (vị trí cân bằng tự nhiên nơi lực bằng không).
  - Nếu học sinh sử dụng hàm thế năng $U = \frac{1}{2}k(x - x_1)^2$, thì lực tương ứng thu được bằng cách lấy đạo hàm đổi dấu là:
$$
\begin{aligned}
F_x &= -\frac{dU}{dx} \\
&= -k(x - x_1).
\end{aligned}
$$
  - Biểu thức này ngụ ý rằng lực đàn hồi bằng không tại vị trí $x = x_1$ và hướng về vị trí $x = x_1$. Điều này hoàn toàn sai lệch về mặt vật lý, vì tại vị trí lò xo dãn $x_1 \ne 0$, lò xo thực tế đang bị kéo dãn và đang tác dụng một lực kéo thực tế bằng $-kx_1 \ne 0$, chứ lực không thể bằng không.

- Cách chọn mốc thế năng đúng:
  - Để thế năng bằng không tại $x = x_1$ mà không làm thay đổi bản chất lực của hệ, ta chỉ được phép cộng thêm một hằng số $C$ vào hàm thế năng chuẩn:
$$
U(x) = \frac{1}{2}kx^2 + C
$$
  - Với điều kiện $U(x_1) = 0$, ta có $C = -\frac{1}{2}kx_1^2$. Khi đó hàm thế năng đúng quy tắc phải là:
$$
U(x) = \frac{1}{2}kx^2 - \frac{1}{2}kx_1^2
$$
  - Khi lấy đạo hàm, hằng số bị triệt tiêu và ta thu lại đúng lực vật lý $F_x = -dU/dx = -kx$.

</details>

---

### Q7.17 - Đồ thị thế năng của lực đẩy $F_x = +kx$

Hình 7.22a thể hiện đồ thị thế năng của lực hồi phục $F_x = -kx$. Hãy phác họa dạng đồ thị thế năng cho lực $F_x = +kx$. Đối với lực này, vị trí $x = 0$ có phải là điểm cân bằng không? Trạng thái cân bằng này là bền hay không bền? Giải thích.

![Hình 7.22: Thế năng của lò xo và thế năng trọng trường](/vat-ly-1/bai-giang/img/young-07/r-theory-hinh-7-22.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Phân tích hàm thế năng, điểm cân bằng và tính bền vững của lực $F_x = +kx$.

**Hướng đi:**

- Tích phân lực để tìm hàm thế năng: $U(x) = -\int F_x dx$.

- Xét điều kiện cân bằng ($F_x = 0$) và dấu của đạo hàm bậc hai $d^2U/dx^2$.

**Lời giải:**

- Xác định hàm thế năng:
  - Mối liên hệ vi phân: $dU = -F_x dx = -(kx)dx$.
  - Tích phân với điều kiện chọn mốc thế năng $U(0) = 0$:
$$
U(x) = -\frac{1}{2}kx^2
$$
  - Dạng đồ thị: Đồ thị thế năng $U(x)$ là một đường parabol có đỉnh tại gốc tọa độ $(0, 0)$ và bề lõm quay xuống dưới.

![Đồ thị thế năng dạng parabol quay xuống, cực đại tại vị trí cân bằng không bền x bằng không.](/vat-ly-1/bai-giang/img/young-07/r-solution-q717-unstable.svg)

- Điểm cân bằng:
  - Tại vị trí $x = 0$, ta có $F_x = +k(0) = 0$.
  - Vì hợp lực tác dụng lên hạt bằng không, vị trí $x = 0$ là một điểm cân bằng.

- Tính ổn định của cân bằng:
  - Đây là trạng thái cân bằng không bền (unstable equilibrium).
  - Về mặt toán học: Đạo hàm bậc hai của thế năng là:
$$
\frac{d^2U}{dx^2} = -k < 0
$$
  Thế năng đạt giá trị cực đại địa phương tại $x = 0$.
  - Về mặt cơ học: Giả sử hạt bị dịch chuyển nhẹ khỏi vị trí cân bằng một đoạn nhỏ $\Delta x > 0$. Lực tác dụng khi đó là $F_x = +k\Delta x > 0$, hướng cùng chiều với độ lệch và đẩy hạt ngày càng ra xa vị trí cân bằng hơn chứ không kéo hạt quay về.

</details>

---

### Q7.18 - Đọc hướng trọng lực từ đồ thị thế năng

Hình 7.22b biểu diễn hàm thế năng ứng với trọng lực giữa một vật và Trái Đất. Hãy dùng đồ thị này để giải thích vì sao vật rơi về phía Trái Đất khi được thả tự do.

![Hình 7.22: Thế năng của lò xo và thế năng trọng trường](/vat-ly-1/bai-giang/img/young-07/r-theory-hinh-7-22.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Dùng đồ thị thế năng trọng trường $U(y)=mgy$ trong Hình 7.22b để xác định hướng của trọng lực. Trục $y$ hướng thẳng đứng lên trên.

**Hướng đi:**

- Dùng $F_y=-dU/dy$, vì lực theo một tọa độ bằng đạo hàm đổi dấu của thế năng theo tọa độ ấy.

- Đọc dấu của độ dốc đường thẳng $U(y)$ để xác định dấu của $F_y$.

**Lời giải:**

Đồ thị $U(y)=mgy$ là đường thẳng đi lên khi $y$ tăng, có độ dốc $mg>0$. Do đó:

$$
F_y=-\frac{dU}{dy}=-mg<0.
$$

Trọng lực hướng theo chiều âm của trục $y$, tức là hướng xuống phía Trái Đất. Khi vật được thả từ trạng thái nghỉ, gia tốc có cùng hướng với trọng lực nên vật bắt đầu rơi xuống. Trong mô hình bỏ qua lực cản, thế năng giảm và động năng tăng một lượng tương ứng.

</details>

---

### Q7.19 - Dấu của thế năng tương tác ở khoảng cách hữu hạn

Đối với một hệ gồm hai hạt, người ta thường quy ước thế năng tương tác giữa hai hạt tiến về không khi khoảng cách giữa chúng tiến ra vô cùng ($U(\infty) = 0$). Với quy ước này, hãy giải thích tại sao ở khoảng cách hữu hạn, thế năng lại mang giá trị dương nếu hai hạt đẩy nhau và mang giá trị âm nếu hai hạt hút nhau.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Giải thích dấu của hàm thế năng ở khoảng cách hữu hạn khi chọn $U(\infty) = 0$ cho lực đẩy và lực hút.

**Hướng đi:**

- Sử dụng định nghĩa công của lực tương tác khi đưa hai hạt từ khoảng cách $r$ ra vô cùng:
$$
W_{r \to \infty} = U(r)
$$

**Lời giải:**

- Theo định nghĩa của hàm thế năng, công do nội lực tương tác thực hiện khi khoảng cách giữa hai hạt tăng từ $r$ đến $\infty$ là:
$$
W_{r \to \infty} = -\Delta U
$$

- Với quy ước chuẩn $U(\infty) = 0$, ta có mối liên hệ trực tiếp:
$$
U(r) = W_{r \to \infty}
$$

- Trường hợp hai hạt đẩy nhau:
  - Lực tương tác giữa hai hạt là lực đẩy, có hướng đẩy hai hạt ra xa nhau, tức là cùng hướng với vectơ dịch chuyển từ $r$ ra $\infty$.
  - Lực đẩy do đó sinh công dương trong quá trình hai hạt tách xa nhau:
$$
W_{r \to \infty} > 0 \implies U(r) > 0
$$
  - Thế năng ở khoảng cách hữu hạn luôn mang dấu dương.

- Trường hợp hai hạt hút nhau:
  - Lực tương tác giữa hai hạt là lực hút, có hướng kéo hai hạt lại gần nhau, tức là ngược hướng với vectơ dịch chuyển từ $r$ ra $\infty$.
  - Lực hút do đó sinh công âm trong quá trình tách hai hạt ra xa nhau vô cực:
$$
W_{r \to \infty} < 0 \implies U(r) < 0
$$
  - Thế năng ở khoảng cách hữu hạn luôn mang dấu âm.
  - Dấu âm này phản ánh một trạng thái liên kết (bound state): Ta phải cung cấp công từ bên ngoài để thắng lực hút mới có thể giải phóng hai hạt ra xa nhau vô hạn.

</details>

---

### Q7.20 - Bản chất của điểm quay đầu (Turning Points)

Hãy giải thích tại sao các điểm $x = A$ và $x = -A$ trong Hình 7.23b lại được gọi là các "điểm quay đầu" (turning points). Tại một điểm quay đầu, giá trị của cơ năng $E$ và thế năng $U$ có mối quan hệ như thế nào?

![Hình 7.23: Đồ thị cơ năng, thế năng và các điểm quay đầu](/vat-ly-1/bai-giang/img/young-07/r-theory-hinh-7-23.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Định nghĩa và giải thích bản chất vật lý của điểm quay đầu trên đồ thị năng lượng.

**Hướng đi:**

- Biểu diễn động năng qua cơ năng và thế năng: $K = E - U(x) \ge 0$.

- Phân tích vận tốc và gia tốc tại vị trí $K = 0$.

- Dùng điều kiện động năng không âm để tìm giới hạn chuyển động. Một điểm quay đầu là biên nơi vật không thể tiếp tục theo chiều cũ vì miền kế bên đòi hỏi động năng âm.

**Lời giải:**

- Mối liên hệ giữa $E$ và $U$ tại điểm quay đầu:
  - Cơ năng toàn phần của hệ bảo toàn là hằng số:
$$
E = K + U(x)
$$
  - Động năng của vật là $K = \frac{1}{2}mv^2$. Vì khối lượng $m > 0$ và $v^2 \ge 0$, động năng không bao giờ mang giá trị âm ($K \ge 0$):
$$
U(x) \le E
$$
  - Hạt chỉ có thể chuyển động trong các miền không gian mà thế năng nhỏ hơn hoặc bằng cơ năng.
  - Tại các vị trí biên $x = A$ và $x = -A$, đường thế năng $U(x)$ cắt ngang đường cơ năng $E$:
$$
U(A) = U(-A) = E
$$
  Do đó, tại điểm quay đầu, thế năng bằng đúng cơ năng toàn phần của hệ.

- Tại sao gọi là "điểm quay đầu":
  - Vì $U = E$, động năng tại đây triệt tiêu hoàn toàn:
$$
K = 0 \implies v = 0
$$
  Tốc độ của hạt tức thời bằng không.
  - Tại các điểm này, thế năng đang có độ dốc khác không ($dU/dx \ne 0$), nên lực tác dụng $F_x = -dU/dx \ne 0$. Lực này đóng vai trò gia tốc kéo hạt đổi chiều chuyển động, hướng ngược trở lại vùng có thế năng thấp hơn.
  - Hạt chạm đến điểm này, dừng lại rồi lập tức quay ngược hướng di chuyển, nên điểm này được gọi là điểm quay đầu.

</details>

---

### Q7.21 - Cân bằng phiếm định và đồ thị thế năng

Một hạt ở trạng thái cân bằng phiếm định (neutral equilibrium) nếu hợp lực tác dụng lên nó bằng không và vẫn tiếp tục bằng không khi hạt bị dịch chuyển nhẹ theo bất kỳ hướng nào. Hãy phác họa dạng hàm thế năng gần một điểm cân bằng phiếm định trong trường hợp chuyển động một chiều. Cho một ví dụ thực tế về một vật ở trạng thái cân bằng phiếm định.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Nêu đặc điểm hàm thế năng và ví dụ thực tế cho cân bằng phiếm định.

**Hướng đi:**

- Mối liên hệ giữa lực và đạo hàm thế năng: $F_x = -dU/dx = 0$ tại mọi điểm lân cận.

- Xét các vị trí lân cận vì cân bằng phiếm định đòi hỏi vật vẫn cân bằng sau khi được dịch chuyển nhẹ rồi đặt lại ở trạng thái nghỉ.

**Lời giải:**

- Dạng của hàm thế năng:
  - Điều kiện cân bằng phiếm định đòi hỏi hợp lực triệt tiêu trên toàn bộ lân cận:
$$
F_x = -\frac{dU}{dx} = 0
$$
  - Tích phân phương trình này cho thấy thế năng $U(x)$ phải là một hàm hằng số không đổi trên miền đó:
$$
U(x) = C = \mathrm{const}
$$
  - Do đó, trên đồ thị thế năng $U$ theo $x$, đồ thị là một đoạn thẳng nằm ngang phẳng hoàn toàn. Cả đạo hàm bậc nhất và đạo hàm bậc hai của thế năng đều triệt tiêu:
$$
\frac{dU}{dx} = 0 \quad \text{và} \quad \frac{d^2U}{dx^2} = 0
$$

![Thế năng không đổi trong lân cận một vị trí cân bằng phiếm định.](/vat-ly-1/bai-giang/img/young-07/r-solution-q721-neutral.svg)

- Ví dụ thực tế:
  - Một quả bi đặt trên mặt bàn ngang nhẵn. Nếu dịch chuyển nó sang vị trí khác rồi đặt nghỉ, trọng lực và lực pháp tuyến tiếp tục cân bằng. Độ cao không đổi nên thế năng trọng trường giữ nguyên. Không có lực kéo nó về vị trí cũ hoặc đẩy ra xa hơn.

</details>

---

### Q7.22 - Đồ thị tốc độ ứng với hai mức cơ năng

Hợp lực tác dụng lên một hạt khối lượng $m$ có hàm thế năng như Hình 7.24a. Nếu cơ năng toàn phần là $E_1$, hãy vẽ đồ thị tốc độ $v$ theo tọa độ $x$. Tại giá trị nào của $x$ tốc độ lớn nhất? Hãy phác họa đồ thị $v$ theo $x$ nếu cơ năng là $E_2$.

![Hình 7.24: Các mức cơ năng, điểm quay đầu và vị trí cân bằng trong trường thế](/vat-ly-1/bai-giang/img/young-07/r-theory-hinh-7-24.png)

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

Đọc các mức $E_1,E_2$ và các vị trí $x_a,x_b,x_c,x_d,x_1,x_2,x_3$ trên Hình 7.24a. Tìm miền chuyển động và phác đồ thị tốc độ cho hạt ban đầu ở giếng thế gần $x_1$.

**Hướng đi:**

- Từ $K=E-U(x)$ và $K=mv^2/2$, suy ra công thức tốc độ:

$$
v(x)=\sqrt{\frac{2[E-U(x)]}{m}}.
$$

- Chỉ vẽ trên miền liên thông mà hạt tiếp cận được và $U(x)\le E$, vì động năng không âm và hạt không thể vượt qua một đoạn có $U>E$.

- Tốc độ bằng không ở điểm quay đầu và lớn nhất tại đáy thế năng thấp nhất trong miền chuyển động.

**Lời giải:**

Với cơ năng $E_1$, hạt ở giếng thế thứ nhất chuyển động giữa $x_a$ và $x_b$. Ở hai đầu, $U=E_1$ nên tốc độ bằng không. Tốc độ tăng từ $x_a$ tới $x_1$, đạt cực đại tại đáy giếng $x_1$, rồi giảm về không tại $x_b$.

![Đồ thị phác tốc độ theo tọa độ khi hạt có cơ năng E1, với hai điểm quay đầu xa và xb.](/vat-ly-1/bai-giang/img/young-07/r-solution-q722-speed-e1.svg)

Với cơ năng $E_2$, hạt vượt được rào tại $x_2$ và chuyển động trong miền từ $x_c$ đến $x_d$. Tốc độ bằng không tại hai đầu. Hai cực đại tốc độ nằm tại hai cực tiểu thế năng $x_1,x_3$. Tại đỉnh rào $x_2$, tốc độ có cực tiểu địa phương nhưng vẫn dương vì $E_2>U(x_2)$.

![Đồ thị phác tốc độ theo tọa độ khi hạt có cơ năng E2, với hai cực đại và một cực tiểu dương giữa chúng.](/vat-ly-1/bai-giang/img/young-07/r-solution-q722-speed-e2.svg)

Các hình phác biểu diễn dạng đồ thị, không xác định thang số của trục. Tốc độ luôn không âm. Không có cơ sở để coi hai nhánh đối xứng vì đồ thị thế năng ban đầu không có tính đối xứng ấy.

</details>

---

### Q7.23 - Xác định hướng của lực từ hàm thế năng bậc ba

Hàm thế năng tương ứng với một lực $\vec{F}$ một chiều có dạng $U(x) = ax^3$, trong đó $a$ là một hằng số dương ($a > 0$). Hãy xác định hướng của vectơ lực $\vec{F}$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:**

- Cho $U(x) = ax^3$ với $a > 0$. Xác định hướng của lực $\vec{F}$.

**Hướng đi:**

- Tính thành phần lực $F_x$ qua đạo hàm đổi dấu của thế năng: $F_x = -dU/dx$.

- Xét dấu của $F_x$ trên các miền giá trị của tọa độ $x$.

- Lấy đạo hàm vì đề cho hàm thế năng của lực bảo toàn. Dấu của thành phần lực, không phải dấu của thế năng, quyết định hướng lực.

**Lời giải:**

- Thành phần lực theo phương $x$ được tính bằng đạo hàm đổi dấu của hàm thế năng:
$$
\begin{aligned}
F_x &= -\frac{dU}{dx} \\
&= -\frac{d}{dx}(ax^3) \\
&= -3ax^2.
\end{aligned}
$$

- Phân tích dấu của biểu thức lực $F_x$:
  - Theo giả thiết đề bài, hằng số $a > 0$.
  - Bình phương tọa độ luôn thỏa mãn $x^2 > 0$ với mọi $x \ne 0$, và $x^2 = 0$ khi $x = 0$.
  - Do đó đại lượng $-3ax^2$ luôn mang dấu âm với mọi giá trị $x \ne 0$:
$$
F_x < 0 \quad \forall x \ne 0
$$
  - Tại vị trí $x = 0$, lực triệt tiêu: $F_x = 0$.

- Kết luận về hướng của lực:
  - Ngoại trừ tại gốc tọa độ $x = 0$ nơi hạt ở vị trí cân bằng ($F_x = 0$), tại mọi điểm khác trên trục tọa độ (bất kể $x > 0$ hay $x < 0$), lực $\vec{F}$ luôn có thành phần đại số âm.
  - Điều này có nghĩa là vectơ lực $\vec{F}$ luôn hướng thẳng theo chiều âm của trục tọa độ $x$ (hướng sang trái, theo chiều $-x$).
  - Khi $x > 0$, lực hướng về gốc tọa độ (lực hút). Tuy nhiên, khi $x < 0$, lực vẫn tiếp tục hướng sang chiều âm, đẩy hạt càng ngày càng ra xa gốc tọa độ.

</details>
