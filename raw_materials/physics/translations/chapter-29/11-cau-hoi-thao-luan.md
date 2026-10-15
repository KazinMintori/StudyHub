## Câu hỏi thảo luận

::: exercise Q29.1
Một tấm đồng nằm giữa hai cực nam châm điện, với từ trường vuông góc mặt tấm. Muốn kéo tấm ra phải tác dụng lực đáng kể, và lực cần thiết tăng theo tốc độ. Vì sao? Khi đưa tấm vào giữa hai cực có cần lực như vậy không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tấm đồng dẫn điện đi qua ranh giới vùng từ trường. Cần giải thích lực cản khi kéo ra và khi đưa vào.

**Hướng đi:**

- Dùng cảm ứng điện từ để nhận biết các dòng Fu-cô khi phần diện tích nằm trong trường thay đổi.
- Dùng định luật Lenz để tìm chiều lực. Lực phải chống chuyển động gây biến thiên từ thông.

Khi tấm đi ra, từ thông qua các đường dòng bên trong tấm biến đổi. Các dòng Fu-cô xuất hiện và chịu lực từ ngược chiều chuyển động. Kéo nhanh hơn làm từ thông biến thiên nhanh hơn, gây dòng lớn hơn và lực cản lớn hơn, trong điều kiện điện trở và hình học giữ nguyên.

Khi đưa tấm vào, chiều dòng Fu-cô đảo lại nhưng lực vẫn cản chuyển động. Do đó cũng phải tác dụng lực để đưa tấm vào. Công của lực ngoài chủ yếu chuyển thành nhiệt trong tấm. Đồng không cần có tính sắt từ để xuất hiện tác dụng này.
:::

::: exercise Q29.2
Trong Hình 29.8, khi tốc độ góc của vòng dây tăng gấp đôi, tần số đổi chiều của dòng cảm ứng và suất điện động cực đại đều tăng gấp đôi. Vì sao? Mômen lực cần để quay vòng có thay đổi không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vòng quay trong từ trường đều, với diện tích và độ lớn trường không đổi. Tốc độ góc tăng từ $\omega$ lên $2\omega$.

**Hướng đi:**

- Dùng suất điện động của máy phát quay để phân biệt tần số và biên độ.
- Dùng mômen từ của vòng mang dòng để liên hệ tải điện với mômen cơ học.

Suất điện động của một vòng là

$$
\mathcal E=\omega BA\sin\omega t.
$$

Tần số bằng $f=\omega/(2\pi)$ và biên độ bằng $\mathcal E_0=\omega BA$. Cả hai đều tỉ lệ thuận với $\omega$, nên đều tăng gấp đôi.

Nếu vòng nối với điện trở $R$ không đổi và bỏ qua tự cảm, dòng tức thời bằng $I=\mathcal E/R$. Mômen từ có độ lớn $IAB|\sin\phi|$, chống chiều quay. Tại cùng một góc $\phi$, tăng tốc độ gấp đôi làm dòng và mômen cản tăng gấp đôi. Mômen ngoài để giữ quay đều phải tăng tương ứng.

Trong mô hình ấy,

$$
\begin{aligned}
\\tau_{\mathrm{drag}} &= \frac{\omega B^2A^2}{R}\sin^2\phi, \\
\langle P\rangle &= \frac{\omega^2B^2A^2}{2R}.
\end{aligned}
$$

Vì vậy công suất cơ trung bình tăng bốn lần. Nếu mạch hở, không có dòng tải và không có mômen cản từ này, dù vẫn có suất điện động giữa các đầu ra.
:::

::: exercise Q29.3
Hai vòng tròn nằm cạnh nhau trong cùng một mặt phẳng. Một vòng nối với nguồn có dòng tăng dần, vòng kia là một vòng dẫn kín. Dòng cảm ứng ở vòng kín chạy cùng chiều hay ngược chiều dòng của vòng nối nguồn? Nếu dòng ở vòng thứ nhất giảm thì kết quả thế nào? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Hai vòng nằm cạnh nhau, không lồng vào nhau. Cần tìm chiều dòng vòng thứ hai khi dòng vòng thứ nhất tăng hoặc giảm.

**Hướng đi:**

- Xác định chiều từ trường của vòng thứ nhất tại vùng nằm ngoài vòng ấy. Chiều này ngược với trường ở bên trong vòng.
- Dùng Lenz cho biến thiên từ thông qua vòng thứ hai, rồi dùng quy tắc bàn tay phải.

Giả sử dòng ở vòng thứ nhất ngược chiều kim đồng hồ khi nhìn từ một phía của mặt phẳng. Trường bên trong vòng ấy hướng về phía người quan sát, nhưng trường xuyên qua vòng nằm cạnh bên hướng ra xa người quan sát.

Khi dòng thứ nhất tăng, từ thông hướng ra xa qua vòng thứ hai tăng. Dòng cảm ứng phải tạo trường về phía người quan sát, nên cũng ngược chiều kim đồng hồ. Hai dòng cùng chiều quay khi nhìn từ cùng phía.

Khi dòng thứ nhất giảm, vòng thứ hai phải duy trì từ thông hướng ra xa. Dòng cảm ứng theo chiều kim đồng hồ, ngược chiều dòng thứ nhất. Kết luận đảo đồng thời nếu đổi chiều dòng ban đầu.
:::

::: exercise Q29.4
Chứng tỏ trong công thức (29.6), nếu $v$ đo bằng mét trên giây, $B$ bằng tesla và $L$ bằng mét, vế phải có đơn vị joule trên coulomb, tức volt.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Kiểm tra đơn vị của $vBL$ trong hệ SI.

**Hướng đi:**

- Dùng định nghĩa tesla từ lực lên dây mang dòng, rồi thay ampere bằng coulomb trên giây.
- Rút gọn để nhận ra năng lượng trên một đơn vị điện tích.

$$
\begin{aligned}
1\,\mathrm T &= 1\,\frac{\mathrm N}{\mathrm{A\,m}}, \\
[vBL] &= \frac{\mathrm m}{\mathrm s} \frac{\mathrm N}{\mathrm{A\,m}}\mathrm m \\
&= \frac{\mathrm{N\,m}}{\mathrm{A\,s}} \\
&= \frac{\mathrm J}{\mathrm C}=\mathrm V.
\end{aligned}
$$
:::

::: exercise Q29.5
Một dây dẫn thẳng dài đi qua tâm vòng kim loại và vuông góc mặt phẳng vòng. Nếu dòng trong dây tăng, vòng có dòng cảm ứng không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Dây thẳng trùng trục vòng. Từ trường của dây biến thiên vì dòng tăng.

**Hướng đi:**

- Xét thành phần từ trường vuông góc mặt vòng, thay vì chỉ xét việc độ lớn trường có thay đổi.
- Dùng Faraday với từ thông qua vòng.

Trường của dây có đường sức là các đường tròn trong mặt phẳng vòng. Do đó $\vec B$ tiếp tuyến với mặt và vuông góc vector diện tích. Từ thông qua vòng bằng không tại mọi thời điểm. Suất điện động quanh vòng và dòng cảm ứng đều bằng không trong cấu hình đối xứng lý tưởng này.
:::

::: exercise Q29.6
Một người cho rằng nam châm vĩnh cửu thả rơi trong một ống đồng thẳng đứng cuối cùng đạt vận tốc giới hạn, ngay cả khi không có lực cản không khí. Nhận định ấy có đúng không? Vì sao?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nam châm rơi trong ống dẫn điện. Bỏ qua lực cản không khí.

**Hướng đi:**

- Dùng Faraday cho các đường dòng kín trong thành ống, vì từ trường tại mỗi phần thành ống thay đổi khi nam châm đi qua.
- Dùng Lenz và cân bằng lực để giải thích vận tốc giới hạn.

Nhận định đúng đối với ống đồng liền dẫn điện có kích thước phù hợp. Dòng Fu-cô xuất hiện trong thành ống và tạo lực cản từ lên nam châm. Công suất cơ bị mất chuyển thành nhiệt trong đồng.

Khi tốc độ tăng, suất điện động và dòng cảm ứng tăng, làm lực cản tăng. Nam châm đạt vận tốc giới hạn khi lực cản hướng lên bằng trọng lực. Hiện tượng vẫn xảy ra khi không có không khí. Nếu cắt một rãnh dọc ống để làm gián đoạn các đường dòng vòng quanh ống, tác dụng hãm giảm mạnh.
:::

::: exercise Q29.7
Một máy bay bay ngang trên Nam Cực, nơi từ trường Trái Đất chủ yếu hướng lên khỏi mặt đất. Hành khách nhìn về phía trước sẽ thấy đầu cánh trái hay đầu cánh phải có điện thế cao hơn? Kết quả có phụ thuộc hướng bay không?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vận tốc máy bay nằm ngang và từ trường hướng lên. Cần tìm chiều lực từ lên điện tích dương dọc hai cánh.

**Hướng đi:**

- Dùng $\vec F_B=q\vec v\times\vec B$ cho điện tích dương.
- Xác định hướng trái, phải theo người đang nhìn cùng chiều bay.

Khi $\vec v$ hướng về phía trước và $\vec B$ hướng lên, tích có hướng $\vec v\times\vec B$ hướng sang phải. Điện tích dương dồn về đầu cánh phải, nên đầu cánh phải có điện thế cao hơn.

Kết quả không phụ thuộc phương vị bay ngang, vì hướng phải được xác định tương đối với chiều chuyển động. Điều kiện quyết định là thành phần từ trường thẳng đứng hướng lên.
:::

::: exercise Q29.8
Xét cấu hình của Bài 29.21. Trong phần (a), lực do mạch lớn tác dụng lên vòng nhỏ có hướng nào? Giải thích vì sao phù hợp với định luật Lenz.

![Cấu hình của Bài 29.21: Vòng nhỏ lệch về phía trái bên trong vòng lớn nối pin và công tắc.](img/young-29/hinh-e29-21.png)
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Ngay sau khi đóng công tắc, dòng vòng lớn tăng. Vòng nhỏ nằm lệch tâm ở phía trái bên trong vòng lớn.

**Hướng đi:**

- Dùng Lenz để thấy dòng ở vòng nhỏ tạo trường ngược với phần trường đang tăng của vòng lớn.
- Xét lực giữa các đoạn dây gần nhau. Các đoạn gần phía trái mang dòng ngược chiều và đẩy nhau mạnh hơn các đoạn xa.

Dòng cảm ứng ở vòng nhỏ có chiều quay ngược dòng ở vòng lớn. Tại mép trái của hai vòng, hai đoạn gần nhau có dòng ngược chiều nên đẩy nhau. Vì vòng nhỏ nằm phía trong, lực mạnh ở mép trái đẩy nó về phía phải, tức về gần tâm vòng lớn.

Di chuyển vào gần tâm làm vòng nhỏ rời khỏi vùng trường mạnh sát dây vòng lớn, giảm phần từ thông đang tăng. Lực như vậy chống lại nguyên nhân gây cảm ứng. Nếu hai vòng đặt đồng tâm hoàn toàn, đối xứng làm hợp lực tịnh tiến bằng không, dù vẫn có lực trên từng phần vòng.
:::

::: exercise Q29.9
Một khung kim loại hình chữ nhật đặt gần dây thẳng dài mang dòng, với hai cạnh song song dây. Nếu dòng trong dây giảm, khung bị hút về dây hay đẩy ra xa? Giải thích bằng định luật Lenz.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Khung nằm về một phía dây dài. Dòng dây đang giảm.

**Hướng đi:**

- Dùng Lenz để tìm dòng khung có tác dụng duy trì từ trường đang giảm.
- So sánh lực lên cạnh gần và cạnh xa. Trường dây giảm theo khoảng cách.

Dòng cảm ứng có chiều sao cho ở cạnh gần dây, nó cùng chiều dòng trong dây. Cạnh gần chịu lực hút. Cạnh xa mang dòng ngược chiều dây và chịu lực đẩy, nhưng trường tại đó yếu hơn nên lực đẩy nhỏ hơn.

Hợp lực kéo khung lại gần dây. Chuyển động này đưa khung đến vùng từ trường mạnh hơn, chống lại sự giảm từ thông do dòng trong dây giảm. Vì thế lực hút phù hợp với Lenz.
:::

::: exercise Q29.10
Một vòng dây vuông nằm trong từ trường đều, không đổi. Có thể quay vòng quanh một trục dọc theo một cạnh mà không tạo suất điện động không? Hãy xét hướng trục quay so với từ trường.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vòng quay quanh một cạnh. Cần điều kiện để từ thông không biến đổi.

**Hướng đi:**

- Dùng $\Phi_B=BA\cos\phi$, với diện tích không đổi.
- Xét riêng khi trục quay song song từ trường, vì pháp tuyến luôn vuông góc trục ấy.

Có. Nếu trục quay dọc cạnh song song $\vec B$, mặt vòng luôn chứa một phương song song trường. Pháp tuyến mặt vòng luôn vuông góc trường, nên từ thông bằng không trong suốt chuyển động. Do đó suất điện động tổng quanh vòng bằng không.

Nếu trường có thành phần vuông góc trục quay thì nói chung từ thông biến đổi và có suất điện động. Suất điện động có thể bằng không ở những thời điểm riêng lẻ, nhưng không bằng không trong toàn bộ một vòng quay.
:::

::: exercise Q29.11
Ví dụ 29.6 xét lực ngoài cần để kéo thanh trượt đều. Nếu phần bên trái của thanh dẫn chữ U bị đứt, cần lực bao nhiêu để duy trì tốc độ không đổi? Bỏ qua ma sát.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Mạch thanh trượt bị hở. Xét chuyển động đều sau khi điện tích đã phân bố lại.

**Hướng đi:**

- Phân biệt suất điện động với dòng điện. Mạch hở vẫn có suất điện động nhưng không có dòng duy trì quanh mạch.
- Dùng $F_B=IBL$ cho lực hãm do dòng trong thanh.

Mạch hở có $I=0$ trong trạng thái ổn định. Điện tích tách ra tạo hiệu điện thế, nhưng không có dòng tải liên tục. Vì thế lực hãm từ do dòng bằng không. Khi bỏ qua ma sát, lực ngoài cần để duy trì chuyển động đều bằng không. Chỉ giai đoạn phân bố lại điện tích ban đầu có thể có hiệu ứng quá độ rất ngắn.
:::

::: exercise Q29.12
Trong Hình 29.18, có hợp lý khi hỏi một electron nhận bao nhiêu năng lượng sau khi đi một vòng quanh vòng dây mang dòng $I'$ không? Có hợp lý khi hỏi hiệu điện thế mà electron đi qua sau một vòng ấy không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện trường cảm ứng quanh vòng không bảo toàn. Phân biệt công với hiệu điện thế giữa hai điểm.

**Hướng đi:**

- Dùng tích phân công $q\oint\vec E\cdot d\vec\ell$ để tính năng lượng truyền từ trường cho điện tích.
- Xét khả năng định nghĩa thế điện duy nhất cho điện trường có tuần hoàn khác không.

Câu hỏi về năng lượng trường truyền cho electron là hợp lý. Với chiều đường đi đã xác định,

$$
W=q\oint\vec E\cdot d\vec\ell=q\mathcal E.
$$

Đối với electron, $q=-e$, nên dấu công còn phụ thuộc chiều chuyển động. Trong dây có va chạm, năng lượng trường cung cấp không nhất thiết tích lũy thành động năng của electron mà có thể truyền thành nhiệt cho vật liệu.

Không thể gán cho toàn bộ điện trường cảm ứng một hiệu điện thế vô hướng duy nhất trên đường kín. Electron trở về cùng điểm nhưng tích phân công có thể khác không. Suất điện động quanh vòng vẫn xác định được và không đồng nhất với hiệu điện thế giữa hai điểm đầu cuối trùng nhau.
:::

::: exercise Q29.13
Một vòng kim loại có mặt phẳng vuông góc từ trường đều đang tăng với tốc độ không đổi. Nếu bán kính vòng tăng gấp đôi, (a) suất điện động cảm ứng và (b) điện trường cảm ứng trên vòng tăng theo hệ số nào?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Tốc độ biến thiên từ trường giữ nguyên. So sánh hai vòng bán kính $r$ và $2r$.

**Hướng đi:**

- Suất điện động phụ thuộc diện tích qua Faraday.
- Điện trường phụ thuộc suất điện động chia chu vi, nhờ đối xứng tròn.

$$
\begin{aligned}
|\mathcal E| &= \pi r^2\left|\frac{dB}{dt}\right|, \\
E &= \frac{|\mathcal E|}{2\pi r} \\
&= \frac r2\left|\frac{dB}{dt}\right|.
\end{aligned}
$$

(a) Suất điện động tăng bốn lần. (b) Điện trường trên vòng tăng hai lần.
:::

::: exercise Q29.14
Một số động cơ xăng một xi-lanh nhỏ dùng thiết bị magneto để cấp dòng cho bugi. Nam châm vĩnh cửu gắn vào bánh đà, còn cuộn dây đứng yên đặt gần nó. Thiết bị tạo dòng bằng cách nào? Điều gì xảy ra khi nam châm đi qua cuộn?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nam châm quay theo bánh đà, cuộn dây đứng yên. Cần giải thích tín hiệu điện cấp cho bugi.

**Hướng đi:**

- Dùng biến thiên từ thông qua cuộn khi nam châm đến gần rồi đi xa.
- Dùng Faraday để liên hệ chuyển động cơ học với xung suất điện động.

Khi nam châm tiến đến cuộn, từ thông qua cuộn tăng. Sau khi đi qua, từ thông giảm. Hai giai đoạn tạo suất điện động trái dấu. Tại vị trí từ thông đạt cực trị, tốc độ biến thiên tức thời bằng không.

Thiết bị dùng suất điện động cảm ứng và mạch đánh lửa để tạo điện áp cần cho tia lửa ở bugi. Năng lượng điện đến từ cơ năng quay bánh đà. Nam châm đứng yên so với cuộn không tạo tín hiệu cảm ứng liên tục.
:::

::: exercise Q29.15
Định luật Lenz có phát biểu rằng dòng cảm ứng trong vòng kim loại luôn chạy để chống lại từ thông qua vòng không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Phân biệt chống từ thông với chống biến thiên từ thông.

**Hướng đi:**

- Xét hai trường hợp từ thông ngoài tăng và giảm với cùng một hướng.
- Dùng Lenz cho sự thay đổi trong từng trường hợp.

Không. Dòng cảm ứng chống sự thay đổi từ thông. Nếu trường ngoài hướng lên đang tăng, dòng tạo trường hướng xuống. Nếu trường ngoài vẫn hướng lên nhưng đang giảm, dòng tạo trường hướng lên để duy trì phần từ thông bị mất. Trường cảm ứng vì vậy có thể cùng chiều hoặc ngược chiều trường ngoài.
:::

::: exercise Q29.16
Định luật Faraday có nói rằng từ thông lớn qua cuộn tạo suất điện động lớn không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xét giá trị từ thông và tốc độ biến thiên của nó.

**Hướng đi:**

- Dùng $\mathcal E=-N\,d\Phi_B/dt$ để xác định đại lượng chi phối suất điện động.
- So sánh từ thông lớn nhưng không đổi với từ thông đi qua giá trị không nhưng biến thiên nhanh.

Không. Suất điện động phụ thuộc tốc độ biến thiên từ thông, không phụ thuộc riêng độ lớn từ thông. Một cuộn đứng yên trong từ trường mạnh không đổi có thể có từ thông lớn nhưng suất điện động bằng không. Trong máy phát quay, suất điện động đạt cực đại lúc từ thông đi qua giá trị không, vì khi ấy từ thông đổi nhanh nhất.
:::

::: exercise Q29.17
Có thể đồng thời có dòng điện dịch và dòng dẫn bên trong một vật dẫn không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vật dẫn có điện trường có thể biến thiên theo thời gian.

**Hướng đi:**

- Dòng dẫn liên hệ với sự chuyển động của điện tích tự do dưới điện trường.
- Dòng dịch liên hệ với đạo hàm thông lượng điện, nên không bị giới hạn ở chất cách điện.

Có. Khi điện trường trong vật dẫn vừa khác không vừa biến thiên, nó có thể tạo dòng dẫn và dòng dịch đồng thời. Trong mô hình tuyến tính đơn giản,

$$
\begin{aligned}
\vec J_C &= \sigma\vec E, \\
\vec J_D &= \varepsilon\frac{\partial\vec E}{\partial t}.
\end{aligned}
$$

Trong dòng một chiều ổn định, đạo hàm bằng không nên dòng dịch bằng không. Ở nhiều vật dẫn tốt và tần số thấp, dòng dẫn lớn hơn dòng dịch nhiều, nhưng điều đó không có nghĩa dòng dịch bị cấm tồn tại trong vật dẫn.
:::

::: exercise Q29.18
Một tụ phẳng được lấp đầy bằng điện môi. Một người dùng các công thức (29.13) và (29.14) để khẳng định dòng dẫn trong điện môi bằng dòng dịch trong điện môi. Bạn có đồng ý không? Giải thích.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Điện môi lý tưởng lấp khe tụ. Hai công thức cho cùng biểu thức đạo hàm thông lượng nhưng cần xác định đúng vị trí dòng dẫn.

**Hướng đi:**

- Đọc $i_C=dq/dt$ là dòng trong dây nạp điện cho bản tụ.
- Phân biệt dòng dịch trong khe với sự dẫn điện qua chất cách điện.

Không đồng ý. Trong phép suy diễn, $i_C$ là dòng dẫn đi đến bản tụ qua dây, không phải dòng dẫn xuyên điện môi. Điện môi lý tưởng không có dòng dẫn qua khe.

Khi tụ nạp, thông lượng điện trong khe biến thiên và có dòng dịch. Dòng dịch tổng qua khe bằng dòng dẫn trong dây, bảo đảm cùng một đường Ampere cho kết quả nhất quán với các mặt căng khác nhau. Nếu điện môi thực có dòng rò, phải xét thêm dòng rò ấy thay vì đồng nhất hai loại dòng.
:::

::: exercise Q29.19
Ghép các phương trình Maxwell với những phát biểu sau.

(a) Các đường sức điện khép kín được tạo bởi từ thông biến thiên.

(b) Các đường sức từ khép kín được tạo bởi chuyển động điện tích và thông lượng điện biến thiên.

(c) Đường sức điện có thể bắt đầu ở điện tích dương và kết thúc ở điện tích âm.

(d) Không có đơn cực từ để đường sức từ bắt đầu hoặc kết thúc tại đó.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Nhận diện hai định luật thông lượng mặt kín và hai định luật tuần hoàn đường kín.

**Hướng đi:**

- Ghép phát biểu về nguồn hoặc điểm đầu cuối với định luật Gauss.
- Ghép phát biểu về đường sức khép kín do trường biến thiên với Faraday hoặc Ampere–Maxwell.

(a) Định luật Faraday, công thức (29.20).

(b) Định luật Ampere–Maxwell, công thức (29.21).

(c) Định luật Gauss cho điện trường, công thức (29.18).

(d) Định luật Gauss cho từ trường, công thức (29.19).
:::

::: exercise Q29.20
Nếu đơn cực từ tồn tại, vế phải của công thức (29.20) sẽ có thêm số hạng tỉ lệ với dòng đơn cực từ. Giả sử có dòng đơn cực từ không đổi chạy trong một dây thẳng dài. Hãy phác họa các đường sức điện mà nó tạo ra.
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Xét giả thuyết dòng điện tích từ dọc một dây thẳng, không phải dòng điện tích thông thường.

**Hướng đi:**

- Dùng sự đối xứng của dạng Maxwell có thêm nguồn từ. Dòng từ tạo tuần hoàn điện trường tương tự dòng điện tạo tuần hoàn từ trường.
- Dùng đối xứng trụ quanh dây để xác định hình dạng đường sức.

Các đường sức điện là những đường tròn đồng tâm nằm trong các mặt phẳng vuông góc dây. Điện trường tiếp tuyến với các đường tròn, có cùng độ lớn tại các điểm cách dây một khoảng bằng nhau. Chiều tuần hoàn đảo lại khi đảo chiều dòng đơn cực từ.

![Lời giải Q29.20: Các đường sức điện tròn bao quanh dòng đơn cực từ giả định dọc dây thẳng.](img/young-29/hinh-giai-q29-20.svg)

Nếu chọn quy ước mở rộng Faraday có số hạng dòng từ mang dấu âm, chiều điện trường quanh dòng từ dương ngược với chiều quy tắc bàn tay phải dùng cho từ trường quanh dòng điện dương. Điều quyết định trong câu hỏi là cấu trúc đường sức khép kín bao quanh dây.
:::

::: exercise Q29.21
Một chất siêu dẫn loại II nằm trong từ trường ngoài giữa $B_{c1}$ và $B_{c2}$. Vật liệu có các vùng chứa từ thông với điện trở khác không và các vùng vẫn siêu dẫn. Điện trở của một trụ dài, mảnh làm từ vật liệu ấy bằng bao nhiêu?
:::

::: solution Lời giải chi tiết
**Tóm tắt đề bài:** Vật liệu ở trạng thái hỗn hợp, còn các đường dẫn siêu dẫn nối suốt chiều dài trụ.

**Hướng đi:**

- Phân biệt các sợi thường cục bộ với điện trở đo giữa hai đầu toàn vật.
- Dùng tính chất các đường dẫn song song. Đường siêu dẫn liên tục có thể nối tắt các đường có điện trở hữu hạn.

Trong mô hình của chương, điện trở giữa hai đầu trụ bằng không, vì phần siêu dẫn còn liên tục tạo đường dẫn không điện trở. Sự hiện diện của các sợi pha thường không buộc toàn bộ dòng đi qua chúng.

Kết luận áp dụng khi dòng không vượt ngưỡng làm mất trạng thái siêu dẫn và không phát sinh tổn hao do chuyển động các xoáy từ. Khi trường đạt $B_{c2}$, toàn vật chuyển sang pha thường và lập luận về đường dẫn siêu dẫn không còn áp dụng.
:::
