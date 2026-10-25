### Bài tập cầu nối: Sóng trên dây quay

Một dây đồng nhất dài $L$, khối lượng $m$, được giữ ở một đầu và quay trong mặt phẳng ngang với tốc độ góc $\omega$. Bỏ qua trọng lực tác dụng lên dây.

(a) Tại điểm cách đầu được giữ một khoảng $r$, lực căng $F$ bằng bao nhiêu?

(b) Tốc độ truyền sóng ngang tại điểm ấy bằng bao nhiêu?

(c) Tìm thời gian để một sóng ngang truyền từ đầu này tới đầu kia của dây.

#### Các bước hướng dẫn

1. Phác tình huống và ghi các khoảng cách $r$, $L$. Vì sao lực căng khác nhau theo $r$? Dự đoán nơi lực căng lớn nhất và nhỏ nhất.
2. Dự đoán nơi tốc độ sóng lớn nhất và nhỏ nhất trên dây.
3. Xét phần dây ở phía ngoài điểm cách đầu được giữ một khoảng $r$. Những lực nào tác dụng lên phần ấy khi bỏ qua trọng lực? Khối lượng của nó bằng bao nhiêu? Khối tâm cách trục quay bao xa?
4. Liệt kê các đại lượng chưa biết và xác định những đại lượng cần tìm.
5. Vẽ sơ đồ lực cho phần dây ở phía ngoài điểm đang xét.
6. Dùng sơ đồ lực để tìm lực căng tại khoảng cách $r$.
7. Dùng kết quả bước 6 để tìm tốc độ sóng tại khoảng cách $r$.
8. Dùng kết quả bước 7 để tìm thời gian sóng truyền từ đầu này tới đầu kia. Gợi ý: Từ $v=dr/dt$, suy $dt=dr/v$ rồi lấy tích phân. Có thể ôn phép tích phân ở Phụ lục B.
9. Các kết quả ở (a), (b) có phù hợp dự đoán tại bước 1, 2 không? Đơn vị có đúng không?
10. Kiểm tra kết quả (a) bằng một đoạn dây nhỏ tại khoảng cách $r$, dài $dr$, có khối lượng $dm=(m/L)dr$. Hai phía đoạn ấy chịu các lực căng $F(r)$ và $F(r+dr)$. Lập phương trình cho $dF/dr$ rồi tích phân để tìm $F(r)$.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Dây thẳng theo phương bán kính, quay đều, có khối lượng riêng dài $\mu=m/L$. Xét $m>0$, $L>0$, $\omega>0$ và $0\le r\le L$. Sóng ngang đủ nhỏ để dùng tốc độ tại chỗ của dây căng trong trạng thái quay đã cho.

**Hướng đi:**

- Xét cả phần dây ngoài điểm cắt vì chỉ có một lực ngoài hướng tâm tác dụng lên phần ấy. Tổng gia tốc hướng tâm có thể tính từ khối lượng và vị trí khối tâm.
- Sau khi tìm lực căng biến thiên theo vị trí, dùng $v=\sqrt{F/\mu}$. Không dùng một tốc độ trung bình tùy ý cho cả dây.
- Cộng các thời gian vi phân $dt=dr/v(r)$. Tốc độ tiến về không ở đầu tự do đòi kiểm tra tích phân ở đầu mút.

**Lời giải:**

#### 1. Phác tình huống và dự đoán lực căng

Gọi đầu được giữ là $O$ và chọn chiều bán kính dương từ $O$ ra đầu tự do. Điểm đang xét ở tọa độ $r$, đầu tự do ở $L$. Tiết diện càng gần $O$ càng phải cung cấp lực hướng tâm cho nhiều dây ở phía ngoài.

![Sơ đồ lời giải: Phần (a) ghi đầu giữ O, điểm cắt r, đầu tự do L và phần dây ngoài điểm cắt. Phần (b) cho thấy phần dây ngoài chỉ chịu lực căng tại điểm cắt hướng về O, với khối tâm ở giữa r và L.](/vat-ly-1/bai-giang/img/young-15/bridge-15-rope.svg)

Vì vậy dự đoán lực căng lớn nhất ở đầu giữ và nhỏ nhất, bằng không, ở đầu tự do. Lực hướng tâm là vai trò của hợp lực, không phải một lực mới được thêm vào sơ đồ.

#### 2. Dự đoán tốc độ sóng

Với cùng $\mu$, tốc độ tăng theo căn bậc hai lực căng. Vì vậy dự đoán tốc độ lớn nhất gần đầu giữ và nhỏ nhất ở đầu tự do.

#### 3. Phần dây ngoài điểm cắt

Phần dây từ $r$ tới $L$ có chiều dài $L-r$. Gọi khối lượng của nó là $m_o$ và tọa độ khối tâm là $r_c$. Do dây đồng nhất,

$$
m_o=\mu(L-r),
$$

$$
r_c=\frac{L+r}{2}.
$$

Khi bỏ qua trọng lực, phần này chỉ chịu lực kéo của phần dây phía trong tại điểm cắt. Đầu tự do không chịu lực kéo từ một đoạn dây nằm xa hơn, vì không có đoạn như vậy.

#### 4. Các đại lượng cần tìm

Các đích là hàm lực căng $F(r)$, hàm tốc độ $v(r)$ và thời gian truyền $\tau$. Những đại lượng $m_o$, $r_c$ là các bước trung gian đã biểu diễn được theo dữ kiện và vị trí cắt.

#### 5. Sơ đồ lực và dấu của phương trình

Ở phần (b) của sơ đồ, lực căng hướng vào trong, ngược chiều bán kính dương. Khối tâm của phần dây ngoài chuyển động tròn đều nên gia tốc cũng hướng vào trong, có độ lớn $\omega^2r_c$.

Phương trình theo bán kính là

$$
-F(r)=-m_o\omega^2r_c.
$$

Không thêm “lực ly tâm” vào phương trình này, vì đang xét các lực thật và gia tốc trong hệ quán tính.

#### 6. Lực căng theo khoảng cách

Lấy độ lớn của hai vế rồi thay khối lượng và vị trí khối tâm,

$$
F(r)=m_o\omega^2r_c.
$$

Suy ra

$$
F(r)=\frac{\mu\omega^2}{2}(L^2-r^2).
$$

Với $\mu=m/L$, cũng có thể viết

$$
F(r)=\frac{m\omega^2}{2L}(L^2-r^2).
$$

Đây là đáp án phần (a). Lực căng không phải $m\omega^2r$ vì không thể gom toàn bộ dây thành một chất điểm ở chính vị trí cắt.

#### 7. Tốc độ sóng theo khoảng cách

Từ lực căng tại chỗ,

$$
\begin{aligned}
v(r)&=\sqrt{\frac{F(r)}\mu}\\
&=\frac\omega{\sqrt2}\sqrt{L^2-r^2}.
\end{aligned}
$$

Đó là đáp án phần (b). Khối lượng triệt tiêu vì khi tăng đều khối lượng riêng dài, cả lực căng cần cho chuyển động quay và quán tính của sóng đều tăng cùng tỷ lệ.

#### 8. Thời gian truyền

Trên một đoạn rất ngắn, thời gian truyền là

$$
dt=\frac{dr}{v(r)}.
$$

Đặt $r=L\sin\theta$ với $0\le\theta\le\pi/2$. Khi đó

$$
dr=L\cos\theta\,d\theta,
$$

$$
\frac{dr}{v(r)}=\frac{\sqrt2}\omega\,d\theta.
$$

Vì vậy

$$
\begin{aligned}
\tau&=\int_0^L\frac{dr}{v(r)}\\
&=\frac{\sqrt2}\omega\int_0^{\pi/2}d\theta\\
&=\frac\pi{\sqrt2\,\omega}.
\end{aligned}
$$

Đây là đáp án phần (c). Trong mô hình tốc độ tại chỗ này, thời gian từ đầu tự do vào đầu giữ cũng bằng thời gian theo chiều ngược lại.

Dù $v(r)$ tiến về không khi $r\to L$, tích phân thời gian vẫn hữu hạn. Phép đổi biến đã làm rõ điều đó. Không thay cả hành trình bằng tốc độ bằng không tại một điểm đầu mút. Ở đúng đầu không căng, mô hình sóng nhỏ trên dây căng được hiểu qua giới hạn từ phía trong dây.

#### 9. Đối chiếu dự đoán và đơn vị

Tại đầu giữ,

$$
F(0)=\frac12m\omega^2L,
$$

$$
v(0)=\frac{\omega L}{\sqrt2}.
$$

Cả hai đều giảm khi đi ra ngoài và tiến về không tại $r=L$, phù hợp dự đoán. Biểu thức $m\omega^2L$ có đơn vị lực, $\omega L$ có đơn vị tốc độ và $1/\omega$ có đơn vị thời gian.

Khi $\omega$ giảm về không, dây mất lực căng do quay và thời gian truyền tăng không giới hạn. Vì vậy kết quả thời gian được phát biểu với $\omega>0$.

#### 10. Kiểm tra bằng một đoạn vi phân

Xét đoạn từ $r$ tới $r+dr$, có khối lượng

$$
dm=\mu\,dr.
$$

Phần dây phía trong kéo nó vào với lực $F(r)$, còn phần phía ngoài kéo nó ra với lực $F(r+dr)$. Gọi hiệu lực theo chiều bán kính dương là

$$
\Delta F=F(r+dr)-F(r).
$$

Ở bậc nhất theo $dr$, gia tốc hướng tâm cho

$$
\Delta F=-\mu\omega^2r\,dr.
$$

Chia cho $dr$ và lấy giới hạn,

$$
\frac{dF}{dr}=-\mu\omega^2r.
$$

Dùng điều kiện biên $F(L)=0$, tích phân ngược từ đầu tự do được

$$
F(r)=\mu\omega^2\int_r^L s\,ds.
$$

Do đó

$$
F(r)=\frac{\mu\omega^2}{2}(L^2-r^2),
$$

đúng với kết quả đã tìm bằng cả phần dây ngoài. Dấu âm của đạo hàm thể hiện lực căng giảm theo bán kính.

</details>
