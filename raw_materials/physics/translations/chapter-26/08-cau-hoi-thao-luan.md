<!-- Source: Discussion Questions Q26.1–Q26.21, printed pages 869–870, PDF pages 889–890. Figures Q26.4–Q26.10, Q26.12, Q26.14, Q26.16 and Q26.18 are referenced. -->

## Câu hỏi thảo luận

::: exercise Q26.1
Trong các bóng đèn $120\,\mathrm V$, dây tóc của bóng $60\,\mathrm W$ hay bóng $120\,\mathrm W$ có điện trở lớn hơn? Nếu mắc nối tiếp hai bóng vào đường dây $120\,\mathrm V$, bóng nào có độ giảm điện thế lớn hơn? Nếu mắc song song thì sao? Giải thích.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Hai bóng cùng định mức điện áp nhưng có công suất khác nhau. Cần so điện trở định mức và dùng quy tắc mạch nối tiếp, song song.

**Hướng đi:**

- Ở cùng điện áp, dùng $R=V^2/P$ để so điện trở.
- Trong nối tiếp, dòng điện qua hai bóng như nhau. Trong song song, hiệu điện thế hai đầu mỗi bóng như nhau.

Điện trở định mức của hai bóng là

$$
\begin{aligned}
&R_{60} = \frac{(120\,\mathrm V)^2}{60\,\mathrm W}=240\,\Omega,\\
&R_{120} = \frac{(120\,\mathrm V)^2}{120\,\mathrm W}=120\,\Omega.
\end{aligned}
$$

Bóng $60\,\mathrm W$ có điện trở lớn hơn. Khi nối tiếp, dòng điện qua hai bóng bằng nhau nên độ giảm điện thế $V=IR$ lớn hơn trên bóng $60\,\mathrm W$. Khi mắc song song vào nguồn $120\,\mathrm V$, mỗi bóng đều có hiệu điện thế $120\,\mathrm V$.
:::

::: exercise Q26.2
Hai bóng đèn $120\,\mathrm V$, một bóng $25\,\mathrm W$ và một bóng $200\,\mathrm W$, được mắc nối tiếp vào đường dây $240\,\mathrm V$. Một bóng gần như cháy ngay. Bóng nào hỏng và vì sao?
:::

::: solution Lời giải
**Tóm tắt đề bài:** Hai bóng có cùng điện áp định mức nhưng khác công suất, mắc nối tiếp vào nguồn $240\,\mathrm V$.

**Hướng đi:**

- Tính điện trở định mức bằng $R=V^2/P$.
- Dòng nối tiếp như nhau, vì vậy bóng có điện trở lớn hơn nhận phần lớn điện áp và công suất.

Điện trở định mức của bóng $25\,\mathrm W$ là $576\,\Omega$, còn bóng $200\,\mathrm W$ là $72\,\Omega$. Dòng trong mạch và điện áp trên từng bóng là

$$
\begin{aligned}
&I = \frac{240\,\mathrm V}{576\,\Omega+72\,\Omega}\approx0{,}370\,\mathrm A,\\
&V_{25} = I(576\,\Omega)\approx213\,\mathrm V,\\
&V_{200} = I(72\,\Omega)\approx26{,}7\,\mathrm V.
\end{aligned}
$$

Bóng $25\,\mathrm W$ nhận điện áp vượt xa định mức $120\,\mathrm V$. Công suất tức thời theo mô hình điện trở không đổi khoảng $79\,\mathrm W$, lớn hơn nhiều so với mức $25\,\mathrm W$. Bóng công suất thấp bị hỏng trước.
:::

::: exercise Q26.3
Mắc thêm nhiều bóng đèn giống nhau vào pin đèn pin. (a) Độ sáng mỗi bóng thay đổi thế nào khi số bóng tăng nếu chúng mắc (i) nối tiếp và (ii) song song? (b) Pin sẽ dùng được lâu hơn khi các bóng mắc nối tiếp hay song song? Giải thích.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Xét $n$ bóng giống nhau, mỗi bóng có điện trở $R$, nối với nguồn có suất điện động $\mathcal E$.

**Hướng đi:**

- Tính dòng qua mỗi bóng trong hai cách mắc.
- Dùng $P=I^2R$ để so công suất mỗi bóng và dòng tổng do pin cấp.

Khi mắc nối tiếp, điện trở toàn mạch bằng $nR$. Dòng qua mỗi bóng và công suất của mỗi bóng là

$$
I_{\mathrm{nt}}=\frac{\mathcal E}{nR},\qquad
P_{\mathrm{nt}}=\frac{\mathcal E^2}{n^2R}.
$$

Vì vậy, thêm bóng nối tiếp làm mỗi bóng mờ đi. Khi mắc song song, mỗi bóng vẫn nhận điện áp $\mathcal E$, nên công suất mỗi bóng là $\mathcal E^2/R$ và độ sáng gần như không đổi trong mô hình nguồn lý tưởng.

Ở mắc nối tiếp, dòng tổng của pin là $\mathcal E/(nR)$. Ở mắc song song, dòng tổng là $n\mathcal E/R$. Do đó, với pin có dung lượng như nhau trong mô hình này, mắc nối tiếp rút điện chậm hơn và pin dùng được lâu hơn.
:::

::: exercise Q26.4
Trong mạch Hình Q26.4, ba bóng đèn giống nhau nối với pin đèn pin. Độ sáng các bóng so sánh thế nào? Bóng nào có dòng điện lớn nhất? Bóng nào có hiệu điện thế giữa hai đầu lớn nhất? Điều gì xảy ra nếu tháo bóng A, bóng B hoặc bóng C? Giải thích.

![Hình Q26.4: Một bóng ở nhánh riêng song song với nhánh gồm hai bóng nối tiếp](img/young-26/hinh-q26-04.png)

**Hình Q26.4:** Pin có suất điện động $\mathcal E$ đặt song song lên hai nhánh. Nhánh giữa chỉ có bóng A. Nhánh dưới có hai bóng B và C mắc nối tiếp.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Bóng A tạo thành một nhánh riêng. Bóng B và C giống nhau, mắc nối tiếp ở nhánh song song còn lại.

**Hướng đi:**

- Mỗi nhánh song song nhận cùng điện áp của pin.
- So dòng và công suất từng bóng, rồi xét nhánh nào bị hở khi tháo bóng.

Gọi điện trở mỗi bóng là $R$. Nhánh A có dòng $\mathcal E/R$. Nhánh B–C có dòng $\mathcal E/(2R)$, nên dòng qua từng bóng B và C bằng một nửa dòng qua A. Công suất mỗi bóng B và C bằng $\mathcal E^2/(4R)$, còn công suất bóng A bằng $\mathcal E^2/R$. Vì vậy A sáng nhất, còn B và C sáng như nhau và mờ hơn A. Bóng A cũng có dòng lớn nhất và hiệu điện thế lớn nhất, bằng $\mathcal E$.

Tháo A chỉ làm hở nhánh riêng của A. B và C vẫn mắc nối tiếp qua nguồn nên độ sáng của chúng không đổi. Tháo B hoặc C làm hở cả nhánh dưới, vì vậy cả B lẫn C đều tắt. Bóng A vẫn sáng như trước.
:::

::: exercise Q26.5
Hai điện trở $R_1$ và $R_2$ ($R_2>R_1$) mắc nối tiếp như Hình Q26.5. Với mỗi phát biểu, cho biết phát biểu đó luôn đúng hay không và giải thích. (a) $I_1=I_2=I_3$. (b) Dòng qua $R_1$ lớn hơn dòng qua $R_2$. (c) Hai điện trở tiêu thụ công suất bằng nhau. (d) Công suất tiêu thụ ở $R_2$ lớn hơn ở $R_1$. (e) Độ giảm điện thế trên hai điện trở bằng nhau. (f) Điện thế tại $a$ bằng điện thế tại $c$. (g) Điện thế tại $b$ thấp hơn tại $c$. (h) Điện thế tại $c$ thấp hơn tại $b$.

![Hình Q26.5: Hai điện trở mắc nối tiếp với dòng điện hướng từ a đến c](img/young-26/hinh-q26-05.png)

**Hình Q26.5:** Dòng $I_1$, $I_2$ và $I_3$ được chọn cùng hướng từ trái sang phải qua $R_1$ và $R_2$.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Hai điện trở mắc nối tiếp và $R_2>R_1$. Mũi tên dòng điện trong hình hướng từ $a$ qua $b$ đến $c$.

**Hướng đi:**

- Dùng tính liên tục của dòng điện trong một nhánh nối tiếp.
- Với cùng dòng, so $P=I^2R$ và độ giảm thế $V=IR$.

(a) Đúng. Không có nút phân nhánh giữa các điện trở, nên dòng qua cả ba tiết diện bằng nhau.

(b) Sai. Mạch nối tiếp có $I_1=I_2=I_3$.

(c) Sai, và (d) đúng. Vì dòng như nhau nhưng $R_2>R_1$, công suất $I^2R_2$ lớn hơn $I^2R_1$.

(e) Sai. Độ giảm thế trên $R_2$ lớn hơn vì $V=IR$ và $R_2>R_1$.

(f) Sai. Dòng đi từ $a$ đến $c$ qua hai điện trở thụ động nên điện thế giảm, do đó $V_a>V_c$.

(g) Sai. Qua $R_2$, điện thế giảm từ $b$ đến $c$, nên $V_b>V_c$.

(h) Đúng. Đây là cùng quan hệ điện thế vừa xác định ở câu (g).
:::

::: exercise Q26.6
Hai điện trở $R_1$ và $R_2$ ($R_2>R_1$) mắc song song như Hình Q26.6. Với mỗi phát biểu, cho biết phát biểu đó luôn đúng hay không và giải thích. (a) $I_1=I_2$. (b) $I_3=I_4$. (c) Dòng qua $R_1$ lớn hơn dòng qua $R_2$. (d) Hai điện trở tiêu thụ công suất bằng nhau. (e) Công suất tiêu thụ ở $R_2$ lớn hơn ở $R_1$. (f) $V_{cd}=V_{ef}=V_{ab}$. (g) Điểm $c$ có điện thế cao hơn điểm $d$. (h) Điểm $f$ có điện thế cao hơn điểm $e$. (i) Điểm $c$ có điện thế cao hơn điểm $e$.

![Hình Q26.6: Hai nhánh điện trở song song cùng nối giữa hai nút a và b](img/young-26/hinh-q26-06.png)

**Hình Q26.6:** Dòng $I_3$ đi vào nút $a$, chia thành $I_1$ qua nhánh $R_1$ và $I_2$ qua nhánh $R_2$, rồi hợp lại thành $I_4$ tại nút $b$. Các điểm $c,d$ nằm ở hai đầu $R_1$, còn $e,f$ nằm ở hai đầu $R_2$.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Hai điện trở cùng nối giữa hai nút $a$ và $b$. Dòng tổng chia tại $a$ và hợp lại tại $b$.

**Hướng đi:**

- Dùng quy tắc nút để so dòng tổng vào và ra.
- Các nhánh song song có cùng hiệu điện thế. Dùng $I=V/R$ và $P=V^2/R$ để so hai điện trở.

(a) Sai. $I_1=V_{ab}/R_1$ và $I_2=V_{ab}/R_2$. Do $R_1<R_2$, ta có $I_1>I_2$.

(b) Đúng. Bảo toàn điện tích tại hai nút cho $I_3=I_1+I_2=I_4$.

(c) Đúng vì $I_1>I_2$.

(d) Sai, và (e) sai. Ở cùng hiệu điện thế, $P=V^2/R$. Điện trở nhỏ hơn $R_1$ tiêu thụ công suất lớn hơn $R_2$.

(f) Đúng. Cả ba hiệu điện thế đều là hiệu điện thế giữa hai nút chung $a$ và $b$.

(g) Đúng. Dòng $I_1$ đi từ $c$ đến $d$ qua $R_1$, nên điện thế giảm theo hướng đó.

(h) Sai. Dòng $I_2$ đi từ $e$ đến $f$, do đó $V_e>V_f$.

(i) Sai. Các điểm $c$ và $e$ nằm trên cùng nút $a$, nên có cùng điện thế.
:::

::: exercise Q26.7
Pin lý tưởng nối với ba bóng đèn giống nhau như Hình Q26.7. Khi đóng công tắc $S$, độ sáng của bóng $B_1$ và $B_2$ có thay đổi không? Nếu có, thay đổi thế nào? Giải thích.

![Hình Q26.7: Ba bóng mắc thành ba nhánh song song, công tắc điều khiển nhánh bóng B](img/young-26/hinh-q26-07.png)

**Hình Q26.7:** Hai bóng $B_1$ và $B_2$ mỗi bóng nằm trên một nhánh riêng. Nhánh thứ ba gồm bóng $B$ nối tiếp với công tắc $S$.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Đóng công tắc chỉ thêm một nhánh bóng mắc song song với hai nhánh đã có. Pin được mô hình là nguồn lý tưởng.

**Hướng đi:**

- Nguồn lý tưởng giữ nguyên hiệu điện thế hai đầu các nhánh song song.
- Độ sáng của bóng giống nhau không đổi nếu điện áp đặt lên mỗi bóng không đổi.

Độ sáng của $B_1$ và $B_2$ không đổi. Trước và sau khi đóng $S$, mỗi bóng vẫn nhận cùng hiệu điện thế của pin. Dòng tổng do pin cấp tăng, nhưng dòng qua hai bóng này không đổi.
:::

::: exercise Q26.8
Một điện trở gồm ba dải kim loại giống nhau nối như Hình Q26.8. Nếu cắt bỏ một dải, số chỉ ampe kế tăng, giảm hay giữ nguyên? Vì sao?

![Hình Q26.8: Ba dải kim loại tạo ba đường dẫn song song giữa hai cực pin và ampe kế](img/young-26/hinh-q26-08.png)

**Hình Q26.8:** Ba dải giống nhau mắc song song giữa hai nút. Ampe kế đo dòng tổng do pin cấp.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Ba dải kim loại giống nhau tạo ba nhánh song song nối với nguồn và ampe kế.

**Hướng đi:**

- Bỏ một nhánh song song làm điện trở tương đương tăng.
- Nguồn lý tưởng giữ điện áp không đổi, nên dòng tổng giảm khi điện trở tương đương tăng.

Số chỉ ampe kế giảm. Nếu mỗi dải có điện trở $R$, điện trở tương đương tăng từ $R/3$ lên $R/2$. Do đó dòng tổng sau khi bỏ một dải bằng $2/3$ dòng ban đầu.
:::

::: exercise Q26.9
Một bóng đèn mắc trong mạch Hình Q26.9. Khi đóng công tắc $S$, độ sáng của bóng tăng, giảm hay giữ nguyên? Giải thích.

![Hình Q26.9: Công tắc thêm một nhánh điện trở song song trong mạch nối tiếp với bóng đèn](img/young-26/hinh-q26-09.png)

**Hình Q26.9:** Cụm các nhánh điện trở mắc song song nằm nối tiếp với một điện trở, bóng đèn và pin lý tưởng. Công tắc điều khiển nhánh điện trở phía trên.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Đóng công tắc thêm một nhánh song song vào cụm điện trở, còn cụm ấy vẫn mắc nối tiếp với bóng đèn.

**Hướng đi:**

- Thêm nhánh song song làm điện trở tương đương của cụm giảm.
- Vì cụm này nối tiếp với bóng, điện trở toàn mạch giảm và dòng qua bóng tăng.

Bóng sáng hơn. Với pin lý tưởng, dòng qua toàn mạch là dòng qua bóng. Khi điện trở toàn mạch giảm, công suất bóng nhận tăng.
:::

::: exercise Q26.10
Pin thực có điện trở trong đáng kể được nối với bóng đèn như Hình Q26.10. Khi đóng công tắc $S$, độ sáng của bóng thay đổi thế nào? Vì sao?

![Hình Q26.10: Bóng đèn và nhánh điện trở có công tắc cùng mắc song song vào pin thực](img/young-26/hinh-q26-10.png)

**Hình Q26.10:** Bóng đèn tạo một nhánh tải. Nhánh còn lại gồm công tắc $S$ nối tiếp điện trở. Hai nhánh mắc song song vào pin thực, có điện trở trong dù điện trở ấy không được vẽ thành linh kiện riêng.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Đóng công tắc mắc thêm một tải song song trực tiếp vào hai cực pin thực.

**Hướng đi:**

- Nhánh mới làm điện trở tải tương đương giảm và dòng tổng từ pin tăng.
- Với điện trở trong khác không, dòng tăng làm sụt áp trong pin tăng, nên điện áp đầu cực giảm.

Bóng mờ đi. Điện áp trên bóng bằng điện áp đầu cực pin. Khi tải tương đương giảm, pin phải cấp dòng lớn hơn, làm độ giảm thế trên điện trở trong tăng. Vì vậy, điện áp và công suất của bóng giảm.
:::

::: exercise Q26.11
Nếu pin trong Câu hỏi Q26.10 là pin lý tưởng, không có điện trở trong, độ sáng của bóng thay đổi thế nào khi đóng công tắc? Vì sao?
:::

::: solution Lời giải
**Tóm tắt đề bài:** Pin lý tưởng giữ điện áp hai cực không đổi, dù dòng tổng do nguồn cấp có thể tăng.

**Hướng đi:**

- Bóng vẫn mắc trực tiếp giữa hai cực pin.
- Công suất bóng chỉ đổi nếu điện áp trên nó đổi.

Độ sáng bóng không đổi. Khi đóng công tắc, dòng qua nhánh điện trở mới tăng dòng tổng của pin, nhưng điện áp nguồn lý tưởng vẫn giữ nguyên trên bóng.
:::

::: exercise Q26.12
Xét mạch Hình Q26.12. Khi đóng công tắc $S$, độ sáng các bóng thay đổi thế nào nếu pin (a) không có điện trở trong và (b) có điện trở trong đáng kể? Giải thích.

![Hình Q26.12: Hai bóng mắc nối tiếp ở nhánh trên, một bóng ở nhánh dưới và nhánh điện trở có công tắc](img/young-26/hinh-q26-12.png)

**Hình Q26.12:** Hai bóng ở nhánh trên nối tiếp. Nhánh dưới có một bóng. Nhánh giữa có điện trở nối tiếp với công tắc $S$. Ba nhánh đặt song song vào pin.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Đóng công tắc nối thêm nhánh điện trở song song với các nhánh chứa bóng đèn.

**Hướng đi:**

- Pin lý tưởng giữ nguyên điện áp giữa hai nút của ba nhánh.
- Pin thực có sụt áp trong, nên tải tổng lớn hơn làm điện áp đầu cực giảm.

(a) Nếu pin lý tưởng, độ sáng của cả ba bóng không đổi. Điện áp trên mỗi nhánh giữ nguyên, nên dòng qua từng bóng cũng giữ nguyên.

(b) Nếu pin có điện trở trong, nhánh mới làm điện trở tải tương đương giảm. Dòng tổng tăng và điện áp đầu cực pin giảm. Vì vậy, các bóng đều mờ đi.
:::

::: exercise Q26.13
Có thể mắc các điện trở thành một mạng không rút gọn được thành các tổ hợp nối tiếp và song song hay không? Nếu có, hãy nêu một ví dụ. Nếu không, giải thích.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Một phép rút gọn nối tiếp cần các phần tử chung dòng. Một phép rút gọn song song cần các phần tử chung hai nút.

**Hướng đi:**

- Xét một mạng có nhánh nối giữa các nút trung gian.
- Kiểm tra xem cặp phần tử nào thực sự chung dòng hoặc chung cả hai nút.

Có. Một mạch cầu với điện trở nối giữa hai điểm giữa của các nhánh là ví dụ. Nếu điện trở cầu không thỏa điều kiện cân bằng, các điện trở không tạo thành từng cặp nối tiếp hoặc song song trực tiếp. Cần dùng quy tắc Kirchhoff hoặc một phương pháp phân tích mạng tương đương.
:::

::: exercise Q26.14
Pin trong mạch Hình Q26.14 lý tưởng, không có điện trở trong. Sau khi đóng công tắc $S$, độ sáng bóng $B_1$ tăng, giảm hay giữ nguyên?

![Hình Q26.14: Hai bóng B1 và B2 mắc nối tiếp, công tắc nối tắt bóng B2](img/young-26/hinh-q26-14.png)

**Hình Q26.14:** Hai bóng mắc nối tiếp trên nhánh trên. Khi đóng $S$, dây dẫn tạo đường nối tắt song song với bóng $B_2$.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Công tắc tạo một dây dẫn có điện trở rất nhỏ song song với $B_2$.

**Hướng đi:**

- Trước khi đóng công tắc, hai bóng giống nhau chia đều điện áp pin.
- Sau khi đóng, $B_2$ bị nối tắt và $B_1$ nhận gần như toàn bộ điện áp pin.

Độ sáng $B_1$ tăng. Nếu điện trở mỗi bóng được xem như không đổi, công suất của $B_1$ tăng gấp bốn lần so với trước. Bóng $B_2$ không sáng vì hiệu điện thế trên nó bằng không.
:::

::: exercise Q26.15
Trong đèn pin dùng hai pin, các pin thường được nối tiếp. Vì sao không nối chúng song song? Việc mắc song song nhiều pin giống nhau có thể có ưu điểm nào?
:::

::: solution Lời giải
**Tóm tắt đề bài:** Hai cách mắc tạo điện áp nguồn và điện trở trong tương đương khác nhau.

**Hướng đi:**

- So suất điện động của hai pin nối tiếp và song song.
- Xét trường hợp nhiều pin giống nhau cùng chia tải.

Mắc nối tiếp làm suất điện động tổng tăng, phù hợp với đèn pin được thiết kế dùng điện áp cao hơn điện áp của một pin. Mắc song song các pin giống nhau không làm suất điện động tăng, nên có thể không đạt điện áp thiết kế. Tuy vậy, mắc song song nhiều pin giống nhau có thể tăng dung lượng cấp điện và giảm điện trở trong tương đương, nhờ đó duy trì dòng tải lâu hơn. Kết luận này giả sử các pin cùng loại và ở trạng thái tương đương.
:::

::: exercise Q26.16
Ba bóng giống nhau A, B và C nối như Hình Q26.16. Khi đóng công tắc $S$, bóng C tắt. Giải thích. Độ sáng của A và B thay đổi thế nào? Vì sao?

![Hình Q26.16: Ba bóng A, B, C mắc nối tiếp, công tắc tạo đường nối tắt qua bóng C](img/young-26/hinh-q26-16.png)

**Hình Q26.16:** Ba bóng nằm trên cùng một nhánh nối tiếp. Công tắc $S$ mắc song song với bóng C.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Đóng công tắc tạo nhánh nối tắt qua bóng C, nên dòng có thể đi qua dây dẫn thay vì qua bóng này.

**Hướng đi:**

- Khi đóng $S$, hiệu điện thế trên bóng C gần bằng không.
- Điện trở mạch giảm từ ba bóng nối tiếp xuống còn hai bóng nối tiếp.

Bóng C tắt. Dòng qua A và B tăng, vì vậy cả hai sáng hơn. Nếu điện trở bóng không đổi, công suất mỗi bóng A hoặc B tăng từ $\mathcal E^2/(9R)$ lên $\mathcal E^2/(4R)$, tức tăng theo tỉ số $9/4$.
:::

::: exercise Q26.17
Suất điện động của pin đèn pin gần như không đổi theo thời gian, nhưng điện trở trong tăng khi pin cũ và đã sử dụng lâu. Nên dùng loại đồng hồ nào để kiểm tra pin còn tốt không?
:::

::: solution Lời giải
**Tóm tắt đề bài:** Điện áp mạch hở gần bằng suất điện động nên không phản ánh rõ điện trở trong đã tăng.

**Hướng đi:**

- Cho pin cấp dòng qua một tải đã biết.
- Đo điện áp đầu cực khi pin đang có tải và so với giá trị dự kiến.

Dùng vôn kế đo điện áp hai cực khi pin nối với một tải kiểm tra. Khi điện trở trong tăng, sụt áp $Ir$ tăng và điện áp đầu cực dưới tải giảm. Vôn kế đo pin khi để hở mạch có thể vẫn chỉ gần suất điện động, nên phép đo đó không đủ để đánh giá độ suy giảm này.
:::

::: exercise Q26.18
Các tụ trong hai mạch ở Hình Q26.18 có nạp với cùng tốc độ khi đóng công tắc không? Nếu không, ở mạch nào tụ nạp nhanh hơn? Giải thích.

![Hình Q26.18: Mạch nạp gồm hai tụ mắc nối tiếp ở a và hai tụ mắc song song ở b](img/young-26/hinh-q26-18.png)

**Hình Q26.18:** Cả hai mạch dùng cùng nguồn $\mathcal E$, điện trở $R$ và hai tụ giống nhau có điện dung $C$. Ở (a), các tụ nối tiếp. Ở (b), các tụ song song.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Tốc độ nạp tương đối được quyết định bởi hằng số thời gian $\tau=R C_{\mathrm{eq}}$, trong đó $C_{\mathrm{eq}}$ là điện dung tương đương.

**Hướng đi:**

- Tính điện dung tương đương của hai tụ nối tiếp và song song.
- So hằng số thời gian. Hằng số nhỏ hơn ứng với quá trình tiến tới giá trị cuối nhanh hơn.

Ở mạch (a), $C_{\mathrm{eq}}=C/2$, nên $\tau_a=RC/2$. Ở mạch (b), $C_{\mathrm{eq}}=2C$, nên $\tau_b=2RC$. Tụ trong mạch (a) nạp nhanh hơn theo thang thời gian. Dòng ban đầu ở hai mạch đều bằng $\mathcal E/R$ vì tụ chưa tích điện. Tuy vậy, điện tích cuối trên mỗi tụ khác nhau. Mỗi tụ ở mạch (a) đạt $C\mathcal E/2$, còn mỗi tụ ở mạch (b) đạt $C\mathcal E$.
:::

::: exercise Q26.19
Hãy xác minh tích $RC$, hằng số thời gian của mạch, có đơn vị thời gian.
:::

::: solution Lời giải
**Tóm tắt đề bài:** Điện trở có đơn vị ohm, điện dung có đơn vị farad.

**Hướng đi:**

- Khai triển đơn vị SI của hai đại lượng.
- Rút gọn volt và ampere.

$$
\begin{aligned}
&\Omega\cdot\mathrm F = \frac{\mathrm V}{\mathrm A}\cdot\frac{\mathrm C}{\mathrm V}\\
&\quad =\frac{\mathrm C}{\mathrm A}\\
&\quad =\mathrm s.
\end{aligned}
$$

Vì ampere bằng coulomb trên giây, farad nhân ohm có đơn vị giây.
:::

::: exercise Q26.20
Với điện trở rất lớn, có thể tạo mạch R-C có hằng số thời gian vài giây hoặc vài phút. Làm thế nào dùng tính chất này để đo điện trở quá lớn đối với các phương pháp thông thường?
:::

::: solution Lời giải
**Tóm tắt đề bài:** Với điện dung đã biết, hằng số thời gian của mạch nạp bằng tích $RC$.

**Hướng đi:**

- Tạo mạch R-C có tụ điện đã biết điện dung.
- Đo thời gian đáp ứng để suy ra điện trở.

Đo thời gian để điện áp hoặc điện tích của tụ đạt một mốc đã chọn trên quá trình nạp, rồi suy ra hằng số thời gian $\tau$. Từ $\tau=RC$, tính điện trở $R=\tau/C$. Điện trở lớn tạo thời gian đáp ứng dài hơn, nhờ đó khoảng thời gian có thể đo được bằng đồng hồ.
:::

::: exercise Q26.21
Một tụ điện, pin và điện trở mắc nối tiếp. Điện trở có làm thay đổi điện tích cực đại mà tụ tích được không? Vì sao? Điện trở có tác dụng gì?
:::

::: solution Lời giải
**Tóm tắt đề bài:** Xét quá trình nạp từ pin lý tưởng có suất điện động không đổi.

**Hướng đi:**

- Ở trạng thái cuối, dòng điện bằng không nên điện áp trên điện trở bằng không.
- Điện áp cuối trên tụ bằng suất điện động của pin.

Điện trở không làm đổi điện tích cực đại $Q_{\max}=C\mathcal E$. Nó giới hạn dòng ban đầu và quyết định tốc độ nạp qua hằng số thời gian $RC$. Điện trở lớn hơn làm tụ tiến đến điện tích cuối chậm hơn.
:::
