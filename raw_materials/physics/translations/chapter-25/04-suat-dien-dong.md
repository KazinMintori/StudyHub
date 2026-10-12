# 25.4. Suất điện động và mạch điện

Vì sao một điện tích có thể đi qua điện trở và mất thế năng điện, rồi tiếp tục chạy quanh mạch? Để có dòng điện ổn định, mạch phải kín và phải có một nguồn chuyển hóa dạng năng lượng khác thành thế năng điện. Nguồn ấy có suất điện động, nhưng suất điện động không phải là một lực.

## 1. Vì sao cần mạch kín và nguồn điện?

Nếu tạo điện trường bên trong một vật dẫn cô lập, điện tích bắt đầu dịch chuyển. Điện tích dương tích tụ ở một đầu, điện tích âm tích tụ ở đầu kia. Phân bố điện tích này sinh ra điện trường ngược với điện trường ban đầu. Chỉ trong một khoảng thời gian rất ngắn, điện trường tổng bên trong vật dẫn giảm về không, kéo theo mật độ dòng điện và dòng điện cũng bằng không.

![Hình 25.11: Điện tích ở hai đầu vật dẫn cô lập tạo điện trường chống lại trường ban đầu và làm dòng điện dừng](img/young-25/hinh-25-11.png)

**Hình 25.11:** Trong vật dẫn không thuộc mạch kín, dòng điện ban đầu làm điện tích dồn về hai đầu. Trường do điện tích tích tụ tạo ra ngược trường ban đầu, đến khi trường tổng bằng không thì dòng điện dừng.

Điện tích đi qua một vòng kín rồi trở về điểm xuất phát phải có cùng thế năng điện như lúc đầu. Nhưng trong vật liệu có điện trở, điện tích liên tục mất thế năng khi đi theo chiều dòng điện. Vì vậy, ở đâu đó trong mạch phải có quá trình đưa điện tích trở lại mức thế năng cao hơn.

Có thể hình dung như đài phun nước tuần hoàn. Nước chảy từ cao xuống thấp và gom ở bể phía dưới. Máy bơm nâng nước lên trên để chu trình tiếp tục. Không có máy bơm, nước sẽ dồn ở bể đáy và ngừng chảy.

![Hình 25.12: Đài phun nước tuần hoàn cần máy bơm để đưa nước từ thấp lên cao](img/young-25/hinh-25-12.png)

**Hình 25.12:** Máy bơm đưa nước ngược chiều trọng lực để duy trì tuần hoàn. Nguồn điện đảm nhiệm vai trò tương tự đối với điện tích, nhưng cơ chế vật lý của hai hệ khác nhau.

## 2. Suất điện động là công trên một đơn vị điện tích

Một nguồn điện tạo tác dụng đẩy điện tích từ điện thế thấp lên điện thế cao. Tác dụng này được gọi là **suất điện động**, ký hiệu $\mathcal E$. Tên gọi có chữ “động lực” nhưng $\mathcal E$ không phải lực. Nó là năng lượng trên một đơn vị điện tích, cùng đơn vị với điện thế:

$$
1\,\mathrm V=1\,\mathrm{J/C}.
$$

Nguồn điện thực hiện công không do lực điện trường lên điện tích. Ta ký hiệu tác dụng này là lực không tĩnh điện $\vec F_{\mathrm n}$ để phân biệt với lực điện $\vec F_{\mathrm e}=q\vec E$. Trong pin, lực không tĩnh điện bắt nguồn từ phản ứng hóa học và quá trình khuếch tán. Trong máy phát điện, lực từ tác dụng lên điện tích chuyển động tạo cơ chế đẩy. Trong máy tĩnh điện, dây đai hoặc bánh xe chuyển động có thể thực hiện công cơ học lên điện tích.

Đối với một điện tích dương $q$ được nguồn lý tưởng chuyển từ cực âm $b$ lên cực dương $a$, công của nguồn là $W_{\mathrm n}=q\mathcal E$. Điện tích tăng thế năng một lượng $qV_{ab}$, trong đó $V_{ab}=V_a-V_b>0$. Nguồn lý tưởng duy trì hiệu điện thế đầu cực không đổi, độc lập với dòng điện. Đây là mô hình lý tưởng hóa. Trong nguồn ấy, lực không tĩnh điện và lực điện cân bằng nhau, nên động năng không đổi. Do đó:

$$
\begin{aligned}
W_{\mathrm n}&=q\mathcal E,\\
\Delta U&=qV_{ab},\\
q\mathcal E&=qV_{ab},\\
V_{ab}&=\mathcal E.
\end{aligned}
$$

Điều kiện $V_{ab}=\mathcal E$ mô tả nguồn lý tưởng hoặc nguồn thực khi không có dòng điện qua nguồn. Pin, máy phát điện, pin mặt trời, cặp nhiệt điện và pin nhiên liệu đều là các nguồn suất điện động. Chúng chuyển hóa năng lượng cơ, hóa, nhiệt hoặc dạng khác thành thế năng điện của mạch. Một pin đèn pin có suất điện động 1.5 V thực hiện công 1.5 J trên mỗi coulomb điện tích đi qua nó.

![Hình 25.13: Trong nguồn hở, lực không tĩnh điện đẩy điện tích dương từ cực âm lên cực dương, cân bằng lực điện](img/young-25/hinh-25-13.png)

**Hình 25.13:** Ở mạch hở, điện tích không chạy liên tục qua mạch. Bên trong nguồn, lực không tĩnh điện hướng từ cực âm sang cực dương và cân bằng lực điện trên điện tích dương. Vì không có dòng, điện áp đầu cực bằng suất điện động.

## 3. Mạch kín, điện trở trong và điện áp đầu cực

Khi nối điện trở $R$ vào nguồn, hiệu điện thế giữa hai đầu nguồn tạo điện trường trong dây ngoài. Dòng điện quy ước chạy trong mạch ngoài từ cực dương, có điện thế cao, sang cực âm, có điện thế thấp. Bên trong nguồn, dòng điện đi từ cực âm lên cực dương, ngược chiều lực điện tác dụng lên điện tích dương.

Với nguồn lý tưởng và điện trở ngoài Ohm:

$$
\begin{aligned}
V_{ab}&=\mathcal E,\\
V_{ab}&=IR,\\
\mathcal E&=IR.
\end{aligned}
$$

::: warning Dòng điện không bị tiêu thụ trong mạch
Trong một vòng đơn giản, dòng điện có cùng cường độ tại mọi điểm, ngay cả khi tiết diện dây thay đổi. Điện tích được bảo toàn và không tích tụ trong các phần tử mạch đang xét. Điện tích không bị tạo ra hay phá hủy khi đi qua bóng đèn hoặc điện trở. Đại lượng giảm trên điện trở là thế năng điện của điện tích, không phải lượng dòng điện.
:::

![Hình 25.14: Dòng điện chạy từ cực dương qua mạch ngoài về cực âm, còn trong nguồn đi từ cực âm lên cực dương](img/young-25/hinh-25-14.png)

**Hình 25.14:** Trong mạch kín, lực không tĩnh điện bên trong nguồn duy trì dòng điện qua nguồn theo chiều từ cực âm lên cực dương. Trong mạch ngoài, dòng điện chạy từ điện thế cao xuống thấp.

Nguồn thực có điện trở bên trong vật liệu của nó, gọi là **điện trở trong** $r$. Khi dòng điện chạy từ cực âm sang cực dương bên trong nguồn đang cấp điện cho mạch, sụt áp trên điện trở trong là $Ir$. Vì vậy hiệu điện thế giữa hai đầu nguồn, gọi là **điện áp đầu cực**, bằng:

$$
V_{ab}=\mathcal E-Ir.
$$

Năng lượng điện thế mà mỗi coulomb nhận được khi đi qua nguồn là $V_{ab}$ joule, nhỏ hơn công $\mathcal E$ của lực không tĩnh điện trên mỗi coulomb. Phần chênh lệch mất trên điện trở trong.

Với pin 1.5 V, điện áp đầu cực bằng 1.5 V khi không có dòng qua pin. Khi pin cấp dòng, $V_{ab}<\mathcal E$. Nếu pin được nạp và dòng chạy qua nó theo chiều ngược lại, quy ước dòng qua nguồn là âm, nên $V_{ab}=\mathcal E-Ir>\mathcal E$.

Trong mạch ngoài, $V_{ab}=IR$. Ghép hai hệ thức cho nguồn đang cấp dòng:

$$
\begin{aligned}
\mathcal E-Ir&=IR,\\
\mathcal E&=I(R+r),\\
I&=\frac{\mathcal E}{R+r}.
\end{aligned}
$$

::: warning Pin không phải nguồn dòng cố định
Nguồn suất điện động không tạo ra cùng một dòng điện cho mọi mạch. Theo $I=\mathcal E/(R+r)$, khi điện trở ngoài tăng thì dòng điện giảm.
:::

Điện trở trong luôn là đặc tính của nguồn thực, dù sơ đồ mạch vẽ nó thành một phần tử riêng.

![Hình 25.15: Pin có điện áp đầu cực bằng suất điện động khi hở mạch, nhưng thấp hơn khi đang cấp dòng](img/young-25/hinh-25-15.png)

**Hình 25.15:** Điện áp không tải của pin 12 V bằng suất điện động 12 V. Khi pin cấp dòng cho bóng đèn, sụt áp trên điện trở trong làm điện áp đầu cực nhỏ hơn 12 V.

## 4. Ký hiệu mạch và cách mắc dụng cụ đo

Sơ đồ dùng các ký hiệu chuẩn để biểu diễn dây dẫn, điện trở, nguồn và dụng cụ đo. Dây nối lý tưởng có điện trở không đáng kể nên hai đầu dây cùng điện thế. Trong ký hiệu nguồn, vạch dài hơn biểu diễn cực dương, thường là đầu có điện thế cao hơn. Điện trở trong có thể đặt ở hai phía của nguồn trên sơ đồ vì chúng mắc nối tiếp cùng nguồn.

**Bảng 25.4. Ký hiệu sơ đồ mạch**

| Phần tử mạch | Ký hiệu thường dùng | Ý nghĩa hoặc điều kiện lý tưởng |
| --- | --- | --- |
| Dây dẫn | Đoạn nối thẳng | Điện trở không đáng kể |
| Điện trở | Đường gấp khúc | Phần tử có điện trở $R$ |
| Nguồn suất điện động | Hai vạch song song không bằng nhau | Vạch dài là cực dương |
| Nguồn có điện trở trong | Nguồn nối tiếp $r$ | $r$ thuộc tính nội tại của nguồn |
| Vôn kế | Vòng tròn có chữ V | Đo hiệu điện thế, điện trở lý tưởng vô hạn |
| Ampe kế | Vòng tròn có chữ A | Đo dòng điện, điện trở lý tưởng bằng không |

Vôn kế lý tưởng mắc giữa hai điểm cần đo và không hút dòng vì điện trở vô hạn. Ampe kế lý tưởng đặt nối tiếp nhánh cần đo và không làm giảm dòng vì điện trở bằng không.

Để đo hiệu điện thế mà không làm thay đổi đáng kể mạch, mắc vôn kế song song với hai điểm cần đo. Vôn kế lý tưởng có điện trở vô hạn nên không cho dòng điện đi qua. Để đo dòng điện của một nhánh, mắc ampe kế nối tiếp nhánh đó. Ampe kế lý tưởng có điện trở bằng không nên không tạo sụt áp.

### Ứng dụng sinh học: Cá đuối điện

Cá đuối điện tạo cú sốc để làm choáng con mồi hoặc ngăn kẻ săn mồi. Cơ quan phát điện gồm các tế bào dẹt chuyên hóa gọi là electroplaque. Mỗi tế bào tạo suất điện động khoảng 0.05 V. Hàng nghìn tế bào xếp chồng nối tiếp làm suất điện động cộng lại, có thể đạt đến 200 V. Các chồng tế bào này chiếm hơn một nửa khối lượng cơ thể. Cá có thể phát dòng điện đến 30 A trong vài mili giây. Từ thời La Mã cổ đại, cá đuối điện từng được dùng trong một dạng sơ khai của liệu pháp điện để chữa đau đầu và bệnh gút.

![Ảnh ứng dụng sinh học: Cá đuối điện tạo xung điện nhờ các tế bào electroplaque xếp chồng](img/young-25/anh-ca-duoi-dien.png)

**Ảnh ứng dụng sinh học:** Các tế bào điện chuyên hóa xếp chồng làm tăng suất điện động tổng. Hệ này chuyển hóa năng lượng sinh học thành năng lượng điện trong thời gian ngắn.

## 5. Đọc điện áp đầu cực và dòng điện trong các cấu hình khác nhau

### Ví dụ khái niệm 25.4. Nguồn trong mạch hở

Một nguồn có suất điện động $\mathcal E=12\,\mathrm V$ và điện trở trong $r=2\,\Omega$. Mạch ngoài bị hở. Vôn kế và ampe kế lý tưởng chỉ bao nhiêu?

![Hình 25.16: Vôn kế đo điện áp nguồn khi mạch ngoài hở, còn ampe kế chỉ dòng điện bằng không](img/young-25/hinh-25-16.png)

**Hình 25.16:** Hai đầu mạch ngoài không nối với tải, nên không có vòng kín cho dòng điện.

::: details Lời giải Ví dụ khái niệm 25.4
**Tóm tắt đề bài:** $\mathcal E=12\,\mathrm V$, $r=2\,\Omega$, mạch hở.

**Hướng đi:**

- Mạch hở không có đường khép kín, nên dòng qua nguồn bằng không.
- Khi $I=0$, sụt áp $Ir$ trên điện trở trong bằng không và điện áp đầu cực bằng suất điện động.

Do đó:

$$
\begin{aligned}
I&=0,\\
V_{ab}&=\mathcal E-Ir\\
&=12-0\\
&=12\,\mathrm V.
\end{aligned}
$$

Ampe kế chỉ 0 A, vôn kế chỉ 12 V.
:::

### Ví dụ 25.5. Nguồn trong mạch kín

Nối điện trở ngoài $R=4\,\Omega$ vào nguồn của ví dụ trước. Tìm dòng điện và điện áp đầu cực.

![Hình 25.17: Nguồn có điện trở trong nối với điện trở tải 4 Ω, ampe kế nối tiếp và vôn kế đo điện áp hai cực nguồn](img/young-25/hinh-25-17.png)

**Hình 25.17:** Điện trở trong và điện trở tải nối tiếp nhau trong vòng kín. Vôn kế mắc song song với hai đầu nguồn.

::: details Lời giải Ví dụ 25.5
**Tóm tắt đề bài:** $\mathcal E=12\,\mathrm V$, $r=2\,\Omega$, $R=4\,\Omega$.

**Hướng đi:**

- Ampe kế lý tưởng có điện trở không, nên điện trở ngoài vẫn là 4 Ω.
- Dòng qua nguồn chịu tổng điện trở nối tiếp $R+r$.
- Tính điện áp đầu cực bằng $V_{ab}=IR$ hoặc $V_{ab}=\mathcal E-Ir$ để kiểm tra.

$$
\begin{aligned}
I&=\frac{\mathcal E}{R+r}\\
&=\frac{12}{4+2}\\
&=2.00\,\mathrm A,\\
V_{ab}&=IR\\
&=(2.00)(4)\\
&=8.00\,\mathrm V.
\end{aligned}
$$

Kiểm tra trực tiếp ở nguồn:

$$
\begin{aligned}
V_{ab}&=\mathcal E-Ir\\
&=12-(2.00)(2)\\
&=8.00\,\mathrm V.
\end{aligned}
$$

Trong trường hợp pin cấp điện, dòng chạy bên trong pin từ cực âm lên cực dương và điện áp đầu cực thấp hơn suất điện động. Nếu pin được nạp, dòng qua pin đổi chiều và điện áp đầu cực lớn hơn suất điện động. Điện trở trong càng nhỏ thì độ chênh này càng ít.
:::

### Ví dụ khái niệm 25.6. Đặt vôn kế và ampe kế đúng chỗ

Giữ nguyên nguồn $\mathcal E=12$ V, $r=2\,\Omega$ và tải $R=4\,\Omega$, nhưng chuyển vị trí các dụng cụ đo như Hình 25.18. So sánh hai cách mắc.

![Hình 25.18: Hai vị trí khác nhau của vôn kế và ampe kế trong cùng một mạch nguồn và điện trở](img/young-25/hinh-25-18.png)

**Hình 25.18:** Ở (a), vôn kế đo song song với tải còn ampe kế nằm nối tiếp, nên mạch vẫn kín. Ở (b), vôn kế lý tưởng nằm nối tiếp trong vòng mạch và làm dòng điện bằng không.

::: details Lời giải Ví dụ khái niệm 25.6
**Tóm tắt đề bài:** Cùng nguồn và điện trở như Ví dụ 25.5. Vôn kế lý tưởng có điện trở vô hạn, ampe kế lý tưởng có điện trở bằng không.

**Hướng đi:**

- Ở (a), vôn kế mắc song song với tải và ampe kế mắc nối tiếp, nên các dụng cụ không làm đổi mạch lý tưởng.
- Ở (b), điện trở vô hạn của vôn kế chặn dòng qua mạch. Khi đó sụt áp trên tải bằng không, còn vôn kế đo điện áp đầu cực không tải.

(a) Mạch vẫn có dòng $I=2.00$ A như Ví dụ 25.5. Vôn kế mắc giữa hai đầu tải nên chỉ $8.00$ V. Ampe kế đặt ở vị trí khác trên cùng vòng mạch vẫn chỉ $2.00$ A.

(b) Vôn kế mắc nối tiếp làm mạch hở trong giới hạn lý tưởng:

$$
I=0.
$$

Do không có dòng qua điện trở trong hay tải, sụt áp trên mỗi điện trở bằng không. Vôn kế đo toàn bộ điện áp đầu cực không tải:

$$
V_{bb'}=V_{ab}=\mathcal E=12\,\mathrm V.
$$

Ampe kế chỉ 0 A. Vôn kế lý tưởng cần mắc song song với hai điểm cần đo. Đặt nó nối tiếp có thể làm thay đổi hoàn toàn mạch đang đo.
:::

### Cảnh báo: Điện trở trong là một phần của nguồn thực

Sơ đồ thường vẽ suất điện động $\mathcal E$ và điện trở trong $r$ thành hai phần riêng để dễ phân tích. Trong nguồn thực, chúng cùng tạo nên một thiết bị và không thể tách riêng. Bỏ qua $r$ có thể làm sai dòng điện và điện áp đầu cực.

### Ví dụ 25.7. Nguồn bị ngắn mạch

Thay điện trở $4\,\Omega$ trong Ví dụ 25.5 bằng một dây dẫn có điện trở bằng không. Tìm dòng điện và điện áp đầu cực.

![Hình 25.19: Hai cực nguồn nối trực tiếp qua dây dẫn có điện trở bằng không](img/young-25/hinh-25-19.png)

**Hình 25.19:** Dây dẫn lý tưởng nối tắt hai cực, nên hiệu điện thế giữa hai cực bằng không.

::: details Lời giải Ví dụ 25.7
**Tóm tắt đề bài:** $\mathcal E=12\,\mathrm V$, $r=2\,\Omega$, điện trở ngoài $R=0$.

**Hướng đi:**

- Dây nối tắt làm hai cực nguồn cùng điện thế, vì thế $V_{ab}=0$.
- Dòng điện bị giới hạn chỉ bởi điện trở trong. Dùng $V_{ab}=\mathcal E-Ir$ để tính.

$$
\begin{aligned}
V_{ab}&=IR\\
&=I(0)\\
&=0,\\
0&=\mathcal E-Ir,\\
I&=\frac{\mathcal E}{r}\\
&=\frac{12}{2}\\
&=6.00\,\mathrm A.
\end{aligned}
$$

Đây là **ngắn mạch**. Dòng ngắn mạch bằng suất điện động chia cho điện trở trong, nên nguồn có điện trở trong rất nhỏ có thể tạo dòng rất lớn. Dây nhỏ có thể nóng chảy. Ắc quy ô tô hoặc đường dây điện gia dụng có điện trở trong nhỏ hơn nhiều so với ví dụ có thể tạo dòng đủ lớn để làm nổ ắc quy hoặc gây cháy. Không được chủ ý nối tắt nguồn thực.
:::

## 6. Độ biến thiên điện thế quanh một vòng mạch

Điện tích đi hết một vòng kín trở về vị trí ban đầu, nên độ biến thiên tổng thế năng điện bằng không. Do đó tổng đại số các suất điện động và độ giảm điện thế quanh vòng cũng bằng không. Với mạch đơn giản gồm nguồn có $r$ và điện trở ngoài $R$:

$$
\begin{aligned}
\mathcal E-Ir-IR&=0,\\
\mathcal E&=I(r+R).
\end{aligned}
$$

Khi đi qua nguồn theo chiều từ cực âm lên cực dương, điện thế tăng $\mathcal E$. Khi đi qua điện trở trong và điện trở ngoài theo chiều dòng điện, điện thế giảm lần lượt $Ir$ và $IR$. Sau một vòng, điện thế trở về giá trị ban đầu.

![Hình 25.20: Đồ thị điện thế tăng qua nguồn rồi giảm qua điện trở trong và điện trở ngoài](img/young-25/hinh-25-20.png)

**Hình 25.20:** Đồ thị ghi điện thế tại các điểm dọc vòng mạch. Trục ngang biểu thị thứ tự đi quanh mạch, không nhất thiết là khoảng cách hình học.

Các phương trình trên thường giả sử các điện trở tuân theo định luật Ohm. Nếu có linh kiện phi tuyến như điôt, quy tắc tổng biến thiên điện thế vẫn đúng, nhưng không thể coi $R$ là hằng số để giải đại số. Có thể cần giải số quan hệ dòng–áp của linh kiện.

Mô hình nguồn với $\mathcal E$ và $r$ cũng chỉ là gần đúng. Suất điện động có thể thay đổi và quan hệ điện áp–dòng qua nguồn có thể phức tạp hơn một điện trở trong Ohm. Với pin đèn pin cũ, suất điện động thường giảm ít hơn điện trở trong, vốn có thể tăng từ dưới một ôm lên đến khoảng 1000 Ω hoặc hơn sau thời gian dài sử dụng. Ở buổi sáng lạnh, ắc quy ô tô có thể cấp dòng nhỏ hơn do điện trở trong tăng khi nhiệt độ giảm, chứ không nhất thiết vì suất điện động giảm đáng kể.

### Câu hỏi kiểm tra

Xếp dòng điện của ba mạch từ lớn đến nhỏ:

- (i) Điện trở 1.4 Ω nối với pin 1.5 V có điện trở trong 0.10 Ω.
- (ii) Điện trở 1.8 Ω nối với pin 4.0 V có điện áp đầu cực 3.6 V, điện trở trong chưa biết.
- (iii) Một điện trở chưa biết nối với pin 12.0 V có điện trở trong 0.20 Ω và điện áp đầu cực 11.0 V.

<details><summary>Đáp án và giải thích</summary>

Ở (i), tổng điện trở là $1.4+0.10=1.5\,\Omega$:

$$
I_{(i)}=\frac{1.5}{1.5}=1.0\,\mathrm A.
$$

Ở (ii), điện áp đầu cực là điện áp trên điện trở ngoài:

$$
I_{(ii)}=\frac{3.6}{1.8}=2.0\,\mathrm A.
$$

Ở (iii), sụt áp trên điện trở trong là $12.0-11.0=1.0$ V:

$$
I_{(iii)}=\frac{12.0-11.0}{0.20}=5.0\,\mathrm A.
$$

Thứ tự từ lớn đến nhỏ là (iii), (ii), (i).

</details>

## Tóm tắt

- Một vật dẫn cô lập chỉ có dòng điện thoáng qua. Điện tích tích tụ ở hai đầu tạo điện trường ngược làm dòng dừng.
- Nguồn suất điện động dùng lực không tĩnh điện chuyển điện tích từ điện thế thấp lên cao. Suất điện động là công trên một đơn vị điện tích, không phải lực.
- Với nguồn thực cấp dòng, $V_{ab}=\mathcal E-Ir$ và $I=\mathcal E/(R+r)$. Khi nạp pin, dòng qua nguồn đổi chiều và điện áp đầu cực có thể lớn hơn suất điện động.
- Ampe kế lý tưởng mắc nối tiếp, vôn kế lý tưởng mắc song song. Dụng cụ đo mắc sai vị trí có thể làm thay đổi mạch.
- Ngắn mạch có $R=0$ và dòng bị giới hạn bởi $r$. Với vòng mạch kín, tổng đại số các độ tăng và giảm điện thế bằng không.

## Tài liệu tham khảo

Young, H. D., & Freedman, R. A. *University Physics with Modern Physics* (ấn bản 15, mục 25.4, tr. 822–827). Pearson.
