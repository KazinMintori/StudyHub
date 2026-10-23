<!-- Source: Section 19.3, printed 617–618, PDF 637–638. -->

## 19.3. Đường đi giữa các trạng thái nhiệt động

Khi một hệ nhiệt động chuyển biến từ trạng thái ban đầu sang trạng thái cuối cùng, hệ phải đi qua một chuỗi các trạng thái trung gian liên tiếp. Chuỗi các trạng thái trung gian nối liền trạng thái đầu và trạng thái cuối được gọi là **đường đi** (path) của quá trình nhiệt động.

Nếu mọi trạng thái trung gian đều là trạng thái cân bằng, đường đi có thể biểu diễn trên giản đồ $pV$. Với cùng trạng thái đầu và cuối, có nhiều đường đi khác nhau.

### Sự phụ thuộc của công vào đường đi

Để thấy rõ công cơ học phụ thuộc vào đường đi như thế nào, ta xét sự biến đổi của một hệ từ trạng thái ban đầu 1 (với áp suất $p_1$ và thể tích $V_1$) sang trạng thái cuối cùng 2 (với áp suất $p_2 < p_1$ và thể tích $V_2 > V_1$).

![Hình 19.7: Công do hệ thực hiện trong quá trình biến đổi giữa hai trạng thái phụ thuộc vào đường đi: (a) Ba đường đi khác nhau giữa trạng thái 1 và 2. (b) Đường đi qua điểm 3 có công $W = p_1(V_2 - V_1)$. (c) Đường đi qua điểm 4 có công $W = p_2(V_2 - V_1)$. (d) Một đường cong nối trực tiếp trạng thái 1 với trạng thái 2 cho một giá trị công khác.](../img/young-19/a-hinh-19-07.png)

Có nhiều phương án khác nhau để đưa hệ từ trạng thái 1 đến trạng thái 2:

- Phương án 1 (Hình 19.7b): Trước hết cho hệ giãn nở ở áp suất không đổi $p_1$ từ thể tích $V_1$ đến $V_2$ (chuyển sang trạng thái trung gian 3). Trong giai đoạn này, hệ thực hiện công $W = p_1(V_2 - V_1)$. Tiếp theo, giữ thể tích không đổi ở giá trị $V_2$ và làm lạnh hệ để áp suất giảm từ $p_1$ xuống $p_2$ (từ trạng thái 3 sang 2). Vì thể tích không đổi nên công giai đoạn này bằng không. Tổng công thực hiện dọc theo đường $1 \to 3 \to 2$ là $W = p_1(V_2 - V_1)$.
- Phương án 2 (Hình 19.7c): Trước hết giữ thể tích không đổi ở $V_1$ và làm lạnh để giảm áp suất từ $p_1$ xuống $p_2$ (từ trạng thái 1 sang trạng thái trung gian 4). Giai đoạn này không sinh công. Sau đó cho hệ giãn nở ở áp suất không đổi $p_2$ từ $V_1$ đến $V_2$ (từ trạng thái 4 sang 2). Công sinh ra trong giai đoạn này là $W = p_2(V_2 - V_1)$. Tổng công thực hiện dọc theo đường $1 \to 4 \to 2$ là $W = p_2(V_2 - V_1)$.
- Phương án 3 (Hình 19.7a): Cho hệ biến đổi dọc theo đường cong trơn nối trực tiếp từ 1 đến 2, trong đó cả áp suất và thể tích đều biến thiên liên tục. Công thực hiện bằng diện tích hình thang cong dưới đồ thị, nhận giá trị nằm giữa hai giá trị công của phương án 1 và phương án 2.
- Một chu trình có thể được tạo từ những đoạn trên giản đồ: Cho hệ đi từ trạng thái 1 sang 2 theo đường $1 \to 3 \to 2$, sau đó quay trở về trạng thái 1 theo đường $2 \to 4 \to 1$. Tổng công sinh ra trong chu trình bằng hiệu diện tích giữa đường đi tới và đường đi về, chính là diện tích phần mặt phẳng khép kín được bao bởi chu trình.

Vì $p_1 > p_2$, công dọc theo đường $1 \to 3 \to 2$ lớn hơn đáng kể so với công dọc theo đường $1 \to 4 \to 2$. Như vậy:

> Công do một hệ sinh ra không chỉ phụ thuộc vào trạng thái ban đầu và trạng thái cuối cùng, mà phụ thuộc chặt chẽ vào đường đi nối giữa hai trạng thái đó.

### Sự phụ thuộc của nhiệt lượng vào đường đi

Tương tự như công, nhiệt lượng $Q$ truyền vào hệ trong một quá trình nhiệt động cũng phụ thuộc vào đường đi.

Để chứng minh điều này, ta xét hai quá trình khác nhau đưa cùng một lượng khí lý tưởng từ trạng thái ban đầu 1 ($V_1 = 2{,}0\,\mathrm L, T = 300\,\mathrm K$) đến trạng thái cuối cùng 2 ($V_2 = 5{,}0\,\mathrm L, T = 300\,\mathrm K$).

![Hình 19.8: (a) Khí giãn nở đẳng nhiệt chậm và có kiểm soát từ trạng thái 1 đến trạng thái 2 ở cùng nhiệt độ $T$: Hệ sinh công dương và nhận nhiệt từ bếp cấp nhiệt ($W > 0$ và $Q > 0$). (b) Cùng lượng khí đó giãn nở tự do nhanh chóng vào chân không từ cùng trạng thái ban đầu đến cùng trạng thái cuối: Hệ không sinh công và không trao đổi nhiệt với môi trường ngoài ($W = 0$ và $Q = 0$).](../img/young-19/a-hinh-19-08.png)

Hai quá trình được thực hiện như sau:

- Quá trình thứ nhất (Hình 19.8a): Khối khí chứa trong xi lanh tiếp xúc với bếp giữ nhiệt độ không đổi $300\,\mathrm K$. Khí giãn nở chậm và có kiểm soát đẩy pít-tông ra xa cho đến khi thể tích đạt $5{,}0\,\mathrm L$. Vì khí đẩy pít-tông dịch chuyển nên hệ sinh công dương ($W > 0$). Để nhiệt độ của khối khí không bị giảm trong quá trình sinh công, nhiệt lượng phải liên tục truyền từ bếp vào khối khí, do đó $Q > 0$.
- Quá trình thứ hai (Hình 19.8b): Khối khí đặt trong một bình có vỏ cách nhiệt hoàn toàn, được ngăn đôi bởi một vách ngăn mỏng. Ban đầu, một bên chứa $2{,}0\,\mathrm L$ khí ở $300\,\mathrm K$, bên còn lại có thể tích $3{,}0\,\mathrm L$ là chân không hoàn toàn. Khi vách ngăn bị phá, khối khí nhanh chóng tràn vào vùng chân không và lấp đầy toàn bộ bình $5{,}0\,\mathrm L$. Khối khí giãn nở tự do vào chân không không đẩy bất kỳ vật thể chuyển động nào, do đó khí không sinh công cơ học ($W = 0$). Đồng thời, do bình được bọc cách nhiệt hoàn toàn nên không có nhiệt lượng truyền vào hoặc ra khỏi hệ ($Q = 0$).

Thực nghiệm với khí mật độ thấp cho thấy khi khí lý tưởng giãn nở tự do, nhiệt độ của khối khí không thay đổi. Do đó trạng thái cuối cùng của quá trình thứ hai hoàn toàn trùng với trạng thái cuối của quá trình thứ nhất ($V_2 = 5{,}0\,\mathrm L, T = 300\,\mathrm K$).

Hai quá trình xuất phát từ cùng một trạng thái ban đầu và kết thúc ở cùng một trạng thái cuối cùng. Tuy nhiên, ở quá trình thứ nhất ta có $W > 0$ và $Q > 0$, trong khi ở quá trình thứ hai ta có $W = 0$ và $Q = 0$. Điều này khẳng định:

> Nhiệt lượng truyền vào hoặc ra khỏi một hệ trong quá trình nhiệt động phụ thuộc vào đường đi giữa các trạng thái.

Vì nhiệt lượng phụ thuộc vào quá trình biến đổi, việc nói một hệ "chứa một lượng nhiệt xác định" là cách hiểu hoàn toàn sai lầm. Nhiệt lượng không phải là thuộc tính trạng thái của vật chất. Ta chỉ có thể nói về nhiệt lượng khi có sự truyền năng lượng giữa hệ và môi trường xung quanh do chênh lệch nhiệt độ.

::: Exercise Tự kiểm tra 19.3
Xét hệ ở Hình 19.7a. Mỗi quá trình sau được biểu diễn bằng một đoạn thẳng nối trực tiếp trạng thái đầu và trạng thái cuối trên giản đồ $pV$. Hãy sắp xếp các quá trình sau theo thứ tự công do hệ sinh ra, từ giá trị dương lớn nhất đến giá trị âm lớn nhất: (i) $1 \to 2$. (ii) $2 \to 1$. (iii) $3 \to 4$. (iv) $4 \to 3$.

<details><summary>Xem lời giải thích</summary>
Kết quả sắp xếp là: (i) và (iv) bằng nhau (dương lớn nhất), tiếp theo là (ii) và (iii) bằng nhau (âm lớn nhất).

Giải thích chi tiết:

- Trên giản đồ $pV$, mỗi quá trình là một đoạn thẳng nối hai đỉnh của hình chữ nhật $1-3-2-4$.
- Diện tích hình thang dưới mỗi đường biểu diễn là như nhau: Hai đoạn thẳng $1 \to 2$ và $4 \to 3$ có cùng hai đáy $p_1, p_2$ và cùng bề rộng $V_2 - V_1$. Gọi $A$ là diện tích hình thang:

$$
A = \frac{p_1 + p_2}{2}\,(V_2 - V_1)
$$

- Đối với quá trình (i) và (iv): Thể tích tăng ($V_2 > V_1$), khối khí giãn nở sinh công dương:

$$
W_{\mathrm{i}} = W_{\mathrm{iv}} = +A > 0
$$

- Đối với quá trình (ii) và (iii): Thể tích giảm ($V_2 < V_1$), hệ bị nén lại sinh công âm:

$$
W_{\mathrm{ii}} = W_{\mathrm{iii}} = -A < 0
$$

Vì vậy, hai quá trình (i) và (iv) cùng có công dương lớn nhất, còn hai quá trình (ii) và (iii) cùng có công âm lớn nhất.
</details>
:::
