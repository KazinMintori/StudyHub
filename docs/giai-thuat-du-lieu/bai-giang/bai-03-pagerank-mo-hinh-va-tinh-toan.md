---
course: giai-thuat-du-lieu
lecture: bai-03-pagerank-mo-hinh-va-tinh-toan
section: lecture
title: "PageRank: Mô hình & tính toán"
prerequisites: ["do-thi","ma-tran"]
lessonStatus: ready
description: "Mô hình người lướt ngẫu nhiên (Random Surfer), ma trận liên kết, xử lý nút cụt và bẫy liên kết, biểu diễn thưa, tính toán MapReduce theo khối và phân tích chi phí."
---

Học phần **Giải thuật nền tảng của Khoa học dữ liệu**, học kỳ 1 năm học 2026–2027.

Tài liệu đi cùng [bộ trang chiếu Bài 03](#slides). Các lời giải bài tập được gập để người học thử tính trước khi đối chiếu.

---

## 1. Giới thiệu bài học

Một công cụ tìm kiếm phải chọn và sắp xếp các trang phù hợp với truy vấn. Nội dung trang giúp đánh giá mức phù hợp. Cấu trúc liên kết cung cấp thêm tín hiệu về tầm quan trọng của trang. PageRank xây dựng điểm từ cấu trúc này, không tự đo mức phù hợp với từng truy vấn.

Bài học bắt đầu từ một đồ thị bốn trang có thể tính tay. Từ phép chia điểm theo liên kết, ta xây dựng mô hình xử lý được nút cụt và bẫy liên kết. Sau đó chuyển phép tính sang dạng thưa và chia khối. Phần chi phí giải thích việc chia nhỏ tiết kiệm bộ nhớ ở đâu và vì sao thêm máy chưa chắc giảm thời gian theo cùng tỷ lệ.

Sau bài học, sinh viên cần lập được ma trận liên kết và một vòng cập nhật. Giải thích điều kiện hội tụ và dừng. Mô tả Map, Combine, Reduce. Tính các chi phí cơ bản. Và cài đặt, kiểm thử phiên bản Python. Kiến thức sử dụng gồm đồ thị có hướng, phép nhân ma trận–véc tơ, xác suất cơ bản và mô hình MapReduce của Bài 02.

---

## 2. Bài toán Xếp hạng trang web

**Đầu vào và đầu ra.** Đầu vào là đồ thị có hướng $G=(V,E)$, với $n=|V|$ trang và $m=|E|$ liên kết. Cạnh $j\to i$ nghĩa là trang $j$ trỏ tới trang $i$. Hai liên kết cùng nguồn cùng đích được gộp thành một cạnh. Đầu ra là một điểm $r_i\ge0$ cho mỗi trang và thứ tự giảm dần theo điểm (cho phép đồng hạng). Quy ước chuẩn hóa là $r_1+r_2+\cdots+r_n=1$, viết gọn thành $\sum_{i=1}^n r_i=1$: Chỉ số $i$ chạy qua tất cả trang. Lưu ý rằng tổng bằng 1 chưa xác định duy nhất cách chấm điểm, bởi nhiều véc tơ khác nhau đều thỏa mãn điều kiện này. Quy tắc chấm điểm cụ thể là nội dung của phần 3.

**Ví dụ chuẩn xuyên suốt bài giảng.** Ta dùng đồ thị bốn trang trong Hình 5.1 của giáo trình MMDS, $n=4$, $m=8$: A trỏ tới B, C, D. B trỏ tới A, D. C trỏ tới A. D trỏ tới B, C.

![Đồ thị bốn trang: A tới B, C, D. Trang B tới A, D. Trang C tới A. Trang D tới B, C](img/lec-03/graph-pages.svg)

Bậc ra (số liên kết đi khỏi trang) lần lượt là $d_A=3$, $d_B=2$, $d_C=1$, $d_D=2$. Đồ thị này đủ nhỏ để chạy tay từng bước, và cả bài sẽ quay lại nó ở mô hình, thuật toán, chia khối và chi phí.

**Thử nghiệm đầu tiên: Đếm liên kết vào.** Trên ví dụ, A, B, C, D đều có đúng 2 liên kết vào, nên chuẩn hóa cho mỗi trang $\frac{2}{8}=\frac{1}{4}$, dẫn đến cả bốn trang đều đồng hạng. Cách đếm này có hai hạn chế rõ: Nó coi mọi liên kết ngang giá trị, dù liên kết từ C (chỉ trỏ một nơi) khác liên kết từ A (trỏ ba nơi), và nó không lan truyền tầm quan trọng: Một trang được trỏ bởi trang quan trọng đáng lẽ phải quan trọng hơn.

**Từ đếm sang chia điểm.** Ta cho mỗi trang một lượng điểm rồi để trang nguồn *chia đều* điểm của mình cho các đích theo bậc ra, thay vì chỉ đếm cạnh vào. Khởi tạo mỗi trang $\frac{1}{4}$ điểm. A chia cho ba đích: Mỗi đích nhận $(\frac{1}{4})/3=\frac{1}{12}$. B và D chia cho hai đích, mỗi cạnh mang $\frac{1}{8}$. C chuyển cả $\frac{1}{4}$ cho A.

**Cộng tại đích và một vòng hoàn chỉnh.** Mọi trang tính đồng thời từ *điểm cũ*: A chỉ nhận từ B và C, được $\frac{1}{8}+\frac{1}{4}=\frac{3}{8}$. B nhận $\frac{1}{12}$ từ A và $\frac{1}{8}$ từ D, được $\frac{5}{24}$. Tương tự C và D đều $\frac{5}{24}$. Tổng $\frac{3}{8}+3\times \frac{5}{24} = 1$, không mất không thêm. Sau một vòng, A đứng trước B, C, D đồng hạng, khác biệt hoàn toàn với kết quả đồng hạng của cách đếm liên kết vào, vì C chuyển toàn bộ điểm cho A.

Ba điểm phương pháp luận cần giữ:
1. Mọi đóng góp xác định bởi điểm cũ và bậc ra của nguồn, không phải bậc vào của đích.
2. Đồng bộ: Không dùng điểm mới của trang này khi tính trang khác trong cùng vòng.
3. Một vòng chưa phải PageRank. Quy tắc hiện tại còn hai lỗ hổng: Chưa xử lý trang không có liên kết ra, và chưa bảo đảm việc lặp hội tụ trên mọi đồ thị. Phần 3 xử lý cả hai.

---

## 3. Mô hình và thuật toán PageRank

### Ma trận liên kết và phép lặp truyền điểm

**Ma trận $M_0$.** Ta hình thức hóa phép chia điểm bằng đại số tuyến tính. Đặt $d_j$ là bậc ra của trang $j$. Ma trận liên kết $M_0$ cỡ $n\times n$ được định nghĩa theo cột: Giá trị $(M_0)_{ij}=1/d_j$ nếu có cạnh $j\to i$ và $d_j>0$, bằng $0$ trong trường hợp còn lại. Quy ước này quan trọng: **Cột** $j$ là trang nguồn, **hàng** $i$ là trang đích. Với đồ thị bốn trang (thứ tự hàng/cột A, B, C, D):

$$M_0=\begin{pmatrix} 0 & \frac{1}{2} & 1 & 0\\ \frac{1}{3} & 0 & 0 & \frac{1}{2}\\ \frac{1}{3} & 0 & 0 & \frac{1}{2}\\ \frac{1}{3} & \frac{1}{2} & 0 & 0 \end{pmatrix}$$

Cột A là $(0,\frac{1}{3},\frac{1}{3},\frac{1}{3})^T$: A chia cho ba đích và không tự giữ điểm. Cạnh *đi vào* A nằm ở **hàng** A, không nằm ở cột A. Khi lập ma trận từ hình, hãy kiểm tra rõ hàng đích và cột nguồn. Trang không có liên kết ra được biểu diễn bằng cột toàn 0. Ta chưa thực hiện phép chia cho không, phần 3 sẽ xử lý trường hợp này riêng.

**Phép lặp thô.** Điểm là véc tơ cột $r$ với $r_i\ge 0$, $\sum_i r_i=1$. Khởi tạo đều $r^0=(1/n,\dots,1/n)^T$. Chỉ số $t$ đếm số bước đã thực hiện. Khi mọi trang đều có liên kết ra, một vòng là:

$$r^{t+1}=M_0\,r^t.$$

Nhân ma trận–véc tơ thực hiện đồng thời "chia tại nguồn, cộng tại đích": Thành phần $i$ của $M_0r$ là $\sum_{j:\,j\to i} r_j/d_j$. Trên ví dụ: $r^1=(\frac{9}{24},\,\frac{5}{24},\,\frac{5}{24},\,\frac{5}{24})^T$, khớp đúng bảng chia điểm của phần 2.

**Điểm ổn định và mối liên hệ với ma trận.** Điểm ổn định là véc tơ không đổi qua cập nhật, $r^*=M_0r^*$, tức trong ngôn ngữ đại số tuyến tính, đây chính là véc tơ riêng ứng với giá trị riêng bằng 1 của ma trận có tổng mỗi cột bằng 1. Giáo trình MMDS trình bày PageRank qua quan điểm này. Với mục đích tính toán, ta không cần khử hay tính giá trị riêng, mà lặp nhân ma trận–véc tơ tới khi véc tơ ít thay đổi. Ở quy mô lớn, ta tận dụng các phần tử khác 0 thay vì lưu và xử lý toàn bộ ma trận đặc. Phần 4 xây dựng cách tổ chức đó.

**Một quan sát trên ví dụ.** Hai hàng B và C của $M_0$ giống hệt nhau nên $r_B=r_C$ ở mọi vòng. Lập luận quy nạp đơn giản cho thấy $r_D$ cũng bằng chúng. Giới hạn của ví dụ có nghiệm dạng: Điểm $r_A=\frac{3}{9}=\frac{1}{3}$ và $r_B=r_C=r_D=\frac{2}{9}$. Đáng chú ý: **$r_B=r_C=r_D$ là hệ quả của khởi tạo đều và quy tắc cập nhật trên đồ thị này, không phải do ba nút đối xứng về cấu trúc**, bởi C chỉ có 1 liên kết ra trong khi B, D có 2. Điểm số đo tổng khối lượng nhận được, không đo bậc.

**Giới hạn của phép lặp thô.** Không thể kết luận phép lặp hội tụ trên mọi đồ thị chỉ từ điều kiện tổng cột bằng 1. Chẳng hạn, một đồ thị có thể khiến điểm dao động theo chu kỳ. Web còn có nút cụt và nhóm trang không có liên kết ra ngoài. Ta sẽ bổ sung bước nhảy và xử lý nút cụt, rồi chứng minh hội tụ cho mô hình đầy đủ dưới đây.

### Nút cụt, bước nhảy và phép cập nhật đầy đủ

**Nút cụt làm mất điểm.** Xóa cạnh C→A khỏi đồ thị ví dụ: C trở thành nút cụt (không còn liên kết ra, nhưng vẫn nhận cạnh vào). Cột C của $M_0$ toàn 0, nên điểm cũ của C không đóng góp cho đích nào. Từ $r^0$ đều, một vòng lặp thô cho $(\frac{3}{24},\,\frac{5}{24},\,\frac{5}{24},\,\frac{5}{24})^T$, tổng $\frac{18}{24}=\frac{3}{4}$: Mất đúng $\frac{1}{4}$ điểm của C. Lặp tiếp, tổng điểm giảm dần về 0, tức tầm quan trọng bị "rò rỉ" dần khỏi đồ thị. (Biến thể này là Hình 5.3, biến thể `dead` trong mã thực hành.)

**Bẫy liên kết dồn điểm.** Thay C→A bằng khuyên C→C (Hình 5.6, biến thể `trap`): C có bậc ra 1 nên tổng điểm vẫn được giữ, nhưng người đã đến C không bao giờ rời C nếu chỉ đi theo liên kết. Phép lặp thô trên đồ thị này dồn toàn bộ điểm về C. Một bẫy tổng quát là tập trang có liên kết ra nhưng không có cạnh ra khỏi tập.

**Bước nhảy và bù nút cụt.** Mô hình đầy đủ sửa cả hai lỗi bằng cách bổ sung hành vi của người lướt ngẫu nhiên. Mỗi bước, với xác suất $\beta$ người lướt đi theo một liên kết ra (chia đều), với xác suất $1-\beta$ nhảy đều tới một trang bất kỳ trong $n$ trang, kể cả trang hiện tại. Điều kiện $0<\beta<1$, ví dụ tính tay dùng $\beta=\frac{4}{5}$. Riêng cho nút cụt: Trong nhánh theo liên kết, điểm của nút cụt được **phân phối lại đều** cho cả $n$ trang. Đặt $\delta^t=\sum_{j:\,d_j=0}r_j^t$ là tổng điểm các nút cụt và $u=(1/n,\dots,1/n)^T$, quy tắc cập nhật đầy đủ là:

$$r_i^{\,t+1}=\beta\sum_{j:\,j\to i}\frac{r_j^{\,t}}{d_j}+\frac{(1-\beta)+\beta\,\delta^t}{n}.$$

Dạng véc tơ tương đương:

$$r^{t+1}=\beta M_0 r^t+\bigl((1-\beta)+\beta\delta^t\bigr)u.$$

![Điểm từ nút cụt được phân phối lại đều tới cả bốn trang](img/lec-03/model-dead-redistribute.svg)

**Lưu ý về dạng công thức có xử lý nút cụt (Dead ends):** Nếu chỉ áp dụng công thức taxation thuần túy $v'=\beta Mv+(1-\beta)e/n$ trên ma trận còn cột 0 mà thiếu số hạng tái phân bổ $\beta\delta$, thì khi gặp nút cụt, tổng xác suất toàn mạng sẽ bị suy giảm và nhỏ hơn 1. Quy chuẩn chuẩn hóa trong bài giảng này áp dụng nguyên lý: Tái phân bổ đều lượng xác suất tại nút cụt kết hợp bước nhảy ngẫu nhiên ở mọi nút. Nhờ đó, điểm số PageRank qua các vòng lặp luôn bảo toàn tính chất của một phân phối xác suất hợp lệ với tổng bằng 1.

**Vết tính một vòng, $\beta=\frac{4}{5}$, $r^0$ đều.**
- *Đồ thị gốc* (không nút cụt, $\delta=0$):
  - A: $\frac45\cdot\frac38+\frac1{20}=\frac7{20}$.
  - B, C, D: $\frac45\cdot\frac5{24}+\frac1{20}=\frac{13}{60}$.
  - Tổng bằng 1.
- *Biến thể nút cụt* ($\delta^0=\frac{1}{4}$): Thành phần chung $\frac{(\frac{1}{5})+(\frac{1}{5})}{4}=\frac1{10}$.
  - A: $\frac45\cdot\frac18+\frac1{10}=\frac15$.
  - B, C, D: $\frac45\cdot\frac5{24}+\frac1{10}=\frac4{15}$.
  - Tổng lại bằng 1, tức điểm của C được hoàn lại đầy đủ qua phần bù.
- *Biến thể `trap` một vòng*, $z_C$ nhận từ A, C và D: $z_C=\frac1{12}+\frac14+\frac18=\frac{11}{24}$, nên $r_C=\frac45\cdot\frac{11}{24}+\frac1{20}=\frac{5}{12}$. A $\frac{3}{20}$, B, D $\frac{13}{60}$. Tổng $\frac{3}{20}+\frac{13}{60}+\frac{5}{12}+\frac{13}{60}=1$.

**Bảo toàn khối lượng.** Nếu $r^t$ không âm, tổng 1 thì $r^{t+1}$ cũng vậy: Nguồn không cụt cộng lại góp $\beta(1-\delta)$, phần bù trả lại $\beta\delta$, bước nhảy góp $1-\beta$. Tổng ba phần bằng 1 và mọi hệ số không âm. Đây là bất biến dùng để kiểm chương trình ở phần 6.

**Hội tụ.** Đặt $S$ là $M_0$ với mỗi cột nút cụt thay bằng $u$. $S\ge 0$ và mỗi cột tổng 1, và phép cập nhật viết được $F(r)=\beta Sr+(1-\beta)u$. Đo khoảng cách bằng $\|x-y\|_1=\sum_i|x_i-y_i|$. Với mọi véc tơ thực $v$:

$$\|Sv\|_1\;\le\;\sum_i\sum_j S_{ij}|v_j|\;=\;\|v\|_1,$$

vì mỗi cột của $S$ có tổng 1. Suy ra $\|F(x)-F(y)\|_1\le\beta\|x-y\|_1$ (phần bước nhảy triệt tiêu trong hiệu), nên với $\Delta_t=\|r^{t+1}-r^t\|_1$ ta có $\Delta_t\le\beta^t\Delta_0$. Với $q>p$: $\|r^q-r^p\|_1\le\sum_{j=p}^{q-1}\Delta_j$ và $\Delta_j \le \frac{\beta^p\Delta_0}{1-\beta} \to 0$, tức dãy lặp là dãy Cauchy. Giới hạn $r^*$ vẫn không âm và có tổng bằng 1 (các điều kiện này được giữ khi lấy giới hạn), $F$ liên tục nên $r^*=F(r^*)$. Hai điểm bất động bất kỳ phải cách nhau $d$ thỏa $d\le\beta d$, tức $d=0$: Nghiệm duy nhất.

::: derivation Khai triển chi tiết: Cận hậu nghiệm (đọc thêm)
Sai số so với nghiệm bị chặn bởi:
$$\|r^{t+1}-r^*\|_1\le\sum_{j=t+1}^{\infty}\Delta_j\le\frac{\beta}{1-\beta}\Delta_t.$$
Lưu ý $\Delta_t=\|r^{t+1}-r^t\|_1$ đo vòng *sau*, còn cận nói về $r^{t+1}$. Và trên máy tính số dấu phẩy động, kết luận đúng cho số thực lý tưởng còn phép so sánh cần dung sai.
:::

**Thuật toán và dừng.** Vào: Danh sách kề, $n\ge1$, $0<\beta<1$, ngưỡng $\tau>0$, giới hạn $T_{\max}$ nguyên dương. Mỗi vòng: Tính $\delta$ từ véc tơ cũ, đặt phần chung cho mọi trang, cộng đóng góp từng cạnh, tính $\Delta_t=\sum_i|r_i^{t+1}-r_i^t|$, thay $r$. Dừng khi $\Delta_t\le\tau$ (trạng thái *đạt ngưỡng*) hoặc hết $T_{\max}$ (trạng thái *chưa đạt*, kèm véc tơ và $\Delta$ cuối). Lưu ý $\tau$ là ngưỡng độ thay đổi giữa hai vòng, không đồng nhất sai số so với nghiệm. Ví dụ với $\Delta_1=\frac{2}{25}=0{,}08$ và $\tau=0{,}1$ thuật toán dừng sau vòng thứ hai. Vòng đầu có $\Delta_0 = \frac{1}{10} + 3\cdot\frac{1}{30} = \frac{1}{5} > 0{,}1$. Mỗi vòng quét $n+m$ phần tử.

---

## 4. Tính PageRank trên đồ thị lớn: Biểu diễn thưa và MapReduce theo khối

**Vấn đề quy mô.** Quy tắc cập nhật không đổi, nhưng với web thật $n$ rất lớn trong khi số liên kết thường nhỏ hơn nhiều so với số cặp trang có thể có: Ma trận đặc cần $n^2$ ô trong khi thông tin thật chỉ là $m$ cạnh. Khi $m\ll n^2$, phần áp đảo của ma trận là 0. Cần hai việc: Biểu diễn thưa và chia việc sao cho mỗi tác vụ chỉ giữ phần dữ liệu vừa bộ nhớ chính (RAM).

**Biểu diễn theo nguồn (MMDS 5.2.1).** Vì giá trị khác không của cột $j$ luôn là $1/d_j$, chỉ cần lưu cho mỗi nguồn: Mã nguồn, bậc ra toàn cục $d_j$, và danh sách đích. Trên đồ thị ví dụ:
- A: $3 \to  B$, C, D.
- B: $2 \to  A$, D.
- C: $1 \to  A$.
- D: $2 \to  B$, C.

Nút cụt vẫn giữ bản ghi với $d_j=0$, danh sách rỗng, điều này rất cần cho pha tính $\delta$. Bậc ra ở đây là **bậc toàn cục**, không phải số đích trong một khối cụ thể. Ghi sai bậc sẽ làm sai mọi đóng góp từ nguồn đó.

**Chia khối (MMDS 5.2.3–5.2.4).** Đặt $z=M_0r$. $V_b$ là tập trang nguồn thuộc dải $b$. Chia $r$ và $z$ thành $k$ dải, $M_0$ thành $k^2$ khối: Khối $M_{ab}$ chứa cạnh từ nguồn dải $b$ tới đích dải $a$. Nếu chỉ chia theo cột, mỗi tác vụ có thể phải cộng vào toàn bộ véc tơ kết quả. Chia thêm theo hàng giới hạn cả miền vào lẫn miền ra. Trên ví dụ với $k=2$ (nguồn A, B | C, D):
- $M_{11}$ ghi $A\to B$, $B\to A$.
- $M_{21}$ ghi $A\to C$, $A\to D$, $B\to D$.
- $M_{12}$ ghi $C\to A$, $D\to B$.
- $M_{22}$ chỉ ghi D→C (C không trỏ tới C hay D).

Bậc toàn cục $d_A=3$ được lặp lại ở cả hai khối có cạnh của A. Mỗi cạnh thuộc đúng một khối theo cặp (nguồn, đích).

![Ma trận chia thành bốn khối theo hai dải nguồn và hai dải đích](img/lec-03/rlarge-blocks-grid.svg)

**Map, Combine, Reduce.** Map nhận khối $B_{ab}$ và dải điểm $r_b$:

```text
Map(B_ab, r_b):
  với mỗi (j, dj, dests) trong B_ab:
    với mỗi i trong dests:
      yield(i, r_b[j] / dj)

Combine(i, values):
  yield(i, sum(values))
```

Khóa là trang đích. Combine cộng các đóng góp cùng khóa ngay tại tác vụ Map, giảm dữ liệu phải chuyển. Reduce hoàn thiện:

```text
Reduce(i, L_i):
  z_i = sum(L_i)
  return(i, beta * z_i + (1 - beta + beta * delta) / n)
```

**Hai chi tiết quan trọng.**
1. $\delta$ tính một lần từ phân hoạch nguồn (mỗi nút cụt góp đúng một lần), rồi gửi tới các tác vụ Reduce, tránh tính lại $\delta$ từ các khối có bản ghi nguồn lặp.
2. Tạo bản ghi $(i,0)$ cho **mọi** trang từ danh sách trang, để đích không có liên kết vào nào vẫn xuất hiện khi nhóm theo khóa và nhận phần chung.

**Ví dụ gộp tại A.** Đồ thị gốc, $r^0$ đều, $\beta=\frac{4}{5}$, $k=2$: Khối $M_{11}$ sinh $(A, \frac{1}{8})$ (cạnh $B\to A$), $M_{12}$ sinh $(A, \frac{1}{4})$ (cạnh $C\to A$). $z_A=\frac{1}{8}+\frac{1}{4}=\frac{3}{8}$. $r_A^1=\frac45\cdot\frac38+\frac1{20}=\frac7{20}$, hoàn toàn trùng khớp với phép tính một máy của phần 3.

**Tính đúng.** Mọi tác vụ dùng cùng bản chụp cố định của $r$ trong suốt một vòng (véc tơ không đổi khi đang được đọc), nên:

$$\sum_{b=1}^{k}\ \sum_{j\in V_b:\ j\to i}\frac{r_j}{d_j}=\sum_{j:\ j\to i}\frac{r_j}{d_j}.$$

Mỗi cạnh đóng góp đúng một lần vì nó thuộc đúng một khối. Combine và Reduce chỉ tái nhóm các tổng. Trên số thực chính xác kết quả bằng phép cập nhật tuần tự. Trên số dấu phẩy động, thứ tự cộng khác nhau gây chênh làm tròn nhỏ — không khẳng định tính kết hợp tuyệt đối của số thực máy.

**Tổ chức một vòng.** Các pha: Dùng $r$ cố định → Map song song trên $k^2$ khối (pha $\delta$ có thể chạy song song nhưng phải xong trước Reduce) → Combine tại chỗ → truyền và nhóm theo khóa → Reduce → tổng hợp $\Delta$ để quyết định dừng. Lưu ý $k^2$ là số *tác vụ*, không phải số máy. Với $k=2$, bốn tác vụ có thể chạy trên hai máy. Biến thể gộp cả một hàng khối vào một tác vụ (Map đọc cả $v$, Reduce chỉ nối kết quả) nằm ở MMDS 5.2.5 để đọc thêm.

---

## 5. Chi phí: Lưu trữ, bộ nhớ, dữ liệu và thời gian

Phần này đánh giá cách tổ chức tính theo khối bằng các đại lượng riêng biệt của mô hình chi phí đầu vào tác vụ trong MMDS 2.5.1. Trong đó, $I$ là tổng byte đầu vào các tác vụ Map, $H$ là tổng byte đầu vào các tác vụ Reduce và $C=I+H$ cho một công việc có Combine nằm trong Map. Các số byte dưới đây được tính theo quy ước định dạng của mô hình, không phải kích thước đối tượng Python hay số đo thực nghiệm. Tham số gồm $n$ trang, $m$ liên kết, $k$ dải mỗi chiều và $p$ máy.

**Dung lượng lưu đĩa $S$.** Quy ước: Giá trị điểm 8 byte (double), mã trang hoặc bậc ra 4 byte (số nguyên 32 bit).
- Ma trận đặc: $S_{\text{dense}}=8n^2$ byte.
- Danh sách liên kết (mã nguồn ngầm): $S_{\text{adj}}\approx 4(n+m)$, gồm $n$ bậc ra cộng $m$ mã đích. Mô hình bỏ qua phần phụ trội của định dạng và lưu trữ.
- Với $n=4$, $m=8$: 128 và 48 byte. Tỷ số xấp xỉ $2n^2/(n+m)$, có lợi khi $m\ll n^2$.
- Con số 48 byte là của biểu diễn toàn cục. Biểu diễn theo khối lặp lại bậc ra và mã nguồn ở nhiều khối, nên không gán nó cho $S_{\text{blocks}}$.

**Bộ nhớ một tác vụ $B$.** Tác vụ khối đọc ma trận tuần tự qua bộ đệm. Nó giữ hai dải véc tơ (dải vào $r_b$ và dải tích lũy $z_a$), mỗi dải $n/k$ giá trị 8 byte (giả sử $k$ chia hết $n$):

$$B_{\text{task}}\approx \frac{16n}{k}+B_{\text{buf}}.$$

Với $n=4$, $k=2$: Bộ nhớ cần $2\cdot2\cdot8=32$ byte cộng bộ đệm đọc khối $B_{\text{buf}}$. Việc tăng $k$ giúp giảm bộ nhớ mỗi tác vụ nhưng làm tăng số lần mỗi dải được đọc (mỗi dải phục vụ $k$ tác vụ), đây là sự đánh đổi xuất hiện lại ở phần đầu vào.

**Đầu vào Map $I$.** $I=S_{\text{blocks}}+8kn$: Phần ma trận mỗi khối đọc một lần. Phần véc tơ, mỗi dải $r_b$ được gửi tới $k$ tác vụ cùng cột nên toàn véc tơ được đọc $k$ lần, mỗi lần $8n$ byte. Với ví dụ $n=4$, $m=8$, $k=2$: Bảy bản ghi nguồn (phân bổ 2, 2, 2, 1 trên bốn khối. Định dạng nguồn 4 byte + bậc 4 byte + mỗi đích 4 byte) cho $S_{\text{blocks}}=8\cdot7+4\cdot8=88$ byte. Véc tơ $8\cdot2\cdot4=64$ byte. $I=152$ byte. $I$ chưa gồm các pha $\delta$, kiểm tra $\Delta$ và điều phối. Đồ thị ví dụ không có nút cụt và mọi đích có liên kết vào, nên không cần bản ghi seed hay $\delta$ trong bài tính cốt này.

**Combine và $H$:** Khi không dùng Combine: Có $m=8$ bản ghi (khóa 4 + giá trị 8 = 12 byte) → $H=96$ byte. Khi có Combine: Có $q=7$ bản ghi khóa (chỉ khối $M_{21}$ gộp hai đóng góp vào D thành một) → $H=84$ byte. Do đó $C=I+H$ giảm từ $248$ xuống $236$ byte. Mức giảm 12 byte tương ứng 12,5% của $H$, chứ không phải 12,5% toàn bộ thời gian chạy. Đây chỉ là phép nhân theo khối trong một vòng, chưa phải tổng chi phí cả luồng công việc.

**Phân biệt $C$ với $Q$.** $Q$ là số byte **thực sự đi qua mạng**. Nó chỉ bằng $H$ nếu mọi bản ghi ra Map đều qua mạng, không nén, không chạy lại, không phần phụ trội. Dữ liệu khối thường nằm cục bộ, nên $I=Q$ không suy ra được từ dữ kiện. Nếu toàn bộ 7 bản ghi sau Combine qua mạng: Lượng dữ liệu $Q=84$ byte và $T_{\text{shuffle}}\ge Q/b_{\text{eff}}$ với $b_{\text{eff}}$ là băng thông hiệu quả tổng hợp (byte/giây).

**Thời gian.** Mô hình: Mỗi cạnh tốn $c_e$ giây, bỏ I/O, truyền và lập lịch trong pha tính. Tổng việc $W=m\cdot c_e=8c_e$ không đổi theo số máy. Thời gian xử lý các khối tương ứng là:
- $M_{11}$ tốn $2c_e$,
- $M_{21}$ tốn $3c_e$,
- $M_{12}$ tốn $2c_e$,
- $M_{22}$ tốn $1c_e$.

Một máy tuần tự: $8c_e$. Bốn máy, mỗi máy một tác vụ: $T_{\text{map}}=3c_e$ (tác vụ nặng nhất là nút cổ chai), tăng tốc $\frac{8}{3}$, chứ không phải 4. Gọi $w_{\max}$ là thời gian của tác vụ nặng nhất. Khi tác vụ không bị chia nhỏ thêm: $T_{\text{map}}\ge\max(W/p,\ w_{\max})$.

**Một vòng và cả công việc.** Giả định các pha không chồng nhau:

$$T_{\text{round}}\approx T_\delta+T_{\text{map}}+T_{\text{shuffle}}+T_{\text{reduce}}+T_{\text{sync}}.$$

$T_\delta$ đo pha tính tổng điểm nút cụt. $T_{\text{shuffle}}$ đo pha truyền và nhóm. $T_{\text{reduce}}$ đo pha gộp kết quả. $T_{\text{sync}}$ đo pha kiểm tra dừng và đồng bộ.

Với $L$ vòng: $T_{\text{job}}=T_{\text{setup}}+\sum_{t=1}^{L}T_{\text{round},t}$. Nếu pha $\delta$ chạy đồng thời Map, dùng max của hai thời gian thay vì tổng. $L$ phụ thuộc tiêu chí dừng ($\tau$, $T_{\max}$), không mặc định cố định. Lưu ý phân biệt: Quét $n+m$ phần tử *một vòng trên một máy* là mô hình phép toán. $c_e$ giây mỗi cạnh và $W=mc_e$ là mô hình thời gian theo tác vụ — hai cách đếm khác phạm vi và đơn vị, không cộng lẫn.

---

## 6. Thực hành: Chạy mã `pagerank.py`

Tệp mã [pagerank.py](/materials/lec-03/code/pagerank.py) (đi kèm [hướng dẫn chạy](/materials/lec-03/code/practice-README.md)) cài đặt đúng mô hình phần 3 bằng Python 3, chỉ dùng thư viện chuẩn (`argparse`, `json`, `math`, `sys`) — không cần pip. Mục đích là **kiểm chứng công thức trên một máy**, không phải đo hiệu năng hay chứng minh tăng tốc. Không dùng đồ thị bốn nút để suy kết luận về song song hóa.

**Biểu diễn dữ liệu và giao diện.** Đồ thị là dict từ tên nút sang danh sách đích:

```python
adj = {
    "A": ["B", "C", "D"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B", "C"],
}
```

Hàm `pagerank(adj, beta=0.8, tol=1e-8, max_iter=100)` trả về dict gồm `rank` (điểm từng nút), `converged` (trạng thái đạt ngưỡng), `iterations` (số vòng), `delta` (độ thay đổi cuối). Điều kiện vào: $n\ge 1$. Mọi đích là khóa của dict. Cạnh trùng được gộp trong bản sao (hàm không sửa dữ liệu vào). $0<\beta<1$. `tol` dương. `max_iter` nguyên dương. Toàn bộ nút được giữ, kể cả nút không có liên kết vào hay nút cụt — nút cụt phải có mặt để tính phần bù.

**Mã một vòng.** Hàm `step` dịch trực tiếp quy tắc cập nhật:

```python
def step(adj, r, beta):
    n = len(adj)
    delta = sum(r[j] for j in adj if not adj[j])
    common = (1.0 - beta + beta * delta) / n
    new = {i: common for i in adj}
    for j, targets in adj.items():
        if not targets:
            continue
        share = beta * r[j] / len(targets)
        for i in targets:
            new[i] += share
    return new
```

`delta` ở đây là $\delta^t$ (tổng điểm nút cụt, tính từ véc tơ cũ). `common` là phần chung $((1-\beta)+\beta\delta)/n$, cấp sẵn cho mọi nút nên đích không có liên kết vào vẫn nhận điểm. Nút cụt bỏ qua vòng chia vì điểm của nó đã vào phần bù. Vector `r` chỉ được đọc. Điểm mới nằm hoàn toàn trong dict trả về. Lưu ý hai đại lượng cùng họ tên trong tệp: `delta` trong `step` là $\delta$, còn `delta` trong vòng lặp là $\Delta=\sum_i|r_i^{t+1}-r_i^t|$ — hai phạm vi khác nhau.

**Vòng lặp và dừng.** Khởi tạo $r^0$ đều $1/n$. Mỗi vòng gọi `step`, tính $\Delta$, thay `r`, dừng khi $\Delta\le\tau$. Nếu hết `max_iter` chưa đạt ngưỡng, kết quả kèm trạng thái chưa đạt, số vòng và $\Delta$ cuối.

**Lệnh chạy.** Từ thư mục gốc dự án:

```bash
python materials/lec-03/code/pagerank.py --variant base --beta 0.8 --tol 1e-8 --max-iter 100
```

Đổi `--variant` thành `dead` hoặc `trap` cho hai biến thể. Đầu ra là JSON: `rank`, `converged`, `iterations`, `delta`, `rank_sum`.

**Kết quả chạy với các tham số trên.**
- Với `base`, `beta=0.8`, `tol=1e-8`: Đạt ngưỡng sau 20 vòng, $r_A\approx0{,}321429$, $r_B=r_C=r_D\approx0{,}226190$ (nghiệm chính xác lần lượt là $\frac{9}{28}$ và $\frac{19}{84}$), $\Delta$ cuối $\approx 5{,}50\times10^{-9}$, tổng điểm 1.0.
- Với `dead`: 12 vòng.
- Với `trap`: 34 vòng, C chiếm $\approx0{,}642$.

Sai khác làm tròn nhỏ có thể xuất hiện giữa môi trường chạy. Số vòng không phải hằng số để học thuộc — nó phụ thuộc $\tau$ và $\beta$.

**Ba lớp kiểm chứng.**
1. **Bất biến:** tổng điểm xấp xỉ 1, mọi giá trị không âm.
2. **Một bước tính tay:** `base` từ $r^0$ đều, $\beta=0{,}8$ cho $r_A=\frac{7}{20}$, $r_B=r_C=r_D=\frac{13}{60}$. `dead` cho $\frac{1}{5}$ và $\frac{4}{15}$ — khớp bảng phần 3.
3. **Trường hợp biên trong README:** toàn bộ nút cụt ($\delta=1$, mỗi vòng trả lại phân phối đều, không lỗi chia không) và nút có khuyên lên chính nó. So sánh số thực dùng dung sai `abs(got - want) <= 1e-12`, không dùng `==`.

**Các lỗi cần kiểm tra khi cài đặt.** Cập nhật trực tiếp `r[i] += ...` khi quét cạnh làm trộn điểm cũ và điểm mới. Bỏ nút không có liên kết vào trước khi chạy làm mất nút khỏi kết quả. Dùng `==` so sánh float. Ba lỗi này đều trái với bất biến và quy tắc đồng bộ đã nêu.

---

## 7. Bài tập tự luyện

Bốn bài sau giữ nguyên đề và đồ thị của MMDS. Làm trước khi xem gợi ý.

### Bài 1 — MMDS 5.1.1 (trang 187–188, Hình 5.7): PageRank không bước nhảy

::: exercise
Tính PageRank của từng trang trong Hình 5.7, không có bước nhảy.
:::

Đồ thị Hình 5.7: $a\to a, b, c$. $b\to a, c$. $c\to b, c$ — bảy cạnh, có khuyên ở $a$ và $c$.

![Hình 5.7: Trang a trỏ tới a, b, c. Trang b trỏ tới a, c. Trang c trỏ tới b, c. Đồ thị có bảy cạnh, trong đó có hai khuyên](img/lec-03/ex-fig-57.svg)

::: hint
Đặt $a, b, c$ cũng là điểm của ba trang. Viết ma trận theo cột nguồn, lập hệ cân bằng $r=Mr$ kèm điều kiện chuẩn hóa, rồi giải bằng khử tuyến tính.
:::

::: solution
Cột nguồn: Cột $a$ là $(\frac{1}{3},\frac{1}{3},\frac{1}{3})$, cột $b$ là $(\frac{1}{2},0,\frac{1}{2})$, cột $c$ là $(0,\frac{1}{2},\frac{1}{2})$. Hệ cân bằng:

$$a=\frac a3+\frac b2,\qquad b=\frac a3+\frac c2,\qquad c=\frac a3+\frac b2+\frac c2,\qquad a+b+c=1.$$

Từ phương trình đầu: $a-\frac b2=\frac a3\Rightarrow b=\frac{4a}3$.

Thế vào phương trình hai: $b=\frac a3+\frac c2$, suy ra $c=2b-\frac{2a}3=2a$.

Tổng: $a+\frac{4a}3+2a=\frac{13a}3=1$, nên:

$$a=\frac3{13},\quad b=\frac4{13},\quad c=\frac6{13}.$$

Kiểm phương trình ba: $\frac1{13}+\frac2{13}+\frac3{13}=\frac6{13}$. Hai phương trình đầu thỏa trực tiếp. Tổng ba điểm bằng 1.
:::

### Bài 2 — MMDS 5.1.2: Thêm bước nhảy với hệ số 0,8

::: exercise
Tính PageRank của từng trang trong Hình 5.7 với $\beta=0{,}8$.
:::

::: hint
Đồ thị không có nút cụt nên $\delta=0$ và phần chung là $(1-\beta)/3=\frac{1}{15}$. Cần giải $r=\frac45M_0r+\frac1{15}\mathbf 1$ với $a+b+c=1$. Thay $c=1-a-b$ để còn hai ẩn.
:::

::: solution
Hai phương trình đầu (nhân 15):

$$15a=4a+6b+1\ \Rightarrow\ 11a-6b=1;\qquad 15b=4a+6c+1.$$

Thay $c=1-a-b$: $$
15b = 4a + 6 - 6a - 6b + 1 \implies 2a + 21b = 7
$$. Nhân phương trình đầu với 7, phương trình sau với 2 rồi cộng: $77a+4a=7+14\Rightarrow 81a=21$, nên:

$$a=\frac7{27}=\frac{21}{81}.$$

Tiếp tục: $b=\frac{11a-1}{6}=\frac{\frac{231}{81}-1}{6}=\frac{25}{81}$. $c=1-a-b=\frac{35}{81}$.

Kiểm phương trình của $c$:
$$\frac45\left(\frac7{81}+\frac{25}{162}+\frac{35}{162}\right)+\frac1{15}=\frac45\cdot\frac{74}{162}+\frac1{15}=\frac{148}{405}+\frac{27}{405}=\frac{35}{81}.$$
Tổng: $\frac{21+25+35}{81}=1$.

So sánh hai bài: Bước nhảy san phẳng điểm, kéo $c$ từ $\frac{6}{13}\approx0{,}462$ xuống $\frac{35}{81}\approx0{,}432$ và nâng $a$ lên.
:::

### Bài 3 — MMDS 5.2.1 (trang 195): Ngưỡng lưu ma trận thưa

::: exercise
Ma trận Boolean $n\times n$ có thể lưu đặc bằng từng bit, hoặc thưa bằng liệt kê tọa độ các ô 1 — mỗi tọa độ là một cặp số nguyên, mỗi số $\lceil\log_2 n\rceil$ bit. Ma trận phải thưa đến mức nào (tỷ lệ ô 1) để cách liệt kê tiết kiệm chỗ hơn?
:::

::: hint
Gọi $m$ là số ô 1. Viết dung lượng hai cách theo bit, lập bất đẳng thức, chú ý điểm bằng nhau chưa phải là tiết kiệm.
:::

::: solution
Cách đặc: $n^2$ bit.

Cách thưa: $m$ ô 1, mỗi ô cần hai số nguyên, mỗi số $\lceil\log_2 n\rceil$ bit, tổng $2m\lceil\log_2 n\rceil$ bit.

Điều kiện tiết kiệm:

$$2m\lceil\log_2 n\rceil < n^2\quad\Longleftrightarrow\quad \rho=\frac m{n^2}<\frac{1}{2\lceil\log_2 n\rceil}.$$

Tại điểm bằng nhau hai cách tốn như nhau nên điều kiện phải là bất đẳng thức ngặt. Với $n=1$, $\lceil\log_2 n\rceil=0$ và mô hình tọa độ suy biến. So sánh chỉ có nghĩa từ $n\ge2$. Kết luận là điều kiện theo $n$, không cần dữ liệu cụ thể khác.
:::

### Bài 4: Biểu diễn đồ thị theo danh sách kề (Bài tập 5.2.2)

::: exercise
Dùng phương pháp mục 5.2.1, lập bảng (Nguồn, Bậc ra, Danh sách đích) cho: (a) Đồ thị Hình 5.4. (b) Đồ thị Hình 5.7.
:::

![Đồ thị Hình 5.4: A tới B, C, D. Trang B tới A, D. Trang C tới E. Trang D tới B, C, còn E không có cạnh ra](img/lec-03/ex-fig-54.svg)

Hình 5.7 đã cho ở Bài 1.

::: hint
Mỗi nguồn ghi bậc ra toàn cục rồi toàn bộ danh sách đích. Nguồn không có liên kết ra vẫn được liệt kê với bậc 0. Khuyên cũng là một cạnh và tính vào bậc ra.
:::

::: solution
**Hình 5.4** (A→B, C, D. B→A, D. C→E. D→B, C. E không có liên kết ra, đồ thị gồm 8 cạnh):

| Nguồn | Bậc ra | Đích |
|---|---|---|
| A | 3 | B, C, D |
| B | 2 | A, D |
| C | 1 | E |
| D | 2 | B, C |
| E | 0 | (rỗng) |

**Hình 5.7** (a→a, b, c. B→a, c. C→b, c, đồ thị gồm 7 cạnh tính cả 2 khuyên):

| Nguồn | Bậc ra | Đích |
|---|---|---|
| a | 3 | a, b, c |
| b | 2 | a, c |
| c | 2 | b, c |

Bài này chỉ yêu cầu biểu diễn, không yêu cầu tính PageRank. Tổng bậc ra là 8 và 7, khớp số cạnh hai hình. Lưu ý Hình 5.7 có 5 cạnh giữa các nút khác nhau cộng 2 khuyên, tổng 7 cạnh, cần lưu ý không đếm khuyên hai lần.
:::

---

## 8. Hướng dẫn chấm bài tập

| Bài | Tiêu chí đánh giá | Điểm |
|---|---|---|
| **Bài 1** | Ma trận liên kết $M$ đúng dạng theo cột nguồn | 3 |
| | Hệ phương trình cân bằng và điều kiện chuẩn hóa tổng | 3 |
| | Khử tuyến tính và tính ra các giá trị $a, b, c$ | 2 |
| | Kiểm nghiệm lại phương trình và điều kiện tổng 1 | 2 |
| **Bài 2** | Mô hình có bước nhảy và xác định đúng phần bù chung $\frac{1}{15}$ | 3 |
| | Lập và giải hệ phương trình tuyến tính | 4 |
| | Kiểm nghiệm và kết luận độ san phẳng điểm số | 3 |
| **Bài 3** | Viết đúng biểu thức dung lượng cho 2 cách lưu trữ | 4 |
| | Thiết lập bất đẳng thức và suy ra ngưỡng mật độ $\rho$ | 4 |
| | Phân tích điều kiện ngặt và trường hợp biên $n \ge 2$ | 2 |
| **Bài 4** | Lập đúng bảng cho Hình 5.4 (kèm nút cụt $E$) | 4 |
| | Lập đúng bảng cho Hình 5.7 (đếm đúng 2 khuyên) | 4 |
| | Ghi rõ nguồn hình và đối chiếu tổng bậc ra | 2 |
| **Tổng điểm** | | **10** |

---

## 9. Đọc thêm và tài liệu tham khảo

- J. Leskovec, A. Rajaraman, J. D. Ullman, *Mining of Massive Datasets*, 3rd ed., Cambridge University Press. Chương 5 (Link Analysis), mục 5.1.2–5.1.7 trang 178–188, mục 5.2 trang 189–195. Chương 2, mục 2.5.1 trang 53–54 cho mô hình chi phí. Xem thêm tại [MMDS](http://www.mmds.org).
- [Slide MMDS](http://www.mmds.org/), tệp `ch05-linkanalysis1.pdf`, trang chiếu 42 và 52. [Stanford CS246](https://web.stanford.edu/class/cs246/), tệp `09-pagerank.pdf`, trang chiếu 45 và 54: Phân phối điểm nút cụt, nguồn của phần bù $\beta\delta$.
- Tệp mã thực hành: [materials/lec-03/code/pagerank.py](/materials/lec-03/code/pagerank.py) và [materials/lec-03/code/practice-README.md](/materials/lec-03/code/practice-README.md).

[Quay về bộ trang chiếu](#slides).
