---
course: toan-cho-ai
lecture: bai-07-quy-hoach-tuyen-tinh-va-dong
section: lecture
title: "Quy hoạch tuyến tính và quy hoạch động"
prerequisites: ["ma-tran", "he-phuong-trinh", "tap-loi", "do-thi"]
lessonStatus: ready
description: "Từ đa diện và nghiệm cơ sở đến Bellman hữu hạn tất định; so hai cách giải một bài đường đi."
---

Quy hoạch tuyến tính mô tả một quyết định bằng hàm mục tiêu tuyến tính và các ràng buộc tuyến tính. Quy hoạch động lại tổ chức một chuỗi quyết định bằng cách lưu kết quả tốt nhất của phần bài toán còn lại. Hai phương pháp có ngôn ngữ khác nhau, nhưng trong một số bài toán, chẳng hạn tìm đường đi trên đồ thị có hướng không chu trình, chúng có thể mô tả và chứng nhận cùng một nghiệm.

Sau khi học xong, bạn sẽ đưa được một LP về dạng chuẩn, xác minh được một nghiệm cơ sở có khả thi hay không, tính được các giá trị Bellman theo thứ tự ngược và thu hồi được đường đi tối ưu. Mục 1–3 trình bày quy hoạch tuyến tính. Mục 4–6 trình bày quy hoạch động và mối liên hệ với LP. Các dữ liệu số dưới đây đều do người biên soạn tự đặt.

## 1. Một ví dụ quy hoạch tuyến tính hai biến

Xét

$$\max_{x,y}3x+2y,\qquad x+y\le4,\quad x\le2,\quad x,y\ge0.$$

Mục tiêu tuyến tính. Miền là giao các nửa không gian nên là đa diện. Các đỉnh là $(0,0)$, $(2,0)$, $(2,2)$, $(0,4)$. Giá trị mục tiêu lần lượt là $0,6,10,8$. Nghiệm tối ưu $(2,2)$, giá trị 10.

<MathLab type="lp">

```js
const values = vertices.map(([x,y]) => c1*x+c2*y);
const best = Math.max(...values);
```

</MathLab>

Mô phỏng cơ chế hình học LP ở §4.3 của sách với miền tự đặt. Đổi trọng số về $c_1=c_2=1$: mọi điểm trên cạnh $x+y=4$, $0\le x\le2$, đều tối ưu. Có một đỉnh tối ưu không có nghĩa tất cả nghiệm tối ưu đều là đỉnh hoặc nghiệm duy nhất.

### 1.1 Điểm cực và điều kiện tồn tại đỉnh tối ưu

Một **điểm cực** của tập lồi không thể viết thành tổ hợp lồi thật sự của hai điểm khác nhau trong tập. “Thật sự” nghĩa là cả hai trọng số dương. Với đa diện, điểm cực tương đương đỉnh và tương đương đủ ràng buộc độc lập hoạt động tại điểm.

Nếu đa diện khác rỗng có điểm cực và LP có giá trị tối ưu hữu hạn, tồn tại một điểm cực tối ưu. Không bỏ điều kiện có điểm cực: đường thẳng $\{(x,y):y=0\}$ không có điểm cực, nhưng cực tiểu $y$ trên đó có giá trị 0 và mọi điểm đều tối ưu. Trên đa diện compact khác rỗng, một mục tiêu tuyến tính luôn đạt tối ưu và có thể chọn nghiệm ở điểm cực.

## 2. Dạng chuẩn và biến slack

Dạng chuẩn thường dùng trong đại số LP là

$$\min c^Tx,\qquad Ax=b,\quad x\succeq0.$$

Để đổi $a^Tx\le b$ thành đẳng thức, thêm **biến slack** $s\ge0$: $a^Tx+s=b$. Nếu một biến $u$ không bị giới hạn dấu, viết $u=u^+-u^-$, $u^+,u^-\ge0$. Đổi max thành min bằng cách đổi dấu mục tiêu.

LP ở mục 1 trở thành

$$\min(-3x-2y),\quad
x+y+s_1=4,\quad x+s_2=2,\quad x,y,s_1,s_2\ge0.$$

Slack đo phần chưa dùng của mỗi giới hạn. Nó khác nhân tử Lagrange. Tại $(2,2)$, hai slack đều 0.

## 3. Nghiệm cơ sở trong dạng chuẩn

Giả sử $A$ kích thước $m\times n$ có hạng hàng $m$. Chọn $m$ cột độc lập tạo ma trận vuông $A_B$. Đặt các biến ngoài tập cột $B$ bằng 0 và giải $A_Bx_B=b$. Đây là **nghiệm cơ sở**. Nếu $x_B\ge0$, nó là **nghiệm cơ sở khả thi**.

Với ví dụ,

$$A=\begin{bmatrix}1&1&1&0\\1&0&0&1\end{bmatrix},\quad b=(4,2)^T.$$

Chọn cột $x,y$ làm cơ sở: $A_B=\begin{bmatrix}1&1\\1&0\end{bmatrix}$. Đặt $s_1=s_2=0$, giải được $x=2$, $y=2$, cả hai không âm. Chọn cột $s_1,s_2$ thì $x=y=0$, slack $(4,2)$, cũng khả thi nhưng mục tiêu kém hơn.

Không phải bất kỳ $m$ cột nào cũng tạo được một cơ sở: hai cột ứng với $y$ và $s_1$ giống nhau nên phụ thuộc tuyến tính. Một nghiệm cơ sở cũng chưa chắc khả thi. Sau khi giải hệ, vẫn phải xác nhận mọi thành phần đều không âm. Nếu một biến cơ sở bằng 0, ta có **nghiệm cơ sở suy biến**. Vì vậy, việc một biến thuộc cơ sở không có nghĩa giá trị của nó phải dương.

### 3.1 Chứng nhận tối ưu bằng tổ hợp các ràng buộc

Với bài max ở mục 1, chọn nhân tử không âm $(\lambda_1,\lambda_2)=(2,1)$ cho hai giới hạn. Cộng các ràng buộc có trọng số:

$$2(x+y)+x\le2\cdot4+1\cdot2=10.$$

Vế trái đúng bằng $3x+2y$. Do đó mọi điểm khả thi đều có giá trị mục tiêu không vượt quá 10, trong khi điểm $(2,2)$ đạt đúng 10. Đây là một chứng nhận đối ngẫu được tạo từ tổ hợp của các ràng buộc, nối trực tiếp với Bài 03. Chứng nhận này đủ để kết luận tối ưu mà không cần xét từng điểm trong đa diện.

<details><summary>Thử trả lời: Mọi biến cơ sở đều phải dương, đúng hay sai?</summary>

Sai. Điều kiện khả thi chỉ đòi không âm. Chẳng hạn hệ $x+s=0$, $x,s\ge0$, chọn cột $x$ cho biến cơ sở $x=0$.

</details>

## 4. Phương trình Bellman và trạng thái

Xét chuỗi hữu hạn $t=0,\ldots,T-1$. Ở bước $t$, trạng thái $s$, chọn hành động $a\in\mathcal A_t(s)$, chịu chi phí $c_t(s,a)$ và chuyển tất định tới $T_t(s,a)$. Cuối chuỗi chịu chi phí $h(s_T)$.

**Hàm giá trị Bellman** $V_t(s)$ là chi phí nhỏ nhất từ trạng thái đó đến cuối. Công thức **Bellman**:

$$V_T(s)=h(s),\qquad
V_t(s)=\min_{a\in\mathcal A_t(s)}\left[c_t(s,a)+V_{t+1}(T_t(s,a))\right].$$

Ta tách hành động đầu khỏi phần còn lại. Nếu phần sau của một phương án tối ưu chưa tối ưu cho trạng thái đã tới, thay nó bằng phần sau tốt hơn sẽ giảm tổng chi phí, mâu thuẫn. Lập luận này dùng việc trạng thái chứa đủ thông tin quyết định tương lai. Nếu còn ngân sách mà ta chỉ lưu vị trí, trạng thái chưa đủ.

Trong bài này các tập hành động hữu hạn, chuyển trạng thái tất định, thời hạn hữu hạn, nên có thể dùng min và lưu hành động đạt min khi tồn tại hành động khả thi. Trạng thái không có phương án tới đích được gán giá trị $+\infty$. Bài ngẫu nhiên sẽ có kỳ vọng của giá trị tương lai. Ta chưa dùng công thức ấy ở đây.

## 5. Tính các giá trị Bellman trên một DAG

Đồ thị có hướng không chu trình (DAG) tự cung cấp thứ tự tính ngược: đích trước, rồi các nút có mọi nút kế tiếp đã được tính. Xét các cạnh:

| Cạnh | Chi phí |
| --- | ---: |
| $S\to A$ | 1 |
| $S\to B$ | 4 |
| $A\to B$ | 2 |
| $A\to T$ | 5 |
| $B\to T$ | 1 |

<MathLab type="bellman">

```js
// Các nút kế tiếp đã được tính; đích T có V(T)=0.
V[node] = Math.min(...edges[node].map(([to,c]) => c+V[to]));
```

</MathLab>

Ta tính:

1. $V(T)=0$.
2. $V(B)=1+V(T)=1$, chọn $T$.
3. $V(A)=\min\{2+1,5+0\}=3$, chọn $B$.
4. $V(S)=\min\{1+3,4+1\}=4$, chọn $A$.

Theo các lựa chọn đã lưu, đường tối ưu là $S\to A\to B\to T$, chi phí 4. Chỉ lưu giá trị 4 mà không lưu lựa chọn chưa đủ để thu hồi đường đi.

Nếu đổi min thành max, ta tính đường dài nhất trên DAG: $V(B)=1$, $V(A)=5$, $V(S)=6$. §8.7 của *Convex Optimization* dùng cơ chế max này để tính trễ đường lớn nhất trong bài bố trí. Mô phỏng chọn “max” để tái hiện đệ quy ấy với chi phí cạnh tự đặt. Không dùng đệ quy ngược này trực tiếp trên một đồ thị có chu trình.

## 6. Biểu diễn bài toán đường đi bằng quy hoạch tuyến tính

Đặt biến tiềm năng $v_u$ cho mỗi nút, $v_T=0$, và ràng buộc

$$v_u\le c_{uv}+v_v\quad\text{cho mọi cạnh }u\to v.$$

Dọc một đường từ $S$ tới $T$, cộng các bất đẳng thức làm các tiềm năng giữa đường triệt tiêu, cho $v_S\le$ chi phí đường đó. Vì vậy **cực đại $v_S$** cho một cận dưới tốt nhất của đường ngắn nhất.

Các giá trị Bellman $(v_S,v_A,v_B,v_T)=(4,3,1,0)$ thỏa tất cả ràng buộc và chạm chi phí đường đã tìm. LP này có mục tiêu affine và ràng buộc affine. Nó chứng nhận cùng kết quả theo ngôn ngữ cận.

Một cách khác dùng biến luồng trên từng cạnh, giữ cân bằng luồng ở các nút và cực tiểu tổng chi phí. Trong ví dụ DAG, chuyển một đơn vị luồng theo đường tối ưu cho nghiệm nguyên. Với các LP khác, không suy rằng biến nghiệm tự nguyên chỉ vì dữ liệu nguyên.

## Bài tập tự luyện

::: exercise 1. Một cơ sở khác
Trong LP chuẩn ở mục 2, chọn cột $y,s_2$ làm cơ sở. Tính nghiệm và mục tiêu max ban đầu.
:::
::: solution
Đặt $x=s_1=0$. Đẳng thức đầu cho $y=4$, đẳng thức sau cho $s_2=2$. Nghiệm khả thi, mục tiêu $3(0)+2(4)=8$, tương ứng đỉnh $(0,4)$.
:::

::: exercise 2. Đổi một cạnh
Đổi chi phí $S\to B$ từ 4 thành 2, giữ các cạnh khác. Những giá trị nào cần đổi?
:::
::: solution
$V(T),V(B),V(A)$ không đổi vì đường đi phía sau chúng không dùng cạnh ấy. $V(S)=\min\{1+3,2+1\}=3$, chọn $B$. Đường mới $S\to B\to T$. Ta chỉ tính lại phần phụ thuộc cạnh đổi.
:::

::: exercise 3. Trạng thái thiếu thông tin
Một bài đi đường có giới hạn nhiên liệu. Lưu trạng thái chỉ là tên nút có đủ không?
:::
::: solution
Không nếu các hành động tới đây phụ thuộc lượng nhiên liệu còn lại. Hai lần ở cùng nút nhưng nhiên liệu khác nhau có tập hành động khác nhau. Cần thêm nhiên liệu vào trạng thái, chẳng hạn $(u,q)$. Công thức Bellman phải dùng trạng thái đầy đủ ấy.
:::

## Tóm tắt

LP dùng hình học đa diện và hệ tuyến tính để mô tả nghiệm. Quy hoạch động dùng cấu trúc của phần còn lại để tránh liệt kê toàn bộ chuỗi. Trên DAG, tính ngược tạo các giá trị có thể dùng làm tiềm năng LP, nên hai cách nhìn cùng chứng nhận được một đường tối ưu.

## Nguồn và đọc thêm

- Nguồn chính: *Convex Optimization*, §4.3 (LP, tr. 146–152), §8.7, mục Minimax delay placement (tr. 436–438), đặc biệt đệ quy (8.30). Ta trình bày min đường ngắn nhất như một biến thể tự biên soạn của cùng lập luận phần còn lại và chọn max trong mô phỏng để thấy cơ chế gốc.
- Tham khảo local: Bertsimas & Tsitsiklis, *Introduction to Linear Optimization*, chương 2, §2.2–2.6 về điểm cực, nghiệm cơ sở và tồn tại đỉnh tối ưu. Số trang scan được đối chiếu khi đọc. Không đoán công thức từ OCR lỗi.
- Miền LP, cạnh DAG, bảng số và bài tập là dữ liệu tự đặt, không sao chép bài tập trên trang chỉ mục môn.

[Bài 06](./bai-06-phuong-phap-thich-nghi.md) · [Lộ trình ôn lại](../notes/lo-trinh.md).
