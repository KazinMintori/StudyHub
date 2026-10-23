### Bài tập cầu nối: Chuyển động của bi-a

Một bi-a là cầu đặc đồng chất khối lượng $m$, bán kính $R$, ban đầu đứng yên trên bàn ngang. Cơ đánh ngang với lực $F$ tại độ cao $h$ so với tâm trong thời gian ngắn $\Delta t$. Lực đánh lớn hơn nhiều lực ma sát bàn trong thời gian va chạm.

![Hình 10.37: Độ cao điểm đánh so với tâm quyết định xung lượng mômen mà cơ truyền cho bi-a.](./img/young-10/c-hinh-10-37.png)

(a) Cần chọn $h$ bằng bao nhiêu để bi lăn không trượt ngay sau cú đánh?

(b) Nếu đánh đúng tâm, tức $h=0$, bi trượt một thời gian trước khi lăn không trượt. Tốc độ khối tâm khi bắt đầu lăn bằng bao nhiêu?

Các điểm cần thực hiện khi lập lời giải:

1. Vẽ sơ đồ lực trong cú đánh, chọn trục và xác định lực cùng mômen xung lượng do cơ tạo ra.
2. Viết điều kiện giữa tốc độ khối tâm và tốc độ góc để không trượt ngay sau đánh.
3. Với cú đánh đúng tâm, phân biệt sơ đồ lực trong lúc đánh và trong lúc bi trượt sau đó.
4. Xác định tốc độ góc ban đầu và sự tăng, giảm của tốc độ dài, tốc độ góc trong giai đoạn trượt.
5. Dùng xung lượng và xung lượng mômen cho phần (a).
6. Suy ra độ cao đánh.
7. Với phần (b), lập các phương trình chuyển động trong giai đoạn ma sát trượt tác dụng.
8. Tìm thời điểm thỏa điều kiện không trượt và tốc độ tại thời điểm ấy.
9. Nếu có bàn bi-a, đối chiếu dự đoán định tính bằng quan sát cú đánh trên tâm và cú đánh đúng tâm.
10. Thay bi cầu bằng trụ rỗng thành mỏng và xét điểm đánh để không trượt ngay.

<details><summary>Xem lời giải chi tiết</summary>

**Tóm tắt đề bài:** Cầu có $I=2mR^2/5$. Đặt xung lượng của cú đánh $J=F\Delta t$, bỏ qua xung lượng ma sát trong thời gian rất ngắn ấy. Sau cú đánh đúng tâm, ma sát trượt có độ lớn $f=\mu_kmg$.

**Hướng đi:**

- Trong cú đánh, dùng biến thiên động lượng và mômen động lượng để tìm riêng tốc độ dài và tốc độ góc. Điểm đặt lực quyết định tỷ lệ giữa hai đại lượng.
- Sau cú đánh đúng tâm, ma sát ngược chiều trượt làm tốc độ khối tâm giảm nhưng làm tốc độ quay tăng.
- Dùng điều kiện $v=R\omega$ tại lúc hết trượt. Không áp dụng điều kiện ấy trước thời điểm này.

**Lời giải chi tiết:**

(a) Trong thời gian đánh, các lực gồm trọng lực, phản lực bàn, lực cơ và ma sát nhỏ có thể bỏ qua trong xung lượng. Lực ngang tác dụng ở trên tâm vừa đẩy bi đi vừa tạo mômen theo chiều lăn về phía trước.

Từ xung lượng tịnh tiến và xung lượng mômen:

$$
\begin{aligned}
mv&=J,\\
I\omega&=Jh.
\end{aligned}
$$

Muốn không trượt ngay, $v=R\omega$. Kết hợp ba quan hệ:

$$
h=\frac{I}{mR}=\frac25R.
$$

Cần đánh ở trên tâm một đoạn $2R/5$.

(b) Khi đánh đúng tâm, lực cơ không tạo mômen quanh tâm trong xấp xỉ xung lực đang dùng. Ngay sau đánh:

$$
\begin{aligned}
v_0&=J/m,\\
\omega_0&=0.
\end{aligned}
$$

Ở giai đoạn tiếp theo, chỉ còn ma sát ngang ngược chiều trượt tại tiếp điểm. Chọn chiều chuyển động ban đầu là dương và chiều góc lăn tương ứng là dương. Phương trình tịnh tiến và quay:

$$
\begin{aligned}
ma&=-f,\\
I\alpha&=fR.
\end{aligned}
$$

Suy ra $a=-\mu_kg$ và $\alpha=5\mu_kg/(2R)$. Tại thời gian $t$ sau cú đánh:

$$
\begin{aligned}
v(t)&=v_0-\mu_kgt,\\
\omega(t)&=\frac{5\mu_kg}{2R}t.
\end{aligned}
$$

Tiếp điểm hết trượt khi $v(t_*)=R\omega(t_*)$. Phương trình thời gian:

$$
v_0=\tfrac72\mu_kgt_*.
$$

Vì vậy:

$$
t_*=\frac{2v_0}{7\mu_kg}.
$$

Thay vào tốc độ dài:

$$
v_* =\frac57v_0=\frac{5J}{7m}.
$$

Tốc độ giảm, còn tốc độ góc tăng từ không đến $v_*/R$. Kết quả tốc độ cuối không phụ thuộc $\mu_k$ trong mô hình này, nhưng thời gian đạt trạng thái lăn thì phụ thuộc.

Để kiểm tra trường hợp trụ rỗng thành mỏng, thay $I=mR^2$ vào điều kiện phần (a). Khi ấy $h=R$, nghĩa là phải tác dụng lực ngang ở đỉnh trụ để bắt đầu lăn không trượt ngay sau cú đánh.

</details>
